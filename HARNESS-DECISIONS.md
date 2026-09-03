# HARNESS DECISIONS — 裁决登记簿（v3 harness track）

> **这是什么。** harness 的用户裁决的**最高 source of truth**。instruction 层反向 base on 这里的
> 裁决展开细则；细则与裁决冲突，细则错。每条 entry 只装**裁决本身**（一句）+ 元数据；理由进
> journal（经 `basis` 指针可达），待办进 rider/backlog，轮内决定归该 run 的
> `user-decision-*.json`（digest 绑定，比本文件强，不重复登记）。
> **谁读**：每轮 cold read **必读 §live**（且仅 §live）；写 plan / 开设计批时读全部 live 并
> **原样继承**进 plan，不转录改写；执行中撞上计划外的事，按需 grep 本文件与 archive。
> **义务挂在开轮、不挂在 cold read**：指令层的 cold read 被豁免时 §live 照读——豁免的是那一层的
> 成员，本文件不是成员，被豁免的开轮仍读 §live。
> **准入三问**（任一为是即进）：绑下一轮及以后？/ 推翻或收窄已有裁决？/ 用户裁决且除对话与
> commit 正文外无别的家？**颗粒度：一条 = 一件能被独立推翻的事。**
> **状态机**：`live`（在 force 且必读——已裁未落实，或无处承载）→ `implemented`（在 force，
> 细则已由 instruction/代码/模板承载，不必读、grep 可达）→ `superseded`（有后继，双向指针）/
> `retired`（无后继：做完、主题消失、或消耗完毕）。终态不可逆，复活=开新条引用旧 id。
> **部分收窄（2026-08-12 裁，`HD-30`）**：不设第五态——后继条目承载收窄后的**全文**，
> 原条目整条转 `superseded`（双向指针、同 commit 入 archive）。
> 不变量：同一主题至多一条 live · supersession 与 live→implemented 的挪节都在**同一 commit** ·
> 只有用户能翻状态，session 只能提议（`E1`/`R5`）。
> **scope**：`standing`（只能被 supersede）· `mechanism:<path>`（随机制消亡 retire）·
> `batch:<id>`（限构造轮/设计批的排期与成批裁决，执行完 retire；产品 run 用自己的控制面）·
> `one-shot`（消耗即 retire，消耗前仍可 supersede）。
> **删除（纯纪律，无 lint）**：死条目进 [archive](HARNESS-DECISIONS-archive.md)；archive
> **超过 100 行时询问用户一次**要不要清；删除需**双条件合取**——今后不会再被援引 **且** 能从
> record（commit / plan / 评审记录）反推——且默认不删；`superseded` 链**永不可删**。
> **边界**：本文件自 2026-08-08 起记，此前裁决留在原处（ledger / journal / commit），不迁、
> 不建条目（用户裁：旧格式对不上，别浪费）。条目格式的完整性靠纪律，不设机器。
> 设计推演与实证：[journal/decision-log-2026-08-08.md](document-harness/journal/decision-log-2026-08-08.md)。

## §live —— 必读（在 force，且没有别的东西替它说话）
### HD-69 · 修正派发不再另起冷 executor：executor 停在决策点、裁决回来**同会话续跑**（落地归批 `dispatch-economy`）
- 2026-08-30 · user · scope: standing · status: **live**（层内零承载：`ORCHESTRATION.md` 三角色表只说
  executor 是「a full session」，《The executor's report back》只说上报、不说报完之后谁接着做；
  `E1` / `HD-55` 只要求 executor 与 orchestrator 是不同会话。轮 `CORE-ONLY-LAYER` 的实测形态——一个
  主 executor（82 分钟）后跟**四个冷修正 executor**（19 / 18 / 11 / 17 分钟，plan 步骤 5b–5e），
  每个只为套一条新裁决——就是本条要改掉的东西）
- 裁决：**从 START 到 FULL 之间，一轮只有一个 executor 会话。** executor 撞到它不能裁的事时**停在
  决策点**（报给 orchestrator，orchestrator 送用户），裁决回来后**同一会话续跑**
  （`claude -p --resume <session-id>` 一类的续接），而不是另派一个冷 executor 去套裁决。冷启动只属于
  一轮的第一次派发；修正派发是续跑。
- 后果：`HD-55` / `E1` 的分离**不变**——executor 仍是与 orchestrator 不同的独立会话，续跑不改变 `R1`
  四持有的归属（仍由 orchestrator 派发、提示、划界、转报）；变的只是会话的寿命，从「报完即死」改为
  「停下等裁决」。reviewer 与 reader **不受本条影响**，它们每次都冷（`R1` 的独立性靠的就是这个）。
  多 executor 的编排责任本来就在 orchestrator（运输），干活与分解本来就在 executor；本条消除的是
  **会话形态把一个 executor 的工作切成 N 段**这件事，不是把责任挪来挪去。
- 边界：**落地归批 `dispatch-economy`**（用户原话「落到 scope economy 一起做」，读作账本 backlog 里
  排在队首之后、无 deadline 的 `dispatch-economy` 构造批候选，作其第四件），**不在轮 `CORE-ONLY-CODE`
  内改形态**——本轮若再出修正派发，仍按 plan 裁决 33 的冷形态走，closeout 记为本条生效前的最后实例。
  载体由该批的设计轮定：`ORCHESTRATION.md`《The executor's report back》要不要加一句、`dtw dispatch
  --construction-executor` 要不要记 session id 以便续接（命令面改动按 `HD-47` 逐案归用户）。
- basis: 用户裁决 2026-08-30（对话：「不能是冷 executor 啊，我的原本意思是 executor 停在决策点，等
  裁决回来就继续，也就是同会话续跑。这个落到 scope economy 一起做吧」）· 实证＝轮 `CORE-ONLY-LAYER`
  plan `document-harness/plans/core-only.plan.md` 步骤 4–5e（1 主 + 4 冷修正 executor）·
  `ORCHESTRATION.md`《The executor's report back》· `HD-55` · 账本 `dispatch-economy` backlog 条
- **向前更正（轮 `CORE-ONLY-CODE` 修腿，2026-08-30；按 `HD-59`，被更正的六处原句一字未动）：本条
  边界段末句与另五处已提交的结论把构造轮的派发写成 `dtw dispatch` 的某个模式，这自 `7bcdace`
  起为假。** 正确的写法就是 `1a24140` 自己的正文已经在用的那个——**构造侧派发**：构造轮 executor
  的派发是构造侧派发的 executor 模式 `tooling/construction_dispatch.py --construction-executor`，
  而 `--range`（轮评审）与 `--read`（`E10` 层读）同样是那个脚本的；`dtw dispatch` 自 `7bcdace` 起
  只剩 `--subject` 与 `--executor` 两个产品侧模式（两条 `--help` 的实测输出贴在本修腿 commit 正文）。
  **被本段更正的六处**：① 本条边界段末句的「`dtw dispatch --construction-executor` 要不要记 session
  id 以便续接」读作「构造侧派发要不要记 session id」——问题本身、归批与命令面按 `HD-47` 逐案归
  用户，均不变；② `HD-55` 裁决段的「跑 `dtw dispatch --executor`（产品侧）/ `--construction-executor`
  （构造侧）」，构造侧那半读作构造侧派发的 executor 模式；③ `HD-53` 的标题「`dtw dispatch` 收两个
  执行者模式」——今天它收一个（产品侧 `--executor`），构造侧那个住在构造侧派发里，而该条 2026-08-22
  裁决的实质（两侧各有执行者模式、各指自己的 charter）不变；④ rider `e1-reader` 的「`dtw dispatch
  --read` 的第三个派发家族」，该模式是构造侧派发的；⑤ `CONSTRUCTION-LEDGER.md:190` 的「`dtw dispatch
  --read` 只有全层形态」与 ⑥ 同文件 `:254` 的「评审走 `dtw dispatch --range`」——同上。**账本那两行按
  plan 裁决 38 一字不动**（`:190` 那条自陈站在其上界之上、不得再长），本段即它们的更正所在。
  **本段只更正措辞**：不翻任何条目的状态、不改归批、不动裁决实质——`HD-69` 仍 `live` 且落地仍归批
  `dispatch-economy`，`HD-53` 仍 `implemented`。依据＝FULL `v3-review-full-70c82b4.md` `B-2` ·
  plan `document-harness/plans/core-only.plan.md` 裁决 38

### HD-66 · 分发形态：submodule 是默认**而非终局**——core 分发若最终做不到，就上 plugin（推翻 2026-08-24 裁决的该半边）
- 2026-08-29 · user · scope: standing · status: **live**（层内零承载：指令层没有任何一处讲分发形态，
  `CONSTRUCTION-INDEX.md` 只分「travel / 不 travel」而不说怎么送达；原裁只活在
  `CONSTRUCTION-LEDGER.md` 公开化三批那一条的一句话里）
- 裁决：**用户 2026-08-29 推翻 2026-08-24「分发形态维持 submodule」那一半。** 新的形态是条件式的——
  **submodule 仍是当前默认，但若最终证明它无法满足 core 分发，就走 plugin。** 原裁把再议条件写成
  「plugin/包装等**真外部需求出现**再议」（`E6`），本条把那个条件**换掉**：触发器不再是外部需求，
  而是**core 分发被证明做不到**。原裁的另一半（`.claude/` 不放 harness 件）**不受影响、继续有效**。
- **本条不裁「是否已经做不到」，那是后话，且不由 session 判。** 今日实测只作判断材料，不构成判定
  （orchestrator 2026-08-29 用 `tooling/sweep_refs.py` 跑的）：产品层 **58 件**的树上，`E10` 九成员有
  **10 条真断链**——4 个 markdown 链接指向 `CONSTRUCTION-CHECKLIST.md`、2 个 path token 指向
  `tooling/tests/` 与 `.githooks/`、**3 个成员文件本身缺席**。作为对照，全仓 409 件上真断链为
  **0**（14 条全是 NAMETOK，扫描器自陈那是调用者持有物的合规写法），剥史树 120 件上为 **3**
  （批 `CORE-SET` 的成果，余 3 条裁决 12 明许）。
- **结构性的那一条，值得单独看见**：`CONSTRUCTION-CHECKLIST.md` 与两个 retired contract stub **本身
  就是 `E10` 的九成员**，而按 `CONSTRUCTION-INDEX.md` 它们**是构造侧、不 travel**。九分之三不 travel，
  所以「只带 core」在**定义上**就与 `E10` 的成员集冲突——这不是漏了几个链接，是两张清单互不相容。
  已 banked 为 rider `checklist-cited-not-carried`，其抬头写着「每一条出路都是 design」。
- 边界：**「最终」是有内容的，不是修辞。** 至少三条路没走过，走完才谈得上做不到：① sparse-checkout
  （gitlink 照钉整棵树、工作区只 materialize 那 58 个路径；代价是那些引用在工作区变断链而**无守卫可见**）
  ② 开设计轮解 `checklist-cited-not-carried`（把产品层要用的规则搬进产品层，或让 checklist 也 travel）
  ③ core-only 发布产物。本条**不预设**哪条会成，也不授权任何一条免开轮。
- 后果：`.claude/` 那一半维持；`E6`（不为假想需求造机器）在本条下仍成立——本条没有现在就造 plugin，
  只是把它从「等外部需求」改成「等一个可判定的失败」。
- basis: 用户裁决 2026-08-29（对话：「我要推翻之前的定论，如果最后 submodule 无法满足 core 分发，
  就只能上 plugin 了」）· supersedes 2026-08-24 的 §10.5 裁决之分发形态半边（载体＝
  `CONSTRUCTION-LEDGER.md` 公开化三批条目，按 `HD-59` 不就地改，原句留作当日历史）· 实测依据＝
  `tooling/sweep_refs.py` 三棵树对照 · rider `checklist-cited-not-carried`

- **向前更正（2026-08-30，轮 `CORE-ONLY-CODE` 之后）：本条「结构性的那一条」所记的冲突已经消失，
  三处事实均已被本批推翻。** `E10` 的成员数自轮 `CORE-ONLY-CODE` 起为 **七**（item D 删掉两份
  retired contract stub）；`CONSTRUCTION-CHECKLIST.md` 自轮 `CORE-ONLY-LAYER` 起不是成员，而是本仓
  在 `harness.json` 里声明的自有规则文件；两份 stub 已不在树上。故本条所说的「九分之三不 travel、
  两张清单互不相容」不再成立，rider `checklist-cited-not-carried` 亦已于轮 `CORE-ONLY-LAYER` 兑付
  删行（见 `CONSTRUCTION-INDEX.md` 抬头）。**本段只更正措辞与事实，不动本条裁决实质**：分发形态仍
  是「submodule 为默认、core 分发若最终做不到就上 plugin」，本条仍 `live`，边界段的三条路仍未走完。

### HD-65 · 契约 §13.1 的「not accepted」只指**验证路径**，够不到 accessor 与决策检查
- 2026-08-29 · user · scope: standing · status: **live**（这是对签字文本一个词的**解释**，契约自身
  不携带自己的解释，指令层也没有任何一处说这个词该读多严；`HD-64` 的边界段只管「准予改哪一类」，
  不管改完的那句话怎么读。故层内与契约内均无承载）
- 裁决：`contract/Document-Work-Assurance-Contract-v4.md:280-287` 里「one presented nonetheless is
  **not validated and not accepted**, fail closed」的后半句，与前半句**同指一件事**——没有验证路径
  就不可能被接受。它**不**延伸到 accessor（`flow.reviewed_candidate_ref`）与决策检查
  （`flow.check_repair_decision`）。
- 起因与量程（FULL `v3-review-full-a518888.md` `O-1` 实测）：「not validated」半边成立——三个
  validator（`review.validate_n2` · `review_subject.validate_w2` · 包根 `validate`）都把
  `review_result` 当未注册 kind 拒掉。「not accepted」半边够不到两处：accessor 按声明形状去根上读
  `candidate_ref`，而 `check_repair_decision` **用**它做决定且**从不验证它读的那份 result**，喂 v1
  形状进去返回干净报告（`test_the_v1_root_shape_is_unaffected` 钉的就是这条 live 行为）。
- 后果：**`HD-64` 的一致性条件（契约文字与代码行为必须一致）就此满足并关闭**——按本条的读法，代码
  与文字不冲突。本轮不改契约、不改 `flow.py`。
- 边界，且这一条比裁决本身更重要：**真正的缺口比 v1 大，本条不掩盖它**——`check_repair_decision`
  **对任何 result 都不验证**，v2 的也不验证；v1 只是它今天最显眼的一个面。该性质**本轮之前就存在、
  本轮一个字未改**，且已由 `tooling/rsclib/document_harness/review_result_v2.py:33-39` 在代码里写明。
  本条**不裁**那个缺口该不该修——它不是「not accepted 读多严」的问题，要修要另裁。
- basis: 用户裁决 2026-08-29（对话，三选一里选「只指验证路径，记一句边界」，且要求先给全 context）·
  FULL `migration/document-work-assurance-v3/v3-review-full-a518888.md` `O-1`（按 `R5` 归口用户）·
  `HD-64` 的一致性条件（本条即其答案）· plan ruling 2「不存在 v1 活例」使该条款反事实

### HD-62 · `E2` 冻的是**字节**，不是「本仓的这些路径」——故整体搬仓不是写（`HD-44` 的收窄后继）
- 2026-08-28 · user · scope: standing · status: **live**（`E2` 仍不说这些路径必须住在哪个仓：批
  `FREEZE-TO-ALARM` 的 item A（`184387c`，2026-08-27）把该条款从写前 gate 改成事后逐点披露的报警，
  改的是「写了之后欠什么」，没有回答「那些字节住哪」，故本条的主题在层里仍无承载。要转
  `implemented` 须有一个设计轮把「announced 面住哪」写进 `E2`。**`HD-44` 这段括号原写的 `E2` 引文
  「三个 blob 加一个目录，都由 inspection 可判」两度作废**——轮 `CONTRACT-V4`（2026-08-23）合三源
  为 v4 使三个 blob 变一件，item A 又按 open question 3 的答案删光了 blob 字面量，今日的 `E2` 是
  **一条路径加一个目录、零 blob 哈希**；原括号逐字留在 archive 的 `HD-44` 里，不就地改（`HD-59`））
- 裁决：`E2` 冻结的对象是**那些字节**（contract `b2dbdf75` · supersession-1 `68031fa2` ·
  supersession-2 `e1a2f26b` · 再基线时 schema pack 的十五件）。**字节完好地存在于某处、且被
  gitlink 钉住**时，把它们从某个仓移走**不构成 `E2` 意义上的「写」**。反读法（冻的是「本仓的这些
  路径」，故删除本身就是一次 `E2` 意义上的写）**被否**。今后任何调用者删掉自己那份副本，按本条
  同样不是写。
- **本条对 `HD-44` 的收窄只有一处**：原文末句「**真的改动那些字节仍然照旧欠裁决**，本条一个字都
  没放宽那一半」**不承接**。用户 2026-08-27 的裁决 1 取消了那个要求——announced 的字节可以写，
  欠的是事后在 commit 正文里逐站点披露（item A `184387c`）——故那半句是一条已被推翻的规则在决策
  簿里的存续；而本簿抬头写着「细则与裁决冲突，细则错」、`E10` 也写着 `§live` 在冲突时压指令层，
  留着它等于把裁决 1 结束的僵局在更高一层重新装回去（FULL `v3-review-full-ad0663d.md` `B-1`）。
  其余全文承接：主题、判据、反读法被否、后果里的住址与件数、以及基线。被否的反读法在 `HD-44`
  原文里的措辞是「未经裁决的写」，本条改写为「`E2` 意义上的写」——同一个被否的读法，换掉一个
  今日已无所指的限定词，原措辞在 archive 里逐字可读。
- 后果：**冻结面自 2026-08-17 起住在 harness 仓**，与命名它的那条规则同仓——这是本条要留下的
  那个事实，因为拆分后「`E2` 说的那些字节在哪」不再不言自明。调用者仓以 gitlink 钉住哪个
  revision，announced 面就是那个 revision 上的那些件——`HD-44` 建条日（2026-08-18）为十八件；
  自 `HD-56`（2026-08-23）合并三源为 v4 后为十六件（v4 一件 + schema pack 十五件）。
- **边界（本条不裁，写出来是因为它今天第一次可能被误读）**：本条判的是 `E2` 意义上的「写」，
  不是报警的机器谓词。item C 的 CI job `announced-path-disclosure` 用 `git diff-tree` 判某个
  commit 有没有改动 announced 路径，它看不见「这是一次整体搬仓」；真把这些路径搬出本仓的 commit
  照样会被判红，答案是在自己的正文里逐站点写出那些路径，不是援引本条。
- basis: 用户裁决 2026-08-18（对话，`HD-44` 的建条依据）· FULL `v3-review-full-2d148f3.md` `B-4`
  提出两读法并按 `R5` 归口用户 · 先例 `HD-39`（删除轮把 `E2` 的理由写出来）与 `HD-20`（冻结的
  意义就在必须有裁决——该条已于本批转 `retired`，此处只作 `HD-44` 建条时的先例留档）·
  **收窄依据 = 用户裁决 2026-08-27 ruling 1**（载体 `document-harness/plans/freeze-to-alarm.plan.md`）
  **与用户裁决 2026-08-28**（本批修腿的形状：立后继条目、`HD-44` 整条转 `superseded`）·
  FULL `v3-review-full-ad0663d.md` `B-1` · `HD-30` 部分收窄机制 · supersedes `HD-44`

### HD-59 · 已提交的结论不就地改，只向前更正
- 2026-08-26 · user · scope: standing · status: **live**（层内无承载：`E8` 的 commit 种类清单列了
  errata、`E9` 的预算词汇却没有 errata 的位置，两处都不说「已提交的结论怎么办」；本条即那个答案，
  且不靠给 `E9` 加位置来答）
- 裁决：一个**已提交的结论**——journal 的判断、评审记录里的判定、commit 正文的断言——**不得就地
  改写**。更正的形式是**向前新写一条**：新的 commit、新的记录、新的条目，或原处**另起一段**紧挨着
  它，原文逐字留着，让「曾经这么判过」可被 grep。`E8` 的 errata 因此读作「另写一条更正」，不是
  「回去改那句话」。
- 后果：VERIFY `v3-review-verify-0f0498f.md` `V-4` 点名的结构性缺口就此关闭而**不开轮**——那个缺口
  成立的前提是「FULL 之后要更正一个已提交的结论」这件事会发生，本条判它不该发生。`E9` 不加 errata
  预算位置（`E6`：需要新机器的修，是重新质疑被守之物的信号）。
- 边界：本条管**结论**。journal 的**数字**更正照旧走 `HD-23`（它自己的括号就把结论排除在外）；被
  评审的 work product 在 FULL 之后的实质改动照旧是 `E9` 的修腿。
- **追溯到已发生的那一例，用户 2026-08-26 裁「改严格」**：轮 `CORE-SET-LAYER` 的 `0f0498f` 就地
  改写了该轮 journal §6 的结论（该次改写已计入该轮修腿的第二次消耗，收轮 `83aecd4` 写明，不因复原
  而退还）。本条的应用批把该段**逐字复原自 `92cc514`**，更正另起一段紧挨其后，并在那段里写明它自己
  的来历——本条的第一次应用，恰好是对本条第一次违反的更正。
- basis: 用户裁决 2026-08-26（对话，答 `V-4` 经 `R5` 归口之问，并当场裁定追溯形态）·
  `v3-review-verify-0f0498f.md` `V-4` · rider `e9-pair-budget`（相邻的 `E9` 措辞分歧，不由本条兑付）

### HD-41 · 量程纪律 + 扫类留痕：断言先声明量程，修 finding 先跑扫类 grep 并贴证据
- 2026-08-14 · user · scope: standing · status: **live**（`§11` 住在一份讲别的主题的设计稿里，
  `HD-5` 的必读只覆盖 `§live`，故今后设计轮触达不到它——本条即其唯一可达承载。**要转
  `implemented` 须先有一个设计轮把它写进指令层**，那是另一件事）
- 裁决：① **量程先于断言**——每条实测断言先声明量程（整文件 / 某代码块 / 某目录 / 全仓 tracked /
  某 revision），再跑**覆盖该量程**的命令；对不上不得写成断言。② **绝对量词**（全 / 只 / 唯一 /
  零 / 不留）必带量程。③ 带计数的断言注明 revision；会随时间增长的量另写「落地时按当时的 base
  再算」——`E3` 管时间，本条管范围，二者都要。④ **修 finding 先扫类后落笔**：改动前 grep 该断言
  的关键字串在本轮全部工作文件里的命中，**把 grep 输出贴进 commit 正文**；扫类是动作不是自觉，
  贴证据是为了「跑没跑」可被评审员当场看见。
- 起因：至本条建条时 R0 四轮独立 read 共返**五条** must-fix（1+1+2+1，各记录摘要行；其后第五轮再返两条），分两类——**量程错**（断言范围大于所跑命令：删除不留
  悬空引用 / 耦合全在顶层三行 / 其替换句「块外四处」）与**半径不够**（只修 finding 点名那处，
  不扫同一断言的其他写法：`M-2` 的 plan 四处、`M-1D` 的另四处）。①–③ 治前者，实证有效——
  落地当轮自查即抓到 read 未报的五处；④ 治后者，此前只作为 `§11` 第 4 条的自觉纪律存在，写下它的
  下一个 commit 就没执行。放大器照记：同一事实在设计稿 / journal / plan / 决策簿里各写一遍，
  每修一条的潜在站点是 3–5 个。
- 后果：`HD-36` ① 与 `E7` 的扫类义务由「应当」变为**可核**（commit 正文里有没有 grep 输出）。
  **不新增机器**（`E6`）：纯纪律 + 留痕。**未解决**：本条与指令层的关系——`E3` 只管时间，
  范围与扫类留痕在层里无承载，要不要写进 `E3` 或另起一条是**下一个设计轮**的题。
- **2026-08-17 用户追认：维持纯纪律，那个设计轮暂不开**（拆分批 R3 的 FULL `O-A` 归口用户）。
  依据是同一轮的实测：该缺陷类在一轮之内又发生至少四次——FULL 两条 blocker（代码注释里没跑过
  命令的「因为」· 把眼睛扫到的两处写成「全部」），VERIFY 三条残留（其中一条是**修它的那次自己
  把量程写窄了**：声明的量程返 6、实际跑的窄命令返 4；另一条是同一段落相邻两行自相矛盾），
  且全部由**评审员**而非本条纪律抓出。用户看过这组数据后仍选 `E6`：**不为一条被绕过的纪律再造
  机器**。上一行的「未解决」不因此关闭——题还在，只是排期未定。
- basis: 用户裁决 2026-08-14（对话，「同意改写法」+「建一条吧」）· `document-harness/split-design.md`
  §11 · 四份 read 记录 `v3-checkpoint-read-{ffbc393,0cc45ce,b75676e,a2f8c7d}.md` 的 must-fix 段

### HD-36 · `E10` must-fix 通道放松：收扫类 + 无字节由 executor 写；design test 收窄回自由通道
- 2026-08-13 · user · scope: standing · status: **live**（read 已走完（`v3-checkpoint-read-f61ce2c.md`）
  且 ① 的承载已落 `E10` 通道句与 `:110`、② 已落优先句；**用户 2026-08-13 裁定仍留 `live`**——
  按 `HD-2` 的判据「有没有别的东西替它说话」，**②「design test 不伸进 must-fix 通道」这件事层里
  一个字都没有**：`E10` 的通用 design test 仍无限定地盖住每一个 amendment，豁免只由本条承载
  （`v3-checkpoint-read-136f27f.md` / `-f61ce2c.md` 的 `O-1`）。要转 implemented 须先有一个设计轮
  给那句加限定）
- 裁决：① must-fix 通道除「删除 + 点名的字面替换」外，**另收**同一缺陷在**其余站点**的同款修
  （扫类），以及 finding **未供字节**时由 **executor 自己写**的修——must-fix 是唯一不能等的一档。
  ② `E10` 优先句的 `the named literal replacement` 换成 `the bytes the finding supplies`，
  把 design test **收窄回自由通道**，不再伸进 must-fix 通道。
- 后果：`E7`（绑 executor：测缺陷类不测实例）与 `E10`（不许写未点名字节）的对冲解除。同批扫类
  改掉「a finding without appliable bytes banks」为「**below must-fix** without appliable
  bytes banks」——不改这句则无字节 must-fix 仍会被字面读成 bank。**已裁不做**：amendment commit
  声明扫了哪个类/哪些站点（零实例，见 basis）· 给 amendment/re-read 链加计数（`E6`，根因交给扫类）。
- basis: 用户裁决 2026-08-13（对话）· 实证＝批 B R4 一个缺陷类拆成两轮 read 才修完
  （`v3-checkpoint-read-be9878a.md` `M-1` 点了实例、`v3-checkpoint-read-0aed595.md` `M-1` 点了
  兄弟句）· `v3-checkpoint-read-8884f47.md` `O-1`（design test 与 must-fix 通道对删除的分歧，
  且「没加 bound 就不算 design」这个读法两次被取用而文本里没有）· 零实例依据＝同轮 FULL +
  `E10` must-fix 通道至今未发生，且纯 read 轮无 FULL 故按 `E9` 判据每个改动都是 pre-submission
  correction、零消耗

### HD-35 · io-design v1 已签字：R3 / R4 / 拆分批的执行依据
- 2026-08-12 · user · scope: standing · status: **live**（是后续各批的执行依据；各批执行完其
  对应节后可议转 implemented。本条即签字记录本身——io-design.md 按 governance-scan 判据不携带
  自身审批状态，签字住这里）
- 裁决：用户签署 `document-harness/io-design.md` **v1 修正版**（经 R2 转录核查 33 findings 的
  更正，`790e06e`；签字绑定字节 blob `ef75b870`、sha256 `10981afd…c3c6`）。八节全部生效为设计
  依据：R3 按 §5 施工、R4 按 §8 重指清单施工、拆分批按 §6/§7 施工。
- 后果：R2 随本签字 CLOSED（其 gate 即此，按已批预览卡 R2 无 FULL 预算）；对该文件的后续实质
  修改欠重签。
- **重签 2026-08-12（同日第二次）**：载体裁决变更——策略承载由「`CLAUDE.md` 内的一节」改为
  **独立策略文件**（本机 `ResearchSystem/HARNESS-POLICY.md` + `CLAUDE.md`/`AGENTS.md` 各一行
  指针；依据 = 实测 CLAUDE.md 113 行、镜像双写、其 :68 push-detail-down 规则）；§5/§6/§8 三处
  随裁更新。重签绑定 blob `8f3c82c2`、sha256 `730fddf4…8157`（初签 `ef75b870` 留档）。
- **重签 2026-08-23（第三次，轮 `CONTRACT-V4`，随 `HD-56` 签字一并）**：除锈两处——:99-100 的
  `HI-route` 悬空指针改为成文化路由（rider `io-hiroute-stale` 兑付）+ 命令面重签标记（rider
  `six-signed` 本文件半边兑付）。重签绑定 blob `a1594eb2…`、sha256 `6fc29c11…b9c2`（blob 内容，
  LF），135 行；前签 `8f3c82c2` 留档。
- basis: 用户签字 2026-08-12（对话）· `document-harness/io-design.md` @ `8f3c82c2`

### HD-34 · 调用者纪律：零升级、适配留痕；copy 仅为逃生口（`HD-29` 拆分后继 ②）
- 2026-08-12 · user · scope: standing · status: **live**（待首个外部调用者执行）
- 裁决：调用者仓内**不得改动/升级 harness 内容**；任何适配**必须记入调用者自己的 decision
  log**。**copy 仅为逃生口**（submodule × worktree 冲突时），代价 = 版本追溯 + 漂移可见性；
  漂移现阶段接受。
- basis: journal §5 · `document-harness/io-design.md` §7 · 用户裁决 2026-08-12 ·
  supersedes `HD-29`（与 `HD-33` 共同取代）

### HD-23 · journal **数字**更正类比照 ledger/riders-only（扩 2026-08-04 裁决）
- 2026-08-08 · user · scope: standing · status: **live**（判据句无别的承载）
- 裁决：评审 finding 指向 **journal 里的数字**（非结论、非被评审的推理本身）时，其更正比照
  ledger/riders-only 处理——**不消耗 `E9` 修腿、不欠 targeted VERIFY**；前提是更正落在下一次评审的
  subject 范围内（会被评审到）。2026-08-04 原裁决（判据「改的是不是被评审的 work product」）不迁
  不改，本条是其外延；先例 `8dae1e0`；起因 = `7a08265` VERIFY §4.3 指出 A1 曾把原裁决读宽。
- basis: `v3-review-verify-7a08265.md` §4.3 · 用户裁决 2026-08-08

### HD-9 · 记录层三留三砍判据
- 2026-08-08 · user · scope: standing · status: **live**（standing 量尺，判据无别家承载）
- 裁决：一件记录留下的理由按**可核验性**判，且写明谁在什么时候读。**三留**：证据（不可再生的
  一手观测）· 绑定（让断言可被反驳的把手）· 判断（不可由命令重新得出的推理）。**三砍**：可再生
  的方便 · 重复拷贝 · 无锁证词。判断按四作用域分流：绑将来所有轮→提规则面（经本 log 晋升）·
  绑一个机制→就地 docstring · 绑未解问题→rider · 只绑本轮→留在 record 原地。
- 后果：A2 的 T1/T2/T3 设计以此为尺；D3 的重测按配方/证词/判断三分，不用原 M4 的 55%。
- basis: [journal/decision-log-2026-08-08.md](document-harness/journal/decision-log-2026-08-08.md) §1–2

## §implemented —— 在 force，细则已由别处承载（不必读，grep 可达）

### HD-70 · 契约 v4 `:118` 的 VERIFY verdict 行准予就地**加一个值**——本裁**明写盖过契约 §13**，`HD-63` / `HD-64` / `HD-67` / `HD-68` 之后本族第五条，盖的对象是「闭合枚举的**词表扩张**」
- 2026-09-03 · user · scope: one-shot · status: **implemented**（用户裁决 2026-09-03 翻态，挪节与翻转同
  commit 按 `HD-2`；承载 = `15e5ccc`（契约 `:118` 加 `UNRESOLVED_BLOCKER`、`:127` 删序数，
  `CONTRACT-V4-SIGNATURE.md` 第八笔签署后写入），经 FULL `67dbb08` + VERIFY `da1aac3` 审毕；改后文本欠
  `E10` 独立复读，由**下一轮开轮冷读**承载，复读回来后转 `retired` 归用户；原 live 理由随本条挪节留在下文
  括号内：层内零承载：契约 §13 说反面、§5 自称 closed
  enums；前四条各只盖自己那一类——签署时为真后来变假的陈述 / 对空集生效的要求 / 调用者不可达的历史 /
  引用形态——本类不在其中。承载 = 轮 `PROMISE-PATH-VOCAB` executor 写契约的那个 commit +
  `CONTRACT-V4-SIGNATURE.md` 记入第八笔签署后写入 + `E10` 对被改文本的独立复读；落地后转 `implemented`、
  复读回来后 `retired`，两次翻态皆归用户（`HD-2`）。本条由 orchestrator 按 plan 裁决 6 转写 2026-09-01
  的「6 i」与 2026-09-03 `E11` 卡上的站点枚举追认，不加新裁决）
- 裁决：准予 executor 就地改 `contract/Document-Work-Assurance-Contract-v4.md:118`（本 commit 时）的
  VERIFY verdict 行 `REVIEWED_NO_BLOCKER · SPEC_GAP`，**加入一个第三值**，义为「一次修腿之后 blocker
  仍立」，使 `SPEC_GAP` 回到它的定义（spec 有缺、新 WorkSpec、新 START）。值名由 executor 在本轮第一个
  决策点提出、用户追认（`HD-69`：同会话停、不另派发），**追认前一字不写**；FULL 行 `:117` 一字不动。
  本裁**明写盖过 §13** "Signed contracts are never amended in place; corrections create a versioned
  successor"——依据同前四条：本簿抬头「细则与裁决冲突，细则错」与 `E10` 自认 `§live` 冲突时压它。
  被放弃的另一路（为一行表格出 v5 后继）在 plan 开轮问题 6 提出、未取。
- **站点枚举（plan 裁决 6：每处先点名、后动笔；量程 = 全仓 tracked 于本 commit 之父 `6d7e26c`，
  排除两份 archive、`migration/` 与 `document-harness/journal/`；grep 输出贴在本 commit 正文）**。
  **授权站点一处**：`:118`。**兄弟候选两处**，executor 扫类后在命名决策点一并提请追认，追认前一字不写：
  `:127-129`「nonblocking uncertainty is never a fourth control verdict」（加值后「fourth」这个数字可疑，
  但该句主语是 nonblocking，而新值表示 blocking 仍立，语义可能不动）· `:196-197`「A remaining blocker
  or `SPEC_GAP` stops; no second fix or review-of-review exists」（新值正是「remaining blocker」的机器
  形态，语义应不动）。**明确不在射程**：`:117` FULL 行 · §3 接口 · §7 不变量 · §13 版本边界 ·
  `:105` / `:122`（件 1 让它们变真，不改字）。executor 扫类若再见本类站点，同一决策点提请，本条不预授权。
- **与前四条的区别照记，五条各自独立、互不作先例扩张**：`HD-63` 盖「签署时为真后来变假的陈述」，
  `HD-64` 盖「对空集生效的要求」，`HD-67` 盖「调用者不可达的历史」，`HD-68` 盖「引用形态」；本条盖的是
  **闭合枚举的词表扩张**——既非更正也非删除，而是给一条在 force 的要求**加**一个值，是本族唯一一条让
  契约今后要求得更多的。正因如此 plan 明写「scope = this one vocabulary change, no precedent expansion」。
- 边界：只此一行、只此一个值；FULL 词表不动；不开「契约枚举随手可加」的通道；不授权任何别的枚举行。
  `E10` 的 design test **照常触发**——本改动改变 `R3` 要求什么，故开轮，轮即 `PROMISE-PATH-VOCAB`，
  本条**不**做 `HD-64` 式的免开轮 set-aside。
- 后果：v4 是 announced 路径，写它的 commit 按 `E2` 在正文逐点点名
  `contract/Document-Work-Assurance-Contract-v4.md`；`CONTRACT-V4-SIGNATURE.md` 同 commit 记入第八笔
  签署后写入，不重指签字 blob（仍是 `614932de…`）；改后文本欠 `E10` 独立复读，随本轮下一次层读。
  同轮改 `document-harness/RULES.md` `R3`、`document-harness/REVIEW.md:129-135`、
  `schema/document-assurance-v3/review.v2.schema.json`（后者 announced、逐点披露）不是本条的对象——
  它们归 `E10` 的设计轮，本条只盖契约。
- basis: 用户裁决 2026-09-01（对话「6 i」，载体 plan `document-harness/plans/promise-path.plan.md`
  裁决 6）· 用户裁决 2026-09-03（`E11` 卡问题 2「ok」，载体同 plan 裁决 8）· `HD-63` / `HD-64` /
  `HD-67` / `HD-68`（同族前四条，各自边界段把本类排除）· 调用者 run 1 VERIFY 借用 `SPEC_GAP` 的实证
  （其 `1a634fe` 收口正文；plan 件 2）
- **向前更正与兄弟站点终裁（2026-09-03；上文逐字留着，`HD-59`）**：本条站点枚举把「A remaining blocker or
  `SPEC_GAP` stops」句记为 `:196-197`，executor 于 `b9710af` 实测为 `:195-196`（`:197` 空行）。兄弟站点按
  plan 裁决 11 终裁（用户「2 同意」）：`:127-128` 与 `schema/document-assurance-v3/user-decision.schema.json:44`
  删序数，已写入 `15e5ccc`；`:195-196` 与扫类新见的 `:200-201`「an unrepaired blocker」不改——新值命名的是
  报告该状况的 verdict，不是新增通往 `STOPPED_REPLAN` 的路。

### HD-68 · 契约 v4 `:29` 的 wikilink 准予就地去链接——本裁**明写盖过契约 §13**，`HD-63` / `HD-64` / `HD-67` 之后本族第四条，盖的对象是「可跟随、但调用者拿不到字节、且既无路径也无 holder」的**引用形态**
- 2026-08-30 · user · scope: one-shot · status: **implemented**（用户裁决 2026-08-30 翻态，挪节与翻转同 commit 按 `HD-2`；承载 = `322fd1c`，经 FULL `8997d94` + VERIFY `8214f50` 审毕；改后文本欠 `E10` 独立复读，随轮 2 开轮冷读，复读回来后转 `retired` 归用户；原 live 理由随本条挪节留在下文括号内：层内零承载：§13 说反面；前三条各只盖自己那一类，
  本类不在其中；rider `contract-wikilink-tier` 两次到期——`CORE-SET-CODE` 冷读入 bank、本轮 `228df32`
  触碰记录——皆因无授权而不兑。承载 = 本轮 executor 的 pre-submission correction commit +
  `CONTRACT-V4-SIGNATURE.md` 记入签署后写入 + `E10` 对被改文本的独立复读；落地后转 `implemented`、
  复读回来后 `retired`，两次翻态皆归用户（`HD-2`））
- 裁决：准予 executor 就地改 `contract/Document-Work-Assurance-Contract-v4.md:29`（`607728a` 时 `:36`）
  的 `[[document-work-assurance-harness-v3.plan|Document Work Assurance Harness v3]]`：**链接形态消失**——
  该 plan 以标题指称，不给任何可跟随的路径或链接；紧随其后括号里的 SHA-256 与「digest 对本仓无 blob
  可验」（`HD-57`）那段说明是纯建造史，可随之删；「Plan §2 decisions V3-D1–D10 are the locked design
  authority; a genuine conflict between this contract and the plan is a `SPEC_GAP`」这句义务**留**。
  字节归 executor 写并在 commit 正文披露。本裁**明写盖过 §13** "Signed contracts are never amended in
  place"，依据同前三条。
- **与前三条的区别照记**：`HD-63` 盖「签署时为真后来变假的陈述」，`HD-64` 盖「对空集生效的要求」，
  `HD-67` 盖「调用者不可达的历史」；本条盖的是**引用形态**——内容留、形态变。理由是 rider 的实测：
  `layer_path_check` 的 `TOKEN` 要反引号、`PATHLIKE` 白名单无 `.plan`、`sweep_refs` 的 `LINK` 只认
  `](…)`，wikilink 三个守卫都在结构上看不见，是全层唯一一处两边都够不着的形态。四条各自独立，互不作
  先例扩张。
- 边界：只此一站点、只此一种形态；不开「契约里的链接随手可改」的通道；不动 §3 接口 / §5 枚举 / §7
  不变量 / §13 版本边界。
- 后果：写它的 commit 按 `E2` 在正文逐点点名 `contract/Document-Work-Assurance-Contract-v4.md`；
  `CONTRACT-V4-SIGNATURE.md` 同 commit 记入签署后写入，不重指签字 blob；rider `contract-wikilink-tier`
  同 commit 删行（`R10`：兑付 = 同 commit 删行）；改后文本欠 `E10` 独立复读，随本轮下一次层读。
- basis: 用户裁决 2026-08-30（对话：「现在裁 HD-68，本轮一并改」；载体 plan
  `document-harness/plans/core-only.plan.md` 裁决 23）· rider `contract-wikilink-tier`
  （`v3-cold-read-b737742.md` `L-1`）· `228df32` 正文的触碰记录（「redeeming it wants a fourth ruling
  in that family」）· `HD-63` / `HD-64` / `HD-67`

### HD-67 · 契约 v4 里两块**纯建造史**准予就地删除——本裁**明写盖过契约 §13** 的 in-place 禁令，且不开设计轮；`HD-63` / `HD-64` 之后本族第三条，盖的对象是「调用者够不到的历史」
- 2026-08-29 · user · scope: one-shot · status: **implemented**（用户裁决 2026-08-30 翻态，挪节与翻转同 commit 按 `HD-2`；承载 = `228df32` 两块 + `322fd1c` 按 plan 裁决 22 补删 §12 ¶1，经 FULL `8997d94` + VERIFY `8214f50` 审毕；改后文本欠 `E10` 独立复读，随轮 2 开轮冷读，复读回来后转 `retired` 归用户；原 live 理由随本条挪节留在下文括号内：层内零承载：契约 §13 说的是反面；`E10` 的 design test
  管的是「改变规则要求什么」而本条不改任何要求，故 design test 不触发，但 §13 的字面禁令仍须明裁盖过，
  否则 executor 无据可写。承载 = 轮 `CORE-ONLY-LAYER` executor 写契约的那个 commit + `CONTRACT-V4-SIGNATURE.md`
  记入第五笔签署后写入 + `E10` 对被改文本的独立复读；落地后转 `implemented`、复读回来后 `retired`，两次翻态
  皆归用户（`HD-2`）。本条由 orchestrator 按 plan 裁决 18 转写 plan 裁决 4 与 11，不加新裁决）
- 裁决：准予 executor **就地删除** `contract/Document-Work-Assurance-Contract-v4.md` 里两块只属于本仪器
  建造史、任何调用者都够不到的文字：① 抬头的**合并来源段**（本 commit 时 `:21-33`：v4 合并了哪三份签字
  文本、各自 blob、签字日期与记录文件名 `N0-record.md` / `W2-record.md` / `supersession-2-signature.md`、
  措辞差异归 `contract-v4.plan.md`）② **§12 *Dependency and historical map* 的前两段**（`:248-257`：
  v1/v2 不可变性、A4 作为 v2 史、`N0-record.md` §4 提名的复用候选）。**§12 第三段留**（`:259-263`，
  v3 默认接口移除了什么、无用户批准的 plan 修正不得回归——那是对调用者有效的义务）；签字语义抬头块与
  §14 留，其中对 `CONTRACT-V4-SIGNATURE.md` 的指称可由 holder 句替代文件名，归 executor 定。改后的文字
  **该说什么归 executor 写并在 commit 正文披露**（`HD-64` 同款）。本裁**明写盖过 §13** "Signed contracts
  are never amended in place; corrections create a versioned successor"，依据同前两条：本簿抬头
  「细则与裁决冲突，细则错」与 `E10` 自认 `§live` 冲突时压它。
- **与前两条的区别照记，三条各自独立、互不作先例扩张**：`HD-63` 盖「签署时为真、后来变假的陈述」，
  `HD-64` 盖「一条对空集生效的要求」；本条盖的**既不是真假也不是要求，是对调用者不可达的历史**——
  plan 裁决 4 的原话是产品契约装着本仪器的建造史是对规则文本的污染，早先「逐条标 holder」的答法
  治的是症状（实测七处站点里三处已带 holder 句，正是写它的人已知调用者够不到、却以标注代替删除的证据）。
- 边界：只授权这两块。判据 = **该段对调用者是否可达、是否施加义务**——一句对调用者有义务效力的话不在
  射程内，§12 第三段即例；本条**不**开「契约里的历史随手可删」的通道，也**不**授权改动 §3 接口 / §5
  枚举 / §7 不变量 / §13 版本边界的任何一字。走的是 plan 裁决 11 的**轻路线**：不重签，签字对象仍是
  `CONTRACT-V4-SIGNATURE.md` 记的 `614932de…`。
- 后果：v4 是 announced 路径，executor 写它的 commit 按 `E2` 在正文逐点点名
  `contract/Document-Work-Assurance-Contract-v4.md`；`CONTRACT-V4-SIGNATURE.md` 同 commit 记入第五笔
  签署后写入，不重指签字 blob；改后文本欠 `E10` 独立复读，随本轮下一次层读（复读回来前，本轮任何
  依赖被改文本的结论不成立）。剥史树上契约的 7 处 NAMETOK（plan 量程表 `:16/:27/:28/:31/:33/:254/:365`，
  于 `607728a` 测）中五处随两块消失，余两处（`CONTRACT-V4-SIGNATURE.md`）由 holder 句处置。
- basis: 用户裁决 2026-08-29（plan `document-harness/plans/core-only.plan.md` 裁决 4「要一起做了」、
  裁决 11「轻路线」、裁决 18「由 orchestrator 转写并先于冷读落」）· 同 plan 量程表
  *The contract's provenance — ruling 4's object, in blocks rather than lines*（四块四判）· `HD-63` /
  `HD-64`（同族前两条，各自的边界段正是把本类排除在外的那段）· `HD-59` 向前更正（原文各段逐字留着）
- **向前更正（2026-08-29，开轮冷读 `migration/document-work-assurance-v3/v3-cold-read-a542c6d.md`
  `M-1`，用户当日裁；上文各段逐字留着，`HD-59`）。** 后果段「余两处（`CONTRACT-V4-SIGNATURE.md`）由
  holder 句处置」**少算一处**：契约里指向签字记录的站点是**三处**，第三处是 front matter `:9`
  的 `signature_owner: CONTRACT-V4-SIGNATURE.md (this instrument's v4 signature record)`——无反引号，
  故 `sweep_refs.py` 的 NAMETOK 普查在结构上看不见它。错在推断不在量程声明：上文把 NAMETOK 普查当成了
  「调用者够不到的引用」的普查。**用户裁：`:9` 留原样，一字不改**——它是机器读的 owner 委托键
  （`checks.py:486` 记为正确模式、`test_candidate_checks.py:1997-2000` 钉住必须存在），值里已自带
  holder 短语。executor 写契约的 commit 正文按 `E2` 点名三处及各自处置（`:9` 维持；`:16`/`:365` 依上文），
  `HD-41` ④ 的扫类以三处为准。同一冷读 `O-1` 所记——本条以「第五笔签署后写入」取代 plan 裁决 11 的
  「重指新 blob」字面，因后者自 `184387c` 起无对象——照记，不改本条。

### HD-64 · 契约 v4 `:279-281` 的 v1 验证路径规定准予就地改——**这次盖过 §13 的是「要求」，且明裁不开设计轮**
- 2026-08-28 · user · scope: standing · status: **implemented**（用户裁决 2026-08-29 翻态，挪节与翻转同 commit 按 `HD-2`；承载 = amendment `2aabd5a`，经独立复读 `ff00a1d` 确认；其一致性条件由 `HD-65` 答毕；原 live 理由随本条挪节留在下文括号内：`HD-63` 的边界段把「改变契约**要求什么**」
  明确排除在其量程之外，故本条不是 `HD-63` 的重述也不由它承载；`E10` 的 design test 说这类要开轮，
  本条推翻的正是那句在本次的适用——层里没有任何一处说「用户可以裁不开」，故层内无承载。承载 =
  本轮第二份 amendment commit；落地后转 `implemented` 归用户（`HD-2`））
- 裁决：`contract/Document-Work-Assurance-Contract-v4.md:279-281` 的「A result with no
  `schema_version` key is a v1 result and is **validated against pinned v1 semantics**」**准予就地
  更正**。依据是**用户已裁的 plan ruling 2**（`document-harness/plans/v1-result-retire.plan.md:52`：
  「任何地方都不存在 v1 活例」）——该 bullet 规定的动作**没有对象可以触发**，本轮 item C/D 删掉的是
  一条对空集生效的要求的执行路径。**本条不采纳** reader 提出的「第二读法」（把 pinned v1 semantics
  读作 commit 里 `git show` 可达的那份 schema）：那读法让 v4 一字不改，但代价是改变一条未被触碰的
  规则的含义，用户选了就地改，故该读法在本轮不成立、也不作为今后的解释。
- **两笔代价照记，不软化**：① 本条盖过 §13 的对象是**要求**，比 `HD-63`（只盖陈述性事实）走得远，
  是这一族裁决第一次这么做。② `E10` 写着「replacing or deleting text so that what a rule requires
  changes, is design and opens a round」——**本条明裁本轮不开设计轮**，依据是本簿抬头「细则与裁决冲突，
  细则错」与 `E10` 自身承认 `§live` 在冲突时压它。这一次 set aside 是一个可 grep 的事实，不是先例的
  自动扩张（见下边界）。
- 边界：本条**只**授权这一个 bullet、只在这一个依据上（其规定的对象已被用户裁为不存在）。它**不**开
  「签字文本里的要求可以就地改」的通道，也**不**授权今后任何 design 类改动免开轮——下一次要免，
  要另裁。更正后的文字**该说什么**归 executor 写并披露，与 plan item D 的那个 executor 决定
  （`result_schema_kind` 遇到无 `schema_version` 的实例该怎么办）**必须一致**：契约文本与代码行为
  对不上就是本条没执行完。
- 后果：本轮 item C 与 item D 解锁，但**要等这第二份 amendment 的独立复读**（`E10`：改变了要求的
  amendment 不享受「读前可依赖」的延后，因为它对在飞的本轮效果非零）。v4 是 announced 路径，写它的
  commit 按 `E2` 逐点点名全路径；`CONTRACT-V4-SIGNATURE.md` 记入第四笔签署后写入。
- **承载已落，状态未翻（`HD-2`：只有用户能翻，session 只能提议）。** 本条的 amendment commit 即
  `V3-V1-RESULT-RETIRE-HD64-AMENDMENT-v1`（本 commit）。建条时记的 `:279-281` 已漂，落笔前重测为
  `:280-281`。改后的 bullet 不再规定任何验证路径，只绑「不验证、不接受、fail closed」与原有的
  「no cross-version fallback」，并把**由哪个机制抬起这个停**明写为归实现选——这是为满足本条边界段
  「与 item D 的 executor 决定必须一致」而作的执行选择：那个决定尚未做出，两条候选落法（直接 raise ·
  继续指一个已无法验证的 kind，后者落到 `review.py` 的 unknown-kind 分支）都让无 `schema_version`
  的实例不被验证、不被接受，故改后的文本对两者皆成立而不预先锁死其一。**该判断由读代码得出、未经
  执行**（本 session 的 python 被环境权限层拒绝，见本 commit 正文的 ceiling 段）。被否的第二读法按
  本条写进契约并注明不作为今后的解释。扫类与量程见本 commit 正文。`CONTRACT-V4-SIGNATURE.md` 按
  后果段记入第四笔签署后写入。**提议转 `implemented`**——待 `E10` 对被改文本的独立复读回来后由用户
  裁。原文各段逐字留着（`HD-59`）。
- basis: 用户裁决 2026-08-28（对话，四选一里选「再裁一条，扩到『要求』这一类」）· 复读记录
  `migration/document-work-assurance-v3/v3-cold-read-dcb3aef.md` `M-1`（供三种形状、故意不供字节）·
  `document-harness/plans/v1-result-retire.plan.md:52` ruling 2（本条的实质依据）· `HD-63`
  （同族前一条，其边界段正是把本类排除的那段）· `HD-36` ②（design test 不伸进 must-fix 通道——
  本条不倚赖它，因为本次是 design 类而非 must-fix 通道的射程内，故另裁）

### HD-63 · 签字文本里「签署时为真、后来变假」的字面准予就地更正——本裁**明写盖过契约 §13** 的 in-place 禁令
- 2026-08-28 · user · scope: standing · status: **implemented**（用户裁决 2026-08-29 翻态，挪节与翻转同 commit 按 `HD-2`；承载 = amendment `e578e70`，经独立复读 `fad8df2` 确认 must-fix 已 discharge；原 live 理由随本条挪节留在下文括号内：层内与契约内均无承载：契约 §13 说的是
  反面，而本裁盖过它；`E2` 自 2026-08-27 起只欠事后披露、**从来不是**挡就地改的那条，两者是不同的
  对象。承载 = 本轮 must-fix 通道的 amendment commit；落地后转 `implemented` 归用户，session 只能提议
  （`HD-2`））
- 裁决：用户裁「就地改」，并**明写此裁盖过 `contract/Document-Work-Assurance-Contract-v4.md` §13
  的 "Signed contracts are never amended in place; corrections create a versioned successor"**。
  本次量程 = 轮 `V1-RESULT-RETIRE` 的冷读 `M-1` 所指的那一类断言，逐处点名：① v4 `:284-287`
  承诺 `review.schema.json` 与 v1 checker functions 留着供读 pinned v1 history 的那一句，**两半都改**
  （checker 半边已被 `56d1b17` 弄假、schema 半边被本轮 item C 弄假）② `document-harness/REVIEW.md:95-96`
  的 "the frozen v1 schema, which is untouched" ③ `document-harness/README.md:20` 表格里指向
  `review.schema.json` 的链接 ④ 同一缺陷类在别处的站点，由 executor 按 `HD-41` ④ 扫类后逐处修——
  已知一处是 `CONTRACT-V4-SIGNATURE.md` 里「签署后写入 v4」的清单（现列 `HD-57` 与 `CORE-SET-SIGNATURE`
  两笔，本轮是第三笔）。
- **补记：§13 此前已被绕过两次，且两次都没声明。** 实测——v4 签署于 `23ca45b`，其后 `1656e59`
  （`HD-57` 应用批，2026-08-23）与 `07ef526`（`CORE-SET-SIGNATURE` item F，2026-08-26）**都就地改了
  签字文本**，两次的 commit 正文 grep `section 13` / `§13` / `in place` / `amend` **全部零命中**。
  本条把这两笔记在账上；不追溯改写那两个 commit（`HD-59`：向前更正，不就地改历史）。
- 边界：本条**不**授权对签字文本的任意改动。它盖过 §13 的只有一类——**签署时为真、后因别处裁决或
  别处删除而变假的陈述性字面**；改变契约**要求什么**的修改仍是 §13 的正路（versioned successor），
  且按 `E10` 属 design、要开轮。判据是那句话陈述的是事实还是义务。
- 后果：本轮 `M-1` 走 `E10` 的 **must-fix 通道**——amendment commit + 对被改文本的独立复读，**不是轮、
  不花 `E9` 预算**（`HD-36` ① 收扫类与「finding 未供字节时由 executor 自己写」，本 finding 正是未供
  字节）。design test 按 `HD-36` ② 不伸进 must-fix 通道，故不开设计轮。v4 是 announced 路径，
  写它的 commit 按 `E2` 在正文里逐点点名全路径。
- **承载已落，状态未翻（`HD-2`：只有用户能翻，session 只能提议）。** 本条的 amendment commit 即
  `V3-V1-RESULT-RETIRE-M1-AMENDMENT-v1`（本 commit）：量程 ①②③ 逐处改毕，④ 的扫类另加一处
  `schema/document-assurance-v3/review.v2.schema.json:5`（同一句式的兄弟：「The v1 file is
  untouched and stays frozen for reading pinned v1 history」），并按 ④ 已知项在
  `CONTRACT-V4-SIGNATURE.md` 记入第三笔签署后写入。**提议转 `implemented`**——待
  `E10` 对被改文本的独立复读回来后由用户裁。原文各段逐字留着（`HD-59`）。
- basis: 用户裁决 2026-08-28（对话两问：「E2 现在放宽了，不能直接允许 v4 就地更改吗」→ 澄清挡路者是
  §13 而非 `E2`，随后裁「明写盖过 §13，并补记前两次」）· 冷读记录
  `migration/document-work-assurance-v3/v3-cold-read-60bf9eb.md` `M-1` · 先例 `HD-57`（同一形状，
  五处签字面陈旧字面，但其措辞只提 `E2`/`HD-20`、未点名 §13——本条即那个缺口的补记）· `HD-59`
  向前更正 · `HD-41` ④ 扫类留痕


### HD-58 · C4 `O-1` 采样义务两分：产品 run 只记一行；读数与三分支改判归构造轮（`HD-54` 的收窄后继）
- 2026-08-26 · user · scope: one-shot（读数发生并改判后本条消耗；消耗前仍可 supersede）· status:
  **implemented**（承载两处，与本条同 commit 落地于轮 `CORE-SET-LAYER`：`EXECUTION.md`
  Authoring gate 段落——产品侧只剩「每 run 记一行」——+ `CONSTRUCTION-LEDGER.md` 的
  conversation-only 行，现为三分支与读数归属的唯一的家）
- 裁决：C4 `O-1`（2026-08-01）的两 map 分类对照义务**不退役、也不无限收集**——每真 run 的
  review/closeout 照记一行（paragraph map 对 unit map 的分类对照，点名谁或哪个 session 填的；
  同源填写不独立、不入样本），**产品 run 的义务到此为止**。读全已收行、按原三分支改判——分歧恒零
  或恒 paragraph 侧对 → 议 (c) 段落诞生义务；恒 unit 侧对 → 议 classification 列去留；两侧各有
  贡献 → 转常设——是**构造轮**的活，不再挂在「下一个产品 run 的 closeout」上：产品 run 既不执行
  它也不等它，收集不因它未做而停。读数前该记录义务作为 standing run-conduct 住执行者 charter
  （`EXECUTION.md`），不再靠指令 Context 手抄（它为此手抄了五个 run）。用户的范畴框架保留：仪器
  把自己的研究记账挂到被测工作指令面上这件事，以「给研究一个 charter 之家 + 一个到期日」作答，
  不以留在 Context 作答；本条改的只是那个到期日由谁走到，不是有没有到期日。
- 本条对 `HD-54` 的收窄**只有读数时刻归属一处**，其余全文承接：记录义务的形状与措辞、三分支的
  内容、两处载体、one-shot 的消耗条件（读数发生并改判即 retire）均不变。
- basis: 用户裁决 2026-08-25（批 `CORE-SET` 的第 4 条裁决，载体
  `document-harness/plans/core-set.plan.md`）· `HD-30` 部分收窄机制 · supersedes `HD-54`

### HD-57 · `E2` 冻结面陈旧字面五处：recorded ruling，准予更正
- 2026-08-23 · user · scope: standing · status: **implemented**（应用批 2026-08-23 落地——五站点
  同 commit 写入、四 rider 行同 commit 兑付删行、`E2` 条款的 v4 blob 字面量同 commit 更新为
  `dfc983d2…`；本条即 `HD-20` 所要求的那个 recorded ruling，建条与挪节同日，挪节与状态翻转
  同 commit 按 `HD-2`）
- 裁决：用户裁「可以改」——以下五处「签署/冻结时为真、后续裁决后变陈旧」的字面，准予在
  `E2`/`HD-20` 意义下写入更正，一次裁决盖五处：① contract v4 §5 Verification-mode 行的
  `local_check_and_review`（single home 自 SIMP-A1 起两值；`v3-cold-read-cf54a79.md` `L-1`
  供字节）② v4 `:34-36` plan digest 句补「digest 绑 caller-era 签署字节」的 provenance 说明
  （同 read `L-2`）③④ `document-work-spec.schema.json` 与 `document-work-spec.v2.schema.json`
  的 title「sole owner: stage author / planning agent」按 v4 §3 的 executor 读法改写（rider
  `wspec-owner`）⑤ `harness-issue.schema.json:45` `observed_after` description 第二句改严读法
  （rider `hi-schema-gloss`，字节在 `v3-review-verify-860729f.md` `V-1`）。
- 后果：应用批排在轮 `STRANGER-GUARDS` closeout 之后独立落；四 rider 行（`v4-verifmode` /
  `v4-plan-digest` / `wspec-owner` / `hi-schema-gloss`）同 commit 兑付删行；`E2` 条款的 v4
  blob 字面量同 commit 更新；v4 与 checklist 的成员编辑欠独立 read，随下一轮开轮冷读。
  `HD-56` 签字绑定的原 blob `614932de…` 留档为签署对象不变；更正后的 v4 blob＝`dfc983d2…`
  （staged blob，应用批 commit 可核）。
- basis: 用户裁决 2026-08-23（对话「5 可以改」）· plan
  `document-harness/plans/stranger-guards.plan.md` fix-gate 节 ruling 5 ·
  `v3-cold-read-cf54a79.md` `L-1`/`L-2` · riders `wspec-owner`/`hi-schema-gloss`

### HD-55 · executor 与 orchestrator 自此为独立 session；单 session 兼任不再是常规形态
- 2026-08-22 · user · scope: standing · status: **implemented**（轮 `PRERUN-RIDERS` 落 carrier，
  三站同 commit——**home** ＝ `ORCHESTRATION.md` 三角色表下新增的一句「Independent is the norm; one
  session holding both work-side roles is the exception」，该表的主题就是 role→session 指派，故
  归它 · `E1` 中间态披露句改写为**例外通道**（披露机制一字未改，只按本条把适用面收窄为例外）·
  `ORCHESTRATION.md` *What the orchestrator may never do* 首条指路句随改，不再把兼任写成常规。
  第三站由开轮 cold read `v3-cold-read-3a6a10b.md` 的 `O-1` 补上——本条原 status 行只点了两站；
  `HD-41` ④ 的扫类输出见 carrier commit 正文。挪节与状态翻转同 commit，按 `HD-2`）
- 裁决：executor 与 orchestrator 是**独立 session**，产品 run 与构造轮同一形式——orchestrator
  跑 `dtw dispatch --executor`（产品侧）/ `--construction-executor`（构造侧）派发**冷启动**的
  executor，executor 的输入＝派发文档所载（charter 指针 + run 事实），不携带 orchestrator 的
  会话上下文。理由（用户原话的实质）：两个角色行为不同，需要看见的 context 也理所当然不同——
  role 之分若不带 context 之分，就只是称呼。
- 后果：`R1` 四持有在正常派发下天然分离，review dispatch 的独立性不再靠单 session 对自己的
  纪律；`ORCHESTRATION.md` 上报路由（executor → orchestrator → 用户）按原文可走通；`E1` 中间态
  披露句降为**例外通道**——真发生兼任时照旧披露持有项，但兼任自此是偏离、须在轮记录里说明缘由
  （`HD-46` 的披露规则本身不变，本条只收窄其适用面为例外，不 supersede）。rider
  `one-session-roles` 之答即本条，行按其自载兑付条件同 commit 删除；其记的两处文本失配在独立
  形态下不再咬人，剩余「层内落一句」由本条 status 行追踪。冷启动路径已实测（2026-08-22，
  scratchpad 一次性调用者仓）：`dispatch --executor` 派发单正确（charter 经挂载点解析）、字节
  漂移四类拒绝之一实测生效；`claude -p` 冷启动探针第一动作读 charter、自行复核冻结 commit 与
  派发单、25 轮零越权写入——实测记录只活在本对话，照记天花板（`R2`：chat-only 载重材料）。
- basis: 用户裁决 2026-08-22（对话：「我倾向独立跑。如果能分出 executor 和 orchestrator 两个
  role，就说明他们有不一样的行为，需要看见的 context 也理所当然的不一样」+「现在把这个落了。
  之后 executor 和 orchestrator 就是独立的」）· rider `one-session-roles`（FULL
  `v3-review-full-83e3191.md` `O-3` · VERIFY `v3-review-verify-627df95.md` `V-3`，其 deadline
  ＝本裁决，同 commit 兑付删行）· `HD-53`（两个执行者派发模式，本条的机制承载）· `HD-46`
  中间态 tiebreak（适用面被本条收窄）· carrier ＝轮 `PRERUN-RIDERS`（本条 status 行三站）

### HD-53 · `dtw dispatch` 收两个执行者模式；产品侧 charter=`EXECUTION.md`、构造侧=`CONSTRUCTION-CHECKLIST.md`
- 2026-08-22 · user · scope: standing · status: **implemented**（承载随轮 `EXECUTOR-CHARTER`
  candidate `229f03f` 落地：`dispatch.py` 第四 dispatch family 两常量两 prompt + `cli.py` 两模式
  接线 + golden 整文档等式测试；条目按 `HD-51` 先例于 closeout 建）
- 裁决：① 产品侧执行者模式发三件且仅三件——run id、冻结指令的 path 与 revision、charter 指针
  `document-harness/EXECUTION.md`；不枚举「查什么」（shadow-WorkSpec 拒绝对执行者派发同样成立；
  派发时点=START，WorkSpec 由执行者事后起草（`HD-35`），故亦无他物可派生）。② 构造侧模式发一句
  ——charter 指针 `document-harness/CONSTRUCTION-CHECKLIST.md`（其 *Execution side* 标题本就点名
  绑定该角色）、零推导（构造轮无 control plane；手喂轮名与边界即重造本模块要废除之物）。③ 两
  模式均不写 freeze marker——那是 `E9` 评审窗口，executor 派发启动的正是窗口要冻的工作。随其
  落地，`EXECUTION.md` 的「Context 引用」写作规则删除（部分 supersede p4-bridge f1 的
  2026-08-01 路由裁决，替换文本内命名；`ORCHESTRATOR-CHARTER` 轮未答问题①就此关闭）。
- basis: 用户裁决 2026-08-22（对话 + plan `document-harness/plans/executor-charter.plan.md`
  §四条用户裁决为其载体）· 先例 `HD-47`/`HD-51`（命令面按案裁决）· candidate `229f03f` ·
  FULL `v3-review-full-229f03f.md`

### HD-52 · START 卡由脚本渲染这条裁决**对所有 run 都算**，不限编号态；`HD-51` 的范围澄清
- 2026-08-22 · user · scope: standing · status: **implemented**（转条件「一个轮次把那句话移出编号态
  范围、或补一句盖住散文态」已由轮 `EXECUTOR-CHARTER` 满足：`EXECUTION.md` 把「Since round
  PREVIEW-RENDER…」句从 SIMP-C4 bullet 内移出，立为形态之上的独立段落（"However the form
  resolves, the START card of every product run is rendered by `dtw preview` …"），随该轮
  candidate 落地、状态同 commit 翻（`HD-2`）；rider `startcard-form` 同 commit 兑付删行）
- 裁决：`HD-51` 记的「产品 run 的授权本体＝冻结的 control plane，其人类可读渲染由 `dtw preview`
  确定性产出」**适用于每一个产品 run**，与指令取编号态还是散文态无关。
- 判据（用户 2026-08-22 提出，实测后据以裁定）：**散文态本来就能脚本渲染**。`preview.py:178,182`
  读 `declared_form` 后照常渲染，无声明就打印 `form: (undeclared)`；全文唯一的拒绝在 `:120`，
  条件是控制面缺文件，与形态无关。既然脚本不挑形态，把裁决限缩到编号态就没有依据。
- 后果：散文态 run 的 orchestrator 不再是「持着 `ORCHESTRATION.md:58` 的出卡义务却无处可指」。
  这一半尤其要紧，因为散文态是那一节自陈的**默认与兜底**——声明了编号态而结构不符的 run 会落回
  散文态，恰在其指令最不可信的时刻。
- basis: 用户裁决 2026-08-22（对话）· cold read `v3-cold-read-39e395e.md` `L-1` 提出两读法并按
  `R5` 归口用户 · 轮 `TEMPLATE-LIB-ROOT` 的 journal 收批段 · 先例 `HD-47`（命令面的按案裁决）·
  承载 = 轮 `EXECUTOR-CHARTER` candidate 的 `EXECUTION.md` 独立段落

### HD-51 · `dtw preview` 立为第八个命令；产品 run 的 START 卡由其从冻结 control plane 确定性渲染
- 2026-08-21 · user · scope: standing · status: **implemented**（承载与建条同批：`cli.py` 第八命令 +
  `test_cli_entry.py` OPERATIONS + `EXECUTION.md` SIMP-C4 接线句，随轮 `PREVIEW-RENDER` candidate
  `57d1312` 落地；条目按该轮 FULL `v3-review-full-57d1312.md` `L-3` 建——裁决此前只活在 commit 正文，
  先例 `HD-47` 自己的 `basis` 记过同一形状的代价）
- 裁决：① `dtw` 可以有第八个命令 `preview`——从产品 run 的冻结 control plane（instruction + WorkSpec +
  check specs + resolved plan + audit）确定性渲染 START 前的人类可读预览，不经 LLM、可随时重推导故
  不另存渲染产物（`E11` 载体裁决「脚本化立项」半边的兑现）。② `EXECUTION.md` SIMP-C4 段接线：START
  卡由该脚本渲染。命令面自此为八；增减命令仍按 `HD-47` 逐案归用户。
- 轮内小裁决不入册（构造轮无 user-decision 载体，按 `E11` 载体裁决活在 commit 正文与 journal）：
  修腿边界「全包」· boundary 计数「删」· catch-all「不加」——见 journal
  `document-harness/journal/preview-render-2026-08-21.md`。
- basis: 用户裁决 2026-08-21（对话，选择卡）· candidate `57d1312` · FULL `v3-review-full-57d1312.md`
  `L-3` · 轮 journal 同上

### HD-49 · 新仓成员（`HD-28` 的再后继）：仪器开发史归仪器仓；调用者只留自己的账
- 2026-08-19 · user · scope: standing · status: **implemented**（轮 `LEDGER-SPLIT` 执行完毕；条目挪入本节 2026-08-21，用户裁「挪吧」——建条时按当时惯例留在 §live，cold read `17ce3ed` `O-1` 指出与状态机不符：
  `CONSTRUCTION-LEDGER.md` + archive + `document-harness/plans/` 16 件落 `acbc553`/`b5fd58b`，
  调用者账瘦身至 57 行落 `e74be07`/`8f1ad1d`，三腿 FULL→修→VERIFY `REVIEWED_NO_BLOCKER` 走满；
  本条按 `HD-30` 机制为 `HD-28` 的**完整后继**，`HD-28` 同 commit 转 superseded 入 archive，双向指针）
- 裁决：新 harness 仓带 **A 仪器 + B 治理登记（decisions / riders / decisions-archive，3 files）+
  C 构造评审记录 + D（本条新增）仪器自身的开发账**——`CONSTRUCTION-LEDGER.md`、其 archive、与驱动
  构造批的 plans（现 16 件，住 `document-harness/plans/`）。判据从「谁的开发」细化为 **(a)/(b) 切**
  （用户 2026-08-19）：(a) 仪器自身开发史（轮次台账、CLOSED roll、构造裁决、构造 plan）归仪器仓；
  (b) 调用者作为使用者的账（收批义务、ledger 参数、机器接线、router 状态）留调用者。**产品 run 的
  记录与产物仍留调用者**（承 `HD-28`——记录跟着被记录的对象走：产品 run 的对象是调用者的树）；
  **已关闭 run 的产物与 shadow 留产品仓**（承 `HD-16` 原文不变）。`HD-28` 的「ledger 留调用者」
  半边就此被推翻——那半边把「仪器的开发账」与「调用者的使用账」混作一种 ledger，(a)/(b) 切是其修正；
  ledger 的**规则**归属不变（global 约定的收紧方言仍是调用者的，`ledger_cap_check.py` 仍只钉调用者那份）。
- 例外照记：`SPLIT-COPY-RETIRE` 的 FULL 与 VERIFY（`v3-review-full-2d148f3` / `v3-review-verify-bef77f3`）
  虽属构造记录，但该轮 subject 是调用者的树，留调用者——`LEDGER-SPLIT` 的 executor 与 FULL 均按此报告，
  处置归本条。
- basis: 用户裁决 2026-08-19（对话，「按 (a)/(b) 切」，推翻 `HD-28` ledger 半边亦经其明示确认）·
  轮 `LEDGER-SPLIT`（分类清单在 executor 报告，`v3-review-full-e74be07.md` 复核）· supersedes `HD-28`

### HD-47 · `dtw init` 立为第七个命令；`split-design` §1 的「六命令原样」是搬迁指令、不是命令数上限
- 2026-08-18 · user · scope: standing · status: **implemented**（转条件「一个设计轮把命令面的增删判据写进指令层」
  已由轮 `INIT-SURFACE`（2026-08-20/21）满足：判据落 `document-harness/README.md` onboarding 行
  （candidate `7f6e7f0`、量词修正 `84dea06`）——树里那半接线可进 `init`、机器那半不进；`--into`
  处置同行承载（不加选项、根目录 default 非 requirement、挪位走 `HD-34` 通道），`HD-48` ③ 就此
  了结。`split-design` §1 未重签，仍按本条读法读）
- 裁决：`dtw` 可以有第七个命令 `init`，承担新调用者 onboarding 的**机械那半**。`split-design.md` §1 的
  「v3 命令组整块搬新仓……六命令原样」是**搬迁时不得顺手改设计**的指令，**不是**对命令数的永久上限；
  今后增不增命令按 `R5` 逐案归用户，一次「不加」不锁死下一次。
- 与 `RA` 的关系：**不推翻、不消耗**。`RA` 问的是「把 run 目录里的机检引擎接上 CLI」，用户判为便利性
  而非正确性、明写「不为此推翻 §1」；本条问的是「新调用者怎么把仪器装起来」——不同的案子、不同的答案。
  `RA` 行的 redeem-when 一个字未动，只加了一句指向本条的指针。
- 后果：`init` 只做机械的四件（建 `.harness/` · 追 gitignore 条目 · 逐字节拷两个模板 · 逐文件拒绝覆盖），
  并打印它**故意不做**的五件；判断性的那些留在 `document-harness/ONBOARDING.md` 由人做。命令面自此为七，
  `cli.py` 的操作枚举与 `test_cli_entry.py` 的手写 `OPERATIONS` 元组同步。
- basis: 用户裁决 **2026-08-18**（对话；三形态里取「甲 + 给 `dtw` 加 `init`」）。**日期只能从对话核，仓里查不到**
  ——本条初稿写 2026-08-19，与同轮 `cli.py:8`、轮 journal `:44` 的 08-18 相抵，由 VERIFY `v3-review-verify-4029b43.md`
  `V-1` 点出、用户 2026-08-19 裁作记录更正改回。这个天花板照记（`R2`：只活在对话里的载重材料是 finding）：
  08-18 之所以为准，是因为本轮 instruction（写于当日）即以该日期陈述该裁决，两个 08-18 站点都由它派生· 轮 `CALLER-ONBOARDING`
  的候选 `2026a14` · 其 FULL `v3-review-full-2026a14.md` `L-3`（指出该裁决当时只活在 commit 正文里、
  与已签文本相抵，本条即其答案）· `document-harness/split-design.md` §1 · rider `RA` ·
  用户裁决 2026-08-20/21（三选卡：不加 `--into`、判据与分工 home 均落治理层 README；
  次日「确认是治理层的readme」；轮 `INIT-SURFACE`）

### HD-46 · orchestrator charter 立为第十成员；charter 走收窄形（九条只指路）；`E1` 充分条件句按 `R1` 重写
- 2026-08-18 · user · scope: standing · status: **implemented**（承载三处，同 commit：新成员
  `ResearchSystem/document-harness/ORCHESTRATION.md` · `E10` 成员句「exactly these ten paths」·
  `E1` 重写句。初始态即 implemented，形状比照 `HD-30`/`HD-45`——承载与建条同一个 commit）
- 裁决：① orchestrator 的角色说明书**立为指令层第十成员**。② 它走**收窄形**：已在层里的九条义务
  只点名归属并指向规则 id（`E9`/`E10`/`E11`/`E12`/`R5`/`R6`/`R10`，另加住在决策簿的 `HD-2`），
  **不复述条文**；写正文的只有三角色模型本身与三条层内零承载的义务——交付 instruction、读调用者
  策略文件、executor 上报回程。依据：`E10` 明写成员编辑 never re-typed "with the same content"，
  `HD-5` 判转录为漂移面，抄九条即造第二份会漂的拷贝。③ `E1` 的「orchestrator 派发即独立」由**充分
  条件**改为**必要非充分**，判定交回 `R1` 的四项持有（dispatched / prompted / scoped / reported）。
- **`HD-21` 的提问义务，此处即问与答**：ORCHESTRATION.md **算成员**——它对 orchestrator 的义务有
  权威，故按 `HD-21` 必须由成员句点名，本轮点名了；`E10-sync` 的三处（成员句 / `LAYER` /
  `EXPECTED`）同 commit 同改。
- **本条留下的 tiebreak，如实记**：`R1` 同时含「四项全归 executor＝自检」与「executor 一项不占＝
  结构性独立」两句，中间态两句都不管。重写取的读法是：**全占＝失格 · 一项不占＝结构性独立 ·
  中间态＝独立但该轮在记录里写明 executor 占了哪几项，且不得自称结构性独立**。这条中间态处置是
  本轮新加的 bound（rider `E1-suff` 明写任何限定词都是 design），随本轮设计轮落地；它直接作用于
  当时的实际形态——一个 session 同时持 orchestrator 与 executor 两个角色——该形态自
  `HD-55`（2026-08-22）起不再是常规，只余 `E1` 的例外通道。同句另把「一个 session
  一辈子一个角色」重述为**work side / review side 之分**，与 `Execution side` 节头「whether it
  orchestrates the round or executes it」一致，消掉字面读法下每一轮都违规的矛盾。
- 后果：rider `E1-suff` 兑付删行；`E10-sync` 按 `HD-22` 不删行、deadline 顺延。`HD-19`（决策簿不进
  `E10`，必读义务写在 charter 里）**不受影响**：那里的 charter 指 `CONSTRUCTION-CHECKLIST.md`，
  必读义务仍写在其 `E10` 里，本轮新文件不接手该义务、只在自己的表里指向它。
- basis: 用户裁决 2026-08-18（对话，预览卡两问）· rider `E1-suff`（`v3-checkpoint-read-be9878a.md`
  `L-1`）· `document-harness/io-design.md` §2/§3（设计来源，本身非成员、对规则无权威）

### HD-45 · 全档电池按仓分档：六条不减、各归其主体所在的树；例外句按子句读；revert anchor 写明价钱
- 2026-08-18 · user · scope: standing · status: **implemented**（承载 = `EXECUTION.md` 的
  Regression-battery tiering 节，同 commit：分仓两条子项 + 「addresses the enumeration; it does
  not shorten it」句 + 例外句的 path-not-prose 改写 + revert note 的价钱段。**初始状态即
  implemented**，形状比照 `HD-30`——承载与建条同一个 commit，不是 session 事后翻态）
- 裁决：① 全档电池仍是**六条、nothing fewer**，但**按被验证的那个仓分档**——仪器仓一条
  （`python -m pytest -q`，从 `ResearchSystem/tooling` 跑），调用者仓五条（三个 runner +
  fixtures 校验 + `compile --check`）；**主体不在被验证仓里的命令在那里不欠**，且验证记录写明
  跑在哪个仓。② doc-only 例外句**按子句读**：代码与测试钉住的是那些 doc 文件的**路径**，故增删
  或改名这些路径算 tooling-touching，而只改内容、路径不动仍算 doc-only。③ tiering 节头的
  revert anchor **保留但写明价钱**：`HD-14` 把该节搬进指令层之后，行使它是 `E10` 下的设计轮而
  非一次 revert，2026-08-03 裁决隐含的「随时可撤」条件已不存在。
- 判据（实测 2026-08-18，量程＝两棵树上六条腿各跑一次）：仪器仓 `pytest` 712 passed / 92.87s，
  另五个脚本在该仓**根本不存在**；调用者仓五条全绿（29 / 80 / 39 tests · 58 cases · exit 0），
  而 `pytest` 在那里收 `no tests ran`。故拆分之后那份单一清单**两个仓都满足不了**——五条腿测的
  是产品编译器与 schema，不是仪器。
- 后果：`HD-42` ①「不建立『主体消失即可改枚举』的通则」**未被动用**——本条一条都不删，只指明各条
  归哪棵树，两处 `nothing fewer` 保留。真正放弃的是构造轮从另一仓的腿上白拿的附带覆盖，照记。
  riders `battery-travel` / `tier-file-vs-clause` / `tier-scope` 三行随本 commit 兑付删除。
  按 `HD-42` 未豁免的那半同样适用：本轮对 `E10` 成员的写入仍欠该层一次独立 read。
- basis: 用户裁决 2026-08-18（对话，预览卡三问）· rider `battery-travel`（`v3-review-full-297bb2b.md`
  `O-2`）· rider `tier-file-vs-clause`（`v3-review-full-418b89c.md` `L-2`+`O-1`）· rider
  `tier-scope` ②（`v3-review-verify-fbcb035.md` `V-1`）

### HD-40 · split-design v1 已签字：拆分批 R1–R4 的执行依据
- 2026-08-14 · user · scope: standing · status: **implemented**（拆分批 R1–R4 于 2026-08-17
  整批 CLOSED，本条所绑的十节执行义务至此清空——`R5` 归口的两条 rider（`RA` / `PD`）在 R4 收批
  时各自重定范围而非兑付，属 bank 的事、不再是本条的。本条即签字记录本身——`split-design.md`
  按 governance-scan 判据不携带自身审批状态，签字住这里，形状比照 `HD-35`）
- 裁决：用户签署 `document-harness/split-design.md` **v1 定稿**（八问全裁 + §1–§9 与 §10 对齐的
  一致性 pass，`9736670`；签字绑定字节 blob `3f4d2b0a`、sha256 `c4e24f99…ab5c`，251 行）。
  **绑定原文恢复（re-read `O-1`）**：源 read 的 `L-2` 明写「签字是用户的行为，替换归用户」，
  而本 session 曾把 `sha256` 从绑定句里移走——越权，初签绑定原字节留档如上。
- **重签 2026-08-15（`HD-40` 的第二次签字）**：初签后经**五轮独立 read**（记录 `feb7b48` ·
  `6a946ba` · `4342c6b` · `289f8ab` · `72694c4`，共返七条 must-fix）与其全部答复，稿由 251 行
  增至 **352 行**（新增 §11 量程纪律一整节，及各节的更正块）。**八条裁决自初签起逐字节未变**
  （§10 表 `git show 3f4d2b0a` vs tip，diff 为空）；变的是影响面与写法。
  **重签绑定 blob `3140faf1`、sha256 `1108574f…c033`（blob 内容，LF——按 `HD-41` 的口径，
  `git cat-file blob <id> | sha256sum`），352 行**；初签 `3f4d2b0a` / `8da2d17d…59af` / 251 行留档。
- **重签时仍开着的三件**（不阻塞 R1，记明以免被读成已闭）：① 新仓 remote 由用户自建
  ② R1 动手前确认删除范围的净增 32 件 ③ **`ddd773a` 欠一次独立 re-read**——它是 `72694c4` 的
  `M-2` 答复，按 `E10` must-fix 通道欠对被改文本的独立复核；R1 开轮前付清，或用户明示豁免。
  **`sha256` 口径更正（R0 read `L-2`）**：初记的 `c4e24f99…ab5c` 是**工作副本**的摘要，本机
  `core.autocrlf=true` 故每行多一个 CR；**blob 内容（LF）的 sha256 是 `8da2d17d…59af`**。
  今后一律记 blob 内容的摘要——`git cat-file blob <id> | sha256sum`；工作副本摘要在别人的 clone
  上（`core.autocrlf=false`）算不出来，会把好签字读成坏的。`HD-35` 未暴露此坑纯属侥幸：
  **`io-design.md` 的工作副本恰好也是 LF**（写入即 LF、从未被 checkout 重新落盘），故其工作副本
  摘要与 blob 摘要重合；**仓内 blob 一律 LF**，`E2` 三份冻结件亦然（re-read `L-1` 更正本句原写的
  「blob 恰好存的就是 CRLF」——那是反的，且会教读者用错模型验签）。
  十节全部生效为设计依据：R1 按 §3/§4/§7 施工、R2 按 §1 施工、R3 按 §2/§6/§8 施工、
  打包批按 §10.5 立项。
- 后果：R0 的步骤 8 完成，只余步骤 9（独立 read）。对该文件的后续实质修改欠重签。
  **签字时仍开着的两件**（均不阻塞 R1，记明以免被读成已闭）：① 新仓 remote 由用户自建；
  ② 删除范围 **139→171** 的差额欠 R1 动手前的最后确认——用户的「删」是对 139 口径给的，
  32 件的补测发生在其后（`HD-39` 与 §7 均已照记）。
- **重签 2026-08-23（第三次，轮 `CONTRACT-V4`，随 `HD-56` 签字一并）**：除锈两处重签标记——
  §1 六命令句的读法注（`HD-47`/`HD-51`，rider `six-signed` 本文件半边兑付）+ §2 EXCLUDE 提议的
  未走路标（rider `design-route` 兑付）。重签绑定 blob `a078ea31…`、sha256 `fb9e6822…5332`
  （blob 内容，LF），358 行；前签 `3140faf1` 留档。
- basis: 用户签字 2026-08-14（对话）· `document-harness/split-design.md` @ `3f4d2b0a`


### HD-33 · 调用模型 = submodule；run 与实例文件归调用者仓（`HD-29` 拆分后继 ①）
- 2026-08-12 · user · scope: standing · status: **implemented**（拆分批 R3 执行完毕 2026-08-17：
  gitlink 已挂 `ResearchSystem/harness`，run 目录 / freeze marker / 四件实例文件均在调用者仓原位）
- 裁决：调用者仓以 gitlink 钉住 harness 版本（`HD-15` 拆分形态在调用侧的兑现）；run 目录
  （可 gitignore）、freeze marker（`.harness/review-pending.json`）、四件实例文件（decision
  log / rider bank / journal / ledger）**全归调用者仓**。ledger 跨仓指针问题不存在——每库用
  自己的四件。
- 后果：「用哪个版本的仪器查的」由候选 commit 自带（copy 守不住的那条线）；升级 = 显式的
  gitlink 指针变更 commit，历史可读。
- basis: journal §5 · `document-harness/io-design.md` §7 · 用户裁决 2026-08-12 ·
  supersedes `HD-29`（与 `HD-34` 共同取代）

### HD-15 · 拆分形态 = submodule（批 A `D5`）
- 2026-08-08 · user · scope: standing · status: **implemented**（形态已兑现：`.gitmodules` +
  gitlink `ResearchSystem/harness`，拆分批 R3 2026-08-17）
- 裁决：harness 独立成仓，产品仓以 **submodule** 钉住其版本。
- 后果：保障要求「用哪个版本的仪器查的」可复现，submodule 指针恰好把仪器版本钉进候选 commit。
  **A1 的未量项因此转为 A2 必量**：两仓下 `subject_tree: candidate_commit` 出现第二个 revision
  的具体语义。`rsc.py` 的两条入边（`rsclib.document_harness` + `.review`）与
  `hooks/candidate_path_check.py` 的一条须一并处置。
- basis: [journal/batch-a1-2026-08-08.md](document-harness/journal/batch-a1-2026-08-08.md) §13.2–13.3

### HD-10 · harness 独立成仓的目的与必要性
- 2026-08-08 · user · scope: standing · status: **implemented**（拆分已执行：新仓
  `Melclycj/do-the-work` 存在，产品仓以 gitlink 钉住，拆分批 R3 2026-08-17）
- 裁决：**harness 不依附于 ResearchSystem 存在**，因此从本仓拆出为独立 repo **必须做**。
- 后果：批 A 的 `D5` 由「拆不拆 / 哪个方案」收窄为「切线与成员」。**A1 的 M5/M6 costed 的是另一条
  切线**（`ResearchSystem/` 整体离开论文仓），其「(b) 是全部代价、`generated/` 362 处」结论**不适用
  本切线**——`generated/` 属产品侧、不随 harness 走。按本切线重算见 basis。
- basis: [journal/batch-a1-2026-08-08.md](document-harness/journal/batch-a1-2026-08-08.md) §13


### HD-38 · 自由通道字节自带 commit：不搭 amendment 的车（`L-1` 的用户裁决）
- 2026-08-13 · user · scope: standing · status: implemented（承载 =
  `CONSTRUCTION-CHECKLIST.md` `R10` 的「an `E10` amendment commit admits only the answers
  to a read's must-fix findings」——**该句不改，正是本裁决选择的那一边**。**偏差照记**：本条的
  `implemented` 由 session 自定而非用户翻，违 `HD-2`；用户 2026-08-13 preclear **追认**）
- 裁决：`v3-checkpoint-read-f61ce2c.md` `L-1` 摆出的二选一里，**行为让步而非文本让步**——
  `R10` 原句站住；今后自由通道字节（供了字节的 low / observation / wording-level）**单独一个
  commit**，不与 must-fix 的答复混装。
- 后果：`E9` 预算的可核性不再依赖 commit 正文的自愿归属（这也是 2026-08-13 裁「#2 声明扫类
  不做」为何仍站得住的原因——diff 层面就分得开）。**已落地的三个混装 commit 照记不回改**：
  `b9e6fd8`（`M-1`×2 + `W-1`）· `8884f47`（`M-1` 删除 + `W-1`/`W-2`）· `f61ce2c`
  （`M-1` 替换 + `W-1`），三者均在本裁决之前，属已知不符的历史。
- basis: 用户裁决 2026-08-13（对话）· `v3-checkpoint-read-f61ce2c.md` `L-1`（读者明言
  `R5`：哪一边让步不由他定）

### HD-37 · `R10` rider 到期判据：deadline 不得指向本轮；design 形状的只搭有资格开轮的批
- 2026-08-13 · user · scope: standing · status: implemented（2026-08-13，用户于 R5 收批时翻；
  承载 = `CONSTRUCTION-CHECKLIST.md` `R10` rider 格式段的两句新条款——① 在「deadline …
  never inside the round that writes the row」· ② 在「A rider whose fix is design … names a
  redeem-when surface that may open one, never any batch」。**偏差照记**（`HD-2` 要求挪节与实现
  同 commit）：实现在 `136f27f`（`W-1` 的理由句于 `f61ce2c` 更正），本挪节晚三个 commit，
  与 `HD-25`/`HD-32` 同形）
- 裁决：① rider 的 deadline **不得指向创造该行的那一轮**——出生即到期的 deadline 是 malformed。
  ② 修法为 **design 形状**的 rider，其 redeem-when 必须点名**有资格开轮**的表面，不得点名任意批；
  这类 rider 搭**下一个有资格开轮的批**。**③ 只管今后写的行，旧行不回溯**（用户 2026-08-13
  preclear；比照 `HD-8` 历史不迁）——故 `E1-suff`/`wspec-owner`/`frozen-path-prefix` 三行的
  「下一批碰 X」照旧合法。唯一已适配的旧行是 `tier-file-vs-clause`，因它是 `O-4` 的动机实例、
  随本裁决同批重写。
- 后果：`E10` amendment commit 能满足这类行的 touch condition 却结构上无法兑付，该缺口关闭。
  rider `tier-file-vs-clause` 的 redeem-when 已随 R5 按新判据重写（重定范围非兑付，行不删，
  比照 `HD-22`/`HD-27`）；`wl-route` 是**第一条按本判据撰写**的新行。**未解决且如实记**：兑付窗口
  仍窄——一轮里能兑付 design 形状 rider 的通常只有轮首那个候选 commit，而 rider 可在轮中途诞生
  （R4 实例）；本裁决选的是「接受晚一轮」，不给 `R10` 加 closeout 载体（那会让规则字节在无独立
  评审下落地）。
- basis: 用户裁决 2026-08-13（对话，(iv)+(ii)）· `v3-checkpoint-read-8884f47.md` `O-4`
  （`tier-file-vs-clause` 在 R4 的 amendment commit 上到期而无人有资格动）·
  `v3-checkpoint-read-f61ce2c.md` `O-4`（承载已落在 status 行点名的位置）

### HD-32 · 「这轮的结论」= 命令输出，不落盘
- 2026-08-12 · user · scope: standing · status: implemented（2026-08-13，用户 preclear 裁；
  承载两处 = `document-harness/io-design.md` §5（已签字，`HD-35`）+ `ResearchSystem/HARNESS-POLICY.md`
  §1（批 B R3 落笔、修腿 L-2 补全命令面）。**前瞻半边**——单一 conclude 命令随独立 CLI 归拆分批
  ——承载于 io-design §7 与 rider `CLI-hist`。**偏差照记**（`HD-2` 要求挪节与实现同 commit）：
  两个承载分别成于 `790e06e`（R2）与 `080621a`（R3 修腿），本挪节晚于二者，与 `HD-25` 同形）
- 裁决：harness 对外的「这轮的结论」以**命令输出**交付（现可当结论出口用的三命令 `status` /
  `flow` / `disposition`），**不建落盘结论文件**；优先满足现有流程。
- basis: 用户裁决 2026-08-12（对话）· `document-harness/io-design.md` §5 · R2 转录核查 finding 9

### HD-31 · 记账保障承接物移调用者侧（`HD-26` 的收窄后继）
- 2026-08-12 · user · scope: standing · status: implemented（2026-08-12，批 B R3 落地同
  commit；承载 = `ledger_cap_check.py` 移至 `Thesis/Work/Tooling/` + `dispatch.py`
  READ_PROMPT 删 ledger 半句（fixture 同步）+ `ResearchSystem/HARNESS-POLICY.md` §4 的
  承接声明（本机选择 = 不设机器，纪律承接）+ README.md Local-enforcement 行减法。已关闭
  run 的 `write_scope`/`chk-ledger-note` 不回改——依据 `HD-25` 的「现存八个已关闭 run
  不回改」条款（R3 修腿更正：此处原引 `HD-28`，但 `HD-28` 管归仓不管改动，FULL `c7e0ba0`
  L-3）；「今后 run 不得绑 ledger」的规则文本归 R4）
- 裁决：harness **只输出、不写入**任何外部账本（承 `HD-26`）；「citation 规则作废」半边亦承
  原文不变。**收窄的是硬约束半边**：`chk-ledger-note` 类检查拆除后，「这轮该记的事真记下来了」
  的保障**由调用者侧自选机制承接**（调用者策略段可声明锚点断言，进调用者自己的 pre-commit/CI）
  ——不再要求 harness 内有承接物；承接物存在与否是调用者的选择。
- 后果：R3 拆四处耦合（`ledger_cap_check.py` 钉 `HARNESS-LEDGER.md` 的读 · `dispatch.py:636`
  提示词 · run `write_scope` 列 ledger 路径 · `chk-ledger-note` 锚 `.goals/LEDGER.md` 散文）时
  不欠 harness 侧替代检查。
- basis: 用户裁决 2026-08-11/12（对话，io-design §5 定稿讨论）· R2 转录核查 finding 2 ·
  supersedes `HD-26`

### HD-30 · 部分收窄机制：四态维持，后继承载全文、原条 superseded
- 2026-08-12 · user · scope: standing · status: implemented（本文件头部状态机句承载，同 commit）
- 裁决：不设第五态。一条裁决被部分收窄时，**新建后继条目承载收窄后的全文**，原条目**整条转
  `superseded`**（双向指针、同 commit 入 archive）；「同一主题至多一条 live」由此保持。
- 起因：`HD-28`（原为差量式收窄注）与 `HD-16` 同主题双 live，四态机无此形状——第一例 decision
  收窄 decision（此前重定范围先例 `HD-22`/`HD-27` 均作用于 rider 行，非 decision 条目）。
- basis: 用户裁决 2026-08-12（对话）· R2 转录核查 finding 22

### HD-25 · `run_all` 接线，切面 = 只改模板（批 B ①）
- 2026-08-11 · user · scope: standing · status: implemented（2026-08-12，R1 closeout；承载 =
  `assurance/templates/run-v2/run_evidence_v2.py:176-205` 的接线与其八行原因注释 +
  `tooling/tests/document_harness_review/test_run_v2_template_check_order.py` 的八条守卫。
  **偏差照记**：`HD-2` 要求 live→implemented 的挪节与实现它的 commit 同一个，实现在 `e9166d2`
  而本挪节落在 closeout，晚了四个 commit；用户 2026-08-12 裁定照此收口并记录偏差）
- 裁决：把 `run_all`（`checks.py:452`）接进产品路径，切面**只改 `assurance/templates/run-v2/`**；
  现存八个已关闭 run 不回改。
- 后果：接线把顺序源从 `sorted(glob(…))` 换成 plan 的 `check_order`，故 plan 点名之外的 check 文件
  不再跑、plan 点名而控制根缺失的当场 `SPEC_GAP`；`check_order` 在 schema 里是 optional，故读法为
  `.get(…, [])`（下标形式会崩掉 schema 明说合法的 run，R1 实测）。**不继承**：run 是把模板*抄*进
  自己 control root（rider `delta-prose`），只对此后起草的 run 生效——本裁决接受的代价，与 `HD-16`
  同向。R1 链：`e9166d2` 构造 → FULL `CHANGES_REQUIRED`（记录 `1025491`）→ bank `0458bfb` →
  修腿 `dbbec28` → targeted VERIFY `REVIEWED_NO_BLOCKER`（记录 `1986912`）。
- basis: `v3-review-full-11ce5b4.md` `O-4`（`R5` 归口用户）· 用户裁决 2026-08-11

### HD-18 · 拆分单立一批，排在批 B 之后（批 A 因此收窄）
- 2026-08-08 · user · scope: standing · status: implemented（2026-08-10 随 A2 收批：「拆分离开
  批 A」半边已由 A2 执行完毕消耗；前向细则各有承载——排序（排批 B 之后）与「先设计跨仓运作模型
  再执行」在拆分批 backlog 行原文（该行 2026-08-19 随 `HD-49` 迁入本仓 `CONSTRUCTION-LEDGER.md`，此前住调用者 `HARNESS-LEDGER.md`）；rider `CLI-hist` 的随批归属在其
  redeem-when 列；完整搬出账在 A2 plan §R5/R6）
- 裁决：`HD-15`/`HD-16` 的**拆分执行离开批 A**，单立一批，**排在批 B（「谁调用、谁绑定」）之后**；
  批 A 的 A2 只保留单仓内改造。
- 后果：A2 = `AMBIG` 存活审计 + `HD-14` 六节搬层 + CONFIG 参数化 + 共享核抽取 + `HD-12` closeout
  删除，每轮各有 revert unit。拆分批先做**跨仓运作模型设计**再执行——批 B 的三件（`run_all` 接哪个
  入口 · ledger 绑多紧 · `pack_digests` 去留）在两仓下每件都变形，单仓版先答完两仓版才有底；另有
  A1 未 scope 到的面：评审记录在 X 仓而它讲的 run 在 Y 仓 · ledger 指针跨仓 · `rsc.py` 哪半跑哪边 ·
  freeze marker 归哪仓 · `repo-audit.py` 的 `ROOT` 语义。rider `CLI-hist` 随拆分批走。
  **`HD-10` 不变**：推迟执行不等于取消。
- basis: 本对话。**同批更正 A2 plan Notes 的「单仓先建等于建两遍」**——那句说强了：R2 解决的是
  per-run 常量怎么传，与仓库数量无关；R3 的共享核换仓是**路径变更，不是重新设计**。

### HD-20 · `E2` 冻结优先于 `E10` 自由通道（rider `E2-FC` 兑付）
- 2026-08-08 · user · scope: standing · status: **retired**（2026-08-27 批 `FREEZE-TO-ALARM`
  的用户裁决 4 转 `retired`：本条唯一的主题是「自由通道 vs `E2` 冻结」这个冲突，而该批把 `E2`
  由「无 recorded ruling 不得写」改为「写了要逐站点披露」，冲突的一方消失、主题随之消失
  ——状态只有用户能翻，本条的翻转即那次裁决本身。本条承载的两句例外——`E10` 自由通道句与
  `R10` 路由句各自的 `E2` 例外——与本翻转同 commit 删除，`E2` 条款自身的改写紧随其后（同轮下
  一 commit，先删引用再改被引之物）。**本条留在本节、未移入 archive**：该批 plan 的 acceptance
  要求 `HD-20` 在本文件内可读作 `retired` 且该 commit 恰含两个文件；移档是可分离的簿记，留给
  收轮，先例 `a554c0b` 是同 commit 移档。**原 status：implemented**，其括号原文照搬、逐字不
  改：`E10` 自由通道句的 `E2` 例外承载，同 commit；rider 行同 commit 删）
- 裁决：同时被 `E2` 冻结又是 `E10` 成员的路径（2026-08-08 建条时仅 `paragraph-map.schema.json`；
  2026-08-23 起共两件——`HD-56` 使 contract v4 亦入此交叉），其字节**先欠
  `E2` 的 recorded ruling**——自由通道与 must-fix 通道都不写它，供了字节的 finding 在裁决存在前
  bank。理由：若一条 low finding 就能写冻结字节，`E2` 整条被绕开——冻结的意义就在「必须有裁决」。
- basis: rider `E2-FC`（`v3-checkpoint-read-838c413.md` L-1）

### HD-21 · 新治理文件的提问义务：钉死保留（rider `E10-crit` 兑付）
- 2026-08-08 · user · scope: standing · status: implemented（`E10` (b) 义务句后的提问义务承载，
  同 commit；rider 行同 commit 删）
- 裁决：成员集仍由 `E10` 成员句穷尽（钉死不撤）；**后来出现、声称对本层任一规则有权威的文件，
  在成员句点名它之前不是成员，且造出它的那一轮必须把「算不算成员」的问题与答案记下来**。
  `B-1`（决策簿出现时无人发问）即此判据缺失的第一次实现。
- basis: rider `E10-crit`（`v3-checkpoint-read-838c413.md` O-1）· `v3-review-full-a7bb1d6.md` B-1

### HD-22 · `E10` 成员句三处镜像：不加机器，换 deadline（rider `E10-sync` 重定范围，非兑付）
- 2026-08-08 · user · scope: standing · status: implemented（rider 行自身承载新 redeem-when 与
  deadline，同 commit 改写；**行不删**——散文腿无守卫这个缺陷仍在）
- 裁决：不给成员句加解析守卫（`E6`：需要新机器的修是重新质疑被守之物的信号；且天真解析已被 (b)
  义务句弄成 10 项，守卫将依赖散文标点）；纪律＝**碰成员句的任何批三处同改并在 commit 正文点名**；
  deadline 由「v4 铸成」改为「下一次碰成员句的批」（`V-4`：原 deadline 已不再 bound damage）。
- basis: rider `E10-sync` · `v3-review-verify-7a08265.md` V-4 · route-b 轮 P2 实测

### HD-19 · 本文件不进 `E10`；必读义务写在 charter 里
- 2026-08-08 · user · scope: standing · status: implemented（2026-08-08，`E10` cold-read 从句后的
  义务句 + 九成员句共同承载，同 commit）
- 裁决：**决策簿不是指令层成员**；「每轮开轮读 §live」的义务直接写在
  `CONSTRUCTION-CHECKLIST.md` 的 `E10` 里，本文件自身治理仍是纪律（`HD-7`），按小节引用、不按 blob。
- 取代 2026-08-08 早些时候「走最小修 (a)」那条裁决（该条从未建条目、只活在 `fd058aa` 正文，
  正是 VERIFY 的 `V-2`）。**(a) 试过、被独立评审过、退回**：它确实关掉了 `B-1`，但把一个用户随时
  写入的登记簿套进了为九份慢变规则文本设计的机器，换来三条治理问题（`V-1` 读取范围不可满足 ·
  `V-3` 每写一条裁决都成 amendment 而无人分类 · `V-7` 先行词漂移），三条随本轮消失。
  **放弃的**：路径守卫不再扫本文件。**未消失的**：可达性仍靠 `CONSTRUCTION-CHECKLIST.md` 里一句
  无机械守卫的散文——(a) 下是成员句，(b) 下是这句义务句，暴露面等价（VERIFY `P3`）。
- basis: `v3-review-full-a7bb1d6.md` `B-1` · `v3-review-verify-7a08265.md` `V-1`/`V-2`/`V-3`/`V-7`

### HD-1 · 裁决独立成层（立项与四面分工）
- 2026-08-08 · user · scope: standing · status: implemented（2026-08-08，本文件 +
  `document-harness/README.md` journal 行收窄，同 commit）
- 裁决：harness 的用户裁决独立记录于本文件；journal 收窄为分析/推理/实测；待办归 rider/backlog；
  ledger 只留指针。本文件是裁决的最高 source of truth，instruction 反向 base on 它。取代
  `SIMP-D` 三分工（pre-log 裁决，按 HD-8 不建条目、不画边；取代关系记于此）。
- basis: [journal/decision-log-2026-08-08.md](document-harness/journal/decision-log-2026-08-08.md) §2

### HD-2 · 状态机四态与三不变量
- 2026-08-08 · user · scope: standing · status: implemented（本文件头部承载）
- 裁决：live / implemented / superseded / retired；同主题至多一条 live；supersession 与挪节同
  commit；终态不可逆，复活开新条。implemented 的判据＝有没有别的东西替它说话。
- basis: [journal/decision-log-2026-08-08.md](document-harness/journal/decision-log-2026-08-08.md) §3

### HD-3 · scope 四档与用途
- 2026-08-08 · user · scope: standing · status: implemented（本文件头部承载）
- 裁决：standing / mechanism / batch / one-shot；用途＝到期条件 + grep 档位过滤（「读取路由」
  用途被驳回撤销）；batch 限构造轮，产品 run 的轮内约束归其控制面。
- basis: [journal/decision-log-2026-08-08.md](document-harness/journal/decision-log-2026-08-08.md) §3

### HD-4 · 准入与颗粒度
- 2026-08-08 · user · scope: standing · status: implemented（本文件头部承载）
- 裁决：三问任一为是即进；反向排除（轮内约束/收口处置/会话判断/可重算事实）；一条＝一件能被
  独立推翻的事。rider（未解问题）与 decision（已裁约束）正交。
- basis: [journal/decision-log-2026-08-08.md](document-harness/journal/decision-log-2026-08-08.md) §3

### HD-5 · 读者与继承
- 2026-08-08 · user · scope: standing · status: implemented（本文件头部 + README journal 行）
- 裁决：每轮 cold read 必读 §live；plan **原样继承**裁决、不转录（转录是漂移面，两次实证）；
  执行中按需 grep。§implemented 与 archive 不在必读内。
- basis: [journal/decision-log-2026-08-08.md](document-harness/journal/decision-log-2026-08-08.md) §3

### HD-6 · 删除纪律
- 2026-08-08 · user · scope: standing · status: implemented（本文件头部承载）
- 裁决：archive > 100 行时询问一次；删除＝「今后不会再被援引」∧「能从 record 反推」，人判、
  默认不删；superseded 链永不可删。
- basis: [journal/decision-log-2026-08-08.md](document-harness/journal/decision-log-2026-08-08.md) §3

### HD-7 · 无 lint，纯纪律
- 2026-08-08 · user · scope: standing · status: implemented（本文件头部承载）
- 裁决：entry 字段完整性、必读义务、archive 触发询问全部走纪律，不加机械 enforcement。
- basis: [journal/decision-log-2026-08-08.md](document-harness/journal/decision-log-2026-08-08.md) §3

### HD-8 · 历史不迁
- 2026-08-08 · user · scope: standing · status: implemented（本文件头部承载）
- 裁决：本 log 只对今后生效；此前裁决（含 ledger「已裁但只存在于对话里的」12 条）留原处不建
  条目。代价照记：那 12 条继续处在 ledger 120 行上限的压力下，本 log 保护不到。
- basis: [journal/decision-log-2026-08-08.md](document-harness/journal/decision-log-2026-08-08.md) §3
