#!/usr/bin/env python3
"""Generate the run-local paragraph-map skeleton (M11). The human fills ONLY `classification`.

Enumerates the frozen instruction into ``control/paragraph-map.json``: every derived
column (index, 1-based inclusive lines, content digest) is machine-written; the
``classification`` column — ``"obligation" | "context"`` per entry — is deliberately
absent, because that judgment is the human's, and a machine default here would be defect
M8 (a status nobody asserted) in a new place. The freshly generated file is therefore
schema-invalid on purpose until every entry is answered; the authoring gate
(``check_template_instance.py``) refuses an unfilled or stale map.

Refuses to overwrite an existing map: a filled classification column is never clobbered
by regeneration — delete the file first if regeneration is intended.

Usage:  python make_paragraph_map.py <run-dir> [<repo-root>]
"""
from __future__ import annotations

import json
import pathlib
import subprocess
import sys

# __file__-based on purpose: this locates the co-located library, not run data (the run
# directory and the repository the instruction is pinned in both arrive as arguments, and
# since the split that repository is the caller's, which holds no library).
HERE = pathlib.Path(__file__).resolve().parent
RS_ROOT = HERE.parents[2]
sys.path.insert(0, str(RS_ROOT / "tooling"))


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
    map_path = run_dir / "control" / "paragraph-map.json"
    if map_path.exists():
        print(
            f"PARAGRAPH-MAP-EXISTS: {map_path} already exists; a filled classification "
            "column is never clobbered — delete the file first if regeneration is intended")
        return 1
    from rsclib.document_harness import load_json  # noqa: E402
    from rsclib.document_harness.instruction import paragraph_skeleton  # noqa: E402

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
            print(f"PARAGRAPH-MAP-INSTRUCTION-MISSING: {ref.get('path')} resolves in "
                  "neither the pinned revision nor the worktree")
            return 1
        text, tree = target.read_text(encoding="utf-8"), "worktree (NOT the pinned revision)"
    print(f"instruction read from: {tree}")

    document = {
        "schema_version": "1",
        "work_id": spec.get("work_id"),
        "instruction_ref": {"path": ref.get("path"), "revision": ref.get("revision")},
        "paragraphs": [dict(entry) for entry in paragraph_skeleton(text)],
    }
    map_path.parent.mkdir(parents=True, exist_ok=True)
    map_path.write_text(
        json.dumps(document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {len(document['paragraphs'])} paragraph(s) to {map_path}")
    print('fill the classification column: every entry needs "classification": '
          '"obligation" | "context"; the authoring gate refuses an unfilled or stale map')
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
