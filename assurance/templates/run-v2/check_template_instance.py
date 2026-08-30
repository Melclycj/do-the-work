#!/usr/bin/env python3
"""Authoring gate for a v2 run instance (W2-A5 + M11). Run before START; exit 1 blocks.

Three deterministic requirements, of which the last two are **form-conditional** since
SIMP-B1 (2026-08-05):

1. the WorkSpec declares ``schema_version: "2"`` — newly authored specs always declare
   their schema (the v2-mandate, ``a22cca0``); a version-less spec here is a template
   misuse, not a legal historical form. Applies to both forms;
2. if the frozen instruction has a non-trivial preamble (content before its first
   ``## `` heading), the unit map anchors into it at least once — the w1-r1
   unmapped-preamble lesson made mechanical. The check establishes the map *faces* the
   preamble; whether the mapping is adequate is FULL review's question, not this script's;
3. the run-local ``control/paragraph-map.json`` exists, enumerates exactly the
   instruction-derived paragraph skeleton, is classified on every entry, and passes the
   three-way cross-check (instruction bytes ⟷ map ⟷ unit map) — the p3-corr
   omission-invisible lesson made mechanical (M11, Phase C4). Whether a *classification*
   is right stays FULL review's question; what this gate closes is silent absence.

Under the **enumerated** form (2 and 3 skipped): the instruction declares
``form: enumerated`` and ``resolve_form`` establishes it — every block of prose lives
inside a numbered ``R<n>`` section or inside Context, so there is no preamble left to
map and no classification column left to fill. Both legs exist to catch normative text
sitting where no obligation reaches it, and that is now a structural property of the file
rather than a per-run artifact. The resolution is fail-heavy and is **printed either
way**: a declaration the structure does not bear out resolves to ``prose`` and the run
owes both legs again, with the reasons named.

The cores are pure functions over data (``spec_version_issues``, ``preamble_issues``,
``paragraph_map_issues``) so the acceptance tests can exercise them without a filesystem;
the form branch itself lives in ``rsclib.document_harness.instruction.resolve_form``, one
place, so no caller can spell "could not decide" as the cheap answer; ``main`` is the IO
shell.
The instruction is read at the pinned revision when it resolves there, else from the
worktree — and which tree was read is disclosed rather than silent (the subject-tree
discipline).

Usage:  python check_template_instance.py <run-dir> [<repo-root>]
"""
from __future__ import annotations

import pathlib
import subprocess
import sys

# __file__-based on purpose: this locates the co-located library, not run data (the run
# directory and the repository the instruction is pinned in both arrive as arguments, and
# since the split that repository is the caller's, which holds no library).
HERE = pathlib.Path(__file__).resolve().parent
RS_ROOT = HERE.parents[2]
sys.path.insert(0, str(RS_ROOT / "tooling"))


def preamble_of(instruction_text: str) -> str:
    """Everything before the first '## ' heading. The whole file when there is none."""
    lines = []
    for line in instruction_text.splitlines():
        if line.startswith("## "):
            break
        lines.append(line)
    return "\n".join(lines)


def preamble_is_trivial(preamble: str) -> bool:
    """Trivial = nothing but blank lines and the '# ' title."""
    return all(not line.strip() or line.startswith("# ") for line in preamble.splitlines())


def spec_version_issues(spec: dict) -> list[str]:
    """Requirement 1, split out of `preamble_issues` by SIMP-B1 because it is the one leg
    both forms owe: the enumerated form skips the preamble mapping, never the v2-mandate."""
    if spec.get("schema_version") != "2":
        return [
            "TEMPLATE-SPEC-NOT-V2: the WorkSpec does not declare schema_version '2'; "
            "newly authored specs always declare their schema (the v2-mandate)"
        ]
    return []


def preamble_issues(spec: dict, instruction_text: str) -> list[str]:
    """Requirement 2 — the prose form's preamble-mapping leg, as rendered strings."""
    issues: list[str] = []
    preamble = preamble_of(instruction_text)
    if preamble_is_trivial(preamble):
        return issues
    instruction_path = spec.get("instruction_ref", {}).get("path")
    mapped = [
        unit
        for unit in spec.get("instruction_units", [])
        if unit.get("locator", {}).get("path") == instruction_path
        and unit.get("locator", {}).get("anchor", "") in preamble
        and unit.get("locator", {}).get("anchor", "")
    ]
    if not mapped:
        issues.append(
            "TEMPLATE-PREAMBLE-UNMAPPED: the instruction's preamble carries content but no "
            "instruction unit anchors into it; the START approval surface would be narrower "
            "than the instruction (issue-w1-r1-unmapped-preamble)"
        )
    return issues


def paragraph_map_issues(
    spec: dict, instruction_text: str, paragraph_map: dict, derived: list
) -> list[str]:
    """The three-way cross-check (M11): instruction bytes ⟷ map ⟷ unit map.

    ``derived`` is the skeleton the caller computed from the instruction text via
    ``rsclib.document_harness.instruction.paragraph_skeleton`` — passed in, not imported,
    so this core stays a pure function over data and the module stays import-safe as a
    standalone script.

    Leg 1 (bytes ⟷ map): the map must name the WorkSpec's exact frozen instruction and
    enumerate exactly the derived skeleton — count, index, lines, digest. A mismatch is a
    stale or tampered map, and every later judgment over it would be about bytes nobody
    classified, so the binding legs answer first and alone.
    Leg 2 (map ⟷ units): every obligation-classified paragraph needs at least one unit
    anchoring into it — the p3-corr omission made mechanical. An entry without an explicit
    classification is refused, never defaulted (defect M8's lesson).
    Leg 3 (units ⟷ bytes): a unit whose anchor lands in no enumerated paragraph is
    dangling — it maps text the instruction does not carry.
    """
    binding: list[str] = []
    spec_ref = spec.get("instruction_ref", {})
    map_ref = paragraph_map.get("instruction_ref", {})
    for field in ("path", "revision"):
        if map_ref.get(field) != spec_ref.get(field):
            binding.append(
                f"TEMPLATE-PARAGRAPH-MAP-INSTRUCTION-MISMATCH: the map's instruction_ref "
                f"{field} is not the WorkSpec's; the map classifies a different frozen "
                "instruction"
            )
    entries = paragraph_map.get("paragraphs", [])
    if len(entries) != len(derived):
        binding.append(
            f"TEMPLATE-PARAGRAPH-MAP-STALE: the map enumerates {len(entries)} "
            f"paragraph(s) but the instruction derives {len(derived)}; regenerate the "
            "skeleton and re-fill the classification column"
        )
    for want, got in zip(derived, entries):
        for field in ("index", "start_line", "end_line", "digest_sha256"):
            if got.get(field) != want[field]:
                binding.append(
                    f"TEMPLATE-PARAGRAPH-MAP-STALE: entry {want['index']} {field} does "
                    "not match the instruction-derived skeleton"
                )
                break
    if binding:
        return binding

    issues: list[str] = []
    lines = instruction_text.splitlines()
    instruction_path = spec_ref.get("path")
    units = [
        unit
        for unit in spec.get("instruction_units", [])
        if unit.get("locator", {}).get("path") == instruction_path
        and unit.get("locator", {}).get("anchor")
    ]
    paragraph_texts = {
        entry["index"]: "\n".join(lines[entry["start_line"] - 1 : entry["end_line"]])
        for entry in derived
    }
    for want, got in zip(derived, entries):
        classification = got.get("classification")
        if classification not in ("obligation", "context"):
            issues.append(
                f"TEMPLATE-PARAGRAPH-UNCLASSIFIED: entry {want['index']} carries no "
                "explicit classification; an unfilled column is refused, never defaulted "
                "(defect M8's lesson)"
            )
            continue
        if classification == "obligation":
            text = paragraph_texts[want["index"]]
            if not any(unit["locator"]["anchor"] in text for unit in units):
                issues.append(
                    f"TEMPLATE-PARAGRAPH-UNCOVERED: paragraph {want['index']} (lines "
                    f"{want['start_line']}-{want['end_line']}) is classified obligation "
                    "but no instruction unit anchors into it (the p3-corr omission class)"
                )
    for unit in units:
        anchor = unit["locator"]["anchor"]
        if not any(anchor in text for text in paragraph_texts.values()):
            issues.append(
                f"TEMPLATE-UNIT-ANCHOR-DANGLING: unit {unit.get('unit_id')} anchors "
                f"{anchor!r} into no enumerated paragraph"
            )
    return issues


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 2
    run_dir = pathlib.Path(argv[1])
    if len(argv) > 2:
        repo_root = pathlib.Path(argv[2])
    else:
        # The run directory lives in the CALLER's repository at whatever depth that
        # caller keeps it — the old `parents[3]` default was the first caller's layout,
        # silently wrong anywhere else (round STRANGER-GUARDS). Discover, or refuse
        # loudly; never a wrong root taken quietly.
        from rsclib.document_harness import SpecGap
        from rsclib.document_harness.caller import discover_repo_root

        try:
            repo_root = discover_repo_root(run_dir)
        except SpecGap as exc:
            print(f"SPEC_GAP: {exc}")
            return 2
        print(f"repo root discovered: {repo_root}", file=sys.stderr)
    from rsclib.document_harness import load_json, validate  # noqa: E402
    from rsclib.document_harness.instruction import (  # noqa: E402
        FORM_ENUMERATED,
        paragraph_skeleton,
        resolve_form,
    )

    spec = load_json(run_dir / "control" / "work-spec.json")
    ref = spec.get("instruction_ref", {})
    shown = subprocess.run(
        ["git", "-C", str(repo_root), "show", f"{ref.get('revision', '')}:{ref.get('path', '')}"],
        check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    if shown.returncode == 0:
        text, tree = shown.stdout.decode("utf-8", errors="replace"), "pinned revision"
    else:
        target = repo_root / ref.get("path", "")
        if not target.is_file():
            print(f"TEMPLATE-INSTRUCTION-MISSING: {ref.get('path')} resolves in neither the "
                  "pinned revision nor the worktree")
            return 1
        text, tree = target.read_text(encoding="utf-8"), "worktree (NOT the pinned revision)"
    print(f"instruction read from: {tree}")

    form, notes = resolve_form(text)
    print(f"instruction form   : {form}")
    for note in notes:
        print(f"  {note}")

    issues = spec_version_issues(spec)
    if form == FORM_ENUMERATED:
        print("form-conditional   : preamble gate and paragraph map skipped (SIMP-B1) — "
              "every block is inside a numbered section or Context, established above")
    else:
        issues += preamble_issues(spec, text)
        map_path = run_dir / "control" / "paragraph-map.json"
        if map_path.is_file():
            paragraph_map = load_json(map_path)
            issues += [issue.render() for issue in validate("paragraph_map", paragraph_map).issues]
            issues += paragraph_map_issues(
                spec, text, paragraph_map, list(paragraph_skeleton(text)))
        else:
            issues.append(
                "TEMPLATE-PARAGRAPH-MAP-MISSING: control/paragraph-map.json does not exist; "
                "generate the skeleton with make_paragraph_map.py and fill the classification "
                "column — an unenumerated instruction is the p3-corr omission shape")
    for issue in issues:
        print(issue)
    print("authoring gate:", "PASS" if not issues else f"{len(issues)} issue(s)")
    return 0 if not issues else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
