#!/usr/bin/env python3
"""TEMPLATE — deterministic comparator for `command_exit` equality demands.

Copy into ``runs/<run-id>/`` **before the instruction-freeze commit**: the comparator must
live at the run base so the materialized candidate tree carries it (a control-plane script
referenced by a candidate-tree check exists nowhere else). There is no CONFIG block to fill
(`HD-11` part one, R2): every per-run constant arrives as an **argument**, so a run declares
them in the frozen `argv` of the check spec that binds the mode, and the copied file is the
same bytes in every run. Every mode runs inside that tree (cwd = repo root of the
materialization) and decides one equality/shape question against a pinned source that is
outside the run's write scope. First instantiated (pre-template) by run p4-doc; per the
README's authoring rule, mechanically comparable demands bind one of these modes, never a
`locator_exists` proxy.

Two defects of the p4-doc lineage are fixed here (routed `VERIFIER_FIX` by
`runs/p4-doc/issues/user-decision-triage-comparator-environment-defects.json`,
2026-08-01):

1. every subprocess decode is explicit ``encoding="utf-8", errors="replace"`` — the
   lineage's ``text=True`` used the locale encoding and crashed under a GBK Windows
   console on UTF-8 diff output;
2. ``--rebuild`` compares the rebuilt bytes against the ``git show`` **blob bytes**
   directly — the lineage judged via ``git status --porcelain`` / working-tree diff,
   which is eol-normalization sensitive: false-FAIL in a CRLF-checkout materialized
   worktree, and symmetrically able to false-PASS a CRLF-emitting rebuild (p4-doc FULL
   finding f2; the reviewer's own sha256-vs-blob proof is this mode's method now).

Modes (exit 0 = the demand holds; exit 1 + report = it does not). The mode flags keep the
spellings the p4-doc lineage froze, so a check spec's `argv` stays expressible; what R2 adds
after the mode is that run's own constants:

  --blocks --source <path> --owner <path> … --site <id>=<owner>::<start>::<end> …
                  rendered ```research-object fence bodies are byte-identical (after
                  CRLF->LF normalization) to the pinned-source bodies, each sited inside
                  its declared owner section
  --subsections   (optional per run) rendered sections equal a deterministic transform of
                  the pinned source — adapt or delete per the run's demands
  --prose --base <sha> --owner <path> … [--prose-append <line-prefix>::<suffix> …]
                  zero-prose-rewrite: in the base->HEAD diff of the owner files the only
                  removed lines are the declared line-gaining-a-suffix replacements;
                  everything else is pure addition
  --rebuild --generated <path> … --rebuild-argv <command> …
                  delete the declared generated files, re-run the generator, and require
                  each rebuilt file to be byte-identical to its HEAD blob

Run:  python -X utf8 compare_blocks.py <mode> [that mode's declarations]
"""
from __future__ import annotations

import argparse
import pathlib
import re
import subprocess
from typing import Sequence

# `cwd`-based on purpose, and the one derivation that stays: every mode runs INSIDE the
# materialized candidate tree — the check spec sets `cwd` to the repo root of that
# materialization — so the tree under comparison is the working directory itself, never a
# path derived from where this file happens to sit.
REPO = pathlib.Path.cwd()

FENCE_OPEN = "```research-object"
FENCE_CLOSE = "```"

#: Per mode, the declarations that mode cannot proceed without — enforced here rather than
#: with argparse's own `required=`, which is per-option and would demand `--generated` of a
#: `--blocks` run. Nothing is defaulted: a comparator that quietly accepted "no owners, no
#: sites" would print PASS having compared nothing, which is the failure mode R2's
#: no-defaults rule closes on the three step scripts.
REQUIRED_PER_MODE: dict[str, tuple[tuple[str, str], ...]] = {
    "blocks": (("--source", "source"), ("--owner", "owner"), ("--site", "site")),
    "subsections": (),
    "prose": (("--base", "base"), ("--owner", "owner")),
    "rebuild": (("--generated", "generated"), ("--rebuild-argv", "rebuild_argv")),
}


def run(argv: list[str]) -> subprocess.CompletedProcess:
    """Every child process decodes UTF-8 explicitly — never the console locale (fix 1)."""
    return subprocess.run(
        argv, capture_output=True, encoding="utf-8", errors="replace")


def read_lines(rel: str) -> list[str]:
    return (REPO / rel).read_text(encoding="utf-8").replace("\r\n", "\n").split("\n")


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    raise SystemExit(1)


def parse_site(raw: str) -> tuple[str, tuple[str, str, str]]:
    """``<object-id>=<owner>::<section-start>::<section-end>``, refused if it is not.

    A fence must sit strictly between the two anchor lines of its owner file; each prefix
    must occur exactly once in that file. Split on a fixed separator and checked for the
    exact field count, so an anchor that itself contains ``::`` is refused loudly here
    rather than mis-split into a demand nobody wrote.
    """
    object_id, _, rest = raw.partition("=")
    if not object_id or not rest:
        fail(f"--site must be <object-id>=<owner>::<section-start>::<section-end>, got {raw!r}")
    fields = rest.split("::")
    if len(fields) != 3:
        fail(f"--site {object_id}: expected <owner>::<section-start>::<section-end>, found "
             f"{len(fields)} '::'-separated field(s) in {rest!r}")
    return object_id, (fields[0], fields[1], fields[2])


def parse_prose_append(raw: str) -> tuple[str, str]:
    """``<line-prefix>::<suffix>`` — a prose line that legitimately gains an appended suffix."""
    fields = raw.split("::")
    if len(fields) != 2 or not fields[0] or not fields[1]:
        fail(f"--prose-append must be <line-prefix>::<suffix>, got {raw!r}")
    return fields[0], fields[1]


def extract_fences(lines: list[str]) -> list[tuple[int, str]]:
    fences: list[tuple[int, str]] = []
    i = 0
    while i < len(lines):
        if lines[i].strip() == FENCE_OPEN:
            j = i + 1
            body: list[str] = []
            while j < len(lines) and lines[j].strip() != FENCE_CLOSE:
                body.append(lines[j])
                j += 1
            if j >= len(lines):
                fail(f"unclosed research-object fence at line {i + 1}")
            fences.append((i, "\n".join(body)))
            i = j
        i += 1
    return fences


def object_id_of(body: str) -> str:
    m = re.match(r"object_id:\s*(\S+)", body)
    return m.group(1) if m else "<missing object_id>"


def line_index(lines: list[str], startswith: str, rel: str) -> int:
    hits = [i for i, ln in enumerate(lines) if ln.startswith(startswith)]
    if len(hits) != 1:
        fail(f"{rel}: expected exactly one line starting with {startswith!r}, found {len(hits)}")
    return hits[0]


def mode_blocks(source: str, owners: list[str], sites: dict[str, tuple[str, str, str]]) -> None:
    expected_ids = set(sites)
    source_fences = extract_fences(read_lines(source))
    src_by_id = {object_id_of(body): body for _, body in source_fences}
    if not expected_ids <= set(src_by_id):
        fail(f"pinned source lacks expected ids: {sorted(expected_ids - set(src_by_id))}")

    seen: dict[str, tuple[str, int, str]] = {}
    for rel in owners:
        for at, body in extract_fences(read_lines(rel)):
            oid = object_id_of(body)
            if oid in seen:
                fail(f"duplicate rendered block {oid}: {seen[oid][0]} and {rel}")
            seen[oid] = (rel, at, body)
    if set(seen) != expected_ids:
        fail(f"rendered object ids {sorted(seen)} != expected {sorted(expected_ids)}")

    for oid, (owner, start_anchor, end_anchor) in sites.items():
        rel, at, body = seen[oid]
        if rel != owner:
            fail(f"{oid} rendered in {rel}, declared owner is {owner}")
        lines = read_lines(owner)
        lo = line_index(lines, start_anchor, owner)
        hi = line_index(lines, end_anchor, owner)
        if not lo < at < hi:
            fail(f"{oid} fence at {owner}:{at + 1} is outside its declared section")
        if body != src_by_id[oid]:
            import difflib
            diff = "\n".join(difflib.unified_diff(
                src_by_id[oid].split("\n"), body.split("\n"),
                fromfile=f"source {oid}", tofile=f"{owner} rendered", lineterm=""))
            fail(f"{oid} body differs from the pinned source:\n{diff}")
    print(f"PASS: {len(expected_ids)} rendered blocks byte-identical to the pinned source, "
          "each inside its declared section")


def mode_subsections() -> None:
    fail("this run declared no subsection transform — adapt this mode from the p4-doc "
         "lineage or remove the check that binds it")


def mode_prose(base: str, owners: list[str], prose_appends: dict[str, str]) -> None:
    result = run(["git", "diff", "--unified=0", base, "HEAD", "--"] + owners)
    if result.returncode not in (0, 1):
        fail(f"git diff failed (exit {result.returncode}): {result.stderr[:200]}")
    removed: list[str] = []
    added: list[str] = []
    for ln in (result.stdout or "").split("\n"):
        # Anchor to true diff-header shapes only: a bare startswith("---") swallows a
        # removed owner line that itself begins with "--" (e.g. a deleted markdown hr),
        # false-PASSing the zero-rewrite guard (FULL 5f029cd finding L-1; git diff runs
        # with default prefixes, so these four forms are exhaustive).
        if (ln.startswith("--- a/") or ln.startswith("+++ b/")
                or ln.startswith("--- /dev/null") or ln.startswith("+++ /dev/null")):
            continue
        if ln.startswith("-"):
            removed.append(ln[1:])
        elif ln.startswith("+"):
            added.append(ln[1:])
    if len(removed) != len(prose_appends):
        fail(f"expected exactly {len(prose_appends)} removed lines, found {len(removed)}: "
             f"{removed[:5]}")
    matched: set[str] = set()
    for r in removed:
        prefix = next((p for p in prose_appends if r.startswith(p)), None)
        if prefix is None:
            fail(f"removed line is not a declared suffix-gaining line: {r[:120]!r}")
        if prefix in matched:
            fail(f"the same prose line was removed twice: {r[:120]!r}")
        matched.add(prefix)
        if r + " " + prose_appends[prefix] not in added:
            fail(f"removed line was not re-added as itself + ' {prose_appends[prefix]}'")
    print(f"PASS: zero prose rewrite — {len(removed)} removed lines, all re-added "
          "verbatim + suffix; all other diff lines are additions")


def mode_rebuild(generated: list[str], rebuild_argv: list[str]) -> None:
    """Delete + regenerate, then compare each file's bytes to its HEAD blob (fix 2)."""
    for rel in generated:
        (REPO / rel).unlink()
    r = subprocess.run(rebuild_argv, capture_output=True)
    if r.returncode != 0:
        fail(f"rebuild command failed (exit {r.returncode}):\n"
             f"{r.stdout.decode('utf-8', 'replace')[:400]}\n"
             f"{r.stderr.decode('utf-8', 'replace')[:400]}")
    for rel in generated:
        blob = subprocess.run(
            ["git", "show", f"HEAD:{rel}"], capture_output=True)
        if blob.returncode != 0:
            fail(f"git show HEAD:{rel} failed: {blob.stderr.decode('utf-8', 'replace')[:200]}")
        disk = (REPO / rel).read_bytes()
        if disk != blob.stdout:
            fail(f"delete+rebuild is NOT byte-identical to the HEAD blob: {rel} "
                 f"(rebuilt {len(disk)} B vs blob {len(blob.stdout)} B)")
    print(f"PASS: {len(generated)} generated file(s) delete+rebuild byte-identical "
          "to their HEAD blobs")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--blocks", action="store_const", const="blocks", dest="mode",
                      help="rendered fence bodies equal the pinned source's, each in its section")
    mode.add_argument("--subsections", action="store_const", const="subsections", dest="mode",
                      help="rendered sections equal the run's declared transform of the source")
    mode.add_argument("--prose", action="store_const", const="prose", dest="mode",
                      help="zero prose rewrite in the base->HEAD diff of the owner files")
    mode.add_argument("--rebuild", action="store_const", const="rebuild", dest="mode",
                      help="delete + regenerate is byte-identical to the HEAD blobs")
    parser.add_argument("--source", default=None,
                        help="the pinned source document the equality demands compare against "
                             "(outside the run's write scope)")
    parser.add_argument("--owner", action="append", default=[], metavar="PATH",
                        help="an owner file the run renders into; repeat once per file")
    parser.add_argument("--site", action="append", default=[],
                        metavar="ID=OWNER::START::END",
                        help="where one object_id's fence must sit; repeat once per object")
    parser.add_argument("--base", default=None, metavar="SHA",
                        help="--prose: the run base the diff is taken from")
    parser.add_argument("--prose-append", action="append", default=[],
                        metavar="PREFIX::SUFFIX",
                        help="--prose: a prose line that legitimately gains an appended suffix; "
                             "repeat once per line. None declared means no line may be removed")
    parser.add_argument("--generated", action="append", default=[], metavar="PATH",
                        help="--rebuild: a generated file to delete and re-derive; repeat")
    parser.add_argument("--rebuild-argv", nargs=argparse.REMAINDER, default=[],
                        metavar="COMMAND",
                        help="--rebuild: the command that rebuilds them, taken verbatim and "
                             "naming its own interpreter as the check spec's argv does. Must "
                             "come last: every remaining token belongs to it")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    for flag, dest in REQUIRED_PER_MODE[args.mode]:
        if not getattr(args, dest):
            fail(f"--{args.mode} needs {flag}; this run declared none, and nothing here is "
                 "defaulted")
    if args.mode == "blocks":
        mode_blocks(args.source, args.owner, dict(parse_site(raw) for raw in args.site))
    elif args.mode == "subsections":
        mode_subsections()
    elif args.mode == "prose":
        mode_prose(args.base, args.owner,
                   dict(parse_prose_append(raw) for raw in args.prose_append))
    elif args.mode == "rebuild":
        mode_rebuild(args.generated, args.rebuild_argv)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
