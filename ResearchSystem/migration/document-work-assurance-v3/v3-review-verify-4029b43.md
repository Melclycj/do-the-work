# VERIFY — round CALLER-ONBOARDING, `2026a14..4029b43`

**Verdict: `REVIEWED_NO_BLOCKER`.**

Both blockers are closed, and closed by measurement rather than by reading the commit body.
`B-1`'s index mode is `100755` and survives a real clone. `B-2`'s hole is gone in the strongest
available sense: I re-ran the same six-way template mutation at both ends of the repair, and the
before/after difference is exactly the one claimed — at `2026a14` deleting the inheritance block
left 21 of 21 green, at `4029b43` it turns red, and the other five stay red on both sides while
the template restores byte-identical each time. The three lows and the cold read's `O-2` are
each answered on the merits, and every figure the fix commit asserts reproduced when I re-ran
it, including the two sweeps and the battery.

Two lows and two observations, none of them a blocker, all of them about the record rather than
the code. The one worth the closeout's attention is `V-1`: the decision-log entry written to
answer `L-3` dates the ruling one day later than the two sites `L-3` named as its only carriers,
and both of those sites live in files this very commit edited.

Counts: **0 blocker · 2 low · 2 observation**.

---

## 1. Subject, round and budget, re-derived

Under `R2` I took nothing from the dispatch but the range.

```
$ git rev-parse --show-toplevel
D:/Thesis-stage-control-refactor/ResearchSystem/harness

$ git status --porcelain
(no output)

$ git log --oneline 2026a144f4dea83d4ac6c8235a647abe2cbd2590..4029b43dc66dcde37592b3398d4057aa9666e91f
4029b43 V3-CALLER-ONBOARDING-FIX-v1
7375e80 V3-REVIEW-RECORD-CALLER-ONBOARDING-2026a14-v1

$ cat .harness/review-pending.json
{
 "subject": "2026a144f4dea83d4ac6c8235a647abe2cbd2590..4029b43dc66dcde37592b3398d4057aa9666e91f",
 "dispatched_at": "2026-08-19T02:00:21+00:00"
}

$ git log --oneline 4029b43..HEAD
(no output)

$ git branch -vv
* main  4029b43 [origin/main: ahead 27] V3-CALLER-ONBOARDING-FIX-v1
```

The freeze marker names the range I was handed, the tip is the branch head, the worktree is
clean, and nothing is pushed (`E8`).

**Round and budget, derived, not accepted.** Ordered oldest first, the round is:

| commit | date (local) | what it is under `E9` |
|---|---|---|
| `6b5c154` | 2026-08-18 23:53 | record of the `E10` opening read — a read: no budget, no verdict |
| `393ebc5` | 2026-08-18 23:54 | `E10` free-channel byte application — not a round, consumes nothing |
| `2026a14` | 2026-08-19 01:04 | the round's candidate |
| `7375e80` | 2026-08-19 01:24 | **the round's one FULL** (`CHANGES_REQUIRED`) |
| `4029b43` | 2026-08-19 12:00 | **the round's one user-approved fix** |
| — | dispatched 02:00:21Z | **this, the one targeted VERIFY** — closes the cap |

`E9`'s test — *has a valid independent FULL already occurred?* — answers **yes** at `4029b43`,
so it is the fix round and it obliges this VERIFY. The cap is spent exactly, not exceeded.

`E9`'s window held on both legs. The FULL was dispatched `2026-08-18T15:04:13Z` and its record
landed at `7375e80` (`2026-08-18T15:24:59Z`) carrying **one file and nothing else**
(`1 file changed, 464 insertions(+)`); no commit intervened. This VERIFY was dispatched
`2026-08-19T02:00:21Z`, eight seconds after `4029b43` (`2026-08-19T02:00:13Z`), and the branch
has taken no commit since.

**`R6`.** The FULL's record is at the contract's path and name (`v3-review-full-2026a14.md`,
named by the range's tip), and its commit title is `V3-REVIEW-RECORD-CALLER-ONBOARDING-2026a14-v1`.
That it was committed *unchanged* is a process claim I cannot see from inside the repository —
**marked, not verified** (`R4`).

**Change set, classified by hand** (`R2`; 10 paths, `git diff --name-only` over the range):

| path | ∆ | what it is | which accepted finding |
|---|---|---|---|
| `.githooks/pre-commit` | M (mode only) | `100644` → `100755`, blob unchanged | `B-1` |
| `ResearchSystem/HARNESS-DECISIONS.md` | M | new `§live` entry `HD-47` | `L-3` |
| `ResearchSystem/HARNESS-RIDERS.md` | M | rider `RA`: count + pointer clause | `L-1`, `L-3` |
| `…/document-harness/ONBOARDING.md` | M | item 3 *See* row; item 9 *Do* row | `B-2`, `B-1` (class) |
| `…/journal/caller-onboarding-2026-08-19.md` | M | why `HD-47` lands here, not at closeout | `L-3` |
| `…/tooling/hooks/candidate_path_check.py` | M | docstring: count → expression | cold read `O-2` |
| `…/rsclib/document_harness/cli.py` | M | docstring: "these six" → "these" | `L-1` |
| `…/tests/document_harness/test_cli_entry.py` | M | test method name | `L-1` |
| `…/tests/document_harness/test_init_command.py` | M | pinned tuple + comment + method name | `B-2` |
| `…/tests/…_review/test_fix_round_locks.py` | M | comment: "the six operations" | `L-1` |

Every path maps to an approved finding. **No path is unaccounted for**, and no code path outside
docstrings, comments and test literals was touched — the only executable change in the range is
the six-tuple in `test_init_command.py`.

**`E2`.** No frozen byte was written, and the three named blobs are still the named blobs:

```
$ git diff --name-only 2026a14..4029b43 -- ResearchSystem/schema/document-assurance-v3 ResearchSystem/contract
(no output)
$ git ls-tree 4029b43 ResearchSystem/schema/document-assurance-v3/ | wc -l
15
$ git ls-tree 4029b43 -- ResearchSystem/contract/Document-Work-Assurance-Contract-v3*.md
100644 blob 68031fa2ca31272e31da0d42a9a02189d28fcc21  …-v3-supersession-1.md
100644 blob e1a2f26b1d8d323d11e900f8137dea222b6571c1  …-v3-supersession-2.md
100644 blob b2dbdf752d8c155e4c65b14b5f420b880b8184a1  …-Contract-v3.md
```

**`E10`.** Not engaged: none of the ten members is in the change set, and
`paragraph-map.schema.json` is untouched. `E10-sync` is not due — the membership sentence,
`layer_path_check.LAYER` and `test_precommit_checks.EXPECTED` are all outside the range.
`HARNESS-DECISIONS.md` is written but is explicitly **not** a member (`E10`'s tail, `HD-19`);
writing a new `live` entry that records a user ruling is the log's own mechanism and flips no
state, so its `only the user flips a state` invariant is not touched. One `E10` obligation
remains open from the *candidate* and is not this commit's to discharge: `document-harness/README.md`
was written twice under the deferral clause and those bytes still owe the next read of this
layer — deferral, never exemption.

**`E8`.** New commit, not an amend; explicit paths, nothing unrelated; one dense paragraph, no
trailers; title `V3-CALLER-ONBOARDING-FIX-v1` names the round; and the kind is named in the
first three words — *"Review fix: the round's one user-approved fix"*.

---

## 2. The accepted findings, each proved rather than read

### 2.1 `B-1` — closed, and it survives a clone

```
$ git ls-tree 2026a14 -- .githooks/pre-commit
100644 blob 521e707be370d7fbbdbca491344686be42917cf5
$ git ls-tree 4029b43 -- .githooks/pre-commit
100755 blob 521e707be370d7fbbdbca491344686be42917cf5
$ git ls-files -s .githooks/pre-commit
100755 521e707be370d7fbbdbca491344686be42917cf5 0   .githooks/pre-commit
```

Mode only; the blob is the same object, which is right for a mode fix and is the cheapest proof
that no content rode along. I did not stop at the index: cloned to a scratch path outside both
repositories (`git clone --no-local -c core.autocrlf=false`), and the clone's index reads

```
100755 521e707be370d7fbbdbca491344686be42917cf5 0   .githooks/pre-commit
```

so the executable bit is carried by the clone and not merely by this checkout — which is the
half `B-1` said was hollow.

**The class, checked rather than taken on the commit's word.** The class is *a tracked hook
committed non-executable*, and this repository has exactly one tracked hook:

```
$ git ls-files -s | grep -v "^100644"
100755 521e707b… 0  .githooks/pre-commit          # the only non-100644 entry in the tree
$ git ls-files | grep -E "hook|\.sh$|githooks"
.githooks/pre-commit
ResearchSystem/tooling/hooks/{__init__,candidate_path_check,layer_path_check,review_freeze_check}.py
```

The four `hooks/*.py` are guard modules the hook calls, not hooks git runs, so the class has one
member and it is fixed. The fix additionally rewrote `ONBOARDING.md` item 9's *Do* row — the row
that told a caller to track the hook and never to commit it executable — and the commit body
says plainly that a reviewer holding the boundary to the mode alone should read that as the one
place it exceeded. That is `E7` applied to the procedure that produced the defect, and `E9`'s
*said rather than done silently* is satisfied. No new machinery was added, which is `E6` being
respected rather than a gap: nothing mechanical pins the mode, and nothing here asks for it.

The consequential sentences downstream are now true rather than true-on-Windows: `README.md`
:64–68 (*"A clone carries the file; it does not carry the one `git config core.hooksPath`"*) and
`document-harness/README.md` :34 both read correctly at `100755`.

### 2.2 `B-2` — the hole is gone, measured at both ends

Six-way template mutation, driver written outside both repositories, run against a throwaway
clone so the subject worktree was never dirtied. Each case: delete one header block, run
`tests/document_harness/test_init_command.py`, restore from a sha256-checked scratch copy (never
`git checkout --`), assert byte-identity before continuing.

**At `4029b43` (after the fix):**

```
pristine sha256: 8e9d863c0d6b802b709383a236f068307e113ab4cd13861a6183b4e859d038d2
[CLEAN BASELINE (negative control)]   exit=0  21 passed
[DROP who-reads-it (inheritance)  ]   exit=1  1 failed, 20 passed     <- the hole, now must-fire
[DROP admission                   ]   exit=1  1 failed, 20 passed
[DROP state machine               ]   exit=1  1 failed, 20 passed
[DROP scope                       ]   exit=1  1 failed, 20 passed
[DROP narrowing                   ]   exit=1  1 failed, 20 passed
[DROP deletion                    ]   exit=1  1 failed, 20 passed
[CLEAN BASELINE (after restore)]      exit=0  21 passed
final sha256: 8e9d863c0d6b802b709383a236f068307e113ab4cd13861a6183b4e859d038d2
```

**At `2026a14` (before the fix), same driver, same blocks, same template bytes:**

```
[CLEAN BASELINE (negative control)]   exit=0  21 passed
[DROP who-reads-it (inheritance)  ]   exit=0  21 passed               <- the reported hole
[DROP admission … deletion        ]   exit=1  1 failed, 20 passed     (five, each)
[CLEAN BASELINE (after restore)]      exit=0  21 passed
```

The difference is exactly one case and it is the reported one. Note the template's sha256 is
identical at both revisions: the fix changed the **guard**, not the guarded thing, which is `E6`
read the right way round — the template already carried the block, and only the pin was missing.

**The pin is `E5`-clean.** `DECISION_LOG_HEADER_LINES` is six hand-written literals, and the
assertion is `assertIn(line, lines)` against `read_text().splitlines()` — whole-line membership,
never a substring, and never read back off `init_target`'s own constants.

**The enumeration is now right at source.** `io-design.md` §6 :93 reads
「状态机四态 / scope 四档 / 准入三问 / **继承** / 删除纪律」— five, the fourth being inheritance,
and narrowing is not among them. The tuple's first five are those five **in io-design's order**,
and the sixth is narrowing declared as the extra it is. The block the new literal pins is the
one carrying *"Every cold read MUST read `§live`, and only `§live`"* and the verbatim-inheritance
rule, which is what made this a blocker rather than a low.

**The second site, and the class.** Sweeping the whole tree for prose that enumerates these
rules (`git grep -n -I -E "narrowing rule|three admission questions|admission questions|准入三问"`,
migration records excluded) returns four live sites: `io-design.md` :93 (the source of truth),
`HARNESS-DECISIONS.md` :9 (this repository's own filled instance), and the two the fix corrected —
`test_init_command.py` :44–45 and `ONBOARDING.md` :81. Both now name §6's five with inheritance
present and narrowing labelled as an extra. There is no third site repeating the wrong five.

### 2.3 `L-1` — the four live sites are fixed and the renamed guard still binds

All four asserted repairs are in the diff and are correct: `cli.py` :13 (*"while these travel
with the instrument"*), `test_fix_round_locks.py` :328 (*"the operation surface"*),
`test_cli_entry.py` :72 (the test **method name**, a site the FULL did not name), and rider
`RA`'s count, which now reads 「`dtw` 七命令」 with a parenthetical recording that the old count
went false when `init` joined and that the row's substance did not change.

A rename can silently un-bind a test, so I mutated rather than read it. In the throwaway clone,
deleting the `init` subparser registration (`cli.py` :573–578) and running the suite:

```
FAILED tests/document_harness/test_cli_entry.py::TheSurface::test_the_operations_are_the_ones_named
FAILED tests/document_harness/test_cli_entry.py::TheSurface::test_every_operation_binds_a_distinct_function
FAILED tests/document_harness/test_cli_entry.py::TheTwoNames::test_both_names_print_the_same_help
3 failed, 3 passed
```

Restored from a sha256-checked scratch copy (`8052e39e…f8e19` before and after); the clone's
`git status --porcelain` was empty afterwards. Three red is the same shape the FULL of `297bb2b`
recorded for this guard under its old name, so the rename cost it nothing.

The three sentences left standing as history are each accurate as history: `cli.py` :9–10
(*"under which the six travelled"*), `test_cli_entry.py` :4 (*"the then-six operations"*) and
:37 (*"Six until 2026-08-19"*). The two signed sites (`split-design.md` :44, `io-design.md` :115)
are correctly out of boundary — they are bound by `HD-40` / `HD-35` signatures, and `HD-40` :232
says in terms 「对该文件的后续实质修改欠重签」, so touching them is a re-signature, i.e. design.
No rider row exists for them yet; banking them is the closeout's step, not this commit's.

One near-miss I checked and cleared: `EXECUTION.md` :335 reads *"it is these six commands and
nothing fewer"* — that is the six **battery** commands (one instrument-side, five caller-side),
a different class, correctly left alone. See `V-2` for what the sweep's accounting does miss.

### 2.4 `L-2` — every figure reproduces, at this tip

Re-run with the same pattern and the same exclusions the fix commit declares.

```
$ git grep -c -I -E -i "runs nowhere|installs no hook|no hook is installed|no hook at all|\
hook is installed|unwired|installed in neither|guard wiring|re-homing" \
    -- . ':!ResearchSystem/migration' ':!ResearchSystem/document-harness/journal'
.githooks/pre-commit:1
README.md:2
ResearchSystem/HARNESS-RIDERS.md:1
ResearchSystem/document-harness/ONBOARDING.md:1
ResearchSystem/document-harness/README.md:1
                                                    -> 5 files, 6 lines
```

Five files and six lines, and the per-file split is the split the commit body names, file for
file. Extending the pattern with the five Chinese alternatives leaves the instrument at 5 and 6,
as claimed.

Caller side, run in `D:/Thesis-stage-control-refactor` (not my subject; opened only to test a
count the subject asserts):

| sweep | result | claimed |
|---|---|---|
| English pattern, submodule excluded | 9 files, 12 lines | 9 / 12 ✔ |
| …migration also excluded | 8 files, 10 lines | 8 / 10 ✔ |
| + Chinese alternatives, migration excluded | 10 files, 14 lines | 10 / 14 ✔ |

The four caller sites the body classifies are classified right: `HARNESS-LEDGER.md` :106
(「harness 仓未装任何 hook，故它今日跑在无处」) and `HARNESS-POLICY.md` :60 / :62 are stale as of
`2026a14`; `HARNESS-POLICY.md` :39 (「hooksPath 一旦被 unset 只会退化为『无 hook』」) is still
true, because that sentence is about the per-machine half, which the tracked hook does not close.
All four are the caller's and none is touched here, which is right.

I also read all six surviving instrument sites at the tip. Each is accurate as written; the one
that had to change to stay accurate — rider `layer-crossrepo-token`'s premise — did, and it now
records its own deadline as arrived and unpaid.

### 2.5 `L-3` — the entry exists, is well-formed, and its citation checks out

`HD-47` is the newest `§live` entry, ahead of `HD-44`, and it carries every part the log's own
header requires: a one-thing title, the `date · user · scope · status` line, the ruling, its
relation to rider `RA`, its consequences, and a `basis` chain. Its `status: live` is qualified
with what would move it to `implemented` (a re-signature of `split-design.md` §1, or a design
round writing the command-surface criterion into the layer), and that qualification is anchored
correctly — `HD-40` :232 does say later substantive changes owe a re-signature. The log's
「至多一个 live 条目 per topic」 invariant holds: the eight `§live` entries are `HD-47`, `44`,
`41`, `36`, `35`, `34`, `23`, `9`, and no other is on the command surface.

Its factual tail checks out: 「命令面自此为七」 — `cli.py`'s docstring says seven and lists seven,
`OPERATIONS` is seven, and §2.3's mutation shows the two are actually bound to the parser rather
than merely agreeing on paper. 「故意不做的五件」 — `init_target.NOT_DONE` holds exactly five.
「机械的四件」 — the four are the four the suite pins.

Rider `RA`'s treatment is right and is the delicate part: its ruling, its routing and its
redeem-when are byte-unchanged, and the added clause says only that `HD-47` answered a different
question, so the precedent is neither reversed nor silently consumed.

**What is not closed** is when the ruling happened — see `V-1`.

### 2.6 Cold read `O-2` — closed by removing the drift surface, not by re-counting

`candidate_path_check.py`'s docstring no longer carries a member count in prose. It ships the
expression instead, and I ran it:

```
$ python -c "from hooks import layer_path_check as L, candidate_path_check as C; \
             print(len(L.LAYER), len([p for p in L.LAYER if C.scanned(p)]))"
10 7
```

Seven, and the three excluded are the three the docstring accounts for: the two retired-contract
stubs (a `RECORD_SURFACE` prefix exempts them) and `paragraph-map.schema.json`, which the
docstring's own qualifier — *the **Markdown** instruction-layer members* — excludes. `LAYER` is
outside this range, so 7 at `4029b43` is 7 at `2026a14`, and the stamp is honest. The docstring's
account of how the old figure went stale (six from `SIMP-A4` until `ORCHESTRATION.md` became the
tenth member: 4 + 2 = 6 before, 5 + 2 = 7 after) is arithmetically right. This is the `E6`-shaped
fix — the count that could drift is gone, and no guard was added to watch it.

### 2.7 The battery, re-run rather than accepted (`E3`)

```
$ python -m pytest -q          # from ResearchSystem/tooling, at 4029b43
733 passed in 93.19s (0:01:33)
```

733 is the fix commit's figure and the FULL's figure at `2026a14`; the fix adds no test and
removes none, which is what a six-tuple replacing a five-tuple should look like. The renamed
tests are not orphaned: the only reference to the old name anywhere is inside an immutable
review record (`v3-review-full-297bb2b.md` :102), and `test_fix_round_locks.py` :327's prose
cites the class names `TheSurface` / `TheTwoNames`, both of which still exist.

---

## 3. Lows

### `V-1` — the entry written to answer `L-3` dates the ruling a day later than the two sites `L-3` named, and both sites are in files this commit edited

**Location.** `ResearchSystem/HARNESS-DECISIONS.md` :31 (`- 2026-08-19 · user · scope: standing`)
and :44 (`basis: 用户裁决 2026-08-19（对话；三形态里取「甲 + 给 dtw 加 init」）`), against
`ResearchSystem/tooling/rsclib/document_harness/cli.py` :8 (*"the user ruled on 2026-08-18 that a
seventh command may exist"*) and
`ResearchSystem/document-harness/journal/caller-onboarding-2026-08-19.md` :44 (*"The user ruled on
2026-08-18 that a seventh may exist."*). Rider `RA`'s new clause takes the log's side
(「2026-08-19 用户就 onboarding 另裁了一个第七命令 `dtw init`」).

**Ground truth.** Sweeping the whole tree outside review records for a date attached to this
ruling returns exactly those four sites, two saying 2026-08-18 and two saying 2026-08-19:

```
$ git grep -n -I -E "2026-08-18.*(seventh|第七)|(seventh|第七).*2026-08-18" -- . ':!ResearchSystem/migration'
ResearchSystem/document-harness/journal/caller-onboarding-2026-08-19.md:44
ResearchSystem/tooling/rsclib/document_harness/cli.py:8
```

The two 08-18 sites are not sites this round left alone: `cli.py` was edited five lines below the
sentence (:13), and the journal paragraph the fix **adds** begins immediately after the sentence
and is about precisely this entry landing. The commit body itself carries a third date —
*"The user approved the boundary on 2026-08-19"* — for a different ruling, which is what makes
the collision easy to miss.

**What changes if it stays.** `HD-47`'s own `status: live` says it stays required reading until a
re-signature of `split-design.md` §1 carries it. Whoever drafts that re-signature has to state
which ruling is being carried, and the repository gives two answers with nothing reconciling
them: either `HD-47` records a second, later ruling that narrowed or re-confirmed the first — in
which case the log now holds one entry for two rulings and `HD-4`'s granularity rule is engaged —
or it records the same ruling under the wrong date, in which case two live sites contradict the
log that `E10`'s tail makes required reading, and the decision log is the artifact whose whole
claim is to be the higher source when text and ruling disagree. This is the exact residue `L-3`
existed to remove: the ruling stops living only in commit bodies, but the commit bodies and the
log now disagree about it.

**`R4` / `R7` ceiling.** I cannot see the conversation and therefore cannot say which date is
right, or whether there were one ruling or two. What I can say is that the repository disagrees
with itself, that no sentence anywhere acknowledges the disagreement, and that both stale sites
sit in files this commit had open.

**Bytes.** Not supplied — supplying them would require choosing a date, which is the user's.

### `V-2` — the `L-1` class sweep is reported by conclusion, not by output, and its accounting is short of the class

**Location.** The `L-1` sentence of `4029b43`'s commit body: *"the scan found two live sites
beyond the two the record named … so four live sites are fixed, three deliberately historical
sentences are left standing …, and two signed sites … are banked at closeout."* No pattern is
named and no grep output appears.

**Ground truth.** `HD-41` ④ is explicit that the discipline is the *output*: 「**把 grep 输出贴进
commit 正文**；扫类是动作不是自觉，贴证据是为了「跑没跑」可被评审员当场看见」. `L-2` — accepted and
repaired in this same commit — was filed for exactly that failure, and the repair pasted the
figures for its own sweep while its neighbour reported a second sweep by conclusion only.

Declaring my own range, because the fix declares none: whole tree at `4029b43`, review records
under `ResearchSystem/migration` excluded, pattern
`six (operations|commands|subcommands)|these six|the six v3|六命令|六个命令|六条命令|6 operations|六操作`.

```
$ git grep -c -I -E -i "<the pattern>" -- . ':!ResearchSystem/migration'
README.md:1 · HARNESS-DECISIONS.md:3 · HARNESS-RIDERS.md:1 · EXECUTION.md:1 · io-design.md:1
journal/batch-b-2026-08-11.md:1 · journal/caller-onboarding-2026-08-19.md:1 · split-design.md:1
tests/document_harness/test_cli_entry.py:1 · tests/…_review/test_dispatch_freeze_marker.py:1
                                                    -> 10 files, 12 lines
```

Of those twelve: three are `HD-47`'s own quotations of `split-design`'s text and are correct; one
is the different class cleared in §2.3 (`EXECUTION.md` :335); one is the repaired rider row; two
are the banked signed sites; one is `README.md` :59, separately routed by the FULL's `O-3`. That
leaves **four historical sentences**, of which the body's accounting names one:

- `tests/document_harness_review/test_dispatch_freeze_marker.py` :10 — *"the file the six
  commands lived in until the split batch's R2 moved them"*;
- `journal/batch-b-2026-08-11.md` :239 and `journal/caller-onboarding-2026-08-19.md` :42 — the
  latter in a file this commit edits.

Both directions of the mismatch matter. My pattern does **not** reach two of the three sentences
the body says it left standing (`cli.py` :9–10 *"under which the six travelled"*,
`test_cli_entry.py` :37 *"Six until 2026-08-19"*), so the executor's pattern and mine are demonstrably
different — and the executor's is not written down anywhere.

**What changes if it stays.** Nothing in the tree is wrong because of it — I read all twelve, and
every one is either accurate, already routed, or correctly banked. What is unavailable is the
check itself: a later auditor asking *was this class actually swept, and under what pattern* has a
conclusion and no evidence, and the one number the body does give — three sentences left standing —
is short of what any pattern I can construct returns. `HD-41` ④ is pure discipline with a reviewer
as its only enforcement, which is why the miss has to be written down rather than absorbed.

**Bytes.** None supplied — the fix is the run's actual output, which only the executor has, and
the commit that would carry it is already written (`E8`: no amend).

---

## 4. Observations

### `O-1` — rider `e1-disclose-home`'s deadline arrived inside this round, unpaid and unnamed

The row was written at `8fbd8ea` (2026-08-18, ORCHESTRATOR-CHARTER closeout) and its deadline is
「下一个必须遵守该句的构造轮（本轮之外的第一个）」. CALLER-ONBOARDING is that round. The row's
complaint is that `E1`'s intermediate-disclosure sentence says *the round states in its record*
without saying **where** or **who**, and notes that ORCHESTRATOR-CHARTER put all three of its
disclosures in commit bodies by its own choice. This round did the same, twice — the candidate's
`E1` paragraph and the fix's, both in commit bodies, neither in a place any rule names.

Neither the candidate, nor the fix, nor the FULL mentions that the deadline landed. The row's own
fix is design-shaped, so `HD-37` ② correctly points it at a round-eligible surface rather than a
batch — meaning the arrival is not a failure to redeem, it is a fact the closeout should record
so the next reader is not told the deadline is still ahead. Reported, not routed (`R5`).

### `O-2` — the new item-9 sentence says a POSIX clone stops running the hook *silently*; this repository's own record says *with a warning*

`ONBOARDING.md` item 9's added *Do* text reads *"Windows with `core.fileMode=false` hides the
difference until a POSIX clone **silently** stops running it"*. The committed record whose finding
`B-1` re-raised says the opposite adverb: `v3-review-full-eb6fbc2.md` :184 — *"a tracked hook
committed `100644` is **skipped with a warning** on any POSIX clone"*.

**Ceiling, stated rather than dropped (`E3`).** There is no POSIX checkout on this machine and I
did not run one, so I cannot adjudicate which is right; I am reporting that the instruction layer's
procedure document and a committed review record now describe the same behaviour with contradicting
adverbs, in a row added *because* the earlier record was right about the mode. The prescribed
action is unaffected either way — commit it executable, check `git ls-files -s` prints `100755` —
which is why this is an observation and not a low. It bites only on the day someone debugging a
Linux checkout is told there is no signal to look for.

---

## 5. Coverage, and what this VERIFY did not establish

**Read in full:** `CONSTRUCTION-CHECKLIST.md` (both sides; blob `87add4ce`) and the review-contract
stub it supersedes (blob `b576a45e`); `HARNESS-DECISIONS.md` `§live` in full and its entry index in
full (blob `bd00df9e`); the complete diff of all 10 paths in the range, end to end; the fix commit
body and the record commit body; `v3-review-full-2026a14.md` in full; `templates/decision-log.md`;
`test_init_command.py` :1–140; `test_cli_entry.py` :1–95; `cli.py` docstring and parser tail;
`candidate_path_check.py` docstring; `.githooks/pre-commit`; `ONBOARDING.md` :20–50 and :78–130;
`io-design.md` §6; rider rows `RA`, `layer-crossrepo-token`, `e1-disclose-home`.

**Read in part:** `EXECUTION.md` (:325–350 only, to clear the `six commands` near-miss);
`document-harness/README.md` (:34, the *Local enforcement* row); `HARNESS-DECISIONS.md`
`§implemented` (`HD-40`, `HD-41`, `HD-46` by grep and section read); `HARNESS-RIDERS.md` (all row
ids, three rows in full); `v3-review-full-eb6fbc2.md` (:180–190); `init_target.py` (:45–70);
the caller's `HARNESS-LEDGER.md` / `HARNESS-POLICY.md` (grep only — not my subject, opened solely
to test counts the subject asserts). **Not read:** `REVIEW.md`, `ORCHESTRATION.md`,
`document-harness/README.md` beyond :34, `split-design.md` beyond :44.

**Executed:** the full battery at the tip; the six-block template mutation at `4029b43` **and** at
`2026a14`, each with clean baselines on both sides and byte-identity asserted after every restore;
one parser mutation against the renamed surface test; a real `--no-local` clone to check the hook
mode survives; the layer/candidate scanned-member expression; five whole-tree sweeps (two
patterns × instrument, three × caller). All scratch copies, the driver and the clone are outside
both repositories and have been deleted; the subject worktree was never modified, verified clean
before and after (`git status --porcelain` empty; template sha256 `8e9d863c…d038d2` unchanged).

**Not established.**

- **The POSIX half of `B-1`, still.** I have the tree mode, the index mode, and the clone
  carrying it. The behaviour of a POSIX git on a `100644` hook is documented behaviour and a
  committed record's finding, not a run I performed — and `O-2` is the residue of that gap.
- **Which date `HD-47`'s ruling has.** `V-1` states the contradiction; resolving it needs the
  conversation, which `R7` puts outside my reach.
- **That the sweeps the fix reports are the sweeps it ran.** I reproduced every figure with the
  declared pattern and exclusions, which proves the figures are true at this tip. It does not
  prove the executor ran that command at that time, and `V-2` is about precisely the evidence
  that would have.
- **`R4` process claims.** That the FULL's record was committed unchanged, and that the executor
  subagent held none of `R1`'s four holdings, are **marked, not verified**.
- **My own independence, stated as the fix states it.** The work side holds *dispatched by* for
  this VERIFY: the orchestrator that dispatched me also authored three of the byte changes in the
  subject (`HD-47`, rider `RA`'s pointer clause, item 9's mode sentence), by its own disclosure.
  My prompt, scope and reporting channel are the standing contract's, but **this review is not
  structurally independent in all four**, and this record does not claim otherwise.
- **That the repair is defect-free.** Two blockers closed by mutation, three lows and one read
  finding answered on the merits, two lows and two observations returned. Mutation proved the six
  header pins and the renamed surface test have binding force; it did not prove that force is
  sufficient anywhere. A VERIFY is never a re-certification (`R4`).
