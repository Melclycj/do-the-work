#!/usr/bin/env python3
"""M10 — `rsc v3 review --subject <SHA>` reaches BOTH wave-2 checks from the command line.

The gap this closes is reachability, not logic: `check_subject` and `check_review_result_v2`
were fully implemented and fully unit-tested, while the only `v3 review` the CLI offered was
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
        [sys.executable, "rsc.py", "v3", "review", *argv],
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


def readable_package() -> pathlib.Path:
    """A package path that EXISTS and parses.

    Load-bearing for the v1-input tests: a nonexistent path short-circuits in `load_package`,
    which produces the same exit status the guard produces and hides whether the guard ran.
    """
    path = pathlib.Path(tempfile.mkdtemp(prefix="v3-review-v1-")) / "pkg.json"
    path.write_text('{"package_id":"p-1"}', encoding="utf-8")
    return path


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

    def test_check_result_is_refused_in_subject_mode_rather_than_dropped(self):
        """L2 — it is consumed only by the v1 branch; accepting it silently hides that."""
        scn = build_scenario()
        completed = run_cli(
            "--subject", scn.evidence_commit, "--repo-root", str(scn.repo.root),
            "--check-result", "anything.json",
        )
        output = output_of(completed)
        self.assertNotIn("Traceback", output)
        self.assertIn(
            "FATAL: --check-result belongs to --package mode; subject mode derives the check "
            "results from the evidence commit",
            output,
        )
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


class TheVersionOneModeIsUndisturbed(unittest.TestCase):
    """Negative control (E4): M10 ADDS a mode, it does not replace the package path.

    A change that broke everything would be indistinguishable from one that broke only what
    M10 targets without this. The v1 path has a live caller in `test_fix_round_locks.py`.
    """

    def test_a_schema_invalid_package_still_exits_one_without_a_traceback(self):
        tmp = pathlib.Path(tempfile.mkdtemp(prefix="v3-review-v1-"))
        (tmp / "pkg.json").write_text('{"package_id":"p-1"}', encoding="utf-8")
        (tmp / "spec.json").write_text(
            json.dumps(
                {
                    "work_id": "work-one",
                    "objective": "o",
                    "instruction_ref": {"path": "docs/i.md", "revision": "b" * 40},
                    "instruction_units": [],
                    "change_boundary": {"write_scope": ["docs"], "out": ["docs/private"]},
                    "expected_artifacts": [],
                    "obligations": [],
                }
            ),
            encoding="utf-8",
        )
        (tmp / "rec.json").write_text('{"run_id":"run-one"}', encoding="utf-8")
        completed = run_cli(
            "--package", str(tmp / "pkg.json"),
            "--spec", str(tmp / "spec.json"),
            "--record", str(tmp / "rec.json"),
        )
        output = output_of(completed)
        self.assertNotIn("Traceback", output)
        self.assertEqual(completed.returncode, 1, output)
        self.assertIn("defects", output)

    def test_the_two_modes_cannot_be_asked_for_at_once(self):
        scn = build_scenario()
        completed = run_cli(
            "--subject", scn.evidence_commit, "--package", "whatever.json",
        )
        self.assertEqual(completed.returncode, 2, output_of(completed))

    def test_the_version_one_mode_still_requires_its_spec_and_record(self):
        """Making them non-required for `--subject` must not make them optional for v1.

        The package must EXIST and parse. Pointed at a missing path — which is how this test
        was first written — the command dies in `load_package` before the guard is consulted
        and exits 2 either way, so the assertion held with the guard deleted and the test
        proved nothing (FULL a918e37..7572abd, F1). With a readable package the neutered
        guard reaches `load_spec(None)` and raises TypeError at spec.py:67, which is the
        traceback the assertion below was written to catch.
        """
        completed = run_cli("--package", str(readable_package()))
        output = output_of(completed)
        self.assertNotIn("Traceback", output)
        self.assertIn("FATAL: --package mode requires --spec and --record", output)
        self.assertEqual(completed.returncode, 2, output)

    def test_the_refusal_names_only_the_input_that_is_actually_absent(self):
        """The defect class, not the both-missing instance: one supplied, one omitted."""
        completed = run_cli(
            "--package", str(readable_package()), "--spec", str(readable_package()),
        )
        output = output_of(completed)
        self.assertNotIn("Traceback", output)
        self.assertIn("FATAL: --package mode requires --record", output)
        self.assertEqual(completed.returncode, 2, output)


if __name__ == "__main__":
    raise SystemExit(unittest.main(argv=[sys.argv[0]]))
