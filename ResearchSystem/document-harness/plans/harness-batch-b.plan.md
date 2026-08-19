# Plan: Batch B — 谁调用、谁绑定

- **slug**: harness-batch-b
- **created**: 2026-08-11
- **complexity**: 中等（一个构造轮 + 一批记账 + 一个待定的设计轮）
- **status**: **CLOSED 2026-08-13 —— R0/R1/R2/R3/R4/R5 全部收批**
- **base_commit**: `adb6989`
- **base_branch**: document-work-assurance-v3

## Goal (one line)

把 harness 的对外 I/O 边界收干净：让产品 run 真的用上「读不懂就别往下跑」的引擎（`run_all` 接线），
并把 ledger 从仪器里解耦成输出对象——**仪器只输出，不负责往 ledger 写**。

## Entry gates — 已过

- **`§live` cold read**（`E10` (b) 义务句，rider `waiver-live` 标注的边缘不适用：本批未请求豁免）：
  `HD-24` · `HD-23` · `HD-10` · `HD-15` · `HD-16` 五条全读，2026-08-11。
  **本批不执行其中任何一条**——它们是拆分批的。
- **指令层九成员 cold read**（`E10` 引用条款：blob 未变即可引用记录）：九成员在 `3f19561..adb6989`
  之间**零写入**，逐个 `git rev-parse` 比对 blob id 全部 SAME（输出留在本批 journal）。
  按 `v3-checkpoint-read-3f19561.md` §1 逐成员锚引用——**不是 `bd77fd4` §1**（其 `O-2`）。
  blob 7/8 等于 `E2` 的冻结 id，如其所必须。

## 本批要建的裁决（本 session 用户已裁，尚无 HD 条目）

`HD-4` 三问全部为是（绑下一轮及以后 / 收窄已有路由 / 除对话外无家），所以三条都欠条目。
**编号是提议，状态由用户翻（`HD-2`）**：

| 提议 id | 裁决 | 影响 |
|---|---|---|
| `HD-25` | `run_all` **接线**，切面 = **只改模板**，现存 8 个已关闭 run 不回改 | R1 的全部授权；与 `HD-16` 同向 |
| `HD-26` | ledger **解耦**：harness 只输出、不写入；具体形状 **defer 到 I/O design**（= R2）。backlog 里「citation 规则暂留层外」一句**作废**——查无承载，用户裁定删除 | 收窄批 B；改 ledger `:47`/`:94` |
| `HD-27` | `pack_digests()` **不接** `E2`，`E2` 也不加路径判据守卫；**重开条件 = 拆分批** | rider `PD` 重定范围（非兑付，行不删，比照 `HD-22`） |

`HD-27` 的三条实测依据（进 journal，不进条目正文）：产品 run 侧 `_check_git_diff_boundary`
（`checks.py:310`）已拿改动路径比 `boundary.out`，而 run 的 `out` 逐条列着 `ResearchSystem/schema`
与三份契约——暴露面只剩构造批；构造批每轮有独立评审且其 boundary 检查点名 frozen surface；
`HD-16` 刚裁了已关闭 run 的产物不出仓，(b) 的「证据离仓自证」价值随之落空。

## Steps

### R0 — 记账。不开轮（2026-08-03 裁：ledger 删减/记账批 user ruling 即 gate）

- [x] 1. 建 `HD-25` / `HD-26` / `HD-27` 三条 `§live` 条目；`HD-27` 同 commit 改 rider `PD` 的
      redeem-when → **拆分批**（行不删，重定范围非兑付）。— **done**；`HD-27` 定 `live` 而非
      `implemented`：rider `PD` 只承载 `pack_digests` 那半边，「`E2` 通用守卫也不加」这个 standing
      do-not 无别家（`HD-2` 的判据＝有没有别的东西替它说话）。
- [x] 2. `HARNESS-LEDGER.md`：删 `:47` 与 `:94` 的「citation 规则因此暂留层外」半句；批 B backlog 行
      由三件收窄为两件（① 接线 · ② 解耦 defer）；③ 改记「已裁不做，重开条件=拆分批」。
      **120 行上限：一处添加欠一处删除**，落笔前 `wc -l`。— **done**：113 → **114** 行（cap 120），
      `grep -n citation` 返回空。
- [x] 3. 本批 journal 开档 `document-harness/journal/batch-b-2026-08-11.md`：cold-read 的 blob 对照
      输出、`HD-27` 的三条实测、下面 R1 的两个设计子问题。— **done**，四节（cold read / ledger 耦合
      四处 / `E2` 三条实测 / `run_all` 现状与两个未答子问题）。

### R1 — `HD-25`：把 `run_all` 接进模板

- [x] 4. `assurance/templates/run-v2/run_evidence_v2.py:177` 的 list comprehension 换成
      `C.run_all(checks, order, ctx)`。— **done**。
- [x] 5. 顺序来源随之改变：现在是 `sorted(glob("check-chk-*.json"))`，`run_all` 要的是
      **plan 的 `check_order`**（`resolved-plan.json` 已有该字段）。这是行为变更，不是重构——
      须在 commit 正文点名，并加一条断言测试钉住「顺序取自 plan 而非文件名」。— **done**；
      **本步骤的措辞被实测更正**：`check_order` 在 `resolved-assurance-plan.schema.json` 里
      **不是 required**（描述："absent when the run has no deterministic checks"），所以
      `plan["check_order"]` 会崩掉 schema 明说合法的 run——实际写成 `plan.get("check_order", [])`。
      这是本步骤自己发现的缺陷：先写成下标形式，跑全量时打挂了 sibling suite 的 `deriv-bind`
      两条（其 fixture 的 plan 正因为不声明 check 而省略该字段）。
- [x] 6. 新守卫按 `E4`/`E5`/`E7`/`E8` 验：neuter → red → 从 sha256 校验过的 scratchpad 副本还原
      （**不用 `git checkout --`**）；每条 must-fire 配负对照；断言整行不断言子串；测的是缺陷类
      不是报告实例。— **done**，两次 mutation 均从 sha256 校验副本还原（还原后哈希复等
      `a59cc546…`）：**M1**（order 退回文件名排序）杀 6/7——**超杀，如实记**：停机族的断言把顺序
      写进了期望值，故顺序一变它们也红，隔离度不如 M2；**M2**（保留 plan 顺序、拿掉立即停机）
      杀 4/4 停机族、放过顺序族与负对照，隔离干净。M2 的四条里三条值级红，
      `test_a_request_the_plan_orders_but_the_control_root_lacks_is_refused` 是 `KeyError`
      驱动的红（按 `R8`，崩溃只证明测到了代码，不证明绑住了行为）——如实记。
      **⚠ 本步骤上面这段 mutation 证据已作废，勿引用**（VERIFY `dbbec28` `V-1`）：`a59cc546…`
      与「M1 杀 6/7」量的是一个**未交付的中间版本**——快照之后又改了 `.get()` 并加了第八条测试，
      没重测（FULL `e9166d2` `B-2`）。**取代它的**是修腿 `dbbec28` 对交付字节的重测，并经 VERIFY
      逐项复算：模板 `ae3f6c78…`、套件 `228e2bfa…`；**M1 7/8 · M2 4/4（停机族）· M3（下标形式）
      1/7**，M3 杀的正是 `test_no_order_means_no_check_runs`，值级红。
- [x] 7. **电池**：改的是 `.py`，按 `EXECUTION.md` §Regression-battery tiering 属 **tooling-touching
      → 全电池**。按 rider `tier-scope` 实跑**六腿**（枚举句只写四腿，实际另有 `tests/harness` 39 与
      `tests/stage_control` 20），且 pytest **scope 到 `ResearchSystem/tooling`**（仓库根直跑会因
      `ExperimentLab/papers/` 两处同名 `smoke_test.py` 撞包中断收集）。— **done**，五条命令覆盖
      六腿，全绿：`tests/run_tests.py` 29 passed（**仅 P2 goldens**，见其 docstring）·
      `pytest -q` @ `ResearchSystem/tooling` **705 passed** · `tests/harness/run_tests.py` 39 OK ·
      `tests/stage_control/run_tests.py` 20 OK · `rsc.py compile --check` exit 0（173 live）。
      **⚠ 本步骤「五条命令覆盖六腿」的账已作废，勿引用**（FULL `c7e0ba0` `B-1`；V-1 更正，
      用户裁 2026-08-13）：`tests/run_tests.py` **仅 P2 goldens**（见其 docstring），P4 goldens /
      P5A goldens / schema fixtures 三腿在 R1 同样没有命令；更正后的口径见步骤 12 与 journal §7。
- **Revert unit**：`assurance/templates/run-v2/` 加其 `tooling/tests/document_harness_review/`
  下的套件，一个 commit。
- **两个设计子问题，已答（`E11` 卡前查实）**：
  - **① SPEC_GAP 抛出后写不写部分证据 —— 查实后改为不写，这是对已批卡的收窄，如实记。**
    `check_subject`（`review_subject.py:433-452`）遍历 `plan["check_order"]` 要求每 id 一份
    per-result 文件，但它读的是**已提交的 evidence commit**；撞上 `SPEC_GAP` 的 pass 走既有
    `STOP … nothing committed, state not advanced`，什么都不提交，所以够不着。卡上写的是"写已跑出的
    部分结果"，**实际没写**：`run_all` 是 `raise`，要拿到部分结果必须改它的契约（把 results 挂到
    异常上）＝新机器，而 `E6` 反对；且出事的 `check_id` 已在异常消息里，诊断不缺这一口。
  - **② 现存 8 个 run 不继承。** run 是把模板**抄**进自己 control root（rider `delta-prose`），
    所以改模板只对**之后起草的 run** 生效。这是 `HD-25` 已接受的代价，写进 commit 正文。
- **超出卡面的一件，如实记（`E8`）**：卡上是两条断言测试，实际交付**三类共 8 条**——多出来的
  `APlanWithNoCheckOrderRunsNoChecksAndDoesNotCrash` 是步骤 5 那个 schema 事实逼出来的缺陷类
  （`E7`），不是顺手加的。另：既存隐患**未修**——模板只 `EVIDENCE.mkdir(exist_ok=True)`、从不清理
  旧 `check-chk-*.json` 残件，中断的 pass 会留下它们；这是本轮之前就有的形状，不在边界内。
- **可能同批到期的 rider**：`tier-scope` ①（本批就是「下一个 tooling-touching 批按枚举句自选电池腿」
  那一刻）· `readme-three`（仅当 R1 动了 run-v2 README 实例化段）。**`tier-scope` 的修法是改
  `EXECUTION.md` 的枚举句 = 改规则要求 = 设计开轮**，见下面「待用户裁」。

### R2 — `HD-26` 的**设计**（前置 = R1 落地，已满足）

> **用户 2026-08-12 裁：R2 只设计、不落地；落地另开 R3。** 好处是设计成型时用户先看一眼再决定
> 要不要按它施工；代价是多一轮。R2 因此**不动任何产品字节**，产出是设计文档 + 用户签字。

> **用户 2026-08-12 再收窄**：R2 **先只做第 8 步（含下面两个方向），做完停下来报告、与用户讨论
> 出方案，才进第 9 步设计**。第 9/10 步在讨论前不动。

- [x] 8a. **方向甲——ledger 与本 harness 解耦**（`HD-26` 的既定方向）：枚举现状，逐处判"拆了会掉
      什么"。— **done**：四处耦合 + 逐处后果在 journal §2 与 §5 补录表左列。已测得四处耦合，两读两写：
      读 = `tooling/hooks/ledger_cap_check.py`（硬编码 ledger 路径 + `MAX_LINES=120`）·
      `dispatch.py:636` 层 read 提示词（"what the ledger binds to this read"）；
      写 = run 的 `write_scope` 直接列 ledger 路径（p3-corr / p4-bridge / p4-doc）·
      `chk-ledger-note`（p4-bridge 的 `locator_exists`，锚点是 ledger 里一句人写的中文散文，
      全仓仅此一例 1/8）。
- [x] 8b. **方向乙——反向假设：ledger 由 harness 自己拥有，改为从 global Claude Code setting 解耦**
      （用户 2026-08-12 要求同批考察）。问的是：ledger 的写入格式本是 **global 约定**（全局
      `CLAUDE.md` §0.7 的持久账本层 + `/ledger` `/preclear` 命令 + `.goals/LEDGER.md` router），
      若反过来让 harness 拥有它、由 global 侧松手，**harness 的使用会变成什么样**——谁写、谁读、
      新 session 怎么接、拆分批时账本跟谁走。两个方向的后果并排呈表，**不预设结论**。
      — **done**：呈表最初只在对话里（R2 转录核查 finding 4 抓的正是这个缺口），2026-08-12 补录
      进 journal §5 顶部；乙向实测（global 规范完整、harness 是收紧方言占三参数）在 §5 首段。
      用户在表上裁的是第三条路：仪器不写入 + 实例归调用者 + global 规则层保留。
- [x] 9. 设计输出契约：harness 产出**什么**，ledger 自己去取。— **done（2026-08-12）**：设计
      定稿于 `document-harness/io-design.md`（八节：functionality 边界 / 三角色 + 载体 / 11 条
      orchestrator 义务 / 输入面 / 输出面 / 实例初始化 / submodule 调用模型 / 待处理清单）。
      **本步骤原文的「硬约束」被讨论收窄**：结论 = 命令输出（现有 status/flow/disposition 三命令，
      单一结论命令随独立 CLI 归拆分批）；对外动作 = 调用者策略文件（`CLAUDE.md` 承载）由
      orchestrator session 读、harness 代码绝不执行；`chk-ledger-note` 的承接物**在调用者侧自选**
      （策略文件可声明锚点断言进调用者 pre-commit/CI）——保障从 harness 内确定性检查转移出去，
      此代价随方向裁决被接受。**gate = 用户对文档签字**（按已批预览卡，R2 无 FULL 预算）。
      同 commit 建 `HD-28`（`HD-16` B 组收窄，双向指针）与 `HD-29`（submodule + 调用者纪律）。
- [x] 10. **`E`（topology claim 形状）** — **用户 2026-08-12 直接裁删**（"这个我也不记得了，之前
      找过也没找到"）：有界溯源免做，ledger「未结（open）」行已在同 commit 删除该项、未带进 v4
      （ledger 记账批，user ruling 即 gate，不开轮）。
- **产出**：一份设计文档（落 `document-harness/` 或 journal，R2 开轮时定）+ 用户对形状的签字。
- **Revert unit**：设计文档本身，一个 commit。R2 不碰代码，所以 revert 即删文档。
- **电池**：doc-only（`EXECUTION.md` §Regression-battery tiering）——**除非**设计文档落在
  `document-harness/README.md` 这类"代码枚举或测试钉住"的位置，那按该节的例外算 tooling-touching。

### R3 — 按 R2 签字的设计落地（前置 = R2 的设计经用户签字）

- [x] 11. 拆四处 ledger 耦合、ledger 规则/脚本移出 harness 树（`ledger_cap_check.py` →
      `Thesis/Work/Tooling/`，本机 `.git/hooks/pre-commit` 路径引用同步——per-machine 件、非仓库
      保证）、本机策略文件 `ResearchSystem/HARNESS-POLICY.md` 落笔 + `CLAUDE.md`/`AGENTS.md`
      各一行指针（镜像规则同 commit 双写；载体裁决 2026-08-12，重签见 `HD-35`）；
      承接物按 `HD-31`——调用者侧自选，不欠 harness 侧替代检查。
      **边界外**：已关闭 run 的 `write_scope`/`chk-ledger-note`（依据 `HD-25`「现存八个已关闭
      run 不回改」条款；原引 `HD-28` 系张冠李戴——它管归仓不管改动，修腿按 FULL L-3 更正）；
      「今后 run 不得绑 ledger」的规则文本归 R4。— **done（2026-08-12，候选 commit）**：卡经用户批
      （测试删除而非随迁、RECORD_SURFACE 第五处引用维持边界外，均默认通过）；READ_PROMPT 的
      fixture（`expected-read-prompt.txt`）同 commit 同步；README.md Local-enforcement 行减法走
      `E10` deferral 通道；`HD-31` 同 commit 翻 `§implemented`。细目 journal §6 + commit 正文。
- [x] 12. 全电池 + 记账。（rider `RA` 已 2026-08-12 重定范围到拆分批，不在 R3 兑付。）
      ——**done（2026-08-13 closeout）**：记账半边收口（ledger 批 B 行 R3 CLOSED + 锚；
      V-1 两处更正随本 commit）。
      ——电池半边经修腿更正（FULL `c7e0ba0` B-1）：候选 commit 前实跑**五命令**（29 ·
      701（705−4，删 `LedgerCap` 四测试的对账）· 39 · 20 · `compile --check` exit 0），当时
      写的「六腿全电池」是无命令背书的定性——`EXECUTION.md` 点名的 P4 goldens / P5A goldens /
      schema fixtures 三腿没跑（`run_tests.py` 按其 docstring 只跑 P2，R1 记录称其覆盖四腿
      系假，同句已连抄三个 commit）。修腿在改后的树补齐三腿并重跑全套八命令，输出
      journal §7；`tier-scope` ① 注解不变。**记账半边归 closeout**（评审链走完后 ledger
      批 B 行）。
- **Revert unit / 步骤细目**：**刻意不预先编**——形状由 R2 的设计决定，现在写就是凭空猜。
  R3 开轮时按 `E11` 出自己的预览卡。

### R4 — 指令层重指轮（批 B 新增，用户 2026-08-12 裁；前置 = R3 落地）

- [x] 13. amendment：`R1`/`R6`/`R10` 的「executor / execution side」称谓按三角色重指 ·
      `E1` subagent 句（现与「reviewer 可为 subagent」相抵）·「Execution side」节头作用域句 ·
      `R10` "never here" 重新指向（rider `R10-route` 的三问同批一并答，其行同批处置）·
      WorkSpec 入轮内的流程文本落点。**每条 amendment 欠独立 read，改规则要求 = 设计开轮**
      （`E10`）；预算照 `E9` 一轮三腿。— **done（2026-08-13）**：切面经用户批扩为
      **io-design §8 五项 + rider `tier-scope` 三件**（① 全电池枚举句改按 R3 修腿实测的八条命令
      并写「nothing fewer」· ④ pytest 补 scope · L-2 头部 disclaimer 加限定点名 tiering 为唯一
      施工侧例外；② revert anchor 未做，行不删、收窄到只剩它）。评审工具取 `E10` 独立 read
      （先例 `E2-VERB-E10-PIN`），**非 FULL**——`E9` 三腿全程未花。链：`be9878a` 候选 →
      read 1 `2e43ecf`（1 must-fix + 3 low + 1 wording + 2 obs）→ amendment `b9e6fd8` →
      bank `0aed595`（`E1-suff`/`tier-file-vs-clause`/`wspec-owner`）→ read 2 `f3f31c0`
      （**同缺陷类的兄弟句**，`E7`）→ amendment `8884f47`（取删除而非条件化）→ read 3 `18ac031`
      （**0 must-fix**，链终止；1 low）→ bank `55fe9d3`（`frozen-path-prefix`）。
- [x] 14. R4 落地后三角色操作纪律生效：dispatch 改由 orchestrator 发（`R1` 独立性从纪律变结构）、
      reviewer 可走 subagent。零代码，纯操作纪律。— **done（2026-08-13）**：`E1`/`R1` 的字节已落
      并经三次独立 read，纪律自 `8884f47` 起在 force。**尚未行使 subagent-reviewer**——R4 的三次
      read 全走「用户当传输 + 全新 session」，故该半边是**已授权未实测**，如实记。
- **产出**：批 B 收批时，io-design 八节里除 §6/§7（真跨仓、归拆分批）外全部落地。

### R5 — `E10` 通道边界 + `R10` rider 到期判据（批 B 新增，用户 2026-08-13 裁；前置 = R4 落地）

> 起因：R4 跑三次 read 跑出一簇同面的洞，用户逐条裁定后合成一轮。**不是 R4 的修腿**——R4 文本已
> 干净（read 3 零 must-fix），这些是 R4 **暴露**出的规则缺口。

> **R5 CLOSED 2026-08-13。** 链：`136f27f` 候选 → read `bf2fd09`（1 must-fix + 1 wording + 3 obs）
> → amendment `f61ce2c` → 再读 `c0efda3`（**0 must-fix** + 2 low + 4 obs，链终止）→ bank `8dab6ee`
> （`wl-route`）→ 裁决 `1b861db`。`E9` 三腿未花。**read 5 的 `L-1` 用户裁「行为让步」**——`R10` 原句
> 站住、零字节改动，今后自由通道字节单独 commit（`HD-38`）；已落的三个混装 commit 记为已知不符历史。

- [x] 16. `E10` must-fix 通道句加两条（用户裁决 2026-08-13）：executor 可**扫缺陷类**、
      **无字节的 must-fix 由 executor 自己写**。根因证据 = R4 一个缺陷类拆成两轮 read 才修完
      （`E7` 绑 executor 要求扫类、`E10` 又不许写未点名字节，两条对冲）。
- [x] 17. `E10` 优先句 `the named literal replacement` → `the bytes the finding supplies`，
      把 design test 收窄回**自由通道**（read 3 `O-1`：该句混用了两条通道的措辞；本轮两次
      amendment 都靠「没加 bound 就不算 design」这个**文本里没有**的读法过的）。
- [x] 18. `R10` 加：修法为 **design 形状**的 rider，其 redeem-when 必须点名**有资格开轮**的表面
      （read 3 `O-4`：amendment 通道装不下 design 字节，而 deadline 却按「碰没碰这个文件」写）。
- [x] 19. `R10` 加：rider 的 deadline **不得指向创造它的那一轮**；design 形状的搭**下一个可开轮
      的批**（用户选 (iv)+(ii)）。根因 = rider 可在轮中途诞生并当场到期，而唯一能兑付它的
      commit（轮首候选）已经过去。
- [x] 20. rider `tier-file-vs-clause` 按 18/19 的新判据重写 redeem-when（**重定范围非兑付**，
      行不删，比照 `HD-22`/`HD-27`）。
- [x] 21. 建 `HD-36`（`E10` 通道放松：步骤 16+17）与 `HD-37`（`R10` rider 到期判据：步骤 18+19）
      ——**编号是提议，状态只有用户能翻**（`HD-2`）。
- **已裁不做**：#2「amendment commit 声明扫了哪个类 / 哪些站点」——**零实例**（同轮 FULL +
  `E10` must-fix 通道至今未发生过；纯 read 轮无 FULL 故 `E9` 判据下每个改动都是 pre-submission
  correction、零消耗），用户 2026-08-13 裁不做，连 rider 也不记。#5「amendment/re-read 链加计数」
  ——用户选 (a)，靠步骤 16 的扫类间接压短，不加机器（`E6`）。
- **Revert unit**：amendment commit 本身。**电池**：doc-only（先例 `838c413`）。
- **诚实边界**：R5 自己仍受**旧**通道约束——步骤 16 要 R5 落地后才生效，故 R5 若被 read 打回，
  仍只能改点名的那一处，有可能重演 R4 的多读循环。

### Close

- [x] 15. `HD-31` 随 R3 落地同 commit 翻 `§implemented`（`HD-2`——**R1 已在此踩过一次**：
      `HD-25` 的挪节晚了四个 commit，见其条目里记的偏差，R3/R4 别重演）；`HD-27` 留 `§live`
      待拆分批。ledger 批 B 行改 CLOSED + 锚；「未结的用户问题：harness 对外 I/O 边界」整条
      可随之关闭（R1 关掉第一件、R3+R4 关掉第二件）。push debt 现算不写死。

## Acceptance (done = ?)

- 模板的 evidence 脚本经 `run_all` 跑 check，顺序取自 plan 的 `check_order`，且有一条断言测试钉住它。
- 一个含 `SPEC_GAP` 的合成 run 在该 check **之后不再执行任何 check**（mutation 证明该守卫有约束力，
  不是崩溃）。
- 现存 8 个已关闭 run 零改动。
- harness 的仪器代码与 hook 里不再有「往 ledger 写」的路径；`chk-ledger-note` 那道保障有明确承接物
  （或用户明确接受它退化为纪律并记在 `HD-26`）。
- 三条 HD 条目存在且状态正确；rider `PD` 的 redeem-when 指向拆分批。
- **不在本批 acceptance**：任何需要两个仓库存在的东西（`HD-18` 排序）。

## 待用户裁（预览卡上一次问完）——**三问已全裁，本节仅存历史**（① R2 属批 B，且 2026-08-12 扩为
设计-only + R3/R4 ② `tier-scope` ① 补行不开轮，R1 closeout 落 ③ 编号认可；`HD-26`/`HD-27`
后续演化见决策簿）

1. **R2 是不是批 B 的一部分**——本 plan 按「是，排在 R1 之后」写。若你的意思是 ② 整个离开批 B
   单立，说一声，批 B 就只剩 R1 + 记账。
2. **rider `tier-scope` ① 怎么处置**——本批是它的 deadline。改枚举句 = 改规则 = 要开一个小设计轮；
   不改就照六腿跑并把 rider 留着（缺陷仍在：下一个批仍可能按四腿自选而漏跑）。
3. **`HD-25`/`HD-26`/`HD-27` 的编号与措辞**认不认（状态只有你能翻）。

## Resume pointer

当前指针（2026-08-13 收批）: **批 B CLOSED，全部六节收完（R0/R1/R2/R3/R4/R5）**。`E9` 三腿在 R4/R5 两轮全程未花——两轮都用 `E10` 独立 read 而非 FULL。**队首 = 拆分批**（`HD-18`；成员 `HD-28`、调用模型 `HD-33`/`HD-34`；随批 rider `CLI-hist`·`RA`·`PD`），入口 `ResearchSystem/HARNESS-LEDGER.md` backlog。bank 收批时 **28 行**（批 B 净 +5：`E1-suff`/`wspec-owner`/`frozen-path-prefix`/`wl-route` 新增 4、`tier-file-vs-clause` 新增 1，`R10-route` 兑付删 1；`tier-scope` 与 `tier-file-vs-clause` 两次重定范围）。push debt 现算 **645**（`git rev-list --count origin/main..HEAD`，user-gated）。

以下为 R4 的历史指针，保留备查: **R4 CLOSED，队首 = R5**。R4 全链见步骤 13；三次 read 的记录是
`v3-checkpoint-read-{be9878a,0aed595,8884f47}.md`，`E9` 三腿全程未花。R5 的 cold read 已付
（九成员 blob 自 `8884f47` 全 SAME，按 `v3-checkpoint-read-8884f47.md` §1 引用；`§live` blob
`8d2a8799` 未变、十条已读），`E11` 卡经用户批（ok，2026-08-13）。**R5 落地后进 Close（步骤 15）。**
bank 现 27 行——R4 新增四行（`E1-suff` / `tier-file-vs-clause` / `wspec-owner` / `frozen-path-prefix`），
删一行（`R10-route` 兑付）。

以下为 R3 的历史指针，保留备查: **R3 候选已交付（2026-08-12，commit `V3-B-R3-CONSTR-v1`）**，cold read 已重付
（`§live` 实测 12 条——前一稿此处写 13 系误计数，journal §6 对账；九成员 blob 全 SAME，锚
`3f19561` §1）、`E11` 卡经用户批（ok）。施工按 io-design §5 + `HD-31`/`HD-35` 全落：脚本移
`Thesis/Work/Tooling/`、READ_PROMPT+fixture 同步删句、`LedgerCap` 测试删除、
`HARNESS-POLICY.md` 落笔、双指针、README 行减法（`E10` deferral）、`HD-31` 同 commit 翻
`§implemented`。**R3 CLOSED（2026-08-13）**，全链：`c7e0ba0` 候选 → FULL `CHANGES_REQUIRED`
（record `c05f478`：B-1 电池定性 + L-1/L-2/L-3 + O-1/O-2/O-3）→ 修腿 `080621a`（八命令全绿
journal §7）→ VERIFY `REVIEWED_NO_BLOCKER`（record `a4a3bce`；V-1 两处假句随 closeout 按供字节
更正，无预算消耗）。`E9` 三腿已花完。**下一步 = R4 指令层重指轮（新开轮，依据 io-design §8
重指清单 + plan 步骤 13/14）**：每条 amendment 欠独立 read、改规则要求 = 设计开轮（`E10`）、
预算照 `E9` 一轮三腿；开轮时按 `E11` 出卡、重付 cold read（member 2 README 有 `c7e0ba0` 的
deferral 债随该 read 一并清，VERIFY O-3 点名勿当 read-clean）。R4 落地后批 B 进 Close
（步骤 15：ledger「未结的用户问题」整条关闭、`HD-27` 留 `§live` 待拆分批）。
R1 全链：`e9166d2` 构造 → FULL `CHANGES_REQUIRED`（`1025491`）→ bank `0458bfb` → 修腿 `dbbec28`
→ targeted VERIFY `REVIEWED_NO_BLOCKER`（`1986912`）→ closeout。`E9` 预算三腿已用尽，R2 是新一轮。
**R2 开轮前必读**：rider `RA`（已更正为一个产品调用者 + 两处测试调用，其 deadline 就是 R2 开轮）·
FULL `e9166d2` 的 `O-1`（`run_all` docstring 承诺了它的调用者拿不到的东西——R2 若动其签名，
`test_candidate_checks.py:874/887` 是影响面）。cold read 按 `E10` 重付（`§live` 每轮照读）。
新 session 先读 `ResearchSystem/HARNESS-DECISIONS.md` §live，再读本文件，再读两份 R1 评审记录。

## Notes

- **本批不执行任何现存 `§live` 裁决**（`HD-24`/`HD-23`/`HD-10`/`HD-15`/`HD-16` 全属拆分批或 standing
  量尺）。它执行的是 backlog 队首项 + 本 session 三条新裁决。
- **未清 errata（两笔，待用户日后一并裁）**：`2f8c48f` 与 `cbd0b38` 的 commit 标题被污染为
  `@ V3-…-v1` 加正文首尾游离 `@`（PowerShell here-string 泄进 POSIX shell，同错两犯；正文完整，
  `E8` 不许 amend）。教训已定为纪律：**提交一律 `git commit -F <file>`，不再用 here-string**。
- **A1 的失败模式，记在这里防重演**：先测「这东西在我论证里的角色」，后测「这东西本身」。
  本批已踩过一次同形状——rider `PD` 把两件事合并成一条（`E2` 缺守卫 / v3 证据不记 interface 版本），
  分开测之后 `HD-27` 才成立。**任何 R 开轮前先测对象本身。**
