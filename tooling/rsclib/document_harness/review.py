"""The V3-N2 schema extension, and the result helpers a reviewer's output is read through.

**What retired here, and what did not.** Until round `CORE-SET-CODE` this module also held the
version-1 package-bound leg: `member` / `freeze_package` / `package_digest` /
`members_by_role` / `check_package` / `verify_member_bytes` / `load_package`, and with them
`check_review_result`, whose first act was to recompute the package digest. A review subject
is a committed control plane addressed by one evidence commit since wave 2, so nothing built
or verified a package any more — the retirement removed the code, not the reading of history.
`review_subject.py` owns the successor subject, `review_result_v2.py` the successor verdict.

**Both v1 schema kinds stay registered, and that is not an oversight.** `review.schema.json`
holds the frozen ReviewPackage *and* the frozen ReviewResult, and `review.v2.schema.json`
`$ref`s five of its `$defs` — `reviewRound`, `instructionCompleteness`,
`perObligationDisposition`, `finding`, `verifyScope` — so the file has to resolve through this
registry for the v2 validator to work at all (`review_subject._w2_registry` builds on
`N2_SCHEMA_FILES`). The `review_result` pointer stays for the other half of the same reason
the v2 schema states in its own description: pinned v1 history is still readable, and no
migration was ever performed on it.

Nothing here issues a verdict. The reviewer owns `ReviewResult`; this module validates that
what the reviewer produced is well-formed against a closed schema, and renders it.
"""
from __future__ import annotations

import functools
import pathlib
from typing import Any, Iterable, Mapping

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
    canonical_digest,
    load_json,
    report_of,
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
# Reading a returned result
# ---------------------------------------------------------------------------


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


def load_result(path: pathlib.Path | str) -> dict[str, Any]:
    return load_json(path)


__all__ = [
    "N2_SCHEMA_FILES",
    "N2_SCHEMA_POINTERS",
    "accepted_findings",
    "blocking_findings",
    "load_result",
    "render_result",
    "require_valid_n2",
    "result_digest",
    "validate_n2",
]
