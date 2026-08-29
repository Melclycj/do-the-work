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
  (a)+观察条款——记录义务住 `EXECUTION.md` Authoring gate 段（每个产品 run 的 closeout 记一行，
  到此为止）；读数与改判 2026-08-25 裁归构造轮，本行是它唯一的家（`HD-58`，收窄 `HD-54`）**：
  分歧恒零或恒 paragraph 侧对 → 议 (c) 段落诞生义务，恒 unit 侧对 → 议 classification 列去留，
  两侧各有贡献 → 转常设 ·
  **`F-4` 模板守卫不加、等真 run**（条件未到）· **`E10` 收敛循环第五圈若再出 must-fix 则考虑整删
  digest**（瞄准 C1.5 那五个字段，不是 `E2`；条件未触发）。
- **bank** → [HARNESS-RIDERS.md](HARNESS-RIDERS.md)（2026-07-29 迁出，一行一 rider；兑付=同 commit 删行）。

---

## 待办 backlog — 构造侧

- **轮 `V1-RESULT-RETIRE` CLOSED 且已合入 `main` 2026-08-29**（PR #2 → `b6c40a2`；FULL
  `REVIEWED_NO_BLOCKER` `be59ad6`）：v1 评审 schema 退役，pack 15→14，电池 830，`E9` 修腿未花。三条用户
  裁决（`HD-63`/`HD-64`/`HD-65`）、十二条验收与逐条处置全在 plan
  [`v1-result-retire.plan.md`](document-harness/plans/v1-result-retire.plan.md)。**队首 ＝ 批 `CORE-ONLY`
  （构造侧降级为 harness 的普通调用者；三轮 `LAYER`→`CODE`→`RUN`，跨两个仓——轮 3 产品 run 首跑在
  调用者仓 Thesis）：轮 1 `CORE-ONLY-LAYER` 于 2026-08-29 OPEN，`base_commit` = `db1bfa1`**；十八条
  裁决、量程、验收与轮 1 步骤清单全在 plan
  [`core-only.plan.md`](document-harness/plans/core-only.plan.md)，本条只留指针。其后：**候选隔离**
  （未裁是否开轮）· **dispatch-economy**。分发形态由 `HD-66` 承载。**⚠ 本档 20/20 条已顶满**——要新增
  条目须先按抬头 archive 程序腾位。
- **批 B —— 「谁调用、谁绑定」CLOSED 2026-08-13**（plan
  [`harness-batch-b.plan.md`](document-harness/plans/harness-batch-b.plan.md)）：R1 `run_all` 接线
  （`HD-25`）· R2 io-design v1 签字（`HD-35`）· R3 ledger 解耦（`HD-31`）· R4 三角色重指 +
  rider `tier-scope` 三件 · R5 `E10` 通道放松 + `R10` rider 到期判据（`HD-36` 留 live——其②层内
  无承载；`HD-37`/`HD-38` implemented）。③ `E2` 不加守卫已裁不做，重开条件＝拆分批（`HD-27`，
  rider `PD` 重定范围）。**R4/R5 用 `E10` 独立 read 而非 FULL，`E9` 三腿两轮全程未花**；五份 read
  记录 `migration/…/v3-checkpoint-read-{be9878a,0aed595,8884f47,136f27f,f61ce2c}.md`。

- **拆分批 —— harness 搬成独立仓**（`HD-18`）：**整批 CLOSED 2026-08-17**，五轮——R0 设计 · R1 搬 254 件 + 执行 `HD-39` 的删除 · R2 摘 CLI 成 `dtw` · R3 调用者侧接线 · R4 记账收批。**结果**：新仓 = private `Melclycj/do-the-work`，产品仓以 gitlink 钉住 `ResearchSystem/harness`；pre-commit 改 tracked 且三支守卫从 submodule 跑；记账断言定终局（调用者 `HARNESS-POLICY.md` §4）；八条 rider 逐条有归宿；`HD-33` / `HD-28` / `HD-15` / `HD-10` 转 implemented。**「重扎根轮」原定三件，2026-08-18 拆开做**——第一件 CLOSED（轮名 `SPLIT-COPY-RETIRE`：调用者副本 273 件删除 + 入链重写；FULL `CHANGES_REQUIRED` → 修 → VERIFY `REVIEWED_NO_BLOCKER`，`E9` 三腿走满；记录 `v3-review-{full-2d148f3,verify-bef77f3}.md`，两份都留在调用者仓——那一轮的 subject 是调用者的树）。**余下两件仍未排期，且「重扎根轮」这个名字自此不再指任何单一轮次**：② 去 `ResearchSystem/` 前缀与 `REPO_ROOT` 深度（实测只 2 处 `parents[4]` 会断）+ `E10-sync` 三处同改（须同一 commit）③ 步骤 19 的十一个 `--repo-root` 解析点。**三条 rider 的 deadline 原文指向「重扎根轮」，按此重指**：`mount-inert` 与 `PD` → 第 ② 件（`$H` 与冻结面都在那一刻动）· `submod-index` → **deadline 已于第一件到达且未付**，改指下一个碰 `paths.py` / `candidate_path_check` 的批。`nonrec-clone` 已兑付（第一件删副本 + `repo-audit` 认挂载点）；`battery-travel` 已于 2026-08-18 轮 `BATTERY-REPO-SCOPE` 兑付删行（其 deadline 即「第一个于 harness 仓内开的构造轮」，那一轮就是）。五轮叙事在各轮 commit 正文与 `ResearchSystem/migration/document-work-assurance-v3/` 的评审记录里，不在账本重写。plan [`harness-repo-split.plan.md`](document-harness/plans/harness-repo-split.plan.md)。**三期至此全部 CLOSED（2026-08-19，第三期见下方 onboarding 项）。批 DTW-INDEPENDENCE（`HD-50`→retired 入档）四轮全 CLOSED（2026-08-19/21；R4 = 轮 `INIT-SURFACE`，判据入层 + 分工收拢）。构造轮 `PREVIEW-RENDER` 已于 2026-08-21 CLOSED（见当前指针 CLOSED 卷）**。**第 ③ 件的数已按现场重测更正：不是十一个而是 **12 个解析点 / 7 个文件**（`cli.py` 6 个 `args.repo_root else` @ `:43 :80 :147 :329 :414 :462` + 5 个 parser site，`init` 与 `preview` 两个新命令使原数作废；run-v2 六脚本各 1 个 `parents[3]`）。其中**会当场咬人的 2 个已由轮 `TEMPLATE-LIB-ROOT` 修掉**（2026-08-21/22 CLOSED），**余 10 个**（`cli.py` 六 + 六脚本的 `parents[3]` 默认，后者只在不传根时才走到，而今天所有调用都传）。**轮 `EXECUTOR-CHARTER` 已于 2026-08-22 CLOSED**（见当前指针 CLOSED 卷；其 plan——[`executor-charter.plan.md`](document-harness/plans/executor-charter.plan.md)——载的四条用户裁决与一个未答问题均已消费，问题的答案即 `HD-54` 的读数时刻裁决）。**下一队首＝公开化三批（用户 2026-08-23 改队，见下条）**；重扎根第③件余下的 10 个解析点退居其后、拟并入公开化批 C（实测今天不咬人：`cli.py` 六个不传即取 cwd、六脚本的 `parents[3]` 对调用者布局解析正确）；契约 v4 并入公开化批 B。**第③件的 10 个解析点已由轮 `STRANGER-GUARDS` 清零（2026-08-23，批 C 第一轮）——十二处全数改「git 发现或响亮拒绝」，步骤 19 一脉就此全部关闭。**
- **公开化三批 —— 让本仓成为适合公开的 git repo**（用户方向 2026-08-23；同日并裁：产品 run 首跑**不归本仓**，在调用者仓另行开工）：**批 A 门面件**（LICENSE + 双平台 CI——ubuntu 腿即本仓首次 POSIX 验证、顺势兑 rider `posix-mode-wording`；根 README 除锈兑 `readme-cli-stale`）· **批 B 重签打包批**（契约 v4 + 已签件除锈——`six-signed`/`design-route`/`io-hiroute-stale` 等的那个「打包批」）· **批 C 陌生人可用性**（`chk-caller-prefixes` 设计题 + `amend-exempt-caller` + ONBOARDING 第二调用者实证 + 10 解析点并入）。两裁已收（2026-08-23：**MIT** · **A→B→C**，载体 `document-harness/plans/publicization-a.plan.md`）。**批 A = 轮 `PUB-FACADE` CLOSED 2026-08-23**（见指针卷；「余一件用户动作：push 首跑 CI」**已陈旧**——实测 `gh run list` 2026-08-24：用户已于 2026-08-23 起三次 push、三次 CI 全绿，首跑发生于批 A 收批当日 05:21；本句更正随轮 `STRANGER-PROOF` 收批落，依其 plan 变更面所载）。**批 C 增列一件：观众向根 README 重写**（用户 2026-08-23 问「面向观众的 README 在哪批」，对话中拟归批 C——第二调用者实证的实走记录即 quickstart 素材，符合 commands-over-claims；切法批 C 开轮时再裁。现根 README 无假话但仍是 agent/内部视角）。**批 B = 轮 `CONTRACT-V4` CLOSED 2026-08-23**（见指针卷；v4 已签署生效 `HD-56`）。**下一队首＝批 C 陌生人可用性**，清单增至六件：`chk-caller-prefixes` 设计题 · `amend-exempt-caller` · ONBOARDING 第二调用者实证 · 10 解析点收尾 · **观众向根 README 重写**（2026-08-23 对话拟归此批）· **§10.5 两问立案**（分发形态 submodule vs plugin 安装 · `.claude/` 下要不要放 harness 件——用户 2026-08-23 裁「立案挪后」，本行即其家，批 C 开轮时摆给用户裁或另开独立轮）。**批 C 已开且第一轮 CLOSED（2026-08-23）**：开轮四裁（切两轮 `STRANGER-GUARDS`→`STRANGER-PROOF` · `submod-index` 接下 · §10.5 批 C 收批带实证再裁 · 冷读照派）载 plan `stranger-guards.plan.md`；**轮 `STRANGER-GUARDS` CLOSED**（见指针卷——六件中前四件落定：`chk-caller-prefixes` 设计题 + `amend-exempt-caller` + 10 解析点 + `submod-index` 顺带）。**下一队首＝轮 `STRANGER-PROOF`**（第二调用者实证 + 观众向根 README 重写），其收批时裁 §10.5 两问。**轮 `STRANGER-PROOF` ＋ 插入批 `SUBMOD-HOOKENV` 已于 2026-08-24 合并收批 CLOSED**（见指针卷）；批 C 六件全落，**仅余 §10.5 两问**（分发形态 submodule vs plugin · `.claude/` 放不放 harness 件）——收批当日携实走证据摆给用户，答案届时另记。**已裁（2026-08-24，user「维持吧」）：两问皆维持现状——分发形态维持 submodule（实走刚证可用、pin 即版本追溯，plugin/包装等真外部需求出现再议，`E6`）· `.claude/` 不放 harness 件（实走九条零触及，且该区在守卫 VENDORED 豁免盲区，治理件不进盲区）。§10.5 就此关，**批 C 整体 CLOSED**。**仓已于 2026-08-24 翻 public**（用户动作，批 C 收官同日；实测 `visibility=public`）；调用者仓同日 gitlink bump 至 `733cb80` 并按用户裁决收窄其 repo-audit 扫描面（caller commit `931a3fa`，rider `decited-paths` 跨仓兑付毕）。**该队首已由轮 `README-BILINGUAL` 消费**（2026-08-24 落 `2522ce1`，用户 2026-08-25 裁免轮；见指针卷 CLOSED 卷末）。**轮 `RIDER-SETTLEMENT` 已于 2026-08-25 CLOSED**（见指针卷；bank 30→16）。**本仓下一队首＝dispatch-economy 构造批**（原两件 + 本轮增列的九条 design rider，见下条）；**产品 run 首跑不在本仓**，在调用者仓另行开工。**该队首已于 2026-08-25 由批 `CORE-SET` 接过**（用户当日方向 + 当日即令推进，见下第二条）；dispatch-economy 顺延其后。

- **dispatch-economy 构造批候选**（用户 2026-08-24 裁「往后记」，排批 C 之后、无 deadline）：把派发省时纪律做实——① must-fix 结对复读的**窄 subject 出单形态**（`E10` 通道原文本就是 "re-read of the amended text"，而 `dtw dispatch --read` 只有全层形态；命令面改动按 `HD-47` 逐案归用户）② 快 read 并入 executor 无 commit 窗口的重叠纪律找承载。**本批已增列第三件（用户 2026-08-25 裁，轮 `RIDER-SETTLEMENT` 开批裁决 3）：bank 里 13 条 design rider 中的 9 条并入本批一次收**——六条在 checklist 的 `E9`/`E10`/`R9`/`R10` 措辞面（`wl-route` / `hd38-both-ways` / `e9-pair-budget` / `e10-cannot-see` / `read-name-split` / `waiver-live`），三条在 `ORCHESTRATION.md` 义务表面（`charter-qualifiers` / `e1-table` / `e1-reader`），与本批要动的正是同两个表面；余 4 条是机器题（`pin-drift` / `delta-prose` / `argv-cap` / `freeze-audit`）另候用户裁。**`R5` 观察一条**（FULL `8aa9f6e` `O-4`，用户 2026-08-25 裁「先记下」）：bank 现存 16 行中 13 行需开轮才可兑，该比例是否说明 bank 没在做它该做的事，**待本批收完 9 条、bank 降到 7 行时再评**。起因＝轮 `STRANGER-PROOF` 开轮读链约一小时 wall-clock，一个表格单元格的修被按全层复读（1640 行 + 电池重跑）；教训当轮曾写进该轮 plan 的 Dispatch economy 节，但**写于其所辖派发已跑完之后，用户指其无效**——本行才是排期载体。**与批 `CORE-SET` 的交叠（2026-08-25 记）**：本批领的九条 design rider 里有两条
  （`charter-qualifiers` / `e1-table`，`ORCHESTRATION.md` 义务表面）与一条（`waiver-live`，`E10`
  cold-read/`§live` 句）的触碰面，正是 `CORE-SET` 轮 1 item A 要改的两处；哪批兑付按 `CORE-SET`
  plan 的开轮问题 4 归用户裁：已裁**只兑 `waiver-live`**，另两行留 bank 待本批。**第一件（窄 subject
  出单形态）新增第二笔实测成本**：`CORE-SET-LAYER` 开轮读因无窄形态而手工缩范围，把生成器**故意不给**
  的成员名单又贴了回去（`dispatch.py` 注释记着为何不给——手写成员表错过一次）；本次未造成锚定错误
  （派发标了「自己验」、读者独立重推），但按 `O-2` 挂在本件下（read `9f1de08` `O-2`）。

- **批 `CORE-SET` —— 让核心集脱离本仪器自己的建造史**（用户方向 2026-08-25，自此为本仓队首）：
  挂载本仪器的仓只带核心集就能开轮、跑轮、收轮。**十九条用户裁决、四个轮次的量程、验收与全部量测
  在 [`document-harness/plans/core-set.plan.md`](document-harness/plans/core-set.plan.md)**，本行只
  留指针——2026-08-26 一次把复述压回去，因为它撞破了同日新立的每条上限。
  **轮 1 `CORE-SET-LAYER` CLOSED 2026-08-26**（收轮 `83aecd4`；记录 `v3-{cold-read-ff4b749,
  review-full-92cc514,review-verify-0f0498f}.md`；journal `core-set-layer-2026-08-26.md`）：剥史树
  上九成员真断链 **31→13**、`ONBOARDING.md` 另测 **2→0**；`E9` 三腿走满且**修腿花了两次**（用户
  2026-08-26 裁「算，照实写」，VERIFY `V-4`）；bank 16→19。
  **本轮五个在仓成员全部改动，欠独立 read 随下轮开轮**（含免通道 `0420d99` 的字节）；下轮冷读若再走
  窄形态，基线须按 `E10` 取「自**某一份**已记录整读以来未变」，不得只钉一份记录（本轮开轮读的 `O-1`
  即栽在这里）。
  **轮 2 `CORE-SET-SIGNATURE` CLOSED 2026-08-27**（记录 `v3-{cold-read-d3ba221,review-full-a554c0b,
  review-verify-5e5bebf}.md`，三份皆原样落；journal `core-set-signature-2026-08-26.md`）：契约 v4
  的签字迁至根目录 `CONTRACT-V4-SIGNATURE.md`、`HD-56` 转 `superseded`、签字对象仍 `614932de…`
  不重签；轮 1 归本轮的 8 处残留全清，剥史树真断链 **13→5**（余 5 处：3 处裁决 12 明许、2 处为
  `REVIEW.md:93` 一站点、裁决 13 明许悬空、item G 于轮 3 收）；`CORE-SET.md` 并入
  `CONSTRUCTION-INDEX.md`（裁决 22）。开轮两裁落 `HD-61`（`E2` 授权扩至五处引用降名）与裁决 20
  （`README.md:16` 并入范围）；`HD-60`/`HD-61` 消耗后经用户裁转 `retired`（`a554c0b`）。
  **`E9` 三腿走满、修腿只花一次**：FULL `REVIEWED_NO_BLOCKER`（4 low/3 obs）→ 一次用户批准的修
  `5e5bebf`（答 `L-1`，另三条入 bank，bank 19→22）→ VERIFY `REVIEWED_NO_BLOCKER`（2 low/2 obs）。
  **本轮改动的是三个在仓成员，不是两个——契约 v4 是第三个，其字节欠独立 read 随下轮开轮**
  （blob `dfc983d2…`→`5dfb7b64…`，开轮冷读整读的是旧 blob，故无可引之读；VERIFY `V-1`，本行即其
  载体）；`CONSTRUCTION-CHECKLIST.md` 与 `document-harness/README.md` 同欠。**更正一句已提交的
  结论**（`HD-59` 向前更正，原文留在 journal §9）：该节「本轮花的预算是零」写于 `66dfd30` 时为真，
  此后本轮花掉一次 FULL 加一次修腿，VERIFY `V-2` 点名。
  **轮 3 `CORE-SET-CODE` CLOSED、批 `CORE-SET` 整批 CLOSED 2026-08-27**（记录 `v3-{cold-read-b737742,
  review-full-1db5155,review-verify-7a4e47b}.md`）：v1 package 评审腿整条退役、
  `DEFAULT_REVIEW_RECORD_DIRS` 的值改中性。电池 854→**795**（少的 59 条逐条对账）；
  **全批口径：剥史树非解析引用 31→3**，余三条皆裁决 12 明许。FULL `CHANGES_REQUIRED` → 一次修 →
  VERIFY `REVIEWED_NO_BLOCKER`，修腿只花一次；bank 24→27。**本仓自 2026-08-27 起持有
  `.harness/scan-surfaces.json`**（声明旧目录）——gitignore、每个新克隆须重写，直到记录搬家。
  **未结六条逐条见 plan 的 *What this batch leaves open***，皆不卡。**收批 tip `418477a` 上
  orchestrator 亲测复核**：电池 795 passed · 剥史树真断链 3（皆裁决 12 明许）· 成员 9/9 · 三守卫 exit 0。
  **push 债：`origin/main..HEAD` = 58**（本 session 未推；推与不推归用户）。
- **批 `FREEZE-TO-ALARM`（拆冻结）—— 整批 CLOSED 2026-08-28**。plan
  [`document-harness/plans/freeze-to-alarm.plan.md`](document-harness/plans/freeze-to-alarm.plan.md)
  是 2026-08-27 六条裁决 + 四条答问的载体；理由与实测在各 commit 正文与
  `migration/document-work-assurance-v3/` 的三份 record，此处只留指针。
  **结果**：`E2` 由「无裁决不得写」改为**事后在 commit 正文逐条点名完整仓内路径**；CI job
  `announced-path-disclosure` 逐 commit 机械判定并已设为 `main` 的 required status check；
  `main` 转 **PR flow**（`enforce_admins: true`，仓主同受约束，force-push／删分支皆拒）——
  端点回读实测，非据命令回显。`HD-20` retired；`HD-44` superseded、后继 **`HD-62`** 承载收窄全文，
  **全仓再无「`E2` 写前欠裁决」的活要求**。
  **链**：`464b7dc` 冷读 → `580d236` 其 must-fix → `a2d3fb4` B → `184387c` A → `1d4d9aa` C
  → `0355b36` E → `ad0663d` 勘误 → FULL `CHANGES_REQUIRED` `9580ca9` → 唯一修腿
  `013483f`/`1830d47`/`34d63cc`/`629cff5` → VERIFY **`REVIEWED_NO_BLOCKER`** `a8bfe5b` → `57a31c1`。
  电池 795→**813**（新增 18 条为报警的测试）；九条验收全过；报警在 GitHub 实跑两次（后一次判 8 个
  commit）。**本轮 commit 全直推 `main`、保护落在其后——本批装的 PR flow 没管到装它的这一批**，照记。
  **入 bank 未修四件**：`announced-set-anchor`（十六条路径无本仓可解析枚举，判 design；deadline ＝
  pack 首次增减件）· `e10-freeze-exception` · `archive-header-selfcount`（触碰未兑）· 三条 `E2`
  老 rider 改随下一批。
  **另一件小的**：CI 依赖未固定 ＋ 第三方 Action 不受限（`allowed_actions: all`、可变 tag）。
  用户裁「与 `E2` 无关、单独一件小的」。
  **⚠ 落地流程（已实测一次）**：直推 `main` 被拒，走分支 → PR → 报警绿 → 合；**PR #1 已于
  2026-08-28 合入**（`607ec17`，merge 非 squash，`pull_request` 首次求值取范围正确）。**工作分支
  自此为长期 `dev`**（用户 2026-08-28 裁；CI `on: push:` 无分支限定，推即判）——**代价：轮边界与
  PR 边界可能不重合**，评审走 `dtw dispatch --range`、独立于 PR。
  **无 round journal**：本批的理由与实测只活在各 commit 正文与 plan（历批皆有 journal，本批无）——
  **用户 2026-08-28 于 preclear 裁「认了」，不补**。同批路由的 `R5` observation：`O-2` 报警 YAML 接线
  无测试、`O-6` 两处 mutation 未被钉住，二者入 bank 为 rider `alarm-yaml-untested` / `alarm-mutation-gaps`；
  `O-5`（squash 合并可绕过报警）**已修**：`allow_squash_merge` 关闭——端点回读实测
  `squash=False` · `merge=True` · `rebase=True`。留着的两种安全：merge commit 被报警跳过而它带进来的
  原始 commit 逐个受判，rebase 保留每个 commit 自己的说明；只有 squash 会把 N 个压成 `main` 上的一个
  新对象、让报警去判一段它没判过的文字。未裁而按既有路线走的：`O-4`（`HD-57` 主题被 item A 删除，
  但其状态是 `implemented` 非 `live`、不主张现行要求，属陈旧交叉引用）· `V-2`/`V-3` wording-level 按 `R9`
  随下一批 · `V-4`/`V-5` 已发生、留在 VERIFY 记录里。
- **候选隔离机制已丢失 —— 设计题立案（用户 2026-08-27 提出，未裁是否开轮）**：用户批准的 v3 执行计划
  `document-harness/plans/document-work-assurance-harness-v3.plan.md:119` 明写「All payload writing
  occurs on an isolated Git candidate branch/worktree … `REJECT` or `REPLAN` preserves the candidate
  ref but never promotes it」，2026-08-05 journal 称其为**常驻纪律**，且**真被用过**（本档记 run `w1-r1`
  的候选分支）。**今日实测：仓内仅 `main` 一条分支，executor 的 commit 在任何评审看见它之前就已落主线**；
  幸存的只有 `E9` 的评审窗口，而它守的是**记录**不是候选。结构性后果：一个 `CHANGES_REQUIRED` 判定
  **无法**靠「不合入」执行，只能靠事后补一个修的 commit，而那个 commit 又消耗该轮唯一的修腿。
  是否恢复、以何形态恢复，归用户。
- **设计批 `ASSERT-OWNER` —— REVERTED 2026-08-15**（用户裁，依据 `E6`「a rule added about it is not the fix」）：它试图把 `HD-41` 写进指令层，装的过程中自身又出七个同类实例，FULL 返 `CHANGES_REQUIRED`；五个指令层文件已回 `ff05b01`、blob 逐一核对，checklist 回 204 行 / 12 条。诊断钉在 journal [`structure-vs-prose-2026-08-15.md`](document-harness/journal/structure-vs-prose-2026-08-15.md)；过程见 plan [`harness-assertion-owner-design.plan.md`](document-harness/plans/harness-assertion-owner-design.plan.md)。**四件未结已由用户 2026-08-16 一次裁完**：① 该轮 `E9` 预算＝撤回不消耗腿、不欠 VERIFY，该轮就此结账 ② rider `wl-route` 推迟（行不动、redeem-when 照旧，到期未兑的事实留在 FULL 记录里）③ `HD-41` **不再试**指令层承载，永久只住决策簿（用户裁不建条目，锚即本行；`HD-5` 的 §live 必读使其仍可达）④ 决策簿准入口径**维持**——构造批无 choice JSON，其裁决继续只活在 commit 正文，代价照记。

- **契约 v4 —— CLOSED 2026-08-23**（轮 `CONTRACT-V4`，`HD-56`：s1/s2 并入 v4 并经用户通读签署；§13 未改、无 s3；豁免簿契约半退役；两份 s 的 UNSIGNED 残迹随文件退役消失；「签 v4 前整份读一遍」的价钱已付）。原立项文案照录：（用户意向 2026-08-04）：§13 自身已允许（"corrections create
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
