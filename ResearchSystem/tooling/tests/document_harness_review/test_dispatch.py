#!/usr/bin/env python3
"""Acceptance matrix for the executor-side dispatch generator (`dispatch.py`).

The property under test is that a dispatch is *derived*, so every test starts from a real
committed control plane in a disposable repository and asserts what the command reads back
out of it — never what a caller handed in. The scenario builder is **imported from the
wave-2 subject suite rather than copied**, on the same reasoning that suite gives for
importing N1's plumbing: two builders would mean two slightly different notions of "a
committed control plane", and the newer one would quietly stop testing the real shape.

Each "must fire" case asserts an exact issue code and is paired with the clean scenario,
which is asserted clean first — a refusal test proves nothing if the baseline also refuses.
`NamedIssueReachability` pins the module's whole code surface, so a code added later without
a test fails here rather than becoming silent dead surface.
"""
from __future__ import annotations

import json
import pathlib
import re
import unittest

from _harness import TempRepo, git  # noqa: F401  (imported for parity with the suite)
from test_review_v2_subject import CONTROL_ROOT, build_scenario, codes

from rsclib.document_harness import bytes_digest
from rsclib.document_harness import dispatch as D

FAKE_REV = "f" * 40

REPAIR_DECISION = {
    "decision_id": "repair-run-one",
    "work_id": "work-one",
    "run_id": "run-one",
    "phase": "REPAIR",
    "decision": "APPLY_ACCEPTED_FINDINGS",
    "target": {
        "candidate_ref": {"branch": "cand", "commit": "0" * 40},
        "accepted_finding_ids": ["f1-something-wrong", "f2-something-else"],
        "repair_boundary": {"write_scope": ["docs"], "out": ["runs"]},
    },
    "decided_by": "Melclycj (user)",
    "decided_at": "2026-07-25",
}


def repaired_scenario(*, decision_text: str | None = None, drop_file: bool = False,
                      round_value=1):
    """A round-1 control plane carrying a committed REPAIR decision."""
    text = decision_text if decision_text is not None else json.dumps(REPAIR_DECISION, indent=1)
    path = f"{CONTROL_ROOT}/control/user-decision-repair.json"
    overrides = {} if drop_file else {path: text}

    def state_mut(state):
        state["repair_round"] = round_value
        state["repair_decision_ref"] = {
            "path": path,
            "digest_sha256": bytes_digest(text.encode("utf-8")),
        }

    return build_scenario(file_overrides=overrides, state_mut=state_mut)


# ---------------------------------------------------------------------------
# The clean baselines — asserted clean before any refusal is trusted
# ---------------------------------------------------------------------------


class DerivesTheRoundZeroDispatch(unittest.TestCase):
    """Round 0 owes a FULL, and every field comes out of the commit."""

    @classmethod
    def setUpClass(cls):
        cls.scn = build_scenario()
        cls.d = D.dispatch_of(cls.scn.repo.root, cls.scn.evidence_commit)

    def test_the_baseline_derives_clean(self):
        self.assertTrue(self.d.report.ok, codes(self.d.report))

    def test_round_zero_owes_a_full(self):
        self.assertEqual(self.d.role, "FULL")

    def test_the_control_root_is_found_from_the_commits_own_paths(self):
        self.assertEqual(self.d.control_root, CONTROL_ROOT)

    def test_identity_and_binding_are_read_from_the_committed_plane(self):
        self.assertEqual(self.d.run_id, "run-one")
        self.assertEqual(self.d.work_id, "work-one")
        self.assertEqual(self.d.status, "EVIDENCED")
        self.assertEqual(self.d.base_revision, self.scn.repo.base)
        self.assertEqual(self.d.candidate_ref["commit"], self.scn.candidate)

    def test_counts_come_from_the_spec_and_plan_not_from_a_caller(self):
        self.assertEqual(self.d.obligation_count, 1)
        self.assertEqual(self.d.check_count, 1)

    def test_a_full_may_return_changes_required(self):
        self.assertIn("CHANGES_REQUIRED", D.VERDICTS["FULL"])
        self.assertIn("CHANGES_REQUIRED", D.render_derivation(self.d))

    def test_a_full_dispatch_carries_no_repair_scope(self):
        self.assertEqual(self.d.accepted_finding_ids, ())
        self.assertNotIn("repair scope", D.render_derivation(self.d))


class DerivesTheVerifyDispatch(unittest.TestCase):
    """Round 1 owes the targeted VERIFY, scoped by the committed REPAIR decision."""

    @classmethod
    def setUpClass(cls):
        cls.scn = repaired_scenario()
        cls.d = D.dispatch_of(cls.scn.repo.root, cls.scn.evidence_commit)

    def test_the_baseline_derives_clean(self):
        self.assertTrue(self.d.report.ok, codes(self.d.report))

    def test_round_one_owes_a_verify(self):
        self.assertEqual(self.d.role, "VERIFY")

    def test_the_scope_is_the_committed_accepted_finding_ids(self):
        self.assertEqual(
            self.d.accepted_finding_ids,
            ("f1-something-wrong", "f2-something-else"),
        )

    def test_the_repair_boundary_is_the_committed_one(self):
        self.assertEqual(self.d.repair_boundary, {"write_scope": ["docs"], "out": ["runs"]})

    def test_a_verify_may_not_return_changes_required(self):
        self.assertNotIn("CHANGES_REQUIRED", D.VERDICTS["VERIFY"])
        self.assertNotIn("CHANGES_REQUIRED", D.render_derivation(self.d))

    def test_every_accepted_finding_reaches_the_dispatchers_view(self):
        derivation = D.render_derivation(self.d)
        for finding_id in self.d.accepted_finding_ids:
            self.assertIn(finding_id, derivation)


# ---------------------------------------------------------------------------
# Refusals — each asserts one exact code
# ---------------------------------------------------------------------------


class RefusesWhatIsNotADispatchableSubject(unittest.TestCase):

    def test_an_unreadable_commit_is_reported_not_raised(self):
        scn = build_scenario()
        d = D.dispatch_of(scn.repo.root, FAKE_REV)
        self.assertIn(f"{D.CODE}-COMMIT-UNREADABLE", codes(d.report))
        self.assertIsNone(d.control_root)

    def test_a_commit_carrying_no_control_plane_is_not_a_subject(self):
        scn = build_scenario()
        d = D.dispatch_of(scn.repo.root, scn.repo.base)
        self.assertIn(f"{D.CODE}-NOT-AN-EVIDENCE-COMMIT", codes(d.report))

    def test_two_control_roots_in_one_commit_are_ambiguous_never_preferred(self):
        scn = build_scenario(
            extra_files={"runs/run-two/control/state.json": json.dumps({"run_id": "run-two"})}
        )
        d = D.dispatch_of(scn.repo.root, scn.evidence_commit)
        self.assertIn(f"{D.CODE}-AMBIGUOUS-CONTROL-ROOT", codes(d.report))
        self.assertIsNone(d.control_root)

    def test_a_closed_run_is_not_a_position_a_review_is_dispatched_from(self):
        scn = build_scenario(state_mut=lambda s: s.update({"status": "CLOSED"}))
        d = D.dispatch_of(scn.repo.root, scn.evidence_commit)
        self.assertIn(f"{D.CODE}-NOT-DISPATCHABLE", codes(d.report))
        self.assertIsNone(d.role)

    def test_every_non_evidenced_status_refuses(self):
        for status in ("RESOLVED", "AUDITED", "EXECUTING", "REVIEWED", "REPAIRING",
                       "AWAITING_FINAL", "CLOSED", "STOPPED_REPLAN"):
            with self.subTest(status=status):
                role, report = D.role_for({"status": status, "repair_round": 0})
                self.assertIsNone(role)
                self.assertIn(f"{D.CODE}-NOT-DISPATCHABLE", codes(report))

    def test_a_non_integer_round_cannot_decide_which_review_is_owed(self):
        role, report = D.role_for({"status": "EVIDENCED", "repair_round": "1"})
        self.assertIsNone(role)
        self.assertIn(f"{D.CODE}-ROUND-UNREADABLE", codes(report))


class TheSubjectIsAlwaysRoutedInFull(unittest.TestCase):
    """An abbreviation is a weaker binding than the custody chain assumes (REVIEW.md O2)."""

    def test_an_abbreviated_revision_resolves_and_the_document_carries_40_hex(self):
        scn = build_scenario()
        short = scn.evidence_commit[:7]
        d = D.dispatch_of(scn.repo.root, short)
        self.assertTrue(d.report.ok, codes(d.report))
        self.assertEqual(d.evidence_commit, scn.evidence_commit)
        self.assertEqual(len(d.evidence_commit), 40)
        self.assertIn(scn.evidence_commit, D.render_dispatch(d))

    def test_a_symbolic_revision_resolves(self):
        scn = build_scenario()
        resolved, report = D.resolve_subject(scn.repo.root, "HEAD")
        self.assertTrue(report.ok)
        self.assertEqual(resolved, scn.evidence_commit)

    def test_a_revision_that_names_nothing_is_reported(self):
        scn = build_scenario()
        resolved, report = D.resolve_subject(scn.repo.root, "no-such-ref")
        self.assertIsNone(resolved)
        self.assertIn(f"{D.CODE}-COMMIT-UNREADABLE", codes(report))


class TheCommitIsCheckedAsACompleteSubjectNotOnlyAsResolvablePointers(unittest.TestCase):
    """`read_control_plane` answers a narrower question than `check_subject`.

    The first version of this module called only the former, so a commit whose evidence set
    was incomplete derived a *clean* dispatch — fail-open, and the module docstring claimed
    the opposite. These tests pin that `check_subject` is actually reached.
    """

    def test_an_incomplete_evidence_set_no_longer_derives_a_clean_dispatch(self):
        clean = build_scenario()
        self.assertTrue(D.dispatch_of(clean.repo.root, clean.evidence_commit).report.ok)

        scn = build_scenario(drop_files=[f"{CONTROL_ROOT}/evidence/check-chk-one.json"])
        d = D.dispatch_of(scn.repo.root, scn.evidence_commit)
        self.assertFalse(d.report.ok, "an incomplete evidence set derived a clean dispatch")
        self.assertTrue(
            any(code.startswith("V3-SUBJECT") for code in codes(d.report)),
            f"check_subject was not reached: {codes(d.report)}",
        )

    def test_a_record_without_a_candidate_ref_reports_the_check_as_unperformed(self):
        scn = build_scenario(record_mut=lambda r: r.pop("candidate_ref"))
        d = D.dispatch_of(scn.repo.root, scn.evidence_commit)
        self.assertIn(f"{D.CODE}-SUBJECT-UNCHECKED", codes(d.report))


class RefusesAnUnderivableVerifyScope(unittest.TestCase):
    """A VERIFY whose scope cannot be derived is refused, never scoped to everything."""

    def test_a_repaired_run_with_no_committed_repair_decision(self):
        scn = build_scenario(state_mut=lambda s: s.update({"repair_round": 1}))
        d = D.dispatch_of(scn.repo.root, scn.evidence_commit)
        self.assertIn(f"{D.CODE}-REPAIR-DECISION-ABSENT", codes(d.report))
        self.assertEqual(d.accepted_finding_ids, ())

    def test_a_repair_decision_pointer_that_does_not_resolve_in_the_commit(self):
        scn = repaired_scenario(drop_file=True)
        d = D.dispatch_of(scn.repo.root, scn.evidence_commit)
        self.assertIn(f"{D.CODE}-REPAIR-DECISION-MISSING", codes(d.report))

    def test_a_repair_decision_that_is_not_valid_json(self):
        scn = repaired_scenario(decision_text="{not json")
        d = D.dispatch_of(scn.repo.root, scn.evidence_commit)
        self.assertIn(f"{D.CODE}-REPAIR-DECISION-INVALID", codes(d.report))


# ---------------------------------------------------------------------------
# Rendering — the honesty properties, which are the point of the module
# ---------------------------------------------------------------------------


class TheReviewerIsHandedNothingButTheSubject(unittest.TestCase):
    """The finding that reshaped this module: derived facts must NOT reach the reviewer.

    Handing a reviewer a pre-derived table defeats the property the layer exists for — a
    fact you were handed is a fact you did not check, and an error in the table is inherited
    in silence. These tests are the guard against that regressing, so each names a specific
    derived value and asserts it is absent from the reviewer's document.
    """

    @classmethod
    def setUpClass(cls):
        cls.scn = build_scenario()
        cls.d = D.dispatch_of(cls.scn.repo.root, cls.scn.evidence_commit)
        cls.doc = D.render_dispatch(cls.d)

    def test_the_document_carries_the_subject_sha(self):
        self.assertIn(self.scn.evidence_commit, self.doc)

    def test_the_document_points_at_the_role_instruction_rather_than_quoting_it(self):
        self.assertIn(D.ROLE_INSTRUCTION, self.doc)
        # The charter lives in REVIEW.md; a second live copy here would drift.
        self.assertNotIn("A FULL review answers", self.doc)
        self.assertNotIn("REVIEWED_NO_BLOCKER", self.doc)

    def test_the_document_cites_no_numbered_section(self):
        """Reported by a real reviewer: an emitted "your §8" pointed at the wrong charter.

        The product-run reviewer reads `REVIEW.md`, whose sections are named and unnumbered;
        `§n` belongs to the construction-side contract governing a different role. Since
        `REVIEW.md` has no numbered section at all, any `§` in the emitted document is
        necessarily a citation of somebody else's instruction — so the guard is simply that
        none appears. Asserted against the file too, so the premise is checked rather than
        remembered.
        """
        review_md = (
            pathlib.Path(D.__file__).parents[3] / "document-harness" / "REVIEW.md"
        ).read_text(encoding="utf-8")
        self.assertEqual(
            re.findall(r"^#+ *\d", review_md, re.M), [],
            "REVIEW.md gained a numbered section; this guard's premise needs revisiting",
        )
        self.assertNotIn("§", self.doc)

    def test_no_hunt_section_is_offered_at_all(self):
        """A per-round hunt list is a shadow WorkSpec — unapproved, outside the control plane.

        The module used to emit a fill-in marker for one. Asserting its absence keeps a
        future round from reintroducing the section as a convenience.
        """
        self.assertNotIn("hunt", self.doc.lower())
        self.assertNotIn("FILL IN", self.doc)

    def test_no_derived_run_fact_reaches_the_reviewer(self):
        for label, value in (
            ("control root", self.d.control_root),
            ("run id", self.d.run_id),
            ("work id", self.d.work_id),
            ("base revision", self.d.base_revision),
            ("candidate commit", self.d.candidate_ref["commit"]),
        ):
            with self.subTest(fact=label):
                self.assertNotIn(str(value), self.doc)

    def test_no_declared_boundary_path_reaches_the_reviewer(self):
        for path in self.d.change_boundary.get("write_scope", ()):
            with self.subTest(path=path):
                self.assertNotIn(path, self.doc)

    def test_the_reviewer_is_told_to_derive_rather_than_to_accept(self):
        # Whitespace-normalised: the assertion is about the sentence, not the wrap column.
        flat = " ".join(self.doc.split())
        self.assertIn("Everything else you derive from the repository", flat)
        self.assertIn("a fact you were handed is a fact you did not check", flat)

    def test_the_dispatchers_view_does_carry_those_facts(self):
        """The split is the point: absent from one document, present in the other."""
        derivation = D.render_derivation(self.d)
        self.assertIn(self.d.control_root, derivation)
        self.assertIn(self.d.run_id, derivation)
        self.assertIn(self.d.base_revision, derivation)


class AnUnderivableDispatchRefusesInsteadOfRendering(unittest.TestCase):

    def test_a_refusal_does_not_restate_the_sha_as_a_subject(self):
        """So a broken dispatch cannot be routed by pasting past the warning."""
        scn = build_scenario(state_mut=lambda s: s.update({"status": "CLOSED"}))
        doc = D.render_dispatch(D.dispatch_of(scn.repo.root, scn.evidence_commit))
        self.assertIn("NOT DISPATCHABLE", doc)
        self.assertIn(f"{D.CODE}-NOT-DISPATCHABLE", doc)
        self.assertNotIn("Subject:", doc)

    def test_an_unresolved_field_renders_as_a_marker_in_the_dispatchers_view(self):
        scn = build_scenario()
        derivation = D.render_derivation(D.dispatch_of(scn.repo.root, FAKE_REV))
        self.assertIn("NOT DERIVED", derivation)

    def test_a_clean_dispatch_is_the_document_not_a_refusal(self):
        scn = build_scenario()
        doc = D.render_dispatch(D.dispatch_of(scn.repo.root, scn.evidence_commit))
        self.assertNotIn("NOT DISPATCHABLE", doc)

    def test_the_result_schema_is_v2_because_the_subject_is_commit_bound(self):
        self.assertIn("review.v2.schema.json", D.RESULT_SCHEMA)


class ConstructionRoundsGenerateToo(unittest.TestCase):
    """The one irreducible input is the round's boundary; the prompt is a constant.

    This class used to hold eleven tests (counted at `d55d5ce`) guarding a derived churn list
    and the sliced constant that carried its caveat. The derivation is gone (see the module's construction section),
    and with it F1, V1, V2, V3 and V4 — every one of which existed only to hold churn up. What
    remains is the assertion those five were reaching for and never made: the emitted document
    equals the expected document exactly, which catches an added line, a missing line and a
    reordered line with one comparison.
    """

    def _round(self):
        scn = build_scenario()
        repo = scn.repo
        base = git(repo.root, "rev-parse", "HEAD").strip()
        (repo.root / "a.md").write_text("one\n", encoding="utf-8")
        git(repo.root, "add", "a.md")
        git(repo.root, "commit", "-q", "-m", "round commit")
        return repo, base, git(repo.root, "rev-parse", "HEAD").strip()

    #: The expected prompt lives in a committed fixture, not in this file. A golden file is
    #: the ordinary idiom for "the output must be exactly this", and it removes the reason the
    #: two previous guards failed: an expectation sitting next to the source it checks reads as
    #: duplication and invites being collapsed into a reference, which makes the comparison
    #: compare the module to itself. In a separate data file there is nothing to collapse.
    FIXTURE = pathlib.Path(__file__).parents[1] / "fixtures" / "expected-construction-prompt.txt"

    def test_the_prompt_is_exactly_the_golden_file(self):
        """Added, missing and reordered lines all fail here, in one comparison."""
        repo, base, tip = self._round()
        d = D.construction_dispatch_of(repo.root, base, tip)
        self.assertTrue(d.report.ok, codes(d.report))
        expected = self.FIXTURE.read_text(encoding="utf-8").format(base=base, tip=tip)
        self.assertEqual(D.render_construction_dispatch(d), expected)

    def test_the_prompt_carries_nothing_but_the_charter_and_the_range(self):
        """Stated as absences too, so the intent survives an edit to the constant."""
        repo, base, tip = self._round()
        prompt = D.render_construction_dispatch(D.construction_dispatch_of(repo.root, base, tip))
        self.assertIn(D.CONSTRUCTION_ROLE_INSTRUCTION, prompt)
        self.assertIn(f"{base}..{tip}", prompt)
        self.assertNotIn("Churn", prompt)
        self.assertNotIn("commits", prompt)
        self.assertNotIn("upper bound", prompt)
        # §n is correct in THIS direction only — but nothing is cited here at all now.
        self.assertNotIn(D.ROLE_INSTRUCTION, prompt)

    def test_a_reversed_range_does_not_bound_a_round(self):
        repo, base, tip = self._round()
        d = D.construction_dispatch_of(repo.root, tip, base)
        self.assertIn(f"{D.CODE}-RANGE-NOT-ANCESTRAL", codes(d.report))

    def test_a_range_containing_no_commit_is_refused(self):
        repo, base, tip = self._round()
        d = D.construction_dispatch_of(repo.root, tip, tip)
        self.assertIn(f"{D.CODE}-EMPTY-RANGE", codes(d.report))

    def test_an_unresolvable_endpoint_is_reported(self):
        repo, base, tip = self._round()
        d = D.construction_dispatch_of(repo.root, "no-such-ref", tip)
        self.assertIn(f"{D.CODE}-COMMIT-UNREADABLE", codes(d.report))

    def test_a_refusal_is_not_a_prompt_and_names_no_subject(self):
        repo, base, tip = self._round()
        doc = D.render_construction_dispatch(D.construction_dispatch_of(repo.root, tip, base))
        self.assertIn("NOT DISPATCHABLE", doc)
        self.assertNotIn("Subject:", doc)

    def test_both_endpoints_are_routed_in_full(self):
        repo, base, tip = self._round()
        d = D.construction_dispatch_of(repo.root, base[:7], tip[:7])
        self.assertEqual((len(d.base), len(d.tip)), (40, 40))
        self.assertIn(f"{base}..{tip}", D.render_construction_dispatch(d))


class ReadDispatchesGenerateToo(unittest.TestCase):
    """The third family (E10 layer reads): one commit, a constant prompt, no member list.

    The member set stays with E10's sentence on purpose — the hand-written read dispatch
    this mode replaces enumerated the members and got the set wrong
    (`v3-cold-read-451e8b0.md` M-1), which is the anchoring failure the module exists to
    remove.
    """

    FIXTURE = pathlib.Path(__file__).parents[1] / "fixtures" / "expected-read-prompt.txt"

    def test_the_prompt_is_exactly_the_golden_file(self):
        scn = build_scenario()
        d = D.read_dispatch_of(scn.repo.root, "HEAD")
        self.assertTrue(d.report.ok, codes(d.report))
        expected = self.FIXTURE.read_text(encoding="utf-8").format(commit=d.commit)
        self.assertEqual(D.render_read_dispatch(d), expected)

    def test_the_subject_is_routed_in_full(self):
        scn = build_scenario()
        d = D.read_dispatch_of(scn.repo.root, scn.evidence_commit[:7])
        self.assertTrue(d.report.ok, codes(d.report))
        self.assertEqual(len(d.commit), 40)

    def test_no_member_enumeration_reaches_the_reader(self):
        scn = build_scenario()
        prompt = D.render_read_dispatch(D.read_dispatch_of(scn.repo.root, "HEAD"))
        self.assertIn("E10's own", prompt)
        self.assertNotIn("CONSTRUCTION-CHECKLIST.md", prompt)
        self.assertNotIn("supersession", prompt)

    def test_an_unresolvable_revision_refuses_and_names_no_subject(self):
        scn = build_scenario()
        d = D.read_dispatch_of(scn.repo.root, "no-such-ref")
        self.assertIn(f"{D.CODE}-COMMIT-UNREADABLE", codes(d.report))
        doc = D.render_read_dispatch(d)
        self.assertIn("NOT DISPATCHABLE", doc)
        self.assertNotIn("Subject:", doc)


class NamedIssueReachability(unittest.TestCase):
    """Every code `dispatch.py` can raise is asserted by name in this file."""

    def test_no_code_is_silent_surface(self):
        import pathlib
        import re

        module_text = pathlib.Path(D.__file__).read_text(encoding="utf-8")
        declared = set(re.findall(r'f"\{CODE\}-([A-Z-]+)"', module_text))
        test_text = pathlib.Path(__file__).read_text(encoding="utf-8")
        asserted = set(re.findall(r'\{D\.CODE\}-([A-Z-]+)', test_text))
        self.assertEqual(
            declared - asserted,
            set(),
            "codes declared in dispatch.py with no test asserting them by name",
        )
        self.assertEqual(len(declared), 11, f"code surface moved: {sorted(declared)}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
