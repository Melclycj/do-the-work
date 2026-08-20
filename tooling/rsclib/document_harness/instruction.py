"""The pre-start instruction coverage audit and the START binding (V3-D7, V3-D4, N1-A4).

Two distinct things happen before a run may start, and conflating them is the failure this
module prevents:

1. an **instruction auditor** — a context distinguishable from the executor — establishes
   once that the raw instruction was decomposed into units and obligations without
   omission. Its closed result is `COVERED | SPEC_GAP`; there is no repair loop. A
   `SPEC_GAP` needs a new WorkSpec revision and a new START decision. Under the prose form
   that auditor *judges*, in a fresh context. Under the enumerated form it *decides*:
   `transcript_audit` is a deterministic function over the frozen instruction and the unit
   map, and the user ruled 2026-08-05 that it satisfies §6 — what the clause buys is that
   the omission question is not answered by the party being answered about, and a verdict
   anyone can re-run to the same answer meets that more strongly than a differently-named
   context does. What it costs is stated at `transcript_audit` and in EXECUTION.md:
   coverage is established, faithful restatement is not.
2. the **user** makes one START decision bound to the exact ResolvedAssurancePlan and the
   exact audit. That is a workflow gate, not proof that pre-start writes were impossible,
   and there is no second approval or activation path anywhere in v3 (V3-D4).

The audit is a preflight judgment, not a proof. V3 never claims an AI enumerated every
semantic implication of an instruction; the user is the trust terminal for this result, and
FULL review later rechecks instruction completeness against the raw instruction again.

Two mechanical helpers live here. `paragraph_skeleton` (Phase C4) enumerates the frozen
instruction paragraph by paragraph so the run-v2 authoring gate can refuse a unit map that
silently skips text (M11) — the enumeration is derived, the classification stays human.
`resolve_form` (SIMP-C1/C2, 2026-08-05) decides which form the instruction is in, because
the derived artifacts a run owes differ by form: under `enumerated` the unit map is a
transcript of the numbered sections, so the paragraph map and the preamble gate have no
object; under `prose` every one of them still earns its keep. The branch is fail-heavy —
anything undecidable resolves to `prose`.
"""
from __future__ import annotations

import pathlib
import re
from typing import Any, Mapping

from rsclib.document_harness import (
    Issue,
    Report,
    SpecGap,
    bytes_digest,
    canonical_digest,
    load_json,
    report_of,
    validate,
)
from rsclib.document_harness.checks import frontmatter_scalars
from rsclib.document_harness.enumerations import set_equality
from rsclib.document_harness.spec import spec_digest

CODE = "V3-AUDIT"
DECISION_CODE = "V3-START"


def _fence_run(line: str) -> str | None:
    """The fence-marker run of a line, per a simplified CommonMark rule.

    A run of three or more backticks or tildes indented at most three spaces. Returns
    the run itself (e.g. ``````` or ``~~~~``) or None. Deliberately simplified: any
    matching run at least as long as the opening one closes a fence — full CommonMark
    info-string/closing subtleties buy nothing for instruction files and would make the
    enumeration harder to re-derive by eye.
    """
    stripped = line.lstrip(" ")
    if len(line) - len(stripped) > 3:
        return None
    for char in ("`", "~"):
        if stripped.startswith(char * 3):
            return char * (len(stripped) - len(stripped.lstrip(char)))
    return None


def paragraph_skeleton(instruction_text: str) -> tuple[dict[str, Any], ...]:
    """Deterministic paragraph enumeration of a frozen instruction (M11, defect #8).

    The unit map used to be picked by hand, and an omission was invisible: p3-corr's
    audit returned COVERED over a map that had silently missed three normative units.
    This skeleton is the mechanical half of the fix — every block of the instruction is
    enumerated, so a paragraph can be misclassified but never silently absent.

    A paragraph is a maximal run of non-blank lines; blank lines inside a fenced code
    block do not split (see `_fence_run`; an unclosed fence runs to the end). Lines are
    1-based and inclusive. The digest is SHA-256 over the block's lines joined with
    ``"\\n"`` and UTF-8 encoded, so line endings are normalized before binding.

    Classification is deliberately NOT emitted: it is the one human-owned column of the
    run-local paragraph map, and a machine default here would be defect M8 — a status
    nobody asserted — in a new place.
    """
    lines = instruction_text.splitlines()
    entries: list[dict[str, Any]] = []
    block_start: int | None = None
    fence: str | None = None

    def close(end_line: int) -> None:
        nonlocal block_start
        if block_start is None:
            return
        block = "\n".join(lines[block_start - 1 : end_line])
        entries.append(
            {
                "index": len(entries) + 1,
                "start_line": block_start,
                "end_line": end_line,
                "digest_sha256": bytes_digest(block.encode("utf-8")),
            }
        )
        block_start = None

    for number, line in enumerate(lines, start=1):
        run = _fence_run(line)
        if fence is None:
            if not line.strip():
                close(number - 1)
                continue
            if block_start is None:
                block_start = number
            if run:
                fence = run
        elif run and run[0] == fence[0] and len(run) >= len(fence):
            fence = None
    close(len(lines))
    return tuple(entries)


# ---------------------------------------------------------------------------
# Instruction form (SIMP-C1 / SIMP-C2) — which derived artifacts a run actually owes
# ---------------------------------------------------------------------------

FORM_ENUMERATED = "enumerated"
FORM_PROSE = "prose"

#: A numbered requirement heading: any heading level whose text opens with R<digits>.
_NUMBERED_HEADING = re.compile(r"^#{1,6}\s+R(\d+)\b")
_HEADING = re.compile(r"^(#{1,6})\s+(.*)$")

#: Markers that put a sentence's normative force beyond doubt. Deliberately short: this is a
#: *sufficient* signal, never a complete one — see `form_conformance`'s ceiling.
_NORMATIVE_MARKERS = ("(normative)", "MUST", "SHALL", "REQUIRED", "必须", "不得", "禁止")


def declared_form(instruction_text: str) -> str | None:
    """The instruction's own `form:` frontmatter declaration, or None when it makes none.

    SIMP-C1: the instruction declares its own shape rather than having one inferred. The
    rejected alternative was to have a model read the file and judge — an unrecorded
    judgment with no evidence lock, and the same "interpret the prose" step this round
    exists to delete, merely moved earlier.
    """
    return frontmatter_scalars(instruction_text.encode("utf-8")).get("form")


def _is_context_title(title: str) -> bool:
    """Is this heading *the* Context section, rather than a heading that mentions context?

    Tightened twice, because the first tightening kept the defect it was written to close.
    It began as `"context" in title`, which exempted `## Appendix A — the frozen context
    bindings` — a normative frozen table passing as non-normative and taking the
    enumerated form's whole justification with it, since the paragraph map and the
    preamble gate switch off precisely because no prose is supposed to sit outside a
    numbered section (`v3-review-full-3657687.md` f1). It became
    `.startswith("context")`, which exempted `## Contextual appendix — the frozen
    bindings` with the same table under it and the same three artifacts switched off
    (`v3-review-verify-c7fb720.md` `V-1`, reproduced at that tip and again at this one).
    A prefix is not a section, and the sentence this docstring used to end with —
    *anything else falls to the prose form* — was measured false of its own code both
    times. It is now the rule rather than a claim about one: the heading has to **be** the
    section.

    Ground, re-measured immediately before this text: all seven real instructions
    (`p3-corr`, `p4-bridge`, `p4-doc`, `p5a-firewall`, `p5a-shells`, `p5b-firewall`,
    `w1-r1`) head it exactly `## Context (non-normative)`, so the conforming vocabulary
    loses nothing. Case is the one variation tolerated — a shouted heading is still that
    section, and no defect shape turns on it; every heading that is not that section now
    falls to the prose form, which is the direction `resolve_form` promises for whatever
    it cannot decide.

    **Unchanged, so the record does not read as though it were closed.** This decides
    which heading is exempt, never what sits under it: an unmarked normative declarative
    inside the real Context section is still invisible here (`form_conformance`'s stated
    ceiling), and `_NORMATIVE_MARKERS` is still case-sensitive, so lower-case `must` there
    raises nothing (`v3-review-verify-c7fb720.md` `O-4`).
    """
    return title.casefold() == "context (non-normative)"


def _frontmatter_end(lines: list[str]) -> int:
    """The 1-based line of the frontmatter's closing fence, or 0 when there is none.

    The declaration is structure, not content: without this the block carrying it would be
    reported as prose outside every section, and the conforming shape could never pass.
    """
    if not lines or lines[0].lstrip("﻿").strip() != "---":
        return 0
    for number, line in enumerate(lines[1:], start=2):
        if line.strip() in ("---", "..."):
            return number
    return 0


def _heading_spans(lines: list[str]) -> list[dict[str, Any]]:
    """Every heading's span, in file order: through the last line before the next heading of
    the same or higher level. Nested headings appear later, so the innermost span containing
    a line is the last one that contains it."""
    spans: list[dict[str, Any]] = []
    for number, line in enumerate(lines, start=1):
        match = _HEADING.match(line)
        if match:
            spans.append(
                {
                    "start_line": number,
                    "end_line": len(lines),
                    "level": len(match.group(1)),
                    "title": match.group(2).strip(),
                    "numbered": bool(_NUMBERED_HEADING.match(line)),
                }
            )
    for index, span in enumerate(spans):
        for later in spans[index + 1:]:
            if later["level"] <= span["level"]:
                span["end_line"] = later["start_line"] - 1
                break
    return spans


def numbered_sections(instruction_text: str) -> tuple[dict[str, Any], ...]:
    """Every `R<n>` requirement section, in file order: label, number, line span.

    This is the enumerated form's unit of work: one section is one obligation, which is what
    makes the WorkSpec a transcript rather than an interpretation (SIMP-B1).
    """
    lines = instruction_text.splitlines()
    sections = []
    for span in _heading_spans(lines):
        if span["numbered"]:
            match = _NUMBERED_HEADING.match(lines[span["start_line"] - 1])
            sections.append(
                {
                    "label": f"R{int(match.group(1))}",
                    "number": int(match.group(1)),
                    "start_line": span["start_line"],
                    "end_line": span["end_line"],
                    "title": span["title"],
                }
            )
    return tuple(sections)


def form_conformance(instruction_text: str) -> tuple[str, ...]:
    """Everything that keeps an `enumerated` declaration from being established (SIMP-C2).

    The declaration is verified structurally, not by sniffing tone: under the enumerated
    form every block of prose lives inside a numbered section or inside the non-normative
    Context section, and nothing else. A block sitting outside both is text no obligation
    can be a transcript of — the START approval surface would be narrower than the
    instruction, which is exactly the defect w1-r1 and p4-bridge each paid for once.

    **Ceiling, stated rather than papered over.** This cannot detect a normative
    declarative sentence *inside* the Context section that carries no marker word. Context
    is declared non-normative and covered by a context-unit rationale, and the backstop is
    unchanged: FULL review re-walks the raw instruction against the unit map (REVIEW.md).
    What this closes is the silent-absence class, not the misclassification class — the same
    boundary `paragraph_skeleton` draws for the prose form.
    """
    lines = instruction_text.splitlines()
    spans = _heading_spans(lines)
    sections = numbered_sections(instruction_text)
    issues: list[str] = []

    if not sections:
        issues.append(
            "FORM-NO-NUMBERED-SECTIONS: the instruction declares form 'enumerated' but "
            "carries no R<n> requirement heading, so there is nothing to transcribe"
        )
    labels = [section["label"] for section in sections]
    for label in sorted({label for label in labels if labels.count(label) > 1}):
        issues.append(
            f"FORM-DUPLICATE-SECTION: {label} appears {labels.count(label)} times; a "
            "duplicated label makes 'one section, one obligation' undecidable"
        )

    def innermost(line_number: int) -> dict[str, Any] | None:
        found = None
        for span in spans:
            if span["start_line"] <= line_number <= span["end_line"]:
                found = span
        return found

    frontmatter_end = _frontmatter_end(lines)
    for entry in paragraph_skeleton(instruction_text):
        numbered_lines = [
            (number, lines[number - 1])
            for number in range(entry["start_line"], entry["end_line"] + 1)
        ]
        content = [
            (number, line)
            for number, line in numbered_lines
            if number > frontmatter_end and not line.lstrip().startswith("#")
        ]
        if not content:
            continue  # frontmatter and heading lines are structure, not content
        block = [line for _, line in content]
        span = innermost(content[0][0])
        title = (span or {}).get("title", "")
        in_context = _is_context_title(title)
        if span is None or not (span["numbered"] or in_context):
            issues.append(
                f"FORM-BLOCK-OUTSIDE-SECTIONS: lines {entry['start_line']}-"
                f"{entry['end_line']} carry prose under {title or 'no heading'!r}, which is "
                "neither a numbered section nor Context; under the enumerated form no "
                "obligation can be a transcript of it"
            )
            continue
        if in_context:
            for marker in _NORMATIVE_MARKERS:
                if marker in "\n".join(block):
                    issues.append(
                        f"FORM-NORMATIVE-IN-CONTEXT: lines {entry['start_line']}-"
                        f"{entry['end_line']} carry {marker!r} inside a section declared "
                        "non-normative; a demand there sits in no obligation"
                    )
                    break
    return tuple(issues)


def resolve_form(instruction_text: str) -> tuple[str, tuple[str, ...]]:
    """The effective form and why — the single entry every caller uses (SIMP-B3 + SIMP-C2).

    Fail-heavy by construction: `enumerated` is returned only for an instruction that both
    declares it and survives `form_conformance`. Anything else — no declaration, a
    misspelled one, a declaration the structure does not bear out — resolves to `prose`,
    the form that owes every derived artifact. The branch lives here and not in each caller
    so that "could not decide" can never be spelled as the cheap answer somewhere.
    """
    declared = declared_form(instruction_text)
    if declared is None:
        return FORM_PROSE, ("form: not declared — the prose form applies",)
    if declared != FORM_ENUMERATED:
        return FORM_PROSE, (f"form: {declared!r} is not {FORM_ENUMERATED!r}",)
    issues = form_conformance(instruction_text)
    if issues:
        return FORM_PROSE, ("form: 'enumerated' declared but not established:",) + issues
    return FORM_ENUMERATED, ()


def transcript_audit(
    spec: Mapping[str, Any], instruction_text: str
) -> tuple[str, tuple[dict[str, Any], ...]]:
    """The enumerated form's coverage judgment, decided mechanically (SIMP-B1).

    Returns `(result, findings)` shaped for the `InstructionCoverageAudit` document. The
    artifact, its digest and its START binding are unchanged — what this replaces is the
    *execution round*: a fresh-context agent re-reading the frozen instruction end to end
    to answer a question that, once the instruction is a numbered list, a diff answers. The
    measured cost of that round was four from-scratch opus walks on run `p5a-firewall`.

    Five defect classes, each mapped to the closed `auditFindingKind` it actually is:

    * a numbered section no obligation-classified unit anchors into — `UNMAPPED_NORMATIVE_TEXT`,
      the p3-corr omission class, and the only one the deleted walk was reliably catching;
    * a unit whose anchor appears nowhere in the instruction — `BROKEN_LOCATOR`;
    * a unit whose anchor appears in more than one numbered section — `AMBIGUOUS_UNIT`;
    * a unit anchored *inside* a numbered section but classified `context`, or anchored
      outside every numbered section *and* outside every Context section —
      `UNJUSTIFIED_CONTEXT`: under this form a numbered section is a requirement, so
      declaring one non-normative is how a demand leaves the approval surface quietly, and
      being merely outside the requirements is not being inside Context;
    * a unit that maps a requirement section but names no obligation —
      `MISSING_OBLIGATION_LINK`.

    **Writing the result.** On `COVERED` the second element is the empty tuple and the
    caller must omit the key entirely: the audit schema forbids `findings` on `COVERED` and
    requires `minItems: 1` elsewhere, so `"findings": []` is refused twice over.

    **Ceiling, and it is a real reduction.** This establishes that every numbered section
    reaches an obligation. It does not establish that the obligation's `requirement` text is
    a faithful restatement of that section — a human auditor could have judged that, and no
    longer does. The disclosure belongs in the audit record's `audited_by` and in
    EXECUTION.md; the backstop is unchanged and independent: FULL review re-walks the raw
    instruction against the unit map (contract §6's last sentence, REVIEW.md).
    """
    sections = numbered_sections(instruction_text)
    lines = instruction_text.splitlines()
    section_text = {
        section["label"]: "\n".join(lines[section["start_line"] - 1 : section["end_line"]])
        for section in sections
    }
    heading_of = {
        section["label"]: lines[section["start_line"] - 1][:300] for section in sections
    }
    context_text = tuple(
        "\n".join(lines[span["start_line"] - 1 : span["end_line"]])
        for span in _heading_spans(lines)
        if _is_context_title(span["title"])
    )
    instruction_path = spec.get("instruction_ref", {}).get("path")
    findings: list[dict[str, Any]] = []
    covered: set[str] = set()

    for unit in spec.get("instruction_units", []):
        locator = unit.get("locator", {})
        anchor = locator.get("anchor", "")
        if locator.get("path") != instruction_path or not anchor:
            continue
        unit_id = unit.get("unit_id", "unknown-unit")
        hits = [label for label, text in section_text.items() if anchor in text]
        if not hits:
            if anchor not in instruction_text:
                findings.append(
                    _finding(
                        f"audit-broken-locator-{unit_id}",
                        "BROKEN_LOCATOR",
                        instruction_path,
                        anchor,
                        f"unit {unit_id} anchors text the frozen instruction does not carry",
                    )
                )
            elif not any(anchor in text for text in context_text):
                # Tightened 2026-08-05 (FULL f1, the same defect on this leg): "outside the
                # numbered sections" was read as "therefore a Context unit", so a unit
                # anchoring an appendix — text in no requirement and in no Context section —
                # was silently legitimate. Being outside is not being inside Context.
                findings.append(
                    _finding(
                        f"audit-outside-{unit_id}",
                        "UNJUSTIFIED_CONTEXT",
                        instruction_path,
                        anchor,
                        f"unit {unit_id} anchors text that is in no numbered section and in "
                        "no Context section, so nothing carries it into the approval surface",
                    )
                )
            continue
        if len(hits) > 1:
            findings.append(
                _finding(
                    f"audit-ambiguous-{unit_id}",
                    "AMBIGUOUS_UNIT",
                    instruction_path,
                    anchor,
                    f"unit {unit_id} anchors into {len(hits)} numbered sections "
                    f"({', '.join(sorted(hits))}); which requirement it maps is undecided",
                )
            )
            continue
        label = hits[0]
        if unit.get("classification") != "obligation":
            findings.append(
                _finding(
                    f"audit-context-in-{label.lower()}",
                    "UNJUSTIFIED_CONTEXT",
                    instruction_path,
                    heading_of[label],
                    f"unit {unit_id} sits inside requirement section {label} but is "
                    "classified context; a numbered section is a requirement",
                )
            )
            continue
        if not unit.get("obligation_ids"):
            findings.append(
                _finding(
                    f"audit-unlinked-{unit_id}",
                    "MISSING_OBLIGATION_LINK",
                    instruction_path,
                    heading_of[label],
                    f"unit {unit_id} maps requirement section {label} but names no obligation",
                )
            )
            continue
        covered.add(label)

    coverage = set_equality(
        covered,
        section_text,
        subject="numbered sections reached by an obligation",
        found_label="mapped",
        expected_label="instruction",
    )
    for label in sorted(set(section_text) - covered):
        findings.append(
            _finding(
                f"audit-unmapped-{label.lower()}",
                "UNMAPPED_NORMATIVE_TEXT",
                instruction_path,
                heading_of[label],
                f"requirement section {label} is reached by no obligation-classified unit; "
                "its text would be outside the START approval surface",
            )
        )
    if not coverage.ok and not findings:
        # The vacuous case: no sections at all, so nothing above could fire.
        findings.append(
            _finding(
                "audit-no-numbered-sections",
                "UNMAPPED_NORMATIVE_TEXT",
                instruction_path or "",
                "(no numbered section)",
                "the instruction carries no R<n> requirement section, so there is nothing "
                "for the WorkSpec to be a transcript of",
            )
        )

    return ("SPEC_GAP" if findings else "COVERED"), tuple(findings)


def _finding(
    finding_id: str, kind: str, path: str | None, anchor: str, description: str
) -> dict[str, Any]:
    return {
        "finding_id": finding_id,
        "kind": kind,
        "instruction_locator": {"path": path or "", "anchor": anchor},
        "description": description,
    }


def load_audit(path: pathlib.Path | str) -> dict[str, Any]:
    return load_json(path)


def check_audit(
    audit: Mapping[str, Any],
    spec: Mapping[str, Any],
    *,
    executor: str | None = None,
) -> Report:
    """Schema validity plus the binding invariants (invariant 1).

    An audit that does not bind the exact WorkSpec bytes it judged is worthless: it would
    let a revised spec inherit an approval granted to an earlier one.

    `executor` stays optional in the signature but never optional in the *report*: omitting
    it yields `V3-AUDIT-AUDITOR-DISTINCTNESS-UNVERIFIED` rather than silence, so a caller
    cannot switch the guard off by not passing an argument.

    **Permanent residual, deliberately not pursued.** Comparing `audited_by` against the
    executor's name proves only that two declared *names* differ. It cannot prove the two
    contexts were actually independent: an executor writing `audited_by: "Auditor Ada"`
    passes. Contract §1 settles this — role separation is a workflow protocol, not an OS
    guarantee — and trying to mechanize it further would be the regression class V3-N0 hit,
    where a check is stretched past what it can honestly establish. The reachable endpoint
    is that an unverified property is *visible*, not that every property is verified.

    **Under the enumerated form this comparison is satisfied by construction** (SIMP-B1,
    2026-08-05): the audit is produced by `transcript_audit` and `audited_by` names the
    mechanism, so it can never equal an executor's name and this guard can never fail
    there. Its passing is therefore not evidence of anything in that form — the evidence is
    that the verdict is a diff anyone can re-run, which is a stronger property than two
    differing names, and it is *why* the user ruled a deterministic function satisfies
    contract §6's distinguishable auditor. Under the prose form an auditor context still
    supplies the name and the comparison still has an object.
    """
    schema_report = validate("audit", audit)
    if not schema_report.ok:
        return schema_report

    issues: list[Issue] = []
    if audit["work_id"] != spec["work_id"]:
        issues.append(
            Issue(f"{CODE}-WORK-MISMATCH", "audit names a different work_id than the spec", "work_id")
        )

    expected_digest = spec_digest(spec)
    if audit["work_spec_ref"]["digest_sha256"] != expected_digest:
        issues.append(
            Issue(
                f"{CODE}-SPEC-DIGEST-MISMATCH",
                "audit was performed against different WorkSpec bytes than the ones supplied",
                "work_spec_ref/digest_sha256",
            )
        )

    spec_instruction = spec["instruction_ref"]
    audit_instruction = audit["instruction_ref"]
    for field in ("path", "revision"):
        if audit_instruction.get(field) != spec_instruction.get(field):
            issues.append(
                Issue(
                    f"{CODE}-INSTRUCTION-MISMATCH",
                    f"audit judged a different frozen instruction ({field})",
                    "instruction_ref",
                )
            )

    # Role separation is a workflow protocol, not an OS guarantee (contract §1) — but the
    # one thing that can be checked mechanically is that the same actor did not both write
    # the work and certify that the instruction was fully mapped.
    #
    # When no executor identity is supplied the guard cannot run, and an absent guard must
    # never read as a passing one: silence here would be indistinguishable from "checked and
    # distinct". The unchecked state is reported instead of skipped.
    if executor is None:
        issues.append(
            Issue(
                f"{CODE}-AUDITOR-DISTINCTNESS-UNVERIFIED",
                "no executor identity was supplied, so auditor/executor distinctness was not "
                "checked; this is an unverified property, not a satisfied one",
                "audited_by",
            )
        )
    elif audit["audited_by"].strip().casefold() == executor.strip().casefold():
        issues.append(
            Issue(
                f"{CODE}-AUDITOR-NOT-DISTINGUISHABLE",
                f"the audit was performed by the executor of the same run: {executor}",
                "audited_by",
            )
        )

    return schema_report + report_of(issues)


def require_covered(audit: Mapping[str, Any]) -> None:
    """Raise `SpecGap` unless the audit returned `COVERED` (invariant 1).

    `SPEC_GAP` stops the run. It is not a finding to be repaired inside the candidate: the
    instruction map itself was incomplete, so there is nothing sound to execute against.
    """
    if audit["result"] != "COVERED":
        findings = audit.get("findings", [])
        detail = "; ".join(f"{f['kind']}:{f['finding_id']}" for f in findings) or "no findings listed"
        raise SpecGap(f"{CODE}-SPEC-GAP instruction coverage audit did not return COVERED ({detail})")


def audit_digest(audit: Mapping[str, Any]) -> str:
    return canonical_digest(audit)


def check_start_decision(
    decision: Mapping[str, Any],
    plan: Mapping[str, Any],
    audit: Mapping[str, Any],
) -> Report:
    """A START decision must bind the exact plan and the exact audit (N1-A4)."""
    schema_report = validate("decision", decision)
    if not schema_report.ok:
        return schema_report

    issues: list[Issue] = []
    if decision["phase"] != "START":
        return report_of(
            [Issue(f"{DECISION_CODE}-PHASE", f"expected a START decision, got {decision['phase']}", "phase")]
        )

    if decision["work_id"] != plan["work_id"]:
        issues.append(
            Issue(f"{DECISION_CODE}-WORK-MISMATCH", "decision names a different work_id", "work_id")
        )

    target = decision["target"]
    bindings = (
        ("resolved_plan_ref", canonical_digest(plan), "ResolvedAssurancePlan"),
        ("instruction_audit_ref", canonical_digest(audit), "InstructionCoverageAudit"),
    )
    for field, expected, label in bindings:
        actual = target.get(field, {}).get("digest_sha256")
        if actual != expected:
            issues.append(
                Issue(
                    f"{DECISION_CODE}-BINDING-MISMATCH",
                    f"START does not bind the exact {label} supplied",
                    f"target/{field}",
                )
            )

    return schema_report + report_of(issues)


def require_started(
    decision: Mapping[str, Any],
    plan: Mapping[str, Any],
    audit: Mapping[str, Any],
) -> None:
    """Raise unless this is a valid, exactly-bound `START` (not `REPLAN`)."""
    check_start_decision(decision, plan, audit).require(SpecGap)
    if decision["decision"] != "START":
        raise SpecGap(
            f"{DECISION_CODE}-NOT-STARTED the user decided '{decision['decision']}', not START"
        )


def require_single_start(state: Mapping[str, Any], decision_path: str) -> None:
    """There is exactly one approval path; a second START overwriting the first is refused.

    V3 has no PolicyApprovalReceipt, ActivationReceipt or runtime-authority snapshot
    (V3-D4), so "already started" is decided by the one pointer on the state.
    """
    existing = state.get("start_decision_ref")
    if existing and existing.get("path") != decision_path:
        raise SpecGap(
            f"{DECISION_CODE}-SECOND-APPROVAL run already bound START decision "
            f"{existing['path']}; a second approval path does not exist"
        )
