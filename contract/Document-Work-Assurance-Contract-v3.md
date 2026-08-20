---
title: Document Work Assurance Contract v3
tags:
  - research-system
  - harness
  - contract
  - document-work
status: candidate-awaiting-user-signature
created: 2026-07-20
document_role: signed-contract-candidate
signature_owner: V3-N0 administrative record
---

# Document Work Assurance Contract v3

> [!warning] Signature semantics
> This contract becomes binding only when the user signs it at the V3-N0 stop gate. The signature is
> recorded append-only in the [V3-N0 administrative record](../migration/document-work-assurance-v3/N0/N0-record.md),
> binding this file's exact Git blob — this file never carries its own approval status or digest
> (signed contracts are never amended in place; corrections create a versioned successor).

Authored under the user-approved plan
[[document-work-assurance-harness-v3.plan|Document Work Assurance Harness v3]] (plan SHA-256
`9B08CD0038FA0C36E76674B7CE386129D9797EFFE5CEC7FABBF69699811F171F`). Plan §2 decisions V3-D1–D10 are
the locked design authority; a genuine conflict between this contract and the plan is a `SPEC_GAP`,
not a reinterpretation opportunity.

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
| `DocumentWorkSpec` | stage author / planning agent | [document-work-spec.schema.json](../schema/document-assurance-v3/document-work-spec.schema.json) |
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
  -> frozen ReviewPackage / ReviewResult
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
| Review verdict — VERIFY | `REVIEWED_NO_BLOCKER · SPEC_GAP` (schema at N2) |
| Decision phases | `START · REPAIR · FINAL · ISSUE_TRIAGE` |
| START decisions | `START · REPLAN` |
| REPAIR decisions | `APPLY_ACCEPTED_FINDINGS · NO_REPAIR` |
| FINAL decisions | `ACCEPT · ACCEPT_WITH_LIMITATIONS · REJECT · REPLAN` |
| ISSUE_TRIAGE decisions | `WORKFLOW_FIX · DOCUMENT_ASSURANCE_PROFILE_CANDIDATE · VERIFIER_FIX · CORE_CANDIDATE · DEFER · DISMISS` |
| LocalCheckSpec kinds | `file_exists · json_schema · markdown_link · locator_exists · git_diff_boundary · command_exit` (full schema at N1; unknown kind = `SPEC_GAP`) |
| Verification mode | `local_check · review_only · local_check_and_review` |

Every ReviewResult carries `residual_uncertainty` as data; nonblocking uncertainty is never a fourth
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
9. ReviewPackage logically includes raw instruction/sources, plan, actual candidate artifacts,
   fulfillment, manifest, checks and coverage; membership uses exact revision + locator + digest and
   never byte-copies every source. The executor summary is supplemental only.
10. ReviewResult explicitly rechecks instruction completeness and covers every obligation.
11. Repair regenerates manifest, fulfillment mapping, checks, coverage and package for C2.
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
7 controller freezes actual-subject ReviewPackage; reviewer runs one FULL
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

## 12. Dependency and historical map (plan §7)

Signed v1/v2 contracts, schemas and history are immutable. All old directories default to
**historical-only**; referencing any non-nominated old component from v3 is a `SPEC_GAP` until the
dependency map is amended. A4 (`f91a7c4`, closeout `de39b3d`) is accepted v2 history, labelled
**historical-only-for-v3**: reachable source material, never a physical base or default dependency.

The only nominated reuse candidates, with decisions and exact tests, are recorded in the
[N0 administrative record §4](../migration/document-work-assurance-v3/N0/N0-record.md):
canonicalization/content binding; closed JSON-schema validation; Git path/diff observation; frozen
review-subject binding; one-repair/VERIFY limit.

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

## 14. Signature

User signature at the V3-N0 gate means: this contract's interfaces, enums, invariants and
dependency map are frozen for v3 construction, and V3-N1 may be authorized. The signature record
(exact contract blob + candidate SHA + date) lives in the N0 administrative record, appended after
review — never inside this file.
