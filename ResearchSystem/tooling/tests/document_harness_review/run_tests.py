#!/usr/bin/env python3
"""Deterministic acceptance matrix for bounded review, repair and disposition (V3-N2).

Covers plan §9 acceptance IDs N2-A1..N2-A11, plus the two residuals this node inherited:
N0-R2 (terminal status/pointer conditionals, landing as N2-A7) and N1-R2 (nothing obliged a
run to include the R4 governance scan, landing in `flow.py`).

The V3-N1 matrix stays a separate, untouched run. This suite never re-asserts N1's
properties — N1's own signature and its independent VERIFY cover them, and re-verifying
`instruction.check_audit` or `assurance_state.resume` here was explicitly withdrawn when
residual N1-R1 was discharged.

Offline: no network. Every test that needs a repository builds its own disposable one under
the system temp directory; nothing here writes into the repository under assurance.

    python ResearchSystem/tooling/tests/document_harness_review/run_tests.py

Exit 0 = every acceptance property held. Exit 1 = at least one regression.
"""
from __future__ import annotations

import pathlib
import sys
import unittest

TEST_DIR = pathlib.Path(__file__).resolve().parent
if str(TEST_DIR) not in sys.path:
    sys.path.insert(0, str(TEST_DIR))

import _harness  # noqa: E402,F401 — installs the tooling and V3-N1 mechanism import paths


def build_suite() -> unittest.TestSuite:
    loader = unittest.TestLoader()
    return loader.discover(str(TEST_DIR), pattern="test_*.py", top_level_dir=str(TEST_DIR))


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(build_suite())
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
