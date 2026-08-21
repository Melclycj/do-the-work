#!/usr/bin/env python3
"""RunPreview — the deterministic pre-START rendering of a run's frozen control plane.

Written by round PREVIEW-RENDER, executing the 2026-08-21 ruling that the human-readable
form of a product run's authorization — the START card — is rendered by script from the
plane's own bytes, never assembled by a session. What these tests bind is the honesty of
that substitution:

* **the bytes the user approves appear verbatim** — the numbered sections and the host
  table are the plane's own lines, not a summary of them;
* **the one section that is non-normative by its own heading is named, never rendered** —
  Context inside the approval surface would put non-binding prose in front of a signature;
* **the digests are recomputed, never copied** — the preview embeds the digest of the bytes
  on disk, so a stale plane cannot borrow a fresh plane's rendering;
* **incompleteness is loud** — a missing core file is a SpecGap naming every absentee, a
  missing check spec is a marked row and a nonzero exit, and a plan that binds a different
  WorkSpec than the bytes on disk says MISMATCH instead of rendering the wrong candidate
  invisibly (the same wrong-candidate visibility ObligationCoverage exists for);
* **rendering twice yields identical bytes** — which is what makes "re-derive instead of
  store" honest.

Fixtures are built per test-class from hand-written literals (E5): the marker strings the
assertions grep for exist only here, so a preview that satisfies them by echoing its own
constants has no way to know them.
"""
from __future__ import annotations

import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

import _harness  # noqa: F401  — sys.path side effect

from rsclib.document_harness import SpecGap, canonical_digest, validate, write_canonical
from rsclib.document_harness import preview as v3_preview

INSTRUCTION = """---
form: enumerated
---

# Work order — fixture (run `fx-run`)

## Context (non-normative)

CONTEXT-BODY-MARKER must never appear in a rendered preview.

## R0 — the boundary

Only `docs/target.md` changes; THE-BOUND-SENTENCE lands verbatim.

## R1 — the judged half

The claim is supportable only by reading.
"""

HOST_TABLE = "| host | HOST-TABLE-MARKER |\n"

#: The layout the FULL of 57d1312 (B-2) measured being swallowed whole: a numbered section
#: nested inside the Context span. The elision must stop at the nested heading.
NESTED_INSTRUCTION = """---
form: enumerated
---

# Work order — nested fixture

## Context (non-normative)

CONTEXT-BODY-MARKER again.

### R0 — nested under context

NESTED-BOUND-SENTENCE must render.
"""


def build_plane(root: pathlib.Path, *, host_table: bool = True) -> dict:
    """Write a minimal, internally consistent control plane; return its documents."""
    control = root / "control"
    control.mkdir(parents=True)
    (root / "instruction.md").write_text(INSTRUCTION, encoding="utf-8")

    spec = {
        "schema_version": "2",
        "work_id": "fx-work",
        "objective": "exercise the preview renderer",
        "instruction_ref": {"path": "fixture/instruction.md", "revision": "f" * 40},
        "instruction_units": [
            {
                "unit_id": "unit-r0",
                "classification": "obligation",
                "locator": {"path": "fixture/instruction.md", "anchor": "## R0 — the boundary"},
                "obligation_ids": ["ob-r0"],
            },
            {
                "unit_id": "unit-r1",
                "classification": "obligation",
                "locator": {"path": "fixture/instruction.md", "anchor": "## R1 — the judged half"},
                "obligation_ids": ["ob-r1"],
            },
        ],
        "obligations": [
            {
                "obligation_id": "ob-r0",
                "requirement": "the bound sentence lands",
                "verification_mode": "local_check",
                "instruction_unit_ids": ["unit-r0"],
                "local_check_refs": ["chk-alpha", "chk-beta"],
            },
            {
                "obligation_id": "ob-r1",
                "requirement": "the judged half holds",
                "verification_mode": "review_only",
                "instruction_unit_ids": ["unit-r1"],
                "review_only_rationale": "RATIONALE-MARKER: no command decides prose support",
                "not_supported_when": "NOT-SUPPORTED-MARKER: the cited source says otherwise",
            },
        ],
        "change_boundary": {"write_scope": ["docs/target.md"], "out": ["docs/"]},
        "expected_artifacts": [{"artifact_id": "target-doc", "path": "docs/target.md"}],
    }
    write_canonical(control / "work-spec.json", spec)

    plan = {
        "plan_id": "fx-plan",
        "work_id": "fx-work",
        "work_spec_ref": {
            "path": "fixture/control/work-spec.json",
            "digest_sha256": canonical_digest(spec),
        },
        "check_order": ["chk-alpha", "chk-beta"],
        "repair_cap": 1,
        "resolver_version": "1.0.0",
        "effective_change_boundary": {"write_scope": ["docs/target.md"], "out": ["docs/"]},
    }
    write_canonical(control / "resolved-plan.json", plan)

    audit = {
        "audit_id": "fx-audit",
        "work_id": "fx-work",
        "instruction_ref": spec["instruction_ref"],
        "work_spec_ref": plan["work_spec_ref"],
        "result": "COVERED",
        "audited_at": "2026-08-21T00:00:00Z",
        "audited_by": "fixture",
    }
    write_canonical(control / "instruction-audit.json", audit)

    for check_id in ("chk-alpha", "chk-beta"):
        write_canonical(
            control / f"check-{check_id}.json",
            {
                "check_id": check_id,
                "kind": "command_exit",
                "subject_tree": "candidate_commit",
                "config": {"argv": ["true"]},
            },
        )

    if host_table:
        (control / "host-table.md").write_text(HOST_TABLE, encoding="utf-8")

    return {"spec": spec, "plan": plan, "audit": audit}


class PreviewRendering(unittest.TestCase):
    def setUp(self) -> None:
        self.root = pathlib.Path(tempfile.mkdtemp(prefix="v3preview-"))
        self.addCleanup(shutil.rmtree, self.root, ignore_errors=True)
        self.docs = build_plane(self.root)

    def render(self) -> tuple[str, bool]:
        return v3_preview.render_preview(self.root)

    def test_fixture_is_schema_valid(self) -> None:
        """The FULL of 57d1312 (B-1) traced the boundary blocker to an off-schema fixture:
        a shape that cannot occur exercises a branch that never runs. This pins the class."""
        spec_report = validate("spec_v2", self.docs["spec"])
        self.assertTrue(spec_report.ok, [issue.render() for issue in spec_report.issues])
        plan_report = validate("plan", self.docs["plan"])
        self.assertTrue(plan_report.ok, [issue.render() for issue in plan_report.issues])

    def test_boundary_renders_both_lists_not_the_field_names(self) -> None:
        text, _ = self.render()
        self.assertIn("write_scope (1): docs/target.md", text)
        self.assertIn("out (1): docs/", text)

    def test_a_section_nested_inside_context_is_not_swallowed(self) -> None:
        (self.root / "instruction.md").write_text(NESTED_INSTRUCTION, encoding="utf-8")
        text, _ = v3_preview.render_preview(self.root)
        self.assertIn("### R0 — nested under context", text)
        self.assertIn("NESTED-BOUND-SENTENCE must render.", text)
        self.assertNotIn("CONTEXT-BODY-MARKER", text)

    def test_a_check_the_plan_does_not_order_is_loud(self) -> None:
        plan = dict(self.docs["plan"])
        plan["check_order"] = ["chk-alpha"]
        write_canonical(self.root / "control" / "resolved-plan.json", plan)
        text, ok = v3_preview.render_preview(self.root)
        self.assertFalse(ok)
        self.assertIn("absent from the plan order: chk-beta", text)

    def test_all_planned_checks_leave_no_unplanned_line(self) -> None:
        text, ok = self.render()
        self.assertTrue(ok)
        self.assertNotIn("absent from the plan order", text)

    def test_a_plan_without_check_order_renders_the_absence_instead_of_crashing(self) -> None:
        plan = dict(self.docs["plan"])
        del plan["check_order"]
        self.assertTrue(validate("plan", plan).ok)
        write_canonical(self.root / "control" / "resolved-plan.json", plan)
        text, ok = v3_preview.render_preview(self.root)
        self.assertIn("the plan records no check order", text)
        self.assertFalse(ok)  # the obligations still reference chk-alpha/chk-beta

    def test_numbered_sections_appear_verbatim(self) -> None:
        text, ok = self.render()
        self.assertTrue(ok)
        self.assertIn("## R0 — the boundary", text)
        self.assertIn(
            "Only `docs/target.md` changes; THE-BOUND-SENTENCE lands verbatim.", text
        )
        self.assertIn("## R1 — the judged half", text)

    def test_context_is_named_but_its_body_is_not_rendered(self) -> None:
        text, _ = self.render()
        self.assertIn("## Context (non-normative)", text)
        self.assertNotIn("CONTEXT-BODY-MARKER", text)
        self.assertIn("not rendered", text)

    def test_bindings_recompute_the_start_digests(self) -> None:
        text, _ = self.render()
        self.assertIn(canonical_digest(self.docs["plan"]), text)
        self.assertIn(canonical_digest(self.docs["audit"]), text)

    def test_plan_binding_a_different_workspec_says_mismatch(self) -> None:
        plan = dict(self.docs["plan"])
        plan["work_spec_ref"] = {
            "path": plan["work_spec_ref"]["path"],
            "digest_sha256": "0" * 64,
        }
        write_canonical(self.root / "control" / "resolved-plan.json", plan)
        text, ok = v3_preview.render_preview(self.root)
        self.assertFalse(ok)
        self.assertIn("MISMATCH", text)

    def test_matching_plane_does_not_say_mismatch(self) -> None:
        text, ok = self.render()
        self.assertTrue(ok)
        self.assertNotIn("MISMATCH", text)

    def test_rendering_twice_is_byte_identical(self) -> None:
        first, _ = self.render()
        second, _ = self.render()
        self.assertEqual(first, second)

    def test_missing_core_files_raise_one_specgap_naming_every_absentee(self) -> None:
        (self.root / "control" / "work-spec.json").unlink()
        (self.root / "control" / "instruction-audit.json").unlink()
        with self.assertRaises(SpecGap) as caught:
            v3_preview.render_preview(self.root)
        message = str(caught.exception)
        self.assertIn(f"{v3_preview.CODE}-INCOMPLETE", message)
        self.assertIn("work-spec.json", message)
        self.assertIn("instruction-audit.json", message)

    def test_missing_check_spec_is_a_marked_row_and_not_ok(self) -> None:
        (self.root / "control" / "check-chk-beta.json").unlink()
        text, ok = v3_preview.render_preview(self.root)
        self.assertFalse(ok)
        self.assertIn("MISSING", text)
        self.assertIn("chk-beta", text)

    def test_host_table_is_verbatim_and_optional(self) -> None:
        text, _ = self.render()
        self.assertIn("HOST-TABLE-MARKER", text)
        (self.root / "control" / "host-table.md").unlink()
        text, ok = v3_preview.render_preview(self.root)
        self.assertTrue(ok)
        self.assertNotIn("HOST-TABLE-MARKER", text)

    def test_review_only_obligations_show_both_sentences(self) -> None:
        text, _ = self.render()
        self.assertIn("RATIONALE-MARKER: no command decides prose support", text)
        self.assertIn("NOT-SUPPORTED-MARKER: the cited source says otherwise", text)

    def test_check_rows_follow_plan_order(self) -> None:
        text, _ = self.render()
        self.assertLess(text.index("chk-alpha"), text.index("chk-beta"))
        plan = dict(self.docs["plan"])
        plan["check_order"] = ["chk-beta", "chk-alpha"]
        write_canonical(self.root / "control" / "resolved-plan.json", plan)
        text, _ = v3_preview.render_preview(self.root)
        checks_at = text.index("resolved-plan order")
        self.assertLess(text.index("chk-beta", checks_at), text.index("chk-alpha", checks_at))


class NamedIssueReachability(unittest.TestCase):
    """Every code `preview.py` can raise is asserted by name in this file."""

    def test_no_code_is_silent_surface(self) -> None:
        module_text = pathlib.Path(v3_preview.__file__).read_text(encoding="utf-8")
        declared = set(re.findall(r'f"\{CODE\}-([A-Z0-9-]+)', module_text))
        test_text = pathlib.Path(__file__).read_text(encoding="utf-8")
        asserted = set(re.findall(r"\{v3_preview\.CODE\}-([A-Z0-9-]+)", test_text))
        self.assertEqual(
            declared - asserted,
            set(),
            "codes declared in preview.py with no test asserting them by name",
        )
        self.assertEqual(len(declared), 1, f"code surface moved: {sorted(declared)}")


class PreviewCommandLine(unittest.TestCase):
    """`dtw preview` drives the renderer end to end — the proof test_cli_entry cannot give."""

    def setUp(self) -> None:
        self.root = pathlib.Path(tempfile.mkdtemp(prefix="v3preview-cli-"))
        self.addCleanup(shutil.rmtree, self.root, ignore_errors=True)
        build_plane(self.root)

    def run_preview(self) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, "dtw.py", "preview", "--run", str(self.root)],
            cwd=str(_harness.TOOLING_DIR),
            capture_output=True,
            encoding="utf-8",
            errors="replace",
        )

    def test_complete_plane_renders_and_exits_zero(self) -> None:
        completed = self.run_preview()
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertIn("START preview", completed.stdout)
        self.assertIn("## R0 — the boundary", completed.stdout)

    def test_incomplete_plane_exits_one(self) -> None:
        (self.root / "control" / "check-chk-beta.json").unlink()
        completed = self.run_preview()
        self.assertEqual(completed.returncode, 1, completed.stdout)
        self.assertIn("MISSING", completed.stdout)

    def test_missing_core_file_exits_two(self) -> None:
        (self.root / "control" / "work-spec.json").unlink()
        completed = self.run_preview()
        self.assertEqual(completed.returncode, 2, completed.stdout)
        self.assertIn("SPEC_GAP", completed.stderr)


if __name__ == "__main__":
    unittest.main()
