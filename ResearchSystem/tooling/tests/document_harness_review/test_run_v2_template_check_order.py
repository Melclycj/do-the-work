#!/usr/bin/env python3
"""`HD-25` — the evidence template runs the plan's `check_order` through `run_all`.

Two properties, one defect class each (`E7`):

1. **The order is the plan's, never the filenames'.** What this replaces walked
   ``sorted(glob("check-chk-*.json"))``. Filename order and plan order agree by accident on
   every run built so far, so the defect is invisible until they disagree — the fixtures below
   make them disagree on purpose.
2. **A `SPEC_GAP` stops the pass at that check.** The old shape collected the ruling and ran
   every later check anyway, `command_exit` among them, which starts a real process against
   real files under a plan already known to be uninterpretable. The property is *nothing after
   it ran*, which no assertion about the printed summary can express — so the assertion is on
   the sequence of requests that reached `run_check`.

Every expectation is a hand-written literal, never imported from the template or from
`checks.py` (`E5`), and the sequences are asserted whole rather than by membership.

`C.run_check` is replaced (not wrapped) so the real `run_all` still drives the loop under test
while the fixture needs no repository: `run_all` reads only ``result["result"]``, and what the
oracles would do with a real tree is a different module's tested business. `cand.observe_manifest`
is stubbed for the same reason the sibling suite stubs it — it is the first thing past the loop
that needs real Git history.
"""
from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import pathlib
import shutil
import sys
import tempfile
import unittest
from unittest import mock

import _harness  # noqa: F401 — installs the tooling import path the template needs

TEMPLATE_PATH: pathlib.Path = (
    _harness.RS_ROOT / "assurance" / "templates" / "run-v2" / "run_evidence_v2.py"
)


def load_template():
    """Bind the template file directly; never by adding its directory to sys.path."""
    if not TEMPLATE_PATH.is_file():
        raise RuntimeError(f"the v2 evidence template is missing at {TEMPLATE_PATH}")
    spec = importlib.util.spec_from_file_location("v2_evidence_template_order", TEMPLATE_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules.setdefault("v2_evidence_template_order", module)
    spec.loader.exec_module(module)
    return module


#: Filename sort would give alpha, beta, gamma. The plan orders them gamma, alpha, beta — so a
#: run that reports this order can only have read the plan. Hand-written here (`E5`).
PLAN_ORDER = ["chk-gamma", "chk-alpha", "chk-beta"]
FILENAME_ORDER = ["chk-alpha", "chk-beta", "chk-gamma"]

FAKE_MANIFEST = {
    "authored_by": "x", "boundary_result": "CONFORMANT", "expected_artifact_results": [],
}

#: The refusal line the uninterpretable-request path prints, hand-written (`E5`). Asserted as a
#: WHOLE LINE rather than by searching for "STOP:" — this fixture's synthetic record is
#: schema-invalid by construction, so the template's own end-of-pass "evidence not clean" STOP
#: also appears in the output and a substring match on "STOP:" would be satisfied by it. That
#: is the false-negative the first draft of this file walked into.
GAP_REFUSAL = ("      the check request is uninterpretable, so nothing after it ran; "
               "nothing committed, state not advanced")


class EvidenceRunFixture(unittest.TestCase):
    """A run at the real nested depth, carrying three check requests and no obligations.

    Zero obligations on purpose: the fulfillment refusal (the sibling suite's subject) then
    passes vacuously, so nothing here proves or depends on it.
    """

    def setUp(self):
        self.template = load_template()
        root = pathlib.Path(tempfile.mkdtemp(prefix="v2-evidence-order-"))
        self.addCleanup(shutil.rmtree, root, ignore_errors=True)
        self.run_id = "tr-order"
        self.run_dir = root / "ResearchSystem" / "assurance" / "runs" / self.run_id
        self.control = self.run_dir / "control"
        self.control.mkdir(parents=True)
        (self.control / "work-spec.json").write_text(
            json.dumps({"work_id": "w-order", "obligations": [], "expected_artifacts": []}),
            encoding="utf-8")
        (self.control / "resolved-plan.json").write_text(
            json.dumps({
                "check_order": PLAN_ORDER,
                "effective_change_boundary": {"write_scope": [], "out": []},
            }),
            encoding="utf-8")
        (self.control / "state.json").write_text(
            json.dumps({
                "work_id": "w-order", "run_id": self.run_id, "status": "EXECUTING",
                "repair_round": 0,
                "work_spec_ref": {
                    "path": f"ResearchSystem/assurance/runs/{self.run_id}/control/work-spec.json"},
                "resolved_plan_ref": {
                    "path": f"ResearchSystem/assurance/runs/{self.run_id}/control/"
                            "resolved-plan.json"},
            }),
            encoding="utf-8")
        for check_id in FILENAME_ORDER:
            (self.control / f"check-{check_id}.json").write_text(
                json.dumps({"check_id": check_id, "kind": "file_exists",
                            "subject_tree": "candidate_commit", "config": {}}),
                encoding="utf-8")

    def drive(self, gap_at: str | None = None) -> tuple[int | None, list[str], str]:
        """Run `main`, returning (exit code or None, the ids that reached `run_check`, stdout).

        `None` for the code means `main` ran past the loop and died downstream — that is the
        negative-control shape, not a failure of the property under test.
        """
        seen: list[str] = []

        def fake_run_check(check, ctx):
            seen.append(check["check_id"])
            outcome = "SPEC_GAP" if check["check_id"] == gap_at else "PASS"
            return {"check_id": check["check_id"], "result": outcome, "detail": None}

        captured = io.StringIO()
        code: int | None = None
        with mock.patch.object(self.template.C, "run_check", side_effect=fake_run_check), \
                mock.patch.object(self.template.cand, "observe_manifest",
                                  return_value=FAKE_MANIFEST):
            with contextlib.redirect_stdout(captured):
                try:
                    code = self.template.main([
                        str(self.run_dir),
                        "--base", "b" * 40,
                        "--candidate", "c" * 40,
                        "--candidate-branch", f"run/{self.run_id}-candidate",
                    ])
                except Exception:
                    code = None
        return code, seen, captured.getvalue()


class TheOrderIsThePlansNotTheFilenames(EvidenceRunFixture):
    """Property 1. Mutation this kills: restoring `sorted(glob(...))` as the order source."""

    def test_checks_run_in_the_plans_check_order(self):
        _, seen, output = self.drive()
        self.assertEqual(seen, ["chk-gamma", "chk-alpha", "chk-beta"], output)

    def test_the_filename_sort_is_not_the_order(self):
        """Stated as its own assertion so the failure message names the defect, not a diff.

        The literal below is the order the replaced code produced. It is written out rather
        than computed so that a future edit to `PLAN_ORDER` cannot quietly make the two agree
        again and turn this suite vacuous.
        """
        _, seen, output = self.drive()
        self.assertNotEqual(seen, ["chk-alpha", "chk-beta", "chk-gamma"], output)


class ASpecGapStopsThePassAtThatCheck(EvidenceRunFixture):
    """Property 2. Mutation this kills: collecting the gap and finishing the order."""

    def test_no_check_after_the_gap_is_executed(self):
        code, seen, output = self.drive(gap_at="chk-alpha")
        self.assertEqual(seen, ["chk-gamma", "chk-alpha"], output)
        self.assertEqual(code, 1, output)

    def test_the_refusal_names_the_uninterpretable_request(self):
        _, _, output = self.drive(gap_at="chk-alpha")
        self.assertIn("STOP:", output)
        self.assertIn("chk-alpha", output)
        self.assertIn(GAP_REFUSAL, output.splitlines(), output)

    def test_a_gap_on_the_first_check_runs_nothing_else_at_all(self):
        """The boundary case: the stop is at the gap, not one check later."""
        code, seen, output = self.drive(gap_at="chk-gamma")
        self.assertEqual(seen, ["chk-gamma"], output)
        self.assertEqual(code, 1, output)

    def test_a_request_the_plan_orders_but_the_control_root_lacks_is_refused(self):
        """The other `run_all` stop: `-MISSING-REQUEST`, not a silently shorter run."""
        (self.control / "check-chk-beta.json").unlink()
        code, seen, output = self.drive()
        self.assertEqual(seen, ["chk-gamma", "chk-alpha"], output)
        self.assertEqual(code, 1, output)
        self.assertIn("chk-beta", output)


class APlanWithNoCheckOrderRunsNoChecksAndDoesNotCrash(EvidenceRunFixture):
    """`resolved-assurance-plan.schema.json` makes `check_order` OPTIONAL — "absent when the
    run has no deterministic checks". Subscripting it instead of `.get`ing it crashes exactly
    the runs the schema calls legal, and it does so *after* the fulfillment guard, i.e. on a
    run that has already been accepted. Found by this round: `plan["check_order"]` broke the
    sibling suite's `deriv-bind` fixture, whose plan omits the field precisely because it
    declares no checks.

    Stray `check-chk-*.json` files stay on disk here on purpose: absent order means the run
    declares no checks, and `check_subject` re-derives its expected set from the same field,
    so a file no order names was never required and must not run.
    """

    def test_no_order_means_no_check_runs(self):
        (self.control / "resolved-plan.json").write_text(
            json.dumps({"effective_change_boundary": {"write_scope": [], "out": []}}),
            encoding="utf-8")
        code, seen, output = self.drive()
        # The line below is the whole test. `seen == []` and the absent refusal are BOTH
        # satisfied by the defect itself: `drive()` collapses every exception into
        # `code = None`, and a crash at `plan["check_order"]` produces exactly an empty
        # `seen` and no refusal line — so the first draft of this class passed 8/8 under the
        # subscript form and guarded nothing (FULL `e9166d2` `B-1`). This literal is printed
        # only AFTER the loop returns, so it cannot be reached by a run that crashed on the
        # way in. Asserted as a whole line against a hand-written literal (`E5`).
        self.assertIn("deterministic checks : 0/0 PASS", output.splitlines(), output)
        self.assertEqual(seen, [], output)
        self.assertNotIn(GAP_REFUSAL, output.splitlines(), output)


class EveryCheckStillRunsWhenNoneIsUninterpretable(EvidenceRunFixture):
    """Negative control (`E4`): the stop must not fire on a clean pass.

    Paired with the must-fire assertions above so a template edit that broke everything is
    told apart from one that broke only what `HD-25` targets. `main` goes on to real Git work
    the fixture does not provide, so `None` here pins that it got PAST the loop.
    """

    def test_all_three_run_and_nothing_stops(self):
        code, seen, output = self.drive()
        self.assertEqual(seen, ["chk-gamma", "chk-alpha", "chk-beta"], output)
        self.assertIsNone(code, output)
        self.assertNotIn(GAP_REFUSAL, output.splitlines(), output)


if __name__ == "__main__":
    raise SystemExit(unittest.main(argv=[sys.argv[0]]))
