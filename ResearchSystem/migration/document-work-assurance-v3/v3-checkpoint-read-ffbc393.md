# Split-batch R0 read — `0db52a1dcb51def293b4959d72b9d0a6e63f486d..ffbc3939b222fa5b6092c4095ea8f48087b8c991`

Independent read of the split batch's design round (R0), taken under the plan's step 9
(`E10` channel, no FULL). Not a round: no verdict, no budget consumed (`R3`). Its output is
findings tiered must-fix / low / observation.

**Findings: 1 must-fix, 3 low, 5 observations.**

`M-1` is the one that bites: the round's clean-removal claim — *删除不留悬空引用* — is false.
Thirteen real markdown links, in three files that are **not** in the deletion set, resolve into
it; `HD-39`'s consequence paragraph names only four (of which one self-deletes), so **three** are
budgeted where **thirteen** exist. Since `repo-audit`'s link check resolves any target path, not
only `.md`, executing `HD-39` as written makes `repo-audit` exit 1 — the exact failure mode
`HD-24` invoked to say *「直接删」不存在*, and the failure of the plan's own R1 acceptance line.

Against that: the three measurements the round's rulings actually turned on all reproduce **exactly**
— 117 = 29 + 88 records under the corrected criterion, 7 real cross-links / 73 bare-name mentions,
247 travel-set files — as does the 171-file deletion union. The frozen surface and the instruction
layer took zero bytes.

## 1. Subject, re-derived (`R2`)

Handed one range and nothing else. Round, budget, authorization, obligations and every figure
below are re-derived here; no number is taken from the dispatch prompt, a commit body, the plan,
the ledger or the design document.

```
$ git rev-parse HEAD            -> ffbc3939b222fa5b6092c4095ea8f48087b8c991
$ git rev-parse --abbrev-ref HEAD -> document-work-assurance-v3
$ git status --porcelain        -> (empty; 0 lines)
$ cat .harness/review-pending.json
  {"subject": "0db52a1dcb51def293b4959d72b9d0a6e63f486d..ffbc3939b222fa5b6092c4095ea8f48087b8c991",
   "dispatched_at": "2026-08-14T03:58:39+00:00"}
```

HEAD equals the range tip and the tree is clean, so worktree reads are reads of subject bytes.
The freeze marker's subject is byte-equal to the dispatched range.

**Round and authorization.** `.goals/plans/harness-repo-split.plan.md` (created in this range,
`2bf85c7`) declares `status: R0 OPEN 2026-08-13`, `base_commit: 0db52a1…` — base written, tip
unwritten (`E12` satisfied). Round division was approved by the user («正常走吧»); step 9 is
*独立 read（`E10` 通道，非 FULL——本轮无代码字节）*. `E9`: no valid independent FULL has occurred
for R0, so every commit in the range is a pre-submission correction and consumes nothing; the fix
leg and VERIFY are unspent. `R7`: the approvals themselves («正常走吧», the eight §10 rulings, the
`HD-40` signature) exist only in chat — I state that ceiling and move on.

**Nine commits, classified by hand** (`R2` — no commit here names its kind in `E8`'s vocabulary):

| # | sha | kind, as read from the diff |
|---|---|---|
| 1 | `2bf85c7` | record — plan lands |
| 2 | `d8e6b64` | record — journal + design draft |
| 3 | `ea460bc` | errata — `E11` deviation noted in the plan |
| 4 | `5aec7f3` | ruling — six §10 rulings + two figure corrections |
| 5 | `d504beb` | ruling/errata — §10.3 reversed, §10.4 measured |
| 6 | `db44a08` | ruling — Q4, Q8 |
| 7 | `e7a5ff5` | ruling — `HD-39` created, `HD-24` → superseded/archive |
| 8 | `9736670` | correction — §1–§9 aligned to §10 |
| 9 | `ffbc393` | ruling — `HD-40` signature record |

**Five paths changed**, classified by hand, all inside R0's declared scope; no code, no schema,
no instruction-layer byte:

```
$ git diff --stat 0db52a1..ffbc393
 .goals/plans/harness-repo-split.plan.md            | 162 +++
 ResearchSystem/HARNESS-DECISIONS-archive.md        |  22 +-
 ResearchSystem/HARNESS-DECISIONS.md                |  60 +--
 ResearchSystem/document-harness/journal/repo-split-r0-2026-08-13.md | 85 +++
 ResearchSystem/document-harness/split-design.md    | 251 +++
```

## 2. Boundary checks — frozen surface and instruction layer

`E2`, at the tip: contract `b2dbdf75`, supersession-1 `68031fa2`, supersession-2 `e1a2f26b` —
all three equal the ids `E2` records. `git diff --name-only 0db52a1..ffbc393 --
ResearchSystem/schema/document-assurance-v3` → **0 files**. The pack holds exactly **15** files.
**Frozen surface untouched.**

`E10`, all nine members, base vs tip:

```
15999875 15999875 SAME  CONSTRUCTION-CHECKLIST.md      3350bfac 3350bfac SAME  REVIEW.md
54dfef83 54dfef83 SAME  README.md                      17ff31bb 17ff31bb SAME  v3-harness-operating-contract.md
62c55e4b 62c55e4b SAME  EXECUTION.md                   b576a45e b576a45e SAME  v3-harness-review-contract.md
68031fa2 68031fa2 SAME  supersession-1.md              e1a2f26b e1a2f26b SAME  supersession-2.md
09aa8699 09aa8699 SAME  paragraph-map.schema.json
```

Nine of nine unchanged, and item-for-item equal to the nine ids the plan's entry gate cites from
`v3-checkpoint-read-f61ce2c.md`. The citation discount is therefore valid and **this round wrote
zero instruction-layer bytes** — which is also why it is not, in `E10`'s own sense, an amendment
read (see `O-4`).

`§live` entry count: **11** at base (the plan's entry gate says 11 and corrects a spoken "nine" —
the correction is right), **12** at tip (+`HD-39` +`HD-40` −`HD-24`). `HD-30` mechanism honoured:
`e7a5ff5` moves `HD-24` to archive and creates `HD-39` in the same commit, with pointers both
ways. `HD-2`'s *one live per topic* holds.

## 3. `M-1` (must-fix) — the deletion leaves thirteen dangling links, not three

**Where.** `split-design.md` §7 (*清白性实证 … **删除不留悬空引用。***, and *三个 v1 schema 的全仓
读者**只在 v1 族自身内***); `HARNESS-DECISIONS.md` `HD-39` 后果 (*指向 `stages/` 的 4 条链接（其一在
待删的 v1 契约 `:23` 内，随之消失）* — i.e. three survivors) and its 未验 line (*两 schema 全仓读者仅
在 v1 族自身内*); `journal/repo-split-r0-2026-08-13.md` §7 (*`stages/` 的 inbound 里唯一非记录类引用
就是这一条*).

**Ground truth.** `Thesis/Work/Tooling/repo-audit.py:103-115` resolves every markdown link target
with `cand.exists()` — **not** restricted to `.md`, so links to `.json` files and to directories
count, and a missing target is a hard error (`:304`, exit 1). Enumerating every real markdown link
whose source is outside the 171-file deletion set and whose target is inside it (inline code
stripped, exactly as `repo-audit` does at `:49-55`):

```
DELETION SET (union, tracked files): 171
SOURCE FILES OUTSIDE DELETE SET WITH REAL LINKS INTO IT: 3   TOTAL LINKS: 13

  ResearchSystem/README.md  (8)
      -> ResearchSystem/stages
      -> ResearchSystem/contract/Stage-Control-Contract.md
      -> ResearchSystem/stages/README.md
      -> ResearchSystem/stages/_stage-record-template.md
      -> ResearchSystem/schema/stage-record.schema.json
      -> ResearchSystem/schema/review-result.schema.json
      -> ResearchSystem/schema/closure-receipt.schema.json
      -> ResearchSystem/schema/stage-control-fixtures
  .goals/plans/general-harness-v2-architecture-revision.plan.md  (3)
      -> ResearchSystem/migration/general-harness-v2/nodes/{A1,A2,A3}/NODE.md
  .goals/plans/research-system-stage-control-refactor.plan.md  (2)
      -> ResearchSystem/migration/stage-control-refactor/pre-refactor-worktree-manifest.md
      -> ResearchSystem/migration/stage-control-refactor/CTRL-BOOT-v1.md
```

`repo-audit` exits **0** today (re-run at the tip), so all thirteen resolve now and all thirteen
break on deletion.

**What it violates.** Three separate assertions. (i) *删除不留悬空引用* is false. (ii) *三个 v1
schema 的全仓读者只在 v1 族自身内* is false — `ResearchSystem/README.md:43-45` links all three, and
that file is not in the deletion set. The parenthetical that supports it (`stage_close.py` ·
`stage_control.py` · `stage-control-fixtures/validate.py`) enumerates **byte-readers**, and the
conclusion drawn from it is about **references**; the grep answered a narrower question than the
sentence claims. (iii) journal §7's *唯一非记录类引用* is false — `ResearchSystem/README.md:35/41/42`
are three more, in a live index, not a record.

**Why it may not wait.** `HD-40` makes all ten sections R1–R4's execution basis, and `HD-39` is the
live ruling R1 executes. The plan's R1 acceptance is *repo-audit 必须仍 exit 0* (step 12) and
*repo-audit exit 0* (Acceptance). An R1 executor working from `HD-39`'s consequence list fixes the
three surviving `stages/` links and ships; `repo-audit` then exits 1 on the other ten. This is
`HD-24`'s own stated reason that *「直接删」不存在*, surviving into `HD-39` unmeasured.

**Minimum fix.** Replace the three assertions with the enumeration above — thirteen links, three
source files, named — and carry those three files into `HD-39`'s 连带 list so R1's change boundary
includes them. Nothing about the ruling itself changes: the deletion stays a deletion, its blast
radius is stated correctly. Note the cost the fix carries and which is not mine to resolve
(`R5`): `split-design.md` is signed (`HD-40`, blob `3f4d2b0a`), so amending §7 owes a re-signature
under `HD-40`'s own *对该文件的后续实质修改欠重签*; recording the correction in `HD-39` alone leaves
the signed §7 text standing but false. The route is the user's.

**Class, not instance** (`E7`). I ran the sweep rather than reporting the file I first hit: the
enumeration above is every source outside the set, not only `ResearchSystem/README.md`. Two
further checks in the same class came back clean and are recorded so the sweep is not re-run:
importers of `stage_control` / `stage_close` are `rsc.py:48` (to be cut anyway),
`tests/harness/run_tests.py:658,676`, `tests/stage_control/run_tests.py:23` and a docstring
mention in `gitadapter.py:3` — all inside the deletion set or already scheduled, so §7's
**code**-side claim holds; and no travelling `.py` imports anything in the deletion set.

## 4. Low

**`L-1` — the R1 confirmation point is defined by a count and a list that disagree by one file.**
`HD-40` reserves *删除范围 **139→171** 的差额欠 R1 动手前的最后确认*, and §7 / `HD-39` describe the
difference as **32 件**, then list nine bullet groups: `Stage-Control-Contract.md` · `stage_control.py`
· `stage_close.py` · three v1 schemas · `stage-control-fixtures/`(24) · `tests/stage_control/`(2) ·
`.claude/commands/rs-execute.md` = **33** paths, not 32. The union is nevertheless exactly 171
(counted, not summed) because `Stage-Control-Contract.md` is **already inside the 139**: §10.2's
own breakdown reads *… 两份契约 2 · `stages/` 2* and names those two contracts as
`Stage-Control-Contract.md` + `General-Harness-Contract-v2.md`. So one file sits in both buckets,
and the stated fallback *要缩回 139 只需把这 32 件划出去* yields **138**, not 139. Re-derived counts:

```
harness/ 14 · rsclib/harness/ 11 · tests/harness/ 1 · schema/harness-v2/ 81
migration/general-harness-v2/ 26 · migration/stage-control-refactor/ 2 · stages/ 2   = 137
+ 2 contracts = 139        union with the v1 runtime family (32 further files) = 171 (counted)
```

Downstream decision it changes: the user reserved a confirmation over "the delta"; shown the list
as written, they would be shown a file they already approved as if it were new, and the offered
way back to 139 does not reach 139. **Bytes for the fix**: *32 件* → *32 件（列出的 33 条中
`contract/Stage-Control-Contract.md` 已计入 139 的「两份契约」，故并集 171 而非 172）*.
Deadline: before R1 puts the delta to the user.

**`L-2` — `HD-40`'s sha256 does not reproduce from repository bytes.** The entry binds
`split-design.md` by blob `3f4d2b0a` **and** sha256 `c4e24f99…ab5c`, 251 lines. Blob and line count
verify. The sha256 does not:

```
$ git cat-file blob 3f4d2b0a…   | sha256sum   -> 8da2d17d7adac63950eaf74d688b7900ead123cc6676fd4bc781519019ac59af   (19004 bytes)
$ sha256sum ResearchSystem/document-harness/split-design.md
                                              -> c4e24f99334a44413283cc9f7b1e34740dbda511f6ce585bf0cb0152382bab5c   (19255 bytes)
$ git config --get core.autocrlf              -> true
```

The recorded digest is the **checked-out** file on a machine with `core.autocrlf=true`; the blob
stores LF, and the +251 bytes are one CR per line. `HD-35`'s precedent hid this — `io-design.md`'s
blob happens to store CRLF (10423 bytes, worktree-identical), so its two digests coincide.
Downstream decision: §4 rules *新仓从头，不保历史*, and the plan's acceptance asks that the signed
files still verify across repositories. Blob id travels; this sha256 does not — a verifier on a
fresh clone with `core.autocrlf=false` computes `8da2d17d…` and reads the signature as broken.
**Bytes for the fix**: `sha256 c4e24f99…ab5c` → `sha256 8da2d17d…59af（blob 内容，LF）`, or state
that the digest is over the CRLF working copy. The signature is the user's act, so the
substitution is theirs to make.

**`L-3` — §10.4's commit figures do not reproduce.** *碰过 travel 集的 commit **337** / 全仓 724
（47%）*. At the base `0db52a1`:

```
$ git rev-list --count 0db52a1                       -> 720      (--no-merges 712, --first-parent 690, --all 840)
$ git rev-list --count 0db52a1 -- <5 tree prefixes>  -> 330
$ git rev-list --count 0db52a1 -- <the 11 paths that reproduce 247 exactly>  -> 372
```

Neither 337 nor 724 appears under any composition I tried, including the one that reproduces the
247 in the same table exactly. `E3` asks that counts be emitted by the command that produces them;
these two are not reproducible from the repository as recorded. The ruling they fed is unaffected
— *从头* was chosen on ~10 min vs ~1 h, and neither number reorders that — but 337 is carried
forward as a standing fact into §4 (*代价是 337 个 commit 的正文留在调用者仓*) and into the proposed
new-repo README provenance line (*去哪找那 337 条正文*), where a wrong count becomes permanent.
Recompute at R1 and quote the command.

## 5. Observations

**`O-1` — journal §1's six line numbers are not the six commands.** §1 says *六个 `_cmd_v3_*` 函数体
… 全部是函数内惰性 import（`:239/:277/:303/:344/:452/:512`）*. There are **seven** `_cmd_v3_*`
functions; the six cited offsets belong to `governance_scan`(231) · `status`(275) · `flow`(296) ·
`dispatch`(333) · `disposition`(445) · `review_subject`(491) — the last of which is a **mode** of
`review`, not a registered command — while `_cmd_v3_review`(589), which *is* the sixth registered
command, imports at `:599-601` and is absent from the list. The command enumeration in
`split-design.md` §1 is right (six subparsers: `governance-scan` / `status` / `flow` / `dispatch` /
`disposition` / `review`), and the conclusion is unaffected — I re-ran the coupling measurement
over the **whole** block (`:231` to `build_parser`, 421 lines) and `generate.` / `pipeline.` /
`stage_close.` / `stage_control.` / `GENERATED_DIR` all count **0**. Only the line list is wrong,
and it is the artefact an R2 executor would grep by.

**`O-2` — journal §2 says `EXCLUDE` holds *九项*; it holds ten** (`repo-audit.py:38`: `.git`,
`.obsidian`, `.claude`, `.agents`, `node_modules`, `.venv`, `vendor`, `artifacts`, `investigation`,
`.pytest_cache`). Its other citations in the same paragraph are exact: `ROOT` at `:31`, `rglob` at
`:62`, and `contract_provenance_check.py` is indeed absent from the repository (`hooks/` tracks
`__init__.py` + three checks), and no pre-commit hook is tracked.

**`O-3` — `E8`'s commit shape, nine for nine.** No title in the range matches `V3-<ROUND>-v1`
(`git log --format=%s | grep -c '^V3-'` → **0**); all nine are `chore(governance): …`. History
shows that form used for between-round bookkeeping (`2d14a65`, `22b54cd`, `aef047b`) and
`V3-B-R*-…-v1` for round commits, so R0's round commits are carrying the bookkeeping form. Bodies,
against the discipline set one commit before this range's base (batch-B journal §8: *正文 = kind +
改了什么 + 数字，收在十行内；推理进 journal*): non-blank body lines **20 / 26 / 6 / 23 / 20 / 14 /
18 / 17 / 10** — one of nine inside ten lines, though all nine are far below the 1070-word case
that provoked the rule, and R0 *did* write its journal. No commit names its kind in `E8`'s
vocabulary; §1's table above is my classification, which `E8` exists to make unnecessary.

**`O-4` — a design round reviewed through the read channel, after signature.** `E10`'s read is
defined for instruction-layer amendments — *that read's subject is the amendment text itself* —
and this round wrote zero instruction-layer bytes (§2 above), so the channel is being used as a
general no-verdict, no-budget review for a design round. Earlier design rounds took FULLs
(`E2-REBASELINE-DESIGN`, and the 2026-08-04 design-round FULL/VERIFY the ledger cites at `L3` and
at the 松冻结 ruling). Two consequences worth stating rather than concluding (`R5`): a read carries
no verdict, so nothing here can return `CHANGES_REQUIRED` against a design that R1–R4 will execute
from; and `HD-40`'s signature landed in the last commit of the range, so the read cannot gate what
it reads. `M-1` is exactly a finding that would have met a signature gate.

**`O-5` — three docstring lines in travelling code will cite modules that exist nowhere.**
`rsclib/document_harness/__init__.py:12,16,19` describe v3's lineage in terms of `rsclib.harness`,
`rsclib.harness.c14n` and `rsclib.harness.schemas`. That module travels; those modules are deleted
and, under §4's *从头*, will not exist in the new repository's history either. No code breaks —
they are prose — but the provenance they point at becomes unreachable from the new repo. Cheap to
carry in the §4 README provenance line rather than to discover later.

## 6. What reproduced exactly

Recorded so these are not re-measured. Each was re-derived, not read off the document.

| claim | recorded | re-derived |
|---|---|---|
| review records in `migration/document-work-assurance-v3/` | 117 | **117** top-level `.md`, identical at base and tip |
| product-run vs construction split, §10.1 criterion (first 40 lines name a run or `assurance/runs/`) | 29 / 88 | **29 / 88** |
| real cross-links between the two groups, §10.1 | 7 (构造→产品 2 · 产品→构造 5) | **7 (2 · 5)**, direction included |
| bare-name cross mentions, §10.1 | 73 | **73** (total 80) |
| deletion union, `HD-39` | 171 | **171** tracked files (counted, not summed — see `L-1`) |
| 139 breakdown, §10.2 | 14 · 11 · 1 · 81 · 26 · 2 · 2 · 2 | each count exact; sum 139 |
| travel set, §10.4 | 247 | **247** = 18+17+15+25+166 + 3 registers + 3 v3 contracts |
| `rsc.py` | 856 lines; coupling at `:48/:49/:50` | **856**; exactly those three top-level imports |
| v3 ↔ product coupling | 0 | **0** across the whole v3 block (421 lines) |
| `dispatch.py` | 701 lines; `:400` / `:515` / `:626` | **701**; `render_dispatch` `:400`, `CONSTRUCTION_PROMPT` `:515`, `READ_PROMPT` `:626` |
| `pack_digests()` v3 callers | 0 | **0** (`__init__.py:238`, `__all__` at `:266`); v2 live at `resolver.py:272`, `tests/harness/run_tests.py:39` |
| the three v1 schemas vs `E2` | outside the frozen pack | pack = **15** files, none of them; `E2` does not block |
| `stages/` | 2 files, 4 real links | **2**; **4** (`README.md:35,41,42` + `Stage-Control-Contract.md:23`) |
| archive at `e7a5ff5` | 128 lines | **128** (130 at tip, after `ffbc393`) |
| rider bank | 38 lines | **38**; ledger **114** ≤ 120 |

## 7. Coverage and ceilings (`R4`)

**Read in full**: the five changed files at the tip; `CONSTRUCTION-CHECKLIST.md`; `REVIEW.md`;
`HARNESS-DECISIONS.md` §live and the archive diff; all nine commit messages;
`Thesis/Work/Tooling/repo-audit.py`'s link machinery.
**Sampled**: `rsc.py` (the v3 block and the parser registrations, not the product commands);
`document_harness/__init__.py` around `pack_digests`; batch-B journal §8; the
`v3-checkpoint-read-f61ce2c.md` header for the nine cited blob ids.
**Probed only** (`git`/`grep`/one script, no reading): the 171-file deletion set, the 117 records,
the travel set, the commit counts, importer sweeps.
**Not read**: `EXECUTION.md`, `README.md`, the two retired-contract stubs and `paragraph-map.schema.json`
— all four verified byte-unchanged, and nothing in this subject relies on their content;
`io-design.md` beyond the sections §10.3 quotes.

**Ceilings.** Every authorization in this round — the round division, the eight §10 rulings, the
`HD-40` signature — exists only in chat; I verified that the repository records them consistently,
never that they were given (`R7`). `HD-40`'s *八问全裁* and `HD-39`'s user-ruling attribution are
process claims with no evidence lock. The 29/88 classification reproduces **the criterion**, not
its correctness: it is a 40-line heuristic, and whether each of the 117 files is truly a product
or construction record is not something I checked file by file — R1's *路径清单须逐文件列* inherits
that exposure. `L-3`'s figures are reported as not-reproduced, not as wrong: I could not find the
composition that produced them, and one may exist.
