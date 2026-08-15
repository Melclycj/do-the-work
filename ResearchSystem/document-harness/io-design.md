# Harness I/O 边界设计 — v1（批 B R2 交付物）

> **这份文件是什么**：批 B R2 的设计交付物——harness 对外 I/O 边界的完整设计（functionality 边界 ·
> 三角色模型 · orchestrator 义务 · 输入/输出面 · 实例文件初始化 · 调用模型）。R3（构造轮）与
> 后续轮按本设计施工。
>
> **这份文件不是什么**（`HD-21` 的提问义务，此处即答案，commit 正文同录）：**不是指令层成员**——
> `E10` 九成员句未点名它；**对现行任何规则无权威**——凡与现行指令层冲突处，以现行指令层为准，
> 改动走各自的设计轮（已知冲突见 §8 待处理清单）。
>
> **签字归属**：用户。签字记录住在 `HARNESS-DECISIONS.md` 的相应条目，**不在本文件**
> （governance-scan 判据：文件不携带自身审批状态）。

## 1. Harness 的 functionality 边界

**核验机**：冻结 subject → 按 WorkSpec 做确定性检查 → 产出证据包 → 走 verdict 路径。

- WorkSpec 双重身份（2026-08-12 更正）：**执行的追溯项** + 评审的靶子。
  一轮 = 拿到 instruction → closeout（评审预算至多三腿，见 `E9`——预算是轮的属性，不是轮的
  终点：FULL 无 blocker 可直接收轮）；拆解 instruction → WorkSpec 在轮内。
- harness **没有、也不该有**：计划、排期、轮次形式（sprint / requirement spec / phase / …）、
  任何外部账本的写入。外部流程的形状从 harness 内部不可预知，强行对接只会放大接缝——
  调用者读一个稳定的出口，自己决定抄进哪儿、抄多少。

## 2. 三角色模型

| 角色 | 职责 | 载体 |
|---|---|---|
| **orchestrator** | 只做传输与 flow 管理：起 executor、派 reviewer、管预算与冻结窗口、与用户交互拿裁决 | 完整 session（主线） |
| **executor** | 拿 instruction、拆 WorkSpec、执行、产出候选 | **必须完整 session**（对 Claude Code setting 依赖最高；`claude -p` 子进程或用户当传输） |
| **reviewer** | 固定 dispatch 冷启动、自行工作、写记录 | **可为 subagent**——standing instructions（review contract）在仓库里，对 setting 依赖最低；前提是 dispatch 由 orchestrator 发（`R1` 的独立性从纪律变结构） |

- 三角色与 `E1`「一个 session 一辈子只持一个角色」**相容**；由二角色（execution / review）扩为
  三角色是本设计的**新增结构**，不是既有规则的兑现。`E1` 现行的 subagent 句（"你派的 subagent
  是自检，不出 verdict"）与「reviewer 可为 subagent」正面相抵——重指见 §8（R4）。
- **绝不把 setting 抄进 prompt**——`HD-5` 判过的同形（转录 = 漂移面）。
- orchestrator **只传输、不裁决**：能自动化的是传输，不是裁决（全局 §3.7：子进程跳过原生审批，
  不得代人类签字）。

## 3. Orchestrator 的 11 条义务

**编排**：① 开轮 cold read（`E10` 九成员 + `§live`）② 起 executor、交付 instruction ③ 派发
reviewer——一个 SHA/range、零 per-acceptance 论证（`E12`）④ 预算三腿记账、绝不自判消耗（`E9`）

**状态**：⑤ 守冻结窗口（`E9`）⑥ 收评审记录并提交（`R6`）⑦ 收批——状态翻转与实现同 commit（`HD-2`）

**用户坎**：⑧ 渲染用户坎的卡并等确认——构造轮预览卡归 `E11`（其首行一句话说清买什么/多久用/
跳过会怎样，是 orchestrator 自己的判断、不是誊抄）；产品 run 的 START 卡是控制面相位
（`user-decision-start.json`），同为用户坎但不归 `E11` 管 ⑨ 按 `R10` 把 FULL 无 blocker 时
每条 low 的**修腿/bank 选择**摆给用户；按 `R5` 把「某物该不该存在」类结论归口用户——两条各管
一个特定形状，不是"每条 finding 均由用户处置"的泛化授权

**对外**：⑩ 按调用者策略文件执行对外动作（§5）⑪ **executor 上报回程**——执行中撞到改变计划的事，
上报 orchestrator → 摆给用户，executor 不得自决。今日仅 `SPEC_GAP` 一种有机器（停机 + 重开
START），一般情形 = 纪律，写进 executor 的派发词。

## 4. 输入面

instruction（形态不变——编号态与 `## Context (non-normative)` 标题两项约定照旧，见
`EXECUTION.md` 的 Instruction form 节；其余输入约定不在本设计范围）→
**executor 拆 WorkSpec**（轮内，追溯项）→
**orchestrator 渲染 START 卡** → 用户批 → 执行。

已知代价（实测确认为**既有**代价，非本设计新增——p5b-claims 的 start 裁决 target 即已带 digest 的
audit ref）：START 驳回则拆解白做。变的只是**谁**拆（executor 而非合并角色），不是**何时**拆。

## 5. 输出面

- **「这轮的结论」= 命令输出**（`HD-32`）。现可当结论出口用的三命令 =
  `status` / `flow` / `disposition`（v3 另有 `governance-scan` / `review` 两个只读命令与
  `dispatch`）；收敛为单一结论命令，随**独立 CLI** 一起做（拆分批）。
- **调用者自定义策略段**：告诉 orchestrator「拿到结论之后干什么」。**归调用者所有、住调用者仓、
  由 orchestrator（session）读，harness 代码绝不执行它**——若 harness 代码执行它，§1 的边界即被
  拆掉。载体 = **调用者独立策略文件**（用户裁 2026-08-12，取代初签版「`CLAUDE.md` 内的一节」——
  实测项目 `CLAUDE.md` 113 行、与 `AGENTS.md` 镜像双写，且其自身 :68 规则要求 push detail down；
  本机 = `ResearchSystem/HARNESS-POLICY.md`，与其所管的 `HARNESS-LEDGER.md` 同列），
  `CLAUDE.md`/`AGENTS.md` 各一行指针保证可发现；**读它即义务⑩本身**，非新增读取义务。
  对本机：写两本账（harness 轨的 `ResearchSystem/HARNESS-LEDGER.md`——120 行上限等收紧参数在此
  声明——与 router `.goals/LEDGER.md`）、link harness 内部状态、长度脚本。
- **ledger 的规则与脚本移出 harness**（R3 构造轮）：`ledger_cap_check.py`（钉着
  `ResearchSystem/HARNESS-LEDGER.md`）是调用者的机器，不是 harness 的。`chk-ledger-note` 类检查
  （住在产品 run 的 control root、锚定 **`.goals/LEDGER.md`** 里一句散文——注意与上一份是两本账）
  随之拆除；「该记的事记了没」的保障**转移给调用者自选机制**（策略段可声明锚点断言，进调用者
  自己的 pre-commit / CI）——从 harness 内确定性检查变为调用者侧自选，此代价已裁
  （`HD-31`，`HD-26` 的收窄后继）。

## 6. 实例文件初始化（新调用者拿到什么）

内容按「**谁的开发**」归属：harness 仓里填满的四件，是 harness 跑在自身的实例；调用者的归调用者。

| 件 | 新库初始 | 规则（仪器半）住哪 |
|---|---|---|
| decision log | **空条目 + 头部同步指令**（状态机四态 / scope 四档 / 准入三问 / 继承 / 删除纪律） | 头部自带 |
| rider bank | **空表 + 头部**（头部指向规则本体，现 `HARNESS-RIDERS.md` 即此结构） | 指令层 `R10` |
| journal | **不预建**——一轮一份，第一轮自然产生 | 指令层（README 表行，`HD-1`/SIMP-D1） |
| ledger | **harness 不提供任何模板** | 调用者策略文件（本机 `ResearchSystem/HARNESS-POLICY.md`） |

产品侧小债有家：**调用者自己的 rider bank**。`HarnessIssue` 的 **kind 枚举**不改——它只收
`HARNESS_DEFECT` / `PROCESS_BURDEN`（仪器问题），这一半本来就对；其**路由与 `observed_after`
窗口**的未解问题仍挂在 rider `HI-route`，不因本设计关闭。

## 7. 调用模型（submodule）

- **submodule**（`HD-15` 的拆分形态在调用侧的兑现，`HD-29`）：调用者仓以 gitlink 钉住 harness
  版本——「用哪个版本的仪器查的」是保障的一部分，gitlink 把它写进每个候选 commit；copy 使其
  不可复现，且分叉无任何可见性。
- **run 目录永远在调用者仓**（可 `.gitignore`）；freeze marker（`.harness/review-pending.json`，
  分支评审窗口锁——与 `E2` 的字节冻结是两回事）归调用者；四件实例文件归调用者。
- **ledger 跨仓指针问题不存在**：每库用自己的 ledger / rider / journal / decision log。
- **调用者纪律**（`HD-29`）：调用者仓内**不得改动/升级 harness 内容**；任何适配**必须记入调用者
  自己的 decision log**。**copy 是逃生口**（submodule × worktree 冲突时），代价 = 版本追溯 +
  漂移可见性；漂移现阶段接受（用户 2026-08-12）。
- 技术遗留：`--repo-root` 默认 `run_dir.parents[3]`（深度假设，
  `assurance/templates/run-v2/run_evidence_v2.py:121`；`rsc.py` 的同名参数默认 cwd，两者不同），
  跨仓显式传；**独立 CLI**——今日 v3 只是产品 CLI `rsc.py` 的子命令组，六个命令中五个纯读、
  `dispatch` 唯一写盘（只写调用者 `.harness/` 下的 freeze marker），「跑这一轮」住在 run 目录
  脚本里——归拆分批，与 rider `CLI-hist` 同批。

## 8. 待处理清单（本设计产生的后续工作）

| 事项 | 归处 |
|---|---|
| 拆四处 ledger 耦合 + ledger 规则/脚本移出 harness 树 + 本机策略文件落笔（`ResearchSystem/HARNESS-POLICY.md` + `CLAUDE.md`/`AGENTS.md` 各一行指针，镜像同 commit 双写） | **R3 构造轮**（用户已裁其必为构造轮） |
| 指令层重指轮：`R1`/`R6`/`R10` 的「executor / execution side」称谓按三角色重指（`E9` 无此称谓，原文点错对象，R2 转录核查 finding 6 更正）+ `E1` subagent 句（与 reviewer-可-subagent 相抵）+「Execution side」节头作用域句 + `R10` "never here" 重新指向 + WorkSpec 入轮内的流程文本 | **R4（批 B 新增设计轮，用户 2026-08-12 裁）** |
| `HD-16` B 组收窄 | **`HD-28` 已建**（2026-08-12 按 `HD-30` 机制重写为完整后继，`HD-16` superseded） |
| 独立 CLI + `rsc.py` 归属 | 拆分批（rider `CLI-hist`） |
| `E`（topology claim 形状）删除 | 本 commit 已执行（用户裁 2026-08-12：源头追不到，按其自带处置删） |
| orchestrator 载体自动化（`claude -p` 起 executor 等） | 后话；先维持用户当传输 |
