# Checkpoint read #1 — `94a97f5` (`V3-CONTRACT-DISCIPLINE-AMENDMENT-v1`) — findings

**Status: review-side authored (the first checkpoint read under the discipline the subject
commit itself introduces), relayed by the user, committed by the execution side.** Not a node
artifact; sits at the migration root outside every node allowlist; bears on no node verdict.
Reviewer: a single general-purpose agent, model explicitly `fable`, read-only, in a session
independent of the execution session; dispatched with subject SHA + charter + ground-truth
coordinates only (no executor pass-argument), per operating-contract rule 1 / review-contract
§12.

Execution-side framing, disclosed: the user's relay carried a duplicated tail (paste
artifact) — the duplicate block is collapsed here, keeping the more complete second copy of
the dispatch-note list; a session-environment hint at the tail (`claude-env-bootstrap`) is
omitted as non-review content. The reviewer's report is reproduced **in condensed form**; its
substance — each finding's meaning, severity, and minimum fix — was **confirmed unaltered by
checkpoint read #2** (section appended below; this sentence was corrected from an earlier
"reproduced verbatim" over-claim, read #2 finding R1). The user's dispositions of 2026-07-22
are appended at the end.

---

## Findings

**F1 — 事实性 precedent 错误（最重，必修）：** 两处把污染 round 2 的 amendment 写成了
"amendment 2"——operating contract 新 rule 1 与 review contract 新 §11 precedent 行。但按
N3 record §8 自己的编号：污染源是 amendment 1 (`55133a9`)（其 diff 逐字含两个 worked
example）；`eca4902`（编号 2）晚于 round 2，是修掉污染、且首个接受 checkpoint read 的
amendment。这句话把范例反转了——把 checkpoint read 的 subject 说成 unreviewed 污染源；
precedent 行的功能恰是让规则可证伪，读者对着文中所引 ground truth 核对会直接撞矛盾。
custody note §4 与 review contract §12 用不带编号的 "the one unreviewed amendment" 写对
了，只有这两处错。最小修复：改为 "the unreviewed first amendment (`55133a9`)" 或去掉编
号——属两词级 corrective edit，本身是 instruction-layer amendment，按 rule 1 需再过
checkpoint read。

**F2 — 两 contract 的 layer 定义分叉：** operating contract 定义含 "(including prose
carried in schema `description` strings when amended)" 括注，review contract §12 的定义没
有。分歧恰落在"何时欠一次 checkpoint read"的 scope 词上，且较窄定义在执行 read 的一
侧——纯 schema-description amendment（正是 `eca4902` 的一半）在执行侧明确属 layer，评审
侧可读成不属。最小修复：把同一括注补进 §12（additive 一个从句）。

**F3 — 锚点错误：** operating rule 2 把 "yielded C1–C5 in 590 lines" 引到 custody note
§4；实际 C1–C5 在 §2，590（=29+92+214+255，重算成立）在 §0/§8；§4 是 "reader's question
decides the yield" 原理。最小修复：锚点改 "§§0–2" 或引整个 note。

**F4 — hint 级自指：** 两条新 provenance 注自述其授权（"at the user-gated boundary named
by the ADOPT_DOCUMENT_V3 ruling"）——按 §10 属无 evidence lock 的 process claim。降为
hint 的理由：append-only 带日期 provenance（非会漂移的 live state）、已指向授权记录、符
合两文件既有惯例、其可验证一半（additive-only）reviewer 重算为真。Ceiling：
user-instruction 一节无法向任一方向核实。如要修：改纯 pointer 形（"authorization: N3
record §8 ADOPT entry"）。

## Observations（非缺陷，供用户裁定）

- **A：** ruling 未定而由 amendment 落定的四点全部摆在明面且与先例一致——(i) layer 定义把
  amended schema-description prose 计入（超出 N3-R10 定义句字面，但与测量基础及 custody
  note §1 一致）；(ii) "commit first — the read binds committed bytes"；(iii) 两种 read 均
  不耗 plan-§8 budget、不带 node verdict；(iv) anti-renaming 双向适用。建议知情批准；批准
  则无需改文。
- **B：** "each node boundary" 原样继承 ruling 用词，V3-N0..N4 已全关，未来指涉
  （derivative round / post-v3 运行边界 / 未来 construction node）是 ruling 自身的开放
  项——amendment 替用户决定反而越权。建议下次边界事件出现时由用户定。

## Reviewer 重算清单（未采信任何报告数字）

Additivity `git show --numstat` = 71 插入 0 删除、无 rename ✓；590 拆分 ✓；`eca4902` 内容
与 3 defects 由 `c07d682` 修复 ✓；"C1+C2+C3 batch at N4 is the model" 对 `1e6dde9` 与 N4
record §4 逐项对应 ✓；与两 contract 既有条款无矛盾（§7 与 §12 standing-authorization 句已
显式调和）✓；全套件自跑 404 绿 + repo-audit exit 0（对本 prose-only subject 无绑定力，仅
证未破坏他物）。

## Reviewer 建议路由

F1 必修；F2、F3 与 F1 同一批 corrective amendment（符合 rule 3 batch 纪律），落地后按
rule 1 再过一次 checkpoint read；F4 + 两条 observation 交用户裁定。

## 派发说明（技术附录）

- 派发前核实：`94a97f5` parent 确为 `646d8f0`；review contract、N3 record、custody note
  三个 ground-truth 文件在 parent commit 均存在。
- 用户粘贴的 prompt 有六处粘贴截断，**派发侧在把 prompt 交给 reviewer 之前**按前言明说的
  意图做了最小机械修复（未加任何内容转述；reviewer 收到的 prompt 六处均已完整——本条归属
  由 read #2 finding R2 修正）：① "gitthis dispatch" → 补全为 `git show 646d8f0:<review-contract path>` 读
  法 + "NOT the worktree/HEAD version"；② "It ies no plan-§8 budget" → "carries no
  plan-§8 budget"；③ "row N3-R10 — wh" → "— where that standing discipline is recorded"；
  ④ "the N3 record fites" → "the N3 record files it cites"；⑤ "silently deciding a" →
  "silently deciding anything the ruling left open"；⑥ "Eacviolates" → "Each finding: what
  it violates or risks + the minimum fix"。
- Reviewer：单个 general-purpose agent，model 显式 fable，read-only（自称未编辑任何文件，
  与派发约束一致）。Agent ID `a31d92d35ddf6fb1a`，如需追问可续同一 context。

---

## Dispositions (user, 2026-07-22)

- **F1–F3:** fix boundary **approved** — one corrective batch
  (`V3-CONTRACT-DISCIPLINE-CHECKPOINT-FIX-v1`), then checkpoint read #2 per rule 1. The
  execution side independently re-verified all three against N3 record §8 (the `55133a9`
  entry at its own log line) before proposing the boundary.
- **F4:** **fix in the same batch** — both provenance notes to pure pointer form.
- **Observation A:** **informed approval** of all four settlements; no text change.
- **Observation B:** **deferred** to the next real boundary event; the open item is held in
  `.goals/LEDGER.md`'s live pointer, and the contracts stay silent on it until the user rules.

---

## Checkpoint read #2 (2026-07-22) — the fix batch, and this record

Subjects: `f6a7bf8` (`V3-CONTRACT-DISCIPLINE-CHECKPOINT-FIX-v1`) and `fdd2f9d` (this record
file). Same-reviewer continuation — a verify-shaped read of its own prescribed minimum fixes,
per the targeted-VERIFY precedent; instructions read at the subject's parent per the
anti-circularity convention.

**Contract fixes — all four verified, no new defect:**

- **F1** — both sites now read "the unreviewed first amendment (`55133a9`)"; re-checked
  against N3 record §8, still correct; repo-wide grep for the wrong attribution: zero
  residue; the correct `eca4902` → `c07d682` references untouched.
- **F2** — §12 carries the same clause (comma-clause on the review side, nested parenthetical
  on the operating side — literally consistent, no divergent reading).
- **F3** — citation widened to the whole custody note, one of the two prescribed options; no
  other wrong anchor remains.
- **F4** — both provenance notes in pointer form; each appended correction clause is accurate
  per-file against the actual diff and links this record; the 14 deletions are targeted
  correction (the `c07d682` shape), not a rule-3 rewrite.

**The rule-1 obligation on `94a97f5` and `f6a7bf8` is discharged; the contracts may be relied
on.**

**Transcription findings against this record file** (a provenance record, not instruction
layer — no schema validates it, nobody acts on it as instructions, so no rule-1 re-read is
owed), both fixed in the commit carrying this section:

- **R1** — the header claimed the reviewer's words were "otherwise reproduced verbatim"; the
  body is in fact a condensed reconstruction (a conclusions-summary section absent; finding
  layering flattened; several re-derivation items dropped). Substance — every finding's
  meaning, severity, and minimum fix — confirmed unaltered by this read. Header reworded.
  Ceiling: whether the condensation happened at relay or at record-writing is not visible to
  the reviewer.
- **R2** — the dispatch appendix attributed the six paste-truncation repairs to the reviewer;
  they were the dispatching side's act before the prompt was handed over — the reviewer
  received all six sites intact. Re-attributed.
- **R3** (observation, outside subject) — the Obs-B deferral pointer existed only in the
  uncommitted `.goals/LEDGER.md`; resolved by committing the LEDGER alongside this
  correction, giving the deferral a durable home outside this record.

Ceilings carried: the two disclosed header edits (duplicate-tail collapse, omitted session
hint) concern the user's paste, which the reviewer cannot see — unverifiable in either
direction; the dispositions section is consistent with the dispatch summary.
