# FULL review — `97da1ec..22b27aa` (the E2 re-baseline amendment round)

| | |
|---|---|
| round | FULL, construction-side (`CONSTRUCTION-CHECKLIST.md` R1–R10) |
| subject | `97da1ec0d3639b2a740c3e40d35d7f5d08fdfc58..22b27aa2e9ae3d10539d93a75f1339726af04a67` |
| range content | exactly one commit, `22b27aa` (`V3-RETRO-RULINGS-v1`, kind: amendment) |
| **verdict** | **`CHANGES_REQUIRED`** |
| findings | 1 blocker, 4 low, 5 observations |
| record | this file; the execution side commits it (`R6`) |

`CHANGES_REQUIRED` names one blocker: the amendment falsifies a present-tense assertion in
another instruction-layer member and leaves it standing — and, by the same act, moves that
assertion inside the freeze so it can no longer be corrected without a ruling. Everything
else in the range holds. The amendment's own bytes are sound; every factual assertion in
the E2 hunk and every figure in the `E3` witness correction re-derived exactly.

## 1. Subject, re-derived (`R2`)

Handed one range and nothing else. Round, budget, authorization and every number below are
re-derived from the repository; no reported figure is accepted.

```
$ git rev-parse HEAD          -> 4ab1db1b40fecb424ac7d29be0f9192aa0f67c80
$ git status --porcelain      -> (empty)
$ git log --oneline 97da1ec..22b27aa
  22b27aa V3-RETRO-RULINGS-v1
$ git rev-list --count 97da1ec..22b27aa   -> 1
$ git diff --stat 97da1ec..22b27aa
  ResearchSystem/HARNESS-RIDERS.md                          |  2 +
  ResearchSystem/assurance/templates/run-v2/README.md       | 12 +++++-
  ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md |  7 +++-
  ResearchSystem/document-harness/journal/retro-2026-08-03.md | 43 ++++++++++++++++--
  4 files changed, 57 insertions(+), 7 deletions(-)
$ cat .harness/review-pending.json
  {"kind": "construction-round",
   "subject": "97da1ec0…..22b27aa…", "dispatched_at": "2026-08-03T15:26:09+00:00"}
```

**Round and authorization.** The subject is not at the tip: six commits sit between it and
HEAD. The committed authorization is `HARNESS-LEDGER.md`'s ⛔ P5B precondition ①, which
records that the `E2` re-baseline "欠的不止是读，是一个轮", that the read `c8d9afa` returned
must-fix M-1, that the `E10-D-NARROWING` attempt at remedy (c) was withdrawn in full, and
that "下一步 = remedy (a)：以 `22b27aa` 的层 diff 为 subject 单开一轮 FULL". This dispatch is
that FULL. The rulings themselves were given in chat; their record is the retro journal §7
and the subject's commit body, both committed — `R7` ceiling stated, not a block.

**Changed paths, classified by hand** (not from the commit body):

| path | class | frozen by `E2`? |
|---|---|---|
| `document-harness/CONSTRUCTION-CHECKLIST.md` | **instruction-layer member 1** (`E10`; `layer_path_check.LAYER[0]`) | no |
| `HARNESS-RIDERS.md` | rider bank, pure data table (`R10`) | no |
| `assurance/templates/run-v2/README.md` | template documentation — **not** a layer member; incorporation parked in the I/O design batch | no |
| `document-harness/journal/retro-2026-08-03.md` | journal record | no |

No frozen path is in the diff: the four blobs (`8ad404b1` / `b2dbdf75` / `68031fa2` /
`e1a2f26b`) and the whole `schema/document-assurance-v3/` pack are untouched
(`git diff --name-only 97da1ec..22b27aa -- ResearchSystem/schema/` → empty).

**Tier, re-classified.** The `BATTERY-TIERING` section's doc-only test is path-type plus
tree location: "every changed path is prose/markdown outside the schema, tooling, and
generated trees". All four are. Its exception is "a doc file that code enumerates or tests
pin"; `test_precommit_checks.py` names `CONSTRUCTION-CHECKLIST.md` only as a hand-written
path literal inside a `TempRepo`, and `layer_path_check.LAYER` enumerates the *path*, which
did not change — so no test pins this file's content and the exception does not attach.
**This batch is doc-only by the section's letter**, and the batch-specific-checks-only
choice was correct. The commit body says the opposite; see L3.

## 2. The amendment, against the repository (`R3` — implementation first)

The whole layer delta is one hunk in `E2` (−2/+5):

> ~~when the pack entry joined this list (2026-07-29, fourteen files); a pack file added
> later is not frozen by this rule.~~
> → at the 2026-08-03 re-baseline (fifteen files: the fourteen of the 2026-07-29 entry plus
> `ResearchSystem/schema/document-assurance-v3/paragraph-map.schema.json`, which joined
> 2026-07-31 and which the 保障面二期复盘 found sitting outside the freeze); a pack file
> added after that date is not frozen by this rule until a later re-baseline — new schemas
> stabilize first, which is why this clause re-baselines rather than auto-freezing.

Every factual assertion re-derived by command:

| assertion | command | result |
|---|---|---|
| fifteen pack files at the subject | `git ls-tree -r --name-only 22b27aa -- <pack> \| wc -l` | `15` — holds |
| "the fourteen of the 2026-07-29 entry" | same at `11d147e` (`V3-E2-SCHEMA-PACK-AND-FACT-CORRECTION-v1`, 2026-07-29) | `14` — holds |
| the fifteen are those fourteen plus one | `diff <(ls-tree 11d147e) <(ls-tree 22b27aa)` | one line added, `paragraph-map.schema.json` — holds |
| the fourteen are byte-unchanged since | `git rev-parse` each at `11d147e` vs `22b27aa` | 14/14 identical (`b4ddfcf1` `1bdb2cc2` `6e87fe9b` `ecc23297` `419a767f` `42658e19` `f8a3d2cf` `ed8dd969` `19ab2c86` `f607ffc3` `2350ff96` `3617b74e` `fe436c6a` `0e3447f5`) — the re-baseline launders nothing |
| "which joined 2026-07-31" | `git log --diff-filter=A -- <pack>/paragraph-map.schema.json` | `d50d9e5`, 2026-07-31 — holds, and it is the pack's only ever addition after the entry |
| the one added backtick path resolves | `layer_path_check.unresolved_tokens` over the real added lines | `[]` — holds (mutation-tested, §4) |

**The escape clause does what ruling (6) chose.** "a pack file added after that date is not
frozen … until a later re-baseline" preserves the stabilize-then-freeze design the ruling
kept, rather than the rejected auto-freeze. The design is corroborated in the repository:
the fifteenth file was itself edited *after* joining the pack and *before* the re-baseline
— `34cf85b` (2026-08-01) rewrote its `description`'s SHA-256 clause, `6f09935b → c2b713bf`
— which is precisely the iteration window the escape clause exists to leave open, and it
would have been barred had the pack auto-frozen.

**Boundary shape intact.** "Four blobs and one directory, both decidable by inspection"
still parses: the boundary remains four blob ids plus one directory-at-a-commit, and the
fifteen are pinned as fourteen-by-dated-entry plus one named file.

## 3. The `E3` witness correction, re-derived

The round's other substantive claim is the run-v2 README's correction of the
`BATTERY-TIERING` witness. The prior read explicitly did not re-run it ("The battery and
suites — not re-run"), so this is first independent verification.

```
$ python  # mtimes of ResearchSystem/assurance/runs/p5a-shells/evidence/chk-*.out.txt
  chk-*.out.txt files: 15
  first 00:08:34  last 00:10:56  span 142.02s
  00:08:39.998957     3.89s  BATTERY  chk-compile-check
  00:08:50.988142     2.48s  BATTERY  chk-p2-golden
  00:08:53.240500     2.25s  BATTERY  chk-p4-golden
  00:08:55.258002     2.02s  BATTERY  chk-p5a-golden
  00:10:43.543072   108.29s  BATTERY  chk-pytest
  00:10:54.911278     1.89s  BATTERY  chk-schema-fixtures
  battery legs inside the pass: 120.82s / 142.02s = 85.1%
  checks with a JSON result: 17
```

| README claim | re-derived | verdict |
|---|---|---|
| "ran its 17 checks in 2m22s" | 17 `check-chk-*.json`; span of the 15 that wrote `.out.txt` = 142.02s = 2m22s | holds (the method is stated inline; the two checks writing no output — `chk-boundary`, `chk-record-exists` — sit inside the window, not beyond it) |
| "the pytest leg alone ~108s of it" | 108.29s (`chk-p5a-golden`→`chk-pytest`); pytest's own line reads `556 passed in 102.02s` | holds |
| "the battery is ~85% of an evidence pass" | six legs named by the section's own bullet 2 = 120.82s / 142.02s = **85.1%** | holds exactly; the journal's "≈120s / 142s" is the same computation |
| "a pass is ~2.4 minutes, not ~10" | 142.02s = 2.37 min | holds |
| "wrong in magnitude by ~4×" | 10 / 2.4 = 4.2; 8 / 2 = 4 | holds |
| "tallies reproduce exactly" (P2 29 + P4 80 + P5A 32 + fixtures 58 + pytest 556) | ran all six legs live at HEAD | **29 / 80 / 32 / 58 / 556, all rc=0**, `compile --check` clean — holds |
| "that FULL's O2 had already marked the minutes half as carrying no repo lock" | `v3-review-full-4f88dce.md` O2 is titled "the minutes witness has no repo lock" | holds |
| "the battery run directly totals 130s" | my run: five fast legs 2.16s (the journal's "5 腿 2.1s"), pytest 82.87s, **total 85.03s** | wall clock is machine- and load-variable; the direction is unaffected — 85s is further from ≈8 minutes, not closer. Disclosed, not a finding. |

The relative link the correction adds (`../../../document-harness/journal/retro-2026-08-03.md`)
resolves; `repo-audit.py` exits 0 over the tree.

## 4. Do the guards bind (`R8` / `E4`)

This round adds no guard. The one that binds on its diff is `layer_path_check.py`, which
scans only the lines a staged diff *adds* to a layer member. Exercised against the subject's
real added lines, then mutated to the defect shapes this hunk could actually have carried —
`unresolved_tokens(repo_root, "…/CONSTRUCTION-CHECKLIST.md", <added lines>)`:

```
real hunk (unmodified)                 -> []
typo, still .json, RS-rooted           -> [('…/paragraph-maps.schema.json', 'does not resolve from the repo root')]
wrong dir, RS-rooted                   -> [('…/document-assurance-v2/paragraph-map.schema.json', 'does not resolve from the repo root')]
prefix dropped (dcced4e shape)         -> [('schema/…/paragraph-map.schema.json', 'resolves only under ResearchSystem/ — prefix missing')]
extension mangled (out of PATHLIKE)    -> []
```

The guard passes on the real hunk and fires on all three realistic defect shapes; the fourth
mutation produces a token the docstring documents as deliberately skipped. Binding force
shown, negative control included — the commit body's claim ("its one added backtick path
resolves") is verified, not accepted.

The pre-commit hook was read in full at the common dir (`D:/Thesis/.git/hooks/pre-commit` —
this is a worktree; `git rev-parse --git-common-dir` → `D:/Thesis/.git`). It runs
`repo-audit.py`, then existence-guarded `contract_provenance_check.py` (absent since
2026-07-28, skipped), then `review_freeze_check.py` / `ledger_cap_check.py` /
`layer_path_check.py`. All four present guards exit 0 on the current tree.

`test_precommit_checks.py`'s `LayerMembership.EXPECTED` is a hand-written nine-path literal
compared against `layer_path_check.LAYER`, with `test_every_member_is_scanned` proving each
member is reached — `E5` observed, expectation independent of the guarded module.

**`E2` has no mechanical enforcement anywhere in the repository.** A search for the four
frozen blob ids and for `frozen`/`freeze` outside markdown returns nothing in tooling,
hooks, or CI. The freeze is prose-only. This is the fact that decides B-1's severity.

## 5. Findings

### Blocker

**B-1 — the amendment falsifies the frozen file's own description of its freeze status, and
freezes the falsehood in the same act.**

**Location.** `ResearchSystem/schema/document-assurance-v3/paragraph-map.schema.json`,
`description` (blob `c2b713bf` at the subject and unchanged at HEAD), final clause:

> "Authored run-locally, zero signed bytes; joined the pack after 2026-07-29, **so it is not
> part of the E2-frozen surface**."

**Ground truth it violates.** `E2` as amended by this very commit: the frozen list is "every
file the `ResearchSystem/schema/document-assurance-v3/` pack held at the 2026-08-03
re-baseline (fifteen files: … plus
`ResearchSystem/schema/document-assurance-v3/paragraph-map.schema.json` …)". The file is
named in the freeze by the same hunk that leaves it asserting it is outside the freeze. The
"so" makes the clause a live inference from `E2`'s text, not a dated note — there is no
reading on which it survives the amendment.

**Why this is not wording-level under `R9`.** `R9` requires that the fix change no actor's
action and that the accurate fact be recoverable from adjacent text. Both fail. The clause
answers a **permission** question — may these bytes be edited without a ruling — and answers
it wrongly; the adjacent text is the falsehood itself, and the correct fact lives in a
different file. `E2` has zero mechanical enforcement (§4), so this prose *is* the control:
the only thing standing between an editor and a freeze violation is what the file says about
itself, and the most proximate copy now says "go ahead". The clause is also not incidental —
it is instruction-layer text three times over (`E10`'s "schema `description` strings when
amended"; `layer_path_check.LAYER[8]`; the read chain's member 9), and a prior independent
read certified it as true (`v3-checkpoint-read-d01615b.md` §4: "…so it is not part of the
E2-frozen surface" — holds"). The amendment inverted a checked, load-bearing assertion
without touching it.

This is the first bite of the freeze/layer overlap the prior read reported as O-1, and it
bites in the direction that costs: not "a future amendment will be awkward", but "the gap
the round exists to close is, in the file's own words, still open".

**Minimum fix.** The clause changes — `E6`: the fix is that text changing, and a rule added
about it is not the fix. Smallest form: replace the final clause so it states that the file
joined the pack 2026-07-31 and is frozen as of the 2026-08-03 re-baseline. Nothing else in
the description needs to move, and the edit adds no backticked path, so `layer_path_check`
stays green.

**The fix touches `E2`'s own frozen surface**, so it is not free-standing: it needs the
user's ruling reopening the freeze for this file, in the same act — the pattern rider `O-2b`
already records for `local-check-spec` ("属 `E2` 冻结面，须裁决重开才能兑"). `E9`'s repair
leg is "one **user-approved** fix", so that approval is the leg's normal precondition rather
than an extra gate. If the user declines to reopen, the honest terminal state is `E2`'s own
second branch — stop with `SPEC_GAP` and record it — not leaving the contradiction standing.
Whether ruling (6) should instead be narrowed or reverted is the user's question (`R5`); a
reviewer's subject is the text that is there.

### Low (non-blocking — `R3`: not inflated; `R10` leaves spend-vs-bank to the user at closeout)

**L1 — the retro's §1 line-count row is invalidated by this same commit's own edit (`E3`
measure-last).** §1 reports "指令层 9 成员总行数 **901**" and "三份指令文件行数 573（161 +
259 + 153）". Both were true at `97da1ec`; the E2 hunk in `22b27aa` is +3 lines, so at the
subject the same measurements read **904** and **576（164 + 259 + 153）**. `E3`'s rule is
"a figure is invalidated by any later change to what it measures" — here the invalidating
change is in the same commit. Magnitude is immaterial (0.3%), and every other §1 figure I
could re-derive is exact: 22 owned clauses (`E1–E12`/`R1–R10`); 74 record files across 6
families (26+24+8+4+2+10); 62 round records totalling **15,196** lines; pack 15 of 34
schemas. The class is what is worth naming, not the drift.

**L2 — rider `CLI-hist` cites the wrong section as its source.** The row's source column
reads "retro-2026-08-03.md §5；用户裁决 2026-08-03". §5 is 独立 repo 拆分 — 三硬伤现状 and
says nothing about the command groups; the content the row summarizes is §7 ruling 4 (with
§4 as its version-isolation context). Verified at the subject, so this is not later drift:
`git show 22b27aa:…retro-2026-08-03.md | grep -n '^## '` puts §5 at line 94 and §7 at 111,
and `rsc.py` appears only at §5's cross-root row (about `rsc.py:390`) and at §7 ruling 4.

**L3 — the commit body misstates its own tier rule.** It says "the E2 amendment touches an
instruction-layer member, so this batch is not doc-only by the BATTERY-TIERING section's
letter". The section's doc-only test has no instruction-layer term; it is path type plus
tree location, and all four changed paths satisfy it (§1). The batch then ran exactly the
doc-only tier's checks, so nothing owed was skipped — I re-ran the full battery anyway and
it is green. The risk is precedent, not this batch: a future round citing this one has a
recorded example of declaring a non-doc-only tier and skipping the battery on ad-hoc
grounds. The section's own "review can re-classify it" is the mechanism, and §1 is the
re-classification.

**L4 — `rsc.py:48` is named as the site of both historical command groups; it is the site of
one.** Rider `CLI-hist` and retro §7 ruling 4 both read "`rsc.py:48` 暴露的 `harness` /
`stage` 两个历史命令组". Line 48 is `from rsclib.harness import cli as harness_cli`, whose
group is registered at `rsc.py:707` (`harness_cli.register(sub)`); the `stage` group comes
from line **46**'s `stage_control, stage_close` import and its subparser block at 642–703.
A redeemer anchored on line 48 alone would leave the `stage` group behind. The row names
both groups in words, so the accurate fact is recoverable from the row itself — hence low.
The rest of ruling 4's grep evidence is exact: `document_harness/` has **zero** import
statements naming `rsclib.harness` (the three grep hits in `__init__.py` are docstring
prose), and exactly two live CLI tests invoke the historical groups —
`tests/harness/run_tests.py:725` (`test_cli_validate_and_resolve`, method at :722) and
`tests/stage_control/run_tests.py:182`.

### Observations (`R5` — reported; the conclusions are the user's)

**O-1 — the freeze and layer registers now overlap, and B-1 is its first cost.**
`paragraph-map.schema.json` is simultaneously `E2`-frozen and `E10` member 9. Concurs with
the prior read's O-1, which reported the shape prospectively; B-1 is that shape realized
inside the same commit that created it. Whether the two registers should overlap is the
user's question. Related: the C4 `O-1` ruling already contemplates a future paragraph-map
design batch that would "动冻结面" — the amendment raises that batch's cost.

**O-2 — two decidability probes on the amended clause, both decision-invariant.** (a) The
operative set is moment-granular ("every file the pack held at the 2026-08-03 re-baseline")
while the escape clause restates it day-granular ("added after that date"); a pack file
added later on 2026-08-03 would fall in neither. The operative half governs, so nothing
diverges, and no such file exists (pack is 15 at the subject and at HEAD). (b) The clause is
fully decidable today by listing the pack, but names only one of the fifteen; once a
sixteenth lands, deciding membership needs the 2026-08-03 tree. That is the same property
the replaced text had — no regression, and the amendment slightly improves it by naming the
fifteenth.

**O-3 — rider `CLI-hist` carries narrative against `R10`.** The row's `what` cell runs three
clauses plus a parenthetical grep citation plus a consequence clause — the longest row in a
five-row bank whose header declares it a "Pure data table" and whose governing rule says "no
narrative — the source records hold it". Reported because the bank's discipline is the thing
that keeps it cheap, not because this row misleads.

**O-4 (outside the range, live-state note) — retro §7 item 6 is one step behind its own
ledger.** The errata added at `cd4c09e` corrects the rider misclassification and concludes
"read 是**前置条件**而非可搭车的欠账". The read has since returned M-1 establishing that a
*round* is owed, and `HARNESS-LEDGER.md`'s precondition ① records that. The journal still
frames the obligation as a read. Noted so the closeout, which will touch this file, sweeps
it; not a finding against the subject.

**O-5 — the dispatch's subject is wider than the ledger's phrasing, correctly.** The ledger
authorizes "以 `22b27aa` 的**层 diff** 为 subject"; the handoff was the whole range, four
files. `E12` forbids a per-acceptance argument, so a layer-only subject was not expressible
as a handoff — the wider range is the conforming form, and B-1 was found in the layer half
regardless. Noted so the closeout does not read the width as scope drift.

## 6. Boundary and record conformance — second (`R3`)

- **`E1`.** One role per session. My session holds review only; I authored nothing in the
  repository but this record. That the executor's session held one role is a process claim —
  marked, not verified (`R4`).
- **`E2`.** No frozen path in the diff (§1). The commit amends `E2`'s *text*, which is a
  different act from touching bytes `E2` names — `CONSTRUCTION-CHECKLIST.md` is not among
  the four blobs or the pack.
- **`E3`.** The witness correction is measured and its output pasted (§3) — the standard the
  rule asks for, met. L1 is the one figure that fell to the same commit's own edit.
- **`E8`.** Title `V3-RETRO-RULINGS-v1` conforms to `V3-<ROUND>-v1`; kind named
  ("Kind: amendment", in the rule's vocabulary); one dense paragraph; no trailers; a new
  commit, not an amend. Explicit-path staging leaves no post-hoc trace — unverifiable,
  disclosed. Not pushed (`git rev-list --count origin/main..HEAD` → 430, user-gated by the
  2026-07-30 ruling).
- **`E9`.** No `v3-review-full-*22b27aa*` or `v3-review-verify-*` exists for this subject;
  the only prior record is `v3-checkpoint-read-22b27aa.md`, a read, which spends nothing
  (`R3`). So this dispatch is the round's FULL, and the repair leg and targeted VERIFY are
  unspent — B-1's repair is the round's one user-approved fix and obliges the VERIFY. Window
  intact: the newest commit is `4ab1db1` at 2026-08-04 01:12:17 +1000, before the marker's
  01:26:09; since dispatch the branch has taken no commit, and this record is the only one it
  admits.
- **`E10`, opening layer coverage.** The commit body's citation is exact. `git rev-parse`
  over the nine members at `22b27aa^` / `22b27aa` / `HEAD`: member 1 `02461be7 → 2108635f`
  (this edit, the only member in the diff, and still the blob at HEAD — the
  `E10-D-NARROWING` round returned it byte-for-byte); the eight carried forward —
  `f3a31208` `bd490c8b` `c19d8cb9` `17ff31bb` `52a97a48` `68031fa2` `e1a2f26b` `c2b713bf` —
  are identical at all three points. The cited record `v3-review-full-4f88dce.md` §4 does
  state all nine blob ids in its own text, which is what `E10` makes citation depend on. The
  nine-member set equals `layer_path_check.LAYER` at the subject.
- **`E10`, reliance.** Re-derived rather than taken from the errata: no commit after
  `22b27aa` touches `ResearchSystem/schema/document-assurance-v3/`
  (`git log 22b27aa..HEAD -- <pack>` → empty), so no round's `E2` boundary check could turn
  on fourteen-versus-fifteen. The `E10-D-NARROWING` round's changed path was
  `CONSTRUCTION-CHECKLIST.md`, outside the pack under either text. No reliance has occurred.
- **`E11`.** The preview card is not repository-visible; the authorization is (ledger
  precondition ①). `R7` — ceiling stated, not a block.
- **`R10`.** `CLI-hist` names its target files and gives two touch conditions with no
  deadline, which is right for debt whose value does not expire; its source pointer is wrong
  (L2) and its cell carries narrative (O-3). The `E2-rb` row in the subject was the
  misclassification the read caught; `cd4c09e` deleted it before any FULL occurred, which
  `E9`'s test makes a pre-submission correction consuming nothing. Verified applied, not
  accepted: the bank at HEAD holds five rows (F-c, O-2b, SCC, RA, CLI-hist), and §7 item 6
  carries the errata inline.

## 7. Coverage disclosure (`R4`)

**Read in full:** `CONSTRUCTION-CHECKLIST.md` (164 lines, blob `2108635f`, identical at the
subject and HEAD — my standing instructions and member 1); the superseded review-contract
stub that routed me to it; the subject's complete diff and commit body; the base commit
`97da1ec`'s body; `retro-2026-08-03.md` (all sections, at the subject and at HEAD);
`HARNESS-RIDERS.md` (15 lines); `HARNESS-LEDGER.md` (117 lines); `layer_path_check.py` (105
lines); the pre-commit hook at the common dir; run-v2 `README.md` §Regression-battery
tiering and its neighbours (100–163); `cd4c09e`'s body and diff.

**Sampled:** `v3-review-full-4f88dce.md` §4 and O2; `test_precommit_checks.py` (:20–40,
:165–200); `rsc.py` (:1–80 and the subparser registration lines); the p5a-shells check
specs and the six battery legs' `.out.txt` heads and tails; `34cf85b`'s body and its
paragraph-map diff; the 26 FULL records' verdict lines by script, with three resolved by
hand (`0439efe` / `c6d4eb4` declare the older `PASS`; `0b8b824` declares
`REVIEWED_NO_BLOCKER` at :190).

**Probed only:** pack `ls-tree` counts and per-file blob equality at `11d147e` / `22b27aa` /
`HEAD`; `git log --diff-filter=ADR` over the pack's whole history; per-commit path lists for
`22b27aa..HEAD`; evidence `chk-*.out.txt` mtimes; `origin/main..HEAD` count; the freeze
grep across non-markdown files.

**Ran:** the full six-leg battery at HEAD — `run_tests.py` 29, `run_p4_tests.py` 80,
`run_p5a_tests.py` 32, `validate_fixtures.py` 58, `rsc.py compile --check` clean,
`pytest -q` 556 passed — all rc=0, total 85.03s; `repo-audit.py` exit 0; the four present
pre-commit guards, all exit 0; `layer_path_check.unresolved_tokens` on the real hunk plus
four mutations.

**Read after forming my own conclusions, and disclosed as such:**
`v3-checkpoint-read-22b27aa.md` (219 lines). My independent pass agrees with it on all
shared ground and adds §3 (which it declares out of scope: "The battery and suites — not
re-run") and B-1. B-1 sits in the gap its own method names: its staleness sweep grepped "the
eight unchanged members" for the delta's vocabulary, and member 9 — the file the amendment
freezes — was the one member outside that sweep.

**Not verified:** that this review ran in a fresh context (process claim, marked). The six
rulings beyond their in-repo records (`R7`). The retro's subagent-reported token figures
(≈525k / ≈738.5k / ≈426.3k / 1.69M) and its 42-rounds / 16-events counts — the journal's own
coverage disclosure declares these unrechecked, and I did not recheck them; the countable
figures I could reach are listed in L1 and all hold. Mutation proves `layer_path_check` has
binding force on the shapes tested, not that its force is sufficient.

**Ceiling.** What is established here is that the amendment's bytes match the repository,
that the `E3` correction's every figure re-derives, that the one guard on this diff binds,
that the citation chain and the no-reliance claim hold, and that one instruction-layer
assertion the amendment falsified is still standing inside the freeze it created. Whether to
reopen the freeze, narrow ruling (6), or take `E2`'s `SPEC_GAP` branch is the user's call.
