#!/usr/bin/env python3
"""The `E4`-inverse suite: never trust a disposition you have not seen REACHED.

`E4` says never trust a guard you have not seen fail, and this batch's spine is its inverse.
Batch `PROMISE-PATH` exists because the rule layer named dispositions the engine had no path
to, and two of the caller's real runs stopped on that class — each stop cost a full successor
run. A rule that promises an outcome the engine cannot produce is not a documentation defect:
it is a promise the user is invited to rely on and cannot.

**The table below is the guard, and it is hand-written (`E5`).** Every row names a disposition
the rule layer names, where the rules name it, and one of two things: the reacher that drives
the real engine to it, or `no-path` plus the rule site whose own text carries the absence. The
expectations are literals here; the SOURCE they are checked against is the committed schema
pack, read at run time. Neither side is derived from `flow.py`'s own constants, so this file
cannot assert that the code equals itself.

Four properties, and the third is the one the batch is for:

1. every disposition the schemas enumerate has a row — a future rule promising a new one meets
   a red test until the engine or the table answers it;
2. no row names a disposition the schemas do not — a typo'd row is not silent coverage;
3. every `path` row is REACHED, by running the real engine and reading back what it produced;
4. every `no-path` row's named rule site really carries the absence in its own text.

Properties 1, 2 and 4 are also exercised against synthetic tables, because the `no-path` branch
has no real row today: a branch nothing runs is a branch nobody has seen work, which is the
same defect in the guard that the guard exists to find in the engine.

The one stand-in is `review_result_v2.check_review_result_v2` where a bind is driven: its real
form needs a git repository holding the evidence commit, and which DISPOSITION the step
produces is a property of the step alone. Everything else — the flow controller, the summary
generator and their checks — is real.

Offline and deterministic: every repository is a fresh temporary directory, and nothing here
writes into the repository under assurance.
"""
from __future__ import annotations

import contextlib
import dataclasses
import importlib.util
import io
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

import _harness  # noqa: F401 — installs the tooling and V3-N1 mechanism import paths

from rsclib.document_harness import SCHEMA_DIR, canonical_digest, load_json  # noqa: E402
from rsclib.document_harness import flow, summary  # noqa: E402

TEMPLATE_PATH: pathlib.Path = (
    _harness.RS_ROOT / "assurance" / "templates" / "run-v2" / "run_bind_v2.py"
)
RULES = _harness.RS_ROOT / "document-harness" / "RULES.md"


# ---------------------------------------------------------------------------
# The table. One row per disposition the rule layer names.
# ---------------------------------------------------------------------------


@dataclasses.dataclass(frozen=True)
class Row:
    """One disposition, and how this suite answers for it.

    `key` is `<family>:<value>` for the three enumerated families and a bare name for the
    dispositions the rules name in prose. `reacher` is the name of a method on
    `Reachers`; `no-path` instead requires `absence_site` and `absence_text`, and the site's
    bytes must contain that text.
    """

    key: str
    named_by: str
    reacher: str
    absence_site: str = ""
    absence_text: str = ""


TABLE: tuple[Row, ...] = (
    Row(
        key="final:ACCEPT",
        named_by="user-decision.schema.json FINAL branch; assurance.schema.json "
                 "assuranceSummary.outcome",
        reacher="final_accept",
    ),
    Row(
        key="final:ACCEPT_WITH_LIMITATIONS",
        named_by="user-decision.schema.json FINAL branch; assurance.schema.json "
                 "assuranceSummary.outcome (limitations required)",
        reacher="final_accept_with_limitations",
    ),
    Row(
        key="final:REJECT",
        named_by="user-decision.schema.json FINAL branch; invariant 13 forbids promotion",
        reacher="final_reject",
    ),
    Row(
        key="final:REPLAN",
        named_by="user-decision.schema.json FINAL branch; invariant 13 forbids promotion",
        reacher="final_replan",
    ),
    Row(
        key="full-verdict:REVIEWED_NO_BLOCKER",
        named_by="review.v2.schema.json verdict enum; RULES.md R3 FULL row",
        reacher="full_clean_binds_the_candidate",
    ),
    Row(
        key="full-verdict:CHANGES_REQUIRED",
        named_by="review.v2.schema.json verdict enum; RULES.md R3 FULL row",
        reacher="full_changes_required_stops_at_reviewed",
    ),
    Row(
        key="full-verdict:SPEC_GAP",
        named_by="review.v2.schema.json verdict enum; RULES.md R3 FULL row",
        reacher="full_spec_gap_stops_at_reviewed",
    ),
    Row(
        key="verify-verdict:REVIEWED_NO_BLOCKER",
        named_by="review.v2.schema.json VERIFY narrowing; RULES.md R3 VERIFY row",
        reacher="verify_clean",
    ),
    Row(
        key="verify-verdict:SPEC_GAP",
        named_by="review.v2.schema.json VERIFY narrowing; RULES.md R3 VERIFY row",
        reacher="verify_spec_gap",
    ),
    Row(
        key="STOPPED_REPLAN",
        named_by="contract §8 status set; flow._SUCCESSORS reaches it from every "
                 "pre-terminal status",
        reacher="stopped_replan",
    ),
    Row(
        key="repair-leg-after-CHANGES_REQUIRED",
        named_by="RULES.md E9 (one user-approved fix); EXECUTION.md, After a review",
        reacher="repair_leg_after_changes_required",
    ),
    Row(
        key="repair-leg-after-REVIEWED_NO_BLOCKER",
        named_by="RULES.md R10: a FULL returning REVIEWED_NO_BLOCKER with lows does not "
                 "bank them by default",
        reacher="repair_leg_after_a_clean_full",
    ),
    Row(
        key="ACCEPT_WITH_LIMITATIONS-from-residual-uncertainty",
        named_by="REVIEW.md: residual_uncertainty reaches the user at FINAL, where they may "
                 "convert it to ACCEPT_WITH_LIMITATIONS",
        reacher="residual_uncertainty_converted_at_final",
    ),
)


# ---------------------------------------------------------------------------
# The source the table is checked against: the committed schema pack.
# ---------------------------------------------------------------------------


def enumerated() -> dict[str, tuple[str, ...]]:
    """Every disposition the schema pack ENUMERATES, by family.

    Read from the committed files rather than from any module's constants: the schemas are
    what a rule change would touch, and a table checked against `flow.py` would agree with
    the engine by construction.
    """
    decision = load_json(SCHEMA_DIR / "user-decision.schema.json")
    review = load_json(SCHEMA_DIR / "review.v2.schema.json")
    final_branch = next(
        rule for rule in decision["allOf"]
        if rule["if"].get("properties", {}).get("phase", {}).get("const") == "FINAL"
    )
    verify_branch = next(
        rule for rule in review["allOf"]
        if rule["if"].get("properties", {}).get("review_round", {}).get("const") == "VERIFY"
    )
    return {
        "final": tuple(final_branch["then"]["properties"]["decision"]["enum"]),
        "full-verdict": tuple(review["properties"]["verdict"]["enum"]),
        "verify-verdict": tuple(verify_branch["then"]["properties"]["verdict"]["enum"]),
    }


def missing_rows(table, families) -> list[str]:
    """Enumerated dispositions with no row. The guard's first half."""
    keyed = {row.key for row in table}
    return sorted(
        f"{family}:{value}"
        for family, values in families.items()
        for value in values
        if f"{family}:{value}" not in keyed
    )


def unknown_rows(table, families) -> list[str]:
    """Rows in an enumerated family naming a value the schemas do not. The second half."""
    known = {f"{family}:{value}" for family, values in families.items() for value in values}
    return sorted(
        row.key for row in table
        if row.key.split(":", 1)[0] in families and row.key not in known
    )


def unrecorded_absences(table, read_site) -> list[str]:
    """`no-path` rows whose named rule site does not carry the absence in its own text.

    A row that says "the engine cannot reach this" and points at a rule site silent about it
    leaves the promise standing where a reader meets it, which is the whole defect class.
    """
    faults = []
    for row in table:
        if row.reacher != "no-path":
            continue
        if not row.absence_site or not row.absence_text:
            faults.append(f"{row.key}: a no-path row names no site or no absence text")
            continue
        if row.absence_text not in read_site(row.absence_site):
            faults.append(f"{row.key}: {row.absence_site} does not record the absence")
    return faults


# ---------------------------------------------------------------------------
# Fixtures. Hand-written, and never read back from the thing under test.
# ---------------------------------------------------------------------------

CONTROL_ROOT = "ResearchSystem/assurance/runs/tr-reach"
RUN_ID = "tr-reach"
WORK_ID = "w-reach"
CANDIDATE = "c" * 40
BASE = "d" * 40
EVIDENCE_COMMIT = "e" * 40
BOUND_AT = "2026-09-02"

WORK_SPEC = {"work_id": WORK_ID}
RESOLVED_PLAN = {
    "note": "reachability fixture",
    "effective_change_boundary": {"write_scope": ["docs"], "out": ["docs/private"]},
}
AUDIT = {"note": "reachability audit stand-in"}
RECORD = {
    "run_id": RUN_ID,
    "candidate_ref": {"branch": f"run/{RUN_ID}", "commit": CANDIDATE},
    "base_revision": BASE,
    "repair_round": 0,
}
CHECK_RESULT = {"check_id": "chk-one", "result": "PASS"}
DECLARATIONS = {
    "governance_scan": {
        "included": False,
        "skip_reason": "no governance document in this reachability fixture",
    },
    "disclosures": [],
}
LOW = {
    "finding_id": "f-style",
    "blocking": False,
    "statement": "two headings use different capitalisation",
}
BLOCKER = {
    "finding_id": "f-changelog",
    "blocking": True,
    "statement": "the changelog does not name the release the instruction froze",
    "candidate_locator": {"path": "docs/changelog.md", "anchor": "## 1.2.0"},
    "ground_truth_locator": {"path": "docs/instruction.md", "anchor": "## release"},
    "minimum_fix": "name the release the instruction froze",
}
RESIDUAL = "whether the tone requirement was met is a judgment the frozen subjects cannot settle"


def review(*, verdict, round_="FULL", findings=(), residual=(), scope=None):
    """One whole v2 ReviewResult, hand-written. Every field the schema requires is here."""
    disposition = {"obligation_id": "ob-one", "disposition": "SUPPORTED"}
    if any(finding["blocking"] for finding in findings):
        disposition = {
            "obligation_id": "ob-one",
            "disposition": "NOT_SUPPORTED",
            "note": "the frozen subjects contradict the fulfillment claim",
            "finding_ids": [f["finding_id"] for f in findings if f["blocking"]],
        }
    document = {
        "schema_version": "2",
        "result_id": f"rr-{round_.lower()}",
        "work_id": WORK_ID,
        "run_id": RUN_ID,
        "review_round": round_,
        "subject": {
            "evidence_commit": EVIDENCE_COMMIT,
            "candidate_ref": {"branch": f"run/{RUN_ID}", "commit": CANDIDATE},
            "base_revision": BASE,
            "control_root": CONTROL_ROOT,
            "repair_round": 0 if round_ == "FULL" else 1,
        },
        "verdict": verdict,
        "instruction_completeness": {
            "result": "COMPLETE",
            "instruction_ref": {"path": f"{CONTROL_ROOT}/instruction.md", "revision": BASE},
        },
        "per_obligation_disposition": [disposition],
        "residual_uncertainty": list(residual),
        "reviewed_by": "independent reviewer",
    }
    if findings:
        document["findings"] = list(findings)
    if scope is not None:
        document["verify_scope"] = scope
    return document


def repair_decision(*, decision, accepted=("f-style",)):
    target = {"candidate_ref": {"branch": f"run/{RUN_ID}", "commit": CANDIDATE}}
    if decision == "APPLY_ACCEPTED_FINDINGS":
        target["accepted_finding_ids"] = list(accepted)
        target["repair_boundary"] = {"write_scope": ["docs"], "out": ["docs/private"]}
    return {
        "decision_id": "ud-repair",
        "work_id": WORK_ID,
        "run_id": RUN_ID,
        "phase": "REPAIR",
        "decision": decision,
        "target": target,
        "decided_by": "Melclycj (user)",
        "decided_at": BOUND_AT,
    }


def state(status, **overrides):
    """A schema-valid AssuranceWorkState carrying what `status` requires."""
    document = {
        "work_id": WORK_ID,
        "run_id": RUN_ID,
        "status": status,
        "repair_round": 0,
        "work_spec_ref": {"path": f"{CONTROL_ROOT}/control/work-spec.json"},
        "resolved_plan_ref": {"path": f"{CONTROL_ROOT}/control/resolved-plan.json"},
    }
    if status in ("EVIDENCED", "REVIEWED"):
        document.update({
            "instruction_audit_ref": {"path": f"{CONTROL_ROOT}/control/instruction-audit.json"},
            "start_decision_ref": {"path": f"{CONTROL_ROOT}/control/user-decision-start.json"},
            "fulfillment_ref": {"path": f"{CONTROL_ROOT}/evidence/candidate-record.json"},
            "manifest_ref": {"path": f"{CONTROL_ROOT}/evidence/candidate-record.json"},
            "coverage_ref": {"path": f"{CONTROL_ROOT}/evidence/coverage.json"},
        })
    if status == "REVIEWED":
        document["review_ref"] = {"path": f"{CONTROL_ROOT}/evidence/review-full.json"}
    document.update(overrides)
    return document


def candidate_document():
    """The AssuranceCandidate a FINAL decision is taken against, assembled by the real binder."""
    return summary.bind_candidate(
        assurance_candidate_id=f"ac-{RUN_ID}",
        work_id=WORK_ID,
        run_id=RUN_ID,
        repair_round=0,
        candidate_ref={"branch": f"run/{RUN_ID}", "commit": CANDIDATE},
        base_revision=BASE,
        bound_by=f"{RUN_ID} controller (rsclib deterministic)",
        work_spec_ref={"path": f"{CONTROL_ROOT}/control/work-spec.json",
                       "digest_sha256": "1" * 64},
        resolved_plan_ref={"path": f"{CONTROL_ROOT}/control/resolved-plan.json",
                           "digest_sha256": "2" * 64},
        instruction_audit_ref={"path": f"{CONTROL_ROOT}/control/instruction-audit.json",
                               "digest_sha256": "3" * 64},
        fulfillment_ref={"path": f"{CONTROL_ROOT}/evidence/candidate-record.json",
                         "digest_sha256": "4" * 64},
        manifest_ref={"path": f"{CONTROL_ROOT}/evidence/candidate-record.json",
                      "digest_sha256": "5" * 64},
        coverage_ref={"path": f"{CONTROL_ROOT}/evidence/coverage.json",
                      "digest_sha256": "6" * 64},
        review_refs=[{"path": f"{CONTROL_ROOT}/evidence/review-full.json",
                      "digest_sha256": "7" * 64}],
        governance_scan=DECLARATIONS["governance_scan"],
        bound_at=BOUND_AT,
    )


def final_decision(*, outcome, limitations=()):
    document = {
        "decision_id": "ud-final",
        "work_id": WORK_ID,
        "run_id": RUN_ID,
        "phase": "FINAL",
        "decision": outcome,
        "target": {"assurance_candidate_ref": {
            "path": f"{CONTROL_ROOT}/control/assurance-candidate.json",
            "digest_sha256": canonical_digest(candidate_document()),
        }},
        "decided_by": "Melclycj (user)",
        "decided_at": BOUND_AT,
    }
    if limitations:
        document["limitations"] = list(limitations)
    return document


def load_bind_template():
    """The bind step, bound by explicit file path under a distinct module name."""
    spec = importlib.util.spec_from_file_location("reach_bind_template", TEMPLATE_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules["reach_bind_template"] = module
    spec.loader.exec_module(module)
    return module


class StubResultChecker:
    """The one stand-in: the real checker needs a repository holding the evidence commit."""

    @staticmethod
    def check_review_result_v2(result, repo_root, *, evidence_commit, executor=None):
        from rsclib.document_harness import report_of

        return report_of([])


# ---------------------------------------------------------------------------
# The reachers. Each drives the real engine and RETURNS what it reached.
# ---------------------------------------------------------------------------


class Reachers:
    """One method per `path` row. Each returns the disposition it actually produced.

    Returning it, rather than asserting it, is what makes the table the guard: the test below
    compares the returned value against the row's own key, so a reacher that reached
    something else fails on the VALUE.
    """

    def __init__(self, case: unittest.TestCase):
        self.case = case

    # --- the four FINAL outcomes -------------------------------------------------------

    def _final(self, outcome, limitations=()):
        candidate = candidate_document()
        decision = final_decision(outcome=outcome, limitations=limitations)
        promotion = (
            summary.promoted_to({"branch": "main", "commit": CANDIDATE}, "the user accepted it")
            if outcome == "ACCEPT"
            else summary.no_promotion("the user did not promote in this session")
        )
        document = summary.generate_summary(
            summary_id=f"sum-{RUN_ID}",
            candidate=candidate,
            candidate_ref={"path": f"{CONTROL_ROOT}/control/assurance-candidate.json",
                           "digest_sha256": canonical_digest(candidate)},
            decision=decision,
            decision_ref={"path": f"{CONTROL_ROOT}/control/user-decision-final.json",
                          "digest_sha256": canonical_digest(decision)},
            promotion=promotion,
            generated_by="reachability controller",
        )
        report = summary.check_summary(document, candidate, decision)
        self.case.assertEqual(report.rendered(), [], "the summary the engine produced is refused")
        return document["outcome"], document

    def final_accept(self):
        return self._final("ACCEPT")[0]

    def final_accept_with_limitations(self):
        return self._final("ACCEPT_WITH_LIMITATIONS", limitations=[RESIDUAL])[0]

    def final_reject(self):
        return self._final("REJECT")[0]

    def final_replan(self):
        return self._final("REPLAN")[0]

    def residual_uncertainty_converted_at_final(self):
        """REVIEW.md's conversion: the reviewer's residual becomes the user's limitation.

        The FULL carries the residual as data; the user's FINAL decision carries the same
        sentence as an acknowledged limitation; the summary carries it because
        `check_summary` refuses a summary whose limitations differ from the user's.
        """
        full = review(verdict="REVIEWED_NO_BLOCKER", residual=[RESIDUAL])
        outcome, document = self._final("ACCEPT_WITH_LIMITATIONS", limitations=[RESIDUAL])
        self.case.assertEqual(document["limitations"], full["residual_uncertainty"])
        return "ACCEPT_WITH_LIMITATIONS-from-residual-uncertainty"

    # --- the VERIFY verdicts ------------------------------------------------------------

    def _verify(self, verdict):
        decision = repair_decision(decision="APPLY_ACCEPTED_FINDINGS", accepted=["f-changelog"])
        verify = review(
            verdict=verdict,
            round_="VERIFY",
            scope={
                "accepted_finding_ids": ["f-changelog"],
                "repair_diff_reviewed": True,
                "permanent_boundaries_checked": True,
            },
        )
        return flow.check_verify_outcome(verify, decision)

    def verify_clean(self):
        report = self._verify("REVIEWED_NO_BLOCKER")
        self.case.assertEqual(report.rendered(), [])
        return "REVIEWED_NO_BLOCKER"

    def verify_spec_gap(self):
        report = self._verify("SPEC_GAP")
        self.case.assertEqual(
            [issue.code for issue in report.issues], ["V3-FLOW-VERIFY-SPEC-GAP"])
        return "SPEC_GAP"

    # --- the stop ------------------------------------------------------------------------

    def stopped_replan(self):
        stopped = flow.advance_checked(
            state("REVIEWED"), "STOPPED_REPLAN",
            blockers=["the reviewer's blocking finding was never repaired"],
        )
        return stopped["status"]

    # --- the repair leg, in both FULL outcomes -------------------------------------------

    def repair_leg_after_changes_required(self):
        full = review(verdict="CHANGES_REQUIRED", findings=[BLOCKER])
        decision = repair_decision(
            decision="APPLY_ACCEPTED_FINDINGS", accepted=["f-changelog"])
        gate = flow.check_repair_decision(decision, full, RESOLVED_PLAN)
        self.case.assertEqual(gate.rendered(), [])
        repairing = flow.advance_checked(
            state("REVIEWED"), "REPAIRING",
            repair_decision_ref={"path": f"{CONTROL_ROOT}/control/user-decision-repair.json"},
        )
        self.case.assertEqual(repairing["repair_round"], 1)
        return f"repair-leg-after-{full['verdict']}"

    def repair_leg_after_a_clean_full(self):
        """`R10`, and the path item 3 built: the bind surfaces the choice, the user spends it."""
        full = review(verdict="REVIEWED_NO_BLOCKER", findings=[LOW])
        decision = repair_decision(decision="APPLY_ACCEPTED_FINDINGS")
        root = self.case.make_run(full, repair=decision)
        code, out = self.case.drive_bind(root)
        self.case.assertEqual(code, 0, out)
        self.case.assertIn(
            "lows decision          : APPLY_ACCEPTED_FINDINGS — the leg is spent",
            out.splitlines(),
        )
        self.case.assertEqual(self.case.saved_state(root)["status"], "REVIEWED")
        gate = flow.check_repair_decision(decision, full, RESOLVED_PLAN)
        self.case.assertEqual(gate.rendered(), [])
        repairing = flow.advance_checked(
            state("REVIEWED"), "REPAIRING",
            repair_decision_ref={"path": f"{CONTROL_ROOT}/control/user-decision-repair.json"},
        )
        self.case.assertEqual(repairing["status"], "REPAIRING")
        return f"repair-leg-after-{full['verdict']}"

    # --- the three FULL verdicts, through the step that acts on them ---------------------

    def _bind_verdict(self, verdict, **kwargs):
        full = review(verdict=verdict,
                      findings=[BLOCKER] if verdict == "CHANGES_REQUIRED" else ())
        root = self.case.make_run(full, **kwargs)
        code, out = self.case.drive_bind(root)
        self.case.assertEqual(code, 0, out)
        return out, root

    def full_changes_required_stops_at_reviewed(self):
        out, root = self._bind_verdict("CHANGES_REQUIRED")
        self.case.assertIn(
            "verdict                : CHANGES_REQUIRED — no AssuranceCandidate is bound at "
            "round 0",
            out.splitlines(),
        )
        self.case.assertEqual(self.case.saved_state(root)["status"], "REVIEWED")
        return "CHANGES_REQUIRED"

    def full_spec_gap_stops_at_reviewed(self):
        out, root = self._bind_verdict("SPEC_GAP")
        self.case.assertIn(
            "verdict                : SPEC_GAP — no AssuranceCandidate is bound at round 0",
            out.splitlines(),
        )
        self.case.assertEqual(self.case.saved_state(root)["status"], "REVIEWED")
        return "SPEC_GAP"

    def full_clean_binds_the_candidate(self):
        """The whole clean path: a clean FULL with a low, banked, reaches AWAITING_FINAL."""
        full = review(verdict="REVIEWED_NO_BLOCKER", findings=[LOW])
        root = self.case.make_run(
            full, repair=repair_decision(decision="NO_REPAIR"), evidenced=True)
        code, out = self.case.drive_bind(root)
        self.case.assertEqual(code, 0, out)
        saved = self.case.saved_state(root)
        self.case.assertEqual(saved["status"], "AWAITING_FINAL")
        self.case.assertTrue(
            (root / CONTROL_ROOT / "control" / "assurance-candidate.json").is_file())
        return "REVIEWED_NO_BLOCKER"


# ---------------------------------------------------------------------------
# The suite.
# ---------------------------------------------------------------------------


class DispositionReachability(unittest.TestCase):
    """The four properties, over the real table."""

    def setUp(self):
        self.template = load_bind_template()
        self.template.RV = StubResultChecker

    # --- fixture plumbing for the rows that drive the bind step ------------------------

    def make_run(self, full, *, repair=None, evidenced=False):
        root = pathlib.Path(tempfile.mkdtemp(prefix="reach-"))
        self.addCleanup(shutil.rmtree, root, ignore_errors=True)
        subprocess.run(["git", "-C", str(root), "init", "-q"], check=True,
                       stdout=subprocess.DEVNULL)
        control = root / CONTROL_ROOT / "control"
        evidence = root / CONTROL_ROOT / "evidence"
        control.mkdir(parents=True)
        evidence.mkdir(parents=True)
        (evidence / "review-full.json").write_text(json.dumps(full), encoding="utf-8")
        control_files = {"state.json": state("EVIDENCED"), "resolved-plan.json": RESOLVED_PLAN}
        if repair is not None:
            control_files["user-decision-repair.json"] = repair
        if evidenced:
            control_files["work-spec.json"] = WORK_SPEC
            control_files["instruction-audit.json"] = AUDIT
            control_files["bind-declarations.json"] = DECLARATIONS
            for name, document in (
                ("candidate-record.json", RECORD),
                ("check-results.json", [CHECK_RESULT]),
                ("check-chk-one.json", CHECK_RESULT),
                ("coverage.json", {"rows": []}),
            ):
                (evidence / name).write_text(json.dumps(document), encoding="utf-8")
        for name, document in control_files.items():
            (control / name).write_text(json.dumps(document), encoding="utf-8")
        return root

    def drive_bind(self, root):
        buffer = io.StringIO()
        try:
            with contextlib.redirect_stdout(buffer):
                code = self.template.main([
                    str(root / CONTROL_ROOT),
                    "--evidence-commit", EVIDENCE_COMMIT,
                    "--bound-at", BOUND_AT,
                    "--emit",
                ])
        except Exception:
            return None, buffer.getvalue()
        return code, buffer.getvalue()

    def saved_state(self, root):
        return json.loads(
            (root / CONTROL_ROOT / "control" / "state.json").read_text(encoding="utf-8"))

    # --- property 1 and 2: the table matches what the rule layer enumerates -------------

    def test_every_enumerated_disposition_has_a_row(self):
        self.assertEqual(missing_rows(TABLE, enumerated()), [])

    def test_no_row_names_a_disposition_the_schemas_do_not(self):
        self.assertEqual(unknown_rows(TABLE, enumerated()), [])

    def test_the_enumeration_is_not_vacuous(self):
        """A families map that came back empty would make both guards above pass over nothing."""
        families = enumerated()
        self.assertEqual(
            {family: len(values) for family, values in families.items()},
            {"final": 4, "full-verdict": 3, "verify-verdict": 2},
        )

    # --- property 3: every path row is reached ------------------------------------------

    def test_every_path_row_is_reached_by_the_real_engine(self):
        reachers = Reachers(self)
        for row in TABLE:
            if row.reacher == "no-path":
                continue
            with self.subTest(disposition=row.key):
                method = getattr(reachers, row.reacher, None)
                self.assertIsNotNone(
                    method, f"{row.key} names reacher {row.reacher!r}, which does not exist")
                reached = method()
                expected = row.key.split(":", 1)[1] if ":" in row.key else row.key
                self.assertEqual(
                    reached, expected,
                    f"{row.key}'s reacher produced {reached!r}, not the disposition it claims",
                )

    def test_every_row_is_answered_one_way_or_the_other(self):
        """No third state: a row is reached, or its absence is recorded where the rule is."""
        for row in TABLE:
            with self.subTest(disposition=row.key):
                self.assertTrue(row.named_by, "a row that says nothing about where it is named")
                self.assertTrue(row.reacher, "a row with neither a reacher nor `no-path`")

    # --- property 4: no-path rows carry their absence ------------------------------------

    def test_no_no_path_row_is_left_unrecorded(self):
        self.assertEqual(
            unrecorded_absences(TABLE, lambda site: (_harness.RS_ROOT / site).read_text(
                encoding="utf-8")),
            [],
        )


class TheGuardItselfHasBeenSeenToFail(unittest.TestCase):
    """`E4` applied to this file: each of the three checks, red on synthetic input.

    The `no-path` branch has no real row today, so without this class it would be a branch
    nobody has run — the same defect in the guard that the guard exists to find in the engine.
    Every must-fire case is paired with a negative control.
    """

    FAMILIES = {"final": ("ACCEPT", "REJECT"), "full-verdict": ("SPEC_GAP",)}

    def row(self, key, **kwargs):
        return Row(key=key, named_by="a rule site", reacher="a_reacher", **kwargs)

    def test_a_disposition_the_rules_name_and_the_table_omits_is_reported(self):
        table = (self.row("final:ACCEPT"), self.row("full-verdict:SPEC_GAP"))
        self.assertEqual(missing_rows(table, self.FAMILIES), ["final:REJECT"])

    def test_negative_control_a_complete_table_reports_nothing(self):
        table = (self.row("final:ACCEPT"), self.row("final:REJECT"),
                 self.row("full-verdict:SPEC_GAP"))
        self.assertEqual(missing_rows(table, self.FAMILIES), [])

    def test_a_row_naming_a_disposition_the_rules_do_not_is_reported(self):
        table = (self.row("final:ACCEPT"), self.row("final:INVENTED"))
        self.assertEqual(unknown_rows(table, self.FAMILIES), ["final:INVENTED"])

    def test_negative_control_a_row_outside_the_enumerated_families_is_left_alone(self):
        """The prose-named rows — STOPPED_REPLAN and the repair legs — are not typos."""
        table = (self.row("final:ACCEPT"), self.row("STOPPED_REPLAN"))
        self.assertEqual(unknown_rows(table, self.FAMILIES), [])

    def test_a_no_path_row_whose_rule_site_says_nothing_is_reported(self):
        table = (Row(key="final:REJECT", named_by="a rule site", reacher="no-path",
                     absence_site="RULES.md", absence_text="no engine path exists"),)
        self.assertEqual(
            unrecorded_absences(table, lambda site: "a rule site that says nothing"),
            ["final:REJECT: RULES.md does not record the absence"],
        )

    def test_a_no_path_row_that_names_no_site_is_reported(self):
        table = (Row(key="final:REJECT", named_by="a rule site", reacher="no-path"),)
        self.assertEqual(
            unrecorded_absences(table, lambda site: ""),
            ["final:REJECT: a no-path row names no site or no absence text"],
        )

    def test_negative_control_a_recorded_absence_reports_nothing(self):
        table = (Row(key="final:REJECT", named_by="a rule site", reacher="no-path",
                     absence_site="RULES.md", absence_text="no engine path exists"),)
        self.assertEqual(
            unrecorded_absences(
                table, lambda site: "the engine: no engine path exists for this."),
            [],
        )

    def test_negative_control_a_path_row_is_not_asked_for_an_absence(self):
        table = (self.row("final:ACCEPT"),)
        self.assertEqual(unrecorded_absences(table, lambda site: ""), [])

    def test_the_rules_file_this_suite_cites_is_really_there(self):
        """`R10`'s sentence, read out of the committed rule file rather than paraphrased."""
        self.assertIn(
            "A FULL returning REVIEWED_NO_BLOCKER with\n"
            "  lows does not bank them by default",
            RULES.read_text(encoding="utf-8"),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
