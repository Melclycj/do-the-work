#!/usr/bin/env python3
"""TEMPLATE — repair step: record the user's REPAIR decision and enter REPAIRING.

Run in place from ``templates/run-v2/`` against the run directory — a run copies no step script
(`HD-11` part two, A2-R3) and there is no CONFIG block to
fill: the run directory arrives as an argument and everything else is already in the run's
own ``control/``. This step runs **only on a repaired path**: after a round-0 FULL returned a
blocker and the user decided to repair. A clean round never reaches it and never needs the file.

It is not bookkeeping. ``flow.check_repair_decision`` is the gate that verifies the repair binds
the candidate that was actually reviewed, that every accepted finding id exists in that review,
and that the repair boundary does not widen the run's (EXECUTION.md, *After a review*: a repair
boundary may narrow the run's and never widen it). Entering REPAIRING is also the one transition
that moves ``repair_round`` to 1, which is why ``flow.advance_checked`` is used rather than
``assurance_state.advance`` — the pointer rules read that counter, and an authorization recorded
at round 0 is rejected as preceding the repair it authorizes.

Skipping the step skips the gate, and the flow strands: ``run_bind_v2`` at round 0 stops at
REVIEWED and owes a repair decision, and ``dtw dispatch`` refuses the round-1 VERIFY because
the state carries no ``repair_decision_ref`` to derive its scope from. Witnessed on p5b-claims,
which advanced straight to the round-1 evidence pass: both gates then passed clean, but they
confirmed the repair rather than gating it, and unwinding the state to its round-0 position and
re-walking the sequence cost the run a detour. That happened because no document named this step
— the omission this file and the README line beside it close. p3-corr wrote the same transition
by hand before the templates existed; ``../../runs/p5b-claims/run_repair.py`` is the worked
instance this template was lifted from, including the docstring habit of recording, in the run's
own copy, which findings were accepted and which were carried to FINAL unrepaired.

The decision document itself is **read, never authored here**: every ``UserDecision`` is the
user's (EXECUTION.md, *What you may never author*), it is already on disk before this runs, and
re-emitting it from this script would make the executor its author.

Run:  python -X utf8 run_repair.py <run-dir> [--repo-root <path>] [--emit]
"""
from __future__ import annotations

import argparse
import pathlib
import sys
from typing import Sequence

# __file__-based on purpose: this locates the co-located library, not run data (the run
# directory arrives as an argument).
HERE = pathlib.Path(__file__).resolve().parent
RS_ROOT = HERE.parents[2]
sys.path.insert(0, str(RS_ROOT / "tooling"))

from rsclib.document_harness import load_json  # noqa: E402
from rsclib.document_harness import assurance_state, flow  # noqa: E402


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("run_dir", type=pathlib.Path,
                        help="the run's control root, e.g. ResearchSystem/assurance/runs/<run-id>")
    parser.add_argument("--repo-root", type=pathlib.Path, default=None,
                        help="repository root; defaults to the run directory's fourth parent")
    parser.add_argument("--emit", action="store_true",
                        help="write the state transition; without it the step only reports")
    args = parser.parse_args(argv)

    run_dir = args.run_dir.resolve()
    REPO = args.repo_root.resolve() if args.repo_root else run_dir.parents[3]
    RUN_ID = run_dir.name
    CONTROL = run_dir / "control"
    EVIDENCE = run_dir / "evidence"
    CONTROL_ROOT = run_dir.relative_to(REPO).as_posix()

    # The operative review is always the round-0 FULL: a repair exists because the FULL asked
    # for one, and the VERIFY that answers this repair has not been written yet.
    review = load_json(EVIDENCE / "review-full.json")
    plan = load_json(CONTROL / "resolved-plan.json")
    state = assurance_state.load(CONTROL / "state.json")
    decision = load_json(CONTROL / "user-decision-repair.json")

    report = flow.check_repair_decision(decision, review, plan)
    print(f"check_repair_decision : {'clean' if report.ok else 'ISSUES'}")
    for issue in report.issues:
        print("  " + issue.render()[:180])
    if not report.ok:
        return 1
    print(f"accepted findings     : {len(decision['target']['accepted_finding_ids'])} "
          f"({', '.join(decision['target']['accepted_finding_ids'])})")

    if not args.emit:
        print("dry run               : pass --emit to advance the state to REPAIRING")
        return 0

    state = flow.advance_checked(
        state, "REPAIRING",
        repair_decision_ref=assurance_state.pointer_for(
            "repair_decision_ref", f"{CONTROL_ROOT}/control/user-decision-repair.json", REPO),
        next_action=f"executor authors candidate C2 on {RUN_ID}-candidate, then regenerates "
                    "every evidence document and a NEW evidence commit",
    )
    assurance_state.save(state, CONTROL / "state.json")
    print(f"emitted               : state -> REPAIRING (repair_round {state['repair_round']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
