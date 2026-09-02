#!/usr/bin/env python3
"""M9 — the v2 bind template binds the round that actually happened, not always round 0.

The defect CLASS (E7), not the one reported line: a bind step that hard-reads
``review-full.json``, binds a single ref and has no ``repair_round`` branch makes every
repaired run's binding wrong three ways at once — the operative review (the targeted
VERIFY) is never validated, the state pointer stays on the round-0 FULL, and the
AssuranceCandidate binds one review where two happened, which p3-corr could only work
around by hand-writing the whole step (``runs/p3-corr/run_bind_candidate.py``). The
property under test is "the round decides which review files are read, validated and
pointed at, and the binding covers every round that happened", whatever the template's
internal spelling.

Every expectation below is a hand-written literal and is never imported from the template
(E5): a test that asked the module for its own answer would pass against any answer.
Assertions are made against WHOLE returned structures and whole printed lines. The
``canonical_digest`` / ``report_of`` helpers imported here come from rsclib — the library
under its own suites — never from the template under test.

The template is loaded by explicit file path under a distinct module name — importing it
runs only its module level (its ``main`` is guarded by ``__name__``). Failure mode of the
``run_main`` helper follows the C0 F2 lesson: an exception inside ``main`` returns None,
so "the guard did not fire" shows up as a VALUE mismatch (None != 1), never as a test
ERROR that would prove reachability but not behaviour (R8).

Since R2 (`HD-11` part one) the template carries no CONFIG block: the run directory and the
round's refs arrive as ARGUMENTS and the per-run constants are read from the run's own
``control/`` JSON. So every fixture here builds the real directory shape
``<tmp>/ResearchSystem/assurance/runs/<run-id>/{control,evidence}`` — the layout the
template derives the repository root and the control root from — instead of re-pointing
module globals at a flat temp directory, which is what used to hide that derivation.
"""
from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import pathlib
import shutil
import sys
import subprocess
import tempfile
import unittest

import _harness  # noqa: F401 — installs the tooling import path the template needs

from rsclib.document_harness import AssuranceFault, Issue, bytes_digest, canonical_digest, report_of

TEMPLATE_PATH: pathlib.Path = (
    _harness.RS_ROOT / "assurance" / "templates" / "run-v2" / "run_bind_v2.py"
)


def load_template():
    """Bind the template file directly; never by adding its directory to sys.path."""
    if not TEMPLATE_PATH.is_file():
        raise RuntimeError(f"the v2 bind template is missing at {TEMPLATE_PATH}")
    spec = importlib.util.spec_from_file_location("v2_bind_template", TEMPLATE_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules["v2_bind_template"] = module
    spec.loader.exec_module(module)
    return module


def run_main(template, argv):
    """Run main(argv) capturing stdout; an exception returns None so guards fail on VALUE."""
    buffer = io.StringIO()
    try:
        with contextlib.redirect_stdout(buffer):
            code = template.main(argv)
    except Exception:
        return None, buffer.getvalue()
    return code, buffer.getvalue()


class RecordingResultChecker:
    """Stands in for the review_result_v2 module: records the document the gate received.

    The real checker needs a git repository behind the evidence commit; which DOCUMENT
    reaches it is a property of the template alone, and that is all this records.
    """

    def __init__(self, report):
        self.report = report
        self.received = None

    def check_review_result_v2(self, result, repo_root, *, evidence_commit, executor=None):
        self.received = result
        return self.report


class RecordingOutcomeGate:
    """Stands in for the flow module: records the (verify, repair decision) pair."""

    def __init__(self, report):
        self.report = report
        self.received = None

    def check_verify_outcome(self, verify, repair_decision):
        self.received = (verify, repair_decision)
        return self.report


def clean_report():
    return report_of([])


def failing_report():
    return report_of([Issue("V3-TEST-STOP", "stop main here for the recorder", "test")])


#: Hand-written review rounds, never copied from any run on disk. The FULL found one blocker
#: and one non-blocker; the VERIFY covered the approved repair and stands clean.
#:
#: They are whole v2 documents rather than the few keys the template's own helpers read,
#: because round `PROMISE-PATH-ENGINE` gave the step two gates that validate a review before
#: reading it: item 7's entry inside `flow.check_repair_decision`, which the R10 branch calls
#: with the FULL, and the same entry inside `flow.check_verify_outcome`.
BLOCKER_F1 = {
    "finding_id": "f1",
    "blocking": True,
    "statement": "the changelog does not name the release the instruction froze",
    "candidate_locator": {"path": "docs/changelog.md", "anchor": "## 1.2.0"},
    "ground_truth_locator": {"path": "docs/instruction.md", "anchor": "## release"},
    "minimum_fix": "name the release the instruction froze",
}
LOW_F2 = {
    "finding_id": "f2",
    "blocking": False,
    "statement": "two headings use different capitalisation",
}


def full_review(*, result_id, verdict, findings, disposition):
    """One round-0 FULL, spelled out once so the three below cannot drift apart.

    Everything the schema requires is here; nothing is derived from the module under test.
    """
    review = {
        "schema_version": "2",
        "result_id": result_id,
        "work_id": "w-test",
        "run_id": "tr-nine",
        "review_round": "FULL",
        "subject": {
            "evidence_commit": "a" * 40,
            "candidate_ref": {"branch": "run/tr-nine", "commit": "c" * 40},
            "base_revision": "d" * 40,
            "control_root": "ResearchSystem/assurance/runs/tr-nine",
            "repair_round": 0,
        },
        "verdict": verdict,
        "instruction_completeness": {
            "result": "COMPLETE",
            "instruction_ref": {
                "path": "ResearchSystem/assurance/runs/tr-nine/instruction.md",
                "revision": "d" * 40,
            },
        },
        "per_obligation_disposition": [disposition],
        "residual_uncertainty": [],
        "reviewed_by": "independent reviewer",
    }
    if findings:
        review["findings"] = findings
    return review


FULL_REVIEW = full_review(
    result_id="rv-full",
    verdict="CHANGES_REQUIRED",
    findings=[BLOCKER_F1, LOW_F2],
    disposition={
        "obligation_id": "ob-one",
        "disposition": "NOT_SUPPORTED",
        "note": "the frozen subjects contradict the fulfillment claim",
        "finding_ids": ["f1"],
    },
)
#: The other round-0 shape. The verdict — not the round — decides whether the bind builds an
#: AssuranceCandidate at all, so a clean FULL is a distinct fixture rather than a flag on the
#: one above; several negative controls below need a round 0 that walks the whole path.
#: This one carries a LOW, which since round `PROMISE-PATH-ENGINE` makes it an `R10` decision
#: point rather than a green light.
CLEAN_FULL_REVIEW = full_review(
    result_id="rv-full-clean",
    verdict="REVIEWED_NO_BLOCKER",
    findings=[LOW_F2],
    disposition={"obligation_id": "ob-one", "disposition": "SUPPORTED"},
)
#: The third round-0 shape: clean AND carrying nothing to decide. `R10`'s trigger is the
#: lows, so this is the one clean FULL that still walks straight through to the candidate,
#: and it is what the negative controls below use when the property under test is about
#: something other than the decision point.
CLEAN_FULL_NO_LOWS = full_review(
    result_id="rv-full-spotless",
    verdict="REVIEWED_NO_BLOCKER",
    findings=[],
    disposition={"obligation_id": "ob-one", "disposition": "SUPPORTED"},
)
#: The user's recorded choice NOT to spend the repair leg on the low. Read by the bind's R10
#: branch and gated by the real `flow.check_repair_decision`, so it binds this run's reviewed
#: candidate, this work and this run by identity.
NO_REPAIR_DECISION = {
    "decision_id": "ud-repair",
    "work_id": "w-test",
    "run_id": "tr-nine",
    "phase": "REPAIR",
    "decision": "NO_REPAIR",
    "target": {"candidate_ref": {"branch": "run/tr-nine", "commit": "c" * 40}},
    "decided_by": "Melclycj (user)",
    "decided_at": "2026-09-02",
}
#: The opposite choice, same bindings: the user spends the leg on the low.
APPLY_LOWS_DECISION = {
    **NO_REPAIR_DECISION,
    "decision": "APPLY_ACCEPTED_FINDINGS",
    "target": {
        "candidate_ref": {"branch": "run/tr-nine", "commit": "c" * 40},
        "accepted_finding_ids": ["f2"],
        "repair_boundary": {"write_scope": ["docs"], "out": ["docs/private"]},
    },
}
#: The round-1 VERIFY, written out whole. The other fixtures here carry the minimum the
#: template's own helpers read, and this one cannot: round `PROMISE-PATH-ENGINE` (item 7)
#: made ``flow.check_verify_outcome`` validate the result before reading it, and this fixture
#: is the one that reaches the REAL gate (`TheAssembledCandidatePassesTheRealFaithfulnessGate`
#: leaves `flow` unstubbed). `findings` is absent rather than empty: the schema forbids the
#: empty array, and a clean VERIFY found none.
VERIFY_REVIEW = {
    "schema_version": "2",
    "result_id": "rv-verify",
    "work_id": "w-test",
    "run_id": "tr-nine",
    "review_round": "VERIFY",
    "subject": {
        "evidence_commit": "a" * 40,
        "candidate_ref": {"branch": "run/tr-nine", "commit": "c" * 40},
        "base_revision": "d" * 40,
        "control_root": "ResearchSystem/assurance/runs/tr-nine",
        "repair_round": 1,
    },
    "verdict": "REVIEWED_NO_BLOCKER",
    "instruction_completeness": {
        "result": "COMPLETE",
        "instruction_ref": {
            "path": "ResearchSystem/assurance/runs/tr-nine/instruction.md",
            "revision": "d" * 40,
        },
    },
    "per_obligation_disposition": [{"obligation_id": "ob-one", "disposition": "SUPPORTED"}],
    "residual_uncertainty": [],
    "verify_scope": {
        "accepted_finding_ids": ["f1"],
        "repair_diff_reviewed": True,
        "permanent_boundaries_checked": True,
    },
    "reviewed_by": "independent reviewer",
}
REPAIR_DECISION = {
    "decision": "APPLY_ACCEPTED_FINDINGS",
    "target": {"accepted_finding_ids": ["f1"]},
}

CONTROL_ROOT = "ResearchSystem/assurance/runs/tr-nine"
#: The two refs the command line carries. They were CONFIG constants until R2.
EVIDENCE_COMMIT = "a" * 40
BOUND_AT = "2026-07-30"
#: The WorkSpec the fixtures freeze. Kept as one object because a digest-protected state
#: pointer has to bind the exact bytes `make_run` writes for it, and the fixture computes
#: that digest from its own serialisation rather than asking the template for it (E5).
WORK_SPEC = {"work_id": "w-test"}
WORK_SPEC_DIGEST = bytes_digest(json.dumps(WORK_SPEC).encode("utf-8"))
#: The plan the R10 branch reads so the repair gate has a boundary to measure a spend
#: against. A stand-in with no `effective_change_boundary` would make that gate report the
#: boundary UNVERIFIED, which is the fail-open shape it exists to refuse.
RESOLVED_PLAN = {
    "note": "test resolved plan stand-in",
    "effective_change_boundary": {"write_scope": ["docs"], "out": ["docs/private"]},
}


def evidenced_state(repair_round):
    """A schema-valid EVIDENCED state — the position a bind is entered from.

    Written out by hand rather than built by the harness (E5): a state the module under test
    helped construct would agree with it about anything. Since R2 the ROUND lives here and
    nowhere else, so every fixture that drives ``main()`` owes one of these.
    """
    return {
        "work_id": "w-test",
        "run_id": "tr-nine",
        "status": "EVIDENCED",
        "repair_round": repair_round,
        "work_spec_ref": {"path": f"{CONTROL_ROOT}/control/work-spec.json"},
        "resolved_plan_ref": {"path": f"{CONTROL_ROOT}/control/resolved-plan.json"},
    }


class BindTemplateCase(unittest.TestCase):
    """Shared fixture plumbing: a throwaway repository the template is pointed at by argument."""

    def setUp(self):
        self.template = load_template()

    def make_run(self, *, repair_round, reviews=(), repair=None, control_files=None,
                 evidence_files=None, state=None):
        root = pathlib.Path(tempfile.mkdtemp(prefix="m9-bind-"))
        self.addCleanup(shutil.rmtree, root, ignore_errors=True)
        # A real repository, because the default repo-root derivation asks git for
        # the toplevel (round STRANGER-GUARDS) and this file exercises that default.
        subprocess.run(
            ["git", "-C", str(root), "init", "-q"], check=True, stdout=subprocess.DEVNULL
        )
        control = root / CONTROL_ROOT / "control"
        evidence = root / CONTROL_ROOT / "evidence"
        control.mkdir(parents=True)
        evidence.mkdir(parents=True)
        for name, document in reviews:
            (evidence / name).write_text(json.dumps(document), encoding="utf-8")
        if repair is not None:
            (control / "user-decision-repair.json").write_text(
                json.dumps(repair), encoding="utf-8")
        for name, document in (control_files or {}).items():
            (control / name).write_text(json.dumps(document), encoding="utf-8")
        for name, document in (evidence_files or {}).items():
            (evidence / name).write_text(json.dumps(document), encoding="utf-8")
        (control / "state.json").write_text(
            json.dumps(evidenced_state(repair_round) if state is None else state),
            encoding="utf-8")
        return root

    def argv(self, root, *extra):
        """The command line a run is driven by: the run directory, then the round's refs.

        No ``--repo-root`` is passed anywhere in this file on purpose — the default
        derivation (the git toplevel of the run directory, round STRANGER-GUARDS) is
        itself under test, and supplying the root by hand would let a broken
        derivation pass.
        """
        return [str(root / CONTROL_ROOT), "--evidence-commit", EVIDENCE_COMMIT,
                "--bound-at", BOUND_AT, *extra]

    def saved_state(self, root):
        return json.loads(
            (root / CONTROL_ROOT / "control" / "state.json").read_text(encoding="utf-8"))


class TheRoundDecidesWhichReviewsAreBound(BindTemplateCase):
    """M9: '按 repair_round 读 full/verify' — the file set is a function of the round."""

    def test_round_zero_binds_the_full_alone(self):
        self.assertEqual(self.template.round_documents(0), ["review-full.json"])

    def test_a_repaired_round_binds_the_full_then_the_verify(self):
        self.assertEqual(
            self.template.round_documents(1),
            ["review-full.json", "review-verify.json"],
        )


class EveryRoundThatHappenedIsContentBound(BindTemplateCase):
    """M9: 'review_refs 绑全' — each round's own bytes, and every open blocker, are bound."""

    def test_each_round_that_happened_gets_its_own_bytes_bound(self):
        refs = self.template.review_refs_of(
            ["review-full.json", "review-verify.json"], [FULL_REVIEW, VERIFY_REVIEW],
            CONTROL_ROOT,
        )
        self.assertEqual(
            refs,
            [
                {
                    "path": f"{CONTROL_ROOT}/evidence/review-full.json",
                    "digest_sha256": canonical_digest(FULL_REVIEW),
                },
                {
                    "path": f"{CONTROL_ROOT}/evidence/review-verify.json",
                    "digest_sha256": canonical_digest(VERIFY_REVIEW),
                },
            ],
        )

    def test_a_blocker_from_any_round_is_listed_in_the_unresolved_set(self):
        verify_with_blocker = {"findings": [{"finding_id": "v1", "blocking": True}]}
        self.assertEqual(
            self.template.unresolved_ids([FULL_REVIEW, verify_with_blocker]),
            ["f1", "v1"],
        )

    def test_rounds_with_no_blockers_contribute_nothing(self):
        clean_full = {"findings": [{"finding_id": "x9", "blocking": False}]}
        self.assertEqual(self.template.unresolved_ids([clean_full, {"findings": []}]), [])


class TheBindRefusesAnIncompleteReviewSet(BindTemplateCase):
    """A round whose review files are not all on disk is refused before anything is read.

    The refusal fixtures deliberately create no control/ document but the state: a main()
    that consulted the WorkSpec or the candidate record before the review set would crash
    there instead of returning 1, and the assertion below fails on that VALUE (None != 1).
    The state is the one exception because the ROUND is read from it, and the round is what
    decides which files this refusal is about — reading it is the refusal's precondition.
    """

    def test_a_repaired_round_with_no_verify_on_disk_is_refused(self):
        root = self.make_run(repair_round=1, reviews=[("review-full.json", FULL_REVIEW)])
        code, out = run_main(self.template, self.argv(root))
        self.assertEqual(code, 1)
        self.assertIn(
            "STOP: repair round 1 binds review-full.json, review-verify.json; "
            "missing from evidence/: review-verify.json",
            out.splitlines(),
        )

    def test_round_zero_with_no_full_on_disk_is_refused(self):
        root = self.make_run(repair_round=0, reviews=[])
        code, out = run_main(self.template, self.argv(root))
        self.assertEqual(code, 1)
        self.assertIn(
            "STOP: repair round 0 binds review-full.json; "
            "missing from evidence/: review-full.json",
            out.splitlines(),
        )

    def test_a_complete_review_set_does_not_trip_the_refusal(self):
        """Negative control (E4): with every round's file present the refusal stays quiet."""
        root = self.make_run(
            repair_round=1,
            reviews=[("review-full.json", FULL_REVIEW),
                     ("review-verify.json", VERIFY_REVIEW)],
        )
        code, out = run_main(self.template, self.argv(root))
        # It walks INTO the next gate and is stopped there: the result checker runs for real
        # here, and the fixture names an evidence commit no repository holds. Asserting that
        # line rather than the exit code is what keeps this a negative control -- the refusal
        # under test returns 1 too, so `code == 1` alone would be satisfied by the guard
        # firing, which is the opposite of what this method claims.
        self.assertIn("check_review_result_v2 : ISSUES", out.splitlines())
        self.assertNotIn("STOP: repair round", out)


class TheRoundComesFromTheStateNotTheCommandLine(BindTemplateCase):
    """R2 (`HD-11`): the round the bind acts on is the one the flow advanced, not a knob.

    The pre-R2 shape carried `REPAIR_ROUND` as an editable module constant that had to be
    kept in step with the evidence step's own copy by hand — two places for one fact, and
    the file set, the outcome gate, the state pointer and the candidate's `review_refs` all
    hang off it. These pin that the state file is now the single place it lives: the same
    command line yields a round-0 file set or a round-1 one according to the state alone.
    """

    def test_a_state_at_round_one_makes_the_bind_ask_for_the_verify(self):
        root = self.make_run(repair_round=1, reviews=[("review-full.json", FULL_REVIEW)])
        code, out = run_main(self.template, self.argv(root))
        self.assertEqual(code, 1)
        self.assertIn(
            "STOP: repair round 1 binds review-full.json, review-verify.json; "
            "missing from evidence/: review-verify.json",
            out.splitlines(),
        )

    def test_the_same_command_line_at_round_zero_asks_for_the_full_alone(self):
        root = self.make_run(repair_round=0, reviews=[])
        code, out = run_main(self.template, self.argv(root))
        self.assertEqual(code, 1)
        self.assertIn(
            "STOP: repair round 0 binds review-full.json; "
            "missing from evidence/: review-full.json",
            out.splitlines(),
        )


class TheOperativeReviewIsTheRoundsOwn(BindTemplateCase):
    """After a repair the VERIFY answers; at round zero the FULL does. The gates see it."""

    def test_after_a_repair_the_verify_is_what_the_checker_receives(self):
        root = self.make_run(
            repair_round=1,
            reviews=[("review-full.json", FULL_REVIEW),
                     ("review-verify.json", VERIFY_REVIEW)],
            repair=REPAIR_DECISION,
        )
        recorder = RecordingResultChecker(failing_report())
        self.template.RV = recorder
        code, _ = run_main(self.template, self.argv(root))
        self.assertEqual(code, 1)
        self.assertEqual(recorder.received, VERIFY_REVIEW)

    def test_at_round_zero_the_full_is_what_the_checker_receives(self):
        """Negative control: the branch must not steal round zero's own review."""
        root = self.make_run(repair_round=0, reviews=[("review-full.json", FULL_REVIEW)])
        recorder = RecordingResultChecker(failing_report())
        self.template.RV = recorder
        code, _ = run_main(self.template, self.argv(root))
        self.assertEqual(code, 1)
        self.assertEqual(recorder.received, FULL_REVIEW)

    def test_the_verify_outcome_gate_receives_the_verify_and_the_users_decision(self):
        root = self.make_run(
            repair_round=1,
            reviews=[("review-full.json", FULL_REVIEW),
                     ("review-verify.json", VERIFY_REVIEW)],
            repair=REPAIR_DECISION,
        )
        self.template.RV = RecordingResultChecker(clean_report())
        gate = RecordingOutcomeGate(failing_report())
        self.template.flow = gate
        code, _ = run_main(self.template, self.argv(root))
        self.assertEqual(code, 1)
        self.assertEqual(gate.received, (VERIFY_REVIEW, REPAIR_DECISION))

    def test_round_zero_never_asks_for_a_repair_decision(self):
        """Negative control: no repair happened, so no repair decision is demanded.

        The round-0 fixture here is the clean full WITHOUT lows, deliberately, and for the
        reason this docstring already gave once: a `CHANGES_REQUIRED` round 0 returns before
        the outcome gate is reachable, and since round `PROMISE-PATH-ENGINE` so does a clean
        round 0 carrying a low. Either would satisfy the assertion by construction and leave
        it proving nothing.
        """
        root = self.make_run(repair_round=0, reviews=[("review-full.json", CLEAN_FULL_NO_LOWS)])
        self.template.RV = RecordingResultChecker(clean_report())
        gate = RecordingOutcomeGate(failing_report())
        self.template.flow = gate
        code, _ = run_main(self.template, self.argv(root))
        self.assertIsNone(code)  # proceeds past the gates and dies on the absent control docs
        self.assertIsNone(gate.received)


class ARoundZeroBlockerBindsNoCandidate(BindTemplateCase):
    """The round-0 VERDICT decides whether an AssuranceCandidate is built at all.

    issue-p5b-claims-bind-round0-no-blocked-branch (routed WORKFLOW_FIX 2026-08-07). The
    template's round-0 emit bound a candidate and advanced to AWAITING_FINAL
    unconditionally — the clean-review path only. The flow leaves AWAITING_FINAL for CLOSED
    alone, so doing that to a run the user has chosen to repair strands it with REPAIRING
    unreachable. p3-corr's hand-written round-0 bind stopped at REVIEWED for this reason;
    merging the candidate binding into the same step lost the branch.

    The defect CLASS (E7) is *a state transition taken without consulting the verdict that
    licenses it*, so both directions are pinned: a blocking round 0 must stop, and a clean
    one must not be stopped.

    Every fixture leaves `control/` empty but for the state on purpose. Reaching the
    candidate assembly would crash on the absent WorkSpec, so a clean 0 is proof the branch
    returned BEFORE the assembly rather than proof the assembly succeeded, and the failure
    mode stays a VALUE mismatch (C0 F2 / R8).
    """

    def test_a_round_zero_changes_required_stops_before_the_candidate(self):
        root = self.make_run(repair_round=0, reviews=[("review-full.json", FULL_REVIEW)])
        self.template.RV = RecordingResultChecker(clean_report())
        code, out = run_main(self.template, self.argv(root))
        self.assertEqual(code, 0)
        self.assertIn(
            "verdict                : CHANGES_REQUIRED — no AssuranceCandidate is bound at "
            "round 0",
            out.splitlines(),
        )

    def test_a_clean_round_zero_is_not_stopped(self):  # negative control
        # The lows-free clean FULL: this class's property is the VERDICT branch, and a
        # fixture that the R10 branch stops would pass here for the wrong reason.
        root = self.make_run(repair_round=0, reviews=[("review-full.json", CLEAN_FULL_NO_LOWS)])
        self.template.RV = RecordingResultChecker(clean_report())
        code, _ = run_main(self.template, self.argv(root))
        self.assertIsNone(code)  # walks on to the assembly and dies on the absent control docs

    def test_a_repaired_round_is_not_stopped_by_a_round_zero_blocker(self):  # negative control
        # The FULL that asked for the repair is still CHANGES_REQUIRED and is still bound;
        # the branch must key on round 0, not on "some bound review found a blocker".
        root = self.make_run(
            repair_round=1,
            reviews=[("review-full.json", FULL_REVIEW),
                     ("review-verify.json", VERIFY_REVIEW)],
            repair=REPAIR_DECISION,
        )
        self.template.RV = RecordingResultChecker(clean_report())
        self.template.flow = RecordingOutcomeGate(clean_report())
        code, _ = run_main(self.template, self.argv(root))
        self.assertIsNone(code)  # walks on to the assembly and dies on the absent control docs


class TheBlockedRoundPrintsTheInstructionItStores(BindTemplateCase):
    """Rider `sg-print`: the stdout sentence IS `next_action`, not a paraphrase of it.

    v3-review-verify-3b28116 V-1. `next_action` had been branched by verdict (FULL f4e1be1
    O-2) and the print beside it had not, so a round-0 SPEC_GAP was told on stdout that it
    "owes a repair decision" — the one sentence EXECUTION.md says a SPEC_GAP does *not* owe.
    Without `--emit` that print is the only output there is, and with it the two channels
    contradicted each other. The prescribed redemption was to DELETE the paraphrase rather
    than branch it a second time: two rewrites of one fact diverge silently, where a copy
    diverges visibly, so the property's landing points drop from three to two.

    Both verdicts are pinned against the SAME printed line, which is what makes this a test
    of "the field is printed" rather than of "some branch prints the right words".
    """

    def emit(self, review):
        root = self.make_run(repair_round=0, reviews=[("review-full.json", review)])
        self.template.RV = RecordingResultChecker(clean_report())
        code, out = run_main(self.template, self.argv(root, "--emit"))
        return code, out, self.saved_state(root)

    def test_a_changes_required_prints_the_repair_sentence_it_stores(self):
        code, out, saved = self.emit(FULL_REVIEW)
        self.assertEqual(code, 0)
        expected = (
            "user REPAIR decision (APPLY_ACCEPTED_FINDINGS / NO_REPAIR) naming the accepted "
            "finding ids and the repair boundary"
        )
        self.assertEqual(saved["next_action"], expected)
        self.assertIn(f"next action            : {expected}", out.splitlines())

    def test_a_spec_gap_prints_the_spec_gap_sentence_it_stores(self):
        code, out, saved = self.emit({**FULL_REVIEW, "verdict": "SPEC_GAP"})
        self.assertEqual(code, 0)
        expected = (
            "user decision on the SPEC_GAP: the specification is what failed, so a new "
            "WorkSpec revision and a new START decision are owed, not a bounded repair"
        )
        self.assertEqual(saved["next_action"], expected)
        self.assertIn(f"next action            : {expected}", out.splitlines())

    def test_no_verdict_is_told_it_owes_a_repair_decision_in_the_verdict_line(self):
        """The deleted paraphrase, pinned by its absence — the reported defect's own words."""
        for verdict in ("CHANGES_REQUIRED", "SPEC_GAP"):
            with self.subTest(verdict=verdict):
                _, out, _ = self.emit({**FULL_REVIEW, "verdict": verdict})
                verdict_lines = [
                    line for line in out.splitlines() if line.startswith("verdict ")
                ]
                self.assertEqual(
                    verdict_lines,
                    [f"verdict                : {verdict} — no AssuranceCandidate is bound "
                     "at round 0"],
                )

    def test_a_dry_run_still_prints_the_instruction(self):
        """Without --emit the printed line is the ONLY channel — the V-1 half that bit."""
        root = self.make_run(repair_round=0, reviews=[("review-full.json", FULL_REVIEW)])
        self.template.RV = RecordingResultChecker(clean_report())
        code, out = run_main(self.template, self.argv(root))
        self.assertEqual(code, 0)
        self.assertIn(
            "next action            : user REPAIR decision (APPLY_ACCEPTED_FINDINGS / "
            "NO_REPAIR) naming the accepted finding ids and the repair boundary",
            out.splitlines(),
        )
        self.assertEqual(self.saved_state(root)["status"], "EVIDENCED")


class TheBlockedRoundLandsOnReviewed(BindTemplateCase):
    """What the branch WRITES, not only what it declines to write (FULL f4e1be1 L-1).

    The class above pins the early return and the printed line — the half that stops an
    AssuranceCandidate being bound. The reported harm is the other half: the issue says
    binding a candidate at AWAITING_FINAL *strands* a run with REPAIRING unreachable, which
    is a claim about the STATUS the run lands on. Until this class nothing drove the
    ``--emit`` path in this file at all, so swapping REVIEWED for AWAITING_FINAL left the
    whole suite green and would have reintroduced exactly the reported defect (measured:
    that mutation was the L-1 finding's own evidence).

    Both halves of what emit writes are asserted, because the sentence is the executor's
    only instruction at that moment and the two non-clean verdicts do not owe the same act.
    """

    def emit(self, review):
        root = self.make_run(repair_round=0, reviews=[("review-full.json", review)])
        self.template.RV = RecordingResultChecker(clean_report())
        code, out = run_main(self.template, self.argv(root, "--emit"))
        return code, out, self.saved_state(root)

    def test_a_blocking_round_zero_is_saved_as_reviewed(self):
        code, _, saved = self.emit(FULL_REVIEW)
        self.assertEqual(code, 0)
        self.assertEqual(saved["status"], "REVIEWED")
        self.assertEqual(saved["repair_round"], 0)
        self.assertEqual(
            saved["next_action"],
            "user REPAIR decision (APPLY_ACCEPTED_FINDINGS / NO_REPAIR) naming the accepted "
            "finding ids and the repair boundary",
        )
        # No AssuranceCandidate pointer is written: the status is only half the claim.
        self.assertNotIn("assurance_candidate_ref", saved)

    def test_a_spec_gap_is_not_told_to_author_a_repair_decision(self):
        # FULL f4e1be1 O-2: the branch was verdict-shaped but not verdict-discriminating, so
        # a SPEC_GAP inherited the repair sentence while EXECUTION.md says a SPEC_GAP stops
        # and owes a new WorkSpec revision plus a new START decision.
        code, _, saved = self.emit({**FULL_REVIEW, "verdict": "SPEC_GAP"})
        self.assertEqual(code, 0)
        self.assertEqual(saved["status"], "REVIEWED")
        self.assertEqual(
            saved["next_action"],
            "user decision on the SPEC_GAP: the specification is what failed, so a new "
            "WorkSpec revision and a new START decision are owed, not a bounded repair",
        )

    def test_a_clean_round_zero_writes_no_reviewed_state_here(self):  # negative control
        # It walks past the branch into the assembly and dies on the absent WorkSpec, so the
        # state it was seeded with is still on disk untouched. Lows-free for the same reason
        # as the class above: the R10 branch would stop a clean FULL that carried one.
        root = self.make_run(repair_round=0, reviews=[("review-full.json", CLEAN_FULL_NO_LOWS)])
        self.template.RV = RecordingResultChecker(clean_report())
        code, _ = run_main(self.template, self.argv(root, "--emit"))
        self.assertIsNone(code)
        self.assertEqual(self.saved_state(root)["status"], "EVIDENCED")


class TheAuthoredDigestIsNeverDiscarded(BindTemplateCase):
    """FULL 71d43be F-1: a pointer's authored digest is bound, and a contradiction refuses.

    The digest a state pointer carries was written by ``pointer_for`` on a
    digest-protected field — a binding the executor is not entitled to re-derive. The
    pre-fix shape recomputed every field's digest over disk bytes, which silently
    replaced that binding; the property under test is "an authored digest is copied, a
    digestless pointer is computed from the bytes in hand, and a pointer whose digest the
    bytes in hand contradict refuses the assembly" (both sides are present at the call,
    the one moment they can be reconciled without I/O — the M7 shape).
    """

    def digest_fixture(self):
        root = self.make_run(repair_round=0, reviews=[("review-full.json", FULL_REVIEW)],
                             control_files={"work-spec.json": WORK_SPEC})
        return root, f"{CONTROL_ROOT}/control/work-spec.json"

    def test_a_pointer_digest_contradicted_by_disk_refuses_the_assembly(self):
        root, path = self.digest_fixture()
        with self.assertRaises(AssuranceFault) as caught:
            self.template.digest_ref_of({"path": path, "digest_sha256": "0" * 64}, root)
        self.assertIn("changed after it was authored", str(caught.exception))

    def test_a_matching_authored_digest_is_the_one_bound(self):
        root, path = self.digest_fixture()
        self.assertEqual(
            self.template.digest_ref_of(
                {"path": path, "digest_sha256": WORK_SPEC_DIGEST}, root),
            {"path": path, "digest_sha256": WORK_SPEC_DIGEST},
        )

    def test_a_digestless_pointer_still_gets_the_bytes_in_hand(self):
        """Negative control: the five rewritable fields keep the compute-from-disk rule."""
        root, path = self.digest_fixture()
        self.assertEqual(
            self.template.digest_ref_of({"path": path}, root),
            {"path": path, "digest_sha256": WORK_SPEC_DIGEST},
        )


class TheAssembledCandidatePassesTheRealFaithfulnessGate(BindTemplateCase):
    """End to end minus git: the template's own assembly satisfies check_assurance_candidate.

    The result checker is a stub (its real form needs a repository behind the evidence
    commit) but the verify-outcome gate, the assembly and the faithfulness gate are the
    real ones — so a template that bound one review where two happened, dropped the FULL's
    open blocker, or wrote a count instead of content digests fails HERE, on the same
    N2-A9 codes a real run would meet (C2's REVIEW-UNBOUND / BLOCKER-DROPPED guards).
    """

    def test_a_repaired_runs_candidate_passes_the_real_faithfulness_gate(self):
        record = {
            "run_id": "tr-nine",
            "candidate_ref": {"branch": "run/tr-nine", "commit": "c" * 40},
            "base_revision": "d" * 40,
            "repair_round": 1,
        }
        state = {
            "work_id": "w-test",
            "run_id": "tr-nine",
            "status": "EVIDENCED",
            "repair_round": 1,
            "work_spec_ref": {
                "path": f"{CONTROL_ROOT}/control/work-spec.json",
                # O-2 (FULL 71d43be): a real state carries the authored digest on this
                # digest-protected field, so the fixture does too — the copy path runs.
                "digest_sha256": WORK_SPEC_DIGEST,
            },
            "resolved_plan_ref": {"path": f"{CONTROL_ROOT}/control/resolved-plan.json"},
            "instruction_audit_ref": {
                "path": f"{CONTROL_ROOT}/control/instruction-audit.json"},
            "fulfillment_ref": {"path": f"{CONTROL_ROOT}/evidence/candidate-record.json"},
            "manifest_ref": {"path": f"{CONTROL_ROOT}/evidence/candidate-record.json"},
            "coverage_ref": {"path": f"{CONTROL_ROOT}/evidence/coverage.json"},
        }
        root = self.make_run(
            repair_round=1,
            reviews=[("review-full.json", FULL_REVIEW),
                     ("review-verify.json", VERIFY_REVIEW)],
            repair=REPAIR_DECISION,
            control_files={
                "work-spec.json": WORK_SPEC,
                "resolved-plan.json": {"note": "test resolved plan stand-in"},
                "instruction-audit.json": {"note": "test audit stand-in"},
                "bind-declarations.json": {
                    "governance_scan": {
                        "included": False,
                        "skip_reason": "no governance document in this test fixture payload",
                    },
                    "disclosures": [],
                },
            },
            evidence_files={
                "candidate-record.json": record,
                "check-results.json": [],
                "coverage.json": {"rows": []},
            },
            state=state,
        )
        self.template.RV = RecordingResultChecker(clean_report())
        code, out = run_main(self.template, self.argv(root))
        self.assertEqual(code, 0, out)
        self.assertIn("check_assurance_cand.  : clean", out.splitlines())


#: The per-run declarations the bind step may not derive. A run's own copy is authored by a
#: person; this is the fixture's, written out here so the two keys the template refuses
#: without are visible at the point they are supplied.
BIND_DECLARATIONS = {
    "governance_scan": {
        "included": False,
        "skip_reason": "no governance document in this test fixture payload",
    },
    "disclosures": [],
}
#: The clean round-0 evidence layer, hand-written. Every path below is the real control-root
#: shape because the emitted candidate binds paths, and a flat fixture would bind paths no
#: run could have.
CLEAN_RECORD = {
    "run_id": "tr-nine",
    "candidate_ref": {"branch": "run/tr-nine", "commit": "c" * 40},
    "base_revision": "d" * 40,
    "repair_round": 0,
}
CHECK_RESULT = {"check_id": "chk-one", "result": "PASS"}


def clean_round_zero_state():
    """The EVIDENCED state a clean round-0 bind is entered from — every pointer resolved.

    Hand-written (E5). `work_spec_ref` carries a digest because it is the one
    digest-protected field the assembly reads; the other five carry the path alone, which
    is exactly what `pointer_for` writes for them (the 2026-07-29 narrowing).
    """
    return {
        "work_id": "w-test",
        "run_id": "tr-nine",
        "status": "EVIDENCED",
        "repair_round": 0,
        "work_spec_ref": {
            "path": f"{CONTROL_ROOT}/control/work-spec.json",
            "digest_sha256": WORK_SPEC_DIGEST,
        },
        "resolved_plan_ref": {"path": f"{CONTROL_ROOT}/control/resolved-plan.json"},
        "instruction_audit_ref": {"path": f"{CONTROL_ROOT}/control/instruction-audit.json"},
        "fulfillment_ref": {"path": f"{CONTROL_ROOT}/evidence/candidate-record.json"},
        "manifest_ref": {"path": f"{CONTROL_ROOT}/evidence/candidate-record.json"},
        "coverage_ref": {"path": f"{CONTROL_ROOT}/evidence/coverage.json"},
    }


class TheCleanRoundEmitsTheCandidateItPrinted(BindTemplateCase):
    """Rider `bind-emit2`: the OTHER `--emit` block — the one that writes the candidate.

    v3-review-verify-3b28116 V-2. The template has exactly two `--emit` blocks; the class
    above closed the blocked one and left this one dead to the suite, so the reviewer's
    three mutations — wrong terminal state, no `assurance_candidate_ref` written, the
    candidate file never landing on disk at all — each left the whole battery green. The
    banked redemption criterion was COVERING BOTH BLOCKS with one helper rather than
    bolting a test onto this one, because `E7` names the defect CLASS: *a state transition
    taken without the verdict that licenses it*. `clean_round_zero` below is that helper —
    the same fixture shape the blocked class uses, plus the control plane a clean verdict
    needs to reach the assembly.

    Everything from `check_assurance_candidate` inward is REAL here (only the result checker
    stays a stand-in, because its real form needs a repository behind the evidence commit),
    so the fixture has to satisfy the actual N2-A7/A9 reconciliation, and the mutations below
    prove it is engaged rather than merely present.
    """

    def clean_round_zero(self, *, full=CLEAN_FULL_REVIEW, record=None, state=None,
                         repair=NO_REPAIR_DECISION):
        # The fixture carries the user's NO_REPAIR since round `PROMISE-PATH-ENGINE`: the
        # clean FULL it uses carries a low, so `R10` makes the candidate a separate act that
        # only the recorded choice not to spend the leg reaches. Every property this class
        # asserts is about what the candidate act WRITES, so the decision is fixture, not
        # subject -- `TheLowsDecisionIsPutBeforeTheCandidateIsBound` below is its subject.
        root = self.make_run(
            repair_round=0,
            reviews=[("review-full.json", full)],
            repair=repair,
            control_files={
                "work-spec.json": WORK_SPEC,
                "resolved-plan.json": RESOLVED_PLAN,
                "instruction-audit.json": {"note": "test audit stand-in"},
                "bind-declarations.json": BIND_DECLARATIONS,
            },
            evidence_files={
                "candidate-record.json": CLEAN_RECORD if record is None else record,
                "check-results.json": [CHECK_RESULT],
                "check-chk-one.json": CHECK_RESULT,
                "coverage.json": {"rows": []},
            },
            state=clean_round_zero_state() if state is None else state,
        )
        self.template.RV = RecordingResultChecker(clean_report())
        return root

    def emitted_candidate(self, root):
        return json.loads(
            (root / CONTROL_ROOT / "control" / "assurance-candidate.json")
            .read_text(encoding="utf-8"))

    def printed_digest(self, out):
        printed = [line for line in out.splitlines() if line.startswith("candidate digest")]
        self.assertEqual(len(printed), 1, out)
        return printed[0].split(": ", 1)[1]

    # --- (i) the dry run writes nothing -------------------------------------------------

    def test_without_emit_the_candidate_is_assembled_and_nothing_is_written(self):
        root = self.clean_round_zero()
        code, out = run_main(self.template, self.argv(root))
        self.assertEqual(code, 0, out)
        self.assertIn("check_assurance_cand.  : clean", out.splitlines())
        self.assertFalse(
            (root / CONTROL_ROOT / "control" / "assurance-candidate.json").exists())
        saved = self.saved_state(root)
        self.assertEqual(saved["status"], "EVIDENCED")
        self.assertNotIn("assurance_candidate_ref", saved)

    # --- (ii) --emit lands on AWAITING_FINAL, pointing at the bytes it printed -----------

    def test_emit_lands_on_awaiting_final_carrying_the_candidate_pointer(self):
        root = self.clean_round_zero()
        code, out = run_main(self.template, self.argv(root, "--emit"))
        self.assertEqual(code, 0, out)
        saved = self.saved_state(root)
        self.assertEqual(saved["status"], "AWAITING_FINAL")
        # `.get`, not `[...]`: an unwritten pointer must fail on the VALUE (None != the ref)
        # rather than raise, which would prove the test reached the code and nothing more
        # (C0 F2 / R8) — and "the pointer is not written" is one of the three mutations this
        # class exists to catch.
        self.assertEqual(
            saved.get("assurance_candidate_ref"),
            {"path": f"{CONTROL_ROOT}/control/assurance-candidate.json"},
        )
        # The run passed THROUGH REVIEWED on the way, binding the round's own review by
        # bytes — `review_ref` is one of the five digest-protected fields.
        self.assertEqual(
            saved.get("review_ref"),
            {
                "path": f"{CONTROL_ROOT}/evidence/review-full.json",
                "digest_sha256": bytes_digest(
                    json.dumps(CLEAN_FULL_REVIEW).encode("utf-8")),
            },
        )

    def test_the_file_on_disk_is_the_candidate_whose_digest_was_printed(self):
        root = self.clean_round_zero()
        code, out = run_main(self.template, self.argv(root, "--emit"))
        self.assertEqual(code, 0, out)
        self.assertEqual(
            canonical_digest(self.emitted_candidate(root)), self.printed_digest(out))

    def test_the_emitted_candidate_binds_this_runs_evidence_and_nothing_else(self):
        """The whole document, hand-written — a mutation anywhere in the assembly fails here."""
        root = self.clean_round_zero()
        code, out = run_main(self.template, self.argv(root, "--emit"))
        self.assertEqual(code, 0, out)
        self.assertEqual(
            self.emitted_candidate(root),
            {
                "assurance_candidate_id": "ac-tr-nine",
                "work_id": "w-test",
                "run_id": "tr-nine",
                "repair_round": 0,
                "candidate_ref": {"branch": "run/tr-nine", "commit": "c" * 40},
                "base_revision": "d" * 40,
                "bound_at": BOUND_AT,
                "bound_by": "tr-nine controller (rsclib deterministic)",
                "work_spec_ref": {
                    "path": f"{CONTROL_ROOT}/control/work-spec.json",
                    "digest_sha256": WORK_SPEC_DIGEST,
                },
                "resolved_plan_ref": {
                    "path": f"{CONTROL_ROOT}/control/resolved-plan.json",
                    "digest_sha256": bytes_digest(
                        json.dumps(RESOLVED_PLAN).encode("utf-8")),
                },
                "instruction_audit_ref": {
                    "path": f"{CONTROL_ROOT}/control/instruction-audit.json",
                    "digest_sha256": bytes_digest(
                        json.dumps({"note": "test audit stand-in"}).encode("utf-8")),
                },
                "fulfillment_ref": {
                    "path": f"{CONTROL_ROOT}/evidence/candidate-record.json",
                    "digest_sha256": bytes_digest(
                        json.dumps(CLEAN_RECORD).encode("utf-8")),
                },
                "manifest_ref": {
                    "path": f"{CONTROL_ROOT}/evidence/candidate-record.json",
                    "digest_sha256": bytes_digest(
                        json.dumps(CLEAN_RECORD).encode("utf-8")),
                },
                "coverage_ref": {
                    "path": f"{CONTROL_ROOT}/evidence/coverage.json",
                    "digest_sha256": bytes_digest(
                        json.dumps({"rows": []}).encode("utf-8")),
                },
                "review_refs": [
                    {
                        "path": f"{CONTROL_ROOT}/evidence/review-full.json",
                        "digest_sha256": canonical_digest(CLEAN_FULL_REVIEW),
                    }
                ],
                "governance_scan": {
                    "included": False,
                    "skip_reason": "no governance document in this test fixture payload",
                },
                "check_result_refs": [
                    {
                        "path": f"{CONTROL_ROOT}/evidence/check-chk-one.json",
                        "digest_sha256": bytes_digest(
                            json.dumps(CHECK_RESULT).encode("utf-8")),
                    }
                ],
            },
        )

    # --- (iii) the mutations that prove the gate is engaged, not merely present ----------

    def test_a_tampered_digest_protected_pointer_emits_nothing(self):
        """Mutation: the state's `work_spec_ref` digest no longer matches its own bytes.

        The authored digest is the one binding in hand that the executor may not re-derive,
        so a contradiction has to stop the assembly BEFORE any transition — which is the
        `bind-emit2` defect class stated for this block.
        """
        tampered = clean_round_zero_state()
        tampered["work_spec_ref"] = {
            "path": f"{CONTROL_ROOT}/control/work-spec.json",
            "digest_sha256": "0" * 64,
        }
        root = self.clean_round_zero(state=tampered)
        code, _ = run_main(self.template, self.argv(root, "--emit"))
        self.assertIsNone(code)  # AssuranceFault: refused, not reported
        self.assertFalse(
            (root / CONTROL_ROOT / "control" / "assurance-candidate.json").exists())
        self.assertEqual(self.saved_state(root)["status"], "EVIDENCED")

    def test_a_record_from_another_round_emits_nothing(self):
        """Mutation: the CandidateRecord says round 1 where the state and the bind say 0.

        The real `check_assurance_candidate` owns this (`-ROUND-MISMATCH`); the point of the
        assertion is that its verdict gates the WRITE, not merely the printed line.
        """
        root = self.clean_round_zero(record={**CLEAN_RECORD, "repair_round": 1})
        code, out = run_main(self.template, self.argv(root, "--emit"))
        self.assertEqual(code, 1)
        self.assertIn("check_assurance_cand.  : ISSUES", out.splitlines())
        self.assertFalse(
            (root / CONTROL_ROOT / "control" / "assurance-candidate.json").exists())
        self.assertEqual(self.saved_state(root)["status"], "EVIDENCED")

    def test_a_blocker_in_the_bound_review_reaches_the_emitted_candidate(self):
        """Mutation: the clean FULL carries a blocking finding after all.

        Dropping it would be the controller weakening the reviewer's claim, and N2-A9 reports
        exactly that (`-BLOCKER-DROPPED`) — so the visible consequence of the mutation is that
        the emitted document names the blocker, and a template that summarised instead of
        deriving could not both pass the gate and land this value.
        """
        root = self.clean_round_zero(
            full={**CLEAN_FULL_REVIEW, "findings": [BLOCKER_F1, LOW_F2]},
        )
        code, out = run_main(self.template, self.argv(root, "--emit"))
        self.assertEqual(code, 0, out)
        self.assertEqual(self.emitted_candidate(root)["unresolved_finding_ids"], ["f1"])


class TheLowsDecisionIsPutBeforeTheCandidateIsBound(BindTemplateCase):
    """`R10`: a clean FULL with lows is a decision point, and the candidate is a second act.

    Item 3 of batch `PROMISE-PATH`. `RULES.md` `R10` says a FULL returning
    `REVIEWED_NO_BLOCKER` with lows does not bank them by default -- the spend-the-fix-leg /
    bank choice is put to the user. The engine gave that choice no moment to be put: this
    step advanced REVIEWED, wrote the candidate and advanced AWAITING_FINAL in one act, and
    `flow._SUCCESSORS` leaves AWAITING_FINAL exactly one successor, so a user who then chose
    to repair had REPAIRING unreachable from where the run stood. The caller's run
    p5c-firewall-r2 stopped there and cost a successor run.

    The defect CLASS is the same one `ARoundZeroBlockerBindsNoCandidate` names -- a state
    transition taken without consulting what licenses it -- with a different licence: there
    the verdict, here the user's decision. All four positions are pinned, each against the
    thing that distinguishes it from the next: no decision on disk (stop), APPLY (stop, and
    a DIFFERENT next act), NO_REPAIR (the candidate act runs), and no lows at all (nothing to
    decide, so no stop). The negative controls are the last two: a guard that always stopped
    would fail them.
    """

    def lows_round_zero(self, *, repair=None, full=CLEAN_FULL_REVIEW):
        root = self.make_run(
            repair_round=0,
            reviews=[("review-full.json", full)],
            repair=repair,
            control_files={
                "work-spec.json": WORK_SPEC,
                "resolved-plan.json": RESOLVED_PLAN,
                "instruction-audit.json": {"note": "test audit stand-in"},
                "bind-declarations.json": BIND_DECLARATIONS,
            },
            evidence_files={
                "candidate-record.json": CLEAN_RECORD,
                "check-results.json": [CHECK_RESULT],
                "check-chk-one.json": CHECK_RESULT,
                "coverage.json": {"rows": []},
            },
            state=clean_round_zero_state(),
        )
        self.template.RV = RecordingResultChecker(clean_report())
        return root

    #: The stored-and-printed instruction, written out here and never imported (E5).
    R10_ACTION = (
        "user REPAIR decision on the non-blocking findings (f2): APPLY_ACCEPTED_FINDINGS "
        "spends this round's one repair leg on them and NO_REPAIR banks them; the "
        "AssuranceCandidate is bound only after that decision is on disk"
    )
    SPEND_ACTION = (
        "user chose to spend the repair leg on the non-blocking findings; the next act is "
        "run_repair.py, which gates the decision and enters REPAIRING"
    )

    # --- (i) no decision on disk: the run stops and says what is owed -------------------

    def test_a_clean_full_with_lows_stops_at_reviewed_and_binds_no_candidate(self):
        root = self.lows_round_zero()
        code, out = run_main(self.template, self.argv(root, "--emit"))
        self.assertEqual(code, 0, out)
        self.assertIn(
            "verdict                : REVIEWED_NO_BLOCKER with 1 non-blocking finding(s): f2",
            out.splitlines(),
        )
        saved = self.saved_state(root)
        self.assertEqual(saved["status"], "REVIEWED")
        self.assertEqual(saved["next_action"], self.R10_ACTION)
        self.assertNotIn("assurance_candidate_ref", saved)
        self.assertFalse(
            (root / CONTROL_ROOT / "control" / "assurance-candidate.json").exists())

    def test_the_stored_instruction_is_the_one_printed(self):
        """Rider `sg-print`: without --emit the printed line is the only channel."""
        root = self.lows_round_zero()
        code, out = run_main(self.template, self.argv(root))
        self.assertEqual(code, 0, out)
        self.assertIn(f"next action            : {self.R10_ACTION}", out.splitlines())
        self.assertEqual(self.saved_state(root)["status"], "EVIDENCED")

    # --- (ii) the user spends the leg: still no candidate, and a different next act ----

    def test_an_apply_decision_stops_too_and_names_the_repair_step(self):
        root = self.lows_round_zero(repair=APPLY_LOWS_DECISION)
        code, out = run_main(self.template, self.argv(root, "--emit"))
        self.assertEqual(code, 0, out)
        self.assertIn(
            "lows decision          : APPLY_ACCEPTED_FINDINGS — the leg is spent",
            out.splitlines(),
        )
        saved = self.saved_state(root)
        self.assertEqual(saved["status"], "REVIEWED")
        self.assertEqual(saved["next_action"], self.SPEND_ACTION)
        self.assertFalse(
            (root / CONTROL_ROOT / "control" / "assurance-candidate.json").exists())

    def test_a_decision_about_another_run_is_refused_rather_than_acted_on(self):
        """Defect M5's shape: a decline that binds something else closes nothing here.

        This bind is the only step a NO_REPAIR ever reaches -- `run_repair.py` exists for
        the APPLY path -- so an ungated read here would advance the run to AWAITING_FINAL on
        a decision the user made about another run.
        """
        root = self.lows_round_zero(
            repair={**NO_REPAIR_DECISION, "run_id": "another-run"})
        code, out = run_main(self.template, self.argv(root, "--emit"))
        self.assertEqual(code, 1)
        self.assertIn("check_repair_decision  : ISSUES", out.splitlines())
        self.assertEqual(self.saved_state(root)["status"], "EVIDENCED")
        self.assertFalse(
            (root / CONTROL_ROOT / "control" / "assurance-candidate.json").exists())

    # --- (iii) negative controls: the two positions that must NOT stop ------------------

    def test_a_recorded_no_repair_lets_the_candidate_act_run(self):
        root = self.lows_round_zero(repair=NO_REPAIR_DECISION)
        code, out = run_main(self.template, self.argv(root, "--emit"))
        self.assertEqual(code, 0, out)
        self.assertIn(
            "lows decision          : NO_REPAIR — the user banked the low(s); this "
            "bind binds the AssuranceCandidate",
            out.splitlines(),
        )
        saved = self.saved_state(root)
        self.assertEqual(saved["status"], "AWAITING_FINAL")
        self.assertEqual(
            saved.get("assurance_candidate_ref"),
            {"path": f"{CONTROL_ROOT}/control/assurance-candidate.json"},
        )
        # Negative control for the no-op below: a run that reaches the candidate act in ONE
        # pass advances REVIEWED itself and must not report the resumed position.
        self.assertNotIn("state                  : already REVIEWED", out)

    def test_a_clean_full_with_no_lows_never_reaches_the_decision_point(self):
        root = self.lows_round_zero(full=CLEAN_FULL_NO_LOWS)
        code, out = run_main(self.template, self.argv(root, "--emit"))
        self.assertEqual(code, 0, out)
        self.assertEqual(
            [line for line in out.splitlines() if line.startswith("verdict ")], [])
        self.assertEqual(self.saved_state(root)["status"], "AWAITING_FINAL")

    # --- (iv) the second pass resumes from REVIEWED without an illegal self-transition --

    def test_the_second_pass_resumes_from_the_reviewed_state_the_first_wrote(self):
        """The real sequence: stop, the user writes the decision, run the step again.

        REVIEWED -> REVIEWED is not a legal successor and `assurance_state.advance` does not
        check legality, so a second pass that re-advanced would write an illegal transition
        silently. The pass instead finds REVIEWED, leaves it, and takes the one transition it
        is entitled to.
        """
        root = self.lows_round_zero()
        first, _ = run_main(self.template, self.argv(root, "--emit"))
        self.assertEqual(first, 0)
        self.assertEqual(self.saved_state(root)["status"], "REVIEWED")

        (root / CONTROL_ROOT / "control" / "user-decision-repair.json").write_text(
            json.dumps(NO_REPAIR_DECISION), encoding="utf-8")
        second, out = run_main(self.template, self.argv(root, "--emit"))
        self.assertEqual(second, 0, out)
        self.assertIn(
            "state                  : already REVIEWED from the earlier pass; only the "
            "AWAITING_FINAL transition is owed",
            out.splitlines(),
        )
        saved = self.saved_state(root)
        self.assertEqual(saved["status"], "AWAITING_FINAL")
        self.assertEqual(
            saved.get("review_ref"),
            {
                "path": f"{CONTROL_ROOT}/evidence/review-full.json",
                "digest_sha256": bytes_digest(
                    json.dumps(CLEAN_FULL_REVIEW).encode("utf-8")),
            },
        )


class TheDeclarationsAreReadNeverDefaulted(BindTemplateCase):
    """R2 (`HD-11`): `governance_scan` and `disclosures` come from the run, or the bind stops.

    They were CONFIG constants shipped with a placeholder `skip_reason`, which is the one
    shape a template must not supply: a skip reason is an honest sentence about THIS run, and
    a default is the executor's excuse written by somebody who was not there. Both halves are
    pinned — the file's absence and a key's absence — because a partially-filled declaration
    file is the likelier of the two.
    """

    def test_a_missing_declarations_file_stops_the_bind(self):
        root = self.clean_declared(declarations=None)
        code, out = run_main(self.template, self.argv(root, "--emit"))
        self.assertEqual(code, 1)
        self.assertIn(
            "STOP: control/bind-declarations.json does not exist; the governance-scan state "
            "and the run's disclosures are declarations, not derivations",
            out.splitlines(),
        )
        self.assertFalse(
            (root / CONTROL_ROOT / "control" / "assurance-candidate.json").exists())

    def test_a_declarations_file_missing_a_key_stops_the_bind(self):
        root = self.clean_declared(declarations={"disclosures": []})
        code, out = run_main(self.template, self.argv(root, "--emit"))
        self.assertEqual(code, 1)
        self.assertIn(
            "STOP: control/bind-declarations.json carries no governance_scan; this script "
            "supplies no default for either",
            out.splitlines(),
        )

    def test_a_complete_declarations_file_does_not_trip_the_stop(self):
        """Negative control (E4): the guard is about absence, not about the values."""
        root = self.clean_declared(declarations=BIND_DECLARATIONS)
        code, out = run_main(self.template, self.argv(root))
        self.assertEqual(code, 0, out)
        self.assertNotIn("STOP: control/bind-declarations.json", out)

    def clean_declared(self, *, declarations):
        # Carries the NO_REPAIR for the same reason `clean_round_zero` does: this class's
        # property is the declarations file, and the run has to reach the assembly to meet it.
        control_files = {
            "work-spec.json": WORK_SPEC,
            "resolved-plan.json": RESOLVED_PLAN,
            "instruction-audit.json": {"note": "test audit stand-in"},
        }
        if declarations is not None:
            control_files["bind-declarations.json"] = declarations
        root = self.make_run(
            repair_round=0,
            reviews=[("review-full.json", CLEAN_FULL_REVIEW)],
            repair=NO_REPAIR_DECISION,
            control_files=control_files,
            evidence_files={
                "candidate-record.json": CLEAN_RECORD,
                "check-results.json": [CHECK_RESULT],
                "check-chk-one.json": CHECK_RESULT,
                "coverage.json": {"rows": []},
            },
            state=clean_round_zero_state(),
        )
        self.template.RV = RecordingResultChecker(clean_report())
        return root


if __name__ == "__main__":
    unittest.main(verbosity=2)
