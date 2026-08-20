"""Paragraph skeleton + paragraph-map schema — the mechanical half of M11 (Phase C4).

p3-corr's coverage audit returned COVERED over a hand-picked unit map that had silently
missed three normative units; nothing enumerated the instruction, so the omission was
invisible. `paragraph_skeleton` makes the enumeration mechanical: every block of the
frozen instruction is listed with its exact lines and content digest, so a paragraph can
be misclassified but never silently absent.

Expectations here are hand-written literals (E5): line numbers are counted by hand and
digests come from an independent `hashlib` call over hand-selected text — never from
calling the function under test twice.
"""
from __future__ import annotations

import copy
import hashlib
import unittest

import _harness  # noqa: F401 — sys.path side effect only

from rsclib.document_harness import validate
from rsclib.document_harness.instruction import paragraph_skeleton


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


SIMPLE = "# Title\n\nFirst paragraph\nsecond line.\n\nSecond paragraph.\n"
# lines: 1 '# Title' · 2 blank · 3-4 the two-line paragraph · 5 blank · 6 'Second paragraph.'


class ParagraphSkeleton(unittest.TestCase):
    def test_blocks_split_on_blank_lines_with_one_based_inclusive_lines(self):
        self.assertEqual(
            paragraph_skeleton(SIMPLE),
            (
                {"index": 1, "start_line": 1, "end_line": 1,
                 "digest_sha256": sha("# Title")},
                {"index": 2, "start_line": 3, "end_line": 4,
                 "digest_sha256": sha("First paragraph\nsecond line.")},
                {"index": 3, "start_line": 6, "end_line": 6,
                 "digest_sha256": sha("Second paragraph.")},
            ),
        )

    def test_blank_lines_inside_a_backtick_fence_do_not_split(self):
        text = "Intro.\n\n```python\na = 1\n\nb = 2\n```\n\nOutro.\n"
        # lines: 1 Intro. · 2 blank · 3-7 the fenced block (blank line 5 inside) · 8 blank · 9 Outro.
        self.assertEqual(
            paragraph_skeleton(text),
            (
                {"index": 1, "start_line": 1, "end_line": 1,
                 "digest_sha256": sha("Intro.")},
                {"index": 2, "start_line": 3, "end_line": 7,
                 "digest_sha256": sha("```python\na = 1\n\nb = 2\n```")},
                {"index": 3, "start_line": 9, "end_line": 9,
                 "digest_sha256": sha("Outro.")},
            ),
        )

    def test_a_tilde_fence_closes_only_on_a_run_at_least_as_long(self):
        text = "~~~~\nfirst\n\n~~~\n\nstill inside\n~~~~\n\nAfter.\n"
        # opening run of four; the three-tilde line at 4 must NOT close it; line 7 does.
        self.assertEqual(
            paragraph_skeleton(text),
            (
                {"index": 1, "start_line": 1, "end_line": 7,
                 "digest_sha256": sha("~~~~\nfirst\n\n~~~\n\nstill inside\n~~~~")},
                {"index": 2, "start_line": 9, "end_line": 9,
                 "digest_sha256": sha("After.")},
            ),
        )

    def test_an_unclosed_fence_runs_to_the_end_of_the_text(self):
        text = "Intro.\n\n```\ncode\n\nmore\n"
        self.assertEqual(
            paragraph_skeleton(text),
            (
                {"index": 1, "start_line": 1, "end_line": 1,
                 "digest_sha256": sha("Intro.")},
                {"index": 2, "start_line": 3, "end_line": 6,
                 "digest_sha256": sha("```\ncode\n\nmore")},
            ),
        )

    def test_a_four_space_indented_marker_is_not_a_fence(self):
        text = "para\n    ```\n\nnext\n"
        # were the indented run a fence, the blank at line 3 would not split.
        self.assertEqual(
            paragraph_skeleton(text),
            (
                {"index": 1, "start_line": 1, "end_line": 2,
                 "digest_sha256": sha("para\n    ```")},
                {"index": 2, "start_line": 4, "end_line": 4,
                 "digest_sha256": sha("next")},
            ),
        )

    def test_empty_and_blank_only_text_yield_no_paragraphs(self):
        self.assertEqual(paragraph_skeleton(""), ())
        self.assertEqual(paragraph_skeleton("\n\n  \n"), ())

    def test_text_without_a_trailing_newline_is_enumerated(self):
        self.assertEqual(
            paragraph_skeleton("One"),
            ({"index": 1, "start_line": 1, "end_line": 1, "digest_sha256": sha("One")},),
        )


GOOD_MAP = {
    "schema_version": "1",
    "work_id": "run-one",
    "instruction_ref": {"path": "docs/instruction.md", "revision": "a" * 40},
    "paragraphs": [
        {"index": 1, "start_line": 1, "end_line": 1,
         "digest_sha256": "0" * 64, "classification": "obligation"},
    ],
}


class ParagraphMapSchema(unittest.TestCase):
    def test_a_complete_map_validates(self):
        self.assertTrue(validate("paragraph_map", GOOD_MAP).ok)

    def test_an_entry_without_classification_is_rejected(self):
        bad = copy.deepcopy(GOOD_MAP)
        del bad["paragraphs"][0]["classification"]
        self.assertFalse(validate("paragraph_map", bad).ok)

    def test_a_classification_outside_the_enum_is_rejected(self):
        bad = copy.deepcopy(GOOD_MAP)
        bad["paragraphs"][0]["classification"] = "normative"
        self.assertFalse(validate("paragraph_map", bad).ok)

    def test_a_parallel_result_array_is_unrepresentable(self):
        # The ⑤ lesson: results live on the enumerated entry, never in a sibling array.
        bad = copy.deepcopy(GOOD_MAP)
        bad["classifications"] = ["obligation"]
        self.assertFalse(validate("paragraph_map", bad).ok)

    def test_a_version_less_map_is_rejected(self):
        bad = copy.deepcopy(GOOD_MAP)
        del bad["schema_version"]
        self.assertFalse(validate("paragraph_map", bad).ok)


if __name__ == "__main__":
    unittest.main()
