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
import tempfile
import unittest
from unittest import mock

from _harness import TempRepo, git  # noqa: F401  (imported for parity with the suite)
from test_review_v2_subject import CONTROL_ROOT, build_scenario, codes

from rsclib.document_harness import bytes_digest
from rsclib.document_harness import dispatch as D

FAKE_REV = "f" * 40

#: Hand-written whole lines (`E5`), never imported from the module under test: the two
#: forms of the declared-rules line `E10`'s second sentence obliges every prompt to carry.
NO_RULES_LINE = (
    "**This repository's own rules:** none. Its `harness.json` declares no rule files, "
    "which E10 makes a repository that has declared nothing rather than a defective one."
)
ONE_RULE_LINE = (
    "**This repository's own rules:** `rules/CALLER-RULES.md` \u2014 declared under "
    "`rules` in its `harness.json`, to be read after the charter above. They bind this "
    "repository alone."
)

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


class TheCharterIsNamedWhereTheReviewerCanOpenIt(unittest.TestCase):
    """`instrument_relative`: the charter path is a deployment fact, not a constant.

    Bought by a real failure. The caller's duplicate copy of the instrument was deleted, and
    the very next dispatch handed a reviewer
    `ResearchSystem/migration/…/v3-harness-review-contract.md` — a path that had just stopped
    resolving there, because from the caller the instrument now lives under the submodule
    mount. A prompt whose one job is to name the charter had named a file nobody could open.

    Both directions are pinned, and every expectation below is a hand-written literal rather
    than the module's own constant (`E5`).
    """

    #: A member this module still names, hand-written and not read back from it (`E5`).
    #: It was the review-side contract stub until round CORE-ONLY-CODE moved the mode
    #: that named it out of this module and deleted the stub with it.
    MEMBER = "document-harness/REVIEW.md"

    #: Both deployments are BUILT, never read off the live checkout. The first form of these
    #: two tests derived its subject from where this clone happens to sit
    #: (`Path(D.__file__).parents[3].parents[2]`), which is the caller root on the one machine
    #: where the only clone of this repository is a submodule mount — and is two levels above
    #: the repository root in a plain `git clone`, where the assertion failed and took the
    #: whole battery red with it. `E5` asks the expectation to be independent of the thing it
    #: guards; an expectation applied to an environment-derived input is the same defect on
    #: the input side, and a mutation cannot surface it (the FULL of `2d148f3`, B-3).
    def _layout(self, tmp: str, instrument_within: str):
        """A repository root and an instrument planted at a stated depth inside it."""
        root = pathlib.Path(tmp).resolve()
        instrument = root.joinpath(*instrument_within.split("/"))
        instrument.mkdir(parents=True)
        return root, mock.patch("rsclib.document_harness.RS_ROOT", instrument)

    def test_a_caller_that_mounts_the_instrument_gets_the_path_through_the_mount(self):
        with tempfile.TemporaryDirectory() as tmp:
            root, patched = self._layout(tmp, "ResearchSystem/harness")
            with patched:
                self.assertEqual(
                    D.instrument_relative(root, self.MEMBER),
                    "ResearchSystem/harness/" + self.MEMBER,
                )

    def test_the_instruments_own_repo_gets_the_members_own_path(self):
        """Since round DE-PREFIX the instrument root IS the repository root, so the
        repo-relative answer coincides byte-for-byte with the member's own name — reached
        here through `relative_to` succeeding, where the negative control below reaches the
        same bytes through it failing."""
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp).resolve()
            with mock.patch("rsclib.document_harness.RS_ROOT", root):
                self.assertEqual(D.instrument_relative(root, self.MEMBER), self.MEMBER)

    def test_a_repo_that_does_not_contain_the_instrument_gets_the_member_name(self):
        """The negative control: no repo-relative answer exists, and none is invented."""
        scn = build_scenario()
        self.assertEqual(D.instrument_relative(scn.repo.root, self.MEMBER), self.MEMBER)

    def test_the_resolved_charter_is_what_reaches_the_prompt(self):
        scn = build_scenario()
        d = D.dispatch_of(scn.repo.root, scn.evidence_commit)
        self.assertEqual(d.charter, self.MEMBER)
        self.assertIn(f"`{self.MEMBER}`", D.render_dispatch(d))


class ExecutorDispatchesGenerateToo(unittest.TestCase):
    """The second family (round EXECUTOR-CHARTER, 2026-08-22 ruling): the executor's own
    charter, delivered instead of hand-copied.

    Three facts and nothing more — run id, frozen instruction path and revision, charter
    pointer. The executor is dispatched at the START of a run, when the run directory
    holds a frozen instruction.md and little else; the WorkSpec is authored by the
    executor afterwards, so nothing else committed exists to derive, and an enumeration of
    what to do would be the shadow WorkSpec the module's rendering section refuses.
    """

    FIXTURE = pathlib.Path(__file__).parents[1] / "fixtures" / "expected-executor-prompt.txt"

    #: Hand-written, never read back from the module (`E5`): the charter a subject
    #: repository that does NOT contain the instrument gets.
    CHARTER_OUTSIDE = "document-harness/EXECUTION.md"

    RUN_DIR = "assurance/runs/run-one"

    def _run_repo(self) -> TempRepo:
        return TempRepo({f"{self.RUN_DIR}/instruction.md": "# Task\n\nDo the thing.\n"})

    def test_the_prompt_is_exactly_the_golden_file(self):
        """Added, missing and reordered lines all fail here, in one comparison."""
        with self._run_repo() as repo:
            d = D.executor_dispatch_of(repo.root, self.RUN_DIR)
            self.assertTrue(d.report.ok, codes(d.report))
            expected = self.FIXTURE.read_text(encoding="utf-8").format(
                charter=self.CHARTER_OUTSIDE,
                declared_rules=NO_RULES_LINE,
                run_id="run-one",
                instruction_path=f"{self.RUN_DIR}/instruction.md",
                revision=repo.base,
            )
            self.assertEqual(D.render_executor_dispatch(d), expected)

    def test_the_three_facts_come_out_of_the_committed_state(self):
        with self._run_repo() as repo:
            d = D.executor_dispatch_of(repo.root, self.RUN_DIR)
            self.assertEqual(d.run_id, "run-one")
            self.assertEqual(d.instruction_path, f"{self.RUN_DIR}/instruction.md")
            self.assertEqual(d.revision, repo.base)
            self.assertEqual(len(d.revision), 40)

    def test_an_absolute_run_dir_derives_the_same_dispatch(self):
        with self._run_repo() as repo:
            relative = D.executor_dispatch_of(repo.root, self.RUN_DIR)
            absolute = D.executor_dispatch_of(repo.root, repo.root / self.RUN_DIR)
            self.assertTrue(absolute.report.ok, codes(absolute.report))
            self.assertEqual(
                (absolute.run_id, absolute.instruction_path, absolute.revision),
                (relative.run_id, relative.instruction_path, relative.revision),
            )

    def test_a_run_directory_outside_the_repository_is_refused(self):
        with self._run_repo() as repo, tempfile.TemporaryDirectory() as elsewhere:
            d = D.executor_dispatch_of(repo.root, elsewhere)
            self.assertIn(f"{D.CODE}-RUN-OUTSIDE-REPO", codes(d.report))

    def test_a_directory_without_an_instruction_is_refused(self):
        with self._run_repo() as repo:
            (repo.root / "assurance/runs/run-two").mkdir(parents=True)
            d = D.executor_dispatch_of(repo.root, "assurance/runs/run-two")
            self.assertIn(f"{D.CODE}-INSTRUCTION-MISSING", codes(d.report))

    def test_an_uncommitted_instruction_is_not_frozen(self):
        with self._run_repo() as repo:
            repo.write({"assurance/runs/run-three/instruction.md": "# Task\n"})
            d = D.executor_dispatch_of(repo.root, "assurance/runs/run-three")
            self.assertIn(f"{D.CODE}-INSTRUCTION-UNFROZEN", codes(d.report))

    def test_a_worktree_that_drifted_from_the_frozen_bytes_is_refused(self):
        with self._run_repo() as repo:
            repo.write({f"{self.RUN_DIR}/instruction.md": "# Task\n\nEdited after the freeze.\n"})
            d = D.executor_dispatch_of(repo.root, self.RUN_DIR)
            self.assertIn(f"{D.CODE}-INSTRUCTION-DRIFTED", codes(d.report))

    def test_a_refusal_is_not_a_prompt_and_restates_no_run(self):
        """So a broken dispatch cannot be routed by pasting past the warning."""
        with self._run_repo() as repo:
            repo.write({f"{self.RUN_DIR}/instruction.md": "# Task\n\nEdited after the freeze.\n"})
            doc = D.render_executor_dispatch(D.executor_dispatch_of(repo.root, self.RUN_DIR))
            self.assertIn("NOT DISPATCHABLE", doc)
            self.assertNotIn("Run:", doc)
            self.assertNotIn("Instruction:", doc)

    def test_no_enumeration_of_work_reaches_the_executor(self):
        """The shadow-WorkSpec refusal, inherited: no hunt list, no obligations, no `§`."""
        with self._run_repo() as repo:
            prompt = D.render_executor_dispatch(D.executor_dispatch_of(repo.root, self.RUN_DIR))
            self.assertIn(self.CHARTER_OUTSIDE, prompt)
            self.assertNotIn("hunt", prompt.lower())
            self.assertNotIn("FILL IN", prompt)
            self.assertNotIn("obligation", prompt.lower())
            self.assertNotIn("§", prompt)

    def test_the_dispatchers_view_carries_the_derivation(self):
        with self._run_repo() as repo:
            derivation = D.render_executor_derivation(
                D.executor_dispatch_of(repo.root, self.RUN_DIR)
            )
            self.assertIn("run-one", derivation)
            self.assertIn(repo.base, derivation)

    def test_a_caller_that_mounts_the_instrument_gets_the_path_through_the_mount(self):
        """Rider `exec-mount-test`: the construction side had this pin, the product side did not.

        The product mode is the one a caller actually dispatches from, and a caller mounts
        the instrument as a submodule — so the charter it is handed has to travel through
        the mount, not name a path that resolves nowhere in the subject repository.
        """
        with self._run_repo() as repo:
            instrument = repo.root / "ResearchSystem" / "harness"
            instrument.mkdir(parents=True)
            with mock.patch("rsclib.document_harness.RS_ROOT", instrument):
                d = D.executor_dispatch_of(repo.root, self.RUN_DIR)
                self.assertTrue(d.report.ok, codes(d.report))
                self.assertEqual(
                    d.charter, "ResearchSystem/harness/" + self.CHARTER_OUTSIDE
                )


class EveryPromptNamesWhatTheRepositoryDeclares(unittest.TestCase):
    """`E10`'s second sentence, built (round CORE-ONLY-CODE, plan ruling 9 and item H).

    Until this round the sentence was an obligation on this command that the command did not
    meet: a cold session reached a repository's own rules only if something outside the
    dispatch happened to name them. Both prompts this module still writes now carry the line,
    and both forms of it are pinned — a repository that declares rules, and one that declares
    none, which is the negative control (`E4`) and also the case a caller starts in.

    Both expectations are hand-written whole lines (`E5`), never read back from the module:
    an expectation taken from the constant would pass whatever the constant said.
    """

    RULE = "rules/CALLER-RULES.md"

    def _declare(self, repo_root, *rules):
        (repo_root / "harness.json").write_text(
            json.dumps({"policy": None, "rules": list(rules)}, indent=1) + "\n",
            encoding="utf-8",
        )

    def test_the_product_review_prompt_names_the_declaration(self):
        scn = build_scenario()
        self._declare(scn.repo.root, self.RULE)
        doc = D.render_dispatch(D.dispatch_of(scn.repo.root, scn.evidence_commit))
        self.assertIn(ONE_RULE_LINE, doc)

    def test_the_product_review_prompt_says_so_when_nothing_is_declared(self):
        """Negative control: the line is present and says which case this is."""
        scn = build_scenario()
        doc = D.render_dispatch(D.dispatch_of(scn.repo.root, scn.evidence_commit))
        self.assertIn(NO_RULES_LINE, doc)
        self.assertNotIn(self.RULE, doc)

    def test_the_executor_prompt_names_the_declaration(self):
        with TempRepo({"assurance/runs/run-one/instruction.md": "# Task\n"}) as repo:
            self._declare(repo.root, self.RULE)
            doc = D.render_executor_dispatch(
                D.executor_dispatch_of(repo.root, "assurance/runs/run-one")
            )
            self.assertIn(ONE_RULE_LINE, doc)

    def test_the_executor_prompt_says_so_when_nothing_is_declared(self):  # negative control
        with TempRepo({"assurance/runs/run-one/instruction.md": "# Task\n"}) as repo:
            doc = D.render_executor_dispatch(
                D.executor_dispatch_of(repo.root, "assurance/runs/run-one")
            )
            self.assertIn(NO_RULES_LINE, doc)

    def test_two_declarations_are_both_named(self):
        with TempRepo({"assurance/runs/run-one/instruction.md": "# Task\n"}) as repo:
            self._declare(repo.root, "rules/A.md", "rules/B.md")
            doc = D.render_executor_dispatch(
                D.executor_dispatch_of(repo.root, "assurance/runs/run-one")
            )
            self.assertIn("`rules/A.md` \u00b7 `rules/B.md`", doc)

    def test_the_declaration_is_the_swept_repositorys_and_not_this_ones(self):
        """The defect a generator reading its own root would have, asserted directly."""
        with TempRepo({"assurance/runs/run-one/instruction.md": "# Task\n"}) as repo:
            self._declare(repo.root, self.RULE)
            doc = D.render_executor_dispatch(
                D.executor_dispatch_of(repo.root, "assurance/runs/run-one")
            )
            self.assertNotIn("CONSTRUCTION-CHECKLIST.md", doc)


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
        self.assertEqual(len(declared), 13, f"code surface moved: {sorted(declared)}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
