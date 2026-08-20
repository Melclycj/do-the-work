#!/usr/bin/env python3
"""Acceptance matrix for the three tracked pre-commit checks (2026-07-29 repair batch;
`candidate_path_check` joined 2026-08-06 with SIMP-A4; `ledger_cap_check` moved to the
caller side — `Thesis/Work/Tooling/` — 2026-08-12, batch B R3, and its tests were
deleted rather than moved: this suite must not import outside the harness tree, and the
caller runs its machinery untested, same standing as its `repo-audit.py`).

Every must-fire case is paired with a clean baseline asserted first (E4's negative
control): a refusal test proves nothing if the baseline also refuses. Each check is
driven against a disposable repository via its `check(repo_root)` entry — the same bytes
the git hook sees, because both read the staged tree, never the worktree.
"""
from __future__ import annotations

import json
import unittest

from _harness import TempRepo, git

from hooks import (
    candidate_path_check,
    layer_path_check,
    review_freeze_check,
)
from rsclib.document_harness import paths

RECORD = "ResearchSystem/migration/document-work-assurance-v3/v3-cold-read-0123abc.md"
DISPATCH_NOTE = "ResearchSystem/migration/document-work-assurance-v3/v3-dispatch-foo.md"
# Hand-written product-run paths (E5): the returned record of a product run is two
# artifacts — the migration record md AND the run's ReviewResult JSON (triage decision
# user-decision-triage-e9-guard-record-vocabulary, 2026-08-01).
PRODUCT_FULL = "ResearchSystem/assurance/runs/p4-bridge/evidence/review-full.json"
PRODUCT_VERIFY = "ResearchSystem/assurance/runs/p4-bridge/evidence/review-verify.json"
PRODUCT_NON_RESULT = "ResearchSystem/assurance/runs/p4-bridge/evidence/coverage.json"
# Hand-written, never the guarded module's own constant (E5; v3-review-full-8ec4c60.md B2):
CHECKLIST = "document-harness/CONSTRUCTION-CHECKLIST.md"
# A work-product path outside every excluded surface — the shape the A3 defect was written
# into, so the candidate guard is exercised where it actually has to fire.
CANDIDATE = "ResearchSystem/contract/amendments/2026-08-05-a3-p5b-scoped.md"


def stage(repo: TempRepo, files: dict[str, str]) -> None:
    """Stage exactly these paths — the E8 shape; the marker itself is never staged."""
    repo.write(files)
    git(repo.root, "add", "--", *files.keys())


def write_marker(repo: TempRepo) -> None:
    # Mirrors what the producer writes: subject and dispatched_at, and no run-kind label
    # (deleted 2026-08-07 — nothing branched on it and this consumer only displayed it).
    (repo.root / ".harness").mkdir(parents=True, exist_ok=True)
    (repo.root / ".harness" / "review-pending.json").write_text(
        json.dumps({"subject": "f" * 40, "dispatched_at": "2026-08-07T00:00:00+00:00"}),
        encoding="utf-8",
    )


class FreezeCheck(unittest.TestCase):
    """E9's window, mechanised: marker present -> only record commits pass."""

    def test_no_marker_passes_anything(self):  # negative control
        with TempRepo() as repo:
            stage(repo, {"docs/other.md": "x\n"})
            self.assertEqual(review_freeze_check.check(repo.root), 0)

    def test_marker_with_record_only_staged_passes(self):  # negative control
        with TempRepo() as repo:
            write_marker(repo)
            stage(repo, {RECORD: "record\n"})
            self.assertEqual(review_freeze_check.check(repo.root), 0)

    def test_marker_with_a_non_record_path_blocks(self):  # must fire
        with TempRepo() as repo:
            write_marker(repo)
            stage(repo, {RECORD: "record\n", "docs/other.md": "x\n"})
            self.assertEqual(review_freeze_check.check(repo.root), 1)

    def test_a_dispatch_note_is_not_a_record(self):  # the family boundary binds
        with TempRepo() as repo:
            write_marker(repo)
            stage(repo, {DISPATCH_NOTE: "note\n"})
            self.assertEqual(review_freeze_check.check(repo.root), 1)

    def test_a_product_run_reviewresult_json_is_a_record(self):
        # The first product FULL return (391db68/87938f3) had to land in two commits
        # because the vocabulary refused the ReviewResult JSON half of the record.
        with TempRepo() as repo:
            write_marker(repo)
            stage(repo, {RECORD: "record\n", PRODUCT_FULL: "{}\n", PRODUCT_VERIFY: "{}\n"})
            self.assertEqual(review_freeze_check.check(repo.root), 0)

    def test_a_non_result_run_evidence_file_still_blocks(self):  # the family boundary binds
        with TempRepo() as repo:
            write_marker(repo)
            stage(repo, {RECORD: "record\n", PRODUCT_NON_RESULT: "{}\n"})
            self.assertEqual(review_freeze_check.check(repo.root), 1)

    def test_an_unreadable_marker_still_freezes(self):
        with TempRepo() as repo:
            (repo.root / ".harness").mkdir(parents=True, exist_ok=True)
            (repo.root / ".harness" / "review-pending.json").write_text(
                "{not json", encoding="utf-8"
            )
            stage(repo, {"docs/other.md": "x\n"})
            self.assertEqual(review_freeze_check.check(repo.root), 1)


class LayerPath(unittest.TestCase):
    """One class flagged — the token resolving nowhere in this repository (DE-PREFIX, HD-50 R3).

    The two prefix-shaped branches this guard carried until round DE-PREFIX are both
    subsumed: a stale `ResearchSystem/`-prefixed token and a caller-held path now fail the
    same resolution test. Runtime markers and placeholder-bearing tokens are deliberately
    out, and each carve-out is pinned below so the module docstring's claims stay honest.
    """

    def test_resolvable_tokens_pass(self):  # negative control
        with TempRepo() as repo:
            (repo.root / "schema" / "pack").mkdir(parents=True)
            stage(repo, {CHECKLIST: "the `schema/pack/` pack\n"})
            self.assertEqual(layer_path_check.check(repo.root), 0)

    def test_a_token_resolving_nowhere_blocks(self):  # must fire — the class's central shape
        with TempRepo() as repo:
            stage(repo, {CHECKLIST: "kept in the caller's `ExperimentLab/papers/` tree\n"})
            self.assertEqual(layer_path_check.check(repo.root), 1)

    def test_a_stale_prefixed_token_blocks(self):  # must fire — the pre-DE-PREFIX convention
        with TempRepo() as repo:
            (repo.root / "schema" / "pack").mkdir(parents=True)
            stage(repo, {CHECKLIST: "the `ResearchSystem/schema/pack/` pack\n"})
            self.assertEqual(layer_path_check.check(repo.root), 1)

    def test_a_file_dir_relative_token_passes(self):  # the member's own directory is a root
        with TempRepo() as repo:
            (repo.root / "document-harness" / "journal").mkdir(parents=True)
            (repo.root / "document-harness" / "journal" / "x.md").write_text(
                "j\n", encoding="utf-8"
            )
            stage(repo, {CHECKLIST: "see `journal/x.md`\n"})
            self.assertEqual(layer_path_check.check(repo.root), 0)

    def test_a_runtime_marker_counts_as_resolving(self):  # E10's at-rest carve-out
        with TempRepo() as repo:
            stage(repo, {CHECKLIST: "freezes via `.harness/review-pending.json`\n"})
            self.assertEqual(layer_path_check.check(repo.root), 0)

    def test_resolution_escaping_the_repo_root_does_not_count(self):  # must fire
        with TempRepo() as repo:
            (repo.root.parent / "outside.md").write_text("caller bytes\n", encoding="utf-8")
            stage(repo, {CHECKLIST: "see `../outside.md`\n"})
            self.assertEqual(layer_path_check.check(repo.root), 1)

    def test_a_placeholder_token_is_invisible_by_shape(self):  # the disclosed ceiling (L-2)
        with TempRepo() as repo:
            stage(
                repo,
                {CHECKLIST: "the run's `assurance/runs/<run-id>/control/paragraph-map.json`\n"},
            )
            self.assertEqual(layer_path_check.check(repo.root), 0)

    def test_a_non_layer_file_is_never_scanned(self):  # negative control
        with TempRepo() as repo:
            stage(repo, {"docs/notes.md": "see `no/such/file.md`\n"})
            self.assertEqual(layer_path_check.check(repo.root), 0)

    def test_a_pre_existing_token_is_not_this_batchs_to_repair(self):  # B1 negative control
        with TempRepo() as repo:
            repo.write({CHECKLIST: "old `no/such/place.md` mention\n"})
            git(repo.root, "add", "--", CHECKLIST)
            git(repo.root, "commit", "-qm", "pre-existing token")
            stage(repo, {CHECKLIST: "old `no/such/place.md` mention\na new clean line\n"})
            self.assertEqual(layer_path_check.check(repo.root), 0)

    def test_a_newly_added_bad_token_still_blocks(self):  # must fire under diff scope
        with TempRepo() as repo:
            repo.write({CHECKLIST: "clean base line\n"})
            git(repo.root, "add", "--", CHECKLIST)
            git(repo.root, "commit", "-qm", "clean base")
            stage(repo, {CHECKLIST: "clean base line\nsee `no/such/file.md`\n"})
            self.assertEqual(layer_path_check.check(repo.root), 1)

    def test_a_rename_into_the_layer_does_not_rescan_standing_text(self):
        """The DE-PREFIX candidate itself was blocked by this class: a staged rename made
        the member's whole standing text read as added lines, so the E2-frozen tokens the
        clause excepts were re-scanned. A rename adds no lines (negative control)."""
        with TempRepo() as repo:
            repo.write({"old-home/CONSTRUCTION-CHECKLIST.md": "frozen `no/such/place.md`\n"})
            git(repo.root, "add", "--", "old-home/CONSTRUCTION-CHECKLIST.md")
            git(repo.root, "commit", "-qm", "standing text at the old home")
            (repo.root / "document-harness").mkdir(parents=True, exist_ok=True)
            git(repo.root, "mv", "old-home/CONSTRUCTION-CHECKLIST.md", CHECKLIST)
            self.assertEqual(layer_path_check.check(repo.root), 0)

    def test_a_bad_line_added_on_top_of_a_rename_still_blocks(self):  # must fire
        with TempRepo() as repo:
            repo.write({"old-home/CONSTRUCTION-CHECKLIST.md": "clean standing line\n"})
            git(repo.root, "add", "--", "old-home/CONSTRUCTION-CHECKLIST.md")
            git(repo.root, "commit", "-qm", "standing text at the old home")
            (repo.root / "document-harness").mkdir(parents=True, exist_ok=True)
            git(repo.root, "mv", "old-home/CONSTRUCTION-CHECKLIST.md", CHECKLIST)
            stage(repo, {CHECKLIST: "clean standing line\nsee `no/such/file.md`\n"})
            self.assertEqual(layer_path_check.check(repo.root), 1)

    def test_a_pasted_diff_header_does_not_silence_the_rest_of_the_member(self):
        """FULL 39a21a8 B-2: a content line opening `+++ ` renders in the diff as `++++ …`,
        which the parser used to read as a header reset — every added line after it was
        dropped from the scan, a fail-open. Must fire on the token BELOW the pasted header."""
        with TempRepo() as repo:
            stage(
                repo,
                {CHECKLIST: "clean line\n+++ a pasted diff header\nsee `no/such/file.md`\n"},
            )
            self.assertEqual(layer_path_check.check(repo.root), 1)


class LayerMembership(unittest.TestCase):
    """E5: the expectation is this hand-written list, never the module's own tuple.

    A member silently dropped from `LAYER` stops being scanned with every other test still
    green — the reviewer's M5 mutation (v3-review-full-8ec4c60.md B2). The equality pins the
    set; the scan case proves each member is actually reached.
    """

    EXPECTED = (
        "document-harness/CONSTRUCTION-CHECKLIST.md",
        "document-harness/README.md",
        "document-harness/EXECUTION.md",
        "document-harness/REVIEW.md",
        "document-harness/ORCHESTRATION.md",
        "migration/document-work-assurance-v3/v3-harness-operating-contract.md",
        "migration/document-work-assurance-v3/v3-harness-review-contract.md",
        "contract/Document-Work-Assurance-Contract-v3-supersession-1.md",
        "contract/Document-Work-Assurance-Contract-v3-supersession-2.md",
        "schema/document-assurance-v3/paragraph-map.schema.json",
    )

    def test_layer_equals_the_hand_written_membership(self):
        self.assertEqual(tuple(layer_path_check.LAYER), self.EXPECTED)

    def test_every_member_is_scanned(self):
        for path in self.EXPECTED:
            with self.subTest(member=path):
                with TempRepo() as repo:
                    stage(repo, {path: "see `no/such/file.md`\n"})
                    self.assertEqual(layer_path_check.check(repo.root), 1)


class CandidatePath(unittest.TestCase):
    """SIMP-A4: the nowhere-resolving class on work products, split by shorthand.
    (`layer_path_check` skipped that class as *may be illustrative* until round DE-PREFIX
    taught it to block; this lint owns the work-product surface the layer guard never scans.)

    The whole point of this guard is the token that resolves NOWHERE, so the shorthand
    baseline is asserted first in every pair — a guard that blocked both would be a guard
    nobody could commit under.
    """

    #: The real defect, byte-for-byte as written into the signed A3 amendment
    #: (`2026-08-05-a3-p5b-scoped.md` §6) and missed by that run's independent FULL.
    A3_DEFECT = "Thesis/literature-analysis/sota-comparison.md"

    def test_a_directly_resolvable_token_passes(self):  # negative control
        with TempRepo() as repo:
            stage(repo, {
                "ResearchSystem/tooling/rsclib/lint.py": "x\n",
                CANDIDATE: "see `ResearchSystem/tooling/rsclib/lint.py`\n",
            })
            self.assertEqual(candidate_path_check.check(repo.root), 0)

    def test_a_unique_suffix_is_shorthand_and_passes(self):  # negative control
        with TempRepo() as repo:
            stage(repo, {
                "ResearchSystem/tooling/rsclib/lint.py": "x\n",
                CANDIDATE: "the compiler's `rsclib/lint.py`\n",
            })
            self.assertEqual(candidate_path_check.check(repo.root), 0)

    def test_a_token_resolvable_nowhere_blocks(self):  # must fire — the A3 defect
        with TempRepo() as repo:
            stage(repo, {CANDIDATE: f"hosted in `{self.A3_DEFECT}`\n"})
            self.assertEqual(candidate_path_check.check(repo.root), 1)

    def test_an_ambiguous_suffix_blocks(self):  # must fire — two matches is not shorthand
        with TempRepo() as repo:
            stage(repo, {
                "a/pkg/thing.py": "x\n",
                "b/pkg/thing.py": "x\n",
                CANDIDATE: "see `pkg/thing.py`\n",
            })
            self.assertEqual(candidate_path_check.check(repo.root), 1)

    def test_the_suffix_match_is_segment_bounded(self):  # must fire — not a bare endswith
        # `mypkg/lint.py` ends with the string `pkg/lint.py` but is not that path. A bare
        # `endswith` calls this shorthand and lets the miss through; only the `/`-anchored
        # form refuses it. The first fixture written here did not distinguish the two and
        # survived the mutation (E4 — the reason this comment exists).
        with TempRepo() as repo:
            stage(repo, {
                "ResearchSystem/mypkg/lint.py": "x\n",
                CANDIDATE: "see `pkg/lint.py`\n",
            })
            self.assertEqual(candidate_path_check.check(repo.root), 1)

    def test_a_directory_token_resolves_through_its_tracked_files(self):  # negative control
        with TempRepo() as repo:
            stage(repo, {
                "ResearchSystem/schema/pack/a.json": "{}\n",
                CANDIDATE: "the `ResearchSystem/schema/pack/` pack\n",
            })
            self.assertEqual(candidate_path_check.check(repo.root), 0)

    def test_a_relative_token_resolves_from_the_containing_file(self):  # negative control
        with TempRepo() as repo:
            stage(repo, {
                "ResearchSystem/contract/amendments/sibling.md": "x\n",
                CANDIDATE: "see `amendments/sibling.md`\n",
            })
            self.assertEqual(candidate_path_check.check(repo.root), 0)

    def test_a_token_without_a_slash_is_never_path_shaped(self):  # negative control
        with TempRepo() as repo:
            stage(repo, {CANDIDATE: "the `lint.py` module, discussed by name\n"})
            self.assertEqual(candidate_path_check.check(repo.root), 0)

    def test_a_bare_single_segment_directory_is_prose(self):  # negative control
        # 78 distinct such tokens sit in the tracked corpus; one slash is not a citation.
        for token in ("vendor/", "raw/", "docs/", ".venv/", "../"):
            with self.subTest(token=token):
                with TempRepo() as repo:
                    stage(repo, {CANDIDATE: f"kept under `{token}` by convention\n"})
                    self.assertEqual(candidate_path_check.check(repo.root), 0)

    def test_a_directory_with_an_interior_slash_is_still_a_citation(self):  # must fire
        with TempRepo() as repo:
            stage(repo, {CANDIDATE: "see `tooling/no-such-dir/`\n"})
            self.assertEqual(candidate_path_check.check(repo.root), 1)

    def test_a_pre_existing_token_is_not_this_batchs_to_repair(self):  # B1 negative control
        with TempRepo() as repo:
            repo.write({CANDIDATE: f"old `{self.A3_DEFECT}` mention\n"})
            git(repo.root, "add", "--", CANDIDATE)
            git(repo.root, "commit", "-qm", "pre-existing token")
            stage(repo, {CANDIDATE: f"old `{self.A3_DEFECT}` mention\na new clean line\n"})
            self.assertEqual(candidate_path_check.check(repo.root), 0)


class OneNotionOfAPath(unittest.TestCase):
    """The two guards disagree on verdicts by design, and must agree on what a path IS.

    `layer_path_check` stays stdlib-only on purpose — it is existence-guarded on the script,
    not on its imports, so making it import `rsclib` would let a broken package silently
    disarm the older guard. That robustness is worth one duplicated pattern; what it is not
    worth is a silent divergence, which is the shape rider `E10-sync` banks for prose. So the
    duplication is pinned here rather than removed, and the pin is a real assertion: tighten
    one pattern without the other and this fails.
    """

    def test_both_guards_recognise_the_same_token_shape(self):
        self.assertEqual(paths._TOKEN.pattern, layer_path_check.TOKEN.pattern)

    def test_both_guards_recognise_the_same_path_shape(self):
        self.assertEqual(paths._PATHLIKE.pattern, layer_path_check.PATHLIKE.pattern)


class UntrackableByDesign(unittest.TestCase):
    """Trees git never tracks, so the index cannot answer and the lint must not block.

    Not a hypothetical: the guard's first live run blocked its own round on these two
    paths, both legitimate references in the harness README. E5 — the expectation is this
    hand-written pair, never the module's own tuple; narrowing `UNTRACKABLE` to nothing
    would otherwise go unnoticed until it blocked a commit again.
    """

    EXPECTED_UNTRACKABLE = (".git/", ".harness/")

    def test_untrackable_equals_the_hand_written_pair(self):
        self.assertEqual(tuple(paths.UNTRACKABLE), self.EXPECTED_UNTRACKABLE)

    def test_the_two_real_false_positives_pass(self):  # negative control
        for token in (".git/hooks/", ".harness/review-pending.json"):
            with self.subTest(token=token):
                with TempRepo() as repo:
                    stage(repo, {CANDIDATE: f"the untracked `{token}` state\n"})
                    self.assertEqual(candidate_path_check.check(repo.root), 0)

    def test_the_exemption_is_prefix_bound_not_substring(self):  # must fire
        # `docs/.harness/gone.json` is not the runtime tree; only a leading match exempts.
        with TempRepo() as repo:
            stage(repo, {CANDIDATE: "see `docs/.harness/gone.json`\n"})
            self.assertEqual(candidate_path_check.check(repo.root), 1)

    def test_a_tracked_path_is_still_judged_normally(self):  # must fire
        with TempRepo() as repo:
            stage(repo, {CANDIDATE: "see `Thesis/no/such/file.md`\n"})
            self.assertEqual(candidate_path_check.check(repo.root), 1)


class CandidateScanScope(unittest.TestCase):
    """The record surface must stay unscanned, or rider `freeze-audit` reappears.

    E5: the expectation is this hand-written list, never the module's own tuple. A surface
    silently dropped from `NOT_SCANNED` would start blocking returned review records, and
    `E9`'s freeze window admits only the record — leaving no legal commit ordering, which is
    exactly the deadlock the rider banks.
    """

    EXPECTED_NOT_SCANNED = (
        "ResearchSystem/migration/",
        "ResearchSystem/document-harness/journal/",
        "ResearchSystem/inventory/amendments/",
        "ResearchSystem/HARNESS-LEDGER.md",
        "ResearchSystem/HARNESS-LEDGER-archive.md",
        "ResearchSystem/HARNESS-RIDERS.md",
        "ResearchSystem/HARNESS-DECISIONS-archive.md",
        ".goals/LEDGER.md",
        ".goals/LEDGER-archive.md",
        "ResearchSystem/assurance/runs/",
        ".claude/",
        ".agents/",
    )

    #: One concrete path per excluded surface — the equality above pins the set, these
    #: prove each entry is actually reached by the scan filter.
    RECORD_PATHS = (
        "ResearchSystem/migration/document-work-assurance-v3/v3-review-full-abc1234.md",
        "ResearchSystem/document-harness/journal/some-round-2026-08-06.md",
        "ResearchSystem/HARNESS-LEDGER.md",
        "ResearchSystem/HARNESS-LEDGER-archive.md",
        "ResearchSystem/HARNESS-RIDERS.md",
        "ResearchSystem/HARNESS-DECISIONS-archive.md",
        ".goals/LEDGER.md",
        ".goals/LEDGER-archive.md",
        "ResearchSystem/assurance/runs/p5b-claims/instruction.md",
        ".claude/skills/vendored/SKILL.md",
        ".agents/skills/vendored/SKILL.md",
    )

    def test_not_scanned_equals_the_hand_written_list(self):
        self.assertEqual(tuple(candidate_path_check.NOT_SCANNED), self.EXPECTED_NOT_SCANNED)

    def test_the_three_kinds_partition_not_scanned(self):
        """The grouping is the reason; a surface added to none of the three is unexplained."""
        self.assertEqual(
            tuple(candidate_path_check.RECORD_SURFACE)
            + tuple(candidate_path_check.SPECIFICATION_SURFACE)
            + tuple(candidate_path_check.VENDORED),
            self.EXPECTED_NOT_SCANNED,
        )

    def test_every_excluded_surface_may_quote_a_broken_path(self):
        for path in self.RECORD_PATHS:
            with self.subTest(surface=path):
                with TempRepo() as repo:
                    stage(repo, {path: "reporting `Thesis/no/such/file.md` as broken\n"})
                    self.assertEqual(candidate_path_check.check(repo.root), 0)

    def test_an_instruction_may_name_the_file_it_requires(self):  # the 5-of-6 defect
        # The ordinary R1 sentence, verbatim in shape from p5a-firewall:22 and
        # p5b-firewall:25. At freeze time the named file cannot exist — that is what the
        # requirement is for. Five of the six freezes in this repository's history would
        # have been blocked by the first form of this guard.
        with TempRepo() as repo:
            stage(repo, {
                "ResearchSystem/assurance/runs/p5b-claims/instruction.md":
                    "A new file `ResearchSystem/inventory/amendments/"
                    "2026-08-07-p5b-claims.md` exists, accounting for every unit.\n",
            })
            self.assertEqual(candidate_path_check.check(repo.root), 0)

    def test_a_work_product_naming_the_same_missing_file_still_blocks(self):  # must fire
        with TempRepo() as repo:
            stage(repo, {
                CANDIDATE: "hosted in `ResearchSystem/inventory/amendments/"
                           "2026-08-07-p5b-claims.md`\n",
            })
            self.assertEqual(candidate_path_check.check(repo.root), 1)

    def test_a_non_markdown_file_is_never_scanned(self):  # negative control
        with TempRepo() as repo:
            stage(repo, {"ResearchSystem/tooling/x.py": "# `Thesis/no/such/file.md`\n"})
            self.assertEqual(candidate_path_check.check(repo.root), 0)

    def test_a_scanned_surface_next_to_an_excluded_one_still_blocks(self):  # must fire
        with TempRepo() as repo:
            stage(repo, {
                "ResearchSystem/HARNESS-RIDERS.md": "quoting `Thesis/no/such/file.md`\n",
                CANDIDATE: "hosted in `Thesis/no/such/file.md`\n",
            })
            self.assertEqual(candidate_path_check.check(repo.root), 1)


class NonAsciiFilenames(unittest.TestCase):
    """A path git C-quotes must not take its whole file out of the scan.

    Git quotes any path carrying a byte outside ASCII unless `core.quotepath=off`, so the
    name arrives wrapped in literal quotes, no longer ends in `.md`, and `scanned()` drops
    it — with every token in it. Inert in this repository today (`git ls-files | grep -c
    '^"'` → 0) and a silence rather than an error, which is why it needs a test rather than
    a note: nothing would announce it on the day the first such file lands.
    """

    NAME = "Thesis/笔记/note.md"

    def test_a_non_ascii_named_work_product_is_still_scanned(self):  # must fire
        with TempRepo() as repo:
            stage(repo, {self.NAME: "hosted in `Thesis/no/such/file.md`\n"})
            self.assertEqual(candidate_path_check.check(repo.root), 1)

    def test_the_same_file_with_a_clean_path_passes(self):  # negative control
        with TempRepo() as repo:
            stage(repo, {self.NAME: "hosted in `Thesis/no/such/file.md`\n"})
            repo.write({self.NAME: "no citation here at all\n"})
            git(repo.root, "add", "--", self.NAME)
            self.assertEqual(candidate_path_check.check(repo.root), 0)

    def test_an_ascii_directory_holding_one_resolves(self):  # must NOT fire — rider qp-index
        """The other half of the same quoting: the INDEX side, which blocks instead of missing.

        `TrackedPaths.from_index` registers the directories implied by tracked files. A
        C-quoted entry implies quoted ancestors, so a directory whose only content carries a
        non-ASCII segment resolves nowhere and a correct citation of it is reported —
        a false block, one grade worse than the silent miss above, because it is what
        `--no-verify` gets used for. The citation itself is plain ASCII — only the tracked
        file below it is not, so no amount of care in the citing document avoids this.

        Inverse shape to its neighbours, and labelled accordingly (FULL `297bb2b` `O-5`):
        it asserts exit 0, so what proves it binds is the mutation, not a companion
        must-fire — neutering `from_index`'s `core.quotepath=off` turns it red with the
        real message, `pre-commit BLOCKED: … 'ResearchSystem/notes/'`.
        """
        with TempRepo() as repo:
            stage(repo, {
                "ResearchSystem/notes/笔记/x.md": "content\n",
                CANDIDATE: "the notes live under `ResearchSystem/notes/`\n",
            })
            self.assertEqual(candidate_path_check.check(repo.root), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
