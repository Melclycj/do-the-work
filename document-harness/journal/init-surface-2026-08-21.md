# INIT-SURFACE — 2026-08-21（批 DTW-INDEPENDENCE R4 收官轮）

轮次事实（链条、blocker、修法）在各 commit 正文与四份评审记录里，不在此重写。本文件只装
三样按 `HD-1`/`HD-9` 属于 journal 的东西：不可由命令重新得出的设计推理、`E1` 的持有披露、
以及一条跨轮模式的测量注记。

## 1 `E1` 持有披露（本轮四次派发，一次说清）

本轮 orchestrator 与 executor 是**同一个 work-side 会话**。四次派发——开轮 cold read、
amendment 复读、FULL、targeted VERIFY——的 dispatched / prompted / scoped / reported-through
**四项持有全部在该会话手里**。每个评审者都是 fresh-context 会话、所有数字自行从仓库重推导
（各记录的 disclosure 节可核），但按 `E1` 重写后的中间态处置，这**不自称结构性独立**，是
纪律性独立。FULL 的 `O-1` 与 VERIFY 的 `O-5` 各自独立复核并记录了同一事实。

## 2 三件设计裁决的推理（裁决本身由层文本与决策簿承载，此处只留为什么）

- **`--into` 不加**：`E6` 的判据——它缺席时没有任何决策改变。挪位需求已有 `HD-34` 的
  适配通道（caller 自己搬 + 记入自己的 decision log），`init_target.py` 的 `TEMPLATES`
  注释本就声明目的地是 default 而非 requirement。加选项是给一个已有答案的问题造第二个
  机器解。故本轮把答案**写成判据**而不是写成代码。
- **判据与分工 home 都落治理层 `document-harness/README.md`**：用户 2026-08-21 追问后
  确认的关键区分——仓库有两个 README，对外前门的**根 README** 不是成员、无守卫、三句
  已证伪（rider `readme-cli-stale`，用户裁继续 bank，连同 LICENSE 不入本轮）；判据要的
  「被每轮独立 read 覆盖、改动走 amendment 机制」是**成员身份**的属性，与仓库将来
  public 与否无关。用户明确了开源意向（做 public），这只加重根 README+LICENSE 那笔
  bank 的分量，不改变判据落点。
- **判据是判断不是证据**：按 `HD-9` 的量尺没有命令能算出「树里那半可进、机器那半不进」，
  它是 `R5` 裁决写成规则文本；其权威来自裁决，不来自测量。用户问过这一点，答案记档。

## 3 跨轮模式注记：同族句子第四次，以及它的收口

`O-5`（VERIFY `2538893`）记录的「三次连续修腿在同一族分工句子上翻车」在本轮走到第四次：
candidate 自己在「does not restate it」下面四行留了复述（FULL `B-1`），修腿又在一处
pointer 里把「why the two must agree」指给一个不载该事实的 home 行（VERIFY `L-1`）。
两次都不是关键词 grep 抓到的——5 个关键词扩到 7 个仍够不到第八种写法；真正的覆盖命令是
VERIFY 用 `ast` 把两守卫 + 两测试模块的全部 22 条 docstring（13 055 字符）抽出来通读。
测量结论：这族缺陷对关键词扫描免疫，量词句要的是**通读**而非 grep（`HD-41` ① 的「覆盖
该量程的命令」在散文量词上的实际形状）。收口本身按用户裁决落地：home 一处说、四处指过去，
家族自此有守卫可及的单一承载（home 行在 `E10` 成员里，受每轮独立 read 覆盖）。

## 4 零散判断（一行一条）

- FULL `O-2` 的 `R5` 问题（152 行测试 vs `E6`）：用户批修腿时未反对维持，测试留下；
  sweep_refs 仍非守卫（恒 exit 0），测试钉的是报告行为不是 verdict。
- FULL `O-6` 已作为证据注入 rider `self-caller-guards` 的 source 列。
- VERIFY `O-4`（`candidate_path_check.py` 刻意无数字的 overlap 句）：按裁决目的不算
  未完工，留待下次触达该文件时明确决定，记录在 VERIFY 原文即可，不入 bank。
