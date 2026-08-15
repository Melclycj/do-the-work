"""ObligationCoverage — a disposable, byte-rebuildable join (plan §4).

Coverage is not a stored owner. It is recomputed from four sources that each have their own
owner, and it may be deleted at any time:

    WorkSpec.obligation_id
    + FulfillmentReport.implementation_locators
    + CheckResult.evidence_refs
    + ReviewResult.per_obligation_disposition
    -> coverage row

The fourth input does not exist yet. V3-N1 stops before semantic review, so the rows below
carry three columns and the review disposition is deliberately absent rather than stubbed:
an empty "review" column would read as "reviewed, nothing found", which is precisely the
unsupported-completion claim this product exists to prevent. V3-N2 adds the column.

The join is also where wrong-candidate evidence becomes visible. Each owner records the
candidate it observed; only when the rows are assembled does it show that a check certified
a different candidate than the one being reported on.
"""
from __future__ import annotations

from typing import Any, Mapping, Sequence

from rsclib.document_harness import Issue, Report, report_of

CODE = "V3-COVERAGE"


def coverage_rows(
    spec: Mapping[str, Any],
    record: Mapping[str, Any],
    results: Sequence[Mapping[str, Any]] = (),
) -> list[dict[str, Any]]:
    """One row per declared obligation, in WorkSpec order."""
    claims = {claim["obligation_id"]: claim for claim in record["fulfillment"]["claims"]}
    by_check = {result["check_id"]: result for result in results}
    artifact_presence = {
        entry["artifact_id"]: entry["present"]
        for entry in record["manifest"]["expected_artifact_results"]
    }

    rows: list[dict[str, Any]] = []
    for obligation in spec["obligations"]:
        obligation_id = obligation["obligation_id"]
        claim = claims.get(obligation_id)
        row: dict[str, Any] = {
            "obligation_id": obligation_id,
            "verification_mode": obligation["verification_mode"],
            "fulfillment_status": claim["status"] if claim else "NO_CLAIM",
            # 'path :: anchor', not 'path#anchor': a Markdown anchor usually starts with
            # '#' itself, and the concatenated form reads as a broken fragment.
            "implementation_locators": [
                f"{loc['path']} :: {loc['anchor']}"
                for loc in (claim or {}).get("implementation_locators", [])
            ],
            "checks": [
                {
                    "check_id": check_id,
                    "result": by_check[check_id]["result"] if check_id in by_check else "NO_RESULT",
                }
                for check_id in obligation.get("local_check_refs", [])
            ],
            "expected_artifacts": [
                {"artifact_id": artifact_id, "present": artifact_presence.get(artifact_id, False)}
                for artifact_id in obligation.get("expected_artifact_ids", [])
            ],
        }
        rows.append(row)
    return rows


def coverage_report(
    spec: Mapping[str, Any],
    record: Mapping[str, Any],
    results: Sequence[Mapping[str, Any]] = (),
) -> Report:
    """Invariant 8 and the wrong-candidate class (N1-A6, N1-A9)."""
    issues: list[Issue] = []
    by_check = {result["check_id"]: result for result in results}
    candidate_commit = record["candidate_ref"].get("commit")

    for obligation in spec["obligations"]:
        obligation_id = obligation["obligation_id"]
        if obligation["verification_mode"] != "local_check":
            continue
        refs = obligation.get("local_check_refs", [])
        for check_id in refs:
            result = by_check.get(check_id)
            if result is None:
                issues.append(
                    Issue(
                        f"{CODE}-NO-EVIDENCE",
                        f"deterministic obligation binds check '{check_id}' but no CheckResult exists",
                        obligation_id,
                    )
                )
                continue
            if result["result"] != "PASS":
                issues.append(
                    Issue(
                        f"{CODE}-CHECK-NOT-PASSED",
                        f"check '{check_id}' returned {result['result']}: "
                        f"{result.get('detail', 'no detail recorded')}",
                        obligation_id,
                    )
                )

    # Ownership (N1-A7): a deterministic verifier owns its CheckResult and the executor can
    # never author one. The manifest half of this rule is enforced on the record itself; the
    # CheckResult half can only be seen here, where the executor's identity and the results
    # meet for the first time.
    executor = record["fulfillment"]["authored_by"].strip().casefold()
    for result in results:
        if result["verified_by"].strip().casefold() == executor:
            issues.append(
                Issue(
                    f"{CODE}-EXECUTOR-AUTHORED-RESULT",
                    f"check '{result['check_id']}' was authored by the executor of the same run: "
                    f"{result['verified_by']}",
                    result["check_id"],
                )
            )

    # Wrong-candidate evidence: a result that certified other bytes than the record reports on.
    for result in results:
        observed = result["candidate_ref"].get("commit")
        if candidate_commit and observed and observed != candidate_commit:
            issues.append(
                Issue(
                    f"{CODE}-WRONG-CANDIDATE",
                    f"check '{result['check_id']}' certified candidate {observed[:12]} but the "
                    f"record reports on {candidate_commit[:12]}",
                    result["check_id"],
                )
            )
        if result["result"] == "WRONG_SUBJECT":
            issues.append(
                Issue(
                    f"{CODE}-WRONG-SUBJECT",
                    f"check '{result['check_id']}' observed the "
                    f"{result['observed_tree']['kind']}, which does not certify the candidate",
                    result["check_id"],
                )
            )

    return report_of(issues)


def mode_summary(rows: Sequence[Mapping[str, Any]]) -> dict[str, int]:
    """The verification-mode ratio, counted from the rows themselves.

    Wave 1 of the special-case bucket design (§5): the per-row `verification_mode` column
    was always present, but nobody was asked to look at it — at V3-N3 63% of obligations
    were `review_only` and the run's one real defect sat among them, unnoticed until a
    reviewer hand-counted. This is visibility only: a number the user sees, never a gate,
    threshold or blocker.
    """
    return {
        "total": len(rows),
        "review_only": sum(1 for row in rows if row["verification_mode"] == "review_only"),
        "bind_checks": sum(1 for row in rows if row["checks"]),
    }


def mode_summary_line(rows: Sequence[Mapping[str, Any]]) -> str:
    """One line for any decision surface that shows this coverage (START, coverage view)."""
    summary = mode_summary(rows)
    return (
        f"{summary['review_only']} of {summary['total']} obligations review_only · "
        f"{summary['bind_checks']} bind checks"
    )


def render_coverage(rows: Sequence[Mapping[str, Any]]) -> str:
    """A user-facing table. Reports show exceptions, not a wall of green (plan §6)."""
    lines = [
        mode_summary_line(rows),
        f"{'obligation':<28} {'mode':<24} {'fulfillment':<16} checks",
        "-" * 100,
    ]
    for row in rows:
        checks = ", ".join(f"{c['check_id']}={c['result']}" for c in row["checks"]) or "-"
        lines.append(
            f"{row['obligation_id']:<28} {row['verification_mode']:<24} "
            f"{row['fulfillment_status']:<16} {checks}"
        )
        for locator in row["implementation_locators"]:
            lines.append(f"{'':<28} -> {locator}")
        for artifact in row["expected_artifacts"]:
            if not artifact["present"]:
                lines.append(f"{'':<28} !! missing artifact: {artifact['artifact_id']}")
    return "\n".join(lines)


def coverage_document(
    spec: Mapping[str, Any],
    record: Mapping[str, Any],
    results: Sequence[Mapping[str, Any]] = (),
) -> dict[str, Any]:
    """The disposable coverage artifact, carrying no verdict of its own.

    It binds the identities it joined so a reader can tell what it was built from, and it
    reports issues as data. It never converts a set of passing checks into a statement that
    the work is correct — coverage is an accounting of evidence, not a conclusion.
    """
    return {
        "work_id": spec["work_id"],
        "run_id": record["run_id"],
        "candidate_ref": dict(record["candidate_ref"]),
        "repair_round": record["repair_round"],
        "rows": coverage_rows(spec, record, results),
        "issues": [
            {"code": issue.code, "where": issue.where, "message": issue.message}
            for issue in coverage_report(spec, record, results).issues
        ],
        "review_disposition": "NOT_YET_REVIEWED",
    }
