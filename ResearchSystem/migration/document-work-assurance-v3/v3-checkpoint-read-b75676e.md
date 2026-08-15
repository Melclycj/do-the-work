# Split-batch R0 — re-read of both `M-1` amendments and both free-channel applications `feb7b4872c14108cfc1e6b9f0a710ec33ff10ea4..b75676e8f9e26c8c762f8171c9b95a28ad13d882`

Independent read of the five commits that answer the R0 read (`feb7b48`,
`v3-checkpoint-read-ffbc393.md`) and the re-read of its free-channel application (`6a946ba`,
`v3-checkpoint-read-0cc45ce.md`). This is the re-read both prior records recorded as still
owed: each earlier dispatch took the preceding amendment as its base and so excluded that
amendment's own bytes; this range covers all of them. **Not a round** (`R3`): no verdict, no
budget consumed. Output is findings tiered must-fix / low / observation.

**Findings: 2 must-fix, 3 low, 7 observations.**

Every corrected figure in the range re-derives **exactly** — the seven-path 335/720 and the
mid-round 337/724, the 245/247 of the other path set, the 171/139/32 deletion arithmetic, all
thirteen links with their line numbers, both `HD-40` digests, the LF/CRLF mechanism, the ten-item
`EXCLUDE`, the seven `_cmd_v3_*` offsets, the eight in-block handlers. The two must-fixes are not
in any of those numbers.

`M-1`: both must-fix answers were applied at the site the finding named and nowhere else. Three
siblings survive — including `split-design.md` §10.2, which carries the *original* under-counted
connected list verbatim and which §0's own conflict rule (*冲突时以 §10 与 `HD-39` 为准*) makes
authoritative over the §7 that was corrected. `M-2`: the plan R1 executes from still inherits
`HD-24` — superseded, archived, and reversed — and step 11 instructs R1 to **move** the seven
trees that `HD-39` **deletes**; no deletion step, and no fix for the thirteen links, exists
anywhere in R1's checklist or its Acceptance.

## 1. Subject, re-derived (`R2`)

Handed one range and nothing else. Round, budget, authorization, obligations and every figure
below are re-derived here; nothing is taken from the dispatch prompt, a commit body, the plan,
the ledger, the design document or either prior record.

```
$ git rev-parse HEAD               -> b75676e8f9e26c8c762f8171c9b95a28ad13d882   (== range tip)
$ git rev-parse --abbrev-ref HEAD  -> document-work-assurance-v3
$ git status --porcelain           -> (empty)
$ git rev-list --count feb7b487..b75676e8 -> 5
$ cat .harness/review-pending.json
  {"subject": "feb7b4872c14108cfc1e6b9f0a710ec33ff10ea4..b75676e8f9e26c8c762f8171c9b95a28ad13d882",
   "dispatched_at": "2026-08-14T05:36:03+00:00"}
$ git log -1 --format=%cI b75676e   -> 2026-08-14T15:35:56+10:00  (= 05:35:56Z)
```

HEAD equals the tip and the tree is clean, so worktree reads are reads of subject bytes. The
freeze marker's subject is byte-equal to the dispatched range and post-dates the tip by seven
seconds; no commit has landed since dispatch (`E9`'s from-dispatch-to-record clause holds so far).
`.harness/` is gitignored (`git check-ignore -v` → `.gitignore:19`), so the marker deletions the
record commits describe are filesystem actions, never diff content — consistent, no finding.

**Five commits, classified by hand** (`R2`):

| # | sha | title | kind, as read from the diff |
|---|---|---|---|
| 1 | `6208b35` | `V3-SPLIT-R0-AMEND-M1-v1` | amendment — answers `ffbc393`'s `M-1` |
| 2 | `0cc45ce` | `V3-SPLIT-R0-FREE-L1-L2-L3-O1-O2-O5-v1` | free-channel byte application |
| 3 | `6a946ba` | `V3-SPLIT-R0-REREAD-RECORD-0cc45ce-v1` | record — the read of #2 |
| 4 | `f4c9902` | `V3-SPLIT-R0-AMEND-M1B-v1` | amendment — answers `0cc45ce`'s `M-1` |
| 5 | `b75676e` | `V3-SPLIT-R0-FREE-L1-L2-L3-O1-O3-O4-v1` | free-channel byte application |

**Five paths changed**, classified by hand:

```
$ git diff --numstat feb7b487..b75676e8
 7   5   .goals/plans/harness-repo-split.plan.md                                  plan (resume artifact)
27   6   ResearchSystem/HARNESS-DECISIONS.md                                      decision register — NOT an E10 member (HD-19)
29  11   ResearchSystem/document-harness/journal/repo-split-r0-2026-08-13.md      round record (measurement)
65  16   ResearchSystem/document-harness/split-design.md                          design product, user-signed at 3f4d2b0a (HD-40)
334  0   ResearchSystem/migration/.../v3-checkpoint-read-0cc45ce.md               review record (R6)
```

**Round, budget, obligations — derived.** The round is 拆分批 **R0**, plan
`.goals/plans/harness-repo-split.plan.md`, `status: R0 OPEN 2026-08-13`, `base_commit 0db52a1`
(base written, tip unwritten — `E12` satisfied). Plan Notes: *`E9` 预算一轮一算：R0 用 `E10` 独立
read（无 FULL 预算）*. `E9`'s own test settles it independently of what anything is called: **no
valid independent FULL has occurred for R0**, so every commit in this range is a pre-submission
correction and consumes nothing; the fix leg and the VERIFY are unspent. Live rulings visible in
the repository that bind this work: `HD-40` (signature), `HD-39` (deletion), `HD-38` (free-channel
bytes take their own commit), `HD-36` (must-fix channel takes 扫类 and no-bytes fixes), `HD-30`
(supersession mechanism), `HD-23`, `HD-20`, `HD-5`, `HD-2`. `§live` holds **12** entries at the tip.

**What the work was obliged to do**: answer each must-fix with an amendment plus an independent
re-read of the amended text; apply the same fix at *every other site of the defect the finding
names* (`E10` must-fix channel as widened by `HD-36` ①, and `E7` independently); keep free-channel
bytes in their own commit (`HD-38`); write no `E2`-frozen path (`HD-20`); report after the fact.
`HD-38` and `HD-20` hold — see §2. The 扫类 obligation does not — see §3.

**Ceiling stated once** (`R7`): the round division («正常走吧»), the eight §10 rulings, the `HD-40`
signature and the 路线甲 choice `6208b35` cites all exist only in chat. I verified the repository
records them consistently; never that they were given.

## 2. Boundary checks — frozen surface and instruction layer

```
$ git rev-parse feb7b487:<contract> / b75676e:<contract>
  b2dbdf75 b2dbdf75 SAME   68031fa2 68031fa2 SAME   e1a2f26b e1a2f26b SAME
$ git diff --name-only feb7b487..b75676e8 -- ResearchSystem/schema/document-assurance-v3   -> (empty)
$ git ls-tree -r --name-only b75676e -- ResearchSystem/schema/document-assurance-v3 | wc -l -> 15
$ per-member base-vs-tip blob compare, all nine E10 paths:
  15999875 SAME CONSTRUCTION-CHECKLIST.md   3350bfac SAME REVIEW.md
  54dfef83 SAME README.md                   17ff31bb SAME v3-harness-operating-contract.md
  62c55e4b SAME EXECUTION.md                b576a45e SAME v3-harness-review-contract.md
  68031fa2 SAME supersession-1.md           e1a2f26b SAME supersession-2.md
  09aa8699 SAME paragraph-map.schema.json
```

`E2`'s three blobs unchanged; the pack is fifteen files and none changed; **nine of nine
instruction-layer members unchanged**, so no layer read is owed by this range and `HD-20` is not
engaged. `HD-38` holds at diff level: `6208b35` and `f4c9902` carry only the two `M-1` answers,
`0cc45ce` and `b75676e` only low/observation bytes; the four diffs do not overlap.

`repo-audit` at the tip: **exit 0**, scope 514 markdown files. `ledger_cap_check.py`: **exit 0**;
`HARNESS-LEDGER.md` **114** lines. `HD-24` sits in the archive with `status: superseded` and a
pointer to `HD-39`; `HD-39` points back — `HD-30`'s mechanism is honoured in the register (which
is exactly what makes `M-2` visible).

## 3. `M-1` (must-fix) — both must-fix answers were applied at the reported instance only

`HD-36` ① widened the must-fix channel *specifically* so that the same defect at its remaining
sites travels with the answer; `E7` says the same thing to the executor unconditionally. Neither
answer swept. Three sites survive, spanning both defect classes.

**(a) `split-design.md:221-223` (§10.2) carries the original under-counted connected list,
verbatim.** This is the sentence `M-1` corrected:

> **连带三处**：① `rsc.py:48`/`:50` 两条 import（本就要剪，rider `CLI-hist`）· ② 指向 `stages/` 的
> 4 条链接（其一在待删的 v1 契约 `:23` 内，随之消失）· ③ 已关闭 run `p5b-firewall/…`

Four links where thirteen exist, and no `:850`. **§7 was corrected; §10.2 was not** — and §0:14
reads *冲突时以 §10 与 `HD-39` 为准*, so on the conflict the document's own rule points the reader
at the uncorrected text. `HD-39`'s `basis:` line cites `split-design.md` **§7/§10.2** as its
grounds, so the ruling now rests on one corrected and one uncorrected statement of the same fact.

**(b) `journal/repo-split-r0-2026-08-13.md:9` carries the file-scope coupling claim in its
strongest form, untouched by either amendment**: *`ResearchSystem/tooling/rsc.py` 856 行，**顶层
import 三行是全部耦合面***. `M-1B` corrected `:33-34` twenty-four lines below it and left `:9`
standing. Both amendments' correction blocks say *本段原写「耦合全在顶层三行」* — `:9` is that
sentence, in the same section, in a stronger form (*全部耦合面*).

**(c) The replacement sentences are themselves false at the scope they assert.**
`split-design.md:18-20` and `journal:33-34` now read *`rsc.py` 的耦合**在该块之外**有四处：顶层三行
（`:48`/`:49`/`:50`）**与 `:850`***. Ground truth, whole file:

```
$ grep -nE 'generate\.|pipeline\.|stage_close\.|stage_control\.|GENERATED_DIR' ResearchSystem/tooling/rsc.py
49  57  93  95 104 106 116 126        <- product: GENERATED_DIR / pipeline. / generate.
134 145 146 158 161 164 177 178 193 194 208 209 211 220 223   <- v1 stage group (:134-230)
850                                   <- except stage_control.StageControlFault
$ ... | awk -F: '$1<231 || $1>651' | wc -l   -> 24     (token lines outside the measured block)
$ grep -n 'harness_cli' ResearchSystem/tooling/rsc.py -> 50, 739
$ grep -n '^def ' ...  -> build_parser 652 ; main 842        (block :231-:651 = 421 lines)
```

Outside the block: three imports (`:48`/`:49`/`:50`), seven product-body lines, **fifteen v1
stage-group lines**, `harness_cli.register(sub)` at `:739`, the `stage` subparser block from
`:674`, and `:850`. Under *every* reading of 耦合 the sentence fails — product modules (8 sites
outside the block), modules `HD-39` deletes (17 for `stage_control`/`stage_close`, 19 counting
`harness_cli`), or coupling of any kind (26 lines plus the `:674` subparser block). The
contradiction is internal and local: journal §1's **own table at `:11-18`** enumerates `:739`
`harness_cli.register(sub)` as a coupling site, twenty-five lines above the sentence claiming
four. The previous record printed the full line list in its §3 before the fix was written.

**What goes wrong.** `HD-39` 后果 ① is the connected list R1 executes from and now names three
sites. The fifteen `_cmd_stage_*` body lines are covered only by §1's 提议 prose (*剪完两个组连同
其树一并删除*) and by rider `CLI-hist`, never by the measurement sentence or the ruling. An R1/R2
executor who trusts the sentence — *outside the block the coupling is these four lines* — cuts
`:48`/`:50`/`:850`, deletes `rsclib/stage_control.py` and `stage_close.py`, and leaves fifteen
call-time `NameError`s in `rsc stage …`: the identical failure shape `M-1B` was raised to prevent,
multiplied by fifteen. `from __future__ import annotations` is present (`:36`), so the
`stage_control.StageControlReport` annotation at `:134` does **not** fire at import — the breakage
stays at call time, which is why no import-level check catches it.

**Minimum fix.** (i) Correct §10.2's 连带三处 to the §7 table plus `:850`, or replace it with a
pointer to §7 — while §0's conflict rule stands, the §10 copy is the operative one. (ii) Apply
`M-1B`'s correction at `journal:9`. (iii) Replace *四处* with the measured enumeration and the
class it is scoped to, e.g. *块外：顶层三行 · 产品命令体 7 处（`:57/:93/:95/:104/:106/:116/:126`，
随 `rsc.py` 留调用者仓）· v1 stage 组 15 处（`:134`–`:223`）+ `:674` 子解析器块 + `:739` 注册（随
两组剪除，rider `CLI-hist`）· `:850`（共用错误出口，无归宿）*. Whether `:850` is deleted, re-bound
to a v3 fault, or replaced by a bare `except` remains R1/R2's design call (`R5`).

## 4. `M-2` (must-fix) — the plan R1 executes from still inherits the reversed ruling

`.goals/plans/harness-repo-split.plan.md` is the artifact `HD-5` designates for **原样继承** of
live rulings and the artifact a cold session reads first. `HD-24` was superseded by `HD-39` at
`e7a5ff5` — moved to the archive, `status: superseded`, seven trees reversed from *travel* to
*delete*. The plan was not propagated, and `b75676e`, whose stated job included de-staling it
(*`O-4` plan 陈旧*), corrected the two instances the finding named and stopped.

```
$ grep -rn '整体 travel\|两记录树' --include='*.md' . | grep -v 'v3-checkpoint-read\|v3-review\|DECISIONS-archive'
 .goals/plans/harness-repo-split.plan.md:42   | HD-24 | 七树归属 … 整体 travel；两记录树 … travel …
 .goals/plans/harness-repo-split.plan.md:99   - [ ] 11. 搬 HD-24 的 v2 连通件五件 + 两记录树；…
$ grep -n 'HD-39\|HD-40' .goals/plans/harness-repo-split.plan.md
 :93 (step 8, HD-40)   :150 :154 (Resume pointer, HD-40)      <- HD-39 appears nowhere
```

Two sites, both action-bearing:

- **`:42`** — the 继承的 live 裁决 table still carries `HD-24`'s full text as an inherited live
  ruling. It is not live, and it says the opposite of what is. `HD-39` and `HD-40` have no row.
- **`:99`, R1 step 11** — *搬 `HD-24` 的 v2 连通件五件 + 两记录树*. R1's checklist instructs the
  executor to **move** the five connected files and the two record trees. `HD-39` deletes them.

And what is absent is as load-bearing as what is wrong. R1's steps 10–14 contain **no deletion
step at all** — step 12 covers only `stages/` (2 of 171 files) — and `HD-39` ②'s *3 个文件、13 条
真 markdown 链接 … 全部进 R1 改动边界*, which is the whole product of the `M-1` answer, appears in
neither the steps nor the Acceptance (`:128-137`). The Acceptance's only related line is
*repo-audit exit 0*, which is precisely the line the thirteen links break.

**What goes wrong.** An R1 executor working the checklist moves 139 files into the new repo that
the live ruling says to delete, or halts on the contradiction; either way the round opens against
a plan that disagrees with its own governing decision. `:123` (step 23) compounds it by listing
`HD-24` among decisions to flip to `implemented` — a terminal state under `HD-2`, unreachable.

**Minimum fix.** Replace `:42`'s row with `HD-39` (and add `HD-40`), rewrite step 11 as a deletion
of the 171-file set, add the three link-source files to R1's change boundary, and drop `HD-24` from
step 23. Whether the deletion is one step or several is R1's shape to choose, not this read's
(`R5`). Note the cost this fix does **not** carry: nothing in `split-design.md` changes, so no
re-signature is triggered by it.

**Scope, stated rather than assumed.** These two sentences predate the range; the range is where
they became wrong-and-unswept, on a file it edits, in the commit that declared the plan's staleness
its subject. I report them; whether they belong to this round's answer or to R1's opening is the
orchestrator's call.

## 5. Low

**`L-1` — the *命令照录* block is not a command, and is not the command that produced 335.**
`split-design.md:281` is one physical line. Rendered (blockquote marker stripped), the code block
reads:

```
git log --oneline 0db52a1 -- >   ResearchSystem/document-harness >   …/rsclib/document_harness >   … | wc -l   -> 335
```

The seven operands are separated by literal `>` characters — blockquote markers flattened into the
code line. As text it is a `git log` with an **empty pathspec** followed by seven output
redirections. Both shells on this machine reject it rather than truncating anything, which bounds
the hazard:

```
$ (echo hello -- >   adir >   afile.md)        # bash, scratch dir
  bash: adir: Is a directory        exit=1     afile.md unchanged
PS> cmd /c echo hello -- >   adir >   afile.md
  The output stream for this command is already redirected.   afile.md unchanged
```

The figure itself is right — with the operands properly separated I get exactly the recorded
values, and the `E3` diagnosis behind them is exactly right:

```
$ git log --oneline 0db52a1 -- <the seven paths> | wc -l  -> 335     $ git rev-list --count 0db52a1 -> 720
$ git log --oneline 5aec7f3 -- <the seven paths> | wc -l  -> 337     $ git rev-list --count 5aec7f3 -> 724
```

Downstream decision: the same block instructs *R1 落地时按当时的 base 再算*, and the resume pointer
makes *先声明唯一的 travel 集* R1's first act. R1 copies this line and gets an error, not a number
— which is what `L-2` of the previous read asked to be fixed. **Bytes**: put each operand on its
own line with a trailing `\`, or write them space-separated on one line with no `>`. Deadline:
before R1 re-derives the travel figures.

**`L-2` — the journal still reports the superseded 7, and the plan repeats it.** `journal:60-61`
records *其中首 20 行内点名产品 run … 的 = **7 份***, and `:65` builds the reclassification on *这个
117 / 7 的构成*. `split-design.md:204-206` (§10.1) records that this criterion was too narrow and
the count is **29**; `journal` §3 has no correction block, though this same range wrote inline
correction blocks into §1 (twice), §2 and §7 of that file. `plan:78/:80` repeats the 7. The journal
is the measurement record of record and is cited by `HD-39`'s `basis:`. Harm is bounded — §0's
conflict rule sends a reader of the design document to §10, and R1's step 10 does not quote a
number — so this is a low, not a must-fix. **Bytes**: a correction block under §3 mirroring the
four already in that file, pointing at §10.1. Deadline: before R1 writes the per-file 29/88 list.

**`L-3` — `117` is a base-pinned measurement carried as a standing fact, the exact defect `L-3` of
the source read fixed for 335/720.** `split-design.md:68` (*共 **117 份 = 29 产品 run + 88 构造***)
and `:206`, and `journal:60/:72`, state 117 without the base pin that §10.4 now carries:

```
$ git ls-tree --name-only 0db52a1 -- …/document-work-assurance-v3/ | grep -c '\.md$'  -> 117
$ same at feb7b487 -> 118        $ same at b75676e -> 119
```

It is already 119 at the tip and grows with every record this round produces, while §4's *88 份
travel* and R1's per-file list are derived from it. §10.4 got *R1 落地时按当时的 base 再算*; §3 and
§10.1 did not, in the same commit whose purpose was that repair. **Bytes**: append *（数于 base
`0db52a1`；tip 上已 119，R1 落地时按当时的 base 再算）* at `:68` and `:206`. Deadline: same as `L-2`.

## 6. Observations

**`O-1` — every `E10` construct this round invoked ran over paths `E10` does not govern.** Zero of
the nine members and zero `E2` bytes changed in all five commits (§2), so the must-fix amendment,
its independent re-read, and the free channel were all exercised on a design document, a decision
register (`HD-19`: explicitly not a member), a journal and a plan. `R10`'s routing sentence supports
this — it routes *findings*, and says neither their tier nor their producer changes the route — and
`E10`'s free-channel clause says *instruction layer included*, which reads as general-with-emphasis
rather than layer-only. So this is reported, not concluded (`R5`). It matters only for one thing,
and that one thing is independently settled: `E9`'s budget. Its test — *has a valid independent
FULL already occurred?* — answers **no** for R0, so nothing here could consume the cap however the
commits are classified. Stated so that a later reading does not have to reconstruct it.

**`O-2` — `R6`'s record title form was dropped.** `R6` fixes the title as
`V3-REVIEW-RECORD-<ROUND>-<sha>-v1`, and **83** commits in this branch's history carry it,
batch B's five read records included (`V3-REVIEW-RECORD-B-R5-READ-136f27f-v1`,
`…-REREAD-f61ce2c-v1`). This round writes `V3-SPLIT-R0-READ-RECORD-ffbc393-v1` and
`V3-SPLIT-R0-REREAD-RECORD-0cc45ce-v1`:
`git log --format=%s feb7b487..b75676e8 | grep -c '^V3-REVIEW-RECORD'` → **0**. The cost is that
review records stop being reachable by one prefix grep, which is how the ledger's *不可变、可 grep*
claim is cashed. Trivial to fix at the next record; unfixable for these two.

**`O-3` — `E8` kind naming, two of five.** All five titles now match `V3-…-v1` and name the round,
and all five bodies carry **0** trailers. Kind: `6a946ba` says *record*, `f4c9902` and `6208b35`
say *amendment* — inside `E8`'s vocabulary. `0cc45ce` names none, and `b75676e` opens with
*自由通道*, which is the channel, not one of candidate / pre-submission correction / review fix /
closeout / errata / amendment / ruling / record. Body lengths, non-blank: **19 / 22 / 18 / 11 /
17** against the batch-B §8 ten-line discipline. `b75676e`'s own body records both deviations
(*正文长度仍未收进十行，照记不辩*), so this is measurement, not news.

**`O-4` — `6a946ba`'s body says `+335`; the record is 334 lines.** `wc -l` → 334, and the commit's
own `--numstat` → `334 0`. A number in a commit body contradicted by the same commit's stat.

**`O-5` — the restored method still elides its operand.** `journal:23` now reads
`sed -n '231,651p' rsc.py | grep -cE '…'` → 0. `O-3` of the previous read asked for the command
that produced the count; what came back has the command's *shape* but a placeholder where the
pattern goes — the same defect as `L-1` above, one class, two instances, both written in this
range. Recoverable here (the five tokens are named in the sentence immediately above), which is why
this is an observation and `L-1` is not.

**`O-6` — the signed document has moved four times and no gate has closed behind it.**

```
$ git log --oneline 9736670..b75676e -- ResearchSystem/document-harness/split-design.md   -> 4 commits
  blob 3f4d2b0a (251 lines, signed)  ->  3d5eed90 (267)  ->  74d70ca7 (280)  ->  067b6c69 (290)  ->  46b67776 (300)
```

`HD-40:39` says *自 `6208b35` 起被改过三次* — four, and it is short by exactly the commit that wrote
it, which is `E12`'s written-tip failure applied to a count. Wording-level under `R9`: it changes no
action (the entry already says the binding is stale and re-signature is imminent) and the accurate
value is recoverable from `git log`, so it rides the next batch. The larger shape, restated rather
than concluded (`R5`) because the previous two records already put it to the user: `HD-40`'s
signature landed *before* all five of these commits, and the four rewrites since have been reviewed
only by a channel that cannot return `CHANGES_REQUIRED`. `M-1` and `M-2` are both findings a
signature gate would have had to answer.

**`O-7` — the two `M-1` answers are, on their own terms, correct and well made.** `f4c9902`'s
analysis of `:850` is exact: it is in `main()` (`:842`), wraps `args.func(args)` (`:849`), the eight
in-block handlers catch `SpecGap`/`AssuranceFault` only, and every `FATAL:` string the CLI tests
assert on comes from inside the block (`:523`, `:609`) — no test asserts on `:850`'s output. The
`E3` root-cause diagnoses in both answers (*断言写文件尺度，命令只跑块内*; *grep 的是字节读者，写下的
却是引用面*) name the defect precisely. What failed was not the diagnosis but its radius: each was
applied where the finding pointed. Recorded because `M-1` above should not be read as doubting the
work, only its reach.

## 7. What reproduced exactly

Recorded so these are not re-measured. Each was re-derived here, not read off any document or
prior record.

| claim (subject bytes) | recorded | re-derived |
|---|---|---|
| commits touching the seven-path travel set, base `0db52a1` | 335 | **335** |
| repo commits at base | 720 | **720** |
| same seven paths at `5aec7f3` | 337 | **337**; repo **724** — the `E3` story reproduces |
| the eleven-path set is a different population | 247 mid-round, 245 at base | **247** @`5aec7f3`, **245** @`0db52a1` (files); seven-path set 253 / 251 |
| deletion union | 171 | **171** tracked files (`git ls-files … \| sort -u`) |
| the 139 bucket | 139 | **139**; per-tree 14 · 11 · 1 · 81 · 26 · 2 · 2 · 2 + 2 contracts |
| net addition after removing the double-counted contract | 32 | **32** (extra-only = 32; 171 − 139 = 32) |
| links from outside the deletion set into it | 3 files, 13 links | **3 / 13**, every line number exact (README `:35/:39/:41/:42/:43/:44/:45/:46`; v2 plan `:723-725`; refactor plan `:323/:324`) |
| `repo-audit` link machinery | `cand.exists()` `:103-115`, exit 1 `:304`, `EXCLUDE` ten items | **exact**; `ROOT` `:31`, `rglob` `:62`; audit **exit 0** at tip |
| `HD-40` blob-content sha256 | `8da2d17d…59af` | **`8da2d17d7adac639…9ac59af`** (19004 bytes, 251 lines) |
| `HD-40` working-copy sha256 | `c4e24f99…ab5c` | **`c4e24f99334a4441…382bab5c`** = blob + one CR per line |
| *仓内 blob 一律 LF，`E2` 三份亦然* | true | **true** — `git ls-files --eol`: 1482 `i/lf`, 316 `i/none`, 115 `i/-text`, **zero** `i/crlf`/`i/mixed`; the three `E2` blobs carry 0 CR |
| why `HD-35` did not expose it | io-design's **working copy** is LF | **0 CR on disk**; blob sha256 `730fddf4…8157` == worktree sha256 == the digest `HD-35` records |
| the CRLF-on-disk files | split-design / decisions / journal | **300 / 406 / 103** CR in the worktree, LF blobs |
| `_cmd_v3_*` count and offsets | seven: 231 · 275 · 296 · 333 · 445 · 491 · 589 | **exact, all seven**; `build_parser` `:652`, `main` `:842` |
| v3 block | `:231`→`build_parser`, 421 lines, coupling 0 | **421**; **0** for all five tokens |
| in-block handlers | 8 | **8**, all `SpecGap` / `AssuranceFault` |
| `rsc.py:850` | `except stage_control.StageControlFault` in `main()` wrapping `args.func(args)` | **exact** (`:849` call, `:850` handler, `:851` `FATAL:`/`return 2`) |
| `EXCLUDE` | ten items | **10**, same members |
| `HD-24` supersession | archived, `superseded`, pointers both ways | **exact**; archive 130 lines; `§live` **12** at tip |
| ledger | ≤ 120 | **114**; `ledger_cap_check.py` exit 0 |
| `HD-38` separation | free-channel bytes in their own commits | **holds** — the four diffs do not overlap |
| `E2` / instruction layer across the range | untouched | **3 blobs SAME, pack 15 / 0 changed, 9 of 9 members SAME** |
| review records in the directory | 117 | **117** @`0db52a1` — but 119 at tip, see `L-3` |

## 8. Coverage and ceilings (`R4`)

**Read in full**: the four non-record files at the tip (`split-design.md`, the journal,
`HARNESS-DECISIONS.md`, the plan); `v3-checkpoint-read-0cc45ce.md`, the record committed inside
this range; `CONSTRUCTION-CHECKLIST.md`; `v3-checkpoint-read-ffbc393.md`; `HARNESS-LEDGER.md`;
`HARNESS-RIDERS.md`; all five commit messages; the whole range diff.

**Sampled**: `rsc.py` — every line matching the five coupling tokens, the import head, `main()`,
`build_parser`'s registrations, the eight in-block handlers and the `FATAL:` emitters; not the
whole 856. `Thesis/Work/Tooling/repo-audit.py` — `:25-70`, `:95-125`, `:295-310`.
`HARNESS-DECISIONS-archive.md` — the `HD-24` entry and the header. The four subprocess test
drivers of `rsc.py` — their `returncode` and `FATAL` assertions only.

**Probed only** (command/script output, no reading): the 171-file deletion set and its per-tree
breakdown; the link scan (a script replicating `repo-audit`'s `MD` regex, fence and inline-code
stripping, and `cand.exists()` resolution); the commit counts; `git ls-files --eol` over 1913
tracked files; the record counts.

**Not read**: `EXECUTION.md`, `README.md`, the two retired-contract stubs and
`paragraph-map.schema.json` — all four verified byte-unchanged and nothing in this subject depends
on their content; `io-design.md` beyond the digest checks; the caller-side product tree; the
regression battery (not run).

**`UNVERIFIABLE`, not folded into supported** (`R4`):

- **That no test reaches `rsc.py:850`.** I read the four subprocess drivers and confirmed every
  asserted `FATAL:` string is emitted inside the v3 block, and that the v1 `_cmd_stage_*` bodies
  carry no handler of their own — so `:850` is the live handler for v1 faults and the one CLI test
  that drives `rsc stage` (`tests/stage_control/run_tests.py:177-205`) asserts `returncode 0`, a
  success path. I did not execute the battery. An escaping-exception driver elsewhere would falsify
  this.
- **The travel-set membership behind `247` and `335`.** Both figures reproduce, each under a
  different path set, and neither set is declared anywhere in the repository; §10.4 now prints the
  seven-path operands, and the eleven-path set remains my reconstruction from the figure. `HD-28`'s
  membership ruling matches neither, as the subject itself now records.
- **Process claims marked, not verified**: that this session held only the review role for its
  whole life (`E1`); that the round division, the eight rulings, the signature and the 路线甲 choice
  were given as the repository records them (`R7`).

**Independence** (`R1`): this session was dispatched, scoped and is reported through the
orchestrator; the executor set none of the four. No prior record for this subject existed in the
worktree at open (`git status --porcelain` empty, canonical path absent), so unlike the previous
read there is no collision disclosure to make. `M-1`(c), `M-2` and `L-3` are findings neither prior
record raised; `M-1`(a) and `M-1`(b) are sweeps of defects those records named, re-derived here from
the repository.
