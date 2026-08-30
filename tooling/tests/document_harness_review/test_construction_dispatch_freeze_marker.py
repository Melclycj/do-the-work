#!/usr/bin/env python3
"""The construction-side dispatch WRITES `.harness/review-pending.json` (producer side).

The producer half of `test_dispatch_freeze_marker.py`, for the three modes round
`CORE-ONLY-CODE` moved to `tooling/construction_dispatch.py` (`core-only.plan.md` item C).
The marker is the mechanical half of `E9`'s review window: the tracked
`review_freeze_check.py` (the consumer) refuses commits while it exists, and that side is
already red-tested via `test_precommit_checks`. A dispatch that silently stopped writing the
marker would leave the window unheld while every consumer test stayed green — and the move
itself is exactly the kind of change that could have dropped the write, which is why this
file exists rather than the assertion being carried across informally.

The command is driven exactly as a dispatcher would drive it (subprocess against a real
disposable repository). The expected field set, subject form and marker path are hand-written
literals, never imported from the module under test (`E5`), and the field set is asserted
WHOLE because what the marker does not carry matters as much as what it does.
"""
from __future__ import annotations

import json
import subprocess
import sys
import unittest

import _harness
from _harness import TempRepo

MARKER = ".harness/review-pending.json"

#: The declaration the three modes derive their charter from; without one they refuse, and a
#: refusal writes no marker — which is this file's own negative control, below.
DECLARATION = json.dumps({"policy": None, "rules": ["RULES-OF-THIS-REPOSITORY.md"]}, indent=1)


def run(*argv: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, "construction_dispatch.py", *argv],
        cwd=str(_harness.TOOLING_DIR),
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )


def declared_repo() -> TempRepo:
    return TempRepo(
        {
            "a.md": "one\n",
            "harness.json": DECLARATION + "\n",
            "RULES-OF-THIS-REPOSITORY.md": "# rules\n",
        }
    )


class TheReviewSideModesWriteTheFreezeMarker(unittest.TestCase):
    """A successful review-side dispatch opens E9's window; a failed one must not."""

    def test_a_range_dispatch_writes_the_marker(self) -> None:
        with declared_repo() as repo:
            repo.write({"b.md": "two\n"})
            tip = repo.commit_all("tip")
            marker = repo.root / MARKER
            self.assertFalse(marker.exists())  # clean before: the write below is the dispatch's

            completed = run("--range", f"{repo.base}..{tip}", "--repo-root", str(repo.root))
            output = (completed.stdout or "") + (completed.stderr or "")
            self.assertEqual(completed.returncode, 0, output)
            self.assertTrue(marker.exists(), "a successful dispatch left no freeze marker")
            document = json.loads(marker.read_text(encoding="utf-8"))
            self.assertEqual(sorted(document), ["dispatched_at", "subject"])
            self.assertEqual(document["subject"], f"{repo.base}..{tip}")

    def test_a_read_dispatch_writes_the_marker(self) -> None:
        with declared_repo() as repo:
            marker = repo.root / MARKER
            self.assertFalse(marker.exists())

            completed = run("--read", repo.base, "--repo-root", str(repo.root))
            output = (completed.stdout or "") + (completed.stderr or "")
            self.assertEqual(completed.returncode, 0, output)
            document = json.loads(marker.read_text(encoding="utf-8"))
            self.assertEqual(sorted(document), ["dispatched_at", "subject"])
            self.assertEqual(document["subject"], repo.base)

    def test_a_failed_dispatch_writes_no_marker(self) -> None:
        """Negative control: the marker appears only when the dispatch derived (exit 0)."""
        with declared_repo() as repo:
            completed = run(
                "--range", f"{repo.base}..{repo.base}", "--repo-root", str(repo.root)
            )
            self.assertEqual(completed.returncode, 1)
            self.assertFalse((repo.root / MARKER).exists())

    def test_an_undeclared_repository_writes_no_marker(self) -> None:
        """Second negative control: no charter, no prompt, and so no window either."""
        with TempRepo({"a.md": "one\n"}) as repo:
            completed = run("--read", repo.base, "--repo-root", str(repo.root))
            self.assertEqual(completed.returncode, 1)
            self.assertFalse((repo.root / MARKER).exists())


class TheExecutorModeOpensNoReviewWindow(unittest.TestCase):
    """The marker is E9's REVIEW window; an executor dispatch starts precisely the work
    that window would freeze, so a successful executor dispatch must write nothing
    (round EXECUTOR-CHARTER, 2026-08-22 ruling). The range test above is this class's
    positive control: the same command, review-side, does write the marker.
    """

    def test_a_construction_executor_dispatch_writes_no_marker(self) -> None:
        with declared_repo() as repo:
            completed = run("--construction-executor", "--repo-root", str(repo.root))
            output = (completed.stdout or "") + (completed.stderr or "")
            self.assertEqual(completed.returncode, 0, output)
            self.assertFalse(
                (repo.root / MARKER).exists(),
                "a construction executor dispatch opened a review window",
            )


if __name__ == "__main__":
    unittest.main()
