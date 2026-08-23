#!/usr/bin/env python3
"""TEMPLATE — closeout retirement step: a CheckResult does not survive its run (HD-12).

Run in place from ``templates/run-v2/`` against the run directory — a run copies no step
script (`HD-11`) and there is no CONFIG block to fill: the run directory arrives as the one
argument this step needs, and everything else — the run's status, the committed plan's
``check_order`` — is already in the run's own ``control/``. It runs **only after CLOSED**:
the state's own terminal status (`flow.py`'s ``TERMINAL_STATUSES``), reached once and never
left, is the entire eligibility condition. A run in any earlier status — including
``STOPPED_REPLAN``, which this decision leaves alone — refuses with the status it actually
carries, and nothing is deleted.

``HD-12`` (2026-08-08, user, batch A `D2`): once a run closes, its per-CheckResult files
(``evidence/check-<check_id>.json``, one per id the committed plan's ``check_order`` names)
are retired — deleted, never rewritten — and only the aggregate
(``evidence/check-results.json``) and the raw one-hand output each check wrote
(``evidence/<check_id>.out.txt``, where a ``command_exit`` check produced one) survive.
The ruling reaches **only future runs**: the eight runs already closed when it was taken stay
exactly as they are, per the plan's closed-runs-are-read-only constraint, and this script
never walks them — it only ever acts on the one run directory it is pointed at.

What HD-12 leaves alone (ruled D-a, same session): the ``check_result_refs`` array on
``control/assurance-candidate.json`` is not touched by this step, or by anything else. Each
entry already carries a ``digest_sha256`` computed over the bytes of a file this run
committed to git — deleting the working-tree copy deletes nothing from that history, and
``git show <evidence-commit>:<path>`` still resolves the exact bytes the digest was taken
over. The array keeps pointing at paths this script may just have removed from the worktree;
that is the ruling, not an oversight this step owes a fix for.

What this step does not relax: for every status before CLOSED, the per-check file this
script retires is still load-bearing. ``review_subject.check_subject``'s completeness pass
re-derives the expected file set from the committed plan's ``check_order`` and requires each
one to resolve in the evidence commit for every live run exactly as before — the CLOSED
carve-out lives in that function, keyed off the same state this script reads, and this script
itself enforces nothing; it only deletes what CLOSED already permits absent.

The deletion is staged, never committed: ``git rm -q --`` leaves the removal in the index for
whatever commit the operator takes next, the same way an evidence commit elsewhere in this
template family is a deliberate, explicit act rather than a side effect of a housekeeping
script.

Run:  python -X utf8 run_retire.py <run-dir> [--repo-root <path>]
"""
from __future__ import annotations

import argparse
import pathlib
import subprocess
import sys
from typing import Sequence

# __file__-based on purpose: this locates the co-located library, not run data (the run
# directory arrives as an argument).
HERE = pathlib.Path(__file__).resolve().parent
RS_ROOT = HERE.parents[2]
sys.path.insert(0, str(RS_ROOT / "tooling"))

from rsclib.document_harness import load_json  # noqa: E402
from rsclib.document_harness import SpecGap  # noqa: E402
from rsclib.document_harness.caller import discover_repo_root  # noqa: E402
from rsclib.document_harness import assurance_state  # noqa: E402
from rsclib.document_harness import review_subject as RS  # noqa: E402


def plan_closeout(
    status: str, check_order: Sequence[str], existing_ids: Sequence[str]
) -> tuple[list[str], list[str], str | None]:
    """Which per-CheckResult files a CLOSED run's closeout retires (HD-12). Pure — no I/O.

    Decides from data alone: the state's status, the committed plan's derived
    ``check_order``, and the set of check ids whose per-result file is currently on disk.
    Returns ``(to_delete, already_gone, refusal)`` — a non-empty ``refusal`` means the run is
    not eligible and the other two are always empty in that case, never a partial answer.

    The gate is status alone, not a second look at the round or at anything else on the
    state: HD-12 binds retirement to the run having reached its terminal CLOSED status,
    and every earlier status — REPAIRING and a mid-repair EVIDENCED included — keeps every
    file this function would otherwise mark for deletion.
    """
    if status != "CLOSED":
        return [], [], (
            f"run status is {status}, not CLOSED — HD-12 retires per-CheckResult files only "
            "after a run closes"
        )
    existing = set(existing_ids)
    to_delete = [check_id for check_id in check_order if check_id in existing]
    already_gone = [check_id for check_id in check_order if check_id not in existing]
    return to_delete, already_gone, None


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("run_dir", type=pathlib.Path,
                        help="the run's control root, e.g. assurance/runs/<run-id>")
    parser.add_argument("--repo-root", type=pathlib.Path, default=None,
                        help="repository root; defaults to the git toplevel of the run directory (loud refusal outside a work tree)")
    args = parser.parse_args(argv)

    run_dir = args.run_dir.resolve()
    if args.repo_root:
        REPO = args.repo_root.resolve()
    else:
        # The run directory lives in the CALLER's repository at whatever depth that
        # caller keeps it — the old `parents[3]` default was the first caller's layout,
        # silently wrong anywhere else (round STRANGER-GUARDS). Discover, or refuse
        # loudly; never a wrong root taken quietly.
        try:
            REPO = discover_repo_root(run_dir)
        except SpecGap as exc:
            print(f"SPEC_GAP: {exc}")
            return 2
        print(f"repo root discovered: {REPO}", file=sys.stderr)
    CONTROL = run_dir / "control"
    EVIDENCE = run_dir / "evidence"
    CONTROL_ROOT = run_dir.relative_to(REPO).as_posix()

    state = assurance_state.load(CONTROL / "state.json")
    status = state["status"]

    # The plan is read only once the run is known to be CLOSED — a non-CLOSED run refuses
    # on status alone and owes this script no resolved-plan.json at all.
    if status == "CLOSED":
        plan = load_json(CONTROL / "resolved-plan.json")
        check_order = plan.get("check_order", [])
        existing_ids = [
            check_id for check_id in check_order
            if (run_dir / RS.CHECK_RESULT_PATH.format(check_id=check_id)).is_file()
        ]
    else:
        check_order, existing_ids = [], []

    to_delete, already_gone, refusal = plan_closeout(status, check_order, existing_ids)
    if refusal:
        print(f"STOP: {refusal}")
        return 1

    print(f"status                 : {status}")
    print(f"check_order            : {len(check_order)} check id(s)")

    for check_id in to_delete:
        rel = f"{CONTROL_ROOT}/{RS.CHECK_RESULT_PATH.format(check_id=check_id)}"
        subprocess.run(["git", "-C", str(REPO), "rm", "-q", "--", rel], check=True)
    print(f"deleted                : {len(to_delete)}"
          + (f" ({', '.join(to_delete)})" if to_delete else ""))
    print(f"already-retired        : {len(already_gone)}"
          + (f" ({', '.join(already_gone)})" if already_gone else ""))

    aggregate_present = (EVIDENCE / "check-results.json").is_file()
    # Derived from check_order the way the deletion set is — never a directory glob, whose
    # answer would depend on the unenforced `chk-` id convention and count files the plan
    # never named (FULL d52f41b L-3: this printed line is the retirement act's only record).
    out_files = [
        check_id for check_id in check_order
        if (EVIDENCE / f"{check_id}.out.txt").is_file()
    ]
    print(f"kept                   : {1 if aggregate_present else 0} aggregate "
          f"(check-results.json) + {len(out_files)} raw output(s) (<check_id>.out.txt)")
    print("note                   : check_result_refs in control/assurance-candidate.json "
          "stay as-is; their digests remain verifiable against the evidence commit in git "
          "history")

    if not to_delete:
        print("nothing to delete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
