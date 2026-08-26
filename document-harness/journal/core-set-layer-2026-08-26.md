# Journal — round `CORE-SET-LAYER` (batch `CORE-SET`, round 1), 2026-08-26

Analysis, reasoning and measurement. The round's obligations, rulings and acceptance live in
`document-harness/plans/core-set.plan.md`; its narrative lives in the six candidate commit bodies.
Neither is restated here.

## 1. The measurement the round exists to move

**Instrument: `tooling/sweep_refs.py`, and nothing else.** It imports `LAYER`, `PATHLIKE`,
`RUNTIME_PREFIX` and `TOKEN` from `layer_path_check`, so it cannot drift from the guard the way a
hand-written list would. Two earlier answers to this same question — a scratch script written by
the orchestrator (38 / 29) and the batch briefing's own tokenizer (32 / 24) — are **withdrawn**,
and no number from either survives anywhere in this round. Writing that script was the round's
own `E6` lapse: new machinery for a question the repository already answered. It is recorded
because the rule names exactly this reflex, and the round tripped it before it applied it.

**Method.** `git archive <commit>` into a scratch tree, then delete what a caller does not carry —
`document-harness/journal/`, `document-harness/plans/`, all of `migration/` except the two
retired-contract stubs that are `E10` members, and the five root registers plus
`CONSTRUCTION-INDEX.md`. **124 files on both trees** — item I's deletion of the history file
exactly offsets `CORE-SET.md`, and the two trees differ by that pair alone. (This sentence first
read "124 before, 125 after"; the FULL's `L-2` measured both at 124 and it was right.) Then
`git init && git add -A && commit` so the sweep's `git ls-files` basename resolution works, then
run the sweep and count **only `LINK` and `PATHTOK`**. `NAMETOK` is a backticked bare filename,
which since round `XREPO-REFS` is the *compliant* form for a caller-held artifact — counting it as
breakage is what inflated both withdrawn figures.

| stripped tree at | real breaks (`LINK` + `PATHTOK`) over the nine members |
|---|---|
| `cc3b3ab` — before the candidate | **31** |
| `c5f00f6` — after items A–M | **13** |

**`ONBOARDING.md` is measured separately and by grep, because it is not a member and the sweep
never scans it.** Path-shaped references from it into the three registers: **2 → 0** (`:16` by
item B, `:100` by item C — the second being a site the briefing's item list did not name and this
session's own opening measurement found).

## 2. Every one of the thirteen residuals is accounted for

A count is only honest if nothing in it is unexplained, and `E9`'s acceptance requires the round
to state what it leaves rather than imply none.

| sites | where | why it is still there |
|---|---|---|
| 3 | `CONSTRUCTION-CHECKLIST.md:6`, both stubs `:3` | **Allowed by ruling 12.** Construction-side documents may depend on construction history; the test is who cites, not what is cited. |
| 2 | `REVIEW.md:93` (LINK and PATHTOK, one site) | **Ruled dangling by ruling 13.** The target was deleted by item I and the pointer retires with item G in round 3. |
| 1 | `document-harness/README.md:16` | Round 2's. It sits inside the contract-signature sentence that item F rewrites; splitting it now would touch the same clause twice. |
| 7 | `contract/Document-Work-Assurance-Contract-v4.md` | Round 2's, and `E2`-frozen: writing these bytes needs a recorded user ruling that does not exist yet. |

**Acceptance 1 holds**: of `ORCHESTRATION.md`, `EXECUTION.md`, `CONSTRUCTION-CHECKLIST.md` and
`ONBOARDING.md`, **zero** path-shaped references into the decision log, the rider bank or the
construction ledger remain on the stripped tree. `CONSTRUCTION-CHECKLIST.md:6` points into
`plans/`, which is not a register. The bare names at `CONSTRUCTION-CHECKLIST.md` and
`ORCHESTRATION.md:51` are **expected to survive** — ruling 1 removed the prefix, never the name.

## 3. Why ruling 16 was needed, and what it says about ruling 12

Ruling 12 gave the right test and the wrong list. Its test — a construction-side document may
cite construction history, a product-facing one may not — is what decided items J and M alike.
Its *enumeration* named `plans/`, `journal/` and `history/`, and stopped there. But this batch's
goal sentence also says **no review records**, and `migration/`'s N0, W2 and supersession-2
records are exactly that. `EXECUTION.md:110` and `REVIEW.md:90` are product-facing documents
citing them, so ruling 12's own test already condemned two sites its list did not mention.

The lesson worth keeping is not "the list was short". It is that **a ruling stated as a test and
then illustrated by a list gets executed against the list.** The list is what an executor greps
for. When both are present, the test has to be the thing the item names and the list has to be
marked as illustrative — which is how item M is written.

Ruling 16 also cost nothing to take late, and the reason is worth recording because `E9` says
every recorded escape from the cap was a renamed round: **no independent FULL had occurred**, so
item M is a pre-submission correction by `E9`'s own test, consuming no budget leg and owing no
targeted VERIFY. Had it arrived after the FULL, it would have been the round's single
user-approved fix and would have obliged a VERIFY.

## 4. The opening read's correction to the dispatch, and the baseline error behind it

The opening cold read ran in narrow form by user ruling: two members read end to end, the rest
covered by citation. The orchestrator's coverage claim said six citable and three owed; the reader
measured **seven and two**, and the defect was not arithmetic but the choice of baseline. `E10`
covers a member unchanged since **a** recorded end-to-end read of it, not since one nominated
record. `ORCHESTRATION.md` had changed since `21dad76` and was nonetheless covered, by
`v3-checkpoint-read-153302a.md`.

Three things follow. The error direction was safe — a single-baseline test can only over-read.
`CONSTRUCTION-LEDGER.md:67` already named the correct two, so the dispatch drifted from the
ledger rather than the ledger being stale. And the claim was only caught because it was handed
over marked *verify this, do not accept it*; handed over as fact, `R2` would have been violated
and the arithmetic would have propagated.

The read's `O-2` is the second measured cost of `dtw dispatch --read` having no narrow form: the
hand-scoping re-supplied the member enumeration `dispatch.py` deliberately withholds, its comments
recording that a hand-written member table was wrong once before. Logged under the
dispatch-economy batch's first item, not fixed here.

## 5. Two claims this round made and had to withdraw

Recorded together because they are the same failure at different scales, and `E3` is the rule both
land under.

- **"Invisible to every machine in this repository."** The plan said deleting item I's target left
  a dangling link no machine could see. The guard half was right — `layer_path_check` scans only
  added lines. `sweep_refs.py` reads standing text and reports it twice, moving the whole-tree
  count from 13 to 15. No consequence, since the sweep exits 0 and blocks nothing; the claim was
  simply broader than what was measured.
- **The two withdrawn breakage counts** of §1.

Both were assertions written before the command that could falsify them was run. That is the
sentence `E3` already contains.

## 6. Left open, named rather than absorbed

- **`CONSTRUCTION-LEDGER.md` stands at exactly 180 lines, its own declared bound.** The header
  says to move the oldest closed material into the archive when the bound is reached; the archive
  is marked *read-only, do not continue writing*. **This journal first called those two
  instructions contradictory, and that was wrong** — the archive forbids *appending narrative*,
  giving its own reason (a round's narrative belongs in its review record and commit body), while
  the header prescribes *moving closed material*, which is not authoring narrative and is exactly
  how the archive came to exist ("Moved verbatim, nothing deleted, nothing retyped"). The header's
  remedy is available.
  **What the measurement did show is worse than a contradiction: the bound does not measure what
  it is for.** The file is 180 lines and **53,609 bytes**, and **one line — the CLOSED roll —
  is 26,110 UTF-8 bytes / 16,171 characters, 48.9% of the file's bytes**. Across the 17 top-level
  entries that entry holds **56.7% of all entry content by characters** (55.6% by bytes), the next
  largest being 2,405 characters / 4,060 bytes. **Units are given on both sides deliberately**:
  this paragraph first set 26,110 beside 2,405 without saying that the first was bytes and the
  second characters, which read as a 10.9x gap where like for like it is 6.7x — the VERIFY's `V-1`,
  and `HD-23` routes a journal number outside the fix leg. The byte totals are worktree bytes under
  `core.autocrlf=true` and move with the checkout; the ratios and the conclusion do not. A line-count bound cannot see growth
  that happens *inside* an existing line, which is where all of it happened; the header's own
  stated target is "the 20-to-300-line session, not line 181". The user ruled on 2026-08-26 that
  the bound changes its unit — bytes or entry count rather than lines. That change is not this
  round's and lands as its own commit, so the round's diff stays what the FULL reviewed.
- **Four `ONBOARDING.md` Owner cells were not re-pointed**, banked as rider
  `onboarding-io-design-owners`. Their decisions live nowhere but `io-design.md`: the empty-instance
  shape, *deliberately not pre-created*, *the harness provides no template*, and the §5 carrier
  decision behind the standalone policy file. Re-pointing them would have meant inventing an owner,
  which adds a clause to a rule — design, and beyond the approved card. Ruling 15's bound held.
- **`HD-6`'s archive threshold fired for the fourth time** and reached the user for the first
  time; answered *do not clear* (ruling 17). The previous three were sessions recording *no answer
  received* to themselves, which is a failure mode of the obligation rather than of any session.

## 7. Honesty caps

The stripped tree is a `git archive` scratch copy, not a real caller: it proves the references
resolve, **not** that a stranger can mount this and run a round. Nothing here re-runs the
briefing's end-to-end mechanical check (`dtw --help`, the two guards, a fresh `init`) on the
stripped tree; the executor ran `dtw init` into an empty repository on the **full** tree and got
exit 0 with exactly one decision log. The narrow-form read means seven of nine members were
covered by citation rather than re-read at this commit — sound under `E10`, and still less
coverage than a full read would have given.
