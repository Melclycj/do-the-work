# Plan: General Harness v2 architecture revision

> [!warning] SUPERSEDED — historical only (2026-07-20)
> The product goal moved from General Harness v2 to **Document Work Assurance Harness v3** per the
> user-approved [[document-work-assurance-harness-v3.plan|v3 plan]] (approval binds plan SHA-256
> `9B08CD0038FA0C36E76674B7CE386129D9797EFFE5CEC7FABBF69699811F171F`; recorded in the
> [V3-N0 record](../../migration/document-work-assurance-v3/N0/N0-record.md)).
> A1–A4 are closed and immutable accepted history; **A5–A7 and cutover are parked** under this plan:
> they never started and do not continue automatically. Do not execute any node below. The v3 branch is `document-work-assurance-v3`, rooted at
> accepted A3 closeout `7db177d`; A4 remains accepted v2 history (historical-only-for-v3).

- **slug**: `general-harness-v2-architecture-revision`
- **created**: 2026-07-19
- **status**: `SUPERSEDED — historical only; the v3 plan is active (see banner)`
- **current node**: `none — v2 closed at A4; A5–A7 and cutover are parked (never started, no automatic continuation)`
- **bootstrap state**: `SUPERSEDED_BY_V3`
- **latest accepted node boundary**: A3 accepted at fix candidate
  `a5861fff8ec116addd9db60e3ebc07e0e1e33f20` on this branch's history; A4 accepted on the v2 line at
  fix candidate `f91a7c45fe6d6a920f03ac0e33b7baed7d034d58` (closeout `de39b3d`, VERIFY `PASS` —
  not part of the v3 branch history)
- **contract v2 signature boundary**: the unique `A2-ADMINISTRATIVE-CLOSEOUT-v1` commit; the
  signature authorized A3 construction
- **historical A1 rev1 result**: `SPEC_GAP`; payload/fix line remains immutable history
- **superseded unapproved replan candidate**: `180ccb4aef80f7d7bed9866c5c7aa37901ab476c`
- **next action**: none under this plan — follow the v3 plan (`document-work-assurance-harness-v3`)
- **v1 boundary**: S0–S2 complete at `c64b9c5f921238eb307f67227b5082b54ad45420`
- **planning base**: `c64b9c5f921238eb307f67227b5082b54ad45420`
- **A0 execution base**: the unique correctly-parented `HARNESS-V2-PLAN-BOUNDARY-v1` marker commit
- **parent plan**: `research-system-stage-control-refactor.plan.md`
- **execution worktree**: `D:\Thesis-stage-control-refactor`
- **execution branch**: `codex/research-system-stage-control-refactor` (v2 historical line, tip
  `de39b3d`); v3 work happens on `document-work-assurance-v3`
- **execution session**: sole writer
- **node-review session**: read-only; works with the user at every node gate

## 1. Goal

Replace the v1 monolithic, Git-centred Stage Record with a small, domain-neutral harness model that
can govern coding, multi-file document work, research synthesis, semantic review and privileged
external actions without forcing every workflow to carry every possible field.

The result must remain safe to resume in a fresh context, must preserve immutable evidence and user
authority, and must have an operational feedback loop through which shortcomings discovered during
real runs can be recorded and considered for a later harness update.

This plan revises the harness architecture before original S3. It does not execute P4.

## 2. Corrected baseline and interlock

1. Harness v1 consists of the complete S0–S2 line:
   - S0: safe snapshot and isolated execution baseline;
   - S1: Stage-Control Contract v1, schemas, lifecycle and deterministic fixtures;
   - S2: deterministic controller, closure checks and repo-local `rs-execute`.
2. The immutable v1 implementation boundary is commit
   `c64b9c5f921238eb307f67227b5082b54ad45420` (`S2-DETERMINISTIC-CONTROLLER-v1`).
3. Original S3–S7 are paused. No review-generator implementation, P4 Stage Record migration,
   blocking cutover or P4 content write may start until this plan completes A7 after the user's A6
   cutover decision.
4. Signed S1 is not edited in place. If v2 is adopted, a separately signed v2 contract supersedes
   v1 for new runs; v1 remains immutable historical evidence.
5. Existing S2 code is neither discarded nor assumed to be the v2 core. A3 decides its disposition
   component by component after the v2 interfaces are signed.

## 3. Product boundary

The harness is a long-lived execution substrate. ResearchSystem, ResearchAgent, thesis work,
ExperimentLab, coding tasks and document-design tasks are consumers of it. No consumer-specific
object type, paper concept, P4 identifier or Obsidian convention belongs in the core.

The architecture must be extractable later, but physical extraction into a separate repository or
package is OUT for this revision. During A0–A7 it remains repo-local so that model validation is not
mixed with packaging and distribution work.

### 3.1 V1-to-v2 migration facts

At planning time, repository inspection finds no canonical v1 Stage Record, ReviewResult or Closure
Receipt. `ResearchSystem/stages/` contains only its README and `_stage-record-template.md`; original
S3/S4 never created a live P4 Stage. Therefore this plan does not presume a production-data migration
or permanent dual-runtime support.

A0 must deterministically confirm this fact. If it finds any real v1 run record, the migration class
changes and A0 returns `SPEC_GAP` before A1; the plan must then add an explicit per-record preservation
and migration route.

### 3.2 V1 component change map

| V1 asset | V2 disposition |
|---|---|
| S0 snapshot/worktree boundary | Retain as immutable rollback history. Move its reusable worktree/snapshot semantics into the optional `git-worktree` profile/adapter, not the core. |
| Stage-Control Contract v1 | Keep immutable as the source of proven invariants. The v2 signature authorizes v2 construction; no business run starts during transition, and v2 becomes the default only at A7 cutover. |
| v1 Stage/Review/Closure schemas and template | Keep unchanged through A5 as regression/reference inputs. Replace them as the authored/runtime public interface with StageSpec, generated ResolvedStage/StageState and receipts. Do not convert empty templates into fake v2 records. |
| v1 schema fixtures/validator | Preserve the existing suite; map each meaningful positive/negative case into `v1-safety-traceability.md` and a v2 equivalent. No v1 case is deleted before parity is demonstrated at A5. |
| `stage_control.py` canonicalization/digest logic | Extract/adapt the proven deterministic primitives for generated v2 artifacts; remove monolithic StageRecord projections from the new core. |
| `stage_control.py` path matching, Git identity/diff/input checks | Adapt into the `git-worktree` adapter. They are not copied into the domain-neutral core. |
| `stage_control.py` lifecycle, preflight, pause/resume | Re-implement against StageState + immutable events while preserving the named v1 failure tests. Direct v1 dictionary-field access is not reused as an interface. |
| `stage_close.py` terminal/rollback/review/authority guards | Port the invariants to receipt-based closure. Move Git-specific ancestry/worktree checks to the Git adapter; replace direct monolithic-field coupling. |
| `rsc.py` and `.claude/commands/rs-execute.md` | Add v2 commands side-by-side first. Do not make v2 the default until A7 cutover. |
| `generated/stages/**` | Disposable v1 views; do not migrate. Regenerate v2 views from v2 canonical artifacts. |
| S2 test suite | Remains green throughout A3–A5 and supplies parity/negative cases. After cutover it becomes legacy regression evidence until an explicit retirement decision. |

### 3.3 Migration sequence

```text
A0: confirm no live v1 run data; freeze component/invariant map
→ A1: validate the smaller v2 ownership model without production code
→ A2: sign v2 interfaces before changing implementation
→ A3: build v2 core and Git adapter side-by-side; reuse/extract only mapped primitives
→ A4: build v2 review/gates/feedback path
→ A5: run v1 regression + v2 parity/cross-archetype shadow tests
→ A6: dry-run P4 and choose CUTOVER / REVISE / ROLLBACK
→ A7 on CUTOVER: make v2 the default; freeze v1 runtime as non-default rollback/legacy evidence
→ after a successful real P4 pilot: separately decide whether to remove v1 runtime files
```

V2 is therefore not a blank-slate rewrite and not an in-place mutation of v1. It is an
interface-first replacement that reuses proven primitives and tests, runs side-by-side until parity,
then cuts over at an explicit boundary. Because no live v1 Stage exists, default cutover requires no
record conversion. Removing v1 source before the first real v2 pilot is forbidden because it would
destroy the immediate rollback implementation.

## 4. Target model

The following ownership split is the target architecture. A1 tests its necessity and A2 freezes its
exact schemas. Field lists below are the maximum proposed authored surface, not permission to add
more fields without A1 evidence.

### 4.1 `StageSpec` — small authored intent

`StageSpec` contains only decisions that a user or planning agent must make:

```yaml
stage_id: stable identity
objective: one bounded outcome
harness_contract: versioned contract reference
profiles: version-pinned profile references
inputs: declared input resources and revisions
resource_policy:
  write_scope: resources this stage may mutate
  out: explicit negative boundary
expected_outputs: completion artifacts
interfaces: declared downstream hand-off contracts
acceptance: stable requirements and oracles
gates: optional authority decisions
review: optional review tracks
recovery: required only for side-effecting work
```

Rules:

- optional mechanisms are absent, not represented by forests of `null`, `false` and `[]`;
- undeclared capabilities are denied;
- fields that the controller can derive are forbidden in authored input;
- a StageSpec is immutable once activated; changes create a new revision and require re-resolution;
- StageSpec contains no live execution status and no review result.

### 4.2 `Profile` — reusable domain policy

A profile supplies conditional requirements, capability names, gates, verifier types and adapter
bindings for one reusable environment or workflow family. Initial validation profiles are:

- `git-worktree` — revision, branch/worktree, diff, commit and Git recovery semantics;
- `document-workflow` — document/note resources, anchors, snapshots, link/render checks;
- `semantic-review` — immutable review packages, tracks, findings and user decision packets;
- `research-evidence` — source verification, evidence sufficiency and promotion gates;
- `privileged-actions` — network, spend, experiment, publication and external-side-effect authority.

Only profiles needed by a stage are resolved. A profile may strengthen core invariants but may not
weaken scope enforcement, immutable reviewed inputs, actor separation, explicit user authority,
audit retention or the prohibition on automatic next-stage authorization.

Profile composition is deterministic. Conflicting policies fail closed and name the conflict; the
controller never chooses a more permissive interpretation.

Ownership is one-way: profiles own reusable policy floors and vocabulary; StageSpec selects profiles,
supplies their declared parameters and may add stage-specific requirements. StageSpec cannot redefine
profile semantics or weaken a floor. Resolution uses restrictive composition: allowed scopes
intersect, denials and required gates/checks accumulate, quantitative limits take the stricter value,
and a stage may request only a subset of profile-supported capabilities. Any unresolvable combination
is rejected rather than copied into two competing owners.

### 4.3 `ResolvedStage` — generated immutable policy candidate

Before approval or activation, the resolver combines the StageSpec, exact profile versions and
declared environment/revision requirements into one immutable machine-generated candidate:

```text
spec identity and digest
resolved profile and adapter versions
required authorities and activation conditions
resolved resource/capability policy
resolved gates and acceptance plan
environment/revision binding
recovery plan
policy and payload digests
```

This is the normalized enforcement input. It is generated, digest-pinned and never hand-maintained.
The reusable validation logic from S1/S2 should target this layer or its adapters, not force the same
normalized fields back onto every StageSpec author.

Approval and activation are separate, non-circular steps:

```text
resolve immutable ResolvedStage candidate
→ authority approves its exact policy/payload digests in a PolicyApprovalReceipt
→ controller rechecks environment/revision facts
→ a different authorized actor issues ActivationReceipt binding candidate + approval + runtime authority snapshot
→ StageState enters the active run
```

Activation never mutates the ResolvedStage. Runtime authority/environment digests live in the
ActivationReceipt. A mismatch requires re-resolution and a new approval; the controller cannot
approve or activate its own candidate.

This is a logical safety separation, not necessarily two user prompts. For a low-risk stage, one user
decision may both approve the exact candidate and delegate activation to the controller if named
preflight conditions pass; the system still writes a separate approval receipt and later activation
receipt. High-risk profiles may require a second explicit user activation. In both cases approval
answers “is this exact plan allowed?”, while activation answers “have its start conditions now been
met, so may this run begin?”.

### 4.4 `StageState` — one small live state owner

Exactly one controller-owned StageState records the current position:

```yaml
stage_id: ...
run_id: ...
spec_ref: ...
resolved_stage_ref: ...
status: ...
current_action: optional
next_action: ...
blockers: optional
checkpoint_ref: optional
latest_event_ref: ...
latest_review_ref: optional
pending_gate_ref: optional
closure_ref: optional
```

It contains pointers, not copied evidence. Status transitions are controller-written. Human and agent
authors do not directly edit StageState. Historical transition detail lives in immutable events, so
the live file does not grow without bound.

State/event updates are crash-consistent. A transition event is content-addressed and carries the
prior event digest, expected `state_version` and an idempotency key. The controller writes the event
first, then atomically compare-and-swaps StageState to reference it. Only an event referenced by the
current StageState head is effective; a crash-created dangling event remains auditable but inert and
may be safely retried with the same idempotency key. StageState can be rebuilt by reducing the valid
event chain ending at its recorded head. A stale state version or mismatched prior digest fails closed.

### 4.5 Immutable events and receipts

Evidence is append-only and generated when applicable. Receipt types may include:

- activation;
- action/checkpoint;
- deterministic verification;
- scope delta or tripwire;
- ReviewPackage and ReviewResult;
- user decision or waiver;
- rollback/recovery;
- closure;
- harness observation and post-run retrospective.

Events record authority, lifecycle, checkpoint, review/gate, recovery, observation and closure
boundaries—not every ordinary edit or tool call.

Every receipt binds the run, relevant spec/resolved-stage versions and evidence revisions. Receipt
types are conditional: a read-only task without review or external effects does not manufacture empty
review, rollback, spend or publication records.

### 4.6 Adapters

Adapters enforce or observe profile rules against a concrete environment. Each adapter declares:

- profile and adapter version;
- supported capability/check types;
- enforcement level (`hard`, `instrumented`, `audit-only`, `unsupported`);
- inputs it reads and evidence it emits;
- failure and rollback semantics.

An unsupported or merely audit-only adapter cannot satisfy a stage that requires blocking
enforcement. Git is the first adapter, not the universal world model.

## 5. Long-term growth: operational feedback, not speculative expansion

The harness grows from evidenced shortcomings found while it is being used.

### 5.1 During a run

An executor, verifier, reviewer or user may record a `HarnessObservation` when the pinned harness
version exhibits a defect, security gap, false positive, false negative, missing capability or
material usability burden.

The minimum observation is:

```text
observation_id
originating run/stage and harness/profile/adapter versions
category and severity
concise observed behaviour
evidence reference
safe workaround, if one exists
```

An observation does not modify the harness, current StageSpec, resolved policy or acceptance contract.
Severity determines only the immediate run response:

- any safety, authority, scope-enforcement or evidence-integrity concern—and any observation whose
  category/severity is uncertain—triggers a tripwire and safe pause;
- a non-critical limitation may use an explicitly recorded workaround within existing authority;
- a convenience idea is recorded without expanding the current stage.

Executor and reviewer cannot downgrade a safety-relevant observation. Only an explicit user or
designated safety-authority receipt may reclassify it. A workaround is permitted only when the
controller proves that it does not change StageSpec, ResolvedStage, acceptance, profile/adapter
versions, write scope or expected outputs; otherwise it is a scope delta and the run remains paused.

### 5.2 At stage closure or safe pause

The controller generates a `HarnessRetrospective` containing the run's observations, duplicates or
related prior observations, impact evidence and the workaround actually used. The user decides one
of four dispositions:

1. `NO_CHANGE` — expected limitation or insufficient evidence;
2. `BACKLOG` — real issue, but no immediate harness work;
3. `OPEN_MAINTENANCE_STAGE` — bounded normal update;
4. `URGENT_SECURITY_MAINTENANCE` — original run stays paused; repair begins in an isolated harness
   maintenance stage.

The originating stage never updates the harness as part of its own scope and never silently resumes
under a new version.

If a run has no HarnessObservation, closure records `observation_count=0`; it does not create an empty
Retrospective or another user gate. If observations exist, every observation requires one of the four
user dispositions before normal closure. `BACKLOG` and both maintenance dispositions create or update a
stable `HarnessIssue` in one versioned issue registry; repeated observations link to that issue rather
than creating competing status owners. The immutable observations remain the evidence, while the
registry alone owns issue lifecycle (`open`, `accepted`, `in-maintenance`, `resolved`, `rejected`).

### 5.3 Harness maintenance stage

Every accepted update is a separate harness-maintenance stage with:

- exact originating observations and evidence as inputs;
- affected core/profile/adapter boundary;
- regression case reproducing the observed failure;
- impact and migration decision;
- deterministic tests plus independent node review;
- user approval of the new version and activation policy.

The smallest owning layer changes:

- adapter defect → adapter patch;
- reusable workflow requirement → profile revision;
- genuinely cross-profile invariant or ownership change → core contract revision.

No field or mechanism enters the core merely because it might someday be useful.

### 5.4 Versioning and compatibility

- Every run pins core contract, schema, resolver, profile and adapter versions plus their content
  digests; names or semantic versions alone are insufficient.
- Closed records are never rewritten; corrections append superseding evidence.
- A breaking ownership/schema/lifecycle change creates a new core major version.
- A backward-compatible optional profile capability creates a profile minor version.
- An adapter fix that does not change declared semantics creates an adapter patch version.
- Migrations are deterministic transformations that emit a receipt binding source/target digests,
  transform version, loss report and renewed authority validation; source artifacts remain intact and
  continue to be verified by their original bundle.
- Every retained Stage/receipt keeps content-digest references to the exact core/schema/profile/
  adapter/resolver validation bundle needed to read it. Those bundles remain available in read-only
  form for as long as the records are retained; Git history alone is not treated as an active support
  policy. Whether an old version remains executable is a separate explicit decision.
- Before executable support is removed, every paused side-effecting run on that version must reach
  safe closure/recovery or receive an explicit rebind decision.
- A paused run may use a newer harness only through an explicit rebind/restart decision whose receipt
  names both versions and revalidates authority.

These bundle-retention rules apply to canonical run/receipt records. If A0 confirms the expected fact
that v1 produced no such records, v1 needs no permanent compatibility runtime: its Git boundary and
regression evidence are retained through cutover, and later source removal follows A7's explicit
retirement route.

## 6. Minimal bootstrap development protocol

The product harness does not govern its own construction before it exists. This fixed bootstrap
protocol governs the outer A0–A7 development plan. Product-grade StageState, ReviewPackage,
ReviewResult, receipt, digest, lease, idempotency and activation mechanisms are implemented and tested
inside A2–A6; they are not manually simulated as authority for the outer development workflow.

The two sessions may remain open simultaneously, but only the execution session writes.

### 6.1 Execution session — sole writer

For one current node, the execution session:

1. reads this plan and verifies the exact current node, clean base and node write allowlist;
2. changes only the node payload and deterministic tests;
3. runs the declared checks;
4. creates one candidate commit with a unique node candidate marker;
5. reports the candidate SHA, base, changed paths, test results and known limitations;
6. stops. It does not create a review packet, review receipt, user-disposition receipt or lease update.

It may implement review findings only after the user explicitly authorizes them. Silence is never
approval.

### 6.2 Node-review session — read-only user partner

The reviewer receives the candidate SHA from the user, reads the current node definition and inspects
the candidate directly. It checks the node payload, interfaces, ground truth and acceptance criteria;
it does not audit absent bootstrap receipts or demand the unbuilt product harness to certify itself.
It reports `PASS`, `CHANGES_REQUIRED` or `SPEC_GAP` to the user and writes nothing.

### 6.3 One concise durable Node Record

After the user decides, the execution session creates or updates exactly one node-local record:

`ResearchSystem/migration/general-harness-v2/nodes/<node-id>/NODE.md`

It records only:

- node objective and write scope;
- candidate SHA(s) and deterministic result summary;
- review verdict and blocking finding IDs/locations;
- the user's decision;
- current status and next action;
- any known bootstrap incident that materially affects interpretation.

The Node Record is a concise handoff, not a verbatim ReviewResult or a second controller. Git commits
provide payload identity and rollback. Because a candidate cannot contain its own commit SHA, the Node
Record is not part of the semantic candidate. The user's decision authorizes one administrative
closeout commit that may change only the Node Record and, when the decision changes the active node or
state, this plan's top metadata/current-pointer explanation. It must not modify the reviewed payload.
`.goals/LEDGER.md` remains a static entry to this plan and changes only when the active plan itself
changes, not at every node transition.

### 6.4 Bounded convergence

- FULL review: `PASS | CHANGES_REQUIRED | SPEC_GAP`.
- If the user accepts `CHANGES_REQUIRED`, the executor may create one bounded fix candidate.
- VERIFY examines only accepted findings, changed cells and permanent scope/interface checks; its
  result is `PASS | SPEC_GAP`.
- Any remaining/new blocker after VERIFY stops for user-directed node replanning. It does not create
  another automatic review/fix round.

### 6.5 A1 bootstrap incident and supersession

The committed files `review-result-verify-v1.txt` and `user-disposition-verify-v1.txt` are byte-identical
and both contain the user disposition. The actual VERIFY ReviewResult was not persisted. Both files and
all existing A1 commits remain immutable history, but neither duplicate file is treated as an
authoritative ReviewResult.

This is a bootstrap bookkeeping incident, not a product `SPEC_GAP`. Do not create the previously
requested D1 correction/receipt/hash/supersession chain. Candidate
`180ccb4aef80f7d7bed9866c5c7aa37901ab476c` was never approved and its rev2 definition is superseded by
the simplified A1 definition below.

### 6.6 Self-hosting threshold

- A0–A4 and the outer control of A5–A7 use this minimal bootstrap protocol.
- A5 runs the completed v2 harness only as a shadow test subject.
- A6 may use it for a non-writing P4 dry-run, still inside the bootstrap boundary.
- Only after reviewed A7 cutover does v2 become the default harness for later real stages.

### 6.7 Bootstrap correction boundary

The user's 2026-07-19 instruction to simplify the workflow authorizes one plan/LEDGER-only commit,
`HARNESS-V2-BOOTSTRAP-SIMPLIFICATION-v1`, as the direct child of unapproved historical candidate
`180ccb4aef80f7d7bed9866c5c7aa37901ab476c`. No semantic review packet is required for this planning
correction. After deterministic repository checks, the execution agent starts only the simplified A1
node and stops at its candidate review gate.

## 7. Architecture-revision nodes

### 7.1 Exact write matrix and shared tripwire

The semantic candidate may write only the node's payload paths in the table below. After the user
decision, the administrative closeout may update only this plan's current-pointer fields and one
`ResearchSystem/migration/general-harness-v2/nodes/<node-id>/NODE.md`; it may not change payload.
Neither boundary may create outer bootstrap ReviewPackage/ReviewResult/UserDisposition files. A4/A5
may create similarly named product fixtures only as test payload, never as authority for the outer
node. Exact payload paths are:

| Node | Exact additional write allowlist |
|---|---|
| PLAN-GATE | this plan; historical parent plan; `.goals/LEDGER.md` |
| A0 | `ResearchSystem/migration/general-harness-v2/nodes/A0/**`; `ResearchSystem/migration/general-harness-v2/v1-safety-traceability.md` |
| A1 | `ResearchSystem/migration/general-harness-v2/nodes/A1/revision-2/**`; shared `v1-safety-traceability.md`; all existing A1 rev1/review artifacts are read-only history |
| A2 | `ResearchSystem/migration/general-harness-v2/nodes/A2/**`; shared traceability file; `ResearchSystem/contract/General-Harness-Contract-v2.md`; `ResearchSystem/schema/harness-v2/**`; `ResearchSystem/harness/README.md`; `ResearchSystem/harness/profiles/**`; `ResearchSystem/harness/adapters/**`; `ResearchSystem/harness/issues/**` |
| A3 | `ResearchSystem/migration/general-harness-v2/nodes/A3/**`; shared traceability file; `ResearchSystem/tooling/rsc.py`; `ResearchSystem/tooling/rsclib/harness/**`; `ResearchSystem/tooling/tests/harness/**`; `.claude/commands/rs-execute.md`; `ResearchSystem/generated/harness/**` |
| A4 | `ResearchSystem/migration/general-harness-v2/nodes/A4/**`; shared traceability file; `ResearchSystem/tooling/rsclib/harness/**`; `ResearchSystem/tooling/tests/harness/**`; `ResearchSystem/harness/templates/**`; `.claude/commands/rs-execute.md`; `ResearchSystem/generated/harness/**` |
| A5 | `ResearchSystem/migration/general-harness-v2/nodes/A5/**`; shared traceability file; `ResearchSystem/generated/harness/shadow/**` |
| A6 | `ResearchSystem/migration/general-harness-v2/nodes/A6/**`; `ResearchSystem/generated/harness/p4-dry-run/**`; only after the final user decision, this plan, the historical parent plan and `.goals/LEDGER.md` for pointer reconciliation |
| A7 | `ResearchSystem/migration/general-harness-v2/nodes/A7/**`; shared traceability file; `ResearchSystem/tooling/rsc.py`; `.claude/commands/rs-execute.md`; `ResearchSystem/harness/README.md`; `ResearchSystem/stages/README.md`; `ResearchSystem/stages/_stage-record-template.md`; `ResearchSystem/generated/stages/README.md`; this plan, historical parent plan and `.goals/LEDGER.md` |

Anything else is a hard scope tripwire. In particular, all `Thesis/**`, `ExperimentLab/**`, P4 owner
files, existing research-object schemas and original S3 paths are forbidden unless a later node's
table row names them exactly. A node may not use another node's broader future allowlist.

`v1-safety-traceability.md` is created at A0 and carried through A5. Its fixed columns are: v1
invariant/failure mode → A1 scenario and ablation → A2 contract/schema rule → A3/A4 enforcement guard
→ A5 negative test/result. Missing cells block the relevant node.

### A0 — Freeze and characterize Harness v1

- **Entry:** clean unique `HARNESS-V2-PLAN-BOUNDARY-v1` child of
  `c64b9c5f921238eb307f67227b5082b54ad45420`; original S3 has not begun.
- **IN:** S0–S2 plan/history, signed v1 contract/schemas/templates, S2 controller and all v1 tests.
- **OUT:** any v1 rewrite, v2 schema/code, original S3, P4 files.
- **Artifacts:**
  - `nodes/A0/v1-baseline.md` and deterministic test report;
  - `nodes/A0/v1-component-disposition.md`: ownership/duplication inventory plus component map
    `retain`, `adapt`, `legacy-read-only`, `replace`;
  - shared `v1-safety-traceability.md` with named failure modes already closed by v1.
- **Acceptance:** every v1 component has a disposition; repository-wide inventory confirms there are
  no canonical v1 run records/receipts, or the node stops as `SPEC_GAP`; no claim of unnecessary
  complexity is based only on file size; baseline tests are reproducible; S0–S2 is recorded as the
  full v1 boundary.
- **Rollback:** one documentation/evidence commit.
- **Node review focus:** factual completeness and whether the future plan would discard a proven
  safety invariant.

### A1 — Validate the minimal ownership model by ablation

- **Entry:** A0 approved at `028354f40b3b73ef52e5e804ba25567ab88b6460`; A1 rev1 closed
  `SPEC_GAP`; unapproved replan candidate `180ccb4...` is historical only.
- **Objective:** decide whether the proposed ownership split is necessary, smaller than v1 and
  representable across five workflow archetypes. A1 does not build the harness.
- **IN:** the target model in §4, A0's failure-mode inventory and reusable facts from the historical
  A1 rev1 artifacts.
- **OUT:** production schemas/controller code; executable event-chain/CAS/idempotency logic; exact
  glob-algebra implementation; product ReviewPackage/receipt/lease machinery; A2, P4 and original S3.
- **Exact payload home:** `ResearchSystem/migration/general-harness-v2/nodes/A1/revision-2/**` plus the
  A1 cells of shared `v1-safety-traceability.md`. Existing A1 root/review files remain read-only.
- **Artifacts:**
  1. `revision-2/model.md` — StageSpec/Profile/ResolvedStage/StageState/Receipt ownership and field
     decision table (`authored-core`, `conditional-profile`, `generated`, `receipt-only`, `remove`);
  2. `revision-2/scenarios.md` — Git coding, multi-file document/design, research synthesis,
     read-only semantic review and privileged external action;
  3. `revision-2/burden-rubric.md` — one simple v1/v2 comparison rule frozen in prose before counts,
     with authored work separated from generated/receipt work;
  4. `revision-2/validation-report.md` — acceptance results, limitations and explicit A2/A3 handoffs.
  After the user decision, `nodes/A1/NODE.md` is the separate administrative closeout under §6.
- **Required analysis:** remove each proposed authored field/mechanism and identify whether a named
  failure, cold-resume requirement, authority boundary or unique ownership is lost. At this node,
  cold-resume and profile composition are checked as ownership/interface requirements, not implemented
  algorithms.
- **Acceptance:**
  - all five scenarios are representable;
  - every authored-core field has ablation evidence and exactly one owner;
  - Git assumptions occur only in the Git profile;
  - simple scenarios contain zero empty optional modules, zero authored-derived fields and zero
    duplicate facts;
  - the same burden rubric is applied to v1 and v2, and applicable v2 scenarios require strictly fewer
    meaningful authored fields/actions;
  - profile floors, stage tightening and fail-closed conflict ownership are specified; exact
    path/glob subset/intersection algorithms are handed to A2/A3;
  - content-addressed events, prior-event binding, CAS, idempotency reuse, dangling-event behavior and
    approval/activation receipt binding are named as A2 contract/A3 negative-test obligations, not
    prematurely implemented here.
- **Deterministic check:** Markdown/link/structure checks and, only if useful, a small read-only
  structural validator inside `revision-2/`; no measurement-protocol commit or micro-controller.
- **Review/stop:** use §6. Reviewer evaluates the four model artifacts directly. Even `PASS` stops at
  the user's ownership-model approval gate; A2 remains forbidden until explicit approval.
- **Rollback:** one candidate commit; existing rev1 and `180ccb4` history remain untouched.

### A2 — Freeze Contract v2, schemas and extension interfaces

- **Entry:** A1 ownership model approved.
- **IN:** only A1-approved model and failure cases.
- **OUT:** controller implementation, live state migration, P4 StageSpec, standalone packaging.
- **Artifacts:**
  - General Harness Contract v2;
  - closed schemas for StageSpec, ResolvedStage, StageState and receipt/event envelopes;
  - conditional schemas for review, user decision, closure, HarnessObservation and Retrospective;
  - HarnessIssue registry schema/ownership contract;
  - profile and adapter interface contracts;
  - versioning, compatibility, deprecation and migration policy;
  - positive/negative fixtures covering all five archetypes.
- **Acceptance:** authored StageSpec remains sparse; generated fields cannot be supplied as authored
  authority; profile floors and StageSpec parameters have one-way composition; profile conflicts fail
  closed; resolve → approval → activation is non-circular and actor-separated; receipts bind exact
  version content digests; event identity includes canonical bytes, prior-event binding, expected state
  version and idempotency key; the contract states that the same idempotency key may repeat only for
  identical canonical event bytes and outcome; State-head ancestry, dangling-event inertness,
  approval/activation receipt binding and profile resource-set composition are schema-testable;
  observation cannot mutate a run; validator bundles remain readable for retained records; legacy v1
  validator remains read-only; core schemas contain no P4/domain token.
- **Rollback:** unsigned candidate commit; signed boundary only after user approval.
- **User gate:** sign Contract v2. Until signed, A3 is forbidden and v1 remains active historical
  implementation only.

### A3 — Refactor the deterministic controller around v2 ownership

- **Entry:** signed Contract v2.
- **IN:** S2 implementation and tests plus signed v2 interfaces.
- **OUT:** semantic model review, P4 migration/execution, speculative profiles.
- **Implementation order:**
  1. StageSpec parser and validator;
  2. deterministic profile resolver → immutable ResolvedStage;
  3. controller-owned StageState and append-only event writer;
  4. core scope/authority/checkpoint/closure guards;
  5. extract current Git/worktree enforcement into `git-worktree` adapter;
  6. retain v1 reader/tests as legacy compatibility evidence.
- **Acceptance:** simple stages do not require unused modules; generated normalized policy preserves or
  strengthens every retained v1 invariant; controller rejects hand-edited state/receipts; crash tests
  cover event-written/state-not-swapped, stale CAS, duplicate same-content retry, same-key/different-
  content-or-outcome rejection, dangling events, old-ref content tampering, missing ACTIVE receipt
  binding and missing/ambiguous/cyclic event ancestry; profile adapter tests cover exact match, nested
  subset, partial overlap, disjoint and multi-profile intersection using normalized resource sets; v1
  and v2 tests pass in their declared support modes; no P4/domain token in core.
- **Rollback:** one v2-core candidate boundary; v1 `c64b9c5` remains runnable as the rollback anchor.
- **Node review focus:** ownership leaks and accidental weakening of v1 safeguards.

### A4 — Add review, user gates and the operational growth loop

- **Entry:** A3 approved.
- **IN:** v2 StageSpec/ResolvedStage/StageState/event interfaces.
- **OUT:** changing the core model without `SPEC_GAP`; P4 execution.
- **Artifacts/behavior:**
  - immutable ReviewPackage and ReviewResult generation;
  - optional named review tracks with independent epochs;
  - actor/context separation;
  - user decision receipt and closure receipt;
  - HarnessObservation capture and end-of-run Retrospective;
  - maintenance-stage specification generation only after the user's retrospective disposition;
  - stable HarnessIssue deduplication and lifecycle ownership.
- **Acceptance:** post-package state/gate updates cannot change reviewed bytes; findings cannot silently
  disappear; a critical observation pauses safely; a non-critical observation can close with a user
  disposition; ambiguous safety severity fails closed; workarounds cannot hide scope deltas; no
  observation self-activates a harness update; FULL and VERIFY verdict sets are mode-closed; one full +
  one verify limit is enforced.
- **Rollback:** one review/evolution candidate boundary.

### A5 — Cross-archetype shadow validation and dual-session dogfood

- **Entry:** A4 approved.
- **IN:** the five A1 scenarios and complete v2 harness in shadow mode.
- **OUT:** P4 canonical writes, external publication, network/spend/experiment side effects.
- **Execution:** run all five scenarios through parse → resolve → preflight → checkpoint → applicable
  checks/review/gates → closure. The v2 harness is the shadow test subject; the outer A5 node remains
  governed by the minimal bootstrap protocol in §6 and does not let v2 approve its own adoption.
- **Evidence:** safety results plus the A1 burden measures repeated against the implemented system.
  Record every deficiency actually observed in shadow execution as a HarnessObservation; do not repair
  the harness during a scenario run. A1's hypothetical mechanism fixtures are not promoted as issues.
- **Acceptance:** all archetypes cold-resume in a fresh context; no scenario carries irrelevant empty
  modules; all attempted scope/authority/review bypasses fail; each observation receives an explicit
  post-run disposition; v1 regression suite remains green.
- **User gate:** `ADOPT_FOR_P4_DRY_RUN`, `REVISE`, or `ROLLBACK_TO_V1`.

### A6 — P4 dry-run and cutover decision

- **Entry:** user chose `ADOPT_FOR_P4_DRY_RUN` at A5.
- **IN:** signed A1/P4 firewall and approved v2 harness.
- **OUT:** any P4 canonical/content write, format acceptance, P5+, silent activation.
- **Artifacts:** a P4 StageSpec, resolved profile/adapter set, immutable dry-run ResolvedStage,
  preflight/review/user-gate packets and a comparison against every signed A1/P4 constraint.
- **Acceptance:** dry-run grants no authority beyond A1; every P4 write path and expected artifact is
  represented; P4-specific semantics remain configuration/profile data; `P4-IMPL-v1` remains
  ineffective throughout the node.
- **User gate:**
  - `CUTOVER` — authorize A7 to make v2 the default harness; this still does not authorize P4;
  - `REVISE` — open a harness maintenance stage from recorded observations;
  - `ROLLBACK_TO_V1` — preserve v2 evidence and return to the v1 decision point.
- **Closure:** `CUTOVER` advances only to A7. `REVISE` and `ROLLBACK_TO_V1` stop with their explicit
  pointer reconciliation. This node never executes P4.

### A7 — Default cutover and v1 runtime retirement boundary

- **Entry:** user chose `CUTOVER` at A6; exact v2 candidate and dry-run evidence remain unchanged.
- **IN:** CLI/command default selection, legacy notices and roadmap/LEDGER reconciliation.
- **OUT:** deleting v1 source/tests, converting nonexistent v1 records, P4 implementation, P5+.
- **Actions:**
  1. make the v2 StageSpec flow the default `rs-execute` entry;
  2. retain v1 controller/schema/tests as non-default, read-only rollback/regression evidence;
  3. mark the v1 Stage Record template and generated-v1 view as legacy—not valid for new runs;
  4. run the complete v1 regression and v2 suites from the cutover tree;
  5. reconcile this plan, its historical parent and LEDGER to the separately bounded P4 execution
     entry without activating P4.
- **Acceptance:** new-run entry cannot accidentally select v1; explicit legacy validation remains
  possible; v1 and v2 tests are green; rollback to `c64b9c5...` remains documented; no P4 content is
  touched and `P4-IMPL-v1` remains ineffective.
- **Boundary:** one reviewed `HARNESS-V2-CUTOVER-v1` commit closes this plan.
- **Later retirement:** only after a successful real P4 pilot may a separate harness-maintenance stage
  decide whether to remove v1 runtime/schema/template/test files. That decision is not presumed and
  does not require maintaining v1 as a parallel product.

## 8. Global scope firewall

### IN

- harness architecture, contracts, schemas, controller, profiles/adapters and tests required by A0–A7;
- implementation migration and temporary regression/rollback compatibility for v1 S0–S2;
- generated synthetic records and a non-writing P4 dry-run configuration;
- plan/LEDGER pointer reconciliation needed to prevent an incorrect S3 start.

### OUT

- P4 content or research-object implementation;
- P5–P14 work;
- rewriting signed A1 or closed v1 evidence;
- standalone repository/package publication;
- speculative capabilities not exercised by the five archetypes;
- harness modification inside the business stage that discovered an issue;
- simultaneous writes by execution and node-review sessions.

Any required work outside IN becomes a `SPEC_GAP` or HarnessObservation and stops the current node.

## 9. Current pointer

The metadata tuple at the top of this file is the sole machine-readable live pointer; this section
explains that tuple and must not restate a different value.

`A4 — review, user gates and the operational growth loop / A3_CLOSED_A4_AUTHORIZED`. A0–A2 are
accepted; Contract v2 was signed at the `A2-ADMINISTRATIVE-CLOSEOUT-v1` boundary. The A3 FULL
review returned `CHANGES_REQUIRED` (driving finding A3-F1); the user accepted the finding, the one
bounded fix candidate `a5861fff8ec116addd9db60e3ebc07e0e1e33f20` added the deterministic v1↔v2
canonicalization equivalence lock, and the user's decision (2026-07-19) closed A3 accepting that
fix candidate and explicitly authorized A4. The concise durable dispositions were in
`ResearchSystem/migration/general-harness-v2/nodes/{A1,A2,A3}/NODE.md`, deleted 2026-08-15 with
the rest of the v2 family (`HD-39`); reachable through `git log` on those paths.

A1 revision 1 remains closed `SPEC_GAP`; `180ccb4...` remains an unapproved, superseded historical
candidate and must not execute. The execution session proceeds into A4 under §6/§7 (review/user-
gate/feedback layer over the accepted A3 core, one candidate commit) and stops at the A4 node
review gate. Original S3, P4, A5+ writes and cutover remain forbidden.

## 10. Cold-start prompts

### Execution session

```text
Read AGENTS.md, then .goals/LEDGER.md, then
.goals/plans/general-harness-v2-architecture-revision.plan.md in full.
You are the sole writer. Verify the unique bootstrap-simplification boundary, clean worktree and the
current A1 simplified definition. Do not execute or repair the superseded 180ccb4 rev2 plan and do not
create D1 correction receipts, review packets, lease fields or disposition files. Implement only the
four A1 model artifacts under nodes/A1/revision-2/** and permitted A1 traceability cells. Run
deterministic checks, create one A1 model candidate commit, report its SHA,
base, changed paths, checks and limitations, then stop. Do not self-review, enter A2 or touch P4/S3.
```

### Node-review session

```text
Read AGENTS.md, then .goals/LEDGER.md, then
.goals/plans/general-harness-v2-architecture-revision.plan.md in full and inspect the exact candidate
SHA supplied by the user. You are read-only: do not edit, persist review evidence, commit or advance
the node. Review only the current node payload against its IN/OUT, interfaces, acceptance criteria and
ground truth. Do not require bootstrap ReviewPackage/ReviewResult/UserDisposition files, packet
digests, leases or state versions. Report PASS, CHANGES_REQUIRED or SPEC_GAP with stable finding IDs
and exact file/section evidence; optional improvements cannot block. In VERIFY mode, inspect only
accepted findings, changed cells and permanent scope/interface checks; return PASS or SPEC_GAP.
```
