#!/usr/bin/env python3
"""TEMPLATE — evidence step, v2 shape: checks, manifest, record, coverage, EVIDENCE COMMIT.

Run in place from ``templates/run-v2/`` against the run directory — a run copies no step script
(`HD-11` part two, A2-R3) and there is no CONFIG block
to fill: the run directory and the round's revisions arrive as arguments, and the per-run
constants come from the run's own ``control/`` JSON. Differences from the w1-r1 evidence
step it descends from: no ReviewPackage is frozen. Instead, once the evidence layer is
clean, this script **commits the control plane** (an evidence commit staged as the explicit
control root, never ``git add -A``), builds the commit-bound subject, and verifies it with
``check_subject``. The value it prints last — the evidence commit SHA — is the entire
review handoff.

State pointers are written with ``pointer_for``, which decides per field whether a bytes
digest is written at all: the four this script sets are outside
``assurance_state.DIGEST_PROTECTED_FIELDS``, so they carry the path alone (2026-07-29
narrowing — this run authored those files and cannot bind itself by digesting them). The
per-CheckResult files are the derivation target ``check_subject`` re-enumerates from the
committed plan's ``check_order``.

The evidence commit's MESSAGE arrives as an argument and is used verbatim (item 4 of batch
``PROMISE-PATH``, round ``PROMISE-PATH-ENGINE``). It used to be a hard-coded one-line
f-string, so a title and a body the orchestrator is obliged to require -- ``E8``: a single
dense title naming the round, one dense paragraph, the commit's kind named so the review side
can attribute it without asking -- could not land on an evidence commit at all; the caller's
`2c6ed15` carries the template's own string and no tier declaration. What stays here is the
STRUCTURE, which is decidable without knowing anything about the run: a non-empty title, a
blank line under it, and a non-empty body. The words are the author's, and their absence is
refused rather than defaulted -- a message this script invented would be the executor's commit
described by somebody who was not there, the same reason ``fulfillment.json`` and
``bind-declarations.json`` carry no defaults either.

Run:  python -X utf8 run_evidence_v2.py <run-dir> --base <sha> --candidate <sha>
              --candidate-branch <branch>
              (--commit-message <text> | --commit-message-file <path>)
              [--repo-root <path>]
"""
from __future__ import annotations

import argparse
import glob
import json
import pathlib
import subprocess
import sys
from typing import Any, Mapping, Sequence

# __file__-based on purpose: this locates the co-located library, not run data (the run
# directory arrives as an argument).
HERE = pathlib.Path(__file__).resolve().parent
RS_ROOT = HERE.parents[2]
sys.path.insert(0, str(RS_ROOT / "tooling"))

from rsclib.document_harness import SpecGap, load_json  # noqa: E402
from rsclib.document_harness.caller import discover_repo_root  # noqa: E402
from rsclib.document_harness import assurance_state  # noqa: E402
from rsclib.document_harness import candidate as cand  # noqa: E402
from rsclib.document_harness import checks as C, review_subject as RS  # noqa: E402
from rsclib.document_harness import review as R  # noqa: E402
from rsclib.document_harness import views  # noqa: E402
from rsclib.document_harness.candidate import CandidateTreeReader  # noqa: E402
from rsclib.document_harness.spec import artifact_index  # noqa: E402


def build_claims(
    obligations: Sequence[Mapping[str, Any]],
    fulfillment: Mapping[str, Mapping[str, Any]],
) -> tuple[list[dict[str, Any]], list[str]]:
    """One claim per obligation, every status authored by a person — never supplied here.

    What this replaces wrote ``"status": "IMPLEMENTED"`` for every obligation inside a
    comprehension. That made unfinished work *unrepresentable*: a complete obligation list
    stamped every row done, so any enumeration built on it reported full implementation
    whatever the run had actually achieved, and no reviewer could see the difference. Status
    is therefore read from ``FULFILLMENT`` and never defaulted; an obligation the executor
    never answered for is returned as unfilled so the caller refuses the run before anything
    is written or committed.

    Entries are copied through verbatim rather than reshaped, which keeps
    ``candidate-record.schema.json`` the single place the per-status shape rules live — an
    entry that gets them wrong is refused by `check_record`'s schema pass, not by a second
    copy of the rules here.

    Claims follow WorkSpec order, not the map's: coverage rows join on the WorkSpec, and a
    map-ordered list would drift from them for no reason a reader could see.
    """
    claims: list[dict[str, Any]] = []
    unfilled: list[str] = []
    for obligation in obligations:
        obligation_id = obligation["obligation_id"]
        entry = fulfillment.get(obligation_id)
        if entry is None or "status" not in entry:
            unfilled.append(obligation_id)
            continue
        claims.append({"obligation_id": obligation_id, **entry})
    return claims, unfilled


def commit_control_plane(repo: pathlib.Path, control_root: str, message: str) -> None:
    """Stage the run's control root explicitly and commit it with the author's message.

    A function rather than two lines inside ``main`` so that "the message reaches git
    unedited" is a property a test can assert against a real repository, instead of one a
    reader has to take on the evidence of the source. What it does NOT do is the point: no
    run id prepended, no candidate SHA appended, no trailer. Both facts a generated suffix
    would carry are already bound by the commit it would ride on -- the staged control plane
    holds the run's state and the CandidateRecord names the candidate -- so appending them
    would restate evidence in the one place ``E8`` asks for prose, and would make the
    committed message not the message the author wrote.

    ``add`` names the control root explicitly and never ``-A`` (supersession-1 S2/S4;
    operating contract rule 7).
    """
    subprocess.run(["git", "-C", str(repo), "add", control_root], check=True)
    subprocess.run(["git", "-C", str(repo), "commit", "-m", message], check=True)


def commit_message_fault(message: str) -> str | None:
    """The one thing this script may still decide about the message: its shape.

    Returns the sentence naming the fault, or None. Three rules, each decidable without
    knowing the round, the kind or the run: a title, a blank line, a body. They are the
    structure ``E8`` needs in order to be met -- a title and one dense paragraph cannot be
    told apart from a one-line string without them -- and they are the whole of what is
    checked here. Whether the title names the round and whether the body names the commit's
    kind are judgments about content, and a template that scored them would be grading the
    author against a vocabulary this instrument does not own.
    """
    lines = message.split("\n")
    if not lines[0].strip():
        return "the message has no title: the first line is empty"
    if len(lines) < 3:
        return ("the message is a title and nothing else; E8 asks for a title AND one dense "
                "paragraph naming the commit's kind")
    if lines[1].strip():
        return ("the second line is not blank, so the title and the body are one paragraph; "
                "git reads the first line as the subject and everything after the blank line "
                "as the body")
    if not "\n".join(lines[2:]).strip():
        return "the message has a title and a blank line but no body"
    return None


def next_action_for(repair_round: int) -> str:
    """Which review the evidenced state asks for — round-dependent by construction.

    The normal sequence is one FULL, then, if the user approves a bounded repair, one
    targeted VERIFY of that repair (contract §8). A round-blind string instructs a cold
    session to open a SECOND FULL after a repair — the round-renaming shape the operating
    contract exists to prevent, reached by accident. This is the instruction, not a label:
    ``dtw status`` prints it verbatim as the cold-resume action, and nothing mechanical
    relates it to the round, so ``dtw flow`` still reports consistent. Witnessed on
    p3-corr as VERIFY finding v2 (issue-p3-corr-template-next-action-round-blind, routed
    WORKFLOW_FIX 2026-07-25).
    """
    if repair_round == 0:
        return ("user routes one FULL review of the evidence commit SHA to a "
                "fresh-context reviewer")
    return ("user routes one targeted VERIFY of the evidence commit SHA to a fresh-context "
            "reviewer; the VERIFY checks the accepted findings, the entire repair diff and "
            "the permanent boundaries")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("run_dir", type=pathlib.Path,
                        help="the run's control root, e.g. assurance/runs/<run-id>")
    parser.add_argument("--repo-root", type=pathlib.Path, default=None,
                        help="repository root; defaults to the git toplevel of the run directory (loud refusal outside a work tree)")
    # Not read from control/: no pre-evidence control document carries them. The WorkSpec's
    # `inputs` pin the revisions of the INPUT FILES, which is a different fact from the base
    # this run's diff is observed against.
    parser.add_argument("--base", required=True, metavar="SHA",
                        help="the 40-hex base revision the candidate is rooted at")
    parser.add_argument("--candidate", required=True, metavar="SHA",
                        help="the 40-hex payload candidate commit this round evidences")
    parser.add_argument("--candidate-branch", required=True, metavar="BRANCH",
                        help="the isolated branch the payload candidate lives on")
    # Not `required=True` on a mutually exclusive group: argparse answers a missing required
    # argument with SystemExit(2) and a usage block, and this script's refusals are exit 1
    # with a sentence saying what to write. The absence is checked below with the others.
    parser.add_argument("--commit-message", metavar="TEXT",
                        help="the evidence commit's message, used verbatim (title, blank "
                             "line, body); mutually exclusive with --commit-message-file")
    parser.add_argument("--commit-message-file", type=pathlib.Path, metavar="PATH",
                        help="a file holding that message; the usual form, since a body is "
                             "a paragraph and a shell argument is not")
    args = parser.parse_args(argv)

    # Refused FIRST, before the run directory is even resolved: the checks below take minutes
    # and the evidence commit is irreversible, so the cheapest refusal goes at the front. The
    # script supplies no message and no fallback text (item 4) -- only the structure rules.
    if (args.commit_message is None) == (args.commit_message_file is None):
        print("STOP: supply the evidence commit's message with exactly one of "
              "--commit-message or --commit-message-file")
        print("      E8: a single dense title naming the round, then one dense paragraph "
              "naming the commit's kind; this script supplies neither")
        return 1
    if args.commit_message_file is not None:
        if not args.commit_message_file.is_file():
            print(f"STOP: --commit-message-file names {args.commit_message_file}, "
                  "which does not exist")
            return 1
        COMMIT_MESSAGE = args.commit_message_file.read_text(encoding="utf-8")
    else:
        COMMIT_MESSAGE = args.commit_message
    fault = commit_message_fault(COMMIT_MESSAGE)
    if fault is not None:
        print(f"STOP: the evidence commit message is malformed — {fault}")
        return 1

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
    VERIFIER = f"{RUN_ID} deterministic verifier (rsclib)"
    DIFF_VERIFIER = f"{RUN_ID} diff verifier (rsclib deterministic)"
    BASE = args.base
    CANDIDATE = args.candidate
    CANDIDATE_BRANCH = args.candidate_branch

    spec = load_json(CONTROL / "work-spec.json")
    plan = load_json(CONTROL / "resolved-plan.json")
    # 0 for the first evidence layer; 1 after a user-approved repair produced C2. Every
    # evidence document is regenerated against the round's candidate, and the round drives
    # which review the state then asks for — see `next_action_for` below. It is read from the
    # state, where the schema requires it, so there is no default to fall back on and no
    # second copy of the round to drift from the one the flow advanced.
    REPAIR_ROUND = assurance_state.load(CONTROL / "state.json")["repair_round"]
    # Executor fulfillment — ONE ENTRY PER OBLIGATION_ID, each written by the person who did
    # the work. There is no default and no derived status: an obligation absent from this map,
    # or present without a `status`, refuses the run (`build_claims` above). The two shapes are
    # the schema's (candidate-record.schema.json `$defs.fulfillmentClaim`), not this file's:
    #
    #   "<obligation-id>": {"status": "IMPLEMENTED",
    #                       "implementation_locators": [{"path": ..., "anchor": ...}, ...]}
    #   "<obligation-id>": {"status": "NOT_IMPLEMENTED", "note": "<why, at least 8 chars>"}
    #
    # IMPLEMENTED requires locators that each resolve uniquely in the candidate commit;
    # NOT_IMPLEMENTED requires the note and forbids locators. An absent file is not an empty
    # map with a shrug — it takes the same refusal below, naming every obligation.
    fulfillment_path = CONTROL / "fulfillment.json"
    FULFILLMENT: dict[str, dict[str, Any]] = (
        load_json(fulfillment_path) if fulfillment_path.is_file() else {})
    candidate_ref = {"branch": CANDIDATE_BRANCH, "commit": CANDIDATE}

    # Refused here, at the top: the checks below take minutes and the evidence commit is
    # irreversible, so an unanswered obligation should cost neither. The evidence directory
    # is created AFTER this point, not before — creating it first left the one thing on disk
    # that made "refused before anything is written" true of documents and false of the
    # directory (FULL a918e37..7572abd, F2).
    claims, unfilled = build_claims(spec["obligations"], FULFILLMENT)
    if unfilled:
        print("STOP: no explicit fulfillment status for: " + ", ".join(unfilled))
        print("      fill control/fulfillment.json for each — this script supplies no "
              "default status")
        return 1

    # The bind step's hand-authored declarations, checked HERE because here is before the
    # evidence commit and therefore before the independent review reads those bytes. The bind
    # is where they are used and it checks them again; the bind is also the last step of the
    # round, so a defect first reported there costs a correction to a document the reviewer
    # has already read (round `PROMISE-PATH-ENGINE`, batch `PROMISE-PATH` item 6). Absence is
    # not refused here and is refused at the bind: `governance_scan.result_ref` names a
    # CheckResult this step has not written yet, so a run that authors the file after the
    # evidence layer is legitimate, while one that has already authored it gets the caps now.
    declarations_path = CONTROL / "bind-declarations.json"
    if declarations_path.is_file():
        decl_report = R.validate_n2("bind_declarations", load_json(declarations_path))
        print(f"bind declarations    : {'clean' if decl_report.ok else 'ISSUES'}")
        for issue in decl_report.issues:
            print("  " + issue.render()[:160])
        if not decl_report.ok:
            print("STOP: control/bind-declarations.json is not a valid BindDeclarations "
                  "document — nothing committed, state not advanced")
            return 1
    else:
        print("bind declarations    : absent (the bind step refuses it there; "
              "it may be authored after this step)")

    EVIDENCE.mkdir(parents=True, exist_ok=True)
    ctx = C.CheckContext(
        repo_root=REPO, candidate_ref=candidate_ref, base_revision=BASE,
        boundary=plan["effective_change_boundary"], verified_by=VERIFIER,
        artifact_paths=artifact_index(spec), evidence_dir=f"{CONTROL_ROOT}/evidence",
    )
    # The plan's `check_order` is the order, and `run_all` is the engine (`HD-25`). What this
    # replaces walked `sorted(glob(...))` and ran every request to completion, so a `SPEC_GAP`
    # — the ruling that a check request is uninterpretable — was collected and printed while
    # every later check still ran, `command_exit` among them, which starts a real process
    # against real files under a plan already known to be unreadable. `run_all` stops at the
    # first one instead; stopping late is not a slower stop, it is a different thing happening.
    #
    # Two consequences of taking the order from the plan rather than from the filenames, both
    # deliberate: the plan is authoritative, so a `check-chk-*.json` the plan does not order no
    # longer runs (it produced a result file nothing required — `check_subject` re-derives the
    # expected set from `check_order`); and a request the plan orders but the control root
    # lacks is now a `SPEC_GAP` at that point in the order, not a silently shorter run.
    # A malformed request with no `check_id` lands under a key no order entry names, so it is
    # unreachable and the entry that wanted it reports missing — fail-closed, not fail-open.
    # `.get` and not `plan["check_order"]`: the field is OPTIONAL in
    # `resolved-assurance-plan.schema.json` — "absent when the run has no deterministic
    # checks" — so subscripting it would crash exactly the runs the schema says are legal.
    # Empty order therefore means zero checks, which is also what `check_subject` concludes
    # from the same field; the two agree by reading one place rather than by two rules.
    requests: dict[str, Any] = {}
    for path in sorted(glob.glob(str(CONTROL / "check-chk-*.json"))):
        document = load_json(path)
        requests[document.get("check_id")] = document
    try:
        results = C.run_all(requests, plan.get("check_order", []), ctx)
    except SpecGap as gap:
        print(f"STOP: {gap}")
        print("      the check request is uninterpretable, so nothing after it ran; "
              "nothing committed, state not advanced")
        return 1
    passed = sum(1 for r in results if r["result"] == "PASS")
    print(f"deterministic checks : {passed}/{len(results)} PASS")
    for r in results:
        if r["result"] != "PASS":
            print(f"  !! {r['check_id']}: {r['result']} — {(r.get('detail') or '')[:100]}")

    manifest = cand.observe_manifest(
        REPO, BASE, CANDIDATE, plan["effective_change_boundary"], spec["expected_artifacts"],
        authored_by=DIFF_VERIFIER,
    )
    print(f"manifest             : {len(manifest.get('changes', []))} observed changes, "
          f"boundary {manifest['boundary_result']}")

    record = cand.build_record(
        record_id=f"rec-{RUN_ID}-r{REPAIR_ROUND}", work_id=spec["work_id"], run_id=RUN_ID,
        repair_round=REPAIR_ROUND, candidate_ref=candidate_ref, base_revision=BASE,
        control_root=CONTROL_ROOT,
        fulfillment={"authored_by": EXECUTOR, "claims": claims},
        manifest=manifest,
    )

    ok = True
    for label, report in (
        ("check_record", cand.check_record(record, spec)),
        ("check_locators", cand.check_locators(record, CandidateTreeReader(REPO, CANDIDATE))),
        ("coverage_report", views.coverage_report(spec, record, results)),
    ):
        print(f"{label:21}: {'clean' if report.ok else str(len(report.issues)) + ' ISSUE(S)'}")
        ok = ok and report.ok
        for issue in report.issues:
            print("  " + issue.render()[:160])

    # newline="\n" is load-bearing on Windows, not cosmetic: the default translates "\n" to
    # "\r\n" on write, while git (with core.autocrlf=true) stores LF — so the committed bytes
    # would differ from the bytes these state pointers digest, and check_subject would report
    # every evidence pointer STALE. write_canonical is immune because it writes bytes
    # directly; these write_text calls are not. Witnessed on p3-corr, whose first evidence
    # commit was correctly refused with four POINTER-STALE issues
    # (issue-p3-corr-template-write-text-newline, routed WORKFLOW_FIX 2026-07-25).
    (EVIDENCE / "check-results.json").write_text(
        json.dumps(results, indent=1), encoding="utf-8", newline="\n")
    # One file per CheckResult — load-bearing: check_subject re-derives the expected set
    # from the committed plan's check_order and requires exactly these paths.
    for r in results:
        (EVIDENCE / f"check-{r['check_id']}.json").write_text(
            json.dumps(r, indent=1), encoding="utf-8", newline="\n")
    (EVIDENCE / "candidate-record.json").write_text(
        json.dumps(record, indent=1), encoding="utf-8", newline="\n")
    (EVIDENCE / "coverage.json").write_text(
        json.dumps(views.coverage_document(spec, record, results), indent=1),
        encoding="utf-8", newline="\n")
    print(views.render_coverage(views.coverage_rows(spec, record, results)))
    if not ok or passed != len(results) or manifest["boundary_result"] != "CONFORMANT":
        print("STOP: evidence not clean — nothing committed, state not advanced")
        return 1

    state = assurance_state.load(CONTROL / "state.json")
    state = assurance_state.advance(
        state, "EVIDENCED",
        fulfillment_ref=assurance_state.pointer_for(
            "fulfillment_ref", f"{CONTROL_ROOT}/evidence/candidate-record.json", REPO),
        manifest_ref=assurance_state.pointer_for(
            "manifest_ref", f"{CONTROL_ROOT}/evidence/candidate-record.json", REPO),
        check_results_ref=assurance_state.pointer_for(
            "check_results_ref", f"{CONTROL_ROOT}/evidence/check-results.json", REPO),
        coverage_ref=assurance_state.pointer_for(
            "coverage_ref", f"{CONTROL_ROOT}/evidence/coverage.json", REPO),
        # The round is a STATE field, not only a sentence in `next_action`. `dispatch.role_for`
        # reads `state["repair_round"]` to decide FULL versus the targeted VERIFY, while the
        # subject it builds beside it reads the CandidateRecord — so a state left at 0 after a
        # repair makes one dispatch carry a round-1 subject under a FULL role, and a cold
        # session opens a second FULL of a repaired candidate. That is the round-renaming shape
        # `next_action_for` below already documents; this template had fixed the string and left
        # the field it is derived from behind. Witnessed on p5b-claims round 1, the first
        # repaired run to reach `dtw dispatch` (p3-corr's VERIFY predates the generator).
        repair_round=REPAIR_ROUND,
        next_action=next_action_for(REPAIR_ROUND),
    )
    assurance_state.save(state, CONTROL / "state.json")
    print("state                : EVIDENCED")

    # --- the evidence commit: stage the explicit control root, commit, verify ---
    # (supersession-1 S2/S4; operating contract rule 7 — explicit paths, no add -A)
    commit_control_plane(REPO, CONTROL_ROOT, COMMIT_MESSAGE)
    evidence_commit = cand.head_revision(REPO)

    subject = RS.subject_of(
        evidence_commit=evidence_commit, candidate_ref=candidate_ref,
        base_revision=BASE, control_root=CONTROL_ROOT, repair_round=REPAIR_ROUND,
    )
    report = RS.check_subject(subject, REPO)
    print(f"check_subject        : {'clean' if report.ok else str(len(report.issues)) + ' ISSUE(S)'}")
    for issue in report.issues:
        print("  " + issue.render()[:160])
    if not report.ok:
        print("STOP: the evidence commit is not a dispatchable subject — fix, commit again "
              "(a NEW commit, never amend), re-run")
        return 1

    print(f"REVIEW SUBJECT (dispatch this SHA and nothing else): {evidence_commit}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
