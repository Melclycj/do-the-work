#!/usr/bin/env python3
"""Locks for the V3-N2 bounded fix round — the blocker and the six findings.

Every test here exists because the independent FULL review of candidate `0ba649c` found
something the acceptance matrix did not. They are kept in one file so the fix round's
additions stay attributable, rather than being folded invisibly into the two large halves.

The last class is the one that matters most. The FULL's finding F4 was not a defect in the
product at all — it was a defect in *the tests*: the named-code inventory sweep covered
`review.py` alone, and the other three modules were checked by a hand-written expected set
using a subset assertion, so any code missing from that list was never checked for
reachability at all. Two codes had already fallen through
(`V3-FLOW-STATE-INCOMPLETE`, `V3-FLOW-REPAIR-BOUNDARY-UNVERIFIED`): both existed, neither
appeared anywhere in the suite. `EveryNamedCodeIsAssertedSomewhere` closes that by reading the
codes out of all four modules and requiring each to be named by some test — a guard that
covers codes nobody has thought to add yet, which a hand-written list by construction cannot.

Offline and deterministic.
"""
from __future__ import annotations

import pathlib
import re
import sys
import unittest

import _harness  # noqa: F401 — installs the tooling and V3-N1 import paths

from rsclib.document_harness import Report, flow, issues, summary  # noqa: E402

MODULES = (flow, issues, summary)
TEST_DIR = pathlib.Path(__file__).resolve().parent
RSCLIB = _harness.TOOLING_DIR / "rsclib" / "document_harness"

COMMIT_A = "a" * 40
COMMIT_B = "9" * 40


def codes(report: Report) -> list[str]:
    return [issue.code for issue in report.issues]


def make_repair_decision(*, accepted: list[str], decision: str = "APPLY_ACCEPTED_FINDINGS") -> dict:
    return {
        "decision_id": "decision-repair",
        "work_id": "work-one",
        "run_id": "run-one",
        "phase": "REPAIR",
        "decision": decision,
        "target": {
            "candidate_ref": {"branch": "cand", "commit": COMMIT_A},
            "accepted_finding_ids": accepted,
            "repair_boundary": {"write_scope": ["docs"], "out": ["docs/private"]},
        },
        "decided_by": "User Melclycj",
        "decided_at": "2026-07-20",
    }


def make_verify(*, covered: list[str], findings: list[dict] | None = None) -> dict:
    """A whole v2 VERIFY result, hand-written field by field.

    It used to carry only the four keys the outcome gate reads. Round
    `PROMISE-PATH-ENGINE` (item 7) made `flow.check_verify_outcome` validate the result
    before reading it, so a fixture trimmed to the read fields is now refused by the schema
    before any property below is reached -- which is the fix working, and the reason this
    literal grew. `findings` is added only when there are some: the schema forbids the empty
    array, so `or []` would make every clean VERIFY here schema-invalid. Nothing is imported
    from the module under test (E5).
    """
    result = {
        "schema_version": "2",
        "result_id": "rr-verify",
        "work_id": "work-one",
        "run_id": "run-one",
        "review_round": "VERIFY",
        "subject": {
            "evidence_commit": COMMIT_B,
            "candidate_ref": {"branch": "cand", "commit": COMMIT_A},
            "base_revision": "0" * 40,
            "control_root": "runs/run-one",
            "repair_round": 1,
        },
        "verdict": "REVIEWED_NO_BLOCKER",
        "instruction_completeness": {
            "result": "COMPLETE",
            "instruction_ref": {"path": "docs/instruction.md", "revision": "0" * 40},
        },
        "per_obligation_disposition": [
            {"obligation_id": "ob-one", "disposition": "SUPPORTED"}
        ],
        "residual_uncertainty": [],
        "verify_scope": {
            "accepted_finding_ids": covered,
            "repair_diff_reviewed": True,
            "permanent_boundaries_checked": True,
        },
        "reviewed_by": "independent reviewer",
    }
    if findings:
        result["findings"] = findings
    return result


#: A blocking finding with every field a blocker may not omit -- `minimum_fix` is what a
#: REPAIR boundary is derived from, so the schema requires it of a blocking finding.
BLOCKING_FINDING = {
    "finding_id": "f-a",
    "blocking": True,
    "statement": "the candidate does not carry the release the instruction froze",
    "candidate_locator": {"path": "docs/changelog.md", "anchor": "## 1.2.0"},
    "ground_truth_locator": {"path": "docs/instruction.md", "anchor": "## release"},
    "minimum_fix": "name the release the instruction froze",
}


class VerifyCoversWhatTheUserApproved(unittest.TestCase):
    """B1 — the declared VERIFY scope is reconciled against the approved repair.

    Before this, a VERIFY could declare it had covered finding C while the user approved A
    and B, and nothing anywhere compared the two. The same shape as a summary terminating a
    candidate the user never decided about, one step later in the flow.
    """

    def test_a_finding_the_user_approved_but_the_verify_skipped_is_named(self):
        report = flow.check_verify_outcome(
            make_verify(covered=["f-b"]), make_repair_decision(accepted=["f-a", "f-b"])
        )
        self.assertIn("V3-FLOW-VERIFY-SCOPE-MISMATCH", codes(report))
        self.assertIn("f-a", " ".join(report.rendered()))

    def test_a_finding_the_verify_claims_but_the_user_never_approved_is_named(self):
        report = flow.check_verify_outcome(
            make_verify(covered=["f-a", "f-c"]), make_repair_decision(accepted=["f-a"])
        )
        self.assertIn("V3-FLOW-VERIFY-SCOPE-MISMATCH", codes(report))
        self.assertIn("f-c", " ".join(report.rendered()))

    def test_the_exact_case_the_review_found(self):
        """Approved A and B, VERIFY declares C. Two mismatches, not silence."""
        report = flow.check_verify_outcome(
            make_verify(covered=["f-c"]), make_repair_decision(accepted=["f-a", "f-b"])
        )
        self.assertEqual(
            codes(report),
            ["V3-FLOW-VERIFY-SCOPE-MISMATCH"] * 3,  # a and b missed, c unapproved
        )

    def test_a_verify_answering_a_no_repair_decision_is_named(self):
        report = flow.check_verify_outcome(
            make_verify(covered=["f-a"]), make_repair_decision(accepted=["f-a"], decision="NO_REPAIR")
        )
        self.assertIn("V3-FLOW-VERIFY-WITHOUT-REPAIR", codes(report))

    def test_negative_control_matching_scopes_are_silent(self):
        """The guard is not always-on: identical sets raise nothing."""
        report = flow.check_verify_outcome(
            make_verify(covered=["f-a", "f-b"]), make_repair_decision(accepted=["f-b", "f-a"])
        )
        self.assertEqual(codes(report), [])

    def test_the_decision_cannot_be_omitted(self):
        """Optional would be the fail-open shape this node has now hit four times."""
        with self.assertRaises(TypeError):
            flow.check_verify_outcome(make_verify(covered=["f-a"]))  # type: ignore[call-arg]

    def test_a_blocker_still_standing_after_verify_stops_the_run(self):
        """The pre-existing N2-A6 property must survive the new argument."""
        report = flow.check_verify_outcome(
            make_verify(covered=["f-a"], findings=[BLOCKING_FINDING]),
            make_repair_decision(accepted=["f-a"]),
        )
        self.assertIn("V3-FLOW-BLOCKER-AFTER-VERIFY", codes(report))


class MalformedDocumentsAreReportedNotRaised(unittest.TestCase):
    """F1 and F2 — a checker that raises takes the run down instead of recording what happened.

    Two of these were fixed earlier in the node but pinned by nothing: reverting either fix
    left all 176 tests green, which is the definition of an unlocked fix.
    """

    def test_a_state_with_no_repair_round_is_reported(self):
        report = flow.check_transition({"status": "REVIEWED"}, "REPAIRING")
        self.assertEqual(codes(report), ["V3-FLOW-STATE-INCOMPLETE"])

    def test_a_state_with_no_status_is_reported(self):
        """The sibling case, missed when only the round was guarded."""
        report = flow.check_transition({"repair_round": 0}, "REPAIRING")
        self.assertEqual(codes(report), ["V3-FLOW-STATE-INCOMPLETE"])

    def test_a_run_state_missing_its_identity_is_reported(self):
        issue = issues.record_issue(
            issue_id="issue-one",
            work_id="work-one",
            run_id="run-one",
            kind="HARNESS_DEFECT",
            statement="the manifest was regenerated twice",
            evidence_refs=[{"path": "control/manifest.json", "digest_sha256": "e" * 64}],
            observed_after="CLOSED",
            observed_by="Observer Oki",
        )
        report = issues.check_issue(issue, {"status": "CLOSED"})  # no run_id
        self.assertEqual(codes(report), ["V3-HARNESS-ISSUE-RUN-STATE-UNVERIFIED"])

    def test_a_governance_block_of_the_wrong_type_is_reported(self):
        report = flow.check_governance_obligation({"governance_scan": "it ran, honest"})
        self.assertEqual(codes(report), ["V3-FLOW-GOVERNANCE-UNSTATED"])

    def test_a_governance_block_of_the_wrong_type_still_produces_a_disclosure(self):
        """Silence about whether the scan ran is the one outcome N1-R2 forbids."""
        disclosures = flow.governance_disclosures(
            {"governance_scan": "it ran, honest"}, {"path": "control/assurance.json"}
        )
        self.assertEqual(len(disclosures), 1)
        self.assertIn("malformed", disclosures[0]["statement"])

    def test_a_final_decision_whose_target_is_the_wrong_type_is_reported(self):
        report = summary.check_summary(
            {"summary_id": "s-1", "promotion": {"promoted": False}}, {}, {"target": "not a mapping"}
        )
        self.assertTrue(report.issues)  # reported, and above all not raised

    def test_negative_control_well_formed_documents_raise_none_of_these(self):
        report = flow.check_transition(
            {"status": "REVIEWED", "repair_round": 0, "work_id": "w", "run_id": "r"}, "REPAIRING"
        )
        self.assertEqual(codes(report), [])


class RepairBindingIsNeverSilentlySkipped(unittest.TestCase):
    """F3 -- a repair that cannot be shown to bind the reviewed candidate never passes.

    F3's own finding was that the guard fell silent: `if reviewed_commit and ...` switched
    itself off for a review naming only a branch, and raised outright for one naming no
    candidate at all. Both cases are still refused, and since round `PROMISE-PATH-ENGINE`
    (item 7) they are refused one layer earlier: `check_repair_decision` validates the review
    before reading it, and `review.v2.schema.json` requires `subject.candidate_ref` and
    requires a `commit` inside it. The two methods below therefore assert the SCHEMA code
    rather than the flow's UNVERIFIED one -- the property is unchanged, the layer holding it
    is not, and this file pins layers rather than inferring them. The flow's own guard stays
    as the second layer and is still reached for the bindings the schema leaves optional
    (`run_id`), which is where `V3-FLOW-REPAIR-BINDING-UNVERIFIED` is asserted.
    """

    def _review(self, candidate_ref=None):
        """A schema-valid v2 review except for the candidate binding under test."""
        review = {
            "schema_version": "2",
            "result_id": "rr-full",
            "work_id": "work-one",
            "run_id": "run-one",
            "review_round": "FULL",
            "subject": {
                "evidence_commit": COMMIT_B,
                "base_revision": "0" * 40,
                "control_root": "runs/run-one",
                "repair_round": 0,
            },
            "verdict": "CHANGES_REQUIRED",
            "instruction_completeness": {
                "result": "COMPLETE",
                "instruction_ref": {"path": "docs/instruction.md", "revision": "0" * 40},
            },
            "per_obligation_disposition": [
                {"obligation_id": "ob-one", "disposition": "NOT_SUPPORTED",
                 "note": "the frozen subjects contradict the fulfillment claim",
                 "finding_ids": ["f-a"]}
            ],
            "residual_uncertainty": [],
            "findings": [BLOCKING_FINDING],
            "reviewed_by": "independent reviewer",
        }
        if candidate_ref is not None:
            review["subject"]["candidate_ref"] = candidate_ref
        return review

    def _plan(self):
        return {"effective_change_boundary": {"write_scope": ["docs"], "out": ["docs/private"]}}

    def test_a_review_naming_only_a_branch_is_refused(self):
        report = flow.check_repair_decision(
            make_repair_decision(accepted=["f-a"]), self._review({"branch": "cand"}), self._plan()
        )
        self.assertEqual(codes(report), ["V3-SCHEMA-REVIEW_RESULT_V2"])

    def test_a_review_with_no_candidate_at_all_is_reported_not_raised(self):
        report = flow.check_repair_decision(
            make_repair_decision(accepted=["f-a"]), self._review(), self._plan()
        )
        self.assertEqual(codes(report), ["V3-SCHEMA-REVIEW_RESULT_V2"])

    def test_a_decision_naming_no_run_is_still_reported_unverified(self):
        """The flow's own UNVERIFIED guard, on the binding the schema leaves optional."""
        decision = make_repair_decision(accepted=["f-a"])
        del decision["run_id"]
        report = flow.check_repair_decision(
            decision, self._review({"branch": "cand", "commit": COMMIT_A}), self._plan()
        )
        self.assertEqual(codes(report), ["V3-FLOW-REPAIR-BINDING-UNVERIFIED"])

    def test_negative_control_an_exact_commit_verifies_silently(self):
        report = flow.check_repair_decision(
            make_repair_decision(accepted=["f-a"]),
            self._review({"branch": "cand", "commit": COMMIT_A}),
            self._plan(),
        )
        self.assertEqual(codes(report), [])

    def test_a_repair_binding_the_wrong_candidate_is_still_caught(self):
        report = flow.check_repair_decision(
            make_repair_decision(accepted=["f-a"]),
            self._review({"branch": "cand", "commit": COMMIT_B}),
            self._plan(),
        )
        self.assertIn("V3-FLOW-REPAIR-WRONG-CANDIDATE", codes(report))


# `TheReviewCommandReportsRatherThanCrashes` stood here: F5's pin that a schema-invalid
# ReviewPackage reached the `review --package` command as a report and not as a traceback.
# Round `CORE-SET-CODE` retired that mode, so there is no longer a package for the command
# to be handed. The surviving half of F5 — a malformed document reported rather than traced
# — is asserted against the subject mode in `test_review_cli_v2_subject.py`.


class EveryNamedCodeIsAssertedSomewhere(unittest.TestCase):
    """F4 — no named issue code may exist without some test naming it.

    The inventory sweep it replaces covered one module and compared against a hand-written
    list, so a code absent from that list was never checked. This reads the codes out of the
    source instead, which means a code added later is covered the moment it is written — the
    property the hand-written list could not have.
    """

    CODE_PATTERN = re.compile(r'f"\{(?:CODE|PACKAGE_CODE|GOVERNANCE_CODE)\}(-[A-Z0-9-]+)"')

    #: The prefix declaration the pattern above interpolates. Read together they are the two
    #: halves of a coded vocabulary, and `test_the_no_code_listing_stays_true` needs both:
    #: a module acquires one by declaring a prefix and then using it, and either half alone
    #: is enough to say the listing below has gone stale.
    PREFIX_PATTERN = re.compile(r'^(?:CODE|PACKAGE_CODE|GOVERNANCE_CODE)\s*=\s*"[^"]+"', re.M)

    #: The modules V3-N2 authored that still name coded issues. N1's modules carry their own
    #: named codes and are covered by N1's own signed matrix; sweeping them here would make
    #: this node's suite responsible for an earlier node's coverage, which is not what F4
    #: asked for.
    N2_MODULES = ("flow.py", "summary.py", "issues.py")

    #: V3-N2 modules with NO coded vocabulary left to sweep — listed rather than dropped, so
    #: the partition below still accounts for them. That is the whole of what listing buys,
    #: and the boundary belongs here rather than in a reader's assumption: the partition
    #: reacts to a *module*, never to a *code*. `named_codes()` reads `N2_MODULES` alone and
    #: the partition compares module names against the directory, so a coded vocabulary
    #: returning to a module listed here is swept by nothing and stays green. The way back is
    #: to move that module into `N2_MODULES`, which is the only thing that restores a sweep.
    #: Measured 2026-08-27 (round `CORE-SET-CODE`'s fix leg, answering `B-1` of
    #: `v3-review-full-1db5155.md`): `CODE = "V3-REVIEW"` plus one `f"{CODE}-UNSWEPT-CODE"`
    #: call site added to `review.py`, asserted by no test, left this class at 21 passed and
    #: the whole battery at 795 passed — while `CODE_PATTERN` matched the added code when run
    #: against the file by hand, so the blind spot is the module list and not the regex.
    #: `review.py` joined 2026-08-27 (round `CORE-SET-CODE`): its `CODE` / `PACKAGE_CODE`
    #: vocabulary was the version-1 package leg's — `V3-PACKAGE-*` from `check_package` and
    #: `verify_member_bytes`, `V3-REVIEW-*` from `check_review_result` — and retired with it.
    #: What the module still emits is `V3-SCHEMA-<KIND>`, built from the kind argument rather
    #: than from a module constant, so this regex cannot see it and a sweep here would report
    #: an empty vocabulary as a covered one. What stands in its place is `N2ValidatorTests` in
    #: `test_golden_review_views.py`, which drives every registered kind through
    #: `validate_n2` and requires each to produce a non-clean report — the reachability
    #: property, asserted where the codes are actually raised.
    #: The hole that measurement found is closed from the other side since round
    #: `V1-RESULT-RETIRE` (2026-08-28): `test_the_no_code_listing_stays_true` below asserts
    #: that every module named here really declares no code prefix and names none at a call
    #: site, so re-running the measured mutation now turns this class red instead of leaving
    #: the battery green. The substitute named above was carrying a second instance of the
    #: same F4 shape — it iterated the kind tables it was checking — and gained a
    #: hand-written expectation for them in the same round.
    N2_MODULES_WITHOUT_CODES = ("review.py",)

    #: The V3-N1 modules, listed so the two sets can be checked to partition the package.
    N1_MODULES = (
        "spec.py",
        "assurance_profiles.py",
        "assurance_plan.py",
        "assurance_state.py",
        "instruction.py",
        "candidate.py",
        "checks.py",
        "views.py",
    )

    #: Modules authored by a later successor ROUND rather than by a node. Excluded from this
    #: node's sweep for the same reason as N1's: the round that wrote them carries its own
    #: reachability sweep — wave 2's lives in `test_review_v2_subject.py`
    #: (`NamedIssueReachability`) and `dispatch.py`'s in `test_dispatch.py` (same class
    #: name), each reading its codes out of the source the same way and requiring each to be
    #: asserted by name. Listing them here keeps the partition honest: a module belonging to
    #: no set still fails — which is how `dispatch.py` announced itself when it was added.
    #: `enumerations.py` joined 2026-08-05 (round SIMP-ABCD); its sweep is
    #: `NamedIssueReachability` in `tests/document_harness/test_transcript_audit.py`, beside
    #: the tests that name its codes.
    #: `paths.py` joined 2026-08-06 (round SIMP-A4) and is the one member here with NO code
    #: sweep, because it names no coded issue: its whole vocabulary is the three plain
    #: constants `DIRECT` / `SHORTHAND` / `UNRESOLVED`, so a reachability scan would be
    #: vacuous rather than reassuring. What stands in its place is the acceptance matrix
    #: `CandidatePath` + `CandidateScanScope` in
    #: `tests/document_harness/test_precommit_checks.py`, each must-fire case paired with a
    #: negative control and the whole set mutation-tested against five neutered mechanisms.
    #: Listed rather than silently excluded: a later module that *does* name codes must not
    #: be able to hide behind this precedent — it fails this partition until someone says
    #: which sweep covers it.
    #: `cli.py` joined 2026-08-16 (split batch R2), the six command bodies moved verbatim out
    #: of `rsc.py`. Second member with NO code sweep, and for a different reason than
    #: `paths.py`: it names no code because it *originates* none — every code it prints was
    #: raised by the module it called, and each of those is swept where it lives. A sweep
    #: here would re-assert other modules' vocabulary through a caller, which is the shape
    #: that makes a green sweep uninformative. What stands in its place: `TheSurface` +
    #: `TheTwoNames` in `tests/document_harness/test_cli_entry.py` (the operation surface and
    #: the two entry names, both mutation-tested), plus the **two** suites that drive real
    #: commands through it in a subprocess — `test_dispatch_freeze_marker.py` and
    #: `test_review_cli_v2_subject.py` — each asserting an effect or a code only the called
    #: function can produce, which is what proves the CLI reaches it. (`test_dispatch.py`
    #: was named here as a third until the FULL of `297bb2b` `L-2` measured it: it exercises
    #: `dispatch` in-process off the module, never through the entry, so it says nothing
    #: about the CLI.)
    #: `init_target.py` joined 2026-08-19 (round CALLER-ONBOARDING), the body of the seventh
    #: command. Third member with NO code sweep, and for a third reason: it raises only plain
    #: stdlib exceptions and returns a dataclass, so it has no coded vocabulary to sweep —
    #: `FileNotFoundError` / `NotADirectoryError` reach the caller as the CLI's `FATAL` line.
    #: What stands in its place is `tests/document_harness/test_init_command.py`, whose two
    #: load-bearing properties (the copy is verbatim; an existing file is never overwritten)
    #: are mutation-tested — three neutered mechanisms, each turning the matching case red.
    #: This module announced itself here when it was added, which is the sentence above
    #: working rather than a nuisance.
    #: `preview.py` joined 2026-08-21 (round PREVIEW-RENDER), the body of the eighth
    #: command. Its sweep is `NamedIssueReachability` in
    #: `tests/document_harness/test_preview.py`, beside the tests that name its one code —
    #: the same shape as `dispatch.py`'s: read the codes out of the source, require each
    #: asserted by name, and pin the count so a code surface that moves announces itself.
    #: `caller.py` joined 2026-08-23 (round STRANGER-GUARDS): repository-root discovery and
    #: the scan-surface declaration both pre-commit guards read. Fourth member with NO code
    #: sweep, `init_target.py`'s reason: it raises plain `SpecGap` /
    #: `SurfaceDeclarationError` prose and names no coded issue. What stands in its place:
    #: `tests/document_harness/test_caller_surfaces.py` (declaration loading, loud refusal,
    #: both guards driven under declared surfaces) and
    #: `tests/document_harness/test_repo_root_discovery.py` (discovery and refusal, unit
    #: and through the CLI), each must-fire case paired with a control.
    SUCCESSOR_ROUND_MODULES = (
        "review_subject.py", "review_result_v2.py", "dispatch.py", "enumerations.py",
        "paths.py", "cli.py", "init_target.py", "preview.py", "caller.py",
    )

    def named_codes(self) -> dict[str, set[str]]:
        found: dict[str, set[str]] = {}
        for path in sorted(RSCLIB / name for name in self.N2_MODULES):
            source = path.read_text(encoding="utf-8")
            prefixes = dict(re.findall(r'^(CODE|PACKAGE_CODE|GOVERNANCE_CODE)\s*=\s*"([^"]+)"', source, re.M))
            suffixes = set()
            for match in re.finditer(r'f"\{(CODE|PACKAGE_CODE|GOVERNANCE_CODE)\}(-[A-Z0-9-]+)"', source):
                prefix = prefixes.get(match.group(1))
                if prefix:
                    suffixes.add(prefix + match.group(2))
            if suffixes:
                found[path.name] = suffixes
        return found

    def test_the_no_code_listing_stays_true(self):
        """`N2_MODULES_WITHOUT_CODES` is a hole in the sweep; this keeps the hole empty.

        The comment above that constant records the measurement: a module listed there is
        read by `named_codes()` never, so a coded vocabulary returning to it is swept by
        nothing and the whole battery stays green — `CODE = "V3-REVIEW"` plus one call site
        added to `review.py` left 795 tests passing at round `CORE-SET-CODE`. The comment
        names the way back (move the module into `N2_MODULES`) and nothing made anyone take
        it, because nothing failed.

        Rather than sweep a module that has no vocabulary to sweep, this asserts the
        listing's own precondition: each listed module declares no code prefix and uses
        none. The moment either appears the listing is a false statement and this goes red,
        which is the signal the measurement found missing.

        `flow.py` is the control. Both patterns must find their shape there, so a pattern
        that had stopped matching anything could not report the exclusion list as clean —
        the vacuous-scan trap this class already guards against for `N2_MODULES`.
        """
        control = (RSCLIB / "flow.py").read_text(encoding="utf-8")
        self.assertTrue(
            self.PREFIX_PATTERN.search(control),
            "the prefix pattern matched nothing in flow.py, so a clean result below would "
            "prove nothing",
        )
        self.assertTrue(
            self.CODE_PATTERN.search(control),
            "the call-site pattern matched nothing in flow.py, so a clean result below "
            "would prove nothing",
        )
        for name in self.N2_MODULES_WITHOUT_CODES:
            with self.subTest(module=name):
                source = (RSCLIB / name).read_text(encoding="utf-8")
                self.assertEqual(
                    self.PREFIX_PATTERN.findall(source),
                    [],
                    f"{name} is listed as having no coded vocabulary but declares a code "
                    "prefix; move it into N2_MODULES so the sweep actually reads it",
                )
                self.assertEqual(
                    self.CODE_PATTERN.findall(source),
                    [],
                    f"{name} is listed as having no coded vocabulary but names a code at a "
                    "call site; move it into N2_MODULES so the sweep actually reads it",
                )

    def test_the_swept_set_and_the_n1_set_partition_the_package(self):
        """The sweep's own scope is pinned — otherwise narrowing it goes unnoticed.

        Mutation-tested and found toothless in its first form: shrinking `N2_MODULES` to a
        single entry left every assertion green, because the coverage test iterated the same
        list it was supposed to be checking. That is the F4 defect class — a sweep that
        silently covers less — reappearing inside the fix for F4. Comparing against the
        directory instead makes a shrunk list, or a module belonging to neither node, fail.
        """
        present = {path.name for path in RSCLIB.glob("*.py")} - {"__init__.py"}
        self.assertEqual(
            present,
            set(self.N2_MODULES)
            | set(self.N2_MODULES_WITHOUT_CODES)
            | set(self.N1_MODULES)
            | set(self.SUCCESSOR_ROUND_MODULES),
            "a module in the package belongs to neither the swept V3-N2 set, the V3-N2 set "
            "with no coded vocabulary, the V3-N1 exclusion list nor a successor round's own "
            "sweep, so nothing checks whether its named codes can fire",
        )

    def test_the_sweep_actually_finds_codes_in_every_v3n2_module(self):
        """Guard against a regex that silently matches nothing — the vacuous-scan trap."""
        found = self.named_codes()
        for name in self.N2_MODULES:
            with self.subTest(module=name):
                self.assertIn(name, found)
                self.assertGreater(len(found[name]), 3, f"{name} yielded suspiciously few codes")

    def test_every_named_code_is_named_by_at_least_one_test(self):
        suite_text = "\n".join(
            path.read_text(encoding="utf-8") for path in sorted(TEST_DIR.glob("test_*.py"))
        )
        unasserted = sorted(
            code
            for codes_for_module in self.named_codes().values()
            for code in codes_for_module
            if code not in suite_text
        )
        self.assertEqual(
            unasserted,
            [],
            "these named codes exist in the implementation but no test names them, so nothing "
            f"checks they can ever fire: {unasserted}",
        )


if __name__ == "__main__":
    raise SystemExit(unittest.main(argv=[sys.argv[0]]))
