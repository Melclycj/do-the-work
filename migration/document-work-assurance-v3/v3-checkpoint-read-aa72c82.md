# Amendment read — Phase A closeout (`aa72c82`)

Subject: `1ddece755a0f31488e7a82c0eb15604ef1bbb437..aa72c8274150c2286ee5a638bff41b3ba890c1ed`
(one commit, `V3-PHASE-A-CLOSEOUT-v1`). Round derived from the repository: the disposition batch
for the three must-fix and three low of [`v3-checkpoint-read-cf8e1b1.md`](v3-checkpoint-read-cf8e1b1.md),
which amended two checklist rules (`E10`, `R3`) and therefore owes the read E10 mandates. Plan
Step 3's closing clause and the plan's resume pointer (`:87`) name this dispatch.

**This is a read, not a FULL or a VERIFY.** E10: the read's *"subject is the amendment text
itself, never the work it governs, and it is never banked as the round's FULL."* Scope taken:
the two amended rules primarily, plus the whole diff and the permanent boundaries — the precedent
the previous read set, and the only independent look this batch gets. Findings are tiered
must-fix / low / observation.

Two notes on standing, both consequences of R2 rather than choices:

- The ledger (`:22`) and the plan (`:87`) both characterize this dispatch as a *"短 read"* of
  *"收口轮那两行 checklist 改动"*. Under R1 the executor does not set the reviewer's question, so
  the two-line framing was not treated as scope. It did not change the outcome — every finding
  below is inside the amendment or inside the diff.
- The new R3 clause defines what a read is, and this read must know its own standing to open. It
  cannot rely on an amendment it has not yet passed, so the position was established independently
  from source review §12 at `7011916` (`rev.md:335-337`), which carries it verbatim in substance.
  The circularity is unavoidable at the first read after such a clause lands; it is on record here
  rather than resolved.

## Subject re-derivation

| Item | Re-derived value |
|---|---|
| tip == `HEAD`, branch | `aa72c8274150c2286ee5a638bff41b3ba890c1ed`, `document-work-assurance-v3` |
| range contents | exactly one commit; parent is `1ddece7`, the read record it disposes |
| changed paths | 3 (3 M) — plan, `HARNESS-LEDGER.md`, `CONSTRUCTION-CHECKLIST.md`; classified by hand below |
| line churn | +11 / −8; `--ignore-all-space` diffstat identical, so no whitespace-only edit is hiding |
| worktree | clean except untracked `ResearchSystem/docs/General-Harness-v2-Design.md` (Phase D disposition; mtime 07-19, unchanged, not smuggled) |
| suite | `432 passed in 48.88s` — re-run; matches the claim and matches `cf8e1b1`'s 432 |
| repo-audit | `RESULT: clean (exit 0)` — re-run, matches the claim |
| plan blob | `8ad404b12b3242e700d0ad215048dffccada7d9c` ✓ · contract `b2dbdf752d8c155e4c65b14b5f420b880b8184a1` ✓ · supersession-1 `68031fa2ca31272e31da0d42a9a02189d28fcc21` ✓ |
| both user-locked oracles + `schema/document-assurance-v3/` + `ResearchSystem/contract/` | `git diff` empty across the range ✓ |
| checklist content lines | **64** (E1 at `:16` through `:82`, less 2 blanks and the one heading) — the commit's "62 to 64" is exact; previous count re-derived at `1ddece7` = 62 ✓ |
| compression baseline | `7011916` op 308 + rev 375 = **683** ✓; 64/683 still rounds to −91%, so the plan's percentage survives the move |
| rule inventory | E1–E12 + R1–R8 ✓; draft at `2b5fa28` was E1–E12 + R1–R7 ✓, so Step 2's new *"[起草时为 R1–R7]"* is accurate |
| ledger pointer block | 53 non-blank lines against its own *"≤ 30 行"* (`:17`); was 52 at `1ddece7` |

Per-path classification: checklist (`E10` membership + `R3` read definition — the two amended
rules), plan (`:46` freeze surface, `:63` Step 2 annotation, `:87` resume pointer), HARNESS-LEDGER
(`:19-21` status line re-dated and chained, `:22` NEXT repointed). All inside the round's declared
boundary as that boundary now reads — see MF-3 and L-3 on the boundary itself.

### Disposition of the previous read, checked one by one

| Prior finding | Disposition | Verified |
|---|---|---|
| MF-1 ledger pointer stale | fixed | `:19` re-dated 07-28 + chain; `:22` now points at Phase B's preview card ✓ |
| MF-2 plan `:46` freeze over-breadth | fixed | `.goals/plans/` 既有文件 → 签名 plan blob `8ad404b1` 本身; now matches E2's list exactly (3 blobs + N0 schemas + `contract/`) ✓ |
| MF-3 read type undefined | fixed | new R3 clause ✓ (fidelity below) |
| L-1 stubs outside E10 | fixed | both stub paths named in E10 ✓ |
| L-2 plan Step 2 stale | fixed | R1–R7→R1–R8 with drafting-time note; the *"reviewer 可建议删除"* phrase struck and annotated with its reversal; attribution to read `820b287` MF-2 checked against that record and correct ✓ |
| L-3 no record that the amendment was read | declined, recorded in the commit body | the decline and its reasoning are in a committed, greppable record, which is where the ledger header (`:11-15`) says narrative belongs — not a finding |
| observations 1–8 | no fix owed | obs 3 (ledger ≤30) grew by one line; obs 4 (`plan:6 status: planned`) and obs 5 (`dispatch.py:362`) unchanged — all still carried |

### Fidelity of the two amendments, against source at `7011916`

- **E10 membership.** Source op.md:249-251 — *"the prose that steers every human and agent in this
  system: `document-harness/README.md`, `EXECUTION.md`, `REVIEW.md`, these two operating contracts,
  and any versioned successor to signed prose."* The amended E10 is that list with the checklist
  added as the successor and the two contracts named at their stub paths. Restoration, not
  authoring ✓. One addition is not source-carried — see L-2.
- **R3 read definition.** Source rev.md:335-337 — *"Neither read is a round in §3's sense: it
  consumes no plan-§8 budget and carries no node verdict; its output is findings in a review-side
  note, routed by the user like this file."* The amendment carries the first three clauses
  faithfully (*"§8 budget"* generalized to *"budget"*, *"node verdict"* to *"verdict"* — both
  correct under the checklist's vocabulary). Two things did not come across: *"routed by the user"*,
  and the paragraph that immediately follows it in the same section. That paragraph is MF-2 below.

## Must-fix

**MF-1 — E9 forbids self-classification of what a round consumed and supplies no test to replace
it, and this commit is the instance.** E9 (`:39-41`): *"Budget per round: one FULL, at most one
user-approved fix, one targeted VERIFY … Never self-classify which round consumed what: every
recorded escape from the cap was a renamed round."* E8 (`:36-38`) tells the executor to *"name the
commit's kind — candidate / pre-submission correction / review fix / closeout / errata — so the
review side can attribute it without asking."* The two rules are in tension as compressed: E8 makes
the executor's label the review side's input, E9 forbids the review side from accepting a
self-classification, and nothing in the file gives the reviewer an independent criterion. Source
§3 (`rev.md:133-145`) is exactly that criterion, and it was dropped: *"What consumes budget is
**not** what a commit is called: **Has a valid independent FULL already occurred?** No → the change
is a pre-submission correction. Consumes nothing. Yes → the change is the fix round. Consumes the
fix and obliges the VERIFY … the discriminator above is applied to substance, never to the commit
message."* The consequence is live and concrete. This commit's title names the round `CLOSEOUT`;
its body opens *"Review fix:"* — two different E8 kinds on one commit — and it is the second fix
batch inside a round the plan declares to be *"一轮"* (`:63`), which on the checklist's face reads
as an escape from *"at most one user-approved fix"*. It is **not** an escape: no FULL record exists
for any Phase A sha (`ls migration/document-work-assurance-v3/` returns only
`v3-checkpoint-read-820b287.md` and `-cf8e1b1.md`), so under the source discriminator every batch so
far is a pre-submission correction consuming nothing. I could only establish that from a retired
contract. This is the second consecutive read forced into `7011916` to determine its own round's
standing — MF-3 of the previous read was the first. **Minimum fix:** one clause on E9 — what
consumes the fix is whether a valid independent FULL has already occurred; before it a change is a
pre-submission correction and consumes nothing, after it the change is the fix round and obliges
the VERIFY; applied to substance, never to the commit's name.

**MF-2 — the user ruling that ends read recursion was dropped, and this round is an instance of the
recursion it ended.** The amendment restores rev.md:335-337 and stops one line short of
`rev.md:340-346`: *"Wording-level findings from these reads are **banked, never rounds** (user
ruling 2026-07-27, ending a 2→1→0 read recursion): a finding is wording-level when its fix changes
no actor's action — no check outcome, no permission, no obligation, no verdict path — and the
accurate fact is already recoverable from adjacent text or a committed record. The test is to name
the downstream decision that goes wrong if it stays unfixed; if no decision can be named, the
finding rides the next batch that touches this layer and spawns no fix round and no read of its
own."* Nothing in the live layer carries this — `grep -i "wording-level\|banked"` across
`document-harness/`, the ledger and the plan returns E10's unrelated *"never banked as the round's
FULL"*, the ledger's *"banked HarnessIssue"* (a third sense), and the plan's *"清 bank"*. The plan
Step 2 discharges a bank (*"bank 以删除清偿"*) whose governing rule no longer exists anywhere live —
the MF-3 shape of the previous read, one level up. The instance: the previous read's **L-2** (a
stale descriptive phrase in an already-ticked Step) changes no actor's action and its accurate fact
was recoverable from the checklist itself; by the source test it was wording-level and should have
ridden the next batch. It instead spawned an edit in this commit, which owes this read, which
produces these findings. **Minimum fix:** one clause on R3 or E10 carrying the bank test — a
finding whose fix changes no actor's action and whose fact is already recoverable rides the next
batch touching this layer and spawns no fix round and no read of its own.

**MF-3 — the plan Note the user is routed to for a pending ruling states a figure this same commit
invalidated.** `plan:91`: *"**偏差（2026-07-28，Phase A 修复批次）：checklist 内容行 62，超
Acceptance 的「≤50」12 行** … 对比基线：两份契约 683 行 → 62 行（−91%）… **处置待用户裁**"*. The
count is now **64** and the overage **14** — re-derived independently, and stated correctly in this
commit's own body (*"Checklist content lines 62 to 64"*). `plan:87` sends the user to that Note for
the open ruling (*"待用户裁：checklist 行数 vs Acceptance ≤50（见 Notes）"*), so the ruling would be
made on the stale number. E3 is the rule the round applied to its own claims and not to the claim it
displaced: *"a figure is invalidated by any later change to what it measures."* Disclosed
counter-argument: both 62 and 64 fall under the Note's own proposed `≤65`, and the −91% baseline
survives the move, so one of the two offered dispositions is unaffected; the other (*"接受实测值"*)
would write 62 into the Acceptance. A decision can be named, so it is not bankable under MF-2's
test. **Minimum fix:** two numbers on `plan:91` — 62→64, 12→14.

## Low

- **L-1 — `"tiered findings"` is mandated and nowhere defined.** The new R3 clause requires a read's
  output to be *"tiered findings in its record"*; the checklist never names the tiers, while R3
  enumerates the FULL and VERIFY verdict sets precisely. The tiers exist only in the read records
  under `migration/`. By MF-2's own test this finding is **wording-level and bankable** — must-fix /
  low / observation is recoverable from every committed read record, and no actor's action changes.
  Recorded here rather than fixed, as the restored rule would require. **Minimum fix if taken:**
  three words on R3.
- **L-2 — the amendment adds rationale to a file that declares rationale absent.** E10's new
  membership clause carries *"(they route every reviewer)"*. The banner (`:9-11`) states *"Rationale
  is deliberately absent: every rule below was paid for by a recorded incident, and the records —
  not this file — hold the stories"*, and the 2026-07-27 narration-diet ruling in the ledger (`:35`)
  is *"rules 层不动，叙事是唯一反复出错的来源，砍它"*. The clause is true and four words long, and
  the source membership list carries no such parenthetical, so it is new characterization inside the
  rules layer. E9's rationale clause was checked by the previous read and found source-carried; this
  one is not. **Minimum fix:** delete the four words — the membership binds, the reason lives in this
  record and the commit body.
- **L-3 — the plan's freeze-surface declaration is load-bearing under E8 yet sits outside E10's
  layer, and this round is the precedent.** E8 obliges the executor to *"stay inside the round's
  declared change boundary"*; `plan:46` is what declares it; this commit edited `plan:46` and owes no
  read for it under E10 as amended. The edit itself is sound — it narrows toward E2, which had
  already passed a read, so no new authority was created — which is why this is low rather than
  must-fix. But the same argument that put the stubs into E10 last round (L-1: live routing prose
  outside the layer) applies unchanged to a line that decides which bytes are frozen. Not bankable
  under MF-2's test: its fix changes an obligation. **Minimum fix:** name the plan's freeze-surface
  declaration in E10, or state in E2 that plan-declared boundaries are derived from E2 and never
  independently authoritative.

## Observations — no fix owed

1. **Phase A has never had a FULL.** Only two checkpoint reads, which under the amendment carry no
   verdict. So the checklist that now governs every construction round has itself received no
   verdict from any round. This is *not* a defect against the plan: Acceptance `:82` accepts
   *"每轮有独立 review/read 记录"* — read records satisfy it by the plan's own words, and
   `plan:56`'s *"每轮独立 review"* is read down by it. Whether the instruction layer should carry a
   verdict before Phase B relies on it is the user's question; R5 bars me from concluding it.
2. **The *"three of the last four rounds on this file have been repairs of the repair"* figure is
   not re-derivable.** Carried from the previous read into this commit's body. Four commits touch
   `CONSTRUCTION-CHECKLIST.md` (`2b5fa28` draft, `820b287` diet, `cf8e1b1`, `aa72c82`); two of them
   are repair batches, and under the amendment the interleaved reads are not rounds at all, so no
   counting rule I can construct yields three. The **shape** the figure points at is real and
   unchanged: each batch on this file has so far generated the next. The count is not.
3. The ledger pointer block is 53 non-blank lines against its own *"≤ 30 行"* (`:17`); this round
   added one. Carried from the previous read's observation 3, which is where it was already noted
   that MF-1 of that read lived in the same over-long block.
4. `plan:6` still reads `status: planned` with Steps 1–3 ticked. Pre-existing, carried.
5. `dispatch.py:361-362` still attributes the numbered `§n` form to `v3-harness-review-contract.md`,
   which is now a five-line stub with no sections. Carried unchanged through three reads.
6. "Bank" now carries three unrelated senses across live files (E10's *"banked as the round's FULL"*,
   the ledger's *"banked HarnessIssue"*, the plan's cleared finding-bank), with the governing rule
   for the third deleted. Noted as context for MF-2, not as a separate finding.

## Negative results by dimension

Checked, found nothing: all three signed blobs intact and owned by the paths E2 names; both
user-locked oracles, `schema/document-assurance-v3/` and `ResearchSystem/contract/` diff-empty
across the range; no whitespace-only or invisible edit (`--ignore-all-space` diffstat identical to
plain); the three changed files are the whole change and each edit is inside the boundary as
declared; the E10 reflow (parenthetical → comma clause on the schema-`description` phrase) does not
move the clause's scope; the two stubs are five lines each, matching Acceptance `:79`, and both
links resolve with `7011916` still the correct full-text anchor; `README.md:24` still accurately
says *"E1–E12 execution, R1–R8 review"* after the R-count question raised by `plan:63`;
`EXECUTION.md:9-11` and `REVIEW.md:6-8` point at the checklist and are unaffected; the plan's
Step 2 attribution to read `820b287` MF-2 matches that record's MF-2 word for word; the ledger's
new chain (`820b287` → `3743849` → `cf8e1b1` → `1ddece7`) resolves — the two read shas are the
record commits, the two others the content commits; the commit body's four verification claims
(suite, audit, blobs, tree/oracle diffs) all reproduce.

## Guard probe (E4/R8) — run as a negative control

No test in the repository reads any of the three changed files: `grep -rn
"CONSTRUCTION-CHECKLIST\|HARNESS-LEDGER\|harness-deletion-first" ResearchSystem/tooling/` returns
nothing. Rather than mutate an unrelated guard, I mutated the subject itself to measure what the
round's own green evidence is worth:

- **Deleted E10 entirely** from the checklist (the amended rule) → suite **`432 passed`**, unchanged.
  The 432-green claim therefore carries *zero* information about this amendment. That is the source's
  own position about this layer (*"no schema validates it, no test reads it"*, op.md:252-254) and it
  is now measured on the amended bytes, not assumed.
- **Repointed a ledger markdown link** to a nonexistent file → repo-audit **RED**, `[!!] Broken
  markdown links: 1 - ResearchSystem\HARNESS-LEDGER.md`. So the audit-clean claim *does* bind the
  ledger's links, and nothing else about the ledger's content.
- Restored both files from sha256-checked scratchpad copies, never `git checkout --`:
  `253f8060…` / `6f3e661c…` before and after, worktree clean, audit back to `exit 0`.

Binding force, not sufficiency (R4): the audit binds link existence only.

## Coverage

**Read in full:** `CONSTRUCTION-CHECKLIST.md`; both source contracts at `7011916` (308 + 375 lines,
re-extracted); both stubs; the stabilization plan; `HARNESS-LEDGER.md` pointer block and rulings
block; `v3-checkpoint-read-cf8e1b1.md`; `v3-checkpoint-read-820b287.md` (MF-2 region and structure);
the full diff.
**Sampled:** `EXECUTION.md` / `REVIEW.md` (checklist-referencing regions); `document-harness/README.md`
(row 23-24); `dispatch.py` (the contract-referencing and hunt-list regions); the checklist at
`2b5fa28` and `820b287` (rule inventory only); `HARNESS-LEDGER-archive.md` (grep).
**Probed only:** the 432-test suite (run twice — clean and mutated); `repo-audit.py` (run three
times — clean, mutated, restored); the ledger and checklist under mutation.

**Recomputed, never accepted as reported:** suite count, audit exit, all three signed blobs and the
paths that own them, oracle and tree diffs, the checklist's 64 content lines and the prior 62, the
683-line compression baseline and the −91% it yields, the E1–E12 / R1–R8 inventory at three
revisions, the ledger block's line count at five revisions, the absence of a Phase A FULL record,
and the plan's citation of read `820b287` MF-2.

## Ceilings

The claim that this round ran in a fresh context is marked, not verified. The user's approval of
this batch's boundary is not visible to me as a repository fact for this specific commit — R7
applies: stated as a ceiling, not treated as a block. `UNVERIFIABLE`, not folded into supported:
whether 64 lines is *sufficient* governance is not establishable by reading them, and this read
adds the second and third data points against self-sufficiency (MF-1, MF-2) after the first
(the previous read's MF-3) — three consecutive reads have each had to open `7011916` to establish
something the live layer was supposed to state. That trajectory is the shape R5 tells me to report
and not to conclude; whether the compression target or the round structure is what should change is
yours to decide.
