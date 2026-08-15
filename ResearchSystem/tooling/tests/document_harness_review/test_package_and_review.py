#!/usr/bin/env python3
"""First half of the V3-N2 acceptance matrix: the frozen subject and the bounded verdict.

Covers plan §9 acceptance IDs `N2-A1` (ReviewPackage membership), `N2-A2` (FULL rechecks
instruction completeness and covers every obligation) and `N2-A3` (closed verdict enums,
`residual_uncertainty` as data, no semantic-proof field anywhere in the review surface).

Every method asserts an exact issue **code** or an exact schema/enum **value**. A test that
passes because nothing was checked is worse than no test, so each "must fire" case is paired
with a negative control proving the same guard is silent when the property holds.

Three shapes are probed on purpose, because they are the ones this project has been bitten
by before:

* **fail-open guards** — an optional argument or optional field that silently disables an
  integrity check. `check_review_result(executor=None)` is claimed to report
  `V3-REVIEW-REVIEWER-DISTINCTNESS-UNVERIFIED` instead of staying silent; that claim is
  tested directly, and the same shape is then hunted elsewhere in the module.
* **green-light traps** — a negative that would still pass if the fix regressed. Every
  guard here is exercised from a *schema-valid* document, so nothing passes merely because
  the schema rejected the fixture first.
* **unreachable invariants** — V3-N1 shipped two named invariants permanently shadowed by a
  schema validation that ran first. `NamedIssueReachabilityTests` walks **every** named issue
  code in `review.py` and proves each one fires from a document the schema accepts.

Five methods here began as `@unittest.expectedFailure` defect records. Every one of those
defects was fixed inside V3-N2, so the markers are gone and the assertions — which were
always the correct ones — are now live regressions.

Offline and deterministic. Every Git identity comes from a disposable `TempRepo` under the
system temp directory; nothing here writes into the repository under assurance.
"""
from __future__ import annotations

import copy
import inspect
import io
import json
import re
import unittest

from _harness import TempRepo  # noqa: F401 — installs the tooling and V3-N1 import paths

from rsclib.document_harness import SCHEMA_DIR, Report, SpecGap, bytes_digest
from rsclib.document_harness.candidate import CandidateTreeReader, WorktreeReader
from rsclib.document_harness.review import (
    REQUIRED_ROLES,
    check_package,
    check_review_result,
    freeze_package,
    member,
    members_by_role,
    package_digest,
    validate_n2,
    verify_member_bytes,
)

#: A syntactically valid but meaningless Git revision, used where a fixture needs a
#: schema-valid `gitRev` that no test resolves against a real object.
FAKE_REV = "0" * 40
CANDIDATE_COMMIT = "1" * 40
OTHER_COMMIT = "9" * 40
DIGEST = "a" * 64
OTHER_DIGEST = "b" * 64

EXECUTOR = "executor agent"
REVIEWER = "independent reviewer"
CONTROLLER = "assurance controller"

#: The eight member roles, split by whether the schema requires the ref to pin a revision.
#: Read off the enum rather than restated, so a role added to the schema without a matching
#: `if/then` clause shows up here as an unclassified role rather than silently passing.
TREE_ROLES = ("raw_instruction", "source_input", "candidate_artifact")
CONTROL_ROLES = ("resolved_plan", "fulfillment", "manifest", "check_result", "coverage")


def review_schema() -> dict:
    with io.open(SCHEMA_DIR / "review.schema.json", encoding="utf-8") as handle:
        return json.load(handle)


def codes(report: Report) -> list[str]:
    return [issue.code for issue in report.issues]


# ---------------------------------------------------------------------------
# Minimal fixture builders. They build the *envelope* only — every defect a test
# demonstrates is written explicitly in that test's own body.
# ---------------------------------------------------------------------------


def make_members(*, drop: str | None = None, extra: list[dict] | None = None) -> list[dict]:
    """The six unconditional roles, one member each, optionally with one role dropped."""
    entries = [
        member("m-instruction", "raw_instruction", "docs/instruction.md", DIGEST, revision=FAKE_REV),
        member("m-plan", "resolved_plan", "control/plan.json", DIGEST),
        member("m-guide", "candidate_artifact", "docs/guide.md", DIGEST, revision=FAKE_REV),
        member("m-fulfillment", "fulfillment", "control/fulfillment.json", DIGEST),
        member("m-manifest", "manifest", "control/manifest.json", DIGEST),
        member("m-coverage", "coverage", "control/coverage.json", DIGEST),
    ]
    if drop:
        entries = [entry for entry in entries if entry["role"] != drop]
    return entries + list(extra or [])


def make_package(members: list[dict] | None = None, **overrides) -> dict:
    package = freeze_package(
        package_id="pkg-one",
        work_id="work-one",
        run_id="run-one",
        repair_round=0,
        review_round="FULL",
        candidate_ref={"branch": "cand", "commit": CANDIDATE_COMMIT},
        base_revision=FAKE_REV,
        frozen_by=CONTROLLER,
        members=make_members() if members is None else members,
    )
    package.update(overrides)
    return package


def make_spec(**overrides) -> dict:
    spec = {
        "work_id": "work-one",
        "objective": "produce the declared documents",
        "instruction_ref": {"path": "docs/instruction.md", "revision": FAKE_REV},
        "instruction_units": [
            {
                "unit_id": "unit-guide",
                "locator": {"path": "docs/instruction.md", "anchor": "## Guide"},
                "classification": "obligation",
                "obligation_ids": ["ob-guide"],
            }
        ],
        "change_boundary": {"write_scope": ["docs"], "out": ["docs/private"]},
        "expected_artifacts": [{"artifact_id": "artifact-guide", "path": "docs/guide.md"}],
        "obligations": [
            {
                "obligation_id": "ob-guide",
                "instruction_unit_ids": ["unit-guide"],
                "requirement": "the guide states the declared procedure",
                "verification_mode": "review_only",
            }
        ],
    }
    spec.update(overrides)
    return spec


def make_record(**overrides) -> dict:
    record = {
        "record_id": "record-one",
        "work_id": "work-one",
        "run_id": "run-one",
        "repair_round": 0,
        "candidate_ref": {"branch": "cand", "commit": CANDIDATE_COMMIT},
        "base_revision": FAKE_REV,
        "control_root": "control",
        "fulfillment": {
            "authored_by": EXECUTOR,
            "claims": [
                {
                    "obligation_id": "ob-guide",
                    "status": "IMPLEMENTED",
                    "implementation_locators": [{"path": "docs/guide.md", "anchor": "## Guide"}],
                }
            ],
        },
        "manifest": {
            "authored_by": "deterministic diff verifier",
            "boundary_result": "CONFORMANT",
            "expected_artifact_results": [{"artifact_id": "artifact-guide", "present": True}],
        },
    }
    record.update(overrides)
    return record


def make_result(package: dict, **overrides) -> dict:
    result = {
        "result_id": "result-one",
        "work_id": "work-one",
        "run_id": "run-one",
        "review_round": "FULL",
        "package_ref": {"path": "control/package.json", "digest_sha256": package_digest(package)},
        "candidate_ref": {"branch": "cand", "commit": CANDIDATE_COMMIT},
        "verdict": "REVIEWED_NO_BLOCKER",
        "instruction_completeness": {
            "result": "COMPLETE",
            "instruction_ref": {"path": "docs/instruction.md", "revision": FAKE_REV},
        },
        "per_obligation_disposition": [{"obligation_id": "ob-guide", "disposition": "SUPPORTED"}],
        "residual_uncertainty": [],
        "reviewed_by": REVIEWER,
    }
    result.update(overrides)
    return result


#: A schema-complete blocking finding. A blocker must name where it is, what it violates and
#: the smallest fix, so a fixture that omits any of the three is rejected before the guard
#: under test can run.
BLOCKING_FINDING = {
    "finding_id": "f-one",
    "blocking": True,
    "statement": "the guide contradicts the frozen instruction",
    "candidate_locator": {"path": "docs/guide.md", "anchor": "## Guide"},
    "ground_truth_locator": {"path": "docs/instruction.md", "anchor": "## Guide"},
    "minimum_fix": "restate the guide section so it matches the instruction",
}

VERIFY_SCOPE = {
    "accepted_finding_ids": ["f-one"],
    "repair_diff_reviewed": True,
    "permanent_boundaries_checked": True,
}

#: An instruction recheck that found the map incomplete, disclosed as the revise round requires.
#: `unmapped_unit_ids` carries the reviewer's OWN id for the omitted unit — a unit the map never
#: mapped has no WorkSpec id to borrow, which is exactly why it went missing.
INCOMPLETE_RECHECK = {
    "result": "INCOMPLETE",
    "instruction_ref": {"path": "docs/instruction.md", "revision": FAKE_REV},
    "unmapped_unit_ids": ["unit-appendix"],
    "detail": "unit-appendix is normative and was never mapped to an obligation",
}

#: The map-level finding an INCOMPLETE recheck must carry. `obligation_id` is deliberately
#: absent — a unit the map never mapped belongs to no obligation, which is the schema's own
#: reading of that field. Non-blocking, because the deficiency is in the WorkSpec's map rather
#: than in the candidate: inflating it to a blocker would demand a repair to the wrong object
#: and burn the single permitted round on it.
GAP_FINDING = {
    "finding_id": "f-gap",
    "blocking": False,
    "statement": (
        "unit-appendix is normative in the raw instruction and is mapped to no obligation, so "
        "no disposition in this result reaches it"
    ),
}

#: The residual that carries the same gap to the user at FINAL, where it is convertible to an
#: ACCEPT_WITH_LIMITATIONS limitation (V3-D6). The finding and the residual are not redundant:
#: one is addressed to the review record, the other to the deciding user.
GAP_RESIDUAL = (
    "unit-appendix was never mapped, so this verdict is relative to review dimensions that do "
    "not include it"
)


# ===========================================================================
# N2-A1 — the package is the actual work: exact logical membership, no byte copies
# ===========================================================================


class PackageMembershipTests(unittest.TestCase):
    """N2-A1: membership is exact, by reference, and requires actual subjects."""

    def test_n2_a1_baseline_package_is_schema_valid(self):
        """The negative control every membership test below is a mutation of."""
        self.assertEqual(codes(validate_n2("review_package", make_package())), [])

    def test_n2_a1_every_required_role_is_asserted_independently(self):
        """Cross-product: dropping any one of the six unconditional roles must fail.

        One clause per role rather than one combined assertion — a schema that only checked
        the first role would pass a single-role probe and fail the whole run in production.
        """
        for role in REQUIRED_ROLES:
            with self.subTest(dropped_role=role):
                package = make_package(make_members(drop=role))
                self.assertIn("V3-SCHEMA-REVIEW_PACKAGE", codes(validate_n2("review_package", package)))

    def test_n2_a1_executor_summary_never_rescues_a_missing_role(self):
        """The same cross-product with a summary attached: supplemental never substitutes.

        This is the assertion N2-A1 names — a package carrying a summary and no actual
        subjects is not a review subject at all.
        """
        for role in REQUIRED_ROLES:
            with self.subTest(dropped_role=role):
                package = make_package(
                    make_members(drop=role),
                    executor_summary_ref={"path": "control/executor-summary.md", "digest_sha256": DIGEST},
                )
                self.assertIn("V3-SCHEMA-REVIEW_PACKAGE", codes(validate_n2("review_package", package)))

    def test_n2_a1_summary_only_package_is_rejected(self):
        """A package whose only content is the executor's own summary is not a subject."""
        summary_only = make_package(
            [member("m-summary", "fulfillment", "control/executor-summary.md", DIGEST)],
            executor_summary_ref={"path": "control/executor-summary.md", "digest_sha256": DIGEST},
        )
        report = validate_n2("review_package", summary_only)
        self.assertIn("V3-SCHEMA-REVIEW_PACKAGE", codes(report))
        # One failure per absent required role, not merely "something failed": five of the
        # six unconditional roles are missing here, and `candidate_artifact` — the actual
        # subject a summary is standing in for — is one of them.
        self.assertEqual(len(report.issues), len(REQUIRED_ROLES) - 1)
        self.assertEqual({issue.where for issue in report.issues}, {"members"})

        # And the same members WITH a real candidate artifact still fail, because a summary
        # never covers the other four either — the roles are asserted independently.
        with_artifact = make_package(
            [
                member("m-summary", "fulfillment", "control/executor-summary.md", DIGEST),
                member("m-guide", "candidate_artifact", "docs/guide.md", DIGEST, revision=FAKE_REV),
            ],
            executor_summary_ref={"path": "control/executor-summary.md", "digest_sha256": DIGEST},
        )
        self.assertEqual(
            len(validate_n2("review_package", with_artifact).issues), len(REQUIRED_ROLES) - 2
        )

    def test_n2_a1_conditional_roles_may_be_absent(self):
        """Negative control: `source_input` and `check_result` are conditional, not required.

        Without this the six-role cross-product above would prove nothing — a schema that
        required all eight roles would also pass every drop test.
        """
        package = make_package()
        for role in ("source_input", "check_result"):
            with self.subTest(absent_role=role):
                self.assertEqual(members_by_role(package, role), [])
        self.assertEqual(codes(validate_n2("review_package", package)), [])

    def test_n2_a1_membership_binds_bytes_and_can_never_carry_them(self):
        """Byte-copying every source is not merely discouraged; it is unrepresentable."""
        with_member_content = make_members()
        with_member_content[2]["content"] = "the entire candidate artifact, inlined"
        self.assertIn(
            "V3-SCHEMA-REVIEW_PACKAGE",
            codes(validate_n2("review_package", make_package(with_member_content))),
        )

        with_ref_content = make_members()
        with_ref_content[2]["ref"]["content"] = "the entire candidate artifact, inlined"
        self.assertIn(
            "V3-SCHEMA-REVIEW_PACKAGE",
            codes(validate_n2("review_package", make_package(with_ref_content))),
        )

    def test_n2_a1_tree_roles_pin_a_revision_and_control_roles_need_none(self):
        """Cross-product over all eight roles: which tree the bytes came from is disclosed.

        A digest alone says "these bytes"; the revision says which tree they were taken
        from. Both halves are asserted, so a schema that dropped the `if/then` (making every
        role revision-free) fails the first half, and one that required a revision from every
        role fails the second.
        """
        for role in TREE_ROLES:
            with self.subTest(role=role, revision="omitted"):
                entries = make_members(
                    extra=[member("m-probe", role, "docs/probe.md", DIGEST)]
                )
                self.assertIn(
                    "V3-SCHEMA-REVIEW_PACKAGE",
                    codes(validate_n2("review_package", make_package(entries))),
                )
        for role in CONTROL_ROLES:
            with self.subTest(role=role, revision="omitted"):
                entries = make_members(
                    extra=[member("m-probe", role, "control/probe.json", DIGEST)]
                )
                self.assertEqual(
                    codes(validate_n2("review_package", make_package(entries))), []
                )

    def test_n2_a1_role_enum_is_closed_and_fully_classified(self):
        """The eight roles are exactly the enum, and every one is classified above.

        Guards the cross-product against drift: a ninth role added to the schema without a
        revision rule would otherwise be tested by nothing.
        """
        schema = review_schema()
        self.assertEqual(
            sorted(schema["$defs"]["memberRole"]["enum"]),
            sorted(TREE_ROLES + CONTROL_ROLES),
        )
        self.assertIn(
            "V3-SCHEMA-REVIEW_PACKAGE",
            codes(
                validate_n2(
                    "review_package",
                    make_package(make_members(extra=[member("m-x", "executor_summary", "x.md", DIGEST)])),
                )
            ),
        )

    def test_n2_a1_required_roles_constant_matches_the_schema_assertions(self):
        """`REQUIRED_ROLES` is documentation unless it equals what the schema asserts."""
        asserted = tuple(
            clause["properties"]["members"]["contains"]["properties"]["role"]["const"]
            for clause in review_schema()["allOf"]
        )
        self.assertEqual(asserted, tuple(REQUIRED_ROLES))


# ===========================================================================
# N2-A1 — completeness against the run, which only `check_package` can see
# ===========================================================================


class PackageCompletenessTests(unittest.TestCase):
    """N2-A1: schema-valid is not the same as complete against the run that produced it."""

    def test_n2_a1_complete_package_is_the_negative_control(self):
        """Every "must fire" case below is a single mutation away from this."""
        report = check_package(make_package(), make_spec(), make_record(), [])
        self.assertEqual(codes(report), [], report.rendered())

    def test_n2_a1_declared_source_input_omitted_is_named_exactly(self):
        spec = make_spec(inputs=[{"path": "docs/source.md", "revision": FAKE_REV}])
        report = check_package(make_package(), spec, make_record(), [])
        self.assertIn("V3-PACKAGE-INPUT-OMITTED", codes(report))
        self.assertTrue(
            any("docs/source.md" in issue.message for issue in report.issues), report.rendered()
        )

    def test_n2_a1_declared_source_input_present_is_not_flagged(self):
        """Negative control: the guard is per-path, not "any source_input will do"."""
        spec = make_spec(inputs=[{"path": "docs/source.md", "revision": FAKE_REV}])
        members = make_members(
            extra=[member("m-source", "source_input", "docs/source.md", DIGEST, revision=FAKE_REV)]
        )
        report = check_package(make_package(members), spec, make_record(), [])
        self.assertEqual(codes(report), [], report.rendered())

    def test_n2_a1_present_expected_artifact_omitted_is_named_exactly(self):
        """An artifact the candidate really contains must be an actual subject."""
        spec = make_spec(
            expected_artifacts=[
                {"artifact_id": "artifact-guide", "path": "docs/guide.md"},
                {"artifact_id": "artifact-appendix", "path": "docs/appendix.md"},
            ]
        )
        record = make_record(
            manifest={
                "authored_by": "deterministic diff verifier",
                "boundary_result": "CONFORMANT",
                "expected_artifact_results": [
                    {"artifact_id": "artifact-guide", "present": True},
                    {"artifact_id": "artifact-appendix", "present": True},
                ],
            }
        )
        report = check_package(make_package(), spec, record, [])
        self.assertIn("V3-PACKAGE-ARTIFACT-OMITTED", codes(report))
        self.assertTrue(
            any("artifact-appendix" in issue.message for issue in report.issues), report.rendered()
        )

    def test_n2_a1_absent_expected_artifact_is_not_demanded_as_a_member(self):
        """Negative control: an artifact the manifest reports missing cannot be a member."""
        spec = make_spec(
            expected_artifacts=[
                {"artifact_id": "artifact-guide", "path": "docs/guide.md"},
                {"artifact_id": "artifact-appendix", "path": "docs/appendix.md"},
            ]
        )
        record = make_record(
            manifest={
                "authored_by": "deterministic diff verifier",
                "boundary_result": "CONFORMANT",
                "expected_artifact_results": [
                    {"artifact_id": "artifact-guide", "present": True},
                    {"artifact_id": "artifact-appendix", "present": False},
                ],
            }
        )
        report = check_package(make_package(), spec, record, [])
        self.assertNotIn("V3-PACKAGE-ARTIFACT-OMITTED", codes(report))
        self.assertEqual(codes(report), [], report.rendered())

    def test_n2_a1_substituted_raw_instruction_is_named_exactly(self):
        """The reviewer must recheck against the instruction the WorkSpec actually froze."""
        members = make_members(drop="raw_instruction") + [
            member("m-instruction", "raw_instruction", "docs/paraphrase.md", DIGEST, revision=FAKE_REV)
        ]
        report = check_package(make_package(members), make_spec(), make_record(), [])
        self.assertIn("V3-PACKAGE-INSTRUCTION-SUBSTITUTED", codes(report))

    def test_n2_a1_check_results_wholly_omitted_is_named_exactly(self):
        report = check_package(
            make_package(), make_spec(), make_record(), [{"check_id": "chk-one"}]
        )
        self.assertIn("V3-PACKAGE-CHECKS-OMITTED", codes(report))

    def test_n2_a1_check_results_included_are_not_flagged(self):
        """Negative control for the guard above."""
        members = make_members(
            extra=[member("m-check-one", "check_result", "control/check-one.json", DIGEST)]
        )
        report = check_package(
            make_package(members), make_spec(), make_record(), [{"check_id": "chk-one"}]
        )
        self.assertEqual(codes(report), [], report.rendered())

    def test_n2_a1_run_identity_mismatches_are_each_named_exactly(self):
        """The package must be the subject of *this* run, at *this* round, on *this* candidate."""
        cases = {
            "V3-PACKAGE-WORK-MISMATCH": ("work_id", "work-other"),
            "V3-PACKAGE-RUN-MISMATCH": ("run_id", "run-other"),
            "V3-PACKAGE-ROUND-MISMATCH": ("repair_round", 1),
            "V3-PACKAGE-WRONG-CANDIDATE": ("candidate_ref", {"branch": "cand", "commit": OTHER_COMMIT}),
        }
        for code, (field, value) in cases.items():
            with self.subTest(code=code):
                package = make_package()
                package[field] = value
                report = check_package(package, make_spec(), make_record(), [])
                self.assertIn(code, codes(report), report.rendered())


# ===========================================================================
# N2-A1 / V3-D5 — the binding becomes evidence only when the bytes are recomputed
# ===========================================================================


class MemberByteBindingTests(unittest.TestCase):
    """`verify_member_bytes` against real trees: a digest that is never recomputed is a claim."""

    def package_for(self, members: list[dict]) -> dict:
        return make_package(members)

    def test_n2_a1_control_member_matching_its_bytes_is_the_negative_control(self):
        with TempRepo({"docs/instruction.md": "instruction\n"}) as repo:
            repo.write({"control/coverage.json": '{"coverage":1}'})
            digest = bytes_digest((repo.root / "control" / "coverage.json").read_bytes())
            package = self.package_for(
                [member("m-coverage", "coverage", "control/coverage.json", digest)]
            )
            report = verify_member_bytes(package, repo.root)
            self.assertEqual(codes(report), [], report.rendered())

    def test_n2_a1_member_whose_bytes_moved_is_named_exactly(self):
        with TempRepo({"docs/instruction.md": "instruction\n"}) as repo:
            repo.write({"control/coverage.json": '{"coverage":1}'})
            digest = bytes_digest((repo.root / "control" / "coverage.json").read_bytes())
            package = self.package_for(
                [member("m-coverage", "coverage", "control/coverage.json", digest)]
            )
            repo.write({"control/coverage.json": '{"coverage":2}'})
            report = verify_member_bytes(package, repo.root)
            self.assertIn("V3-PACKAGE-MEMBER-STALE", codes(report))
            self.assertEqual([issue.where for issue in report.issues], ["m-coverage"])

    def test_n2_a1_member_that_does_not_resolve_is_named_exactly(self):
        with TempRepo({"docs/instruction.md": "instruction\n"}) as repo:
            package = self.package_for(
                [member("m-coverage", "coverage", "control/absent.json", DIGEST)]
            )
            report = verify_member_bytes(package, repo.root)
            self.assertIn("V3-PACKAGE-MEMBER-MISSING", codes(report))

    def test_n2_a1_a_revision_member_needs_no_reader_and_verifies_against_its_own_tree(self):
        """The reader argument is gone: each member is read from the revision it pins.

        It previously took a `reader` whose omission downgraded the check to
        `V3-PACKAGE-MEMBER-UNVERIFIED` — a fail-open parameter. Reading each member through
        its own pinned revision removes both the parameter and the wrong-tree defect below,
        so there is no longer an unverified state to report here.
        """
        with TempRepo({"docs/instruction.md": "instruction\n"}) as repo:
            candidate = repo.commit_candidate({"docs/guide.md": "## Guide\n"})
            digest = bytes_digest(CandidateTreeReader(repo.root, candidate).read("docs/guide.md"))
            package = self.package_for(
                [member("m-guide", "candidate_artifact", "docs/guide.md", digest, revision=candidate)]
            )
            self.assertEqual(codes(verify_member_bytes(package, repo.root)), [])

            # Negative control: the same member with a wrong digest must still be caught, so
            # the clean result above is a verification and not a skipped check.
            wrong = self.package_for(
                [member("m-guide", "candidate_artifact", "docs/guide.md", OTHER_DIGEST, revision=candidate)]
            )
            self.assertEqual(codes(verify_member_bytes(wrong, repo.root)), ["V3-PACKAGE-MEMBER-STALE"])

    def test_n2_a1_member_digest_is_checked_against_the_revision_it_pins(self):
        """`ref.revision` is honoured — the member is read from the tree it names.

        The member below pins the *base* revision and carries the digest of the *candidate's*
        bytes, so its digest does not match the bytes at the tree it names. That is precisely
        the binding a digest exists to make falsifiable, and it is reported clean, because
        `verify_member_bytes` reads every revision-bearing member through the single supplied
        reader and never compares `ref["revision"]` with `reader.revision`.

        The assertion here is the correct one. Do not invert it; delete the marker when the
        implementation honours the pinned revision.
        """
        with TempRepo({"docs/instruction.md": "INSTRUCTION VERSION A\n"}) as repo:
            base = repo.base
            candidate = repo.commit_candidate({"docs/instruction.md": "INSTRUCTION VERSION B\n"})
            reader = CandidateTreeReader(repo.root, candidate)
            candidate_digest = bytes_digest(reader.read("docs/instruction.md"))

            package = self.package_for(
                [
                    member(
                        "m-instruction",
                        "raw_instruction",
                        "docs/instruction.md",
                        candidate_digest,  # the bytes at `candidate`, not at `base`
                        revision=base,
                    )
                ]
            )
            report = verify_member_bytes(package, repo.root)
            self.assertIn("V3-PACKAGE-MEMBER-STALE", codes(report), report.rendered())

    def test_n2_a1_uncommitted_bytes_can_never_certify_a_pinned_revision(self):
        """FIXED during this node (was a real defect): a worktree reader is accepted for a pinned member.

        N1's R1 taught this exact lesson and `check_locators` refuses any reader whose kind is
        not `candidate_commit`. `verify_member_bytes` once took a reader and had no such
        guard, so bytes existing in no committed tree at all could verify a member pinning
        an exact revision. It now reads each member from its own pinned revision, so an
        uncommitted edit is invisible to it and the member is reported stale.
        """
        with TempRepo({"docs/instruction.md": "INSTRUCTION VERSION A\n"}) as repo:
            candidate = repo.commit_candidate({"docs/instruction.md": "INSTRUCTION VERSION B\n"})
            repo.write({"docs/instruction.md": "UNCOMMITTED EDIT\n"})  # never committed anywhere
            worktree_digest = bytes_digest((repo.root / "docs" / "instruction.md").read_bytes())

            package = self.package_for(
                [
                    member(
                        "m-instruction",
                        "raw_instruction",
                        "docs/instruction.md",
                        worktree_digest,
                        revision=candidate,
                    )
                ]
            )
            report = verify_member_bytes(package, repo.root)
            self.assertIn("V3-PACKAGE-MEMBER-STALE", codes(report), report.rendered())


# ===========================================================================
# N2-A2 — FULL rechecks instruction completeness and covers every obligation
# ===========================================================================


class ReviewResultCompletenessTests(unittest.TestCase):
    """N2-A2: invariants 2 and 10, from documents the schema already accepted."""

    def test_n2_a2_complete_result_is_the_negative_control(self):
        package = make_package()
        report = check_review_result(make_result(package), make_spec(), package, executor=EXECUTOR)
        self.assertEqual(codes(report), [], report.rendered())

    def test_n2_a2_obligation_coverage_is_exactly_once(self):
        """Cross-product over the three ways coverage can fail: missing, extra, repeated."""
        package = make_package()
        spec = make_spec(
            obligations=[
                {
                    "obligation_id": name,
                    "instruction_unit_ids": ["unit-guide"],
                    "requirement": f"the work satisfies {name}",
                    "verification_mode": "review_only",
                }
                for name in ("ob-guide", "ob-appendix")
            ]
        )
        cases = {
            "V3-REVIEW-OBLIGATION-UNDISPOSED": [
                {"obligation_id": "ob-guide", "disposition": "SUPPORTED"}
            ],
            "V3-REVIEW-UNDECLARED-DISPOSITION": [
                {"obligation_id": "ob-guide", "disposition": "SUPPORTED"},
                {"obligation_id": "ob-appendix", "disposition": "SUPPORTED"},
                {"obligation_id": "ob-ghost", "disposition": "SUPPORTED"},
            ],
            "V3-REVIEW-DUPLICATE-DISPOSITION": [
                {"obligation_id": "ob-guide", "disposition": "SUPPORTED"},
                {"obligation_id": "ob-guide", "disposition": "SUPPORTED", "note": "reviewed twice"},
                {"obligation_id": "ob-appendix", "disposition": "SUPPORTED"},
            ],
        }
        for code, dispositions in cases.items():
            with self.subTest(code=code):
                result = make_result(package, per_obligation_disposition=dispositions)
                self.assertEqual(codes(validate_n2("review_result", result)), [])
                report = check_review_result(result, spec, package, executor=EXECUTOR)
                self.assertIn(code, codes(report), report.rendered())

        exactly_once = make_result(
            package,
            per_obligation_disposition=[
                {"obligation_id": "ob-guide", "disposition": "SUPPORTED"},
                {"obligation_id": "ob-appendix", "disposition": "SUPPORTED"},
            ],
        )
        report = check_review_result(exactly_once, spec, package, executor=EXECUTOR)
        self.assertEqual(codes(report), [], report.rendered())

    def test_n2_a2_unverifiable_is_a_reported_state_not_a_failure(self):
        """Negative control with teeth: UNVERIFIABLE is disposed, never folded into SUPPORTED."""
        package = make_package()
        result = make_result(
            package,
            per_obligation_disposition=[
                {
                    "obligation_id": "ob-guide",
                    "disposition": "UNVERIFIABLE",
                    "note": "the frozen subjects do not reach this claim either way",
                }
            ],
        )
        report = check_review_result(result, make_spec(), package, executor=EXECUTOR)
        self.assertEqual(codes(report), [], report.rendered())
        self.assertIn(
            "UNVERIFIABLE",
            review_schema()["$defs"]["perObligationDisposition"]["properties"]["disposition"]["enum"],
        )

    def test_n2_a2_recheck_must_read_the_instruction_the_workspec_froze(self):
        """Invariant 10 is about the raw instruction, not a derived map or a later revision."""
        package = make_package()
        for field, value in (("path", "docs/paraphrase.md"), ("revision", "c" * 40)):
            with self.subTest(field=field):
                result = make_result(package)
                result["instruction_completeness"]["instruction_ref"][field] = value
                self.assertEqual(codes(validate_n2("review_result", result)), [])
                report = check_review_result(result, make_spec(), package, executor=EXECUTOR)
                self.assertIn("V3-REVIEW-INSTRUCTION-MISMATCH", codes(report), report.rendered())

    def test_v3_revise_an_incomplete_map_is_disclosed_rather_than_refused(self):
        """The combination V3-N2 refused outright is legal — *with* disclosure.

        `V3-REVIEW-INCOMPLETE-CONTRADICTS-VERDICT` asserted that an unmapped normative unit *is*
        a blocking discrepancy. Contract §5 does not say that: it defines `REVIEWED_NO_BLOCKER`
        as scope-relative — "no blocking discrepancy found **within the frozen subjects and
        review dimensions**" — so an incomplete map means the dimensions were narrower and the
        verdict stays true as defined. Refusing it while naming no replacement was a deadlock,
        and both real shadow runs walked into it.
        """
        package = make_package()
        result = make_result(
            package,
            instruction_completeness=INCOMPLETE_RECHECK,
            findings=[GAP_FINDING],
            residual_uncertainty=[GAP_RESIDUAL],
        )
        self.assertEqual(codes(validate_n2("review_result", result)), [])
        report = check_review_result(result, make_spec(), package, executor=EXECUTOR)
        self.assertEqual(codes(report), [], report.rendered())

    def test_v3_revise_an_incomplete_map_without_disclosure_is_refused(self):
        """Silence is what stops being an option. Each half alone is insufficient.

        The cross-product matters: requiring only *a* finding would be satisfied by any unrelated
        finding, and requiring only the finding would leave the gap out of `residual_uncertainty`
        — the one field that reaches the user at FINAL.
        """
        package = make_package()
        for name, over in (
            ("neither", {}),
            ("finding only", {"findings": [GAP_FINDING]}),
            ("residual only", {"residual_uncertainty": [GAP_RESIDUAL]}),
        ):
            with self.subTest(disclosure=name):
                result = make_result(
                    package, instruction_completeness=INCOMPLETE_RECHECK, **over
                )
                self.assertEqual(codes(validate_n2("review_result", result)), [])
                report = check_review_result(result, make_spec(), package, executor=EXECUTOR)
                self.assertIn("V3-REVIEW-INCOMPLETE-UNDISCLOSED", codes(report), report.rendered())

    def test_v3_revise_the_disclosure_must_name_the_unmapped_unit(self):
        """A finding and a residual that never name the gap disclose nothing about it.

        This is the guard's whole content: without the name test, a result carrying any finding
        and any residual would pass while the omission stayed invisible.
        """
        package = make_package()
        result = make_result(
            package,
            instruction_completeness=INCOMPLETE_RECHECK,
            findings=[dict(GAP_FINDING, statement="the guide's tone is inconsistent")],
            residual_uncertainty=["I sampled the appendix rather than reading it in full"],
        )
        self.assertEqual(codes(validate_n2("review_result", result)), [])
        report = check_review_result(result, make_spec(), package, executor=EXECUTOR)
        self.assertIn("V3-REVIEW-INCOMPLETE-UNDISCLOSED", codes(report), report.rendered())

    def test_v3_revise_incomplete_must_enumerate_the_units_not_only_describe_them(self):
        """`detail` alone no longer satisfies the schema: prose cannot be joined to anything."""
        prose_only = dict(INCOMPLETE_RECHECK)
        prose_only.pop("unmapped_unit_ids")
        result = make_result(
            make_package(),
            instruction_completeness=prose_only,
            findings=[GAP_FINDING],
            residual_uncertainty=[GAP_RESIDUAL],
        )
        self.assertIn("V3-SCHEMA-REVIEW_RESULT", codes(validate_n2("review_result", result)))

    def test_v3_revise_spec_gap_remains_the_stop_route_for_an_incomplete_map(self):
        """Disclosing is now legal, which must not make stopping unavailable.

        V3-D7 routes an incomplete map to a new WorkSpec revision and a new user START, and
        `REVIEW.md` states the criterion for choosing that over disclose-and-continue. The two
        real cases split on exactly it, so both routes have to stay reachable.
        """
        package = make_package()
        result = make_result(
            package,
            verdict="SPEC_GAP",
            instruction_completeness=INCOMPLETE_RECHECK,
            findings=[GAP_FINDING],
            residual_uncertainty=[GAP_RESIDUAL],
        )
        self.assertEqual(codes(validate_n2("review_result", result)), [])
        report = check_review_result(result, make_spec(), package, executor=EXECUTOR)
        self.assertEqual(codes(report), [], report.rendered())

    def test_v3_revise_disclosure_is_required_on_every_verdict_not_only_no_blocker(self):
        """Run-p3 returned CHANGES_REQUIRED and had *also* dropped a normative unit.

        Gating the requirement on `REVIEWED_NO_BLOCKER` — the shape the old guard keyed on —
        would have let that silence through, which is why the disclosure rule is unconditional.
        """
        package = make_package()
        result = make_result(
            package,
            verdict="CHANGES_REQUIRED",
            findings=[BLOCKING_FINDING],
            instruction_completeness=INCOMPLETE_RECHECK,
        )
        self.assertEqual(codes(validate_n2("review_result", result)), [])
        report = check_review_result(result, make_spec(), package, executor=EXECUTOR)
        self.assertIn("V3-REVIEW-INCOMPLETE-UNDISCLOSED", codes(report), report.rendered())

        # Negative control: the same verdict, the same gap, now disclosed.
        disclosed = copy.deepcopy(result)
        disclosed["findings"] = [BLOCKING_FINDING, GAP_FINDING]
        disclosed["residual_uncertainty"] = [GAP_RESIDUAL]
        report = check_review_result(disclosed, make_spec(), package, executor=EXECUTOR)
        self.assertEqual(codes(report), [], report.rendered())

    def test_n2_a2_a_blocking_finding_cannot_coexist_with_no_blocker_found(self):
        package = make_package()
        result = make_result(package, findings=[BLOCKING_FINDING])
        self.assertEqual(codes(validate_n2("review_result", result)), [])
        report = check_review_result(result, make_spec(), package, executor=EXECUTOR)
        self.assertIn("V3-REVIEW-BLOCKER-CONTRADICTS-VERDICT", codes(report))

        # Negative control: a non-blocking finding is a finding, not an inflated blocker.
        non_blocking = make_result(
            package,
            findings=[
                {
                    "finding_id": "f-two",
                    "blocking": False,
                    "statement": "the appendix heading style drifts from the rest of the document",
                }
            ],
        )
        report = check_review_result(non_blocking, make_spec(), package, executor=EXECUTOR)
        self.assertEqual(codes(report), [], report.rendered())

    def test_n2_a2_findings_cited_by_a_disposition_must_exist(self):
        package = make_package()
        dangling = make_result(
            package,
            per_obligation_disposition=[
                {"obligation_id": "ob-guide", "disposition": "SUPPORTED", "finding_ids": ["f-ghost"]}
            ],
        )
        report = check_review_result(dangling, make_spec(), package, executor=EXECUTOR)
        self.assertIn("V3-REVIEW-DANGLING-FINDING-REF", codes(report))

        unsupported = make_result(
            package,
            verdict="CHANGES_REQUIRED",
            findings=[BLOCKING_FINDING],
            per_obligation_disposition=[
                {
                    "obligation_id": "ob-guide",
                    "disposition": "NOT_SUPPORTED",
                    "note": "the frozen subjects contradict the fulfillment claim",
                }
            ],
        )
        report = check_review_result(unsupported, make_spec(), package, executor=EXECUTOR)
        self.assertIn("V3-REVIEW-UNSUPPORTED-WITHOUT-FINDING", codes(report))

        # Negative control: the same disposition citing a real finding is clean.
        cited = copy.deepcopy(unsupported)
        cited["per_obligation_disposition"][0]["finding_ids"] = ["f-one"]
        report = check_review_result(cited, make_spec(), package, executor=EXECUTOR)
        self.assertEqual(codes(report), [], report.rendered())

    def test_n2_a2_a_verdict_binds_the_exact_package_it_answers_for(self):
        package = make_package()
        rebound = make_result(package)
        rebound["package_ref"]["digest_sha256"] = OTHER_DIGEST
        report = check_review_result(rebound, make_spec(), package, executor=EXECUTOR)
        self.assertIn("V3-REVIEW-PACKAGE-BINDING-MISMATCH", codes(report))

        # A package edited after the result was produced breaks the same binding — the
        # digest is over the package's own bytes, so this is not a tautology.
        drifted = make_package()
        drifted["frozen_by"] = "a different controller"
        report = check_review_result(make_result(package), make_spec(), drifted, executor=EXECUTOR)
        self.assertIn("V3-REVIEW-PACKAGE-BINDING-MISMATCH", codes(report))

    def test_n2_a2_verify_scope_must_cover_the_diff_and_the_permanent_boundaries(self):
        package = make_package(review_round="VERIFY")
        for missing in ("repair_diff_reviewed", "permanent_boundaries_checked"):
            with self.subTest(unchecked=missing):
                scope = dict(VERIFY_SCOPE, **{missing: False})
                result = make_result(package, review_round="VERIFY", verify_scope=scope)
                result["package_ref"]["digest_sha256"] = package_digest(package)
                self.assertEqual(codes(validate_n2("review_result", result)), [])
                report = check_review_result(result, make_spec(), package, executor=EXECUTOR)
                self.assertIn("V3-REVIEW-VERIFY-SCOPE-INCOMPLETE", codes(report), report.rendered())

        complete = make_result(package, review_round="VERIFY", verify_scope=dict(VERIFY_SCOPE))
        complete["package_ref"]["digest_sha256"] = package_digest(package)
        report = check_review_result(complete, make_spec(), package, executor=EXECUTOR)
        self.assertEqual(codes(report), [], report.rendered())


# ===========================================================================
# N2-A3 — closed verdicts, residual uncertainty as data, no semantic-proof field
# ===========================================================================


class ClosedVerdictSurfaceTests(unittest.TestCase):
    """N2-A3: the review surface can express a bounded finding and nothing stronger."""

    def test_n2_a3_control_verdicts_are_exactly_the_contract_set(self):
        schema = review_schema()
        self.assertEqual(
            schema["$defs"]["reviewResult"]["properties"]["verdict"]["enum"],
            ["REVIEWED_NO_BLOCKER", "CHANGES_REQUIRED", "SPEC_GAP"],
        )
        self.assertEqual(schema["$defs"]["reviewRound"]["enum"], ["FULL", "VERIFY"])
        self.assertEqual(
            schema["$defs"]["instructionCompleteness"]["properties"]["result"]["enum"],
            ["COMPLETE", "INCOMPLETE"],
        )
        self.assertEqual(
            schema["$defs"]["perObligationDisposition"]["properties"]["disposition"]["enum"],
            ["SUPPORTED", "NOT_SUPPORTED", "UNVERIFIABLE"],
        )

    def test_n2_a3_a_verify_cannot_request_a_second_repair(self):
        package = make_package(review_round="VERIFY")
        result = make_result(
            package,
            review_round="VERIFY",
            verdict="CHANGES_REQUIRED",
            findings=[BLOCKING_FINDING],
            verify_scope=dict(VERIFY_SCOPE),
        )
        self.assertIn("V3-SCHEMA-REVIEW_RESULT", codes(validate_n2("review_result", result)))

        # Negative control: the same verdict on the FULL round is legal — the narrowing is
        # per round, not a blanket ban.
        full = make_result(make_package(), verdict="CHANGES_REQUIRED", findings=[BLOCKING_FINDING])
        self.assertEqual(codes(validate_n2("review_result", full)), [])

    def test_n2_a3_no_fourth_control_verdict_can_be_smuggled_in(self):
        """Uncertainty and user decisions are not verdicts, and cannot be written as one."""
        for smuggled in ("ACCEPT_WITH_LIMITATIONS", "RESIDUAL_UNCERTAINTY", "REVIEWED_PROVEN"):
            with self.subTest(verdict=smuggled):
                result = make_result(make_package(), verdict=smuggled)
                self.assertIn("V3-SCHEMA-REVIEW_RESULT", codes(validate_n2("review_result", result)))

    def test_n2_a3_residual_uncertainty_is_required_data_and_may_be_empty(self):
        package = make_package()
        absent = make_result(package)
        del absent["residual_uncertainty"]
        self.assertIn("V3-SCHEMA-REVIEW_RESULT", codes(validate_n2("review_result", absent)))

        empty = make_result(package, residual_uncertainty=[])
        self.assertEqual(codes(validate_n2("review_result", empty)), [])

        stated = make_result(
            package,
            residual_uncertainty=["the source could not be reached during the review window"],
        )
        self.assertEqual(codes(validate_n2("review_result", stated)), [])
        report = check_review_result(stated, make_spec(), package, executor=EXECUTOR)
        self.assertEqual(codes(report), [], report.rendered())

    def test_n2_a3_residual_uncertainty_cannot_carry_a_verdict_shaped_value(self):
        for value in ([{"verdict": "UNCERTAIN"}], ["no"], [True]):
            with self.subTest(value=value):
                result = make_result(make_package(), residual_uncertainty=value)
                self.assertIn("V3-SCHEMA-REVIEW_RESULT", codes(validate_n2("review_result", result)))

    def test_n2_a3_no_semantic_proof_field_exists_in_the_review_surface(self):
        """Recursive scan of every property name, required name and enum value.

        Descriptions are deliberately not scanned: the module docstring's "not an OS
        guarantee" is a *denial* of a proof claim, and a scan that flagged it would push the
        next author to delete the disclosure rather than the field.
        """
        forbidden = (
            "proof",
            "proved",
            "proven",
            "guarantee",
            "certified",
            "correctness",
            "exhaustive",
            "mathematic",
            "verified_complete",
        )
        names: set[str] = set()
        values: set[str] = set()

        def walk(node: object) -> None:
            if isinstance(node, dict):
                for key, value in node.items():
                    if key == "properties" and isinstance(value, dict):
                        names.update(value.keys())
                    if key == "required" and isinstance(value, list):
                        names.update(str(item) for item in value)
                    if key == "enum" and isinstance(value, list):
                        values.update(str(item) for item in value)
                    if key == "const":
                        values.add(str(value))
                    walk(value)
            elif isinstance(node, list):
                for item in node:
                    walk(item)

        walk(review_schema())
        self.assertIn("residual_uncertainty", names)  # the scan really did reach the leaves
        self.assertIn("REVIEWED_NO_BLOCKER", values)
        for token in forbidden:
            for name in sorted(names):
                self.assertNotIn(token, name.casefold(), f"proof vocabulary in property {name}")
            for value in sorted(values):
                self.assertNotIn(token, value.casefold(), f"proof vocabulary in enum value {value}")

    def test_n2_a3_an_unknown_review_field_is_rejected_rather_than_ignored(self):
        """`additionalProperties: false` is what keeps the scan above meaningful at runtime."""
        result = make_result(make_package(), semantic_proof={"proved": True})
        self.assertIn("V3-SCHEMA-REVIEW_RESULT", codes(validate_n2("review_result", result)))

        package = make_package()
        package["proof_of_completeness"] = True
        self.assertIn("V3-SCHEMA-REVIEW_PACKAGE", codes(validate_n2("review_package", package)))

    def test_n2_a3_the_validated_kinds_are_closed_and_fail_shut(self):
        with self.assertRaises(SpecGap):
            validate_n2("review_proof", {})
        with self.assertRaises(SpecGap):
            validate_n2("candidate", make_record())  # a real N1 kind, not registered here


# ===========================================================================
# Fail-open probes — an argument or value that silently switches a guard off
# ===========================================================================


class FailOpenGuardTests(unittest.TestCase):
    """The shape this project has been bitten by: a check that did not run, reported green."""

    def test_reviewer_distinctness_without_an_executor_is_reported_not_skipped(self):
        package = make_package()
        result = make_result(package)

        omitted = check_review_result(result, make_spec(), package)
        self.assertEqual(codes(omitted), ["V3-REVIEW-REVIEWER-DISTINCTNESS-UNVERIFIED"])

        # Negative control: supplied and distinct, the guard is silent — so the code above
        # marks an unrun check rather than firing unconditionally.
        distinct = check_review_result(result, make_spec(), package, executor=EXECUTOR)
        self.assertEqual(codes(distinct), [], distinct.rendered())

    def test_check_completeness_cannot_be_switched_off_by_omitting_an_argument(self):
        """`results` carries no default, so a caller cannot silently skip the guard.

        This pins a fix rather than a defect: the parameter began as `results = ()`, and with
        that default `check_package(package, spec, record)` reported a package missing every
        CheckResult as clean. An empty sequence is legitimately meaningful here — a run whose
        obligations are all `review_only` produces none — so "none exist" cannot be
        distinguished from "the caller did not say" after the call, which is why the ambiguity
        has to be removed at the signature. A regression to a default would reopen it.
        """
        parameter = inspect.signature(check_package).parameters["results"]
        self.assertIs(parameter.default, inspect.Parameter.empty)
        with self.assertRaises(TypeError):
            check_package(make_package(), make_spec(), make_record())  # type: ignore[call-arg]

        # And an explicit empty sequence still means "this run produced no checks", which is
        # not a defect and must stay silent.
        report = check_package(make_package(), make_spec(), make_record(), [])
        self.assertEqual(codes(report), [], report.rendered())

    def test_reviewer_that_is_the_executor_is_named_exactly(self):
        package = make_package()
        for spelling in (REVIEWER, REVIEWER.upper(), f"  {REVIEWER}  "):
            with self.subTest(executor=spelling):
                report = check_review_result(
                    make_result(package), make_spec(), package, executor=spelling
                )
                self.assertIn("V3-REVIEW-REVIEWER-NOT-DISTINGUISHABLE", codes(report))

    def test_a_blank_executor_identity_is_not_a_supplied_one(self):
        """FIXED during this node (was a real defect): `executor=""` silently disables the distinctness guard.

        The guard tests `executor is None`, so an empty or whitespace-only identity — what a
        caller gets from a missing config field or an unset environment variable — takes the
        `elif` branch, compares unequal against any `reviewed_by` (minimum length 2), and
        reports nothing at all. That is the same "omitting an argument silently disabled it"
        failure the module docstring says this shape exists to prevent.

        `V3-REVIEW-REVIEWER-DISTINCTNESS-UNVERIFIED` is the correct code: no usable executor
        identity was supplied, so distinctness was not checked.
        """
        package = make_package()
        for blank in ("", "   "):
            with self.subTest(executor=repr(blank)):
                report = check_review_result(
                    make_result(package), make_spec(), package, executor=blank
                )
                self.assertIn(
                    "V3-REVIEW-REVIEWER-DISTINCTNESS-UNVERIFIED", codes(report), report.rendered()
                )

    def test_partial_check_result_omission_is_detected(self):
        """FIXED during this node (was a real defect): only *total* omission of CheckResults fires.

        `check_package`'s own docstring names this case — "a package that satisfies the schema
        while omitting half the check results is a subject the reviewer cannot judge the
        candidate from" — but the implementation only tests whether the set of
        `check_result` members is empty. Three results and one member is reported clean,
        while the sibling guard for declared source inputs is exact per path.

        The assertion here is the correct one.
        """
        members = make_members(
            extra=[member("m-check-one", "check_result", "control/check-one.json", DIGEST)]
        )
        report = check_package(
            make_package(members),
            make_spec(),
            make_record(),
            [{"check_id": "chk-one"}, {"check_id": "chk-two"}, {"check_id": "chk-three"}],
        )
        self.assertIn("V3-PACKAGE-CHECKS-OMITTED", codes(report), report.rendered())

    def test_raw_instruction_member_must_be_the_frozen_revision_not_just_the_path(self):
        """FIXED during this node (was a real defect): the substitution guard compares paths only.

        Invariant 9 binds membership by exact revision *and* digest, and the schema requires
        `raw_instruction` to pin a revision precisely so the tree it came from is disclosed.
        `check_package` then compares only `ref["path"]` against the WorkSpec, so a package
        that froze a different revision of the same instruction file passes — while
        `check_review_result` does compare the revision for the reviewer's own recheck ref,
        which is how the asymmetry is visible without inventing a requirement.

        The assertion here is the correct one.
        """
        members = make_members(drop="raw_instruction") + [
            member("m-instruction", "raw_instruction", "docs/instruction.md", DIGEST, revision="c" * 40)
        ]
        report = check_package(make_package(members), make_spec(), make_record(), [])
        self.assertIn("V3-PACKAGE-INSTRUCTION-SUBSTITUTED", codes(report), report.rendered())


# ===========================================================================
# Reachability — no named invariant may be permanently shadowed (the V3-N1 defect class)
# ===========================================================================


class NamedIssueReachabilityTests(unittest.TestCase):
    """Every issue code `review.py` can name must fire from a schema-valid document.

    V3-N1 shipped two named invariants that a schema validation running first made
    unreachable. `check_package` and `check_review_result` both return early on a schema
    error, so the same defect is available here; this sweep is the proof that it was not
    repeated.
    """

    PACKAGE_CODES = (
        "V3-PACKAGE-WORK-MISMATCH",
        "V3-PACKAGE-RUN-MISMATCH",
        "V3-PACKAGE-ROUND-MISMATCH",
        "V3-PACKAGE-WRONG-CANDIDATE",
        "V3-PACKAGE-INPUT-OMITTED",
        "V3-PACKAGE-CHECKS-OMITTED",
        "V3-PACKAGE-ARTIFACT-OMITTED",
        "V3-PACKAGE-INSTRUCTION-SUBSTITUTED",
        "V3-PACKAGE-MEMBER-MISSING",
        "V3-PACKAGE-MEMBER-STALE",
        "V3-PACKAGE-DUPLICATE-MEMBER-ID",
        "V3-PACKAGE-RECORD-CANDIDATE-UNBOUND",
        "V3-PACKAGE-CANDIDATE-BRANCH-MISMATCH",
        "V3-PACKAGE-BASE-MISMATCH",
    )

    REVIEW_CODES = (
        "V3-REVIEW-WORK-MISMATCH",
        "V3-REVIEW-PACKAGE-BINDING-MISMATCH",
        "V3-REVIEW-ROUND-MISMATCH",
        "V3-REVIEW-WRONG-CANDIDATE",
        "V3-REVIEW-OBLIGATION-UNDISPOSED",
        "V3-REVIEW-UNDECLARED-DISPOSITION",
        "V3-REVIEW-DUPLICATE-DISPOSITION",
        "V3-REVIEW-DANGLING-FINDING-REF",
        "V3-REVIEW-UNSUPPORTED-WITHOUT-FINDING",
        "V3-REVIEW-BLOCKER-CONTRADICTS-VERDICT",
        "V3-REVIEW-INCOMPLETE-UNDISCLOSED",
        "V3-REVIEW-INSTRUCTION-MISMATCH",
        "V3-REVIEW-VERIFY-SCOPE-INCOMPLETE",
        "V3-REVIEW-REVIEWER-DISTINCTNESS-UNVERIFIED",
        "V3-REVIEW-REVIEWER-NOT-DISTINGUISHABLE",
    )

    def test_the_code_inventory_is_the_whole_inventory(self):
        """The two lists above must name every `Issue(...)` code the module can emit."""
        import rsclib.document_harness.review as review_module

        source = inspect.getsource(review_module)
        prefixes = {"CODE": review_module.CODE, "PACKAGE_CODE": review_module.PACKAGE_CODE}
        emitted = {
            f"{prefixes[constant]}-{suffix}"
            for constant, suffix in re.findall(r'f"\{(CODE|PACKAGE_CODE)\}-([A-Z0-9-]+)"', source)
        }
        self.assertEqual(emitted, set(self.PACKAGE_CODES) | set(self.REVIEW_CODES))

    def test_every_named_package_code_is_reachable(self):
        fired: set[str] = set()
        for name, report in self._package_reports():
            self.assertTrue(report.issues, f"{name} produced no issue at all")
            fired.update(codes(report))
        for code in self.PACKAGE_CODES:
            with self.subTest(code=code):
                self.assertIn(code, fired)

    def test_every_named_review_code_is_reachable(self):
        fired: set[str] = set()
        for name, report in self._review_reports():
            self.assertTrue(report.issues, f"{name} produced no issue at all")
            fired.update(codes(report))
        for code in self.REVIEW_CODES:
            with self.subTest(code=code):
                self.assertIn(code, fired)

    def test_no_named_code_fires_on_a_clean_run(self):
        """The negative control for the whole sweep: nothing above is always-on."""
        package = make_package()
        self.assertEqual(codes(check_package(package, make_spec(), make_record(), [])), [])
        self.assertEqual(
            codes(check_review_result(make_result(package), make_spec(), package, executor=EXECUTOR)),
            [],
        )

    # -- fixtures for the two sweeps -------------------------------------------------

    def _package_reports(self):
        spec = make_spec(inputs=[{"path": "docs/source.md", "revision": FAKE_REV}])
        two_artifacts = make_spec(
            expected_artifacts=[
                {"artifact_id": "artifact-guide", "path": "docs/guide.md"},
                {"artifact_id": "artifact-appendix", "path": "docs/appendix.md"},
            ]
        )
        both_present = make_record(
            manifest={
                "authored_by": "deterministic diff verifier",
                "boundary_result": "CONFORMANT",
                "expected_artifact_results": [
                    {"artifact_id": "artifact-guide", "present": True},
                    {"artifact_id": "artifact-appendix", "present": True},
                ],
            }
        )
        substituted = make_members(drop="raw_instruction") + [
            member("m-instruction", "raw_instruction", "docs/other.md", DIGEST, revision=FAKE_REV)
        ]

        yield "work", check_package(make_package(work_id="work-other"), make_spec(), make_record(), [])
        yield "run", check_package(make_package(run_id="run-other"), make_spec(), make_record(), [])
        yield "round", check_package(make_package(repair_round=1), make_spec(), make_record(), [])
        yield "candidate", check_package(
            make_package(candidate_ref={"branch": "cand", "commit": OTHER_COMMIT}),
            make_spec(),
            make_record(),
            [],
        )
        yield "input", check_package(make_package(), spec, make_record(), [])
        yield "checks", check_package(
            make_package(), make_spec(), make_record(), [{"check_id": "chk-one"}]
        )
        yield "artifact", check_package(make_package(), two_artifacts, both_present, [])
        yield "instruction", check_package(make_package(substituted), make_spec(), make_record(), [])
        yield "record-unbound", check_package(
            make_package(), make_spec(), make_record(candidate_ref={"branch": "cand"}), []
        )
        yield "branch", check_package(
            make_package(candidate_ref={"branch": "other-branch", "commit": CANDIDATE_COMMIT}),
            make_spec(),
            make_record(),
            [],
        )
        yield "base", check_package(
            make_package(base_revision=OTHER_COMMIT), make_spec(), make_record(), []
        )

        with TempRepo({"docs/instruction.md": "instruction\n"}) as repo:
            repo.commit_candidate({"docs/guide.md": "## Guide\n"})
            repo.write({"control/coverage.json": '{"coverage":1}'})
            stale = make_package(
                [member("m-coverage", "coverage", "control/coverage.json", OTHER_DIGEST)]
            )
            missing = make_package(
                [member("m-coverage", "coverage", "control/absent.json", DIGEST)]
            )
            duplicated = make_package(
                [
                    member("m-dup", "coverage", "control/coverage.json", DIGEST),
                    member("m-dup", "manifest", "control/coverage.json", DIGEST),
                ]
            )
            yield "member-stale", verify_member_bytes(stale, repo.root)
            yield "member-missing", verify_member_bytes(missing, repo.root)
            yield "member-duplicate-id", verify_member_bytes(duplicated, repo.root)

    def _review_reports(self):
        spec = make_spec()
        package = make_package()
        verify_package = make_package(review_round="VERIFY")

        def result_with(**over):
            return make_result(package, **over)

        yield "work", check_review_result(
            result_with(work_id="work-other"), spec, package, executor=EXECUTOR
        )
        yield "binding", check_review_result(
            result_with(package_ref={"path": "control/package.json", "digest_sha256": OTHER_DIGEST}),
            spec,
            package,
            executor=EXECUTOR,
        )
        yield "round", check_review_result(
            result_with(review_round="VERIFY", verify_scope=dict(VERIFY_SCOPE)),
            spec,
            package,
            executor=EXECUTOR,
        )
        yield "candidate", check_review_result(
            result_with(candidate_ref={"branch": "cand", "commit": OTHER_COMMIT}),
            spec,
            package,
            executor=EXECUTOR,
        )
        yield "undisposed", check_review_result(
            result_with(
                per_obligation_disposition=[{"obligation_id": "ob-other", "disposition": "SUPPORTED"}]
            ),
            spec,
            package,
            executor=EXECUTOR,
        )
        yield "undeclared", check_review_result(
            result_with(
                per_obligation_disposition=[
                    {"obligation_id": "ob-guide", "disposition": "SUPPORTED"},
                    {"obligation_id": "ob-ghost", "disposition": "SUPPORTED"},
                ]
            ),
            spec,
            package,
            executor=EXECUTOR,
        )
        yield "duplicate", check_review_result(
            result_with(
                per_obligation_disposition=[
                    {"obligation_id": "ob-guide", "disposition": "SUPPORTED"},
                    {"obligation_id": "ob-guide", "disposition": "SUPPORTED", "note": "again"},
                ]
            ),
            spec,
            package,
            executor=EXECUTOR,
        )
        yield "dangling", check_review_result(
            result_with(
                per_obligation_disposition=[
                    {
                        "obligation_id": "ob-guide",
                        "disposition": "SUPPORTED",
                        "finding_ids": ["f-ghost"],
                    }
                ]
            ),
            spec,
            package,
            executor=EXECUTOR,
        )
        yield "unsupported", check_review_result(
            result_with(
                verdict="CHANGES_REQUIRED",
                findings=[BLOCKING_FINDING],
                per_obligation_disposition=[
                    {
                        "obligation_id": "ob-guide",
                        "disposition": "NOT_SUPPORTED",
                        "note": "the frozen subjects contradict the claim",
                    }
                ],
            ),
            spec,
            package,
            executor=EXECUTOR,
        )
        yield "blocker", check_review_result(
            result_with(findings=[BLOCKING_FINDING]), spec, package, executor=EXECUTOR
        )
        yield "incomplete", check_review_result(
            result_with(instruction_completeness=INCOMPLETE_RECHECK),
            spec,
            package,
            executor=EXECUTOR,
        )
        yield "instruction", check_review_result(
            result_with(
                instruction_completeness={
                    "result": "COMPLETE",
                    "instruction_ref": {"path": "docs/other.md", "revision": FAKE_REV},
                }
            ),
            spec,
            package,
            executor=EXECUTOR,
        )

        scope_result = make_result(
            verify_package,
            review_round="VERIFY",
            verify_scope={
                "accepted_finding_ids": ["f-one"],
                "repair_diff_reviewed": False,
                "permanent_boundaries_checked": False,
            },
        )
        yield "verify-scope", check_review_result(
            scope_result, spec, verify_package, executor=EXECUTOR
        )
        yield "distinctness-unverified", check_review_result(result_with(), spec, package)
        yield "distinctness", check_review_result(
            result_with(), spec, package, executor=REVIEWER
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
