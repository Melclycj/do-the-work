# VERIFY — `c05f478cf5c0c9dc89514a238dea2b6d241c24f2..080621aea62fc834e8b92d55c3f191d266be01c7` (batch B, round R3)

**Verdict: `REVIEWED_NO_BLOCKER`.** One finding (`V-1`), three observations.

The repair discharges every accepted finding at the location the FULL named. `B-1`'s
minimum fix was a corrected account plus the three missing commands: the commands were run
and their output is in journal §7, and I re-ran the whole battery myself at the tip — all
eight legs green, every figure in §7 reproducing (29 · 80 · 39 · 58 · 701 · 39 · 20 ·
`compile --check` exit 0). `L-1`, `L-2` and `L-3` landed as supplied bytes or their exact
content, and each one's *claim* checks out independently: `HARNESS-POLICY.md` §3 really is
the declaration home the moved script now cites; `dispatch` really is the only one of the
six `rsc v3` subcommands whose handler writes; `HD-25` really does carry the closed-run
clause and `HD-28` really does not. No work product changed except one docstring line, and
the guard behind it still fires. `E2`, `E10` and the round's declared boundary are intact.

`V-1` is what the repair did **not** reach. Its own commit body names the root cause as a
false sentence — `tests/run_tests.py` covering P2/P4/P5A goldens plus schema fixtures in one
script — and that sentence is still live and unmarked in two files: the plan's own step 7
(the copy-source, in a file this commit edited elsewhere) and the `tier-scope` rider row,
which is the text the next tooling-touching batch is obliged to read at exactly the moment
it picks its battery legs. The reported instance is fixed; the class's live instances are not.

## 1. Subject, re-derived (`R2`)

Handed a range and nothing else. Round, budget, authorization, boundary and every number
below are derived here; nothing is taken from the commit body, the plan, the journal or the
ledger.

```
$ git rev-parse HEAD                  -> 080621aea62fc834e8b92d55c3f191d266be01c7
$ git status --porcelain              -> (empty)
$ git log --oneline c05f478..080621a  -> 080621a V3-B-R3-FIX-v1   (one commit)
$ cat .harness/review-pending.json
  {"subject": "c05f478c…..080621ae…", "dispatched_at": "2026-08-12T14:34:28+00:00"}
```

HEAD equals the range tip and the tree is clean, so worktree reads are reads of the subject.
Dispatch (14:34:28Z = 00:34:28+10:00) post-dates the tip commit (00:34:12+10:00) by 16
seconds and the branch has taken no commit since — this record is the first it admits (`E9`).

**Round and budget.** `git log` on the branch, back from the tip: `c7e0ba0` (candidate) →
`c05f478` (FULL record, verdict `CHANGES_REQUIRED`) → `080621a` (this subject). R3's FULL
has therefore validly occurred, so by `E9`'s test this commit is the round's one fix — not a
pre-submission correction — and it obliges exactly this targeted VERIFY. Budget after this
record: spent. R1 and R2 are closed chains (`e9166d2`…`0c02a3c`; `b75f5b3`…`1d6f3c4`) and do
not bear on it.

**Authorization, as visible in the repository.** `HD-35` (`§live`) signs `io-design.md` v1 as
the execution basis; `HD-31` (now `§implemented`) is the per-clause warrant; the FULL record
`c05f478` is the obligation this commit answers, and it is committed. The user's fix approval
of 2026-08-13 is chat-only; journal §7 and the plan's resume pointer transcribe it, so the
load-bearing content is in the repository even though the rendering is not (`R7`: ceiling
stated, not a block).

**Changed paths, classified by hand** (5 entries; `git diff --name-status c05f478 080621a`):

| path | class | in the approved fix boundary? |
|---|---|---|
| `Thesis/Work/Tooling/ledger_cap_check.py` | work product (1 docstring line) | yes — `L-1`'s supplied bytes |
| `ResearchSystem/HARNESS-POLICY.md` | caller policy (non-member, self-declared) | yes — `L-2` |
| `ResearchSystem/HARNESS-DECISIONS.md` | decision register | yes — `L-3`, one of its two named places |
| `.goals/plans/harness-batch-b.plan.md` | record family | yes — `L-3`'s other place + `B-1`'s step 12 |
| `ResearchSystem/document-harness/journal/batch-b-2026-08-11.md` | record family | yes — `B-1`'s output record (new §7) |

Nothing outside the accepted findings; no path added, deleted or renamed.

**`E2`.** `git diff --name-only c05f478 080621a -- ResearchSystem/schema/ ResearchSystem/contract/`
returns nothing. The pack is still 15 files, and at the tip contract `b2dbdf75…`,
supersession-1 `68031fa2…`, supersession-2 `e1a2f26b…` are unchanged.

**`E10`.** No member changed: `git diff --name-only` over `document-harness/` and `migration/`
returns only the journal, which is not a member. All nine member blobs at the tip —
`44d622b9` / `54dfef83` / `8bbd330f` / `3350bfac` / `17ff31bb` / `52a97a48` / `68031fa2` /
`e1a2f26b` / `09aa8699` — differ from the pre-round set in member 2 alone, which is
`c7e0ba0`'s README subtraction riding the deferral channel. That debt is untouched by the
repair, was not owed by it, and still rides the next read of this layer (`O-3`).

## 2. What I read, and how (`R4`)

**In full:** `CONSTRUCTION-CHECKLIST.md` (standing instructions, this session's first read);
`v3-harness-review-contract.md` (the stub that routes to it); the complete diff of the range;
`v3-review-full-c7e0ba0.md`; `HARNESS-POLICY.md`; `Thesis/Work/Tooling/ledger_cap_check.py`;
journal §7; `HARNESS-LEDGER.md`; `HARNESS-DECISIONS.md` `§live` inventory plus the `HD-23`,
`HD-25`, `HD-28` and `HD-31` entries; the plan's steps 7, 11, 12 and resume pointer.
**Sampled at the places the change touches:** `EXECUTION.md` §Regression-battery tiering
(305-348); `run_tests.py` docstring; `rsc.py` `v3` subparser and all six `_cmd_v3_*` handler
bodies; `HARNESS-RIDERS.md` `tier-scope` row; the commit bodies of `e9166d2` / `dbbec28` /
`c7e0ba0`.
**Probed only:** the rest of `HARNESS-DECISIONS.md` and `HARNESS-RIDERS.md`; `REVIEW.md`;
the journal's §1–§6.
**Marked, not verified (`R4`):** that this session is fresh context; that the executor staged
explicit paths rather than `add -A`; that the eight commands ran on the fixed tree *before*
the commit rather than at some other moment — I can only measure the tip, which I did.

## 3. Does the repair discharge the accepted findings

**`B-1` — the battery account.** The minimum fix had two halves and both landed.

*Commands.* I ran the full battery myself at the tip, and every figure journal §7 pastes
reproduces:

```
$ python ResearchSystem/tooling/tests/run_tests.py        tests: 29  passed: 29  failed: 0   exit 0
$ python ResearchSystem/tooling/tests/run_p4_tests.py     tests: 80  passed: 80  failed: 0   exit 0
$ python ResearchSystem/tooling/tests/run_p5a_tests.py    tests: 39  passed: 39  failed: 0   exit 0
$ python ResearchSystem/schema/fixtures/validate_fixtures.py
                                                  cases: 58  matched: 58  unexpected: 0      exit 0
$ python -m pytest -q            (cwd ResearchSystem/tooling)   701 passed in 108.63s        exit 0
$ python ResearchSystem/tooling/tests/harness/run_tests.py      Ran 39 tests … OK            exit 0
$ python ResearchSystem/tooling/tests/stage_control/run_tests.py
                                  stage-control deterministic matrix: 20 run, 0 failure(s), 0 error(s)  exit 0
$ python ResearchSystem/tooling/rsc.py compile --check
                                  161 md scanned, 173 live, 0 error(s) 0 warning(s)
                                  RESULT: generated output fresh; lint clean (exit 0)
```

The three legs `B-1` said had no command are green at the tip and agree with the FULL's
independent 80 / 39 / 58. Wall time differs (108.63s vs the recorded 103.16s), which is the
only figure that cannot reproduce and the only one that does not matter.

*Account.* Plan step 12 now says five commands ran and names the three legs that did not,
citing the docstring fact. I checked the fact rather than the citation: `run_tests.py`'s
docstring line 2 is `"""ResearchSystem P2 golden tests.` and its body enumerates P2 material
only. The candidate commit body is immutable under `E8` and its wrong sentence is explicitly
superseded in three places. Discharged at the locations `B-1` named — see `V-1` for the two it
did not name.

**`L-1`.** `ledger_cap_check.py:9` now reads
`Advisory and per-machine, bypassable with --no-verify (ResearchSystem/HARNESS-POLICY.md §3).`
— the supplied bytes exactly. I checked the target rather than the pointer: §3 (机械检查) names
the script at its new path and states advisory, per-machine, wired in the main repo's
`.git/hooks/pre-commit`, bypassable with `--no-verify`. The citation now lands where the
declaration is.

**`L-2`.** §1's parenthetical now reads `另有 governance-scan / review 只读，与 dispatch——
六命令中唯一写盘者：调用者 .harness/review-pending.json 冻结 marker`. Not byte-identical to the
supplied string but the same content, expanded; the file is a self-declared non-member, so
literal-byte application is not owed. I verified the assertion it now makes, because it is a
factual claim written into a policy file:

```
$ python ResearchSystem/tooling/rsc.py v3 --help
  {governance-scan,status,flow,dispatch,disposition,review}      -> six
```
and a scan of the six handler bodies by line range (`_cmd_v3_governance_scan` 231-274,
`status` 275-295, `flow` 296-332, `dispatch` 333-444, `disposition` 445-490, `review`
589-651) finds write calls in `dispatch` alone — `rsc.py:418-419`, the marker `mkdir` +
`write_text`. Five handlers, zero writes.

**`L-3`.** Both named places now rest the closed-run exclusion on `HD-25`:
`HARNESS-DECISIONS.md` HD-31's `§implemented` note and plan step 11, each also recording that
the previous `HD-28` citation was wrong and why. I checked both registers: `HD-25:185` ends
`现存八个已关闭 run 不回改。`, and `HD-28` (line 45) rules new-repository membership, not
editing. The third occurrence is in the immutable candidate body and is noted in the fix body,
as the finding allowed. See `O-1` for what the transplant costs.

**`E6`.** The repair adds no machinery: no new guard, no new rule, no derived field. Where a
finding named text as wrong, that text changed. Nothing to refuse.

## 4. Guard binding after the repair (`R8`)

The repair's only code byte is a docstring, so the binding question is not whether a new
guard fires but whether the one the repair touched still does. Mutation would answer a
question the FULL already answered at `c7e0ba0`; firing answers this one directly. In a
disposable repository (session scratchpad, nothing here touched), with the file copied from
its committed path:

| # | case | result |
|---|---|---|
| M1 | ledger staged at 121 lines | `exit 1`, whole block message printed — must-fire |
| — | ledger staged at 120 lines | `exit 0` — negative control |
| — | ledger not staged | `exit 0` — negative control |

The guard binds at its new path with its edited docstring. Repository worktree clean after
the probe (`git status --porcelain` empty; the `compile --check` leg wrote nothing).

## 5. Finding

### `V-1` — the false sentence the fix names as the root cause is still live in two files

**Location.**
`.goals/plans/harness-batch-b.plan.md:85-88` (step 7, R1's ticked battery record):
*"— **done**，五条命令覆盖六腿，全绿：`tests/run_tests.py` 29 passed（P2/P4/P5A goldens +
schema fixtures 同一脚本）· …"*
`ResearchSystem/HARNESS-RIDERS.md:33` (`tier-scope` ①): *"该批 tooling-touching，按实跑六腿
（`tests/run_tests.py` 29 · pytest 705 · `tests/harness` 39 · `tests/stage_control` 20 ·
`compile --check`），未改枚举句"* — six legs asserted over five commands.

**Ground truth.** The fix's own commit body: *"the root cause is R1's inherited false claim
that `tests/run_tests.py` covers P2/P4/P5A goldens plus schema fixtures in one script (its own
docstring says P2 only), a sentence copied across three consecutive commits."* Journal §7
repeats it as `该句为假`. The plan line above is that sentence — the only place in the
repository where the false mechanism is spelled out rather than implied — and it is
unchanged and unmarked in a file this commit edited at three other points. The rider row makes
the same arithmetic in the bank. `E7` asks for the defect class, not the reported instance;
the class's two live instances survive.

**Downstream decision that goes wrong.** The `tier-scope` ① row's own deadline is *"下一个
tooling-touching 批按枚举句自选电池腿的那一刻"* — the executor of the next tooling-touching
batch reads that row at exactly the moment of choosing battery legs, and reads there that
R1 "ran six legs" with a five-command list. The plan's step 7 is the nearest ticked precedent
for what a full battery looked like in practice. That is the copy path `B-1` predicted
(*"the next one will copy it"*), and it is still open: 80 + 39 + 58 = 177 fixture-driven cases
asserting stable error codes would again go unrun.

**Why this is a finding and not a blocker.** `B-1`'s Location named the commit body and plan
step 12; both are discharged. These two are locations the FULL did not name, so the accepted
finding is met and the round's obligation is closed — the class is not.

**Bytes.** In the plan, replace `（P2/P4/P5A goldens + schema fixtures 同一脚本）` with
`（**仅 P2 goldens**，见其 docstring）` and append one line in the file's own supersession
convention (step 6 already carries a `⚠ …已作废，勿引用` marker for falsified evidence):
`**⚠ 本步骤「五条命令覆盖六腿」的账已作废**（FULL `c7e0ba0` `B-1`）：P4 goldens / P5A goldens /`
`schema fixtures 三腿在 R1 同样没有命令；更正后的口径见步骤 12 与 journal §7。`
In `HARNESS-RIDERS.md:33`, replace `按实跑六腿（` with
`按实跑五命令（当时记作「六腿」，实为 P4/P5A goldens + schema fixtures 三腿未跑，FULL `c7e0ba0` `B-1`）（`.

**Routing, as the repository already rules it.** Both targets are outside the reviewed work
product: `HARNESS-RIDERS.md` is riders, the plan is record family (this commit's own body
classifies it so, as did the FULL's path table). The 2026-08-04 ruling recorded at
`HARNESS-LEDGER.md:78-81` — *"ledger/riders-only 的 finding 修不算 `E9` 的一次用户批准的修…
判据=改的是不是被评审的 work product"* — and its extension `HD-23` therefore appear to reach it:
the correction would consume no fix leg and owe no VERIFY. Whether the plan counts as
"ledger/riders-only" under that criterion is the user's call, not mine. Failing that, the row
is `tier-scope` ①'s own and redeems with it, deadline unchanged.

## 6. Observations

- **`O-1` — `L-3` moves the exclusion onto a clause scoped to a different cut-plane.**
  `HD-25`'s subject is the `run_all` wiring and its 切面 = *只改模板*; *"现存八个已关闭 run
  不回改"* is that decision's own cost line. R3's exclusion is about `write_scope` /
  `chk-ledger-note` in those runs — a different change borrowing the clause. The FULL offered
  this byte as one of two acceptable fixes (the other being to state the exclusion as the
  plan's own boundary decision), so the finding is discharged as supplied. Recorded because
  the split batch will have to re-derive the closed-run rule and will find it cited twice, in
  two subjects, from one clause.

- **`O-2` — the `EXECUTION.md` revert anchor is not triggered by `B-1`, and should not be read
  as triggered.** The anchor (`EXECUTION.md:341-348`) fires on *"`SPEC_GAP`s or blockers whose
  ground a skipped battery would have caught"*. `B-1` is a skipped-battery blocker, but the
  skipped legs were green at the subject — its ground is the claim, not a defect the battery
  would have caught. The tiering section is not the part to suspect here. Recorded so the
  round's shape does not later read as the anchor's first trigger.

- **`O-3` — `c7e0ba0`'s `E10` deferral debt is still outstanding at the tip.** Member 2
  (`README.md`) stands at `54dfef83` against the `dab9f71a` of the last recorded end-to-end
  read. The repair neither owed nor touched it; it rides the next read of this layer, as that
  commit's body says. Noted only so the closeout does not treat the round as read-clean.

## 7. Record and boundary conformance (`R3`, run second)

`E8`: one commit, no amend (`git reflog` shows `commit:` for `080621a`, not `commit (amend)`);
title `V3-B-R3-FIX-v1` naming the round; one dense paragraph; no trailers
(`%(trailers)` empty); kind named ("review fix"). Not pushed — the remote carries `main` and
`intake-parse-2026-08` only. Whether paths were staged explicitly is not visible to me.
`E9`: correctly spent and correctly declared — the body and journal §7 both state this is the
round's one user-approved fix and that a targeted VERIFY is owed, which is what this is.
Nothing landed on the branch between the FULL's record and the fix but the fix.
`E3`: every figure I could re-derive reproduces — the eight battery legs above; §live at 11
(`grep -c 'status: \*\*live\*\*'`), consistent with the 12→11 move of `HD-31`; the ledger at
117 lines against its 120 cap; the pack at 15 files. One texture note, not a finding: journal
§7's `tests/harness/run_tests.py    Ran 39 tests  OK` merges two output lines
(`Ran 39 tests in 3.713s` and `OK`) into one string that appears in no command's output. Both
components are literal, the count is true, and I reproduced it.
`E12`: the handoff was one range and no per-acceptance argument; the plan records the next
step as `rsc v3 dispatch` without a written SHA.
`E11`: no card is owed for a fix leg inside an open round.
Boundary: the commit's declared boundary — *"work-product bytes are exactly the three low
fixes … everything else is record family"* — matches the five-path diff exactly, and no
approved boundary was exceeded.

## 8. Worktree integrity after review

```
$ git status --porcelain
  ?? ResearchSystem/migration/document-work-assurance-v3/v3-review-verify-080621a.md
```

The only path the worktree carries beyond the subject is this record. The `compile --check`
leg and the `pytest` leg wrote nothing tracked. The disposable repository used for the guard
firing lives in the session scratchpad and touches nothing here.
