#!/usr/bin/env python3
"""Pre-commit: a repository path newly written into a work product must exist somewhere.

The candidate-side half of the path guard, and SIMP-A4's deliverable (recorded user ruling
2026-08-05; re-ruled 2026-08-06 after the round closed it against `form_conformance`, which
runs pre-START when no candidate yet exists and so cannot save any review time).

How this lint and the instruction-layer guard (`layer_path_check.py`) divide the work is
stated once, in the *Local enforcement* row of `document-harness/README.md` (ruled
2026-08-20); this docstring does not restate it. Local to this file: it reads work products,
splits the nowhere-resolving class by whether the token is shorthand — a unique tracked path
suffix passes — and `rsclib.document_harness.paths` holds the whole decision.

The count of instruction-layer members this lint also scans is deliberately not written
here — it was "six" from `SIMP-A4` until 2026-08-19 and went stale the moment
`ORCHESTRATION.md` became the tenth member, with nothing to notice (`v3-cold-read-c22e229.md`
`O-2`). Compute it instead:
`[p for p in layer_path_check.LAYER if candidate_path_check.scanned(p)]` — 7 at
`2026a14`; 9 at `2538893`, the schema member being the only one `scanned()`'s `.md` test
drops.

Measured before it was written — four real product candidates, 47 added path tokens, 4
resolving nowhere: three shorthand, and `Thesis/literature-analysis/sota-comparison.md`
written into the A3 amendment, missed by a 25-minute independent FULL that returned seven
other findings, and signed. One fire, no false positives, on the sample that existed.

**What it does not judge is chosen by what a document IS, and then written down as a list of
places.** The first shipped form got the choosing wrong: the scope was defined by subtracting
a blacklist from "every staged Markdown file", which is wider than the *candidate* SIMP-A4
named, and the blacklist was built from a two-way split when this tree holds three kinds of
document. See `not_scanned`.

**The record and specification surfaces are the CALLER's declaration, not this file's
list** (round STRANGER-GUARDS; rider `chk-caller-prefixes`). Until then they were two
hard-coded tuples of the first caller's directory names, so any caller whose records lived
elsewhere had them scanned as work products — and a record quoting the broken path it
reports is then *blocked*: loud, not silent, but loud is the shape that earns a hook
bypass, which is this file's own argument for the specification surface. The surfaces now
come from `.harness/scan-surfaces.json` (`rsclib.document_harness.caller`; `dtw init`
writes the defaults), and a caller with no declaration gets defaults covering the layout
`init` creates. The maintenance lesson stands under the new carrier — measured instance
(2026-08-06, run `p5b-claims`): the P5B batch inventory record under the first caller's
`inventory/amendments/` tree drew four blocks — three control-plane documents correctly
absent from the candidate branch, and one the non-existent path the record exists to
report. That tree was already carrying records of the same kind when the then-list was
drawn, so the omission was an oversight rather than an unforeseeable location; it was added
rather than answered with new machinery, per E6. Adding a record kind in a new place owes
the caller's declaration an entry.

Advisory and per-machine, bypassable with --no-verify (README "Local enforcement" row).
"""
from __future__ import annotations

import pathlib
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from rsclib.document_harness.caller import (  # noqa: E402
    DEFAULTS,
    ScanSurfaces,
    SurfaceDeclarationError,
    load_scan_surfaces,
)
from rsclib.document_harness.paths import (  # noqa: E402
    TrackedPaths,
    staged_added_lines,
    unresolved_path_tokens,
)

#: The three surface kinds and why each is exempt — the semantics live here, their
#: *locations* in the caller's declaration (`caller.ScanSurfaces`):
#:
#: * A **record** reports on other text, so it quotes the broken path it is reporting.
#:   Scanning one blocks the returned review record, and `E9`'s freeze window admits only
#:   that record — leaving no legal commit ordering, which is the deadlock rider
#:   `freeze-audit` banks.
#: * A **specification** names the files the candidate is *required to create*, so at
#:   freeze time they cannot exist — a run's instruction and its control plane. This is the
#:   class the first form missed, and it is not a near-miss: replayed over the first
#:   caller's history, 5 of the 6 instruction freezes would have been blocked, on the
#:   ordinary R1 sentence "A new file `…` exists". The harness already draws the line
#:   elsewhere — run-v2's pre-freeze reconciliation checks an instruction's enumerations
#:   against the tree **and** the WorkSpec's `write_scope`, and
#:   in-write-scope-but-not-yet-in-tree is the legitimate cell. A lint that blocks the
#:   normal opening move of every run is one that gets `--no-verify`'d on first contact,
#:   after which it protects nothing.
#:
#: Vendored documentation stays this file's own constant — its `folder/note.md`
#: placeholders are not any repository's paths to resolve, whoever the caller is.
VENDORED = (".claude/", ".agents/")


def not_scanned(surfaces: ScanSurfaces = DEFAULTS) -> tuple[str, ...]:
    """The exempt prefixes: the caller's three surfaces plus vendored documentation.

    Prefixes match by path start; an entry ending in `/` is a whole tree. What remains
    after them is the **work product** — a candidate, an amendment, a design note — where a
    path resolving nowhere is a defect and this guard is the point.
    """
    return (
        surfaces.record
        + surfaces.review_record_dirs
        + surfaces.specification
        + VENDORED
    )


def scanned(path: str, surfaces: ScanSurfaces = DEFAULTS) -> bool:
    """Every staged Markdown file outside the surfaces of `not_scanned`."""
    return path.endswith(".md") and not path.startswith(not_scanned(surfaces))


def check(repo_root: pathlib.Path) -> int:
    try:
        surfaces = load_scan_surfaces(repo_root)
    except SurfaceDeclarationError as exc:
        print(f"pre-commit BLOCKED: {exc}")
        print(
            "Fix the declaration as declared; this guard never falls back to defaults "
            "silently."
        )
        return 1
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
    targets = [
        line.strip() for line in staged.splitlines() if scanned(line.strip(), surfaces)
    ]
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
