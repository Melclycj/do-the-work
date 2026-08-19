# Plan: Batch A — where the harness's bytes live (record layer + repo split)

- **slug**: harness-record-layer-and-repo-split
- **created**: 2026-08-07
- **complexity**: 复杂
- **status**: **A1 CLOSED 2026-08-09** — all nine steps done. Review: `a7bb1d6` FULL
  (`CHANGES_REQUIRED`) → `fd058aa` fix → `7a08265` VERIFY (no blocker). Batch A's construction
  continues in [harness-a2-construction.plan.md](harness-a2-construction.plan.md) (single-repo
  only after `HD-18`; the split is its own later batch).
- **base_commit**: dbec65f371f4ed2a0a4562f92368cda3a42b9390
- **base_branch**: document-work-assurance-v3

## Goal (one line)

Decide, on measured evidence, where the harness's bytes should live — what a run stores, what the
instruction layer governs, and what travels if the harness becomes its own repository — then split
the construction that follows into rounds that can each be reverted alone.

## Why / value

Four open items are the same question wearing four hats, and each has been deferred at least twice
because none of them is decidable alone. Grouped, they share one criterion (*which bytes belong to
the harness, and where do they sit*) and one measurement base.

The cost is measured, not asserted. Every product run copies **2,000–2,658 lines of template
scripts** into its own directory — 43–52% of the run's whole footprint, and **all of it
regenerable from the template**. That number does not scale with the product: p5b-firewall's
evidence-to-product ratio was 18.7:1 and p5b-claims's was 3.9:1, because the ratio is set by the
denominator, but the copied-script absolute stayed ~2,000–2,658 in both. Only **6%** of a run's
footprint is first-hand, non-regenerable evidence (the captured command output).

> **Corrected 2026-08-08 by A1's own M1 — the paragraph above is left standing because the verbal
> summary that preceded it gave the user this version once.** Two of its claims do not survive
> measurement. (i) The "2,000–2,658 lines" is the **whole `scripts` category**, not the template
> copies; the template-*named* copies are **502–1,088 lines/run** (16% of run bytes, not 43–52%).
> (ii) "**all of it regenerable from the template**" is false: of 23 template-named copies across
> seven runs, only **6** were ever byte-identical to any historical version of the template, and
> **no** `run_bind_v2.py` or `run_evidence_v2.py` in any run ever was. Measured properly, the
> genuinely shareable mass is **≈883 lines/run** — about a third of what this paragraph projects —
> and it needs a "shared core + per-run delta" shape, not a plain reference swap, because
> `build_run.py` (the largest single script, 25% of all script bytes) is only **24%** similar
> across runs. Full derivation: [journal/batch-a1-2026-08-08.md](../../document-harness/journal/batch-a1-2026-08-08.md) §2.

Second measured cost, taken 2026-08-07 during `HI-REDEEM-5`: one FULL review ran **252k tokens /
25.5 min**, and its targeted VERIFY — on a subject one-third the size — ran **208k / 23.8 min**,
i.e. **83%**. Reading breadth did halve (≈20 read-in-full items → ≈9), but the saving went to
(a) reading the FULL record itself in full (412 lines), (b) the identical seven-command battery,
and (c) deeper per-item verification. **A can reduce what a reviewer must READ; it cannot reduce
what `R2` makes them RE-DERIVE.** Sample n=1; `subagent_tokens` units unverified.

## Context to resume cold

### The four items, and where each is already recorded

| # | Item | Recorded where | What is open |
|---|---|---|---|
| ① | **Record-layer redesign** | [ResearchSystem/document-harness/journal/record-layer-2026-08-05.md](../../document-harness/journal/record-layer-2026-08-05.md) — ledger §1-2, criterion §3, scope §4, the five questions §5, second data point §7 | §5's five questions |
| ② | **Independent-repo split** | `ResearchSystem/HARNESS-LEDGER.md` backlog | option (subtree split / submodule / nested repo) + three hard problems |
| ③ | **run-v2 README layering** | [ResearchSystem/migration/document-work-assurance-v3/v3-review-full-0b8b824.md](../../migration/document-work-assurance-v3/v3-review-full-0b8b824.md) O-1, plus the ledger's open line | three-way choice |
| ④ | **rider `CLI-hist`** | `ResearchSystem/HARNESS-RIDERS.md` | nothing — the fix is already written out; it is A2 work whose trigger is tied to ② |

**Not recorded anywhere before this file** (it existed only in the 2026-08-07 conversation): the
grouping into batch A, the A1/A2 staging, the three couplings below, the `E2`-retirement ruling,
and the sibling batch B.

### The three couplings — why these four travel together

1. **§5.2 (copies → references) ↔ hard problem (b) (instruction-layer / hook cross-root
   references).** Changing whether the template is copied into each run *is* changing where files
   live, which is that hard problem's subject.
2. **Record-layer volume ↔ migration cost.** The journal §6 already says it: the volume is the
   main component of what a split has to carry.
3. **§5.2 ↔ ③.** They are **the same object** — whether the run-v2 README joins the instruction
   layer and whether the run-v2 template is still copied per run are two questions about one file
   set.

Explicitly **not** coupled (journal §6 says so): riders `RA` / `PD` / `CLI-hist` are the same
problem domain but **do not merge** — each keeps its own redemption condition.

### Already ruled — carry these in, do not re-litigate

- **`E2` retirement of the signed plan blob (user, 2026-08-07).** The plan
  `.goals/plans/document-work-assurance-harness-v3.plan.md` (blob `8ad404b1…`, 712 lines,
  byte-unchanged since it was frozen) leaves `E2`'s frozen list. Then it is archived into the new
  repository's own `.goals/`. Two sites must change **together** in
  `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` — the enumeration at `:26` (drop the
  blob) and the count at `:34` ("Four blobs and one directory" → three) — because changing one and
  leaving the other is the dangling-neighbour shape a FULL already rejected once (`9dcb783` B-1).
- **Why it is cheap in substance**: `E2` names a **blob**, not a path, so it never blocked moving
  the file; immutability has a second, independent source (the plan's own §0/§11/§13 plus the blob
  binding recorded at `N0-record.md:19`); and `E2` has **zero mechanical enforcement** (nothing in
  `ResearchSystem/tooling/` reads those blob ids). What retirement buys is that the freeze surface
  becomes wholly contained in `ResearchSystem/` — 3 blobs + 1 directory, none of them outside.
- **Honest edge, recorded when the ruling was taken**: retirement removes a *prohibition* while the
  `N0` record keeps the change *detectable*. Those are not the same thing.

### One measured constraint the split must plan around — and it is narrower than it first looked

`ResearchSystem/contract/Document-Work-Assurance-Contract-v3.md:23` links the plan as a **wikilink**
(`[[document-work-assurance-harness-v3.plan|…]]`), and `Thesis/Work/Tooling/repo-audit.py:306`
treats broken wikilinks as a **hard** failure (`block(..., True)`) on a pre-commit gate.

**But the resolution rule decides how much that matters, and it was read rather than assumed**
(`repo-audit.py:89`, `base.setdefault(p.stem.lower(), …)` over every markdown file in the tree; the
lookup at `:128` is `alias.get(c.lower()) or base.get(c.lower())`). A wikilink resolves against the
**basename, anywhere in the tree** — not against a path. Therefore:

- Moving the plan **anywhere inside one repository** costs nothing; the link still resolves.
- The break happens **only if the plan and the contract end up in different repositories** — then
  the repo holding the contract has a dangling basename and its audit fails.
- **The chosen shape does not trigger it.** Archiving the plan into the *new* repo's `.goals/` puts
  it in the same repository as the contract, which is a harness file and travels too.

So this is a **check A1 must not skip**, not a blocker A1 must clear: confirm the two land together.
If some option would separate them, repairing the link means writing the contract — an `E2` frozen
blob needing its own recorded ruling — and that cost belongs to that option, not to the batch.
(Corrected 2026-08-07 during preclear: an earlier draft of this file, and the verbal summary that
preceded it, stated flatly that the plan leaving this repository fails the audit. That is true only
of the separation case, and the archive shape is not it.)

### Where the harness's own rules bind this batch

- Record-layer journal, top: *"任何改动都要另开轮"* — the journal is a problem statement, and A1 may
  not turn it into construction by itself.
- Journal §5 heading: *"下一步就是这些，不是方案"* — A1's measurements come before any design.
- `E10`: an amendment that changes what a rule requires is design and **opens a round**. The `E2`
  edit is such an amendment, so it lands inside A1's round rather than as a maintenance batch.
- `E1` / `R5`: a session may measure, cost out and propose; it may not take the decisions. Every
  `D<n>` below is the user's.
- `E11`: each round owes a preview card and waits.

## Constraints / Out-of-scope

- **A1 decides; A1 does not build the record layer.** The only construction A1 carries is `C1`
  (the `E2` edit), because that one is already ruled.
- **Out of A's scope entirely — batch B** (`run_all` wiring shape · ledger binding degree · rider
  `RA`). Same original "I/O design 批" label, different criterion: B is about who calls and who
  binds, A is about where bytes live. B does not need A first; A makes B's question clearer.
- **Out — rider `PD`** (`pack_digests()` zero-caller) and **`E` (topology claim shape)**, whose
  source was never located; the ledger's standing instruction on `E` is *"追不到就删，别带进 v4"*.
- **Out — `E2`'s remaining surface.** The contract, both supersessions and the 15-file schema pack
  stay frozen. Only the plan blob leaves, and only under the ruling above.
- **Out — closed runs' records.** Journal §4: read-only, no retroactive restructuring.
- **Out — reducing what `R2` makes a reviewer re-derive.** A can shrink reading, not re-derivation.

## Steps

### A1 — measure, cost out, land the one ruled edit, then put the decisions

- [x] 1. **M1 — measure the other six runs.** The distribution is measured for 2 of 8
      (`p5b-firewall`, `p5b-claims`); do `w1-r1`, `p3-corr`, `p4-bridge`, `p4-doc`, `p5a-firewall`,
      `p5a-shells` on the journal §1 method (per-file line accumulation over the run directory,
      `__pycache__` excluded), and report per-run: evidence / scripts / control / instruction split,
      plus the product denominator. Answers journal §5.1. Mechanical; do it first, everything else
      cites it.
- [x] 2. **M2 — establish what copies→references would break.** One cost is already known and must
      be reproduced rather than repeated from this file: a `command_exit` check with
      `subject_tree: candidate_commit` needs the script present in the **materialized candidate
      tree**. Enumerate every other binding that assumes a script sits inside the run directory.
- [x] 3. **M3 — establish what a non-persisted CheckResult would break.** Known suspects to verify:
      the state pointer, the coverage document's join, and a reviewer's re-run. Report which
      bindings break and which survive recomputation from the captured output plus the check spec.
- [x] 4. **M4 — classify a review record's mass.** Take two or three records and split their lines
      into *re-derivation shown* versus *conclusion*. Answers journal §5.4 with a number instead of
      an impression.
- [x] 5. **M5 — cost the three split options** (subtree split / submodule / nested repo) against the
      three hard problems, and **M6 — confirm the plan and the contract land in the same
      repository** under whichever option wins. Wikilinks resolve by basename tree-wide, so
      co-location is the whole requirement; only an option that separates them owes a contract
      ruling (an `E2` blob) before it can land. Do not re-derive this from the earlier draft's
      wording — read `repo-audit.py:86-94` and `:128`.
- [x] 6. **C1 — land the ruled `E2` retirement.** Both sites in `CONSTRUCTION-CHECKLIST.md`
      (`:26` enumeration, `:34` count) in one commit. This is instruction-layer, so the round it
      lands in owes the opening `E10` cold read and an independent review; and per `E10` the
      amended text owes an independent read before any round relies on it.
- [x] 7. **Put the seven decisions to the user**, each with its measurement attached and its
      consequence for A2 stated. They are `D1`–`D7` in the table below. Do not proceed past this
      step without answers — `E1` and `R5` both forbid it.
      **Done 2026-08-08. It took four passes, and each pass was the user rejecting the framing, not
      the answer** — journal §10 (`HD-9`'s re-cut), §11 (three subject questions: format / when is it
      re-read / is it a verbatim copy), §12 (the real question: what is it FOR once it is a record),
      §13 (`D5`'s cut was never fixed; M5/M6 costed a different one). Rulings live in
      `ResearchSystem/HARNESS-DECISIONS.md` `HD-10`–`HD-17`, **not restated here** (`HD-5`:
      inherit as-is, never transcribe).
- [x] 8. **Dispatch one independent review of A1** (`rsc v3 dispatch --range BASE..TIP`) to a
      fresh-context reviewer; land its record and close the freeze window in that commit.
- [x] 9. **Write A2's own `/lite-plan`** from the answers, with the round split and each round's
      revert unit named. Then update `ResearchSystem/HARNESS-LEDGER.md` and close A1 out.

### A2 — construction, scoped only after A1 answers

**Superseded 2026-08-08 by the rulings.** The table below is left standing as the record of what A1
projected; **the live version is A2's own plan file** (step 9), and the rulings themselves are in
`HARNESS-DECISIONS.md`. What actually changed: **T3 and T4 are gone** (`HD-13`, `HD-1`), **T5/T6
changed cut** (`HD-15`/`HD-16` — submodule, members A+B+C only), **T8 gained a precondition**
(`HD-17` — survival audit first), and **two measurement tasks were added** that A1 had left unmeasured.

Nothing here can start before step 7. Each task names the decision it hangs on and what happens
under each answer.

| A2 task | Depends on | If the ruling goes the other way |
|---|---|---|
| **T1** template scripts copied → referenced | **D1** (§5.2), bounded by **M2** | if "keep copying", T1 vanishes and A2 loses its largest item — the ~2,000–2,658 lines per run stay |
| **T2** CheckResult stops being persisted, recomputed instead | **D2** (§5.3), bounded by **M3** | if "keep persisting", T2 vanishes; the 19% share stays |
| **T3** review-record form (what a record must show vs may cite) | **D3** (§5.4), evidence **M4** | if "unchanged", T3 vanishes. **Note:** T3 edits `REVIEW.md` / `CONSTRUCTION-CHECKLIST.md`, i.e. the instruction layer — its own round plus an `E10` read |
| ~~**T4**~~ decision homes re-cut | ~~**D4**~~ **done 2026-08-08** — the decision-log round re-cut the homes (four surfaces, `HD-1`); T4 leaves A2's scope | — |
| **T5** execute the repository split | **D5** (option) + **D6** (three hard problems) | option decides everything about T5's shape; there is no default |
| **T6** archive the plan into the new repo's `.goals/` | **D5** + **D6(a)**; `C1` already done in A1 | **M6** is a check, not a blocker: the chosen shape keeps plan and contract in the same repo so the link holds. Only an option that separates them owes a contract ruling first |
| **T7** run-v2 README layering landed | **D7** | three shapes: README joins `E10` (and owes reads), rules move to `EXECUTION.md`, or the classification stands and T7 vanishes |
| **T8** redeem rider `CLI-hist` — drop the `harness` and `stage` command groups plus their two live CLI tests | **D5** only (trigger, not shape — the rider already names the fix) | independent of D1–D4, D6, D7; can ride whichever A2 round touches `ResearchSystem/tooling/rsc.py`'s command registration |

**The decisions — all seven ruled 2026-08-08. Answers are NOT restated here** (`HD-5`: a plan
inherits a ruling as-is; transcription is a drift surface, and this batch has three measured
instances of exactly that). Read them in `ResearchSystem/HARNESS-DECISIONS.md` §live.

| id | Question as A1 finally managed to pose it | Ruling |
|---|---|---|
| D1 | Do runs stop carrying their own copy of the template scripts? | `HD-11` |
| D2 | Does a CheckResult survive the run that produced it? (**re-posed twice** — journal §4.1, §11.1, §12.1) | `HD-12` |
| D3 | What does the prose record hold that the machine result does not? (**re-posed twice** — journal §10, §11.2, §12.2) | `HD-13` |
| ~~D4~~ | ~~Does `SIMP-D`'s journal / ledger / commit-body split survive?~~ Answered by the decision-log round | `HD-1` |
| D5 | Which split shape, and **across which cut** (A1 had costed the wrong one — journal §13.2) | `HD-10`, `HD-15` |
| D6 | Which of the five groups travel? (the three "hard problems" dissolved under the corrected cut) | `HD-16`, `HD-17` |
| D7 | run-v2 README: joins `E10`, rules move to `EXECUTION.md`, or classification stands? | `HD-14` |

## Acceptance (done = ?)

**A1 is done when:**

- Eight runs measured on one method, with the per-run split and the product denominator, and the
  ~2,000–2,658-line copied-script figure either confirmed across the set or corrected by it.
- M2 / M3 each return an enumerated list of bindings, produced by reading the code rather than by
  reasoning about it; M4 returns a number; M5 returns three costed options; M6 states, per option,
  whether the plan and the contract stay co-located, and prices any option that separates them.
- `CONSTRUCTION-CHECKLIST.md` names three blobs and one directory, and the enumeration and the
  count agree with each other — checked by reading both sites, not one.
- All seven decisions answered by the user, each recorded where it will still be found: the ruling
  in `ResearchSystem/HARNESS-LEDGER.md`, the reasoning in a round journal.
- One independent review round completed, its record committed, freeze marker gone.
- A2's plan file exists on disk, with each round's revert unit named.

**A2 is done when:** defined by A1 step 9. Writing acceptance for it now would be inventing the
answers A1 exists to obtain.

## Resume pointer

当前指针: **A1 CLOSED — nothing resumes here.** Batch A continues in
[harness-a2-construction.plan.md](harness-a2-construction.plan.md); the split is its own later
batch (`HD-18`). A resuming session reads `ResearchSystem/HARNESS-LEDGER.md` → 
`ResearchSystem/HARNESS-DECISIONS.md` §live (`HD-5`) → the A2 plan — not this file.
Measurements: [journal/batch-a1-2026-08-08.md](../../document-harness/journal/batch-a1-2026-08-08.md)
§1–13. `C1` landed `55fe4e9`.

**Step 8 is blocked and it is not this session's to unblock**: `rsc v3 dispatch` needs a clean tree
and freezes the whole branch, and a second session has been holding
`.goals/plans/research-system-p5c-p8-revision.plan.md` modified in this worktree since 2026-08-07.
Owed with it: `C1`, the decision-log round and every A1 measurement commit carry no `E10` opening
cold read and no independent review yet.

Two questions the eventual review should judge, both found by self-audit rather than by a reviewer:

1. (2026-08-08 preclear) The "cold read MUST read `HARNESS-DECISIONS.md` §live" rule is carried by
   the README navigation row and the log header only — `EXECUTION.md` and `CONSTRUCTION-CHECKLIST.md`,
   the role instructions a cold read actually follows, do not mention it. A session entering straight
   through a role instruction would miss the obligation.
2. (2026-08-08, step 7) **Four of A1's own framings were wrong and the user caught all four, not the
   harness.** `D2` asked "persist or recompute" when recompute has no implementation (§4.1), then
   "how many of 13 fields" (§11.1), before the answerable question turned out to be "keep it after
   the run closes?" (§12.1). `D3` quoted a 55% that conflated three categories (§10) and treated one
   object where there are two (§11.2). `D5` was costed against a cut nobody had fixed (§13.2). The
   pattern is one thing: **A1 measured objects' roles in its own argument before measuring the
   objects.** Whether the harness owes a rule about that is the reviewer's call, not this session's.

## Notes

- **This batch cannot be one round.** The record-layer journal forbids it in its own opening line,
  and A1's output is decisions rather than files. Expect at minimum: A1 (one round) → A2 (several).
- **Do not let A1 drift into A2.** The measurable temptation is T1: `M2` will surface a concrete
  copies→references design, and writing it is not A1's job. Propose, cost, stop.
- **Sibling batch B** (`run_all` wiring · ledger binding degree · rider `RA`) is unstarted and
  unblocked by A. Named here only so a cold session does not re-derive the split.
- **Concurrency**: this worktree has had two sessions in it on 2026-08-07. A dispatch freezes the
  branch against everyone until the record lands. Check `git status` is clean before dispatching,
  and stage explicit paths only.
- `.goals/` is tracked, so this file is committable.

### What A1 actually found that this plan did not predict (2026-08-08)

Three of this file's own premises moved. All three are in
[journal/batch-a1-2026-08-08.md](../../document-harness/journal/batch-a1-2026-08-08.md);
named here so a cold session does not re-derive them.

- **The copies→references prize is ~1/3 of what Why projects**, and the achievable shape is
  "shared core + per-run delta" rather than plain referencing (journal §2). D1's framing changes
  accordingly.
- **`D2` as posed has no implementation.** "Recompute the CheckResult from `chk-*.out.txt` + spec"
  cannot work for `command_exit`: the verdict is `returncode in allowed_exit_codes`, and the
  returncode never reaches the `.out.txt` — `chk-manifest-unchanged.out.txt` is **0 bytes** while
  its CheckResult records `PASS`/`exit_code: 0` (journal §4.1). The real alternative to persisting
  is **re-running**, which is a different and larger proposition.
- **Hard problem (c) is 7–12 commits, not "276+".** That figure appears in **no** ledger file — it
  survives only in this plan's D6 row. Measured: 613 non-merge commits, 121 "mixed", of which
  **111 mix only with `.goals/`** (journal §6.2). Conversely **(b) is where the whole cost is**,
  concentrated in `generated/object-index.json`'s **362 live refs** into `Thesis/`/`Paper/`/
  `Knowledge/`/`ExperimentLab/` plus `chk-regen`'s requirement that a rebuild see both trees at
  once (journal §6.3).
- **`M2`'s known cost was narrower than journal §5.2 states.** `materialized_candidate` materializes
  the *whole repository* at the candidate commit, so a referenced script only needs to be
  **committed**, not to sit in the run directory — the runs already reference `rsc.py` and
  `Thesis/Work/Tooling/repo-audit.py` this way and it works. That cost belongs to the split, not to
  D1 (journal §3.1). The genuine in-run binding is `__file__`-derived roots plus CONFIG-block
  editing (journal §3.2).
