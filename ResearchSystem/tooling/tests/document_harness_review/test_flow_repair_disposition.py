#!/usr/bin/env python3
"""Adversarial half of the V3-N2 acceptance matrix: flow, the one repair, and disposition.

Every test here answers one question — *does the harness actually detect the failure it
claims to detect?* Following the rule V3-N1 set, each method asserts an exact issue **code**
(and usually its exact ``where``) or an exact result **value**; never merely that "something
failed". Every "must fire" assertion is paired with a negative control proving the guard is
not simply always-on.

Coverage:

* ``N2-A4`` — REPAIR binds the reviewed candidate, the accepted finding IDs and a boundary
  that may only narrow (`flow.check_repair_decision`).
* ``N2-A5`` — C2 regenerates fulfillment, manifest, coverage, package and the checks;
  inheriting any one of them is named (`flow.check_repair_regeneration`, `flow.EvidenceSet`).
* ``N2-A6`` — a blocker still standing after VERIFY stops the run, and no second REPAIRING is
  reachable (`flow.check_verify_outcome`, `flow.check_transition`).
* ``N2-A7`` — the pointer conditionals in both directions: a status must carry what its own
  stages produced, and must not carry a pointer from a stage it has not reached. This is
  where inherited residual ``N0-R2`` lands (`flow.check_state_pointers`,
  `summary.check_assurance_candidate`, `summary.generate_summary`).
* ``N2-A8`` — REJECT/REPLAN never promotes; an accepted promotion says where it went and why.
* ``N2-A9`` — the controller is checked against the documents it binds: the unresolved set is
  *exactly* the reviewer's blocking findings, and the summary's outcome and limitations are
  *exactly* the user's decision.
* ``N2-A10`` — a HarnessIssue is post-run, binds its run, and is routed only by a user
  ``ISSUE_TRIAGE`` decision (`issues.check_issue`, `issues.check_triage`,
  `issues.triage_route`).
* ``N2-A11`` — no recursive review (round cap, no third round, no review-of-review), no
  generic waiver/gate vocabulary, and no mutable state or resolution field on a HarnessIssue.
* ``N1-R2`` — a run must state whether the R4 governance scan ran; a skip is explicit,
  reasoned and surfaces as a disclosure (`flow.governance_state`,
  `flow.check_governance_obligation`, `flow.governance_disclosures`).

Two shapes are probed deliberately because this project has been bitten by both:

* **fail-open guards** — an optional argument or field that silently disables an integrity
  check. `check_issue(state=None)` is asserted to *report* rather than stay silent.
* **reachability** — a named issue code that can never fire because the schema already
  rejected the document. Rather than assume, the enforcement layer of every conditional
  property is pinned explicitly in ``EnforcementLayerIsPinned``: the assertion names the code
  that actually fires for a schema-invalid document, so a later reader can see which layer
  holds each property instead of inferring it.

The transition table is enumerated as a **full 9x9 cross-product** against a table written
here independently from contract §8, not sampled — an over- or under-permissive edge hides in
the cells nobody names.

The ``KnownDefects`` class began as four ``@unittest.expectedFailure`` records. Each states the
property the contract, the acceptance ID or the implementation's own docstring claims, and
each currently fails. They are **defect records, not accepted behaviour**: the assertion
inside is the correct one, and fixing the defect turns the method into an unexpected success
that fails this suite — which is the signal to delete the marker, never the assertion.

Offline and deterministic: pure data fixtures with fixed identities, no Git repository, no
clock, no filesystem write. Nothing here writes into the repository under assurance.

    python ResearchSystem/tooling/tests/document_harness_review/run_tests.py
"""
from __future__ import annotations

import json
import re
import unittest
from typing import Any, Iterable

import _harness  # noqa: F401 — installs the tooling and V3-N1 mechanism import paths

from rsclib.document_harness import SCHEMA_DIR, Report, SpecGap, validate  # noqa: E402
from rsclib.document_harness import flow, issues, summary  # noqa: E402
from rsclib.document_harness.review import result_digest, validate_n2  # noqa: E402

# ---------------------------------------------------------------------------
# Identities. Fixed so every digest and every failure message is reproducible.
# ---------------------------------------------------------------------------


def rev(n: int) -> str:
    """A schema-valid 40-hex Git revision that no test resolves against a real object."""
    return format(n, "040x")


def dig(n: int) -> str:
    """A schema-valid 64-hex content digest."""
    return format(n, "064x")


CANDIDATE_C = rev(0xC1)
CANDIDATE_C2 = rev(0xC2)
BASE_B = rev(0xB0)

EXECUTOR = "executor agent"
REVIEWER = "independent reviewer"
CONTROLLER = "assurance controller"
USER = "the user"
OBSERVER = "post-run observer"

WORK_ID = "doc-work"
RUN_ID = "run-one"

#: The run's effective acceptance boundary, used by every repair-boundary test.
EFFECTIVE_BOUNDARY = {"write_scope": ["docs", "notes/public"], "out": ["docs/private"]}


# ---------------------------------------------------------------------------
# Contract §8, restated here independently of the implementation.
#
# These tables are derived from the contract text, NOT read from `flow._SUCCESSORS`
# or `flow._REQUIRED_POINTERS`. Mirroring the implementation's own tables would make the
# cross-product below assert that the code equals itself.
# ---------------------------------------------------------------------------

STATUSES = (
    "RESOLVED",
    "AUDITED",
    "EXECUTING",
    "EVIDENCED",
    "REVIEWED",
    "REPAIRING",
    "AWAITING_FINAL",
    "CLOSED",
    "STOPPED_REPLAN",
)

TERMINAL = ("CLOSED", "STOPPED_REPLAN")

#: "RESOLVED -> AUDITED -> EXECUTING -> EVIDENCED -> REVIEWED (again after VERIFY) ->
#:  REPAIRING (repair_round 0->1) -> AWAITING_FINAL -> CLOSED" (contract §8). The repair loop
#: re-enters EVIDENCED from REPAIRING and REVIEWED from EVIDENCED.
CONTRACT_SUCCESSORS: dict[str, tuple[str, ...]] = {
    "RESOLVED": ("AUDITED",),
    "AUDITED": ("EXECUTING",),
    "EXECUTING": ("EVIDENCED",),
    "EVIDENCED": ("REVIEWED",),
    "REVIEWED": ("REPAIRING", "AWAITING_FINAL"),
    "REPAIRING": ("EVIDENCED",),
    "AWAITING_FINAL": ("CLOSED",),
    "CLOSED": (),
    "STOPPED_REPLAN": (),
}

#: Which stage produces which state pointer, per contract §8's 1:1 status/flow mapping.
#: Requirements accumulate: reaching a status means every earlier stage's product exists.
STAGE_PRODUCTS: dict[str, tuple[str, ...]] = {
    "RESOLVED": ("work_spec_ref", "resolved_plan_ref"),
    "AUDITED": ("instruction_audit_ref", "start_decision_ref"),
    "EXECUTING": (),
    "EVIDENCED": ("fulfillment_ref", "manifest_ref", "coverage_ref"),
    "REVIEWED": ("review_ref",),
    "REPAIRING": ("repair_decision_ref",),
    "AWAITING_FINAL": ("assurance_candidate_ref",),
    "CLOSED": ("final_decision_ref", "summary_ref"),
}

STAGE_ORDER = (
    "RESOLVED",
    "AUDITED",
    "EXECUTING",
    "EVIDENCED",
    "REVIEWED",
    "REPAIRING",
    "AWAITING_FINAL",
    "CLOSED",
)

#: The earliest status at which each late pointer can honestly exist. An AssuranceCandidate is
#: generated at step 9 and the user's FINAL decision answers it, so both belong to
#: AWAITING_FINAL; the single summary is generated after FINAL, so it belongs to CLOSED.
EARLIEST_LATE_POINTER: dict[str, str] = {
    "assurance_candidate_ref": "AWAITING_FINAL",
    "final_decision_ref": "AWAITING_FINAL",
    "summary_ref": "CLOSED",
}

#: Every pointer path a full state can carry.
POINTER_PATHS: dict[str, str] = {
    "work_spec_ref": "control/work-spec.json",
    "resolved_plan_ref": "control/resolved-plan.json",
    "instruction_audit_ref": "control/instruction-audit.json",
    "start_decision_ref": "control/start-decision.json",
    "fulfillment_ref": "control/record.json",
    "manifest_ref": "control/record.json",
    "coverage_ref": "control/coverage.json",
    "review_ref": "control/review-full.json",
    "repair_decision_ref": "control/repair-decision.json",
    "assurance_candidate_ref": "control/assurance-candidate.json",
    "final_decision_ref": "control/final-decision.json",
    "summary_ref": "control/summary.json",
}


def required_for(status: str) -> tuple[str, ...]:
    """Contract §8's cumulative pointer requirement for one status."""
    if status == "STOPPED_REPLAN":
        # A stop can happen anywhere, so nothing beyond the resolution pointers is implied.
        return STAGE_PRODUCTS["RESOLVED"]
    accumulated: list[str] = []
    for stage in STAGE_ORDER[: STAGE_ORDER.index(status) + 1]:
        if stage == "REPAIRING" and status != "REPAIRING":
            continue  # REPAIRING is a detour off the path to AWAITING_FINAL, not a step on it
        accumulated.extend(STAGE_PRODUCTS[stage])
    return tuple(accumulated)


# ---------------------------------------------------------------------------
# Fixture builders. They build the *envelope* only — every defect a test demonstrates is
# written explicitly in that test's own body, so a reader sees the defect rather than
# chasing a shared factory. `FixturesAreSchemaValid` proves each envelope is schema-clean,
# which is what makes "this issue code is reachable with a schema-valid document" a claim
# rather than an assumption.
# ---------------------------------------------------------------------------


def codes(report: Report) -> list[str]:
    return [issue.code for issue in report.issues]


def located(report: Report) -> list[tuple[str, str]]:
    return [(issue.code, issue.where) for issue in report.issues]


def ref(path: str, seed: int) -> dict[str, Any]:
    return {"path": path, "digest_sha256": dig(seed)}


def review_refs_for(*reviews: dict[str, Any]) -> list[dict[str, Any]]:
    """Content-bound review_refs for the supplied rounds, the way run_bind authors them."""
    return [
        {
            "path": "control/review-verify.json"
            if entry.get("review_round") == "VERIFY"
            else "control/review-full.json",
            "digest_sha256": result_digest(entry),
        }
        for entry in reviews
    ]


def make_state(status: str, **overrides: Any) -> dict[str, Any]:
    """A schema-valid AssuranceWorkState carrying exactly what `status` requires."""
    state: dict[str, Any] = {
        "work_id": WORK_ID,
        "run_id": RUN_ID,
        "status": status,
        "repair_round": 1 if status == "REPAIRING" else 0,
    }
    for field in required_for(status):
        state[field] = {"path": POINTER_PATHS[field]}
    if status == "STOPPED_REPLAN":
        state["blockers"] = ["the reviewer's blocking finding was never repaired"]
    state.update(overrides)
    return state


def make_finding(
    finding_id: str, *, blocking: bool = True, obligation_id: str = "ob-changelog"
) -> dict[str, Any]:
    finding: dict[str, Any] = {
        "finding_id": finding_id,
        "obligation_id": obligation_id,
        "blocking": blocking,
        "statement": f"the candidate does not satisfy {obligation_id}",
    }
    if blocking:
        # A blocker names where it is, what it violates and the smallest fix, or it is not one.
        finding["candidate_locator"] = {"path": "docs/changelog.md", "anchor": "## 1.2.0"}
        finding["ground_truth_locator"] = {"path": "docs/instruction.md", "anchor": "## release"}
        finding["minimum_fix"] = "name the release the instruction froze"
    return finding


def make_review(
    *,
    result_id: str = "rr-full",
    review_round: str = "FULL",
    verdict: str = "CHANGES_REQUIRED",
    findings: Iterable[dict[str, Any]] = (),
    candidate_commit: str = CANDIDATE_C,
    accepted_finding_ids: Iterable[str] = (),
) -> dict[str, Any]:
    """A schema-valid ReviewResult owned by the reviewer."""
    finding_list = list(findings)
    disposition: dict[str, Any] = {"obligation_id": "ob-changelog", "disposition": "SUPPORTED"}
    if finding_list:
        disposition = {
            "obligation_id": "ob-changelog",
            "disposition": "NOT_SUPPORTED",
            "note": "the frozen subjects contradict the fulfillment claim",
            "finding_ids": [entry["finding_id"] for entry in finding_list],
        }
    result: dict[str, Any] = {
        "result_id": result_id,
        "work_id": WORK_ID,
        "run_id": RUN_ID,
        "review_round": review_round,
        "package_ref": ref("control/review-package.json", 0x9A),
        "candidate_ref": {"branch": "candidate", "commit": candidate_commit},
        "verdict": verdict,
        "instruction_completeness": {
            "result": "COMPLETE",
            "instruction_ref": {"path": "docs/instruction.md", "revision": BASE_B},
        },
        "per_obligation_disposition": [disposition],
        "residual_uncertainty": [],
        "reviewed_by": REVIEWER,
    }
    if finding_list:
        result["findings"] = finding_list
    if review_round == "VERIFY":
        result["verify_scope"] = {
            "accepted_finding_ids": list(accepted_finding_ids) or ["f-changelog"],
            "repair_diff_reviewed": True,
            "permanent_boundaries_checked": True,
        }
    return result


def make_record(
    *, candidate_commit: str = CANDIDATE_C, repair_round: int = 0, run_id: str = RUN_ID
) -> dict[str, Any]:
    """The three CandidateRecord fields `check_assurance_candidate` reads.

    Deliberately not a whole record: the function reads `run_id`, `candidate_ref` and
    `repair_round` and nothing else, and a full record here would hide which three fields the
    binding is actually checked against.
    """
    return {
        "run_id": run_id,
        "candidate_ref": {"branch": "candidate", "commit": candidate_commit},
        "repair_round": repair_round,
    }


def make_candidate(**overrides: Any) -> dict[str, Any]:
    """A schema-valid AssuranceCandidate: the pre-decision binding."""
    candidate = summary.bind_candidate(
        assurance_candidate_id="ac-one",
        work_id=WORK_ID,
        run_id=RUN_ID,
        repair_round=0,
        candidate_ref={"branch": "candidate", "commit": CANDIDATE_C},
        base_revision=BASE_B,
        bound_by=CONTROLLER,
        work_spec_ref=ref("control/work-spec.json", 0x11),
        resolved_plan_ref=ref("control/resolved-plan.json", 0x12),
        instruction_audit_ref=ref("control/instruction-audit.json", 0x13),
        fulfillment_ref=ref("control/record.json", 0x14),
        manifest_ref=ref("control/record.json", 0x15),
        coverage_ref=ref("control/coverage.json", 0x16),
        review_refs=review_refs_for(make_review()),
        governance_scan=flow.governance_state(result_ref=ref("control/check-r4.json", 0x18)),
    )
    for key, value in overrides.items():
        if value is None:
            candidate.pop(key, None)
        else:
            candidate[key] = value
    return candidate


def make_decision(
    *,
    phase: str,
    decision: str,
    target: dict[str, Any],
    decision_id: str = "ud-one",
    work_id: str = WORK_ID,
    limitations: Iterable[str] = (),
) -> dict[str, Any]:
    """A schema-valid UserDecision."""
    document: dict[str, Any] = {
        "decision_id": decision_id,
        "work_id": work_id,
        "run_id": RUN_ID,
        "phase": phase,
        "decision": decision,
        "target": target,
        "decided_by": USER,
        "decided_at": "2026-07-20",
    }
    if limitations:
        document["limitations"] = list(limitations)
    return document


def make_repair_decision(
    *,
    candidate_commit: str = CANDIDATE_C,
    accepted_finding_ids: Iterable[str] = ("f-changelog",),
    write_scope: Iterable[str] = ("docs",),
    out: Iterable[str] = ("docs/private",),
    decision: str = "APPLY_ACCEPTED_FINDINGS",
) -> dict[str, Any]:
    target: dict[str, Any] = {"candidate_ref": {"branch": "candidate", "commit": candidate_commit}}
    if decision == "APPLY_ACCEPTED_FINDINGS":
        target["accepted_finding_ids"] = list(accepted_finding_ids)
        target["repair_boundary"] = {"write_scope": list(write_scope), "out": list(out)}
    return make_decision(
        phase="REPAIR", decision=decision, target=target, decision_id="ud-repair"
    )


def verify_outcome(verify: dict[str, Any], decision: dict[str, Any] | None = None):
    """`flow.check_verify_outcome` with a decision approving exactly what the VERIFY declares.

    The function grew a required `repair_decision` parameter during the V3-N2 fix round, so
    that the findings a VERIFY claims to have covered are reconciled against the findings the
    user actually approved. The tests in this file predate it and are about other properties —
    the stop, the SPEC_GAP, the round guard — so the default here supplies a *matching*
    decision and leaves them testing what they were written to test. The mismatch itself is
    pinned in `test_fix_round_locks.py`, deliberately not here: a helper that silently
    manufactures agreement must never be the thing that checks for agreement.
    """
    if decision is None:
        scope = verify.get("verify_scope") or {}
        decision = make_repair_decision(
            accepted_finding_ids=scope.get("accepted_finding_ids", ["f-changelog"])
        )
    return flow.check_verify_outcome(verify, decision)


def make_final_decision(
    *, decision: str = "ACCEPT", candidate: dict[str, Any] | None = None, limitations: Iterable[str] = ()
) -> dict[str, Any]:
    bound = candidate if candidate is not None else make_candidate()
    return make_decision(
        phase="FINAL",
        decision=decision,
        target={
            "assurance_candidate_ref": {
                "path": "control/assurance-candidate.json",
                "digest_sha256": summary.candidate_digest(bound),
            }
        },
        decision_id="ud-final",
        limitations=limitations,
    )


def make_summary(
    *,
    candidate: dict[str, Any] | None = None,
    decision: dict[str, Any] | None = None,
    promotion: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """A schema-valid AssuranceSummary generated from a real FINAL decision."""
    bound = candidate if candidate is not None else make_candidate()
    final = decision if decision is not None else make_final_decision(candidate=bound)
    return summary.generate_summary(
        summary_id="sum-one",
        candidate=bound,
        candidate_ref={
            "path": "control/assurance-candidate.json",
            "digest_sha256": summary.candidate_digest(bound),
        },
        decision=final,
        decision_ref={
            "path": "control/final-decision.json",
            "digest_sha256": flow.decision_digest(final),
        },
        promotion=promotion if promotion is not None else summary.no_promotion(
            "the user accepted the work but asked for no local promotion"
        ),
        generated_by=CONTROLLER,
        generated_at="2026-07-20",
    )


def make_issue(**overrides: Any) -> dict[str, Any]:
    """A schema-valid HarnessIssue: one immutable post-run observation."""
    issue = issues.record_issue(
        issue_id="hi-one",
        work_id=WORK_ID,
        run_id=RUN_ID,
        kind="HARNESS_DEFECT",
        statement="the coverage view dropped an obligation with no locator",
        evidence_refs=[ref("control/coverage.json", 0x31)],
        observed_after="CLOSED",
        observed_by=OBSERVER,
        observed_at="2026-07-20",
    )
    for key, value in overrides.items():
        if value is None:
            issue.pop(key, None)
        else:
            issue[key] = value
    return issue


def make_triage(
    *, decision: str = "WORKFLOW_FIX", work_id: str = WORK_ID, issue_path: str = "control/hi-one.json"
) -> dict[str, Any]:
    return make_decision(
        phase="ISSUE_TRIAGE",
        decision=decision,
        target={"harness_issue_ref": {"path": issue_path}},
        decision_id="ud-triage",
        work_id=work_id,
    )


def evidence_set(seed: int, *, checks: tuple[str, ...] = ()) -> flow.EvidenceSet:
    return flow.EvidenceSet(
        fulfillment=dig(seed),
        manifest=dig(seed + 1),
        coverage=dig(seed + 2),
        package=dig(seed + 3),
        checks=checks,
    )


# ---------------------------------------------------------------------------
# Fixture validity — the precondition every reachability claim below rests on
# ---------------------------------------------------------------------------


class FixturesAreSchemaValid(unittest.TestCase):
    """Each envelope is schema-clean, so every issue a test triggers is reachable *in a run*.

    A named issue code that only fires for a document the schema would have rejected is not a
    guard, it is dead text — V3-N1 shipped exactly that defect. These assertions are what
    stop this matrix from claiming reachability it never demonstrated.
    """

    def test_state_fixtures_validate(self) -> None:
        for status in STATUSES:
            with self.subTest(status=status):
                self.assertEqual(codes(validate("state", make_state(status))), [])

    def test_review_fixtures_validate(self) -> None:
        full = make_review(findings=[make_finding("f-changelog")])
        verify = make_review(
            result_id="rr-verify",
            review_round="VERIFY",
            verdict="REVIEWED_NO_BLOCKER",
            candidate_commit=CANDIDATE_C2,
        )
        self.assertEqual(codes(validate_n2("review_result", full)), [])
        self.assertEqual(codes(validate_n2("review_result", verify)), [])

    def test_candidate_summary_and_decision_fixtures_validate(self) -> None:
        candidate = make_candidate()
        final = make_final_decision(candidate=candidate)
        self.assertEqual(codes(validate_n2("assurance_candidate", candidate)), [])
        self.assertEqual(codes(validate("decision", final)), [])
        self.assertEqual(codes(validate("decision", make_repair_decision())), [])
        self.assertEqual(
            codes(validate_n2("assurance_summary", make_summary(candidate=candidate, decision=final))),
            [],
        )

    def test_issue_and_triage_fixtures_validate(self) -> None:
        self.assertEqual(codes(validate_n2("harness_issue", make_issue())), [])
        self.assertEqual(codes(validate("decision", make_triage())), [])


# ---------------------------------------------------------------------------
# N2-A6 / N2-A11 — the transition table, enumerated
# ---------------------------------------------------------------------------


class TransitionTableCrossProduct(unittest.TestCase):
    """All 81 status x status cells against contract §8, not a sample.

    An over- or under-permissive edge hides in the cells nobody names, so every cell is
    asserted: the legal ones report no issue at all, and the illegal ones report the exact
    code that names *why* they are illegal.
    """

    def test_every_cell_matches_contract_section_8(self) -> None:
        for current in STATUSES:
            for target in STATUSES:
                with self.subTest(current=current, target=target):
                    report = flow.check_transition(
                        {"status": current, "repair_round": 0}, target
                    )
                    if current in TERMINAL:
                        self.assertEqual(
                            codes(report),
                            ["V3-FLOW-TERMINAL"],
                            f"{current} has ended; nothing continues from it",
                        )
                    elif target == "STOPPED_REPLAN" or target in CONTRACT_SUCCESSORS[current]:
                        self.assertEqual(
                            codes(report), [], f"{current} -> {target} is legal under §8"
                        )
                    else:
                        self.assertEqual(
                            codes(report),
                            ["V3-FLOW-ILLEGAL-TRANSITION"],
                            f"{current} -> {target} is not legal under §8",
                        )

    def test_a_stop_is_reachable_from_every_pre_terminal_status(self) -> None:
        for current in STATUSES:
            if current in TERMINAL:
                continue
            with self.subTest(current=current):
                report = flow.check_transition({"status": current, "repair_round": 0}, "STOPPED_REPLAN")
                self.assertEqual(codes(report), [])

    def test_no_status_may_transition_to_itself(self) -> None:
        for current in STATUSES:
            with self.subTest(current=current):
                expected = "V3-FLOW-TERMINAL" if current in TERMINAL else "V3-FLOW-ILLEGAL-TRANSITION"
                self.assertEqual(
                    codes(flow.check_transition({"status": current, "repair_round": 0}, current)),
                    [expected],
                )

    def test_an_unknown_status_is_named_on_either_side(self) -> None:
        self.assertEqual(
            codes(flow.check_transition({"status": "REVIEWING", "repair_round": 0}, "REVIEWED")),
            ["V3-FLOW-UNKNOWN-STATUS"],
        )
        self.assertEqual(
            codes(flow.check_transition({"status": "REVIEWED", "repair_round": 0}, "RE_REVIEWED")),
            ["V3-FLOW-UNKNOWN-STATUS"],
        )

    def test_required_pointers_refuses_an_unknown_status(self) -> None:
        with self.assertRaises(SpecGap) as raised:
            flow.required_pointers("MAINTENANCE")
        self.assertIn("V3-FLOW-UNKNOWN-STATUS", str(raised.exception))


class OneRepairOnly(unittest.TestCase):
    """V3-D6 / N2-A6: one user-approved repair exists, and there is no second."""

    def test_a_second_repairing_is_refused_from_every_status(self) -> None:
        for current in STATUSES:
            with self.subTest(current=current):
                report = flow.check_transition({"status": current, "repair_round": 1}, "REPAIRING")
                if current in TERMINAL:
                    # A terminal run is refused before the round is even consulted.
                    self.assertIn("V3-FLOW-TERMINAL", codes(report))
                else:
                    self.assertIn("V3-FLOW-SECOND-REPAIR", codes(report))

    def test_the_second_repair_guard_is_the_only_complaint_on_the_legal_edge(self) -> None:
        # REVIEWED -> REPAIRING is legal; only the exhausted round makes it refusable.
        self.assertEqual(
            codes(flow.check_transition({"status": "REVIEWED", "repair_round": 1}, "REPAIRING")),
            ["V3-FLOW-SECOND-REPAIR"],
        )

    def test_negative_control_the_first_repair_is_allowed(self) -> None:
        self.assertEqual(
            codes(flow.check_transition({"status": "REVIEWED", "repair_round": 0}, "REPAIRING")),
            [],
        )

    def test_after_a_verify_the_run_may_only_close_or_stop(self) -> None:
        # The run is back at REVIEWED with its single repair spent.
        reviewed_after_verify = {"status": "REVIEWED", "repair_round": 1}
        self.assertEqual(codes(flow.check_transition(reviewed_after_verify, "AWAITING_FINAL")), [])
        self.assertEqual(codes(flow.check_transition(reviewed_after_verify, "STOPPED_REPLAN")), [])
        self.assertEqual(
            codes(flow.check_transition(reviewed_after_verify, "REPAIRING")),
            ["V3-FLOW-SECOND-REPAIR"],
        )
        self.assertEqual(
            codes(flow.check_transition(reviewed_after_verify, "REVIEWED")),
            ["V3-FLOW-ILLEGAL-TRANSITION"],
        )

    def test_advance_checked_raises_rather_than_returning_an_illegal_state(self) -> None:
        state = make_state("REVIEWED", repair_round=1)
        state["repair_decision_ref"] = {"path": POINTER_PATHS["repair_decision_ref"]}
        with self.assertRaises(SpecGap) as raised:
            flow.advance_checked(state, "REPAIRING")
        self.assertIn("V3-FLOW-SECOND-REPAIR", str(raised.exception))


# ---------------------------------------------------------------------------
# N2-A7 / N0-R2 — the pointer conditionals, both directions
# ---------------------------------------------------------------------------


class StatusPointerConditionals(unittest.TestCase):
    """A status makes a claim; the pointers are what back it (inherited residual N0-R2).

    Both directions are enumerated over every status: a required pointer that is missing, and
    a pointer present at a status that cannot yet have produced it.
    """

    def test_negative_control_a_complete_state_reports_nothing(self) -> None:
        for status in STATUSES:
            with self.subTest(status=status):
                self.assertEqual(codes(flow.check_state_pointers(make_state(status))), [])

    #: The two pointers the AssuranceWorkState schema itself makes unconditionally required.
    #: A state without them is refused before `check_state_pointers` can speak, so the layer
    #: that holds them is named here rather than left for a reader to infer.
    SCHEMA_REQUIRED_POINTERS = frozenset({"work_spec_ref", "resolved_plan_ref"})

    def test_every_required_pointer_is_named_when_it_is_missing(self) -> None:
        for status in STATUSES:
            for field in required_for(status):
                with self.subTest(status=status, missing=field):
                    state = make_state(status)
                    del state[field]
                    reported = located(flow.check_state_pointers(state))
                    if field in self.SCHEMA_REQUIRED_POINTERS:
                        self.assertIn(
                            "V3-SCHEMA-STATE",
                            [code for code, _ in reported],
                            f"{status} without {field} must be refused by the schema",
                        )
                    else:
                        self.assertIn(
                            ("V3-FLOW-POINTER-REQUIRED", field),
                            reported,
                            f"{status} without {field} claims a stage that left no record",
                        )

    def test_a_late_pointer_at_an_early_status_is_named_premature(self) -> None:
        for field, earliest in EARLIEST_LATE_POINTER.items():
            for status in STAGE_ORDER[: STAGE_ORDER.index(earliest)]:
                with self.subTest(field=field, status=status):
                    state = make_state(status)
                    state[field] = {"path": POINTER_PATHS[field]}
                    self.assertIn(
                        ("V3-FLOW-POINTER-PREMATURE", field),
                        located(flow.check_state_pointers(state)),
                        f"{field} cannot be produced before {earliest}",
                    )

    def test_negative_control_a_late_pointer_at_or_after_its_own_stage_is_not_premature(self) -> None:
        for field, earliest in EARLIEST_LATE_POINTER.items():
            for status in STAGE_ORDER[STAGE_ORDER.index(earliest) :]:
                with self.subTest(field=field, status=status):
                    state = make_state(status)
                    state[field] = {"path": POINTER_PATHS[field]}
                    self.assertNotIn(
                        "V3-FLOW-POINTER-PREMATURE", codes(flow.check_state_pointers(state))
                    )

    def test_a_stop_must_record_why_it_stopped(self) -> None:
        state = make_state("STOPPED_REPLAN")
        del state["blockers"]
        self.assertEqual(
            located(flow.check_state_pointers(state)),
            [("V3-FLOW-STOP-WITHOUT-REASON", "blockers")],
        )

    def test_a_repair_round_without_its_authorization_is_named(self) -> None:
        # Round 1 with the evidence regenerated but no recorded REPAIR decision: the pointer
        # is not required by EVIDENCED itself, so only the authorization guard can see it.
        state = make_state("EVIDENCED", repair_round=1)
        self.assertEqual(
            located(flow.check_state_pointers(state)),
            [("V3-FLOW-REPAIR-WITHOUT-AUTHORIZATION", "repair_decision_ref")],
        )

    def test_negative_control_round_zero_needs_no_repair_authorization(self) -> None:
        self.assertEqual(codes(flow.check_state_pointers(make_state("EVIDENCED"))), [])

    def test_a_schema_invalid_state_reports_the_schema_layer(self) -> None:
        state = make_state("REVIEWED")
        state["status"] = "MAINTENANCE"
        self.assertEqual(codes(flow.check_state_pointers(state)), ["V3-SCHEMA-STATE"])

    def test_the_whole_repair_path_advances_without_a_single_complaint(self) -> None:
        """The end-to-end negative control: none of the guards above is simply always-on."""
        state = make_state("RESOLVED")
        state = flow.advance_checked(
            state,
            "AUDITED",
            instruction_audit_ref={"path": POINTER_PATHS["instruction_audit_ref"]},
            start_decision_ref={"path": POINTER_PATHS["start_decision_ref"]},
        )
        state = flow.advance_checked(state, "EXECUTING")
        state = flow.advance_checked(
            state,
            "EVIDENCED",
            fulfillment_ref={"path": POINTER_PATHS["fulfillment_ref"]},
            manifest_ref={"path": POINTER_PATHS["manifest_ref"]},
            coverage_ref={"path": POINTER_PATHS["coverage_ref"]},
        )
        state = flow.advance_checked(state, "REVIEWED", review_ref={"path": POINTER_PATHS["review_ref"]})
        state = flow.advance_checked(
            state, "REPAIRING", repair_decision_ref={"path": POINTER_PATHS["repair_decision_ref"]}
        )
        self.assertEqual(state["repair_round"], 1)
        state = flow.advance_checked(state, "EVIDENCED")
        state = flow.advance_checked(state, "REVIEWED")
        state = flow.advance_checked(
            state,
            "AWAITING_FINAL",
            assurance_candidate_ref={"path": POINTER_PATHS["assurance_candidate_ref"]},
        )
        state = flow.advance_checked(
            state,
            "CLOSED",
            final_decision_ref={"path": POINTER_PATHS["final_decision_ref"]},
            summary_ref={"path": POINTER_PATHS["summary_ref"]},
        )
        self.assertEqual(state["status"], "CLOSED")
        self.assertEqual(codes(flow.check_state_pointers(state)), [])

    def test_advance_checked_refuses_a_status_whose_product_is_missing(self) -> None:
        state = make_state("REVIEWED")
        with self.assertRaises(SpecGap) as raised:
            flow.advance_checked(state, "AWAITING_FINAL")
        self.assertIn("V3-FLOW-POINTER-REQUIRED", str(raised.exception))
        self.assertIn("assurance_candidate_ref", str(raised.exception))


# ---------------------------------------------------------------------------
# N2-A4 — the repair authorization
# ---------------------------------------------------------------------------


def as_v2_review(review: dict[str, Any]) -> dict[str, Any]:
    """The same ReviewResult in the v2 successor shape (review.v2.schema.json).

    The delta that matters to the binding guard: `candidate_ref` moves off the root and
    into `subject`, and the root declares `schema_version: "2"`. Built by transforming a
    v1 fixture so the two shapes cannot drift apart in this file.
    """
    v2 = {key: value for key, value in review.items() if key not in ("candidate_ref", "package_ref")}
    v2["schema_version"] = "2"
    v2["subject"] = {
        "evidence_commit": rev(0xE1),
        "candidate_ref": review["candidate_ref"],
        "base_revision": rev(0xB1),
        "control_root": "runs/r1",
        "repair_round": 0,
    }
    return v2


class RepairDecisionBindingAcrossResultVersions(unittest.TestCase):
    """The binding guard reads the candidate from whichever shape the result declares.

    Regression for the defect class, not just its instance: when the v2 successor moved
    `candidate_ref` into `subject`, the guard kept reading the root and reported every v2
    review as unbound — fail-closed, but on a shape mismatch rather than a real one, so the
    property went untested for exactly the runs the successor governs. Witnessed at p3-corr.
    Each "must fire" case is paired with a negative control so neither version can pass by
    the guard being always-on or always-off.
    """

    def setUp(self) -> None:
        self.plan = {"effective_change_boundary": EFFECTIVE_BOUNDARY}
        self.v1 = make_review(findings=[make_finding("f-changelog")])
        self.v2 = as_v2_review(self.v1)

    def test_negative_control_a_v2_review_bound_to_its_candidate_reports_nothing(self) -> None:
        self.assertEqual(
            codes(flow.check_repair_decision(make_repair_decision(), self.v2, self.plan)), []
        )

    def test_a_v2_review_still_names_a_repair_bound_to_the_wrong_candidate(self) -> None:
        decision = make_repair_decision(candidate_commit=CANDIDATE_C2)
        self.assertEqual(
            located(flow.check_repair_decision(decision, self.v2, self.plan)),
            [("V3-FLOW-REPAIR-WRONG-CANDIDATE", "target/candidate_ref")],
        )

    def test_a_v2_review_carrying_no_subject_candidate_is_reported_unverified(self) -> None:
        stripped = {**self.v2, "subject": {k: v for k, v in self.v2["subject"].items()
                                           if k != "candidate_ref"}}
        self.assertEqual(
            located(flow.check_repair_decision(make_repair_decision(), stripped, self.plan)),
            [("V3-FLOW-REPAIR-BINDING-UNVERIFIED", "target/candidate_ref")],
        )

    def test_a_v2_no_repair_bound_to_the_wrong_candidate_is_still_named(self) -> None:
        """Defect M5 under the v2 result shape: a decline binds what it declined."""
        decision = make_repair_decision(decision="NO_REPAIR", candidate_commit=CANDIDATE_C2)
        self.assertEqual(
            located(flow.check_repair_decision(decision, self.v2, self.plan)),
            [("V3-FLOW-REPAIR-WRONG-CANDIDATE", "target/candidate_ref")],
        )

    def test_the_v1_root_shape_is_unaffected(self) -> None:
        self.assertEqual(
            codes(flow.check_repair_decision(make_repair_decision(), self.v1, self.plan)), []
        )
        self.assertEqual(
            located(flow.check_repair_decision(
                make_repair_decision(candidate_commit=CANDIDATE_C2), self.v1, self.plan)),
            [("V3-FLOW-REPAIR-WRONG-CANDIDATE", "target/candidate_ref")],
        )

    def test_an_unknown_result_version_stops_instead_of_matching_a_shape(self) -> None:
        """No cross-version fallback: an unrecognised version is not silently read as v1."""
        future = {**self.v2, "schema_version": "3"}
        with self.assertRaises(SpecGap):
            flow.check_repair_decision(make_repair_decision(), future, self.plan)

    def test_a_present_but_null_version_is_a_declaration_not_an_absence(self) -> None:
        nulled = {**self.v2, "schema_version": None}
        with self.assertRaises(SpecGap):
            flow.check_repair_decision(make_repair_decision(), nulled, self.plan)


class RepairDecisionBinding(unittest.TestCase):
    """REPAIR binds the reviewed candidate, the accepted findings and a narrowing boundary."""

    def setUp(self) -> None:
        self.review = make_review(findings=[make_finding("f-changelog")])
        self.plan = {"effective_change_boundary": EFFECTIVE_BOUNDARY}

    def test_negative_control_a_well_bound_repair_reports_nothing(self) -> None:
        self.assertEqual(
            codes(flow.check_repair_decision(make_repair_decision(), self.review, self.plan)), []
        )

    def test_a_repair_bound_to_a_different_candidate_is_named(self) -> None:
        decision = make_repair_decision(candidate_commit=CANDIDATE_C2)
        self.assertEqual(
            located(flow.check_repair_decision(decision, self.review, self.plan)),
            [("V3-FLOW-REPAIR-WRONG-CANDIDATE", "target/candidate_ref")],
        )

    def test_an_accepted_finding_the_review_never_raised_is_named(self) -> None:
        decision = make_repair_decision(accepted_finding_ids=["f-changelog", "f-invented"])
        report = flow.check_repair_decision(decision, self.review, self.plan)
        self.assertEqual(
            located(report),
            [("V3-FLOW-ACCEPTED-FINDING-UNKNOWN", "target/accepted_finding_ids")],
        )
        self.assertIn("f-invented", report.issues[0].message)

    def test_a_repair_boundary_reaching_outside_the_effective_scope_is_named(self) -> None:
        decision = make_repair_decision(write_scope=["ResearchSystem/tooling"])
        report = flow.check_repair_decision(decision, self.review, self.plan)
        self.assertEqual(
            located(report),
            [("V3-FLOW-REPAIR-BOUNDARY-WIDENS", "target/repair_boundary/write_scope")],
        )

    def test_a_repair_boundary_reaching_into_the_negative_boundary_is_named(self) -> None:
        decision = make_repair_decision(write_scope=["docs/private"])
        self.assertEqual(
            located(flow.check_repair_decision(decision, self.review, self.plan)),
            [("V3-FLOW-REPAIR-BOUNDARY-WIDENS", "target/repair_boundary/write_scope")],
        )

    def test_widening_is_detected_per_path_across_the_boundary_cross_product(self) -> None:
        """Every relation a repair path can have to the effective boundary, enumerated."""
        cases = {
            "docs": True,                      # exactly the write scope
            "docs/changelog.md": True,         # inside it
            "notes/public/one.md": True,       # inside the second scope entry
            "docs/private": False,             # the negative boundary wins
            "docs/private/secret.md": False,   # inside the negative boundary
            "notes": False,                    # a parent of a scope entry is not inside it
            "docsx": False,                    # segment-boundary containment, not prefix
            "elsewhere/file.md": False,        # plainly outside
        }
        for path, conforms in cases.items():
            with self.subTest(path=path):
                decision = make_repair_decision(write_scope=[path])
                report = flow.check_repair_decision(decision, self.review, self.plan)
                if conforms:
                    self.assertEqual(codes(report), [])
                else:
                    self.assertEqual(codes(report), ["V3-FLOW-REPAIR-BOUNDARY-WIDENS"])

    def test_a_narrowed_boundary_is_the_point_of_the_rule(self) -> None:
        decision = make_repair_decision(write_scope=["docs/changelog.md"])
        self.assertEqual(codes(flow.check_repair_decision(decision, self.review, self.plan)), [])

    def test_negative_control_a_well_bound_no_repair_reports_nothing(self) -> None:
        # The accepted-findings and boundary sections bind nothing for a decline, but the
        # decline itself still binds this run's reviewed candidate.
        decision = make_repair_decision(decision="NO_REPAIR", candidate_commit=CANDIDATE_C)
        self.assertEqual(codes(flow.check_repair_decision(decision, self.review, self.plan)), [])

    def test_a_no_repair_bound_to_a_different_candidate_is_named(self) -> None:
        """Defect M5: the early return skipped every binding check for a decline."""
        decision = make_repair_decision(decision="NO_REPAIR", candidate_commit=CANDIDATE_C2)
        self.assertEqual(
            located(flow.check_repair_decision(decision, self.review, self.plan)),
            [("V3-FLOW-REPAIR-WRONG-CANDIDATE", "target/candidate_ref")],
        )

    def test_a_no_repair_answering_another_runs_review_is_named(self) -> None:
        decision = make_repair_decision(decision="NO_REPAIR")
        decision["run_id"] = "run-two"
        self.assertEqual(
            located(flow.check_repair_decision(decision, self.review, self.plan)),
            [("V3-FLOW-REPAIR-RUN-MISMATCH", "run_id")],
        )

    def test_an_apply_answering_another_works_review_is_named(self) -> None:
        """The defect class covers both decision values, not the NO_REPAIR instance alone."""
        decision = make_repair_decision()
        decision["work_id"] = "other-work"
        self.assertEqual(
            located(flow.check_repair_decision(decision, self.review, self.plan)),
            [("V3-FLOW-REPAIR-WORK-MISMATCH", "work_id")],
        )

    def test_a_decision_naming_no_run_is_reported_unverified(self) -> None:
        # run_id is schema-optional on a decision; absence is an unverified binding, never
        # a silently skipped one.
        decision = make_repair_decision()
        del decision["run_id"]
        self.assertEqual(
            located(flow.check_repair_decision(decision, self.review, self.plan)),
            [("V3-FLOW-REPAIR-BINDING-UNVERIFIED", "run_id")],
        )

    def test_a_decision_from_another_phase_is_refused(self) -> None:
        final = make_final_decision()
        self.assertEqual(
            located(flow.check_repair_decision(final, self.review, self.plan)),
            [("V3-FLOW-PHASE", "phase")],
        )

    def test_a_schema_invalid_decision_never_reaches_the_binding_checks(self) -> None:
        decision = make_repair_decision()
        del decision["target"]["repair_boundary"]
        self.assertEqual(
            codes(flow.check_repair_decision(decision, self.review, self.plan)),
            ["V3-SCHEMA-DECISION"],
        )


# ---------------------------------------------------------------------------
# N2-A5 — C2 regenerates everything
# ---------------------------------------------------------------------------


class RepairRegeneratesEveryEvidenceDocument(unittest.TestCase):
    """Invariant 11: a round-0 document carried into round 1 describes the replaced candidate."""

    def test_negative_control_a_fully_regenerated_set_reports_nothing(self) -> None:
        before = evidence_set(0x100, checks=(dig(0x200), dig(0x201)))
        after = evidence_set(0x300, checks=(dig(0x400), dig(0x401)))
        self.assertEqual(codes(flow.check_repair_regeneration(before, after)), [])

    def test_each_inherited_document_is_named_individually(self) -> None:
        before = evidence_set(0x100)
        for field in ("fulfillment", "manifest", "coverage", "package"):
            with self.subTest(inherited=field):
                after = evidence_set(0x300)
                # Carry exactly one round-0 document into round 1.
                mutated = flow.EvidenceSet(**{**after.as_map(), field: getattr(before, field)})
                self.assertEqual(
                    located(flow.check_repair_regeneration(before, mutated)),
                    [("V3-FLOW-EVIDENCE-NOT-REGENERATED", field)],
                )

    def test_inheriting_the_whole_set_names_all_four(self) -> None:
        before = evidence_set(0x100)
        report = flow.check_repair_regeneration(before, evidence_set(0x100))
        self.assertEqual(
            located(report),
            [
                ("V3-FLOW-EVIDENCE-NOT-REGENERATED", "fulfillment"),
                ("V3-FLOW-EVIDENCE-NOT-REGENERATED", "manifest"),
                ("V3-FLOW-EVIDENCE-NOT-REGENERATED", "coverage"),
                ("V3-FLOW-EVIDENCE-NOT-REGENERATED", "package"),
            ],
        )

    def test_checks_that_are_byte_identical_were_not_re_run(self) -> None:
        checks = (dig(0x200), dig(0x201))
        before = evidence_set(0x100, checks=checks)
        after = evidence_set(0x300, checks=checks)
        self.assertEqual(
            located(flow.check_repair_regeneration(before, after)),
            [("V3-FLOW-CHECKS-NOT-RERUN", "checks")],
        )

    def test_an_added_or_removed_check_result_changes_the_set(self) -> None:
        before = evidence_set(0x100, checks=(dig(0x200),))
        added = evidence_set(0x300, checks=(dig(0x200), dig(0x201)))
        self.assertEqual(codes(flow.check_repair_regeneration(before, added)), [])

    def test_the_evidence_set_map_round_trips(self) -> None:
        original = evidence_set(0x100, checks=(dig(0x200),))
        self.assertEqual(flow.EvidenceSet(**original.as_map()), original)


# ---------------------------------------------------------------------------
# N2-A6 — VERIFY and the stop
# ---------------------------------------------------------------------------


class VerifyOutcomeStopsRatherThanLooping(unittest.TestCase):
    """A problem still standing after VERIFY stops the run: no second fix, no second review."""

    def test_negative_control_a_clean_verify_reports_nothing(self) -> None:
        verify = make_review(
            result_id="rr-verify",
            review_round="VERIFY",
            verdict="REVIEWED_NO_BLOCKER",
            candidate_commit=CANDIDATE_C2,
        )
        self.assertEqual(codes(verify_outcome(verify)), [])

    def test_a_blocker_still_standing_after_verify_stops_the_run(self) -> None:
        verify = make_review(
            result_id="rr-verify",
            review_round="VERIFY",
            verdict="REVIEWED_NO_BLOCKER",
            candidate_commit=CANDIDATE_C2,
            findings=[make_finding("f-changelog"), make_finding("f-links", obligation_id="ob-links")],
        )
        report = verify_outcome(verify)
        self.assertEqual(located(report), [("V3-FLOW-BLOCKER-AFTER-VERIFY", "findings")])
        self.assertIn("f-changelog", report.issues[0].message)
        self.assertIn("f-links", report.issues[0].message)

    def test_a_non_blocking_finding_after_verify_does_not_stop_the_run(self) -> None:
        verify = make_review(
            result_id="rr-verify",
            review_round="VERIFY",
            verdict="REVIEWED_NO_BLOCKER",
            candidate_commit=CANDIDATE_C2,
            findings=[make_finding("f-style", blocking=False)],
        )
        self.assertEqual(codes(verify_outcome(verify)), [])

    def test_a_spec_gap_at_verify_stops_and_is_never_patched(self) -> None:
        verify = make_review(
            result_id="rr-verify",
            review_round="VERIFY",
            verdict="SPEC_GAP",
            candidate_commit=CANDIDATE_C2,
        )
        self.assertEqual(located(verify_outcome(verify)), [("V3-FLOW-VERIFY-SPEC-GAP", "verdict")])

    def test_a_full_result_is_not_a_verify_outcome(self) -> None:
        full = make_review(findings=[make_finding("f-changelog")])
        self.assertEqual(located(verify_outcome(full)), [("V3-FLOW-NOT-VERIFY", "review_round")])

    def test_a_verify_cannot_request_changes_and_has_no_third_round(self) -> None:
        # A VERIFY that returned CHANGES_REQUIRED would be asking for a repair that cannot exist.
        verify = make_review(
            result_id="rr-verify",
            review_round="VERIFY",
            verdict="CHANGES_REQUIRED",
            candidate_commit=CANDIDATE_C2,
            findings=[make_finding("f-changelog")],
        )
        self.assertEqual(set(codes(validate_n2("review_result", verify))), {"V3-SCHEMA-REVIEW_RESULT"})

        third = make_review(result_id="rr-third", review_round="RE_VERIFY")
        self.assertEqual(set(codes(validate_n2("review_result", third))), {"V3-SCHEMA-REVIEW_RESULT"})

    def test_the_stop_after_verify_is_a_legal_transition_and_a_second_repair_is_not(self) -> None:
        after_verify = {"status": "REVIEWED", "repair_round": 1}
        self.assertEqual(codes(flow.check_transition(after_verify, "STOPPED_REPLAN")), [])
        self.assertEqual(
            codes(flow.check_transition(after_verify, "REPAIRING")), ["V3-FLOW-SECOND-REPAIR"]
        )


# ---------------------------------------------------------------------------
# N2-A7 / N2-A9 — the AssuranceCandidate binds, and never strengthens
# ---------------------------------------------------------------------------


class AssuranceCandidateIsFaithful(unittest.TestCase):
    """The controller is checked against the reviewer's document, not trusted to summarise it."""

    def test_negative_control_a_faithful_candidate_reports_nothing(self) -> None:
        review = make_review()
        self.assertEqual(
            codes(summary.check_assurance_candidate(make_candidate(), make_record(), [review])), []
        )

    def test_a_dropped_blocking_finding_is_named(self) -> None:
        review = make_review(findings=[make_finding("f-changelog")])
        # carries no unresolved_finding_ids at all
        candidate = make_candidate(review_refs=review_refs_for(review))
        report = summary.check_assurance_candidate(candidate, make_record(), [review])
        self.assertEqual(
            located(report), [("V3-ASSURANCE-BLOCKER-DROPPED", "unresolved_finding_ids")]
        )
        self.assertIn("f-changelog", report.issues[0].message)

    def test_an_invented_unresolved_finding_is_named(self) -> None:
        review = make_review()
        candidate = make_candidate(unresolved_finding_ids=["f-imagined"])
        report = summary.check_assurance_candidate(candidate, make_record(), [review])
        self.assertEqual(
            located(report), [("V3-ASSURANCE-BLOCKER-INVENTED", "unresolved_finding_ids")]
        )
        self.assertIn("f-imagined", report.issues[0].message)

    def test_a_non_blocking_finding_is_not_an_unresolved_blocker(self) -> None:
        review = make_review(findings=[make_finding("f-style", blocking=False)])
        clean = make_candidate(review_refs=review_refs_for(review))
        self.assertEqual(codes(summary.check_assurance_candidate(clean, make_record(), [review])), [])
        inflated = make_candidate(
            review_refs=review_refs_for(review), unresolved_finding_ids=["f-style"]
        )
        self.assertEqual(
            codes(summary.check_assurance_candidate(inflated, make_record(), [review])),
            ["V3-ASSURANCE-BLOCKER-INVENTED"],
        )

    def test_a_blocker_raised_at_full_and_still_open_at_verify_stays_unresolved(self) -> None:
        full = make_review(findings=[make_finding("f-changelog")])
        verify = make_review(
            result_id="rr-verify",
            review_round="VERIFY",
            verdict="REVIEWED_NO_BLOCKER",
            candidate_commit=CANDIDATE_C2,
            findings=[make_finding("f-links", obligation_id="ob-links")],
        )
        record = make_record(candidate_commit=CANDIDATE_C2, repair_round=1)
        base = {
            "repair_round": 1,
            "candidate_ref": {"branch": "candidate", "commit": CANDIDATE_C2},
            "review_refs": review_refs_for(full, verify),
        }
        faithful = make_candidate(**base, unresolved_finding_ids=["f-changelog", "f-links"])
        self.assertEqual(
            codes(summary.check_assurance_candidate(faithful, record, [full, verify])), []
        )

        partial = make_candidate(**base, unresolved_finding_ids=["f-links"])
        report = summary.check_assurance_candidate(partial, record, [full, verify])
        self.assertEqual(located(report), [("V3-ASSURANCE-BLOCKER-DROPPED", "unresolved_finding_ids")])
        self.assertIn("f-changelog", report.issues[0].message)

    def test_a_review_round_that_happened_but_is_unbound_is_named(self) -> None:
        full = make_review(findings=[make_finding("f-changelog")])
        verify = make_review(
            result_id="rr-verify",
            review_round="VERIFY",
            verdict="REVIEWED_NO_BLOCKER",
            candidate_commit=CANDIDATE_C2,
        )
        candidate = make_candidate(unresolved_finding_ids=["f-changelog"])  # one review_ref only
        self.assertIn(
            ("V3-ASSURANCE-REVIEW-BINDING-INCOMPLETE", "review_refs"),
            located(summary.check_assurance_candidate(candidate, make_record(), [full, verify])),
        )

    def test_binding_no_reviews_at_all_is_reported_rather_than_passing_clean(self) -> None:
        """The fail-open probe: an empty review set must not silently satisfy the guard."""
        candidate = make_candidate(unresolved_finding_ids=["f-changelog"])
        report = summary.check_assurance_candidate(candidate, make_record(), [])
        self.assertIn("V3-ASSURANCE-BLOCKER-INVENTED", codes(report))
        self.assertIn("V3-ASSURANCE-REVIEW-BINDING-INCOMPLETE", codes(report))

    def test_a_review_ref_binding_bytes_no_review_has_is_named(self) -> None:
        """Defect M6: the count check alone was satisfied by a ref to anything."""
        review = make_review()
        candidate = make_candidate(review_refs=[ref("control/review-full.json", 0x99)])
        self.assertEqual(
            located(summary.check_assurance_candidate(candidate, make_record(), [review])),
            [
                ("V3-ASSURANCE-REVIEW-UNBOUND", "review_refs"),
                ("V3-ASSURANCE-REVIEW-INVENTED", "review_refs"),
            ],
        )

    def test_a_stale_round_zero_ref_in_a_repaired_run_is_named(self) -> None:
        """Same count, wrong bytes: one live ref plus one stale ref passes the count."""
        full = make_review(findings=[make_finding("f-changelog")])
        verify = make_review(
            result_id="rr-verify",
            review_round="VERIFY",
            verdict="REVIEWED_NO_BLOCKER",
            candidate_commit=CANDIDATE_C2,
        )
        record = make_record(candidate_commit=CANDIDATE_C2, repair_round=1)
        candidate = make_candidate(
            repair_round=1,
            candidate_ref={"branch": "candidate", "commit": CANDIDATE_C2},
            review_refs=[review_refs_for(full)[0], ref("control/review-verify.json", 0x99)],
            unresolved_finding_ids=["f-changelog"],
        )
        self.assertEqual(
            located(summary.check_assurance_candidate(candidate, record, [full, verify])),
            [
                ("V3-ASSURANCE-REVIEW-UNBOUND", "review_refs"),
                ("V3-ASSURANCE-REVIEW-INVENTED", "review_refs"),
            ],
        )

    def test_run_candidate_and_round_mismatches_are_each_named(self) -> None:
        review = make_review()
        cases = {
            "V3-ASSURANCE-RUN-MISMATCH": (make_candidate(run_id="run-two"), make_record()),
            "V3-ASSURANCE-WRONG-CANDIDATE": (
                make_candidate(candidate_ref={"branch": "candidate", "commit": CANDIDATE_C2}),
                make_record(),
            ),
            "V3-ASSURANCE-ROUND-MISMATCH": (make_candidate(repair_round=1), make_record()),
        }
        for expected, (candidate, record) in cases.items():
            with self.subTest(code=expected):
                self.assertIn(
                    expected, codes(summary.check_assurance_candidate(candidate, record, [review]))
                )

    def test_the_candidate_carries_no_document_produced_after_it(self) -> None:
        """N2-A7: a binding cannot include the thing it precedes."""
        for field in summary.FORWARD_FIELDS:
            with self.subTest(forward_field=field):
                candidate = make_candidate()
                candidate[field] = (
                    ref("control/later.json", 0x41) if field.endswith("_ref") else "ACCEPT"
                )
                report = summary.check_assurance_candidate(candidate, make_record(), [make_review()])
                self.assertIn(
                    "V3-SCHEMA-ASSURANCE_CANDIDATE",
                    codes(report),
                    f"a candidate carrying '{field}' must be refused",
                )


# ---------------------------------------------------------------------------
# N2-A7 / N2-A8 / N2-A9 — the single terminal summary
# ---------------------------------------------------------------------------


class SummaryIsTheUsersDecision(unittest.TestCase):
    """Exactly one summary follows FINAL, and it says exactly what the user decided."""

    def test_negative_control_a_generated_summary_checks_clean(self) -> None:
        candidate = make_candidate()
        decision = make_final_decision(candidate=candidate)
        document = make_summary(candidate=candidate, decision=decision)
        self.assertEqual(codes(summary.check_summary(document, candidate, decision)), [])

    def test_a_summary_is_generated_only_from_a_final_decision(self) -> None:
        candidate = make_candidate()
        for phase in ("REPAIR", "START", "ISSUE_TRIAGE"):
            with self.subTest(phase=phase):
                if phase == "REPAIR":
                    wrong = make_repair_decision()
                elif phase == "START":
                    wrong = make_decision(
                        phase="START",
                        decision="START",
                        target={
                            "resolved_plan_ref": ref("control/resolved-plan.json", 0x12),
                            "instruction_audit_ref": ref("control/instruction-audit.json", 0x13),
                        },
                    )
                else:
                    wrong = make_triage()
                with self.assertRaises(SpecGap) as raised:
                    summary.generate_summary(
                        summary_id="sum-one",
                        candidate=candidate,
                        candidate_ref=ref("control/assurance-candidate.json", 0x20),
                        decision=wrong,
                        decision_ref=ref("control/decision.json", 0x21),
                        promotion=summary.no_promotion("nothing was promoted"),
                        generated_by=CONTROLLER,
                    )
                self.assertIn("V3-ASSURANCE-NOT-FINAL", str(raised.exception))
                self.assertIn(phase, str(raised.exception))

    def test_the_outcome_is_copied_and_never_edited(self) -> None:
        candidate = make_candidate()
        decision = make_final_decision(
            candidate=candidate,
            decision="ACCEPT_WITH_LIMITATIONS",
            limitations=["the tone obligation was unverifiable within the frozen subjects"],
        )
        generated = make_summary(candidate=candidate, decision=decision)
        self.assertEqual(generated["outcome"], "ACCEPT_WITH_LIMITATIONS")
        self.assertEqual(generated["limitations"], decision["limitations"])

        softened = dict(generated)
        softened["outcome"] = "ACCEPT"
        report = summary.check_summary(softened, candidate, decision)
        self.assertEqual(located(report), [("V3-ASSURANCE-OUTCOME-ALTERED", "outcome")])

    def test_every_outcome_substitution_is_caught(self) -> None:
        candidate = make_candidate()
        outcomes = ("ACCEPT", "ACCEPT_WITH_LIMITATIONS", "REJECT", "REPLAN")
        for decided in outcomes:
            limitations = ["one obligation stayed unverifiable"] if decided == "ACCEPT_WITH_LIMITATIONS" else ()
            decision = make_final_decision(candidate=candidate, decision=decided, limitations=limitations)
            promotion = (
                summary.no_promotion("the decision does not authorize promotion")
                if decided in ("REJECT", "REPLAN")
                else summary.promoted_to(
                    {"branch": "main", "commit": CANDIDATE_C}, "the user accepted and promoted"
                )
            )
            generated = make_summary(candidate=candidate, decision=decision, promotion=promotion)
            for reported in outcomes:
                with self.subTest(decided=decided, reported=reported):
                    document = dict(generated)
                    document["outcome"] = reported
                    if reported == "ACCEPT_WITH_LIMITATIONS" and not document.get("limitations"):
                        document["limitations"] = ["one obligation stayed unverifiable"]
                    if reported in ("REJECT", "REPLAN") and document["promotion"]["promoted"]:
                        continue  # the schema refuses this shape; covered in EnforcementLayerIsPinned
                    report = summary.check_summary(document, candidate, decision)
                    if reported == decided:
                        self.assertNotIn("V3-ASSURANCE-OUTCOME-ALTERED", codes(report))
                    else:
                        self.assertIn("V3-ASSURANCE-OUTCOME-ALTERED", codes(report))

    def test_a_dropped_limitation_is_named(self) -> None:
        candidate = make_candidate()
        decision = make_final_decision(
            candidate=candidate,
            decision="ACCEPT_WITH_LIMITATIONS",
            limitations=[
                "the tone obligation was unverifiable within the frozen subjects",
                "one source input could not be resolved at its frozen revision",
            ],
        )
        generated = make_summary(candidate=candidate, decision=decision)
        trimmed = dict(generated)
        trimmed["limitations"] = generated["limitations"][:1]
        self.assertEqual(
            located(summary.check_summary(trimmed, candidate, decision)),
            [("V3-ASSURANCE-LIMITATIONS-ALTERED", "limitations")],
        )

    def test_an_invented_limitation_is_named(self) -> None:
        candidate = make_candidate()
        decision = make_final_decision(candidate=candidate, decision="ACCEPT")
        generated = make_summary(candidate=candidate, decision=decision)
        embellished = dict(generated)
        embellished["limitations"] = ["a limitation the user never acknowledged"]
        self.assertEqual(
            located(summary.check_summary(embellished, candidate, decision)),
            [("V3-ASSURANCE-LIMITATIONS-ALTERED", "limitations")],
        )

    def test_generate_refuses_a_decision_ref_binding_other_bytes(self) -> None:
        """Defect M7, generate side: both are in hand, so a mismatch refuses to ship."""
        candidate = make_candidate()
        decision = make_final_decision(candidate=candidate)
        with self.assertRaises(SpecGap) as raised:
            summary.generate_summary(
                summary_id="sum-one",
                candidate=candidate,
                candidate_ref={
                    "path": "control/assurance-candidate.json",
                    "digest_sha256": summary.candidate_digest(candidate),
                },
                decision=decision,
                decision_ref=ref("control/final-decision.json", 0x99),
                promotion=summary.no_promotion("nothing was promoted"),
                generated_by=CONTROLLER,
            )
        self.assertIn("V3-ASSURANCE-DECISION-BINDING-MISMATCH", str(raised.exception))

    def test_a_summary_citing_a_decision_it_was_not_generated_from_is_named(self) -> None:
        """Defect M7, check side: the recorded pointer must name the decision in hand."""
        candidate = make_candidate()
        decision = make_final_decision(candidate=candidate)
        tampered = dict(make_summary(candidate=candidate, decision=decision))
        tampered["final_decision_ref"] = ref("control/final-decision.json", 0x99)
        self.assertEqual(
            located(summary.check_summary(tampered, candidate, decision)),
            [("V3-ASSURANCE-DECISION-BINDING-MISMATCH", "final_decision_ref/digest_sha256")],
        )

    def test_a_summary_bound_to_different_candidate_bytes_is_named(self) -> None:
        candidate = make_candidate()
        decision = make_final_decision(candidate=candidate)
        generated = make_summary(candidate=candidate, decision=decision)
        other = make_candidate(assurance_candidate_id="ac-two")
        self.assertEqual(
            located(summary.check_summary(generated, other, decision)),
            [
                ("V3-ASSURANCE-CANDIDATE-BINDING-MISMATCH", "assurance_candidate_ref/digest_sha256"),
                ("V3-ASSURANCE-DECISION-TARGET-MISMATCH", "final_decision_ref"),
            ],
        )

    def test_a_summary_terminating_a_non_final_decision_is_named(self) -> None:
        candidate = make_candidate()
        decision = make_final_decision(candidate=candidate)
        generated = make_summary(candidate=candidate, decision=decision)
        # The document is well-formed; the decision handed alongside it is from another phase.
        report = summary.check_summary(generated, candidate, make_repair_decision())
        self.assertIn(("V3-ASSURANCE-NOT-FINAL", "final_decision_ref"), located(report))

    def test_exactly_one_summary_pointer_exists_on_the_state(self) -> None:
        """'Exactly one' is structural: `summary_ref` is a single pointer, never a list."""
        state = make_state("CLOSED")
        state["summary_ref"] = [
            {"path": "control/summary.json"},
            {"path": "control/summary-2.json"},
        ]
        self.assertEqual(codes(validate("state", state)), ["V3-SCHEMA-STATE"])


class PromotionIsExplicit(unittest.TestCase):
    """N2-A8: REJECT/REPLAN never promotes; an accepted promotion says where and why."""

    def test_negative_control_an_accepted_promotion_is_recorded_and_valid(self) -> None:
        candidate = make_candidate()
        decision = make_final_decision(candidate=candidate, decision="ACCEPT")
        promotion = summary.promoted_to(
            {"branch": "main", "commit": CANDIDATE_C}, "the user accepted and authorized promotion"
        )
        document = make_summary(candidate=candidate, decision=decision, promotion=promotion)
        self.assertEqual(codes(summary.check_summary(document, candidate, decision)), [])
        self.assertTrue(document["promotion"]["promoted"])
        self.assertEqual(document["promotion"]["promoted_to"]["branch"], "main")

    def test_an_acceptance_may_leave_the_payload_unpromoted(self) -> None:
        candidate = make_candidate()
        decision = make_final_decision(candidate=candidate, decision="ACCEPT")
        document = make_summary(
            candidate=candidate,
            decision=decision,
            promotion=summary.no_promotion("accepted, but the user promotes by hand later"),
        )
        self.assertEqual(codes(summary.check_summary(document, candidate, decision)), [])
        self.assertFalse(document["promotion"]["promoted"])

    def test_a_refusal_that_promoted_is_refused(self) -> None:
        for outcome in ("REJECT", "REPLAN"):
            with self.subTest(outcome=outcome):
                candidate = make_candidate()
                decision = make_final_decision(candidate=candidate, decision=outcome)
                document = make_summary(
                    candidate=candidate,
                    decision=decision,
                    promotion=summary.no_promotion("the decision does not authorize promotion"),
                )
                document["promotion"] = {
                    "promoted": True,
                    "promoted_to": {"branch": "main", "commit": CANDIDATE_C},
                    "reason": "promoted despite the refusal",
                }
                self.assertEqual(
                    codes(validate_n2("assurance_summary", document)),
                    ["V3-SCHEMA-ASSURANCE_SUMMARY"],
                    f"a {outcome} summary must never carry promoted:true",
                )

    def test_negative_control_a_refusal_that_did_not_promote_is_valid(self) -> None:
        for outcome in ("REJECT", "REPLAN"):
            with self.subTest(outcome=outcome):
                candidate = make_candidate()
                decision = make_final_decision(candidate=candidate, decision=outcome)
                document = make_summary(
                    candidate=candidate,
                    decision=decision,
                    promotion=summary.no_promotion("the decision does not authorize promotion"),
                )
                self.assertEqual(codes(validate_n2("assurance_summary", document)), [])
                self.assertEqual(codes(summary.check_summary(document, candidate, decision)), [])

    def test_a_promotion_that_does_not_say_where_it_went_is_refused(self) -> None:
        candidate = make_candidate()
        decision = make_final_decision(candidate=candidate, decision="ACCEPT")
        document = make_summary(candidate=candidate, decision=decision)
        document["promotion"] = {"promoted": True, "reason": "it went somewhere"}
        self.assertEqual(
            codes(validate_n2("assurance_summary", document)), ["V3-SCHEMA-ASSURANCE_SUMMARY"]
        )

    def test_a_promotion_that_does_not_say_why_is_refused(self) -> None:
        candidate = make_candidate()
        decision = make_final_decision(candidate=candidate, decision="ACCEPT")
        document = make_summary(candidate=candidate, decision=decision)
        document["promotion"] = {"promoted": True, "promoted_to": {"branch": "main"}}
        self.assertEqual(
            codes(validate_n2("assurance_summary", document)), ["V3-SCHEMA-ASSURANCE_SUMMARY"]
        )

    def test_the_helpers_produce_the_two_recorded_shapes(self) -> None:
        self.assertEqual(
            summary.no_promotion("nothing moved anywhere"),
            {"promoted": False, "reason": "nothing moved anywhere"},
        )
        promoted = summary.promoted_to({"branch": "main"}, "the user authorized promotion")
        self.assertEqual(promoted["promoted"], True)
        self.assertEqual(promoted["promoted_to"], {"branch": "main"})


# ---------------------------------------------------------------------------
# Inherited residual N1-R2 — the governance obligation
# ---------------------------------------------------------------------------


class GovernanceScanStateIsAlwaysStated(unittest.TestCase):
    """N1-R2: nothing previously obliged a run to include the R4 governance scan.

    The obligation is to *report* the state, not to force the scan. So the three properties
    are: the state cannot be left unsaid, a skip carries a reason, and a skip surfaces as a
    disclosure the user sees rather than vanishing.
    """

    def test_neither_result_nor_reason_fails_closed(self) -> None:
        with self.assertRaises(SpecGap) as raised:
            flow.governance_state()
        self.assertIn("V3-FLOW-GOVERNANCE-UNSTATED", str(raised.exception))

    def test_both_at_once_fails_closed(self) -> None:
        with self.assertRaises(SpecGap) as raised:
            flow.governance_state(
                result_ref=ref("control/check-r4.json", 0x18), skip_reason="and also skipped"
            )
        self.assertIn("V3-FLOW-GOVERNANCE-UNSTATED", str(raised.exception))

    def test_a_scan_that_ran_references_its_result(self) -> None:
        state = flow.governance_state(result_ref=ref("control/check-r4.json", 0x18))
        self.assertEqual(state["included"], True)
        self.assertEqual(state["result_ref"]["path"], "control/check-r4.json")
        self.assertEqual(codes(flow.check_governance_obligation({"governance_scan": state})), [])

    def test_a_skip_carries_its_reason(self) -> None:
        state = flow.governance_state(skip_reason="no governance document changed in this run")
        self.assertEqual(state["included"], False)
        self.assertEqual(state["skip_reason"], "no governance document changed in this run")
        self.assertEqual(codes(flow.check_governance_obligation({"governance_scan": state})), [])

    def test_a_candidate_that_says_nothing_about_the_scan_is_refused(self) -> None:
        """The obligation lands in the document itself: the field is not optional."""
        candidate = make_candidate(governance_scan=None)
        self.assertEqual(
            codes(validate_n2("assurance_candidate", candidate)), ["V3-SCHEMA-ASSURANCE_CANDIDATE"]
        )
        self.assertEqual(
            located(flow.check_governance_obligation(candidate)),
            [("V3-FLOW-GOVERNANCE-UNSTATED", "governance_scan")],
        )

    def test_a_claim_that_the_scan_ran_must_reference_evidence(self) -> None:
        candidate = make_candidate(governance_scan={"included": True})
        self.assertEqual(
            codes(validate_n2("assurance_candidate", candidate)), ["V3-SCHEMA-ASSURANCE_CANDIDATE"]
        )
        self.assertEqual(
            located(flow.check_governance_obligation(candidate)),
            [("V3-FLOW-GOVERNANCE-UNEVIDENCED", "governance_scan/result_ref")],
        )

    def test_a_skip_without_a_reason_is_refused(self) -> None:
        candidate = make_candidate(governance_scan={"included": False})
        self.assertEqual(
            codes(validate_n2("assurance_candidate", candidate)), ["V3-SCHEMA-ASSURANCE_CANDIDATE"]
        )

    def test_a_skip_surfaces_as_a_user_visible_disclosure(self) -> None:
        skip = flow.governance_state(skip_reason="no governance document changed in this run")
        candidate = make_candidate(governance_scan=skip)
        candidate_ref = ref("control/assurance-candidate.json", 0x20)
        disclosures = flow.governance_disclosures(candidate, candidate_ref)
        self.assertEqual(len(disclosures), 1)
        self.assertIn("governance frontmatter scan did not run", disclosures[0]["statement"])
        self.assertIn("no governance document changed", disclosures[0]["statement"])
        self.assertEqual(disclosures[0]["source_ref"], candidate_ref)

        # And it survives into the document the user decides from.
        disclosed = make_candidate(governance_scan=skip, disclosures=disclosures)
        self.assertEqual(codes(validate_n2("assurance_candidate", disclosed)), [])
        self.assertEqual(disclosed["disclosures"], disclosures)

    def test_negative_control_a_scan_that_ran_discloses_nothing(self) -> None:
        candidate = make_candidate()
        self.assertEqual(
            flow.governance_disclosures(candidate, ref("control/assurance-candidate.json", 0x20)), []
        )

    def test_a_disclosure_must_name_the_document_it_came_from(self) -> None:
        """A disclosure with no source would be the controller speaking in its own voice."""
        candidate = make_candidate(
            governance_scan=flow.governance_state(skip_reason="skipped for a stated reason"),
            disclosures=[{"statement": "the governance scan did not run in this run"}],
        )
        self.assertEqual(
            codes(validate_n2("assurance_candidate", candidate)), ["V3-SCHEMA-ASSURANCE_CANDIDATE"]
        )


# ---------------------------------------------------------------------------
# N2-A10 — the HarnessIssue is post-run
# ---------------------------------------------------------------------------


class HarnessIssueCannotTouchTheLiveRun(unittest.TestCase):
    """An issue is observed after a run ended; it changes nothing about the run it came from."""

    def test_the_missing_state_argument_reports_rather_than_stays_silent(self) -> None:
        """The fail-open probe: an unchecked property must report itself as unchecked."""
        report = issues.check_issue(make_issue())
        self.assertEqual(
            located(report), [("V3-HARNESS-ISSUE-RUN-STATE-UNVERIFIED", "observed_after")]
        )
        self.assertIn("unverified property, not a satisfied one", report.issues[0].message)

    def test_negative_control_a_supplied_terminal_state_reports_nothing(self) -> None:
        for status in TERMINAL:
            with self.subTest(status=status):
                issue = make_issue(observed_after=status)
                self.assertEqual(codes(issues.check_issue(issue, make_state(status))), [])

    def test_an_issue_recorded_against_a_live_run_is_named(self) -> None:
        for status in STATUSES:
            if status in TERMINAL:
                continue
            with self.subTest(status=status):
                report = issues.check_issue(make_issue(), make_state(status))
                self.assertEqual(
                    located(report), [("V3-HARNESS-ISSUE-RUN-STILL-LIVE", "observed_after")]
                )

    def test_an_issue_naming_another_run_is_named(self) -> None:
        state = make_state("CLOSED")
        state["run_id"] = "run-two"
        report = issues.check_issue(make_issue(), state)
        self.assertEqual(located(report), [("V3-HARNESS-ISSUE-RUN-MISMATCH", "run_id")])

    def test_an_issue_naming_the_wrong_terminal_status_is_named(self) -> None:
        report = issues.check_issue(make_issue(observed_after="STOPPED_REPLAN"), make_state("CLOSED"))
        self.assertEqual(
            located(report), [("V3-HARNESS-ISSUE-TERMINAL-STATUS-MISMATCH", "observed_after")]
        )

    def test_a_mid_run_observation_is_unrepresentable(self) -> None:
        for status in STATUSES:
            if status in TERMINAL:
                continue
            with self.subTest(status=status):
                self.assertEqual(
                    codes(validate_n2("harness_issue", make_issue(observed_after=status))),
                    ["V3-SCHEMA-HARNESS_ISSUE"],
                )

    def test_an_evidence_free_issue_is_refused(self) -> None:
        self.assertEqual(
            codes(validate_n2("harness_issue", make_issue(evidence_refs=[]))),
            ["V3-SCHEMA-HARNESS_ISSUE"],
        )

    def test_the_recorded_issue_is_complete_when_written(self) -> None:
        issue = issues.record_issue(
            issue_id="hi-two",
            work_id=WORK_ID,
            run_id=RUN_ID,
            kind="PROCESS_BURDEN",
            statement="freezing the package cost more than the work it protected",
            evidence_refs=[ref("control/review-package.json", 0x9A)],
            observed_after="STOPPED_REPLAN",
            observed_by=OBSERVER,
        )
        self.assertEqual(codes(validate_n2("harness_issue", issue)), [])
        self.assertNotIn("observed_at", issue)  # optional, and absent rather than empty


class TriageIsTheOnlyRoute(unittest.TestCase):
    """Only a post-run user ISSUE_TRIAGE decision routes an issue (V3-D10, contract §11)."""

    def test_negative_control_a_well_formed_triage_reports_nothing(self) -> None:
        self.assertEqual(codes(issues.check_triage(make_triage(), make_issue())), [])

    def test_every_closed_route_round_trips(self) -> None:
        self.assertEqual(
            issues.TRIAGE_ROUTES,
            (
                "WORKFLOW_FIX",
                "DOCUMENT_ASSURANCE_PROFILE_CANDIDATE",
                "VERIFIER_FIX",
                "CORE_CANDIDATE",
                "DEFER",
                "DISMISS",
            ),
        )
        for route in issues.TRIAGE_ROUTES:
            with self.subTest(route=route):
                decision = make_triage(decision=route)
                self.assertEqual(codes(issues.check_triage(decision, make_issue())), [])
                self.assertEqual(issues.triage_route(decision), route)

    def test_a_decision_from_another_phase_never_routes_an_issue(self) -> None:
        final = make_final_decision()
        self.assertEqual(located(issues.check_triage(final, make_issue())), [("V3-HARNESS-ISSUE-PHASE", "phase")])
        with self.assertRaises(SpecGap) as raised:
            issues.triage_route(final)
        self.assertIn("V3-HARNESS-ISSUE-PHASE", str(raised.exception))

    def test_a_triage_naming_a_different_work_is_named(self) -> None:
        decision = make_triage(work_id="other-work")
        self.assertEqual(
            located(issues.check_triage(decision, make_issue())),
            [("V3-HARNESS-ISSUE-WORK-MISMATCH", "work_id")],
        )

    def test_a_route_outside_the_closed_set_is_refused(self) -> None:
        decision = make_triage()
        decision["decision"] = "ACCEPT"
        self.assertEqual(
            codes(issues.check_triage(decision, make_issue())),
            ["V3-SCHEMA-DECISION", "V3-HARNESS-ISSUE-UNKNOWN-ROUTE"],
        )

    def test_a_triage_that_points_at_no_issue_is_refused(self) -> None:
        decision = make_triage()
        decision["target"] = {}
        self.assertEqual(
            codes(issues.check_triage(decision, make_issue())),
            ["V3-SCHEMA-DECISION", "V3-HARNESS-ISSUE-UNBOUND-TRIAGE"],
        )

    def test_a_triage_pointing_at_a_sibling_issue_of_the_same_work_is_named(self) -> None:
        """The p3-corr shape: several issues on one work, triaged in one pass.

        `work_id` alone cannot say WHICH issue a decision routes, so before this guard a
        decision made about a sibling issue read as this issue's routing and reported
        clean — the CT defect (rider bank, redeemed Phase D).
        """
        decision = make_triage(issue_path="control/hi-two.json")
        self.assertEqual(
            located(issues.check_triage(decision, make_issue())),
            [("V3-HARNESS-ISSUE-TARGET-MISMATCH", "target/harness_issue_ref/path")],
        )

    def test_an_issue_with_no_identity_cannot_be_bound_to_any_target(self) -> None:
        self.assertEqual(
            located(issues.check_triage(make_triage(), make_issue(issue_id=None))),
            [("V3-HARNESS-ISSUE-TARGET-MISMATCH", "target/harness_issue_ref/path")],
        )

    def test_a_triage_from_another_run_of_the_same_work_is_named(self) -> None:
        """L-2 (v3-review-full-34cf85b.md): the guard bound issue and work but not run.

        Two runs of one work can each hold a same-named issue, so a decision made in
        one run must not read as the other run's routing. The comparison fires only
        when both documents carry `run_id` (optional on the decision side).
        """
        decision = make_triage()
        decision["run_id"] = "run-two"
        self.assertEqual(
            located(issues.check_triage(decision, make_issue())),
            [("V3-HARNESS-ISSUE-TRIAGE-RUN-MISMATCH", "run_id")],
        )


# ---------------------------------------------------------------------------
# N2-A11 — no recursion, no generic waiver, no lifecycle
# ---------------------------------------------------------------------------


class NoRecursionNoWaiverNoLifecycle(unittest.TestCase):
    """The absences are the property, so each is asserted rather than assumed."""

    #: Vocabulary that would turn a bounded assurance run into a generic gate/waiver system,
    #: or an observation into a work item with a state. Matched per underscore-separated token
    #: on property names only, so legitimate values (the DISMISS triage route) are untouched.
    BANNED_PROPERTY_TOKENS = frozenset(
        {
            "waiver",
            "waivers",
            "waive",
            "waived",
            "override",
            "overrides",
            "overridden",
            "exemption",
            "exemptions",
            "exempt",
            "gate",
            "gates",
            "suppress",
            "suppressed",
            "retrospective",
            "dedup",
            "lifecycle",
            "resolution",
            "reopened",
            "assignee",
        }
    )

    N2_SCHEMA_FILENAMES = (
        "review.schema.json",
        "assurance.schema.json",
        "harness-issue.schema.json",
    )

    @staticmethod
    def property_names(node: Any) -> list[str]:
        found: list[str] = []
        if isinstance(node, dict):
            block = node.get("properties")
            if isinstance(block, dict):
                found.extend(block.keys())
            for value in node.values():
                found.extend(NoRecursionNoWaiverNoLifecycle.property_names(value))
        elif isinstance(node, list):
            for value in node:
                found.extend(NoRecursionNoWaiverNoLifecycle.property_names(value))
        return found

    def test_no_generic_waiver_gate_or_lifecycle_property_exists(self) -> None:
        for filename in self.N2_SCHEMA_FILENAMES:
            document = json.loads((SCHEMA_DIR / filename).read_text(encoding="utf-8"))
            for name in self.property_names(document):
                for token in re.split(r"[_-]", name):
                    with self.subTest(schema=filename, property=name, token=token):
                        self.assertNotIn(token.lower(), self.BANNED_PROPERTY_TOKENS)

    def test_the_harness_issue_carries_exactly_its_declared_fields(self) -> None:
        document = json.loads((SCHEMA_DIR / "harness-issue.schema.json").read_text(encoding="utf-8"))
        self.assertFalse(document["additionalProperties"])
        self.assertEqual(
            sorted(document["properties"]),
            [
                "evidence_refs",
                "issue_id",
                "kind",
                "observed_after",
                "observed_at",
                "observed_by",
                "run_id",
                "statement",
                "work_id",
            ],
        )

    def test_a_status_or_resolution_field_on_an_issue_is_unrepresentable(self) -> None:
        for field, value in (
            ("status", "OPEN"),
            ("resolution", "FIXED"),
            ("triage_route", "WORKFLOW_FIX"),
            ("assignee", "someone"),
            ("dedup_key", "abc"),
        ):
            with self.subTest(field=field):
                self.assertEqual(
                    codes(validate_n2("harness_issue", make_issue(**{field: value}))),
                    ["V3-SCHEMA-HARNESS_ISSUE"],
                )

    def test_the_issues_module_exports_no_writer(self) -> None:
        """Routing lives with the person who chose it, not as mutable state on the issue."""
        mutators = re.compile(r"^(update|set|close|resolve|reopen|mutate|apply|amend|edit|patch)_")
        for name in issues.__all__:
            with self.subTest(export=name):
                self.assertIsNone(mutators.match(name))
        self.assertNotIn("route_issue", issues.__all__)
        self.assertNotIn("resolve_issue", issues.__all__)

    def test_no_third_review_round_can_be_bound(self) -> None:
        candidate = make_candidate(
            review_refs=[
                ref("control/review-full.json", 0x17),
                ref("control/review-verify.json", 0x19),
                ref("control/review-third.json", 0x1A),
            ]
        )
        self.assertEqual(
            codes(validate_n2("assurance_candidate", candidate)), ["V3-SCHEMA-ASSURANCE_CANDIDATE"]
        )

    def test_a_full_round_declares_no_verify_scope(self) -> None:
        full = make_review(findings=[make_finding("f-changelog")])
        full["verify_scope"] = {
            "accepted_finding_ids": ["f-changelog"],
            "repair_diff_reviewed": True,
            "permanent_boundaries_checked": True,
        }
        self.assertEqual(codes(validate_n2("review_result", full)), ["V3-SCHEMA-REVIEW_RESULT"])

    def test_the_status_set_is_closed_and_has_two_terminals(self) -> None:
        common = json.loads((SCHEMA_DIR / "common.schema.json").read_text(encoding="utf-8"))
        self.assertEqual(tuple(common["$defs"]["assuranceStatus"]["enum"]), STATUSES)
        self.assertEqual(flow.TERMINAL_STATUSES, frozenset(TERMINAL))

    def test_the_repair_round_cap_is_one(self) -> None:
        state = make_state("REPAIRING")
        state["repair_round"] = 2
        self.assertEqual(codes(validate("state", state)), ["V3-SCHEMA-STATE"])
        self.assertEqual(
            codes(validate_n2("assurance_candidate", make_candidate(repair_round=2))),
            ["V3-SCHEMA-ASSURANCE_CANDIDATE"],
        )


# ---------------------------------------------------------------------------
# Reachability — which layer actually holds each conditional property
# ---------------------------------------------------------------------------


class EnforcementLayerIsPinned(unittest.TestCase):
    """For each conditional property, the code that actually fires is named.

    V3-N1 shipped an invariant that could never fire because an earlier return had already
    rejected the document, so "the guard exists" is not evidence that the guard runs. Each
    case below feeds a document that violates exactly one property and pins the code the
    harness really reports — which is what a later reader needs in order to know whether
    editing a schema conditional silently removes the only enforcement of a rule.

    Three of these properties are held at BOTH layers, and the module's own code is asserted
    as well as the schema's: a generic "does not match the schema" does not tell a user which
    of a dozen conditionals they violated, and that specificity is the whole reason the
    module keeps a named guard alongside a schema that already refuses the document.
    """

    def test_a_forward_field_on_a_candidate_is_named_at_both_layers(self) -> None:
        report = summary.check_assurance_candidate(
            make_candidate(summary_ref=ref("control/summary.json", 0x51)),
            make_record(),
            [make_review()],
        )
        self.assertIn("V3-SCHEMA-ASSURANCE_CANDIDATE", codes(report))
        self.assertIn(
            ("V3-ASSURANCE-SELF-BINDING", "summary_ref"),
            located(report),
            "the guard must name WHICH forward field appeared, not defer to a schema error",
        )

    def test_a_refusal_that_promoted_is_named_at_both_layers(self) -> None:
        candidate = make_candidate()
        decision = make_final_decision(candidate=candidate, decision="REJECT")
        document = make_summary(
            candidate=candidate,
            decision=decision,
            promotion=summary.no_promotion("the decision does not authorize promotion"),
        )
        document["promotion"] = {
            "promoted": True,
            "promoted_to": {"branch": "main"},
            "reason": "promoted despite the refusal",
        }
        report = summary.check_summary(document, candidate, decision)
        self.assertIn("V3-SCHEMA-ASSURANCE_SUMMARY", codes(report))
        self.assertIn(
            ("V3-ASSURANCE-PROMOTED-AFTER-REFUSAL", "promotion/promoted"), located(report)
        )

    def test_an_unrecorded_promotion_is_named_at_both_layers(self) -> None:
        candidate = make_candidate()
        decision = make_final_decision(candidate=candidate, decision="ACCEPT")
        document = make_summary(candidate=candidate, decision=decision)
        document["promotion"] = {"promoted": True, "reason": "went somewhere unnamed"}
        report = summary.check_summary(document, candidate, decision)
        self.assertIn("V3-SCHEMA-ASSURANCE_SUMMARY", codes(report))
        self.assertIn(
            ("V3-ASSURANCE-PROMOTION-UNRECORDED", "promotion/promoted_to"), located(report)
        )

    def test_a_triage_route_outside_the_closed_set_is_held_by_two_layers(self) -> None:
        """Both layers speak: the schema rejects it, and the module names which route was bad.

        The module's own code was once unreachable behind an early schema return, so this
        pins that the specific reason survives alongside the generic one.
        """
        decision = make_triage()
        decision["decision"] = "REPLAN"
        self.assertEqual(
            codes(issues.check_triage(decision, make_issue())),
            ["V3-SCHEMA-DECISION", "V3-HARNESS-ISSUE-UNKNOWN-ROUTE"],
        )

    def test_governance_state_is_held_by_the_schema_and_by_the_builder(self) -> None:
        # Schema layer: the field is required, and its two branches are conditional.
        self.assertEqual(
            codes(validate_n2("assurance_candidate", make_candidate(governance_scan=None))),
            ["V3-SCHEMA-ASSURANCE_CANDIDATE"],
        )
        # Builder layer: neither-nor is refused before a document can be written at all.
        with self.assertRaises(SpecGap):
            flow.governance_state()

    def test_the_module_level_codes_that_do_fire_are_reachable_with_valid_documents(self) -> None:
        """Every flow/summary/issues code this matrix relies on, triggered from a valid base."""
        reached: set[str] = set()
        reached.update(codes(flow.check_transition({"status": "CLOSED", "repair_round": 0}, "AUDITED")))
        reached.update(codes(flow.check_transition({"status": "RESOLVED", "repair_round": 0}, "CLOSED")))
        reached.update(codes(flow.check_transition({"status": "REVIEWED", "repair_round": 1}, "REPAIRING")))

        missing_pointer = make_state("REVIEWED")
        del missing_pointer["review_ref"]
        reached.update(codes(flow.check_state_pointers(missing_pointer)))

        premature = make_state("EVIDENCED")
        premature["summary_ref"] = {"path": POINTER_PATHS["summary_ref"]}
        reached.update(codes(flow.check_state_pointers(premature)))

        stopped = make_state("STOPPED_REPLAN")
        del stopped["blockers"]
        reached.update(codes(flow.check_state_pointers(stopped)))
        reached.update(codes(flow.check_state_pointers(make_state("EVIDENCED", repair_round=1))))

        review = make_review(findings=[make_finding("f-changelog")])
        plan = {"effective_change_boundary": EFFECTIVE_BOUNDARY}
        reached.update(codes(flow.check_repair_decision(make_final_decision(), review, plan)))
        reached.update(
            codes(
                flow.check_repair_decision(
                    make_repair_decision(candidate_commit=CANDIDATE_C2), review, plan
                )
            )
        )
        reached.update(
            codes(
                flow.check_repair_decision(
                    make_repair_decision(accepted_finding_ids=["f-unknown"]), review, plan
                )
            )
        )
        reached.update(
            codes(
                flow.check_repair_decision(
                    make_repair_decision(write_scope=["elsewhere"]), review, plan
                )
            )
        )

        reached.update(
            codes(flow.check_repair_regeneration(evidence_set(0x100, checks=(dig(1),)), evidence_set(0x100, checks=(dig(1),))))
        )
        reached.update(codes(verify_outcome(make_review())))
        reached.update(
            codes(
                verify_outcome(
                    make_review(
                        result_id="rr-verify",
                        review_round="VERIFY",
                        verdict="SPEC_GAP",
                        candidate_commit=CANDIDATE_C2,
                    )
                )
            )
        )
        reached.update(
            codes(
                verify_outcome(
                    make_review(
                        result_id="rr-verify",
                        review_round="VERIFY",
                        verdict="REVIEWED_NO_BLOCKER",
                        candidate_commit=CANDIDATE_C2,
                        findings=[make_finding("f-changelog")],
                    )
                )
            )
        )

        reached.update(
            codes(summary.check_assurance_candidate(make_candidate(run_id="run-two"), make_record(), [make_review()]))
        )
        reached.update(
            codes(
                summary.check_assurance_candidate(
                    make_candidate(candidate_ref={"branch": "candidate", "commit": CANDIDATE_C2}),
                    make_record(),
                    [make_review()],
                )
            )
        )
        reached.update(
            codes(summary.check_assurance_candidate(make_candidate(repair_round=1), make_record(), [make_review()]))
        )
        reached.update(
            codes(
                summary.check_assurance_candidate(
                    make_candidate(),
                    make_record(),
                    [make_review(findings=[make_finding("f-changelog")])],
                )
            )
        )
        reached.update(
            codes(
                summary.check_assurance_candidate(
                    make_candidate(unresolved_finding_ids=["f-imagined"]), make_record(), [make_review()]
                )
            )
        )
        reached.update(
            codes(
                summary.check_assurance_candidate(
                    make_candidate(unresolved_finding_ids=["f-changelog"]),
                    make_record(),
                    [
                        make_review(findings=[make_finding("f-changelog")]),
                        make_review(
                            result_id="rr-verify",
                            review_round="VERIFY",
                            verdict="REVIEWED_NO_BLOCKER",
                            candidate_commit=CANDIDATE_C2,
                        ),
                    ],
                )
            )
        )

        candidate = make_candidate()
        decision = make_final_decision(candidate=candidate)
        document = make_summary(candidate=candidate, decision=decision)
        altered = dict(document)
        altered["outcome"] = "REJECT"
        reached.update(codes(summary.check_summary(altered, candidate, decision)))
        embellished = dict(document)
        embellished["limitations"] = ["a limitation the user never acknowledged"]
        reached.update(codes(summary.check_summary(embellished, candidate, decision)))
        reached.update(
            codes(summary.check_summary(document, make_candidate(assurance_candidate_id="ac-two"), decision))
        )
        reached.update(codes(summary.check_summary(document, candidate, make_repair_decision())))

        declined_elsewhere = make_repair_decision(decision="NO_REPAIR")
        declined_elsewhere["run_id"] = "run-two"
        reached.update(codes(flow.check_repair_decision(declined_elsewhere, review, plan)))
        other_work = make_repair_decision()
        other_work["work_id"] = "other-work"
        reached.update(codes(flow.check_repair_decision(other_work, review, plan)))
        reached.update(
            codes(
                summary.check_assurance_candidate(
                    make_candidate(review_refs=[ref("control/review-full.json", 0x99)]),
                    make_record(),
                    [make_review()],
                )
            )
        )
        repointed = dict(document)
        repointed["final_decision_ref"] = ref("control/final-decision.json", 0x99)
        reached.update(codes(summary.check_summary(repointed, candidate, decision)))

        reached.update(codes(issues.check_issue(make_issue())))
        reached.update(codes(issues.check_issue(make_issue(), make_state("REVIEWED"))))
        reached.update(codes(issues.check_issue(make_issue(observed_after="STOPPED_REPLAN"), make_state("CLOSED"))))
        mismatched = make_state("CLOSED")
        mismatched["run_id"] = "run-two"
        reached.update(codes(issues.check_issue(make_issue(), mismatched)))
        reached.update(codes(issues.check_triage(make_final_decision(), make_issue())))
        reached.update(codes(issues.check_triage(make_triage(work_id="other-work"), make_issue())))
        reached.update(
            codes(issues.check_triage(make_triage(issue_path="control/hi-two.json"), make_issue()))
        )
        cross_run = make_triage()
        cross_run["run_id"] = "run-two"
        reached.update(codes(issues.check_triage(cross_run, make_issue())))

        expected = {
            "V3-FLOW-TERMINAL",
            "V3-FLOW-ILLEGAL-TRANSITION",
            "V3-FLOW-SECOND-REPAIR",
            "V3-FLOW-POINTER-REQUIRED",
            "V3-FLOW-POINTER-PREMATURE",
            "V3-FLOW-STOP-WITHOUT-REASON",
            "V3-FLOW-REPAIR-WITHOUT-AUTHORIZATION",
            "V3-FLOW-PHASE",
            "V3-FLOW-REPAIR-WRONG-CANDIDATE",
            "V3-FLOW-REPAIR-RUN-MISMATCH",
            "V3-FLOW-REPAIR-WORK-MISMATCH",
            "V3-FLOW-ACCEPTED-FINDING-UNKNOWN",
            "V3-FLOW-REPAIR-BOUNDARY-WIDENS",
            "V3-FLOW-EVIDENCE-NOT-REGENERATED",
            "V3-FLOW-CHECKS-NOT-RERUN",
            "V3-FLOW-NOT-VERIFY",
            "V3-FLOW-VERIFY-SPEC-GAP",
            "V3-FLOW-BLOCKER-AFTER-VERIFY",
            "V3-ASSURANCE-RUN-MISMATCH",
            "V3-ASSURANCE-WRONG-CANDIDATE",
            "V3-ASSURANCE-ROUND-MISMATCH",
            "V3-ASSURANCE-BLOCKER-DROPPED",
            "V3-ASSURANCE-BLOCKER-INVENTED",
            "V3-ASSURANCE-REVIEW-BINDING-INCOMPLETE",
            "V3-ASSURANCE-REVIEW-UNBOUND",
            "V3-ASSURANCE-REVIEW-INVENTED",
            "V3-ASSURANCE-DECISION-BINDING-MISMATCH",
            "V3-ASSURANCE-OUTCOME-ALTERED",
            "V3-ASSURANCE-LIMITATIONS-ALTERED",
            "V3-ASSURANCE-CANDIDATE-BINDING-MISMATCH",
            "V3-ASSURANCE-NOT-FINAL",
            "V3-HARNESS-ISSUE-RUN-STATE-UNVERIFIED",
            "V3-HARNESS-ISSUE-RUN-STILL-LIVE",
            "V3-HARNESS-ISSUE-TERMINAL-STATUS-MISMATCH",
            "V3-HARNESS-ISSUE-RUN-MISMATCH",
            "V3-HARNESS-ISSUE-PHASE",
            "V3-HARNESS-ISSUE-WORK-MISMATCH",
            "V3-HARNESS-ISSUE-TARGET-MISMATCH",
            "V3-HARNESS-ISSUE-TRIAGE-RUN-MISMATCH",
        }
        self.assertEqual(sorted(expected - reached), [])


# ---------------------------------------------------------------------------
# Defect records
# ---------------------------------------------------------------------------


class KnownDefects(unittest.TestCase):
    """Properties this matrix expected to hold and found do not.

    Each method below began as an `@unittest.expectedFailure` record and states the property the
    contract, the acceptance ID or the implementation's own docstring claims. The assertion
    inside is the **correct** one — these are defect records, not accepted behaviour. When a
    defect is fixed the method becomes an unexpected success and this suite reports failure,
    which is the signal to delete the marker, never the assertion.
    """

    def test_the_final_decisions_target_must_be_the_candidate_the_summary_terminates(self) -> None:
        """FIXED during this node (was a real defect): the user's FINAL target is never compared to anything.

        `check_summary` receives the summary, the candidate and the user's FINAL decision, and
        binds the first two together by digest — but never reads
        `decision["target"]["assurance_candidate_ref"]`. So a summary can faithfully terminate
        candidate A while the decision it cites was made about candidate B, and every digest in
        the document still verifies. That is the "check candidate A, report candidate B" class
        (V3-D5) arriving at the one step where the user is the trust terminal: what the user
        decided about and what was closed are different documents, and nothing says so.
        """
        candidate = make_candidate()
        other = make_candidate(assurance_candidate_id="ac-two")
        self.assertNotEqual(summary.candidate_digest(candidate), summary.candidate_digest(other))

        # The user decided about `other`; the controller terminates `candidate`.
        decision = make_final_decision(candidate=other, decision="ACCEPT")
        document = summary.generate_summary(
            summary_id="sum-one",
            candidate=candidate,
            candidate_ref={
                "path": "control/assurance-candidate.json",
                "digest_sha256": summary.candidate_digest(candidate),
            },
            decision=decision,
            decision_ref={
                "path": "control/final-decision.json",
                "digest_sha256": flow.decision_digest(decision),
            },
            promotion=summary.promoted_to(
                {"branch": "main", "commit": CANDIDATE_C}, "the user accepted and promoted"
            ),
            generated_by=CONTROLLER,
        )
        self.assertNotEqual(
            codes(summary.check_summary(document, candidate, decision)),
            [],
            "a summary terminating a candidate the FINAL decision never named must be refused",
        )

    def test_a_repair_boundary_is_checked_even_when_the_plan_omits_its_boundary(self) -> None:
        """FIXED during this node (was a real defect): an absent plan field silently disables the guard.

        `check_repair_decision` reads `plan.get("effective_change_boundary") or {}` and never
        validates the plan, so a plan-shaped mapping without that field turns the
        boundary-widening check off and the function reports clean. This is the fail-open shape
        the module elsewhere refuses to take: `check_issue(state=None)` reports
        `V3-HARNESS-ISSUE-RUN-STATE-UNVERIFIED` rather than staying silent, and
        `check_package` reports `V3-PACKAGE-RECORD-CANDIDATE-UNBOUND` for the same reason.
        Fixed inside V3-N2 — the widest possible repair boundary no longer passes silently.
        """
        review = make_review(findings=[make_finding("f-changelog")])
        decision = make_repair_decision(write_scope=["ResearchSystem/tooling"])
        self.assertNotEqual(
            codes(flow.check_repair_decision(decision, review, {})),
            [],
            "an unverifiable boundary is an unverified property, not a satisfied one",
        )

    def test_every_pointer_is_guarded_against_appearing_before_its_own_stage(self) -> None:
        """FIXED during this node (was a real defect): only three of the twelve pointers are guarded.

        `flow.py`'s own docstring states the rule generally — "a status must **not** carry a
        pointer from a stage it has not reached ... a document that precedes the thing it
        binds is bound to nothing" — but `_EARLIEST_POINTER` lists only
        `assurance_candidate_ref`, `final_decision_ref` and `summary_ref`. Every earlier
        pointer may appear at any status: a `review_ref` at `AUDITED` names a review of a
        candidate the executor has not written yet, and it is reported clean. The
        required-pointer direction of N0-R2 is complete; this direction covers the last three
        stages only.
        """
        impossible = (
            ("AUDITED", "review_ref"),
            ("EXECUTING", "review_ref"),
            ("RESOLVED", "fulfillment_ref"),
            ("RESOLVED", "manifest_ref"),
            ("RESOLVED", "coverage_ref"),
            ("AUDITED", "repair_decision_ref"),
        )
        unguarded: list[tuple[str, str]] = []
        for status, field in impossible:
            state = make_state(status)
            state[field] = {"path": POINTER_PATHS[field]}
            self.assertEqual(codes(validate("state", state)), [], f"{status}/{field} fixture")
            if "V3-FLOW-POINTER-PREMATURE" not in codes(flow.check_state_pointers(state)):
                unguarded.append((status, field))
        self.assertEqual(unguarded, [])

    def test_a_wrongly_typed_promotion_is_reported_rather_than_raised(self) -> None:
        """FIXED during this node (was a real defect): `check_summary` raises instead of returning a Report.

        The promotion guards were deliberately moved ahead of the schema gate so that a
        promotion-after-refusal reports its own reason instead of a generic schema error, and
        the accompanying comment states "Accessors are defensive because this runs before the
        shape is known". They are defensive against a *missing* `promotion` only:
        `summary.get("promotion") or {}` yields the value itself when it is a non-empty string,
        and the next `.get` raises `AttributeError`. So the one document class this reorder
        exists to serve — a summary whose shape is not yet known — is also the one that can
        crash the checker before the schema ever names the problem.
        """
        candidate = make_candidate()
        decision = make_final_decision(candidate=candidate)
        document = dict(make_summary(candidate=candidate, decision=decision))
        document["promotion"] = "promoted to main"
        self.assertEqual(
            codes(summary.check_summary(document, candidate, decision)),
            ["V3-SCHEMA-ASSURANCE_SUMMARY"],
        )


if __name__ == "__main__":
    unittest.main()
