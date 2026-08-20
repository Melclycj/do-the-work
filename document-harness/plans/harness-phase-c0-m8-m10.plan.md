# Plan: Phase C0 — M8 + M10（让构造轮能跑成 run）

- **slug**: harness-phase-c0-m8-m10
- **created**: 2026-07-28
- **complexity**: 中等
- **status**: **CLOSED** — FULL `CHANGES_REQUIRED`（`bff5f39`）→ 一次 fix（`fbe0b63`）→ VERIFY `REVIEWED_NO_BLOCKER`。预算清零。残留两条 low 见 Notes
- **base_commit**: a918e37
- **base_branch**: document-work-assurance-v3
- **parent plan**: [`harness-deletion-first-stabilization`](harness-deletion-first-stabilization.plan.md) Step 4.6

## Goal (one line)

修 M8 + M10 两条，让一个构造轮能以 run 的形式跑起来——义务逐条有真实状态、v2 的 review 检查有 CLI 入口。

## 范围（用户指定，不自行加）

- **只做 M8 + M10。M9 不做**，留在 Phase C3。
- 披露的残缺：M9 写死读 `review-full.json`、只绑一个 ref、无 `repair_round` 分支，所以 C0 之后**只有「单轮无修复」的 happy path 能跑通**，带修复轮的 bind 仍不完整。

## 两条缺陷的原文（**Acceptance 用这两行的原话，不要转述**）

抄自父 plan 的已验证缺陷表，逐字：

> **M8** | `templates/run-v2/run_evidence_v2.py` (line ~109) | 每个 obligation 无条件写 `IMPLEMENTED`，全文件无第二个 status 字面量 | 模板要求逐条显式 status；缺条目=拒绝

> **M10** | `rsc.py` line ~430 | CLI `v3 review` 仍是 v1 `check_package`；`check_subject`（review_subject.py:319）与 `check_review_result_v2`（review_result_v2.py:66）零 CLI 接线 | `--subject <SHA>` 模式接 v2 双检查

**这次 B2 的教训就在这里**：八项规格只交付两项，成因是执行者把规格转述成了自己更容易满足的版本。所以本 plan 的 Acceptance 段**照抄上面两行的第 3、4 列**，不写"我理解的意思"。

## 开写细节前必须先读的（**读完再写"怎么改"，不要反过来**）

用户 2026-07-28：*"很多错误都是因为 plan 的时候没有好好读现在的 project 里面有什么，导致 plan 和实际该做的有出入。"* 下面每条后面是它要回答的问题；**答不出就不许往 plan 里写对应的结论**。

M8 侧：

1. `ResearchSystem/assurance/templates/run-v2/run_evidence_v2.py` **全文**——除了 `claims` 那个推导式，还有哪里假设"每条都已实现"？人在哪一步决定状态？（现状：没有这一步）
2. `claims` 的消费者：`candidate.build_record` / `candidate.check_record` / `candidate.check_locators` / `views.coverage_report`——**有没有谁把覆盖率算成 `len(claims)/len(obligations)` 而不看 status**？若有，只改模板等于白改。
3. 模板里的 `LOCATORS`——`NOT_IMPLEMENTED` 的条目还需不需要 locator？`check_locators` 会不会因此报错？
4. 现在有没有测试碰这个模板？Phase B 加过 `test_run_v2_template_usable.py` **又在同轮删掉了**，所以很可能是零覆盖——先确认，别假设。

M10 侧：

5. `ResearchSystem/tooling/rsc.py` 约 430 行处的参数面，以及它喂给 `check_package` 的东西。
6. `review_subject.check_subject` 与 `review_result_v2.check_review_result_v2` 的签名：各需要哪些文档、什么顺序、返回什么。
7. v1 `check_package` 还有没有别的调用方 / 测试——CLI 切过去会不会断它们。

共同：

8. 上述路径现有的测试覆盖，确保本轮补的负向测试是新增而不是重复。

## 已经用命令核过的事实（本 session 跑出来的，可直接用；其余一律现读）

| 事实 | 怎么核的 | 为什么重要 |
|---|---|---|
| `candidate-record.schema.json` 的 `fulfillmentClaim.status` enum = `['IMPLEMENTED','NOT_IMPLEMENTED']` | 解析该 schema 打印 enum | **M8 不需要改 schema、不碰 `E2` 冻结面**——词汇已经存在，模板只是从没写过第二个值 |
| `run_evidence_v2.py` 的 `claims` 推导式给每条 obligation 无条件写 `"status": "IMPLEMENTED"` | 读该文件源码 | M8 的缺陷成立；**且它使任何义务枚举（含 C4 的 M11）失效**——完整清单每行自动盖"已实现" |
| `rsc.py:430` 仍调 v1 `v3_review.check_package`；该文件内无 `check_subject` / `check_review_result_v2` 任何引用 | grep 该文件 | M10 的缺陷成立 |

**未验的**：上面读物清单 1–8 全部未做。M8 的"line ~109"与 M10 的"line ~430"是父 plan 的旧行号，**开工时重新定位，不要照抄**。

## §读物清单 1–8 的答案（Step 1 产出，2026-07-28 冷 session 读出，非转述）

**基线（读之前跑的，E3 要求收尾再跑一次）**：五个 suite 全绿 —
`document_harness` 137 / `document_harness_review` 295 / `harness` 39 / `stage_control` 20 / 顶层 P2 29 = **520**。
（父 plan 说的「432」= 前两个之和 137+295，口径对得上。）

### M8 侧

**1. `templates/run-v2/run_evidence_v2.py` 全文——还有哪里假设"每条都已实现"？人在哪一步决定状态？**
除 `claims` 推导式（**line 108–112**，行号已重新定位，父 plan 的「~109」偏一点）外，**没有第二处假设**——但也**没有任何一处拦得住**：
STOP 闸门在 **line 152** 是 `not ok or passed != len(results) or manifest["boundary_result"] != "CONFORMANT"`，
**从不看 claim status**。所以就算模板诚实写了 `NOT_IMPLEMENTED`，这个 run 照样推进到 EVIDENCED 并落 evidence commit。
**人决定状态的那一步：不存在。** 模板里唯一按义务逐条要人填的是 `LOCATORS`（line 56），status 全程由机器写死。
附带一条现状：line 110 的 `LOCATORS[ob["obligation_id"]]` 是**无保护下标**——义务在 `LOCATORS` 里缺条目时是
**KeyError traceback**，不是"拒绝"。所以 M8 的「缺条目=拒绝」现在连崩溃形式的近似都算不上体面。

**2. `claims` 的消费者——有没有谁把覆盖率算成 `len(claims)/len(obligations)`？**
**没有。** 逐个核过：
- `cand.build_record`（candidate.py:312）纯信封，原样 copy `fulfillment`，无 status 逻辑。
- `cand.check_record`（candidate.py:350）invariant 2（**line 375–401**）：每条义务恰好一个 claim，缺→`OBLIGATION-OMITTED`、
  多→`UNDECLARED-CLAIM`、重→`DUPLICATE-CLAIM`。**完全不读 `status`。**
- `cand.check_locators`（candidate.py:468）**line 490** `if claim["status"] != "IMPLEMENTED": continue` ——**读 status，且跳过非 IMPLEMENTED。**
- `views.coverage_report`（views.py:75）**不读 status**，只管 check refs / executor 自签 / wrong-candidate。
- `views.coverage_rows`（views.py:38, 52）读进 `fulfillment_status`（无 claim 时 `"NO_CLAIM"`），`render_coverage`（line 188）打出来。
- `views.mode_summary`（views.py:152）只数 total / review_only / bind_checks，**没有任何以 claims 为分子的比率**。
→ **结论：M8 只改模板即可，不存在"只改模板等于白改"的第二现场。**
→ **但读出一条 plan 没提的**：`check_record` 只数条目、`coverage_report` 无视 status，所以**一条诚实的 `NOT_IMPLEMENTED`
  不会阻断 run**，只会出现在 coverage 表里。这是真实属性，但**不在 M8 的原话里**（M8 说的是"逐条显式 status；缺条目=拒绝"，
  不是"NOT_IMPLEMENTED 阻断"）。**按 `E6` 记为观察，不顺手加机制**——要不要拦是另一条规格，由用户裁。

**3. `NOT_IMPLEMENTED` 的条目还需不需要 locator？`check_locators` 会不会报错？**
`check_locators` 跳过（candidate.py:490），**不报错**。但 **schema 比 plan 记的那条事实强得多**——
`candidate-record.schema.json` 的 `$defs.fulfillmentClaim`（本 session 解析打印确认）：
`NOT_IMPLEMENTED` **必须带 `note`**（minLength 8）且 **禁止带 `implementation_locators`**（`not: {required:[implementation_locators]}`）；
`IMPLEMENTED` **必须带 `implementation_locators`**。
→ 模板必须**按 status 出两种形状**；给 `NOT_IMPLEMENTED` 塞 locator 是 **schema-invalid**，`check_record` 会在 line 352–354 直接早退。
→ 这不是新增机制，是 schema 早就写好的契约——**M8 仍然零 schema 改动，`E2` 冻结面不碰**。

**4. 现在有没有测试碰这个模板？**
**零。** `test_run_v2_template_usable.py` 只剩一个陈旧 `.pyc`；`.py` 已在 `c43a324 V3-GUARD-DELETION-v1` 删除
（`git log --diff-filter=D` 确认）。`test_review_v2_subject.py` 里的 "template" 是无关字串。**先确认了，没假设。**

### M10 侧

**5. `rsc.py` 的 `v3 review` 参数面与它喂给 `check_package` 的东西**
`_cmd_v3_review` 在 **rsc.py:413–459**（父 plan 的「~430」指的是里面 `check_package` 那行，函数头在 413）；parser 在 **607–624**。
参数：`--package`(必) `--spec`(必) `--record`(必) `--check-result`(可重复) `--result` `--executor` `--repo-root`。
三个必填全是**调用者自己给的路径**——正好是 `R2`「你只收到一个 SHA，别的什么都没有」的反面。

**6. 两个 v2 检查的签名**
- `check_subject(subject: Mapping, repo_root) -> Report`（review_subject.py:319）。`subject` 是
  `subject_of(evidence_commit=, candidate_ref=, base_revision=, control_root=, repair_round=)`（review_subject.py:121）产的 5 字段文档。
- `check_review_result_v2(result: Mapping, repo_root, *, evidence_commit: str, executor: str|None=None) -> Report`（review_result_v2.py:66）。
  拿到 v1 result 会 raise `SpecGap`。**它自己在 review_result_v2.py:108 调用 `check_subject`。**
  → 所以把 `check_review_result_v2` 接上 CLI，`check_subject` 自动一并接上。

**7. v1 `check_package` 还有没有别的调用方 / 测试——切过去会不会断？**（本条读出**规格前提被证伪的一半**）
- **`check_subject` 已经有 CLI 接线**，不是"零"：`rsc v3 dispatch --subject <SHA>` → `_cmd_v3_dispatch`（rsc.py:307）
  → `dispatch.dispatch_of`（dispatch.py:250）→ **`check_subject`（dispatch.py:298）**；且 `test_dispatch.py:227` 就是
  专门钉「`check_subject` 有没有被走到」的测试。**缺陷表 M10 那句「`check_subject` … 零 CLI 接线」对 `check_subject` 不成立。**
- **`check_review_result_v2` 确实零 CLI 接线**：全仓 `--include=*.py` grep，只出现在自身模块、`review_subject.py` 的 docstring、
  p3-corr 与模板的 `run_bind_v2.py` 两个 run 脚本、以及测试里。**`rsc.py` 里一次都没有。** 这半句成立。
- **且 dispatch 已经实现了我本来要造的那套推导**：`control_root_of`（dispatch.py:89）+ `resolve_subject`（dispatch.py:144）
  + dispatch.py:290–298 的「从 commit 推 control_root → 从 record 建 subject → 跑 check_subject」。
  **M10 必须复用这些，不得重写**（`E6` + 复用优先）。
- v1 `check_package` 的调用方：`rsc.py:430`，加上历史 run 脚本（`assurance/runs/w1-r1/run_evidence.py:184`、
  `assurance/shadow/**` 的 freeze 脚本）。测试侧**没有**直接调 `check_package` 的，但
  **`test_fix_round_locks.py:233` 用 subprocess 驱动 `rsc.py v3 review` 三个路径参数并断言 exit 1 + 无 traceback**。
  → **切换必须是"加一个 `--subject` 模式"，不是替换 v1 路径**，否则这个测试断掉。

### 共同

**8. 现有测试覆盖，确认本轮补的负向测试是新增不是重复**
- 已覆盖：`V3-CANDIDATE-OBLIGATION-OMITTED`（test_candidate_checks.py:318, 766）；`NOT_IMPLEMENTED` 渲染
  （test_golden_views.py:111, 203）；两个 v2 检查**作为函数**（test_review_v2_subject.py 大量）。
- **未覆盖**：(a) 模板的 status 作者面——模板整体零测试；(b) `v3 review` CLI 除那一条 traceback 测试外无覆盖；
  (c) `check_review_result_v2` **经由 CLI** 被走到。
→ 本轮两个负向测试落在 (a) 和 (c)，**是新增，不重复**。

## Constraints / Out-of-scope

- **冻结面**：signed plan blob `8ad404b1` / contract `b2dbdf75` / supersession-1 `68031fa2`；`ResearchSystem/schema/document-assurance-v3/` 既有文件；`ResearchSystem/contract/` 既有文件。两个 user-locked oracle——`tooling/tests/fixtures/expected-construction-prompt.txt` + `tooling/tests/document_harness/test_readme_enumeration.py`——**动它们须先经用户本人**。
- 每个修复配**敌对负向测试**（红→修→绿）；mutation 探针按 `E4`，从 sha256 校验的 scratchpad 副本还原，**禁 `git checkout --`**（Windows autocrlf）。
- 修复若需要**新增机制** → 停下重新质疑范围（`E6`），不加守卫。
- OUT：M9；M1–M7、M11；Stage 2；memory 侧任何内容。

## Steps

- [x] 0. **`E10` 读债——用户 2026-07-28 裁：waive（既不 ①也不 ②，直接免掉这次 read）。** 四个 commit 用 `git show --stat` 核过，**全部改 `CONSTRUCTION-CHECKLIST.md`**：`079361f`+`a07dec0` 是 B2 的 memory→harness 搬迁（同时改 B2 plan 文件），`5937164`+`a918e37` 是由它长出来的两条规则修订（E3 decision-condition / E6 both-sides）。用户对内容的判断（"这些是把 memory 条目搬进 harness 的活"）与 stat 一致。
  **诚实边界（reviewer 会看到，别当它不存在）**：`E10` 里带 "unless the user waives it" 的只有**开轮 cold read** 那一句；"each amendment passes an independent read before any round relies on it" **本身没有写 waiver 条款**。所以这是**用户对 `E10` amendment-read 的一次明示 override**，不是规则内的既有出口。记在此处以便 FULL 归因，不静默。先例：2026-07-27 Phase A 开轮同类 waive（ledger 有载）。
- [x] 1. 按上面 §读物清单 1–8 逐条读，把每条的答案写进本文件（**先读后写**）。→ 见 §读物清单 1–8 的答案。**读出两条 plan 未记的事实**：①schema 对 `NOT_IMPLEMENTED` 强制 `note` 且禁 locator（M8 的形状因此是两种，仍零 schema 改动）②**M10 的规格前提一半被证伪**——`check_subject` 已经经 `rsc v3 dispatch --subject` 接线（dispatch.py:298），真正零接线的只有 `check_review_result_v2`。
- [x] 2. preview card 已渲染并经用户确认（`E11`）。**M10 范围裁定 = A**：照缺陷表原话做 `--subject <SHA>` 模式，两条 v2 检查都接；v1 `--package` 路径原样保留（否则 `test_fix_round_locks.py:233` 断）。
  **落地形状**（依据 §读物清单 7）：单给 `--subject <SHA>` → 复用 `dispatch.control_root_of` + `read_control_plane` + `subject_of` 推导 subject，跑 `check_subject`；再给 `--result <path>` → 跑 `check_review_result_v2(result, repo_root, evidence_commit=SHA, executor=…)`，**此时不再单独跑推导版 `check_subject`**——它在 review_result_v2.py:108 内部已用 **reviewer 自己写的 subject** 跑过一次，两者是不同文档，重复跑只会出重复 issue。
  **一并披露（不修，供 FULL 看）**：无 `--result` 时 subject 由 record 推导，`check_subject` 的 5 项 identity 交叉核里有 4 项（candidate commit/branch/base/round）因此是自比。**这是既有形状不是本轮引入**——`dispatch.py:290-298` 与模板 `run_evidence_v2.py`（subject 与 record 同出一套 CONFIG 常量）早就如此。`control_root` 一项仍有力（推导自 commit 的 change set，与 record 里 authored 的那份对比）。按 `E6` 不为此加机制。
- [x] 3. **M8 已实施**：`LOCATORS` → `FULFILLMENT`（一条义务一个整 claim，不用并排 dict——ledger 的「不要并排数组」教训）；新增 `build_claims(obligations, fulfillment)` 返回 `(claims, unfilled)`；`main()` 在**载完 spec 后立刻**拒绝，早于任何检查、任何写盘、任何 commit。条目原样 copy-through，所以 per-status 形状规则仍只住在 schema 里，模板不抄第二份。
  测试 `tooling/tests/document_harness_review/test_run_v2_template_fulfillment.py`（7 个）：**先红**（6 error：`build_claims` 不存在；第 7 个 negative control 当时就绿，证明 loader 与基线是好的）→ 修 → 全绿。
  **`E4` mutation 探针**：把守卫改回 `entry.setdefault("status", "IMPLEMENTED")`（复现真实缺陷形状）→ **3 个行为型 FAIL**（`AssertionError: Lists differ: [] != ['ob-two']` 等，**不是崩溃**）→ 从 sha256 校验的 scratchpad 副本还原，还原后 sha256 `8356075763…` 与改前逐字节一致（**未用 `git checkout --`**）。
- [x] 4. **M10 已实施**（范围 A）：`rsc.py` 加 `_cmd_v3_review_subject`；`v3 review` 的 `--subject` / `--package` 成互斥必选组（复用 `v3 dispatch` 同款 argparse 形状），`--spec`/`--record` 降为非必填但**在 v1 分支内显式重新强制**——加第二个模式不得顺手放宽第一个模式的输入。推导全部复用 `dispatch.resolve_subject` / `dispatch.control_root_of` / `review_subject.read_control_plane` / `subject_of`，**未重写一行推导逻辑**。
  测试 `tooling/tests/document_harness_review/test_review_cli_v2_subject.py`（12 个，subprocess 驱动真 CLI）：**先红**（8 failures）→ 修 → 全绿。可达性按 `test_dispatch.py` 的既有手法断言——只有目标函数才会发的 issue code（`V3-SUBJECT-*` 只出自 `check_subject`；`V3-REVIEW-*` 只出自 `check_review_result_v2`），所以「没崩溃」满足不了它。
  **`E4` mutation 探针（两次，各自独立）**：①丢弃 `check_review_result_v2` 的 report → 3 个行为型 FAIL，且 CLI 打出 **`RESULT: sound subject (exit 0)`**——正是 M10 要堵的 fail-open 形状；②丢弃 `check_subject` 的 report → 恰好 1 个 FAIL（点名它的那个）。两次都从 sha256 副本还原，还原后 `76cae3b0d6…` 逐字节一致。
- [x] 5. 验证 + 提交 + dispatch 全部完成：
  - suite 五个：137 / 314 / 39 / 20 / 29 = **539** 全 OK（开工前 520，本轮净增 19）
  - `python Thesis/Work/Tooling/repo-audit.py` 仓根跑 **exit 0**（pre-commit hook 两次 commit 各自又跑一遍，均 clean）
  - 冻结面逐项复核通过（三 blob resolve / 14 schema + 11 contract 无改动 / 两个 oracle blob hash 与 HEAD 相同）
  - commit：`d9ff80a V3-PHASE-C0-M8-M10-v1`（候选，explicit paths、未 amend、未 push）+ `3e27b5f V3-PHASE-C0-LEDGER-POINTER-v1`（ledger 指针 + 两条裁决）
  - dispatch：**`python ResearchSystem/tooling/rsc.py v3 dispatch --range a918e37..HEAD`** → exit 0。
    **base 定死 `a918e37`；tip 用 `HEAD`，不写死。** 理由：写死的 tip 必然落后——记录 tip 的那次 plan 编辑本身
    又是一个 commit，追不上（第一次写 `..d9ff80a`，落了 ledger 那笔；改成 `..3e27b5f`，又落了这次更正）。
    这正是 `dispatch.py` 自己写明的「派生副本会对着生成器变陈旧」，所以此处存**推导方式**而不存**推导结果**。
- [x] 6. **FULL 已回：`CHANGES_REQUIRED`**（记录 `bff5f39 V3-REVIEW-RECORD-PHASE-C0-7572abd-v1`，2 must-fix / 4 low / 4 observation）。评审员独立重跑五 suite、重推每个数字、复核冻结面，M8 / M10 的实现本身**照规格落地无异议**；**两条 blocker 全在测试层**。
  **核心指摘（成立，不辩）**：本轮加了**五道**守卫只探了**三道**，commit 正文却写「both fixes were then mutation-probed」。评审员把五道全探了——**探过的三道都咬得住，没探的两道都咬不住**。
- [x] 7. **修复已落**（`E9` 的那一次 user-approved fix，用户 2026-07-28 批「show me the findings first, then fix」）：
  - **F1** `test_the_version_one_mode_still_requires_its_spec_and_record` 的 fixture 用了**不存在**的 package 路径 → `load_package` 先短路，有无守卫都是 exit 2。已复现（掐守卫 12/12 仍绿；真 defect 是 `TypeError` traceback @ `spec.py:67`）。改为用**能读**的 package + 断言整行 `FATAL: --package mode requires --spec and --record`，并补一条只缺 `--record` 的用例（`E7` 打类不打实例）。
  - **F2** M8 规格原话的「拒绝」半边无测试。已复现（删 `main()` 四行，7/7 仍绿）。补 `TheRunIsRefusedNotMerelyReported` 四条，直接调 `main()`；并把 `EVIDENCE.mkdir` **挪到拒绝之后**——原顺序使「在任何东西被写之前拒绝」对文档为真、对那个目录为假。
    **自己抓到的二次问题**：第一版这四条在 mutation 下是 **ERROR 不是 FAIL**（`main()` 越过守卫后在下游炸），正是 `R8` 说的「崩溃只证明测试碰到了代码，不证明它绑住了行为」。已把 `run_main` 改成捕获并返回 `None`，现在「没被拒绝」表现为 `None != 1` 的**值级失败**。
  - **L1** `HARNESS-LEDGER.md` 的派发范围改 `a918e37..HEAD`（**tip 不写死**——plan 侧修过两次，漏了 ledger 这半边）。**L2** `--check-result` 配 `--subject` 由静默丢弃改为 exit 2 拒绝。**L4** subject 打全 40 hex，不再截 12。
  - **L3 不修**：`3e27b5f` 未按 `E8` 声明 kind，但 `E8` 禁 amend。本次 fix commit 显式声明 kind。
  - **八道守卫全探**（不是三道）：G1 / G2 / G2b / G3 / G4 / G5 / G6 / G7 → **8/8 BINDS，全部值级失败、零 ERROR**；两文件探完 sha256 与探前逐字节一致（`167772b0ca…` / `607210bfe7…`）。探针脚本本身是一次性的，不入仓。
  - 验证（**修复轮那一刻**的口径，非现值）：五 suite **137 / 321 / 39 / 20 / 29**（review 侧 314 → 321，+7）全 OK；repo-audit **exit 0**；冻结面复核通过。
- [x] 8. **targeted VERIFY 已回：`REVIEWED_NO_BLOCKER`**（记录 `v3-review-verify-fbe0b63.md`，2 low / 3 observation，无 blocker）。评审员独立重探了修复所创建或搬动的**五道**守卫，全部 binds、全值级失败零 ERROR；F1 的复现与 FULL 的诊断逐字对上（掐守卫后真的走到 `load_spec(None)`，`spec.py:67` 抛 `TypeError`）。**本轮预算就此清零**：一次 FULL、一次 fix、一次 VERIFY，全部用完。
- [x] 9. **收口**：两条 low 的处置见 Notes；Acceptance 按用户裁 (b) 去数字化。**Phase C0 CLOSED**，回父 plan Step 5（Phase C1）。

## Acceptance (done = ?)

照抄缺陷表原话，不转述：

- [x] **M8**：*"模板要求逐条显式 status；缺条目=拒绝"* —— 且套件里有一个**曾经红过**的负向测试证明"缺条目会被拒绝"。
  → `test_an_obligation_with_no_entry_is_refused_and_never_claimed`（红过：`AttributeError: no attribute 'build_claims'`）+ mutation 探针的 `Lists differ: [] != ['ob-two']`。
- [x] **M10**：*"`--subject <SHA>` 模式接 v2 双检查"* —— 且套件里有一个**曾经红过**的负向测试证明两个 v2 检查真的被调用。
  → `check_subject` 侧 `test_a_check_result_the_plan_orders_but_the_commit_lacks_is_reported`；`check_review_result_v2` 侧 `test_a_result_answering_for_another_commit_is_reported` / `..._naming_another_run_...` / `..._omitted_executor_...`。两侧**都红过**（先 argparse 拒收 `--subject`，后 mutation 各自打回）。
- [x] 读物清单 1–8 每条都有 written 答案在本文件里 → §读物清单 1–8 的答案（8/8，无 `UNVERIFIABLE`）。
- [x] 五 suite 全绿 + `repo-audit.py` 仓根 exit 0 + 冻结面逐项复核（三 blob 仍 resolve / `schema/document-assurance-v3/` 与 `contract/` `git status` 空 / 两个 user-locked oracle 的 blob hash 与 HEAD 相同）。
  **本条只留判据，不留数字**（用户 2026-07-28 裁 (b)，起因 VERIFY 的 V2）：条数与 hash 记在**各 commit 正文**里——commit 不可变，且天然锁定在它测的那一刻；Acceptance 里冻一个总数则必然被下一次修复作废（`E3`：任何对被测对象的后续改动都使该数字失效）。这与本轮已经修过的 dispatch tip 是同一类，同一修法：**存推导方式，不存推导结果**。
  各轮口径：候选见 `d9ff80a` 正文（Step 5 同录）、修复轮见 `fbe0b63` 正文（Step 7 同录）；两者都是**当时那一刻**的记录，不是现值。
- [x] 本轮有独立 review/read 记录，按 `R6` 的命名与渠道。
  → FULL `v3-review-full-7572abd.md`（提交 `bff5f39`，`CHANGES_REQUIRED`）+ targeted VERIFY `v3-review-verify-fbe0b63.md`（`REVIEWED_NO_BLOCKER`）。
- [x] `E10` 读债（Step 0）已清，方式记录在案 → 用户 waive，连同「这是对 `E10` amendment-read 的明示 override、不是规则内出口」一并写在 Step 0。

## Resume pointer

当前指针: **Step 5 已落 commit + dispatch 已生成；等用户把 SHA 路由到独立 review session（`R1` 独立性由用户设题保证，不是由我派 subagent）。** 回来之后走 Step 6 收口，回父 plan Step 5（Phase C1）。

**给 reviewer 的已知披露（别当我藏了）**：
1. **M9 未做**（用户裁，留 C3）：`run_bind_v2.py` 仍写死读 `review-full.json`、只绑一个 ref、无 `repair_round` 分支 → C0 之后**只有「单轮无修复」的 happy path 跑得通**。
2. **M10 的规格前提有一半是假的**，本轮读出来并已按 A 交付：`check_subject` 早已经 `rsc v3 dispatch --subject` 接线（dispatch.py:298），零接线的只有 `check_review_result_v2`。缺陷表那句照抄进 Acceptance 是遵纪律，但它描述的现状不准。
3. **无 `--result` 时 subject 由 record 推导** → `check_subject` 5 项 identity 里 4 项是自比。既有形状（dispatch / 模板皆然），按 `E6` 不加机制。
4. **`E10` amendment-read 由用户明示 waive**（Step 0），不是规则内出口。
5. `NOT_IMPLEMENTED` **不阻断** run（`check_record` 只数条目、`coverage_report` 无视 status）——本轮读出，**不在 M8 原话内故不实施**，供用户裁是否单开一条。

## Notes

### VERIFY 的两条 low — 处置（预算已清零，均不开轮）

- **V2「Acceptance 挂着修复前的数字」——已修**，用户裁 (b)：Acceptance 去数字化，只留判据；条数留在各 commit 正文。理由与 dispatch tip 同类，见 Acceptance 那条。本次 errata 提交。
- **V1「`test_nothing_is_written_before_the_refusal` 断言过宽」——不修，留给下一批碰这两个测试文件的轮次**。
  内容：该断言（拒绝后 `EVIDENCE` 目录不存在）被两件事同时满足——① `mkdir` 正确排在拒绝之后（要的）② `mkdir` **压根不存在**（缺陷）。评审员实探：整行删掉 `EVIDENCE.mkdir`，321 条 review 测试全绿。`E4` 要求每条 must-fire 配负向对照，G2b 这个方向没有。
  **为什么不是 blocker**（三条，评审员给的，我复核同意）：F2 的最小修法是照做的；那行是本轮**搬动**的既有代码不是新增守卫，没有回归；且它缺席**不静默**——第一次实跑就在 `run_evidence_v2.py:189` 的 `write_text` 炸 `FileNotFoundError`。
  **最便宜的关法**：在既有负向对照 `test_a_complete_map_does_not_trip_the_refusal` 里加一句 `assertTrue(EVIDENCE.exists())`——那条跑过了守卫，`mkdir` 应已执行。一行。
- 另有 3 条 observation 只在 VERIFY 记录里，不搬运（O1 L4 注释比代码承诺得多 / O2 v1 拒绝消息的缺陷类只覆盖两三分之二 / O3 新测试的 mkdtemp 无 tearDown）。

### 早先的教训

- **B2 的教训随身带**：①规格的完成标准要照抄，不要转述（八项漏六项就是转述出来的）②`plan` 详细 ≠ 正确——B2 的 plan 很长仍然漏，分界是**事实是不是读出来的** ③声称覆盖率之前先问有没有分母。
- 顺序依据（`M8` 先于 `M11`）：`run_evidence_v2.py` 无条件写 `IMPLEMENTED`，所以 M8 不修则义务枚举为空。对话里一度说过"M11 先做"，**作废**——那是把用户的反对翻译成动作，没有论证。
- `E6` 最后一句已标 **Both sides**，且写明 *"A VERIFY that meets such a fix refuses it."* —— 本轮若遇到"只加规则不改被指出对象"的修法，reviewer 有依据拒绝。
- **一条已知、不修**：`E6` 那句"refuses it"在 `R3` 的 VERIFY 判决集（`REVIEWED_NO_BLOCKER | SPEC_GAP`）里没有直接对应词，推下去落 `SPEC_GAP`。这不是新缺口——`R3` 本来就没有"修复无效"的判决词，`E6` 只是把它照出来。顺本轮 FULL 带走，不为它单开一轮。
