# V3 review — FULL — subject `eec4171`

**Subject range** `fbcb035e..eec41711` — 7 commits, of which **2 are this round's construction**
(`7e8f920` the R2 parameterization, `eec4171` the plan tick) and 5 close out the previous round
(`e27641e` VERIFY record, `7ea3566` VERIFY disposition, `3f19561` R1 closeout, `d03bf9f` layer-read
record, `51c81bb` layer-read accounting).

**Verdict: `CHANGES_REQUIRED`** — 2 blockers, 4 low findings, 5 observations.

The code is good. The parameterization is correct where it landed, the two rider redemptions are
real and I proved them by mutation, the whole battery reproduces the commit body's numbers exactly,
and ten of my fourteen mutations die on a VALUE assertion. What fails is narrower and entirely in
the round's **written account of itself**: two texts now assert a completion state the repository
contradicts. `HD-11` part one is "replace *edit the file, fill the CONFIG block* with *read config,
pass arguments*", and its own basis names **four** CONFIG-carrying scripts and eight constants. Three
scripts and six constants were converted. The fourth script — `compare_blocks.py`, holding exactly
the two constants (`SOURCE`, `SITES`) the plan step names and did not convert — sits untouched in the
same template directory whose README this round rewrote to say **"there is no CONFIG block to fill"**,
and the plan closed the step with a measured correction (`SOURCE`/`SITES` "stay in the per-check
argv") that four committed check specs falsify. Separately, the layer-read accounting commit declared
a two-pointer fix and delivered one, leaving the plan's Resume pointer contradicting itself two lines
apart and still authorising the citation its own read record had just ruled wrong.

Both blockers are text-side and both are cheap. Neither asks for new machinery; each asks that a
sentence stop claiming something the tree does not carry (`E6`: when a finding names existing text as
wrong, the fix is that text changing).

---

## 1. What this round is, re-derived

Nothing below is taken from the dispatch, which carried the range and one operational note and
nothing else (`R2`).

| Question | Answer | Where I read it |
|---|---|---|
| Round | **Batch A / A2 · R2** — `HD-11` part one: parameterize before sharing (plan steps 4 and 5) | `.goals/plans/harness-a2-construction.plan.md` §Steps R2; `7e8f920` body |
| Governing instructions | `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` (E1–E12 / R1–R10). The `v3-harness-review-contract.md` the prompt named is a 5-line stub that names the checklist as both my standing instruction and its own counterpart | review-contract stub `:3`; checklist header `:9-12` |
| Standing rulings | `HARNESS-DECISIONS.md` §live read in full at the subject: `HD-24 · HD-23 · HD-10 · HD-18 · HD-15 · HD-16 · HD-11 · HD-12 · HD-13 · HD-9`. `HD-11` (`scope: batch:A`, `live`, "待 A2 的 T1") is this round's warrant | `HARNESS-DECISIONS.md:26-121` |
| Budget position (`E9`) | This **is** the FULL. `grep -rl '7e8f920\|eec4171\|A2-R2'` over the 110-entry record directory returns nothing; no prior independent FULL of R2 exists. One user-approved fix + one targeted VERIFY remain | `grep` + `git log` |
| Verdict domain | FULL → `REVIEWED_NO_BLOCKER \| CHANGES_REQUIRED \| SPEC_GAP` (`R3`) | checklist `R3` |
| Authorization | `HD-11` carries `· user ·` 2026-08-08 and is `live`. The R2 preview card and its approval are **not** in the repository; the plan pre-authorises steps 4–5 and their revert unit. Ceiling stated below (`R7`) | `HARNESS-DECISIONS.md:91-96`; plan `:100-119` |
| Obligations | Replace CONFIG-filling with read-config/pass-arguments for `RUN_ID` / `BASE` / `CANDIDATE` / `CANDIDATE_BRANCH` / `REPAIR_ROUND` / `EVIDENCE_COMMIT` / `SOURCE` / `SITES`; cut the three `__file__`-derived roots over to an explicit run-directory argument; must precede R3; revert unit = `assurance/templates/run-v2/` plus one pilot run, in one commit | plan `:100-119`; `HD-11` 后果 |
| Ledger state | Batch A row: A2 in progress, R0.1 paid, R1 closed, "下一步 = R2（模板参数化）" | `HARNESS-LEDGER.md:91-96` |
| Freeze state | `.harness/review-pending.json` carries exactly this range, `dispatched_at 2026-08-09T04:26:38+00:00` = 14:26:38+10:00, 12 s after the tip commit `eec4171` (14:26:26). `git status --porcelain` empty, `HEAD == eec4171`. The branch has taken no commit since dispatch (`E9`) | marker + `git log` |

**Ceiling (`R7`).** The `E11` preview card for R2, its user approval, R2's opening `E10` cold read,
and the "frozen work order" the commit body says the construction agent worked from all exist only
in chat. I see no committed trace of any of them and do not treat their absence as a block. What I
can say from the repository: at `eec4171` all nine instruction-layer blobs are byte-identical to the
ones `v3-checkpoint-read-3f19561.md` §1 tabulates, so an opening citation was *available*; whether it
was made is not visible to me. "Fresh context" is marked, not verified (`R4`).

**Read coverage (`R4`).** Read **in full**: the three changed template scripts, both changed test
files, `templates/run-v2/README.md`, `compare_blocks.py`, `make_paragraph_map.py`,
`check_template_instance.py`, the plan, `HARNESS-DECISIONS.md`, `HARNESS-LEDGER.md`,
`HARNESS-RIDERS.md`, `CONSTRUCTION-CHECKLIST.md`, the seven commit bodies, and
`v3-checkpoint-read-3f19561.md` §1. Read **sampled**: `review_subject.py` (`read_control_plane`,
`check_subject`), `candidate_path_check.py`, `review_freeze_check.py`, `EXECUTION.md` around the
tiering and stage-marker sections, `batch-a1-2026-08-08.md` §3.2–3.3, `batch-a2-2026-08-09.md`
headings. Only **probed**: `v3-review-verify-fbcb035.md` and `d03bf9f`'s body (I did not re-adjudicate
R1 — it closed before this range's first commit); the eight closed runs' script copies; `rsclib`
internals below the call sites named here.

---

## 2. The implementation (`R3` — this first)

### 2.1 What the parameterization actually does

All three scripts take the same shape: a positional `run_dir`, an optional `--repo-root` defaulting
to `run_dir.parents[3]`, and everything else either derived or read from the run's own `control/`.

| Was (CONFIG constant) | Is now | Where |
|---|---|---|
| `RUN_ID = "<run-id>"` | `run_dir.name` | all three |
| `CONTROL_ROOT = f"…/runs/{RUN_ID}"` | `run_dir.relative_to(REPO).as_posix()` | all three |
| `CONTROL = HERE/"control"`, `EVIDENCE = HERE/"evidence"`, `REPO = RS_ROOT.parent` | derived from `run_dir` / `--repo-root` | all three |
| `REPAIR_ROUND = 0` (a knob in **two** scripts, hand-synced) | `assurance_state.load(CONTROL/"state.json")["repair_round"]` | evidence, bind |
| `EVIDENCE_COMMIT`, `BOUND_AT` | `--evidence-commit`, `--bound-at` (required) | bind |
| `BASE`, `CANDIDATE`, `CANDIDATE_BRANCH` | `--base`, `--candidate`, `--candidate-branch` (required) | evidence |
| `FULFILLMENT` dict | `control/fulfillment.json`, no default, absence = the same refusal | evidence |
| `GOVERNANCE_SCAN` + `DISCLOSURES` (shipped with a placeholder `skip_reason`) | `control/bind-declarations.json`, no default, absence or a missing key = STOP | bind |
| `if "--emit" in sys.argv` | `--emit` argparse flag | bind, repair |

Three judgments in here are right and worth naming. **(a)** Deleting the shipped placeholder
`skip_reason` is the strongest single change in the round: a template that ships a default excuse is
authoring the run's own honesty, and both the file's own docstring and the new test class say so.
**(b)** Killing the two-place `REPAIR_ROUND` removes a hand-synced mirror that four separate
behaviours hang off (file set, outcome gate, state pointer, `review_refs`). **(c)** Keeping the
`sys.path` bootstrap `__file__`-based is correct and is disclosed as deliberate — and it resolves
identically from `templates/run-v2/` and from `runs/<id>/` (`parents[2]` is `ResearchSystem` in both),
so the template can now be exercised in place. I verified (c) by loading and driving `run_repair.py`
directly from the template directory.

Two derivations I checked by hand rather than by test: `run_dir.parents[3]` is the repository root for
a run at `<repo>/ResearchSystem/assurance/runs/<id>` (four ancestors up), which matches the help
string "the run directory's fourth parent"; and `run_dir.relative_to(REPO)` raises rather than
misbehaves if `--repo-root` is not an ancestor.

### 2.2 The guards bind — my own mutation matrix (`R8`, `E4`)

I did not take the commit body's mutation account. I ran my own: fourteen mutations, each applied in
place, both suites re-run, then restored from a sha256-checked scratchpad copy with the digest
re-verified after every single one (never `git checkout --`). Baseline and post-run digests are
identical:

```
b82f209b5a47515a0e43f6a45edfa494aaee895a21434d63b2346ee83a04f12a *run_bind_v2.py
2328d0d21be5216b3582a16eea2084874ce36a6c7d07c6b0fc3437d86c8ab093 *run_evidence_v2.py
0c698330575a52940a6257c6e2e01e42ba59c2ca083a719c56a566741194cfd1 *run_repair.py
```

| # | mutation (the real defect shape, not a crash) | result |
|---|---|---|
| M1 | bind: `run_dir.parents[3]` → `parents[2]` | **CAUGHT** |
| M2 | bind: `REPAIR_ROUND` hard-coded to 0 (the pre-M9 shape) | **CAUGHT** |
| M3 | bind: absent `bind-declarations.json` supplies a default `skip_reason` | **CAUGHT** |
| M4 | bind: missing-key guard neutered (`absent = []`) | **CAUGHT** |
| M5 | bind: the `sg-print` paraphrase restored verbatim | **CAUGHT** |
| M6 | bind: clean `--emit` lands on `REVIEWED`, not `AWAITING_FINAL` | **CAUGHT** |
| M7 | bind: clean `--emit` writes no `assurance_candidate_ref` | **CAUGHT** |
| M8 | bind: candidate never lands on disk (`write_canonical` → digest only) | **CAUGHT** |
| M9 | evidence: `build_claims` defaults an absent entry to `IMPLEMENTED` (defect M8's own shape) | **CAUGHT** |
| M10 | evidence: an absent `fulfillment.json` is treated as nothing owed | **CAUGHT** |
| M11 | evidence: `run_dir.parents[3]` → `parents[2]` | *survived* |
| M12 | evidence: `CONTROL_ROOT` hard-coded to a different run id | *survived* |
| M13 | repair: `run_dir.parents[3]` → `parents[2]` | *survived* |
| M14 | repair: `--emit` ignored — a dry run advances the state to `REPAIRING` | *survived* |

M6/M7/M8 are the three mutations rider `bind-emit2` was banked on, each of which previously left 632
tests green. All three now die. The failure mode is a VALUE mismatch in every case, not a test ERROR:
both suites route an exception inside `main` to `None`, so "the guard did not fire" surfaces as
`None != 1` rather than as reachability-without-binding (`R8`, C0 F2). The four survivors are §4 `L-1`
and `L-2`.

### 2.3 The two rider redemptions, verified rather than accepted

- **`sg-print`** — redeem-when was "下一批碰 `run_bind_v2.py` 的 round-0 分支", and the prescription was
  *delete the paraphrase, do not branch it a second time*. Delivered exactly: the verdict line now
  ends at "no AssuranceCandidate is bound at round 0" and `next_action` is printed as itself. Both
  verdicts are pinned against the **same** printed line, and a third test pins the deleted sentence by
  its absence in the verdict line. M5 kills it. Row deleted in `7e8f920` (`R10`: redemption = the row
  goes in the same commit). ✔
- **`bind-emit2`** — redeem-when was "下一批碰 emit 路径或 `test_run_v2_template_bind.py`", criterion
  *cover both blocks, not bolt a test onto one*. Both `--emit` blocks are now driven end to end
  through the shared `make_run` fixture, and the candidate block runs the **real**
  `S.check_assurance_candidate` over a synthetic control plane (only the result checker stays a
  stand-in, correctly, since its real form needs a repository behind the evidence commit). The
  emitted document is asserted whole. M6/M7/M8 kill it. Row deleted in the same commit. ✔
  Minor and not a finding: the criterion's literal "one helper driving both blocks" landed as two thin
  class-local helpers over one shared fixture. The defect class is closed, which is what `E7` asks.

`E5` holds throughout the new tests: every expectation is a hand-written literal, `CONTROL_ROOT` and
the digests are the fixture's own, whole structures and whole printed lines are asserted, and the only
imports are from `rsclib` — the library under its own suites — never from the template under test. The
`argv` helper deliberately never passes `--repo-root`, so the default derivation is itself under test;
that is why M1 dies.

### 2.4 Battery — re-run at the subject tip, not read from the body (`E3`)

Every figure in `7e8f920`'s body reproduces exactly on the subject tree:

```
P2 goldens            tests: 29   passed: 29   failed: 0    RESULT: OK
P4 goldens            tests: 80   passed: 80   failed: 0    RESULT: OK
P5A goldens           tests: 39   passed: 39   failed: 0    RESULT: OK
schema fixtures       cases: 58   matched: 58  unexpected: 0  RESULT: OK
harness v2            Ran 39 tests   OK
stage-control v1      20 run, 0 failure(s), 0 error(s)
rsc.py compile --check  diagnostics: 0 error(s), 0 warning(s)   exit 0
repo-audit.py         RESULT: clean (exit 0)
pytest                649 passed in 121.53s
```

The two changed suites alone are 50 (bind 38, fulfillment 12), matching the body's 22→38 and 11→12.

### 2.5 The claim about `candidate_path_check`, reproduced

The body discloses two things about the path lint. Both hold, measured through
`rsclib.document_harness.paths.unresolved_path_tokens` against the tracked index at the subject:

- the lines R2 **added** to the README yield `[]` — no new token would have been blocked;
- the file as a whole yields `['control/state.json']` — a pre-existing token that will block the next
  batch touching that line, exactly the `freeze-audit` shape the body flags for the reviewer's ruling.

I concur with banking it (§5 `O-3`). One locator is wrong — §4 `L-4`.

---

## 3. Blockers

### `B-1` — the round's two texts assert a CONFIG conversion the tree does not carry

**Location.** `ResearchSystem/assurance/templates/run-v2/README.md:6-12` and `:24`;
`.goals/plans/harness-a2-construction.plan.md:102-111` (step 4, now `[x]`) and `:180-182` (Resume
pointer).

**Ground truth.** `HD-11`'s 后果 names the work as "把「改文件填 CONFIG 块」换成「读配置 + 传参」（三份脚本
`__file__` 派生 control/evidence 根、**四份靠填 CONFIG**）", and its `basis`,
`journal/batch-a1-2026-08-08.md` §3.2, names the fourth and enumerates the constants:

> `run_evidence_v2.py` · `run_bind_v2.py` · `run_repair.py` | **绑死** …
> `compare_blocks.py` | 半绑 | `REPO = Path.cwd()` + `sys.argv`，位置不绑；**但带 CONFIG 块**
> … `RUN_ID` / `BASE` / `CANDIDATE` / `CANDIDATE_BRANCH` / `REPAIR_ROUND` / `EVIDENCE_COMMIT` /
> `SOURCE` / `SITES` 是**改文件填进去的**

At the subject, `templates/run-v2/compare_blocks.py` is untouched by this round and still carries:

- `:4` — "Copy into ``runs/<run-id>/`` and **fill CONFIG** **before the instruction-freeze commit**";
- `:48-66` — `# ---- CONFIG — fill per run ---` with `SOURCE`, `OWNERS`, `SITES`, `PROSE_APPENDS`,
  `GENERATED`, `REBUILD_ARGV`, shipped as placeholders (`"<repo-relative path …>"`, `[]`, `{}`).

`SOURCE` and `SITES` are that block's, and the plan's correction note says they "stay in the per-check
argv". They do not. All four committed check specs that invoke the comparator pass a mode flag and
nothing else:

```
runs/p4-doc/control/check-chk-compare-blocks.json      argv: [python,-X,utf8,…/compare_blocks.py,--blocks]
runs/p4-doc/control/check-chk-compare-subsections.json argv: […/compare_blocks.py,--subsections]
runs/p4-doc/control/check-chk-index-five.json          argv: […/compare_blocks.py,--index]
runs/p4-doc/control/check-chk-prose-preserved.json     argv: […/compare_blocks.py,--prose,--base,993911dc…]
```

and `runs/p4-doc/compare_blocks.py:44-70` carries `OWNERS`/`SITES` filled in as module constants. The
per-check argv carries the mode, never the constants.

**Why it is a blocker and not a low.** Three actors act on the false text.

1. **The template's instantiating executor.** The README's replaced sentence used to be true
   ("Instantiate by copying … **and filling each script's CONFIG block**"); this round replaced it with
   its negation — "there is **no CONFIG block to fill** … **each script** takes the run directory and
   the round's refs as arguments … and reads **every** per-run constant from the run's own `control/`
   JSON", closed by "A missing file or a missing key refuses the step; nothing is defaulted." The
   README never mentions `compare_blocks.py` at all, so the truth is not recoverable from adjacent
   text — it fails `R9`'s wording-level test on both legs. The consequence is not uniformly loud:
   `--blocks` and `--rebuild` crash on the placeholders, but `--prose` with `OWNERS=[]` and
   `PROSE_APPENDS={}` **passes** on any all-additions diff, i.e. a green `command_exit` CheckResult
   over a comparator that compared nothing.
2. **R3.** The plan's Resume pointer now reads "**R3** (shared core — its precondition,
   parameterization, **is now in place**)", and R2's own "Must precede R3" line explains why: "A shared
   script cannot carry per-run constants." One of the four scripts still does.
3. **Close (step 10).** `HD-11` moves to `§implemented` "in the same commit as the change that
   implements each" (`HD-2`). On the current record that will happen with a quarter of it unbuilt.

**Minimum fix.** Make the two texts true — nothing more is required of this round:

- README: scope the sentence to the three step scripts it already enumerates, and say that
  `compare_blocks.py` still carries a per-run CONFIG block (its own docstring is the reference);
- plan step 4: replace "`SOURCE`/`SITES` stay in the per-check argv" with the measured fact — they
  remain a CONFIG block in `templates/run-v2/compare_blocks.py`; the per-check argv carries only the
  mode flag — and either un-tick the step or carve `compare_blocks.py` out explicitly with a named
  successor;
- Resume pointer: state R3's precondition as met for the three step scripts and open for the fourth.

Whether `compare_blocks.py` should *also* be parameterized now, in R3, or never is the user's call,
not mine (`R5`). I report only that the text and the tree disagree.

### `B-2` — the layer-read accounting declared a two-pointer fix and landed one; the plan now contradicts itself

**Location.** `.goals/plans/harness-a2-construction.plan.md:188-190`, against `:183-185`.

**Ground truth.** `d03bf9f`'s `O-2` found that the ledger and the plan both told an opening cold read
to cite `v3-checkpoint-read-bd77fd4.md` §1, while that record's own table records five of the nine
members as *cited to* `a5a04c3` rather than read there — `v3-checkpoint-read-3f19561.md` §1 states it
directly:

> Rows 4, 5, 7, 8 and 9 are byte-identical to `bd77fd4`'s table, whose own cells record them as
> *cited* to `a5a04c3` … so that is the record where the reading happened.

`51c81bb`'s body claims the fix for both carriers: "② ledger 批 A 行与 ③ plan resume pointer 按 O-2 改锚
——opening cold read 引 v3-checkpoint-read-3f19561.md §1 的逐成员锚". The ledger row was changed
correctly (`HARNESS-LEDGER.md:94-96`). In the plan, the diff rewrote the *reads-R1-owed* sentence and
left the *opening cold read* sentence — the one the commit body names — untouched. At the subject the
Resume pointer therefore reads, two lines apart:

> … cite it, not `bd77fd4` §1, which itself cited `a5a04c3` for five members).
> …
> The opening cold read **may cite `v3-checkpoint-read-bd77fd4.md` §1** for any member whose blob is
> unchanged;

**Why it is a blocker.** It changes an obligation, so `R9` does not reach it: `E10` discharges the
opening read for an unchanged member only "by citing that record", and for five of the nine members
`bd77fd4` is not that record. A cold session obeying the surviving sentence records coverage it does
not have. That the contradiction is adjacent bounds the damage but does not remove it — and the
correction was already paid for and declared landed.

**Minimum fix.** Delete or re-anchor the surviving sentence so the plan names
`v3-checkpoint-read-3f19561.md` §1 in both places. One line.

---

## 4. Low findings

Named, not inflated — none of these would justify spending the repair on its own, and `R10`'s
weighing at closeout applies.

### `L-1` — `run_repair.py` was rewritten this round and has no test at all

The file's entire argument surface changed (CONFIG block → `argparse`, `sys.argv` scan → `args.emit`),
and `grep -rln run_repair ResearchSystem/tooling/` returns nothing. M13 (repo-root off by one) and
**M14 (`--emit` ignored, so a dry run advances the state to `REPAIRING`)** each survive all 649 tests.
M14 is the interesting one: the dry-run/emit split is the same "state transition taken without the
authorization that licenses it" class `E7` names and `bind-emit2` was banked on, and here it is
unguarded in the one step whose whole job is a gated transition.

What I can say for it: I loaded the module from the template directory and drove `main([<run-dir>])`
against a synthetic run; argv → `REPO` → `CONTROL`/`EVIDENCE` → all four document loads → the real
`flow.check_repair_decision` all worked, and the step returned 1 on my (deliberately invalid) decision
fixture. The plumbing is reachable and correct; nothing binds it.

### `L-2` — the evidence step's two new derivations are unbound

M11 (`parents[3]` → `parents[2]`) and M12 (`CONTROL_ROOT` hard-coded to a different run) both survive.
`CONTROL_ROOT` is what `git add` stages, what every state pointer's path is built from, and what the
review subject records; `REPO` is where the evidence commit is taken. Before R2 both were literals a
human wrote and a freeze reviewed; after R2 they are computed, and the computation is what can now be
wrong. **Honest bound**: both mutations fail loudly downstream at run time — a wrong `CONTROL_ROOT`
makes `git add` exit non-zero under `check=True`, and a `ResearchSystem`-rooted `REPO` produces a
`control_root` that `check_subject`'s `-CONTROL-ROOT-MISMATCH` compares against the CandidateRecord.
That is why this is a low and not a blocker. The bind step's equivalent derivation *is* pinned (M1),
by the whole-document assertion; the evidence step has no counterpart.

### `L-3` — the declarations path is spelled twice in `run_bind_v2.py`

`:70` `DECLARATIONS = "control/bind-declarations.json"` is used only in two STOP messages, while the
path the code actually reads is built independently at `:276` as `CONTROL / "bind-declarations.json"`.
Two landing points for one fact, introduced in the same commit that redeemed `sg-print` for that
shape. It is the *copy* kind, not the *rewrite* kind — the lesser of the two, and today the pairing of
`test_a_missing_declarations_file_stops_the_bind` with
`test_a_complete_declarations_file_does_not_trip_the_stop` catches a divergence. Bytes supplied:
`declarations_path = run_dir / DECLARATIONS`.

### `L-4` — the disclosed lint locator is off by one screen

`7e8f920`'s body says "README:25 既有 state-file token 对 candidate_path_check 是 UNRESOLVED". The
substance is true and I reproduced it, but the token is at `templates/run-v2/README.md:32` at the
subject (`:13` before this round); neither is `:25`. `R9`-shaped — the fact is recoverable by grep —
recorded so the next batch that goes looking finds the line.

---

## 5. Observations

**`O-1` — the plan's declared revert unit for R2 was not met and not amended.** The plan says
"**Revert unit**: `assurance/templates/run-v2/` plus one pilot run, in one commit", and Acceptance
says "Each of R1–R4 landed as **one commit** whose revert unit is exactly what this file names."
`7e8f920` carries no run and does carry two files outside that directory
(`tooling/tests/document_harness_review/test_run_v2_template_*.py`); the commit declares its own,
different revert unit in its body. `eec4171` ticked steps 4 and 5 and left the Revert-unit line
untouched, with no note. The round also discloses, correctly, that no run in the repository yet
carries the two new control files. Whether a pilot run is even reachable inside A2's own constraint
("**Out — the eight closed runs**") is the user's question, not mine (`R5`); I report only that the
plan's line and the commit disagree and that neither was reconciled.

**`O-2` — the two new control documents are committed but named by no state pointer.**
`read_control_plane` enumerates the control plane from `state.json`'s pointers — "the enumeration is
the committed tree's own, never an authored list" — so a cold reviewer's entry point does not surface
`control/fulfillment.json` or `control/bind-declarations.json`. Nothing is lost, because the substance
of both is copied into documents that *are* bound (`fulfillment` → the CandidateRecord via
`fulfillment_ref`; `governance_scan`/`disclosures` → the AssuranceCandidate), and `check_subject`
enumerates no exhaustive control-file set, so the extras break nothing. Recorded because the first run
to carry them will be the first to test this, and `bind-declarations.json`'s bytes are the one input
to the candidate that no digest binds.

**`O-3` — the `freeze-audit`-shaped block the body asks the reviewer to rule on.** I reproduce it: the
sole unresolved token in the run-v2 README is `control/state.json`, pre-existing, and any future batch
that re-adds that line stages a candidate-surface Markdown file whose token resolves nowhere. It is
the same interlock rider `freeze-audit` banks. My reading is that it belongs in the bank, not in this
round; the ruling is the user's.

**`O-4` — a third thing in this run directory is now called "fulfillment".** `control/fulfillment.json`
(new: the executor's per-obligation status map) sits beside `state["fulfillment_ref"]`, which points at
`evidence/candidate-record.json`, and beside the record's own `fulfillment` block. The README's new
bullet describes the first; nothing warns the executor that the pointer with the matching name means
the third.

**`O-5` — `E1` was handled correctly and visibly.** The commit body says the construction was done by
a dispatched agent under a frozen work order and that the executor's own step was **核收** — a
file-by-file check of the change surface, spot checks of key hunks, and a battery re-run — with the
independent FULL dispatched afterwards. No verdict word is applied to the subagent's output anywhere
in the body. That is the shape `E1` asks for, and it is worth recording as a positive precedent rather
than assumed.

---

## 6. Boundary and record conformance (run second, `R3`)

**`E2` — frozen bytes.** Untouched. At `eec4171` the three frozen blobs are still
`b2dbdf75` (contract), `68031fa2` (supersession-1), `e1a2f26b` (supersession-2), and
`ResearchSystem/schema/document-assurance-v3/` is 15 files, unchanged across the range. No path in the
13-path change set is inside the freeze.

**`E10` — instruction layer.** One member is written in the range: `document-harness/EXECUTION.md` at
`7ea3566`. I read the diff line by line: five lines, nested-italic → `**bold**` on the R1 stage
marker's six section names, no clause added, no requirement changed — the free-channel application the
disposition commit describes, with the reviewer's supplied bytes. `d03bf9f` reads exactly those bytes
and says so ("`7ea3566`'s bytes have had no independent look before this one"). At `eec4171` all nine
member blobs equal their values at `3f19561`, so the read record's citation table is current.

**`E9` — budget.** The freeze window was respected in both directions inside the range: nothing landed
between `fbcb035` and the VERIFY record `e27641e`, nor between `3f19561` and the read record `d03bf9f`.
`7ea3566` (VERIFY disposition) and `51c81bb` (read accounting) are ledger/riders/plan-only and route
through the 2026-08-04 ruling and `HD-23`, consuming no fix leg. R2 itself has spent one construction
commit and this FULL; one fix and one targeted VERIFY remain.

**`E8` — git.** Seven new commits, no amends, no push (`origin/main..HEAD` is not this round's
concern). Each commit's kind is derivable from its title or body: record, disposition, closeout,
record, accounting, candidate, accounting. The two construction/accounting commits use the branch's
established `feat(harness):` / `chore(...)` title form rather than the literal `V3-<ROUND>-v1`; that is
the same shape `418b89c` carried through a FULL that returned no blocker, so I raise it as neither a
blocker nor a low. `7e8f920`'s change surface is exactly the seven files its body declares, no
untracked residue.

**`E3` — measure last.** Every figure I could re-derive, I re-derived at the tip: the nine battery
legs, the 50 tests in the two changed suites, the rider count (17 rows, `sg-print` and `bind-emit2`
gone), the ledger at exactly 120 lines with `ledger_cap_check.py` exit 0, the path-lint token sets, the
nine layer blobs and the three frozen blobs. All reproduce. One locator does not — `L-4`.

**`R6` / freeze marker.** This record is written to
`ResearchSystem/migration/document-work-assurance-v3/v3-review-full-eec4171.md`, named for the range's
tip per the precedent of `v3-review-full-065a9b8.md`, `…-22b27aa.md`, `…-0b8b824.md`. I do not commit
it; the execution side lands it, and the marker deletion rides that same commit
(`review_freeze_check.py` docstring; `E9`).

**Worktree hygiene.** Every mutation in §2.2 was restored from a sha256-checked scratchpad copy and
re-verified; the probe script lived under the gitignored `.harness/` and is deleted.
`git status --porcelain` is empty at the moment this record is written, and the three template files
digest identically to their `eec4171` blobs.

---

## 7. What this review does not establish (`R4`)

- **No product run was executed.** The three scripts are exercised by their suites and by my probes,
  never by a real run against a real repository. The round discloses this ("全仓尚无 run 携带两个新
  control 文件"), and the first run to reach the bind step is where `O-2`, `L-1` and `L-2` are actually
  paid or not.
- **The eight closed runs' copies are now a different shape from the template** by a non-constant
  delta. The body flags it as R3's problem; I did not measure it and take no position.
- **`E11` preview approval, R2's opening `E10` cold read, and the construction work order are
  `UNVERIFIABLE`** — not folded into supported, not counted against the round (`R7`).
- **R1 is not re-adjudicated.** `e27641e`, `7ea3566` and `3f19561` are in my range and I checked their
  boundary and record conformance, not their verdicts; `d03bf9f` is a read record and carries none.
- **Mutation proves binding force, not sufficiency.** The ten caught mutations show those tests hold
  the properties they name; they do not show the property set is complete. The four survivors are the
  part of the shape I can name.
