"""Golden test for the user-facing coverage view (V3-N1).

Plan §6: user-facing reports show only the objective/candidate, instruction or obligation
exceptions, failed checks and boundary deltas, blocking findings, uncertainty and the
requested decision. What the user *sees* is therefore part of the product, not a rendering
detail — a later node that silently changed a missing artifact into a blank cell would
change what a user is deciding on without changing any acceptance ID.

So the view is pinned. The fixture deliberately contains exceptions rather than a wall of
green: one obligation not implemented, one failing check, one missing expected artifact and
one review-only obligation with no deterministic evidence at all.

The fixture is pure data with fixed identities — no Git repository, no clock, no filesystem
observation — so the golden is byte-reproducible. Regenerate deliberately with::

    python ResearchSystem/tooling/tests/document_harness/test_golden_views.py --regen
"""
from __future__ import annotations

import json
import pathlib
import sys
import unittest

import _harness  # noqa: F401 — installs the tooling import path

from rsclib.document_harness import canonical_bytes  # noqa: E402
from rsclib.document_harness import views  # noqa: E402

GOLDEN_DIR = _harness.RS_ROOT / "assurance" / "test"
VIEW_GOLDEN = GOLDEN_DIR / "coverage-view.golden.txt"
DOCUMENT_GOLDEN = GOLDEN_DIR / "coverage-document.golden.json"

_CANDIDATE = "a" * 40
_BASE = "b" * 40

SPEC = {
    "work_id": "golden-work",
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
            "unit_id": "u-changelog",
            "locator": {"path": "docs/instruction.md", "anchor": "record the change"},
            "classification": "obligation",
            "obligation_ids": ["o-changelog"],
        },
        {
            "unit_id": "u-tone",
            "locator": {"path": "docs/instruction.md", "anchor": "keep the tone plain"},
            "classification": "obligation",
            "obligation_ids": ["o-tone"],
        },
    ],
    "change_boundary": {"write_scope": ["docs"], "out": ["control"]},
    "expected_artifacts": [
        {"artifact_id": "a-guide", "path": "docs/guide.md"},
        {"artifact_id": "a-changelog", "path": "docs/changelog.md"},
    ],
    "obligations": [
        {
            "obligation_id": "o-guide",
            "instruction_unit_ids": ["u-guide"],
            "requirement": "the guide exists and every local link resolves",
            "expected_artifact_ids": ["a-guide"],
            "verification_mode": "local_check",
            "local_check_refs": ["c-guide-exists", "c-guide-links"],
        },
        {
            "obligation_id": "o-changelog",
            "instruction_unit_ids": ["u-changelog"],
            "requirement": "the changelog records this change",
            "expected_artifact_ids": ["a-changelog"],
            "verification_mode": "local_check",
            "local_check_refs": ["c-changelog-exists"],
        },
        {
            "obligation_id": "o-tone",
            "instruction_unit_ids": ["u-tone"],
            "requirement": "the guide reads plainly for a non-specialist",
            "verification_mode": "review_only",
        },
    ],
}

RECORD = {
    "record_id": "golden-record",
    "work_id": "golden-work",
    "run_id": "golden-run",
    "repair_round": 0,
    "candidate_ref": {"branch": "cand", "commit": _CANDIDATE},
    "base_revision": _BASE,
    "control_root": "control",
    "fulfillment": {
        "authored_by": "executor",
        "authored_at": "2026-07-20",
        "claims": [
            {
                "obligation_id": "o-guide",
                "status": "IMPLEMENTED",
                "implementation_locators": [{"path": "docs/guide.md", "anchor": "# Guide"}],
            },
            {
                "obligation_id": "o-changelog",
                "status": "NOT_IMPLEMENTED",
                "note": "the changelog file was not created; the instruction unit was read late",
            },
            {
                "obligation_id": "o-tone",
                "status": "IMPLEMENTED",
                "implementation_locators": [{"path": "docs/guide.md", "anchor": "## Overview"}],
            },
        ],
    },
    "manifest": {
        "authored_by": "diff-verifier",
        "authored_at": "2026-07-20",
        "changes": [{"path": "docs/guide.md", "change_kind": "added"}],
        "boundary_result": "CONFORMANT",
        "expected_artifact_results": [
            {"artifact_id": "a-guide", "present": True},
            {"artifact_id": "a-changelog", "present": False},
        ],
    },
}


def _result(check_id: str, kind: str, outcome: str, detail: str | None = None) -> dict:
    result = {
        "result_id": f"{check_id}-r",
        "check_id": check_id,
        "kind": kind,
        "request_digest_sha256": "c" * 64,
        "candidate_ref": {"branch": "cand", "commit": _CANDIDATE},
        "observed_tree": {"kind": "candidate_commit", "revision": _CANDIDATE},
        "result": outcome,
        "verified_by": "local-verifier",
    }
    if detail:
        result["detail"] = detail
    return result


RESULTS = [
    _result("c-guide-exists", "file_exists", "PASS"),
    _result(
        "c-guide-links",
        "markdown_link",
        "FAIL",
        "1 unresolved local link(s): docs/guide.md -> changelog.md",
    ),
    _result(
        "c-changelog-exists",
        "file_exists",
        "FAIL",
        "declared artifact is absent from the candidate: docs/changelog.md",
    ),
]


def render_view() -> str:
    return views.render_coverage(views.coverage_rows(SPEC, RECORD, RESULTS)) + "\n"


def render_document() -> bytes:
    return canonical_bytes(views.coverage_document(SPEC, RECORD, RESULTS)) + b"\n"


def regenerate() -> None:
    GOLDEN_DIR.mkdir(parents=True, exist_ok=True)
    VIEW_GOLDEN.write_bytes(render_view().encode("utf-8"))
    DOCUMENT_GOLDEN.write_bytes(render_document())
    print(f"wrote {VIEW_GOLDEN}")
    print(f"wrote {DOCUMENT_GOLDEN}")


class GoldenCoverageView(unittest.TestCase):
    """The user-facing surface is pinned, exceptions and all."""

    def test_rendered_view_matches_golden(self) -> None:
        """A change to what the user sees must be a deliberate, reviewed change."""
        self.assertTrue(VIEW_GOLDEN.exists(), f"golden missing: run this file with --regen")
        self.assertEqual(render_view(), VIEW_GOLDEN.read_text(encoding="utf-8"))

    def test_coverage_document_matches_golden(self) -> None:
        """The coverage document is a byte-reproducible join, not a stored owner."""
        self.assertTrue(DOCUMENT_GOLDEN.exists(), f"golden missing: run this file with --regen")
        self.assertEqual(render_document(), DOCUMENT_GOLDEN.read_bytes())

    def test_document_is_rebuildable(self) -> None:
        """Rebuilding the join twice yields identical bytes — coverage is disposable."""
        self.assertEqual(render_document(), render_document())

    def test_view_surfaces_every_exception(self) -> None:
        """Silence is never success: each exception in the fixture is visible in the view."""
        rendered = render_view()
        self.assertIn("NOT_IMPLEMENTED", rendered)
        self.assertIn("c-guide-links=FAIL", rendered)
        self.assertIn("missing artifact: a-changelog", rendered)

    def test_review_only_obligation_carries_no_review_verdict(self) -> None:
        """V3-N1 stops before semantic review, and the view must not imply otherwise."""
        document = views.coverage_document(SPEC, RECORD, RESULTS)
        self.assertEqual(document["review_disposition"], "NOT_YET_REVIEWED")
        tone_row = next(row for row in document["rows"] if row["obligation_id"] == "o-tone")
        self.assertEqual(tone_row["checks"], [])
        self.assertEqual(tone_row["verification_mode"], "review_only")


if __name__ == "__main__":
    if "--regen" in sys.argv:
        regenerate()
    else:
        raise SystemExit(
            unittest.main(module=None, argv=[sys.argv[0], "-v"], exit=False).result.wasSuccessful() is False
        )
