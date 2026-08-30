#!/usr/bin/env python3
"""F-3r — `dtw dispatch` actually WRITES `.harness/review-pending.json` (producer side).

The freeze marker is the mechanical half of E9's review window: the tracked
`review_freeze_check.py` (the consumer) refuses commits while the marker exists, and that
side is already red-tested via `test_precommit_checks`. Until this file nothing bound the
PRODUCER — a dispatch that silently stopped writing the marker would leave the window
unheld while every consumer test stayed green. Rider F-3r (source:
`v3-review-full-8ec4c60.md` F-3), redeemed in Phase D, the batch that touched `rsc.py` —
the file the six commands lived in until the split batch's R2 moved them to `dtw.py`.

The command is driven exactly as a dispatcher would drive it (subprocess against a real
disposable repository), following `test_review_cli_v2_subject.py`. The expected field set,
subject form and marker path are hand-written literals, never imported from the module under
test (E5).

The range and read modes this file drove until round `CORE-ONLY-CODE` left the command with
their module (`core-only.plan.md` item C); their half of this matrix is
`test_construction_dispatch_freeze_marker.py`. What remains here is the product run's own
pair: the review mode, which writes the marker, and the executor mode, which must not.

The field set is asserted WHOLE rather than key by key, because the property that matters is
as much what the marker does not carry as what it does. It carried a `kind` until 2026-08-07,
derived from which flag was typed rather than from what was dispatched, so a product run
forced onto `--range` was labelled a construction round; the field was deleted, and asserting
the exact set is what stops one growing back unnoticed.
"""
from __future__ import annotations

import json
import subprocess
import sys
import unittest

import _harness
from _harness import TempRepo
from test_review_v2_subject import build_scenario

MARKER = ".harness/review-pending.json"


def run_dispatch(*argv: str) -> subprocess.CompletedProcess:
    """Drive the real command, exactly as a dispatcher would (the point of this suite)."""
    return subprocess.run(
        [sys.executable, "dtw.py", "dispatch", *argv],
        cwd=str(_harness.TOOLING_DIR),
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )


class TheDispatchWritesTheFreezeMarker(unittest.TestCase):
    """A successful dispatch opens E9's window by writing the marker; a failed one must not."""

    def test_a_product_review_dispatch_writes_the_marker(self) -> None:
        scn = build_scenario()
        marker = scn.repo.root / MARKER
        self.assertFalse(marker.exists())  # clean before: the write below is the dispatch's

        completed = run_dispatch(
            "--subject", scn.evidence_commit, "--repo-root", str(scn.repo.root)
        )
        output = (completed.stdout or "") + (completed.stderr or "")
        self.assertEqual(completed.returncode, 0, output)
        self.assertTrue(marker.exists(), "a successful dispatch left no freeze marker")
        document = json.loads(marker.read_text(encoding="utf-8"))
        self.assertEqual(sorted(document), ["dispatched_at", "subject"])
        self.assertEqual(document["subject"], scn.evidence_commit)

    def test_a_failed_dispatch_writes_no_marker(self) -> None:
        """Negative control: the marker appears only when the dispatch derived (exit 0)."""
        with TempRepo({"a.md": "one\n"}) as repo:
            completed = run_dispatch(
                "--subject", repo.base, "--repo-root", str(repo.root)
            )
            self.assertEqual(completed.returncode, 1)
            self.assertFalse((repo.root / MARKER).exists())


class AnExecutorDispatchOpensNoReviewWindow(unittest.TestCase):
    """The marker is E9's REVIEW window; an executor dispatch starts precisely the work
    that window would freeze, so a successful executor dispatch must write nothing
    (round EXECUTOR-CHARTER, 2026-08-22 ruling). The review test above is this class's
    positive control: the same command, review-side, does write the marker.
    """

    def test_a_product_executor_dispatch_writes_no_marker(self) -> None:
        with TempRepo({"assurance/runs/run-one/instruction.md": "# Task\n"}) as repo:
            completed = run_dispatch(
                "--executor", "assurance/runs/run-one", "--repo-root", str(repo.root)
            )
            output = (completed.stdout or "") + (completed.stderr or "")
            self.assertEqual(completed.returncode, 0, output)
            self.assertFalse(
                (repo.root / MARKER).exists(),
                "a product executor dispatch opened a review window",
            )


if __name__ == "__main__":
    unittest.main()
