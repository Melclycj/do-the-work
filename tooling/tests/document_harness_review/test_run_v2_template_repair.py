#!/usr/bin/env python3
"""L-1 — the repair step's argument surface, which R2 rewrote and no test held.

`v3-review-full-eec4171.md` §4 `L-1`: the whole surface of ``run_repair.py`` changed in R2
(CONFIG block → ``argparse``, ``sys.argv`` scan → ``args.emit``) and
``grep -rln run_repair ResearchSystem/tooling/`` returned nothing, so two mutations survived
all 649 tests:

* **M14** — ``--emit`` ignored, so a *dry run* advances the state to ``REPAIRING``. This is
  the class `E7` names — a state transition taken without the authorization that licenses it
  — sitting unguarded in the one step whose entire job is a gated transition.
* **M13** — the repo-root default off by one (``run_dir.parents[3]`` → ``parents[2]``), which
  yields a control root that is not repository-relative and so a state pointer nobody can
  resolve.

The property under test is therefore "the state file changes only when ``--emit`` says so,
and when it does the pointer it gains is built from the run's repository-relative control
root", whatever the module's internal spelling.

Every expectation below is a hand-written literal and is never imported from the template
(E5): a test that asked the module for its own answer would pass against any answer.
Assertions are made against WHOLE structures and whole printed lines. The one value computed
rather than typed is the decision file's bytes digest, computed from the fixture's OWN
serialisation via rsclib — the library under its own suites — never from the template.

The gate itself is the real ``flow.check_repair_decision`` over a schema-valid fixture
decision, review and plan: a stand-in would let the step pass documents the gate refuses.

The template is loaded by explicit file path under a distinct module name — importing it
runs only its module level (its ``main`` is guarded by ``__name__``). Failure mode of the
``run_main`` helper follows the C0 F2 lesson: an exception inside ``main`` returns None, so
"the guard did not fire" shows up as a VALUE mismatch (None != 1), never as a test ERROR
that would prove reachability but not behaviour (R8).

Since R2 the run directory arrives as an ARGUMENT, so every fixture builds the real shape
``<tmp>/ResearchSystem/assurance/runs/<run-id>/{control,evidence}`` — the layout the default
repo-root derivation counts four parents up from — instead of re-pointing module globals.
"""
from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import pathlib
import shutil
import sys
import subprocess
import tempfile
import unittest

import _harness  # noqa: F401 — installs the tooling import path the template needs

from rsclib.document_harness import bytes_digest

TEMPLATE_PATH: pathlib.Path = (
    _harness.RS_ROOT / "assurance" / "templates" / "run-v2" / "run_repair.py"
)


def load_template():
    """Bind the template file directly; never by adding its directory to sys.path."""
    if not TEMPLATE_PATH.is_file():
        raise RuntimeError(f"the v2 repair template is missing at {TEMPLATE_PATH}")
    spec = importlib.util.spec_from_file_location("v2_repair_template", TEMPLATE_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules["v2_repair_template"] = module
    spec.loader.exec_module(module)
    return module


def run_main(template, argv):
    """Run main(argv) capturing stdout; an exception returns None so guards fail on VALUE."""
    buffer = io.StringIO()
    try:
        with contextlib.redirect_stdout(buffer):
            code = template.main(argv)
    except Exception:
        return None, buffer.getvalue()
    return code, buffer.getvalue()


RUN_ID = "tr-seven"
WORK_ID = "w-test"
CONTROL_ROOT = f"ResearchSystem/assurance/runs/{RUN_ID}"
CANDIDATE_COMMIT = "c" * 40

#: The round-0 FULL this repair answers, hand-written in the v1 result shape the step reads
#: from ``evidence/review-full.json``. It found one blocker and one non-blocker.
FULL_REVIEW = {
    "result_id": "rv-full",
    "work_id": WORK_ID,
    "run_id": RUN_ID,
    "review_round": "FULL",
    "verdict": "CHANGES_REQUIRED",
    "candidate_ref": {"branch": f"{RUN_ID}-candidate", "commit": CANDIDATE_COMMIT},
    "findings": [
        {"finding_id": "f1", "blocking": True},
        {"finding_id": "f2", "blocking": False},
    ],
}

#: The plan whose effective boundary the repair boundary must only narrow.
RESOLVED_PLAN = {
    "effective_change_boundary": {"write_scope": ["docs"], "out": ["docs/private"]},
}


def repair_decision(*, accepted=("f1",)) -> dict:
    """A schema-valid REPAIR UserDecision that binds the reviewed candidate."""
    return {
        "decision_id": "ud-repair",
        "work_id": WORK_ID,
        "run_id": RUN_ID,
        "phase": "REPAIR",
        "decision": "APPLY_ACCEPTED_FINDINGS",
        "target": {
            "candidate_ref": {"branch": f"{RUN_ID}-candidate", "commit": CANDIDATE_COMMIT},
            "accepted_finding_ids": list(accepted),
            "repair_boundary": {"write_scope": ["docs"], "out": ["docs/private"]},
        },
        "decided_by": "Melclycj (user)",
        "decided_at": "2026-08-09",
    }


#: The position a repair is entered from: REVIEWED at round 0, carrying every pointer the
#: stages before it produced. Written out by hand rather than built by the harness (E5).
REVIEWED_STATE = {
    "work_id": WORK_ID,
    "run_id": RUN_ID,
    "status": "REVIEWED",
    "repair_round": 0,
    "work_spec_ref": {"path": f"{CONTROL_ROOT}/control/work-spec.json"},
    "resolved_plan_ref": {"path": f"{CONTROL_ROOT}/control/resolved-plan.json"},
    "instruction_audit_ref": {"path": f"{CONTROL_ROOT}/control/instruction-audit.json"},
    "start_decision_ref": {"path": f"{CONTROL_ROOT}/control/user-decision-start.json"},
    "fulfillment_ref": {"path": f"{CONTROL_ROOT}/evidence/candidate-record.json"},
    "manifest_ref": {"path": f"{CONTROL_ROOT}/evidence/candidate-record.json"},
    "coverage_ref": {"path": f"{CONTROL_ROOT}/evidence/coverage.json"},
    "review_ref": {"path": f"{CONTROL_ROOT}/evidence/review-full.json"},
    "next_action": "user decides the repair",
}

#: The exact sentence the emitted state carries, typed out here rather than imported.
EMITTED_NEXT_ACTION = (
    f"executor authors candidate C2 on {RUN_ID}-candidate, then regenerates every evidence "
    "document and a NEW evidence commit"
)


class RepairTemplateCase(unittest.TestCase):
    """Shared fixture: a throwaway repository the template is pointed at by argument."""

    def setUp(self):
        self.template = load_template()

    def make_run(self, *, decision=None, state=None,
                 under=("ResearchSystem", "assurance", "runs"), git=True):
        """The real run layout under a throwaway root.

        `under` is the path from the repository root down to the run's parent: the default
        repo-root derivation asks git for the toplevel (round STRANGER-GUARDS), so a run
        planted at another depth is how the derivation is shown to be discovery rather
        than the depth count it used to be. `git=False` withholds the repository, for the
        one test that drives the refusal.
        """
        root = pathlib.Path(tempfile.mkdtemp(prefix="l1-repair-"))
        self.addCleanup(shutil.rmtree, root, ignore_errors=True)
        if git:
            subprocess.run(
                ["git", "-C", str(root), "init", "-q"],
                check=True, stdout=subprocess.DEVNULL,
            )
        run_dir = root.joinpath(*under, RUN_ID)
        control = run_dir / "control"
        evidence = run_dir / "evidence"
        control.mkdir(parents=True)
        evidence.mkdir(parents=True)
        (evidence / "review-full.json").write_text(
            json.dumps(FULL_REVIEW), encoding="utf-8")
        (control / "resolved-plan.json").write_text(
            json.dumps(RESOLVED_PLAN), encoding="utf-8")
        (control / "state.json").write_text(
            json.dumps(REVIEWED_STATE if state is None else state), encoding="utf-8")
        (control / "user-decision-repair.json").write_text(
            json.dumps(repair_decision() if decision is None else decision), encoding="utf-8")
        self.root = root
        self.run_dir = run_dir
        return run_dir

    def saved_state(self):
        return json.loads(
            (self.run_dir / "control" / "state.json").read_text(encoding="utf-8"))

    def decision_digest(self, decision=None) -> str:
        """The digest of the bytes THIS fixture wrote, computed from its own serialisation."""
        return bytes_digest(
            json.dumps(repair_decision() if decision is None else decision).encode("utf-8"))


class TheStateMovesOnlyWhenEmitSaysSo(RepairTemplateCase):
    """M14: the dry run announces itself and leaves the state exactly as it found it."""

    def test_without_emit_the_state_file_is_not_touched(self):
        run_dir = self.make_run()
        code, out = run_main(self.template, [str(run_dir)])
        self.assertEqual(code, 0, out)
        self.assertEqual(self.saved_state(), REVIEWED_STATE)

    def test_the_dry_run_says_which_flag_would_have_moved_it(self):
        run_dir = self.make_run()
        _, out = run_main(self.template, [str(run_dir)])
        self.assertIn(
            "dry run               : pass --emit to advance the state to REPAIRING",
            out.splitlines(),
        )

    def test_the_dry_run_reports_the_gate_it_ran_and_the_findings_it_read(self):
        """The step is not silent about what it checked, or a dry run proves nothing."""
        run_dir = self.make_run()
        _, out = run_main(self.template, [str(run_dir)])
        self.assertEqual(
            out.splitlines(),
            [
                "check_repair_decision : clean",
                "accepted findings     : 1 (f1)",
                "dry run               : pass --emit to advance the state to REPAIRING",
            ],
        )

    def test_with_emit_the_state_advances_and_carries_the_decision_pointer(self):
        run_dir = self.make_run()
        code, out = run_main(self.template, [str(run_dir), "--emit"])
        self.assertEqual(code, 0, out)
        self.assertEqual(
            self.saved_state(),
            {
                "work_id": WORK_ID,
                "run_id": RUN_ID,
                "status": "REPAIRING",
                "repair_round": 1,
                "work_spec_ref": {"path": f"{CONTROL_ROOT}/control/work-spec.json"},
                "resolved_plan_ref": {"path": f"{CONTROL_ROOT}/control/resolved-plan.json"},
                "instruction_audit_ref": {
                    "path": f"{CONTROL_ROOT}/control/instruction-audit.json"},
                "start_decision_ref": {
                    "path": f"{CONTROL_ROOT}/control/user-decision-start.json"},
                "fulfillment_ref": {"path": f"{CONTROL_ROOT}/evidence/candidate-record.json"},
                "manifest_ref": {"path": f"{CONTROL_ROOT}/evidence/candidate-record.json"},
                "coverage_ref": {"path": f"{CONTROL_ROOT}/evidence/coverage.json"},
                "review_ref": {"path": f"{CONTROL_ROOT}/evidence/review-full.json"},
                "repair_decision_ref": {
                    "path": f"{CONTROL_ROOT}/control/user-decision-repair.json",
                    "digest_sha256": self.decision_digest(),
                },
                "next_action": EMITTED_NEXT_ACTION,
            },
        )

    def test_the_emitting_run_says_which_round_it_moved_to(self):
        run_dir = self.make_run()
        _, out = run_main(self.template, [str(run_dir), "--emit"])
        self.assertIn(
            "emitted               : state -> REPAIRING (repair_round 1)",
            out.splitlines(),
        )
        self.assertNotIn(
            "dry run               : pass --emit to advance the state to REPAIRING",
            out.splitlines(),
        )


class TheRepoRootIsTheRunDirectorysToplevel(RepairTemplateCase):
    """M13's successor: the default derivation, and what it is for — a repository-relative
    control root. Round STRANGER-GUARDS replaced the fourth-parent count with the git
    toplevel of the run directory, or a loud refusal — a depth count was the first
    caller's layout, silently wrong anywhere else.

    No test in this class passes ``--repo-root`` where the derivation is the subject: supplying
    the root by hand is exactly what would let a broken derivation pass.
    """

    def test_the_control_root_is_repository_relative_without_being_told_the_root(self):
        run_dir = self.make_run()
        code, out = run_main(self.template, [str(run_dir), "--emit"])
        self.assertEqual(code, 0, out)
        self.assertEqual(
            self.saved_state()["repair_decision_ref"],
            {
                "path": f"ResearchSystem/assurance/runs/{RUN_ID}/control/user-decision-repair.json",
                "digest_sha256": self.decision_digest(),
            },
        )

    def test_an_explicit_root_reproduces_the_derived_one(self):
        """Negative control (E4): the default and the explicit answer must be the same root."""
        run_dir = self.make_run()
        code, out = run_main(
            self.template, [str(run_dir), "--repo-root", str(self.root), "--emit"])
        self.assertEqual(code, 0, out)
        self.assertEqual(
            self.saved_state()["repair_decision_ref"]["path"],
            f"ResearchSystem/assurance/runs/{RUN_ID}/control/user-decision-repair.json",
        )

    def test_a_run_planted_at_another_depth_still_takes_the_repository_root(self):
        """The derivation is discovery, not a count of parents — the old bound is gone.

        A run at `<repo>/a/b/c/runs/<id>` instead of the first caller's
        `<repo>/ResearchSystem/assurance/runs/<id>`: the fourth-parent count this class
        used to pin took `<repo>/a` here and wrote a control root that started inside the
        repository — asserted then as "the template is depth-sensitive and detects
        nothing". Discovery answers the toplevel at any depth, so the whole path below
        starts at the repository; a regression to depth counting fails on the missing
        leading segment.
        """
        run_dir = self.make_run(under=("a", "b", "c", "runs"))
        code, out = run_main(self.template, [str(run_dir), "--emit"])
        self.assertEqual(code, 0, out)
        self.assertEqual(
            self.saved_state()["repair_decision_ref"]["path"],
            f"a/b/c/runs/{RUN_ID}/control/user-decision-repair.json",
        )

    def test_outside_any_repository_the_default_refuses_rather_than_guesses(self):
        """The other half of the contract: no toplevel to discover means SPEC_GAP, exit 2.

        The old default could not refuse — any directory has a fourth parent — which is
        exactly how a wrong root was taken quietly. The refusal line is asserted whole.
        """
        run_dir = self.make_run(git=False)
        code, out = run_main(self.template, [str(run_dir)])
        self.assertEqual(code, 2, out)
        self.assertIn(
            f"SPEC_GAP: no repository root was given and {run_dir.resolve()} is not "
            "inside a git work tree; pass --repo-root explicitly",
            out.splitlines(),
        )

    def test_a_root_that_is_not_an_ancestor_refuses_rather_than_guesses(self):
        """`relative_to` raises: there is no repository-relative control root to write."""
        run_dir = self.make_run()
        elsewhere = pathlib.Path(tempfile.mkdtemp(prefix="l1-elsewhere-"))
        self.addCleanup(shutil.rmtree, elsewhere, ignore_errors=True)
        with self.assertRaises(ValueError):
            self.template.main([str(run_dir), "--repo-root", str(elsewhere), "--emit"])


class TheGateIsTheRealOne(RepairTemplateCase):
    """The step's whole reason to exist: a decision the gate refuses moves nothing.

    Driven through the real ``flow.check_repair_decision`` — a stand-in here would test the
    template against an oracle that agrees with it by construction.
    """

    def test_a_decision_accepting_a_finding_the_review_never_made_is_refused(self):
        run_dir = self.make_run(decision=repair_decision(accepted=("f1", "f-nonexistent")))
        code, out = run_main(self.template, [str(run_dir), "--emit"])
        self.assertEqual(code, 1, out)
        self.assertIn("check_repair_decision : ISSUES", out.splitlines())

    def test_the_refused_decision_leaves_the_state_where_it_was(self):
        run_dir = self.make_run(decision=repair_decision(accepted=("f-nonexistent",)))
        code, _ = run_main(self.template, [str(run_dir), "--emit"])
        self.assertEqual(code, 1)
        self.assertEqual(self.saved_state(), REVIEWED_STATE)


if __name__ == "__main__":
    raise SystemExit(unittest.main(argv=[sys.argv[0]]))
