#!/usr/bin/env python3
"""Round `CORE-ONLY-LAYER`: `harness.json`, the declaration E10's second sentence names.

The defect class this closes (E7): a rule a repository writes for itself is invisible to
every instrument the harness ships. `layer_path_check.py` scanned nine hard-coded members
and nothing else, so a dangling path newly written into a caller's own rule file passed
green; `sweep_refs.py` swept the same nine. Both now scan the members **plus** whatever the
repository declares under `rules`, and the declaration is one tracked file at its root.

Four properties, each with its negative control (E4) — a block proves nothing if the
baseline also blocks, and a report proves nothing if the clean tree also reports:

* **Absence is a real answer.** No `harness.json` means no declared rules and no policy
  file, which is a repository that has declared nothing rather than an error.
* **A declaration is read, not assumed.** The guard blocks a dangling path in a declared
  rule file, and the identical file with `rules` empty is not blocked — the pair is what
  shows the declaration is load-bearing rather than incidental.
* **A malformed declaration refuses loudly**, never a silent empty declaration: an
  unnoticed typo would stop both instruments scanning a repository's rules with every
  check still green, which is the failure the file exists to prevent.
* **The rendered bytes are pinned by hand** (E5) rather than by re-rendering, because an
  expectation computed from the module under test can only agree with it.

`test_init_command.py` pins that `dtw init` writes these bytes; `test_precommit_checks.py`
pins the guard's behaviour on the members themselves. This file is the declared path.
"""
from __future__ import annotations

import contextlib
import io
import json
import unittest

from _harness import TempRepo, git

import sweep_refs
from hooks import layer_path_check
from rsclib.document_harness import caller

#: Hand-written (E5), never `caller.HARNESS_CONFIG` or `layer_path_check.LAYER`. `OWN_RULE`
#: is deliberately a path no member list has ever held: the claim under test is that a
#: repository's *own* rule file becomes scannable by declaring it, so a path a later
#: membership change could pull in would make the negative controls stop meaning anything.
CONFIG = "harness.json"
OWN_RULE = "docs/MY-RULES.md"
MEMBER = "document-harness/README.md"

#: A backticked token that resolves nowhere, assembled here so no committed test file
#: carries a live broken path token (rider `decited-paths`' concern).
BAD_LINE = "a rule naming " + "`" + "document-harness/no-such-rule-surface.md" + "`" + "\n"
#: The same sentence with a token that does resolve — the negative control's whole point is
#: that only the token differs.
GOOD_LINE = "a rule naming " + "`" + "document-harness/README.md" + "`" + "\n"

#: The empty declaration `dtw init` writes, byte for byte.
EMPTY_BYTES = '{\n "policy": null,\n "rules": []\n}\n'


def declare(repo: TempRepo, payload) -> None:
    """Write `harness.json` at the repository root, JSON object or raw string."""
    text = payload if isinstance(payload, str) else json.dumps(payload)
    (repo.root / CONFIG).write_text(text, encoding="utf-8")


def stage(repo: TempRepo, files: dict[str, str]) -> None:
    repo.write(files)
    git(repo.root, "add", "--", *files.keys())


def run_sweep(repo: TempRepo) -> str:
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        sweep_refs.sweep(repo.root)
    return buffer.getvalue()


class Loading(unittest.TestCase):
    def test_absent_declaration_is_the_empty_declaration(self):
        with TempRepo() as repo:
            config = caller.load_harness_config(repo.root)
            self.assertIsNone(config.policy)
            self.assertEqual(config.rules, ())

    def test_declared_fields_are_returned_as_written(self):
        with TempRepo() as repo:
            declare(repo, {"policy": "CONSTRUCTION-LEDGER.md", "rules": [OWN_RULE]})
            config = caller.load_harness_config(repo.root)
            self.assertEqual(config.policy, "CONSTRUCTION-LEDGER.md")
            self.assertEqual(config.rules, (OWN_RULE,))

    def test_a_missing_field_keeps_its_empty_default(self):
        with TempRepo() as repo:
            declare(repo, {"rules": [OWN_RULE]})
            config = caller.load_harness_config(repo.root)
            self.assertIsNone(config.policy)
            self.assertEqual(config.rules, (OWN_RULE,))

    def test_null_policy_is_a_caller_that_wrote_none(self):
        with TempRepo() as repo:
            declare(repo, {"policy": None, "rules": []})
            self.assertIsNone(caller.load_harness_config(repo.root).policy)

    def test_unparseable_json_refuses_loudly(self):
        with TempRepo() as repo:
            declare(repo, "{not json")
            with self.assertRaises(caller.HarnessConfigError):
                caller.load_harness_config(repo.root)

    def test_a_json_array_refuses_loudly(self):
        with TempRepo() as repo:
            declare(repo, [OWN_RULE])
            with self.assertRaises(caller.HarnessConfigError):
                caller.load_harness_config(repo.root)

    def test_an_unknown_field_refuses_rather_than_being_ignored(self):
        with TempRepo() as repo:
            declare(repo, {"rulez": [OWN_RULE]})
            with self.assertRaises(caller.HarnessConfigError):
                caller.load_harness_config(repo.root)

    def test_a_non_string_rule_entry_refuses(self):
        with TempRepo() as repo:
            declare(repo, {"rules": [OWN_RULE, 7]})
            with self.assertRaises(caller.HarnessConfigError):
                caller.load_harness_config(repo.root)

    def test_an_empty_rule_entry_refuses(self):
        with TempRepo() as repo:
            declare(repo, {"rules": [""]})
            with self.assertRaises(caller.HarnessConfigError):
                caller.load_harness_config(repo.root)

    def test_a_non_string_policy_refuses(self):
        with TempRepo() as repo:
            declare(repo, {"policy": ["CONSTRUCTION-LEDGER.md"]})
            with self.assertRaises(caller.HarnessConfigError):
                caller.load_harness_config(repo.root)

    def test_rendered_bytes_are_the_hand_written_empty_declaration(self):
        self.assertEqual(caller.render_harness_config(), EMPTY_BYTES)

    def test_rendered_bytes_carry_a_declared_rule(self):
        rendered = caller.render_harness_config(
            caller.HarnessConfig(policy="POLICY.md", rules=(OWN_RULE,))
        )
        self.assertEqual(
            rendered,
            '{\n "policy": "POLICY.md",\n "rules": [\n  "' + OWN_RULE + '"\n ]\n}\n',
        )


class ScannedSurface(unittest.TestCase):
    def test_no_declaration_scans_the_members_alone(self):
        with TempRepo() as repo:
            self.assertEqual(
                layer_path_check.scanned_paths(repo.root),
                tuple(layer_path_check.LAYER),
            )

    def test_a_declared_rule_joins_the_scanned_surface(self):
        with TempRepo() as repo:
            declare(repo, {"rules": [OWN_RULE]})
            scanned = layer_path_check.scanned_paths(repo.root)
            self.assertEqual(scanned[: len(layer_path_check.LAYER)],
                             tuple(layer_path_check.LAYER))
            self.assertEqual(scanned[len(layer_path_check.LAYER):], (OWN_RULE,))

    def test_declaring_a_member_does_not_duplicate_it(self):
        with TempRepo() as repo:
            declare(repo, {"rules": [MEMBER]})
            scanned = layer_path_check.scanned_paths(repo.root)
            self.assertEqual(scanned.count(MEMBER), 1)


class GuardReadsTheDeclaration(unittest.TestCase):
    """Acceptance 12's shape: the guard blocks a dangling path in a declared rule file.

    Each case pairs with the control immediately beside it — same repository, same staged
    bytes, one thing changed.
    """

    def test_a_dangling_path_in_a_declared_rule_is_blocked(self):
        with TempRepo() as repo:
            declare(repo, {"rules": [OWN_RULE]})
            stage(repo, {OWN_RULE: BAD_LINE})
            self.assertEqual(layer_path_check.check(repo.root), 1)

    def test_the_same_file_undeclared_is_not_blocked(self):
        with TempRepo() as repo:
            stage(repo, {OWN_RULE: BAD_LINE})
            self.assertEqual(layer_path_check.check(repo.root), 0)

    def test_a_resolving_path_in_a_declared_rule_is_not_blocked(self):
        with TempRepo() as repo:
            declare(repo, {"rules": [OWN_RULE]})
            stage(repo, {MEMBER: "member\n", OWN_RULE: GOOD_LINE})
            self.assertEqual(layer_path_check.check(repo.root), 0)

    def test_a_malformed_declaration_stops_the_guard_rather_than_emptying_it(self):
        with TempRepo() as repo:
            declare(repo, "{not json")
            stage(repo, {OWN_RULE: BAD_LINE})
            with self.assertRaises(caller.HarnessConfigError):
                layer_path_check.check(repo.root)


class SweepReadsTheDeclaration(unittest.TestCase):
    def test_a_declared_rule_file_is_swept(self):
        with TempRepo() as repo:
            declare(repo, {"rules": [OWN_RULE]})
            repo.write({OWN_RULE: BAD_LINE})
            git(repo.root, "add", "-A")
            output = run_sweep(repo)
            self.assertIn("PATHTOK " + OWN_RULE, output)

    def test_the_same_file_undeclared_is_not_swept(self):
        with TempRepo() as repo:
            repo.write({OWN_RULE: BAD_LINE})
            git(repo.root, "add", "-A")
            self.assertNotIn(OWN_RULE, run_sweep(repo))


if __name__ == "__main__":
    unittest.main()
