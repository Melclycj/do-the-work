#!/usr/bin/env python3
"""`do-the-work` — the Document Work Assurance harness's command line.

The main name of the two `HD-40` §10 recorded; `dtw.py` beside it is the short alias, and
both are this same four-line shim over `rsclib.document_harness.cli.main`. Neither carries
behaviour: a name is a name, and duplicating the commands to give them a second one would be
the drift this file exists to avoid.
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
