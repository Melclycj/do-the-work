#!/usr/bin/env python3
"""B-1 — the comparator's per-run constants are arguments, and none of them is defaulted.

`v3-review-full-eec4171.md` §3 `B-1`: R2 converted three of the four CONFIG-carrying scripts
and the round's texts asserted the conversion of all four, while
`templates/run-v2/compare_blocks.py` still shipped `SOURCE` / `OWNERS` / `SITES` /
`PROSE_APPENDS` / `GENERATED` / `REBUILD_ARGV` as a "fill per run" block of placeholders. The
consequence the review measured is why the defaults matter more than the block: `--blocks`
and `--rebuild` crash on the placeholders, but `--prose` with `OWNERS=[]` and
`PROSE_APPENDS={}` **passes** on any all-additions diff — a green `command_exit` CheckResult
over a comparator that compared nothing.

So the property under test is the argument SURFACE, not the comparison algebra (which the
p4-doc lineage and its run already exercise): the mode flags keep the spellings a frozen
check spec's `argv` carries, each mode's declarations arrive from that `argv`, and a
declaration the run did not make is refused rather than assumed.

Every expectation below is a hand-written literal and is never imported from the template
(E5). Assertions are made against WHOLE structures and whole printed lines.

The template is loaded by explicit file path under a distinct module name — importing it
runs only its module level (its ``main`` is guarded by ``__name__``). ``REPO =
pathlib.Path.cwd()`` is read at import and stays a `cwd` derivation by design — every mode
runs inside the materialized candidate tree — so the fixtures below become that tree by
loading the module from inside one, never by re-pointing the module's global afterwards.
"""
from __future__ import annotations

import contextlib
import importlib.util
import io
import os
import pathlib
import shutil
import sys
import tempfile
import unittest

import _harness  # noqa: F401 — installs the tooling import path the suite runs under

TEMPLATE_PATH: pathlib.Path = (
    _harness.RS_ROOT / "assurance" / "templates" / "run-v2" / "compare_blocks.py"
)


def load_template():
    """Bind the template file directly; never by adding its directory to sys.path."""
    if not TEMPLATE_PATH.is_file():
        raise RuntimeError(f"the v2 comparator template is missing at {TEMPLATE_PATH}")
    spec = importlib.util.spec_from_file_location("v2_comparator_template", TEMPLATE_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules["v2_comparator_template"] = module
    spec.loader.exec_module(module)
    return module


def load_template_in(directory: pathlib.Path):
    """Load it with `directory` as the working directory — i.e. as the materialized tree."""
    previous = os.getcwd()
    os.chdir(directory)
    try:
        return load_template()
    finally:
        os.chdir(previous)


def run_main(template, argv):
    """Run main(argv) capturing stdout; `fail()` exits, anything else returns None.

    C0 F2: a refusal that has been removed lets `main` run on into work that needs a real
    tree and raise there, and letting that escape would turn every assertion below into an
    ERROR — which proves the code was reached, not that it binds anything (R8). Mapped to a
    value, "not refused" fails as `None != 1`.
    """
    buffer = io.StringIO()
    try:
        with contextlib.redirect_stdout(buffer):
            code = template.main(argv)
    except SystemExit as stop:
        return stop.code, buffer.getvalue()
    except Exception:
        return None, buffer.getvalue()
    return code, buffer.getvalue()


#: The one fence both fixture documents carry. Written as lines so the file that declares it
#: is not itself a Markdown document with an unterminated fence.
FENCE = ["```research-object", "object_id: obj-one", "kind: claim", "```"]
SOURCE_MD = "\n".join(["# Pinned source", "", *FENCE, ""])
OWNER_MD = "\n".join(
    ["# Owner", "", "## Section start", "", *FENCE, "", "## Section end", ""])
#: Same id, different body — the difference the `--blocks` mode exists to find.
OWNER_MD_ALTERED = OWNER_MD.replace("kind: claim", "kind: claim-rewritten")
#: Same body, sited after the section it is declared to live in.
OWNER_MD_MISPLACED = "\n".join(
    ["# Owner", "", "## Section start", "", "## Section end", "", *FENCE, ""])

SITE_ONE = "obj-one=owner.md::## Section start::## Section end"


class TheModeFlagsKeepTheSpellingsTheCheckSpecsFroze(unittest.TestCase):
    """A frozen check spec's `argv` carries the mode; R2 may add after it, never rename it.

    Measured against the four committed p4-doc specs, which are the only check specs in the
    repository that invoke a comparator: `chk-compare-blocks` passes `--blocks`,
    `chk-compare-subsections` passes `--subsections`, `chk-prose-preserved` passes
    `--prose --base <sha>`, and `chk-index-five` passes `--index` — a run-local mode of the
    pre-template p4-doc instance that this template does not carry. `--rebuild` is the
    template's own fourth mode, which no committed spec invokes yet; it is pinned here beside
    the three that are frozen so a rename is caught before the first spec depends on it.
    """

    def setUp(self):
        self.template = load_template()

    def test_each_frozen_mode_token_still_names_its_own_mode(self):
        parser = self.template.build_parser()
        self.assertEqual(
            {token: parser.parse_args([token]).mode
             for token in ["--blocks", "--subsections", "--prose", "--rebuild"]},
            {"--blocks": "blocks", "--subsections": "subsections",
             "--prose": "prose", "--rebuild": "rebuild"},
        )

    def test_prose_still_takes_the_base_sha_as_its_own_option(self):
        """`--prose --base <sha>` is the exact pair the p4-doc spec freezes."""
        args = self.template.build_parser().parse_args(
            ["--prose", "--base", "993911dc6b267fe29d61aa00ef2bfeaf7a272056"])
        self.assertEqual(
            (args.mode, args.base),
            ("prose", "993911dc6b267fe29d61aa00ef2bfeaf7a272056"),
        )

    def test_a_command_line_naming_no_mode_is_refused(self):
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as stop:
                self.template.build_parser().parse_args([])
        self.assertEqual(stop.exception.code, 2)

    def test_two_modes_at_once_are_refused(self):
        """One invocation decides one question; two modes would silently run only one."""
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as stop:
                self.template.build_parser().parse_args(["--blocks", "--prose"])
        self.assertEqual(stop.exception.code, 2)


class NoPerRunConstantIsDefaulted(unittest.TestCase):
    """B-1's measured consequence: a comparator that defaults compares nothing and says PASS.

    Each refusal below is the placeholder the deleted CONFIG block shipped — an empty
    `SITES`, an empty `OWNERS`, a `<repo-relative path …>` `SOURCE` — expressed as the
    absence of the option that now carries it.
    """

    def setUp(self):
        self.template = load_template()

    def test_blocks_without_a_source_is_refused(self):
        code, out = run_main(self.template, ["--blocks", "--owner", "owner.md", "--site", SITE_ONE])
        self.assertEqual(code, 1, out)
        self.assertEqual(
            out.splitlines(),
            ["FAIL: --blocks needs --source; this run declared none, and nothing here is "
             "defaulted"],
        )

    def test_blocks_without_a_single_site_is_refused(self):
        """The shipped `SITES = {}`: expected-id set empty, every comparison vacuous."""
        code, out = run_main(
            self.template, ["--blocks", "--source", "source.md", "--owner", "owner.md"])
        self.assertEqual(code, 1, out)
        self.assertEqual(
            out.splitlines(),
            ["FAIL: --blocks needs --site; this run declared none, and nothing here is "
             "defaulted"],
        )

    def test_blocks_without_an_owner_is_refused(self):
        code, out = run_main(
            self.template, ["--blocks", "--source", "source.md", "--site", SITE_ONE])
        self.assertEqual(code, 1, out)
        self.assertEqual(
            out.splitlines(),
            ["FAIL: --blocks needs --owner; this run declared none, and nothing here is "
             "defaulted"],
        )

    def test_prose_without_an_owner_is_refused(self):
        """The exact vacuous PASS `B-1` measured: no owners, no appends, any diff is clean."""
        code, out = run_main(self.template, ["--prose", "--base", "a" * 40])
        self.assertEqual(code, 1, out)
        self.assertEqual(
            out.splitlines(),
            ["FAIL: --prose needs --owner; this run declared none, and nothing here is "
             "defaulted"],
        )

    def test_prose_without_a_base_is_refused(self):
        code, out = run_main(self.template, ["--prose", "--owner", "owner.md"])
        self.assertEqual(code, 1, out)
        self.assertEqual(
            out.splitlines(),
            ["FAIL: --prose needs --base; this run declared none, and nothing here is "
             "defaulted"],
        )

    def test_rebuild_without_a_generated_file_is_refused(self):
        code, out = run_main(
            self.template, ["--rebuild", "--rebuild-argv", "python", "-X", "utf8", "gen.py"])
        self.assertEqual(code, 1, out)
        self.assertEqual(
            out.splitlines(),
            ["FAIL: --rebuild needs --generated; this run declared none, and nothing here is "
             "defaulted"],
        )

    def test_rebuild_without_a_command_is_refused(self):
        """Deleting the generated files and then rebuilding nothing is the worst of the four."""
        code, out = run_main(self.template, ["--rebuild", "--generated", "out/index.json"])
        self.assertEqual(code, 1, out)
        self.assertEqual(
            out.splitlines(),
            ["FAIL: --rebuild needs --rebuild-argv; this run declared none, and nothing here "
             "is defaulted"],
        )

    def test_subsections_declares_nothing_and_says_so_in_its_own_words(self):
        """The one mode with no declarations: it refuses by design until a run adapts it."""
        code, out = run_main(self.template, ["--subsections"])
        self.assertEqual(code, 1, out)
        self.assertEqual(
            out.splitlines(),
            ["FAIL: this run declared no subsection transform — adapt this mode from the "
             "p4-doc lineage or remove the check that binds it"],
        )


class TheDeclarationsParseIntoWhatTheModesRead(unittest.TestCase):
    """The CONFIG block's two structured constants, now written on a command line."""

    def setUp(self):
        self.template = load_template()

    def test_two_sites_parse_into_owner_and_the_two_section_anchors(self):
        self.assertEqual(
            dict(self.template.parse_site(raw) for raw in [
                SITE_ONE,
                "obj-two=other.md::## Second start::Accepted answer (refined 2026-07-03):",
            ]),
            {
                "obj-one": ("owner.md", "## Section start", "## Section end"),
                "obj-two": ("other.md", "## Second start",
                            "Accepted answer (refined 2026-07-03):"),
            },
        )

    def test_a_site_missing_an_anchor_is_refused_not_padded(self):
        code, out = run_main(
            self.template,
            ["--blocks", "--source", "source.md", "--owner", "owner.md",
             "--site", "obj-one=owner.md::## Section start"],
        )
        self.assertEqual(code, 1, out)
        self.assertEqual(
            out.splitlines(),
            ["FAIL: --site obj-one: expected <owner>::<section-start>::<section-end>, found "
             "2 '::'-separated field(s) in 'owner.md::## Section start'"],
        )

    def test_a_site_naming_no_object_id_is_refused(self):
        code, out = run_main(
            self.template,
            ["--blocks", "--source", "source.md", "--owner", "owner.md",
             "--site", "owner.md::## Section start::## Section end"],
        )
        self.assertEqual(code, 1, out)
        self.assertEqual(
            out.splitlines(),
            ["FAIL: --site must be <object-id>=<owner>::<section-start>::<section-end>, got "
             "'owner.md::## Section start::## Section end'"],
        )

    def test_prose_appends_parse_into_the_line_prefix_and_its_suffix(self):
        self.assertEqual(
            dict(self.template.parse_prose_append(raw) for raw in [
                "Current agent identity models fail::^gap3-proposition",
                "- The per-arm FARs have **different denominators**::^far-contrast-basis",
            ]),
            {
                "Current agent identity models fail": "^gap3-proposition",
                "- The per-arm FARs have **different denominators**": "^far-contrast-basis",
            },
        )

    def test_a_prose_append_with_no_suffix_is_refused(self):
        code, out = run_main(
            self.template,
            ["--prose", "--base", "a" * 40, "--owner", "owner.md",
             "--prose-append", "Current agent identity models fail"],
        )
        self.assertEqual(code, 1, out)
        self.assertEqual(
            out.splitlines(),
            ["FAIL: --prose-append must be <line-prefix>::<suffix>, got 'Current agent "
             "identity models fail'"],
        )

    def test_the_rebuild_command_keeps_its_own_option_shaped_tokens(self):
        """`-X utf8` is the generator's argument, not this parser's, and must survive as one."""
        args = self.template.build_parser().parse_args(
            ["--rebuild", "--generated", "out/index.json",
             "--rebuild-argv", "python", "-X", "utf8", "rsc.py", "compile"])
        self.assertEqual(
            (args.generated, args.rebuild_argv),
            (["out/index.json"], ["python", "-X", "utf8", "rsc.py", "compile"]),
        )


class TheComparisonRunsOnWhatTheArgvNamed(unittest.TestCase):
    """End to end on a two-file synthetic tree: the constants reach the comparison from argv.

    Small on purpose — the comparison algebra is the p4-doc lineage's and is exercised by
    that run; what is new in R2 is where its inputs come from.
    """

    def make_tree(self, owner_text: str) -> pathlib.Path:
        tree = pathlib.Path(tempfile.mkdtemp(prefix="b1-comparator-"))
        self.addCleanup(shutil.rmtree, tree, ignore_errors=True)
        (tree / "source.md").write_text(SOURCE_MD, encoding="utf-8")
        (tree / "owner.md").write_text(owner_text, encoding="utf-8")
        return tree

    def drive(self, owner_text: str):
        tree = self.make_tree(owner_text)
        template = load_template_in(tree)
        return run_main(template, [
            "--blocks", "--source", "source.md", "--owner", "owner.md", "--site", SITE_ONE])

    def test_a_rendered_block_matching_its_source_inside_its_section_passes(self):
        code, out = self.drive(OWNER_MD)
        self.assertEqual(code, 0, out)
        self.assertEqual(
            out.splitlines(),
            ["PASS: 1 rendered blocks byte-identical to the pinned source, each inside its "
             "declared section"],
        )

    def test_a_rewritten_body_fails_against_the_source_the_argv_named(self):
        code, out = self.drive(OWNER_MD_ALTERED)
        self.assertEqual(code, 1, out)
        self.assertEqual(
            out.splitlines()[0],
            "FAIL: obj-one body differs from the pinned source:",
        )

    def test_a_block_outside_the_section_the_site_declared_fails(self):
        code, out = self.drive(OWNER_MD_MISPLACED)
        self.assertEqual(code, 1, out)
        self.assertEqual(
            out.splitlines(),
            ["FAIL: obj-one fence at owner.md:7 is outside its declared section"],
        )


if __name__ == "__main__":
    raise SystemExit(unittest.main(argv=[sys.argv[0]]))
