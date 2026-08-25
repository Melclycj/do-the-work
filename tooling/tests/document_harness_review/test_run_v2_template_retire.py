#!/usr/bin/env python3
"""HD-12 — closeout retires per-CheckResult files, and only on a CLOSED run.

`run_retire.py` is the sixth shared run-v2 template script (A2-R4; named `run_closeout.py`
until FULL `d52f41b` `B-1` — that name already means the run-own post-run issue step in
p4-doc and p4-bridge, so the template member was renamed), added the round after
the shared-core round (`HD-11` part two, A2-R3) that made the other five call-in-place. Its
whole job is `HD-12` (2026-08-08, user, batch A `D2`): once a run's `control/state.json`
reaches the terminal `CLOSED` status, the per-CheckResult files the committed plan's
`check_order` names — `evidence/check-<check_id>.json` — are retired (deleted, staged, never
rewritten), and only the aggregate (`evidence/check-results.json`) and the raw one-hand
output each check wrote (`evidence/<check_id>.out.txt`) survive. Two things HD-12
explicitly leaves alone, and this suite does NOT re-litigate: `check_result_refs` on
`control/assurance-candidate.json` is untouched (ruled D-a — its digests still verify against
the evidence commit in git history, `git show` and all); and the ruling reaches only *future*
runs, never the eight already closed, which this suite never opens.

The property under test is therefore "CLOSED gates everything, the plan's check_order is the
only source of what might be deleted, presence deletes, absence is reported not raised, and
nothing outside the per-CheckResult set is ever touched" — whatever the script's internal
spelling. Every expected string below is a hand-written literal, never imported from the
template (E5): a test that asked the module for its own answer would pass against any answer.

The template is loaded by explicit file path under a distinct module name — importing it
runs only its module level (its `main` is guarded by `__name__`). `run_main`'s failure mode
follows the C0 F2 lesson: an exception inside `main` returns `None`, so a guard that did not
fire shows up as a VALUE mismatch (`None != 1`), never as a test ERROR that would prove
reachability but not behaviour (R8).

The end-to-end cases build a REAL disposable Git repository (`_harness.TempRepo`) and run the
template's actual `git rm`, because that is the one thing a stand-in cannot honestly exercise
— whether the working-tree file and the staged index entry both actually move. The pure-core
cases below them exercise `plan_closeout` directly, with no filesystem and no git, because the
status/check_order/existing-set partition is a property of data, not of I/O.
"""
from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import pathlib
import sys
import unittest

import _harness  # noqa: F401 — installs the tooling import path the template needs

from _harness import TempRepo, git

TEMPLATE_PATH: pathlib.Path = (
    _harness.RS_ROOT / "assurance" / "templates" / "run-v2" / "run_retire.py"
)


def load_template():
    """Bind the template file directly; never by adding its directory to sys.path."""
    if not TEMPLATE_PATH.is_file():
        raise RuntimeError(f"the v2 retirement template is missing at {TEMPLATE_PATH}")
    spec = importlib.util.spec_from_file_location("v2_retire_template", TEMPLATE_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules["v2_retire_template"] = module
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


RUN_ID = "tc-closeout"
CONTROL_ROOT = f"ResearchSystem/assurance/runs/{RUN_ID}"
#: Three checks the plan ordered; the third's per-result file is already gone when the
#: fixture is built, standing in for "a prior closeout pass already retired it".
CHECK_ORDER = ("chk-a", "chk-b", "chk-c", "chk-d")
PRESENT_IDS = ("chk-a", "chk-b", "chk-c")
#: Raw outputs exist for SOME ordered checks, never all of them (rider `retire-suite`): a
#: `command_exit` check writes one and other check kinds do not. The count they produce **must
#: differ from every count the template could derive without asking the filesystem** — with
#: three ordered checks that was impossible, because every non-zero raw count collided with
#: `check_order` (3), the deletion set (2) or `already_gone` (1), and each collision in turn
#: left a wrong implementation green (measured three times, three disguises). A fourth ordered
#: check breaks the tie: 2 against 4 / 3 / 1, and against a directory glob (3, the stray
#: included). `chk-d` carries the HD-12 property the docstring below states — per-result JSON
#: already gone, raw output surviving — and `chk-a` carries its mirror image.
RAW_IDS = ("chk-a", "chk-d")
ALREADY_GONE_IDS = ("chk-c",)


def state_doc(status: str) -> dict:
    return {"work_id": "w-closeout", "run_id": RUN_ID, "status": status, "repair_round": 0}


def plan_doc(check_order=CHECK_ORDER) -> dict:
    return {"plan_id": f"{RUN_ID}-plan", "work_id": "w-closeout", "check_order": list(check_order)}


class CloseoutTemplateCase(unittest.TestCase):
    """Shared fixture: a real disposable Git repository carrying one committed run."""

    def setUp(self):
        self.template = load_template()

    def make_run(
        self, *, status="CLOSED", check_order=CHECK_ORDER, present_ids=PRESENT_IDS,
        raw_ids=RAW_IDS,
    ) -> pathlib.Path:
        """A committed run under `<repo>/ResearchSystem/assurance/runs/<run-id>/`.

        A check in `raw_ids` gets a raw `<check_id>.out.txt` whether or not its per-result
        JSON is present — the two survive or vanish independently in this harness, exactly
        as HD-12 describes. `raw_ids` is deliberately a proper subset of `check_order`, so
        the kept count can only be right if the template asks the filesystem.
        """
        repo = TempRepo()
        self.addCleanup(repo.cleanup)
        files = {
            f"{CONTROL_ROOT}/control/state.json": json.dumps(state_doc(status)),
            f"{CONTROL_ROOT}/control/resolved-plan.json": json.dumps(plan_doc(check_order)),
            f"{CONTROL_ROOT}/evidence/check-results.json": json.dumps(
                {"aggregate": True, "of": list(check_order)}),
        }
        for check_id in raw_ids:
            files[f"{CONTROL_ROOT}/evidence/{check_id}.out.txt"] = f"raw output: {check_id}\n"
        # A stray raw output whose name matches the `chk-` id convention but belongs to no
        # check_order entry: the kept count must not include it (FULL d52f41b L-3 — the count
        # is derived from check_order like the deletion set, never from a directory glob).
        files[f"{CONTROL_ROOT}/evidence/chk-stray.out.txt"] = "not named by the plan\n"
        for check_id in present_ids:
            files[f"{CONTROL_ROOT}/evidence/check-{check_id}.json"] = json.dumps(
                {"check_id": check_id, "result": "PASS"})
        repo.write(files)
        repo.commit_all("closeout fixture: run setup")
        self.repo = repo
        run_dir = repo.root / "ResearchSystem" / "assurance" / "runs" / RUN_ID
        self.run_dir = run_dir
        return run_dir

    def staged_deletions(self) -> set[str]:
        """Paths `git diff --cached --name-status` reports as a staged Delete."""
        out = git(self.repo.root, "diff", "--cached", "--name-status")
        return {
            line.split("\t", 1)[1]
            for line in out.splitlines()
            if line.startswith("D\t")
        }


class ClosedRunRetiresPresentFiles(CloseoutTemplateCase):
    """① / ⑤: on a CLOSED run, present per-result files are git-rm'd; absent ones are not
    an error — they are counted as already retired."""

    def test_present_per_result_files_are_deleted_and_staged(self):
        run_dir = self.make_run()
        code, out = run_main(self.template, [str(run_dir)])
        self.assertEqual(code, 0, out)

        for check_id in PRESENT_IDS:
            target = run_dir / "evidence" / f"check-{check_id}.json"
            self.assertFalse(target.exists(), f"{target} should have been removed")

        expected = {f"{CONTROL_ROOT}/evidence/check-{check_id}.json" for check_id in PRESENT_IDS}
        self.assertEqual(self.staged_deletions(), expected)

    def test_the_summary_names_what_it_deleted(self):
        run_dir = self.make_run()
        _, out = run_main(self.template, [str(run_dir)])
        self.assertIn("deleted                : 3 (chk-a, chk-b, chk-c)", out.splitlines())

    def test_an_already_absent_check_result_is_reported_not_raised(self):
        run_dir = self.make_run()
        code, out = run_main(self.template, [str(run_dir)])
        self.assertEqual(code, 0, out)
        self.assertIn("already-retired        : 1 (chk-d)", out.splitlines())


class SurvivorsAreLeftAlone(CloseoutTemplateCase):
    """②: the aggregate and every raw one-hand output survive, staged and unstaged alike."""

    def test_aggregate_and_raw_outputs_still_exist_on_disk(self):
        run_dir = self.make_run()
        code, _ = run_main(self.template, [str(run_dir)])
        self.assertEqual(code, 0)
        self.assertTrue((run_dir / "evidence" / "check-results.json").is_file())
        for check_id in RAW_IDS:
            self.assertTrue(
                (run_dir / "evidence" / f"{check_id}.out.txt").is_file(),
                f"{check_id}.out.txt should have survived",
            )

    def test_survivors_carry_no_staged_change_at_all(self):
        run_dir = self.make_run()
        run_main(self.template, [str(run_dir)])
        staged = self.staged_deletions()
        for check_id in RAW_IDS:
            self.assertNotIn(f"{CONTROL_ROOT}/evidence/{check_id}.out.txt", staged)
        self.assertNotIn(f"{CONTROL_ROOT}/evidence/check-results.json", staged)

    def test_the_summary_reports_the_kept_counts(self):
        run_dir = self.make_run()
        _, out = run_main(self.template, [str(run_dir)])
        self.assertIn(
            "kept                   : 1 aggregate (check-results.json) + 2 raw output(s) "
            "(<check_id>.out.txt)",
            out.splitlines(),
        )
        self.assertIn(
            "note                   : check_result_refs in control/assurance-candidate.json "
            "stay as-is; their digests remain verifiable against the evidence commit in git "
            "history",
            out.splitlines(),
        )


class NonClosedRunRefuses(CloseoutTemplateCase):
    """③: a run that has not reached CLOSED refuses, names its actual status, deletes nothing."""

    def test_a_reviewed_run_is_refused_with_its_actual_status(self):
        run_dir = self.make_run(status="REVIEWED")
        code, out = run_main(self.template, [str(run_dir)])
        self.assertEqual(code, 1, out)
        self.assertEqual(
            out.strip(),
            "STOP: run status is REVIEWED, not CLOSED — HD-12 retires per-CheckResult files "
            "only after a run closes",
        )

    def test_a_refused_run_deletes_nothing(self):
        run_dir = self.make_run(status="REVIEWED")
        run_main(self.template, [str(run_dir)])
        for check_id in PRESENT_IDS:
            self.assertTrue((run_dir / "evidence" / f"check-{check_id}.json").is_file())
        self.assertEqual(self.staged_deletions(), set())


class SecondPassIsIdempotent(CloseoutTemplateCase):
    """④: running closeout again after everything is already retired changes nothing."""

    def test_the_second_pass_reports_nothing_to_delete(self):
        run_dir = self.make_run()
        first_code, _ = run_main(self.template, [str(run_dir)])
        self.assertEqual(first_code, 0)

        second_code, second_out = run_main(self.template, [str(run_dir)])
        self.assertEqual(second_code, 0, second_out)
        lines = second_out.splitlines()
        self.assertIn("deleted                : 0", lines)
        self.assertIn(
            f"already-retired        : {len(CHECK_ORDER)} ({', '.join(CHECK_ORDER)})", lines)
        self.assertIn("nothing to delete", lines)


class PureCoreDecision(unittest.TestCase):
    """⑥: `plan_closeout` is a pure function of (status, check_order, existing_ids) — no git."""

    def test_non_closed_status_refuses_and_deletes_nothing(self):
        template = load_template()
        to_delete, already_gone, refusal = template.plan_closeout(
            "REPAIRING", ["chk-a", "chk-b"], {"chk-a", "chk-b"})
        self.assertEqual(to_delete, [])
        self.assertEqual(already_gone, [])
        self.assertEqual(
            refusal,
            "run status is REPAIRING, not CLOSED — HD-12 retires per-CheckResult files only "
            "after a run closes",
        )

    def test_closed_status_partitions_by_the_existing_set(self):
        template = load_template()
        to_delete, already_gone, refusal = template.plan_closeout(
            "CLOSED", ["chk-a", "chk-b", "chk-c"], {"chk-a", "chk-c"})
        self.assertIsNone(refusal)
        self.assertEqual(to_delete, ["chk-a", "chk-c"])
        self.assertEqual(already_gone, ["chk-b"])

    def test_closed_status_with_nothing_on_disk_marks_everything_already_gone(self):
        template = load_template()
        to_delete, already_gone, refusal = template.plan_closeout(
            "CLOSED", ["chk-a", "chk-b"], set())
        self.assertIsNone(refusal)
        self.assertEqual(to_delete, [])
        self.assertEqual(already_gone, ["chk-a", "chk-b"])


if __name__ == "__main__":
    raise SystemExit(unittest.main(argv=[sys.argv[0]]))
