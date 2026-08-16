# VERIFY — split batch R2 repair, `8896ede..af93d49`

**Verdict: `REVIEWED_NO_BLOCKER`.**

Every accepted finding landed, and the two that carry force — the identity assertion of `L-1`
and the ledger clause of `B-2` — I proved rather than read. The verbatim-`main()` fork that
passed all five old tests now fails the new assertion and only it; the ledger line is true
clause by clause at the tip. `L-2`, `O-4`, `O-5` reproduce exactly as written. Nothing touched
`E2`'s frozen surface or the `E10` layer, and the six-leg battery is green at the tip.

The repair's weakness is entirely in one place: **the prose that measures**. `B-1`'s blocker was
scan evidence that could not have produced what it claimed. Its replacement has the same
property — neither pasted count reproduces from the command it is credited to (`V-1`). Two of
the round's three self-corrections are themselves wrong: the 「仅剩」 count was corrected to the
wrong revision's number (`V-2`), and the divergence count was corrected from a right answer to a
wrong one (`V-3` — the error originates in the FULL's own `O-3`, which I overturn). And one of
the seven plans bucketed as closed history is not closed, and the line at issue in it is a live
round-discipline instruction naming a deleted command (`V-5`) — the residue of `B-1` itself.

The code is clean. The record of the code is where every finding is.

Findings: 5, all non-blocking (a VERIFY has no `CHANGES_REQUIRED` and I do not inflate one —
`R3`). Routing question raised, not decided (`R5`, `R10`).

---

## 1. Subject, re-derived

Everything below is re-derived from the repository; no reported figure was accepted, the FULL's
included (`R2`).

| | |
|---|---|
| Range | `8896ede521f9028b61d6b8a57f07cf64456723ae..af93d4979e805e43aa189ac79180025824009595` |
| Branch / worktree | `document-work-assurance-v3` @ `D:/Thesis-stage-control-refactor`; `HEAD` == range tip. `git status --porcelain` empty at entry and at exit |
| Commits | 3, author-date == committer-date on all three (no amend/rebase evidence): `2ba4369` `V3-SPLIT-R2-FIX-B1-L1-L2-O3-O4-O5-v1` 18:53:19 +1000 · `df75fc9` `V3-SPLIT-R2-LEDGER-B2-RIDER-O2-v1` 19:20:53 · `af93d49` `V3-SPLIT-R2-CHORE-SETTINGS-2-v1` 19:21:58 |
| Base | `8896ede` `V3-REVIEW-RECORD-SPLIT-R2-297bb2b-v1`, the FULL's record commit. A VERIFY range starting at the record commit is what `E9` requires ("has occurred only when its record's commit lands") |
| Round | Split batch **R2**, repair leg. Prior FULL: `v3-review-full-297bb2b.md`, subject `4546835..297bb2b`, `CHANGES_REQUIRED`, 2 blocker / 3 low / 5 observation |
| Freeze marker | `.harness/review-pending.json` names this exact range, `dispatched_at 2026-08-16T09:22:05+00:00`; tip commits 09:21:58Z, i.e. dispatch 7s later. `.harness/` is gitignored (`.gitignore:19`), so the marker is untracked and the clean status is consistent. No commit on the branch since dispatch |
| Budget (`E9`) | Correct and exhausted. Over `migration/document-work-assurance-v3/`, the only SPLIT-R2 record is `v3-review-full-297bb2b.md`; no record names `af93d49`, `8896ede`, `2ba4369` or `df75fc9`. So: one FULL (spent), `2ba4369` = the one user-approved fix (spent), this VERIFY = the third leg. `df75fc9` claims the `HD-23` / 2026-08-04 ledger-riders carve-out; the substance holds, one supporting clause in its body does not — §5 `V-4a` |
| Authorization | User's 「全批」 approval of 2026-08-16 covering both blockers + `L-1`/`L-2`/`O-3`/`O-4`/`O-5`, recorded in `2ba4369`'s body. Chat in origin but committed, so not an `R2` chat-only finding — with the ceiling that it is the executor's own record of the user's words (`R4`). `HD-23` + the 2026-08-04 ruling for the free commit; `HD-37` for the rider row; `HD-34`/`HD-40` inherited from the FULL |
| Paths | 10, all **M**, 0 A, 0 D — classified by hand below |
| Out-of-repo | `D:/do-the-work` @ `a97d578`, 260 tracked, clean — unchanged since the FULL measured it, consistent with the plan deferring resync until after this VERIFY |

Paths by hand, against what the fix was authorized to touch:

```
M .goals/plans/harness-repo-split.plan.md                   B-1(1) Acceptance + step 17/17b + pointer
M .goals/plans/harness-deletion-first-stabilization.plan.md B-1(2) :22, :168 rewritten
M .goals/plans/research-agent-dev-p3corr-p4.plan.md         B-1(2) :34, :99 rewritten
M ResearchSystem/HARNESS-LEDGER.md                          B-2                       (df75fc9)
M ResearchSystem/HARNESS-RIDERS.md                          O-2 -> rider battery-travel (df75fc9)
M ResearchSystem/document-harness/split-travel-manifest.md  O-4 paragraph
M .../tests/document_harness/test_cli_entry.py              L-1 +1 assertion, +load_entry, docstring
M .../tests/document_harness/test_precommit_checks.py       O-5 label + docstring
M .../tests/document_harness_review/test_fix_round_locks.py L-2 comment
M .claude/settings.local.json                               chore, disclosed          (af93d49)
```

Every path traces to an accepted finding except the last, which `af93d49` declares out of the
work product and explains. Its claim 「零 harness 字节、零 work-product 字节」 is verified: the
whole diff is two added Bash-permission strings.

**Permanent boundaries, all clear.** `E2`: the three frozen contract blobs are byte-identical at
base and tip and match the ids `E2` names — `b2dbdf75`, `68031fa2`, `e1a2f26b`;
`git diff --name-only 8896ede af93d49 -- ResearchSystem/schema/document-assurance-v3/` returns
zero lines, so `HD-20` does not bite. `E10`: the same command over all nine member paths returns
zero lines — no amendment, no read owed by this range. `E8`: three new commits, no amend, single
dense `V3-…-v1` titles, one paragraph, no trailers; `origin/main..HEAD` is 712, i.e. nothing
pushed. Ledger cap: 115 lines, `Thesis/Work/Tooling/ledger_cap_check.py` exit 0 (declared limit
120, `HARNESS-POLICY.md:22`). `repo-audit.py` exit 0.

---

## 2. The repair, checked (`R3`: this leads)

### `L-1` — the identity assertion binds, and I made it fail the real defect

`E4`/`R8`, mutation-tested by me: baseline copies to the scratchpad, sha256 recorded, restore by
copy, never `git checkout --`. Baselines `6c84c6a9` `dtw.py` / `25c22146` `do-the-work.py` /
`241303ac` `cli.py` / `4157cae2` `paths.py`; all verified equal after each restore, and
`git status --porcelain` empty at exit.

| mutation | result |
|---|---|
| `dtw.py` replaced by a **fork carrying its own verbatim copy of `main()`** — the exact shape the FULL's `L-1` proved invisible | **1 red, and only the new one**: `TheTwoNames::test_each_name_is_the_same_entry`, `AssertionError: <function main at 0x…3E0> is not <function main at 0x…880>`. The other five, including both help-comparison tests, stay green — reproducing the FULL's finding and closing it in the same run |
| baseline (genuine shim) | 6 passed |
| neuter `core.quotepath=off` in `TrackedPaths.from_index` | `test_an_ascii_directory_holding_one_resolves` red with the real message, not a crash: `pre-commit BLOCKED: newly written text names a repository path that exists nowhere: … ResearchSystem/notes/`. This is the exact string the new `O-5` docstring asserts |

`E5` holds and the fix is what makes it hold. The old property was "the two entries' help output
currently agrees", where each entry's expectation was the *other entry's* output — the dependence
`E5` warns about. `assertIs(load_entry(script).main, cli.main)` takes its expectation from the
canonical module, which is not the thing guarded (the shim). `E6` holds too: the FULL supplied the
bytes, so this is a finding-named literal, not machinery invented to close a finding — one
assertion plus a nine-line `importlib` helper made necessary only because `do-the-work.py` is not
an importable module name.

### `L-2` — the corrected warrant is accurate

Measured, not read: `test_dispatch.py` contains **zero** occurrences of `subprocess`, `dtw`,
`do-the-work` or `cli`, and imports `from rsclib.document_harness import dispatch as D` — it
drives the module in-process. `test_dispatch_freeze_marker.py:39` and
`test_review_cli_v2_subject.py:42` both run `[sys.executable, "dtw.py", …]`. Two suites, not
three, and the new comment says exactly that plus why the third does not count.

### `B-2` — the ledger line is true clause by clause at the tip

`HARNESS-LEDGER.md:98`. 甲 ruled 2026-08-16 ✓ (plan + `0643229`/`297bb2b` bodies). Re-rooting
deferred past R3, `E10-sync` therefore not due ✓ (plan §R2). Six commands are now the harness's
own CLI ✓ — `python ResearchSystem/tooling/dtw.py --help` prints
`{governance-scan,status,flow,dispatch,disposition,review}`. `rsc.py` 只剩 `inventory`/`compile`
✓ — `rsc.py --help` prints `{inventory,compile}` and `grep -cE "v3|document_harness" rsc.py`
returns 0. FULL `CHANGES_REQUIRED` → 全批修腿已落，欠一次 targeted VERIFY ✓ (true until this
record commits). CLOSED is not pre-written and is left to R4 ✓ — which is what the FULL asked for.

### `B-1` (1) — the Acceptance rewrite is substantive, and both commands it names exist

The line no longer asks R3/R4 to run a deleted command, and it is more than a rename, as the FULL
required: it now demands the invocation go **through the submodule's own entry**, which is the
form `HD-34` leaves available. Both claims in the replacement text check out —
`rsc.py` carries only `inventory`/`compile` (above), and the commands it tells a future round to
run are real: `dtw.py dispatch --help` shows `(--subject | --range | --read) [--repo-root]`,
`dtw.py status --help` shows `--state`. The same is true of the other four rewritten lines:
`harness-deletion-first-stabilization.plan.md:22`/`:168` and
`research-agent-dev-p3corr-p4.plan.md:34`/`:99` now name `dtw`, and `:34`'s subcommand list gained
`dispatch`, which the original had omitted.

### `B-1` (2) — the dispositions are complete; the evidence for them is not

I re-derived both live sets at the tip rather than taking the counts.

Sweep A live set (`git grep -nE "rsc v3"` minus the four immutable families) = **22** lines, and
every one has a disposition in `2ba4369`'s body: `e2-verb-e10-pin` ×1 · `harness-digest-narrowing`
×5 · `harness-issue-redemption-batch` ×1 · `harness-layer-incorporation-round` ×3 ·
`harness-memory-lessons-integration` ×2 · `harness-phase-c0-m8-m10` ×3 ·
`harness-record-layer-and-repo-split` ×2 · `split-design.md:54` · `cli.py:14` ·
`repo-audit.py:299` · plus 2 in `harness-repo-split.plan.md` that are the round's own new
explanatory prose. Sweep B live set = **10** lines, likewise all covered.

The nine `assurance/shadow/` sites are correctly disposed — declared, not edited, per the user's
2026-08-16 ruling. I confirmed the supporting shape: the tree's last commit is `2687d8c`
(2026-07-28), and outside the immutable families nothing points at it as runnable (the only live
mentions are `split-travel-manifest.md:131`, which lists it as not travelling, and old plans
referring to the unrelated `generated/document-assurance/shadow/**`).

So the obligation `split-design.md` §1 states — 「既有文档里的 `rsc v3 <cmd>` 写法随之全部改写」 —
is discharged in substance, with one exception (`V-5`). What fails is the record of how it was
established: `V-1`, `V-2`.

### `O-4` — the undeclared dependency is real and the paragraph's claim holds

`ResearchSystem/tooling/rsclib/__init__.py` is **absent** from `D:/do-the-work@a97d578` (the
travel prefix stops at `rsclib/document_harness`), and it defines `SCHEMA_VERSION = 1` — so the
silent-failure mode the paragraph describes is not hypothetical. Today's claim holds: over every
travel prefix, `from rsclib import` / `import rsclib` (bare) / `SCHEMA_VERSION` return zero hits.
One nearby line is worth stating precisely rather than as a defect —
`test_package_and_review.py:1224` does `import rsclib.document_harness.review as review_module`,
which a prefix-matching reading of 「`import rsclib` 零命中」 would flag; it is not a
counterexample, because a submodule import resolves fine under PEP 420 and only names defined in
`__init__.py` would not.

### `O-2` → rider `battery-travel` — well-formed, and it corrects the FULL

`R10` format satisfied: target named (`EXECUTION.md` tiering section), redeem-when is a touch
condition plus a deadline, source cited. `HD-37` ① — deadline 「第一个在 harness 仓内开的构造轮」
cannot be this round, which ran in the caller. `HD-37` ② — the fix is design-shaped, and the
redeem-when names a design batch, a surface that may open a round, not "any batch". Bank is 37
lines at the tip.

The row says **five** of six legs do not travel; the FULL's `O-2` said "four" while listing five.
Five is right — `run_tests.py`, `run_p4_tests.py`, `run_p5a_tests.py`,
`schema/fixtures/validate_fixtures.py` and `rsc.py` are each absent from `D:/do-the-work`, and
only the two pytest trees (28 files) travel.

### Full battery, six legs, re-run by me at the tip `af93d49`

```
run_tests.py            tests: 29   passed: 29   failed: 0        RESULT: OK
run_p4_tests.py         tests: 80   passed: 80   failed: 0        RESULT: OK
run_p5a_tests.py        tests: 39   passed: 39   failed: 0        RESULT: OK
validate_fixtures.py    cases: 58   matched: 58  unexpected: 0    RESULT: OK
python -m pytest -q     708 passed in 83.28s      (from ResearchSystem/tooling)
rsc.py compile --check  RESULT: generated output fresh; lint clean (exit 0)
```

708 is the figure `2ba4369` reports and it reproduces; 707 + 1 for the new identity assertion
checks out against the diff. But it was measured two commits ago — `V-4`.

---

## 3. Findings

### `V-1` — the replacement scan evidence does not reproduce from the commands it is credited to

**Where.** `2ba4369`'s body, the 「用对写法重扫，全仓 tracked，实测」 block.

**Ground truth.** `HD-41` ④: paste the grep output *so that whether it ran can be seen by the
reviewer on the spot*. `E3`: counts are emitted from the command that produces them or omitted.
The FULL's `B-1` minimum fix, item 2: "paste the real output".

**What I measured.** Both pasted patterns, run at every revision in the range:

| pasted command | body claims | @`2ba4369` (its own tree) | @`af93d49` (tip) | @`297bb2b` (pre-fix) |
|---|---|---|---|---|
| `git grep -nE "rsc v3"` | 141 (live 23) | 140 (live 22) | 140 (live 22) | 138 (live 23) |
| `git grep -nE '"rsc\.py", "v3"\|rsc\.py v3'` | 32 (live 17) | 20 (live 10) | 20 (live 10) | 18 (live 10) |

No revision produces 141, and none comes near 32. The FULL's own figure for the second pattern —
18 tracked lines at `297bb2b` — reproduces exactly, which is what makes 32 measurable as wrong
rather than merely different.

The breakdown is the sharper half. The body says the second sweep's live set is 「17 行，其中 6 行
是可执行代码、3 行是已冻结的 run control JSON」. Those nine lines are the `assurance/shadow/`
sites, and that command cannot see them. Negative control, in the FULL's own style:

```
$ git grep -nE '"rsc\.py", "v3"|rsc\.py v3' -- ResearchSystem/assurance/shadow
  -> exit 1, zero lines
$ git grep -ncE 'rsc\.py"?,? ?"?v3'         -- ResearchSystem/assurance/shadow
  -> 9 lines across 9 files (3 measure.py, 3 run_shadow.py, 3 control JSON)
```

The cause is the leading quote in `"rsc\.py"`: every real site writes
`…/tooling/rsc.py", "v3"`, where the character before `rsc` is `/`. And the union of *both*
pasted sweeps contains zero `assurance/shadow` lines at the tip — I checked directly.

**Why it is not a blocker.** I re-derived the live sets myself and every hit is disposed (§2), so
the obligation is discharged and this record is now the evidence for it. **Why it matters
anyway.** `B-1` was a pasted sweep that could not have produced what it claimed; the repair for
`B-1` is a pasted sweep that could not have produced what it claimed. Fixing the instance did not
touch the class — which is `E7`'s whole subject, and the same argument the FULL used against
`B-2`.

**Minimum fix.** Wherever this round's corrections land: state the actual commands with their
actual output, or drop the counts and keep the dispositions, which are the part that is true.

### `V-2` — the 「仅剩」 correction is scoped to the wrong revision

**Where.** `2ba4369`'s body 「更正两处自陈 ①」 and `harness-repo-split.plan.md` step 17b ②:
「原正文「仅剩 `split-design.md:54`」是假的绝对量词（`HD-41` ②）——**写下时即两行**，另一行
`cli.py:14`」.

**What I measured.** Re-running `0643229`'s own sweep verbatim at `0643229` — the commit whose
body wrote the sentence:

```
$ git grep -n "rsc v3" 0643229 -- ResearchSystem ':!ResearchSystem/migration' \
    ':!ResearchSystem/assurance/runs' ':!ResearchSystem/document-harness/journal' \
    ':!ResearchSystem/HARNESS-LEDGER-archive.md'
  ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md:129
  ResearchSystem/document-harness/README.md:34
  ResearchSystem/document-harness/split-design.md:54
  ResearchSystem/tooling/rsclib/document_harness/cli.py:14
```

**Four**, not two. The first two were renamed by the *next* commit `8d137da`. Two is the count at
the tip `297bb2b`, which is where the FULL measured — the correction adopted the FULL's revision
instead of the one the sentence was written on. `HD-41` ③ is the clause the correction was issued
under: a counted assertion states its revision.

**Minimum fix.** One clause: 「写下时（`0643229`）为四行；`8d137da` 改掉其中两条指令层写法后，在
tip `297bb2b` 上为两行」.

### `V-3` — the `O-3` correction replaces a right count with a wrong one, and the error starts in the FULL

**Where.** `harness-repo-split.plan.md` step 17b ③ and the resume pointer; `2ba4369`'s body
「更正两处自陈 ②」. Source of the error: the FULL's `O-3`, which I overturn.

**What I measured.** Comparing `D:/do-the-work@a97d578` against the caller at the round's **base**
`4546835`, path for path: 0 of the new repo's 260 paths are absent from the caller, and **six**
paths exist in both with differing blobs:

```
README.md
ResearchSystem/HARNESS-DECISIONS.md
ResearchSystem/HARNESS-DECISIONS-archive.md
ResearchSystem/HARNESS-RIDERS.md
ResearchSystem/tooling/hooks/candidate_path_check.py
ResearchSystem/tooling/tests/document_harness/test_precommit_checks.py
```

Blob proof for the two the correction disputes, at the base, before this round wrote a byte:

```
ResearchSystem/HARNESS-RIDERS.md          caller@4546835 e598aeeb   do-the-work@a97d578 d5f2b96c
  (the one differing row: rider `a10-provenance`, present in the caller, absent in the new repo)
ResearchSystem/.../test_precommit_checks.py caller@4546835 8bf90f2e  do-the-work@a97d578 91a7b9e8
  (two occurrences of "ResearchSystem/HARNESS-DECISIONS-archive.md")
```

So 「另两个（`HARNESS-RIDERS.md` · `test_precommit_checks.py`）是被本轮碰到才进集合的」 is false:
both already diverged at the base. The superseded text — 「5 个文件：三本治理登记 +
`candidate_path_check.py` + `test_precommit_checks.py`」 — is exactly those six minus `README.md`,
i.e. it was **correct**, `README.md` being the new repository's own document, which must not be
resynced from the caller.

The FULL's `O-3` is where this comes from: it measured divergence against the **tip** (18 blobs,
which I reproduce), partitioned that set into "this round's own bytes" and "pre-round divergence",
and then asserted causation — "in the set only because this round also touched them" — without
measuring against the base. The partition-at-the-tip is sound; the causal claim is not. `R2` says
I re-derive every number and accept no reported figure, and my predecessor's figures are not
exempt.

**Harm today: zero.** The pointer's instruction is 「本轮字节 + 轮前分叉的 3 个文件」, and both
disputed files are in 本轮字节 — each was touched in the FULL's range *and* in this one — so the
union still covers all five paths a resync must carry.

**Minimum fix.** Restore the count to five at a declared base, or state six and mark `README.md`
excluded with its reason. Either way name the revision the comparison is against.

### `V-4` — the tip's battery is again two commits older than the tip

`2ba4369` measured the six legs on its own tree. `df75fc9` then wrote `HARNESS-LEDGER.md` and
`HARNESS-RIDERS.md` and `af93d49` wrote `.claude/settings.local.json`; neither records a battery.
`HARNESS-RIDERS.md` is a path that `hooks/candidate_path_check.py:70` enumerates and
`test_precommit_checks.py:350`/`:366` pin, so `EXECUTION.md:324`'s file-worded exception — "a doc
file that code enumerates or tests pin … treat the batch as tooling-touching" — reads onto it.
`E3` says re-run immediately before the claim. I re-ran all six at the tip and every figure
reproduces (§2), so the harm is again zero and the finding is the discipline.

This is `L-3` recurring inside the same round, and, as the FULL said of `L-3`, the shape is the
one rider `tier-file-vs-clause` already banks — the section says file, the executor reads clause,
and the tests pin the path string rather than the file's content. Reported for disposition, not as
a fresh problem.

**`V-4a`, the same shape in `df75fc9`'s own warrant.** Its body justifies the `HD-23` /
2026-08-04 carve-out with 「两个文件都在本轮 range 之外」. Measured,
`git diff --name-only 4546835 297bb2b` lists `ResearchSystem/HARNESS-RIDERS.md` — it was inside
the reviewed range; only `HARNESS-LEDGER.md` was outside. The carve-out itself still stands,
because the operative test is 「改的是不是被评审的 work product」 and the row added is new content,
not a reviewed byte — which is exactly what the body's own next clause says
(「bank 那张表本轮只被删过两行」). So the accurate fact sits beside the false one; `R9`'s recovery
test is met and no permission changes. Recorded because `E9` warns that every recorded escape
from the cap was a renamed round, and a warrant is the wrong place for a clause that does not
survive `git diff`.

### `V-5` — one plan bucketed as closed history is not closed, and its hit is a live instruction

**Where.** `.goals/plans/harness-memory-lessons-integration.plan.md:42`.

**Ground truth.** The FULL's `B-1` minimum fix, item 2: give every remaining live-surface hit a
disposition — "rewrite, or 'history, stays'". `2ba4369` put this file in the
「七份**已 closed/done** 的 plan」 bucket.

**What I measured.** Six of the seven are closed by their own headers and carry zero open
checkboxes. This one is not:

```
:6   - **status**: Step 0–6 全部闭合 … **剩 Step 7：回父 plan Step 5（Phase C1）**
:64  - [ ] 7. 过读后回父 plan Step 5（Phase C1）。
:174 - [ ] **未清**：`079361f` 的指令层字节尚未过独立读（`E10`）… Phase C1 开轮前要清
:42  - **轮次纪律**：preview card（E11）→ 用户确认 → 改动 → suite + repo-audit + 冻结面复核
     → commit `V3-<轮名>-v1` … → `python ResearchSystem/tooling/rsc.py v3 dispatch
     --range <base>..<tip>` → **用户路由**到独立 session。
```

`:42` is the round discipline a session picking up Step 7 would follow, and it names a command
this round deleted. It is the same sentence, in the same shape, as
`harness-deletion-first-stabilization.plan.md:22` — which this round **did** rewrite, on the
reasoning that a `planned` plan's Roles section is 「可被捡起执行的指令」. The only difference
between the two is which bucket the executor put them in. The file's other two hits (`:81`,
`:157`) are a completed atom-migration table and are genuinely history.

I checked the one other plan with open boxes so as not to overstate: `harness-digest-narrowing`
has two unchecked steps (`:179`, `:180`) whose text names the old command, but its header declares
the round CLOSED with both review legs recorded at `:226`, and the range they name (`e8ca95c..`)
is dead. "History, stays" is defensible there.

**Minimum fix.** One line, matching the two the round already wrote:
`harness-memory-lessons-integration.plan.md:42`,
`python ResearchSystem/tooling/rsc.py v3 dispatch --range <base>..<tip>` →
`python ResearchSystem/tooling/dtw.py dispatch --range <base>..<tip>`.

**Routing is not mine to settle (`R5`).** `E9`'s fix leg for R2 is spent, and the file is a
caller-side plan, so `E10`'s free channel does not reach it (`.goals/plans/` is not one of the nine
member paths) and `R9` does not either (the fix changes what a session does). That leaves the
bank or the user's spend-the-leg call under `R10`'s closeout clause. The natural touch surface is
**R3**, which rewires the caller side and will be in these files anyway.

---

## 4. Observations

**`O-1'` — `E8`'s kind vocabulary is being treated as open.** Two of three commits name kinds
outside `E8`'s list: `chore` (`af93d49`, following `4546835`) and `ledger/riders-only`
(`df75fc9`). The clause's stated purpose — "so the review side can attribute it without asking" —
was met; I attributed all three without asking. Recording it because this is the second round in
which the enumeration is extended, and `CONSTRUCTION-CHECKLIST`'s own banner says a silence rides
the next batch under `R9` rather than opening a round. Whether the list is closed is the user's
question.

**`O-2'` — where this round's error rate actually sits.** Four of my five findings (`V-1`, `V-2`,
`V-3`, `V-4a`) are defects in *prose that reports a measurement*, and three of them are
corrections that are themselves wrong. Zero are in code, schemas, tests or guards: the identity
assertion, the label, the comment and the manifest paragraph all say exactly what is true, and
every guard I mutated bound the real defect. `R5` says the shape is mine to report and the
conclusion is the user's, so: the failure mode this harness keeps paying for is not the work, it
is the account of the work, and the accounts that fail most are the ones written *to correct a
previous account*. `V-3` is the sharpest instance — a correct sentence was replaced by an
incorrect one, on a reviewer's figure that was itself unmeasured.

---

## 5. What I read, and what I could not verify (`R4`)

**In full:** `CONSTRUCTION-CHECKLIST.md` and the review-contract stub that names it;
`v3-review-full-297bb2b.md`; `HARNESS-DECISIONS.md` (§live and §implemented) and the `HD-` index
of the archive; `HARNESS-LEDGER.md`; `HARNESS-RIDERS.md`; `split-travel-manifest.md`; the three
commit bodies; the whole diff of the range; `test_cli_entry.py`, `dtw.py`, `rsclib/__init__.py`.

**Sampled:** `harness-repo-split.plan.md` (the R2 section, Acceptance, step 17/17b, resume
pointer — not the other ~230 lines); `EXECUTION.md` (the tiering section and battery enumeration
only); `harness-memory-lessons-integration.plan.md` (status, `:38–46`, `:78–84`, `:155–159`, the
open boxes); the six other disposed plans' headers and checkbox counts; `cli.py` around `main`
and the parser tail; `paths.py` around `from_index`; `test_precommit_checks.py` and
`test_fix_round_locks.py` around the changed regions; `HARNESS-POLICY.md` §ledger.

**Probed only:** `harness-digest-narrowing.plan.md` and the other closed plans — grepped for hits
and open boxes, not read; `HARNESS-DECISIONS-archive.md` — read `HD-20`, `HD-37` and the entry
index, nothing else.

**Executed:** all six battery legs at the tip; `repo-audit.py`; `ledger_cap_check.py`; `--help` on
`rsc.py`, `dtw.py`, `dtw.py dispatch`, `dtw.py status`; both `B-1` sweeps at four revisions plus
six pattern variants and a negative control on the shadow tree; the full blob-by-blob comparison
against `D:/do-the-work@a97d578` at both the base and the tip; three mutations with sha256-checked
restore.

**`UNVERIFIABLE`, not folded into supported:**

- `E11`'s preview card for the fix leg. Nothing in the repository records one, as was true of the
  FULL. `R7`: stated as a ceiling, not a block.
- The user's 「全批」 approval and the 2026-08-16 ruling not to touch `assurance/shadow/`. Both are
  recorded in commit bodies, so not chat-only under `R2`, but both are the executor's own record
  of the user's words and nothing else in the repository corroborates them.
- Whether `df75fc9` or `af93d49` was preceded by a battery run. Neither body records one; I
  established only that the figures reproduce at the tip, which is a different fact (`V-4`).
- The 「新仓 21 个 `.py` 含 110 处硬编码 `ResearchSystem/`」 support for the 甲 ruling — a tree
  outside every range, not re-derived, and the ruling is the user's regardless. Carried forward
  from the FULL unchanged.
- Freshness of context. A process claim; marked, not verified.

**Worktree state on exit.** Three mutations, each restored by copy from sha256-checked scratchpad
baselines, never `git checkout --`; all four touched files verified equal to their baselines
afterwards. `git status --porcelain` is **empty**, `HEAD` == `af93d49`. Unlike the FULL, this
session left no line in `.claude/settings.local.json` — the permissions it needed were already
granted by `af93d49`.
