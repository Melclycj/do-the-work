"""AssuranceCandidate and AssuranceSummary — the two controller bindings (N2-A7..A9).

The controller's job is narrow and its temptation is specific. It may freeze subjects and
bind refs; it may **not** restate evidence with stronger epistemic meaning (V3-D5). The
failure mode is not malice, it is summarisation: a controller that assembles a user-facing
view naturally wants to say "checks passed, review clean", and the moment it does, a verdict
exists that no verifier or reviewer authored.

So the surface here is deliberately poor in claims and rich in references, and the two guards
that matter are both about *faithfulness rather than judgment*:

* `unresolved_finding_ids` must be **exactly** the reviewer's blocking findings. Dropping one
  weakens the reviewer's claim; adding one invents a claim the reviewer never made. This is
  the mechanical core of N2-A9 — the controller is checked against the document it is binding,
  not trusted to summarise it.
* the summary's `outcome` and `limitations` must be **exactly** the user's own decision. A
  controller that could quietly turn `ACCEPT_WITH_LIMITATIONS` into `ACCEPT`, or drop a
  limitation the user attached, would be deciding on the user's behalf.
* the refs to the reviewer's and the user's documents are bound by content, not stored on
  faith: each supplied review round's canonical digest must appear among `review_refs`, and
  the summary's `final_decision_ref` must carry the canonical digest of the FINAL decision
  in hand — a count, or a verbatim-stored pointer, is satisfied by refs to anything.

The other axis is temporal (N2-A7). An `AssuranceCandidate` exists before the FINAL decision
and therefore cannot reference it or the summary; exactly one summary is generated after.
The schema makes a self-binding candidate unrepresentable; this module refuses to generate a
summary from anything but a real FINAL decision.
"""
from __future__ import annotations

import pathlib
from typing import Any, Mapping, Sequence  # Mapping is also used as a runtime type guard

from rsclib.document_harness import (
    Issue,
    Report,
    SpecGap,
    canonical_digest,
    load_json,
    report_of,
    validate,
)
from rsclib.document_harness.review import blocking_findings, validate_n2

CODE = "V3-ASSURANCE"

#: Fields a candidate must never carry, because each names a document produced after it.
#: The schema already rejects them through additionalProperties:false; they are listed here
#: so the rule is greppable and so the guard reports *which* one appeared rather than a
#: generic schema error.
FORWARD_FIELDS = ("final_decision_ref", "summary_ref", "outcome", "verdict", "decision")


def bind_candidate(
    *,
    assurance_candidate_id: str,
    work_id: str,
    run_id: str,
    repair_round: int,
    candidate_ref: Mapping[str, Any],
    base_revision: str,
    bound_by: str,
    work_spec_ref: Mapping[str, Any],
    resolved_plan_ref: Mapping[str, Any],
    instruction_audit_ref: Mapping[str, Any],
    fulfillment_ref: Mapping[str, Any],
    manifest_ref: Mapping[str, Any],
    coverage_ref: Mapping[str, Any],
    review_refs: Sequence[Mapping[str, Any]],
    governance_scan: Mapping[str, Any],
    check_result_refs: Sequence[Mapping[str, Any]] = (),
    unresolved_finding_ids: Sequence[str] = (),
    disclosures: Sequence[Mapping[str, Any]] = (),
    bound_at: str | None = None,
) -> dict[str, Any]:
    """Assemble the pre-decision binding. Assembling is not judging."""
    candidate: dict[str, Any] = {
        "assurance_candidate_id": assurance_candidate_id,
        "work_id": work_id,
        "run_id": run_id,
        "repair_round": repair_round,
        "candidate_ref": dict(candidate_ref),
        "base_revision": base_revision,
        "bound_by": bound_by,
        "work_spec_ref": dict(work_spec_ref),
        "resolved_plan_ref": dict(resolved_plan_ref),
        "instruction_audit_ref": dict(instruction_audit_ref),
        "fulfillment_ref": dict(fulfillment_ref),
        "manifest_ref": dict(manifest_ref),
        "coverage_ref": dict(coverage_ref),
        "review_refs": [dict(ref) for ref in review_refs],
        "governance_scan": dict(governance_scan),
    }
    if bound_at:
        candidate["bound_at"] = bound_at
    if check_result_refs:
        candidate["check_result_refs"] = [dict(ref) for ref in check_result_refs]
    if unresolved_finding_ids:
        candidate["unresolved_finding_ids"] = list(unresolved_finding_ids)
    if disclosures:
        candidate["disclosures"] = [dict(entry) for entry in disclosures]
    return candidate


def check_assurance_candidate(
    candidate: Mapping[str, Any],
    record: Mapping[str, Any],
    reviews: Sequence[Mapping[str, Any]],
) -> Report:
    """N2-A7 and N2-A9: bound to the right things, and faithful to the reviewer.

    `reviews` is every review round that happened — the FULL, plus the VERIFY when there was
    a repair. The unresolved set is judged against all of them, because a blocker raised at
    FULL and left standing through VERIFY is still open.
    """
    # --- N2-A7, run FIRST and unconditionally ---
    #
    # These are plain key inspections that assume nothing about the document's shape, and the
    # schema's additionalProperties:false rejects every one of these fields — so validating
    # first would shadow them permanently and the reader would get a generic "unknown
    # property" error instead of the reason the property is forbidden. Deleting the check as
    # redundant was the other option and is rejected for the reason V3-N1 recorded when it hit
    # the same shape: in a governance record the reason is the part worth reading, and a
    # greppable code per invariant is what makes it auditable.
    issues: list[Issue] = []
    for field in FORWARD_FIELDS:
        if field in candidate:
            issues.append(
                Issue(
                    f"{CODE}-SELF-BINDING",
                    f"the assurance candidate carries '{field}', which names a document produced "
                    "after it; a binding cannot include the thing it precedes",
                    field,
                )
            )

    schema_report = validate_n2("assurance_candidate", candidate)
    if not schema_report.ok:
        return schema_report + report_of(issues)

    if candidate["run_id"] != record["run_id"]:
        issues.append(Issue(f"{CODE}-RUN-MISMATCH", "candidate names a different run_id", "run_id"))
    if candidate["candidate_ref"].get("commit") != record["candidate_ref"].get("commit"):
        issues.append(
            Issue(
                f"{CODE}-WRONG-CANDIDATE",
                "the assurance candidate binds a different payload candidate than the record",
                "candidate_ref/commit",
            )
        )
    if candidate["repair_round"] != record["repair_round"]:
        issues.append(
            Issue(
                f"{CODE}-ROUND-MISMATCH",
                f"candidate binds repair round {candidate['repair_round']} but the record is round "
                f"{record['repair_round']}",
                "repair_round",
            )
        )

    # --- N2-A9: the unresolved set is exactly the reviewer's blocking findings ---
    open_blockers = {
        finding["finding_id"] for review in reviews for finding in blocking_findings(review)
    }
    declared = set(candidate.get("unresolved_finding_ids", []))
    for dropped in sorted(open_blockers - declared):
        issues.append(
            Issue(
                f"{CODE}-BLOCKER-DROPPED",
                f"blocking finding '{dropped}' is recorded by the reviewer but absent from the "
                "candidate's unresolved set; the controller may bind a reviewer's claim, never "
                "weaken it",
                "unresolved_finding_ids",
            )
        )
    for invented in sorted(declared - open_blockers):
        issues.append(
            Issue(
                f"{CODE}-BLOCKER-INVENTED",
                f"the candidate lists '{invented}' as unresolved but no review records it as a "
                "blocking finding",
                "unresolved_finding_ids",
            )
        )

    # --- every review round that happened must be bound ---
    if len(candidate["review_refs"]) != len(reviews):
        issues.append(
            Issue(
                f"{CODE}-REVIEW-BINDING-INCOMPLETE",
                f"{len(reviews)} review round(s) happened but the candidate binds "
                f"{len(candidate['review_refs'])}",
                "review_refs",
            )
        )

    # --- and bound by content: a count alone is satisfied by refs to anything ---
    #
    # The digests compared are canonical digests of the review documents already in hand —
    # the kind the authoring precedent writes (w1-r1 run_bind) — so this adds no I/O. The
    # six evidence/spec refs stay stored-without-content-check by the 2026-07-30 C2 ruling
    # (M6 option B): supersession-2 narrowed state-pointer digests to the five protected
    # fields, so no independently-authored digest is in hand to check them against, and a
    # digest recomputed over files the same actor may rewrite binds nobody.
    known = {canonical_digest(review): review.get("result_id", "<unnamed>") for review in reviews}
    bound_digests = {entry["digest_sha256"] for entry in candidate["review_refs"]}
    for review_digest, result_id in known.items():
        if review_digest not in bound_digests:
            issues.append(
                Issue(
                    f"{CODE}-REVIEW-UNBOUND",
                    f"review round '{result_id}' happened but no review_ref binds its bytes; "
                    "binding the count is not binding the review",
                    "review_refs",
                )
            )
    for stray in sorted(bound_digests - set(known)):
        issues.append(
            Issue(
                f"{CODE}-REVIEW-INVENTED",
                f"review_refs binds digest '{stray[:12]}' which is no review round of this "
                "run; the controller may bind the reviewer's document, never substitute one",
                "review_refs",
            )
        )

    return schema_report + report_of(issues)


def candidate_digest(candidate: Mapping[str, Any]) -> str:
    return canonical_digest(candidate)


# ---------------------------------------------------------------------------
# The terminal summary
# ---------------------------------------------------------------------------


def generate_summary(
    *,
    summary_id: str,
    candidate: Mapping[str, Any],
    candidate_ref: Mapping[str, Any],
    decision: Mapping[str, Any],
    decision_ref: Mapping[str, Any],
    promotion: Mapping[str, Any],
    generated_by: str,
    generated_at: str | None = None,
) -> dict[str, Any]:
    """Generate the single terminal binding — only from a real FINAL decision (invariant 12).

    Refuses rather than defaults. A summary generated without a FINAL decision would be the
    controller closing a run the user never closed, and the whole point of the phase is that
    the user is the trust terminal.
    """
    validate("decision", decision).require(SpecGap)
    if decision["phase"] != "FINAL":
        raise SpecGap(
            f"{CODE}-NOT-FINAL a summary follows the FINAL decision; got phase "
            f"{decision['phase']}"
        )
    # Both the decision and the ref to record for it are in hand right here, which is the
    # one moment the two can be reconciled without I/O — so a mismatch refuses rather than
    # ships (defect M7: the ref used to be stored verbatim and compared to nothing, ever).
    if decision_ref.get("digest_sha256") != canonical_digest(decision):
        raise SpecGap(
            f"{CODE}-DECISION-BINDING-MISMATCH the decision_ref does not bind the FINAL "
            "decision this summary is generated from; a summary citing a decision other "
            "than the one in hand would close the run on an authorization nobody checked"
        )

    summary: dict[str, Any] = {
        "summary_id": summary_id,
        "work_id": candidate["work_id"],
        "run_id": candidate["run_id"],
        "assurance_candidate_ref": dict(candidate_ref),
        "final_decision_ref": dict(decision_ref),
        "outcome": decision["decision"],
        "promotion": dict(promotion),
        "generated_by": generated_by,
    }
    if decision.get("limitations"):
        summary["limitations"] = list(decision["limitations"])
    if generated_at:
        summary["generated_at"] = generated_at
    return summary


def check_summary(
    summary: Mapping[str, Any],
    candidate: Mapping[str, Any],
    decision: Mapping[str, Any],
) -> Report:
    """Invariants 12 and 13, N2-A8 and N2-A9: faithful to the user, and never promoting a refusal."""
    # --- invariant 13 / N2-A8, run FIRST and unconditionally ---
    #
    # The schema also holds this rule (a REJECT/REPLAN summary pins promoted to false, and a
    # promotion requires promoted_to), so validating first would shadow both codes and a
    # promotion-after-refusal would surface only as a generic schema error. This is the one
    # place where a wrong value silently ships bytes the user declined, so it reports its own
    # reason. Accessors are defensive because this runs before the shape is known.
    issues: list[Issue] = []
    # `or {}` alone was not defensive: it returns the value itself for any truthy non-mapping,
    # so a `promotion` that was a string crashed the next `.get` with an AttributeError. A
    # checker that raises on a malformed document instead of reporting it takes the run down
    # rather than recording what happened — and the malformed document is exactly the class
    # this pre-schema position exists to serve.
    promotion = summary.get("promotion")
    if not isinstance(promotion, Mapping):
        promotion = {}
    outcome = summary.get("outcome")
    if outcome in ("REJECT", "REPLAN") and promotion.get("promoted"):
        issues.append(
            Issue(
                f"{CODE}-PROMOTED-AFTER-REFUSAL",
                f"the payload was promoted despite a {outcome} decision",
                "promotion/promoted",
            )
        )
    if promotion.get("promoted") and not promotion.get("promoted_to"):
        issues.append(
            Issue(
                f"{CODE}-PROMOTION-UNRECORDED",
                "a promotion happened but nothing records where the payload went; accepted "
                "promotion is explicit and recorded, never implied by acceptance",
                "promotion/promoted_to",
            )
        )

    schema_report = validate_n2("assurance_summary", summary)
    if not schema_report.ok:
        return schema_report + report_of(issues)

    expected = candidate_digest(candidate)
    if summary["assurance_candidate_ref"]["digest_sha256"] != expected:
        issues.append(
            Issue(
                f"{CODE}-CANDIDATE-BINDING-MISMATCH",
                "the summary binds different AssuranceCandidate bytes than the ones supplied",
                "assurance_candidate_ref/digest_sha256",
            )
        )

    # --- the recorded decision pointer names the decision actually supplied ---
    #
    # The outcome/limitations checks below prove faithfulness to the decision IN HAND; this
    # proves the summary's permanent pointer names that same decision, so the record cannot
    # cite decision A while every content check below ran against decision B (defect M7).
    if summary["final_decision_ref"]["digest_sha256"] != canonical_digest(decision):
        issues.append(
            Issue(
                f"{CODE}-DECISION-BINDING-MISMATCH",
                "the summary's final_decision_ref binds different decision bytes than the "
                "FINAL decision supplied; the recorded authorization is not the one checked",
                "final_decision_ref/digest_sha256",
            )
        )

    # --- the user decided about THIS candidate ---
    #
    # The summary↔candidate binding above proves the controller terminated the candidate it
    # was handed; it says nothing about which candidate the *user* was looking at. Without
    # this comparison a summary can faithfully terminate candidate A while the FINAL decision
    # it cites was made about candidate B, and every digest still verifies — "check candidate
    # A, report candidate B" (V3-D5) at the one step where the user is the trust terminal.
    # Chained `.get` is only defensive against *absent* keys; a truthy non-mapping `target`
    # raised here. This function never validates the decision it is handed, so the shape has
    # to be guarded rather than assumed.
    decided_target = decision.get("target")
    decided_ref = decided_target.get("assurance_candidate_ref") if isinstance(decided_target, Mapping) else None
    decided_about = decided_ref.get("digest_sha256") if isinstance(decided_ref, Mapping) else None
    if decided_about != expected:
        issues.append(
            Issue(
                f"{CODE}-DECISION-TARGET-MISMATCH",
                "the FINAL decision was made about a different AssuranceCandidate than the one "
                "this summary terminates",
                "final_decision_ref",
            )
        )

    # --- N2-A9: the outcome is the user's decision, unaltered ---
    if summary["outcome"] != decision.get("decision"):
        issues.append(
            Issue(
                f"{CODE}-OUTCOME-ALTERED",
                f"the summary records outcome '{summary['outcome']}' but the user decided "
                f"'{decision.get('decision')}'",
                "outcome",
            )
        )
    if decision.get("phase") != "FINAL":
        issues.append(
            Issue(
                f"{CODE}-NOT-FINAL",
                f"the summary terminates on a {decision.get('phase')} decision, not a FINAL one",
                "final_decision_ref",
            )
        )

    declared_limits = list(summary.get("limitations", []))
    user_limits = list(decision.get("limitations", []))
    if declared_limits != user_limits:
        issues.append(
            Issue(
                f"{CODE}-LIMITATIONS-ALTERED",
                "the summary's limitations differ from the ones the user acknowledged; a "
                "limitation the user attached is not the controller's to edit or drop",
                "limitations",
            )
        )

    # (invariant 13 / N2-A8 is checked at the top of this function, before schema validation,
    # so that a promotion-after-refusal reports its own reason rather than a schema error.)

    return schema_report + report_of(issues)


def summary_digest(summary: Mapping[str, Any]) -> str:
    return canonical_digest(summary)


def no_promotion(reason: str) -> dict[str, Any]:
    """The explicit not-promoted form. Used by REJECT/REPLAN and by an accept left unpromoted."""
    return {"promoted": False, "reason": reason}


def promoted_to(candidate_ref: Mapping[str, Any], reason: str) -> dict[str, Any]:
    return {"promoted": True, "promoted_to": dict(candidate_ref), "reason": reason}


def render_summary(summary: Mapping[str, Any]) -> str:
    """The user-facing close-out: outcome, what moved, and what was accepted as still open."""
    promotion = summary["promotion"]
    lines = [
        f"outcome      : {summary['outcome']}",
        f"candidate    : bound by digest {summary['assurance_candidate_ref']['digest_sha256'][:12]}",
        f"promoted     : {'yes' if promotion['promoted'] else 'no'}"
        + (f" -> {promotion['promoted_to'].get('branch')}" if promotion["promoted"] else ""),
    ]
    if promotion.get("reason"):
        lines.append(f"  reason     : {promotion['reason']}")
    for limitation in summary.get("limitations", []):
        lines.append(f"  !! accepted limitation: {limitation}")
    return "\n".join(lines)


def load_candidate(path: pathlib.Path | str) -> dict[str, Any]:
    return load_json(path)


def load_summary(path: pathlib.Path | str) -> dict[str, Any]:
    return load_json(path)


__all__ = [
    "FORWARD_FIELDS",
    "bind_candidate",
    "candidate_digest",
    "check_assurance_candidate",
    "check_summary",
    "generate_summary",
    "load_candidate",
    "load_summary",
    "no_promotion",
    "promoted_to",
    "render_summary",
    "summary_digest",
]
