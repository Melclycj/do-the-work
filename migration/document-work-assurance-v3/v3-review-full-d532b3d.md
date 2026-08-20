# V3 review record — FULL, design round `ASSERT-OWNER`, subject `ff05b01..d532b3d`

Independent FULL review of the assertion-discipline / one-owner design round. Dispatched as the
range `ff05b01240c357b222b6adc0852736b76ffde379..d532b3d60dfce96e48b2feaf510ddff47032150d` and
nothing else; round, budget, authorization, obligations and every figure below were re-derived
from the repository. No reported figure was accepted.

**Verdict: `CHANGES_REQUIRED`.** Two blockers, two findings that ride the same repair, one low,
four observations. The rules themselves landed correctly and the battery is green — what fails is
the round's own conformance to the rule it installed, in the one artifact the round leaves behind.

## What the subject turned out to be

| | |
|---|---|
| Round | `ASSERT-OWNER` — design round, plan [`harness-assertion-owner-design.plan.md`](../../../.goals/plans/harness-assertion-owner-design.plan.md) |
| Kind | instruction-layer design (`E10.10`: adds clauses and changes what rules require ⇒ design, opens a round) |
| Base / tip | `ff05b01` → `d532b3d`, branch `document-work-assurance-v3`, worktree clean at review time |
| Commits | `cf1e3ee` amendment (`E3`/`E7`/`E13` + `EXECUTION.md` item 5) · `50c2b31` amendment (`E10` sub-clause numbering) · `2de05c3` record (the `E10.2` independent read) · `d532b3d` free-channel application of that read's three lows |
| Budget consumed before this dispatch | **none.** Under `E9`'s discriminator no valid independent FULL had occurred, so both amendments are pre-submission; the `E10.2` read is not a round; the `E10.5` free-channel application is not a round. **This dispatch is the round's one FULL.** |
| Obligations | plan §五项修订 items 1–5 + plan §Acceptance (six criteria) |
| Authorization | not visible in the repository — see `O-2` |

Files changed across the range (`git diff --name-only ff05b01 d532b3d`): 7 — the checklist, `EXECUTION.md`,
`README.md`, both retired-contract stubs, the new plan, the new read record.

**`E2` holds.** The frozen set is three blobs (`b2dbdf75`, `68031fa2`, `e1a2f26b`) plus every file
of `ResearchSystem/schema/document-assurance-v3/` at the 2026-08-03 re-baseline; `git ls-files` on
that directory returns **15** at `d532b3d`. None of the seven changed paths is in that set.

## What was re-executed, not read

All six battery legs re-run by this reviewer at `d532b3d`, in a clean worktree, output read
directly:

- `ResearchSystem/tooling/tests/run_tests.py` → `tests: 29 passed: 29 failed: 0`, exit 0
- `ResearchSystem/tooling/tests/run_p4_tests.py` → `tests: 80 passed: 80 failed: 0`, exit 0
- `ResearchSystem/tooling/tests/run_p5a_tests.py` → `tests: 39 passed: 39 failed: 0`, exit 0
- `ResearchSystem/schema/fixtures/validate_fixtures.py` → `cases: 58 matched: 58 unexpected: 0`, exit 0
- `python -m pytest -q` from `ResearchSystem/tooling` → `701 passed in 99.56s`, exit 0
- `rsc.py compile --check` → `generated output fresh; lint clean`, exit 0
- `Thesis/Work/Tooling/repo-audit.py` → `RESULT: clean`, exit 0

Tier selection is correct: `README.md` is pinned by `test_readme_enumeration.py` and the checklist,
`EXECUTION.md` and both stubs are enumerated by `layer_path_check.py`, so the tiering section's
own exception makes this batch tooling-touching and the full battery owed. No new guard was added,
so `E4`/`E5` have no subject this round.

**Entry gate (`E10.12`) holds.** Comparing blob ids member by member between the cited cold read
`v3-cold-read-ddd773a.md` and the base `ff05b01`: eight of the nine are byte-identical
(`15999875`, `54dfef83`, `3350bfac`, `17ff31bb`, `b576a45e`, `68031fa2`, `e1a2f26b`, `09aa8699`),
and the cited record does state the blob ids citation depends on. The ninth, `EXECUTION.md`,
changed `62c55e4b` → `9f80e728` and was re-read end to end. Its length at `9f80e728` is **430**
lines, not the 431 first reported — already caught and corrected inside the round.

**The `E10` numbering claim holds.** I re-derived it from the bytes rather than from the record.
Extracting `E10` at `cf1e3ee` and at `50c2b31`, normalizing whitespace, stripping the new list
markers and diffing at word granularity: every substantive word is preserved in order. The only
changes are semicolon → full stop, capitalization, `(relied …)` → `— relied …`, `this channel` →
`that channel`, plus two added sentences that the commit body discloses. **Added no clause,
removed none, changed no requirement — confirmed.** Old-14 → new-15 maps as 1–4 → 1–4, old 5 →
new 5 + 6, old 6–14 → new 7–15.

**The corrected rationale sentence is true.** Splitting the pre-numbering chain mechanically on
semicolons returns **14** segments (13 semicolons), and segment 5 does contain both new clause 5
and new clause 6, joined by `— but`. The `L-2` fix in `d532b3d` replaced a false reason with a
verified one.

**`L-3` was a zero-byte move** — the two lines removed from `E13`'s tail and re-inserted after
`E12`'s range clause are byte-identical.

**The cost disclosure reproduces exactly.** Checklist length: `ff05b01` 204 → `cf1e3ee` 231 →
`50c2b31` 241 → `d532b3d` 242. The disclosed `+37 / +18%` against the executor's own earlier
`≈215 / +5%` estimate is right, and it is the one number in this round measured and published to
the standard the round is about.

---

## Blockers

### `B-1` — the round's permanent instruction text carries a measurement no command produces, in the justification of the rule it installs

**Location.** `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` `E13`:

> Measured inside this layer before this rule existed: `E3` and EXECUTION.md's *Measure last*
> stated one rule independently and had drifted to **six clauses against two**.

and the same figure again at `ResearchSystem/document-harness/EXECUTION.md` item 5:
"the two had drifted to six clauses against two, which is the defect `E13` is now the rule about."

**Ground truth.** Re-derived at `ff05b01`, the revision the sentence speaks of. Old `E3`: **5**
sentences, **2** semicolons, so **7** under a sentence-plus-semicolon split. Old `EXECUTION.md`
item 5: **2** sentences, **0** semicolons, so **2** either way. The *two* reproduces under both
readings; the *six* reproduces under neither, and no third reading is named.

**What it violates.** `E3`, in the form that was already in force at `ff05b01`: "Counts, digests,
path enumerations and worktree state are emitted from the command that produces them or omitted"
and "A factual assertion written into instruction text runs the command that could falsify it
first, output kept in the commit body or the round journal." `cf1e3ee`'s body pastes no such
command for this figure. `E3` as this same commit amended it adds "A count carries the revision it
was taken at" — this one carries none. And `E13`'s own second half — "a deliverable carries what
stays true of the artifact and points for the rest, because a deliverable is read by people who
will never see the round that wrote it" — is broken by the sentence carrying it: a drift that this
round then repaired is round state, not a durable property of the artifact, and it is now written
into two deliverables, one of which (`EXECUTION.md`) is read by product-run executors who will
never see this round.

**Why this is not wording-level.** `R9`'s test is a conjunction, and the second half fails: the
accurate fact is **not** recoverable from adjacent text or from a committed record. Nothing in the
repository states 5, or 7, or names the counting rule; recovering it requires an independent
re-derivation the text gives no pointer to. Every future cold read of this layer reads "Measured"
as an established figure, which is exactly the standing-fact carry-forward `E3` now names as a
defect.

**Minimum fix.** At both sites, either state a figure a command produces and name the counting
rule and revision — "five sentences against two, at `ff05b01`" — or drop the figure and keep the
qualitative claim, which needs no number to do its work. If the figure is kept, `E3` requires the
counting command's output in the commit body or the round journal.

### `B-2` — rider `wl-route` came due inside this round, on both of its conditions, and was neither redeemed nor recorded

**Location.** `ResearchSystem/HARNESS-RIDERS.md`, row `wl-route`. Its blob is `e598aeeb` at
`ff05b01` and `e598aeeb` at `d532b3d` — the bank is byte-unchanged across the whole range.

**Ground truth.** The row's redeem-when is "下一个有资格开轮且碰 `E10` 自由通道枚举句 / `R9` 抬头句 /
`R10` 路由句的设计批", deadline "下一份对 wording-level finding 供字节的 read 记录". Both arrived here:

- This is a round-eligible **design** batch, and `50c2b31` re-punctuated the free-channel clause
  itself — it is now `E10.5`, and its wording moved from `… reversible — but neither this channel …`
  to `… reversible.` / `Neither that channel …`. The named surface was touched.
- `v3-cold-read-50c2b31.md` is a read record supplying exact bytes for three findings, and the
  record itself classifies them: ":288–289" states each "supplies exact bytes and each is
  wording-level, which is precisely the case rider `wl-route` records". The deadline is not my
  inference; the read named it.

**The predicted damage then materialized inside the round.** The executor could not resolve the
route from the text — `E10.5` and `R10` say apply now, `R9` says bank — stopped, and escalated. The
resulting user ruling ("用户 2026-08-15 裁「套」") now lives only in `d532b3d`'s commit body. That is
the exact failure the row was banked to prevent, and `R10` makes redemption due on arrival, not on
convenience.

**Minimum fix**, either branch:

1. **Redeem.** This round is design-eligible, so the tiebreak clause the row says is design is
   in-power: one bound added to `E10.5`, `R9`'s opening sentence, or `R10`'s routing sentence, and
   the row deleted in the same commit.
2. **Decline, durably.** Record that both conditions arrived and were not taken, re-date the row
   per `HD-37`, and give the user's instance ruling a home — it satisfies the decision log's third
   admission question (a user ruling with no home but the conversation and a commit body) and
   currently has no `HD-` entry.

---

## Findings riding the same repair

### `F-3` — two of the round's three `E7` sweeps do not reproduce, and the one in the final commit pastes no output

`E7`, as this round wrote it, is literal: a fix "runs, in the same commit, the search that would
find the rest, and **pastes that search and its output in the body**". `E7` was in force for
`d532b3d` — it landed at `cf1e3ee` and passed its `E10.2` read at `2de05c3` before `d532b3d` was
written.

**`d532b3d`'s sweep.** The body reports "命中 38 个文件 … 其余 32 处全在不可变评审记录里", declares no
scope, and pastes no output. Re-derived with `git grep -lE 'E1(–|-)E1[0-9]'` over the tracked tree,
at both `2de05c3` (pre-fix) and `d532b3d` (post-fix): **37 files / 49 matching lines**, the same at
both. Repeating the file half with `grep -rlE` over the whole working directory — untracked and
ignored files included — returns the identical 37-file set, so no out-of-tree file explains the
difference. The buckets are **3** live sites (1 line each) + **6** (4 plans,
2 journals, 1 line each) + **28 files / 40 lines** in immutable review records — 3 + 6 + 28 = 37 and
3 + 6 + 40 = 49, both closing exactly. Neither 38 nor 32 appears anywhere.

**`cf1e3ee`'s measure-last sweep.** This one *did* declare its scope — "全仓 tracked `*.md`/`*.py`，
排除评审记录与 archive" — and reports 12 hits. Under that scope I get **14**; the two extra are
`ResearchSystem/migration/document-work-assurance-v3/W2/W2-record.md:40` and `:173`. The figure is
recoverable only if "评审记录" silently includes the `W2/` tree, which the declared scope does not
say. This is the weaker of the two, and its classification is unaffected.

**What holds.** Both sweeps' *conclusions* are correct. I confirmed independently that the three
live `E1–E12` sites were the only live ones and are all fixed; that the six remaining non-record
hits are historical statements pinned at their time; and that `cf1e3ee`'s second sweep
(`one section below|the exception and says so|only section`) is genuinely zero at `cf1e3ee` and
had exactly one hit at `ff05b01` — the line the round changed. The defect is the evidence, not the
sweep.

### `F-4` — the `763` count a design reversal rests on reproduces at no revision or scope

`50c2b31`'s body, and plan lines 47 and 71, state "`E10` 被引用 **763** 次（量程 = 全仓 tracked
`*.md`/`*.py`，排除 checklist 自身）", and this is the stated basis for reversing the plan's original
proposal to split `E10` into a new rule. Under that exact declared scope I measure, at all four
revisions in the range: backticked `` `E10` `` occurrences **755 / 769 / 769 / 776**; bare-token
`E10` occurrences **1095**; matching lines **1025**. 763 is none of them. The count also carries no
revision, which `E3` as amended by this round now requires.

**The decision it supports is unaffected** — any figure in the hundreds carries the argument
identically — and I confirmed the substantive acceptance criterion holds: the numbering left the
membership enumeration byte-unchanged and dangles no reference. What fails is that the number a
recorded reversal cites cannot be reproduced by the reader it was written for.

---

## Low

### `L-5` — the file `E13` designates as the owner of round state carries stale round state

`.goals/plans/harness-assertion-owner-design.plan.md` is byte-unchanged since `cf1e3ee`
(`git log` on the path returns one commit). At `d532b3d` it still reads `status: R1 起草中`; steps 2,
3, 4 and 5 are all `- [ ]` although `cf1e3ee`, `50c2b31`, `2de05c3` and `d532b3d` respectively
completed them; the resume pointer still says "下一步 = 步骤 2 起草落地第 1–4 项"; and the acceptance
criterion still reads "`E10` **十四**条子条可寻址" against **fifteen** delivered and against
`50c2b31`'s own body, which says fifteen.

**Named downstream decision.** `E13` now instructs that round state is owned by the plan. A reviewer
or a fresh session deriving this round's state from its designated owner concludes that nothing
after step 1 was done — I read it that way first, and had to reconstruct the real state from the
commit graph instead. Under `R9` this is above wording-level for the same reason as `B-1`: the
accurate fact is recoverable only by an independent derivation the file gives no pointer to.

## Observations

- **`O-1` — `E8`'s kind list has no entry for a free-channel layer application.** `d532b3d` names
  its kind as "自由通道（`E10.5`）", which is not one of `E8`'s eight (candidate / pre-submission
  correction / review fix / closeout / errata / amendment / ruling / record). It follows the
  precedent `e4ffa2b` set, and `HD-38` establishes the category as one that carries its own commit.
  Pre-existing gap in the enumeration, not introduced here; per `R5` I report the shape and leave
  the question.
- **`O-2` — authorization and the routing ruling are chat-only.** No preview card (`E11`) and no
  record of user approval to open this round is visible anywhere in the repository, and neither is
  the routing ruling that sent the three lows down the free channel. `R7`: an authorization I
  cannot see is a hint, never a block — so this is a stated ceiling, not a blocker. `R2` names
  chat-only load-bearing material as a finding, and the routing ruling is load-bearing: it decided
  a live rule conflict.
- **`O-3` — the round's shape.** `2de05c3`'s own body records that the read found "三个同类新实例"
  inside the round's first two commits. I find four more of the same class — `B-1`, `F-3` (two
  sweeps), `F-4` — three of them in the commits that answered those findings, including the sweep
  paragraph that exists to demonstrate the new `E7` was obeyed. The rule text landed correctly and
  is, as far as I can verify, exactly what the plan specified; the round's own assertion practice
  did not converge across four commits and one read. Whether that means the discipline needs a
  machine, or a different fix, or is converging at an acceptable rate, is not mine to conclude
  (`R5`).
- **`O-4` — a `wl-route` sibling was not checked.** Rider `E10-sync` says it "是每次触碰时的核对项",
  and `50c2b31` added a sentence immediately after the `E10` membership enumeration. The enumeration
  itself is byte-unchanged, so the three-way mirror (prose / `LAYER` / `EXPECTED`) cannot have
  drifted and no damage exists; neither commit body records the check. Noted only because the row's
  own terms make it a per-touch item.

## Coverage disclosure (`R4`)

- **Read in full**: `CONSTRUCTION-CHECKLIST.md` at `d532b3d` (242 lines, this session's standing
  instruction); the four commit bodies in the range; the round plan; `HARNESS-LEDGER.md`;
  `HARNESS-RIDERS.md`; `HARNESS-DECISIONS.md` header and all of `§live` (read lines 1–295; `§live`
  spans 28–290).
- **Read in the relevant part**: `EXECUTION.md` — the header, item 5, and the *Regression-battery
  tiering* and *Pre-freeze gate* sections; `v3-cold-read-50c2b31.md` — its findings and routing
  sections, sampled elsewhere.
- **Probed only**: `v3-cold-read-ddd773a.md` (blob table and coverage statement, to test the
  citation, not re-read end to end); `REVIEW.md` (grep-probed for a measure-last restatement, none
  found); the review-record corpus (grep-probed for the `E1–E1x` class).
- **Marked, not verified** (`R4`): that `2de05c3` was produced in a fresh independent context; that
  the routing ruling and round authorization were given as reported. Independence of that read is
  structurally plausible — the orchestrator holds the dispatch (`R1`) — but nothing in the
  repository proves the context was fresh.
- **`UNVERIFIABLE`**: the "38 files" figure — I could not construct any scope, at any revision in
  the range, that yields it, and I do not assert it was fabricated; I assert only that it does not
  reproduce.
- Not a re-certification of anything the battery covers: mutation was not run, because this round
  added no guard.
