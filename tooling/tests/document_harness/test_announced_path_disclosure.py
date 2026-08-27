#!/usr/bin/env python3
"""Acceptance matrix for `tooling/announced_path_disclosure.py` — `E2`'s CI alarm.

This one IS a guard: it returns a non-zero exit and a required status check hangs on it, so
`E4` applies in full — every must-fire case below is paired with a negative control asserted
in the same test, because a red that fires on everything proves nothing. The mutation record
(neuter → red → restore) rides the round's commit body, not this file.

The announced list is pinned as a hand-written literal (`E5`), never read back from the
module and never derived from the schema directory: `E2` names the fifteen files the pack held
at the 2026-08-03 re-baseline, so a schema added later must NOT be watched until a re-baseline
enrols it, and a test that listed the directory would call that silent enrolment correct.

Each test drives `check(repo_root, before, after)` against a disposable repository, which is
the same entry the CI step calls through `main`. The alarm's floor — the commit that first
added the script — is exercised by creating a file at that path inside the temp repository;
where a test does not create it, no floor is found and the whole range is judged, which is the
strict fallback and the state most of these cases want.
"""
from __future__ import annotations

import contextlib
import io
import unittest

from _harness import TempRepo, git

import announced_path_disclosure as alarm

#: Hand-written (E5). One announced path plus one that is not, so every must-fire case has a
#: shape that must stay green beside it.
CONTRACT = "contract/Document-Work-Assurance-Contract-v4.md"
SCHEMA = "schema/document-assurance-v3/review.schema.json"
NOT_ANNOUNCED = "document-harness/CONSTRUCTION-CHECKLIST.md"


def run(repo, before, after):
    """`check` plus its stdout — the failure text is part of what this guard has to deliver."""
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        code = alarm.check(repo.root, before, after)
    return code, buffer.getvalue()


def commit(repo, files, message):
    repo.write(files)
    git(repo.root, "add", "--", *files.keys())
    git(repo.root, "commit", "-qm", message)
    return repo.head()


class AnnouncedList(unittest.TestCase):
    EXPECTED = (
        "contract/Document-Work-Assurance-Contract-v4.md",
        "schema/document-assurance-v3/assurance-work-state.schema.json",
        "schema/document-assurance-v3/assurance.schema.json",
        "schema/document-assurance-v3/candidate-record.schema.json",
        "schema/document-assurance-v3/common.schema.json",
        "schema/document-assurance-v3/document-assurance-profile.schema.json",
        "schema/document-assurance-v3/document-work-spec.schema.json",
        "schema/document-assurance-v3/document-work-spec.v2.schema.json",
        "schema/document-assurance-v3/harness-issue.schema.json",
        "schema/document-assurance-v3/instruction-coverage-audit.schema.json",
        "schema/document-assurance-v3/local-check-spec.schema.json",
        "schema/document-assurance-v3/paragraph-map.schema.json",
        "schema/document-assurance-v3/resolved-assurance-plan.schema.json",
        "schema/document-assurance-v3/review.schema.json",
        "schema/document-assurance-v3/review.v2.schema.json",
        "schema/document-assurance-v3/user-decision.schema.json",
    )

    def test_announced_equals_the_hand_written_list(self):
        self.assertEqual(tuple(alarm.ANNOUNCED), self.EXPECTED)

    def test_the_list_is_sixteen_paths(self):
        """E2's own count: one contract plus the fifteen of the 2026-08-03 re-baseline."""
        self.assertEqual(len(self.EXPECTED), 16)

    def test_every_announced_path_is_watched(self):
        """The equality above pins the set; this proves each member is actually reached."""
        for path in self.EXPECTED:
            with self.subTest(announced=path):
                with TempRepo() as repo:
                    head = commit(repo, {path: "changed\n"}, "no disclosure here")
                    code, out = run(repo, repo.base, head)
                    self.assertEqual(code, 1)
                    self.assertIn(path, out)


class DisclosurePredicate(unittest.TestCase):
    def test_a_commit_naming_the_full_path_passes(self):  # negative control
        with TempRepo() as repo:
            head = commit(repo, {CONTRACT: "x\n"}, f"rewrote a line of {CONTRACT} for reason R")
            code, out = run(repo, repo.base, head)
            self.assertEqual(code, 0, out)

    def test_a_commit_not_naming_the_path_fails(self):  # must fire
        with TempRepo() as repo:
            head = commit(repo, {CONTRACT: "x\n"}, "rewrote a line of the contract for reason R")
            code, out = run(repo, repo.base, head)
            self.assertEqual(code, 1)
            self.assertIn(head, out)
            self.assertIn(CONTRACT, out)

    def test_a_basename_alone_does_not_satisfy_the_predicate(self):
        """Naming test (a), not the declined (b): the FULL repo-relative path or nothing."""
        with TempRepo() as repo:
            head = commit(
                repo,
                {CONTRACT: "x\n"},
                "rewrote a line of Document-Work-Assurance-Contract-v4.md for reason R",
            )
            code, out = run(repo, repo.base, head)
            self.assertEqual(code, 1)
            self.assertIn(CONTRACT, out)

    def test_a_commit_touching_nothing_announced_passes(self):  # negative control
        with TempRepo() as repo:
            head = commit(repo, {NOT_ANNOUNCED: "x\n"}, "no announced path here at all")
            code, out = run(repo, repo.base, head)
            self.assertEqual(code, 0, out)

    def test_naming_one_of_two_changed_paths_still_fails_on_the_other(self):
        with TempRepo() as repo:
            head = commit(
                repo,
                {CONTRACT: "x\n", SCHEMA: "{}\n"},
                f"changed {CONTRACT} and something else",
            )
            code, out = run(repo, repo.base, head)
            self.assertEqual(code, 1)
            self.assertIn(SCHEMA, out)
            self.assertNotIn(f"changed {CONTRACT} —", out)


class PerCommitEvaluation(unittest.TestCase):
    """`E2` binds each commit to its OWN body; a later apology cannot cover an earlier write."""

    def test_a_later_commit_naming_the_path_does_not_rescue_an_earlier_one(self):
        with TempRepo() as repo:
            silent = commit(repo, {CONTRACT: "x\n"}, "changed the contract, said nothing")
            head = commit(repo, {NOT_ANNOUNCED: "y\n"}, f"for the record, {CONTRACT} moved")
            code, out = run(repo, repo.base, head)
            self.assertEqual(code, 1)
            self.assertIn(silent, out)

    def test_a_clean_earlier_commit_leaves_a_dirty_later_one_visible(self):
        with TempRepo() as repo:
            commit(repo, {CONTRACT: "x\n"}, f"changed {CONTRACT} and said so")
            dirty = commit(repo, {SCHEMA: "{}\n"}, "changed a schema, said nothing")
            code, out = run(repo, repo.base, repo.head())
            self.assertEqual(code, 1)
            self.assertIn(dirty, out)


class MergeCommits(unittest.TestCase):
    def test_a_merge_commit_is_skipped(self):
        """Its changes belong to the commits it merges, which are judged on their own."""
        with TempRepo() as repo:
            git(repo.root, "checkout", "-q", "-b", "side")
            commit(repo, {NOT_ANNOUNCED: "side\n"}, "a side change naming nothing")
            git(repo.root, "checkout", "-q", "main")
            base = commit(repo, {CONTRACT: "x\n"}, f"changed {CONTRACT} and said so")
            git(repo.root, "merge", "-q", "--no-ff", "-m", "merge side", "side")
            code, out = run(repo, base, repo.head())
            self.assertEqual(code, 0, out)
            # The range holds two commits, one of them the merge. Asserting the count is what
            # binds `--no-merges`: a merge commit's own diff-tree is empty without conflicts,
            # so judging it would stay green and the skip would be untested.
            self.assertIn("1 non-merge commit(s) judged", out)

    def test_the_merged_commits_are_still_judged(self):  # the pair's must-fire half
        with TempRepo() as repo:
            git(repo.root, "checkout", "-q", "-b", "side")
            silent = commit(repo, {CONTRACT: "x\n"}, "a side change naming nothing")
            git(repo.root, "checkout", "-q", "main")
            base = commit(repo, {NOT_ANNOUNCED: "main\n"}, "an unrelated main change")
            git(repo.root, "merge", "-q", "--no-ff", "-m", "merge side", "side")
            code, out = run(repo, base, repo.head())
            self.assertEqual(code, 1)
            self.assertIn(silent, out)
            self.assertIn("1 non-merge commit(s) judged", out)


class NoRange(unittest.TestCase):
    """A push that creates a branch sends an all-zeros `before` — head alone, never all history."""

    def test_all_zeros_before_judges_the_head_commit_and_fires(self):
        with TempRepo() as repo:
            commit(repo, {CONTRACT: "x\n"}, "an older silent change to the contract")
            head = commit(repo, {SCHEMA: "{}\n"}, "a newer silent change to a schema")
            code, out = run(repo, alarm.NO_RANGE, head)
            self.assertEqual(code, 1)
            self.assertIn("1 non-merge commit(s) judged", out)
            self.assertIn(SCHEMA, out)
            self.assertNotIn(CONTRACT, out)

    def test_all_zeros_before_stays_green_when_the_head_discloses(self):  # negative control
        with TempRepo() as repo:
            commit(repo, {CONTRACT: "x\n"}, "an older silent change to the contract")
            head = commit(repo, {SCHEMA: "{}\n"}, f"a newer change to {SCHEMA}, disclosed")
            code, out = run(repo, alarm.NO_RANGE, head)
            self.assertEqual(code, 0, out)

    def test_an_empty_before_is_treated_as_no_range(self):
        with TempRepo() as repo:
            commit(repo, {CONTRACT: "x\n"}, "an older silent change to the contract")
            head = commit(repo, {NOT_ANNOUNCED: "y\n"}, "a newer harmless change")
            code, out = run(repo, "", head)
            self.assertEqual(code, 0, out)


class Floor(unittest.TestCase):
    """Commits made before the alarm landed are not re-judged, and the floor is derived."""

    def test_a_commit_below_the_alarms_own_landing_is_not_judged(self):
        with TempRepo() as repo:
            commit(repo, {CONTRACT: "x\n"}, "a silent pre-alarm change to the contract")
            commit(repo, {alarm.SELF_PATH: "the alarm lands here\n"}, "land the alarm")
            head = commit(repo, {NOT_ANNOUNCED: "y\n"}, "a harmless post-alarm change")
            code, out = run(repo, repo.base, head)
            self.assertEqual(code, 0, out)
            self.assertIn("1 non-merge commit(s) judged", out)

    def test_a_commit_above_the_floor_is_judged(self):  # the pair's must-fire half
        with TempRepo() as repo:
            commit(repo, {alarm.SELF_PATH: "the alarm lands here\n"}, "land the alarm")
            head = commit(repo, {CONTRACT: "x\n"}, "a silent post-alarm change")
            code, out = run(repo, repo.base, head)
            self.assertEqual(code, 1)
            self.assertIn(head, out)

    def test_no_floor_found_judges_the_whole_range_and_says_so(self):
        with TempRepo() as repo:
            head = commit(repo, {CONTRACT: "x\n"}, "a silent change with no alarm in history")
            code, out = run(repo, repo.base, head)
            self.assertEqual(code, 1)
            self.assertIn("none found", out)


if __name__ == "__main__":
    unittest.main()
