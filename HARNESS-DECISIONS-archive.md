# HARNESS DECISIONS — archive（只装死条目）

> 从 [HARNESS-DECISIONS.md](HARNESS-DECISIONS.md) 移入的 `superseded` 与 `retired` 条目，
> 原文照搬、不改写。不在任何必读范围内，grep 可达。本文件**超过 100 行**时询问用户一次
> 要不要清（删除双条件合取 + 默认不删 + superseded 链永不可删，见主文件头部 HD-6）。
>
> **`HD-6` 的询问第八次已付：2026-09-04（就地改契约族 `HD-63/64/67/68/70` 五条移入，随批
> `CORE-MOUNT` 收批）。** 触发点即本次移入（本行随收批补记于抬头，与前七次同处——VERIFY `674ac43`
> 的 `L-2v` 指出触发说明先前只落在下方 2026-09-04 搬入节的节内、未在此抬头登记）。**判据实测，删除的
> 双条件合取不成立**：五条仍被外部援引（`HD-65` 引 `HD-64`；`HD-63` 的类名仍被多处沿用），按**默认不删**
> 执行。**同处并记 `L-1v` 的前向更正（`HD-59`，下方搬入节原文一字不动）**：该节举 rider
> `protected-set-says-five` 为「`HD-63` 仍被援引」的例证，但该 rider 已于 `4020efa` 兑付删行，举例已陈旧；
> 结论（`HD-63` 仍被援引）不受影响，凭的是上述其余援引。
>
> **`HD-6` 的询问第七次已付：2026-08-28（`HD-44` 移入，随批 `FREEZE-TO-ALARM` 的修腿）。**
> 触发点即本次移入。**判据实测，删除的双条件合取不成立**，且这次第一个条件就已落空：`HD-44`
> 仍被援引——`CONTRACT-V4-SIGNATURE.md:41` 拿它判三个已退役源文件的字节不可写、
> `document-harness/journal/de-prefix-2026-08-20.md:208` 拿它判去前缀那次改名不是写、本批的 plan
> 与 FULL 记录各点名它一次；何况它是 `superseded` 链的一端（后继 `HD-62`），而该链**永不可删**。
> 按**默认不删**执行。执行者按纪律触发并转呈 orchestrator，本腿内未得答复（先例：第四次同形）。
> 下次触发点仍是下一次有条目移入本档时。**本次刻意不写移入后的行数 figure**——那个数写在被它所量
> 之物最后一次改动之前就作废（`E3`），rider `archive-header-selfcount` 记的正是本抬头块上一次这么
> 做的那一例；要数就现跑 `wc -l HARNESS-DECISIONS-archive.md`。
>
> **`HD-6` 的询问第六次已付：2026-08-26（`HD-61` 与 `HD-60` 移入、移入后本档 404 行）。**
> 触发点即本次移入。**判据实测，删除的双条件合取不成立**：两条都仍被援引——plan
> `document-harness/plans/core-set.plan.md` 的裁决 21 与 item F、轮 2 的开轮与 item F
> commit 正文、以及冷读记录 `v3-cold-read-d3ba221.md` 都点名它们——故第一个条件
> 「今后不会再被援引」对两条都为假，按**默认不删**执行。本次连同结论一并呈报用户，
> 用户未另裁即维持不删。下次触发点仍是下一次有条目移入本档时。**
>
> **`HD-6` 的询问第五次已付，且是四次里第一次真拿到答复：2026-08-26（`HD-56` 移入、移入后本档
> 345 行），用户裁**「不删」**——判据是 `HD-6` 的双条件合取不成立（`HD-54`→`HD-58`
> 与本次的 `HD-56` 都是 `superseded` 链，该链永不可删），载体为 plan
> `document-harness/plans/core-set.plan.md` 裁决 17。下次触发点仍是下一次有条目移入本档时。**
> **第四次：2026-08-26（`HD-54` 移入、移入后 309 行），执行者按纪律触发并转呈
> orchestrator，本轮内未得答复；按「默认不删」执行——不清。**
> **第三次：2026-08-21（`HD-50` 移入、290 行），用户未答；按「默认不删」执行——不清。**
> **第二次：2026-08-14（`HD-24` 移入、128 行），用户未答；同按默认不删。**
> **第一次：2026-08-13（104 行触发），用户裁「不清」。** 判据实测：
> 七条全部仍被外部援引（`HD-11` 46 · `HD-14` 42 · `HD-16` 40 · `HD-12` 33 · `HD-17` 22 ·
> `HD-13` 17 · `HD-26` 16 · `HD-29` 8 处，`grep` 排除本文件自身），故删除的第一个条件
> 「今后不会再被援引」对每一条都不成立；其中三条 superseded（`HD-16`→`HD-28` · `HD-26`→`HD-31` ·
> `HD-29`→`HD-33`/`HD-34`）另受「链永不可删」保护。下次询问的触发点是**下一次有条目移入本档时**。

### HD-44 · `E2` 冻的是**字节**，不是「本仓的这些路径」——故整体搬仓不是写，不欠裁决
- 2026-08-18 · user · scope: standing · status: **superseded**（2026-08-28 批 `FREEZE-TO-ALARM`
  的修腿按用户当日裁决转 `superseded`，后继＝**`HD-62`**，双向指针与本次移档同 commit——`HD-30`
  部分收窄机制：后继承载收窄后的全文，原条整条转 `superseded` 入 archive。被收窄的只有末句
  「真的改动那些字节仍然照旧欠裁决」：用户 2026-08-27 的裁决 1 已把 `E2` 从写前 gate 改成事后
  逐点披露（item A `184387c`），而本条 status 为 `live`、决策簿又压细则，留着那半句等于把裁决 1
  结束的僵局在更高一层重新装回去（FULL `v3-review-full-ad0663d.md` `B-1`）。**原 status：live**，
  其括号原文照搬、逐字不改：`E2` 正文只说「三个 blob 加一个目录，
  都由 inspection 可判」，没说这些路径必须留在哪个仓；跨仓之后这个歧义第一次咬人，而层里无承载。
  要转 `implemented` 须有一个设计轮把「冻结面住哪」写进 `E2`）
- 裁决：`E2` 冻结的对象是**那些字节**（contract `b2dbdf75` · supersession-1 `68031fa2` ·
  supersession-2 `e1a2f26b` · 再基线时 schema pack 的十五件）。**字节完好地存在于某处、且被
  gitlink 钉住**时，把它们从某个仓移走**不构成 `E2` 意义上的「写」**，因而不欠 `E2` 的记录裁决。
  反读法（冻的是「本仓的这些路径」，故删除是一次未经裁决的写）**被否**。
- 后果：**冻结面自 2026-08-17 起住在 harness 仓**，与命名它的那条规则同仓——这是本条要留下的
  那个事实，因为拆分后「`E2` 说的那些字节在哪」不再不言自明。调用者仓以 gitlink 钉住哪个
  revision，冻结面就是那个 revision 上的那些件——本条建条日（2026-08-18）为十八件；自 `HD-56`
  （2026-08-23）合并三源为 v4 后为十六件（v4 一件 + schema pack 十五件）。（此句更正落于
  2026-08-23，依用户当日「落」裁决——签字 commit `3b25f3c` 曾声称同批更新此句而其 diff 未含，
  见 `v3-cold-read-cf54a79.md` `L-3`。）今后任何调用者删掉自己那份副本，按本条同样
  不欠裁决；**真的改动那些字节仍然照旧欠裁决**，本条一个字都没放宽那一半。
- basis: 用户裁决 2026-08-18（对话）· FULL `v3-review-full-2d148f3.md` `B-4` 提出两读法并按 `R5`
  归口用户 · 先例 `HD-39`（删除轮把 `E2` 的理由写出来）与 `HD-20`（冻结的意义就在必须有裁决）

### HD-61 · `E2` recorded ruling：准予轮 2 一并写契约 v4 的五处引用降名
- 2026-08-26 · user · scope: one-shot（与 `HD-60` 同随轮 2 的契约写入消耗 retire；消耗前仍可
  supersede）· status: **retired**（2026-08-26 轮 `CORE-SET-SIGNATURE` 的 item F commit 消耗
  完毕后由用户裁决转 `retired`，同日移入本档。**原 status：live**（授权已给、尚未应用——轮 2
  开轮当日给出），其下的追注原文照搬、逐字不改：**追注 2026-08-26**：
  授权已由轮 `CORE-SET-SIGNATURE` 的 item F commit 应用完毕，五处降名与 `HD-60` 的三处改址落在
  同一次契约写入；按 one-shot 的消耗条件本条应转 `retired`，但**状态只有用户能翻、session 只能
  提议**（本文件头部不变量 + `E1`/`R5`），故本行只记消耗事实、不翻状态）
- 裁决：除 `HD-60` 授权的签字改址三处之外，准许轮 `CORE-SET-SIGNATURE` 在**同一次契约写入**里
  一并降名**五处引用**——`:25` `:27` `:30` `:253` 四处指向本仓 `migration/` 的节点与签字记录
  （N0 记录 · W2 记录 · supersession-2 签字记录），`:32` 一处指向
  `document-harness/plans/contract-v4.plan.md`。降名＝路径形态去掉、名与持有者留下，与轮 1 的
  item J / item M 同形。**站点由 executor 写入前自行复核，不以本条枚举为准。**
- 为什么另立一条而不是改 `HD-60`：两条授权的**对象不同**——`HD-60` 授权的是签字载体改址，本条
  授权的是引用降名；`HD-60` 无需收窄也无需推翻，故不走 `HD-30` 的后继承载，两条并存、各自消耗。
  颗粒度按准入三问的「一条 = 一件能被独立推翻的事」：撤回本条不动签字改址，反之亦然。
- 为什么一次写完而不分两轮：那五处与已授权的两处是**同一类缺陷**（产品档的契约指向调用者不携带的
  材料），`E10` 自己写着「a channel narrowed to the reported instance leaves its siblings to be
  found one re-read at a time」；分两轮写同一个文件的同一类字节，等于对同一个冻结面开两次写入
  窗口。用户 2026-08-26 于轮 2 的 `E11` 卡上裁「一次写完」。
- 授权**不含**：契约的接口 / enum / invariant / 版本边界 / 依赖图，即签字所冻结的实质文本；
  `schema/document-assurance-v3/` 十五件一件不碰。越出即「无裁决写入冻结面」。
- 随行义务：`HD-60` 义务①（写入后 `E2` 名单的 v4 blob 字面量当场更新为新 blob）**覆盖本条的
  字节**——两条授权若落在同一个 commit，只更新一次；若分开落，后落的那个负责把字面量对齐。
- basis: 用户裁决 2026-08-26（轮 2 `E11` 卡，选项 A）· `E2` 的 "obtain the ruling and write
  under it" 条款 · `HD-60`（同轮同文件的姊妹授权）· plan
  `document-harness/plans/core-set.plan.md` 裁决 12 与 item M · 冷读
  `v3-cold-read-d3ba221.md`（同一次开轮读，独立点出 `HD-60` 比 item F 更窄）

- **retired 2026-08-26**（用户裁决：两条 one-shot 授权已由轮 `CORE-SET-SIGNATURE` 的 item F commit 消耗完毕，随行义务同 commit 兑现，故一并转 `retired` 并移入 archive。**状态翻转与消耗它的那个 commit 不是同一个**——`HD-2` 的字面是「状态翻转随载体同 commit」，而载体 commit 由冷 executor 落、翻转只有用户能做，两者不可能同 commit；照实记，不改名。）

### HD-60 · `E2` recorded ruling：准予轮 2 写契约 v4 的签字改址字节
- 2026-08-26 · user · scope: one-shot（轮 2 写入并更新 `E2` 字面量后消耗 retire；消耗前仍可
  supersede）· status: **retired**（2026-08-26 轮 `CORE-SET-SIGNATURE` 的 item F commit 消耗
  完毕后由用户裁决转 `retired`，同日移入本档。**原 status：live**（授权已给、尚未应用——轮 2
  未开），其下的追注原文照搬、逐字不改：**追注 2026-08-26**：轮 2 已开，
  授权已由 `CORE-SET-SIGNATURE` 的 item F commit 应用完毕——三处改址落定，随行义务三件同 commit
  兑现：① `E2` 的 v4 字面量已更新为 `5dfb7b64…` · ② 签字对象仍为 `614932de…`、v4 未重签 ·
  ③ 新载体 `CONTRACT-V4-SIGNATURE.md` 与 `HD-56` 转 `superseded` 的双向指针同 commit。按 one-shot
  的消耗条件本条应转 `retired`，但**状态只有用户能翻、session 只能提议**，故本行只记消耗事实）
- 裁决：准许轮 `CORE-SET-SIGNATURE`（批 `CORE-SET` 轮 2，item F）写入
  `contract/Document-Work-Assurance-Contract-v4.md` 的字节，**限于签字载体改址这一件**。站点三处，
  写入前由 executor 自行复核、不以本条为准：frontmatter 的 `signature_owner:` 字段 · 抬头
  *Signature semantics* 警示块里指向决策簿的那句 · 文末「The signature record … lives as an `HD`
  entry」那句。**`E2` 条款本身一字不改**——本条走的是 `E2` 自己写的第二条出路（"obtain the ruling
  and write under it"），形状比照 `HD-57`。
- 授权**不含**：契约的接口 / enum / invariant / 版本边界 / 依赖图，即签字所冻结的实质文本；
  `schema/document-assurance-v3/` 十五件一件不碰。越出即「无裁决写入冻结面」。
- 三件随行义务，缺一不可，且与写入**同 commit**：① 写入后契约 blob 改变，`E2` 名单里的 v4 字面量
  `dfc983d2…` 当场更新为新 blob（`HD-57` 同形先例）· ② `HD-56` 绑定的**签字对象仍是 `614932de…`**，
  不因载体改址而改（批 `CORE-SET` 裁决 10：搬载体不动被签字节）· ③ 新签字载体文件、与 `HD-56` 转
  `superseded` 的双向指针，三者同一个 commit（`HD-30` 后继承载全文 + `HD-2` 状态翻转同 commit）。
- 顺带闭合：上述三处里有两处是指向 `../HARNESS-DECISIONS.md` 的 markdown 链接，属轮 1 收轮时记在册
  的「八条归轮 2」残留（journal `document-harness/journal/core-set-layer-2026-08-26.md` §2）。
- basis: 用户裁决 2026-08-26（对话）· `E2` 的 "obtain the ruling and write under it" 条款 ·
  `HD-20`（`E2` 冻结优先于 `E10` 自由通道，故本条是写入的前置）· `HD-57` 形状先例 · plan
  `document-harness/plans/core-set.plan.md` 裁决 10 与 item F
- **retired 2026-08-26**（用户裁决：两条 one-shot 授权已由轮 `CORE-SET-SIGNATURE` 的 item F commit 消耗完毕，随行义务同 commit 兑现，故一并转 `retired` 并移入 archive。**状态翻转与消耗它的那个 commit 不是同一个**——`HD-2` 的字面是「状态翻转随载体同 commit」，而载体 commit 由冷 executor 落、翻转只有用户能做，两者不可能同 commit；照实记，不改名。）

### HD-24 · AMBIG 七树归属已裁：v2 连通件 + 两记录树 travel，stages/ 随 v1 族归拆分批（`HD-17` 的兑付）
- 2026-08-09 · user · scope: standing · status: **superseded**（2026-08-14 由 `HD-39` 取代——
  按 `HD-30` 机制：七树处置由 travel 收窄为**删除**，全文由 `HD-39` 承接并补上其未 scope 的
  v1 运行时族；原文以下照搬不改写）
- 裁决：R0.1 存活审计呈表后逐项裁定——① `ResearchSystem/harness/` ② `tooling/rsclib/harness/`
  ③ `tooling/tests/harness/` ④ `schema/harness-v2/` 是一个连通 live 件，连同
  `contract/General-Harness-Contract-v2.md`（39 测试运行时读其字节）**整体 travel**；
  ⑤ `migration/general-harness-v2/` ⑥ `migration/stage-control-refactor/` 按「记录跟着被记录的
  对象走」属**造仪器的记录**（非 harness 在产品上跑出的保障记录），**travel**；⑦ `stages/`
  **处置归拆分批、与 v1 stage-control 族同批**——4 条真 markdown 链接钉着它（含已签
  `Stage-Control-Contract.md:23`），单删即 repo-audit 硬失败，「直接删」不存在。
- 后果：travel 集在 `HD-16` 的 A+B+C 之外新增本批成员；执行全落拆分批（搬 ② 必同批剪
  `rsc.py:50`/`:739`，即 rider `CLI-hist` 的一半）；`rsc.py` 归属维持缓裁。① 的字节级身份
  （5 profile 为域中立工作形态原型、4 adapter 全 `declared` 从未实现、issue registry 空、
  区域 UNSIGNED CANDIDATE 从未签署）与全部测量在 basis。
- basis: [journal/batch-a2-2026-08-09.md](document-harness/journal/batch-a2-2026-08-09.md) §2–§7 ·
  用户裁决 2026-08-09

### HD-16 · 新仓成员 = A+B+C；已关闭 run 与 shadow 留在产品仓（批 A `D6`）
- 2026-08-08 · user · scope: standing · status: **superseded**（2026-08-12 由 `HD-28` 取代——
  按 `HD-30` 机制：B 组成员定义收窄（ledger 两份留调用者仓），其余半边原文由 `HD-28` 全文承接）
- 裁决：新 harness 仓只带 **A 仪器 + B 治理账本 + C 评审记录**（242 files / 57,273 行 / 向外引用
  152 处）；**D 已关闭 run 的产物与 E shadow 留在产品仓**。
- 后果：**记录跟着被记录的对象走，不跟仪器走**——run 是 harness 关于*这个*产品的记录，换个产品即
  不适用。接受的代价：两边各持一半历史；harness 的历史产出住在产品仓。避开的代价：新仓不再背
  2,241 条指向对面仓库的只读路径（占全带方案外引用的 94%）。
- basis: journal §13.4

### HD-26 · ledger 解耦：仪器只输出、不写入；形状 defer 到 I/O design（批 B ②）
- 2026-08-11 · user · scope: standing · status: **superseded**（2026-08-12 由 `HD-31` 取代——
  按 `HD-30` 机制：硬约束半边收窄（承接物移调用者侧自选），只输出不写入 + citation 作废两半边
  由 `HD-31` 全文承接）
- 裁决：harness **不负责往 ledger 写**，只负责输出；ledger 的写入格式是 global 的，不该被仪器绑住。
  具体输出契约 **defer 到 I/O design**（批 B R2，前置 = R1 落地）。**并附**：backlog 里
  「citation 规则因此暂留层外」一句作废——全仓查无承载（`citation` 一词被产品概念 `citation-key`
  占满），用户裁定删除而非补写。
- 后果：现测四处耦合，两读两写——读 = `tooling/hooks/ledger_cap_check.py`（硬编码 ledger 路径 +
  `MAX_LINES`）· `dispatch.py:636` 层 read 提示词；写 = run 的 `write_scope` 直接列 ledger 路径
  （p3-corr / p4-bridge / p4-doc）· `chk-ledger-note`（p4-bridge 的 `locator_exists`，锚点是 ledger
  里一句人手写的散文）。**硬约束**：`chk-ledger-note` 一拆，harness 就再没有手段验证「这轮该记的事
  真记下来了」，该保障退化为纪律——输出契约必须有承接物，否则是净损失。
- basis: 本批 journal batch-b-2026-08-11.md §2 · 用户裁决 2026-08-11

### HD-29 · 调用模型：submodule 钉版 + 调用者仓零升级 + 适配必须留痕
- 2026-08-12 · user · scope: standing · status: **superseded**（2026-08-12 拆分为 `HD-33`
  （调用模型 + 归属）与 `HD-34`（调用者纪律 + 逃生口）——颗粒度修正（一条 = 一件能被独立推翻
  的事，R2 转录核查 finding 21），两后继共同取代）
- 裁决：调用模型 = **submodule**（`HD-15` 拆分形态在调用侧的兑现）：调用者仓以 gitlink 钉住
  harness 版本，run 目录（可 gitignore）、freeze marker、四件实例文件全归调用者仓；**调用者仓内
  不得改动/升级 harness 内容，任何适配必须记入调用者自己的 decision log**；**copy 仅为逃生口**
  （submodule × worktree 冲突时），代价 = 版本追溯 + 漂移可见性，漂移现阶段接受。
- 后果：升级 = 显式的 gitlink 指针变更 commit，历史可读；「用哪个版本的仪器查的」由候选 commit
  自带（copy 守不住的那条线）。ledger 跨仓指针问题不存在——每库用自己的四件。
- basis: journal §5（submodule vs copy 决定线 + freeze marker 身份）· io-design.md §7 ·
  用户裁决 2026-08-12

### HD-17 · `AMBIG` 138 件本轮不裁，A2 前先查存活（批 A）
- 2026-08-08 · user · scope: batch:A · status: **retired**（2026-08-09 消耗完毕：R0.1 存活审计
  已付，七项归属由 `HD-24` 裁定；与 `HD-24` 立条同 commit 移入本 archive）
- 裁决：v2 harness 遗留（`ResearchSystem/harness/` · `tooling/rsclib/harness/` ·
  `tooling/tests/harness/` · `schema/harness-v2/` · `migration/general-harness-v2/` ·
  `migration/stage-control-refactor/` · `stages/`）与 `tooling/rsc.py` 的归属**本轮不裁**；
  A2 开工前先查它们是否还有活消费者，**避免把死件搬进新仓**。
- basis: journal §13.5

### HD-11 · 模板脚本改「共享核 + per-run 增量」（批 A `D1`）
- 2026-08-08 · user · scope: batch:A · status: **retired**（2026-08-10 batch:A 随 A2 收批到期，
  用户批准；细则由 carrier 继续在力不受影响。曾 implemented（2026-08-09，R2+R3 两轮承载：R2
  参数化 `7e8f920`→修腿 `3b6267c`→VERIFY 无 blocker；R3 共享核定形 `cef6138`→FULL
  `CHANGES_REQUIRED`→修腿 `638972f`→VERIFY 无 blocker（`v3-review-verify-638972f.md`）。
  carrier = run-v2 README 实例化节 + 三步骤脚本 docstring 同向 + 五套模板测试自模板路径驱动
  （102 条）——散文承载、无机械 enforcement：run 抄模板不被任何 gate 拒绝（rider
  `delta-prose`）；「零抄件」限步骤脚本，comparator 仍按 `EXECUTION.md` 规则抄于 instruction 旁
  （VERIFY `V-1` 的限定）））
- 裁决：run 不再各自携带模板脚本抄件，改为共享核 + per-run 增量。
- 后果：A2 最大项。**必须先把「改文件填 CONFIG 块」换成「读配置 + 传参」**（三份脚本 `__file__`
  派生 control/evidence 根、四份靠填 CONFIG）。可共享面实测 ≈883 行/run。
- basis: journal §2 · §3

### HD-12 · CheckResult 关闭后删，只留一手输出，只管今后的 run（批 A `D2`）
- 2026-08-08 · user · scope: batch:A · status: **retired**（2026-08-10 batch:A 随 A2 收批到期，
  用户批准；细则由 carrier 继续在力。曾 implemented（2026-08-10，R4 承载：构造 `ed37a25`→FULL
  `CHANGES_REQUIRED`→修腿 `de8f4ef`→VERIFY 无 blocker（`v3-review-verify-de8f4ef.md`）。
  carrier = 模板第六共享脚本 `run_retire.py`（落地名 run_closeout.py，修腿改名——该名已是
  p4-doc/p4-bridge run-own post-run issue step 之名，FULL `B-1`）+ `review_subject.py` 的
  CLOSED carve-out（缺席合法、在场照验，注释 amend 载裁决）+ retire 套件 12 测试与 review 套件
  2 测试 + README retirement 句。删除范围按用户 D-a/D-b（2026-08-09）：只删 `check_order` 派生
  的逐份文件，聚合件与 `<check_id>.out.txt` 留，`check_result_refs` 原样——digest 对 evidence
  commit 历史永远可验。诚实边界：无 gate 强制 retirement 被执行（脚本自述 enforces nothing；
  `B-1` 失败路径靠改名消歧、非机器）；carve-out 钥匙是 run 自写 status（rider `status-key`）））
- 裁决：run **关闭后**删除逐份 CheckResult，只留一手输出；**只对今后的 run 生效**，已关闭的八个 run
  不追溯（守计划书 Constraints 的 closed-runs 只读）。
- 后果：A2 的 T2。**裁定时已知并接受的代价**：一手输出 20 份里 3 份 0 字节、10 份 11–23 字节，删后
  无法再从字节证明当时过没过；`check_result_refs` 的 digest 目标消失，closeout 需处置；新旧两套形态
  共存，`review_subject.py` 的完整性检查要能分辨。
- basis: journal §4.1 · §11.1 · §12.1

### HD-13 · 评审记录形态不变（批 A `D3`）
- 2026-08-08 · user · scope: batch:A · status: **retired**（2026-08-10 batch:A 随 A2 收批到期，
  用户批准；do-not 无承载物，批终即耗尽——A2 全程未就记录形态开轮，裁决兑现）
- 裁决：评审记录不动，T3 离开 A2 范围；不再就「记录要不要展示重推」开轮。
- 后果：实测支持——53 份里 50 份被引共 169 次，最硬的一类（16 次代码/测试 docstring）引的正是判断；
  且 66% 配方行不带把手，改「引用+重放」是加工作量而非减。
- basis: journal §10 · §12.2

### HD-14 · run-v2 README 的六节规则搬入 `EXECUTION.md`（批 A `D7`）
- 2026-08-08 · user · scope: batch:A · status: **retired**（2026-08-10 batch:A 随 A2 收批到期，
  用户批准；细则由 carrier 继续在力。曾 implemented（2026-08-09，`EXECUTION.md` 六节承载：搬移
  `418b89c` + 修腿 `fbcb035`；FULL `v3-review-full-418b89c.md` 与 VERIFY
  `v3-review-verify-fbcb035.md` 均 `REVIEWED_NO_BLOCKER`，R1 收轮；实际落点 404 行，非预估 350））
- 裁决：`templates/run-v2/README.md` 的六节规则移入已受 `E10` 保护的 `EXECUTION.md`，README 只留
  「怎么实例化这个模板」。
- 后果：搬迁本身是指令层 amendment，**开轮**。`EXECUTION.md` 171 → 约 350 行，成为层内最大文件。
  A2 要答的结构问题：`Instruction form` 与 `Authoring gate` 是起草期规则，而 `EXECUTION.md` 是
  执行者役职指令，读者是否同一。（答案落 R1 预览与 stage marker：多读者一文件，标注惯例既有。）
- basis: journal §11.3 · §12.4

### HD-43 · 拆分批 R1 的 `E9` 超腿：一次性追认，不改 `E9`、不立通则
- 2026-08-15 · user · scope: one-shot · status: **retired**（本条即裁即成立，无待执行动作；
  R4 收批时议转 `implemented`。**编号与状态只有用户能翻**，`HD-2`）
- 裁决：R1 走满五腿而 `E9` 上限为三，用户裁定**一次性追认**第四、第五腿（fix `100e2dd` +
  VERIFY `caf633c`），**不修改 `E9` 的三腿上限、不建立「超了再补批」的通则**。
- 判据（实测，非断言）：`E9` 原文「Budget per round: one FULL, at most one user-approved fix,
  one targeted VERIFY」把 FULL 与 VERIFY 一并计入，故 FULL `0792a89`（1）→ fix `22264b5`（2）
  → VERIFY `dd7a27c`（3）即已用满；`io-design.md:19` 同义（「评审预算至多三腿、预算是轮的
  属性」）。超腿的**内容**经 VERIFY `caf633c` 独立复算全部成立（travel 集 259 机械复现、
  260 blob 中 259 个跨仓逐字节相同、新仓套件 24/677→20/681 在校验过的 clone 里复现），故追认
  的是**预算**不是质量。
- 后果 / 诚实边界：**用户批准第二条修腿（「甲 + 花」）时拿到的账目是错的**——executor 报的是
  「三腿花了两腿」，那是只把 fix 计入腿数的读法，`E9` 文本不支持（VERIFY `100e2dd` 的 `F-1`）。
  退役 operating contract 写死「预算分类是用户的，executor 只 propose the accounting，绝不
  自行分类哪一轮消耗了什么」——本条追认的正是一次**在错账上做出的批准**，故记此边界而非略过。
  更正落 `030a999`。**本条不豁免任何未来轮次**：下一轮超腿仍须当场停下并重新取得裁决。
- basis: 用户裁决 2026-08-15（对话）· `v3-review-verify-100e2dd.md` `F-1` + 其自开自闭的
  `SPEC_GAP` 段 · `document-harness/CONSTRUCTION-CHECKLIST.md` `E9`
- retired 2026-08-15（用户裁）：执行完毕，无后继。

### HD-42 · 全电池枚举随删除由八条改六条：只此一次、只这两条、与删除同 commit
- 2026-08-15 · user · scope: one-shot（R1 执行即 retire）· status: **retired**（待 R1 执行）
- 裁决：`HD-39` 的删除使 `EXECUTION.md` 全电池枚举中的两条指向不存在的文件——
  `ResearchSystem/tooling/tests/harness/run_tests.py` 与
  `ResearchSystem/tooling/tests/stage_control/run_tests.py`。用户裁定**把枚举由「八条」改为
  「六条」并删去这两项，不算 `E10` 意义上的规则变更、不开设计轮**。**四重收窄，缺一不可**：
  ① **只此一次**（不建立「主体消失即可改枚举」的通则）② **只这两条**（其余六条一字不动，
  `nothing fewer` 子句保留）③ **与删除同一个 commit 落地**（不得先删文件后补规则，也不得反过来）
  ④ **该 commit 正文点名**本裁决与被删的两条。
- 判据（实测，非断言）：两个 runner 是 `unittest` 独立脚本，**pytest 收不到**——`python -m pytest -q
  --collect-only`（量程 = 从 `ResearchSystem/tooling` 跑）收 **701** 个测试，其中来自这两个文件的
  **0**；正因如此当年才把它们单列，防静默跳过。二者的 import 面**全部落在删除集内**
  （`rsclib.harness.*` 十个模块 / `rsclib.{stage_close,stage_control}`），**59 个测试
  （39 + 20）无一测到删除后仍存活的东西**。故删除零覆盖损失，留着则是两条指向空气的强制命令。
- 后果：`E10` 的 design test **无**「枚举主体消失不算改规则」这一例外，故本条是**用户当场造的一个
  例外**，形状比照 `E2` 的「只为该文件、只此一次」松冻结（`O-2b`）。**未豁免的**：该编辑仍是对
  `E10` 成员 `EXECUTION.md` 的写入，按 `E10` **仍欠该层的一次独立 read**（riding the next read of
  this layer at per-member digest cost）——本条只免「开设计轮」，不免读。
  **同批须核**：rider `tier-scope` ② 的 redeem-when 点名的是 tiering **节头**，而本次编辑落在节内
  的枚举句，严格论不触发；R1 应主动核一次而非等它咬人。**承载点三处**（扫类实测，量程 = 全仓
  tracked `*.md`/`*.py`，排除评审记录与 archive）：`EXECUTION.md:329` · plan 步骤 13 · plan
  Acceptance；另五处「八条」属别的主题（`HD-25` 八条守卫 / digest-narrowing 八条探针 / 批 B
  第八条测试），不动。**无测试或代码钉住该枚举**。
- basis: 用户裁决 2026-08-15（对话）· `v3-checkpoint-read-a654fb2.md` `M-1` ·
  executor 复现（pytest collect 701/0 · import 面 · 39+20 测试数）
- retired 2026-08-15（用户裁）：执行完毕，无后继。

### HD-39 · v1/v2 全族**删除**（`HD-24` 的收窄后继）：七树不 travel，连 v1 运行时族一并删
- 2026-08-14 · user · scope: standing · status: **retired**（待拆分批 R1 执行；**编号是提议，
  状态只有用户能翻**（`HD-2`）。按 `HD-30` 机制承载 `HD-24` 收窄后的**全文**，`HD-24` 同 commit
  转 `superseded` 入 archive，双向指针）
- 裁决：`HD-24` 逐项裁定的七树**全部改为删除、不 travel**——① `ResearchSystem/harness/` ②
  `tooling/rsclib/harness/` ③ `tooling/tests/harness/` ④ `schema/harness-v2/` 及
  `contract/General-Harness-Contract-v2.md` ⑤ `migration/general-harness-v2/` ⑥
  `migration/stage-control-refactor/` ⑦ `stages/`（其「处置归拆分批」于本条兑现）；
  连同 `HD-24` **未 scope 到的 v1 运行时族**：`contract/Stage-Control-Contract.md` ·
  `rsclib/stage_control.py` · `rsclib/stage_close.py` · `schema/stage-record.schema.json` ·
  `schema/review-result.schema.json` · `schema/closure-receipt.schema.json` ·
  `schema/stage-control-fixtures/`（24）· `tooling/tests/stage_control/`（2）·
  `.claude/commands/rs-execute.md`。**合计 171 文件**（`HD-24` 时点报的 139 只覆盖前七树）。
- 判据：`HD-9` 三砍之**「无锁证词」**——无任何决定依赖这批字节。事实基础：A2 存活审计定性
  「注册在案、从未行使」（零份 Stage Record 曾存在），用户 2026-08-14 补充 v1 实际存活约半小时
  即被 v2 推翻、v2 未活过一天。`E2` **不挡**：其冻结清单穷举（v3 契约 `b2dbdf75` + 两份
  supersession + 15 个 schema 文件），两份待删契约均在清单外，规则原文「a path outside them is
  not frozen by this rule」——删除是普通用户裁决，不是动冻结面。
- 后果：travel 集不再含这七树，新仓不带从未行使的字节出门。**连带清单（R0 read `M-1` 更正后）**：
  ① `rsc.py:48`/`:50` 两条 import（rider `CLI-hist` 照旧兑付）**外加 `rsc.py:850`**——
  `except stage_control.StageControlFault` 在 `main()` 里包着 `args.func(args)`，是所有命令
  （含六个 v3 命令）的共用错误出口；只剪 import 不动它，会把每个命令的意外失败路径从
  `FATAL: …`/exit 2 变成未捕获的 `NameError`（re-read `M-1`；处置方式归 R1/R2 的设计判断）· ② **删除集之外有 4 个文件、
  **14 条引用**（13 markdown 链接 + **1 wikilink**）指进删除集，全部进 R1 改动边界**（**「3 个文件」是加入 wikilink 那一处时漏改的残数，R1 更正为 4——`split-design.md` §7 表与 plan 步骤 12/Acceptance 一直是 4**）——`ResearchSystem/README.md`（8）·
  `.goals/plans/general-harness-v2-architecture-revision.plan.md`（3，`:723-725`）·
  `.goals/plans/research-system-stage-control-refactor.plan.md`（2，`:323`/`:324`）·
  **`.goals/plans/document-work-assurance-harness-v3.plan.md`（1 条 wikilink，`:41`，目标 stem
  `General-Harness-Contract-v2`；**不原样引用**——wikilink 扫描无 inline-code 豁免，照抄即自造断链——`repo-audit` 的 wikilink 是与 markdown-link 并列的另一道
  硬检查 `:306`，按 stem 解析、不受 inline-code 豁免，故修完 13 条 markdown 仍 exit 1；re-read `M-2`）**；逐条见
  `split-design.md` §7 表。**本条初稿只点了「指向 `stages/` 的 4 条」（其一自删），即预算 3 条而
  实存 13 条**；`repo-audit` 的链接检查 resolve 任意目标路径、一条断链即 exit 1，故按初稿执行会
  撞上 `HD-24` 当初用来说「直接删」不存在的那个失败形态。③ 已关闭 run
  `p5b-firewall/build_run.py:216-217` 把两契约列在**边界排除表**（纯字符串、不读字节，不影响该
  run 既有证据）。rider `SCC` 随其 subject 删除而在 R1 **retire**；rider `PD`
  提到的「两处活调用是 v2 `schemas.pack_digests()`」随 ② 消失，其 v3 半边（删零调用函数）不变。
  **诚实边界**：⑤⑥ 是**记录**不是仪器（`HD-9` 三留之「证据」），删除它们在 tip 上移除 v2 的构造
  与评审轨迹；缓解事实 = 调用者仓保留全部 git 历史（本批新仓从头、不保历史，故历史只在调用者仓，
  `git show` 仍可达）。**已验并更正**：三个 v1 schema 的**字节读者**仅在 v1 族自身内、v3 零命中
  （本条初稿把这个 grep 结果写成了「全仓读者」，而 `ResearchSystem/README.md:43-45` 正链接着它们
  ——字节读者 ≠ 引用者，R0 read `M-1`）。
- basis: 用户裁决 2026-08-14（对话）· [journal/repo-split-r0-2026-08-13.md](document-harness/journal/repo-split-r0-2026-08-13.md) §7 ·
  `document-harness/split-design.md` §7/§10.2 · supersedes `HD-24`
- retired 2026-08-15（用户裁）：执行完毕，无后继。

### HD-27 · `E2` 不加守卫：`pack_digests()` 不接、路径判据也不加；重开条件 = 拆分批（批 B ③）
- 2026-08-11 · user · scope: standing · status: **retired**（"不加守卫"是 standing do-not，
  rider `PD` 只承载 `pack_digests` 那半边，`E2` 通用守卫这半边无别家）
- 裁决：**不**把 `pack_digests()`（`__init__.py:238`）接成 `E2` 的机械挂点，**也不**另加路径判据守卫；
  `E2` 维持纯散文规则 + 纪律。**重开条件 = 拆分批**（三条理由届时同时变形）。
- 后果：rider `PD` 的 redeem-when 由「I/O design 批一起议」重定为拆分批（比照 `HD-22`，重定范围
  非兑付，**行不删**）。同批分开的两件事：`pack_digests` 零调用**不是** `E2` 缺守卫的症状，而是
  **v3 证据从不记自己由哪个 interface 版本产出**（v2 的 `resolver.py:272` 记在 `bindings`，v3 全仓
  零命中）——后者与 `E2` 无关，随重开条件一并再议。
- basis: 本批 journal §3（三条实测：产品 run 的 `_check_git_diff_boundary` 已把 `schema`/契约列进
  `boundary.out`；构造批每轮独立评审且 boundary 检查点名 frozen surface；`HD-16` 使"证据离仓自证"
  价值落空）· `E6` · 用户裁决 2026-08-11
- retired 2026-08-15（用户裁）：执行完毕，无后继。

### HD-28 · 新仓成员（`HD-16` 的收窄后继）：A 仪器 + B=decisions/riders+decisions-archive + C 评审记录；ledger 留调用者
- 2026-08-12 · user · scope: standing · status: **superseded**（→ `HD-49`，2026-08-19 同 commit 迁入本档）（成员集已由
  `document-harness/split-travel-manifest.md` 承载并于 R1 搬迁完毕，拆分批 R3 2026-08-17 转；
  本条 2026-08-12 按 `HD-30` 机制由差量式收窄注重写为 `HD-16` 的**完整后继**，`HD-16` 同 commit
  转 superseded 入 archive，双向指针）
- 裁决：新 harness 仓带 **A 仪器 + B 治理登记（`HARNESS-DECISIONS.md` · `HARNESS-RIDERS.md` ·
  `HARNESS-DECISIONS-archive.md`，3 files——riders 无 archive）+ C 评审记录**；
  **`HARNESS-LEDGER.md` 与 `HARNESS-LEDGER-archive.md` 留调用者仓**；**D 已关闭 run 的产物与
  E shadow 留产品仓**（此半边承 `HD-16` 原文不变）。
- 判据：实例内容按「**谁的开发**」归属——harness 仓里填满的四件（decision log / rider bank /
  journal / ledger）是 harness 跑在自身的实例，调用者的归调用者；四件中唯 ledger 连**规则**都
  不归 harness（global 约定的收紧方言，harness 只占三个参数），故其实例随调用者。
- 后果：记录跟着被记录的对象走，不跟仪器走（承 `HD-16`）；A1 §13.4 的「B 治理账本 5 files」
  重算为 3。
- basis: [journal/batch-b-2026-08-11.md](document-harness/journal/batch-b-2026-08-11.md) §5 ·
  `document-harness/io-design.md` §6/§7 · 用户裁决 2026-08-12 · supersedes `HD-16`

### HD-48 · 下一个设计轮 = 三题打包（`layer-crossrepo-token` · `e1-disclose-home` · `dtw init` 写哪儿）
- 2026-08-19 · user · scope: batch:next-design · status: **superseded**（→ `HD-50`，2026-08-19 同 commit 迁入本档；其三题两题并入批 DTW-INDEPENDENCE R2、一题并入 R4）（排期裁决，执行完 retire；除本条外只活在对话里）
- 裁决：`CALLER-ONBOARDING` 收批后的**下一个队首是一个设计轮**，收三题：① rider `layer-crossrepo-token`
  （deadline 已于本轮到达——guard 接进仪器仓那一刻；今天不咬人只因它只扫新增行）② rider
  `e1-disclose-home`（deadline 亦于本轮到达：`E1` 的四持有披露句无载体、无责任人，本轮两次披露都只写在
  commit 正文里，属自定而非规则要求）③ `dtw init` 的两个实例文件写在 target 根固定文件名，要不要加
  `--into` 或改默认（`HD-33`/`HD-34`/io-design 均未定位置）。三题的修法都是 design 形状——加 clause 或
  加 bound——故 `E10` 要求开轮，不得搭任何 amendment 的车。
- **未选中的一题继续 bank**：仪器仓要不要也跑 `review_freeze_check` / `candidate_path_check`
  （它对自己的构造轮也是调用者、也真持有冻结窗口，而 `E9` 那道窗口在该仓目前零机械执行）。用户
  2026-08-19 裁不进本批；rider 见 `self-caller-guards`。
- basis: 用户裁决 2026-08-19（对话，四选多）· FULL `v3-review-full-2026a14.md` 与 VERIFY
  `v3-review-verify-4029b43.md` `O-1` 各记一条到期未付 · `HD-37` ②（design 形状的 rider 只点名有资格开轮的表面）

### HD-50 · 批 DTW-INDEPENDENCE：四轮独立化（取代 `HD-48` 的排期）
- 2026-08-19 · user · scope: batch:dtw-independence · status: **retired**（R1–R4 全部
  CLOSED：R1 `LEDGER-SPLIT` · R2 `XREPO-REFS` · R3 `DE-PREFIX`（2026-08-19/20）· R4
  `INIT-SURFACE`（2026-08-21，`E9` 三腿走满，rider `guard-division-home` 兑付删行）；批执行
  完毕，按本条自身「执行完 retire」于同日移入本档，四轮锚在 CONSTRUCTION-LEDGER 的 CLOSED roll。
  原 status 注记的「批的授权只活在对话里」的缺口自建条起由本条补上，随批终结）
- 裁决：用户批准四轮批（预览卡确认）：**R1** ledger 切（已收）· **R2 `XREPO-REFS`（已收
  2026-08-20，三腿走满）**——落地为「层文本不写调用者路径」的 `E10` 条款 + 四处降名 +
  `e1-disclose-home` 落座 + `E10` provenance 死从句删除；**「教守卫认全类」与 `sweep_refs.py`
  入仓经用户 2026-08-20 裁改入 R3**（R2 的 FULL `B-1` 实测守卫只判前缀形状，而 R3 去前缀时守卫
  路径模型本来就要重写，一次改到位；`HD-50` 原文把它记在 R2 名下，本次更新即 V-2 要的承载）·
  **R3** 去 `ResearchSystem/` 前缀（重扎根第②件，`E10-sync` 三处同 commit）+ 守卫认全类 +
  `sweep_refs.py` 入仓；VERIFY `O-1` 的实测入题面——守卫的缺前缀分支今天会拦 R3 自己要写的
  token 形状 · **R4** `dtw init` 命令面（`--into` 与「树里那半接线可进 init、机器那半不进」的
  判据）**＋分工收拢**（两支路径守卫的关系改为一处说、其余指过去——VERIFY `2538893` `O-5` 的 `R5`
  问题，用户 2026-08-20 裁做、搭 R4；站点清单与细节在 rider `guard-division-home`）。**R2 先于 R3 的理由已兑现**：`E10` 条款与降名先落，R3 改 `EXECUTION.md` 枚举句不再
  会被守卫按旧判据挡住。本条取代 `HD-48`：其三题两题并入 R2、一题并入 R4，`HD-48` 同 commit
  转 superseded 入 archive。
- 未入批（用户明示）：人看的根 README + LICENSE（继续 bank，rider `readme-cli-stale` 兼指其三句
  已证伪断言；诚实提醒已给——无 LICENSE 则第二人无法合法使用）· 仪器仓自跑另两支守卫
  （rider `self-caller-guards`）。
- basis: 用户裁决 2026-08-19（对话：批预览卡「ok」· B 类「降成名字」· 「继续躺 bank」）·
  supersedes `HD-48`

### HD-54 · C4 `O-1` 采样义务定读数时刻：下一产品 run 的 closeout 一次读数改判；义务安家执行者 charter
- 2026-08-22 · user · scope: one-shot（读数发生并改判后本条消耗；消耗前仍可 supersede）· status:
  **superseded**（2026-08-26 由 `HD-58` 取代——按 `HD-30` 机制：只收窄「读数时刻」一处，从下一个
  产品 run 的 closeout 改为构造轮；记录义务、三分支、载体、one-shot 消耗条件由 `HD-58` 全文承接。
  原 status：implemented，承载＝`EXECUTION.md` Authoring gate 段落——candidate `229f03f` 立段、
  修腿 `3dd226b` 修正行为主体句——+ `CONSTRUCTION-LEDGER.md` conversation-only 行；FULL
  `v3-review-full-229f03f.md` `O-6` 指出本裁决 chat-only 且 load-bearing，本条即其登记，
  `O-5`(b) 之兑）
- 裁决：C4 `O-1`（2026-08-01）的两 map 分类对照义务**不退役、也不无限收集**——每真 run 的
  review/closeout 照记一行，至**下一个产品 run 的 closeout** 一次读全已收行、按原三分支改判；
  读数前该义务作为 standing run-conduct 住执行者 charter（`EXECUTION.md`），不再靠指令 Context
  手抄（它为此手抄了五个 run）。用户的范畴框架保留：仪器把自己的研究记账挂到被测工作指令面上
  这件事，以「给研究一个 charter 之家 + 一个到期日」作答，不以留在 Context 作答。
- basis: 用户裁决 2026-08-22（对话，预览卡三问之二）· plan `document-harness/plans/executor-charter.plan.md`
  §Open question 三选项 · FULL `v3-review-full-229f03f.md` `O-6`/`O-5`(b) · journal
  `document-harness/journal/executor-charter-2026-08-22.md` · superseded by `HD-58`

### HD-56 · 契约 v4 已签署：单文件操作契约 + v4 入层 + 三源文件退役
- 2026-08-23 · user · scope: standing · status: **superseded**（2026-08-26 轮
  `CORE-SET-SIGNATURE` 由**根目录的 `CONTRACT-V4-SIGNATURE.md`** 取代——后继不是另一条 `HD`，
  而是那份独立签字记录文件：用户裁决 2026-08-25（批 `CORE-SET` 裁决 5）判签字载体迁出决策簿，
  故 `HD-30` 的「后继承载全文」由该文件承担，双向指针与本条状态翻转、与该文件的创建同一个
  commit（`HD-2`），写入授权 `HD-60` 义务③。**签字本身未变**：绑定字节仍是
  `614932de40b841ec9777719aea88de04864eb67b`，v4 不重签（批 `CORE-SET` 裁决 10）。
  原 status：live——本条曾即签字记录本身，v4 按 governance-scan 判据不携带自身审批状态，
  签字当时住这里，形状比照 `HD-35`/`HD-40`；`E2` 名单的 v4 blob 字面量与本条互为印证）
- 裁决①（签字本体）：用户签署 `contract/Document-Work-Assurance-Contract-v4.md`（轮
  `CONTRACT-V4`，经 FULL `28852a6` `CHANGES_REQUIRED` → 一次用户批准的修 `d0f185c` → VERIFY
  `REVIEWED_NO_BLOCKER`，用户自述通读全文后签署）。**签字绑定字节 blob
  `614932de40b841ec9777719aea88de04864eb67b`、sha256（blob 内容，LF，`git cat-file blob <id> |
  sha256sum` 口径，按 `HD-40` 的更正）`1b1061cb…7a23fa`，339 行**。v4 自此为唯一操作契约文本，
  合并取代三份已签源文件——v3（`b2dbdf75…`）· supersession-1（`68031fa2…`）· supersession-2
  （`e1a2f26b…`）——三者按用户 2026-08-23 确认退役入 git 历史，字节按 `HD-44` 不可写。`E2`
  冻结面自此 = v4 一件 + schema pack 十五件，共十六件。
- 裁决②（v4 入层，落簿）：v4 为 `E10` 第九成员（用户 2026-08-23 裁，答 FULL `O-2` 经 `R5`
  归口之问、履 `HD-21` 的记录义务；此前该裁决只活在修腿 commit `d0f185c` 正文，VERIFY 点名
  欠簿，本条即其家）。v4 因此处于 `HD-20` 交叉——同时 `E2` 冻结与 `E10` 成员，其字节先欠
  `E2` 的 recorded ruling。
- 裁决③（豁免退役授权）：`governance-exemptions.json` 的契约条目（blob `b2dbdf75…`）退役；
  该文件 retired 块所引的「removing decision」即本条。
- **本条转 superseded 时，②③不随载体迁移、也不重裁**：②的承载是 `E10` 成员句本身（成员句一字
  未动，`E10-sync` 不落地）；③已执行完毕，`governance-exemptions.json` retired 块仍援引本条 id，
  按状态机 `superseded` 为 grep 可达而非必读，该援引照旧解析。后继文件把这两句照记一遍，
  以免读者以为它们被静默丢掉。
- basis: 用户签字 2026-08-23（对话「签字」，签前确认两次评审均实读 v4）· plan
  `document-harness/plans/contract-v4.plan.md` D1–D10 · 记录
  `v3-review-full-5f849da.md` · `v3-review-verify-d0f185c.md` · superseded by
  `CONTRACT-V4-SIGNATURE.md`（本仓根目录）

### 2026-09-04 搬入 —— 「就地改契约族」整族 retired（HD-70 / HD-68 / HD-67 / HD-64 / HD-63）

> **为什么整族死。** 这五条都是「准予就地改签名契约 X、盖过 §13 的 in-place 禁令」的一次性授权
> （HD-63 盖签署时真后来假的陈述 · HD-64 盖对空集生效的要求 · HD-67 盖调用者不可达的历史 ·
> HD-68 盖引用形态 · HD-70 盖闭合枚举的词表扩张）。2026-09-04 用户裁：**契约 v4 的签名挂起**
> （进入活跃修订期，载体 `CONTRACT-V4-SIGNATURE.md` 的 SUSPENDED 段），故 §13 的「signed contracts
> are never amended in place」对此刻的草稿**不适用**——这一族授权的对象（撬 §13 那把锁）随之消失。
> 且今后签名文本的编辑授权是**签字记录里的一次事件**、不再造 HD（这才是它们该待的地方，呼应
> 2026-08-21「不造批准载体」裁决）。五条**无后继、终态**（不是 superseded：没有接替的 HD，是机制
> 替代 + 主题消失）。HD-70 本就已 retired；其余四条的 status 行在本次搬入时翻 retired，前一态
> `implemented`/`live` 的理由原样留在各自括号内（`HD-59`）。
>
> **`HD-6` 询问第八次触发（本次移入）**：判据实测删除的双条件合取**不成立**——五条仍被外部援引
> （`HD-63` 尤甚，rider `protected-set-says-five` 等仍写「HD-63 的类」；`HD-65` 引 `HD-64`）,
> 故第一个条件「今后不再被援引」为假；按**默认不删**执行,只搬不删。要清由用户另裁。
### HD-70 · 契约 v4 `:118` 的 VERIFY verdict 行准予就地**加一个值**——本裁**明写盖过契约 §13**，`HD-63` / `HD-64` / `HD-67` / `HD-68` 之后本族第五条，盖的对象是「闭合枚举的**词表扩张**」
- 2026-09-03 · user · scope: one-shot · status: **retired**（用户裁决 2026-09-03 二次翻态「转」：本条所欠的
  `E10` 独立复读已由轮 `CORE-MOUNT` 的开轮冷读承载——记录 `v3-cold-read-73bfe1e.md` 于 `d0d029a` 原样落地，
  其 §3 通读 `15e5ccc` 改后的契约 `:118`/`:127`、`RULES.md` `R3` 与 `REVIEW.md` 文本并判该设计 stands、
  五个站点均如裁；无后继，终态；前一态 `implemented` 的理由原样留在下文：用户裁决 2026-09-03 翻态，挪节与翻转同
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
- 2026-08-30 · user · scope: one-shot · status: **retired**（本条 2026-09-04 随就地改契约族整族转 retired（用户裁，理由见本节抬头）；前一态 implemented 理由原样留下文——用户裁决 2026-08-30 翻态，挪节与翻转同 commit 按 `HD-2`；承载 = `322fd1c`，经 FULL `8997d94` + VERIFY `8214f50` 审毕；改后文本欠 `E10` 独立复读，随轮 2 开轮冷读，复读回来后转 `retired` 归用户；原 live 理由随本条挪节留在下文括号内：层内零承载：§13 说反面；前三条各只盖自己那一类，
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
- 2026-08-29 · user · scope: one-shot · status: **retired**（本条 2026-09-04 随就地改契约族整族转 retired（用户裁，理由见本节抬头）；前一态 implemented 理由原样留下文——用户裁决 2026-08-30 翻态，挪节与翻转同 commit 按 `HD-2`；承载 = `228df32` 两块 + `322fd1c` 按 plan 裁决 22 补删 §12 ¶1，经 FULL `8997d94` + VERIFY `8214f50` 审毕；改后文本欠 `E10` 独立复读，随轮 2 开轮冷读，复读回来后转 `retired` 归用户；原 live 理由随本条挪节留在下文括号内：层内零承载：契约 §13 说的是反面；`E10` 的 design test
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
- 2026-08-28 · user · scope: standing · status: **retired**（本条 2026-09-04 随就地改契约族整族转 retired（用户裁，理由见本节抬头）；前一态 implemented 理由原样留下文——用户裁决 2026-08-29 翻态，挪节与翻转同 commit 按 `HD-2`；承载 = amendment `2aabd5a`，经独立复读 `ff00a1d` 确认；其一致性条件由 `HD-65` 答毕；原 live 理由随本条挪节留在下文括号内：`HD-63` 的边界段把「改变契约**要求什么**」
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
- 2026-08-28 · user · scope: standing · status: **retired**（本条 2026-09-04 随就地改契约族整族转 retired（用户裁，理由见本节抬头）；前一态 implemented 理由原样留下文——用户裁决 2026-08-29 翻态，挪节与翻转同 commit 按 `HD-2`；承载 = amendment `e578e70`，经独立复读 `fad8df2` 确认 must-fix 已 discharge；原 live 理由随本条挪节留在下文括号内：层内与契约内均无承载：契约 §13 说的是
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


