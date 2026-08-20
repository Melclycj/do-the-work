# 构造轮 `V1-CONTEXT-EXACT` — 兑付 rider `V-1`（2026-08-05）

> 起因：用户裁决 **P5B 走编号态，先兑 `V-1`**。`V-1` 的 deadline 原文是「任何一份指令被写成编号态
> 之前」，所以它是 P5B 批次的先决，不是可延后的清理。范围：`288e36f..HEAD`。
> 本轮刻意短——产物是一行判定 + 两组测试，叙事不该比它长（记录层重设计的 18.7:1 底账正是冲这个来的）。

## 1. 改了什么，为什么是「精确」

`_is_context_title` 由 `title.casefold().startswith("context")` 改为
`title.casefold() == "context (non-normative)"`。

这是**同一个洞的第二次收窄**。它最初是 `"context" in title`，被 f1 抓住
（`## Appendix A — the frozen context bindings` 下挂规范冻结表，判为非规范）；f1 的修法收成前缀，
于是 `## Contextual appendix — the frozen bindings` 原封不动地重现同一失效
（`v3-review-verify-c7fb720.md` `V-1`）。**前缀不是小节**——两次都被证伪的是同一句话：
docstring 自述的 *anything else falls to the prose form*。现在那句不再是对代码的断言，它就是规则本身。

施工前实测（`E3`，在改动前跑，即缺陷的复现）：

```
resolve_form    : enumerated   notes=()          ← 标题 "## Contextual appendix - the frozen bindings"
form_conformance: ()                                下挂 "Every row above is frozen; ... is a defect"
EXEMPT  | Contextual appendix - the frozen bindings
EXEMPT  | Context bindings for the frozen shells
EXEMPT  | CONTEXTUALISED requirements addendum
```

三件派生件（paragraph map · preamble gate · 逐义务审计的对象）正是在 `enumerated` 下被关掉的，
所以「静默通过」等于 START 批准面比指令窄——w1-r1 与 p4-bridge 各为此付过一次。

合规词汇的代价实测为零：

```
$ grep -rn '^#\{1,6\}.*[Cc]ontext' ResearchSystem/assurance/runs/*/instruction.md
p3-corr:90  p4-bridge:80  p4-doc:114  p5a-firewall:86  p5a-shells:217  p5b-firewall:146  w1-r1:67
→ 7 hits，全部恰为 "## Context (non-normative)"
```

**保留大小写不敏感是一个决定，不是遗留**：喊着写的标题仍是那个小节，没有任何缺陷形状落在这个差别上；
它被单独写成一条测试，好让评审员能挑战它，而不是让它藏在 `casefold` 里。

## 2. 钉的是类 —— 第一版只钉了一半，被 FULL 测出来（`E7` · `O-1` · `b1`）

VERIFY 的 `O-1` 指出：f1 的修法只钉了 appendix 那一个实例，`## Additional context` 行为上被拒但
无任何测试绑定。第一版据此把集合写进 `NOT_THE_CONTEXT_SECTION`（手写字面量，`E5`），五个形状全断言，
并在 `transcript_audit` 那条腿上加了 V-1 形状——`context_text` 与 form lint 共用同一个豁免判定，
前缀修法把两条腿一起留了口子。断言不只看错误码，还要求 issue 文本里出现**被测那个标题**的 `repr`，
否则任何无关块都能满足它（`E5` 的「断言整行」）。

**然后 FULL 的 `b1` 证明那句「钉的是类」是假的**（`v3-review-full-ca9c055.md`）。五个形状**全部**取自
f1（子串）与 `V-1`（前缀）这两代**已经关掉**的失效——那是「已见过的缺陷集」，不是类。评审员把同一个
substring→prefix 的手滑套到**新字面量**上（`startswith("context (non-normative)")`），
`## Context (non-normative) — the frozen bindings` 下挂规范冻结表照样 `enumerated`、零 notes，
**全电池 600 全绿**。f1 的失效形态第三次，而写来终结这个循环的 sweep 看不见它。

修法（本轮唯一一次用户批准的修）：集合**向前也写**——补进新字面量自己的边界，以及**裸标题
`## Context`**（前两代豁免、精确态起被拒，这是一次真实行为变更而它记录在零处；评审员**没有**要求这一条，
是用户在批准修法时明确加入的，见 commit 正文的边界声明）。`transcript_audit` 那条腿同批补 `b1` 形状。
现在集合七个形状，两代历史 + 当前边界 + 一条被记录下来的行为变更。

## 3. `E4` mutation（三次；跑的是**两个被改模块共 38 例**：`test_instruction_form.py` + `test_transcript_audit.py`。scratchpad 复制 + sha256 前后比对，未用 `git checkout --`）

| # | 中和成什么 | 预期红的 | 实际（38 例作用域内） |
|---|---|---|---|
| **M3** | `.startswith("context (non-normative)")`（`b1` 的形状：把同一手滑套到**新**字面量） | 新增的 `b1` 行 + audit 腿 | **2 failed, 36 passed**。失败的 subtest 由断言消息自报身份：`("FULL b1: the new literal's own boundary — opens with the whole exempt title", ())`。**修之前这一档是 600 全绿** |
| M1 | `.startswith("context")`（`V-1` 缺陷形状**逐字**） | class sweep + audit 腿 | **2 failed, 36 passed**；首个失败 subtest `('V-1: opens with it, one word later than f1', ())`。负对照（精确标题、大小写变体）全绿 |
| M2 | `"context" in title.casefold()`（f1 时期的形状） | 上面两条 + f1 原测试 | **3 failed, 35 passed** — sweep 同时覆盖两代 |

**为什么这里要写作用域**（`L-1`）：38 与 §4 的 600 是两条不同的命令，不写清楚，后来人会把口径差读成回归。
`E3` 要求数字由产生它的命令吐出——命令与例数都在这一行的标题里。

复原后摘要与交付物一致：`f2dee2480df86432a5e7408916f5dd026738ef1ebbb38e4c0309a271e0db398a`
（交付的 `instruction.py` 与 scratchpad 同摘要；每次 mutation 后各比对一次）。

## 4. 全电池（触及 tooling → 重档），末次读数

pytest 全树 **600 passed** · P2 **29/29** · P4 **80/80** · P5A **32/32** ·
N0 契约 fixtures **41/41** · `rsc compile --check` **0 error(s), 0 warning(s)**。

598 → 600 可自行推导、不必采信：本轮只新增两个测试方法（`test_no_heading_but_the_context_section_itself_is_exempt`
与 `test_the_context_section_stays_exempt_however_it_is_cased`）；`transcript_audit` 那条由单例改为
循环，方法数不变。**修腿之后仍是 600**，同样可推导：`b1` 的修法加的是 `subTest` 循环里的**数据行**
（form 腿 5→7 个形状、audit 腿 2→3 个），不是测试方法——所以「例数不变而覆盖变宽」在这里是正确读数，
不是漏跑。

## 5. 开轮 `E10` 层 read

已跑，记录 `v3-checkpoint-read-a5a04c3.md`（commit `562e948`），**0 must-fix · 2 low · 1 observation**。
读者九个成员全部通读、并关掉了成员 7/8 的引用链，故该记录可被后续开轮直接引用全部九个。
**本轮不碰任何层成员**，其开轮 read 即由该记录引用满足。两条 low 已入 bank（`chk-thin` / `HI-route`，
处置 commit `288e36f`），deadline 是下一个 product run 的 FULL，即 P5B。

## 6. SIMP-ABCD 两笔未落账的处置（搭车，用户 2026-08-05 批准）

**① VERIFY `v3-review-verify-c7fb720.md` §4 的五条 observation**，逐条：

| id | 处置 | 依据 |
|---|---|---|
| `O-1` | **本轮关闭** | §2 的 class sweep 覆盖它点名的 `## Additional context` 及其余四形状 |
| `O-2` | **入 bank**（rider `ctx-ground`） | 用户裁决不做：让 harness 测试去读 `assurance/runs/*` 是新机器，`E6` 的反面。但「7 份指令都恰好这么写」是精确匹配与其负对照共同踩的地基，将来写歪会静默掉进 prose 态，故记账 |
| `O-3` | **`R9` wording-level，不入 bank** | VERIFY 自述「方向是 fail-safe（违反即停机），没有决定会错，只是措辞强于机制」——这正是 `R9` 判据里「点不出会出错的下游决定」。搭下一批碰 `check_audit` docstring 或 run-v2 README `:148` 的批 |
| `O-4` | **入 bank**（rider `mark-case`） | 有决定会错（小写 `must` 落在 Context 里不响，规范要求可无标记地留在批准面外），但改成大小写不敏感会让普通英文 must 满地误报——是设计题，不是字节修。同时**已写进交付的 docstring**，免得记录读起来像已关 |
| `O-5` | **本轮修准** | `R9`，原文「rides the next batch touching either file」。那句是**新增那一节**的结尾句（`EXECUTION.md:154-155`），文件真正的结尾是 *What you are never asked to do*。只改本 journal 与下条的指针措辞，**不动 `EXECUTION.md`**（层成员，动它另算） |

**② `SIMP-A4` 的两种读法** —— **未决，需用户裁决**，本轮只把问题写准，不替它选。
需求原文（`checker-and-map-2026-08-05.md:106`）：*保留一条不绑定任何义务真值的 lint，只抓低级错误、
省评审时间*。SIMP-ABCD 按读法 (a) 结账：落地物是 `form_conformance`，规则文字是
`EXECUTION.md` 新增那一节的结尾句（**不是**文件结尾句——见上 `O-5`）。

- **(a) 指令侧 lint**：`form_conformance` 判指令形态、不判任何义务真假。字面吻合，且**已交付**。
- **(b) 候选侧 lint**：接替被删的逐义务检查器，对**候选**抓低级错误。**未做**。需求里「省评审时间」
  更偏这一读——评审员的时间花在读候选上，而 `form_conformance` 跑在 pre-START，那时还没有候选。

两读法都不改任何层成员文字（读记录 §4 独立确认了这点），所以这是记账问题、不是规则冲突。

## 7. 诚实边界（本轮**没有**关掉的）

- **只判哪个标题豁免，不判它下面写了什么**：真 Context 小节里没有标记词的规范陈述句照旧看不见——
  这是 `form_conformance` 自述的 ceiling，backstop 仍是 FULL 的指令重走。
- **`_NORMATIVE_MARKERS` 仍大小写敏感**（`O-4`），已写进 docstring。
- **编号态仍然没有一份真实指令**：关于它的一切断言——包括本轮的——都建立在合成形状上。第一份真编号态
  指令（P5B）同时是 `V-1`、`O-2`、`O-4` 三条的首次真实检验。

## 8. 收口（2026-08-06）

链条：FULL `v3-review-full-ca9c055.md` **`CHANGES_REQUIRED`**（1 blocker · 2 low · 1 observation）
→ 一次用户批准的修 `25511d9` → VERIFY `v3-review-verify-25511d9.md` **`REVIEWED_NO_BLOCKER`**
（0 blocker · 0 low · 3 observation）。`E9` 预算三样用尽。

**blocker `b1` 是对本轮中心主张的否定，不是对代码的**。我在三处（commit 正文 / 本 journal §2 /
sweep 的 docstring）都写了「测试钉的是类」，而五个形状全部取自已关掉的两代——那是**已见过的缺陷集**。
VERIFY 用双向实测封死了这一点：同一个 mutation 对**修前**的测试是 38 全绿、对**交付**的测试是 2 红。
`instruction.py` 全程未动（`f2dee248…` 与被评审字节同摘要），所以修法边界比本轮边界更窄。

**三条 observation 的处置**：

| id | 是什么 | 处置 |
|---|---|---|
| `O-1v` | **第四种手滑仍然全绿**：把判定松成 `endswith("(non-normative)")`，`## Appendix A (non-normative)` 下挂规范表又变非规范，pytest **600 全绿**。评审员明说：**没有任何字面量集合能关掉这个类** | **不修**（`E9` 预算已空，且这是设计题）。它是 FULL 的 `O-1`（豁免小节该不该改成**声明式**）的实测证据，**归用户**，随 P5B 一起议 |
| `O-2v` | 出轮 commit `32cf220` 在正文里自判「不占 `E9` 预算」，而 `E9` 写着**不得自判哪一轮消耗了什么**；评审员判其 benign（判据在 commit 表面、可由检视判定），但要求 **closeout ratify 而非 inherit** | **本次追认**：用户 2026-08-05 批准「⓪ 走自己的 commit、不占额度」，判据=改的不是被评审的 work product 且路径在 `ResearchSystem/**` 外。追认落 ledger |
| `O-3v` | base commit `2d76629` 的树不能通过本仓自己的 pre-commit gate（audit 修当时未暂存），下一个 commit 自愈。评审员附言「更省事的顺序（先 audit 修、后记录）当时可用且零成本」 | 事实部分**接受**；**附言经实测不成立**——见下 |

**对 `O-3v` 附言的实测更正**（`E3`：不凭记忆下结论）。冻结窗口开着时把 `repo-audit.py` 暂存并跑
`review_freeze_check.py`：

```
pre-commit BLOCKED: a review/read is out (E9: from dispatch to its record's
commit the branch takes no commit but the record itself).
  staged : Thesis/Work/Tooling/repo-audit.py  (not a review record)
review_freeze exit=1
```

所以「先 audit 修、后记录」这条路要么删 marker、要么 `--no-verify`，两者都违反 `E9` 本身。真正暴露的
不是一次随手的顺序选择，而是**两道守卫的互锁**：`review_freeze_check` 说只有记录能落，`repo-audit`
说这份记录不能落。返回的记录一旦踩中 audit，就没有同时满足两者的顺序。这条**入 bank**
（rider `freeze-audit`），因为它会复发，而且下一次未必有像本次这样干净的根因修法。
