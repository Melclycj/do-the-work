"""Commit-bound review subject: the wave-2 successor to the ReviewPackage layer.

This module and its sibling [`review_result_v2.py`](review_result_v2.py) are the live path
for v2 runs (contract supersession-1); `review.py` holds the v1 path, **frozen for reading
pinned history** — closed runs and shadow rounds keep their frozen packages, no migration
(wave-2 design §3.5). The layer is sibling modules rather than an extension of `review.py`
for a recorded reason (W2 record, decision D1): that file sits just under the 800-line
ceiling and cannot absorb this layer, and the design names the sibling-module fallback
explicitly. The split between these two modules is by object — this one owns the
**subject** (is this commit a dispatchable, complete, self-consistent review subject?),
the sibling owns the **verdict** (does this result bind the subject it claims?) — and it
keeps each file under the same ceiling.

**The subject is one commit.** The controller commits the run's control plane before
dispatching review; the review subject is that commit's SHA, and everything else is
derived from it. Git content-addresses every member byte, so there are no per-member
digests and — deliberately — **no hand-authored member enumeration**: the expected set is
derived from the committed documents themselves (the state's pointers, the plan's
`check_order`), which kills the w1-r1 freeze-check-paths defect class at the root instead
of guarding it.

**Git replaces byte binding, not verification.** The two check classes the package layer
carried survive it and are re-homed (design must-fix 1): `check_subject` below carries
completeness and identity against the CandidateRecord read from the evidence commit, and
the sibling's `check_review_result_v2` carries the verdict binding a v2 result must answer
for.

Nothing here issues a verdict. This module validates that a committed control plane is
what it claims to be.
"""
from __future__ import annotations

import dataclasses
import functools
import json
import pathlib
from typing import Any, Mapping

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

from rsclib.document_harness import (
    SCHEMA_DIR,
    SCHEMA_FILES,
    SCHEMA_URI_BASE,
    AssuranceFault,
    Issue,
    Report,
    SpecGap,
    bytes_digest,
    canonical_digest,
    load_json,
    report_of,
    validate,
)
from rsclib.document_harness import candidate as cand
from rsclib.document_harness.assurance_state import DIGEST_PROTECTED_FIELDS
from rsclib.document_harness.candidate import CandidateTreeReader, covered_by
from rsclib.document_harness.review import N2_SCHEMA_FILES
from rsclib.document_harness.spec import spec_schema_kind

CODE = "V3-SUBJECT"

#: Run-layout conventions established by w1-r1 in production and recorded at its close;
#: load-bearing here (supersession-1 S2). Paths are relative to the run's control root.
STATE_PATH = "control/state.json"
CHECK_RESULT_PATH = "evidence/check-{check_id}.json"

W2_SCHEMA_FILES: dict[str, str] = {"review_result_v2": "review.v2.schema.json"}
W2_SCHEMA_POINTERS: dict[str, str] = {
    "review_subject": "review.v2.schema.json#/$defs/reviewSubject",
}


# ---------------------------------------------------------------------------
# Schema plumbing — the same in-boundary local-registry route review.py recorded
# ---------------------------------------------------------------------------


@functools.lru_cache(maxsize=1)
def _w2_registry() -> Registry:
    resources = []
    for filename in (*SCHEMA_FILES.values(), *N2_SCHEMA_FILES.values(), *W2_SCHEMA_FILES.values()):
        path = SCHEMA_DIR / filename
        if not path.exists():
            raise AssuranceFault(f"schema pack is incomplete: missing {path}")
        resources.append((SCHEMA_URI_BASE + filename, Resource.from_contents(load_json(path))))
    return Registry().with_resources(resources)


@functools.lru_cache(maxsize=None)
def _w2_validator(kind: str) -> Draft202012Validator:
    if kind in W2_SCHEMA_FILES:
        schema = load_json(SCHEMA_DIR / W2_SCHEMA_FILES[kind])
        Draft202012Validator.check_schema(schema)
        return Draft202012Validator(schema, registry=_w2_registry())
    if kind in W2_SCHEMA_POINTERS:
        return Draft202012Validator(
            {"$ref": SCHEMA_URI_BASE + W2_SCHEMA_POINTERS[kind]}, registry=_w2_registry()
        )
    raise SpecGap(f"unknown document kind: {kind}")


def validate_w2(kind: str, document: Mapping[str, Any]) -> Report:
    """Validate one wave-2 document against its closed schema."""
    errors = sorted(_w2_validator(kind).iter_errors(document), key=lambda error: list(error.path))
    return report_of(
        Issue(
            f"V3-SCHEMA-{kind.upper()}",
            error.message[:300],
            "/".join(str(part) for part in error.path) or "<root>",
        )
        for error in errors
    )


# ---------------------------------------------------------------------------
# Subject construction
# ---------------------------------------------------------------------------


def subject_of(
    *,
    evidence_commit: str,
    candidate_ref: Mapping[str, Any],
    base_revision: str,
    control_root: str,
    repair_round: int,
) -> dict[str, Any]:
    """The commit-bound review subject. Binding an identity is not judging it."""
    return {
        "evidence_commit": evidence_commit,
        "candidate_ref": dict(candidate_ref),
        "base_revision": base_revision,
        "control_root": control_root,
        "repair_round": repair_round,
    }


def subject_binding(evidence_commit: str, review: Mapping[str, Any]) -> dict[str, str]:
    """What a later reader re-verifies: the commit under review, and the verdict's digest.

    The v1 analogue paired a package digest with the review digest (`flow.review_binding`,
    retired with the package leg in round `CORE-SET-CODE`). Here the commit stands where the
    package digest stood, because it content-addresses every member byte the package bound by
    hand — one fewer digest to reproduce, and nothing hand-authored to get wrong.
    """
    return {"evidence_commit": evidence_commit, "review_digest": canonical_digest(review)}


# ---------------------------------------------------------------------------
# The committed control plane, read back out of the evidence commit
# ---------------------------------------------------------------------------


@dataclasses.dataclass(frozen=True)
class ControlPlane:
    """What could be derived from the evidence commit. Missing pieces are None + issues."""

    state: dict[str, Any] | None
    spec: dict[str, Any] | None
    plan: dict[str, Any] | None
    record: dict[str, Any] | None
    report: Report


def _read_document(
    reader: CandidateTreeReader, path: str, where: str, issues: list[Issue]
) -> dict[str, Any] | None:
    raw = reader.read(path)
    if raw is None:
        issues.append(
            Issue(
                f"{CODE}-POINTER-MISSING",
                f"document does not resolve in the evidence commit: {path}",
                where,
            )
        )
        return None
    try:
        return json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        issues.append(
            Issue(f"{CODE}-DOCUMENT-INVALID", f"{path} is not valid JSON: {exc}", where)
        )
        return None


def _resolve_pointer(
    reader: CandidateTreeReader,
    state: Mapping[str, Any],
    field: str,
    issues: list[Issue],
    *,
    required: bool,
) -> bytes | None:
    """Resolve one state pointer inside the evidence commit and verify its bytes digest.

    A missing digest is an issue on a `DIGEST_PROTECTED_FIELDS` pointer and nothing at all
    elsewhere (the 2026-07-29 narrowing). Those six name files whose current version the
    executor is not entitled to produce — the user's decisions, the reviewer's record, and
    the WorkSpec this run is judged against — so there the absent digest says a binding was
    never taken. Everywhere else the executor legitimately authors the file it points at, a
    digest it computes over its own output binds no one, and demanding one only taught
    readers to expect a guarantee that was never there.

    A digest that IS present is still checked on every field: the narrowing removed an
    obligation to write one, never permission to write one that does not match.
    """
    ref = state.get(field)
    if not ref:
        if required:
            issues.append(
                Issue(
                    f"{CODE}-POINTER-ABSENT",
                    f"the state carries no {field}, so the control plane cannot be derived "
                    "from the evidence commit",
                    field,
                )
            )
        return None
    raw = reader.read(ref["path"])
    if raw is None:
        issues.append(
            Issue(
                f"{CODE}-POINTER-MISSING",
                f"pointer target does not resolve in the evidence commit: {ref['path']}",
                field,
            )
        )
        return None
    expected = ref.get("digest_sha256")
    if not expected:
        if field in DIGEST_PROTECTED_FIELDS:
            issues.append(
                Issue(
                    f"{CODE}-POINTER-UNVERIFIED",
                    f"pointer carries no digest, so the bytes at {ref['path']} were NOT verified "
                    "against what the state bound; this is an unverified property, not a "
                    "satisfied one",
                    field,
                )
            )
    elif bytes_digest(raw) != expected:
        issues.append(
            Issue(
                f"{CODE}-POINTER-STALE",
                f"pointer digest no longer matches the committed bytes at {ref['path']}",
                field,
            )
        )
        return None
    return raw


def read_control_plane(
    repo_root: pathlib.Path | str, evidence_commit: str, control_root: str
) -> ControlPlane:
    """Derive spec, plan and CandidateRecord from the evidence commit alone.

    The state file at the conventional `control/state.json` is the entry point; its
    pointers name every other control document, so the enumeration is the committed
    tree's own, never an authored list. A cold session needs nothing but the SHA
    (W2-A7).
    """
    reader = CandidateTreeReader(pathlib.Path(repo_root), evidence_commit)
    issues: list[Issue] = []
    state_path = f"{control_root.rstrip('/')}/{STATE_PATH}"
    state = _read_document(reader, state_path, "state", issues)
    if state is None:
        return ControlPlane(None, None, None, None, report_of(issues))

    schema_report = validate("state", state)
    issues.extend(
        Issue(f"{CODE}-STATE-INVALID", issue.message, issue.where)
        for issue in schema_report.issues
    )

    spec: dict[str, Any] | None = None
    plan: dict[str, Any] | None = None
    record: dict[str, Any] | None = None

    spec_raw = _resolve_pointer(reader, state, "work_spec_ref", issues, required=True)
    if spec_raw is not None:
        spec = _read_document(reader, state["work_spec_ref"]["path"], "work_spec_ref", issues)
    plan_raw = _resolve_pointer(reader, state, "resolved_plan_ref", issues, required=True)
    if plan_raw is not None:
        plan = _read_document(reader, state["resolved_plan_ref"]["path"], "resolved_plan_ref", issues)
    record_raw = _resolve_pointer(reader, state, "fulfillment_ref", issues, required=True)
    if record_raw is not None:
        record = _read_document(reader, state["fulfillment_ref"]["path"], "fulfillment_ref", issues)
    # Every remaining pointer the state carries must also resolve inside the commit —
    # the subject is the whole control plane, not the three documents this module joins.
    for field in ("instruction_audit_ref", "start_decision_ref", "manifest_ref",
                  "check_results_ref", "coverage_ref", "review_ref", "repair_decision_ref",
                  "assurance_candidate_ref", "bind_authorization_ref", "final_decision_ref",
                  "summary_ref"):
        _resolve_pointer(reader, state, field, issues, required=False)

    if spec is not None:
        spec_report = validate(spec_schema_kind(spec), spec)
        issues.extend(
            Issue(f"{CODE}-DOCUMENT-INVALID", issue.message, f"work_spec/{issue.where}")
            for issue in spec_report.issues
        )
    if record is not None:
        record_report = validate("candidate", record)
        issues.extend(
            Issue(f"{CODE}-DOCUMENT-INVALID", issue.message, f"candidate_record/{issue.where}")
            for issue in record_report.issues
        )
    # The plan binds the exact WorkSpec bytes it was resolved from; a spec swapped after
    # resolution would otherwise verify clean document by document.
    if plan is not None and spec_raw is not None:
        bound = plan.get("work_spec_ref", {}).get("digest_sha256")
        if bound and bound != bytes_digest(spec_raw):
            issues.append(
                Issue(
                    f"{CODE}-SPEC-BINDING-MISMATCH",
                    "the committed plan was resolved from different WorkSpec bytes than the "
                    "ones the committed state points at",
                    "resolved_plan_ref/work_spec_ref",
                )
            )

    return ControlPlane(state, spec, plan, record, report_of(issues))


# ---------------------------------------------------------------------------
# check_subject — completeness and identity, derived from the committed tree
# ---------------------------------------------------------------------------


def check_subject(subject: Mapping[str, Any], repo_root: pathlib.Path | str) -> Report:
    """The subject must be derivable, complete and identical to what the commit records.

    Re-homes what git cannot replace (design §3.2): the v1 `check_package` identity
    cross-checks land here as subject-versus-CandidateRecord comparisons, with the record
    read **from the evidence commit**; completeness lands here as tree-derived expectation
    (state pointers, `plan.check_order` → one CheckResult file each) versus the committed
    tree. There is no authored member list to get wrong.
    """
    schema_report = validate_w2("review_subject", subject)
    if not schema_report.ok:
        return schema_report

    root = pathlib.Path(repo_root)
    control_root = subject["control_root"]
    plane = read_control_plane(root, subject["evidence_commit"], control_root)
    issues: list[Issue] = list(plane.report.issues)
    reader = CandidateTreeReader(root, subject["evidence_commit"])

    # --- identity: the subject must agree with the CandidateRecord at the commit ---
    #
    # Each row carries its code as a WHOLE `f"{CODE}-…"` literal rather than a bare suffix
    # interpolated at the raise site. The suffix form worked identically but was invisible
    # to every sweep that reads codes out of the source — including this layer's own
    # reachability test, which found 33 of 38 and silently exempted exactly these five
    # (W2 review finding 1). A code a sweep cannot see is a code no test is obliged to
    # assert, so the literal form is what keeps the guard as wide as it claims to be.
    if plane.record is not None:
        record = plane.record
        for code, label, mine, recorded in (
            (f"{CODE}-WRONG-CANDIDATE", "candidate commit",
             subject["candidate_ref"].get("commit"), record["candidate_ref"].get("commit")),
            (f"{CODE}-CANDIDATE-BRANCH-MISMATCH", "candidate branch",
             subject["candidate_ref"].get("branch"), record["candidate_ref"].get("branch")),
            (f"{CODE}-BASE-MISMATCH", "base revision",
             subject["base_revision"], record["base_revision"]),
            (f"{CODE}-CONTROL-ROOT-MISMATCH", "control root",
             subject["control_root"], record["control_root"]),
            (f"{CODE}-ROUND-MISMATCH", "repair round",
             subject["repair_round"], record["repair_round"]),
        ):
            if mine != recorded:
                issues.append(
                    Issue(
                        code,
                        f"the subject's {label} ({str(mine)[:12]}) disagrees with the "
                        f"CandidateRecord at the evidence commit ({str(recorded)[:12]})",
                        "subject",
                    )
                )
        if plane.spec is not None:
            # Internal record invariants are the existing v1 function, reused on the
            # committed documents rather than restated (N0-A6).
            issues.extend(cand.check_record(record, plane.spec).issues)

    # --- completeness: declared inputs and the frozen instruction resolve as pinned ---
    if plane.spec is not None:
        frozen = plane.spec["instruction_ref"]
        raw = CandidateTreeReader(root, frozen["revision"]).read(frozen["path"])
        if raw is None:
            issues.append(
                Issue(
                    f"{CODE}-INSTRUCTION-UNRESOLVED",
                    f"the frozen instruction does not resolve at its pinned revision: "
                    f"{frozen['path']} @ {str(frozen['revision'])[:12]}",
                    "work_spec/instruction_ref",
                )
            )
        elif frozen.get("digest_sha256") and bytes_digest(raw) != frozen["digest_sha256"]:
            issues.append(
                Issue(
                    f"{CODE}-INSTRUCTION-STALE",
                    f"the frozen instruction's digest does not match the bytes at its pinned "
                    f"revision: {frozen['path']}",
                    "work_spec/instruction_ref",
                )
            )
        for declared in plane.spec.get("inputs", []):
            raw_in = CandidateTreeReader(root, declared["revision"]).read(declared["path"])
            if raw_in is None:
                issues.append(
                    Issue(
                        f"{CODE}-INPUT-UNRESOLVED",
                        f"declared source input does not resolve at its pinned revision: "
                        f"{declared['path']} @ {str(declared['revision'])[:12]}",
                        "work_spec/inputs",
                    )
                )
            elif declared.get("digest_sha256") and bytes_digest(raw_in) != declared["digest_sha256"]:
                issues.append(
                    Issue(
                        f"{CODE}-INPUT-STALE",
                        f"declared source input's digest does not match the bytes at its "
                        f"pinned revision: {declared['path']}",
                        "work_spec/inputs",
                    )
                )

    # --- completeness: one committed file per resolved CheckResult (w1-r1 convention,
    # now load-bearing). The expected set comes from the committed plan's check_order —
    # derived, never authored — so writing eight results into one aggregate file is
    # reported here as eight missing per-result files (W2-A2's representable half).
    #
    # HD-12 (2026-08-08): a CheckResult does not survive its run — on a CLOSED control
    # plane absence is the ruled state; per-result files remain load-bearing for every
    # pre-CLOSED status.
    if plane.plan is not None:
        status = plane.state.get("status") if plane.state else None
        for check_id in plane.plan.get("check_order", []):
            rel = f"{control_root.rstrip('/')}/{CHECK_RESULT_PATH.format(check_id=check_id)}"
            raw_result = reader.read(rel)
            if raw_result is None:
                if status == "CLOSED":
                    # HD-12's carve-out: the retirement step (`run_retire.py`) retires exactly
                    # this file once the run reaches CLOSED, and its absence here is that
                    # ruling taking effect, not a completeness defect. Every earlier status
                    # still falls through to the MISSING report below unchanged.
                    continue
                issues.append(
                    Issue(
                        f"{CODE}-CHECK-RESULT-MISSING",
                        f"the plan orders check '{check_id}' but the evidence commit carries "
                        f"no per-result file at {rel}",
                        "plan/check_order",
                    )
                )
                continue
            try:
                document = json.loads(raw_result.decode("utf-8"))
            except (UnicodeDecodeError, json.JSONDecodeError) as exc:
                issues.append(
                    Issue(f"{CODE}-CHECK-RESULT-INVALID", f"{rel} is not valid JSON: {exc}",
                          "plan/check_order")
                )
                continue
            result_report = validate("check_result", document)
            if not result_report.ok:
                issues.append(
                    Issue(
                        f"{CODE}-CHECK-RESULT-INVALID",
                        f"{rel} is not a valid CheckResult: "
                        + result_report.issues[0].message[:160],
                        "plan/check_order",
                    )
                )
            elif document.get("check_id") != check_id:
                issues.append(
                    Issue(
                        f"{CODE}-CHECK-RESULT-INVALID",
                        f"{rel} carries check_id '{document.get('check_id')}', not the "
                        f"'{check_id}' its path claims",
                        "plan/check_order",
                    )
                )

    # --- containment: the evidence commit changes nothing outside the control root ---
    # (supersession-1 S2; W2-A10; design must-fix 2). Checked against the commit's own
    # parent with the same segment-boundary containment the candidate boundary uses.
    try:
        changes = cand.observe_changes(
            root, f"{subject['evidence_commit']}^", subject["evidence_commit"]
        )
    except AssuranceFault as exc:
        issues.append(
            Issue(
                f"{CODE}-CONTAINMENT-UNVERIFIED",
                "the evidence commit's own change set could not be observed, so its "
                f"containment in the control root was NOT verified: {exc}",
                "evidence_commit",
            )
        )
    else:
        for change in changes:
            if not covered_by(change["path"], [control_root]):
                issues.append(
                    Issue(
                        f"{CODE}-EVIDENCE-OUT-OF-ROOT",
                        f"the evidence commit changes a path outside the run's control root: "
                        f"{change['path']}",
                        "evidence_commit",
                    )
                )

    return schema_report + report_of(issues)


# ---------------------------------------------------------------------------
# Invariant 11, successor form (supersession-1 S3)
# ---------------------------------------------------------------------------


@dataclasses.dataclass(frozen=True)
class EvidenceSetV2:
    """The regenerable evidence of one repair round: digests plus the evidence commit."""

    fulfillment: str
    manifest: str
    coverage: str
    evidence_commit: str
    checks: tuple[str, ...] = ()


def check_repair_regeneration_v2(before: EvidenceSetV2, after: EvidenceSetV2) -> Report:
    """C2 regenerates every piece of evidence and commits a NEW evidence commit.

    The v2 counterpart of `flow.check_repair_regeneration`, which compares the package
    digest v2 no longer has; a round-1 subject reusing the round-0 evidence commit would
    review C while reporting on C2 — the same class, arriving through the subject.
    """
    issues: list[Issue] = []
    for name, old, new in (
        ("fulfillment", before.fulfillment, after.fulfillment),
        ("manifest", before.manifest, after.manifest),
        ("coverage", before.coverage, after.coverage),
    ):
        if old == new:
            issues.append(
                Issue(
                    f"{CODE}-EVIDENCE-NOT-REGENERATED",
                    f"the repaired candidate reuses the round-0 {name}; it describes the "
                    "candidate that was replaced",
                    name,
                )
            )
    if before.evidence_commit == after.evidence_commit:
        issues.append(
            Issue(
                f"{CODE}-EVIDENCE-COMMIT-REUSED",
                "the repair round reuses the round-0 evidence commit; a new control plane "
                "requires a new commit",
                "evidence_commit",
            )
        )
    if before.checks and before.checks == after.checks:
        issues.append(
            Issue(
                f"{CODE}-CHECKS-NOT-RERUN",
                "every check result is byte-identical to round 0, so the checks were not "
                "re-run against the repaired candidate",
                "checks",
            )
        )
    return report_of(issues)


__all__ = [
    "CHECK_RESULT_PATH",
    "ControlPlane",
    "EvidenceSetV2",
    "STATE_PATH",
    "W2_SCHEMA_FILES",
    "W2_SCHEMA_POINTERS",
    "check_repair_regeneration_v2",
    "check_subject",
    "read_control_plane",
    "subject_binding",
    "subject_of",
    "validate_w2",
]
