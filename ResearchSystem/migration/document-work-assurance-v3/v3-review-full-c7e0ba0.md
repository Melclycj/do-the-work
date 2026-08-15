# FULL review — `5d1741236d1f6e6fdfaebf3f042e4c580da87e52..c7e0ba022a5ae53e71ac7560fab041d1be589ecc` (batch B, round R3)

**Verdict: `CHANGES_REQUIRED`.** One blocker, three lows, three observations.

The construction is sound. Both live read-couplings between the harness and the caller's
ledger are cut, and cut cleanly: `ledger_cap_check.py` leaves the harness tree by a 100%
rename and still binds from its new path (I fired it), and the `READ_PROMPT` half-sentence
is gone with its committed fixture edited in the same commit, so the whole-text comparison
that pins that prompt stays binding (I mutated it red and restored). The write-couplings
really do live only in closed runs and shadow rounds — the live `run-v2` template holds no
ledger reference at all — and no live harness module reads or writes ledger content any
more. `HARNESS-POLICY.md` discharges the three things `io-design` §5 asks of it, `HD-31`'s
flip to `§implemented` rides the implementing commit as `HD-2` requires, the mirror rule
holds byte-for-byte, and the `E2` frozen surface is untouched.

The blocker is the round's own verification warrant. The commit body and the plan claim a
full battery over "six legs, all green"; five commands ran, and three of the legs
`EXECUTION.md` names for a tooling-touching change — P4 goldens, P5A goldens, schema
fixtures — had no command in this round. I ran all three at the subject: 80, 39 and 58
green. So the fix is a corrected record, not a code change; but "full battery" as written
is a characterization no command established, which is the shape `E3` exists to refuse.

## 1. Subject, re-derived (`R2`)

Handed a range and nothing else. Round, budget, authorization, boundary and every number
below are derived here; nothing is taken from the commit body, the plan, or the ledger.

```
$ git rev-parse HEAD                  -> c7e0ba022a5ae53e71ac7560fab041d1be589ecc
$ git status --porcelain              -> (empty)
$ git log --oneline 5d17412..c7e0ba0  -> c7e0ba0 V3-B-R3-CONSTR-v1   (one commit)
$ cat .harness/review-pending.json
  {"subject": "5d17412…..c7e0ba0…", "dispatched_at": "2026-08-12T12:31:13+00:00"}
```

HEAD equals the range tip and the tree is clean, so worktree reads are reads of the subject.
Dispatch (12:31:13Z = 22:31:13+10:00) post-dates the tip commit (22:30:40+10:00) by 33
seconds and the branch has taken no commit since — this record is the first it admits (`E9`).

**Round and budget.** `git log` on the branch: R1 ran `e9166d2` → FULL `1025491` → bank
`0458bfb` → fix `dbbec28` → VERIFY `1986912` → closeout `0c02a3c`; R2 ran
`b75f5b3`→`790e06e`→`cbd0b38`→`1d6f3c4` and closed on the user's signature (`HD-35`), with no
FULL. No review record exists for any commit after `1986912`. So no valid independent FULL
has occurred for R3: by `E9`'s test this commit is the candidate and this is R3's FULL, with
the round's budget intact — at most one user-approved fix and one targeted VERIFY behind it.

**Authorization, as visible in the repository.** `HD-35` (live) signs `io-design.md` v1 at
blob `8f3c82c2` as the execution basis, §5 for R3. `HD-31` (the `HD-26` successor) is the
per-clause warrant. `.goals/plans/harness-batch-b.plan.md` step 11 states the boundary,
including the two exclusions. The `E11` card itself is chat-only; journal §6 transcribes its
two defaults and the approval, and the plan carries the boundary, so the load-bearing content
is in the repository even though the rendering is not (`R7`: ceiling stated, not a block).

**Changed paths, classified by hand** (11 entries; `git diff --name-status`):

| path | class | in the declared boundary? |
|---|---|---|
| `ResearchSystem/tooling/hooks/ledger_cap_check.py` → `Thesis/Work/Tooling/ledger_cap_check.py` | work product (R100 rename, 0 byte delta) | yes — plan step 11 names the target dir |
| `ResearchSystem/tooling/rsclib/document_harness/dispatch.py` | work product | yes — `HD-31` 后果 names `dispatch.py:636` |
| `ResearchSystem/tooling/tests/fixtures/expected-read-prompt.txt` | work product (committed fixture) | yes — forced by the line above |
| `ResearchSystem/tooling/tests/document_harness/test_precommit_checks.py` | work product | yes — card default, per journal §6 |
| `ResearchSystem/HARNESS-POLICY.md` | caller policy (non-member, self-declared) | yes — plan step 11 |
| `CLAUDE.md`, `AGENTS.md` | caller navigation | yes — plan step 11, mirror rule |
| `ResearchSystem/document-harness/README.md` | **instruction layer (`E10` member 2)** | not enumerated in step 11; disclosed in the body as an `E10` deferral-channel subtraction |
| `ResearchSystem/HARNESS-DECISIONS.md` | decision register | yes — `HD-2` forces the flip into this commit |
| `.goals/plans/harness-batch-b.plan.md`, `document-harness/journal/batch-b-2026-08-11.md` | record family | yes |

**`E2`.** No changed path is frozen. `git diff --name-only 5d17412 c7e0ba0 -- ResearchSystem/schema/ ResearchSystem/contract/` returns nothing; the pack is still 15 files; contract
`b2dbdf75`, supersession-1 `68031fa2`, supersession-2 `e1a2f26b` all unchanged at the tip.

## 2. What I read, and how (`R4`)

**In full:** `CONSTRUCTION-CHECKLIST.md` (standing instructions, this session's first read);
`v3-harness-review-contract.md` (the stub that routes to it); the complete diff of the range;
`HARNESS-DECISIONS.md`; `HARNESS-LEDGER.md`; `HARNESS-RIDERS.md`; the new `HARNESS-POLICY.md`
in its entirety; `Thesis/Work/Tooling/ledger_cap_check.py`; `hooks/__init__.py`; the main
repo's `.git/hooks/pre-commit`.
**Sampled at the places the change touches:** `io-design.md` §5–§7; `EXECUTION.md` §Pre-freeze
gate and §Regression-battery tiering; `test_dispatch.py:430-480`; `candidate_path_check.py:50-90`;
`v3-checkpoint-read-3f19561.md` §1; `run_p4_tests.py` / `run_p5a_tests.py` / `run_tests.py`
docstrings; `runs/p5a-shells/control/check-chk-*.json`.
**Probed only:** the closed runs and shadow rounds (grep for ledger paths, not read); `REVIEW.md`.
**Marked, not verified (`R4`):** that this session is fresh context; that the executor staged
explicit paths rather than `add -A`; that the six-leg battery ran "before commit" as opposed to
at some other moment — I can only measure the tip.

## 3. Does the implementation do what it claims

**The rename is a rename.** `R100`, zero byte delta, and the file still functions from the
caller tree — I exercised it in a disposable repo: staged ledger at 121 lines → `exit 1` with
the block message; at 120 → `exit 0`; not staged → `exit 0`. The per-machine hook was updated
as the body says: a caller-side existence-guarded block invokes `Thesis/Work/Tooling/
ledger_cap_check.py`, and the harness loop below it is now three checks
(`review_freeze_check`, `layer_path_check`, `candidate_path_check`). Per-machine and untracked,
so it is evidence about this machine, never a repository guarantee.

**The prompt edit and its fixture.** `READ_PROMPT` drops "what the ledger binds to this read"
and the committed fixture drops the same clause. `test_dispatch.py:453-458` compares the
rendered prompt to the whole fixture text with `assertEqual`, expectation independent of the
module (`E5`), so the pair stays pinned. Mutation below.

**The write couplings.** Verified independently rather than accepted: `grep -rn "LEDGER"` over
`rsclib/`, `hooks/` and `rsc.py` returns exactly four hits, all in `candidate_path_check.py`'s
`RECORD_SURFACE` skip list (O-1). `assurance/templates/run-v2/` — the live template every future
run copies — contains no ledger reference at all. Every `write_scope` and `chk-ledger-note`
occurrence sits under `assurance/runs/` (p3-corr, p4-bridge, p4-doc, p5a-*, p5b-*) or
`assurance/shadow/`. The claim holds: nothing live binds the ledger.

**The instruction layer after the edit.** `ls ResearchSystem/tooling/hooks/` = the three modules
the amended README row now names, plus `__init__.py`. The row's factual assertion is true as
edited. Each of the three surviving modules still cites that row in its docstring and each is
still listed there; the moved module cites it and is not (L-1). No test pins the row —
`test_readme_enumeration.py` pins the schema-file enumeration only — so nothing else moved.

**`HARNESS-POLICY.md` against what authorizes it.** `io-design` §5 asks the caller policy file
for three things: the two ledgers with the tightened parameters declared there, a link to
harness internal state, the length script. §2 carries the two-ledger table with the ≤120-line
cap; §1 names the command exits; §3 names the script at its new path. `HD-31`'s carry-over
obligation — the caller chooses whether a mechanism succeeds `chk-ledger-note` — is answered in
§4 with an explicit "no machine, discipline carries it", citing `E6`. The header declares
non-membership and instruction-layer supremacy on conflict, which is what `HD-21` wants of a new
governance file (that obligation fell on `1d6f3c4`, the round that created the stub, not on this one).

**Decision-register mechanics.** `HD-31` moves whole into `§implemented` in the same commit as
its implementation, which is `HD-2`'s invariant and the deviation `HD-25` had to record. `§live`
counts: 12 at `5d17412`, 11 at `c7e0ba0` (`grep -c 'status: \*\*live\*\*'`) — the body's correction
of the plan's "13" is right, and the decisions file took no write between `1d6f3c4` and the base.

**The nine `E10` members at the base.** `git ls-tree 5d17412` returns exactly the digests the body
reports — `44d622b9` / `dab9f71a` / `8bbd330f` / `3350bfac` / `17ff31bb` / `52a97a48` / `68031fa2` /
`e1a2f26b` / `09aa8699` — and they equal the Section 1 table of `v3-checkpoint-read-3f19561.md`,
so every member was unchanged since a recorded read and the citation clause covers the cold read.
At the tip only member 2 differs (`dab9f71a` → `54dfef83`), which is the README subtraction and
which the next read of this layer will see.

**`E10` deferral channel, tested against the clause.** The subtraction adds no clause and changes
what no rule requires — the row is a registry of advisory per-machine checks, and removing an item
that moved out of the tree restores its accuracy; its effect on rounds in flight is nil, there
being one round and this is it. Both facts are recorded in the commit, and the body states the
bytes ride the next read. The path is not one `E2` freezes. Conformant.

## 4. Guard binding — my own mutations (`R8`)

Both restored from sha256-checked scratchpad copies, never `git checkout --`; `dispatch.py` hashes
back to `a3fa8460a669ee3f51cb2c20dfb87dfb78e3471f8a0a837ba33e71f0cad58050` after the probe and the
worktree is clean.

| # | mutation | result |
|---|---|---|
| — | negative control, unmutated | `51 passed` |
| M1 | the deleted half-sentence restored into `READ_PROMPT` **only** (the real defect shape: prompt drifts, fixture does not follow) | `1 failed, 50 passed` — exactly `test_the_prompt_is_exactly_the_golden_file`, at value level |
| M2 | moved guard fired at its new path in a disposable repo: 121 staged / 120 staged / not staged | `1` / `0` / `0` — must-fire plus two negative controls |

M1 isolates cleanly: one test, the right one, failing on the diff rather than on an import or a
crash. The fixture binding survived the edit intact.

## 5. Blocker

### `B-1` — the round claims a battery it did not run

**Location.** Commit `c7e0ba0` body: *"Full battery (tooling-touching), six legs, all green before
commit: tests/run_tests.py 29 passed; pytest … 701 passed …; tests/harness 39 OK;
tests/stage_control 20 run 0 failures; rsc.py compile --check exit 0 lint clean."* Five commands,
presented as six legs. Mirrored in `.goals/plans/harness-batch-b.plan.md` step 12
(*"候选 commit 前六腿全绿：29 · 701 … · 39 · 20 · compile --check exit 0"*).

**Ground truth.** `EXECUTION.md:322-323`: *"**Schema, tooling, or generated surfaces touched**: the
full battery runs — P2/P4/P5A goldens, schema fixtures, pytest, `compile --check`."* The change set
includes `rsclib/document_harness/dispatch.py` and two files under `tooling/tests/`, and the body
itself labels the tier "tooling-touching", so the full battery is owed. What those leg names denote
is not open: the harness instantiates them as commands in its own runs —
`runs/p5a-shells/control/check-chk-{p2,p4,p5a}-golden.json`, `check-chk-schema-fixtures.json`,
`check-chk-pytest.json`, `check-chk-compile-check.json` — and `EXECUTION.md:331-332` costs the same
set as *"P2 29 + P4 80 + P5A 32 + fixtures 58 + pytest 556"*. Three of those legs had no command in
this round: `tests/run_p4_tests.py`, `tests/run_p5a_tests.py`, `schema/fixtures/validate_fixtures.py`.
None is reachable from what did run — pytest collects `test_*.py` only, there is no `conftest.py`
and no pytest config anywhere under `tooling/`, and `tests/run_tests.py` is the P2 goldens alone by
its own docstring. `E3` then applies directly: "full battery … all green" is a characterization of
the work that no command established for half the legs it names, and `E3` says such a
characterization is dropped, not softened.

**Why this is not the rider.** `tier-scope` ① banks the opposite direction — legs that run but are
not enumerated (`tests/harness`, `tests/stage_control`) — and the 2026-08-12 ruling that left it in
place explicitly accepted that "下一个 tooling-touching 批仍会遇到同一张四腿枚举，仍只靠执行者恰好知道".
That ruling accepted a short enumeration; it did not authorize running fewer legs than the
enumeration names. Nothing in the repository covers this direction.

**What is at stake if it stands.** The three skipped legs are exactly the ones covering the schema
and generated surfaces that pytest and `compile --check` do not: 80 + 39 + 58 = 177 fixture-driven
cases asserting stable error codes. The five-command pattern is now on its third consecutive
tooling-touching commit (`e9166d2`, `dbbec28`, this one), so the next one will copy it, and a
tooling change that reddens a golden or a schema fixture would ship unseen.

**Minimum fix.** Run the three commands at the round's tip and record their output in the round
record or journal; correct the "six legs" account so the leg set named matches the commands run.
No work-product byte changes. I ran all three at the subject and they are green —
`run_p4_tests.py` `tests: 80 passed: 80` exit 0; `run_p5a_tests.py` `tests: 39 passed: 39` exit 0;
`schema/fixtures/validate_fixtures.py` `cases: 58 matched: 58 unexpected: 0` exit 0 — so the
expected outcome is a corrected record and not a repair to the change itself. If the executor
would rather rule that these legs are not owed for construction batches, that is a rule change
and opens its own round (`E10`); it is not something this round's body may assume.

## 6. Lows

- **`L-1` — the moved script cites a row that this commit emptied of it.**
  `Thesis/Work/Tooling/ledger_cap_check.py:9` still reads *"Advisory and per-machine, bypassable
  with --no-verify (README "Local enforcement" row)"*, and the same commit removed the ledger-cap
  item from that row. Its declaration home is now `ResearchSystem/HARNESS-POLICY.md` §3, which the
  per-machine hook comment already cites correctly. Downstream decision that goes wrong: a
  maintainer following the citation lands in the harness's instruction layer and reads a
  caller-owned script as harness-registered — the ownership confusion the round exists to remove.
  **Bytes:** replace `(README "Local enforcement" row)` with
  `(ResearchSystem/HARNESS-POLICY.md §3)`.

- **`L-2` — `HARNESS-POLICY.md` §1 drops `dispatch` from the command surface.**
  It reads *"另有 `governance-scan` / `review` 只读"*. `rsc v3 --help` lists six subcommands, and
  `io-design` §5 — the signed text this section is written from — names *"`governance-scan` /
  `review` 两个只读命令与 `dispatch`"*. The omitted one is the only command that writes (the freeze
  marker under the caller's `.harness/`), so a policy file whose subject is the harness's outward
  I/O drops precisely the command with an effect on the caller's tree.
  **Bytes:** append `与 `dispatch`（唯一写盘：`.harness/review-pending.json`）` to that parenthetical.

- **`L-3` — `HD-28` cited for a rule it does not contain.**
  The commit body (*"stay untouched per HD-28"*), `HARNESS-DECISIONS.md:157` (HD-31's
  `§implemented` note) and plan step 11 (*"`HD-28` 不许碰"*) all rest the closed-run exclusion on
  `HD-28`. `HD-28` rules *which repository* those artifacts live in — "D 已关闭 run 的产物与 E
  shadow 留产品仓" — and says nothing about editing them. The nearest actual ruling is `HD-25`'s
  "现存八个已关闭 run 不回改", scoped to that decision's own subject. The exclusion itself is
  authorized (plan + card); what fails is its basis pointer, in the register that is the highest
  source of truth. **Bytes:** in the three places, cite `HD-25`'s closed-run clause, or state the
  exclusion as the plan's own boundary decision rather than as a decision-register consequence.

## 7. Observations

- **`O-1` — `RECORD_SURFACE` is the fifth reference, and it is still a harness file holding
  caller path literals.** `hooks/candidate_path_check.py:64-73` hard-codes
  `ResearchSystem/HARNESS-LEDGER{,-archive}.md` and `.goals/LEDGER{,-archive}.md`. I confirm the
  executor's characterization: it is a prefix skip-list, matched by `startswith` against staged
  paths, and no code path reads or writes ledger content. It was found, disclosed on the card and
  judged out of boundary, and journal §6 names it as the split batch's checkpoint. The shape
  nonetheless survives the round: after the split, the harness repository would carry four
  caller-specific path literals. Whether that matters is the user's call (`R5`).

- **`O-2` — the deleted tests include the one written for a defect this guard actually had.**
  `test_the_guard_targets_the_real_ledger_path` asserted `ledger_cap_check.LEDGER` against a
  hand-written literal because that constant was once genuinely typo'd, so the guard could never
  fire on the real ledger (`v3-review-full-8ec4c60` M-3, red-proven at `v3-review-verify-49d9829`
  V1). That failure mode is silent: a mistargeted constant returns 0 forever. The script now has
  no test at any path. The deletion is a card default the user approved and the body discloses it
  as untested at caller standing; my M2 shows the behaviour survived the move today. Recorded so
  the cost is visible, not as a finding against the round.

- **`O-3` — `HD-28`'s membership list predates the policy file.** `ResearchSystem/HARNESS-POLICY.md`
  was created at `1d6f3c4`, after `HD-28` enumerated the new repository's members (A instruments +
  three governance registers + review records, ledger to the caller). It is caller-owned by its own
  header, so its placement is decidable, but the split batch's member list will have to say so
  rather than derive it.

## 8. Record and boundary conformance (`R3`, run second)

`E8`: one commit, no amend (`git log` shows a single new object on the branch), title
`V3-B-R3-CONSTR-v1` naming the round, one dense paragraph, no trailers, kind named ("candidate").
Not pushed — the remote carries `main` and `intake-parse-2026-08` only; push debt is 624 and
user-gated. Whether paths were staged explicitly is not visible to me.
`E9`: budget intact and correctly spent — this is the round's FULL; the marker was written after
the commit landed, so nothing landed inside the freeze window.
`E12`: the handoff was one range and no per-acceptance argument; the plan records the next step as
`rsc v3 dispatch` without a written SHA.
`E11`: card chat-only; its two defaults and the approval are transcribed in journal §6 and its
boundary in plan step 11 — ceiling stated per `R7`.
`E3`: every other figure in the body reproduces. `701` measured; the `705 → 701` delta is exactly
the four deleted `def test_` methods (46 → 42 in the only changed test file, no other test file in
the range, no dynamic collection); `29` / `39` / `20` / `compile --check exit 0` all reproduce; the
ledger is 117 lines against the 120 cap; `CLAUDE.md` and `AGENTS.md` differ only in the four
expected name swaps, so the mirror holds. The one exception is `B-1`.

## 9. Worktree integrity after review

```
$ git status --porcelain
  ?? ResearchSystem/migration/document-work-assurance-v3/v3-review-full-c7e0ba0.md
$ sha256sum ResearchSystem/tooling/rsclib/document_harness/dispatch.py
  a3fa8460a669ee3f51cb2c20dfb87dfb78e3471f8a0a837ba33e71f0cad58050
$ sha256sum ResearchSystem/tooling/tests/fixtures/expected-read-prompt.txt
  92facd0bce73ae927d8f620f40d9cdb53a8a7631691426062f34689d1c9c9a01
```

Both equal their pre-mutation values, and the only path the worktree carries beyond the subject is
this record. The disposable repository used for M2 lives in the session scratchpad and touches
nothing here.
