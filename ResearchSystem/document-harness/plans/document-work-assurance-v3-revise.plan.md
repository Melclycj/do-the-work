---
title: V3 REVISE — unblock the review deadlock, teach SPEC_GAP, re-run the shadow evidence
slug: document-work-assurance-v3-revise
created: 2026-07-21
status: authored, awaiting execution
plan_role: durable handoff for a fresh session
---

# V3 REVISE — the deadlock fix and shadow round 2

> [!important] Read this first, then `ResearchSystem/migration/document-work-assurance-v3/N3/N3-record.md`.
> This file is **out-of-node** (`.goals/` is excluded from the N1–N3 allowlists, plan §9) and was
> written at the user's explicit request for session continuity. It is a plan, not a node
> artifact, and it carries no authorization of its own.

## 0. Where the work actually stands

Repo `D:\Thesis-stage-control-refactor`, branch `document-work-assurance-v3`.
Governing plan: `.goals/plans/document-work-assurance-harness-v3.plan.md` (approved bytes,
immutable, blob `8ad404b1…`). Contract: `ResearchSystem/contract/Document-Work-Assurance-Contract-v3.md`
(signed blob `b2dbdf75…`). **Neither may be modified.**

| Node | State |
|---|---|
| V3-N0 | closed, user-signed |
| V3-N1 | closed, user-signed (`802e16a`) |
| V3-N2 | closed, user-signed (`23ac473`), closeout `655bae5`. Budget fully spent |
| **V3-N3** | shadow runs **executed and committed** (`8e863c5` → `00c78fd` → `00963e4`). **Adoption decision NOT taken** |
| V3-N4 | not started; entry condition is `ADOPT_DOCUMENT_V3` at N3 |

**The user has indicated `REVISE_V3`.** The formal adoption adjudication was being taken
separately; this plan assumes REVISE and must be re-checked against the actual ruling before
step 1.

Key commits to know:
- `8efe3e9` `V3-N1-SCHEMA-PIN-AMENDMENT-v1` — **the precedent for an out-of-node amendment**
- `655bae5` — N2 closeout (this plan's base for the amendment)
- `00963e4` — the N3 orchestration errata (read it; it corrects two earlier mis-reports)

## 1. The problem being fixed

A reviewer who finds **"the deliverable has no blocker, but the obligation map was incomplete"**
has no honest verdict available:

| verdict | why it is wrong here |
|---|---|
| `REVIEWED_NO_BLOCKER` | overreaches — the reviewed scope was narrower than the instruction requires |
| `CHANGES_REQUIRED` | wrong object — the candidate is fine; the WorkSpec's map is what is deficient |
| `SPEC_GAP` | discards a real review entirely and forces a full re-run even when the artifact is sound |

`check_review_result` currently refuses the first outright
(`V3-REVIEW-INCOMPLETE-CONTRADICTS-VERDICT`), which is the deadlock: it rejects the only
verdict that could be made honest, and names no replacement.

**Both shadow runs hit this, with different reviewers on different subjects.** Hand-authored
obligation maps drop normative units as the normal case, so this recurs on every run.

### 1.1 The finding that unlocks it

**Contract §5 already defines the verdict as scope-relative:** *"`REVIEWED_NO_BLOCKER` means
only 'no blocking discrepancy found **within the frozen subjects and review dimensions**'"*.

An incomplete map means the dimensions were narrower — the verdict remains true **as defined**,
provided the narrowness is disclosed. The V3-N2 guard asserted that an unmapped normative unit
*is* a blocking discrepancy. **The contract does not say that. The guard over-read it.**

This is why no fourth verdict is needed, and why V3-D6 ("nonblocking uncertainty is not a
fourth control verdict; the user may choose `ACCEPT_WITH_LIMITATIONS`") is not violated — the
existing `residual_uncertainty` → `ACCEPT_WITH_LIMITATIONS` path is exactly the route for this.

## 2. The fix — four parts

1. **Stop refusing the combination.** `INCOMPLETE` + `REVIEWED_NO_BLOCKER` becomes legal.
2. **Force disclosure instead.** When `instruction_completeness.result == INCOMPLETE`:
   `unmapped_unit_ids` must be present and non-empty, a finding naming the gap is required, and
   a `residual_uncertainty` entry is required. Silence stops being an option.
3. **The user sees it at FINAL** and may choose `ACCEPT_WITH_LIMITATIONS`.
4. **Teach `SPEC_GAP`.** `REVIEW.md` must state the criterion for when an incomplete map means
   *stop* rather than *disclose and continue*, with one worked example of each. This is the item
   the user named explicitly: **the agent must learn to write `SPEC_GAP`.**

### 2.1 Validated against both witnessed cases

- **run-a1** — map omitted the instruction's §4 (31 locked decisions); reviewer verified
  conformance by hand and it held → `REVIEWED_NO_BLOCKER` + gap finding + residual. The user
  decides. ✔ sensible
- **run-p3** — map dropped one of five acceptance assertions, *and* a real blocker existed (the
  count defect) → `CHANGES_REQUIRED` anyway, plus the gap finding. ✔ sensible

## 3. Landing sites and boundary

**All three files were authored at V3-N2 and are NOT covered by the N0 signature.** No signed
byte is touched. Each change is an out-of-node amendment on the `8efe3e9` pattern.

| File | Change |
|---|---|
| `ResearchSystem/schema/document-assurance-v3/review.schema.json` | `if/then`: `INCOMPLETE` ⇒ require `unmapped_unit_ids` (non-empty) and `findings` |
| `ResearchSystem/tooling/rsclib/document_harness/review.py` | replace `V3-REVIEW-INCOMPLETE-CONTRADICTS-VERDICT` with a disclosure requirement; keep a guard that fires when disclosure is absent |
| `ResearchSystem/document-harness/REVIEW.md` | the `SPEC_GAP` criterion + one worked example each way |

**Explicitly OUT of this round:**
`ResearchSystem/schema/document-assurance-v3/document-work-spec.schema.json` — the
`review_only` incentive-gradient fix. It is **N0-signed**, so it needs a versioned successor
(plan §11), not an amendment. The user has ruled it a separate special case (特例). Its
analysis lives in `ResearchSystem/migration/document-work-assurance-v3/v3-review-note-obligation-authoring.md`
(untracked) and the witnessed evidence is in N3 record §4.1: **12/19 obligations were
`review_only`, ≥4 were mechanisable, and the single real defect found sat inside one of them.**

## 4. Steps

1. **Re-check the adoption ruling.** If it is not `REVISE_V3`, stop and re-plan.
2. **Amend the three files**, one out-of-node commit, kind named in the title.
3. **Mutation-verify**: neuter the disclosure requirement → the pinning test must go red →
   restore from a byte-checked scratchpad copy. **Never `git checkout --`** (this repo has an
   incident).
4. **Add tests** under `ResearchSystem/tooling/tests/document_harness_review/` covering: the
   combination is now legal *with* disclosure; refused *without* it; `SPEC_GAP` still available.
5. **Shadow round 2** under a **new root** — `ResearchSystem/generated/document-assurance/shadow/round-2/**`.
   **Round 1 is frozen in place and must not be modified or deleted** (V3-D9: evidence sets are
   never mutated; round 1 is the before-side of the comparison and the N3 record cites it).
   The mechanical part is scripted and takes minutes — reuse:
   `shadow/run-a1/build_run.py`, `shadow/run-a1/run_evidence.py`, `shadow/run-p3/run_shadow.py`,
   `shadow/freeze_packages.py`, `shadow/measure.py`.
6. **Re-run the two FULL reviews** (the only real cost — ~35 min each by the reviewers' own
   account). Expect both to look *different*: a correctly-routed incomplete map may now stop
   with `SPEC_GAP`, which N3-A1 explicitly allows (*"complete **or truthfully stop**"*).
7. **Before/after comparison** into the N3 record. **§8 is append-only** — append, never rewrite.
8. **Re-take the adoption decision.**

## 5. Traps — each of these was actually hit

- **`.goals/LEDGER.md` is excluded at N1–N3** (permitted at N0 and N4). A hook will ask for it
  every session; the answer is the node record. Writing it mid-node is an out-of-node act.
- **`rsclib/document_harness/__init__.py` is on no node's allowlist after N1.** The package root
  froze; `review.py` carries its own schema registry for exactly this reason.
- **Signed bytes are untouchable** — approved plan, Contract v3, the seven N0 schemas including
  `common.schema.json`. When the cleanest fix needs one, take the in-boundary fix and record
  why, or stop with `SPEC_GAP`.
- **Measure last.** Any figure is invalidated by a later change to what it measures.
- **Do not guess locators.** Four guessed anchors failed across the two shadow runs. Read the
  document.
- **Do not report an un-invoked mechanism as a useless one.** This was the errata at `00963e4`:
  the freeze/binding layer was reported as unused surface when the orchestrator had simply never
  called it. Switched on, it refused a tampered package and caught two real defects immediately.

## 6. Open items the user still owes a ruling on

| # | Item |
|---|---|
| 1 | The adoption decision itself (`ADOPT` / `REVISE` / `ROLLBACK`) — being taken separately |
| 2 | Two review-side notes at the migration root are **uncommitted**: `v3-review-note-obligation-authoring.md` and `v3-review-handoff-2026-07-21.md`. Committing them is the execution side's act, by convention, but the user routes |
| 3 | **N3-R3** — a real defect in committed project data: `ResearchSystem/inventory/P3-inventory.md` claims ExperimentLab holds 110 in-scope Markdown files; the base commit holds **51**. True total 161, not 220. The `54+39+17+110=220 ✔` line is that document's only evidence for its "100% accounted" acceptance property. Outside every v3 node's allowlist |
| 4 | **N2-R2** — `ResearchSystem/document-harness/README.md` still says "V3-N1 is not yet authorized and no runtime exists yet" |
| 5 | **N2-R5** — two test files exceed the 800-line rule (2115 and 1344); all implementation modules are inside it. The repo's own tripwire says *propose, never auto-split* |
| 6 | **N2-R7** — the VERIFY report that closed V3-N2 is not in the repository; only its verdict reached the record |
| 7 | `.goals/LEDGER.md` has four stale lines (documented in `v3-review-handoff-2026-07-21.md` §1). Fix at a node boundary, not mid-node |

## 7. Shadow-run facts a fresh session must not re-derive wrong

| Run | base | candidate | instruction |
|---|---|---|---|
| run-a1 | `b626cb508bf2892cdc2bbb80d2278303e8cacc36` | `5ca6cc1cbf4ba0694130704d7aaf0e5c16fca71c` | `ResearchSystem/handoffs/P4-reopen-2026-07-17.md` @ candidate |
| run-p3 | `90deba7c4207b307f3561b2a5f5c165852d4f850` | `244e057e00541f4261c034538343f8a04e7f7cb8` | `.goals/plans/research-system-agent-integration.plan.md` @ base |

Both candidates are **real historical commits read through `git show`** — no disposable copies,
nothing mutable, N3-A8 held in the strongest available form.

Round-1 measured burden: protected work 89,739 B · authored control 14,811 (**17%**) · generated
control 69,215 (77%) · all control 84,026 (**94%**). Plan §10's criterion is *effort*, so 17% is
the figure that decides it and it does not dominate. 6/6 check kinds exercised; zero profiles;
zero repair rounds; cold resume `exit 0` on both.

## 8. Acceptance for this revise round

- [ ] The three files amended; no signed byte touched; changed paths classified individually
- [ ] Disclosure requirement mutation-verified (neuter → red → restore from byte-checked copy)
- [ ] `REVIEW.md` teaches the `SPEC_GAP` criterion with a worked example each way
- [ ] Round 1 evidence untouched; round 2 under its own root
- [ ] Both round-2 reviews executed in independent contexts
- [ ] Before/after comparison appended to the N3 record §8
- [ ] Every deterministic suite re-run **immediately before** the figures are written
- [ ] Adoption decision re-taken by the user
