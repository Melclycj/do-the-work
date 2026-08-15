"""WorkSpec v2 — the special-case bucket wave-1 successor (W1-A1..W1-A4, W1-A6).

The N0-signed v1 schema is never modified; `document-work-spec.v2.schema.json` supersedes it
for newly authored WorkSpecs. The delta under test:

* root `schema_version` const "2" — the instance names its own schema;
* `review_only` obligations must carry `review_only_rationale` + `not_supported_when`
  (the cheap path costs two honest sentences); the deterministic mode forbids both;
* the mode enum is two-valued since SIMP-A1 (2026-08-05) — `local_check_and_review` is
  deleted, not deprecated, and a spec declaring it is refused;
* the loader keys on the declared version explicitly and never falls back across versions —
  a fallback would silently mix versions, the fail-open shape N1 taught this package to hunt;
* the coverage view opens with the verification-mode ratio line (visibility, never a gate).

Every negative here is the defect class, not one instance: the mode × field cross-product
is enumerated, and the no-fallback property is asserted from both directions.
"""
from __future__ import annotations

import copy
import unittest

import _harness  # noqa: F401 — installs the tooling import path

from rsclib.document_harness import SpecGap, validate  # noqa: E402
from rsclib.document_harness import spec as spec_mod  # noqa: E402
from rsclib.document_harness import views  # noqa: E402

_BASE = "b" * 40

V2_SPEC = {
    "schema_version": "2",
    "work_id": "w1-work",
    "objective": "author the guide and its changelog entry",
    "instruction_ref": {"path": "docs/instruction.md", "revision": _BASE},
    "instruction_units": [
        {
            "unit_id": "u-guide",
            "locator": {"path": "docs/instruction.md", "anchor": "write the guide"},
            "classification": "obligation",
            "obligation_ids": ["o-guide"],
        },
        {
            "unit_id": "u-tone",
            "locator": {"path": "docs/instruction.md", "anchor": "keep the tone plain"},
            "classification": "obligation",
            "obligation_ids": ["o-tone"],
        },
    ],
    "change_boundary": {"write_scope": ["docs"], "out": ["control"]},
    "expected_artifacts": [{"artifact_id": "a-guide", "path": "docs/guide.md"}],
    "obligations": [
        {
            "obligation_id": "o-guide",
            "instruction_unit_ids": ["u-guide"],
            "requirement": "the guide exists and every local link resolves",
            "expected_artifact_ids": ["a-guide"],
            "verification_mode": "local_check",
            "local_check_refs": ["c-guide-exists"],
        },
        {
            "obligation_id": "o-tone",
            "instruction_unit_ids": ["u-tone"],
            "requirement": "the guide reads plainly for a non-specialist",
            "verification_mode": "review_only",
            "review_only_rationale": "plainness is a reader judgement no closed check kind can decide",
            "not_supported_when": "a non-specialist reader cannot follow a section without outside help",
        },
    ],
}


def _v2(**overrides) -> dict:
    doc = copy.deepcopy(V2_SPEC)
    doc.update(overrides)
    return doc


def _review_only_obligation(**tweaks) -> dict:
    ob = copy.deepcopy(V2_SPEC["obligations"][1])
    for key, value in tweaks.items():
        if value is None:
            ob.pop(key, None)
        else:
            ob[key] = value
    return ob


def _deterministic_obligation(mode: str, **extra) -> dict:
    ob = copy.deepcopy(V2_SPEC["obligations"][0])
    ob["verification_mode"] = mode
    ob.update(extra)
    return ob


class VersionKeying(unittest.TestCase):
    """W1-A3 + W1-A4: explicit keying, fail-closed, no cross-version fallback."""

    def test_absent_version_keys_to_v1(self) -> None:
        self.assertEqual(spec_mod.spec_schema_kind({}), "spec")

    def test_version_two_keys_to_v2(self) -> None:
        self.assertEqual(spec_mod.spec_schema_kind({"schema_version": "2"}), "spec_v2")

    def test_unknown_versions_stop(self) -> None:
        """No older label, future label, non-string — or explicit null — is ever guessed at.

        The explicit-null case is the W1 review's A1: `.get()` alone reads `null` as absent
        and would route it silently to v1; a *present* `schema_version` is a declaration,
        whatever its value, and an undeclarable declaration stops."""
        for declared in ("1", "3", "2.0", "", 2, 2.0, True, ["2"], {"v": "2"}, None):
            with self.subTest(declared=declared):
                with self.assertRaises(SpecGap):
                    spec_mod.spec_schema_kind({"schema_version": declared})

    def test_check_spec_stops_on_unknown_version(self) -> None:
        with self.assertRaises(SpecGap):
            spec_mod.check_spec(_v2(schema_version="3"))

    def test_v1_never_accepts_v2_fields(self) -> None:
        """A v2-shaped document that forgets its version lands on v1 and is rejected —
        the closed v1 root leaves no silent path for the new fields."""
        doc = _v2()
        del doc["schema_version"]
        report = spec_mod.check_spec(doc)
        self.assertFalse(report.ok)
        rendered = "\n".join(report.rendered())
        self.assertIn("V3-SCHEMA-SPEC", rendered)
        self.assertNotIn("SPEC_V2", rendered)

    def test_v2_failure_is_reported_against_v2_never_retried_on_v1(self) -> None:
        """The no-fallback direction that would actually fail open: a declared-v2 document
        with a v2 violation must surface v2's own error, not a v1 acceptance."""
        doc = _v2()
        doc["obligations"][1] = _review_only_obligation(review_only_rationale=None)
        report = spec_mod.check_spec(doc)
        self.assertFalse(report.ok)
        self.assertTrue(
            all(issue.code == "V3-SCHEMA-SPEC_V2" for issue in report.issues),
            [issue.render() for issue in report.issues],
        )


class ReviewOnlyFields(unittest.TestCase):
    """W1-A1: the cheap path costs two honest sentences, enforced as presence."""

    def test_valid_v2_spec_passes(self) -> None:
        report = spec_mod.check_spec(_v2())
        self.assertTrue(report.ok, report.rendered())

    def test_review_only_missing_either_or_both_fields_is_rejected(self) -> None:
        cases = {
            "missing rationale": {"review_only_rationale": None},
            "missing not_supported_when": {"not_supported_when": None},
            "missing both": {"review_only_rationale": None, "not_supported_when": None},
        }
        for label, tweaks in cases.items():
            with self.subTest(case=label):
                doc = _v2()
                doc["obligations"][1] = _review_only_obligation(**tweaks)
                self.assertFalse(spec_mod.check_spec(doc).ok)

    def test_empty_or_short_field_values_are_rejected(self) -> None:
        """A present-but-hollow-empty field is not a sentence; minLength holds the floor."""
        for field in ("review_only_rationale", "not_supported_when"):
            for value in ("", "short"):
                with self.subTest(field=field, value=value):
                    doc = _v2()
                    doc["obligations"][1] = _review_only_obligation(**{field: value})
                    self.assertFalse(spec_mod.check_spec(doc).ok)

    def test_v2_requires_its_version_const(self) -> None:
        """Defense in depth for direct validate('spec_v2', ...) callers."""
        doc = _v2()
        del doc["schema_version"]
        self.assertFalse(validate("spec_v2", doc).ok)
        self.assertFalse(validate("spec_v2", _v2(schema_version="1")).ok)


class DeterministicModeForbidsTheFields(unittest.TestCase):
    """W1-A2: the full mode × field cross-product, not one instance.

    Since SIMP-A1 (2026-08-05) there is exactly one deterministic mode, so the product is
    1 × 2; `TwoStateVerificationMode` below guards the deletion itself.
    """

    def test_cross_product_rejected(self) -> None:
        fields = {
            "review_only_rationale": "this could not be a script for a stated reason",
            "not_supported_when": "the stated condition that would refute the requirement",
        }
        for field, value in fields.items():
            with self.subTest(field=field):
                doc = _v2()
                doc["obligations"][0] = _deterministic_obligation(
                    "local_check", **{field: value})
                self.assertFalse(spec_mod.check_spec(doc).ok)

    def test_deterministic_mode_still_passes_without_the_fields(self) -> None:
        """Negative control: the cross-product failures above are caused by the fields."""
        doc = _v2()
        doc["obligations"][0] = _deterministic_obligation("local_check")
        report = spec_mod.check_spec(doc)
        self.assertTrue(report.ok, report.rendered())


class TwoStateVerificationMode(unittest.TestCase):
    """SIMP-A1: the both-modes value is deleted from the closed enum, not deprecated.

    The rule this guards is that a WorkSpec cannot declare an obligation whose check
    decides only half of it. A deprecation that still validated would leave the mode
    reachable by anyone who did not read the prose, which is the shape the deletion exists
    to end.
    """

    def test_both_modes_value_is_rejected(self) -> None:
        doc = _v2()
        doc["obligations"][0] = _deterministic_obligation("local_check_and_review")
        rendered = "\n".join(spec_mod.check_spec(doc).rendered())
        self.assertFalse(spec_mod.check_spec(doc).ok)
        self.assertIn("verification_mode", rendered)

    def test_both_surviving_values_are_accepted(self) -> None:
        """Negative control: the rejection above is the deleted value, not the field.

        The base fixture already carries one obligation of each surviving mode, so a green
        report here is the two-value enum passing, not a mode going unexercised.
        """
        report = spec_mod.check_spec(_v2())
        self.assertTrue(report.ok, report.rendered())
        self.assertEqual(
            {ob["verification_mode"] for ob in V2_SPEC["obligations"]},
            {"local_check", "review_only"},
        )


class SpineRulesApplyToV2(unittest.TestCase):
    """The v1 cross-document spine (ids, both-direction references) governs v2 unchanged."""

    def test_dangling_unit_ref_still_caught_under_v2(self) -> None:
        doc = _v2()
        doc["obligations"][0]["instruction_unit_ids"] = ["u-ghost"]
        rendered = "\n".join(spec_mod.check_spec(doc).rendered())
        self.assertIn("V3-SPEC-DANGLING-UNIT-REF", rendered)

    def test_unreferenced_obligation_still_caught_under_v2(self) -> None:
        doc = _v2()
        doc["instruction_units"][1]["obligation_ids"] = ["o-guide"]
        rendered = "\n".join(spec_mod.check_spec(doc).rendered())
        self.assertIn("V3-SPEC-UNREFERENCED-OBLIGATION", rendered)


class ModeSummaryLine(unittest.TestCase):
    """W1-A6: the ratio is visible, correct, and carries no verdict semantics."""

    # Deliberately asymmetric (W1 review finding A2): review_only (1) differs from its
    # complement (3), so a count inversion cannot hide behind symmetry; and one row binds
    # TWO checks, so counting checks (4) is distinguishable from counting rows that bind
    # checks (3).
    ROWS = [
        {
            "verification_mode": "local_check",
            "checks": [
                {"check_id": "c1", "result": "PASS"},
                {"check_id": "c2", "result": "FAIL"},
            ],
        },
        {"verification_mode": "review_only", "checks": []},
        {"verification_mode": "local_check", "checks": [{"check_id": "c3", "result": "NO_RESULT"}]},
        {"verification_mode": "local_check", "checks": [{"check_id": "c4", "result": "PASS"}]},
    ]

    def test_counts(self) -> None:
        self.assertEqual(
            views.mode_summary(self.ROWS),
            {"total": 4, "review_only": 1, "bind_checks": 3},
        )

    def test_line_wording(self) -> None:
        self.assertEqual(
            views.mode_summary_line(self.ROWS),
            "1 of 4 obligations review_only · 3 bind checks",
        )

    def test_render_coverage_opens_with_the_line(self) -> None:
        rows = [
            dict(row, obligation_id=f"o-{i}", fulfillment_status="IMPLEMENTED",
                 implementation_locators=[], expected_artifacts=[])
            for i, row in enumerate(self.ROWS)
        ]
        rendered = views.render_coverage(rows)
        self.assertTrue(
            rendered.startswith("1 of 4 obligations review_only · 3 bind checks"),
            rendered.splitlines()[0],
        )

    def test_line_carries_no_verdict_vocabulary(self) -> None:
        """Visibility, never a gate: no verdict or threshold word rides the line."""
        line = views.mode_summary_line(self.ROWS).casefold()
        for token in ("pass", "fail", "block", "gate", "threshold", "verdict", "ok"):
            self.assertNotIn(token, line)


if __name__ == "__main__":
    raise SystemExit(
        unittest.main(module=None, argv=[__import__("sys").argv[0], "-v"], exit=False)
        .result.wasSuccessful()
        is False
    )
