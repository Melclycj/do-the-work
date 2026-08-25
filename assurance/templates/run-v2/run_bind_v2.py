#!/usr/bin/env python3
"""TEMPLATE — bind step, v2 shape: accept the round's review, bind every round, advance.

Run in place from ``templates/run-v2/`` against the run directory — a run copies no step script
(`HD-11` part two, A2-R3) and there is no CONFIG block
to fill: the run directory and the dispatched evidence commit arrive as arguments, and the
per-run constants come from the run's own ``control/`` JSON. Differences from the w1-r1
bind step: the operative result is validated with
``review_result_v2.check_review_result_v2`` against the **evidence commit SHA that was
actually dispatched** (``--evidence-commit``, not the result's own copy — trusting the
result's copy alone is the re-attribution class the binding closes), and the
recorded binding is ``review_subject.subject_binding`` (evidence commit + review digest)
instead of a package digest pair.

The repair round — read from ``control/state.json``, where the evidence step wrote it —
decides everything round-shaped here
(defect M9 — this file used to hard-read ``review-full.json``, bind that single ref and
carry no branch, so every repaired run had to hand-write the whole step; see
``../../runs/p3-corr/run_bind_candidate.py`` for the round-1 shape p3-corr wrote by hand,
now absorbed): which review file is the operative one (round 0: the FULL; round 1: the
targeted VERIFY, additionally reconciled against the user's repair decision via
``flow.check_verify_outcome``), which file the state's ``review_ref`` points at, and the
AssuranceCandidate binding **every round that happened** — the FULL is what the repair
answers, and dropping it would hide the round that found the blocker. One branch is not
round-shaped but verdict-shaped: at round 0 a verdict other than ``REVIEWED_NO_BLOCKER``
binds no candidate at all and stops at REVIEWED, because the next act is the user's repair
decision (``run_repair.py``) and AWAITING_FINAL is left only for CLOSED.

The assembly follows the worked precedents (round 0: ``../../runs/w1-r1/run_bind.py``;
round 1: p3-corr above): rich in references, poor in claims (V3-D5) — assembling is not
judging. ``unresolved_finding_ids`` is derived from the reviews in hand because N2-A9's
check enforces exactly that set in both directions; a hand-maintained list is wrong the
moment it drifts. The FINAL decision keeps the w1-r1 shape (``run_final.py``) and no FINAL
decision exists yet.

Run:  python -X utf8 run_bind_v2.py <run-dir> --evidence-commit <sha> --bound-at <date>
              [--repo-root <path>] [--emit]
"""
from __future__ import annotations

import argparse
import pathlib
import sys
from typing import Any, Mapping, Sequence

# __file__-based on purpose: this locates the co-located library, not run data (the run
# directory arrives as an argument).
HERE = pathlib.Path(__file__).resolve().parent
RS_ROOT = HERE.parents[2]
sys.path.insert(0, str(RS_ROOT / "tooling"))

from rsclib.document_harness import AssuranceFault, bytes_digest, canonical_digest, load_json, write_canonical  # noqa: E402
from rsclib.document_harness import SpecGap  # noqa: E402
from rsclib.document_harness.caller import discover_repo_root  # noqa: E402
from rsclib.document_harness import assurance_state  # noqa: E402
from rsclib.document_harness import flow  # noqa: E402
from rsclib.document_harness import review_result_v2 as RV  # noqa: E402
from rsclib.document_harness import review_subject as RS  # noqa: E402
from rsclib.document_harness import summary as S  # noqa: E402
from rsclib.document_harness.review import blocking_findings  # noqa: E402

#: The per-run declarations this step may not derive, and the two keys it must carry:
#:
#:   "governance_scan": whether the governance-frontmatter scan ran in this run
#:                      (assurance.schema.json governanceScanState) — included true
#:                      requires result_ref; false requires skip_reason.
#:   "disclosures":     run-specific disclosures ({"statement": ..., "source_ref": digestRef}),
#:                      each naming the owner-authored document it came from. Empty list when
#:                      there is nothing to disclose.
#:
#: There is no default for either. A skip_reason is an honest sentence about this run, and a
#: template that supplied one would be authoring the run's own excuse.
DECLARATIONS = "control/bind-declarations.json"


def round_documents(repair_round: int) -> list[str]:
    """The review files this round binds, oldest first; the last is the operative one.

    Round 0 has only the FULL. From round 1 on, the FULL and the targeted VERIFY both
    exist and both are bound — the schema caps ``review_refs`` at two because no third
    review round exists (V3-D6, N2-A11), and the flow's budget grants no second repair.
    """
    names = ["review-full.json"]
    if repair_round >= 1:
        names.append("review-verify.json")
    return names


def review_refs_of(
    names: Sequence[str], reviews: Sequence[Mapping[str, Any]], control_root: str
) -> list[dict[str, str]]:
    """One ref per round that happened, content-bound by canonical digest.

    Canonical, not bytes, is the kind the authoring precedent writes (w1-r1 run_bind) and
    the kind ``check_assurance_candidate`` reconciles against the reviews in hand — a
    count, or a verbatim-stored pointer, is satisfied by refs to anything.
    """
    return [
        {
            "path": f"{control_root}/evidence/{name}",
            "digest_sha256": canonical_digest(review),
        }
        for name, review in zip(names, reviews)
    ]


def unresolved_ids(reviews: Sequence[Mapping[str, Any]]) -> list[str]:
    """Every finding any bound review marked blocking — exactly, never a summary.

    N2-A9 is mechanical and deliberately unforgiving: ``blocking`` is a property of the
    immutable review that recorded it, and the controller has no vocabulary for
    "repaired" — whether a repair worked is the reviewer's judgment, carried by the
    VERIFY, not a controller edit to the FULL's claim. The faithfulness gate reports a
    dropped blocker and an invented one alike, so this list is derived, never authored.
    """
    return sorted(
        {
            finding["finding_id"]
            for review in reviews
            for finding in blocking_findings(review)
        }
    )


def digest_ref_of(ref: Mapping[str, Any], repo: pathlib.Path) -> dict[str, str]:
    """A candidate digestRef built from a state pointer, preferring the authored digest.

    A pointer that carries ``digest_sha256`` was authored by ``pointer_for`` on a
    digest-protected field — a binding the executor is not entitled to re-derive — so it
    is copied, never recomputed (FULL 71d43be F-1: recomputing over disk discarded the
    one binding digest in hand, and the candidate shown at FINAL could present a clean
    digest over a silently-rewritten WorkSpec). When the bytes in hand contradict that
    digest the assembly refuses: both sides are present right here, the one moment they
    can be reconciled without I/O (the M7 shape), and binding either side silently would
    record a file nobody authorized or a digest nothing on disk satisfies. A pointer
    without a digest names a file the executor may rewrite (the post-supersession-2
    narrowing), and its digest is computed over the bytes in hand — the same rule the
    check_result_refs below always used.
    """
    path = ref["path"]
    disk = bytes_digest((repo / path).read_bytes())
    authored = ref.get("digest_sha256")
    if authored is None:
        return {"path": path, "digest_sha256": disk}
    if authored != disk:
        raise AssuranceFault(
            f"state pointer for {path} binds digest {authored[:16]}… but the bytes in "
            f"hand digest {disk[:16]}… — the file changed after it was authored; "
            "re-resolve the run before binding"
        )
    return {"path": path, "digest_sha256": authored}


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("run_dir", type=pathlib.Path,
                        help="the run's control root, e.g. assurance/runs/<run-id>")
    parser.add_argument("--repo-root", type=pathlib.Path, default=None,
                        help="repository root; defaults to the git toplevel of the run directory (loud refusal outside a work tree)")
    # The SHA this run actually dispatched for review (printed by run_evidence_v2). For a
    # repaired run this is the ROUND-1 evidence commit — the repair regenerated everything
    # and committed anew, and the VERIFY answers that commit, never round 0's.
    parser.add_argument("--evidence-commit", required=True, metavar="SHA",
                        help="the 40-hex evidence commit this run dispatched for review")
    parser.add_argument("--bound-at", required=True, metavar="YYYY-MM-DD",
                        help="the date this binding is taken")
    parser.add_argument("--emit", action="store_true",
                        help="write the state transitions; without it the step only reports")
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
    RUN_ID = run_dir.name
    CONTROL = run_dir / "control"
    EVIDENCE = run_dir / "evidence"
    CONTROL_ROOT = run_dir.relative_to(REPO).as_posix()
    EXECUTOR = f"{RUN_ID} executor session"
    BOUND_BY = f"{RUN_ID} controller (rsclib deterministic)"
    EVIDENCE_COMMIT = args.evidence_commit
    BOUND_AT = args.bound_at

    # 0 while the FULL answers; 1 after a user-approved repair, when the targeted VERIFY
    # answers. Drives the review file set, the outcome gate, the state pointer and the
    # candidate's review_refs. Read from the state rather than mirrored from the evidence
    # step: a mirror is a second place for the round to be wrong.
    REPAIR_ROUND = assurance_state.load(CONTROL / "state.json")["repair_round"]

    names = round_documents(REPAIR_ROUND)
    missing = [name for name in names if not (EVIDENCE / name).is_file()]
    if missing:
        print(
            f"STOP: repair round {REPAIR_ROUND} binds {', '.join(names)}; "
            f"missing from evidence/: {', '.join(missing)}"
        )
        print(
            "      run the round's review first — a bind that reads only the FULL after "
            "a repair re-points the run at the round the repair answered"
        )
        return 1
    reviews = [load_json(EVIDENCE / name) for name in names]
    operative = reviews[-1]

    report = RV.check_review_result_v2(
        operative, REPO, evidence_commit=EVIDENCE_COMMIT, executor=EXECUTOR)
    print(f"check_review_result_v2 : {'clean' if report.ok else 'ISSUES'}")
    for issue in report.issues:
        print("  " + issue.render()[:160])
    if not report.ok:
        return 1

    if REPAIR_ROUND >= 1:
        repair = load_json(CONTROL / "user-decision-repair.json")
        outcome = flow.check_verify_outcome(operative, repair)
        print(f"check_verify_outcome   : {'clean' if outcome.ok else 'ISSUES'}")
        for issue in outcome.issues:
            print("  " + issue.render()[:160])
        if not outcome.ok:
            return 1

    binding = RS.subject_binding(EVIDENCE_COMMIT, operative)
    print(f"subject binding        : evidence_commit {binding['evidence_commit'][:12]}, "
          f"review digest {binding['review_digest'][:16]}")

    # A round-0 review that asks for changes does NOT bind an AssuranceCandidate. The
    # candidate is the thing a FINAL decision is taken against, and the flow leaves
    # AWAITING_FINAL only for CLOSED — so building one here would strand a run the user
    # chose to repair, with REPAIRING unreachable from where it stands. The transition this
    # round owes is REVIEWED, and the repair decision is the next act (`run_repair.py`).
    # p3-corr's round-0 bind stopped at REVIEWED for exactly this reason; this template
    # merged the candidate binding in and lost the branch, which p5b-claims found by walking
    # into it.
    blocked = REPAIR_ROUND == 0 and operative["verdict"] != "REVIEWED_NO_BLOCKER"
    if blocked:
        # The status is the same for both non-clean verdicts and the NEXT ACT is not, so the
        # sentence is branched where the transition is not. CHANGES_REQUIRED asks for a
        # bounded repair; SPEC_GAP says the specification is what failed, and EXECUTION.md's
        # "When the instruction itself is the problem" makes that a new WorkSpec revision and
        # a new user START decision — never a repair decision, which would name an act the
        # run does not owe and point the executor at a document nobody is going to author.
        # REVIEWED is right for both: STOPPED_REPLAN is reachable from every non-terminal
        # status (flow.py's explicit escape in the transition check), so neither strands.
        next_action = (
            "user decision on the SPEC_GAP: the specification is what failed, so a new "
            "WorkSpec revision and a new START decision are owed, not a bounded repair"
            if operative["verdict"] == "SPEC_GAP" else
            "user REPAIR decision (APPLY_ACCEPTED_FINDINGS / NO_REPAIR) naming the accepted "
            "finding ids and the repair boundary"
        )
        # The instruction is PRINTED, never paraphrased. `next_action` above is already
        # verdict-branched, and the sentence beside it used to restate it in different words
        # ("owes a repair decision") — a rewrite, not a copy, so the two diverged silently the
        # moment one of them learned about SPEC_GAP and the other did not, and without --emit
        # the paraphrase is the only output there is. Printing the field itself leaves the
        # property two landing points instead of three (rider sg-print, redeemed 2026-08-09).
        print(f"verdict                : {operative['verdict']} — no AssuranceCandidate is "
              "bound at round 0")
        print(f"next action            : {next_action}")
        if args.emit:
            state = assurance_state.load(CONTROL / "state.json")
            state = assurance_state.advance(
                state, "REVIEWED",
                review_ref=assurance_state.pointer_for(
                    "review_ref", f"{CONTROL_ROOT}/evidence/{names[-1]}", REPO),
                next_action=next_action,
            )
            assurance_state.save(state, CONTROL / "state.json")
            print(f"emitted                : {names[-1]} -> state REVIEWED "
                  "(review_ref = bytes digest via pointer_for)")
        return 0

    spec = load_json(CONTROL / "work-spec.json")
    record = load_json(EVIDENCE / "candidate-record.json")
    results = load_json(EVIDENCE / "check-results.json")
    state = assurance_state.load(CONTROL / "state.json")

    # Read only on the branch that binds a candidate — the blocked round-0 branch above
    # returns without one and owes no declarations. Absence refuses rather than defaults:
    # see DECLARATIONS at the top of this file for what each key is and why neither has one.
    declarations_path = run_dir / DECLARATIONS
    if not declarations_path.is_file():
        print(f"STOP: {DECLARATIONS} does not exist; the governance-scan state and the run's "
              "disclosures are declarations, not derivations")
        return 1
    declarations = load_json(declarations_path)
    absent = [key for key in ("governance_scan", "disclosures") if key not in declarations]
    if absent:
        print(f"STOP: {DECLARATIONS} carries no {', '.join(absent)}; "
              "this script supplies no default for either")
        return 1
    GOVERNANCE_SCAN = declarations["governance_scan"]
    DISCLOSURES = declarations["disclosures"]

    candidate = S.bind_candidate(
        assurance_candidate_id=f"ac-{RUN_ID}",
        work_id=spec["work_id"],
        run_id=RUN_ID,
        repair_round=REPAIR_ROUND,
        candidate_ref=record["candidate_ref"],
        base_revision=record["base_revision"],
        bound_by=BOUND_BY,
        work_spec_ref=digest_ref_of(state["work_spec_ref"], REPO),
        resolved_plan_ref=digest_ref_of(state["resolved_plan_ref"], REPO),
        instruction_audit_ref=digest_ref_of(state["instruction_audit_ref"], REPO),
        fulfillment_ref=digest_ref_of(state["fulfillment_ref"], REPO),
        manifest_ref=digest_ref_of(state["manifest_ref"], REPO),
        coverage_ref=digest_ref_of(state["coverage_ref"], REPO),
        review_refs=review_refs_of(names, reviews, CONTROL_ROOT),
        governance_scan=GOVERNANCE_SCAN,
        check_result_refs=[
            {
                "path": f"{CONTROL_ROOT}/evidence/check-{r['check_id']}.json",
                "digest_sha256": bytes_digest(
                    (EVIDENCE / f"check-{r['check_id']}.json").read_bytes()),
            }
            for r in results
        ],
        unresolved_finding_ids=unresolved_ids(reviews),
        disclosures=DISCLOSURES,
        bound_at=BOUND_AT,
    )
    cand_report = S.check_assurance_candidate(candidate, record, reviews)
    print(f"check_assurance_cand.  : {'clean' if cand_report.ok else 'ISSUES'}")
    for issue in cand_report.issues:
        print("  " + issue.render()[:160])
    if not cand_report.ok:
        return 1
    cand_digest = canonical_digest(candidate)
    print(f"candidate digest       : {cand_digest}")

    if args.emit:
        state = assurance_state.advance(
            state, "REVIEWED",
            review_ref=assurance_state.pointer_for(
                "review_ref", f"{CONTROL_ROOT}/evidence/{names[-1]}", REPO),
            next_action="controller binds the AssuranceCandidate for the FINAL decision",
        )
        assurance_state.save(state, CONTROL / "state.json")
        emitted = write_canonical(CONTROL / "assurance-candidate.json", candidate)
        state = assurance_state.advance(
            state, "AWAITING_FINAL",
            assurance_candidate_ref=assurance_state.pointer_for(
                "assurance_candidate_ref",
                f"{CONTROL_ROOT}/control/assurance-candidate.json", REPO),
            next_action="user FINAL decision (ACCEPT / ACCEPT_WITH_LIMITATIONS / REJECT / "
                        "REPLAN) binding the AssuranceCandidate digest; on ACCEPT the "
                        "promotion step is explicit and recorded",
        )
        assurance_state.save(state, CONTROL / "state.json")
        print(f"emitted                : {names[-1]} REVIEWED (review_ref = bytes digest "
              f"via pointer_for; digest-protected) -> assurance-candidate.json "
              f"({emitted[:16]}) -> state AWAITING_FINAL")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
