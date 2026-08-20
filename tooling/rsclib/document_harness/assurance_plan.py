"""Profile resolution into a disposable ResolvedAssurancePlan (§5.2, N1-A1).

The plan is immutable for a run but **disposable**: it can be deleted and rebuilt
byte-identically from the pinned WorkSpec, the exact profile versions and this resolver.
That property is the whole point — a plan that copied canonical facts would drift from the
WorkSpec it claims to resolve, which is the v1 StageRecord failure this design removes
(N0-A6). So the plan stores references, the deltas resolution actually produced, the
boundary projection, the check order, named conflicts and the repair cap. Nothing else.

Byte-rebuildability forces two properties on everything below: no timestamp and no
iteration over an unordered set. Profiles are visited in the WorkSpec's declaration order
and every derived collection is sorted.

Resolution semantics (§5.2):

* checks and change constraints **accumulate**;
* a numeric limit bound by more than one profile resolves to the **stricter** value;
* a genuine disagreement is a named conflict attributed to its owners, and a plan carrying
  conflicts is unusable for START — resolution fails closed rather than picking a winner;
* profiles contribute reusable *rules*; the WorkSpec supplies the concrete *paths*. A
  materialized constraint can only add to the negative boundary `out`, never widen
  `write_scope` (V3-D3).
"""
from __future__ import annotations

import json
from typing import Any, Mapping, Sequence

from rsclib.document_harness import (
    RESOLVER_VERSION,
    Issue,
    Report,
    SpecGap,
    canonical_bytes,
    report_of,
    validate,
)
from rsclib.document_harness.assurance_profiles import profile_digest
from rsclib.document_harness.spec import declared_check_ids, spec_digest

CODE = "V3-PLAN"

#: Facts owned by the WorkSpec or the raw instruction. The plan references them; copying any
#: of them into the plan is the duplication defect N0-A6 forbids.
CANONICAL_FACTS = frozenset(
    {"objective", "instruction_ref", "instruction_units", "obligations", "inputs", "expected_artifacts"}
)

_SLUG_MAX = 64
_OWNER_MAX = 120


def _slug(prefix: str, name: str) -> str:
    return f"{prefix}-{name}"[:_SLUG_MAX].rstrip("-")


def _owner_label(profile: Mapping[str, Any]) -> str:
    return f"{profile['owner']} ({profile['profile_id']})"[:_OWNER_MAX]


def _selection_parameters(selection: Mapping[str, Any]) -> dict[str, Any]:
    return dict(selection.get("parameters", {}))


def _paths_from_parameter(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, list) and all(isinstance(item, str) for item in value):
        return list(value)
    return []


def resolve(
    spec: Mapping[str, Any],
    spec_path: str,
    selected: Sequence[tuple[Mapping[str, Any], Mapping[str, Any]]] = (),
    *,
    plan_id: str | None = None,
) -> dict[str, Any]:
    """Resolve a WorkSpec plus its exact leaf profiles into a ResolvedAssurancePlan.

    `selected` is the ordered `(selection, profile)` list from
    `assurance_profiles.load_selected`. An empty sequence is the required no-profile
    positive path: the result simply carries no `assurance_profiles` field (N1-A1).
    """
    work_id = spec["work_id"]
    plan: dict[str, Any] = {
        "plan_id": plan_id or _slug(work_id, "plan"),
        "work_id": work_id,
        "work_spec_ref": {"path": spec_path, "digest_sha256": spec_digest(spec)},
        "resolver_version": RESOLVER_VERSION,
    }

    if selected:
        plan["assurance_profiles"] = [
            {
                "profile_id": profile["profile_id"],
                "version": profile["version"],
                "digest_sha256": profile_digest(profile),
            }
            for _, profile in selected
        ]

    conflicts: list[dict[str, Any]] = []
    added_checks: list[dict[str, Any]] = []
    materialized: list[dict[str, Any]] = []
    tightened: list[dict[str, Any]] = []

    # --- checks accumulate; a repeated id with a different kind is a real disagreement ---
    check_owner: dict[str, tuple[str, Mapping[str, Any]]] = {}
    for _, profile in selected:
        for check in profile.get("required_checks", []):
            check_id, kind = check["check_id"], check["kind"]
            if check_id in check_owner:
                prior_kind, prior_profile = check_owner[check_id]
                if prior_kind != kind:
                    conflicts.append(
                        {
                            "conflict_id": _slug("check-kind", check_id),
                            "description": (
                                f"check '{check_id}' is required as '{prior_kind}' and as "
                                f"'{kind}' — resolution cannot pick one"
                            ),
                            "owners": [_owner_label(prior_profile), _owner_label(profile)],
                        }
                    )
                continue
            check_owner[check_id] = (kind, profile)
            added_checks.append(
                {"check_id": check_id, "kind": kind, "source_profile": profile["profile_id"]}
            )

    # --- change constraints materialize into added negative-boundary paths ---
    constraint_owner: dict[str, tuple[tuple[str, ...], Mapping[str, Any]]] = {}
    for selection, profile in selected:
        parameters = _selection_parameters(selection)
        for constraint in profile.get("change_constraints", []):
            constraint_id = constraint["constraint_id"]
            paths: list[str] = []
            for name in constraint.get("parameter_names", []):
                paths.extend(_paths_from_parameter(parameters.get(name)))
            ordered = tuple(sorted(set(paths)))
            if constraint_id in constraint_owner:
                prior_paths, prior_profile = constraint_owner[constraint_id]
                if prior_paths != ordered:
                    conflicts.append(
                        {
                            "conflict_id": _slug("constraint", constraint_id),
                            "description": (
                                f"constraint '{constraint_id}' materializes to different paths "
                                f"in two profiles"
                            ),
                            "owners": [_owner_label(prior_profile), _owner_label(profile)],
                        }
                    )
                continue
            constraint_owner[constraint_id] = (ordered, profile)
            entry: dict[str, Any] = {
                "constraint_id": constraint_id,
                "source_profile": profile["profile_id"],
            }
            if ordered:
                entry["added_out_paths"] = list(ordered)
            materialized.append(entry)

    # --- numeric limits bound by more than one profile: the stricter value wins ---
    bindings: dict[str, list[tuple[Any, Mapping[str, Any]]]] = {}
    for selection, profile in selected:
        for name, value in sorted(_selection_parameters(selection).items()):
            if isinstance(value, float):
                # The canonical form forbids floating point, so a float limit could never be
                # digested or rebuilt. Refuse it here, where the parameter can be named,
                # rather than crashing later inside canonicalization.
                raise SpecGap(
                    f"{CODE}-FLOAT-LIMIT parameter '{name}' in profile "
                    f"'{profile['profile_id']}' is floating point; v3 limits are integers"
                )
            bindings.setdefault(name, []).append((value, profile))
    for name in sorted(bindings):
        entries = bindings[name]
        if len(entries) < 2:
            continue
        numeric = [
            (value, profile)
            for value, profile in entries
            if isinstance(value, int) and not isinstance(value, bool)
        ]
        if len(numeric) == len(entries):
            winner_value, winner_profile = min(numeric, key=lambda item: item[0])
            tightened.append(
                {
                    "limit_name": name,
                    "value": winner_value,
                    "source_profile": winner_profile["profile_id"],
                }
            )
            continue
        distinct = {json.dumps(value, sort_keys=True, ensure_ascii=False) for value, _ in entries}
        if len(distinct) > 1:
            conflicts.append(
                {
                    "conflict_id": _slug("parameter", name),
                    "description": (
                        f"parameter '{name}' is bound to incompatible non-numeric values by two "
                        f"profiles — resolution has no stricter-wins rule for these"
                    ),
                    "owners": [_owner_label(entries[0][1]), _owner_label(entries[1][1])],
                }
            )

    deltas: dict[str, Any] = {}
    if added_checks:
        deltas["added_checks"] = added_checks
    if tightened:
        deltas["tightened_limits"] = tightened
    if materialized:
        deltas["materialized_constraints"] = materialized
    if deltas:
        plan["resolved_deltas"] = deltas
    if conflicts:
        plan["conflicts"] = sorted(conflicts, key=lambda item: item["conflict_id"])

    boundary = spec["change_boundary"]
    added_out: set[str] = set()
    for entry in materialized:
        added_out.update(entry.get("added_out_paths", []))
    plan["effective_change_boundary"] = {
        "write_scope": list(boundary["write_scope"]),
        "out": sorted(set(boundary["out"]) | added_out),
    }

    order = sorted(declared_check_ids(spec) | {check["check_id"] for check in added_checks})
    if order:
        plan["check_order"] = order

    plan["repair_cap"] = 1
    return plan


def check_plan(plan: Mapping[str, Any]) -> Report:
    """Schema validity plus the non-duplication and bounded-repair invariants.

    The two named invariants run **before** the schema report and unconditionally. Both are
    plain key inspections that assume nothing about the document's shape, and the schema
    would otherwise shadow them: `additionalProperties: false` and `repair_cap: {const: 1}`
    already reject these documents, so a schema-first ordering with an early return would
    leave `V3-PLAN-CANONICAL-FACT-COPIED` and `V3-PLAN-REPAIR-CAP` permanently unreachable.

    That shadowing is worth undoing rather than deleting the checks, because the two reports
    say different things. The schema says a property was unexpected; these say *why the
    shape is forbidden* — a plan that copies a canonical fact will drift from the WorkSpec it
    claims to resolve (N0-A6), and the repair cap is the bounded-convergence guarantee
    (V3-D6). In a governance record the reason is the part worth reading, and a greppable
    code per invariant is what makes it auditable.
    """
    issues: list[Issue] = []
    for fact in sorted(CANONICAL_FACTS & set(plan)):
        issues.append(
            Issue(
                f"{CODE}-CANONICAL-FACT-COPIED",
                f"plan duplicates a canonical WorkSpec fact: {fact}",
                "<root>",
            )
        )
    if plan.get("repair_cap") != 1:
        issues.append(
            Issue(f"{CODE}-REPAIR-CAP", "repair cap is fixed at exactly one round", "repair_cap")
        )
    return report_of(issues) + validate("plan", plan)


def require_startable(plan: Mapping[str, Any]) -> None:
    """Raise `SpecGap` unless this plan can carry a START decision.

    A plan carrying conflicts is unusable: resolution named two owners and refused to pick
    between them, so there is no effective configuration to start against (§5.2).
    """
    check_plan(plan).require(SpecGap)
    conflicts = plan.get("conflicts", [])
    if conflicts:
        raise SpecGap(
            f"{CODE}-CONFLICTS resolution failed closed with {len(conflicts)} named conflict(s): "
            + ", ".join(conflict["conflict_id"] for conflict in conflicts)
        )


def rebuild_matches(
    plan: Mapping[str, Any],
    spec: Mapping[str, Any],
    spec_path: str,
    selected: Sequence[tuple[Mapping[str, Any], Mapping[str, Any]]] = (),
) -> bool:
    """True when deleting the plan and re-resolving reproduces it byte-for-byte (§5.2)."""
    rebuilt = resolve(spec, spec_path, selected, plan_id=plan.get("plan_id"))
    return canonical_bytes(rebuilt) == canonical_bytes(plan)
