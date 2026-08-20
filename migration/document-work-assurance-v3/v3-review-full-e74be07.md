# FULL review — round `LEDGER-SPLIT`, caller range `7c54507..e74be07` (instrument `7701f03..acbc553`)

**Verdict: `CHANGES_REQUIRED`.** 1 blocker · 3 low · 4 observation.

---

## 0. Dispatch as received, and what I refused to take from it

One range — `7c54507ce40347ac60b3feff316eff4ef26f14a3..e74be0764eccd8cbd8c29cec2216970d32f7f0a2` —
plus the standing-contract pointer and one transport paragraph (Windows shell shape; where to
write this file). No round name, no budget, no obligations, no authorization. Everything below
that names a round, a rule, a count or a path was re-derived here (`R2`); where a figure could
only come from chat it is named as such in §7 and is not folded into anything supported (`R4`).

**Standing instructions read.**
`ResearchSystem/migration/document-work-assurance-v3/v3-harness-review-contract.md` (a stub) →
`ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` in full, both sides, per the stub's
"read all of it". Then the rest of the layer as the subject required: `README.md`,
`ORCHESTRATION.md`, `EXECUTION.md` §*Regression-battery tiering* in full and the rest sampled,
`REVIEW.md` by grep only. `ResearchSystem/HARNESS-DECISIONS.md` `§live` in full (HD-48, HD-47,
HD-44, HD-41, HD-36, HD-35, HD-34, HD-23, HD-9) plus the file header; from `§implemented`,
HD-2, HD-5, HD-22, HD-28, HD-33, HD-37, HD-38, HD-46 by grep, because claims I checked cite
them. `ResearchSystem/HARNESS-RIDERS.md` for the two rows this round edited and the two it
touches without editing.

## 1. Subject, re-derived

```
$ git -C D:/Thesis-stage-control-refactor rev-parse HEAD
e74be0764eccd8cbd8c29cec2216970d32f7f0a2

$ git -C D:/Thesis-stage-control-refactor status --porcelain --untracked-files=no
 M .claude/settings.local.json

$ git -C D:/Thesis-stage-control-refactor/ResearchSystem/harness rev-parse HEAD
acbc553ff2ab8971e0780f0ad0b317b91ca61c85

$ git -C D:/Thesis-stage-control-refactor/ResearchSystem/harness status --porcelain --untracked-files=all
(no output)
```

The instrument worktree is clean, so blob = working-tree file for every instrument measurement
below; the caller carries one unrelated modified path outside the subject. Both are falsified
from the moment this file is written by exactly one path — this record, untracked until the
orchestrator commits it.

**The range carries two repositories.** The caller range is one commit; its gitlink moves.

```
$ git diff 7c54507 e74be07 -- ResearchSystem/harness
-Subproject commit 7701f03091a606bcee98340d708b5005745b6031
+Subproject commit acbc553ff2ab8971e0780f0ad0b317b91ca61c85

$ git -C …/harness log --oneline 7701f03..acbc553
acbc553 V3-LEDGER-SPLIT-v1
eea11e1 V3-LEDGER-SPLIT-RIDERS-L2-O2-v1
30b33a9 V3-LEDGER-SPLIT-FREE-L1-v1
00a3d48 V3-REVIEW-RECORD-LEDGER-SPLIT-7701f03-v1
```

So the subject is five commits over two repositories. Classified by hand from
`git diff --name-status` at both ends: caller = 16 plan deletions + 1 archive deletion + 1
ledger rewrite + 1 policy edit + 2 mirror edits (`CLAUDE.md`/`AGENTS.md`) + 3 link-retarget
files + 1 gitlink = 25 paths. Instrument = 2 new ledger files + 16 new plans + 1 new read
record + 2 instruction-layer member edits with a third and fourth inside them (the two stubs)
+ 1 rider-bank edit = 24 paths.

**The review window held.** `.harness/review-pending.json` names this range and
`2026-08-19T07:31:21+00:00`; the caller candidate is committed at `17:31:11 +1000` =
`07:31:11Z`, ten seconds before the window opened, and the branch has taken nothing since.
`R4` ceiling: I re-derived that the window held; the instrument repository runs no
`review_freeze_check` (its `.githooks/pre-commit` says so in its own comment, and rider
`self-caller-guards` banks the question), so for the four instrument commits nothing *made*
it hold.

## 2. What the round claims to have done, checked against what it did

### 2.1 The move is byte-exact — verified independently, seventeen for seventeen

The claim is that sixteen plans and the ledger archive travel byte-identical. I did not read
the executor's MATCH list; I compared object names at both ends.

```
$ git -C <caller> ls-tree -r 7c54507 --format='%(objectname) %(path)' -- .goals/plans \
      ResearchSystem/HARNESS-LEDGER-archive.md
$ git -C <instrument> ls-tree -r acbc553 --format='%(objectname) %(path)' -- \
      ResearchSystem/document-harness/plans ResearchSystem/CONSTRUCTION-LEDGER-archive.md
```

Every one of the sixteen plan blobs is identical across the two trees, and
`HARNESS-LEDGER-archive.md` → `CONSTRUCTION-LEDGER-archive.md` is `50d3e66edcadd4de…` at both
ends. Seventeen of seventeen. The eleven plans left behind (`arm3-binding-lab`,
`capsicum-one-sandbox-per-agent`, `research-agent-dev-p3corr-p4`,
`research-system-agent-integration`, `research-system-p5c-p8-revision`,
`research-system-p9-architecture.draft`, `research-system-stage-control-refactor`,
`shared-sandbox-identity-intake`, `stage2-p4-activation-bridge-run`,
`thesis-department-redesign`, `thesis-harvest-lab-results`) are product-run, thesis and lab
plans; 27 at base, 16 moved, 11 remain.

### 2.2 The scan-class claim holds

The instrument commit claims the class was swept rather than the two named links: "grep for
`.goals|HARNESS-LEDGER` over the ten members returned five, re-run returns zero". Re-run at
both ends over `E10`'s ten paths:

```
$ git grep -n -E "\.goals|HARNESS-LEDGER" 7701f03 -- <the ten>     → 5 hits
  CONSTRUCTION-CHECKLIST.md:6 · README.md:16 · README.md:37
  v3-harness-operating-contract.md:3 · v3-harness-review-contract.md:3
$ grep -n -E "\.goals|HARNESS-LEDGER" <the ten, at acbc553>        → 0 hits
```

Five and zero. `HD-41` ④ satisfied, and this is the one place in the round where the scan
discipline visibly did its job.

### 2.3 The verification legs reproduce

`EXECUTION.md` §*Regression-battery tiering* makes the tier turn on the change surface, with
an explicit clause: a gitlink bump "is not a prose/markdown path, so a caller-side batch
carrying one is never doc-only, and the caller's five legs run at every bump", while a change
to the *content* of a path-pinned doc file, its path unchanged, "stays doc-only".

Instrument tier — every changed path is markdown outside the schema, tooling and generated
trees; `document-harness/README.md` changes content at an unchanged path. Doc-only is the
correct call. Ran the single leg anyway:

```
$ cd ResearchSystem/tooling && python -m pytest -q
733 passed in 87.31s
```

Caller tier — the gitlink moves, so the five legs are owed. All five re-run here at the tip:

```
$ python ResearchSystem/tooling/tests/run_tests.py        tests: 29   passed: 29   failed: 0
$ python ResearchSystem/tooling/tests/run_p4_tests.py     tests: 80   passed: 80   failed: 0
$ python ResearchSystem/tooling/tests/run_p5a_tests.py    tests: 39   passed: 39   failed: 0
$ python ResearchSystem/schema/fixtures/validate_fixtures.py  cases: 58  matched: 58
$ python ResearchSystem/tooling/rsc.py compile --check    RESULT: … exit 0
$ python Thesis/Work/Tooling/repo-audit.py
scope: 335 markdown files under the checkout root
[OK] Broken markdown links: 0
RESULT: clean (exit 0)
```

Every claimed figure reproduces. The tiering call is right on both sides.

### 2.4 `E2` untouched, decision log untouched

```
$ git -C <instrument> diff --stat 7701f03 acbc553 -- ResearchSystem/contract ResearchSystem/schema \
      ResearchSystem/HARNESS-DECISIONS.md
(no output)
```

No write to the frozen surface and none to the decision log. `HD-44` is the ruling that makes
the *archive*'s relocation a non-write in any case, but nothing on `E2`'s list moved at all.

### 2.5 The free-channel commit is inside its channel

`30b33a9` applies the read's `L-1` bytes to member 7. I checked the three things the channel
turns on rather than the label: the read record supplies the replacement verbatim (§L-1,
*Minimum fix — exact bytes*) and the applied line matches it word for word; the stub is not on
`E2`'s frozen list (which names the two supersessions and the schema pack, never the stubs);
and the commit lands alone, per `HD-38`. It records that it still owes its independent read.

I also re-derived the substance the replacement asserts, because `E3` binds a factual claim
written into instruction text:

```
$ grep -n CONSTRUCTION_ROLE_INSTRUCTION ResearchSystem/tooling/rsclib/document_harness/dispatch.py
545:CONSTRUCTION_ROLE_INSTRUCTION = (
546:    "migration/document-work-assurance-v3/v3-harness-review-contract.md"
$ grep -n "CHARTER_OUTSIDE\|MEMBER =" …/tests/document_harness_review/test_dispatch.py
398,520: CHARTER_OUTSIDE = "migration/…/v3-harness-review-contract.md"
463:      MEMBER          = "migration/…/v3-harness-review-contract.md"
$ head …/tests/fixtures/expected-construction-prompt.txt   → "Your standing instructions are `{charter}`"
```

The old sentence was false and the new one is true. Note the fixture's `{charter}` is exactly
what my own dispatch prompt was rendered from, which is the same fact seen from the other end.

### 2.6 The riders commit is riders-only

`eea11e1` edits two rows and nothing else (`git diff` over the range shows one file, two
changed lines). Under the 2026-08-04 typing it consumes no leg. Its own content is where a
problem starts — see `L-1` below.

---

## 3. Blocker

### `B-1` — ten markdown links inside the sixteen moved plans resolved at the base and do not resolve at the tip; nothing in either repository can see it

**Location.** `ResearchSystem/document-harness/plans/` in the instrument, at `acbc553`:

| file | line | link target as written |
|---|---|---|
| `general-harness-v2-architecture-revision.plan.md` | 7 | `../../ResearchSystem/harness/ResearchSystem/migration/document-work-assurance-v3/N0/N0-record.md` |
| `harness-a2-construction.plan.md` | 32 | `../../ResearchSystem/harness/ResearchSystem/HARNESS-DECISIONS.md` |
| `harness-a2-construction.plan.md` | 38 | `../../ResearchSystem/harness/ResearchSystem/document-harness/journal/batch-a1-2026-08-08.md` |
| `harness-digest-narrowing.plan.md` | 126 | `../../ResearchSystem/harness/ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` |
| `harness-issue-redemption-batch.plan.md` | 169 | `../../ResearchSystem/harness/ResearchSystem/document-harness/journal/hi-redeem-5-2026-08-07.md` |
| `harness-record-layer-and-repo-split.plan.md` | 42, 251, 290 | `../../ResearchSystem/harness/ResearchSystem/document-harness/journal/batch-a1-2026-08-08.md` |
| `harness-record-layer-and-repo-split.plan.md` | 57 | `../../ResearchSystem/harness/ResearchSystem/document-harness/journal/record-layer-2026-08-05.md` |
| `harness-record-layer-and-repo-split.plan.md` | 59 | `../../ResearchSystem/harness/ResearchSystem/migration/document-work-assurance-v3/v3-review-full-0b8b824.md` |

**Scope of the measurement** (`HD-41` ①): inline markdown links `](target)` in the sixteen
`*.md` files under `ResearchSystem/document-harness/plans/` at the instrument worktree =
`acbc553`, excluding `http`/`https`/`#`/`mailto`, resolved with `(file.parent / target)`.
Result: 21 relative links, **10 broken**. The same measurement over all 24 changed markdown
files in the instrument range returns 76 relative links and 17 broken — the other 7 are in
`CONSTRUCTION-LEDGER-archive.md` and are covered by a disclosed policy (see `O-2`).

**The ground truth it violates.** These links worked before the move and do not work after it,
and both halves are commands, not judgment:

```
$ ls "…/.goals/plans/../../ResearchSystem/harness/ResearchSystem/HARNESS-DECISIONS.md"
-rw-r--r-- … 48461 … HARNESS-DECISIONS.md                                    ← resolves

$ ls "…/document-harness/plans/../../ResearchSystem/harness/ResearchSystem/HARNESS-DECISIONS.md"
ls: cannot access … : No such file or directory                              ← does not
```

Every one of the seven distinct targets exists in the instrument, one segment shorter:
`ResearchSystem/HARNESS-DECISIONS.md`, `…/document-harness/CONSTRUCTION-CHECKLIST.md`,
`…/document-harness/journal/{batch-a1-2026-08-08,record-layer-2026-08-05,hi-redeem-5-2026-08-07}.md`,
`…/migration/document-work-assurance-v3/{N0/N0-record.md,v3-review-full-0b8b824.md}` — all
seven confirmed present by `ls`.

**Why nothing caught it, which is the part that matters.** The caller's `repo-audit.py` does
check markdown links and reports zero — because it excludes this tree by construction:
`SUBMODULES = ('ResearchSystem/harness/',)` at `:48`, applied in `excluded()` at `:55`. The
instrument's `.githooks/pre-commit` runs exactly one check, `layer_path_check.py`, whose
`LAYER` is `E10`'s ten members (`:30–41`) and whose `TOKEN` regex reads backticked tokens
only. Sixteen plans under `document-harness/plans/` are in neither set. So the round moved
sixteen files out of a link-checked tree into an unchecked one and broke ten links on the way,
and no guard in either repository could have said so. That is the omission-made-invisible
shape this harness exists to surface, occurring inside the harness's own tree.

**Not covered by the round's own history carve-out.** The round did recognise this class — for
the archive. `CONSTRUCTION-LEDGER.md`'s header declares "Caller paths inside these entries are
historical facts, not links … left exactly as they were written; the same rule as the archive's
title", and the commit body says history is not rewritten to match its new shelf. No such
declaration covers `plans/`, and the plans are not presented as history: `README.md:16` at this
same commit advertises them as current navigation ("with the other construction-batch plans in
[plans/](plans/)"), `CONSTRUCTION-LEDGER.md` links four of them as live pointers, and
`harness-repo-split.plan.md`'s backlog is cited by the ledger as *open* work. A live document
whose links are dead is a different thing from an archive that quotes an old path.

**Minimum fix**, either arm, in one commit:

- **(a)** retarget the ten: replace the literal `../../ResearchSystem/harness/ResearchSystem/`
  with `../../` in each of the ten links above. Mechanical, byte-exact, targets verified
  present; the byte-identity provenance is unharmed because it is anchored permanently by the
  caller's history at `7c54507` and by `acbc553` itself, both immutable. **Or**
- **(b)** if the user prefers the archive's treatment, extend the declared "historical facts,
  not links" carve-out to `plans/` explicitly, in the same commit that advertises them as
  navigable — and then `README.md:16`'s presentation of `plans/` needs to match.

`E6` note: neither arm needs new machinery, and I am not proposing one. Whether the instrument
repository should acquire a link check at all is not mine to conclude (`R5`) — it is already
banked as part of rider `self-caller-guards`' shape, and I only report that today the class is
unguarded here.

---

## 4. Low

### `L-1` — the round paid two of rider `layer-outbound-refs`' six items and left the row saying six

`eea11e1` corrected that row at `15:55` to "六处引用（五个不同目标）… README《Authoritative
documents》与 Predecessors 各一条 `.goals/plans/*` 链接 · `REVIEW.md` … · `EXECUTION.md` 两处
… 与一处 …". `acbc553` at `17:29` then retargeted exactly those two README links so that they
resolve. Measured at the tip, over the ten members:

```
$ grep -n fef3a2e ResearchSystem/document-harness/REVIEW.md
45: [`v3-review-full-fef3a2e.md`](../migration/document-work-assurance-v3/v3-review-full-fef3a2e.md)
$ ls …/migration/document-work-assurance-v3/v3-review-full-fef3a2e.md   → No such file
$ grep -n "assurance/runs" ResearchSystem/document-harness/EXECUTION.md
186, 449 (p5a-shells audit-rounds.md)   452 (p4-doc issue JSON)
      (:259 is a `<run-id>` placeholder, not a concrete path — excluded)
```

Four occurrences over three distinct targets, not six over five. The row's *count* is
revision-pinned ("read `7701f03` `O-2` 独立重测为六/五"), which is `HD-41` ③ behaving as
designed and is why this is not a blocker; but the row's *item list* is the outstanding-debt
statement, and two of its items were paid inside the same round. `R10`'s redemption condition
was met and not honoured: the row's own redeem-when names "下一批碰 README《Authoritative
documents》表", and `acbc553` is that batch touching that table.

*Minimum fix.* Strike the two README `.goals/plans/*` legs from the row's enumeration and
restate the figure as four occurrences over three targets measured at `acbc553`, noting the
partial redemption. Riders-only under the 2026-08-04 typing, so it costs no leg.

### `L-2` — `CLAUDE.md:24` and `AGENTS.md:24` carry a malformed nested markdown link

Both files, identical (the mirror rule holds — the defect mirrors too):

```
… and lives at [[ResearchSystem/harness/ResearchSystem/CONSTRUCTION-LEDGER.md](ResearchSystem/harness/ResearchSystem/CONSTRUCTION-LEDGER.md)](ResearchSystem/harness/ResearchSystem/CONSTRUCTION-LEDGER.md).
```

A link whose text is itself a link. It renders as a `[` , a working link, then a literal
`](ResearchSystem/…CONSTRUCTION-LEDGER.md)` in the running prose. `repo-audit.py` reports zero
broken links because the inner link resolves, so the audit's clean run is true and does not
cover this. The commit body records this as one of three backtick tokens converted "to plain
markdown links" after `candidate_path_check` blocked the first attempt — so the pre-submission
correction is where it came from, and it was not re-read after being applied.

These two lines are the agent-facing entry file, and `ORCHESTRATION.md` makes the caller's
entry file the only discovery path a cold orchestrator has for the policy file. Bytes for the
fix, both files, replacing the nested construct:

```
… and lives at [ResearchSystem/harness/ResearchSystem/CONSTRUCTION-LEDGER.md](ResearchSystem/harness/ResearchSystem/CONSTRUCTION-LEDGER.md).
```

### `L-3` — three count-and-scope errors in the caller candidate's commit body (one class, `E3` / `HD-41` ②)

Filed as one finding because they are one defect class (`E7`), all in `e74be07`'s body, all
falsifiable by a command:

1. **"rewritten from 120 lines to 57"** — the base file was **113** lines.
   `git show 7c54507:ResearchSystem/HARNESS-LEDGER.md | wc -l` → `113`, and the same commit's
   own diffstat corroborates it: `170 ++---` = 113 deletions + 57 insertions. 120 is the
   *cap*, not the count; the two were conflated.
2. **"Four remaining caller files retarget five plan links"** — **three** files, five links,
   and the body's own parenthetical names three: `.goals/LEDGER-archive.md:76` (two links),
   `.goals/plans/research-system-p5c-p8-revision.plan.md:51`,
   `.goals/plans/research-system-stage-control-refactor.plan.md:20,:608`. Verified by
   `git grep -n -E "\]\([^)]*plans/(…)" e74be07`, which returns exactly those four lines.
3. **The "not retargeted" enumeration is short by one category.** The body names three —
   immutable review records, digest-bound artifacts under `assurance/runs/`, the untracked
   machine log. `git grep -l` for the sixteen moved plan paths at `e74be07` returns 21 files
   in **four** categories; the fourth is `ResearchSystem/assurance/shadow/round-3/`
   (`dispatch-prompt-run-a1.md`, `dispatch-prompt-run-p3.md`), which is neither a review
   record nor under `assurance/runs/`.

None of the three changes an outcome; each is the shape `HD-41` was created to stop, and the
first is contradicted by a number printed in the same commit. `E8` bars amending, so the fix
is an erratum in the round's record, not in the body.

---

## 5. Observations

### `O-1` — the construction ledger left a mechanically-enforced line cap behind and is over the old bound at birth

The base ledger's own heading carried its cap: "全文件 ≤120 行，`ledger_cap_check.py` 机械
enforce". The new `CONSTRUCTION-LEDGER.md` heading declares what may enter and what may not,
and no size bound at all. Measured: caller `HARNESS-LEDGER.md` **57** lines (under its cap,
which stays), instrument `CONSTRUCTION-LEDGER.md` **130** lines. `ledger_cap_check.py:19` is
bound to the literal string `ResearchSystem/HARNESS-LEDGER.md` and lives in the caller; the
instrument's hook runs only `layer_path_check.py`. So the larger half of what used to be one
capped file is now uncapped and already ten lines past the bound it was under yesterday.
Whether it should have a bound is the user's question, not mine (`R5`); the fact that the
round moved content out from under a guard without saying so is what I am reporting.

### `O-2` — seven broken links in `CONSTRUCTION-LEDGER-archive.md`, six covered by the declared policy and two pointing at files that are here

`:24, :518, :544, :547, :622` are `../.goals/plans/*` — caller history, squarely inside the
"historical facts, not links" declaration. `:559` and `:576` are different in kind:
`harness/ResearchSystem/migration/document-work-assurance-v3/{N0/N0-record.md,N1/N1-record.md}`
name *instrument* records that exist in this repository at `ResearchSystem/migration/…`. They
are still history and I am not asking for them to change; I record that the declaration's own
example set ("`handoffs/…`, `assurance/runs/…`, `.goals/LEDGER.md` — those tokens resolve in
the caller, not here") does not describe these two, which resolve nowhere and name something
local.

### `O-3` — three surfaces are false at the tip; all three are disclosed as reserved to closeout

- `ResearchSystem/HARNESS-DECISIONS.md` `HD-28` (scope `standing`, status `implemented`) still
  reads "**`HARNESS-LEDGER.md` 与 `HARNESS-LEDGER-archive.md` 留调用者仓**". Its successor
  entry has not landed. The file header's invariant is "supersession 与 live→implemented 的挪
  节都在**同一 commit**", and `HD-37`'s own status note applies that as carrier-and-transition
  together, recording a three-commit lag as a deviation. Here the carrier is `acbc553` /
  `e74be07` and the transition is absent.
- `document-harness/split-travel-manifest.md:75` and `:127` still assign `HARNESS-LEDGER.md`
  and its archive to the caller, citing `HD-28`.
- `.goals/LEDGER.md:24` still routes readers to the caller ledger for "未结项、开着的裁决与
  rider"; the caller ledger holds none of those now.

`e74be07`'s body names all three as deliberately held for the orchestrator's closeout. I take
the disclosure at face value and report the state rather than the intent, because a reader
arriving at the tip meets the state.

### `O-4` — what is load-bearing and lives only in chat (`R2`, `R7`, `R4`)

- **The round's authorization.** The (a)/(b) classification ruling of 2026-08-19, the batch
  name, and the "round instruction's R0.4" that reserves the closeout appear nowhere in either
  repository — `grep -rn "DTW-INDEPENDENCE" D:/Thesis-stage-control-refactor` returns nothing.
  `R7`: a hint, never a block. I state the ceiling: I cannot see what was authorized, so I
  cannot check the boundary the work was meant to stay inside, only that the change set is
  coherent with the work described.
- **The schedule.** `HD-48` is `live` and names the next queue head as a three-topic design
  round; `CONSTRUCTION-LEDGER.md` repeats that at the tip. This round is not that round, and
  no committed ruling reschedules it. That is either an unrecorded user ruling or a queue
  deviation; I cannot tell which from the repository.
- **The executor's report.** Cited in both bodies as the home of the sixteen MATCH lines, the
  `cmp` check and the class-(b) enumeration. Not in the repository. The MATCH claim I
  re-derived independently and it holds (§2.1); the class-(b) enumeration and the "18
  class-(a) files" figure I could not reconcile against the diff (17 files moved; two review
  records named as staying; 18 is neither) and I leave it `UNVERIFIABLE` rather than reading a
  charitable arithmetic into it.
- **`E1`.** Both bodies disclose that the executor was a subagent the orchestrator dispatched
  and held none of `R1`'s four holdings, and that the three-token correction is the
  orchestrator's own bytes. Under `E1` as written that is the structurally-independent case
  and needs no middle-state disclosure. It is a process claim and I mark it, not verify it.
  What I can verify is my own side: I was dispatched by the orchestrator over a committed
  range, prompted by the fixture-rendered prompt, scoped by the repository, and this record
  goes back through the orchestrator — the executor holds none of the four.
- **`E11`.** No preview card is in either repository. Already a standing open item in the
  construction ledger; noted, not re-opened.

---

## 6. Process and boundary check (run second, per `R3`)

| check | result |
|---|---|
| `E9` budget | Intact. No valid independent FULL had occurred for `LEDGER-SPLIT` before this one, so the candidate and the pre-submission three-token correction consume nothing; the `E10` read (`00a3d48`) and free-channel application (`30b33a9`) are not rounds; the riders commit (`eea11e1`) is riders-only under the 2026-08-04 typing. This FULL is the first leg spent. |
| `E9` window (the read) | Marker `{"subject":"7701f03…","dispatched_at":"2026-08-19T05:37:48Z"}`; record committed `05:53:55Z`; `git log 7701f03..00a3d48` = that commit alone. Held. |
| `E9` window (this FULL) | Opened `07:31:21Z`, ten seconds after the caller candidate. Held so far. |
| `E10` cold read at opening | Present and committed before the candidate: `v3-cold-read-7701f03.md`, all ten members read end-to-end with blob ids stated. |
| `E10` member edits | Four members touched (`CONSTRUCTION-CHECKLIST.md:6`, `README.md:16/:37` + one new row, both stubs). Relied on under the deferral, with both facts recorded and the bytes riding the next read. See the caveat below. |
| `E10` free channel | Conditions met (bytes supplied, not `E2`-frozen, no round had relied on the sentence, own commit per `HD-38`). |
| `E2` | No write. Verified by empty diff over `contract/` and `schema/`. |
| `E8` | Titles name the round and the kind (candidate / free-channel / riders-only / record); single dense paragraph, no trailers; no push (27 unpushed on the caller, 4 on the instrument). |
| `R6` | The read record's commit title is `V3-REVIEW-RECORD-LEDGER-SPLIT-7701f03-v1`, the form the rule names. |
| `E12` | One range, no per-acceptance argument, and the recorded range in the freeze marker is written by the CLI. |

**One caveat on the `E10` deferral, and it is a low-grade one I am deliberately not filing
separately.** `acbc553`'s justification reads "every changed token is a location and its effect
on rounds in flight is nil" — but the same sentence, one clause earlier, discloses that
`README.md` "gains one navigation row naming the construction ledger — an addition beyond the
two named links". The new row is not a location change; it carries prose ("nothing of that kind
enters here"). The deferral's real ground — no clause added to any *rule*, nil effect on rounds
in flight — still holds, so the outcome is right and the stated reason is not. It is the same
absolute-quantifier shape as `L-3` and I count it there rather than twice.

---

## 7. Disclosure — what I read in full, sampled, and only probed (`R4`)

**In full:** `CONSTRUCTION-CHECKLIST.md` (both sides); `HARNESS-DECISIONS.md` `§live` + header;
`ORCHESTRATION.md`; `document-harness/README.md`; the new `CONSTRUCTION-LEDGER.md`; the caller's
new `HARNESS-LEDGER.md`; all five commit bodies; the full diffs of `HARNESS-POLICY.md`,
`CLAUDE.md`, `AGENTS.md`, `.goals/LEDGER-archive.md`, the four member files and
`HARNESS-RIDERS.md`; `EXECUTION.md` §*Regression-battery tiering*; both repositories'
`.githooks/pre-commit`; `ledger_cap_check.py`.

**Sampled:** `v3-cold-read-7701f03.md` (header, member table, `E2` check, `L-1` in full, other
findings by heading); `EXECUTION.md` outside the tiering section; `layer_path_check.py`
(`LAYER` + `TOKEN`); `repo-audit.py` (exclusion logic only); `HARNESS-DECISIONS.md`
`§implemented` (eight entries by grep); `HARNESS-RIDERS.md` (four rows).

**Probed by command only, not read:** the sixteen moved plans (link extraction and blob
comparison only — their *content* is unreviewed, and they arrived byte-identical from a tree
where they had already lived); `CONSTRUCTION-LEDGER-archive.md` (link extraction only, 658
lines unread); `REVIEW.md` (grep only); `dispatch.py` / `test_dispatch.py` / the prompt fixture
(the three constants only).

**Not verified, marked:** every process claim in `O-4`; that the executor was a subagent; that
the three-token correction was the orchestrator's bytes; that a preview card was rendered. No
mutation testing was performed and none was owed — this round adds no guard, so `E4` does not
attach; `R8`'s question here was the inverse one (which guard *could* have caught `B-1`), and
that I answered by reading the two guards' own scopes rather than by mutating them.

---

## 8. Verdict

**`CHANGES_REQUIRED`** — on `B-1` alone.

The round's substance is sound and unusually well evidenced: the move is byte-exact seventeen
for seventeen, the scan class was swept rather than the instances patched, the battery tiering
is correctly derived on both sides and every claimed figure reproduces, `E2` is untouched, and
the free-channel and riders-only commits are inside their channels. What failed is the thing
the round was least likely to look at: sixteen files changed repository, and ten of their
internal links changed meaning with them, in a tree where no check can see a link at all.

`L-1` is accounting the round itself invalidated one commit after correcting it; `L-2` is a
rendering defect introduced by the pre-submission correction and invisible to the audit that
was re-run after it; `L-3` is three numbers that a command in the same commit contradicts.
None of the three would justify spending the repair on its own. All three are cheap to carry in
the same commit as `B-1`'s fix, and `L-1`'s route is riders-only in any case.

The four observations are for the user, not for the executor: `O-1` and `O-2` are consequences
of the split that the round did not state, `O-3` is state the round declared it was holding
back, and `O-4` is the ceiling on what I could check at all.
