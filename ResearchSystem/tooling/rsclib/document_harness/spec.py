"""DocumentWorkSpec loading and the instruction-obligation spine (V3-D7, N1-A3).

The WorkSpec is the only object a human authors in full. Its schema closes the authored
surface; this module closes what a single document cannot express: that the instruction
units and the obligations actually refer to each other, in both directions, and that every
identifier a downstream verifier will resolve is declared exactly once.

The spine is the product's centre:

    instruction unit -> obligation (or an explicit non-normative rationale)
    -> executor fulfillment claim + implementation locator(s)
    -> applicable verification evidence -> per-obligation review disposition

This module owns the first arrow only. Whether the *raw instruction* was fully decomposed
into units is a separate judgment, owned by the instruction auditor (``instruction.py``);
a bidirectionally consistent WorkSpec can still omit instruction content, which is exactly
why the audit exists as a distinct pre-start step.
"""
from __future__ import annotations

import pathlib
from typing import Any, Mapping

from rsclib.document_harness import (
    Issue,
    Report,
    SpecGap,
    canonical_digest,
    load_json,
    report_of,
    validate,
)

CODE = "V3-SPEC"

#: Explicit version keying (wave 1, special-case bucket design §4). A v1 instance carries no
#: version field — the signed v1 schema's closed root leaves it no way to; a v2 instance
#: names its schema via the required root const. Anything else fails closed. There is
#: deliberately NO cross-version fallback: a document that declares "2" and fails v2 is
#: reported against v2, never quietly re-tried against v1 (and vice versa) — a fallback
#: would silently mix versions, which is the fail-open shape N1 taught this package to hunt.
SPEC_SCHEMA_KINDS: dict[str, str] = {"2": "spec_v2"}

#: Sentinel distinguishing a missing key from an explicitly present value. `.get()` alone
#: cannot tell `null` from absent, and "present but null" is a declaration, not absence
#: (W1 review finding A1) — only true key absence selects v1.
_ABSENT = object()


def spec_schema_kind(spec: Mapping[str, Any]) -> str:
    """The schema kind this WorkSpec instance declares. Unknown versions stop (`SpecGap`)."""
    declared = spec.get("schema_version", _ABSENT)
    if declared is _ABSENT:
        return "spec"
    if isinstance(declared, str):
        kind = SPEC_SCHEMA_KINDS.get(declared)
        if kind is not None:
            return kind
    raise SpecGap(
        f"unsupported WorkSpec schema_version: {declared!r} — "
        "no cross-version fallback; supported: absent (v1), '2'"
    )


def load_spec(path: pathlib.Path | str) -> dict[str, Any]:
    """Read a WorkSpec document. Validation is a separate, explicit step."""
    return load_json(path)


def spec_digest(spec: Mapping[str, Any]) -> str:
    """Canonical digest binding this exact WorkSpec to every record derived from it."""
    return canonical_digest(spec)


def unit_index(spec: Mapping[str, Any]) -> dict[str, dict[str, Any]]:
    return {unit["unit_id"]: dict(unit) for unit in spec.get("instruction_units", [])}


def obligation_index(spec: Mapping[str, Any]) -> dict[str, dict[str, Any]]:
    return {ob["obligation_id"]: dict(ob) for ob in spec.get("obligations", [])}


def artifact_index(spec: Mapping[str, Any]) -> dict[str, str]:
    return {art["artifact_id"]: art["path"] for art in spec.get("expected_artifacts", [])}


def declared_check_ids(spec: Mapping[str, Any]) -> set[str]:
    """Every local check id the WorkSpec's obligations request."""
    ids: set[str] = set()
    for ob in spec.get("obligations", []):
        ids.update(ob.get("local_check_refs", []))
    return ids


def _duplicates(values: list[str]) -> list[str]:
    seen: set[str] = set()
    dupes: set[str] = set()
    for value in values:
        if value in seen:
            dupes.add(value)
        seen.add(value)
    return sorted(dupes)


def check_spec(spec: Mapping[str, Any]) -> Report:
    """Schema validity plus the cross-document spine rules.

    A schema-invalid spec returns early: the structural rules below assume the shape the
    schema guarantees, and reporting derived errors on top of a malformed document would
    bury the real defect.
    """
    schema_report = validate(spec_schema_kind(spec), spec)
    if not schema_report.ok:
        return schema_report

    issues: list[Issue] = []
    units = spec["instruction_units"]
    obligations = spec["obligations"]
    artifacts = spec["expected_artifacts"]

    # Identity: every declared id is declared exactly once, or later joins are ambiguous.
    for label, values, where in (
        ("instruction unit", [u["unit_id"] for u in units], "instruction_units"),
        ("obligation", [o["obligation_id"] for o in obligations], "obligations"),
        ("expected artifact", [a["artifact_id"] for a in artifacts], "expected_artifacts"),
    ):
        for dupe in _duplicates(values):
            issues.append(Issue(f"{CODE}-DUPLICATE-ID", f"{label} id declared twice: {dupe}", where))

    unit_ids = set(unit_index(spec))
    obligation_ids = set(obligation_index(spec))
    artifact_ids = set(artifact_index(spec))

    # Forward: every obligation traces back to declared instruction units.
    for ob in obligations:
        where = f"obligations/{ob['obligation_id']}"
        for unit_id in ob["instruction_unit_ids"]:
            if unit_id not in unit_ids:
                issues.append(
                    Issue(
                        f"{CODE}-DANGLING-UNIT-REF",
                        f"obligation refers to undeclared instruction unit: {unit_id}",
                        where,
                    )
                )
        for artifact_id in ob.get("expected_artifact_ids", []):
            if artifact_id not in artifact_ids:
                issues.append(
                    Issue(
                        f"{CODE}-DANGLING-ARTIFACT-REF",
                        f"obligation refers to undeclared expected artifact: {artifact_id}",
                        where,
                    )
                )

    # Backward: every obligation-classified unit points at declared obligations, and every
    # obligation is claimed by at least one unit. An unreferenced obligation is a real
    # defect, not a harmless extra: nothing in the instruction demands it, so review has no
    # ground truth to judge it against.
    referenced: set[str] = set()
    for unit in units:
        where = f"instruction_units/{unit['unit_id']}"
        if unit["classification"] != "obligation":
            continue
        for obligation_id in unit.get("obligation_ids", []):
            if obligation_id not in obligation_ids:
                issues.append(
                    Issue(
                        f"{CODE}-DANGLING-OBLIGATION-REF",
                        f"instruction unit refers to undeclared obligation: {obligation_id}",
                        where,
                    )
                )
            referenced.add(obligation_id)

    for orphan in sorted(obligation_ids - referenced):
        issues.append(
            Issue(
                f"{CODE}-UNREFERENCED-OBLIGATION",
                f"obligation is not claimed by any instruction unit: {orphan}",
                "obligations",
            )
        )

    return schema_report + report_of(issues)


def require_startable(spec: Mapping[str, Any]) -> None:
    """Raise `SpecGap` unless the spine is complete enough to start (N1-A3).

    An instruction unit with no disposition — neither an obligation binding nor an explicit
    non-normative rationale — is the silent-omission failure class this product exists to
    make visible. It blocks START; it is never repaired inside the run.
    """
    check_spec(spec).require(SpecGap)


def undisposed_units(spec: Mapping[str, Any]) -> list[str]:
    """Unit ids carrying neither an obligation binding nor a context rationale.

    The schema already rejects these, so a schema-valid spec returns an empty list. This
    reports the same defect class over a *raw* authored document that has not been
    validated yet, which is what an authoring tool needs in order to explain itself.
    """
    missing: list[str] = []
    for unit in spec.get("instruction_units", []):
        classification = unit.get("classification")
        if classification == "obligation" and not unit.get("obligation_ids"):
            missing.append(unit.get("unit_id", "<unnamed>"))
        elif classification == "context" and not unit.get("rationale"):
            missing.append(unit.get("unit_id", "<unnamed>"))
        elif classification not in ("obligation", "context"):
            missing.append(unit.get("unit_id", "<unnamed>"))
    return missing


def obligations_for_mode(spec: Mapping[str, Any], *modes: str) -> list[dict[str, Any]]:
    """Obligations whose verification_mode is one of `modes` (deterministic vs review)."""
    wanted = set(modes)
    return [ob for ob in spec.get("obligations", []) if ob["verification_mode"] in wanted]
