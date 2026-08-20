# Amendment read — Phase A read-fix (`cf8e1b1`)

Subject: `3743849823ebe0cd68327957519a00ac41a2b907..cf8e1b1a9960e97b4d2803397f2861d1e9cb05bf`
(one commit, `V3-PHASE-A-READ-FIX-v1`). Round derived from the repository: the repair batch for
the six must-fix and six low of [`v3-checkpoint-read-820b287.md`](v3-checkpoint-read-820b287.md),
and the read that batch owes itself — plan Step 3's closing clause (*"修复批次按 E10 自身欠一次
amendment read（该条不可 waive）"*) and the plan's resume pointer name this dispatch. First round
performed under `document-harness/CONSTRUCTION-CHECKLIST.md`; its own subject is that file.

**This is a read, not a FULL or a VERIFY.** E10: the read's *"subject is the amendment text
itself, never the work it governs, and it is never banked as the round's FULL."* It therefore
carries no verdict — a position the checklist no longer states anywhere, which is MF-3 below.
Scope taken: the amendment text primarily, plus the whole repair diff and the permanent
boundaries (R3's VERIFY clause, applied because this is the only independent look the repair
gets). Findings are tiered must-fix / low / observation, the vocabulary every instruction-layer
read here has used. If the user instead classifies this dispatch as the round's VERIFY, the
honest verdict is `REVIEWED_NO_BLOCKER`: none of the three must-fix violates a signed clause or
an acceptance ID, so none is a blocker in R3's sense — but that classification is the user's.

## Subject re-derivation

| Item | Re-derived value |
|---|---|
| tip == `HEAD`, branch | `cf8e1b1a9960e97b4d2803397f2861d1e9cb05bf`, `document-work-assurance-v3` |
| range contents | exactly one commit; parent is `3743849`, the read record it repairs |
| changed paths | 7 (6 M, 1 D) — classified by hand below |
| worktree | clean except untracked `ResearchSystem/docs/` (Phase D disposition; unchanged, not smuggled) |
| suite | `432 passed in 52.08s` — re-run; matches the claim and matches `820b287`'s 432 (a guard with no tests was deleted, a README row added) |
| repo-audit | `RESULT: clean (exit 0)` — re-run, matches the claim |
| plan blob | `8ad404b12b3242e700d0ad215048dffccada7d9c` = `.goals/plans/document-work-assurance-harness-v3.plan.md` ✓ (path re-derived, not assumed) |
| contract blob | `b2dbdf752d8c155e4c65b14b5f420b880b8184a1` ✓ · supersession-1 `68031fa2ca31272e31da0d42a9a02189d28fcc21` ✓ |
| both user-locked oracles + `schema/document-assurance-v3/` + `ResearchSystem/contract/` | `git diff` empty across the range ✓ |
| checklist content lines | **62** (E1 at :16 through :80, less 2 blanks and the one heading) — the disclosed figure is exact; 20 rules, E10 the longest at 7 |
| compression baseline | `7011916` op 308 + rev 375 = **683** ✓ — the plan Notes' −91% is arithmetic on real counts |
| `tooling/hooks/` | directory gone entirely; no tracked live file references the deleted script |
| pre-commit hook (machine-local) | run: `EXIT=0`; `sh -x` shows `[ -f …contract_provenance_check.py ]` false → `exit 0`. The commit's existence-guard claim holds end to end |

Per-path classification: checklist (E2/E5/E8/E9/E10 + R3/R4/R5 — the twelve restored
obligations), `document-harness/README.md` (1 row added, 1 row narrowed), both contract stubs
(1 line each), plan (Step 2/3 tick + resume pointer + 2 Notes), HARNESS-LEDGER (2 ruling
bullets appended), `tooling/hooks/contract_provenance_check.py` (deleted, 57 lines, whole
file). All inside the round's declared boundary.

### Fidelity of the twelve restorations, checked word by word against `7011916`

Every one is a restoration toward source, not an re-authoring. Spot-checks that mattered:

- **MF-1 / E2** — source hard rule 5 (`op.md:174`) is *"Signed bytes are untouchable (approved
  plan, contracts, N0 schemas incl. `common.schema.json`)"*. It never contained `.goals/plans/`;
  dropping the blanket restores source scope, and the signed plan stays covered by blob. ✓
- **MF-2 / R5** — source §10 (`rev.md:275-284`): *"My subject is always the code that is
  there… When successive rounds on one artifact keep adding components to close findings, say so
  as an observation. I cannot conclude it should go."* The new R5 is that, direction intact. ✓
- **MF-5 / R3** — source §5.4 (`rev.md:181`): *"VERIFY is scoped to the accepted findings plus
  the whole repair diff — the boundaries are checked regardless."* ✓
- **MF-6 / E10** — source execution rule 1 (`op.md:262`) and §12 (`rev.md:337`). Both directions
  are carried: the read cannot be the FULL (stated), and the FULL cannot be the read (entailed
  by the subject clause). ✓
- **L-4 / R4** — source §10's *"Mutation testing proves a test has binding force, not that its
  force is sufficient"* and *"A `VERIFY PASS` is not a re-certification"*. ✓
- **E9's rationale clause** — *"every recorded escape from the cap was a renamed round"* is
  source-carried (`rev.md:139-142`, V3-N0 and V3-N1 named), not new characterization. Checked
  because the checklist's banner declares rationale deliberately absent.

## Must-fix

**MF-1 — the harness track's live pointer still sends a cold session to a step this commit
closed.** `HARNESS-LEDGER.md:19` reads *"状态 (2026-07-27)：… Phase A 已提交，等 checkpoint
read"* and `:22` reads *"NEXT = plan Step 3：Phase A checkpoint read（用户路由独立 session），
过读后 Phase B 搬家"*. The checkpoint read landed at `3743849` and its entire disposition set
landed in this subject. The round edited this exact file — appending two ruling bullets at
`:38-44` — and left the pointer untouched, while updating the plan's resume pointer in the same
commit. Ground truth is the file's own header (`:11-13`): *"What belongs here going forward: the
current pointer (what is next, what is blocked)"*, and `CLAUDE.md` names it *"the live pointer —
state, next step"*; `.goals/LEDGER.md` is a router whose only job is to send a fresh session
here. So the one file a cold harness session opens first now instructs it to perform a completed
step, while the correct next action (this read, then Phase B's preview card) exists only in the
plan. **Minimum fix:** re-date the status line and repoint the NEXT bullet.

**MF-2 — the freeze surface was corrected on the checklist side only; the plan still declares
the over-breadth E2 just dropped.** `plan:46`: *"**外加 hard rule 5 的全集**：N0 schemas 既有字
节…、`ResearchSystem/contract/` 既有文件、`.goals/plans/` 既有文件"*. Hard rule 5 never contained
that last clause (quoted above), so the plan line is a mis-derivation from a source it names —
the previous read said so explicitly (*"The source (plan line 46 …) carries the same
over-breadth"*) and scoped its minimum fix to E2 because E2 was what would govern. E2 is not the
only thing that governs: **E8** obliges the executor to *"stay inside the round's declared change
boundary"*, and the plan is what declares it. Under that declaration this commit's own plan edit
is out of boundary, plan Steps 4–10 each tick a box in the same file, and Step 11 mandates
*"本 plan 状态改 done"*. Two live texts now disagree about the same bytes. **Minimum fix:** one
clause on `plan:46` — narrow `.goals/plans/` to the signed plan blob `8ad404b1`, matching E2.

**MF-3 — the checklist mandates a round type it never defines, and this dispatch is that round.**
E10 requires *"an independent read before any round relies on"* an amendment; R6 names its record
file (`v3-checkpoint-read-<sha>.md`). Nothing anywhere says what a read *is*. Dropped from review
§12 (`rev.md:335-338`), a listed compression source: *"Neither read is a round in §3's sense: it
consumes no plan-§8 budget and carries no node verdict; its output is findings in a review-side
note, routed by the user."* That sentence is now inside a stub. The consequences are live in this
very dispatch: R3's verdict sets cover FULL and VERIFY only, so a reader of the checklist alone
can conclude either that a read must return `REVIEWED_NO_BLOCKER` — which makes it a round and
spends E9 budget the round has already spent — or that reads have no sanctioned output at all.
E10's new clause closes one direction (*"never banked as the round's FULL"*) and leaves the rest
open. I had to classify my own round from the plan and from a retired document to open this
record. **Minimum fix:** one clause on E10 or R3 — a read is not a round: no budget, no verdict,
output is tiered findings in its record.

## Low

- **L-1** E10's membership substitution removed the two contract paths from the layer while they
  still carry live routing prose that this same commit edited. `v3-harness-review-contract.md` is
  the hard-coded target of the user-locked dispatch fixture and is the first text every reviewer
  reads; its five lines decide where the reviewer goes and which SHA holds the full text. Under
  E10 as amended, editing it owes no read. This follows the previous read's own prescribed
  substitution (*"with the checklist itself substituted for the two retired contracts"*), so it
  is not a deviation — the consequence is new. **Minimum fix:** name the two stub paths in E10's
  list.
- **L-2** `plan:63` still describes the checklist as *"execution E1–E12 + review R1–R7，含
  "reviewer 可建议删除"R5"* — the exact widening this round reversed, plus a rule count two short.
  Step 2 is marked done and reads as a record of the draft, but it sits in the section a cold
  session is told to read to resume. **Minimum fix:** strike or annotate the phrase.
- **L-3** The checklist carries no record that its own 2026-07-28 amendment happened or was read.
  The banner still reads *"Compressed 2026-07-27"*; twelve of twenty rules were materially
  amended on 07-28; the mechanized provenance reminder was deleted in the same commit; and E10
  conditions reliance on a read having occurred. Nothing in the layer will ever say whether it
  did — the fact lives only in git, the plan and the ledger. The retired contracts' provenance
  blocks carried exactly this (*"the amended text may be relied on as it stands"*).
  **Minimum fix:** one dated line in E10's own one-line-derived-fact format, or an explicit
  statement that reliance-state is tracked in the plan.

## Observations — no fix owed

1. E8 restored hard rule 7's kind-naming minus *"in the title"*. The subject complies anyway
   (title `V3-PHASE-A-READ-FIX-v1`, body opening *"Review fix:"*), and the fixed
   `V3-<ROUND>-v1` shape leaves the round name as the only title slot for it.
2. E10 names `README.md` bare where the source said `document-harness/README.md`. Resolves by
   co-location; the repo has many READMEs.
3. The ledger's pointer block is 51 non-blank lines against its own declared *"≤ 30 行"*
   (`:17`). Pre-existing at 44; this round added 7. Not this round's defect to fix, noted
   because it added to it and because MF-1 lives in the same block.
4. `plan:6` still reads `status: planned` with Steps 1–3 ticked. Pre-existing.
5. `dispatch.py:362`'s comment still attributes the numbered `§n` form to
   `v3-harness-review-contract.md`, which no longer numbers sections. Carried from the previous
   read, unchanged.
6. R3's `REVIEWED_NO_BLOCKER` re-verified independently against the signed contract's §5 enum
   table (`Document-Work-Assurance-Contract-v3.md:113-114`, blob `b2dbdf75`) — correct, and not
   a re-entry of the vocabulary work reverted at `7011916`. I did not take the previous read's
   observation 2 on trust.
7. The machine-local pre-commit hook's comment block (lines 22–25) still describes the deleted
   check and cites the README row that was narrowed. Untracked, inert, per-machine — no repo
   action possible or owed.
8. The fixture's *"read it, and the counterpart it names"* now resolves by construction: both
   stubs state that the successor carries both sides, and the review stub adds *"It is your
   standing instruction and its own counterpart; read all of it."* I arrived through that chain.

## Negative results by dimension

Checked, found nothing: all three signed blobs intact **and owned by the paths E2 names**; both
user-locked oracles, `schema/document-assurance-v3/` and `ResearchSystem/contract/` diff-empty
across the range; the guard deletion is whole-file with no partial residue and no live
reference anywhere (`git grep contract_provenance` outside the plan/ledger rulings and immutable
records returns nothing; `tooling/hooks/` no longer exists); `EXECUTION.md:11` and `REVIEW.md:8`
already point at the checklist and are unaffected; E5 carries no duplicated sentence, so the
commit's self-caught Edit race was in fact removed before staging; the README's new row is
accurate about what the checklist contains (E1–E12, R1–R8) and its narrowed Local-enforcement
row is accurate about what the hook now runs; both stub links resolve and `7011916` is still the
correct full-text anchor; the two chat-only items R2 would make findings — the preview-card
approval and the cold-read waiver — are now in the ledger at `:38-40`, and the MF-4 disposition
at `:41-44`; the 62-vs-50 deviation is disclosed in plan Notes with the acceptance left unedited.

**Guard probe (E4/R8).** The one guard bearing on this round's bytes is
`test_readme_enumeration.py`, which pins the README's schema enumeration and whose subject file
was edited here. Mutated the README (dropped the `harness-issue` enumeration entry) → **RED**
with `missing` populated; restored from a sha256-checked scratchpad copy, never `git checkout --`
→ **GREEN**, `3bf09628…` before and after, worktree clean. The guard still binds after this
round's edit. Its force is binding, not proven sufficient (R4).

## Coverage

**Read in full:** `CONSTRUCTION-CHECKLIST.md`; both source contracts at `7011916` (308 + 375
lines); both stubs; `document-harness/README.md`; the stabilization plan; `HARNESS-LEDGER.md`;
`v3-checkpoint-read-820b287.md`; the construction dispatch fixture; the machine-local
`pre-commit` hook; the full repair diff including the deleted guard.
**Sampled:** `EXECUTION.md` / `REVIEW.md` (headers plus grep for checklist and contract
references); the signed contract's §5 enum table; `.goals/LEDGER.md` (harness row);
`dispatch.py` (the two contract-referencing regions).
**Probed only:** the 432-test suite (run, not read); `repo-audit.py` (run); the README
enumeration guard (mutated); `HARNESS-LEDGER-archive.md` (grep).

**Recomputed, never accepted as reported:** suite count, audit exit, all three signed blobs and
the paths that own them, oracle and tree diffs, the checklist's 62 content lines, the 683-line
compression baseline, the deleted guard's whole reference surface, the pre-commit hook's runtime
behaviour, and the previous read's own observation 2.

**Ceilings.** The claim that this round ran in a fresh context is marked, not verified. The
user's approval of this repair's boundary and of MF-4's disposition is now recorded in the ledger
and the plan — I verified that the record exists, not that it matches what was said. Whether 62
lines is *sufficient* governance is not establishable by reading them; MF-3 is the first
evidence from an actual round that it is not yet self-sufficient for the round types it mandates.
Whether the harness should keep converging by adding clauses to close read findings is the shape
R5 tells me to report and not to conclude: three of the last four rounds on this file have been
repairs of the repair. The question and the conclusion are yours.
