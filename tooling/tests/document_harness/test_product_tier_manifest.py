#!/usr/bin/env python3
"""`document-harness/product-tier.txt` — the product-run tier as a list a caller can run.

Round `CORE-MOUNT`. The tier a repository mounts has always been defined by
`CONSTRUCTION-INDEX.md`'s product-run table, which is construction-side and does not travel,
so a caller narrowing its checkout to that tier had to read this repository to learn what the
tier is. The manifest is that table's *Where* column, one repo-relative path per line and
self-including, in a file that does travel: `git sparse-checkout set --no-cone --stdin` reads
it directly (`document-harness/ONBOARDING.md` item 1b).

Two copies of one list is the shape `E10-sync` records, so the two are held equal here rather
than by discipline. The expectation is parsed from `CONSTRUCTION-INDEX.md` — a different file
from the one guarded (`E5`) — and drift in either direction is what turns this red; neither
copy is derived from the other at runtime, which is why the guard has anything to say.

The end-to-end case is the one that decides whether the step works at all: a `--no-checkout`
clone of this repository, the manifest fed to `sparse-checkout`, a checkout, and then the two
consumers compared against each other on the result — what is on disk against what
`git ls-files` matches from the same lines. The four construction-side files it asserts absent
are a hand-written literal (`E5`), and each is asserted *present in the clone's index* in the
same breath, so "absent" cannot be satisfied by a path that stopped existing.

Read from the worktree, not from `HEAD`: the manifest under test is the file as it stands, so
an edit to it is visible to these assertions without a commit — which is what makes them
mutation-testable (`E4`).
"""
from __future__ import annotations

import pathlib
import re
import shutil
import subprocess
import tempfile
import unittest

REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]

#: Hand-written, not derived from the manifest — this is the path the manifest must list
#: (`E5`), and computing it from the file under test would make the claim vacuous.
MANIFEST_PATH = "document-harness/product-tier.txt"

#: Hand-written (`E5`): four files the construction-side tier owns, one per kind — the round
#: pointer, the decision log, this repository's own declared rule file, and the construction
#: dispatch. A narrowed checkout carries none of them.
CONSTRUCTION_SIDE_FILES = (
    "CONSTRUCTION-LEDGER.md",
    "HARNESS-DECISIONS.md",
    "document-harness/CONSTRUCTION-CHECKLIST.md",
    "tooling/construction_dispatch.py",
)

#: The heading the product-run table sits under, and the token form its *Where* cells use.
PRODUCT_TIER_HEADING = "## Product-run tier"
CODE_SPAN = re.compile(r"`([^`]+)`")


def git(root: pathlib.Path, *args: str, stdin: str | None = None) -> str:
    completed = subprocess.run(
        ["git", "-C", str(root), *args],
        check=False,
        input=stdin,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        errors="replace",
    )
    if completed.returncode:
        raise RuntimeError(
            f"git {' '.join(args)} failed ({completed.returncode}): "
            f"{completed.stderr or completed.stdout}"
        )
    return completed.stdout


def manifest_lines() -> list[str]:
    """The manifest's paths, CR stripped — a checkout with `core.autocrlf=true` has them."""
    text = (REPO_ROOT / MANIFEST_PATH).read_text(encoding="utf-8")
    return [line.strip() for line in text.splitlines() if line.strip()]


def where_tokens_from_index() -> list[str]:
    """The *Where* column of `CONSTRUCTION-INDEX.md`'s product-run tier table, in row order.

    Scoped to that one section: the construction-side table below it uses markdown links
    rather than path tokens, and the rows above the table are prose.
    """
    text = (REPO_ROOT / "CONSTRUCTION-INDEX.md").read_text(encoding="utf-8")
    start = text.index(PRODUCT_TIER_HEADING)
    end = text.index("\n## ", start + len(PRODUCT_TIER_HEADING))
    tokens: list[str] = []
    for line in text[start:end].splitlines():
        if not line.startswith("|"):
            continue
        cells = line.split("|")
        if len(cells) != 6 or not cells[1].strip().isdigit():
            continue
        tokens.extend(CODE_SPAN.findall(cells[3]))
    return tokens


class TheManifestNamesFilesThatExist(unittest.TestCase):
    """(a) Every line matches at least one tracked file."""

    def test_every_manifest_line_matches_a_tracked_file(self) -> None:
        lines = manifest_lines()
        self.assertTrue(lines, "the manifest is empty — every assertion below would be vacuous")
        unmatched = [
            line for line in lines if not git(REPO_ROOT, "ls-files", "--", line).strip()
        ]
        self.assertEqual(
            unmatched,
            [],
            f"{MANIFEST_PATH} lines matching no tracked file: {unmatched}",
        )


class TheManifestAndTheIndexTableAreOneList(unittest.TestCase):
    """(b) The two copies of the tier definition agree, in both directions."""

    def test_the_manifest_equals_the_index_tables_where_column(self) -> None:
        tokens = where_tokens_from_index()
        self.assertTrue(
            tokens,
            "no *Where* tokens parsed out of CONSTRUCTION-INDEX.md's product-run table — "
            "the parse, not the tier, is what broke",
        )
        self.assertEqual(
            sorted(set(manifest_lines())),
            sorted(set(tokens)),
            f"{MANIFEST_PATH} and CONSTRUCTION-INDEX.md's product-run table disagree about "
            "what travels; the table is the definition and the manifest is what a caller runs",
        )

    def test_the_index_table_names_each_path_once(self) -> None:
        tokens = where_tokens_from_index()
        duplicates = sorted({token for token in tokens if tokens.count(token) > 1})
        self.assertEqual(duplicates, [], f"repeated *Where* tokens: {duplicates}")


class TheManifestCarriesItself(unittest.TestCase):
    """(c) A narrowed mount carries the list it was narrowed by, so it can be redone."""

    def test_the_manifest_lists_its_own_path(self) -> None:
        self.assertIn(
            MANIFEST_PATH,
            manifest_lines(),
            "the manifest does not list itself, so a sparse checkout made from it would not "
            "carry it and the step could not be repeated after a gitlink bump",
        )


class ASparseCheckoutFromTheManifestCarriesTheTierAndNothingElse(unittest.TestCase):
    """(d) End to end, on a real clone: the step this repository tells a caller to run."""

    def test_the_narrowed_clone_holds_exactly_what_the_manifest_matches(self) -> None:
        lines = manifest_lines()
        self.assertTrue(lines, "the manifest is empty — the clone below would prove nothing")
        clone = pathlib.Path(tempfile.mkdtemp(prefix="core-mount-"))
        try:
            subprocess.run(
                ["git", "clone", "-c", "core.longpaths=true", "--no-checkout",
                 str(REPO_ROOT), str(clone)],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            git(clone, "sparse-checkout", "set", "--no-cone", "--stdin",
                stdin="\n".join(lines) + "\n")
            git(clone, "checkout")

            on_disk = sorted(
                path.relative_to(clone).as_posix()
                for path in clone.rglob("*")
                if path.is_file() and ".git" not in path.relative_to(clone).parts
            )
            matched = sorted(
                line for line in git(clone, "ls-files", "--", *lines).splitlines() if line
            )
            self.assertEqual(
                on_disk,
                matched,
                "the two consumers of the manifest disagree: what sparse-checkout put on "
                "disk is not what `git ls-files` matches from the same lines",
            )

            tracked = set(git(clone, "ls-files").splitlines())
            for path in CONSTRUCTION_SIDE_FILES:
                self.assertIn(
                    path,
                    tracked,
                    f"{path} is not tracked in the clone at all, so its absence from disk "
                    "would say nothing about the narrowing",
                )
                self.assertNotIn(
                    path,
                    on_disk,
                    f"{path} is construction-side and reached a narrowed checkout",
                )
        finally:
            shutil.rmtree(clone, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
