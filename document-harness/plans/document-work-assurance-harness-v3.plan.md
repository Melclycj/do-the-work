---
title: Document Work Assurance Harness v3 Execution Plan
aliases:
  - Document Assurance Harness Plan
tags:
  - research-system
  - harness
  - planning
  - document-work
status: candidate-plan
created: 2026-07-19
document_role: execution-plan
approval_status_owner: V3-N0 administrative record
---

# Plan: Document Work Assurance Harness v3

> [!warning] Candidate only
> This file authorizes no implementation, further v2 execution, A5, P4 work or pointer change. User approval
> binds the exact Git blob/candidate containing this plan and is recorded append-only at V3-N0; this
> plan never writes a digest or approval status into its own approved bytes.

## 0. Exact transition state

- **plan slug:** `document-work-assurance-harness-v3`
- **plan state:** `CANDIDATE_AWAITING_USER_APPROVAL`
- **planning worktree HEAD:** `de39b3d4bbe61ed09175d56a074f412f6031b94c`
- **v2 fact:** A4 closed with VERIFY `PASS`; its accepted payload tip is
  `f91a7c45fe6d6a920f03ac0e33b7baed7d034d58` and its administrative closeout is `de39b3d...`.
  A5--A7 and production cutover never started.
- **accepted v3 implementation base:** after plan approval, branch from accepted A3 closeout
  `7db177de9fd3c81e872dccd76cbbdfaba8925e02`, then apply the exact approved plan bytes. Although A4
  is accepted v2 history, v3 deliberately does not import its generalized review/growth layer; the
  A4 commits remain reachable source material but are not the physical base or a default dependency.
- **v1 historical implementation:** `c64b9c5f921238eb307f67227b5082b54ad45420`.
- **signed v2 interface boundary:** `2b68859d34cc7766df70f664860315fa64e19cfb`.
- **before approval, permitted action:** read-only review of this plan only.
- **after approval, permitted action:** V3-N0 only. Each later node has its own stop gate.

This candidate does not modify [[general-harness-v2-architecture-revision.plan|the v2 plan]],
the signed v2 contract (its file was deleted 2026-08-15 by `HD-39`, so the wikilink that stood
here is gone rather than rewritten — a wikilink resolves by stem and has no inline-code
exemption, so quoting the dead one in any form would re-break the scan), `.goals/LEDGER.md`,
A4 code or any business content.

## 1. Goal shift

V2 attempted a domain-neutral substrate for coding, documents, research, review and privileged
external action. V3 deliberately stops pursuing that product.

The v3 product is:

> A local, instruction-driven Document Work Assurance Harness that makes silent omission,
> unsupported completion claims, wrong review subjects and unbounded repair loops visible before a
> user accepts document changes.

The primary assurance statement is bounded:

> For one frozen instruction/source set and one exact candidate, every declared instruction unit is
> mapped to an obligation or an explicit `SPEC_GAP`; every obligation is accounted for against actual
> candidate locators and applicable evidence; one independent semantic challenge occurred; residual
> uncertainty was disclosed to the user.

V3 does not prove semantic truth or reviewer infallibility.

## 2. Locked design decisions

These decisions were accepted by the user on 2026-07-19. An implementation node may not reinterpret
them; a genuine conflict returns `SPEC_GAP` and stops.

### V3-D1 -- document work only

Consumer stages write Markdown, JSON, YAML, plans, design notes, metadata or coordinated multi-file
document sets. Product-stage source-code implementation, coding orchestrators, network, publication,
spend, experiment execution and irreversible external effects are OUT. Harness implementation code
may be written to implement the product.

The executor is the ordinary instruction-following agent. The v3 core has no integration or adapter
layer for GSD, UI/Quality or other external executors. Appendix A records a separately authorized,
optional Claude Code guard adapter; it is not a core dependency, executor integration or adoption
requirement.

### V3-D2 -- DocumentAssuranceProfile is optional, small and evidence-promoted

A `DocumentAssuranceProfile` owns one reusable assurance rule family with one owner and one reason
to change. It is not a Coding, Marketing, Document or Research mega-template.

- task paths, exact instruction/schema/rubric refs, outputs and stage order belong to the
  `DocumentWorkSpec` or exact inputs;
- task-local shared data remains workflow config, not a `DocumentAssuranceProfile`;
- a non-authoritative bundle may expand to exact leaf `DocumentAssuranceProfile` versions but cannot
  override them;
- `document_assurance_profiles` is optional; absence means no profile, never an empty placeholder;
- a rule becomes a `DocumentAssuranceProfile` only after two distinct real work instances demonstrate
  reuse, it has a stable owner/version cadence and sharing removes real duplication or preserves an
  invariant.

Before that threshold, the rule remains in the WorkSpec/check configuration. V3 may begin with zero
published `DocumentAssuranceProfile` objects.

### V3-D3 -- scope is acceptance boundary, not hard enforcement

Concrete `write_scope` and `out` remain necessary because a candidate may satisfy its instruction
while also changing unrelated files. Their meaning is:

> only a candidate whose observed change set conforms to this boundary may be accepted.

V3 does not claim the boundary prevented bytes from being written. Core schemas and reports do not
describe audit-only behavior as `hard enforcement`, `capability granted`, `access denied` or an
execution authority. `DocumentAssuranceProfile` objects may contribute reusable change constraints;
stages supply concrete paths. A future sandbox/tool gateway is a separate platform integration.

Future Authorization and Enforcement planes may reference exact v3 objects and contribute external
observations as evidence. They may not extend, mutate or reinterpret `DocumentAssuranceProfile`,
`ResolvedAssurancePlan`, `AssuranceWorkState`, `UserDecision` or the change boundary as a permit,
capability or grant. Composition occurs through an external envelope owned outside v3; v3 defines no
schema for that envelope.

All payload writing occurs on an isolated Git candidate branch/worktree rooted at an exact base.
`REJECT` or `REPLAN` preserves the candidate ref but never promotes it; the canonical branch remains
unchanged. `ACCEPT` or `ACCEPT_WITH_LIMITATIONS` may authorize an explicit local promotion step. This
is candidate isolation and disposition, not a general recovery/side-effect framework.

### V3-D4 -- authorization is lightweight workflow metadata

There is exactly one typed `UserDecision` interface with closed phases:

| Phase | Allowed decisions | Exact target |
|---|---|---|
| `START` | `START`, `REPLAN` | ResolvedAssurancePlan + InstructionCoverageAudit |
| `REPAIR` | `APPLY_ACCEPTED_FINDINGS`, `NO_REPAIR` | candidate + accepted finding IDs + repair boundary |
| `FINAL` | `ACCEPT`, `ACCEPT_WITH_LIMITATIONS`, `REJECT`, `REPLAN` | AssuranceCandidate |
| `ISSUE_TRIAGE` | `WORKFLOW_FIX`, `DOCUMENT_ASSURANCE_PROFILE_CANDIDATE`, `VERIFIER_FIX`, `CORE_CANDIDATE`, `DEFER`, `DISMISS` | HarnessIssue |

A START decision is a workflow gate, not proof that pre-start writes were impossible. V3 has no
PolicyApprovalReceipt, ActivationReceipt or runtime-authority snapshot.

Priority order:

1. instruction/obligation coverage;
2. deterministic verification and bounded semantic assurance;
3. observed change-boundary conformance;
4. exact candidate/evidence binding and resumability.

### V3-D5 -- evidence records do not manufacture truth

A deterministic verifier owns its CheckResult. The diff verifier alone owns the
CandidateArtifactManifest. A reviewer owns ReviewResult. The controller may freeze subjects and bind
refs into an AssuranceCandidate/Summary, but may not restate evidence with stronger epistemic
meaning. The executor cannot author check outcomes or reviewer verdicts.

Digests prevent “check candidate A, report candidate B”; they are generated bindings, not the product
centre and not substitutes for source inspection or instruction coverage.

### V3-D6 -- semantic review is bounded and non-recursive

Closed review control verdicts are:

- FULL: `REVIEWED_NO_BLOCKER | CHANGES_REQUIRED | SPEC_GAP`;
- VERIFY: `REVIEWED_NO_BLOCKER | SPEC_GAP`.

Every result carries `residual_uncertainty` as data; nonblocking uncertainty is not a fourth control
verdict. The user may choose `ACCEPT_WITH_LIMITATIONS`.

Normal sequence:

```text
one FULL
-> optional user-approved bounded repair
-> rerun every deterministic check
-> one targeted VERIFY
-> user FINAL decision or STOPPED_REPLAN
```

Repair authorization binds the original candidate, accepted finding IDs and their minimum repair
boundary. Repair produces a new payload candidate, new manifest, refreshed fulfillment locators,
new checks and new coverage. VERIFY checks the accepted findings, the entire repair diff and permanent
boundaries. Remaining blocker/`SPEC_GAP` stops; no second fix or review-of-review exists.

`REVIEWED_NO_BLOCKER` means only “no blocking discrepancy found within the frozen subjects and
review dimensions”.

### V3-D7 -- instruction obligations are the spine

The WorkSpec contains stable, locatable instruction units and obligations:

```text
instruction unit
-> obligation (or explicit non-normative context rationale)
-> executor fulfillment claim + implementation locator(s)
-> applicable verification evidence
-> per-obligation review disposition
```

Before START, a distinguishable instruction auditor performs exactly one
`InstructionCoverageAudit` over the raw frozen instruction and proposed unit/obligation map. Its
closed result is `COVERED | SPEC_GAP`; it has no repair loop. `SPEC_GAP` requires a new WorkSpec
revision and new user START decision. The user is the trust terminal for this preflight result.

FULL review later rechecks instruction-to-obligation completeness against the raw instruction. V3
does not claim an AI has mathematically proved that every semantic implication was enumerated.

### V3-D8 -- one small live state

One controller-owned `AssuranceWorkState` records current status and exact pointers. V3's
single-writer local scope does not use a content-addressed event chain, CAS, idempotency protocol or
dangling-event recovery. An append-only diagnostic log may exist but owns no current truth.

### V3-D9 -- payload and assurance evidence never share identity

The storage/commit topology is fixed:

```text
base B
  -> payload candidate C (declared document changes only)

control root E(C), outside C's payload identity
  -> WorkSpec / ResolvedAssurancePlan / AssuranceWorkState
  -> FulfillmentReport / manifest / checks / coverage
  -> frozen ReviewPackage / ReviewResult
  -> AssuranceCandidate
  -> UserDecision
  -> one final AssuranceSummary
```

ReviewPackage membership uses exact revision + locator + digest; it does not copy every source byte.
Repair creates payload `C2` from `C` and a new evidence set `E(C2)`. Evidence generation never
changes the payload candidate being reviewed.

### V3-D10 -- growth happens after the run

A real harness defect/burden may create one immutable, evidence-linked `HarnessIssue`; it does not
change the active WorkSpec, plan, `DocumentAssuranceProfile`, checks or verdict. After terminal
disposition, a user `ISSUE_TRIAGE` decision routes it to workflow config,
`DocumentAssuranceProfile` candidate, verifier fix, core candidate,
defer or dismiss. V3 has no Retrospective state machine, dedup registry or automatic maintenance
stage.

## 3. Product boundary

### IN

- one local Git repository and isolated candidate worktree;
- one execution writer, a distinguishable instruction/review auditor and the user;
- instruction-driven Markdown/JSON/YAML/design/plan/metadata work;
- exact input/ground-truth revisions;
- expected artifacts and concrete change boundary;
- closed local deterministic checks;
- one FULL, optional one repair and one VERIFY;
- small resumable `AssuranceWorkState`, actual-artifact visibility and final AssuranceSummary.

Role separation is a workflow protocol in v3, not an OS security guarantee.

### OUT

- coding/task-decomposition orchestrators and executor plug-ins;
- tool discovery, model routing, memory or autonomous planning platforms;
- sandbox, identity, secrets, DLP, network or OS enforcement;
- spend, publication, experiments or irreversible external actions;
- dashboards/artifact-viewer UI;
- proof of semantic truth;
- general multi-domain profile catalogues;
- production P4 while v3 is built;
- in-place mutation or deletion of signed/historical v1/v2 assets.

## 4. Target logical owners

Logical interfaces do not imply one standalone file each. Candidate control data may be stored as
owner-partitioned immutable sections under one run root; users author only WorkSpec decisions and
their decisions, not generated metadata.

| Logical object | Sole owner | Responsibility |
|---|---|---|
| `DocumentWorkSpec` | stage author/planning agent | raw instruction/input refs; instruction-unit map; objective; optional `DocumentAssuranceProfile` refs; concrete boundary; expected artifacts; obligations and check requests |
| `DocumentAssuranceProfile` | profile publisher | one witnessed reusable rule family, declared parameters, change constraints and required checks |
| `InstructionCoverageAudit` | instruction auditor | one pre-start judgment of raw-instruction -> instruction-unit -> obligation completeness |
| `ResolvedAssurancePlan` | resolver, generated | WorkSpec ref/digest; exact `DocumentAssuranceProfile` refs; only resolved deltas/conflicts; effective boundary/check order; repair cap |
| `AssuranceWorkState` | controller, generated | current assurance status and pointers only |
| `FulfillmentReport` | executor | one implemented/not-implemented claim and exact candidate locator(s) per obligation |
| `CandidateArtifactManifest` | deterministic diff verifier | actual add/modify/delete set, candidate identity and observed boundary delta |
| `CheckResult` | deterministic local verifier | exact request/subject/result/raw evidence ref |
| `ReviewResult` | independent reviewer | package-bound instruction-coverage judgment, per-obligation disposition, findings and residual uncertainty |
| `AssuranceCandidate` | controller, generated | pre-decision binding of candidate, coverage, checks and review without a user outcome |
| `UserDecision` | user | START, REPAIR, FINAL or ISSUE_TRIAGE decision bound to an exact target |
| `AssuranceSummary` | controller, generated after FINAL | terminal binding of AssuranceCandidate, UserDecision, promotion/disposition and limitations |
| `HarnessIssue` | observer | optional immutable post-run defect/burden observation and evidence ref |

`ObligationCoverage` is a disposable, byte-rebuildable join:

```text
WorkSpec.obligation_id
+ FulfillmentReport.implementation_locators
+ CheckResult.evidence_refs
+ ReviewResult.per_obligation_disposition
-> coverage row
```

## 5. Core interfaces and invariants

### 5.1 WorkSpec maximum authored surface

```yaml
work_id: stable ID
objective: bounded outcome
instruction_ref: exact ref + revision
instruction_units:
  - unit_id
    locator
    classification: obligation | context
    obligation_ids: []       # required for obligation
    rationale: ...           # required for context
inputs: exact ground-truth/source refs + revisions
document_assurance_profiles: [exact leaf refs]  # whole field absent when none; non-empty if present
change_boundary:
  write_scope: concrete local paths
  out: explicit negative boundary
expected_artifacts: stable IDs + refs
obligations:
  - obligation_id
    instruction_unit_ids
    requirement
    expected_artifact_ids
    verification_mode
    local_check_refs
```

Every normative unit maps to at least one obligation; every obligation maps back to a unit. Context
classification requires a rationale. Generated digests/state/evidence/verdicts are forbidden.

### 5.2 Optional DocumentAssuranceProfile and disposable resolution

`DocumentAssuranceProfile` retains version, summary, parameters, one rule-family identifier,
owner/reason-to-change, two real reuse witnesses, change constraints and required checks. It contains
no capability, enforcement level, authority, concrete task path, stage order or one-off schema/rubric.

A resolution with no `DocumentAssuranceProfile` is a required positive case. Resolution accumulates
checks/constraints and uses stricter numeric limits; conflicts name owners and fail. V3 implements
normalized local paths, not generalized URI/glob algebra.

`ResolvedAssurancePlan` is immutable for a run but disposable and byte-rebuildable from pinned
WorkSpec, `DocumentAssuranceProfile` versions and resolver. It does not copy canonical instruction
text, obligations, inputs,
expected artifacts or ground truth. It stores references plus only resolved deltas, boundary
projection, check order, conflicts and repair cap.

### 5.3 Closed local deterministic checks

V3 is not a tool plug-in framework. `LocalCheckSpec` is a closed union:

| Kind | Required subjects/config | Success oracle |
|---|---|---|
| `file_exists` | candidate ref + artifact ref | declared artifact resolves |
| `json_schema` | candidate JSON ref + exact schema ref | validator reports valid |
| `markdown_link` | candidate Markdown refs | every in-scope local link resolves |
| `locator_exists` | candidate/source ref + locator | locator resolves uniquely |
| `git_diff_boundary` | base + candidate + effective boundary | observed diff conforms |
| `command_exit` | exact argv array, fixed cwd ref, subject refs, allowed exit codes | process exit is allowed |

`command_exit` forbids shell interpolation and network assumptions; it records exact argv/cwd/exit
and raw output ref. Unknown check kind is `SPEC_GAP`, not dynamic tool discovery.

### 5.4 Coverage and candidate invariants

1. InstructionCoverageAudit binds the exact WorkSpec/instruction and is `COVERED` before START.
2. Every obligation occurs exactly once in FulfillmentReport and ReviewResult.
3. `IMPLEMENTED` requires at least one resolvable locator into the exact payload candidate.
4. `NOT_IMPLEMENTED` is explicit and cannot become unqualified success.
5. Manifest covers every actual add/modify/delete and is solely diff-verifier-authored.
6. Any out-of-boundary delta is `NONCONFORMANT`.
7. Every expected artifact exists in the manifest or is explicitly missing.
8. Every deterministic obligation binds an exact CheckResult; raw evidence remains authoritative.
9. ReviewPackage logically includes raw instruction/sources, plan, actual candidate artifacts,
   fulfillment, manifest, checks and coverage. Executor summary is supplemental only.
10. ReviewResult explicitly rechecks instruction completeness and covers every obligation.
11. Repair regenerates manifest, fulfillment mapping, checks, coverage and package for C2.
12. AssuranceCandidate exists before FINAL; one AssuranceSummary is generated only after FINAL.
13. `REJECT/REPLAN` never promotes payload; accepted promotion is explicit and recorded.

## 6. Product flow

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

User-facing reports show only objective/candidate, instruction or obligation exceptions, failed
checks/boundary deltas, blocking findings, uncertainty and the requested decision.

## 7. V2 disposition

Signed v1/v2 contracts, schemas and history remain immutable. V3 defaults all old directories to
`historical-only`. V3-N0 inventories only old primitives explicitly proposed as dependencies:

- canonicalization/content binding;
- closed JSON-schema validation;
- Git path/diff observation;
- frozen review-subject binding;
- one-repair/VERIFY limit.

Each proposed reuse receives `reuse | adapt | reject` plus exact tests. Reusing any other old component
later is `SPEC_GAP` until the dependency map is amended. A4 is accepted v2 history and may be
inspected as source material, but it has no v3 dependency authority unless selected through this
reuse process.

V3 removes from its default interface: capabilities/enforcement floors, resource grants, generalized
URI/intersection algebra, approval/activation receipts, distributed event/CAS/idempotency protocol,
generic receipt taxonomy, multi-track review, generic gates/waivers, external-effect recovery and
Retrospective/issue-registry state machines.

## 8. Construction review protocol

V3 does not use the unfinished product harness to certify itself.

- execution session is sole writer to the current node allowlist;
- reviewer reads exact candidate directly and never edits it;
- a blocker names node acceptance ID, candidate locator, ground-truth locator and minimum fix;
- `SPEC_GAP` stops; it is not patched inside an implementation candidate;
- implementation nodes permit one FULL, at most one user-approved fix and one targeted VERIFY;
- no autonomous second fix/review round.

Review burden is deliberately tiered:

| Node | Gate |
|---|---|
| V3-N0 | contract/transition semantic review + user signature |
| V3-N1 | one interface/implementation FULL; optional one fix/VERIFY |
| V3-N2 | one review/repair implementation FULL; optional one fix/VERIFY |
| V3-N3 | deterministic results + real-pilot user adoption decision; no extra code FULL |
| V3-N4 | deterministic administrative verification only |

Reviewer prompt:

```text
Review only V3-N<n> and the exact candidate diff.
Check the node allowlist, every acceptance ID, handed-forward interfaces and declared ground truth.
Do not redesign v3, import future-node requirements or request OUT features.
Return PASS / CHANGES_REQUIRED / SPEC_GAP.
```

## 9. Execution nodes

### V3-N0 -- transition boundary and core contract

**Outcome:** a signed narrow contract on an uncontaminated A3-based branch.

- **IN:** approved plan bytes; A3 `7db177d...`; historical v1/v2 refs; decisions D1--D10.
- **OUT:** controller implementation, A4 import or rewrite, A5--A7, P4, business content,
  old-file deletion.
- **allowed existing files:** this plan; `.goals/LEDGER.md` thin pointer;
  `.goals/plans/general-harness-v2-architecture-revision.plan.md` historical banner/pointer only;
  `ResearchSystem/docs/General-Harness-v2-Design.md` historical banner only if retained.
- **allowed new roots/files:**
  - `ResearchSystem/migration/document-work-assurance-v3/N0/**`;
  - `ResearchSystem/contract/Document-Work-Assurance-Contract-v3.md`;
  - `ResearchSystem/schema/document-assurance-v3/common.schema.json`;
  - `ResearchSystem/schema/document-assurance-v3/document-work-spec.schema.json`;
  - `ResearchSystem/schema/document-assurance-v3/document-assurance-profile.schema.json`;
  - `ResearchSystem/schema/document-assurance-v3/resolved-assurance-plan.schema.json`;
  - `ResearchSystem/schema/document-assurance-v3/assurance-work-state.schema.json`;
  - `ResearchSystem/schema/document-assurance-v3/instruction-coverage-audit.schema.json`;
  - `ResearchSystem/schema/document-assurance-v3/user-decision.schema.json`;
  - `ResearchSystem/document-harness/README.md`.
- **generated outputs:** N0 contract fixtures/results only under its migration root.
- **acceptance:**
  - `N0-A1`: branch base is accepted A3; approved plan ref/blob and rollback are recorded;
  - `N0-A2`: A4 is labelled accepted-v2/historical-only-for-v3; no A4 import/default dependency
    exists;
  - `N0-A3`: only explicitly nominated old primitives receive reuse decisions; all other old roots
    default historical-only;
  - `N0-A4`: WorkSpec instruction mapping, optional no-`DocumentAssuranceProfile` path, disposable
    `ResolvedAssurancePlan`, small `AssuranceWorkState`, candidate/evidence topology and UserDecision
    phases are closed;
  - `N0-A5`: no capability/enforcement/activation/authority-grant surface exists;
  - `N0-A6`: no canonical fact is duplicated into `ResolvedAssurancePlan`;
  - `N0-A7`: every authored field maps to a locked decision and observed failure mode; no exhaustive
    speculative ablation catalogue is required;
  - `N0-A8`: named consumers, P4 and non-document platform/domain vocabulary are absent from core
    schemas; document-work vocabulary is permitted;
  - `N0-A9`: contract and schema fixtures are green; repository audit/diff check pass.
- **stop:** user signs Contract v3 and authorizes V3-N1.

### V3-N1 -- obligation-to-evidence vertical slice

**Outcome:** from WorkSpec to a mechanically checked candidate, without semantic review yet.

- **IN:** signed N0 interfaces and exact reuse decisions.
- **OUT:** ReviewResult, repair, final decision, cutover, P4/business writes.
- **allowed existing file:** `ResearchSystem/tooling/rsc.py` only for explicit v3 subcommands.
- **allowed new roots/files:**
  - `ResearchSystem/schema/document-assurance-v3/local-check-spec.schema.json`;
  - `ResearchSystem/schema/document-assurance-v3/candidate-record.schema.json`;
  - `ResearchSystem/tooling/rsclib/document_harness/{__init__,spec,assurance_profiles,assurance_plan,assurance_state,instruction,candidate,checks,views}.py`;
  - `ResearchSystem/tooling/tests/document_harness/**`;
  - `ResearchSystem/migration/document-work-assurance-v3/N1/**`;
  - `ResearchSystem/generated/document-assurance/test/**`.
- **interfaces handed forward:** validated WorkSpec; InstructionCoverageAudit; rebuildable
  `ResolvedAssurancePlan`; `AssuranceWorkState`; CandidateRecord partitions;
  LocalCheckSpec/CheckResult; coverage view.
- **internal checkpoints, no user gate:** N1a spec/no-assurance-profile/resolve/state; N1b instruction audit,
  candidate topology, fulfillment/manifest/checks/coverage.
- **acceptance:**
  - `N1-A1`: no-`DocumentAssuranceProfile` positive path and no empty placeholder;
  - `N1-A2`: any `DocumentAssuranceProfile` instance supplies one rule family,
    owner/reason-to-change and two real reuse witnesses; otherwise the rule stays stage-local;
  - `N1-A3`: instruction unit without obligation/context disposition blocks START as `SPEC_GAP`;
  - `N1-A4`: START binds exact plan + audit; no second approval/activation path;
  - `N1-A5`: payload C contains only declared document changes; all control evidence is outside C;
  - `N1-A6`: every obligation, expected artifact and observed diff has an explicit result;
  - `N1-A7`: manifest sole author and raw CheckResult ownership are enforced;
  - `N1-A8`: closed LocalCheckSpec kinds bind exact subjects/config/evidence; unknown kind is SPEC_GAP;
  - `N1-A9`: omission, stale locator, missing artifact, wrong-candidate evidence, out-of-boundary diff,
    control-file-in-payload and executor-authored result are named negatives;
  - `N1-A10`: cold resume works from `AssuranceWorkState`/pointers without event-chain reconstruction;
  - `N1-A11`: relevant reused v1/v2 primitives remain regression-green.
- **stop:** independent bounded review + user authorization for V3-N2.

### V3-N2 -- bounded semantic review, repair and final disposition

**Outcome:** actual-artifact review and one terminal assurance path.

- **IN:** accepted N1 interfaces/evidence topology.
- **OUT:** multi-track review, second repair, review-of-review, external gates, default cutover, P4.
- **allowed existing files:** `ResearchSystem/tooling/rsc.py` v3 subcommands only;
  `ResearchSystem/document-harness/README.md` interface links only.
- **allowed new roots/files:**
  - `ResearchSystem/schema/document-assurance-v3/review.schema.json`;
  - `ResearchSystem/schema/document-assurance-v3/assurance.schema.json`;
  - `ResearchSystem/schema/document-assurance-v3/harness-issue.schema.json`;
  - `ResearchSystem/tooling/rsclib/document_harness/{review,flow,summary,issues}.py`;
  - `ResearchSystem/tooling/tests/document_harness_review/**`;
  - `ResearchSystem/document-harness/EXECUTION.md`;
  - `ResearchSystem/document-harness/REVIEW.md`;
  - `ResearchSystem/migration/document-work-assurance-v3/N2/**`;
  - `ResearchSystem/generated/document-assurance/review-test/**`.
- **interfaces handed forward:** ReviewPackage/Result; repair boundary; AssuranceCandidate;
  UserDecision; AssuranceSummary; optional HarnessIssue/triage.
- **acceptance:**
  - `N2-A1`: ReviewPackage uses exact logical membership and requires actual subjects; summary-only
    substitution fails without byte-copying every source;
  - `N2-A2`: FULL rechecks instruction completeness and covers every obligation;
  - `N2-A3`: verdict enums/residual uncertainty are closed and no semantic-proof field exists;
  - `N2-A4`: REPAIR binds candidate + accepted findings + repair boundary;
  - `N2-A5`: C2 regenerates manifest, fulfillment mapping, all checks, coverage and package;
  - `N2-A6`: VERIFY covers findings, whole repair diff and permanent boundaries; remaining problem
    stops without second repair/review;
  - `N2-A7`: AssuranceCandidate precedes FINAL; one Summary follows FINAL; no temporal self-binding;
  - `N2-A8`: REJECT/REPLAN never promotes; accepted promotion is explicit and recorded;
  - `N2-A9`: controller never strengthens verifier/reviewer claims;
  - `N2-A10`: HarnessIssue cannot mutate the live run and only post-run user triage routes it;
  - `N2-A11`: no recursive review, generic waiver/gate or Retrospective lifecycle exists.
- **stop:** independent bounded review + user authorization for V3-N3.

### V3-N3 -- two real document shadow runs and adoption decision

**Outcome:** measured evidence from real workflows, not self-designed fixtures alone.

- **IN:** accepted N2; one real archived/disposable multi-file Markdown/design workflow; one real
  archived/disposable structured JSON/YAML workflow with schema/lint/semantic review. User approves
  the exact shadow subjects; no production mutation is required.
- **OUT:** synthetic-only adoption, source-code task, external effects, P4, default cutover.
- **allowed existing files:** none outside the approved disposable/shadow subjects.
- **allowed new roots:**
  - `ResearchSystem/migration/document-work-assurance-v3/N3/**`;
  - `ResearchSystem/generated/document-assurance/shadow/**`.
- **measure:** authored fields/files; generated records; user decision surface; elapsed execution and
  review effort; obligation omissions; false-positive blockers; manual recovery; cold resume; unused
  mechanisms; whether control effort dominates protected work.
- **acceptance:**
  - `N3-A1`: both real workflows complete or truthfully stop under the v3 lifecycle;
  - `N3-A2`: no instruction, candidate artifact or residual uncertainty disappears;
  - `N3-A3`: simple runs create no empty `DocumentAssuranceProfile`/gate/recovery/capability/event
    artifacts;
  - `N3-A4`: one FULL/repair/VERIFY cap and candidate isolation hold end to end;
  - `N3-A5`: user primarily approves WorkSpec obligations/exceptions, not generated metadata;
  - `N3-A6`: burden/false-positive/limitations report is complete;
  - `N3-A7`: a `DocumentAssuranceProfile` proposal is permitted only for a rule witnessed in both
    real instances;
  - `N3-A8`: v1/v2 history, production P4 and canonical pilot sources remain untouched.
- **decision:** user chooses `ADOPT_DOCUMENT_V3`, `REVISE_V3` or `ROLLBACK_TO_V2_HISTORY`. Synthetic
  evidence alone can never produce `ADOPT_DOCUMENT_V3`.

### V3-N4 -- conditional administrative cutover

**Entry:** user chose `ADOPT_DOCUMENT_V3` at N3.

- **IN:** exact accepted N2 implementation and N3 measurement/user decision.
- **OUT:** business-stage activation, P4, source-code/general-platform expansion, old runtime deletion.
- **allowed existing files:**
  - `ResearchSystem/tooling/rsc.py` document-work default only;
  - `ResearchSystem/document-harness/{README,EXECUTION,REVIEW}.md`;
  - `ResearchSystem/README.md` document-harness link only;
  - this plan and `.goals/LEDGER.md` pointer/status only;
  - v2 plan historical/supersession banner only.
- **allowed new root:** `ResearchSystem/migration/document-work-assurance-v3/N4/**`.
- **acceptance:**
  - `N4-A1`: default applies only to declared document-work consumers;
  - `N4-A2`: one entry reads WorkSpec/`ResolvedAssurancePlan`/`AssuranceWorkState` and fixed role
    instructions;
  - `N4-A3`: v1/v2 remain recoverable history and are only eligible for a later retirement review;
  - `N4-A4`: exact rollback/default pointer is tested and recorded;
  - `N4-A5`: P4 and every business run remain separately authorized;
  - `N4-A6`: deterministic suites, repository audit and diff allowlist pass.
- **gate:** deterministic administrative verification, then user confirms cutover; no additional FULL.

## 10. Adoption and anti-overfitting rules

- No v3 adoption without two real document shadow runs.
- No `DocumentAssuranceProfile` without two real reuse witnesses.
- No candidate acceptance when obligation coverage, actual-artifact membership or boundary result is
  incomplete.
- No core mechanism added for a hypothetical coding/security/platform consumer.
- If measured harness control effort dominates the protected document work, decision is `REVISE_V3`,
  not adoption.

## 11. Rollback and long-term growth

- Every semantic implementation node has one candidate plus at most one user-approved fix.
- Signed contracts are never amended in place; corrections create a versioned successor.
- A live run pins exact WorkSpec/`DocumentAssuranceProfile`/resolver/schema versions; later changes do
  not mutate it.
- V3 branch starts from accepted A3, so abandoning v3 leaves v1/v2 history untouched.
- N4 changes only the document-work entry/pointer. Rollback restores that pointer; it does not delete
  or rewrite history.
- HarnessIssue triage follows observed evidence: workflow-local first, then
  `DocumentAssuranceProfile` only after reuse, verifier/reviewer implementation if local, and core
  only for ownership/invariant defects shared across multiple `DocumentAssuranceProfile` objects.
- Hard enforcement, tools/security/compliance, observability dashboards and artifact UI are separate
  projects. V3 neither models their schemas nor claims their guarantees.

## 12. Fresh-context reading contract

Before approval: read this plan §§0--3, §9 and the exact Git status only.

After approval, every execution/review context reads:

1. §§0, 2--6, 8 and 10 of this plan;
2. only the current node in §9;
3. the immediately preceding accepted interface/reuse record;
4. exact node ground-truth refs.

No chat history, full v2 plan or unrelated earlier node report is required. A node-local summary may
link these sources but cannot reinterpret locked decisions.

## 13. Approval semantics

User approval means:

- the product goal moves from General Harness v2 to Document Work Assurance Harness v3;
- V3-D1--D10 and the five-node execution sequence are accepted;
- completed A4 does not become a v3 dependency, and A5--A7 do not continue automatically;
- only V3-N0 is authorized next.

Approval does not authorize a v3 contract/code candidate, cutover, P4 or deletion. The execution
session records the exact approved plan Git blob/candidate ref in the V3-N0 administrative record;
the approved plan bytes remain unchanged.

Approval also does not authorize Appendix A. Its implementation requires a later, separate user gate
and must not be added to V3-N0--V3-N4 implicitly.

## Appendix A -- optional Claude Code hook adapter

### A.1 Status and entry condition

This is a Claude-Code-specific outer guard, not part of the portable v3 core. It is optional, is not
required for v3 adoption, and is not a sixth execution node. It may be proposed only after V3-N3
records at least one recurring relevant failure class -- an out-of-boundary native write, assurance
state left stale after mutation, or an unsupported completion claim -- or after a later explicit user
request. Implementation requires its own bounded plan, candidate and review.

If authorized later, its implementation root is:

`ResearchSystem/integrations/claude-code/document-assurance-hooks/`

Expected adapter-local artifacts are `README.md`, `pre-write-guard.js`,
`post-write-observer.js`, `stop-assurance-gate.js`, `settings.project.snippet.json` and bounded
adapter tests. This appendix authorizes none of them now.

### A.2 Hook responsibilities

1. `PreToolUse[Write|Edit]` may compare the target path with the already-resolved boundary
   and reject a matched native write before bytes are written. It may also protect core control and
   evidence roots. This is a partial guard only: it does not cover shell commands, external processes
   or other write paths and must not be described as non-bypassable enforcement.
2. `PostToolUse[Write|Edit]` may record the touched path or mark the current candidate dirty
   so that existing verification or review evidence becomes visibly stale. It cannot undo the write.
3. `Stop` may run one bounded completion check for missing obligations or artifacts, stale checks or
   review, and a missing `AssuranceSummary`; it may block an unsupported completion claim. Full
   verification remains owned by the v3 verifier and reviewer.

Hooks may emit only an external `HookObservation` or dirty marker bound to the exact candidate. They
do not author or own `AssuranceWorkState`, the manifest, `CheckResult`, `ReviewResult`,
`UserDecision` or `AssuranceSummary`. The absence of a hook event is not evidence that work was
correct or authorized, and the core workflow must remain fully usable without the adapter.

### A.3 Performance and anti-expansion contract

- Register pre/post hooks only for native `Write` and `Edit` events, not for every tool.
- Per-event work is bounded to local path comparison and a small append/update. It must not run a
  repository-wide scan, Git diff, candidate hash, schema suite, compiler, test suite or semantic
  review.
- Run expensive checks once at `Stop` or at the existing v3 verification boundary.
- Before adoption, measure event count, total added time, median/p95 hook latency and false blocks in
  a disposable comparison run. Do not adopt the adapter if its overhead dominates or the motivating
  failure does not recur.
- Do not add a shell-command parser, universal authorization model, human-identity proof, semantic
  reviewer, receipt chain or hook-event ledger under this appendix.
