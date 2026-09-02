#!/usr/bin/env python3
"""Item 6 — `bind-declarations.json` is a schema'd document, refused where it is authored.

Batch `PROMISE-PATH`, round `PROMISE-PATH-ENGINE`. Nothing under ``schema/`` named this file:
a hand-authored control document fed a schema-capped generated one (``assurance.schema.json``
caps a disclosure statement and a governance ``skip_reason`` at 500 characters), and the only
thing that ever read its shape was ``run_bind_v2``'s two-key presence test. So an over-long
disclosure was first refused at the BIND — after the independent review had already read
those bytes, when correcting them means changing what was reviewed. The caller's run 2 met
exactly that: three disclosures at 541 / 843 / 513 characters, ``check_assurance_candidate``
refused, and the bind exited 1 having moved nothing.

The fix has two halves and this module owns the earlier one. The bind still validates (its
half is pinned in ``test_run_v2_template_bind.py``, where the run that USES the declarations
lives); the EVIDENCE step validates too, because the evidence commit is the moment the bytes
become what a reviewer reads, and everything before it is still the author's to correct
freely. Absence is deliberately NOT refused here: ``governance_scan.result_ref`` names a
CheckResult this step has not written yet, so a run that authors the file after the evidence
layer is legitimate — the bind refuses the absence there.

Every expectation is a hand-written literal, never imported from the template or from the
schema (E5), and every must-fire case is paired with a negative control (E4). The template is
loaded by explicit file path under a distinct module name, and ``main`` returning ``None``
means it ran PAST the guard and died downstream on a repository that holds no such commits —
so "the guard did not fire" fails on a VALUE, never as a test ERROR (R8).
"""
from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

import _harness  # noqa: F401 — installs the tooling import path the template needs

TEMPLATE_PATH: pathlib.Path = (
    _harness.RS_ROOT / "assurance" / "templates" / "run-v2" / "run_evidence_v2.py"
)

CONTROL_ROOT = "ResearchSystem/assurance/runs/tr-decl"
OBLIGATIONS = [{"obligation_id": "ob-one", "verification_mode": "review_only"}]
LOCATOR = {"path": "docs/thing.md", "anchor": "## The Thing"}

#: The state the evidence step reads its round from, hand-written (E5).
STATE = {
    "work_id": "w-test",
    "run_id": "tr-decl",
    "status": "EXECUTING",
    "repair_round": 0,
    "work_spec_ref": {"path": f"{CONTROL_ROOT}/control/work-spec.json"},
    "resolved_plan_ref": {"path": f"{CONTROL_ROOT}/control/resolved-plan.json"},
}

#: A well-formed declarations document: the scan did not run, and it says why.
VALID_DECLARATIONS = {
    "governance_scan": {
        "included": False,
        "skip_reason": "no governance document in this test fixture payload",
    },
    "disclosures": [],
}

#: The reported instance, at the reported length class: one character over the cap the
#: AssuranceCandidate enforces. 501 and 500 are written out rather than derived from the
#: schema, so a schema that silently relaxed its cap would fail here rather than agree.
SOURCE_REF = {"path": "docs/notes.md", "digest_sha256": "0" * 64}
OVER_CAP = {"statement": "x" * 501, "source_ref": SOURCE_REF}
AT_CAP = {"statement": "x" * 500, "source_ref": SOURCE_REF}


def load_template():
    """Bind the template file directly; never by adding its directory to sys.path."""
    if not TEMPLATE_PATH.is_file():
        raise RuntimeError(f"the v2 evidence template is missing at {TEMPLATE_PATH}")
    spec = importlib.util.spec_from_file_location("v2_evidence_declarations", TEMPLATE_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules.setdefault("v2_evidence_declarations", module)
    spec.loader.exec_module(module)
    return module


class DeclarationsAreRefusedBeforeTheEvidenceCommit(unittest.TestCase):
    """The earlier half of item 6: the bytes are checked before a reviewer can read them."""

    def setUp(self):
        self.template = load_template()
        root = pathlib.Path(tempfile.mkdtemp(prefix="v2-evidence-decl-"))
        self.addCleanup(shutil.rmtree, root, ignore_errors=True)
        subprocess.run(
            ["git", "-C", str(root), "init", "-q"], check=True, stdout=subprocess.DEVNULL
        )
        self.run_dir = root / CONTROL_ROOT
        self.control = self.run_dir / "control"
        self.control.mkdir(parents=True)
        (self.control / "work-spec.json").write_text(
            json.dumps({"obligations": OBLIGATIONS}), encoding="utf-8")
        (self.control / "resolved-plan.json").write_text(
            json.dumps({"effective_change_boundary": {"write_scope": [], "out": []}}),
            encoding="utf-8")
        (self.control / "state.json").write_text(json.dumps(STATE), encoding="utf-8")
        # Complete, so the fulfillment refusal above this guard never fires and every result
        # below is attributable to the declarations.
        (self.control / "fulfillment.json").write_text(
            json.dumps({"ob-one": {"status": "IMPLEMENTED",
                                   "implementation_locators": [LOCATOR]}}),
            encoding="utf-8")

    def write_declarations(self, document) -> None:
        (self.control / "bind-declarations.json").write_text(
            json.dumps(document), encoding="utf-8")

    def run_main(self) -> tuple[int | None, str]:
        captured = io.StringIO()
        try:
            with contextlib.redirect_stdout(captured):
                code = self.template.main([
                    str(self.run_dir),
                    "--base", "b" * 40,
                    "--candidate", "c" * 40,
                    "--candidate-branch", "run/tr-decl-candidate",
                ])
        except Exception:
            return None, captured.getvalue()
        return code, captured.getvalue()

    STOP = ("STOP: control/bind-declarations.json is not a valid BindDeclarations document "
            "— nothing committed, state not advanced")

    # --- must fire ---------------------------------------------------------------------

    def test_a_disclosure_over_the_cap_stops_before_anything_is_written(self):
        self.write_declarations({**VALID_DECLARATIONS, "disclosures": [OVER_CAP]})
        code, out = self.run_main()
        self.assertEqual(code, 1, out)
        self.assertIn("bind declarations    : ISSUES", out.splitlines())
        self.assertIn(self.STOP, out.splitlines())
        self.assertFalse((self.run_dir / "evidence").exists())

    def test_a_missing_key_stops_and_names_it(self):
        self.write_declarations({"disclosures": []})
        code, out = self.run_main()
        self.assertEqual(code, 1, out)
        self.assertIn(
            "  V3-SCHEMA-BIND_DECLARATIONS <root> — 'governance_scan' is a required property",
            out.splitlines(),
        )

    def test_a_skip_reason_over_the_cap_stops_too(self):
        """The defect CLASS (E7): both capped strings, not the disclosure that was reported."""
        self.write_declarations({
            "governance_scan": {"included": False, "skip_reason": "y" * 501},
            "disclosures": [],
        })
        code, out = self.run_main()
        self.assertEqual(code, 1, out)
        self.assertIn(self.STOP, out.splitlines())

    def test_a_disclosure_with_no_source_stops(self):
        """A disclosure with no source would be the controller speaking in its own voice."""
        self.write_declarations({
            **VALID_DECLARATIONS,
            "disclosures": [{"statement": "the scan did not run in this run"}],
        })
        code, out = self.run_main()
        self.assertEqual(code, 1, out)
        self.assertIn(self.STOP, out.splitlines())

    def test_a_key_the_document_may_not_carry_stops(self):
        """`additionalProperties: false`: a declaration the bind would silently ignore."""
        self.write_declarations({**VALID_DECLARATIONS, "verdict": "REVIEWED_NO_BLOCKER"})
        code, out = self.run_main()
        self.assertEqual(code, 1, out)
        self.assertIn(self.STOP, out.splitlines())

    # --- must not fire -----------------------------------------------------------------

    def test_negative_control_a_valid_document_is_reported_clean_and_passes(self):
        self.write_declarations(VALID_DECLARATIONS)
        code, out = self.run_main()
        self.assertIsNone(code, out)  # walks on and dies on the absent commits downstream
        self.assertIn("bind declarations    : clean", out.splitlines())
        self.assertNotIn(self.STOP, out)

    def test_negative_control_a_disclosure_exactly_at_the_cap_passes(self):
        self.write_declarations({**VALID_DECLARATIONS, "disclosures": [AT_CAP]})
        code, out = self.run_main()
        self.assertIsNone(code, out)
        self.assertIn("bind declarations    : clean", out.splitlines())

    def test_an_absent_file_is_reported_and_left_to_the_bind(self):
        """Absence is the bind's refusal, not this step's: the result_ref is not knowable yet."""
        code, out = self.run_main()
        self.assertIsNone(code, out)
        self.assertIn(
            "bind declarations    : absent (the bind step refuses it there; "
            "it may be authored after this step)",
            out.splitlines(),
        )
        self.assertNotIn(self.STOP, out)


if __name__ == "__main__":
    unittest.main(verbosity=2)
