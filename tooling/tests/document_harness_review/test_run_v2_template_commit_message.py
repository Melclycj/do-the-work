#!/usr/bin/env python3
"""Item 4 — the evidence commit's message is the author's, and its absence is refused.

Batch `PROMISE-PATH`, round `PROMISE-PATH-ENGINE`. ``run_evidence_v2`` committed with a
hard-coded one-line f-string, ``f"{RUN_ID} evidence commit (control plane; candidate ...)"``,
so a title and a body the orchestrator is obliged to require could not land on an evidence
commit at all: `E8` asks for a single dense title naming the round and one dense paragraph
naming the commit's kind, and the caller's `2c6ed15` carries the template's own string and no
tier declaration. The step now takes the message as an argument (inline or from a file), uses
it verbatim, and refuses its absence.

What is deliberately NOT checked, and the tests that pin the line: whether the title names the
round, and whether the body names the commit's kind. Both are judgments about CONTENT, and a
template that scored them would be grading the author against a vocabulary this instrument
does not own — the same reason ``fulfillment.json`` carries no derived status and
``bind-declarations.json`` no default ``skip_reason``. What is checked is the STRUCTURE `E8`
needs in order to be meetable at all: a title, a blank line, a body.

Every expectation is a hand-written literal, never imported from the template (E5), and every
must-fire case is paired with a negative control (E4). ``main`` returning ``None`` means it
ran PAST the refusals and died downstream, so "the guard did not fire" fails on a VALUE rather
than as a test ERROR (R8).
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

CONTROL_ROOT = "ResearchSystem/assurance/runs/tr-msg"
OBLIGATIONS = [{"obligation_id": "ob-one", "verification_mode": "review_only"}]
LOCATOR = {"path": "docs/thing.md", "anchor": "## The Thing"}
STATE = {
    "work_id": "w-test",
    "run_id": "tr-msg",
    "status": "EXECUTING",
    "repair_round": 0,
    "work_spec_ref": {"path": f"{CONTROL_ROOT}/control/work-spec.json"},
    "resolved_plan_ref": {"path": f"{CONTROL_ROOT}/control/resolved-plan.json"},
}

#: A message with every part the structure rules ask for. Its words are a fixture's, which is
#: the point: the template supplies none of them.
GOOD = (
    "p9-notes evidence commit: the control plane at repair round 0\n"
    "\n"
    "Kind: evidence commit. Regenerates fulfillment, manifest, coverage and every check "
    "result against candidate c1, and stages the run's control root explicitly.\n"
)

ABSENT_STOP = ("STOP: supply the evidence commit's message with exactly one of "
               "--commit-message or --commit-message-file")


def load_template():
    """Bind the template file directly; never by adding its directory to sys.path."""
    if not TEMPLATE_PATH.is_file():
        raise RuntimeError(f"the v2 evidence template is missing at {TEMPLATE_PATH}")
    spec = importlib.util.spec_from_file_location("v2_evidence_message", TEMPLATE_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules.setdefault("v2_evidence_message", module)
    spec.loader.exec_module(module)
    return module


class TheStructureRulesAreTheOnlyThingStillHardCoded(unittest.TestCase):
    """`commit_message_fault` in isolation: three rules, each with its own literal.

    Asserted against the WHOLE returned sentence, not a substring, so a rule that started
    reporting a different fault than it detected would fail here.
    """

    def setUp(self):
        self.template = load_template()

    def test_a_message_with_no_title_is_named(self):
        self.assertEqual(
            self.template.commit_message_fault("\n\nKind: evidence commit. A body.\n"),
            "the message has no title: the first line is empty",
        )

    def test_a_title_and_nothing_else_is_named(self):
        self.assertEqual(
            self.template.commit_message_fault("p9-notes evidence commit"),
            "the message is a title and nothing else; E8 asks for a title AND one dense "
            "paragraph naming the commit's kind",
        )

    def test_a_title_run_into_its_body_is_named(self):
        self.assertEqual(
            self.template.commit_message_fault(
                "p9-notes evidence commit\nKind: evidence commit. A body.\nmore\n"),
            "the second line is not blank, so the title and the body are one paragraph; git "
            "reads the first line as the subject and everything after the blank line as the "
            "body",
        )

    def test_a_title_and_a_blank_line_and_no_body_is_named(self):
        self.assertEqual(
            self.template.commit_message_fault("p9-notes evidence commit\n\n   \n"),
            "the message has a title and a blank line but no body",
        )

    def test_negative_control_a_well_shaped_message_has_no_fault(self):
        self.assertIsNone(self.template.commit_message_fault(GOOD))

    def test_negative_control_the_shape_is_all_that_is_judged(self):
        """The line this round draws: no vocabulary check on the title or the kind.

        A message that names no round and declares no kind is structurally fine and passes.
        Deleting this method would let a later round quietly add a content rule and call it
        a bug fix, which is the thing the plan's item 4 explicitly does not ask for.
        """
        self.assertIsNone(self.template.commit_message_fault("x\n\ny\n"))


class TheMessageIsRefusedBeforeAnythingIsRead(unittest.TestCase):
    """The step's own refusals, driven through `main()` against a throwaway run."""

    def setUp(self):
        self.template = load_template()
        root = pathlib.Path(tempfile.mkdtemp(prefix="v2-evidence-msg-"))
        self.addCleanup(shutil.rmtree, root, ignore_errors=True)
        subprocess.run(
            ["git", "-C", str(root), "init", "-q"], check=True, stdout=subprocess.DEVNULL
        )
        self.root = root
        self.run_dir = root / CONTROL_ROOT
        self.control = self.run_dir / "control"
        self.control.mkdir(parents=True)
        (self.control / "work-spec.json").write_text(
            json.dumps({"obligations": OBLIGATIONS}), encoding="utf-8")
        (self.control / "resolved-plan.json").write_text(
            json.dumps({"effective_change_boundary": {"write_scope": [], "out": []}}),
            encoding="utf-8")
        (self.control / "state.json").write_text(json.dumps(STATE), encoding="utf-8")
        (self.control / "fulfillment.json").write_text(
            json.dumps({"ob-one": {"status": "IMPLEMENTED",
                                   "implementation_locators": [LOCATOR]}}),
            encoding="utf-8")

    def run_main(self, *message_args) -> tuple[int | None, str]:
        captured = io.StringIO()
        try:
            with contextlib.redirect_stdout(captured):
                code = self.template.main([
                    str(self.run_dir),
                    "--base", "b" * 40,
                    "--candidate", "c" * 40,
                    "--candidate-branch", "run/tr-msg-candidate",
                    *message_args,
                ])
        except Exception:
            return None, captured.getvalue()
        return code, captured.getvalue()

    # --- must fire ---------------------------------------------------------------------

    def test_no_message_at_all_refuses_the_run(self):
        code, out = self.run_main()
        self.assertEqual(code, 1, out)
        self.assertIn(ABSENT_STOP, out.splitlines())
        self.assertIn(
            "      E8: a single dense title naming the round, then one dense paragraph "
            "naming the commit's kind; this script supplies neither",
            out.splitlines(),
        )

    def test_both_forms_at_once_refuses_the_run(self):
        """Two sources for one fact is the shape this repository keeps paying for."""
        path = self.root / "message.txt"
        path.write_text(GOOD, encoding="utf-8")
        code, out = self.run_main(
            "--commit-message", GOOD, "--commit-message-file", str(path))
        self.assertEqual(code, 1, out)
        self.assertIn(ABSENT_STOP, out.splitlines())

    def test_a_message_file_that_is_not_there_refuses_the_run(self):
        missing = self.root / "nowhere.txt"
        code, out = self.run_main("--commit-message-file", str(missing))
        self.assertEqual(code, 1, out)
        self.assertIn(
            f"STOP: --commit-message-file names {missing}, which does not exist",
            out.splitlines(),
        )

    def test_a_malformed_message_refuses_the_run_and_names_the_fault(self):
        code, out = self.run_main("--commit-message", "p9-notes evidence commit")
        self.assertEqual(code, 1, out)
        self.assertIn(
            "STOP: the evidence commit message is malformed — the message is a title and "
            "nothing else; E8 asks for a title AND one dense paragraph naming the commit's "
            "kind",
            out.splitlines(),
        )

    def test_the_refusal_happens_before_the_run_directory_is_even_read(self):
        """The evidence commit is irreversible and the checks take minutes, so this is first.

        Driven at a run directory that does not exist: a refusal that came later would raise
        on the absent control plane and return None instead of 1.
        """
        captured = io.StringIO()
        with contextlib.redirect_stdout(captured):
            code = self.template.main([
                str(self.root / "no" / "such" / "run"),
                "--base", "b" * 40,
                "--candidate", "c" * 40,
                "--candidate-branch", "run/tr-msg-candidate",
            ])
        self.assertEqual(code, 1)
        self.assertIn(ABSENT_STOP, captured.getvalue().splitlines())

    # --- must not fire -----------------------------------------------------------------

    def test_negative_control_a_well_shaped_inline_message_passes_the_guards(self):
        code, out = self.run_main("--commit-message", GOOD)
        self.assertIsNone(code, out)  # walks on and dies on the absent commits downstream
        self.assertNotIn(ABSENT_STOP, out)
        self.assertNotIn("STOP: the evidence commit message is malformed", out)

    def test_negative_control_the_same_message_from_a_file_passes_too(self):
        path = self.root / "message.txt"
        path.write_text(GOOD, encoding="utf-8")
        code, out = self.run_main("--commit-message-file", str(path))
        self.assertIsNone(code, out)
        self.assertNotIn(ABSENT_STOP, out)


class TheAuthorsBytesAreWhatIsCommitted(unittest.TestCase):
    """The committed message is the one that was supplied -- read back out of git.

    Driven against a real throwaway repository rather than a recorder, because "verbatim" is
    a claim about what git stored and a recorded argv would only show what was passed. The
    expectation is the fixture string itself, compared whole: a template that prefixed the
    run id, appended the candidate SHA or added a trailer -- each of which the replaced
    hard-coded f-string did -- fails on the VALUE.
    """

    def setUp(self):
        self.template = load_template()
        self.repo = pathlib.Path(tempfile.mkdtemp(prefix="v2-evidence-commit-"))
        self.addCleanup(shutil.rmtree, self.repo, ignore_errors=True)
        for argv in (
            ["init", "-q"],
            ["config", "user.email", "fixture@example.invalid"],
            ["config", "user.name", "fixture"],
            ["config", "commit.gpgsign", "false"],
        ):
            subprocess.run(["git", "-C", str(self.repo), *argv], check=True,
                           stdout=subprocess.DEVNULL)
        staged = self.repo / CONTROL_ROOT / "control"
        staged.mkdir(parents=True)
        (staged / "state.json").write_text(json.dumps(STATE), encoding="utf-8")

    def committed_message(self) -> str:
        return subprocess.run(
            ["git", "-C", str(self.repo), "log", "-1", "--format=%B"],
            check=True, capture_output=True, text=True,
        ).stdout

    def test_the_message_git_stored_is_the_message_that_was_supplied(self):
        self.template.commit_control_plane(self.repo, CONTROL_ROOT, GOOD)
        # `git log --format` appends one record separator after the format it renders, so
        # the stored message is the supplied one and the trailing newline below is git's,
        # not the step's. Written out rather than stripped: a comparison that rstrips both
        # sides would also pass for a step that appended a trailer.
        self.assertEqual(self.committed_message(), GOOD + "\n")

    def test_the_title_git_reports_is_the_authors_first_line(self):
        """The half the replaced one-liner made impossible: a subject and a body."""
        self.template.commit_control_plane(self.repo, CONTROL_ROOT, GOOD)
        subject = subprocess.run(
            ["git", "-C", str(self.repo), "log", "-1", "--format=%s"],
            check=True, capture_output=True, text=True,
        ).stdout.strip()
        body = subprocess.run(
            ["git", "-C", str(self.repo), "log", "-1", "--format=%b"],
            check=True, capture_output=True, text=True,
        ).stdout.strip()
        self.assertEqual(subject, "p9-notes evidence commit: the control plane at repair "
                                  "round 0")
        self.assertTrue(body.startswith("Kind: evidence commit."), body)

    def test_only_the_named_control_root_is_staged(self):
        """Negative control for the other half of the act: explicit paths, never add -A."""
        stray = self.repo / "unrelated.txt"
        stray.write_text("not this run's\n", encoding="utf-8")
        self.template.commit_control_plane(self.repo, CONTROL_ROOT, GOOD)
        committed = subprocess.run(
            ["git", "-C", str(self.repo), "show", "--name-only", "--format=", "HEAD"],
            check=True, capture_output=True, text=True,
        ).stdout.split()
        self.assertEqual(committed, [f"{CONTROL_ROOT}/control/state.json"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
