#!/usr/bin/env python3
"""Document Work Assurance v3 (V3-N0) contract fixture runner.

Validates the seeded positive/negative fixtures in cases.json against the frozen
document-assurance-v3 JSON Schemas, then runs the named cross-document checks (X-*)
that a single JSON document cannot express: no-profile absence (never an empty
placeholder), instruction-unit <-> obligation bidirectional mapping, authored-surface
vocabulary neutrality (N0-A5/N0-A8), resolved-plan canonical-fact non-duplication
(N0-A6) and state pointer-only shape (V3-D8).

This is N0 test infrastructure ONLY — it validates hand-authored fixtures. It is NOT
the N1 verifier/controller and computes no digest (fixture digests are shape-valid
placeholders; digest recomputation is an N1 obligation). Offline: no network, no
wall-clock in output.

Exit 0 = every case behaved as declared. Exit 1 = at least one regression.
"""
import json
import pathlib
import sys

try:
    from jsonschema import Draft202012Validator
    from referencing import Registry, Resource
except Exception as exc:  # pragma: no cover
    print(f"[FATAL] jsonschema/referencing not importable: {exc}", file=sys.stderr)
    sys.exit(2)

BASE = pathlib.Path(__file__).resolve().parent
SCHEMA_DIR = BASE.parents[3] / "schema" / "document-assurance-v3"
SCHEMA_URI_BASE = "researchsystem/schema/document-assurance-v3/"

SCHEMA_FILES = {
    "common": "common.schema.json",
    "spec": "document-work-spec.schema.json",
    "profile": "document-assurance-profile.schema.json",
    "plan": "resolved-assurance-plan.schema.json",
    "state": "assurance-work-state.schema.json",
    "audit": "instruction-coverage-audit.schema.json",
    "decision": "user-decision.schema.json",
}


def load(p: pathlib.Path):
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


SCHEMAS = {k: load(SCHEMA_DIR / v) for k, v in SCHEMA_FILES.items()}

# 1) The schemas themselves must be valid Draft 2020-12 schemas.
for name, schema in SCHEMAS.items():
    try:
        Draft202012Validator.check_schema(schema)
    except Exception as exc:
        print(f"[FATAL] schema '{name}' is not a valid JSON Schema: {exc}", file=sys.stderr)
        sys.exit(2)

REGISTRY = Registry().with_resources(
    [(SCHEMA_URI_BASE + fname, Resource.from_contents(schema))
     for fname, schema in ((SCHEMA_FILES[k], SCHEMAS[k]) for k in SCHEMAS)]
)
VALIDATORS = {
    k: Draft202012Validator(v, registry=REGISTRY)
    for k, v in SCHEMAS.items() if k != "common"
}

rows = []
failures = 0


def record(name: str, kind: str, expect: str, actual: str, detail: str = "") -> None:
    global failures
    ok = expect == actual
    if not ok:
        failures += 1
    rows.append(("PASS" if ok else "XXXX", name, kind, f"want={expect}", f"got={actual}", detail))


# 2) Declarative schema cases.
cases = load(BASE / "cases.json")
for case in cases["schema_cases"]:
    doc = load(BASE / case["file"])
    errs = sorted(VALIDATORS[case["schema"]].iter_errors(doc), key=str)
    actual = "valid" if not errs else "invalid"
    detail = errs[0].message[:90] if errs else ""
    record(case["name"], f"schema:{case['schema']}", case["expect"], actual, detail)


# 3) Cross-document checks.
def bundle(name: str, expect: str, ok: bool, detail: str = "") -> None:
    record(name, "bundle", expect, "pass" if ok else "fail", detail)


spec_minimal = load(BASE / "positive/POS-spec-minimal-no-profile.json")
spec_full = load(BASE / "positive/POS-spec-full-profile.json")
plan_no_profile = load(BASE / "positive/POS-plan-no-profile.json")
spec_dangling = load(BASE / "negative/NEG-bundle-spec-dangling-obligation.json")


# X-NO-PROFILE-ABSENT — V3-D2/N1-A1: "no profile" is field absence, never [].
bundle(
    "X-NO-PROFILE-ABSENT/spec", "pass",
    "document_assurance_profiles" not in spec_minimal,
)
bundle(
    "X-NO-PROFILE-ABSENT/plan", "pass",
    "assurance_profiles" not in plan_no_profile,
)


# X-SPEC-BIDIRECTIONAL — V3-D7: every obligation unit-ref resolves; every obligation-classified
# unit's obligation_ids resolve; every obligation is referenced by at least one unit.
def bidirectional(spec) -> bool:
    unit_ids = {u["unit_id"] for u in spec["instruction_units"]}
    obligation_ids = {o["obligation_id"] for o in spec["obligations"]}
    for o in spec["obligations"]:
        if not set(o["instruction_unit_ids"]) <= unit_ids:
            return False
    referenced = set()
    for u in spec["instruction_units"]:
        if u["classification"] == "obligation":
            ids = set(u.get("obligation_ids", []))
            if not ids <= obligation_ids:
                return False
            referenced |= ids
    return referenced == obligation_ids


bundle("X-SPEC-BIDIRECTIONAL/positive", "pass", bidirectional(spec_full))
bundle("X-SPEC-BIDIRECTIONAL/dangling", "fail", bidirectional(spec_dangling))


# X-SURFACE-VOCAB — N0-A5/N0-A8: no capability/enforcement/activation/authority-grant,
# receipt/event-chain, or consumer/platform vocabulary on the authored/generated SURFACE
# (property names + enum values). Prose descriptions may explain the prohibition.
FORBIDDEN_SURFACE_TOKENS = [
    "capabilit", "enforcement", "authority", "activation", "receipt", "lease",
    "idempoten", "event", "waiver", "gate_", "retrospective", "spend", "publication",
    "p4", "thesis", "experimentlab", "obsidian", "stage_id", "gsd", "uiux", "appsec",
]


def surface_terms(node, out):
    if isinstance(node, dict):
        for key, val in node.items():
            if key in ("properties", "$defs"):
                for prop in val:
                    out.append(prop)
            if key == "required" and isinstance(val, list):
                out.extend(str(v) for v in val)
            if key == "enum" and isinstance(val, list):
                out.extend(str(v) for v in val)
            surface_terms(val, out)
    elif isinstance(node, list):
        for item in node:
            surface_terms(item, out)
    return out


hits = []
for name, schema in SCHEMAS.items():
    for term in surface_terms(schema, []):
        low = term.lower()
        for tok in FORBIDDEN_SURFACE_TOKENS:
            if tok in low:
                hits.append((name, term))
bundle("X-SURFACE-VOCAB/core-schemas", "pass", not hits, str(hits[:4]))


# X-PLAN-NO-CANONICAL-FACT — N0-A6: ResolvedAssurancePlan defines no property that would
# duplicate a canonical WorkSpec/instruction fact.
CANONICAL_FACTS = {
    "objective", "instruction_ref", "instruction_units", "obligations",
    "inputs", "expected_artifacts",
}
plan_props = set(SCHEMAS["plan"]["properties"])
overlap = plan_props & CANONICAL_FACTS
bundle("X-PLAN-NO-CANONICAL-FACT/schema", "pass", not overlap, str(sorted(overlap)))


# X-STATE-POINTERS-ONLY — V3-D8: the state surface is exactly identity + closed status +
# repair round + pointers + blockers/next_action. Any extra property is a drift signal.
EXPECTED_STATE_PROPS = {
    "work_id", "run_id", "status", "repair_round",
    "work_spec_ref", "resolved_plan_ref", "instruction_audit_ref", "start_decision_ref",
    "candidate_ref", "fulfillment_ref", "manifest_ref", "check_results_ref",
    "coverage_ref", "review_ref", "repair_decision_ref", "assurance_candidate_ref",
    "final_decision_ref", "summary_ref", "blockers", "next_action",
}
state_props = set(SCHEMAS["state"]["properties"])
bundle(
    "X-STATE-POINTERS-ONLY/schema", "pass",
    state_props == EXPECTED_STATE_PROPS,
    f"unexpected={sorted(state_props - EXPECTED_STATE_PROPS)} missing={sorted(EXPECTED_STATE_PROPS - state_props)}",
)


# 4) Report.
width = max(len(r[1]) for r in rows)
for status, name, kind, want, got, detail in rows:
    line = f"[{status}] {name.ljust(width)}  {kind:16} {want:14} {got:12}"
    if detail:
        line += f"  {detail}"
    print(line)

total = len(rows)
print(f"\n{total - failures}/{total} cases behaved as declared; failures={failures}")
sys.exit(0 if failures == 0 else 1)
