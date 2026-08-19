# Plan: E2 动词改写 + E10 open-tail 钉死（一个构造轮，三处编辑，一个文件）

- **slug**: e2-verb-e10-pin
- **created**: 2026-08-04
- **complexity**: 中等（编辑面 1 文件 / 3 处；但仪式是一个完整构造轮：预览卡 → 候选 → 独立 FULL → closeout）
- **status**: done（2026-08-04 closeout；FULL `REVIEWED_NO_BLOCKER`，三条 low 按用户裁决落 ledger/riders）
- **base_commit**: 6178330430f2201f02700aecbcdfc42254c494de
- **base_branch**: document-work-assurance-v3

## Goal (one line)

把 `E2` 的动词从「任何写入都禁」改成「不得无裁决写入」，并把 `E10` 的层成员从「八个 + 开口尾巴」钉死为
写死的九个，使规则文本与守卫实际执行的东西一致。

## Why / value

- **E2**：改 15 个 schema 里的任何一个，今天没有合法路径 —— 规则说 untouchable，给的两条出路
  （in-boundary 修法 / 停在 `SPEC_GAP`）都不让你改它。实践里走的是「用户裁决重开冻结」这条**不在规则里
  的第三条**，已用两次（rider `O-2b` 一次、`c05d052` 一次），每次都是靠先例办的特例。改完之后这条路
  写进规则，措辞类 schema 改写从「特例」变成「一次裁决 + 全电池」。
- **E10**：散文承诺「any later prose successor…including schema `description` strings when amended」
  自动成为层成员，**而守卫根本实现不了** —— `layer_path_check.LAYER` 是写死的九元组，
  `test_precommit_checks.py` 的 `LayerMembership.EXPECTED` 是手写的九路径字面量与之对账。散文比守卫
  多承诺了一截，`v3-checkpoint-read-d01615b.md` 的 L-1 记的就是这个。钉死 = 散文停止承诺守卫不做的事。
- **附带**：兑掉 ledger「未结」里的 `read O-1（E10 open-tail pin 与否）`。

## Context to resume cold

### 这一轮改哪个文件

只有 `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md`（层成员 1，blob `2108635f` at base）。
**不碰代码、不碰测试、不碰 schema。**

### 三处编辑

| # | 位置 | 现状 | 改成 |
|---|---|---|---|
| 1 | `E2` 开头动词 | `Frozen bytes are **untouchable**, and the list is exactly this: …` | `These bytes are **not written without a recorded user ruling**, and the list is exactly this: …`（清单本身、`ls` 可判定句、"未列即不冻"句、"别处声明的边界不独立生效"句 **全部原样**） |
| 2 | `E2` 菜单句 | `When the cleanest fix needs one, take the in-boundary fix and record why, or stop with SPEC_GAP.` | 三分支：`… either take the in-boundary fix and record why, or obtain the ruling and write under it, or stop with SPEC_GAP.` |
| 3 | `E10` 成员句 | `The instruction layer is this file, README.md, EXECUTION.md, REVIEW.md, the two retired contracts' stubs, the contract supersessions …, and any later prose successor to text this harness governs, including schema description strings when amended.` | 写死九个成员（= `layer_path_check.LAYER` 的九项，**含** `paragraph-map.schema.json`），删掉开口尾巴 |

**编辑 2 是必须的，不是可选的**：动词一改，菜单句就悬空（规则同时说「有裁决可以写」和「需要写时只有
这两条路、而其中没有拿裁决」）。这正是本轮之前 `9dcb783` 被 FULL 打回的 B-1 形状 —— 改一句把邻居晾着。

**编辑 3 采用的是代码里已有的那九项，所以零代码 delta**：散文是被拉去和 `LAYER` / `EXPECTED` 对齐，
不是反过来。执行时先跑 `sed -n '/^LAYER/,/)/p' ResearchSystem/tooling/hooks/layer_path_check.py` 取
准确九项，不要凭记忆抄。

### 用户已裁决的边界（2026-08-04，只存在于对话里，此处是唯一记录）

- **`O-2b` 不做** —— `local-check-spec` 的 description 措辞不在本轮兑。它换文件、会把 tier 从 doc-only
  翻成碰 schema 面（欠全电池），且本身不急。留在 bank 里，动词改完后它的障碍自动从「须裁决重开」降为
  「欠一次裁决」。
- **`paragraph-map` 的双闸不动** —— 它继续同时是 `E2` 冻结件和 `E10` 成员，因此**留在钉死的九人名单
  里**。钉死正好把这个双闸从「意外造成」变成「明写」，与该裁决同向。
- **不捆 `PD` / `RA` / `CLI-hist` / `F-c` / `SCC` / ④审计拆层** —— 都在别的文件，redeem-when 不匹配。
  `PD` 的 redeem-when 写的是「下一个碰 **`E2` 冻结面** 的批」，而本轮碰的是 **`E2` 的条文**，不是被冻
  的字节，**严格不匹配**。

### 一个看起来矛盾、其实不矛盾的点（**执行者必读，否则会在这里卡住**）

2026-08-04 用户曾裁决 `E2` 的「第三出路」**不写进正文**（源自 `v3-review-verify-c05d052.md` 的 O-1）。
本轮编辑 2 却在菜单句里加了第三分支 —— 看似翻案，实则不是：

- 那次裁的是「在**保留 untouchable** 的前提下，要不要**额外**加一条例外」→ 裁：不加。
- 本轮把动词整个换掉，「拿裁决后写入」**不再是例外，而是唯一的常规路径**。菜单句必须反映这一点，
  否则就是编辑 1 留下的悬空。

**两条裁决一致，不需要重新请示。**

### 冷启动读什么

1. 本文件
2. `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` —— `E2`（约 25-38 行）与 `E10`（约 73-101 行）
3. `ResearchSystem/HARNESS-LEDGER.md` 的当前指针 + 未结栏
4. `ResearchSystem/migration/document-work-assurance-v3/v3-review-verify-c05d052.md` —— 它的 O-2 里有
   **九个层成员在当前的 blob id**（`paragraph-map` 已变为 `09aa8699`），是本轮开轮 cold read 的**引用
   对象**；`v3-checkpoint-read-22b27aa.md` §1 那张表已过期（仍写旧的 `c2b713bf`），**别引它**

### 治理机制（照做，别自创）

- **`E11`**：开轮前渲染预览卡，等用户确认
- **开轮 cold read**：`E10` 允许引用 discharge —— 九个成员 blob 若与上面那份 VERIFY 记录逐个相同即零预算，
  **落候选前现验一次**（`E3` measure-last）
- **`E9` 预算**：一次 FULL + 至多一次用户批准的修 + 一次 targeted VERIFY
- **派发**：`python ResearchSystem/tooling/rsc.py v3 dispatch --range <base>..HEAD`，把打印出来的
  prompt 交给用户，**由用户另开独立 session 跑**（`R1`：executor 派的 subagent 算自查，顶不了独立评审）
- **冻结窗口**：dispatch 会写 `.harness/review-pending.json`；从派发到评审记录落地，分支只能落那一份记录
- **`E8`**：显式 path 暂存、新 commit 不 amend、不 push、标题 `V3-<ROUND>-v1`、正文一段无 trailer、
  写明 kind（candidate / review fix / record / closeout）
- **round 名**：`E2-VERB-E10-PIN`
- **tier**：**doc-only**（一个 .md，在 schema/tooling/generated 树之外）。BATTERY-TIERING 的例外
  （「code enumerates or tests pin」）**不适用** —— `layer_path_check.LAYER` 枚举的是**路径**且路径不变，
  `test_precommit_checks.py` 只把本文件名当 TempRepo 里的手写字面量。先例：`v3-review-full-22b27aa.md` §1
  的重分档。故只跑批次专项检查（三个 tracked guard + commit 时的 repo-audit），**不欠全电池**

## Constraints / Out-of-scope

- 只改 `CONSTRUCTION-CHECKLIST.md`，三处。**其余一个字节不动。**
- 不碰 `layer_path_check.py`、`test_precommit_checks.py`、任何 schema、任何 `E2` 冻结件
- OUT：`O-2b` 的兑付 · `paragraph-map` 双闸的拆解 · `PD`/`RA` 接线 · 契约 v4（另有 ledger backlog 条目）
- OUT：任何 `E10` design 测试本身的改动（本轮不碰 design 句 —— 那是 `E10-D-NARROWING` 已撤回的题目）
- 不 push（user-gated，2026-07-30 裁决）

## Steps

- [x] 1. 冷读：本文件 + `E2`/`E10` 现文 + ledger 指针 + `v3-review-verify-c05d052.md` 的九 blob 表
- [x] 2. 现验开轮 cold read：九成员 blob 与该记录逐个比对，相同则引用 discharge（`E3`：落候选前跑，不用旧数）
- [x] 3. 从 `layer_path_check.py` 取准九项路径（不凭记忆）
- [x] 4. 渲染 `E11` 预览卡（含三处编辑的确切字面），**等用户确认**
- [x] 5. 落三处编辑；机检：`git diff --word-diff=porcelain` 看清增删 token；三个 guard 各 exit 0
- [x] 6. 提交候选，标题 `V3-E2-VERB-E10-PIN-v1`，kind: candidate；正文写清 tier 判定 + cold read 引用 + token 账 → `838c413`
- [x] 7. `rsc v3 dispatch --range <base>..HEAD`，把 prompt 交给用户开独立 session → range `3b7ebe2..838c413`
- [x] 8. 收到评审记录 → 删冻结标记 + 同一动作提交记录（`V3-REVIEW-RECORD-E2-VERB-E10-PIN-<sha>-v1`）→ `c667d08`
- [x] 9. ~~若 `CHANGES_REQUIRED`~~ **不触发** —— FULL 返 `REVIEWED_NO_BLOCKER`（0 blocker / 3 low / 2 观察），
      修腿与 VERIFY 均未动用
- [x] 10. closeout：更新 ledger（兑掉未结的 `read O-1`；记录本轮结果与仍开着的观察），标题
      `V3-E2-VERB-E10-PIN-CLOSEOUT-v1`。**先腾再加** —— ledger 有 120 行硬上限，落前 `wc -l`

## Acceptance (done = ?)

- `CONSTRUCTION-CHECKLIST.md` 三处已改，其余字节不变（`git diff` 只有那三处）
- `E2` 不再出现 `untouchable`；菜单句含三分支
- `E10` 成员句枚举九项，与 `layer_path_check.LAYER` **逐项相同**（用命令对账，不用眼看）
- 独立 FULL 返 `REVIEWED_NO_BLOCKER`（或 `CHANGES_REQUIRED` → 修 → VERIFY 返 `REVIEWED_NO_BLOCKER`）
- 三个 tracked guard + repo-audit 全 exit 0；ledger ≤120 行
- ledger 未结栏的 `read O-1（E10 open-tail pin 与否）` 已删除（兑付）
- closeout 已提交，工作树干净

## Resume pointer

**本轮已结（2026-08-04）。** 链条：记账 `3b7ebe2` → 候选 `838c413` → FULL record `c667d08`
（`REVIEWED_NO_BLOCKER`，0 blocker / 3 low / 2 观察）→ closeout。`E9` 预算只花了那一次 FULL，
修腿与 VERIFY 均未动用。

**L-2 已讨清（2026-08-04，本计划之外的追加一步）**：layer read `c68d3d4`（subject `838c413`，
0 must-fix / 1 low / 1 观察），处置 `7ef4ed4` 已删掉 ledger 未结栏那条。**不再阻挡 P5B。** 该 read
另兑掉 ledger 的 bytes-channel 欠读，并把成员 4 `REVIEW.md` 的引用链读断（259 行端到端，后续轮可引）。

**留给下一轮的两条 rider**：`E10-sync`（FULL 的 L-3，三处成员同步、散文腿无守卫，deadline=铸契约 v4
那一刻）· `E2-FC`（read 的 L-1，成员 9 同处 `E2` 冻结面与 `E10` 成员表，换动词后两规则对同一动作给
相反答案，deadline=下条对该文件供字节的 finding 或下批碰 `E2`/`E10` 文本，孰先）。

## Notes

### 执行期偏离与新事实（2026-08-04 执行 session 记）

- **base 前移**：`6178330` → `b075d25`。其间三个 commit（`fd71c8e` 本计划、`6383091`、`b075d25`）
  只碰 `.goals/LEDGER.md` / 本计划 / `HARNESS-LEDGER.md`，**未碰编辑面**，故计划正文的编辑字面全部仍然成立。
- **计划第 2 步的引用 discharge 假设只有 8/9 成立**。计划写「九成员 blob 与 VERIFY 记录逐个相同即零预算」。
  实测：成员 1-8 的 blob 与 `v3-checkpoint-read-22b27aa.md` §1 那张表逐个相同 → 引用成立。**成员 9
  `paragraph-map.schema.json` 不成立**：现 blob `09aa8699`，而那份**读**记录写的是 `c2b713bf`；唯一写了
  `09aa8699` 的 `v3-review-verify-c05d052.md` 是 **VERIFY 记录不是 read 记录**，`E10` 的引用 discharge
  要求 "a recorded end-to-end read"。故本 session 实读该文件 44 行。这正是该 VERIFY 的 O-2 预言的第二笔成本；
  计划第 4 条冷启动清单把它写成「引用对象」是**措辞过宽**，此处更正。
- **`E11` 卡上用户裁的两处字面（2026-08-04）**：① 编辑 1 开头用 **`Frozen bytes`** 而非计划表里的
  `These bytes` —— 后者在规则首句无先行词，且 `E2` 下文尚有 3 处 "frozen by this rule"、rider `O-2b`
  也写「属 `E2` 冻结面」，换名词会造成内部不一致；只换动词。② 编辑 3 **保留** "prose successors to signed
  text" 作为成员 7/8 的同位语。
- **钉死的一处已知残留（不修，仅披露）**：`supersession-2` §5 写「Under `E10` it is a **prose successor**
  to signed text and owes an independent read」。删开口尾巴后 `E10` 本可不再有该词汇 —— 上面裁决②把词汇
  留住，交叉引用因此不断。即便断了也只是 `R9` wording-level（它是明写成员 #8，读的义务来自 `E10` 另一条，
  动作不变），且它本身是 `E2` 冻结件、改它反要一次裁决。
- **顺带效应（不动，仅记）**：编辑 1 落地后 rider `O-2b` 的 redeem-when「须裁决重开」实际降为「欠一次裁决」。
  本轮不兑、不改 `HARNESS-RIDERS.md`，只写进 candidate 正文供 FULL 核。
- **机检实测**：`git diff` 19+/10−，仅 `CONSTRUCTION-CHECKLIST.md`；九路径与 `layer_path_check.LAYER`
  逐项相同（脚本对账，非眼看）；三 guard 与 `repo-audit` 全 exit 0；ledger 119 行 —— **closeout 必须先腾再加**。

- **此工程的更大背景**：这一轮属于 v3 document-work-assurance harness 的构造侧。真正在排队的主线是
  **P5B**（`ResearchSystem/HARNESS-LEDGER.md` 的 ⛔ 前置栏：① 已关闭，只剩 ② —— P5B 需要自己的
  owner-batch firewall amendment + 用户签字）。**本轮可以在 P5B 之前顺手做完，也可以让路。**
- **P5B 的实质已摸清**（若先做 P5B 需要知道）：它铸 13 个 Claim + 2 个 GapHypothesis（P3 冻结的 17 个
  load-bearing 单元减去 P4 已铸的 2 个）；最硬的 OPEN 问题是 schema 卡着 load-bearing Claim 必须
  要么指向真实 `EvidenceRecord`、要么标 `evidence-insufficient`+`blocker`，而证据登记按计划归 P5C。
- **另一条 ledger backlog**：契约 v4（把 s1/s2 合并回一个文件）。§13 已允许，不需改 §13 也不需 s3。
  真代价是签 v4 前要整份读一遍。与本轮无关，别混。
- **一条已知的、不可原地修的错**：commit `6178330` 的正文写了 ledger "at 115 lines"，实测 117
  （`E3` 违规，我用了预测值而非重跑）。commit 正文不可 amend，按 L3 先例**记录不追改** —— 下次碰
  ledger 时可带一条 errata。
- `.goals/` 在**本仓库是 tracked 的**（不是默认的 gitignored 约定），所以本计划文件会进版本库。
