"""Resident enumeration assertions — the one binding check worth keeping per round.

SIMP-A2/A3 (2026-08-05). Run-local checkers were written fresh each round and discarded
with it, so the review surface they created accumulated nothing: three consecutive rounds
returned findings about checker assertion strength, and every one of those findings died
with its run. The checks that survive that deletion need somewhere to live, and this is it
— the layer that has actually been paying off, alongside `check_record`'s empty-locator
refusal, `check_spec`'s field-length refusal and `build_run`'s fake-BASE refusal.

**Set equality, both directions, and never vacuous.** The first migration target is the
one check that caught something real: a set a document *declares* must equal the set the
repository *derives*. Missing and extra are reported separately because they are different
defects — a missing member is work the document forgot, an extra one is work it invented —
and two empty sets are reported as a failure rather than a pass, because an extractor that
silently stopped matching produces exactly that shape and would otherwise read as clean.

**What deliberately stays run-local: the extraction.** Every document shapes its table
differently (a status column here, a bare list there), so a generalized extractor would be
a parameter soup with one caller per shape. The reusable half is the comparison and its
refusal rules; the run supplies two sets. That split is also why nothing here is written
before it has a caller — a resident helper with no consumer is the shape riders `RA` and
`PD` already carry twice.
"""
from __future__ import annotations

from typing import Iterable

from rsclib.document_harness import Issue, Report, report_of

CODE = "V3-ENUM"


def set_equality(
    found: Iterable[str],
    expected: Iterable[str],
    *,
    subject: str,
    found_label: str = "declared",
    expected_label: str = "derived",
) -> Report:
    """`found` must equal `expected`, both directions, and neither may be empty.

    `subject` names what is being compared, so a caller with several enumerations gets
    distinguishable issues. Members are sorted in the message: the comparison is over sets,
    and a stable rendering is what makes the output diffable across runs.
    """
    found_set, expected_set = set(found), set(expected)
    issues: list[Issue] = []

    if not found_set and not expected_set:
        issues.append(
            Issue(
                f"{CODE}-VACUOUS",
                f"{subject}: both the {found_label} and the {expected_label} set are empty, "
                "so the comparison asserts nothing; an extractor that stopped matching "
                "produces this exact shape",
                subject,
            )
        )
        return report_of(issues)

    missing = sorted(expected_set - found_set)
    extra = sorted(found_set - expected_set)
    if missing:
        issues.append(
            Issue(
                f"{CODE}-MISSING",
                f"{subject}: {len(missing)} member(s) in the {expected_label} set are absent "
                f"from the {found_label} set: {', '.join(missing)}",
                subject,
            )
        )
    if extra:
        issues.append(
            Issue(
                f"{CODE}-EXTRA",
                f"{subject}: {len(extra)} member(s) in the {found_label} set are not in the "
                f"{expected_label} set: {', '.join(extra)}",
                subject,
            )
        )
    return report_of(issues)
