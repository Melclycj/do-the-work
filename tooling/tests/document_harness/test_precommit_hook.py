#!/usr/bin/env python3
"""The tracked pre-commit hook, run as git runs it — a subprocess under ``sh`` — works.

The defect class (round PUB-FACADE): the hook is a shell wrapper, and the battery exercised
only the Python script inside it, never the wrapper itself — so the wrapper invoked a bare
``python`` for months while every test stayed green, and the repository's first POSIX run
(2026-08-23, WSL Ubuntu, git 2.43.0) found that a wired clone could not commit at all:
``.githooks/pre-commit: 30: python: Permission denied``, exit 127, the check never running.
Same shape as round TEMPLATE-LIB-ROOT's dead template scripts: in-process green, subprocess
dead. The pin is therefore a subprocess running the hook file exactly as git would.

Three wrapper behaviours are pinned, and they are the ones that make it a guard rather than
a script: a benign staged tree passes (exit 0); a resolve-nowhere token staged into an
instruction-layer member comes back **through the wrapper** as the check's own BLOCKED
verdict and exit 1 — so a wrapper that runs nothing, or that swallows the check's non-zero
status, goes red here; and a tree without the check script refuses the commit loudly,
because a silent skip is how the caller's hook once spent a month calling a deleted script.

NOT pinned, stated so the next reader is not sold more than is bought (the first version of
this file claimed both halves and the FULL falsified it, ``v3-review-full-28dd80b.md`` B-2):
the python3-before-python *preference* itself. On any machine where ``python`` exists —
Windows, and CI runners after setup-python — a hook reverted to bare ``python`` still
resolves an interpreter and passes all three tests; only a platform without ``python``
observes that half (the RED run in ``journal/pub-facade-2026-08-23.md``). A fixture PATH
holding ``sh`` and ``git`` but no ``python`` was judged not worth its cost (E6); the
preference's carrier is the hook's own probe loop and the comment above it.

Also out of scope, deliberately: the no-interpreter-anywhere branch (same fixture-PATH cost),
and the check's own semantics, which ``test_precommit_checks.py`` already owns. Where ``sh``
itself is unavailable the tests skip — the ubuntu CI leg is the binding run, and it always
has ``sh``.
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

#: Hand-written expectations (E5): independent of the hook and the check they guard, whole
#: lines a mutation cannot half-satisfy.
MISSING_LINE = (
    "pre-commit: tooling/hooks/layer_path_check.py not found — the layer path check did NOT run."
)
BLOCKED_LINE = (
    "pre-commit BLOCKED: newly added instruction text names a repository path that does not resolve:"
)

#: A hand-written member path (E5: not imported from the module under guard) and a token that
#: resolves nowhere; the backticks are assembled here so no committed text carries a live
#: broken path token (the de-backticking concern rider `decited-paths` records).
MEMBER = "document-harness/CONSTRUCTION-CHECKLIST.md"
BAD_LINE = "probe " + "`" + "document-harness/no-such-file-pub-facade.md" + "`" + " token\n"


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


def _stage_bad_member_line(root: pathlib.Path) -> None:
    member = root / MEMBER
    member.parent.mkdir(parents=True, exist_ok=True)
    member.write_text(BAD_LINE, encoding="utf-8")
    subprocess.run(
        ["git", "-C", str(root), "add", MEMBER],
        check=True,
        capture_output=True,
        text=True,
    )


def _run_hook(root: pathlib.Path) -> subprocess.CompletedProcess:
    # errors="replace", the same tolerance layer_path_check itself applies to git's output:
    # on a Windows console locale the check's own findings print in the ANSI codepage, and a
    # strict decode here turns a correctly blocking hook into a crashed reader thread. The
    # asserted lines survive for two different reasons: BLOCKED_LINE is pure ASCII, and
    # MISSING_LINE — which carries an em dash — is echoed by the shell as the hook file's own
    # UTF-8 bytes, never through the check's locale-encoded stdout (measured,
    # v3-review-verify-71e1f24.md V-1).
    return subprocess.run(
        ["sh", ".githooks/pre-commit"],
        cwd=root,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )


@unittest.skipUnless(shutil.which("sh"), "no sh on PATH — the ubuntu CI leg is the binding run")
class PrecommitHookAsProcessTests(unittest.TestCase):
    def test_hook_passes_a_benign_commit(self):
        """A wired clone, check present, nothing offending staged: the wrapper exits 0."""
        with tempfile.TemporaryDirectory(prefix="v3-hook-") as tmp:
            root = pathlib.Path(tmp)
            _scratch_repo(root, with_check=True)
            result = _run_hook(root)
            self.assertEqual(
                result.returncode,
                0,
                f"hook failed where it must pass:\nstdout={result.stdout}\nstderr={result.stderr}",
            )

    def test_hook_blocks_when_the_layer_check_fails(self):
        """A resolve-nowhere token staged into a member: the check's verdict survives the wrapper.

        This is the assertion only a wrapper that actually ran the check and propagated its
        status can satisfy — an exit-0 stub fails the returncode, a wrapper that swallows
        the status fails it too, and one that never reaches the check cannot produce the
        BLOCKED line.
        """
        with tempfile.TemporaryDirectory(prefix="v3-hook-") as tmp:
            root = pathlib.Path(tmp)
            _scratch_repo(root, with_check=True)
            _stage_bad_member_line(root)
            result = _run_hook(root)
            self.assertEqual(
                result.returncode,
                1,
                f"hook must block:\nstdout={result.stdout}\nstderr={result.stderr}",
            )
            self.assertIn(BLOCKED_LINE, result.stdout.splitlines())

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
