"""Shared plumbing for the V3-N2 test matrix.

The disposable-Git-repository mechanism is **imported from the V3-N1 suite rather than
copied**. It is pure mechanism — `TempRepo` and a `git` wrapper — and duplicating a hundred
lines of it here would mean two harnesses that drift, with the second one quietly testing a
slightly different notion of "a candidate commit" than the first. The coupling is deliberate
and narrow: V3-N1 is closed, so the imported mechanism is stable, and N2 reads it without
writing it.

It is loaded **by explicit file path under a distinct module name**, not by adding N1's test
directory to `sys.path`. Both suites name their plumbing `_harness`, so a path-based import
would resolve to whichever directory came first — this file would import itself in one order
and shadow N1's suite in the other. Binding the file directly makes the ambiguity
unrepresentable rather than order-dependent.

Fixtures are deliberately NOT centralized, following the same rule N1 set: each test builds
the exact document it is making a claim about, so a reader sees the defect being demonstrated
instead of chasing a shared factory.

Nothing in this matrix may write into the repository under assurance — every repository is a
fresh temporary directory, and an out-of-boundary write by the suite would itself violate the
node's change boundary.
"""
from __future__ import annotations

import importlib.util
import pathlib
import sys

TEST_DIR = pathlib.Path(__file__).resolve().parent
RS_ROOT = TEST_DIR.parents[2]
TOOLING_DIR = RS_ROOT / "tooling"
N1_HARNESS_PATH = TOOLING_DIR / "tests" / "document_harness" / "_harness.py"

if str(TOOLING_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLING_DIR))


def _load_n1_harness():
    """Load the V3-N1 plumbing under an unambiguous module name."""
    if not N1_HARNESS_PATH.is_file():
        raise RuntimeError(
            f"the V3-N1 test mechanism is missing at {N1_HARNESS_PATH}; this suite imports it "
            "rather than copying it"
        )
    spec = importlib.util.spec_from_file_location("v3n1_harness", N1_HARNESS_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules.setdefault("v3n1_harness", module)
    spec.loader.exec_module(module)
    return module


_n1 = _load_n1_harness()

TempRepo = _n1.TempRepo
git = _n1.git

__all__ = ["N1_HARNESS_PATH", "RS_ROOT", "TOOLING_DIR", "TempRepo", "git"]
