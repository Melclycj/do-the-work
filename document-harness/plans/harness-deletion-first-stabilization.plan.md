# Plan: harness deletion-first stabilization

- **slug**: harness-deletion-first-stabilization
- **created**: 2026-07-27（同日经独立 review agent 对抗审查后修订，逐条吸收）
- **complexity**: 复杂
- **status**: planned
- **base_commit**: 1c97e61
- **base_branch**: document-work-assurance-v3

## Goal (one line)

按 2026-07-27 外部审计的采纳裁决收敛 v3 harness：删掉制造 finding 的散文面，修掉验证过的机制缺口，把 run 证据搬出说谎的目录，然后用一个真实小任务证明 happy path 能跑、用诚实口径重测负担——在此之前 Stage 2 暂停。

## Why / value

收敛后：construction 轮次的指令面从 ~200 行缩到 ≤50 行（read 递归停）、E1.3 契约恢复为真、11 组真实机制缺口关闭、下一次论文文档工作可以直接用 harness 而不手抄历史脚本。

## Context to resume cold

**全部裁决**在 `ResearchSystem/HARNESS-LEDGER.md` 的**整个「▶ 当前指针」块**——不只裁决清单，还包括 **bank**（两条 rider：`nd-F1` 措辞修正 + `O3` read-flag 收口，都欠"下一批碰 instruction layer 的批次"——**Phase A 就是那一批**，见 Step 2）。不要重新裁已裁的。

**Roles**：执行按现行两份 contract（`ResearchSystem/migration/document-work-assurance-v3/v3-harness-{operating,review}-contract.md`）直到 Phase A 落地；每轮改动前渲染 preview card——**首行必须写「买到什么 / 多久用一次 / 不做会怎样」**（card 模板依赖全局 CLAUDE.md §0.6；若该配置缺席，最低要求 = 首行买到什么 + 轮次表 + 等确认）；独立 review 走 `dtw dispatch --range <base>..<tip>`（`ResearchSystem/tooling/dtw.py`，2026-08-16 前是 `rsc.py v3 dispatch`；六个命令由拆分批 R2 摘进 `rsclib/document_harness/cli.py`），用户路由到独立 session。**每轮的记录**沿用既有惯例：review/read 记录写到 `ResearchSystem/migration/document-work-assurance-v3/v3-review-{full,verify}-<subject-sha>.md` 或 `v3-checkpoint-read-<sha>.md`，commit 标题 `V3-<轮名>-v1` 单行 + 一段正文。

**已验证的缺陷清单（不要重新验证，直接修；行号以 base_commit 为准，均经两轮独立核实）：**

| # | 位置 | 缺陷 | 修法形状 |
|---|---|---|---|
| M1 | `rsclib/document_harness/checks.py` `_collapse` (**line ~262**) | `..` 会 pop 掉栈里已有的 `..`：`a/b/c.md` 里 `../../../../x.md`（逃逸仓库）被归一化成仓库根 `x.md` → false PASS | 前导 `..` 不互相抵消；解析出仓外 = broken link |
| M2 | `checks.py` `run_all` (~line 405) | SPEC_GAP 结果被收集后**继续跑完全部后续 check**（含外部命令），循环结束才 raise，与自身 docstring 矛盾 | 记录该 gap 结果后立即 raise，不执行后续 |
| M3 | `checks.py` `_run_command` (~line 328) | `subprocess.run` 无 `timeout` | 加固定宽松超时（如 600s），超时 = FAIL 带说明；不加配置旋钮 |
| M4 | `checks.py` `frontmatter_keys` (~line 471) | **已实证**（review agent 复现）：`"approved_by":` 与 `'approved_by':` 两种引号形式都绕过 governance scan | regex 兼容引号 key；测试红→修→绿 |
| M5 | `rsclib/document_harness/flow.py` `check_repair_decision` (line ~368) | `NO_REPAIR` 在一切绑定检查**之前**提前 return——指向别的 run/work/candidate 的 NO_REPAIR 判 clean | 提前 return 前先核 run/work/candidate 绑定 |
| M6 | `rsclib/document_harness/summary.py` `check_assurance_candidate` | 精确计数：9 个 ref 属性中 `candidate_ref` 有核、`review_refs` 只数个数，**恰好 7 个**（work_spec/resolved_plan/instruction_audit/fulfillment/manifest/coverage/check_result）只存不核 | 与同在手上的 state pointers 交叉核对 path+digest（不引新 I/O） |
| M7 | `summary.py` `generate_summary` (line ~205) / `check_summary` | `decision_ref` 原样存入、从不与 decision 字节核对；check 只核 candidate digest 与 decision 的 target | generate 处两者都在手，enforce；check 处给 ref 校验路径 |
| M8 | `templates/run-v2/run_evidence_v2.py` (line ~109) | 每个 obligation 无条件写 `IMPLEMENTED`，全文件无第二个 status 字面量 | 模板要求逐条显式 status；缺条目=拒绝 |
| M9 | `templates/run-v2/run_bind_v2.py` (line 44/63) | 写死读 `review-full.json`、只绑一个 ref，无 `repair_round` 分支 | 按 repair_round 读 full/verify，`review_refs` 绑全 |
| M10 | `rsc.py` line ~430 | CLI `v3 review` 仍是 v1 `check_package`；`check_subject`（review_subject.py:319）与 `check_review_result_v2`（review_result_v2.py:66）零 CLI 接线 | `--subject <SHA>` 模式接 v2 双检查 |
| M11 | **#8 机械化**（最大一项，独立轮） | unit map 人工挑选，漏看不可见（p3-corr 实证：audit COVERED 仍漏 3 个规范单元） | paragraph skeleton（`instruction.py` 新函数，按段落枚举+sha256）→ run-local `paragraph-map.json`（人只填 classification 列；enum 已确认 `["obligation","context"]`，零 signed 字节）→ cross-checker 三向核对；升级现有 `check_template_instance.preamble_issues`。**结果列挂在枚举条目上，禁建平行数组**（⑤ 教训：平行数组的对齐税产出了那轮 2/3 的 blocker） |

**明令不修（写进批次记录，防"顺手修复"）：**
- START 覆盖 / `advance()` 无守卫重置 state——契约 §1 威胁模型内（single writer, tamper-evidence not tamper-proof）；修=升级契约承诺，需用户另行发起。
- digestless pointer——`_resolve_pointer` 已报 `POINTER-UNVERIFIED` issue，是"可见的未验证"设计，非缺口。
- unit-map 判断充分性天花板——M11 让漏看不可表示后，错判仍可能且可见即可（V3-D7 本来不承诺语义完备）。
- General Harness v2 / Stage-Control 的旧实现缺口——历史化处理（Phase D），不修。

**冻结面（完整版，比口头说的宽）**：signed 三 blob——plan `8ad404b1` / contract `b2dbdf75` / supersession-1 `68031fa2`（`git rev-parse HEAD:<path>` 每轮复核）；**外加 hard rule 5 的全集**：N0 schemas 既有字节（`common` / `local-check-spec` / `review` / `user-decision` 等 `schema/document-assurance-v3/` 既有文件）、`ResearchSystem/contract/` 既有文件、**签名 plan blob `8ad404b1` 本身**（2026-07-28 收窄：原写「`.goals/plans/` 既有文件」是对 hard rule 5 的误推，源文只冻结 approved plan；与 checklist E2 对齐，本 plan 自身的 tracker/pointer 因此可写）。**新增文件**到 `.goals/plans/` 与 schema 目录允许（后者会被 `test_readme_enumeration.py` 强制登记 README 行）。两个精确 oracle——`ResearchSystem/tooling/tests/fixtures/expected-construction-prompt.txt` + `tooling/tests/document_harness/test_readme_enumeration.py`——**用户声明：动它们必须先经其本人**。

**工作区现状（base_commit 时点）**：`ResearchSystem/HARNESS-LEDGER.md` 有未提交的裁决记录；本 plan 文件 untracked；`ResearchSystem/docs/General-Harness-v2-Design.md` untracked（Phase D 处置）——Step 1 提交前两者。

**Phase E 的负担对照锚**：N3 的旧口径在 `migration/document-work-assurance-v3/N3/N3-record.md` §measurement + `shadow/measure.py`（authored-bytes / payload，17% 结论的出处；已判定该口径漏掉脚本/评审/轮次）。

## Constraints / Out-of-scope

- 每个修复配**敌对负向测试**（红→修→绿；mutation 探针按 hard rule 4，从 scratchpad 副本 sha256 还原，禁 `git checkout --`）。
- 每 commit：pytest 全绿 + `python Thesis/Work/Tooling/repo-audit.py` exit 0。
- 分组成轮，**不做 10 个微轮**；每轮独立 review（用户路由）。
- 修复若需要**新增机制** → 停下重新质疑范围（scope rule 1），不加守卫。
- OUT: Stage 2（暂停中，Phase E 后由用户裁决复开）；威胁模型升级；预测性补模板脚本（真实 run 见证到缺什么才补什么）；删 v2/stage-control 的代码或测试；parked I/O-boundary round 的其余范围。

## Steps

- [x] 1. **落账**：提交 HARNESS-LEDGER 裁决记录 + 本 plan 文件（一个 commit）。→ 已由 `2b5fa28 STABILIZATION-PLAN-AND-RULINGS-v1` 完成（用户提前落账，见该 commit 正文末句）。
- [x] 2. **Phase A — 指令层收缩**（一轮）。→ `820b287` + 修复批次（cold read 用户 waive；bank 以删除清偿）。**checklist 草稿已存在**：`ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md`（2026-07-27 规划 session 起草，带 DRAFT banner，**未生效**——冷 session 压缩 200 行契约正是 no-rewrites 风险，所以趁两份契约都在上下文时写好；双侧同文件：execution E1–E12 + review R1–R7（起草时）→ R1–R8（收缩轮）→ R1–R9（刹车轮加 bank 规则）；channel 定死 R6 + rule-2 cold read 保留在 E10。**起草时的 R5「reviewer 可建议删除」已于 2026-07-28 按 read `820b287` MF-2 推翻**——恢复源 §10 的认知上限：报形状、不下结论）。**尺寸披露：较 ledger 裁决"~30 行"放宽为双侧合计（review agent 高-3：退役两份契约后 review 侧不能没治理文本）——user 2026-07-27 追认（"这个现在做吧"）**。Phase A 的活 = ①对照两份源 contract 逐条复核草稿无漏（压缩源清单：operating 的 §Role boundary / §Hard rules 1–9 / §Scope discipline 1–2 / §Instruction discipline 1–4 + budget + dispatch + commit 规矩；review 的 §1 / §5 / §8 / §10）②去 DRAFT banner ③两份旧 contract 变 stub ④清 bank ⑤过 read。**channel 定死**（关闭 `issue-p3-corr-review-record-channel-unspecified`）：review record 由 review session 在 worktree 写 `v3-review-{full,verify}-<sha>.md`，execution side 提交，commit 标题 `V3-REVIEW-RECORD-<轮>-<sha>-v1`。**两份旧 contract 变 5 行 stub**（首行 `> 2026-MM-DD superseded by CONSTRUCTION-CHECKLIST.md; full text at <退役前最后一个 sha>`——dated 行顺带满足 contract-provenance pre-commit hook；叙事与 rationale 留在 git 历史，**不抄**）。**保持两个旧路径存在**：受保护的 dispatch fixture 硬编码指向 `v3-harness-review-contract.md`，stub 在原路径重定向 → **fixture 一个字节不动**。**同批清空 bank**：nd-F1 与 O3 所在的句子随叙事删除而消失，batch message 里记明"bank 以删除方式清空"。`REVIEW.md` 的 v1 package 段搬 `ResearchSystem/document-harness/history/`。**开轮时在 preview card 上向用户申请 rule-2 cold read 的处置**（waive 先例：⑤——`1df6245` 已冷读、其后每批自带 read；user 裁 route 则先读后开）。
- [x] 3. **Phase A read**：checklist 的独立 checkpoint read（rule 1 对旧文本的最后一次全额执行）；此后各轮在 checklist 下运行。→ 记录 `v3-checkpoint-read-820b287.md`（提交 `3743849`）：6 must-fix / 6 low / 9 observation；全部 dispositioned，MF-4 由用户裁「删守卫」。**修复批次按 E10 自身欠一次 amendment read**（该条不可 waive，只有开轮 cold read 可）——Phase B 依赖 checklist 之前须过。
- [x] 4. **Phase B — 搬家**（一轮）：`git mv ResearchSystem/generated/document-assurance ResearchSystem/assurance`。→ 235 文件纯改名（0 insert / 0 delete）；3 处活引用同轮改并经 mutation 探针证明绑得住（指回旧路径 → 真红 `golden missing`，非崩溃）；closed-run blob digest 与文件数搬前搬后一致。**偏差（已披露）**：research-agent plan 的 3 处不止「加注释」而是**改成新路径**——其中一处是可粘贴执行的 cold-resume 命令，留旧路径等于留一条必坏的命令；HARNESS-LEDGER 唯一那处在裁决记录里、本身已同时写明新旧两个路径，故未动。**第二处偏差（已披露）**：`N3-record.md` 里 4 条 **markdown 链接**搬后断链、audit 红——plan 的「历史记录不改字」把这类当成散文提及、没区分链接。只改 4 个链接**目标**（`](...)` 内），散文与表格（含 §61 当年批过的 allowlist 声明）一字未动，另加一行 dated 说明；理由：证据够不着比路径过时更坏。**活代码引用 = 3 处测试模块，pathlib 分段拼接，同轮改**：`tooling/tests/document_harness/test_golden_views.py:30`、`tooling/tests/document_harness_review/test_golden_review_views.py:39`、`tooling/tests/document_harness_review/test_review_v2_subject.py:52`（找残留用分段形式 `"generated"` grep，**勿用**字面 `generated/document-assurance`——字面 grep 正是漏掉这三处的原因）。历史散文引用 **11 文件 / 36 处**（4 plans + 6 migration records + 1 ledger-archive；Step 1 之后 HARNESS-LEDGER 成第 12 个）：历史记录不改字；**其中签名 plan `8ad404b1` 只读**；活文件（research-agent plan、HARNESS-LEDGER）加一行注释。E1.3 无需 carve-out 自动恢复为真。suite+audit 绿。
- [x] 4.5 **Phase B2 — 把 memory 里早已总结的经验真正接进 harness**（一轮，用户 2026-07-28 新增）。**起因是实证不是主张**：本 session 的 7 个执行者错误里，至少 5 个违反的是 memory 里**已经写着的**条款——`v3-review-craft-lessons`「枚举型主张必重推」被违反 4 次（16/46 的分类、38 vs 36 且据此否掉正确的 reviewer、「四轮里三轮」的搬运、README 的计数），`feedback-prose-claims-derive-or-omit`「characterization 先跑命令再写」被违反 2 次（两句"已扫干净/已证明没削弱"，验证范围都窄于声明，第二次发生在修第一次的那个 commit 里）。**结论：写在 memory 里的经验，模型不会自动照做；它必须成为 harness 的一条规则，或者不存在。** 活 = ①逐个 atom 判定（checklist 已覆盖 / 需新增一条 / 属 preference 留 memory）②新增的**合并成一次** instruction-layer 修订、走一次 read（不逐条开轮）③**C 规则在此落地**：commit body 与记录只留 digest 类身份证明，不写描述性计数——判据是「这个数缺席时哪个决定会变」④operative atom 迁出 memory、preference 留下，关闭 `issue-p3-corr-harness-knowledge-in-memory`（原挂在 Phase D，移到此处）⑤在轮记录里附「本 session 7 个错误 → 各自违反的 atom」对照表，作为该 atom 值得成为规则的证据。**候选 atom**：`v3-review-craft-lessons` / `feedback-prose-claims-derive-or-omit` / `feedback-derivability-is-not-a-reason` / `feedback-guard-expectation-independence` / `feedback-thesis-change-impact-pass` / `v3-session-role-separation` / `v3-review-priority-implementation-correctness` / `feedback-subjects-before-argument` / `feedback-concise-reporting`。
- [x] 4.6 **Phase C0 — 让构造轮能跑成 run**（一轮，用户 2026-07-28 从 C3 提前；**执行在新 session**）。
  → **CLOSED 2026-07-28**：候选 `d9ff80a` → FULL `bff5f39`（`CHANGES_REQUIRED`，2 must-fix，两条都在测试层：五道守卫只探了三道）→ 一次 fix `fbe0b63` → VERIFY `6349c90`（`REVIEWED_NO_BLOCKER`）→ errata/收口 `d8cd593`。预算用尽。M9 按裁决未做，故 bind 对含修复轮的 run 仍不完整。残留一条 low（`test_nothing_is_written_before_the_refusal` 断言过宽）留给下一批碰该测试文件的轮次。展开见 [`harness-phase-c0-m8-m10`](harness-phase-c0-m8-m10.plan.md)。**展开见 [`harness-phase-c0-m8-m10`](harness-phase-c0-m8-m10.plan.md)**——含开写前必读的 8 条读物清单、已用命令核过的 3 条事实、以及照抄缺陷表原话的 Acceptance。范围 = **M8 + M10 两条，M9 不动**（用户指定范围，不自行加）。
  **为什么提前**：B2 实证——用户给的八项规格只交付两项，两半都塌：**清单不全**（哪些算义务由执行者手挑）+ **状态不诚实**（执行者自己宣布关闭）。后者的机器修法就是 M8。本 session 读源确认 `templates/run-v2/run_evidence_v2.py` 的 `claims` 推导式给每条 obligation 无条件写 `"status": "IMPLEMENTED"`，因此**只要 M8 不修，任何义务枚举（含 C4 的 M11）都是空的**：一张完整清单，每行自动盖「已实现」。顺序因此是 **M8 先于 M11**——先前在对话里说过「M11 先做」，那是把用户的反对直接翻译成动作、没有论证，**作废**。
  **M8**：模板改为逐条显式 status，缺条目 = 拒绝（缺陷表 M8 行）。
  **M10**：`rsc.py:430` 仍调 v1 `check_package`，且该文件内无 `check_subject` / `check_review_result_v2` 任何引用（本 session grep 确认）→ 接 `--subject <SHA>` 走 v2 双检查。
  **披露的残缺（不要当成没有）**：M9 按用户裁决留在 C3。它写死读 `review-full.json`、只绑一个 ref、无 `repair_round` 分支，所以 C0 之后 bind 这一步对**含修复轮的 run** 仍不完整；C0 只让「单轮无修复」的 happy path 能跑通。
- [x] 5. **Phase C1 — checks.py 组**（一轮）：M1 + M2 + M3 + M4，各配负向测试 + 正向对照 + mutation 探针。
  → **CLOSED 2026-07-29**：候选 `11ce5b4` → FULL 记录 `70a530a` `REVIEWED_NO_BLOCKER`，**零 blocker，
  修复与 VERIFY 预算未动**。FULL 独立重跑了五套件 / repo-audit / 三个签名 blob / `run_all` 调用者 grep，
  并按真实修复前形状独立复现了全部四个 mutation 探针（四次值级红 + sha256 匹配还原），其中包括本轮披露
  「行为证明只靠探针」的 M3。五条 observation 全部 non-blocking：**O-1** 交用户裁（已裁，见 ledger）、
  **O-2** 存入 R9 bank、**O-3**（C1 捎带 C0 收尾编辑）noted not charged、**O-4**（`run_all` 零调用者）
  进 harness backlog、**O-5**（M3 探针依赖）属已验证的诚实披露。
  **开轮时的两处裁决**（记此供 FULL 归因）：① `E10` 开轮 cold read 判 **waive**——本轮 subject 全在 `checks.py`
  代码层，一个指令层字节都不碰（先例 ⑤ / Phase A / C0）；② **M3 的结果词汇从缺陷表写的 `FAIL` 改为
  `SPEC_GAP`**——`local-check-spec.schema.json` 的 `allOf` 要求 `command_exit` 的 PASS/FAIL 必带
  `exit_code`（integer 0–255），被杀死的进程没有 exit code，编一个正是该 schema 自己写明禁止的
  "invent evidence"；schema 属 E2 冻结面，故走 E2 的「take the in-boundary fix and record why」，用户当场裁 `SPEC_GAP`。
  **披露的残缺**：(i) `run_all` 全仓**零调用者**（M2 修的是 N1 设计好但产品路径尚未接线的 API 面，本轮不改变
  任何运行时行为——与 C0 发现 CLI 还停在 v1 路径同源）；(ii) M3 的 RED 阶段只拿到 AttributeError（常量尚不
  存在），其**行为**证明只来自 mutation 探针；(iii) 本轮不碰
  `tests/document_harness_review/test_run_v2_template_fulfillment.py`，C0 那条残留 low 仍留在下一批碰该文件的轮次。
- [x] 6. **Phase C2 — flow/summary 组**（一轮）：M5 + M6 + M7。**开轮前须知（2026-07-29）**：Phase C1.5
  （[`harness-digest-narrowing`](harness-digest-narrowing.plan.md)）插在本步之前，它把 digest 收窄到三类保护
  文件。**因此缺陷表给 M6/M7 写的「加 path+digest 交叉核对」已经过时**——C1.5 之后只有 `review_refs`
  （指向保护集里的 review 记录）值得核内容，其余 ref 的 digest 交叉核对已无意义。**M5 不受影响**
  （`check_repair_decision` 的绑定走 commit，与 digest 无关）。C2 开轮时须向用户重新确认 M6/M7 的形状。
  → **CLOSED 2026-07-30**：开轮 cold read `v3-cold-read-ae4df09.md`（提交 `853fe4c`，0 must-fix，顺带清偿
  `a6b87ad` 层内 read 欠账）；用户三裁决记录于 journal 与候选 commit 正文（read=dispatch / **M6=B**：只对
  在手 reviews 做 review_refs 内容绑定、其余 6 类 ref 有意不核，理由写在检查点 / **M7=按缺陷表原形状**，
  digest kind=canonical 依 w1-r1 授权先例）；候选 `86533f2`（10 个新断言先红后绿、既有测试零破坏、五套件
  29/20/39/169/338 绿 + repo-audit 0、4 个新守卫 mutation 探针值级红、证据贴在
  `document-harness/journal/c2-2026-07-30.md`）→ FULL 记录 `5499e4f` **`REVIEWED_NO_BLOCKER`，零 blocker，
  修复与 VERIFY 预算未动**。3 条 observation 均 non-blocking：O-1（generate 侧 candidate_ref 仍原样存，
  类由 check_summary 既有 CANDIDATE-BINDING-MISMATCH 兜住，搭下批碰 `generate_summary` 的轮）、O-2
  （REPAIR-BINDING-UNVERIFIED 双触发点，两处均有独立测试）、O-3（组件积累数据点 → 已排定的保障面二期复盘）。
- [x] 7. **Phase C3 — 产品入口组**（一轮）：M8 + M9 + M10。→ **CLOSED 2026-07-30**（实际只剩 M9——
  M8/M10 已由 C0 完成）：开轮 cold read 按 `E10` 引用覆盖（八成员 blob 自 `ae4df09` 未变，derivation 在
  journal `c3-2026-07-30.md` 与候选 commit 正文；未派 read、零预算）；候选 `71d43be`（模板加 REPAIR_ROUND
  分支、拒绝不完整 review 集、吸收候选装配依 w1-r1/p3-corr 两个 worked precedent；13 个新断言先红后绿、
  五套件绿 + repo-audit 0、5 个 mutation 探针全值级咬住——含真 `check_verify_outcome` 把回放的原缺陷形状
  当场打回）→ FULL 记录 `0576322` `REVIEWED_NO_BLOCKER`（零 blocker，修复与 VERIFY 预算未动）。1 条 bank
  形 finding **F-1**（`digest_ref_of` 对 digest-protected 的 `work_spec_ref` 丢弃在手保护 digest 改现算，
  "六 ref 全 path-only"的前提对该字段不成立；入 HARNESS-RIDERS `F-1c3`，兑付=下一批碰 `run_bind_v2.py`
  或 digest policy，O-2 fixture 随修）；O-1（round-1 `DISCLOSURES` 空默认无提示，同 F-4 等真 run 类）
  无本轮动作。`--emit` 链无测试、评审记 UNVERIFIABLE（F-4 同类披露）。
  **2026-07-30 追记：F-1 banking 被用户翻案，fix 腿激活**（`E9` 判据 = 有效 FULL 已发生，closeout 不灭它）：
  fix `V3-PHASE-C3-FIX-v1` 修 F-1（`digest_ref_of` 沿用在手 authored digest，mismatch 时 `AssuranceFault`
  拒绝——M7 同款"两样在手即对账"）+ O-2（fixture 补真 digest）+ riders 档头三条收紧（点名目标 / 最晚兑付 /
  closeout 天平，用户裁 2026-07-30）；`F-1c3` 行同 commit 删除兑付。VERIFY 已回：`REVIEWED_NO_BLOCKER`
  （记录 `f0e5d64`，0 blocker 0 finding，3 observation——O-1v noted 不入 bank / O-2v wording 级 /
  **O-3v 归用户**：actor-binding 惯例在 `E10` 层外累积，要不要收编入层，已挂 ledger 未结问题槽）。
  **C3 预算三格用满（一 FULL + 一 fix + 一 VERIFY），彻底 CLOSED。**
- [x] 8. **Phase C4 — #8 机械化**（独立一轮）：M11 + 新 schema 文件（README 枚举守卫会强制登记行）。
  → **CLOSED 2026-07-31**：开轮 cold read 按 `E10` 引用覆盖（八成员 blob 自 `784e49b` 未变，零预算，
  推导在 journal `c4-2026-07-31.md` 与候选 commit 正文）；候选 `d50d9e5`（`paragraph_skeleton` +
  `paragraph-map.schema.json`（第 15 个 pack 文件，classification 挂条目、平行数组不可表示）+ gate
  三向核对 + `make_paragraph_map.py`；三个缺陷实例修复前在旧 gate 值级放行（exit 0）、修复后全拒；
  12+14 新测试、六 mutation 探针值级咬住并按 sha256 快照还原；五套件 29/20/39/181/368 +
  repo-audit 0；README 登记行走 `E10` 延后通道）→ FULL 记录 `v3-review-full-d50d9e5.md`（提交
  `ce5196c`）`REVIEWED_NO_BLOCKER`，零 blocker 零 low，修复与 VERIFY 预算未动——reviewer 重放 RED、
  自跑四探针、实跑 pinned-revision 分支。W-1 wording 级按 `R9` 随层文本下批（ride 已由 `E10` 延后债
  排定）；O-1 分类分歧设计问归用户（入 ledger 未结问题槽）；O-2 anchor 子串语义先在；O-3 组件积累
  数据点入保障面二期复盘。**M1–M11 至此全部关闭。**
- [x] 9. **Phase D — 历史层退出 + memory 迁移**（一轮）：`rsc.py` 的 `stage` / `harness` 子命令加 deprecated/historical 标记（注册点：`rsc.py:539` `harness_cli.register(sub)` → `rsclib/harness/cli.py:66`；**不删码不删测**）；`General-Harness-v2-Design.md` 加 superseded banner 移入 `migration/general-harness-v2/` 提交；memory 逐 atom 分类（operative→仓库 / preference→留 memory）并迁移 operative 的（cold-read charter→checklist 或 dispatch 说明、session-role/review-priority→checklist 行、craft lessons→指向 records 的指针）——**用户裁决 2026-07-27：`feedback-subjects-before-argument`（subjects-first + 答题四段式）也在迁移范围内，此处一并从 memory 变成 harness 的一部分（怎么向用户解释是 harness session 的 operative 行为，不是纯 preference）**——关闭 `issue-p3-corr-harness-knowledge-in-memory`；为三条未 triage 的 issue（channel / burden / knowledge-in-memory，均在 `assurance/runs/p3-corr/issues/`——Phase B 后的新路径）补用户 ISSUE_TRIAGE 决定（rationale 指向本 plan + ledger 裁决）。
  → **CLOSED 2026-08-01**：开轮四裁决（① cold read 用户 waive、收口 read 一次清偿 ② rider CT/F-d 提前兑付 + F-3r 到期 ③ session-role 入 `E1` 一句、memory 两 atom **整删不留指针**（用户收紧「memory 不算 harness 部分」；subjects-before-argument 已由全局 §0.5 于 2026-07-28 接管，残留为 preference 合规）④ channel triage = `CORE_CANDIDATE`）；候选 `34cf85b`（historical 标记 / `check_triage` TARGET-MISMATCH 守卫红→绿 / dispatch producer CLI 测试 / 决定文件 / E1 句 / W-1 ride；riders CT·F-d·F-3r 同 commit 删）→ FULL `766fe02` `REVIEWED_NO_BLOCKER`（零 blocker；L-1 wording no-action，L-2 用户裁「顺带做」）→ L-2 byte-channel 套用 `d01615b`（run 维度守卫，零预算无 VERIFY）→ 收口 layer read `b22eca4`（0 must-fix；一次清偿五笔：C4 延后 README 行 + schema descriptions + E1 amendment read + W-1 的 read + waived 开轮 read 补足；**层成员自此 9 条**）→ read L-1 套用 `ace0845`（`layer_path_check.py` LAYER 补第 9 成员，红→绿即探针）。**fix/VERIFY 预算未烧**。triage 决定 knowledge-in-memory + channel 在库；burden 按 Step 10 等 Phase E 材料。
- [x] 10. **Phase E — 真实小任务 + 重测**：用户挑一个小文档任务（论文侧优先），从 START 到 CLOSED 跑完整 happy path，**不许手抄历史脚本**（缺什么当场见证、当场裁）；用诚实口径记负担（时间/轮次/人工文件数与行数/评审行数 vs payload），对照 N3 旧口径（锚见 Context 末行）写短对比；把 measure.py 口径缺陷记进 burden issue 的关闭材料。
  → **CLOSED 2026-08-01（= Stage 2 run `p4-bridge`，裁 B 并入）**：START→CLOSED 全链真跑（audit×3
  含 2 轮 SPEC_GAP 修订 → START `d10bcf7` → candidate `7b79f14` → evidence `8e2ab26`（11/11 checks，
  含 governance-scan + merge-base 两个 command_exit 首跑）→ FULL `REVIEWED_NO_BLOCKER`（1 次回件
  form 修正，零 blocker，repair 未用）→ FINAL ACCEPT → promotion `728eadd` → successor 签署
  `f7a6bed`，P4-IMPL-v1 effective）。四义务：① 零手抄（5 个 run 脚本 fresh + 模板按 README 实例化；
  缺口见证 4 条 HarnessIssue，含 E9 guard 词表不认产品 ReviewResult JSON）② 负担对比表在 closeout
  commit 正文（N3 口径 authored 12,472 B = **129%** of payload 9,688 B vs N3 锚 17%——规模效应；
  measure.py 四条口径缺陷记入 burden 关闭材料）③ F-4 兑付、rider 行同 commit 删 ④ O-1 两行
  （review record §3 + closeout commit，均标 same-source）。burden ISSUE_TRIAGE 决定草案已交
  用户，签字后落 `runs/p3-corr/issues/` 并跑 `check_triage`。
  → **2026-08-01 用户裁 B（并入，不再单独执行）**：**Stage 2 (P4-ACTIVATION-BRIDGE) 复开，其首个真 run 即本步的「真实小任务」**。依据：对象同类——两者都是同一台 v3 机器上的 document-work run（同 WorkSpec/评审/CLOSED 链、同指令层、同 gate），规模/题材是参数不是类型；「论文侧优先」偏好作废（harness 初衷 = 工程件，Stage 2 即代表性负载；论文侧数据点已有 `w1-r1`）。本步义务**原样绑定**该 run：① happy path 缺口当场见证、当场裁，不手抄历史脚本 ② 诚实口径负担记录 + 对照 N3 锚 + measure.py 口径缺陷入 burden issue 关闭材料（burden ISSUE_TRIAGE 用该 run 材料）③ rider F-4 兑付 ④ C4 `O-1` 观察条款：该 run 的 review/closeout 记两 map 分类对照行。
- [x] 11. **收口**：Stage 2 是否复开 → 用户裁决；HARNESS-LEDGER 更新指针；本 plan 状态改 done。
  → **复开已裁（2026-08-01，裁 B）**：记录于 HARNESS-LEDGER NEXT 行与 `V3-STAGE2-REOPEN-RULING-v1` commit 正文。
  → **收口完成（2026-08-01）**：run `p4-bridge` CLOSED、Step 10 四义务核销（见上）、两级 ledger 指针
  已指 Stage 3 (P4-CODE)。本 plan 记 **done**——唯一后置件 = burden ISSUE_TRIAGE 决定文件（用户签字
  即落盘，格式先例 p3-corr，`check_triage` 三维 clean 后本行不再欠任何东西）。

## Acceptance (done = ?)

- 全 suite 绿 + repo-audit exit 0 + 冻结面完整复核（三 blob + N0 schemas 既有字节 + 两个 oracle 逐字节不变）——每轮验，收口再验。
- M1–M11 各有一个**曾经红过**的负向测试在套件里（M4 的红即引号绕过复现）。
- `generated/` 下不再有 authored 的 **run/证据文件**（剩余两个目录 README 是说明文件，不在 E1.3 的 research-content 口径内）；`ResearchSystem/assurance/` 结构完整，两个 closed run（p3-corr / w1-r1）字节原样；三个搬迁测试模块绿。
- 两份旧 contract = 5 行 stub（原路径保留）；CONSTRUCTION-CHECKLIST.md **承载每一轮真正用得上的源义务，由独立 read 验证**（2026-07-28 用户裁 **(a)**：行数上限作废——它量的是「写出来的面」，而 banner 把 `7011916` 的 683 行定为存疑时的准据，管着的面是两者之和；且 ≤50 只被从未生效的 49 行草稿满足过一次）；bank 清空；REVIEW.md 只含 commit-bound 流程；dispatch fixture 逐字节未动。
- 三条 issue 有 ISSUE_TRIAGE 决定文件且 `check_triage` clean；memory 里不再有 operative harness 指令（preference 类保留）。
- 首个真 run（2026-08-01 裁 B：= Stage 2 P4-ACTIVATION-BRIDGE 的 run）达到 CLOSED（或诚实 STOPPED_REPLAN + 见证清单）；负担对比表落在 run 记录或 ledger。
- 每轮有独立 review/read 记录，按 Step 2 定死的 channel 与命名。
- Step 11 完成：Stage 2 复开裁决已记录（无论裁向哪边），ledger 指针指向下一步。

## Resume pointer

当前指针（2026-07-30 五次更新）: **Phase A / B / B2 / C0 / C1 / C1.5 / C1.6 / C2 / C3 CLOSED；其后插入的
2026-07-29/30 修理批（reform 轮）、挂账清算与 supersession-2 签字批亦全部 CLOSED**（状态与裁决见
`ResearchSystem/HARNESS-LEDGER.md`；轮次记录 `v3-review-full-8ec4c60.md` / `v3-review-verify-49d9829.md`
+ 三次 layer read `451e8b0` / `d58969d` / `403fc9a`）。修理批落地：churn 三防线（E10 免费通道收窄 /
E3 断言先证伪 / 规则零理由）、E9 判决未回冻结 + 三个 tracked pre-commit guard、`dtw dispatch --read`
第三家族 + freeze marker、journal / HARNESS-RIDERS 记录件、cold read 按成员 digest 覆盖。**旧指针的两笔
欠账已清**：`f453369` 未审字节与 `supersession-2` 欠的 read 均由三次 layer read 清偿；原「给 E10 加
amendment-read 出口的独立轮」被 reform 轮的 digest 条款取代，**不再单开**。`supersession-2` **已签**
（2026-07-30，blob `e1a2f26b…`，记录 `migration/document-work-assurance-v3/supersession-2-signature.md`）。
bytes-channel (a) 全开（ledger 已裁行；E10 条款文本挂 rider `BC-1`）。**C3 已闭（2026-07-30）**：cold read
引用覆盖（八成员 blob 未变，零预算）→ 候选 `71d43be` → FULL `0576322` `REVIEWED_NO_BLOCKER`（零 blocker，
修复/VERIFY 未动——**后经用户翻案动用 fix 腿并 VERIFY 收官，三格用满**，追记见 Step 7；C2 链见 Step 6）。
Layer 收编轮已闭（2026-07-31，独立 plan `harness-layer-incorporation-round.plan.md`）；**Phase C4
亦已闭（2026-07-31，见 Step 8——M1–M11 全部关闭）**；**Phase D 亦已闭（2026-08-01，见 Step 9——
FULL 零 blocker，两 low 均 byte-channel 当场偿清，fix/VERIFY 未烧；层成员自此 9 条）**。
**Stage 2 run `p4-bridge` 已 CLOSED（2026-08-01，见 Step 10 闭包）：successor 已签、P4-IMPL-v1
effective、四义务核销、本 plan done**——唯一后置件 = burden ISSUE_TRIAGE 决定文件（用户签字即落盘）。
下一步归 reactivation plan：**Stage 3 (P4-CODE)**。C1 的轮次链见 Step 5；C0 见 Step 4.6；B2 见 Step 4.5。

以下为 Phase A 当时的历史链，保留不改：**Phase A 完成**。链：`820b287` 收缩 → `3743849` read → `cf8e1b1` 修复 → `1ddece7` read → `aa72c82` 收口 → `4ba5e95` read → `377d591` 刹车 → `abe44f0` read → 本更正批（全部在 instruction layer 外或按 R9 顺次带走，**不欠新 read**）。刹车经 read `377d591` 判定装对（其 2 条 must-fix 均不在 R9 管辖内，5 条 low 中 3 条被 banked 顺次带走）。**Phase B 已落 + FULL `CHANGES_REQUIRED` 已修复**（候选 `2687d8c` → FULL 记录 `3ca107a` → 修复批次）。FULL 抓到的是**活产品被搬坏**：run-v2 模板三个脚本的 `parents[]` 下标与 README/CONTROL_ROOT 旧路径——套件当时看不见（无测试读这些文件）。修复同轮补了守卫 `test_run_v2_template_usable.py`（四种 mutation 全咬住），suite 432→437。38 个 frozen 脚本按用户 2026-07-28 裁决**不动**，`assurance/README.md` 说明之。VERIFY `REVIEWED_NO_BLOCKER`（记录 `fb6c20b`）；其 V-1/V-2 与用户当日裁决在收口轮落地：repo-audit 的行内代码剥离收窄到只服务 markdown 链接扫描（此前误伤 wikilink 29% / fragment-ID 10%，四路 mutation 覆盖全部三个消费者），模板守卫砍掉重复响故障的 import 两条、只留防静默写错目录的三条，废计数从 plan 与 `assurance/README.md` 删除。末批：17 个 issue 文件里的 evidence_ref 路径改到新家（16 条恢复解析、digest 逐条吻合；一条 mismatch 是 Phase A 退役 contract 的遗留，路径可解析、字节确已变，不修）；模板守卫整个删除（一次性搬迁不属于会复发的缺陷类，V-2/V-4 随之消失），suite 回到 432、**本轮净增测试 0**。**Phase B CLOSED。下一步 = Phase B2（Step 4.5）的 preview card。** 待用户裁：两条未 banked 的 low 残留（E2 新句伸进 E8 的边界口径 / banner 把沉默指向 R9 而 R9 会把有后果的沉默判回来）——修它们要碰 checklist、要再欠一次 read，故留待你裁。

## Notes

- **行数验收已作废（用户裁 (a)，2026-07-28）**：checklist 的实质判据写进 Acceptance；行数量的是「写出来的面」，而 banner 把 `7011916` 定为存疑时的准据，所以它从来没量对过要量的东西。三轮的行数轨迹随本条一并删除——它没喂给任何决定。成因仍记：≤50 是压缩前的猜测，而 `820b287` 的 read 找出 12 处源义务在压缩中丢失，复原必然涨。
- **MF-4 裁决落地（用户 2026-07-28）**：`contract_provenance_check.py` 删除，不 retarget；README Local-enforcement 行同批收窄。机器本地 pre-commit hook 未动（`if [ -f ]` 存在性守卫自动跳过）。
- 审计原文只存在于 2026-07-27 的对话里；其可复用结论已全部转写进本 plan 与 ledger 裁决，执行不需要原文。
- 本 plan 经独立 review agent 对抗审查（同日）：修正了"活代码引用 0"（假——pathlib 分段拼接骗过字面 grep）、补了 dispatch-fixture 与契约退役的碰撞解法（stub 保路径）、review 侧治理归属、bank 清偿、冻结面全集、M1 行号（395→262）、M4 由推定转实证。教训：**字面 grep ≠ 引用面**，分段拼接、变量拼接都要用分段词 grep 复核。
- ⑤ 轮的教训随身带：并排数组是对齐税；"derivability is not a reason"（每张 preview card 首行写买到什么）。
- 执行者注意：一个 session 一个角色；review 由用户路由到独立 session；不要在执行 session 里自审。
