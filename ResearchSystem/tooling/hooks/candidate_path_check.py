#!/usr/bin/env python3
"""Pre-commit: a repository path newly written into a work product must exist somewhere.

The candidate-side half of the path guard, and SIMP-A4's deliverable (recorded user ruling
2026-08-05; re-ruled 2026-08-06 after the round closed it against `form_conformance`, which
runs pre-START when no candidate yet exists and so cannot save any review time).

`layer_path_check.py` deliberately skips a token that resolves nowhere, because it *may be
illustrative*. This one takes exactly that skipped class, split by whether the token is
shorthand: a unique tracked path suffix passes, nothing anywhere blocks.
`rsclib.document_harness.paths` holds the whole decision; the two hooks keep separate rules
on purpose and share no verdict.

The two are **not** a partition of the tree, and saying so was this file's own first error:
the six Markdown instruction-layer members outside `NOT_SCANNED` are scanned by both, and
there this guard overrides the exemption the older one takes on purpose. That is intended —
an amendment is a work product, and the class the older guard waves through is exactly where
the defect this lint exists for was found — but it is a stricter rule applying on top, not a
division of territory.

Measured before it was written — four real product candidates, 47 added path tokens, 4
resolving nowhere: three shorthand, and `Thesis/literature-analysis/sota-comparison.md`
written into the A3 amendment, missed by a 25-minute independent FULL that returned seven
other findings, and signed. One fire, no false positives, on the sample that existed.

**What it does not judge is chosen by what a document IS, and then written down as a list of
places.** The first shipped form got the choosing wrong: the scope was defined by subtracting
a blacklist from "every staged Markdown file", which is wider than the *candidate* SIMP-A4
named, and the blacklist was built from a two-way split when this tree holds three kinds of
document. See `NOT_SCANNED`.

**The list is the implementation, and it is maintained by hand — that is stated here because
this file used to claim otherwise.** A document that IS a record but lives outside these
prefixes is scanned, and the failure is a *false block*: loud, not silent, but loud is the
shape that earns a hook bypass, which is this file's own argument for the specification
surface. Measured instance (2026-08-06, run `p5b-claims`): the P5B batch inventory record
under `ResearchSystem/inventory/amendments/` drew four blocks — three control-plane documents
correctly absent from the candidate branch, and one the non-existent path the record exists to
report. That prefix was already carrying records of the same kind when this list was drawn
(`2026-08-02-p5a-shells.md`), so the omission was an oversight rather than an unforeseeable
location; it is added rather than answered with new machinery, per E6. Adding a record kind in
a new place owes an entry here.

Advisory and per-machine, bypassable with --no-verify (README "Local enforcement" row).
"""
from __future__ import annotations

import pathlib
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from rsclib.document_harness.paths import (  # noqa: E402
    TrackedPaths,
    staged_added_lines,
    unresolved_path_tokens,
)

#: A **record** reports on other text, so it quotes the broken path it is reporting.
#: Scanning one blocks the returned review record, and `E9`'s freeze window admits only that
#: record — leaving no legal commit ordering, which is the deadlock rider `freeze-audit`
#: banks.
RECORD_SURFACE = (
    "ResearchSystem/migration/",
    "ResearchSystem/document-harness/journal/",
    "ResearchSystem/inventory/amendments/",
    "ResearchSystem/HARNESS-LEDGER.md",
    "ResearchSystem/HARNESS-LEDGER-archive.md",
    "ResearchSystem/HARNESS-RIDERS.md",
    "ResearchSystem/HARNESS-DECISIONS-archive.md",
    ".goals/LEDGER.md",
    ".goals/LEDGER-archive.md",
)

#: A **specification** names the files the candidate is *required to create*, so at freeze
#: time they cannot exist — a run's instruction and its control plane. This is the class the
#: first form missed, and it is not a near-miss: replayed over this repository's history, 5
#: of the 6 instruction freezes would have been blocked, on the ordinary R1 sentence "A new
#: file `…` exists". The harness already draws the line elsewhere — run-v2's pre-freeze
#: reconciliation checks an instruction's enumerations against the tree **and** the
#: WorkSpec's `write_scope`, and in-write-scope-but-not-yet-in-tree is the legitimate cell.
#: A lint that blocks the normal opening move of every run is one that gets `--no-verify`'d
#: on first contact, after which it protects nothing.
SPECIFICATION_SURFACE = ("ResearchSystem/assurance/runs/",)

#: Vendored documentation, skipped for the ordinary reason: its `folder/note.md`
#: placeholders are not this repository's paths to resolve.
VENDORED = (".claude/", ".agents/")

#: Prefixes match by path start; an entry ending in `/` is a whole tree. What remains after
#: these three is the **work product** — a candidate, an amendment, a design note — where a
#: path resolving nowhere is a defect and this guard is the point.
NOT_SCANNED = RECORD_SURFACE + SPECIFICATION_SURFACE + VENDORED


def scanned(path: str) -> bool:
    """Every staged Markdown file outside the three surfaces of `NOT_SCANNED`."""
    return path.endswith(".md") and not path.startswith(NOT_SCANNED)


def check(repo_root: pathlib.Path) -> int:
    # `core.quotepath=off`: git otherwise C-quotes any path with a byte outside ASCII, so
    # `Thesis/笔记/note.md` arrives as `"Thesis/\347\254\224\350\256\260/note.md"` — quotes
    # included, no longer ending in `.md`, silently dropped by `scanned()` along with every
    # token in it. A silence, not an error, so nothing would have announced it.
    staged = subprocess.run(
        ["git", "-C", str(repo_root), "-c", "core.quotepath=off",
         "diff", "--cached", "--name-only"],
        check=False,
        stdout=subprocess.PIPE,
    ).stdout.decode("utf-8", errors="replace")
    targets = [line.strip() for line in staged.splitlines() if scanned(line.strip())]
    if not targets:
        return 0
    tracked = TrackedPaths.from_index(repo_root)
    failures: list[tuple[str, str]] = []
    for path in targets:
        text = "\n".join(staged_added_lines(repo_root, path))
        failures += [(path, token) for token in unresolved_path_tokens(tracked, path, text)]
    if not failures:
        return 0
    print("pre-commit BLOCKED: newly written text names a repository path that exists nowhere:")
    for path, token in failures:
        print(f"  {path}: `{token}`")
    print("Fix the path as written, or bypass with --no-verify.")
    return 1


if __name__ == "__main__":
    sys.exit(check(pathlib.Path.cwd()))
