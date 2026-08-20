# V3-N3 administrative record — two real document shadow runs and the adoption decision

Node: `V3-N3` of [[document-work-assurance-harness-v3.plan|the v3 plan]] §9. Sole writer: the
execution session.

> Path move 2026-07-28 (stabilization plan Phase B): `ResearchSystem/generated/document-assurance/`
> → `ResearchSystem/assurance/`. Four markdown link targets in this record were repointed so the
> artefacts stay reachable; every prose and table mention — including §'s allowlist declarations —
> is left at its N3-time value, so the record still states what was approved then.

**Section roles, declared here because the numbering shifts per node** (N0: §8 log, §9
register; N1: §9 log, §10 register; N2: §8 log, §9 register; this node: §8 log, §9 register):

- **§8 is the append-only log** — entries are added, never rewritten or reordered.
- **§9 is a cumulative register** — rows are appended and may be sharpened; every such change
  is itself logged in §8.
- **§§1–7 record this node's own facts** and are not rewritten once the node closes.

## 1. Authorization and base (plan §9, V3-N3 IN)

- **N2 closed and signed:** the user signed V3-N2 on 2026-07-20, binding candidate `23ac473`;
  the targeted VERIFY returned `PASS`. Budget closed fully spent (FULL 1/1, fix 1/1,
  VERIFY 1/1). See [N2 record §8](../N2/N2-record.md) — including residual **N2-R7**, which
  records that the VERIFY report itself is not in the repository.
- **N3 authorization:** the user authorized V3-N3 on 2026-07-20.
- **Shadow subjects approved by the user on 2026-07-20** — this is a distinct gate, required
  by the node's own IN clause, and it is why N3 could not simply follow N2:

| Leg | Approved subject | Why it qualifies |
|---|---|---|
| multi-file Markdown / design | the **A1 amendment episode**: `contract/amendments/2026-07-18-a1-p4-scoped.md` (726 lines) with `handoffs/P4-reopen-2026-07-17.md`, the park banner on `handoffs/P4-to-P5.md` and the associated pointer edits | real archived document work carrying a real adversarial review history — 6 Codex rounds, 2 user bounded audits, 5 user adjudications, one real signature |
| structured JSON / YAML with schema, lint and semantic review | the **P3 batch**: `inventory/P3-inventory.md`, `inventory/dependency-baseline.md`, `inventory/coverage-manifest.json` validated against `schema/coverage-manifest.schema.json` | structured artifacts with a deterministic schema check and a real user gate ("approve as-is") |

- **Node base:** `655bae5` (`V3-N2-ADMINISTRATIVE-CLOSEOUT-v1`).
- **OUT (not touched by this node):** synthetic-only adoption, any source-code task, external
  effects, P4, default cutover.

### 1.1 Why the whole ResearchSystem P0–P14 workflow is *not* the subject

The user asked whether the 14-step ResearchSystem development workflow could serve directly.
Most of it cannot, and the reason is in the plan rather than in preference: **N3's OUT clause
names "source-code task"**, and V3-D1 places product-stage source-code implementation outside
the v3 product entirely. P2 (the compiler and its ten modules), P5–P8 and P9–P14 are source
code, so assuring them would be measuring v3 against work it does not claim to do.

What *is* in scope is the document-producing part of that same programme, which is what the
approved subjects are: a contract amendment and an inventory/manifest batch. Both are real,
both are archived, and both already carry the review history N3 needs to measure against.

### 1.2 Adjacency, stated rather than left for a later reader

Both approved subjects live under `ResearchSystem/`, and the A1 amendment governs tooling that
sits beside the v3 implementation. This is **not** the self-certification plan §8 forbids —
that ban is on using the unfinished harness to certify **its own construction** (V3-N0..N4),
and neither subject is v3 construction work. The adjacency is recorded because the two are
easy to confuse at a glance, not because it weakens the evidence.

## 2. Change boundary actually used

Derived fresh from plan §9 V3-N3 before any write. This node's allowlist is the narrowest so
far: **"allowed existing files: none outside the approved disposable/shadow subjects."**

| Path | Basis |
|---|---|
| `ResearchSystem/migration/document-work-assurance-v3/N3/**` | allowed new root |
| `ResearchSystem/generated/document-assurance/shadow/**` | allowed new root — every disposable copy and every generated record lives here |

Two consequences, recorded now rather than discovered later:

- **`.goals/LEDGER.md` is excluded at N1–N3** (permitted only at N0 and N4). This record is
  therefore N3's durable ledger, as at N1 and N2.
- **The canonical shadow subjects are read-only.** N3-A8 requires that v1/v2 history,
  production P4 and the canonical pilot sources remain untouched, so every run operates on a
  disposable copy under `generated/document-assurance/shadow/**`. The originals are inputs,
  never targets.

> [!important] Resume pointer — FINAL (the node is closed; this block no longer mutates)
>
> **V3-N3 CLOSED 2026-07-21 — the user ruled `ADOPT_DOCUMENT_V3` at the §8 decision gate**
> (plan §8 gives N3 a decision gate, not a signature). Three shadow rounds complete; the
> round-2 → round-3 comparison with its bundle confound is in §8; residual register runs
> N3-R1 – N3-R10. **Next: V3-N4 upon explicit user authorization** (default pointer +
> C1/C2/C3 prose batch + `.goals/LEDGER.md` sync + tested rollback pointer), then the
> harness-contract discipline edit, then the 特例-bucket design round. The historical
> resume narrative below is preserved as written; read §8 top-down for the authoritative
> sequence of events.
>
> **Goal:** V3-N3, two real document shadow runs then the user's adoption decision.
> **Node base:** `655bae5`. Nothing committed for this node yet; the whole surface is
> uncommitted working tree under the two allowed new roots.
>
> **Landed:** shadow run 1 (A1 amendment episode) — WorkSpec (14 units / 13 obligations),
> resolved plan, 8 deterministic checks **8/8 PASS**, manifest **CONFORMANT** over 8 observed
> changes, record / locator / coverage all clean. Its FULL review is running in an independent
> context.
>
> **Also landed:** shadow run 2 (P3 inventory + Coverage Manifest) — 7 units / 6 obligations /
> **7 checks 7/7 PASS**, manifest CONFORMANT, record / locator / coverage clean. The §4 burden
> measurement is computed. Both runs cold-resume `exit 0`.
>
> **断点 / next step (updated 2026-07-21, revise round):** **the user ruled `REVISE_V3`**, and
> ruled that the revise round is a **derivative of this node** — amend, then re-run N3 — so it
> inherits N3's boundary and `N3-A1`–`A8` rather than needing a bar of its own (§8).
>
> **Round 1 is closed as the before-side** and its evidence is frozen. Its plan of record is
> [`.goals/plans/document-work-assurance-v3-revise.plan.md`](../../../../.goals/plans/document-work-assurance-v3-revise.plan.md),
> an out-of-node file written for session continuity.
>
> **Done:** the amendment (`55133a9`, out-of-node, four V3-N2-authored paths, no signed byte,
> mutation-verified in four probes) and shadow round 2's mechanical layer — both runs rebuilt by
> derivation under `shadow/round-2/**`, 8/8 and 7/7 PASS, both packages frozen and byte-verified.
>
> **Round 2 is complete.** Both FULL reviews ran in independent contexts and validate clean.
> **The deadlock is broken and both branches fired, one each way** — run-a1 returned
> `REVIEWED_NO_BLOCKER` + `INCOMPLETE` + disclosure (the exact combination round 1's harness
> refused), run-a1's reviewer enumerating six unmapped units; run-p3 returned `SPEC_GAP` on the
> stated criterion. Both found materially more than round 1 (6 and 3 unmapped units against 1 and
> 1). Deterministic suites, burden and the binding guard are in §8.
>
> **断点 (updated 2026-07-21, revise amendment 2) — both rulings were taken and executed.**
> The user ruled re-run (round 3) on de-contaminated instructions, plus the further
> review-layer fixes recorded in §8 (floor-not-ceiling, the disposition split, evidence
> discipline, the stop-criterion redraft, the canonical-digest note). Amendment 2 is committed
> out-of-node (`eca4902`, `V3-REVISE-REVIEW-CLARITY-AMENDMENT-v1`); **N3-R9** is registered;
> round 3 is built by derivation, its mechanical layer matches round 2 (8/8, 7/7, CONFORMANT),
> and both packages are frozen pre-review (digests in §8).
>
> **ROUND 3 IS COMPLETE (2026-07-21).** The external checkpoint review passed 4/4 with
> findings (all dispositioned — L1 severe prompt-history leak fixed pre-dispatch, F4/F1/F2
> fixed as amendment 3 `c07d682`); both FULL reviews ran in fresh contexts on the
> amendment-2+3 bundle and validate clean; the binding guard accepted correct / refused
> tampered on both; suites and burden measured figures-last; the round-2 → round-3 comparison
> is in §8 **with the bundle confound stated**. Headlines: run-a1 `REVIEWED_NO_BLOCKER` +
> `INCOMPLETE` + disclosure (1 unit, newly coined); run-p3 **`CHANGES_REQUIRED`** — the
> verdict moved off round-2's `SPEC_GAP` because floor semantics let the reviewer establish
> the dropped unit's work was done, and the count blocker (fourth reproduction) now drives
> the verdict. Committed in-node as `V3-N3-SHADOW-ROUND-3-CANDIDATE-v1` — a commit cannot
> carry its own SHA; find it as the branch tip.
>
> **Then:** the adoption decision (`ADOPT_DOCUMENT_V3` / `REVISE_V3` / `ROLLBACK_TO_V2_HISTORY`)
> is re-taken by the user. Nothing here takes it.
>
> **Round 1's evidence is frozen and must not be modified or deleted** — it is the before-side
> of the comparison, and V3-D9's rule that evidence sets are never mutated applies to this
> node's own output as much as to a run's.
>
> **The START gate was cancelled, deliberately, and that is a measurement not a shortcut.**
> §3 records why: in a replay the deliverable already exists, so asking the user "would you
> have authorized this?" cannot change anything, and run 1's review had already established
> what a real START would have concluded (the WorkSpec widened the boundary and omitted §4's
> locked decisions — a live gate would have returned `REPLAN`). A gate that consumes a user
> decision and produces no signal is exactly the control cost plan §10 asks to be measured, so
> it is counted as one rather than performed as ritual. The user challenged the repeated
> approval requests and was right to.
>
> **Why not `.goals/LEDGER.md`:** it is permitted at N0 and N4 and excluded at N1–N3 (plan §9),
> so writing a pointer there would be an out-of-boundary write. This record is the node ledger,
> as at N1 and N2.

## 3. What a shadow run is here, and what it is not

A shadow run here is a **replay**, not a live parallel run. Both approved subjects are
finished work, so the payload candidate is a real historical commit read through `git show`,
and the base is its parent. Nothing is copied and nothing is mutated — candidate isolation is
supplied by history itself, which is stronger than the disposable copy N3-A8 would have
accepted.

The replay has one honest consequence, recorded before any measurement rests on it: **the
lifecycle's order is inverted.** The product's flow puts the user's START decision before the
executor writes; in a replay the deliverable already exists, so START can only be asked as
*"looking at this WorkSpec, would you have authorized this work?"*. That is a weaker question
than the real gate, and no measurement below may be read as evidence that a live START gate
would have behaved the same way.

## 3.1 What one session driving every role does and does not establish

One session authored the WorkSpec, played the executor, and drove the deterministic verifiers.
The ownership invariants are exercised rather than bypassed — the manifest, the check results
and the fulfillment carry three distinct `authored_by` / `verified_by` values, so the
executor-authored-manifest and executor-authored-result guards actually run. But they compare
declared names, and all three names are this session. Contract §1 settles what that can mean:
role separation is a workflow protocol, not an OS guarantee. The FULL review is the one role
placed in a genuinely separate context.

## 4. Measured burden

Computed by [`shadow/measure.py`](../../../assurance/shadow/measure.py) from
files on disk and from git, so the adoption decision rests on arithmetic rather than
impression. **These figures are re-run immediately before §7 closes; the table below is the
current reading and is not the final claim until then.**

| | A1 leg (Markdown) | P3 leg (JSON/YAML) | total |
|---|---:|---:|---:|
| protected work | 57,259 B | 32,480 B | **89,739 B** |
| **authored control** (WorkSpec + check requests) | 9,090 (16%) | 5,721 (18%) | **14,811 = 17%** |
| generated control | 37,269 (65%) | 31,946 (98%) | 69,215 = 77% |
| all control | | | 84,026 = **94%** |
| obligations | 13 | 6 | 19 |
| deterministic checks | 8 | 7 | 15 |

**How the 94% must and must not be read.** Plan §10's criterion is *measured harness control
effort dominating the protected document work* — **effort**, not bytes. The 77% the harness
generates costs no human effort, and the honest effort figure is the **17% authored**, which
does not dominate. But the 94% is not nothing: it is what the repository stores and what a
later reader navigates past, and on the JSON leg the generated control (31,946 B) very nearly
equals the entire deliverable it describes (32,480 B). Both figures are reported because
quoting either alone misrepresents in a different direction — and the two answer different
questions, which is why the adoption decision cannot be read off a single number.

**Unused mechanisms (N3-A3, plan §9).** None. All **6/6** check kinds were exercised across
the two legs — the JSON leg reached `json_schema` and the `command_exit` governance scan that
the Markdown leg could not. **Zero `DocumentAssuranceProfile` instances and zero repair rounds**
were created: the no-profile and no-repair paths held, and no empty placeholder artifact was
produced, which is exactly what N3-A3 requires.

### 4.1 The review side's witnessed-case question, answered

An uncommitted review-side note at the migration root
([`v3-review-note-obligation-authoring.md`](../v3-review-note-obligation-authoring.md)) put one
concrete question to this node, on the grounds that a real occurrence is the evidence that
would justify amending a signed schema and no occurrence is the evidence that it should not be
built:

> What fraction of this run's obligations are `review_only`, and how many of those could a
> script have verified?

**Measured: 12 of 19 obligations (63%) are `review_only`; 0 are `local_check` alone; 7 are
`local_check_and_review`.**

Of the 12, at least four could have been verified by a script with no judgement involved:

| obligation | run | what a script could have done |
|---|---|---|
| `ob-scan` | P3 | count `.md` per declared root and compare to the stated totals — **exactly the check that would have caught the blocker** |
| `ob-ref-kinds` | A1 | enumerate the Ref kinds used in the five blocks; compare to the frozen list. A set comparison |
| `ob-propositions` | A1 | string-equality of the canonical proposition against its owner file — the reviewer did precisely this by hand, character for character |
| `ob-coverage-field` | A1 | the field is present with a closed shape, or absent. A presence test |

**The note predicted the incentive gradient; the node witnessed its consequence.** The single
real defect this node found — `P3-inventory.md`'s 110-vs-51 count — sat inside an obligation
declared `review_only` that a five-line script could have falsified instantly. It was declared
`review_only` by me, for the reason the note names: `review_only` costs no `LocalCheckSpec`, no
binding, and no separately-authored `CheckResult`. It was then caught only because a reviewer
spent roughly 60% of their effort counting files by hand.

This is a witnessed case, not a hypothesis. It does not by itself justify amending an N0-signed
schema — that remains a user decision at §4's disposition — but the evidence the note asked for
now exists, and it points the same way from both runs.

### 4.2 `N3-A5` — what was actually put in front of the user

Recorded late, on user challenge (2026-07-21). The observation existed from run 1 and this
record failed to make it, which is why A5 was twice mis-reported as untested.

**A5 asks what the user is asked to approve**, and that is determined by the START decision
surface, which is generated from the WorkSpec — so its *shape does not depend on whether the
work is finished*, and a replay observes it as well as a live run would.

What run 1 actually put in front of the user at START:

| On the surface | Not on the surface |
|---|---|
| the objective, one line | the resolved plan and its digests |
| the frozen instruction ref | the `AssuranceWorkState` |
| **13 obligations**, one sentence each | the eight check requests |
| **1 non-normative unit + its rationale** | any manifest, coverage join or pointer set |
| the change boundary | the schema-pack digest |
| the one expected artifact | |

**The first half of A5 holds, and holds strongly.** Measured control volume was 94% of the
protected work (§4) — but **none of that generated bulk reached the decision surface.** What
reached it was thirteen obligations and one declared exception. Volume and decision surface are
different quantities, and conflating them would have been the easiest wrong conclusion to draw
from §4's headline figure.

**The second half is a permanent boundary, not a gap.** Whether a human *engages* with that
surface when it genuinely matters cannot be established by a shadow run of any kind: in a replay
the outcome is already known, and in a live run the user knows they are being measured. The
first real use is its own observation. Registered as N3-R5(ii).

### 4.3 Cold resume (N1-A10, exercised on real shadow state)

Both runs resume `exit 0`. It failed first, and the failure was mine: pointers were written
run-relative while `relPath` specifies repository-relative, and `resume` correctly refused to
resolve them. Recorded because a guard that refuses a malformed pointer is the feature working,
and it would have been easy to misreport as a product defect.

## 5. Deliberate non-implementations

| Not done | Why not |
|---|---|
| the START gate, twice | §3: a replay cannot make it a real decision, and run 1's review had already established what a live gate would have concluded. Counted as a control cost rather than performed as ritual |
| any repair round or VERIFY | Run 2 returned `CHANGES_REQUIRED`, so a repair was *available*. It was not taken: repairing would mean editing `P3-inventory.md`, which N3-A8 forbids and which no v3 node's allowlist reaches. The finding is carried as N3-R3 instead |
| fixing N3-R1, N3-R2 or the unused freeze surface | N3 owns no module. A measurement node that quietly patches the thing it is measuring has destroyed its own evidence |
| a `DocumentAssuranceProfile` proposal (N3-A7) | The threshold is a rule witnessed in **both** real instances. The only candidate — "an obligation map drops normative units" — is a defect pattern, not a reusable assurance rule, and one witness pair does not make it one |

## 6. Honesty boundaries of what this node measured

- **A replay is not a live run.** The order is inverted (§3), the outcome is known in advance,
  and no measurement here establishes how the harness behaves when the work does not yet
  exist. Every number below is about assuring *finished* work.
- **One session drove every role except review** (§3.1). The ownership guards ran against three
  distinct declared names, all of which were this session.
- **Two subjects is the plan's minimum, and they are adjacent.** Both come from the same
  programme in the same repository, authored by the same user under the same conventions. That
  the harness behaved consistently across them is weaker evidence than two unrelated
  workflows would have given.
- **The effort figures are bytes and counts, not clock time.** Reviewer-reported effort (~35
  minutes for run 2; ~12 tool calls for run 1) is self-reported and carries no evidence lock.
- **The strongest result is a single defect.** One real error found in one of two subjects is
  evidence that the discipline can find real errors — not a rate, not a guarantee, and not a
  basis for claiming the harness would have caught it prospectively.
- **Two reviewers agreeing is not proof.** They were given the same role instructions
  (`REVIEW.md`) and the same shaped evidence, so their convergence may partly reflect a shared
  prompt rather than an independent read of the product.

## 7. Deterministic results

Measured in one pass immediately before this section was written, after the last change to
what they measure.

| Check | Result | Observed tree |
|---|---|---|
| shadow run 1 — deterministic checks | **8/8 PASS** | candidate commit `5ca6cc1` |
| shadow run 1 — record / locators / coverage | clean | candidate commit |
| shadow run 2 — deterministic checks | **7/7 PASS** | candidate `244e057`; `chk-governance` honestly declares the **worktree** |
| shadow run 2 — record / locators / coverage | clean | candidate commit |
| cold resume, both runs (`rsc v3 status`) | **exit 0, resumable** | worktree |
| V3-N2 acceptance matrix | 198 OK | worktree |
| V3-N1 acceptance matrix | 113 OK | worktree |
| `repo-audit.py` | exit 0 | worktree |

The N1 and N2 suites are unchanged and are re-run only to show this node broke nothing: **N3
owns no module and modified none.**

**Changed-path set** — `git diff --name-only 655bae5` plus untracked: **36 paths**, every one
under `ResearchSystem/generated/document-assurance/shadow/**` (35) or
`ResearchSystem/migration/document-work-assurance-v3/N3/**` (1), which are exactly the two
roots plan §9 allows. **Zero out-of-boundary.** The 37th path is the pre-existing untracked
`ResearchSystem/docs/General-Harness-v2-Design.md`, which is not part of this node.

**N3-A8 held in the strongest available form:** not one canonical pilot source, v1/v2 asset or
P4 artifact was written. The payload candidates were real historical commits read through
`git show`, so the runs could not have mutated them even by mistake.

## 8. Append-only log

- 2026-07-20 — node opened. The user authorized V3-N3 and, in a separate and separately
  required act, approved the two exact shadow subjects (§1). Boundary re-derived from plan §9
  before any write (§2); the two exclusions were found at that point rather than later.
- 2026-07-20 — **shadow run 1 built and its evidence layer run.** WorkSpec
  `shadow-a1-amendment`: 14 instruction units (13 obligation, 1 context with a rationale), 13
  obligations, 8 deterministic checks. The obligation spine was **not invented for the
  shadow** — it is the instruction's own §5 (eight OPEN items the amendment "MUST settle") and
  §6 (five method-contract requirements), and the boundary and expected artifact are lifted
  from the instruction's own §9 Scope Firewall.

  Results: **8/8 checks PASS**; manifest **CONFORMANT** across 8 observed changes;
  `check_record`, `check_locators` and `coverage_report` all clean.

  **Four observations the run produced about the harness, three of them against its author.**
  They are recorded now, while they are fresh, rather than reconstructed at §4:
  - **the guard caught a guessed locator three times, every time correctly.** A guessed
    heading (`## 3. The five object blocks`) returned `FAIL`; then eight guessed `### §1.x`
    subsection anchors returned eight `V3-CANDIDATE-LOCATOR-UNRESOLVED`. The real answer was
    that the eight OPEN items were answered in a **table**, one row each. The locator rule
    forced the deliverable to actually be read rather than assumed — which is precisely the
    "a claim is not evidence" property, demonstrated against the person making the claim;
  - **the schema refused a mis-authored WorkSpec**: binding a deterministic check to a
    `review_only` obligation was rejected. "The amendment decided the enum conflict" is not
    something a file-existence check can speak to, and binding one would have dressed a
    semantic obligation in deterministic evidence;
  - **the instruction had already hand-authored a proto-WorkSpec.** Its §9 carries one
    objective, a write allowlist, an OUT list, an expected artifact and an acceptance/stop
    gate. The structure v3 asks for was largely already there, which is a *cost* datum: for
    this workflow the authoring burden is low because the work was already being done by hand;
  - **the deliverable already back-referenced its obligations.** The amendment's §2–§6 are
    each titled with the instruction obligation they answer (`(handoff §6.1)` … `(§6.5)`), so
    instruction-to-obligation traceability existed before v3 was applied.
- 2026-07-20 — two small friction points worth keeping, neither a defect in the product's
  claims: `--emit` does not clean its control directory, so a check request from an earlier
  resolution survived and was run against the new candidate until it was removed by hand; and
  `checks.run_check` raises `AttributeError` rather than reporting when handed a list instead
  of a mapping — the crash-instead-of-report class, this time in an N1 module and therefore
  outside this node's boundary to fix.

- 2026-07-20 — **shadow run 1's FULL review returned `REVIEWED_NO_BLOCKER` with
  `instruction_completeness: INCOMPLETE`, and the harness refused that combination.**
  `check_review_result` fired `V3-REVIEW-INCOMPLETE-CONTRADICTS-VERDICT`. This is the most
  useful thing the node has produced, because product and reviewer disagree on substance and
  neither is obviously wrong:

  - **the reviewer's position:** the WorkSpec's map is incomplete — it carries the
    instruction's §5 and §6 but not §4's **31 locked decisions**, which bind the deliverable's
    content and are dispositionable by no obligation, so `ob-constraint-table` would read
    `SUPPORTED` even if the table carried wrong bounds. The reviewer checked that conformance
    by hand and it held. Hence *"INCOMPLETE describes the map, not the artifact"*, and the
    artifact carried no blocker;
  - **the guard's position** (authored at V3-N2): an unmapped normative unit is a blocking
    discrepancy, not a residual, because the product's own primary assurance statement is that
    *every declared instruction unit is mapped to an obligation or an explicit `SPEC_GAP`*
    (plan §1). If the map missed normative units, that statement is false for this run
    regardless of how good the artifact is.

  **Both are right about different objects, and the harness offers no verdict that says so.**
  The honest disposition is arguably `SPEC_GAP` — V3-D7 already routes an incomplete map to
  "a new WorkSpec revision and a new user START decision", which is exactly what a missing
  obligation needs and is something no repair to the candidate could fix. But nothing tells
  the reviewer that: `REVIEW.md` does not say an `INCOMPLETE` recheck should return
  `SPEC_GAP`, and the guard only says *not* `REVIEWED_NO_BLOCKER` without saying which of the
  two remaining verdicts applies.

  **Not fixed here.** N3's allowlist contains no module, and N3 is a measurement node — a
  product change belongs to a later node or to a `REVISE_V3` decision. Registered as N3-R1.

- 2026-07-20 — **the reviewer's adoption feedback, recorded verbatim in substance because it
  is evidence for the §4 decision and it is not flattering.** Asked bluntly whether the
  harness helped:
  - **the obligation ratchet earned its place.** Being forced to disposition all 13 exactly
    once "stopped me from reviewing the interesting parts and hand-waving the boring ones",
    and the reviewer would not have self-imposed it;
  - **the deterministic layer did almost nothing.** Five PASS results establishing that
    sections exist, on a deliverable whose whole question is whether those sections *settle*
    anything. The reviewer's warning is sharper than the observation: *"a reader who saw 'all
    checks PASS' would over-trust it"*;
  - **`coverage.json` was pure restatement**, read only because the task demanded it;
  - **the fulfillment locators had mild negative value** — they point at the table row where
    the executor *claims* the item was settled rather than at the settlement, so following
    them "would have led me to a summary of the work rather than the work". The reviewer
    ignored them and navigated by section;
  - **the placeholder `package_ref` is worse than an absent one**: 64 zeros "looks bound and
    isn't". No frozen ReviewPackage file was produced by this run at all;
  - **the boundary check answered a looser question than the instruction asked** — the
    instruction's §9 pre-signature allowlist is *one file*; the WorkSpec widened it to three
    directories, so `CONFORMANT` is a weaker statement than it appears. That is a defect in
    this run's authoring, by me, not in the product;
  - **the one required step that felt like busywork and then justified itself** was rechecking
    completeness against the *raw instruction* rather than the map — it produced the §4 gap
    above.

  Structural conclusion the reviewer offered for the adoption decision, recorded because it
  is the sharpest framing available: on a document-shaped deliverable the deterministic layer
  is doing almost nothing while the *procedural* layer — obligation ratchet, raw-instruction
  recheck, mandatory `residual_uncertainty`, `UNVERIFIABLE` as a first-class answer — is doing
  most of the work.

- 2026-07-21 — **shadow run 2's FULL review returned `CHANGES_REQUIRED` with one blocking
  finding, and the blocker is a real defect in real committed work.** Independently
  reproduced before being recorded, because it is a claim about the repository rather than
  about the harness:

  `P3-inventory.md`'s frozen baseline states *"total in-scope Markdown files: 220 (Thesis 54 ·
  ExperimentLab 110 · Paper 39 · Knowledge 17)"*. At base `90deba7` ExperimentLab holds **51**
  Markdown files, not 110. Verified: Thesis 54 ✓, Paper 39 ✓, Knowledge 17 ✓ — the defect is
  isolated to one root. **110 is exactly ExperimentLab's tracked files minus `.py` and
  `.eval`** (235 tracked), a population including `.json`, `.yaml`, `.png` and `Dockerfile`,
  while `content-roots.yaml` declares that root as `formats: [md]`. The true declared-format
  total is **161**. It propagates: §4's `Coverage check: 54 + 39 + 17 + 110 = 220 ✔` is the
  document's *only* evidence for its "100% of scoped eligible units are accounted for"
  acceptance property.

  **This is the strongest single result the node produced** — the harness, applied to real
  archived work, surfaced a factual error that had already passed a user gate. It is recorded
  as a residual against the P3 inventory (N3-R3), not fixed here: N3's allowlist reaches
  neither `ResearchSystem/inventory/**` nor any canonical source, and N3-A8 requires the pilot
  sources stay untouched.

  **Attribution, stated precisely because it decides what adoption would buy.** The harness did
  not find this. The reviewer found it by counting files — *"60% [of my effort] was
  independently reproducing the counts … that is the work the harness did not do for me"*.
  What the harness contributed was the `per_obligation_disposition` grid that forced the
  reviewer to walk the instruction's nine-item freeze list one at a time, which is how
  `ob-freeze` came to be examined at all and how a second omission ("unparseable cases" — no
  such row exists anywhere) surfaced.

- 2026-07-21 — **both runs returned `instruction_completeness: INCOMPLETE`, independently.**
  Run 1's map omitted the instruction's §4 locked decisions; run 2's folded a five-assertion
  Acceptance paragraph into one unit and enumerated four, dropping *"second inventory run
  produces no diff"* — an obligation that consequently exists nowhere. Two different
  reviewers, two different subjects, the same failure mode: **a hand-authored obligation map
  silently drops normative units, and only the recheck against the raw instruction catches
  it.** N3-R1 is therefore not a one-off disagreement about one review; the verdict collision
  it describes will recur on every run whose map is imperfect, which on this evidence is every
  run.

- 2026-07-21 — **the two reviewers, in separate contexts and without sight of each other,
  reached the same verdict about the product's own layers.** Recorded verbatim in substance
  because converging independent judgment is the strongest evidence this node can produce:
  - **the deterministic check layer contributed nothing to either verdict.** Run 1: five PASS
    results establishing that sections exist. Run 2, which had the "real" checks: *"Not one of
    them touched the thing that was actually wrong. The defect was a factual count inside a
    Markdown table, and the only way to it was to go count the files."*
  - **`json_schema` on a hand-authored manifest is shape, not truth.** The PASS establishes
    the file has the right keys; `claim_ref` is an unpatterned string, `approved_by` any
    non-empty string. *"A reader who sees 'schema check PASS' next to 'user-approved manifest'
    will over-trust it."* Having a real schema check on the JSON leg *"changed the answer not
    at all"*.
  - **`chk-governance` was worse than neutral.** Its `observed_tree` is the worktree at a
    commit far downstream of the candidate, and its subject digests diverge from the candidate
    blobs — a CRLF checkout artifact. The reviewer spent real time chasing it for zero
    information.
  - **three checks were unbound extras** (`chk-boundary`, `chk-links`, `chk-governance`),
    present in neither the resolved plan's `check_order` nor any obligation's
    `local_check_refs`. My authoring, and a gap the harness does not flag.
  - **what both would pay for:** the obligation grid (*"reviewing freehand I would have written
    'looks solid, two nits'"*), the raw-instruction recheck (*"left to my own devices I would
    have reviewed against the WorkSpec, because it was the tidy artifact in front of me"*), and
    `UNVERIFIABLE` as a first-class answer (*"the difference between a review and a rubber
    stamp"*).

- 2026-07-21 — **neither run produced a `ReviewPackage` at all.** Both reviewers filled
  `package_ref` with 64 zeros and disclosed it; run 2 noted that the centrepiece guard of the
  role instructions — refusing a package whose digest diverged — *"could not be exercised
  because there was no package to refuse"*. The V3-N2 freeze/binding surface
  (`freeze_package`, `check_package`, `verify_member_bytes`) went entirely unused by two real
  runs. Read together with residual **N2-R6** (8 of 14 checkers had no caller), this is the
  same signal from the other end: the built surface is wider than the exercised surface.

- 2026-07-21 — **ERRATA, on user challenge. Two of the four "problems" this record reported
  were the orchestrator's failures reported as product findings, and the framing of a third was
  too soft. The entries of 2026-07-21 above stand as written; read them through this one.**

  The user's objection was exact: *are these tools something an agent gets to choose to
  invoke?* They are not, and treating their absence as a verdict on their worth would have
  biased the adoption decision against layers that had never been switched on.

  **(1) "the deterministic check layer contributed nothing to either verdict" — measured
  against the wrong standard.** The check layer is a **floor**: its job is to guarantee a
  minimum below which no run can fall, not to find the interesting defect. Judging a backstop
  by "did it catch the headline bug" is a category error, and both reviewers' feedback — which
  I relayed approvingly — answers a question the layer does not exist to answer. What the
  evidence actually supports is narrower: *the checks that were requested in these two runs
  were weak, and I chose them.*

  **(2) "neither run produced a `ReviewPackage`, so the V3-N2 freeze/binding surface went
  entirely unexercised" — that was my failure to invoke it, not a property of the product.**
  I never called `freeze_package`, then let both reviewers fill `package_ref` with 64 zeros.
  The mechanism whose entire purpose is to bind review evidence to its exact subject was
  skipped by the orchestrator and then reported as unused surface.

  **Corrected by running it rather than by re-describing it**
  ([`freeze_packages.py`](../../../assurance/shadow/freeze_packages.py)).
  Result — the layer earned its place within seconds of being switched on:

  | probe | result |
  |---|---|
  | packages frozen | 16 members each, both runs |
  | `verify_member_bytes` (digest recomputed against the tree each member pins) | **clean, 32/32 members** |
  | binding guard, correct package | accepted |
  | **binding guard, one member dropped** | **REFUSED — `V3-REVIEW-PACKAGE-BINDING-MISMATCH`** |
  | `check_package` against the run's own spec and record | **caught two defects of mine immediately** |

  The two it caught: **`V3-PACKAGE-INSTRUCTION-SUBSTITUTED`** on run-p3 — I had frozen the
  instruction at the *candidate* revision while the WorkSpec pins it at *base*, a real
  substitution, now fixed; and **`V3-PACKAGE-CHECKS-OMITTED`** on both runs — the run produced
  8 (and 7) CheckResults while the package includes 1, because my evidence layout batches every
  result into a single file where the package model expects one member per result so a reviewer
  can address each individually. **That second one is left standing rather than hacked around:
  it is a genuine finding about evidence layout, and it is exactly the membership
  incompleteness `check_package` exists to detect.**

  So the honest statement is the reverse of what this record first said: **the freeze/binding
  layer was never tested, and the moment it was, it found two real defects in the orchestration
  around it and refused a tampered subject.** Residual N2-R6 (8 of 14 checkers with no caller)
  should be read the same way — as a statement about what was invoked, not about what is worth
  having.

  **(3) The count defect was under-stated as "the harness didn't find it".** The user's framing
  is sharper and correct: **that is the design failure.** `ob-scan` was mechanisable in five
  lines — count Markdown per declared root, compare to the stated total — and I declared it
  `review_only` because that declaration costs no `LocalCheckSpec`, no binding and no
  separately-authored `CheckResult`. This is not a separate problem from §4.1's 63% finding;
  **it is the same defect, and reporting them as two softened both.** The floor was available,
  I declined to lay it, and a human then spent 60% of a review recovering what the floor would
  have caught for free.

- 2026-07-21 — **`N3-A5` corrected twice in one exchange, both times because the user pushed
  back, and the second correction removed a whole round of work.**

  `/preclear` first reported five acceptance IDs unaddressed and claimed the node was *"not
  closeable without an acceptance matrix"*. The user's reply — *N3 本来也没有验收吧* — was
  right: plan §8 gives N3 a **decision** gate, not a signature, and a `REVISE_V3` ruling makes
  round 1's evidence not the adoption basis anyway. Over-stated, corrected.

  The row was then rewritten to say A5 is *structurally untestable in a replay*, and that
  round 2 would need a **live** run on undone work to reach it. The user proposed a subject
  (the P6 amendment) and raised two constraints — run it in a **worktree**, and note that
  P0–P4 already carries heavy revision churn that pulling P6 forward would worsen. Both are
  right, and the worktree point is simply V3-D3's own design: payload writing happens on an
  isolated branch and promotion is a separate explicit act after FINAL.

  **But answering the user's question — *has START never been tested?* — collapsed the premise.**
  N1-A4 already tests the START **mechanism** (12 assertions: correct binding passes, a second
  approval path is refused, an undisposed unit blocks START). What is untested is the START
  **purpose**, which is A5. And A5's first half — *what the decision surface contains* — is a
  property of the WorkSpec's shape, independent of whether the work is finished. **Run 1 had
  already produced that observation and this record simply failed to write it down** (§4.2).

  So the live run was not needed, and recommending it would have pulled real work into an
  already-churning area to buy an observation that (a) half existed and (b) half cannot be
  bought at all, since a user who knows they are being measured is not the thing A5 asks about.
  **P6 stays where it is.** Round 2 continues as a replay.

  Worth keeping as method: two of this session's largest proposed pieces of work were removed by
  the user asking a plain question about a term I had been using — first *what is 重放*, then
  *has START never been tested*. Neither was a challenge to a conclusion; both were requests to
  explain a premise, and the premise did not survive being explained.

- 2026-07-21 — **the user ruled `REVISE_V3`, and ruled how the revise round is shaped: it is a
  derivative of this node — amend, then re-run N3.**

  That second half settled a question the plan does not answer. Plan §9 defines five nodes and
  V3-N4's entry condition is `ADOPT_DOCUMENT_V3`, so **`REVISE_V3` has no node**: no allowlist,
  no acceptance IDs, no gate. The session raised this as a defect before writing anything,
  proposing to state a bar for the round explicitly. The user's framing removed that work: as an
  N3 derivative the round **inherits N3's boundary and `N3-A1`–`A8`**, and nothing needed
  inventing. Recorded because a later reader will ask the same question and should find it
  answered rather than re-open it.

  Structurally the round is two halves with different standing, and they are kept in separate
  commits so the changed-path classification of each is uniform:

  | half | boundary |
  |---|---|
  | the amendment to the review layer | **out-of-node**, on the `8efe3e9` pattern, user-authorized |
  | shadow round 2 | **in-node** — `N3/**` and `generated/document-assurance/shadow/**`, N3's own two roots |

- 2026-07-21 — **the amendment: `55133a9` `V3-REVISE-REVIEW-DISCLOSURE-AMENDMENT-v1`.** Four
  paths — `review.schema.json`, `rsclib/document_harness/review.py`,
  `document-harness/REVIEW.md`, `tests/document_harness_review/test_package_and_review.py`.

  **No signed byte touched, and this was verified rather than accepted.** The revise plan
  asserted all three landing sites were V3-N2-authored; that claim was re-derived with
  `git log --diff-filter=A`, which put all four at `0ba649c`
  (`V3-N2-REVIEW-REPAIR-DISPOSITION-CANDIDATE-v1`). The two permanently immutable blobs were
  re-hashed at the working tree and are unchanged: plan `8ad404b1…`, contract `b2dbdf75…`.

  **What changed and why.** `V3-REVIEW-INCOMPLETE-CONTRADICTS-VERDICT` asserted that an unmapped
  normative unit *is* a blocking discrepancy. **Contract §5 does not say that** — it defines
  `REVIEWED_NO_BLOCKER` as scope-relative, *"no blocking discrepancy found within the frozen
  subjects and review dimensions"* — so an incomplete map means the dimensions were narrower and
  the verdict stays true as defined, provided the narrowness is disclosed. The V3-N2 guard
  over-read the contract, and a guard that refuses the only honest verdict while naming no
  replacement is a deadlock rather than a check. No fourth verdict is needed and V3-D6 is intact:
  the existing `residual_uncertainty` → `ACCEPT_WITH_LIMITATIONS` route is exactly this case.

  The requirement therefore moved from the verdict to the disclosure, and is **unconditional**
  rather than keyed on `REVIEWED_NO_BLOCKER` — run-p3 returned `CHANGES_REQUIRED` and had *also*
  dropped a normative unit, which the old shape would never have made it say. `INCOMPLETE` now
  requires `unmapped_unit_ids` enumerated (schema), plus a finding **and** a
  `residual_uncertainty` entry each naming one of those ids (`V3-REVIEW-INCOMPLETE-UNDISCLOSED`).
  Both halves, because they do different work: the finding enters the review record, the residual
  is what reaches the deciding user at FINAL.

  **Two ceilings written into the artifacts rather than left implicit:**
  - the guard matches an id as a **substring**. It establishes the omission is *traceable* from
    the result, not that it was *explained*; a reviewer determined to satisfy it cheaply can. The
    module says so at the guard;
  - `REVIEW.md`'s collision rule — a real candidate blocker *and* a stopping-kind gap resolves to
    `SPEC_GAP`, because a bounded repair cannot create an obligation — is **labelled in the file
    as that document's rule, not a derivation**. V3-D6 and V3-D7 do not settle the collision.

  **Mutation-verified in four probes** against byte-checked scratchpad copies (never
  `git checkout --`; this repo has an incident): dropping the residual half reddened the
  finding-only subtest; replacing the name test with a truthiness test reddened the naming test;
  disabling the guard reddened six assertions including the code-reachability sweep; relaxing the
  schema's `required` list reddened the enumeration test. Both files restored and re-digested
  identical to their controls (`review.py` `e2645f0d…`, `review.schema.json` `e4d2ae5e…`).

- 2026-07-21 — **shadow round 2 built by derivation, not by re-authoring.** Round 2 answers one
  question — with the review layer amended, do the same two runs behave differently? — which is
  only answerable if round 2 differs from round 1 in the review layer **alone**. So the run
  scripts are generated by
  [`round-2/build_round2.py`](../../../assurance/shadow/round-2/build_round2.py)
  from round 1's, through a substitution table of three kinds and no fourth: the control root
  moves under `round-2/`, `parents[N]` gains a level, and the run ids gain `-r2` (V3-D9 forbids
  two evidence sets sharing an identity; `work_id` deliberately does not change — same work,
  assured twice). A hand-edited copy could not have been checked; this can, and any drift not in
  the table is visible rather than trusted. The script asserts round 1 is unmutated and it is
  (37 files, 0 changed).

  **The round-1 WorkSpecs are deliberately NOT repaired.** Fixing the maps would return
  `COMPLETE`, the new disclosure path would never fire, and round 2 would measure nothing. The
  imperfect maps *are* the test subject.

  **A real ordering defect in round 1's orchestration, found by running it.**
  `freeze_packages.py` freezes the package and then immediately exercises the binding guard
  against an existing `review-full.json` — so it can only run **after** the review. That is
  backwards, and it is the mechanical reason round 1 shipped no package at all and both reviewers
  filled `package_ref` with 64 zeros: a package frozen after a review cannot be what that review
  was bound to. The errata at `00963e4` correctly identified that the orchestrator never invoked
  the layer; this is the next layer down — *the script's own shape made invoking it in the right
  order awkward.* Round 2 splits the halves (`freeze_only.py` before the reviews, then
  `freeze_packages.py` after) and both reviewers received a real frozen package with a real
  digest to bind.

  **Round-2 mechanical results**, all matching round 1 as expected since the amendment touches
  only the review layer: run-a1 **8/8 PASS**, manifest CONFORMANT over 8 observed changes; run-p3
  **7/7 PASS**, CONFORMANT over 7; record / locators / coverage clean on both. Packages frozen at
  **16 members each**, `verify_member_bytes` **clean 32/32**.
  `V3-PACKAGE-INSTRUCTION-SUBSTITUTED` **did not recur** — the errata's fix carried.
  `V3-PACKAGE-CHECKS-OMITTED` **did**, on both runs, and is again left standing rather than
  worked around: it is residual **N3-R4**, a genuine finding about evidence layout, and it is
  exactly the membership incompleteness `check_package` exists to detect.

- 2026-07-21 — **round 2's two FULL reviews, in independent contexts. The deadlock is broken, and
  both branches of the new criterion fired — one each way.** Both results validate
  `check_review_result : clean`, both bound a real frozen package digest.

  | | round 1 | round 2 |
  |---|---|---|
  | run-a1 verdict | `REVIEWED_NO_BLOCKER` + `INCOMPLETE` → **harness REFUSED the combination** | `REVIEWED_NO_BLOCKER` + `INCOMPLETE` + disclosure → **accepted, clean** |
  | run-a1 unmapped units found | 1 (the instruction's §4) | **6**, ids coined by the reviewer |
  | run-p3 verdict | `CHANGES_REQUIRED`; the map gap surfaced but routed nowhere | **`SPEC_GAP`** — the stop route, chosen on the criterion |
  | run-p3 unmapped units found | 1 | **3** |
  | `package_ref` | 64 zeros, both runs — no package existed | real digests, bound and verified |
  | binding guard | never exercised | **accepted correct / REFUSED tampered, both runs** |

  **The thing round 1 could not do, round 2 did.** run-a1's reviewer reached exactly the verdict
  the old guard rejected, and it is now a legal, disclosed result carrying six enumerated unmapped
  units, a map-level finding with a WorkSpec-revision minimum fix, and nine residuals. run-p3's
  reviewer took the other branch and stopped. Neither was told which to take.

  **Both reviewers found materially more than round 1 did** — 6 and 3 unmapped units against 1
  and 1. The disclosure requirement plus a stated criterion made them look harder at the raw
  instruction, which is the one behaviour both round-1 reviewers said they would not have
  self-imposed.

  **run-p3's blocker independently reproduced for a third time.** `P3-inventory.md`'s
  ExperimentLab count, re-derived at base `90deba7`: 51, not 110. This reviewer went further than
  round 1 — it showed 110 matches *no* basis (235 files of all types), and found two more
  arithmetic failures in the same table (`smoke-01/** (55)` against 11 actual files; an
  out-of-scope estimate exceeding the root's whole `.md` population). **N3-R3 stands and is
  sharper.**

- 2026-07-21 — **the round-2 evidence is contaminated, by me, and the reviewer caught it.**
  Recorded first among the findings because it bounds everything above.

  `REVIEW.md`'s two worked examples were drawn from round 1's two witnessed cases — **which are
  the two subjects round 2 reviews.** The stop example states run-p3's answer verbatim (a
  five-assertion acceptance paragraph enumerated as four, dropping the second-run assertion); the
  disclose example states run-a1's (§4's 31 locked decisions, verified by hand). run-p3's reviewer
  identified this unprompted and put it in `residual_uncertainty` rather than quietly benefiting:

  > *"Whatever independence this round has on that point is not established by my having reached
  > it … If the harness wants uncontaminated evidence about whether reviewers find map gaps, that
  > example must be replaced with one drawn from a different subject."*

  **What this does and does not invalidate.** The amendment itself is untouched — the guard, the
  schema and the disclosure requirement are mutation-verified and subject-independent. What is
  weakened is precisely what round 2 existed to measure: *whether a reviewer, given the new
  instructions, independently finds a map gap and routes it correctly.* Partial independence
  survives — run-a1 found six units where the example names one and hand-checked all 31 decisions
  rather than taking the example's word, and run-p3 found three where the example names one, plus
  the blocker by counting files. But the headline routing decision on the example unit is not
  clean evidence. Registered as **N3-R6**.

- 2026-07-21 — **round 2 found three defects in the amendment itself, two of them independently
  by both reviewers. The repair needed repair, which is the harness working on its own output.**

  1. **`REVIEW.md` never says whether the frozen package is a *ceiling* on evidence or a *floor*.**
     Both reviewers hit this, and **they resolved it in opposite directions, which changed a
     verdict.** run-a1's probed outside the package (anchors, paths, byte-identity of a quoted
     paragraph) and disclosed the probe as not-frozen-evidence, noting that a reviewer following
     the file literally *"would have returned several avoidable `UNVERIFIABLE`s"*. run-p3's
     declined to read `P3-to-P4.md` though `git show` would have reached it, on the reading that
     rescuing an unmapped unit with out-of-package material is doing the executor's evidence work
     — and states that choice *"materially affected my verdict"*. One instruction, two defensible
     readings, different outcomes: that is a specification gap, not reviewer variance.
  2. **The stopping criterion collides with the file's own process-claims ceiling.** *"Nothing in
     the frozen package can settle whether it was"*, read literally, makes every process
     instruction (a read order, a review-record requirement) a `SPEC_GAP` — contradicting the same
     file's *"process claims have no evidence lock"*. run-a1's reviewer resolved it against
     `SPEC_GAP` and recorded that it had to. **My wording, and it is wrong as written.**
  3. **`package_ref` is a canonical-JSON digest, not the file's bytes**, and nothing says so. run-p3's
     reviewer computed `sha256sum review-package.json` → `0e203582…` against the real
     `6c15f559…` and notes that a reviewer deriving it themselves *"would have concluded the
     package was corrupt"*. The prompt happened to supply the right value; the product does not.

  Registered as **N3-R7** (1 and 2) and **N3-R8** (3).

- 2026-07-21 — **a bound on run-a1 that round 1 never stated.** run-a1's reviewer established that
  the raw instruction **does not exist at base `b626cb5`** — the manifest records it `added`, so it
  was authored by the very commit under review — and that its §9 embeds the candidate artifact's
  own signed SHA (`2D672D0D…`, byte-equal to the frozen `candidate_artifact` digest). The
  completeness recheck is therefore **partly self-referential**: text authorising this commit's
  change set travelled inside the commit it authorises. Round 1's build script noted the instruction
  was pinned at the candidate and called it a measurement; it did not notice the self-reference.
  Contract §8 step 1 expects the instruction frozen before execution. This is not a defect in the
  amendment and not one in the candidate — it bounds what run-a1 can establish, and it is the kind
  of thing only a reviewer reading the manifest against the tree would find.

- 2026-07-21 — **deterministic results and burden, measured in one pass immediately before this
  entry and after the last change to what they measure.**

  | Check | Result |
  |---|---|
  | round-2 run-a1 / run-p3 deterministic checks | **8/8** and **7/7 PASS**, manifests CONFORMANT |
  | record / locators / coverage, both runs | clean |
  | packages frozen · `verify_member_bytes` | 16 members each · **clean 32/32** |
  | binding guard, correct package / one member dropped | **accepted / REFUSED `V3-REVIEW-PACKAGE-BINDING-MISMATCH`** |
  | cold resume, both runs | **exit 0** |
  | V3-N1 · V3-N2 · harness · stage-control · compiler suites | 113 · 203 · 39 · 20 · 29, all OK |
  | `repo-audit.py` | exit 0 |
  | check kinds exercised · profiles · repair rounds | **6/6** · zero · zero |

  **Burden, and the one figure that moved.** Authored control is **unchanged at 14,811 B = 17%**
  of protected work — the WorkSpecs are byte-derived from round 1, so this had to hold, and it is
  the figure plan §10's *effort* criterion turns on. **All control rose from 94% to 115%**, now
  exceeding the deliverable it describes. The increase is entirely generated (69,215 → 88,144) and
  its cause is the amendment: **the disclosure requirement makes reviewers write more.** Round 2's
  two results carry 14 findings and 11 residuals against round 1's leaner pair. That is the
  mechanism working as designed and costing what it costs, and both readings belong in the
  adoption decision: the human effort did not move, and the repository's control volume passed the
  work it protects.

- 2026-07-21 — **the user's second round of revise rulings, taken in-session and binding on
  amendment 2.** Recorded so the reasoning survives the session rather than only its outcome:

  1. **The package is a FLOOR, not a ceiling** — settled after sustained argument. The
     reviewer may read anything at the pinned revisions, and the disposition records the
     reviewer's real judgment of the obligation (the world-口径 reading, which is how all four
     real reviews actually filled it). The "out-of-package evidence can only downgrade" rule
     this session first proposed is **wrong and withdrawn**: verdicts are driven by findings,
     and findings may use any pinned-revision evidence in either direction. The
     `established_from` / `missing_members` field proposal was withdrawn with it — no consumer.
  2. **What freezing is actually for**, settled by 反事实分析: the ReviewPackage's only
     load-bearing function is pinning the **uncommitted control plane** (resolved plan,
     fulfillment/manifest, check results, coverage) so the executor cannot edit its own
     materials mid-review. Tree members are already content-addressed by the pinned commit —
     their member digests re-prove what `git show` already guarantees. Payload immutability
     comes from reading pinned revisions, not from the package. **Registered as N3-R9.**
  3. **Deferred to the 特例 bucket, explicitly out of this round** (user: "这三样之后再说"):
     (a) the `review_only` incentive-gradient fix and (b) obligations declaring their own
     required evidence — both land in `document-work-spec.schema.json`, which is N0-signed;
     (c) the commit-first workflow that would supersede the ReviewPackage layer — it hits
     N2-signed acceptance N2-A1, so it can only arrive as a versioned successor, never as an
     amendment. Also deferred: the two visibility items (the START-surface `review_only`
     ratio; `EXECUTION.md` declaration discipline).

- 2026-07-21 — **amendment 2: `eca4902` `V3-REVISE-REVIEW-CLARITY-AMENDMENT-v1`.** Two paths —
  `document-harness/REVIEW.md` and `schema/document-assurance-v3/review.schema.json` — both
  first-added at `0ba649c` (V3-N2), re-verified by `--diff-filter=A`; the two immutable blobs
  re-hashed unchanged (plan `8ad404b1…`, contract `b2dbdf75…`). Description/instruction layer
  only: the schema diff is 6 lines, all inside description strings, with zero guard /
  `required` / enum changes — so no pinning test moved and there was no behavior to
  mutation-verify (the grep proving so is recorded in the revise-2 plan's Notes). The five
  fixes: **(1)** N3-R6 — both worked examples replaced with synthetic cases drawn from neither
  shadow subject (a CLI-migration-guide compatibility table; a release-notes
  re-run-the-benchmarks acceptance clause), same teaching shape; **(2)** the disposition
  boundary split — `SUPPORTED` = established from evidence at the pinned revisions (package
  members or beyond, coverage disclosed via the existing `note` / `residual_uncertainty`
  fields), `NOT_SUPPORTED` = evidence **contradicts**, `UNVERIFIABLE` = could not establish
  either way **including** evidence-not-reachable, the state two real reviewers labelled
  differently; **(3)** N3-R7(i) — floor semantics stated in both files, the refusal list
  recast by what load-bears: digest mismatch and branch-instead-of-commit stay refusals, the
  six schema-mandated roles stay a freeze-time hard failure, and conditional/completeness
  membership (the N3-R4 `CHECKS-OMITTED` class) is downgraded to finding-and-continue —
  `check_package` tooling and the schema `allOf` unchanged; **(4)** a new Evidence-discipline
  section — pinned-revision reads only, control-plane digest verification before reliance,
  the out-of-band digest custody chain, and the contract-§5 reconciliation labelled as
  REVIEW.md's reading rather than a derivation; **(5)** N3-R7(ii) — the stop criterion
  re-drafted to "cannot be established from any evidence at the pinned revisions" with an
  explicit process-claims exemption, and N3-R8 — `package_ref` documented in both files as
  `canonical_digest(package)` with the one-line reproduction command. All suites green after
  the change (113 / 203 / 39 / 20 / 29).

- 2026-07-21 — **shadow round 3 built by derivation from round 2**
  ([`round-3/build_round3.py`](../../../assurance/shadow/round-3/build_round3.py)):
  all **seven** round-2 scripts derived — build_round2's five plus `freeze_only.py` and
  `validate_review.py`, which are round-2-only — through a substitution table of two kinds and
  no third (`round-2` → `round-3` control roots; `-r2` → `-r3` run ids). build_round2's
  `parents[N]` bump was deliberately **not** carried over: rounds 2 and 3 sit at equal
  directory depth, and carrying it would have broken `RS_ROOT` resolution in every derived
  script. The script asserts round 2 unmutated and it is (41 files, 0 changed). The WorkSpecs
  remain deliberately unrepaired — the imperfect maps are still the test subject.

  **Round-3 mechanical results**, matching round 2 exactly as they must (the amendment touches
  only the review layer): run-a1 **8/8 PASS**, manifest CONFORMANT over 8 observed changes;
  run-p3 **7/7 PASS**, CONFORMANT over 7; record / locators / coverage clean on both. Packages
  frozen **before** any review (`freeze_only.py`, keeping the round-2 ordering fix): **16
  members each**, `verify_member_bytes` clean on both, `V3-PACKAGE-CHECKS-OMITTED` recurring
  on both runs exactly as N3-R4 records — left standing again. Package digests: run-a1
  `d8851f99…`, run-p3 `5d676b03…`.

  **The dispatch prompts are files this round** (`round-3/dispatch-prompt-run-{a1,p3}.md`), so
  their contamination-freedom is auditable rather than asserted: no expected verdict, no
  worked-example content, no round-1/round-2 verdict facts; independence constraints as round
  2 **plus** the round-3 additions — `shadow/round-2/**` is barred, and each reviewer is
  barred from the sibling run's round-3 root and prompt. Reviews **not yet dispatched** at
  this entry: the amendment commit (`eca4902`) goes first to the user's independent review
  agent, on the round-2 lesson that an unreviewed amendment contaminated a full round's
  evidence.

- 2026-07-21 — **the amendment went through an external checkpoint review before round-3
  dispatch — a control new to this round — and the checkpoint caught what the executor had
  twice missed.** The user runs an independent read-only review agent; amendment 2
  (`eca4902`), the round-3 build and the dispatch prompts went to it before any reviewer was
  dispatched, on the round-2 lesson that an unreviewed amendment contaminated a full round's
  evidence. Its result, in substance, with dispositions:

  - **All four checkpoint questions returned PASS.** The five fixes verified faithful to the
    rulings (the reviewer re-ran the structure check itself: keys added/removed none, three
    leaf changes, all description strings; all five suites re-run independently, green; the
    canonical-digest reproduction command executed against both frozen packages and matching
    the out-of-band values, with `sha256sum` confirmed ≠ — the N3-R8 trap is real). The new
    worked examples verified non-derivable from either subject — and the old examples
    confirmed, against subject bytes, to have been verbatim answers. The plan deviation
    (schema root description) judged a necessary fix, and **ratified by the user**
    (`approved-by-user: 2026-07-21`, stamped in the revise-2 plan Notes; the agent
    recommended, the user ratified — reviewers do not ratify).
  - **L1, severe, found by the checkpoint, fixed before dispatch:** the prompts' do-not-read
    list barred paths but not **history**. `REVIEW.md` sits on the read-first list, so
    `git show eca4902^:<REVIEW.md>` returned both subjects' answers verbatim, and the
    amendment commit's own message advertised the retrieval. The executor had missed this in
    two successive prompt drafts. Fixed: role-instruction and schema file history barred;
    branch commit history barred (`git log`, commit objects and messages); `git show
    <revision>:<path>` scoped to the package-pinned revisions only — any path within those
    trees, so floor semantics survive intact; the commit name-drop removed from the prompts.
  - **L2/L4/L5, signpost surfaces, fixed structurally:** the shadow-tree bar inverted from
    denylist to **allowlist** — inside `shadow/**` a reviewer may read only its own run root,
    `validate_review.py`, and its own prompt — plus `.harness/**` barred. One rule now covers
    the class, including members the executor might have missed a third time.
  - **L3, accepted with reasons:** `validate_review.py`'s docstring reveals that a round 2
    existed. The bar list itself reveals the same by naming `round-2` paths; "a previous
    round exists" is unavoidable, non-actionable knowledge, and hand-editing a derived script
    would break the zero-drift derivation discipline for no gain.
  - **F4/F1/F2, fixed as amendment 3 — `c07d682`
    (`V3-REVISE-REVIEW-CHECKPOINT-AMENDMENT-v1`):** the stop example rewritten onto the
    criterion's FIRST leg (work never done — a localization pack missing translated
    quick-start files for two declared locales, the absence establishable from the pinned
    tree; vocabulary cross-checked zero-overlap against all six subject files at their pinned
    revisions), removing both the skeleton echo of run-p3's leg and the residual phrase the
    checkpoint flagged; the process-claims exemption gained its missing positive instruction
    (an unmapped process unit is still disclosed through the three items — the exemption
    removes only the stopping branch); the over-broad third exemption example dropped (a
    VERIFY's prior-round record is pinned and mechanically checkable, so "no evidence lock at
    any revision" was not universally true of it).
  - **F3, registered:** "checks belong in the package" has no mechanical owner — contract
    invariant 9 binds the *executor*, the schema `allOf` mandates six roles (checks not among
    them), and REVIEW.md now explicitly declines to refuse over missing check members. The
    three are consistent because they bind different parties, and the
    deterministic-obligation evidence binding is separately owned by coverage `NO_RESULT`.
    Recorded so no reader infers an enforcement that is not there.
  - **F5, the checkpoint's honesty ceiling, recorded as stated:** the five fixes have **zero
    mechanical binding** — no test pins the changed description text, so "all suites green"
    must never be read as "these wordings are held". The reviewer independently confirmed the
    no-mutation-verify exemption was correct rather than evasive. This is the instruction
    layer's inherent property (visibility, never guarantee), and it bounds every prose fix
    this revise round has made.

  Round 3 now measures the **amendment-2+3 bundle** (`eca4902` + `c07d682`); the §8
  comparison's confound statement widens accordingly.

- 2026-07-21 — **round 3: two FULL reviews in fresh contexts on the amendment-2+3 bundle,
  both validating clean, both binding real digests. The comparison follows, and it must be
  read through its confound first.**

  **The confound, stated before any number:** round 3 differs from round 2 in the whole
  amendment-2+3 bundle — de-contaminated worked examples AND the revised
  disposition/floor/stop criteria AND the checkpoint fixes (`eca4902` + `c07d682`) — plus
  hardened dispatch prompts (history bars, shadow-tree allowlist). Any verdict delta is
  attributable to the bundle, never to de-contamination alone.

  | | round 2 | round 3 |
  |---|---|---|
  | run-a1 verdict | `REVIEWED_NO_BLOCKER` + `INCOMPLETE` + disclosure | same shape, clean |
  | run-a1 unmapped units | 6, ids coined by reviewer | **1** — `raw-scope-allowlist-hard-error`, the handoff §3 hard-error requirement; §4 judged **subsumed** as constraints inside mapped obligations, §8/§9 process-exempt |
  | run-p3 verdict | **`SPEC_GAP`** — stopped | **`CHANGES_REQUIRED`** — the blocker drives the verdict |
  | run-p3 unmapped units | 3 | **1** — `unit-acceptance-rerun-determinism`, the same dropped fifth assertion |
  | package digest | supplied out-of-band, trusted | supplied out-of-band **and independently reproduced from tooling by both reviewers** — the N3-R8 fix making reproduction possible |
  | binding guard post-review | accepted / REFUSED tampered | same, both runs |
  | validator | clean ×2 | clean ×2, exit 0 |

  **run-p3's verdict moved, and the move is the criterion change working, not noise.**
  Round 2's reviewer, under the ceiling reading, declined to establish the dropped
  determinism assertion and stopped at `SPEC_GAP`. Round 3's reviewer, under floor semantics
  and the redrafted criterion, established from the pinned candidate that the dropped unit's
  work **was in fact done** (P3-inventory §0/§3/§7 address re-run determinism) →
  disclose-and-continue — and the verdict was then driven by the real defect: the
  ExperimentLab count, independently reproduced a **fourth** time and sharper again (51 not
  110; `smoke-01/** (55)` is 11 tracked files; true `.md` total 161; base and candidate trees
  identical on the point). `CHANGES_REQUIRED` with a bounded minimum fix — exactly the route
  V3-D6 intends for a repairable candidate defect. **N3-R3 stands, twice sharpened.**

  **The de-contamination payoff is provenance, not novelty.** Round 3's run-p3 reviewer found
  the same dropped assertion round 2 found — but round 2 reached it with the answer printed
  in the reviewer's own role instructions, and round 3 reached it by a line-by-line recheck
  of the Acceptance paragraph against six obligations, under instructions carrying no trace
  of it (prompt sweep: zero hits for verdict words, both example vocabularies, both amendment
  hashes). The same finding is now clean evidence. run-a1's reviewer coined a gap **no
  earlier reviewer and no example ever named** (§3's hard-error code) and explicitly judged
  the previously-famous §4 gap subsumed — independent judgment, visibly different from
  example-copying.

  **The unmapped-unit counts dropped (6→1, 3→1) and the honest reading is undetermined.**
  Both candidate explanations are stated: floor semantics + the process-claims exemption +
  subsumption reasoning legitimately triage what round 2 counted as separate gaps; or the
  narrowed framing suppresses disclosure. Unit ids are reviewer-coined, so the counts are not
  a comparable metric across reviewers. What is comparable: both round-3 reviewers still
  returned `INCOMPLETE` with enumerated ids, and the disclosure guard was exercised — the
  maps' imperfection stayed visible, as designed.

  **Deterministic results, measured in one pass immediately before this entry:**

  | Check | Result |
  |---|---|
  | round-3 run-a1 / run-p3 deterministic checks | **8/8** and **7/7 PASS**, manifests CONFORMANT |
  | `validate_review`, both runs | **exit 0, `check_review_result : clean`** |
  | packages · `verify_member_bytes` | 16 members each · clean |
  | binding guard, correct / one member dropped | **accepted / REFUSED `V3-REVIEW-PACKAGE-BINDING-MISMATCH`**, both runs |
  | `V3-PACKAGE-CHECKS-OMITTED` | recurs on both runs — N3-R4 standing, deliberately untouched |
  | cold resume, both runs | exit 0 |
  | V3-N1 · V3-N2 · harness · stage-control · compiler suites | 113 · 203 · 39 · 20 · 29, all OK |
  | `repo-audit.py` | exit 0 |
  | check kinds exercised · profiles · repair rounds | **6/6** · zero · zero |

  **Burden.** Authored control unchanged at **14,811 B = 17%** of protected work — the
  WorkSpecs are byte-derived, so this had to hold, and it is the figure plan §10's *effort*
  criterion turns on (still not triggered). All control **89%** (79,621 B), down from round
  2's 115%: the round-3 results carry 3 findings and 11 residuals against round 2's 14 and
  11 — leaner reviewer output, not a rule change; no rule caps volume, and the figure is
  descriptive in both directions.

  **Rounds 1 and 2 byte-untouched** (no write under their roots this session;
  `build_round3.py` asserted round 2 unmutated at derivation, 41 files, 0 changed).

- 2026-07-21 — **the review side delivered the first read whose *subject* was the
  instruction layer itself**
  ([`v3-review-note-instruction-layer-custody.md`](../v3-review-note-instruction-layer-custody.md),
  committed `f01502f` with the other two review-side notes at the user's routing). Produced
  at the user's request after they flagged the prose layer as disordered. Its five note-local
  items and its diagnosis, with the dispositions the user approved:

  - **C1** (README.md banner three nodes stale and self-contradicting) and **C2** (the
    contract's frontmatter `status:` violating the contract's own no-self-status rule, patched
    by a duplicate line in README.md) — quotes independently re-verified by the execution side
    before routing. Both fixes are **subtractive** (delete the state assertion; delete the
    duplicate, point at N0 record §8). **C3** (one unmapped-unit trigger, three statements
    across contract §6 / EXECUTION.md / REVIEW.md, no stage markers — the only item no script
    could ever catch) — fix is **additive**, one stage-qualifier line in each role file.
    **All three are batched into V3-N4, whose allowlist holds exactly their landing files**
    (`document-harness/{README,EXECUTION,REVIEW}.md`) — no fourth ad-hoc out-of-node
    amendment, per the note's own routing.
  - **C4** (REVIEW.md's labelled local rules, now two, growing into the contract's
    silence-gap) and **C5** (rule duplication without derivation — e.g. seven copies of the
    contract-§5 sentence across five files, on the one surface where the product forbids
    exactly that) — **registered, no v3 action**; the fold-back threshold and any checkers
    are post-v3 questions.
  - **L3 / F3 / F5** — already dispositioned in the checkpoint entry above; the note concurs
    with each disposition.
  - **The §5 ruling is adopted as standing discipline**: never rewrite the instruction layer
    (nothing holds its semantics; the measured edit risk is 3 defects per 79 careful lines,
    n=1); prefer few, batched, additive/subtractive edits at node boundaries; the edit *rate*,
    not size, is what outran review this week.
  - **The §1+§4 custody analysis went into the adoption adjudication as input, not blocker**
    (the note's own §7 ruling): the instruction layer is load-bearing, mechanically unbound
    and had no scheduled read; every defect that caused measured harm was in the class no
    checker catches; the demonstrated instrument is the **independent read** — per-amendment
    checkpoint (yield: 3/79 lines) plus node-boundary cold read (yield: C1–C5). Registered
    as **N3-R10**.

- 2026-07-21 — **the user ruled `ADOPT_DOCUMENT_V3`. V3-N3 closes at its decision gate.**

  **Basis.** Round-3 evidence (`2672abf`) on top of the full three-round record; plan §10
  checked clause by clause — the only clause that can force `REVISE_V3` (measured control
  *effort* dominating the protected work) is not triggered (authored control 14,811 B = 17%,
  constant across all three rounds); both review-side product notes (obligation-authoring,
  instruction-layer custody) were on the table as decision inputs, and each rules itself a
  finding rather than an adoption blocker. The known negative side was stated to the user
  before the ruling: replay-only evidence, the untested real-work repair/VERIFY path, subject
  adjacency, zero mechanical binding of the instruction layer, and the parked structural
  questions (N3-R9 commit-first supersession, the `review_only` incentive gradient).

  **What the ruling does.** V3-N4's entry condition is met. **N4 execution still requires its
  own explicit user authorization** — not given by the adoption ruling itself, matching every
  prior node. What the ruling does **not** do (plan §9 N4 OUT + N4-A5): no business-stage
  activation, no P4 (`P4-IMPL-v1` stays `approved / effective=false`), no source-code or
  platform expansion, no v1/v2 deletion; P4 and every business run remain separately
  authorized.

  **Standing discipline attached to adoption by the user** (to be written into the two
  `v3-harness-{operating,review}-contract.md` files at a user-gated boundary): (1) every
  instruction-layer amendment passes an independent checkpoint read before use; (2) a cold
  read with the instruction layer as its subject at each node boundary; (3) no rewrites —
  batched additive/subtractive edits only.

  **Queue after this ruling, in order:** V3-N4 (default pointer + C1/C2/C3 batch + LEDGER
  sync + tested rollback pointer) upon explicit authorization; the harness-contract
  discipline edit; the 特例-bucket design round (`review_only` incentive +
  obligations-declare-evidence + commit-first successor — the custody question and the
  obligation-authoring question are the same `review_only` question asked of the harness and
  of the work).

## 9. Carried-forward residuals

| # | Residual | Owner | What must actually land |
|---|---|---|---|
| N3-R10 | **The instruction layer (`README`/`EXECUTION`/`REVIEW` + contract prose) is load-bearing, mechanically unbound, and had no scheduled read.** Measured: two amendments changed 92 prose lines + 3 schema descriptions with zero test movement; all five harm-causing instruction defects this node witnessed (N3-R6, R7 i+ii, R8, the disposition split) were found *incidentally*, and every one falls in the class no checker catches, while every checker-catchable defect (C1/C2/C5) never caused measured harm. The demonstrated instrument is the **independent read**: per-amendment checkpoint (3 defects / 79 lines) + cold read with the layer as subject (C1–C5). C4 (growing labelled local rules) and C5 (rule duplication without derivation) are registered under this row as records, not tasks. Full analysis: [`v3-review-note-instruction-layer-custody.md`](../v3-review-note-instruction-layer-custody.md) | **standing discipline (user-attached to adoption) + post-v3 governance** | C1+C2+C3 land at V3-N4 (its allowlist holds exactly their files). The three-part discipline (amendment checkpoint reads; node-boundary cold reads; no rewrites) goes into the two v3-harness contracts at a user-gated boundary. C4's fold-back threshold and any C5 checkers are post-v3 questions — checkers must never be presented as covering the class that caused harm |
| N3-R9 | **The ReviewPackage's only load-bearing function is pinning the uncommitted control plane; the rest of the freeze layer is redundant with git.** Tree members (instruction, sources, candidate artifacts) are content-addressed by the pinned commit, so their member digests re-prove what `git show` already guarantees; member-completeness loses consequence under floor semantics (amendment 2 downgraded conditional membership to finding-and-continue); and a commit-first workflow — commit the control plane, then review everything at a commit — would supersede the whole layer. That supersession hits N2-signed acceptance **N2-A1**, so it is 特例-bucket work: a versioned successor, never an amendment | **特例 bucket — user-gated, out of every current round** | Nothing in this round. If taken up: a versioned successor to the review layer in which the control plane is committed before review and the package reduces to a commit plus a member list, with N2-A1 re-satisfied by the successor's own acceptance rather than by amending the signed schema |
| N3-R8 | **`package_ref` is a canonical-JSON digest, not the package file's bytes, and no document says so.** A round-2 reviewer computed `sha256sum review-package.json` and got a value unrelated to the real digest; it concluded, correctly on the information available, that it *"would have concluded the package was corrupt"*. The reviewer only bound the right value because the dispatch prompt supplied it — which is not a property of the product | **a later node, if adopted** | One sentence in `REVIEW.md` (and the schema's `package_ref` description) stating the digest is `canonical_digest(package)`, plus the one-line command that reproduces it. Cheap, and it currently costs every reviewer either a false alarm or an unverified assumption |
| N3-R7 | **Two defects in the V3 revise amendment to `REVIEW.md`, both found by round-2 reviewers.** (i) The file says the frozen package *"is what you are entitled to review"* but never says whether that is a **ceiling** or a **floor** on evidence — the two reviewers read it oppositely and **one of them states the choice materially changed its verdict**; (ii) the stopping criterion's *"nothing in the frozen package can settle whether it was"*, read literally, makes every process instruction a `SPEC_GAP`, contradicting the same file's *"process claims have no evidence lock"* ceiling | **the execution side — this is my authoring, and it is wrong as written** | (i) A rule for out-of-package probing: permitted, and disclosed as the reviewer's probe rather than as frozen evidence, is what run-a1's reviewer improvised and is probably right — but it must be stated, not improvised. (ii) Exempt process claims from the stopping branch explicitly; they are an honesty ceiling, not a spec gap |
| N3-R6 | **Round 2's routing evidence is contaminated: `REVIEW.md`'s two worked examples are the answers to the two subjects round 2 reviews.** The stop example states run-p3's answer verbatim; the disclose example states run-a1's. Found and disclosed unprompted by run-p3's reviewer, not by the author. The amendment itself is unaffected — it is mutation-verified and subject-independent — but *"whether a reviewer independently finds and correctly routes a map gap"*, which is what round 2 exists to measure, is not cleanly established on the example units. Partial independence survives: both reviewers found several units the examples do not name (6 and 3 against 1 and 1), and run-a1's hand-checked all 31 locked decisions rather than taking the example's word | **user decision** — re-run with de-contaminated examples, or accept the bound | Replace both worked examples with cases drawn from a subject that is **not** under review, then re-run both FULL reviews (measured cost: ~10 min each). Otherwise the adoption decision rests on evidence a reviewer itself labelled self-referential |
| N3-R5 | **`N3-A5` splits in two, and only the second half is a real limit.** A5 is *"the user primarily approves WorkSpec obligations/exceptions, not generated metadata"*. **(i) What the decision surface contains** is a property of the WorkSpec's shape, independent of whether the work is finished — **and run 1 already produced the observation** (§4.2). It was not recorded, which is the actual defect in this row's history. **(ii) Whether a human engages with that surface under real stakes** cannot be established by any shadow run, replay or live: the user knows they are being measured | **(i) discharged at §4.2 · (ii) permanent — do not schedule work against it** | Nothing. (ii) is an endpoint, not debt: the first real use is its own observation, and v3 is local and non-binding so the cost of learning it late is one wasted gate, not damage. `N3-A4` remains half-exercised (neither run performed a repair or a VERIFY, because repairing meant editing a pilot source `N3-A8` forbids) and `N3-A1`'s *"complete **or truthfully stop**"* applies to run 2, which returned `CHANGES_REQUIRED` and stopped unrepaired — both worth stating in round 2 rather than assumed. **Twice corrected on user challenge (2026-07-21):** first this row claimed the node was "not closeable without an acceptance matrix" — over-stated, since plan §8 gives N3 a *decision* gate, not a signature; then it claimed A5 was wholly untestable in a replay — also over-stated, since half of it had already been observed and I had failed to record it |
| N3-R4 | **Evidence layout batches all `CheckResult`s into one file**, so a `ReviewPackage` can carry only one `check_result` member for a run that produced eight. `check_package` reports it as `CHECKS-OMITTED`, correctly — a reviewer cannot address an individual result | **a later node, if adopted** | Either one file per `CheckResult`, or a package member shape that can address a result inside a batched file. Found only because the freeze step was finally run |
| N3-R3 | **`P3-inventory.md` overstates ExperimentLab by 59 files** (110 vs 51), making its frozen total 220 instead of 161 and invalidating the `Coverage check … ✔` line that is its only evidence for the 100%-accounted acceptance property. Independently verified at base `90deba7` | **user** — it is real committed project data, outside every v3 node's allowlist | A correction to that one document, plus a decision on whether the manifest frozen against it needs re-approval. Found by a shadow run; not repaired by one, because N3-A8 requires the pilot sources stay untouched |
| N3-R2 | **Three checks in run 2 were unbound extras**, in neither `check_order` nor any `local_check_refs`, and the harness did not flag them. A check bound to no obligation produces evidence nobody is accountable for reading | **a later node, if adopted** | Either the resolver rejects a check request no obligation references, or the coverage view reports it. My authoring error surfaced a missing guard |
| N3-R1 | **`INCOMPLETE` + `REVIEWED_NO_BLOCKER` is refused by the guard, but nothing tells a reviewer which verdict to use instead.** Product and reviewer disagreed on real work, and both positions are defensible about different objects (the map vs the artifact) | **user decision at §4** — a `REVISE_V3` item, or a later node if the decision is `ADOPT_DOCUMENT_V3` | Either `REVIEW.md` states that an `INCOMPLETE` recheck returns `SPEC_GAP` (routing to a new WorkSpec revision, per V3-D7), or the guard is narrowed to say which verdict it expects. Not fixable at N3, which owns no module |
