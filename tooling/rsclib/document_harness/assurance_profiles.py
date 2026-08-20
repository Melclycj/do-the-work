"""DocumentAssuranceProfile loading and the promotion threshold (V3-D2, N1-A2).

A profile is optional, small and **evidence-promoted**: one reusable assurance rule family,
one owner, one reason to change, and two distinct real work instances that already
demonstrated the reuse. Below that threshold the rule stays in the WorkSpec or the check
configuration — v3 may run indefinitely with zero published profiles, and a no-profile
resolution is a required positive case, not a degraded one (N1-A1).

The rule this module exists to prevent is the one v2 actually hit: a five-profile catalogue
authored before any real reuse existed. Everything below is a mechanical statement of the
promotion threshold, so a speculative profile fails at load rather than at review.

Honesty ceiling: "two *real* work instances" is only partly mechanizable. The distinctness
of the two witnesses and their evidence refs is checked exactly; whether the referenced work
was real is a human judgment. The one mechanical proxy here rejects witnesses that point
into a test or fixture root, which catches the obvious self-witnessing case and nothing more.
"""
from __future__ import annotations

import pathlib
from typing import Any, Mapping, Sequence

from rsclib.document_harness import (
    Issue,
    Report,
    SpecGap,
    canonical_digest,
    load_json,
    report_of,
    validate,
)

CODE = "V3-PROFILE"

#: Path segments that disqualify a reuse witness. A fixture authored to satisfy the
#: promotion threshold is not a witness of reuse — it is the threshold marking its own
#: homework (V3-D2, plan §10).
SYNTHETIC_WITNESS_SEGMENTS = ("tests", "fixtures", "fixture", "example", "examples", "sample")


def load_profile(path: pathlib.Path | str) -> dict[str, Any]:
    return load_json(path)


def profile_digest(profile: Mapping[str, Any]) -> str:
    return canonical_digest(profile)


def declared_parameter_names(profile: Mapping[str, Any]) -> set[str]:
    return {param["name"] for param in profile.get("parameters", [])}


def _referenced_parameter_names(profile: Mapping[str, Any]) -> set[str]:
    names: set[str] = set()
    for constraint in profile.get("change_constraints", []):
        names.update(constraint.get("parameter_names", []))
    for check in profile.get("required_checks", []):
        names.update(check.get("parameter_names", []))
    return names


def check_profile(profile: Mapping[str, Any]) -> Report:
    """Schema validity plus the promotion threshold (N1-A2)."""
    schema_report = validate("profile", profile)
    if not schema_report.ok:
        return schema_report

    issues: list[Issue] = []
    profile_id = profile["profile_id"]

    # Two DISTINCT witnesses. `uniqueItems` rejects identical objects only; two witnesses
    # citing the same evidence are one witness wearing two descriptions.
    witnesses = profile["reuse_witnesses"]
    evidence_paths = [w["evidence_ref"]["path"] for w in witnesses]
    if len(set(evidence_paths)) < 2:
        issues.append(
            Issue(
                f"{CODE}-WITNESS-NOT-DISTINCT",
                "two reuse witnesses cite the same evidence — that is one witness, not two",
                f"{profile_id}/reuse_witnesses",
            )
        )
    for index, path in enumerate(evidence_paths):
        segments = {segment.lower() for segment in pathlib.PurePosixPath(path).parts}
        if segments & set(SYNTHETIC_WITNESS_SEGMENTS):
            issues.append(
                Issue(
                    f"{CODE}-WITNESS-SYNTHETIC",
                    f"reuse witness cites test/fixture material, not real work: {path}",
                    f"{profile_id}/reuse_witnesses/{index}",
                )
            )

    # Every parameter a rule uses must be declared, or the selecting WorkSpec has no way to
    # know what to supply and resolution silently materializes nothing.
    declared = declared_parameter_names(profile)
    for name in sorted(_referenced_parameter_names(profile) - declared):
        issues.append(
            Issue(
                f"{CODE}-UNDECLARED-PARAMETER",
                f"rule references an undeclared parameter: {name}",
                f"{profile_id}/parameters",
            )
        )

    return schema_report + report_of(issues)


def require_publishable(profile: Mapping[str, Any]) -> None:
    """Raise `SpecGap` unless the profile has actually earned promotion (N1-A2)."""
    check_profile(profile).require(SpecGap)


def check_selection(selection: Mapping[str, Any], profile: Mapping[str, Any]) -> Report:
    """A WorkSpec's exact leaf pin must match the profile it claims to pin."""
    issues: list[Issue] = []
    where = f"document_assurance_profiles/{selection['profile_id']}"

    if selection["profile_id"] != profile["profile_id"]:
        issues.append(
            Issue(f"{CODE}-SELECTION-MISMATCH", "selection names a different profile", where)
        )
    if selection["version"] != profile["version"]:
        issues.append(
            Issue(
                f"{CODE}-VERSION-MISMATCH",
                f"selection pins {selection['version']}, profile is {profile['version']}",
                where,
            )
        )
    pinned = selection.get("digest_sha256")
    if pinned and pinned != profile_digest(profile):
        issues.append(
            Issue(
                f"{CODE}-DIGEST-MISMATCH",
                "pinned digest does not match the loaded profile bytes",
                where,
            )
        )

    supplied = set(selection.get("parameters", {}))
    for param in profile.get("parameters", []):
        if param["required"] and param["name"] not in supplied:
            issues.append(
                Issue(
                    f"{CODE}-MISSING-PARAMETER",
                    f"required parameter not supplied by the WorkSpec: {param['name']}",
                    where,
                )
            )
    for name in sorted(supplied - declared_parameter_names(profile)):
        issues.append(
            Issue(
                f"{CODE}-UNDECLARED-PARAMETER-VALUE",
                f"WorkSpec supplies a parameter the profile never declared: {name}",
                where,
            )
        )

    return report_of(issues)


def load_selected(
    spec: Mapping[str, Any], profile_dir: pathlib.Path | str
) -> list[tuple[dict[str, Any], dict[str, Any]]]:
    """Load the exact leaf profiles a WorkSpec selected, in declaration order.

    Returns an empty list when the WorkSpec selected none — absence of the field means no
    profile, never an empty placeholder (V3-D2, N1-A1). Every loaded profile must satisfy
    the promotion threshold and match its pin, or the run stops.
    """
    selections: Sequence[Mapping[str, Any]] = spec.get("document_assurance_profiles", [])
    root = pathlib.Path(profile_dir)
    loaded: list[tuple[dict[str, Any], dict[str, Any]]] = []
    for selection in selections:
        path = root / f"{selection['profile_id']}.profile.json"
        profile = load_profile(path)
        require_publishable(profile)
        check_selection(selection, profile).require(SpecGap)
        loaded.append((dict(selection), profile))
    return loaded
