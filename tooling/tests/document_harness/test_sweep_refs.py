#!/usr/bin/env python3
"""Tests for `tooling/sweep_refs.py` — the reference sweep round DE-PREFIX brought into the
repository with no test (FULL `v3-review-full-39a21a8.md` `O-4`: a diagnostic whose output is
banked as a round's evidence has the untested-instrument shape; round INIT-SURFACE settles
that account).

The sweep is not a guard — it always exits 0 and decides nothing — so what these tests pin
is not a verdict but the enumeration itself: each reference form is reported when broken and
kept silent when whole, the resolution rule honours the member's own directory and refuses
root escape, and the exit code stays 0 with and without hits (a sweep that started failing
would become a guard nobody chartered). Every must-report case is paired with a clean
baseline asserted in the same test (E4's negative-control shape, applied to a reporter).

The member list is patched per test: the real `LAYER` tuple would tie every assertion to the
live instruction layer's current contents, which is the staleness this module itself avoids
by importing the list instead of copying it.
"""
from __future__ import annotations

import contextlib
import io
import unittest
from unittest import mock

from _harness import TempRepo, git

import sweep_refs


def run_sweep(repo: TempRepo) -> tuple[int, str]:
    """Run the sweep over the repo, returning (exit code, captured stdout)."""
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        code = sweep_refs.sweep(repo.root)
    return code, buffer.getvalue()


def tracked(repo: TempRepo, files: dict[str, str]) -> None:
    repo.write(files)
    git(repo.root, "add", "--", *files.keys())
    git(repo.root, "commit", "-qm", "tracked fixture")


class Resolution(unittest.TestCase):
    """`resolves()` — root-relative, member-relative, runtime marker, and root escape."""

    def test_root_relative_and_member_relative_resolve(self):
        with TempRepo() as repo:
            tracked(repo, {"docs/member.md": "x\n", "docs/near.md": "x\n", "top.md": "x\n"})
            self.assertTrue(sweep_refs.resolves(repo.root, "docs/member.md", "top.md"))
            self.assertTrue(sweep_refs.resolves(repo.root, "docs/member.md", "near.md"))

    def test_a_missing_target_does_not_resolve(self):
        with TempRepo() as repo:
            tracked(repo, {"docs/member.md": "x\n"})
            self.assertFalse(sweep_refs.resolves(repo.root, "docs/member.md", "no-such.md"))

    def test_a_runtime_marker_resolves_without_existing(self):
        # Hand-written literal, not the module's constant (E5).
        with TempRepo() as repo:
            tracked(repo, {"docs/member.md": "x\n"})
            self.assertTrue(
                sweep_refs.resolves(repo.root, "docs/member.md", ".harness/review-pending.json")
            )

    def test_escaping_the_repository_root_counts_as_nowhere(self):
        with TempRepo() as repo:
            tracked(repo, {"docs/member.md": "x\n"})
            # The sibling file genuinely exists outside the repo root; escape must not count.
            outside = repo.root.parent / f"{repo.root.name}-outside.md"
            outside.write_text("x\n", encoding="utf-8")
            try:
                self.assertTrue(outside.exists())  # the escape target is real ...
                self.assertFalse(  # ... and still refused
                    sweep_refs.resolves(
                        repo.root, "docs/member.md", f"../../{outside.parent.name}/{outside.name}"
                    )
                )
            finally:
                outside.unlink(missing_ok=True)


class TrackedBasenames(unittest.TestCase):
    def test_only_tracked_files_contribute_basenames(self):
        with TempRepo() as repo:
            tracked(repo, {"docs/known.md": "x\n"})
            repo.write({"docs/untracked.md": "x\n"})  # written, never added
            names = sweep_refs.tracked_basenames(repo.root)
            self.assertIn("known.md", names)
            self.assertNotIn("untracked.md", names)


class Sweep(unittest.TestCase):
    """End-to-end over a patched one-member layer: each form reported broken, silent whole."""

    def test_each_reference_form_is_reported_exactly_when_broken(self):
        with TempRepo() as repo:
            tracked(
                repo,
                {
                    "docs/member.md": (
                        "[good](target.md) and [bad](gone.md)\n"
                        "see `docs/real.py` and `docs/ghost.py`\n"
                        "named `target.md` and `phantom.md`\n"
                    ),
                    "docs/target.md": "x\n",
                    "docs/real.py": "x\n",
                },
            )
            with mock.patch.object(sweep_refs, "LAYER", ("docs/member.md",)):
                code, out = run_sweep(repo)
        self.assertEqual(code, 0)
        # must-report, one per form:
        self.assertIn("LINK    docs/member.md:1  gone.md", out)
        self.assertIn("PATHTOK docs/member.md:2  docs/ghost.py", out)
        self.assertIn("NAMETOK docs/member.md:3  phantom.md", out)
        # negative controls — the whole siblings on the same lines stay silent:
        self.assertNotIn("target.md", out.replace("phantom.md", ""))
        self.assertNotIn("docs/real.py", out)
        self.assertIn("-- 3 caller-held or unresolvable references over 1 members", out)

    def test_a_placeholder_token_is_invisible_by_design(self):
        # The documented shared blindness (docstring; `v3-cold-read-4410899.md` L-2): a
        # `<...>` segment matches no pattern, so the sweep must stay silent — a test that
        # expected a report here would be pinning behaviour the module disclaims.
        with TempRepo() as repo:
            tracked(repo, {"docs/member.md": "at `migration/<round>/record.md`\n"})
            with mock.patch.object(sweep_refs, "LAYER", ("docs/member.md",)):
                code, out = run_sweep(repo)
        self.assertEqual(code, 0)
        self.assertIn("-- 0 caller-held or unresolvable references over 1 members", out)

    def test_a_missing_member_is_reported_and_exit_stays_zero(self):
        with TempRepo() as repo:
            with mock.patch.object(sweep_refs, "LAYER", ("docs/absent.md",)):
                code, out = run_sweep(repo)
        self.assertEqual(code, 0)  # a sweep, not a guard: hits never move the exit code
        self.assertIn("MISSING docs/absent.md", out)
        self.assertIn("-- 1 caller-held or unresolvable references over 1 members", out)

    def test_a_clean_layer_reports_zero_and_exits_zero(self):
        with TempRepo() as repo:
            tracked(repo, {"docs/member.md": "[good](target.md) and `docs/member.md`\n",
                           "docs/target.md": "x\n"})
            with mock.patch.object(sweep_refs, "LAYER", ("docs/member.md",)):
                code, out = run_sweep(repo)
        self.assertEqual(code, 0)
        self.assertIn("-- 0 caller-held or unresolvable references over 1 members", out)


if __name__ == "__main__":
    unittest.main()
