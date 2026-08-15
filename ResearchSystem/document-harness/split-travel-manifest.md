# 拆分批 travel manifest —— 唯一的成员集

> R1 的第一件事（`split-design.md` §4 / plan 步骤 10 的前置）：**在搬任何字节之前，声明唯一的
> travel 集**。此前仓内有三个互不相等的路径集合在流通（§10.4 的七前缀集 → 245；同表另一个
> 七路径集 → 335 个 commit；再早一版的十一路径集 → 247），**三个都不等于 `HD-28` 的成员裁决**。
> 本文件取代它们：**成员由本文件的规则与例外表定义，不由任何散文里的数字定义。**
>
> **量程与 revision（`HD-41` ①③）**：下列每条计数的量程写在该条上，revision = `a7437d3`
> （`V3-REVIEW-RECORD-SPLIT-R0-REREAD-ddd773a-v1`）。**记录类目录随每轮增长**，故计数是该
> revision 的快照、不是常驻事实；搬动当时按同一命令现算。
>
> 依据：`HD-28`（成员）· `HD-33`（run / freeze marker / 四件实例文件归调用者）· `HD-39`
> （v1/v2 全族删除，与本集合不相交）· `split-design.md` §3 已裁的**乙案**（评审记录逐文件分）。

## A —— 仪器（整前缀 travel）

量程 = 全仓 tracked，`git ls-files <prefix> | wc -l` @ `a7437d3`。

| # | 路径（前缀或文件） | 文件数 | 为什么是仪器 |
|---|---|---|---|
| A1 | `ResearchSystem/document-harness/` | 26 | 指令层四件 + 设计稿 + journal + history；journal 按 `HD-28` 判据是 harness 跑在自身的实例，随仪器 |
| A2 | `ResearchSystem/tooling/rsclib/document_harness/` | 18 | v3 运行时 |
| A3 | `ResearchSystem/tooling/hooks/` | 4 | 三个 pre-commit 守卫 + `__init__.py` |
| A4 | `ResearchSystem/tooling/tests/document_harness/` | 11 | 钉仪器行为的测试 |
| A5 | `ResearchSystem/tooling/tests/document_harness_review/` | 17 | 同上（评审侧） |
| A6 | `ResearchSystem/schema/document-assurance-v3/` | 15 | `E2` 冻结的 schema pack |
| A7 | `ResearchSystem/assurance/templates/run-v2/` | 8 | run 模板（模板是仪器；模板的**实例**即 run 目录归调用者，`HD-33`） |
| A8 | `ResearchSystem/assurance/review-test/` | 6 | A5 的 golden；唯一读者是 `tooling/tests/document_harness_review/test_golden_review_views.py:39`。**两个历史集合都漏了它**，不跟走则 A5 直接红 |
| A9 | `ResearchSystem/contract/Document-Work-Assurance-Contract-v3.md`<br>`ResearchSystem/contract/Document-Work-Assurance-Contract-v3-supersession-1.md`<br>`ResearchSystem/contract/Document-Work-Assurance-Contract-v3-supersession-2.md` | 3 | 后两份是指令层九成员之二；三份都在 `E2` 冻结面上，**必须逐字节复制**（acceptance：跨仓后 blob id 与签字记录一致） |

**A 小计 108。**

## B —— 治理登记（`HD-28` 点名的 3 件）

- `ResearchSystem/HARNESS-DECISIONS.md`
- `ResearchSystem/HARNESS-RIDERS.md`
- `ResearchSystem/HARNESS-DECISIONS-archive.md`

**B 小计 3。** `HARNESS-LEDGER.md` 与 `HARNESS-LEDGER-archive.md` **不在其列**（`HD-28`：ledger 连
规则都不归 harness）；`HARNESS-POLICY.md` 同样留调用者（它按定义就是调用者侧策略文件）。

## C —— 评审记录（`migration/document-work-assurance-v3/`，逐文件分）

**规则**：该目录下的一切随仪器走，**例外表列出的 29 份留调用者**。29 与 88/94 同住一个目录，
故此处不能只写目录前缀。

**判据（`split-design.md` §10.1 的原判据，本轮已复核可复现）**：顶层 `.md` 文件，首 40 行内点名
八个产品 run 之一或出现 `assurance/runs/` 路径者 = 产品 run 的记录，留调用者。

```
D=ResearchSystem/migration/document-work-assurance-v3
RUNS='p3-corr|p4-bridge|p4-doc|p5a-firewall|p5a-shells|p5b-claims|p5b-firewall|w1-r1'
for f in $(git ls-files $D | sed "s#^$D/##" | grep -v '/'); do
  head -40 "$D/$f" | grep -qE "assurance/runs/|$RUNS" && echo "$f"
done
```

**复现记录**：@base `0db52a1` 该命令给出 117 顶层 `.md` = **29 产品 + 88 构造**，与设计稿 §3/§10.1
逐字相符；@`a7437d3` 为 123 = **29 + 94**。（R1 开轮时一度报「不复现」，是把量程错扩到含子目录并
手挑排除了 11 个顶层文件所致——量程错，不是判据错。此即 `HD-41` ① 要防的那一类，照记。）

**子目录（49 文件，量程 = `git ls-files $D | grep '/'`）全部 travel**：`N0/`(38) · `N1/`(2) ·
`N2/` · `N3/` · `N4/` · `W1/` · `W2/`(4) · `journal/` —— 它们是 v3 自身的建造节点记录（构造），
不在 117 的 population 内，故不受上表规则约束，逐项判定为构造。

### C 例外表 —— 留调用者仓的 29 份

产品 run 的**治理件** 5 份：

- `a1-p4-activation-successor-signature.md`
- `a2-p5a-activation.md`
- `a2-p5a-firewall-signature.md`
- `a3-p5b-activation.md`
- `a3-p5b-firewall-signature.md`

产品 run 的**评审记录** 24 份：

- `v3-checkpoint-read-403fc9a.md`
- `v3-cold-read-1df6245.md`
- `v3-cold-read-e90243a.md`
- `v3-review-full-0439efe.md`
- `v3-review-full-285c596.md`
- `v3-review-full-3137ca9.md`
- `v3-review-full-3657687.md`
- `v3-review-full-3ded65a.md`
- `v3-review-full-5f029cd.md`
- `v3-review-full-86defbc.md`
- `v3-review-full-8ad8c2f.md`
- `v3-review-full-8e2ab26.md`
- `v3-review-full-9c13008.md`
- `v3-review-full-d4769f8.md`
- `v3-review-full-d50d9e5.md`
- `v3-review-full-d52f41b.md`
- `v3-review-full-dcfb2f2.md`
- `v3-review-full-fd0e2ed.md`
- `v3-review-full-fef3a2e.md`
- `v3-review-verify-275da5b.md`
- `v3-review-verify-638972f.md`
- `v3-review-verify-d55d5ce.md`
- `v3-review-verify-dc1e8a3.md`
- `v3-review-verify-de8f4ef.md`

**C 小计 143**（94 顶层 + 49 子目录）。

## 合计与不在其内的

**travel 合计 = A 108 + B 3 + C 143 = 254 @ `a7437d3`。**

明确**不 travel**（列出是因为三个历史集合各自漏或多算过它们）：

- `ResearchSystem/HARNESS-LEDGER.md` · `HARNESS-LEDGER-archive.md` · `HARNESS-POLICY.md`（`HD-28`/`HD-33`）
- `ResearchSystem/tooling/rsc.py`（`split-design.md` §1：`rsc` 这个名字是产品的；v3 命令组的搬迁在 R2）
- `ResearchSystem/assurance/runs/` · `assurance/shadow/` · `assurance/test/` · `generated/` ·
  `handoffs/` · `inventory/` · `contract/` 的其余成员（`HD-28` D/E）
- `.claude/`（既不在任何 travel 集内，也被 repo-audit 排除；其归属归打包批，`split-design.md` §10.5）
- `HD-39` 的 171 个待删文件——与本集合**不相交**（v1/v2 族 vs v3 族）

## 已知的未接线项（R1 不做，`E10` 不允许 R1 做）

新仓内 `tooling/hooks/layer_path_check.py` 的 `LAYER` 常量把指令层九成员**硬编码为
`ResearchSystem/` 开头的字符串**；同一名单另有两处镜像——`document-harness/CONSTRUCTION-CHECKLIST.md:78`
的 `E10` 成员句、`tooling/tests/document_harness/test_precommit_checks.py:164` 的 `EXPECTED`。
新仓里这三处指向不存在的路径，**守卫匹配不到任何 staged path = 静默失效，而电池照样全绿**
（rider `E10-sync` 的三处同改义务正是为此）。

**R1 不改**：改 `E10` 成员句是改规则文本，`HD-42` 那种一次性例外是用户当场造的、且明写不设通则。
故 R1 的交付**明确排除**「新仓的 pre-commit 守卫可用」这一条，新仓 README 照记；接线归 R2
（新仓拿到自己的 CLI 入口那一轮），届时按 rider `E10-sync` 三处同改并在 commit 正文点名。
