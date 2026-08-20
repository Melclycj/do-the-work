#!/usr/bin/env python3
"""M8 — the v2 evidence template may not author fulfillment status on the executor's behalf.

The defect CLASS (E7), not the one reported line: a run script that *derives* a per-obligation
status makes unfinished work unrepresentable. The shape this guards against wrote
``"status": "IMPLEMENTED"`` for every obligation inside a comprehension, so a complete
obligation list stamped every row done and any enumeration built on it carried no real state —
including the completeness enumeration a later node adds. The property under test is therefore
"status is read from the human-filled map and never supplied by the template, and an obligation
the human never answered for refuses the run", whatever the template's internal spelling.

Every expectation below is a hand-written literal and is never imported from the template (E5):
a test that asked the module for its own answer would pass against any answer. Assertions are
made against the WHOLE returned structure rather than a substring of it.

The template is loaded by explicit file path under a distinct module name — importing it runs
only its module level (its ``main`` is guarded by ``__name__``), and it needs no filesystem.
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
    spec = importlib.util.spec_from_file_location("v2_evidence_template", TEMPLATE_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules.setdefault("v2_evidence_template", module)
    spec.loader.exec_module(module)
    return module


#: Two obligations, hand-written here. The suite never reads the template's own fixtures.
OBLIGATIONS = [
    {"obligation_id": "ob-one", "verification_mode": "local_check"},
    {"obligation_id": "ob-two", "verification_mode": "review_only"},
]

LOCATOR_ONE = {"path": "docs/thing.md", "anchor": "## The Thing"}

#: Since R2 (`HD-11`) the template takes the run directory as an ARGUMENT and derives the
#: repository root from its fourth parent, so the fixtures below build the real shape rather
#: than re-pointing module globals at a flat temp directory.
CONTROL_ROOT = "ResearchSystem/assurance/runs/tr-eight"
#: A schema-shaped state, hand-written (E5). The only field the evidence step reads from it
#: is the round — which is the point: the round is the state's, never the script's.
EVIDENCED_STATE = {
    "work_id": "w-test",
    "run_id": "tr-eight",
    "status": "EXECUTING",
    "repair_round": 0,
    "work_spec_ref": {"path": f"{CONTROL_ROOT}/control/work-spec.json"},
    "resolved_plan_ref": {"path": f"{CONTROL_ROOT}/control/resolved-plan.json"},
}


class TheTemplateNeverSuppliesAStatus(unittest.TestCase):
    """M8: 'the template requires an explicit status per entry; a missing entry is refused'."""

    def setUp(self):
        self.template = load_template()

    # --- the refusal half -------------------------------------------------------------

    def test_an_obligation_with_no_entry_is_refused_and_never_claimed(self):
        """The reported defect: a comprehension over obligations could not express this."""
        claims, unfilled = self.template.build_claims(
            OBLIGATIONS,
            {"ob-one": {"status": "IMPLEMENTED", "implementation_locators": [LOCATOR_ONE]}},
        )
        self.assertEqual(unfilled, ["ob-two"])
        self.assertEqual(
            claims,
            [
                {
                    "obligation_id": "ob-one",
                    "status": "IMPLEMENTED",
                    "implementation_locators": [LOCATOR_ONE],
                }
            ],
        )

    def test_an_entry_that_never_says_which_status_it_is_is_refused(self):
        """'Explicit status' means the word is present, not that some key was filled in."""
        claims, unfilled = self.template.build_claims(
            OBLIGATIONS,
            {
                "ob-one": {"implementation_locators": [LOCATOR_ONE]},  # no status
                "ob-two": {"status": "NOT_IMPLEMENTED", "note": "deferred to C3"},
            },
        )
        self.assertEqual(unfilled, ["ob-one"])
        self.assertEqual(
            claims,
            [{"obligation_id": "ob-two", "status": "NOT_IMPLEMENTED", "note": "deferred to C3"}],
        )

    def test_every_unanswered_obligation_is_named_not_just_the_first(self):
        claims, unfilled = self.template.build_claims(OBLIGATIONS, {})
        self.assertEqual(unfilled, ["ob-one", "ob-two"])
        self.assertEqual(claims, [])

    # --- the honesty half: unfinished work must be representable ----------------------

    def test_not_implemented_survives_the_template_unchanged(self):
        """The property the old shape destroyed: a human's NOT_IMPLEMENTED reaches the record.

        This is the assertion a template that defaults to IMPLEMENTED cannot satisfy, and it
        fails on the VALUE rather than by crashing — which is what makes it binding.
        """
        claims, unfilled = self.template.build_claims(
            OBLIGATIONS,
            {
                "ob-one": {"status": "IMPLEMENTED", "implementation_locators": [LOCATOR_ONE]},
                "ob-two": {"status": "NOT_IMPLEMENTED", "note": "no source found for this"},
            },
        )
        self.assertEqual(unfilled, [])
        self.assertEqual(
            claims,
            [
                {
                    "obligation_id": "ob-one",
                    "status": "IMPLEMENTED",
                    "implementation_locators": [LOCATOR_ONE],
                },
                {
                    "obligation_id": "ob-two",
                    "status": "NOT_IMPLEMENTED",
                    "note": "no source found for this",
                },
            ],
        )

    def test_a_not_implemented_claim_carries_no_locator_key_at_all(self):
        """candidate-record.schema.json forbids locators on NOT_IMPLEMENTED, not merely empties them."""
        claims, _ = self.template.build_claims(
            OBLIGATIONS,
            {
                "ob-one": {"status": "NOT_IMPLEMENTED", "note": "out of this round's scope"},
                "ob-two": {"status": "NOT_IMPLEMENTED", "note": "out of this round's scope"},
            },
        )
        for claim in claims:
            self.assertNotIn("implementation_locators", claim)

    def test_claim_order_follows_the_workspec_not_the_fulfillment_map(self):
        """Coverage rows join on WorkSpec order; a map-ordered claim list would drift from it."""
        claims, unfilled = self.template.build_claims(
            OBLIGATIONS,
            {
                "ob-two": {"status": "NOT_IMPLEMENTED", "note": "written out of order"},
                "ob-one": {"status": "IMPLEMENTED", "implementation_locators": [LOCATOR_ONE]},
            },
        )
        self.assertEqual(unfilled, [])
        self.assertEqual([claim["obligation_id"] for claim in claims], ["ob-one", "ob-two"])


class TheRunIsRefusedNotMerelyReported(unittest.TestCase):
    """M8's wording is 缺条目=**拒绝** — the refusal, not the report of one.

    `build_claims` returning an obligation as unfilled is the INPUT to that decision; the step
    that turns it into a non-zero exit is its own guard. The first version of this file tested
    only the helper, so deleting the four-line refusal from `main()` left it 7/7 green and the
    behaviour the Acceptance quoted was never exercised (FULL a918e37..7572abd, F2).

    `main()` is pointed at a throwaway run directory by ARGUMENT, and the fulfillment map it
    reads is the run's own `control/fulfillment.json` — since R2 there is no module global to
    re-point. Nothing here touches the repository.
    """

    def setUp(self):
        self.template = load_template()
        root = pathlib.Path(tempfile.mkdtemp(prefix="v2-evidence-run-"))
        self.addCleanup(shutil.rmtree, root, ignore_errors=True)
        self.run_dir = root / CONTROL_ROOT
        self.control = self.run_dir / "control"
        self.control.mkdir(parents=True)
        (self.control / "work-spec.json").write_text(
            json.dumps({"obligations": OBLIGATIONS}), encoding="utf-8")
        (self.control / "resolved-plan.json").write_text(
            json.dumps({"effective_change_boundary": {"write_scope": [], "out": []}}),
            encoding="utf-8")
        (self.control / "state.json").write_text(
            json.dumps(EVIDENCED_STATE), encoding="utf-8")

    def write_fulfillment(self, fulfillment) -> None:
        """The executor's map, on disk where the template now reads it.

        Not written at all by the test that pins the absent-file case: an absent map is an
        answered-for-nothing run, and it takes the same refusal as an incomplete one.
        """
        (self.control / "fulfillment.json").write_text(
            json.dumps(fulfillment), encoding="utf-8")

    def run_main(self) -> tuple[int | None, str]:
        """Returns `None` when `main()` ran PAST the guard and died somewhere downstream.

        Caught rather than propagated on purpose. A refusal that has been removed makes
        `main()` continue into checks that need a real repository and raise; letting that
        escape would turn every assertion below into an ERROR, which proves the test reached
        the code but not that it binds the behaviour (R8). Mapped to a value, "not refused"
        fails as `None != 1`.
        """
        captured = io.StringIO()
        try:
            with contextlib.redirect_stdout(captured):
                code = self.template.main([
                    str(self.run_dir),
                    "--base", "b" * 40,
                    "--candidate", "c" * 40,
                    "--candidate-branch", "run/tr-eight-candidate",
                ])
        except Exception:
            return None, captured.getvalue()
        return code, captured.getvalue()

    def test_an_unanswered_obligation_refuses_the_run(self):
        self.write_fulfillment(
            {"ob-one": {"status": "IMPLEMENTED", "implementation_locators": [LOCATOR_ONE]}})
        code, output = self.run_main()
        self.assertEqual(code, 1, output)
        self.assertIn("STOP: no explicit fulfillment status for: ob-two", output)

    def test_the_refusal_names_every_unanswered_obligation(self):
        self.write_fulfillment({})
        code, output = self.run_main()
        self.assertEqual(code, 1, output)
        self.assertIn("STOP: no explicit fulfillment status for: ob-one, ob-two", output)

    def test_an_absent_fulfillment_file_takes_the_same_refusal(self):
        """R2: the map moved from a CONFIG dict to `control/fulfillment.json`.

        A file nobody wrote is not an empty answer that may be defaulted — it is the same
        unanswered run as an empty map, and the refusal names the file so a cold executor
        knows what to write rather than what to edit.
        """
        code, output = self.run_main()
        self.assertEqual(code, 1, output)
        self.assertIn("STOP: no explicit fulfillment status for: ob-one, ob-two", output)
        self.assertIn(
            "      fill control/fulfillment.json for each — this script supplies no "
            "default status",
            output.splitlines(),
        )

    def test_nothing_is_written_before_the_refusal(self):
        """The other half of the claim: refused *before anything is written*."""
        self.write_fulfillment({})
        code, _ = self.run_main()
        self.assertEqual(code, 1)
        evidence = self.run_dir / "evidence"
        self.assertFalse(evidence.exists(), f"the refused run created {evidence}")

    def test_a_complete_map_does_not_trip_the_refusal(self):
        """Negative control: the guard must not fire when every obligation is answered.

        `main()` goes on to real checks that need a repository and stops there — `None` — so
        this pins that it got PAST the guard rather than being refused by it.
        """
        self.write_fulfillment({
            "ob-one": {"status": "IMPLEMENTED", "implementation_locators": [LOCATOR_ONE]},
            "ob-two": {"status": "NOT_IMPLEMENTED", "note": "answered, and answered no"},
        })
        code, output = self.run_main()
        self.assertIsNone(code, output)
        self.assertNotIn("STOP: no explicit fulfillment status", output)


class TheTemplateStillCarriesItsRoundDependentNextAction(unittest.TestCase):
    """Negative control (E4): a property the M8 change must NOT have disturbed.

    Paired with the must-fire assertions above so that a template edit which broke everything
    would be told apart from one that broke only what M8 targets.
    """

    def setUp(self):
        self.template = load_template()

    def test_round_zero_asks_for_a_full_and_a_repair_round_asks_for_a_verify(self):
        self.assertIn("FULL", self.template.next_action_for(0))
        self.assertIn("VERIFY", self.template.next_action_for(1))


class TheEvidenceStepDerivesRepoRootAndControlRootFromRunDir(unittest.TestCase):
    """rider `deriv-bind` (`ResearchSystem/HARNESS-RIDERS.md`): R2 (`HD-11` part one) moved
    REPO and CONTROL_ROOT off two literals a human wrote and a freeze reviewed onto a
    derivation from `run_dir` alone, and the derivation itself shipped with no test.
    `v3-review-full-eec4171.md` L-2 names the two mutations that prove it, both surviving
    the full 649-test battery: M11 (`run_dir.parents[3]` -> `parents[2]`) and M12
    (`CONTROL_ROOT` hard-coded to a different run's name).

    Both properties are observed the same way: a `wraps` spy on `cand.build_record`, whose
    `control_root=` keyword is the derivation's first externally visible trace (set at the
    template's :124, ahead of every Git operation). `cand.observe_manifest` is stubbed out
    so the fixture needs no real Git history at all — only the path arithmetic under test
    has to be real, and everything downstream of the spy is allowed to fail (a bare
    directory is not a Git repository), because the assertions never depend on it.
    """

    def setUp(self):
        self.template = load_template()

    def _run_and_capture_control_root(self, run_id: str) -> str:
        """Build a run at the true nested depth and return the `control_root` build_record saw."""
        root = pathlib.Path(tempfile.mkdtemp(prefix="v2-evidence-deriv-"))
        self.addCleanup(shutil.rmtree, root, ignore_errors=True)
        # The real layout every run lives at: <repo-root>/ResearchSystem/assurance/runs/<id>
        # — four levels below repo-root, matching `run_dir.parents[3]` in the template.
        run_dir = root / "ResearchSystem" / "assurance" / "runs" / run_id
        control = run_dir / "control"
        control.mkdir(parents=True)
        # Zero obligations: the fulfillment guard (M8/M9/M10, tested above) passes vacuously,
        # so this fixture stays about the derivation alone and proves nothing about them.
        (control / "work-spec.json").write_text(
            json.dumps({"work_id": "w-deriv", "obligations": [], "expected_artifacts": []}),
            encoding="utf-8")
        (control / "resolved-plan.json").write_text(
            json.dumps({"effective_change_boundary": {"write_scope": [], "out": []}}),
            encoding="utf-8")
        (control / "state.json").write_text(
            json.dumps({
                "work_id": "w-deriv", "run_id": run_id, "status": "EXECUTING",
                "repair_round": 0,
                "work_spec_ref": {
                    "path": f"ResearchSystem/assurance/runs/{run_id}/control/work-spec.json"},
                "resolved_plan_ref": {
                    "path": f"ResearchSystem/assurance/runs/{run_id}/control/resolved-plan.json"},
            }),
            encoding="utf-8")

        # `observe_manifest` is the first thing after CONTROL_ROOT that needs a real Git
        # repository; stubbing it keeps this fixture testing path arithmetic, not Git.
        fake_manifest = {
            "authored_by": "x", "boundary_result": "CONFORMANT",
            "expected_artifact_results": [],
        }
        with mock.patch.object(
            self.template.cand, "build_record", wraps=self.template.cand.build_record,
        ) as spy_build_record, mock.patch.object(
            self.template.cand, "observe_manifest", return_value=fake_manifest,
        ):
            captured_stdout = io.StringIO()
            with contextlib.redirect_stdout(captured_stdout):
                try:
                    self.template.main([
                        str(run_dir),
                        "--base", "b" * 40,
                        "--candidate", "c" * 40,
                        "--candidate-branch", f"run/{run_id}-candidate",
                    ])
                except Exception:
                    # Whatever main() does after build_record — real Git calls against a
                    # directory that is not a Git repository — is not this fixture's concern;
                    # the derivation was already captured by the spy above.
                    pass

        self.assertIsNotNone(
            spy_build_record.call_args,
            f"cand.build_record was never reached for run {run_id!r} — the guard or the "
            "fixture broke before the derivation under test ever ran")
        return spy_build_record.call_args.kwargs["control_root"]

    def test_repo_root_defaults_to_the_run_directorys_fourth_parent(self):
        """M11: no --repo-root on argv, so REPO must come from `run_dir.parents[3]`.

        A regression to `parents[2]` makes REPO one level too shallow, which drops the
        leading `ResearchSystem/` segment from `control_root` (`run_dir.relative_to(REPO)`
        starts one directory later) — caught here by the wrong VALUE, exactly the shape M11
        currently survives silently rather than by any exception.

        What the assertion observes is `control_root` alone, so it binds REPO only while
        `CONTROL_ROOT = run_dir.relative_to(REPO)` stands — replace that derivation and the
        `parents[3]` default is unguarded again (FULL `7dd027e` L-1, its M13: a per-run
        hard-coded prefix plus `parents[2]` passes the whole suite).
        """
        control_root = self._run_and_capture_control_root("tr-deriv-one")
        self.assertEqual(control_root, "ResearchSystem/assurance/runs/tr-deriv-one")

    def test_control_root_is_derived_per_run_not_a_shared_constant(self):
        """M12: `CONTROL_ROOT` hard-coded to a different run's name.

        Two different run ids must each see their OWN name in `control_root`. A hard-coded
        constant is the same string for both calls, so it can match at most one of the two
        expected values below — this fails wherever M12 does not.
        """
        first = self._run_and_capture_control_root("tr-deriv-alpha")
        second = self._run_and_capture_control_root("tr-deriv-beta")
        self.assertEqual(first, "ResearchSystem/assurance/runs/tr-deriv-alpha")
        self.assertEqual(second, "ResearchSystem/assurance/runs/tr-deriv-beta")
        self.assertNotEqual(first, second)


if __name__ == "__main__":
    raise SystemExit(unittest.main(argv=[sys.argv[0]]))
