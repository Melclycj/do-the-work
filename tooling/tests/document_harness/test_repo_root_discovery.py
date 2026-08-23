#!/usr/bin/env python3
"""Round STRANGER-GUARDS: no command resolves a repository root silently from the cwd.

The defect class (E7): six commands defaulted `--repo-root` to the bare cwd, which is the
repository root only when the operator happens to stand there — one directory down, every
root-relative derivation went quietly wrong, the freeze marker's home included, and outside
any repository the commands still ran against whatever directory they were started in. The
contract now: `--repo-root` as given; otherwise the git toplevel of the cwd, announced on
stderr; otherwise a loud refusal, exit 2.

Three layers, because each hides a different regression:

* the discovery function itself (`caller.discover_repo_root`), unit-driven;
* the six call sites, pinned structurally — one command exercised end-to-end proves the
  helper works, and the source pin is what stops a seventh site (or a regressed sixth)
  from quietly going back to `Path.cwd()`;
* the real command line, subprocess with a real cwd — `init` for where writes land, and
  `dispatch` for the freeze marker, the write whose mis-homing disarms `E9`'s window.
"""
from __future__ import annotations

import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

import _harness
from _harness import TempRepo

from rsclib.document_harness import SpecGap, caller

CLI_SOURCE = (
    _harness.TOOLING_DIR / "rsclib" / "document_harness" / "cli.py"
).read_text(encoding="utf-8")


def outside_any_repository(case: unittest.TestCase) -> pathlib.Path:
    """A directory this test owns and no git work tree holds.

    Never a shared parent like the system temp directory: the first form of one test below
    asserted nothing was written into `repo.root.parent` — which is the machine's shared
    temp, where an earlier mutation run had legitimately left files, so the assertion
    failed on state the test never controlled.
    """
    made = pathlib.Path(tempfile.mkdtemp(prefix="no-repo-")).resolve()
    case.addCleanup(shutil.rmtree, made, ignore_errors=True)
    return made


def run_dtw(cwd: pathlib.Path, *argv: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(_harness.TOOLING_DIR / "dtw.py"), *argv],
        cwd=str(cwd),
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )


class Discovery(unittest.TestCase):
    def test_the_root_itself_and_a_nested_directory_both_answer_the_root(self):
        with TempRepo() as repo:
            nested = repo.root / "docs" / "deep"
            nested.mkdir(parents=True)
            expected = repo.root.resolve()
            self.assertEqual(caller.discover_repo_root(repo.root), expected)
            self.assertEqual(caller.discover_repo_root(nested), expected)

    def test_a_file_is_probed_through_its_directory(self):
        with TempRepo() as repo:
            self.assertEqual(
                caller.discover_repo_root(repo.root / "README.md"), repo.root.resolve()
            )

    def test_outside_a_work_tree_the_refusal_is_a_spec_gap(self):  # must fire
        outside = outside_any_repository(self)
        with self.assertRaises(SpecGap) as caught:
            caller.discover_repo_root(outside)
        self.assertEqual(
            str(caught.exception),
            f"no repository root was given and {outside} is not inside a git work "
            "tree; pass --repo-root explicitly",
        )


class TheSixCommandsShareTheDefault(unittest.TestCase):
    """The source pin: every `--repo-root` command routes through `_rooted`, none through cwd.

    E5: the expectations are these hand-written literals. Six is the count of commands
    taking `--repo-root` (governance-scan, status, dispatch, review's two modes, init); a
    seventh caller of the old cwd default would change the second count from zero and a
    dropped site would change the first from six.
    """

    def test_exactly_six_sites_take_the_helper(self):
        self.assertEqual(CLI_SOURCE.count("repo_root = _rooted(args)"), 6)

    def test_no_site_takes_the_bare_cwd_default(self):
        self.assertEqual(CLI_SOURCE.count("else pathlib.Path.cwd().resolve()"), 0)


class ThroughTheCommandLine(unittest.TestCase):
    def test_init_from_a_nested_directory_writes_at_the_toplevel(self):
        with TempRepo() as repo:
            nested = repo.root / "docs" / "deep"
            nested.mkdir(parents=True)
            completed = run_dtw(nested, "init")
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertIn(
                f"repo root discovered: {repo.root.resolve()}",
                completed.stderr.splitlines(),
            )
            self.assertTrue((repo.root / ".harness" / "scan-surfaces.json").is_file())
            self.assertFalse((nested / ".harness").exists(),
                             "init wrote into the cwd — the exact defect this round ends")

    def test_outside_a_work_tree_the_command_refuses_and_writes_nothing(self):  # must fire
        outside = outside_any_repository(self)
        completed = run_dtw(outside, "init")
        self.assertEqual(completed.returncode, 2, completed.stderr)
        self.assertIn(
            f"FATAL: no repository root was given and {outside} is not "
            "inside a git work tree; pass --repo-root explicitly",
            completed.stderr.splitlines(),
        )
        self.assertEqual(list(outside.iterdir()), [])

    def test_an_explicit_root_needs_no_discovery(self):  # negative control
        outside = outside_any_repository(self)
        with TempRepo() as repo:
            completed = run_dtw(outside, "init", "--repo-root", str(repo.root))
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertNotIn("repo root discovered", completed.stderr)
            self.assertTrue((repo.root / ".harness").is_dir())
            self.assertEqual(list(outside.iterdir()), [])

    def test_the_freeze_marker_lands_at_the_toplevel_not_the_cwd(self):
        # The concrete harm of the old default: a dispatch from a subdirectory wrote
        # `.harness/review-pending.json` beside the operator, where the tracked freeze
        # guard — reading from the repository root — would never see it, so E9's window
        # never actually held.
        with TempRepo({"a.md": "one\n"}) as repo:
            repo.write({"b.md": "two\n"})
            tip = repo.commit_all("tip")
            nested = repo.root / "docs"
            nested.mkdir(exist_ok=True)
            completed = run_dtw(nested, "dispatch", "--range", f"{repo.base}..{tip}")
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertTrue((repo.root / ".harness" / "review-pending.json").is_file())
            self.assertFalse((nested / ".harness").exists())


if __name__ == "__main__":
    raise SystemExit(unittest.main())
