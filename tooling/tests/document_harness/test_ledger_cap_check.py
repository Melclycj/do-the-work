#!/usr/bin/env python3
"""Acceptance matrix for `ledger_cap_check`, the ledger's own bounds (joined 2026-08-28).

Every must-fire case is paired with a clean baseline asserted first (`E4`'s negative control):
a refusal test proves nothing if the baseline also refuses. The check is driven against a
disposable repository through its `check(repo_root)` entry — the same bytes the git hook sees,
because both read the staged tree and never the worktree.

**One case here exists because the guard failed it.** `test_chinese_content_does_not_silence_the_guard`
pins the defect the first version shipped with: `subprocess(text=True)` decoded with the system
codepage, so on Windows the ledger's Chinese raised `UnicodeDecodeError` inside the reader
thread, `stdout` arrived empty, nothing parsed, and **every breach passed**. An ASCII-only
fixture would still be green today with that bug restored, which is why the fixtures below are
written in the language the real file is written in.
"""
from __future__ import annotations

import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "hooks"))

from _harness import TempRepo, git  # noqa: E402

import ledger_cap_check as cap  # noqa: E402

LEDGER = cap.LEDGER

HEADER = "# CONSTRUCTION LEDGER\n\n> 抬头散文，不是 entry。\n\n## ▶ 当前指针\n\n"


def ledger(entries: list[str]) -> str:
    return HEADER + "\n".join(entries) + "\n"


def entry(head: str, filler: int = 0) -> str:
    """One top-level entry: `- ` in column 0, continuations indented two spaces."""
    body = f"- **{head}**：一条指针。\n"
    if filler:
        body += "  " + ("填充" * (filler // 2)) + "\n"
    return body


def stage(repo: TempRepo, text: str) -> None:
    repo.write({LEDGER: text})
    git(repo.root, "add", "--", LEDGER)


class LedgerCapTests(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = TempRepo()
        self.addCleanup(self.repo.cleanup)

    # --- baselines (E4's negative control) -------------------------------------------------

    def test_a_conforming_ledger_passes(self):
        stage(self.repo, ledger([entry(f"第 {n} 条") for n in range(1, 21)]))
        self.assertEqual(cap.check(self.repo.root), 0)

    def test_an_unstaged_ledger_is_not_judged(self):
        """A commit that does not touch the ledger is none of this guard's business."""
        self.repo.write({LEDGER: ledger([entry("超长", filler=4000)])})
        git(self.repo.root, "add", "--", ".gitignore") if (self.repo.root / ".gitignore").exists() else None
        self.assertEqual(cap.check(self.repo.root), 0)

    def test_exactly_at_both_bounds_passes(self):
        """The bounds are inclusive: 2,500 characters and 20 entries pass; 2,501 and 21 do not.

        The full-size entry is placed first, never last, so no trailing newline lands inside its
        body and the assertion below measures what it says it measures.
        """
        head = "- **顶格**：一条指针。"
        exact = head + "填" * (cap.MAX_ENTRY_CHARS - len(head))
        self.assertEqual(len(exact), cap.MAX_ENTRY_CHARS)
        entries = [exact] + [entry(f"第 {n} 条") for n in range(1, 20)]
        text = ledger(entries)
        found = cap.entries(text)
        self.assertEqual(len(found), 20)
        self.assertEqual(len(found[0][1]), cap.MAX_ENTRY_CHARS)
        stage(self.repo, text)
        self.assertEqual(cap.check(self.repo.root), 0)

    def test_one_character_over_the_bound_blocks(self):
        """The paired must-fire for the case above: 2,501 is a breach."""
        head = "- **超一格**：一条指针。"
        over = head + "填" * (cap.MAX_ENTRY_CHARS + 1 - len(head))
        self.assertEqual(len(over), cap.MAX_ENTRY_CHARS + 1)
        stage(self.repo, ledger([over, entry("第二条")]))
        self.assertEqual(cap.check(self.repo.root), 1)

    # --- must fire -------------------------------------------------------------------------

    def test_one_oversized_entry_blocks(self):
        stage(self.repo, ledger([entry("正常"), entry("超长", filler=4000)]))
        self.assertEqual(cap.check(self.repo.root), 1)

    def test_too_many_entries_blocks(self):
        stage(self.repo, ledger([entry(f"第 {n} 条") for n in range(1, 22)]))
        self.assertEqual(cap.check(self.repo.root), 1)

    def test_chinese_content_does_not_silence_the_guard(self):
        """The regression that shipped in the first version — see this module's docstring.

        The payload is Chinese, so a system-codepage decode raises rather than mis-parsing. If
        the explicit `encoding="utf-8"` is ever removed, this goes green-to-red instead of the
        guard going silently permissive.
        """
        stage(self.repo, ledger([entry("中文条目要能被读到", filler=4000)]))
        self.assertEqual(cap.check(self.repo.root), 1)

    # --- the ratchet: standing debt may shrink or stand, never grow -------------------------

    def _commit_debt(self) -> str:
        """Put an over-bound entry in HEAD, so later edits meet it as standing debt."""
        debt_head = "- **历史欠账**：这条在上限收紧之前就写好了。"
        debt = debt_head + "\n  " + ("填充" * 700)
        self.assertGreater(len(debt), cap.MAX_ENTRY_CHARS)
        stage(self.repo, ledger([debt, entry("正常")]))
        git(self.repo.root, "commit", "-qm", "debt")
        return debt

    def test_standing_debt_left_alone_passes(self):
        debt = self._commit_debt()
        stage(self.repo, ledger([debt, entry("正常"), entry("新增的短条")]))
        self.assertEqual(cap.check(self.repo.root), 0)

    def test_standing_debt_that_shrinks_passes(self):
        debt = self._commit_debt()
        shorter = debt[: len(debt) - 200]
        self.assertGreater(len(shorter), cap.MAX_ENTRY_CHARS)
        stage(self.repo, ledger([shorter, entry("正常")]))
        self.assertEqual(cap.check(self.repo.root), 0)

    def test_standing_debt_that_grows_blocks(self):
        debt = self._commit_debt()
        stage(self.repo, ledger([debt + "填", entry("正常")]))
        self.assertEqual(cap.check(self.repo.root), 1)

    def test_a_new_entry_beside_standing_debt_still_meets_the_bound(self):
        """The ratchet forgives history, never the entry being written now."""
        debt = self._commit_debt()
        stage(self.repo, ledger([debt, entry("超长新条", filler=3000)]))
        self.assertEqual(cap.check(self.repo.root), 1)

    # --- the parser, which is where a silent pass would hide --------------------------------

    def test_indented_continuations_belong_to_the_entry_above(self):
        text = ledger([entry("一条", filler=100)])
        found = cap.entries(text)
        self.assertEqual(len(found), 1)
        self.assertIn("填充", found[0][1])

    def test_headings_end_an_entry(self):
        text = HEADER + entry("一条") + "\n## 待办 backlog\n\n" + entry("二条")
        self.assertEqual(len(cap.entries(text)), 2)

    def test_header_prose_is_not_an_entry(self):
        """Blockquote lines open with `>`, not `- `, so the header contributes nothing."""
        self.assertEqual(cap.entries(HEADER), [])


if __name__ == "__main__":
    unittest.main()
