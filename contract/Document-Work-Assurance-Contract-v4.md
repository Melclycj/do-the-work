---
title: Document Work Assurance Contract v4
tags:
  - research-system
  - harness
  - contract
  - document-work
created: 2026-08-23
signature_owner: CONTRACT-V4-SIGNATURE.md (this instrument's v4 signature record)
---

# Document Work Assurance Contract v4

> [!warning] Signature semantics
> This contract becomes binding only when the user signs it. The signature is recorded, write-once
> and after review, in this instrument's own signature record — held with its construction record
> and not by a repository that runs against it — binding this file's exact Git blob; this
> file never carries its own approval status or digest (signed contracts are never amended in
> place; corrections create a versioned successor).

This file is the **versioned successor merging the signed v3 contract and its two signed
supersessions into one operative text**, under v3's own §13 rule. Which three texts those were,
the blob and signing date of each, the records that carry their signatures and the enumerated
wording deltas the merge was held to are this instrument's own construction history: reachable
in its repository and in no repository that runs against this contract, and therefore not
reproduced here. §14 states what the supersession means, which is the part a repository acts on.

Authored under the user-approved plan *Document Work Assurance Harness v3*. Plan §2 decisions
V3-D1–D10 are the locked design authority; a genuine conflict between this contract and the plan
is a `SPEC_GAP`, not a reinterpretation opportunity.

## 1. Product and bounded assurance statement

The product is a local, instruction-driven **Document Work Assurance Harness** that makes silent
omission, unsupported completion claims, wrong review subjects and unbounded repair loops visible
before a user accepts document changes.

The primary assurance statement is bounded:

> For one frozen instruction/source set and one exact candidate, every declared instruction unit is
> mapped to an obligation or an explicit `SPEC_GAP`; every obligation is accounted for against actual
> candidate locators and applicable evidence; one independent semantic challenge occurred; residual
> uncertainty was disclosed to the user.

V3 does not prove semantic truth or reviewer infallibility. Role separation is a workflow protocol,
not an OS security guarantee.

## 2. Scope (V3-D1)

- **IN:** one local Git repository and isolated candidate worktree; one execution writer, a
  distinguishable instruction/review auditor and the user; instruction-driven
  Markdown/JSON/YAML/plan/design/metadata work; exact frozen inputs; concrete change boundary;
  closed local deterministic checks; one FULL review, optional one repair, one VERIFY; one small
  resumable state; one final AssuranceSummary.
- **OUT:** source-code product implementation, coding orchestrators, executor plug-ins/adapters,
  tool discovery, model routing, sandbox/OS/network guarantees, spend/publication/experiments,
  dashboards, semantic-truth proof, multi-domain profile catalogues.

The executor is the ordinary instruction-following agent; the v3 core has no integration layer for
any named external orchestrator.

## 3. Interface ownership (plan §4)

| Logical object | Sole owner | Schema file (this node) |
|---|---|---|
| `DocumentWorkSpec` | the run's executor (its WorkSpec author) | [document-work-spec.schema.json](../schema/document-assurance-v3/document-work-spec.schema.json) |
| `DocumentAssuranceProfile` | profile publisher | [document-assurance-profile.schema.json](../schema/document-assurance-v3/document-assurance-profile.schema.json) |
| `InstructionCoverageAudit` | instruction auditor | [instruction-coverage-audit.schema.json](../schema/document-assurance-v3/instruction-coverage-audit.schema.json) |
| `ResolvedAssurancePlan` | resolver (generated) | [resolved-assurance-plan.schema.json](../schema/document-assurance-v3/resolved-assurance-plan.schema.json) |
| `AssuranceWorkState` | controller (generated) | [assurance-work-state.schema.json](../schema/document-assurance-v3/assurance-work-state.schema.json) |
| `UserDecision` | user | [user-decision.schema.json](../schema/document-assurance-v3/user-decision.schema.json) |
| shared vocabulary | this contract | [common.schema.json](../schema/document-assurance-v3/common.schema.json) |

Owned by later nodes (interface obligations fixed here, schemas at V3-N1/N2): `FulfillmentReport`
(executor), `CandidateArtifactManifest` (deterministic diff verifier — sole author),
`CheckResult` (deterministic local verifier), `LocalCheckSpec` (closed check union),
`ReviewResult` (independent reviewer), `AssuranceCandidate` / `AssuranceSummary` (controller,
generated), `HarnessIssue` (observer). `ObligationCoverage` is a disposable, byte-rebuildable join,
never a stored owner.

Ownership rule (V3-D5): a deterministic verifier owns its CheckResult; the diff verifier alone owns
the manifest; the reviewer owns ReviewResult; the controller may freeze subjects and bind refs but
may never restate evidence with stronger epistemic meaning; the executor cannot author check
outcomes or reviewer verdicts.

## 4. Storage and candidate topology (V3-D9, V3-D3)

```text
base B
  -> payload candidate C (declared document changes only; isolated branch/worktree)

control root E(C), outside C's payload identity
  -> WorkSpec / ResolvedAssurancePlan / AssuranceWorkState
  -> FulfillmentReport / manifest / checks / coverage
  -> evidence commit (control plane committed; subject = one SHA) / ReviewResult
  -> AssuranceCandidate -> UserDecision -> one final AssuranceSummary
```

- Payload and assurance evidence never share identity; evidence generation never changes the payload
  candidate under review. Repair creates payload `C2` from `C` and a new evidence set `E(C2)`.
- `write_scope`/`out` are an **acceptance boundary**: only a candidate whose observed change set
  conforms may be accepted. V3 never claims the boundary prevented bytes from being written, and no
  v3 record may describe audit-only behavior as hard enforcement, capability, grant or denial.
- `REJECT`/`REPLAN` preserves the candidate ref but never promotes it; `ACCEPT`/
  `ACCEPT_WITH_LIMITATIONS` may authorize one explicit, recorded local promotion step.
- Future Authorization/Enforcement planes may reference exact v3 objects and contribute external
  observations as evidence, but may not extend, mutate or reinterpret v3 objects or the change
  boundary as a permit, capability or grant. Composition occurs through an external envelope owned
  outside v3; v3 defines no schema for it.

## 5. Closed enums (single home: common.schema.json)

| Enum | Values |
|---|---|
| WorkState status | `RESOLVED · AUDITED · EXECUTING · EVIDENCED · REVIEWED · REPAIRING · AWAITING_FINAL · CLOSED · STOPPED_REPLAN` |
| Audit result | `COVERED · SPEC_GAP` (no repair loop) |
| Review verdict — FULL | `REVIEWED_NO_BLOCKER · CHANGES_REQUIRED · SPEC_GAP` (schema at N2) |
| Review verdict — VERIFY | `REVIEWED_NO_BLOCKER · SPEC_GAP · UNRESOLVED_BLOCKER` (schema at N2) |
| Decision phases | `START · REPAIR · FINAL · ISSUE_TRIAGE` |
| START decisions | `START · REPLAN` |
| REPAIR decisions | `APPLY_ACCEPTED_FINDINGS · NO_REPAIR` |
| FINAL decisions | `ACCEPT · ACCEPT_WITH_LIMITATIONS · REJECT · REPLAN` |
| ISSUE_TRIAGE decisions | `WORKFLOW_FIX · DOCUMENT_ASSURANCE_PROFILE_CANDIDATE · VERIFIER_FIX · CORE_CANDIDATE · DEFER · DISMISS` |
| LocalCheckSpec kinds | `file_exists · json_schema · markdown_link · locator_exists · git_diff_boundary · command_exit` (full schema at N1; unknown kind = `SPEC_GAP`) |
| Verification mode | `local_check · review_only` |

Every ReviewResult carries `residual_uncertainty` as data; nonblocking uncertainty is never a
control verdict. `REVIEWED_NO_BLOCKER` means only "no blocking discrepancy found within the frozen
subjects and review dimensions".

## 6. The instruction-obligation spine (V3-D7)

```text
instruction unit
-> obligation (or explicit non-normative context rationale)
-> executor fulfillment claim + implementation locator(s)
-> applicable verification evidence
-> per-obligation review disposition
```

Before START, a distinguishable instruction auditor performs exactly one `InstructionCoverageAudit`
over the raw frozen instruction and the proposed unit/obligation map. `SPEC_GAP` requires a new
WorkSpec revision and a new user START decision; the audit has no repair loop. The user is the trust
terminal for this preflight result. FULL review later rechecks instruction-to-obligation
completeness against the raw instruction.

## 7. Coverage and candidate invariants (plan §5.4 — binding)

1. InstructionCoverageAudit binds the exact WorkSpec/instruction and is `COVERED` before START.
2. Every obligation occurs exactly once in FulfillmentReport and ReviewResult.
3. `IMPLEMENTED` requires at least one resolvable locator into the exact payload candidate.
4. `NOT_IMPLEMENTED` is explicit and can never become unqualified success.
5. The manifest covers every actual add/modify/delete and is solely diff-verifier-authored.
6. Any out-of-boundary delta is `NONCONFORMANT`.
7. Every expected artifact exists in the manifest or is explicitly missing.
8. Every deterministic obligation binds an exact CheckResult; raw evidence remains authoritative.
9. The review subject is one **evidence commit**: before dispatch the controller commits
   the run's control root — plan, fulfillment, manifest, one file per CheckResult, and
   coverage — so the commit content-addresses every member byte, and the raw instruction,
   sources and actual candidate artifacts are read at the exact revisions the WorkSpec and
   CandidateRecord pin. The member enumeration is **derived from the committed tree**,
   never hand-authored. The evidence commit's changed-path set must lie inside the run's
   control root (checked, not hoped). The executor summary is supplemental only.
10. ReviewResult explicitly rechecks instruction completeness and covers every obligation.
11. Repair regenerates manifest, fulfillment mapping, checks and coverage for C2, and
    commits a **new evidence commit**; no round-1 subject may reuse the round-0 evidence
    commit.
12. AssuranceCandidate exists before FINAL; exactly one AssuranceSummary is generated after FINAL.
13. `REJECT`/`REPLAN` never promotes payload; accepted promotion is explicit and recorded.

Digests prevent "check candidate A, report candidate B"; they are generated bindings, not the
product centre and never substitutes for source inspection or instruction coverage.

## 8. Product flow (plan §6)

```text
1 freeze instruction, inputs and base B
2 author instruction-unit map, obligations, boundary and expected artifacts
3 resolve optional leaf DocumentAssuranceProfile refs -> disposable ResolvedAssurancePlan
4 one InstructionCoverageAudit -> user START or REPLAN
5 executor writes isolated payload candidate C + FulfillmentReport
6 diff verifier generates manifest; local verifiers run closed checks
7 controller commits the control plane and verifies the evidence commit
  (`check_subject`); the dispatched review subject is that commit's SHA; reviewer runs one
  FULL, re-deriving from pinned revisions
8 optional user REPAIR -> C2 -> regenerate evidence -> one VERIFY
9 controller generates AssuranceCandidate
10 user FINAL decision -> explicit promotion/no-promotion -> one AssuranceSummary
11 optional post-run HarnessIssue -> user ISSUE_TRIAGE
```

Normal review sequence (V3-D6): one FULL → optional user-approved bounded repair → rerun every
deterministic check → one targeted VERIFY → user FINAL decision or `STOPPED_REPLAN`. Repair
authorization binds the original candidate, accepted finding IDs and their minimum repair boundary.
VERIFY checks the accepted findings, the entire repair diff and permanent boundaries. A remaining
blocker or `SPEC_GAP` stops; no second fix or review-of-review exists.

WorkState status maps 1:1 onto this flow: `RESOLVED` (steps 1–3) → `AUDITED` (4) → `EXECUTING` (5)
→ `EVIDENCED` (6) → `REVIEWED` (7, and again after VERIFY) → `REPAIRING` (8, `repair_round` 0→1) →
`AWAITING_FINAL` (9) → `CLOSED` (10–11); `STOPPED_REPLAN` is reachable from any pre-CLOSED status by
a user REPLAN or an unrepaired blocker.

## 9. DocumentAssuranceProfile promotion rule (V3-D2)

A rule becomes a `DocumentAssuranceProfile` only after two distinct real work instances demonstrate
reuse, it has a stable owner/version cadence, and sharing removes real duplication or preserves an
invariant. Before that threshold the rule stays in WorkSpec/check configuration. `document_assurance_
profiles` is optional; absence means no profile, never an empty placeholder. A no-profile resolution
is a required positive case. Profiles contain no capability, enforcement level, authority, concrete
task path, stage order or one-off schema/rubric. Resolution accumulates checks/constraints, uses
stricter numeric limits, and fails closed naming owners on conflict. V3 may operate indefinitely
with zero published profiles.

## 10. Authorization model (V3-D4)

Exactly one typed `UserDecision` interface exists (phases/decisions in §5). A START decision is a
workflow gate, not proof that pre-start writes were impossible. V3 has no PolicyApprovalReceipt,
ActivationReceipt or runtime-authority snapshot. Priority order when concerns compete:

1. instruction/obligation coverage;
2. deterministic verification and bounded semantic assurance;
3. observed change-boundary conformance;
4. exact candidate/evidence binding and resumability.

## 11. Growth after the run (V3-D10)

A real harness defect/burden may create one immutable, evidence-linked `HarnessIssue`; it never
changes the active WorkSpec, plan, profiles, checks or verdict. Only a post-run user `ISSUE_TRIAGE`
decision routes it (§5). Triage follows observed evidence: workflow-local first, then profile only
after witnessed reuse, verifier/reviewer implementation if local, core only for ownership/invariant
defects shared across multiple profiles. V3 has no Retrospective state machine, dedup registry or
automatic maintenance stage.

## 12. Removed from the v3 default interface (plan §7)

Removed from the v3 default interface (never to be reintroduced without a user-approved plan
amendment): capabilities/enforcement floors, resource grants, generalized URI/intersection algebra,
approval/activation receipts, distributed event/CAS/idempotency protocol, generic receipt taxonomy,
multi-track review, generic gates/waivers, external-effect recovery, Retrospective/issue-registry
state machines.

## 13. Versioning, rollback and supersession (plan §11)

- A live run pins exact WorkSpec/profile/resolver/schema versions; later changes never mutate it.
- Signed contracts are never amended in place; corrections create a versioned successor.
- The v3 branch roots at accepted A3 closeout `7db177d`; abandoning v3 leaves v1/v2 history intact.
- Cutover (V3-N4, conditional) changes only the document-work entry/pointer; rollback restores the
  pointer and deletes no history.
- Hard enforcement, tools/security/compliance, observability dashboards and artifact UI are separate
  projects; v3 neither models their schemas nor claims their guarantees.

### 13.1 Review-subject version boundary (merged from supersession 1, adjudicated 2026-07-23)

- A successor **ReviewResult declares its own version**: root `schema_version` const `"2"`
  (`schema/document-assurance-v3/review.v2.schema.json`), binding
  `subject = { evidence_commit, candidate_ref, base_revision, control_root, repair_round }`
  in place of `package_ref`. A result with no `schema_version` key is a v1 result, and that
  class is empty: the user ruled on 2026-08-28 that no v1 ReviewResult instance exists
  anywhere. This clause therefore prescribes **no validation path** for such a result — one
  presented nonetheless is not validated and not accepted, fail closed; which mechanism
  raises the stop is the implementation's to choose, and this clause does not fix it. `"2"`
  selects v2; a present-but-null or any other value is a `SPEC_GAP`, fail closed — **no
  cross-version fallback in either direction** (the W1 keying pattern, `_ABSENT` sentinel
  included). Until 2026-08-28 this bullet required instead that a result with no
  `schema_version` key **be validated against pinned v1 semantics**. Round
  `V1-RESULT-RETIRE` removes that path on the strength of the same ruling — the requirement
  had no object left to act on. `HD-64` authorises the correction in place; it is the first
  authorisation in this family to override §13 for a statement of what this contract
  *requires* rather than a statement of fact, and it rules that no design round opens for it,
  a set-aside recorded there with its costs and expressly not a precedent. The reading that
  would have left this bullet untouched — taking *pinned v1 semantics* to mean the schema as
  it stands in the commits that hold v1 history — was put to the user and **declined**; it is
  not the interpretation going forward.
- Newly opened runs author v2 results. Closed runs and shadow rounds keep their frozen
  packages as **pinned v1 history**: no migration, no re-freeze, no retroactive script
  fixes; what reads that history is the commits that hold it, and this clause promises no
  working-tree artifact for that reading (§13 above: a live run pins exact schema versions;
  later changes never mutate it — the pin lives in the commit that made it). Until
  2026-08-28 this bullet promised instead that `review.schema.json` and the v1 checker
  functions stay frozen for that reading. The checker functions had already retired with the
  version-1 package leg in round `CORE-SET-CODE` (`56d1b17`) with nothing telling this
  clause, and that schema was this instrument's own rather than any caller's: it left the tree
  with the same round and is reachable in this repository's git history at blob
  `3617b74e9149e3c51ddfaf9c969a6be584972961`, in no working tree and in no repository that runs
  against this contract. The schema half's ground — that some v1 result still needs validating — was
  withdrawn by the user's ruling of 2026-08-28 that no v1 ReviewResult instance exists
  anywhere. `HD-63` authorises this correction in place and says in as many words that it
  overrides §13's prohibition, for one class only: a signed statement of fact that was true
  when signed and has since been made false elsewhere. A statement of what this contract
  *requires* still takes §13's versioned-successor route.
- Digest-strength disclosure (wave-2 design §9): v1 package members carried SHA-256 digests; the successor
  rests member binding on git content addressing, whose object format in this repository is
  SHA-1. Acceptable under §1's threat model (single writer, workflow protocol rather than
  OS guarantee) — a real strength change, stated rather than glossed.

### 13.2 State-pointer digest policy (merged from supersession 2, adjudicated 2026-07-29)

- A state pointer carries the **BYTES digest** of the pointed-at file **when, and only
  when, its field is one the executor may not author the current version of**:
  `work_spec_ref`, `start_decision_ref`, `repair_decision_ref`, `final_decision_ref` and
  `review_ref` (`assurance_state.DIGEST_PROTECTED_FIELDS`). Every other state pointer
  carries the path alone; `pointerRef` requires only `path`, so this needs no schema
  change. The documented authoring path is the `assurance_state.pointer_for` helper, which
  applies the field policy and delegates to `pointer_to` for the digest; `pointer_to`
  remains correct for what it does and is **no longer the authoring path for a newly opened
  run** — closed-run scripts (held in the caller's run directories) and the helper's own
  tests still call it directly, and nothing here asks them to change. **When a digest is
  present it is still of the pointed-at file's bytes and is still verified** — the w1-r1
  pointer-digest-kind lesson is unchanged, and a wrong digest on any field remains
  `POINTER-STALE`. What changed is the obligation to write one, never the meaning of one
  that is written.
- Version boundary: a state pointer is authored under this policy when it is written by
  `assurance_state.pointer_for`; one written by `pointer_to` or `pointer` directly is under
  the prior text where the two texts differ; for an unprotected field written as a bare
  `pointer(path)` they do not. The boundary is the authoring call, not a date, and the unit
  is the pointer — a single run may author some pointers each way, which is the shape to
  expect. Closed runs and shadow rounds keep the digests they were written with as **pinned
  history**: no migration, no re-write, no retroactive removal — a record edited to match a
  later rule stops being a record of what happened. Existing digests on closed runs remain
  verifiable exactly as before.
- Five bounded properties, stated rather than glossed: **no schema byte changes**
  (`pointerRef` already made `digest_sha256` optional; nothing in `schema/` is amended by
  this policy). **The `digestRef` side is untouched** — the plan's `work_spec_ref` binding
  and the review/summary/profile digest comparisons continue to require and check a digest;
  those refs require `[path, digest_sha256]` by schema and are outside this statement
  entirely; `instruction_ref` is **not** among them — it is a `frozenFileRef`, required as
  `[path, revision]`, and nothing requires or checks a digest on it; it was named here in
  error and is outside this statement for a different reason. **Detection strength**: the surviving
  digests detect an uninformed mis-write; they do **not** detect a consistent rewrite of
  file and digest together, and they never did — the limit is recorded, not narrowed.
  **Coverage of the narrowing is partial and named**: `assurance_state.pointer(path,
  digest)` still accepts a caller-supplied digest and is used directly by hand-written run
  scripts, so a run authored by copying an existing precedent will keep writing digests on
  unprotected fields; the obligation removed is on the documented authoring path. **Only
  one protected field has a live write path**: of the five, only `review_ref` is authored
  by `assurance/templates/run-v2/` (`run_bind_v2.py`); the other four are written by
  hand-authored run scripts, which this policy governs but no shipped template exercises —
  end-to-end demonstration covers one field, unit tests the rest.

## 14. Signature

User signature means: this contract's interfaces, enums, invariants, version boundaries and
default-interface removals are frozen as the operative text for v3-family construction, and
this file supersedes the v3 contract and its two supersessions as one operative document. The
signature record (exact contract blob + date) lives with this instrument's own construction
record and not with a repository that runs against it, written after
review — never inside this file.
