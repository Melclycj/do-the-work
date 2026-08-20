# FULL review — V3-PHASE-D-HISTORICAL-EXIT-v1 (`34cf85b`)

- **Subject**: `83e88fdeb5d06747e7b18d52a19d47c675855dd9..34cf85b438991b64017a6a71c311e9ddb63d19e3`
  (one commit; range and round derived from the repository per `R2` — freeze marker at
  `.harness/review-pending.json` holds exactly this subject, kind `construction-round`)
- **Round**: Phase D of `.goals/plans/harness-deletion-first-stabilization.plan.md` Step 9
  (ledger `NEXT = Phase D` at opening); commit kind self-named `candidate`; no prior FULL
  record for this round exists in the repository, so this dispatch is the round's one FULL.
- **Reviewer**: independent review session, 2026-08-01. Fresh context (process claim, marked
  not verified per `R4`).
- **Verdict**: **`REVIEWED_NO_BLOCKER`** — zero blockers; 2 lows (L-1 wording-level count,
  L-2 run-dimension gap in the new guard), 3 observations. Fix and VERIFY budget untouched.

## 1. Implementation (led with, per R3)

**`check_triage` TARGET-MISMATCH guard (CT + F-d)** — the guard binds. The new `else`
branch (`issues.py:194-210`) compares the target path's filename against
`f"{issue_id}.json"` after `\\`→`/` normalization; an issue with no `issue_id` reports the
same code. Both new tests assert hand-written code+locator literals, never module
constants (`E5` holds). I re-ran the fix myself and independently reproduced probe M-A:
neutering the comparison to `if False:` produced **exactly 3 value-level FAILs, zero
errors** in the 372-test review suite —

```
FAIL: test_the_module_level_codes_that_do_fire_are_reachable_with_valid_documents
FAIL: test_a_triage_pointing_at_a_sibling_issue_of_the_same_work_is_named
FAIL: test_an_issue_with_no_identity_cannot_be_bound_to_any_target
Ran 372 tests in 63.247s
FAILED (failures=3)
```

— matching the journal's RED shape; restore from my own sha256-checked snapshot returned
the suite to green. `make_triage`'s fixture default now names `control/hi-one.json`,
matching `make_issue`'s `issue_id="hi-one"` — the alignment the guard requires, correctly
disclosed as the only use of the old literal. The reachability enumeration
(`EnforcementLayerIsPinned`) gained both the new code and a real invocation reaching it.
`record_issue`'s docstring now says build-and-return (F-d) — verified against the body:
the function persists nothing.

**Real-data triage sweep** — I re-ran `check_triage` over every decision–issue pair in
`assurance/runs/p3-corr/issues/` myself (accepting no reported figure): **8 pairs, all
clean under the new guard**; my cross-pair control (channel decision vs
`harness-knowledge-in-memory` issue) fired `V3-HARNESS-ISSUE-TARGET-MISMATCH`. The new
decision file's `target.harness_issue_ref.digest_sha256`
(`d38e72a8c207dac145134e21eb3e3358167e4a8704982d5e45df7a24ad91b8be`) equals the sha256 I
computed over the issue file's bytes. Byte style verified: all 8 decisions, the new one
included, are compact JSON, sorted keys, no trailing newline (the older five carry raw
UTF-8 em-dashes, i.e. `ensure_ascii` differs — content-irrelevant for the new pure-ASCII
file). Untriaged remainder: `harness-self-maintenance-burden` only, per plan Steps 9/10.

**Freeze-marker producer test (F-3r)** — the suite drives the real
`rsc.py v3 dispatch` as a subprocess against a disposable repo; expected marker path,
kind, and subject are hand-written literals (`E5` holds); the failed-dispatch negative
control asserts exit 1 and no marker. Born green as disclosed; I reproduced probe M-B
myself: guarding the marker write with `if False:` (the "dispatch silently stops holding
E9's window" shape — the CLI even still prints its success line) produced **exactly 1
value-level FAIL** (`a successful dispatch left no freeze marker`) with the negative
control staying green; restore from my snapshot, suite green. Binding force shown.

**`[historical]` markers** — the diffs to `rsc.py` and `rsclib/harness/cli.py` touch
string literals only (module docstrings, two `add_parser` help kwargs); no operation,
argument, or exit path changed; no code or test deleted (`--name-status` shows no
deletions). `python rsc.py --help` renders both markers. Both legacy suites re-run by me:
harness `Ran 39 … OK`, stage-control `20 run, 0 failure(s), 0 error(s)`.

**W-1 wording fix** — the schema `description` now states SHA-256 over lines joined with
`"\n"`, UTF-8 encoded, line endings normalized, no trailing newline; verified against
`instruction.py`'s `paragraph_skeleton` (splitlines → `"\n".join` → no trailing newline).
Exactly the ride the C4 FULL scheduled (`v3-review-full-d50d9e5.md` W-1). Schema still
parses; suites green.

**E1 sentence (design amendment)** — reviewed as text in the subject diff: consistent
with `R1` and the pre-existing E1 clause; codifies the deleted memory habit without
changing any verdict path. Correctly declared design (adds a clause), correctly run
inside a carded round, its independent read correctly deferred to the closing layer read
and **not** banked as this FULL. Nothing has relied on it; I find no defect in the
sentence itself.

## 2. Suites and frozen surface (independently re-run at the subject tip)

```
tests                         29 passed / 0 failed   RESULT: OK
tests/stage_control           20 run, 0 failure(s), 0 error(s)
tests/harness                 Ran 39 tests  OK
tests/document_harness        Ran 181 tests  OK   (exit 0)
tests/document_harness_review Ran 372 tests  OK
repo-audit                    exit 0
```

`git rev-parse` at `34cf85b`: `8ad404b1…` / `b2dbdf75…` / `68031fa2…` / `e1a2f26b…` —
the four `E2` blobs byte-identical. Pack diff over the range touches exactly one file,
`paragraph-map.schema.json` (15th member, joined post-2026-07-29, not frozen); pack count
15. Both user-locked oracles: empty diff over the range.

## 3. Process and record conformance (boundary check, run second)

- **E8** — title `V3-PHASE-D-HISTORICAL-EXIT-v1`, kind named (candidate), one dense
  paragraph, no trailers; ten changed paths, all inside Step 9's declared scope
  (tooling markers, guard+tests, triage decision, riders, checklist E1, journal, W-1).
- **E9** — freeze marker present and holding this subject; branch has taken no commit
  after the candidate; this FULL is the round's first budget consumption.
- **Cold-read waiver (card ruling ①)** — factual basis independently verified: I
  recomputed all eight member blob ids at `83e88fd`; seven equal the
  `v3-checkpoint-read-784e49b.md` §1 table; the eighth (`document-harness/README.md`,
  `bb84e6f2`→`f3a31208`) diffs by **exactly one added row** (the C4 paragraph-map
  enumeration row already riding `E10`'s deferral). The waiver itself is the user's
  (`R7`: authorization visible only as the journal/commit record — ceiling stated).
- **Riders (R10)** — CT, F-d, F-3r rows deleted in the same commit as their fixes, each
  fix riding this batch's touched surfaces (`issues.py`, `rsc.py`); CT's early redemption
  is within its recorded deadline ("最晚 Phase E 的 ISSUE_TRIAGE 前") and this round's
  triage is the recorded bite scenario. Remaining rows verified: F-4, F-c, O-2b, SCC,
  RA, L-2li, L-1lr — none else due on this batch's surfaces.
- **Memory disposition** — beyond the journal's honest "unwitnessable from the
  repository": I probed the memory directory at review time; **no `v3-*.md` file
  remains** and `MEMORY.md` carries no rows for the two deleted atoms. The five
  previously-migrated atoms' owners spot-checked in the layer (E3/E5/E6/R3 carry them).
  Plan acceptance "memory 里不再有 operative harness 指令" holds as far as this machine
  can witness.
- **Preview card / four rulings** — recorded in journal + commit body (committed, so not
  chat-only under `R2`); that the user issued them is not repo-verifiable (`R7`).

## 4. Findings

- **L-1 (wording-level, R9)** — commit body and journal ruling ② call p3-corr "the
  8-issue … run" / "(8 issues, one work_id)". The run has **9** issue files (all one
  `work_id`; I enumerated them); 8 is the count of decision–issue *pairs* checked. No
  downstream decision turns on it — the CT redemption needs only "multiple issues on one
  work", true at 9 as at 8 — and the accurate count is recoverable from the repository
  and from this record. Commit bodies are immutable; no action beyond this note; `E3`'s
  count discipline is the clause this grazed.
- **L-2 (low)** — the new guard binds the *issue* dimension but not the *run* dimension:
  `check_triage` compares target-filename↔`issue_id` and `work_id`↔`work_id`, but never
  `decision.run_id`↔`issue.run_id` (the field is optional in the user-decision schema,
  present on all 8 real decisions). A decision about a same-`work_id`, same-`issue_id`
  issue in a *different run* would still read clean. Remote today (issue_ids embed the
  run slug by convention — but convention, not enforcement). Minimum fix: when both
  documents carry `run_id` and they differ, report; one test. Non-blocking — per `R10`
  the executor weighs bank-vs-fix-leg with the user before closeout; the touch surface
  is `issues.py`.
- **O-1 (observation)** — accumulation data point for the 保障面二期复盘 backlog item:
  this round adds one guard branch and one two-test CLI suite while deleting three rider
  rows and two memory atoms — the deletion-first shape running in the intended
  direction; reported as shape only (`R5`).
- **O-2 (observation)** — the freeze marker records a resolved full-SHA tip; under
  `E12`'s window invariant this cannot go stale (the only commit that may land deletes
  the marker in the same act), and the marker is transient state, not a round record. No
  action; noted so the next reader does not re-derive it.
- **O-3 (observation)** — suite-count arithmetic verified: review suite 368→372 (+2
  triage guard, +2 freeze marker), consistent with C4's recorded 368.

## 5. Disclosure (R4)

Read in full: the subject diff (all ten files), `issues.py` (current bytes),
`test_dispatch_freeze_marker.py`, the `make_issue`/`make_triage`/helper fixtures and both
new tests in `test_flow_repair_disposition.py`, journal `d-2026-08-01.md`,
`CONSTRUCTION-CHECKLIST.md` (current), `HARNESS-RIDERS.md` (current), the new decision
JSON, plan Step 9/10 + Resume pointer, `HARNESS-LEDGER.md` pointer block, the freeze
marker. Sampled: `rsc.py` (dispatch marker block :370-405, module docstring, stage
parser), `instruction.py` (`paragraph_skeleton` head), `user-decision.schema.json`
(required list, run_id), C4 FULL record (W-1 block), `v3-checkpoint-read-784e49b.md`
(§1 member table via grep), README member blob diff. Probed only: memory directory
(glob + MEMORY.md), `--help` render, oracle/pack diffs, frozen blob ids. Re-derived, not
accepted: all suite counts, repo-audit, triage sweep, sha256 binding, member blobs, pack
count, rider rows, issue count. Mutation probes M-A and M-B reproduced by me from my own
sha256-checked snapshots (snapshot hashes matched the journal's recorded `3ba42ffc…` /
`a33f445d…`, i.e. committed bytes = the executor's post-probe restore). Not verified:
that the user issued the four card rulings (chat; recorded in repo), the executor's
process claims (RED-first ordering of the original run, scratchpad custody), the
MEMORY.md edit's authorship. Mutation proves the two new tests have binding force, not
that their force is sufficient (`R4`).
