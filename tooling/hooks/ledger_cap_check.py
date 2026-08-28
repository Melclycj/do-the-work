#!/usr/bin/env python3
"""Pre-commit guard: this repository's construction ledger stays within its own bounds.

`CONSTRUCTION-LEDGER.md`'s header states them: **every top-level entry <= 1,000 characters
(user ruling 2026-08-28, down from 2,500 the same week), and <= 20 top-level entries**.

**It is a ratchet, not a sweep.** An entry written or rewritten must meet the bound; an entry
that already breached it carries a standing debt this guard does not call in, because trimming
one means re-reading the batch it records — the user ruled those are trimmed when a round next
touches them. Growing such an entry is refused. Six entries stood in debt the day the bound
moved, every one of them a batch narrative written where a pointer belongs.

**Why a machine at all.** The header used to end this rule with "Discipline only, no machine
enforces it here", and gave two reasons. Both were measured false on 2026-08-28 and the user
ruled the guard in:

* *"A second checker would be new machinery"* — it is not a second one. A `ledger_cap_check.py`
  existed here until 2026-08-12, when batch B R3 moved it to the caller side, pinned there to
  the caller's own ledger, on the ground that a ledger is the caller's concern (io-design §5).
  **This repository acquired a ledger of its own seven days later** (2026-08-19, round
  `LEDGER-SPLIT`), and no machine followed it. For this file the count of checkers was zero,
  not one.
* *"for a file with one writer"* — a single writer is exactly what discipline failed to
  restrain. Measured in one session on 2026-08-28: three separate breaches, at 3,231, 2,815
  and 2,582 characters, each found only because the writer stopped to measure by hand. The
  bound is not the kind of thing a writer notices while writing prose.

**Why per-entry characters and not lines.** The header's own 2026-08-26 reasoning: the roll of
closed batches was a single line of 17,128 characters, and a line-count bound cannot see growth
that never adds a line.

**Both `git` calls decode as UTF-8 explicitly.** Without it `text=True` decodes with the system
codepage, and on Windows (cp936) the ledger's Chinese raises `UnicodeDecodeError` inside
subprocess's reader thread — `stdout` arrives empty, no entry parses, and the guard passes
everything. That is not hypothetical: it is what the first version of this file did, caught by
the mutation test the same hour it was written (`E4`). Same defect class as the GBK decode fixed
in round `PUB-FACADE`.

**What this does not judge.** Whether the content *belongs* in a ledger at all — the header
admits only the current pointer and construction-side rulings with no other home — is a
reading, not a measurement, and stays with the independent review. A short entry full of
narrative passes here. That ceiling is stated rather than left to be inferred (`E5`: this
guard's expectation is the header's two numbers, written here by hand, never read back out of
the file it guards).
"""
from __future__ import annotations

import pathlib
import re
import subprocess
import sys

#: The ledger this guards. One path, decidable by inspection — the caller keeps its own ledger
#: and its own machine (io-design §5), and this guard never looks outside this repository.
LEDGER = "CONSTRUCTION-LEDGER.md"

#: `CONSTRUCTION-LEDGER.md`'s header, hand-written here (`E5`). Changing the header without
#: changing these is a drift this guard cannot see; the header names the numbers, and the two
#: sites are kept in step by the round that edits either.
#:
#: 1,000 since 2026-08-28 (user ruling), down from the 2,500 of 2026-08-26. The measurement that
#: moved it: of the twenty entries standing that day, fourteen were already under 700 and the
#: current-pointer entry was 390, while every entry over 1,000 was diagnosed as the same defect
#: — a batch's narrative written where a pointer belongs. The bound is what a pointer costs, not
#: what the longest entry happens to be.
MAX_ENTRY_CHARS = 1000
MAX_ENTRIES = 20

#: A top-level entry opens with "- " in column 0. Continuation lines are indented and belong to
#: the entry above; a heading or a horizontal rule ends the run.
_ENTRY_START = re.compile(r"^- ")
_BLOCK_END = re.compile(r"^(#|---|历史轮次)")


def staged_ledger(repo_root: pathlib.Path) -> str | None:
    """The ledger as it is STAGED, not as it sits in the worktree.

    The same posture as the other hooks here: what the commit will contain is what is judged,
    so an unstaged edit neither rescues a breach nor causes one.
    """
    listed = subprocess.run(
        ["git", "-C", str(repo_root), "diff", "--cached", "--name-only", "--", LEDGER],
        capture_output=True, text=True, encoding="utf-8", errors="replace", check=False,
    )
    if listed.returncode != 0 or not listed.stdout.strip():
        return None
    blob = subprocess.run(
        ["git", "-C", str(repo_root), "show", f":{LEDGER}"],
        capture_output=True, text=True, encoding="utf-8", errors="replace", check=False,
    )
    return blob.stdout if blob.returncode == 0 else None


def entries(text: str) -> list[tuple[int, str]]:
    """Top-level entries as (1-based start line, full text including continuations)."""
    found: list[tuple[int, str]] = []
    current: list[str] | None = None
    start = 0
    for number, line in enumerate(text.split("\n"), 1):
        if _ENTRY_START.match(line):
            if current is not None:
                found.append((start, "\n".join(current)))
            current, start = [line], number
        elif current is not None:
            if _BLOCK_END.match(line):
                found.append((start, "\n".join(current)))
                current = None
            else:
                current.append(line)
    if current is not None:
        found.append((start, "\n".join(current)))
    return found


def committed_sizes(repo_root: pathlib.Path) -> dict[str, int]:
    """Each entry's size in `HEAD`, keyed by its opening line.

    Empty when the ledger is new to the tree, which makes every entry new and therefore held
    to the bound outright — the correct reading for a file that has no history to inherit.
    Duplicate opening lines keep the smallest size, so a ratchet can never be loosened by an
    ambiguity.
    """
    show = subprocess.run(
        ["git", "-C", str(repo_root), "show", f"HEAD:{LEDGER}"],
        capture_output=True, text=True, encoding="utf-8", errors="replace", check=False,
    )
    if show.returncode != 0:
        return {}
    sizes: dict[str, int] = {}
    for _, body in entries(show.stdout):
        key = body.split("\n")[0]
        sizes[key] = min(len(body), sizes.get(key, len(body)))
    return sizes


def check(repo_root: pathlib.Path) -> int:
    text = staged_ledger(repo_root)
    if text is None:
        return 0

    found = entries(text)
    before = committed_sizes(repo_root)
    breaches: list[str] = []

    # A ratchet, not a sweep. An entry written or rewritten under the bound must meet it; an
    # entry that already breached it is a standing debt this guard does not call in — the user
    # ruled on 2026-08-28 that existing over-long entries are trimmed when a round next touches
    # them, never in a batch of their own, because trimming one means re-reading the batch it
    # records. What the ratchet forbids is making that debt worse.
    for start, body in found:
        size = len(body)
        head = body.split("\n")[0]
        was = before.get(head)
        label = head[2:62].strip()

        if was is not None and was > MAX_ENTRY_CHARS:
            if size > was:
                breaches.append(
                    f"  {LEDGER}:{start} — entry was already over the bound at {was:,} "
                    f"characters and this commit makes it {size:,}. Standing debt may be "
                    f"reduced or left alone, never grown: {label}…"
                )
            continue

        if size > MAX_ENTRY_CHARS:
            verb = "is now" if was is not None else "is"
            breaches.append(
                f"  {LEDGER}:{start} — entry {verb} {size:,} characters, bound is "
                f"{MAX_ENTRY_CHARS:,} (over by {size - MAX_ENTRY_CHARS:,}): {label}…"
            )

    if len(found) > MAX_ENTRIES:
        breaches.append(
            f"  {LEDGER} — {len(found)} top-level entries, bound is {MAX_ENTRIES}"
        )

    if not breaches:
        return 0

    print(f"ledger cap: {LEDGER} is over its own stated bounds.")
    print("\n".join(breaches))
    print(
        "\nThe bounds are the ledger's own (header, user ruling 2026-08-26): a ledger holds\n"
        "pointers, not reasoning. The remedy is to move detail to where it belongs — a journal\n"
        "(not bound to a round since 2026-08-28), the round's plan, the commit body, or the\n"
        "review record — never to compress meaning out of a live pointer. Oldest CLOSED\n"
        "material may be relocated verbatim to CONSTRUCTION-LEDGER-archive.md."
    )
    return 1


if __name__ == "__main__":
    sys.exit(check(pathlib.Path.cwd()))
