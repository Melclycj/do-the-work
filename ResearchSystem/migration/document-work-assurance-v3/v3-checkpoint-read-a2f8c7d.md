# Split-batch R0 — re-read of the `M-1C`/`M-2` amendment, the free-channel application, and the two method self-audits `4342c6be0516c8a140685927503a5ee7bcc78c47..a2f8c7da9c9f17a980b5578f4f8b760c9e191137`

Independent read of the four commits that answer the third R0 read (`4342c6b`,
`v3-checkpoint-read-b75676e.md`) and carry the newly approved 量程纪律 into the design
document and its journal. **Not a round** (`R3`): no verdict, no budget consumed. Output is
findings tiered must-fix / low / observation.

**Findings: 1 must-fix, 5 low, 7 observations.**

The `M-1` answer is complete and correct at all three sites, and every figure the two
self-audit commits re-derived is right where I could reproduce its command: the 24 out-of-block
token lines, the 15 v1 stage-group lines, the seven product-body offsets, the four/six pre-commit
hook split, the four tracked hook files, the five `pack_digests` hits and their v2 attribution,
245 @ base and 250 @ tip, 335/720, the 171/139/32 arithmetic, 29/88 under the stated criterion,
117 @ base. The `L-1` command block now executes verbatim and returns 335.

`M-1` below is the third consecutive instance of one shape: **the answer landed at the sites the
finding enumerated and nowhere else.** `M-2` named four sites in the plan; all four are fixed. The
same file still tells its reader, in four other places, that Q3 is undecided, that seven forks
await the user before signature, that two reads have run and the next one takes `feb7b48` as base,
and that the design document has been revised three times. Two of those contradict `HD-40` — the
live ruling the same commit added to the plan's own inheritance table.

## 1. Subject, re-derived (`R2`)

Handed one range and nothing else. Round, budget, authorization, obligations and every figure
below are re-derived here; nothing is taken from the dispatch prompt, a commit body, the plan,
the ledger, the design document or any prior record.

```
$ git rev-parse HEAD               -> a2f8c7da9c9f17a980b5578f4f8b760c9e191137   (== range tip)
$ git rev-parse --abbrev-ref HEAD  -> document-work-assurance-v3
$ git status --porcelain           -> (empty)
$ git rev-list --count 4342c6be..a2f8c7da -> 4
$ cat .harness/review-pending.json
  {"subject": "4342c6be0516c8a140685927503a5ee7bcc78c47..a2f8c7da9c9f17a980b5578f4f8b760c9e191137",
   "dispatched_at": "2026-08-14T07:58:08+00:00"}
$ git log -1 --format=%cI a2f8c7d   -> 2026-08-14T17:58:06+10:00  (= 07:58:06Z)
$ git log --format='%H %P' 4342c6b..a2f8c7d  -> linear, four commits, no merge, no reparent
```

HEAD equals the tip and the tree is clean, so worktree reads are reads of subject bytes. The
freeze marker's subject is byte-equal to the dispatched range and post-dates the tip by two
seconds. `.harness/` is gitignored (`git check-ignore -v` → `.gitignore:19`), so marker writes and
deletions are filesystem actions, never diff content.

**Four commits, classified by hand** (`R2`):

| # | sha | title | kind, as read from the diff |
|---|---|---|---|
| 1 | `e788169` | `V3-SPLIT-R0-AMEND-M1C-M2-v1` | amendment — answers `b75676e`'s `M-1`(a)(b)(c) and `M-2` |
| 2 | `f97bb17` | `V3-SPLIT-R0-FREE-L1-L2-L3-O5-O6-v1` | free-channel byte application |
| 3 | `12a28ce` | `V3-SPLIT-R0-METHOD-SELFAUDIT-v1` | errata — new 量程纪律 + three self-caught corrections |
| 4 | `a2f8c7d` | `V3-SPLIT-R0-METHOD-SELFAUDIT-JOURNAL-v1` | errata — same discipline applied to the journal |

**Four paths changed**, classified by hand:

```
$ git diff --numstat 4342c6be..a2f8c7da
10   5   .goals/plans/harness-repo-split.plan.md                                 plan (resume artifact)
 3   1   ResearchSystem/HARNESS-DECISIONS.md                                     decision register — NOT an E10 member (HD-19)
50  20   ResearchSystem/document-harness/journal/repo-split-r0-2026-08-13.md     round record (measurement)
61  15   ResearchSystem/document-harness/split-design.md                         design product, user-signed at 3f4d2b0a (HD-40)
```

**Round, budget, obligations — derived.** The round is 拆分批 **R0**, plan
`.goals/plans/harness-repo-split.plan.md`, `status: R0 OPEN 2026-08-13`, `base_commit 0db52a1`
(base written, tip unwritten — `E12` satisfied). Plan Notes: *`E9` 预算一轮一算：R0 用 `E10` 独立
read（无 FULL 预算）*. `E9`'s own test settles it independently of what anything is called: **no
valid independent FULL has occurred for R0**, so every commit in this range is a pre-submission
correction and consumes nothing; the fix leg and the VERIFY are unspent. Live rulings visible in
the repository that bind this work: `HD-40` (signature, and *R1 按 §3/§4/§7 施工*), `HD-39`
(deletion), `HD-38` (free-channel bytes take their own commit), `HD-36` (must-fix channel takes
扫类 and no-bytes fixes), `HD-30`, `HD-23`, `HD-20`, `HD-5`, `HD-4`, `HD-2`. `§live` holds **12**
entries at the tip.

**What the work was obliged to do**: answer each must-fix with an amendment plus an independent
re-read, applying the same fix at *every other site of the defect the finding names* (`E10`
must-fix channel as widened by `HD-36` ①, and `E7` independently); keep free-channel bytes in
their own commit (`HD-38`); write no `E2`-frozen path (`HD-20`); re-run every figure immediately
before the claim (`E3`); name the commit's kind (`E8`). `HD-38`, `HD-20`, `E8` and the `M-1` half
of the 扫类 obligation all hold — see §2 and §6. The `M-2` half does not — see §3.

**Ceiling stated once** (`R7`): the round division, the eight §10 rulings, the `HD-40` signature,
and the 2026-08-14 approval of the 量程纪律 («用户批准改写法») all exist only in chat. I verified
that the repository records them consistently; never that they were given.

## 2. Boundary checks — frozen surface and instruction layer

```
$ per-path base-vs-tip blob compare:
  b2dbdf75 SAME Document-Work-Assurance-Contract-v3.md      (E2 blob 1)
  68031fa2 SAME …-supersession-1.md                          (E2 blob 2, E10 member)
  e1a2f26b SAME …-supersession-2.md                          (E2 blob 3, E10 member)
  15999875 SAME CONSTRUCTION-CHECKLIST.md    3350bfac SAME REVIEW.md
  54dfef83 SAME README.md                    17ff31bb SAME v3-harness-operating-contract.md
  62c55e4b SAME EXECUTION.md                 b576a45e SAME v3-harness-review-contract.md
  09aa8699 SAME paragraph-map.schema.json
$ git diff --name-only 4342c6be..a2f8c7da -- ResearchSystem/schema/document-assurance-v3  -> (empty)
$ git ls-tree -r --name-only a2f8c7d -- ResearchSystem/schema/document-assurance-v3 | wc -l -> 15
```

`E2`'s three blobs unchanged; the pack is fifteen files and none changed; **nine of nine
instruction-layer members unchanged**, so no layer read is owed by this range and `HD-20` is not
engaged. `HD-38` holds at diff level: `e788169` carries only the `M-1`/`M-2` answers, `f97bb17`
only low/observation bytes; the two diffs do not overlap. `12a28ce` and `a2f8c7d` are neither —
they are new work under a user-approved method change, so `HD-38` does not reach them.

`repo-audit` at the tip: **exit 0**. `ledger_cap_check.py`: **exit 0**; `HARNESS-LEDGER.md`
**114** lines. `HARNESS-RIDERS.md` **38** lines (28 rows) — unchanged by this range; nothing was
banked and, apart from `L-5` below, nothing owed the bank.

## 3. `M-1` (must-fix) — `M-2`'s answer was applied at the four sites the finding enumerated, and the plan still contradicts `HD-40` in four others

`M-2`'s minimum fix listed four sites: the `:42` inheritance row, step 11, the change boundary for
the thirteen links, and `HD-24`'s removal from step 23. **All four are correct**: the row now
carries `HD-39` + `HD-40`, step 11 is a deletion of the 171-file set with `rsc.py:48`/`:50`/`:674`/
`:739`/`:850` named, step 12 covers the three link sources, the Acceptance carries *13 条入链全部
处置完毕*, and step 23 drops `HD-24` with the `HD-2` reason stated. `HD-39`'s three 后果 items map
onto steps 11/12 and the row.

And nothing else in the file moved. `HD-36` ① widened the must-fix channel *specifically* so the
same defect at its remaining sites travels with the answer; `E7` says the same unconditionally;
§11 rule 4, written into `split-design.md` two commits later, restates it in the executor's own
words (*改完点名那处，立刻在同一 commit 里 grep 同一断言的其余写法*). Four sites survive.

**(a) `plan:77-82`, step 3 — «最终状态：待裁 … 设计稿 §3 出甲/乙两案».** `split-design.md` §3's
heading is *两次改判后已裁：乙*, §10 row 3 records 已裁, and `HD-40` makes §3 R1's construction
basis. The plan's own `:43` row now says *`HD-40` … R1 按 §3/§4/§7 施工*. Same file, thirty-five
lines apart: one says §3 is decided and binding, the other says it is 待裁 with two options open.

**(b) `plan:150-151`, 待用户裁 item 3 — «R0 设计稿 §9 的 7 个岔口 … 签字前须全答».**
`split-design.md:191` reads *§9 待用户拍板清单 —— **全部已答（2026-08-13/14）***, and `HD-40`
records the signature. The plan lists as pending-user-ruling exactly what `HD-40` records as ruled
and signed. `plan:94` (step 8) carries the same stale «§9 列 7 个待拍板岔口» while its own sentence
says 已签.

**(c) `plan:155-161`, the Resume pointer — one whole read cycle stale, with an actionable base.**

> 已跑**两次**独立 read（记录 `feb7b48`、`6a946ba`），各返 1 must-fix … **仍欠**：一次覆盖**全部**
> amendment 字节的 re-read … 故**下一次以 `feb7b48` 为 base**。

Three reads have run. The third is `4342c6b`, `v3-checkpoint-read-b75676e.md`, covering
`feb7b48..b75676e`, returning **2 must-fix, 3 low, 7 observations** — the record this entire range
answers. `split-design.md:324` knows this (*R0 的三轮独立 read 共返四条 must-fix*, and 1+1+2 = 4
reproduces from the three records' own summary lines). A cold session working the Resume pointer
dispatches a fourth read at base `feb7b48` — a range that **excludes every commit in this range**,
i.e. excludes the answers it would be reading for.

**(d) `plan:159` — «稿已三改».** Measured:

```
$ git log --oneline 9736670..HEAD -- ResearchSystem/document-harness/split-design.md | wc -l -> 7
  3f4d2b0a(251, signed) -> 3d5eed90(267) -> 74d70ca7(280) -> 067b6c69(290)
                        -> 46b67776(300) -> 2dad0da6(310) -> 9ae5def1(315) -> 3287ab49(346)
```

Seven. `f97bb17` corrected exactly this count in `HD-40` (三次 → 四次以上) and did not sweep the
sibling in the plan — the `O-6` defect at its second site, in the commit whose subject was `O-6`.

**What goes wrong.** (a) and (b) are the `M-2` shape verbatim: the plan states, as the current
state of a question, the opposite of what a live ruling says. An R1 executor or a cold orchestrator
reading step 3 sees Q3 open and §3 offering two schemes, while `HD-40` binds R1 to build from §3's
乙; reading item 3 it sees a signature gate still ahead of it. (c) costs a redundant dispatch on a
base that would exclude the answers, and it is the artifact `HD-5` designates for 原样继承 and the
one a cold session reads first — the exact argument that made `M-2` a must-fix.

**Minimum fix.** Rewrite step 3's verdict clause to 已裁乙 with the `HD-40` pointer (the two-改判
history is worth keeping; only *最终状态：待裁* and *出甲/乙两案* are false). Strike item 3 from
待用户裁 or strike it through as items 1–2 already are, leaving `HD-40`'s two genuinely open items
(remote, the 32-file confirmation). Rewrite the Resume pointer to: three reads
(`feb7b48`/`6a946ba`/`4342c6b`), the third returning 2 must-fix + 3 low + 7 observations, answered
by `e788169` + `f97bb17`, plus the two self-audit commits; next = the re-read of *this* range, base
`4342c6b`. Change 稿已三改 to 七改 or drop the count and keep the pointer to `HD-40`. Whether step
3's history text is trimmed further is the executor's call (`R5`).

## 4. Low

**`L-1` — §11's own discipline is broken by three assertions written inside this range.** Rule 1
is *先写量程 … 再跑覆盖该量程的命令；两者对不上时不得写成断言*; rule 2 is *绝对量词必须带量程*.
All three sites below declare a scope-command and then assert something the command does not
produce. Recoverable in each case from adjacent text, which is why these are low, not must-fix.

**(a) `split-design.md:24-28` and `journal:43-47` — the *完整枚举* is 28 sites; the command cited
for it returns 24 and contains four of them nowhere.** Both files carry the identical sentence,
which is the `M-1`(c) answer:

> **块外耦合的完整枚举（`grep -nE 'generate\.|pipeline\.|stage_close\.|stage_control\.|GENERATED_DIR' rsc.py` 排除 `:231`–`:651` 后 24 行）**：顶层三行 `:48`/`:49`/`:50` · 产品命令体 7 处 … · v1 `stage` 组 15 处 … 另加 `:674` 子解析器块与 `:739` … · **`:850`**

```
$ grep -nE 'generate\.|pipeline\.|stage_close\.|stage_control\.|GENERATED_DIR' rsc.py | awk -F: '{print $1}'
  49 57 93 95 104 106 116 126 134 145 146 158 161 164 177 178 193 194 208 209 211 220 223 850   (24, all outside the block)
$ sed -n '48p;50p' rsc.py
  from rsclib import generate, pipeline, stage_close, stage_control     <- `generate,` not `generate.`
  from rsclib.harness import cli as harness_cli                          <- no token at all
$ sed -n '674p;739p' rsc.py -> `stage = sub.add_parser(` / `harness_cli.register(sub)`   <- no token
```

The enumeration is 3 + 7 + 15 + `:674` + `:739` + `:850` = **28**; the grep's out-of-block output is
**24** = `:49` + 7 + 15 + `:850`. `:48`, `:50`, `:674` and `:739` are in the list because the
previous record put them there, not because that command found them — and they are precisely the
four lines R1 must cut. A reader who verifies the sentence by running the command it names gets a
24-line list missing all four. **Bytes**: split the parenthetical — *（该 grep 排除 `:231`–`:651`
后 24 行，另加 grep 不匹配的 `:48`/`:50` 两条 import 与 `:674`/`:739` 两处注册，共 28 处）*.
Deadline: before R1 re-derives the cut list, and before the re-signature that `HD-40` says is
imminent.

**(b) `journal:21` — «`grep -n 'sub.add_parser(' rsc.py` 得四处» returns 14.**

```
$ grep -c 'sub.add_parser(' rsc.py    -> 14      $ grep -c '= sub.add_parser(' rsc.py -> 4
```

`stage_sub.add_parser(` (`:681`/`:705`/`:717`/`:728`) and `v3_sub.add_parser(` (`:753`/`:769`/
`:776`/`:783`/`:802`/`:811`) contain the quoted substring. The claim the annotation supports —
五个顶层命令组, four via `sub.add_parser` and `harness` via `:739` — is **correct** and its line
numbers (`:656`/`:664`/`:674`/`:746`/`:739`) all check out; only the reproducer is wrong. This is
the same defect the annotation was written to eliminate, in the annotation. **Bytes**: `grep -n '=
sub.add_parser(' rsc.py` 得四处. Deadline: same as (a).

**(c) `journal:107-109` — «其余命中只有本轮自己写的两份文档» at declared scope 全仓 tracked.**

```
$ git grep -nE 'interface_version|harness_version|tool_version' -- . | wc -l -> 8
  journal ×2 · split-design ×1 · schema/harness-v2/observation.schema.json ×2
  · schema/harness-v2/fixtures/{negative/NEG-observation-mutates-run,negative/NEG-observation-workaround-without-proof,positive/observation}.json ×3
```

The primary assertion — zero hits under `tooling` and `schema/document-assurance-v3` — is **true**.
The bracketed 量程 note names one v2 file and then says *其余命中只有* this round's two documents;
three further v2-fixture hits exist. An absolute quantifier whose enumeration does not cover its
declared scope (rule 2). **Bytes**: *除 v2 的 `observation.schema.json` 与 `harness-v2/fixtures/`
三份 fixture 外*. Deadline: same as (a).

**`L-2` — `split-design.md:79` says the tip holds 119 records; it holds 120, and the journal says
120.**

```
$ git ls-tree --name-only <rev> -- …/document-work-assurance-v3/ | grep -c '\.md$'
  0db52a1 -> 117    b75676e -> 119    4342c6b -> 120    f97bb17 -> 120    a2f8c7d -> 120
```

119 was true at `b75676e`, which is where the source record measured it — one revision before this
range's base. `f97bb17` carried it across instead of re-running (`E3`: *re-run immediately before
the claim*), so the correction written to fix a base-pinning defect introduced a stale figure of
its own. `journal:77`, written two commits later, has **120**: the two files of the same range now
disagree about the same quantity. Harm is bounded — both sentences carry *R1 落地时按当时的 base
再算* — so this is low. **Bytes**: 119 → 120 at `:79`. Deadline: before R1 writes the per-file
29/88 list.

**`L-3` — the design document's title and status line still say it is unsigned, in the same
sentence that says it does not carry its approval status.** `split-design.md:1` reads *（R0 产物,
**欠用户签字**）* and `:3` reads *状态：**定稿待签***, three lines above the 量程纪律 block this
range inserted. `:3-4` also reads *本文件按 governance-scan 判据**不携带自身审批状态***. `HD-40`
records the signature of 2026-08-14. So the document simultaneously declares that it carries no
approval status and carries a false one; its true state is 已签、欠重签. This is the same shape as
the `paragraph-map.schema.json` self-statement that cost an `E2` unfreeze. **Bytes**: title →
*（R0 产物，已签 `HD-40`，实质修改后欠重签）*; `:3` → *状态：**已签（`HD-40`，绑定陈旧、欠重签）***
— or, if the no-self-status rule is meant literally, delete both clauses and leave the pointer to
`HARNESS-DECISIONS.md`. Which of the two is the executor's call (`R5`). Deadline: the re-signature.

**`L-4` — `split-design.md:100` calls 245 the new repository's first commit, and its own §10.4 says
that set is not the membership.** `:100` now reads *新仓第一个 commit 即 **245**（@base；量程见
§10.4）个文件*. §10.4 row 1 states the 245 is the seven-prefix set and that *按乙案还须从
`migration/document-work-assurance-v3/` 排除 29 份产品记录*, and the §10.4 correction block adds
*两个集合都不等于 `HD-28` 的成员裁决*. Under the ruled 乙 the figure drops by 29, and `HD-28`'s B
tier (three governance registers) is not in the seven prefixes at all. The self-audit changed
247 → 245 and pinned the base without asking whether the number means what the sentence says.
**Bytes**: *新仓第一个 commit 的量级约 **245**（七前缀集 @base `0db52a1`；**不等于新仓成员**——按
乙案减 29 份产品记录、按 `HD-28` 加 B 治理登记 3 件，见 §10.4）*. Deadline: R1's first act, which
§10.4 already defines as 先声明唯一的 travel 集.

**`L-5` — the 量程纪律 binds future design rounds and has no entry in the decision register.**
`split-design.md:329` scopes it *本文件与其 journal 适用，**今后设计轮同***, and the journal header
carries it too. `HD-4`'s admission test is *绑下一轮及以后？* — any one yes admits — and `HD-1`
makes `HARNESS-DECISIONS.md` the highest source of truth for user rulings, with instruction detail
based on it rather than the reverse. `§live` holds 12 entries at the tip and none of them is this
one:

```
$ awk '/^## §live/,/^## §implemented/' HARNESS-DECISIONS.md | grep -c '^### HD-'  -> 12
  HD-40 39 36 35 28 33 34 27 23 10 15 9   (no 写法修正 entry)
```

**What goes wrong.** `HD-5` makes `§live` the cold-read obligation and states that
`§implemented` and the archive are not in it — nothing routes a future design round to
`split-design.md` §11. So a rule the user approved for 今后设计轮 is reachable only from a document
about a different subject, and the next design round (契约 v4, the packaging batch) will not see
it. **No bytes**: creating or refusing an entry is the user's act under `HD-2`/`HD-4`, and the
alternative — narrowing §11's scope to this document — is equally the user's. Banks or is answered
by a ruling.

## 5. Observations

**`O-1` — `journal:76`'s 63/64 is the one figure in the range I could not reproduce, and its
annotation declares a scope without declaring a criterion.** The sentence is *全文提到产品 run 的
= **63 份*** with 〔量程 = 该目录顶层 `*.md` @ base `0db52a1`〕 and *tip 上已 … 64 份*. Every sibling
annotation the same commit added carries its command (`grep -c 'python '`, `git ls-files`,
`grep -rn pack_digests`); this one does not, and the run-name list in the adjacent clause does not
yield it:

```
p3-corr|p4-|p5a-|p5b-|w1-r1                     -> 69 @base, 70 @tip
p3-corr|p4-bridge|p4-doc|p5a-|p5b-|w1-r1        -> 64
p3-corr|p4-|p5a-|p5b-|w1-r1|assurance/runs/     -> 78
p3-corr|p5a-|p5b-|w1-r1                         -> 57
```

`UNVERIFIABLE` (`R4`), not folded into supported. It is an observation rather than a low because
the 63 is decorative — §10.1's 29/88 replaced it as the operative split and reproduces exactly, and
the journal's own correction block says so. The gap is that rule 1 asks for the command and this
annotation gives only the scope.

**`O-2` — the freeze marker was withdrawn without a return record, and two commits landed after
the dispatch it belonged to.** `12a28ce`'s body records this in full and calls it a deviation, not
an exemption: the previous session dispatched `4342c6b..f97bb17`, the user redirected to the method
change, and the marker was deleted with no record commit. `E9`'s clause is *a dispatched FULL,
VERIFY or read has occurred only when its record's commit lands; from dispatch to that commit the
branch takes no commit but the record itself* — it attaches at dispatch, and carries no carve-out
for a dispatch that reached no session. The executor's reading (the window protects an in-flight
reviewer's subject tree) is a sound purpose argument but is not in the text. **The cost is
genuinely nil and I can state it rather than assume it**: the abandoned range `4342c6b..f97bb17` is
a strict prefix of this one, so its bytes have now been read. Recorded so that the second instance,
if there is one, is not the first time anyone counts.

**`O-3` — the signed document has grown 38% since signature and now contains a section that did not
exist when it was signed.** blob `3f4d2b0a` (251 lines) → `3287ab49` (**346**), seven revisions,
+95 lines net; §11 (25 lines) and the 3-line header discipline block are entirely post-signature,
as is every correction block cited above. `HD-40` says the binding is stale and re-signature is
imminent, and both the ledger and the plan carry that. Restated rather than concluded (`R5`)
because the previous two records already put the shape to the user: **four independent reads, four
answered defect classes, and no gate that can return `CHANGES_REQUIRED` has closed behind any of
them.** `M-1`, `L-1`, `L-3` and `L-4` are all findings a signature gate would have had to answer.
Whether the document should be re-signed before or after this record's findings are applied is the
user's call, not this read's.

**`O-4` — `E8` kind naming now conforms on all four commits; body length still does not.** All four
titles match `V3-…-v1` and name the round; **0** trailer-shaped lines in all four bodies. Kinds:
*amendment* (`e788169`), *自由通道（errata 类）* (`f97bb17`), *自查（errata 类）* (`12a28ce`,
`a2f8c7d`) — `errata` and `amendment` are both inside `E8`'s vocabulary, which closes the previous
record's `O-3`. Non-blank body lines: **18 / 14 / 23 / 20** against the batch-B §8 ten-line
discipline. Measurement, not news. `R6`'s title form has nothing to check here — this range
commits no record.

**`O-5` — every `E10` construct this round invokes still runs over paths `E10` does not govern.**
Zero of the nine members and zero `E2` bytes changed in all four commits (§2), so the must-fix
amendment and the free channel were again exercised on a design document, a decision register
(`HD-19`: explicitly not a member), a journal and a plan. The previous record raised this as its
`O-1` and it is unchanged; repeated only because it still matters for exactly one thing, which is
still independently settled: `E9`'s test — *has a valid independent FULL already occurred?* —
answers **no** for R0, so nothing here consumes the cap however the commits are classified.

**`O-6` — `split-design.md:266`'s «`.claude/commands/` 11 项» sits under a 量程 of 全仓 tracked,
where the number is 18.** `git ls-files .claude/commands` → **18** (11 top-level `.md` plus 7 under
`agent-analysis-profiles/`). Reading 项 as *commands* makes 11 exactly right and the profiles not
commands; reading it under the cell's own 〔量程 = 全仓 tracked，`git ls-files .claude`〕 makes it 18.
The two other figures in that cell (**166** skill files / **3** skills; plugin manifests **0**)
reproduce exactly, and the conclusion — no installable artifact belongs to the harness — is
unaffected either way. Reported rather than filed as a low because the ambiguity is in the unit,
not in the measurement.

**`O-7` — what the range got right, recorded so `M-1` is not read as doubting the work.** The
`M-1` answer is complete at all three sites: §10.2 no longer carries the under-counted list and now
points at §7 (whose table and the `HD-39` 连带清单 agree item for item); `journal:12` no longer
claims the three imports are the whole coupling surface; the replacement enumeration is, as a list
of sites, exactly right — 15 v1 lines within `:134`–`:223`, 7 product-body offsets, `:850` in
`main()`, all verified line by line. `L-1`'s command block now executes verbatim from `:297` and
returns **335**; `L-3`'s base pins landed at §10.4 and §3; `O-5`'s grep pattern is written out in
full; `O-6`'s count was corrected in `HD-40` with a live reproducer attached. The two self-audit
commits caught three real defects nobody had reported (§10.3's packaging claim, §5's narrow scope,
§10.4's mid-round 247) and two more in the journal (the command-group count, the pre-commit hook's script count),
and every one of those corrections is right. What failed, for the third time, is the radius.

## 6. What reproduced exactly

Recorded so these are not re-measured. Each was re-derived here, not read off any document or
prior record.

| claim (subject bytes) | recorded | re-derived |
|---|---|---|
| out-of-block token lines, whole file minus `:231`–`:651` | 24 | **24**, and the block itself holds **0** — the total is 24 |
| product command body | 7 · `:57/:93/:95/:104/:106/:116/:126` | **exact, all seven** |
| v1 stage group | 15 within `:134`–`:223` | **15** · `134 145 146 158 161 164 177 178 193 194 208 209 211 220 223` |
| `:850` shared error exit | `except stage_control.StageControlFault` in `main()` | **exact** |
| top-level command groups | 5 (4 via `add_parser` + `:739`) | **exact** — `:656` `:664` `:674` `:746` + `harness_cli.register` `:739`; `rsc.py` **856** lines |
| pre-commit hook | 4 python call sites, 6 scripts | **4** (`:13/:27/:40/:56`) and **6** (audit · provenance · ledger-cap · three harness hooks in the `for`) |
| `tooling/hooks` tracked | 4 | **4** — `__init__.py` + three checks; `contract_provenance_check.py` absent, so that hook段 is dead |
| `pack_digests` whole-repo `*.py` | 5 hits, 3 of them v2 | **5** — `__init__.py:238`/`:266`, `harness/schemas.py:75`, `resolver.py:272`, `tests/harness/run_tests.py:39` |
| travel set, seven prefixes | 245 @base, 250 @tip | **245** / **250** |
| commits touching the seven-*path* set | 335 / 720 @ `0db52a1` | **335** / **720**; the printed command runs verbatim |
| records in the migration directory | 117 @base | **117**; 120 at tip (see `L-2`) |
| 29 / 88 under the stated criterion | 29 product, 88 construction | **29 / 88** — first 40 lines, run name or `assurance/runs/` |
| deletion arithmetic | 171 / 139 / net 32 | consistent with the prior record's re-derivation; `stages/` **2** files verified here |
| §11's 起因 count | three reads, four must-fix | **1 + 1 + 2 = 4** from the three records' own summary lines |
| `E2` / instruction layer across the range | untouched | **3 blobs SAME, pack 15 / 0 changed, 9 of 9 members SAME** |
| `repo-audit` / `ledger_cap_check` at tip | clean | **exit 0** / **exit 0**, ledger **114** lines |
| `HD-38` separation | free-channel bytes in their own commit | **holds** — `e788169` and `f97bb17` do not overlap |
| `§live` entries | — | **12** at tip |

## 7. Coverage and ceilings (`R4`)

**Read in full**: the four changed files at the tip (`split-design.md` 346 lines, the journal 133,
`HARNESS-DECISIONS.md` 408, the plan 169); `v3-checkpoint-read-b75676e.md`, the record this range
answers; `CONSTRUCTION-CHECKLIST.md`; `HARNESS-LEDGER.md`; `HARNESS-RIDERS.md`; all four commit
messages; the whole range diff.

**Sampled**: `rsc.py` — every line matching the five coupling tokens, every `add_parser`
registration, the import head, `:674`, `:739`, `:850`; not the whole 856.
`D:/Thesis/.git/hooks/pre-commit` — its python invocations and the `for` loop; not its error text.
The three prior R0 read records — their summary lines only, to reproduce §11's 起因 count.

**Probed only** (command output, no reading): the record-directory counts at five revisions; the
seven-prefix and seven-path commit and file counts; the 29/88 and 63 classifications; the
`interface_version` scan; the `.claude` inventory; the split-design blob chain; `repo-audit` and
`ledger_cap_check`.

**Not read**: `EXECUTION.md`, `README.md`, the two retired-contract stubs and
`paragraph-map.schema.json` — all four verified byte-unchanged and nothing in this subject depends
on their content; `io-design.md`; `Thesis/Work/Tooling/repo-audit.py` (exit code only, no source
read this round); the thirteen inbound links (unchanged since the prior record re-derived them line
by line); the caller-side product tree; the regression battery (not run).

**`UNVERIFIABLE`, not folded into supported** (`R4`):

- **`journal:76`'s 63/64** — see `O-1`. Four candidate criteria give 69 / 64 / 78 / 57; the text
  states none.
- **That `12a28ce`'s abandoned dispatch reached no review session.** The commit asserts it; the
  repository can show the marker existed and that no record for `4342c6b..f97bb17` was ever
  written, which is consistent with the assertion and does not establish it. What I *can* establish
  is that the cost is nil, because that range is a prefix of this one.
- **Process claims marked, not verified**: that this session held only the review role for its whole
  life (`E1`); that the round division, the eight §10 rulings, the `HD-40` signature and the
  2026-08-14 approval of the 量程纪律 were given as the repository records them (`R7`).

**Independence** (`R1`): this session was dispatched, scoped and is reported through the
orchestrator; the executor set none of the four. No prior record for this subject existed in the
worktree at open (`git status --porcelain` empty, canonical path absent), so there is no collision
disclosure to make. `M-1`(a)(b)(d), `L-1`(b)(c), `L-2`, `L-3`, `L-4`, `L-5` and `O-1` are findings
no prior record raised; `M-1`(c) is the surviving half of the previous record's own `M-2` scope
note, re-derived here; `L-1`(a) is a sweep of the class `M-1`(c) named, re-derived from the
repository.
