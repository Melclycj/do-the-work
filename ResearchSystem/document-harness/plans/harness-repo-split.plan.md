# Plan: 拆分批 — harness 搬成独立仓

- **slug**: harness-repo-split
- **created**: 2026-08-13
- **complexity**: 复杂（一个设计轮 + 三个构造轮 + 一个记账收批）
- **status**: **R0 + R1 CLOSED 2026-08-15；R2 CLOSED 2026-08-16**（岔口裁**甲**：只摘 CLI、不重扎根；
  FULL `CHANGES_REQUIRED` → 一条修腿 → VERIFY `REVIEWED_NO_BLOCKER`）。**R3 CLOSED 2026-08-17**
  （FULL `CHANGES_REQUIRED` → 一条修腿 → VERIFY `REVIEWED_NO_BLOCKER` 带三条同类残留，用户裁并入
  R4）**· R4 CLOSED 2026-08-17 —— 整批 CLOSED**（记账批不开轮，八条 rider 逐条有归宿、四条 decision
  转 implemented、ledger 指针转下一队首）。R3 的三个待裁由用户当场裁完：① 调用者副本**本轮不删**（删除与入链重写并进重扎根轮，
  免得同一批链改两遍）② 步骤 19 **移出 R3**（实测：全部 site 都已在 harness 仓，清单见步骤 19——此处刻意不写数字，
  VERIFY `V-1` 抓到的正是本行与步骤 19 的枚举各说一套）
  ③ 指令层三个变更文件欠的独立 read 按**丙**处理，债务原样挂到下次层 read。**理由已按 FULL
  `L-3` 更正**：初版说的「不省电池档故不构成 `E10` 的 relied」站不住——本轮用的正是 tiering 节
  第二个 bullet（tooling 档），而那句恰是 `HD-42` 改过的（`these eight commands` → `these six
  commands and nothing fewer`），属 rule-changing replacement，`E10` 的 deferral 通道够不着它。
  真正让这次 deferral 无害的是另一个事实：`HD-39` 在同一个 commit 里删掉了那两个被划走的 runner
  的整棵树，所以**新旧两种文本下可跑的电池都是同样这六条**，本轮实跑的验证不受该 amendment 是否
  已被独立读过影响。checklist 与 README 那两处是一个 token 的命令改名（`rsc v3 dispatch` →
  `dtw dispatch`），不改变任何规则的要求，确在 deferral 通道内。
- **base_commit**: `0db52a1dcb51def293b4959d72b9d0a6e63f486d`
- **base_branch**: document-work-assurance-v3

## Goal (one line)

把 harness 从 `ResearchSystem/` 里拆出为独立 repo，产品仓以 submodule 钉住其版本——让「这轮是用
哪个版本的仪器查的」写进每个候选 commit，并让仪器可被本仓之外的调用者使用。

## Why / value

`HD-10` 已裁「harness 不依附于 ResearchSystem 存在，因此必须拆」。目的 / 形态 / 成员三件全部裁完
（`HD-10` / `HD-15`+`HD-33`/`HD-34` / `HD-28`+`HD-24`），**执行零进度**。同时四条 rider 的 deadline
或 redeem-when 指向本批，拖住本批即拖住它们。

## Entry gates — 已过

- **`§live` cold read**（`E10` (b) 义务句 + `HD-5`）：`HARNESS-DECISIONS.md` `§live` **11 条全读**，
  2026-08-13（`HD-36` · `HD-35` · `HD-28` · `HD-33` · `HD-34` · `HD-27` · `HD-24` · `HD-23` ·
  `HD-10` · `HD-15` · `HD-9`）。**开卡时口头说的「九条」是错的**——实际 11 条，本行为准。
- **指令层九成员 cold read**（`E10` 引用条款：blob 未变即可引用记录）：九成员在 `f61ce2c..HEAD`
  之间**零写入**，逐个 `git rev-parse` 比对 blob id 全部 SAME，且与
  `v3-checkpoint-read-f61ce2c.md` §表所记的九个 blob id 逐一相等（`15999875` / `54dfef83` /
  `62c55e4b` / `3350bfac` / `17ff31bb` / `b576a45e` / `68031fa2` / `e1a2f26b` / `09aa8699`），
  该记录九成员均标 **read end to end**。故本批开轮的层 cold read 由**引用该记录**贴现。
  **各轮开轮时须重验**——本 gate 只对 `0db52a1` 这个 base 成立。

## 继承的 live 裁决（`HD-5`：原样继承，不转录改写）

| id | 与本批的关系 |
|---|---|
| `HD-10` | 本批的**存在理由**：拆分必须做。执行完可议转 `implemented` |
| `HD-15` | 形态 = submodule（调用侧兑现在 `HD-33`）。**A1 的未量项转 A2 必量**那半已由 A2 完成 |
| `HD-28` | **成员**：新仓 = A 仪器 + B 治理登记 3 件（`HARNESS-DECISIONS.md` · `HARNESS-RIDERS.md` · `HARNESS-DECISIONS-archive.md`）+ C 评审记录；`HARNESS-LEDGER.md` 与其 archive **留调用者**；D 已关闭 run 的产物与 E shadow **留产品仓** |
| `HD-33` | 调用模型：gitlink 钉版本；run 目录 / freeze marker（`.harness/review-pending.json`）/ 四件实例文件**全归调用者仓** |
| `HD-34` | 调用者纪律：调用者仓内不得改动/升级 harness 内容，适配必须记入调用者自己的 decision log；copy 仅为逃生口 |
| `HD-39` | **v1/v2 全族删除（171 文件）**，取代 `HD-24`：七树 + v1 运行时族全部**删除、不 travel**；连带 = §7 表的 3 文件 13 条链接 + `rsc.py:850` + `:48`/`:50` 两条 import + 已关闭 run 的边界排除表（纯字符串）。**`HD-24` 已 superseded 入 archive，不再是 live 裁决** |
| `HD-40` | `split-design.md` 已签（绑定随重签更新）：R1 按 §3/§4/§7 施工、R2 按 §1、R3 按 §2/§6/§8 |
| `HD-27` | `E2` 不加守卫、`pack_digests()` 不接——**重开条件 = 本批**（三条理由届时同时变形）→ R0 的问题 5 |
| `HD-35` | io-design v1 已签（重签 blob `8f3c82c2`）：**本批按 §6/§7 施工**。执行完其对应节后可议转 `implemented` |
| `HD-9` | 记录层三留三砍判据——本批切线（保历史 vs 从头）用它当尺 |
| `HD-23` | journal 数字更正比照 ledger/riders-only：不消耗 `E9` 修腿 |
| `HD-36` | `E10` must-fix 通道含扫类与无字节自写；design test 只在自由通道——各轮修腿的通道判据 |

## 随批 rider

**确定随批（redeem-when 或 deadline 点名拆分批）4 条**：`RA`（独立 CLI 接线）· `PD`（`pack_digests`
去留 + `E2` 守卫重开）· `CLI-hist`（`rsc.py` 两个历史命令组 + 两个 CLI 测试）· `ledger-assert`
（deadline = 拆分批：分家那一刻「谁来验记账」必须当场有答案）。

**可能被触碰即到期 4 条**（碰到才兑付，不预支）：`SCC`（`Stage-Control-Contract.md` 在 `stages/`
族内，`HD-24` ⑦ 一同处置）· `frozen-path-prefix`（若搬动使两份 supersession 的路径 token 变得可写）·
`qp-index` / `qp-inert`（若碰 `paths.py` / `candidate_path_check.py` 的仓根语义）。

**本轮 read `L-3` 补漏的 2 条**（原分类漏掉，二者一执行即到期）：
- **`E10-sync`** —— redeem-when 是「碰 `E10` 成员句的任何批：三处（成员句 / `LAYER` / `EXPECTED`）
  同改并在 commit 正文点名」。**本批必碰**：`tooling/hooks` 是 travel 前缀，故 `layer_path_check.py`
  随仪器走，而它的 `LAYER` 常量把九个成员**硬编码成 `ResearchSystem/` 开头的字符串**；到了新仓
  这些路径匹配不到任何 staged path，**守卫等于不存在而电池照样全绿**，与它配对的
  `EXPECTED` 断言同样失效。§2 安排的「R3 更新三个 hook 的路径前缀」指的是 pre-commit 脚本的调用
  前缀，**不是 `LAYER` 的成员路径**——两件事。
- **`tier-scope` ②** —— 其主题正是 `HD-42` 要改的 tiering 节（见步骤 13 的核对要求）。

bank 现 **28 行**（`HARNESS-RIDERS.md` 38 行 − 表头/说明 10 行），开批时复算。

## Steps

### R0 — 设计轮：跨仓运作模型（ledger 明写「先设计再执行」）

产出：`document-harness/io-design.md` 的续篇或同级新文件（载体形态本轮第一步定），回答下列七问。
**六问来自 io-design §7/§8 与 `HD-18` basis 里 A1 未 scope 到的面，第七问来自 `HD-24` ⑦。**

> **偏差照记（`E11`）**：本轮的预览卡**后置**了——用户 2026-08-13 说「正常走吧」后我直接开跑步骤
> 1–7，卡在实测完成后才渲染。`E11` 要求卡在轮**之前**且等用户（除非另有指示）。「正常走吧」可读作
> 「另有指示」的免等，但**不免渲染**，故此处是偏差不是豁免。本轮零字节落在指令层与 `E2` 冻结面，
> 损害以「用户没能在开跑前看到范围」为限；R1 起照 `E11` 先渲染再动。

- [x] 1. **`rsc.py` 归属**（`HD-24` 缓裁）：v3 子命令组（6 命令，5 纯读 + `dispatch` 唯一写盘）与
      v1/v2 历史命令组（`harness` / `stage`）分别跑在哪个仓；独立 CLI 的入口形态（rider `RA`/`CLI-hist`）。
- [x] 2. **`repo-audit.py` 的 `ROOT` 语义**：两仓下它扫谁的树、submodule 目录算不算。
- [x] 3. **评审记录归哪仓** —— **已裁：乙（逐文件分）**，见设计稿 §3 与 §10 表第 3 行；`HD-40`
      绑 R1 照 §3 施工。**下面三行是改判史，不是当前状态**（曾两次改判）。① 开卡时说成「方向相反、须显式裁」；
      ② 随后降级为「判据可直接推出、不占裁决」；③ **R0 实测把它升回待裁**——
      `migration/document-work-assurance-v3/` 共 **117 份记录，其中 7 份是产品 run 的评审记录**
      （journal §3），目录是混装的，故 `HD-28` 的组级措辞（C 整组 travel）与其自身判据（记录跟着
      被记录的对象走）在这 7 份上相反。**改判依据就是这个 117/7 的构成**（该 7 份判据过窄，
      §10.1 更正为 29/88）。甲/乙两案摆出后**用户 2026-08-14 裁乙**，本步至此关闭。
      **今后新 run 的记录**确按判据归调用者仓——那半确实是确认，见设计稿 §8。
- [x] 4. **切线机制**：保历史（`git filter-repo` / `subtree split`）vs 新仓从头。**唯一真代价 =
      新仓里还有没有 `git log`/`git blame`**（旧仓的历史无论如何都还在）。判据用 `HD-9` 三留三砍。
      **原挂的「`E2` 签字绑定会否失效」已排除**：git blob id 仅由文件内容算出（`sha1("blob "+len+"\0"+content)`），
      换仓不变，三份签字件跨仓照样验得过——本步不必再查它。
- [x] 5. **`pack_digests` / `E2` 守卫**（`HD-27` 重开条件到达）：接不接、`E2` 加不加守卫；连带其
      第二问——**v3 证据从不记自己由哪个 interface 版本产出**（v2 `resolver.py:272` 记在 `bindings`，
      v3 全仓零命中），submodule 的 gitlink 是否恰好承接这件事。
- [x] 6. **谁来验记账**（rider `ledger-assert`）：调用者仓 pre-commit/CI 的一段机器，还是维持纪律。
      修法方向已定（`HARNESS-POLICY.md` 声明锚点 → 断言进调用者仓），**不回 harness 侧**。
- [x] 7. **`stages/` 处置**（`HD-24` ⑦）：删 / 搬 / 留三选一 + 4 条真链接的处置（含已签
      `Stage-Control-Contract.md:23`）。**裁在 R0，执行在 R1。**
- [x] 8. 设计定稿 → 用户签字（**已签 2026-08-14，`HD-40`；稿已成文** `document-harness/split-design.md`，§9 的七个岔口**已全部答毕**）（比照 `HD-35` 的 io-design 签字形状：签字绑 blob + sha256）。
      **绑定已陈旧**：稿自签字后反复修改（次数现算 `git log --oneline 9736670..HEAD -- <该文件>`，
      不写死），重签待 R0 收批。
- [x] 9. 独立 read —— **五轮**（`feb7b48` · `6a946ba` · `4342c6b` · `289f8ab` · `72694c4`），
      共返七条 must-fix，全部已答复。**残留**：末次答复 `ddd773a` 欠一次独立 re-read（`E10`
      must-fix 通道），R1 开轮前付清或由用户明示豁免。

### R1 — 构造：搬字节（前置 = R0 签字）

**开轮前三件已付清**（2026-08-15）：① `ddd773a` 的独立 re-read 回 **0 must-fix / 1 low / 6 obs**
（记录 `v3-cold-read-ddd773a.md`，commit `a7437d3`）② 用户确认删除按 **171** 口径、不缩回 139
③ travel 集由 `document-harness/split-travel-manifest.md` 唯一定义（**254 件** = A 108 + B 3 +
C 143，commit `a1b80fa`），此前流通的 245 / 335 / 247 三个集合一并作废。

- [x] 10. 建新仓 **`D:/do-the-work`**（从头、不保历史，`HD-40`/§4），搬 254 件 + 一份 README
      来历指针（同时承接 R0 read `O-5`）。首 commit `345acdd`，255 tracked。**布局保留
      `ResearchSystem/` 前缀**——R1 的构造判断：仪器按目录深度解析根（`RS_ROOT=parents[3]` /
      `REPO_ROOT=parents[4]`），去前缀会让 `REPO_ROOT` 走出仓外；同一动作里既搬又重扎根会使
      「搬字节」与「改内容」不可分辨。故 R1 只搬，**254 个 blob 与源仓 `e4ffa2b` 逐一相同
      （实测 0 mismatch）**，`E2` 三份签字件 `b2dbdf75`/`68031fa2`/`e1a2f26b` 跨仓验签通过。
      重扎根归 R2。
- [x] 11. **执行 `HD-39` 的删除**：171 文件（139 七树 + 净增 32 v1 运行时族，实测并集 171）。
      同 commit 剪 `rsc.py:48`/`:50` 两条 import 与两个命令组（`CLI-hist` 一半），`:850` 取**删**
      （其捕获的异常类型随模块消失，留着即捕获不可能被抛出的类型）；另修三处随之陈旧的散文。
      `rsc.py` 856→**686** 行（`a8af54c` 正文与本行初版都写 687，实测 686，FULL `L-6`；
      commit 正文不可编辑，更正落此），CLI 现为 inventory / compile / v3。commit `a8af54c`。
- [x] 12. **修 14 条入链（13 markdown + 1 wikilink）**，4 个源文件全在 `a8af54c` 边界内。
      第 14 条按纪律**整句重写去掉 wikilink**，不原样引用、不改写为 inline code。
      同 commit 更正 `HD-39` 后果 ② 的「3 个文件」为 4（漏改残数，`HD-23` 不消耗 `E9` 修腿）。
- [x] 13. `EXECUTION.md:329` 枚举八→六，与步骤 11 **同一个 commit** `a8af54c`、正文点名 `HD-42`
      与被删两条，四重收窄逐条兑现；句尾加一句把 one-shot 边界写进文本。全电池**六条全绿**
      （29 / 80 / 39 / 58 cases / pytest 701 / compile fresh）。`HD-42` 判据当场复证：删前删后
      pytest 均 **701**，两个被删 runner 对 pytest 收集贡献为 0，零覆盖损失。rider `tier-scope` ②
      已主动核：redeem-when 点名节头、本次编辑落在节内枚举句，**不触发，行保留**。
      **该编辑仍欠指令层一次独立 read**（`HD-42` 未豁免），与步骤 13b 同欠、随下次层 read 兑付。
- [x] 13b. **`L-1` 兑付**（用户 2026-08-15 裁「当场套」而非入 bank；`wl-route` 本身未裁、行保留）：
      `EXECUTION.md` tiering 节的五个子计数改为钉 revision + 指示重跑，删去 "tallies reproduce
      exactly"。当期读数由 executor 亲测 @`a8af54c`：六条腿合计 **107s**（pytest 106s），
      节头「≈2 分钟而非 ≈8」不动。自由通道字节按 `HD-38` 自带 commit `e4ffa2b`。
- [x] 14. FULL（`0792a89`，record `v3-review-full-e608204.md`）→ **`CHANGES_REQUIRED`**，
      2 blocker / 6 low / 3 obs → 用户批「A」→ 修腿 `22264b5`（`E9` 第一腿）+ riders-only
      `e6b4d2c` + 新仓 `8cd0b9c` → targeted VERIFY（`dd7a27c`，record
      `v3-review-verify-e6b4d2c.md`）→ **`REVIEWED_NO_BLOCKER`，但带一条 blocker 形状的 `F-1`**
      → 用户批「甲 + 花」→ 第二条修腿（本步的收尾 commit）。
- [x] 14b. **travel 集补 A10 五件**（用户 2026-08-15 裁「甲」）：`assurance/test/`（3，A4
      `test_golden_views.py` 的 coverage golden）+ `tooling/tests/fixtures/expected-{construction,read}-prompt.txt`
      （A5 `test_dispatch.py` 的 prompt golden）。判据与 `A8` 同：已 travel 的测试所读的 golden。
      **合计 254 → 259。** 实测新仓 `pytest -q` 由 **24 failed / 677 passed** 降为
      **20 failed / 681 passed**；余 20 = 15 点名 `rsc.py` + 2 由其 subprocess 导致 + **3 条读
      一份没搬过去的调用者 plan**——最后 3 条**本轮不动**，「仪器的测试去读调用者的树」是 R2 的
      设计问题。

### R2 — 构造：CLI 拆分（前置 = R1 落地）

**范围已裁（用户 2026-08-16）：甲——只摘 CLI，不重扎根。** 重扎根（去 `ResearchSystem/` 前缀 +
`RS_ROOT`/`REPO_ROOT` 深度 + `E10-sync` 三处同改）排到 **R3 之后**单开一轮：那时 submodule 已挂、
调用者副本已删，harness 仓成为 harness 轮次的施工现场，改动落在一个评审员够得着的 range 里；
现在做只能落在新仓，而新仓不在任何 range 内（R1 已为此付过一次代价）。实测支撑：新仓 21 个 `.py`
含 110 处硬编码 `ResearchSystem/`，两处 `parents[4]` 去前缀后会算到仓外。rider `E10-sync` 不到期、
行保留。

- [x] 15. ~~摘 `rsc.py` 的 `harness`/`stage` 命令组 + 两个活 CLI 测试~~ —— **本步点名的四件在 R1
      随 `HD-39` 全部删除**（FULL `L-5`；初写引成 `L-6`，那是行数那条，VERIFY `F-4`），
      故 `CLI-hist` 的这一半已在 `a8af54c` **以删除的方式
      兑付**，无从「摘」。R2 只剩另一半：把 **v3 命令组**（六命令）摘进新仓的独立入口——并入步骤 16。
      rider 行本轮删除（两半全消耗）。
- [x] 16. 独立 CLI 入口落地（`0643229`）：六命令搬进 `rsclib/document_harness/cli.py`（机械切片，
      函数块 421 行 + parser 块 85 行逐行比对 0 mismatch），入口 `tooling/do-the-work.py` +
      `tooling/dtw.py` 两名一入口；`rsc.py` 685→164 行只剩 `inventory`/`compile`；三个 subprocess
      测试改驱新入口；新增 `test_cli_entry.py`（5 例，双 mutation 实证）；manifest 加 A 行；
      顺带兑付 rider `qp-index`（`from_index` 补 `core.quotepath=off` + 负对照）与 `qp-inert`（删空转
      flag），删 `CLI-hist` / `a10-provenance` 两行。**`RA` 未兑付**：其 CLI 半边要新增第七个命令，
      §1 已裁六命令原样，「该不该存在」按 `R5` 归用户——留 R4 对账。指令层两处命名（`E12` /
      `document-harness/README.md:34`）单独 amendment commit `8d137da`，按 `E10` 记两条事实、
      分类可被评审员推翻。
- [x] 17. 全电池六条绿（29 · 80 · 39 · 58 · pytest 707 · compile fresh）；**FULL 已回**
      （`8896ede`，记录 `v3-review-full-297bb2b.md`）→ **`CHANGES_REQUIRED`**，2 blocker /
      3 low / 5 obs。评审员逐行复算两个切片断言（diff 皆空）、在 tip 上亲跑六条电池、四次
      mutation 全复现——**零 blocker 落在实现上**，两条都在「本轮写下的、关于自己伸手到轮外」的
      记述。用户批**全批**修腿（两 blocker + `L-1`/`L-2`/`O-3`/`O-4`/`O-5`）。
- [x] 17b. 修腿 `2ba4369`（`E9` 本轮唯一一条）+ 自由 commit `df75fc9` → **targeted VERIFY
      `a4cc434` `REVIEWED_NO_BLOCKER`**（记录 `v3-review-verify-af93d49.md`；5 条非阻塞
      finding，**零条在代码/schema/测试/守卫上**，全部在「报告测量的散文」）。
      **本轮的更正三次里有两次自己也错，按 VERIFY 逐条改正如下**——
      ① `0643229` 正文的扫类证据里两条 grep 用 BRE 写 `|`，恒返 0（评审员负对照坐实）；**但修腿
      正文贴的替代计数同样不复现**（`V-1`：141/32 在任何 revision 上都产不出；且「17 行里 6 行可
      执行代码 + 3 行冻结 JSON」所依据的命令因模式里的前导引号根本看不见 `assurance/shadow/`）。
      **可信的是处置本身**——两个活面集合由评审员在 tip 上独立重算：sweep A 22 行、sweep B 10 行，
      逐条有归宿。计数不再复述，要当下的数就跑命令。
      ② 「仅剩 `split-design.md:54`」的更正**把量程钉错了 revision**（`V-2`）：写下那句的
      `0643229` 上实为**四行**（另含 `CONSTRUCTION-CHECKLIST.md:129` 与 `document-harness/README.md:34`，
      二者由下一个 commit `8d137da` 改掉），两行是 tip `297bb2b` 上的数。
      ③ 「轮前分叉 3 个」是**把对的改成错的**（`V-3`，评审员据此推翻 FULL 自己的 `O-3`）：在 base
      `4546835` 上逐 blob 比对，新仓与调用者差 **6 个路径**，其中 `README.md` 是新仓自有文档、
      不回灌，故 **resync 要带的轮前分叉是 5 个**——`HARNESS-DECISIONS.md` ·
      `HARNESS-DECISIONS-archive.md` · `HARNESS-RIDERS.md` · `hooks/candidate_path_check.py` ·
      `tests/document_harness/test_precommit_checks.py`。原文的「5 个文件」本来就对。
      ④ `df75fc9` 正文的豁免理由句「两个文件都在本轮 range 之外」被 `git diff --name-only` 证伪
      （`HARNESS-RIDERS.md` 在范围内）；**豁免本身仍成立**，判据是「改的是不是被评审的 work
      product」，而本轮对 bank 的动作是新增一行（`V-4a`）。
      ⑤ `V-5`：七份 plan 归桶时漏了一份没关——`harness-memory-lessons-integration.plan.md`
      尚剩 Step 7，其 `:42` 轮次纪律行已随本收批改写（用户 2026-08-16 裁「当场修」；该文件从未进过
      任何 range，按 2026-08-04 判据不吃修腿）。
      ⑥ `V-4` 电池又比 tip 早两个 commit——评审员在 tip 上六条全绿、数字全复现，形状归已有 rider
      `tier-file-vs-clause`，不另立。

### R3 — 构造：调用者侧接线（前置 = R2 落地）

- [x] 17c. **新仓 `.gitignore` 已建**（用户 2026-08-16 裁「现在删，然后加个 .gitignore」，
      三条候选里取第一条）：新仓自写一份最小件（`__pycache__/` · `*.py[cod]` · `.pytest_cache/` ·
      `.harness/`），**不从调用者搬**——那份在仓根、不在 travel 集内且带论文侧规则。同一动作删掉
      已产生的 6 个 `__pycache__` 与 `.pytest_cache`。commit `f65dcf2`（新仓）。**实证**：再跑一次
      完整 708 条测试后 `git status --porcelain` 为空。**连带一条要记住的**：该文件与 `README.md`
      同属「新仓自有、永不回灌」，故今后按 manifest 命令对账时，**新仓比成员集多的是两条不是一条**。
- [x] 18. **submodule 挂在 `ResearchSystem/harness`**（gitlink = 新仓 `main` @ `f65dcf2`；
      `git submodule status` 有输出）。挂载路径是本轮的构造判断——设计稿未指定：放 `ResearchSystem/`
      域内而非仓根，因为仓根四个顶级目录是 `CLAUDE.md` 讲的部门层叙事，多一个顶级概念要改那份叙事；
      过渡期路径因此是 `ResearchSystem/harness/ResearchSystem/…`（新仓保留前缀所致），重扎根轮后
      收敛为 `ResearchSystem/harness/…`。**四件实例文件 / freeze marker / run 目录本就在调用者仓
      原位，`HD-33` 无需搬动**——新仓自带的是它跑在自身的那一套。**调用者副本按用户裁不删**（① ）。
      连带：`repo-audit.py` 新增 `SUBMODULES` **路径式**排除，而不是往 `EXCLUDE` 名字集里塞一个
      `harness`——`excluded()` 按 part 无限定匹配，那样排掉的是**任何层级、任何将来出现**的同名
      目录，而路径式只钉这一个挂载点、可枚举可审。（写这条时我先举了 rsclib 底下那个 harness 目录
      当反例，连着两次被自己刚接上的 checker 判为解析不到并拦下：`HD-39` 已把它的 tracked 内容删光，
      `git ls-files` 对它现在返 0 条，盘上只剩一个含 `__pycache__` 的空壳。checker 三次都判对，
      两次是这个反例、一次是下面 `submod-index` 那个假阳。）
      mutation 实证见 commit 正文。
- [x] 18b. **pre-commit hook 改 tracked**（split-design §2 用户 2026-08-14 已裁，明写「落在 R3」）：
      仓内 `.githooks/pre-commit` + `git config core.hooksPath .githooks`（config 本身仍 per-machine，
      故 `HARNESS-POLICY.md` §3 写明 clone 后要跑那一条）。**三个 harness hook 改从 submodule 调用**
      ——gitlink 钉住哪个版本的仪器，跑的就是哪个版本的守卫；三支都从进程 cwd 解析仓根，故住在
      submodule 里守的仍是本仓 staged path（blob 三支皆 SAME + 从新位置实跑 exit 0 + 一条真负对照，
      见 commit 正文）。**死代码同批清除**：`contract_provenance_check.py` 那段自 2026-07-28 脚本被删
      起就是空转，正是「untracked = 不进任何评审 subject」的实证，随本次搬迁删掉。
      **已知过渡代价**：`.githooks/` 只在本分支，未合入前别的分支提交时 git 静默不跑 hook。
- [ ] 19. ~~`--repo-root` 跨仓显式传~~ —— **用户 2026-08-16 裁：移出 R3，并进重扎根轮。**
      实测推翻了本步的排期假设：**全部 site 都已在 harness 仓**，`rsc.py` 那一份已随 R2 消失。
      **site 清单按命令输出列全，两次才列对**（FULL `B-2` 抓初版的「两处」；VERIFY `V-3` 又抓到
      更正版在自己声明的量程内仍短两个——声明的量程是 `run-v2/*.py`，跑的却是窄命令
      `grep 'REPO = args.repo_root'`（返 4），而 io-design §7 点名的债是 `run_dir.parents[3]`
      **深度假设**、不是那个 flag）。量程 = `rsclib/document_harness/cli.py` 全文 +
      `assurance/templates/run-v2/*.py`；覆盖该量程的命令是
      `grep -n 'parents\[3\]' ResearchSystem/assurance/templates/run-v2/*.py`（返 **6**）与
      `grep -c '\-\-repo-root' <cli.py>` / `grep -c 'args.repo_root else' <cli.py>`；
      revision = `5fdea21`——
      `cli.py`：**4 个 parser site**（`add_argument("--repo-root")`）+ **5 个解析点**
      （`args.repo_root else` @ `:38` `:75` `:142` `:324` `:409`）；
      **run-v2 模板六个脚本各带同一个 `run_dir.parents[3]` 默认**——带 `--repo-root` 的四个：
      `run_bind_v2.py:170` · `run_evidence_v2.py:121` · `run_repair.py:63` · `run_retire.py:98`；
      **另两个走位置参 `argv[2]`、根本没有 `--repo-root`**：`check_template_instance.py:188` ·
      `make_paragraph_map.py:30`——对它们「显式传」得**先加参数、再改每个调用点**，比原先的
      口径更重；两者还各带一句 `sys.path.insert(0, str(repo_root / "ResearchSystem" / "tooling"))`，
      正是同一轮要去掉的前缀。io-design §7 只点名了 `run_evidence_v2.py:121`，那是**正确的行号、
      不完整的清单**。合计要动的解析点 **11 个、分布 7 个文件**，全部落在 travel 前缀内，
      故**裁决不变**：在 R3 做它即是**在 harness 仓内开构造轮**
      ——撞 rider `battery-travel` 的 deadline，且那些 commit 落在调用者仓任何 range 之外，正是
      R2 裁「重扎根排到 R3 之后」的同一个理由。
- [x] 20. **记账断言明确转纪律**（R0 第 6 问 · split-design §6 用户 2026-08-14 已裁）：
      `HARNESS-POLICY.md` §4 由「此项未定，是待办不是终局」改为终局并写全三条理由；
      rider `ledger-assert` **同 commit 删行**（`R10`：兑付=删行）。同批兑付 rider `cache-count`
      （redeem-when 点名「碰 `repo-audit.py` 的 `EXCLUDE` 或其头部注释」，本轮两处都碰）。
- [ ] 21. **FULL**（本轮碰代码：`repo-audit.py` + 新增 tracked hook，按 tiering 是 tooling 档，
      全电池六条已跑）。`E9` 本轮预算：一 FULL + 至多一条用户批准的修腿 + 一 targeted VERIFY。

### R4 — 收批（记账批，不开轮：2026-08-03 裁「ledger 记账批 user ruling 即 gate」）

- [x] 22. rider 对账**八条逐条有归宿，无一静默留着**（用户 2026-08-17 逐条裁）。随批四条：
      `CLI-hist` **已兑付删行**（R2，两半分别以摘出与删除的方式落地）· `ledger-assert` **已兑付
      删行**（R3，`HARNESS-POLICY.md` §4 定终局）· `RA` **重定范围、非兑付**——产品调用者那半早由
      `HD-25` 关闭（R4 实测一个产品调用者 + 三处测试引用），只剩 CLI 入口一件事，用户判定为便利性
      而非正确性、不为它推翻 `split-design` §1 的六命令原样 · `PD` **重定范围、非兑付**——`HD-27`
      的重开条件已到达，但复核后其三条理由未同时变形（前两条照旧成立，只有 `HD-16` 那条随 `HD-28`
      supersede 而变），且拆分带来的「冻结面两份拷贝」是 `pin-drift` 的题、守卫守不到，故 `E2`
      维持不接，redeem-when 重定为**重扎根轮之后**。可能被触碰的四条：`SCC` 随 `HD-39` 的删除处置
      （R1）· `qp-index`/`qp-inert` **修在 R2 已落而行未删，R4 追认删行**（`R10` 的兑付定义是修 +
      同 commit 删行，本轮补齐后半）· `frozen-path-prefix` 未触碰、行保留。
- [x] 23. decisions 状态（用户 2026-08-17 approve 转）：**转了四条**——`HD-33` · `HD-28` ·
      `HD-15` · `HD-10`，其 `live` 的理由都写着「待拆分批执行」而拆分已执行完（gitlink 已挂、
      成员集已搬、新仓存在），状态词与挪节同 commit（`HD-2` 不变量）。**另四条不转，逐条有据**：
      `HD-34` 的 status 明写「待**首个外部调用者**执行」，那个人还没出现，判据未满足；
      `HD-35` 自写「各批执行完其对应节后可议转」，而 io-design §7 的技术遗留（`--repo-root`
      跨仓）已被移出 R3、并进重扎根轮，对应节未完；`HD-40` 同理，自写「R1–R4 的执行依据、
      各轮执行完其对应节后可议转」，而 R4 本身尚未收完。**`HD-27` 与 `HD-39` 根本不在议转之列**
      ——两条都已在 `HARNESS-DECISIONS-archive.md`，`HD-2` 下终态不可逆；本步初版把它们列进来
      是过期的，与 `HD-24` 同类。**编号与状态只有用户能翻（`HD-2`）**。
- [x] 24. ledger 更新：拆分批 backlog 行转 **CLOSED** 并大幅精简（五轮叙事已在各轮 commit 正文与
      `migration/document-work-assurance-v3/` 的评审记录里，按 ledger 自己的规矩不在账本再写一遍），
      指针转下一队首 = **契约 v4**；`ledger_cap_check.py` ≤120 行复查通过。

## Acceptance (done = ?)

- 新仓存在且 `HD-28` 的四类成员就位；产品仓以 gitlink 钉住它，`git submodule status` 有输出。
- 产品仓在**不改 harness 内容**的前提下，**经 submodule 内的入口**跑通 harness 的 CLI
  （`HD-34` 的纪律面在真实调用上成立）。**本条按 FULL `O-5` 拆两半，用户 2026-08-17 裁甲**——
  原文要求 `status` 与 `dispatch` 各一次，而 `status` 必须带 `--state` 指向一份
  AssuranceWorkState，**只有产品 run 有那份文档，构造轮结构上无法自证**：
  ① **`dispatch` 半：本轮 discharge 完毕**——R3 经挂载点实跑两次（FULL 的
  `f9786a8..eb6fbc2`、VERIFY 的 `eb6fbc2..b1f5b53`），两次都写出了冻结 marker 并产出评审 subject；
  ② **`status` 半：转由下一个产品 run discharge**。本轮另有一次能力证明（借已关闭 run 的
  `ResearchSystem/assurance/runs/p5b-claims/control/state.json` 经挂载点跑通、exit 0，读的是调用者仓
  的 run 目录）——那证明入口可用，**不算本半的 discharge**，因为它没有验证一个活的产品 run 在两仓
  下的状态解析。**两处改动，不只是改名**（FULL `297bb2b` `B-1`）：
  ① `rsc v3 <cmd>` 这条路径已被 R2 删除，`rsc.py` 只剩 `inventory`/`compile`；② `HD-34` 禁止
  调用者侧包 shim，所以「产品仓跑得通」的唯一合法形态就是直接调 submodule 里的 `dtw`——本条从前
  写成 `rsc v3` 时，恰好把被禁的那条路径写成了验收标准。
- `E2` 冻结面三份签字件的 blob id 与签字记录一致（跨仓后仍可验签）。
- repo-audit exit 0；**14 条入链全部处置完毕**（13 markdown + 1 wikilink，**4** 个源文件在 R1 边界内）；全电池**六条**命令绿（`HD-42`）。
- 四条随批 rider 各有归宿（兑付 / 重定 / 明确转纪律），无一条静默留着。
- **不在本 acceptance**：契约 v4（另一 backlog 项）· ④ 审计拆层（2026-08-02 起「仅记录待议」）·
  orchestrator 载体自动化（io-design §8「后话」）。

## 待用户裁（预览卡一次问完）

1. ~~**轮次划分**认不认~~ —— **已批 2026-08-13**（「正常走吧」）：R0 设计 → R1 搬 → R2 CLI →
   R3 接线 → R4 收批。
2. ~~**R0 的七问**够不够~~ —— **已答 2026-08-13**：七问维持。第 4 问收窄（签字绑定与切线无关）；
   第 3 问一度被我降级为确认、R0 实测后升回待裁，**最终由用户 2026-08-14 裁乙**（步骤 3 记改判史）。
3. ~~**R0 设计稿 §9 的 7 个岔口**~~ —— **已全答并签字 2026-08-14（`HD-40`）**。
   **签字后仍开着的只有两件**（`HD-40` 条目内记）：① 新仓 remote 由用户自建 ② R1 动手前确认删除
   范围的净增 32 件。~~**外加本轮 read `L-5`**：量程纪律无 decision 条目~~ —— **已建 `HD-41`（用户 2026-08-14
   「建一条吧」）**，同批把「扫类」由自觉纪律改为**留痕动作**（改动前跑 grep、把输出贴进 commit
   正文）。**其与指令层的关系仍未定**：`E3` 只管时间，范围与扫类留痕在层里无承载，归下一个设计轮。

## R1 收尾账（历史，不是当前指针——当前指针在本文件末尾）

2026-08-15：**R1 步骤 10–14b 全部落地；`E9` 预算已超——本轮走了五腿，上限是三。**
`E9` 原文「one FULL, at most one user-approved fix, one targeted VERIFY」把 FULL 与 VERIFY 一并
计入，故 FULL `0792a89`（1）→ fix `22264b5`（2）→ VERIFY `dd7a27c`（3）**即已用满**；
fix `100e2dd`（4）与 VERIFY `caf633c`（5）都在上限之外。**预算分类是用户的裁决，executor 只
提交账目、不自行分类**（退役 operating contract 的 role 表 + budget 段；VERIFY `100e2dd` 的
`F-1`）。此前本行写「两条修腿花掉三腿中的两腿」是错的——那是只把 fix 计入腿数的读法，`E9`
文本不支持；用户批「甲 + 花」时拿到的正是这个错账。链：
`a1b80fa` travel manifest → `a8af54c` 删 171 + 修 14 条入链 + 枚举八改六 → `e4ffa2b` `L-1`
自由通道 → `e608204` plan → **FULL `0792a89` `CHANGES_REQUIRED`** → `22264b5` 第一腿 +
`e6b4d2c` riders-only → **VERIFY `dd7a27c` `REVIEWED_NO_BLOCKER`（带 blocker 形状 `F-1`）**
→ 第二腿 `100e2dd`（A10 补件 + `F-1`..`F-5`）→ **VERIFY `caf633c` `REVIEWED_NO_BLOCKER`**
（2 low / 4 obs / 0 blocker；`F-1` 即上面这笔账，已改；`F-2` 措辞级入 bank）。新仓
`D:/do-the-work`：`345acdd` → `8cd0b9c` → `f7966c4`（A10 补件），**260 tracked**；本仓外、
不在任何 range 里，其验证由 reviewer 机械复算承担——manifest 规则在 `e4ffa2b` 上跑出 **259**
条路径，新仓恰持这 259 条别无他物，260 个 blob 中 **259 个与调用者逐字节相同**（唯一不同的是
新仓自己写的 README）。

**R1 的两件用户裁决已结（2026-08-16）**：① `E9` 超腿 = **不消耗腿、不欠 VERIFY**（撤回/超出部分
按用户裁一次结账，记账 commit `60088e8`）② ledger 的「执行零进度」假话已于上一 session 的
preclear 改掉（`022fac5`）。`E10-sync` 三处在新仓里**仍解析得到、守卫是活的**（保留
`ResearchSystem/` 前缀所致）——它们在**重扎根那一刻**才死，故那一轮必须把三处同改与重扎根放进
**同一个 commit**；甲案下这一刻推到 R3 之后，rider 行保留、不到期。

## Resume pointer（2026-08-16，R2）

**R2 CLOSED 2026-08-16。** 链（base = `4546835`，调用者侧 settings chore，刻意置于 range 外）：
`0643229` CLI 摘出 + 两条 rider 兑付 + 两行 rider 删除 → `8d137da` 指令层两处命名 amendment →
`297bb2b` plan → **FULL `8896ede` `CHANGES_REQUIRED`**（2 blocker / 3 low / 5 obs，零条在实现上）
→ 用户批全批 → 修腿 `2ba4369` + 自由 commit `df75fc9` → **VERIFY `a4cc434`
`REVIEWED_NO_BLOCKER`**（5 条非阻塞，全在散文层）→ 本收批（`V-5` 当场修 + 四条账面更正 +
resync + 指针）。`E9` 预算用满，未超。

**新仓已有 remote**：private repo `Melclycj/do-the-work`（用户 2026-08-16 批准，`gh repo create --private`，273 文件全推，`origin/main` = `f65dcf2`）——`HD-40` 重签时开着的第①件（新仓 remote 由用户自建）**就此关闭**，R3 挂 submodule 的 URL 已存在。**resync 已落**：新仓 `D:/do-the-work` @ `8e6f3cb`（其后 `f65dcf2` 加 `.gitignore`）。成员集按 manifest 那条命令现算（不写死计数），
逐条对账：新仓持有的**除自有 `README.md` 外与成员集完全相同**，全体成员 blob 与调用者
`d1638a9` **零差异**；本次同步 29 个文件、暂存前逐个比对 0 mismatch。**新仓 pytest 由
20 failed / 681 passed 变为 708 passed / 0 failed**——15 条点名 `rsc.py`（不 travel）、2 条由其
subprocess 连带、3 条读调用者的 plan，全部随 R2 关闭。

## Resume pointer（2026-08-16，R3 构造已落、待 FULL）

**R3 是一轮纯调用者侧的批**——零字节落在 harness 仓（那正是把步骤 19 移出去买到的东西）。
落地四件：① submodule 挂 `ResearchSystem/harness`（gitlink `f65dcf2`）② `repo-audit.py` 加
`SUBMODULES` 排除（mutation 实证：置空则 15 条断链 exit 1，装上则 exit 0、orphan 357→250）
③ pre-commit 改 tracked 且三支 harness 守卫改从 submodule 跑（负对照实证 exit 1）
④ 记账断言定终局 + 两条 rider 兑付删行。bank 在本轮内的净变化：**删 2（`ledger-assert` /
`cache-count` 兑付）、加 1（`submod-index`）、修腿再加 4（`mount-inert` / `nonrec-clone` /
`pin-drift` / `design-route`）**；行数与条数是会长的量，要当下的值就跑
`awk 'NR>10 && /^\| /' ResearchSystem/HARNESS-RIDERS.md | wc -l`（`HD-41` ③）。
**下一步 = 你派 FULL**（range 见收尾 commit；`dtw dispatch` 出）。**FULL 之后**：修腿≤1 →
targeted VERIFY → R4 收批（rider 对账 / decisions 议转 / ledger 指针）。
**重扎根轮**（排在 R3 之后单开）带三件：调用者副本删除 + 入链重写 · 去 `ResearchSystem/` 前缀
与 `RS_ROOT`/`REPO_ROOT` 深度 · `E10-sync` 三处同改（须与重扎根落在同一个 commit）；
步骤 19 的 `--repo-root` 并入该轮。**R3 未触发的 rider**：`battery-travel`（deadline =
第一个在 harness 仓内开的构造轮——本轮不在，行保留）· `E10-sync`（未碰成员句，行保留）。

## Resume pointer（2026-08-16，R2 — 历史）

**下一步 = R3（步骤 18–21）**：submodule gitlink 挂载 + 四件实例文件归位（`HD-33`）·
`--repo-root` 跨仓显式传 · 记账断言按 R0 第 6 问明确转纪律。**R3 开轮前先付的两件**：① 层 cold
read（九成员按 blob 比对，`E10` 引用条款）② `§live` 全读。**重扎根**（去 `ResearchSystem/` 前缀 +
`RS_ROOT`/`REPO_ROOT` 深度 + `E10-sync` 三处同改于同一 commit）排在 R3 之后单开一轮。
**R3 会碰到的两条 rider**：`battery-travel`（新仓跑不了自己指令层要求的电池，deadline = 第一个在
harness 仓内开的构造轮）· `ledger-assert`（deadline = 拆分批）。**R3 带着的三件**：① submodule gitlink 挂载 + 四件实例文件归位（`HD-33`）
② `--repo-root` 跨仓显式传 ③ 记账断言按 R0 第 6 问明确转纪律。**重扎根排在 R3 之后**，单开一轮。
入口：`ResearchSystem/HARNESS-LEDGER.md` backlog 拆分批行。
push debt 现算 `git rev-list --count origin/main..HEAD`（user-gated，勿信 prose 里的数）。

## Notes

- **本批不碰产品侧**：`generated/` 属产品，不随 harness 走（`HD-10` 的 basis 已更正 A1 的 M5/M6
  ——那是另一条切线的代价）。
- **`E9` 预算一轮一算**：R0 用 `E10` 独立 read（无 FULL 预算），R1/R2 各欠 FULL，R3 视档。
- **`HD-36` 的通道判据**在各轮修腿时生效：must-fix 收扫类与无字节自写，design test 只管自由通道。
