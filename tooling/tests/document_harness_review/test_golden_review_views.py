"""Golden tests for the user-facing review, flow and disposition views (V3-N2).

Plan §6: user-facing reports show only the objective/candidate, instruction or obligation
exceptions, failed checks and boundary deltas, blocking findings, uncertainty and the
requested decision. What the user *sees* is therefore part of the product, not a rendering
detail — a later node that silently turned an `UNVERIFIABLE` obligation into a blank line, or
dropped the "no residual uncertainty" statement, would change what a user is deciding on
without changing any acceptance ID.

Three renderings are pinned, and each fixture deliberately carries the exception rather than
the happy path:

* `review.render_result` — one unsupported obligation, one unverifiable one, a blocker with
  its minimum fix, and a residual;
* `flow.render_flow` — a state missing a pointer its own status requires;
* `summary.render_summary` — an `ACCEPT_WITH_LIMITATIONS` close-out that promoted nothing.

A fourth pins the empty-residual line specifically. `residual_uncertainty: []` is a positive
statement by the reviewer that none was found, and it must render as such — if it rendered as
nothing at all it would be indistinguishable from a reviewer who never considered the
question, which is the exact distinction the required-but-possibly-empty field exists to make.

The fixtures are pure data with fixed identities — no Git repository, no clock, no filesystem
observation — so the goldens are byte-reproducible. Regenerate deliberately with::

    python tooling/tests/document_harness_review/test_golden_review_views.py --regen
"""
from __future__ import annotations

import json
import pathlib
import sys
import unittest

import _harness  # noqa: F401 — installs the tooling and V3-N1 mechanism import paths

from rsclib.document_harness import canonical_bytes  # noqa: E402
from rsclib.document_harness import flow, issues, review, summary  # noqa: E402

GOLDEN_DIR = _harness.RS_ROOT / "assurance" / "review-test"
RESULT_GOLDEN = GOLDEN_DIR / "review-result-view.golden.txt"
RESULT_EMPTY_RESIDUAL_GOLDEN = GOLDEN_DIR / "review-result-no-residual.golden.txt"
FLOW_GOLDEN = GOLDEN_DIR / "flow-position.golden.txt"
SUMMARY_GOLDEN = GOLDEN_DIR / "summary-view.golden.txt"
ISSUE_GOLDEN = GOLDEN_DIR / "harness-issue-view.golden.txt"

_CANDIDATE = "a" * 40
_BASE = "b" * 40
_DIGEST = "c" * 64
_PACKAGE_DIGEST = "d" * 64

REVIEW_RESULT = {
    "result_id": "rr-golden",
    "work_id": "golden-work",
    "run_id": "golden-run",
    "review_round": "FULL",
    "package_ref": {"path": "control/package.json", "digest_sha256": _PACKAGE_DIGEST},
    "candidate_ref": {"branch": "cand", "commit": _CANDIDATE},
    "verdict": "CHANGES_REQUIRED",
    "instruction_completeness": {
        "result": "COMPLETE",
        "instruction_ref": {"path": "docs/instruction.md", "revision": _BASE},
    },
    "per_obligation_disposition": [
        {"obligation_id": "ob-guide", "disposition": "SUPPORTED"},
        {
            "obligation_id": "ob-changelog",
            "disposition": "NOT_SUPPORTED",
            "note": "the changelog entry names a different release than the instruction froze",
            "finding_ids": ["f-changelog-release"],
        },
        {
            "obligation_id": "ob-tone",
            "disposition": "UNVERIFIABLE",
            "note": "the instruction gives no criterion the frozen subjects could be read against",
        },
    ],
    "findings": [
        {
            "finding_id": "f-changelog-release",
            "obligation_id": "ob-changelog",
            "blocking": True,
            "statement": "the changelog entry is filed under 2.1 but the instruction freezes 2.0",
            "candidate_locator": {"path": "docs/CHANGELOG.md", "anchor": "## 2.1"},
            "ground_truth_locator": {"path": "docs/instruction.md", "anchor": "release 2.0"},
            "minimum_fix": "move the entry under the 2.0 heading; no other line needs to change",
        },
        {
            "finding_id": "f-heading-case",
            "blocking": False,
            "statement": "two headings use sentence case where the rest of the document uses title case",
        },
    ],
    "residual_uncertainty": [
        "whether the tone requirement was met is a judgment the frozen subjects cannot settle"
    ],
    "reviewed_by": "Reviewer Rin",
}

FLOW_STATE = {
    "work_id": "golden-work",
    "run_id": "golden-run",
    "status": "REVIEWED",
    "repair_round": 0,
    "work_spec_ref": {"path": "control/spec.json"},
    "resolved_plan_ref": {"path": "control/plan.json"},
    "instruction_audit_ref": {"path": "control/audit.json"},
    "start_decision_ref": {"path": "control/start.json"},
    "fulfillment_ref": {"path": "control/fulfillment.json"},
    "manifest_ref": {"path": "control/manifest.json"},
    # coverage_ref is deliberately absent: REVIEWED requires it, so the view must say so.
    "review_ref": {"path": "control/review.json"},
}

SUMMARY_DOCUMENT = {
    "summary_id": "sum-golden",
    "work_id": "golden-work",
    "run_id": "golden-run",
    "assurance_candidate_ref": {"path": "control/assurance.json", "digest_sha256": _DIGEST},
    "final_decision_ref": {"path": "control/final.json", "digest_sha256": _PACKAGE_DIGEST},
    "outcome": "ACCEPT_WITH_LIMITATIONS",
    "promotion": {
        "promoted": False,
        "reason": "the user accepted the document set but chose not to promote it in this session",
    },
    "limitations": [
        "the tone requirement was accepted as unverifiable rather than met",
        "the governance frontmatter scan did not run in this run",
    ],
    "generated_by": "controller",
}

HARNESS_ISSUE = {
    "issue_id": "hi-golden",
    "work_id": "golden-work",
    "run_id": "golden-run",
    "kind": "PROCESS_BURDEN",
    "statement": "freezing the package by hand took longer than writing the document it reviews",
    "evidence_refs": [{"path": "control/package.json", "digest_sha256": _PACKAGE_DIGEST}],
    "observed_after": "CLOSED",
    "observed_by": "Observer Oki",
}


def _render_all() -> dict[pathlib.Path, str]:
    no_residual = dict(REVIEW_RESULT, residual_uncertainty=[], verdict="REVIEWED_NO_BLOCKER")
    no_residual["findings"] = [REVIEW_RESULT["findings"][1]]  # the non-blocking one only
    no_residual["per_obligation_disposition"] = [REVIEW_RESULT["per_obligation_disposition"][0]]
    return {
        RESULT_GOLDEN: review.render_result(REVIEW_RESULT),
        RESULT_EMPTY_RESIDUAL_GOLDEN: review.render_result(no_residual),
        FLOW_GOLDEN: flow.render_flow(FLOW_STATE),
        SUMMARY_GOLDEN: summary.render_summary(SUMMARY_DOCUMENT),
        ISSUE_GOLDEN: issues.render_issue(HARNESS_ISSUE),
    }


class GoldenViewTests(unittest.TestCase):
    """The rendered views are pinned byte-for-byte."""

    def test_views_match_their_goldens(self):
        for path, rendered in _render_all().items():
            with self.subTest(golden=path.name):
                self.assertTrue(path.exists(), f"missing golden: {path}")
                self.assertEqual(
                    path.read_bytes(),
                    rendered.encode("utf-8"),
                    f"{path.name} drifted; regenerate deliberately, never to make a test pass",
                )

    def test_result_view_shows_every_exception_and_the_minimum_fix(self):
        """The view is not merely stable — it must actually carry the decision inputs."""
        rendered = review.render_result(REVIEW_RESULT)
        for expected in (
            "NOT_SUPPORTED",
            "UNVERIFIABLE",
            "[BLOCKER] f-changelog-release",
            "minimum fix:",
            "?? residual:",
        ):
            with self.subTest(fragment=expected):
                self.assertIn(expected, rendered)
        self.assertNotIn("ob-guide", rendered, "a SUPPORTED obligation is not an exception")

    def test_empty_residual_renders_as_a_positive_statement(self):
        """`residual_uncertainty: []` is the reviewer saying 'none', not saying nothing.

        If it rendered as absence, a reviewer who found none and a reviewer who never
        considered the question would produce identical output — the distinction the
        required-but-possibly-empty field exists to preserve.
        """
        rendered = review.render_result(dict(REVIEW_RESULT, residual_uncertainty=[]))
        self.assertIn("the reviewer recorded no residual uncertainty", rendered)

    def test_flow_view_names_the_missing_required_pointer(self):
        rendered = flow.render_flow(FLOW_STATE)
        self.assertIn("missing required pointer: coverage_ref", rendered)
        self.assertIn("REPAIRING", rendered)  # the legal successors are shown

    def test_flow_view_of_a_complete_state_reports_nothing_missing(self):
        """Negative control: the missing-pointer line must not be printed unconditionally."""
        complete = dict(FLOW_STATE, coverage_ref={"path": "control/coverage.json"})
        self.assertNotIn("missing required pointer", flow.render_flow(complete))

    def test_summary_view_states_non_promotion_and_every_limitation(self):
        rendered = summary.render_summary(SUMMARY_DOCUMENT)
        self.assertIn("promoted     : no", rendered)
        for limitation in SUMMARY_DOCUMENT["limitations"]:
            with self.subTest(limitation=limitation[:30]):
                self.assertIn(limitation, rendered)

    def test_issue_view_states_that_routing_is_not_on_the_document(self):
        """N2-A11: an issue has no lifecycle, and the view must not imply one."""
        rendered = issues.render_issue(HARNESS_ISSUE)
        self.assertIn("routing is a separate user ISSUE_TRIAGE decision", rendered)


class N2ValidatorTests(unittest.TestCase):
    """The V3-N2 schema extension: registered, closed, and failing closed."""

    #: The kinds `review.py` registers, hand-written here and deliberately never read back
    #: from the module (`E5`). Without it this class is the F4 defect class it was built to
    #: replace: `test_every_n2_kind_resolves_to_a_real_schema` below iterates the very tables
    #: it checks, so a table that loses an entry loses the assertion with it and stays green.
    #: `test_fix_round_locks.py` fixed exactly that shape for the module list by comparing
    #: against the directory and never for these tables; round `V1-RESULT-RETIRE` made the
    #: gap urgent by removing two entries — `review_package` and `review_result`, which went
    #: with the version-1 schema file — so the set below is the post-retirement one. Round
    #: `PROMISE-PATH-ENGINE` added `bind_declarations`, whose schema `$ref`s two `$defs` of
    #: `assurance.schema.json` and therefore has to resolve through THIS registry.
    EXPECTED_N2_KINDS = frozenset(
        {"assurance_candidate", "harness_issue", "assurance_summary", "bind_declarations"}
    )

    #: Kinds that existed and were deliberately retired. A retired kind must stop, never
    #: quietly validate, and never come back unannounced.
    RETIRED_N2_KINDS = ("review_package", "review_result")

    def test_the_registered_kinds_are_exactly_the_hand_written_set(self):
        self.assertEqual(
            set(review.N2_SCHEMA_FILES) | set(review.N2_SCHEMA_POINTERS),
            set(self.EXPECTED_N2_KINDS),
            "the N2 kind tables no longer match the hand-written expectation; a kind was "
            "added or lost without this test being told",
        )

    def test_the_retired_version_1_kinds_no_longer_resolve(self):
        """Round `V1-RESULT-RETIRE`: both v1 kinds went with `review.schema.json`.

        The negative control is `test_every_n2_kind_resolves_to_a_real_schema` below — the
        live kinds report rather than raise, so this is not a validator that raises for
        everything.
        """
        from rsclib.document_harness import SpecGap

        for kind in self.RETIRED_N2_KINDS:
            with self.subTest(kind=kind):
                with self.assertRaises(SpecGap):
                    review.validate_n2(kind, {})

    def test_every_n2_kind_resolves_to_a_real_schema(self):
        for kind in (*review.N2_SCHEMA_FILES, *review.N2_SCHEMA_POINTERS):
            with self.subTest(kind=kind):
                report = review.validate_n2(kind, {})
                self.assertFalse(
                    report.ok, f"{kind} accepted an empty document, so it validated nothing"
                )

    def test_unknown_kind_fails_closed(self):
        """An unrecognised document kind is never validated permissively."""
        from rsclib.document_harness import SpecGap

        with self.assertRaises(SpecGap):
            review.validate_n2("not_a_real_kind", {})

    def test_n2_registry_covers_the_frozen_pack_as_well_as_the_new_schemas(self):
        """The extension must not shadow the N0/N1 pack it builds on.

        `__init__.py` is outside V3-N2's boundary, so the three schemas authored here cannot
        be registered with the package validator and this local registry exists instead. The
        risk that creates is a second, divergent view of the pack — so the registry is built
        from the public `SCHEMA_FILES` export rather than a restatement of it, and this test
        pins that: every frozen schema must still resolve through the N2 registry.
        """
        from rsclib.document_harness import SCHEMA_FILES

        registry = review._n2_registry()
        for filename in (*SCHEMA_FILES.values(), *review.N2_SCHEMA_FILES.values()):
            with self.subTest(schema=filename):
                resolved = registry.get("researchsystem/schema/document-assurance-v3/" + filename)
                self.assertIsNotNone(resolved, f"{filename} does not resolve through the N2 registry")

    def test_canonical_bytes_of_a_review_result_are_stable(self):
        """A result is bound by digest, so its canonical form must not depend on key order."""
        shuffled = dict(reversed(list(REVIEW_RESULT.items())))
        self.assertEqual(canonical_bytes(REVIEW_RESULT), canonical_bytes(shuffled))


def _schema(filename: str) -> dict:
    from rsclib.document_harness import SCHEMA_DIR

    with open(SCHEMA_DIR / filename, encoding="utf-8") as handle:
        return json.load(handle)


def review_v2_schema() -> dict:
    """The live ReviewResult schema — it states the verdict enum inline."""
    return _schema("review.v2.schema.json")


def common_schema() -> dict:
    """The shared definitions that schema references, five of them ex-version-1."""
    return _schema("common.schema.json")


class TheClosedReviewSurface(unittest.TestCase):
    """N2-A3: the review surface can express a bounded finding and nothing stronger.

    Both methods came here from `test_package_and_review.py` when round `CORE-SET-CODE`
    retired the v1 package leg and that suite with it. They are the two of its N2-A3 set
    that assert against a schema alone and needed no v1 function, and they are kept rather
    than dropped because what they pin is **still live**. Their subject moved in round
    `V1-RESULT-RETIRE` and their reason did not: the five `$defs` the successor result
    references — `reviewRound`, `instructionCompleteness`, `perObligationDisposition`,
    `finding`, `verifyScope` — moved byte-equal into `common.schema.json`, and the verdict
    and residual-uncertainty leaves are stated inline in `review.v2.schema.json`. Together
    those two files are the review surface today, which is why both are read below; the
    version-1 file that used to hold all of it was retired in the same round.

    The other six N2-A3 methods needed the retired `make_package` / `check_review_result`
    and went with the leg; what they covered (an unknown kind failing shut, every kind
    resolving) is `N2ValidatorTests` above.
    """

    def test_n2_a3_control_verdicts_are_exactly_the_contract_set(self):
        result = review_v2_schema()
        shared = common_schema()
        # The root enum is the UNION of the two rounds and has been since round
        # `PROMISE-PATH-VOCAB` gave the VERIFY round `UNRESOLVED_BLOCKER` (contract §5's
        # VERIFY row, amended in place under `HD-70`). Asserting only the root would no
        # longer say what contract §5 says, because §5 states the two rows separately and
        # closes the FULL one at three; so each round's narrowing is asserted here beside
        # the union, against hand-written literals.
        self.assertEqual(
            result["properties"]["verdict"]["enum"],
            ["REVIEWED_NO_BLOCKER", "CHANGES_REQUIRED", "SPEC_GAP", "UNRESOLVED_BLOCKER"],
        )
        rounds = {
            rule["if"]["properties"]["review_round"]["const"]:
                rule["then"].get("properties", {}).get("verdict", {}).get("enum")
            for rule in result["allOf"]
            if "review_round" in rule["if"].get("properties", {})
        }
        self.assertEqual(
            rounds["FULL"], ["REVIEWED_NO_BLOCKER", "CHANGES_REQUIRED", "SPEC_GAP"])
        self.assertEqual(
            rounds["VERIFY"], ["REVIEWED_NO_BLOCKER", "SPEC_GAP", "UNRESOLVED_BLOCKER"])
        self.assertEqual(shared["$defs"]["reviewRound"]["enum"], ["FULL", "VERIFY"])
        self.assertEqual(
            shared["$defs"]["instructionCompleteness"]["properties"]["result"]["enum"],
            ["COMPLETE", "INCOMPLETE"],
        )
        self.assertEqual(
            shared["$defs"]["perObligationDisposition"]["properties"]["disposition"]["enum"],
            ["SUPPORTED", "NOT_SUPPORTED", "UNVERIFIABLE"],
        )

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

        for document in (review_v2_schema(), common_schema()):
            walk(document)
        self.assertIn("residual_uncertainty", names)  # the scan really did reach the leaves
        self.assertIn("REVIEWED_NO_BLOCKER", values)
        for token in forbidden:
            for name in sorted(names):
                self.assertNotIn(token, name.casefold(), f"proof vocabulary in property {name}")
            for value in sorted(values):
                self.assertNotIn(token, value.casefold(), f"proof vocabulary in enum value {value}")


def _regen() -> int:
    GOLDEN_DIR.mkdir(parents=True, exist_ok=True)
    for path, rendered in _render_all().items():
        path.write_bytes(rendered.encode("utf-8"))
        print(f"wrote {path}")
    return 0


if __name__ == "__main__":
    if "--regen" in sys.argv:
        raise SystemExit(_regen())
    raise SystemExit(unittest.main(argv=[sys.argv[0]]))
