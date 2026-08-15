"""AssuranceWorkState — one small live state and cold resume (V3-D8, N1-A10).

The state records the current status and exact pointers. Nothing else. There is no
content-addressed event chain, no CAS, no idempotency protocol and no dangling-event
recovery, because the scope is a single writer working locally: the failure this design
answers is "a new session cannot tell where the run stopped", not "two writers raced".

Cold resume is therefore a property of this file plus the records it points at. `resume`
reads the state, resolves every pointer and re-verifies every digest a pointer carries
against the bytes on disk. A pointer that no longer matches is reported rather than
followed — a stale pointer is precisely the drift that would otherwise let a run continue
against evidence that has silently moved.

Only `DIGEST_PROTECTED_FIELDS` are **written** with a digest (2026-07-29); a digest that is
present is verified wherever it appears, on protected and unprotected fields alike. The
distinction is not pedantry — every state file committed to this repository predates the
narrowing and carries digests on unprotected fields too. What the narrowing changed is what
new writes are obliged to produce, because a digest the executor computed over a file the
executor is entitled to rewrite never bound the one actor it would have to bind. Whether
any particular committed state still resolves is a question for a command, not for this
docstring.

Status *ordering* is deliberately not implemented here. The flow controller owns transition
legality and lives at V3-N2 (`flow.py`); N1 stops before semantic review, so a transition
table written now would be a guess about objects N1 cannot yet produce. This module owns
the state object and its resumability.
"""
from __future__ import annotations

import dataclasses
import pathlib
from typing import Any, Mapping

from rsclib.document_harness import (
    AssuranceFault,
    Issue,
    Report,
    bytes_digest,
    load_json,
    report_of,
    validate,
    write_canonical,
)

CODE = "V3-STATE"

#: Every pointer-shaped field on the state, in the order the flow reaches them.
POINTER_FIELDS = (
    "work_spec_ref",
    "resolved_plan_ref",
    "instruction_audit_ref",
    "start_decision_ref",
    "fulfillment_ref",
    "manifest_ref",
    "check_results_ref",
    "coverage_ref",
    "review_ref",
    "repair_decision_ref",
    "assurance_candidate_ref",
    "final_decision_ref",
    "summary_ref",
)


#: The pointer fields that still carry — and are still checked against — a bytes digest.
#:
#: The criterion is *permission*, never value: **if this file were mis-written and the
#: executor regenerated it, would that be forgery?** Yes for these five. A START / REPAIR /
#: FINAL decision is the user's authorization and a review record is the reviewer's
#: judgement, so an executor re-issuing either is signing someone else's name; the WorkSpec
#: is the paper this run is judged against, and while the executor authored its first
#: version, re-issuing it once a run has bound it is editing one's own exam. Everywhere else
#: the executor IS the legitimate author of the current version, so re-deriving that file is
#: ordinary work and a digest the executor computes over it binds nobody.
#:
#: What the surviving digests buy is narrow, and is written down so it is not over-read: they
#: catch an **uninformed mis-write** — a write that did not know the pointer was there. They
#: do not catch a rewrite of file and digest together, because the single actor they would
#: have to constrain can do both (issue-p3-corr-digest-binds-nothing-against-the-only-writer,
#: triaged CORE_CANDIDATE; narrowed from "delete them all" to this set, 2026-07-29).
DIGEST_PROTECTED_FIELDS = frozenset(
    {
        "work_spec_ref",
        "start_decision_ref",
        "repair_decision_ref",
        "final_decision_ref",
        "review_ref",
    }
)


def pointer(path: str, digest: str | None = None) -> dict[str, Any]:
    """Build a pointer. The digest is what makes a stale pointer detectable."""
    ref: dict[str, Any] = {"path": path}
    if digest:
        ref["digest_sha256"] = digest
    return ref


def pointer_to(path: str, repo_root: pathlib.Path | str) -> dict[str, Any]:
    """Build a pointer to an existing file, computing its BYTES digest here.

    What it makes executable: **when a state pointer carries a digest, that digest is of
    the pointed-at file's bytes** — w1-r1 witnessed a CANONICAL digest written where
    `resume` verifies bytes, and the run was refused at cold resume
    (issue-w1-r1-pointer-digest-kind, triaged CORE_CANDIDATE). With the digest computed
    from the file itself, that mistake has no authoring surface left; the raw
    `pointer(path, digest)` form remains only for schema compatibility. A pointer to a file
    that does not exist is a fault at write time, not a discovery left for resume.

    **Call `pointer_for` instead**, which applies this only to the fields entitled to a
    digest. Supersession-1 §3 named this helper as *the* authoring path and described a
    state pointer as carrying the bytes digest without qualification; supersession-2
    (2026-07-29) supersedes that one statement, leaving both earlier files byte-identical.
    """
    target = pathlib.Path(repo_root) / path
    if not target.is_file():
        raise AssuranceFault(f"pointer target does not exist: {path}")
    return pointer(path, bytes_digest(target.read_bytes()))


def pointer_for(field: str, path: str, repo_root: pathlib.Path | str) -> dict[str, Any]:
    """Build the pointer a given state field is entitled to.

    One place decides whether a digest is written, so the policy is a thing a test can hold
    rather than a judgement re-made at each call site. A field in `DIGEST_PROTECTED_FIELDS`
    goes through `pointer_to` and carries the bytes digest; every other field carries the
    path alone.

    The write-time existence fault is NOT part of that policy and is kept for every field: a
    pointer to a file that is not there is an authoring mistake whoever may rewrite it later,
    and the narrowing that removed the digests never argued against catching it.
    """
    if field in DIGEST_PROTECTED_FIELDS:
        return pointer_to(path, repo_root)
    if not (pathlib.Path(repo_root) / path).is_file():
        raise AssuranceFault(f"pointer target does not exist: {path}")
    return pointer(path)


def new_state(
    work_id: str,
    run_id: str,
    work_spec_ref: Mapping[str, Any],
    resolved_plan_ref: Mapping[str, Any],
    *,
    next_action: str | None = None,
) -> dict[str, Any]:
    """The state at the moment resolution completed: RESOLVED, repair round 0."""
    state: dict[str, Any] = {
        "work_id": work_id,
        "run_id": run_id,
        "status": "RESOLVED",
        "repair_round": 0,
        "work_spec_ref": dict(work_spec_ref),
        "resolved_plan_ref": dict(resolved_plan_ref),
    }
    if next_action:
        state["next_action"] = next_action
    return state


def advance(state: Mapping[str, Any], status: str, **fields: Any) -> dict[str, Any]:
    """Return a NEW state with the given status and merged fields.

    The input is never mutated: a state is a record of a moment, and rewriting it in place
    is how a run loses the ability to say what it knew when.
    """
    updated = dict(state)
    updated["status"] = status
    for key, value in fields.items():
        if value is None:
            updated.pop(key, None)
        else:
            updated[key] = value
    return updated


def check_state(state: Mapping[str, Any]) -> Report:
    """Schema validity — the closed status set and the pointer-only surface."""
    return validate("state", state)


def save(state: Mapping[str, Any], path: pathlib.Path | str) -> str:
    """Write the state canonically and return its digest."""
    check_state(state).require()
    return write_canonical(pathlib.Path(path), state)


def load(path: pathlib.Path | str) -> dict[str, Any]:
    return load_json(path)


@dataclasses.dataclass(frozen=True)
class ResumePoint:
    """What a cold session can establish from the state alone.

    Two different things were once collapsed into one `resolved` set: a pointer whose digest
    was checked and matched, and a pointer that merely exists because it carried no digest to
    check against. Both rendered as `ok`, so "we verified this" and "we never verified this"
    were indistinguishable in the output — and a digest-less pointer whose target had been
    rewritten still read as sound. They are separate sets now.

    A `pointerRef` may legitimately omit `digest_sha256` (`common.schema.json`), so an
    unverified pointer is not an error and does not fail the report. The reachable property
    is not that everything is verified — it is that what was *not* verified is visible.
    """

    state: dict[str, Any]
    verified: dict[str, str]
    present_unverified: dict[str, str]
    report: Report

    @property
    def status(self) -> str:
        return self.state["status"]

    @property
    def next_action(self) -> str:
        return self.state.get("next_action", f"continue from status {self.status}")

    def render(self) -> str:
        lines = [
            f"work_id      : {self.state['work_id']}",
            f"run_id       : {self.state['run_id']}",
            f"status       : {self.status}",
            f"repair_round : {self.state['repair_round']}",
            f"next_action  : {self.next_action}",
        ]
        for field in POINTER_FIELDS:
            if field not in self.state:
                continue
            if field in self.verified:
                mark = "ok"
            elif field in self.present_unverified:
                mark = "??"
            else:
                mark = "!!"
            lines.append(f"  {mark} {field}: {self.state[field]['path']}")
        if self.present_unverified:
            lines.append(
                f"  ?? {len(self.present_unverified)} pointer(s) carry no digest: the target "
                "exists but its bytes were NOT verified"
            )
        lines.extend("  " + issue.render() for issue in self.report.issues)
        return "\n".join(lines)


def resume(state_path: pathlib.Path | str, repo_root: pathlib.Path | str) -> ResumePoint:
    """Reconstruct a run's position from the state file and its pointers (N1-A10).

    No event chain is replayed and no earlier record is required: everything needed is the
    state document plus the files it points at.
    """
    root = pathlib.Path(repo_root)
    state = load(state_path)
    issues = list(check_state(state).issues)
    verified: dict[str, str] = {}
    present_unverified: dict[str, str] = {}

    for field in POINTER_FIELDS:
        ref = state.get(field)
        if not ref:
            continue
        target = root / ref["path"]
        if not target.exists():
            issues.append(
                Issue(f"{CODE}-POINTER-MISSING", f"pointer target does not exist: {ref['path']}", field)
            )
            continue
        expected = ref.get("digest_sha256")
        if not expected:
            # Existence is all this pointer can establish. It is recorded separately so it
            # is never counted as a verified one — the bytes at that path may have changed
            # since the pointer was written and nothing here could tell.
            present_unverified[field] = ref["path"]
            if field in DIGEST_PROTECTED_FIELDS:
                # ...and on a protected field that is a defect, not merely a limit: its current
                # version is not the executor's to produce, so a pointer that took no
                # binding leaves nothing able to say the file is still the one authorized.
                # It stays in `present_unverified` as well — rendering it `??` is the
                # N1-A10 property, and reporting the issue instead of it would delete a
                # recorded behaviour to make room for a new one.
                issues.append(
                    Issue(
                        f"{CODE}-POINTER-UNVERIFIED",
                        f"pointer carries no digest, so the bytes at {ref['path']} were "
                        "NOT bound; this field names a file the executor may not re-issue",
                        field,
                    )
                )
            continue
        if bytes_digest(target.read_bytes()) != expected:
            issues.append(
                Issue(
                    f"{CODE}-POINTER-STALE",
                    f"pointer digest no longer matches the bytes at {ref['path']}",
                    field,
                )
            )
            continue
        verified[field] = ref["path"]

    return ResumePoint(
        state=state,
        verified=verified,
        present_unverified=present_unverified,
        report=report_of(issues),
    )
