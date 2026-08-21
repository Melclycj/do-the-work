#!/usr/bin/env python3
"""Every run-v2 template script locates its own library — proven by subprocess, not import.

The defect class (round TEMPLATE-LIB-ROOT): a template script that reaches for the harness
library through the tree it was handed as an *argument* finds nothing there. Since the
repository split, that argument names the **caller's** repository, which holds run data and
no library, so the only tree a script may locate its library in is the one it lives in.
``check_template_instance.py`` and ``make_paragraph_map.py`` computed it as
``<repo-root>/ResearchSystem/tooling`` and died at import against a real caller run
directory; the other four already computed it from ``__file__``. One variable was doing two
jobs — finding the library, and being the repository the instruction is pinned in — and
after the split those are two different repositories.

Why a subprocess and not ``main()``: the in-process tests load these scripts with
``exec_module`` after ``_harness`` has already put ``tooling/`` on ``sys.path``, so the test
satisfies the very import the script is supposed to satisfy itself, and the defect is
invisible — every one of them stayed green while the two scripts were dead. A subprocess
gets only the script's own directory on ``sys.path[0]``, and ``PYTHONPATH`` is stripped
below so that an ambient setting cannot stand in for the script's own answer.

All six are exercised, not the two that were reported: the class is "a template script
invoked as a real process finds its library", and the four that were already right are the
regression pins for it.

RED evidence, re-run 2026-08-21 with its commands and output pasted in
``document-harness/journal/template-lib-root-2026-08-21.md``: the pre-fix bytes, recovered
with ``git show 39e395e:``, exit 1 on ``ModuleNotFoundError: No module named 'rsclib'``
against a disposable caller-shaped repository, and — for the read-only gate, pointed at the
caller's own run directory — on ``ImportError: cannot import name 'load_json' from
'rsclib.document_harness' (unknown location)``; the two diagnostics differ only in whether
the tree being reached into still holds an ``rsclib`` package at all. The same invocations
at HEAD exit 0.

Out of scope, deliberately: the ``run_dir.parents[3]`` default each script falls back to
when no repository root is given. That depth assumption is the remainder of the re-rooting
item and is not this round's subject, and nothing below reaches it: the two invocations
that resolve a root pass one explicitly, the four ``--help`` calls exit at argparse before
root resolution, and the probe is a standalone file taking no arguments at all.
"""
from __future__ import annotations

import json
import os
import pathlib
import subprocess
import sys
import tempfile
import unittest

from _harness import RS_ROOT, TempRepo

TEMPLATE_DIR = RS_ROOT / "assurance" / "templates" / "run-v2"

# Three paragraphs, one per non-blank line — hand-counted here rather than derived from the
# skeleton function the scripts themselves call (E5: an expectation may not come from the
# thing it guards).
INSTRUCTION = (
    "# Task instruction\n"
    "\n"
    "Write the guide.\n"
    "\n"
    "Every claim in the guide cites its source note.\n"
)
PARAGRAPH_COUNT = 3

SELF_LOCATING = ("run_evidence_v2.py", "run_bind_v2.py", "run_repair.py", "run_retire.py")

IMPORT_DIAGNOSTICS = ("ModuleNotFoundError", "ImportError", "Traceback")


def run_script(script: pathlib.Path, *args: str) -> subprocess.CompletedProcess:
    """Invoke a script the way a run does: a real process, no inherited import path."""
    env = {k: v for k, v in os.environ.items() if k != "PYTHONPATH"}
    env["PYTHONIOENCODING"] = "utf-8"
    return subprocess.run(
        [sys.executable, "-X", "utf8", str(script), *args],
        check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        encoding="utf-8", errors="replace", env=env,
    )


def run_template(name: str, *args: str) -> subprocess.CompletedProcess:
    return run_script(TEMPLATE_DIR / name, *args)


def assert_library_was_found(case: unittest.TestCase, done: subprocess.CompletedProcess) -> None:
    """No import diagnostic on stderr, whatever else the script went on to decide."""
    for marker in IMPORT_DIAGNOSTICS:
        case.assertNotIn(marker, done.stderr)


def caller_shaped_run(repo: TempRepo) -> pathlib.Path:
    """A run directory where a caller's sits, with the WorkSpec the two scripts read."""
    run_dir = repo.root / "assurance" / "runs" / "run-lib"
    (run_dir / "control").mkdir(parents=True)
    (run_dir / "control" / "work-spec.json").write_text(json.dumps({
        "schema_version": "2",
        "work_id": "run-lib",
        "instruction_ref": {"path": "docs/instruction.md", "revision": repo.base},
        "unit_map": [],
    }), encoding="utf-8")
    return run_dir


class SelfLocatingScriptsStayThatWay(unittest.TestCase):
    """The four that already computed the library from __file__ — the regression pins.

    ``--help`` is enough: the module-level imports run before argparse sees the flag, so a
    script that could not find its library never reaches the usage line.
    """

    def test_each_prints_its_usage_after_importing_the_library(self):
        for name in SELF_LOCATING:
            with self.subTest(script=name):
                done = run_template(name, "--help")
                assert_library_was_found(self, done)
                self.assertEqual(done.returncode, 0)
                self.assertEqual(done.stdout.splitlines()[0].split()[:2], ["usage:", name])


class RepairedScriptsFindTheLibraryFromTheirOwnTree(unittest.TestCase):
    """The two that reached through the caller's tree. Both now run against a caller-shaped one.

    The fixture is a disposable repository whose run directory sits where a caller's does and
    whose instruction is pinned at a real commit, so the tree each script reports is the
    pinned one and the assertion below is a whole line rather than a prefix.
    """

    def setUp(self):
        self.repo = TempRepo({"docs/instruction.md": INSTRUCTION})
        self.addCleanup(self.repo.cleanup)
        self.run_dir = caller_shaped_run(self.repo)

    def test_make_paragraph_map_writes_the_skeleton(self):
        done = run_template("make_paragraph_map.py", str(self.run_dir), str(self.repo.root))
        assert_library_was_found(self, done)
        self.assertEqual(done.returncode, 0)
        map_path = self.run_dir / "control" / "paragraph-map.json"
        lines = done.stdout.splitlines()
        self.assertIn("instruction read from: pinned revision", lines)
        self.assertIn(f"wrote {PARAGRAPH_COUNT} paragraph(s) to {map_path}", lines)
        written = json.loads(map_path.read_text(encoding="utf-8"))
        self.assertEqual(len(written["paragraphs"]), PARAGRAPH_COUNT)

    def test_the_authoring_gate_reaches_its_own_verdict(self):
        """No map on disk, so the gate refuses — a verdict it reaches only after importing."""
        done = run_template("check_template_instance.py", str(self.run_dir), str(self.repo.root))
        assert_library_was_found(self, done)
        self.assertEqual(done.returncode, 1)
        lines = done.stdout.splitlines()
        self.assertIn("instruction read from: pinned revision", lines)
        self.assertTrue(any("TEMPLATE-PARAGRAPH-MAP-MISSING" in line for line in lines),
                        f"gate produced no map-missing verdict: {done.stdout!r}")


class TheProbeCanFail(unittest.TestCase):
    """Negative control for the assertion the two classes above lean on.

    Without it they would also pass against a runner that swallowed the child's stderr or
    its exit code — which is the shape that let the defect live: the in-process tests were
    green because something other than the script satisfied the import.
    """

    def test_a_process_that_cannot_find_the_library_is_observed_failing(self):
        with tempfile.TemporaryDirectory(prefix="libpath-") as tmp:
            probe = pathlib.Path(tmp) / "probe.py"
            probe.write_text(
                "from rsclib.document_harness import load_json\n", encoding="utf-8")
            done = run_script(probe)
        self.assertNotEqual(done.returncode, 0)
        self.assertIn("ModuleNotFoundError", done.stderr)
        with self.assertRaises(AssertionError):
            assert_library_was_found(self, done)


if __name__ == "__main__":
    unittest.main()
