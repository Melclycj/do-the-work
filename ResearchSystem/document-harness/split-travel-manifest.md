# 拆分批 travel manifest —— 成员集的定义

这份文件定义 harness 独立仓（`do-the-work`）的成员集：**哪些路径随仪器走、哪些留调用者**，
以及决定每一条的规则。依据 `HD-28`（成员）· `HD-33`（run 目录 / freeze marker / 四件实例文件归
调用者）· `split-design.md` §3 已裁的乙案（评审记录逐文件分）。

**这里放规则和名单，不放计数。** 计数是从规则导出的，会随每轮新增记录而变；要当下的集合就跑
下面这条命令。搬迁过程中的更正、读数与轮次经过同样不在此处——它们住在
`migration/document-work-assurance-v3/` 的评审记录与各轮 commit 正文里。

```
# 当前成员集（在调用者仓根跑）
D=ResearchSystem/migration/document-work-assurance-v3
RUNS='p3-corr|p4-bridge|p4-doc|p5a-firewall|p5a-shells|p5b-claims|p5b-firewall|w1-r1'
PREFIXES='ResearchSystem/document-harness
ResearchSystem/tooling/rsclib/document_harness
ResearchSystem/tooling/hooks
ResearchSystem/tooling/tests/document_harness
ResearchSystem/tooling/tests/document_harness_review
ResearchSystem/schema/document-assurance-v3
ResearchSystem/assurance/templates/run-v2
ResearchSystem/assurance/review-test
ResearchSystem/assurance/test
ResearchSystem/tooling/tests/fixtures/expected-construction-prompt.txt
ResearchSystem/tooling/tests/fixtures/expected-read-prompt.txt
ResearchSystem/tooling/do-the-work.py
ResearchSystem/tooling/dtw.py
ResearchSystem/contract/Document-Work-Assurance-Contract-v3.md
ResearchSystem/contract/Document-Work-Assurance-Contract-v3-supersession-1.md
ResearchSystem/contract/Document-Work-Assurance-Contract-v3-supersession-2.md
ResearchSystem/HARNESS-DECISIONS.md
ResearchSystem/HARNESS-RIDERS.md
ResearchSystem/HARNESS-DECISIONS-archive.md'
{ echo "$PREFIXES" | xargs git ls-files
  for f in $(git ls-files $D | sed "s#^$D/##"); do
    case "$f" in */*) echo "$D/$f"; continue;; esac
    head -40 "$D/$f" | grep -qE "assurance/runs/|$RUNS" || echo "$D/$f"
  done
} | sort -u
```

## A —— 仪器

| 路径 | 为什么是仪器 |
|---|---|
| `ResearchSystem/document-harness/` | 指令层四件 + 设计稿 + journal + history；journal 按 `HD-28` 判据是 harness 跑在自身的实例 |
| `ResearchSystem/tooling/rsclib/document_harness/` | v3 运行时 |
| `ResearchSystem/tooling/hooks/` | 三个 pre-commit 守卫 |
| `ResearchSystem/tooling/tests/document_harness/` | 钉仪器行为的测试 |
| `ResearchSystem/tooling/tests/document_harness_review/` | 同上（评审侧） |
| `ResearchSystem/schema/document-assurance-v3/` | `E2` 冻结的 schema pack |
| `ResearchSystem/assurance/templates/run-v2/` | run 模板。模板的**实例**即 run 目录归调用者（`HD-33`） |
| `ResearchSystem/assurance/review-test/` | `tests/document_harness_review` 的 golden |
| `ResearchSystem/assurance/test/` | `tests/document_harness` 的 coverage golden |
| `ResearchSystem/tooling/tests/fixtures/expected-construction-prompt.txt`<br>`ResearchSystem/tooling/tests/fixtures/expected-read-prompt.txt` | dispatch prompt 的 golden。**该前缀其余文件不 travel**——它们是产品编译器的 fixture |
| `ResearchSystem/contract/Document-Work-Assurance-Contract-v3.md`<br>`…-supersession-1.md`<br>`…-supersession-2.md` | 后两份是指令层九成员之二；三份都在 `E2` 冻结面上，**逐字节复制**，跨仓后 blob id 须与签字记录一致 |
| `ResearchSystem/tooling/do-the-work.py`<br>`ResearchSystem/tooling/dtw.py` | 仪器自己的 CLI 入口（R2 建，`split-design.md` §1 + `HD-40` §10：一个入口两个名字）。**该前缀其余文件不 travel**——`rsc.py` 是产品编译器 |

**一条未写明的依赖（FULL `297bb2b` `O-4`）**：travel 前缀是
`ResearchSystem/tooling/rsclib/document_harness`，所以 `rsclib/__init__.py` **不 travel**——两个
入口的 `from rsclib.document_harness.cli import main` 在新仓靠 **PEP 420 namespace package** 生效。
今日成立且实测：五个 travel 前缀内 `from rsclib import` / `import rsclib` / `SCHEMA_VERSION`
零命中，新仓 pytest 已按此导入。记在这里是因为它一旦失效是**静默**的——谁哪天在 `rsclib/`
根加一个必须被导入的名字，新仓就会在 import 期炸而这份 manifest 一个字都没提过它。

判据一句话：**已 travel 的测试所读的 golden 必须一同 travel**，否则那些测试在新仓必红。
`assurance/review-test/` · `assurance/test/` · 两个 prompt golden 这四行全部由这一句决定
（原写「后四行」，R2 在其后加了 CLI 入口那行，按位置指的说法就此作废）。

## B —— 治理登记（`HD-28` 点名的 3 件）

`ResearchSystem/HARNESS-DECISIONS.md` · `ResearchSystem/HARNESS-RIDERS.md` ·
`ResearchSystem/HARNESS-DECISIONS-archive.md`。

`HARNESS-LEDGER.md` 与其 archive **不在其列**（`HD-28`：ledger 连规则都不归 harness）；
`HARNESS-POLICY.md` 同样留调用者——它按定义就是调用者侧的策略文件。

## C —— 评审记录：逐文件分

**规则**：`migration/document-work-assurance-v3/` 下的一切随仪器走，**下面点名的 29 份留调用者**。
两类记录同住一个目录，所以这里不能只写目录前缀。

**判据**（`split-design.md` §10.1 原文）：该目录**顶层** `.md`，首 40 行内点名八个产品 run 之一
或出现 `assurance/runs/` 路径者 = 产品 run 的记录，留调用者。命令见文首。
**子目录全部 travel**（`N0/` `N1/` `N2/` `N3/` `N4/` `W1/` `W2/` `journal/`）——它们是 v3 自身的
建造节点记录，不在顶层 `.md` 这个 population 内，逐项判定为构造。

### 留调用者的 29 份

产品 run 的治理件：

- `a1-p4-activation-successor-signature.md`
- `a2-p5a-activation.md`
- `a2-p5a-firewall-signature.md`
- `a3-p5b-activation.md`
- `a3-p5b-firewall-signature.md`

产品 run 的评审记录：

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

## 不 travel

- `ResearchSystem/HARNESS-LEDGER.md` · `HARNESS-LEDGER-archive.md` · `HARNESS-POLICY.md`（`HD-28`/`HD-33`）
- `ResearchSystem/tooling/rsc.py`（`split-design.md` §1：`rsc` 这个名字是产品的。R2 已把 v3 命令组
  搬进 `rsclib/document_harness/cli.py` 与上面两个入口，`rsc.py` 只剩 `inventory` / `compile`）
- `ResearchSystem/tooling/tests/fixtures/` 的其余成员——产品编译器的 fixture
- `ResearchSystem/assurance/runs/` · `assurance/shadow/` · `generated/` · `handoffs/` ·
  `inventory/` · `contract/` 的其余成员（`HD-28` D/E）
- `.claude/`——归打包批（`split-design.md` §10.5），且被 repo-audit 排除
- `HD-39` 删除的 v1/v2 全族——与本集合不相交

## 新仓的守卫状态

不写在这里。它是随时会变的状态，且已有 owner：**当下的事实跑新仓 README「State of this
repository」那张命令表；`E10-sync` 何时到期归 rider bank 那一行。**
