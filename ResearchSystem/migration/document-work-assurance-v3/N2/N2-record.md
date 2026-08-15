# V3-N2 administrative record — bounded semantic review, repair and final disposition

Node: `V3-N2` of [[document-work-assurance-harness-v3.plan|the v3 plan]] §9. Sole writer: the
execution session.

**Section roles, declared here because the numbering shifts per node** (N0: §8 log, §9
register; N1: §9 log, §10 register; this node: §8 log, §9 register):

- **§8 is the append-only log.** Entries are added, never rewritten or reordered. A wrong
  entry is corrected by appending one that names it, exactly as N1's errata did.
- **§9 is a cumulative register.** Rows are appended, and an existing row may be sharpened
  when a later finding changes what must land; every such change is itself logged in §8.
- **§§1–7 record this node's own facts** and are not rewritten once the node closes.

Nothing here weakens the rule that signed contract bytes and approved plan bytes are never
modified.

> [!done] Node closed — user-signed 2026-07-20
> Signed candidate: `23ac473` (`V3-N2-REVIEW-FIX1-CANDIDATE-v1`). Plan §8 budget at close:
> **FULL 1/1, fix 1/1, VERIFY 1/1 — fully spent.** The signature closes V3-N2 only; it does
> not authorize V3-N3, which needs its own explicit user authorization **and** user approval
> of the two exact shadow subjects its IN clause requires. Seven residuals carry forward in
> §9; two are stated limits rather than debt, and N2-R7 records that the VERIFY report itself
> is not in the repository.

> [!important] Resume pointer — where this node stood while open (superseded by the box above)
> **Goal:** V3-N2, bounded semantic review, repair and final disposition.
> **Node base:** `1e34a1e`. **Out-of-node amendment already landed:** `8efe3e9` (§2.1, §8).
>
> **Landed:** three schemas; the four modules `review` / `flow` / `summary` / `issues`;
> `EXECUTION.md`, `REVIEW.md`, the README interface rows; `rsc v3 flow` and
> `rsc v3 disposition`; the golden/validator half of the acceptance matrix.
>
> **Landed since:** both acceptance halves (176 tests), the eleven defects they found fixed and
> mutation-verified, their tests reconciled onto the corrected behaviour, `rsc v3 review`, and
> §7 measured last.
>
> **断点 / next step:** the FULL returned `CHANGES_REQUIRED` (one blocker, seven findings) against
> `0ba649c`; the user approved a fix boundary of the blocker plus F1–F6, and that repair is
> committed. **Budget: FULL 1/1, fix 1/1 — one targeted VERIFY remains (1/1).**
>
> Next is the targeted VERIFY, whose scope V3-D6 fixes as the accepted findings, the **entire**
> repair diff and the permanent boundaries. Late-churned code, which is what the review side
> asked for rather than an argument: `flow.py`, `summary.py`, `rsc.py` and the three test files
> in the repair diff. After that the user classifies and signs — or, if a blocker still stands,
> the run stops; there is no second fix.
>
> **Why this block and not `.goals/LEDGER.md`:** that file is on the N0 and N4 allowlists and
> excluded at N1–N3 (plan §9), so this record is the node's durable ledger. A pointer written
> there now would be an out-of-boundary write, and a copy of this state in Claude memory would
> be a second copy that drifts the moment the node moves — the duplication defect this harness
> exists to prevent (N0-A6, V3-D8).

## 1. Authorization and base (plan §9, V3-N2 IN)

- **N1 closed and signed:** the user signed V3-N1 on 2026-07-20, binding candidate `802e16a`;
  an independent targeted VERIFY of that candidate returned `PASS`
  ([N1 record §8 errata](../N1/N1-record.md), 2026-07-20). N1's plan §8 budget closed fully
  spent: FULL 1/1, fix 1/1, VERIFY 1/1.
- **N2 authorization:** the user explicitly authorized V3-N2 on 2026-07-20 ("startN2"), which
  is what the N1 stop gate required — N1's signature closed N1 only and authorized nothing
  further ([N1 record §10.1](../N1/N1-record.md)).
- **IN:** the accepted N1 interfaces and evidence topology (N1 record §3), the seven N0
  schemas plus N1's two, and Contract v3 as signed.
- **OUT (not touched by this node):** multi-track review, a second repair, review-of-review,
  external gates, default cutover, P4 and any business content.
- **Node base:** `1e34a1e` (`V3-LEDGER-SYNC-v1`), the branch tip when this node opened.

### 1.1 Two residuals arrive with this node, and two must not be worked on

| Inherited | Source | Owner |
|---|---|---|
| **N0-R2** — terminal status↔pointer conditionals on `AssuranceWorkState` | N0 record §9, deferred at N1 because the pointers involved name objects only N2 creates | this node, `N2-A7` |
| **N1-R2** — nothing obliges a run to include the R4 governance scan | N1 record §10 | this node, `flow.py` |
| N1-R3 — `check_audit` compares declared names, not contexts | N1 record §10 | **permanent endpoint — do not schedule work** |
| N1-R4 — a digest-less pointer cannot be verified at resume | N1 record §10 | **permanent endpoint — do not schedule work** |

N1-R1 was **discharged** by the N1 errata. Its withdrawn instruction is honoured here:
**this node does not re-verify `instruction.check_audit` or `assurance_state.resume` on the
premise that no review covered them.** Both were covered by the N1 VERIFY.

## 2. Change boundary actually used

Derived fresh from plan §9 V3-N2 before any write, per the rule N1 set for itself. Two
consequences are easy to miss and are recorded rather than discovered later:

- **`.goals/LEDGER.md` is not on this node's allowlist.** It is explicitly permitted at N0
  (thin pointer) and at N4 (pointer/status only) and excluded at N1–N3, so the answer is
  node-specific and N1's answer is not carried forward as a general rule. This record is
  therefore N2's durable progress ledger; no LEDGER pointer is written at this node.
- **`rsclib/document_harness/__init__.py` is not on this node's allowlist either.** The plan
  fixes each node's module list by name, so the package root froze when N1 closed. §3.1
  records what that costs and the in-boundary route taken instead.

| Path | Basis |
|---|---|
| `ResearchSystem/schema/document-assurance-v3/review.schema.json` | allowed new file |
| `ResearchSystem/schema/document-assurance-v3/assurance.schema.json` | allowed new file |
| `ResearchSystem/schema/document-assurance-v3/harness-issue.schema.json` | allowed new file |
| `ResearchSystem/tooling/rsclib/document_harness/{review,flow,summary,issues}.py` | allowed new files (four named modules) |
| `ResearchSystem/tooling/tests/document_harness_review/**` | allowed new root |
| `ResearchSystem/document-harness/EXECUTION.md` | allowed new file |
| `ResearchSystem/document-harness/REVIEW.md` | allowed new file |
| `ResearchSystem/migration/document-work-assurance-v3/N2/**` | allowed new root |
| `ResearchSystem/generated/document-assurance/review-test/**` | allowed new root |
| `ResearchSystem/tooling/rsc.py` | allowed existing file, v3 subcommands only |
| `ResearchSystem/document-harness/README.md` | allowed existing file, interface links only |

### 2.1 `SPEC_GAP` — the N2 allowlist and the artifact N1 landed are jointly unsatisfiable

Found before any schema was authored, and **verified by running the suite, not by reading it**.

Plan §9 V3-N2 mandates three new files under `ResearchSystem/schema/document-assurance-v3/`.
The N1 test [`test_candidate_checks.py`](../../../tooling/tests/document_harness/test_candidate_checks.py)
pins that directory:

```text
line 1334  files = sorted(SCHEMA_DIR.glob("*.schema.json"))
line 1335  self.assertEqual(len(files), 9, ...)
line 1336  self.assertEqual({path.name for path in files}, set(SCHEMA_FILES.values()))
```

Landing N2's mandated schemas therefore turns a green N1 suite red, and **neither repair site
is inside this node's boundary**: `tests/document_harness/**` is N1's root (N2 owns
`tests/document_harness_review/**`), and `SCHEMA_FILES` lives in `__init__.py`, which no node
after N1 may write. There is no in-boundary fix, so this is not a case of taking the lesser
fix and recording why — it is a stop.

**Evidence, in order.**

1. Baseline: `python tests/document_harness/run_tests.py` → `Ran 113 tests` / `OK`.
2. One placeholder schema file added to the directory → same command → `FAILED (failures=1)`,
   `AssertionError: 10 != 9`. The placeholder was then deleted; `git status` clean apart from
   this node's own new directory.
3. Scope of the collision established rather than assumed: exactly one site globs that
   directory (grep over `ResearchSystem/tooling` and `ResearchSystem/migration`). The **N0
   frozen fixture runner is unaffected** — it names its files explicitly through its own
   `SCHEMA_FILES` dict and does not glob — confirmed green at 41/41 with the placeholder
   present.

**What the assertion was for, and why it now misfires.** At N1 the pinned count was a real
guard: it proved the vocabulary scan had covered *every* schema rather than silently scanning
a subset — the R3 defect class. But it encodes the *count* where the acceptance property is
*cleanliness of whatever is present*, so the plan's own next node trips it. This is not an N1
defect that escaped review; it is a guard that was correct for the tree it was written
against.

**Not decided here.** `SPEC_GAP` stops (plan §8) and is settled by the user, not by this
session. The node was halted at the boundary-derivation step with nothing implemented.

> **Settled 2026-07-20 — see §8.** The user ruled for a narrow out-of-node amendment,
> landed at `8efe3e9` (`V3-N1-SCHEMA-PIN-AMENDMENT-v1`), outside this node's candidate. The
> text above stands as the finding; the resolution and its evidence are logged in §8 and the
> register row is sharpened in §9.

## 3. Interfaces handed forward

| Interface | Where | Note |
|---|---|---|
| `ReviewPackage` freeze + membership | `document_harness/review.py` + `review.schema.json` | six unconditional roles asserted by the schema; input/check/artifact completeness asserted against the run |
| `ReviewResult` (FULL / VERIFY) | same | closed verdicts per round; `residual_uncertainty` required, empty permitted |
| repair authorization + boundary | `document_harness/flow.py` | binds original candidate + accepted findings; the boundary may narrow, never widen |
| status transition legality | same | contract §8 mapping, plus the single-repair cap |
| terminal status↔pointer conditionals | same | both directions: required-at-status and not-yet-at-status |
| governance obligation | same | a run states whether the R4 scan ran; a skip is explicit and surfaces as a disclosure |
| `AssuranceCandidate` / `AssuranceSummary` | `document_harness/summary.py` + `assurance.schema.json` | pre-decision binding carries no outcome; the summary is faithful to the user's own decision |
| `HarnessIssue` + triage | `document_harness/issues.py` + `harness-issue.schema.json` | immutable, post-run, no lifecycle field |
| CLI surface | `rsc v3 flow`, `rsc v3 disposition` | read-only; makes the flow and the governance state invocable |

### 3.1 The package root froze when V3-N1 closed

The plan fixes each node's module list by name, so `__init__.py` — authored at N1 — is on no
later node's allowlist. Two consequences landed here:

- **the `SPEC_GAP` of §2.1**, whose repair site was partly `SCHEMA_FILES` in that file;
- **the three V3-N2 schemas cannot be registered with the package validator.** The
  in-boundary route is a local registry inside `review.py`, built from the *public*
  `SCHEMA_DIR` / `SCHEMA_FILES` / `SCHEMA_URI_BASE` exports rather than restating them, so it
  cannot drift from the frozen pack. It fails closed on an unknown kind exactly as the root
  validator does, and a test pins that every frozen schema still resolves through it.

The cost is a duplicated registry that would otherwise have been one line in a dict. It is
recorded here rather than hidden in the module, because a later reader finding two registries
should know it was a boundary decision and not an oversight.

## 4. Residuals discharged at this node

Two arrived (§1.1). Both are discharged in the interface, not only in the code.

### N0-R2 — a status that claims a stage which left no record

`flow.check_state_pointers` enforces two directions, and the second is the one that matters.
**Required-at-status** is cumulative: reaching `CLOSED` means every earlier stage's product
exists, so `CLOSED` without a `summary_ref` is refused — a run asserting it finished without
the document that finishes it. **Not-yet-at-status** is the mechanical form of "no temporal
self-binding" (N2-A7): `assurance_candidate_ref` cannot appear before `AWAITING_FINAL` and
`summary_ref` cannot appear before `CLOSED`, so a document that precedes the thing it binds
is unrepresentable rather than merely discouraged. The `assurance.schema.json` root reinforces
it from the other side — the AssuranceCandidate has no field that could hold a decision, an
outcome or a summary.

### N1-R2 — a check nobody was obliged to run

R4 left the governance scan mechanical and reachable, but an operator who never invoked it got
no signal at all. The obligation now sits on the `AssuranceCandidate`: `governance_scan` is
**required**, and it is a closed choice between `included: true` with a `result_ref` and
`included: false` with a `skip_reason`. `flow.governance_state` refuses to build either half
by default — supplying neither is rejected rather than defaulted, because the default would
have to be "assume it ran" or "assume it did not", and both are a guess recorded as a fact.

A skip stays legal. That is deliberate: R4's requirement is that the run *record* the state,
and forcing the scan would be forcing verification rather than making the unverified visible.
What a skip can no longer do is disappear — `flow.governance_disclosures` turns it into a
user-visible disclosure carried into the pre-decision binding, and `rsc v3 disposition` prints
`governance : NOT RUN — <reason>` above the decision.

## 5. Deliberate non-implementations

| Not implemented | Owner | Why not now |
|---|---|---|
| two real document shadow runs and the adoption decision | **V3-N3** | plan §9; nothing here claims v3 is adopted, and plan §10 forbids adoption without them |
| any v3 default entry / cutover / pointer change | **V3-N4** | conditional on the N3 adoption decision |
| a closed `kind` enum on `finding` | **none — deliberately absent** | no code switches on it, so it would be surface with no acceptance ID behind it (N0-A7). A finding is already located by `obligation_id` presence, `candidate_locator` and `minimum_fix` |
| promotion mechanics (the act of moving bytes) | **outside v3** | `AssuranceSummary` records *that* a promotion happened and where; performing it is a local step the user authorizes, not a harness capability (V3-D3) |
| any `DocumentAssuranceProfile` instance | **not yet witnessed** | V3-D2 requires two distinct real reuse witnesses; V3 may run indefinitely with zero published profiles |

## 6. Honesty boundaries of what this node built

- **Reviewer/executor distinctness is a comparison of declared names**, exactly as N1-R3
  records for the auditor. An executor writing `reviewed_by: "Reviewer Rin"` passes. Contract
  §1 settles it: role separation is a workflow protocol, not an OS guarantee. What is reachable
  — and is implemented — is that an unsupplied executor reports
  `V3-REVIEW-REVIEWER-DISTINCTNESS-UNVERIFIED` rather than silence.
- **`verify_member_bytes` proves a package's members still match their bytes *in the trees
  they pin*; it does not prove the package was complete when frozen.** A member never added
  cannot be found stale. Completeness is a separate check against the run (`check_package`),
  and neither substitutes for the other — a package can pass one and fail the other, which is
  why both exist and why neither is allowed to imply the other's result.
- **A `git` failure and an absent path are indistinguishable to it.** Reading a member out of
  a revision returns `None` either way, so a member naming a revision this repository does not
  contain is reported `MEMBER-MISSING` — accurate about the outcome, not about the cause.
- **The controller's faithfulness is checked against structure, not meaning.** The unresolved
  set must be exactly the reviewer's blocking findings, and the summary's outcome and
  limitations must be exactly the user's — but nothing here can tell whether a *disclosure's
  prose* fairly represents its source document. Requiring `source_ref` on every disclosure is
  what makes the claim traceable, not true.
- **`check_issue` without a run state cannot establish that the run was over.** It reports
  `V3-HARNESS-ISSUE-RUN-STATE-UNVERIFIED` rather than accepting the issue's own declaration —
  an issue asserting its own post-run status would be the self-referential class N0 spent five
  levels on.
- **A `SPEC_GAP` in this node's own construction was settled by an out-of-node amendment
  (§2.1, §8).** That amendment was written and verified by the execution session; it is
  executor-side evidence and is not a review of V3-N1.

## 7. Deterministic results

Every figure below was produced by running the named command **after the last change to what
it measures**, in one uninterrupted pass immediately before this section was written. N1 §8.4
records what happens otherwise: a count taken before a later file was added, presented under a
sentence claiming every figure came from a command. Per residual R1, each entry states which
tree it observed.

### 7.1 N2 acceptance matrix — 176/176, exit 0

`python ResearchSystem/tooling/tests/document_harness_review/run_tests.py` → `Ran 176 tests` /
`OK`. Observed tree: **worktree** (the suite builds its own disposable Git repositories and
never reads this repository's payload).

| File | Tests | Covers |
|---|---:|---|
| `test_package_and_review.py` | 51 | N2-A1, N2-A2, N2-A3 — membership cross-products, run-completeness, member byte binding, closed verdict surface, fail-open probes, named-code reachability sweep |
| `test_flow_repair_disposition.py` | 114 | N2-A4..N2-A11 plus inherited N0-R2 and N1-R2 — the full 9×9 transition cross-product, pointer conditionals in both directions, repair binding and boundary, C2 regeneration, VERIFY stop, controller faithfulness, promotion, issue/triage, no-lifecycle |
| `test_golden_review_views.py` | 11 | the pinned user-facing renderings and the V3-N2 schema extension |

The two acceptance halves were **authored in fresh contexts that did not write the
implementation**; the goldens and the validator regressions were authored by the execution
session. That split is why the halves found eleven defects rather than confirming assumptions
(§8). **This is a claim about how the work was done and carries no evidence lock** — it is
recorded as a claim, not as evidence.

### 7.2 Every other deterministic suite stays green

Observed tree: **worktree**.

| Suite | Result |
|---|---|
| `tests/document_harness/run_tests.py` (V3-N1) | 113 run, `OK` |
| `tests/stage_control/run_tests.py` (v1) | 20 run, 0 failures, 0 errors |
| `tests/run_tests.py` (P2 compiler + shadow lint) | 29 passed, 0 failed |
| `tests/harness/run_tests.py` (v2 A3) | 39 run, `OK` |
| `N0/fixtures/validate_fixtures.py` (contract fixtures) | 41/41, failures=0 |

The N1 figure is the one worth noting: it is 113 both before and after the three schemas this
node added, because the amended assertion (§2.1) scans whatever is present rather than pinning
a count.

### 7.3 Repository audit — exit 0, clean

`python Thesis/Work/Tooling/repo-audit.py` → `RESULT: clean (exit 0)`. Observed tree:
**worktree** — the audit reads working-tree bytes, which is what this node's uncommitted
candidate content is; the same worktree-scope caveat R1 recorded at N0 applies unchanged.

### 7.4 Changed-path allowlist — 23 in-node paths, zero out-of-boundary

`git diff --name-only 8efe3e9` plus `git ls-files --others --exclude-standard` → **24 paths**,
classified **individually against §2 rather than by bucket total** — N1 §8.4 proved a bucket
total hides an off-by-one.

| Path | §2 basis |
|---|---|
| `schema/document-assurance-v3/review.schema.json` | allowed new file |
| `schema/document-assurance-v3/assurance.schema.json` | allowed new file |
| `schema/document-assurance-v3/harness-issue.schema.json` | allowed new file |
| `tooling/rsclib/document_harness/review.py` | allowed new file (1 of the 4 named) |
| `tooling/rsclib/document_harness/flow.py` | allowed new file (2 of 4) |
| `tooling/rsclib/document_harness/summary.py` | allowed new file (3 of 4) |
| `tooling/rsclib/document_harness/issues.py` | allowed new file (4 of 4) |
| `tooling/tests/document_harness_review/_harness.py` | allowed new root |
| `tooling/tests/document_harness_review/run_tests.py` | allowed new root |
| `tooling/tests/document_harness_review/test_package_and_review.py` | allowed new root |
| `tooling/tests/document_harness_review/test_flow_repair_disposition.py` | allowed new root |
| `tooling/tests/document_harness_review/test_golden_review_views.py` | allowed new root |
| `generated/document-assurance/review-test/.gitattributes` | allowed new root |
| `generated/document-assurance/review-test/review-result-view.golden.txt` | allowed new root |
| `generated/document-assurance/review-test/review-result-no-residual.golden.txt` | allowed new root |
| `generated/document-assurance/review-test/flow-position.golden.txt` | allowed new root |
| `generated/document-assurance/review-test/summary-view.golden.txt` | allowed new root |
| `generated/document-assurance/review-test/harness-issue-view.golden.txt` | allowed new root |
| `document-harness/EXECUTION.md` | allowed new file |
| `document-harness/REVIEW.md` | allowed new file |
| `document-harness/README.md` | allowed existing — interface links only (see N2-R2) |
| `migration/document-work-assurance-v3/N2/N2-record.md` | allowed new root |
| `tooling/rsc.py` | allowed existing — v3 subcommands only (`flow`, `disposition`, `review`) |

The 24th path, `ResearchSystem/docs/General-Harness-v2-Design.md`, is **not part of this node**:
it is the untracked parallel-agent file that predates it. The user ruled at N0 that it stays
untracked and outside the candidate; this node did not touch it, does not stage it and does not
retain it.

No controller code outside the four named modules, no A4 import, no business content, no
old-file deletion and no `.goals/` write appears in the set.

### 7.6 Re-measured after the bounded fix round

Every deterministic check re-run after the repair, which is the step V3-D6 places between the
fix and the VERIFY. Measured in one pass immediately before this subsection.

| Check | Before the fix (§7.1–7.4) | After |
|---|---|---|
| N2 acceptance matrix | 176 OK | **198 OK** (+22: the fix-round locks) |
| V3-N1 matrix | 113 OK | 113 OK |
| v1 stage-control | 20 | 20 |
| P2 compiler | 29 | 29 |
| v2 A3 harness | 39 | 39 |
| N0 contract fixtures | 41/41 | 41/41 |
| `repo-audit.py` | exit 0 | exit 0 |

**Changed paths in the repair diff** — `git diff --name-only 0ba649c` plus untracked, classified
individually: `rsclib/document_harness/flow.py`, `rsclib/document_harness/summary.py`,
`tooling/rsc.py`, `tests/document_harness_review/test_fix_round_locks.py` (new),
`tests/document_harness_review/test_flow_repair_disposition.py`,
`tests/document_harness_review/test_package_and_review.py`, and this record — **7 paths, every
one on the §2 allowlist, zero out-of-boundary**. The eighth path is the pre-existing untracked
`ResearchSystem/docs/General-Harness-v2-Design.md`, which is not part of this node.

`issues.py` and `review.py` are **not** in the repair diff: the fix boundary the user approved
did not reach them.

### 7.5 Permanent boundaries

Re-derived, not carried forward from an earlier node's record:

| Boundary | Observed |
|---|---|
| approved plan blob | `git hash-object` → `8ad404b12b3242e700d0ad215048dffccada7d9c` — unchanged |
| signed contract blob | `git hash-object` → `b2dbdf752d8c155e4c65b14b5f420b880b8184a1` — unchanged |
| A4 (`f91a7c4`) is not an ancestor | `git merge-base --is-ancestor` → false; v3 still roots at A3 |
| N0 schemas / N1 modules | not in the changed-path set (§7.4) |

## 8. Append-only log

- 2026-07-20 — node opened. The user authorized V3-N2 explicitly; N1's signature had closed
  N1 only. Boundary re-derived from plan §9 before any write (§2), and two exclusions were
  found at that point rather than later: `.goals/LEDGER.md` (this record becomes the node
  ledger) and `__init__.py` (§3.1).
- 2026-07-20 — **node halted at `SPEC_GAP` before any implementation was written** (§2.1). The
  three schemas plan §9 mandates for this node cannot be added without turning the N1 suite
  red, and neither repair site is in this node's boundary. Verified by running the suite
  against a placeholder file, not by reading the assertion; the placeholder was deleted and
  the collision's scope was established by grep (one site) with the N0 frozen runner confirmed
  unaffected at 41/41. Nothing implemented, nothing committed, no schema authored. Awaiting
  the user's ruling on which of the routes in §9 to take.
- 2026-07-20 — interfaces frozen in dependency order: the three schemas authored and checked
  as valid Draft 2020-12 with resolving `$ref`s (12 files now in the pack, all 12 confirmed
  resolvable), then `review.py`, `flow.py`, `summary.py`, `issues.py`. One interface
  assumption was caught by reading the schema rather than trusting memory: the resolved plan's
  boundary field is `effective_change_boundary`, not `effective_boundary`, and the repair
  boundary check was written against the wrong name until it was verified.
- 2026-07-20 — **the amended N1 assertion earned itself immediately.** Because the pinned
  count became a subset assertion that scans every file present, the three schemas authored
  here were swept by the R3 vocabulary guard automatically, with no N2-side test needed and no
  edit to the N1 suite. 113 tests still green with 12 schemas in the pack; N0 fixtures 41/41.
- 2026-07-20 — **executor self-check found the V3-N1 D3 defect class reproduced in this
  node's own code: three named invariants were permanently unreachable.**
  `V3-ASSURANCE-SELF-BINDING`, `V3-ASSURANCE-PROMOTED-AFTER-REFUSAL` and
  `V3-ASSURANCE-PROMOTION-UNRECORDED` all sat *after* a schema validation that returned early,
  and the schema already rejected each of those documents — `additionalProperties: false` for
  the first, the `REJECT`/`REPLAN` promotion conditional for the other two. Verified by
  probing each with a document that should have triggered it: every probe returned only
  `V3-SCHEMA-…`.

  The acceptance property always held — such documents *are* rejected — so this was a
  **reporting** defect, not a correctness one, exactly as at N1. Fixed the same way the N1
  precedent settled it: run the invariants first and unconditionally (they are plain key
  inspections that assume nothing about shape, with defensive accessors since they now run
  before the shape is known), and append the schema report rather than replacing it. Deleting
  the now-redundant code was the other option and was rejected for N1's stated reason: in a
  governance record the reason is the part worth reading, and a greppable code per invariant
  is what makes it auditable. Re-probed after the fix — all three now report their specific
  reason alongside the schema error — with a negative control confirming a clean summary
  raises none of them.

  Worth recording about the method: this was found by walking every named issue code and
  asking "can a schema-valid document reach this line?", not by a test failing. A test written
  from the acceptance ID would have passed, because the document was rejected either way.
- 2026-07-20 — **a second self-check finding: a fail-open argument in `check_package`.**
  `results` defaulted to `()`, so the ordinary call `check_package(package, spec, record)`
  skipped the check-completeness guard entirely and a package omitting every CheckResult
  reported clean. This is the shape N1 found twice (`check_audit(executor=None)`,
  `ResumePoint.resolved`) and the review contract warns to expect more of.

  The N1 fix — report the unchecked state — **does not work here**, and the reason is worth
  keeping: an empty sequence is legitimately meaningful, because a run whose obligations are
  all `review_only` genuinely produces no results. "None exist" and "the caller did not say"
  are therefore indistinguishable once the call has been made, so no report could tell them
  apart. The ambiguity had to be removed at the call site instead: `results` is now required
  with no default, and a caller passes `[]` to state that the run had no checks. N1 rejected
  making a parameter required because its pinning test needed a report to assert against;
  that obstacle does not exist here, which is why the two guards of the same shape correctly
  get different fixes.
- 2026-07-20 — a **second boundary consequence** recorded while the first is settled, because
  it shapes the modules and is better known now than discovered mid-implementation: the four
  N2 modules cannot register their schemas with the package validator either, for the same
  reason (`SCHEMA_FILES` and `_registry()` live in `__init__.py`). Unlike §2.1 this one **has**
  an in-boundary route — an N2-local registry built inside the new modules from the public
  `SCHEMA_DIR` / `SCHEMA_FILES` / `load_json` exports — so it is not a gap. It is recorded as
  a cost: it duplicates package-level machinery that would otherwise be one line in a dict.

- 2026-07-20 — **the `SPEC_GAP` was settled by the user and the node resumed.** Ruling: a
  narrow out-of-node amendment to the one over-specified assertion, rather than replanning
  N2 or amending the approved plan bytes. Landed at `8efe3e9`
  (`V3-N1-SCHEMA-PIN-AMENDMENT-v1`) as a **separate commit outside this node's candidate**,
  touching exactly one file and no schema, module, signed byte or acceptance ID — deliberately
  not folded into the N2 candidate, so the review side can attribute it without asking.

  **What changed.** `assertEqual(len(files), 9)` plus the set-equality against `SCHEMA_FILES`
  became a subset assertion: every *registered* schema must be present, and every file present
  is scanned. A later node adding a schema no longer trips it; a registered schema going
  missing — the case that would make the scan cover less than it claims — still fails.

  **Both directions were mutation-verified, and neither probe touched a signed byte.** A
  temporary file carrying a forbidden `const` turned the test red; monkeypatching a ghost
  entry into `SCHEMA_FILES` turned it red; the unmutated control passed before and after both
  probes. The temporary file was deleted and the directory confirmed back at nine. Suite
  re-run green at 113. Testing the "registered file absent" branch by deleting a real schema
  was considered and rejected — the in-process patch proves the same property without ever
  putting an N0-signed file at risk.

  **What this does not establish.** The amendment was written, verified and committed by the
  execution session. That is executor-side evidence: it is not a review of N1, and it does not
  re-open or re-certify the closed node. It is also a change to a file the reviewed N1
  candidate contained, so the reviewed bytes and the current bytes of that file now differ —
  stated plainly here rather than left for a later reader to discover.

- 2026-07-20 — **the two acceptance halves were authored in fresh contexts that did not write
  the implementation, and between them they found eleven further defects.** Every one was
  reproduced against the candidate before being acted on. Recorded by shape, because the
  shapes repeat and the individual bugs will not:

  **The wrong-tree class — the most serious.** `verify_member_bytes` took a single `reader`
  and pushed every revision-bearing member through it, never comparing `ref["revision"]` with
  the tree actually read. It was wrong in both directions: a member pinning the base but
  carrying the candidate's digest verified **clean**, while the *correct* base digest was
  reported stale. Worse, it made the normal shape of a package unverifiable — instruction and
  sources are frozen at the base, artifacts at the candidate, so whichever tree the caller
  passed, the other group was checked against the wrong one. A `WorktreeReader` was also
  accepted for a revision-pinned member, so uncommitted bytes existing in **no committed tree**
  could certify it — the N1 R1 lesson, which `candidate.check_locators` already refuses.
  Fixed by reading each member through `CandidateTreeReader(root, ref["revision"])`, which
  removes all three at once and removes the fail-open `reader` parameter with them.

  **The fail-open class, twice more.** `check_review_result` tested `executor is None`, so an
  empty or whitespace identity — what an unset config field actually looks like — reached the
  comparison, differed from every `reviewed_by`, and reported *nothing at all*: the guard
  silently off, in the very function whose docstring claims that shape is prevented. And
  `check_repair_decision` read `plan.get("effective_change_boundary") or {}` without
  validating, so a plan missing that field let the widest possible repair boundary pass clean.
  Fixed by testing `not executor.strip()`, and by reporting
  `V3-FLOW-REPAIR-BOUNDARY-UNVERIFIED` rather than skipping.

  **Guards that fired only in the total case.** `CHECKS-OMITTED` used
  `if results and not member_check_paths`, so three results with one member was clean — the
  case the function's own docstring names as the one it catches. Now compared by count, with
  the residual limit stated in the code: a *swap* of one result for another is still not
  caught, because a CheckResult carries no storage path to match on. `INSTRUCTION-SUBSTITUTED`
  compared paths only, accepting a different revision of the same instruction file.

  **The identity comparisons that were simply missing:** the package's `base_revision` and
  candidate branch against the record's, and — the worst of them —
  **the user's FINAL decision target was compared to nothing.** A summary could faithfully
  terminate candidate A while the decision it cited was made about candidate B, and every
  digest verified. That is "check candidate A, report candidate B" at the one step where the
  user is the trust terminal; it is now `V3-ASSURANCE-DECISION-TARGET-MISMATCH`.

  **The N2-A7 guard covered 3 of 12 pointers.** `flow.py`'s docstring stated the
  no-temporal-self-binding rule generally while `_EARLIEST_POINTER` listed only the last three,
  so a `review_ref` at `AUDITED` or a `manifest_ref` at `RESOLVED` reported clean. Extended to
  every pointer — and the extension exposed something the first version would have got wrong:
  the repair loop returns the run to an *earlier* stage while it legitimately carries later
  pointers, so a naive stage comparison reports the whole round-0 evidence set as premature.
  The rule is therefore round-aware, and `repair_decision_ref` is bounded by the round rather
  than by a stage at all. A negative control pins that a repaired run at `EVIDENCED` is clean.

  **Two crashes where a report was owed**, both `Mapping`-typed parameters dereferenced
  without validation: `check_transition` on a state with no `repair_round`, and `check_issue`
  on a state with no `run_id`. A checker that raises on a malformed document takes the run
  down instead of recording what happened.

  **And the V3-N1 D3 shape once more, in `issues.py`.** `check_triage`'s
  `UNKNOWN-ROUTE` and `UNBOUND-TRIAGE` sat behind an early schema return that already rejected
  both cases. `summary.py` had been corrected for exactly this earlier in the node and
  `issues.py` had not — evidence that finding a defect class once does not sweep it.

- 2026-07-20 — **a regression this node introduced and then caught.** The fix that moved the
  promotion invariants before schema validation used `summary.get("promotion") or {}`, which
  returns the value itself for any truthy non-mapping — so a `promotion` that was a string
  crashed the checker with an `AttributeError`. The malformed document class that the reorder
  exists to serve was exactly the class it could not survive. Fixed with an `isinstance`
  guard. Worth keeping: the reorder was itself a fix for a real defect, and it introduced a
  new one in the same lines — which is why the independent halves were re-run against the
  post-fix implementation rather than the version they were written against.

- 2026-07-20 — **the two suites were reconciled against the implementation, not the reverse.**
  Because the defects were fixed while the halves were being written, eleven of their tests
  had pinned the *defective* behaviour as expected — the green-light trap, arriving from the
  direction nobody warns about. Each was re-pointed at the correct behaviour and each
  `@unittest.expectedFailure` marker was removed, so every one is now a live regression rather
  than a documented defect. Two tests calling the old three-argument `verify_member_bytes` were
  rewritten; the named-code inventory was updated for four added codes and one removed
  (`MEMBER-UNVERIFIED`, which the reader-less design makes unreachable and therefore dishonest
  to keep).

- 2026-07-20 — **every guard fixed this round was mutation-verified**, not merely re-run
  green: member-read-by-pinned-revision, blank-executor, partial-CheckResult-omission,
  FINAL-decision-target, pointer coverage, and repair-boundary-unverified were each neutered
  in place, the suite confirmed red, and the source restored from a byte-checked scratchpad
  copy — never `git checkout --`. Every restoration verified byte-identical, control green
  before and after. The four user-facing renderings were mutation-verified the same way
  earlier in the node.

- 2026-07-20 — `rsc v3 review` added, closing the observation that `check_package`,
  `verify_member_bytes` and `check_review_result` had **no caller anywhere in the repository**.
  The N1-R2 lesson applies to this node's own code: a check nobody can invoke is a check that
  will eventually not be run.

- 2026-07-20 — **the independent FULL happened, and this is the one bounded fix that answers
  it.** Budget: **FULL used (1/1). This fix round used (1/1). One targeted VERIFY remains
  (1/1).** The reviewer returned one blocker and seven findings against `0ba649c`; the user
  approved a boundary covering the blocker and F1–F6, with F7 to be disclosed rather than
  built. **Every item was reproduced against the candidate before being acted on** — reproduced
  to write the fix correctly, not to adjudicate the reporter — and all eight were real.

  **B1 — the blocker. Nothing compared what a VERIFY claims to have covered against what the
  user approved.** `accepted_finding_ids` appeared exactly once in the four modules, in the
  REPAIR→FULL direction (an approved finding must exist in the FULL); the VERIFY→REPAIR
  direction existed in neither code nor tests, and `check_verify_outcome` never received the
  decision at all. A reviewer could declare it had covered finding C where the user approved A
  and B, and every digest, summary and other check still verified. This is the same shape as
  the defect this node had already called its second worst — the user's decision target
  compared to nothing — one step later in the flow. Fixed by giving
  `check_verify_outcome` a **required** `repair_decision` and reporting both directions of set
  difference, plus `V3-FLOW-VERIFY-WITHOUT-REPAIR` when the decision was not a repair at all.

  The reviewer also pre-empted the defence I would have reached for — that a `ReviewResult` is
  reviewer-owned and declaring the scope is itself the acceptance — and the rebuttal is
  correct on this node's own standard: the module already validates the other two VERIFY-scope
  booleans, and of the three things V3-D6 scopes a VERIFY to, this is the only one with a
  second document to reconcile against. Leaving it unreconciled was the weakest point of the
  set, not a principled ceiling.

  **F1/F2/F3 — the same class the node had already hit, in the places it had not looked.**
  Both earlier crash fixes were **unlocked**: reverting either left all 176 tests green, and
  neither named code appeared anywhere in the suite. Three further crashes of that class
  survived (`check_transition` missing `status` — the sibling line of the one that *was*
  fixed; `governance_scan` as a truthy non-mapping in two functions), plus one more fail-open:
  `check_repair_decision` silently skipped the "repair binds the reviewed candidate" guard
  whenever the review named only a branch, and raised outright when it named no candidate.
  Fixed; the guard now reports `V3-FLOW-REPAIR-BINDING-UNVERIFIED`, matching what the boundary
  check beside it and `check_package` already did for the identical situation.

  **F5 — `rsc v3 review` tracebacked on exactly the input it exists to report on.** A
  schema-invalid package reached `verify_member_bytes`, which walks `package["members"]`.
  Fixed by gating byte verification on the package being well-formed; the schema failure *is*
  the finding.

  **F6 — self-describing prose that had become false.** Three docstrings still claimed
  `@unittest.expectedFailure` markers and methods that no longer existed, and one cited a code
  this node had deliberately deleted. Repaired by deleting text, which is the only repair this
  class accepts (N0 spent five levels learning that adding prose about prose does not
  converge).

  **F4 — and the finding that was about the tests rather than the product.** The named-code
  inventory swept `review.py` only; the other three modules were checked against a
  hand-written list with a subset assertion, so a code missing from the list was never checked
  at all. The cost was already real: two codes existed that no test anywhere named. Replaced
  by a sweep that reads the codes out of all four modules and requires each to be named by
  some test — which covers codes nobody has thought of yet, as a hand-written list cannot.

  **The fix for F4 initially contained F4.** Mutation testing caught it: shrinking the swept
  module list to one entry left the suite green, because the coverage test iterated the very
  list it was meant to be checking. A partition assertion against the package directory now
  pins the scope, and that assertion was itself mutation-tested — as was the extraction regex,
  by making it match nothing.

  **All seven guards were mutation-verified**, each neutered in place, the suite confirmed red,
  and the source restored from a byte-checked scratchpad copy — never `git checkout --`. Two
  of my own probes were wrong before they were right (a one-character actor name that failed
  schema validation, and an `or` mutation that evaluated to the original expression); both are
  worth recording, because a mutation that does not actually mutate reports "no teeth" for a
  guard that has them, and the opposite mistake would have been invisible.

- 2026-07-20 — **targeted VERIFY returned `PASS`; user signed V3-N2** (Melclycj). Signed
  candidate: `23ac473` (`V3-N2-REVIEW-FIX1-CANDIDATE-v1`), node base `1e34a1e`, with the
  out-of-node amendment `8efe3e9` beneath it. Plan §8 budget at close: **FULL 1/1, fix 1/1,
  VERIFY 1/1 — fully spent.** The signature is recorded here, in this append-only log, and
  this record carries no approval field of its own — the R4 rule made mechanical at N1,
  applied to the record that inherits it.

  **What this signature is recorded as covering, and what it cannot show.** The verdict and
  the signature reached the execution session as a single instruction. The reviewer's own
  VERIFY report is **not in the repository**, so this record cannot show its scope, its
  method, or what it examined — it states that the trust terminal issued `PASS` and signed,
  which is what the execution session actually knows. V3-N1 hit the mirror image of this: a
  VERIFY that *had* happened was recorded as not having happened, and needed an errata to
  correct. Recorded as residual N2-R7 so the gap is visible rather than implied, and so a
  later reader does not mistake the absence of a report for the absence of a review.

  This signature closes **V3-N2 only**. It promotes nothing: the candidate stays on
  `document-work-assurance-v3`, unmerged and unpushed.

## 9. Carried-forward residuals

| # | Residual | Owner node | What must actually land |
|---|---|---|---|
| N2-R7 | **The VERIFY report that closed this node is not in the repository.** The verdict reached the execution session as an instruction; its scope and method are therefore unrecorded, and the review contract's own rule is that load-bearing material existing only in chat is itself a finding | **user** | Either the reviewer's VERIFY report is landed under `N2/**` by a later out-of-node commit, or this row stands as the permanent statement of what the signature rests on. Recorded rather than smoothed over because V3-N1 hit the mirror image — a VERIFY that had happened, recorded as not having happened — and needed an errata to fix |
| N2-R6 | **8 of the 14 V3-N2 checkers have no caller in the repository** — `check_repair_decision`, `check_repair_regeneration`, `check_verify_outcome`, `check_assurance_candidate`, `check_summary`, `check_issue`, `check_triage`, `governance_disclosures` are referenced only by tests. Raised as FULL finding F7; disclosed here rather than built, on the user-approved fix boundary | **V3-N3** | Nothing at this node. The N1-R2 lesson applies — a check nobody can invoke is a check that will eventually not be run — and `rsc v3 review` applied it to three functions while these eight were left in exactly the state that lesson describes, which the record did not previously say. The honest resolution is not more CLI surface invented now: V3-N3's shadow runs are what will show which of these a real run actually reaches, and a wrapper built before that would be guessing at the call site |
| N2-R5 | **Two test files exceed the global 800-line rule** — `test_flow_repair_disposition.py` at 2115 lines and `test_package_and_review.py` at 1344. Every implementation module is inside it (`review` 730, `flow` 626, `summary` 406, `issues` 240) | **user** | A decision, not a silent deviation. The suite's own convention already exceeds the rule — N1's signed `test_candidate_checks.py` is 1753 lines — and the repository's split tripwire says *propose to the user, never auto-split*. Splitting late, after the reconciliation pass, would also risk breaking a matrix that is currently green and mutation-verified. Recorded here rather than acted on |
| N2-R3 | **`CHECKS-OMITTED` compares the number of CheckResults, not the set.** A package including the right *count* of results but the wrong ones is not detected. The sibling source-input guard is exact per path; this one cannot be, because a CheckResult document carries no storage path to match on | **not scheduled — a stated limit, not debt** | Nothing, unless a later node has reason to change how results are stored. The two ways to close it are both worse: putting a path inside a CheckResult duplicates a canonical fact (N0-A6), and taking the paths from the caller trusts the caller for exactly the completeness this check exists to establish. The limit is recorded in the code beside the guard |
| N2-R4 | **`check_repair_regeneration` proves regeneration by digest inequality alone.** A C2 that *dropped* every CheckResult passes it, because the function can see what changed but not what should exist | **V3-N3** (observe in the shadow runs) | Whether this matters in a real run. If a shadow run produces a C2 with fewer checks than C and nothing notices, the fix is to compare the expected check set from the resolved plan rather than the digests. Recorded rather than built now, because the plan's own check order is the natural source and inventing that coupling without a witnessed case would be speculative |
| N2-R2 | **`document-harness/README.md` still says "V3-N1 is not yet authorized and no runtime exists yet".** That went stale when N1 closed — N1's own allowlist did not include this file either, so no node has been able to correct it. This node's allowlist permits **interface links only**, so the interface table was updated and the status paragraph deliberately was not | **user** (a narrow out-of-node commit, as at §2.1) or **V3-N4** | One sentence. It is recorded rather than quietly fixed because "interface links only" is an explicit boundary, and a status paragraph is not an interface link. Worth doing before the file is read as current: the new V3-N2 interface rows now sit directly beneath a line asserting V3-N1 was never authorized |
| N2-R1 | ~~`SPEC_GAP` (§2.1) — plan §9's V3-N2 schema list and N1's pinned schema-directory assertion cannot both hold.~~ **DISCHARGED by user ruling 2026-07-20**, via the out-of-node amendment `8efe3e9`; both directions mutation-verified, suite green at 113. Sharpened rather than deleted: the register is cumulative and why a row died is the auditable part | **none — discharged** | Nothing. The collision class is worth remembering, though: a guard that pins a *count* of a directory the plan itself keeps adding to will misfire at the next node. §9 rows below should be read for that shape |
