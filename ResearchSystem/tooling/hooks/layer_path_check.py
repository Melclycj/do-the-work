#!/usr/bin/env python3
"""Pre-commit: a repository path written into instruction text must resolve.

Backstop for the defect class the `dcced4e` read banked and `d322816` paid — a pack path
written without its `ResearchSystem/` prefix. Two mechanically decidable classes are
flagged, and nothing else:

- a backtick token starting with `ResearchSystem/` that does not resolve from the repo
  root (a broken absolute-convention path);
- a backtick token that resolves from neither the repo root nor the file's own directory
  but does resolve under `ResearchSystem/` (the missing-prefix class).

Tokens resolvable nowhere at all are skipped — they may be illustrative — and semantic
assertions are E3's territory, not this script's. Runs only on staged instruction-layer
files, and only on the lines the staged diff ADDS: the defect class is a path newly
written (both `dcced4e` and `d322816` were), and a pre-existing token elsewhere in the
file is not this batch's to repair (`v3-review-full-8ec4c60.md` B1). The member list
mirrors E10's membership sentence.

Advisory and per-machine, bypassable with --no-verify (README "Local enforcement" row).
"""
from __future__ import annotations

import pathlib
import re
import subprocess
import sys

#: Mirrors E10's membership sentence. Drift here is caught by the next layer read.
LAYER = (
    "ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md",
    "ResearchSystem/document-harness/README.md",
    "ResearchSystem/document-harness/EXECUTION.md",
    "ResearchSystem/document-harness/REVIEW.md",
    "ResearchSystem/document-harness/ORCHESTRATION.md",
    "ResearchSystem/migration/document-work-assurance-v3/v3-harness-operating-contract.md",
    "ResearchSystem/migration/document-work-assurance-v3/v3-harness-review-contract.md",
    "ResearchSystem/contract/Document-Work-Assurance-Contract-v3-supersession-1.md",
    "ResearchSystem/contract/Document-Work-Assurance-Contract-v3-supersession-2.md",
    "ResearchSystem/schema/document-assurance-v3/paragraph-map.schema.json",
)

TOKEN = re.compile(r"`([^`\s]+)`")
PATHLIKE = re.compile(r"^[A-Za-z0-9_.\-/]+(?:\.(?:md|py|json|yaml|yml|txt|js)|/)$")


def unresolved_tokens(
    repo_root: pathlib.Path, layer_path: str, text: str
) -> list[tuple[str, str]]:
    file_dir = (repo_root / layer_path).parent
    bad: list[tuple[str, str]] = []
    for token in TOKEN.findall(text):
        if "/" not in token or not PATHLIKE.match(token):
            continue
        from_root = (repo_root / token).exists()
        from_dir = (file_dir / token).exists()
        under_rs = (repo_root / "ResearchSystem" / token).exists()
        if token.startswith("ResearchSystem/"):
            if not from_root:
                bad.append((token, "does not resolve from the repo root"))
        elif not from_root and not from_dir and under_rs:
            bad.append((token, "resolves only under ResearchSystem/ — prefix missing"))
    return bad


def added_lines(repo_root: pathlib.Path, path: str) -> list[str]:
    """The lines the staged diff adds for one path — the only lines this guard scans."""
    out = subprocess.run(
        ["git", "-C", str(repo_root), "diff", "--cached", "-U0", "--", path],
        check=False,
        stdout=subprocess.PIPE,
    )
    return [
        line[1:]
        for line in out.stdout.decode("utf-8", errors="replace").splitlines()
        if line.startswith("+") and not line.startswith("+++")
    ]


def check(repo_root: pathlib.Path) -> int:
    staged = subprocess.run(
        ["git", "-C", str(repo_root), "diff", "--cached", "--name-only"],
        check=False,
        stdout=subprocess.PIPE,
    ).stdout.decode("utf-8", errors="replace")
    staged_set = {line.strip() for line in staged.splitlines() if line.strip()}
    failures: list[tuple[str, str, str]] = []
    for layer_path in LAYER:
        if layer_path not in staged_set:
            continue
        text = "\n".join(added_lines(repo_root, layer_path))
        failures += [
            (layer_path, token, why)
            for token, why in unresolved_tokens(repo_root, layer_path, text)
        ]
    if not failures:
        return 0
    print("pre-commit BLOCKED: newly added instruction text names a repository path that does not resolve:")
    for path, token, why in failures:
        print(f"  {path}: `{token}` — {why}")
    print("Fix the path as written, or bypass with --no-verify.")
    return 1


if __name__ == "__main__":
    sys.exit(check(pathlib.Path.cwd()))
