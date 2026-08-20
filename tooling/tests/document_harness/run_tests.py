#!/usr/bin/env python3
"""Deterministic acceptance matrix for the Document Work Assurance Harness v3 core (V3-N1).

Covers plan §9 acceptance IDs N1-A1..N1-A11 and the three residuals V3-N0 carried forward
to this node (R1 observed-tree recording, R3 `const` vocabulary blindness, R4 governance
self-approval). The v1 and v2 suites remain separate, untouched runs; N1-A11 re-runs them
rather than importing their assertions.

Offline: no network. Every test builds its own disposable Git repository under the system
temp directory — nothing here writes into the repository under assurance.

    python tooling/tests/document_harness/run_tests.py

Exit 0 = every acceptance property held. Exit 1 = at least one regression.
"""
from __future__ import annotations

import pathlib
import sys
import unittest

TEST_DIR = pathlib.Path(__file__).resolve().parent
if str(TEST_DIR) not in sys.path:
    sys.path.insert(0, str(TEST_DIR))

import _harness  # noqa: E402,F401 — installs the tooling import path


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
