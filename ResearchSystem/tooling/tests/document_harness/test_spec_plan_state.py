"""Deterministic acceptance tests for the V3-N1 core: spec spine, profiles, plan, state.

Covers plan §9 acceptance IDs N1-A1, N1-A2, N1-A3, N1-A4, N1-A10, the plan-rebuildability
invariant (§5.2), and the profile-resolution accumulation property. Each test method proves
exactly one named property; the acceptance ID and a one-line statement of the property live
in the method's docstring.

Fixtures are built inline per test, following `_harness.py`'s own discipline: a reader must
see the defect being demonstrated in the test body without chasing a shared factory. Some
duplication across tests is intentional and accepted.

Offline: no network, no wall-clock dependence. `TempRepo` (from `_harness`) provides a
disposable Git repository for anything needing real file bytes on disk; nothing here writes
into the repository under assurance.
"""
from __future__ import annotations

import unittest

import _harness  # noqa: F401 — installs the tooling import path before rsclib imports below
from _harness import TempRepo

from rsclib.document_harness import (
    SpecGap,
    canonical_bytes,
    canonical_digest,
    validate,
    write_canonical,
)
from rsclib.document_harness import assurance_plan as plan_mod
from rsclib.document_harness import assurance_profiles as prof_mod
from rsclib.document_harness import assurance_state as state_mod
from rsclib.document_harness import instruction as instr_mod
from rsclib.document_harness import spec as spec_mod

#: A syntactically valid 40-hex Git revision. Its value carries no meaning — it only needs
#: to satisfy the `gitRev` pattern, so it is a plain constant rather than a fixture.
GIT_REV = "a" * 40


# ---------------------------------------------------------------------------
# N1-A1 — the no-profile path is a required POSITIVE case; absence, never [].
# ---------------------------------------------------------------------------


class TestN1A1NoProfilePositivePath(unittest.TestCase):
    def test_n1_a1_absent_profiles_field_resolves_cleanly_with_no_assurance_profiles_key(self):
        """N1-A1(a): a WorkSpec with no `document_assurance_profiles` field resolves cleanly
        and the resulting ResolvedAssurancePlan carries no `assurance_profiles` key."""
        spec = {
            "work_id": "thesis-note-update",
            "objective": "Update the literature review note with the new source list.",
            "instruction_ref": {"path": "docs/instruction.md", "revision": GIT_REV},
            "instruction_units": [
                {
                    "unit_id": "unit-scope",
                    "locator": {"path": "docs/instruction.md", "anchor": "Scope"},
                    "classification": "obligation",
                    "obligation_ids": ["ob-update-note"],
                },
            ],
            "change_boundary": {"write_scope": ["docs/note.md"], "out": ["docs/instruction.md"]},
            "expected_artifacts": [{"artifact_id": "art-note", "path": "docs/note.md"}],
            "obligations": [
                {
                    "obligation_id": "ob-update-note",
                    "instruction_unit_ids": ["unit-scope"],
                    "requirement": "The note must list every source named in the instruction.",
                    "expected_artifact_ids": ["art-note"],
                    "verification_mode": "review_only",
                },
            ],
        }
        self.assertNotIn("document_assurance_profiles", spec)
        self.assertTrue(validate("spec", spec).ok)

        selected = prof_mod.load_selected(spec, "nonexistent-profile-dir")
        self.assertEqual(selected, [])

        plan = plan_mod.resolve(spec, "docs/spec.json", selected)
        self.assertNotIn("assurance_profiles", plan)
        self.assertTrue(plan_mod.check_plan(plan).ok)

    def test_n1_a1_empty_profiles_array_is_rejected_by_schema(self):
        """N1-A1(b): a WorkSpec carrying `document_assurance_profiles: []` is REJECTED —
        an empty placeholder is not "no profile"."""
        spec = {
            "work_id": "thesis-note-update",
            "objective": "Update the literature review note with the new source list.",
            "instruction_ref": {"path": "docs/instruction.md", "revision": GIT_REV},
            "instruction_units": [
                {
                    "unit_id": "unit-scope",
                    "locator": {"path": "docs/instruction.md", "anchor": "Scope"},
                    "classification": "obligation",
                    "obligation_ids": ["ob-update-note"],
                },
            ],
            "document_assurance_profiles": [],
            "change_boundary": {"write_scope": ["docs/note.md"], "out": ["docs/instruction.md"]},
            "expected_artifacts": [{"artifact_id": "art-note", "path": "docs/note.md"}],
            "obligations": [
                {
                    "obligation_id": "ob-update-note",
                    "instruction_unit_ids": ["unit-scope"],
                    "requirement": "The note must list every source named in the instruction.",
                    "expected_artifact_ids": ["art-note"],
                    "verification_mode": "review_only",
                },
            ],
        }
        report = validate("spec", spec)
        self.assertFalse(report.ok)
        self.assertTrue(
            any(
                issue.code == "V3-SCHEMA-SPEC" and issue.where == "document_assurance_profiles"
                for issue in report.issues
            )
        )


# ---------------------------------------------------------------------------
# N1-A2 — the profile promotion threshold.
# ---------------------------------------------------------------------------


class TestN1A2ProfilePromotionThreshold(unittest.TestCase):
    def _valid_profile(self):
        return {
            "profile_id": "doc-length-guard",
            "version": "1.0.0",
            "summary": "Cap the maximum line count of a generated document artifact.",
            "rule_family": "doc-length",
            "owner": "Doc Assurance WG",
            "reason_to_change": "The line-count ceiling has changed twice across real stage work.",
            "parameters": [
                {"name": "max_lines", "description": "Maximum permitted line count.", "required": True},
            ],
            "reuse_witnesses": [
                {
                    "work_description": "First real reuse of the length guard.",
                    "evidence_ref": {"path": "Thesis/Work/Design/alpha/NOTES.md"},
                },
                {
                    "work_description": "Second real reuse of the length guard.",
                    "evidence_ref": {"path": "Thesis/Work/Design/beta/NOTES.md"},
                },
            ],
            "required_checks": [
                {"check_id": "doc-length-check", "kind": "file_exists", "parameter_names": ["max_lines"]},
            ],
        }

    def test_n1_a2_valid_profile_passes_check_profile(self):
        """N1-A2: a profile with one rule family, an owner, a reason to change and two
        distinct real reuse witnesses passes `check_profile` cleanly."""
        report = prof_mod.check_profile(self._valid_profile())
        self.assertTrue(report.ok)
        self.assertEqual(report.issues, ())

    def test_n1_a2_fewer_than_two_witnesses_fails(self):
        """N1-A2: a profile with only one reuse witness is rejected — below the promotion
        threshold, the rule must stay stage-local."""
        profile = self._valid_profile()
        profile["reuse_witnesses"] = [profile["reuse_witnesses"][0]]
        report = prof_mod.check_profile(profile)
        self.assertFalse(report.ok)
        self.assertTrue(
            any(
                issue.code == "V3-SCHEMA-PROFILE" and issue.where == "reuse_witnesses"
                for issue in report.issues
            )
        )

    def test_n1_a2_two_witnesses_same_evidence_path_fails(self):
        """N1-A2: two witnesses citing the same evidence path is one witness wearing two
        descriptions, not two distinct reuse instances."""
        profile = self._valid_profile()
        profile["reuse_witnesses"][1]["evidence_ref"]["path"] = profile["reuse_witnesses"][0][
            "evidence_ref"
        ]["path"]
        report = prof_mod.check_profile(profile)
        self.assertFalse(report.ok)
        self.assertTrue(any(issue.code == "V3-PROFILE-WITNESS-NOT-DISTINCT" for issue in report.issues))

    def test_n1_a2_witness_pointing_into_fixture_root_fails(self):
        """N1-A2: a reuse witness whose evidence path points into a test/fixture root is
        synthetic self-witnessing, not evidence of real work."""
        profile = self._valid_profile()
        profile["reuse_witnesses"][1]["evidence_ref"]["path"] = "tests/fixtures/witness.md"
        report = prof_mod.check_profile(profile)
        self.assertFalse(report.ok)
        self.assertTrue(any(issue.code == "V3-PROFILE-WITNESS-SYNTHETIC" for issue in report.issues))

    def test_n1_a2_rule_referencing_undeclared_parameter_fails(self):
        """N1-A2: a rule (here, a required check) referencing a parameter the profile never
        declared is rejected — the selecting WorkSpec would have no way to know what to
        supply."""
        profile = self._valid_profile()
        del profile["parameters"]  # "max_lines" is now referenced but never declared
        report = prof_mod.check_profile(profile)
        self.assertFalse(report.ok)
        self.assertTrue(any(issue.code == "V3-PROFILE-UNDECLARED-PARAMETER" for issue in report.issues))


# ---------------------------------------------------------------------------
# N1-A3 — the instruction-obligation spine and its START-blocking behaviour.
# ---------------------------------------------------------------------------


class TestN1A3InstructionObligationSpine(unittest.TestCase):
    def test_n1_a3_obligation_unit_without_obligation_ids_blocks_start(self):
        """N1-A3: an instruction unit classified `obligation` with no `obligation_ids` has
        no disposition and blocks START as `SpecGap`."""
        spec = {
            "work_id": "thesis-note-update",
            "objective": "Update the literature review note with the new source list.",
            "instruction_ref": {"path": "docs/instruction.md", "revision": GIT_REV},
            "instruction_units": [
                {
                    "unit_id": "unit-scope",
                    "locator": {"path": "docs/instruction.md", "anchor": "Scope"},
                    "classification": "obligation",
                    # obligation_ids deliberately omitted: the silent-omission defect this
                    # product exists to make visible.
                },
            ],
            "change_boundary": {"write_scope": ["docs/note.md"], "out": ["docs/instruction.md"]},
            "expected_artifacts": [{"artifact_id": "art-note", "path": "docs/note.md"}],
            "obligations": [
                {
                    "obligation_id": "ob-update-note",
                    "instruction_unit_ids": ["unit-scope"],
                    "requirement": "The note must list every source named in the instruction.",
                    "verification_mode": "review_only",
                },
            ],
        }
        report = spec_mod.check_spec(spec)
        self.assertFalse(report.ok)
        self.assertTrue(
            any(
                issue.code == "V3-SCHEMA-SPEC" and issue.where == "instruction_units/0"
                for issue in report.issues
            )
        )
        with self.assertRaises(SpecGap):
            spec_mod.require_startable(spec)

    def test_n1_a3_context_unit_without_rationale_blocks_start(self):
        """N1-A3: an instruction unit classified `context` with no `rationale` has no
        disposition and blocks START as `SpecGap`."""
        spec = {
            "work_id": "thesis-note-update",
            "objective": "Update the literature review note with the new source list.",
            "instruction_ref": {"path": "docs/instruction.md", "revision": GIT_REV},
            "instruction_units": [
                {
                    "unit_id": "unit-background",
                    "locator": {"path": "docs/instruction.md", "anchor": "Background"},
                    "classification": "context",
                    # rationale deliberately omitted.
                },
                {
                    "unit_id": "unit-scope",
                    "locator": {"path": "docs/instruction.md", "anchor": "Scope"},
                    "classification": "obligation",
                    "obligation_ids": ["ob-update-note"],
                },
            ],
            "change_boundary": {"write_scope": ["docs/note.md"], "out": ["docs/instruction.md"]},
            "expected_artifacts": [{"artifact_id": "art-note", "path": "docs/note.md"}],
            "obligations": [
                {
                    "obligation_id": "ob-update-note",
                    "instruction_unit_ids": ["unit-scope"],
                    "requirement": "The note must list every source named in the instruction.",
                    "verification_mode": "review_only",
                },
            ],
        }
        report = spec_mod.check_spec(spec)
        self.assertFalse(report.ok)
        self.assertTrue(
            any(
                issue.code == "V3-SCHEMA-SPEC" and issue.where == "instruction_units/0"
                for issue in report.issues
            )
        )
        with self.assertRaises(SpecGap):
            spec_mod.require_startable(spec)

    def test_n1_a3_unit_with_bogus_classification_blocks_start(self):
        """N1-A3: an instruction unit carrying a classification outside the closed
        `obligation | context` set has no disposition and blocks START as `SpecGap`."""
        spec = {
            "work_id": "thesis-note-update",
            "objective": "Update the literature review note with the new source list.",
            "instruction_ref": {"path": "docs/instruction.md", "revision": GIT_REV},
            "instruction_units": [
                {
                    "unit_id": "unit-scope",
                    "locator": {"path": "docs/instruction.md", "anchor": "Scope"},
                    "classification": "bogus",
                    "obligation_ids": ["ob-update-note"],
                },
            ],
            "change_boundary": {"write_scope": ["docs/note.md"], "out": ["docs/instruction.md"]},
            "expected_artifacts": [{"artifact_id": "art-note", "path": "docs/note.md"}],
            "obligations": [
                {
                    "obligation_id": "ob-update-note",
                    "instruction_unit_ids": ["unit-scope"],
                    "requirement": "The note must list every source named in the instruction.",
                    "verification_mode": "review_only",
                },
            ],
        }
        report = spec_mod.check_spec(spec)
        self.assertFalse(report.ok)
        self.assertTrue(
            any(
                issue.code == "V3-SCHEMA-SPEC" and issue.where == "instruction_units/0/classification"
                for issue in report.issues
            )
        )
        with self.assertRaises(SpecGap):
            spec_mod.require_startable(spec)

    def test_n1_a3_obligation_referencing_undeclared_unit(self):
        """N1-A3 bidirectionality: an obligation whose `instruction_unit_ids` names a unit
        that was never declared produces `V3-SPEC-DANGLING-UNIT-REF`."""
        spec = {
            "work_id": "thesis-note-update",
            "objective": "Update the literature review note with the new source list.",
            "instruction_ref": {"path": "docs/instruction.md", "revision": GIT_REV},
            "instruction_units": [
                {
                    "unit_id": "unit-scope",
                    "locator": {"path": "docs/instruction.md", "anchor": "Scope"},
                    "classification": "obligation",
                    "obligation_ids": ["ob-update-note"],
                },
            ],
            "change_boundary": {"write_scope": ["docs/note.md"], "out": ["docs/instruction.md"]},
            "expected_artifacts": [{"artifact_id": "art-note", "path": "docs/note.md"}],
            "obligations": [
                {
                    "obligation_id": "ob-update-note",
                    "instruction_unit_ids": ["unit-missing"],  # never declared above
                    "requirement": "The note must list every source named in the instruction.",
                    "verification_mode": "review_only",
                },
            ],
        }
        report = spec_mod.check_spec(spec)
        self.assertFalse(report.ok)
        self.assertTrue(
            any(
                issue.code == "V3-SPEC-DANGLING-UNIT-REF" and issue.where == "obligations/ob-update-note"
                for issue in report.issues
            )
        )

    def test_n1_a3_unit_referencing_undeclared_obligation(self):
        """N1-A3 bidirectionality: an obligation-classified unit whose `obligation_ids`
        names an obligation that was never declared produces `V3-SPEC-DANGLING-OBLIGATION-REF`."""
        spec = {
            "work_id": "thesis-note-update",
            "objective": "Update the literature review note with the new source list.",
            "instruction_ref": {"path": "docs/instruction.md", "revision": GIT_REV},
            "instruction_units": [
                {
                    "unit_id": "unit-scope",
                    "locator": {"path": "docs/instruction.md", "anchor": "Scope"},
                    "classification": "obligation",
                    "obligation_ids": ["ob-missing"],  # never declared below
                },
                {
                    # Claims the real obligation, so it stays claimed and this test isolates
                    # exactly the dangling-obligation-ref defect (no stray unreferenced issue).
                    "unit_id": "unit-extra",
                    "locator": {"path": "docs/instruction.md", "anchor": "Extra"},
                    "classification": "obligation",
                    "obligation_ids": ["ob-update-note"],
                },
            ],
            "change_boundary": {"write_scope": ["docs/note.md"], "out": ["docs/instruction.md"]},
            "expected_artifacts": [{"artifact_id": "art-note", "path": "docs/note.md"}],
            "obligations": [
                {
                    "obligation_id": "ob-update-note",
                    "instruction_unit_ids": ["unit-scope"],
                    "requirement": "The note must list every source named in the instruction.",
                    "verification_mode": "review_only",
                },
            ],
        }
        report = spec_mod.check_spec(spec)
        self.assertFalse(report.ok)
        codes = {issue.code for issue in report.issues}
        self.assertIn("V3-SPEC-DANGLING-OBLIGATION-REF", codes)
        self.assertTrue(
            any(
                issue.code == "V3-SPEC-DANGLING-OBLIGATION-REF" and issue.where == "instruction_units/unit-scope"
                for issue in report.issues
            )
        )

    def test_n1_a3_obligation_unclaimed_by_any_unit(self):
        """N1-A3 bidirectionality: an obligation that no instruction unit claims produces
        `V3-SPEC-UNREFERENCED-OBLIGATION` — nothing in the instruction demands it."""
        spec = {
            "work_id": "thesis-note-update",
            "objective": "Update the literature review note with the new source list.",
            "instruction_ref": {"path": "docs/instruction.md", "revision": GIT_REV},
            "instruction_units": [
                {
                    "unit_id": "unit-scope",
                    "locator": {"path": "docs/instruction.md", "anchor": "Scope"},
                    "classification": "obligation",
                    # Claims the secondary obligation, not the real target, so the real
                    # target ends up unclaimed while the unit itself stays schema-valid.
                    "obligation_ids": ["ob-secondary"],
                },
            ],
            "change_boundary": {"write_scope": ["docs/note.md"], "out": ["docs/instruction.md"]},
            "expected_artifacts": [{"artifact_id": "art-note", "path": "docs/note.md"}],
            "obligations": [
                {
                    "obligation_id": "ob-update-note",
                    "instruction_unit_ids": ["unit-scope"],
                    "requirement": "The note must list every source named in the instruction.",
                    "verification_mode": "review_only",
                },
                {
                    "obligation_id": "ob-secondary",
                    "instruction_unit_ids": ["unit-scope"],
                    "requirement": "A secondary requirement that unit-scope actually claims.",
                    "verification_mode": "review_only",
                },
            ],
        }
        report = spec_mod.check_spec(spec)
        self.assertFalse(report.ok)
        self.assertTrue(
            any(
                issue.code == "V3-SPEC-UNREFERENCED-OBLIGATION" and issue.where == "obligations"
                for issue in report.issues
            )
        )

    def test_n1_a3_duplicate_id(self):
        """N1-A3 bidirectionality: two instruction units declaring the same `unit_id`
        produce `V3-SPEC-DUPLICATE-ID` — a later join could not tell them apart."""
        spec = {
            "work_id": "thesis-note-update",
            "objective": "Update the literature review note with the new source list.",
            "instruction_ref": {"path": "docs/instruction.md", "revision": GIT_REV},
            "instruction_units": [
                {
                    "unit_id": "unit-scope",
                    "locator": {"path": "docs/instruction.md", "anchor": "Scope"},
                    "classification": "obligation",
                    "obligation_ids": ["ob-update-note"],
                },
                {
                    "unit_id": "unit-scope",  # duplicate of the id above
                    "locator": {"path": "docs/instruction.md", "anchor": "Scope2"},
                    "classification": "context",
                    "rationale": "A duplicate unit id sharing the identifier of the unit above.",
                },
            ],
            "change_boundary": {"write_scope": ["docs/note.md"], "out": ["docs/instruction.md"]},
            "expected_artifacts": [{"artifact_id": "art-note", "path": "docs/note.md"}],
            "obligations": [
                {
                    "obligation_id": "ob-update-note",
                    "instruction_unit_ids": ["unit-scope"],
                    "requirement": "The note must list every source named in the instruction.",
                    "verification_mode": "review_only",
                },
            ],
        }
        report = spec_mod.check_spec(spec)
        self.assertFalse(report.ok)
        self.assertTrue(
            any(
                issue.code == "V3-SPEC-DUPLICATE-ID" and issue.where == "instruction_units"
                for issue in report.issues
            )
        )

    def test_n1_a3_obligation_referencing_undeclared_artifact(self):
        """N1-A3 bidirectionality: an obligation whose `expected_artifact_ids` names an
        artifact that was never declared produces `V3-SPEC-DANGLING-ARTIFACT-REF`."""
        spec = {
            "work_id": "thesis-note-update",
            "objective": "Update the literature review note with the new source list.",
            "instruction_ref": {"path": "docs/instruction.md", "revision": GIT_REV},
            "instruction_units": [
                {
                    "unit_id": "unit-scope",
                    "locator": {"path": "docs/instruction.md", "anchor": "Scope"},
                    "classification": "obligation",
                    "obligation_ids": ["ob-update-note"],
                },
            ],
            "change_boundary": {"write_scope": ["docs/note.md"], "out": ["docs/instruction.md"]},
            "expected_artifacts": [{"artifact_id": "art-note", "path": "docs/note.md"}],
            "obligations": [
                {
                    "obligation_id": "ob-update-note",
                    "instruction_unit_ids": ["unit-scope"],
                    "requirement": "The note must list every source named in the instruction.",
                    "expected_artifact_ids": ["art-missing"],  # never declared above
                    "verification_mode": "review_only",
                },
            ],
        }
        report = spec_mod.check_spec(spec)
        self.assertFalse(report.ok)
        self.assertTrue(
            any(
                issue.code == "V3-SPEC-DANGLING-ARTIFACT-REF"
                and issue.where == "obligations/ob-update-note"
                for issue in report.issues
            )
        )


# ---------------------------------------------------------------------------
# N1-A4 — START binds the exact plan and the exact audit; no second approval path.
# ---------------------------------------------------------------------------


class TestN1A4StartBinding(unittest.TestCase):
    def _spec(self, objective="Update the literature review note with the new source list."):
        return {
            "work_id": "thesis-note-update",
            "objective": objective,
            "instruction_ref": {"path": "docs/instruction.md", "revision": GIT_REV},
            "instruction_units": [
                {
                    "unit_id": "unit-scope",
                    "locator": {"path": "docs/instruction.md", "anchor": "Scope"},
                    "classification": "obligation",
                    "obligation_ids": ["ob-update-note"],
                },
            ],
            "change_boundary": {"write_scope": ["docs/note.md"], "out": ["docs/instruction.md"]},
            "expected_artifacts": [{"artifact_id": "art-note", "path": "docs/note.md"}],
            "obligations": [
                {
                    "obligation_id": "ob-update-note",
                    "instruction_unit_ids": ["unit-scope"],
                    "requirement": "The note must list every source named in the instruction.",
                    "expected_artifact_ids": ["art-note"],
                    "verification_mode": "review_only",
                },
            ],
        }

    def _audit(self, spec, *, audited_by="Auditor Ada"):
        return {
            "audit_id": "audit-thesis-note-update",
            "work_id": "thesis-note-update",
            "work_spec_ref": {"path": "docs/spec.json", "digest_sha256": spec_mod.spec_digest(spec)},
            "instruction_ref": {"path": "docs/instruction.md", "revision": GIT_REV},
            "result": "COVERED",
            "audited_by": audited_by,
            "audited_at": "2026-07-01",
        }

    def _decision(self, plan, audit):
        return {
            "decision_id": "decision-start-1",
            "work_id": "thesis-note-update",
            "phase": "START",
            "decision": "START",
            "target": {
                "resolved_plan_ref": {"path": "docs/plan.json", "digest_sha256": canonical_digest(plan)},
                "instruction_audit_ref": {
                    "path": "docs/audit.json",
                    "digest_sha256": instr_mod.audit_digest(audit),
                },
            },
            "decided_by": "User Uma",
            "decided_at": "2026-07-01",
        }

    def test_n1_a4_correct_start_decision_passes(self):
        """N1-A4: a START decision that binds the exact plan and the exact audit passes
        `check_start_decision` and `require_started`."""
        spec = self._spec()
        plan = plan_mod.resolve(spec, "docs/spec.json", [])
        audit = self._audit(spec)
        decision = self._decision(plan, audit)

        report = instr_mod.check_start_decision(decision, plan, audit)
        self.assertTrue(report.ok)
        instr_mod.require_started(decision, plan, audit)  # must not raise

    def test_n1_a4_mutated_plan_breaks_binding(self):
        """N1-A4: mutating the plan (via an upstream WorkSpec byte change) after the START
        decision was signed makes the binding fail — the decision no longer names the
        exact plan bytes the user approved."""
        spec = self._spec()
        plan = plan_mod.resolve(spec, "docs/spec.json", [])
        audit = self._audit(spec)
        decision = self._decision(plan, audit)  # signed against the ORIGINAL plan

        mutated_spec = self._spec(
            objective="Update the literature review note with the new source list!"
        )
        mutated_plan = plan_mod.resolve(mutated_spec, "docs/spec.json", [])

        report = instr_mod.check_start_decision(decision, mutated_plan, audit)
        self.assertFalse(report.ok)
        self.assertTrue(
            any(
                issue.code == "V3-START-BINDING-MISMATCH" and issue.where == "target/resolved_plan_ref"
                for issue in report.issues
            )
        )

    def test_n1_a4_mutated_audit_breaks_binding(self):
        """N1-A4: mutating the audit dict after the START decision was signed makes the
        binding fail — the decision no longer names the exact audit bytes."""
        spec = self._spec()
        plan = plan_mod.resolve(spec, "docs/spec.json", [])
        audit = self._audit(spec)
        decision = self._decision(plan, audit)  # signed against the ORIGINAL audit

        mutated_audit = dict(audit)
        mutated_audit["audited_by"] = "Auditor Zed"

        report = instr_mod.check_start_decision(decision, plan, mutated_audit)
        self.assertFalse(report.ok)
        self.assertTrue(
            any(
                issue.code == "V3-START-BINDING-MISMATCH"
                and issue.where == "target/instruction_audit_ref"
                for issue in report.issues
            )
        )

    def test_n1_a4_require_covered_raises_on_spec_gap(self):
        """N1-A4: `require_covered` raises `SpecGap` on a `SPEC_GAP` audit result — there is
        no repair loop for the instruction coverage audit."""
        spec = self._spec()
        audit = self._audit(spec)
        audit["result"] = "SPEC_GAP"
        audit["findings"] = [
            {
                "finding_id": "finding-1",
                "kind": "UNMAPPED_NORMATIVE_TEXT",
                "instruction_locator": {"path": "docs/instruction.md", "anchor": "X"},
                "description": "Some text was never mapped to a unit or obligation.",
            }
        ]
        with self.assertRaises(SpecGap):
            instr_mod.require_covered(audit)

    def test_n1_a4_check_audit_catches_spec_digest_mismatch(self):
        """N1-A4 invariant 1: `check_audit` catches an audit performed against different
        WorkSpec bytes than the ones supplied."""
        spec = self._spec()
        audit = self._audit(spec)
        audit["work_spec_ref"] = {"path": "docs/spec.json", "digest_sha256": "0" * 64}

        report = instr_mod.check_audit(audit, spec, executor="Executor Eve")
        self.assertFalse(report.ok)
        self.assertTrue(
            any(
                issue.code == "V3-AUDIT-SPEC-DIGEST-MISMATCH"
                and issue.where == "work_spec_ref/digest_sha256"
                for issue in report.issues
            )
        )

    def test_n1_a4_check_audit_catches_instruction_ref_mismatch(self):
        """N1-A4 invariant 1: `check_audit` catches an audit that judged a different frozen
        instruction revision than the WorkSpec's."""
        spec = self._spec()
        audit = self._audit(spec)
        audit["instruction_ref"] = {"path": "docs/instruction.md", "revision": "b" * 40}

        report = instr_mod.check_audit(audit, spec, executor="Executor Eve")
        self.assertFalse(report.ok)
        self.assertTrue(
            any(
                issue.code == "V3-AUDIT-INSTRUCTION-MISMATCH" and issue.where == "instruction_ref"
                for issue in report.issues
            )
        )

    def test_n1_a4_check_audit_catches_same_actor_auditor_and_executor(self):
        """N1-A4 invariant 1: `check_audit` catches an auditor that is the same actor as the
        executor of the same run — the audit was not performed by a distinguishable
        context."""
        spec = self._spec()
        audit = self._audit(spec, audited_by="Auditor Ada")

        report = instr_mod.check_audit(audit, spec, executor="Auditor Ada")
        self.assertFalse(report.ok)
        self.assertTrue(
            any(
                issue.code == "V3-AUDIT-AUDITOR-NOT-DISTINGUISHABLE" and issue.where == "audited_by"
                for issue in report.issues
            )
        )

    def test_n1_a4_omitting_the_executor_does_not_silently_skip_the_distinctness_guard(self):
        """N1-A4: with no executor identity supplied the distinctness guard cannot run, and an
        absent guard must never read as a passing one.

        This is the shape that matters: the caller omits an argument, so the check is skipped
        — and previously that produced a clean report indistinguishable from "checked and
        distinct". Neutering the guard (`if False`) must break this test.
        """
        spec = self._spec()
        audit = self._audit(spec, audited_by="Auditor Ada")

        report = instr_mod.check_audit(audit, spec)  # executor deliberately not supplied
        self.assertFalse(report.ok)
        self.assertTrue(
            any(
                issue.code == "V3-AUDIT-AUDITOR-DISTINCTNESS-UNVERIFIED"
                and issue.where == "audited_by"
                for issue in report.issues
            )
        )

    def test_n1_a4_supplying_a_distinct_executor_reports_neither_code(self):
        """N1-A4 negative control: with a genuinely distinct executor the guard runs and is
        silent — so an always-firing check would fail this, and the test above cannot pass
        for the trivial reason that `check_audit` never returns ok."""
        spec = self._spec()
        audit = self._audit(spec, audited_by="Auditor Ada")

        report = instr_mod.check_audit(audit, spec, executor="Executor Eve")
        codes = [issue.code for issue in report.issues]
        self.assertTrue(report.ok, codes)
        self.assertNotIn("V3-AUDIT-AUDITOR-DISTINCTNESS-UNVERIFIED", codes)
        self.assertNotIn("V3-AUDIT-AUDITOR-NOT-DISTINGUISHABLE", codes)

    def test_n1_a4_require_single_start_raises_on_second_approval(self):
        """N1-A4: `require_single_start` raises `SpecGap` when the state already points at a
        different START decision — there is no second approval path."""
        state = {
            "work_id": "thesis-note-update",
            "run_id": "run-1",
            "status": "RESOLVED",
            "repair_round": 0,
            "work_spec_ref": {"path": "docs/spec.json"},
            "resolved_plan_ref": {"path": "docs/plan.json"},
            "start_decision_ref": {"path": "docs/decision-start-OLD.json"},
        }
        with self.assertRaises(SpecGap):
            instr_mod.require_single_start(state, "docs/decision-start-NEW.json")


# ---------------------------------------------------------------------------
# N1-A10 — cold resume from the state plus its pointers, with no event chain.
# ---------------------------------------------------------------------------


class TestN1A10ColdResume(unittest.TestCase):
    def _spec(self):
        return {
            "work_id": "thesis-note-update",
            "objective": "Update the literature review note with the new source list.",
            "instruction_ref": {"path": "docs/instruction.md", "revision": GIT_REV},
            "instruction_units": [
                {
                    "unit_id": "unit-scope",
                    "locator": {"path": "docs/instruction.md", "anchor": "Scope"},
                    "classification": "obligation",
                    "obligation_ids": ["ob-update-note"],
                },
            ],
            "change_boundary": {"write_scope": ["docs/note.md"], "out": ["docs/instruction.md"]},
            "expected_artifacts": [{"artifact_id": "art-note", "path": "docs/note.md"}],
            "obligations": [
                {
                    "obligation_id": "ob-update-note",
                    "instruction_unit_ids": ["unit-scope"],
                    "requirement": "The note must list every source named in the instruction.",
                    "expected_artifact_ids": ["art-note"],
                    "verification_mode": "review_only",
                },
            ],
        }

    def test_n1_a10_resume_reads_only_state_and_its_pointers(self):
        """N1-A10: cold resume reconstructs the run's position from the state file plus the
        exact files its pointers name — nothing else present in the repo is required."""
        with TempRepo() as repo:
            spec = self._spec()
            spec_digest = write_canonical(repo.root / "docs" / "spec.json", spec)
            plan = plan_mod.resolve(spec, "docs/spec.json", [])
            plan_digest = write_canonical(repo.root / "docs" / "plan.json", plan)

            state = state_mod.new_state(
                "thesis-note-update",
                "run-1",
                work_spec_ref=state_mod.pointer("docs/spec.json", spec_digest),
                resolved_plan_ref=state_mod.pointer("docs/plan.json", plan_digest),
                next_action="await instruction coverage audit",
            )
            state_path = repo.root / "docs" / "state.json"
            state_mod.save(state, state_path)

            resume_point = state_mod.resume(state_path, repo.root)

            self.assertTrue(resume_point.report.ok)
            self.assertEqual(
                resume_point.verified,
                {"work_spec_ref": "docs/spec.json", "resolved_plan_ref": "docs/plan.json"},
            )
            self.assertEqual(resume_point.present_unverified, {})
            self.assertEqual(resume_point.status, "RESOLVED")

    def test_n1_a10_deleted_pointer_target_reports_pointer_missing(self):
        """N1-A10: a pointer whose target file was deleted is reported `POINTER-MISSING`,
        not silently skipped."""
        with TempRepo() as repo:
            spec = self._spec()
            spec_digest = write_canonical(repo.root / "docs" / "spec.json", spec)
            plan = plan_mod.resolve(spec, "docs/spec.json", [])
            plan_digest = write_canonical(repo.root / "docs" / "plan.json", plan)

            state = state_mod.new_state(
                "thesis-note-update",
                "run-1",
                work_spec_ref=state_mod.pointer("docs/spec.json", spec_digest),
                resolved_plan_ref=state_mod.pointer("docs/plan.json", plan_digest),
            )
            state_path = repo.root / "docs" / "state.json"
            state_mod.save(state, state_path)

            repo.delete("docs/plan.json")

            resume_point = state_mod.resume(state_path, repo.root)

            self.assertFalse(resume_point.report.ok)
            self.assertTrue(
                any(
                    issue.code == "V3-STATE-POINTER-MISSING" and issue.where == "resolved_plan_ref"
                    for issue in resume_point.report.issues
                )
            )
            self.assertNotIn("resolved_plan_ref", resume_point.verified)

    def test_n1_a10_changed_pointer_bytes_reports_pointer_stale_and_is_not_followed(self):
        """N1-A10: a pointer whose target bytes changed after the digest was taken is
        reported `POINTER-STALE` and is excluded from the resolved set — it is not silently
        followed."""
        with TempRepo() as repo:
            spec = self._spec()
            spec_digest = write_canonical(repo.root / "docs" / "spec.json", spec)
            plan = plan_mod.resolve(spec, "docs/spec.json", [])
            plan_digest = write_canonical(repo.root / "docs" / "plan.json", plan)

            state = state_mod.new_state(
                "thesis-note-update",
                "run-1",
                work_spec_ref=state_mod.pointer("docs/spec.json", spec_digest),
                resolved_plan_ref=state_mod.pointer("docs/plan.json", plan_digest),
            )
            state_path = repo.root / "docs" / "state.json"
            state_mod.save(state, state_path)

            # Bytes drift after the digest was taken — no re-save of the state.
            plan_path = repo.root / "docs" / "plan.json"
            plan_path.write_bytes(plan_path.read_bytes() + b" ")

            resume_point = state_mod.resume(state_path, repo.root)

            self.assertFalse(resume_point.report.ok)
            self.assertTrue(
                any(
                    issue.code == "V3-STATE-POINTER-STALE" and issue.where == "resolved_plan_ref"
                    for issue in resume_point.report.issues
                )
            )
            self.assertNotIn("resolved_plan_ref", resume_point.verified)
            self.assertIn("work_spec_ref", resume_point.verified)  # the sound pointer still resolves

    def test_n1_a10_pointer_without_a_digest_is_never_reported_as_verified(self):
        """N1-A10: a pointer carrying no digest can only establish existence, so it must not
        appear as verified and must not render as `ok`.

        The sharp case: the target's bytes are rewritten after the state was saved. Nothing
        can detect that — the pointer never carried a digest to compare against — so the only
        honest outcome is that the pointer is visibly *unverified* rather than sound.
        """
        with TempRepo() as repo:
            spec = self._spec()
            write_canonical(repo.root / "docs" / "spec.json", spec)
            plan = plan_mod.resolve(spec, "docs/spec.json", [])
            plan_digest = write_canonical(repo.root / "docs" / "plan.json", plan)

            state = state_mod.new_state(
                "thesis-note-update",
                "run-1",
                work_spec_ref=state_mod.pointer("docs/spec.json"),  # no digest
                resolved_plan_ref=state_mod.pointer("docs/plan.json", plan_digest),
            )
            state_path = repo.root / "docs" / "state.json"
            state_mod.save(state, state_path)

            # The bytes behind the digest-less pointer drift. Nothing can catch this.
            (repo.root / "docs" / "spec.json").write_text("tampered", encoding="utf-8")

            resume_point = state_mod.resume(state_path, repo.root)

            self.assertNotIn("work_spec_ref", resume_point.verified)
            self.assertIn("work_spec_ref", resume_point.present_unverified)
            self.assertIn("resolved_plan_ref", resume_point.verified)

            rendered = resume_point.render()
            spec_line = next(line for line in rendered.splitlines() if "work_spec_ref" in line)
            self.assertIn("??", spec_line)
            self.assertNotIn("ok", spec_line)
            self.assertIn("NOT verified", rendered)

    def test_a_protected_pointer_without_a_digest_is_an_issue_and_still_unverified(self):
        """The digest narrowing (2026-07-29): on a DIGEST_PROTECTED_FIELDS pointer a missing
        digest is now reported, and the pointer *also* stays in `present_unverified`.

        Both halves matter. Reporting it is the new obligation — those five files have no
        legitimate digest-less shape, because the only author entitled to their current
        version is not the executor writing the pointer. Keeping it in `present_unverified`
        is the old N1-A10 property above: an unverified pointer renders `??`, and swapping
        that for an issue alone would delete a recorded property to make room for a new one.
        """
        with TempRepo() as repo:
            spec = self._spec()
            write_canonical(repo.root / "docs" / "spec.json", spec)
            plan = plan_mod.resolve(spec, "docs/spec.json", [])
            plan_digest = write_canonical(repo.root / "docs" / "plan.json", plan)

            state = state_mod.new_state(
                "thesis-note-update",
                "run-1",
                work_spec_ref=state_mod.pointer("docs/spec.json"),  # protected, no digest
                resolved_plan_ref=state_mod.pointer("docs/plan.json", plan_digest),
            )
            state_path = repo.root / "docs" / "state.json"
            state_mod.save(state, state_path)

            resume_point = state_mod.resume(state_path, repo.root)

            self.assertFalse(resume_point.report.ok)
            self.assertTrue(
                any(
                    issue.code == "V3-STATE-POINTER-UNVERIFIED"
                    and issue.where == "work_spec_ref"
                    for issue in resume_point.report.issues
                ),
                "; ".join(resume_point.report.rendered()),
            )
            self.assertIn("work_spec_ref", resume_point.present_unverified)
            self.assertNotIn("work_spec_ref", resume_point.verified)

    def test_an_unprotected_pointer_without_a_digest_is_unverified_but_not_an_issue(self):
        """The negative control for the test above, and the narrowing's actual purpose.

        Outside the protected set the executor is the legitimate author of the file's
        current version, so a digest it computed over that file constrains nobody and its
        absence is not a defect. The pointer is still *visibly* unverified — that split is
        N1-A10 and is untouched — it simply raises nothing.
        """
        with TempRepo() as repo:
            spec = self._spec()
            spec_digest = write_canonical(repo.root / "docs" / "spec.json", spec)
            plan = plan_mod.resolve(spec, "docs/spec.json", [])
            write_canonical(repo.root / "docs" / "plan.json", plan)

            state = state_mod.new_state(
                "thesis-note-update",
                "run-1",
                work_spec_ref=state_mod.pointer("docs/spec.json", spec_digest),
                resolved_plan_ref=state_mod.pointer("docs/plan.json"),  # unprotected, none
            )
            state_path = repo.root / "docs" / "state.json"
            state_mod.save(state, state_path)

            resume_point = state_mod.resume(state_path, repo.root)

            self.assertTrue(resume_point.report.ok,
                            "; ".join(resume_point.report.rendered()))
            self.assertIn("resolved_plan_ref", resume_point.present_unverified)
            self.assertNotIn("resolved_plan_ref", resume_point.verified)


# ---------------------------------------------------------------------------
# Plan rebuildability (§5.2) — the ResolvedAssurancePlan is disposable and rebuildable.
# ---------------------------------------------------------------------------


class TestPlanRebuildability(unittest.TestCase):
    def _spec(self):
        return {
            "work_id": "thesis-note-update",
            "objective": "Update the literature review note with the new source list.",
            "instruction_ref": {"path": "docs/instruction.md", "revision": GIT_REV},
            "instruction_units": [
                {
                    "unit_id": "unit-scope",
                    "locator": {"path": "docs/instruction.md", "anchor": "Scope"},
                    "classification": "obligation",
                    "obligation_ids": ["ob-update-note"],
                },
            ],
            "change_boundary": {"write_scope": ["docs/note.md"], "out": ["docs/instruction.md"]},
            "expected_artifacts": [{"artifact_id": "art-note", "path": "docs/note.md"}],
            "obligations": [
                {
                    "obligation_id": "ob-update-note",
                    "instruction_unit_ids": ["unit-scope"],
                    "requirement": "The note must list every source named in the instruction.",
                    "expected_artifact_ids": ["art-note"],
                    "verification_mode": "review_only",
                },
            ],
        }

    def _profile(self, profile_id):
        return {
            "profile_id": profile_id,
            "version": "1.0.0",
            "summary": "A rule family reused across two real stages of document work.",
            "rule_family": "doc-validity",
            "owner": "Doc Assurance WG",
            "reason_to_change": "The validity check shape changed once across real reuse.",
            "reuse_witnesses": [
                {
                    "work_description": "First real reuse.",
                    "evidence_ref": {"path": "Thesis/Work/Design/alpha/NOTES.md"},
                },
                {
                    "work_description": "Second real reuse.",
                    "evidence_ref": {"path": "Thesis/Work/Design/beta/NOTES.md"},
                },
            ],
            "required_checks": [{"check_id": "doc-validity-check", "kind": "file_exists"}],
        }

    def test_plan_rebuild_matches_for_no_profile_resolution(self):
        """§5.2: a no-profile ResolvedAssurancePlan rebuilds byte-identically from its
        pinned WorkSpec and the resolver."""
        spec = self._spec()
        plan = plan_mod.resolve(spec, "docs/spec.json", [])
        self.assertTrue(plan_mod.rebuild_matches(plan, spec, "docs/spec.json", []))

    def test_plan_rebuild_matches_for_with_profile_resolution(self):
        """§5.2: a with-profile ResolvedAssurancePlan rebuilds byte-identically from its
        pinned WorkSpec, the exact profile version and the resolver."""
        spec = self._spec()
        profile = self._profile("profile-a")
        selection = {"profile_id": "profile-a", "version": "1.0.0"}
        selected = [(selection, profile)]

        plan = plan_mod.resolve(spec, "docs/spec.json", selected)
        self.assertTrue(plan_mod.rebuild_matches(plan, spec, "docs/spec.json", selected))

    def test_plan_resolving_twice_yields_byte_identical_canonical_bytes(self):
        """§5.2: resolving the same WorkSpec plus profiles twice yields byte-identical
        `canonical_bytes` — no timestamp, no unordered-set drift."""
        spec = self._spec()
        profile_a = self._profile("profile-a")
        profile_b = self._profile("profile-b")
        selected = [
            ({"profile_id": "profile-a", "version": "1.0.0"}, profile_a),
            ({"profile_id": "profile-b", "version": "1.0.0"}, profile_b),
        ]

        first = plan_mod.resolve(spec, "docs/spec.json", selected)
        second = plan_mod.resolve(spec, "docs/spec.json", selected)
        self.assertEqual(canonical_bytes(first), canonical_bytes(second))

    def test_plan_check_plan_rejects_copied_canonical_fact(self):
        """§5.2: `check_plan` rejects a plan that copies a canonical WorkSpec fact (here,
        `obligations`) — the plan may only reference canonical facts, never duplicate them."""
        spec = self._spec()
        plan = plan_mod.resolve(spec, "docs/spec.json", [])

        tainted = dict(plan)
        tainted["obligations"] = spec["obligations"]  # a canonical fact, never plan-owned

        report = plan_mod.check_plan(tainted)
        codes = [issue.code for issue in report.issues]
        self.assertFalse(report.ok)
        # BOTH must fire, and the pairing is the point. The schema's additionalProperties:
        # false says an unexpected property appeared; the module's own code says WHY that
        # shape is forbidden — a plan copying a canonical fact drifts from the WorkSpec it
        # claims to resolve (N0-A6). An earlier ordering returned the schema report early
        # and left the named code permanently unreachable; this asserts it is reachable.
        self.assertIn("V3-PLAN-CANONICAL-FACT-COPIED", codes)
        self.assertIn("V3-SCHEMA-PLAN", codes)

    def test_plan_repair_cap_is_exactly_one(self):
        """§5.2: the resolver always stamps `repair_cap: 1`, and `check_plan` rejects any
        other value — at most one user-approved bounded repair per run."""
        spec = self._spec()
        plan = plan_mod.resolve(spec, "docs/spec.json", [])
        self.assertEqual(plan["repair_cap"], 1)
        self.assertTrue(plan_mod.check_plan(plan).ok)

        tampered = dict(plan)
        tampered["repair_cap"] = 2
        report = plan_mod.check_plan(tampered)
        codes = [issue.code for issue in report.issues]
        self.assertFalse(report.ok)
        # As above: the named invariant must be reachable, not shadowed by the schema's
        # `repair_cap: {const: 1}`. V3-D6's bounded-convergence guarantee deserves its own
        # greppable code in the evidence, not just a const violation.
        self.assertIn("V3-PLAN-REPAIR-CAP", codes)
        self.assertTrue(
            any(issue.code == "V3-SCHEMA-PLAN" and issue.where == "repair_cap" for issue in report.issues)
        )

    def test_plan_named_conflicts_block_require_startable(self):
        """§5.2: a resolution that produced a named conflict (two profiles requiring the
        same check id with different kinds) makes `require_startable` raise `SpecGap` —
        resolution fails closed rather than picking a winner."""
        spec = self._spec()
        profile_a = self._profile("profile-a")
        profile_a["required_checks"] = [{"check_id": "shared-check", "kind": "file_exists"}]
        profile_b = self._profile("profile-b")
        profile_b["required_checks"] = [{"check_id": "shared-check", "kind": "markdown_link"}]
        selected = [
            ({"profile_id": "profile-a", "version": "1.0.0"}, profile_a),
            ({"profile_id": "profile-b", "version": "1.0.0"}, profile_b),
        ]

        plan = plan_mod.resolve(spec, "docs/spec.json", selected)
        self.assertEqual(len(plan.get("conflicts", [])), 1)
        self.assertEqual(plan["conflicts"][0]["conflict_id"], "check-kind-shared-check")

        with self.assertRaises(SpecGap):
            plan_mod.require_startable(plan)


# ---------------------------------------------------------------------------
# Profile resolution accumulation.
# ---------------------------------------------------------------------------


class TestProfileResolutionAccumulation(unittest.TestCase):
    def test_profile_resolution_accumulates_checks_and_materializes_constraint_paths_into_out(self):
        """§5.2: two profiles contributing `required_checks` land in
        `resolved_deltas.added_checks` and in `check_order`; a `change_constraints` entry
        whose parameter supplies paths materializes those paths into
        `effective_change_boundary.out` and never into `write_scope` — constraints only
        tighten."""
        spec = {
            "work_id": "thesis-note-update",
            "objective": "Update the literature review note with the new source list.",
            "instruction_ref": {"path": "docs/instruction.md", "revision": GIT_REV},
            "instruction_units": [
                {
                    "unit_id": "unit-scope",
                    "locator": {"path": "docs/instruction.md", "anchor": "Scope"},
                    "classification": "obligation",
                    "obligation_ids": ["ob-update-note"],
                },
            ],
            "change_boundary": {"write_scope": ["docs/note.md"], "out": ["docs/instruction.md"]},
            "expected_artifacts": [{"artifact_id": "art-note", "path": "docs/note.md"}],
            "obligations": [
                {
                    "obligation_id": "ob-update-note",
                    "instruction_unit_ids": ["unit-scope"],
                    "requirement": "The note must list every source named in the instruction.",
                    "expected_artifact_ids": ["art-note"],
                    "verification_mode": "review_only",
                },
            ],
        }

        profile_a = {
            "profile_id": "profile-a",
            "version": "1.0.0",
            "summary": "First accumulating rule family reused across two real stages.",
            "rule_family": "doc-validity",
            "owner": "Doc Assurance WG",
            "reason_to_change": "Needed a deterministic check bound at resolution time.",
            "reuse_witnesses": [
                {
                    "work_description": "First real reuse.",
                    "evidence_ref": {"path": "Thesis/Work/Design/alpha/NOTES.md"},
                },
                {
                    "work_description": "Second real reuse.",
                    "evidence_ref": {"path": "Thesis/Work/Design/beta/NOTES.md"},
                },
            ],
            "required_checks": [{"check_id": "check-a", "kind": "file_exists"}],
        }
        profile_b = {
            "profile_id": "profile-b",
            "version": "1.0.0",
            "summary": "Second accumulating rule family that also materializes a constraint.",
            "rule_family": "doc-boundary",
            "owner": "Doc Assurance WG",
            "reason_to_change": "Needed a reusable boundary-tightening pattern.",
            "parameters": [
                {"name": "protected_paths", "description": "Paths to keep out of scope.", "required": True},
            ],
            "reuse_witnesses": [
                {
                    "work_description": "First real reuse.",
                    "evidence_ref": {"path": "Thesis/Work/Design/gamma/NOTES.md"},
                },
                {
                    "work_description": "Second real reuse.",
                    "evidence_ref": {"path": "Thesis/Work/Design/delta/NOTES.md"},
                },
            ],
            "required_checks": [{"check_id": "check-b", "kind": "file_exists"}],
            "change_constraints": [
                {
                    "constraint_id": "no-touch-secrets",
                    "description": "Never touch secret material during this work.",
                    "parameter_names": ["protected_paths"],
                },
            ],
        }
        selected = [
            ({"profile_id": "profile-a", "version": "1.0.0"}, profile_a),
            (
                {
                    "profile_id": "profile-b",
                    "version": "1.0.0",
                    "parameters": {"protected_paths": ["secrets/config.env"]},
                },
                profile_b,
            ),
        ]

        plan = plan_mod.resolve(spec, "docs/spec.json", selected)

        added_check_ids = {entry["check_id"] for entry in plan["resolved_deltas"]["added_checks"]}
        self.assertEqual(added_check_ids, {"check-a", "check-b"})
        self.assertEqual(plan["check_order"], ["check-a", "check-b"])

        self.assertIn("secrets/config.env", plan["effective_change_boundary"]["out"])
        self.assertNotIn("secrets/config.env", plan["effective_change_boundary"]["write_scope"])
        self.assertEqual(plan["effective_change_boundary"]["write_scope"], ["docs/note.md"])


if __name__ == "__main__":
    unittest.main()
