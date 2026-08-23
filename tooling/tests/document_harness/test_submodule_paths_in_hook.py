#!/usr/bin/env python3
"""Submodule-internal paths, judged where the guard actually runs: inside a git hook.

The defect class (round SUBMOD-HOOKENV): round STRANGER-GUARDS taught `TrackedPaths` to
answer for a mounted submodule by listing that submodule's own index, and every test of it
called the code directly. Git does not. It runs a pre-commit hook with the SUPERPROJECT's
repository-location variables exported, and `git -C <mount> ls-files` inherits them, so the
question "what does this submodule track" is answered by the superproject. Both directions
were measured on one scratch tree, and neither raises:

* `git commit` exports ``GIT_INDEX_FILE=.git/index``, relative. Resolved under the mount,
  where `.git` is a gitdir *file*, it names nothing: **0 lines, exit 0**. An empty listing
  was read as *this submodule tracks nothing*, so the mount never entered
  `unlistable_mounts` and every real path under it came back UNRESOLVED — the false block
  that earns a hook bypass.
* `git commit -a` and `git commit -- <path>` export it **absolute**, naming the
  superproject's own index or lock. Resolved under the mount it opens fine, and the
  superproject's file list is returned as the submodule's — so `mount/<superproject file>`
  falsely resolves while the mount's real files still do not. Measured on four probes, every
  answer inverted.

Same shape as rounds TEMPLATE-LIB-ROOT and PUB-FACADE: in-process green, dead in the only
context that ships. The pin is therefore a real `git commit` in a real superproject with a
real submodule — git exports the environment, not the test, so a future git that exports
something else is caught here rather than in a caller's tree.

The two commit forms are both exercised because they are different branches of the defect,
not two spellings of one; the plain form is the false block, the `-a` form the false
resolution. Each is paired with a control that must still fire: a nonexistent path under the
mount, and a nonexistent path in the superproject, both blocked. A fix that cleared the
environment by blinding the guard fails those.

NOT pinned, stated so the next reader is not sold more than is bought: which variables git
exports, and to which hooks. This file asks git to run the hook and reads what happens; the
variable names are git's own answer (`git rev-parse --local-env-vars`), not a list here.
"""
from __future__ import annotations

import os
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest
import unittest.mock

from _harness import RS_ROOT

from rsclib.document_harness.paths import (
    DIRECT,
    OUT_OF_INDEX,
    UNRESOLVED,
    TrackedPaths,
    classify_path_token,
)

CHECK = RS_ROOT / "tooling" / "hooks" / "candidate_path_check.py"

#: Hand-written expectations (E5): whole lines, independent of the module under guard.
BLOCKED_LINE = (
    "pre-commit BLOCKED: newly written text names a repository path that exists nowhere:"
)

#: The work product every test stages, and the paths it cites. Backticks are assembled at
#: use so no committed line of this file carries a live broken path token.
NOTE = "docs/note.md"
MOUNT_REAL = "mount/deep/dir/file.md"
MOUNT_ABSENT = "mount/no-such-file-submod-hookenv.md"
SUPER_ABSENT = "docs/no-such-file-submod-hookenv.md"
#: Exists in the SUPERPROJECT at this path and nowhere under the mount — the token that
#: falsely resolved when the superproject answered for the submodule.
MOUNT_SHADOWING_SUPER = "mount/" + NOTE


def _cited(token: str) -> str:
    return "probe " + "`" + token + "`" + " token\n"


def _finding_line(token: str) -> str:
    return "  " + NOTE + ": " + "`" + token + "`"


def _git(root: pathlib.Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-C", str(root), *args],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )


def _init(root: pathlib.Path) -> None:
    root.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["git", "init", "-q", "-b", "main", str(root)], check=True, capture_output=True
    )
    _git(root, "config", "user.email", "harness@example.invalid")
    _git(root, "config", "user.name", "V3 test harness")
    _git(root, "config", "commit.gpgsign", "false")


def _mount_source(root: pathlib.Path, files: dict[str, str]) -> pathlib.Path:
    """A standalone repository to mount. No files means a commit of an empty tree."""
    _init(root)
    for rel, text in files.items():
        target = root / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
    if files:
        _git(root, "add", "-A")
        _git(root, "commit", "-qm", "mount base")
    else:
        _git(root, "commit", "-q", "--allow-empty", "-m", "empty mount base")
    return root


def _superproject(base: pathlib.Path, mount_files: dict[str, str]) -> pathlib.Path:
    """A superproject with `mount_files` mounted at `mount/`, hook not yet wired."""
    source = _mount_source(base / "mount-source", mount_files)
    root = base / "super"
    _init(root)
    (root / "seed.md").write_text("seed\n", encoding="utf-8")
    _git(root, "add", "seed.md")
    _git(root, "commit", "-qm", "seed")
    _git(
        root,
        "-c",
        "protocol.file.allow=always",
        "submodule",
        "add",
        "-q",
        source.as_posix(),
        "mount",
    )
    _git(root, "commit", "-qm", "mount the submodule")
    return root


def _wire_hook(root: pathlib.Path) -> None:
    """Point the superproject's pre-commit at the instrument's own guard.

    `sys.executable`, never a bare `python`: the battery's interpreter is the one carrying
    this checkout's dependencies, and round PUB-FACADE measured a bare name resolving to the
    other one.
    """
    hook = root / ".git" / "hooks" / "pre-commit"
    hook.write_text(
        "#!/bin/sh\n"
        f'exec "{pathlib.Path(sys.executable).as_posix()}" "{CHECK.as_posix()}"\n',
        encoding="utf-8",
    )
    os.chmod(hook, 0o755)


def _stage_note(root: pathlib.Path, token: str) -> None:
    note = root / NOTE
    note.parent.mkdir(parents=True, exist_ok=True)
    note.write_text(_cited(token), encoding="utf-8")
    _git(root, "add", NOTE)


def _commit(root: pathlib.Path, *extra: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-C", str(root), "commit", "-m", "cite a path", *extra],
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )


def _head(root: pathlib.Path) -> str:
    return _git(root, "rev-parse", "HEAD").stdout.strip()


def _lines(result: subprocess.CompletedProcess) -> list[str]:
    """The hook's output, both streams.

    Which stream carries it is git's choice, not the guard's: git attaches a hook's stdout
    to its own stderr, so the guard's `print` arrives on stderr here (measured — the first
    form of this file asserted against stdout alone and found it empty). Reading both keeps
    the assertion about what the guard said rather than about how git plumbed it.
    """
    return result.stdout.splitlines() + result.stderr.splitlines()


@unittest.skipUnless(shutil.which("git"), "no git on PATH")
@unittest.skipUnless(shutil.which("sh"), "no sh on PATH — git cannot run the hook")
class SubmodulePathsInsideAHookTests(unittest.TestCase):
    """Every test drives a real `git commit`, so git exports the hook environment."""

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory(prefix="v3-submod-hook-")
        self.base = pathlib.Path(self._tmp.name)
        self.root = _superproject(
            self.base, {"deep/dir/file.md": "deep\n", "top.md": "top\n"}
        )
        _wire_hook(self.root)

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def _assert_committed(self, before: str, result: subprocess.CompletedProcess) -> None:
        detail = f"\nstdout={result.stdout}\nstderr={result.stderr}"
        self.assertEqual(result.returncode, 0, "the hook blocked a real path:" + detail)
        self.assertNotEqual(_head(self.root), before, "no commit landed:" + detail)

    def _assert_blocked(
        self, before: str, result: subprocess.CompletedProcess, token: str
    ) -> None:
        detail = f"\nstdout={result.stdout}\nstderr={result.stderr}"
        self.assertEqual(result.returncode, 1, "the hook let a nowhere path through:" + detail)
        self.assertIn(BLOCKED_LINE, _lines(result), detail)
        self.assertIn(_finding_line(token), _lines(result), detail)
        self.assertEqual(_head(self.root), before, "a blocked commit landed anyway:" + detail)

    def test_a_real_submodule_path_survives_a_plain_commit(self):
        """`git commit`: relative GIT_INDEX_FILE, the false-block branch."""
        before = _head(self.root)
        _stage_note(self.root, MOUNT_REAL)
        self._assert_committed(before, _commit(self.root))

    def test_a_real_submodule_path_survives_an_all_commit(self):
        """`git commit -a`: absolute GIT_INDEX_FILE, the branch that opens the wrong index."""
        before = _head(self.root)
        _stage_note(self.root, MOUNT_REAL)
        self._assert_committed(before, _commit(self.root, "-a"))

    def test_the_superprojects_own_files_do_not_answer_for_the_mount(self):
        """A path that exists in the superproject and not under the mount stays a finding.

        Only clearing the inherited environment satisfies this: while the superproject's
        index answers, its every tracked path resolves a second time under `mount/`, and no
        amount of distrusting an empty listing sees it — the listing is full, and wrong.
        """
        before = _head(self.root)
        _stage_note(self.root, MOUNT_SHADOWING_SUPER)
        self._assert_blocked(before, _commit(self.root, "-a"), MOUNT_SHADOWING_SUPER)

    def test_a_nowhere_path_under_the_mount_is_still_blocked(self):
        """Control: the guard must not have been fixed by blinding it under the mount."""
        before = _head(self.root)
        _stage_note(self.root, MOUNT_ABSENT)
        self._assert_blocked(before, _commit(self.root), MOUNT_ABSENT)

    def test_a_nowhere_path_in_the_superproject_is_still_blocked(self):
        """Control: the superproject scan still binds — the index the commit is building."""
        before = _head(self.root)
        _stage_note(self.root, SUPER_ABSENT)
        self._assert_blocked(before, _commit(self.root), SUPER_ABSENT)


@unittest.skipUnless(shutil.which("git"), "no git on PATH")
class AmbientRepositoryEnvironmentTests(unittest.TestCase):
    """The other half of the clear: the toplevel probe, and the variable that redirects it.

    `_submodule_files` asks the mount for its own toplevel before trusting any listing, and
    that question is answerable by the wrong repository too. Measured: with `GIT_WORK_TREE`
    exported at the superproject, `git -C mount rev-parse --show-toplevel` returns the
    SUPERPROJECT, the mount fails its own identity check, and every path under it turns
    OUT_OF_INDEX — the guard blind rather than wrong, and silent either way.

    Git does not export `GIT_WORK_TREE` to a pre-commit hook, so this branch is set here by
    hand rather than by a commit — it is a member of the class git's own
    `--local-env-vars` names, not a second spelling of the hook case, and it is the
    assertion the toplevel probe's cleared environment answers to.
    """

    def test_a_redirected_work_tree_does_not_reach_the_mounts_own_question(self):
        with tempfile.TemporaryDirectory(prefix="v3-submod-env-") as tmp:
            root = _superproject(pathlib.Path(tmp), {"real.md": "real\n"})
            with unittest.mock.patch.dict(os.environ, {"GIT_WORK_TREE": str(root)}):
                tracked = TrackedPaths.from_index(root)
            self.assertEqual(tracked.unlistable_mounts, ())
            self.assertEqual(
                classify_path_token("mount/real.md", "docs", tracked), DIRECT
            )
            # Not vacuous: the same listing still refuses a path that is not in it.
            self.assertEqual(
                classify_path_token(MOUNT_ABSENT, "docs", tracked), UNRESOLVED
            )


@unittest.skipUnless(shutil.which("git"), "no git on PATH")
class EmptySubmoduleListingTests(unittest.TestCase):
    """A mount that lists nothing is unanswerable, not empty — read directly, no hook.

    Separated from the hook tests on purpose: inside a hook the pre-fix environment produced
    an empty listing too, so a hook-driven assertion here could not tell which cause it was
    measuring. This one runs with the environment already clean, leaving the listing itself
    as the only variable.
    """

    def test_a_mount_whose_index_lists_nothing_is_out_of_index(self):
        with tempfile.TemporaryDirectory(prefix="v3-submod-empty-") as tmp:
            root = _superproject(pathlib.Path(tmp), {})
            tracked = TrackedPaths.from_index(root)
            self.assertEqual(tracked.unlistable_mounts, ("mount/",))
            self.assertEqual(
                classify_path_token(MOUNT_ABSENT, "docs", tracked), OUT_OF_INDEX
            )


if __name__ == "__main__":
    unittest.main()
