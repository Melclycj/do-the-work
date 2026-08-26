# Journal — round `CORE-SET-SIGNATURE` (batch `CORE-SET`, round 2), 2026-08-26

Analysis, reasoning and measurement. The round's obligations, rulings and acceptance live in
`document-harness/plans/core-set.plan.md`; its narrative lives in the two candidate commit
bodies. Neither is restated here.

## 1. The measurement the round exists to move

**Instrument: `tooling/sweep_refs.py`, and nothing else** — round 1's rule, kept.

**Method**, the same recipe as round 1 with one stated difference: `git archive <commit>` into a
scratch tree, delete what a caller does not carry (`document-harness/journal/`,
`document-harness/plans/`, all of `migration/` except the two retired-contract stubs that are
`E10` members, and the root registers), `git init && git add -A && commit` so the sweep's
`git ls-files` basename resolution works, then count **only `LINK` and `PATHTOK`** — `NAMETOK` is
a backticked bare filename, the compliant form for an artifact held elsewhere.

**The stated difference.** Round 1's strip left `CORE-SET.md` on the tree and measured **124
files**; this one deletes it, and `CONTRACT-V4-SIGNATURE.md` with it, on the ground both files
themselves assert — construction side, a caller does not carry them. Both trees here measure
**123 files**, base and tip alike, so the count is not evidence of anything having shrunk; the
recipe changed by one file and is written down so the next reader does not read 124 → 123 as
decay.

| stripped tree at | real breaks (`LINK` + `PATHTOK`) over the nine members |
|---|---|
| `8e576a1` — the round's base | **13** |
| `cb4f22f` — after items F and N | **5** |

Eight closed, and they are the eight round 1 routed here: contract v4 `:16` `:25` `:27` `:30`
`:32` `:253` `:341`, and `document-harness/README.md:16`.

## 2. The five that remain, each by ruling rather than by omission

| sites | where | why it is still there |
|---|---|---|
| 3 | `CONSTRUCTION-CHECKLIST.md:6`, both stubs `:3` | **Allowed by ruling 12.** Construction-side documents may depend on construction history; the test is who cites, not what is cited. |
| 2 | `REVIEW.md:93` (`LINK` and `PATHTOK`, one site) | **Ruled dangling by ruling 13.** Item G retires the pointer in round 3. |

## 3. A correction to the plan's own acceptance sentence, measured

Acceptance 1 for this round says the sweep count "drops by the seven contract sites" and that
`document-harness/README.md:16` "is the eighth and is **not a sweep hit** but a truth claim,
checked by reading it." The second half is wrong, and the base measurement above shows it:
`README.md:16` carried a backticked token naming the decision log through a parent-directory
prefix — a token containing a slash, which the guard's own `PATHLIKE` matches and the sweep
reports as a `PATHTOK` on a stripped tree. (Written in words rather than quoted: quoting it here
draws a `candidate_path_check` block, which is the record-quotes-the-broken-path-it-reports class
rider `freeze-audit` banks, met and worked around rather than argued with.)
It is **both** — a sweep hit and a truth claim — which is why the drop is 13 → 5 rather than
13 → 6. Round 1's journal counted it correctly inside its thirteen; the plan's acceptance drifted
from the journal, in the direction that under-reports the round's own effect. Recorded rather
than silently corrected, because the plan is the batch's carrier and the next round reads it.

## 4. Why `HD-56`'s successor is a file and not another entry

This was the round's one genuinely under-determined reading, and the ground is worth keeping.
`HD-60`'s obligation ③ names three things for one commit — the new signature carrier file, and
the two directions of `HD-56`'s pointer — and glosses it "(`HD-30` 后继承载全文 + `HD-2` 状态
翻转同 commit)". The plan's paraphrase, "a successor carrying the signature in full … in the same
commit as the new carrier", reads as though the successor and the carrier were two objects, which
would put a full copy of the signature back into the decision log.

Three things decide it the other way. Ruling 5 says the signature moves **out of**
`HARNESS-DECISIONS.md`; an entry carrying it in full would not have moved. Acceptance 2's own
headline is that the signature is traceable through **the new carrier alone**. And the decision
log outranks the plan on conflict — its own header says so in as many words. So the carrier *is*
the successor: `HD-56` → `superseded`, archived, pointing forward at `CONTRACT-V4-SIGNATURE.md`,
which points back. The novelty is real and is stated rather than hidden — a `superseded` entry
whose successor is a file rather than an `HD` id is new in this register — and it is the shape
ruling 5 requires.

## 5. Where the new carrier went, and the row that decided it

Ruling 5 says "beside `contract/`" and item F says "beside the contract", which are not the same
place. `document-harness/README.md` row 17 settled it: it states that `contract/` "holds exactly
one file", it is a product-tier member, and this round's scope does not reach it. A file placed
inside `contract/` would have falsified a member sentence no item authorised touching. The
repository root is also where the other four carriers' successors would be looked for — the
registers all live there — so the root reading costs nothing and the other one costs a member
edit. Verified after the fact: `git ls-tree -r --name-only HEAD contract/` returns one path.

The carrier does not travel, and the contract therefore **names** it instead of linking it, which
is the same demotion the five citation sites took. That is not a regression against ruling 5's
purpose: what ruling 5 removes is a signed product-tier document pointing by path into a live
construction register, and a name plus its holder is the form `E10` already prescribes for
exactly this.

## 6. A measurement attempted and withdrawn

The VERIFY of round 1 (`V-2`) measured a **product-tier-only** tree — the 59 files and nothing
else — and reported 29 references resolving nowhere, of which 7 + 1 were this round's. Re-running
that would have been the strongest possible statement of acceptance 1, so it was attempted. It
required a second tokenizer, because `sweep_refs.py` is hard-wired to the nine members, and the
one written here reported 105 → 103 on the same two commits: a different caliber, not a different
tree. **The figure is withdrawn and no number from it is carried anywhere.** This is round 1's own
`E6` lapse in the same batch — new machinery for a question the repository already answers — and
it is recorded because it was caught before it entered a claim rather than after. What the
attempt did show, and what the committed instrument shows independently, is the *shape* of the
change: contract v4's `LINK`s became bare names at the same lines. The count that stands is §1's.

## 7. What item N's reduction actually cut, and what it could not

`CORE-SET.md` was 82 lines and 7,646 characters, of which 47 lines were prose around an 18-row
list. The merged `CONSTRUCTION-INDEX.md` carries **1,609 characters of its own prose** (table rows
and the fenced block excluded; 1,804 with headings), against the item's "well under 2,000". The
cut is a little over half, and it is not larger for a reason worth naming: three blocks are
mandated rather than chosen — `HD-21`'s question and answer, the bounded sufficiency claim with
its measured gap, and the pointer saying where the argument for the split now lives. What went is
the *why* column of both tables, which was 62% of the table's characters at the item's own
measurement, and the two argument blocks, whose substance the plan already carries at ruling 11
and item K. That was checked rather than assumed before deleting them.

The byte figures went too, and that is the closure of `figure-units`' site (a) rather than a
re-pointing: the merged file states file counts, which the tree determines, and its footnote says
why a worktree byte figure does not — which is the prescription that rider itself wrote. Its other
two sites are journal numbers and stay open under `HD-23`.

## 8. The dispatch form, marked rather than adjudicated (`R4`)

The executor's prompt opened with `dispatch.CONSTRUCTION_EXECUTOR_PROMPT` verbatim, `{charter}`
resolved to `document-harness/CONSTRUCTION-CHECKLIST.md`. The orchestrator then appended the round
name, the item scope, the plan pointer and the three decision-log entries that bind the round.
`HD-53` ② makes the construction executor mode derive nothing **on purpose** — "手喂轮名与边界即
重造本模块要废除之物" — so everything after the first paragraph is hand-scoping, and this is the
third measured instance of that class in this batch after the two the ledger already records for
`--read`. Stated as a fact about this dispatch, not as a finding: whether the mode should carry a
round name is a design question, and `R5` puts the conclusion with the user.

## 9. Left open, named rather than absorbed

- **`HD-60` and `HD-61` are consumed and are still `live`.** Both are one-shot and both were spent
  by item F's contract write. Only the user flips a state; a session may only propose. Each entry
  therefore carries an additive note recording the consumption and the proposal, with its original
  words untouched, and the flip to `retired` is waiting on the user.
- **Two member edits are relied on before their independent read.** `E2`'s blob literal and its
  binder name, and `document-harness/README.md:16`. Neither adds a clause to any rule nor changes
  what any rule requires, and no other round is in flight, so `E10`'s deferral applies — deferral,
  not exemption: the bytes ride the next read of this layer, at per-member digest cost.
- **Nothing about a product run is proved here.** Round 1's step 6b already narrowed its honesty
  cap to the product-run leg, and this round narrows it no further: no run directory was built, no
  instruction frozen, no reviewer dispatched from a mounted stripped tree. That is out of the
  batch's scope and stays stated rather than implied.
- **`E9` is untouched.** No valid independent FULL has occurred on this round, so both work
  commits are candidates by `E9`'s own test, the fix leg is unspent, and no VERIFY is owed. The
  budget this round has spent is zero.
