# HARNESS DECISIONS — archive（只装死条目）

> 从 [HARNESS-DECISIONS.md](HARNESS-DECISIONS.md) 移入的 `superseded` 与 `retired` 条目，
> 原文照搬、不改写。不在任何必读范围内，grep 可达。本文件**超过 100 行**时询问用户一次
> 要不要清（删除双条件合取 + 默认不删 + superseded 链永不可删，见主文件头部 HD-6）。
>
> **`HD-6` 的询问第二次已付：2026-08-14（`HD-24` 移入、128 行），用户未答；按 `HD-6` 的
> 「默认不删」执行——不清。下次触发点仍是下一次有条目移入本档时。**
> **第一次：2026-08-13（104 行触发），用户裁「不清」。** 判据实测：
> 七条全部仍被外部援引（`HD-11` 46 · `HD-14` 42 · `HD-16` 40 · `HD-12` 33 · `HD-17` 22 ·
> `HD-13` 17 · `HD-26` 16 · `HD-29` 8 处，`grep` 排除本文件自身），故删除的第一个条件
> 「今后不会再被援引」对每一条都不成立；其中三条 superseded（`HD-16`→`HD-28` · `HD-26`→`HD-31` ·
> `HD-29`→`HD-33`/`HD-34`）另受「链永不可删」保护。下次询问的触发点是**下一次有条目移入本档时**。

### HD-24 · AMBIG 七树归属已裁：v2 连通件 + 两记录树 travel，stages/ 随 v1 族归拆分批（`HD-17` 的兑付）
- 2026-08-09 · user · scope: standing · status: **superseded**（2026-08-14 由 `HD-39` 取代——
  按 `HD-30` 机制：七树处置由 travel 收窄为**删除**，全文由 `HD-39` 承接并补上其未 scope 的
  v1 运行时族；原文以下照搬不改写）
- 裁决：R0.1 存活审计呈表后逐项裁定——① `ResearchSystem/harness/` ② `tooling/rsclib/harness/`
  ③ `tooling/tests/harness/` ④ `schema/harness-v2/` 是一个连通 live 件，连同
  `contract/General-Harness-Contract-v2.md`（39 测试运行时读其字节）**整体 travel**；
  ⑤ `migration/general-harness-v2/` ⑥ `migration/stage-control-refactor/` 按「记录跟着被记录的
  对象走」属**造仪器的记录**（非 harness 在产品上跑出的保障记录），**travel**；⑦ `stages/`
  **处置归拆分批、与 v1 stage-control 族同批**——4 条真 markdown 链接钉着它（含已签
  `Stage-Control-Contract.md:23`），单删即 repo-audit 硬失败，「直接删」不存在。
- 后果：travel 集在 `HD-16` 的 A+B+C 之外新增本批成员；执行全落拆分批（搬 ② 必同批剪
  `rsc.py:50`/`:739`，即 rider `CLI-hist` 的一半）；`rsc.py` 归属维持缓裁。① 的字节级身份
  （5 profile 为域中立工作形态原型、4 adapter 全 `declared` 从未实现、issue registry 空、
  区域 UNSIGNED CANDIDATE 从未签署）与全部测量在 basis。
- basis: [journal/batch-a2-2026-08-09.md](document-harness/journal/batch-a2-2026-08-09.md) §2–§7 ·
  用户裁决 2026-08-09

### HD-16 · 新仓成员 = A+B+C；已关闭 run 与 shadow 留在产品仓（批 A `D6`）
- 2026-08-08 · user · scope: standing · status: **superseded**（2026-08-12 由 `HD-28` 取代——
  按 `HD-30` 机制：B 组成员定义收窄（ledger 两份留调用者仓），其余半边原文由 `HD-28` 全文承接）
- 裁决：新 harness 仓只带 **A 仪器 + B 治理账本 + C 评审记录**（242 files / 57,273 行 / 向外引用
  152 处）；**D 已关闭 run 的产物与 E shadow 留在产品仓**。
- 后果：**记录跟着被记录的对象走，不跟仪器走**——run 是 harness 关于*这个*产品的记录，换个产品即
  不适用。接受的代价：两边各持一半历史；harness 的历史产出住在产品仓。避开的代价：新仓不再背
  2,241 条指向对面仓库的只读路径（占全带方案外引用的 94%）。
- basis: journal §13.4

### HD-26 · ledger 解耦：仪器只输出、不写入；形状 defer 到 I/O design（批 B ②）
- 2026-08-11 · user · scope: standing · status: **superseded**（2026-08-12 由 `HD-31` 取代——
  按 `HD-30` 机制：硬约束半边收窄（承接物移调用者侧自选），只输出不写入 + citation 作废两半边
  由 `HD-31` 全文承接）
- 裁决：harness **不负责往 ledger 写**，只负责输出；ledger 的写入格式是 global 的，不该被仪器绑住。
  具体输出契约 **defer 到 I/O design**（批 B R2，前置 = R1 落地）。**并附**：backlog 里
  「citation 规则因此暂留层外」一句作废——全仓查无承载（`citation` 一词被产品概念 `citation-key`
  占满），用户裁定删除而非补写。
- 后果：现测四处耦合，两读两写——读 = `tooling/hooks/ledger_cap_check.py`（硬编码 ledger 路径 +
  `MAX_LINES`）· `dispatch.py:636` 层 read 提示词；写 = run 的 `write_scope` 直接列 ledger 路径
  （p3-corr / p4-bridge / p4-doc）· `chk-ledger-note`（p4-bridge 的 `locator_exists`，锚点是 ledger
  里一句人手写的散文）。**硬约束**：`chk-ledger-note` 一拆，harness 就再没有手段验证「这轮该记的事
  真记下来了」，该保障退化为纪律——输出契约必须有承接物，否则是净损失。
- basis: 本批 journal batch-b-2026-08-11.md §2 · 用户裁决 2026-08-11

### HD-29 · 调用模型：submodule 钉版 + 调用者仓零升级 + 适配必须留痕
- 2026-08-12 · user · scope: standing · status: **superseded**（2026-08-12 拆分为 `HD-33`
  （调用模型 + 归属）与 `HD-34`（调用者纪律 + 逃生口）——颗粒度修正（一条 = 一件能被独立推翻
  的事，R2 转录核查 finding 21），两后继共同取代）
- 裁决：调用模型 = **submodule**（`HD-15` 拆分形态在调用侧的兑现）：调用者仓以 gitlink 钉住
  harness 版本，run 目录（可 gitignore）、freeze marker、四件实例文件全归调用者仓；**调用者仓内
  不得改动/升级 harness 内容，任何适配必须记入调用者自己的 decision log**；**copy 仅为逃生口**
  （submodule × worktree 冲突时），代价 = 版本追溯 + 漂移可见性，漂移现阶段接受。
- 后果：升级 = 显式的 gitlink 指针变更 commit，历史可读；「用哪个版本的仪器查的」由候选 commit
  自带（copy 守不住的那条线）。ledger 跨仓指针问题不存在——每库用自己的四件。
- basis: journal §5（submodule vs copy 决定线 + freeze marker 身份）· io-design.md §7 ·
  用户裁决 2026-08-12

### HD-17 · `AMBIG` 138 件本轮不裁，A2 前先查存活（批 A）
- 2026-08-08 · user · scope: batch:A · status: **retired**（2026-08-09 消耗完毕：R0.1 存活审计
  已付，七项归属由 `HD-24` 裁定；与 `HD-24` 立条同 commit 移入本 archive）
- 裁决：v2 harness 遗留（`ResearchSystem/harness/` · `tooling/rsclib/harness/` ·
  `tooling/tests/harness/` · `schema/harness-v2/` · `migration/general-harness-v2/` ·
  `migration/stage-control-refactor/` · `stages/`）与 `tooling/rsc.py` 的归属**本轮不裁**；
  A2 开工前先查它们是否还有活消费者，**避免把死件搬进新仓**。
- basis: journal §13.5

### HD-11 · 模板脚本改「共享核 + per-run 增量」（批 A `D1`）
- 2026-08-08 · user · scope: batch:A · status: **retired**（2026-08-10 batch:A 随 A2 收批到期，
  用户批准；细则由 carrier 继续在力不受影响。曾 implemented（2026-08-09，R2+R3 两轮承载：R2
  参数化 `7e8f920`→修腿 `3b6267c`→VERIFY 无 blocker；R3 共享核定形 `cef6138`→FULL
  `CHANGES_REQUIRED`→修腿 `638972f`→VERIFY 无 blocker（`v3-review-verify-638972f.md`）。
  carrier = run-v2 README 实例化节 + 三步骤脚本 docstring 同向 + 五套模板测试自模板路径驱动
  （102 条）——散文承载、无机械 enforcement：run 抄模板不被任何 gate 拒绝（rider
  `delta-prose`）；「零抄件」限步骤脚本，comparator 仍按 `EXECUTION.md` 规则抄于 instruction 旁
  （VERIFY `V-1` 的限定）））
- 裁决：run 不再各自携带模板脚本抄件，改为共享核 + per-run 增量。
- 后果：A2 最大项。**必须先把「改文件填 CONFIG 块」换成「读配置 + 传参」**（三份脚本 `__file__`
  派生 control/evidence 根、四份靠填 CONFIG）。可共享面实测 ≈883 行/run。
- basis: journal §2 · §3

### HD-12 · CheckResult 关闭后删，只留一手输出，只管今后的 run（批 A `D2`）
- 2026-08-08 · user · scope: batch:A · status: **retired**（2026-08-10 batch:A 随 A2 收批到期，
  用户批准；细则由 carrier 继续在力。曾 implemented（2026-08-10，R4 承载：构造 `ed37a25`→FULL
  `CHANGES_REQUIRED`→修腿 `de8f4ef`→VERIFY 无 blocker（`v3-review-verify-de8f4ef.md`）。
  carrier = 模板第六共享脚本 `run_retire.py`（落地名 run_closeout.py，修腿改名——该名已是
  p4-doc/p4-bridge run-own post-run issue step 之名，FULL `B-1`）+ `review_subject.py` 的
  CLOSED carve-out（缺席合法、在场照验，注释 amend 载裁决）+ retire 套件 12 测试与 review 套件
  2 测试 + README retirement 句。删除范围按用户 D-a/D-b（2026-08-09）：只删 `check_order` 派生
  的逐份文件，聚合件与 `<check_id>.out.txt` 留，`check_result_refs` 原样——digest 对 evidence
  commit 历史永远可验。诚实边界：无 gate 强制 retirement 被执行（脚本自述 enforces nothing；
  `B-1` 失败路径靠改名消歧、非机器）；carve-out 钥匙是 run 自写 status（rider `status-key`）））
- 裁决：run **关闭后**删除逐份 CheckResult，只留一手输出；**只对今后的 run 生效**，已关闭的八个 run
  不追溯（守计划书 Constraints 的 closed-runs 只读）。
- 后果：A2 的 T2。**裁定时已知并接受的代价**：一手输出 20 份里 3 份 0 字节、10 份 11–23 字节，删后
  无法再从字节证明当时过没过；`check_result_refs` 的 digest 目标消失，closeout 需处置；新旧两套形态
  共存，`review_subject.py` 的完整性检查要能分辨。
- basis: journal §4.1 · §11.1 · §12.1

### HD-13 · 评审记录形态不变（批 A `D3`）
- 2026-08-08 · user · scope: batch:A · status: **retired**（2026-08-10 batch:A 随 A2 收批到期，
  用户批准；do-not 无承载物，批终即耗尽——A2 全程未就记录形态开轮，裁决兑现）
- 裁决：评审记录不动，T3 离开 A2 范围；不再就「记录要不要展示重推」开轮。
- 后果：实测支持——53 份里 50 份被引共 169 次，最硬的一类（16 次代码/测试 docstring）引的正是判断；
  且 66% 配方行不带把手，改「引用+重放」是加工作量而非减。
- basis: journal §10 · §12.2

### HD-14 · run-v2 README 的六节规则搬入 `EXECUTION.md`（批 A `D7`）
- 2026-08-08 · user · scope: batch:A · status: **retired**（2026-08-10 batch:A 随 A2 收批到期，
  用户批准；细则由 carrier 继续在力。曾 implemented（2026-08-09，`EXECUTION.md` 六节承载：搬移
  `418b89c` + 修腿 `fbcb035`；FULL `v3-review-full-418b89c.md` 与 VERIFY
  `v3-review-verify-fbcb035.md` 均 `REVIEWED_NO_BLOCKER`，R1 收轮；实际落点 404 行，非预估 350））
- 裁决：`templates/run-v2/README.md` 的六节规则移入已受 `E10` 保护的 `EXECUTION.md`，README 只留
  「怎么实例化这个模板」。
- 后果：搬迁本身是指令层 amendment，**开轮**。`EXECUTION.md` 171 → 约 350 行，成为层内最大文件。
  A2 要答的结构问题：`Instruction form` 与 `Authoring gate` 是起草期规则，而 `EXECUTION.md` 是
  执行者役职指令，读者是否同一。（答案落 R1 预览与 stage marker：多读者一文件，标注惯例既有。）
- basis: journal §11.3 · §12.4

### HD-43 · 拆分批 R1 的 `E9` 超腿：一次性追认，不改 `E9`、不立通则
- 2026-08-15 · user · scope: one-shot · status: **retired**（本条即裁即成立，无待执行动作；
  R4 收批时议转 `implemented`。**编号与状态只有用户能翻**，`HD-2`）
- 裁决：R1 走满五腿而 `E9` 上限为三，用户裁定**一次性追认**第四、第五腿（fix `100e2dd` +
  VERIFY `caf633c`），**不修改 `E9` 的三腿上限、不建立「超了再补批」的通则**。
- 判据（实测，非断言）：`E9` 原文「Budget per round: one FULL, at most one user-approved fix,
  one targeted VERIFY」把 FULL 与 VERIFY 一并计入，故 FULL `0792a89`（1）→ fix `22264b5`（2）
  → VERIFY `dd7a27c`（3）即已用满；`io-design.md:19` 同义（「评审预算至多三腿、预算是轮的
  属性」）。超腿的**内容**经 VERIFY `caf633c` 独立复算全部成立（travel 集 259 机械复现、
  260 blob 中 259 个跨仓逐字节相同、新仓套件 24/677→20/681 在校验过的 clone 里复现），故追认
  的是**预算**不是质量。
- 后果 / 诚实边界：**用户批准第二条修腿（「甲 + 花」）时拿到的账目是错的**——executor 报的是
  「三腿花了两腿」，那是只把 fix 计入腿数的读法，`E9` 文本不支持（VERIFY `100e2dd` 的 `F-1`）。
  退役 operating contract 写死「预算分类是用户的，executor 只 propose the accounting，绝不
  自行分类哪一轮消耗了什么」——本条追认的正是一次**在错账上做出的批准**，故记此边界而非略过。
  更正落 `030a999`。**本条不豁免任何未来轮次**：下一轮超腿仍须当场停下并重新取得裁决。
- basis: 用户裁决 2026-08-15（对话）· `v3-review-verify-100e2dd.md` `F-1` + 其自开自闭的
  `SPEC_GAP` 段 · `document-harness/CONSTRUCTION-CHECKLIST.md` `E9`
- retired 2026-08-15（用户裁）：执行完毕，无后继。

### HD-42 · 全电池枚举随删除由八条改六条：只此一次、只这两条、与删除同 commit
- 2026-08-15 · user · scope: one-shot（R1 执行即 retire）· status: **retired**（待 R1 执行）
- 裁决：`HD-39` 的删除使 `EXECUTION.md` 全电池枚举中的两条指向不存在的文件——
  `ResearchSystem/tooling/tests/harness/run_tests.py` 与
  `ResearchSystem/tooling/tests/stage_control/run_tests.py`。用户裁定**把枚举由「八条」改为
  「六条」并删去这两项，不算 `E10` 意义上的规则变更、不开设计轮**。**四重收窄，缺一不可**：
  ① **只此一次**（不建立「主体消失即可改枚举」的通则）② **只这两条**（其余六条一字不动，
  `nothing fewer` 子句保留）③ **与删除同一个 commit 落地**（不得先删文件后补规则，也不得反过来）
  ④ **该 commit 正文点名**本裁决与被删的两条。
- 判据（实测，非断言）：两个 runner 是 `unittest` 独立脚本，**pytest 收不到**——`python -m pytest -q
  --collect-only`（量程 = 从 `ResearchSystem/tooling` 跑）收 **701** 个测试，其中来自这两个文件的
  **0**；正因如此当年才把它们单列，防静默跳过。二者的 import 面**全部落在删除集内**
  （`rsclib.harness.*` 十个模块 / `rsclib.{stage_close,stage_control}`），**59 个测试
  （39 + 20）无一测到删除后仍存活的东西**。故删除零覆盖损失，留着则是两条指向空气的强制命令。
- 后果：`E10` 的 design test **无**「枚举主体消失不算改规则」这一例外，故本条是**用户当场造的一个
  例外**，形状比照 `E2` 的「只为该文件、只此一次」松冻结（`O-2b`）。**未豁免的**：该编辑仍是对
  `E10` 成员 `EXECUTION.md` 的写入，按 `E10` **仍欠该层的一次独立 read**（riding the next read of
  this layer at per-member digest cost）——本条只免「开设计轮」，不免读。
  **同批须核**：rider `tier-scope` ② 的 redeem-when 点名的是 tiering **节头**，而本次编辑落在节内
  的枚举句，严格论不触发；R1 应主动核一次而非等它咬人。**承载点三处**（扫类实测，量程 = 全仓
  tracked `*.md`/`*.py`，排除评审记录与 archive）：`EXECUTION.md:329` · plan 步骤 13 · plan
  Acceptance；另五处「八条」属别的主题（`HD-25` 八条守卫 / digest-narrowing 八条探针 / 批 B
  第八条测试），不动。**无测试或代码钉住该枚举**。
- basis: 用户裁决 2026-08-15（对话）· `v3-checkpoint-read-a654fb2.md` `M-1` ·
  executor 复现（pytest collect 701/0 · import 面 · 39+20 测试数）
- retired 2026-08-15（用户裁）：执行完毕，无后继。

### HD-39 · v1/v2 全族**删除**（`HD-24` 的收窄后继）：七树不 travel，连 v1 运行时族一并删
- 2026-08-14 · user · scope: standing · status: **retired**（待拆分批 R1 执行；**编号是提议，
  状态只有用户能翻**（`HD-2`）。按 `HD-30` 机制承载 `HD-24` 收窄后的**全文**，`HD-24` 同 commit
  转 `superseded` 入 archive，双向指针）
- 裁决：`HD-24` 逐项裁定的七树**全部改为删除、不 travel**——① `ResearchSystem/harness/` ②
  `tooling/rsclib/harness/` ③ `tooling/tests/harness/` ④ `schema/harness-v2/` 及
  `contract/General-Harness-Contract-v2.md` ⑤ `migration/general-harness-v2/` ⑥
  `migration/stage-control-refactor/` ⑦ `stages/`（其「处置归拆分批」于本条兑现）；
  连同 `HD-24` **未 scope 到的 v1 运行时族**：`contract/Stage-Control-Contract.md` ·
  `rsclib/stage_control.py` · `rsclib/stage_close.py` · `schema/stage-record.schema.json` ·
  `schema/review-result.schema.json` · `schema/closure-receipt.schema.json` ·
  `schema/stage-control-fixtures/`（24）· `tooling/tests/stage_control/`（2）·
  `.claude/commands/rs-execute.md`。**合计 171 文件**（`HD-24` 时点报的 139 只覆盖前七树）。
- 判据：`HD-9` 三砍之**「无锁证词」**——无任何决定依赖这批字节。事实基础：A2 存活审计定性
  「注册在案、从未行使」（零份 Stage Record 曾存在），用户 2026-08-14 补充 v1 实际存活约半小时
  即被 v2 推翻、v2 未活过一天。`E2` **不挡**：其冻结清单穷举（v3 契约 `b2dbdf75` + 两份
  supersession + 15 个 schema 文件），两份待删契约均在清单外，规则原文「a path outside them is
  not frozen by this rule」——删除是普通用户裁决，不是动冻结面。
- 后果：travel 集不再含这七树，新仓不带从未行使的字节出门。**连带清单（R0 read `M-1` 更正后）**：
  ① `rsc.py:48`/`:50` 两条 import（rider `CLI-hist` 照旧兑付）**外加 `rsc.py:850`**——
  `except stage_control.StageControlFault` 在 `main()` 里包着 `args.func(args)`，是所有命令
  （含六个 v3 命令）的共用错误出口；只剪 import 不动它，会把每个命令的意外失败路径从
  `FATAL: …`/exit 2 变成未捕获的 `NameError`（re-read `M-1`；处置方式归 R1/R2 的设计判断）· ② **删除集之外有 4 个文件、
  **14 条引用**（13 markdown 链接 + **1 wikilink**）指进删除集，全部进 R1 改动边界**（**「3 个文件」是加入 wikilink 那一处时漏改的残数，R1 更正为 4——`split-design.md` §7 表与 plan 步骤 12/Acceptance 一直是 4**）——`ResearchSystem/README.md`（8）·
  `.goals/plans/general-harness-v2-architecture-revision.plan.md`（3，`:723-725`）·
  `.goals/plans/research-system-stage-control-refactor.plan.md`（2，`:323`/`:324`）·
  **`.goals/plans/document-work-assurance-harness-v3.plan.md`（1 条 wikilink，`:41`，目标 stem
  `General-Harness-Contract-v2`；**不原样引用**——wikilink 扫描无 inline-code 豁免，照抄即自造断链——`repo-audit` 的 wikilink 是与 markdown-link 并列的另一道
  硬检查 `:306`，按 stem 解析、不受 inline-code 豁免，故修完 13 条 markdown 仍 exit 1；re-read `M-2`）**；逐条见
  `split-design.md` §7 表。**本条初稿只点了「指向 `stages/` 的 4 条」（其一自删），即预算 3 条而
  实存 13 条**；`repo-audit` 的链接检查 resolve 任意目标路径、一条断链即 exit 1，故按初稿执行会
  撞上 `HD-24` 当初用来说「直接删」不存在的那个失败形态。③ 已关闭 run
  `p5b-firewall/build_run.py:216-217` 把两契约列在**边界排除表**（纯字符串、不读字节，不影响该
  run 既有证据）。rider `SCC` 随其 subject 删除而在 R1 **retire**；rider `PD`
  提到的「两处活调用是 v2 `schemas.pack_digests()`」随 ② 消失，其 v3 半边（删零调用函数）不变。
  **诚实边界**：⑤⑥ 是**记录**不是仪器（`HD-9` 三留之「证据」），删除它们在 tip 上移除 v2 的构造
  与评审轨迹；缓解事实 = 调用者仓保留全部 git 历史（本批新仓从头、不保历史，故历史只在调用者仓，
  `git show` 仍可达）。**已验并更正**：三个 v1 schema 的**字节读者**仅在 v1 族自身内、v3 零命中
  （本条初稿把这个 grep 结果写成了「全仓读者」，而 `ResearchSystem/README.md:43-45` 正链接着它们
  ——字节读者 ≠ 引用者，R0 read `M-1`）。
- basis: 用户裁决 2026-08-14（对话）· [journal/repo-split-r0-2026-08-13.md](document-harness/journal/repo-split-r0-2026-08-13.md) §7 ·
  `document-harness/split-design.md` §7/§10.2 · supersedes `HD-24`
- retired 2026-08-15（用户裁）：执行完毕，无后继。

### HD-27 · `E2` 不加守卫：`pack_digests()` 不接、路径判据也不加；重开条件 = 拆分批（批 B ③）
- 2026-08-11 · user · scope: standing · status: **retired**（"不加守卫"是 standing do-not，
  rider `PD` 只承载 `pack_digests` 那半边，`E2` 通用守卫这半边无别家）
- 裁决：**不**把 `pack_digests()`（`__init__.py:238`）接成 `E2` 的机械挂点，**也不**另加路径判据守卫；
  `E2` 维持纯散文规则 + 纪律。**重开条件 = 拆分批**（三条理由届时同时变形）。
- 后果：rider `PD` 的 redeem-when 由「I/O design 批一起议」重定为拆分批（比照 `HD-22`，重定范围
  非兑付，**行不删**）。同批分开的两件事：`pack_digests` 零调用**不是** `E2` 缺守卫的症状，而是
  **v3 证据从不记自己由哪个 interface 版本产出**（v2 的 `resolver.py:272` 记在 `bindings`，v3 全仓
  零命中）——后者与 `E2` 无关，随重开条件一并再议。
- basis: 本批 journal §3（三条实测：产品 run 的 `_check_git_diff_boundary` 已把 `schema`/契约列进
  `boundary.out`；构造批每轮独立评审且 boundary 检查点名 frozen surface；`HD-16` 使"证据离仓自证"
  价值落空）· `E6` · 用户裁决 2026-08-11
- retired 2026-08-15（用户裁）：执行完毕，无后继。

### HD-28 · 新仓成员（`HD-16` 的收窄后继）：A 仪器 + B=decisions/riders+decisions-archive + C 评审记录；ledger 留调用者
- 2026-08-12 · user · scope: standing · status: **superseded**（→ `HD-49`，2026-08-19 同 commit 迁入本档）（成员集已由
  `document-harness/split-travel-manifest.md` 承载并于 R1 搬迁完毕，拆分批 R3 2026-08-17 转；
  本条 2026-08-12 按 `HD-30` 机制由差量式收窄注重写为 `HD-16` 的**完整后继**，`HD-16` 同 commit
  转 superseded 入 archive，双向指针）
- 裁决：新 harness 仓带 **A 仪器 + B 治理登记（`HARNESS-DECISIONS.md` · `HARNESS-RIDERS.md` ·
  `HARNESS-DECISIONS-archive.md`，3 files——riders 无 archive）+ C 评审记录**；
  **`HARNESS-LEDGER.md` 与 `HARNESS-LEDGER-archive.md` 留调用者仓**；**D 已关闭 run 的产物与
  E shadow 留产品仓**（此半边承 `HD-16` 原文不变）。
- 判据：实例内容按「**谁的开发**」归属——harness 仓里填满的四件（decision log / rider bank /
  journal / ledger）是 harness 跑在自身的实例，调用者的归调用者；四件中唯 ledger 连**规则**都
  不归 harness（global 约定的收紧方言，harness 只占三个参数），故其实例随调用者。
- 后果：记录跟着被记录的对象走，不跟仪器走（承 `HD-16`）；A1 §13.4 的「B 治理账本 5 files」
  重算为 3。
- basis: [journal/batch-b-2026-08-11.md](document-harness/journal/batch-b-2026-08-11.md) §5 ·
  `document-harness/io-design.md` §6/§7 · 用户裁决 2026-08-12 · supersedes `HD-16`

### HD-48 · 下一个设计轮 = 三题打包（`layer-crossrepo-token` · `e1-disclose-home` · `dtw init` 写哪儿）
- 2026-08-19 · user · scope: batch:next-design · status: **superseded**（→ `HD-50`，2026-08-19 同 commit 迁入本档；其三题两题并入批 DTW-INDEPENDENCE R2、一题并入 R4）（排期裁决，执行完 retire；除本条外只活在对话里）
- 裁决：`CALLER-ONBOARDING` 收批后的**下一个队首是一个设计轮**，收三题：① rider `layer-crossrepo-token`
  （deadline 已于本轮到达——guard 接进仪器仓那一刻；今天不咬人只因它只扫新增行）② rider
  `e1-disclose-home`（deadline 亦于本轮到达：`E1` 的四持有披露句无载体、无责任人，本轮两次披露都只写在
  commit 正文里，属自定而非规则要求）③ `dtw init` 的两个实例文件写在 target 根固定文件名，要不要加
  `--into` 或改默认（`HD-33`/`HD-34`/io-design 均未定位置）。三题的修法都是 design 形状——加 clause 或
  加 bound——故 `E10` 要求开轮，不得搭任何 amendment 的车。
- **未选中的一题继续 bank**：仪器仓要不要也跑 `review_freeze_check` / `candidate_path_check`
  （它对自己的构造轮也是调用者、也真持有冻结窗口，而 `E9` 那道窗口在该仓目前零机械执行）。用户
  2026-08-19 裁不进本批；rider 见 `self-caller-guards`。
- basis: 用户裁决 2026-08-19（对话，四选多）· FULL `v3-review-full-2026a14.md` 与 VERIFY
  `v3-review-verify-4029b43.md` `O-1` 各记一条到期未付 · `HD-37` ②（design 形状的 rider 只点名有资格开轮的表面）
