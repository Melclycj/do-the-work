#!/usr/bin/env python3
"""The tracked pre-commit hook, run as git runs it — a subprocess under ``sh`` — works.

The defect class (round PUB-FACADE): the hook is a shell wrapper, and the battery exercised
only the Python script inside it, never the wrapper itself — so the wrapper invoked a bare
``python`` for months while every test stayed green, and the repository's first POSIX run
(2026-08-23, WSL Ubuntu, git 2.43.0) found that a wired clone could not commit at all:
``.githooks/pre-commit: 30: python: Permission denied``, exit 127, the check never running.
Same shape as round TEMPLATE-LIB-ROOT's dead template scripts: in-process green, subprocess
dead. The pin is therefore a subprocess running the hook file exactly as git would.

Both halves of the hook's contract are pinned: the working half (an interpreter is resolved
and the layer check runs — trivially clean in a scratch repository that stages no
instruction-layer member) and the loud-missing half (a tree without the check script refuses
the commit with a message, because a silent skip is how the caller's hook once spent a month
calling a deleted script).

Out of scope, deliberately: the no-interpreter-anywhere branch (crafting a PATH that holds
``sh`` and ``git`` but no Python is its own fixture project, and the branch is three lines of
straight-line shell); and the check's own semantics, which ``test_precommit_checks.py``
already owns. Where ``sh`` itself is unavailable the tests skip — the ubuntu CI leg is the
binding run, and it always has ``sh``.
"""
from __future__ import annotations

import pathlib
import shutil
import subprocess
import tempfile
import unittest

from _harness import RS_ROOT

HOOK = RS_ROOT / ".githooks" / "pre-commit"
CHECK = RS_ROOT / "tooling" / "hooks" / "layer_path_check.py"

#: Hand-written expectation (E5): the loud-missing line the hook must print, not read back
#: from the hook file it guards.
MISSING_LINE = (
    "pre-commit: tooling/hooks/layer_path_check.py not found — the layer path check did NOT run."
)


def _scratch_repo(root: pathlib.Path, *, with_check: bool) -> None:
    subprocess.run(
        ["git", "init", "-q", str(root)], check=True, capture_output=True, text=True
    )
    hooks_dir = root / ".githooks"
    hooks_dir.mkdir()
    shutil.copy(HOOK, hooks_dir / "pre-commit")
    if with_check:
        check_dir = root / "tooling" / "hooks"
        check_dir.mkdir(parents=True)
        shutil.copy(CHECK, check_dir / "layer_path_check.py")
    (root / "scratch.txt").write_text("scratch\n", encoding="utf-8")
    subprocess.run(
        ["git", "-C", str(root), "add", "scratch.txt"],
        check=True,
        capture_output=True,
        text=True,
    )


def _run_hook(root: pathlib.Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["sh", ".githooks/pre-commit"],
        cwd=root,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )


@unittest.skipUnless(shutil.which("sh"), "no sh on PATH — the ubuntu CI leg is the binding run")
class PrecommitHookAsProcessTests(unittest.TestCase):
    def test_hook_resolves_an_interpreter_and_runs_the_check(self):
        """A wired clone with the check script present can commit: the wrapper exits 0."""
        with tempfile.TemporaryDirectory(prefix="v3-hook-") as tmp:
            root = pathlib.Path(tmp)
            _scratch_repo(root, with_check=True)
            result = _run_hook(root)
            self.assertEqual(
                result.returncode,
                0,
                f"hook failed where it must pass:\nstdout={result.stdout}\nstderr={result.stderr}",
            )

    def test_hook_is_loud_when_the_check_script_is_missing(self):
        """A tree without the check refuses the commit and says the check did NOT run."""
        with tempfile.TemporaryDirectory(prefix="v3-hook-") as tmp:
            root = pathlib.Path(tmp)
            _scratch_repo(root, with_check=False)
            result = _run_hook(root)
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            self.assertIn(MISSING_LINE, result.stdout.splitlines())


if __name__ == "__main__":
    unittest.main()
