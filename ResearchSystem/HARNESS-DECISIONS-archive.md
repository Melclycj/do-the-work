# HARNESS DECISIONS — archive（只装死条目）

> 从 [HARNESS-DECISIONS.md](HARNESS-DECISIONS.md) 移入的 `superseded` 与 `retired` 条目，
> 原文照搬、不改写。不在任何必读范围内，grep 可达。本文件**超过 100 行**时询问用户一次
> 要不要清（删除双条件合取 + 默认不删 + superseded 链永不可删，见主文件头部 HD-6）。
>
> **`HD-6` 的询问第二次已付：2026-08-14（`HD-24` 移入、128 行），用户未答；按 `HD-6` 的
> 「默认不删」执行——不清。下次触发点仍是下一次有条目移入本档时。**
> **第一次：2026-08-13（104 行触发），用户裁「不清」。** 判据实测：
> 七条全部仍被外部援引（`HD-11` 46 · `HD-14` 42 · `HD-16` 40 · `HD-12` 33 · `HD-17` 22 ·
> `HD-13` 17 · `HD-26` 16 · `HD-29` 8 处，`grep` 排除本文件自身），故删除的第一个条件
> 「今后不会再被援引」对每一条都不成立；其中三条 superseded（`HD-16`→`HD-28` · `HD-26`→`HD-31` ·
> `HD-29`→`HD-33`/`HD-34`）另受「链永不可删」保护。下次询问的触发点是**下一次有条目移入本档时**。

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
