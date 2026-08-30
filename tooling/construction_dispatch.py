#!/usr/bin/env python3
"""Construction-side dispatch — the three cold entries a round against a repository's own rules uses.

Three dispatch families live here: the **bounded review** of a round's commit range, the
**E10 instruction-layer read**, and that round's own **executor**. They were three modes of
`dtw dispatch` until round `CORE-ONLY-CODE` (`document-harness/plans/core-only.plan.md`
item C), which measured them as the code a repository mounting this harness receives and
cannot use, and whose acceptance 6 bounds a construction-only code path out of the tree that
travels. So they live here instead: outside `tooling/rsclib/document_harness/`, beside the
instrument's other construction-side scripts, and outside every row of
`CONSTRUCTION-INDEX.md`'s product-run tier.

**Not in `tooling/rsclib/document_harness/`, and not a fourth guard in `tooling/hooks/`.**
That package is one product-tier row and travels whole, so a module inside it would travel
whatever this docstring said; `tooling/hooks/` holds pre-commit checks a repository wires,
which this is not. `tooling/` itself is where this instrument already keeps the instruments
its own rounds run — `sweep_refs.py`, `ledger_cap_check.py`, `announced_path_disclosure.py` —
and a construction-side dispatch generator is one more of those.

**What is imported rather than copied.** The derivation this whole layer exists for stays in
`rsclib.document_harness.dispatch`, in one live copy: `resolve_subject` (a dispatched
abbreviation is a weaker binding than the custody chain assumes), `write_freeze_marker`
(E9's review window, which `review_freeze_check.py` reads), and the declared-rules naming.
Two copies of any of them would be the drift surface the dispatch layer was built to remove.
`_value` is imported under its private name deliberately: re-typing its marker text here
would be a second copy of it, and promoting it to the package's public surface would widen
what a caller receives for a reason no caller has any part in.

**The charter is derived, never hard-coded — and it is the declaration itself.** Until this
round the two review-side modes named a retired contract stub by constant and the executor
mode named this repository's checklist by another; `E10`'s second sentence and plan ruling 9
replace both with what the repository declares under `rules` in its own `harness.json`.
`REVIEW.md` says the same thing from the other side: *what is left of the construction-side
contract for reviewing the harness itself is that instrument's own rule file, declared under
`rules` in its `harness.json`*. So the charter line and the declared-rules line ruling 9 asks
every prompt to carry are **one line here** — the ruling's own second option, *the generator
folds them* — because the file is the same file, and naming it twice would say less, not
more. A repository that declares nothing gets a refusal rather than a prompt naming no
charter: a prompt whose one job is to name the standing instruction cannot do it, and that is
a mis-route the dispatcher cannot otherwise see.

**Nothing else is derived, and that is the design.** A construction round has no control
plane — its range is the one thing no control plane records — so what a product review
derives from committed state has no counterpart here, and feeding a round's name, boundary or
"what to hunt for" in by hand would reproduce exactly what the dispatch layer exists to
abolish: a fact you were handed is a fact you did not check. What can be refused is refused,
each of it one git call.

    python tooling/construction_dispatch.py --range BASE..TIP
    python tooling/construction_dispatch.py --read REVISION
    python tooling/construction_dispatch.py --construction-executor

The prompt goes to stdout and the dispatcher's own view to stderr, so redirecting stdout
yields a file holding only what the dispatched session should see. Exit 0 = derived,
1 = not dispatchable (printed with its issues, because the dispatcher needs to see what is
wrong more than they need a success), 2 = the command itself could not run.
"""
from __future__ import annotations

import argparse
import dataclasses
import pathlib
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from rsclib.document_harness import Issue, Report, report_of  # noqa: E402
from rsclib.document_harness.caller import HarnessConfigError  # noqa: E402
from rsclib.document_harness.dispatch import (  # noqa: E402
    CODE,
    _value,
    declared_rules,
    declared_rules_phrase,
    resolve_subject,
    write_freeze_marker,
)

#: The whole reviewer-facing prompt. One constant, three substitutions — so the test can
#: assert the emitted document equals this exactly, which catches an added line, a missing
#: line and a reordered line alike. The partition guard it replaced could only ever catch the
#: first. The declaration sits on a line of its own in all three prompts below, so that a
#: long or plural one cannot push a fixed line past the width.
CONSTRUCTION_PROMPT = """\
You are the independent bounded reviewer for Document Work Assurance Harness v3.

Your standing instructions are the rule files this repository declares under
`rules` in its `harness.json`:
{rules}
Read them, and the counterpart they name, before anything else. They govern this
round and bind this repository alone. This prompt does not govern it — it exists
only to hand you the subject.

**Subject: `{base}..{tip}`**

Everything else you derive from the repository: which round this is and what budget
it carries, what was authorized and by whom, what the work was obliged to do, and how
to report. All of it is committed; none of it is restated here, because a fact you
were handed is a fact you did not check.
"""

#: The reader's prompt. The member set is NOT enumerated here: `E10`'s own sentence owns it
#: and the reader derives it there. The hand-written read dispatch this mode replaced
#: enumerated the members and got the set wrong (`v3-cold-read-451e8b0.md` M-1), which is the
#: anchoring failure this layer exists to remove.
READ_PROMPT = """\
You are the independent reader for Document Work Assurance Harness v3.

Your standing instructions are the rule files this repository declares under
`rules` in its `harness.json`:
{rules}
Read them, and the counterpart they name, before anything else. They govern this
read and bind this repository alone. This prompt does not govern it — it exists
only to hand you the subject.

**Subject: the instruction layer at `{commit}` (an E10 read)**

Everything else you derive from the repository: the layer's member set from E10's own
sentence, each member's bytes at the subject commit, and how to report. All of it is
committed; none of it is restated here, because a fact you were handed is a fact you
did not check.
"""

#: The executor's prompt: one sentence, one substitution, nothing derived.
CONSTRUCTION_EXECUTOR_PROMPT = """\
You are the executor for a construction round of Document Work Assurance Harness v3.
Your standing instructions are the rule files this repository declares under
`rules` in its `harness.json`:
{rules}
Read them, and the counterpart they name, before anything else — their
execution-side heading binds this role by name.
"""

#: Refused rather than defaulted. A repository that declares no rules is not defective
#: (`E10`), but it has no standing instruction for these three roles, so there is no prompt
#: to write — and inventing one, or naming the harness's own charter as though it were this
#: repository's, is the anchoring failure rather than a convenience.
#: What the dispatcher's own view shows where the charter could not be named.
NOTHING = "(none declared)"

UNDECLARED = (
    "this repository declares no rule files under `rules` in its `harness.json`, so a "
    "construction round here has no standing instruction to name; declare one, then "
    "dispatch"
)


def _charter(repo_root: pathlib.Path) -> tuple[tuple[str, ...], Report]:
    """The declared rules that are this round's charter, or the refusal that there are none."""
    rules = declared_rules(repo_root)
    if rules:
        return rules, report_of([])
    return rules, report_of([Issue(f"{CODE}-NO-DECLARED-RULES", UNDECLARED, "rules")])


def _refusal(what: str, report: Report) -> str:
    """A refusal is not a prompt: it names no subject, so it cannot be routed by pasting."""
    lines = [
        "# NOT DISPATCHABLE",
        "",
        f"{what} Resolve the following, then re-run.",
        "",
    ]
    lines += [f"- {issue.render()}" for issue in report.issues]
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# A round's bounded review — the range is the one irreducible input
# ---------------------------------------------------------------------------


@dataclasses.dataclass(frozen=True)
class ConstructionDispatch:
    """The two bounding revisions, resolved. `None` means derivation stopped; see report."""

    base: str | None
    tip: str | None
    report: Report
    #: The rule files this repository declares, which are this round's charter.
    rules: tuple[str, ...] = ()


def construction_dispatch_of(
    repo_root: pathlib.Path | str, base: str, tip: str
) -> ConstructionDispatch:
    """Resolve and sanity-check the two revisions that bound a construction round."""
    repo_root = pathlib.Path(repo_root)
    rules, report = _charter(repo_root)
    base_sha, base_report = resolve_subject(repo_root, base)
    tip_sha, tip_report = resolve_subject(repo_root, tip)
    report = report + base_report + tip_report
    if base_sha is None or tip_sha is None:
        return ConstructionDispatch(base_sha, tip_sha, report, rules)

    # An unordered pair does not bound a round, and picking an order for the caller would
    # invent a round they did not mean.
    ancestry = subprocess.run(
        ["git", "-C", str(repo_root), "merge-base", "--is-ancestor", base_sha, tip_sha],
        check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    if ancestry.returncode != 0:
        return ConstructionDispatch(base_sha, tip_sha, rules=rules, report=report + report_of([
            Issue(
                f"{CODE}-RANGE-NOT-ANCESTRAL",
                f"{base_sha[:12]} is not an ancestor of {tip_sha[:12]}, so these two do not "
                "bound a round",
                "base",
            )
        ]))

    revs = subprocess.run(
        ["git", "-C", str(repo_root), "rev-list", "--count", f"{base_sha}..{tip_sha}"],
        check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    if revs.returncode != 0 or int(revs.stdout.decode().strip() or 0) == 0:
        return ConstructionDispatch(base_sha, tip_sha, rules=rules, report=report + report_of([
            Issue(
                f"{CODE}-EMPTY-RANGE",
                f"{base_sha[:12]}..{tip_sha[:12]} contains no commit, so there is nothing to "
                "review",
                "tip",
            )
        ]))

    return ConstructionDispatch(base=base_sha, tip=tip_sha, report=report, rules=rules)


def render_construction_dispatch(dispatch: ConstructionDispatch) -> str:
    """The reviewer-facing prompt: the charter, the range, and nothing else."""
    if not dispatch.report.ok:
        return _refusal(
            "The two revisions given do not bound a reviewable round, so no dispatch was "
            "produced.",
            dispatch.report,
        )
    return CONSTRUCTION_PROMPT.format(
        rules=declared_rules_phrase(dispatch.rules),
        base=dispatch.base,
        tip=dispatch.tip,
    )


def render_construction_derivation(dispatch: ConstructionDispatch) -> str:
    """Two lines for the dispatcher: what the typed revisions resolved to, and the charter.

    Deliberately not a second view of the prompt. The dispatcher types abbreviations; this
    confirms what they became, and nothing else is derived to show.
    """
    lines = [
        f"derived round     : {_value(dispatch.base)}..{_value(dispatch.tip)}",
        f"  charter         : {declared_rules_phrase(dispatch.rules) or NOTHING}",
    ]
    for issue in dispatch.report.issues:
        lines.append("  ! " + issue.render())
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Instruction-layer reads (E10) — one commit, no control plane, no member list
# ---------------------------------------------------------------------------


@dataclasses.dataclass(frozen=True)
class ReadDispatch:
    """The one resolved revision a layer read is bound to. `None` means see report."""

    commit: str | None
    report: Report
    #: The rule files this repository declares, which are this read's charter.
    rules: tuple[str, ...] = ()


def read_dispatch_of(repo_root: pathlib.Path | str, revision: str) -> ReadDispatch:
    """Resolve the commit whose instruction layer is the read's subject."""
    repo_root = pathlib.Path(repo_root)
    rules, report = _charter(repo_root)
    commit, resolve_report = resolve_subject(repo_root, revision)
    return ReadDispatch(commit=commit, report=report + resolve_report, rules=rules)


def render_read_dispatch(dispatch: ReadDispatch) -> str:
    """The reader-facing prompt: the charter, the commit, and nothing else."""
    if not dispatch.report.ok:
        return _refusal(
            "The revision given does not resolve to a commit under a declared charter, so no "
            "read dispatch was produced.",
            dispatch.report,
        )
    return READ_PROMPT.format(
        rules=declared_rules_phrase(dispatch.rules), commit=dispatch.commit
    )


def render_read_derivation(dispatch: ReadDispatch) -> str:
    """Two lines for the dispatcher: what the typed revision resolved to, and the charter."""
    lines = [
        f"derived subject   : {_value(dispatch.commit)} (instruction-layer read)",
        f"  charter         : {declared_rules_phrase(dispatch.rules) or NOTHING}",
    ]
    for issue in dispatch.report.issues:
        lines.append("  ! " + issue.render())
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# The round's executor — the charter, and nothing else to derive
# ---------------------------------------------------------------------------


@dataclasses.dataclass(frozen=True)
class ConstructionExecutorDispatch:
    """The charter and nothing else — a construction round derives nothing."""

    report: Report
    #: The rule files this repository declares, which are this executor's charter.
    rules: tuple[str, ...] = ()


def construction_executor_dispatch_of(
    repo_root: pathlib.Path | str,
) -> ConstructionExecutorDispatch:
    """Resolve the construction executor's charter. Nothing else exists to derive."""
    rules, report = _charter(pathlib.Path(repo_root))
    return ConstructionExecutorDispatch(report=report, rules=rules)


def render_construction_executor_dispatch(dispatch: ConstructionExecutorDispatch) -> str:
    """One sentence: the charter pointer."""
    if not dispatch.report.ok:
        return _refusal(
            "No charter could be named for a construction executor, so no dispatch was "
            "produced.",
            dispatch.report,
        )
    return CONSTRUCTION_EXECUTOR_PROMPT.format(rules=declared_rules_phrase(dispatch.rules))


def render_construction_executor_derivation(
    dispatch: ConstructionExecutorDispatch,
) -> str:
    """One line for the dispatcher; the mode derives nothing but the charter, and says so."""
    lines = [
        f"derived charter   : {declared_rules_phrase(dispatch.rules) or NOTHING} "
        "(construction executor — nothing else is derived)"
    ]
    for issue in dispatch.report.issues:
        lines.append("  ! " + issue.render())
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# The command
# ---------------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="construction_dispatch",
        description="derive a construction round's dispatch from committed state: a round's "
                    "review range, an E10 layer read, or that round's executor",
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument(
        "--range",
        help="ROUND review: BASE..TIP, the one thing no control plane records",
    )
    mode.add_argument(
        "--read",
        help="E10 layer read: the commit whose instruction layer is the subject",
    )
    mode.add_argument(
        "--construction-executor",
        action="store_true",
        help="ROUND executor: one sentence naming the charter; nothing derived",
    )
    parser.add_argument(
        "--repo-root",
        help="repository root (default: the git toplevel of the current directory, or a "
             "loud refusal)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    try:  # UTF-8 console so diagnostics never crash on a Windows cp1252 stdout
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    args = build_parser().parse_args(argv)

    from rsclib.document_harness import SpecGap
    from rsclib.document_harness import caller as v3_caller

    if args.repo_root:
        repo_root = pathlib.Path(args.repo_root).resolve()
    else:
        # Never the bare cwd (round STRANGER-GUARDS): git is asked for the toplevel, and a
        # refusal is loud rather than a plausible wrong root taken quietly.
        try:
            repo_root = v3_caller.discover_repo_root(pathlib.Path.cwd())
        except SpecGap as exc:
            print(f"FATAL: {exc}", file=sys.stderr)
            return 2
        print(f"repo root discovered: {repo_root}", file=sys.stderr)

    try:
        if args.range:
            base, sep, tip = args.range.partition("..")
            if not sep or not base or not tip:
                print(f"FATAL: --range takes BASE..TIP, got {args.range!r}", file=sys.stderr)
                return 2
            derived = construction_dispatch_of(repo_root, base, tip)
            render, render_derivation = (
                render_construction_dispatch,
                render_construction_derivation,
            )
            subject = f"{derived.base}..{derived.tip}"
        elif args.read:
            derived = read_dispatch_of(repo_root, args.read)
            render, render_derivation = render_read_dispatch, render_read_derivation
            subject = derived.commit
        else:
            derived = construction_executor_dispatch_of(repo_root)
            render, render_derivation = (
                render_construction_executor_dispatch,
                render_construction_executor_derivation,
            )
            subject = None
    except HarnessConfigError as exc:
        print(f"FATAL: {exc}", file=sys.stderr)
        return 2

    # Two audiences, two streams. The derivation is the DISPATCHER's check that they are
    # routing the round they think they are; it goes to stderr so that stdout carries only
    # what the dispatched session should see.
    print(render_derivation(derived), file=sys.stderr)

    # A review-side dispatch opens E9's window; an executor dispatch starts precisely the
    # work that window would freeze, so it writes nothing.
    if derived.report.ok and subject is not None:
        marker = write_freeze_marker(repo_root, subject)
        print(
            f"freeze marker written: {marker} — delete it in the act that commits the "
            "returned record",
            file=sys.stderr,
        )

    # Printed, never written. A dispatch is a startup PROMPT, not an artifact: every fact in
    # it is already committed, and persisting it would store a derived copy that can go stale
    # against the generator — which is what happened when one was committed and then read
    # back after the generator had moved on. There is deliberately no --out.
    print(render(derived), end="")
    print(
        "RESULT: " + ("derived (exit 0)" if derived.report.ok else "NOT dispatchable (exit 1)"),
        file=sys.stderr,
    )
    return 0 if derived.report.ok else 1


if __name__ == "__main__":
    sys.exit(main())
