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

**What "is a v1 result" buys after round `V1-RESULT-RETIRE`, decided here rather than left to
fall out.** Contract v4 §13.1 now prescribes *no* validation path for a result with no
`schema_version` key — one presented nonetheless is not validated and not accepted, fail
closed — and expressly leaves the choice of which mechanism raises that stop to this
implementation (`HD-64`). The choice made, and disclosed because the clause requires the code
and the contract to agree: `result_schema_kind` keeps *classifying*, returning the kind the
instance declares by omission, and the stop is raised by whoever tries to *validate* that
kind. Measured over `tooling/` at this round's base, this function has exactly two callers in
the package — `check_review_result_v2` below and `flow.reviewed_candidate_ref` — plus
`test_review_v2_subject.py`, which asserts the classification directly at three sites and
calls nothing else; which of the two §13.1 reaches is the part worth stating rather than
glossing. The first is a validation path and it raises: `check_review_result_v2` refuses any
kind that is not `review_result_v2` with a message naming why. It is not the only thing that
refuses, though the others reach that stop from the kind name rather than through this
function — every validator in the package, `review.validate_n2`,
`review_subject.validate_w2` and the package root's `validate`, refuses `"review_result"` as
an unregistered kind, round `V1-RESULT-RETIRE` having deleted both v1 registrations along
with the schema file. The second caller, `flow.reviewed_candidate_ref`, is an accessor: it
branches on the declared shape to read `candidate_ref` from the right place and neither
validates nor accepts anything, so §13.1 does not reach it and this round changes neither its
behaviour nor the fact — true before this round and unchanged by it — that
`check_repair_decision` reads a result it never validated. That gap is about validating
results at all, not about v1, and the class ruled empty is what keeps it from having a v1
instance to bite on.

Making this function raise on absence instead was considered and not taken: it would collapse
the `_ABSENT` sentinel's measured distinction between an absent key and an explicit `null`
(W1 review finding A1) into one behaviour, it would pre-empt the specific v1 message below
with a generic one, and it would turn that accessor into a raising path for a shape it reads
correctly.

**Corrected forward 2026-09-02, round `PROMISE-PATH-ENGINE`; the two paragraphs above are
left standing word for word (`HD-59`).** Three of their statements no longer hold, and each
was removed by a change rather than found wrong when written. (1) The caller count: measured
over `tooling/` and `assurance/` at this round's base, `result_schema_kind` has **three**
callers in the package — `validate_result` and `check_review_result_v2` below, and
`flow.reviewed_candidate_ref` — the first of them added here. (2) The accessor now validates:
`flow.reviewed_candidate_ref` reads nothing until `validate_result` has passed on the
instance, so §13.1 reaches it after all, and a version-1 root shape stops there instead of
being read correctly and decided from. (3) `check_repair_decision` no longer reads a result it
never validated, and neither does `check_verify_outcome`; the gap the last sentence named —
about validating results at all, not about v1 — is what item 7 of batch `PROMISE-PATH` closed,
by the entry below and its three uses in `flow.py`. What did **not** change is the choice
those paragraphs defend: `result_schema_kind` still classifies and never raises on absence, so
the `_ABSENT` distinction and the specific v1 message both survive, and the stop is still
raised by whoever tries to validate.

**Parity ceiling, stated rather than glossed (W2 record §6).** The result-internal checks
shared with v1 (obligation coverage, finding coherence, INCOMPLETE disclosure, verify scope,
reviewer distinctness) were re-implemented here rather than imported, because v1's lived in
one function that required a package. That function retired with the package leg in round
`CORE-SET-CODE`, so what was a duplication against a frozen artifact is now the only copy:
these are the checks, and a defect found in them is fixed here.

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
    """The schema kind this ReviewResult instance declares. Unknown versions stop.

    `"review_result"` is still what key absence returns, and since round `V1-RESULT-RETIRE`
    no registered schema answers to it — every path that tries to validate it raises, which
    is contract v4 §13.1's fail-closed outcome reached without this classifier deciding it.
    The module docstring records why the stop was left downstream rather than raised here.
    """
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


def validate_result(result: Mapping[str, Any]) -> Report:
    """Validate a ReviewResult against the schema the instance itself declares. Fails closed.

    The entry the flow controller reads a returned result through. Until round
    `PROMISE-PATH-ENGINE` nothing in `flow.py` validated the review it decided from:
    `check_repair_decision` reconciled a repair against a document of any shape at all, and a
    version-1 root shape — the kind no registered schema answers to since round
    `V1-RESULT-RETIRE` — returned a clean report rather than a stop (`HD-65`'s boundary
    paragraph, 2026-08-29: "对任何 result 都不验证，v2 的也不验证；v1 只是它今天最显眼的一个面").

    Keyed on `result_schema_kind`, so the routing rule is the module's one rule and not a
    second copy of it: `"2"` selects the v2 schema; key absence selects the v1 kind, which
    `validate_w2` refuses as unregistered — contract v4 §13.1's "not validated and not
    accepted", reached by trying to validate rather than by a second decision here; any other
    value raises out of the classifier, with no cross-version fallback. Both refusals raise
    rather than report, which is what separates "this result is defective" (a Report the
    caller weighs) from "this result has no validation path" (a stop).
    """
    return validate_w2(result_schema_kind(result), result)


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
            "package-bound, and the checker that answered for them retired with the package "
            "leg in round CORE-SET-CODE — pinned v1 history is read, not re-checked"
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

    # --- a blocking discrepancy cannot coexist with 'no blocker found', and the verdict that
    # --- reports one cannot decline to name it. Both directions of the same reconciliation,
    # --- and this is the one function holding the verdict and the findings at once. The
    # --- schema gets as far as requiring `findings` on an UNRESOLVED_BLOCKER; whether any of
    # --- them is BLOCKING is a value it cannot see across two subschemas, so it says so in
    # --- its own description and leaves the second half here.
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
    if result["verdict"] == "UNRESOLVED_BLOCKER" and not blocking:
        issues.append(
            Issue(
                f"{RESULT_CODE}-UNRESOLVED-BLOCKER-NAMES-NONE",
                "verdict is UNRESOLVED_BLOCKER while no blocking finding is recorded; the "
                "verdict means a blocker stands after the single permitted repair, and the "
                "stop it triggers reports which ones — so a verdict naming none stops the "
                "run over nothing and leaves the user deciding about an unnamed defect",
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
    "validate_result",
]
