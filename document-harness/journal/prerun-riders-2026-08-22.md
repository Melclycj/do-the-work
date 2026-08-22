# Round journal — `PRERUN-RIDERS` (2026-08-22)

> Narrative, errata and the fix leg's dispositions. The round's rulings themselves live in
> `document-harness/plans/prerun-riders.plan.md` (the seven user rulings of 2026-08-22) and in
> `HARNESS-DECISIONS.md` (`HD-55`). Records: `v3-cold-read-3a6a10b.md` (opening read) ·
> `v3-review-full-7cb7213.md` (FULL) — both under `migration/document-work-assurance-v3/`.
> Plan: `document-harness/plans/prerun-riders.plan.md`.
>
> **The round's first journal content, written by the fix leg**, because the larger half of
> what it carries is errata to a commit body `E8` forbids amending. Every figure below was
> re-measured from this repository by the executor of that leg; none is copied from the FULL.

## What the round did

Seven user rulings of 2026-08-22 stopped being chat-only. Four rider rows were redeemed by
deletion (`plan-delivery`, `chk-thin`, `HI-route`, `mark-case`) and two rewritten with a
second upholding (`status-key`, `ctx-ground`); the governing plans became a delivered item in
`ORCHESTRATION.md` with the instruction-first bound landing in `EXECUTION.md`'s authoring
rules; `REVIEW.md` gained the thin-check disposition and the reviewer's real routing path for
an out-of-scope observation; and `HD-55`'s carrier sentence landed in the three-roles table
with the merged-role class closed at all three sites the cold read's `O-1` had completed.
Prose only — no code, no schema, no test.

**Role form.** First round under `HD-55`: orchestrator and executor were separate sessions on
both the candidate leg and this one. `R1`'s four holdings were the orchestrator's throughout.
That is a process claim about sessions and is not verifiable from the repository (`R4`) — the
git identity is the same on every commit in this history.

## Errata to `7cb7213`'s commit body (`E3`)

The FULL's `L-1` and `L-2` name two figures in the candidate's body that do not reproduce.
`E8` forbids the amend that would correct a commit body, so this file is the carrier. Both
figures were **re-derived here**, and the third measurement in each block — the same census on
this leg's own tree — is new.

### 1. The rider-bank census (`L-1`)

The body wrote: *"of the bank's 34 data rows at this commit, 32 cite a review or read record in
the source column; the two that do not are submod-index … and chk-caller-prefixes"*.

Re-measured at `7cb7213`. `git show 7cb7213:HARNESS-RIDERS.md | grep -c '^| '` → **36**, which
is the header row at `:9` plus **35 data rows** (the separator at `:10` opens `|-` and is not
counted). Of those 35, the rows carrying a
`v3-{review-full,review-verify,checkpoint-read,cold-read}-<sha>.md` citation number **32**, and
**three** carry none:

| row | what its source column cites instead |
|---|---|
| `submod-index` | an R3 construction measurement |
| `chk-caller-prefixes` | an executor report |
| `io-hiroute-stale` | **the same commit's own deletion scan** |

**So: 35 data rows, 32 citing, 3 not — not 34 / 32 / 2.** The third non-citing row is the row
that same commit added, in a later paragraph of the same body. This is the failure
`E3` names in its first clause and not arithmetic: the figure was taken before the last edit,
and the last edit changed the thing measured.

The assertion the figure supports is unchanged. `REVIEW.md`'s ruling-3 route says it codifies
what reviewers have in fact done, and 32 of 35 carries that as well as 32 of 34; the body
already hedged to *"the practice and not an absolute"*.

Same census on this leg's tree, measured after its last edit to the bank: **35 table lines →
34 data rows, 31 citing, the same 3 not**. One row fewer than the subject because this leg
redeems `fixleg-scan-paste` by deletion (below), and that row cited a record; the `O-3` fix
rewrites only the `what` column of `io-hiroute-stale` and moves no count.

### 2. The `plan` line enumeration (`L-2`)

The body wrote: *"plan/plans now occurs in `ORCHESTRATION.md` at :65 :72 :74 :77 :79 :102"*.

Re-measured. `git grep -n -i plan 7cb7213 -- document-harness/ORCHESTRATION.md` returns six
hits at **`:65 :75 :77 :80 :83 :102`**. The count and the file are right; `:72`, `:74` and
`:79` name no hit, and `:75`, `:80` and `:83` are missing from the body's list. Three values
appear in both lists (`:65`, `:77`, `:102`), of which `:65` (the delivery sentence) and `:102`
(the report-back section) are the same lines in both readings.

The contrast the body draws **does** reproduce: the same command at `3a6a10b` returns exactly
one hit, `:83`, inside the report-back section and not as a deliverable.

Why it happened, and why a reader cannot tell: the class-1 scan two paragraphs earlier declares
it was run after the last edit and reproduces byte for byte; this one was not, and nothing in
the body distinguishes them. The short line the FULL points at, `ORCHESTRATION.md:81`
(*"in the instruction is"*), is the unrewrapped seam of the edit that happened after the count —
and it is inside the clause `L-4` deletes below, so both the seam and the stale count leave
together.

On this leg's tree the enumeration is **`:65 :75 :77 :80 :100`** — five, not six. `L-4`'s
deletion removed the re-typed clause that carried the `:83` occurrence, and the two lines that
deletion removes shift the report-back hit from `:102` to `:100`.

## The seventh operation: `io-hiroute-stale` kept

The plan enumerated six operations on `HARNESS-RIDERS.md`; the candidate performed seven,
adding row `io-hiroute-stale`, disclosed the widening in its own body and in the row's source
column, and offered the one-line reversal. The FULL's `O-2` confirmed the disclosure was
adequate and the ground real, and left the accept-or-strike call where the row put it.

**The user ruled the row kept (2026-08-23).** It is not reverted. What this leg does to it is
the `O-3` correction below — the row stays, and its quotation of the signed file becomes exact.
The ruling is appended to the row's own source column in the house form the `status-key` and
`ctx-ground` rewrites use: the historical offer (*用户可一行划掉*) is kept as what the candidate
said, and the answer is written after it. Left alone, that clause would have gone on inviting a
strike already declined — which is the *已答之事写成未答* shape this very row exists to record.

`O-2`'s second half is recorded without action, as the FULL wrote it: a round that widens its
own change surface has taken a share of its own scoping, which is a real tension with the
none-held claim, and all four holdings are process claims no repository can settle.

## What the fix leg changed

One user-approved fix under `E9`, taken all-in on the FULL's five lows plus `O-3`:

| finding | site | what landed |
|---|---|---|
| `L-3` | `document-harness/REVIEW.md:47`–`:48` | the reviewer's bytes: *an issue **recorded while the run is still in flight*** replaces *an issue **claiming a mid-run observation***, which is what `observed_after` actually constrains and which leaves `:50`'s after-the-run route reachable |
| `L-4` | `document-harness/ORCHESTRATION.md:80`–`:82` | the reviewer's bytes: the em-dash gloss of the instruction-first bound is deleted, leaving the pointer at `EXECUTION.md`'s *Instruction authoring rules* and no second copy (`HD-5`) |
| `L-5` | `HARNESS-DECISIONS.md:290`–`:292` | the reviewer's bytes: `HD-46`'s tiebreak rationale reads 当时的实际形态, with the dated note that the shape stopped being the norm at `HD-55` |
| `L-1`, `L-2` | commit body of `7cb7213` | not appliable — errata above |
| `O-3` | `HARNESS-RIDERS.md:44` | the row now quotes the signed sentence whole: 其**路由与 `observed_after` 窗口**的未解问题… |

**One operation beyond that list, said rather than left silent (`E9`).** Rider
`fixleg-scan-paste`'s redeem-when is *"下一次修腿落地时……修腿正文贴了扫类输出即兑付删行"* — this
leg is that moment, its commit body carries the paste, so `R10`'s redemption applies and the row
is deleted in this same commit. It is one line and reversible; strike the deletion if the
four-in-a-row streak is wanted on the books for longer. Nothing else references the row except
records that read as history (`CONSTRUCTION-LEDGER.md:67`, the `EXECUTOR-CHARTER` journal, and
this round's plan), so no dangling pointer is created — the defect class the round's own
`io-hiroute-stale` row exists for.

Not acted on, and why: `O-1` (`CONSTRUCTION-LEDGER.md:79`'s stale `HI-route` premise) is the
orchestrator's at closeout by the plan's own surface table and outside this leg's boundary;
`O-2` and `O-4` are recorded observations the FULL asks no action on.

## Honesty boundaries

- **The `O-3` fix widens the citation as well as the quotation.** The row cited
  `io-design.md:100`; the sentence it quotes begins at `:99` (`:99` ends *其**路由与
  `observed_after`*, `:100` carries *窗口**的未解问题仍挂在 rider `HI-route`…*), so the row now
  reads `:99-100`. A pointer whose line does not contain the bytes it quotes is the same defect
  the finding names, but the FULL supplied bytes only for the quotation — the line span is the
  executor's, measured, and disclosed here rather than folded in silently.
- **`HD-46`'s edit sits in `§implemented`**, which the decision log marks 不必读. It changes a
  tense and appends a dated note; it does not rewrite the recorded reasoning. That is consistent
  with the `EXECUTOR-CHARTER` closeout, where the user ruled `HD-46`'s recorded text is read as
  history rather than corrected — history is what dating it preserves.
- **The two member edits owe their independent `E10` read**, riding the next read of this
  layer at per-member digest cost. `REVIEW.md` and `ORCHESTRATION.md` are the members touched;
  `E10`'s membership sentence is untouched, so no `E10-sync` is due and that rider stays banked.
- **`L-5`'s second half is closed by the fix, not by a tracker.** The FULL noted that `HD-55`'s
  move to `§implemented` retired the only thing naming the residual site. With the site itself
  corrected there is nothing left to track, and adding a tracker for a closed site is what `E6`
  refuses.
- **The class scans behind this leg are in its commit body** (`HD-41` ④), run on the fixed
  tree. Two of them widen the range or the pattern the candidate used, and the widening is
  itself a measured finding: the candidate's merged-role pattern is English-only and its range
  was the ten members, so `HD-46`'s Chinese-form site was outside both. `L-5` was reachable by
  neither, which is what the FULL said about the range and did not say about the pattern.
- Rider `fixleg-scan-paste` records four consecutive fix legs that did not paste `HD-41` ④'s
  output. This leg pastes it; the row redeems by deletion in the same commit.
