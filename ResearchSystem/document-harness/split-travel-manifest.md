# 拆分批 travel manifest —— 唯一的成员集

> R1 的第一件事（`split-design.md` §4 / plan 步骤 10 的前置）：**在搬任何字节之前，声明唯一的
> travel 集**。此前仓内有三个互不相等的路径集合在流通（§10.4 的七前缀集 → 245；同表另一个
> 七路径集 → 335 个 commit；再早一版的十一路径集 → 247），**三个都不等于 `HD-28` 的成员裁决**。
> 本文件取代它们：**成员由本文件的规则与例外表定义，不由任何散文里的数字定义。**
>
> **量程与 revision（`HD-41` ①③）**：下列每条计数的量程写在该条上，revision = **`e4ffa2b`**
> ——搬动实际发生的那个 tip。**记录类目录随每轮增长**，故计数是该 revision 的快照、不是常驻
> 事实；搬动当时按同一命令现算。
> **更正（FULL `L-4`）**：初版把 revision 写成 `a7437d3`，而 A1 的 26 与 A 合计 108 自
> `a1b80fa` 起才成立——**本文件住在 `document-harness/` 里，把自己算进去了**，在 `a7437d3` 上
> 该前缀是 25、A 合计 107。交付的集合一直是对的（108 / 254 @ `e4ffa2b`，与新仓实测一致），
> 错的只是那两个数字头上的 revision 标签。犯在一份**自称是成员唯一权威、且抬头点名 `HD-41` ①③**
> 的文件里，照记。
>
> 依据：`HD-28`（成员）· `HD-33`（run / freeze marker / 四件实例文件归调用者）· `HD-39`
> （v1/v2 全族删除，与本集合不相交）· `split-design.md` §3 已裁的**乙案**（评审记录逐文件分）。

## A —— 仪器（整前缀 travel）

量程 = 全仓 tracked，`git ls-files <prefix> | wc -l` @ `e4ffa2b`（A10 一行于 `dd7a27c` 补入，
其 5 件在 `e4ffa2b` 上同样存在，故该 revision 对整表成立）。

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

| A10 | `ResearchSystem/assurance/test/`（3）<br>`ResearchSystem/tooling/tests/fixtures/expected-construction-prompt.txt`<br>`ResearchSystem/tooling/tests/fixtures/expected-read-prompt.txt` | 5 | **已搬过去的测试所读的 golden**，判据与 A8 完全相同。用户 2026-08-15 裁「甲」补入（VERIFY `F-1`）。前三件是 A4 `test_golden_views.py` 的 coverage golden——初版把 `assurance/test/` 明文列进「不 travel」，而携带它的测试已 travel；后两件是 A5 `test_dispatch.py` 的 prompt golden，其整个前缀（`tooling/tests/fixtures/`，调用者 98 件）**无任何 A 行覆盖**，故新仓为 0 |

**A 小计 113**（原 108 + A10 的 5）。

> **A8 抓到的形状，A10 是同一个**（VERIFY `F-1`）：初版为 `review-test` 抓住了「golden 不跟走
> 则测试红」，却没把同一把尺子扫过其余 fixture 前缀——`E7`/`HD-41` ④ 的扫类不扫实例，本文件
> 自己没做到。补入前实测新仓 `pytest -q` = **24 failed / 677 passed**，其中 **7 条与 `rsc.py`
> 无关**：3 条读一份没搬过去的调用者 plan（**两案都不动**，「仪器的测试去读调用者的树」是 R2
> 的设计问题）、2 条缺 A10 的 coverage golden、2 条缺 A10 的 prompt golden。

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

**travel 合计 = A 113 + B 3 + C 143 = 259 @ `e4ffa2b`。**（初版 254 @ `a7437d3`：两处错——
revision 标签见抬头的 `L-4` 更正块，成员数见 A10。）

明确**不 travel**（列出是因为三个历史集合各自漏或多算过它们）：

- `ResearchSystem/HARNESS-LEDGER.md` · `HARNESS-LEDGER-archive.md` · `HARNESS-POLICY.md`（`HD-28`/`HD-33`）
- `ResearchSystem/tooling/rsc.py`（`split-design.md` §1：`rsc` 这个名字是产品的；v3 命令组的搬迁在 R2）
- `ResearchSystem/assurance/runs/` · `assurance/shadow/` · `generated/` ·
  `handoffs/` · `inventory/` · `contract/` 的其余成员（`HD-28` D/E）
- `.claude/`（既不在任何 travel 集内，也被 repo-audit 排除；其归属归打包批，`split-design.md` §10.5）
- `HD-39` 的 171 个待删文件——与本集合**不相交**（v1/v2 族 vs v3 族）

## `E10-sync` 何时到期 —— 不是现在，是 R2 重扎根那一刻

`tooling/hooks/layer_path_check.py` 的 `LAYER` 常量把指令层九成员**硬编码为 `ResearchSystem/`
开头的字符串**；同一名单另有两处镜像——`document-harness/CONSTRUCTION-CHECKLIST.md:78` 的
`E10` 成员句、`tooling/tests/document_harness/test_precommit_checks.py:164` 的 `EXPECTED`。

**实测（量程 = 新仓 `D:/do-the-work` @ 首 commit，命令见下）**：R1 步骤 10 保留了
`ResearchSystem/` 前缀，**正是这个决定让九个成员全部解析得到**——`LAYER` 九项 missing **0**。
守卫在新仓里是**活的**：往指令层文件塞一条坏路径并 stage 后，`layer_path_check` 与
`candidate_path_check` **两条都 exit 1 当场 BLOCK**；`review_freeze_check` exit 0，因为
`.harness/review-pending.json` 按 `HD-33` 是**调用者的**文件——设计内的惰性，不是失效。
新仓 `pytest tests/document_harness/test_precommit_checks.py` **42 passed**，含
`test_layer_equals_the_hand_written_membership`。

> **更正（FULL `B-1`）**：本节初版写「三处指向不存在的路径、守卫匹配不到任何 staged path =
> 静默失效、电池照样全绿」，**是反的**。那句写于 `a1b80fa`，当时新仓布局未定、它是一条预测；
> `345acdd` 决定保留前缀使它变假，而无人回头跑那条能证伪它的命令（一条 `test -f` 即可）。
> 违 `E3`（写进文本的事实断言须先跑可证伪它的命令）与 `HD-41` ①②（「匹配不到任何」「静默失效」
> 是无量程的绝对量词）。**后果不是措辞**：它把 `E10-sync` 咬人的时刻搞反了——见下。

**真实状态 = 调用者已接线、新仓未接线、两边逻辑都完好**：`D:/Thesis/.git/hooks/pre-commit`
**存在**并逐条调用那三个 check，`core.hooksPath` 未设、worktree 无本地 `hooks/` 目录，故 git
从 common dir 解析——**本轮每一个 commit 都走过它**；新仓 `.git/hooks` 里没有 pre-commit。
这是 `document-harness/README.md` "Local enforcement" 已记的 per-machine 约定（装不装是每台
机器的事，fresh clone 上本就没有），与守卫逻辑是否成立无关。

> **更正（VERIFY `F-2`）**：本段初版写「**两个仓**的 `.git/hooks` 都没装 pre-commit」——假。
> FULL 的原句带着使它为真的限定（source repo 的 hook 住在 main repo 的 `.git/hooks` 里），
> 压缩成「两个仓」时把限定丢了。要紧处在于本节主题恰恰是「守卫什么时候真的跑」，被抹平的正是
> 它要解释的那个不对称。**这是本轮第三次同一形状**（`B-1` · `F-1` · 本条）：写下绝对量词而
> 没先跑那条能证伪它的命令，而 `HD-41` ① 正是管这个的。

**故 `E10-sync` 的到期点是 R2**：重扎根（去掉 `ResearchSystem/` 前缀）**正是**让那九个字符串
不再解析的动作。R2 必须把三处镜像的修改与重扎根放进**同一个 commit**——否则就交付一个守卫静默
失效的窗口，形状与 `HD-42` ③ 强制枚举编辑骑同一 commit 的理由完全一致。R1 不改这三处，理由是
改 `E10` 成员句是改规则文本、R1 无此权限（`HD-42` 那种一次性例外是用户当场造的且明写不设通则）
——**不是**因为它们已经坏了。

复现命令（在新仓根跑）：

```
python - <<'PY'
import pathlib, sys
sys.path.insert(0, "ResearchSystem/tooling")
from hooks import layer_path_check as L
root = pathlib.Path(".").resolve()
print([m for m in L.LAYER if not (root/m).exists()])   # -> []
PY
```
