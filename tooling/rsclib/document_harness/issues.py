"""HarnessIssue and its triage — growth strictly after the run (V3-D10, N2-A10, N2-A11).

A harness that could improve itself mid-run would be changing the thing under assurance while
assuring it. So the boundary here is temporal and absolute: an issue is *observed* after a run
reaches a terminal status, **a written issue is never edited**, and it changes nothing about
the run it came from — not the WorkSpec, not the plan, not a check, not a verdict.

That middle clause is an obligation on whoever writes here, not a property of the system.
Nothing enforces it: the file is ordinary text in the working tree, and this module offers no
edit path only because it declines to, not because one is unavailable. It once read "it is
immutable once written", which asserted as fact something no code checks — the wording was
corrected on 2026-07-29 rather than answered by building an enforcement mechanism, because a
rule stated as a fact is the defect, and adding machinery to make the false sentence true
would be guarding the wrong thing.

The part worth stating plainly is what is **absent**. There is no state field, no resolution,
no dedup key, no lifecycle and no automatic maintenance stage (N2-A11). Routing an issue is a
user `ISSUE_TRIAGE` decision, which is a separate document in a separate phase — so the route
lives with the person who chose it, not as mutable state on the observation. An issue that
carried its own status would become a work-tracking system inside an assurance harness, and
the first thing such a system does is acquire a way to close items without evidence.

`triage_route` therefore *reads* a decision and returns where it points. Nothing in this
module writes back onto the issue, and there is deliberately no function that does.
"""
from __future__ import annotations

import pathlib
from typing import Any, Mapping  # Mapping is also used as a runtime type guard

from rsclib.document_harness import (
    Issue,
    Report,
    SpecGap,
    canonical_digest,
    load_json,
    report_of,
    validate,
)
from rsclib.document_harness.flow import TERMINAL_STATUSES
from rsclib.document_harness.review import validate_n2

CODE = "V3-HARNESS-ISSUE"

#: The closed triage routes (contract §5/§11). Order is the routing preference the contract
#: states: workflow-local first, profile only after witnessed reuse, verifier/reviewer
#: implementation when the defect is local, core only for shared ownership/invariant defects.
TRIAGE_ROUTES = (
    "WORKFLOW_FIX",
    "DOCUMENT_ASSURANCE_PROFILE_CANDIDATE",
    "VERIFIER_FIX",
    "CORE_CANDIDATE",
    "DEFER",
    "DISMISS",
)


def record_issue(
    *,
    issue_id: str,
    work_id: str,
    run_id: str,
    kind: str,
    statement: str,
    evidence_refs: list[Mapping[str, Any]],
    observed_after: str,
    observed_by: str,
    observed_at: str | None = None,
) -> dict[str, Any]:
    """Build one observation (the caller persists it). Complete when written; never amend it."""
    issue: dict[str, Any] = {
        "issue_id": issue_id,
        "work_id": work_id,
        "run_id": run_id,
        "kind": kind,
        "statement": statement,
        "evidence_refs": [dict(ref) for ref in evidence_refs],
        "observed_after": observed_after,
        "observed_by": observed_by,
    }
    if observed_at:
        issue["observed_at"] = observed_at
    return issue


def check_issue(issue: Mapping[str, Any], state: Mapping[str, Any] | None = None) -> Report:
    """N2-A10: the issue is post-run, evidence-linked, and binds the run it came from.

    When the live `state` is supplied the strongest form of the rule is checked: the run must
    actually have reached a terminal status. Without it, only the issue's own declaration can
    be read — and that gap is **reported rather than assumed away**, because "the run really
    was over" is exactly the property an issue could otherwise assert about itself.
    """
    schema_report = validate_n2("harness_issue", issue)
    if not schema_report.ok:
        return schema_report

    issues: list[Issue] = []

    if state is None:
        issues.append(
            Issue(
                f"{CODE}-RUN-STATE-UNVERIFIED",
                "no run state was supplied, so the claim that this issue was observed after the "
                "run ended was not checked against the run; this is an unverified property, not a "
                "satisfied one",
                "observed_after",
            )
        )
        return schema_report + report_of(issues)

    if "run_id" not in state or "status" not in state:
        # A malformed state is reported, never dereferenced: raising here would take the run
        # down instead of recording that the post-run claim could not be checked.
        issues.append(
            Issue(
                f"{CODE}-RUN-STATE-UNVERIFIED",
                "the supplied run state carries no run_id or status, so the post-run claim could "
                "not be checked against it; this is an unverified property, not a satisfied one",
                "observed_after",
            )
        )
        return schema_report + report_of(issues)

    if state["run_id"] != issue["run_id"]:
        issues.append(
            Issue(
                f"{CODE}-RUN-MISMATCH",
                f"the issue names run '{issue['run_id']}' but the supplied state is for "
                f"'{state['run_id']}'",
                "run_id",
            )
        )
        return schema_report + report_of(issues)

    if state["status"] not in TERMINAL_STATUSES:
        issues.append(
            Issue(
                f"{CODE}-RUN-STILL-LIVE",
                f"the run is at status {state['status']}, which is not terminal; an issue recorded "
                "against a live run could influence the run it is about",
                "observed_after",
            )
        )
    elif issue["observed_after"] != state["status"]:
        issues.append(
            Issue(
                f"{CODE}-TERMINAL-STATUS-MISMATCH",
                f"the issue says it was observed after {issue['observed_after']} but the run ended "
                f"at {state['status']}",
                "observed_after",
            )
        )

    return schema_report + report_of(issues)


def check_triage(decision: Mapping[str, Any], issue: Mapping[str, Any]) -> Report:
    """Only a post-run user decision routes an issue (V3-D10, contract §11)."""
    # --- run FIRST and unconditionally ---
    #
    # The user-decision schema's ISSUE_TRIAGE conditional already narrows `decision` to the
    # six routes and requires `target.harness_issue_ref.path`, so validating first would leave
    # both codes below permanently unreachable — the V3-N1 D3 shape, which `summary.py` was
    # corrected for and this module initially was not. Reported here so a bad route says which
    # route was bad, rather than surfacing as a generic schema error. Accessors are defensive
    # because this runs before the shape is known.
    issues: list[Issue] = []
    phase = decision.get("phase")
    if phase != "ISSUE_TRIAGE":
        return report_of(
            [Issue(f"{CODE}-PHASE", f"expected an ISSUE_TRIAGE decision, got {phase}", "phase")]
        )
    if decision.get("decision") not in TRIAGE_ROUTES:
        issues.append(
            Issue(
                f"{CODE}-UNKNOWN-ROUTE",
                f"'{decision.get('decision')}' is not one of the closed triage routes",
                "decision",
            )
        )
    target = decision.get("target")
    target_path = (
        target.get("harness_issue_ref", {}).get("path") if isinstance(target, Mapping) else None
    )
    if not target_path:
        issues.append(
            Issue(
                f"{CODE}-UNBOUND-TRIAGE",
                "the triage decision does not point at an issue document",
                "target/harness_issue_ref",
            )
        )
    else:
        # p3-corr triaged five issues of one work in a single pass, so `work_id` alone cannot
        # say WHICH issue a decision routes: a decision made about a sibling issue must not
        # read as this issue's routing. The one cross-check that needs no new I/O is the file
        # the target names against the in-hand issue's own identity.
        target_name = str(target_path).replace("\\", "/").rsplit("/", 1)[-1]
        issue_id = issue.get("issue_id")
        if not issue_id or target_name != f"{issue_id}.json":
            issues.append(
                Issue(
                    f"{CODE}-TARGET-MISMATCH",
                    f"the triage decision's target names '{target_name}', which is not the "
                    f"in-hand issue '{issue_id}' — a decision about a different issue must "
                    "not read as this issue's routing",
                    "target/harness_issue_ref/path",
                )
            )
    if decision.get("work_id") != issue.get("work_id"):
        issues.append(
            Issue(
                f"{CODE}-WORK-MISMATCH",
                "the triage decision names a different work_id than the issue it routes",
                "work_id",
            )
        )
    # L-2 (FULL 34cf85b): work_id and target filename bind the work and issue dimensions,
    # but two runs of one work can each hold a same-named issue. Compare runs when both
    # documents name one — the field is optional on the decision side of the schema.
    decision_run = decision.get("run_id")
    issue_run = issue.get("run_id")
    if decision_run and issue_run and decision_run != issue_run:
        issues.append(
            Issue(
                f"{CODE}-TRIAGE-RUN-MISMATCH",
                f"the triage decision was made in run '{decision_run}' but the in-hand issue "
                f"belongs to run '{issue_run}' — a decision routes only its own run's issue",
                "run_id",
            )
        )

    schema_report = validate("decision", decision)
    return schema_report + report_of(issues)


def triage_route(decision: Mapping[str, Any]) -> str:
    """Read where a triage decision points. Nothing is written back onto the issue.

    The absence of a writer here is the design, not an omission: an issue is an observation,
    and an observation that acquires a mutable status becomes a lifecycle (N2-A11).
    """
    if decision.get("phase") != "ISSUE_TRIAGE":
        raise SpecGap(f"{CODE}-PHASE not an ISSUE_TRIAGE decision: {decision.get('phase')}")
    return decision["decision"]


def issue_digest(issue: Mapping[str, Any]) -> str:
    return canonical_digest(issue)


def render_issue(issue: Mapping[str, Any]) -> str:
    lines = [
        f"issue        : {issue['issue_id']} ({issue['kind']})",
        f"run          : {issue['run_id']}, observed after {issue['observed_after']}",
        f"observed_by  : {issue['observed_by']}",
        f"statement    : {issue['statement']}",
    ]
    for ref in issue["evidence_refs"]:
        lines.append(f"  -> evidence: {ref['path']}")
    lines.append("  (routing is a separate user ISSUE_TRIAGE decision; this document has none)")
    return "\n".join(lines)


def load_issue(path: pathlib.Path | str) -> dict[str, Any]:
    return load_json(path)


__all__ = [
    "TRIAGE_ROUTES",
    "check_issue",
    "check_triage",
    "issue_digest",
    "load_issue",
    "record_issue",
    "render_issue",
    "triage_route",
]
