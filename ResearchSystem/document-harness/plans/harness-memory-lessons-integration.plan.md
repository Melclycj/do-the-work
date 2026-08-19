# Plan: Phase B2 — memory 里的经验接进 harness

- **slug**: harness-memory-lessons-integration
- **created**: 2026-07-28
- **complexity**: 中等
- **status**: Step 0–6 全部闭合（read `ff05ea3` 已回、修复批次 `079361f` 已落、memory 迁移已执行）；**剩 Step 7：回父 plan Step 5（Phase C1）**
- **base_commit**: cf51534
- **base_branch**: document-work-assurance-v3
- **parent plan**: [`harness-deletion-first-stabilization`](harness-deletion-first-stabilization.plan.md) Step 4.5（本文件是那一步的展开；父 plan 的 Step 5 起不受影响）

## Goal (one line)

把 Claude memory 里那些 **operative** 的构造侧经验，变成 `CONSTRUCTION-CHECKLIST.md` 里有仪器的规则，或者判定它不该存在——因为写在 memory 里的经验，模型不会自动照做。

## Why / value

**起因是实证，不是主张。** 2026-07-28 的 Phase A+B 里，执行者的错误清单如下，右列是它违反的、**当时已经写在 memory 里**的条款：

| 错误 | 违反的既有条款 |
|---|---|
| 搬家前只 grep 了 `tooling/`，没 grep 被搬的树本身 → 活产品被搬坏 | `v3-review-craft-lessons`「枚举型主张必重推」 |
| commit 写「joined form 残留已扫干净」——那次 grep 范围窄于声明 | `feedback-prose-claims-derive-or-omit` |
| 「16 文件 / 46 处」把模板 README 数进去、又整批当历史散文放过 | 同上「枚举型主张必重推」 |
| 「38 个脚本坏」实为 36，且据此否掉了正确的 reviewer | 同上 |
| 「四轮里三轮是修上一轮」——数字从上一份记录搬运，未重推 | 同上 |
| 改 repo-audit 只探了 3 个消费者里的 1 个，commit 却写「已证明没削弱」（**第二次**，就发生在修第一次的那个 commit 里） | `feedback-prose-claims-derive-or-omit` |
| `evidence_ref`（第三条引用通道）从未被核 | `feedback-thesis-change-impact-pass`（改动后 grep reverse-deps） |
| 三个 Edit 并发打同一文件 → 写竞争产生重复句 | 全局 CLAUDE.md §4.5（同文件并行禁止） |
| ledger 指针**连续两轮**落后（改了 plan 指针忘了 ledger） | 无对应条款——新的 |
| 给一次性目录搬迁配永久守卫，并替它辩护两轮 | `E6` 有近似表述但没咬住——候选新规则 |

**结论**：知识在 memory 里 ≠ 知识生效。它要么成为 checklist 的一条规则（有仪器、进 read、被 reviewer 读得到），要么就该判定不存在。

同时关闭 HarnessIssue `issue-p3-corr-harness-knowledge-in-memory`（原挂 Phase D，用户 2026-07-28 移到此处并加宽）。该 issue 的原文诉求是**托管**问题：operative 知识在仓库外，`instruction layer` 的封闭枚举是仓库路径，所以规则 1 覆盖不到、reviewer 读不到、没有任何 blob 绑定。本 plan = 该 issue + 上表的**有效性**证据。

## Context to resume cold

- **治理文本**：`ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md`（E1–E12 执行侧 / R1–R9 评审侧）。两份旧 contract 已是 5 行 stub，全文在 `7011916`。**checklist 是 operative 规则集，不是完整替代**——它没说的地方以 `7011916` 为准（banner 已写）。
- **memory 目录**：`C:\Users\j3236\.claude\projects\D--Thesis\memory\`，索引 `MEMORY.md`。
- **候选 atom（构造侧 operative）**：`v3-review-craft-lessons` / `feedback-prose-claims-derive-or-omit` / `feedback-derivability-is-not-a-reason` / `feedback-guard-expectation-independence` / `feedback-thesis-change-impact-pass` / `v3-session-role-separation` / `v3-review-priority-implementation-correctness` / `v3-cold-read-charter-template` / `feedback-subjects-before-argument` / `feedback-concise-reporting`。
- **预判已被 checklist 覆盖（判定时复核，覆盖则直接判掉不重复写）**：guard-expectation-independence → `E5`；session-role → `E1`/`R1`；review-priority → `R3`。
- **轮次纪律**：preview card（E11）→ 用户确认 → 改动 → suite + `python Thesis/Work/Tooling/repo-audit.py`（**从仓库根跑**）+ 冻结面复核 → commit `V3-<轮名>-v1` 单行标题 + 一段正文 → `python ResearchSystem/tooling/dtw.py dispatch --range <base>..<tip>` → **用户路由**到独立 session（2026-08-16 前是 `rsc.py v3 dispatch`；六个命令由拆分批 R2 摘成 harness 自己的入口）。
- **记录渠道（R6）**：review session 在 worktree 写 `v3-checkpoint-read-<sha>.md`；execution side 提交，标题 `V3-REVIEW-RECORD-<轮>-<sha>-v1`。
- **冻结面**：signed plan blob `8ad404b1` / contract `b2dbdf75` / supersession-1 `68031fa2`；N0 schemas 与 `ResearchSystem/contract/` 既有文件；两个 user-locked oracle（`tooling/tests/fixtures/expected-construction-prompt.txt` + `tooling/tests/document_harness/test_readme_enumeration.py`）——**动它们须先经用户本人**。
- **状态**：Phase A / Phase B 均 CLOSED。工作区状态自己跑 `git status --porcelain`；`ResearchSystem/docs/` 未跟踪，Phase D 处置，别碰。

## Constraints / Out-of-scope

- **改动合并成一次** instruction-layer 修订，走**一次** read；不逐条开轮（这正是被 R9 终止的递归形状）。
- 每条新规则必须能回答：**它缺席时哪个决定会变**（E6）。答不上来就不写。
- **不为一次性事件配永久机械**（守卫那轮的教训）。
- OUT：Phase C 的 M1–M11 代码修复；Stage 2；`Knowledge/` 与论文侧任何内容；把规则写进全局 `~/.claude/CLAUDE.md`（用户 2026-07-27 裁：全局不动）。

## Steps

- [x] 0. **等用户提供他自己的思路**（用户 2026-07-28 明示："关于怎么改我还要提供我自己的思路"）。**这是硬坎——收到之前不要开始设计规则文本，也不要渲染 preview card。** 收到后把它记进本文件 Notes，再进 Step 1。→ 2026-07-28 收到，原文摘要见 Notes §用户思路；它把本 phase 的净产出压到四件事。
- [x] 1. 逐个候选 atom 判定：**已覆盖**（指出是哪条）/ **需新增**（写出它缺席时哪个决定会变）/ **属 preference 留 memory**。产出一张判定表。→ 见下 §判定表，每行的"已覆盖"都经本轮 grep/读原文复核，不采信预判。
- [x] 2. 需新增的合并成一次 checklist 修订。渲染 preview card 等确认。→ 卡经两次收窄后批准（见 Notes §轮次形状裁决）；落 `E3` 追加一句 + `R3` 插入一句，**净新增可执行字节 0**。同批带 R9 rider：两份退役 stub 的 `R1–R8`→`R1–R9`。
- [x] 3. **C 规则落地**：commit body 与记录只留 **digest 类身份证明**，不写描述性计数；判据同上。（用户 2026-07-28 裁「要做」，并指定放在本 phase 而非单独写。）→ 即 `E3` 的追加句；用户思路定的完成标准是「按字段处理、不加全局词汇禁令」，故它点名 counts / digests / path enumerations / worktree state 四个字段与 omit 一臂，不禁任何词。
- [x] 4b. 关闭 `issue-p3-corr-harness-knowledge-in-memory`：补 ISSUE_TRIAGE 决定。→ `user-decision-triage-harness-knowledge-in-memory.json`，route **CORE_CANDIDATE**（用户 2026-07-28 裁），`check_triage` clean。
- [x] 4. operative atom 迁出 memory（preference 类留下），`MEMORY.md` 索引同步。→ 已执行，见下 §Step 4 的落地记录。**用户 2026-07-28 裁：memory 侧不需要 review，read 过后一次直接改完——不开轮、不吃 FULL、无 commit 仪式**（memory 不在版本控制里，reviewer 本来就看不见它）。清单见 §判定表：删 8 / 改写 3 / 修 `goals-ledger-entrypoint` 里 1 处指向已删 atom 的 wikilink / `MEMORY.md` 24→16 行。
- [x] 5. 轮记录里附「上表：错误 → 违反的 atom」，作为该 atom 值得成为规则的证据。→ **不新造记录文件**：该表已在本 plan §Why 且已随 `604ee27` 提交，commit body 指向它的位置而不复制——复制正是本轮 `E3` 新句在禁的形状。
- [x] 6. suite + audit + 冻结面 → commit → dispatch → **用户路由 read**。→ amendment commit `a8113d4 V3-PHASE-B2-AMENDMENT-v1`；本条 tracker 行与指针**随后单独提交**（pre-submission correction——`E9`：本轮尚无独立 FULL，故不消耗预算），dispatch 的 range base 是 `604ee27`、tip 是该 tracker commit。验证输出见 §本轮验证。**在此停下等你路由 read。**
- [ ] 7. 过读后回父 plan Step 5（Phase C1）。

## 判定表（Step 1 产出）

每行的「已覆盖」都在 2026-07-28 对 `CONSTRUCTION-CHECKLIST.md` 原文复核过，不采信 Context 段的预判。

| # | atom | 判定 | 依据 / 落点 |
|---|---|---|---|
| 1 | `feedback-derivability-is-not-a-reason` | **已覆盖** | `E6` 逐字含两半（"what decision changes if it is absent" + "A fix that requires new machinery is the signal to re-question the guarded thing"）。全仓该措辞的规则实例只有 E6 一处；两份 plan 里是**引用 E6**，不是副本 → canonical owner 单一，确认后不再复制 |
| 2 | `feedback-guard-expectation-independence` | **已覆盖** | `E5`（expectation 独立：hand-written literal 或 committed fixture，禁 module 自己的常量；断言整行）+ `E4`（mutation：neuter→red→sha256 校验还原，禁 `git checkout --`；must-fire 配 negative control）。机械面在位：`tooling/tests/fixtures/expected-construction-prompt.txt` 是独立 golden 文件，`test_the_prompt_is_exactly_the_golden_file` 整体 `assertEqual` |
| 3 | `v3-review-priority-implementation-correctness` | **半覆盖 → 净新增一句** | 阻塞门槛那半已在 `R9`（"changes no actor's action — no check outcome, no permission, no obligation, no verdict path"）；**优先级排序那半仓内不存在**（`document-harness/` 里 implementation-correctness / priority 零命中）。缺席时变的决定：reviewer 把读的深度花在流程面而非实现面，且 `R3` 的「不得 inflate」失去它的因 |
| 4 | `feedback-prose-claims-derive-or-omit` | **半覆盖 → 净新增一句（= C 规则）** | `E3` 已有 "paste tool output, never describe it from memory"，但只管**数字**，缺 omit 那一臂，也没点名 enumeration / worktree state。缺席时变的决定：commit body 与记录继续写没有命令支撑的 characterization（本 session 两次「已扫干净 / 已证明没削弱」即此类） |
| 5 | `feedback-thesis-change-impact-pass` | **留 memory**（用户思路未裁，我方判定） | 论文侧规则（`Thesis/` 树），机械面是 `repo-audit.py` + pre-commit hook。harness 侧残余（字面 grep ≠ 引用面）由 E3 新句吸收——不许声称「已扫干净」除非跑过建立它的命令 |
| 6 | `feedback-concise-reporting` | **留 memory** | 纯沟通偏好；「多短算简洁」无仪器，进 harness 只会产出格式 finding。不进 EXECUTION / REVIEW / schema / acceptance |
| 7 | `feedback-subjects-before-argument` | **留 memory，但改写** | 软偏好（先列 subject 再论证）保留；**删掉 atom 自带的「2026-07-27 裁：Phase D 迁入 harness」段**——被 2026-07-28 裁决取代；四段式 / 强制表格 / 每 verdict 必重跑命令 / 恰好一个 recommendation 降级为建议（它们与 concise-reporting 直接冲突） |
| 8 | `v3-harness-operating-contract` | **留 memory，但改写** | 它本身是 bootstrap pointer，不是 contract。现文把两份 contract 描述成活的——**已失实**（Phase A 退役成 5 行 stub）。改写为 non-authoritative 指针，指向 `CONSTRUCTION-CHECKLIST.md`。**不改名**（E6 自检：改名不改变任何决定，description 已承载真相） |
| 9 | `v3-session-role-separation` | **留 memory，但裁剪** | role invariant 归 `E1`/`R1`，memory 不重述；只留 session mis-routing 提醒与「让用户路由」的协作偏好 |
| 10 | `v3-cold-read-charter-template` | **退役（删）** | 第二份 shadow WorkSpec。已核实替代面在位：`rsc v3 dispatch --range BASE..TIP` 生成 construction 轮 reviewer prompt，charter 指向 canonical role 文件，且被冻结 golden fixture 守住 |
| 11 | `v3-review-craft-lessons` | **退役（删）** | 枚举重推归 `R2`（"every number you re-derive from the repository yourself; accept no reported figure"）+ E3 新句；Windows 还原纪律归 `E4`；间接构造盲区已在测试里。历史留 review record，不留压缩版 craft doctrine |
| 12 | `v3-ledger-lives-in-the-node-record` | **退役（删）** | 自标 HISTORICAL；ledger/router 分拆后路径与状态描述已失效 |
| 13 | `w2-review-session-breakpoint` | **退役（删）** | 自标 HISTORICAL 且内部自相矛盾（前半 CLOSED、后半仍写「下一步待 sign-off」）；终态由 W2 record 持有 |

**净 checklist 变更 = 两句**（第 3、4 行），外加一条 rider：两份退役 stub 仍写 `R1–R8`，而 `R9` 在刹车轮已生效（`README.md:24` 当时已修、stub 漏了）。按 `R9` 它是 wording-level、顺下一批碰 instruction layer 的批次兑付——**本批就是那一批**（`E10` 明列 stub 属 instruction layer）。

## 本轮验证（Step 6，命令输出而非描述）

```
pytest -q (ResearchSystem/tooling)                      432 passed in 55.83s
python Thesis/Work/Tooling/repo-audit.py (仓根)          RESULT: clean (exit 0)
git ls-tree -r HEAD | grep <三个冻结 blob>
  8ad404b12b3242e700d0ad215048dffccada7d9c  .goals/plans/document-work-assurance-harness-v3.plan.md
  68031fa2ca31272e31da0d42a9a02189d28fcc21  ResearchSystem/contract/…-v3-supersession-1.md
  b2dbdf752d8c155e4c65b14b5f420b880b8184a1  ResearchSystem/contract/Document-Work-Assurance-Contract-v3.md
git rev-parse 604ee27:<oracle> 与 HEAD:<oracle>（正身份，不是空 diff——路径打错也返回空）
  ResearchSystem/tooling/tests/fixtures/expected-construction-prompt.txt
    604ee27 = HEAD = 5cf970c17ad509e7517f59fb9421a2de4cb9bd68
  ResearchSystem/tooling/tests/document_harness/test_readme_enumeration.py
    604ee27 = HEAD = 57cecbb0c467485b692308ebb13cc64dfeb630b7
```

**新 triage 决定的绑定**：证据是**重算 digest**——`sha256(目标 issue 当前字节)` 等于决定里 `harness_issue_ref.digest_sha256`。`check_triage` 也跑了（`ok=True, issues=[]`），但它核的是 phase / route 成员资格 / target path 存在 / `work_id` 相等 / schema，**不核 digest，也不核该 path 指的是不是被一起传进来的那个 issue**——read `ff05ea3` 的 L-4 用反向对照证明了：拿不相干的 issue 去核照样 `ok=True`（八个 p3-corr issue 共用同一个 `work_id`，唯一有区分力的字段在本 run 里没有区分力）。所以 `check_triage clean` 不是绑定的证据，重算的 digest 才是。

**Mutation 探针**（item ②「guard oracle 独立并有 red mutation」的证据；打的是**既有** oracle，本轮不新增守卫）：改 `dispatch.py` 里 `CONSTRUCTION_PROMPT` 的一句、**golden 文件一字不动** → `test_the_prompt_is_exactly_the_golden_file` 由 `1 passed` 变 `1 failed`；还原后 sha256 与基线相同（`106d99d8…`），再跑回 `1 passed`。

还原用的是 `git show HEAD:<path>` 的字节，**不是** `E4` 规定的 sha256 校验 scratchpad 副本。它这次安全**只因为** `dispatch.py` 在 HEAD 是干净的——这个前提 `E4` 的方法本身不需要，而当时的记录也没写出来。同样的捷径用在**本轮也改过**的文件上，会把本轮自己的改动静默回滚，而 sha256 仍然对着错误的基线通过。（read `ff05ea3` 的 L-2。）

第一次探针**是空的**（node ID 写错，control 就 `rc=4 / no tests ran`）——按 craft 纪律 control 先跑，所以当场看见而不是当成绿。这条留着：探针的价值全在 control 那一步。

## Read `ff05ea3` 的处置

记录：`ResearchSystem/migration/document-work-assurance-v3/v3-checkpoint-read-ff05ea3.md`（提交 `feb9bdd`）。判为 **read 不是 FULL**（`E10` + `R3` + 退役 review contract §12 的 `ADOPT_DOCUMENT_V3` 排期），**B2 的 FULL 未消耗**；本修复批次按 `E9` 的判据（尚无独立 FULL）是 **pre-submission correction，不消耗预算**。

| 项 | 处置 |
|---|---|
| **MF-1** `R3` 新句枚举里没有指令层，而它诞生的这一轮全是指令层 | **已修**：枚举改为 `the code, schemas, tests or instruction text`。机器复核（对 `604ee27` 基线做 word-level 最长公共前后缀）：`E3` +38/−0、`R3` +32/−0，`E10` 的「只增删、不重打」成立。reviewer 附的反读（该句位于 verdict 规则内、而 read 不带 verdict，故可争论它根本不约束 read）一并留档——它指向的是**该句的家在哪**，而家的位置是用户已裁的（并进 `R3`、不开 `R10`），不由执行侧翻案 |
| **MF-2** Step 3 按用户亲口否掉的标准打了勾 | **已裁 + 已修**：该 finding 对**记录**成立、对**交付**不成立。缺陷在那句话缺了条件——无条件读法会让同一份思路自相矛盾（item ③ 原文就是「**加入一条** implementation-first review priority」）。三项裁决：①不加"曾经是 X 现在是 Y"的叙事；②**直接 rephrase，把条件写进句子本身**，不另立判据盒子；③规则进 **checklist**，与本轮 memory 并入的那两句同处——两侧都读的地方。落地：Notes §用户思路 item 2 那句改为「修复或删改既有文本时…；引入新经验时，加上那条规则本身就是交付」；`E6` 追加一句「When a finding names existing text or code as wrong, the fix is that text changing; a rule added about it is not the fix.」**Step 3 保持关闭**，Step 4 可跑 |
| **L-1** 两个 user-locked oracle 的证据是「空 diff」且路径省略 | **已修**：改记 blob 正身份（两个 oracle 在 `604ee27` 与 `HEAD` 的 blob hash 各自相同），本 session 独立重算，未采信 read 记录里的值 |
| **L-2** `E4` 的还原方法被静默替换 | **已修**：记明实际用的是 `git show HEAD:<path>` 而非 sha256 校验的 scratchpad 副本，并写出它这次成立的前提（该文件在 HEAD 干净）与失效条件（用在本轮也改过的文件上会静默回滚本轮改动） |
| **L-3** front-matter `status:` 落后三步（`R9` wording-level，reviewer 判 banked） | **已修**（本批次正在碰这些文件，顺手兑付；`R9` 的 bank 保持空） |
| **L-4** `check_triage clean` 被当成绑定证据 | **已修**：证据改为重算 digest，并写明 `check_triage` 实际核什么、不核什么 |
| **Obs 1** 新优先级与 `R2` 排的是不同的轴 | 无需修 |
| **Obs 2** 规则范围枚举现有三份手工副本、无仪器 | 无需修；并入 park 的那条一起裁 |
| **Obs 3** `check_triage` 连 path→issue 同一性都不核 | 无需修；**并入已 park 的 digest 那条**（原 park 只说不核 digest，实际更宽） |
| **Obs 4** `R3` 插入尾部那行 108 字符 | 随 MF-1 重排消失（全文件最长行现为 96） |

## 补做批次（2026-07-28，用户对照原始规格后裁定）

用户把四段规格重新贴出、逐项对照，结论：**一 的 1、2 满足；一 的 3 部分；二 未满足**。两处补做，一批完成。

**① `R9` 的枚举漏了一格。** 规格 一.3 的第二句原文是「流程或文档差异只有在改变**允许的动作、证据绑定、义务、verdict 路径**时才阻塞」；我当时判"已被 `R9` 覆盖"而没加。逐词对：允许的动作=permission、义务=obligation、verdict 路径=verdict path 都在，**证据绑定没有对应项**——`R9` 那一格放的是 *check outcome*。两者不等价，且差别正命中本仓实况：**证据绑定可以断掉而所有 check outcome 全绿**（五个 triage digest 失效 + `check_triage` 不核 path→issue 同一性，就是这种）。按现在的字面，那类 finding 会被判 wording-level 而 banked。已补：`no evidence binding` 插入枚举，`R9` +3 词 / 删 0。**这次判错的成因写明：我用"意思差不多"结掉了枚举比对，而"枚举型主张必重推"正是本轮退役的那个 atom 的第一条。**

**② 删除臂。** 规格 二 的「无法可靠生成、又不影响决定的描述直接删除」，两个条件都满足才删。范围只扫**活文件**（两份 plan + `HARNESS-LEDGER.md` + `document-harness/` 指令层）；**历史记录一字不动**（Phase B 定下的规矩）。删掉的：

| 位置 | 原文 | 为什么两个条件都满足 |
|---|---|---|
| 本 plan §Context | 「工作区干净，除未跟踪的 …」 | 状态claim，冷 session 自己跑 `git status` 就有；改成指向命令，保留"别碰 `docs/`"这个真的喂决定的部分 |
| 本 plan §Why 表 | 「**16 个** `evidence_ref`…」 | 数字从上一轮记录搬运、本轮没重推；事实（这条引用通道从未被核）才喂决定，数字不喂 |
| 本 plan Step 1 | 「（**13 行**，…）」 | 数的是紧挨着的那张表，一眼可见；不喂任何决定 |
| 父 plan front-matter | 「4 高 / 5 中 / 4 低 / 4 冷启动缺口全部吸收」 | 那次审查的原文已不可再推导；吸收与否已由后续轮次证明，计数不喂决定 |
| 父 plan §Why 首句 | 「近 50 commit…+3494 / +2776；46 条 finding 只有 ~11% 是核心问题」 | **文件自己写着「审计原文已不可再推导，此处仅作动机记录」**——即它自陈不可生成且只作动机；决定（做 deletion-first）早已作出并记录 |

**保留没删的**（说明判据不是"见数就删"）：`MEMORY.md 24→16`、`432 passed`、blob hash、`E3/E6/R3/R9` 的增删词数——都由本轮命令产出且是某个结论的唯一证据；`EXECUTION.md` 的 "exactly one claim. Not zero, not two." 是**规则里的合法约束**，规格明令不要误杀。

**删除臂的覆盖率：不知道，没有分母。** 用户追问「涵盖了多少可以省去的手写事实」，诚实回答是**测不出来**：我做的是**一次手写 grep pattern 扫六个活文件**，删了上表五处。同一 pattern 在删后仍命中 40 / 19 / 13 / 0 / 1 / 0 行（两份 plan、ledger、README、EXECUTION、REVIEW）——但那些多数是合法保留（命令产出的数字、规则文本、引用的证据原文），而**命中行数不等于"可省去的手写事实"**，我自己写的 pattern 也无法确立它漏了什么。所以这里只登记做过什么，**不声称覆盖率**——声称它正是 `E3` 新句禁止的那类主张。

**一条自查出的记录缺口（chat-only，`R2` 判其为 finding）**：对话里我说过「那些数字的正解是删掉、改写成产生它的命令」，并给了理由「`R2` 明令 reviewer 不采信任何被告知的数，所以给评审侧看的数字本来就零价值」。核对仓库：`E3` 记的是 "emitted from the command that produces them **or omitted**"——**omit 那一半记了；「改写成命令」这个具体形状没记；R2 那条理由在仓里不存在**（全仓唯一命中是本文件判定表里对 `R2` 的引用，用途不同）。要不要把它变成记录，等用户裁——本批次不擅自加。

## Step 4 的落地记录（memory 侧，仓外）

**诚实边界先说**：`C:\Users\j3236\.claude\projects\D--Thesis\memory\` 不在版本控制里，所以下面的前后清单**就是**这次改动的全部证据——没有 diff 可看、没有 blob 可绑、reviewer 复核不了。这正是 `issue-p3-corr-harness-knowledge-in-memory` 指的那个性质，也是用户裁「memory 侧不需要 review」的前提。

**前**：24 个 atom / `MEMORY.md` 24 行。**后**：16 个 atom / 16 行。

**删 8**（内容已由仓内规则承接，或判为退役）：`feedback-derivability-is-not-a-reason`（→`E6`）、`feedback-guard-expectation-independence`（→`E5`+`E4`）、`feedback-prose-claims-derive-or-omit`（→`E3` 追加句）、`v3-review-priority-implementation-correctness`（→`R3` 插入句）、`v3-cold-read-charter-template`（→`rsc v3 dispatch` 生成，charter 指向 canonical role 文件）、`v3-review-craft-lessons`（枚举重推→`R2`；Windows 还原纪律→`E4`；其余留在各 review record）、`v3-ledger-lives-in-the-node-record`（自标 HISTORICAL，路径已失效）、`w2-review-session-breakpoint`（自标 HISTORICAL，终态由 W2 record 持有）。

**改写 3**：`v3-harness-operating-contract`（改成**标明 non-authoritative** 的指针，指向 `CONSTRUCTION-CHECKLIST.md`；不改名——`E6` 自检：改名不改变任何决定）、`v3-session-role-separation`（只留 mis-routing 与"让用户路由"的协作习惯，role invariant 引用 `E1`/`R1` 不重述）、`feedback-subjects-before-argument`（软偏好保留；删掉「Phase D 迁入 harness」的旧裁决段——被本轮裁决取代；四段式降为 "Useful, not required"，因为它与 `feedback-concise-reporting` 的强制表格/固定结构部分直接冲突）。

**留 2（harness 相邻但判为 preference）**：`feedback-concise-reporting`、`feedback-thesis-change-impact-pass`。其余 11 个是论文 / lab 侧，不在本 phase 范围。

**一致性检查（脚本双向跑，非目测）**：索引指向的文件全部存在、目录里的文件全部被索引（两个方向皆为 `none`）；悬空 wikilink 只剩 `research-operation-architecture.md` 里那个反引号包着的 wikilink 格式示例（双方括号里写着 slug 这个词本身）——那是示例不是链接，本轮未碰。**此处不复写它的字面形式**：repo-audit 的 wikilink 扫描按裁决不剥离行内代码，写出来会让 pre-commit 判红（本轮实测被拦一次）。修掉 1 处真悬空：`goals-ledger-entrypoint` 指向已删的 `feedback-derivability-is-not-a-reason`。

## Acceptance (done = ?)

- [x] 每个候选 atom 有明确判定（覆盖/新增/留），无一项悬空。→ §判定表 13 行，含用户思路未覆盖的 `feedback-thesis-change-impact-pass`（已单独裁）。
- [x] 新增规则在 checklist 里，且每条都写得出「缺席时哪个决定会变」。→ `E3` 追加句（缺席时：commit body 与记录继续写没有命令支撑的 characterization）、`R3` 插入句（缺席时：reviewer 把读的深度花在流程面而非实现面）、`E6` 追加句（缺席时：一次"修复"可以只加一条规则而被指出的文本原样留着）。
- [x] C 规则生效；此后轮次的 commit body 不含描述性计数。→ `E3` 的追加句即 C 规则。**边界**：它是规则生效，不是既有散文被清扫——按本轮裁决，"自由文本被替代或删除"是**修复/删改**场景的完成标准，引入新经验时加上规则本身就是交付。
- [x] memory 里不再有 operative 构造侧指令；`MEMORY.md` 与实际文件一致。→ 16 atom / 16 行，双向一致性脚本跑过（两个方向皆 `none`）。**证据只有前后清单**——memory 不在版本控制里。
- [x] `issue-p3-corr-harness-knowledge-in-memory` 有 ISSUE_TRIAGE 决定。→ `CORE_CANDIDATE`，`check_triage` clean（绑定的真证据是重算的 digest，见 §本轮验证）。
- [x] 一次独立 read 的记录在案（按 R6 命名与渠道）。→ `v3-checkpoint-read-ff05ea3.md`，执行侧提交于 `feb9bdd`，标题 `V3-REVIEW-RECORD-PHASE-B2-ff05ea3-v1`。
- [x] suite 绿 + repo-audit exit 0 + 冻结面逐项复核。→ 每个 commit 前都跑；最后一次：`432 passed`、audit `exit 0`、三 blob 原 hash、两个 oracle 在 `604ee27` 与 `HEAD` blob 正身份相同、`ResearchSystem/contract` 与 `ResearchSystem/schema` 在 range 内 0 改动。
- [ ] **未清**：`079361f` 的指令层字节尚未过独立读（`E10`）。不阻塞本 phase（Step 4 不依赖它），但 Phase C1 开轮前要清——见 Resume pointer。

## Resume pointer

当前指针: **Phase B2 做完。下一步是父 plan 新增的 Step 4.6（Phase C0 — M8 + M10），用户裁定「执行在新 session」——本 session 只改计划，不动代码。**

一条**未清的 `E10` 尾巴**，留给下一轮开轮时处理：修复批次 `079361f` 改的指令层字节（`R3` 的 MF-1 修正 + `E6` 新句）**尚未经过独立读**。`E10` 要求的是「在任何轮次**依赖**它之前」过读——Step 4 不依赖它（memory 删除的授权是 `E3`/`R3`，且用户已裁 memory 侧不 review），所以本 phase 到此可收；但 Phase C1 会在这层规则下运行，**开轮时要么先读 `604ee27..079361f`，要么由 Phase C1 自己的 FULL 一并覆盖**（B2 的 FULL 未消耗，read 与 pre-submission correction 都不吃预算）。read 之后：Step 4 的 memory 8 删 3 改一次改完，然后回父 plan Step 5（Phase C1）。 Step 0/1/2/3/4b/5 已闭合（判定表 + 三项裁决 + 轮次形状 (b) 见上）。三项已裁：净新增两句**并进 `E3`/`R3`**（不开 `R10`）；`feedback-thesis-change-impact-pass` **留 memory 原样**；triage route **CORE_CANDIDATE**。read 过后才做 Step 4（memory 8 删 3 改，一次直接改完，不开轮）。冷 session 接手时：先读本文件全文与父 plan 的 Step 4.5。

## Notes

### 用户思路（2026-07-28，Step 0 的硬坎输入）

用户把候选 atom 分成四类，并给出净产出：

1. **可提炼（3）**——`derivability-is-not-a-reason` 只留「移除它不改变任何下游决定就不要新增」，且**只需确认有一个 canonical owner，不再复制**；`guard-expectation-independence` 的落点是**测试 fixture + mutation test 而不是 doctrine 文件**，repo 已基本实现；`review-priority-implementation-correctness` 是**三项里唯一明确的净新增**。三项都**不迁**当时的事件经过、churn 叙事、Windows 事故复述。
2. **机械化而不是迁散文（1）**——`prose-claims-derive-or-omit` **按字段处理**：计数由版本控制生成、SHA/digest 由工具算、artifact 枚举由目录/schema 生成、clean/dirty 由命令返回、不能生成又不喂决定的直接删；**不加全局词汇禁令**（机械禁 all/only/every 会误杀合法约束）。**修复或删改既有文本时**，完成标准不是「加了一条 instruction」，而是被指出的那段自由文本真的被生成字段替代或删除；**引入新经验时**，加上那条规则本身就是交付。
3. **只留 memory（4）**——`concise-reporting`（无仪器，进 harness 只产格式 finding）；`subjects-before-argument`（只留软偏好，**删掉「必须迁入 Phase D」的声明**，四段式/强制表格不规范化——与 concise-reporting 冲突）；`harness-operating-contract`（是 pointer 不是 contract，标 non-authoritative，指向的东西被 Phase A 退役了就同步或删）；`session-role-separation`（只留 mis-routing 与转交提醒，role invariant 引用 repo owner）。
4. **退役或归档（4）**——`cold-read-charter-template`（典型第二份 shadow WorkSpec：hunt list 会与 WorkSpec 漂移、严格格式把展示偏好升级成 correctness 规则、路径与 branch 假设会过时；reviewer 启动输入应由 repo 的 dispatch 工具从 subject SHA + canonical role 文件生成）；`review-craft-lessons`（已机械化的留测试、历史留 record，**不保留压缩版 craft doctrine**；其「优先看 record/log prose」与 implementation-first 直接冲突）；`ledger-lives-in-the-node-record`；`w2-review-session-breakpoint`（不允许 breakpoint 继续被当当前工作指令加载）。

**用户给的收口句**：本 phase 最终只需处理四件事——保住一条价值 gate；保证 guard oracle 独立并有 red mutation；加入一条 implementation-first review priority；把可生成的 prose facts 机械化、其余删除。**其他内容不是继续扩写 harness 的理由。**

### 轮次形状裁决（2026-07-28，卡经两次收窄）

用户加的两条硬约束：**① dispatch 收在 Step 2 末尾**（`E10`：amendment 的独立 read 要在任何轮次依赖它之前完成；memory 删除的授权正是这两句，故不能同轮）；**② 一次性搬迁不允许 executor 出守卫**（守卫那轮的教训）——本轮 authors 零个可执行字节，唯一的 mutation 探针打在**已存在**的 golden-file oracle 上，用完按 `E4` 还原。

首版切成两轮后用户反问「为什么第一轮是 harness 侧增、第二轮是 memory 侧删改」。承认：两轮不是 plan 的形状，是我从上面两条推出来的，代价是 `R5` 要报的那个形状（加先落、删押后）且轮 2 的可评审面只剩一个 JSON。裁决 **(b)**：**一轮一 dispatch**——两句规则 + stub rider + triage JSON + plan/ledger 一起 commit 并 dispatch；memory 的 8 删 3 改在 read 过后**一次直接改完，不 review、不开轮**。理由：加与删记在同一轮的账上，而不可逆的那一步（memory 不在 git 里）排在验证之后。

### 本轮发现、未修（在轮边界外，待裁）

`assurance/runs/p3-corr/issues/` 里**五个既有 ISSUE_TRIAGE 决定的 `harness_issue_ref.digest_sha256` 全部与它们所指 issue 文件的当前字节不符**。逐 revision 复算钉住成因：`4440fa2` 原始字节 = 决定里存的 digest；`2687d8c` 纯改名，字节未变、digest 未变；`cf51534`（Phase B 末批，改 issue 文件里的 evidence_ref 路径到新家）改变了 issue 文件自身的字节，于是**指向这些 issue 的 digest 绑定全部失效**。末批的记录覆盖的是 issue 文件**里面**的 ref（「16 条恢复解析、digest 逐条吻合」），没覆盖**指向它们**的 ref。没有任何东西变红，因为 `check_triage` 只核 phase / route / target path / work_id，**不核 digest**（本轮已实跑：五对全 `ok=True`）。

两件事值得你裁：①这五个 digest 修不修（修 = 碰 closed run 的字节）；②`issues.py` 的模块文档把 HarnessIssue 声明为 *immutable once written*，而末批编辑了它们——是承认那次编辑是有理由的例外并记下，还是别的处置。本轮**不动**（轮边界是 instruction layer + 本 phase 的 triage 决定）。本轮新写的第六个决定绑的是**当前**字节，`check_triage` clean。

### 其余

- 本 plan 自身遵守 C 规则：上面的错误表只列条目、不给总数——数目会随发现而变，而它不喂任何决定。
- 反面教材就在手边：父 plan 的 Phase B 是「一次 `git mv`」，实际走了 6 个 commit、1 个 FULL、1 个 VERIFY、2 次修复、2 次删除。用户原话：「10 分钟的工作又做了两小时，所以我才要先提 B2」。
- 一条不修的已知状态：`issue-p3-corr-harness-knowledge-in-memory` 的 evidence_ref 指向 `v3-harness-operating-contract.md`，路径可解析但 digest 已不符——Phase A 把它退役成 5 行 stub 了。这是**可见的未验证**，不是缺陷；全文在 `7011916`。
