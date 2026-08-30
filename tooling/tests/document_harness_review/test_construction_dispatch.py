#!/usr/bin/env python3
"""Acceptance matrix for the construction-side dispatch generator (`tooling/construction_dispatch.py`).

Three families moved out of `dispatch.py` in round `CORE-ONLY-CODE` (`core-only.plan.md`
item C): a round's bounded review, an E10 layer read, and that round's executor. Their tests
moved with them, so the file a reviewer opens to see what the generator promises sits beside
the generator rather than inside the product tier's own matrix. What each class asserts is
unchanged where the behaviour is unchanged; the classes are the ones `test_dispatch.py`
carried until this round, and the diff worth reading is the charter.

**The charter is the one thing that changed, and it is asserted twice.** Every prompt used to
name a constant — the retired review-side contract stub for the two review modes, this
repository's checklist for the executor mode. All three now name what the swept repository
declares under `rules` in its `harness.json` (`E10`'s second sentence; plan ruling 9), which
is why every scenario below *writes a declaration* into its disposable repository and asserts
the prompt names that file rather than any file this suite happens to sit next to. The
negative control is the repository that declares nothing: it gets a refusal, never a prompt.

Every expectation here is a hand-written literal or a committed fixture, never read back from
the module under test (`E5`); each must-fire case is paired with the clean scenario, asserted
clean first, because a refusal test proves nothing if the baseline also refuses (`E4`).
"""
from __future__ import annotations

import importlib.util
import json
import pathlib
import sys
import unittest

import _harness
from _harness import TempRepo, git  # noqa: F401  (imported for parity with the suite)
from test_review_v2_subject import build_scenario, codes

#: Loaded by explicit path: the module is a construction-side script at `tooling/`, not a
#: member of the `rsclib.document_harness` package, and binding the file directly is how this
#: suite already loads plumbing that is not importable by package name (`_harness`).
MODULE_PATH = _harness.TOOLING_DIR / "construction_dispatch.py"


def _load():
    """Bound under an unambiguous module name, and registered before it is executed.

    `sys.modules` first because the module defines frozen dataclasses, and
    `dataclasses` resolves a field's annotations through `sys.modules[cls.__module__]` —
    a module executed before it is registered raises there rather than defining its types.
    """
    spec = importlib.util.spec_from_file_location("v3_construction_dispatch", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules.setdefault("v3_construction_dispatch", module)
    spec.loader.exec_module(module)
    return module


C = _load()

FIXTURES = pathlib.Path(__file__).parents[1] / "fixtures"

#: The declaration every scenario writes, and the literal every assertion below expects
#: (`E5`): a path of the swept repository's own, not a path of this one's.
DECLARED = "rules/THIS-REPOSITORY-RULES.md"
DECLARED_TOKEN = "`rules/THIS-REPOSITORY-RULES.md`"


def declare(repo_root: pathlib.Path, *rules: str) -> None:
    """Write the repository's own `harness.json`, as `dtw init` would and a repository edits."""
    (repo_root / "harness.json").write_text(
        json.dumps({"policy": None, "rules": list(rules)}, indent=1) + "\n",
        encoding="utf-8",
    )
    for rule in rules:
        path = repo_root / rule
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("# a rule file\n", encoding="utf-8")


class ConstructionRoundsGenerateToo(unittest.TestCase):
    """The one irreducible input is the round's boundary; the prompt is a constant.

    This class used to hold eleven tests (counted at `d55d5ce`) guarding a derived churn list
    and the sliced constant that carried its caveat. The derivation is gone (see the module's
    docstring), and with it F1, V1, V2, V3 and V4 — every one of which existed only to hold
    churn up. What remains is the assertion those five were reaching for and never made: the
    emitted document equals the expected document exactly, which catches an added line, a
    missing line and a reordered line with one comparison.
    """

    def _round(self, *rules: str):
        scn = build_scenario()
        repo = scn.repo
        declare(repo.root, *(rules or (DECLARED,)))
        base = git(repo.root, "rev-parse", "HEAD").strip()
        (repo.root / "a.md").write_text("one\n", encoding="utf-8")
        git(repo.root, "add", "a.md")
        git(repo.root, "commit", "-q", "-m", "round commit")
        return repo, base, git(repo.root, "rev-parse", "HEAD").strip()

    #: The expected prompt lives in a committed fixture, not in this file. A golden file is
    #: the ordinary idiom for "the output must be exactly this", and it removes the reason the
    #: two previous guards failed: an expectation sitting next to the source it checks reads as
    #: duplication and invites being collapsed into a reference, which makes the comparison
    #: compare the module to itself. In a separate data file there is nothing to collapse.
    FIXTURE = FIXTURES / "expected-construction-prompt.txt"

    def test_the_prompt_is_exactly_the_golden_file(self):
        """Added, missing and reordered lines all fail here, in one comparison."""
        repo, base, tip = self._round()
        d = C.construction_dispatch_of(repo.root, base, tip)
        self.assertTrue(d.report.ok, codes(d.report))
        expected = self.FIXTURE.read_text(encoding="utf-8").format(
            base=base, tip=tip, rules=DECLARED_TOKEN
        )
        self.assertEqual(C.render_construction_dispatch(d), expected)

    def test_the_prompt_carries_nothing_but_the_charter_and_the_range(self):
        """Stated as absences too, so the intent survives an edit to the constant."""
        repo, base, tip = self._round()
        prompt = C.render_construction_dispatch(C.construction_dispatch_of(repo.root, base, tip))
        self.assertIn(DECLARED_TOKEN, prompt)
        self.assertIn(f"{base}..{tip}", prompt)
        self.assertNotIn("Churn", prompt)
        self.assertNotIn("commits", prompt)
        self.assertNotIn("upper bound", prompt)
        # The product-run reviewer's charter governs a different role and is never cited here.
        self.assertNotIn("document-harness/REVIEW.md", prompt)

    def test_the_charter_is_the_declaration_and_not_a_constant(self):
        """The round's own change: a second declaration is named, a hard-coded one is not.

        The stub the two review modes named until this round is asserted absent by its own
        name, hand-written here, so a constant growing back is a failure rather than a silent
        second charter.
        """
        repo, base, tip = self._round("rules/A.md", "rules/B.md")
        prompt = C.render_construction_dispatch(C.construction_dispatch_of(repo.root, base, tip))
        self.assertIn("`rules/A.md` · `rules/B.md`", prompt)
        self.assertNotIn("v3-harness-review-contract.md", prompt)
        self.assertNotIn("CONSTRUCTION-CHECKLIST.md", prompt)

    def test_a_repository_that_declares_nothing_is_refused(self):
        """Must fire: no declaration, no standing instruction, so no prompt."""
        scn = build_scenario()
        repo = scn.repo
        base = git(repo.root, "rev-parse", "HEAD").strip()
        (repo.root / "a.md").write_text("one\n", encoding="utf-8")
        git(repo.root, "add", "a.md")
        git(repo.root, "commit", "-q", "-m", "round commit")
        tip = git(repo.root, "rev-parse", "HEAD").strip()
        d = C.construction_dispatch_of(repo.root, base, tip)
        self.assertIn(f"{C.CODE}-NO-DECLARED-RULES", codes(d.report))
        doc = C.render_construction_dispatch(d)
        self.assertIn("NOT DISPATCHABLE", doc)
        self.assertNotIn("Subject:", doc)

    def test_the_same_round_with_a_declaration_is_clean(self):  # negative control
        repo, base, tip = self._round()
        d = C.construction_dispatch_of(repo.root, base, tip)
        self.assertEqual(codes(d.report), [])

    def test_a_reversed_range_does_not_bound_a_round(self):
        repo, base, tip = self._round()
        d = C.construction_dispatch_of(repo.root, tip, base)
        self.assertIn(f"{C.CODE}-RANGE-NOT-ANCESTRAL", codes(d.report))

    def test_a_range_containing_no_commit_is_refused(self):
        repo, base, tip = self._round()
        d = C.construction_dispatch_of(repo.root, tip, tip)
        self.assertIn(f"{C.CODE}-EMPTY-RANGE", codes(d.report))

    def test_an_unresolvable_endpoint_is_reported(self):
        repo, base, tip = self._round()
        d = C.construction_dispatch_of(repo.root, "no-such-ref", tip)
        self.assertIn(f"{C.CODE}-COMMIT-UNREADABLE", codes(d.report))

    def test_a_refusal_is_not_a_prompt_and_names_no_subject(self):
        repo, base, tip = self._round()
        doc = C.render_construction_dispatch(C.construction_dispatch_of(repo.root, tip, base))
        self.assertIn("NOT DISPATCHABLE", doc)
        self.assertNotIn("Subject:", doc)

    def test_both_endpoints_are_routed_in_full(self):
        repo, base, tip = self._round()
        d = C.construction_dispatch_of(repo.root, base[:7], tip[:7])
        self.assertEqual((len(d.base), len(d.tip)), (40, 40))
        self.assertIn(f"{base}..{tip}", C.render_construction_dispatch(d))


class ReadDispatchesGenerateToo(unittest.TestCase):
    """One commit, a constant prompt, no member list.

    The member set stays with E10's sentence on purpose — the hand-written read dispatch
    this mode replaces enumerated the members and got the set wrong
    (`v3-cold-read-451e8b0.md` M-1), which is the anchoring failure the layer exists to
    remove.
    """

    FIXTURE = FIXTURES / "expected-read-prompt.txt"

    def test_the_prompt_is_exactly_the_golden_file(self):
        scn = build_scenario()
        declare(scn.repo.root, DECLARED)
        d = C.read_dispatch_of(scn.repo.root, "HEAD")
        self.assertTrue(d.report.ok, codes(d.report))
        expected = self.FIXTURE.read_text(encoding="utf-8").format(
            commit=d.commit, rules=DECLARED_TOKEN
        )
        self.assertEqual(C.render_read_dispatch(d), expected)

    def test_the_subject_is_routed_in_full(self):
        scn = build_scenario()
        declare(scn.repo.root, DECLARED)
        d = C.read_dispatch_of(scn.repo.root, scn.evidence_commit[:7])
        self.assertTrue(d.report.ok, codes(d.report))
        self.assertEqual(len(d.commit), 40)

    def test_no_member_enumeration_reaches_the_reader(self):
        scn = build_scenario()
        declare(scn.repo.root, DECLARED)
        prompt = C.render_read_dispatch(C.read_dispatch_of(scn.repo.root, "HEAD"))
        self.assertIn("E10's own", prompt)
        self.assertNotIn("supersession", prompt)
        self.assertNotIn("paragraph-map.schema.json", prompt)

    def test_the_declared_charter_is_what_reaches_the_reader(self):
        scn = build_scenario()
        declare(scn.repo.root, DECLARED)
        d = C.read_dispatch_of(scn.repo.root, "HEAD")
        self.assertEqual(d.rules, (DECLARED,))
        self.assertIn(DECLARED_TOKEN, C.render_read_dispatch(d))

    def test_a_repository_that_declares_nothing_is_refused(self):
        scn = build_scenario()
        d = C.read_dispatch_of(scn.repo.root, "HEAD")
        self.assertIn(f"{C.CODE}-NO-DECLARED-RULES", codes(d.report))
        self.assertIn("NOT DISPATCHABLE", C.render_read_dispatch(d))

    def test_an_unresolvable_revision_refuses_and_names_no_subject(self):
        scn = build_scenario()
        declare(scn.repo.root, DECLARED)
        d = C.read_dispatch_of(scn.repo.root, "no-such-ref")
        self.assertIn(f"{C.CODE}-COMMIT-UNREADABLE", codes(d.report))
        doc = C.render_read_dispatch(d)
        self.assertIn("NOT DISPATCHABLE", doc)
        self.assertNotIn("Subject:", doc)


class ConstructionExecutorDispatchGeneratesToo(unittest.TestCase):
    """The executor mode: one sentence, the charter, nothing derived.

    A construction round has no control plane, and hand-fed round facts would reproduce
    the anchoring this layer exists to abolish — so the mode's whole honesty is that it
    emits the charter pointer and refuses to know anything else.
    """

    FIXTURE = FIXTURES / "expected-construction-executor-prompt.txt"

    def test_the_prompt_is_exactly_the_golden_file(self):
        scn = build_scenario()
        declare(scn.repo.root, DECLARED)
        d = C.construction_executor_dispatch_of(scn.repo.root)
        self.assertTrue(d.report.ok, codes(d.report))
        expected = self.FIXTURE.read_text(encoding="utf-8").format(rules=DECLARED_TOKEN)
        self.assertEqual(C.render_construction_executor_dispatch(d), expected)

    def test_nothing_is_derived_beyond_the_charter(self):
        scn = build_scenario()
        declare(scn.repo.root, DECLARED)
        d = C.construction_executor_dispatch_of(scn.repo.root)
        prompt = C.render_construction_executor_dispatch(d)
        self.assertIn(DECLARED_TOKEN, prompt)
        self.assertNotIn("Subject:", prompt)
        self.assertNotIn("Everything else you derive", prompt)
        self.assertIn(
            "nothing else is derived", C.render_construction_executor_derivation(d)
        )

    def test_the_charter_is_not_the_review_sides(self):
        scn = build_scenario()
        declare(scn.repo.root, DECLARED)
        prompt = C.render_construction_executor_dispatch(
            C.construction_executor_dispatch_of(scn.repo.root)
        )
        self.assertNotIn("v3-harness-review-contract.md", prompt)
        self.assertNotIn("REVIEW.md", prompt)

    def test_a_repository_that_declares_nothing_is_refused(self):
        scn = build_scenario()
        d = C.construction_executor_dispatch_of(scn.repo.root)
        self.assertIn(f"{C.CODE}-NO-DECLARED-RULES", codes(d.report))
        self.assertIn("NOT DISPATCHABLE", C.render_construction_executor_dispatch(d))

    def test_the_same_repository_with_a_declaration_is_clean(self):  # negative control
        scn = build_scenario()
        declare(scn.repo.root, DECLARED)
        d = C.construction_executor_dispatch_of(scn.repo.root)
        self.assertEqual(codes(d.report), [])


class NoCharterIsNamedFromThisRepositorysOwnLayout(unittest.TestCase):
    """The defect class item C closes, asserted directly (`E7`).

    A generator that reads its own repository's declaration rather than the swept one's would
    pass every test above on this machine and hand a second repository a charter it does not
    have. So: sweep a repository that declares one thing while this one declares another, and
    assert the prompt carries the swept repository's answer and not this repository's.
    """

    #: Hand-written (`E5`): what THIS repository declares, which no prompt below may name.
    THIS_REPOSITORY_DECLARES = "document-harness/CONSTRUCTION-CHECKLIST.md"

    def test_the_swept_repositorys_declaration_is_the_one_named(self):
        with TempRepo({"a.md": "one\n"}) as repo:
            declare(repo.root, DECLARED)
            d = C.construction_executor_dispatch_of(repo.root)
            prompt = C.render_construction_executor_dispatch(d)
            self.assertIn(DECLARED_TOKEN, prompt)
            self.assertNotIn(self.THIS_REPOSITORY_DECLARES, prompt)

    def test_this_repository_does_declare_that_file(self):  # premise, checked not remembered
        declared = json.loads(
            (_harness.RS_ROOT / "harness.json").read_text(encoding="utf-8")
        )["rules"]
        self.assertIn(
            self.THIS_REPOSITORY_DECLARES,
            declared,
            "this repository stopped declaring that file; the guard above needs a new one",
        )


class NamedIssueReachability(unittest.TestCase):
    """Every code the construction dispatch can raise is asserted by name in this file."""

    def test_no_code_is_silent_surface(self):
        import re

        module_text = MODULE_PATH.read_text(encoding="utf-8")
        declared = set(re.findall(r'f"\{CODE\}-([A-Z-]+)"', module_text))
        test_text = pathlib.Path(__file__).read_text(encoding="utf-8")
        asserted = set(re.findall(r"\{C\.CODE\}-([A-Z-]+)", test_text))
        self.assertEqual(
            declared - asserted,
            set(),
            "codes declared in construction_dispatch.py with no test asserting them by name",
        )
        self.assertEqual(len(declared), 3, f"code surface moved: {sorted(declared)}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
