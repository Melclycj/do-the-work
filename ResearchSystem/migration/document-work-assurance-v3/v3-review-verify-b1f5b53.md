# Targeted VERIFY — split batch R3 repair, `eb6fbc2..b1f5b53`

**Verdict: `REVIEWED_NO_BLOCKER`.**

The verdict word is the only one available besides `SPEC_GAP` (`R3`), and there is no spec gap
here — so read it as what it is: *the accepted findings were repaired, the repair introduces no
defect in code, wiring or boundary, and nothing found is a spec question.* It is not "clean".
Three residuals of the very class the repair was written to sweep survive it, two of them inside
the repair's **own declared sweep scope**, and one of those two makes a single file contradict
itself. They are recorded below with the bytes named, because a VERIFY has no `CHANGES_REQUIRED`
and this round's fix leg is spent.

Both blockers are correctly closed. `B-1`'s false counterexample is gone and its replacement is
the general argument the reviewer asked for, with no substituted example, and I proved the
replacement true rather than read it. `B-2`'s enumeration now matches command output for every
site it names. `L-1` is corrected *past* the FULL — the executor reproduced the mutation, found
the reviewer's own classification short by two, and said so; I re-ran it and the executor is
right. `L-2`'s 26 reproduces. `L-3`'s ground is now the one that actually carries it.

**Findings: 0 blockers (none available), 3 residuals, 3 observations.**

---

## 1. Subject, re-derived

Everything below is re-derived from the repository. No reported figure was accepted (`R2`).

| | |
|---|---|
| Range | `eb6fbc21d8a38fe7a955ebe5fbe0b078fa3d1885..b1f5b53285d86c7861543471aacca707cc964581` |
| Branch / worktree | `document-work-assurance-v3` at `D:/Thesis-stage-control-refactor`; `HEAD` == range tip == `b1f5b53`. `git status --porcelain` empty at entry and at exit |
| Commits | 2, linear. `cf6ec32` `V3-REVIEW-RECORD-SPLIT-R3-eb6fbc2-v1` 2026-08-17 00:25:41 +1000, Kind: record · `b1f5b53` `V3-SPLIT-R3-FIX-v1` 09:55:43, Kind: review fix. author-date == committer-date on both — no amend or rebase evidence |
| Leg | The **targeted VERIFY** `E9` obliges. Re-derived, not accepted: exactly one review record exists for this round (`v3-review-full-eb6fbc2.md`, landed as `cf6ec32`), it returned `CHANGES_REQUIRED`, and no `*verify*` record for any commit in this chain exists. So the FULL has occurred, `b1f5b53` is the one user-approved fix, and this is the leg that closes the budget |
| Repair paths | 4: `.goals/plans/harness-repo-split.plan.md` +25 −8 · `ResearchSystem/HARNESS-POLICY.md` +6 −2 · `ResearchSystem/HARNESS-RIDERS.md` +4 −0 · `Thesis/Work/Tooling/repo-audit.py` +4 −2. (`git diff --name-status eb6fbc2 b1f5b53` also shows the review record as **A**; that is `cf6ec32`, not the repair) |
| Freeze marker | `.harness/review-pending.json` names **this exact range**, `dispatched_at 2026-08-16T23:56:03+00:00`. `b1f5b53` commits at 23:55:43 UTC — dispatch 20s later, and the branch has taken no commit since. `E9`'s "from dispatch to that commit the branch takes no commit but the record itself" holds on both legs: `eb6fbc2 → cf6ec32` is also direct |
| Push | `origin/document-work-assurance-v3` is at `f9786a8`, 4 commits behind `HEAD`. Nothing in this round is pushed. `E8` holds |
| Boundary | Every path is a site the FULL named (`B-1` → `repo-audit.py`; `B-2` + the sweep's sixth site → plan; `O-2` → policy; `L-4`/`O-1`/`O-3`/`O-4` → riders). Zero bytes in the harness repository: `git -C ResearchSystem/harness status --porcelain` empty, `git ls-files -s ResearchSystem/harness` still `160000 f65dcf2…`, and `git diff --name-only eb6fbc2 b1f5b53 -- ResearchSystem/harness` returns nothing |

## 2. Permanent boundaries

Checked, not assumed.

**`E2`.** Contract `b2dbdf75`, supersession-1 `68031fa2`, supersession-2 `e1a2f26b` — byte-identical
at `f9786a8`, at `eb6fbc2` and at `b1f5b53`. The schema pack holds 15 tracked files and
`git diff --name-only f9786a8 b1f5b53 -- ResearchSystem/schema/document-assurance-v3/` returns
**0** paths.

**`E10`.** All nine members, blob at `eb6fbc2` vs `b1f5b53`:

```
3af69265 3af69265 SAME  document-harness/CONSTRUCTION-CHECKLIST.md
e5c205ac e5c205ac SAME  document-harness/README.md
9f80e728 9f80e728 SAME  document-harness/EXECUTION.md
3350bfac 3350bfac SAME  document-harness/REVIEW.md
17ff31bb 17ff31bb SAME  migration/…/v3-harness-operating-contract.md
b576a45e b576a45e SAME  migration/…/v3-harness-review-contract.md
68031fa2 68031fa2 SAME  contract/…-supersession-1.md
e1a2f26b e1a2f26b SAME  contract/…-supersession-2.md
09aa8699 09aa8699 SAME  schema/…/paragraph-map.schema.json
```

The repair opened no amendment and needed none.

**`E8` form.** Title `V3-SPLIT-R3-FIX-v1`, single line, names the round. Body: **1** non-empty
line — one dense paragraph — and no trailers (`grep -E '^(Co-Authored-By|Signed-off-by|…)'`
returns nothing). Kind is named in the first clause. Paths were staged explicitly is not
observable after the fact (`R4`).

**Caller vs pin, re-measured** (the `pin-drift` row asserts it, so I did not take it):
9 of 9 members, 3 of 3 guards (`e6ce4941` / `468381fe` / `3e8a2b1e`) and `cli.py` (`e7308dc7`)
all SAME. The row's claim is true today and its point — that nothing *keeps* it so — is
untouched by that.

## 3. What I re-executed

All at the range tip, worktree clean, immediately before writing (`E3`).

**The battery — six commands, on the repaired tree.**

```
$ python ResearchSystem/tooling/tests/run_tests.py        tests: 29  passed: 29  failed: 0   OK
$ python ResearchSystem/tooling/tests/run_p4_tests.py     tests: 80  passed: 80  failed: 0   OK
$ python ResearchSystem/tooling/tests/run_p5a_tests.py    tests: 39  passed: 39  failed: 0   OK
$ python ResearchSystem/schema/fixtures/validate_fixtures.py
                                                          cases: 58  matched: 58  unexpected: 0  OK
$ cd ResearchSystem/tooling && python -m pytest -q         708 passed in 79.47s
$ python ResearchSystem/tooling/rsc.py compile --check     RESULT: generated output fresh; lint clean (exit 0)
$ python Thesis/Work/Tooling/ledger_cap_check.py           exit 0     (HARNESS-LEDGER.md = 120 lines)
```

29 / 80 / 39 / 58 / 708 / fresh — the repair's figures reproduce exactly, and the tier is still
right: the repair touches `Thesis/Work/Tooling/repo-audit.py`, so the tooling branch applies and
the doc-only exemption does not.

**`B-1`'s replacement reason is true, and I proved the mechanism rather than read it.**
`excluded()` at `repo-audit.py:55` is
`any(x in EXCLUDE for x in p.parts) or p.as_posix().startswith(SUBMODULES)`:

```
$ python -c "…"
name-in-EXCLUDE matches at depth 4: True     # Thesis/Work/deep/nested/harness/note.md
path-scoped matches that same path : False
path-scoped matches the real mount : True    # ResearchSystem/harness/README.md
```

So "`EXCLUDE` is matched against every path part at any depth … while a path-scoped prefix pins
this one mount and stays enumerable" is exactly what the code does. No example was substituted,
which the FULL required. The retracted counterexample's ground truth also holds:
`git ls-files ResearchSystem/tooling/rsclib/harness/ | wc -l` → **0**, directory contains only
`__pycache__`.

**The `SUBMODULES` exclusion is still must-fire after the edit** (`E4`, `R8`), neutered and
restored from a sha256-checked scratchpad copy, never `git checkout --`:

```
# as committed
scope: 497 markdown files    [OK] Broken markdown links: 0     [~~] Orphan notes: 251
# mutation: SUBMODULES = ()
scope: 644 markdown files    [!!] Broken markdown links: 15    [~~] Orphan notes: 358
# restore
$ sha256sum Thesis/Work/Tooling/repo-audit.py
899cb084824fec48f63cd26851301d3ae9bb7aadb4abe5f42535f66f3085f571
$ git status --porcelain     # empty
```

497 / 644 and 251 / 358 rather than the FULL's 496 / 643 and 250 / 357 — the delta is exactly
`+1`, the review record `cf6ec32` added. The broken-link count is unchanged at **15**.

**`L-1` re-run, and the executor's correction of the reviewer is right.** Classifying the 15
targets by hand from the mutation output: `.goals/plans/*` = **6** (lines 1, 2, 4, 5, 7, 15),
`assurance/shadow/*` = **4** (8–11), record-class = **5** — `REVIEW.md → v3-review-full-fef3a2e.md`,
`journal/simp-a4-2026-08-06.md → v3-review-full-285c596.md`, `W2-design.md → v3-cold-read-e90243a.md`,
and `v3-review-full-c6d4eb4.md →` both `v3-review-full-0439efe.md` and `v3-review-verify-d55d5ce.md`.
6 + 4 + 5 = 15. The FULL said three records and I was wrong by two; the repair names precisely
the two I missed. `E12` observed — it reproduced to write the fix, not to adjudicate me, and
disclosed that the finding came out heavier than reported.

**The three guards fire from the submodule, with a negative control.** My first attempt returned
exit 0 and I nearly wrote it down: I had `git add`-ed an unmodified file, so nothing was staged,
and my `$?` was `tail`'s, not the hook's. Both errors are mine and are recorded because this is
the class under review. Redone:

```
$ printf 'probe\n' > tmp-verify-probe.md && git add tmp-verify-probe.md
$ python …/hooks/review_freeze_check.py
pre-commit BLOCKED: a review/read is out (E9: …)
  marker : D:\…\.harness\review-pending.json  (subject eb6fbc21…..b1f5b53…)
  staged : tmp-verify-probe.md  (not a review record)
exit 1
$ sh .githooks/pre-commit                                     exit 1   # chain propagates
# negative control — staged path matching R6's record families
$ git add …/v3-review-verify-deadbeef.md ; python …/review_freeze_check.py   exit 0
$ git reset -q ; git status --porcelain                       # empty
```

All three scripts are `PRESENT` under `ResearchSystem/harness/ResearchSystem/tooling/hooks/`.

**The repair's own new text passes the path guards.** `candidate_path_check.scanned()` covers the
plan and `HARNESS-POLICY.md`; `HARNESS-RIDERS.md` is in `RECORD_SURFACE` and `repo-audit.py` is
not Markdown, so neither is scanned. Driving `unresolved_path_tokens` over the repair's added
lines for the two scanned files: plan 25 added lines → **NONE**; policy 6 added lines → **NONE**.

**`O-2`'s three factual claims, all verified.**
`git config --show-origin --get core.hooksPath` → `file:D:/Thesis/.git/config  .githooks`;
`git worktree list` returns **4** worktrees sharing that config (`D:/Thesis` on `main`, a
scratchpad detached one, `D:/Thesis-intake`, and this one); `git ls-tree origin/main -- .githooks`
is empty and `D:/Thesis/.githooks` does not exist on disk. So "范围是整仓" is the right scope and
the narrower "别的分支" was indeed wrong. `D:/Thesis/.git/hooks/` now holds `*.sample` only — the
predecessor is gone, as the body says, and that deletion is correctly declared a machine action
outside every commit.

**`O-5` reproduces through the mount.**
`python ResearchSystem/harness/…/dtw.py status --state ResearchSystem/assurance/runs/p5b-claims/control/state.json`
→ exit 0, prints `work_id p5b-claims-load-bearing-mint` / `status CLOSED`. The Acceptance line is
literally satisfiable; whether to split it stays R4's, as routed.

**Bookkeeping.** Rider rows: `awk 'NR>10 && /^\| /' | wc -l` → **27** at `f9786a8`, **26** at
`eb6fbc2`, **30** at tip. The plan's new net-change sentence (删 2 / 加 1 / 修腿再加 4) is
arithmetically exact, and the command it now prints instead of a frozen number runs and returns
30. `L-2`'s corrected 26 is right. `chk-ledger-note` appears in **1** of **8** run directories
(`p4-bridge`) — the §4 reason ② tally holds. Ledger 120 lines, cap check exit 0.

**`L-3`'s new ground, checked against primary sources.** `EXECUTION.md:329` is in the tiering
section's *second* bullet ("Schema, tooling, or generated surfaces touched"), which is the branch
R3 used, and it reads `these six commands and nothing fewer` with the note that "It was eight
until `HD-42`". `HD-42` (archive) states its own consequence in as many words: 该编辑仍是对 `E10`
成员 `EXECUTION.md` 的写入，按 `E10` **仍欠该层的一次独立 read** … 本条只免「开设计轮」，不免读.
And `HD-39`'s deletions are real — `ResearchSystem/tooling/tests/harness/` and
`…/tests/stage_control/` hold **0** tracked files and the two `run_tests.py` are absent. So the
corrected reasoning is sound in all three parts, the debt is correctly still carried, and the
checklist/README deferral is correctly kept in the free channel.

**`B-2`'s named sites, re-derived.** `cli.py`: `grep -c '"--repo-root"'` → **4**
(`:459` `:471` `:499` `:536`); `args.repo_root` resolution points → **5** at `:38` `:75` `:142`
`:324` `:409`. run-v2: `grep -n 'REPO = args.repo_root'` → the four scripts at `run_bind_v2.py:170`,
`run_evidence_v2.py:121`, `run_repair.py:63`, `run_retire.py:98`. Every line number and every
count the rewritten step 19 prints is what the command prints. Both prefixes are travel prefixes
in `split-travel-manifest.md` (`ResearchSystem/tooling/rsclib/document_harness`,
`ResearchSystem/assurance/templates/run-v2`), so the ruling — doing step 19 in R3 means opening a
round inside the harness repository — is confirmed independently.

## 4. Residuals

All three are the class the repair exists to sweep: an assertion whose scope exceeds the command
behind it, or a fix applied where the finding pointed rather than across the class. Two of them
sit inside the repair's **own declared sweep scope** — the body declares 量程 = `base f9786a8` 到工作树的
净 diff 的 `+` 侧，覆盖本轮全部改动路径, and asserts 更正后的量程下共 6 条计数断言，逐条有命令背书.
That last assertion is false: the `+` side of that exact scope carries at least two further count
assertions with no command behind them, one of which the same round's own command refutes.

### `V-1` — the plan contradicts itself: `:9` still says 两处, `:253` says 两处 was wrong

**Location.** `.goals/plans/harness-repo-split.plan.md:9`, on the `+` side of
`f9786a8..b1f5b53`:

> ② 步骤 19 **移出 R3**（实测：两处 `--repo-root` 都已在 harness 仓）

The repair rewrote item ③ of that same bullet — lines 10–17, the `L-3` correction — and left
item ② one line above it carrying the exact figure `B-2` blocked. Meanwhile the same file at
`:253` now reads 初版写「两处」，实为九个 site 分布在五个文件. One file, two answers, and the wrong
one is in the status block a reader meets first.

```
$ git diff f9786a8 b1f5b53 -- . ':!…/v3-review-full-eb6fbc2.md' | grep '^+' | grep -c '两处 `--repo-root` 都已在 harness 仓'
1
$ grep -n '两处 `--repo-root` 都已在 harness 仓' .goals/plans/harness-repo-split.plan.md
9:  免得同一批链改两遍）② 步骤 19 **移出 R3**（实测：两处 `--repo-root` 都已在 harness 仓）
```

**Bytes.** Replace 两处 in `:9` with a pointer rather than a number — e.g.
（实测：全部 site 都已在 harness 仓，清单见步骤 19）— so the status block cannot drift from the
enumeration again.

### `V-2` — `HARNESS-LEDGER.md:103` carries both defects verbatim, and it is the live pointer

**Location.** `ResearchSystem/HARNESS-LEDGER.md:103`, the split-batch row, rewritten by `eb6fbc2`
and therefore also on the `+` side of the declared scope:

> ② 步骤 19 `--repo-root` 移出本轮（实测**两处**都已在 harness 仓）③ 指令层三个变更成员欠的独立
> read 按丙处理，**不省电池档故不构成 `E10` 的 relied**、债务挂到下次层 read

Both retracted statements, unedited. The second is the one the plan now says 站不住.

**Ground truth it violates.** `B-2` established 两处 is 9 sites in 5 files; `L-3` established the
`E10`-relied reasoning does not carry the deferral. This repository's own `CLAUDE.md` designates
this file the harness track's live pointer — *"the whole file is the live pointer — state, next
step, the rider bank, and the user rulings that exist in no other file"* — and instructs a new
session to read it first. So the two statements a cold session meets first are the two this round
retracted, while the corrections live in the plan and in a commit body.

This is `HD-41` ④ precisely: 只修 finding 点名那处，不扫同一断言的其他写法. A `grep '^+' | grep 两处`
over the declared scope would have returned it.

**Bytes.** In `:103`, ② → （实测：全部 site 都已在 harness 仓，清单见 plan 步骤 19）; ③ → drop the
不省电池档 clause and state the ground the plan now gives (`HD-39` 同 commit 删掉两棵 runner 树，故新旧
文本下电池同为六条), or reduce ③ to the debt itself and let the plan hold the reason. The row also
still reads **R3 候选已落 `a14d203`，待 FULL**, which the FULL and this VERIFY have overtaken; if
the convention is that R4 refreshes it at closeout, that is fine and this sentence is not part of
the finding.

### `V-3` — step 19's rewritten site list is still short by two, inside its own declared 量程

**Location.** `.goals/plans/harness-repo-split.plan.md:250-263`. The step declares
量程 = `rsclib/document_harness/cli.py` 全文 + `assurance/templates/run-v2/*.py` and then
enumerates **run-v2 模板四个脚本各带同一句** `REPO = args.repo_root…else run_dir.parents[3]`.

**Ground truth it violates.** The debt step 19 exists to pay is named by `io-design` §7 as
`--repo-root` 默认 `run_dir.parents[3]`（深度假设） — the depth default, not the flag. Over the
declared 量程 that class has **six** members, not four:

```
$ grep -n 'parents\[3\]' ResearchSystem/assurance/templates/run-v2/*.py
check_template_instance.py:188:    repo_root = pathlib.Path(argv[2]) if len(argv) > 2 else run_dir.parents[3]
make_paragraph_map.py:30:          repo_root = pathlib.Path(argv[2]) if len(argv) > 2 else run_dir.parents[3]
run_bind_v2.py:170:    REPO = args.repo_root.resolve() if args.repo_root else run_dir.parents[3]
run_evidence_v2.py:121: REPO = args.repo_root.resolve() if args.repo_root else run_dir.parents[3]
run_repair.py:63:      REPO = args.repo_root.resolve() if args.repo_root else run_dir.parents[3]
run_retire.py:98:      REPO = args.repo_root.resolve() if args.repo_root else run_dir.parents[3]
```

The command the round ran (`grep 'REPO = args.repo_root'`) returns 4; the command covering the
declared 量程 returns 6 — `HD-41` ① exactly. The two missed scripts take the repo root as a
**positional** `argv[2]` with no `--repo-root` flag at all, so for them step 19 is not "pass it
explicitly" but "add the parameter first, at every call site" — strictly more work than the
sizing text shows. Both also carry
`sys.path.insert(0, str(repo_root / "ResearchSystem" / "tooling"))`, the prefix the same
re-rooting round drops.

**What survives.** The ruling, again and more strongly: both extra files are under
`ResearchSystem/assurance/templates/run-v2`, a travel prefix, so every site is still in the
harness repository. What does not survive is the sentence the repair itself wrote about the
initial version — 照初版枚举施工会改一个文件、留三个兄弟带着同一缺陷 — which is now true of the
corrected version at 四个文件、留两个兄弟.

**Bytes.** Add to the run-v2 clause: `check_template_instance.py:188` · `make_paragraph_map.py:30`
（同一 `run_dir.parents[3]` 默认，经位置参数 `argv[2]` 而非 `--repo-root`，故须先加参数）, and state
the 量程-covering command (`grep -n 'parents\[3\]' …/run-v2/*.py`) rather than the narrower one.

## 5. Observations

`R5` — whether any of these should change anything is the user's, not mine.

- **`O-A` — this class has now survived three consecutive sweeps of itself.** `HD-41` ④ records
  that 写下它的下一个 commit 就没执行. The FULL then found two blockers of the class plus two lows.
  The repair, written expressly to 一次扫类修完、而非五处点修, declared a scope, ran a command
  narrower than it, asserted 逐条有命令背书, and left three residuals — one of them a
  self-contradiction between two lines of the same paragraph it was editing. `HD-41` chose
  discipline plus 留痕 over machinery on `E6` grounds, and `HD-41` itself notes 本条与指令层的关系 …
  是下一个设计轮的题. I report the shape and stop: three data points is a trend, and whether the
  discipline-only choice is holding is a question, not a conclusion I get to draw.
- **`O-B` — two of the four new rider rows declare their fix `design` but name 下一批 as the
  redeem-when surface.** `mount-inert` (都是给现有规则加一条要求 = design) and `pin-drift`
  (加一致性检查是新机器（`E6`）) both write 下一批碰 …, where the three precedent design-shaped rows
  (`battery-travel`, `wl-route`, `tier-file-vs-clause`) all write 只点名**有资格开轮**的表面 and
  cite `HD-37` ② by name. No damage follows in these two cases — the surfaces they name
  (`.githooks/pre-commit`'s `H`, `layer_path_check.LAYER`, the resync flow) are not `E10` members,
  so the `E10`-amendment-meets-but-cannot-redeem hole `HD-37` ② closes cannot open on them, and
  both carry a well-formed deadline outside this round. It is the wording that has drifted from
  the precedent, not the outcome.
- **`O-C` — `nonrec-clone` carries 无 deadline where the defect does have a biting moment.**
  `R10` requires a deadline when a finding's value expires. The row argues 只在非递归 clone 上咬人，
  本机不发生 and points at the re-rooting round for self-resolution, which is a real argument and
  has precedent (`frozen-path-prefix` carries 无 deadline the same way). But the split's whole
  purpose is that a second caller clones this repository, and that is the moment. Whether "the
  first non-recursive clone by anyone" is a usable deadline or an unbounded one is the user's call.

## 6. Unverifiable, and ceilings

Stated, never folded into supported (`R4`).

- **The user's approval of the fix table (2026-08-17), and the 裁乙 ruling routing `L-4` to the
  bank.** Both are recorded in `b1f5b53`'s body and the `design-route` row, so they are in the
  repository; the act of ruling is not inspectable. `R7`: a ceiling, stated, not a block. Same for
  `E11`'s preview card for this leg, which is nowhere in the repository — as it was at the FULL.
- **`E8`'s "stage explicit paths, never `add -A`".** Not observable after the fact.
- **Whether the repair commit passed the hook chain or used `--no-verify`.** No artifact survives.
  I established instead that the guards fire now and that the repair's own added text produces no
  unresolved path tokens, which is the property that matters.
- **The scratchpad backup of the deleted `D:/Thesis/.git/hooks/pre-commit` (sha256 `e695d000…`).**
  I verified the file is gone and that only `*.sample` remain; the backup itself is outside the
  repository and I did not go looking for it.
- **Mutation caveat.** §3 proves the `SUBMODULES` clause and the freeze guard have binding force.
  It does not prove that force is sufficient, and a VERIFY is never a re-certification (`R4`) —
  the two path guards I exercised through their library rather than through a staged commit, and
  I did not re-run the FULL's `layer_path_check` must-fire pair, because the repair changed
  neither guard.

## 7. Coverage

**Read in full:** `CONSTRUCTION-CHECKLIST.md`, the review-contract stub, `HARNESS-DECISIONS.md`
(all 11 `§live` entries and all of `§implemented`), `v3-review-full-eb6fbc2.md`, the complete diff
of the repair's 4 paths, `.githooks/pre-commit`, `review_freeze_check.py`,
`candidate_path_check.py`, `HARNESS-RIDERS.md`'s four new rows and the header, `repo-audit.py`
lines 30–72.

**Sampled:** `HARNESS-DECISIONS-archive.md` (`HD-42`, the head of `HD-39`), `EXECUTION.md`
(the tiering section, `:317-345`), `io-design.md` (§7, §8, the section index),
`split-travel-manifest.md` (the prefix block and §A), `HARNESS-POLICY.md` §3,
`HARNESS-LEDGER.md` (the split-batch row and its neighbours), the plan (head, step 19, step 20,
the closing summary — not the whole file), `check_template_instance.py` and `make_paragraph_map.py`
(their `main()` heads only).

**Probed only:** the seven battery/cap legs, the `SUBMODULES` mutation and its sha256 restore, the
freeze guard's must-fire and negative-control pair, `unresolved_path_tokens` over the repair's
added lines, `E2` and `E10` blob stability, caller-vs-pin parity, the `--repo-root` and
`parents[3]` sweeps, rider row counts at three revisions, `chk-ledger-note` across the 8 run
directories, `core.hooksPath` origin and `origin/main` content, `git worktree list`, and
`dtw status` through the mount.

**Worktree at exit:** `git status --porcelain` empty apart from this record, which is untracked
until the orchestrator commits it (`R6`). `HEAD` = `b1f5b53`, `repo-audit.py` sha256
`899cb084…f571`.
