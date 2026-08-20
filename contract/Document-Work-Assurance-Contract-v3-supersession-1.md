# Document Work Assurance Contract v3 — supersession 1 (commit-bound review subject)

**Status: authored at the W2 implementation round (2026-07-23); UNSIGNED until the wave-2
gate.** This file is a versioned successor under the signed contract's own §13 rule —
*"Signed contracts are never amended in place; corrections create a versioned successor"* —
authorized by the user's adjudication of the wave-2 design
(`ResearchSystem/migration/document-work-assurance-v3/W2/W2-design.md`, adjudicated
2026-07-23). The signed [`Document-Work-Assurance-Contract-v3.md`](Document-Work-Assurance-Contract-v3.md)
stays byte-identical; nothing here rewrites it. This file carries exactly four statement
supersessions and nothing else. Where this file is silent, the signed contract governs
unchanged.

## 1. What is superseded, and why

The signed contract fixes the ReviewPackage layer in exactly four places (the wave-2
design §2, four-site count independently re-verified by its review). The package's only
load-bearing function was pinning the **uncommitted control plane** at review time; once
the controller commits the control plane before dispatching review, git content-addresses
every member byte and the review subject becomes **one evidence commit SHA**. The reviewer
re-derives everything from pinned revisions — the same shape as the construction-side
review contract §2, exercised in production by every checkpoint read of the v3
construction itself. Witnessed grounds (w1-r1): a hand-authored member enumeration
disagreed with the run directory (freeze-check-paths); the successor derives the
enumeration from the committed tree, so the authored-list defect class becomes
unrepresentable rather than guarded.

## 2. The four supersessions

Each row names the signed site exactly, quotes its signed text, and states the successor
text in full. The successor text governs newly opened runs; §3 below pins the version
boundary.

### S1 — §4 "Storage and candidate topology", the control-root diagram line

Signed text (line inside the E(C) diagram):

> `-> frozen ReviewPackage / ReviewResult`

Successor text:

> `-> evidence commit (control plane committed; subject = one SHA) / ReviewResult`

### S2 — §7 "Coverage and candidate invariants", invariant 9

Signed text:

> 9. ReviewPackage logically includes raw instruction/sources, plan, actual candidate
> artifacts, fulfillment, manifest, checks and coverage; membership uses exact revision +
> locator + digest and never byte-copies every source. The executor summary is
> supplemental only.

Successor text:

> 9. The review subject is one **evidence commit**: before dispatch the controller commits
> the run's control root — plan, fulfillment, manifest, one file per CheckResult, and
> coverage — so the commit content-addresses every member byte, and the raw instruction,
> sources and actual candidate artifacts are read at the exact revisions the WorkSpec and
> CandidateRecord pin. The member enumeration is **derived from the committed tree**,
> never hand-authored. The evidence commit's changed-path set must lie inside the run's
> control root (checked, not hoped). The executor summary is supplemental only.

### S3 — §7 "Coverage and candidate invariants", invariant 11

Signed text:

> 11. Repair regenerates manifest, fulfillment mapping, checks, coverage and package for C2.

Successor text:

> 11. Repair regenerates manifest, fulfillment mapping, checks and coverage for C2, and
> commits a **new evidence commit**; no round-1 subject may reuse the round-0 evidence
> commit.

### S4 — §8 "Product flow", step 7

Signed text:

> 7 controller freezes actual-subject ReviewPackage; reviewer runs one FULL

Successor text:

> 7 controller commits the control plane and verifies the evidence commit
> (`check_subject`); the dispatched review subject is that commit's SHA; reviewer runs one
> FULL, re-deriving from pinned revisions

## 3. Version boundary — explicit keying, no fallback

- A successor **ReviewResult declares its own version**: root `schema_version` const `"2"`
  (`schema/document-assurance-v3/review.v2.schema.json`), binding
  `subject = { evidence_commit, candidate_ref, base_revision, control_root, repair_round }`
  in place of `package_ref`. A result with no `schema_version` key is a v1 result and is
  validated against pinned v1 semantics; `"2"` selects v2; a present-but-null or any other
  value is a `SPEC_GAP`, fail closed — **no cross-version fallback in either direction**
  (the W1 keying pattern, `_ABSENT` sentinel included).
- Newly opened runs author v2 results. Closed runs and shadow rounds keep their frozen
  packages as **pinned v1 history**: no migration, no re-freeze, no retroactive script
  fixes; `review.schema.json` and the v1 checker functions stay frozen for reading that
  history (signed contract §13: a live run pins exact schema versions; later changes never
  mutate it).
- A state pointer carries the **BYTES digest** of the pointed-at file (the w1-r1
  pointer-digest-kind lesson, triaged `CORE_CANDIDATE`); the documented authoring path is
  the `assurance_state.pointer_to` helper, which computes the bytes digest itself.

## 4. What this supersession does not touch

- N2-A1's substance — a review requires actual subjects; summary-only substitution fails —
  is **re-satisfied by the successor's own mechanics, never amended**: subjects are read at
  pinned revisions from the repository, not from executor-supplied bytes.
- No other signed statement, enum, interface, invariant or flow step changes meaning. The
  §3 ownership row "frozen review-subject binding" continues to hold: the controller still
  binds the review subject — by commit instead of by package.
- Digest-strength disclosure (wave-2 design §9): v1 package members carried SHA-256
  digests; the successor rests member binding on git content addressing, whose object
  format in this repository is SHA-1. Acceptable under the signed contract §1's threat
  model (single writer, workflow protocol rather than OS guarantee) — a real strength
  change, stated rather than glossed.

## 5. Signature

User signature at the wave-2 gate means: these four supersessions and the §3 version
boundary are frozen for successor runs. The signature record (exact blob + candidate SHA +
date) lives in the W2 round record
(`ResearchSystem/migration/document-work-assurance-v3/W2/W2-record.md`), appended after
review — never inside this file.
