# Targeted VERIFY — `dbbec288e816c2ab35f09aa1b02edaaca9f955ba` (batch B, round R1 repair)

**Verdict: `REVIEWED_NO_BLOCKER`.** Both accepted blockers are closed and measured closed.
2 residual findings, 1 wording note, 1 independence ceiling disclosed below.

`B-1` is shut: the guard that passed under its own defect now fails under it, at value level,
with the message the leg quotes. `B-2` is shut where it can be: every digit and digest in the
repair commit reproduces against the bytes that shipped — I re-took all three mutations and the
whole battery rather than reading the account of them. The repair is the supplied line and
nothing else; the template took no byte in this range.

The residuals are both carriers, not code. The plan still records the falsified mutation figures
`B-2` was about, in a file this range edited twice; and rider `RA`'s corrected row states a
caller count that the R2 batch will read to scope itself, and states it low.

## 1. Subject, re-derived (`R2`)

```
$ git rev-parse HEAD              -> dbbec288e816c2ab35f09aa1b02edaaca9f955ba
$ git status --porcelain          -> (empty)
$ cat .harness/review-pending.json
  {"subject": "e9166d28…..dbbec288…", "dispatched_at": "2026-08-11T16:27:10+00:00"}
```

Three commits, twelve lines of payload between them, classified by hand:

| commit | title | paths | kind |
|---|---|---|---|
| `1025491` | `V3-REVIEW-RECORD-B-R1-e9166d2-v1` | the FULL record, +285, sole content | record (`R6`) |
| `0458bfb` | `V3-REVIEW-BANK-B-R1-v1` | `harness-batch-b.plan.md`, `HARNESS-RIDERS.md` | bank / bookkeeping |
| `dbbec28` | `V3-REVIEW-FIX-B-R1-v1` | `…/test_run_v2_template_check_order.py` | the repair leg |

**Round, budget, obligations.** `HD-25` authorized R1; FULL `e9166d2` returned
`CHANGES_REQUIRED` with `B-1`, `B-2` accepted into the repair and `L-1`/`L-2`/`L-3` routed
riders-only. `E9`'s ledger for this round therefore reads: FULL spent, one user-approved fix
spent at `dbbec28`, this VERIFY is the last leg. The bank commit changes no reviewed work
product (plan and rider bank only), so under the 2026-08-04 ruling it consumes nothing — I
checked its contents rather than its label, and no template or suite byte is staged in it.

**`E9`'s dispatch clause holds on both legs.** The FULL was dispatched 15:28:54Z and its record
landed at `1025491` (15:56:34Z) with no other commit between; this VERIFY was dispatched
16:27:10Z, after `dbbec28` (16:09:28Z), and the branch has taken nothing since. Nothing is
pushed (`origin/main..HEAD` = 616, user-gated).

## 2. Independence — the ceiling on this record (`R1`, `R4`)

This VERIFY was routed by the user, not by the executor, and nothing about its question was set
by the session under review — `R1`'s test is met. But it is **not fresh context**: the same
session wrote FULL `e9166d2`, so its independence from *the FULL's own reasoning* is nil, and the
template's `next_action_for` string asks for a fresh-context reviewer. What that costs is
specific and worth naming: a genuinely fresh reviewer might have judged `B-1`'s supplied fix
wrong, and I cannot; I can only confirm the fix does what I said it would. Marked, not verified
(`R4`). Everything in §3–§5 is re-measured from commands, not carried over.

## 3. `B-1` — closed, measured

The repair is the supplied literal plus a seven-line comment that states the defect it exists
for. Nothing else moved: `run_evidence_v2.py`'s blob is `e43cfa33…` at both ends of the range
and `git diff --name-only e9166d2..dbbec28 -- …/templates/` is empty, so the leg's stated
boundary — the suite alone — holds by inspection rather than by claim.

Applied the defect the class names (`plan.get("check_order", [])` → `plan["check_order"]`) to
the delivered template:

```
1 failed, 7 passed
FAILED …::APlanWithNoCheckOrderRunsNoChecksAndDoesNotCrash::test_no_order_means_no_check_runs
E  AssertionError: 'deterministic checks : 0/0 PASS' not found in [] :
```

Value-level red, not a crash, and the same test passed 8/8 under this mutation before the fix
(`e9166d2` `B-1`, measured there). That is the whole claim of the leg and it holds. The
assertion is a hand-written literal asserted whole against `output.splitlines()` (`E5`), it adds
no machinery (`E6`), and the line it names is printed only after `run_all` returns, so no run
that died on the way in can reach it.

**What this does not prove (`R4`).** Mutation shows the guard now has binding force, not that its
force is sufficient. One sibling keeps the same shape the finding was about —
`test_the_filename_sort_is_not_the_order` asserts only a `assertNotEqual`, which an empty `seen`
also satisfies — but its class-mate `test_checks_run_in_the_plans_check_order` fails on that
same state, so the property is held at class level. Untouched by this range and not a finding of
it; recorded so the shape is not re-discovered as new.

## 4. `B-2` — closed, every figure re-taken

The defect was evidence describing bytes that were never delivered. The test of the fix is
therefore not whether the leg says it re-measured but whether its numbers reproduce. All of them
do, re-run by me against the subject tree:

| claim in `dbbec28` | re-measured |
|---|---|
| template `ae3f6c78…` | `ae3f6c789dd4b4c5e5e72bae76f478d2262f39713507b872ad60ab50afe3f393` ✔ |
| suite `228e2bfa…` | `228e2bfa170cb9afe69f72ee4632f4c2b1619b0f2e4178be1899e8f9945c04c0` ✔ |
| M1 order source → filename sort: 7 failed, 1 passed | 7 failed, 1 passed ✔ (survivor `test_the_refusal_names_the_uninterpretable_request`, as last round) |
| M2 stop removed: 4 failed, 4 passed, the stop family | 4 failed, 4 passed, exactly that family ✔ |
| M3 subscript: 1 failed, 7 passed | 1 failed, 7 passed ✔, message verbatim |
| `tests/run_tests.py` 29 · `pytest -q` @ `ResearchSystem/tooling` 705 · `tests/harness` 39 · `tests/stage_control` 20 · `compile --check` exit 0 | 29 ✔ · **705 passed in 82.72s** ✔ · 39 OK ✔ · 20 OK ✔ · exit 0 ✔ |

Each mutation restored from a sha256-checked scratchpad copy, never `git checkout --`; the
worktree is clean and both digests are back to the values above. The leg also re-ran the six
battery legs rather than four, which is the same reading of rider `tier-scope` R1 took.

My own record is committed unaltered — `sha256` of `1025491`'s blob equals the file I wrote
(`2fd23644…`) — and it is the sole content of that commit, as `R6` requires.

## 5. The bank leg (`L-1`, `L-2`, `L-3`) — checked, not re-litigated

- **`L-1`** The plan's `status` and resume pointer now carry where the batch stands, name the
  FULL's verdict and record SHA, and route the next action to the owed VERIFY before R2. The
  misroute the finding named — a cold session re-opening R0 — is gone.
- **`L-2`** Rider `RA` no longer says zero callers, names the template, keeps its redeem-when and
  gains a deadline at R2's opening. See `V-2` for what the new wording still gets low.
- **`L-3`** Rider `tier-scope` ① now records that its deadline fired in this batch, with the six
  legs and their counts, that `EXECUTION.md` was not amended, and that the user deferred the
  design round on 2026-08-12 — and, correctly, that the defect therefore stands and the next
  tooling-touching batch is still protected by nothing but the executor happening to know.
  Recording the deferral rather than the survival is the right shape: a fired deadline that
  leaves no mark reads afterwards as one that never came.

Separating the bank from the repair is `L-4`'s lesson applied rather than restated; the fix
commit carries one path.

## 6. Residual findings

### `V-1` — the plan still asserts the falsified mutation evidence as R1's evidence

`.goals/plans/harness-batch-b.plan.md:71-73`, step 6, still reads "还原后哈希复等 `a59cc546…`"
and "**M1** … 杀 6/7" — the exact digest that matches no delivered artifact and the exact count
that belongs to a seven-test suite. Both were superseded by `dbbec28`'s re-measurement; the plan
carries no marker that they were, and this range edited that file twice.

**Why it is not closed by the commit body.** `E8` forbids amending `e9166d2`, so the commit-body
copy is immutable and everyone accepts that. The plan is not: it is the cold-resume document —
its own resume pointer tells a new session to read it second, before the FULL record — and it is
where an auditor of R1's `E4` discharge lands first. Leaving the falsified figures there, with
the correction reachable only from a commit body two commits later, reproduces `B-2`'s failure in
the one carrier that could still be fixed.

**Bytes** (riders/plan-only, so free under the 2026-08-04 ruling and no fix leg is left to
spend): append to step 6 — *本步骤的 mutation 证据已由修腿 `dbbec28` 对交付字节重测取代：模板
`ae3f6c78…`、套件 `228e2bfa…`；M1 7/8、M2 4/4、M3 1/7。上面的 `a59cc546…` 与 6/7 属未交付的中间
版本，勿引用。* **Deadline: closeout of R1** — after that the plan is read as the settled account
of the round.

### `V-2` — rider `RA`'s corrected row states the caller surface low, and mis-dates its own correction

The new row says `run_all` 现有**一个**调用者 and that the old wording "全仓零调用者" became false
*from* `e9166d2`. Measured: `run_all` has three call sites — the template, and
`tooling/tests/document_harness/test_candidate_checks.py:874` and `:887`, which have been there
since `11ce5b4` (2026-07-28), the very commit whose FULL is this rider's source. So the old
wording was never literally true, and the new count is literally low by two.

**Why it matters where it sits.** The row's own new deadline is "R2 开轮——该批要读本行给自己划
范围". R2 is the batch that may reshape `run_all`'s contract (the FULL's `O-1` — partial results
on the exception — would change its signature), and those two tests are exactly what pins that
contract today: one asserts a check ordered after the gap never ran, the other is its negative
control. A batch scoping itself from "one caller" undercounts its own blast radius.

**Bytes**: 一个**产品**调用者（run-v2 evidence 模板），另有两处单元测试调用
`tests/document_harness/test_candidate_checks.py:874/887`（自 `11ce5b4` 起，钉住 `run_all` 的
stop 契约与其负对照）；原文"全仓零调用者"指的是产品侧，从来不是字面全仓。 Riders-only, free.
**Deadline: R2's opening**, the same one the row already carries.

### `W-1` — wording-level (`R9`), spawning nothing

The plan's `status` line says 修腿进行中; the repair landed four minutes after the bank commit
that wrote it. No actor acts wrongly on it — the adjacent resume pointer already says a targeted
VERIFY is owed once the repair lands, and `git log` settles the rest — and closeout rewrites the
line anyway. Named here only so it is not re-found as new.

## 7. Permanent boundaries (`R3`, however narrow the round)

- **`E2`**: no path under `ResearchSystem/schema/` or `ResearchSystem/contract/` appears anywhere
  in `e9166d2..dbbec28`. The pack is still exactly fifteen files.
- **`E10`**: all nine member blobs at `dbbec28` are byte-identical to their values at `e9166d2`,
  which I re-derived last round against `v3-checkpoint-read-3f19561.md` §1 — so no amendment
  rides this range and no read is owed by it. (These are also my own standing instructions:
  `44d622b9…` and `52a97a48…`, unchanged since I read them.)
- **`E8`**: three new commits, none an amend, none pushed, each single-purpose with its kind named
  in title and body; the repair leg carries one path and stays inside the boundary it declares.
- **`E12`**: the handoff was one range; the executor reproduced `B-1` before writing the fix and
  said so in the terms `E12` uses — to write the fix correctly, not to adjudicate the reviewer.

## 8. Worktree integrity after review

```
$ git status --porcelain   -> (empty)
$ git rev-parse HEAD       -> dbbec288e816c2ab35f09aa1b02edaaca9f955ba
$ sha256sum run_evidence_v2.py               -> ae3f6c78…f393
$ sha256sum test_run_v2_template_check_order.py -> 228e2bfa…c04c0
```

Three mutations applied and restored from the checksummed copy; no `git checkout --`; the branch
has taken no commit during this review.
