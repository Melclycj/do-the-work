"""The v2 ReviewResult: version keying and the verdict binding a commit-bound result carries.

Sibling of [`review_subject.py`](review_subject.py), which owns the *subject* — whether an
evidence commit is a dispatchable, complete, self-consistent review subject. This module
owns the *verdict*: whether a result is well-formed, complete against the WorkSpec, and
bound to the exact commit it claims to answer for. The two questions are separable and the
split keeps each file under the 800-line ceiling; `check_subject` is called from here, never
the other way round.

**Version keying is explicit, with no cross-version fallback** (the W1 pattern). A result
with no `schema_version` key is a v1 result; `"2"` selects v2; anything else present —
including an explicit `null` — is a `SpecGap`, fail closed. A v1 result handed to the v2
checker stops the same way: silently accepting it would validate a package-bound result
against commit-bound semantics, which is the fail-open shape N1 taught this package to hunt.

**Parity ceiling, stated rather than glossed (W2 record §6).** The result-internal checks
shared with v1 (obligation coverage, finding coherence, INCOMPLETE disclosure, verify scope,
reviewer distinctness) are re-implemented here rather than imported, because v1's live in
one function that requires a package and is frozen for reading pinned history. The
duplication is against a frozen artifact, so it cannot drift forward — but a defect later
found in the shared semantics must be fixed here and recorded against the frozen copy.

Nothing here issues a verdict. The reviewer owns the ReviewResult; this module validates
what the reviewer produced.
"""
from __future__ import annotations

import pathlib
from typing import Any, Mapping

from rsclib.document_harness import Issue, Report, SpecGap, report_of
from rsclib.document_harness.review_subject import (
    check_subject,
    read_control_plane,
    validate_w2,
)

#: Issue prefix shared with v1's result checker: the same property, reported under the same
#: name, so a reader joining a v1 and a v2 run sees one vocabulary.
RESULT_CODE = "V3-REVIEW"

#: The successor ReviewResult declares its own version (root `schema_version` const).
RESULT_SCHEMA_KINDS: dict[str, str] = {"2": "review_result_v2"}

#: Sentinel distinguishing a missing key from an explicitly present value — `.get()` alone
#: cannot tell `null` from absent, and "present but null" is a declaration, not absence
#: (W1 review finding A1). Only true key absence selects v1.
_ABSENT = object()


def result_schema_kind(result: Mapping[str, Any]) -> str:
    """The schema kind this ReviewResult instance declares. Unknown versions stop."""
    declared = result.get("schema_version", _ABSENT)
    if declared is _ABSENT:
        return "review_result"
    if isinstance(declared, str):
        kind = RESULT_SCHEMA_KINDS.get(declared)
        if kind is not None:
            return kind
    raise SpecGap(
        f"unsupported ReviewResult schema_version: {declared!r} — "
        "no cross-version fallback; supported: absent (v1), '2'"
    )


def check_review_result_v2(
    result: Mapping[str, Any],
    repo_root: pathlib.Path | str,
    *,
    evidence_commit: str,
    executor: str | None = None,
) -> Report:
    """Invariants 2 and 10 for a v2 result, plus the subject binding git cannot carry.

    `evidence_commit` is the commit under check — the SHA the controller actually
    dispatched. The result's own `subject.evidence_commit` must equal it; trusting the
    result's copy alone would let a result answer for whatever commit it names, which is
    the re-attribution class the binding exists to close (V3-D5).

    `executor` keeps v1's shape: optional in the signature, never optional in the report —
    omitting it yields `V3-REVIEW-REVIEWER-DISTINCTNESS-UNVERIFIED` rather than silence.
    """
    kind = result_schema_kind(result)
    if kind != "review_result_v2":
        raise SpecGap(
            "a version-1 ReviewResult was handed to the v2 checker; v1 results are "
            "package-bound and belong to review.check_review_result"
        )
    schema_report = validate_w2(kind, result)
    if not schema_report.ok:
        return schema_report

    issues: list[Issue] = []
    subject = result["subject"]

    # --- the verdict binds the exact commit it answers for ---
    if subject["evidence_commit"] != evidence_commit:
        issues.append(
            Issue(
                f"{RESULT_CODE}-SUBJECT-COMMIT-MISMATCH",
                f"the result answers for evidence commit {subject['evidence_commit'][:12]} "
                f"but the commit under check is {evidence_commit[:12]}",
                "subject/evidence_commit",
            )
        )

    # --- the subject itself must be derivable, complete and true to the commit ---
    subject_report = check_subject(subject, repo_root)
    issues.extend(subject_report.issues)

    plane = read_control_plane(pathlib.Path(repo_root), subject["evidence_commit"],
                               subject["control_root"])
    spec, record = plane.spec, plane.record

    if spec is not None and result["work_id"] != spec["work_id"]:
        issues.append(
            Issue(f"{RESULT_CODE}-WORK-MISMATCH",
                  "result names a different work_id than the committed WorkSpec", "work_id")
        )
    if record is not None:
        if result["run_id"] != record["run_id"]:
            # v1 carried this only in check_package; dissolving the package would have
            # orphaned it (design verify finding 1) — it lives here now.
            issues.append(
                Issue(f"{RESULT_CODE}-RUN-MISMATCH",
                      "result names a different run_id than the CandidateRecord at the "
                      "evidence commit", "run_id")
            )
        expected_round = "FULL" if record["repair_round"] == 0 else "VERIFY"
        if result["review_round"] != expected_round:
            issues.append(
                Issue(
                    f"{RESULT_CODE}-ROUND-MISMATCH",
                    f"a {result['review_round']} result answers a repair-round "
                    f"{record['repair_round']} candidate, which takes a {expected_round}",
                    "review_round",
                )
            )

    # --- invariant 2: every obligation exactly once, no more and no fewer ---
    if spec is not None:
        declared = {ob["obligation_id"] for ob in spec["obligations"]}
        disposed = [row["obligation_id"] for row in result["per_obligation_disposition"]]
        for missing in sorted(declared - set(disposed)):
            issues.append(
                Issue(f"{RESULT_CODE}-OBLIGATION-UNDISPOSED",
                      f"no review disposition for obligation: {missing}",
                      "per_obligation_disposition")
            )
        for unknown in sorted(set(disposed) - declared):
            issues.append(
                Issue(f"{RESULT_CODE}-UNDECLARED-DISPOSITION",
                      f"disposition for an obligation the WorkSpec never declared: {unknown}",
                      "per_obligation_disposition")
            )
        for obligation_id in sorted({name for name in disposed if disposed.count(name) > 1}):
            issues.append(
                Issue(f"{RESULT_CODE}-DUPLICATE-DISPOSITION",
                      f"obligation disposed more than once: {obligation_id}",
                      "per_obligation_disposition")
            )

        # --- invariant 10: the instruction rechecked must be the one the WorkSpec froze ---
        rechecked = result["instruction_completeness"]["instruction_ref"]
        for field in ("path", "revision"):
            if rechecked.get(field) != spec["instruction_ref"].get(field):
                issues.append(
                    Issue(
                        f"{RESULT_CODE}-INSTRUCTION-MISMATCH",
                        f"the completeness recheck read a different frozen instruction ({field})",
                        "instruction_completeness/instruction_ref",
                    )
                )

    # --- findings referenced by a disposition must exist ---
    finding_ids = {finding["finding_id"] for finding in result.get("findings", [])}
    for row in result["per_obligation_disposition"]:
        for referenced in row.get("finding_ids", []):
            if referenced not in finding_ids:
                issues.append(
                    Issue(
                        f"{RESULT_CODE}-DANGLING-FINDING-REF",
                        f"disposition cites finding '{referenced}', which this result does "
                        "not contain",
                        f"per_obligation_disposition/{row['obligation_id']}",
                    )
                )
        if row["disposition"] == "NOT_SUPPORTED" and not row.get("finding_ids"):
            issues.append(
                Issue(
                    f"{RESULT_CODE}-UNSUPPORTED-WITHOUT-FINDING",
                    f"obligation '{row['obligation_id']}' is NOT_SUPPORTED but cites no "
                    "finding, so nothing names what would have to change",
                    f"per_obligation_disposition/{row['obligation_id']}",
                )
            )

    # --- a blocking discrepancy cannot coexist with 'no blocker found' ---
    blocking = [f["finding_id"] for f in result.get("findings", []) if f["blocking"]]
    if blocking and result["verdict"] == "REVIEWED_NO_BLOCKER":
        issues.append(
            Issue(
                f"{RESULT_CODE}-BLOCKER-CONTRADICTS-VERDICT",
                f"verdict is REVIEWED_NO_BLOCKER while {len(blocking)} blocking finding(s) "
                f"are recorded: {', '.join(blocking)}",
                "verdict",
            )
        )

    # --- an INCOMPLETE map is DISCLOSED, never silently carried. Same floor and same
    # honestly-stated ceiling as v1: the id must be traceable from the result, which
    # establishes mention, not explanation.
    completeness = result["instruction_completeness"]
    if completeness["result"] == "INCOMPLETE":
        unmapped = completeness.get("unmapped_unit_ids", [])

        def names_a_gap(text: str) -> bool:
            return any(unit in text for unit in unmapped)

        undisclosed = [
            requirement
            for requirement, satisfied in (
                ("a finding naming one of them",
                 any(names_a_gap(f["statement"]) for f in result.get("findings", []))),
                ("a residual_uncertainty entry naming one of them",
                 any(names_a_gap(note) for note in result["residual_uncertainty"])),
            )
            if not satisfied
        ]
        if undisclosed:
            issues.append(
                Issue(
                    f"{RESULT_CODE}-INCOMPLETE-UNDISCLOSED",
                    "the instruction recheck returned INCOMPLETE, naming unmapped unit(s) "
                    f"{', '.join(unmapped)}, but the result carries no "
                    + " and no ".join(undisclosed)
                    + "; a narrowing the deciding user cannot see is the one thing it may "
                    "not be",
                    "instruction_completeness/unmapped_unit_ids",
                )
            )

    # --- V3-D6: a VERIFY is answerable for the whole repair diff and the boundaries ---
    scope = result.get("verify_scope")
    if scope:
        unchecked = [
            name
            for name, flag in (
                ("the whole repair diff", scope["repair_diff_reviewed"]),
                ("the permanent boundaries", scope["permanent_boundaries_checked"]),
            )
            if not flag
        ]
        if unchecked:
            issues.append(
                Issue(
                    f"{RESULT_CODE}-VERIFY-SCOPE-INCOMPLETE",
                    "the VERIFY did not cover " + " or ".join(unchecked)
                    + "; V3-D6 scopes it to the accepted findings, the entire repair diff "
                    "and the permanent boundaries",
                    "verify_scope",
                )
            )

    # --- V3-D5: the reviewer is not the executor, or that is reported as unverified ---
    if executor is None or not executor.strip():
        issues.append(
            Issue(
                f"{RESULT_CODE}-REVIEWER-DISTINCTNESS-UNVERIFIED",
                "no executor identity was supplied, so reviewer/executor distinctness was "
                "not checked; this is an unverified property, not a satisfied one",
                "reviewed_by",
            )
        )
    elif result["reviewed_by"].strip().casefold() == executor.strip().casefold():
        issues.append(
            Issue(
                f"{RESULT_CODE}-REVIEWER-NOT-DISTINGUISHABLE",
                f"the review was performed by the executor of the same run: {executor}",
                "reviewed_by",
            )
        )

    return schema_report + report_of(issues)


__all__ = [
    "RESULT_CODE",
    "RESULT_SCHEMA_KINDS",
    "check_review_result_v2",
    "result_schema_kind",
]
