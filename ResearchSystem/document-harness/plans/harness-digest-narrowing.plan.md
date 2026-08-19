# Plan: harness digest narrowing — 把 digest 收窄到三类保护文件

- **slug**: harness-digest-narrowing
- **created**: 2026-07-29（同日经自检 agent 逐条取证后修订，见 Notes 末「修订记录」）
- **complexity**: 复杂
- **status**: CLOSED — C1.5 `REVIEWED_NO_BLOCKER`（预算未动）· C1.6 `CHANGES_REQUIRED` → 修复 → VERIFY `REVIEWED_NO_BLOCKER`（预算用尽）
- **round_base**: `e8ca95c070c1420ec3e3cfc4cec64789d9097f0b`（`V3-PHASE-C1-CLOSEOUT-v1`，Phase C1 的收口）
- **plan_commit**: `6c39d92e99e8b68ee9a6653be10e32f22690d8d3`（`V3-PHASE-C1.5-PLAN-AND-RULINGS-v1`，本 plan 自己，**是本轮的第一笔 commit**）
- **base_branch**: document-work-assurance-v3

> **`round_base` 与 `plan_commit` 的区别很要紧**：dispatch range 用 `e8ca95c..HEAD`（`round_base` 是 base），
> 而冷 session 开工时 `git rev-parse HEAD` 应当是 `6c39d92` **或其后代**——因为本 plan 自己就在轮内。
> 初版把两者混成一个 `base_commit: e8ca95c`，Step 1 会因此当场判「plan 已过期」自我卡死。

## Goal (one line)

把 digest 从「到处都写、几乎没人读」收窄到 **executor 不是合法作者的那三类文件**，其余**由本轮改到的写入路径**全部停写——**行为上的净减**，用诚实的空白换掉假保护。

> **不是「纯减法」**（FULL 的 F-3 更正，2026-07-29）：本轮**加了**一个 frozenset、一个 helper
> （`pointer_for`）、一个新 issue code（`V3-STATE-POINTER-UNVERIFIED`）和一条新的非零退出路径
> （`rsc v3 status`）。这四样在 commit 正文里都披露了，**只有「纯减法」这个概括没有任何命令支持**
> ——`E3` 针对的正是这种无来源的概括。减掉的是**行为**（写 digest 的义务），不是代码量。

> 「其余全部停写」限定在**本轮改得到的写入路径**（`run-v2` 活模板 + `_write_evidence`）。手写 run 脚本里
> 直接调 `assurance_state.pointer(path, digest)` 的形式仍能写出 digest（见 Constraints 的 O3 条），
> 本轮不封那条路——封它要动 `pointer()` 的签名，属另一次范围。

## Why / value

现状是：13 处 digest 比对，在「agent 能同时改文件和 digest」的前提下**零处有真实收益**；四类 pointerRef 的 digest 写了从没人读；`cf51534` 改路径让五份 ISSUE_TRIAGE 决定的 digest 全部失效而套件全绿。收窄之后，digest 只留在「误写之后 agent 自己重做一份 = 伪造别人签字」的文件上，其余位置的绑定回到 commit——**说得清它在保护什么，也说得清它不保护什么**。

## ⚠ E2 冲突 —— C1.5 以 override 发出；契约的成文更正在 C1.6（2026-07-29）

> **C1.5 的处置，最终且不追改：用户裁「显式 override」。** 不采窄读、不走 `SPEC_GAP`，
> 公开违反那句签名文本。候选 `7052a89` 的正文按此写死；FULL（`v3-review-full-7052a89.md` §3）
> 也**正是按 override 认证的**，并明写它「不曾把自己描述成 E2 允许的例外」。**这条是历史事实，
> 后续任何文件都不得把 C1.5 改写成 in-boundary。**
>
> **C1.6 补的是契约文本，不是 C1.5 的定性。** FULL 返回后，用户批准新写
> `Document-Work-Assurance-Contract-v3-supersession-2.md`——依据是 supersession-1 自己开头引的
> 签名契约 §13：*"Signed contracts are never amended in place; corrections create a versioned
> successor"*，而 `E2` 冻的是「**既有**文件」，新建一份零冻结字节。**它让今后契约与代码一致；
> 它不能倒回去把 C1.5 变成 in-boundary。** 该文件按 `E10` 属 instruction layer，
> **欠一次独立 read**，那次 read 不得当任何轮次的 FULL。
> 起因：用户追问「override 是不是该直接改写措辞」，查证后发现 versioned-successor 机制一直存在，
> 只是 plan 当初枚举的三个选项面（窄读 / `SPEC_GAP` / override）漏了它。**这是选项面漏列，
> 不是 C1.5 处置错误**——FULL 独立读出同一个字面空隙，并把「新建 contract 文件该不该先经裁决」
> 作为 R5 问题交回用户；用户 2026-07-29 裁「存在」。

**冲突内容（保留，FULL 会核）：签名的 supersession-1 §3 明写「state pointer 携带 BYTES digest」，而本轮让四个活的 state pointer 停止携带。**

```
$ git rev-parse HEAD:ResearchSystem/contract/Document-Work-Assurance-Contract-v3-supersession-1.md
68031fa2ca31272e31da0d42a9a02189d28fcc21          ← checklist E2 点名的冻结 blob

contract §3 原文：
- A state pointer carries the **BYTES digest** of the pointed-at file (the w1-r1
  pointer-digest-kind lesson, triaged `CORE_CANDIDATE`); the documented authoring path is
  the `assurance_state.pointer_to` helper, which computes the bytes digest itself.
```

**字节上不冲突**（本轮不改那个文件），但这是一句**无限定的签名陈述**，而 Step 5 让 `fulfillment_ref` /
`manifest_ref` / `check_results_ref` / `coverage_ref` 四个 state pointer 不再携带 digest。2026-07-28 的
ISSUE_TRIAGE 只针对 **schema**（`pointerRef` 的 digest 可选）授权，**从未处理过这句比 schema 更强的签名句**。

`E2` 自己给的路径是 *"take the in-boundary fix and record why, or stop with `SPEC_GAP`."* ——**C1.5 两条都没选，选了第三条：显式 override**。当初枚举的备选（(a) 窄读「约束的是 digest 的种类而非存在」/ (c) `SPEC_GAP` 停轮）**漏了第四条**：契约自带的 versioned-successor 机制。那条在 C1.6 被采用，**但它到得太晚，改不了 C1.5 的定性**。

**诚实边界**：① `supersession-2` 是 **UNSIGNED**，且按 `E10` 欠一次独立 read，**在那次 read 之前不得声称「契约已对齐」**——只能说「已写出成文的更正，待读」。② 候选 `7052a89` 的正文按 override 措辞写着，那是当时的真实处置，不追改；FULL 也按 override 认证。③ 因此 **2026-07-28 以来对 harness 自身规则的 explicit override 是三次**：前两次在 `E10` 的 amendment-read 上（C1 的 FULL 以 O-1 提出，用户已裁「给 `E10` 加一条明确出口」并排在 C2 之后），第三次就是 C1.5 的这一条。C1.6 不减少这个计数。

## Context to resume cold

> 本节是给零记忆的新 session 的。**不要重新裁已裁的**，也不要重新论证已论证的。

### 这一轮的由来

父计划 [`harness-deletion-first-stabilization`](harness-deletion-first-stabilization.plan.md) 的 Phase C1 已 CLOSED（`REVIEWED_NO_BLOCKER`）。开 Phase C2（flow/summary 组 M5–M7）时发现撞车：**M6/M7 的缺陷表修法是「加 path+digest 交叉核对」，而 digest 已于 2026-07-28 被裁为删**。用户裁「先做 digest 这一轮，C2 让路」。本 plan 就是那一轮。

### 裁决链（按时间，全部已定，勿重开）

1. **2026-07-28**：digest 裁「删」。理由（用户原话）：**agent 有能力同时改文件和签名**，自算 digest 对它唯一需要约束的那一方毫无约束力。issue `issue-p3-corr-digest-binds-nothing-against-the-only-writer`（`PROCESS_BURDEN`）+ ISSUE_TRIAGE `CORE_CANDIDATE`，均在 `ResearchSystem/assurance/runs/p3-corr/issues/`。
2. **2026-07-29 修正**：从「删」改为「**收窄**」。用户原话：*「虽然抵挡不了主动同时修改 hash+内容的攻击，但是 digest 还是可以防 agent 失误的写入，不过只在最重要的文件上才需要上这个保护。」*
3. **2026-07-29 威胁模型收窄**：用户明确 *「我指的只有 (a) 的那类」* —— 即**不知情的写偏**，**不是**恶意篡改，**也不是**「通知我」那一类。
4. **2026-07-29 否决三项**：
   - **HarnessIssue 不进保护集**。用户理由：另外三类是 harness 流程内不能改变的内容，而 **HarnessIssue 的写入时间点不确定，甚至不需要在 harness 流程内**。（`issues.py` 那句 "immutable once written" 是代码里的声明，流程给不出对应时刻——**C1.5 当时记为发现、未动；已由 C1.6 修掉**：用户裁定它是「把规矩写成了断言」，修法即改措辞成 obligation，不补机制。）
   - **不加指令层 digest 基线，也不加任何通知机制**。
   - **p3-corr 的 CRLF 事故不算 (a) 类**。自检 agent 曾以它为据主张「保护边界划错了」（那次事故的四个 `POINTER-STALE` 恰好落在本轮要停写的四个 pointer 上）。用户裁：**那是编译/工具链问题**——agent 写的内容本来就是对的，被平台改的是行尾——**不构成不知情的写偏，保持原决定**。记此以免 FULL 或后续 session 再提一次。

### 判据（唯一，可判定）

> **这个文件被误写/误删之后，agent 自己重新生成一份，算不算伪造？** 算 → 保。不算 → 不保。

不问价值，只问**权限**：谁有资格产出这份文件的**当前版本**。

### 保护集 —— 5 个 pointer field / 3 类文件

| pointer field | 指向 | 为什么 agent 重做 = 伪造 |
|---|---|---|
| `work_spec_ref` | **WorkSpec** | executor 确实是它的**初始**作者（`runs/p3-corr/build_run.py` 写 `work-spec.json`），但一旦 run 绑定，它就是**这次 run 被拿来judge 的那份考卷**。executor 事后重出一份 = 改自己被评判的依据。**判据在这里问的是「有没有资格产出当前版本」，不是「最初谁写的」。** |
| `start_decision_ref` | START 决定 | 伪造用户授权 |
| `repair_decision_ref` | REPAIR 决定 | 伪造用户授权 |
| `final_decision_ref` | FINAL 决定 | 伪造用户授权 |
| `review_ref` | review 记录 | 自审 |

**三类都已经有读者，本轮不需要补任何读者**：`assurance_state.resume`（读工作树）与 `review_subject._resolve_pointer`（读 evidence commit）都遍历全部 `POINTER_FIELDS`。WorkSpec 另有两处 digestRef 比对（`instruction.py::check_audit`、`review_subject.py` 的 spec-binding 检查），**本轮不碰**。

### 已用命令核过的事实（不要重新核，除非改动使其失效）

1. **`pointerRef` 的全部使用点**（`grep -rn pointerRef ResearchSystem/schema/document-assurance-v3/*.json`）：`assurance-work-state`（13 个 state pointer）· `document-assurance-profile.evidence_ref` · `local-check-spec` CheckResult 的 `evidence_ref` · `review.executor_summary_ref` · `user-decision.target.harness_issue_ref`。
2. **三种 ref 形状**：`pointerRef` required=`[path]`（digest **可选** → 停写无需改 schema）· `digestRef` required=`[path, digest_sha256]` · `frozenFileRef` required=`[path, revision]`。
3. **后四类 pointerRef 的 digest 从没有任何代码读回来**（在 v3 `document_harness` 包内逐个 grep，零命中）。`stage_control.py:809` 的 `evidence_ref.get("digest")` 是 v2/历史层的**另一个字段名**，不在范围内。
4. **`pointer_to` 全仓 11 个调用点**：**5 个是活的**，全在 `ResearchSystem/assurance/templates/run-v2/`（`run_bind_v2.py:62`、`run_evidence_v2.py:209/211/213/215`）；**另外 6 个在 `ResearchSystem/assurance/runs/p3-corr/`**（`run_bind_candidate.py` + `run_bind_v2.py` + `run_evidence_v2.py`），属 frozen evidence，**不在范围内也不要动**。
5. **`executor_summary_ref` / profile `evidence_ref` / `harness_issue_ref` 没有库内写入点**——都是调用方/手工提供。`review.py` 只把参数原样放进 package；`assurance_profiles.py` 只读 `["path"]`；`issues.py::check_triage` 只读 `.path`。**它们不需要代码改动，停止授权它们即可。**
6. **`ResearchSystem/assurance/templates/run-v2/` 是 live 模板，可改**；`assurance/runs/**` 与 `assurance/shadow/**` 是 **frozen evidence（V3-D9：never modify）**，见 `assurance/README.md:17`。
7. **基线套件（`6c39d92` 时点）**：`document_harness` 147 · `document_harness_review` 321 · `tests/harness/run_tests.py` 39 · `tests/stage_control/run_tests.py` 20 · `tests/run_tests.py` 29；从**仓库根**跑 `python Thesis/Work/Tooling/repo-audit.py` exit 0。**跑法见下方 Notes。**

### 本轮会打破的现存测试（初版漏了，必须同轮处置）

| 测试 | 为什么会红 | 处置 |
|---|---|---|
| `tests/document_harness_review/test_review_v2_subject.py:562-563`（`SubjectAgainstSeededPlanes::test_state_pointer_family`） | 它用 **`coverage_ref`（非保护字段）**删掉 digest 来断言 `V3-SUBJECT-POINTER-UNVERIFIED`。Step 4 之后非保护字段不再报该 code | 把这个 subTest 的 mutation 换到**保护字段**。注意：`build_scenario` 放进 state 的保护字段只有 `work_spec_ref` |
| 同文件 `:796-802`（`test_every_declared_code_is_asserted_by_name_in_this_suite`） | 它要求 `review_subject.py` 声明的每个 issue code 的字面量出现在**这同一个测试文件里** | 因此 Step 3 的测试 ②**必须写在 `test_review_v2_subject.py` 里**，不能另起文件 |
| `tests/document_harness/test_spec_plan_state.py:891`（`test_n1_a10_pointer_without_a_digest_is_never_reported_as_verified`） | 它用 **`work_spec_ref`（保护字段）**无 digest，断言进 `present_unverified`、渲染成 `??`、含 "NOT verified" | 见 Step 4 的读法裁定：**保护字段缺 digest 时既报 issue、又留在 `present_unverified`**，该测试三条断言全部保持绿 |

### 运行本轮时适用的 harness 规则

执行契约是 [ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md](../../ResearchSystem/harness/ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md)（E1–E12 执行侧 / R1–R9 评审侧）。最要紧的几条：

- **E11 preview card**：范围已由用户在 2026-07-29 规划会话逐项批准，执行 session 的卡可以精简为「按 plan 做，范围不变」一行确认，不必重新推销范围。**但上面那条 E2 冲突必须在卡上单独提出并等用户处置。**
- **E10 开轮 cold read**：本轮 subject 全在代码层，**零指令层字节、零 schema 字节**。仍须向用户申请一次。先例：⑤ 与 Phase A 判 waive（`E10` 内置的出口）；**C0 那次 waive 的是 amendment-read，ledger 明记为 override 而非规则内出口**——引用先例时别把两者混为一谈。
- **E4 / hard rule 4**：每个新守卫做 mutation 探针（neuter → 值级红 → 从 **sha256 校验过的 scratchpad 副本**还原，**禁 `git checkout --`**）。
- **E5**：断言用手写字面量或已提交 fixture，**不得引用模块自己的常量**（本轮尤其是 `DIGEST_PROTECTED_FIELDS`——测试里要写死那 5 个字段名）。
- **E8**：显式路径 `git add`、新 commit 不 amend、不 push、单行标题 `V3-PHASE-C1.5-DIGEST-NARROWING-v1` + 一段密实正文、无 trailer、正文里点名 commit 类别（candidate）。
- **E12**：dispatch 用 `python rsc.py v3 dispatch --range e8ca95c..HEAD`（base = `round_base`），**tip 永远写 `HEAD`，不写死 SHA**。
- **R6 记录通道**：review session 在 worktree 写 `ResearchSystem/migration/document-work-assurance-v3/v3-review-full-<sha>.md`，**执行侧提交**，标题 `V3-REVIEW-RECORD-PHASE-C1.5-<sha>-v1`，逐字提交、不改其文本、不在里面嵌回应。
- **E1**：不许自审。review 由用户路由到独立 session。

## Constraints / Out-of-scope

- **零 schema 改动。** 停写 `pointerRef` 的 digest 不需要动 schema（digest 本来可选）。跑完后 `git diff --name-only e8ca95c..HEAD -- ResearchSystem/schema/` **必须为空**。
- **零 E2 冻结**字节**接触**。三个签名 blob（`8ad404b1` / `b2dbdf75` / `68031fa2`）+ `ResearchSystem/contract/` 既有文件 + N0 schema 既有字节，逐条复核不变。**注意：字节不变不等于不冲突——见上方「开轮前必须由用户处置的一项」。** 两个精确 oracle（`tooling/tests/fixtures/expected-construction-prompt.txt` + `tooling/tests/document_harness/test_readme_enumeration.py`）**动它们须先经用户本人**。
- **不重写历史文档。** 已提交的 run / issue / decision / summary 文档里现存的 digest 原样保留——它们是 frozen evidence，改它们会让记录与当时实际发生的事不符。本轮只改**今后怎么写**。
- **不碰 `digestRef` 一侧。** `instruction.py` / `review.py` / `summary.py` / `assurance_profiles.py` / `review_subject.py` 的 spec-binding 检查里的 digestRef 比对全部原样保留。让它们变可选要动 5 个冻结 N0 schema 文件 = 用户对 E2 的另裁，不是轮次能裁。
- **不补新读者。** 保护集三类都已有读者。`check_assurance_candidate` 的 `review_refs` 只数个数不核内容（`summary.py:183`）——**那是 M6，留在 Phase C2**。
- **不封 `pointer(path, digest)` 这条手写路径。** 它在 8/13 个 state pointer 上被手写 run 脚本使用（当前 25 个调用点全在 frozen `runs/**` / `shadow/**`）。本轮不动它，因此**一个照抄既有先例的新 run 仍会写出 digest**——这是已知的不完整，写进 commit 正文，别声称"全部停写"。
- OUT：指令层 digest 基线（已否决）· 任何通知/打印机制（已否决）· HarnessIssue 进保护集（已否决）· 全仓 digest 扫描面（新机制，`E6` 反对）· Phase C2 的 M5/M6/M7 · 重写 `assurance/runs/**` 或 `shadow/**` 下任何脚本 · 改 `pointer()` 的签名。

## Steps

- [x] 0. **处置 E2 冲突** → **已完成（2026-07-29，用户裁「显式 override」）**。执行 session 不需要再问，但**必须**：① 在 preview card 上复述这一条；② 在 commit 正文里按文首的措辞写明「这是对签名文本的公开违反、E2 的两条规则内出口未被采用、由用户裁决」。
- [x] 1. **对基线**：`git rev-parse HEAD` 应为 `6c39d92`（本 plan 自己的 commit）**或其后代**，且 `git rev-parse 6c39d92^` = `e8ca95c`（`round_base`）。跑五套件 + repo-audit，确认与 Context 第 7 条一致。不一致就先停下报告（plan 已过期）。
- [x] 2. **写策略常量**：在 `rsclib/document_harness/assurance_state.py` 加
      `DIGEST_PROTECTED_FIELDS = frozenset({"work_spec_ref", "start_decision_ref", "repair_decision_ref", "final_decision_ref", "review_ref"})`
      + 一段注释写清判据（「谁有资格产出这份文件的当前版本」），并加 `pointer_for(field, path, repo_root)`：字段在保护集里就走 `pointer_to`（算 digest），否则走 `pointer(path)`（只有 path）。**这是本轮唯一的新增物**。
- [x] 3. **先写测试，确认真红**（每条都要看到值级失败，不是崩溃）：
      ① 非保护 pointer 缺 digest → `_resolve_pointer` **不**报 issue（**当前会红**：现在无条件报）
      ② 保护 pointer 缺 digest → `_resolve_pointer` 报 `V3-SUBJECT-POINTER-UNVERIFIED`（回归，防删过头）。**必须写在 `tests/document_harness_review/test_review_v2_subject.py` 里**（原因见上表第二行）
      ③ 保护 pointer digest 不匹配 → `V3-SUBJECT-POINTER-STALE`（回归）
      ④ `resume`：保护 pointer 缺 digest → 进 issues **且仍进 `present_unverified`**；非保护 pointer 缺 digest → 只进 `present_unverified`、不报 issue
      ⑤ `pointer_for` 策略单测：5 个保护字段各带 digest、若干非保护字段各不带（**断言写死那 5 个字段名，不得 import `DIGEST_PROTECTED_FIELDS`** —— E5）
      ⑥ `_write_evidence` 返回的 ref 不含 `digest_sha256`，且带该 ref 的 CheckResult 仍通过 `validate("check_result", …)`
      **同时**按上表把 `test_review_v2_subject.py:562-563` 的 mutation 换到 `work_spec_ref`。
- [x] 4. **改读侧（两处，同一个 frozenset 门控）**：
      · `review_subject.py::_resolve_pointer` —— `V3-SUBJECT-POINTER-UNVERIFIED` 只对保护字段报；非保护字段缺 digest 是正常，不报。
      · `assurance_state.py::resume` —— 保护字段缺 digest 时**既报一个新 issue（建议 code `V3-STATE-POINTER-UNVERIFIED`），又仍然进 `present_unverified`**。
      **裁定理由（别改成"只报 issue"）**：`test_spec_plan_state.py:891` 记录了一条 N1-A10 属性——digest-less 的 pointer 必须渲染成 `??` 且含 "NOT verified"。只报 issue 会打掉那三条断言，而"为了让新规则通过而删掉一条已记录的属性"正是 `E6` 指的反模式。
      **副作用（写进 commit 正文，是预期不是意外）**：`rsc.py::_cmd_v3_status` 用 `return 0 if point.report.ok else 1`，所以保护字段缺 digest 会让 `rsc v3 status` 从 0 翻成 1。
      **注意**：新增 issue code 可能触发 N1 模块的 code-reachability 要求——落地前先确认 `tests/document_harness/` 里有没有对 `assurance_state.py` 的同类 sweep，有就一并满足。
- [x] 5. **改写侧**（**先完成 Step 0**）：
      · `checks.py::_write_evidence`（`:180`）只返回 `{"path": rel}`，不再算 `bytes_digest`（两个调用点 `:379` / `:381` 自动跟随）。
      · `ResearchSystem/assurance/templates/run-v2/run_bind_v2.py:62` 与 `run_evidence_v2.py:209/211/213/215` 的 5 个 `pointer_to(...)` 改走 `pointer_for(<field>, ...)`。其中 `run_bind_v2.py:62` 的 `review_ref` **在保护集里，行为不变**；`run_evidence_v2.py` 的四个**都不在保护集**，改后不再带 digest。
      · **同轮修正被本轮证伪的活文档**（初版漏了）：`ResearchSystem/assurance/templates/run-v2/README.md:15`（"state pointers carry BYTES digests, authored via `assurance_state.pointer_to`"）与 `run_evidence_v2.py:11` 的模块 docstring；顺带 `assurance_state.py:8-12` 的模块 docstring 与 `pointer_to` 自己的 docstring（`:64-79`）。模板 README **不是 instruction layer**（HARNESS-LEDGER 记的 2026-07-26 裁决），可以同轮改。
- [x] 6. **绿 + mutation 探针**：五套件 + repo-audit 复跑；对第 3 步**六条**守卫各做一次 neuter → 看值级红 → sha256 校验副本还原（禁 `git checkout --`）。把每条的红消息原样记下来，commit 正文要用。
- [x] 7. **复核边界**：
      `git diff --name-only e8ca95c..HEAD -- ResearchSystem/schema/` 为空 ·
      `git diff --name-only e8ca95c..HEAD -- ResearchSystem/contract/ ResearchSystem/tooling/tests/fixtures/expected-construction-prompt.txt ResearchSystem/tooling/tests/document_harness/test_readme_enumeration.py` 为空 ·
      `git diff --name-only e8ca95c..HEAD -- ResearchSystem/assurance/runs/ ResearchSystem/assurance/shadow/` 为空 ·
      三个签名 blob 用 `git rev-parse HEAD:<path>` 逐条复核仍为 `8ad404b1` / `b2dbdf75` / `68031fa2`。
- [x] 8. **落 commit**：显式路径 `git add`，标题 `V3-PHASE-C1.5-DIGEST-NARROWING-v1`，一段密实正文（含：本轮是 candidate、判据、保护集 5 字段、停写清单、四类无库内写入点因此靠停止授权、**六个** mutation 探针的值级红消息、五套件计数与 repo-audit exit、冻结面复核结果、Step 0 的 E2 处置及其理由、以及 Notes 里那四条诚实边界）。同轮更新本 plan 的 Steps 勾选 + Resume pointer，以及 `ResearchSystem/HARNESS-LEDGER.md` 指针与裁决段、`.goals/LEDGER.md` 的 harness 行、**父 plan 的 Resume pointer**。
- [ ] 9. **交审**：`python rsc.py v3 dispatch --range e8ca95c..HEAD`（在 `ResearchSystem/tooling/` 下跑），把**整段 dispatch 输出**交给用户路由到独立 session——不是只交 range 那一行（那段 prompt 才是告诉 reviewer「你是谁、standing instructions 在哪」的信封）。
- [ ] 10. **收 verdict**：FULL 回来后按 R6 逐字提交记录 → 按结果走（`REVIEWED_NO_BLOCKER` → 回到父 plan Step 6 · Phase C2；`CHANGES_REQUIRED` → 一次修复 + 一次 VERIFY 吃完 E9 预算）。

## Acceptance (done = ?)

每一条都给了可跑的命令；没有命令的那两条标明了它们只能从轮次记录里核。

- **五套件全绿 + repo-audit exit 0**，在最后一次改动之后重跑（E3：测量放最后）。命令见 Notes。基线 147/321/39/20/29，本轮会因新增测试而增长。
- **零 schema 改动**：`git diff --name-only e8ca95c..HEAD -- ResearchSystem/schema/` 输出为空。
- **冻结面未动**：Step 7 的三条 `git diff --name-only` 全部为空 + 三个 blob 的 `git rev-parse` 值不变。
- **策略生效可验证**：`python -m pytest tests/document_harness -k pointer_for -q` 绿——5 个保护字段带 digest、非保护字段不带。
  （**注意**：5 个保护字段里只有 `review_ref` 有活的写入点，`run_bind_v2.py:62`；其余四个的写入在手写 run 脚本里，本轮碰不到。所以"仍带 digest"这条**只能靠 `pointer_for` 的单测证明**，不能靠跑一次 run 证明。）
- **噪音消失可验证**：`python -m pytest tests/document_harness_review -k state_pointer -q` 绿——非保护 pointer 缺 digest 不再产生 `UNVERIFIED`。
- **六条守卫各有一个曾经红过的测试 + 一次 mutation 探针**：这是**历史属性**，事后无命令可验。判据改为可核的形式——**六个测试存在于套件中，且六段探针记录（neuter 的目标、值级红消息、还原后的 sha256 匹配）逐条出现在 commit 正文里**。
- **三个账本 + 父 plan 一致**：具体到行——本 plan 的 Resume pointer、`ResearchSystem/HARNESS-LEDGER.md` 的当前指针块、`.goals/LEDGER.md` 的 harness 行、`.goals/plans/harness-deletion-first-stabilization.plan.md` 的 Resume pointer，**四处都指向本轮的下一步**。

## Resume pointer

当前指针: **本 plan CLOSED，Steps 0–10 全部走完**。C1.5 `REVIEWED_NO_BLOCKER`（预算未动）· C1.6 `CHANGES_REQUIRED` → 修复 → VERIFY `REVIEWED_NO_BLOCKER`（预算用尽）。**`supersession-2` 的 `E10` read 已完成**（记录 `17e2b65`）：**1 must-fix（`M-1`）/ 1 low（`L-1`）/ 4 observation**——`M-1` = 契约 §4 把 `instruction_ref` 说成 `digestRef`，实为 `frozenFileRef`；`L-1` = §1 的 `cf51534` 波及面是**八**份 triage 决定不是五份。（先前此处写「2 must-fix / 3 low」并把范围钉成 `R-1`/`R-2`，**全部作废**——那是执行侧把对话转述当成记录内容写入，未核磁盘上的记录；更正与 errata 见 `HARNESS-LEDGER.md`。）**下一步不在本 plan 内**：① 用户 2026-07-29 裁「**先收敛链，后修文本**」——指令层 amendment 轮（`E10` 出口 + UNSIGNED 文本反复修改的读义务 + `E2` 措辞收窄，三件合并）提前，**C1.7 文本修正挂起**；② 之后回父 plan [`harness-deletion-first-stabilization`](harness-deletion-first-stabilization.plan.md) 的 **Step 6 · Phase C2**，开轮先重定 M6/M7 的形状。**一件待用户裁**：并发形状第二次发生（见上方「C1.6 的 VERIFY 与收口」段）。

## Notes

**怎么跑套件**（五个，前两个是 pytest，后三个各有自己的 runner；**cwd 很重要**，repo-audit 必须从仓库根跑，从 `tooling/` 跑会 exit 2 且那是**路径错不是失败**）：

```bash
cd ResearchSystem/tooling
python -m pytest tests/document_harness -q            # 147
python -m pytest tests/document_harness_review -q     # 321
python tests/harness/run_tests.py                     # 39
python tests/stage_control/run_tests.py               # 20
python tests/run_tests.py                             # 29
cd ../..            # 回仓库根
python Thesis/Work/Tooling/repo-audit.py; echo $?     # 0
```

**mutation 探针的做法**（C1 用过，可复用）：把要探的模块复制到 scratchpad 并记 sha256 → 用脚本做**精确字符串替换**把修复 neuter 掉（替换目标必须恰好出现 1 次，否则报错停下）→ 跑那条测试 → 确认是**值级**失败而不是 crash → 从副本还原并**复核 sha256 一致**。整段禁用 `git checkout --`。

**本轮必须在 commit 正文里披露的诚实边界**（写清楚，别软化）：
1. **收窄后的 digest 只挡「不知情的写偏」**，挡不住同时改文件和 digest 的一致修改——这是用户明示的威胁模型边界，不是遗漏。
2. **这些 assert 没有自动执行面**：pre-commit 只跑 `repo-audit.py`（其中 `digest|sha256` 命中 0），没有 CI。它们只在有人跑 `resume` / dispatch / run 模板时执行。对「run 进行中的误写」够用；**对已关闭的 run 事后被误改，仍然不会当场红**。
3. **`issues.py` 声明 HarnessIssue "immutable once written"，而流程给不出对应的写入时刻**（用户 2026-07-29 指出）。C1.5 按裁决不把它列入保护集，并把这条矛盾记为悬置。**已由 C1.6 关闭**：矛盾不在机制缺失，而在语气——无 enforcement 时只能声称「不许改」，两句已改成 obligation。（本条是 C1.5 commit 正文里那份四条边界的第 4 条；**注意 plan 与 commit 正文对第 3、4 条的排序相反**，引用前先看清是哪一份。）
4. **"其余全部停写"不成立于手写路径**：`assurance_state.pointer(path, digest)` 仍能写出 digest，一个照抄既有先例的新 run 会在 `resolved_plan_ref` / `instruction_audit_ref` / `summary_ref` / `assurance_candidate_ref` 上继续写。本轮不封那条路。

**为什么是行为上的净减，而不是纯减法**：三类保护文件都已经有读者，所以**不需要补新的读者**——但本轮确实新增了**四样**：一个 frozenset、一个 helper（`pointer_for`，把「写不写 digest」这个策略从 5 个散落的调用点收到一处可测的地方）、一个新 issue code（`V3-STATE-POINTER-UNVERIFIED`）、以及 `rsc v3 status` 的一条新非零退出路径。减掉的是**写 digest 的义务**，不是代码量。（这一行是 C1.6 FULL 的 `B-2`：F-3 在文首 Goal 处修了，这里没修，而这里的说法更详细也更错——「不需要新增任何检查」被那个新 issue code 证伪，「唯一的新增物是两样」被四段前自己的更正证伪。）

**下一步是什么**：本轮 CLOSED 后回到父 plan [`harness-deletion-first-stabilization`](harness-deletion-first-stabilization.plan.md) 的 **Step 6 · Phase C2（flow/summary 组 M5–M7）**。届时 M6/M7 的形状要重新判：本轮之后 `review_refs`（digestRef，属保护集里的 review 记录）值得核内容，而其余 ref 的 digest 交叉核对已无意义——**缺陷表原话在这一点上已经过时**，C2 开轮时须向用户重新确认 M6/M7 的形状。

**FULL 结果（2026-07-29）**：`REVIEWED_NO_BLOCKER`，零 blocker，记录 `v3-review-full-7052a89.md`（逐字提交于 `7ff29b3`）。**C1.5 的 fix 与 VERIFY 预算未动。** reviewer 自跑 11 条 mutation 探针（比本轮多 4 条），并独立确认了三件本轮未主张的事：8 个已提交 `state.json` 在每个保护字段上都带 digest，故披露的 `rsc v3 status` 退出码副作用**目前从已提交状态不可达**；「零 schema 改动」是 `pointerRef` 本就允许的；全仓唯一被写falsified的活文档就是冻结的 supersession-1 本身。它并**背书**本轮那处偏离 plan 的自裁（存在性 fault 保留在所有字段）。五条 finding 的处置见下。

**五条 finding 的处置（用户 2026-07-29 逐条裁）**：

| # | 处置 |
|---|---|
| F-1（模块 docstring 那句对全部 8 个已提交 state 为假） | **R9 bank，在 C1.6 兑付**——bank 条件是「下次碰这一层的批次」，C1.6 改的正是该文件 |
| F-2（正文「同轮修了两个既有测试」无命令支持，`git diff --numstat` 只支持一个） | commit 不可变，**在此更正**：实际只有 `test_state_pointer_family` 一个测试方法被改（mutation 换到 `work_spec_ref`）；另两个是靠**放置位置**与 Step 4 的裁定保持绿的，**没有被修** |
| F-3（「纯减法」无命令支持） | **改 Goal 的措辞**（见文首），plan 是活文档 |
| F-4（run-v2 模板五个 `pointer_for` 调用点无测试覆盖） | **裁「不加守卫，等真 run」**（用户 2026-07-29）。判据是 `E6`：不加的最坏后果只是模板被改回去、新 run 又写那四个**本轮刚认定为无用**的 digest——即回到 C1.5 之前的状态；而真正要紧的那半（保护字段掉 digest）已有读侧门控在 resume/dispatch 当场报。为防一个无害回档去给模板搭一个能跑穿 checks→manifest→record 的假仓库，正是 `E6` 点名的反模式。**并进 C0 复验已经记下的那笔欠账**（「模板形状能否扛住真实 run」= `UNVERIFIABLE`，从无真 run 跑过改后模板），不新开一笔 |
| F-5（`pointer_for` 字段名写两遍，无交叉核对；后果被读侧门控兜住） | **观察项，不动**。记此以便知道兜住它的是什么 |

**并发问题的用户裁决（2026-07-29）**：FULL 在外期间同一工作树被改写，**用户裁为自己这侧的问题、正常不应发生**，并裁「**当作这些改动发生在 FULL 结束之后**」——因此它们构成独立的 C1.6，而非 C1.5 的 fix round。诚实边界：FULL 的数字不受影响（时间窗不重叠，探针全部 `RESTORE-SHA256: MATCH`），受影响的是**可复现性**——复核其数字须对 `git archive 7052a89`，不是工作树。

**C1.6 内容（`7052a89` + FULL 之后的独立一轮；不吃 C1.5 预算）**：

- **契约成文更正**：新写 `ResearchSystem/contract/Document-Work-Assurance-Contract-v3-supersession-2.md`，按 supersession-1 自己援引的签名契约 §13（versioned successor）做**一条** statement supersession。零冻结字节（`E2` 冻的是**既有**文件；「新建 contract 文件是否需先经裁决」由 FULL 作为 `R5` 问题交回，用户 2026-07-29 裁「存在」）。**它只让今后契约与代码一致，不改 C1.5 的 override 定性**；且它 UNSIGNED、属 instruction layer，**欠一次 `E10` 独立 read**，那次 read 不得当任何轮次的 FULL。
- **F-1 兑付**：`assurance_state.py` 模块 docstring 那句「其余靠存在性解析并被报为 unverified」对全部 8 个已提交 state 为假，改为「只有保护字段**被写入** digest；已存在的 digest 在每个字段上都会被校验」。
- **F-3 兑付**：Goal 的「纯减法」改为「行为上的净减」，并列出本轮实际新增的四样。
- **F-2 更正**：见上表，只有一个测试方法被改。
- **`issues.py` 措辞改判**（用户指出）：`:5` 与 `:62` 的 "immutable once written" / "nothing amends it" 是**陈述句**，而无 enforcement 时只能声称「不许改」。两句改成 obligation，并在模块 docstring 里写明"没有任何东西 enforce 它、原措辞是把规矩写成了断言"。**修法是改文字，不是补机制**（`E6`）。
- **诚实边界 3 降级**：「已关闭的 run 事后被误改不会当场红」按用户裁决**本就不在覆盖范围内**，改成范围声明，不再写成缺口。
- **诚实边界 4 改判**：`issues.py` 的矛盾**不是**「系统兑现不了自己的声明」（那个说法暗示欠一个机制），而是「把规矩写成了断言」，修法即改文字。
- **`run-v2/README.md` 补一句**：五个保护字段里只有 `review_ref` 由本模板写，其余四个在手写 run 脚本里。
- **一次自我翻案（留档，供 C1.6 的 FULL 归因）**：C1.6 起草期间我据一次读取认为保护集已变成 4 个字段（`review_ref` 移出），并据此做了整套对齐编辑、也据此向用户汇报「零活写入点再产出 digest」。**`git diff 7052a89` 显示 frozenset 区段无变化 + 直接 grep 读回 5 个成员**——两个测量一致，那个前提在仓库里不成立，全部对齐编辑已逐条还原。保护集仍是 5 个，`review_ref` 仍是唯一有活写入点的那个（`run_bind_v2.py:62`）。FULL 的 M9 探针独立覆盖了同一处：把 `review_ref` 从 frozenset 拿掉会当场红。

**C1.6 的 FULL 与修复（2026-07-29）**：FULL 判 **`CHANGES_REQUIRED`**，4 个 blocker + 4 条非 blocker，记录 `v3-review-full-f2507a5.md`（逐字提交于 `10aeb10`，sha256 `c8b7c33a…`）。**用户批准动用 C1.6 的唯一一次 repair，范围严格限于 §5 的四条**（F-a~F-d 不进本次，另记账）。四条我逐条用命令复现过再改：

| blocker | 复现结果 | 修法 |
|---|---|---|
| B-1 `assurance_state.py:14-20` | `resume` 跑遍 8 个已提交 state：`verified` **全为 0**，只报 `POINTER-MISSING`（指针仍指 2026-07-27 搬家前的老路） | 删掉「`resume` 把这些验进 `verified`」那半句；改成只陈述**代码路径**性质（「已存在的 digest 在任何字段上都会被校验」），并明写「某个已提交 state 还解不解析得开，是命令的问题，不是 docstring 的问题」 |
| B-2 `plan:222` | 该行仍写「纯减法 / 不需要新增任何检查 / 唯一新增物是两样」，被本轮新加的 `V3-STATE-POINTER-UNVERIFIED` 与文首自己的更正双重证伪 | 整行改写：净减的是**写 digest 的义务**，并列出实际新增的四样 |
| B-3 `supersession-2 §2` | `git grep "pointer_to("` = **6 个已提交 run 脚本调用点**（`runs/p3-corr/`）+ **3 个活测试** | 「is no longer called directly」改为「no longer the authoring path for a **newly opened run**」，并点名闭合 run 脚本与该 helper 自己的测试仍在直接调 |
| B-4 `supersession-2:3` | 状态行写着 `authored at the Phase C1.5 round` | 改为 `authored at Phase C1.6` —— 「这是 C1.6 不是 C1.5」正是保住 C1.5 那次 repair 的裁决本身，而这是唯一会活得比所有 plan/ledger 都久的文件 |

**FULL 看不到的一笔（执行侧披露）**：FULL 的 subject 止于 `f2507a5`，而当时分支 HEAD 已是 `bed6161`（记 F-4 裁决的那笔，写在 dispatch 之后）。**它未被审过，必须进 VERIFY 的范围**——因此 VERIFY 的 base 取 `f2507a5`，覆盖 `bed6161` + 记录 commit + 整个修复 diff。

**未进本次修复的四条非 blocker（R3：修复限于 §5，塞进去即超出批准边界）**：`F-a` HARNESS-LEDGER 的「同批仍待裁」bullet 仍把 `issues.py` 的 immutability 写成待裁事项（本轮已修）· `F-b` plan 的「否决三项」段与诚实边界段两处仍用「本轮不动 / 仍然悬着」的活语态 · `F-c` C1.6 记录里「诚实边界 3 / 4」的编号对不上（plan 与 commit 正文把 3 和 4 的顺序排反了）· `F-d` `issues.py:70` 的 "Write one observation" 里 `record_issue` 其实不落盘。**四条都是同一类（活文档留着已不成立的旧说法），一并顺下一批兑付。**

**C1.6 的 VERIFY 与收口（2026-07-29）**：VERIFY 判 **`REVIEWED_NO_BLOCKER`**，记录 `v3-review-verify-293f657.md`（逐字提交于 `dd99204`，sha256 `00105cda…`）。**C1.6 三笔预算（FULL / repair / VERIFY）全部用尽，本 plan CLOSED。** reviewer 逐条用命令原样复现四个 blocker 再判修得对不对，并指出**其中两条修得超出最低限度**：`B-2` 把同一错误说法在整份 plan 里对齐（不只被点名那行）、`B-3` 的限定语逐个调用点核过且穷尽。代码那处改动经 **AST 比对**证明行为一字未变。它另查清两件：① **`bed6161` FULL 从没审过**（FULL 记的 HEAD 是 `f2507a5`），这次进了范围，且它的立论前提「模板五个调用点无测试覆盖」被**跨全部五套测试的 coverage 实测**证实——比本轮自己给的证据更硬；② **`B-1` 修出来那句是四句里唯一有测试兜底的**，reviewer 做了一次 mutation 探针（打歪 `resume` → 值级红 → sha256 一致还原）。

**VERIFY 明确不包含的两件**：① 它**不算** `supersession-2` 欠的那次 `E10` 独立 read，且**那次 read 现在要读的是修复之后的文本**；② 它**不是**对 C1.6 整轮的重新认证，只对四条已接受 finding、整个修复 diff 与常设边界负责。

**VERIFY 的三条非阻塞（预算已尽，按 `R9` 兑付）**：① 修复正文里的「ledger 63-65」被同一笔提交挤到 68-70 —— **本收口已改成按内容引用，不再写行号**；② 修复正文称「没改 `contract/` 下的既有文件」而一条命令返回 `M` —— 实质无错（`7011916` 的原始规则冻的是**签名字节**，而该文件明写 UNSIGNED），但 **`E2` 压缩后的措辞读起来比它压缩的规则更宽，欠一句限定**，只能在下次开指令层时补，**留 bank**；③ plan 里一处中文句中混入英文 "already" —— **本收口已改**。

**并发形状第二次发生 —— 待用户裁（`R5`，reviewer 不下结论）**：`bed6161` 是在 C1.6 的 FULL still running 时落到同一分支上的。执行侧按 `E9` 定性为 pre-submission correction，理由是「FULL 尚未发生」——但「发生」指审阅跑完还是判决返回，**是对话里的时间，仓库查不到**，reviewer 按 `UNVERIFIABLE` 标记且**没有任何结论压在它上面**。上下文：C1.6 这个轮次本身就是上一次同样的事逼出来的用户裁决，而 `E9` 写着「每一次逃逸预算上限的记录都是一次改名的轮次」。**第二次是否可接受，是用户的问题。**

**执行记录（2026-07-29，Steps 0–8）**：

- **E10 开轮 cold read：用户判 waive**（规则内出口，非 override——`E10` 的 waiver 条款只覆盖开轮 cold read 那一句，本轮用的正是它）。本轮唯一的 override 是文首那条 `E2`。
- **一处偏离本 plan（执行 session 自裁，交 FULL 复核）**：Step 2 原文「否则走 `pointer(path)`（只有 path）」照字面做会顺手删掉一条**已提交且有测试**的属性——`pointer_to` 文档、并由 `test_pointer_to_a_missing_file_is_a_fault_at_write_time` 守住的**写时存在性 fault**（不算 digest 就不再读文件，fault 随之消失）。`pointer_for` 因此对**所有**字段保留该 fault，只有 digest 是条件的，并补了守卫 `test_pointer_for_keeps_the_write_time_existence_fault_on_every_field`。判据与 Step 4 的裁定同源：不为让新规则通过而删掉一条已记录的属性（`E6`）。
- **净增 8 个测试方法**（plan 预计六条守卫，实到八个：`pointer_for` 的策略与存在性 fault 各一、`resume` 的正负各一、subject 侧的正负各一、`_write_evidence` 的路径形状与 schema 合法性各一）。
- **八条 mutation 探针全部值级红、还原后 sha256 全部 MATCH**（P1/P2 = 同一个门控的两个方向；P3 = STALE 未被钝化；P4/P4b = `resume` 门控两方向；P5 = `pointer_for` 策略；P5b = 存在性 fault；P6 = `_write_evidence`）。红消息原文在 commit 正文。
- **最终计数**：`document_harness` 151 · `document_harness_review` 325 · `tests/harness` 39 · `tests/stage_control` 20 · `tests/run_tests.py` 29 · repo-audit exit 0（基线 147/321/39/20/29）。
- **冻结面复核**：`ResearchSystem/schema/`、`ResearchSystem/contract/`、两个精确 oracle、`assurance/runs/`、`assurance/shadow/` 的 diff 全部为空；三个签名 blob 仍为 `8ad404b1` / `b2dbdf75` / `68031fa2`。
- **未纳入本轮提交**：工作树里的未跟踪目录 `ResearchSystem/docs/`（开轮前即存在，非本轮产物）。

**修订记录（2026-07-29，自检 agent 取证后）**：初版有 6 must-fix / 9 low。已修：`base_commit` 自我卡死（拆成 `round_base` / `plan_commit`）· 两条现存测试会红未列（新增「本轮会打破的现存测试」表）· `resume` 读法歧义（Step 4 裁定为"既报 issue 又留 `present_unverified`"并给了理由）· 被证伪的活文档未列入改动面（Step 5 第三条）· `check_instruction_audit` → `check_audit` · `pointer_to` 调用点 5 → 11（5 活 6 冻结）· 探针数 4 → 6 · Acceptance 三条补命令、两条改成可核形式 · `rsc v3 status` 退出码副作用 · 手写 `pointer()` 路径未封（Constraints + 诚实边界 4）· 冷读先例引用（C0 那次是 override 不是规则内 waive）· 保护集表里 `work_spec_ref` 的理由改成权限论证。**未修、升级为开轮阻塞项**：supersession-1 §3 的 E2 冲突（见文首）。**驳回**：以 p3-corr CRLF 事故为据改保护边界——用户裁定那是编译/工具链问题，不是不知情写偏。
