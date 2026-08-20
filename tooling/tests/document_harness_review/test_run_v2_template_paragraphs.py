"""Run-v2 authoring gate — the paragraph-map three-way cross-check (M11, Phase C4).

The defect class (p3-corr, `issue-p3-corr` family): the unit map was hand-picked, so a
normative paragraph the map missed was invisible — the coverage audit judged COVERED
anyway. The mechanical fix pinned here: the gate refuses a run whose paragraph map is
missing, stale against the instruction bytes, bound to another instruction, or
unclassified; refuses an obligation-classified paragraph no instruction unit anchors
into; and reports a unit whose anchor lands in no enumerated paragraph. The preamble
rule of W2-A5 is retained un-loosened.

RED evidence (2026-07-31, pasted in document-harness/journal/c4-2026-07-31.md): the
main-level tests fail AT VALUE against the pre-C4 template — the old gate exits 0 over
the uncovered / stale / missing-map instances — while the pure-core tests error on the
then-absent `paragraph_map_issues`. The passing tests are the negative controls.
"""
from __future__ import annotations

import contextlib
import copy
import hashlib
import importlib.util
import io
import json
import pathlib
import tempfile
import unittest

from _harness import RS_ROOT  # noqa: F401 — sys.path side effect included

TEMPLATE_DIR = RS_ROOT / "assurance" / "templates" / "run-v2"

FAKE_REV = "f" * 40

INSTRUCTION = (
    "# Task instruction\n"
    "\n"
    "Run condition: the candidate stays on its isolated branch.\n"
    "\n"
    "## Task\n"
    "\n"
    "Write the guide.\n"
    "\n"
    "Every claim in the guide must cite its source note.\n"
)
# five paragraphs, one per non-blank line: 1 · 3 · 5 · 7 · 9. Paragraph 5 (line 9) is the
# p3-corr shape: normative text the unit map below does not anchor.


def load_template(name: str, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, TEMPLATE_DIR / name)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


GATE = load_template("check_template_instance.py", "c4_template_gate")


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def spec_of() -> dict:
    return {
        "schema_version": "2",
        "work_id": "run-c4",
        "instruction_ref": {"path": "docs/instruction.md", "revision": FAKE_REV},
        "instruction_units": [
            {"unit_id": "unit-preamble",
             "locator": {"path": "docs/instruction.md", "anchor": "Run condition:"},
             "classification": "obligation", "obligation_ids": ["ob-one"]},
            {"unit_id": "unit-task",
             "locator": {"path": "docs/instruction.md", "anchor": "Write the guide."},
             "classification": "obligation", "obligation_ids": ["ob-one"]},
        ],
    }


_ROWS = (
    (1, 1, "# Task instruction"),
    (3, 3, "Run condition: the candidate stays on its isolated branch."),
    (5, 5, "## Task"),
    (7, 7, "Write the guide."),
    (9, 9, "Every claim in the guide must cite its source note."),
)


def map_of(*classifications: str) -> dict:
    """Hand-written map entries (E5): lines counted by hand, digests via hashlib."""
    return {
        "schema_version": "1",
        "work_id": "run-c4",
        "instruction_ref": {"path": "docs/instruction.md", "revision": FAKE_REV},
        "paragraphs": [
            {"index": i + 1, "start_line": start, "end_line": end,
             "digest_sha256": sha(text), "classification": cls}
            for i, ((start, end, text), cls) in enumerate(zip(_ROWS, classifications))
        ],
    }


COVERED = ("context", "obligation", "context", "obligation", "context")
UNCOVERED = ("context", "obligation", "context", "obligation", "obligation")


def run_gate(spec: dict, paragraph_map: dict | None, *, drop_map: bool = False,
             instruction: str = INSTRUCTION):
    """Materialize a run dir + worktree instruction on disk; run main; capture (exit, out)."""
    with tempfile.TemporaryDirectory(prefix="c4gate-") as tmp:
        tmp_path = pathlib.Path(tmp)
        run_dir = tmp_path / "runs" / "run-c4"
        (run_dir / "control").mkdir(parents=True)
        (run_dir / "control" / "work-spec.json").write_text(
            json.dumps(spec), encoding="utf-8")
        if not drop_map:
            (run_dir / "control" / "paragraph-map.json").write_text(
                json.dumps(paragraph_map), encoding="utf-8")
        (tmp_path / "docs").mkdir()
        (tmp_path / "docs" / "instruction.md").write_text(instruction, encoding="utf-8")
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = GATE.main(["check_template_instance.py", str(run_dir), str(tmp_path)])
        return code, out.getvalue()


class GateRefusesTheOmission(unittest.TestCase):
    """Main-level, value-red against the pre-C4 template (old gate exits 0 over these)."""

    def test_an_obligation_paragraph_no_unit_anchors_is_refused(self):
        code, out = run_gate(spec_of(), map_of(*UNCOVERED))
        self.assertEqual(code, 1)
        self.assertIn("TEMPLATE-PARAGRAPH-UNCOVERED", out)

    def test_a_missing_paragraph_map_is_refused(self):
        code, out = run_gate(spec_of(), None, drop_map=True)
        self.assertEqual(code, 1)
        self.assertIn("TEMPLATE-PARAGRAPH-MAP-MISSING", out)

    def test_a_stale_map_is_refused(self):
        stale = map_of(*COVERED)
        stale["paragraphs"][4]["digest_sha256"] = "0" * 64
        code, out = run_gate(spec_of(), stale)
        self.assertEqual(code, 1)
        self.assertIn("TEMPLATE-PARAGRAPH-MAP-STALE", out)

    # --- negative controls: green before AND after the upgrade ---

    def test_a_covered_and_classified_run_passes(self):
        code, out = run_gate(spec_of(), map_of(*COVERED))
        self.assertEqual(code, 0)
        self.assertIn("authoring gate: PASS", out)

    def test_an_obligation_paragraph_with_a_unit_anchor_passes(self):
        spec = spec_of()
        spec["instruction_units"].append(
            {"unit_id": "unit-cite",
             "locator": {"path": "docs/instruction.md",
                         "anchor": "must cite its source note"},
             "classification": "obligation", "obligation_ids": ["ob-one"]})
        code, _ = run_gate(spec, map_of(*UNCOVERED))
        self.assertEqual(code, 0)

    def test_the_preamble_rule_is_retained_unloosened(self):
        # Classify every preamble paragraph context so the new checks are silent; drop the
        # preamble-anchoring unit. W2-A5's rule must still refuse (red pre-C4 would mean
        # the rule was loosened — this is a retention control, green before and after).
        spec = spec_of()
        spec["instruction_units"] = [
            u for u in spec["instruction_units"] if u["unit_id"] != "unit-preamble"]
        m = map_of("context", "context", "context", "obligation", "context")
        code, out = run_gate(spec, m)
        self.assertEqual(code, 1)
        self.assertIn("TEMPLATE-PREAMBLE-UNMAPPED", out)


ENUMERATED = (
    "---\n"
    "form: enumerated\n"
    "---\n"
    "# Task instruction\n"
    "\n"
    "## Requirements\n"
    "\n"
    "### R0 — run conditions\n"
    "The candidate stays on its isolated branch.\n"
    "\n"
    "### R1 — the guide\n"
    "Write the guide, and every claim in it cites its source note.\n"
    "\n"
    "## Context (non-normative)\n"
    "\n"
    "Standing run-conduct discipline appears by reference: EXECUTION.md governs it.\n"
)


def enumerated_spec() -> dict:
    spec = spec_of()
    spec["instruction_units"] = [
        {"unit_id": "unit-r0",
         "locator": {"path": "docs/instruction.md", "anchor": "### R0"},
         "classification": "obligation", "obligation_ids": ["ob-one"]},
        {"unit_id": "unit-r1",
         "locator": {"path": "docs/instruction.md", "anchor": "### R1"},
         "classification": "obligation", "obligation_ids": ["ob-two"]},
    ]
    return spec


class EnumeratedFormSkipsTheDerivedLegs(unittest.TestCase):
    """SIMP-B1 (2026-08-05): under the enumerated form the paragraph map and the preamble
    gate have no object, so the gate stops demanding them — and stops only then.

    Every case here is paired: the skip is asserted against the same run that would be
    refused under the prose form, so a test that passed because the gate stopped checking
    altogether would show up in the second half."""

    def test_no_paragraph_map_is_needed(self):
        code, out = run_gate(enumerated_spec(), None, drop_map=True, instruction=ENUMERATED)
        self.assertEqual(code, 0, out)
        self.assertIn("instruction form   : enumerated", out)
        self.assertIn("paragraph map skipped", out)
        self.assertNotIn("TEMPLATE-PARAGRAPH-MAP-MISSING", out)

    def test_the_same_run_without_the_declaration_is_refused(self):
        """The control: identical instruction bytes minus the frontmatter — the map is owed
        again, so the pass above is the declaration doing the work, not the gate going
        quiet."""
        code, out = run_gate(enumerated_spec(), None, drop_map=True,
                             instruction=ENUMERATED.split("---\n", 2)[2])
        self.assertEqual(code, 1)
        self.assertIn("instruction form   : prose", out)
        self.assertIn("TEMPLATE-PARAGRAPH-MAP-MISSING", out)

    def test_a_declaration_the_structure_does_not_bear_out_is_refused(self):
        """Fail-heavy end to end: a normative preamble under an `enumerated` declaration
        resolves to prose, and the run owes the artifacts again."""
        broken = ENUMERATED.replace(
            "## Requirements",
            "**Run conditions (normative).** Nothing is promoted without FINAL.\n\n"
            "## Requirements")
        code, out = run_gate(enumerated_spec(), None, drop_map=True, instruction=broken)
        self.assertEqual(code, 1)
        self.assertIn("FORM-BLOCK-OUTSIDE-SECTIONS", out)
        self.assertIn("TEMPLATE-PARAGRAPH-MAP-MISSING", out)

    def test_the_v2_mandate_still_applies(self):
        """The one leg both forms owe: skipping is scoped to the two derived artifacts."""
        spec = enumerated_spec()
        del spec["schema_version"]
        code, out = run_gate(spec, None, drop_map=True, instruction=ENUMERATED)
        self.assertEqual(code, 1)
        self.assertIn("TEMPLATE-SPEC-NOT-V2", out)


class PureCoreThreeWay(unittest.TestCase):
    """The pure function over data — no filesystem, skeleton passed in by the caller."""

    def derived(self) -> list[dict]:
        from rsclib.document_harness.instruction import paragraph_skeleton
        return list(paragraph_skeleton(INSTRUCTION))

    def test_the_covered_instance_is_clean(self):
        issues = GATE.paragraph_map_issues(
            spec_of(), INSTRUCTION, map_of(*COVERED), self.derived())
        self.assertEqual(issues, [])

    def test_an_entry_with_no_classification_is_refused_not_defaulted(self):
        m = map_of(*COVERED)
        del m["paragraphs"][1]["classification"]
        issues = GATE.paragraph_map_issues(spec_of(), INSTRUCTION, m, self.derived())
        self.assertTrue(any("TEMPLATE-PARAGRAPH-UNCLASSIFIED" in i for i in issues))

    def test_a_dropped_entry_is_stale(self):
        m = map_of(*COVERED)
        m["paragraphs"].pop(2)
        issues = GATE.paragraph_map_issues(spec_of(), INSTRUCTION, m, self.derived())
        self.assertTrue(any("TEMPLATE-PARAGRAPH-MAP-STALE" in i for i in issues))

    def test_a_map_bound_to_another_instruction_is_refused(self):
        m = map_of(*COVERED)
        m["instruction_ref"]["revision"] = "0" * 40
        issues = GATE.paragraph_map_issues(spec_of(), INSTRUCTION, m, self.derived())
        self.assertTrue(
            any("TEMPLATE-PARAGRAPH-MAP-INSTRUCTION-MISMATCH" in i for i in issues))

    def test_a_dangling_unit_anchor_is_reported(self):
        spec = spec_of()
        spec["instruction_units"].append(
            {"unit_id": "unit-ghost",
             "locator": {"path": "docs/instruction.md",
                         "anchor": "text that appears nowhere"},
             "classification": "obligation", "obligation_ids": ["ob-one"]})
        issues = GATE.paragraph_map_issues(
            spec, INSTRUCTION, map_of(*COVERED), self.derived())
        self.assertTrue(any("TEMPLATE-UNIT-ANCHOR-DANGLING" in i for i in issues))

    def test_a_stale_map_suppresses_coverage_judgments(self):
        # Coverage judged over bytes the map does not match would be meaningless; the
        # binding legs answer first and alone.
        m = map_of(*UNCOVERED)
        m["paragraphs"][0]["digest_sha256"] = "0" * 64
        issues = GATE.paragraph_map_issues(spec_of(), INSTRUCTION, m, self.derived())
        self.assertTrue(any("TEMPLATE-PARAGRAPH-MAP-STALE" in i for i in issues))
        self.assertFalse(any("TEMPLATE-PARAGRAPH-UNCOVERED" in i for i in issues))


class MakeParagraphMap(unittest.TestCase):
    """The generator writes every derived column; classification is left to the human."""

    @classmethod
    def setUpClass(cls):
        cls.maker = load_template("make_paragraph_map.py", "c4_map_maker")

    def run_maker(self, *, pre_existing: str | None = None):
        with tempfile.TemporaryDirectory(prefix="c4make-") as tmp:
            tmp_path = pathlib.Path(tmp)
            run_dir = tmp_path / "runs" / "run-c4"
            (run_dir / "control").mkdir(parents=True)
            (run_dir / "control" / "work-spec.json").write_text(
                json.dumps(spec_of()), encoding="utf-8")
            map_path = run_dir / "control" / "paragraph-map.json"
            if pre_existing is not None:
                map_path.write_text(pre_existing, encoding="utf-8")
            (tmp_path / "docs").mkdir()
            (tmp_path / "docs" / "instruction.md").write_text(
                INSTRUCTION, encoding="utf-8")
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                code = self.maker.main(
                    ["make_paragraph_map.py", str(run_dir), str(tmp_path)])
            content = map_path.read_text(encoding="utf-8") if map_path.exists() else None
            return code, out.getvalue(), content

    def test_generates_the_skeleton_with_classification_left_to_the_human(self):
        code, _, content = self.run_maker()
        self.assertEqual(code, 0)
        document = json.loads(content)
        self.assertEqual(document["schema_version"], "1")
        self.assertEqual(document["work_id"], "run-c4")
        self.assertEqual(document["instruction_ref"],
                         {"path": "docs/instruction.md", "revision": FAKE_REV})
        for entry in document["paragraphs"]:
            self.assertNotIn("classification", entry)
        from rsclib.document_harness.instruction import paragraph_skeleton
        self.assertEqual(document["paragraphs"],
                         [dict(entry) for entry in paragraph_skeleton(INSTRUCTION)])

    def test_refuses_to_overwrite_an_existing_map(self):
        sentinel = '{"sentinel": true}'
        code, out, content = self.run_maker(pre_existing=sentinel)
        self.assertEqual(code, 1)
        self.assertIn("PARAGRAPH-MAP-EXISTS", out)
        self.assertEqual(content, sentinel)


if __name__ == "__main__":
    unittest.main()
