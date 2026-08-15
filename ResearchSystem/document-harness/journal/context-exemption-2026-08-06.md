# Context 豁免的去留 —— 跨轮设计判断（2026-08-06）

> **这是什么。** SIMP-D1 设的第二类 journal 的第三份：**跨轮设计判断**，不是轮次叙事。
> 起因：同一个判定 `_is_context_title` 连吃四轮，评审员在 `V1-CONTEXT-EXACT` 的 FULL 里把它提为
> `O-1`——「豁免小节该不该由指令**声明**，而不是从标题字符串**推断**」——并明说关掉当轮的 `b1`
> 不会终结这个形状。本文件记：**实测**、**两条替代为何都输**、**用户裁决**、**剩余风险**。
> 形状照 [`checker-and-map-2026-08-05.md`](checker-and-map-2026-08-05.md)：实测在前，判断在后。
>
> 裁决本身的指针在 `HARNESS-LEDGER.md`；本轮叙事在 `v1-context-exact-2026-08-05.md` 与各 commit 正文。

## 1. 四轮，同一个形状

判定要回答的是「这个标题是不是**那个** Context 小节」。四次都是：**匹配比「就是这一节」更宽**，于是
一个不是 Context 的小节被豁免，而豁免正是编号态下关掉 paragraph map 与 preamble 授权门的开关。

| # | 判定当时 | 漏掉的标题 | 性质 |
|---|---|---|---|
| f1 | `"context" in title` | `## Appendix A — the frozen context bindings` | 真实缺陷（交付的代码有洞） |
| `V-1` | `startswith("context")` | `## Contextual appendix — the frozen bindings` | 真实缺陷（f1 的修法自带） |
| `b1` | 精确匹配（**代码对**） | 松成 `startswith("context (non-normative)")` 即漏，**600 全绿** | 测试缺陷（守卫不响） |
| `O-1v` | 精确匹配 + 修好的测试 | 松成 `endswith("(non-normative)")` 即漏，**仍 600 全绿** | 仍未被守住的方向 |

评审员在 `v3-review-verify-25511d9.md` §4 的结论：**没有任何字面量集合能关掉这个类**。

## 2. 实测：七份真实指令的 Context 装着什么

（2026-08-06，逐 run 抽 `## Context (non-normative)` 到下一个 `#`/`##` 之间的正文。）

**不是标准引用句。** 每份 20–30 行实质内容，成分固定：**why now**（这轮为什么现在做、在计划里的位置）·
**precedents this run stands on** · **freeze-time disclosure**（哪些留给 FULL 承担）· 冻结版本修订史 ·
ground-truth 方法说明。这是让指令**可读、可评审**的那部分，不是噪音。

> 这条推翻了本判断施工前的一个猜测（「Context 里只有那句 standing discipline 的引用」）——那句话只在
> 测试 fixture `CONFORMING` 里成立，真实指令不是那样。

## 3. 实测：`form_conformance` 那条 ceiling 已经在真实指令里发生

docstring 自述看不见「真 Context 小节里没有标记词的规范陈述句」。实测：这类句子**已经存在**，且
`_NORMATIVE_MARKERS`（`("(normative)", "MUST", "SHALL", "REQUIRED", "必须", "不得", "禁止")`）**一条都不命中**：

| 出处 | 原句 | 它在约束什么 | 类型 |
|---|---|---|---|
| p5a-shells | *every pre-START audit round of this run is a from-scratch full walk* | 审计档位 | process |
| p5a-shells | *every python `command_exit` argv runs `-X utf8`* | 执行方式 | process |
| p4-doc | *semantic re-review of their content is **not** this run's job; faithful rendering is* | 评审范围 | scope |
| p3-corr | *the truth of each corrected figure is established by the independent reviewer re-deriving it* | 责任分配 | process |

**四条全是 process 或 scope，没有一条是「要交付的内容」。** 这个分布是下面裁决的地基。

## 4. `REVIEW.md` 对这个分布的既有处置

FULL 的指令重走是强制的，读的是**原始字节**（`REVIEW.md:111`，invariant 10：*A map cannot reveal
the omission the map itself made*），而且历史命中率是 3/3（截至 w1-r1，三评审员三 subject 全 INCOMPLETE）。

抓到之后强制三样（`review.schema.json` 的 `allOf` 机械 enforce）：`unmapped_unit_ids` · 一条 finding ·
一条 `residual_uncertainty`（**唯一到达用户的那条**）。然后分两支：活做了且证据可查 → 披露并继续；
活没做或无法从 pinned revision 确立 → `SPEC_GAP`，停机 + 新 WorkSpec 修订 + 新 START（V3-D7）。

**关键豁免**：

> **process claims are never `SPEC_GAP` grounds.** An instruction unit that commands *process* — a read
> order, a fresh-context requirement — has no evidence lock at any revision.

即 §3 那四条即使漏映射，按规则**本来就只报告、不停机**。

## 5. 两条替代，为何都输

**(1) 取消豁免**（编号态下每个内容块必须在 `R<n>` 里）。技术上最干净：检查从**语义式**（这句是不是
规范？不可判定）变成**结构式**（这块有没有 `R<n>` 祖先？一次 parse），**两个洞同时构造上消失**，
且是纯删除（`_is_context_title` · 标记词表 · `FORM-NORMATIVE-IN-CONTEXT` · `context_text` 全退役）。
**输在 §2**：那 20–30 行 why-now / precedents / 冻结披露必须搬出指令，指令因此变得不可读——用可读性
换一个「不需要信任」的检查。

**(2) 声明式**（让指令声明哪一节是 Context）。**输在它不同构**：`form: enumerated` 有**结构证伪器**
（有没有 `R<n>`、有没有块落在外面），所以「verified, not believed」在那里是实话；而 `context_section: X`
**没有**任何结构证伪器——作者把 `## Appendix A` 声明成 Context 再塞规范条文，照样过。它把信任从
「harness 猜标题」挪到「作者写声明」，**没有消除信任**。买到的只是：意外 → 明示假陈述、不可见 →
START 时可见、不可归属 → 可归属。

**两条共同的代价**：都要退回 SIMP-B1 那笔省钱（编号态重新欠回 paragraph map + preamble 授权门）。
成本量级——仓库有记录的是**单次从零通读 ~212k tokens / 14 分钟**（run-v2 README，p5a-shells round 6），
以及 p5a-firewall 为审计烧过**四轮 ~525k tokens**；**「每次全量 START ≈2 小时」是用户自己的估计，
本仓库没有该口径的测量**（此处照 `E3` 标明来源，不当作实测数字用）。

## 6. 裁决（用户 2026-08-06）

**维持现状：保留 Context 豁免，不取消、不改声明式、不加机器。** 承担「指令在 Context 里写规范条文」
的风险，理由是该风险的代价低于每次全量 START 的固定开销。

赌注的实际形态由 §3 + §4 界定：**今天真实存在的那类误写，规则本来就只报告、不停机**。

**剩余风险（不因裁决而消失，写明以便日后核对）**：若有人在 Context 写**要交付的内容**（不是 process/
scope），且 WorkSpec 漏映射，且做没做**无法从 pinned revision 的证据确立**——仍然是 `SPEC_GAP`：停机、
新 WorkSpec 修订、重开 START。豁免只摘掉 process 那一支的停机分支，从不摘掉披露。

## 7. 两个后果

- **rider `mark-case` 价值下降**：它记 `_NORMATIVE_MARKERS` 大小写敏感（小写 `must` 不响），而那是本次
  整类接受的「无标记规范句」的**窄实例**。接受整类却仍在意小写 `must` 不自洽。**未撤**——撤一条已入
  bank 的行本身是一个决定，本次裁决没做这个决定。
- **P5B 是这个赌注的第一次真实检验**：第一份编号态指令写出来时，它的 Context 装的是不是仍然只有
  process/scope，是可直接复核的——复核方法就是 §3 那张表的做法。
