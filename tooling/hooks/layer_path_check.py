#!/usr/bin/env python3
"""Pre-commit: a repository path written into instruction text must resolve.

Backstop for the defect class the `dcced4e` read banked and `d322816` paid — a pack path
written so that it does not resolve. Until round `DE-PREFIX` this check knew only two
prefix-shaped classes (a broken `ResearchSystem/`-absolute token, and a token missing that
prefix), which round `XREPO-REFS`'s FULL measured as blind to the class's central shape: a
token that resolves nowhere in this repository at all, which is how a caller-held path reads
(`v3-review-full-dd18226.md` B-1; taught here under `HD-50` R3, the same round that removed
the prefix both old branches were shaped around). One class is flagged now, and nothing else:

- a backtick path token that resolves neither from the repo root nor from the file's own
  directory. Resolution that escapes the repository root does not count — through a caller's
  mount, an escaping token is exactly another repository's bytes.

A `.harness/` token is exempt: a run-time marker this repository itself writes counts as
resolving whether or not it exists at rest (E10). A token carrying a placeholder segment
(`<run-id>`, `<control root>`) is invisible to this check — the path shape it matches admits
no angle brackets — so placeholder-form locations are held by E10's clause, not here
(`v3-cold-read-4410899.md` L-2). Semantic assertions are E3's territory, not this script's.
Runs only on staged instruction-layer files, and only on the lines the staged diff ADDS: the
defect class is a path newly written (both `dcced4e` and `d322816` were), and a pre-existing
token elsewhere in the file is not this batch's to repair (`v3-review-full-8ec4c60.md` B1) —
the standing stock the guard never re-scans is likewise the clause's, not this script's. The
member list mirrors E10's membership sentence.

Advisory and per-machine, bypassable with --no-verify (README "Local enforcement" row).
"""
from __future__ import annotations

import pathlib
import re
import subprocess
import sys

#: Mirrors E10's membership sentence. Drift here is caught by the next layer read.
LAYER = (
    "document-harness/CONSTRUCTION-CHECKLIST.md",
    "document-harness/README.md",
    "document-harness/EXECUTION.md",
    "document-harness/REVIEW.md",
    "document-harness/ORCHESTRATION.md",
    "migration/document-work-assurance-v3/v3-harness-operating-contract.md",
    "migration/document-work-assurance-v3/v3-harness-review-contract.md",
    "contract/Document-Work-Assurance-Contract-v3-supersession-1.md",
    "contract/Document-Work-Assurance-Contract-v3-supersession-2.md",
    "schema/document-assurance-v3/paragraph-map.schema.json",
)

TOKEN = re.compile(r"`([^`\s]+)`")
PATHLIKE = re.compile(r"^[A-Za-z0-9_.\-/]+(?:\.(?:md|py|json|yaml|yml|txt|js)|/)$")

#: Run-time markers this repository itself writes; they count as resolving at rest (E10).
RUNTIME_PREFIX = ".harness/"


def unresolved_tokens(
    repo_root: pathlib.Path, layer_path: str, text: str
) -> list[tuple[str, str]]:
    root = repo_root.resolve()
    file_dir = (repo_root / layer_path).parent
    bad: list[tuple[str, str]] = []
    for token in TOKEN.findall(text):
        if "/" not in token or not PATHLIKE.match(token):
            continue
        if token.startswith(RUNTIME_PREFIX):
            continue
        resolved = False
        for base in (repo_root, file_dir):
            candidate = (base / token).resolve()
            if candidate.exists() and candidate.is_relative_to(root):
                resolved = True
                break
        if not resolved:
            bad.append(
                (token, "resolves nowhere in this repository — name the artifact and its holder instead")
            )
    return bad


def added_lines_by_path(repo_root: pathlib.Path) -> dict[str, list[str]]:
    """Added lines of the whole staged diff, keyed by post-image path — all this guard scans.

    `-M` follows staged renames: without it a moved member's whole standing text reads as
    added lines, which re-scans exactly the stock the E10 clause says this guard never
    re-scans — the DE-PREFIX candidate was blocked by its own frozen supersessions that way.
    One un-pathspec'd diff, because limiting the diff to the new path filters the old path
    out and breaks the very rename pairing `-M` exists to make.

    Header detection is textual and has a residual ambiguity no parse of `-U0` output can
    remove (FULL `v3-review-full-39a21a8.md` B-2): an added line whose own CONTENT opens
    `++ ` renders as `+++ …` — `++ b/x` mis-files the lines after it, any other `++ …`
    silences them. A pasted diff header (content `+++ …`, rendering `++++ …`) is handled:
    the header branches require a space in fourth position, which four plusses fail.
    """
    out = subprocess.run(
        ["git", "-C", str(repo_root), "-c", "diff.noprefix=false",
         "diff", "--cached", "-M", "-U0"],
        check=False,
        stdout=subprocess.PIPE,
    )
    added: dict[str, list[str]] = {}
    current: str | None = None
    for line in out.stdout.decode("utf-8", errors="replace").splitlines():
        if line.startswith("+++ b/"):
            current = line[len("+++ b/"):]
        elif line.startswith("+++ "):
            current = None
        elif line.startswith("+") and current is not None:
            added.setdefault(current, []).append(line[1:])
    return added


def check(repo_root: pathlib.Path) -> int:
    added = added_lines_by_path(repo_root)
    failures: list[tuple[str, str, str]] = []
    for layer_path in LAYER:
        if layer_path not in added:
            continue
        text = "\n".join(added[layer_path])
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
