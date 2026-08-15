# Split-batch R0 — read of the free-channel application `6208b35bbe61ad6a5aefab33f81e7fb30ea09e82..0cc45ce07c5c19c2fceecba77c77fc4ed63d1529`

Independent read of the `E10` free-channel byte application answering the R0 read's `L-1` /
`L-2` / `L-3` / `O-1` / `O-2` / `O-5` (source record `feb7b48`, `v3-checkpoint-read-ffbc393.md`).
**Not a round** (`R3`, `E9`'s free-channel clause): no verdict, no budget consumed. Output is
findings tiered must-fix / low / observation.

**Findings: 1 must-fix, 3 low, 5 observations.**

Every figure the commit writes was re-derived here, none accepted as reported. Five of the six
applications are exact: the corrected `sha256`, the seven `_cmd_v3_*` functions and their offsets,
the 421-line block with coupling 0, the ten-item `EXCLUDE`, the 33/32/171/138 arithmetic, and the
three docstring lines. `L-3`'s diagnosis is better than the source read's — that read could not
reproduce 337/724 under any composition it tried; the executor found the cause, and both halves
reproduce here exactly (see §6).

The must-fix is not in the corrected bytes but in the sentence they exist to support. The
conclusion this commit newly vouches for — *结论不受影响* — covers a `split-design.md` §1 /
journal §1 claim that is false at file scope: `rsc.py:850` couples to `stage_control` outside the
top three imports and outside the measured block, and `HD-39` ①'s connected list does not name it.

**Process disclosure, stated up front because it bears on independence (`R4`).** An uncommitted
record for this same subject SHA, written by an earlier session, was already present in the
worktree when this read opened (`v3-checkpoint-read-0cc45ce.md`, 24968 bytes,
`sha256 0483aeb1…956c`). I completed the whole derivation before opening it, then read its
headings and opening summary to resolve the write collision at `R6`'s fixed path. It named a
must-fix I had not found; per `E12` I reproduced that finding from the repository rather than
adopting it, and §3 below rests only on commands run here. Its bytes are preserved outside the
repository at
`…/scratchpad/PRIOR-SESSION-v3-checkpoint-read-0cc45ce.md`; this file replaced it at the canonical
path. The overlap between the two records is therefore **not** independent corroboration on §3, and
is marked as such.

## 1. Subject, re-derived (`R2`)

```
$ git rev-parse HEAD                     -> 0cc45ce07c5c19c2fceecba77c77fc4ed63d1529   (== subject tip)
$ git rev-list --count 6208b35..0cc45ce  -> 1
$ git status --porcelain                 -> ?? ResearchSystem/migration/document-work-assurance-v3/v3-checkpoint-read-0cc45ce.md
$ git diff --numstat 6208b35 0cc45ce
6   1   ResearchSystem/HARNESS-DECISIONS.md
13  6   ResearchSystem/document-harness/journal/repo-split-r0-2026-08-13.md
21  8   ResearchSystem/document-harness/split-design.md
```

One commit, three files, +40 / −15. Paths classified by hand:

| path | class | governed by |
|---|---|---|
| `ResearchSystem/HARNESS-DECISIONS.md` | decision register, **not** an instruction-layer member | `HD-19`, `HD-7` (discipline), `HD-2` (only the user flips state) |
| `ResearchSystem/document-harness/journal/repo-split-r0-2026-08-13.md` | round record (measurement) | `HD-1`, `HD-23` |
| `ResearchSystem/document-harness/split-design.md` | design product, **user-signed** at blob `3f4d2b0a` (`HD-40`) | `HD-40`; re-signature owed since `6208b35` |

**Round, budget, obligations — derived, not handed to me.** The round is 拆分批 **R0**, plan
`.goals/plans/harness-repo-split.plan.md`, base `0db52a1`, steps 1–7 measured, step 8 (signature)
recorded in `HD-40`, step 9 = *独立 read* — this read. The plan's Notes fix the budget: *`E9` 预算
一轮一算：R0 用 `E10` 独立 read（无 FULL 预算）*. The subject commit is an `E10` free-channel byte
application, which `E9` places outside the cap entirely (*not a round and consumes nothing*), so
nothing here is spent either way. Authorization visible in the repository: `HD-40` (signature,
2026-08-14), `HD-39` (deletion ruling), `HD-38` (free-channel bytes take their own commit),
`HD-36` (channel criteria), `HD-20` (`E2` outranks the free channel), `HD-23`.

**What the work was obliged to do**: apply only the byte-supplied or content-named findings below
must-fix; keep them out of the `M-1` answer's commit (`HD-38`); write no `E2`-frozen path (`HD-20`);
report after the fact and stay reversible (`E10`). All four hold — see §2.

**One obligation the subject range does not carry.** `6208b35` is the range **base**, so the
`M-1` amendment's own bytes are outside this read. `E10` answers a must-fix with *an amendment
commit plus an independent re-read of the amended text*; no record for `6208b35` exists
(`git log --all -- …v3-checkpoint-read-6208b35.md` → empty). If this read is banked as discharging
R0 step 9, that re-read is still owed and the `M-1` amendment text has been gated by nothing. Stated,
not concluded (`R5`).

## 2. Boundary checks — frozen surface and instruction layer

Run first because the free channel's two hard limits are here.

```
$ for p in Document-Work-Assurance-Contract-v3.md …-supersession-1.md …-supersession-2.md;
    do git rev-parse 6208b35:$p ; git rev-parse 0cc45ce:$p ; done
b2dbdf75 SAME   68031fa2 SAME   e1a2f26b SAME
$ git diff --name-only 6208b35 0cc45ce -- ResearchSystem/schema/document-assurance-v3   -> (empty)
$ git ls-tree -r --name-only 0cc45ce -- ResearchSystem/schema/document-assurance-v3 | wc -l  -> 15
$ git diff --name-only 6208b35 0cc45ce -- <the nine E10 member paths>                  -> (empty)
```

`E2`'s three blobs unchanged; the pack is 15 files and none changed; the instruction layer's nine
members are untouched, so no layer read is owed by this commit. `HD-20` is not engaged: no changed
path is frozen. `HD-38` holds — `6208b35` carries the `M-1` answer only, `0cc45ce` carries the
low/observation bytes only; the two sets do not overlap in the diffs.

## 3. `M-1` (must-fix) — the conclusion this commit vouches for is false outside the measured block

The commit's new journal text ends: *「**结论不受影响**：耦合数 0 已由评审员在整块 421 行上复测。」*
The coupling count is right; the conclusion it protects is not. Journal §1 concludes *留在 `rsc.py`
里的耦合全在顶层三行*, and `split-design.md` §1 states it as fact — *`rsc.py` 的产品耦合全在顶层
三行（`:48`/`:49`/`:50`）*. Re-derived over the **whole file**, not the block:

```
$ grep -nE 'generate\.|pipeline\.|stage_close\.|stage_control\.|GENERATED_DIR' ResearchSystem/tooling/rsc.py
49,57,93,95,104,106,116,126        (product: GENERATED_DIR / pipeline. / generate.)
134,145,146,158,161,164,177,178,193,194,208,209,211,220,223   (v1 stage command group, :134-230)
850:    except stage_control.StageControlFault as exc:
$ sed -n '231,651p' ResearchSystem/tooling/rsc.py | grep -cE '…'   -> 0     (block measurement, confirmed)
$ grep -n '^def ' … | awk -F: '$1<=850' | tail -1                  -> 842: def main(…)
$ python - <<'…'  ast walk of main()                               -> handler :845 -> Exception
                                                                      handler :850 -> stage_control.StageControlFault
$ grep -n 'class StageControlFault' ResearchSystem/tooling/rsclib/stage_control.py  -> 122
```

`:850` is in `main()`, not in any command body, and it wraps `args.func(args)` — the shared error
path of **every** `rsc` command including all six v3 ones. It is the single use of `stage_control`
outside `:48` and outside the v1 command group. A measurement scoped to `:231`–`build_parser`
cannot see it, which is why two independent block measurements both returned 0 and the file-scope
claim survived.

**What goes wrong.** `HD-39` 后果 ① and `split-design.md` §1 direct R1/R2 to cut `rsc.py:48`'s
`stage_control`/`stage_close` and `:50`'s `harness_cli` while deleting `rsclib/stage_control.py`.
The module import is evaluated at import time; the `except` expression is evaluated only when an
exception escapes `args.func(args)`. So the cut leaves `rsc.py` importable and every success path
green, and turns the unexpected-failure path of every command into an uncaught `NameError:
stage_control` — a crash where a `FATAL: …` / exit 2 exists today. The v3 commands catch their own
`SpecGap` / `AssuranceFault` (8 handlers inside the block), so this handler is exactly the residual
path, and no test reaches it: the four subprocess tests that drive `rsc.py`
(`test_dispatch_freeze_marker.py:38`, `test_review_cli_v2_subject.py:42`, `:109`/`:203`/`:262`/`:272`,
`test_fix_round_locks.py:258`) assert on handled FATAL strings returned from inside the command, not
on an exception escaping into `main()`.

**Ground truth violated**: `E3` — a factual assertion (*耦合全在顶层三行*) written into a design
document that R1/R2 execute from, whose falsifying command was not run at the scope the assertion
claims. **Location**: `ResearchSystem/document-harness/journal/repo-split-r0-2026-08-13.md:31`;
`ResearchSystem/document-harness/split-design.md:19`; `HARNESS-DECISIONS.md` `HD-39` 后果 ①
(`:68-69`). **Minimum fix**: name `rsc.py:850` as a fourth connected site in `HD-39` ① and in
`split-design.md` §1, and qualify both *全在顶层三行* sentences to the scope actually measured
(*v3 命令块内*). Whether the handler is deleted, re-typed against a v3 fault, or replaced by a bare
`except Exception` is R1/R2's design call, not this read's (`R5`).

**Not independent of the prior worktree record on this point** (see the disclosure above): it named
`:850` first; §3 is my reproduction of it.

## 4. Low

**`L-1` — the new `HD-40` clause states a false fact about `io-design.md`'s bytes.** The added
sentence reads *「`HD-35` 未暴露此坑纯属侥幸：`io-design.md` 的 blob 恰好存的就是 CRLF，两个摘要
重合。」* The blob stores no CR at all:

```
$ git cat-file blob 8f3c82c2 | tr -dc '\r' | wc -c   -> 0
$ git cat-file blob 8f3c82c2 | wc -c ; | wc -l       -> 10423 ; 128
$ git cat-file blob 8f3c82c2 | sha256sum             -> 730fddf4…8157   (== the digest HD-35 records)
$ git cat-file blob 8f3c82c2 | sed 's/$/\r/' | sha256sum -> 35a47fbb…e08f   (what a CRLF blob would give)
$ sha256sum ResearchSystem/document-harness/io-design.md -> 730fddf4…8157
$ for b in b2dbdf75 68031fa2 e1a2f26b ; do git cat-file blob $b | tr -dc '\r' | wc -c ; done -> 0 0 0
```

Every blob in this repository is LF, the three `E2`-frozen ones included. `HD-35`'s recorded digest
is the **blob-content** digest, and the reason it also matches the file on disk is that
`io-design.md`'s *working copy* is LF — it was written LF and never re-materialised by a checkout,
so `core.autocrlf=true` never converted it. `split-design.md` (280 CR), `HARNESS-DECISIONS.md`
(397 CR) and the journal (96 CR) are CRLF on disk against LF blobs; `io-design.md` and the v3
contract are LF on disk. The conclusion the clause defends — that `HD-35`'s digest is sound — is
**true and verified**; only the stated mechanism is inverted.

Downstream decision it changes: the clause is the entry's sole explanation of why the older
signature is still trustworthy, and it teaches the reader to look at the blob's line endings. A
verifier applying that model to a fresh clone gets the wrong answer, because after a checkout with
`core.autocrlf=true` `io-design.md`'s worktree copy becomes CRLF and stops matching `HD-35` — the
exact failure the same paragraph warns about (*会把好签字读成坏的*). The accurate fact is not
recoverable from adjacent text, which asserts its opposite, so this is not wording-level under `R9`.
**Bytes for the fix**: *`io-design.md` 的 blob 恰好存的就是 CRLF，两个摘要重合* →
*`io-design.md` 的**工作副本**恰好也是 LF（写入即 LF、从未被 checkout 重新落盘），故它的工作副本
摘要与 blob 摘要重合；仓内 blob 一律 LF，`E2` 三份冻结件亦然*.

**`L-2` — the `L-3` correction says *命令照录* and records a command that cannot be run.** The
new §10.4 block writes `git log --oneline 0db52a1 -- <7 个 travel 前缀> | wc -l` → **335**. The
operand list is a placeholder, and no file in the repository enumerates the seven prefixes
(`git grep '七个前缀\|travel 前缀'` returns only this line and the table row it annotates). Both
figures are correct — I reproduced them, but only after reverse-engineering the operand set:

```
seven paths that reproduce both figures =
  ResearchSystem/document-harness · …/tooling/rsclib/document_harness ·
  …/tooling/tests/document_harness · …/tooling/tests/document_harness_review ·
  …/schema/document-assurance-v3 · …/migration/document-work-assurance-v3 ·
  ResearchSystem/HARNESS-POLICY.md
$ git log --oneline 0db52a1 -- <those seven> | wc -l   -> 335     (the corrected figure)
$ git log --oneline 5aec7f3 -- <those seven> | wc -l   -> 337     (the original figure, as the block claims)
$ git rev-list --count 0db52a1  -> 720        $ git rev-list --count 5aec7f3  -> 724
```

So the `E3` diagnosis is exactly right and the numbers are sound. Two things follow that the block
does not say. First, the same block instructs *R1 落地时按当时的 base 再算一次* — an instruction R1
cannot execute, since the operands live nowhere. Second, that seven-path set is **not** the set that
produced the `247` in the row directly above it, and the two rows of one table are therefore measured
over different populations:

```
                                   files@0db52a1  files@5aec7f3  commits@0db52a1  commits@5aec7f3
seven-path set (reproduces 335/337)      251            253            335              337
eleven-path set (reproduces 247)         245            247            372              374
   = 5 dirs + 3 registers + 3 v3 contracts; omits tooling/tests/document_harness,
     includes HARNESS-DECISIONS/RIDERS/DECISIONS-archive
```

Neither set matches `HD-28`'s membership ruling: the 335 set carries `HARNESS-POLICY.md`, which
`HD-28`/`HD-33` assign to the caller, and omits the three registers `HD-28` sends to the new repo;
the 247 set omits a test tree. `247` is also a mid-round figure (245 at the base), while `335` is now
explicitly pinned to the base — the correction deepened the mismatch inside the row pair. What the
membership *should* be is `HD-28`'s question, not this read's (`R5`). **Bytes for the fix**: replace
`<7 个 travel 前缀>` with the seven paths above, or with whatever set R1 adopts, and re-derive both
rows over the one set. Deadline: before R1 verifies *247 文件到齐*.

**`L-3` — the `337` sweep missed a site six lines below the block announcing it.** The commit body
claims *§4 两处 337 一并更正*; §4's two sites are indeed corrected (`:75`, `:82`). One more survives,
inside §10.4 itself:

```
$ git grep -n '337' -- ResearchSystem/document-harness/split-design.md
:75  (corrected, cites the L-3 block)   :265 :266  (the correction block, quoting the old value)
:271 **诚实边界**：不能说「那 337 条正文的要点已被 88 份 travel 的评审记录覆盖」…
```

`E7` asks for the defect class, not the reported instance, and the class here is one file wide. The
accurate value is recoverable from `:265-269` immediately above, so this is wording-level under `R9`
and I can name no decision that turns on it — it rides the next batch touching this file, most
naturally the re-signature edit already owed. **Bytes for the fix**: `那 337 条正文` → `那 335 条正文`.

## 5. Observations

**`O-1` — the free channel wrote a user-signed file, and edited the binding clause the source read
reserved to the user.** `feb7b48`'s `L-2` supplied the substitution and then withheld it: *The
signature is the user's act, so the substitution is theirs to make.* The commit made it, and not as
either offered option — it **removed** `sha256 c4e24f99…ab5c` from the binding sentence and relegated
both digests to a correction note, so `HD-40` now binds by blob id and line count alone. No user
ruling is cited in the commit body for that edit. The net position is defensible (a blob id is itself
a content hash, and both digests remain recorded), and the channel does require reversibility and
after-the-fact reporting, which this commit gives. Two facts for the user, not a conclusion (`R5`):
the binding still names blob `3f4d2b0a` / 251 lines while the live file is `74d70ca7` / 280 lines, and
the re-signature delta that `6208b35` announced (*重签绑定在后续 commit 记入 `HD-40`*) now spans two
commits and three sections (§4, §7, §10.4) rather than one.

**`O-2` — `E8`: title form now met, body shape not.** The source read's `O-3` measured nine of nine
commits carrying `chore(governance):` bodies of 20/26/6/23/20/14/18/17/10 non-blank lines, and this
commit's body answers that *纪律从本轮两个 amendment commit 起照 `E8` 形式执行*. The title now matches
(`V3-SPLIT-R0-FREE-…-v1`, names the round). The body measures **22 non-blank lines, 0 trailers**
(`git log -1 --format=%b | grep -c '[^[:space:]]'`), against the batch-B journal §8 discipline the
same sentence invokes (*正文 = kind + 改了什么 + 数字，收在十行内；推理进 journal*). It also names no
kind from `E8`'s own vocabulary — *自由通道* is the channel, not one of candidate / pre-submission
correction / review fix / closeout / errata / amendment / ruling / record — which is the attribution
`E8` exists to spare the review side. The multi-paragraph shape is fine (ledger, 2026-08-07,
HI-REDEEM-5 `L-4`).

**`O-3` — the `O-1` application deleted the recorded method while keeping the count.** The journal's
决定性测量 paragraph previously ended *…的出现次数 = **0**（`sed` 截取 `_cmd_v3_governance_scan`..
`build_parser` 后 grep -c）*; the rewrite keeps the 0 and drops the parenthetical. `E3` allows a count
that is emitted by the command that produces it, or no count. This is the same weakening as `L-2` in
a second place, in the commit whose purpose was `E3` repair — the difference is that this one is
trivially re-derivable, and I re-derived it (0 over `:231`–`:651`, all five tokens).

**`O-4` — the plan's own state is stale at the subject tip.** `.goals/plans/harness-repo-split.plan.md`
still carries `- [ ] 8. 设计定稿 → 用户签字` although `HD-40` records that signature, and its Resume
pointer still reads *下一步 = 用户答设计稿 §9 的 7 个岔口 → 定稿签字（步骤 8）*, while `split-design.md`
§9 now reads *全部已答*. Step 9 correctly remains open. This is the cross-session resume artifact
(`§0.7` layer 2), and it is the one surface a new session reads first.

**`O-5` — channel shape, reported not concluded (`R5`).** The source read's `O-4` already put the
design-round-through-the-read-channel question to the user; the commit body routes it there
unchanged. One mechanical addition from §1 above: this read's range **excludes** the `M-1` amendment
commit, so whatever this read discharges, it is not the independent re-read `E10` attaches to that
amendment. Three consecutive R0 commits have now been reviewed by a channel that cannot return
`CHANGES_REQUIRED`, against a design R1–R4 will execute from.

## 6. What reproduced exactly

Recorded so these are not re-measured. Each was re-derived here, not read off the document or the
source record.

| claim (subject bytes) | recorded | re-derived |
|---|---|---|
| `split-design.md` blob at `9736670` | `3f4d2b0a` | **`3f4d2b0a1e948be0…`**, 251 lines |
| blob-content sha256 (`L-2` fix) | `8da2d17d…59af` | **`8da2d17d7adac639…9ac59af`** |
| working-copy sha256, `core.autocrlf=true` | `c4e24f99…ab5c` | **`c4e24f99334a4441…382bab5c`** (LF blob + one CR per line) |
| `core.autocrlf` on this machine | true | **true** |
| commits touching the travel set, base `0db52a1` | 335 | **335** (seven-path set, `L-2`) |
| same command at `5aec7f3` | 337 | **337** — the `E3` story reproduces |
| repo commits, base | 720 | **720**; at `5aec7f3` **724** |
| `_cmd_v3_*` function count | seven | **7** |
| their offsets | 231 · 275 · 296 · 333 · 445 · 491 · 589 | **exact, all seven** |
| the six old offsets are import lines | yes | **yes** (`:239/:277/:303/:344/:452/:512`) |
| `review_subject` is a mode, not a command | yes | **yes** — called from `_cmd_v3_review` at `:597`; six `add_parser` subcommands only |
| `_cmd_v3_review` imports at `:599-601` | yes | **yes** |
| block `:231`→`build_parser` | 421 lines | **421** (`build_parser` at `:652`) |
| coupling count in that block | 0 | **0**, each of the five tokens |
| `repo-audit.py:38` `EXCLUDE` | ten, listed | **10**, same members and order; `ROOT:31`, `rglob:62`, `cand.exists()` `:103-115`, `exit 1` `:304` all exact |
| deletion list length | 33 paths | **33** tracked files |
| `Stage-Control-Contract.md` already inside 139 | yes | **yes** — 139 union counted: 14·11·1·81·26·2·2·2 |
| union | 171 | **171** (counted, not summed) |
| union minus all 33 listed | 138 | **138** |
| net addition | 32 | **32** (171 − 139) |
| docstring lineage lines | `__init__.py:12,16,19` | **exact**: `rsclib.harness` `:12`, `.c14n` `:16`, `.schemas` `:19` |
| `E2` frozen blobs across range | — | **SAME** ×3; pack **15** files, 0 changed |
| instruction layer across range | — | **0** of nine members changed |
| `HD-38` separation | — | **holds**; `6208b35` = `M-1` only, `0cc45ce` = low/observation only |

## 7. Coverage and ceilings (`R4`)

**Read in full**: the three changed files at the tip; `CONSTRUCTION-CHECKLIST.md`;
`HARNESS-DECISIONS.md` (§live and §implemented); `HARNESS-LEDGER.md`;
`.goals/plans/harness-repo-split.plan.md`; the source read record's findings sections
(`ffbc393`, `:167-319`).

**Sampled**: `rsc.py` — the v3 block, `main()`, the v1 command group and every line matching the
five coupling tokens, not the whole 856 lines; `repo-audit.py` around `:28-50`, `:60-64`, `:101-117`,
`:302-306`; `rsclib/document_harness/__init__.py:1-26`; `stage_control.py` only for
`StageControlFault`'s definition and raise sites.

**Probed only**: the test battery — I located the four subprocess drivers of `rsc.py` and read their
assertions, and ran no test. §3's claim that no test reaches `:850` rests on that reading plus the
absence of any escaping-exception driver, not on an executed run; a battery run could still surface
one. Marked, not verified.

**`UNVERIFIABLE`, stated rather than folded into supported** (`R4`): the travel-set membership behind
`247` / `335`. Both figures reproduce, each under a different path set, and neither set is recorded
anywhere — the sets in `L-2` are my reconstruction from the figures, not a reading of a declared list.
If R1 declares the set, both rows must be re-derived over it.

**Process claims marked, not verified**: that this session held only the review role for its whole
life (`E1`) — true of this session as run, unverifiable from the repository; and the independence
qualification on §3 stated in the header, which is a real ceiling on that finding and on the overlap
between this record and the preserved prior one.

**Not examined**: the `M-1` amendment `6208b35`'s own bytes (outside the range, §1); anything in
`split-design.md` §1–§3, §5–§6, §8–§9, §10.1–§10.3, §10.5 beyond the passages the subject touches or
the findings above reach; the caller-side product tree.
