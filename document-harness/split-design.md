# 拆分批设计稿 —— 跨仓运作模型（R0 产物，已签 `HD-40`；实质修改后欠重签）

> 状态：**已签 2026-08-14（`HD-40`）；签字后经多轮 read 反复修改，绑定陈旧、欠重签**——
> 准确次数现算 `git log --oneline 9736670..HEAD -- <本文件>`（不写死：写死的那一刻就少算写下它的那个 commit）。
> 签字形状比照 `HD-35`（绑 blob + sha256），签字记录进
> `HARNESS-DECISIONS.md`；本文件按 governance-scan 判据**不携带自身审批状态**。
> 上游：`document-harness/io-design.md` v1（已签，`HD-35`）§6/§7。**本文件是其续篇、不是修订**
> ——io-design 已签字节不动，续篇独立成件独立签。
> 实测与推理：[journal/repo-split-r0-2026-08-13.md](journal/repo-split-r0-2026-08-13.md)。
> **量程纪律（用户 2026-08-14 批准的写法修正，起因见 §11）**：本文件每一条实测断言**先声明量程
> （整文件 / 某代码块 / 某目录 / 全仓 tracked / 某 revision），再跑覆盖该量程的命令**；两者对不上
> 时不得写成断言。凡带 base 的计数一律注明 revision——`E3` 管的是时间，本纪律管的是**范围**。

## §0 本稿回答什么

`HD-10`/`15`/`28`/`33`/`34`/`35` 已裁「拆不拆 · 什么形态 · 谁跟着走」（`HD-24` 已由 `HD-39` 取代）。
本稿只答**分家之后怎么还能跑**的问题。**§1–§8 每节的落点均已由用户裁定**（2026-08-13/14），
逐条汇总在 §10；节内保留初稿的提议与被推翻的读法，是为了让「改判依据是哪个测量」可查，
**冲突时以 §10 与 `HD-39` 为准**。

## §1 `rsc.py` 归属与独立 CLI（原 `HD-24` 缓裁项，今归 `HD-39` · rider `CLI-hist`/`RA`）

实测（journal §1）：v3 命令块（`:231`→`build_parser`，421 行）对产品模块引用数 = 0，且对
`document_harness` 全是函数内惰性 import。

**块外耦合的完整枚举，共 28 处**〔量程 = 整文件；**两条命令合成**——上述 grep 排除 `:231`–`:651` 得 **24** 行，**另加该 grep 不匹配的四行**：`:48`（`generate,` 是逗号不是点）· `:50`（`harness_cli` 不含任一 token）· `:674`（`stage = sub.add_parser(`）· `:739`（`harness_cli.register(sub)`）。**这四行恰是 R1 要剪的四行**，只跑那条 grep 会全部漏掉〕：顶层三行 `:48`/`:49`/`:50` · **产品命令体 7 处**
（`:57`/`:93`/`:95`/`:104`/`:106`/`:116`/`:126`——随 `rsc.py` 留调用者仓）· **v1 `stage` 组 15 处**
（`:134`–`:223`）另加 `:674` 子解析器块与 `:739` `harness_cli.register(sub)`（随两组剪除，
rider `CLI-hist`）· **`:850`**（共用错误出口，无归宿）。

> **更正二次（re-read 2 `M-1`(c)，2026-08-14）**：上一次把它改成「块外四处」——**仍为假**，
> 且是同一个错法的第三次：断言的量程仍未与所跑命令对齐。现按上面的完整枚举陈述。
> **更正（re-read `M-1`，2026-08-14）**：本节原写「耦合全在顶层三行」——**在文件尺度上为假**。
> `rsc.py:850` 的 `except stage_control.StageControlFault` 位于 `main()`、包着 `args.func(args)`，
> 是**每一个** `rsc` 命令（含全部六个 v3 命令）的共用错误出口，既不在顶层三行、也不在被测块内，
> 故两次块内测量都合法地返回 0 而假断言存活。**执行含义**：import 在导入时求值、`except` 表达式
> 只在异常逃逸时求值，所以按原文剪掉 `:48` 并删 `rsclib/stage_control.py` 后，`rsc.py` 仍可导入、
> 成功路径全绿，而**每个命令的意外失败路径由 `FATAL: …`/exit 2 变成未捕获的 `NameError`**；
> 六个 v3 命令自捕 `SpecGap`/`AssuranceFault`（块内 8 处 handler），这一处正是残余路径，且无测试
> 到达它。`:850` 如何处置（删 / 改绑 v3 fault / 换裸 `except Exception`）是 R1/R2 的设计判断。

**提议**：
- `rsc.py` **留调用者仓**——`inventory` / `compile` 是产品编译器命令，`rsc` 这个名字是产品的。
- **v3 命令组整块搬新仓**，成为新仓自己的 CLI 入口（六命令原样：`governance-scan` / `status` /
  `flow` / `dispatch` / `disposition` / `review`）。零耦合已实测，搬动不需重新设计。
- v1 `stage` 组与 v2 `harness` 组**随各自的树删除**（**已裁 `HD-39`**——初稿此处写的是「随各自的树
  travel」，依据 `HD-24`；`HD-24` 已被 `HD-39` 取代）。`rsc.py:48` 的 `stage_control`/`stage_close`
  与 `:50` 的 `harness_cli` 两条 import 同批剪掉——rider `CLI-hist` 在此兑付，**且剪完两个组连同
  其树一并删除，不再有接收方**。
- 调用者仓**不留 shim**：调用者直接跑 submodule 内的 CLI（`HD-34` 的「不得改动 harness 内容」
  正好排除了在调用者侧包一层的做法）。

**已裁（用户 2026-08-14）**：新仓名 **`do-the-work`**，CLI **主名同仓名 + 短别名 `dtw`**（同一入口
两个名字）。既有文档里的 `rsc v3 <cmd>` 写法随之全部改写，落在 R2。

## §2 `repo-audit.py` 的 ROOT 与 hook 接线（`HD-18` basis 未 scope 面）

实测（journal §2）：`ROOT = parents[3]` 全仓 rglob，`EXCLUDE` 不含 harness 路径；**pre-commit hook
本身未跟踪**，其中 `contract_provenance_check.py` 一段今日已是死代码（脚本不存在），三个 harness
hook 也靠 existence guard 挂着。

**提议**：
- `repo-audit.py` 是**调用者的**（已在 `Thesis/Work/Tooling/`，`HD-31` 之后归属明确）。ROOT 维持
  仓库根，**`EXCLUDE` 新增 submodule 目录**——否则仪器文档会被当论文内容审（今日 246 条 orphan
  噪声里已有一大半来自 harness 树）。
- harness 新仓**不自带 repo-audit**（`E6`：需要新机器的修是重新质疑被守之物的信号）。新仓的
  markdown 完整性由其 pytest 电池与每轮独立评审承担。
- **三个 harness hook 的路径前缀在 R3 显式更新**，并在调用者策略文件（`HARNESS-POLICY.md`）里
  写明这三行的存在——不允许靠 existence guard 静默失效。
- **同批处理今日的死代码**：hook 里 `contract_provenance_check.py` 那段删掉或补回脚本，二选一。

**已裁（用户 2026-08-14）**：hook **改为 tracked**（`core.hooksPath` 指向仓内目录），使其随 clone 走。
**这同时关掉本节记的两个缺陷的根**——untracked = 不进任何评审 subject，故仓里 2026-07-28 已删的
`contract_provenance_check` 在本机 hook 里留存至今无人发现；改 tracked 后这类残留会落进正常评审面。
落在 R3。**边界**：这是**调用者仓**的改动，不进新仓。

## §3 评审记录归哪仓（Q3 —— 两次改判后已裁：乙）

实测：`migration/document-work-assurance-v3/` 共 **117 份 = 29 产品 run + 88 构造**
（**数于 base `0db52a1`；tip 上持续增长——本轮每落一份评审记录就 +1，故此处不记 tip 值，R1 落地时按当时的 base 现算**
——re-read 2 `L-3`：117 原被当常驻事实用，正是 `L-3` 为 335/720 修掉的那个缺陷）（初稿报的
「7 份产品」是判据过窄，更正见 §10.1）。`HD-28` 的判据（记录跟着被记录的对象走）与其组级措辞
（C 整组 travel）在那 29 份上相反。

**已裁（用户 2026-08-14）：乙——逐文件分。** 29 份产品 run 的评审记录**留调用者仓**，88 份构造
记录 **travel**。初稿倾向甲（整目录 travel），被用户以「产品开发的搬进 harness 是污染独立库」推翻；
甲的主要论据（跨仓断链）在重测后大幅缩水——**真链接仅 7 处**，其余 73 处是散文提及不报错（§10.1）。

**R1 的执行含义**：路径清单**须逐文件列**（29 与 88 同住一个目录），并处理那 7 处真链接。

## §4 切线机制（保历史 vs 从头）

实测（journal §4）：签字绑定与切线无关（blob id 只由内容算），故原先挂在这条上的「保历史才能保
签字」不成立、已排除。真代价是**记录与其理由分居两仓**——本 harness 的纪律是理由住 commit 正文。

**已裁（用户 2026-08-14）：新仓从头，不保历史。**（本节初稿倾向 filter-repo 保历史，理由是
`HD-9` 三留之「判断」——不可由命令重新得出的推理住在 commit 正文里。用户在看过 §10.4 的工作量
实测后取「从头」：约 10 分钟、零风险，代价是 **335** 个 commit 的正文留在调用者仓（初版写 337，
更正见 §10.4 的 `L-3` 块）。）

**代价照记**：新仓第一个 commit 的**量级**约 **245**（七前缀集 @base `0db52a1`，量程见 §10.4）
——**该数不等于新仓成员**：按已裁的乙案要减 29 份产品记录、按 `HD-28` 要加 B 治理登记 3 件，
故 R1 的第一件事就是声明唯一的成员集。新仓首 commit 无 provenance；travel 的 88 份评审记录与决策簿
承载规则的「为什么」，而**构造理由留在调用者仓的 commit 正文里**，两者不等价（重叠未测，§10.4）。

**配套（本设计提议，成本近零）**：新仓 README 写一行来历指针——「本仓字节此前的历史住调用者仓
`<repo> @ <commit>`，`ResearchSystem/` 下」。不保历史不等于不留指针；这一行把「去哪找那 335 条
正文」从口口相传变成仓内可读。**同一行顺带承接 R0 read `O-5`**：`rsclib/document_harness/__init__.py:12,16,19`
三行 docstring 用 `rsclib.harness` / `.c14n` / `.schemas` 描述 v3 的来历，而那三个模块按 `HD-39`
删除、按 §4「从头」也不会存在于新仓历史里——代码不坏（是散文），但它指向的来历在新仓内不可达，
由这行指针接住。

## §5 `pack_digests` 与 `E2` 守卫（`HD-27` 重开条件到达 · rider `PD`）

实测（journal §5）：v3 `pack_digests()` **全仓零调用者**〔量程 = 全仓 `*.py`，`grep -rn pack_digests
--include=*.py ResearchSystem`：仅 `__init__.py:238` 定义与 `:266` 的 `__all__`；另三处命中全属 v2 的
同名函数〕——原写「产品侧零调用者」，量程窄于实测；v2 每份 resolved 产物自带 `bindings`
（schema pack digest + resolver 版本），v3 侧 `interface_version`/`harness_version` 零命中。

**提议**：
- **`E2` 维持不加守卫**——`HD-27` 的结论在新条件下仍成立，但**理由换了**：原三条理由里的
  「`HD-16` 使证据离仓自证落空」被 submodule 取代——gitlink 把「用哪个版本的仪器查的」写进了每个
  候选 commit，这正是 `pack_digests` 当年想解决的问题，且比它强（gitlink 覆盖整个仪器，pack_digests
  只覆盖 schema pack）。
- **v3 `pack_digests()` 删除**（`E6`：无任何决定依赖的机器）。v2 的同名函数不动——它有活调用者。
- rider `PD` 因此**兑付**（两半都有归宿：守卫不加、函数删）。

**边界照记**：gitlink 只存在于**调用者仓**。harness 仓自己跑自己（构造轮）时没有 gitlink，其
「哪个版本」由该仓自己的 commit 决定——这不是缺口，是同义反复；但它意味着**产品 run 的证据**能
自证仪器版本，**构造轮的记录**仍不能，与今天一样。

## §6 谁来验记账（rider `ledger-assert`，deadline = 本批）

实测（journal §6）：承接物仍为零；唯一在跑的邻居（`ledger_cap_check.py`）挂在未跟踪的 hook 上。

**提议**：**明确转纪律，不加机器**。两条理由（rider 行已记）在分家后**更强**：① `E6`——刚拆掉一道
检查就造新的等于没裁；② 原锚点脆（`locator_exists` 钉 `.goals/LEDGER.md` 一句人写的中文散文，
8 个 run 里 1 个用过）。分家新增第三条：断言必须住在**调用者仓**的 pre-commit/CI，而调用者仓的
pre-commit 今天连自己都不随 clone 走（§2）——在那个地基上加断言是加在沙子上。

配套：`HARNESS-POLICY.md` §4 已声明「本机不设机器、纪律承接」，本提议只是把它从「暂缺」定为
**终局**。rider `ledger-assert` 随之**兑付删行**（转纪律是处置，不是悬空）。

**已裁（用户 2026-08-14）：接受永久无机器，转纪律。** 与 §2 的 hook 改 tracked 不冲突——后者让
现有的 `ledger_cap_check`（管 120 行上限）随仓走，本条说的是**内容完整性**断言不做。

## §7 `stages/` 与 v1/v2 全族处置（原 `HD-24` ⑦ → 已裁 `HD-39` · rider `SCC`）

实测（journal §7）：2 文件、4 条真链接、零份 Stage Record 曾存在；处置与 §1 的 v1/v2 半边是同一
决定的两面。

**已裁（用户 2026-08-14）：删除，不 travel。** 本节初稿提议 travel，被用户推翻并扩大范围——
连 v1 运行时族一并删。裁决全文见 `HD-39`（`HD-24` 的收窄后继，`HD-24` 同 commit 转 superseded）。

**范围（本轮实测，两次报数）**：向用户呈报「139 文件」时只覆盖 `HD-24` 的七树；补测 v1 运行时族
后**实为 171 文件** —— 139 + `contract/Stage-Control-Contract.md` · `rsclib/stage_control.py` ·
`rsclib/stage_close.py` · `schema/stage-record.schema.json` · `schema/review-result.schema.json` ·
`schema/closure-receipt.schema.json` · `schema/stage-control-fixtures/`（24）·
`tooling/tests/stage_control/`（2）· `.claude/commands/rs-execute.md`。
**上列 33 条中 `contract/Stage-Control-Contract.md` 已计入 139 的「两份契约」，故净增 32 件、
并集 171（实测 `git ls-files … | sort -u | wc -l` = 171，不是相加得来）**——R0 read `L-1` 指出
本处原写「= 32 件」而列了 33 条，按列表划出去会得到 138。
**是这次补测把 139 改成 171 的**；用户的「删」是对 139 那个口径给的，差额留作 R1 执行前的
最后确认点（要缩回 139，划出去的是**净增的 32 件**、不含已在 139 内的 v1 契约）。

**影响面（本节初稿的「删除不留悬空引用」为假，经 R0 read `M-1` 指出并由 executor 复现）**：

- **代码侧成立**：三个 v1 schema 的**字节读者**只在 v1 族自身内（`stage_close.py` ·
  `stage_control.py` · `stage-control-fixtures/validate.py`），v3 零命中；`stage_control`/
  `stage_close` 的全部 importer（`rsc.py` · `rsclib/harness/gitadapter.py` ·
  `rsclib/harness/__init__.py` · 两个 v1/v2 测试）要么在待删集内、要么是本就要剪的 `rsc.py` 两行。
- **文档侧不成立——删除集之外有 4 个文件、14 条引用指进删除集**（13 条 markdown 链接 + **1 条 wikilink**），删除后全部悬空。
  `repo-audit.py:103-115` 用 `cand.exists()` resolve **任意**目标路径（不限 `.md`，目录与 `.json`
  同样计入），一条断链即 exit 1（`:304`）：

| 源文件（**不在**删除集内） | 条数 | 目标 |
|---|---|---|
| `ResearchSystem/README.md` | **8** | `:35` `stages/` · `:39` `contract/Stage-Control-Contract.md` · `:41` `stages/README.md` · `:42` `stages/_stage-record-template.md` · `:43`/`:44`/`:45` 三个 v1 schema · `:46` `schema/stage-control-fixtures/` |
| `.goals/plans/general-harness-v2-architecture-revision.plan.md` | **3** | `:723-725` → `migration/general-harness-v2/nodes/{A1,A2,A3}/NODE.md` |
| `.goals/plans/research-system-stage-control-refactor.plan.md` | **2** | `:323` `pre-refactor-worktree-manifest.md` · `:324` `CTRL-BOOT-v1.md` |
| `.goals/plans/document-work-assurance-harness-v3.plan.md` | **1**（**wikilink**） | `:41` 的 wikilink，目标 stem `General-Harness-Contract-v2` —— 全仓唯一带该 stem 的文件正是被删的 v2 契约。**本表刻意不原样引用该 wikilink**：wikilink 扫描**无 inline-code 豁免**，照抄会让本文件自己变成一条坏 wikilink（实测：写进来即 `repo-audit` exit 1）。**R1 修那 14 条时同此纪律** |

**根因**：初稿 grep 的是**谁读它的字节**，结论却写成**谁引用它**——窄问题的答案被当成了宽问题的。
**`repo-audit` 有三道并列的硬链接检查**（`:304` markdown · `:305` source_trace · `:306` **wikilink**），wikilink 不按路径解析、按 stem 解析，且不受 inline-code 豁免——**故修完 13 条 markdown 链接仍会 exit 1**。（re-read `M-2`；本节初稿只写 markdown 一种，是扫类扩到了「文件」维度、没扩到「链接种类」维度。）

**后果**：这四个文件必须进 R1 的改动边界（已同步进 `HD-39` 的连带清单），否则 R1 的验收线
「repo-audit exit 0」必然不过——正是 `HD-24` 当初用来说「直接删」不存在的那个失败形态。
**裁决不变**：删仍是删，只是影响面按上表计。

## §8 确认（非裁决）

- **今后新 run 的评审记录**：按 `HD-28` 判据随其 run 归调用者仓（新 run 在调用者仓）。本条与 §3
  的历史记录处置**互不影响**——§3 管已存在的 117 份，本条管今后产生的。
- **`--repo-root` 跨仓显式传**（io-design §7 技术遗留：模板默认 `run_dir.parents[3]`，`rsc.py` 同名
  参数默认 cwd，两者不同）——落在 R3，本稿不再展开。

## §9 待用户拍板清单 —— **全部已答（2026-08-13/14）**

原七项加签字前新增的第八项，逐条落点见 §10 表。**签字后仍开着的只有两件，且都不阻塞 R1**：
① 新仓 remote 由用户自建（本地路径先行）；② R1 执行前对删除范围 139→171 的差额做最后确认（§7）。

## §10 用户裁决落点（2026-08-13/14 对话，逐条）

| # | 裁决 | 状态 |
|---|---|---|
| 1 | 新仓名 **`do-the-work`**；remote 由用户自建 | 已裁 |
| 2 | CLI 主名 `do-the-work` + 短别名 **`dtw`**（同一入口两个名字） | 已裁 |
| 3 | **乙：逐文件分** —— 29 份产品 run 的评审记录留调用者仓，88 份构造记录 travel | 已裁 |
| 5 | 记账断言 **永久转纪律**，不加机器 | 已裁 |
| 6 | v1/v2 全族**删除**（非 travel），范围补测后 **171 文件** | 已裁 2026-08-14（`HD-39`） |
| 7 | pre-commit hook **改 tracked**（`core.hooksPath`） | 已裁 |
| 4 | **新仓从头，不保历史**；配套 README 一行来历指针（§4） | 已裁 2026-08-14 |
| 8 | 定位「extend Claude Code」**成立**（§10.3 核实）；**打包层单立一批** | 已裁 2026-08-14 |

**八问全部答毕并全部已裁**（1/2/3/4/5/6/7/8）。R0 步骤 1–7 完成，下一步 = 定稿签字（步骤 8）→ 独立 read（步骤 9）。

### §10.1 §3 乙案的真实代价（本轮重测，推翻 R0 初稿的口径）

R0 初稿说「乙 = 80 处跨仓引用断掉」——**说过头了**。重测把那 80 次拆开：
**真 markdown/wiki 链接仅 7 次**（构造→产品 2 · 产品→构造 5），其余 **73 次是散文里的纯文件名
提及**。机器（repo-audit broken-link）只拦链接，故乙的机械代价 = **7 处**须改写或去掉；73 处退化为
「人要跨两个仓 grep」，不报错。**是这个 7/73 的拆分改的口径**，`HD-28` 的 C 半边照此收窄执行。

同批更正 R0 初稿的分组数：产品 run 记录**不是 7 份而是 29 份**（初稿用的判据是「首 20 行同一行
同时出现 run 名与 run 字」，过窄；改判据为「首 40 行点名任一 run 或出现 `assurance/runs/` 路径」）。
117 = 29 产品 + 88 构造。

### §10.2 删除案（§7 的替代，用户 2026-08-14 提出）

**事实**：v1 stage-control 活约半小时即被 v2 推翻，v2 从未活过一天（用户口述，与 A2 审计的
「注册在案、从未行使」一致——零份 Stage Record 曾存在）。

**`E2` 不挡**：`E2` 的冻结清单是穷举的（v3 契约 `b2dbdf75` + 两份 supersession + 15 个 schema
文件），**v1 `Stage-Control-Contract.md` 与 v2 `General-Harness-Contract-v2.md` 均不在其中**；
规则原文「a path outside them is not frozen by this rule」。故删除是普通用户裁决，不是动冻结面。

**规模（本轮实测，`git ls-files`）**：139 文件 = `harness/` 14 · `tooling/rsclib/harness/` 11 ·
`tooling/tests/harness/` 1 · `schema/harness-v2/` 81 · `migration/general-harness-v2/` 26 ·
`migration/stage-control-refactor/` 2 · 两份契约 2 · `stages/` 2。

**连带清单：以 §7 的表为准，本处不复制**（re-read 2 `M-1`(a)：本段原逐字保留「连带三处 …
指向 `stages/` 的 4 条链接」，即 `M-1` 已改正而此处未扫到的同一断言；而 §0 的冲突规则「以 §10 与
`HD-39` 为准」使这份**未改的**成为操作依据——同一事实两处并存、错的那份反而权威）。
现行连带清单 = §7 表的 **4 文件 14 条引用（13 markdown + 1 wikilink）** + **`rsc.py:850`** + `rsc.py:48`/`:50` 两条 import
+ 已关闭 run `p5b-firewall/build_run.py:216-217` 的边界排除表（纯字符串、不读字节，不影响该 run
的既有证据）。

**代价照记**：`HD-24` 裁的是 travel，删除是**推翻它**，须新建一条后继裁决（`HD-30` 机制）。
本设计**倾向删**，判据 `HD-9` 三砍之「无锁证词」：无任何决定依赖这 139 个文件，留着的唯一效果是
让新仓带一族从未行使的字节出门。

### §10.3 「新仓 = extend Claude Code」定位 —— **上一版本节的判断被核实推翻**

**本节第一版写「仓内属于 Claude Code 的近乎为零」，错。** 用户 2026-08-14 要求核实，核实结果站在
用户那边，依据是 io-design 自己的字节：

- **§2 的「载体」列直接按 Claude Code 定义三角色**：orchestrator = 完整 session（主线）；
  executor = **必须完整 session**「对 Claude Code setting 依赖最高；`claude -p` 子进程或用户当
  传输」；reviewer = **可为 subagent**「对 setting 依赖最低」。
- **§8 待办**列着「orchestrator 载体自动化（`claude -p` 起 executor 等）| 后话；先维持用户当传输」。
- `rsclib/document_harness/dispatch.py`（701 行）内有三份**喂给 Claude Code session 的 prompt
  模板**：`CONSTRUCTION_PROMPT`（`:515`）· `READ_PROMPT`（`:626`）· review dispatch 渲染
  （`render_dispatch` `:400`）。
- §2 另有一条**只在 Claude Code 语境下才有意义**的禁令：「绝不把 setting 抄进 prompt」。

**错在哪**：第一版把「可安装的 Claude Code 件（plugin / skill / command 包）」等同于「Claude Code
资产」。正确的两层口径：

| 层 | 现状 |
|---|---|
| **设计层** | **已经是 Claude Code 形状**——三角色 ↔ 三种载体（session / subagent / `claude -p`），是本 harness 的核心结构，不是外挂 |
| **打包层** | **无 harness 自己的可安装件**〔量程 = 全仓 tracked，`git ls-files .claude`〕：plugin manifest **0** 个；`.claude/skills/` 有 **166 文件 / 3 个 skill**（`nature-academic-search` · `nature-figure` · `nature-polishing`）——**全属论文侧，无一属 harness**；`.claude/commands/` 顶层 **11 个命令**（同一〔全仓 tracked〕量程下 `git ls-files` 数为 **18**，多出的 7 项在 `agent-analysis-profiles/` 子目录内、非命令）中唯一与 harness 沾边的 `rs-execute.md` 属待删的 v1 支。`.claude/` 整个目录被 repo-audit 排除、也不在 travel 集内 |

**故「extend Claude Code 为主」这个定位成立**，缺的只是打包层。真正待裁的因此变成一件具体的事：
**`.claude/` 下该不该有属于 harness 的件**（如 `/dtw-review` 命令、reviewer subagent 定义），
以及它们随不随新库走。**本设计仍建议**打包层单立一批——但理由从「那是新方向」降为「那是**这个
方向的下一步**，其设计面（安装形态、命令面、与规则文本的关系）一条都还没议过」，别让 R1 从搬家
膨胀成重新产品化。

### §10.4 §4 切线：保历史的工作量与复杂度（实测）

| 量 | 值 |
|---|---|
| travel 集跟踪文件 | 〔量程 = 下列七前缀，`git ls-tree -r --name-only <rev>`〕**245 @ base `0db52a1`**（原写 247，那是轮中途值；tip 上已 250 并随本轮记录增长）。按乙案还须从 `migration/document-work-assurance-v3/` 排除 29 份产品记录。**七前缀**：`document-harness` · `tooling/rsclib/document_harness` · `tooling/hooks` · `tooling/tests/document_harness` · `schema/document-assurance-v3` · `assurance/templates/run-v2` · `migration/document-work-assurance-v3`（均以 `ResearchSystem/` 为前缀）。**注意：本行的七前缀与下一行 335 所用的七路径集不是同一个集合**——R1 的前置动作就是先声明唯一的 travel 集，再把两行按同一集合重算 |
| 碰过 travel 集的 commit | **335** / 全仓 **720**（47%），在 base `0db52a1` 上 |
| `git filter-repo` | **本机未装**；`pip install git-filter-repo`（纯 Python，无编译） |
| 主仓 `.git` | 84 MB（克隆一份是秒级） |

**步骤**：装工具 → 克隆一份 → 写路径清单 → 跑一次过滤 → 核对。
**工作量集中在核对，不在跑**（过滤本身分钟级）：247 文件到齐 · 29 份产品记录一份没混进来 ·
tip 的树与源仓子集逐字节相同 · 抽查 commit 正文仍在。
**唯一真需小心处来自乙案**：29 份产品记录与 88 份构造记录同住一个目录，故路径清单不能只写目录前缀，
须逐文件列（或列 29 条排除）。
**风险低且可逆**：filter-repo 在克隆上跑，源仓零改动；结果不满意删掉重来。
**估**：**约 1 小时**（过滤 <5 分钟，其余是清单 + 核对）。对比「从头」：建目录 + 拷 245 文件 +
一个 commit，**约 10 分钟、零风险**，代价 = **335** 个 commit 的正文留在调用者仓。

> **更正（R0 read `L-3`）**：本表初版写 337 / 724，在 base 上不复现。**原因不是算错，是 `E3`
> ——那两个数测于轮中途的 `5aec7f3`（同一条命令在该时点确给 337 / 724），却被当成常驻事实带走。**
> 现值固定在 base `0db52a1`，命令照录（**操作数逐条列出，re-read `L-2` 指出原文的
> `<7 个 travel 前缀>` 是占位符、仓内无处枚举，R1 无法执行**）：
>
> `git log --oneline 0db52a1 -- ResearchSystem/document-harness ResearchSystem/tooling/rsclib/document_harness ResearchSystem/tooling/tests/document_harness ResearchSystem/tooling/tests/document_harness_review ResearchSystem/schema/document-assurance-v3 ResearchSystem/migration/document-work-assurance-v3 ResearchSystem/HARNESS-POLICY.md | wc -l` → **335**
>
> `git rev-list --count 0db52a1` → **720**
>
> （re-read 2 `L-1`：上一版把操作数分行写在 blockquote 内的 code fence 里，渲染后
> blockquote 标记被压进代码行，七个操作数之间成了字面 `>` 字符——那不是 `git log` 而是一串
> 输出重定向，R1 照抄会拿到报错而不是数字。改为单行空格分隔。）
>
> **同表两行不是同一个 population（re-read `L-2`）**：上面这七路径集产出 335/337，而产出 **247**
> 的是另一个十一路径集（5 目录 + 3 登记簿 + 3 份 v3 契约，含 `HARNESS-DECISIONS`/`RIDERS`/
> `DECISIONS-archive`、不含 `tests/document_harness`）；且七路径集带着 `HARNESS-POLICY.md`
> ——按 `HD-28`/`HD-33` 它归调用者。**两个集合都不等于 `HD-28` 的成员裁决**。247 亦是轮中途值
> （base 上为 245）。**R1 的前置动作：先声明唯一的 travel 集，再把这两行按同一集合重算。**

**诚实边界**：不能说「那 335 条正文的要点已被 88 份 travel 的评审记录覆盖」——两者不等价（记录讲
评审发现，正文讲构造理由），**重叠多少本轮未测**。

### §10.5 打包批的已知输入（用户 2026-08-14，随批带走，本批不设计）

- **形态可能不止 submodule**：submodule 是**当前**调用形态（`HD-15`/`HD-33`）；用户意向是
  「若能做成 **plugin 安装**更好」。两者关系（并存 / 取代 / 分别面向谁）**到时候再议**，
  本批不裁、不预设——记此一行是为了打包批开轮时它有个家，不必从对话里捞。
- **`.claude/` 下该不该有属于 harness 的件**（`/dtw-review` 命令、reviewer subagent 定义等）
  随打包批一并议；今日 `.claude/` 既不在 travel 集内、也被 repo-audit 排除。

## §11 写法修正（用户 2026-08-14 批准）—— 量程先声明，再跑命令

**起因**：至本节写下时 R0 已有四轮独立 read、共返**五条** must-fix（1+1+2+1，各记录摘要行）；其后第五轮再返两条。其中**三条同源**——断言的量程与产出它的命令的
量程不一致：① 「删除不留悬空引用」（grep 的是字节读者，写下的是引用面）② 「耦合全在顶层三行」
（跑的是 v3 命令块，写的是整个文件）③ 修 ② 时写的替换句「块外四处」（实为 24 行）。第四条
（plan 仍继承已被 `HD-39` 取代的 `HD-24`）是另一回事——裁决改了没往下游传。

**纪律（本文件与其 journal 适用，今后设计轮同）**：

1. 每条实测断言**先写量程**（整文件 / 某代码块 / 某目录 / 全仓 tracked / 某 revision），再跑
   **覆盖该量程**的命令；对不上就不写成断言。本文件用〔量程 = …〕标注。
2. **绝对量词**（全 / 只 / 唯一 / 零 / 不留）必须带量程，否则降格为限定陈述。
3. 带计数的断言**注明 revision**；随时间增长的量（记录数、commit 数、文件数）额外写明「落地时
   按当时的 base 再算」。`E3` 管时间，本条管范围，二者都要。
4. must-fix 的答复**扫类不扫实例**（`HD-36` ① / `E7`）：改完点名那处，立刻在同一 commit 里
   grep 同一断言的其余写法。

**本轮按此纪律自查后改掉的三处**（非 read 指出，是自查抓的）：
- §10.3「打包层空——无 plugin manifest、无 skill」**在全仓量程上为假**：`.claude/skills/` 有
  166 文件 / 3 个 skill（全属论文侧）。真命题是「无 **harness 自己的**可安装件」，已改。
- §5「`pack_digests` 产品侧零调用者」量程窄于实测——全仓 `*.py` 亦零调用（仅定义与 `__all__`），
  已按实测量程改写。
- §10.4「travel 集 247」是轮中途值；@base `0db52a1` 为 **245**、tip 上已 250，且该七前缀集与
  同表 335 所用的七路径集**不是同一个集合**。已注明量程、base 与两集合不同的事实。

