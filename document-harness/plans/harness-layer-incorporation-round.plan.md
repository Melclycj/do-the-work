# Plan: Layer 收编轮 — bank 治理散文入 E10 层 + 11 行层系 rider 清仓

- **slug**: harness-layer-incorporation-round
- **created**: 2026-07-31
- **complexity**: 复杂
- **status**: done
- **base_commit**: bf73536
- **base_branch**: document-work-assurance-v3

## Goal (one line)

按用户 2026-07-31 裁决把 bank 的治理散文（三条规则+兑付惯例+bank↔HarnessIssue 分工句）收编进 `E10` 指令层（迁入 `CONSTRUCTION-CHECKLIST.md`，riders 退为纯数据表），并在同一 amendment 轮里兑付全部 11 行层系 rider——一批、一次 FULL、一次层 read 清掉 bank 的一大半。

## Why / value

层外累积的 actor-binding 规则（O-3v 报的形状）从此受层纪律管（改动欠 read、有第二双眼睛）；bank 11/19 的债一次清偿；E8 kind 词汇缺口修掉后不再每轮产生自造 kind 的 commit（C3 一轮出过两个）。

## Context to resume cold

**本轮是什么**：一个真 amendment 轮（改 `E10` 层文本 = "adding a clause … is design and opens a round"），走完整轮机械：E11 卡 → 候选 → FULL →（如有 blocker：≤1 次 user-approved fix + targeted VERIFY）→ **最终层字节的 amendment read**（用 `rsc v3 dispatch --read`，reform 轮加的第三 family）。预算按 `E9`；read 不占预算。

**裁决出处（不要重新裁）**：`HARNESS-LEDGER.md` 「已裁但只存在于对话里的」bullet 的 **2026-07-31 条**（commit `bf73536`）——bank 保留（分工：bank=构造侧债，HarnessIssue=产品 run 观察、schema 治理、CLOSED 后准入）；bank 治理散文收编入层；**ledger 的 citation 规则不收**（ledger 绑定度在 I/O 批未决）。backlog 首条即本轮。

**必读文件（开工顺序）**：
1. 本 plan 全文
2. `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` — 被修订的规则书（E1–E12/R1–R9；本轮动 E2/E8/E10/E12 + 新增 bank 规则 + `REVIEW.md` 一处）
3. `ResearchSystem/HARNESS-RIDERS.md` — 档头（待迁文本的单一真相源，现有三段：兑付惯例+路由、2026-07-30 三条收紧、backfill 记录）+ 19 行数据
4. `ResearchSystem/HARNESS-LEDGER.md` — 指针/已裁/未结槽/backlog
5. `ResearchSystem/tooling/hooks/layer_path_check.py` — 碰层文件的 commit 会触发什么，先读再提交
6. `ResearchSystem/migration/document-work-assurance-v3/v3-cold-read-ae4df09.md` §1 — 八成员 blob 基线（开轮 cold read 的 citation 覆盖判据）
7. 轮次惯例样例：`ResearchSystem/document-harness/journal/c3-2026-07-30.md`（journal 结构）、`R6`（record 命名）、C3 各 commit 正文（E8 commit 纪律）

**11 行层系 rider 清单**（id · 一句话 · source；**最小修法以 Step 2 回源为准，本表只是索引**）：

| rider | 一句话 | source |
|---|---|---|
| BC-1 | `E10` 免费通道扩展条款文本落地（(a) 裁定：record 携字节/点名内容的 low 即时套用、同 must-fix 待遇；实质在 ledger 已裁行 2026-07-30 条） | (a) ruling · ledger |
| E10-d | `E10` 延后条款「不新增条款」管不住替换/删除 | checklist read chain（Step 2 定位具体 record） |
| F-1r | `E10` 免费通道子句与「no round has relied」限定句的接缝（字面替换同时加界时谁赢未定） | v3-review-full-8ec4c60.md F-1 |
| L-2r | citation 覆盖依赖 read record 载成员 blob id，但无规则要求 record 必须载 | v3-checkpoint-read-d58969d.md L-2 |
| E2-t | `E2` 的 *existing* 未钉时刻（也见 451e8b0 O-3：同一未钉使 schema-description 条款不可达） | dcced4e / 451e8b0 reads |
| E2-s2 | 签字后的 supersession-2 blob `e1a2f26b` 是否入 `E2` 冻结清单（对称 supersession-1）【**需用户裁**；carrier 的 UNSIGNED 残留受契约 §13 约束、不改 carrier 字节】 | 签字批 · v3-checkpoint-read-403fc9a.md L-1 |
| O-4r | `E12` "never a written SHA" 未限定「记录进文件的 range」，与 CLI 打印全 SHA 字面相抵 | v3-cold-read-451e8b0.md O-4 |
| O-6 | `E8` 五种 commit-kind 盖不住 amendment/ruling/record 批（四次实证：af2905c O-6、403fc9a O-2、ae4df09 O-2、C3 两个 record commit）【**需用户裁词表**】 | v3-review-full-af2905c.md O-6 |
| V-c | `E10` qualifier 吞掉对比破折号（纯措辞，R9 级，搭本批） | v3-review-verify-f054a08.md V-c |
| O-1 | `E10` 已 7+ 子句、增长系 finding 驱动（R5 形状观察）【**需用户裁：E10 拆不拆**——本轮又要往层里加文本，正是表态时机】 | v3-review-full-af2905c.md O-1 |
| VB-1 | review 判据（repo 现实为判据、requirement 当问题清单）落 `REVIEW.md` 明文 | 2026-07-29 修理批 ruling（reform records：8ec4c60/49d9829 附近） |

**关键事实（已核，可引用）**：
- `HARNESS-RIDERS.md` **不在** `E10` 八成员清单（ae4df09 冷读逐一数过；C3 VERIFY 复核）——收编后它仍在层外、行编辑照旧免 read；进层的是**规则文本**（住进 checklist），不是文件本身。**不要**把 riders 文件加进 E10 成员表或 `layer_path_check.LAYER`。
- 三条 bank 规则曾被 `f0e5d64` VERIFY 顺带审过（repair diff 一部分），但从未受过以条款文本为 subject 的 read——本轮的层 read 补上这道。
- dispatch base 用 **`0224176`**（C3 verify-closeout）：让三笔未独立审过的记账 commit（`0a3d18d` backfill、`4ad1184`+`bf73536` ledger 记录）落进本轮 FULL 视野——用户已认可此意图。
- 开轮 cold read 照 `E10`：八成员 blob 对 `ae4df09` 记录逐一 `git rev-parse` 比对，未变则引用覆盖（C3 先例，derivation 记入 journal+候选 commit 正文）；有变则用户路由 read。C3 全轮未碰层，大概率未变——**现场重核，勿信此句**（E3）。
- `E2` 冻结面每 commit 复核：signed plan blob `8ad404b1`（`.goals/plans/document-work-assurance-harness-v3.plan.md`）/ contract `b2dbdf75` / supersession-1 `68031fa2` + `schema/document-assurance-v3/` pack + 两个 user-locked oracle（`tooling/tests/fixtures/expected-construction-prompt.txt`、`tooling/tests/document_harness/test_readme_enumeration.py`）。E2-s2 若裁「入」，改的是 **checklist 里 E2 的清单行**，绝不动 supersession-2 本体字节。
- 五 suite 基线（C3 收口时）：29 / 20 / 39 / 169 / 354 + `repo-audit.py` exit 0——纯文本轮也每 commit 跑。
- commit 正文与 plan 忌讳：大写前缀+连字符+F+数字（如 FIX 后接 -F1）拼成的串会撞 repo-audit 的
  fragment-ID 扫描（C3 的 fix commit 标题实踩过一次，本 plan 落盘时原样引用它又踩了第二次）；写
  finding 名一律用带连字符的 `F-1` 形，别把那种串原样写进任何入库文本。

## Constraints / Out-of-scope

- `E10` 修订纪律：additive or subtractive，**never re-typed "with the same content"**；每处编辑对应一个点名的 rider/裁决，不顺手改别的。
- 修法与源 finding 的最小修法对齐（`E6` both-sides：finding 点名的文本要改，不许用"加规则"替代改文本）。
- 三个【需用户裁】项（E2-s2 / O-6 词表 / O-1 拆否）+ bank 规则落点（建议：R9 之后新增一条，编号顺延）全部摆上 E11 卡，得到裁决才动笔。
- OUT：ledger citation 规则（裁定不收）；I/O 批议题（run_all 接线、ledger 绑定、bank export）；C4/M11；产品代码；两份 contract stub；一切 `E2` 冻结字节。
- 一个 session 一个角色：FULL/VERIFY/read 由用户路由独立 session，执行侧绝不自审（`E1`）。

## Steps

- [x] 1. **开轮预检**：读必读清单 1–7；`git rev-parse HEAD` 对 `base_commit`（漂了先 diff 看变化）；核 bank 仍 19 行、riders 档头三段仍在；读 `layer_path_check.py` 知道碰层 commit 会触发什么。（2026-07-31 done：HEAD=c61d82d，漂 3 笔记账 commit 无冲突；bank 19 行✓ 档头三段✓）
- [x] 2. **逐 rider 回源**：11 行各自打开 source record 读 finding 原文，抄录其最小修法（找不到最小修法的记 SPEC 缺口，卡上标注）；BC-1 的条款实质从 ledger 已裁行取。产出 per-rider 修法清单（journal 草稿，`document-harness/journal/layer-inc-<date>.md`）。（done：journal/layer-inc-2026-07-31.md；E10-d 无逐字最小修法，SPEC 缺口已标）
- [x] 3. **cold read 处置**：八成员 blob 对 `ae4df09` 逐一比对；未变→引用覆盖记档；有变→请用户路由 read。（done：八成员全 SAME，成员集仍 8，引用覆盖零预算，derivation 在 journal）
- [x] 4. **设计修订文本**：bank 规则条目（三条+兑付惯例+分工句，从 riders 档头迁移、只删不重打）；11 处 rider 修订各自成稿；riders 档头收缩稿（指针一行+表）。（done：9 处修订稿全文在 journal §Drafted revision texts；R10 落点=R9 块后；C-3→E10 活引用替换已披露）
- [x] 5. **渲染 E11 卡**（首行=买到什么/多久用/不做会怎样；逐条列每处编辑+三个待裁项+落点建议+dispatch base `0224176`）→ **等用户 OK + 三项裁决**。（done 2026-07-31：卡 OK；③ 明示不拆；①=入、②=+amendment/ruling/record 随卡建议采纳——记录方式见 journal）
- [x] 6. **执行**：checklist / REVIEW.md 修订；riders 档头收缩 + 11 行同 commit 删除兑付；journal 记 RED 无（纯文本轮无测试面——如实写明，勿硬造）；候选 commit（explicit paths；kind 命名注意 O-6 新词表若已裁可首用）。（done：9 处编辑落地；五 suite 29/20/39/169/354 绿 + repo-audit 0 + 冻结面四 blob 复核;候选 commit 见 git）
- [x] 7. **验证 + 派发**：五 suite + repo-audit + 冻结面每 commit；`rsc v3 dispatch --range 0224176..HEAD`；freeze marker 落地后本分支停写直到 record 回。（done：候选 feacb86 每 commit 全绿；dispatch 发出，freeze 持守至 record 回）
- [x] 8. **FULL 判决处置**：REVIEWED_NO_BLOCKER→收口；CHANGES_REQUIRED→findings 先摆给用户、批准后一次 fix + targeted VERIFY（fix 若再碰层文本，read 落在修后字节上——af2905c O-5 先例）。（done：REVIEWED_NO_BLOCKER，record commit 6132828；L-1 走 byte-channel 套用 7463229——通道首用；L-2 用户裁 bank→L-2li 行；fix+VERIFY 未动用）
- [x] 9. **层 read**：`rsc v3 dispatch --read` 派最终层字节的 amendment read（用户路由）；record 落地（`R6` 命名）。（done：subject 784e49b，record v3-checkpoint-read-784e49b.md commit f196fb7；0 must-fix、1 low（L-1lr 入 bank）、4 obs；L-1 三处套用的搭车 read 同场结清）
- [x] 10. **收口**：ledger 指针（NEXT=Phase C4）+ 本 plan status=done + journal 终稿；bank 应剩 ≤8 行；若 FULL/read 对三笔记账 commit（`0a3d18d` 等）有 finding，按 bank 新规则（现已在层内）处置。（done：11 行旧债全清；bank 现 10 行=8 旧余+2 本轮新收（L-2li/L-1lr）——"≤8"写于新 low 未知时，指旧债清仓，新债新记；记账 commit 无 finding，FULL O-1 的 E8-scope 问题留 record 归用户）

## Acceptance (done = ?)

- checklist 承载 bank 规则全部内容（三条+兑付惯例+分工句），riders 档头= 指针+纯数据表；**riders 文件仍不在层内**。
- 11 行层系 rider 全部在其修法落地的同 commit 删行；每处层文本编辑可追溯到点名的 rider/裁决，无一处顺手改动。
- 三个待裁项各有用户裁决记录（journal/卡/commit 正文任一，ledger 已裁行汇一行）。
- 轮链完整且按 `R6` 命名：卡 OK → 候选 → FULL record →（fix+VERIFY 如动用）→ 层 read record → 收口；dispatch base = `0224176`。
- 每 commit：五 suite 绿 + repo-audit exit 0 + `E2` 冻结面复核（三 blob + schema pack + 两 oracle）。
- ledger：指针推进 NEXT=C4，本轮裁决入已裁行；bank ≤8 行。

## Resume pointer

当前指针: **done**（2026-07-31 全轮闭环：候选 feacb86 → FULL 6132828 RNB → byte-apply 7463229 → bank ruling 784e49b → read record f196fb7 → 收口 commit）。NEXT = Phase C4（见 `ResearchSystem/HARNESS-LEDGER.md`）。

## Notes

- 用户裁决链回放（防冷 session 误读）：2026-07-30 用户曾倾向不收（理由：bank/ledger 存废未定，不给可能要拆的结构立法）→ 2026-07-31 确认 bank 保留（以 bank↔HarnessIssue 分工为前提）后**翻案为部分收编**；ledger citation 规则因绑定度未决而不收——原理由对它仍成立。
- 本轮先于 C4 是用户选的顺序（收编在前：clause 上下文热、先清账、O-6 止血、C4 得稳定规则书）。
- riders 档头的 backfill 记录段（2026-07-30 那段）随收缩处置：内容已在 `0a3d18d` commit 正文，档头可只留一行指针——设计时定，卡上披露即可。
- 若执行中发现某 rider 的最小修法需要**新机制**（非文本修）→ 停下按 `E6` 质疑，单列给用户，不并入本轮。
