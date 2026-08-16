#!/usr/bin/env python3
"""Pre-commit: while a review or read is out, only its record may land.

The marker `.harness/review-pending.json` is written by `dtw dispatch` at the moment a
subject is handed over, and deleted by the executor in the same act that commits the
returned record. While it exists, every staged path must belong to the record families R6
names (`v3-review-full-* / v3-review-verify-* / v3-checkpoint-read-* / v3-cold-read-*`
under the migration directory) or be a product run's returned ReviewResult
(`runs/<id>/evidence/review-full.json` / `review-verify.json` — a product return is two
artifacts, and refusing the JSON half forced the first product FULL to land in two
commits; witnessed at 391db68/87938f3, routed WORKFLOW_FIX by
`user-decision-triage-e9-guard-record-vocabulary`, 2026-08-01) — anything else is the
concurrency shape E9 forbids: the branch moving while its bytes are under review.

Advisory and per-machine, bypassable with --no-verify (README "Local enforcement" row).
"""
from __future__ import annotations

import json
import pathlib
import re
import subprocess
import sys

MARKER = pathlib.Path(".harness/review-pending.json")
RECORD_DIR = "ResearchSystem/migration/document-work-assurance-v3/"
RECORD_NAME = re.compile(
    r"^v3-(review-full|review-verify|checkpoint-read|cold-read)-[0-9a-f]{7,40}\.md$"
)
#: A product run's ReviewResult — the machine half of the returned record. Exactly the
#: two review documents; every other run file (evidence, control, issues) stays refused.
PRODUCT_RESULT = re.compile(
    r"^ResearchSystem/assurance/runs/[a-z0-9][a-z0-9-]*/evidence/review-(full|verify)\.json$"
)


def staged_paths(repo_root: pathlib.Path) -> list[str]:
    out = subprocess.run(
        ["git", "-C", str(repo_root), "diff", "--cached", "--name-only"],
        check=False,
        stdout=subprocess.PIPE,
    )
    return [
        line.strip()
        for line in out.stdout.decode("utf-8", errors="replace").splitlines()
        if line.strip()
    ]


def is_record(path: str) -> bool:
    if path.startswith(RECORD_DIR) and RECORD_NAME.match(pathlib.PurePosixPath(path).name):
        return True
    return bool(PRODUCT_RESULT.match(path))


def check(repo_root: pathlib.Path) -> int:
    marker = repo_root / MARKER
    if not marker.exists():
        return 0
    try:
        pending = json.loads(marker.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        pending = {}
    offending = [p for p in staged_paths(repo_root) if not is_record(p)]
    if not offending:
        return 0
    subject = pending.get("subject", "?")
    print("pre-commit BLOCKED: a review/read is out (E9: from dispatch to its record's")
    print("commit the branch takes no commit but the record itself).")
    print(f"  marker : {marker}  (subject {subject})")
    for p in offending:
        print(f"  staged : {p}  (not a review record)")
    print("Land the returned record alone and delete the marker; or bypass with --no-verify.")
    return 1


if __name__ == "__main__":
    sys.exit(check(pathlib.Path.cwd()))
