#!/usr/bin/env python3
"""`dtw init` — the two properties the command is load-bearing for.

`init` is the mechanical half of caller onboarding: `.harness/`, its ignore entry, and the two
empty instance files io-design §6 says ship from here. What can go wrong is not that it fails
loudly — it is that it succeeds while doing something subtly different, so exactly two
properties are pinned:

* **the copy is verbatim** — a caller's decision log must carry the header rules as this
  repository wrote them, not as a generator re-derived them. Byte equality against the tracked
  template catches any transformation (a decode/encode round trip normalising line endings is
  the near miss); the whole-line pins that follow catch a template hollowed out until byte
  equality holds trivially.
* **an existing file is never overwritten** — a re-run against a live caller must not clobber
  a decision log with rulings in it. The refusal is per file, not all-or-nothing, and it is
  reported by name.

`E5`: every expectation here is a hand-written literal or a file read from a hand-written
path, never `init_target`'s own constants — reading `TEMPLATES` back would assert that the
module equals itself, and a destination silently renamed is exactly what must fail. `E4`:
each must-fire case is preceded by the clean baseline that proves the same input passes when
the defect is absent.
"""
from __future__ import annotations

import hashlib
import pathlib
import subprocess
import sys
import tempfile
import unittest

import _harness

from rsclib.document_harness import init_target

#: Hand-written, never the module's `TEMPLATES` (E5). Source path -> destination name.
TEMPLATE_SOURCES = {
    "HARNESS-DECISIONS.md": _harness.RS_ROOT / "document-harness" / "templates" / "decision-log.md",
    "HARNESS-RIDERS.md": _harness.RS_ROOT / "document-harness" / "templates" / "rider-bank.md",
}

#: Whole lines (E5: never a substring unrelated content can satisfy). The first five are
#: io-design §6's five, in its order — 状态机四态 / scope 四档 / 准入三问 / 继承 / 删除纪律:
#: the state machine, the four scopes, the three admission questions, **inheritance**, and the
#: deletion discipline. The sixth, narrowing (`HD-30`), is **not** one of §6's five; it is
#: pinned as an extra because the template ships it and a template edited to drop it would
#: still be wrong.
#:
#: The inheritance line was missing until 2026-08-19 while this comment claimed it was here
#: (`v3-review-full-2026a14.md` `B-2`): dropping that block left the whole suite green, and it
#: is the block carrying "Every cold read MUST read `§live`" and the verbatim-inheritance rule
#: — the two `E10`/`HD-5` obligations that are the reason to ship a decision log at all. All
#: six blocks are now must-fire, each proven by deleting it from the template in turn.
DECISION_LOG_HEADER_LINES = (
    "> **State machine.** `live` (in force and required reading — ruled but not yet carried, or",
    "> **Scope.** `standing` (only supersedable) · `mechanism:<path>` (retires with the mechanism)",
    "> **Admission — three questions; any yes admits.** Does it bind the next round and beyond? ·",
    "> **Who reads it.** Every cold read MUST read `§live`, and only `§live`. A plan author reads",
    "> **Deletion — discipline, no lint.** Dead entries move to the archive file beside this one.",
    "> **Narrowing is not a fifth state.** A successor entry carries the narrowed text **in full**",
)

#: The rider bank's header points at the rule instead of restating it (io-design §6).
RIDER_BANK_HEADER_LINE = (
    "`R10` in the instrument's `CONSTRUCTION-CHECKLIST.md`. They are deliberately **not** restated"
)

SENTINEL = "# a live decision log with rulings in it\n"


def digest(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class Target:
    """A disposable target directory. Not a git repository: `init` never invokes git."""

    def __enter__(self) -> pathlib.Path:
        self._tmp = tempfile.TemporaryDirectory(prefix="dtw-init-")
        return pathlib.Path(self._tmp.name)

    def __exit__(self, *exc_info: object) -> None:
        self._tmp.cleanup()


class FreshTarget(unittest.TestCase):
    """The baseline every refusal case below is measured against (E4's negative control)."""

    def test_a_fresh_target_gets_both_instance_files(self):
        with Target() as root:
            result = init_target.init_target(root)
            for name in TEMPLATE_SOURCES:
                with self.subTest(instance=name):
                    self.assertTrue((root / name).is_file())
                    self.assertIn(name, result.created)

    def test_a_fresh_target_gets_the_runtime_directory_and_its_ignore_entry(self):
        with Target() as root:
            result = init_target.init_target(root)
            self.assertTrue((root / ".harness").is_dir())
            self.assertTrue(result.ignore_appended)
            self.assertEqual(
                (root / ".gitignore").read_text(encoding="utf-8").splitlines(), [".harness/"]
            )

    def test_nothing_else_is_written_into_the_target(self):
        with Target() as root:
            init_target.init_target(root)
            written = sorted(
                str(p.relative_to(root)).replace("\\", "/")
                for p in root.rglob("*")
            )
            self.assertEqual(
                written,
                [
                    ".gitignore",
                    ".harness",
                    ".harness/scan-surfaces.json",
                    "HARNESS-DECISIONS.md",
                    "HARNESS-RIDERS.md",
                ],
            )

    def test_the_declaration_carries_the_default_surfaces(self):
        """E5: the expected bytes are this hand-written literal, never the module's own
        renderer — a default silently dropped from the declaration `init` writes would
        re-scan the records of every caller that trusted `init`'s output as its schema."""
        with Target() as root:
            result = init_target.init_target(root)
            self.assertIn(".harness/scan-surfaces.json", result.created)
            self.assertEqual(
                (root / ".harness" / "scan-surfaces.json").read_text(encoding="utf-8"),
                "{\n"
                ' "record_surface": [\n'
                '  "HARNESS-RIDERS.md",\n'
                '  "journal/"\n'
                " ],\n"
                ' "review_record_dirs": [\n'
                '  "assurance/review-records/"\n'
                " ],\n"
                ' "specification_surface": [\n'
                '  "assurance/runs/"\n'
                " ]\n"
                "}\n",
            )


class TheCopyIsVerbatim(unittest.TestCase):
    def test_each_copy_is_byte_identical_to_its_tracked_template(self):
        with Target() as root:
            init_target.init_target(root)
            for name, source in TEMPLATE_SOURCES.items():
                with self.subTest(instance=name):
                    self.assertEqual((root / name).read_bytes(), source.read_bytes())

    def test_the_copied_decision_log_carries_every_pinned_header_rule(self):
        with Target() as root:
            init_target.init_target(root)
            lines = (root / "HARNESS-DECISIONS.md").read_text(encoding="utf-8").splitlines()
            for line in DECISION_LOG_HEADER_LINES:
                with self.subTest(rule=line[:40]):
                    self.assertIn(line, lines)

    def test_the_copied_decision_log_ships_with_no_entries(self):
        # An "empty instance" that arrived carrying this repository's own rulings would put
        # another repository's decisions into a caller's tree under its own name.
        with Target() as root:
            init_target.init_target(root)
            text = (root / "HARNESS-DECISIONS.md").read_text(encoding="utf-8")
            self.assertNotIn("\n### ", text)
            self.assertIn("_No entries yet._", text)

    def test_the_copied_rider_bank_points_at_the_rule_and_has_no_rows(self):
        with Target() as root:
            init_target.init_target(root)
            lines = (root / "HARNESS-RIDERS.md").read_text(encoding="utf-8").splitlines()
            self.assertIn(RIDER_BANK_HEADER_LINE, lines)
            self.assertEqual(lines[-1], "|---|---|---|---|")

    def test_the_instrument_s_own_templates_are_not_touched(self):
        before = {name: digest(path) for name, path in TEMPLATE_SOURCES.items()}
        with Target() as root:
            init_target.init_target(root)
        self.assertEqual({name: digest(path) for name, path in TEMPLATE_SOURCES.items()}, before)


class RefusesToOverwrite(unittest.TestCase):
    def test_an_existing_instance_file_keeps_its_bytes(self):  # must fire
        with Target() as root:
            (root / "HARNESS-DECISIONS.md").write_text(SENTINEL, encoding="utf-8")
            result = init_target.init_target(root)
            self.assertEqual((root / "HARNESS-DECISIONS.md").read_text(encoding="utf-8"), SENTINEL)
            self.assertIn("HARNESS-DECISIONS.md", result.already_present)
            self.assertNotIn("HARNESS-DECISIONS.md", result.created)

    def test_the_report_says_which_file_it_kept(self):  # must fire — "and says which"
        with Target() as root:
            (root / "HARNESS-DECISIONS.md").write_text(SENTINEL, encoding="utf-8")
            report = init_target.render(init_target.init_target(root)).splitlines()
            self.assertIn(
                "kept     : HARNESS-DECISIONS.md — already existed, left untouched", report
            )

    def test_a_fresh_target_s_report_keeps_nothing(self):  # negative control for both above
        with Target() as root:
            report = init_target.render(init_target.init_target(root)).splitlines()
            self.assertEqual([line for line in report if line.startswith("kept")], [])
            self.assertIn("created  : HARNESS-DECISIONS.md", report)

    def test_the_refusal_is_per_file_not_all_or_nothing(self):
        with Target() as root:
            (root / "HARNESS-DECISIONS.md").write_text(SENTINEL, encoding="utf-8")
            result = init_target.init_target(root)
            self.assertIn("HARNESS-RIDERS.md", result.created)
            self.assertTrue((root / "HARNESS-RIDERS.md").is_file())

    def test_an_edited_declaration_keeps_its_bytes(self):  # must fire
        """A caller's declared surfaces are exactly the adaptation `HD-34` tells them to
        keep; a re-run that reset them to defaults would silently re-scan its records."""
        with Target() as root:
            (root / ".harness").mkdir()
            (root / ".harness" / "scan-surfaces.json").write_text(SENTINEL, encoding="utf-8")
            result = init_target.init_target(root)
            self.assertEqual(
                (root / ".harness" / "scan-surfaces.json").read_text(encoding="utf-8"),
                SENTINEL,
            )
            self.assertIn(".harness/scan-surfaces.json", result.already_present)
            self.assertNotIn(".harness/scan-surfaces.json", result.created)

    def test_a_second_run_creates_nothing(self):  # must fire — idempotence is the re-run case
        with Target() as root:
            init_target.init_target(root)
            first = {name: digest(root / name) for name in TEMPLATE_SOURCES}
            second = init_target.init_target(root)
            self.assertEqual(second.created, ())
            self.assertEqual({name: digest(root / name) for name in TEMPLATE_SOURCES}, first)


class TheIgnoreEntry(unittest.TestCase):
    """Appending is not overwriting — the one file `init` may extend, and only by one line."""

    def test_an_existing_gitignore_keeps_its_bytes_and_gains_one_line(self):
        with Target() as root:
            (root / ".gitignore").write_text("__pycache__/\n*.pyc\n", encoding="utf-8")
            init_target.init_target(root)
            self.assertEqual(
                (root / ".gitignore").read_text(encoding="utf-8").splitlines(),
                ["__pycache__/", "*.pyc", ".harness/"],
            )

    def test_a_gitignore_without_a_trailing_newline_does_not_gain_a_glued_entry(self):
        with Target() as root:
            (root / ".gitignore").write_text("*.pyc", encoding="utf-8")
            init_target.init_target(root)
            self.assertEqual(
                (root / ".gitignore").read_text(encoding="utf-8").splitlines(),
                ["*.pyc", ".harness/"],
            )

    def test_a_second_run_adds_no_second_entry(self):  # must fire
        with Target() as root:
            init_target.init_target(root)
            result = init_target.init_target(root)
            self.assertFalse(result.ignore_appended)
            self.assertEqual(
                (root / ".gitignore").read_text(encoding="utf-8").count(".harness/"), 1
            )

    def test_the_slashless_spelling_counts_as_present(self):  # must fire
        with Target() as root:
            (root / ".gitignore").write_text(".harness\n", encoding="utf-8")
            result = init_target.init_target(root)
            self.assertFalse(result.ignore_appended)
            self.assertEqual(
                (root / ".gitignore").read_text(encoding="utf-8").splitlines(), [".harness"]
            )

    def test_a_lookalike_entry_does_not_count_as_present(self):  # negative control
        # `docs/.harness/` is not the runtime tree; only the entry itself exempts.
        with Target() as root:
            (root / ".gitignore").write_text("docs/.harness/\n", encoding="utf-8")
            result = init_target.init_target(root)
            self.assertTrue(result.ignore_appended)
            self.assertEqual(
                (root / ".gitignore").read_text(encoding="utf-8").splitlines(),
                ["docs/.harness/", ".harness/"],
            )


class ThroughTheCommandLine(unittest.TestCase):
    """The parser wiring and the report, driven the way a caller actually runs it."""

    def run_init(self, root: pathlib.Path) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, "dtw.py", "init", "--repo-root", str(root)],
            cwd=str(_harness.TOOLING_DIR),
            capture_output=True,
            encoding="utf-8",
            errors="replace",
        )

    def test_init_runs_from_another_directory_and_reports_what_it_did(self):
        with Target() as root:
            completed = self.run_init(root)
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertIn("created  : HARNESS-DECISIONS.md", completed.stdout.splitlines())
            self.assertTrue((root / "HARNESS-RIDERS.md").is_file())

    def test_the_report_names_what_it_deliberately_did_not_do(self):
        # The command's own output is the only place a caller who runs *only* this command
        # meets the five items it does not perform.
        with Target() as root:
            lines = self.run_init(root).stdout.splitlines()
            self.assertIn(
                "NOT done by this command — these are the procedure's, and are judgment:", lines
            )
            for item in (
                "  - mount the instrument as a submodule, and pin a revision",
                "  - write the caller's policy file",
                "  - add the one-line pointer to that policy file in CLAUDE.md / AGENTS.md",
                "  - wire a pre-commit hook, and run the per-machine core.hooksPath step",
                "  - the journal is not pre-created (one file per round) and the ledger has no template",
            ):
                with self.subTest(item=item):
                    self.assertIn(item, lines)

    def test_a_missing_target_is_a_fatal_not_a_silent_success(self):  # must fire
        with Target() as root:
            completed = self.run_init(root / "no-such-directory")
            self.assertEqual(completed.returncode, 2)
            self.assertIn("FATAL", completed.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
