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

A second branch stops at the same place for the opposite verdict, and is item 3 of batch
``PROMISE-PATH`` (round ``PROMISE-PATH-ENGINE``, 2026-09-02). ``RULES.md`` ``R10`` says a
FULL returning ``REVIEWED_NO_BLOCKER`` **with lows** does not bank them by default: the
spend-the-fix-leg / bank choice is put to the user, and a late activation is still that
round's one approved fix. This step used to advance REVIEWED, write the candidate and
advance AWAITING_FINAL in one act, and ``flow._SUCCESSORS`` gives AWAITING_FINAL exactly one
successor -- so the choice ``R10`` orders never got a moment to be put, and the caller's run
p5c-firewall-r2 stopped exactly there: a clean FULL, three findings accepted for repair, and
the decision could not be executed. Now a clean round-0 FULL carrying non-blocking findings
stops at REVIEWED until the user's REPAIR decision is on disk, and the candidate plus
AWAITING_FINAL are a **separate act** that only a recorded ``NO_REPAIR`` -- the choice not to
spend the leg -- reaches. A clean FULL with no findings at all skips the stop: ``R10``'s
trigger is the lows, and a decision point with nothing to decide is ceremony. Nothing about
the banked lows is written into the candidate: a disclosure is a declaration with a source
(V3-D5), the bound FULL already carries the findings, and a controller-authored line about
them would be the controller speaking in its own voice.

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
from rsclib.document_harness import review as R  # noqa: E402
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
#:
#: Since round `PROMISE-PATH-ENGINE` the file is read through three gates rather than one, and
#: they answer different questions: it exists (absence is refused, and neither key is
#: defaulted), it is a valid BindDeclarations document (item 6 -- the schema, which is also
#: run one step earlier by `run_evidence_v2`), and every digest it declares matches the bytes
#: it names (item 5 -- `declared_ref_faults` below).
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


def declared_ref_faults(
    declarations: Mapping[str, Any], repo: pathlib.Path
) -> list[str]:
    """Every authored digest in the declarations, recomputed against the bytes it names.

    Item 5 of batch `PROMISE-PATH`. The bind copies ``governance_scan`` -- ``result_ref``
    and its ``digest_sha256`` included -- verbatim into the AssuranceCandidate it assembles,
    and nothing recomputed it: at the caller's `2c6ed15` the candidate declared a round-0
    digest for a file whose bytes had changed, and every later reader saw a candidate stating
    what was scanned. A digest nobody checks certifies nothing, and this is the one moment
    the declared digest and the bytes are both in hand -- the same M7 shape ``digest_ref_of``
    answers for state pointers.

    The CLASS and not the reported instance (`E7`): ``disclosures[].source_ref`` is the same
    thing, a hand-authored ``digestRef`` copied straight into the candidate, and its
    consequence is worse -- a disclosure exists to name the owner-authored document it came
    from, so a source_ref that binds nothing turns "what the user should know before
    deciding" into an unsourced sentence, which is exactly what ``assurance.schema.json``
    makes the field required to prevent. Both are checked here; the schema (item 6) has
    already established that every ref present is a ``digestRef`` with both keys.

    Returns one sentence per fault rather than raising, so a run with several stale
    declarations sees all of them in one pass instead of one per re-run. An absent file is a
    fault of its own: a ref to bytes that are not there is not a weaker binding, it is none.
    """
    faults: list[str] = []
    scan = declarations["governance_scan"]
    refs = [("governance_scan/result_ref", scan["result_ref"])] if scan.get("result_ref") else []
    refs += [
        (f"disclosures/{index}/source_ref", entry["source_ref"])
        for index, entry in enumerate(declarations["disclosures"])
    ]
    for where, ref in refs:
        target = repo / ref["path"]
        if not target.is_file():
            faults.append(f"{where} names {ref['path']}, which does not exist")
            continue
        observed = bytes_digest(target.read_bytes())
        if observed != ref["digest_sha256"]:
            faults.append(
                f"{where} declares digest {ref['digest_sha256'][:16]}… for {ref['path']} "
                f"but its bytes digest {observed[:16]}…"
            )
    return faults


def emit_reviewed(
    state: Mapping[str, Any],
    *,
    control_path: pathlib.Path,
    review_path: str,
    repo: pathlib.Path,
    next_action: str,
) -> bool:
    """Advance the state to REVIEWED, binding this round's review by bytes, and save.

    Returns whether it advanced, which is not decoration: already-REVIEWED is a **no-op**
    rather than a self-transition, because the R10 branch below is reached a second time by
    the run that returns with the user's decision in hand, and REVIEWED -> REVIEWED is not a
    legal successor (``flow._SUCCESSORS``). ``assurance_state.advance`` does not check
    legality, so without the no-op that illegal transition would be written with nothing to
    show for it -- the same status, the same pointer, no visible difference. The return value
    is what gives the no-op a consequence a test can hold: the caller says on stdout which of
    the two passes this is, so deleting the no-op changes the output.

    Both stopping branches land here and the candidate act passes through it, so the
    transition is written once rather than three times -- the copy-class fork rider
    ``decl-dup`` names that shape.
    """
    if state["status"] == "REVIEWED":
        return False
    advanced = assurance_state.advance(
        state, "REVIEWED",
        review_ref=assurance_state.pointer_for("review_ref", review_path, repo),
        next_action=next_action,
    )
    assurance_state.save(advanced, control_path)
    return True


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
            emit_reviewed(
                assurance_state.load(CONTROL / "state.json"),
                control_path=CONTROL / "state.json",
                review_path=f"{CONTROL_ROOT}/evidence/{names[-1]}",
                repo=REPO,
                next_action=next_action,
            )
            print(f"emitted                : {names[-1]} -> state REVIEWED "
                  "(review_ref = bytes digest via pointer_for)")
        return 0

    # --- R10: a clean FULL carrying lows is a DECISION POINT, not a green light ---------
    #
    # See the module docstring. The vocabulary is R10's: "lows" are the reviewer's
    # non-blocking findings, read from the operative review rather than counted anywhere
    # else, so the trigger is the reviewer's own claim. At round 1 there is no leg left to
    # spend, so the stop is round-0's alone.
    lows = [
        finding["finding_id"]
        for finding in operative.get("findings", [])
        if not finding["blocking"]
    ]
    if REPAIR_ROUND == 0 and lows:
        decision_path = CONTROL / "user-decision-repair.json"
        r10_action = (
            "user REPAIR decision on the non-blocking findings "
            f"({', '.join(lows)}): APPLY_ACCEPTED_FINDINGS spends this round's one repair "
            "leg on them and NO_REPAIR banks them; the AssuranceCandidate is bound only "
            "after that decision is on disk"
        )
        print(f"verdict                : REVIEWED_NO_BLOCKER with {len(lows)} non-blocking "
              f"finding(s): {', '.join(lows)}")
        if not decision_path.is_file():
            # The instruction is PRINTED and STORED as one string, never paraphrased into a
            # second sentence beside it (rider `sg-print`: two rewrites of one fact diverge
            # silently, where a copy diverges visibly).
            print(f"next action            : {r10_action}")
            if args.emit:
                emit_reviewed(
                    assurance_state.load(CONTROL / "state.json"),
                    control_path=CONTROL / "state.json",
                    review_path=f"{CONTROL_ROOT}/evidence/{names[-1]}",
                    repo=REPO,
                    next_action=r10_action,
                )
                print(f"emitted                : {names[-1]} -> state REVIEWED "
                      "(review_ref = bytes digest via pointer_for)")
            return 0

        # The decision is READ, never authored here (every UserDecision is the user's), and
        # it is gated by the same function `run_repair.py` gates the other branch with: a
        # NO_REPAIR naming another run's review would close this run's repair phase on a
        # decision the user made about something else (defect M5), and this is the only step
        # a NO_REPAIR ever reaches -- `run_repair.py` exists for the APPLY path.
        r10_decision = load_json(decision_path)
        r10_plan = load_json(CONTROL / "resolved-plan.json")
        r10_report = flow.check_repair_decision(r10_decision, operative, r10_plan)
        print(f"check_repair_decision  : {'clean' if r10_report.ok else 'ISSUES'}")
        for issue in r10_report.issues:
            print("  " + issue.render()[:160])
        if not r10_report.ok:
            return 1
        if r10_decision["decision"] != "NO_REPAIR":
            spend_action = (
                "user chose to spend the repair leg on the non-blocking findings; the next "
                "act is run_repair.py, which gates the decision and enters REPAIRING"
            )
            print(f"lows decision          : {r10_decision['decision']} — the leg is spent")
            print(f"next action            : {spend_action}")
            if args.emit:
                emit_reviewed(
                    assurance_state.load(CONTROL / "state.json"),
                    control_path=CONTROL / "state.json",
                    review_path=f"{CONTROL_ROOT}/evidence/{names[-1]}",
                    repo=REPO,
                    next_action=spend_action,
                )
                print(f"emitted                : {names[-1]} -> state REVIEWED "
                      "(review_ref = bytes digest via pointer_for)")
            return 0
        print("lows decision          : NO_REPAIR — the user banked the low(s); this bind "
              "binds the AssuranceCandidate")

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
    # The whole document against its own schema, not the two key names. Key presence was all
    # this step could check while nothing under `schema/` named the file (round
    # `PROMISE-PATH-ENGINE`, item 6): a disclosure over the candidate's 500-character cap
    # passed here and was refused later by `check_assurance_candidate`, after the independent
    # review had read those bytes. The schema is the same cap by reference, so the two cannot
    # disagree, and the evidence step now runs this check before the commit as well -- this
    # one stays because the file may be edited between the two.
    decl_report = R.validate_n2("bind_declarations", declarations)
    if not decl_report.ok:
        print(f"STOP: {DECLARATIONS} is not a valid BindDeclarations document; "
              "the governance-scan state and the run's disclosures are declarations, and "
              "this script supplies no default for either")
        for issue in decl_report.issues:
            print("  " + issue.render()[:160])
        return 1
    # The digests the declarations carry are recomputed here, before any of them is copied
    # into the candidate. See `declared_ref_faults` for what this closes and why the
    # disclosure refs are in it too.
    faults = declared_ref_faults(declarations, REPO)
    print(f"declared digests       : {'verified' if not faults else 'STALE'}")
    for fault in faults:
        print("  " + fault)
    if faults:
        print(f"STOP: {DECLARATIONS} binds bytes it does not match; a digest nobody checks "
              "certifies nothing, and re-declaring it is the run's act, not this script's")
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
        if not emit_reviewed(
            state,
            control_path=CONTROL / "state.json",
            review_path=f"{CONTROL_ROOT}/evidence/{names[-1]}",
            repo=REPO,
            next_action="controller binds the AssuranceCandidate for the FINAL decision",
        ):
            print("state                  : already REVIEWED from the earlier pass; only "
                  "the AWAITING_FINAL transition is owed")
        # Re-read rather than carried forward: the helper above may have written a new state
        # or, on the second pass of the R10 branch, deliberately left the REVIEWED one it
        # found. Reading back is what makes the two paths converge on one document.
        state = assurance_state.load(CONTROL / "state.json")
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
