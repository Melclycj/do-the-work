#!/usr/bin/env python3
"""Round STRANGER-GUARDS: every template's git target is discovered or refused — as a process.

The defect class (E7), the remainder `test_run_v2_template_library_path.py` declared out of
its own scope: each of the six run-v2 template scripts defaulted its repository root to
``run_dir.parents[3]`` — a depth count that is the first caller's layout, an ancestor of
any run directory whatever the layout, and therefore a *plausible* wrong answer taken
quietly. The contract now: an explicit ``--repo-root`` (or second argument) as given;
otherwise the git toplevel of the run directory, announced on stderr; otherwise a loud
``SPEC_GAP`` refusal, exit 2.

Subprocess for the same reason as the library-path suite: the in-process suites already
pass explicit roots or build git fixtures, so only a real process shows what a run
operator actually gets. All six are exercised on the refusal leg — the old default could
not refuse at all, so this leg alone separates every script from its predecessor — and
the discovery leg is proven where each family makes it observable: the two argv gates by
their real verdicts at a depth the old count mis-rooted, the argparse family by the
announced root on a planted shallow run.
"""
from __future__ import annotations

import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

from _harness import RS_ROOT, TempRepo

TEMPLATE_DIR = RS_ROOT / "assurance" / "templates" / "run-v2"

#: Three paragraphs, one per non-blank line — hand-counted here rather than derived from
#: the skeleton function the scripts themselves call (E5).
INSTRUCTION = (
    "# Task instruction\n"
    "\n"
    "Write the guide.\n"
    "\n"
    "Every claim in the guide cites its source note.\n"
)
PARAGRAPH_COUNT = 3

#: Script -> the extra argv its parser requires before it can reach root resolution.
REQUIRED_ARGS = {
    "run_evidence_v2.py": (
        "--base", "b" * 40, "--candidate", "c" * 40, "--candidate-branch", "run/x",
        # Item 4: the message is refused before the root is resolved, so a fixture that
        # omits it never reaches the derivation this file is about.
        "--commit-message", "evidence commit\n\nKind: evidence commit. Fixture body.\n",
    ),
    "run_bind_v2.py": ("--evidence-commit", "e" * 40, "--bound-at", "2026-08-23"),
    "run_repair.py": (),
    "run_retire.py": (),
    "check_template_instance.py": (),
    "make_paragraph_map.py": (),
}

IMPORT_DIAGNOSTICS = ("ModuleNotFoundError", "ImportError", "Traceback")


def run_template(name: str, *args: str) -> subprocess.CompletedProcess:
    env = {**os.environ, "PYTHONIOENCODING": "utf-8"}
    return subprocess.run(
        [sys.executable, "-X", "utf8", str(TEMPLATE_DIR / name), *args],
        check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        encoding="utf-8", errors="replace", env=env,
    )


def shallow_run(repo: TempRepo) -> pathlib.Path:
    """A run directory at `runs/<id>` — a depth the old fourth-parent count mis-rooted."""
    run_dir = repo.root / "runs" / "run-root"
    (run_dir / "control").mkdir(parents=True)
    (run_dir / "control" / "work-spec.json").write_text(json.dumps({
        "schema_version": "2",
        "work_id": "run-root",
        "instruction_ref": {"path": "docs/instruction.md", "revision": repo.base},
        "unit_map": [],
    }), encoding="utf-8")
    return run_dir


class OutsideAnyRepositoryEveryScriptRefuses(unittest.TestCase):
    """The must-fire leg, all six: no toplevel to discover means SPEC_GAP and exit 2.

    The library must still have been found (no import diagnostic), or a crash would
    impersonate the refusal — which is how the previous defect class hid.
    """

    def test_each_script_refuses_loudly_with_the_same_sentence(self):
        for name, extra in REQUIRED_ARGS.items():
            with self.subTest(script=name):
                base = pathlib.Path(tempfile.mkdtemp(prefix="rr-refuse-")).resolve()
                self.addCleanup(shutil.rmtree, base, ignore_errors=True)
                run_dir = base / "run-x"
                run_dir.mkdir()
                done = run_template(name, str(run_dir), *extra)
                for marker in IMPORT_DIAGNOSTICS:
                    self.assertNotIn(marker, done.stderr)
                self.assertEqual(done.returncode, 2, done.stdout + done.stderr)
                self.assertIn(
                    f"SPEC_GAP: no repository root was given and {run_dir} is not "
                    "inside a git work tree; pass --repo-root explicitly",
                    done.stdout.splitlines(),
                )


class TheArgvGatesDiscoverTheRootAndReachTheirRealVerdicts(unittest.TestCase):
    """Discovery observed through behaviour only a correct root can produce.

    The instruction is pinned at a real commit of the fixture repository, so "instruction
    read from: pinned revision" can only be printed by a script whose `git -C` target was
    the discovered toplevel — the old count, pointed at this shallow layout, escaped the
    repository and fell back to a worktree miss.
    """

    def setUp(self):
        self.repo = TempRepo({"docs/instruction.md": INSTRUCTION})
        self.addCleanup(self.repo.cleanup)
        self.run_dir = shallow_run(self.repo)

    def test_make_paragraph_map_writes_the_skeleton_without_being_told_the_root(self):
        done = run_template("make_paragraph_map.py", str(self.run_dir))
        self.assertEqual(done.returncode, 0, done.stdout + done.stderr)
        self.assertIn(
            f"repo root discovered: {self.repo.root.resolve()}", done.stderr.splitlines()
        )
        lines = done.stdout.splitlines()
        self.assertIn("instruction read from: pinned revision", lines)
        map_path = self.run_dir / "control" / "paragraph-map.json"
        self.assertIn(f"wrote {PARAGRAPH_COUNT} paragraph(s) to {map_path}", lines)

    def test_the_authoring_gate_reaches_its_own_verdict_without_being_told_the_root(self):
        done = run_template("check_template_instance.py", str(self.run_dir))
        self.assertEqual(done.returncode, 1, done.stdout + done.stderr)
        self.assertIn(
            f"repo root discovered: {self.repo.root.resolve()}", done.stderr.splitlines()
        )
        lines = done.stdout.splitlines()
        self.assertIn("instruction read from: pinned revision", lines)
        self.assertTrue(any("TEMPLATE-PARAGRAPH-MAP-MISSING" in line for line in lines),
                        f"gate produced no map-missing verdict: {done.stdout!r}")

    def test_an_explicit_root_reproduces_the_discovered_answer(self):  # negative control
        told = run_template(
            "check_template_instance.py", str(self.run_dir), str(self.repo.root)
        )
        discovered = run_template("check_template_instance.py", str(self.run_dir))
        self.assertEqual(discovered.returncode, told.returncode)
        self.assertEqual(discovered.stdout, told.stdout)


class TheArgparseFamilyAnnouncesTheDiscoveredRoot(unittest.TestCase):
    """The stderr contract for the four run_* scripts, on the lightest of them.

    `run_retire.py` refuses a non-CLOSED run *after* root resolution, so reaching its STOP
    with the discovered root announced proves the family's default took the toplevel — at
    a depth where the old count landed outside the repository.
    """

    def test_run_retire_announces_the_root_and_then_refuses_on_status(self):
        repo = TempRepo()
        self.addCleanup(repo.cleanup)
        run_dir = shallow_run(repo)
        (run_dir / "control" / "state.json").write_text(json.dumps({
            "work_id": "run-root", "run_id": "run-root", "status": "REVIEWED",
            "repair_round": 0,
            "work_spec_ref": {"path": "runs/run-root/control/work-spec.json"},
            "resolved_plan_ref": {"path": "runs/run-root/control/resolved-plan.json"},
        }), encoding="utf-8")
        done = run_template("run_retire.py", str(run_dir))
        self.assertEqual(done.returncode, 1, done.stdout + done.stderr)
        self.assertIn(
            f"repo root discovered: {repo.root.resolve()}", done.stderr.splitlines()
        )
        self.assertTrue(
            any(line.startswith("STOP: run status is REVIEWED") for line in
                done.stdout.splitlines()),
            f"retire never reached its own refusal: {done.stdout!r}",
        )


if __name__ == "__main__":
    raise SystemExit(unittest.main())
