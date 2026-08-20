#!/usr/bin/env python3
"""`dtw` — the short alias of `do-the-work.py`, the same entry under the shorter name.

Both shims call `rsclib.document_harness.cli.main`; neither carries behaviour (`HD-40` §10:
one entry, two names). Type whichever is less to type.
"""
from __future__ import annotations

import pathlib
import sys

_HERE = pathlib.Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

from rsclib.document_harness.cli import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
