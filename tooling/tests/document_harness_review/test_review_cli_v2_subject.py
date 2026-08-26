#!/usr/bin/env python3
"""M10 — `dtw review --subject <SHA>` reaches BOTH wave-2 checks from the command line.

The gap this closes is reachability, not logic: `check_subject` and `check_review_result_v2`
were fully implemented and fully unit-tested, while the only `review` the CLI offered was
the version-1 package path — so the wave-2 checks a reviewer is supposed to run had no
command to run them from, and `check_review_result_v2` had no caller outside a run script.

Reachability is asserted the way `test_dispatch.py` asserts it: by an issue code that ONLY
the function under test can emit. A code appearing in the CLI's output is proof the CLI
reached that function, and it cannot be satisfied by the command merely not crashing.
`V3-SUBJECT-…` codes come only from `review_subject.check_subject`; `V3-REVIEW-…` codes only
from `review_result_v2.check_review_result_v2`.

Every must-fire case is paired with the clean scenario, asserted clean FIRST (E4): a refusal
test proves nothing if the baseline also refuses. The scenario builder and the v2 result
fixture are imported from the wave-2 subject suite rather than copied, on that suite's own
reasoning — two builders would mean two slightly different notions of "a committed control
plane", and the newer one would quietly stop testing the real shape.

Expected codes and exit statuses below are hand-written literals, never imported from the
modules under test (E5).
"""
from __future__ import annotations

import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

import _harness
from test_review_v2_subject import EXECUTOR, build_scenario, make_result

FAKE_REV = "f" * 40


def run_cli(*argv: str) -> subprocess.CompletedProcess:
    """Drive the real command, exactly as a reviewer would (the point of this suite)."""
    return subprocess.run(
        [sys.executable, "dtw.py", "review", *argv],
        cwd=str(_harness.TOOLING_DIR),
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )


def output_of(completed: subprocess.CompletedProcess) -> str:
    return (completed.stdout or "") + (completed.stderr or "")


def write_json(document: dict) -> str:
    path = pathlib.Path(tempfile.mkdtemp(prefix="v3-review-cli-")) / "result.json"
    path.write_text(json.dumps(document, indent=1), encoding="utf-8")
    return str(path)


class TheSubjectModeReachesCheckSubject(unittest.TestCase):
    """`--subject <SHA>` alone answers 'is this commit a sound review subject'."""

    def test_the_clean_scenario_is_a_sound_subject(self):
        """The paired baseline. Without it, every refusal below would be uninformative."""
        scn = build_scenario()
        completed = run_cli("--subject", scn.evidence_commit, "--repo-root", str(scn.repo.root))
        output = output_of(completed)
        self.assertNotIn("Traceback", output)
        self.assertEqual(completed.returncode, 0, output)

    def test_a_check_result_the_plan_orders_but_the_commit_lacks_is_reported(self):
        """`V3-SUBJECT-CHECK-RESULT-MISSING` exists in `check_subject` and nowhere else."""
        scn = build_scenario(plan_mut=lambda plan: plan["check_order"].append("chk-two"))
        completed = run_cli("--subject", scn.evidence_commit, "--repo-root", str(scn.repo.root))
        output = output_of(completed)
        self.assertNotIn("Traceback", output)
        self.assertIn("V3-SUBJECT-CHECK-RESULT-MISSING", output)
        self.assertEqual(completed.returncode, 1, output)

    def test_the_subject_is_printed_in_full_never_abbreviated(self):
        """A reviewer copies this line into a record; 12 hex is a weaker binding (L4)."""
        scn = build_scenario()
        completed = run_cli("--subject", scn.evidence_commit, "--repo-root", str(scn.repo.root))
        output = output_of(completed)
        self.assertIn(f"evidence commit : {scn.evidence_commit}", output)
        self.assertEqual(len(scn.evidence_commit), 40)

    def test_an_input_of_the_retired_package_mode_is_refused_not_accepted(self):
        """L2's successor. `--check-result` fed the v1 branch, and this command used to
        refuse it by hand so that silently dropping it could not hide the disagreement — the
        subject mode derives the check results from the evidence commit. Round
        `CORE-SET-CODE` retired the branch and every input that only fed it, so the refusal
        is argparse's now. Kept as a test because what matters is that the flag is refused,
        not which layer refuses it: accepted and ignored is the failure either way.
        """
        scn = build_scenario()
        completed = run_cli(
            "--subject", scn.evidence_commit, "--repo-root", str(scn.repo.root),
            "--check-result", "anything.json",
        )
        output = output_of(completed)
        self.assertNotIn("Traceback", output)
        self.assertIn("unrecognized arguments: --check-result", output)
        self.assertEqual(completed.returncode, 2, output)

    def test_a_commit_carrying_no_control_plane_is_refused_not_traced(self):
        scn = build_scenario()
        completed = run_cli("--subject", scn.repo.base, "--repo-root", str(scn.repo.root))
        output = output_of(completed)
        self.assertNotIn("Traceback", output)
        self.assertIn("V3-DISPATCH-NOT-AN-EVIDENCE-COMMIT", output)
        self.assertEqual(completed.returncode, 1, output)

    def test_a_revision_that_does_not_resolve_is_refused_not_traced(self):
        scn = build_scenario()
        completed = run_cli("--subject", FAKE_REV, "--repo-root", str(scn.repo.root))
        output = output_of(completed)
        self.assertNotIn("Traceback", output)
        self.assertIn("V3-DISPATCH-COMMIT-UNREADABLE", output)
        self.assertEqual(completed.returncode, 1, output)


class TheSubjectModeReachesCheckReviewResultV2(unittest.TestCase):
    """`--subject <SHA> --result <path>` additionally checks the reviewer's own verdict."""

    def test_a_clean_v2_result_against_its_own_commit_passes(self):
        """Paired baseline for the refusals below. `--executor` is part of a clean call."""
        scn = build_scenario()
        completed = run_cli(
            "--subject", scn.evidence_commit, "--repo-root", str(scn.repo.root),
            "--result", write_json(make_result(scn)), "--executor", EXECUTOR,
        )
        output = output_of(completed)
        self.assertNotIn("Traceback", output)
        self.assertEqual(completed.returncode, 0, output)

    def test_an_omitted_executor_is_reported_unverified_rather_than_passed(self):
        """`--executor` really reaches the checker: omitting it must not read as clean.

        The checker's stated contract is 'optional in the signature, never optional in the
        report'. A CLI that dropped the flag on the floor would silently satisfy it.
        """
        scn = build_scenario()
        completed = run_cli(
            "--subject", scn.evidence_commit, "--repo-root", str(scn.repo.root),
            "--result", write_json(make_result(scn)),
        )
        output = output_of(completed)
        self.assertNotIn("Traceback", output)
        self.assertIn("V3-REVIEW-REVIEWER-DISTINCTNESS-UNVERIFIED", output)
        self.assertEqual(completed.returncode, 1, output)

    def test_a_result_answering_for_another_commit_is_reported(self):
        """`V3-REVIEW-SUBJECT-COMMIT-MISMATCH` exists in `check_review_result_v2` alone.

        This is the re-attribution class the commit binding exists to close: a verdict that
        names a different evidence commit than the one under check.
        """
        scn = build_scenario()
        result = make_result(scn)
        result["subject"]["evidence_commit"] = FAKE_REV
        completed = run_cli(
            "--subject", scn.evidence_commit, "--repo-root", str(scn.repo.root),
            "--result", write_json(result),
        )
        output = output_of(completed)
        self.assertNotIn("Traceback", output)
        self.assertIn("V3-REVIEW-SUBJECT-COMMIT-MISMATCH", output)
        self.assertEqual(completed.returncode, 1, output)

    def test_a_result_naming_another_run_is_reported(self):
        """A second `V3-REVIEW-…` code, so the wiring is not pinned by one branch alone."""
        scn = build_scenario()
        completed = run_cli(
            "--subject", scn.evidence_commit, "--repo-root", str(scn.repo.root),
            "--result", write_json(make_result(scn, run_id="run-two")),
        )
        output = output_of(completed)
        self.assertNotIn("Traceback", output)
        self.assertIn("V3-REVIEW-RUN-MISMATCH", output)
        self.assertEqual(completed.returncode, 1, output)

    def test_a_version_1_result_handed_to_the_v2_mode_stops_without_a_traceback(self):
        """`check_review_result_v2` raises SpecGap on a v1 result; the CLI must report it."""
        scn = build_scenario()
        v1_shaped = make_result(scn)
        del v1_shaped["schema_version"]
        completed = run_cli(
            "--subject", scn.evidence_commit, "--repo-root", str(scn.repo.root),
            "--result", write_json(v1_shaped),
        )
        output = output_of(completed)
        self.assertNotIn("Traceback", output)
        self.assertIn("FATAL", output)
        self.assertEqual(completed.returncode, 2, output)


# `TheVersionOneModeIsUndisturbed` stood here: E4's negative control for M10, proving the
# added `--subject` mode did not replace the `--package` path. Round `CORE-SET-CODE`
# retired that path, so the control has nothing left to be a control for; its four methods
# (a schema-invalid package reported rather than traced, the two modes refused together,
# and the two spec/record requirement cases) went with the mode they drove.


if __name__ == "__main__":
    raise SystemExit(unittest.main(argv=[sys.argv[0]]))
