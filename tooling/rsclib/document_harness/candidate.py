"""Payload-candidate observation: tree readers, the artifact manifest and the record.

Git vocabulary lives here and in nothing else. This is the adaptation of the v1/v2 Git
path/diff primitive: the exact-base diff and the segment-boundary path comparison are
carried over; the enforcement-level vocabulary and lease logic of the v2 adapter are
stripped, not carried, because v3's boundary is an **acceptance** boundary and never claims
to have prevented a write (V3-D3).

Two rules shape everything below.

**The candidate is a commit, not the working tree.** A payload candidate C is an exact
commit on an isolated branch. Reading a file "from the candidate" therefore means reading it
out of that commit with ``git show``, never off disk — the working tree is mutable, may
contain the control root, and can drift from C between the moment C was written and the
moment a check runs. Both readers below record which tree they are, so every result can say
what it actually observed.

**Payload and evidence never share identity.** The control root E(C) holds the state, the
plan, this record, the checks and the coverage view; none of it may appear inside the payload
candidate's own change set (V3-D9, N1-A5). A control file written into the payload is not a
tidiness problem — it means the candidate under review contains the evidence about itself.
"""
from __future__ import annotations

import contextlib
import dataclasses
import pathlib
import shutil
import subprocess
import tempfile
from typing import Any, Iterable, Iterator, Mapping, Sequence

from rsclib.document_harness import (
    AssuranceFault,
    Issue,
    Report,
    report_of,
    validate,
)

CODE = "V3-CANDIDATE"

#: `git diff --name-status` letters that v3 understands. Renames and copies are disabled at
#: the call site (`--no-renames`) so a moved file is observed honestly as a delete plus an
#: add, rather than as a single change whose old path silently disappears.
_STATUS_MAP = {"A": "added", "M": "modified", "D": "deleted", "T": "modified"}


def git(repo_root: pathlib.Path | str, *args: str) -> str:
    """Run one read-only git command. A git failure is a tooling fault, not a verdict."""
    completed = subprocess.run(
        ["git", "-C", str(repo_root), *args],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        errors="replace",
    )
    if completed.returncode:
        detail = completed.stderr.strip() or completed.stdout.strip() or f"exit {completed.returncode}"
        raise AssuranceFault(f"git {' '.join(args)} failed: {detail}")
    return completed.stdout


def head_revision(repo_root: pathlib.Path | str) -> str:
    return git(repo_root, "rev-parse", "HEAD").strip()


# ---------------------------------------------------------------------------
# Tree readers
# ---------------------------------------------------------------------------


class TreeReader:
    """A read-only view of one tree, which always knows which tree it is."""

    kind: str = "worktree"

    def __init__(self, repo_root: pathlib.Path | str, revision: str) -> None:
        self.repo_root = pathlib.Path(repo_root)
        self.revision = revision

    def read(self, path: str) -> bytes | None:  # pragma: no cover - interface
        raise NotImplementedError

    def exists(self, path: str) -> bool:
        return self.read(path) is not None

    def observed_tree(self) -> dict[str, str]:
        """The R1 disclosure every CheckResult carries."""
        return {"kind": self.kind, "revision": self.revision}


class CandidateTreeReader(TreeReader):
    """Reads the exact payload candidate commit — the only tree that certifies a candidate."""

    kind = "candidate_commit"

    def read(self, path: str) -> bytes | None:
        completed = subprocess.run(
            ["git", "-C", str(self.repo_root), "show", f"{self.revision}:{path}"],
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if completed.returncode:
            return None
        return completed.stdout


class WorktreeReader(TreeReader):
    """Reads the mutable working tree.

    Its `revision` is the HEAD at observation time, which does **not** certify the bytes
    that were read: an uncommitted edit is invisible to that revision. Results observed
    through this reader are never candidate evidence.
    """

    kind = "worktree"

    def __init__(self, repo_root: pathlib.Path | str, revision: str | None = None) -> None:
        super().__init__(repo_root, revision or head_revision(repo_root))

    def read(self, path: str) -> bytes | None:
        target = self.repo_root / path
        if not target.is_file():
            return None
        return target.read_bytes()


def reader_for(tree_kind: str, repo_root: pathlib.Path | str, revision: str) -> TreeReader:
    if tree_kind == "candidate_commit":
        return CandidateTreeReader(repo_root, revision)
    if tree_kind == "worktree":
        return WorktreeReader(repo_root)
    raise AssuranceFault(f"unknown tree kind: {tree_kind}")


# ---------------------------------------------------------------------------
# Candidate materialization — how a process gets to observe the candidate commit
# ---------------------------------------------------------------------------


@contextlib.contextmanager
def materialized_candidate(
    repo_root: pathlib.Path | str, revision: str
) -> Iterator[pathlib.Path]:
    """A disposable checkout of the exact candidate commit, for a process to run against.

    ``git show`` serves the readers above one file at a time, but a *process* (the
    ``command_exit`` check kind) needs the candidate's files on disk. Checking out the
    candidate in the main working tree would clobber uncommitted work — this repository has
    an incident — so the candidate is materialized into a private temporary Git worktree
    that shares the repository's object store, and the caller's command runs there.

    **What this establishes, exactly:** the process ran against a tree Git built from that
    commit. Nothing else. It does *not* establish that the process left the tree alone — a
    command is free to write, delete, commit or ``git checkout`` inside its own
    materialization. The gap cannot be closed from here: no comparison of end state can
    recover what a process read while running, since a file modified, read and restored
    mid-run is byte-identical afterwards. That is a permanent endpoint, not debt; do not
    schedule work against it. What a check's command actually does is settled where the
    command is chosen — the WorkSpec author writes the argv, and review reads it
    (`REVIEW.md`'s `review_only` question). An earlier revision of this function carried a
    post-run drift check that claimed to close the gap; four evasions were demonstrated
    against it, one of them unclosable, and the claim was the defect.

    **The materialization is a checkout, not the stored bytes.** ``git worktree add``
    applies the repository's eol/filter configuration, so under ``core.autocrlf=true``
    (this repository) a subject stored with LF endings is written out with CRLF. The
    ``subjects[].digest_sha256`` on the same CheckResult is computed from the Git object
    instead, so a byte-exact comparison must read Git objects rather than the file system.

    Materialization failure raises ``AssuranceFault`` (a tooling fault, never a verdict).
    Cleanup is best-effort: a stale worktree entry cannot corrupt evidence — it only
    occupies disk — so a cleanup failure never overturns an outcome already honestly
    observed. It removes this worktree by path and nothing else; a repository-wide
    ``git worktree prune`` would deregister any *other* worktree whose directory happened
    to be missing at that moment, and this repository has a second live one.
    """
    parent = pathlib.Path(tempfile.mkdtemp(prefix="v3-candidate-"))
    target = parent / "tree"
    try:
        git(repo_root, "worktree", "add", "--detach", str(target), revision)
        yield target
    finally:
        subprocess.run(
            ["git", "-C", str(repo_root), "worktree", "remove", "--force", str(target)],
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        shutil.rmtree(parent, ignore_errors=True)


# ---------------------------------------------------------------------------
# Path algebra — normalized local paths only, no URI or glob algebra (V3-D3)
# ---------------------------------------------------------------------------


def _normalize(path: str) -> str:
    return path.replace("\\", "/").strip("/").casefold()


def covered_by(path: str, prefixes: Iterable[str]) -> bool:
    """Segment-boundary containment: `a/b` covers `a/b` and `a/b/c`, never `a/bc`."""
    key = _normalize(path)
    for prefix in prefixes:
        norm = _normalize(prefix)
        if norm and (key == norm or key.startswith(norm + "/")):
            return True
    return False


def evaluate_boundary(
    changes: Sequence[Mapping[str, Any]], boundary: Mapping[str, Any]
) -> tuple[str, list[str]]:
    """Classify an observed change set against the effective boundary (invariant 6).

    A path conforms only if it is inside `write_scope` **and** outside every `out` entry —
    the negative boundary wins, so a profile-materialized constraint can only tighten.
    """
    offenders = [
        change["path"]
        for change in changes
        if not covered_by(change["path"], boundary["write_scope"])
        or covered_by(change["path"], boundary["out"])
    ]
    unique = sorted(set(offenders))
    return ("NONCONFORMANT" if unique else "CONFORMANT"), unique


def resolve_locator(reader: TreeReader, locator: Mapping[str, Any]) -> int:
    """How many times the locator's anchor occurs in its file, in the observed tree.

    A locator resolves only when the count is exactly 1. Zero means the claim points at
    nothing (the stale-locator failure class); more than one means the anchor is ambiguous,
    so it does not identify a location either (plan §5.3).
    """
    raw = reader.read(locator["path"])
    if raw is None:
        return 0
    return raw.decode("utf-8", errors="replace").count(locator["anchor"])


# ---------------------------------------------------------------------------
# Observation
# ---------------------------------------------------------------------------


def observe_changes(
    repo_root: pathlib.Path | str, base_revision: str, candidate_revision: str
) -> list[dict[str, str]]:
    """Every actual add/modify/delete between the exact base and the exact candidate."""
    raw = git(
        repo_root,
        "diff",
        "--no-renames",
        "--name-status",
        base_revision,
        candidate_revision,
    )
    changes: list[dict[str, str]] = []
    for line in raw.splitlines():
        if not line.strip():
            continue
        status, _, path = line.partition("\t")
        letter = status.strip()[:1]
        if letter not in _STATUS_MAP:
            raise AssuranceFault(f"unhandled git status letter '{status}' for {path}")
        changes.append({"path": path.strip().replace("\\", "/"), "change_kind": _STATUS_MAP[letter]})
    return sorted(changes, key=lambda change: change["path"])


def observe_manifest(
    repo_root: pathlib.Path | str,
    base_revision: str,
    candidate_revision: str,
    boundary: Mapping[str, Any],
    expected_artifacts: Sequence[Mapping[str, Any]],
    *,
    authored_by: str,
    authored_at: str | None = None,
) -> dict[str, Any]:
    """Produce the manifest partition. Sole author: the deterministic diff verifier.

    Expected-artifact presence is observed in the **candidate tree**, not in the diff: an
    artifact that already existed at the base and was left unchanged is present but absent
    from the change set, and reporting it missing would be a false blocker.
    """
    changes = observe_changes(repo_root, base_revision, candidate_revision)
    result, offenders = evaluate_boundary(changes, boundary)
    reader = CandidateTreeReader(repo_root, candidate_revision)

    manifest: dict[str, Any] = {
        "authored_by": authored_by,
        "boundary_result": result,
        "expected_artifact_results": [
            {"artifact_id": artifact["artifact_id"], "present": reader.exists(artifact["path"])}
            for artifact in expected_artifacts
        ],
    }
    if authored_at:
        manifest["authored_at"] = authored_at
    if changes:
        manifest["changes"] = changes
    if offenders:
        manifest["out_of_boundary_paths"] = offenders
    return manifest


def build_record(
    *,
    record_id: str,
    work_id: str,
    run_id: str,
    repair_round: int,
    candidate_ref: Mapping[str, Any],
    base_revision: str,
    control_root: str,
    fulfillment: Mapping[str, Any],
    manifest: Mapping[str, Any],
) -> dict[str, Any]:
    """Assemble the controller envelope around the two owner-authored partitions."""
    return {
        "record_id": record_id,
        "work_id": work_id,
        "run_id": run_id,
        "repair_round": repair_round,
        "candidate_ref": dict(candidate_ref),
        "base_revision": base_revision,
        "control_root": control_root,
        "fulfillment": dict(fulfillment),
        "manifest": dict(manifest),
    }


# ---------------------------------------------------------------------------
# Invariants
# ---------------------------------------------------------------------------


@dataclasses.dataclass(frozen=True)
class LocatorFinding:
    obligation_id: str
    locator: dict[str, Any]
    matches: int


def check_record(record: Mapping[str, Any], spec: Mapping[str, Any]) -> Report:
    """Every invariant this record can be judged against without reading a tree."""
    schema_report = validate("candidate", record)
    if not schema_report.ok:
        return schema_report

    issues: list[Issue] = []
    fulfillment = record["fulfillment"]
    manifest = record["manifest"]

    if record["work_id"] != spec["work_id"]:
        issues.append(Issue(f"{CODE}-WORK-MISMATCH", "record names a different work_id", "work_id"))

    # --- N1-A7: the diff verifier alone owns the manifest ---
    executor = fulfillment["authored_by"].strip().casefold()
    if manifest["authored_by"].strip().casefold() == executor:
        issues.append(
            Issue(
                f"{CODE}-EXECUTOR-AUTHORED-MANIFEST",
                f"the manifest was authored by the executor of the same run: "
                f"{fulfillment['authored_by']}",
                "manifest/authored_by",
            )
        )

    # --- invariant 2: exactly one claim per obligation, no more and no fewer ---
    declared = {ob["obligation_id"] for ob in spec["obligations"]}
    claimed: list[str] = [claim["obligation_id"] for claim in fulfillment["claims"]]
    for missing in sorted(declared - set(claimed)):
        issues.append(
            Issue(
                f"{CODE}-OBLIGATION-OMITTED",
                f"no fulfillment claim for obligation: {missing}",
                "fulfillment/claims",
            )
        )
    for unknown in sorted(set(claimed) - declared):
        issues.append(
            Issue(
                f"{CODE}-UNDECLARED-CLAIM",
                f"claim for an obligation the WorkSpec never declared: {unknown}",
                "fulfillment/claims",
            )
        )
    for obligation_id in sorted({name for name in claimed if claimed.count(name) > 1}):
        issues.append(
            Issue(
                f"{CODE}-DUPLICATE-CLAIM",
                f"obligation claimed more than once: {obligation_id}",
                "fulfillment/claims",
            )
        )

    # --- invariant 7: every expected artifact is present or explicitly missing ---
    expected = {artifact["artifact_id"] for artifact in spec["expected_artifacts"]}
    reported = {entry["artifact_id"] for entry in manifest["expected_artifact_results"]}
    for missing in sorted(expected - reported):
        issues.append(
            Issue(
                f"{CODE}-ARTIFACT-UNREPORTED",
                f"expected artifact has no presence result: {missing}",
                "manifest/expected_artifact_results",
            )
        )
    for unknown in sorted(reported - expected):
        issues.append(
            Issue(
                f"{CODE}-ARTIFACT-UNDECLARED",
                f"presence reported for an artifact the WorkSpec never declared: {unknown}",
                "manifest/expected_artifact_results",
            )
        )
    for entry in manifest["expected_artifact_results"]:
        if not entry["present"]:
            issues.append(
                Issue(
                    f"{CODE}-ARTIFACT-MISSING",
                    f"declared expected artifact is absent from the candidate: {entry['artifact_id']}",
                    "manifest/expected_artifact_results",
                )
            )

    # --- N1-A5: no control file inside the payload candidate ---
    control_root = record["control_root"]
    for change in manifest.get("changes", []):
        if covered_by(change["path"], [control_root]):
            issues.append(
                Issue(
                    f"{CODE}-CONTROL-FILE-IN-PAYLOAD",
                    f"assurance evidence was written into the payload candidate: {change['path']}",
                    "manifest/changes",
                )
            )

    # --- invariant 6: an out-of-boundary delta is NONCONFORMANT, and it must be a real path ---
    change_paths = {change["path"] for change in manifest.get("changes", [])}
    for path in manifest.get("out_of_boundary_paths", []):
        if path not in change_paths:
            issues.append(
                Issue(
                    f"{CODE}-OFFENDER-NOT-OBSERVED",
                    f"out-of-boundary path is not in the observed change set: {path}",
                    "manifest/out_of_boundary_paths",
                )
            )
    if manifest["boundary_result"] == "NONCONFORMANT":
        issues.append(
            Issue(
                f"{CODE}-BOUNDARY-NONCONFORMANT",
                "the observed change set falls outside the effective acceptance boundary: "
                + ", ".join(manifest.get("out_of_boundary_paths", [])),
                "manifest/boundary_result",
            )
        )

    return schema_report + report_of(issues)


def check_locators(record: Mapping[str, Any], reader: TreeReader) -> Report:
    """Invariant 3: an `IMPLEMENTED` claim needs a locator that actually resolves.

    A claim is not evidence. This is the check that separates "the executor says it did the
    work" from "the work is at a locatable place in this exact candidate", and it must read
    the candidate tree — reading the working tree here would certify bytes the candidate
    does not contain (R1).
    """
    issues: list[Issue] = []
    if reader.kind != "candidate_commit":
        return report_of(
            [
                Issue(
                    f"{CODE}-WRONG-SUBJECT",
                    f"locator resolution observed the {reader.kind}, which does not certify "
                    "the payload candidate",
                    "fulfillment/claims",
                )
            ]
        )

    for claim in record["fulfillment"]["claims"]:
        if claim["status"] != "IMPLEMENTED":
            continue
        for locator in claim.get("implementation_locators", []):
            matches = resolve_locator(reader, locator)
            if matches == 1:
                continue
            reason = "does not resolve" if matches == 0 else f"is ambiguous ({matches} matches)"
            issues.append(
                Issue(
                    f"{CODE}-LOCATOR-UNRESOLVED",
                    f"implementation locator {reason}: {locator['path']} :: {locator['anchor']}",
                    f"fulfillment/claims/{claim['obligation_id']}",
                )
            )
    return report_of(issues)
