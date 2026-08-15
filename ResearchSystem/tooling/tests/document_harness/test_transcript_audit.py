"""The enumerated form's mechanical coverage judgment — SIMP-A2/A3 + SIMP-B1 (2026-08-05).

What is deleted is the audit's *execution round*, not the audit: the artifact, its digest
and the START binding are untouched, and `transcript_audit` supplies the `result` and
`findings` a fresh-context agent used to supply after re-reading the frozen instruction.
So the bar these tests hold it to is the bar that walk was meeting: every numbered section
reaches an obligation, or the run stops with `SPEC_GAP` naming which one does not.

Each defect class has its own case and the conforming spec is asserted `COVERED` in the
same file, because a judgment that returns `SPEC_GAP` for everything would pass any single
negative test on its own.

The ceiling is not tested because it is not detectable here and is disclosed instead: a
faithful-restatement question — does the obligation's `requirement` say what the section
says — is FULL review's, and `transcript_audit`'s docstring says so.
"""
from __future__ import annotations

import copy
import unittest

import _harness  # noqa: F401 — installs the tooling import path

from rsclib.document_harness.enumerations import set_equality  # noqa: E402
from rsclib.document_harness.instruction import transcript_audit  # noqa: E402

PATH = "docs/instruction.md"

INSTRUCTION = """---
form: enumerated
---
# Work order — transcript audit fixture

## Requirements

### R0 — run conditions
The candidate is authored on an isolated branch rooted at the exact base.

### R1 — the carrier
A new file exists at the declared path.

### R2 — the index row
One governance-index row is added.

## Context (non-normative)

Dispatched by the user; standing discipline is in EXECUTION.md.
"""


def unit(unit_id: str, anchor: str, *, classification: str = "obligation",
         obligations: list[str] | None = None) -> dict:
    return {
        "unit_id": unit_id,
        "locator": {"path": PATH, "anchor": anchor},
        "classification": classification,
        "obligation_ids": ["ob-one"] if obligations is None else obligations,
    }


def spec_of(*units: dict) -> dict:
    return {
        "work_id": "transcript-fixture",
        "instruction_ref": {"path": PATH, "revision": "a" * 40},
        "instruction_units": list(units),
    }


COVERING = (
    unit("unit-r0", "### R0"),
    unit("unit-r1", "### R1"),
    unit("unit-r2", "### R2"),
)


class TheConformingTranscript(unittest.TestCase):
    def test_every_section_mapped_is_covered(self) -> None:
        result, findings = transcript_audit(spec_of(*COVERING), INSTRUCTION)
        self.assertEqual((result, findings), ("COVERED", ()))

    def test_a_context_unit_outside_the_sections_is_legitimate(self) -> None:
        """The dispatch paragraph's standing context-unit anchors into Context, not into a
        requirement; that is the shape EXECUTION.md prescribes, not a defect."""
        spec = spec_of(*COVERING, unit("unit-dispatch", "Dispatched by the user",
                                       classification="context", obligations=[]))
        self.assertEqual(transcript_audit(spec, INSTRUCTION)[0], "COVERED")


class TheDefectClasses(unittest.TestCase):
    def test_an_unmapped_section_stops_the_run(self) -> None:
        """The p3-corr class: normative text outside the START approval surface."""
        result, findings = transcript_audit(spec_of(*COVERING[:2]), INSTRUCTION)
        self.assertEqual(result, "SPEC_GAP")
        self.assertEqual([f["kind"] for f in findings], ["UNMAPPED_NORMATIVE_TEXT"])
        self.assertEqual(findings[0]["finding_id"], "audit-unmapped-r2")
        self.assertIn("R2", findings[0]["instruction_locator"]["anchor"])

    def test_a_broken_locator_is_named(self) -> None:
        spec = spec_of(*COVERING, unit("unit-ghost", "### R9 — never written"))
        result, findings = transcript_audit(spec, INSTRUCTION)
        self.assertEqual(result, "SPEC_GAP")
        self.assertEqual([f["kind"] for f in findings], ["BROKEN_LOCATOR"])

    def test_an_anchor_matching_two_sections_is_ambiguous(self) -> None:
        """`### R` is inside R0, R1 and R2 alike; which requirement it maps is undecided."""
        spec = spec_of(*COVERING, unit("unit-vague", "### R"))
        result, findings = transcript_audit(spec, INSTRUCTION)
        self.assertEqual(result, "SPEC_GAP")
        self.assertEqual([f["kind"] for f in findings], ["AMBIGUOUS_UNIT"])

    def test_a_requirement_section_declared_context_is_refused(self) -> None:
        """How a demand leaves the approval surface quietly: relabel it non-normative."""
        units = list(copy.deepcopy(COVERING))
        units[2]["classification"] = "context"
        result, findings = transcript_audit(spec_of(*units), INSTRUCTION)
        self.assertEqual(result, "SPEC_GAP")
        self.assertEqual({f["kind"] for f in findings},
                         {"UNJUSTIFIED_CONTEXT", "UNMAPPED_NORMATIVE_TEXT"})

    def test_a_unit_naming_no_obligation_is_refused(self) -> None:
        units = list(copy.deepcopy(COVERING))
        units[1]["obligation_ids"] = []
        result, findings = transcript_audit(spec_of(*units), INSTRUCTION)
        self.assertEqual(result, "SPEC_GAP")
        self.assertIn("MISSING_OBLIGATION_LINK", {f["kind"] for f in findings})

    def test_a_unit_anchored_outside_both_kinds_of_section_is_refused(self) -> None:
        """FULL finding f1's other leg: "outside the numbered sections" was read as
        "therefore a Context unit", so a unit anchoring an appendix — text in no requirement
        and in no Context section — was silently legitimate and the audit returned COVERED.

        The second heading is VERIFY `V-1`: `context_text` is assembled from the same
        exempt test as the form lint, so the prefix repair left this leg open in exactly the
        same way — a heading merely *opening* with the word made its text count as Context
        and the finding disappeared. The third is FULL `b1` (`v3-review-full-ca9c055.md`):
        the first two are both shapes from eras already closed, and a set built only
        backwards misses the boundary the *current* literal creates — measured, by applying
        the same slip to the new string.
        """
        for heading in (
            "Appendix A — the frozen context bindings",       # f1: contains the word
            "Contextual appendix — the frozen bindings",      # V-1: opens with it
            "Context (non-normative) — the frozen bindings",  # b1: opens with the whole title
        ):
            with self.subTest(heading=heading):
                text = INSTRUCTION.replace(
                    "## Context (non-normative)",
                    f"## {heading}\n\n"
                    "Every row above is frozen; deviating from a key here is a defect.\n\n"
                    "## Context (non-normative)",
                )
                spec = spec_of(*COVERING, unit("unit-appendix", "Every row above is frozen",
                                               classification="context", obligations=[]))
                result, findings = transcript_audit(spec, text)
                self.assertEqual(result, "SPEC_GAP")
                self.assertEqual([f["finding_id"] for f in findings],
                                 ["audit-outside-unit-appendix"])
                self.assertEqual(findings[0]["kind"], "UNJUSTIFIED_CONTEXT")

    def test_an_instruction_with_no_numbered_section_is_refused(self) -> None:
        """The vacuous shape: nothing to be a transcript of must not read as full coverage."""
        result, findings = transcript_audit(spec_of(), "# Title\n\nJust prose.\n")
        self.assertEqual(result, "SPEC_GAP")
        self.assertEqual(findings[0]["finding_id"], "audit-no-numbered-sections")


class SetEquality(unittest.TestCase):
    """The resident assertion the coverage leg is built on (SIMP-A3)."""

    def test_equal_sets_pass(self) -> None:
        self.assertTrue(set_equality(["a", "b"], ["b", "a"], subject="s").ok)

    def test_missing_and_extra_are_separate_issues(self) -> None:
        report = set_equality(["a", "c"], ["a", "b"], subject="s")
        codes = [issue.code for issue in report.issues]
        self.assertEqual(sorted(codes), ["V3-ENUM-EXTRA", "V3-ENUM-MISSING"])
        rendered = "\n".join(report.rendered())
        self.assertIn("b", rendered)
        self.assertIn("c", rendered)

    def test_two_empty_sets_are_a_failure_not_a_pass(self) -> None:
        """An extractor that stopped matching produces this exact shape."""
        report = set_equality([], [], subject="s")
        self.assertFalse(report.ok)
        self.assertEqual([issue.code for issue in report.issues], ["V3-ENUM-VACUOUS"])

    def test_one_empty_side_is_reported_as_the_difference(self) -> None:
        self.assertEqual(
            [issue.code for issue in set_equality([], ["a"], subject="s").issues],
            ["V3-ENUM-MISSING"],
        )


class NamedIssueReachability(unittest.TestCase):
    """Every code `enumerations.py` can raise is asserted by name in this file (F4).

    The partition test in `test_fix_round_locks.py` requires each package module to belong
    to a swept set; a module authored by a later round carries its own sweep, and this is
    `enumerations.py`'s. It announced itself exactly that way — the partition failed the
    moment the module was added, before this class existed.
    """

    def test_no_code_is_silent_surface(self) -> None:
        import pathlib
        import re

        from rsclib.document_harness import enumerations as E

        module_text = pathlib.Path(E.__file__).read_text(encoding="utf-8")
        declared = set(re.findall(r'f"\{CODE\}-([A-Z-]+)"', module_text))
        test_text = pathlib.Path(__file__).read_text(encoding="utf-8")
        asserted = {
            code for code in declared if f"{E.CODE}-{code}" in test_text
        }
        self.assertEqual(
            declared - asserted,
            set(),
            "codes declared in enumerations.py with no test asserting them by name",
        )
        self.assertEqual(len(declared), 3, f"code surface moved: {sorted(declared)}")


if __name__ == "__main__":
    raise SystemExit(
        unittest.main(module=None, argv=[__import__("sys").argv[0], "-v"], exit=False)
        .result.wasSuccessful()
        is False
    )
