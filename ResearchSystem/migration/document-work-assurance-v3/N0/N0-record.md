# V3-N0 administrative record — transition boundary and core contract

Node: `V3-N0` of [[document-work-assurance-harness-v3.plan|the v3 plan]] §9. Sole writer: the
execution session.

Write rules for this file, stated precisely because an imprecise version of this sentence was itself
caught by review: **§8 is the append-only log** — entries are added, never rewritten or reordered.
**§9 is a cumulative register** — rows are appended and existing rows may be sharpened when a later
finding changes what must land; every such row addition or provenance clarification is itself logged
in §8. §§1–7 record the node's own facts and are not rewritten once the node closes. Nothing here
weakens the rule that signed contract and approved plan bytes are never modified.

## 1. Plan approval binding and branch base (N0-A1)

- **User approval (2026-07-20, Melclycj):** "我批准以下计划的精确版本" binding file
  `.goals/plans/document-work-assurance-harness-v3.plan.md` at SHA-256
  `9B08CD0038FA0C36E76674B7CE386129D9797EFFE5CEC7FABBF69699811F171F`.
- **Verification before work:** worktree file hash and Git status matched; recorded in-session.
- **Approved plan Git blob:** `8ad404b12b3242e700d0ad215048dffccada7d9c` (blob bytes SHA-256
  re-verified identical to the approved hash — no normalization drift).
- **Plan-boundary commit:** `V3-PLAN-BOUNDARY-v1` = `ebbc304ffbb882826c18da9f9da93e40fece973c`,
  sole change = adding the approved plan bytes.
- **Branch base:** `document-work-assurance-v3` created from accepted A3 closeout
  `7db177de9fd3c81e872dccd76cbbdfaba8925e02` (`A3-ADMINISTRATIVE-CLOSEOUT-v1`). The A4 line is not
  in this branch's history.
- **Rollback:** delete/ignore branch `document-work-assurance-v3`; the v2 line
  (`codex/research-system-stage-control-refactor` at `de39b3d`) and all v1/v2 history remain intact.
  No old file is deleted by v3 (plan §3 OUT, §11).

## 2. A4 disposition (N0-A2)

A4 (base candidate `3150919`, accepted fix `f91a7c45fe6d6a920f03ac0e33b7baed7d034d58`, closeout
`de39b3d`) is **accepted v2 history, historical-only-for-v3**: its commits remain reachable source
material for inspection, but v3 has no A4 import, no A4 physical base and no A4 default dependency.
Any v3 use of A4 material must pass through the §4 reuse process below (currently: read-only
consultation for the two N2-scoped primitives).

## 3. Historical-only default (N0-A3, part 1)

Every old root defaults to historical-only for v3. Explicitly: `ResearchSystem/harness/**`,
`ResearchSystem/schema/harness-v2/**`, `ResearchSystem/migration/general-harness-v2/**`,
`ResearchSystem/generated/harness/**`, the v1 stage-control line (`ResearchSystem/contract/
Stage-Control-Contract.md`, `stages/`, v1 schemas/tests), and all `rsclib/harness` modules not
nominated in §4. Referencing any non-nominated old component from v3 code or records is `SPEC_GAP`
until the plan's dependency map is amended (plan §7). The untracked parallel-agent file
`ResearchSystem/docs/General-Harness-v2-Design.md` stays untracked and outside this candidate (user
ruled ignore, 2026-07-20 LEDGER note); if later retained it receives a historical banner only.

## 4. Nominated reuse decisions (N0-A3, part 2)

Only these five primitives were nominated by plan §7. Decisions:

| # | Primitive | Old asset (location) | Decision | Where | Exact tests binding the decision |
|---|---|---|---|---|---|
| 1 | Canonicalization / content binding | `rsclib/harness/c14n.py` (on v3 base) | **adapt** | V3-N1 | N1 golden digest tests (same input → same digest; delete+rebuild of `ResolvedAssurancePlan` byte-identical); retained v2 c14n unit tests stay green (N1-A11) |
| 2 | Closed JSON-schema validation | `rsclib/harness/schemas.py` + A2 fixture-runner pattern (on v3 base) | **adapt** | N0 (done) + V3-N1 | N0 contract fixture suite green — result §5; N1 runtime-validation negatives (unknown field / unknown enum rejected) |
| 3 | Git path/diff observation | `rsclib/harness/gitadapter.py` (on v3 base) | **adapt** | V3-N1 | N1 manifest goldens (actual add/modify/delete captured); out-of-boundary diff negative (N1-A9); retained gitadapter regression tests stay green (N1-A11). Enforcement-level vocabulary and lease logic are stripped, not carried |
| 4 | Frozen review-subject binding | A2 `review.schema.json` pattern (on base) + A4 `review.py` (source material only) | **adapt** | V3-N2 | N2-A1 negatives: summary-only substitution fails; package-digest mismatch fails. A4 code is consulted read-only, never imported |
| 5 | One-repair / VERIFY limit | v2 §6.4 bounded convergence + A4 `feedback.py` (source material only) | **adapt** | N0 (schema) + V3-N2 | N0: `repair_cap` const 1 + `repair_round` enum [0,1] fixtures (NEG-plan-repair-cap-2 green); N2-A6 negative: second repair rejected; VERIFY covers findings + whole repair diff |

No primitive received `reuse` (verbatim import) — every old asset crosses into v3 through an
adaptation with its own tests. Nothing was `reject`ed outright; rejection of the *non-nominated*
surface is the §3 default.

## 5. Deterministic results (N0-A9 evidence)

- Contract fixture suite: `fixtures/validate_fixtures.py` → **41/41 green, exit 0**
  ([results/fixture-run.txt](results/fixture-run.txt)): 13 positive + 21 negative schema cases + 7
  cross-document checks (no-profile absence, unit↔obligation bidirectionality, surface-vocabulary
  neutrality N0-A5/A8, resolved-plan non-duplication N0-A6, state pointer-only shape).
- Fixture digests/revisions are shape-valid placeholders; digest recomputation is an N1 obligation
  (same honesty boundary as the v2 A2 runner).
- Repository audit: `python Thesis/Work/Tooling/repo-audit.py` → **exit 0, RESULT: clean**, in-scope
  **247 markdown files**. All hard checks green (broken links / source_trace / wikilinks 0; KB
  one-way 0; status-tag, register↔block and >800-line tripwires 0). Soft-only findings remain: 55
  orphan notes and 4 cross-listed PDFs, none introduced by this node.
- Changed-path allowlist: `git diff --name-only ebbc304 <this candidate>` → **49 paths, zero
  out-of-boundary**. Each path was classified against the plan §9 V3-N0 allowlist: `.goals/LEDGER.md`
  (1, thin pointer) · `.goals/plans/general-harness-v2-architecture-revision.plan.md` (1, historical
  banner + pointer fields only) · `ResearchSystem/contract/Document-Work-Assurance-Contract-v3.md`
  (1) · `ResearchSystem/schema/document-assurance-v3/**` (7, exactly the nominated schema files) ·
  `ResearchSystem/document-harness/README.md` (1) ·
  `ResearchSystem/migration/document-work-assurance-v3/N0/**` (38 = this record + 34 fixture
  documents + `cases.json` + runner + fixture-run result). No path fell outside these buckets, and
  no controller/tooling code,
  A4 import, business content or old-file deletion appears in the diff.

## 6. Authored-field traceability (N0-A7)

Each authored field maps to a locked decision and an observed failure mode from this repository's
own history (no speculative ablation catalogue):

| Authored surface | Locked decision | Observed failure mode it answers |
|---|---|---|
| `work_id`, `objective` | V3-D1 | resume ambiguity across sessions (stale-pointer incidents, LEDGER 2026-07-11 reviews) |
| `instruction_ref` + `instruction_units` (obligation/context + rationale) | V3-D7 | silent omission of instruction content — v2 A1 rev1 `SPEC_GAP`; "every consumption surface" overstatement caught only by a sweep (LEDGER 2026-07-11 fourth review) |
| `inputs` (frozen revisions) | V3-D5, plan §6 step 1 | reviewing against drifted ground truth (wrong-subject class, v2 A1 bootstrap incident §6.5) |
| `document_assurance_profiles` (optional, leaf refs + parameters) | V3-D2 | empty-placeholder/mega-template burden proven in v1 monolith and v2 A1 ablation; parameters sit in the WorkSpec because task-local data may not enter a profile |
| `change_boundary` (write_scope + out) | V3-D3 | unrelated-file mutation — the 2026-07-11 `git checkout --` clobber incident; v2 scope-tripwire history |
| `expected_artifacts` | invariant 7 | claimed-but-absent artifact (unsupported completion claims) |
| `obligations` (+ `verification_mode`, `local_check_refs`) | V3-D7, invariant 8 | "done" without evidence — the recurring verify-before-claiming-complete failure class (global hard rule 5; LEDGER lessons) |
| Profile: `rule_family`, `owner`, `reason_to_change`, `reuse_witnesses` (min 2) | V3-D2 | speculative profile growth — v2's five-profile catalogue built before any real reuse existed |
| Audit: closed `COVERED/SPEC_GAP`, findings, distinct auditor | V3-D7 | self-certified coverage; the P4 amendment monolith needed four external review rounds to expose spec swelling (2026-07-17) |
| UserDecision: closed phases/decisions + exact targets | V3-D4 | approval ambiguity — v2 A1 duplicated-disposition incident; "which bytes did I approve" |
| State: closed statuses + pointers only | V3-D8 | cold-resume failure and copied-evidence drift (v1 monolithic StageRecord lesson, A0 inventory) |
| ResolvedAssurancePlan: refs + deltas only, `repair_cap` 1 | §5.2, V3-D6, N0-A6 | duplicated canonical facts drifting apart (v1 StageRecord); unbounded repair loops (P4 monolith 2026-07-17) |

## 7. Node status

- Payload complete: Contract v3, 7 schemas, document-harness README, this record, fixtures+results,
  v2-plan historical banner, LEDGER thin pointer.
- **Stop gate: CLOSED.** Semantic review returned `PASS` with three non-blocking residuals; the user
  signed off N0 on 2026-07-20 (§8). **V3-N1 is not yet authorized** — it requires an explicit user
  authorization at the start of the next session. Nothing in this node authorizes implementation code.

## 8. Append-only log

- 2026-07-20 — record created with the N0 candidate `V3-N0-TRANSITION-CONTRACT-CANDIDATE-v1`.
- 2026-07-20 — FULL review returned `CHANGES_REQUIRED`; the user accepted a bounded fix with an
  explicit fix boundary (3 files / 4 edits; schemas, contract body, fixtures, results, README and the
  approved plan bytes forbidden). Fix candidate `V3-N0-REVIEW-FIX1-CANDIDATE-v1` = `85742ae`:
  (1)+(2)+(3) v2 `A5–A7`/cutover restated as **parked** (never started, no automatic continuation,
  resuming needs explicit user authorization) in `.goals/LEDGER.md`, the v2 plan banner and its
  `current node` field; (4) this record §5's dangling "candidate report" pointer replaced with inline
  measured evidence. Re-verified at the fix candidate: fixtures 41/41 exit 0; repo-audit exit 0
  (247 in-scope); 49 changed paths, zero out-of-boundary; `9237960..85742ae` touched exactly the
  three authorized files.
- 2026-07-20 — **VERIFY `PASS`. User signed off V3-N0** (Melclycj), independently reproducing the
  three checks rather than accepting the reported numbers. Three residuals were recorded as
  non-blocking and **carried forward to N1/N2** (§9). This signature closes N0 only; it does not
  authorize V3-N1, implementation code, cutover or P4.
- 2026-07-20 — **signature subject binding (appended after a post-signature audit found the binding
  missing).** The contract's own warning block promises that the signature is recorded here "binding
  this file's exact Git blob", but the entry above named no blob. Recorded now:
  - **signed contract blob:** `b2dbdf752d8c155e4c65b14b5f420b880b8184a1`
    (`ResearchSystem/contract/Document-Work-Assurance-Contract-v3.md`);
  - **signed payload candidate:** `85742ae` (`V3-N0-REVIEW-FIX1-CANDIDATE-v1`);
  - **closeout recording the signature:** `9bda771` (`V3-N0-ADMINISTRATIVE-CLOSEOUT-v1`);
  - **date:** 2026-07-20.

  **Three-point blob identity — the reviewed object and the signed object are the same bytes.** The
  contract blob is identical at the original candidate `9237960`, at the reviewed/signed fix
  candidate `85742ae` and at the closeout `9bda771`; the bounded fix never touched contract bytes.
  Reproduce with one command, which must print the same hash three times:

  ```text
  git rev-parse 9237960:ResearchSystem/contract/Document-Work-Assurance-Contract-v3.md \
                85742ae:ResearchSystem/contract/Document-Work-Assurance-Contract-v3.md \
                9bda771:ResearchSystem/contract/Document-Work-Assurance-Contract-v3.md
  ```

  **Errata — contract frontmatter `status:`.** The signed contract's frontmatter carries
  `status: candidate-awaiting-user-signature`. This is an **authoring residue**: it contradicts the
  same file's warning block and §14, which state that the file never carries its own approval status
  and that the signature lives here instead. **This record is authoritative for the contract's
  approval state**, and the frontmatter field must not be read as current. The errata explicitly
  **does not** constitute grounds to modify contract bytes — amending a signed contract in place is
  forbidden (§13); the field may only be removed by a versioned successor if one is ever issued for
  an independent reason. See §9 R4 for the deterministic check that must exist so this class of
  self-carried approval status is caught mechanically rather than by audit.
- 2026-07-20 — **post-signature review of the errata itself returned three further findings; R4's
  specification was sharpened and this file's write rules were corrected.** No signed or approved
  bytes were touched and no review was reopened.
  - **R4 was unimplementable as first written.** The check it demanded would permanently fail the
    approved plan (`8ad404b…`, line `status: candidate-plan`) and the signed contract
    (`b2dbdf75…`, line `status: candidate-awaiting-user-signature`) — both immutable by plan
    §0/§11 and contract §13. N1 would have been forced either to relax the standard (violating the
    hard rule "a correct check is never loosened") or to add an unrecorded ad-hoc exemption. R4 now
    mandates a **blob-keyed, enumerated grandfather list** recorded in the N1 node record.
  - **R4 would also have produced false positives on the correct pattern.** `approval_status_owner`
    (plan) and `signature_owner` (contract) delegate ownership without carrying state — the very
    behaviour the rule wants. R4 now mandates exact field-name matching with an explicit `*_owner`
    whitelist, never substring matching.
  - **A third false-positive class was found while writing the errata above:** it quotes the literal
    field text inside backticks, so a raw-text scanner would flag this record for documenting the
    defect. R4 now scopes the check to parsed frontmatter keys, not text search.
  - **This file's own append-only claim was literally false.** The preceding errata commit rewrote
    §9's heading and intro (provenance of R1–R3 vs R4) while the header asserted that later entries
    never rewrite earlier sections; adding a table row cannot be done by pure append. The substance
    of R1–R3 was never altered and every change is visible in Git, but the self-claim did not match
    the behaviour — the same defect class this node has been chasing. The header now states the real
    rule: §8 append-only, §9 a cumulative register whose row additions and clarifications are logged
    here, §§1–7 not rewritten after closure. This entry logs both that header correction and the R4
    sharpening above.

## 9. Carried-forward residuals (non-blocking)

R1–R3 come from the N0 VERIFY, recorded verbatim in substance from the reviewer. **R4 was found
later, by a post-signature audit of this record's own binding — no check produced it**, which is
itself the reason R4 exists. None is a defect of the signed interfaces; each is a real limitation of
this node's evidence or of its guards.

| # | Residual | Owner node | What must actually land |
|---|---|---|---|
| R1 | `repo-audit.py` observes the **working tree**, not the candidate commit tree (the two differed only by the ignored untracked `ResearchSystem/docs/`, and the reviewer reproduced identical numbers under identical conditions — so no discrepancy here, but `247` is a worktree-scoped figure) | **V3-N1** | Any deterministic check that inspects repository content must record **which tree it observed** (candidate commit vs worktree) in its `CheckResult`. A check whose subject is the payload candidate must observe the candidate tree; observing the worktree instead is a wrong-subject class defect (V3-D5). Applies first to `git_diff_boundary` and `command_exit` |
| R2 | `AssuranceWorkState` has no **status↔pointer conditional requirement**: `status: CLOSED` with no `summary_ref` still validates | **V3-N2** (already scoped by `N2-A7`) | A real negative fixture must exist and fail: terminal status without its required pointers (`CLOSED` without `summary_ref`/`final_decision_ref`; `AWAITING_FINAL` without `assurance_candidate_ref`; `repair_round: 1` without `repair_decision_ref`). `N2-A7` is not satisfied by prose — it needs the failing case |
| R3 | The `X-SURFACE-VOCAB` guard is **blind to `const` literals**: it scans property names, nested `$defs`, `if/then` properties, `required` lists and `enum` values, but never `const` | **V3-N1** | Extend the vocabulary scan to `const` values before any N1 schema expresses an enumerated surface via `const`. Until extended, `const` is an unguarded path into the forbidden-vocabulary surface (N0-A5/N0-A8 would silently pass) |
| R4 | **A contract/plan-class file can carry its own approval status and nothing catches it.** The signed contract's frontmatter says `status: candidate-awaiting-user-signature` while its own body forbids exactly that; the N0 fixture suite passed because no check looks at governance-document frontmatter. Found by post-signature audit, not by a check (§8 errata) | **V3-N1** | A deterministic check must reject a governance document (contract / plan / signed interface record) that **carries** a self-referential approval field — `status`, `approval_status`, `approved`, `signed`, `signature`, or a digest of itself. The rule already exists in prose (contract §14, plan §0: never write approval status into the approved bytes); N1 must make it mechanical. **Three specification constraints are mandatory — the naive version of this check is unimplementable and would force either a relaxed standard or an undocumented exemption:** **(a) scope = parsed frontmatter keys (and structured fields), never a raw-text scan** — §8's errata quotes the literal string `status: candidate-awaiting-user-signature` inside backticks, so a text scanner would flag this very record for *documenting* the defect; **(b) exact field-name match, never substring** — `approval_status_owner` (plan) and `signature_owner` (contract) are the **correct** pattern: they name who owns the approval state without carrying it, and must PASS. Whitelist the `*_owner` suffix explicitly. A substring match on `approval_status` / `signature` turns the correct delegation into a false positive, and false positives are how a real check gets switched off; **(c) grandfather list keyed by exact blob, enumerated, never globbed** — the approved plan (`8ad404b12b3242e700d0ad215048dffccada7d9c`, carries `status: candidate-plan`) and the signed contract (`b2dbdf752d8c155e4c65b14b5f420b880b8184a1`, carries `status: candidate-awaiting-user-signature`) are permanently immutable (plan §0/§11; contract §13) and can never be brought into compliance, so without an exemption this check can never go green against the repository's own constitution. Blob-keyed exemption **fails closed**: edit the bytes and the blob changes and the exemption evaporates by itself, whereas a path/glob exemption would silently keep covering whatever that path later becomes. Each entry must name the immutability rule that forces it, and the list must live in the N1 node record — not inline in the checker. A passing fixture suite that never inspects the governance layer is not evidence that layer is clean |

A node that closes without discharging its assigned residual is incomplete, regardless of its own
acceptance IDs.
