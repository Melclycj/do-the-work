# Targeted VERIFY — `22b27aa..c05d052` (the E2 re-baseline design round's repair)

| | |
|---|---|
| round | targeted VERIFY, construction-side (`CONSTRUCTION-CHECKLIST.md` R1–R10) |
| subject | `22b27aa2e9ae3d10539d93a75f1339726af04a67..c05d052b865d0702effb63866faa2c2e03c5d9e6` |
| range content | 10 commits; the repair under review is `c05d052` alone (`V3-E2-REBASELINE-DESIGN-REVIEW-FIX-v1`, kind: review fix) |
| **verdict** | **`REVIEWED_NO_BLOCKER`** |
| findings | 0 blocker, 4 low, 4 observations |
| record | this file; the execution side commits it (`R6`) |

All five accepted findings are closed, and each was re-derived here rather than accepted:
B-1's replacement clause is true against the repository at the bytes, L1's two counts are
exact, L2's section pointer resolves, L4 now names both command-group sites, and L3's
routing landed with faithful content. The repair adds no rule and no machinery to close a
finding that named text as wrong (`E6`) — no `.py` file changes anywhere in the range.
The full battery is owed by the repair's own tier and is green when re-run at `HEAD`.

The four lows are all reproducible defects the repair left or introduced; none of them
would have changed the fix, which is why none is inflated. Two matter more than the
others: the class B-1 belongs to survives four lines below a hunk this repair edited
(V-1), and the user ruling that let this repair touch a frozen file exists only in its own
commit body (V-2).

## 1. Subject, re-derived (`R2`)

Handed one range and nothing else. Round, budget, authorization and every number below are
re-derived from the repository; no reported figure is accepted.

```
$ git rev-parse HEAD                     -> c05d052b865d0702effb63866faa2c2e03c5d9e6
$ git status --porcelain                 -> (empty)
$ git rev-list --count 22b27aa..c05d052  -> 10
$ git rev-list --count c05d052..HEAD     -> 0
$ cat .harness/review-pending.json
  {"kind": "construction-round",
   "subject": "22b27aa2…..c05d052b…", "dispatched_at": "2026-08-03T16:23:44+00:00"}
$ git log -1 --format=%cI HEAD           -> 2026-08-04T02:23:34+10:00
```

**Which round, and which leg.** The range's base is the subject of the FULL that ran one
commit ago, not the repair's parent — so eight of the ten commits belong to work already
reviewed and closed. Classified by hand from each commit's own diff:

| commit | belongs to | reviewed by |
|---|---|---|
| `7fde391` `cd4c09e` | 保障面二期复盘 closeout + errata | — (`cd4c09e`'s effect on `E2` was the read's subject) |
| `c8d9afa` | the `E10` read record of `22b27aa` | is itself a record |
| `9dcb783` `120e8ec` `440e205` `440d79b` `4ab1db1` | round `E10-D-NARROWING`, whole | `120e8ec` (FULL) + `440d79b` (VERIFY) |
| `15b6e34` | the FULL record of this round | is itself a record |
| **`c05d052`** | **this round's repair — the subject of this VERIFY** | this record |

`git diff --stat 22b27aa..c05d052` confirms the width is inert:
`CONSTRUCTION-CHECKLIST.md` does not appear in the net diff at all, because
`E10-D-NARROWING` withdrew its own candidate whole. Net across ten commits: four review
records added (1,252 lines), two ledgers and one journal edited, one schema line replaced.

**Budget (`E9`).** The round's FULL occurred and its record landed (`15b6e34`,
`CHANGES_REQUIRED`, 1 blocker / 4 low / 5 observations). `E9`'s test — *has a valid
independent FULL already occurred?* — is therefore yes at `c05d052`, so that commit is the
round's one user-approved fix and obliges exactly this VERIFY. One FULL, one fix, one
VERIFY: the cap is met, not exceeded, and the closeout is the remaining leg. Consequence
the closeout inherits: **the fix leg is spent**, so none of the four lows below can be
applied as a second repair without `E9`'s "exceeding an approved fix boundary requires
saying so".

**Window (`E9`).** The marker was written 2026-08-04 02:23:44 +1000; `HEAD` is stamped
02:23:34 +1000, ten seconds earlier, and `git rev-list --count c05d052..HEAD` is 0. Since
dispatch the branch has taken no commit, and this record is the only one it admits.

**Changed paths of the repair, classified by hand** (not from the commit body):

| path | class | frozen by `E2`? |
|---|---|---|
| `schema/document-assurance-v3/paragraph-map.schema.json` | **instruction-layer member 9** (`E10`; `layer_path_check.LAYER[8]`) **and** pack file 15 | **yes** — by the very amendment this round reviews |
| `HARNESS-LEDGER.md` | ledger pointer file, `ledger_cap_check` bound | no |
| `HARNESS-RIDERS.md` | rider bank, data table (`R10`) | no |
| `document-harness/journal/retro-2026-08-03.md` | journal record | no |

**Tier.** A schema-pack file is in the diff, so the run-v2 `Regression-battery tiering`
section puts this batch squarely in "Schema, tooling, or generated surfaces touched: the
full battery runs". The commit declares that tier and it is correct — re-derived from the
diff, not read off the body.

## 2. The accepted findings, re-derived (`R3` — implementation first)

### B-1 — closed, and the replacement clause is true

The one hunk in the frozen file, `−1/+1`:

> ~~Authored run-locally, zero signed bytes; joined the pack after 2026-07-29, **so it is
> not part of the E2-frozen surface**.~~
> → Authored run-locally, zero signed bytes; joined the pack **2026-07-31, and is part of
> the E2-frozen surface as of the 2026-08-03 re-baseline**.

Every assertion in the new clause re-derived by command:

| assertion | command | result |
|---|---|---|
| joined the pack 2026-07-31 | `git log --diff-filter=A -- <member 9>` | `d50d9e5`, 2026-07-31 (`V3-PHASE-C4-M11-v1`) — holds, and it is the pack's only addition ever after the 2026-07-29 entry |
| is inside the freeze as of the re-baseline | `E2` at `HEAD` names the file by full path inside "fifteen files" | holds — the amended text and the description now agree |
| the pack is still fifteen | `git ls-tree -r --name-only HEAD -- <pack> \| wc -l` | `15` |
| the freeze is otherwise unmoved | per-file blob compare `22b27aa` vs `HEAD` across all 15 | 14 identical, 1 changed (this file) — no other frozen byte moved |
| the file is still valid JSON | `json.loads(read_bytes())` | OK; keys, `$id`, `$defs` untouched; only `description` differs |

Two properties of the replacement worth recording because they were not required and are
better than the minimum. It is **dated, not inferential** — the old clause said "*so* it is
not part of…", a live inference from `E2` that any later amendment could invert silently;
"as of the 2026-08-03 re-baseline" is anchored to an event and cannot rot the same way. And
it adds **no backtick token**, so `layer_path_check` has nothing new to resolve (§4).

`E6` is met in the strict sense the rule asks for: the finding named text as wrong, and
that text is what changed. Nothing in the range adds a rule, a clause, a guard or a test
about the defect — `git diff --name-only 22b27aa..c05d052 | grep '\.py$'` is empty.

### L1 — closed exactly

Retro §1's two rows now read `576（164 + 259 + 153）` and `**904**`. Re-derived by `wc -l`
over the nine members at `HEAD`:

```
164  CONSTRUCTION-CHECKLIST.md      5  v3-harness-operating-contract.md
 37  README.md                      5  v3-harness-review-contract.md
153  EXECUTION.md                 124  …supersession-1.md
259  REVIEW.md                    113  …supersession-2.md
                                   44  paragraph-map.schema.json
                                  ---
                            total  904
```

164 + 259 + 153 = 576 for the three prose instruction files; 904 for all nine. Both exact.
The `E3` hazard that produced L1 in the first place — a figure invalidated by the same
commit that writes it — does not recur here: the repair's only line-count-affecting edit
replaces one line of member 9 with one line (44 before, 44 after), so 904 is still true at
`HEAD` after the repair, and stays true after this record lands, since a file under
`migration/` is not a member.

### L2 — closed

Rider `CLI-hist`'s source cell now reads `retro-2026-08-03.md §7 裁决 4（§4 为版本隔离上下
文）；用户裁决 2026-08-03`. Verified against the file's own headings at `HEAD`: §4 is
`版本隔离（v1/v2/v3）` at line 84, §5 is `独立 repo 拆分 — 三硬伤现状` at line 99, §7 is
`用户裁决` at line 116 and its ruling 4 (lines 140–145) is where the command-group content
actually lives. The pointer now resolves to the content it summarizes.

### L4 — closed in substance, with one new inaccuracy (V-3 below)

Both the rider row and retro §7 ruling 4 now name two sites instead of one:
`harness`（`rsc.py:48` 导入、`:707` 注册）and `stage`（`rsc.py:46` 导入、`:643` 起的子解析器
块）. Re-derived at the bytes:

```
rsc.py:46   from rsclib import generate, pipeline, stage_close, stage_control
rsc.py:48   from rsclib.harness import cli as harness_cli
rsc.py:642  stage = sub.add_parser(
rsc.py:643      "stage",
rsc.py:647  stage_sub = stage.add_subparsers(dest="stage_operation", required=True)
rsc.py:707  harness_cli.register(sub)
```

Three of the four anchors are exact. The finding's stated harm — a redeemer anchored on
line 48 alone leaving the `stage` group behind — is removed: `stage` now has its own import
line and its own registration site. The fourth anchor is one line off; see V-3.

### L3 — routed, and the routed content is faithful

Not repairable in place (a misstatement inside an already-landed commit body), so the FULL
left it to a ruling. It is now one entry in `HARNESS-LEDGER`'s rulings block:

> **L3（2026-08-04 设计轮 FULL）**：`22b27aa` 正文自述"非 doc-only"有误——BATTERY-TIERING
> 判据是路径类型+树位置、无指令层项，那批实为 doc-only 且已跑该档检查，无漏跑；风险仅在先例，
> 勿引作跳电池依据。

Checked against the governing text rather than against the FULL: the run-v2
`Regression-battery tiering` section's doc-only test reads "every changed path is
prose/markdown outside the schema, tooling, and generated trees" — path type plus tree
location, with no instruction-layer term anywhere in the section. The entry states the rule
correctly, states that nothing owed was skipped, and confines the risk to precedent. That
is the finding, not a softened version of it.

## 3. The rest of the repair diff

Four files, and nothing in them beyond the five findings. Checked for the changes a repair
of this shape can smuggle:

- **No observation was quietly acted on.** O-1…O-5 are untouched, as the commit body says.
  Retro §7 item 6 still frames the re-baseline's obligation as a read (O-4) and ends the
  file at line 160; the ⛔ ledger block is unedited except for the appended L3 entry.
- **The rider bank is still five rows.** `CLI-hist` was edited, not duplicated; no row was
  added or deleted, so no redemption is silently claimed.
- **The `CLI-hist` `what` cell grew 263 → 307 characters** and remains by far the longest in
  the bank (next longest: 99). The growth is target anchors, which `R10` explicitly wants
  ("A row names its target file(s) or clause"), and the narrative clauses O-3 objected to
  are unchanged — so O-3's substance is neither repaired nor worsened, only its symptom is
  more pronounced. Measured and reported rather than counted as a finding.
- **The ledger grew 117 → 119 lines** against `ledger_cap_check`'s hard cap of 120. See O-3.

## 4. Do the guards bind (`R8`)

The repair adds no guard, so there is nothing to mutation-test under `E4`. The guard that
binds on this diff is `layer_path_check.py`, and this is the first time it has ever bound on
**member 9**: the member joined `LAYER` at `ace0845` (2026-08-01), and `c05d052` is the only
commit to touch the file since. Exercised against the real added line, then mutated to the
defect shapes a `description` edit on a pack schema could actually carry:

```
member in LAYER: True   index: 8   added lines: 1
real added line                                  -> []
typo in pack path (RS-rooted)                    -> [('…/paragraph-maps.schema.json', 'does not resolve from the repo root')]
wrong pack dir (RS-rooted)                       -> [('…/document-assurance-v2/paragraph-map.schema.json', 'does not resolve from the repo root')]
prefix dropped (dcced4e shape)                   -> [('schema/…/paragraph-map.schema.json', 'resolves only under ResearchSystem/ — prefix missing')]
NEGATIVE CONTROL: correct pack path              -> []
NEGATIVE CONTROL: sibling path (file-dir relative) -> []
```

Fires on all three realistic defect shapes from within member 9's own directory context,
silent on both controls. Binding force shown for this member; `R4` — that is not a claim
that its force is sufficient, and the real added line contains zero backticks, so on this
particular diff the guard had nothing to decide.

**The battery, re-run at `HEAD`** rather than inherited from the commit body:

```
run_tests.py        tests: 29   passed: 29   failed: 0   RESULT: OK
run_p4_tests.py     tests: 80   passed: 80   failed: 0   RESULT: OK
run_p5a_tests.py    tests: 32   passed: 32   failed: 0   RESULT: OK
validate_fixtures.py  cases: 58   matched: 58   unexpected: 0   RESULT: OK
rsc.py compile --check   161 md scanned, 153 objects, 0 error(s) 0 warning(s)  exit 0
pytest -q           556 passed in 88.79s
repo-audit.py       RESULT: clean (exit 0)
review_freeze_check / ledger_cap_check / layer_path_check   rc=0 / 0 / 0
```

29 / 80 / 32 / 58 / 556 reproduce the commit body's tallies exactly. Wall clock differs
(88.79s vs the body's 95.05s) and is machine- and load-variable; disclosed, not a finding.
The guards were run on a clean tree, where they exit 0 with nothing staged — the commit's
claim that each exited 0 **over the staged diff** is unreproducible after the fact, since
staging leaves no trace. Disclosed as unverified rather than folded into supported.

## 5. Findings

### Low (`R3`: none inflated — the fix leg is already spent, so each of these banks or rides a later batch unless the user reopens the cap)

**V-1 — B-1's defect class survives in the journal, four lines below a hunk this repair
edited.** `retro-2026-08-03.md` §1, lines 40–42, still reads:

> **一处未冻结缺口（新发现）**：`E2` 冻结 schema pack 时写死 "fourteen files"（2026-07-29），而
> `paragraph-map.schema.json` 于 07-31 加入，按 `E2` 自身文字…**不在冻结面内**。
> **pack 现 15 个文件，其中 1 个不受 E2 保护。**

That last sentence is present-tense and false at `HEAD`: the pack's fifteenth file has been
inside the freeze since `22b27aa`, and this repair is the commit that made the file say so
about itself. §1's heading is `保障面现况（HEAD）` — current state at HEAD — and the repair
**accepted that standard four lines above**, updating the same section's line counts to
their HEAD values under L1. It applied the standard to the numbers in the table and not to
the prose immediately below them, in the same section, in the same file, in the same commit.

`E7`'s test is the defect class, not the reported instance, and this is the same class B-1
named: an assertion about who is inside the freeze, falsified by the re-baseline, left
standing. Why it is a low and not more: the reader who needs the answer to act — someone
about to edit those bytes — reads the file itself or `E2`, and both are now correct; §7
item 6 of the same journal records the re-baseline; and `R9`'s recoverability arm is
satisfied. The downstream decision that goes wrong if it stays: this block is the witness
the whole re-baseline was built on, so a session auditing whether the gap was ever closed
reads §1 first and finds it open.

**Minimum fix.** The block becomes past-tense, or takes the inline `⚠ errata` marker §7
item 6 already uses in this same file. **Target:** `retro-2026-08-03.md` §1 lines 40–42.
**Redeem-when:** the closeout, which O-4 already obliges to open this file — the touch
condition arrives immediately, so this should not need the bank.

**V-2 — the ruling that reopened `E2`'s freeze exists only in the repair's own commit
body.** `E2`'s text offers two responses when the cleanest fix needs a frozen path: take
the in-boundary fix and record why, or stop with `SPEC_GAP`. This repair took a third —
the user reopening the freeze for one file and one act — which the FULL named in advance and
which the repository does record as a pattern, in rider `O-2b`
("特殊：属 `E2` 冻结面，须裁决重开才能兑"). The ruling itself is nowhere in the repository
but `c05d052`'s body. `R7` applies and this is not a block; the ceiling is stated and I
move on. What makes it a finding rather than a ceiling note is that
`HARNESS-LEDGER.md`'s own header claims exactly this content — "the current pointer … and
**the user rulings that exist nowhere else**" — and **this commit edited that very block**,
adding the L3 entry two lines from where the ruling belongs. One round earlier the same
defect was found and accepted as VERIFY low `V-1` on `440e205`, and `4ab1db1` discharged it
by writing three such rulings into that block; this ruling is load-bearing for a *permanent
boundary*, which the three were not.

**Minimum fix.** One entry in the rulings block naming the date, the file, and that the
reopening was for this act only. **Collision the closeout must plan for:** the ledger is at
119 lines against `ledger_cap_check`'s cap of 120 (O-3), so the entry does not fit as an
addition — the ⛔ P5B block is the natural place to reclaim lines, since precondition ① is
about to close anyway (O-4). **Target:** `HARNESS-LEDGER.md` rulings block.
**Redeem-when:** the closeout. **Deadline:** the moment the defect bites is the next freeze
audit or the next `E2`-surface edit that looks for precedent, whichever comes first.

**V-3 — the repair introduced a one-line anchor error into the finding it was repairing,
in two files.** L4's fix writes `stage`'s site as ``rsc.py`` `:643` 起的子解析器块 in both
`HARNESS-RIDERS.md` and retro §7 ruling 4. Line 643 is the string literal `"stage",`; the
`sub.add_parser(` call opens at **642**, the `add_subparsers` at 647, and the FULL's own
re-derivation wrote the block as 642–703. Under no reading does the block start at 643.
`R9`: no actor's action changes — a redeemer landing on 643 sees the call one line up — and
the accurate fact is recoverable from the row's own words, so this is the smallest of the
four. It is reported because it is a *new* inaccuracy, in the cell the finding existed to
correct, duplicated across two files. **Target:** `HARNESS-RIDERS.md` `CLI-hist`; retro §7
ruling 4. **Redeem-when:** the next batch touching either, or the `CLI-hist` redemption
batch. **Deadline:** before `CLI-hist` is redeemed — that is when a wrong anchor bites.

**V-4 — the two facts the repair says decided B-1's severity are overstated as written,
and the one mechanism that could have carried the freeze is unmentioned.** The commit body
states both as re-derived rather than accepted: "the four frozen blob ids … their only
repo-wide occurrence is `N1/governance-exemptions.json`", and "the sole `frozen` token in
tooling is `dataclasses.dataclass(frozen=True)`". Re-derived here:

```
files containing any of the four blob ids                    -> 82
  … of which non-markdown                                    -> 2  (.harness/runs.jsonl, N1/governance-exemptions.json)
  … of which .py                                             -> 0
`frozen|freeze` occurrences under ResearchSystem/tooling/*.py -> 184
```

The **conclusion survives intact** — zero `.py` files name a frozen blob id; nothing in
`tooling/`, `hooks/` or the pre-commit hook compares a frozen file's bytes; `E2` has no
mechanical enforcement and the prose is the whole control surface — and that conclusion is
what B-1's severity rested on. But neither sentence is true as written, and the second is
false by a wide margin (the 184 hits are the product-run instruction freeze, the `E9`
review-window marker, `frozenset`, and `@dataclass(frozen=True)`). The FULL's own §4
formulation was the careful one and remains available.

What the compression hides is worth more than the correction.
`rsclib/document_harness/__init__.py:237` defines `pack_digests()`, whose docstring is
"Content digests binding the signed contract text and the exact schema pack" and which
hashes every file in
`SCHEMA_FILES` — member 9 included. It is **the** place a mechanical freeze check would
attach, and it has **zero callers repo-wide**: the two live call sites
(`rsclib/harness/resolver.py:272`, `tests/harness/run_tests.py:39`) are the v2
`rsclib.harness.schemas` function over the `harness-v2` pack, a different directory.
Verified as a by-product: because the v3 digest is never computed or recorded anywhere,
this repair's edit to member 9's bytes invalidates no stored digest — which is the
strongest available evidence that the edit was byte-safe, and the commit body does not
claim it. **Target:** none in place (a landed commit body, the L3 shape). **Redeem-when:**
the record for it is this file; the `pack_digests()` half routes to O-2 below.

### Observations (`R5` — reported; the conclusions are the user's)

**O-1 — `E2` names two branches for a fix that needs a frozen path, and this round took a
third.** "Take the in-boundary fix and record why, or stop with `SPEC_GAP`" does not
include "the user reopens the freeze for one act", yet that is the accepted practice —
rider `O-2b` has carried it as the redemption condition for another pack file since
`v3-review-full-11ce5b4`, and this round's FULL treated it as the fix leg's normal
precondition. So the branch exists in the repository's practice and not in the rule that
governs it. Whether `E2` should carry it explicitly, or whether the practice should stop,
is the user's question, not mine.

**O-2 — the freeze register and the layer register now overlap, and this round paid the
overlap's second cost.** The FULL reported the overlap as O-1 and B-1 as its first cost.
The second is procedural: member 9's blob moved `c2b713bf → 09aa8699`, so **the next round's
opening cold read can no longer discharge member 9 by citation** — `E10` makes citation
depend on a record stating the blob id, and every existing record states the old one
(`v3-checkpoint-read-22b27aa.md` §1's nine-blob table, quoted forward into `9dcb783`'s
body). The other eight are unmoved and still citable. Re-derived at `HEAD`:

```
2108635f  CONSTRUCTION-CHECKLIST.md      17ff31bb  v3-harness-operating-contract.md
f3a31208  README.md                      52a97a48  v3-harness-review-contract.md
bd490c8b  EXECUTION.md                   68031fa2  …supersession-1.md
c19d8cb9  REVIEW.md                      e1a2f26b  …supersession-2.md
                                         09aa8699  paragraph-map.schema.json   ← moved
```

This record states the new id so citation is available again from here. A session that
cites the old table without re-deriving will mismatch on member 9, which is the mechanism
working. Related and unresolved: `pack_digests()` (V-4) is the same shape as the `RA` rider's
`run_all` — a v3 mechanism with no caller — and it is the one that would give this freeze
teeth.

**O-3 — the ledger is at 119 lines against a mechanical cap of 120, with the closeout still
owing writes.** `ledger_cap_check.MAX_LINES` is 120 and measures the staged file; the
repair took the ledger 117 → 119. The closeout owes at least the precondition-① rewrite
(O-4) and, if the user routes it there, V-2's ruling entry. One line of headroom is not a
finding — the ⛔ block is 11 lines and is about to shrink — but the ordering matters: reclaim
before adding, or the guard blocks the closeout commit.

**O-4 — two pointers are one step behind the work, both closeout sweeps.** `HARNESS-LEDGER`
precondition ① still reads "下一步 = remedy (a)：以 `22b27aa` 的层 diff 为 subject 单开一轮
FULL" — that FULL ran (`15b6e34`), its repair landed, and this VERIFY is the last leg before
closeout. Retro §7 item 6 still frames the obligation as a read, which is the FULL's O-4,
still live and still owed. Both are the same class the previous round carried as its O-3 and
discharged at closeout; noted so this closeout sweeps both rather than one.

## 6. Boundary and record conformance — second (`R3`)

- **`E1`.** One role per session. This session holds review only; nothing in the repository
  was authored by it but this record. That the executor's session held one role is a
  process claim — marked, not verified (`R4`).
- **`E2`.** The repair touches a frozen path by design, under a ruling recorded only in its
  own commit body (V-2). The freeze is otherwise unmoved and verified so file-by-file: 14
  of 15 pack blobs identical between `22b27aa` and `HEAD`, and the four frozen blob ids
  (`8ad404b1` / `b2dbdf75` / `68031fa2` / `e1a2f26b`) unchanged. The pack remains fifteen.
- **`E3`.** The repair's figures were re-run here at `HEAD` and reproduce (§4). The one
  class `E3` exists to catch — a count invalidated by the commit that writes it, which is
  what produced L1 — does not recur: 576 / 904 are true at `HEAD` after the repair. The
  staged-diff guard exits are unreproducible after the fact and are disclosed as such, not
  softened.
- **`E6`.** The finding named text as wrong and that text changed; no rule, clause, guard or
  test was added about it anywhere in the range. A VERIFY refuses a fix that adds machinery
  instead — there is nothing here to refuse.
- **`E7`.** Class-swept for other live copies of the falsified assertion. Hits in
  `v3-checkpoint-read-*` / `v3-review-full-*` are immutable records that correctly preserve
  what was true at their time; `layer-inc-2026-07-31.md:113` is a "Current: / Draft:" text
  under consideration in a dated session note, not a live claim. Two are live prose:
  `retro-2026-08-03.md` §1 (V-1) and `.goals/plans/stage2-p4-activation-bridge-run.plan.md:34`
  ("N0 schema pack 14 冻结件"), the latter a never-touch list inside a closed run's plan,
  outside `ResearchSystem/` and outside anything this round names — reported here as sweep
  coverage, not as a finding.
- **`E8`.** Title `V3-E2-REBASELINE-DESIGN-REVIEW-FIX-v1` conforms to `V3-<ROUND>-v1`; the
  kind is named in the rule's vocabulary ("Kind: review fix"); one dense paragraph, no
  trailers (`git log -1 --format=%b` has exactly one blank line, the terminator). A new
  commit, not an amend. Explicit-path staging leaves no post-hoc trace — unverifiable,
  disclosed. Not pushed (`git rev-list --count origin/main..HEAD` → 432, user-gated by the
  2026-07-30 ruling). **Change boundary held:** all four paths trace to an accepted
  finding, and no observation was acted on.
- **`E9`.** Budget and window as re-derived in §1: one FULL, one fix, one VERIFY; zero
  commits since dispatch. The fix leg is spent, which constrains how the four lows can be
  routed at closeout.
- **`E10`.** The repair amends a schema `description` string, which `E10` names as
  instruction-layer text, so this is a layer amendment. It is not the design test's
  business: correcting a derived statement so it conforms to the rule that governs it adds
  no clause and changes what no rule requires. `E10`'s "each amendment passes an independent
  read before any round relies on it" is satisfied by this VERIFY, whose subject includes
  the amended bytes and which read them in full and re-derived every assertion in them
  (§2). What remains is bookkeeping, not obligation: member 9's blob moved, so citation
  discharge for that member is unavailable until a record states the new id — this one does
  (O-2).
- **`E12`.** The handoff is one range, no per-acceptance argument. The written full-SHA tip
  lives in `.harness/review-pending.json`, which `.gitignore:19` excludes — untracked local
  state written by the CLI, not a range recorded in a file, so `E12`'s "tip is `HEAD`, never
  a written SHA" is not engaged; the written tip equals `HEAD` in any case.
- **`R10`.** Bank unchanged at five rows; `CLI-hist` edited in place, no row added or
  deleted, so no redemption is claimed. Row still names targets and two touch conditions
  with no deadline, which suits debt whose value does not expire. The four lows above are
  written in row form — target, redeem-when, deadline where one exists — so the closeout can
  route them without re-deriving them.

## 7. Coverage disclosure (`R4`)

**Read in full:** `CONSTRUCTION-CHECKLIST.md` (164 lines, blob `2108635f` — my standing
instructions and member 1) and the superseded review-contract stub that routes to it;
`v3-review-full-22b27aa.md` (397 lines, the FULL whose findings this VERIFY covers);
`c05d052`'s complete diff and commit body; the commit bodies of all ten commits in the
range; `HARNESS-LEDGER.md` (119 lines); `HARNESS-RIDERS.md`; `paragraph-map.schema.json`
(44 lines) before and after; `layer_path_check.py` (105 lines), `ledger_cap_check.py` (46),
`review_freeze_check.py` (78); the pre-commit hook at the common dir
(`git rev-parse --git-common-dir` → `D:/Thesis/.git`); run-v2 README
`Regression-battery tiering` (125–163).

**Sampled:** `retro-2026-08-03.md` §1, §4, §5, §7 (headings enumerated, rulings 1–5 and item
6 read); `rsc.py` :40–52 and :630–710 plus every `add_parser` / `register` line;
`tests/stage_control/run_tests.py` :175–190; `rsclib/document_harness/__init__.py` :225–270;
`rsclib/harness/schemas.py` :60–90; `layer-inc-2026-07-31.md` :106–118; `440d79b`'s and
`120e8ec`'s records for the prior round's V-1 and O-3.

**Probed only:** pack `ls-tree` counts and per-file blob equality at `22b27aa` / `HEAD`;
`git log --diff-filter=ADR` over the pack's whole history; the nine-member blob table at
both points; per-commit path lists across the range; the four-blob-id and `frozen|freeze`
greps by file type; `origin/main..HEAD`; `.gitignore` for `.harness/`; rider cell lengths by
script.

**Ran:** the full six-leg battery at `HEAD` (29 / 80 / 32 / 58 / `compile --check` clean /
556 passed), `repo-audit.py`, the three tracked guards, a JSON reparse of the edited schema,
and `layer_path_check.unresolved_tokens` on the real added line plus five mutations
including two negative controls (§4).

**Not verified:** that this review ran in a fresh context (process claim, marked). The
2026-08-04 freeze-reopening ruling beyond `c05d052`'s body (`R7`; V-2). That the three
guards exited 0 **over the staged diff** at commit time — staging leaves no trace, and my
runs were on a clean tree. That the executor's session held one role (`E1`, process claim).
The retro's subagent-reported token figures, which its own coverage disclosure declares
unrechecked and which the FULL also did not recheck. `E4` mutation is not owed here — the
repair adds no guard — and `R4` holds regardless: what §4 shows is that
`layer_path_check` has binding force on member 9's defect shapes, not that its force is
sufficient. **A VERIFY is never a re-certification:** nothing here re-opens the FULL's
verdict on `22b27aa`, and the observations O-1…O-5 it left standing are not re-adjudicated.

**Ceiling.** What is established: all five accepted findings are closed against the
repository at the bytes; the replacement clause in the frozen file is true and better
anchored than the minimum required; the repair adds no rule or machinery to close a
text-is-wrong finding; the battery its tier owes is green when re-run independently; the
freeze is otherwise unmoved and the layer's other eight members are unchanged. What is
not: whether the freeze should be reopenable by ruling at all (O-1), whether the two
overlapping registers should stay overlapped (O-2), and how the four lows are routed at a
closeout whose fix leg is already spent. Those are the user's.
