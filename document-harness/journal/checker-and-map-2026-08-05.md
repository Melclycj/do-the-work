# 检查器与两轴映射 — 设计判断与需求（2026-08-05）

> **这是什么。** 一次**跨轮设计判断**的记录，不是轮次叙事。起因：run `p5b-firewall` 收口后，
> 用户按成本追问「执行 8 分钟、其余全是审计与 harness overhead，比例是不是太夸张」，追下去变成
> 两个结构性问题——检查器为什么会成为评审对象，以及"指令→义务"那次翻译的四道守卫是否还有对象。
> 形状照 [`retro-2026-08-03.md`](retro-2026-08-03.md)：实测在前，裁决在后，理由留在这里而不进
> ledger（用户 2026-08-05：「不记讨论过程和 evidence，ledger 不是记这个的」）。
>
> **journal 的定位随本文件扩宽**：从「一轮一份的 construction narrative」扩为「轮次叙事**或**
> 跨轮设计判断」。`document-harness/README.md` 的 journal 行随 A–D 轮一并改。

## 1. 触发的成本读数（run `p5b-firewall`，实测）

| 时段 | 用时 | 内容 |
|---|---|---|
| 23:17–00:11 | 54 min | 读 ledger/契约/schema · 计划卡 · 写工作单与检查器 · 预冻结自检 |
| 00:11–01:23 | 72 min | 三次冻结 · 两轮独立审计（11m49s + 8m14s）· 一批修完 · START |
| 01:23–01:31 | 8 min | 写候选 + 16 项机检 |
| 01:31–01:58 | 27 min | 独立 FULL（24m48s） |
| 01:58–02:35 | 37 min | bind · FINAL · promotion · closeout · 开 issue · 签字 · ledger |

产物 252 行（A3 248 + 契约 1 + plan 3）；运行机器与证据 71 个文件 4,710 行（多为机器生成的 JSON
与模板抄件）；评审与签字记录 196 行。三个 subagent 合计 668,178 tokens。粗分：**约 20% 产品、
80% 机器与返工**。返工里可避免的约 30–40 分钟（三次冻结中的两次源于我起草时未先读代码；evidence
重跑三次；round-2 复审"先否后跑"的冲突暴露太晚）。

## 2. 实测一：这套重机器抓到过什么

三轮同类记录，FULL 的 findings 分布：

| 轮次 | findings | 阻断 | 其中关于**产物** |
|---|---|---|---|
| p5b-firewall | 7 | 0 | 1（OUT 行措辞提醒签字人，非缺陷） |
| p5a-firewall | 2 | 0 | 1（A2 §1 把枚举来源归错文件——真缺陷，轻） |
| p5a-shells | 3 | 0 | 0（三条都在说检查器断言太弱） |

今天唯一真正致命的捕获——firewall 漏掉 `RSC-P4-SCOPE-001` 白名单扩展（漏了则 P5B 每铸一个对象
都是硬报错）——**不是这套机器抓的**：来自上一 session 留在 scratch 的一张笔记，随后由读
`refcheck.py` 代码确认。审计抓到的 O1 是「WorkSpec 没跟上指令」，而 WorkSpec 只因 harness 存在
而存在，其价值是循环的。

## 3. 实测二：绑定检查器有没有提前抓到过错

- 全历史已提交 CheckResult **196 条，100% PASS**——按构造如此：检查红了走不到 commit，所以已提交
  记录对这个问题**天然沉默**。
- 翻 git 全历史 + 各轮 `audit-rounds.md` + 评审记录找「某条 `chk-*` 红了因此抓出候选缺陷」：**零例**。
- 找到的是反向三例，且每次都由人/agent 读出，不是检查器自己发现：
  1. p5a-shells 审计 R5 f1：两条义务绑到了**构造上看不见非 Shell 对象**的检查（`load_shells` 按
     `object_type == Shell` 过滤；无任何检查读 `live_count`）。
  2. run-v2 README 自记：v2 冻结把 `check_shells.py` 冻进去却从未执行，`load_shells` 遇真实索引即
     崩，**直到 FULL 才以 SPEC_GAP 暴露，赔掉整个周期**。
  3. p5a-shells FULL f1：四条脚本可判定的属性实际由 review 扛着；检查器解析一列后丢弃。
- 对照：今天 16 项检查首跑全绿（零捕获），而真正拦下东西的是**常驻库层验证器**——`check_record`
  拒空 locator、`check_spec` 拒超长字段、`build_run` 拒假 BASE。**积累硬化的共享验证器在兑现，
  一次性检查器没有。**
- 诚实边界：无记录 ≠ 未发生。起草期检查红过又被修掉不留痕，无法证明零次；能说的是所有记录里没有
  一次，今天全程在场零次，而三次反例都有记录。

## 4. 结构性诊断：检查器为何必然成为评审对象

`REVIEW.md` 从未写过「重跑检查器」；重跑源自 R2「accept no reported figure，每个数字自己重推」。
真正把检查器拖进评审面的是 **`local_check_and_review` 这个模式本身**：义务的真值有一半由检查器
给出，评审要下 `SUPPORTED` 就**必须**判断那半到底判没判——判检查器不是越界，是下结论的前置条件。
而检查器每轮现写现弃，这块评审面零积累硬化，于是每轮必然产出 findings，且这些 findings 随轮作废。

`EXECUTION.md` 早已预言这个失败模式：*"declaring `local_check_and_review` with a trivial check to
dodge both sentences … is caught, if at all, by review examining what the bound check actually
decides. Treat it as the next witnessed case, not a loophole."* 今天这轮**就是那个 witnessed
case**：10 条义务全绑检查、`review_only` 为 0，随后 FULL 有 4 条发现落在这些检查的断言强度上。

## 5. 实测三：那次「翻译」到底翻译了多少

| run | 指令行数 | R 编号标题 | 单元 | 义务 |
|---|---|---|---|---|
| w1-r1 | 76 | 8 | 9 | 8 |
| p3-corr | 104 | 8 | 10 | 8 |
| p4-bridge | 96 | 5 | 8 | 6 |
| p4-doc | 140 | 8 | 14 | 9 |
| p5a-firewall | 101 | 7 | 10 | 8 |
| p5a-shells | 244 | 10 | 20 | 12 |
| p5b-firewall | 183 | 8 | 11 | 10 |

**七轮全部是编号指令，义务 ≈ R + 0~2**，而多出的 0~2 条永远来自同一处：**规范性前言
（Run conditions）**。抽取步骤近似恒等。

两轴门（paragraph map × unit map）历次结果：p5a-firewall 8 段**零分歧** · p5a-shells **20/20
一致** · p5b-firewall **15/15 一致**。唯一一次分歧（p5a-shells R5 f2）是 paragraph map 自己把附录
标题行标错，处理是翻转它——**发现的是它自己错了，不是漏了义务**。且三次的两张图**都由同一
session 填**，每次都如实声明「不算独立样本」：**机制的独立性前提从未成立**。C4 `O-1` 裁决自订的
改判条件是「分歧恒零**且**独立性成立」——独立性一次未成立、分歧一次未有。

这一带唯一真捕获（w1-r1 前言单元未映射，`issue-w1-r1-unmapped-preamble`）是 **FULL 抓的，不是这
道门**；之后才把前言条款加进授权门。

**作用域声明（用户更正，2026-08-05）**：以上只证明编号态下三件冗余。**散文指令七轮从未跑过**，
故散文态下它们未经检验，不得据此停用。

## 6. 用户裁决（2026-08-05）

> **标签前缀 `SIMP-`**：本轮需求编号与既有 contract amendment 的 A1/A2/A3 撞名（A2=P5A firewall、A3=P5B firewall）。需求一律加 `SIMP-` 前缀，amendment 保持裸名。

**A. 一次性检查器**
- **SIMP-A1 批准** — 取消 `verification_mode` 的 `local_check_and_review`，只留「检查判定」与
  `review_only` 两态。判据（用户批准的修正）：**机器的答案是不是全部答案**，而非「散文 vs 代码」
  ——用户原话「我的说法太简单了」。
- **SIMP-A4 批准** — 保留一条不绑定任何义务真值的 lint，只抓低级错误、省评审时间。
- **SIMP-A5 批准** — `REVIEW.md` 补明文：**检查器不在评审主体内；疑似检查器缺陷是 HarnessIssue，不是
  对候选的 finding**。（今天评审员报 4 条检查器 findings 是尽责——没有任何一句告诉过他不该报。）
- **SIMP-A2 / SIMP-A3 已批（2026-08-05）** — SIMP-A2＝把绑定断言迁入 `rsclib` 常驻层（删掉一次性检查器后，活下来的检查必须有
  地方住；四条里工作量最大，动代码 + 补测试）；SIMP-A3＝首批迁移目标，提议「枚举集 == 冻结集」（今天
  唯一真有价值的检查，且可泛化到 P5C 证据集、P5D 原子清单）。

**B. 派生件的分模式简化**（分支由**指令形态自声明**决定，不按 run 类别——避免二维白名单）
- **SIMP-B1 批准（编号态）** — 件 2（WorkSpec）**保留**，产生方式由「解释散文」降为**机械转录**；
  paragraph-map、授权门、InstructionCoverageAudit **停用**（无对象）。连带：审计 O1 那类发现在恒等
  转录下结构上不可能发生。
- **SIMP-B2 批准（散文态）** — 件 2 照旧派生，三件**全开**。理由是未经检验，不是已证明有用。
- **SIMP-B3 归入 C** — 「判不出形态时朝重失败」与 C2 是同一条规则，合并，避免一条规则两个家。

**C. 指令格式**
- **SIMP-C1** 指令自声明形态（frontmatter `form: enumerated`）。**不采用「让 AI 读一遍判断」**——那是
  一次无 evidence lock 的判断，且把「解释散文」原样搬到更早的位置。
- **SIMP-C2** lint 验证声明为真：**规范内容必须落在编号小节内；编号小节外出现规范语气即不合规**；判不
  出即走散文路径（朝重失败）。
- **SIMP-C3 裁 (b)** — 前言按**拆**处理：本轮特有的规范句升成 **R0**；常驻纪律退回 Context 靠引用
  （run-v2 README 本已要求 standing run-conduct discipline appears by reference）。今天的前言是
  典型：「隔离分支 / FINAL 前不得合入」是常驻纪律，「不激活 `P5B-CLAIMS-v1`」才是本轮特有。
- **SIMP-C4** 编号态下 START 卡呈现编号清单本身，WorkSpec 降为转录件，用户不必读它。

**D. 决策的家**
- **SIMP-D1** journal 定位扩为「轮次叙事**或**跨轮设计判断」，写进 `document-harness/README.md`。
- **SIMP-D2** 本文件即该类别的第一份。
- **SIMP-D3** ledger 只留一行指针，**不进讨论过程与 evidence**。

**落地**
- SIMP-A + SIMP-B **同轮**：两者都要动 `E2` 冻结面（`common.schema.json` 的 `verificationMode`、
  `document-work-spec.v2.schema.json`），同轮只需**一次** recorded user ruling；拆轮要两次。
- 唯一风险：一轮只有**一条修腿**而合并后的面很宽（schema + 模板 + 指令层 + 工具代码）。缓解＝提交
  顺序：**B 的删除在前（便宜、独立），SIMP-A2 的代码迁移在后**。
- 顺序（用户）：**activation → A–D 轮 → P5B 批次**；**F6/F7 两个 HarnessIssue 在 P5C 之前**处理。
- C3 只对该轮之后新写的指令生效，已关闭轮次不追溯。

## 7. 未裁、已记

- （本节此前列的 SIMP-A2 / SIMP-A3 已于同日批准，移入 §6。）
- **A2 amendment（`2026-08-02-a2-p5a-scoped.md`，P5A 的 firewall）的治理索引行已过期**：写着 `signed 2026-08-02 — approved, not yet effective` /
  `effective_at=null`，而 A2 已于 2026-08-02 激活（`6295346`）、P5A 批次已完成并促成
  （`d749406`）。与本轮修掉的 plan 漏账同类：激活更新了记录文件、没更新索引行。属 A2 激活的收尾，
  未擅动。
