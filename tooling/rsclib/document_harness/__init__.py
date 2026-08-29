"""Document Work Assurance Harness v3 — shared foundation for the v3 core (V3-N1).

This package implements the interfaces signed at V3-N0. Two primitives that every module
needs live here rather than in a module of their own: the plan's V3-N1 file list is fixed
(``spec``, ``assurance_profiles``, ``assurance_plan``, ``assurance_state``, ``instruction``,
``candidate``, ``checks``, ``views``), so no separate primitives module is authorized and
the package root is the only home a shared foundation can have. It deliberately imports no
submodule, so importing any module never triggers a cycle.

Both primitives are **adaptations**, not imports: neither is a verbatim reuse of an older
implementation, so the two are re-implemented here with v3 shapes and their own tests:

* canonicalization / content binding — adapted from ``rsclib.harness.c14n`` (v1 lineage).
  Same normalization rules; the v3 shape is a **bare** 64-hex digest, matching the
  ``sha256`` pattern the N0 schemas actually declare, instead of v2's ``sha256:`` prefix.
* closed JSON-schema validation — adapted from ``rsclib.harness.schemas`` and the A2 fixture
  runner. The v3 pack is the frozen ``schema/document-assurance-v3/`` directory; an unknown
  document kind fails closed.

Nothing here writes a file, runs a subprocess or touches the network.
"""
from __future__ import annotations

import dataclasses
import functools
import hashlib
import json
import pathlib
import unicodedata
from typing import Any, Iterable, Mapping

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

RS_ROOT = pathlib.Path(__file__).resolve().parents[3]
SCHEMA_DIR = RS_ROOT / "schema" / "document-assurance-v3"
SCHEMA_URI_BASE = "researchsystem/schema/document-assurance-v3/"
CONTRACT_PATH = RS_ROOT / "contract" / "Document-Work-Assurance-Contract-v4.md"

#: The resolver identity stamped into every ResolvedAssurancePlan. A plan is rebuildable
#: only against the resolver version that produced it (§5.2).
RESOLVER_VERSION = "1.0.0"

SCHEMA_FILES: dict[str, str] = {
    "common": "common.schema.json",
    "spec": "document-work-spec.schema.json",
    "spec_v2": "document-work-spec.v2.schema.json",
    "profile": "document-assurance-profile.schema.json",
    "plan": "resolved-assurance-plan.schema.json",
    "state": "assurance-work-state.schema.json",
    "audit": "instruction-coverage-audit.schema.json",
    "decision": "user-decision.schema.json",
    "check": "local-check-spec.schema.json",
    "candidate": "candidate-record.schema.json",
    "paragraph_map": "paragraph-map.schema.json",
}

#: Kinds that are addressed by a pointer into a schema file rather than by its root.
SCHEMA_POINTERS: dict[str, str] = {
    "check_result": "local-check-spec.schema.json#/$defs/checkResult",
}


class AssuranceFault(Exception):
    """Environment or tooling fault: a dependency, path or schema could not be used.

    Distinct from `SpecGap`: a fault means the harness could not run, not that the work
    under assurance is deficient.
    """


class SpecGap(Exception):
    """A `SPEC_GAP`: the request cannot be interpreted under the signed v3 interfaces.

    Plan §8: a `SPEC_GAP` stops. It is never patched inside an implementation candidate and
    never downgraded into a soft finding.
    """


@dataclasses.dataclass(frozen=True)
class Issue:
    """One deterministic defect, always attributable to an exact location."""

    code: str
    message: str
    where: str = "<root>"

    def render(self) -> str:
        return f"{self.code} {self.where} — {self.message}"


@dataclasses.dataclass(frozen=True)
class Report:
    """An immutable set of issues. Empty means the checked property held."""

    issues: tuple[Issue, ...] = ()

    @property
    def ok(self) -> bool:
        return not self.issues

    def __add__(self, other: "Report") -> "Report":
        return Report(self.issues + other.issues)

    def rendered(self) -> list[str]:
        return [issue.render() for issue in self.issues]

    def require(self, exc: type[Exception] = SpecGap) -> None:
        """Raise on the first issue. Used where the contract says the run must stop."""
        if self.issues:
            raise exc(self.issues[0].render())


def report_of(issues: Iterable[Issue]) -> Report:
    return Report(tuple(issues))


# ---------------------------------------------------------------------------
# Canonicalization / content binding (adapted from the v1/v2 rs-c14n primitive)
# ---------------------------------------------------------------------------


def _canonical_value(value: Any) -> Any:
    if isinstance(value, float):
        raise AssuranceFault("canonical form forbids floating-point values")
    if isinstance(value, str):
        return unicodedata.normalize("NFC", value)
    if isinstance(value, list):
        return [_canonical_value(item) for item in value]
    if isinstance(value, dict):
        normalized: dict[str, Any] = {}
        for key, item in value.items():
            normalized_key = unicodedata.normalize("NFC", str(key))
            if normalized_key in normalized:
                raise AssuranceFault(f"duplicate key after NFC normalization: {normalized_key}")
            normalized[normalized_key] = _canonical_value(item)
        return normalized
    if value is None or isinstance(value, (bool, int)):
        return value
    raise AssuranceFault(f"unsupported canonical value: {type(value).__name__}")


def canonical_bytes(value: Any) -> bytes:
    """Deterministic UTF-8 bytes: NFC-normalized, sorted keys, no insignificant space."""
    return json.dumps(
        _canonical_value(value),
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")


def canonical_digest(value: Any) -> str:
    """Bare 64-hex SHA-256 of the canonical bytes — the shape the v3 schemas declare."""
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def bytes_digest(raw: bytes) -> str:
    """Bare 64-hex SHA-256 of raw file bytes (Markdown, plans, arbitrary artifacts)."""
    return hashlib.sha256(raw).hexdigest()


def write_canonical(path: pathlib.Path, value: Any) -> str:
    """Write a document in canonical form and return its digest.

    Canonical-on-disk keeps a stored record byte-identical to what was digested, so a later
    reader recomputes the same digest without a normalization step of its own.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = canonical_bytes(value)
    path.write_bytes(raw)
    return hashlib.sha256(raw).hexdigest()


def load_json(path: pathlib.Path | str) -> Any:
    target = pathlib.Path(path)
    try:
        with open(target, encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError as exc:
        raise AssuranceFault(f"document not found: {target}") from exc
    except json.JSONDecodeError as exc:
        raise AssuranceFault(f"document is not valid JSON: {target}: {exc}") from exc


# ---------------------------------------------------------------------------
# Closed JSON-schema validation (adapted from the v2 schema pack loader)
# ---------------------------------------------------------------------------


@functools.lru_cache(maxsize=1)
def _registry() -> Registry:
    resources = []
    for filename in SCHEMA_FILES.values():
        path = SCHEMA_DIR / filename
        if not path.exists():
            raise AssuranceFault(f"schema pack is incomplete: missing {path}")
        resources.append((SCHEMA_URI_BASE + filename, Resource.from_contents(load_json(path))))
    return Registry().with_resources(resources)


@functools.lru_cache(maxsize=None)
def _validator(kind: str) -> Draft202012Validator:
    if kind in SCHEMA_FILES and kind != "common":
        schema = load_json(SCHEMA_DIR / SCHEMA_FILES[kind])
        Draft202012Validator.check_schema(schema)
        return Draft202012Validator(schema, registry=_registry())
    if kind in SCHEMA_POINTERS:
        return Draft202012Validator(
            {"$ref": SCHEMA_URI_BASE + SCHEMA_POINTERS[kind]}, registry=_registry()
        )
    # Fail closed: an unrecognised document kind is never validated permissively.
    raise SpecGap(f"unknown document kind: {kind}")


def validate(kind: str, document: Mapping[str, Any]) -> Report:
    """Validate one document against its closed v3 schema."""
    errors = sorted(_validator(kind).iter_errors(document), key=lambda error: list(error.path))
    return report_of(
        Issue(
            f"V3-SCHEMA-{kind.upper()}",
            error.message[:300],
            "/".join(str(part) for part in error.path) or "<root>",
        )
        for error in errors
    )


def require_valid(kind: str, document: Mapping[str, Any]) -> None:
    validate(kind, document).require(SpecGap)


@functools.lru_cache(maxsize=1)
def pack_digests() -> dict[str, str]:
    """Content digests binding the signed contract text and the exact schema pack.

    Recorded alongside generated evidence so a later reader can prove which interface
    version produced it. These are generated bindings, never the product centre (V3-D5).
    """
    per_file = {
        name: bytes_digest((SCHEMA_DIR / filename).read_bytes())
        for name, filename in SCHEMA_FILES.items()
    }
    digests = {"schema_pack_digest": canonical_digest(per_file)}
    if CONTRACT_PATH.exists():
        digests["contract_digest"] = bytes_digest(CONTRACT_PATH.read_bytes())
    return digests


__all__ = [
    "AssuranceFault",
    "Issue",
    "RESOLVER_VERSION",
    "Report",
    "SCHEMA_DIR",
    "SCHEMA_FILES",
    "SpecGap",
    "bytes_digest",
    "canonical_bytes",
    "canonical_digest",
    "load_json",
    "pack_digests",
    "report_of",
    "require_valid",
    "validate",
    "write_canonical",
]
