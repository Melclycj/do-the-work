"""Dispatch derivation — every dispatched role's cold entry, from committed state.

The reviewer side has a cold entry: `review_subject.read_control_plane` derives spec, plan
and CandidateRecord from an evidence commit, so a fresh session needs nothing but the SHA.
The executor side had no counterpart. Every dispatch to date — this package's own product
runs and the hand-written `W2/W2-dispatch-*.md` — was composed by hand from values re-read
off a screen, which makes the facts a reviewer is anchored by the *dispatcher's* rather than
the *repository's*. That is avoidable: role, subject, control root, boundary, accepted
findings and result schema are all derivable from committed state
(`issue-p3-corr-no-dispatch-generator`, routed CORE_CANDIDATE 2026-07-25). Two dispatch
families live here — a product run's review and, since round EXECUTOR-CHARTER (2026-08-22
ruling), that run's executor's own charter; each family's section below carries its
reasoning.

**Three families left in round CORE-ONLY-CODE** (plan `core-only.plan.md` item C): the
bounded review of a round's commit range, the E10 instruction-layer read, and that round's
executor. All three are of use only to a repository running rounds against its own declared
rules, so acceptance 6 bounds them out of the tree a caller mounts, and they live outside it
now. What went with them is only their own prompts and their own derivation; the generic
plumbing — `resolve_subject`, `write_freeze_marker`, `declared_rules_line` — stays here in
one live copy and is imported rather than duplicated.

**Every prompt names what the repository declares.** `E10`'s second sentence holds this
command to naming the declared files in every prompt it writes, so that a cold session
receives a repository's rules by the channel it receives its charter. The line is generated
from `harness.json` (`declared_rules_line` below), never hand-copied into each prompt
constant, and it is emitted even when nothing is declared: a cold session cannot otherwise
tell "this repository declares no rules" from "the generator forgot to say".

**What this module deliberately does not generate.** An earlier version emitted a marked gap
for the dispatcher to fill with what *this* round was worth hunting for. That is gone: once
such a section enumerates what to check it is a shadow WorkSpec, ex post and approved by
nobody, competing with the artifact that legitimately says what the work was obliged to do.
The reasoning is set out at the rendering section below, which is the single home for it.

Nothing here judges the run. Deriving a dispatch is not approving one — but a subject that
fails `check_subject` is still *printed*, as a refusal rather than as a dispatch document:
the dispatcher sees exactly what is wrong, and the refusal deliberately does not restate the
SHA as a subject, so it cannot be routed by pasting past the warning.
"""
from __future__ import annotations

import dataclasses
import json
import pathlib
import subprocess
from typing import Any, Mapping, Sequence

from rsclib.document_harness import Issue, Report, report_of
from rsclib.document_harness.caller import load_harness_config
from rsclib.document_harness.candidate import CandidateTreeReader
from rsclib.document_harness.review_subject import (
    STATE_PATH,
    check_subject,
    read_control_plane,
    subject_of,
)

CODE = "V3-DISPATCH"

#: The one status a review is dispatched from. The flow reaches it twice — once at the
#: round-0 evidence layer and again after a repair regenerates evidence (contract §8) — and
#: `repair_round` is what tells the two apart. Any other status means the run is not at a
#: position where a review is the next thing, which is worth refusing to paper over.
DISPATCHABLE_STATUS = "EVIDENCED"

#: A commit-bound subject admits only the v2 ReviewResult: `review_result_v2` stops a v1
#: result outright rather than validating package-bound semantics against a commit. So this
#: is derived with certainty from the shape of the subject, not guessed from the spec.
#: Instrument-relative, resolved for the subject repository by `instrument_relative`.
RESULT_SCHEMA = "schema/document-assurance-v3/review.v2.schema.json"


def instrument_relative(repo_root: pathlib.Path | str, member: str) -> str:
    """Where `member` — a path inside this instrument — is opened from `repo_root`.

    Not a constant, because it is a deployment fact. A member is its own repository-root
    path when a round runs inside this repository and `ResearchSystem/harness/…` from the
    caller that mounts it as a submodule, and a prompt naming a path the reviewer
    cannot open is a prompt that fails at its one job. Written as a literal it was right in
    exactly one of the two, and the split made the caller the wrong one: the first dispatch
    issued after the caller's duplicate copy was deleted named a charter resolving nowhere.

    When the instrument is not under `repo_root` at all — a synthetic repository built by a
    test, where the instrument is somewhere else entirely — no repo-relative answer exists
    and the member's own name is returned. That is the honest output for that case and it is
    what the goldens pin.
    """
    from rsclib.document_harness import RS_ROOT

    try:
        prefix = RS_ROOT.resolve().relative_to(pathlib.Path(repo_root).resolve())
    except ValueError:
        return member
    return (prefix / member).as_posix()


#: The one sentence every prompt carries about the repository's own rules, in one live copy
#: rather than repeated into each prompt constant (E10's second sentence; plan ruling 9).
DECLARED_RULES_LINE = (
    "**This repository's own rules:** {rules} — declared under `rules` in its "
    "`harness.json`, to be read after the charter above. They bind this repository alone."
)

#: What that line says where a repository declares nothing. Stated rather than omitted: an
#: absent line reads the same as a generator that failed, and E10 says a repository that has
#: declared nothing is not defective — so the prompt says which of the two it is.
DECLARED_RULES_ABSENT_LINE = (
    "**This repository's own rules:** none. Its `harness.json` declares no rule files, "
    "which E10 makes a repository that has declared nothing rather than a defective one."
)


def declared_rules(repo_root: pathlib.Path | str) -> tuple[str, ...]:
    """The rule files this repository declares — repo-root-relative, never mount-relative.

    Unlike a charter, which is a path inside this instrument and needs `instrument_relative`
    to be openable from a caller, a declared rule belongs to the repository being dispatched
    in and is already named from that repository's own root.
    """
    return load_harness_config(repo_root).rules


def declared_rules_phrase(rules: Sequence[str]) -> str:
    """How any prompt names the declarations, so the naming has one live copy."""
    return " · ".join(f"`{path}`" for path in rules)


def declared_rules_line(rules: Sequence[str]) -> str:
    """The prompt's declared-rules line — two sentences, because none is not a short list.

    Formatting an empty list into the sentence below would emit "your own rules: — declared
    under rules in its harness.json", which is a defect that reads like a template bug. The
    absence gets a sentence of its own instead.
    """
    if not rules:
        return DECLARED_RULES_ABSENT_LINE
    return DECLARED_RULES_LINE.format(rules=declared_rules_phrase(rules))


#: E9's review window, held mechanically by the tracked `review_freeze_check.py`, which reads
#: this file. Written by a review-side dispatch; deleted by the act that commits the returned
#: record. An executor-side dispatch writes none — the marker freezes precisely the work an
#: executor dispatch starts.
FREEZE_MARKER = ".harness/review-pending.json"


def write_freeze_marker(repo_root: pathlib.Path | str, subject: str) -> pathlib.Path:
    """Open E9's window for `subject` and return where the marker was written.

    One live copy, called by every review-side dispatch wherever its mode lives. The marker
    records the SUBJECT and nothing about what kind of work it is. It used to carry a `kind`
    derived from which flag was typed rather than from what was dispatched, so a product run
    forced onto a range was labelled "construction-round" (p5b-firewall,
    issue-p5b-firewall-dispatch-types-product-run-as-construction). The field was deleted
    rather than taught: nothing branches on it — `review_freeze_check.py` read it only to
    print a display line — and `R2` forbids a reviewer trusting anything handed to them, so a
    value no code consumes and no reviewer may rely on can only ever mislead. The subject
    itself says which family it is: a `..` range, or one 40-hex commit.
    """
    import datetime
    import json as _json

    marker = pathlib.Path(repo_root) / FREEZE_MARKER
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
    return marker


#: Closed per-round verdicts (contract §5). A VERIFY cannot return `CHANGES_REQUIRED`:
#: there is no second repair for it to request, and a remaining blocker stops the round.
VERDICTS: dict[str, tuple[str, ...]] = {
    "FULL": ("REVIEWED_NO_BLOCKER", "CHANGES_REQUIRED", "SPEC_GAP"),
    "VERIFY": ("REVIEWED_NO_BLOCKER", "SPEC_GAP"),
}

_STATE_SUFFIX = f"/{STATE_PATH}"


@dataclasses.dataclass(frozen=True)
class Dispatch:
    """Everything a dispatch can state from the repository, plus what could not be derived.

    Fields are `None` when derivation failed; the reason is always in `report`, never
    swallowed. `render` prints an unresolved field as an explicit marker rather than an
    empty string, so a half-derived dispatch cannot be pasted out looking whole.
    """

    evidence_commit: str
    control_root: str | None
    role: str | None
    run_id: str | None
    work_id: str | None
    repair_round: int | None
    status: str | None
    base_revision: str | None
    candidate_ref: dict[str, Any] | None
    accepted_finding_ids: tuple[str, ...]
    repair_boundary: dict[str, Any] | None
    change_boundary: dict[str, Any] | None
    obligation_count: int | None
    check_count: int | None
    report: Report
    #: Instrument paths resolved for THIS subject repository (`instrument_relative`).
    charter: str = ""
    result_schema: str = ""
    #: What THIS repository declares under `rules`; repo-root-relative, so no resolution.
    declared_rules: tuple[str, ...] = ()


def control_root_of(
    repo_root: pathlib.Path | str, evidence_commit: str
) -> tuple[str | None, Report]:
    """Find the run's control root from the evidence commit's own changed paths.

    The evidence step advances the state and commits the control root, so exactly one path
    in the commit ends in `control/state.json`. Deriving the root from that is what makes
    the command SHA-only: `read_control_plane` needs the root, and requiring the caller to
    supply it would just move the hand-copied value one step earlier.

    Zero matches and several matches are both reported rather than resolved by preference:
    a commit touching two runs' control planes is a real defect in how it was staged, and
    silently picking one would hide it.
    """
    issues: list[Issue] = []
    shown = subprocess.run(
        ["git", "-C", str(repo_root), "show", "--name-only", "--format=", evidence_commit],
        check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    if shown.returncode != 0:
        issues.append(
            Issue(
                f"{CODE}-COMMIT-UNREADABLE",
                f"git could not read {evidence_commit}: "
                f"{shown.stderr.decode('utf-8', errors='replace').strip()}",
                "evidence_commit",
            )
        )
        return None, report_of(issues)

    paths = [line.strip() for line in shown.stdout.decode("utf-8", errors="replace").splitlines()]
    roots = sorted({p[: -len(_STATE_SUFFIX)] for p in paths if p.endswith(_STATE_SUFFIX)})
    if not roots:
        # The remedy is part of the refusal, not left to the reader. Stating only the fact
        # tells an executor that this commit will not work and nothing about what will, and
        # the reasonable next move from there is the other door: p5b-firewall met exactly
        # this message and dispatched its product run through `--range`, which is the
        # construction-round entry and hands the reviewer a range diff instead of a control
        # plane (issue-p5b-firewall-dispatch-types-product-run-as-construction, 2026-08-07).
        # Routing around a correct refusal is the failure; naming the way through is the fix.
        issues.append(
            Issue(
                f"{CODE}-NOT-AN-EVIDENCE-COMMIT",
                f"no path in {evidence_commit} ends in {STATE_PATH}, so this commit does not "
                "carry a run's control plane and is not a review subject; re-stage the run's "
                "whole control root and commit it, then dispatch that commit",
                "evidence_commit",
            )
        )
        return None, report_of(issues)
    if len(roots) > 1:
        issues.append(
            Issue(
                f"{CODE}-AMBIGUOUS-CONTROL-ROOT",
                f"{evidence_commit} touches the control plane of more than one run "
                f"({', '.join(roots)}); an evidence commit stages exactly one control root",
                "control_root",
            )
        )
        return None, report_of(issues)
    return roots[0], report_of(issues)


def resolve_subject(
    repo_root: pathlib.Path | str, revision: str
) -> tuple[str | None, Report]:
    """Expand any git revision to the full 40-hex commit the dispatch will name.

    Not a convenience. A dispatched abbreviation is a weaker binding than the custody chain
    assumes — w1-r1 routed an 8-hex prefix, a 2^32 collision space, and REVIEW.md's escrow
    section was corrected to require the digest in full. Resolving here means the dispatcher
    may type `HEAD` or a short SHA while the routed document always carries the full commit.
    """
    out = subprocess.run(
        ["git", "-C", str(repo_root), "rev-parse", "--verify", "--quiet", f"{revision}^{{commit}}"],
        check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    resolved = out.stdout.decode("utf-8", errors="replace").strip()
    if out.returncode != 0 or len(resolved) != 40:
        return None, report_of([
            Issue(
                f"{CODE}-COMMIT-UNREADABLE",
                f"'{revision}' does not resolve to a commit in this repository",
                "evidence_commit",
            )
        ])
    return resolved, report_of([])


def role_for(state: Mapping[str, Any]) -> tuple[str | None, Report]:
    """Which review the run is owed: FULL at round 0, the targeted VERIFY afterwards.

    Both facts are needed. `status` says whether a review is the next thing at all, and
    `repair_round` says which one — reading either alone would dispatch a FULL of a repaired
    candidate or a review of a run that already closed.
    """
    issues: list[Issue] = []
    status = state.get("status")
    if status != DISPATCHABLE_STATUS:
        issues.append(
            Issue(
                f"{CODE}-NOT-DISPATCHABLE",
                f"the run is at status {status}, not {DISPATCHABLE_STATUS}; a review is not "
                "the next action from this position",
                "status",
            )
        )
        return None, report_of(issues)
    round_ = state.get("repair_round")
    if not isinstance(round_, int):
        issues.append(
            Issue(
                f"{CODE}-ROUND-UNREADABLE",
                f"the state carries no integer repair_round ({round_!r}), so which review is "
                "owed cannot be derived",
                "repair_round",
            )
        )
        return None, report_of(issues)
    return ("FULL" if round_ == 0 else "VERIFY"), report_of(issues)


def _repair_binding(
    plane_state: Mapping[str, Any], repo_root: pathlib.Path | str, evidence_commit: str
) -> tuple[tuple[str, ...], dict[str, Any] | None, list[Issue]]:
    """The accepted findings and repair boundary a VERIFY is scoped to, read from the commit.

    This is the part of a hand-written VERIFY dispatch most exposed to anchoring: the
    reviewer's whole scope is these IDs, and a list retyped from a screen can silently drop
    one. Here it comes from the committed REPAIR decision or not at all.
    """
    issues: list[Issue] = []
    ref = plane_state.get("repair_decision_ref")
    if not ref:
        issues.append(
            Issue(
                f"{CODE}-REPAIR-DECISION-ABSENT",
                "the run is past a repair but the committed state carries no "
                "repair_decision_ref, so the VERIFY's scope cannot be derived",
                "repair_decision_ref",
            )
        )
        return (), None, issues
    raw = CandidateTreeReader(pathlib.Path(repo_root), evidence_commit).read(ref["path"])
    if raw is None:
        issues.append(
            Issue(
                f"{CODE}-REPAIR-DECISION-MISSING",
                f"the repair decision does not resolve in the evidence commit: {ref['path']}",
                "repair_decision_ref",
            )
        )
        return (), None, issues
    try:
        decision = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        issues.append(
            Issue(f"{CODE}-REPAIR-DECISION-INVALID", f"{ref['path']} is not valid JSON: {exc}",
                  "repair_decision_ref")
        )
        return (), None, issues
    target = decision.get("target", {})
    return (
        tuple(target.get("accepted_finding_ids", ())),
        target.get("repair_boundary"),
        issues,
    )


def dispatch_of(repo_root: pathlib.Path | str, evidence_commit: str) -> Dispatch:
    """Derive the whole dispatch from one SHA. Failures are reported, never raised."""
    repo_root = pathlib.Path(repo_root)
    rules = declared_rules(repo_root)
    resolved, resolve_report = resolve_subject(repo_root, evidence_commit)
    if resolved is None:
        return Dispatch(evidence_commit, None, None, None, None, None, None, None, None,
                        (), None, None, None, None, resolve_report,
                        instrument_relative(repo_root, ROLE_INSTRUCTION),
                        instrument_relative(repo_root, RESULT_SCHEMA), rules)
    evidence_commit = resolved

    control_root, report = control_root_of(repo_root, evidence_commit)
    if control_root is None:
        return Dispatch(evidence_commit, None, None, None, None, None, None, None, None,
                        (), None, None, None, None, report,
                        instrument_relative(repo_root, ROLE_INSTRUCTION),
                        instrument_relative(repo_root, RESULT_SCHEMA), rules)

    plane = read_control_plane(repo_root, evidence_commit, control_root)
    report = report + plane.report
    state = plane.state or {}
    role, role_report = role_for(state)
    report = report + role_report

    issues: list[Issue] = []
    accepted: tuple[str, ...] = ()
    repair_boundary: dict[str, Any] | None = None
    if role == "VERIFY":
        accepted, repair_boundary, repair_issues = _repair_binding(
            state, repo_root, evidence_commit
        )
        issues.extend(repair_issues)

    record = plane.record or {}
    plan = plane.plan or {}
    spec = plane.spec or {}

    # `read_control_plane` answers "do the pointers resolve and match their bytes"; it does
    # NOT answer "is this a complete review subject" — that is `check_subject`, which
    # re-derives the expected CheckResult set from the committed plan's check_order and
    # verifies the commit against what its own CandidateRecord claims. Deriving a clean
    # dispatch for a commit that fails it would route an incomplete subject with no signal,
    # which is the fail-open shape this package exists to refuse. Skipped only when the
    # record is unreadable, since there would be nothing to build the subject from.
    if record.get("candidate_ref") and record.get("base_revision") is not None:
        subject = subject_of(
            evidence_commit=evidence_commit,
            candidate_ref=record["candidate_ref"],
            base_revision=record["base_revision"],
            control_root=control_root,
            repair_round=record.get("repair_round", state.get("repair_round", 0)),
        )
        report = report + check_subject(subject, repo_root)
    else:
        issues.append(
            Issue(
                f"{CODE}-SUBJECT-UNCHECKED",
                "the CandidateRecord did not yield a candidate_ref and base_revision, so the "
                "commit could not be checked as a complete review subject; this is an "
                "unverified property, not a satisfied one",
                "fulfillment_ref",
            )
        )

    return Dispatch(
        evidence_commit=evidence_commit,
        control_root=control_root,
        role=role,
        run_id=state.get("run_id"),
        work_id=state.get("work_id"),
        repair_round=state.get("repair_round"),
        status=state.get("status"),
        base_revision=record.get("base_revision"),
        candidate_ref=record.get("candidate_ref"),
        accepted_finding_ids=accepted,
        repair_boundary=repair_boundary,
        change_boundary=plan.get("effective_change_boundary"),
        obligation_count=len(spec.get("obligations", [])) or None,
        check_count=len(plan.get("check_order", [])) or None,
        report=report + report_of(issues),
        charter=instrument_relative(repo_root, ROLE_INSTRUCTION),
        result_schema=instrument_relative(repo_root, RESULT_SCHEMA),
        declared_rules=rules,
    )


# ---------------------------------------------------------------------------
# Rendering — two audiences, deliberately separated
# ---------------------------------------------------------------------------
#
# The reviewer's document and the dispatcher's are NOT the same document, and the first
# version of this module got that wrong by making them one. It handed the reviewer a
# pre-derived table of run facts and a restatement of the review contract — which defeats
# the property the whole layer exists for. `REVIEW.md` already carries the role charter
# ("The two rounds", "When the subject is one commit", "What every result must carry"), so
# repeating it here is a second live copy that can drift; and the run template's own README
# says it plainly: *the reviewer re-derives; there is no member list to hand over*. A fact
# you hand a reviewer is a fact they did not check, and an error in the handed table is
# inherited in silence. That is the same anchoring risk this module was written to remove,
# only mechanised.
#
# So exactly ONE thing is told rather than derived: the **subject SHA**, which must arrive
# out-of-band from the dispatching party (REVIEW.md's custody chain). Everything else — which
# round, the control plane, the boundary, the obligations, the checks — the reviewer derives
# from the SHA, and the contract they answer to they read from `REVIEW.md`.
#
# An earlier version also carried a per-round "what is worth hunting for" section for the
# dispatcher to fill. It is gone, and the reason generalises the rule above. Once such a
# section enumerates what to check it has become a **shadow WorkSpec**: ex post,
# executor-authored, approved by nobody, outside the control plane, competing with the one
# artifact that legitimately states what the work was obliged to do. `REVIEW.md`'s *What you
# are given: a floor, never a ceiling* already warns that an executor summary is supplemental
# and that reviewing it establishes only that the executor described its own output
# consistently; a hunt list is that same substitution in a softer register. An executor who
# knows where its work is weak has two honest moves — fix it, or record it in the repository
# as a declared limitation — and routing it through a prompt is neither.
#
# **Cite the reviewer's OWN instruction, never the other side's.** The product-run reviewer
# reads `REVIEW.md`, whose sections are named and unnumbered; the numbered `§n` form belonged
# to the retired construction-side review contract, which governed a different role.
# An earlier version of this module emitted "your §8" into a product-run dispatch and a real
# reviewer reported it: the citation pointed at a document that was not their charter. Two
# charters, one module — so every reference here names its document explicitly.
#
# The retired construction-side review contract named one supplement as useful — which code was
# churned late — and this module does not emit it. For a product run it is vacuous: a bounded
# repair re-edits what round 0 edited, so "paths revised more than once" degenerates into the
# write scope, and the precise version of the same fact is already committed in the REPAIR
# decision's accepted findings and repair boundary. The construction half derived it for a
# while; that half and its write-up left this module in round `CORE-ONLY-CODE`. The short
# version is that §8's own opening ("One commit SHA. Nothing else") and §5.1's ban on
# accepting a reported number together mean the recipient must recompute whatever is sent,
# so sending it buys nothing.
#
# The derived table still matters, to the **dispatcher**: it is how a human confirms they
# are routing the run they think they are. `render_derivation` is that view, and the CLI
# sends it to stderr so that redirecting stdout yields a file containing only what the
# reviewer should see.

#: The reviewer's fixed role instruction. Named, never quoted — one live copy.
#: Instrument-relative; `Dispatch.charter` carries it resolved for the subject repository.
ROLE_INSTRUCTION = "document-harness/REVIEW.md"

_UNRESOLVED = "<<< NOT DERIVED — see the issues below >>>"


def _value(x: Any) -> str:
    return _UNRESOLVED if x is None else str(x)


def render_dispatch(dispatch: Dispatch) -> str:
    """The reviewer-facing document: the role instruction and the subject. Nothing else.

    A dispatch that could not be derived cleanly renders as a refusal instead — the SHA is
    not even restated, so a broken dispatch cannot be routed by pasting past the warning.
    """
    if not dispatch.report.ok:
        lines = [
            "# NOT DISPATCHABLE",
            "",
            f"`{dispatch.evidence_commit}` did not derive a clean review subject, so no",
            "dispatch document was produced. Resolve the following, then re-run.",
            "",
        ]
        lines += [f"- {issue.render()}" for issue in dispatch.report.issues]
        return "\n".join(lines) + "\n"

    lines = [
        f"# Review dispatch — `{dispatch.evidence_commit}`",
        "",
        "Read your role instruction first: it is the contract for this round, and this file",
        "is not. This file exists only to hand you the subject.",
        "",
        f"- **Role instruction:** `{dispatch.charter or ROLE_INSTRUCTION}`",
        f"- **Subject:** `{dispatch.evidence_commit}`",
        # The marker is state this dispatch itself created — like the subject, it is a fact
        # only the dispatch can hand over, so naming it here does not restate anything the
        # repository could teach (routed WORKFLOW_FIX by
        # user-decision-triage-review-role-deliverables-gap, p4-doc 2026-08-01: the duty
        # previously lived only on the executor-facing stdout, and the reviewer never saw it).
        "- **Freeze marker:** `.harness/review-pending.json` was written at this dispatch;",
        "  the commit that lands your returned record deletes it (see your role",
        "  instruction's deliverables section).",
        "",
        # E10's second sentence, generated rather than restated: the charter above is the
        # harness's, and this line is whatever THIS repository adds to it.
        declared_rules_line(dispatch.declared_rules),
        "",
        "Everything else you derive from the repository: which round this is and what budget",
        "it carries, what was authorized and by whom, what the work was obliged to do, and how",
        "to report. All of it is committed; none of it is restated here, because a fact you",
        "were handed is a fact you did not check.",
    ]
    return "\n".join(lines) + "\n"


def render_derivation(dispatch: Dispatch) -> str:
    """The dispatcher's view: what this SHA resolves to, so a mis-route is caught before it.

    Never part of the reviewer's document. Its whole purpose is that the person routing can
    see they are sending the run they mean to send.
    """
    role = dispatch.role or "UNKNOWN"
    lines = [
        f"derived subject   : {dispatch.evidence_commit}",
        f"  review round    : {role}   (admissible: {' / '.join(VERDICTS.get(role, ('—',)))})",
        f"  control root    : {_value(dispatch.control_root)}",
        f"  run / work      : {_value(dispatch.run_id)} / {_value(dispatch.work_id)}",
        f"  status / round  : {_value(dispatch.status)} / {_value(dispatch.repair_round)}",
        f"  base revision   : {_value(dispatch.base_revision)}",
    ]
    if dispatch.candidate_ref:
        lines.append(
            f"  candidate       : {dispatch.candidate_ref.get('commit')} "
            f"on {dispatch.candidate_ref.get('branch')}"
        )
    lines.append(
        f"  obligations/chk : {_value(dispatch.obligation_count)} / {_value(dispatch.check_count)}"
    )
    lines.append(f"  result schema   : {dispatch.result_schema or RESULT_SCHEMA}")
    if dispatch.accepted_finding_ids:
        lines.append("  repair scope    : " + ", ".join(dispatch.accepted_finding_ids))
    boundary = dispatch.repair_boundary if role == "VERIFY" else dispatch.change_boundary
    if boundary:
        scope = ", ".join(boundary.get("write_scope", ()) or ()) or "(none declared)"
        lines.append(f"  write scope     : {scope}")
    for issue in dispatch.report.issues:
        lines.append("  ! " + issue.render())
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Executor dispatches — the second family: the work side's own charter
# ---------------------------------------------------------------------------
#
# Until round EXECUTOR-CHARTER (user ruling 2026-08-22) every dispatch above was
# review-side, and ORCHESTRATION.md said so in as many words. A cold executor session held
# an instruction and a subject and had no way to learn that EXECUTION.md exists; the gap
# was papered over by an authoring rule requiring every product instruction to hand-copy a
# pointer to the standing discipline into its Context section — N instructions each
# restating one sentence, the drift surface this module exists to remove, while the
# reviewer's pointer was generated identically every time. These two modes close that
# asymmetry, and the authoring rule is deleted with them.
#
# The PRODUCT mode emits three facts and nothing more: the run id, the frozen
# instruction's path and revision, and the charter pointer. The timing is what makes that
# the whole of what is honest: the executor is dispatched at the START of a run, when the
# run directory holds a frozen instruction.md and little else — the WorkSpec is authored
# by the executor afterwards (HD-35), so no obligation, boundary or check exists yet to
# derive, and a "what to do" section composed here would be the shadow WorkSpec the
# rendering section above refuses, ex post and approved by nobody. What CAN be refused is
# refused: a directory outside the repository, a missing instruction, an instruction no
# commit has frozen, and worktree bytes that drifted from the frozen blob — each a real
# mis-route the dispatcher cannot see, each one git call.
#
# This mode writes no freeze marker: that marker opens E9's REVIEW window, and an
# executor dispatch starts precisely the work that window would freeze. The CLI holds
# that split.

#: The product-run executor's fixed role instruction. Named, never quoted — one live copy.
#: Instrument-relative; `ExecutorDispatch.charter` carries it resolved for the subject
#: repository.
EXECUTOR_ROLE_INSTRUCTION = "document-harness/EXECUTION.md"

#: The whole product-executor prompt. One constant, five substitutions — the test asserts
#: the emitted document equals it exactly, the shape that catches an added, missing or
#: reordered line alike.
EXECUTOR_PROMPT = """\
You are the executor for a product run of Document Work Assurance Harness v3.

Your role instruction is `{charter}`;
read it before anything else. It governs your work in this run.
This prompt does not — it exists only to hand you the run.

{declared_rules}

**Run: `{run_id}`**
**Instruction: `{instruction_path}`, frozen at `{revision}`**

Everything else you derive from the repository, and the WorkSpec is yours to
author — nothing here says what to do or what to check, because such a list
would be a WorkSpec nobody approved. A fact you were handed is a fact you did
not check.
"""


@dataclasses.dataclass(frozen=True)
class ExecutorDispatch:
    """The three facts a product executor is handed. `None` means see report."""

    run_dir: str
    run_id: str | None
    instruction_path: str | None
    revision: str | None
    report: Report
    #: The executor charter, resolved for THIS subject repository.
    charter: str = ""
    #: What THIS repository declares under `rules`; repo-root-relative, so no resolution.
    declared_rules: tuple[str, ...] = ()


def executor_dispatch_of(
    repo_root: pathlib.Path | str, run_dir: pathlib.Path | str
) -> ExecutorDispatch:
    """Derive the product executor's dispatch from the run directory's committed state.

    The run id is the run directory's own name — the run template's layout
    (`assurance/runs/<run-id>/`) makes the name part of the one committed path that exists
    at dispatch time — and the revision is the last commit touching the instruction, which
    is its freeze. Drift between the worktree bytes and that frozen blob is refused, not
    smoothed: an executor reading bytes nobody froze is the mis-route this mode can see.
    """
    repo_root = pathlib.Path(repo_root)
    charter = instrument_relative(repo_root, EXECUTOR_ROLE_INSTRUCTION)
    rules = declared_rules(repo_root)

    def refused(issue: Issue) -> ExecutorDispatch:
        return ExecutorDispatch(
            str(run_dir), None, None, None, report_of([issue]), charter, rules
        )

    root = pathlib.Path(run_dir)
    if not root.is_absolute():
        root = repo_root / root
    try:
        rel = root.resolve().relative_to(repo_root.resolve())
    except ValueError:
        return refused(
            Issue(
                f"{CODE}-RUN-OUTSIDE-REPO",
                f"{run_dir} does not resolve inside {repo_root}, so no committed fact "
                "about it can be derived",
                "run_dir",
            )
        )
    instruction_rel = (rel / "instruction.md").as_posix()
    if not (root / "instruction.md").is_file():
        return refused(
            Issue(
                f"{CODE}-INSTRUCTION-MISSING",
                f"{instruction_rel} does not exist; an executor is dispatched from a run "
                "directory holding its frozen instruction, and this one holds none",
                "run_dir",
            )
        )
    logged = subprocess.run(
        ["git", "-C", str(repo_root), "log", "-1", "--format=%H", "--", instruction_rel],
        check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    revision = logged.stdout.decode("utf-8", errors="replace").strip()
    if logged.returncode != 0 or len(revision) != 40:
        return refused(
            Issue(
                f"{CODE}-INSTRUCTION-UNFROZEN",
                f"no commit touches {instruction_rel}, so the instruction is not frozen; "
                "freeze it first, then dispatch",
                "instruction",
            )
        )
    # Blob-id equality, filters applied — a byte comparison would false-positive on eol
    # conversion, and `git hash-object` hashes the file as an add would stage it.
    frozen = subprocess.run(
        ["git", "-C", str(repo_root), "rev-parse", f"{revision}:{instruction_rel}"],
        check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    on_disk = subprocess.run(
        ["git", "-C", str(repo_root), "hash-object", instruction_rel],
        check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    if (
        frozen.returncode != 0
        or on_disk.returncode != 0
        or frozen.stdout.strip() != on_disk.stdout.strip()
    ):
        return refused(
            Issue(
                f"{CODE}-INSTRUCTION-DRIFTED",
                f"{instruction_rel} on disk differs from its frozen bytes at "
                f"{revision[:12]}; an executor dispatched now would read bytes nobody "
                "froze",
                "instruction",
            )
        )
    return ExecutorDispatch(
        run_dir=str(run_dir),
        run_id=rel.name,
        instruction_path=instruction_rel,
        revision=revision,
        report=report_of([]),
        charter=charter,
        declared_rules=rules,
    )


def render_executor_dispatch(dispatch: ExecutorDispatch) -> str:
    """The executor-facing prompt: the charter and the three facts. Nothing else."""
    if not dispatch.report.ok:
        lines = [
            "# NOT DISPATCHABLE",
            "",
            "The run directory given does not hand an executor a frozen instruction, so",
            "no dispatch was produced. Resolve the following, then re-run.",
            "",
        ]
        lines += [f"- {issue.render()}" for issue in dispatch.report.issues]
        return "\n".join(lines) + "\n"
    return EXECUTOR_PROMPT.format(
        charter=dispatch.charter or EXECUTOR_ROLE_INSTRUCTION,
        declared_rules=declared_rules_line(dispatch.declared_rules),
        run_id=dispatch.run_id,
        instruction_path=dispatch.instruction_path,
        revision=dispatch.revision,
    )


def render_executor_derivation(dispatch: ExecutorDispatch) -> str:
    """The dispatcher's view: which run, which frozen instruction."""
    lines = [
        f"derived run       : {_value(dispatch.run_id)} (executor dispatch)",
        f"  instruction     : {_value(dispatch.instruction_path)} @ {_value(dispatch.revision)}",
    ]
    for issue in dispatch.report.issues:
        lines.append("  ! " + issue.render())
    return "\n".join(lines)


__all__ = [
    "DECLARED_RULES_ABSENT_LINE",
    "DECLARED_RULES_LINE",
    "DISPATCHABLE_STATUS",
    "Dispatch",
    "EXECUTOR_PROMPT",
    "EXECUTOR_ROLE_INSTRUCTION",
    "ExecutorDispatch",
    "FREEZE_MARKER",
    "RESULT_SCHEMA",
    "ROLE_INSTRUCTION",
    "VERDICTS",
    "control_root_of",
    "declared_rules",
    "declared_rules_line",
    "declared_rules_phrase",
    "dispatch_of",
    "executor_dispatch_of",
    "instrument_relative",
    "render_derivation",
    "render_dispatch",
    "render_executor_derivation",
    "render_executor_dispatch",
    "resolve_subject",
    "role_for",
    "write_freeze_marker",
]
