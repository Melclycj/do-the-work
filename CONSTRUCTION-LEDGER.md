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
> **An `R5` observation never enters by a session's own judgment (user ruling 2026-08-26).** A
> reviewer's observation is routed to the user, not filed by the session that received it: at the
> session's preclear it is **put to the user**, and it lands here — or anywhere — only under a
> ruling that says where. A session filing its own observation has closed nothing and has added a
> component, which is the shape those observations are usually about; and the entry it writes has
> no one who reads it and no moment when they would, so it accumulates instead of resolving. The
> one `R5` observation already carried below shows the admissible form: the user ruled it be
> recorded, and it names the moment it is read again. Until such a ruling exists, an observation
> stays where the reviewer put it — its review record, immutable and greppable.
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
> **How long this file may get — measured per entry, not in lines (user ruling 2026-08-26):
> every top-level entry ≤ **1,000** characters, and ≤ 20 top-level entries.** **A machine
> enforces both since 2026-08-28** (user ruling): `tooling/ledger_cap_check.py`, on this repository's
> tracked pre-commit. **Deliberately not in `tooling/hooks/`** — those four files are product
> tier, copied by whoever mounts this harness, and a ledger is each repository's own policy
> rather than the harness's business (io-design §5).
>
> **1,000, down from the 2,500 set two days earlier, and the measurement that moved it.** Of the
> twenty entries standing on 2026-08-28, **fourteen were already under 700** and the
> current-pointer entry was 390; the six above 1,000 were read one by one and every one carried
> the same defect — a batch's narrative written where a pointer belongs. 2,500 had been
> calibrated on the longest entry that existed; 1,000 is calibrated on **what a pointer costs**.
> In English that is roughly 165 words.
>
> **The machine is a ratchet, not a sweep.** An entry written or rewritten must meet the bound.
> The six standing over it are a debt the guard does not call in — **they are trimmed when a
> round next touches them**, never in a batch of their own, because trimming one means
> re-reading the batch it records. Growing one is refused.
>
> **This paragraph used to end "Discipline only, no machine enforces it here", and gave two
> reasons. Both were measured false on 2026-08-28 and are corrected forward rather than
> rewritten** (`HD-59`). *"A second checker would be new machinery"* — not a second one: a
> `ledger_cap_check.py` lived here until 2026-08-12, when batch B R3 moved it to the caller,
> pinned there to the caller's own ledger, on the ground that a ledger is the caller's concern
> (io-design §5) — and **this repository acquired a ledger of its own seven days later**
> (2026-08-19, round `LEDGER-SPLIT`), with no machine following it. The count for this file was
> zero. *"for a file with one writer"* — one writer is precisely what discipline failed to
> restrain: three breaches in a single session on 2026-08-28, at 3,231 / 2,815 / 2,582
> characters, each caught only because the writer stopped to measure by hand.
>
> **What the machine does not judge**: whether an entry's content belongs in a ledger at all.
> That is the paragraph above's rule, it is a reading rather than a measurement, and it stays
> with the independent review — a short entry full of narrative passes the guard.
>
> **Why the unit changed, measured 2026-08-26.** The bound was 180 lines, and the file reached it
> while the thing it exists to stop had already happened *inside* a line: one entry — the CLOSED
> roll — is a single line of 26,110 UTF-8 bytes / 16,171 characters, **48.9% of the file's bytes**,
> and **56.7% of all entry content**, where the next largest entry is 2,405 characters. A
> line-count bound cannot see growth that never adds a line, and the blocked event this paragraph
> has always named is the 20-to-300-line session, not line 181. Characters per entry can see it;
> lines never could. **2,500 is calibrated on this tree rather than chosen**: every entry except
> the CLOSED roll is under it, the largest at 2,405. 20 entries against today's 17 leaves room for
> the batches in flight and nowhere near enough to absorb a round's narrative.
>
> **The new bound fired on the day it was written, and that was it working.** The CLOSED roll
> breached at 16,171 characters — 17,128 by the time it moved. The remedy is the one this header
> has always named, and it was carried out on **2026-08-28** under a user ruling: the roll was
> moved into [the archive](CONSTRUCTION-LEDGER-archive.md) verbatim, leaving a pointer entry
> here. The archive permits exactly that — its own marking forbids *appended narrative* (a
> round's narrative belongs in its review record and commit body) and not the relocation of
> closed pointer material, which is how that file came to exist at all ("Moved verbatim, nothing
> deleted, nothing retyped"). That move was its own ledger batch, gated by a user ruling under
> the 2026-08-03 rule rather than by a round. **Never compress meaning out of a live pointer** —
> move it to where detail belongs: a journal (not bound to a round since 2026-08-28), the round's
> plan, the commit body, or the review record.

## ▶ 当前指针 — 只放指针与未结裁决（理由与叙事进各轮 commit 正文 / round record）

- **CLOSED —— 已关闭的批次与轮次全卷**：2026-08-28 原样搬入
  [archive](CONSTRUCTION-LEDGER-archive.md) 的「CLOSED 卷」节（17,128 字符，占本档字节近半，
  自 2026-08-26 新上限立起当日即超标 6.8 倍）。名与锚全在那里，可 grep；链条、blocker、修法、
  预算一如既往在各轮 commit 正文与 `migration/document-work-assurance-v3/` 的 record / journal。
  **2026-08-30 第二次搬入（用户裁「closed 全部撤走」）**：余下九条 CLOSED 条目——保障面二期复盘 ·
  HI-REDEEM-5 · harness 对外 I/O 边界 · 批 B · 拆分批 · 批 `CORE-SET` · 批 `FREEZE-TO-ALARM` ·
  契约 v4 · 新调用者 onboarding——亦原样搬入同一节；本档自此只剩指针、未结裁决与开着的批。
- **用户 08-06/08-07 裁决（只此一处）**：编号态 · host 表进指令 · route α 兼读 `P3-inventory.md`
  §5 证据列 · **option A 作废、改裁重扎根**——`de4c37a` 携带修好的 checker，候选**继承**而非写入，边界不放宽
  （两路实测皆不通：留 = `chk-boundary` 越界，退 = 误判 R2 的锚点追加）· **f2 接受现状记局限**（第 9 行锚点
  只覆盖 liveness 半边；P6 会 hash 该位置，改被锚句标陈旧、改真正该盯的句无人知）· **f3 不采信并被 VERIFY
  独立追认**（`cwd` 被读成仓库根，spec 记 `ResearchSystem/tooling`；`ob-r12-tier` 因此回到 SUPPORTED）。
  `HI-route` 已闭（2026-08-22/23 轮 `PRERUN-RIDERS` 裁决 3：观察路由成文化入 `REVIEW.md`，行兑付删除）；
  重扎根这条裁决仍只活在 commit 正文/台账/本行。
- **`O-1` 已裁：维持现状、承担风险**（用户 2026-08-06；理由与三组实测在跨轮设计判断 journal
  [`context-exemption-2026-08-06.md`](document-harness/journal/context-exemption-2026-08-06.md)）。不取消
  Context 豁免、不改声明式、不加机器。**剩余风险**：Context 里若写「**要交付的内容**」且漏映射又无证据，
  仍是 `SPEC_GAP`（停机 + 重开 START）；process/scope 类按 `REVIEW.md` 豁免只报告。
- **未结（open）**：**`E11` 载体问题已裁关（2026-08-21，user，本行即承载）**：不造批准载体——
  笔在 orchestrator 手里，仓内「用户批了」永远是主张不是证据，载体是零增益机器（`E6`）；
  可由脚本重新推导的就不记录。构造轮的卡**不落盘**（开轮前无产物可供脚本读），评审记录照记
  `UNVERIFIABLE`/`R7` 天花板；产品 run 的授权本体＝冻结的 control plane，其人类可读渲染
  **已脚本化**（轮 `PREVIEW-RENDER` CLOSED 2026-08-21，`dtw preview`，`HD-51`）· **异地副本已解决**（调用者分支推
  `origin/document-work-assurance-v3`，**该仓 2026-08-23 实测 private——匿名 API 404、匿名
  `ls-remote` 要求认证；原「public 仓、用户知情后重申」记录以此更正（用户当日「改」裁决，
  见 stranger-guards.plan.md fix-gate 节 ruling 4）**；新仓 =
  `Melclycj/do-the-work`，**2026-08-24 起 public**（公开化三批收官同日用户翻转，实测 API
  visibility=public；建仓时 private，本句更正随 preclear 落），`HD-40` ① 关闭）·
  **④ 审计拆层**
  （E topology-claim 项已删——2026-08-12 用户裁：源头追不到，
  按其自带处置删除、不带进 v4）。批 B 的 preclear 三条已各归其家、不占本区：`HD-38` 追认与
  `HD-37` ③「旧行不回溯」在各自条目，commit 正文违 `E8` 的纪律与根因在
  [journal §8](document-harness/journal/batch-b-2026-08-11.md)。 · **charter 轮留下两条 `R5` 归口用户的问题（2026-08-18）**：**① 已由轮 `EXECUTOR-CHARTER` 关闭（2026-08-22，`HD-53`：构造侧 charter=`CONSTRUCTION-CHECKLIST.md`，`dtw dispatch --construction-executor` 送达）**；② `R9` 的 wording-level 通道要不要立一个可枚举物**仍开**——实证：一条 banked 小修在同一轮内碰了三次 README 都没搭上车。
- **已裁但只存在于对话里的（一行一条）** —— 2026-08-17 清理：**十条已被别处承载或已消耗者整段
  搬入 [archive](CONSTRUCTION-LEDGER-archive.md)**（判据＝该条已由指令层正文 / 已签载体 / 决策簿条目
  说话，或是一次性且已用掉），**留下六条**，都是今后仍会被反复援引且层内确无别家的：
  **`E8` 的 one dense paragraph 买密度与无 trailer，不要求字面单段**（2026-08-07，HI-REDEEM-5 L-4）·
  **ledger 批分型（2026-08-03）**：ledger 删减/记账批不开轮，user ruling 即 gate（`bf70d89` 先例
  追认，`0f2ab2c` 的 dispatch 依此撤销）；规则变更批照旧走轮 · **ledger/riders-only 的 finding 修
  不算 `E9` 的「一次用户批准的修」（2026-08-04）**：判据＝改的是不是被评审的 work product，不消耗
  修腿、不欠 targeted VERIFY——`HD-23` 明写它是本条的外延，故本条不可搬 · **C4 `O-1`（2026-08-01）：
  (a)+观察条款——记录义务住 `EXECUTION.md` Authoring gate 段（每个产品 run 的 closeout 记一行，
  到此为止）；读数与改判 2026-08-25 裁归构造轮，本行是它唯一的家（`HD-58`，收窄 `HD-54`）**：
  分歧恒零或恒 paragraph 侧对 → 议 (c) 段落诞生义务，恒 unit 侧对 → 议 classification 列去留，
  两侧各有贡献 → 转常设 ·
  **`F-4` 模板守卫不加、等真 run**（条件未到）· **`E10` 收敛循环第五圈若再出 must-fix 则考虑整删
  digest**（瞄准 C1.5 那五个字段，不是 `E2`；条件未触发）。
- **`R5` 观察：工具键扫类关不掉「调用者解析不到」这一类（用户 2026-08-30 裁「账本单立一项」）**：
  批 `CORE-ONLY` 两轮共六次 pre-FULL 修正 + 轮 2 的两个 blocker，每一圈关掉的都只是当时那把量具看得见的
  形状——`sweep_refs` 只认路径与文件名，漏裸标识符；grep 文件名漏裸 `R<n>`；grep「nine」漏清单外的
  文件；反引号 7 位 commit id 两把量具都看不见（rider `caller-cannot-resolve-ids`）。会话形态那一半
  `HD-69` 已答；**量具这一半未答**：要么换量法（在剥史树上以调用者视角逐 token 解析，而非按写法
  grep），要么承认扫类对此类只能靠独立评审兜底。**再读时刻（用户裁，只此一处）：任何验收靠「对产品
  层扫类」来量的批开轮时**——下一个即轮 3 `CORE-ONLY-RUN`。来源 FULL `v3-review-full-70c82b4.md` `O-3`。
- **bank** → [HARNESS-RIDERS.md](HARNESS-RIDERS.md)（2026-07-29 迁出，一行一 rider；兑付=同 commit 删行）。

---

## 待办 backlog — 构造侧

- **批 `CORE-ONLY`（构造侧降级为 harness 的普通调用者；三轮 `LAYER`→`CODE`→`RUN`，跨两个仓；裁决与处置全在
  plan [`core-only.plan.md`](document-harness/plans/core-only.plan.md)）：轮 1 `CORE-ONLY-LAYER` CLOSED 2026-08-30**
  （base `db1bfa1`；FULL `8997d94` → 修 `c7f9c8d` → VERIFY `8214f50`）。**轮 2 `CORE-ONLY-CODE` CLOSED 2026-08-30**
  （base `fff2203`；冷读 `69a9a71` → 候选 `70c82b4` → FULL `affacc2` → 修 `894bc92` → VERIFY `552b405`；成员 9→7、
  构造侧 dispatch 独立、剥史树指向仪器持有物者 4→0）。**轮 3 `CORE-ONLY-RUN` OPEN 2026-08-30，仪器侧 base
  `78d51ac`**（item F：真产品 run 在调用者 `D:/Thesis-stage-control-refactor` 开，调用者侧 base `2b1ad3b`、挂载 `3060a23`；裁决 39–43：sparse 只留 59 件 + 冷会话禁网 · 调用者收轮路由改回自己根上的簿 · run 由调用者里新起的冷
  orchestrator 会话跑 · 读审计 hook · 开轮冷读窄形；run 的活＝P5C A4 amendment 草案）。轮 `V1-RESULT-RETIRE`
  CLOSED 且已合入 `main` 2026-08-29（PR #2 → `b6c40a2`）。其后：候选隔离 · dispatch-economy。分发形态由 `HD-66`
  承载。**⚠ 本档 20/20 条已顶满**。
- **公开化三批 —— 让本仓成为适合公开的 git repo**（用户方向 2026-08-23；同日并裁：产品 run 首跑**不归本仓**，在调用者仓另行开工）：**批 A 门面件**（LICENSE + 双平台 CI——ubuntu 腿即本仓首次 POSIX 验证、顺势兑 rider `posix-mode-wording`；根 README 除锈兑 `readme-cli-stale`）· **批 B 重签打包批**（契约 v4 + 已签件除锈——`six-signed`/`design-route`/`io-hiroute-stale` 等的那个「打包批」）· **批 C 陌生人可用性**（`chk-caller-prefixes` 设计题 + `amend-exempt-caller` + ONBOARDING 第二调用者实证 + 10 解析点并入）。两裁已收（2026-08-23：**MIT** · **A→B→C**，载体 `document-harness/plans/publicization-a.plan.md`）。**批 A = 轮 `PUB-FACADE` CLOSED 2026-08-23**（见指针卷；「余一件用户动作：push 首跑 CI」**已陈旧**——实测 `gh run list` 2026-08-24：用户已于 2026-08-23 起三次 push、三次 CI 全绿，首跑发生于批 A 收批当日 05:21；本句更正随轮 `STRANGER-PROOF` 收批落，依其 plan 变更面所载）。**批 C 增列一件：观众向根 README 重写**（用户 2026-08-23 问「面向观众的 README 在哪批」，对话中拟归批 C——第二调用者实证的实走记录即 quickstart 素材，符合 commands-over-claims；切法批 C 开轮时再裁。现根 README 无假话但仍是 agent/内部视角）。**批 B = 轮 `CONTRACT-V4` CLOSED 2026-08-23**（见指针卷；v4 已签署生效 `HD-56`）。**下一队首＝批 C 陌生人可用性**，清单增至六件：`chk-caller-prefixes` 设计题 · `amend-exempt-caller` · ONBOARDING 第二调用者实证 · 10 解析点收尾 · **观众向根 README 重写**（2026-08-23 对话拟归此批）· **§10.5 两问立案**（分发形态 submodule vs plugin 安装 · `.claude/` 下要不要放 harness 件——用户 2026-08-23 裁「立案挪后」，本行即其家，批 C 开轮时摆给用户裁或另开独立轮）。**批 C 已开且第一轮 CLOSED（2026-08-23）**：开轮四裁（切两轮 `STRANGER-GUARDS`→`STRANGER-PROOF` · `submod-index` 接下 · §10.5 批 C 收批带实证再裁 · 冷读照派）载 plan `stranger-guards.plan.md`；**轮 `STRANGER-GUARDS` CLOSED**（见指针卷——六件中前四件落定：`chk-caller-prefixes` 设计题 + `amend-exempt-caller` + 10 解析点 + `submod-index` 顺带）。**下一队首＝轮 `STRANGER-PROOF`**（第二调用者实证 + 观众向根 README 重写），其收批时裁 §10.5 两问。**轮 `STRANGER-PROOF` ＋ 插入批 `SUBMOD-HOOKENV` 已于 2026-08-24 合并收批 CLOSED**（见指针卷）；批 C 六件全落，**仅余 §10.5 两问**（分发形态 submodule vs plugin · `.claude/` 放不放 harness 件）——收批当日携实走证据摆给用户，答案届时另记。**已裁（2026-08-24，user「维持吧」）：两问皆维持现状——分发形态维持 submodule（实走刚证可用、pin 即版本追溯，plugin/包装等真外部需求出现再议，`E6`）· `.claude/` 不放 harness 件（实走九条零触及，且该区在守卫 VENDORED 豁免盲区，治理件不进盲区）。§10.5 就此关，**批 C 整体 CLOSED**。**仓已于 2026-08-24 翻 public**（用户动作，批 C 收官同日；实测 `visibility=public`）；调用者仓同日 gitlink bump 至 `733cb80` 并按用户裁决收窄其 repo-audit 扫描面（caller commit `931a3fa`，rider `decited-paths` 跨仓兑付毕）。**该队首已由轮 `README-BILINGUAL` 消费**（2026-08-24 落 `2522ce1`，用户 2026-08-25 裁免轮；见指针卷 CLOSED 卷末）。**轮 `RIDER-SETTLEMENT` 已于 2026-08-25 CLOSED**（见指针卷；bank 30→16）。**本仓下一队首＝dispatch-economy 构造批**（原两件 + 本轮增列的九条 design rider，见下条）；**产品 run 首跑不在本仓**，在调用者仓另行开工。**该队首已于 2026-08-25 由批 `CORE-SET` 接过**（用户当日方向 + 当日即令推进，见下第二条）；dispatch-economy 顺延其后。

- **dispatch-economy 构造批候选**（用户 2026-08-24 裁「往后记」，排批 C 之后、无 deadline）：把派发省时纪律做实——① must-fix 结对复读的**窄 subject 出单形态**（`E10` 通道原文本就是 "re-read of the amended text"，而 `dtw dispatch --read` 只有全层形态；命令面改动按 `HD-47` 逐案归用户）② 快 read 并入 executor 无 commit 窗口的重叠纪律找承载。**本批已增列第三件（用户 2026-08-25 裁，轮 `RIDER-SETTLEMENT` 开批裁决 3）：bank 里 13 条 design rider 中的 9 条并入本批一次收**——六条在 checklist 的 `E9`/`E10`/`R9`/`R10` 措辞面（`wl-route` / `hd38-both-ways` / `e9-pair-budget` / `e10-cannot-see` / `read-name-split` / `waiver-live`），三条在 `ORCHESTRATION.md` 义务表面（`charter-qualifiers` / `e1-table` / `e1-reader`），与本批要动的正是同两个表面；余 4 条是机器题（`pin-drift` / `delta-prose` / `argv-cap` / `freeze-audit`）另候用户裁。**`R5` 观察一条**（FULL `8aa9f6e` `O-4`，用户 2026-08-25 裁「先记下」）：bank 现存 16 行中 13 行需开轮才可兑，该比例是否说明 bank 没在做它该做的事，**待本批收完 9 条、bank 降到 7 行时再评**。起因＝轮 `STRANGER-PROOF` 开轮读链约一小时 wall-clock，一个表格单元格的修被按全层复读（1640 行 + 电池重跑）；教训当轮曾写进该轮 plan 的 Dispatch economy 节，但**写于其所辖派发已跑完之后，用户指其无效**——本行才是排期载体。**与批 `CORE-SET` 的交叠（2026-08-25 记）**：本批领的九条 design rider 里有两条
  （`charter-qualifiers` / `e1-table`，`ORCHESTRATION.md` 义务表面）与一条（`waiver-live`，`E10`
  cold-read/`§live` 句）的触碰面，正是 `CORE-SET` 轮 1 item A 要改的两处；哪批兑付按 `CORE-SET`
  plan 的开轮问题 4 归用户裁：已裁**只兑 `waiver-live`**，另两行留 bank 待本批。**第一件（窄 subject
  出单形态）新增第二笔实测成本**：`CORE-SET-LAYER` 开轮读因无窄形态而手工缩范围，把生成器**故意不给**
  的成员名单又贴了回去（`dispatch.py` 注释记着为何不给——手写成员表错过一次）；本次未造成锚定错误
  （派发标了「自己验」、读者独立重推），但按 `O-2` 挂在本件下（read `9f1de08` `O-2`）。

- **候选隔离机制已丢失 —— 设计题立案（用户 2026-08-27 提出，未裁是否开轮）**：用户批准的 v3 执行计划
  `document-harness/plans/document-work-assurance-harness-v3.plan.md:119` 明写「All payload writing
  occurs on an isolated Git candidate branch/worktree … `REJECT` or `REPLAN` preserves the candidate
  ref but never promotes it」，2026-08-05 journal 称其为**常驻纪律**，且**真被用过**（本档记 run `w1-r1`
  的候选分支）。**今日实测：仓内仅 `main` 一条分支，executor 的 commit 在任何评审看见它之前就已落主线**；
  幸存的只有 `E9` 的评审窗口，而它守的是**记录**不是候选。结构性后果：一个 `CHANGES_REQUIRED` 判定
  **无法**靠「不合入」执行，只能靠事后补一个修的 commit，而那个 commit 又消耗该轮唯一的修腿。
  是否恢复、以何形态恢复，归用户。
- **设计批 `ASSERT-OWNER` —— REVERTED 2026-08-15**（用户裁，依据 `E6`「a rule added about it is not the fix」）：它试图把 `HD-41` 写进指令层，装的过程中自身又出七个同类实例，FULL 返 `CHANGES_REQUIRED`；五个指令层文件已回 `ff05b01`、blob 逐一核对，checklist 回 204 行 / 12 条。诊断钉在 journal [`structure-vs-prose-2026-08-15.md`](document-harness/journal/structure-vs-prose-2026-08-15.md)；过程见 plan [`harness-assertion-owner-design.plan.md`](document-harness/plans/harness-assertion-owner-design.plan.md)。**四件未结已由用户 2026-08-16 一次裁完**：① 该轮 `E9` 预算＝撤回不消耗腿、不欠 VERIFY，该轮就此结账 ② rider `wl-route` 推迟（行不动、redeem-when 照旧，到期未兑的事实留在 FULL 记录里）③ `HD-41` **不再试**指令层承载，永久只住决策簿（用户裁不建条目，锚即本行；`HD-5` 的 §live 必读使其仍可达）④ 决策簿准入口径**维持**——构造批无 choice JSON，其裁决继续只活在 commit 正文，代价照记。

---

历史轮次叙事 + 592 行 control-plane interlock + backlog 完整版：
[`CONSTRUCTION-LEDGER-archive.md`](CONSTRUCTION-LEDGER-archive.md)（只读，勿续写）。
