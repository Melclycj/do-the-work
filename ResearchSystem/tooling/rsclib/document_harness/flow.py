"""The flow controller: status legality, the one repair, and the obligations a run carries.

V3-N1 built the state object and its resumability but deliberately left transition legality
here, because a transition table written before review existed would have been a guess about
statuses N1 could not reach. This module owns it, plus the three things that only become
expressible once review and repair exist.

**Status legality (contract §8).** The statuses map 1:1 onto the product flow, so an illegal
transition is not a style violation — it is a run claiming to have reached a stage whose work
did not happen.

**Pointer conditionals (N0 residual R2, N2-A7).** A status makes a claim; the pointers are
what back it. Two directions are enforced, and the second is the one that matters:

* a status must carry the pointers its own stage produced — `CLOSED` without a summary is a
  run asserting it finished without the document that finishes it;
* a status must **not** carry a pointer from a stage it has not reached. This is the
  mechanical form of "no temporal self-binding": an `AssuranceCandidate` that exists before
  the review it binds, or a summary that exists before the decision it terminates, is a
  document created before the thing it claims to be about.

**The single repair (V3-D6, N2-A4..A6).** Repair authorization binds the original candidate,
the accepted finding IDs and their minimum boundary; C2 must regenerate every piece of
evidence rather than inherit it; and a blocker still standing after VERIFY stops the run —
there is no second fix and no review-of-review.

**The governance obligation (N1 residual R2).** N1 made the R4 governance scan mechanical and
reachable, but nothing obliged a run to invoke it, so an operator who never called it got no
signal at all. A run cannot reach a final decision here without stating whether the scan ran;
a skip is legal, but it is a *recorded, reasoned, user-visible* skip. The obligation is to
report the state, not to force the scan — forcing verification is the wrong endpoint, and
making the unverified visible is the reachable one.
"""
from __future__ import annotations

import dataclasses
from typing import Any, Mapping, Sequence

from rsclib.document_harness import (
    Issue,
    Report,
    SpecGap,
    canonical_digest,
    report_of,
    validate,
)
from rsclib.document_harness.candidate import covered_by
from rsclib.document_harness.review import package_digest, result_digest

CODE = "V3-FLOW"

#: Legal successors per status (contract §8). `STOPPED_REPLAN` is reachable from every
#: pre-terminal status and is therefore added to each row below rather than repeated here.
_SUCCESSORS: dict[str, tuple[str, ...]] = {
    "RESOLVED": ("AUDITED",),
    "AUDITED": ("EXECUTING",),
    "EXECUTING": ("EVIDENCED",),
    # After a repair the run regenerates evidence and is reviewed again, so EVIDENCED is
    # re-entered from REPAIRING and REVIEWED is re-entered from EVIDENCED. The loop is
    # bounded by repair_round, not by the transition table.
    "EVIDENCED": ("REVIEWED",),
    "REVIEWED": ("REPAIRING", "AWAITING_FINAL"),
    "REPAIRING": ("EVIDENCED",),
    "AWAITING_FINAL": ("CLOSED",),
    "CLOSED": (),
    "STOPPED_REPLAN": (),
}

TERMINAL_STATUSES = frozenset({"CLOSED", "STOPPED_REPLAN"})

#: Pointers each status must carry, cumulatively: reaching a status means every earlier
#: stage's product exists too. Absence means the status is claiming work that left no record.
_REQUIRED_POINTERS: dict[str, tuple[str, ...]] = {
    "RESOLVED": ("work_spec_ref", "resolved_plan_ref"),
    "AUDITED": ("instruction_audit_ref", "start_decision_ref"),
    "EXECUTING": (),
    "EVIDENCED": ("fulfillment_ref", "manifest_ref", "coverage_ref"),
    "REVIEWED": ("review_ref",),
    "REPAIRING": ("repair_decision_ref",),
    "AWAITING_FINAL": ("assurance_candidate_ref",),
    "CLOSED": ("final_decision_ref", "summary_ref"),
}

#: The order stages are reached in, used to accumulate the requirement above.
_STAGE_ORDER = (
    "RESOLVED",
    "AUDITED",
    "EXECUTING",
    "EVIDENCED",
    "REVIEWED",
    "REPAIRING",
    "AWAITING_FINAL",
    "CLOSED",
)

#: Pointers that cannot honestly exist before a given status (N2-A7): the value is the
#: earliest stage that produces the pointer.
#:
#: This covers **every** pointer, not only the last three. An earlier version listed the three
#: terminal ones and left nine unguarded, so a `review_ref` at `AUDITED` or a `manifest_ref`
#: at `RESOLVED` — a run carrying evidence from a stage it had not reached — reported clean
#: while the module docstring stated the rule generally.
_EARLIEST_POINTER: dict[str, str] = {
    "work_spec_ref": "RESOLVED",
    "resolved_plan_ref": "RESOLVED",
    "instruction_audit_ref": "AUDITED",
    "start_decision_ref": "AUDITED",
    "fulfillment_ref": "EVIDENCED",
    "manifest_ref": "EVIDENCED",
    "check_results_ref": "EVIDENCED",
    "coverage_ref": "EVIDENCED",
    "review_ref": "REVIEWED",
    "assurance_candidate_ref": "AWAITING_FINAL",
    "final_decision_ref": "AWAITING_FINAL",
    "summary_ref": "CLOSED",
}

#: `repair_decision_ref` is deliberately NOT in the table above. The repair loop runs
#: REPAIRING -> EVIDENCED -> REVIEWED -> AWAITING_FINAL, so after a repair the state sits at
#: an *earlier* stage index while legitimately carrying a pointer from a later one. A stage
#: comparison would report that as premature. What actually bounds it is the round: the
#: pointer may exist only once a repair has been authorized.
_REPAIR_ROUND_POINTER = "repair_decision_ref"


def _stage_index(status: str) -> int:
    return _STAGE_ORDER.index(status) if status in _STAGE_ORDER else -1


def required_pointers(status: str) -> tuple[str, ...]:
    """Every pointer a run at `status` must carry, accumulated over the stages it passed."""
    if status == "STOPPED_REPLAN":
        # A stop can happen anywhere, so nothing beyond the resolution pointers is implied.
        return _REQUIRED_POINTERS["RESOLVED"]
    index = _stage_index(status)
    if index < 0:
        raise SpecGap(f"{CODE}-UNKNOWN-STATUS unknown assurance status: {status}")
    # REPAIRING sits between REVIEWED and AWAITING_FINAL in the flow but is not on the path
    # to AWAITING_FINAL, so its own pointer is required only when the run is in it.
    accumulated: list[str] = []
    for stage in _STAGE_ORDER[: index + 1]:
        if stage == "REPAIRING" and status != "REPAIRING":
            continue
        accumulated.extend(_REQUIRED_POINTERS[stage])
    return tuple(accumulated)


# ---------------------------------------------------------------------------
# Transition legality
# ---------------------------------------------------------------------------


def check_transition(state: Mapping[str, Any], next_status: str) -> Report:
    """Is moving from this state's status to `next_status` legal (contract §8)?"""
    # Checked FIRST, before either field is dereferenced. An earlier version guarded only the
    # round and did so after reading `state["status"]`, so a state missing its status still
    # raised. Reported rather than defaulted: a state missing either field cannot be judged
    # against the transition table or the single-repair rule, and silently reading an absent
    # round as 0 would make a second repair legal on a malformed document.
    missing = [field for field in ("status", "repair_round") if field not in state]
    if missing:
        return report_of(
            [
                Issue(
                    f"{CODE}-STATE-INCOMPLETE",
                    f"the state carries no {' and no '.join(missing)}, so this transition could "
                    "not be judged",
                    missing[0],
                )
            ]
        )

    current = state["status"]
    if current not in _SUCCESSORS:
        return report_of([Issue(f"{CODE}-UNKNOWN-STATUS", f"unknown status: {current}", "status")])
    if next_status not in _SUCCESSORS:
        return report_of(
            [Issue(f"{CODE}-UNKNOWN-STATUS", f"unknown target status: {next_status}", "status")]
        )

    issues: list[Issue] = []

    if current in TERMINAL_STATUSES:
        issues.append(
            Issue(
                f"{CODE}-TERMINAL",
                f"{current} is terminal; a run that has ended does not continue",
                "status",
            )
        )
    elif next_status != "STOPPED_REPLAN" and next_status not in _SUCCESSORS[current]:
        issues.append(
            Issue(
                f"{CODE}-ILLEGAL-TRANSITION",
                f"{current} -> {next_status} is not a legal transition; legal successors are "
                + ", ".join((*_SUCCESSORS[current], "STOPPED_REPLAN")),
                "status",
            )
        )

    # --- V3-D6: exactly one repair round exists ---
    if next_status == "REPAIRING" and state["repair_round"] != 0:
        issues.append(
            Issue(
                f"{CODE}-SECOND-REPAIR",
                f"the run is already at repair round {state['repair_round']}; V3-D6 permits one "
                "user-approved repair and no second fix",
                "repair_round",
            )
        )
    return report_of(issues)


def check_state_pointers(state: Mapping[str, Any]) -> Report:
    """The pointer conditionals for the state's own status (N0 residual R2, N2-A7)."""
    schema_report = validate("state", state)
    if not schema_report.ok:
        return schema_report

    status = state["status"]
    issues: list[Issue] = []

    for field in required_pointers(status):
        if not state.get(field):
            issues.append(
                Issue(
                    f"{CODE}-POINTER-REQUIRED",
                    f"status {status} requires {field}; without it the status claims a stage that "
                    "left no record",
                    field,
                )
            )

    if status == "STOPPED_REPLAN" and not state.get("blockers"):
        issues.append(
            Issue(
                f"{CODE}-STOP-WITHOUT-REASON",
                "STOPPED_REPLAN carries no blockers, so nothing records why the run stopped",
                "blockers",
            )
        )

    # --- no temporal self-binding: a pointer from a stage this run has not reached ---
    #
    # A run that has been through a repair (`repair_round == 1`) has already reached REVIEWED
    # once, so every pointer produced at or before that stage is legitimate wherever the run
    # now sits — the loop goes back to EVIDENCED, and comparing stage indices alone would
    # report the entire round-0 evidence set as premature.
    repaired = state["repair_round"] >= 1
    for field, earliest in _EARLIEST_POINTER.items():
        if not state.get(field):
            continue
        if status == "STOPPED_REPLAN":
            continue  # a stop can happen after any stage; its pointers are whatever existed
        if repaired and _stage_index(earliest) <= _stage_index("REVIEWED"):
            continue
        if _stage_index(status) < _stage_index(earliest):
            issues.append(
                Issue(
                    f"{CODE}-POINTER-PREMATURE",
                    f"{field} exists at status {status} but cannot be produced before {earliest}; "
                    "a document that precedes the thing it binds is bound to nothing",
                    field,
                )
            )

    if state.get(_REPAIR_ROUND_POINTER) and not repaired:
        issues.append(
            Issue(
                f"{CODE}-POINTER-PREMATURE",
                f"{_REPAIR_ROUND_POINTER} exists while the run is still at repair round 0; a "
                "repair authorization cannot precede the repair it authorizes",
                _REPAIR_ROUND_POINTER,
            )
        )

    if state["repair_round"] == 1 and not state.get("repair_decision_ref"):
        issues.append(
            Issue(
                f"{CODE}-REPAIR-WITHOUT-AUTHORIZATION",
                "the run is at repair round 1 but carries no repair decision; a repair with no "
                "recorded authorization is an unapproved rewrite of the candidate",
                "repair_decision_ref",
            )
        )

    return schema_report + report_of(issues)


def advance_checked(state: Mapping[str, Any], next_status: str, **fields: Any) -> dict[str, Any]:
    """Advance the state only when the transition and the resulting pointers are legal.

    Raises rather than returning a bad state: a controller that silently produced an illegal
    state would leave the illegality for a later reader to discover, which is the class of
    defect this module exists to close.
    """
    check_transition(state, next_status).require(SpecGap)
    updated = dict(state)
    updated["status"] = next_status
    for key, value in fields.items():
        if value is None:
            updated.pop(key, None)
        else:
            updated[key] = value
    if next_status == "REPAIRING":
        updated["repair_round"] = 1
    check_state_pointers(updated).require(SpecGap)
    return updated


# ---------------------------------------------------------------------------
# The one repair (N2-A4, N2-A5)
# ---------------------------------------------------------------------------


def reviewed_candidate_ref(review: Mapping[str, Any]) -> Any:
    """The candidate a ReviewResult covers, read from the shape that result declares.

    v1 carries `candidate_ref` at the root. The v2 successor moved it inside `subject`
    (review.v2.schema.json) and carries nothing at the root, so a root-only read reports
    every v2 review as unbound: the guard stays fail-closed, but it fails on a shape
    mismatch rather than on a real one, and the property it exists to check goes untested
    for exactly the runs the successor governs. Witnessed at p3-corr, the first v2 run to
    reach a repair.

    Keyed on the declared version rather than trying both shapes in turn — reading whichever
    happens to be present would make an unknown future version silently match one of them,
    the cross-version fallback wave 1 ruled out.
    """
    # Imported here rather than at module scope: flow is the older module, and a top-level
    # edge into the successor would make the successor unable to import flow later.
    from rsclib.document_harness.review_result_v2 import result_schema_kind

    if result_schema_kind(review) == "review_result_v2":
        subject = review.get("subject")
        return subject.get("candidate_ref") if isinstance(subject, Mapping) else None
    return review.get("candidate_ref")


def check_repair_decision(
    decision: Mapping[str, Any],
    review: Mapping[str, Any],
    plan: Mapping[str, Any],
) -> Report:
    """REPAIR binds the original candidate, the accepted findings and a minimum boundary.

    The boundary check is the one worth reading: a repair boundary that reaches outside the
    run's own effective boundary would let the single approved repair write where the original
    candidate was never allowed to. That is not a repair, it is a second, wider authorization
    obtained by calling it a fix.
    """
    schema_report = validate("decision", decision)
    if not schema_report.ok:
        return schema_report

    if decision["phase"] != "REPAIR":
        return report_of(
            [
                Issue(
                    f"{CODE}-PHASE",
                    f"expected a REPAIR decision, got {decision['phase']}",
                    "phase",
                )
            ]
        )

    issues: list[Issue] = []
    target = decision["target"]

    # --- the decision answers THIS review: same work, same run ---
    #
    # Checked before the NO_REPAIR return below, because a declined repair still binds what
    # it declined: a NO_REPAIR naming another run's review would close this run's repair
    # phase on a decision the user made about something else, and used to report clean.
    # run_id is schema-optional on a decision, so an absent side is reported as unverified
    # rather than silently skipped — the fail-open shape this function has been bitten by.
    for field, mismatch_code in (
        ("work_id", f"{CODE}-REPAIR-WORK-MISMATCH"),
        ("run_id", f"{CODE}-REPAIR-RUN-MISMATCH"),
    ):
        decided = decision.get(field)
        reviewed_value = review.get(field)
        if decided is None or reviewed_value is None:
            side = "decision" if decided is None else "review"
            issues.append(
                Issue(
                    f"{CODE}-REPAIR-BINDING-UNVERIFIED",
                    f"the {side} names no {field}, so it could not be checked that this repair "
                    "decision answers this review; this is an unverified property, not a "
                    "satisfied one",
                    field,
                )
            )
        elif decided != reviewed_value:
            issues.append(
                Issue(
                    mismatch_code,
                    f"the repair decision names {field} '{decided}' but the review it answers "
                    f"carries '{reviewed_value}'",
                    field,
                )
            )

    # --- the repair binds the candidate that was reviewed, not some later one ---
    #
    # `if reviewed_commit and ...` silently switched this guard off whenever the review named
    # only a branch, and raised outright when it named no candidate at all — the same
    # fail-open shape the boundary check below reports as UNVERIFIED and `check_package`
    # reports as RECORD-CANDIDATE-UNBOUND. It is reported here for the same reason: a repair
    # that cannot be shown to bind the reviewed candidate is unverified, not approved.
    reviewed_ref = reviewed_candidate_ref(review)
    reviewed_commit = reviewed_ref.get("commit") if isinstance(reviewed_ref, Mapping) else None
    target_ref = target.get("candidate_ref")
    target_commit = target_ref.get("commit") if isinstance(target_ref, Mapping) else None
    if not reviewed_commit:
        issues.append(
            Issue(
                f"{CODE}-REPAIR-BINDING-UNVERIFIED",
                "the review names no exact candidate commit, so it could not be checked that the "
                "repair binds the candidate that was reviewed; this is an unverified property, "
                "not a satisfied one",
                "target/candidate_ref",
            )
        )
    elif target_commit != reviewed_commit:
        issues.append(
            Issue(
                f"{CODE}-REPAIR-WRONG-CANDIDATE",
                f"the repair binds candidate {str(target_commit)[:12]} but the review it answers "
                f"covered {reviewed_commit[:12]}",
                "target/candidate_ref",
            )
        )

    if decision["decision"] == "NO_REPAIR":
        # The user declined the repair, and the run proceeds to FINAL with the findings still
        # standing. The accepted-findings and boundary sections below bind nothing for a
        # decline — but the decline itself binds this run's reviewed candidate, which is why
        # the binding checks above run first instead of being skipped (defect M5: this return
        # once sat before them, so a NO_REPAIR aimed at anything at all reported clean).
        return schema_report + report_of(issues)

    # --- every accepted finding must exist in that review ---
    known = {finding["finding_id"] for finding in review.get("findings", [])}
    for unknown in sorted(set(target.get("accepted_finding_ids", [])) - known):
        issues.append(
            Issue(
                f"{CODE}-ACCEPTED-FINDING-UNKNOWN",
                f"the repair accepts finding '{unknown}', which the review does not contain",
                "target/accepted_finding_ids",
            )
        )

    # --- the repair boundary may only narrow, never widen ---
    #
    # The plan's boundary is what "narrower" is measured against, so a plan that does not
    # carry one disables this guard entirely — the fail-open shape, reached by passing a
    # plan-shaped mapping with the field missing. It is reported rather than skipped: an
    # unmeasurable boundary is an unverified property, not a satisfied one.
    effective = plan.get("effective_change_boundary") or {}
    repair_boundary = target.get("repair_boundary") or {}
    if not effective.get("write_scope"):
        issues.append(
            Issue(
                f"{CODE}-REPAIR-BOUNDARY-UNVERIFIED",
                "the plan carries no effective write scope, so it could not be checked that the "
                "repair boundary only narrows it; this is an unverified property, not a "
                "satisfied one",
                "target/repair_boundary",
            )
        )
    for path in repair_boundary.get("write_scope", []):
        if effective.get("write_scope") and not covered_by(path, effective["write_scope"]):
            issues.append(
                Issue(
                    f"{CODE}-REPAIR-BOUNDARY-WIDENS",
                    f"repair boundary path '{path}' falls outside the run's effective write scope; "
                    "a repair may narrow the boundary, never widen it",
                    "target/repair_boundary/write_scope",
                )
            )
        if effective.get("out") and covered_by(path, effective["out"]):
            issues.append(
                Issue(
                    f"{CODE}-REPAIR-BOUNDARY-WIDENS",
                    f"repair boundary path '{path}' is inside the run's negative boundary",
                    "target/repair_boundary/write_scope",
                )
            )

    return schema_report + report_of(issues)


@dataclasses.dataclass(frozen=True)
class EvidenceSet:
    """The regenerable evidence of one repair round, by digest.

    `checks` is a tuple so an added or removed CheckResult changes the set even when every
    surviving result is unchanged.
    """

    fulfillment: str
    manifest: str
    coverage: str
    package: str
    checks: tuple[str, ...] = ()

    def as_map(self) -> dict[str, Any]:
        return {
            "fulfillment": self.fulfillment,
            "manifest": self.manifest,
            "coverage": self.coverage,
            "package": self.package,
            "checks": self.checks,
        }


def check_repair_regeneration(before: EvidenceSet, after: EvidenceSet) -> Report:
    """Invariant 11 / N2-A5: C2 regenerates every piece of evidence, inheriting none.

    Carrying a round-0 document into round 1 is the "check candidate A, report candidate B"
    class arriving through the back door: the document would describe C while the run reports
    on C2, and every digest in it would still verify.
    """
    issues: list[Issue] = []
    for name, old, new in (
        ("fulfillment", before.fulfillment, after.fulfillment),
        ("manifest", before.manifest, after.manifest),
        ("coverage", before.coverage, after.coverage),
        ("package", before.package, after.package),
    ):
        if old == new:
            issues.append(
                Issue(
                    f"{CODE}-EVIDENCE-NOT-REGENERATED",
                    f"the repaired candidate reuses the round-0 {name}; it describes the candidate "
                    "that was replaced",
                    name,
                )
            )
    if before.checks and before.checks == after.checks:
        issues.append(
            Issue(
                f"{CODE}-CHECKS-NOT-RERUN",
                "every check result is byte-identical to round 0, so the checks were not re-run "
                "against the repaired candidate",
                "checks",
            )
        )
    return report_of(issues)


def check_verify_outcome(verify: Mapping[str, Any], repair_decision: Mapping[str, Any]) -> Report:
    """N2-A6: the VERIFY covered what the user approved, and a problem still standing stops.

    `repair_decision` is **required with no default**. Without it nothing in v3 ever compared
    the findings a VERIFY claims to have covered against the findings the user actually
    approved for repair: the reviewer could declare `accepted_finding_ids: [C]` where the
    decision approved `[A, B]`, and every digest, every summary and every other check would
    still verify. That is the same defect shape as a summary terminating a candidate the user
    never decided about — the user's authorization compared to nothing — arriving one step
    later in the flow.

    The other two things V3-D6 scopes a VERIFY to are self-declared booleans, and this module
    already checks those; this is the one of the three with a second document to reconcile
    against, so leaving it unreconciled was the weakest point of the set rather than an
    acceptable ceiling. What is still *not* established, and cannot be here, is whether the
    reviewer really looked — only that the scope it declared is the scope that was authorized.

    There is no second fix and no review-of-review, so a blocker still standing leaves only
    `STOPPED_REPLAN` or a user `ACCEPT_WITH_LIMITATIONS` naming what is open.
    """
    issues: list[Issue] = []
    if verify["review_round"] != "VERIFY":
        return report_of(
            [Issue(f"{CODE}-NOT-VERIFY", f"expected a VERIFY result, got {verify['review_round']}", "review_round")]
        )

    # --- the declared scope is the authorized scope ---
    target = repair_decision.get("target")
    approved = set(target.get("accepted_finding_ids", []) or []) if isinstance(target, Mapping) else set()
    scope = verify.get("verify_scope")
    covered = set(scope.get("accepted_finding_ids", []) or []) if isinstance(scope, Mapping) else set()

    if repair_decision.get("decision") != "APPLY_ACCEPTED_FINDINGS":
        issues.append(
            Issue(
                f"{CODE}-VERIFY-WITHOUT-REPAIR",
                f"a VERIFY answers a repair, but the decision supplied is "
                f"'{repair_decision.get('decision')}'; there is nothing for it to have verified",
                "verify_scope/accepted_finding_ids",
            )
        )
    else:
        for missed in sorted(approved - covered):
            issues.append(
                Issue(
                    f"{CODE}-VERIFY-SCOPE-MISMATCH",
                    f"the user approved finding '{missed}' for repair but the VERIFY does not "
                    "claim to have covered it",
                    "verify_scope/accepted_finding_ids",
                )
            )
        for extra in sorted(covered - approved):
            issues.append(
                Issue(
                    f"{CODE}-VERIFY-SCOPE-MISMATCH",
                    f"the VERIFY claims to have covered finding '{extra}', which the user did not "
                    "approve for repair",
                    "verify_scope/accepted_finding_ids",
                )
            )
    if verify["verdict"] == "SPEC_GAP":
        issues.append(
            Issue(
                f"{CODE}-VERIFY-SPEC-GAP",
                "the VERIFY returned SPEC_GAP; a SPEC_GAP stops and is never patched inside the "
                "candidate",
                "verdict",
            )
        )
    remaining = [f["finding_id"] for f in verify.get("findings", []) if f["blocking"]]
    if remaining:
        issues.append(
            Issue(
                f"{CODE}-BLOCKER-AFTER-VERIFY",
                f"{len(remaining)} blocking finding(s) remain after the single permitted repair "
                f"({', '.join(remaining)}); the run stops rather than opening a second round",
                "findings",
            )
        )
    return report_of(issues)


# ---------------------------------------------------------------------------
# The governance obligation (N1 residual R2)
# ---------------------------------------------------------------------------


def governance_state(
    *, result_ref: Mapping[str, Any] | None = None, skip_reason: str | None = None
) -> dict[str, Any]:
    """Build the AssuranceCandidate's `governance_scan` block. Fails closed.

    Exactly one of the two must be supplied. Supplying neither is refused rather than
    defaulted, because the default would have to be one of "assume it ran" or "assume it did
    not", and both are a guess recorded as a fact.
    """
    if (result_ref is None) == (skip_reason is None):
        raise SpecGap(
            f"{CODE}-GOVERNANCE-UNSTATED a run must record either the governance scan result or "
            "an explicit reason it was skipped; it cannot record neither or both"
        )
    if result_ref is not None:
        return {"included": True, "result_ref": dict(result_ref)}
    return {"included": False, "skip_reason": skip_reason}


def governance_disclosures(
    candidate: Mapping[str, Any], candidate_ref: Mapping[str, Any]
) -> list[dict[str, Any]]:
    """Turn a skipped governance scan into a disclosure the user sees before deciding.

    A skip is legal; a silent skip is not. This is deliberately a *disclosure* and not an
    issue: N1-R2 requires the run to include the scan **or record explicitly that it was
    skipped**, so a recorded skip has met the obligation and inflating it into a blocker would
    misrepresent what the rule asks for. What it must never do is disappear.
    """
    scan = candidate.get("governance_scan")
    if not isinstance(scan, Mapping):
        # A malformed block is disclosed, never dereferenced. Saying nothing here would be the
        # exact failure this discharge of N1-R2 exists to prevent: silence about whether the
        # governance scan ran.
        return [
            {
                "statement": "the governance scan state on this candidate is malformed, so "
                "whether the scan ran could not be read",
                "source_ref": dict(candidate_ref),
            }
        ]
    if scan.get("included"):
        return []
    return [
        {
            "statement": "the governance frontmatter scan did not run in this run: "
            + scan["skip_reason"][:400],
            "source_ref": dict(candidate_ref),
        }
    ]


def check_governance_obligation(candidate: Mapping[str, Any]) -> Report:
    """The obligation itself: the state must be stated, whichever way it went."""
    scan = candidate.get("governance_scan")
    if not isinstance(scan, Mapping) or not scan:
        # `not scan` alone let a truthy non-mapping through to `scan["included"]` and raised.
        return report_of(
            [
                Issue(
                    f"{CODE}-GOVERNANCE-UNSTATED",
                    "the assurance candidate does not say whether the governance scan ran; a check "
                    "nobody is obliged to record is a check that will eventually not be run",
                    "governance_scan",
                )
            ]
        )
    if scan.get("included") and not scan.get("result_ref"):
        return report_of(
            [
                Issue(
                    f"{CODE}-GOVERNANCE-UNEVIDENCED",
                    "the run claims the governance scan ran but references no result",
                    "governance_scan/result_ref",
                )
            ]
        )
    return Report()


# ---------------------------------------------------------------------------
# Binding helpers
# ---------------------------------------------------------------------------


def review_binding(package: Mapping[str, Any], review: Mapping[str, Any]) -> dict[str, str]:
    """The two digests that tie a round together, for the caller to record as pointers."""
    return {"package_digest": package_digest(package), "review_digest": result_digest(review)}


def decision_digest(decision: Mapping[str, Any]) -> str:
    return canonical_digest(decision)


def render_flow(state: Mapping[str, Any]) -> str:
    """A user-facing position line: where the run is and what it still owes."""
    status = state["status"]
    missing = [field for field in required_pointers(status) if not state.get(field)]
    if status in TERMINAL_STATUSES:
        legal_next = "— (terminal)"
    else:
        legal_next = ", ".join((*_SUCCESSORS.get(status, ()), "STOPPED_REPLAN"))
    lines = [
        f"status       : {status}",
        f"repair_round : {state['repair_round']}",
        f"legal next   : {legal_next}",
    ]
    for field in missing:
        lines.append(f"  !! missing required pointer: {field}")
    for blocker in state.get("blockers", []):
        lines.append(f"  !! blocker: {blocker}")
    return "\n".join(lines)


__all__ = [
    "EvidenceSet",
    "TERMINAL_STATUSES",
    "advance_checked",
    "check_governance_obligation",
    "check_repair_decision",
    "check_repair_regeneration",
    "check_state_pointers",
    "check_transition",
    "check_verify_outcome",
    "decision_digest",
    "governance_disclosures",
    "governance_state",
    "render_flow",
    "required_pointers",
    "review_binding",
]
