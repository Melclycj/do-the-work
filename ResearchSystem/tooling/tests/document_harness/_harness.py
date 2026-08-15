"""Shared plumbing for the V3-N1 test matrix.

Only mechanism lives here — a disposable Git repository and the import path. Fixtures are
deliberately NOT centralized: each test builds the exact document it is making a claim
about, so a reader can see the defect being demonstrated without chasing a shared factory.

Every repository this module creates is a fresh temporary directory. Nothing in the test
matrix may write into the repository under assurance: an out-of-boundary write by the test
suite would itself violate the node's change boundary.
"""
from __future__ import annotations

import pathlib
import shutil
import subprocess
import sys
import tempfile

TEST_DIR = pathlib.Path(__file__).resolve().parent
RS_ROOT = TEST_DIR.parents[2]
TOOLING_DIR = RS_ROOT / "tooling"
if str(TOOLING_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLING_DIR))


def git(root: pathlib.Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", "-C", str(root), *args],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        errors="replace",
    )
    if completed.returncode:
        raise RuntimeError(f"git {' '.join(args)} failed: {completed.stderr or completed.stdout}")
    return completed.stdout.strip()


class TempRepo:
    """A disposable Git repository with a base commit and an isolated candidate branch.

    Usage::

        with TempRepo({"docs/instruction.md": "..."}) as repo:
            candidate = repo.commit_candidate({"docs/guide.md": "..."})

    `repo.base` and `candidate` are exact commit SHAs — the identities every v3 record binds.
    """

    def __init__(self, base_files: dict[str, str] | None = None) -> None:
        self.root = pathlib.Path(tempfile.mkdtemp(prefix="v3n1-"))
        git(self.root, "init", "-q", "-b", "main")
        git(self.root, "config", "user.email", "harness@example.invalid")
        git(self.root, "config", "user.name", "V3 test harness")
        git(self.root, "config", "commit.gpgsign", "false")
        self.write(base_files or {"README.md": "base\n"})
        git(self.root, "add", "-A")
        git(self.root, "commit", "-qm", "base")
        self.base = git(self.root, "rev-parse", "HEAD")
        self.branch = "main"

    def __enter__(self) -> "TempRepo":
        return self

    def __exit__(self, *exc_info: object) -> None:
        self.cleanup()

    def cleanup(self) -> None:
        shutil.rmtree(self.root, ignore_errors=True)

    def write(self, files: dict[str, str]) -> None:
        for rel, content in files.items():
            target = self.root / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")

    def delete(self, *rel_paths: str) -> None:
        for rel in rel_paths:
            (self.root / rel).unlink(missing_ok=True)

    def commit_candidate(self, files: dict[str, str], branch: str = "cand", message: str = "candidate") -> str:
        """Write files on an isolated branch and return the exact candidate commit."""
        if branch != self.branch:
            git(self.root, "checkout", "-q", "-b", branch)
            self.branch = branch
        self.write(files)
        git(self.root, "add", "-A")
        git(self.root, "commit", "-qm", message)
        return git(self.root, "rev-parse", "HEAD")

    def commit_all(self, message: str = "change") -> str:
        git(self.root, "add", "-A")
        git(self.root, "commit", "-qm", message)
        return git(self.root, "rev-parse", "HEAD")

    def head(self) -> str:
        return git(self.root, "rev-parse", "HEAD")

    def candidate_ref(self, commit: str, branch: str | None = None) -> dict[str, str]:
        return {"branch": branch or self.branch, "commit": commit}
