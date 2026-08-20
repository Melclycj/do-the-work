# VERIFY — split batch R1 repair, `0792a89..e6b4d2c`

**Verdict: `REVIEWED_NO_BLOCKER`** — every accepted finding is discharged, the repair diff is
sound in substance, and the permanent boundaries hold.

**Read the caveat before acting on that word.** One finding below (`F-1`) is blocker-shaped, and
`R3`'s VERIFY domain (`REVIEWED_NO_BLOCKER | SPEC_GAP`) has no word for it: it is not a `SPEC_GAP`
— the instruction is fine and a bounded repair would fix it — and the round's single fix is spent,
so it cannot be repaired inside R1. Had this been a FULL it would be `CHANGES_REQUIRED`. It is
therefore **reported and routed, not graded**: the disposition (open a round / bank / accept) is
the user's under `R5`. `F-1` is the same defect class as `B-1` — a factual claim about the
delivery written into a delivered document without running the command that could falsify it —
occurring inside the commit that fixed `B-1`.

Findings: 1 blocker-shaped, 4 low, 5 observations.

---

## 1. Subject, re-derived

Nothing here was accepted as reported (`R2`).

| | |
|---|---|
| Range | `0792a89067a74adf97a9090d94cc0ce93671e25c..e6b4d2c83bba11c1ab6e7b8b3a2236bbb65f31c7` |
| Branch / worktree | `document-work-assurance-v3` @ `D:/Thesis-stage-control-refactor`; `git status --porcelain` empty; `HEAD` == range tip; no upstream on this branch, so nothing is pushed (`E8`) |
| Freeze marker | `.harness/review-pending.json` names this exact range, `dispatched_at 2026-08-15T02:05:12+00:00`; tip commit `2026-08-15 12:04:28 +1000` = `02:04:28Z` — dispatch 44s after the last commit, so `E9`'s "branch takes no commit but the record" holds as of this read |
| Commits | 2: `22264b5` `V3-SPLIT-R1-FIX-B1-L1-L3-L4-L5-L6-v1` · `e6b4d2c` `V3-SPLIT-R1-RIDER-SCC-RETIRE-v1`. Author date == committer date on both (no amend/rebase evidence) |
| Paths | 6 `M`, 0 `A`, 0 `D`, classified by hand: `.goals/plans/harness-repo-split.plan.md` · `ResearchSystem/HARNESS-RIDERS.md` · `ResearchSystem/README.md` · `ResearchSystem/document-harness/EXECUTION.md` · `ResearchSystem/document-harness/split-travel-manifest.md` · `ResearchSystem/tooling/rsc.py` |
| Round / leg | Split batch **R1**, the repair leg. Base `0792a89` is the FULL's own record commit (`v3-review-full-e608204.md`, `CHANGES_REQUIRED`, 2 blockers / 6 low / 3 observations) |
| Budget (`E9`) | The FULL has occurred (its record landed at `0792a89`). `ls` over the migration directory returns no `*e6b4d2c*`, `*22264b5*` or `SPLIT-R1` verify record, so this is R1's one targeted VERIFY. `22264b5` is the one user-approved fix; `e6b4d2c` is riders-only and consumes nothing — see §5 |
| Authorization | The FULL's `CHANGES_REQUIRED` obliges the fix; the fix *scope* (B-1 + five low, approval "A", 2026-08-15) exists only as executor prose in `22264b5`'s body — `R7` ceiling, nothing in the repository contradicts it. `HD-39` authorizes the `SCC` retire by name; `HD-42` and the 2026-08-04 riders-only ruling are cited and both check out |
| Out-of-repo | `D:/do-the-work`, now 2 commits (`345acdd`, `8cd0b9c`), 255 tracked, `git status` clean. In remit and reviewed |

---

## 2. What I re-executed

The battery, in full, at the tip — not sampled, not taken from the commit body:

```
P2   tests/run_tests.py         tests: 29   passed: 29   failed: 0
P4   tests/run_p4_tests.py      tests: 80   passed: 80   failed: 0
P5A  tests/run_p5a_tests.py     tests: 39   passed: 39   failed: 0
fix  schema/fixtures/validate_fixtures.py   cases: 58   matched: 58   unexpected: 0
pytest -q (from ResearchSystem/tooling)     701 passed in 85.49s
rsc.py compile --check   RESULT: generated output fresh; lint clean (exit 0)
Thesis/Work/Tooling/repo-audit.py           RESULT: clean (exit 0)
```

Six legs, six green, plus repo-audit. The reported 29/80/39/58/701 reproduce exactly.
(`repo-audit.py` lives at `Thesis/Work/Tooling/`, not under `ResearchSystem/tooling/` — worth
recording because the obvious guess is wrong.)

**Guard mutation in the new repository** (`E4`/`R8`), in a throwaway clone of `D:/do-the-work`,
restored from a sha256-checked scratchpad copy rather than `git checkout --`:

```
LAYER count: 9        missing: []          # all nine E10 members resolve

# negative control — staged added line naming a path that DOES resolve
layer EXIT=0     candidate EXIT=0

# must-fire — staged added line naming `ResearchSystem/does-not-exist/nope.md`
pre-commit BLOCKED: newly added instruction text names a repository path that does not resolve
layer EXIT=1
pre-commit BLOCKED: newly written text names a repository path that exists nowhere
candidate EXIT=1

review_freeze_check EXIT=0     # `.harness/` does not exist in the new repo (HD-33)
pytest tests/document_harness/test_precommit_checks.py  ->  42 passed
```

Restored, sha256 identical, `git reset` clean. `B-1`'s replacement text reproduces in every
particular.

**Cross-repository byte identity, per file rather than in aggregate.** For each of the new
repository's 255 tracked paths I compared its blob id against the caller at the range tip:

```
new_repo_tracked=255   matched=254   mismatch=1   only_in_new=0
  MISMATCH  README.md   new=966621ae  caller=745adb8e
```

The single difference is the new repository's own authored `README.md`, whose path happens to
collide with the caller's unrelated root README; it is not a travelled file. So the resync claim
holds exactly: `EXECUTION.md`, `split-travel-manifest.md` and `HARNESS-RIDERS.md` are
byte-identical across the two repositories at the tip, and the two instruction layers and the two
rider banks did not diverge on their first day.

---

## 3. Accepted findings — discharge

| Finding | Discharged | Evidence |
|---|---|---|
| `B-1` guard posture recorded backwards | **Yes**, with one residual (`F-2`) | mutation output above; all three sites rewritten; the delivery exclusion deleted |
| `B-2` rider `SCC` not retired | **Yes** | rows 29 → 28 in both repos; `e6b4d2c` body names `HD-39`; `HD-39` does say "rider `SCC` 随其 subject 删除而在 R1 **retire**" |
| `L-1` unrecorded family survivor | **Yes** | `ResearchSystem/README.md` now says "171 files" and records the survivor, why `E8` barred deleting it, and whose it is |
| `L-2` dead import | **Yes** | `import json` gone; only `import json as _json` (`:308`) remains, used at `:319`; no bare `json.` reference survives |
| `L-3` absolute quantifier in the layer | **Yes**, see `O-2` | scoped to the five named legs and names the same-batch deletion; `HD-42`'s 39+20 checks out |
| `L-4` manifest revision label | **Partly** — see `F-3` | header corrected to `e4ffa2b` with a correction block; two same-file labels left at `a7437d3` |
| `L-5` R2 step naming deleted artifacts | **Yes**, mis-cited — see `F-4` | step 15 struck; both named test files absent at tip, present at `a7437d3` |
| `L-6` line count off by one | **Yes** | re-derived: `a7437d3` 856 → `a8af54c` **686** → tip **685** after `L-2` |

Re-derived independently: `git diff --diff-filter=D --name-only a7437d3 a8af54c | wc -l` = **171**,
and `HD-39`'s enumeration does not contain `ResearchSystem/generated/stages/README.md`, so `L-1`'s
load-bearing claim about `E8`'s boundary is sound. The three CLI groups are now
`inventory / compile / v3` (six v3 subcommands), matching what the plan says.

---

## 4. Findings

### F-1 — the delivered README's own "Measured consequence" is false, and what it hides is a delivery gap

**Blocker shape.** Reported and routed under the caveat at the top, not graded.

**Location.** `D:/do-the-work/README.md`, §*What does not work yet*, first bullet (written by
`8cd0b9c`); the same characterization in `22264b5`'s and `8cd0b9c`'s commit bodies.

**What it says.** "**Measured consequence, so that nobody discovers it the hard way:**
`python -m pytest -q` here is **24 failed, 677 passed** — every failure is
`can't open file '…/ResearchSystem/tooling/rsc.py'` **and nothing else**."

**Ground truth.** The count reproduces exactly (24 failed, 677 passed). The cause does not. Of
the 24:

```
15  traceback names rsc.py
 2  returncode 2 != 1 from a subprocess that runs rsc.py (test_dispatch_freeze_marker,
    test_fix_round_locks) — caused by it, does not name it
 7  NOT caused by rsc.py:
      3  GovernanceRealDocumentTests — "governance document not readable at
         <root>\.goals\plans\document-work-assurance-harness-v3.plan.md"   (caller-side, never travelled)
      2  GoldenCoverageView — "golden missing: run this file with --regen"
         (needs ResearchSystem/assurance/test/coverage-{view,document}.golden.{txt,json})
      2  test_dispatch.py …test_the_prompt_is_exactly_the_golden_file — FileNotFoundError on
         ResearchSystem/tooling/tests/fixtures/expected-{construction,read}-prompt.txt
```

Those last four are travelled tests whose fixtures did not travel. `assurance/test/` is excluded
**by name** in the manifest's own 不 travel list while `A4` carries the test that reads it; the
whole `ResearchSystem/tooling/tests/fixtures/` prefix — 100 files in the caller, **0 in the new
repo** — is covered by no `A` row at all, although two of its files are the goldens for `A5`'s
dispatch test. This is the exact shape the manifest's `A8` row congratulates itself on catching
for `A5` ("两个历史集合都漏了它，不跟走则 A5 直接红").

**Why it is not wording (`R9`).** Two actions change.
① The bullet tells R2 that the CLI extraction is the whole gap between here and green. It is not:
seven failures survive it, four of them because the instrument shipped without fixtures its own
tests need. That is a delivery-scope statement of the same kind `B-1` corrected in the other
direction.
② Two of the seven print "golden missing: **run this file with --regen**". A reader who follows
that instruction inside the new repository writes a golden from whatever the new repository
currently renders — silently replacing a pinned surface with its own output. The pin exists
precisely so that "a change to what the user sees must be a deliberate, reviewed change"
(`test_golden_views.py:187`).

**Rule breached.** `E3` — "a characterization of the work no command established … is dropped,
not softened". The falsifying command is the same `pytest -q` the round already ran, read one
level deeper (`--tb=line`); the count was measured and the cause was inherited from the FULL's
`O-2`, which asserted it without support. `E12`'s "reproduce a reported finding to write the fix
correctly" is the discipline that would have caught it: the count was reproduced, the causal claim
was not.

**Minimum fix.** Replace "every failure is … and nothing else" with the measured split (17 trace
to `rsc.py`, 7 do not), name the three missing dependencies, and state that extracting the CLI does
not by itself green the suite. Whether the four instrument fixtures belong in the travel set is a
manifest question for the user, not something the README should settle (`R5`).

### F-2 — the corrective passage for `B-1` contains a new false assertion about the same subject

**Low.**

**Location.** `ResearchSystem/document-harness/split-travel-manifest.md:143-145`, and its
byte-identical copy in the new repository.

**What it says.** "**真实状态 = 接线缺席、逻辑完好**：两个仓的 `.git/hooks` 都没装 pre-commit，这是
`document-harness/README.md:34` 已记的 per-machine 约定".

**Ground truth.** `D:/Thesis/.git/hooks/pre-commit` exists and calls all three checks:

```
52:for chk in ResearchSystem/tooling/hooks/review_freeze_check.py \
53:           ResearchSystem/tooling/hooks/layer_path_check.py \
54:           ResearchSystem/tooling/hooks/candidate_path_check.py; do
```

`core.hooksPath` is unset and `D:/Thesis/.git/worktrees/Thesis-stage-control-refactor/` holds no
`hooks/` directory, so git resolves hooks from the common dir — every commit made in this
worktree, including this round's own, runs it. The new repository has no hook (verified). So the
true state is **wired in the caller, not wired in the new repo**, not "neither". The FULL's own
sentence was accurate ("no hook is installed in either repository's `.git/hooks`; the source
repo's `pre-commit` lives in the main repo's `.git/hooks`"); the compression into 两个仓 dropped
the qualifier that made it true. The cited `document-harness/README.md:34` says the same thing
correctly. It matters because the passage's entire subject is *when the guards actually run*, and
the asymmetry it flattens is the one the section exists to explain.

**Minimum fix.** One clause: name the caller's hook as installed per-machine and the new repo's as
absent.

### F-3 — `L-4`'s repair fixed the header and left the same label on the two numbers the finding named

**Low.**

**Location.** `split-travel-manifest.md:22` ("量程 = 全仓 tracked … @ `a7437d3`") and `:112`
("**travel 合计 = A 108 + B 3 + C 143 = 254 @ `a7437d3`**").

**Measured.**

```
document-harness/   a7437d3: 25   a1b80fa: 26   e4ffa2b: 26   tip: 26
A subtotal          a7437d3: 107  e4ffa2b: 108  tip: 108
C (94 top + 49 sub) a7437d3: 143  e4ffa2b: 143
=> total            a7437d3: 253  e4ffa2b: 254
```

Line 112 asserts A 108 and total 254 **at the revision where the file's own new correction block
states they are 107 and 253**. Before the repair the file was uniformly (and wrongly) labelled
`a7437d3`; after it, the file contradicts itself — in the one document whose declared purpose is to
be the single authoritative membership definition and whose header invokes `HD-41` ①③ by name.
`E7` is the discipline: the defect class was the label, not the header line the finding happened
to cite.

**Minimum fix.** The same one-token change at `:22` and `:112`.

### F-4 — the struck plan step cites the wrong finding

**Low, wording-level under `R9`** — the accurate fact is recoverable from the FULL record, and no
action changes. `.goals/plans/harness-repo-split.plan.md:145-147`, step 15: "…**本步点名的四件在 R1
随 `HD-39` 全部删除**（FULL `L-6`）". The finding that named step 15's four artifacts is `L-5`;
`L-6` is the line count, cited correctly two steps above at step 11. The commit title says `L5`.

### F-5 — the Resume pointer, edited by this repair, still says the FULL is owed

**Low.**

`.goals/plans/harness-repo-split.plan.md`, §Resume pointer: "当前指针（2026-08-15）：**R1 步骤
10–13b 已落地，欠步骤 14 的 FULL**。四个 commit：…", and step 14's checkbox is still `[ ]`. The FULL
occurred and its record landed at `0792a89`, before this repair; `22264b5` edited the last
paragraph of that very block and left the opening sentence and the commit list standing. The plan
names this pointer as the cold-start entry, so a fresh session reads the round as owing a FULL that
`E9` would not grant it a second of.

Second half of the same block: "**另欠指令层一次独立 read**——`a8af54c` 的 `HD-42` 枚举编辑与
`e4ffa2b` 的 `L-1` 两笔自由通道字节都骑在它上面" now under-counts — `22264b5` is a third write to
`EXECUTION.md`. That half is self-correcting and I flag it only for completeness: `E10`'s read is
per-member digest, and the blob moved `e56b1a3d` → `9f80e728`, so any read covering the member
covers all three writes.

---

## 5. Permanent boundaries

**`E2` — frozen bytes.** Untouched, and identical across both repositories:

```
Document-Work-Assurance-Contract-v3.md   b2dbdf75   base = tip = new repo
…-supersession-1.md                      68031fa2   base = tip = new repo
…-supersession-2.md                      e1a2f26b   base = tip = new repo
schema/document-assurance-v3/            15 files;  git diff base..tip -- <pack> = 0 changes
```

**`E10` — instruction layer, nine members.** Eight `SAME`; one `CHANGED`,
`EXECUTION.md` `e56b1a3d` → `9f80e728` (the `L-3` application). All nine are byte-identical between
the caller tip and the new repository. No unauthorized layer write. The `L-3` edit is a
replacement inside a measurement narrative — it adds no clause and changes what no rule requires —
so it does not trip `E10`'s design test and does not open a round. It still owes the layer's
independent read; see `F-5` and `O-4`.

**`E9` — budget.** One FULL (record `0792a89`), one user-approved fix (`22264b5`), this VERIFY. I
checked the riders-only classification of `e6b4d2c` rather than accepting it: the 2026-08-04 ruling
in `HARNESS-LEDGER.md` states 判据 = 改的是不是被评审的 work product, and `HARNESS-RIDERS.md` is a
governance register, not R1's work product — so the classification holds, and splitting it out of
the fix commit rather than bundling it errs in the conservative direction. Nothing in the range
exceeds the cap.

**`E8` — git.** Two new commits, no amend evidence, six explicit paths all inside R1's surfaces,
titles `V3-SPLIT-R1-…-v1` naming round and kind, dense bodies, no trailers, branch has no upstream
so nothing was pushed.

**`E12` / freeze window.** The marker names exactly this range; `HEAD` == tip; worktree clean.

---

## 6. Observations

- **O-1 — the fix commit's title omits `L-2`.** It reads `FIX-B1-L1-L3-L4-L5-L6`, and the same
  commit also discharges `L-2` (the dead import), documented in the body and visible in the diff.
  `E8` asks the title to name the round and the commit's kind, not its findings, so nothing is
  breached — noted because a reader auditing discharge by title would score `L-2` unfixed.

- **O-2 — the `L-3` replacement is scoped but still unmeasured.** "these five legs have only gained
  tests since" is narrower than "test counts only grow", which is what `HD-41` ② asked for. The
  endpoints support it (29≥29, 80≥80, 39≥32, 58≥58, 701≥556); the path between the p5a-shells
  revision and now is **`UNVERIFIABLE`** from anything I ran and no command established it. Nothing
  turns on it — the next sentence tells the reader to re-run — so this is an observation, not a
  finding.

- **O-3 — `HARNESS-LEDGER.md`'s split-batch row is stale.** It still reads "**执行零进度：171 文件
  一个没删、新仓不存在**" and "R1 开轮前三件", which R1's own commits falsified. Outside the range
  and outside the repair; ledger fixes do not consume `E9` and this is the closeout's to make.
  Named only so the closeout does not skip it.

- **O-4 — the layer write's channel is again unstated.** `22264b5` writes an `E10` member and its
  body does not name the channel it travels (the user-approved fix leg, or `E10`'s free channel for
  a low whose record names the content) nor the read it owes. This is the same shape the FULL
  raised as `O-1` for `a8af54c` and which the round recorded as 未采取行动. No rule is breached —
  nothing relies on the new text, so `E10`'s deferral branch is not engaged — but two consecutive
  layer writes now sit there with no stated channel.

- **O-5 — a shape, reported not concluded (`R5`).** R1's two blockers and two of my four findings
  are one defect class: a factual claim about the delivery written into a delivered document
  without running the command that could falsify it. The correction of that class in the
  README/manifest honesty passages has now itself introduced a new instance of it (`F-1`, `F-2`).
  Whether that calls for machinery, a checklist item, or nothing at all is the user's question, not
  mine; my subject is the text that is there.

---

## 7. Coverage and ceilings (`R4`)

**Read in full**: both commit bodies in the range and both in `D:/do-the-work`;
`CONSTRUCTION-CHECKLIST.md`; `v3-review-full-e608204.md`; `split-travel-manifest.md`;
`HARNESS-LEDGER.md`; `HARNESS-RIDERS.md` header and the `SCC` / `E10-sync` rows; `HD-39`, `HD-41`,
`HD-42`; the plan's R1/R2 sections, Resume pointer and Acceptance; `D:/do-the-work/README.md`; the
diffs of all six changed files.

**Sampled**: `HARNESS-DECISIONS.md` — `§live` headings plus three entries end to end, not the whole
file; `EXECUTION.md` around the edited passage, not end to end; the three hook docstrings and
`layer_path_check`'s `LAYER`; `rsc.py` by diff plus targeted greps.

**Probed, not read**: the 254 travelled files — compared by blob id, which is stronger than reading,
and not read; the 171 deleted — I re-derived the count and `HD-39`'s enumeration, and did not read
their contents.

**Executed**: the six battery legs and `repo-audit` at the tip; in a throwaway clone of the new
repository, its full suite twice (once grouped by failure cause), `test_precommit_checks`, the
`LAYER` resolution probe, and two guard mutations with a negative control.

**Ceilings.**
- The new-repository measurements were taken in a **clone**, to leave the subject worktree
  untouched. The clone is byte-identical and sits at the same directory depth, so `RS_ROOT` /
  `REPO_ROOT` resolve identically; the only difference is the absolute path string, which nothing
  I exercised reads. The 24/677 split reproduces the round's own figure exactly, which is
  independent corroboration that the clone behaves as the original — but the equivalence is
  argued, not proved.
- The mutations prove those two guards bind on the newly-added-path class **in the new repository's
  layout** — the precise claim the `B-1` repair turns on. They do not show their force is
  sufficient for anything else, and a VERIFY is never a re-certification (`R4`).
- Whether `.harness/review-pending.json` was written by a real `rsc v3 dispatch` invocation is a
  process claim: contents verified, the command **`UNVERIFIABLE`** from my side.
- The user's 2026-08-15 "A" approval of the fix scope is visible only as executor prose in
  `22264b5`'s body. `R7`: ceiling stated, nothing in the repository contradicts it.
- `E9`'s "branch takes no commit but the record" is verified as of this read; it cannot be verified
  for the interval after I stop.
- **Not concluded, by `R5`**: whether the four instrument fixtures (`assurance/test/` goldens,
  `tests/fixtures/expected-*-prompt.txt`) should join the travel set; whether the three
  caller-coupled governance tests should be excluded in the new repository; and `O-5`'s question.

---

## 8. What holds

`B-1` is discharged in substance, and independently: nine `LAYER` members resolve in the new
repository, both path guards block a staged unresolvable path with a clean negative control,
`review_freeze_check` is inert only because `.harness/` is the caller's under `HD-33`,
`test_precommit_checks` is 42 passed, and the scheduling correction — the three-mirror edit falls
due in the same commit as R2's re-rooting — is stated at all three sites, with the delivery
exclusion deleted. `B-2` is discharged in both repositories with `HD-39` named. `L-1`, `L-2`,
`L-3`, `L-5` and `L-6` are discharged and each of their load-bearing numbers re-derives: 171
deletions, `generated/stages/README.md` outside `HD-39`'s enumeration, 856 → 686 → 685, both named
CLI test files gone. The battery is six-for-six green at the tip and every reported tally
reproduces exactly. `E2`'s frozen bytes are untouched in both repositories, `E10`'s nine members
are in sync across them, 254 of 255 blobs are byte-identical, and `E9`'s cap is intact with the
fix leg spent exactly once.
