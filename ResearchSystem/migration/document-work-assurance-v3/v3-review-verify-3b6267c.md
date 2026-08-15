# V3 review — VERIFY — subject `eec4171..3b6267c`

**Subject range** `eec41711..3b6267c8` — 3 commits, linear, no merge: `e37acfb` (the FULL
record, 447 lines), `1610d94` (two bank rows), `3b6267c` (the round's one user-approved fix).
7 files, 1329 insertions, 75 deletions across the range; the fix commit alone is 5 files,
880 insertions, 75 deletions.

**Verdict: `REVIEWED_NO_BLOCKER`** — 0 blockers, 4 low findings, 5 observations.

The repair took the harder of the two roads `B-1` left open and it arrived. `HD-11` part one
is now built in **all four** CONFIG-carrying scripts and for **all eight** constants its basis
enumerates: `compare_blocks.py`'s block is gone, its six constants are CLI arguments, and
`grep -rn CONFIG` over the template directory returns only the four docstrings and the README
saying there is none. The two texts `B-1` measured as false are true of the tree I read, not
because they were softened but because the tree moved to meet them. `B-2` is closed to its
minimum fix — the plan names `v3-checkpoint-read-3f19561.md` §1 in both places, and I checked
that the record it now names really does carry a per-member table whose nine blob ids are the
nine at this tip. `L-1`'s two named mutations both die, and so do three more I invented,
including the inverse of `M14`. I ran fourteen mutations of my own: **all fourteen are caught**,
every death a VALUE mismatch against a whole structure or a whole printed line, and the two
mutated files digest identically to their subject blobs afterwards. The nine battery legs
reproduce figure for figure. `E2`'s three frozen blobs and the fifteen-file schema pack are
byte-identical across the range — the pack's tree id does not move — and no `E10` member is
written, so this range owes no layer read.

The four lows are all about what the round wrote about itself rather than what it built, and
none of them would have justified spending a repair. The one worth reading first is `V-1`: the
declarations did not merely move from a Python file to a command line, they moved into a
**schema-constrained** command line, and 14% of this repository's candidate-surface headings
cannot be written as one. Nothing committed is broken by it. Nothing written says it.

---

## 1. What this round is, re-derived (`R2`)

Nothing below is taken from the dispatch, which carried the range and one operational note and
nothing else.

| Question | Answer | Where I read it |
|---|---|---|
| Round | **Batch A / A2 · R2**, repair leg — `HD-11` part one, plan steps 4–5 | `.goals/plans/harness-a2-construction.plan.md` §R2; the three commit bodies |
| Which leg this is | The **targeted VERIFY**. `e37acfb` is the FULL record (`CHANGES_REQUIRED`), `3b6267c` the one user-approved fix. `grep -rl '3b6267c\|1610d94\|A2-R2'` over the 111-entry record directory returns only the FULL record itself — no VERIFY of this repair exists | `grep` + `git log` |
| Governing instructions | `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` (E1–E12 / R1–R10). The `v3-harness-review-contract.md` the prompt named is a 5-line stub naming the checklist as both my standing instruction and its own counterpart | review-contract stub `:3`; checklist header `:9-12` |
| Standing rulings | `HARNESS-DECISIONS.md` §live read in full at the subject: `HD-24 · HD-23 · HD-10 · HD-18 · HD-15 · HD-16 · HD-11 · HD-12 · HD-13 · HD-9`. `HD-11` (`scope: batch:A`, `live`, "待 A2 的 T1") is the warrant; `HD-23` and the 2026-08-04 ruling are what let `1610d94` be riders-only without spending a leg | `HARNESS-DECISIONS.md:26-121` |
| Verdict domain | VERIFY → `REVIEWED_NO_BLOCKER \| SPEC_GAP` (`R3`) | checklist `R3` |
| What was authorized, and by whom | The user's REPAIR decision of 2026-08-09, quoted in `3b6267c`'s body — 「既然都是执行问题，按建议」 — taking `B-1` **fix (a)** (complete the conversion, not merely correct the text), `B-2`, `L-1`, and the `O-1` plan sentence; `L-2`/`L-3` excluded and banked. A second user ruling of the same date, recorded in the plan itself, redefines R2's pilot | `3b6267c` body; plan `:126-135` |
| What the work was obliged to do | Close `B-1` and `B-2` to at least their minimum fixes; bind `L-1`'s two surviving mutations; amend the R2 revert unit under the pilot ruling. Permanently: `E2` freeze, `E10` layer, `E8` git, `E9` cap, `R10` row format | FULL §3–§4; checklist |
| Ledger / plan state | Plan: steps 4 and 5 `[x]`, R3/R4 and step 10 open. Ledger batch-A row: A2 in progress, R0.1 paid, R1 closed, "下一步 = R2". Neither is written in this range | `HARNESS-LEDGER.md:91-96`; plan `:100-207` |
| Freeze state | `.harness/review-pending.json` carries exactly this range, `dispatched_at 2026-08-09T05:34:46+00:00` = 15:34:46+10:00, **2 s** after the tip commit `3b6267c` (15:34:44). `git status --porcelain` empty, `HEAD == 3b6267c`, no commit since dispatch (`E9`) | marker + `git log` |

**Ceiling (`R7`).** The `E11` preview card for the repair leg, the finding-disposition table the
executor put to the user, this session's opening `E10` citation, and the "frozen 施工单" the
construction agent worked from exist only in chat. I see no committed trace of any of them and
do not treat their absence as a block. What the repository does carry: the user's REPAIR wording,
quoted; the pilot ruling, in the plan; and every finding's disposition, distributed across the
three commit bodies (see `O-3v`). "Fresh context" is marked, not verified (`R4`).

**Read coverage (`R4`).** Read **in full**: `compare_blocks.py` at both ends of the range,
`run_repair.py`, `templates/run-v2/README.md`, both new test files, the plan, the FULL record,
`CONSTRUCTION-CHECKLIST.md`, `HARNESS-DECISIONS.md`, `HARNESS-RIDERS.md`, the three commit
bodies, and `v3-checkpoint-read-3f19561.md` §1 through its blob table. Read **sampled**:
`run_evidence_v2.py` and `run_bind_v2.py` at their argument surfaces and the declarations block
`:274-286`; `EXECUTION.md` §*Instruction authoring rules* and §*Regression-battery tiering*;
`HARNESS-LEDGER.md`'s batch-A row; `local-check-spec.schema.json`'s `commandExitConfig`;
`layer_path_check.py`'s `LAYER`; p4-doc's four check specs and its own `compare_blocks.py`
CONFIG region. Only **probed**: `rsclib` below the call sites named here; the three older
template suites (counted, not read); the eight closed runs. **Not re-adjudicated**: the FULL's
verdict on the three step scripts — I established instead that their blobs are unchanged across
this range and that their sha256 digests equal the FULL's own §2.2 baseline exactly
(`b82f209b…`, `2328d0d2…`, `0c698330…`), so its account of them still describes the tree.

---

## 2. The repair (`R3` — this first)

### 2.1 `B-1` — the conversion is real now, in all four scripts and all eight constants

`HD-11`'s 后果 names "三份脚本 `__file__` 派生 control/evidence 根、**四份靠填 CONFIG**", and its
basis (`journal/batch-a1-2026-08-08.md` §3.2–3.3) enumerates the four and the eight constants.
I checked each against the tip rather than against the round's account of it:

| constant | where it lives now | verified |
|---|---|---|
| `RUN_ID` | `run_dir.name` | three step scripts |
| `BASE` · `CANDIDATE` · `CANDIDATE_BRANCH` | `--base` / `--candidate` / `--candidate-branch`, all `required=True` | `run_evidence_v2.py:111-115` |
| `REPAIR_ROUND` | `state.json` | evidence + bind |
| `EVIDENCE_COMMIT` | `--evidence-commit`, `required=True` | `run_bind_v2.py:160` |
| `SOURCE` · `SITES` | `--source` / `--site`, refused when absent | `compare_blocks.py:70-75, 258-265` |

`grep -rn CONFIG` over the template directory's `.py` and `.md` files returns six hits, and all six
are the *denial* — the four scripts' docstrings, plus the README's opening sentence and its
`:69` "no CONFIG knob since R2". The block that `B-1` measured — `:48-66`,
`SOURCE`/`OWNERS`/`SITES`/`PROSE_APPENDS`/`GENERATED`/`REBUILD_ARGV` shipped as placeholders — is
deleted, and with it the `sys` import that only `REBUILD_ARGV`'s default needed. The comparison
algebra is untouched: every hunk in `mode_blocks`, `mode_prose` and `mode_rebuild` is a module
constant becoming a parameter, nothing else moved. That is the minimal shape (`E6`), and it is
why the p4-doc lineage's two `VERIFIER_FIX` repairs survive intact.

**The three actors `B-1` named, re-checked.** (1) *The instantiating executor*: the README's
sentence is now scoped — "no CONFIG block to fill **in any of the four** scripts … **each of the
three step scripts** takes the run directory", with `compare_blocks.py` given its own paragraph
as "the fourth script". True of the tree. (2) *R3*: the Resume pointer's "R3 — its precondition,
parameterization, is now in place" is true for all six template scripts; I confirmed the two the
journal classified as 不绑 (`check_template_instance.py`, `make_paragraph_map.py`) still take
their run directory as argv. (3) *Close*: `HD-11` part one is whole, so step 10 will move a
built thing.

**Nothing existing breaks.** `runs/p4-doc/compare_blocks.py` is the only run-local copy in the
repository and its blob is unchanged across the range (`21da325c`). No checker compares a run's
copy against the template's bytes — I grepped `rsclib/document_harness/` and
`check_template_instance.py` for any such comparison and found none. The four frozen p4-doc
check specs bind that copy, not the template.

**The `B-1` ground truth reproduced.** I re-derived the fact the plan's old note denied, from the
four committed specs rather than from either record:

```
check-chk-compare-blocks.json      argv: [python,-X,utf8,…/p4-doc/compare_blocks.py,--blocks]
check-chk-compare-subsections.json argv: […/compare_blocks.py,--subsections]
check-chk-index-five.json          argv: […/compare_blocks.py,--index]
check-chk-prose-preserved.json     argv: […/compare_blocks.py,--prose,--base,993911dc…]
```

Mode flag only, plus the base sha for `--prose`; zero constants. `--index` is a p4-doc run-local
mode the template carries in neither version — the round says so and it is true.

**The disclosed semantic change is the only one.** `REBUILD_ARGV` was
`[sys.executable, "-X", "utf8", "<generator>", "<args>"]`; the command is now taken verbatim from
the declaration, naming its own interpreter as a check spec's argv does. Disclosed in the commit
body, the `--rebuild-argv` help and the docstring. I diffed the remaining bodies line by line and
found no second behavioural change. `V-1` is the cost that was *not* disclosed.

### 2.2 The guards bind — my own mutation matrix (`R8`, `E4`)

I did not take the commit body's mutation account. Fourteen mutations, each applied in place from
a sha256-checked scratchpad copy held **outside the repository**, both suites re-run, then the
file restored from that copy (never `git checkout --`) with the digest re-verified after every
one. Baseline and post-run digests are identical:

```
2a3bee33f078027561d1581d09d525f4788823b6b55aebf7ba6300f48f325914 *compare_blocks.py
0c698330575a52940a6257c6e2e01e42ba59c2ca083a719c56a566741194cfd1 *run_repair.py
```

| # | mutation (the real defect shape) | result |
|---|---|---|
| C1 | every `REQUIRED_PER_MODE` entry emptied — the pre-repair no-guard shape | **CAUGHT** (7 failed) |
| C2 | **the exact `B-1` defect**: `--prose` no longer requires `--owner`, so it compares nothing | **CAUGHT** (1 failed) |
| C3 | `--rebuild` no longer requires a command — deletes the generated files, rebuilds nothing | **CAUGHT** (1 failed) |
| C4 | a frozen mode spelling renamed (`--blocks` → `--block`) | **CAUGHT** (9 failed) |
| C5 | `--site` short of an anchor padded instead of refused | **CAUGHT** (1 failed) |
| C6 | an argv naming no mode accepted (`required=False`) | **CAUGHT** (1 failed) |
| C7 | `--rebuild-argv` stops swallowing its own option-shaped tokens (`REMAINDER` → `+`) | **CAUGHT** (2 failed) |
| C8 | the CONFIG regression: `--source` parsed, the old placeholder compared against | **CAUGHT** (3 failed) |
| C9 | the per-mode requirement loop made dead code | **CAUGHT** (7 failed) |
| M14 | repair: `--emit` ignored — a dry run advances the state to `REPAIRING` | **CAUGHT** (3 failed) |
| M14b | repair: the inverse — an authorized run never advances | **CAUGHT** (5 failed) |
| M13 | repair: repo-root default off by one (`parents[3]` → `parents[2]`) | **CAUGHT** (3 failed) |
| M15 | repair: the real gate's verdict ignored | **CAUGHT** (2 failed) |
| M16 | repair: the recorded pointer drops its repository-relative control root | **CAUGHT** (5 failed) |

`M13` and `M14` are the two the FULL banked `L-1` on; both die. `C2` is `B-1`'s own measured
consequence; it dies. **All fourteen die on a VALUE assertion, not a test ERROR** — I re-ran the
four that matter most with `--tb=line` and read the failures: `M14` on a whole-state-dict
comparison and a whole printed-line list; `M13` on the whole wrong path
(`'c/runs/tr-seven/…' != 'b/c/runs/tr-seven/…'`); `M15` on `0 != 1`; `C2` on the whole FAIL line
(`['FAIL: git diff failed (exit 128)…'] != ['FAIL: --prose needs --owner; …']`). `C2` is worth
naming precisely: under the mutation the step still exits 1, for an unrelated reason, and only
the **whole-line** assertion separates the two — `E5`'s "assert the whole line, never a substring"
is doing real work there rather than being a stylistic habit.

`E4`'s negative controls are present and are not decorative:
`test_an_explicit_root_reproduces_the_derived_one` pairs the derivation with the explicit answer;
`TheComparisonRunsOnWhatTheArgvNamed`'s passing case pairs the two failing ones;
`test_the_emitting_run_says_which_round_it_moved_to` asserts both the presence of the emit line
and the **absence** of the dry-run line, which is what makes `M14b` die five times over.
`E5` holds: every expectation is a hand-written literal, and the one computed value — the
decision file's digest — is computed from the fixture's own serialisation via `rsclib`, disclosed
in the docstring as such.

### 2.3 `B-2` — one record named in both places, and it is the right record

The FULL's minimum fix was "delete or re-anchor the surviving sentence so the plan names
`v3-checkpoint-read-3f19561.md` §1 in both places. One line." Delivered as one sentence:

> The opening cold read may cite that same record, `v3-checkpoint-read-3f19561.md` §1, for any
> member whose blob is unchanged — never `bd77fd4` §1, for the reason two lines above;

The `§live`/`waiver-live` clause is untouched, as the body claims. The contradiction is gone: both
sentences in that paragraph now point at the same record.

A VERIFY has to check the substituted claim, not just the substitution. `v3-checkpoint-read-3f19561.md`
§1 does carry a **per-member** citation table with a blob id per row, and `E10` makes citation
depend on exactly that. I compared its nine blob ids against `git rev-parse 3b6267c:<member>` for
all nine members: `44d622b9 · dab9f71a · 8bbd330f · 3350bfac · 17ff31bb · 52a97a48 · 68031fa2 ·
e1a2f26b · 09aa8699` — identical, member for member. The citation the plan now authorises is
current at this tip.

### 2.4 `L-1` — the repair step has tests, and they hold the property it names

11 tests in three classes. The property under test is stated as behaviour, not spelling: "the
state file changes only when `--emit` says so, and when it does the pointer it gains is built
from the run's repository-relative control root." Three things I checked beyond the mutations:

- **`run_repair.py` itself was not touched.** Its blob is unchanged across the range and its
  sha256 equals the FULL's §2.2 baseline. The fix is tests only, which is what `L-1` asked for and
  what `E6` would have refused had the fix instead added machinery.
- **The gate is the real one.** `TheGateIsTheRealOne` drives `flow.check_repair_decision` over a
  schema-shaped fixture rather than a stand-in, so `M15` — the gate's verdict ignored — dies. A
  stand-in would have agreed with the template by construction.
- **The depth sensitivity is asserted as a fact, not as a refusal.**
  `test_a_run_planted_at_another_depth_takes_a_root_that_is_not_the_repository` pins the *wrong*
  path a shallower run produces, and its docstring says why: the derivation cannot refuse this.
  That is the honest bound `R4` asks for, written into the test rather than into a record.

Every one of the six template scripts now has at least one suite naming it — `run_repair.py` and
`compare_blocks.py` were the two that did not, and both gained one here.

### 2.5 `O-1` — the revert unit is amended, and the original is preserved

The line records the amendment rather than replacing the text `O-1` measured against: the original
sentence is quoted, the 2026-08-09 user ruling is named, the reason is given (A2's own *Out — the
eight closed runs* leaves no run to pilot on), and the new unit is stated —
`assurance/templates/run-v2/` plus its suites under `tooling/tests/document_harness_review/`,
across `7e8f920` and this repair. That is a better record than a rewrite would have been. It also
leaves a sibling sentence behind: `V-2`.

### 2.6 The bank, and where the four lows went

Four lows, four dispositions, all traceable in the repository: `L-1` into the fix; `L-2` and `L-3`
into `HARNESS-RIDERS.md` as `deriv-bind` and `decl-dup` (rows 17 → 19); `L-4` disposed of by the
FULL itself as `R9`-shaped, and in any case unfixable — it names a figure inside `7e8f920`'s
immutable commit body.

Both new rows meet `R10`'s format: one row each, `what · redeem-when · source`, each naming a
target file (`run_evidence_v2.py`; `run_bind_v2.py`'s declarations read and its STOP messages)
rather than a vague surface, each with a touch condition. `decl-dup` carries the exact bytes the
FULL supplied. I verified the banked ground truth is genuinely still there and was not quietly
fixed: `run_bind_v2.py:70` still declares `DECLARATIONS` for the two STOP messages while `:276`
independently rebuilds `CONTROL / "bind-declarations.json"`.

`decl-dup`'s routing is the one that needed a second look. `R10`'s three-channel sentence sends "a
middle low whose record supplies the exact bytes" to the `E10` free channel "never the bank" — but
that sentence is scoped to lows **from reads**, and the free channel is an instruction-layer
mechanism, which `run_bind_v2.py` is not. Banking is therefore correct, and the harness has
already recorded exactly this reading in rider `R10-route`'s second leg. No `SPEC_GAP`: the
question is asked and banked, not unanswered.

### 2.7 The battery, re-run at the tip (`E3`)

All nine legs, run by me on the subject tree, against the nine figures `3b6267c`'s body claims:

```
P2 goldens            tests: 29   passed: 29   failed: 0    RESULT: OK
P4 goldens            tests: 80   passed: 80   failed: 0    RESULT: OK
P5A goldens           tests: 39   passed: 39   failed: 0    RESULT: OK
schema fixtures       cases: 58   matched: 58  unexpected: 0  RESULT: OK
harness v2            Ran 39 tests   OK
stage-control v1      20 run, 0 failure(s), 0 error(s)
rsc.py compile --check  diagnostics: 0 error(s), 0 warning(s)   exit 0
repo-audit.py         RESULT: clean (exit 0)
pytest                681 passed in 105.64s
```

Every figure reproduces. The two new suites are 32 of the 681 (comparator 21, repair 11), which is
exactly the 649 → 681 delta the body claims. `ledger_cap_check.py` exits 0 at 120 lines.

The round's path-lint disclosure also reproduces, measured through
`rsclib.document_harness.paths.unresolved_path_tokens` against the tracked index at the tip: the
**11 lines this repair added to the README yield `()`**, and the file as a whole yields
`('control/state.json',)` both before and after — the pre-existing token the FULL logged as `O-3`.
The three new `control/` filenames named in the README's specification list resolve or are exempt;
none of them is a new blocker for the next batch touching that file.

---

## 3. Findings

Four lows. None is a blocker, none is a `SPEC_GAP`, and `R10`'s weighing at closeout applies to
each.

### `V-1` — the declarations moved onto a schema-constrained command line, and no text says so

**Location.** `ResearchSystem/assurance/templates/run-v2/README.md:27-33`;
`compare_blocks.py:28-46` (the Modes block) and `:261-271` (the `--site` / `--prose-append` help).

**What changed.** Before the repair, `SITES` and `PROSE_APPENDS` were Python literals in the run's
own copy of the comparator: any string was expressible. After it, they are tokens in the check
spec's `argv` — and `local-check-spec.schema.json`'s `commandExitConfig` constrains every argv item
to `"pattern": "^[^`$|;&<>\\n\\r]*$"` with `"maxLength": 500`. A `--site` anchor or a
`--prose-append` prefix is a **line taken verbatim from a real markdown document**, so this is not
a theoretical class.

**Measured.** Over `Thesis/`, `ExperimentLab/` and `ResearchSystem/` (excluding `runs/` and
`migration/`): **329 of 2313 markdown headings — 14%, across 126 files — contain one of those
characters** and therefore cannot be written as a check-spec argv token. Seven of them sit inside
p4-doc's **own** owner files (`scope-and-boundary.md` 4, `sota-comparison.md` 3). p4-doc itself
survives: I evaluated its real five `SITES` and two `PROSE_APPENDS` against the pattern and the
length cap — **0 rejected**, longest token 226 characters — so nothing committed is broken.

There is a second, smaller leg. `::` is the field separator, so an anchor or a prose prefix
containing `::` cannot be declared either. `parse_site`'s docstring says so explicitly and well;
`parse_prose_append`'s does not, and neither does its help.

**Why it is a low and not more.** The failure is loud and early — the check spec fails schema
validation at freeze time — and there is a workaround, since an anchor is already chosen under a
uniqueness constraint (`line_index` demands exactly one match, and p4-doc's own comment records
picking a different anchor for exactly that reason). But the message a run would get points at a
schema pattern, not at the comparator's argument design, and the round's own disclosure list names
exactly one deliberate semantic change (`REBUILD_ARGV`) and not this one.

**Bytes appliable**, one sentence, in the README paragraph or the docstring's Modes block: a
declaration must be expressible as a check-spec `argv` token — no `` ` `` `$` `|` `;` `&` `<` `>`,
no `::` inside a field, ≤500 characters — so anchors and prose prefixes are chosen accordingly.
**Deadline**: the first run after p4-doc that binds any comparator mode. That is the moment it
bites, and it bites during instruction freeze, when the run is least able to absorb a redesign.

### `V-2` — the plan's Acceptance still says "one commit" while R2's amended revert unit names two

**Location.** `.goals/plans/harness-a2-construction.plan.md:186`, against `:126-135`.

Acceptance reads "Each of R1–R4 landed as **one commit** whose revert unit is exactly what this
file names." The amended R2 revert unit reads "…across the **two commits** this round spent:
`7e8f920` and the `B-1`/`L-1` repair commit." Before this repair the two lines agreed with each
other and both were falsified by the tree — which is what `O-1` measured. After it, the revert-unit
line is true and its sibling is not.

**The downstream decision that goes wrong.** Step 10 (Close) is checked against Acceptance. A
session running that check reads a criterion R2 does not meet, and either records A2 as accepted on
a false reading or reopens a closed round. The accurate fact is recoverable — it is 60 lines above,
dated, and attributed to a user ruling — which is why this is a low and not a blocker, and why the
fix is a clause, not a rewrite: Acceptance should say what the revert-unit line says, that a round's
unit is what this file names for it. Same defect class as `B-2`: a correction landed in one carrier
and not in its sibling.

### `V-3` — the Resume pointer's head is stale in the very paragraph the repair edited

**Location.** `.goals/plans/harness-a2-construction.plan.md:196-199`.

The paragraph opens "R2 is CONSTRUCTED (`7e8f920` … battery green at 649) and its FULL review is
**dispatched — record pending**." At this tip the FULL record has landed (`e37acfb`), two rows are
banked, the repair has landed, and the battery is 681. The repair edited the **last** sentence of
this same paragraph — there is no blank line between `:196` and `:207` — and left its first sentence
asserting a superseded state.

I weigh this as a low rather than an observation for one reason: this branch already carries the
incident. `8e018e1`'s own body records it — 「评审与 read 落地后没人回头关这份 plan，冷进它的
session 会拿到假断点」 — for the A1 plan, and it did so **on this same day**, 14 h 24 min before
the tip I am reviewing (`2026-08-09 01:10:11` vs `15:34:44`). A cold session obeying `:196-199`
looks for a record that is three commits behind it.

The mitigating fact is real and I state it: `E9`'s freeze forbids the branch any commit but this
record between dispatch and now, so the executor could not have refreshed it after `e37acfb`
without spending the window. **Deadline: this round's closeout**, which is the first commit
permitted to carry it. The same sweep owes `HARNESS-LEDGER.md:93-94`, whose batch-A row still reads
"下一步 = R2（模板参数化）" — outside my subject range, named here because it is the same sentence
in a second carrier and the closeout is the one moment both are reachable.

### `V-4` — a cross-reference that A2's own R1 invalidated was re-typed in the paragraph that was rewritten

**Location.** `compare_blocks.py:11-13` — "per the README's authoring rule, mechanically comparable
demands bind one of these modes, never a `locator_exists` proxy."

The rule it points at is not in that README. I checked `418b89c~1`: the pre-R1 README carried
*Instruction authoring rules*, including both "The comparator is a template member" and
"Mechanically comparable demands bind a comparison, not a locator proxy" — and A2-R1 moved all six
sections into `EXECUTION.md` (`:350-397`). So the reference was correct until R1 and false after it.
This repair rewrote the docstring paragraph that contains it (lines 4-13 all changed) and re-typed
the clause unchanged.

It is disclosed, which is the right instinct, but the disclosure mis-files it: 「先于本轮、非本批之
修」 reads as putting the defect outside batch A2, and it was created **by** batch A2, in its own
first round. That matters for `R10`, whose redemption trigger is "the fix rides a batch already
touching that surface" — a batch has now touched that exact paragraph twice, and the row that would
have caught it does not exist. **Bytes appliable**: point the clause at `EXECUTION.md`'s
*Instruction authoring rules*. The truth is recoverable from adjacent text — the README's own
`:75-79` notice says the sections moved — which is what keeps this a low.

---

## 4. Observations

**`O-1v` — the declarations are now inside the frozen control plane, which is a governance gain
nobody claimed.** Before, a run's comparison constants lived in a script the executor edited after
copying; they were frozen only in the sense that the file was. Now they are `argv` in a check spec —
part of the control plane the user approves at START and the reviewer re-derives from the committed
tree. `V-1` is the price of that; the gain is that a comparator's *scope* is no longer something an
executor can adjust without the change being visible as a control-plane diff. Recorded because the
round sells the change as parameterization and it is also a widening of the approval surface.

**`O-2v` — the pilot is a suite, and a suite is not a run.** The amended revert unit makes the
template's own suites the pilot, and on its own terms that holds: the comparator suite drives a
synthetic two-file tree through the real `mode_blocks`, and the repair suite builds the real
`<repo>/ResearchSystem/assurance/runs/<id>/{control,evidence}` shape so the default derivation is
itself under test. What no suite covers is a comparator invoked *the way a run invokes it* — as a
`command_exit` subprocess, with `cwd` set by the runner, against a materialized candidate tree. The
first run to bind a mode is where `V-1`, `O-2` and `L-2` are actually paid or not.

**`O-3v` — every finding's disposition is in the repository, but the table the user saw is not.**
Across the three commit bodies, all six findings and five observations are accounted for. The
artifact that determined which of them the user actually ruled on exists only in chat, and
`1610d94` discloses that it omitted `L-3` — 「此条 executor 呈表时漏报、用户未裁」. The disclosure is
what makes the omission visible at all; nothing in the repository could have caught it. I record
this as the shape rather than as a finding, because the post-hoc coverage is complete and because
`R10`'s weighing sentence is written for a FULL returning `REVIEWED_NO_BLOCKER`, which this one did
not — a `CHANGES_REQUIRED` FULL's unaccepted lows have no rule of their own.

**`O-4v` — `E1` held again, and visibly.** The construction was done by a dispatched agent under a
frozen work order; the executor's own step is named 核收 — change-surface check (exactly 5 paths,
which I confirmed) plus a battery re-run — and no verdict word is applied to the subagent's output
anywhere in the body. That is the second consecutive round with this shape (the FULL recorded the
first as its `O-5`), which is worth saying out loud before it stops being noticed.

**`O-5v` — the test surface is now larger than the thing it tests, and that is the user's question,
not mine (`R5`).** The six template scripts are 1,360 lines; the five suites that hold them are
2,375. This round contributed 712 of those lines to close one blocker and one low. I take no
position on whether that ratio is right — for a template whose copies are frozen into candidate
trees and whose defects surface rounds later, it may be exactly right. I record only that two
successive rounds have each answered a finding by adding a suite, and that R3 (shared core) will
have to decide whether the suites travel with the core or stay behind.

---

## 5. The permanent boundaries (`R3` — run second)

**`E2` — frozen bytes.** Untouched, and I checked the identities rather than the paths. At both
ends of the range the three frozen blobs are `b2dbdf75` (contract), `68031fa2` (supersession-1),
`e1a2f26b` (supersession-2) — the exact ids `E2` names. `ResearchSystem/schema/document-assurance-v3/`
holds 15 files at both ends and its **tree id is identical** (`1c33d26e`), which is a stronger
statement than a file count. No path in the 7-path change set is inside the freeze.

**`E10` — instruction layer.** No member is written in this range: all nine blobs are byte-identical
at `eec4171` and `3b6267c`, and I checked them against `layer_path_check.py`'s `LAYER` tuple rather
than against a list in a record. This range therefore owes no layer read, and the `E10` free channel
is not in play.

**`E9` — budget.** One FULL (record `e37acfb`), one user-approved fix (`3b6267c`), one targeted
VERIFY (this record). `1610d94` is riders-only — one file, two added rows — and routes through the
2026-08-04 ruling as extended by `HD-23`, spending no leg. The freeze window held in both
directions: `eec4171` → `e37acfb` is the branch's next commit with nothing between, and nothing has
landed since the marker was written 2 s after `3b6267c`. The approved fix boundary was not exceeded:
the 5 changed paths sit inside the amended revert unit plus the plan's own bookkeeping.

**`E8` — git.** Three commits, no amends (author and committer timestamps identical on all three),
no trailers, no upstream configured so no push. Each title names the round and its kind —
`V3-REVIEW-RECORD-A2-R2-eec4171-v1`, `V3-REVIEW-BANK-A2-R2-v1`, `V3-REVIEW-FIX-A2-R2-v1`. `BANK` is
not one of `E8`'s enumerated kind words, but the kind is attributable without asking and
`V3-REVIEW-BANK-A2-R1-v1` is the established precedent one round back; not a finding. Each body is
one dense paragraph.

**`E3` — measure last.** Every figure in this record is emitted by the command that produced it, at
this tip, after the last mutation was restored. One figure in `3b6267c`'s body does not reproduce as
written: the abbreviated digest 「0c698330…94d1」. The prefix is right and the file is right — the
full digest is `0c698330…1194cfd1` and `94d1` is not its tail (`94cfd1` is). `R9`-shaped and
unfixable in place, since the body is immutable; recorded so the next reader who checks the
abbreviation against the file knows why it did not match.

**Worktree hygiene.** Every mutation was applied from and restored to a sha256-checked copy held
outside the repository; both files' digests were re-verified after each restore and again at the
end. My scratchpad never entered the working tree. `git status --porcelain --untracked-files=all` is
empty at the moment this record is written; the template directory's `__pycache__` that my imports
touched is covered by `.gitignore:11`.

**`R6` / freeze marker.** This record is written to
`ResearchSystem/migration/document-work-assurance-v3/v3-review-verify-3b6267c.md`, named for the
range's tip per the precedent of `v3-review-verify-fbcb035.md`, `…-7a08265.md`, `…-a1fad7e.md`. I do
not commit it; the execution side lands it and the marker deletion rides that same commit.

---

## 6. What this VERIFY does not establish (`R4`)

- **No product run was executed.** Not one line of the parameterized comparator has run as a
  `command_exit` subprocess against a materialized candidate tree. Everything in §2 is suites and my
  own probes.
- **Mutation proves binding force, not sufficiency.** Fourteen deaths show those tests hold the
  properties they name. They do not show the property set is complete — `L-2`'s two survivors from
  the FULL are still survivors, correctly banked as `deriv-bind`, and I did not re-attempt them.
- **I did not re-adjudicate the FULL.** Its verdict on the three step scripts stands on its own
  reading; I established only that their bytes have not moved since it read them.
- **`V-1` is measured, not exhausted.** I counted headings, which is where anchors come from. I did
  not enumerate every string a future run might pass as a `--prose-append` prefix or a `--source`
  path, and the 14% is a rate over one repository at one moment, not a probability.
- **`E11` preview approval, the disposition table, and this session's opening `E10` citation are
  `UNVERIFIABLE`** — not folded into supported, not counted against the round (`R7`).

---

**Verdict: `REVIEWED_NO_BLOCKER`** — 0 blockers, 4 low findings (`V-1` `V-2` `V-3` `V-4`),
5 observations. The accepted findings are discharged: `B-1` by building the fourth script rather
than softening the sentence, `B-2` to its one-line minimum with the cited record verified current,
`L-1` by eleven tests that kill both named mutations and three more, `O-1` by an amendment that
preserves what it amends. `L-2` and `L-3` are banked with targets and triggers. The permanent
boundaries hold: `E2`'s three blobs and the pack tree are unmoved, no `E10` member is written, the
cap is intact, and the worktree is clean. `V-3` carries a deadline of this round's closeout;
`V-1` carries one of the first run to bind a comparator mode.
