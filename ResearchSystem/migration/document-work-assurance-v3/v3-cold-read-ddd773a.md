# Cold read — the instruction layer at `ddd773a`

**No verdict.** A read is not a round (`R3`): it spends no budget, carries no verdict, and its
output is findings tiered must-fix / low / observation. This is the read `E10` owes over the
instruction layer; nothing below certifies any text, and nothing below is banked as any round's
FULL.

**Findings: 0 must-fix, 1 low, 6 observations.** The one low is a stale measurement inside
`EXECUTION.md`'s regression-battery tiering section, caught by re-running the battery the
section describes. Everything else the layer asserts and that a command can falsify was
re-executed and reproduced.

---

## 1. Subject, re-derived

```
$ git log -1 --format='%h %ad %s' --date=short ddd773a58e3ee2ebc18a2cbc6226915817f8b305
ddd773a 2026-08-15 V3-SPLIT-R0-AMEND-M2-FREE-L1-L2-L3-L4-L5-v1
$ git rev-parse HEAD
dbd96f85c3d961491668afd84fbaa437563e506d
$ git status --porcelain
                                              # clean
```

The subject commit changes four paths, **none of them a layer member**:

```
$ git show --stat --format='' ddd773a
 .goals/plans/harness-repo-split.plan.md            | 24 ++++++++++++++++------
 ResearchSystem/HARNESS-DECISIONS.md                |  9 +++++---
 .../journal/repo-split-r0-2026-08-13.md            | 11 ++++++----
 ResearchSystem/document-harness/split-design.md    | 16 +++++++------
 4 files changed, 41 insertions(+), 19 deletions(-)
```

So the subject of this read is the layer's **standing bytes** at that commit, not a diff. The
member set is enumerated from `E10`'s own sentence read at `ddd773a` (not from HEAD, not from
the dispatch) — nine paths, and the sentence's self-count "exactly these nine paths and nothing
else" reconciles with the enumeration.

| # | blob | lines | path | read |
|---|---|---|---|---|
| 1 | `15999875` | 204 | `document-harness/CONSTRUCTION-CHECKLIST.md` | end to end — also this session's standing instruction |
| 2 | `54dfef83` | 38 | `document-harness/README.md` | end to end |
| 3 | `62c55e4b` | 421 | `document-harness/EXECUTION.md` | end to end |
| 4 | `3350bfac` | 284 | `document-harness/REVIEW.md` | end to end |
| 5 | `17ff31bb` | 5 | `migration/…/v3-harness-operating-contract.md` (stub) | end to end |
| 6 | `b576a45e` | 5 | `migration/…/v3-harness-review-contract.md` (stub) | end to end — the dispatch entry point |
| 7 | `68031fa2` | 124 | `contract/…-v3-supersession-1.md` | end to end |
| 8 | `e1a2f26b` | 113 | `contract/…-v3-supersession-2.md` | end to end |
| 9 | `09aa8699` | 44 | `schema/document-assurance-v3/paragraph-map.schema.json` | end to end |

**1 238 lines, none by citation.** Blob ids and line counts emitted by
`git rev-parse --short=8 ddd773a:<path>` / `git show ddd773a:<path> | wc -l`.

Outside the layer but owed at the same opening (`E10`): `ResearchSystem/HARNESS-DECISIONS.md`
at blob `2a28e0a2`, `§live` read in full (lines 28–266: `HD-42`, `HD-41`, `HD-40`, `HD-39`,
`HD-36`, `HD-35`, `HD-28`, `HD-33`, `HD-34`, `HD-27`, `HD-23`, `HD-10`, `HD-15`, `HD-9`). This
file's blob differs at HEAD (`e859f96f`); it was read at the subject, per `R2`.

## 2. Citation status — the layer has not moved since its last end-to-end read

Every member's blob at `ddd773a` is identical to the blob the `f61ce2c` read recorded reading
end to end on 2026-08-13 (`v3-checkpoint-read-f61ce2c.md` §1: the same nine short ids, the same
"1 238 lines"). Per-path history confirms no member changed after `f61ce2c`:

```
$ git log --format='  %h %ad %s' --date=short -1 ddd773a -- <each member>
  f61ce2c 2026-08-13 V3-B-R5-AMEND-v1        # CONSTRUCTION-CHECKLIST.md
  c7e0ba0 2026-08-12 V3-B-R3-CONSTR-v1       # README.md
  8884f47 2026-08-13 V3-B-R4-AMEND-2-v1      # EXECUTION.md
  6f850db 2026-08-05 V3-SIMP-ABCD-A1-DELETION-v1   # REVIEW.md
  7463229 2026-07-31 V3-LAYER-INC-L1-BYTES-APPLIED-v1  # operating-contract stub
  8884f47 2026-08-13 V3-B-R4-AMEND-2-v1      # review-contract stub
  19cb882 2026-07-24 V3-W2-COMMIT-FIRST-CANDIDATE-v1   # supersession-1
  403fc9a 2026-07-30 V3-SUPERSESSION-2-SIGNING-BATCH-v1  # supersession-2
  c05d052 2026-08-04 V3-E2-REBASELINE-DESIGN-REVIEW-FIX-v1  # paragraph-map.schema.json
```

Two consequences, both stated rather than assumed:

- The cold-read obligation at this round's opening was **already dischargeable by citing
  `v3-checkpoint-read-f61ce2c.md`** at zero per-member cost. This read did not take that route:
  all nine were read end to end again, so it is an independent read, not a citation (`O-1`).
- **No per-member digest debt is riding.** `E10` makes a free-channel layer application "ride
  the next read of this layer at per-member digest cost"; since nothing has been applied to the
  layer since `f61ce2c`'s read, this read discharges nothing and leaves nothing owed (`O-2`).

## 3. What was re-executed

Everything below ran against the worktree, which is byte-identical to the subject for all
tooling and test paths — the only three files differing between `ddd773a` and HEAD are
`.goals/plans/harness-repo-split.plan.md`, `HARNESS-DECISIONS.md` and `HARNESS-LEDGER.md`
(`git diff --stat ddd773a HEAD`), so no measurement below is affected.

**`E2`'s frozen surface reconciles.**

```
$ git ls-tree -r --name-only ddd773a -- ResearchSystem/schema/document-assurance-v3/ | wc -l
15                                             # E2: "fifteen files"
$ git rev-parse ddd773a:<the three contracts>
b2dbdf752d8c155e4c65b14b5f420b880b8184a1       # E2: contract b2dbdf75…
68031fa2ca31272e31da0d42a9a02189d28fcc21       # E2: supersession-1 68031fa2…
e1a2f26b1d8d323d11e900f8137dea222b6571c1       # E2: supersession-2 e1a2f26b…
```

**The three membership mirrors are in sync** (rider `E10-sync`'s standing check-item).
`E10`'s sentence, `tooling/hooks/layer_path_check.py`'s `LAYER`, and
`tooling/tests/document_harness/test_precommit_checks.py`'s `LayerMembership.EXPECTED` carry the
same nine paths in the same order. The pinning test's expectation is a hand-written literal, not
the module's own tuple (`E5`-conformant, and its docstring says so).

```
$ python -m pytest -q tests/document_harness/test_precommit_checks.py \
                      tests/document_harness/test_readme_enumeration.py
43 passed in 12.17s
```

**Full-stock path scan over all nine members** — the guard normally sees only staged added
lines, so this ran `layer_path_check.unresolved_tokens` over each member's whole text at
`ddd773a`:

```
ResearchSystem/contract/…-supersession-1.md
    `schema/document-assurance-v3/review.v2.schema.json` — resolves only under ResearchSystem/ — prefix missing
ResearchSystem/contract/…-supersession-2.md
    `assurance/runs/` — resolves only under ResearchSystem/ — prefix missing
ResearchSystem/contract/…-supersession-2.md
    `schema/` — resolves only under ResearchSystem/ — prefix missing
  total flagged: 3
```

Exactly the set rider `frozen-path-prefix` already banks, all inside the two `E2`-frozen
supersessions; the fourth token that rider names (`templates/run-v2/`) is skipped by the
guard's design, as the rider says. **Nothing new.**

**Layer assertions a command could falsify, re-run:**

| assertion | site | result |
|---|---|---|
| fixtures "41/41 green" | `README.md:33` | `41/41 cases behaved as declared; failures=0` — holds |
| pytest from repo root aborts on two same-named `smoke_test.py` under `ExperimentLab/papers/` | `EXECUTION.md:337-338` | both files exist (`agentspec/replication/`, `guardagent/replication/`) — holds |
| all eight full-battery paths exist | `EXECUTION.md:332-339` | all eight resolve at `ddd773a` — holds (see `O-3`) |
| `DIGEST_PROTECTED_FIELDS` = the five named fields | supersession-2 §2 | `assurance_state.py:81` — exactly `work_spec_ref`, `start_decision_ref`, `repair_decision_ref`, `final_decision_ref`, `review_ref` — holds |
| `pointer_for` / `pointer_to` / `pointer` all exist | supersession-2 §2, §4 | `assurance_state.py:122 / :100 / :92` — holds |
| "`pointerRef` requires only `path`" | supersession-2 §2 | `common.schema.json` `$defs.pointerRef.required == ['path']` — holds |
| p5b-firewall FULL: "four of that FULL's seven findings (`f2`–`f5`)" name checker assertion strength | `REVIEW.md:43-47` | `v3-review-full-fef3a2e.md` carries f1–f7; f2–f5 name `chk-bookkeeping` / `chk-tripwires` / `chk-tooling` / `chk-open` — holds exactly |
| `7011916` carries both retired contracts' full text | checklist header, both stubs | both blobs present at `7011916` — holds |
| every other repository path named in the layer | all nine members | all resolve at `ddd773a` — holds |

**The full battery, re-run end to end** (green, and the source of the one low below):

```
$ python tests/run_tests.py            → tests: 29   passed: 29   failed: 0
$ python tests/run_p4_tests.py         → tests: 80   passed: 80   failed: 0
$ python tests/run_p5a_tests.py        → tests: 39   passed: 39   failed: 0
$ python ../schema/fixtures/validate_fixtures.py → cases: 58  matched: 58  unexpected: 0
                                                   [legs 1-4 elapsed: 2s]
$ python -m pytest -q                  → 701 passed in 82.92s      [leg elapsed: 86s]
$ python tests/harness/run_tests.py    → Ran 39 tests … OK
$ python tests/stage_control/run_tests.py → 20 run, 0 failure(s), 0 error(s)
$ python rsc.py compile --check        → 0 error(s), 0 warning(s); RESULT: generated output fresh
                                                   [legs 6-8 elapsed: 11s]
```

## 4. Findings

### L-1 (low) — `EXECUTION.md` §Regression-battery tiering: two of five stated tallies no longer reproduce, under a sentence asserting they do

**Location.** `EXECUTION.md:348-349` — "the battery run directly totals 130s (p5a-shells scale:
P2 29 + P4 80 + P5A 32 + fixtures 58 + pytest 556 — **tallies reproduce exactly**)".

**Ground.** Re-running the battery the sentence describes, immediately before writing this
(`E3`, measure-last):

| leg | text says | measured now |
|---|---|---|
| P2 (`run_tests.py`) | 29 | **29** ✓ |
| P4 (`run_p4_tests.py`) | 80 | **80** ✓ |
| P5A (`run_p5a_tests.py`) | 32 | **39** ✗ |
| fixtures (`schema/fixtures/validate_fixtures.py`) | 58 | **58** ✓ |
| pytest (from `ResearchSystem/tooling`) | 556 | **701** ✗ |
| wall total | 130s | **≈99s** (2 + 86 + 11) |

**What this does and does not touch.** The section's headline is what a decision turns on: its
own revert anchor tells the user to "weigh the revert anchor below against that number", and
that number is "**≈2 minutes per doc-only pass, not ≈8**". At ≈99s the headline **survives** —
no ruling is falsified, and this is not a must-fix. What is false is the present-tense
reproducibility claim attached to the sub-tallies: a reader who does what the sentence invites
and re-runs the battery finds two of the five disagree, and has no way to tell from the text
whether the ratio, the magnitude, or their own environment is wrong.

**Why it is a finding rather than drift to be ignored.** `E3`'s last clause is exactly this
case — "a factual assertion written into instruction text runs the command that could falsify
it first". The falsifying command is a one-line re-run, and the tallies grew because tests were
added (pytest +145, P5A +7), which is the growth `HD-41` ③ names: "会随时间增长的量另写
「落地时按当时的 base 再算」".

**Content for the fix, not bytes.** I deliberately do not dictate bytes here, because the fix
shape is already settled by precedent rather than by me: the subject commit `ddd773a` itself
applied `HD-41` ③ to three sites, changing hard-coded counts to compute-at-landing. The same
treatment applies — drop the frozen sub-tallies, or re-mark them as a measurement pinned to a
named revision, keeping the headline figure the ruling turns on. Any rewrite that hard-codes
fresh numbers reproduces the defect on a later date.

**Routing is not mine to settle.** `EXECUTION.md` is an `E10` member and is **not** on `E2`'s
frozen list, so nothing bars the free channel from carrying this. But rider `wl-route` records
precisely the unresolved question of which channel a below-must-fix finding with supplied
content takes — `E10`'s enumeration and `R10`'s routing sentence say apply now, `R9`'s opening
says bank — and adjudicating it would be adding a bound. The orchestrator routes; this record
supplies the content either channel would need.

### O-1 (observation) — the cold read was dischargeable by citation, and was not discharged that way

All nine blobs are unchanged since `v3-checkpoint-read-f61ce2c.md`'s recorded end-to-end read
(§2 above). `E10`'s citation clause would have met this round's opening obligation at zero
per-member cost. This read instead re-read all nine end to end. Neither route is wrong; the
fact is recorded because the orchestrator may want to know the cheaper one existed, and because
a future reader comparing the two records should know they rest on identical bytes.

### O-2 (observation) — no per-member digest debt is outstanding, and the next one is already named

Nothing has been applied to the layer since `f61ce2c`, so no free-channel application is riding
this read. The next such debt is already scheduled and disclosed: `HD-42` (live, one-shot,
pending R1) authorizes the eight→six edit to `EXECUTION.md`'s battery enumeration and states in
its own 后果 that the exemption covers only 开设计轮 and **not** the read — "按 `E10` 仍欠该层
的一次独立 read". A reader of this record should not treat it as covering that edit.

### O-3 (observation) — the eight-command enumeration is still accurate at this commit

`HD-42` is live and pending, so the two runners it will delete still exist and the enumeration
still names eight real files. Verified rather than assumed:
`tests/harness/run_tests.py` (Ran 39 tests, OK) and `tests/stage_control/run_tests.py`
(20 run, 0 failures) both resolve and both pass at `ddd773a`. No finding is owed here **yet** —
the defect `HD-42` describes begins the moment the deletion lands, and `HD-42`'s ③ requires the
enumeration change to ride that same commit.

### O-4 (observation) — `tier-file-vs-clause` reproduced independently, and this read is a fresh instance of its trigger

Reading `EXECUTION.md`'s tiering exception cold, I reached the banked defect without having seen
the rider: "a doc file that code enumerates or tests pin … is tooling-load-bearing" is written
by file, and **all nine layer members** are enumerated by `layer_path_check.LAYER`, so the
sentence read literally makes every doc-only layer batch tooling-touching and owing the full
eight-command battery. The parenthetical compounds it by naming `layer_path_check.py` — a `.py`
file — as an instance of "a doc file". Rider `tier-file-vs-clause` already banks this, with the
redeem-when rewritten under `HD-37`, so **no new row is owed**. Recorded because independent
re-derivation is evidence the rider's account is accurate, and because the rider's redeem-when
names "下一个有资格开轮的构造批按此句自选档位的那一刻" — a moment that arrives whenever a layer
batch picks its tier.

### O-5 (observation) — supersession-2 carries a second UNSIGNED assertion beyond the one the disclosures name

`README.md:19` and `supersession-2-signature.md` both explain the **top-of-file** UNSIGNED line
as a pre-signature residue that the signed contract's §13 bars correcting in place. A second,
separately-worded assertion lives in the body — supersession-2 §5, "This file is **UNSIGNED**"
— and neither disclosure names it. Same class, same ground, and not appliable by any channel in
any case: `e1a2f26b` is on `E2`'s frozen list, so `HD-20` banks any bytes for it until `E2`'s
recorded ruling exists. Recorded so that the eventual `E2` ruling, if it ever reaches these
bytes, covers both sites rather than the one the current disclosures point at.

### O-6 (observation) — `R9` and `R10` sit out of numeric order in the review side

File order is `R1 R2 R3 R9 R10 R4 R5 R6 R7 R8` (emitted by grepping the bolded ids in file
order). The placement is topically coherent — verdicts, then finding routing, then the rest —
and `README.md:27`'s "R1–R10 review" is accurate as a set. No downstream decision goes wrong,
so by `R9`'s own test this rides the next batch touching the layer and spawns no round and no
read.

## 5. Coverage and ceilings (`R4`)

- **Read in full at the subject blobs:** all nine members, 1 238 lines, none by citation;
  `HARNESS-DECISIONS.md` `§live` (lines 28–266) at blob `2a28e0a2`, carrying fourteen entries
  (`HD-42`, `-41`, `-40`, `-39`, `-36`, `-35`, `-28`, `-33`, `-34`, `-27`, `-23`, `-10`, `-15`,
  `-9`); `HARNESS-RIDERS.md` in full at the subject (**28** rows, enumerated by id), read to
  avoid re-filing banked findings, which caught `O-4`.
- **Read to check a specific claim, not in full:** `v3-checkpoint-read-f61ce2c.md` (its §1
  coverage table and blob ids); `v3-review-full-fef3a2e.md` (its finding table);
  `supersession-2-signature.md` (in full, 26 lines); `layer_path_check.py` and
  `test_precommit_checks.py` `LayerMembership` (in full); `assurance_state.py:81-130`;
  `common.schema.json` `$defs.pointerRef`.
- **Re-executed:** the full eight-command battery, the two layer-pinning test modules, the N0
  fixture runner, and a full-stock path scan over all nine members. Every command's output is
  pasted above or in §3; none is described from memory.
- **Not established.** Whether the layer's rules are *sufficient* is not a read's question
  (`R5`). Token-cost and minutes figures quoted inside `EXECUTION.md` from earlier rounds
  (~176k, ~525k, ~28 min, the 2m22s mtime span) were **not** re-derived — they are historical
  observations with no reproducible command, and `L-1` deliberately does not extend to them.
- **This record's own counts were re-measured last, and two were wrong.** The rider-row count
  and the signature record's line count were first written from impression and corrected to 28
  and 26 by the commands above before this record was handed back. Disclosed because it is the
  same class as `L-1`: a figure written into a record without the command that produces it
  drifts silently, and the reader has no way to tell.
- **One machine, one run.** The battery timings are from this Windows worktree in a single
  pass; wall-clock is environment-bound and the `≈99s` figure should not be read as a repo
  constant. What is repo-bound, and what `L-1` rests on, are the **counts** — 39 and 701 —
  which are properties of the test tree, not of this machine.
- **Process claims are marked, not verified** (`R4`): that this read ran in a context set by the
  orchestrator rather than by any executor is a declaration, and no evidence at any revision
  locks it.
