#!/usr/bin/env python3
"""Wave-2 acceptance matrix: the commit-bound review subject (W2-A1..A5, A7, A9, A10).

Every method asserts an exact issue **code**, an exact schema outcome or an exact
exception, and each "must fire" case is paired with (or shares) a negative control — the
clean scenario itself, asserted clean before any perturbation is trusted to mean anything.

The scenario is a real disposable Git repository carrying a complete committed control
plane (state + work-spec + resolved-plan + candidate-record + coverage + one file per
CheckResult), because the property under test is precisely that everything is derived
from a commit rather than from documents a caller hands over. Identity and result-binding
tests share one class-level scenario and perturb only in-memory dicts; tests that need a
different committed shape build their own repository.

`NamedIssueReachability` pins the layer's full issue-code surface: every code declared in
`review_subject.py` **or** `review_result_v2.py` must be asserted by name somewhere in this
file, so a code added without a test shows up as a failure here rather than as silent dead
surface. The sweep reads both modules by name, so moving a code between them changes
nothing and dropping a module from the sweep fails the count assertion.
"""
from __future__ import annotations

import copy
import importlib.util
import json
import pathlib
import re
import shutil
import types
import unittest

from _harness import RS_ROOT, TempRepo, git

from rsclib.document_harness import AssuranceFault, SpecGap, bytes_digest, canonical_digest
from rsclib.document_harness import assurance_state
from rsclib.document_harness import review_result_v2 as RV
from rsclib.document_harness import review_subject as RS

FAKE_REV = "f" * 40
OTHER_COMMIT = "9" * 40
WRONG_DIGEST = "b" * 64
CONTROL_ROOT = "runs/run-one"
EXECUTOR = "executor agent"
REVIEWER = "independent reviewer"

INSTRUCTION = (
    "# Task instruction\n\nRun condition: the candidate stays on its isolated branch.\n\n"
    "## Task\n\nWrite the guide.\n"
)

TEMPLATE_DIR = RS_ROOT / "assurance" / "templates" / "run-v2"


def codes(report) -> list[str]:
    return [issue.code for issue in report.issues]


# ---------------------------------------------------------------------------
# Scenario: one committed control plane in a disposable repository
# ---------------------------------------------------------------------------


def build_scenario(
    *,
    spec_mut=None,
    plan_mut=None,
    record_mut=None,
    state_mut=None,
    drop_files=(),
    extra_files=None,
    file_overrides=None,
) -> types.SimpleNamespace:
    """A complete, clean, committed control plane; every mutator is a seeded defect."""
    repo = TempRepo({"docs/instruction.md": INSTRUCTION})
    candidate = repo.commit_candidate({"docs/guide.md": "# Guide\n"})
    git(repo.root, "checkout", "-q", "main")
    repo.branch = "main"

    spec = {
        "work_id": "work-one",
        "objective": "verify the wave-2 subject machinery",
        "instruction_ref": {"path": "docs/instruction.md", "revision": repo.base},
        "instruction_units": [
            {
                "unit_id": "unit-one",
                "locator": {"path": "docs/instruction.md", "anchor": "## Task"},
                "classification": "obligation",
                "obligation_ids": ["ob-one"],
            }
        ],
        "change_boundary": {"write_scope": ["docs"], "out": ["runs"]},
        "expected_artifacts": [{"artifact_id": "art-guide", "path": "docs/guide.md"}],
        "obligations": [
            {
                "obligation_id": "ob-one",
                "instruction_unit_ids": ["unit-one"],
                "requirement": "the guide exists and is checked",
                "verification_mode": "local_check",
                "local_check_refs": ["chk-one"],
            }
        ],
    }
    if spec_mut:
        spec_mut(spec)
    record = {
        "record_id": "rec-one",
        "work_id": "work-one",
        "run_id": "run-one",
        "repair_round": 0,
        "candidate_ref": {"branch": "cand", "commit": candidate},
        "base_revision": repo.base,
        "control_root": CONTROL_ROOT,
        "fulfillment": {
            "authored_by": EXECUTOR,
            "claims": [
                {
                    "obligation_id": "ob-one",
                    "status": "IMPLEMENTED",
                    "implementation_locators": [{"path": "docs/guide.md", "anchor": "# Guide"}],
                }
            ],
        },
        "manifest": {
            "authored_by": "diff verifier",
            "boundary_result": "CONFORMANT",
            "expected_artifact_results": [{"artifact_id": "art-guide", "present": True}],
            "changes": [{"path": "docs/guide.md", "change_kind": "added"}],
        },
    }
    if record_mut:
        record_mut(record)
    check_result = {
        "result_id": "res-chk-one",
        "check_id": "chk-one",
        "kind": "file_exists",
        "request_digest_sha256": "a" * 64,
        "candidate_ref": {"branch": "cand", "commit": candidate},
        "observed_tree": {"kind": "candidate_commit", "revision": candidate},
        "result": "PASS",
        "verified_by": "deterministic verifier",
    }
    spec_text = json.dumps(spec, indent=1)
    plan = {
        "plan_id": "plan-one",
        "work_id": "work-one",
        "work_spec_ref": {
            "path": "control/work-spec.json",
            "digest_sha256": bytes_digest(spec_text.encode("utf-8")),
        },
        "resolver_version": "1.0.0",
        "effective_change_boundary": {"write_scope": ["docs"], "out": ["runs"]},
        "repair_cap": 1,
        "check_order": ["chk-one"],
    }
    if plan_mut:
        plan_mut(plan)

    files = {
        f"{CONTROL_ROOT}/control/work-spec.json": spec_text,
        f"{CONTROL_ROOT}/control/resolved-plan.json": json.dumps(plan, indent=1),
        f"{CONTROL_ROOT}/evidence/candidate-record.json": json.dumps(record, indent=1),
        f"{CONTROL_ROOT}/evidence/coverage.json": json.dumps({"rows": ["ob-one"]}, indent=1),
        f"{CONTROL_ROOT}/evidence/check-chk-one.json": json.dumps(check_result, indent=1),
        f"{CONTROL_ROOT}/evidence/check-results.json": json.dumps([check_result], indent=1),
    }
    if file_overrides:
        files.update(file_overrides)
    for dropped in drop_files:
        files.pop(dropped, None)
    state = {
        "work_id": "work-one",
        "run_id": "run-one",
        "status": "EVIDENCED",
        "repair_round": 0,
        "work_spec_ref": _ref(files, f"{CONTROL_ROOT}/control/work-spec.json"),
        "resolved_plan_ref": _ref(files, f"{CONTROL_ROOT}/control/resolved-plan.json"),
        "fulfillment_ref": _ref(files, f"{CONTROL_ROOT}/evidence/candidate-record.json"),
        "manifest_ref": _ref(files, f"{CONTROL_ROOT}/evidence/candidate-record.json"),
        "check_results_ref": _ref(files, f"{CONTROL_ROOT}/evidence/check-results.json"),
        "coverage_ref": _ref(files, f"{CONTROL_ROOT}/evidence/coverage.json"),
    }
    if state_mut:
        state_mut(state)
    files[f"{CONTROL_ROOT}/control/state.json"] = json.dumps(state, indent=1)
    repo.write(files)
    if extra_files:
        repo.write(extra_files)
    evidence_commit = repo.commit_all("evidence commit")

    subject = RS.subject_of(
        evidence_commit=evidence_commit,
        candidate_ref={"branch": "cand", "commit": candidate},
        base_revision=repo.base,
        control_root=CONTROL_ROOT,
        repair_round=0,
    )
    return types.SimpleNamespace(
        repo=repo, candidate=candidate, evidence_commit=evidence_commit, subject=subject,
        spec=spec, record=record,
    )


def _ref(files: dict, path: str) -> dict:
    if path in files:
        return {"path": path, "digest_sha256": bytes_digest(files[path].encode("utf-8"))}
    return {"path": path, "digest_sha256": WRONG_DIGEST}


def make_result(scn, **overrides) -> dict:
    result = {
        "schema_version": "2",
        "result_id": "res-one",
        "work_id": "work-one",
        "run_id": "run-one",
        "review_round": "FULL",
        "subject": copy.deepcopy(scn.subject),
        "verdict": "REVIEWED_NO_BLOCKER",
        "instruction_completeness": {
            "result": "COMPLETE",
            "instruction_ref": {"path": "docs/instruction.md", "revision": scn.repo.base},
        },
        "per_obligation_disposition": [{"obligation_id": "ob-one", "disposition": "SUPPORTED"}],
        "residual_uncertainty": [],
        "reviewed_by": REVIEWER,
    }
    result.update(overrides)
    return result


# ---------------------------------------------------------------------------
# W2-A3 — version keying: explicit, fail closed, no cross-version fallback
# ---------------------------------------------------------------------------


class VersionKeying(unittest.TestCase):
    def test_absent_keys_to_v1_and_declared_2_to_v2(self):
        self.assertEqual(RV.result_schema_kind({}), "review_result")
        self.assertEqual(RV.result_schema_kind({"schema_version": "2"}), "review_result_v2")

    def test_present_but_null_and_unknown_values_stop(self):
        for declared in (None, "1", "3", 2, {"v": 2}):
            with self.subTest(declared=declared):
                with self.assertRaises(SpecGap):
                    RV.result_schema_kind({"schema_version": declared})

    def test_v1_result_handed_to_v2_checker_stops(self):
        with self.assertRaises(SpecGap):
            RV.check_review_result_v2({}, ".", evidence_commit=FAKE_REV)

    def test_v2_failure_is_reported_against_v2_never_v1(self):
        report = RS.validate_w2("review_result_v2", {"schema_version": "2"})
        self.assertFalse(report.ok)
        self.assertTrue(all(code == "V3-SCHEMA-REVIEW_RESULT_V2" for code in codes(report)))


# ---------------------------------------------------------------------------
# W2-A1 — schema shape: subject binding required, package surface unrepresentable
# ---------------------------------------------------------------------------


class SchemaShape(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scn = build_scenario()

    @classmethod
    def tearDownClass(cls):
        cls.scn.repo.cleanup()

    def test_valid_v2_result_is_accepted(self):
        self.assertTrue(RS.validate_w2("review_result_v2", make_result(self.scn)).ok)

    def test_subjectless_packageful_and_hybrid_are_rejected(self):
        subjectless = make_result(self.scn)
        del subjectless["subject"]
        packageful = make_result(self.scn, package_ref={"path": "p.json", "digest_sha256": "a" * 64})
        del packageful["subject"]
        hybrid = make_result(self.scn, package_ref={"path": "p.json", "digest_sha256": "a" * 64})
        for label, document in (("subject-less", subjectless), ("package-bound", packageful),
                                ("both-present hybrid", hybrid)):
            with self.subTest(label=label):
                self.assertFalse(RS.validate_w2("review_result_v2", document).ok)

    def test_subject_requires_all_five_fields(self):
        for field in ("evidence_commit", "candidate_ref", "base_revision", "control_root",
                      "repair_round"):
            with self.subTest(field=field):
                result = make_result(self.scn)
                del result["subject"][field]
                self.assertFalse(RS.validate_w2("review_result_v2", result).ok)

    def test_round_conditionals_carried_over_from_v1(self):
        verify_without_scope = make_result(self.scn, review_round="VERIFY")
        full_with_scope = make_result(
            self.scn,
            verify_scope={"accepted_finding_ids": ["f-one"], "repair_diff_reviewed": True,
                          "permanent_boundaries_checked": True},
        )
        changes_without_findings = make_result(self.scn, verdict="CHANGES_REQUIRED")
        for label, document in (("VERIFY without scope", verify_without_scope),
                                ("FULL with scope", full_with_scope),
                                ("CHANGES_REQUIRED without findings", changes_without_findings)):
            with self.subTest(label=label):
                self.assertFalse(RS.validate_w2("review_result_v2", document).ok)

    def test_the_two_verdict_conditionals_round_2_added(self):
        """Round `PROMISE-PATH-VOCAB`, item 2: the value is VERIFY-only and names a finding.

        The root enum is now the UNION of the two rounds, so `UNRESOLVED_BLOCKER` is a legal
        root value and only the FULL narrowing keeps a FULL from returning it — a narrowing
        this round had to ADD, because until now the root enum was the FULL set and the FULL
        branch constrained `verify_scope` alone. The first case is that narrowing; without it
        contract §5's FULL row would be closed on paper and open in the schema.
        """
        scope = {"accepted_finding_ids": ["f-one"], "repair_diff_reviewed": True,
                 "permanent_boundaries_checked": True}
        low = {"finding_id": "f-style", "blocking": False,
               "statement": "two headings use different capitalisation"}
        for label, document in (
            ("FULL reaching for the VERIFY-only value",
             make_result(self.scn, verdict="UNRESOLVED_BLOCKER", findings=[low])),
            ("UNRESOLVED_BLOCKER naming no finding at all",
             make_result(self.scn, review_round="VERIFY", verify_scope=scope,
                         verdict="UNRESOLVED_BLOCKER")),
            ("VERIFY reaching for CHANGES_REQUIRED",
             make_result(self.scn, review_round="VERIFY", verify_scope=scope,
                         verdict="CHANGES_REQUIRED", findings=[low])),
        ):
            with self.subTest(label=label):
                self.assertFalse(RS.validate_w2("review_result_v2", document).ok)
        # Negative controls: each differs from a case above by exactly one field, so a
        # schema that simply refused everything would fail here.
        for label, document in (
            ("VERIFY returning it, with a finding",
             make_result(self.scn, review_round="VERIFY", verify_scope=scope,
                         verdict="UNRESOLVED_BLOCKER", findings=[low])),
            ("FULL returning a FULL value", make_result(self.scn, verdict="SPEC_GAP")),
        ):
            with self.subTest(label=label):
                self.assertTrue(RS.validate_w2("review_result_v2", document).ok)


# ---------------------------------------------------------------------------
# W2-A4 — pointer_to writes bytes digests; the resume guard keeps its teeth
# ---------------------------------------------------------------------------


class PointerHelper(unittest.TestCase):
    def test_pointer_to_writes_the_bytes_digest_not_the_canonical_one(self):
        with TempRepo() as repo:
            document = {"b": 2, "a": 1}
            (repo.root / "doc.json").write_text(json.dumps(document, indent=1), encoding="utf-8")
            ref = assurance_state.pointer_to("doc.json", repo.root)
            raw = (repo.root / "doc.json").read_bytes()
            self.assertEqual(ref["digest_sha256"], bytes_digest(raw))
            # On an indent-formatted file the two digest kinds genuinely differ, so the
            # w1-r1 mistake (canonical digest in a bytes pointer) is demonstrably not
            # what the helper produces.
            self.assertNotEqual(ref["digest_sha256"], canonical_digest(document))

    def test_pointer_to_a_missing_file_is_a_fault_at_write_time(self):
        with TempRepo() as repo:
            with self.assertRaises(AssuranceFault):
                assurance_state.pointer_to("missing.json", repo.root)

    def test_every_digest_protected_field_is_a_pointer_field(self):
        """The CLASS FULL `97cc298` `B-2` was one instance of (`E7`).

        `pointer_for` writes a digest on every `DIGEST_PROTECTED_FIELDS` member, and the
        readers that resolve and verify a state's pointers walk `POINTER_FIELDS` —
        `assurance_state.resume`, `ResumePoint.render`. A name in the first set and not the
        second is written with a digest nothing in this repository ever reads, which is
        exactly what `bind_authorization_ref` was for one round.

        Both sets are read from the module here, and that is the point rather than a lapse:
        the property is a RELATION between them, and hand-writing either side would pin the
        one name this finding reported instead of the rule it broke. The membership of the
        protected set is pinned by hand in the test below, which is where that belongs.
        """
        self.assertEqual(
            sorted(set(assurance_state.DIGEST_PROTECTED_FIELDS)
                   - set(assurance_state.POINTER_FIELDS)),
            [],
            "a digest is written on this field and no reader of the state resolves it",
        )

    def test_pointer_for_writes_a_digest_on_exactly_the_protected_fields(self):
        """The narrowed policy, held by hand-written field names (never the module's set).

        Importing `DIGEST_PROTECTED_FIELDS` here would make the test agree with whatever the
        module currently says, including after an edit that widened or emptied it. The six
        names are therefore typed out, and every other state field is checked to carry the
        path alone. Six since round `PROMISE-PATH-VOCAB`: `bind_authorization_ref` joined
        them as the fourth user-decision pointer, protected for the reason the other three
        are — it names a document the user authored and the executor may not rewrite.
        """
        protected = ("work_spec_ref", "start_decision_ref", "repair_decision_ref",
                     "bind_authorization_ref", "final_decision_ref", "review_ref")
        unprotected = ("resolved_plan_ref", "instruction_audit_ref", "fulfillment_ref",
                       "manifest_ref", "check_results_ref", "coverage_ref",
                       "assurance_candidate_ref", "summary_ref")
        document = {"b": 2, "a": 1}
        pretty = json.dumps(document, indent=1)
        with TempRepo() as repo:
            (repo.root / "doc.json").write_text(pretty, encoding="utf-8")
            # Digest the bytes that landed, never the string handed to `write_text`: on
            # Windows the newline translation makes those two different files, and a
            # fixture asserting the un-translated form fails for a reason that has nothing
            # to do with the policy under test.
            expected = bytes_digest((repo.root / "doc.json").read_bytes())
            for field in protected:
                with self.subTest(field=field, expect="digest"):
                    ref = assurance_state.pointer_for(field, "doc.json", repo.root)
                    self.assertEqual(ref, {"path": "doc.json", "digest_sha256": expected})
            for field in unprotected:
                with self.subTest(field=field, expect="path only"):
                    ref = assurance_state.pointer_for(field, "doc.json", repo.root)
                    self.assertEqual(ref, {"path": "doc.json"})

    def test_pointer_for_keeps_the_write_time_existence_fault_on_every_field(self):
        """Narrowing removed the digest, never the check that the target is actually there.

        The unprotected branch computes no digest and so never reads the file — which is
        exactly how the fault `pointer_to` documents could have been dropped for those
        fields without any test noticing.
        """
        with TempRepo() as repo:
            for field in ("work_spec_ref", "coverage_ref"):
                with self.subTest(field=field):
                    with self.assertRaises(AssuranceFault):
                        assurance_state.pointer_for(field, "missing.json", repo.root)

    def test_resume_still_refuses_a_hand_written_wrong_digest(self):
        # The document must be one whose canonical bytes DIFFER from its file bytes —
        # `{}` digests identically either way, so a fixture using it would assert the
        # guard from a case that carries no mismatch at all.
        document = {"b": 2, "a": 1}
        pretty = json.dumps(document, indent=1)
        with TempRepo() as repo:
            (repo.root / "spec.json").write_text(pretty, encoding="utf-8")
            (repo.root / "plan.json").write_text(pretty, encoding="utf-8")
            self.assertNotEqual(canonical_digest(document),
                                bytes_digest(pretty.encode("utf-8")))
            state = {
                "work_id": "work-one", "run_id": "run-one", "status": "RESOLVED",
                "repair_round": 0,
                "work_spec_ref": assurance_state.pointer("spec.json",
                                                         canonical_digest(document)),
                "resolved_plan_ref": assurance_state.pointer_to("plan.json", repo.root),
            }
            assurance_state.save(state, repo.root / "state.json")
            point = assurance_state.resume(repo.root / "state.json", repo.root)
            self.assertIn("V3-STATE-POINTER-STALE", [i.code for i in point.report.issues])
            self.assertIn("resolved_plan_ref", point.verified)


# ---------------------------------------------------------------------------
# W2-A2 / W2-A9 / W2-A10 — the committed subject: completeness, identity, containment
# ---------------------------------------------------------------------------


class SubjectAgainstCleanPlane(unittest.TestCase):
    """Perturbations of subject/result dicts against ONE clean committed plane."""

    @classmethod
    def setUpClass(cls):
        cls.scn = build_scenario()
        clean = RS.check_subject(cls.scn.subject, cls.scn.repo.root)
        assert clean.ok, "negative control broken: " + "; ".join(clean.rendered())

    @classmethod
    def tearDownClass(cls):
        cls.scn.repo.cleanup()

    def test_the_clean_scenario_is_clean(self):
        self.assertTrue(RS.check_subject(self.scn.subject, self.scn.repo.root).ok)

    def test_subject_identity_mismatches_each_fire(self):
        for field, value, code in (
            ("candidate_ref", {"branch": "cand", "commit": OTHER_COMMIT},
             "V3-SUBJECT-WRONG-CANDIDATE"),
            ("candidate_ref", {"branch": "other", "commit": self.scn.candidate},
             "V3-SUBJECT-CANDIDATE-BRANCH-MISMATCH"),
            ("base_revision", FAKE_REV, "V3-SUBJECT-BASE-MISMATCH"),
            ("repair_round", 1, "V3-SUBJECT-ROUND-MISMATCH"),
        ):
            with self.subTest(code=code):
                subject = copy.deepcopy(self.scn.subject)
                subject[field] = value
                self.assertIn(code, codes(RS.check_subject(subject, self.scn.repo.root)))

    def test_state_unreachable_control_root_is_reported(self):
        subject = copy.deepcopy(self.scn.subject)
        subject["control_root"] = "runs/elsewhere"
        report = RS.check_subject(subject, self.scn.repo.root)
        self.assertIn("V3-SUBJECT-POINTER-MISSING", codes(report))
        self.assertFalse(report.ok)

    def test_result_binding_mismatches_each_fire(self):
        scn = self.scn
        wrong_round = make_result(scn, review_round="VERIFY", verify_scope={
            "accepted_finding_ids": ["f-one"], "repair_diff_reviewed": True,
            "permanent_boundaries_checked": True})
        for label, result, code in (
            ("foreign work_id", make_result(scn, work_id="work-two"), "V3-REVIEW-WORK-MISMATCH"),
            ("foreign run_id", make_result(scn, run_id="run-two"), "V3-REVIEW-RUN-MISMATCH"),
            ("VERIFY answering a round-0 candidate", wrong_round, "V3-REVIEW-ROUND-MISMATCH"),
        ):
            with self.subTest(label=label):
                report = RV.check_review_result_v2(
                    result, scn.repo.root, evidence_commit=scn.evidence_commit,
                    executor=EXECUTOR)
                self.assertIn(code, codes(report))

    def test_result_answering_a_different_evidence_commit_is_refused(self):
        # A second, containment-clean commit inside the control root: the control plane
        # is unchanged at it, so ONLY the binding mismatch distinguishes the two.
        self.scn.repo.write({f"{CONTROL_ROOT}/control/note.md": "later note\n"})
        later = self.scn.repo.commit_all("later control commit")
        result = make_result(self.scn)
        result["subject"]["evidence_commit"] = later
        report = RV.check_review_result_v2(
            result, self.scn.repo.root, evidence_commit=self.scn.evidence_commit,
            executor=EXECUTOR)
        self.assertIn("V3-REVIEW-SUBJECT-COMMIT-MISMATCH", codes(report))

    def test_obligation_coverage_and_finding_coherence(self):
        scn = self.scn
        undisposed = make_result(scn, per_obligation_disposition=[
            {"obligation_id": "ob-ghost", "disposition": "SUPPORTED"}])
        duplicate = make_result(scn, per_obligation_disposition=[
            {"obligation_id": "ob-one", "disposition": "SUPPORTED"},
            {"obligation_id": "ob-one", "disposition": "UNVERIFIABLE", "note": "said twice"}])
        dangling = make_result(scn, per_obligation_disposition=[
            {"obligation_id": "ob-one", "disposition": "NOT_SUPPORTED", "note": "contradicted",
             "finding_ids": ["f-ghost"]}], verdict="CHANGES_REQUIRED", findings=[
            {"finding_id": "f-real", "blocking": False, "statement": "a stated non-blocker"}])
        unsupported = make_result(scn, per_obligation_disposition=[
            {"obligation_id": "ob-one", "disposition": "NOT_SUPPORTED", "note": "contradicted"}])
        blocker = make_result(scn, findings=[
            {"finding_id": "f-block", "blocking": True, "statement": "a blocking defect",
             "candidate_locator": {"path": "docs/guide.md", "anchor": "# Guide"},
             "ground_truth_locator": {"path": "docs/instruction.md", "anchor": "## Task"},
             "minimum_fix": "repair the guide"}])
        mismatched = make_result(scn)
        mismatched["instruction_completeness"]["instruction_ref"]["revision"] = FAKE_REV
        cases = (
            ("undisposed + undeclared", undisposed,
             ("V3-REVIEW-OBLIGATION-UNDISPOSED", "V3-REVIEW-UNDECLARED-DISPOSITION")),
            ("duplicate disposition", duplicate, ("V3-REVIEW-DUPLICATE-DISPOSITION",)),
            ("dangling finding ref", dangling, ("V3-REVIEW-DANGLING-FINDING-REF",)),
            ("NOT_SUPPORTED naming nothing", unsupported,
             ("V3-REVIEW-UNSUPPORTED-WITHOUT-FINDING",)),
            ("blocker under a no-blocker verdict", blocker,
             ("V3-REVIEW-BLOCKER-CONTRADICTS-VERDICT",)),
            ("recheck of a different instruction", mismatched, ("V3-REVIEW-INSTRUCTION-MISMATCH",)),
        )
        for label, result, expected in cases:
            with self.subTest(label=label):
                report = RV.check_review_result_v2(
                    result, scn.repo.root, evidence_commit=scn.evidence_commit,
                    executor=EXECUTOR)
                for code in expected:
                    self.assertIn(code, codes(report))

    def test_an_unresolved_blocker_verdict_must_name_the_blocker_that_stands(self):
        """Round `PROMISE-PATH-VOCAB`, item 2: the other half of the same reconciliation.

        `review.v2.schema.json` gets as far as requiring `findings` on this verdict. Whether
        any of them is BLOCKING is a value it cannot see — the verdict and the findings sit
        in separate subschemas — so the schema says so in its own description and this
        function, which holds both at once, carries it. Mirror of the
        `BLOCKER-CONTRADICTS-VERDICT` case above: that one is a blocker under a verdict
        claiming none, this one a verdict claiming one over no blocker.
        """
        scn = self.scn
        scope = {"accepted_finding_ids": ["f-one"], "repair_diff_reviewed": True,
                 "permanent_boundaries_checked": True}
        low = {"finding_id": "f-style", "blocking": False,
               "statement": "two headings use different capitalisation"}
        stands = {"finding_id": "f-block", "blocking": True,
                  "statement": "the repair did not close the blocking defect",
                  "candidate_locator": {"path": "docs/guide.md", "anchor": "# Guide"},
                  "ground_truth_locator": {"path": "docs/instruction.md", "anchor": "## Task"},
                  "minimum_fix": "repair the guide"}
        names_none = make_result(scn, review_round="VERIFY", verify_scope=scope,
                                 verdict="UNRESOLVED_BLOCKER", findings=[low])
        report = RV.check_review_result_v2(
            names_none, scn.repo.root, evidence_commit=scn.evidence_commit, executor=EXECUTOR)
        self.assertIn("V3-REVIEW-UNRESOLVED-BLOCKER-NAMES-NONE", codes(report))
        # Negative control: the same verdict, one blocking finding, and this guard is silent.
        names_one = make_result(scn, review_round="VERIFY", verify_scope=scope,
                                verdict="UNRESOLVED_BLOCKER", findings=[stands])
        report = RV.check_review_result_v2(
            names_one, scn.repo.root, evidence_commit=scn.evidence_commit, executor=EXECUTOR)
        self.assertNotIn("V3-REVIEW-UNRESOLVED-BLOCKER-NAMES-NONE", codes(report))

    def test_incomplete_map_must_be_disclosed_and_disclosure_silences_it(self):
        silent = make_result(self.scn)
        silent["instruction_completeness"] = {
            "result": "INCOMPLETE",
            "instruction_ref": {"path": "docs/instruction.md", "revision": self.scn.repo.base},
            "unmapped_unit_ids": ["unit-preamble"],
            "detail": "the preamble carries an unmapped normative condition",
        }
        report = RV.check_review_result_v2(
            silent, self.scn.repo.root, evidence_commit=self.scn.evidence_commit,
            executor=EXECUTOR)
        self.assertIn("V3-REVIEW-INCOMPLETE-UNDISCLOSED", codes(report))
        disclosed = copy.deepcopy(silent)
        disclosed["residual_uncertainty"] = ["unit-preamble was found normative but unmapped"]
        disclosed["findings"] = [{"finding_id": "f-map", "blocking": False,
                                  "statement": "unit-preamble is normative but unmapped"}]
        report = RV.check_review_result_v2(
            disclosed, self.scn.repo.root, evidence_commit=self.scn.evidence_commit,
            executor=EXECUTOR)
        self.assertNotIn("V3-REVIEW-INCOMPLETE-UNDISCLOSED", codes(report))

    def test_verify_scope_and_reviewer_distinctness_guards(self):
        scn = self.scn
        narrow = make_result(scn, review_round="VERIFY", verify_scope={
            "accepted_finding_ids": ["f-one"], "repair_diff_reviewed": False,
            "permanent_boundaries_checked": True})
        report = RV.check_review_result_v2(
            narrow, scn.repo.root, evidence_commit=scn.evidence_commit, executor=EXECUTOR)
        self.assertIn("V3-REVIEW-VERIFY-SCOPE-INCOMPLETE", codes(report))
        for label, executor, code in (
            ("no executor supplied", None, "V3-REVIEW-REVIEWER-DISTINCTNESS-UNVERIFIED"),
            ("blank executor", "   ", "V3-REVIEW-REVIEWER-DISTINCTNESS-UNVERIFIED"),
            ("reviewer IS the executor", REVIEWER, "V3-REVIEW-REVIEWER-NOT-DISTINGUISHABLE"),
        ):
            with self.subTest(label=label):
                report = RV.check_review_result_v2(
                    make_result(scn), scn.repo.root, evidence_commit=scn.evidence_commit,
                    executor=executor)
                self.assertIn(code, codes(report))

    def test_clean_result_reports_nothing(self):
        report = RV.check_review_result_v2(
            make_result(self.scn), self.scn.repo.root,
            evidence_commit=self.scn.evidence_commit, executor=EXECUTOR)
        self.assertTrue(report.ok, "; ".join(report.rendered()))


class SubjectAgainstSeededPlanes(unittest.TestCase):
    """Each test commits a deliberately defective plane in its own repository."""

    def assert_scenario_reports(self, expected_code: str, **kwargs):
        scn = build_scenario(**kwargs)
        try:
            report = RS.check_subject(scn.subject, scn.repo.root)
            self.assertIn(expected_code, codes(report))
        finally:
            scn.repo.cleanup()

    def test_missing_per_check_result_file(self):
        # W2-A2: the expected set is derived from the committed plan's check_order. Also the
        # negative control for the CLOSED carve-out below: this scenario's default status is
        # EVIDENCED (a live run), and a live run still reports the same drop as MISSING.
        self.assert_scenario_reports(
            "V3-SUBJECT-CHECK-RESULT-MISSING",
            drop_files=(f"{CONTROL_ROOT}/evidence/check-chk-one.json",))

    def test_a_closed_control_plane_does_not_report_a_missing_check_result(self):
        """HD-12 (2026-08-08): a CheckResult does not survive its run — the CLOSED carve-out.

        Same dropped file as `test_missing_per_check_result_file` above; the only difference
        is the state's own status, and only the CLOSED plane is silent about the absence.
        """
        scn = build_scenario(
            state_mut=lambda state: state.update(status="CLOSED"),
            drop_files=(f"{CONTROL_ROOT}/evidence/check-chk-one.json",),
        )
        try:
            report = RS.check_subject(scn.subject, scn.repo.root)
            self.assertNotIn("V3-SUBJECT-CHECK-RESULT-MISSING", codes(report))
            self.assertTrue(report.ok, "; ".join(report.rendered()))
        finally:
            scn.repo.cleanup()

    def test_a_closed_control_plane_still_reports_an_invalid_present_check_result(self):
        """The carve-out is absence-only: a present-but-broken per-result file is reported
        on a CLOSED plane exactly as it would be on a live one."""
        scn = build_scenario(
            state_mut=lambda state: state.update(status="CLOSED"),
            file_overrides={f"{CONTROL_ROOT}/evidence/check-chk-one.json": "{not valid json"},
        )
        try:
            report = RS.check_subject(scn.subject, scn.repo.root)
            self.assertIn("V3-SUBJECT-CHECK-RESULT-INVALID", codes(report))
        finally:
            scn.repo.cleanup()

    def test_aggregate_only_storage_is_reported(self):
        # W2-A2's representable half: results written into ONE aggregate file. The
        # authored member LIST collapse of w1-r1 is unrepresentable — there is no list
        # object to author — which is a constructive property, untestable by design.
        self.assert_scenario_reports(
            "V3-SUBJECT-CHECK-RESULT-MISSING",
            plan_mut=lambda plan: plan.update(check_order=["chk-one", "chk-two"]),
            drop_files=(f"{CONTROL_ROOT}/evidence/check-chk-one.json",))

    def test_check_result_file_with_foreign_check_id(self):
        scn = build_scenario()
        try:
            wrong = json.loads(
                git(scn.repo.root, "show",
                    f"{scn.evidence_commit}:{CONTROL_ROOT}/evidence/check-chk-one.json"))
            wrong["check_id"] = "chk-two"
            scn.repo.write({f"{CONTROL_ROOT}/evidence/check-chk-one.json": json.dumps(wrong)})
            later = scn.repo.commit_all("swap check id")
            subject = dict(scn.subject, evidence_commit=later)
            self.assertIn("V3-SUBJECT-CHECK-RESULT-INVALID",
                          codes(RS.check_subject(subject, scn.repo.root)))
        finally:
            scn.repo.cleanup()

    def test_control_root_recorded_differently_is_reported(self):
        self.assert_scenario_reports(
            "V3-SUBJECT-CONTROL-ROOT-MISMATCH",
            record_mut=lambda record: record.update(control_root="runs/other-root"))

    def test_state_pointer_family(self):
        for code, kwargs in (
            ("V3-SUBJECT-POINTER-ABSENT",
             {"state_mut": lambda state: state.pop("fulfillment_ref")}),
            ("V3-SUBJECT-POINTER-MISSING",
             {"state_mut": lambda state: state.update(
                 coverage_ref={"path": f"{CONTROL_ROOT}/evidence/gone.json"})}),
            # `work_spec_ref`, not `coverage_ref`: since the digest narrowing only a
            # DIGEST_PROTECTED_FIELDS pointer is obliged to carry one, so a digest-less
            # `coverage_ref` is the normal shape and raises nothing. It is also the only
            # protected field this scenario's state carries.
            ("V3-SUBJECT-POINTER-UNVERIFIED",
             {"state_mut": lambda state: state["work_spec_ref"].pop("digest_sha256")}),
            ("V3-SUBJECT-POINTER-STALE",
             {"state_mut": lambda state: state["coverage_ref"].update(
                 digest_sha256=WRONG_DIGEST)}),
            ("V3-SUBJECT-STATE-INVALID",
             {"state_mut": lambda state: state.update(status="EVIDENCED-ISH")}),
        ):
            with self.subTest(code=code):
                self.assert_scenario_reports(code, **kwargs)

    def test_a_protected_pointer_with_a_wrong_digest_is_still_stale(self):
        """Narrowing removed digests from other fields; it must not blunt the ones kept.

        `work_spec_ref` is the protected field this scenario's state carries, so this is the
        must-fire half whose negative control is the digest-less *unprotected* pointer below.
        """
        self.assert_scenario_reports(
            "V3-SUBJECT-POINTER-STALE",
            state_mut=lambda state: state["work_spec_ref"].update(
                digest_sha256=WRONG_DIGEST))

    def test_an_unprotected_pointer_without_a_digest_is_reported_as_nothing_at_all(self):
        """The narrowing's whole point: outside DIGEST_PROTECTED_FIELDS a digest-less
        pointer is the normal shape, so it raises no issue — not a downgraded one.

        The assertion is the report as a whole rather than the absence of one code, because
        a gate that swapped UNVERIFIED for some other complaint would still pass an
        `assertNotIn`.
        """
        scn = build_scenario(state_mut=lambda state: state["coverage_ref"].pop("digest_sha256"))
        try:
            report = RS.check_subject(scn.subject, scn.repo.root)
            self.assertTrue(report.ok, "; ".join(report.rendered()))
        finally:
            scn.repo.cleanup()

    def test_document_and_binding_family(self):
        for code, kwargs in (
            ("V3-SUBJECT-DOCUMENT-INVALID",
             {"spec_mut": lambda spec: spec.pop("objective")}),
            ("V3-SUBJECT-SPEC-BINDING-MISMATCH",
             {"plan_mut": lambda plan: plan["work_spec_ref"].update(
                 digest_sha256=WRONG_DIGEST)}),
            ("V3-SUBJECT-INSTRUCTION-UNRESOLVED",
             {"spec_mut": lambda spec: spec["instruction_ref"].update(revision=FAKE_REV)}),
            ("V3-SUBJECT-INSTRUCTION-STALE",
             {"spec_mut": lambda spec: spec["instruction_ref"].update(
                 digest_sha256=WRONG_DIGEST)}),
            ("V3-SUBJECT-INPUT-UNRESOLVED",
             {"spec_mut": lambda spec: spec.update(
                 inputs=[{"path": "docs/missing.md", "revision": FAKE_REV}])}),
        ):
            with self.subTest(code=code):
                self.assert_scenario_reports(code, **kwargs)

    def test_input_with_a_stale_digest(self):
        # The input pins a REAL revision holding the file — so only the digest is wrong,
        # and the guard cannot pass merely because the path failed to resolve.
        scn = build_scenario(spec_mut=lambda spec: spec.update(
            inputs=[{"path": "docs/instruction.md",
                     "revision": spec["instruction_ref"]["revision"],
                     "digest_sha256": WRONG_DIGEST}]))
        try:
            self.assertIn("V3-SUBJECT-INPUT-STALE",
                          codes(RS.check_subject(scn.subject, scn.repo.root)))
        finally:
            scn.repo.cleanup()

    def test_evidence_commit_touching_outside_the_control_root(self):
        # W2-A10, seeded violation: the evidence commit also writes a payload path.
        self.assert_scenario_reports(
            "V3-SUBJECT-EVIDENCE-OUT-OF-ROOT",
            extra_files={"docs/notes.md": "smuggled into the evidence commit\n"})

    def test_a_parentless_evidence_commit_reports_containment_unverified(self):
        spec = {"work_id": "work-one", "objective": "root-commit containment probe",
                "instruction_ref": {"path": "docs/instruction.md", "revision": FAKE_REV},
                "instruction_units": [{"unit_id": "unit-one",
                                       "locator": {"path": "docs/instruction.md",
                                                   "anchor": "## Task"},
                                       "classification": "obligation",
                                       "obligation_ids": ["ob-one"]}],
                "change_boundary": {"write_scope": ["docs"], "out": ["runs"]},
                "expected_artifacts": [{"artifact_id": "art-guide", "path": "docs/guide.md"}],
                "obligations": [{"obligation_id": "ob-one",
                                 "instruction_unit_ids": ["unit-one"],
                                 "requirement": "the guide exists and is checked",
                                 "verification_mode": "review_only"}]}
        spec_text = json.dumps(spec, indent=1)
        state = {"work_id": "work-one", "run_id": "run-one", "status": "RESOLVED",
                 "repair_round": 0,
                 "work_spec_ref": {
                     "path": f"{CONTROL_ROOT}/control/work-spec.json",
                     "digest_sha256": bytes_digest(spec_text.encode("utf-8"))},
                 "resolved_plan_ref": {"path": f"{CONTROL_ROOT}/control/plan-none.json"}}
        with TempRepo({
            "docs/instruction.md": INSTRUCTION,
            f"{CONTROL_ROOT}/control/work-spec.json": spec_text,
            f"{CONTROL_ROOT}/control/state.json": json.dumps(state, indent=1),
        }) as repo:
            subject = RS.subject_of(
                evidence_commit=repo.base, candidate_ref={"branch": "cand",
                                                          "commit": OTHER_COMMIT},
                base_revision=FAKE_REV, control_root=CONTROL_ROOT, repair_round=0)
            self.assertIn("V3-SUBJECT-CONTAINMENT-UNVERIFIED",
                          codes(RS.check_subject(subject, repo.root)))


# ---------------------------------------------------------------------------
# W2-A7 — cold re-derivation from the SHA alone
# ---------------------------------------------------------------------------


class ColdRederivation(unittest.TestCase):
    def test_the_whole_subject_re_derives_with_no_worktree_state(self):
        scn = build_scenario()
        try:
            shutil.rmtree(scn.repo.root / "runs")
            self.assertFalse((scn.repo.root / CONTROL_ROOT).exists())
            plane = RS.read_control_plane(scn.repo.root, scn.evidence_commit, CONTROL_ROOT)
            self.assertTrue(plane.report.ok, "; ".join(plane.report.rendered()))
            self.assertEqual(plane.spec["work_id"], "work-one")
            self.assertEqual(plane.record["run_id"], "run-one")
            self.assertTrue(RS.check_subject(scn.subject, scn.repo.root).ok)
            report = RV.check_review_result_v2(
                make_result(scn), scn.repo.root, evidence_commit=scn.evidence_commit,
                executor=EXECUTOR)
            self.assertTrue(report.ok, "; ".join(report.rendered()))
        finally:
            scn.repo.cleanup()


# ---------------------------------------------------------------------------
# Invariant 11, successor form
# ---------------------------------------------------------------------------


class RepairRegenerationV2(unittest.TestCase):
    def test_wholesale_reuse_fires_every_guard(self):
        before = RS.EvidenceSetV2("a" * 64, "b" * 64, "c" * 64, "1" * 40, ("d" * 64,))
        report = RS.check_repair_regeneration_v2(before, before)
        for code in ("V3-SUBJECT-EVIDENCE-NOT-REGENERATED",
                     "V3-SUBJECT-EVIDENCE-COMMIT-REUSED", "V3-SUBJECT-CHECKS-NOT-RERUN"):
            self.assertIn(code, codes(report))

    def test_fully_regenerated_round_is_clean(self):
        before = RS.EvidenceSetV2("a" * 64, "b" * 64, "c" * 64, "1" * 40, ("d" * 64,))
        after = RS.EvidenceSetV2("e" * 64, "f" * 64, "0" * 64, "2" * 40, ("9" * 64,))
        self.assertTrue(RS.check_repair_regeneration_v2(before, after).ok)


# ---------------------------------------------------------------------------
# W2-A5 — the template's authoring gate
# ---------------------------------------------------------------------------


def _template_module():
    spec = importlib.util.spec_from_file_location(
        "w2_template_gate", TEMPLATE_DIR / "check_template_instance.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TemplateAuthoringGate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.gate = _template_module()
        cls.spec = {
            "schema_version": "2",
            "instruction_ref": {"path": "docs/instruction.md", "revision": FAKE_REV},
            "instruction_units": [
                {"unit_id": "unit-task",
                 "locator": {"path": "docs/instruction.md", "anchor": "## Task"},
                 "classification": "obligation", "obligation_ids": ["ob-one"]}],
        }

    def test_unmapped_preamble_fails_the_gate(self):
        issues = self.gate.preamble_issues(self.spec, INSTRUCTION)
        self.assertTrue(any("TEMPLATE-PREAMBLE-UNMAPPED" in issue for issue in issues))

    def test_mapping_the_preamble_passes(self):
        spec = copy.deepcopy(self.spec)
        spec["instruction_units"].append(
            {"unit_id": "unit-run-conditions",
             "locator": {"path": "docs/instruction.md", "anchor": "Run condition:"},
             "classification": "obligation", "obligation_ids": ["ob-one"]})
        self.assertEqual(self.gate.preamble_issues(spec, INSTRUCTION), [])

    def test_a_version_less_spec_fails_the_gate(self):
        """The v2-mandate leg moved to `spec_version_issues` (SIMP-B1) because it is the
        one requirement the enumerated form still owes; the assertion is unchanged."""
        spec = copy.deepcopy(self.spec)
        del spec["schema_version"]
        spec["instruction_units"].append(
            {"unit_id": "unit-run-conditions",
             "locator": {"path": "docs/instruction.md", "anchor": "Run condition:"},
             "classification": "obligation", "obligation_ids": ["ob-one"]})
        issues = self.gate.spec_version_issues(spec)
        self.assertTrue(any("TEMPLATE-SPEC-NOT-V2" in issue for issue in issues))
        self.assertEqual(self.gate.spec_version_issues(self.spec), [])

    def test_a_trivial_preamble_requires_no_mapping(self):
        trivial = "# Title\n\n## Task\n\nRun condition: buried in a section, not preamble.\n"
        self.assertEqual(self.gate.preamble_issues(self.spec, trivial), [])


# ---------------------------------------------------------------------------
# The module's issue-code surface is pinned and fully asserted in this file
# ---------------------------------------------------------------------------


class NamedIssueReachability(unittest.TestCase):
    #: Both modules of the wave-2 layer. Named explicitly so dropping one is a visible
    #: edit here rather than a silent narrowing of the sweep (the F4 defect class).
    MODULES = ("review_subject.py", "review_result_v2.py")

    def declared_codes(self) -> set[str]:
        package = RS_ROOT / "tooling" / "rsclib" / "document_harness"
        declared = set()
        for name in self.MODULES:
            source = (package / name).read_text(encoding="utf-8")
            for prefix, code in re.findall(
                    r'f"\{(CODE|RESULT_CODE)\}-([A-Z0-9-]+)"', source):
                declared.add(("V3-SUBJECT-" if prefix == "CODE" else "V3-REVIEW-") + code)
        return declared

    #: Codes raised from the `check_subject` identity table. They are listed here because
    #: they are the ones a suffix-only construction hid: built as `f"{CODE}-{code}"` from a
    #: loop variable, they were raised correctly and asserted by hand, but no sweep reading
    #: the source could see them, so nothing would have obliged a *future* row to be
    #: asserted at all (W2 review finding 1). Pinning them by name here fails if the
    #: construction ever reverts to the invisible form.
    IDENTITY_TABLE_CODES = (
        "V3-SUBJECT-WRONG-CANDIDATE",
        "V3-SUBJECT-CANDIDATE-BRANCH-MISMATCH",
        "V3-SUBJECT-BASE-MISMATCH",
        "V3-SUBJECT-CONTROL-ROOT-MISMATCH",
        "V3-SUBJECT-ROUND-MISMATCH",
    )

    def test_the_sweep_reaches_both_modules(self):
        """Guard against a sweep that silently covers one file — the vacuous-scan trap."""
        package = RS_ROOT / "tooling" / "rsclib" / "document_harness"
        for name in self.MODULES:
            with self.subTest(module=name):
                self.assertTrue((package / name).is_file())
                self.assertRegex((package / name).read_text(encoding="utf-8"),
                                 r'f"\{(?:CODE|RESULT_CODE)\}-[A-Z0-9-]+"')

    def test_the_sweep_reaches_the_identity_table_codes(self):
        """The codes a suffix-only construction made invisible must be swept, not just raised.

        Asserting them in the suite is not enough on its own: that establishes today's
        coverage, while this establishes that tomorrow's added row *must* be covered.
        """
        declared = self.declared_codes()
        missing = [code for code in self.IDENTITY_TABLE_CODES if code not in declared]
        self.assertEqual(missing, [],
                         "identity-table codes are raised but invisible to the sweep, so a "
                         "row added later would carry no assertion obligation")

    def test_every_declared_code_is_asserted_by_name_in_this_suite(self):
        declared = self.declared_codes()
        self.assertGreaterEqual(len(declared), 30)
        suite_source = pathlib.Path(__file__).read_text(encoding="utf-8")
        unasserted = sorted(code for code in declared if code not in suite_source)
        self.assertEqual(unasserted, [],
                         "codes declared by the wave-2 layer but never asserted here")


if __name__ == "__main__":
    unittest.main(verbosity=2)
