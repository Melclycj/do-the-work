#!/usr/bin/env python3
"""Round STRANGER-GUARDS: the guards' surfaces are the caller's declaration, not constants.

The defect class (E7, rider `chk-caller-prefixes`): a guard whose exempt surfaces are
hard-coded to one caller's directory names scans every other caller's records as work
products — and a record quoting the broken path it reports is then blocked, replaying the
`freeze-audit` deadlock on a stranger; during `E9`'s freeze window the blocked commit is
the only one the window admits. Three properties pin the class, each with its negative
control (E4):

* **A declaration is honored** — records live where the caller says, and a declared key
  REPLACES its default rather than extending it (an extension could never narrow a
  surface).
* **The first caller's entries survive as ITS declaration** — the exact
  `ResearchSystem/…` list that used to be the constants is written here as a declaration
  fixture, hand-typed (E5), and the paths that were exempt before are exempt under it.
* **A malformed declaration blocks loudly** — never a silent fall back to defaults, which
  would re-scan the caller's records with nothing announcing it (the wrong-root-taken-
  quietly shape, one surface over).

`test_precommit_checks.py` pins the DEFAULTS the undeclared caller gets;
`test_init_command.py` pins the bytes `dtw init` writes. This file is the declared path.
"""
from __future__ import annotations

import json
import unittest

from _harness import TempRepo, git

from hooks import candidate_path_check, review_freeze_check
from rsclib.document_harness import caller

BROKEN = "Thesis/no/such/file.md"

#: A work-product path outside every surface any fixture below declares.
CANDIDATE = "contract/amendments/2026-08-23-stranger.md"

#: The first caller's layout, byte-for-byte the two tuples `candidate_path_check` carried
#: until round STRANGER-GUARDS plus the record directory `review_freeze_check` carried —
#: hand-written here (E5), never derived from any module or from git history.
FIRST_CALLER_DECLARATION = {
    "record_surface": [
        "ResearchSystem/migration/",
        "ResearchSystem/document-harness/journal/",
        "ResearchSystem/inventory/amendments/",
        "ResearchSystem/HARNESS-LEDGER.md",
        "ResearchSystem/HARNESS-LEDGER-archive.md",
        "ResearchSystem/HARNESS-RIDERS.md",
        "ResearchSystem/HARNESS-DECISIONS-archive.md",
        ".goals/LEDGER.md",
        ".goals/LEDGER-archive.md",
    ],
    "review_record_dirs": ["ResearchSystem/migration/document-work-assurance-v3/"],
    "specification_surface": ["ResearchSystem/assurance/runs/"],
}


def declare(repo: TempRepo, declaration) -> None:
    (repo.root / ".harness").mkdir(parents=True, exist_ok=True)
    (repo.root / ".harness" / "scan-surfaces.json").write_text(
        declaration if isinstance(declaration, str) else json.dumps(declaration),
        encoding="utf-8",
    )


def stage(repo: TempRepo, files: dict[str, str]) -> None:
    repo.write(files)
    git(repo.root, "add", "--", *files.keys())


def write_marker(repo: TempRepo) -> None:
    (repo.root / ".harness").mkdir(parents=True, exist_ok=True)
    (repo.root / ".harness" / "review-pending.json").write_text(
        json.dumps({"subject": "f" * 40, "dispatched_at": "2026-08-23T00:00:00+00:00"}),
        encoding="utf-8",
    )


class TheLoader(unittest.TestCase):
    """`caller.load_scan_surfaces`: defaults, declaration, and the refusal boundary."""

    def test_no_declaration_yields_the_defaults(self):
        with TempRepo() as repo:
            self.assertEqual(caller.load_scan_surfaces(repo.root), caller.DEFAULTS)

    def test_a_declared_key_replaces_its_default_and_an_absent_key_keeps_it(self):
        with TempRepo() as repo:
            declare(repo, {"record_surface": ["docs/records/"]})
            surfaces = caller.load_scan_surfaces(repo.root)
            self.assertEqual(surfaces.record, ("docs/records/",))
            self.assertEqual(surfaces.review_record_dirs, caller.DEFAULTS.review_record_dirs)
            self.assertEqual(surfaces.specification, caller.DEFAULTS.specification)

    def test_an_empty_list_is_a_declaration_too(self):
        """Declaring no specification surface means the runs tree is scanned — the
        caller's call to make, not a malformed input."""
        with TempRepo() as repo:
            declare(repo, {"specification_surface": []})
            self.assertEqual(caller.load_scan_surfaces(repo.root).specification, ())

    def test_unreadable_json_is_refused_not_defaulted(self):  # must fire
        with TempRepo() as repo:
            declare(repo, "{not json")
            with self.assertRaises(caller.SurfaceDeclarationError):
                caller.load_scan_surfaces(repo.root)

    def test_a_misspelled_key_is_refused_not_ignored(self):  # must fire
        # The quiet failure this guards: `record_surfaces` (plural) silently ignored would
        # revert that key to defaults with nothing announcing it.
        with TempRepo() as repo:
            declare(repo, {"record_surfaces": ["docs/records/"]})
            with self.assertRaises(caller.SurfaceDeclarationError) as caught:
                caller.load_scan_surfaces(repo.root)
            self.assertIn("record_surfaces", str(caught.exception))

    def test_a_non_object_and_a_non_string_entry_are_refused(self):  # must fire
        for bad in (["a-list"], {"record_surface": "not-a-list"}, {"record_surface": [1]}):
            with self.subTest(declaration=bad):
                with TempRepo() as repo:
                    declare(repo, bad)
                    with self.assertRaises(caller.SurfaceDeclarationError):
                        caller.load_scan_surfaces(repo.root)


class TheCandidateGuardReadsTheDeclaration(unittest.TestCase):
    def test_a_record_on_a_declared_surface_may_quote_a_broken_path(self):
        with TempRepo() as repo:
            declare(repo, {"record_surface": ["docs/records/"]})
            stage(repo, {"docs/records/finding.md": f"reporting `{BROKEN}` as broken\n"})
            self.assertEqual(candidate_path_check.check(repo.root), 0)

    def test_without_the_declaration_the_same_path_blocks(self):  # negative control
        with TempRepo() as repo:
            stage(repo, {"docs/records/finding.md": f"reporting `{BROKEN}` as broken\n"})
            self.assertEqual(candidate_path_check.check(repo.root), 1)

    def test_a_declared_key_replaces_the_default_not_extends_it(self):  # must fire
        # `journal/` is a default record surface; a declaration that names only
        # `docs/records/` withdraws it, so a journal file is scanned again.
        with TempRepo() as repo:
            declare(repo, {"record_surface": ["docs/records/"]})
            stage(repo, {"journal/round-2026-08-23.md": f"quoting `{BROKEN}`\n"})
            self.assertEqual(candidate_path_check.check(repo.root), 1)

    def test_a_work_product_still_blocks_under_a_declaration(self):  # must fire
        with TempRepo() as repo:
            declare(repo, {"record_surface": ["docs/records/"]})
            stage(repo, {CANDIDATE: f"hosted in `{BROKEN}`\n"})
            self.assertEqual(candidate_path_check.check(repo.root), 1)

    def test_a_malformed_declaration_blocks_loudly(self):  # must fire
        with TempRepo() as repo:
            declare(repo, "{not json")
            stage(repo, {CANDIDATE: "a perfectly clean line\n"})
            self.assertEqual(candidate_path_check.check(repo.root), 1)

    def test_a_valid_declaration_and_a_clean_stage_pass(self):  # negative control
        with TempRepo() as repo:
            declare(repo, {"record_surface": ["docs/records/"]})
            stage(repo, {CANDIDATE: "a perfectly clean line\n"})
            self.assertEqual(candidate_path_check.check(repo.root), 0)


class TheFreezeGuardReadsTheDeclaration(unittest.TestCase):
    def test_a_record_in_a_declared_directory_lands_during_the_window(self):
        with TempRepo() as repo:
            write_marker(repo)
            declare(repo, {"review_record_dirs": ["audits/"]})
            stage(repo, {"audits/v3-review-full-0123abc.md": "record\n"})
            self.assertEqual(review_freeze_check.check(repo.root), 0)

    def test_without_the_declaration_the_same_record_blocks(self):  # negative control
        with TempRepo() as repo:
            write_marker(repo)
            stage(repo, {"audits/v3-review-full-0123abc.md": "record\n"})
            self.assertEqual(review_freeze_check.check(repo.root), 1)

    def test_a_non_record_name_in_the_declared_directory_still_blocks(self):  # must fire
        # The family names are R6's, the same in every repository — the declaration moves
        # the directory, never widens the vocabulary.
        with TempRepo() as repo:
            write_marker(repo)
            declare(repo, {"review_record_dirs": ["audits/"]})
            stage(repo, {"audits/notes.md": "not a record\n"})
            self.assertEqual(review_freeze_check.check(repo.root), 1)

    def test_a_product_result_under_a_declared_runs_tree_lands(self):
        with TempRepo() as repo:
            write_marker(repo)
            declare(repo, {"specification_surface": ["work/runs/"]})
            stage(repo, {"work/runs/p9/evidence/review-full.json": "{}\n"})
            self.assertEqual(review_freeze_check.check(repo.root), 0)

    def test_a_non_result_file_under_that_tree_still_blocks(self):  # must fire
        with TempRepo() as repo:
            write_marker(repo)
            declare(repo, {"specification_surface": ["work/runs/"]})
            stage(repo, {"work/runs/p9/evidence/coverage.json": "{}\n"})
            self.assertEqual(review_freeze_check.check(repo.root), 1)

    def test_a_malformed_declaration_blocks_during_the_window(self):  # must fire, closed
        with TempRepo() as repo:
            write_marker(repo)
            declare(repo, "{not json")
            stage(repo, {"migration/document-work-assurance-v3/v3-cold-read-0123abc.md": "r\n"})
            self.assertEqual(review_freeze_check.check(repo.root), 1)

    def test_no_marker_passes_whatever_the_declaration_says(self):  # negative control
        with TempRepo() as repo:
            declare(repo, "{not json")
            stage(repo, {CANDIDATE: "x\n"})
            self.assertEqual(review_freeze_check.check(repo.root), 0)


class TheFirstCallersEntriesSurviveAsItsDeclaration(unittest.TestCase):
    """The plan's ruling verbatim: the old constants become the first caller's declaration,
    not universal truth. Every path exempt under the old tuples is exempt under the
    declaration above — and scanned again the moment the declaration is absent."""

    #: One concrete path per entry of the old constants, spelling and depth as the first
    #: caller writes them.
    FIRST_CALLER_RECORDS = (
        "ResearchSystem/migration/document-work-assurance-v3/v3-review-full-abc1234.md",
        "ResearchSystem/document-harness/journal/some-round-2026-08-06.md",
        "ResearchSystem/inventory/amendments/2026-08-02-p5a-shells.md",
        "ResearchSystem/HARNESS-LEDGER.md",
        "ResearchSystem/HARNESS-LEDGER-archive.md",
        "ResearchSystem/HARNESS-RIDERS.md",
        "ResearchSystem/HARNESS-DECISIONS-archive.md",
        ".goals/LEDGER.md",
        ".goals/LEDGER-archive.md",
        "ResearchSystem/assurance/runs/p5b-claims/instruction.md",
    )

    def test_every_old_exemption_holds_under_the_declaration(self):
        for path in self.FIRST_CALLER_RECORDS:
            with self.subTest(surface=path):
                with TempRepo() as repo:
                    declare(repo, FIRST_CALLER_DECLARATION)
                    stage(repo, {path: f"reporting `{BROKEN}` as broken\n"})
                    self.assertEqual(candidate_path_check.check(repo.root), 0)

    def test_the_declarations_absence_withdraws_them(self):  # negative control
        with TempRepo() as repo:
            stage(repo, {
                "ResearchSystem/migration/document-work-assurance-v3/"
                "v3-review-full-abc1234.md": f"reporting `{BROKEN}` as broken\n",
            })
            self.assertEqual(candidate_path_check.check(repo.root), 1)

    def test_the_first_callers_freeze_window_still_admits_its_records(self):
        with TempRepo() as repo:
            write_marker(repo)
            declare(repo, FIRST_CALLER_DECLARATION)
            stage(repo, {
                "ResearchSystem/migration/document-work-assurance-v3/"
                "v3-cold-read-0123abc.md": "record\n",
                "ResearchSystem/assurance/runs/p4-bridge/evidence/review-full.json": "{}\n",
                "ResearchSystem/assurance/runs/p4-bridge/evidence/review-verify.json": "{}\n",
            })
            self.assertEqual(review_freeze_check.check(repo.root), 0)

    def test_the_first_callers_window_still_refuses_a_work_product(self):  # must fire
        with TempRepo() as repo:
            write_marker(repo)
            declare(repo, FIRST_CALLER_DECLARATION)
            stage(repo, {"ResearchSystem/contract/amendments/x.md": "work product\n"})
            self.assertEqual(review_freeze_check.check(repo.root), 1)


if __name__ == "__main__":
    raise SystemExit(unittest.main())
