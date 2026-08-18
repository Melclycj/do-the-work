# HARNESS DECISIONS — 裁决登记簿（v3 harness track）

> **这是什么。** harness 的用户裁决的**最高 source of truth**。instruction 层反向 base on 这里的
> 裁决展开细则；细则与裁决冲突，细则错。每条 entry 只装**裁决本身**（一句）+ 元数据；理由进
> journal（经 `basis` 指针可达），待办进 rider/backlog，轮内决定归该 run 的
> `user-decision-*.json`（digest 绑定，比本文件强，不重复登记）。
> **谁读**：每轮 cold read **必读 §live**（且仅 §live）；写 plan / 开设计批时读全部 live 并
> **原样继承**进 plan，不转录改写；执行中撞上计划外的事，按需 grep 本文件与 archive。
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

### HD-44 · `E2` 冻的是**字节**，不是「本仓的这些路径」——故整体搬仓不是写，不欠裁决
- 2026-08-18 · user · scope: standing · status: **live**（`E2` 正文只说「三个 blob 加一个目录，
  都由 inspection 可判」，没说这些路径必须留在哪个仓；跨仓之后这个歧义第一次咬人，而层里无承载。
  要转 `implemented` 须有一个设计轮把「冻结面住哪」写进 `E2`）
- 裁决：`E2` 冻结的对象是**那些字节**（contract `b2dbdf75` · supersession-1 `68031fa2` ·
  supersession-2 `e1a2f26b` · 再基线时 schema pack 的十五件）。**字节完好地存在于某处、且被
  gitlink 钉住**时，把它们从某个仓移走**不构成 `E2` 意义上的「写」**，因而不欠 `E2` 的记录裁决。
  反读法（冻的是「本仓的这些路径」，故删除是一次未经裁决的写）**被否**。
- 后果：**冻结面自 2026-08-17 起住在 harness 仓**，与命名它的那条规则同仓——这是本条要留下的
  那个事实，因为拆分后「`E2` 说的那些字节在哪」不再不言自明。调用者仓以 gitlink 钉住哪个
  revision，冻结面就是那个 revision 上的这十八件。今后任何调用者删掉自己那份副本，按本条同样
  不欠裁决；**真的改动那些字节仍然照旧欠裁决**，本条一个字都没放宽那一半。
- basis: 用户裁决 2026-08-18（对话）· FULL `v3-review-full-2d148f3.md` `B-4` 提出两读法并按 `R5`
  归口用户 · 先例 `HD-39`（删除轮把 `E2` 的理由写出来）与 `HD-20`（冻结的意义就在必须有裁决）

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

### HD-28 · 新仓成员（`HD-16` 的收窄后继）：A 仪器 + B=decisions/riders+decisions-archive + C 评审记录；ledger 留调用者
- 2026-08-12 · user · scope: standing · status: **implemented**（成员集已由
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
  再执行」在 `HARNESS-LEDGER.md` 拆分批 backlog 行原文；rider `CLI-hist` 的随批归属在其
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
- 2026-08-08 · user · scope: standing · status: implemented（`E10` 自由通道句的 `E2` 例外承载，
  同 commit；rider 行同 commit 删）
- 裁决：同时被 `E2` 冻结又是 `E10` 成员的路径（现仅 `paragraph-map.schema.json`），其字节**先欠
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
