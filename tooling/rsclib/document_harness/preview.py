"""RunPreview — deterministic pre-START rendering of a run's frozen control plane.

What the user approves at START is the control plane itself: the instruction's numbered
sections, the checks the resolved plan will run, and the digests the START decision binds
(N1-A4). Until round PREVIEW-RENDER the human-readable form of that plane was assembled by
the orchestrating session — a transcription, with a transcription's failure mode: what the
user read was whatever the session wrote, not what the plane said. This module removes the
transcriber. The preview is a pure function of the run directory's bytes, so re-rendering
is always possible and storing the rendering is never necessary (the 2026-08-21 ruling:
what a script can re-derive is not recorded).

Two properties are the design:

* **Deterministic.** The output depends on the input files and the run directory's name —
  the one input beyond their bytes — and nothing else: no clock, no randomness, no
  environment, no absolute paths. Rendering the same run directory twice yields identical
  bytes, which is what makes "re-derive instead of store" honest.
* **Render, never judge.** The preview states what the plane contains and recomputes the
  digests START will bind. The one comparison it prints — the plan's recorded WorkSpec
  digest against the WorkSpec bytes on disk — is wrong-candidate visibility (the same
  principle as ObligationCoverage): both values are shown, and the gates that judge the
  plane (`check_template_instance.py`, the coverage audit, review) are untouched by it.

The instruction is rendered whole, verbatim, with one elision: a Context section is named
with its line span but its body is not rendered, because it is non-normative by its own
heading and rendering it would put non-binding prose inside the surface the user is asked
to approve. Everything else — preamble, title, every numbered section, any unnumbered
normative section — appears as its own bytes, so eliding cannot drop an obligation. The
exemption is `_is_context_title`'s: only the heading that IS the Context section, exactly.
The elision inherits `form_conformance`'s stated ceiling unchanged: an unmarked normative
sentence hiding inside the real Context section is invisible to the form's gates and
equally absent from this preview — that defect lives in the instruction, and the preview
does not add a second judge of it.
"""
from __future__ import annotations

import pathlib
from typing import Any, Mapping

from rsclib.document_harness import SpecGap, bytes_digest, canonical_digest, load_json
from rsclib.document_harness.instruction import (
    _heading_spans,
    _is_context_title,
    declared_form,
    numbered_sections,
)

CODE = "V3-PREVIEW"

RULE = "=" * 72
LINE = "-" * 72

#: The plane's core: absent any of these there is nothing coherent to preview.
REQUIRED = (
    "instruction.md",
    "control/work-spec.json",
    "control/resolved-plan.json",
    "control/instruction-audit.json",
)


def _instruction_body(instruction_text: str) -> list[str]:
    """The instruction verbatim, with each Context body elided under a note.

    The elision is bounded by ownership, not by the Context span alone: a heading nested
    inside that span — a numbered section, an appendix — opens a section of its own, and
    from its line onward the bytes belong to it, not to Context, so elision stops there
    and those lines render. Only lines whose innermost enclosing heading IS the Context
    heading are elided, which is what keeps "eliding cannot drop an obligation" true of
    the code: the FULL of 57d1312 (B-2) measured the unbounded form swallowing a nested
    `### R0` whole while `coherent` stayed True.
    """
    lines = instruction_text.splitlines()
    spans = _heading_spans(lines)
    elide: dict[int, int] = {}
    for span in spans:
        if not _is_context_title(span["title"]):
            continue
        first_body = span["start_line"] + 1  # the heading itself stays
        end = span["end_line"]
        nested = [s["start_line"] for s in spans if first_body <= s["start_line"] <= end]
        if nested:
            end = min(nested) - 1
        if first_body <= end:
            elide[first_body] = end
    out: list[str] = []
    number = 1
    while number <= len(lines):
        if number in elide:
            end = elide[number]
            out.append(
                f"    [lines {number}-{end} not rendered: the section above is "
                "non-normative by its own heading; read instruction.md for its body]"
            )
            number = end + 1
        else:
            out.append(lines[number - 1])
            number += 1
    return out


def _obligations_by_check(spec: Mapping[str, Any]) -> dict[str, list[str]]:
    by_check: dict[str, list[str]] = {}
    for obligation in spec["obligations"]:
        for check_id in obligation.get("local_check_refs", ()):
            by_check.setdefault(check_id, []).append(obligation["obligation_id"])
    return by_check


def render_preview(run_dir: pathlib.Path | str) -> tuple[str, bool]:
    """Render the START preview of the control plane under `run_dir`.

    Returns `(text, coherent)`: `coherent` is False when the plane renders but is missing
    a referenced check spec or disagrees with itself. A missing core file is a `SpecGap`
    naming every absentee — an incomplete plane has no approval surface to render.
    """
    root = pathlib.Path(run_dir)
    missing = [rel for rel in REQUIRED if not (root / rel).is_file()]
    if missing:
        raise SpecGap(f"{CODE}-INCOMPLETE control plane is missing: " + ", ".join(missing))

    instruction_text = (root / "instruction.md").read_text(encoding="utf-8")
    spec = load_json(root / "control" / "work-spec.json")
    plan = load_json(root / "control" / "resolved-plan.json")
    audit = load_json(root / "control" / "instruction-audit.json")

    coherent = True
    out: list[str] = []
    put = out.append

    put(RULE)
    put("Document Work Assurance v3 — START preview (rendered from the frozen control plane)")
    put(RULE)
    ref = spec["instruction_ref"]
    sections = numbered_sections(instruction_text)
    put(f"run dir     : {root.name}")
    put(f"work_id     : {spec['work_id']}")
    put(f"objective   : {spec['objective']}")
    put(
        f"work spec   : schema_version {spec.get('schema_version', '1 (undeclared)')} · "
        f"{len(spec['obligations'])} obligation(s) · "
        f"{len(spec.get('instruction_units', ()))} instruction unit(s)"
    )
    put(
        f"instruction : {ref['path']} @ {ref.get('revision', '(no revision)')} — "
        "rendered below from the run directory's copy"
    )
    put(
        f"plan        : {plan['plan_id']} · resolver {plan['resolver_version']} · "
        f"repair_cap {plan['repair_cap']}"
    )
    boundary = plan["effective_change_boundary"]
    put("boundary    : write_scope: " + ", ".join(boundary["write_scope"]))
    put("              out: " + ", ".join(boundary["out"]))
    put(f"audit       : {audit['result']} · by {audit['audited_by']} at {audit['audited_at']}")
    put("")

    put(LINE)
    put("Bindings the START decision will carry (N1-A4) — recomputed from the bytes on disk")
    put(LINE)
    put(f"resolved_plan.digest_sha256     = {canonical_digest(plan)}")
    put(f"instruction_audit.digest_sha256 = {canonical_digest(audit)}")
    put("")
    put("Cross-references already frozen inside the plane:")
    recorded = plan["work_spec_ref"].get("digest_sha256", "(absent)")
    computed = canonical_digest(spec)
    put(f"plan.work_spec_ref.digest_sha256 = {recorded}")
    put(f"work-spec.json bytes on disk     = {computed}")
    if recorded != computed:
        coherent = False
        put("  MISMATCH — the plan binds a different WorkSpec than the bytes on disk")
    put(f"instruction.md bytes sha256      = {bytes_digest(instruction_text.encode('utf-8'))}")
    put("")

    put(LINE)
    put("The authorization body — the instruction, verbatim (Context elided)")
    put(LINE)
    form = declared_form(instruction_text)
    section_list = " · ".join(
        f"{s['label']} (lines {s['start_line']}-{s['end_line']})" for s in sections
    ) or "(none)"
    put(f"form: {form or '(undeclared)'} · numbered sections: {section_list}")
    put("")
    out.extend(_instruction_body(instruction_text))
    put("")

    host_table = root / "control" / "host-table.md"
    if host_table.is_file():
        put(LINE)
        put("Host table (control/host-table.md, verbatim)")
        put(LINE)
        out.extend(host_table.read_text(encoding="utf-8").splitlines())
        put("")

    put(LINE)
    put("The machine half — checks in resolved-plan order")
    put(LINE)
    by_check = _obligations_by_check(spec)
    check_order = plan.get("check_order")
    if check_order is None:
        # The plan schema's own description: absent when the run has no deterministic
        # checks. A legal shape, so it renders as a fact rather than crashing (FULL
        # of 57d1312, L-2 — the crash exited with the code RESULT reserves for
        # "incoherent").
        put("(the plan records no check order — absent when the run has no deterministic checks)")
        check_order = []
    for position, check_id in enumerate(check_order, start=1):
        path = root / "control" / f"check-{check_id}.json"
        if not path.is_file():
            coherent = False
            put(f"{position:3d}. {check_id}  MISSING — control/check-{check_id}.json not found")
            continue
        check = load_json(path)
        obligations = ", ".join(by_check.get(check_id, ())) or "(no obligation references it)"
        put(
            f"{position:3d}. {check_id}  kind={check['kind']}  "
            f"subject={check['subject_tree']}  obligations: {obligations}"
        )
    unplanned = sorted(set(by_check) - set(check_order))
    if unplanned:
        coherent = False
        put("obligations reference checks absent from the plan order: " + ", ".join(unplanned))
    put("")

    review_only = [
        obligation
        for obligation in spec["obligations"]
        if obligation.get("verification_mode") == "review_only"
    ]
    if review_only:
        put(LINE)
        put("Review-only obligations — no deterministic check decides these")
        put(LINE)
        for obligation in review_only:
            put(f"{obligation['obligation_id']}: {obligation['requirement']}")
            put(f"    rationale        : {obligation.get('review_only_rationale', '(absent)')}")
            put(f"    NOT_SUPPORTED if : {obligation.get('not_supported_when', '(absent)')}")
        put("")

    put(LINE)
    put("Derived entirely from the run directory's bytes; re-run `dtw preview` to re-derive.")
    put("Not stored, and not an approval: START is the user's decision, recorded by the")
    put("run's own start script in control/user-decision-start.json.")
    return "\n".join(out) + "\n", coherent
