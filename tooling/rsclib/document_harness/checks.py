"""The closed deterministic check union and its results (plan §5.3, N1-A8).

V3 is not a tool plug-in framework. Six kinds exist, they are enumerated in the signed
contract, and an unknown kind is a `SPEC_GAP` that stops the run — never an invitation to
discover a tool at runtime.

Two disciplines are enforced here rather than trusted.

**Subject-tree discipline.** Every result records which tree it observed.
Five of the six kinds make a claim *about the payload candidate*, so they must observe the
candidate commit; a request that declares the working tree gets `WRONG_SUBJECT`, never
`PASS`, because an outcome read off mutable files says nothing about the candidate.
`command_exit` is the exception only in mechanism: a process runs against files on disk, so
a command that claims to observe the candidate runs inside a disposable materialization of
the exact candidate commit (a Git worktree), never against the mutable checkout. What that
buys, and what it does not, is stated precisely in `materialized_candidate` — the process
ran against a tree built from that commit, and *not* that it left the tree alone. A command
that declares the working tree runs in the working tree and its result says so, which
certifies nothing about the candidate.

**Ownership discipline (V3-D5).** A CheckResult belongs to the verifier that produced it.
The raw output is written out and referenced; the structured result never restates it with
stronger meaning, and the executor can never author one.

The governance-frontmatter scan at the bottom is the mechanical form of a rule the contract
and plan already state in prose — that an approval-bearing document never carries its own
approval status. It is reached through `command_exit`, deliberately: adding a seventh check
kind would contradict the signed closed union (contract §5).
"""
from __future__ import annotations

import dataclasses
import hashlib
import json
import pathlib
import re
import subprocess
from typing import Any, Mapping, Sequence

from jsonschema import Draft202012Validator

from rsclib.document_harness import (
    Issue,
    Report,
    SpecGap,
    bytes_digest,
    canonical_digest,
    report_of,
    validate,
)
from rsclib.document_harness.candidate import (
    TreeReader,
    evaluate_boundary,
    materialized_candidate,
    observe_changes,
    reader_for,
    resolve_locator,
)

CODE = "V3-CHECK"

#: Kinds whose claim is *about the payload candidate*. Observing anything else is a
#: wrong-subject defect, not a softer result (V3-D5).
CANDIDATE_SUBJECT_KINDS = frozenset(
    {"file_exists", "json_schema", "markdown_link", "locator_exists", "git_diff_boundary"}
)

_MD_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
#: A top-level frontmatter key, in each of YAML's three spellings of the same key: bare,
#: single-quoted, double-quoted. The backreference forces the quotes to match, so a mismatched
#: pair is not read as a key — it is not valid YAML either. Anchoring on the bare form alone
#: was a complete bypass: `"approved_by": someone` parsed to no key and the whole governance
#: scan reported the document clean.
_FRONTMATTER_KEY = re.compile(r"^([\"']?)([A-Za-z_][A-Za-z0-9_-]*)\1\s*:")


@dataclasses.dataclass(frozen=True)
class CheckContext:
    """Everything a check binds at run time and therefore never duplicates in its request."""

    repo_root: pathlib.Path
    candidate_ref: Mapping[str, Any]
    base_revision: str
    boundary: Mapping[str, Any]
    verified_by: str
    artifact_paths: Mapping[str, str] = dataclasses.field(default_factory=dict)
    evidence_dir: str | None = None
    verified_at: str | None = None
    exemptions_path: str | None = None

    @property
    def candidate_revision(self) -> str:
        commit = self.candidate_ref.get("commit")
        if not commit:
            raise SpecGap(
                f"{CODE}-UNBOUND-CANDIDATE the candidate has no exact commit; a check cannot "
                "certify a branch name"
            )
        return commit


def require_supported_kind(kind: str) -> None:
    """An unknown kind is a `SPEC_GAP` and stops the run (N1-A8).

    It cannot even be recorded as a result: the result schema's `kind` is the same closed
    enum, so an unrecognised kind has no representable outcome. That is the intended shape
    — v3 refuses to produce a verdict about a request it does not understand.
    """
    from rsclib.document_harness import SCHEMA_DIR, load_json

    known = load_json(SCHEMA_DIR / "common.schema.json")["$defs"]["checkKind"]["enum"]
    if kind not in known:
        raise SpecGap(f"{CODE}-UNKNOWN-KIND unknown check kind '{kind}'; the union is closed")


# ---------------------------------------------------------------------------
# Result construction
# ---------------------------------------------------------------------------


def _result(
    check: Mapping[str, Any],
    ctx: CheckContext,
    reader: TreeReader | None,
    outcome: str,
    detail: str | None = None,
    **extra: Any,
) -> dict[str, Any]:
    result: dict[str, Any] = {
        "result_id": f"{check['check_id']}-r"[:64],
        "check_id": check["check_id"],
        "kind": check["kind"],
        "request_digest_sha256": canonical_digest(check),
        "candidate_ref": dict(ctx.candidate_ref),
        "observed_tree": (
            reader.observed_tree()
            if reader
            else {"kind": check["subject_tree"], "revision": ctx.candidate_revision}
        ),
        "result": outcome,
        "verified_by": ctx.verified_by,
    }
    if detail:
        result["detail"] = detail[:2000]
    if ctx.verified_at:
        result["verified_at"] = ctx.verified_at
    result.update({key: value for key, value in extra.items() if value is not None})
    if "subjects" in result:
        result["subjects"] = _dedupe_subjects(result["subjects"])
    return result


def _dedupe_subjects(subjects: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    """Collapse repeated observations of one path into one subject, preserving order.

    A request may legitimately name the same path twice — a `json_schema` check whose
    subject and schema paths coincide, for instance. That is one subject observed once, and
    emitting it twice would both overstate the observation and violate the result schema's
    `uniqueItems`, turning a degenerate-but-valid request into a crash instead of a reported
    outcome.
    """
    seen: list[dict[str, Any]] = []
    for subject in subjects:
        entry = dict(subject)
        if entry not in seen:
            seen.append(entry)
    return seen


def _subject(path: str, reader: TreeReader | None) -> dict[str, Any]:
    subject: dict[str, Any] = {"path": path}
    if reader is not None:
        subject["revision"] = reader.revision
        raw = reader.read(path)
        if raw is not None:
            subject["digest_sha256"] = bytes_digest(raw)
    return subject


def _write_evidence(ctx: CheckContext, check_id: str, text: str) -> dict[str, Any] | None:
    if not ctx.evidence_dir:
        return None
    rel = f"{ctx.evidence_dir.rstrip('/')}/{check_id}.out.txt"
    target = ctx.repo_root / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(text.encode("utf-8"))
    # Path only. The file was produced by this run a line earlier, so a digest taken here
    # is this run attesting to its own output — it detects nothing the run itself did, and
    # `pointerRef` requires only `path` (2026-07-29 narrowing; digests are kept where the
    # writer is not the file's legitimate author, `assurance_state.DIGEST_PROTECTED_FIELDS`).
    return {"path": rel}


# ---------------------------------------------------------------------------
# The six oracles
# ---------------------------------------------------------------------------


def _check_file_exists(check, ctx, reader):
    artifact_id = check["config"]["artifact_id"]
    path = ctx.artifact_paths.get(artifact_id)
    if not path:
        return _result(
            check, ctx, reader, "SPEC_GAP",
            f"artifact '{artifact_id}' is not declared by the WorkSpec, so the subject cannot be resolved",
        )
    present = reader.exists(path)
    return _result(
        check, ctx, reader,
        "PASS" if present else "FAIL",
        None if present else f"declared artifact is absent from the candidate: {path}",
        subjects=[_subject(path, reader)],
    )


def _check_json_schema(check, ctx, reader):
    config = check["config"]
    subject_raw = reader.read(config["subject_path"])
    schema_raw = reader.read(config["schema_path"])
    subjects = [_subject(config["subject_path"], reader), _subject(config["schema_path"], reader)]
    if subject_raw is None or schema_raw is None:
        missing = config["subject_path"] if subject_raw is None else config["schema_path"]
        return _result(check, ctx, reader, "SPEC_GAP", f"declared subject not found in the observed tree: {missing}", subjects=subjects)
    try:
        document = json.loads(subject_raw.decode("utf-8"))
        schema = json.loads(schema_raw.decode("utf-8"))
        Draft202012Validator.check_schema(schema)
    except Exception as exc:
        return _result(check, ctx, reader, "SPEC_GAP", f"subject or schema could not be parsed: {exc}", subjects=subjects)
    errors = sorted(Draft202012Validator(schema).iter_errors(document), key=lambda e: list(e.path))
    if not errors:
        return _result(check, ctx, reader, "PASS", subjects=subjects)
    first = errors[0]
    where = "/".join(str(part) for part in first.path) or "<root>"
    return _result(
        check, ctx, reader, "FAIL",
        f"{len(errors)} schema error(s); first at {where}: {first.message}",
        subjects=subjects,
    )


def _local_links(text: str) -> list[str]:
    links = []
    for target in _MD_LINK.findall(text):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        links.append(target.split("#", 1)[0])
    return [link for link in links if link]


def _check_markdown_link(check, ctx, reader):
    broken: list[str] = []
    subjects = []
    for subject_path in check["config"]["subject_paths"]:
        raw = reader.read(subject_path)
        subjects.append(_subject(subject_path, reader))
        if raw is None:
            return _result(check, ctx, reader, "SPEC_GAP", f"declared subject not found in the observed tree: {subject_path}", subjects=subjects)
        base = pathlib.PurePosixPath(subject_path).parent
        for link in _local_links(raw.decode("utf-8", errors="replace")):
            resolved = (base / link) if not link.startswith("/") else pathlib.PurePosixPath(link.lstrip("/"))
            collapsed = _collapse(resolved.parts)
            if collapsed and collapsed[0] == "..":
                broken.append(f"{subject_path} -> {link} (resolves outside the repository)")
                continue
            if not reader.exists(str(pathlib.PurePosixPath(*collapsed))):
                broken.append(f"{subject_path} -> {link}")
    if not broken:
        return _result(check, ctx, reader, "PASS", subjects=subjects)
    return _result(check, ctx, reader, "FAIL", f"{len(broken)} unresolved local link(s): " + "; ".join(broken[:20]), subjects=subjects)


def _collapse(parts: Sequence[str]) -> list[str]:
    """Resolve `.` and `..` textually, leaving any escape from the tree *visible*.

    A `..` only cancels a real name. Cancelling one against another leading `..` would fold
    a path that climbs above the repository root back inside it — the earlier defect, where
    `../../../README.md` from `docs/guide.md` normalized to the root's own `README.md` and
    the link check passed. The caller reads a leading `..` as unresolvable; it is the one
    outcome that must never be silently rewritten into a resolvable one.
    """
    out: list[str] = []
    for part in parts:
        if part == ".":
            continue
        if part == "..":
            if out and out[-1] != "..":
                out.pop()
            else:
                out.append("..")
            continue
        out.append(part)
    return out


def _check_locator_exists(check, ctx, reader):
    locator = check["config"]["locator"]
    matches = resolve_locator(reader, locator)
    subjects = [_subject(locator["path"], reader)]
    if matches == 1:
        return _result(check, ctx, reader, "PASS", subjects=subjects)
    reason = "does not resolve" if matches == 0 else f"is ambiguous ({matches} matches)"
    return _result(
        check, ctx, reader, "FAIL",
        f"locator {reason}: {locator['path']} :: {locator['anchor']}",
        subjects=subjects,
    )


def _check_git_diff_boundary(check, ctx, reader):
    changes = observe_changes(ctx.repo_root, ctx.base_revision, ctx.candidate_revision)
    outcome, offenders = evaluate_boundary(changes, ctx.boundary)
    return _result(
        check, ctx, reader,
        "PASS" if outcome == "CONFORMANT" else "FAIL",
        None if outcome == "CONFORMANT" else f"{len(offenders)} path(s) outside the acceptance boundary: " + ", ".join(offenders[:20]),
        boundary_observed={"write_scope": list(ctx.boundary["write_scope"]), "out": list(ctx.boundary["out"])},
        base_revision=ctx.base_revision,
        subjects=[{"path": change["path"]} for change in changes] or None,
    )


def _check_command_exit(check, ctx, reader):
    """Run the command against the tree the request declared.

    `candidate_commit` never means the checkout: the exact candidate is materialized into a
    disposable Git worktree and the process runs there, so the declaration is satisfied by
    construction rather than by demanding that the checkout already be the candidate — the
    demand the same-branch evidence-commit topology could never meet. What the
    materialization does and does not establish is stated in `materialized_candidate`;
    this function adds no claim beyond it. `worktree` runs in the working tree, whose
    result certifies no candidate.
    """
    if check["subject_tree"] != "candidate_commit":
        return _run_command(check, ctx, reader, ctx.repo_root)

    with materialized_candidate(ctx.repo_root, ctx.candidate_revision) as materialized_root:
        return _run_command(check, ctx, reader, materialized_root)


#: Wall-clock ceiling for one `command_exit` process, in seconds. Deliberately a module
#: constant and not a request field: a per-request knob would let the request that hangs buy
#: its own patience, and the ceiling exists precisely because no request can be trusted to
#: bound itself. It is generous rather than tuned — its job is to end an unbounded wait, not
#: to enforce a performance budget.
COMMAND_TIMEOUT_SECONDS = 600


def _run_command(check, ctx, reader, exec_root):
    """One process execution against `exec_root`; evidence always lands in the main repo.

    A process that never returns is a `SPEC_GAP`, never a `FAIL`. The result schema requires
    an exact `exit_code` on every `command_exit` PASS or FAIL, and a process killed at the
    ceiling produced none; naming one would invent evidence the run never observed. `SPEC_GAP`
    is the vocabulary's word for *no verdict was produced*, and it stops the run, which is
    what an unbounded command deserves. Whatever the process managed to write before the kill
    is still recorded — partial output is evidence too.
    """
    config = check["config"]
    cwd = pathlib.Path(exec_root) / config["cwd"]
    if not cwd.is_dir():
        return _result(
            check, ctx, reader, "SPEC_GAP",
            f"declared cwd does not exist in the observed tree: {config['cwd']}",
        )
    try:
        completed = subprocess.run(
            list(config["argv"]),
            cwd=str(cwd),
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            encoding="utf-8",
            errors="replace",
            timeout=COMMAND_TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired as expired:
        return _result(
            check, ctx, reader, "SPEC_GAP",
            f"declared command did not finish within {COMMAND_TIMEOUT_SECONDS}s and was killed; "
            "a killed process has no exit code, so no verdict is representable",
            evidence_ref=_write_evidence(ctx, check["check_id"], expired.output or ""),
        )
    evidence = _write_evidence(ctx, check["check_id"], completed.stdout or "")
    allowed = completed.returncode in config["allowed_exit_codes"]
    subjects = [_subject(path, reader) for path in config.get("subject_paths", [])] or None
    return _result(
        check, ctx, reader,
        "PASS" if allowed else "FAIL",
        None if allowed else f"exit {completed.returncode} is not in {config['allowed_exit_codes']}",
        exit_code=completed.returncode,
        evidence_ref=evidence,
        subjects=subjects,
    )


_ORACLES = {
    "file_exists": _check_file_exists,
    "json_schema": _check_json_schema,
    "markdown_link": _check_markdown_link,
    "locator_exists": _check_locator_exists,
    "git_diff_boundary": _check_git_diff_boundary,
    "command_exit": _check_command_exit,
}


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------


def _wrong_subject(check: Mapping[str, Any], ctx: CheckContext) -> dict[str, Any] | None:
    """The subject-tree ruling, or None when the request may observe what it declared.

    `command_exit` is not ruled here: a candidate-declared command is *honoured* by running
    it inside a materialization of the exact candidate commit (`_check_command_exit`), so
    there is no checkout state under which its declaration cannot be satisfied.
    """
    declared_tree = check["subject_tree"]

    if check["kind"] in CANDIDATE_SUBJECT_KINDS and declared_tree != "candidate_commit":
        return _result(
            check, ctx, reader_for(declared_tree, ctx.repo_root, ctx.candidate_revision),
            "WRONG_SUBJECT",
            f"a {check['kind']} check speaks about the payload candidate but declared the "
            f"{declared_tree}; its outcome would not certify the candidate",
        )

    return None


def run_check(check: Mapping[str, Any], ctx: CheckContext) -> dict[str, Any]:
    """Run one check and return its CheckResult. Never raises for a *failing* subject.

    Every path leaves through the single validation below. An earlier version returned the
    wrong-subject ruling directly and skipped validation, which let a schema-invalid result
    escape unnoticed — the defect was invisible precisely because the unvalidated path was
    the one that never ran the check.
    """
    require_supported_kind(check.get("kind", ""))
    validate("check", check).require(SpecGap)

    result = _wrong_subject(check, ctx)
    if result is None:
        reader = reader_for(check["subject_tree"], ctx.repo_root, ctx.candidate_revision)
        result = _ORACLES[check["kind"]](check, ctx, reader)

    validate("check_result", result).require(SpecGap)
    return result


def run_all(
    checks: Mapping[str, Mapping[str, Any]],
    order: Sequence[str],
    ctx: CheckContext,
) -> list[dict[str, Any]]:
    """Run the resolved checks in the plan's deterministic order.

    A `SPEC_GAP` result is produced first and then stops the run *immediately*: the evidence
    that the request was uninterpretable is itself worth keeping (plan §8), and nothing after
    it may run. The earlier version collected the gap and finished the order anyway, so every
    later check — `command_exit` among them, which starts a real process against real files —
    still executed under a plan already known to be uninterpretable. Stopping late is not a
    slower stop; it is a different thing happening.
    """
    results: list[dict[str, Any]] = []
    for check_id in order:
        check = checks.get(check_id)
        if check is None:
            raise SpecGap(f"{CODE}-MISSING-REQUEST no LocalCheckSpec found for check id '{check_id}'")
        result = run_check(check, ctx)
        results.append(result)
        if result["result"] == "SPEC_GAP":
            raise SpecGap(f"{CODE}-SPEC-GAP uninterpretable check request: {result['check_id']}")
    return results


# ---------------------------------------------------------------------------
# Governance-frontmatter scan
# ---------------------------------------------------------------------------

GOVERNANCE_CODE = "V3-GOVERNANCE"

#: Exact frontmatter field names that make a document carry its own approval state. Matching
#: is by exact field name and never by substring: `approval_status_owner` and
#: `signature_owner` are the *correct* pattern — they name who owns the approval without
#: carrying it — and a substring rule would turn the correct pattern into a false positive.
#: False positives are how a real check gets switched off.
SELF_APPROVAL_FIELDS = frozenset(
    {
        "status",
        "approval_status",
        "approved",
        "approved_by",
        "approved_at",
        "signed",
        "signature",
        "signed_by",
        "digest",
        "self_digest",
        "content_digest",
        "sha256",
    }
)

#: Suffix that marks the delegating form, whitelisted explicitly.
OWNER_SUFFIX = "_owner"


def git_blob_id(raw: bytes) -> str:
    """The Git blob id of these exact bytes, computed without invoking git.

    Exemptions are keyed on this. That is what makes the grandfather list fail closed: edit
    a byte and the blob changes, so the exemption evaporates by itself. A path-keyed or
    globbed exemption would keep covering whatever that path later became.
    """
    header = f"blob {len(raw)}\0".encode("utf-8")
    return hashlib.sha1(header + raw).hexdigest()  # noqa: S324 - Git's object id, not a security digest


def frontmatter_keys(raw: bytes) -> list[str]:
    """Top-level keys of a leading YAML frontmatter block, or `[]` when there is none.

    The scan is scoped to *parsed frontmatter keys*, never to a raw text search. A text
    scanner would flag any document that merely *quotes* a forbidden field while explaining
    the defect.

    Scoped to keys is not the same as scoped to one *spelling* of a key: a quoted key is the
    same key, and reading only the bare form let a document opt out of the governance rule by
    adding two characters.
    """
    text = raw.decode("utf-8", errors="replace").lstrip("﻿")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return []
    keys: list[str] = []
    for line in lines[1:]:
        if line.strip() in ("---", "..."):
            break
        if line[:1].isspace() or not line.strip() or line.lstrip().startswith("#"):
            continue  # nested key or comment — only top-level keys are in scope
        match = _FRONTMATTER_KEY.match(line)
        if match:
            keys.append(match.group(2))
    return keys


def frontmatter_scalars(raw: bytes) -> dict[str, str]:
    """Top-level `key: value` scalars of a leading frontmatter block, or `{}` when absent.

    The value view `frontmatter_keys` does not offer, added for the instruction `form:`
    declaration (SIMP-C1). Deliberately a sibling walk rather than a refactor of
    `frontmatter_keys` into `list(frontmatter_scalars(...))`: that function is the
    governance scan's input and its list semantics preserve duplicate keys, which a dict
    view silently collapses. Widening a guard's behaviour as a side effect of adding a
    convenience is the class `E6` names.

    Values are stripped of surrounding quotes and of a trailing ` #` comment; a key with no
    scalar (a nested block) maps to the empty string, so a caller comparing against an
    expected value never reads a block as a declaration.
    """
    text = raw.decode("utf-8", errors="replace").lstrip("﻿")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    scalars: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() in ("---", "..."):
            break
        if line[:1].isspace() or not line.strip() or line.lstrip().startswith("#"):
            continue  # nested key or comment — only top-level keys are in scope
        match = _FRONTMATTER_KEY.match(line)
        if not match:
            continue
        value = line[match.end():].strip()
        if " #" in value:
            value = value.split(" #", 1)[0].strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        scalars.setdefault(match.group(2), value)
    return scalars


@dataclasses.dataclass(frozen=True)
class Exemption:
    blob: str
    path_hint: str
    fields: tuple[str, ...]
    immutability_rule: str


def load_exemptions(path: pathlib.Path | str | None) -> dict[str, Exemption]:
    """Load the blob-keyed grandfather list.

    The list lives outside this module by design: an enumerated, human-owned register
    recorded with the node, not a constant hidden in a checker where nobody reviews it.
    Absence of the file means no exemption, never an implicit one.
    """
    if not path:
        return {}
    target = pathlib.Path(path)
    if not target.exists():
        raise SpecGap(f"{GOVERNANCE_CODE}-EXEMPTIONS-MISSING exemption register not found: {target}")
    raw = json.loads(target.read_text(encoding="utf-8"))
    out: dict[str, Exemption] = {}
    for entry in raw["exemptions"]:
        for field in ("blob", "path_hint", "fields", "immutability_rule"):
            if not entry.get(field):
                raise SpecGap(
                    f"{GOVERNANCE_CODE}-EXEMPTION-INCOMPLETE entry missing '{field}': {entry}"
                )
        out[entry["blob"]] = Exemption(
            blob=entry["blob"],
            path_hint=entry["path_hint"],
            fields=tuple(entry["fields"]),
            immutability_rule=entry["immutability_rule"],
        )
    return out


@dataclasses.dataclass(frozen=True)
class GovernanceScan:
    report: Report
    scanned: tuple[str, ...]
    exempted: tuple[str, ...]


def governance_scan(
    reader: TreeReader,
    paths: Sequence[str],
    exemptions: Mapping[str, Exemption] | None = None,
) -> GovernanceScan:
    """Reject a governance document that carries its own approval status.

    The rule already exists in prose — contract §14 and plan §0 both say the approval status
    lives in the append-only record, never inside the approved bytes. This makes it
    mechanical, because a fixture suite that never inspects the governance layer is not
    evidence that the layer is clean.
    """
    exemptions = exemptions or {}
    issues: list[Issue] = []
    scanned: list[str] = []
    exempted: list[str] = []

    for path in paths:
        raw = reader.read(path)
        if raw is None:
            issues.append(
                Issue(f"{GOVERNANCE_CODE}-SUBJECT-MISSING", "declared governance document not found", path)
            )
            continue
        scanned.append(path)
        blob = git_blob_id(raw)
        offending = [
            key
            for key in frontmatter_keys(raw)
            if key in SELF_APPROVAL_FIELDS and not key.endswith(OWNER_SUFFIX)
        ]
        if not offending:
            continue
        exemption = exemptions.get(blob)
        if exemption:
            uncovered = sorted(set(offending) - set(exemption.fields))
            if not uncovered:
                exempted.append(path)
                continue
            issues.append(
                Issue(
                    f"{GOVERNANCE_CODE}-EXEMPTION-NARROWER",
                    f"blob is grandfathered for {list(exemption.fields)} but also carries "
                    f"{uncovered}",
                    path,
                )
            )
            continue
        issues.append(
            Issue(
                f"{GOVERNANCE_CODE}-SELF-APPROVAL",
                f"governance document carries its own approval state in frontmatter: {offending}",
                path,
            )
        )

    return GovernanceScan(report_of(issues), tuple(scanned), tuple(exempted))
