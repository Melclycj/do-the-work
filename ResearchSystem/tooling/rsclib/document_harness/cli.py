#!/usr/bin/env python3
"""The command line of the Document Work Assurance v3 harness.

Six read-only-by-default operations: `governance-scan` / `status` / `flow` / `dispatch` /
`disposition` / `review`. `dispatch` is the only one that writes anything (the freeze marker
`.harness/review-pending.json`, E9's review window).

They lived under `rsc.py v3 <op>` until the split batch's R2 moved them here: `rsc` is the
product compiler's name and stays with the caller, while these six travel with the instrument
(`HD-28`, split-design §1). The two entry scripts beside `rsc.py` — `do-the-work.py` and its
short alias `dtw.py` — are the same entry under the two names `HD-40` §10 recorded; both do
nothing but call `main()` below.

The command bodies below are the bytes that ran under `rsc v3`, moved without retyping; the
only edits are the parser's own plumbing (`v3_sub` -> `sub`, a `prog` of its own) and this
docstring.
"""
from __future__ import annotations

import argparse
import pathlib
import sys


def _cmd_v3_governance_scan(args: argparse.Namespace) -> int:
    """Reject a governance document that carries its own approval status (V3-N1, R4).

    Reached through the closed `command_exit` check kind rather than a seventh check kind,
    because the LocalCheckSpec union is frozen by the signed Contract v3 §5.
    """
    # Imported here rather than at module scope: the P2 compiler must stay usable even if
    # the v3 package is mid-change. (The v1 `stage` runtime was the other beneficiary until
    # `HD-39` deleted it.)
    from rsclib.document_harness import AssuranceFault, SpecGap
    from rsclib.document_harness import candidate as v3_candidate
    from rsclib.document_harness import checks as v3_checks

    repo_root = pathlib.Path(args.repo_root).resolve() if args.repo_root else pathlib.Path.cwd().resolve()
    try:
        if args.tree == "candidate_commit":
            if not args.revision:
                print("FATAL: --revision is required when scanning a candidate commit", file=sys.stderr)
                return 2
            reader = v3_candidate.CandidateTreeReader(repo_root, args.revision)
        else:
            reader = v3_candidate.WorktreeReader(repo_root)
        exemptions = v3_checks.load_exemptions(args.exemptions)
        scan = v3_checks.governance_scan(reader, args.path, exemptions)
    except SpecGap as exc:
        print(f"SPEC_GAP: {exc}", file=sys.stderr)
        return 2
    except AssuranceFault as exc:
        print(f"FATAL: {exc}", file=sys.stderr)
        return 2

    print("=" * 72)
    print(f"Document Work Assurance v3 — governance frontmatter scan ({reader.kind})")
    print("=" * 72)
    print(f"scanned  : {len(scan.scanned)} document(s)")
    print(f"exempted : {len(scan.exempted)} blob-keyed grandfather match(es)")
    for path in scan.exempted:
        print(f"  - {path}")
    for issue in scan.report.issues:
        print("  " + issue.render())
    print("-" * 72)
    print("RESULT: " + ("clean (exit 0)" if scan.report.ok else "findings (exit 1)"))
    return 0 if scan.report.ok else 1


def _cmd_v3_status(args: argparse.Namespace) -> int:
    """Cold resume: reconstruct a run's position from the state file and its pointers."""
    from rsclib.document_harness import AssuranceFault, SpecGap
    from rsclib.document_harness import assurance_state as v3_state

    repo_root = pathlib.Path(args.repo_root).resolve() if args.repo_root else pathlib.Path.cwd().resolve()
    try:
        point = v3_state.resume(args.state, repo_root)
    except (SpecGap, AssuranceFault) as exc:
        print(f"FATAL: {exc}", file=sys.stderr)
        return 2

    print("=" * 72)
    print("Document Work Assurance v3 — assurance work state")
    print("=" * 72)
    print(point.render())
    print("-" * 72)
    print("RESULT: " + ("resumable (exit 0)" if point.report.ok else "pointers unresolved (exit 1)"))
    return 0 if point.report.ok else 1


def _cmd_v3_flow(args: argparse.Namespace) -> int:
    """Where a run stands, and whether its status is backed by the pointers it implies.

    N1's `v3 status` answers "can this run be resumed"; this answers "is the position it
    claims a legal one". They are different questions: a run whose pointers all resolve can
    still be at `CLOSED` without a summary, which resume has no reason to notice.
    """
    from rsclib.document_harness import AssuranceFault, SpecGap
    from rsclib.document_harness import assurance_state as v3_state
    from rsclib.document_harness import flow as v3_flow

    try:
        state = v3_state.load(args.state)
        report = v3_flow.check_state_pointers(state)
        rendered = v3_flow.render_flow(state)
        transition = v3_flow.check_transition(state, args.next) if args.next else None
    except (SpecGap, AssuranceFault) as exc:
        print(f"FATAL: {exc}", file=sys.stderr)
        return 2

    print("=" * 72)
    print("Document Work Assurance v3 — flow position")
    print("=" * 72)
    print(rendered)
    for issue in report.issues:
        print("  " + issue.render())
    if transition is not None:
        verdict = "legal" if transition.ok else "REFUSED"
        print(f"-- proposed transition -> {args.next}: {verdict}")
        for issue in transition.issues:
            print("  " + issue.render())
    ok = report.ok and (transition is None or transition.ok)
    print("-" * 72)
    print("RESULT: " + ("consistent (exit 0)" if ok else "inconsistent (exit 1)"))
    return 0 if ok else 1


def _cmd_v3_dispatch(args: argparse.Namespace) -> int:
    """Derive a review dispatch from an evidence commit — the executor's cold entry.

    The mirror of `read_control_plane`, which lets a reviewer start from nothing but the
    SHA. Until this existed the executor side had no such entry, so every dispatch was
    hand-composed and its facts were the dispatcher's rather than the repository's
    (`issue-p3-corr-no-dispatch-generator`).

    A dispatch that could not be derived cleanly is still printed, with its issues, and
    exits 1: the dispatcher needs to see what is wrong more than they need a success.
    """
    from rsclib.document_harness import AssuranceFault, SpecGap
    from rsclib.document_harness import dispatch as v3_dispatch

    repo_root = pathlib.Path(args.repo_root).resolve() if args.repo_root else pathlib.Path.cwd().resolve()
    try:
        if args.range:
            # A CONSTRUCTION round: no control plane declares where it began, so the two
            # revisions bounding it are the one irreducible input — and, unlike the product
            # path, very nearly the only input. This half derives nothing but two resolved
            # SHAs; the reasoning for that lives in dispatch.py's construction section.
            base, sep, tip = args.range.partition("..")
            if not sep or not base or not tip:
                print(f"FATAL: --range takes BASE..TIP, got {args.range!r}", file=sys.stderr)
                return 2
            derived = v3_dispatch.construction_dispatch_of(repo_root, base, tip)
            render, render_derivation = (
                v3_dispatch.render_construction_dispatch,
                v3_dispatch.render_construction_derivation,
            )
        elif getattr(args, "read", None):
            # An E10 instruction-layer read: one commit, no control plane. The member set
            # is deliberately not derived here — E10's sentence owns it (dispatch.py's
            # read section).
            derived = v3_dispatch.read_dispatch_of(repo_root, args.read)
            render, render_derivation = (
                v3_dispatch.render_read_dispatch,
                v3_dispatch.render_read_derivation,
            )
        else:
            derived = v3_dispatch.dispatch_of(repo_root, args.subject)
            render, render_derivation = (
                v3_dispatch.render_dispatch,
                v3_dispatch.render_derivation,
            )
    except (SpecGap, AssuranceFault) as exc:
        print(f"FATAL: {exc}", file=sys.stderr)
        return 2

    # Two audiences, two streams. The derivation is the DISPATCHER's check that they are
    # routing the run they think they are; it goes to stderr so that stdout carries only what
    # the reviewer should see. Handing a reviewer pre-derived run facts is the anchoring this
    # command exists to remove; printing them to the human costs nothing.
    print(render_derivation(derived), file=sys.stderr)

    # Printed, never written. A dispatch is a startup PROMPT, not an artifact: it carries
    # only a pointer to the reviewer's charter and one SHA, so every fact in it is already
    # committed and persisting it would store a derived copy that can go stale against the
    # generator — which is exactly what happened when one was committed and then read back
    # after the generator had moved on. There is deliberately no --out; a caller who wants a
    # file can redirect stdout and owns the staleness that follows.
    #
    # The freeze marker below is STATE, not the prompt: a successful dispatch opens E9's
    # window (dispatch -> record commit, no other commit lands), and the tracked
    # `review_freeze_check.py` reads this file to hold that window mechanically. The
    # executor deletes it in the act that commits the returned record.
    # The marker records the SUBJECT and nothing about what kind of work it is. It used to
    # carry a `kind`, derived from which flag was typed rather than from what was dispatched,
    # so a product run forced onto `--range` was labelled "construction-round" (p5b-firewall,
    # issue-p5b-firewall-dispatch-types-product-run-as-construction). The field was deleted
    # rather than taught: nothing branches on it — `review_freeze_check.py` read it only to
    # print a display line — and `R2` forbids a reviewer trusting anything handed to them, so
    # a value no code consumes and no reviewer may rely on can only ever mislead. The subject
    # itself says which family it is: a `..` range, or one 40-hex commit.
    if derived.report.ok:
        import datetime
        import json as _json

        if args.range:
            subject = f"{derived.base}..{derived.tip}"
        elif getattr(args, "read", None):
            subject = derived.commit
        else:
            subject = derived.evidence_commit
        marker = repo_root / ".harness" / "review-pending.json"
        marker.parent.mkdir(parents=True, exist_ok=True)
        marker.write_text(
            _json.dumps(
                {
                    "subject": subject,
                    "dispatched_at": datetime.datetime.now(
                        datetime.timezone.utc
                    ).isoformat(timespec="seconds"),
                },
                indent=1,
            )
            + "\n",
            encoding="utf-8",
        )
        print(
            f"freeze marker written: {marker} — delete it in the act that commits the "
            "returned record",
            file=sys.stderr,
        )
    print(render(derived), end="")
    print(
        "RESULT: " + ("derived (exit 0)" if derived.report.ok else "NOT dispatchable (exit 1)"),
        file=sys.stderr,
    )
    return 0 if derived.report.ok else 1


def _cmd_v3_disposition(args: argparse.Namespace) -> int:
    """Render an AssuranceCandidate or AssuranceSummary, and state the governance obligation.

    The governance line is the point of this command rather than a detail of it: N1 made the
    scan mechanical but nothing obliged a run to invoke it, so a run that never called it
    produced no signal at all. Here a skipped scan is printed, with its reason.
    """
    from rsclib.document_harness import AssuranceFault, SpecGap
    from rsclib.document_harness import flow as v3_flow
    from rsclib.document_harness import summary as v3_summary
    from rsclib.document_harness.review import validate_n2

    try:
        document = v3_summary.load_candidate(args.document)
        kind = "assurance_summary" if "summary_id" in document else "assurance_candidate"
        report = validate_n2(kind, document)
    except (SpecGap, AssuranceFault) as exc:
        print(f"FATAL: {exc}", file=sys.stderr)
        return 2

    print("=" * 72)
    print(f"Document Work Assurance v3 — {kind.replace('_', ' ')}")
    print("=" * 72)
    if kind == "assurance_summary" and report.ok:
        print(v3_summary.render_summary(document))
    elif report.ok:
        obligation = v3_flow.check_governance_obligation(document)
        scan = document["governance_scan"]
        print(f"candidate    : {document['candidate_ref'].get('commit', '?')[:12]}")
        print(f"repair_round : {document['repair_round']}")
        print(
            "governance   : "
            + ("scan ran" if scan["included"] else f"NOT RUN — {scan['skip_reason']}")
        )
        for finding_id in document.get("unresolved_finding_ids", []):
            print(f"  !! unresolved blocking finding: {finding_id}")
        for entry in document.get("disclosures", []):
            print(f"  ?? {entry['statement']}")
        report = report + obligation
    for issue in report.issues:
        print("  " + issue.render())
    print("-" * 72)
    print("RESULT: " + ("well-formed (exit 0)" if report.ok else "defects (exit 1)"))
    return 0 if report.ok else 1


def _cmd_v3_review_subject(args: argparse.Namespace) -> int:
    """Check a commit-bound wave-2 review subject, and a v2 ReviewResult when supplied.

    The reviewer's counterpart to `v3 dispatch --subject`: that command asks whether a commit
    may be routed and which review it owes; this one asks whether the commit is a sound
    subject and whether a returned verdict answers for it. Until this existed the two wave-2
    checks had no caller outside a run script — `check_review_result_v2` had none at all — so
    a reviewer's own result could not be checked from the command line.

    Only the SHA is required (review side rule 2). The control root is derived from the
    commit's own staged paths and the rest is read back out of the committed control plane,
    REUSING `dispatch`'s derivation rather than keeping a second copy of it.

    Disclosed, deliberately not repaired here: with no `--result` the subject is rebuilt from
    the CandidateRecord it is then compared against, so four of `check_subject`'s five
    identity rows are self-comparisons. That is the shape `dispatch_of` and the run template
    already have; the record's `control_root` against the derived one stays a real
    comparison, and the completeness, freshness and containment halves are unaffected. With
    `--result` the subject checked is the reviewer's own document and the binding is
    independent by construction.
    """
    from rsclib.document_harness import AssuranceFault, SpecGap
    from rsclib.document_harness import dispatch as v3_dispatch
    from rsclib.document_harness import review as v3_review
    from rsclib.document_harness import review_result_v2 as v3_result_v2
    from rsclib.document_harness import review_subject as v3_subject

    # Refused rather than ignored: subject mode derives the check results from the commit, so
    # a caller who passes them has a different model of what is being checked than the command
    # does, and silently dropping the flag leaves that disagreement invisible.
    if args.check_result:
        print(
            "FATAL: --check-result belongs to --package mode; subject mode derives the check "
            "results from the evidence commit",
            file=sys.stderr,
        )
        return 2

    repo_root = pathlib.Path(args.repo_root).resolve() if args.repo_root else pathlib.Path.cwd().resolve()
    subject_checked = True
    try:
        evidence_commit, report = v3_dispatch.resolve_subject(repo_root, args.subject)
        control_root = None
        if evidence_commit is not None:
            control_root, root_report = v3_dispatch.control_root_of(repo_root, evidence_commit)
            report = report + root_report
        if evidence_commit is not None and control_root is not None:
            result = v3_review.load_result(args.result) if args.result else None
            if result is not None:
                # `check_review_result_v2` runs `check_subject` itself, on the REVIEWER's
                # subject document. Running the derived one as well would report the same
                # class of issue twice against two different documents.
                report = report + v3_result_v2.check_review_result_v2(
                    result, repo_root, evidence_commit=evidence_commit, executor=args.executor
                )
            else:
                plane = v3_subject.read_control_plane(repo_root, evidence_commit, control_root)
                report = report + plane.report
                record = plane.record or {}
                if record.get("candidate_ref") and record.get("base_revision") is not None:
                    report = report + v3_subject.check_subject(
                        v3_subject.subject_of(
                            evidence_commit=evidence_commit,
                            candidate_ref=record["candidate_ref"],
                            base_revision=record["base_revision"],
                            control_root=control_root,
                            repair_round=record.get("repair_round", 0),
                        ),
                        repo_root,
                    )
                else:
                    # No invented code: the plane report above already carries why the record
                    # could not be read, and this exits 1 either way. What would otherwise be
                    # missing is the disclosure that the check did not run, so say that.
                    subject_checked = False
    except (SpecGap, AssuranceFault) as exc:
        print(f"FATAL: {exc}", file=sys.stderr)
        return 2

    print("=" * 72)
    print("Document Work Assurance v3 — commit-bound review subject")
    print("=" * 72)
    # Printed in full, never abbreviated: `dispatch.resolve_subject` records why a shortened
    # commit is a weaker binding than the custody chain assumes, and a reviewer copying this
    # line into a record would be copying the weaker form.
    print(f"evidence commit : {evidence_commit or args.subject}")
    print(f"control root    : {control_root or '?'}")
    print(f"result checked  : {args.result or 'none supplied'}")
    if not subject_checked:
        print("  !! the CandidateRecord yielded no candidate_ref/base_revision, so this commit "
              "was NOT checked as a complete subject — an unverified property, not a passing one")
    for issue in report.issues:
        print("  " + issue.render())
    print("-" * 72)
    print("RESULT: " + ("sound subject (exit 0)" if report.ok else "defects (exit 1)"))
    return 0 if report.ok else 1


def _cmd_v3_review(args: argparse.Namespace) -> int:
    """Check a frozen ReviewPackage, and a ReviewResult when one is supplied.

    The package checks answer a question no schema can: is the frozen subject the *whole*
    work? Membership completeness is judged against the run's own spec and record, and the
    member digests are re-computed against the trees the members pin.
    """
    if args.subject:
        return _cmd_v3_review_subject(args)

    from rsclib.document_harness import AssuranceFault, SpecGap
    from rsclib.document_harness import review as v3_review
    from rsclib.document_harness import spec as v3_spec

    # `--spec` and `--record` stopped being argparse-required when `--subject` arrived, since
    # that mode needs neither. They are still required OF THIS MODE — enforced here so the
    # addition of a second mode could not quietly relax the first one's inputs.
    missing = [name for name in ("spec", "record") if not getattr(args, name)]
    if missing:
        print(
            "FATAL: --package mode requires " + " and ".join(f"--{name}" for name in missing),
            file=sys.stderr,
        )
        return 2

    repo_root = pathlib.Path(args.repo_root).resolve() if args.repo_root else pathlib.Path.cwd().resolve()
    try:
        package = v3_review.load_package(args.package)
        spec = v3_spec.load_spec(args.spec)
        record = v3_review.load_package(args.record)
        results = [v3_review.load_package(path) for path in (args.check_result or [])]
        report = v3_review.check_package(package, spec, record, results)
        # Byte verification walks `package["members"]`, which a schema-invalid package may not
        # have — running it anyway turned a document this command exists to REPORT on into a
        # traceback. The schema failure is the finding; there is nothing further to verify.
        well_formed = not any(issue.code.startswith("V3-SCHEMA-") for issue in report.issues)
        if well_formed:
            report = report + v3_review.verify_member_bytes(package, repo_root)
        result = v3_review.load_result(args.result) if args.result else None
        if result is not None and well_formed:
            report = report + v3_review.check_review_result(
                result, spec, package, executor=args.executor
            )
    except (SpecGap, AssuranceFault) as exc:
        print(f"FATAL: {exc}", file=sys.stderr)
        return 2

    print("=" * 72)
    print("Document Work Assurance v3 — frozen review subject")
    print("=" * 72)
    print(f"package      : {package.get('package_id', '?')} ({package.get('review_round', '?')})")
    print(f"candidate    : {str(package.get('candidate_ref', {}).get('commit', '?'))[:12]}")
    print(f"members      : {len(package.get('members', []))}")
    if result is not None:
        print("-" * 72)
        print(v3_review.render_result(result))
    for issue in report.issues:
        print("  " + issue.render())
    print("-" * 72)
    print("RESULT: " + ("sound subject (exit 0)" if report.ok else "defects (exit 1)"))
    return 0 if report.ok else 1

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="do-the-work",
        description="Document Work Assurance v3 — the harness's own command line",
    )
    sub = p.add_subparsers(dest="operation", required=True)

    gov = sub.add_parser(
        "governance-scan",
        help="reject a governance document that carries its own approval status",
    )
    gov.add_argument("--path", action="append", required=True, help="repo-relative document (repeatable)")
    gov.add_argument("--exemptions", help="blob-keyed grandfather register (JSON)")
    gov.add_argument("--repo-root", help="repository root (default: current directory)")
    gov.add_argument(
        "--tree",
        choices=["worktree", "candidate_commit"],
        default="worktree",
        help="which tree to observe; recorded so a result never hides its subject",
    )
    gov.add_argument("--revision", help="exact commit when --tree candidate_commit")
    gov.set_defaults(func=_cmd_v3_governance_scan)

    status = sub.add_parser("status", help="cold resume from an AssuranceWorkState")
    status.add_argument("--state", required=True, help="path to the AssuranceWorkState document")
    status.add_argument("--repo-root", help="repository root (default: current directory)")
    status.set_defaults(func=_cmd_v3_status)

    # V3-N2 read-only surfaces. A check nobody can invoke is a check that will eventually
    # not be run, which is exactly the residual N1 carried forward (N1-R2).
    flow_cmd = sub.add_parser(
        "flow", help="flow position: are the status and its required pointers consistent?"
    )
    flow_cmd.add_argument("--state", required=True, help="path to the AssuranceWorkState document")
    flow_cmd.add_argument("--next", help="optional proposed next status, checked for legality")
    flow_cmd.set_defaults(func=_cmd_v3_flow)

    dispatch_cmd = sub.add_parser(
        "dispatch",
        help="derive a review dispatch from an evidence commit (the executor's cold entry)",
    )
    dispatch_mode = dispatch_cmd.add_mutually_exclusive_group(required=True)
    dispatch_mode.add_argument(
        "--subject", help="PRODUCT run: the evidence commit — the only input needed"
    )
    dispatch_mode.add_argument(
        "--range",
        help="CONSTRUCTION round: BASE..TIP, the one thing no control plane records",
    )
    dispatch_mode.add_argument(
        "--read",
        help="E10 layer read: the commit whose instruction layer is the subject",
    )
    dispatch_cmd.add_argument("--repo-root", help="repository root (default: current directory)")
    dispatch_cmd.set_defaults(func=_cmd_v3_dispatch)

    disposition = sub.add_parser(
        "disposition",
        help="render an AssuranceCandidate or AssuranceSummary and state the governance obligation",
    )
    disposition.add_argument(
        "--document", required=True, help="path to the AssuranceCandidate or AssuranceSummary"
    )
    disposition.set_defaults(func=_cmd_v3_disposition)

    review_cmd = sub.add_parser(
        "review",
        help="check a review subject: a wave-2 evidence commit, or a frozen v1 ReviewPackage",
    )
    review_mode = review_cmd.add_mutually_exclusive_group(required=True)
    review_mode.add_argument(
        "--subject",
        help="WAVE 2: the evidence commit — the only input needed; add --result to check a "
             "returned v2 ReviewResult against it",
    )
    review_mode.add_argument(
        "--package", help="VERSION 1: path to the frozen ReviewPackage (needs --spec/--record)"
    )
    review_cmd.add_argument("--spec", help="v1 mode only: path to the DocumentWorkSpec")
    review_cmd.add_argument("--record", help="v1 mode only: path to the CandidateRecord")
    review_cmd.add_argument(
        "--check-result",
        action="append",
        help="path to a CheckResult the run produced (repeatable; pass none when it produced none)",
    )
    review_cmd.add_argument("--result", help="optional ReviewResult to check against the package")
    review_cmd.add_argument(
        "--executor",
        help="the executor's identity; omitted, reviewer distinctness is reported as UNVERIFIED",
    )
    review_cmd.add_argument("--repo-root", help="repository root (default: current directory)")
    review_cmd.set_defaults(func=_cmd_v3_review)

    return p


def main(argv: list[str] | None = None) -> int:
    try:  # UTF-8 console so diagnostics never crash on a Windows cp1252 stdout
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
