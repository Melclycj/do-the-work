#!/usr/bin/env python3
"""The harness's own command line: what it offers, and that both its names reach it.

Written by the split batch's R2, the round that moved the then-six operations out of the
product compiler `rsc.py` and gave the instrument an entry of its own. Two properties are
worth binding and nothing more:

* **the surface** — exactly seven operations, each wired to its own function. The expectation
  is a hand-written literal (`E5`); reading it back off `build_parser()` would assert that
  the parser equals itself, and a command silently disappearing in a later move is precisely
  what this must catch.
* **the two names** — `do-the-work.py` and `dtw.py` are one entry under two names (`HD-40`
  §10). Two assertions, and they bind different things: `main is cli.main` binds the
  identity — a fork that copies `main()` verbatim fails it — while comparing the two
  `--help` streams binds only that the two entries currently *agree*, which a verbatim fork
  passes. The FULL of `297bb2b` established that by mutation (`L-1`): the comparison alone
  called a fork a shim, and the weaker fork it did catch was caught incidentally, on an em
  dash and a cp1252 console. The comparison stays because it is the end-to-end evidence
  that both names actually run; the identity assertion is what closes the drift.

Reachability of each operation's *behaviour* is not asserted here: `test_dispatch.py`,
`test_dispatch_freeze_marker.py` and `test_review_cli_v2_subject.py` drive the real commands
through this entry against disposable repositories, which is proof this file cannot give.
"""
from __future__ import annotations

import importlib.util
import subprocess
import sys
import unittest

import _harness

from rsclib.document_harness import cli

#: Hand-written, never `cli`'s own list (E5). Ordered as `build_parser` declares them.
#: Six until 2026-08-19, when the user's ruling admitted `init` as a seventh.
OPERATIONS = (
    "governance-scan",
    "status",
    "flow",
    "dispatch",
    "disposition",
    "review",
    "init",
)

ENTRIES = ("do-the-work.py", "dtw.py")


def run_entry(script: str, *argv: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, script, *argv],
        cwd=str(_harness.TOOLING_DIR),
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )


def load_entry(script: str):
    """Import a shim by path — `do-the-work.py` is not an importable module name."""
    spec = importlib.util.spec_from_file_location(
        script.replace("-", "_").removesuffix(".py"), _harness.TOOLING_DIR / script
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TheSurface(unittest.TestCase):
    def test_the_operations_are_the_ones_named(self):
        sub = cli.build_parser()._subparsers._group_actions[0]
        self.assertEqual(tuple(sub.choices), OPERATIONS)

    def test_every_operation_binds_a_distinct_function(self):
        sub = cli.build_parser()._subparsers._group_actions[0]
        bound = {}
        for name in OPERATIONS:
            func = sub.choices[name].get_default("func")
            self.assertIsNotNone(func, f"{name} parses but runs nothing")
            self.assertIs(func, getattr(cli, func.__name__), f"{name} is bound outside cli.py")
            bound[name] = func
        self.assertEqual(len(set(bound.values())), len(OPERATIONS))

    def test_an_unknown_operation_is_refused(self):  # must fire — the parser is closed
        completed = run_entry("dtw.py", "compile")
        self.assertEqual(completed.returncode, 2)
        self.assertIn("invalid choice", completed.stderr)


class TheTwoNames(unittest.TestCase):
    """One entry, two names: same `main`, and both actually run."""

    def test_each_name_is_the_same_entry(self):  # must fire — a fork fails identity
        for script in ENTRIES:
            with self.subTest(script=script):
                self.assertIs(load_entry(script).main, cli.main)

    def test_both_names_run(self):  # negative control for the comparison below
        for script in ENTRIES:
            with self.subTest(script=script):
                self.assertEqual(run_entry(script, "--help").returncode, 0)

    def test_both_names_print_the_same_help(self):
        """Agreement, not identity — the identity is the assertion above (`L-1`)."""
        first, second = (run_entry(script, "--help").stdout for script in ENTRIES)
        self.assertEqual(first, second)
        for name in OPERATIONS:
            self.assertIn(name, first)


if __name__ == "__main__":
    unittest.main(verbosity=2)
