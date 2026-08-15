# Journal — 拆分批 R0 设计轮：六问的实测

- 日期：2026-08-13 · base `0db52a1`（plan `harness-repo-split`）
- 性质：分析 / 实测（`HD-1`：裁决进 `HARNESS-DECISIONS.md`，本文件只装测量与推理）
- 产物：`document-harness/split-design.md`（R0 的设计稿，已签 `HD-40`，重签待 R0 收批）
- **量程纪律**（用户 2026-08-14 批准，规格见 `split-design.md` §11）：本文件每条实测断言标
  〔量程 = …〕并跑覆盖该量程的命令；绝对量词必带量程；带计数的断言注明 revision。
  **本轮按此纪律复查全文，改动逐处标「量程复查」**——非 read 指出，是自查。

## §1 · Q1 `rsc.py` 归属 —— v3 命令组与产品**零耦合**（实测）

`ResearchSystem/tooling/rsc.py` 856 行。**顶层 import 三行是 v3 命令块之外耦合的一部分、不是全部**
（原写「是全部耦合面」，re-read 2 `M-1`(b) 扫类更正；完整枚举见本节末）：

| 行 | import | 属谁 |
|---|---|---|
| `:48` | `from rsclib import generate, pipeline, stage_close, stage_control` | 产品（`generate`/`pipeline`）+ v1 stage 运行时 |
| `:49` | `from rsclib.config import GENERATED_DIR, load_config` | 产品 |
| `:50` | `from rsclib.harness import cli as harness_cli` | v2 仪器（rider `CLI-hist` 的一半） |

顶层命令组**五个**〔量程 = 整文件，`grep -c '= sub.add_parser(' rsc.py` 得 **4**；注意去掉 `= ` 后返 **14**——`stage_sub.` 与 `v3_sub.` 的十处子命令含同一子串。第五个命令组不经 `add_parser`〕：
`inventory`（`:656`）· `compile`（`:664`）· `stage`（`:674`，v1）· v3（`:746`）四个由 `sub.add_parser`
直接注册；v2 `harness` 由 `:739` 的 `harness_cli.register(sub)` **程序化注册**，故 grep `add_parser`
看不见它。**（量程复查：原写「四个」却列了五项——按注册方式数是 4，按命令组数是 5，本处取后者并
写明差异来源。）**

**决定性测量**：`_cmd_v3_*` 各函数体对 `rsclib.document_harness` 的 import **全部是函数内惰性
import**，且整块（`:231` 起至 `build_parser`，421 行）里 `generate.` / `pipeline.` /
`stage_close.` / `stage_control.` / `GENERATED_DIR` 的出现次数 = **0**
（`sed -n '231,651p' ResearchSystem/tooling/rsc.py | grep -cE 'generate\.|pipeline\.|stage_close\.|stage_control\.|GENERATED_DIR'`
→ 0；**pattern 照录，re-read 2 `O-5` 指出上一版只留了命令形状、pattern 处仍是省略号**）。

> **更正（R0 read `O-1`）**：本段原列六个行号 `:239/:277/:303/:344/:452/:512` 并称之为「六个
> `_cmd_v3_*` 函数体」——**行号与命令对不上**。`_cmd_v3_*` 实为**七个**函数；那六个 offset 属
> `governance_scan`(231) · `status`(275) · `flow`(296) · `dispatch`(333) · `disposition`(445) ·
> `review_subject`(491)，其中末者是 `review` 的一个 **mode**、不是注册命令；而真正的第六个注册
> 命令 `_cmd_v3_review`(589) 在 `:599-601` import，原列表里没有。**结论不受影响**：耦合数 0 已由
> 评审员在整块 421 行上复测。`split-design.md` §1 的六个 subparser 枚举本身是对的。

→ v3 命令组**可以整块摘走**，不带任何产品代码。留在 `rsc.py` 里的耦合按下列枚举计（原写「四处」，
re-read 2 `M-1`(c) 更正——同一错法第三次：断言量程未与所跑命令对齐）：

**块外耦合的完整枚举，共 28 处**〔量程 = 整文件；**两条命令合成**——上述 grep 排除 `:231`–`:651` 得 **24** 行，**另加该 grep 不匹配的四行**：`:48`（`generate,` 是逗号不是点）· `:50`（`harness_cli` 不含任一 token）· `:674`（`stage = sub.add_parser(`）· `:739`（`harness_cli.register(sub)`）。**这四行恰是 R1 要剪的四行**，只跑那条 grep 会全部漏掉〕：顶层三行 `:48`/`:49`/`:50` · **产品命令体 7 处**
（`:57`/`:93`/`:95`/`:104`/`:106`/`:116`/`:126`——随 `rsc.py` 留调用者仓）· **v1 `stage` 组 15 处**
（`:134`–`:223`）另加 `:674` 子解析器块与 `:739` `harness_cli.register(sub)`（随两组剪除，
rider `CLI-hist`）· **`:850`**（共用错误出口，无归宿）。

> **更正（re-read `M-1`，2026-08-14）**：本段原写「耦合全在顶层三行」，在**文件尺度**上为假——
> `rsc.py:850` 的 `except stage_control.StageControlFault` 在 `main()` 里包着 `args.func(args)`，
> 是所有命令（含六个 v3 命令）的共用错误出口。断言写的是文件尺度，跑的命令却只覆盖 `:231`–
> `build_parser`（`E3`：判据与量程不符）。执行含义与处置见 `split-design.md` §1 的同名更正块。

## §2 · Q2 `repo-audit.py` 的 ROOT —— 且 pre-commit hook **未跟踪**（今天就有问题）

- `Thesis/Work/Tooling/repo-audit.py:31` `ROOT = Path(__file__).resolve().parents[3]` = 仓库根；
  `:62` `ROOT.rglob('*.md')` 全仓扫描，`EXCLUDE`（`:38`）目前挡**十项**（`.git` · `.obsidian` ·
  `.claude` · `.agents` · `node_modules` · `.venv` · `vendor` · `artifacts` · `investigation` ·
  `.pytest_cache`；原写「九项」，R0 read `O-2` 更正），**不含任何 harness 路径**。分家后 submodule 目录仍在磁盘上 → 会被当论文内容审。
- **本轮发现（与 Q2 同源、但今天就是假的）**：pre-commit hook 位于
  `D:/Thesis/.git/hooks/pre-commit`（worktree 共用 `git-common-dir`），**未跟踪、不随 clone 走**
  ——hook 自己的注释就写着这件事。它有 **4 个 python 调用点、覆盖 6 个脚本**〔量程 = 该 hook 文件，`grep -c 'python '` = 4〕：
  `repo-audit.py` · `contract_provenance_check.py` · `ledger_cap_check.py` · 一个 `for` 循环跑三个
  harness hook（`review_freeze_check` / `layer_path_check` / `candidate_path_check`）。
  **（量程复查：原写「五段」——按调用点是 4、按脚本是 6，五既不是调用点数也不是脚本数。）**
- 其中 **`ResearchSystem/tooling/hooks/contract_provenance_check.py` 仓内不存在**
  〔量程 = 全仓 tracked，`git ls-files ResearchSystem/tooling/hooks` = **4** 项：`__init__.py` +
  三个 check〕。该段被 existence guard 包着，
  故**从不 fire** —— 一段今日已死的 enforcement，无人知道。
- 三个 harness hook 在 hook 脚本里写死 `ResearchSystem/tooling/hooks/…` 前缀，同样 existence-guarded。
  分家后前缀变化 → **静默停跑**，与上面那段死代码同一形状。

## §3 · Q3 评审记录目录**是混装的**（推翻本 session 早先的降级）

`migration/document-work-assurance-v3/*.md` 共 **117 份**。其中首 20 行内点名产品 run
（p3-corr / p4-* / p5a-* / p5b-* / w1-r1）的 = **7 份**；全文提到产品 run 的 = **63 份**〔量程 = 该目录顶层 `*.md` @ base `0db52a1`，共 117 份；
**判据 = 全文命中 `p3-corr|p4-bridge|p4-doc|p5a-|p5b-|w1-r1`**（该判据算出 **64**，非下文的 63）——read `O-1` 指出原注只声明量程、
未声明判据，而四种候选判据分别给 69/64/78/57；**按本判据 @base 实为 64 不是 63**（re-read `L-2`）。
tip 值不记——每落一份评审记录就 +1，R1 落地时现算。
**本数已非操作依据**——§10.1 的 29/88 取代之〕。

> **更正（re-read 2 `L-2`）**：本节的 **7 份**判据过窄（「首 20 行同一行同时出现 run 名与 run 字」），
> 已被 `split-design.md` §10.1 取代——改判据为「首 40 行点名任一 run 或出现 `assurance/runs/` 路径」
> 后是 **29 产品 / 88 构造**。下文的 7 与「117/7 的构成」按 29/88 读；结论（目录混装、判据须逐文件
> 应用）不变，只是规模大三倍。

→ `HD-28` 的判据（记录跟着被记录的对象走）与其组级措辞（「C 评审记录」整组 travel）在这 7 份上
指向相反方向。**本 session 早先把 Q3 降级为「可由判据直接推出、不占裁决」是错的**，改判依据就是
这个 117 / 7 的构成——判据能定规则，但目录混装使它必须逐文件应用，而 `HD-28` 是按组写的。

## §4 · Q4 切线 —— blob id 与 commit 正文的分居风险

- `E2` 签字绑定不受切线影响：git blob id = `sha1("blob "+len+"\0"+content)`，只由内容决定，换仓不变。
  本轮据此**排除**了「保历史才能保签字」这条理由（原 plan 步骤 4 挂着它）。
- 真代价在另一边：本 harness 的既定纪律是**理由住 commit 正文**（ledger 反复声明「不可变、可 grep」，
  §当前指针第一条即为此）。新仓从头 → **88 份构造记录** travel 到新仓（按已裁的乙案逐文件分，29 份产品 run 记录留调用者仓；
  本段原写「117 份」，那是分案前的全量——**量程复查**），而解释它们的 commit 正文留在调用者仓
  → 记录与其理由分居两仓，`HD-9` 三留里的「判断」腿断在跨仓边界上。

## §5 · Q5 `pack_digests` 与 interface 版本 —— v2 记、v3 零

- `rsclib/document_harness/__init__.py:238` `pack_digests()`：**全仓零调用者**
  〔量程 = 全仓 `*.py`，`grep -rn pack_digests --include=*.py ResearchSystem` 五处命中：本函数定义
  `:238` + `__all__` `:266`，另三处属**同名 v2 函数**（`harness/schemas.py:75` 定义、
  `resolver.py:272` 与 `tests/harness/run_tests.py:39` 调用）〕。**（量程复查：原写「产品侧零调用者」，
  窄于实测。）**
- `resolver.py:272` 的形状：`"bindings": {**schemas.pack_digests(), "resolver_version": …}` —— v2
  的每份 resolved 产物**自带**「我由哪个 schema pack + 哪个 resolver 版本产出」。
- v3 侧：`interface_version` / `harness_version` / `tool_version` 在 `tooling` 与 `schema/document-assurance-v3`
  下**零命中**〔量程 = 全仓 tracked，`git grep -cE 'interface_version|harness_version|tool_version'` **六个文件**
  命中：v2 的 `schema/harness-v2/observation.schema.json` 与 `harness-v2/fixtures/` 三份 fixture，
  外加本轮自己写的**三份**（本 journal · `split-design.md` · 提出该 finding 的评审记录本身）〕。
  → rider `PD` 的第二问在本轮复证：v3 证据确实从不记自己由哪个版本的仪器产出。

## §6 · Q6 记账断言 —— 承接物仍为零，且唯一在跑的那段也未跟踪

`chk-ledger-note` 拆除后（批 B R3），**内容完整性断言的承接物为零**〔量程 = 全仓 tracked 的
`ResearchSystem/tooling/hooks/` 四项 + 调用者侧 `Thesis/Work/Tooling/`：无一断言「该记的事记了」〕；
最接近的是 `ledger_cap_check.py`，而它只管 120 行上限、不看内容。
它挂在 §2 那个**未跟踪**的 pre-commit 上 —— 即「本机有、clone 无」。故「这轮该记的事真记下来了」
今天既无机器、其邻居的机器也不随仓走。

## §7 · Q7 `stages/` —— 2 文件 4 链接，处置与 Q1 的 v1/v2 半边同一决定

`git ls-files ResearchSystem/stages` = **2**（`README.md` + `_stage-record-template.md`）。
A2 journal §⑦ 已定性为「注册在案、从未行使」（**零份 Stage Record 曾存在——承 A2 的审计结论，
本轮未复测**〔量程 = A2 当时的全仓审计〕），并记明 retire 的前置
= 先裁 `/rs-execute` command 与 `rsc stage` 组的去留（`CLI-hist` 的另一半）。真链接四条，其一是
已签 `contract/Stage-Control-Contract.md:23` 的模板指针；单删即 repo-audit 硬失败。

> **更正（R0 read `M-1`，2026-08-14）**：本段原写「`stages/` 的 inbound 里唯一非记录类引用就是
> 这一条」——**假**。`ResearchSystem/README.md:35/41/42` 是另外三条，且该文件是活索引不是记录。
> 把删除集当整体看，**其外有 4 个文件、14 条引用**指进来（13 markdown + 1 wikilink，逐条见
> `split-design.md` §7 表）。**wikilink 那条由 re-read `M-2` 补**——`repo-audit` 的 wikilink 是与
> markdown-link 并列的另一道硬检查，本轮初稿只扫了一种。
> 本轮的错法：grep 的是字节读者，写下的却是引用面。

→ Q7 不是独立问题：它与 Q1 的「v1/v2 命令组去哪」是**同一个决定的两面**。
