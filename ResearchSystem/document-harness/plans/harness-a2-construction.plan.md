# Plan: Batch A / A2 — build what A1's rulings bought

- **slug**: harness-a2-construction
- **created**: 2026-08-08
- **complexity**: 复杂
- **status**: **COMPLETE — R0 through R4 CLOSED and step 10 (batch close) executed 2026-08-10.
  batch:A rulings retired (`HD-11`/`HD-12`/`HD-13`/`HD-14`, archive), `HD-18` implemented,
  `HD-10`/`HD-15`/`HD-16`/`HD-24` live awaiting the split batch. Nothing in this plan remains
  open; successors are batch B, then the split batch (`HD-18` sequencing).** Both entry gates had
  cleared 2026-08-09: A1's review landed
  (`a7bb1d6` FULL → `fd058aa` fix → `7a08265` VERIFY, no blocker) and the `E10` layer read is paid
  (superseded during the batch by `v3-checkpoint-read-3f19561.md` — cite its §1, per its `O-2`).
- **scope narrowed 2026-08-08 by `HD-18`**: the split itself (`HD-15` / `HD-16`) and rider
  `CLI-hist` **left this plan** for a batch of their own, sequenced after batch B. What remains here
  is single-repository work only, every round with a revert unit.
- **base_commit**: `8e018e1` (tip at A2's opening / R0 start, set 2026-08-09 — the field had said
  "set at the first A2 round" and no round set it; A1's tip at authoring time was `41b4835`)
- **base_branch**: document-work-assurance-v3

## Goal (one line)

Stop copying template scripts into every run, stop keeping a run's CheckResults after it closes,
and put the run template's six rule sections under the protection they already behave like — all
inside the current repository, so that the split, when its own batch reaches it, moves a harness
whose shape is already settled.

## The rulings this plan executes — inherited, not transcribed

`HD-5` forbids transcribing a ruling into a plan: transcription is a drift surface and batch A has
**three measured instances** of exactly that failure (the "276+ mixed history" figure with no
source, the plan's Why paragraph, and `D5`'s cut). So this file names the ids and nothing more.
Read them in [ResearchSystem/HARNESS-DECISIONS.md](../../ResearchSystem/harness/ResearchSystem/HARNESS-DECISIONS.md) §live:

**This plan executes**: `HD-11` (D1) · `HD-12` (D2) · `HD-14` (D7) · `HD-17` (AMBIG audit) ·
`HD-13` (D3 — a *do-not*, and the reason there is no round for the review record).
**Ruled but executed elsewhere**: `HD-10` / `HD-15` / `HD-16` / `HD-18` are the split batch's.
Measurements behind all of them:
[journal/batch-a1-2026-08-08.md](../../ResearchSystem/harness/ResearchSystem/document-harness/journal/batch-a1-2026-08-08.md).

## Why / value

Two things A1 measured, each of which one round below is aimed at:

- Every run copies **≈883 shareable lines** of instrument into itself, and the copies have already
  diverged — 17 of 23 were never the template's bytes, and `build_run.py` is only 24% alike across
  runs. Copying is not what it was believed to be, so the fix is a shared core plus a per-run delta.
- A run's per-check CheckResults are **22% of the run** and have been cited **zero times** after
  their run closed, across eight runs and six weeks.

The third measurement — the harness is **74% of `ResearchSystem/`** and depends on the product
almost one-way (**1,092 refs out, 12 back**; `rsclib/document_harness/` imports nothing from the
product side) — is the split batch's warrant, not this plan's. It says the harness is already a
leaf, which is why deferring the split costs little.

## Constraints / Out-of-scope

- **A1's review must land first.** A1 measured, ruled and wrote this plan without a single
  independent read. Opening construction on unreviewed measurements is the failure `E10` exists to
  stop.
- **Out — the split itself** (`HD-18`). Nothing in A2 may create a second repository, a submodule,
  or a cross-repo reference. If a round finds it *needs* one, that round is mis-scoped: stop and
  hand the finding to the split batch.
- **Out — the eight closed runs.** `HD-12` binds future runs only; the closed runs keep their
  CheckResults and stay where they are (`HD-16`).
- **Out — the review record's form.** `HD-13` closed it. Do not reopen; the measurement that would
  justify reopening (§10, §12.2) is the measurement that closed it.
- **Out — `AMBIG`'s 138 files.** `HD-17` defers them behind a survival audit (R0 below). Do not
  move them, do not delete them, do not assume they are dead.
- **Out — `rsc.py`'s command surface** until R0 reports. Rider `CLI-hist` names the fix, but its
  trigger is the split and its precondition is the audit.

## Steps

### R0 — two read-only measurements. No construction, no revert unit.

- [x] 1. **AMBIG survival audit** (`HD-17`). For each of `ResearchSystem/harness/`,
      `tooling/rsclib/harness/`, `tooling/tests/harness/`, `schema/harness-v2/`,
      `migration/general-harness-v2/`, `migration/stage-control-refactor/`, `stages/`: does anything
      still import, execute, validate against or link to it? Report per item: live consumer / dead /
      records-only. Then the user rules each one travel / stay / retire. **Do not propose retirement
      for anything with a live consumer.**
~~2. submodule semantics~~ — **moved to the split batch by `HD-18`.** It is that batch's first
measurement, not A2's: nothing here crosses a repository boundary.

Lands in a journal. Analysis, not construction — no round, no revert unit.

### R1 — `HD-14`: move the six rule sections into `EXECUTION.md`

- [x] 3. Move `Pre-freeze gate` · `Instruction form` · `Authoring gate` · `Audit cadence` ·
      `Regression-battery tiering` · `Instruction authoring rules` out of
      `assurance/templates/run-v2/README.md` and into `EXECUTION.md`; leave the README holding only
      how to instantiate the template. — **round closed 2026-08-09**: `418b89c` move → FULL
      `REVIEWED_NO_BLOCKER` → dispositions (`87cadf0` bank/free-channel · `fbcb035` L-1 fix leg) →
      VERIFY `REVIEWED_NO_BLOCKER` → `7ea3566` VERIFY dispositions.
- **This is an instruction-layer amendment: it opens a round** and owes the opening `E10` cold read
  plus one independent review, and the amended text owes its own read before any round relies on it.
- **Answer first, in the round's own preview**: `Instruction form` and `Authoring gate` are
  authoring-time rules while `EXECUTION.md` is the *executor's* role instruction. If they are not
  the same reader, some of the six belong elsewhere and this round's scope shrinks.
- **Revert unit**: the single commit. `EXECUTION.md` goes 171 → ~350 lines and becomes the layer's
  largest member; `layer_path_check.py`'s `LAYER` is unchanged because no member is added.

### R2 — `HD-11` part one: parameterize before sharing

- [x] 4. Replace "edit the file, fill the CONFIG block" with "read config, pass arguments".
      `RUN_ID` / `BASE` / `CANDIDATE` / `CANDIDATE_BRANCH` / `REPAIR_ROUND` / `EVIDENCE_COMMIT` /
      `SOURCE` / `SITES` come from the run's control JSON, which is already JSON. — **done (R2
      `7e8f920`), with a measured correction to this step's own sentence**: `REPAIR_ROUND` reads
      from the run's state file and `RUN_ID` is the directory name, but `BASE` / `CANDIDATE` /
      `EVIDENCE_COMMIT` have **no pre-use control-JSON carrier** (work-spec `inputs` pins
      input-file revisions, not the base commit) — they became required CLI arguments under the
      same sentence's "pass arguments" half. Rich per-run data moved to two new per-run files,
      `runs/<run-id>/control/fulfillment.json` and `runs/<run-id>/control/bind-declarations.json`
      (no defaults, missing = STOP). **`SOURCE` / `SITES` — corrected again 2026-08-09**: the
      claim that they "stay in the per-check argv" was measured **false** by FULL `eec4171`
      `B-1`. They were a CONFIG block in the round's fourth script, `compare_blocks.py`, which
      R2 left untouched; the four committed check specs that invoke it carry a mode flag —
      plus, for `--prose`, its base sha — and no constant at all. The repair leg converts that
      script the same way: `SOURCE` / `SITES` and
      the rest of that block are now its CLI arguments, carried after the mode flag by the
      check spec's own argv.
- [x] 5. Cut the three `__file__`-derived roots (`run_evidence_v2.py`, `run_bind_v2.py`,
      `run_repair.py` compute `CONTROL`/`EVIDENCE`/`RS_ROOT` from their own location) over to an
      explicit run-directory argument — the shape `check_template_instance.py` already uses. —
      **done (R2 `7e8f920`)**; the `sys.path` bootstrap stays `__file__`-based on purpose (it
      locates the co-located library, not run data).
- **Must precede R3.** A shared script cannot carry per-run constants; this is the whole of what
  journal §3.2 found.
- **Revert unit** — originally: "`assurance/templates/run-v2/` plus one pilot run, in one
  commit". **Amended 2026-08-09** (user ruling, on FULL `eec4171` `O-1`, which measured that
  `7e8f920` carried no run and two files outside that directory): the pilot for this round is
  **the template's own test suite driving the parameterized scripts on synthetic runs**, not a
  scratch run — A2's own constraint (*Out — the eight closed runs*) leaves no run to pilot on,
  and a suite binds the argument surface where a single run would only exercise one path. The
  unit is therefore `assurance/templates/run-v2/` plus its suites under
  `tooling/tests/document_harness_review/`, across the two commits this round spent: `7e8f920`
  and the `B-1`/`L-1` repair commit. Recorded as an amendment rather than a rewrite because the
  original line is what `O-1` measured against.

### R3 — `HD-11` part two: extract the shared core

- [x] 6. Split the template into shared core + per-run delta. Budget from measurement: ~883
      shareable lines per run, ~45% of script bytes. **Do not plan a plain reference swap** — 17 of
      23 copies are forks and `build_run.py` is 76% run-specific. — **done (R3 `cef6138`), FULL
      pending**: sweep found zero instruction-layer sentences falsified and zero rsclib/hook
      consumers of run-local copies; README instantiation rewritten to the shared-core model
      (five scripts invoked in place, comparator still copied beside the instruction per
      `EXECUTION.md`'s unchanged rule, run-own files self-authored); the two assertion tests
      redeemed rider `deriv-bind` with M11/M12 mutation-kill evidence; battery nine legs green,
      pytest 683.
- **Revert unit** — originally: "the new template layout plus the pilot run's switchover, in one
  commit". **Amended 2026-08-09** (user opening approval, mirroring R2's `O-1` amendment — A2's
  own constraint leaves no run to pilot on, and post-R2 there is no new layout to land): the
  pilot is the template's own test suites driving the shared scripts on synthetic runs; the unit
  is `assurance/templates/run-v2/` plus its suites plus the redeemed rider row, in the one
  commit `cef6138`.
- **Executor analysis 2026-08-09 (re-presented and user-approved 2026-08-09 at the R3
  opening)**: R3 is lighter than authored. Post-R2 the shared core *physically
  exists* — the template scripts are invocable from their own path and the ~70 template tests
  already drive exactly that against synthetic runs (measured at the opening: **100**, not ~70 —
  bind 38 · comparator 21 · paragraphs 18 · fulfillment 12 · repair 11; the estimate
  under-counted). Remaining work ≈ a read-only sweep for any
  mechanism assuming run-local script copies, a run-v2 README instantiation rewrite (copy list
  shrinks to the comparator + run-own files; the three step scripts + two gate/map tools are
  invoked in place), and 0–2 assertion tests. Two design judgments to re-present: no new
  boundary convention is needed (`templates/` sits outside any normal `write_scope`, so a
  candidate touching the shared instrument is already non-conformant — unlike the p5b-claims
  incident, whose checker sat *inside* `write_scope`); the eight closed runs' old copies stay.
- **Not gated on the split** — corrected 2026-08-08 with `HD-18`. An earlier draft of this file said
  the core had to be built for two repositories or it would be built twice. That was too strong:
  R2 solves how per-run constants travel, which is independent of repository count, and moving the
  core into the harness repo later is a **path change, not a redesign**.
- **R3 round closed 2026-08-09**: `cef6138` construction (rider `deriv-bind` redeemed) → FULL
  `CHANGES_REQUIRED` (record `f1cd408`) → user REPAIR (conditional ruling — executor-error
  attribution, so repair; `841bd3b` bank, rider `delta-prose` for `L-2`) → `638972f` fix leg
  (`B-1` three docstrings, `L-1` honesty sentence) → targeted VERIFY `REVIEWED_NO_BLOCKER`
  (record `v3-review-verify-638972f.md`, committed executor-side per `R6`) → closeout: `V-1`
  banked as rider `copy-qual` (its carrier-wording half discharged in `HD-11`'s `§implemented`
  entry), `V-3` folded into rider `tier-scope` as its fourth leg, `V-2` adopted as dispatch
  practice (hand the CLI output only), `O-1v`–`O-5v` recorded.
- **R2 round closed 2026-08-09**: `7e8f920` construction (riders `bind-emit2`/`sg-print` redeemed)
  → FULL `CHANGES_REQUIRED` (record `e37acfb`) → user REPAIR, remedy (a) → `1610d94` bank
  (`deriv-bind` · `decl-dup`) + `3b6267c` fix leg (B-1 completed across all four scripts, B-2,
  L-1 tests, O-1 amendment) → VERIFY `REVIEWED_NO_BLOCKER` (record `620717f`) → closeout:
  `V-1` banked as rider `argv-cap`, `V-2`/`V-3` fixed in this file, `V-4` recorded only.

### R4 — `HD-12`: a CheckResult does not survive its run

- [x] 7. At closeout, delete the per-check CheckResults and keep the first-hand output. — **done
      (R4 `ed37a25`)**: sixth shared template script `run_retire.py` (landed as
      `run_closeout.py`; renamed by the repair leg `de8f4ef` on FULL `B-1` — that name already
      meant the run-own post-run issue step in p4-doc and p4-bridge), CLOSED-only
      (`STOPPED_REPLAN` expressly outside the ruling, stays strict), idempotent, deletion staged
      via `git rm` never committed by the script. Scope per the user's D-b ruling (2026-08-09):
      only the per-check files the committed plan's `check_order` names; the aggregate
      `check-results.json` and every `chk-*.out.txt` survive, so `state.check_results_ref`
      dangles nothing.
- [x] 8. Teach `review_subject.py:428-445` the difference between a live run (per-result files
      required, `-CHECK-RESULT-MISSING` on absence) and a closed one (absence is correct). Its
      comment currently declares the strictness deliberate — amend the comment with the ruling, do
      not silently weaken it. — **done (R4 `ed37a25`)**: absence-only carve-out keyed off the
      plane's own state status; present-but-broken files still report `-CHECK-RESULT-INVALID`;
      the original load-bearing comment retained with the `HD-12` sentence appended.
- [x] 9. Decide what `check_result_refs`' digests point at once the targets are gone. **The ruling
      accepted this cost; it did not specify the mechanism.** — **decided (user D-a ruling,
      2026-08-09)**: the refs stay exactly as bound — each digest pins bytes the run committed,
      and `git show <evidence-commit>:<path>` resolves them permanently after the worktree copy
      is retired. No reviewed artifact is rewritten, no deletion inventory is created (`HD-9`'s
      duplicate-copy cut); the closeout commit body is the record of the retirement act.
- **Revert unit** — originally "closeout code + `review_subject.py`'s predicate + their tests,
  in one commit". **Amended 2026-08-10** (VERIFY `de8f4ef` `V-2`, mirroring R2/R3): two commits —
  `ed37a25` construction + `de8f4ef` repair leg (the `B-1` rename plus `L-1`/`L-2`/`L-3`).
- **R4 round closed 2026-08-10**: `ed37a25` construction (rider `copy-qual` redeemed) → FULL
  `CHANGES_REQUIRED` (record `34e312f`) → user REPAIR (conditional ruling, second of its kind —
  executor-error attribution → remedy (a) + fold-all; `65ce815` bank, rider `status-key` for
  `O-1`) → `de8f4ef` fix leg (rename to `run_retire.py`, `L-1`, `L-2`, `L-3` with a stray-output
  fixture pin) → targeted VERIFY `REVIEWED_NO_BLOCKER` (record committed executor-side per `R6`)
  → closeout: `V-1`/`V-2` fixed in this file, `V-3`+`V-5` banked as rider `retire-suite`, `V-4`
  banked as rider `readme-three`, `O-1v`–`O-6v` recorded.
- **Forward-only.** The eight closed runs are untouched, so both shapes coexist and the predicate
  above is what tells them apart.

### ~~R5 / R6~~ — left this plan 2026-08-08 (`HD-18`)

The split (`HD-15` members + `HD-16` shape) and rider `CLI-hist` are their own batch, sequenced
**after batch B**. Carried there, not lost: the five-group membership account, the `rsc.py`
division, the submodule pin, the plan archive (**M6 holds** — the contract is in group A and travels
with it, so plan and contract stay co-located), the submodule-semantics measurement, and the fact
that **a history migration has no revert unit** and so needs a throwaway-clone rehearsal first.

Why it left: batch B's three items — which entrypoint `run_all` attaches to, how tightly the ledger
binds, whether `pack_digests` stays — **each change shape under two repositories**, and A1 never
scoped the cross-repo operating model at all (a review record in one repo describing a run in the
other; ledger pointers across the boundary; which half of `rsc.py` runs where; which repo holds the
freeze marker; `repo-audit.py`'s `ROOT`). Answer them in one repository first.

### Close

- [x] 10. Update `ResearchSystem/HARNESS-LEDGER.md` (120-line cap — an addition owes a deletion),
      move `HD-11`, `HD-12`, `HD-14`, `HD-17` from `§live` to `§implemented` **in the same commit as
      the change that implements each** (`HD-2`), and retire the `batch:A`-scoped ones when A2
      finishes. `HD-13` retires with the batch (it is a do-not, carried by nothing else).
      **`HD-10` / `HD-15` / `HD-16` / `HD-18` stay `live`** — they belong to the split batch.
      — **done (batch close, 2026-08-10), with three deviations from this step's own text, each
      user-ruled on the full-`§live` audit the user ordered**: ① `HD-17` never passed through
      `§implemented` — it was consumed and retired directly at R0.1 (with `HD-24`), so the close
      moved only `HD-11`/`HD-12`/`HD-14` (implemented en route, at each round's closeout) plus
      `HD-13` to retired; ② `HD-18` did **not** stay live — the audit found its every forward
      clause carried (ledger split-batch backlog line · rider `CLI-hist` · this file's §R5/R6)
      and its batch-A-narrowing half consumed, so the user flipped it to `§implemented`;
      ③ `HD-10`/`HD-15`/`HD-16` stay live as ruled, with their stale "待 A2" annotations
      corrected to 待拆分批 (`HD-9`'s likewise dropped). Archive at 4+1 entries, under the
      100-line ask-user threshold.

## Acceptance (done = ?)

- R0's survival audit is recorded and the user has ruled each `AMBIG` item.
- Each of R1–R4 landed with the revert unit this file names — one commit each, **except R2,
  whose revert unit was amended 2026-08-09** (user pilot ruling + VERIFY `3b6267c` `V-2`) to its
  two commits: `7e8f920` construction + `3b6267c` repair leg, **and R3, amended the same way at
  its opening**: `cef6138` construction + `638972f` repair leg, **and R4, amended at its closeout
  (VERIFY `de8f4ef` `V-2`)**: `ed37a25` construction + `de8f4ef` repair leg.
- A future run produces no per-check CheckResult after closeout, and a closed run's absence of them
  does not raise `-CHECK-RESULT-MISSING`.
- A future run's directory carries its delta and not the shared core.
- The six rule sections are inside the instruction layer; the run-v2 README holds instantiation only.
- `HD-11`, `HD-12`, `HD-14`, `HD-17` have moved to `§implemented` with their carrier named.
- **Not in A2's acceptance**: anything that requires two repositories to exist.

## Resume pointer

当前指针: **BATCH CLOSED (2026-08-10; battery at 697).** This plan is finished — a resuming
session starts at `ResearchSystem/HARNESS-LEDGER.md`, whose backlog now leads with batch B. The reads
R1 owed are discharged (`v3-checkpoint-read-3f19561.md`; its §1 is the per-member citation
table — cite it, not `bd77fd4` §1, which itself cited `a5a04c3` for five members).
A resuming session reads `ResearchSystem/HARNESS-DECISIONS.md` §live first
(`HD-5`), then this file, then the two journals (A1's, then `batch-a2-2026-08-09.md`).
The opening cold read may cite that same record, `v3-checkpoint-read-3f19561.md` §1, for any
member whose blob is unchanged — never `bd77fd4` §1, for the reason two lines above; the
`§live` read is owed fresh each opening (rider `waiver-live` marks its one unsettled edge —
it only bites if the user grants an opening waiver).

## Notes

- **The order is now nearly forced, and that is a consequence of `HD-18`.** R2 must precede R3 (a
  shared script cannot carry per-run constants); R0.1 gates nothing here but feeds the split batch;
  R1 and R4 are independent of both and of each other. **The one genuine ordering choice A1 agonised
  over — split first or last — disappeared when the split left.**
- **A1's own failure mode, recorded so A2 does not repeat it**: four of A1's seven questions were
  posed against the wrong object and the user caught all four, not the harness. The shape was always
  the same — A1 measured an object's role in its own argument before measuring the object (its
  format, its consumers, whether it is a copy). **Before any A2 round measures a thing's cost,
  measure the thing.**
