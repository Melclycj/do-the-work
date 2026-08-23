#!/usr/bin/env python3
"""Adversarial half of the V3-N1 acceptance matrix: the seven named negatives.

Every test here exists to answer one question — *does the harness actually detect the
failure it claims to detect?* A test that passes because nothing was checked is worse than
no test, so each method asserts the exact issue **code** or the exact result **value**, never
merely that "something failed".

Coverage:

* ``N1-A5`` — the payload candidate contains only declared document changes; control
  evidence lives outside it.
* ``N1-A6`` — every obligation, expected artifact and observed diff has an explicit result;
  silence is never success.
* ``N1-A7`` — the manifest's sole author is the deterministic diff verifier, never the
  executor of the same run.
* ``N1-A8`` — the LocalCheckSpec union is closed: exact per-kind config, and an unknown kind
  is a ``SPEC_GAP`` that has no representable result.
* ``N1-A9`` — the seven named negatives, each against a real Git repository.
* ``R1``    — observed-tree recording: a candidate-subject check reads the candidate commit,
  never the mutable working tree.
* ``R3``    — the schema vocabulary guard is extended to ``const`` literals, which the frozen
  V3-N0 fixture runner never scanned.
* ``R4``    — a governance document never carries its own approval status, and the
  grandfather list is blob-keyed so it fails closed on the first edited byte.

Offline and deterministic. Every Git identity comes from a disposable ``TempRepo`` under the
system temp directory; the only files read out of the repository under assurance are the two
real governance documents in the R4 scan, which are read, never written.
"""
from __future__ import annotations

import copy
import json
import pathlib
import subprocess
import sys
import tempfile
import time
import unittest
from unittest import mock

from _harness import TempRepo, git  # noqa: F401 — installs the tooling import path

from rsclib.document_harness import (
    SCHEMA_DIR,
    SCHEMA_FILES,
    SpecGap,
    load_json,
    validate,
)
from rsclib.document_harness.candidate import (
    CandidateTreeReader,
    WorktreeReader,
    build_record,
    check_locators,
    check_record,
    covered_by,
    evaluate_boundary,
    observe_changes,
    observe_manifest,
    resolve_locator,
)
from rsclib.document_harness import checks as checks_module
from rsclib.document_harness.checks import (
    CANDIDATE_SUBJECT_KINDS,
    CheckContext,
    Exemption,
    SELF_APPROVAL_FIELDS,
    frontmatter_keys,
    git_blob_id,
    governance_scan,
    load_exemptions,
    require_supported_kind,
    run_all,
    run_check,
)
from rsclib.document_harness.views import coverage_report, coverage_rows

#: The real repository root. `__file__` sits at
#: `<root>/tooling/tests/document_harness/`, so four parents up is the root — the
#: instrument's own repository since round DE-PREFIX removed the caller-era prefix.
REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]

#: A syntactically valid but meaningless Git revision, used where a fixture needs a
#: schema-valid `gitRev` that no test resolves against a real object.
FAKE_REV = "0" * 40

BOUNDARY = {"write_scope": ["docs"], "out": ["docs/private"]}

EXECUTOR = "executor agent"
VERIFIER = "deterministic diff verifier"


# ---------------------------------------------------------------------------
# Minimal fixture builders. They build the *envelope* only — every defect a test
# demonstrates is written explicitly in that test's own body.
# ---------------------------------------------------------------------------


def codes(report) -> list[str]:
    return [issue.code for issue in report.issues]


def make_obligation(
    obligation_id: str,
    *,
    verification_mode: str = "review_only",
    local_check_refs: list[str] | None = None,
    expected_artifact_ids: list[str] | None = None,
) -> dict:
    obligation = {
        "obligation_id": obligation_id,
        "instruction_unit_ids": [f"unit-{obligation_id}"],
        "requirement": f"the work satisfies {obligation_id}",
        "verification_mode": verification_mode,
    }
    if local_check_refs:
        obligation["local_check_refs"] = local_check_refs
    if expected_artifact_ids:
        obligation["expected_artifact_ids"] = expected_artifact_ids
    return obligation


def make_spec(
    obligations: list[dict],
    expected_artifacts: list[dict],
    *,
    work_id: str = "work-one",
    boundary: dict | None = None,
) -> dict:
    spec = {
        "work_id": work_id,
        "objective": "produce the declared documents",
        "instruction_ref": {"path": "docs/instruction.md", "revision": FAKE_REV},
        "instruction_units": [
            {
                "unit_id": f"unit-{obligation['obligation_id']}",
                "locator": {"path": "docs/instruction.md", "anchor": f"## {obligation['obligation_id']}"},
                "classification": "obligation",
                "obligation_ids": [obligation["obligation_id"]],
            }
            for obligation in obligations
        ],
        "change_boundary": dict(boundary or BOUNDARY),
        "expected_artifacts": list(expected_artifacts),
        "obligations": list(obligations),
    }
    return spec


def make_claim(obligation_id: str, *, path: str = "docs/guide.md", anchor: str = "## Guide") -> dict:
    return {
        "obligation_id": obligation_id,
        "status": "IMPLEMENTED",
        "implementation_locators": [{"path": path, "anchor": anchor}],
    }


def make_record(
    *,
    spec: dict,
    candidate_ref: dict,
    base_revision: str,
    manifest: dict,
    claims: list[dict],
    control_root: str = "control",
    fulfillment_author: str = EXECUTOR,
) -> dict:
    return build_record(
        record_id="record-one",
        work_id=spec["work_id"],
        run_id="run-one",
        repair_round=0,
        candidate_ref=candidate_ref,
        base_revision=base_revision,
        control_root=control_root,
        fulfillment={"authored_by": fulfillment_author, "claims": claims},
        manifest=manifest,
    )


def make_manifest(
    *,
    boundary_result: str = "CONFORMANT",
    changes: list[dict] | None = None,
    artifact_results: list[dict] | None = None,
    out_of_boundary_paths: list[str] | None = None,
    authored_by: str = VERIFIER,
) -> dict:
    manifest = {
        "authored_by": authored_by,
        "boundary_result": boundary_result,
        "expected_artifact_results": artifact_results or [{"artifact_id": "artifact-guide", "present": True}],
    }
    if changes:
        manifest["changes"] = changes
    if out_of_boundary_paths:
        manifest["out_of_boundary_paths"] = out_of_boundary_paths
    return manifest


def context_for(repo: TempRepo, candidate: str, **overrides) -> CheckContext:
    kwargs = {
        "repo_root": repo.root,
        "candidate_ref": repo.candidate_ref(candidate),
        "base_revision": repo.base,
        "boundary": dict(BOUNDARY),
        "verified_by": VERIFIER,
    }
    kwargs.update(overrides)
    return CheckContext(**kwargs)


# ===========================================================================
# N1-A5 — payload holds only declared document changes; control evidence is outside it
# ===========================================================================


class PayloadEvidenceSeparationTests(unittest.TestCase):
    """N1-A5: a control file committed into the payload collapses the identity separation."""

    def test_n1_a5_control_file_committed_into_payload_is_detected(self):
        """A change under the record's control_root inside the candidate is reported."""
        with TempRepo({"docs/guide.md": "base\n"}) as repo:
            # The defect: the executor wrote assurance evidence into the payload candidate.
            candidate = repo.commit_candidate(
                {
                    "docs/guide.md": "## Guide\ncandidate\n",
                    "control/run-one/record.json": '{"authored_by": "executor agent"}\n',
                }
            )
            spec = make_spec(
                [make_obligation("ob-guide")],
                [{"artifact_id": "artifact-guide", "path": "docs/guide.md"}],
                # 'control' is inside the write scope, so the boundary result stays
                # CONFORMANT and the only issue left is the identity collapse itself.
                boundary={"write_scope": ["docs", "control"], "out": ["docs/private"]},
            )
            manifest = observe_manifest(
                repo.root,
                repo.base,
                candidate,
                spec["change_boundary"],
                spec["expected_artifacts"],
                authored_by=VERIFIER,
            )
            record = make_record(
                spec=spec,
                candidate_ref=repo.candidate_ref(candidate),
                base_revision=repo.base,
                manifest=manifest,
                claims=[make_claim("ob-guide")],
                control_root="control",
            )

            self.assertEqual(manifest["boundary_result"], "CONFORMANT")
            report = check_record(record, spec)
            self.assertIn("V3-CANDIDATE-CONTROL-FILE-IN-PAYLOAD", codes(report))
            self.assertTrue(
                any("control/run-one/record.json" in issue.message for issue in report.issues),
                report.rendered(),
            )

    def test_n1_a5_clean_payload_reports_no_control_file_issue(self):
        """A candidate that touches only declared document paths is not flagged."""
        with TempRepo({"docs/guide.md": "base\n"}) as repo:
            candidate = repo.commit_candidate({"docs/guide.md": "## Guide\ncandidate\n"})
            spec = make_spec(
                [make_obligation("ob-guide")],
                [{"artifact_id": "artifact-guide", "path": "docs/guide.md"}],
            )
            manifest = observe_manifest(
                repo.root,
                repo.base,
                candidate,
                spec["change_boundary"],
                spec["expected_artifacts"],
                authored_by=VERIFIER,
            )
            record = make_record(
                spec=spec,
                candidate_ref=repo.candidate_ref(candidate),
                base_revision=repo.base,
                manifest=manifest,
                claims=[make_claim("ob-guide")],
            )
            report = check_record(record, spec)
            self.assertNotIn("V3-CANDIDATE-CONTROL-FILE-IN-PAYLOAD", codes(report))
            self.assertTrue(report.ok, report.rendered())

    def test_n1_a5_control_root_containment_is_segment_bounded(self):
        """`control` covers `control/x` but never a sibling whose name merely starts the same."""
        self.assertTrue(covered_by("control/run-one/record.json", ["control"]))
        self.assertFalse(covered_by("controlled/notes.md", ["control"]))


# ===========================================================================
# N1-A6 — every obligation, artifact and observed diff has an explicit result
# ===========================================================================


class ExplicitResultTests(unittest.TestCase):
    """N1-A6: nothing under assurance may be left without a stated outcome."""

    def _clean_manifest(self, artifact_results=None) -> dict:
        return make_manifest(artifact_results=artifact_results)

    def test_n1_a6_obligation_without_a_claim_is_reported(self):
        """An obligation the executor never answered is an omission, not a pass."""
        spec = make_spec(
            [make_obligation("ob-alpha"), make_obligation("ob-beta")],
            [{"artifact_id": "artifact-guide", "path": "docs/guide.md"}],
        )
        record = make_record(
            spec=spec,
            candidate_ref={"branch": "cand", "commit": FAKE_REV},
            base_revision=FAKE_REV,
            manifest=self._clean_manifest(),
            claims=[make_claim("ob-alpha")],  # ob-beta is simply absent
        )
        report = check_record(record, spec)
        self.assertIn("V3-CANDIDATE-OBLIGATION-OMITTED", codes(report))
        self.assertTrue(any("ob-beta" in issue.message for issue in report.issues), report.rendered())

    def test_n1_a6_claim_for_an_undeclared_obligation_is_reported(self):
        """A claim the WorkSpec never asked for cannot be silently absorbed."""
        spec = make_spec(
            [make_obligation("ob-alpha")],
            [{"artifact_id": "artifact-guide", "path": "docs/guide.md"}],
        )
        record = make_record(
            spec=spec,
            candidate_ref={"branch": "cand", "commit": FAKE_REV},
            base_revision=FAKE_REV,
            manifest=self._clean_manifest(),
            claims=[make_claim("ob-alpha"), make_claim("ob-invented")],
        )
        report = check_record(record, spec)
        self.assertIn("V3-CANDIDATE-UNDECLARED-CLAIM", codes(report))
        self.assertTrue(any("ob-invented" in issue.message for issue in report.issues), report.rendered())

    def test_n1_a6_duplicate_claim_for_one_obligation_is_reported(self):
        """Exactly one claim per obligation — a second answer is a defect, not a refinement."""
        spec = make_spec(
            [make_obligation("ob-alpha")],
            [{"artifact_id": "artifact-guide", "path": "docs/guide.md"}],
        )
        record = make_record(
            spec=spec,
            candidate_ref={"branch": "cand", "commit": FAKE_REV},
            base_revision=FAKE_REV,
            manifest=self._clean_manifest(),
            claims=[
                make_claim("ob-alpha", anchor="## Guide"),
                make_claim("ob-alpha", anchor="## Guide Again"),
            ],
        )
        report = check_record(record, spec)
        self.assertIn("V3-CANDIDATE-DUPLICATE-CLAIM", codes(report))

    def test_n1_a6_expected_artifact_without_a_presence_result_is_reported(self):
        """An expected artifact with no presence result is unreported, not absent-by-default."""
        spec = make_spec(
            [make_obligation("ob-alpha")],
            [
                {"artifact_id": "artifact-guide", "path": "docs/guide.md"},
                {"artifact_id": "artifact-notes", "path": "docs/notes.md"},
            ],
        )
        record = make_record(
            spec=spec,
            candidate_ref={"branch": "cand", "commit": FAKE_REV},
            base_revision=FAKE_REV,
            manifest=self._clean_manifest(
                artifact_results=[{"artifact_id": "artifact-guide", "present": True}]
            ),
            claims=[make_claim("ob-alpha")],
        )
        report = check_record(record, spec)
        self.assertIn("V3-CANDIDATE-ARTIFACT-UNREPORTED", codes(report))
        self.assertTrue(any("artifact-notes" in issue.message for issue in report.issues), report.rendered())

    def test_n1_a6_presence_result_for_an_undeclared_artifact_is_reported(self):
        """Presence reported for something the WorkSpec never declared is a defect."""
        spec = make_spec(
            [make_obligation("ob-alpha")],
            [{"artifact_id": "artifact-guide", "path": "docs/guide.md"}],
        )
        record = make_record(
            spec=spec,
            candidate_ref={"branch": "cand", "commit": FAKE_REV},
            base_revision=FAKE_REV,
            manifest=self._clean_manifest(
                artifact_results=[
                    {"artifact_id": "artifact-guide", "present": True},
                    {"artifact_id": "artifact-smuggled", "present": True},
                ]
            ),
            claims=[make_claim("ob-alpha")],
        )
        report = check_record(record, spec)
        self.assertIn("V3-CANDIDATE-ARTIFACT-UNDECLARED", codes(report))

    def test_n1_a6_every_observed_diff_yields_a_boundary_result(self):
        """A real diff always classifies — CONFORMANT or NONCONFORMANT, never silence."""
        cases = [
            ({"docs/guide.md": "in scope\n"}, "CONFORMANT", []),
            ({"elsewhere/notes.md": "outside\n"}, "NONCONFORMANT", ["elsewhere/notes.md"]),
            ({"docs/private/secret.md": "negative wins\n"}, "NONCONFORMANT", ["docs/private/secret.md"]),
        ]
        for files, expected, offenders in cases:
            with self.subTest(files=sorted(files)):
                with TempRepo({"docs/guide.md": "base\n"}) as repo:
                    candidate = repo.commit_candidate(files)
                    manifest = observe_manifest(
                        repo.root,
                        repo.base,
                        candidate,
                        BOUNDARY,
                        [{"artifact_id": "artifact-guide", "path": "docs/guide.md"}],
                        authored_by=VERIFIER,
                    )
                    self.assertIn("boundary_result", manifest)
                    self.assertIn(manifest["boundary_result"], ("CONFORMANT", "NONCONFORMANT"))
                    self.assertEqual(manifest["boundary_result"], expected)
                    self.assertEqual(manifest.get("out_of_boundary_paths", []), offenders)

                    # Every single observed change is individually accounted for.
                    changes = observe_changes(repo.root, repo.base, candidate)
                    self.assertTrue(changes)
                    for change in changes:
                        conformant, single = evaluate_boundary([change], BOUNDARY)
                        self.assertIn(conformant, ("CONFORMANT", "NONCONFORMANT"))
                        self.assertEqual(
                            change["path"] in offenders,
                            conformant == "NONCONFORMANT",
                            f"{change['path']} was not classified consistently: {single}",
                        )

    def test_n1_a6_deterministic_obligation_without_a_checkresult_is_no_evidence(self):
        """Silence is never success: a bound check with no result is V3-COVERAGE-NO-EVIDENCE."""
        spec = make_spec(
            [
                make_obligation(
                    "ob-alpha",
                    verification_mode="local_check",
                    local_check_refs=["check-guide"],
                )
            ],
            [{"artifact_id": "artifact-guide", "path": "docs/guide.md"}],
        )
        record = make_record(
            spec=spec,
            candidate_ref={"branch": "cand", "commit": FAKE_REV},
            base_revision=FAKE_REV,
            manifest=make_manifest(),
            claims=[make_claim("ob-alpha")],
        )
        report = coverage_report(spec, record, results=())
        self.assertEqual(codes(report), ["V3-COVERAGE-NO-EVIDENCE"])

        # The row renders the absence explicitly rather than leaving the cell blank.
        rows = coverage_rows(spec, record, results=())
        self.assertEqual(rows[0]["checks"], [{"check_id": "check-guide", "result": "NO_RESULT"}])


# ===========================================================================
# N1-A7 — manifest sole author and raw CheckResult ownership
# ===========================================================================


class ManifestOwnershipTests(unittest.TestCase):
    """N1-A7: the executor of a run can never author the manifest about its own work."""

    def _record_with_authors(self, executor: str, manifest_author: str) -> tuple[dict, dict]:
        spec = make_spec(
            [make_obligation("ob-alpha")],
            [{"artifact_id": "artifact-guide", "path": "docs/guide.md"}],
        )
        record = make_record(
            spec=spec,
            candidate_ref={"branch": "cand", "commit": FAKE_REV},
            base_revision=FAKE_REV,
            manifest=make_manifest(authored_by=manifest_author),
            claims=[make_claim("ob-alpha")],
            fulfillment_author=executor,
        )
        return record, spec

    def test_n1_a7_executor_authored_manifest_is_detected(self):
        """Identical author strings on both partitions collapse the ownership split."""
        record, spec = self._record_with_authors("executor agent", "executor agent")
        report = check_record(record, spec)
        self.assertIn("V3-CANDIDATE-EXECUTOR-AUTHORED-MANIFEST", codes(report))

    def test_n1_a7_executor_authored_manifest_detection_ignores_case_and_whitespace(self):
        """Re-spelling the same actor does not buy a second owner."""
        for manifest_author in ("Executor Agent", "  EXECUTOR agent  ", "executor agent\t"):
            with self.subTest(manifest_author=manifest_author):
                record, spec = self._record_with_authors("Executor Agent", manifest_author)
                report = check_record(record, spec)
                self.assertIn("V3-CANDIDATE-EXECUTOR-AUTHORED-MANIFEST", codes(report))

    def test_n1_a7_distinct_authors_pass(self):
        """A genuinely separate diff verifier is accepted."""
        record, spec = self._record_with_authors(EXECUTOR, VERIFIER)
        report = check_record(record, spec)
        self.assertNotIn("V3-CANDIDATE-EXECUTOR-AUTHORED-MANIFEST", codes(report))
        self.assertTrue(report.ok, report.rendered())


# ===========================================================================
# N1-A8 — the closed LocalCheckSpec union
# ===========================================================================


VALID_CONFIGS = {
    "file_exists": {"artifact_id": "artifact-guide"},
    "json_schema": {"subject_path": "docs/subject.json", "schema_path": "docs/schema.json"},
    "markdown_link": {"subject_paths": ["docs/guide.md"]},
    "locator_exists": {"locator": {"path": "docs/guide.md", "anchor": "## Anchored Section"}},
    "command_exit": {"argv": [sys.executable, "-c", "pass"], "cwd": ".", "allowed_exit_codes": [0]},
    "git_diff_boundary": None,
}


def check_doc(check_id: str, kind: str, *, subject_tree: str = "candidate_commit", config=None) -> dict:
    doc = {"check_id": check_id, "kind": kind, "subject_tree": subject_tree}
    if config is not None:
        doc["config"] = config
    return doc


class ClosedCheckUnionTests(unittest.TestCase):
    """N1-A8: six kinds, exact configs, and no representable outcome for an unknown kind."""

    def test_n1_a8_unknown_kind_raises_spec_gap(self):
        """`require_supported_kind` stops the run rather than widening the union."""
        with self.assertRaises(SpecGap):
            require_supported_kind("totally_new_kind")

    def test_n1_a8_run_check_on_unknown_kind_raises_and_returns_nothing(self):
        """An unknown kind has no representable CheckResult, so run_check must raise."""
        with TempRepo({"docs/guide.md": "base\n"}) as repo:
            candidate = repo.commit_candidate({"docs/guide.md": "## Anchored Section\n"})
            ctx = context_for(repo, candidate)
            with self.assertRaises(SpecGap):
                run_check(check_doc("check-x", "totally_new_kind", config={"anything": True}), ctx)

    def test_n1_a8_each_kind_validates_with_its_exact_config(self):
        """The six declared shapes are the six accepted shapes."""
        for kind, config in VALID_CONFIGS.items():
            with self.subTest(kind=kind):
                report = validate("check", check_doc(f"check-{kind.replace('_', '-')}", kind, config=config))
                self.assertTrue(report.ok, report.rendered())

    def test_n1_a8_config_belonging_to_another_kind_is_rejected(self):
        """A json_schema config on a file_exists request is not silently tolerated."""
        for kind, config in VALID_CONFIGS.items():
            if config is None:
                continue
            for other_kind, other_config in VALID_CONFIGS.items():
                if other_kind == kind or other_config is None:
                    continue
                with self.subTest(kind=kind, config_of=other_kind):
                    report = validate(
                        "check",
                        check_doc(f"check-{kind.replace('_', '-')}", kind, config=other_config),
                    )
                    self.assertFalse(report.ok, f"{kind} accepted {other_kind}'s config")

    def test_n1_a8_missing_config_is_rejected_for_every_config_bearing_kind(self):
        """Five of the six kinds cannot resolve a subject without their config."""
        for kind, config in VALID_CONFIGS.items():
            if config is None:
                continue
            with self.subTest(kind=kind):
                report = validate("check", check_doc(f"check-{kind.replace('_', '-')}", kind))
                self.assertFalse(report.ok, f"{kind} was accepted with no config")

    def test_n1_a8_git_diff_boundary_must_carry_no_config(self):
        """Its subjects are all bound at run time, so any config is an over-declaration."""
        self.assertTrue(validate("check", check_doc("check-boundary", "git_diff_boundary")).ok)
        for config in ({"artifact_id": "artifact-guide"}, {}, {"write_scope": ["docs"]}):
            with self.subTest(config=config):
                report = validate("check", check_doc("check-boundary", "git_diff_boundary", config=config))
                self.assertFalse(report.ok, f"git_diff_boundary accepted config {config}")

    def test_n1_a8_command_exit_argv_rejects_shell_metacharacters(self):
        """argv is executed without a shell, so a metacharacter has no meaning it could carry."""
        for metachar in ("$", "`", "|", ";", "&", "<", ">"):
            with self.subTest(metachar=metachar):
                doc = check_doc(
                    "check-command",
                    "command_exit",
                    config={
                        "argv": ["python", f"-c{metachar}pass"],
                        "cwd": ".",
                        "allowed_exit_codes": [0],
                    },
                )
                report = validate("check", doc)
                self.assertFalse(report.ok, f"argv containing {metachar!r} was accepted")

    # --- end-to-end: each kind returns a real PASS and a real FAIL ---

    def _repo(self) -> TempRepo:
        return TempRepo({"docs/guide.md": "base\n"})

    def test_n1_a8_file_exists_runs_pass_and_fail(self):
        """file_exists resolves the WorkSpec artifact path in the candidate tree."""
        with self._repo() as repo:
            candidate = repo.commit_candidate({"docs/guide.md": "## Anchored Section\n"})
            doc = check_doc("check-file-exists", "file_exists", config=VALID_CONFIGS["file_exists"])

            present = run_check(doc, context_for(repo, candidate, artifact_paths={"artifact-guide": "docs/guide.md"}))
            self.assertEqual(present["result"], "PASS")

            absent = run_check(doc, context_for(repo, candidate, artifact_paths={"artifact-guide": "docs/absent.md"}))
            self.assertEqual(absent["result"], "FAIL")

    def test_n1_a8_json_schema_runs_pass_and_fail(self):
        """json_schema validates the candidate's document against the candidate's schema."""
        schema = json.dumps({"type": "object", "required": ["name"], "properties": {"name": {"type": "string"}}})
        with self._repo() as repo:
            candidate = repo.commit_candidate(
                {
                    "docs/schema.json": schema,
                    "docs/subject.json": '{"name": "ok"}',
                    "docs/bad.json": '{"name": 42}',
                }
            )
            ctx = context_for(repo, candidate)

            good = run_check(check_doc("check-json-ok", "json_schema", config=VALID_CONFIGS["json_schema"]), ctx)
            self.assertEqual(good["result"], "PASS")

            bad = run_check(
                check_doc(
                    "check-json-bad",
                    "json_schema",
                    config={"subject_path": "docs/bad.json", "schema_path": "docs/schema.json"},
                ),
                ctx,
            )
            self.assertEqual(bad["result"], "FAIL")

    def test_n1_a8_markdown_link_runs_pass_and_fail(self):
        """markdown_link resolves local links against the candidate tree."""
        with self._repo() as repo:
            candidate = repo.commit_candidate(
                {
                    "docs/guide.md": "## Anchored Section\nsee [notes](notes.md)\n",
                    "docs/notes.md": "notes\n",
                    "docs/broken.md": "see [gone](missing.md)\n",
                }
            )
            ctx = context_for(repo, candidate)

            good = run_check(check_doc("check-links-ok", "markdown_link", config=VALID_CONFIGS["markdown_link"]), ctx)
            self.assertEqual(good["result"], "PASS")

            bad = run_check(
                check_doc("check-links-bad", "markdown_link", config={"subject_paths": ["docs/broken.md"]}),
                ctx,
            )
            self.assertEqual(bad["result"], "FAIL")

    def test_n1_a8_locator_exists_runs_pass_and_fail(self):
        """locator_exists demands a unique anchor in the candidate tree."""
        with self._repo() as repo:
            candidate = repo.commit_candidate({"docs/guide.md": "## Anchored Section\nbody\n"})
            ctx = context_for(repo, candidate)

            good = run_check(
                check_doc("check-locator-ok", "locator_exists", config=VALID_CONFIGS["locator_exists"]), ctx
            )
            self.assertEqual(good["result"], "PASS")

            bad = run_check(
                check_doc(
                    "check-locator-bad",
                    "locator_exists",
                    config={"locator": {"path": "docs/guide.md", "anchor": "## Never Written"}},
                ),
                ctx,
            )
            self.assertEqual(bad["result"], "FAIL")

    def test_n1_a8_git_diff_boundary_runs_pass_and_fail(self):
        """git_diff_boundary classifies the real base..candidate diff."""
        with self._repo() as repo:
            candidate = repo.commit_candidate({"docs/guide.md": "in scope\n"})
            good = run_check(check_doc("check-boundary-ok", "git_diff_boundary"), context_for(repo, candidate))
            self.assertEqual(good["result"], "PASS")

        with self._repo() as repo:
            candidate = repo.commit_candidate({"elsewhere/notes.md": "outside\n"})
            bad = run_check(check_doc("check-boundary-bad", "git_diff_boundary"), context_for(repo, candidate))
            self.assertEqual(bad["result"], "FAIL")
            self.assertIn("elsewhere/notes.md", bad["detail"])

    def test_n1_a8_command_exit_runs_pass_and_fail(self):
        """command_exit records the real process exit code against the allowed set."""
        with self._repo() as repo:
            candidate = repo.commit_candidate({"docs/guide.md": "## Anchored Section\n"})
            ctx = context_for(repo, candidate)

            good = run_check(
                check_doc(
                    "check-command-ok",
                    "command_exit",
                    config={
                        "argv": [sys.executable, "-c", "raise SystemExit(0)"],
                        "cwd": ".",
                        "allowed_exit_codes": [0],
                    },
                ),
                ctx,
            )
            self.assertEqual(good["result"], "PASS")
            self.assertEqual(good["exit_code"], 0)

            bad = run_check(
                check_doc(
                    "check-command-bad",
                    "command_exit",
                    config={
                        "argv": [sys.executable, "-c", "raise SystemExit(3)"],
                        "cwd": ".",
                        "allowed_exit_codes": [0],
                    },
                ),
                ctx,
            )
            self.assertEqual(bad["result"], "FAIL")
            self.assertEqual(bad["exit_code"], 3)


class EvidenceRefDigestNarrowingTests(unittest.TestCase):
    """The evidence file a check writes is pointed at by path alone (2026-07-29 narrowing).

    A `CheckResult.evidence_ref` names a file this same run just produced, so a digest it
    computes over its own output records nothing any actor is bound by. The digest is
    therefore no longer written — and the result must still be a valid `check_result`,
    because `pointerRef` requires only `path`. That second half is what makes this a
    deletion rather than a break: nothing downstream has to change to accept it.
    """

    def _repo(self):
        return TempRepo({"docs/guide.md": "base\n"})

    def test_written_evidence_is_pointed_at_by_path_alone(self):
        with self._repo() as repo:
            candidate = repo.commit_candidate({"docs/guide.md": "## Anchored Section\n"})
            ctx = context_for(repo, candidate, evidence_dir="runs/run-one/evidence")
            result = run_check(
                check_doc(
                    "check-command-evidence",
                    "command_exit",
                    config={
                        "argv": [sys.executable, "-c", "print('hello from the check')"],
                        "cwd": ".",
                        "allowed_exit_codes": [0],
                    },
                ),
                ctx,
            )
            self.assertEqual(result["result"], "PASS")
            self.assertEqual(
                result["evidence_ref"],
                {"path": "runs/run-one/evidence/check-command-evidence.out.txt"},
            )
            # The evidence itself is still written — the narrowing dropped the digest, not
            # the file, so a reviewer can still read what the command printed.
            written = (repo.root / "runs/run-one/evidence"
                       / "check-command-evidence.out.txt").read_text(encoding="utf-8")
            self.assertIn("hello from the check", written)

    def test_a_result_carrying_that_ref_is_still_schema_valid(self):
        with self._repo() as repo:
            candidate = repo.commit_candidate({"docs/guide.md": "## Anchored Section\n"})
            ctx = context_for(repo, candidate, evidence_dir="runs/run-one/evidence")
            result = run_check(
                check_doc(
                    "check-command-schema",
                    "command_exit",
                    config={
                        "argv": [sys.executable, "-c", "raise SystemExit(0)"],
                        "cwd": ".",
                        "allowed_exit_codes": [0],
                    },
                ),
                ctx,
            )
            self.assertNotIn("digest_sha256", result["evidence_ref"])
            report = validate("check_result", result)
            self.assertTrue(report.ok, "; ".join(report.rendered()))


class MarkdownLinkEscapeTests(unittest.TestCase):
    """A local link resolving OUTSIDE the repository is broken, never folded back inside.

    The defect: `..` segments cancelled each other, so from `docs/guide.md` the link
    `../../../README.md` — two levels *above* the repository root — normalized to the root's
    own `README.md` and the check reported PASS. An escaping link names a target no tree of
    the candidate contains, so a PASS there certifies something never observed.
    """

    def test_a_link_resolving_above_the_repository_root_is_broken(self):
        with TempRepo({"README.md": "outside the candidate's reach\n"}) as repo:
            candidate = repo.commit_candidate({"docs/guide.md": "see [escape](../../../README.md)\n"})
            result = run_check(
                check_doc("check-escape", "markdown_link", config={"subject_paths": ["docs/guide.md"]}),
                context_for(repo, candidate),
            )
            self.assertEqual(result["result"], "FAIL")
            self.assertIn(
                "docs/guide.md -> ../../../README.md (resolves outside the repository)",
                result["detail"],
            )

    def test_an_upward_link_that_stays_inside_still_passes(self):
        """Negative control: ordinary `../` links inside the tree must keep resolving."""
        with TempRepo({"README.md": "base\n"}) as repo:
            candidate = repo.commit_candidate(
                {"docs/guide.md": "target\n", "docs/sub/note.md": "see [up](../guide.md)\n"}
            )
            result = run_check(
                check_doc("check-inside", "markdown_link", config={"subject_paths": ["docs/sub/note.md"]}),
                context_for(repo, candidate),
            )
            self.assertEqual(result["result"], "PASS")


class RunAllStopsAtTheFirstGapTests(unittest.TestCase):
    """`run_all` stops at the first `SPEC_GAP` result instead of finishing the order.

    The defect: the gap result was collected and the loop ran to completion, so every later
    check — `command_exit` among them, which starts a real process — still executed against a
    plan already known to be uninterpretable. Only a side effect can witness that: the raised
    `SpecGap` looks identical whether or not the rest of the order ran.
    """

    #: Written with `__import__` rather than an `import` statement because the LocalCheckSpec
    #: schema rejects `;` in any argv element — argv is never interpolated through a shell.
    WRITE_SENTINEL = "__import__('pathlib').Path(__import__('sys').argv[1]).write_text('ran')"

    def _sentinel_check(self, check_id: str, sentinel: pathlib.Path) -> dict:
        return check_doc(
            check_id,
            "command_exit",
            subject_tree="worktree",
            config={
                "argv": [sys.executable, "-c", self.WRITE_SENTINEL, str(sentinel)],
                "cwd": ".",
                "allowed_exit_codes": [0],
            },
        )

    def test_a_check_ordered_after_a_gap_never_runs(self):
        with tempfile.TemporaryDirectory() as scratch:
            sentinel = pathlib.Path(scratch) / "the-command-ran"
            with TempRepo({"README.md": "base\n"}) as repo:
                candidate = repo.commit_candidate({"docs/guide.md": "## Anchored Section\n"})
                gap = check_doc(
                    "check-gap",
                    "json_schema",
                    config={"subject_path": "docs/absent.json", "schema_path": "docs/absent.json"},
                )
                after = self._sentinel_check("check-after-the-gap", sentinel)
                with self.assertRaises(SpecGap):
                    run_all(
                        {"check-gap": gap, "check-after-the-gap": after},
                        ["check-gap", "check-after-the-gap"],
                        context_for(repo, candidate),
                    )
                self.assertFalse(sentinel.exists(), "a check ordered after the gap still ran")

    def test_the_whole_order_runs_when_no_request_is_uninterpretable(self):
        """Negative control: without a gap the same command must still run to completion."""
        with tempfile.TemporaryDirectory() as scratch:
            sentinel = pathlib.Path(scratch) / "the-command-ran"
            with TempRepo({"README.md": "base\n"}) as repo:
                candidate = repo.commit_candidate({"docs/guide.md": "## Anchored Section\n"})
                results = run_all(
                    {"check-only": self._sentinel_check("check-only", sentinel)},
                    ["check-only"],
                    context_for(repo, candidate),
                )
                self.assertEqual([result["result"] for result in results], ["PASS"])
                self.assertTrue(sentinel.exists())


class CommandTimeoutTests(unittest.TestCase):
    """A command that never finishes stops the run instead of hanging it forever.

    `subprocess.run` without `timeout` waits indefinitely, so one wedged process froze the
    whole assurance run with no result and no evidence. The outcome is `SPEC_GAP`, not
    `FAIL`: the schema requires an exact `exit_code` on every command_exit PASS or FAIL, a
    killed process has none, and inventing one would invent evidence the run never observed.
    """

    def _check(self, check_id: str, code: str) -> dict:
        return check_doc(
            check_id,
            "command_exit",
            subject_tree="worktree",
            config={"argv": [sys.executable, "-c", code], "cwd": ".", "allowed_exit_codes": [0]},
        )

    def test_a_wedged_command_is_killed_at_the_ceiling_and_reported_as_a_gap(self):
        with TempRepo({"README.md": "base\n"}) as repo:
            candidate = repo.commit_candidate({"docs/guide.md": "## Anchored Section\n"})
            started = time.monotonic()
            with mock.patch.object(checks_module, "COMMAND_TIMEOUT_SECONDS", 1):
                # `__import__` again: the schema rejects `;` in argv (see WRITE_SENTINEL).
                result = run_check(self._check("check-wedged", "__import__('time').sleep(20)"),
                                   context_for(repo, candidate))
            elapsed = time.monotonic() - started
            self.assertEqual(result["result"], "SPEC_GAP")
            self.assertIn("did not finish within 1s", result["detail"])
            self.assertNotIn("exit_code", result)
            self.assertLess(elapsed, 15, "the process outlived the ceiling that was meant to kill it")

    def test_a_command_finishing_under_the_ceiling_is_unaffected(self):
        """Negative control: the ceiling must not turn a fast command into a gap."""
        with TempRepo({"README.md": "base\n"}) as repo:
            candidate = repo.commit_candidate({"docs/guide.md": "## Anchored Section\n"})
            with mock.patch.object(checks_module, "COMMAND_TIMEOUT_SECONDS", 30):
                result = run_check(self._check("check-fast", "raise SystemExit(0)"),
                                   context_for(repo, candidate))
            self.assertEqual(result["result"], "PASS")
            self.assertEqual(result["exit_code"], 0)

    def test_the_shipped_ceiling_is_fixed_and_not_a_request_field(self):
        """A per-request knob would let the request that hangs buy its own patience."""
        self.assertEqual(checks_module.COMMAND_TIMEOUT_SECONDS, 600)
        properties = load_json(SCHEMA_DIR / "local-check-spec.schema.json")["$defs"][
            "commandExitConfig"
        ]["properties"]
        self.assertEqual(sorted(properties), ["allowed_exit_codes", "argv", "cwd", "subject_paths"])


# ===========================================================================
# N1-A9 — the seven named negatives
# ===========================================================================


class NamedNegativeTests(unittest.TestCase):
    """N1-A9: the seven failure classes v3 exists to detect, each against a real repository."""

    # --- negative 1: omission ---

    def test_n1_a9_negative1_omission_is_detected(self):
        """An obligation with no fulfillment claim is reported against a real candidate."""
        with TempRepo({"docs/guide.md": "base\n"}) as repo:
            candidate = repo.commit_candidate({"docs/guide.md": "## Guide\ncandidate\n"})
            spec = make_spec(
                [make_obligation("ob-guide"), make_obligation("ob-forgotten")],
                [{"artifact_id": "artifact-guide", "path": "docs/guide.md"}],
            )
            manifest = observe_manifest(
                repo.root, repo.base, candidate, spec["change_boundary"], spec["expected_artifacts"],
                authored_by=VERIFIER,
            )
            record = make_record(
                spec=spec,
                candidate_ref=repo.candidate_ref(candidate),
                base_revision=repo.base,
                manifest=manifest,
                claims=[make_claim("ob-guide")],  # ob-forgotten was never answered
            )
            report = check_record(record, spec)
            self.assertIn("V3-CANDIDATE-OBLIGATION-OMITTED", codes(report))
            self.assertTrue(any("ob-forgotten" in i.message for i in report.issues), report.rendered())

    # --- negative 2: stale locator ---

    def test_n1_a9_negative2_stale_locator_is_detected(self):
        """An IMPLEMENTED claim whose anchor is absent from the candidate does not resolve."""
        with TempRepo({"docs/guide.md": "base\n"}) as repo:
            candidate = repo.commit_candidate({"docs/guide.md": "## Guide\nbody\n"})
            spec = make_spec(
                [make_obligation("ob-guide")],
                [{"artifact_id": "artifact-guide", "path": "docs/guide.md"}],
            )
            record = make_record(
                spec=spec,
                candidate_ref=repo.candidate_ref(candidate),
                base_revision=repo.base,
                manifest=make_manifest(),
                # The defect: the claim points at an anchor the candidate never got.
                claims=[make_claim("ob-guide", path="docs/guide.md", anchor="## Section That Was Renamed")],
            )
            reader = CandidateTreeReader(repo.root, candidate)
            self.assertEqual(resolve_locator(reader, {"path": "docs/guide.md", "anchor": "## Section That Was Renamed"}), 0)

            report = check_locators(record, reader)
            self.assertEqual(codes(report), ["V3-CANDIDATE-LOCATOR-UNRESOLVED"])
            self.assertIn("does not resolve", report.issues[0].message)

    def test_n1_a9_negative2_ambiguous_locator_is_detected(self):
        """An anchor occurring twice identifies no location, so it fails just as hard."""
        with TempRepo({"docs/guide.md": "base\n"}) as repo:
            candidate = repo.commit_candidate(
                {"docs/guide.md": "## Guide\nfirst\n\n## Guide\nsecond\n"}
            )
            spec = make_spec(
                [make_obligation("ob-guide")],
                [{"artifact_id": "artifact-guide", "path": "docs/guide.md"}],
            )
            record = make_record(
                spec=spec,
                candidate_ref=repo.candidate_ref(candidate),
                base_revision=repo.base,
                manifest=make_manifest(),
                claims=[make_claim("ob-guide", anchor="## Guide")],
            )
            reader = CandidateTreeReader(repo.root, candidate)
            self.assertEqual(resolve_locator(reader, {"path": "docs/guide.md", "anchor": "## Guide"}), 2)

            report = check_locators(record, reader)
            self.assertEqual(codes(report), ["V3-CANDIDATE-LOCATOR-UNRESOLVED"])
            self.assertIn("ambiguous", report.issues[0].message)

    def test_n1_a9_negative2_resolving_locator_passes(self):
        """A locator that occurs exactly once is the only accepted case."""
        with TempRepo({"docs/guide.md": "base\n"}) as repo:
            candidate = repo.commit_candidate({"docs/guide.md": "## Guide\nbody\n"})
            spec = make_spec(
                [make_obligation("ob-guide")],
                [{"artifact_id": "artifact-guide", "path": "docs/guide.md"}],
            )
            record = make_record(
                spec=spec,
                candidate_ref=repo.candidate_ref(candidate),
                base_revision=repo.base,
                manifest=make_manifest(),
                claims=[make_claim("ob-guide", anchor="## Guide")],
            )
            report = check_locators(record, CandidateTreeReader(repo.root, candidate))
            self.assertTrue(report.ok, report.rendered())

    # --- negative 3: missing artifact ---

    def test_n1_a9_negative3_missing_expected_artifact_is_detected(self):
        """An expected artifact absent from the candidate tree is recorded present: false."""
        with TempRepo({"docs/guide.md": "base\n"}) as repo:
            candidate = repo.commit_candidate({"docs/guide.md": "## Guide\ncandidate\n"})
            spec = make_spec(
                [make_obligation("ob-guide")],
                [
                    {"artifact_id": "artifact-guide", "path": "docs/guide.md"},
                    # The defect: the candidate never produced this declared artifact.
                    {"artifact_id": "artifact-summary", "path": "docs/summary.md"},
                ],
            )
            manifest = observe_manifest(
                repo.root, repo.base, candidate, spec["change_boundary"], spec["expected_artifacts"],
                authored_by=VERIFIER,
            )
            presence = {entry["artifact_id"]: entry["present"] for entry in manifest["expected_artifact_results"]}
            self.assertEqual(presence, {"artifact-guide": True, "artifact-summary": False})

            record = make_record(
                spec=spec,
                candidate_ref=repo.candidate_ref(candidate),
                base_revision=repo.base,
                manifest=manifest,
                claims=[make_claim("ob-guide")],
            )
            report = check_record(record, spec)
            self.assertIn("V3-CANDIDATE-ARTIFACT-MISSING", codes(report))
            self.assertTrue(any("artifact-summary" in i.message for i in report.issues), report.rendered())

    def test_n1_a9_negative3_unchanged_preexisting_artifact_is_present(self):
        """Presence is observed in the candidate tree, not in the diff — no false blocker."""
        with TempRepo({"docs/guide.md": "base\n", "docs/legacy.md": "untouched\n"}) as repo:
            candidate = repo.commit_candidate({"docs/guide.md": "## Guide\ncandidate\n"})
            manifest = observe_manifest(
                repo.root, repo.base, candidate, BOUNDARY,
                [{"artifact_id": "artifact-legacy", "path": "docs/legacy.md"}],
                authored_by=VERIFIER,
            )
            self.assertEqual(manifest["expected_artifact_results"], [{"artifact_id": "artifact-legacy", "present": True}])

    # --- negative 4: wrong-candidate evidence ---

    def test_n1_a9_negative4_wrong_candidate_evidence_is_detected(self):
        """A CheckResult that certified another commit cannot support this record."""
        with TempRepo({"docs/guide.md": "base\n"}) as repo:
            first = repo.commit_candidate({"docs/guide.md": "## Anchored Section\nfirst\n"})
            second = repo.commit_candidate({"docs/guide.md": "## Anchored Section\nsecond\n"}, branch="cand")

            # A real result, honestly produced — but about the FIRST candidate.
            stale_result = run_check(
                check_doc("check-locator", "locator_exists", config=VALID_CONFIGS["locator_exists"]),
                context_for(repo, first),
            )
            self.assertEqual(stale_result["result"], "PASS")

            spec = make_spec(
                [
                    make_obligation(
                        "ob-guide", verification_mode="local_check", local_check_refs=["check-locator"]
                    )
                ],
                [{"artifact_id": "artifact-guide", "path": "docs/guide.md"}],
            )
            record = make_record(
                spec=spec,
                candidate_ref=repo.candidate_ref(second),  # the record reports on the SECOND candidate
                base_revision=repo.base,
                manifest=make_manifest(),
                claims=[make_claim("ob-guide", anchor="## Anchored Section")],
            )
            report = coverage_report(spec, record, results=[stale_result])
            self.assertIn("V3-COVERAGE-WRONG-CANDIDATE", codes(report))
            self.assertNotEqual(first, second)

    # --- negative 5: out-of-boundary diff ---

    def test_n1_a9_negative5_path_outside_write_scope_is_nonconformant(self):
        """A real commit touching a path outside write_scope is NONCONFORMANT, and the check FAILs."""
        with TempRepo({"docs/guide.md": "base\n"}) as repo:
            candidate = repo.commit_candidate(
                {"docs/guide.md": "## Guide\nok\n", "elsewhere/rogue.md": "outside the scope\n"}
            )
            manifest = observe_manifest(
                repo.root, repo.base, candidate, BOUNDARY,
                [{"artifact_id": "artifact-guide", "path": "docs/guide.md"}],
                authored_by=VERIFIER,
            )
            self.assertEqual(manifest["boundary_result"], "NONCONFORMANT")
            self.assertEqual(manifest["out_of_boundary_paths"], ["elsewhere/rogue.md"])

            result = run_check(check_doc("check-boundary", "git_diff_boundary"), context_for(repo, candidate))
            self.assertEqual(result["result"], "FAIL")
            self.assertIn("elsewhere/rogue.md", result["detail"])

            spec = make_spec(
                [make_obligation("ob-guide")],
                [{"artifact_id": "artifact-guide", "path": "docs/guide.md"}],
            )
            record = make_record(
                spec=spec,
                candidate_ref=repo.candidate_ref(candidate),
                base_revision=repo.base,
                manifest=manifest,
                claims=[make_claim("ob-guide")],
            )
            self.assertIn("V3-CANDIDATE-BOUNDARY-NONCONFORMANT", codes(check_record(record, spec)))

    def test_n1_a9_negative5_negative_boundary_wins_over_write_scope(self):
        """A path inside write_scope but also inside `out` is still NONCONFORMANT."""
        with TempRepo({"docs/guide.md": "base\n"}) as repo:
            # docs/private is inside write_scope 'docs' AND inside out 'docs/private'.
            candidate = repo.commit_candidate({"docs/private/secret.md": "excluded subtree\n"})
            manifest = observe_manifest(
                repo.root, repo.base, candidate, BOUNDARY,
                [{"artifact_id": "artifact-guide", "path": "docs/guide.md"}],
                authored_by=VERIFIER,
            )
            self.assertTrue(covered_by("docs/private/secret.md", BOUNDARY["write_scope"]))
            self.assertEqual(manifest["boundary_result"], "NONCONFORMANT")
            self.assertEqual(manifest["out_of_boundary_paths"], ["docs/private/secret.md"])

            result = run_check(check_doc("check-boundary", "git_diff_boundary"), context_for(repo, candidate))
            self.assertEqual(result["result"], "FAIL")
            self.assertIn("docs/private/secret.md", result["detail"])

    # --- negative 6: control file in payload (see N1-A5 for the full fixture) ---

    def test_n1_a9_negative6_control_file_in_payload_is_detected(self):
        """The named negative, restated: evidence about the candidate inside the candidate."""
        with TempRepo({"docs/guide.md": "base\n"}) as repo:
            candidate = repo.commit_candidate(
                {"docs/guide.md": "## Guide\nok\n", "control/coverage.json": "{}\n"}
            )
            spec = make_spec(
                [make_obligation("ob-guide")],
                [{"artifact_id": "artifact-guide", "path": "docs/guide.md"}],
                boundary={"write_scope": ["docs", "control"], "out": ["docs/private"]},
            )
            manifest = observe_manifest(
                repo.root, repo.base, candidate, spec["change_boundary"], spec["expected_artifacts"],
                authored_by=VERIFIER,
            )
            record = make_record(
                spec=spec,
                candidate_ref=repo.candidate_ref(candidate),
                base_revision=repo.base,
                manifest=manifest,
                claims=[make_claim("ob-guide")],
                control_root="control",
            )
            self.assertEqual(codes(check_record(record, spec)), ["V3-CANDIDATE-CONTROL-FILE-IN-PAYLOAD"])

    # --- negative 7: executor-authored result ---

    def test_n1_a9_negative7_executor_authored_manifest_is_detected(self):
        """The record half of the ownership negative (see N1-A7 for the case-folding cases)."""
        spec = make_spec(
            [make_obligation("ob-alpha")],
            [{"artifact_id": "artifact-guide", "path": "docs/guide.md"}],
        )
        record = make_record(
            spec=spec,
            candidate_ref={"branch": "cand", "commit": FAKE_REV},
            base_revision=FAKE_REV,
            manifest=make_manifest(authored_by=EXECUTOR),
            claims=[make_claim("ob-alpha")],
            fulfillment_author=EXECUTOR,
        )
        self.assertEqual(codes(check_record(record, spec)), ["V3-CANDIDATE-EXECUTOR-AUTHORED-MANIFEST"])

    def _result_and_record(self, repo: TempRepo, candidate: str, verified_by: str):
        """A PASSing check plus the record whose executor may or may not be its verifier."""
        result = run_check(
            check_doc("check-locator", "locator_exists", config=VALID_CONFIGS["locator_exists"]),
            context_for(repo, candidate, verified_by=verified_by),
        )
        self.assertEqual(result["result"], "PASS")
        spec = make_spec(
            [make_obligation("ob-guide", verification_mode="local_check", local_check_refs=["check-locator"])],
            [{"artifact_id": "artifact-guide", "path": "docs/guide.md"}],
        )
        record = make_record(
            spec=spec,
            candidate_ref=repo.candidate_ref(candidate),
            base_revision=repo.base,
            manifest=make_manifest(),
            claims=[make_claim("ob-guide", anchor="## Anchored Section")],
            fulfillment_author=EXECUTOR,
        )
        return result, record, spec

    def test_n1_a9_negative7_executor_authored_checkresult_is_visible_and_reported(self):
        """A CheckResult whose `verified_by` is the executor of the same run is rejected.

        The result still PASSes as an oracle — the defect is not the outcome but the
        ownership, which only becomes visible where the executor's identity and the results
        meet, i.e. in the coverage join.
        """
        with TempRepo({"docs/guide.md": "base\n"}) as repo:
            candidate = repo.commit_candidate({"docs/guide.md": "## Anchored Section\n"})
            # The defect: the executor of the run is also named as the verifier.
            result, record, spec = self._result_and_record(repo, candidate, verified_by=EXECUTOR)

            self.assertEqual(result["verified_by"], EXECUTOR)
            self.assertEqual(record["fulfillment"]["authored_by"], result["verified_by"])
            self.assertEqual(
                codes(coverage_report(spec, record, results=[result])),
                ["V3-COVERAGE-EXECUTOR-AUTHORED-RESULT"],
            )

    def test_n1_a9_negative7_executor_authored_checkresult_detection_ignores_case(self):
        """Re-spelling the executor's name does not buy a second owner here either."""
        with TempRepo({"docs/guide.md": "base\n"}) as repo:
            candidate = repo.commit_candidate({"docs/guide.md": "## Anchored Section\n"})
            result, record, spec = self._result_and_record(repo, candidate, verified_by="  EXECUTOR Agent ")
            self.assertEqual(
                codes(coverage_report(spec, record, results=[result])),
                ["V3-COVERAGE-EXECUTOR-AUTHORED-RESULT"],
            )

    def test_n1_a9_negative7_distinct_verifier_is_not_reported(self):
        """A genuinely separate deterministic verifier owns its result cleanly."""
        with TempRepo({"docs/guide.md": "base\n"}) as repo:
            candidate = repo.commit_candidate({"docs/guide.md": "## Anchored Section\n"})
            result, record, spec = self._result_and_record(repo, candidate, verified_by=VERIFIER)
            self.assertEqual(codes(coverage_report(spec, record, results=[result])), [])


# ===========================================================================
# R1 — observed-tree recording (carried forward from V3-N0)
# ===========================================================================


class ObservedTreeTests(unittest.TestCase):
    """R1: the wrong-subject class — a result must say which tree it actually read."""

    def test_r1_every_checkresult_records_kind_and_revision(self):
        """Observed-tree disclosure is present on every result the six kinds produce."""
        schema = json.dumps({"type": "object"})
        with TempRepo({"docs/guide.md": "base\n"}) as repo:
            candidate = repo.commit_candidate(
                {
                    "docs/guide.md": "## Anchored Section\nsee [notes](notes.md)\n",
                    "docs/notes.md": "notes\n",
                    "docs/schema.json": schema,
                    "docs/subject.json": "{}",
                }
            )
            ctx = context_for(repo, candidate, artifact_paths={"artifact-guide": "docs/guide.md"})
            for kind, config in VALID_CONFIGS.items():
                with self.subTest(kind=kind):
                    doc = check_doc(f"check-{kind.replace('_', '-')}", kind, config=config)
                    result = run_check(doc, ctx)
                    self.assertIn("observed_tree", result)
                    self.assertEqual(result["observed_tree"]["kind"], "candidate_commit")
                    self.assertEqual(result["observed_tree"]["revision"], candidate)

    def test_r1_candidate_subject_kind_declaring_worktree_returns_wrong_subject(self):
        """The exact result value must be WRONG_SUBJECT — a PASS here would fail this test."""
        schema = json.dumps({"type": "object"})
        with TempRepo({"docs/guide.md": "base\n"}) as repo:
            candidate = repo.commit_candidate(
                {
                    "docs/guide.md": "## Anchored Section\nsee [notes](notes.md)\n",
                    "docs/notes.md": "notes\n",
                    "docs/schema.json": schema,
                    "docs/subject.json": "{}",
                }
            )
            ctx = context_for(repo, candidate, artifact_paths={"artifact-guide": "docs/guide.md"})
            self.assertEqual(len(CANDIDATE_SUBJECT_KINDS), 5)
            for kind in sorted(CANDIDATE_SUBJECT_KINDS):
                with self.subTest(kind=kind):
                    doc = check_doc(
                        f"check-{kind.replace('_', '-')}",
                        kind,
                        subject_tree="worktree",
                        config=VALID_CONFIGS[kind],
                    )
                    result = run_check(doc, ctx)
                    self.assertEqual(result["result"], "WRONG_SUBJECT")
                    self.assertEqual(result["observed_tree"]["kind"], "worktree")

    def test_r1_candidate_reader_does_not_see_uncommitted_worktree_bytes(self):
        """The sharp case: content on disk but not in the candidate is invisible to the check."""
        with TempRepo({"docs/guide.md": "base\n"}) as repo:
            candidate = repo.commit_candidate({"docs/guide.md": "## Committed Section\nbody\n"})
            # Written to the working tree and deliberately NOT committed.
            repo.write({"docs/guide.md": "## Committed Section\n## Uncommitted Section\nbody\n"})

            candidate_bytes = CandidateTreeReader(repo.root, candidate).read("docs/guide.md")
            worktree_bytes = WorktreeReader(repo.root).read("docs/guide.md")
            self.assertIsNotNone(candidate_bytes)
            self.assertIsNotNone(worktree_bytes)
            self.assertNotEqual(candidate_bytes, worktree_bytes)
            self.assertNotIn(b"## Uncommitted Section", candidate_bytes)
            self.assertIn(b"## Uncommitted Section", worktree_bytes)

            # A candidate-subject check therefore reports the anchor as unresolved.
            result = run_check(
                check_doc(
                    "check-uncommitted",
                    "locator_exists",
                    config={"locator": {"path": "docs/guide.md", "anchor": "## Uncommitted Section"}},
                ),
                context_for(repo, candidate),
            )
            self.assertEqual(result["result"], "FAIL")
            self.assertEqual(result["observed_tree"]["revision"], candidate)

    def test_r1_command_exit_on_a_different_head_reads_candidate_bytes(self):
        """A candidate-declared command observes the exact candidate even after HEAD moved.

        The probe exits 0 only if the file it reads carries the candidate's bytes; both the
        checkout HEAD and the working tree carry different bytes, so a command that ran
        against either would exit 7 and this test would fail. This is the capability whose
        absence was `issue-p3-corr-command-exit-subject-tree`: before materialization, this
        exact request was refused as WRONG_SUBJECT and no check kind could decide it.
        """
        with TempRepo({"docs/guide.md": "base\n"}) as repo:
            candidate = repo.commit_candidate({"docs/guide.md": "candidate bytes\n"})
            repo.write({"docs/guide.md": "later bytes\n"})
            moved_head = repo.commit_all("move HEAD past the candidate")
            self.assertNotEqual(moved_head, candidate)

            probe = "exit(0 if open('docs/guide.md').read() == 'candidate bytes\\n' else 7)"
            doc = check_doc(
                "check-command",
                "command_exit",
                config={
                    "argv": [sys.executable, "-c", probe],
                    "cwd": ".",
                    "allowed_exit_codes": [0],
                },
            )
            result = run_check(doc, context_for(repo, candidate))
            self.assertEqual(result["result"], "PASS")
            self.assertEqual(result["exit_code"], 0)
            self.assertEqual(
                result["observed_tree"], {"kind": "candidate_commit", "revision": candidate}
            )

    def test_r1_command_exit_on_the_candidate_head_is_honoured(self):
        """The request also passes when the checkout HEAD happens to be the candidate."""
        with TempRepo({"docs/guide.md": "base\n"}) as repo:
            candidate = repo.commit_candidate({"docs/guide.md": "candidate bytes\n"})
            self.assertEqual(repo.head(), candidate)
            result = run_check(
                check_doc(
                    "check-command",
                    "command_exit",
                    config={
                        "argv": [sys.executable, "-c", "raise SystemExit(0)"],
                        "cwd": ".",
                        "allowed_exit_codes": [0],
                    },
                ),
                context_for(repo, candidate),
            )
            self.assertEqual(result["result"], "PASS")

    def test_r1_coverage_report_surfaces_wrong_subject(self):
        """A WRONG_SUBJECT result is reported by the join, never absorbed as a soft finding."""
        with TempRepo({"docs/guide.md": "base\n"}) as repo:
            candidate = repo.commit_candidate({"docs/guide.md": "## Anchored Section\n"})
            result = run_check(
                check_doc(
                    "check-locator",
                    "locator_exists",
                    subject_tree="worktree",
                    config=VALID_CONFIGS["locator_exists"],
                ),
                context_for(repo, candidate),
            )
            self.assertEqual(result["result"], "WRONG_SUBJECT")

            spec = make_spec(
                [make_obligation("ob-guide")],  # review_only, so no NO-EVIDENCE noise
                [{"artifact_id": "artifact-guide", "path": "docs/guide.md"}],
            )
            record = make_record(
                spec=spec,
                candidate_ref=repo.candidate_ref(candidate),
                base_revision=repo.base,
                manifest=make_manifest(),
                claims=[make_claim("ob-guide", anchor="## Anchored Section")],
            )
            report = coverage_report(spec, record, results=[result])
            self.assertEqual(codes(report), ["V3-COVERAGE-WRONG-SUBJECT"])

    def test_r1_check_locators_refuses_a_worktree_reader(self):
        """Locator resolution through the working tree would certify bytes the candidate lacks."""
        with TempRepo({"docs/guide.md": "base\n"}) as repo:
            candidate = repo.commit_candidate({"docs/guide.md": "## Guide\n"})
            spec = make_spec(
                [make_obligation("ob-guide")],
                [{"artifact_id": "artifact-guide", "path": "docs/guide.md"}],
            )
            record = make_record(
                spec=spec,
                candidate_ref=repo.candidate_ref(candidate),
                base_revision=repo.base,
                manifest=make_manifest(),
                claims=[make_claim("ob-guide", anchor="## Guide")],
            )
            report = check_locators(record, WorktreeReader(repo.root))
            self.assertEqual(codes(report), ["V3-CANDIDATE-WRONG-SUBJECT"])


# ===========================================================================
# Candidate materialization for command_exit (issue-p3-corr-command-exit-subject-tree)
# ===========================================================================


class CommandExitMaterializationTests(unittest.TestCase):
    """A candidate-declared command runs inside a materialization of the exact candidate.

    Closes the class `issue-p3-corr-command-exit-subject-tree` witnessed: no check kind
    could count or diff files in the payload candidate, because `command_exit` demanded
    checkout HEAD == candidate — a state the same-branch evidence-commit topology never
    produces. The read-your-own-bytes positive case lives in `ObservedTreeTests`
    (`test_r1_command_exit_on_a_different_head_reads_candidate_bytes`); this class covers
    the counting class itself, cleanup, scoring, and the untouched worktree-declared path.

    Nothing here asserts that a command left the materialization undisturbed. A post-run
    drift check was written, reviewed and removed: `materialized_candidate`'s docstring
    records the four demonstrated evasions and why the gap is a permanent endpoint rather
    than debt. A test pinning the resulting behaviour would be encoding a ceiling as an
    expectation, so the ceiling is stated where the mechanism is, not asserted here.
    """

    def _moved_head_repo(self) -> tuple[TempRepo, str]:
        """A repo whose candidate holds 3 docs/*.md while HEAD and the worktree hold 2."""
        repo = TempRepo({"docs/guide.md": "base\n"})
        self.addCleanup(repo.cleanup)
        candidate = repo.commit_candidate(
            {"docs/notes.md": "notes\n", "docs/extra.md": "extra\n"}
        )
        repo.delete("docs/extra.md")
        moved_head = repo.commit_all("drop extra.md after the candidate")
        assert moved_head != candidate
        return repo, candidate

    def _run(self, repo: TempRepo, candidate: str, probe: str, *, subject_tree: str = "candidate_commit"):
        return run_check(
            check_doc(
                "check-command",
                "command_exit",
                subject_tree=subject_tree,
                config={
                    "argv": [sys.executable, "-c", probe],
                    "cwd": ".",
                    "allowed_exit_codes": [0],
                },
            ),
            context_for(repo, candidate),
        )

    def test_a_counting_command_observes_the_candidate_file_set(self):
        """The motivating class: the count that decides is the candidate's, nobody else's.

        The candidate holds 3 docs/*.md; HEAD and the working tree hold 2. Exit 0 requires
        counting 3, so a command that observed any tree but the candidate fails this check.
        """
        repo, candidate = self._moved_head_repo()
        probe = "exit(0 if len(__import__('glob').glob('docs/*.md')) == 3 else 9)"
        result = self._run(repo, candidate, probe)
        self.assertEqual(result["result"], "PASS")
        self.assertEqual(result["exit_code"], 0)
        self.assertEqual(
            result["observed_tree"], {"kind": "candidate_commit", "revision": candidate}
        )

    def test_a_failing_command_still_reports_fail_with_its_exit_code(self):
        """Materialization changes where the command runs, never how its outcome is scored."""
        repo, candidate = self._moved_head_repo()
        result = self._run(repo, candidate, "exit(5)")
        self.assertEqual(result["result"], "FAIL")
        self.assertEqual(result["exit_code"], 5)

    def test_the_materialization_is_removed_after_the_check(self):
        """Cleanup postcondition: no worktree survives run_check, whatever the command did.

        The mutating case is here for cleanup only — `worktree remove --force` must succeed
        against a dirty tree — and asserts nothing about the outcome of such a run.
        """
        cases = {
            "clean run": "exit(0)",
            "mutating run": "exit(0 if open('docs/guide.md', 'w').write('poisoned') else 0)",
        }
        for shape, probe in cases.items():
            with self.subTest(shape=shape):
                repo, candidate = self._moved_head_repo()
                self._run(repo, candidate, probe)
                listed = git(repo.root, "worktree", "list", "--porcelain")
                entries = [line for line in listed.splitlines() if line.startswith("worktree ")]
                self.assertEqual(len(entries), 1, f"a materialization survived: {listed}")

    def test_a_worktree_declared_command_still_runs_in_the_working_tree(self):
        """The governance-scan path is untouched: a worktree-declared command reads bytes
        that exist in no commit at all, and its result says which tree that was."""
        repo, candidate = self._moved_head_repo()
        repo.write({"docs/uncommitted.txt": "only on disk\n"})
        probe = "exit(0 if open('docs/uncommitted.txt').read() == 'only on disk\\n' else 8)"
        result = self._run(repo, candidate, probe, subject_tree="worktree")
        self.assertEqual(result["result"], "PASS")
        self.assertEqual(result["exit_code"], 0)
        self.assertEqual(result["observed_tree"]["kind"], "worktree")

    def test_a_cwd_absent_from_the_candidate_is_spec_gap(self):
        """cwd resolves inside the materialization: a directory that exists only in the
        working tree is not a place a candidate-declared command can run."""
        repo, candidate = self._moved_head_repo()
        repo.write({"tools/only-on-disk.txt": "x\n"})
        result = run_check(
            check_doc(
                "check-command",
                "command_exit",
                config={
                    "argv": [sys.executable, "-c", "exit(0)"],
                    "cwd": "tools",
                    "allowed_exit_codes": [0],
                },
            ),
            context_for(repo, candidate),
        )
        self.assertEqual(result["result"], "SPEC_GAP")
        # The whole line, hand-written here: "tools" alone is four characters that unrelated
        # wording in this sentence could satisfy (execution contract, scope-discipline 2).
        self.assertEqual(
            result["detail"], "declared cwd does not exist in the observed tree: tools"
        )


# ===========================================================================
# R3 — the vocabulary guard must not be blind to `const`
# ===========================================================================


#: Exactly the V3-N0 forbidden-surface list. Substring match, case-insensitive.
FORBIDDEN_TOKENS = (
    "capabilit",
    "enforcement",
    "authority",
    "activation",
    "receipt",
    "lease",
    "idempoten",
    "event",
    "waiver",
    "gate_",
    "retrospective",
    "spend",
    "publication",
    "p4",
    "thesis",
    "experimentlab",
    "obsidian",
    "stage_id",
    "gsd",
    "uiux",
    "appsec",
)


def _flag(text: object, where: str, out: list[tuple[str, str, str]]) -> None:
    lowered = str(text).casefold()
    for token in FORBIDDEN_TOKENS:
        if token in lowered:
            out.append((where, str(text), token))


def scan_surface_vocabulary(node, where: str = "<root>", out: list | None = None) -> list:
    """Flag a forbidden token in any *surface* string a schema declares.

    Surface = property names, `$defs` keys, `required` entries, `enum` values **and `const`
    values**. The frozen V3-N0 fixture runner scanned the first four only, so a schema could
    smuggle a forbidden term through a `const` literal and pass. Descriptions are not
    surface — they are prose about the surface — and are deliberately out of scope.
    """
    if out is None:
        out = []
    if isinstance(node, dict):
        for section in ("properties", "$defs"):
            block = node.get(section)
            if isinstance(block, dict):
                for name in block:
                    _flag(name, f"{where}/{section}/{name}", out)
        required = node.get("required")
        if isinstance(required, list):
            for name in required:
                _flag(name, f"{where}/required", out)
        enum = node.get("enum")
        if isinstance(enum, list):
            for value in enum:
                if isinstance(value, str):
                    _flag(value, f"{where}/enum", out)
        if isinstance(node.get("const"), str):
            _flag(node["const"], f"{where}/const", out)
        for name, value in node.items():
            scan_surface_vocabulary(value, f"{where}/{name}", out)
    elif isinstance(node, list):
        for index, value in enumerate(node):
            scan_surface_vocabulary(value, f"{where}[{index}]", out)
    return out


class SchemaVocabularyGuardTests(unittest.TestCase):
    """R3: extend the vocabulary guard to `const`, then prove it over all nine schemas."""

    def test_r3_guard_catches_a_forbidden_token_in_a_const(self):
        """Self-test: a guard that silently scans nothing would otherwise also 'pass'."""
        hits = scan_surface_vocabulary({"$defs": {"thing": {"const": "capability_grant"}}})
        self.assertEqual([hit[2] for hit in hits], ["capabilit"])
        self.assertIn("const", hits[0][0])

    def test_r3_guard_catches_forbidden_tokens_on_every_scanned_surface(self):
        """Property names, $defs keys, required entries, enum values and const are all in scope."""
        cases = {
            "property name": {"properties": {"enforcement_mode": {"type": "string"}}},
            "$defs key": {"$defs": {"capabilityRef": {"type": "string"}}},
            "required entry": {"type": "object", "required": ["receipt_id"]},
            "enum value": {"enum": ["ACTIVATION", "OTHER"]},
            "const value": {"const": "waiver"},
        }
        for label, schema in cases.items():
            with self.subTest(surface=label):
                self.assertTrue(scan_surface_vocabulary(schema), f"{label} was not scanned")

    def test_r3_every_v3_schema_present_is_clean_under_the_extended_scan(self):
        """Covers N1's two, N0's seven, and every schema a later node adds.

        This assertion originally pinned the directory to exactly nine files. That pin was
        correct for the tree it was written against, but it encoded the *count* where the
        property is *cleanliness of whatever is present* — so the three schemas plan §9
        mandates for V3-N2 turned it red, with no repair site inside V3-N2's boundary
        (`tests/document_harness/**` is N1's root and `SCHEMA_FILES` lives in `__init__.py`,
        which no later node may write).

        The force the pin was really carrying is kept: it proved the scan covered every
        *registered* schema rather than silently scanning a subset. That is now a subset
        assertion, which a later node cannot trip by adding a file, while a registered schema
        that goes missing — the case that would make the loop below cover less than it claims
        — still fails.
        """
        files = sorted(SCHEMA_DIR.glob("*.schema.json"))
        present = {path.name for path in files}
        self.assertEqual(
            sorted(set(SCHEMA_FILES.values()) - present),
            [],
            "a registered schema is absent from the pack directory, so the scan below would "
            "silently cover a subset",
        )
        for path in files:
            with self.subTest(schema=path.name):
                hits = scan_surface_vocabulary(load_json(path), where=path.name)
                self.assertEqual(hits, [], f"{path.name} declares forbidden surface vocabulary: {hits}")

    def test_r3_scan_is_not_vacuous_over_a_real_schema(self):
        """Injecting a forbidden const into a real schema must be caught."""
        poisoned = copy.deepcopy(load_json(SCHEMA_DIR / "candidate-record.schema.json"))
        poisoned["$defs"]["observedChange"]["properties"]["change_kind"] = {"const": "capability_activation"}
        hits = scan_surface_vocabulary(poisoned, where="candidate-record.schema.json")
        self.assertTrue(hits)
        self.assertIn("capabilit", {hit[2] for hit in hits})


# ===========================================================================
# R4 — a governance document must not carry its own approval status
# ===========================================================================


CONTRACT_PATH = "contract/Document-Work-Assurance-Contract-v4.md"
#: The caller's `.goals/plans/document-work-assurance-harness-v3.plan.md` was the second
#: real document here until the split batch's R2. It does not travel with the instrument
#: (`HD-28`), and a test that reads the caller's tree passes in one repository and fails in
#: the other — which is a statement about who checked out what, not about the scan. The
#: contract is the real, `E2`-frozen sample that travels. Until round `CONTRACT-V4` the
#: in-tree contract (v3) carried a frontmatter `status:` and was the real flagged-then-
#: exempted sample; v4 carries no self-approval field, so the real document now proves the
#: PASSING side on its own merit, and the flagged/exempted behaviours stay covered by the
#: in-memory cases above, which is where a fixture belongs.


class GovernanceFrontmatterScopeTests(unittest.TestCase):
    """R4(a): scope is parsed frontmatter keys, never a raw text scan."""

    def test_r4a_frontmatter_keys_returns_only_top_level_keys(self):
        """Only the leading `---` block's own keys are in scope."""
        raw = b"---\ntitle: A doc\nstatus: draft\n---\n\n# Body\n\nstatus: not frontmatter\n"
        self.assertEqual(frontmatter_keys(raw), ["title", "status"])

    def test_r4a_body_quoted_status_is_not_flagged(self):
        """A document that merely QUOTES the forbidden field is not carrying it.

        A raw-text scanner would flag the very record that documents this defect.
        """
        raw = (
            b"---\ntitle: Errata record\n---\n\n"
            b"The contract's frontmatter carries `status: candidate-awaiting-user-signature`,\n"
            b"which is the defect this record describes.\n\n"
            b"    status: quoted-in-an-indented-block\n"
        )
        self.assertEqual(frontmatter_keys(raw), ["title"])
        scan = governance_scan(_InMemoryReader({"docs/errata.md": raw}), ["docs/errata.md"])
        self.assertTrue(scan.report.ok, scan.report.rendered())

    def test_r4a_nested_key_is_not_treated_as_top_level(self):
        """An indented key belongs to its parent mapping, not to the document."""
        raw = b"---\ntitle: A doc\nmeta:\n  status: draft\n  approved: true\n---\n\nbody\n"
        self.assertEqual(frontmatter_keys(raw), ["title", "meta"])
        scan = governance_scan(_InMemoryReader({"docs/nested.md": raw}), ["docs/nested.md"])
        self.assertTrue(scan.report.ok, scan.report.rendered())

    def test_r4a_document_without_frontmatter_yields_no_keys(self):
        """No leading `---` block means there is nothing in scope at all."""
        self.assertEqual(frontmatter_keys(b"# Just a heading\n\nstatus: approved\n"), [])
        self.assertEqual(frontmatter_keys(b""), [])


class GovernanceFieldMatchTests(unittest.TestCase):
    """R4(b): exact field-name match, never substring."""

    def _scan_one(self, key: str, value: str = "something"):
        raw = f"---\ntitle: A governance doc\n{key}: {value}\n---\n\nbody\n".encode("utf-8")
        return governance_scan(_InMemoryReader({"docs/doc.md": raw}), ["docs/doc.md"])

    def test_r4b_self_approval_fields_are_flagged(self):
        """A document that states its own approval state is rejected."""
        for key in ("status", "approval_status", "approved", "signed", "signature"):
            with self.subTest(field=key):
                scan = self._scan_one(key)
                self.assertEqual(codes(scan.report), ["V3-GOVERNANCE-SELF-APPROVAL"])
                self.assertIn(key, scan.report.issues[0].message)

    def test_r4b_owner_delegating_fields_pass(self):
        """`approval_status_owner` names WHO owns the approval without carrying it."""
        for key in ("approval_status_owner", "signature_owner"):
            with self.subTest(field=key):
                scan = self._scan_one(key, "V3-N0 administrative record")
                self.assertTrue(scan.report.ok, scan.report.rendered())
                self.assertEqual(scan.scanned, ("docs/doc.md",))

    def test_r4b_matching_is_by_exact_field_name(self):
        """The declared field set is exact names; a substring rule would misfire on the owner form."""
        self.assertIn("status", SELF_APPROVAL_FIELDS)
        self.assertNotIn("approval_status_owner", SELF_APPROVAL_FIELDS)
        self.assertNotIn("signature_owner", SELF_APPROVAL_FIELDS)


class GovernanceQuotedKeyTests(unittest.TestCase):
    """R4(b): a YAML key written in quotes is the same key.

    The defect: the key pattern anchored on a bare identifier, so `"approved_by": someone`
    and `'approved_by': someone` — both ordinary YAML spellings of the same mapping — parsed
    to no key at all and the document passed the scan. Quoting a field name was a complete
    bypass, and the bypass was invisible because the scan reported a clean result rather than
    an error.
    """

    def _scan(self, line: str):
        raw = f"---\ntitle: A governance doc\n{line}\n---\n\nbody\n".encode("utf-8")
        return governance_scan(_InMemoryReader({"docs/doc.md": raw}), ["docs/doc.md"])

    def test_every_quoted_spelling_of_a_self_approval_key_is_flagged(self):
        for line in ('"approved_by": someone', "'approved_by': someone", '"approved_by" : someone'):
            with self.subTest(line=line):
                self.assertEqual(frontmatter_keys(f"---\n{line}\n---\n".encode("utf-8")), ["approved_by"])
                scan = self._scan(line)
                self.assertEqual(codes(scan.report), ["V3-GOVERNANCE-SELF-APPROVAL"])
                self.assertIn("approved_by", scan.report.issues[0].message)

    def test_the_quoted_owner_form_still_delegates(self):
        """Negative control: quoting must not turn the *correct* pattern into a false positive."""
        scan = self._scan('"approval_status_owner": V3-N0 administrative record')
        self.assertTrue(scan.report.ok, scan.report.rendered())
        self.assertEqual(scan.scanned, ("docs/doc.md",))

    def test_a_quoted_mention_in_the_body_is_still_not_frontmatter(self):
        """Negative control: the scope stays the leading block, never a raw text search."""
        raw = b'---\ntitle: Errata record\n---\n\nThe defect is a doc carrying "approved_by": someone.\n'
        self.assertEqual(frontmatter_keys(raw), ["title"])
        scan = governance_scan(_InMemoryReader({"docs/errata.md": raw}), ["docs/errata.md"])
        self.assertTrue(scan.report.ok, scan.report.rendered())


class GovernanceExemptionTests(unittest.TestCase):
    """R4(c): the grandfather list is keyed by exact blob, enumerated, and fails closed."""

    ORIGINAL = b"---\ntitle: Frozen governance doc\nstatus: candidate-awaiting-user-signature\n---\n\nbody\n"

    def test_r4c_git_blob_id_matches_git(self):
        """The whole exemption scheme rests on this identity."""
        with TempRepo() as repo:
            for raw in (self.ORIGINAL, b"", b"one line\n", b"a\r\nb\r\n"):
                with self.subTest(raw=raw[:20]):
                    completed = subprocess.run(
                        ["git", "-C", str(repo.root), "hash-object", "--stdin"],
                        input=raw,
                        check=True,
                        stdout=subprocess.PIPE,
                    )
                    self.assertEqual(git_blob_id(raw), completed.stdout.decode("ascii").strip())

            # And the on-disk form agrees for content Git does not rewrite.
            target = repo.root / "frozen.md"
            target.write_bytes(self.ORIGINAL)
            from_path = subprocess.run(
                ["git", "-C", str(repo.root), "hash-object", "--", "frozen.md"],
                check=True,
                stdout=subprocess.PIPE,
            )
            self.assertEqual(git_blob_id(self.ORIGINAL), from_path.stdout.decode("ascii").strip())

    def test_r4c_exempted_blob_passes(self):
        """An enumerated blob, exempted for the exact field it carries, is allowed through."""
        exemptions = {
            git_blob_id(self.ORIGINAL): Exemption(
                blob=git_blob_id(self.ORIGINAL),
                path_hint="docs/frozen.md",
                fields=("status",),
                immutability_rule="frozen at V3-N0; never edited in place",
            )
        }
        scan = governance_scan(
            _InMemoryReader({"docs/frozen.md": self.ORIGINAL}), ["docs/frozen.md"], exemptions
        )
        self.assertTrue(scan.report.ok, scan.report.rendered())
        self.assertEqual(scan.exempted, ("docs/frozen.md",))

    def test_r4c_one_changed_byte_makes_the_exemption_evaporate(self):
        """Fail-closed: the exemption is keyed on bytes, so an edit un-exempts the file itself."""
        exemptions = {
            git_blob_id(self.ORIGINAL): Exemption(
                blob=git_blob_id(self.ORIGINAL),
                path_hint="docs/frozen.md",
                fields=("status",),
                immutability_rule="frozen at V3-N0; never edited in place",
            )
        }
        edited = self.ORIGINAL.replace(b"body\n", b"bodY\n")  # exactly one byte differs
        self.assertEqual(len(edited), len(self.ORIGINAL))
        self.assertNotEqual(git_blob_id(edited), git_blob_id(self.ORIGINAL))

        scan = governance_scan(_InMemoryReader({"docs/frozen.md": edited}), ["docs/frozen.md"], exemptions)
        self.assertEqual(codes(scan.report), ["V3-GOVERNANCE-SELF-APPROVAL"])
        self.assertEqual(scan.exempted, ())

    def test_r4c_exemption_does_not_silently_widen_to_another_field(self):
        """A blob grandfathered for `status` alone does not cover a newly added `approved`."""
        raw = (
            b"---\ntitle: Frozen governance doc\n"
            b"status: candidate-awaiting-user-signature\napproved: true\n---\n\nbody\n"
        )
        exemptions = {
            git_blob_id(raw): Exemption(
                blob=git_blob_id(raw),
                path_hint="docs/frozen.md",
                fields=("status",),
                immutability_rule="frozen at V3-N0; never edited in place",
            )
        }
        scan = governance_scan(_InMemoryReader({"docs/frozen.md": raw}), ["docs/frozen.md"], exemptions)
        self.assertEqual(codes(scan.report), ["V3-GOVERNANCE-EXEMPTION-NARROWER"])
        self.assertIn("approved", scan.report.issues[0].message)

    def test_r4c_incomplete_exemption_entry_raises_spec_gap(self):
        """An entry without its immutability rule is not a usable exemption."""
        with TempRepo() as repo:
            register = repo.root / "exemptions.json"
            register.write_text(
                json.dumps(
                    {
                        "exemptions": [
                            {
                                "blob": git_blob_id(self.ORIGINAL),
                                "path_hint": "docs/frozen.md",
                                "fields": ["status"],
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )
            with self.assertRaises(SpecGap):
                load_exemptions(register)

    def test_r4c_complete_exemption_entry_loads(self):
        """The same register loads once the rule is enumerated."""
        with TempRepo() as repo:
            register = repo.root / "exemptions.json"
            register.write_text(
                json.dumps(
                    {
                        "exemptions": [
                            {
                                "blob": git_blob_id(self.ORIGINAL),
                                "path_hint": "docs/frozen.md",
                                "fields": ["status"],
                                "immutability_rule": "frozen at V3-N0; never edited in place",
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )
            loaded = load_exemptions(register)
            self.assertEqual(list(loaded), [git_blob_id(self.ORIGINAL)])
            self.assertEqual(loaded[git_blob_id(self.ORIGINAL)].fields, ("status",))

    def test_r4c_absent_register_means_no_exemption_and_a_missing_one_raises(self):
        """No register means nothing is exempt; a named-but-missing register is a SPEC_GAP."""
        self.assertEqual(load_exemptions(None), {})
        with self.assertRaises(SpecGap):
            load_exemptions("this-register-does-not-exist.json")


class GovernanceRealDocumentTests(unittest.TestCase):
    """R4: the scan must hold over the repository's real, immutable governance document."""

    def setUp(self) -> None:
        self.reader = WorktreeReader(REPO_ROOT)
        self.paths = [CONTRACT_PATH]
        for path in self.paths:
            # A skip here would be a silent pass — the whole point of R4 is that the scan
            # actually reaches the real governance layer.
            self.assertIsNotNone(
                self.reader.read(path), f"governance document not readable at {REPO_ROOT / path}"
            )

    def test_r4_the_real_contract_passes_on_its_own_merit(self):
        """v4 carries no self-approval field, so the scan passes it with ZERO exemptions.

        This is the inverse of the sample v3 provided (flagged until its blob-keyed
        exemption): the operative contract now demonstrates that a governance document can
        simply be written correctly — the exemption register's own note says the register
        is not for documents that could have been. The flagged and exempted behaviours keep
        their coverage in the in-memory fixture classes above.
        """
        for path in self.paths:
            raw = self.reader.read(path)
            offending = tuple(key for key in frontmatter_keys(raw) if key in SELF_APPROVAL_FIELDS)
            self.assertEqual(offending, (), f"{path} carries {offending}")
        scan = governance_scan(self.reader, self.paths)
        self.assertTrue(scan.report.ok, scan.report.rendered())
        self.assertEqual(list(scan.exempted), [])

    def test_r4_owner_delegating_fields_in_the_real_documents_are_not_flagged(self):
        """The contract's `signature_owner` names WHO approves without carrying approval."""
        contract_keys = frontmatter_keys(self.reader.read(CONTRACT_PATH))
        self.assertIn("signature_owner", contract_keys)
        self.assertNotIn("signature_owner", SELF_APPROVAL_FIELDS)


class EmittedResultConformanceTests(unittest.TestCase):
    """Every emitted CheckResult conforms to its schema, on every path (R1 regression).

    Added by the lead session after this defect was found during implementation: the
    wrong-subject ruling returned early and skipped validation, so a `git_diff_boundary`
    result that never ran still claimed the shape of one that had — and nothing caught it,
    because the unvalidated path was exactly the path that never checked anything.

    The test is written against the whole kind x subject_tree cross-product rather than the
    one reported case, because the defect class is "a result escaped without validation",
    not "one field was missing".
    """

    def setUp(self) -> None:
        self.repo = TempRepo({"docs/instruction.md": "# Instruction\n\nwrite the guide\n"})
        self.addCleanup(self.repo.cleanup)
        self.candidate = self.repo.commit_candidate(
            {
                "docs/guide.md": "# Guide\n",
                "docs/data.json": '{"name": "guide"}',
                "docs/data.schema.json": json.dumps(
                    {
                        "$schema": "https://json-schema.org/draft/2020-12/schema",
                        "type": "object",
                        "required": ["name"],
                        "properties": {"name": {"type": "string"}},
                    }
                ),
            }
        )

    def _requests(self) -> list[dict]:
        configs = {
            "file_exists": {"artifact_id": "a-guide"},
            "json_schema": {
                "subject_path": "docs/data.json",
                "schema_path": "docs/data.schema.json",
            },
            "markdown_link": {"subject_paths": ["docs/guide.md"]},
            "locator_exists": {"locator": {"path": "docs/guide.md", "anchor": "# Guide"}},
            "git_diff_boundary": None,
            "command_exit": {
                "argv": [sys.executable, "-c", "raise SystemExit(0)"],
                "cwd": ".",
                "allowed_exit_codes": [0],
            },
        }
        return [
            check_doc(f"c-{kind.replace('_', '-')}-{tree[:4]}", kind, subject_tree=tree, config=config)
            for kind, config in configs.items()
            for tree in ("candidate_commit", "worktree")
        ]

    def test_every_kind_and_subject_tree_emits_a_schema_valid_result(self) -> None:
        """No path may return a result the schema would reject."""
        ctx = context_for(self.repo, self.candidate)
        for check in self._requests():
            with self.subTest(check_id=check["check_id"]):
                result = run_check(check, ctx)
                self.assertEqual(
                    validate("check_result", result).rendered(),
                    [],
                    f"{check['check_id']} emitted a schema-invalid result: {result}",
                )

    def test_a_degenerate_request_is_reported_not_crashed(self) -> None:
        """A schema-valid request whose two subject paths coincide is one subject observed
        once. It must produce a reported outcome, never an exception: crashing on a valid
        request would take the whole run down instead of recording what happened."""
        ctx = context_for(self.repo, self.candidate)
        result = run_check(
            check_doc(
                "c-json-same",
                "json_schema",
                config={"subject_path": "docs/guide.md", "schema_path": "docs/guide.md"},
            ),
            ctx,
        )
        self.assertEqual(result["result"], "SPEC_GAP")
        self.assertEqual(len(result["subjects"]), 1)
        self.assertEqual(validate("check_result", result).rendered(), [])

    def test_wrong_subject_boundary_result_claims_no_observation(self) -> None:
        """A boundary check that never ran states no boundary and no base — inventing either
        would be evidence of an observation that did not happen."""
        ctx = context_for(self.repo, self.candidate)
        result = run_check(
            check_doc("c-boundary-wt", "git_diff_boundary", subject_tree="worktree"), ctx
        )
        self.assertEqual(result["result"], "WRONG_SUBJECT")
        self.assertNotIn("boundary_observed", result)
        self.assertNotIn("base_revision", result)

    def test_a_boundary_check_that_did_run_states_what_it_applied(self) -> None:
        """The converse: an executed boundary check must name its boundary and its base."""
        ctx = context_for(self.repo, self.candidate)
        result = run_check(
            check_doc("c-boundary-ok", "git_diff_boundary", subject_tree="candidate_commit"), ctx
        )
        self.assertIn(result["result"], ("PASS", "FAIL"))
        self.assertIn("boundary_observed", result)
        self.assertEqual(result["base_revision"], self.repo.base)


class _InMemoryReader:
    """A TreeReader-shaped stub for the frontmatter cases, which need bytes and nothing else.

    The governance scan only ever calls `read`; using real bytes here keeps each R4 fixture
    visible in the test that makes the claim, instead of hidden in a temporary file.
    """

    kind = "candidate_commit"

    def __init__(self, files: dict[str, bytes]) -> None:
        self.files = files
        self.revision = FAKE_REV

    def read(self, path: str) -> bytes | None:
        return self.files.get(path)

    def exists(self, path: str) -> bool:
        return path in self.files

    def observed_tree(self) -> dict[str, str]:
        return {"kind": self.kind, "revision": self.revision}


if __name__ == "__main__":
    unittest.main(verbosity=2)
