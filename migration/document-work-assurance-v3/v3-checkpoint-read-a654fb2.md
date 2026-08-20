# Split-batch R0 — read of the whole round `0db52a1dcb51def293b4959d72b9d0a6e63f486d..a654fb2181be0b05516806eb6a0c7abf45afe642`

Independent read of the split batch's design round (R0) end to end: the plan, the design
document, its journal, the decision-register changes, the four review records the round
produced, and the three commits that answer the fourth of them. This is the plan's step 9,
dispatched over the batch base rather than over `289f8ab` — a superset, so it discharges the
re-read owed on `33eb722`/`28c6e26`/`a654fb2` and re-covers everything the four earlier reads
saw in pieces. **Not a round** (`R3`): no verdict, no budget consumed. Output is findings
tiered must-fix / low / observation.

**Findings: 2 must-fix, 5 low, 7 observations.**

Both must-fixes are the same shape as the four the round already answered, at surfaces the
sweeps did not reach. The blast radius of `HD-39`'s deletion was measured over **markdown
links** and over **python importers**, and those two measurements are exact. It was not
measured over the other things that resolve into the deletion set.

`M-1`: two of the **eight** full-battery commands `EXECUTION.md` mandates — *these eight
commands and nothing fewer* — are files R1 deletes. R1's step 13 and the plan's Acceptance
(*全电池八条命令绿*) become unsatisfiable in the round that creates the problem, and the
repair is an edit to an `E10` instruction-layer member that removes items from a mandated
enumeration, i.e. design, i.e. a round R1 cannot open for itself. Nothing in the design, the
journal, `HD-39` or the plan connects the deletion to the battery.

`M-2`: the deletion breaks **fourteen** references, not thirteen. The fourteenth is a
**wikilink**, in a **fourth** source file, and `repo-audit` hard-blocks on wikilinks in a
check separate from the markdown-link scan every previous sweep ran. `HD-39` ②,
`split-design.md` §7's table, plan step 12's change boundary and the Acceptance all say
*3 文件 13 条*; repairing all thirteen still leaves exit 1.

Against that, the substance holds and holds well. Every figure the rulings turn on re-derives
**exactly**: 171 = 139 + 32 counted not summed, the eight-tree breakdown, 29/88 under the
stated criterion at both revisions, the seven cross-links with their directions and endpoints,
all thirteen markdown links with their line numbers, 245 @ base / 335 / 720, the 28-site
`rsc.py` enumeration and its two-command composition, the `:850` shared error exit, five
`pack_digests` hits, the `.claude` inventory, `HD-40`'s blob-content sha256. The frozen surface
and the instruction layer took **zero bytes** across all twenty-four commits. And §1's
load-bearing claim — that the v3 command block lifts out clean — survives a scope *wider* than
the round measured (`O-1`).

## 1. Subject, re-derived (`R2`)

Handed one range and nothing else. Round, budget, authorization, obligations and every figure
below are re-derived here; nothing is taken from the dispatch prompt, a commit body, the plan,
the ledger, the design document or any of the four prior records.

```
$ git rev-parse HEAD                     -> a654fb2181be0b05516806eb6a0c7abf45afe642  (== range tip)
$ git rev-parse --abbrev-ref HEAD        -> document-work-assurance-v3
$ git status --porcelain                 -> (empty)
$ git rev-list --count 0db52a1..a654fb2  -> 24
$ cat .harness/review-pending.json
  {"subject": "0db52a1dcb51def293b4959d72b9d0a6e63f486d..a654fb2181be0b05516806eb6a0c7abf45afe642",
   "dispatched_at": "2026-08-14T13:27:12+00:00"}
$ git log -1 --format=%cI a654fb2         -> 2026-08-14T23:06:26+10:00  (= 13:06:26Z)
```

HEAD equals the tip and the tree is clean, so worktree reads are reads of subject bytes. The
freeze marker's subject is byte-equal to the dispatched range and post-dates the tip by
20m46s; no commit has landed since dispatch (`E9`'s from-dispatch-to-record clause holds).
`.harness/` is gitignored (`git check-ignore -v` → `.gitignore:19`), so marker writes are
filesystem actions, never diff content. No record for this subject existed in the worktree at
open, so there is no collision disclosure to make.

**Round, budget, obligations — derived.** The round is 拆分批 **R0**, plan
`.goals/plans/harness-repo-split.plan.md` (created inside this range, `2bf85c7`),
`status: R0 OPEN 2026-08-13`, `base_commit 0db52a1` — base written, tip unwritten (`E12`
satisfied). Step 9 is *独立 read（`E10` 通道，非 FULL——本轮无代码字节）*; plan Notes: *`E9`
预算一轮一算：R0 用 `E10` 独立 read（无 FULL 预算）*. `E9`'s own test settles it independently
of what anything is called: **no valid independent FULL has occurred for R0**, so every one of
the twenty-four commits is a pre-submission correction and consumes nothing; the fix leg and
the VERIFY are unspent. Live rulings visible in the repository that bind this work: `HD-41`
(量程 discipline + 扫类留痕, created by the tip commit), `HD-40` (signature, *R1 按 §3/§4/§7
施工*), `HD-39` (deletion), `HD-38` (free-channel bytes take their own commit), `HD-36`
(must-fix channel takes 扫类 and no-bytes fixes), `HD-30`, `HD-28`, `HD-27`, `HD-23`, `HD-20`,
`HD-9`, `HD-5`, `HD-4`, `HD-2`. `§live` holds **13** entries at the tip.

**Dispatch base, stated because it differs from the plan.** The plan's Resume pointer sets
*下一次 read 以 `289f8ab` 为 base*; this dispatch used `0db52a1`, a strict superset. Coverage
by the four prior reads, re-derived: `0db52a1..ffbc393` 9 commits · `6208b35..0cc45ce` 1
(contained in the next) · `feb7b48..b75676e` 5 · `4342c6b..a2f8c7d` 4 — union **18** of the
24. The **six** no earlier read saw are the three record commits (`feb7b48`, `4342c6b`,
`289f8ab`, each of which sat on a later read's base line) and the three that answer read 4
(`33eb722`, `28c6e26`, `a654fb2`).

**Twenty-four commits, classified by hand** (`R2`). The first nine carry `chore(governance):`
titles and name no kind in `E8`'s vocabulary; from `feb7b48` on, titles conform and most
bodies name a kind.

| # | sha | kind, as read from the diff |
|---|---|---|
| 1 | `2bf85c7` | record — plan lands |
| 2 | `d8e6b64` | record — journal + design draft |
| 3 | `ea460bc` | errata — `E11` deviation noted |
| 4 | `5aec7f3` | ruling — six §10 rulings + two figure corrections |
| 5 | `d504beb` | ruling/errata — §10.3 reversed, §10.4 measured |
| 6 | `db44a08` | ruling — Q4, Q8 |
| 7 | `e7a5ff5` | ruling — `HD-39` created, `HD-24` → superseded/archive |
| 8 | `9736670` | correction — §1–§9 aligned to §10 (the blob the signature binds) |
| 9 | `ffbc393` | ruling — `HD-40` signature record |
| 10 | `feb7b48` | record — read 1 |
| 11–12 | `6208b35` `0cc45ce` | amendment (`M-1`) · free-channel application |
| 13 | `6a946ba` | record — read 2 |
| 14–15 | `f4c9902` `b75676e` | amendment (`M-1B`) · free-channel application |
| 16 | `4342c6b` | record — read 3 |
| 17–18 | `e788169` `f97bb17` | amendment (`M-1C`/`M-2`) · free-channel application |
| 19–20 | `12a28ce` `a2f8c7d` | errata — the two 量程 self-audits |
| 21 | `289f8ab` | record — read 4 |
| 22 | `33eb722` | amendment (`M-1D`) — plan, four sites |
| 23 | `28c6e26` | free-channel application — seven low/observation fixes |
| 24 | `a654fb2` | ruling — `HD-41` created |

**Nine paths changed across the range**, classified by hand; no code, no schema, no
instruction-layer byte:

```
$ git diff --name-status 0db52a1..a654fb2
A  .goals/plans/harness-repo-split.plan.md                              plan (resume artifact)
M  ResearchSystem/HARNESS-DECISIONS.md                                  decision register — NOT an E10 member (HD-19)
M  ResearchSystem/HARNESS-DECISIONS-archive.md                          decision archive
A  ResearchSystem/document-harness/split-design.md                      design product, user-signed at 3f4d2b0a (HD-40)
A  ResearchSystem/document-harness/journal/repo-split-r0-2026-08-13.md  round record (measurement)
A  …/v3-checkpoint-read-{ffbc393,0cc45ce,b75676e,a2f8c7d}.md            review records (R6)
   2288 insertions, 17 deletions
```

**Ceiling stated once** (`R7`): the round division («正常走吧»), the eight §10 rulings, the
`HD-40` signature, the 量程 method approval and the `HD-41` instruction («建一条吧») all exist
only in chat. I verified that the repository records them consistently; never that they were
given.

## 2. Boundary checks — frozen surface and instruction layer

```
$ per-path blob compare, base 0db52a1 vs tip a654fb2:
  b2dbdf75 SAME  Document-Work-Assurance-Contract-v3.md        (E2 blob 1)
  68031fa2 SAME  …-supersession-1.md                            (E2 blob 2, E10 member)
  e1a2f26b SAME  …-supersession-2.md                            (E2 blob 3, E10 member)
  15999875 SAME  CONSTRUCTION-CHECKLIST.md      3350bfac SAME  REVIEW.md
  54dfef83 SAME  README.md                      17ff31bb SAME  v3-harness-operating-contract.md
  62c55e4b SAME  EXECUTION.md                   b576a45e SAME  v3-harness-review-contract.md
  09aa8699 SAME  paragraph-map.schema.json
$ git diff --name-only 0db52a1..a654fb2 -- ResearchSystem/schema/document-assurance-v3   -> (empty)
$ git ls-tree -r --name-only a654fb2 -- ResearchSystem/schema/document-assurance-v3 | wc -l -> 15
```

`E2`'s three blobs unchanged and equal to the ids `E2` records; the pack holds exactly fifteen
files and none changed; **nine of nine instruction-layer members unchanged**, so no layer read
is owed by this range and `HD-20` is not engaged. `HD-38` holds at diff level: `33eb722`
carries the `M-1D` answer only (plan), `28c6e26` the low/observation bytes only (journal,
design), `a654fb2` the ruling (register + one plan line); the three diffs do not overlap.

`repo-audit` at the tip: **exit 0**, scope 514 markdown files. `ledger_cap_check.py`: **exit
0**; `HARNESS-LEDGER.md` **114** lines. `HARNESS-RIDERS.md` **38** lines, unchanged by this
range — nothing was banked, and apart from `L-3` nothing owed the bank. `HD-24` sits in the
archive with `status: superseded` and a pointer to `HD-39`; `HD-39` points back — `HD-30`'s
mechanism honoured.

## 3. `M-1` (must-fix) — the deletion removes two of the eight mandated full-battery commands, and the repair is an `E10` design change nobody scheduled

**Where.** `EXECUTION.md:328-341` (instruction-layer member, blob `62c55e4b`), *Regression-battery
tiering*:

> **Schema, tooling, or generated surfaces touched**: the full battery runs, and it is
> **these eight commands and nothing fewer** — `…/tools/tests/run_tests.py` … ,
> `ResearchSystem/tooling/tests/harness/run_tests.py`,
> `ResearchSystem/tooling/tests/stage_control/run_tests.py`, and
> `ResearchSystem/tooling/rsc.py compile --check`. Enumerated here because the earlier
> four-item phrasing authorized less than the battery is: **it under-ran twice (batch B R1 and
> R3)** and both times only the executor's private knowledge caught it.

**Ground truth.** Two of those eight are inside `HD-39`'s 171-file deletion set:

```
$ git ls-files ResearchSystem/tooling/tests/harness ResearchSystem/tooling/tests/stage_control
ResearchSystem/tooling/tests/harness/run_tests.py            <- HD-39 ③ tests/harness (1 file)
ResearchSystem/tooling/tests/stage_control/cases.json        <- HD-39 v1 runtime family (2 files)
ResearchSystem/tooling/tests/stage_control/run_tests.py      <-   "
```

Checked as a class, not an instance (`E7`, `HD-41` ④): I put all eight commands against the
deletion set. Six survive — `tooling/tests/run_tests.py`, `run_p4_tests.py`, `run_p5a_tests.py`,
`schema/fixtures/validate_fixtures.py`, `python -m pytest -q` from `ResearchSystem/tooling`,
`rsc.py compile --check` — and none of the six imports or validates anything in the deletion
set, so exactly two commands vanish and the surviving six are unaffected.

**What it violates.** Three action-bearing statements, all in this round's own artifacts.
Plan step 13: *全电池（`EXECUTION.md` tiering 节：本轮碰代码 = 八条命令，nothing fewer）*.
Plan step 17 (R2): *全电池 + FULL*. Plan Acceptance: *全电池**八条命令**绿*. R1 both touches
tooling (so the full tier is owed) and deletes two of the commands that constitute it, in the
same round. The executor is then left with the option `EXECUTION.md:339-341` exists to
forbid: run six, call it the battery. That paragraph records that the previous, looser
phrasing under-ran twice and that only private knowledge caught it — this round would make
the enumeration itself the thing that is wrong, which is worse, because the guard reads as
satisfied.

**Why it may not wait, and why R1 cannot absorb it.** The fix is to remove two items from a
mandated enumeration in `EXECUTION.md`. That is an instruction-layer edit that changes what a
rule requires, so under `E10`'s design test it **opens a round**; it is not a free-channel
application and not a must-fix amendment. The batch plan schedules R1 (搬字节) → R2 (CLI) →
R3 (接线) → R4 (记账收批, explicitly *不开轮*), and no step opens a design round on the layer.
So an R1 executor meets a contradiction it has no in-boundary way to resolve: the layer says
run eight, two do not exist, and the amendment channel available to it cannot say otherwise.
This is `E2`'s menu shape one layer over — take the in-boundary path and record why, obtain
the ruling, or stop with `SPEC_GAP` — and the round that should have surfaced it is this one,
because `HD-40` makes §3/§4/§7 R1's construction basis and `HD-39` is the ruling R1 executes.

**Minimum fix.** State the collision where R1 will meet it — `HD-39`'s 后果 list and the plan's
steps 11/13 — and give it a home: either the enumeration is amended in a design round before
R1 (the honest reading of `E10`), or the user rules that dropping two commands whose subjects
no longer exist is not a rule change, and that ruling is recorded before R1 runs its battery.
Which route is the user's (`R5`). Note the adjacent debt this touches, not as part of the fix:
rider `tier-scope` ② records that the tiering section's *this section is the revert unit*
self-description stopped being cheap once the section moved into the instruction layer, and
`tier-scope` ① is the clause that enumerated these eight commands — see `L-3` for why neither
rider is in the batch's triage.

## 4. `M-2` (must-fix) — the deletion breaks fourteen references in four files, and the fourteenth is a wikilink

**Where.** `split-design.md` §7 (*删除集之外有 3 个文件、13 条真 markdown 链接指进删除集* and
the table under it); `HARNESS-DECISIONS.md` `HD-39` 后果 ② (`:101-105`); the plan's step 12
(*修 13 条入链 … **这三个文件在 R1 的改动边界内***) and Acceptance (*repo-audit exit 0；**13
条入链全部处置完毕**（3 个源文件在 R1 边界内）*).

**Ground truth.** `repo-audit.py` runs three *separate* hard link checks, not one:

```
:304  hard |= block("Broken markdown links", md_broken, True)
:305  hard |= block("Broken source_trace paths", st_broken, True)
:306  hard |= block("Broken wikilinks",       wiki_broken, True)
:325  sys.exit(1 if hard else 0)
```

Wikilinks do not resolve by path. `:86-91` builds `base` from the **stem** of every in-scope
markdown file and `alias` from `aliases:` frontmatter; `:125-129` fails a wikilink when
neither map holds its target, and `strip_inline_code` is deliberately **not** applied to this
scan (`:97-101`). A wikilink therefore survives or dies on whether any file with that stem
exists anywhere in scope.

Replicating all three scans with the 171-file deletion applied — deletion set re-derived by
`git ls-files`, directory targets treated as gone when every tracked file under them is
deleted, `alias`/`base` rebuilt over the surviving tree exactly as `:86-91` does:

```
deletion set size: 171
AFTER DELETION — broken markdown links: 13
    .goals/plans/general-harness-v2-architecture-revision.plan.md -> …/nodes/{A1,A2,A3}/NODE.md
    .goals/plans/research-system-stage-control-refactor.plan.md   -> …/{CTRL-BOOT-v1,pre-refactor-worktree-manifest}.md
    ResearchSystem/README.md -> contract/Stage-Control-Contract.md · schema/{stage-record,review-result,
                                closure-receipt}.schema.json · schema/stage-control-fixtures/ ·
                                stages/ · stages/README.md · stages/_stage-record-template.md
AFTER DELETION — broken wikilinks: 1
    .goals/plans/document-work-assurance-harness-v3.plan.md -> General-Harness-Contract-v2
AFTER DELETION — broken source_trace paths: 0
```

The site:

```
$ grep -n 'General-Harness-Contract-v2' .goals/plans/document-work-assurance-harness-v3.plan.md
41:[[General-Harness-Contract-v2|Contract v2]], `.goals/LEDGER.md`, A4 code or any business content.
$ git ls-files | grep -i 'General-Harness-Contract-v2'
ResearchSystem/contract/General-Harness-Contract-v2.md          <- the only file with that stem
```

That contract is one of the *两份契约* inside the 139, so it is deleted; the plan that links to
it is not in the deletion set; no other file carries the stem and no `aliases:` entry supplies
it (the simulation rebuilt `alias` and still reported it broken); the wikilink is outside a
fence and wikilinks are not exempted by inline code, so nothing suppresses it.

**What it violates.** The corrected §7 sentence is scoped to *真 markdown 链接*, while the
acceptance it protects is `repo-audit exit 0`, which three checks can fail. `HD-39` ② is the
connected list R1 executes from and names three files; step 12 puts exactly those three inside
R1's change boundary. An R1 executor who repairs all thirteen markdown links and re-runs
`repo-audit` gets exit 1 on *Broken wikilinks*, with a source file in nobody's change boundary
— the same failure mode `HD-24` invoked to say *「直接删」不存在*, one link-kind over.

**Class, not instance** (`E7`, `HD-41` ④). I did not report the first thing I hit: I ran every
link kind `repo-audit` hard-blocks on, over the whole tree, with the deletion applied —
markdown links (13, in the three known files, reproduced item for item with line numbers),
wikilinks (this one), `source_trace` frontmatter paths (0). That is the complete set. Two
adjacent classes came back clean and are recorded so they are not re-swept: no `.py` outside
the deletion set imports anything inside it except `rsc.py:48`/`:50`, already scheduled, plus
three docstring lines in `document_harness/__init__.py:12,16,19` already carried as read 1's
`O-5`; and no `.toml`/`.cfg`/`.ini`/`.yml`/`.json` config pins the deleted test trees, so the
pytest leg loses tests without losing a runner.

**Root shape.** This is read 1's `M-1` one axis over. That finding was *the grep answered a
narrower question than the sentence claims* — byte-readers vs references. The answer widened
the sweep across **files** and left it narrow across **link kinds**, so the assertion (*no
dangling references* / *audit exits 0*) is still wider than the command that backs it. It is
`HD-41` ①'s 量程 defect, in the round that created `HD-41`.

**Minimum fix.** Carry the fourth source file and the wikilink into the three places that
enumerate the blast radius — `split-design.md` §7's table (a row for
`.goals/plans/document-work-assurance-harness-v3.plan.md`, 1 wikilink, `:41`), `HD-39` ②'s
connected list, and the plan's step 12 plus Acceptance — and say *14 条入链（13 markdown + 1
wikilink）· 4 个源文件*, so the count and the kinds travel together. The ruling does not
change: the deletion stays a deletion. Cost the fix carries and which is not mine to resolve
(`R5`): §7 is inside the signed document, so that edit rides the re-signature `HD-40` already
owes; `HD-39` and the plan carry no such cost, and repairing only those two leaves the signed
§7 standing and incomplete — the identical route question read 1 raised and the user answered
once already.

## 5. Low

**`L-1` — three counts were already false in the tree they were committed onto.** `E3` asks
that a figure be re-run *immediately before the claim*; all three were carried across from the
revision where a previous record measured them, by `28c6e26`, the commit whose stated job was
repairing exactly this defect one revision earlier.

```
$ git ls-tree --name-only <rev> -- …/migration/document-work-assurance-v3/ | grep -c '\.md$'
  0db52a1 117 · feb7b48 118 · 6a946ba 119 · 4342c6b 120 · 289f8ab 121 · 33eb722 121 · 28c6e26 121 · a654fb2 121
$ git grep -lE 'interface_version|harness_version|tool_version' 28c6e26 -- . | wc -l   -> 7
```

- **(a)** `split-design.md:79` — *tip 上已 **120***. The tree `28c6e26` was committed onto held
  **121**; `289f8ab` added the fourth record before it. The hedge *并随本轮每份记录增长* covers
  growth *after* the claim, not a figure stale *at* it.
- **(b)** `journal:77` — the same *120 份*, same commit.
- **(c)** `journal:107-110` — *〔量程 = 全仓 tracked〕… **六个文件**命中*. Seven at `28c6e26`;
  the seventh is `v3-checkpoint-read-a2f8c7d.md`, the review record that raised the finding
  this line answers, tracked one commit earlier.

Recorded so the fix is not over-applied: §10.4's *tip 上已 250* **was** correct when written at
`12a28ce` (250 then, 251 now) — genuine in-flight growth, and its hedge holds. Downstream: R1
re-derives the per-file 29/88 list at its own base, so no ruling moves; what breaks is
reproducibility — a reader who runs the stated command gets a different number and cannot tell
whether the record or the command is wrong, which is the whole purpose of `HD-41` ③.
**Bytes**: `120` → `121` at (a) and (b), or drop the tip figure and keep the base pin;
*六个文件* → *七个文件*, naming the record as the seventh. Deadline: the re-signature.

**`L-2` — the `O-1` answer supplies a criterion that does not produce the number it
annotates.** `journal:74-78` now declares *判据 = 全文命中
`p3-corr|p4-bridge|p4-doc|p5a-|p5b-|w1-r1`* and asserts *全文提到产品 run 的 = **63 份***
(scope: that directory's top-level `*.md` @ base `0db52a1`) with *tip 上已 120 份 / 64 份*.
Re-derived over exactly that criterion:

```
0db52a1: total 117 | full-text run-name criterion -> 64
a654fb2: total 121 | full-text run-name criterion -> 66
```

Base is **64**, not 63; the tip pair is **121 / 66**. The finding asked for a criterion
precisely so the figure could be checked, and the criterion now contradicts it. Harm is
bounded and the journal says so itself — *本数已非操作依据* — and the operative split
reproduces exactly (29 / 88 at base under the first-40-lines criterion; 29 product at the tip
too), so this is low, not must-fix. **Bytes**: `63` → `64`, tip pair → `121 / 66`; or delete
the sentence and keep the pointer to §10.1, which the same paragraph already says supersedes
it. Deadline: same as `L-1`.

**`L-3` — the batch's rider triage misses the two riders this split actually touches, and one
of them is the instruction layer's only mechanical guard.** The plan's 随批 rider section
enumerates 4 确定随批 (`RA` · `PD` · `CLI-hist` · `ledger-assert`) and 4 可能被触碰即到期
(`SCC` · `frozen-path-prefix` · `qp-index` · `qp-inert`). Two others meet their own
redeem-when the moment this batch executes, and neither appears:

- **`E10-sync`** — redeem-when *碰 `E10` 成员句的任何批：三处（成员句 / `LAYER` / `EXPECTED`）
  同改并在 commit 正文点名*. Measured against the seven-prefix travel set §10.4 row 1
  enumerates: seven of `E10`'s nine members travel (`document-harness/` ×4, the two
  retired-contract stubs under `migration/…`, `paragraph-map.schema.json`) and the two
  supersessions under `ResearchSystem/contract/` do not — while the plan's Acceptance requires
  *`E2` 冻结面三份签字件的 blob id 与签字记录一致（跨仓后仍可验签）*, so some set must carry
  them. Either way the nine paths change. `tooling/hooks` is itself a travel prefix, so
  `layer_path_check.py` travels, and its `LAYER` constant (`:30-40`) hard-codes all nine
  members as `ResearchSystem/`-prefixed strings; its paired guard asserts `LAYER` equals a
  hand-written literal and travels too. In the new repository both are wrong together: no
  staged path can match, the guard guards nothing, and the battery stays green. §2 schedules
  *三个 harness hook 的路径前缀在 R3 显式更新*, which is the pre-commit script's invocation
  prefix, not `LAYER`'s member paths.
- **`tier-scope` ②** — the surviving half, on the tiering section that `M-1` is about.

```
$ grep -rn 'E10-sync\|layer_path_check\|LAYER' split-design.md journal/…-r0-… plan
  journal:63   … 三个 harness hook（review_freeze_check / layer_path_check / candidate_path_check）
  (no other hit; tier-scope appears nowhere)
```

**No bytes**: whether the membership sentence is re-pathed, whether re-pathing it is design or
a free-channel application, and which repo the two supersessions land in are decisions above
this read (`R5`). Deadline: R1's first declared act, *先声明唯一的 travel 集* — after that
declaration the layer members have new addresses and nothing in the plan is watching them.

**`L-4` — the revision count on the signed document is wrong in three places, and one is
falsified by the commit that writes it.**

```
$ git log --oneline 9736670..a654fb2 -- ResearchSystem/document-harness/split-design.md | wc -l -> 8
  3f4d2b0a(251, signed) -> 3d5eed90(267) -> 74d70ca7(280) -> 067b6c69(290)
                        -> 46b67776(300) -> 2dad0da6(310) -> 9ae5def1(315) -> 3287ab49(346) -> e24f837e(348)
$ same command at 33eb722 -> 7
```

`split-design.md:3` reads *签字后经四轮 read 修改**七次***, written by `28c6e26`, which is the
eighth revision — false at the instant it lands. `plan:97` and `:167` say 七次; true at
`33eb722`, now 8. `HD-40` says *四次以上* and prints the live command, so it stays true and is
the recoverable source. `E12`'s written-tip shape, third instance in one round: read 3's `O-6`
caught 三次 → 四次, read 4's `M-1(d)` caught 三改 → 七改, and the answer to `M-1(d)` reproduced
it at the next value; `HD-40`'s own text already names the shape. No action turns on it — the
re-signature is owed either way — so wording-level under `R9`; recorded because it is the one
number the user reads at the moment of re-signing. **Bytes**: drop the count and keep `HD-40`'s
command, at all three sites.

**`L-5` — `HD-41`'s 起因 miscounts the evidence it rests on, its own enumeration contradicts
it, and the sweep the same commit pastes reports the stale sibling as clean.** The four
records' own summary lines:

```
v3-checkpoint-read-ffbc393.md :7   **Findings: 1 must-fix, 3 low, 5 observations.**
v3-checkpoint-read-0cc45ce.md :8   **Findings: 1 must-fix, 3 low, 5 observations.**
v3-checkpoint-read-b75676e.md :10  **Findings: 2 must-fix, 3 low, 7 observations.**
v3-checkpoint-read-a2f8c7d.md :8   **Findings: 1 must-fix, 5 low, 7 observations.**
                                                 1+1+2+1 = 5
```

`HD-41` reads *R0 四轮独立 read 返**四条** must-fix*, then lists five: 删除不留悬空引用 ·
耦合全在顶层三行 · 其替换句「块外四处」 · `M-2` 的 plan 四处 · `M-1D` 的另四处. The plan's own
Resume pointer gets it right (*`feb7b48`（1 must-fix）· `6a946ba`（1）· `4342c6b`（2 …）·
`289f8ab`（1 …）*), which is what makes the accurate fact recoverable. `split-design.md:326`
still carries the pre-fourth-read form — *R0 的**三轮**独立 read 共返四条 must-fix* — and
`a654fb2`'s body, the first commit to execute `HD-41` ④'s new 留痕 obligation, pastes a sweep
over the four 承载点 and concludes *全部一致、无陈旧*, naming `split-design.md:324` (§11) as one
of them. The grep was run and pasted, as ④ requires; the comparison it exists to enable was not
made. No actor's action changes (the ruling ①–④ is unaffected), so wording-level under `R9`.
**Bytes**: 四条 → 五条 in `HD-41`; 三轮…四条 → 四轮…五条 at `split-design.md:326`.

## 6. Observations

**`O-1` — the v3 block lifts clean under a scope wider than the round measured.** §1's
conclusion rests on a five-token grep (`generate.` / `pipeline.` / `stage_close.` /
`stage_control.` / `GENERATED_DIR`) returning 0 inside `:231`–`:651`, which leaves open whether
some other product symbol — `load_config` is imported at `:49` alongside `GENERATED_DIR` —
appears there. It does not. Enumerating **every** `import` / `from` line inside the block
returns `rsclib.document_harness` (twenty-one lines across the seven `_cmd_v3_*` bodies) plus
stdlib `datetime` and `json`, and nothing else; `load_config`, `GENERATED_DIR` and the product
modules appear nowhere in the block under any spelling. The design's load-bearing claim is
stronger than its stated evidence — recorded because two findings above go the other way, and
this one belongs on the record too.

**`O-2` — the 88 «construction records» bucket is not 88 review records.** Of the 117 files at
base, **14** are not review records at all: five signature records
(`a1-p4-activation-successor-signature` · `a2-p5a-activation` · `a2-p5a-firewall-signature` ·
`a3-p5b-activation` · `a3-p5b-firewall-signature`), the **two retired-contract stubs**
(`v3-harness-operating-contract.md` · `v3-harness-review-contract.md` — both `E10` members),
`supersession-2-signature.md`, two dispatch reads, three notes/handoff, and one design doc.
Under the stated criterion the signature records classify as *product* (they name runs) and
stay; the rest ride in the 88 that travels. `HD-28`'s C tier is *评审记录* and §3's ruling is
*88 份构造记录 travel*, so R1's per-file list will move two instruction-layer members and four
notes under that label. Whether that is right is `HD-28`'s question, not this read's (`R5`);
what is measurable is that the label and the bucket are not the same set.

**`O-3` — five of the seven cross-links §3 hands R1 point at an `E10` member, not at a
construction record.** Re-derived at base, both directions, markdown and wiki:

```
c->p (2)  v3-review-full-c6d4eb4.md -> v3-review-full-0439efe.md · v3-review-verify-d55d5ce.md
p->c (5)  v3-review-full-{0439efe,9c13008,dcfb2f2}.md · v3-review-verify-{d55d5ce,dc1e8a3}.md
              -> v3-harness-review-contract.md
```

The count and the direction split (2 · 5) reproduce exactly, so §10.1 is right and R1's *处理那
7 处真链接* is correctly sized. The shape underneath is `O-2`: five of the seven are product-run
records citing the retired review contract, so what R1 repairs is five links from files that
stay to a file that travels — an instruction-layer member, not a peer record.

**`O-4` — `R6`'s record-title prefix was repaired mid-round; two records cannot be.** `R6`
fixes the title as `V3-REVIEW-RECORD-<ROUND>-<sha>-v1`. Records 3 and 4 carry the prefix
(`V3-REVIEW-RECORD-SPLIT-R0-REREAD-{b75676e,a2f8c7d}-v1`); records 1 and 2 do not
(`V3-SPLIT-R0-{READ,REREAD}-RECORD-{ffbc393,0cc45ce}-v1`), which read 3 raised as its `O-2`.
The cost is that a one-prefix grep for review records misses two of this round's four.

**`O-5` — `E8`: titles conform from `feb7b48` on, bodies still run long.** All fifteen commits
from `feb7b48` carry `V3-…-v1` titles naming the round, and **0** trailer-shaped lines anywhere
in the range. The three newest name their kind — *amendment* (`33eb722`), *自由通道（errata
类）* (`28c6e26`), *ruling* (`a654fb2`) — all inside `E8`'s vocabulary. Non-blank body lines:
**15 / 23 / 21**, against the ten-line discipline set one commit before this range's base.
Measurement, not news: prior records logged 20/26/6/23/20/14/18/17/10, 19/22/18/11/17 and
18/14/23/20. The first nine commits carry `chore(governance):` and name no kind, so §1's
classification table is mine — the work `E8` exists to spare the review side.

**`O-6` — the channel question, restated once and not concluded (`R5`).** Zero of the nine
`E10` members and zero `E2` bytes changed in any of the twenty-four commits (§2), so the
must-fix amendment machinery, its independent re-reads and the free channel were exercised
throughout on a design document, a decision register (`HD-19`: explicitly not a member), a
journal, a plan and the archive. Three prior records put this to the user; it is unchanged. It
matters for exactly one thing, which is independently settled: `E9`'s test — *has a valid
independent FULL already occurred?* — answers **no** for R0, so nothing here consumes the cap
however the commits are classified. The larger shape, also put to the user twice already: the
signature binds the blob at commit 8 of 24 and was recorded at commit 9; the file has grown
251 → 348 lines across eight revisions since, gained a whole section (§11) that did not exist
at signature, and **five independent reads have now closed behind it without any gate that can
return `CHANGES_REQUIRED`.** `M-1` and `M-2` are both findings a signature gate would have had
to answer, and `M-1` is one no channel available to R1 can answer by itself.

**`O-7` — what this range got right.** `M-1D`'s answer is complete at all four sites the
finding enumerated, and the sweep beyond them was real: the plan's step 3 now reads 已裁乙 with
its 改判史 explicitly marked *不是当前状态*, item 3 is struck through and replaced with the two
genuinely open items, the Resume pointer lists four reads with their finding counts and sets
the next base at `289f8ab`, and every residual 待裁 / 甲乙 hit I grepped across the plan sits
inside labelled history, exactly as the commit body claims. The free-channel commit's seven
applications are each right where I could reproduce the command: the 28-site enumeration and
its two-command composition (24 out-of-block token lines plus the four the grep cannot match —
`:48` *generate,* is a comma, `:50` `harness_cli` carries no token, `:674` and `:739` likewise,
and those four are precisely the lines R1 must cut), `grep -c '= sub.add_parser('` → 4 against
the bare substring's 14, the LF/CRLF mechanism, the *245 ≠ 成员集* qualification at §4, the
title and status line corrected to 已签, the `.claude/commands/` unit ambiguity written out
both ways. `HD-41` is well-formed against the register's own rules — scope, status, basis, and
a status note correctly saying it cannot become `implemented` until a design round writes it
into the layer (`HD-2`). What failed, for the fifth and sixth time, is the radius.

## 7. What reproduced exactly

Recorded so these are not re-measured. Each was re-derived here, not read off any document or
prior record.

| claim (subject bytes) | recorded | re-derived |
|---|---|---|
| deletion union | 171 | **171** tracked files (`git ls-files … \| sort -u`), counted not summed |
| the 139 bucket | 14 · 11 · 1 · 81 · 26 · 2 · 2 + 2 contracts | **each exact**; union **139** |
| v1 runtime family, net | 32 | **32**; 139 + 32 = 171 |
| markdown links from outside the set into it | 3 files, 13 links | **3 / 13**, every line number exact (README `:35/:39/:41/:42/:43/:44/:45/:46`; v2 plan `:723-725`; refactor plan `:323/:324`) |
| `repo-audit` link machinery | `cand.exists()` `:103-115`, hard at `:304`, `EXCLUDE` ten items, `ROOT` `:31`, `rglob` `:62` | **exact**; wikilink block `:306`, `sys.exit` `:325`, `base`/`alias` `:86-91`, `WIKI` `:94` |
| `repo-audit` / `ledger_cap_check` at tip | clean | **exit 0** / **exit 0**; ledger **114** lines, riders **38** |
| records in the migration directory | 117 @ base | **117** @`0db52a1`; **121** at tip (see `L-1`) |
| product / construction split, first-40-lines criterion | 29 / 88 | **29 / 88** @ base; 29 product at tip too |
| real cross-links between the two groups | 7 (构造→产品 2 · 产品→构造 5) | **7 (2 · 5)**, direction and endpoints exact |
| `rsc.py` | 856 lines | **856**; `build_parser` `:652`, `main` `:842` |
| out-of-block token lines | 24 | **24** (`49 57 93 95 104 106 116 126 · 134…223 · 850`); in-block **0** |
| block-external coupling enumeration | 28 = 3 + 7 + 15 + `:674` + `:739` + `:850` | **28**; the four non-matching lines are exactly `:48` `:50` `:674` `:739` |
| v1 stage group | 15 within `:134`–`:223` | **15** |
| `:850` | `except stage_control.StageControlFault` in `main()` wrapping `args.func(args)` | **exact** (`:849` call, `:850` handler, `:851` `FATAL:` / return 2) |
| the two `add_parser` greps | 4 and 14 | **4** and **14** |
| travel set, seven prefixes | 245 @ base, 250 @ `12a28ce` | **245** / **250**; **251** at tip |
| commits touching the seven-*path* set | 335 / 720 @ `0db52a1` | **335** / **720**; the printed command runs verbatim |
| `pack_digests` whole-repo `*.py` | 5 hits, 3 of them v2 | **5** — `__init__.py:238`/`:266`; v2 `schemas.py:75`, `resolver.py:272`, `tests/harness/run_tests.py:39` |
| pre-commit hook | 4 python call sites, 6 scripts, untracked | **4** (`:13/:27/:40/:56`), **6**; `contract_provenance_check.py` absent (`tooling/hooks` tracks **4** files) |
| `.claude` inventory | 166 skill files / 3 skills / 0 plugin manifests / 11 commands / 18 `ls-files` | **all exact** |
| `HD-40` signed blob | `3f4d2b0a`, 251 lines, sha256 `8da2d17d…59af` | **exact** — `git cat-file blob 3f4d2b0a \| sha256sum` |
| `p5b-firewall` boundary exclusion | both contracts listed as plain strings | **exact**, `build_run.py:216-217` |
| full battery | eight commands, *nothing fewer* | **8** enumerated at `EXECUTION.md:329-338`; **6** survive the deletion, **2** do not (see `M-1`) |
| `E2` / instruction layer across 24 commits | untouched | **3 blobs SAME, pack 15 / 0 changed, 9 of 9 members SAME** |
| `§live` entries | — | **13** at tip (`HD-41` added); `HD-24` superseded in archive, pointers both ways |

## 8. Coverage and ceilings (`R4`)

**Read in full**: the five non-record files at the tip (`split-design.md` 348 lines, the
journal 134, `HARNESS-DECISIONS.md` 430, the plan 177, and the archive diff); all four review
records committed inside this range; `CONSTRUCTION-CHECKLIST.md`; `EXECUTION.md`'s
*Regression-battery tiering* section; `HARNESS-LEDGER.md`; `HARNESS-RIDERS.md`; the three
newest commit messages in full and all twenty-four titles; the whole range diffstat.

**Sampled**: `rsc.py` — every line matching the five coupling tokens, every `import`/`from`
inside `:231`–`:651`, every `add_parser` registration, the import head, `:674`, `:739`, `:850`,
`main()`; not the whole 856. `Thesis/Work/Tooling/repo-audit.py` — `:25-70`, `:80-130`,
`:295-325`. `layer_path_check.py` — `LAYER` only. `D:/Thesis/.git/hooks/pre-commit` — its
python invocations. The four prior read records — in full for their findings and ceilings,
since this range answers the fourth.

**Probed only** (command or script output, no reading): the 171-file deletion set and its
per-tree breakdown; the three-scan post-deletion link simulation; the eight battery commands
against the deletion set; the 29/88 and 63/64 classifications at two revisions; the cross-link
scan; the record counts at eight revisions; the travel-set and commit counts; the `.claude`
inventory; the `interface_version` scan; the split-design blob chain; `repo-audit` and
`ledger_cap_check`.

**Not read**: `README.md`, `REVIEW.md`, the two retired-contract stubs and
`paragraph-map.schema.json` — all verified byte-unchanged and nothing in this subject depends
on their content; `EXECUTION.md` outside the tiering section; `io-design.md`; the caller-side
product tree; the regression battery (**not run** — this range touches no code).

**`UNVERIFIABLE`, stated rather than folded into supported** (`R4`):

- **The bare-name cross-mention figure (73).** My method — any record's stem appearing as a
  substring in another group's file, minus the linked ones — yields **77**, and §10.1's method
  is not recorded, so I cannot say whether 73 is wrong or measured differently. The claim it
  supports (that the non-link cost is prose-only and machine-invisible) is unaffected, and the
  7 that machines do see reproduces exactly.
- **That deleting the 171 files leaves the surviving battery green.** I established that no
  config or runner pins the deleted test trees, that none of the six surviving battery commands
  imports or validates anything in the set, and that no surviving `.py` imports into it beyond
  the two scheduled `rsc.py` lines. I did not execute the battery, and `rsc.py:850`'s residual
  path remains untested by anything, as read 2 established and this read did not re-test.
- **Process claims marked, not verified**: that this session held only the review role for its
  whole life (`E1`); that the round division, the eight §10 rulings, the `HD-40` signature, the
  量程 method approval and the `HD-41` instruction were given as the repository records them
  (`R7`).
- **The 29/88 classification reproduces the criterion, not its correctness.** It is a
  forty-line heuristic; whether each of the 117 files is truly a product or construction record
  is not something I checked file by file, and `O-2` shows the bucket boundaries do not match
  the labels. R1's *路径清单须逐文件列* inherits that exposure.

**Independence** (`R1`): this session was dispatched, scoped and is reported through the
orchestrator; the executor set none of the four. The worktree was clean at open and the
canonical record path was absent, so no prior draft influenced this read. `M-1`, `M-2`,
`L-1`(a)(b)(c), `L-2`, `L-3`, `L-4` and `L-5` are findings no prior record raised; `M-2` is a
sweep of the class read 1's `M-1` named, extended along the axis that sweep did not cover, and
`M-1` extends it along a second, both re-derived here from the repository.
