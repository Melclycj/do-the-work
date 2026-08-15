"""Bounded semantic review: the frozen package and the reviewer's result (V3-D6, N2-A1..A3).

Review in v3 is bounded, non-recursive and answerable for exactly one frozen subject. Three
disciplines are enforced here rather than trusted.

**The subject is frozen, and it is the actual work.** A ReviewPackage binds the raw
instruction, the sources, the plan, the actual candidate artifacts, the fulfillment, the
manifest, the checks and the coverage — by exact revision, locator and digest, never by
copying bytes (invariant 9). The failure this prevents is a reviewer handed a summary of the
work instead of the work: the summary is written by the executor, so reviewing it checks
whether the executor described its own output consistently, which is not a review of anything.
An executor summary may ride along, but it can never stand in for a member (N2-A1).

**A verdict binds its package.** A ReviewResult that does not name the exact package it
answers for could be re-attributed to a different candidate later — the same "check candidate
A, report candidate B" class the digests elsewhere exist to close (V3-D5).

**An unchecked property reports itself.** `check_review_result` takes `executor` as an
optional argument, and omitting it yields `V3-REVIEW-REVIEWER-DISTINCTNESS-UNVERIFIED` rather
than silence. This shape is deliberate and copied from N1's `instruction.check_audit`, where
the same guard was originally off by default: omitting an argument silently disabled it, and
a guard that does not run must never be reported as one that passed.

Nothing here issues a verdict. The reviewer owns `ReviewResult`; this module validates that
what the reviewer produced is well-formed, complete against the WorkSpec, and bound to the
thing it claims to have reviewed.
"""
from __future__ import annotations

import functools
import pathlib
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

from rsclib.document_harness import (
    SCHEMA_DIR,
    SCHEMA_FILES,
    SCHEMA_URI_BASE,
    AssuranceFault,
    Issue,
    Report,
    SpecGap,
    bytes_digest,
    canonical_digest,
    load_json,
    report_of,
)
from rsclib.document_harness.candidate import CandidateTreeReader

CODE = "V3-REVIEW"
PACKAGE_CODE = "V3-PACKAGE"

#: Roles the schema requires unconditionally. Recorded here too because the completeness
#: rules below distinguish them from the two conditional roles.
REQUIRED_ROLES = (
    "raw_instruction",
    "resolved_plan",
    "candidate_artifact",
    "fulfillment",
    "manifest",
    "coverage",
)


# ---------------------------------------------------------------------------
# The V3-N2 schema extension
# ---------------------------------------------------------------------------
#
# `validate()` in the package root can only reach the schemas registered in
# `__init__.SCHEMA_FILES` — ten as of W1 (2026-07-22), when that successor round
# registered WorkSpec v2 there under its own user-adjudicated allowlist (W1 record §6). The plan fixes each *node's*
# module list by name, so `__init__.py` was frozen when V3-N1 closed and no later node may
# write it. Registering the three V3-N2 schemas there was therefore an out-of-boundary
# write for V3-N2, not a tidier one.
#
# The in-boundary route is this local registry, built from the *public* exports
# (`SCHEMA_DIR`, `SCHEMA_FILES`, `SCHEMA_URI_BASE`) so it stays in step with the frozen pack
# instead of restating it. It costs a duplicated registry that would otherwise have been one
# line in a dict; that cost is recorded in the V3-N2 node record rather than hidden here.
#
# It fails closed on an unknown kind, exactly as the root validator does.

N2_SCHEMA_FILES: dict[str, str] = {
    "review_package": "review.schema.json",
    "assurance_candidate": "assurance.schema.json",
    "harness_issue": "harness-issue.schema.json",
}

N2_SCHEMA_POINTERS: dict[str, str] = {
    "review_result": "review.schema.json#/$defs/reviewResult",
    "assurance_summary": "assurance.schema.json#/$defs/assuranceSummary",
}


@functools.lru_cache(maxsize=1)
def _n2_registry() -> Registry:
    resources = []
    for filename in (*SCHEMA_FILES.values(), *N2_SCHEMA_FILES.values()):
        path = SCHEMA_DIR / filename
        if not path.exists():
            raise AssuranceFault(f"schema pack is incomplete: missing {path}")
        resources.append((SCHEMA_URI_BASE + filename, Resource.from_contents(load_json(path))))
    return Registry().with_resources(resources)


@functools.lru_cache(maxsize=None)
def _n2_validator(kind: str) -> Draft202012Validator:
    if kind in N2_SCHEMA_FILES:
        schema = load_json(SCHEMA_DIR / N2_SCHEMA_FILES[kind])
        Draft202012Validator.check_schema(schema)
        return Draft202012Validator(schema, registry=_n2_registry())
    if kind in N2_SCHEMA_POINTERS:
        return Draft202012Validator(
            {"$ref": SCHEMA_URI_BASE + N2_SCHEMA_POINTERS[kind]}, registry=_n2_registry()
        )
    raise SpecGap(f"unknown document kind: {kind}")


def validate_n2(kind: str, document: Mapping[str, Any]) -> Report:
    """Validate one V3-N2 document against its closed schema."""
    errors = sorted(_n2_validator(kind).iter_errors(document), key=lambda error: list(error.path))
    return report_of(
        Issue(
            f"V3-SCHEMA-{kind.upper()}",
            error.message[:300],
            "/".join(str(part) for part in error.path) or "<root>",
        )
        for error in errors
    )


def require_valid_n2(kind: str, document: Mapping[str, Any]) -> None:
    validate_n2(kind, document).require(SpecGap)


# ---------------------------------------------------------------------------
# Package construction
# ---------------------------------------------------------------------------


def member(
    member_id: str,
    role: str,
    path: str,
    digest_sha256: str,
    *,
    revision: str | None = None,
    locator: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """One package member. The ref binds bytes; it never carries them."""
    ref: dict[str, Any] = {"path": path, "digest_sha256": digest_sha256}
    if revision:
        ref["revision"] = revision
    entry: dict[str, Any] = {"member_id": member_id, "role": role, "ref": ref}
    if locator:
        entry["locator"] = dict(locator)
    return entry


def freeze_package(
    *,
    package_id: str,
    work_id: str,
    run_id: str,
    repair_round: int,
    review_round: str,
    candidate_ref: Mapping[str, Any],
    base_revision: str,
    frozen_by: str,
    members: Sequence[Mapping[str, Any]],
    frozen_at: str | None = None,
    executor_summary_ref: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Freeze the review subject. Freezing binds what is reviewed; it judges nothing."""
    package: dict[str, Any] = {
        "package_id": package_id,
        "work_id": work_id,
        "run_id": run_id,
        "repair_round": repair_round,
        "review_round": review_round,
        "candidate_ref": dict(candidate_ref),
        "base_revision": base_revision,
        "frozen_by": frozen_by,
        "members": [dict(entry) for entry in members],
    }
    if frozen_at:
        package["frozen_at"] = frozen_at
    if executor_summary_ref:
        package["executor_summary_ref"] = dict(executor_summary_ref)
    return package


def package_digest(package: Mapping[str, Any]) -> str:
    return canonical_digest(package)


def members_by_role(package: Mapping[str, Any], role: str) -> list[dict[str, Any]]:
    return [entry for entry in package["members"] if entry["role"] == role]


# ---------------------------------------------------------------------------
# Package invariants (N2-A1)
# ---------------------------------------------------------------------------


def check_package(
    package: Mapping[str, Any],
    spec: Mapping[str, Any],
    record: Mapping[str, Any],
    results: Sequence[Mapping[str, Any]],
) -> Report:
    """Invariant 9: the package must be the actual work, completely (N2-A1).

    The schema holds the six unconditional roles and the absence of any content-bearing
    field. What only this function can see is *completeness against the run*: whether every
    declared input, every present expected artifact and every CheckResult that exists is
    actually in the package. A package that satisfies the schema while omitting half the
    check results is a subject the reviewer cannot judge the candidate from.

    `results` is **required with no default**, deliberately. It began as `results = ()`, which
    is the fail-open shape N1 found twice: omitting the argument silently disabled the
    check-completeness guard, and a package missing every CheckResult reported clean. Unlike
    N1's `executor` case the unchecked state cannot be *reported* here, because an empty
    sequence is legitimately meaningful — a run whose obligations are all `review_only`
    produces no results at all — so "none exist" and "the caller did not say" are
    indistinguishable once the call is made. The ambiguity therefore has to be removed at the
    call site rather than described afterwards: pass `[]` to mean the run had no checks.
    """
    schema_report = validate_n2("review_package", package)
    if not schema_report.ok:
        return schema_report

    issues: list[Issue] = []

    if package["work_id"] != spec["work_id"]:
        issues.append(
            Issue(f"{PACKAGE_CODE}-WORK-MISMATCH", "package names a different work_id", "work_id")
        )
    if package["run_id"] != record["run_id"]:
        issues.append(
            Issue(f"{PACKAGE_CODE}-RUN-MISMATCH", "package names a different run_id", "run_id")
        )
    if package["repair_round"] != record["repair_round"]:
        issues.append(
            Issue(
                f"{PACKAGE_CODE}-ROUND-MISMATCH",
                f"package froze repair round {package['repair_round']} but the record is round "
                f"{record['repair_round']}",
                "repair_round",
            )
        )

    package_commit = package["candidate_ref"].get("commit")
    record_commit = record["candidate_ref"].get("commit")
    if not record_commit:
        # `candidateRef` requires only a branch, so a record can arrive naming no commit at
        # all. Skipping the comparison there would make the strongest identity check in this
        # function disappear exactly when the record is weakest — reported instead.
        issues.append(
            Issue(
                f"{PACKAGE_CODE}-RECORD-CANDIDATE-UNBOUND",
                "the record's candidate names no commit, so the package's candidate could not "
                "be compared against it; a branch name follows the branch as it moves",
                "candidate_ref/commit",
            )
        )
    elif package_commit != record_commit:
        issues.append(
            Issue(
                f"{PACKAGE_CODE}-WRONG-CANDIDATE",
                f"package froze candidate {str(package_commit)[:12]} but the record reports on "
                f"{record_commit[:12]}",
                "candidate_ref/commit",
            )
        )
    if package["candidate_ref"].get("branch") != record["candidate_ref"].get("branch"):
        issues.append(
            Issue(
                f"{PACKAGE_CODE}-CANDIDATE-BRANCH-MISMATCH",
                f"package froze branch '{package['candidate_ref'].get('branch')}' but the record "
                f"names '{record['candidate_ref'].get('branch')}'",
                "candidate_ref/branch",
            )
        )
    if record.get("base_revision") and package["base_revision"] != record["base_revision"]:
        issues.append(
            Issue(
                f"{PACKAGE_CODE}-BASE-MISMATCH",
                f"package was frozen against base {package['base_revision'][:12]} but the record "
                f"was built against {record['base_revision'][:12]}; the diff behind them is not "
                "the same diff",
                "base_revision",
            )
        )

    # --- conditional role completeness: every declared input is a member ---
    declared_inputs = {entry["path"] for entry in spec.get("inputs", [])}
    member_input_paths = {entry["ref"]["path"] for entry in members_by_role(package, "source_input")}
    for missing in sorted(declared_inputs - member_input_paths):
        issues.append(
            Issue(
                f"{PACKAGE_CODE}-INPUT-OMITTED",
                f"WorkSpec declares source input '{missing}' but the package does not include it",
                "members",
            )
        )

    # --- every CheckResult the run produced is a member ---
    #
    # Compared by COUNT, and the limit is stated rather than glossed: a CheckResult document
    # does not carry its own storage path, so this function cannot match member to result by
    # identity the way it does for source inputs. It therefore catches the wrong *number* of
    # results — including the partial omission an earlier version missed, which only fired
    # when every result was absent — but not a swap of one result for another. Closing that
    # would mean either putting a path inside a CheckResult, which duplicates a canonical fact
    # (N0-A6), or passing the result paths in, which the caller cannot be trusted to do
    # completely for the same reason this check exists.
    member_check_paths = {entry["ref"]["path"] for entry in members_by_role(package, "check_result")}
    if len(member_check_paths) != len(results):
        issues.append(
            Issue(
                f"{PACKAGE_CODE}-CHECKS-OMITTED",
                f"the run produced {len(results)} CheckResult(s) but the package includes "
                f"{len(member_check_paths)}",
                "members",
            )
        )

    # --- every expected artifact that is present must be an actual candidate artifact ---
    artifact_paths = {artifact["artifact_id"]: artifact["path"] for artifact in spec["expected_artifacts"]}
    member_artifact_paths = {
        entry["ref"]["path"] for entry in members_by_role(package, "candidate_artifact")
    }
    for entry in record["manifest"]["expected_artifact_results"]:
        if not entry["present"]:
            continue  # an absent artifact cannot be a member; the manifest already says so
        path = artifact_paths.get(entry["artifact_id"])
        if path and path not in member_artifact_paths:
            issues.append(
                Issue(
                    f"{PACKAGE_CODE}-ARTIFACT-OMITTED",
                    f"expected artifact '{entry['artifact_id']}' is present in the candidate but "
                    "is not an actual subject in the package",
                    "members",
                )
            )

    # --- the raw instruction member must be the frozen instruction the WorkSpec names ---
    #
    # Path AND revision. Comparing paths alone would accept a *different revision of the same
    # file*, which is precisely how a reviewer ends up rechecking completeness against an
    # instruction that was edited after the work was scoped.
    frozen = spec["instruction_ref"]
    instruction_members = [
        entry["ref"] for entry in members_by_role(package, "raw_instruction")
    ]
    if not any(
        ref["path"] == frozen["path"] and ref.get("revision") == frozen.get("revision")
        for ref in instruction_members
    ):
        issues.append(
            Issue(
                f"{PACKAGE_CODE}-INSTRUCTION-SUBSTITUTED",
                f"the package's raw instruction is not the exact one the WorkSpec froze "
                f"({frozen['path']} @ {str(frozen.get('revision'))[:12]}); found "
                + (
                    ", ".join(
                        f"{ref['path']} @ {str(ref.get('revision'))[:12]}"
                        for ref in instruction_members
                    )
                    or "none"
                ),
                "members",
            )
        )

    return schema_report + report_of(issues)


def verify_member_bytes(package: Mapping[str, Any], repo_root: pathlib.Path | str) -> Report:
    """Recompute each member's digest against real bytes, **in the tree the member pins**.

    A package binds bytes by digest; nothing in the binding proves the bytes still match.
    This is the check that turns the binding into evidence, and it is deliberately separate
    from `check_package` because it needs trees while the invariants above do not.

    **Each revision-bearing member is read from its own revision.** An earlier version took a
    single `reader` and pushed every such member through it, never comparing `ref["revision"]`
    with the tree actually read — which was wrong in both directions and wrong by design:

    * a member pinning the base revision but carrying the candidate's digest verified clean,
      while the *correct* base digest was reported stale. That is the "check candidate A,
      report candidate B" class V3-D5 exists to close, reached through the verifier itself;
    * a package whose members legitimately span two trees — the instruction and sources frozen
      at the base, the artifacts at the candidate — could not be verified correctly at all,
      because whichever tree the caller passed, the other group was checked against the wrong
      one. That is the normal shape of a package, not an edge case;
    * and a `WorktreeReader` was accepted for a revision-pinned member, so uncommitted bytes
      that exist in **no committed tree** could certify a member naming an exact revision —
      the N1 R1 lesson, which `candidate.check_locators` already refuses.

    Reading each member through `CandidateTreeReader(repo_root, ref["revision"])` removes all
    three at once, and removes the fail-open `reader` argument with them: there is no longer a
    parameter whose omission could downgrade the check. Members with no revision are control
    documents in the control root and are read from disk.
    """
    root = pathlib.Path(repo_root)
    issues: list[Issue] = []
    seen_ids: set[str] = set()

    for entry in package["members"]:
        member_id = entry["member_id"]
        if member_id in seen_ids:
            issues.append(
                Issue(
                    f"{PACKAGE_CODE}-DUPLICATE-MEMBER-ID",
                    f"member_id '{member_id}' occurs more than once, so an issue reported "
                    "against it does not identify which member it is about",
                    member_id,
                )
            )
        seen_ids.add(member_id)

        ref = entry["ref"]
        if "revision" in ref:
            # Read out of the exact commit the member pins, never off disk and never through
            # a tree chosen by the caller.
            raw = CandidateTreeReader(root, ref["revision"]).read(ref["path"])
            where = f"{ref['path']} @ {ref['revision'][:12]}"
        else:
            target = root / ref["path"]
            raw = target.read_bytes() if target.is_file() else None
            where = ref["path"]

        if raw is None:
            issues.append(
                Issue(
                    f"{PACKAGE_CODE}-MEMBER-MISSING",
                    f"package member does not resolve: {where}",
                    member_id,
                )
            )
            continue
        if bytes_digest(raw) != ref["digest_sha256"]:
            issues.append(
                Issue(
                    f"{PACKAGE_CODE}-MEMBER-STALE",
                    f"member digest no longer matches the bytes at {where}; the frozen subject "
                    "and the real one have diverged",
                    member_id,
                )
            )
    return report_of(issues)


# ---------------------------------------------------------------------------
# Result invariants (N2-A2, N2-A3)
# ---------------------------------------------------------------------------


def check_review_result(
    result: Mapping[str, Any],
    spec: Mapping[str, Any],
    package: Mapping[str, Any],
    *,
    executor: str | None = None,
) -> Report:
    """Invariants 2 and 10: every obligation covered exactly once, completeness rechecked.

    `executor` stays optional in the signature but never optional in the *report*: omitting
    it yields `V3-REVIEW-REVIEWER-DISTINCTNESS-UNVERIFIED` rather than silence, so a caller
    cannot switch the guard off by not passing an argument. Making the parameter required was
    rejected for the reason N1 recorded: the pinning test shape — call without it, assert the
    report is not ok — is only expressible against a report, since a required parameter would
    raise instead.

    **Permanent boundary, deliberately not pursued.** Comparing `reviewed_by` against the
    executor's name proves only that two declared *names* differ, exactly as N1-R3 records
    for the auditor. Contract §1 settles it: role separation is a workflow protocol, not an
    OS guarantee.
    """
    schema_report = validate_n2("review_result", result)
    if not schema_report.ok:
        return schema_report

    issues: list[Issue] = []

    if result["work_id"] != spec["work_id"]:
        issues.append(Issue(f"{CODE}-WORK-MISMATCH", "result names a different work_id", "work_id"))

    # --- the verdict binds the exact package it answers for ---
    if result["package_ref"]["digest_sha256"] != package_digest(package):
        issues.append(
            Issue(
                f"{CODE}-PACKAGE-BINDING-MISMATCH",
                "the result was produced against different ReviewPackage bytes than the ones "
                "supplied",
                "package_ref/digest_sha256",
            )
        )
    if result["review_round"] != package["review_round"]:
        issues.append(
            Issue(
                f"{CODE}-ROUND-MISMATCH",
                f"a {result['review_round']} result answers a {package['review_round']} package",
                "review_round",
            )
        )
    if result["candidate_ref"].get("commit") != package["candidate_ref"].get("commit"):
        issues.append(
            Issue(
                f"{CODE}-WRONG-CANDIDATE",
                "the result and its package name different candidates",
                "candidate_ref/commit",
            )
        )

    # --- invariant 2: every obligation exactly once, no more and no fewer ---
    declared = {ob["obligation_id"] for ob in spec["obligations"]}
    disposed = [row["obligation_id"] for row in result["per_obligation_disposition"]]
    for missing in sorted(declared - set(disposed)):
        issues.append(
            Issue(
                f"{CODE}-OBLIGATION-UNDISPOSED",
                f"no review disposition for obligation: {missing}",
                "per_obligation_disposition",
            )
        )
    for unknown in sorted(set(disposed) - declared):
        issues.append(
            Issue(
                f"{CODE}-UNDECLARED-DISPOSITION",
                f"disposition for an obligation the WorkSpec never declared: {unknown}",
                "per_obligation_disposition",
            )
        )
    for obligation_id in sorted({name for name in disposed if disposed.count(name) > 1}):
        issues.append(
            Issue(
                f"{CODE}-DUPLICATE-DISPOSITION",
                f"obligation disposed more than once: {obligation_id}",
                "per_obligation_disposition",
            )
        )

    # --- findings referenced by a disposition must exist ---
    finding_ids = {finding["finding_id"] for finding in result.get("findings", [])}
    for row in result["per_obligation_disposition"]:
        for referenced in row.get("finding_ids", []):
            if referenced not in finding_ids:
                issues.append(
                    Issue(
                        f"{CODE}-DANGLING-FINDING-REF",
                        f"disposition cites finding '{referenced}', which this result does not "
                        "contain",
                        f"per_obligation_disposition/{row['obligation_id']}",
                    )
                )
        if row["disposition"] == "NOT_SUPPORTED" and not row.get("finding_ids"):
            issues.append(
                Issue(
                    f"{CODE}-UNSUPPORTED-WITHOUT-FINDING",
                    f"obligation '{row['obligation_id']}' is NOT_SUPPORTED but cites no finding, "
                    "so nothing names what would have to change",
                    f"per_obligation_disposition/{row['obligation_id']}",
                )
            )

    # --- a blocking discrepancy cannot coexist with 'no blocker found' ---
    blocking = [finding["finding_id"] for finding in result.get("findings", []) if finding["blocking"]]
    if blocking and result["verdict"] == "REVIEWED_NO_BLOCKER":
        issues.append(
            Issue(
                f"{CODE}-BLOCKER-CONTRADICTS-VERDICT",
                f"verdict is REVIEWED_NO_BLOCKER while {len(blocking)} blocking finding(s) are "
                f"recorded: {', '.join(blocking)}",
                "verdict",
            )
        )
    # --- an INCOMPLETE map is DISCLOSED, never silently carried (V3 revise round) ---
    #
    # This replaces `V3-REVIEW-INCOMPLETE-CONTRADICTS-VERDICT`, which refused
    # INCOMPLETE + REVIEWED_NO_BLOCKER outright on the reading that an unmapped normative unit
    # *is* a blocking discrepancy. Contract §5 does not say that. It defines the verdict as
    # scope-relative — "no blocking discrepancy found **within the frozen subjects and review
    # dimensions**" — so an incomplete map means the dimensions were narrower and the verdict
    # stays true *as defined*, provided the narrowness is disclosed. The old guard over-read the
    # contract, and refusing the only honest verdict available while naming no replacement is a
    # deadlock rather than a check: both real shadow runs hit it, with different reviewers on
    # different subjects, because a hand-authored obligation map drops normative units as the
    # normal case.
    #
    # The requirement therefore moves from the verdict to the disclosure, and it is
    # **unconditional**. Gating it on REVIEWED_NO_BLOCKER would have let the same silence through
    # everywhere else: run-p3 returned CHANGES_REQUIRED and had *also* dropped a normative unit,
    # which under the old shape nothing would have made it say.
    #
    # Both halves are required because they do different work. The finding puts the gap in the
    # review's own findings list; the `residual_uncertainty` entry is what reaches the user at
    # FINAL and is convertible to an `ACCEPT_WITH_LIMITATIONS` limitation (V3-D6). A gap disclosed
    # only in a finding is one the deciding user never sees.
    #
    # **Ceiling, stated rather than papered over:** this matches an id as a substring. It
    # establishes that the id was *mentioned*, not that the sentence mentioning it is genuinely
    # about the gap — a reviewer determined to satisfy it cheaply can. It is a floor against
    # silence, not a judgment of disclosure quality, and the honest name for what it checks is
    # "the omission is traceable from the result" rather than "the omission was explained".
    completeness = result["instruction_completeness"]
    if completeness["result"] == "INCOMPLETE":
        unmapped = completeness.get("unmapped_unit_ids", [])

        def names_a_gap(text: str) -> bool:
            return any(unit in text for unit in unmapped)

        undisclosed = [
            requirement
            for requirement, satisfied in (
                (
                    "a finding naming one of them",
                    any(names_a_gap(f["statement"]) for f in result.get("findings", [])),
                ),
                (
                    "a residual_uncertainty entry naming one of them",
                    any(names_a_gap(note) for note in result["residual_uncertainty"]),
                ),
            )
            if not satisfied
        ]
        if undisclosed:
            issues.append(
                Issue(
                    f"{CODE}-INCOMPLETE-UNDISCLOSED",
                    "the instruction recheck returned INCOMPLETE, naming unmapped unit(s) "
                    f"{', '.join(unmapped)}, but the result carries no "
                    + " and no ".join(undisclosed)
                    + "; an incomplete map narrows the review dimensions the verdict is relative "
                    "to, and a narrowing the deciding user cannot see is the one thing it may "
                    "not be",
                    "instruction_completeness/unmapped_unit_ids",
                )
            )

    # --- the instruction actually rechecked must be the one the WorkSpec froze ---
    rechecked = result["instruction_completeness"]["instruction_ref"]
    for field in ("path", "revision"):
        if rechecked.get(field) != spec["instruction_ref"].get(field):
            issues.append(
                Issue(
                    f"{CODE}-INSTRUCTION-MISMATCH",
                    f"the completeness recheck read a different frozen instruction ({field})",
                    "instruction_completeness/instruction_ref",
                )
            )

    # --- V3-D6: a VERIFY is answerable for the whole repair diff and the permanent boundaries ---
    scope = result.get("verify_scope")
    if scope:
        unchecked = [
            name
            for name, flag in (
                ("the whole repair diff", scope["repair_diff_reviewed"]),
                ("the permanent boundaries", scope["permanent_boundaries_checked"]),
            )
            if not flag
        ]
        if unchecked:
            issues.append(
                Issue(
                    f"{CODE}-VERIFY-SCOPE-INCOMPLETE",
                    "the VERIFY did not cover " + " or ".join(unchecked)
                    + "; V3-D6 scopes it to the accepted findings, the entire repair diff and the "
                    "permanent boundaries",
                    "verify_scope",
                )
            )

    # --- V3-D5: the reviewer is not the executor, or that is reported as unverified ---
    #
    # `not executor.strip()` and not `executor is None`. An empty or whitespace-only identity
    # is what an unset config field or environment variable actually looks like, and testing
    # only for None let it through to the comparison below, where it differed from every
    # `reviewed_by` (minLength 2) and so reported *nothing at all* — the guard silently off,
    # which is the exact failure this shape exists to prevent.
    if executor is None or not executor.strip():
        issues.append(
            Issue(
                f"{CODE}-REVIEWER-DISTINCTNESS-UNVERIFIED",
                "no executor identity was supplied, so reviewer/executor distinctness was not "
                "checked; this is an unverified property, not a satisfied one",
                "reviewed_by",
            )
        )
    elif result["reviewed_by"].strip().casefold() == executor.strip().casefold():
        issues.append(
            Issue(
                f"{CODE}-REVIEWER-NOT-DISTINGUISHABLE",
                f"the review was performed by the executor of the same run: {executor}",
                "reviewed_by",
            )
        )

    return schema_report + report_of(issues)


def result_digest(result: Mapping[str, Any]) -> str:
    return canonical_digest(result)


def blocking_findings(result: Mapping[str, Any]) -> list[dict[str, Any]]:
    """The findings that must be repaired or accepted as limitations before FINAL."""
    return [finding for finding in result.get("findings", []) if finding["blocking"]]


def accepted_findings(
    result: Mapping[str, Any], accepted_ids: Iterable[str]
) -> tuple[list[dict[str, Any]], list[str]]:
    """Split the requested IDs into the findings they name and the ones that do not exist."""
    by_id = {finding["finding_id"]: finding for finding in result.get("findings", [])}
    wanted = list(accepted_ids)
    return [by_id[name] for name in wanted if name in by_id], [
        name for name in wanted if name not in by_id
    ]


def render_result(result: Mapping[str, Any]) -> str:
    """A user-facing view: exceptions and the requested decision, never a wall of green."""
    lines = [
        f"round        : {result['review_round']}",
        f"verdict      : {result['verdict']}",
        f"candidate    : {result['candidate_ref'].get('commit', '?')[:12]}",
        f"reviewed_by  : {result['reviewed_by']}",
        f"instruction  : {result['instruction_completeness']['result']}",
    ]
    exceptions = [
        row
        for row in result["per_obligation_disposition"]
        if row["disposition"] != "SUPPORTED"
    ]
    for row in exceptions:
        lines.append(f"  !! {row['obligation_id']}: {row['disposition']} — {row.get('note', '')}")
    for finding in result.get("findings", []):
        mark = "BLOCKER" if finding["blocking"] else "finding"
        lines.append(f"  [{mark}] {finding['finding_id']}: {finding['statement']}")
        if finding.get("minimum_fix"):
            lines.append(f"            minimum fix: {finding['minimum_fix']}")
    for note in result["residual_uncertainty"]:
        lines.append(f"  ?? residual: {note}")
    if not result["residual_uncertainty"]:
        lines.append("  -- the reviewer recorded no residual uncertainty")
    return "\n".join(lines)


def load_package(path: pathlib.Path | str) -> dict[str, Any]:
    return load_json(path)


def load_result(path: pathlib.Path | str) -> dict[str, Any]:
    return load_json(path)


__all__ = [
    "N2_SCHEMA_FILES",
    "N2_SCHEMA_POINTERS",
    "REQUIRED_ROLES",
    "accepted_findings",
    "blocking_findings",
    "check_package",
    "check_review_result",
    "freeze_package",
    "load_package",
    "load_result",
    "member",
    "members_by_role",
    "package_digest",
    "render_result",
    "require_valid_n2",
    "result_digest",
    "validate_n2",
    "verify_member_bytes",
]
