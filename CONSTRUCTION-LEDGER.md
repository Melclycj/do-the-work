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
  （closeout `214f743`）· `V1-CONTEXT-EXACT` · `SIMP-A4` · run `p5b-claims`（153→173 objects，promotion `3074ce4`，closeout `efa56ea`；FULL `v3-review-full-8ad8c2f.md` + VERIFY `v3-review-verify-275da5b.md`）· **批 A（A1+A2，2026-08-10 收批）**——A1 链 `a7bb1d6`→`fd058aa`→`7a08265`；A2 五轮链在 plan 步骤注与 `V3-A2-R*-CLOSEOUT` commits，batch:A 裁决 retired 入 decisions-archive、`HD-18` implemented，收批 commit `V3-A2-CLOSE-v1`** · 设计轮 `BATTERY-REPO-SCOPE`（2026-08-18，仪器仓内第一个构造轮：全档电池六条按**被验证的仓**分档、doc-only 例外句改按子句读、revert anchor 标明其价已是设计轮，`HD-45`；rider `battery-travel`/`tier-file-vs-clause`/`tier-scope` 兑付删行，`layer-crossrepo-token`/`layer-outbound-refs` 新入 bank；read `v3-cold-read-28501fe` 0 must-fix，`E9` 三腿全程未花） · 设计轮 `ORCHESTRATOR-CHARTER`（2026-08-18；orchestrator 的角色说明书立为 `E10` **第十成员**，走收窄形——九条已在层里的义务只点名归属并指向规则 id、三条层内零承载的写正文；`E1` 的「派发即独立」由充分条件改为必要非充分并加中间态披露句，`HD-46`；rider `E1-suff` 兑付删行，`e1-disclose-home` 与 `charter-qualifiers` 新入 bank；三次独立 read 收敛——2 must-fix → 1 → **0**，`E9` 三腿全程未花）· 轮 `CALLER-ONBOARDING`（2026-08-19，第三期：onboarding 九条 + 两模板 + 第七命令 `dtw init` + `layer_path_check` 归位；九条在临时仓实跑、两支守卫各见拦一次放行一次；FULL `CHANGES_REQUIRED`（hook 提交成 100644 · 测试少钉一条头部规矩）→ 一次用户批准的修 → VERIFY `REVIEWED_NO_BLOCKER`，`E9` 三腿走满；`HD-47`/`HD-48`，五条 rider 新入 bank；记录 `v3-{cold-read-c22e229,review-full-2026a14,review-verify-4029b43}.md`）。· 轮 `LEDGER-SPLIT`（2026-08-19，批 DTW-INDEPENDENCE R1：仪器开发史入本仓——本账本 + archive + 16 份构造 plan，17 件逐 blob 对账；调用者账瘦 113→57 行；FULL `CHANGES_REQUIRED`（搬入 plan 内 10 条挂载前缀死链）→ 一次用户批准的修 → VERIFY `REVIEWED_NO_BLOCKER`，`E9` 三腿走满；`HD-49` 取代 `HD-28`、`HD-50` 取代 `HD-48`；记录 `v3-{cold-read-7701f03,review-full-e74be07,review-verify-8f1ad1d}.md`）。· 轮 `XREPO-REFS`（2026-08-20，批 DTW-INDEPENDENCE R2：指令层不再写调用者路径——`E10` 收caller-held-path 条款、四处降名、`E1` 披露句得载体与责任人、`E10` provenance 死从句删除，零守卫代码改动；开轮 read 返 1 must-fix（层内 15 处裸 commit id 无家）→ amendment `48b6c5f` + 复读 `c53fc4e` 结对；FULL `CHANGES_REQUIRED`（新条款把守卫说大了）→ 一次用户批准的修（收口径；守卫认全类改入 R3）→ VERIFY `REVIEWED_NO_BLOCKER`，`E9` 三腿走满；V-1/O-3 字节走自由通道 `34a5ae9`；rider 三删五增二细化；记录 `v3-{cold-read-69fc082,checkpoint-read-48b6c5f,review-full-dd18226,review-verify-2937bcd}.md`，journal `xrepo-refs-2026-08-20.md`）。· 轮 `DE-PREFIX`（2026-08-20，批 DTW-INDEPENDENCE R3：去 `ResearchSystem/` 前缀——313 件上提一层、冻结字节按 `HD-44` 整体移动、2 处 `parents[4]`→`[3]`（重测确认台账原数仍准）；守卫认全类（resolve-nowhere 单一类、escape 不算解析、`.harness/` 运行时豁免）+ rename 感知（候选第一次实弹被自己守卫拦下，pre-submission correction 修成 un-pathspec'd `-M` diff）；`E10-sync` 三镜像同 commit（`HD-22`）；`sweep_refs.py` 入仓；开轮 read 0 must-fix（`L-1` 字节随候选、`L-2` 入条款、`L-3` 入 bank 行 `e9-pair-budget`）；FULL `CHANGES_REQUIRED`（B-1 四处守卫分工描述被证伪 · B-2 解析器 fail-open）→ 一次用户批准的修 → VERIFY `REVIEWED_NO_BLOCKER`，`E9` 三腿走满；VERIFY V-1/V-2 字节走免通道 `f8b4ef3`、V-3 入 bank 行 `e10-cannot-see`；rider 一删（`mount-inert` 由调用者侧 `$H` 重指 + hook 硬失败兑付，落调用者本轮 gitlink-bump commit——跨仓兑付，「同 commit 删行」按仓各自成立）三注（`frozen-path-prefix` 事实重写 4→5 处、`submod-index`/`decited-paths` 记 touch 到达不可兑）两增；候选带 trailers 为 `E8` 违规孤例（修腿正文起永不再有）；**层欠一次独立 read，随下一轮开轮**（tip 十成员 blob id 列在 VERIFY 记录）；记录 `v3-{cold-read-4410899,review-full-39a21a8,review-verify-2538893}.md`，journal `de-prefix-2026-08-20.md`）。· 轮 `INIT-SURFACE`（2026-08-21，批 DTW-INDEPENDENCE R4 收官：`dtw init` 命令面判据入层——README onboarding 行载「树里那半接线可进 `init`、机器那半不进」+ `--into` 不加（`HD-47` 转 implemented）；分工收拢——两路径守卫的分工一处说、其余指过去（home = README *Local enforcement* 行，rider `guard-division-home` 兑付删行）；`sweep_refs.py` 补 9 条测试（FULL `39a21a8` `O-4` 账清，电池 739→748）；开轮 cold read 兑 DE-PREFIX 欠的层 read，1 must-fix（`M-1`：REVIEW.md 给 caller 持有的产品评审记录写了仓库路径 token）由 amendment `bba6f94` + 复读结对清掉、零预算；FULL `CHANGES_REQUIRED`（`B-1`：home 句量词被三处残留证伪——含 candidate 自己写的一处）→ 一次用户批准的修 `84dea06`（含搭车 `L-2`/`O-3`/`O-4`）→ VERIFY `REVIEWED_NO_BLOCKER`，`E9` 三腿走满；VERIFY `L-1` 字节走免通道 `9fe60b9`（修腿自己复制了 `B-1` 的内部矛盾形状，第三方连续第四次在同族句子上翻车后由通读收口）；rider `submod-index` redeem-when 改 round-eligible 形（VERIFY `2538893` `O-4` 尾注兑现）；`HD-50` retire 入档；记录 `v3-{cold-read-17ce3ed,checkpoint-read-bba6f94,review-full-7f6e7f0,review-verify-84dea06}.md`，journal `init-surface-2026-08-21.md`）。· 轮 `PREVIEW-RENDER`（2026-08-21，`E11` 载体裁决「脚本化」半边兑现：`dtw preview` 第八命令（`HD-51`）——从产品 run 冻结 control plane 确定性渲染 START 预览，不经 LLM、可重推导不落盘；`EXECUTION.md` SIMP-C4 接线句 + `REVIEW.md` O-1 字节随候选，两成员的独立 read 随下轮开轮；开轮 cold read 0 must-fix（兑 `9fe60b9` 欠读，十成员全实读）；FULL `CHANGES_REQUIRED`（`B-1` boundary 对象按 list 渲染、八真实 plane 全中丢 14–91 条路径 · `B-2` Context 省略吞嵌套节）→ 一次用户批准的修（全包）`15a53fe` → VERIFY `REVIEWED_NO_BLOCKER`，`E9` 三腿走满；VERIFY `V-1`/`V-2` 字节走免通道 `76ebf4a`（含用户裁删 boundary 计数）、`V-3` 裁不加 catch-all；rider `review-record-loc` 迟兑整行删、`RA` 计数改八命令、`e10-cannot-see` 追注两句量程；电池 763→770；记录 `v3-{cold-read-dd22789,review-full-57d1312,review-verify-15a53fe}.md`，journal `preview-render-2026-08-21.md`）。· 轮 `TEMPLATE-LIB-ROOT`（2026-08-21/22，重扎根第③件的收窄首刀，队首由用户当场裁定：两个 run-v2 模板脚本**对着调用者 run 目录 import 就死**——`check_template_instance.py`（唯一 pre-START gate）与 `make_paragraph_map.py` 把 `repo_root` 一个变量当两件事使（找库 + `git -C` 的指令所在仓），拆仓后这是两个仓，而调用者那棵树只有 run 数据没有库；修法＝照抄那四个 `run_*.py` 早就对的形状，库走 `__file__` 相对、`repo_root` 只留给 git。新测试 `test_run_v2_template_library_path.py` 走**子进程**测缺陷类（六个脚本全测，四个本就对的当回归钉）——老测试进程内 `exec_module` 且 `_harness` 已把 `tooling/` 放进 `sys.path`，替脚本满足了它该自证的 import，故 770 全绿而脚本是死的；电池 770→774。开轮 cold read 0 must-fix（兑 PREVIEW-RENDER 欠的两成员读，十成员全实读）；FULL `CHANGES_REQUIRED`（`B-1`：候选正文同时写「orchestrator 与 executor 同 session」与「四持有一项不占、故结构性独立」，自相矛盾且**回归**两轮前已被 `L-4` 纠正过的形式）→ 一次用户批准的修 `627df95`（errata + journal 落盘贴实测 + 假量词）→ VERIFY `REVIEWED_NO_BLOCKER`，`E9` 三腿走满；收批三裁（`V-1` 扫类未贴：补跑两类**均已关闭无新实例**，用户裁不记不贴 · `V-3`+`O-3` 单 session 角色题入 bank 待裁 · cold read `L-1` 范围题**已裁**＝对所有 run 都算，建 `HD-52`）；rider 两处行号更正、两行新增（`startcard-form`/`one-session-roles`）；**披露一次自身越界**：验证时往调用者仓写了一个 `paragraph-map.json`，已删并核对调用者树复原，`ORCHESTRATION.md` 的事前路由在单 session 轮无处可走即 `O-3` 的题；记录 `v3-{cold-read-39e395e,review-full-83e3191,review-verify-627df95}.md`，journal `template-lib-root-2026-08-21.md`）。· 轮 `EXECUTOR-CHARTER`（2026-08-22，队首由用户裁定插于重扎根之前：执行者第一次有机器生成的 charter——`dtw dispatch` 加第四个 dispatch family 两模式（`HD-53`）：`--executor` 产品侧交三事实（run id · 冻结指令 path+revision · charter=`EXECUTION.md`）带四类拒绝（目录出仓 / 无指令 / 未冻结 / worktree 漂移按 blob-id 等值判），`--construction-executor` 构造侧单句指 `CONSTRUCTION-CHECKLIST.md` 零推导；两模式均不写 freeze marker（executor 派发不开评审窗口）；`EXECUTION.md` 删「运行纪律走 Context 引用」写作规则并命名部分 supersession（p4-bridge f1 的 2026-08-01 路由裁决——留强半边：Context 只装背景、出现要求即缺陷；换掉半边：引用之职由 dispatch 承担），`dtw preview` 的 Context 省略就此由「诚实」转「正确」；`HD-52` 载体同批落（START 卡句移出编号态范围成独立段）转 implemented；采样义务定读数时刻（`HD-54`）安家 `EXECUTION.md` Authoring gate；`ORCHESTRATION.md` 被证伪段重写；rider `startcard-form`/`charter-prose-overreach` 兑付删行、义务表刻意不碰（`e1-table`/`charter-qualifiers` 不开）、`mark-case` 明确不兑；电池 774→790。开轮 cold read 0 must-fix + 1 low（十成员全实读、可全引而未引）；FULL `REVIEWED_NO_BLOCKER`（0 blocker 5 low，九 mutation 九红）→ 收批三角六件一次修 `3dd226b`（用户批全包：L-5 counterpart 幻指 · L-2 恢复对冲句 · L-3+L-1 采样段主体句+四改五 · L-4 修 ONBOARDING 簿留史 · 冷读 L-1 判据读法五路径落地）→ VERIFY `REVIEWED_NO_BLOCKER`（2 low 3 obs，接受项逐条重跑、五 mutation 带绿色负对照），`E9` 三腿走满（FULL 返无 blocker 后经 `R10` 晚激活修腿，仍计本轮唯一修）；VERIFY 两 low 入 bank（`plan-delivery` 带 deadline、`fixleg-scan-paste` 记四连趋势）+ FULL `O-1` 入 bank（`exec-mount-test`）；成员编辑欠独立 read 随下轮开轮，咬合时刻=第一份按新规则起草的产品 run 指令；`ORCHESTRATOR-CHARTER` 未答问题①就此关闭；记录 `v3-{cold-read-693b692,review-full-229f03f,review-verify-3dd226b}.md`，journal `executor-charter-2026-08-22.md`）。· 轮 `PRERUN-RIDERS`（2026-08-22/23，产品首跑前清账批，用户批插队于重扎根第③件前、收批即消费、队首回该项；**首个 `HD-55` 独立角色形态轮**——冷读/executor/FULL/修腿/VERIFY 五次派发全部独立 session（`dtw dispatch` 出单），orchestrator 全程零手改，候选 `E1` 披露首次以四持有零占声明 structural）：七裁决落层——plan 送达 + 指令优先 bound（`ORCHESTRATION.md` Handing + `EXECUTION.md` 写作规则；理由=调用者开发自己规则的落脚点）· 薄检查=控制面 finding（`REVIEW.md` 两节对齐 review_only 镜像）· 观察路由成文化（record observations → closeout 按 policy 归口）· status-key 二次维持 + `dtw flow` 递单前纪律 · mark-case **当日翻案**改判维持词表（executor-charter.plan 实测 0/1/0 为据）· ctx-ground 二次维持 · `HD-55` 落层三站点（家=三角色表，冷读 `O-1` 补第三站）同 commit 翻 implemented；riders 五删（plan-delivery/chk-thin/HI-route/mark-case/fixleg-scan-paste——末条由修腿贴扫类自兑）二改写（status-key/ctx-ground）二新增（io-hiroute-stale 超范围披露、用户裁保留；hi-schema-gloss=VERIFY `V-1`）；开轮 cold read 0 must-fix（兑 EXECUTOR-CHARTER 欠读）；FULL `REVIEWED_NO_BLOCKER`（5 low 4 obs）→ 全包修 `860729f`（勘误 journal 逐数重测、四类扫贴正文并扫出英文 pattern 漏中文形的第二重、`io-design` 引文精确化）→ VERIFY `REVIEWED_NO_BLOCKER`（1 low 2 obs），`E9` 三腿走满；纯文本轮零代码零 schema，电池 790 三测同数；两成员编辑欠独立 read 随下轮开轮；记录 `v3-{cold-read-3a6a10b,review-full-7cb7213,review-verify-860729f}.md`，journal `prerun-riders-2026-08-22.md`）。· 轮 `PUB-FACADE`（2026-08-23，公开化批 A 门面件；队首两问当场裁——**MIT** · **顺序 A→B→C**——随第三裁**轻量轮形**落 plan `publicization-a.plan.md`：用户豁免开轮冷读（rider `waiver-live` deadline 到达、未咬——豁免前 `§live` 已整读，touch note 落行；PRERUN-RIDERS 欠的两成员 read 续欠、随下一轮开轮）· 工作侧两角色单 session 合并（`E1` 例外通道，四持有全 held 披露于候选正文）· 独立 FULL 保留：LICENSE(MIT) + 双平台 CI（ubuntu+windows × py3.12/3.13；ubuntu 腿=本仓**首次 POSIX 验证**，定出 jsonschema>=4.18 下限——系统 4.10.3 下 571 failed 单根因）+ 根 README 除锈（`readme-cli-stale` 四句全清兑付删行）+ ONBOARDING 第 9 条按实测改写（`posix-mode-wording` 兑付删行：644 hook=带 hint 跳过、hint 可抑制）+ 计划外抓修两件——`.githooks/pre-commit` 裸 python 使 POSIX 接线后**有钩必死**（python3→python 带 `-c pass` 探测循环，防 Store 假别名）、`test_candidate_checks.py:523` 唯一被执行的裸 python fixture（sys.executable）——+ 新增 `test_precommit_hook.py` 以 subprocess 钉 wrapper 缺陷类；电池 790→793 双平台绿。FULL `CHANGES_REQUIRED`（B-1 本轮自己的缺陷类只扫 tooling、漏了正在改的文档且 README 新写两处裸 python · B-2 新测试三行为只钉一半、exit-0 空壳存活）→ 一次用户批准的修 `71e1f24`（两文件各一句解释器约定句赎清七站点 + blocking 测试杀 mutation 2/4 + docstring 收窄 + GBK errors=replace 第三坑顺手修）→ VERIFY `REVIEWED_NO_BLOCKER`（7 mutation sha256 还原、双平台 793 独立复现），`E9` 三腿走满；VERIFY `V-1`/`O-3` 字节走免通道 `a3ef5ee`；`V-2` 入 bank 行 `fixleg-scan-raw`、`O-1` 入 bank 行 `py-convention`（类残存 `EXECUTION.md:364` 成员内 + run-v2 README 四处）、`O-2` 注入 `E10-sync` 行（第四份机器侧成员路径拷贝）；测量通道两次翻车（wsl.exe 回传 $? 不可信 · 反引号被中间 shell 当命令替换吃掉致正对照一度测了空气）当场识破、有效实验重做，记 journal；**CI 落仓未跑（零 push）——首跑等用户 push**；记录 `v3-{review-full-28dd80b,review-verify-71e1f24}.md`，journal `pub-facade-2026-08-23.md`）。· 轮 `CONTRACT-V4`（2026-08-23，公开化批 B 重签打包批；plan 四裁：冷读+FULL+VERIFY 全独立、v4 捆绑 `wspec-owner` 契约站点、卡片裁授权触 `E2` 面、§10.5 两问立案挪后：**契约 v4 单文件成立并已签署（`HD-56`，blob `614932de…`，用户通读后签）**——合并 v3+s1+s2（考古更正：两份补丁实已签过字，UNSIGNED 是签前残迹）、四句替换+两节版本边界落 13.1/13.2、五断链按三类修、frontmatter 清态、§3 归属行改 executor；三源文件退役入历史（用户确认）、`E2` 冻结面十六件、`E10` 成员 10→8→**9**（v4 入层=用户裁，`HD-56` ②落簿；`E10-sync` 三站同 commit 轮内走两次、散文腿全扫）；豁免簿契约条退役（removing decision=`HD-56` ③）；split-design/io-design 除锈随签重签（`HD-40`/`HD-35` 第三签，四 rider 由此兑付）。开轮冷读 `b8df15a` 0 must-fix（偿两轮欠的成员 read；其 L-1 入 bank 行 `read-name-split`）；FULL `CHANGES_REQUIRED`（B-1 四站点「未签先称签」——D1 刚清的缺陷类在周边文本重现；合并本身逐字节核净、plan 声明 verbatim 处 ratio 1.0000）→ 一次用户批准的修 `d0f185c`（四裁折入：修+O-5 三句补回+v3 退役确认+v4 入层；L-1..L-5 搭车，`fixleg-scan-raw` 以贴原始输出自兑删行）→ VERIFY `REVIEWED_NO_BLOCKER`（V-1 第五站点 operative 走免通道删 `f112135`；L-4 判 transcription 维持；E2 字面量无机器绑定实测在案），`E9` 三腿走满；riders 四删一改写一自兑一增 + `PD` 触注；`HD-20` 枚举随 `HD-56` 同批更新（`HD-44` 的同批更新为签字 commit 声称而 diff 未含——`v3-cold-read-cf54a79.md` `L-3`；2026-08-23 依用户「落」裁决补落）；记录 `v3-{cold-read-b8df15a,review-full-5f849da,review-verify-d0f185c}.md`，journal `contract-v4-2026-08-23.md`；**本轮成员编辑（含免通道 `f112135`）欠独立 read 随下一轮开轮，且下轮冷读并新收 v4 这个 339 行成员、无先前 read 可引**——VERIFY 已注此成本）。· 轮 `STRANGER-GUARDS`（2026-08-23，批 C 陌生人可用性第一轮；开轮四裁 + fix-gate 五裁全在 plan `stranger-guards.plan.md`；`HD-55` 常规形态——冷读/施工/FULL/修腿/VERIFY 五次派发全独立 session，orchestrator 零手改工作产物）：守卫扫描面调用者化——新 `caller.py` 声明加载（`.harness/scan-surfaces.json`，`dtw init` 写默认绝不覆盖、malformed 响亮拒绝不静默回退）+ 两支守卫同读一份声明，首调用者 `ResearchSystem/…` 条目以声明形态存活（测试逐字节钉住）；`TrackedPaths` 认 submodule 内部路径（`submod-index` 裁「认」并兑付删行）；12 解析点全改「git 发现或响亮拒绝」（`review_freeze_check.py` 超 plan 表半步，类扫描证成、代价披露于候选正文）；层修正段对第二调用者不再读反（`amend-exempt-caller` 兑付）；README terminus 经用户否 request-access 提案（「不写，thesis 就是 private」）后回单机历史形态 + 一句 private 说明；候选 `c2e955b` 27 文件、三 rider 同 commit 兑付、`decited-paths` 触注（跨仓兑付待调用者侧）。开轮冷读 `cf54a79` 0 must-fix 3 low 5 obs——一次清偿三笔欠读（本轮开轮读 + v4 首读 339 行 + CONTRACT-V4 成员编辑欠读）；L-1/L-2 入 bank 行 `v4-verifmode`/`v4-plan-digest`，L-3（签字 commit 声称改 `HD-44` 而 diff 未含）归口用户。FULL `REVIEWED_NO_BLOCKER`（2 low 4 obs；电池 838/792 独立重导、8 组自写 mutation、守卫负对照非空转）→ `R10` 晚激活修腿（用户批：Low-1 尾斜杠归一 + README「不写」）`54f7fa7` → VERIFY `REVIEWED_NO_BLOCKER`（2 obs），`E9` 三腿走满；registers `53ec1a6`（`HD-44` 十八→十六带日期注 + ledger public-仓句证伪更正 + `HD-57` 立条——`E2` 五处陈旧字面一次裁「可以改」，应用批排收批后）；Low-2 教训入档＝出单 base 取上一已评审 tip、riders-only commit 落候选之后（本轮 VERIFY 已照此跑）；电池 792→844；成员编辑（checklist 修正段 + 应用批将触的 v4/`E2` 字面量）欠独立 read 随下轮开轮；记录 `v3-{cold-read-cf54a79,review-full-c2e955b,review-verify-53ec1a6}.md`，journal `stranger-guards-2026-08-23.md`。· 轮 `STRANGER-PROOF` ＋ 批 `SUBMOD-HOOKENV`（2026-08-24 合并收批，用户裁一次共享 FULL 罩两单元；全程 `claude -p` 独立 session 派发——`E1` 修正 `1a0a200` 后第一批，该修正由用户裁免轮当日落、其在 `ORCHESTRATION.md:24` 的镜像句由开轮冷读抓出走 must-fix 结对清掉 `153302a`）：第二调用者实证真发生——异布局新仓九条照文档实走（`stranger-proof-walk-2026-08-24.md`），抓出文档三缺陷（依赖步骤缺失 / 双解释器假话 / 决策簿挪位重建空簿，候选内修）+ 重缺陷：守卫 submodule 识别在 pre-commit hook（唯一真实运行环境）失效、`commit -a` 下四探针全反——根因＝git 泄漏给 hook 的定位 env vars 未清，修＝查询前清掉且名单向 `git rev-parse --local-env-vars` 现问，7 条真 `git commit` subprocess 测试 5 红→7 绿；观众向根 README 重写、quickstart 全命令实走背书；候选曾被 orchestrator 记账 commit `0133d1b` 连锅吞（共享 git index，声称 ledger-only 实载 587 行）——用户裁 append-only，披露 `e620b43`、归属勘误落 journal，**教训＝executor 运行期间 orchestrator 零 commit**；首次共享 FULL 派发被用户叫停（按 `E9` 判据未发生、零消耗）后重派返 `CHANGES_REQUIRED`（B-1 quickstart 缺 tracked-hook 步骤、读者会拿到永不运行的 hook 还以为在跑 · B-2 mutation 签名两条身份错）→ 一次用户批全包修 `3149581`（补步并从已发布 remote 逐字重走、关掉 local-clone 天花板 + errata 贴逐测实测撤回假句 + 三 low）→ VERIFY `REVIEWED_NO_BLOCKER`（hook 字节旁证逐字节同、四 mutation 逐格复现），`E9` 三腿走满；电池 792→851；riders：`submod-hookenv` 兑付删行，`discover-root-env` / `move-cost-member-site` / `onboard-clone-decl` / `onboard-cmd-count` / `e1-reader` 新入 bank，`decited-paths` 前提解锁；memory 禁用与「都不立」处置、取消派发披露均落 journal `stranger-proof-2026-08-24.md`；记录 `v3-{cold-read-21dad76,checkpoint-read-153302a,review-full-3d5c705,review-verify-3149581}.md`。journal 在 `document-harness/journal/<轮名>-<日期>.md`。
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
  见 stranger-guards.plan.md fix-gate 节 ruling 4）**；新仓 = private
  `Melclycj/do-the-work`，`HD-40` ① 关闭）·
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
  (a)+观察条款——记录义务与读数时刻自 2026-08-22 住 `EXECUTION.md` Authoring gate 段（`HD-54`；
  读数=下一产品 run 的 closeout），本行只留改判三分支**（层内句为此指回本行）：分歧恒零或恒
  paragraph 侧对 → 议 (c) 段落诞生义务，恒 unit 侧对 → 议 classification 列去留，两侧各有贡献 →
  转常设 ·
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

- **拆分批 —— harness 搬成独立仓**（`HD-18`）：**整批 CLOSED 2026-08-17**，五轮——R0 设计 · R1 搬 254 件 + 执行 `HD-39` 的删除 · R2 摘 CLI 成 `dtw` · R3 调用者侧接线 · R4 记账收批。**结果**：新仓 = private `Melclycj/do-the-work`，产品仓以 gitlink 钉住 `ResearchSystem/harness`；pre-commit 改 tracked 且三支守卫从 submodule 跑；记账断言定终局（调用者 `HARNESS-POLICY.md` §4）；八条 rider 逐条有归宿；`HD-33` / `HD-28` / `HD-15` / `HD-10` 转 implemented。**「重扎根轮」原定三件，2026-08-18 拆开做**——第一件 CLOSED（轮名 `SPLIT-COPY-RETIRE`：调用者副本 273 件删除 + 入链重写；FULL `CHANGES_REQUIRED` → 修 → VERIFY `REVIEWED_NO_BLOCKER`，`E9` 三腿走满；记录 `v3-review-{full-2d148f3,verify-bef77f3}.md`，两份都留在调用者仓——那一轮的 subject 是调用者的树）。**余下两件仍未排期，且「重扎根轮」这个名字自此不再指任何单一轮次**：② 去 `ResearchSystem/` 前缀与 `REPO_ROOT` 深度（实测只 2 处 `parents[4]` 会断）+ `E10-sync` 三处同改（须同一 commit）③ 步骤 19 的十一个 `--repo-root` 解析点。**三条 rider 的 deadline 原文指向「重扎根轮」，按此重指**：`mount-inert` 与 `PD` → 第 ② 件（`$H` 与冻结面都在那一刻动）· `submod-index` → **deadline 已于第一件到达且未付**，改指下一个碰 `paths.py` / `candidate_path_check` 的批。`nonrec-clone` 已兑付（第一件删副本 + `repo-audit` 认挂载点）；`battery-travel` 已于 2026-08-18 轮 `BATTERY-REPO-SCOPE` 兑付删行（其 deadline 即「第一个于 harness 仓内开的构造轮」，那一轮就是）。五轮叙事在各轮 commit 正文与 `ResearchSystem/migration/document-work-assurance-v3/` 的评审记录里，不在账本重写。plan [`harness-repo-split.plan.md`](document-harness/plans/harness-repo-split.plan.md)。**三期至此全部 CLOSED（2026-08-19，第三期见下方 onboarding 项）。批 DTW-INDEPENDENCE（`HD-50`→retired 入档）四轮全 CLOSED（2026-08-19/21；R4 = 轮 `INIT-SURFACE`，判据入层 + 分工收拢）。构造轮 `PREVIEW-RENDER` 已于 2026-08-21 CLOSED（见当前指针 CLOSED 卷）**。**第 ③ 件的数已按现场重测更正：不是十一个而是 **12 个解析点 / 7 个文件**（`cli.py` 6 个 `args.repo_root else` @ `:43 :80 :147 :329 :414 :462` + 5 个 parser site，`init` 与 `preview` 两个新命令使原数作废；run-v2 六脚本各 1 个 `parents[3]`）。其中**会当场咬人的 2 个已由轮 `TEMPLATE-LIB-ROOT` 修掉**（2026-08-21/22 CLOSED），**余 10 个**（`cli.py` 六 + 六脚本的 `parents[3]` 默认，后者只在不传根时才走到，而今天所有调用都传）。**轮 `EXECUTOR-CHARTER` 已于 2026-08-22 CLOSED**（见当前指针 CLOSED 卷；其 plan——[`executor-charter.plan.md`](document-harness/plans/executor-charter.plan.md)——载的四条用户裁决与一个未答问题均已消费，问题的答案即 `HD-54` 的读数时刻裁决）。**下一队首＝公开化三批（用户 2026-08-23 改队，见下条）**；重扎根第③件余下的 10 个解析点退居其后、拟并入公开化批 C（实测今天不咬人：`cli.py` 六个不传即取 cwd、六脚本的 `parents[3]` 对调用者布局解析正确）；契约 v4 并入公开化批 B。**第③件的 10 个解析点已由轮 `STRANGER-GUARDS` 清零（2026-08-23，批 C 第一轮）——十二处全数改「git 发现或响亮拒绝」，步骤 19 一脉就此全部关闭。**
- **公开化三批 —— 让本仓成为适合公开的 git repo**（用户方向 2026-08-23；同日并裁：产品 run 首跑**不归本仓**，在调用者仓另行开工）：**批 A 门面件**（LICENSE + 双平台 CI——ubuntu 腿即本仓首次 POSIX 验证、顺势兑 rider `posix-mode-wording`；根 README 除锈兑 `readme-cli-stale`）· **批 B 重签打包批**（契约 v4 + 已签件除锈——`six-signed`/`design-route`/`io-hiroute-stale` 等的那个「打包批」）· **批 C 陌生人可用性**（`chk-caller-prefixes` 设计题 + `amend-exempt-caller` + ONBOARDING 第二调用者实证 + 10 解析点并入）。两裁已收（2026-08-23：**MIT** · **A→B→C**，载体 `document-harness/plans/publicization-a.plan.md`）。**批 A = 轮 `PUB-FACADE` CLOSED 2026-08-23**（见指针卷；「余一件用户动作：push 首跑 CI」**已陈旧**——实测 `gh run list` 2026-08-24：用户已于 2026-08-23 起三次 push、三次 CI 全绿，首跑发生于批 A 收批当日 05:21；本句更正随轮 `STRANGER-PROOF` 收批落，依其 plan 变更面所载）。**批 C 增列一件：观众向根 README 重写**（用户 2026-08-23 问「面向观众的 README 在哪批」，对话中拟归批 C——第二调用者实证的实走记录即 quickstart 素材，符合 commands-over-claims；切法批 C 开轮时再裁。现根 README 无假话但仍是 agent/内部视角）。**批 B = 轮 `CONTRACT-V4` CLOSED 2026-08-23**（见指针卷；v4 已签署生效 `HD-56`）。**下一队首＝批 C 陌生人可用性**，清单增至六件：`chk-caller-prefixes` 设计题 · `amend-exempt-caller` · ONBOARDING 第二调用者实证 · 10 解析点收尾 · **观众向根 README 重写**（2026-08-23 对话拟归此批）· **§10.5 两问立案**（分发形态 submodule vs plugin 安装 · `.claude/` 下要不要放 harness 件——用户 2026-08-23 裁「立案挪后」，本行即其家，批 C 开轮时摆给用户裁或另开独立轮）。**批 C 已开且第一轮 CLOSED（2026-08-23）**：开轮四裁（切两轮 `STRANGER-GUARDS`→`STRANGER-PROOF` · `submod-index` 接下 · §10.5 批 C 收批带实证再裁 · 冷读照派）载 plan `stranger-guards.plan.md`；**轮 `STRANGER-GUARDS` CLOSED**（见指针卷——六件中前四件落定：`chk-caller-prefixes` 设计题 + `amend-exempt-caller` + 10 解析点 + `submod-index` 顺带）。**下一队首＝轮 `STRANGER-PROOF`**（第二调用者实证 + 观众向根 README 重写），其收批时裁 §10.5 两问。**轮 `STRANGER-PROOF` ＋ 插入批 `SUBMOD-HOOKENV` 已于 2026-08-24 合并收批 CLOSED**（见指针卷）；批 C 六件全落，**仅余 §10.5 两问**（分发形态 submodule vs plugin · `.claude/` 放不放 harness 件）——收批当日携实走证据摆给用户，答案届时另记。

- **dispatch-economy 构造批候选**（用户 2026-08-24 裁「往后记」，排批 C 之后、无 deadline）：把派发省时纪律做实——① must-fix 结对复读的**窄 subject 出单形态**（`E10` 通道原文本就是 "re-read of the amended text"，而 `dtw dispatch --read` 只有全层形态；命令面改动按 `HD-47` 逐案归用户）② 快 read 并入 executor 无 commit 窗口的重叠纪律找承载。起因＝轮 `STRANGER-PROOF` 开轮读链约一小时 wall-clock，一个表格单元格的修被按全层复读（1640 行 + 电池重跑）；教训当轮曾写进该轮 plan 的 Dispatch economy 节，但**写于其所辖派发已跑完之后，用户指其无效**——本行才是排期载体。

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
