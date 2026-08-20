# Decision log 立项 —— 设计推演记录（2026-08-08）

> **这是什么。** 一次跨轮设计判断的推演记录，是 [`HARNESS-DECISIONS.md`](../../HARNESS-DECISIONS.md)
> 首批条目（`HD-1`–`HD-9`）的 basis。起因：批 A / A1 step 7 把七条待裁摆给用户时，用户指出
> 「context 太少」并把问题退回根上——**record 的存在是为了什么**。五轮讨论后裁决为：decision
> 独立成层。本文件按 journal 的新定位只装**分析与推理**；裁决本身在 log，待办在 plan/rider。
> 整理自 2026-08-08 对话，非逐字记录；每个转折记谁的输入。裁决全部是用户的（`E1`/`R5`）。

## 1. record 六类拆分与三留三砍

「record」在本 harness 里至少是六类不同的东西：一手观测（`chk-*.out.txt`，~6–8%）· 绑定件
（CheckResult digest / CandidateRecord digestRef / state protected pointer，~22%）· 需求件
（instruction / work-spec / check spec，~7%）· 裁决件（`user-decision-*.json`，<1%）· 评审记录
（`migration/v3-review-*.md`，22,560 行）· 设计判断（journal / commit 正文）。run 目录下的脚本
（48%）不是 record，是仪器——这一刀先切，否则 D1 会被误当记录层问题。

**三留**：①证据（不可再生的一手观测——唯一「不留就真丢」的类，仅 6–8%）· ②绑定（让断言可被
反驳的把手，价值在可质疑不在被读）· ③判断（同样能干的人拿全部字节从头做也不会自动得出的推理；
例：8ad8c2f FULL 里「additivity 义务原话对 git 行 diff 字面为假，真正成立的是更强性质」——没有
任何命令会吐出这段）。**三砍**：④可再生的方便（journal §3 已裁）· ⑤重复（第二份拷贝必 drift）·
⑥无锁证词（「我完整读了 21 份 spec」不可核验——评审记录自己声明 no evidence lock）。判据统一为
**可核验性**，且要写明**谁的决定、什么时候**。用户裁：三留三砍成立，判断需再议（→ §2）。

由此 M4 的 55% 「重推」需按新刀重切为**配方**（命令可重放，可压缩）/ **证词**（无锁）/ **判断**
（不可替代）三分——D3 的真问题是这三者的占比，原 55% 不能直接拿来裁。

## 2. 判断的四作用域，与缺失的登记处

判断不是字节属性，是关于将来的断言，位置随作用域走：绑将来所有轮→规则面 · 绑一个机制→就地
docstring（先例：`materialized_candidate`）· 绑未解问题→rider · 只绑本轮→历史（不需要家）。
**缺的不是位置，是把前三类从第四类里拣出来的坎。**实证三条：ledger 有一节就叫「已裁但只存在于
对话里的」（12 条孤儿）；「276+ 混合历史」驱动了一整条硬伤框架、八处查不到源、实测 7–12；
ledger 自标「HI-route 未闭：重扎根这条裁决同样只活在 commit 正文/台账/本行」。

用户随即把问题推进一步：**decision 能不能独立于 record**——比 raw 运行记录高维、需常查，而
journal 已被 overload（裁决+分析+待办三种生命周期挤一个文件）。三个现有家的形状全部失配：
journal 一轮一份写完即静止，decision 是活的；ledger 有 120 行硬上限（`ledger_cap_check.py`），
decision 单调增长——**有上限的文件装不下单调增长的东西，是算术不是意见**；commit 正文不可索引、
不可标注被推翻——作废的与现行的在 grep 里长得一样。裁：**decision log 就此立项**。journal 收窄
为分析/推理/实测，待办归 rider/backlog——三种东西两种已有家，新增的只有 log 一个 surface。

## 3. 设计推演的关键转折

- **必读还是按需**：session 提「plan 作者读全 live、执行轮不必读」，反例自证——本轮写 commit
  正文需要「`E8` one dense paragraph 买密度与无 trailer」这条 standing 裁决，plan 没带，靠翻
  账本才没违反；而 `ledger_cap` 那条同样被踩却有 hook 当场拦住——**有机械 enforcement 的
  standing 裁决 cold read 不需要知道，没有的必须被读到**。用户裁：**必读**，体量付得起
  （live ≈ 数十行）。决定性的附带收益（用户点出）：**plan 不再转录裁决、原样继承**——转录是
  漂移面，批 A plan 上已有两次实证（wikilink 约束被写窄、「276+」无源且错，皆转录环节出错）。
- **live 与 implemented 的分离**：用户问「机制类决定 A1 做完还 standing 吗」——暴露三态机把
  「在 force」与「需被读」混在一个 live 里。机制类裁决恰恰持续累积且全是 standing，三态下必读集
  无界。裁：**加 `implemented` 态**——在 force 但细则已由别处承载（instruction 条款/代码/模板），
  不必读、grep 可达。必读集 = live = 已裁未落实 + 无处承载，才真有界，且界在正确的地方（「无处
  承载」正是 12 条孤儿的同类）。判据一句话：**有没有别的东西在替它说话**。
- **方向**：session 曾提「被吸收的 entry 缩成指针指向 `E<n>`」，用户驳回——**log 是裁决的最高
  source of truth，instruction 反向 base on decision**。指针化会让 log 丧失发现 instruction
  漂移的能力（改了 `E2` 正文，指针会默默「变成」从未裁过的内容）。改：entry 永远装裁决原意
  （一句），instruction 装展开的细则；细则与裁决冲突 → 细则错。
- **implemented 放哪**：用户问是否移 archive。答：留本文件 §implemented——若进 archive，archive
  会大部分不可删（implemented 是现行规则的出处），「>100 行询问删除」将反复触发而无真候选。
  按**在不在 force** 切文件：本文件=在 force（live+implemented），archive=只装死的。
- **scope 的用途**：到期条件（让 entry 能死，否则 log 是下一个 120 行问题）+ grep 档位过滤。
  session 原提的第三用途「读取路由」被用户驳回（plan 已继承相关裁决，执行轮不依赖 standing 检索）
  ——撤回。`batch` 档**限构造轮/设计批**：session 先举 p5b R0 为「约束型」例，用户指出类别错误
  ——那是轮次 scope 声明，冻在 instruction + START 批准里，是比 log 更强的家。产品 run 有控制面
  故不用此档；构造轮没有，`batch` 为它们存在（装排期与成批裁决，执行完即 retire=主题消失）。
- **颗粒度**：三问（绑下一轮及以后？/ 推翻或收窄已有裁决？/ 用户裁决且无别的家？）任一为是即进；
  反向排除（轮内约束→instruction+decision json / 收口处置→user-decision json+rider / 会话判断
  →journal / 可重算事实→非 decision）。**一条 = 一件能被独立推翻的事**（status 各自独立变），
  故 D1–D7 是七条。rider 与 decision 正交：未解的问题 vs 已裁的约束。
- **删除**：session 原判据「零入边可删」被用户戳破——**援引先例不产生 supersession 边**（先例
  追认 / 同款形状 / 同向，仓库三例俱在），未来价值不可机械判定。裁：**人判、默认不删、双条件
  合取**（今后不会再被援引 ∧ 能从 record 反推——用户补第二条件），触发=archive **>100 行时
  询问一次**（用户定：grep 本身是 select 机制，archive 大不影响使用，删除既贵又没必要，触发线
  设高）。`superseded` 链永不可删（理解现行规则需知它取代了什么——`E2` 动词例）。压力本在
  live 集不在 archive，删除是可选卫生非必需机制。
- **状态机四态三不变量**：live → implemented → superseded/retired，live 亦可直出终态。不变量：
  同一主题至多一条 live（log 的全部意义）· supersession 两处同 commit（分开做有「两条/零条
  live」窗口——`9dcb783` B-1 的 dangling-neighbour 形状）· 终态不可逆（复活=开新条引用旧 id，
  历史保持单调）。live→implemented 也是落实 commit 同步挪节（与 rider「兑付=同 commit 删行」
  同形）。只有用户能翻状态；`one-shot` 消耗前仍可 supersede，消耗后翻案无对象。
- **历史不迁 / 无 lint**：均用户裁。代价照记：ledger 12 条孤儿继续留在 120 行上限压力下，log
  保护不到；无 lint 意味着字段完整性靠纪律。「唯一靠人不靠结构的地方」=「今后不会再被援引」
  这个判断可错——正因此它必须人判+默认不删。

## 4. 与既有条目的关系及诚实边界

- `SIMP-D` 三分工（journal 理由 / ledger 指针 / commit 本轮）被四面分工取代：journal=分析 ·
  ledger=指针 · commit=本轮理由 · **log=裁决**。`SIMP-D` 是 pre-log 裁决，按「历史不迁」不建
  条目、不画 supersedes 边，取代关系记在 `HD-1` 正文。批 A 的 **D4 因此已答**（三分工不续存，
  被四面取代），七条待裁剩六条。
- 本轮（decision-log 构造轮）与 `C1` 同欠：`E10` 开轮 cold read + 独立评审。dispatch 仍被并发
  脏树挡住（本 worktree 另一 session 在改 P5C-P8 plan）。**落轮不等于评审过。**
- 本文件由 session 整理自对话，选材与措辞是 session 的判断；若与用户原话冲突，以对话与 log
  条目为准。
