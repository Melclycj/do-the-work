"""Instruction form resolution — SIMP-C1 / SIMP-C2 / SIMP-B3 (2026-08-05).

The branch these tests guard decides which derived artifacts a run owes: under the
`enumerated` form the paragraph map and the preamble gate have no object, under `prose`
they do. A wrong answer in the cheap direction silently narrows the START approval surface,
so every negative here asserts the *defect class* and every one of them is paired with a
control showing the conforming shape passes.

The rule under test is structural, not a tone sniff: prose lives inside a numbered `R<n>`
section or inside Context, and nothing else. Its stated ceiling — an unmarked normative
declarative inside Context — is not testable here because it is not detectable at all; the
backstop is FULL review's instruction re-walk, and `form_conformance`'s docstring says so.
"""
from __future__ import annotations

import unittest

import _harness  # noqa: F401 — installs the tooling import path

from rsclib.document_harness.instruction import (  # noqa: E402
    FORM_ENUMERATED,
    FORM_PROSE,
    declared_form,
    form_conformance,
    numbered_sections,
    resolve_form,
)

CONFORMING = """---
form: enumerated
---
# Work order — a conforming enumerated instruction

## Requirements

### R0 — run conditions
The candidate is authored on an isolated branch rooted at the exact base.

### R1 — the carrier
A new file exists at the declared path.

## Context (non-normative)

Standing run-conduct discipline appears by reference: EXECUTION.md governs it.
"""


#: Headings that mention or open with the word but are not the Context section, each paired
#: with why it is in the set. Hand-written literals rather than anything derived from the
#: module (`E5`), and a set rather than one entry because `E7` asks for the defect class and
#: the read's `O-1` recorded that the earlier test pinned a single instance of it.
NOT_THE_CONTEXT_SECTION = (
    ("Contextual appendix — the frozen bindings", "V-1: opens with it, one word later than f1"),
    ("Context bindings for the frozen shells", "V-1: opens with it"),
    ("CONTEXTUALISED requirements addendum", "V-1: opens with it, upper case"),
    ("Additional context", "VERIFY O-1: refused all along, bound by nothing until here"),
    ("Appendix A — the frozen context bindings", "f1: the original instance"),
    ("Context (non-normative) — the frozen bindings",
     "FULL b1: the new literal's own boundary — opens with the whole exempt title"),
    ("Context", "the bare heading: exempt through both earlier eras, refused since the "
                "exact form — a behaviour change nothing else records"),
)


def _without(text: str, block: str) -> str:
    assert block in text, block
    return text.replace(block, "")


class Declaration(unittest.TestCase):
    def test_the_declaration_is_read_from_frontmatter(self) -> None:
        self.assertEqual(declared_form(CONFORMING), "enumerated")

    def test_no_frontmatter_is_no_declaration(self) -> None:
        self.assertIsNone(declared_form("# Work order\n\nBody.\n"))

    def test_a_quoted_declaration_is_the_same_declaration(self) -> None:
        self.assertEqual(declared_form(CONFORMING.replace("form: enumerated",
                                                          'form: "enumerated"')),
                         "enumerated")

    def test_a_body_mention_is_not_a_declaration(self) -> None:
        """Scoped to the frontmatter block: a document explaining the form does not declare
        it — the same scoping rule `frontmatter_keys` carries for governance fields."""
        self.assertIsNone(declared_form("# Work order\n\nThis run uses form: enumerated.\n"))


class NumberedSections(unittest.TestCase):
    def test_labels_and_order(self) -> None:
        self.assertEqual([s["label"] for s in numbered_sections(CONFORMING)], ["R0", "R1"])

    def test_a_section_ends_where_the_next_same_level_heading_starts(self) -> None:
        r0, r1 = numbered_sections(CONFORMING)
        self.assertEqual(r0["end_line"], r1["start_line"] - 1)

    def test_the_last_section_ends_at_the_next_higher_heading_not_at_eof(self) -> None:
        """`## Context` closes `### R1`; a section running to EOF would swallow Context and
        make the outside-blocks check vacuous."""
        r1 = numbered_sections(CONFORMING)[-1]
        lines = CONFORMING.splitlines()
        self.assertTrue(lines[r1["end_line"]].startswith("## Context"))

    def test_a_prose_instruction_has_none(self) -> None:
        self.assertEqual(numbered_sections("# Title\n\n## Task\n\nDo the thing.\n"), ())


class Conformance(unittest.TestCase):
    def test_the_conforming_shape_raises_nothing(self) -> None:
        self.assertEqual(form_conformance(CONFORMING), ())

    def test_prose_outside_every_section_is_caught(self) -> None:
        """The w1-r1 / p4-bridge defect class: a normative preamble paragraph that no
        obligation can be a transcript of."""
        text = CONFORMING.replace(
            "## Requirements",
            "**Run conditions (normative).** Nothing is promoted without FINAL.\n\n"
            "## Requirements",
        )
        issues = form_conformance(text)
        self.assertTrue(any("FORM-BLOCK-OUTSIDE-SECTIONS" in issue for issue in issues), issues)

    def test_a_normative_marker_inside_context_is_caught(self) -> None:
        text = CONFORMING.replace(
            "Standing run-conduct discipline appears by reference: EXECUTION.md governs it.",
            "The executor MUST re-run the battery before freezing.",
        )
        issues = form_conformance(text)
        self.assertTrue(any("FORM-NORMATIVE-IN-CONTEXT" in issue for issue in issues), issues)

    def test_a_heading_that_merely_mentions_context_is_not_the_context_section(self) -> None:
        """FULL finding f1 (`v3-review-full-3657687.md`), the round's one blocker.

        The exempt test was `"context" in title`, so an appendix carrying a normative frozen
        table passed as non-normative — and passing is what switches off the paragraph map
        and the preamble gate, the two artifacts that would have enumerated it. One word in
        a heading was the whole difference. The reviewer's own measurement is why this test
        exists and is not a repair of an existing one: the tightening left all 595 tests
        green, so nothing had ever asserted it.
        """
        text = CONFORMING.replace(
            "## Context (non-normative)",
            "## Appendix A — the frozen context bindings\n\n"
            "Every row above is frozen; a shell that deviates from a key here is a defect.\n\n"
            "## Context (non-normative)",
        )
        issues = form_conformance(text)
        self.assertTrue(any("FORM-BLOCK-OUTSIDE-SECTIONS" in issue for issue in issues), issues)
        self.assertEqual(resolve_form(text)[0], FORM_PROSE)

    def test_no_heading_but_the_context_section_itself_is_exempt(self) -> None:
        """VERIFY `V-1` (`v3-review-verify-c7fb720.md`) — the class f1 named, closed.

        f1's repair matched a *prefix*, so `## Contextual appendix — the frozen bindings`
        carrying the same frozen table went on resolving to `enumerated` with the paragraph
        map and the preamble gate switched off: f1's failure mode verbatim, one word of the
        heading later, and the docstring's own claim that anything else falls to prose was
        measured false a second time.

        **The set is written forwards as well as backwards** (FULL `b1`,
        `v3-review-full-ca9c055.md`). Its first five shapes came only from the two eras
        already closed, which is not the class: the reviewer applied the *same*
        substring→prefix slip to the *new* literal — `startswith("context (non-normative)")`
        — and `## Context (non-normative) — the frozen bindings` over a normative frozen
        table passed with the whole battery green. A sweep that only knows the defects it
        has already seen is a sweep the next repair walks straight past, so the boundary the
        current literal creates is pinned here too, and so is the bare heading, whose
        refusal is a real behaviour change from both earlier eras that nothing else records.
        """
        for heading, why in NOT_THE_CONTEXT_SECTION:
            with self.subTest(heading=heading):
                text = CONFORMING.replace(
                    "## Context (non-normative)",
                    f"## {heading}\n\n"
                    "Every row above is frozen; a shell that deviates from a key here is "
                    "a defect.\n\n"
                    "## Context (non-normative)",
                )
                issues = form_conformance(text)
                outside = [
                    issue for issue in issues
                    if issue.startswith("FORM-BLOCK-OUTSIDE-SECTIONS")
                ]
                self.assertEqual(len(outside), 1, (why, issues))
                self.assertIn(repr(heading), outside[0])
                self.assertEqual(resolve_form(text)[0], FORM_PROSE)

    def test_the_real_context_heading_still_passes(self) -> None:
        """Negative control: all seven real instructions head it exactly this way, so the
        tightening must cost the conforming vocabulary nothing."""
        self.assertEqual(form_conformance(CONFORMING), ())
        self.assertIn("## Context (non-normative)", CONFORMING)

    def test_the_context_section_stays_exempt_however_it_is_cased(self) -> None:
        """The one variation the exact form deliberately keeps, pinned as a decision.

        Case is tolerated because a shouted heading is still that section and no defect
        shape turns on it. Asserted so the tolerance is a choice a reviewer can challenge,
        rather than an unexamined leftover of the `casefold` the prefix form happened to
        use.
        """
        for heading in ("Context (non-normative)", "CONTEXT (NON-NORMATIVE)"):
            with self.subTest(heading=heading):
                text = CONFORMING.replace("## Context (non-normative)", f"## {heading}")
                self.assertEqual(form_conformance(text), ())
                self.assertEqual(resolve_form(text), (FORM_ENUMERATED, ()))

    def test_a_declaration_with_no_numbered_section_is_caught(self) -> None:
        text = "---\nform: enumerated\n---\n# Work order\n\n## Task\n\nDo the thing.\n"
        issues = form_conformance(text)
        self.assertTrue(any("FORM-NO-NUMBERED-SECTIONS" in issue for issue in issues), issues)

    def test_a_duplicated_label_is_caught(self) -> None:
        """Two R1s make 'one section, one obligation' undecidable, which is how a missing
        requirement hides behind a present one (the p5b `chk-open` shape, f5)."""
        text = CONFORMING.replace("### R0 — run conditions", "### R1 — run conditions")
        issues = form_conformance(text)
        self.assertTrue(any("FORM-DUPLICATE-SECTION" in issue for issue in issues), issues)

    def test_headings_alone_are_structure_not_content(self) -> None:
        """Negative control for the outside-blocks rule: `## Requirements` sits outside both
        section kinds and must not be reported, or the conforming shape could never pass."""
        self.assertIn("## Requirements", CONFORMING)
        self.assertEqual(form_conformance(CONFORMING), ())


class Resolution(unittest.TestCase):
    def test_conforming_resolves_enumerated_with_no_notes(self) -> None:
        self.assertEqual(resolve_form(CONFORMING), (FORM_ENUMERATED, ()))

    def test_undeclared_resolves_prose(self) -> None:
        form, notes = resolve_form("# Work order\n\n## Task\n\nDo the thing.\n")
        self.assertEqual(form, FORM_PROSE)
        self.assertTrue(notes)

    def test_a_misspelled_declaration_resolves_prose(self) -> None:
        form, _ = resolve_form(CONFORMING.replace("form: enumerated", "form: enumarated"))
        self.assertEqual(form, FORM_PROSE)

    def test_a_declaration_the_structure_does_not_bear_out_resolves_prose(self) -> None:
        """Fail-heavy: the claim is refused, not the run — the run simply owes the prose
        form's artifacts, and the reasons are carried out with the answer."""
        text = CONFORMING.replace(
            "## Requirements",
            "**Run conditions (normative).** Nothing is promoted without FINAL.\n\n"
            "## Requirements",
        )
        form, notes = resolve_form(text)
        self.assertEqual(form, FORM_PROSE)
        self.assertTrue(any("FORM-BLOCK-OUTSIDE-SECTIONS" in note for note in notes), notes)

    def test_a_third_kind_of_section_flips_the_answer(self) -> None:
        """Only two kinds of section can hold prose. A `## Notes` heading is neither, and
        text under it is exactly the shape that sits in no obligation while looking filed."""
        text = CONFORMING.replace(
            "## Context (non-normative)",
            "## Notes\n\nThe base was re-rooted once; see the ledger.\n\n"
            "## Context (non-normative)",
        )
        form, notes = resolve_form(text)
        self.assertEqual(form, FORM_PROSE)
        self.assertTrue(any("FORM-BLOCK-OUTSIDE-SECTIONS" in note for note in notes), notes)

    def test_trailing_prose_belongs_to_the_last_numbered_section(self) -> None:
        """Pinned because it is a semantic, not an oversight: with the Context heading gone
        the text after R1 falls inside R1's span, so R1's obligation is a transcript of it.
        It is covered, not orphaned — the defect class here is text no obligation reaches,
        and this is not an instance of it."""
        text = _without(CONFORMING, "## Context (non-normative)\n")
        self.assertEqual(resolve_form(text), (FORM_ENUMERATED, ()))
        r1 = numbered_sections(text)[-1]
        self.assertIn("Standing run-conduct discipline",
                      "\n".join(text.splitlines()[r1["start_line"] - 1 : r1["end_line"]]))


if __name__ == "__main__":
    raise SystemExit(
        unittest.main(module=None, argv=[__import__("sys").argv[0], "-v"], exit=False)
        .result.wasSuccessful()
        is False
    )
