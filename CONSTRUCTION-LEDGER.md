# CONSTRUCTION LEDGER — the instrument's own development record

> **What this is.** The pointer file for the rounds that built *this* harness — the record side
> of [`document-harness/CONSTRUCTION-CHECKLIST.md`](document-harness/CONSTRUCTION-CHECKLIST.md),
> which is the rule side. It lives beside the two other governance registers it works with:
> [decision log](HARNESS-DECISIONS.md) (user rulings) and [rider bank](HARNESS-RIDERS.md)
> (banked findings).
>
> **What may enter.** Only two things: the **current pointer** (which construction batches are
> CLOSED, which are open, what the next queue head is) and **construction-side rulings that have
> no other home**. Everything else has an owner and goes there: a new user ruling →
> `HARNESS-DECISIONS.md` (`HD-1`); an unresolved finding → `HARNESS-RIDERS.md`; a round's
> narrative → its own review record under `migration/document-work-assurance-v3/` plus its commit
> body, both immutable and greppable — restating it here is a second copy that drifts; the
> reasoning behind a ruling → `document-harness/journal/<round>-<date>.md`.
>
> **What does not enter.** Anything belonging to a *caller*: a caller's closeout obligations, its
> ledger parameters, its machine wiring, its router state. A caller keeps its own account of using
> the instrument; on the repository that grew this harness that account is its
> `ResearchSystem/HARNESS-LEDGER.md`.
>
> **Where the bytes came from.** The entries below were moved out of that caller — `D:/Thesis`
> (worktree `D:/Thesis-stage-control-refactor`, branch `document-work-assurance-v3`) at commit
> `7c54507`, from its `ResearchSystem/HARNESS-LEDGER.md` — by the round `LEDGER-SPLIT`, which
> overturned the "ledger 留调用者" half of `HD-28` by user ruling of 2026-08-19. The history that
> file carried travels with them as
> [`CONSTRUCTION-LEDGER-archive.md`](CONSTRUCTION-LEDGER-archive.md), byte-identical to its
> source at `acbc553` (source blob `50d3e66e`, still readable at `7c54507` in the caller) and
> since then diverging in exactly two bytes-worth of link target: `:559` and `:576` named two
> records of *this* repository through the caller's mount, so the mount prefix was stripped and
> they resolve here. Narrative, wording and its own former title are untouched — history is not
> rewritten to match its new shelf, and a pointer to a file in this same repository is not
> narrative.
>
> **Caller paths inside these entries are historical facts, not links.** A closed round that ran
> against the caller's product tree names that tree — `handoffs/…`, `assurance/runs/…`,
> `.goals/LEDGER.md`. Those tokens resolve in the caller, not here, and are left exactly as they
> were written; the same rule as the archive's title.
>
> **How long this file may get: 180 lines, discipline only — no machine enforces it here.** The
> caller's `ledger_cap_check.py` is pinned to the literal string `ResearchSystem/HARNESS-LEDGER.md`
> and is the caller's machine, not this repository's (io-design §5); this repository's tracked
> hook runs `layer_path_check.py` alone, and this file is not an `E10` member, so nothing sees it.
> A second checker would be new machinery for a file with one writer, which `E6` names as the
> signal to re-question rather than to guard. The bound is not the caller's 120: that 120 was set
> on a file carrying *both* accounts, which measured 113 lines at the split, and this file is the
> construction half alone — it measured 130 before this paragraph existed and `wc -l` at the
> commit that declares the bound is the figure to trust. 180 leaves room for several CLOSED-roll
> entries and nowhere near enough to absorb a round's narrative, which is the blocked event, the
> same one the caller's cap names: the 20-to-300-line session, not line 181. When it is reached,
> move the oldest closed material into the archive; never compress meaning out of a live pointer.

## ▶ 当前指针 — 只放指针与未结裁决（理由与叙事进各轮 commit 正文 / round record）

- **CLOSED（此处只留名与锚；链条、blocker、修法、预算全在各轮 commit 正文与
  `migration/document-work-assurance-v3/` 的 record / journal——不可变、可 grep）**：v3 迁移
  N0–N4 · wave 1/2 · p3-corr · Phase A/B/B2/C0/C1/C1.5/C1.6/C2/C3/C4/D · 指令层 amendment 轮
  （指令层成员 9 条）· Stage 2 `p4-bridge` · Stage 3 P4-CODE · Stage 4 `p4-doc`——**P4 全程
  ②–⑦ 完成，`P4-IMPL-v1` effective**（链锚 `handoffs/P4-close.md`；签字记录
  `migration/document-work-assurance-v3/a1-p4-activation-successor-signature.md`）· p4-doc 三
  triage + 维护批/rider 兑付轮 · O-5 amendment read（record `10c040b`）· run `p5a-firewall`
  （A2 已签已激活 `6295346`）· run `p5a-shells`（148 壳 promotion `d749406`）· pre-START
  优化维护批 · 回归电池分层批（tiering 规则落 run-v2 README，该节即 revert unit）· **撤回轮
  `E10-D-NARROWING`（净变化零，closeout `4ab1db1`）· 设计轮 `E2-REBASELINE-DESIGN`（closeout
  `e55d304`）· 构造轮 `E2-VERB-E10-PIN`（record `c667d08`）· run `p5b-firewall`（A3 已签 `935cada`、
  已激活 `959104d`；closeout `89383b1`，FULL record `v3-review-full-fef3a2e.md`）· 精简轮 `SIMP-ABCD`
  （closeout `214f743`）· `V1-CONTEXT-EXACT` · `SIMP-A4` · run `p5b-claims`（153→173 objects，promotion `3074ce4`，closeout `efa56ea`；FULL `v3-review-full-8ad8c2f.md` + VERIFY `v3-review-verify-275da5b.md`）· **批 A（A1+A2，2026-08-10 收批）**——A1 链 `a7bb1d6`→`fd058aa`→`7a08265`；A2 五轮链在 plan 步骤注与 `V3-A2-R*-CLOSEOUT` commits，batch:A 裁决 retired 入 decisions-archive、`HD-18` implemented，收批 commit `V3-A2-CLOSE-v1`** · 设计轮 `BATTERY-REPO-SCOPE`（2026-08-18，仪器仓内第一个构造轮：全档电池六条按**被验证的仓**分档、doc-only 例外句改按子句读、revert anchor 标明其价已是设计轮，`HD-45`；rider `battery-travel`/`tier-file-vs-clause`/`tier-scope` 兑付删行，`layer-crossrepo-token`/`layer-outbound-refs` 新入 bank；read `v3-cold-read-28501fe` 0 must-fix，`E9` 三腿全程未花） · 设计轮 `ORCHESTRATOR-CHARTER`（2026-08-18；orchestrator 的角色说明书立为 `E10` **第十成员**，走收窄形——九条已在层里的义务只点名归属并指向规则 id、三条层内零承载的写正文；`E1` 的「派发即独立」由充分条件改为必要非充分并加中间态披露句，`HD-46`；rider `E1-suff` 兑付删行，`e1-disclose-home` 与 `charter-qualifiers` 新入 bank；三次独立 read 收敛——2 must-fix → 1 → **0**，`E9` 三腿全程未花）· 轮 `CALLER-ONBOARDING`（2026-08-19，第三期：onboarding 九条 + 两模板 + 第七命令 `dtw init` + `layer_path_check` 归位；九条在临时仓实跑、两支守卫各见拦一次放行一次；FULL `CHANGES_REQUIRED`（hook 提交成 100644 · 测试少钉一条头部规矩）→ 一次用户批准的修 → VERIFY `REVIEWED_NO_BLOCKER`，`E9` 三腿走满；`HD-47`/`HD-48`，五条 rider 新入 bank；记录 `v3-{cold-read-c22e229,review-full-2026a14,review-verify-4029b43}.md`）。· 轮 `LEDGER-SPLIT`（2026-08-19，批 DTW-INDEPENDENCE R1：仪器开发史入本仓——本账本 + archive + 16 份构造 plan，17 件逐 blob 对账；调用者账瘦 113→57 行；FULL `CHANGES_REQUIRED`（搬入 plan 内 10 条挂载前缀死链）→ 一次用户批准的修 → VERIFY `REVIEWED_NO_BLOCKER`，`E9` 三腿走满；`HD-49` 取代 `HD-28`、`HD-50` 取代 `HD-48`；记录 `v3-{cold-read-7701f03,review-full-e74be07,review-verify-8f1ad1d}.md`）。· 轮 `XREPO-REFS`（2026-08-20，批 DTW-INDEPENDENCE R2：指令层不再写调用者路径——`E10` 收caller-held-path 条款、四处降名、`E1` 披露句得载体与责任人、`E10` provenance 死从句删除，零守卫代码改动；开轮 read 返 1 must-fix（层内 15 处裸 commit id 无家）→ amendment `48b6c5f` + 复读 `c53fc4e` 结对；FULL `CHANGES_REQUIRED`（新条款把守卫说大了）→ 一次用户批准的修（收口径；守卫认全类改入 R3）→ VERIFY `REVIEWED_NO_BLOCKER`，`E9` 三腿走满；V-1/O-3 字节走自由通道 `34a5ae9`；rider 三删五增二细化；记录 `v3-{cold-read-69fc082,checkpoint-read-48b6c5f,review-full-dd18226,review-verify-2937bcd}.md`，journal `xrepo-refs-2026-08-20.md`）。journal 在 `document-harness/journal/<轮名>-<日期>.md`。
- **保障面二期复盘 CLOSED（2026-08-03）**：底账 + 六裁决在 `document-harness/journal/retro-2026-08-03.md` §7 与 `22b27aa`
  正文。后续指针三条：audit 降本收在 (d)（下个产品 run 先测新 cadence 基线）· (c) 跨 freeze 继承挂起 ·
  (b) 轮数封顶压后。
- **HI-REDEEM-5 CLOSED（2026-08-07）**：FULL + 一次修腿 + targeted VERIFY 均
  `REVIEWED_NO_BLOCKER`；锚 = [`journal`](document-harness/journal/hi-redeem-5-2026-08-07.md) +
  [plan](document-harness/plans/harness-issue-redemption-batch.plan.md)。P5C 归根 LEDGER/独立 plan，不归本账本。
- **用户 08-06/08-07 裁决（只此一处）**：编号态 · host 表进指令 · route α 兼读 `P3-inventory.md`
  §5 证据列 · **option A 作废、改裁重扎根**——`de4c37a` 携带修好的 checker，候选**继承**而非写入，边界不放宽
  （两路实测皆不通：留 = `chk-boundary` 越界，退 = 误判 R2 的锚点追加）· **f2 接受现状记局限**（第 9 行锚点
  只覆盖 liveness 半边；P6 会 hash 该位置，改被锚句标陈旧、改真正该盯的句无人知）· **f3 不采信并被 VERIFY
  独立追认**（`cwd` 被读成仓库根，spec 记 `ResearchSystem/tooling`；`ob-r12-tier` 因此回到 SUPPORTED）。
  `HI-route` 未闭：重扎根这条裁决同样只活在 commit 正文/台账/本行。
- **`O-1` 已裁：维持现状、承担风险**（用户 2026-08-06；理由与三组实测在跨轮设计判断 journal
  [`context-exemption-2026-08-06.md`](document-harness/journal/context-exemption-2026-08-06.md)）。不取消
  Context 豁免、不改声明式、不加机器。**剩余风险**：Context 里若写「**要交付的内容**」且漏映射又无证据，
  仍是 `SPEC_GAP`（停机 + 重开 START）；process/scope 类按 `REVIEW.md` 豁免只报告。
- **未结（open）**：**`E11` 预览卡在仓内无承载**（R2 的 FULL 与 VERIFY 各记一次
  `UNVERIFIABLE`/`R7` 天花板：卡渲染在对话里、用户批了，但仓里查不到）· **异地副本已解决**（调用者分支推
  `origin/document-work-assurance-v3`，**public 仓、用户知情后重申**；新仓 = private
  `Melclycj/do-the-work`，`HD-40` ① 关闭）·
  **④ 审计拆层**
  （E topology-claim 项已删——2026-08-12 用户裁：源头追不到，
  按其自带处置删除、不带进 v4）。批 B 的 preclear 三条已各归其家、不占本区：`HD-38` 追认与
  `HD-37` ③「旧行不回溯」在各自条目，commit 正文违 `E8` 的纪律与根因在
  [journal §8](document-harness/journal/batch-b-2026-08-11.md)。 · **charter 轮留下两条 `R5` 归口用户的问题（2026-08-18，此前只活在该轮 closeout 正文）**：① construction executor 的 charter 要不要有载体（product-run 那半有路径，构造轮那半无人管）② `R9` 的 wording-level 通道要不要立一个可枚举物——实证：一条 banked 小修在同一轮内碰了三次 README 都没搭上车。
- **「harness 对外 I/O 边界」整条 CLOSED 2026-08-13**（随批 B 收批；两件均已落地——接线 `HD-25`、
  解耦 `HD-31`）。supersession-2 签字 2026-07-30 记录 `migration/…/supersession-2-signature.md`；
  理由错模式已裁——历史两例接受、今后判据 = `E3` 断言条款。
- **已裁但只存在于对话里的（一行一条）** —— 2026-08-17 清理：**十条已被别处承载或已消耗者整段
  搬入 [archive](CONSTRUCTION-LEDGER-archive.md)**（判据＝该条已由指令层正文 / 已签载体 / 决策簿条目
  说话，或是一次性且已用掉），**留下六条**，都是今后仍会被反复援引且层内确无别家的：
  **`E8` 的 one dense paragraph 买密度与无 trailer，不要求字面单段**（2026-08-07，HI-REDEEM-5 L-4）·
  **ledger 批分型（2026-08-03）**：ledger 删减/记账批不开轮，user ruling 即 gate（`bf70d89` 先例
  追认，`0f2ab2c` 的 dispatch 依此撤销）；规则变更批照旧走轮 · **ledger/riders-only 的 finding 修
  不算 `E9` 的「一次用户批准的修」（2026-08-04）**：判据＝改的是不是被评审的 work product，不消耗
  修腿、不欠 targeted VERIFY——`HD-23` 明写它是本条的外延，故本条不可搬 · **C4 `O-1`（2026-08-01）：
  (a)+观察条款**——gate 不改；自 Phase E 起每个真 run 的 review/closeout 记一行两 map 分类对照（含各
  map 由谁/哪个 session 填，同源填写不独立、不计入样本）；改判条件：分歧恒零或恒 paragraph 侧对 →
  议 (c) 段落诞生义务，恒 unit 侧对 → 议 classification 列去留，两侧各有贡献 → 转常设 ·
  **`F-4` 模板守卫不加、等真 run**（条件未到）· **`E10` 收敛循环第五圈若再出 must-fix 则考虑整删
  digest**（瞄准 C1.5 那五个字段，不是 `E2`；条件未触发）。
- **bank** → [HARNESS-RIDERS.md](HARNESS-RIDERS.md)（2026-07-29 迁出，一行一 rider；兑付=同 commit 删行）。

---

## 待办 backlog — 构造侧

- **批 B —— 「谁调用、谁绑定」CLOSED 2026-08-13**（plan
  [`harness-batch-b.plan.md`](document-harness/plans/harness-batch-b.plan.md)）：R1 `run_all` 接线
  （`HD-25`）· R2 io-design v1 签字（`HD-35`）· R3 ledger 解耦（`HD-31`）· R4 三角色重指 +
  rider `tier-scope` 三件 · R5 `E10` 通道放松 + `R10` rider 到期判据（`HD-36` 留 live——其②层内
  无承载；`HD-37`/`HD-38` implemented）。③ `E2` 不加守卫已裁不做，重开条件＝拆分批（`HD-27`，
  rider `PD` 重定范围）。**R4/R5 用 `E10` 独立 read 而非 FULL，`E9` 三腿两轮全程未花**；五份 read
  记录 `migration/…/v3-checkpoint-read-{be9878a,0aed595,8884f47,136f27f,f61ce2c}.md`。

- **拆分批 —— harness 搬成独立仓**（`HD-18`）：**整批 CLOSED 2026-08-17**，五轮——R0 设计 · R1 搬 254 件 + 执行 `HD-39` 的删除 · R2 摘 CLI 成 `dtw` · R3 调用者侧接线 · R4 记账收批。**结果**：新仓 = private `Melclycj/do-the-work`，产品仓以 gitlink 钉住 `ResearchSystem/harness`；pre-commit 改 tracked 且三支守卫从 submodule 跑；记账断言定终局（调用者 `HARNESS-POLICY.md` §4）；八条 rider 逐条有归宿；`HD-33` / `HD-28` / `HD-15` / `HD-10` 转 implemented。**「重扎根轮」原定三件，2026-08-18 拆开做**——第一件 CLOSED（轮名 `SPLIT-COPY-RETIRE`：调用者副本 273 件删除 + 入链重写；FULL `CHANGES_REQUIRED` → 修 → VERIFY `REVIEWED_NO_BLOCKER`，`E9` 三腿走满；记录 `v3-review-{full-2d148f3,verify-bef77f3}.md`，两份都留在调用者仓——那一轮的 subject 是调用者的树）。**余下两件仍未排期，且「重扎根轮」这个名字自此不再指任何单一轮次**：② 去 `ResearchSystem/` 前缀与 `REPO_ROOT` 深度（实测只 2 处 `parents[4]` 会断）+ `E10-sync` 三处同改（须同一 commit）③ 步骤 19 的十一个 `--repo-root` 解析点。**三条 rider 的 deadline 原文指向「重扎根轮」，按此重指**：`mount-inert` 与 `PD` → 第 ② 件（`$H` 与冻结面都在那一刻动）· `submod-index` → **deadline 已于第一件到达且未付**，改指下一个碰 `paths.py` / `candidate_path_check` 的批。`nonrec-clone` 已兑付（第一件删副本 + `repo-audit` 认挂载点）；`battery-travel` 已于 2026-08-18 轮 `BATTERY-REPO-SCOPE` 兑付删行（其 deadline 即「第一个于 harness 仓内开的构造轮」，那一轮就是）。五轮叙事在各轮 commit 正文与 `ResearchSystem/migration/document-work-assurance-v3/` 的评审记录里，不在账本重写。plan [`harness-repo-split.plan.md`](document-harness/plans/harness-repo-split.plan.md)。**三期至此全部 CLOSED（2026-08-19，第三期见下方 onboarding 项）。批 DTW-INDEPENDENCE（`HD-50`，取代 `HD-48` 排期）四轮：R1、R2 已 CLOSED（2026-08-19/20）；下一队首 = R3 去前缀**（重扎根第②件 + `E10-sync` 三处同 commit + 守卫认全类 + `sweep_refs.py` 入仓——后两件系用户 2026-08-20 自 R2 改入，见 `HD-50`），收尾 R4 `dtw init` 命令面。原三期
  排序把它排在已 CLOSED 的第一件之后、onboarding 第三期之前（详见下方 onboarding backlog 项）。
  **契约 v4 让位**：本行此前写「下一队首 = 契约 v4」，那是三期排序之前的话；契约 v4 仍在 backlog，
  未取消、未排期。
- **设计批 `ASSERT-OWNER` —— REVERTED 2026-08-15**（用户裁，依据 `E6`「a rule added about it is not the fix」）：它试图把 `HD-41` 写进指令层，装的过程中自身又出七个同类实例，FULL 返 `CHANGES_REQUIRED`；五个指令层文件已回 `ff05b01`、blob 逐一核对，checklist 回 204 行 / 12 条。诊断钉在 journal [`structure-vs-prose-2026-08-15.md`](document-harness/journal/structure-vs-prose-2026-08-15.md)；过程见 plan [`harness-assertion-owner-design.plan.md`](document-harness/plans/harness-assertion-owner-design.plan.md)。**四件未结已由用户 2026-08-16 一次裁完**：① 该轮 `E9` 预算＝撤回不消耗腿、不欠 VERIFY，该轮就此结账 ② rider `wl-route` 推迟（行不动、redeem-when 照旧，到期未兑的事实留在 FULL 记录里）③ `HD-41` **不再试**指令层承载，永久只住决策簿（用户裁不建条目，锚即本行；`HD-5` 的 §live 必读使其仍可达）④ 决策簿准入口径**维持**——构造批无 choice JSON，其裁决继续只活在 commit 正文，代价照记。

- **契约 v4 —— 把 s1/s2 合并回一个文件**（用户意向 2026-08-04）：§13 自身已允许（"corrections create
  a versioned successor"，v4 即 successor），**不需改 §13、不需 s3**。带进去：s1 四句（§4 control-root
  图行 · §7 invariant 9 · §7 invariant 11 · §8 step 7）+ s2 一句（§3 state-pointer digest）· 清掉契约
  自身 frontmatter 的 `status: candidate-awaiting-user-signature` 自相矛盾（清了之后
  `N1/governance-exemptions.json` 的契约那半可退役）· 两份 s 顶部 "UNSIGNED" 残迹随文件消失。
  （E topology-claim 项已 2026-08-12 按用户裁删除、不带进 v4；「s1 的 S1 改过 §4 topology」这一
  事实仅留此提示。）真代价 = 签 v4 前整份读一遍——这正是"签过=读过"那个等式的价钱。

- **新调用者 onboarding —— CLOSED 2026-08-19**（轮 `CALLER-ONBOARDING`，三期收官）：九条准备工作
  自此有清单且**被实跑验证过**——`document-harness/ONBOARDING.md`（每条＝做什么/怎么看出生效/归谁）+
  decision-log 与 rider-bank 两个空模板 + 第七个命令 `dtw init`（`HD-47`：§1 的「六命令原样」读作搬迁
  指令、非命令数上限）+ `layer_path_check` 归位（仪器仓自己的 tracked hook，十成员 10/10 解析；调用者
  `HARNESS-POLICY.md` §3 与其 `.githooks/pre-commit` 注释同批更正）。**三条诚实上限照记**：无网故 submodule
  源是本地克隆 · Windows 长路径要额外开关 · **作者在自己机器上走自己写的流程，不构成陌生人能照着走的
  证据**——真正的第二个调用者才关得掉后两条。

---

历史轮次叙事 + 592 行 control-plane interlock + backlog 完整版：
[`CONSTRUCTION-LEDGER-archive.md`](CONSTRUCTION-LEDGER-archive.md)（只读，勿续写）。
