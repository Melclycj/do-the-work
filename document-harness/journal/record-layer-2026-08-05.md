# 记录层重设计 — 问题陈述与底账（2026-08-05）

> **这是什么。** 一次**跨轮设计判断**的开题，不是轮次叙事，也不是方案。起因：用户 2026-08-05 在
> `SIMP-ABCD` 收口后指出——`SIMP-D`（决策的家）那一项开得太小，「要做的不只是决定 decision 记录在
> 哪里，整套 harness 的记录也需要重新设计，现在 harness 存的 evidence 太多了，是真正产出的 10 倍
> 左右」。本文件只做两件事：**把底账量出来**，**把该问的问题列清**。任何改动都要另开轮。
>
> 形状照 [`checker-and-map-2026-08-05.md`](checker-and-map-2026-08-05.md)：实测在前，判断在后。

## 1. 底账（实测，2026-08-05）

```
$ python -X utf8  # 逐文件读字节数行，排除 __pycache__
runs/ 全部        : 450 文件 / 26,973 行
runs/p5b-firewall : 71 文件 / 4,710 行
migration v3-*.md : 80 文件 / 19,347 行      ← 评审与 read 记录
document-harness  : 13 文件 / 2,377 行       ← 指令层 + journal
```

**用户口径「10 倍」是低估。** 以最近一轮产品 run 为准：产物 **252 行**（A3 amendment 248 + 契约索引
行 1 + plan 3），运行机器与证据 **4,710 行** → **≈18.7 : 1**。把评审与签字记录（196 行）算进去是
**≈19.5 : 1**。

> **测量更正**：先前一次用 `find … -exec wc -l {} + | tail -1` 取总数，Windows 上参数表被分批，
> `tail -1` 只拿到最后一批的小计（450 文件报成 5,281 行）。上表是逐文件累加的重测值；
> `runs/p5b-firewall` 的 4,710 与 `checker-and-map-2026-08-05.md` §1 独立记录的数字一致，可互证。

## 2. 钱花在哪（p5b-firewall 一轮 71 文件的分解）

| 份额 | 行 | 是什么 | 可再生性 |
|---|---|---|---|
| **52%** | 2,460 | **run 根目录下的 9 个脚本** — `build_run.py` 617 · `check_a3.py` 595 · `run_evidence_v2.py` 325 · `run_bind_v2.py` 282 · `check_template_instance.py` 210 · `run_final.py` 139 · `run_start.py` 129 · `write_audit.py` 89 · `make_paragraph_map.py` 74 | 其中 **5 份是模板抄件**（run-v2 README 明写 "Instantiate by copying into `runs/<run-id>/`"），1 份是 w1-r1 沿用；只有 `build_run.py` 与一次性检查器 `check_a3.py` 是本 run 特有 |
| **19%** | 914 | `evidence/check-*.json` — 一个检查一份 CheckResult | 机器生成；输入是 `chk-*.out.txt` + check spec + 候选 SHA |
| **11%** | 522 | `coverage.json` 239 · `review-full.json` 182 · `candidate-record.json` 181（合 602，去重后计） | 机器生成或评审员产出 |
| **6%** | 283 | `evidence/chk-*.out.txt` — 命令真实输出 | **不可再生**，是唯一的一手证据 |
| 5% | 242 | `control/audit-rounds.md` 127 · `paragraph-map.json` 115 | 人写 / 半机器 |
| <1% | 24 | `control/` 下 24 份 canonical JSON（多为单行）+ `issues/` | 指针与规格 |

**一句话诊断**：真正不可再生的一手证据只占 **6%**；一半以上的体量是**每个 run 复制一整套脚本**，
外加**一次性检查器**——后者的模式本轮刚被删掉（`SIMP-A1`/`A2`），但**文件仍然一 run 一份地留着**。

## 3. 判据（继承本轮，用于任何后续设计）

一件记录留下来的理由必须是「**某个决定会因为它不在而不同**」，不是「以后可能有人想看」。这与
`E6` 同源（*ask what decision changes if it is absent*），也是本轮删 `local_check_and_review` 用的
同一把尺。派生：**能从已提交字节确定性重算的东西，存的是方便，不是证据。**

## 4. 范围

- **在范围**：产品 run 的 `control/` 与 `evidence/` 布局与粒度 · 模板实例化方式（复制 vs 引用）·
  CheckResult 一检查一文件的粒度 · 评审记录的体量（80 份 19,347 行）· read 记录 · `SIMP-D` 的
  decision 归属（journal / ledger / commit 三者分工，本轮已定的部分不重开）。
- **不在范围**（除非另裁）：`E2` 冻结面 · 契约签名件 · 已关闭轮次的记录（只读，不追溯重构）。

## 5. 待量与待裁（下一步就是这些，不是方案）

1. 另外六个 run 是否复现同一分布？（本文件只分解了 p5b-firewall 一个）
2. 那 5 份模板抄件改为**引用**（run 只存 CONFIG，脚本从 `templates/run-v2/` 解析）会破坏什么？
   —— 已知的一条：`command_exit` 的 `subject_tree: candidate_commit` 要求脚本存在于**物化的候选树**里
   （run-v2 README 的 comparator 规则），所以"只引用"不是无代价的。
3. CheckResult 若不落盘、改为从 `chk-*.out.txt` + spec 重算，哪些绑定会断？（`state.json` 指针、
   `coverage.json` 的 join、评审员的 re-run 都会碰它）
4. 评审记录 300+ 行/次是不是必须？其中多少是**重推过程**（可由结论 + 命令重放替代）vs **结论**？
5. `SIMP-D` 已定的三分工（journal 记理由 / ledger 只留指针 / commit 正文记本轮）在记录层重设计后
   是否还成立。

## 6. 与既有条目的关系

- 本文件**取代不了**任何已裁的东西；`SIMP-D1`–`D3` 仍然有效，本文件是它们的上位问题。
- 与 rider `RA`（`run_all` 零调用者）、`PD`（`pack_digests()` 零调用者）、`CLI-hist`（v1/v2 命令组）
  同属「harness 自身的形状」问题域，但**不合并**：那三条各有自己的兑现条件。
- 与「harness 独立 git repo 拆分评估」相邻——记录层的体量正是搬迁成本的主要构成，两者宜同场议。

## 7. 第二个数据点 — `p5b-claims`（实测 2026-08-07，答 §5.1 的一部分）

§5 待量第 1 条问「另外六个 run 是否复现同一分布」。跑完 `p5b-claims` 后有了第二个点，**分布复现、
比值不复现**：

```
$ python -X utf8  # 同 §1 口径：逐文件累加 git blob 行数，run 目录全量
runs/p5b-claims   : 94 文件 / 6,165 行
  evidence        : 3,166 行   (51%)
  scripts         : 2,658 行   (43%)  ← 每 run 复制的模板抄件
  instruction     :   243 行
  control         :    98 行
产物（候选净增）  : 20 文件 / 1,585 行
                              → ≈3.9 : 1
```

**结论一：分子的形状复现了。** 证据 51% + 模板抄件 43% ≈ 94%，与 §2 对 p5b-firewall 的分解同形；
「一半以上是每 run 复制的模板脚本」在这一轮是 43%，仍是第二大项。**§5.2（抄件改引用）是这两轮共同
指向的那条。**

**结论二：18.7 : 1 这个比值不是常数，它由分母决定。** 两轮的分子同量级（4,710 / 6,165），分母差了
6 倍（252 / 1,585），比值就从 18.7 掉到 3.9。**p5b-firewall 是一份 amendment，p5b-claims 是二十个对象
加两节 prior-art 裁决**——所以 §1「≈18.7 : 1」应读作*小产物轮*的比值，不是记录层的固有开销率。

**对 §4 范围的影响（一条，不是方案）：** 判据若写成「比值超过 N 就要减记录」，会在小产物轮上恒真、
在大产物轮上恒假，等于按产物大小惩罚。可量的替代是**分子的绝对值与可再生性**——两轮的 scripts
一项分别是 ~2,000 与 2,658 行，且**全部可由模板再生**，这个数不随产物大小变。§5.2 直接冲它。

**诚实边界**：本轮未测 token 成本，只测行数；两轮的 `migration/` 评审记录（本轮 FULL + VERIFY 两份）
未计入上表，与 §1 的 run 目录口径保持一致。样本仍是 2/7 个 run。
