# V3 review — FULL — subject `7dd027e`

**Subject range** `eab00f79..7dd027e2` — 2 commits, both this round's: `cef6138` (A2-R3
construction) and `7dd027e` (the plan tick + revert-unit amendment + the `~70→100` correction).
Nothing else is in the range; the previous round had already closed at `eab00f7`.

**Verdict: `CHANGES_REQUIRED`** — 1 blocker, 2 low findings, 4 observations.

Everything this round measured is true and everything it built works. I re-ran all nine battery
legs at the subject tip and every number in `cef6138`'s body reproduces exactly. I proved the two
new tests bind by killing them with both named mutations, and I confirmed the negative control —
the twelve pre-existing tests in the same file survive both, which is the rider's "survived the
649-test battery" claim re-derived rather than accepted. I invoked four of the five shared scripts
**in place** from the template path and they work, including one end-to-end run of the authoring
gate against a real closed run. The README's central operational claim is therefore true of the
code.

What fails is the same class the previous round's `B-1` failed on, one round later and in the
opposite direction: the round rewrote `templates/run-v2/README.md` to say the five scripts are
called in place with **zero copies**, and left three of those five scripts — in the same directory,
inside this round's own declared revert unit — opening with `Copy into ``runs/<run-id>/``` . The
operator instantiating a run reads the script, not only the README. `HD-11`'s whole content is
"a run no longer carries copies of the template scripts", and the closeout is about to promote
`HD-11` to `§implemented` on the strength of the template carrying that rule. Three of five
template scripts currently carry its negation.

## 1. What this round is, re-derived

Nothing below was taken from the dispatch, which handed me a range and nothing else.

- **Round.** A2-R3, `HD-11` part two ("extract the shared core"), step 6 of
  `.goals/plans/harness-a2-construction.plan.md`. Both commits in range name it; the plan's status
  line and Resume pointer put R0–R2 closed and R3's FULL pending.
- **Budget (`E9`).** One FULL, at most one user-approved fix, one targeted VERIFY. Applying `E9`'s
  own test — *has a valid independent FULL already occurred?* — the answer is no, so this document
  is the FULL and nothing before it consumed anything.
- **Authorization.** The plan records a user-approved preview re-presented at the R3 opening and a
  user-approved amendment of the revert unit (`pilot` = the template's own suites on synthetic runs,
  mirroring R2's `O-1` amendment). Both live in chat plus these commit bodies; see `O-4`.
- **Obligation.** Plan step 6, as narrowed by the user-approved executor analysis: a read-only sweep
  for any mechanism assuming run-local script copies, a run-v2 README instantiation rewrite, and
  0–2 assertion tests. Standing constraints: no second repository, the eight closed runs untouched,
  `AMBIG`'s 138 files untouched.
- **Declared change boundary.** The amended revert unit — `assurance/templates/run-v2/` plus its
  suites under `tooling/tests/document_harness_review/` plus the redeemed rider row, in the one
  commit `cef6138`. I classified the four changed paths by hand:

```
M  .goals/plans/harness-a2-construction.plan.md                                (plan tick, 7dd027e)
M  ResearchSystem/HARNESS-RIDERS.md                                            (rider row, in unit)
M  ResearchSystem/assurance/templates/run-v2/README.md                         (in unit)
M  ResearchSystem/tooling/tests/document_harness_review/test_run_v2_template_fulfillment.py  (in unit)
```

  `cef6138` touches exactly the three the unit names; nothing escaped it.
- **Tier.** The change set touches `ResearchSystem/tooling/`, so `EXECUTION.md`'s
  *Regression-battery tiering* puts it in the full-battery tier, which is what the executor
  classified and ran. Agreed independently.

## 2. The implementation (`R3` — this first)

### 2.1 The shared-core claim is true of the code

The README's load-bearing sentence is that the five scripts are "called **in place** from
`ResearchSystem/assurance/templates/run-v2/` against the run directory, zero copies", that "every
one takes the run directory as its first argument", and that "every one of the five reads its
per-run constants from the run's own `control/` JSON". I checked each clause against the files
rather than against the body that claims it.

Argument surface, read from the sources:

| script | run-dir arg | repo-root override | reads from `control/` |
|---|---|---|---|
| `run_evidence_v2.py` | positional `run_dir` | `--repo-root`, default `run_dir.parents[3]` | state, work-spec, resolved-plan, fulfillment |
| `run_bind_v2.py` | positional `run_dir` | `--repo-root`, same default | state, bind-declarations |
| `run_repair.py` | positional `run_dir` | `--repo-root`, same default | state, resolved-plan, user-decision-repair |
| `check_template_instance.py` | `argv[1]` | `argv[2]`, same default | work-spec, paragraph-map |
| `make_paragraph_map.py` | `argv[1]` | `argv[2]`, same default | work-spec |

The `__file__` bootstrap the three step scripts keep (`HERE.parents[2]` → `RS_ROOT/tooling`) is the
library locator, not run data, and it resolves correctly *from the template path* — which is the
whole question this round turns on. Proven by execution, not by reading:

```
$ python ResearchSystem/assurance/templates/run-v2/run_evidence_v2.py --help
usage: run_evidence_v2.py [-h] [--repo-root REPO_ROOT] --base SHA
                          --candidate SHA --candidate-branch BRANCH
                          run_dir
$ python ResearchSystem/assurance/templates/run-v2/run_bind_v2.py --help
usage: run_bind_v2.py [-h] [--repo-root REPO_ROOT] --evidence-commit SHA
                      --bound-at YYYY-MM-DD [--emit]
                      run_dir
$ python ResearchSystem/assurance/templates/run-v2/run_repair.py --help
usage: run_repair.py [-h] [--repo-root REPO_ROOT] [--emit] run_dir
```

and end-to-end against a real run, from the template path, with no copy anywhere:

```
$ python ResearchSystem/assurance/templates/run-v2/check_template_instance.py \
      ResearchSystem/assurance/runs/p5b-claims
instruction read from: pinned revision
instruction form   : enumerated
form-conditional   : preamble gate and paragraph map skipped (SIMP-B1) — every block is inside a numbered section or Context, established above
authoring gate: PASS
exit=0
```

The three documented invocation strings in the README match the parsers exactly. The comparator
paragraph is accurate too: `EXECUTION.md:389-397` says "Copy it beside the instruction and **freeze
both in the base commit**: the materialized candidate tree must carry the comparator", and
`compare_blocks.py:4` still says "Copy into ``runs/<run-id>/`` **before the instruction-freeze
commit**" — consistent with the README naming it the one member still copied.

I also re-derived the two sweep claims the round rests on rather than accepting them.
`grep -rni "copy\|copies\|copied\|copying"` over the four instruction-layer prose members returns
exactly three hits: `EXECUTION.md:235` ("proof-read a mechanical copy", unrelated),
`EXECUTION.md:393` (the comparator rule above, still true), and `CONSTRUCTION-CHECKLIST.md:50`
(`E4`'s scratchpad copies, unrelated). And a name grep for the five scripts across
`tooling/`, `document-harness/`, `contract/`, `schema/` and `.claude/` finds no `rsclib`, hook or
`rsc.py` consumer — only `EXECUTION.md`'s two path-agnostic mentions of the gate and the map
generator, journals, and one supersession-2 sentence about which script writes `review_ref`. Both
claims hold. What neither claim reaches is `§3`.

### 2.2 The two new guards bind — my own mutation matrix (`R8`, `E4`)

Scratchpad copy taken first and both restorations checked by digest, never `git checkout --`:

```
$ sha256sum ResearchSystem/assurance/templates/run-v2/run_evidence_v2.py /tmp/rev-scratch/run_evidence_v2.py.orig
2328d0d21be5216b3582a16eea2084874ce36a6c7d07c6b0fc3437d86c8ab093 *ResearchSystem/assurance/templates/run-v2/run_evidence_v2.py
2328d0d21be5216b3582a16eea2084874ce36a6c7d07c6b0fc3437d86c8ab093 */tmp/rev-scratch/run_evidence_v2.py.orig
```

| # | mutation | result |
|---|---|---|
| M11 | `run_dir.parents[3]` → `parents[2]` | **2 failed, 12 passed** — both new tests die on the VALUE (`'assurance/runs/tr-deriv-one' != 'ResearchSystem/assurance/runs/tr-deriv-one'`) |
| M12 | `CONTROL_ROOT` hard-coded to another run's name | **2 failed, 12 passed** — both new tests die (`'ResearchSystem/assurance/runs/p5b-claims' != …/tr-deriv-one`) |
| M13 | `CONTROL_ROOT = f"ResearchSystem/assurance/runs/{RUN_ID}"` **and** `parents[3]` → `parents[2]` | **14 passed — survives.** See `L-1` |

The `12 passed` column in M11 and M12 is the negative control and it settles a claim I would
otherwise have had to take on trust: the pre-existing fulfillment tests do not detect either
mutation, so the rider's "both survived the full 649-test battery" is re-derived, not accepted.
Restored and re-verified byte-identical, tree clean:

```
$ cp /tmp/rev-scratch/run_evidence_v2.py.orig ResearchSystem/assurance/templates/run-v2/run_evidence_v2.py
$ sha256sum ResearchSystem/assurance/templates/run-v2/run_evidence_v2.py
2328d0d21be5216b3582a16eea2084874ce36a6c7d07c6b0fc3437d86c8ab093 *…/run_evidence_v2.py
$ git status --porcelain=v1
(no output)
```

The tests themselves are clean on `E5`: every expectation is a hand-written literal
(`"ResearchSystem/assurance/runs/tr-deriv-one"`), never asked of the module, and the assertions are
whole-value `assertEqual`s, not substrings. The `wraps` spy on `cand.build_record` plus the
`observe_manifest` stub is an honest fixture — it keeps the test on path arithmetic and lets
everything downstream fail, and it says so in the docstring.

### 2.3 The rider redemption is real

`deriv-bind`'s redeem-when was "the next batch touching `run_evidence_v2.py` or its tests". This
batch touched its test suite, both named mutations now die, and the row is deleted in the same
commit — `R10`'s redemption shape exactly. The riders file diff removes that one line and nothing
else; 19 rows remain, `decl-dup` correctly retained (the bind declarations reader was not touched
this round, which the commit body discloses).

### 2.4 Battery — re-run at the subject tip, not read from the body (`E3`)

Every figure in `cef6138`'s body reproduces on the subject tree (`HEAD` = `7dd027e`, worktree clean):

```
P2 goldens              tests: 29   passed: 29   failed: 0   RESULT: OK
P4 goldens              tests: 80   passed: 80   failed: 0   RESULT: OK
P5A goldens             tests: 39   passed: 39   failed: 0   RESULT: OK
schema fixtures         cases: 58   matched: 58  unexpected: 0   RESULT: OK
harness v2              Ran 39 tests   OK
stage-control v1        20 run, 0 failure(s), 0 error(s)
rsc.py compile --check  diagnostics: 0 error(s), 0 warning(s)   exit 0
repo-audit.py           RESULT: clean (exit 0)
pytest                  683 passed in 109.44s
```

The plan's corrected template-test figure also reproduces. Per-suite, measured:

```
bind 38 · comparator 21 · paragraphs 18 · fulfillment 14 · repair 11
```

which is 100 at the opening (fulfillment 12) and 102 now — the plan's `~70 → 100` correction and its
`38 · 21 · 18 · 12 · 11` breakdown are both exact.

## 3. Blocker

### `B-1` — three of the five "zero copies" scripts still tell the operator to copy them in

**Location.** `ResearchSystem/assurance/templates/run-v2/run_evidence_v2.py:4`,
`run_bind_v2.py:4`, `run_repair.py:4` — all three inside this round's declared revert unit.

**Verbatim, all three, unchanged by this round:**

```
run_evidence_v2.py:4:Copy into ``runs/<run-id>/`` and run it against that directory — there is no CONFIG block
run_bind_v2.py:4:Copy into ``runs/<run-id>/`` and run it against that directory — there is no CONFIG block
run_repair.py:4:Copy into ``runs/<run-id>/`` and run it against that directory — there is no CONFIG block to
```

**What it violates.** `README.md:5-9`, rewritten by this round, states the opposite of these three
lines about these three files:

> as of the shared-core round (A2-R3, `HD-11` part two, 2026-08-09) that no longer means copying
> the step scripts in. The five shared scripts — `run_evidence_v2.py`, `run_bind_v2.py`,
> `run_repair.py`, `check_template_instance.py`, `make_paragraph_map.py` — are called **in place**
> from `ResearchSystem/assurance/templates/run-v2/` against the run directory, zero copies.

and `README.md:20-21` names `compare_blocks.py` "the **one** template member still copied". Behind
the README stands `HD-11` itself — *run 不再各自携带模板脚本抄件* — which is the ruling this round
exists to land and which the closeout is about to move to `§implemented` on the ground that the
template carries it. Three of five template scripts carry its negation. The plan's own acceptance
line, "A future run's directory carries its delta and not the shared core", is the criterion these
sentences work against.

**Failure scenario, concrete.** A run author instantiates the next run. `EXECUTION.md`'s authoring
gate points them at `check_template_instance.py`; the natural next move is to open the step script
they are about to run. Line 4 tells them to copy it into `runs/<run-id>/`. They copy — and the run
directory carries the shared core, which is the exact state `HD-11` abolished and the state A1
measured as costing ≈883 duplicated lines per run with 17 of 23 copies already forked. Nothing
refuses it (see `L-2`), and the divergence is discovered the way every previous one was: rounds
later, by measurement.

This is not recoverable from adjacent text: the sentence is the *first instruction* in the file,
it is affirmative rather than merely stale, and the README that contradicts it is a different file
the author has no reason to re-read at that moment.

**Minimum fix.** The three sentences change. No code, no test, no new machinery: I confirmed no
test in the five template suites pins these docstrings (`grep -rn "Copy into\|__doc__"` over
`test_run_v2_template_*.py` returns nothing), and `argparse` only surfaces each docstring's *first*
line in `--help`, so the three usage banners above are unaffected. `compare_blocks.py:4` must be
left alone — it is the one file for which the sentence is still true.

**Why this is a blocker and not a low.** Its fix changes an actor's action (whether the next run
copies the shared core), and the `§implemented` promotion queued at closeout turns on the answer.

## 4. Low findings

### `L-1` — the new tests bind `REPO` only through `CONTROL_ROOT`, and the docstring claims more

`test_repo_root_defaults_to_the_run_directorys_fourth_parent`'s docstring says "no `--repo-root` on
argv, so REPO must come from `run_dir.parents[3]`". What the assertion actually pins is the
`control_root` string the spy observes. The two are the same fact only while
`CONTROL_ROOT = run_dir.relative_to(REPO)` — the moment that derivation is replaced, `REPO`'s
default is unguarded again. M13 above demonstrates it: hard-coding the standard prefix per run
*and* breaking `parents[3]` passes all 14 tests. The `parents[3]` half of `deriv-bind` is therefore
guarded only transitively.

**Downstream decision that goes wrong.** The rider row is deleted, so the next batch touching
`run_evidence_v2.py` reads the derivation as covered and refactors the control-root line freely,
silently un-guarding the repo-root default. **Not a blocker:** the rider named M11 and M12 and both
die; and a wrong `REPO` still fails loudly downstream at
`subprocess.run(["git", "-C", str(REPO), "add", CONTROL_ROOT], check=True)`, which is the rider's own
stated honesty boundary. **Minimum fix** is one sentence in the test docstring stating what the
assertion observes (`control_root`, hence `REPO` only while the relativization stands) — not a
third test; `E6` says a fix needing new machinery is a signal to re-question, not to add.

### `L-2` — the acceptance criterion is now carried by prose alone, and the approved warrant addresses a different risk

The plan's acceptance line is "A future run's directory carries its delta and not the shared core."
After this round the only thing standing behind it is one README section (and, per `B-1`, three
scripts saying the reverse). Nothing refuses a run that copies: `check_template_instance.py`, the
one pre-START gate, checks the WorkSpec version, the preamble mapping and the paragraph map, and
never looks at what scripts the run directory holds.

The design judgment the user approved to justify adding nothing — "`templates/` sits outside any
normal `write_scope`, so a candidate touching the shared instrument is already non-conformant" —
is sound, but it is about a candidate **modifying the template**. The risk the acceptance criterion
names is a run **copying the template in**, which writes only inside the run's own control root and
is therefore fully conformant. The warrant does not reach the case.

**Downstream decision that goes wrong.** The closeout moves `HD-11` to `§implemented`, whose test
(`HD-2`) is "细则已由 instruction/代码/模板承载". If the carrier is understood to include a
mechanism, the promotion overstates what exists. **This is not a request for a guard** — `E6`
forbids reaching for one here, and `R5` puts the should-it-exist question with the user. The
minimum honest fix is that the `§implemented` entry names its carrier accurately: prose in the
run-v2 README (once `B-1` makes the scripts agree with it), no mechanical enforcement. Fixing `B-1`
does not close this.

## 5. Observations

- **`O-1` — this round changed no script.** `run_evidence_v2.py`'s sha256 at the subject tip is
  `2328d0d2…`, byte-identical to the value the previous FULL recorded at `eec4171:110`. The whole
  shared core was already in place when R3 opened; R3's net product is one README section, two
  tests, and one rider row. The plan step it closes was authored as "split the template into shared
  core + per-run delta … ~883 shareable lines, ~45% of script bytes … do not plan a plain reference
  swap", and the user approved the narrowing at the opening. I report the shape and stop (`R5`):
  two consecutive rounds ran under `HD-11`, and the second one's work was to write down what the
  first one built.
- **`O-2` — second consecutive round whose only blocker is in its account of itself.** `eec4171`'s
  `B-1` was "the README says there is no CONFIG block, and the fourth script still has one";
  this round's is "the README says zero copies, and three scripts still say copy". Same surface
  (`templates/run-v2/`), same direction (a completion sentence outrunning the bytes beside it),
  one round apart. The round did sweep — it swept the instruction layer, `rsclib`/hooks/`rsc.py`,
  the five suites, `write_scope`, and the closed runs, and it swept the README's own numerals. The
  surface it did not enumerate is the one the previous round was blocked on.
- **`O-3` — the repo-root override is undocumented.** All five scripts accept an explicit repo root
  (`--repo-root` for the three step scripts, positional `argv[2]` for the gate and the map
  generator); the README's invocation strings omit it. Harmless while every run sits at the canonical
  depth, and the default is what `L-1` discusses. No fix owed.
- **`O-4` — authorization is chat-only, stated as a ceiling (`R7`, `R2`).** Three load-bearing
  approvals — the re-presented preview card, the revert-unit amendment, and design judgments 1 and 2
  — exist in the repository only as the executor's own assertion in `cef6138`/`7dd027e` and the plan.
  I cannot see the user's words and do not treat their absence as a block; the same condition was
  recorded at the previous VERIFY as `O-3v`. It bears on `L-2`, whose warrant I can only evaluate as
  written, not as approved.

## 6. Boundary and record conformance (run second, `R3`)

Checked, and clean unless noted.

- **`E2`.** No frozen path is written. The two contract supersessions and the 15-file
  `schema/document-assurance-v3/` pack are untouched by the range (`git diff --name-only`
  over them returns empty).
- **`E10`.** No instruction-layer member is written. I re-derived the opening cold-read claim
  mechanically rather than reading it from the body: `git diff --name-only 3f19561..7dd027e` over
  all nine member paths returns empty, so citing `v3-checkpoint-read-3f19561.md` §1 for every member
  is valid at this tip. `HARNESS-DECISIONS.md` `§live` carries ten entries; `HD-11` is the one this
  round executes, and none of the other nine is contradicted by the range.
- **`E9`.** `HEAD` is the subject tip and the worktree is clean, so no commit landed on the branch
  between the dispatch and this record. No prior FULL for R3 exists, so this document is the one
  the cap allows.
- **`E12`.** The plan records the range as base (`base_commit: 8e018e1`) plus "dispatched on this
  chore commit's tip" — a written base and an unwritten tip, which is the rule.
- **`E8`.** Explicit paths, two new commits, no amend, no push (`origin/main..HEAD` = 597, the
  pre-existing user-gated debt, unchanged by this round). Both commit bodies are dense single-topic
  paragraphs and both name their kind (construction / plan chore). The construction title is
  `feat(harness): A2-R3 —— …` rather than the `V3-<ROUND>-v1` form; that matches R1 and R2 in this
  batch and is not raised as a finding.
- **Constraints.** No second repository, no submodule, no cross-repo reference. The eight closed
  runs are untouched — their `Copy into … and fill CONFIG` docstrings are the pre-parameterization
  shape and are correctly out of scope, which is why `B-1` names only the three template files.
- **`HD-23`.** The `~70 → 100` correction is a journal/plan number, lands inside this subject, and
  reproduces exactly. It consumes no repair leg.
- **Plan bookkeeping.** The step-6 tick, the status line, the Resume pointer and the amended revert
  unit all match the tree. R2's `V-2` correction (the Acceptance "one commit each" line) survives
  this round intact: R3's amended unit is also one commit.

## 7. What this review does not establish (`R4`)

- **`make_paragraph_map.py` was not invoked.** It is the one of the five I did not exercise: it
  writes, and the only directories to write into are closed runs. Its in-place viability is
  inferred from its argv shape and from the identical pattern in `check_template_instance.py`,
  which I did run end to end — inferred, not proven.
- **No real run exercises the new model.** A2's own constraint leaves none to instantiate, so
  "a future run carries its delta and not the shared core" is `UNVERIFIABLE` today, by construction
  rather than by omission. `L-2` is about what stands behind it in the meantime.
- **The consumer sweep is name-based.** My grep for the five script names cannot see a reference
  assembled at runtime from parts. Nothing suggests one exists; I did not prove none does.
- **Mutation proves binding force, not sufficiency.** M11 and M12 die; M13 shows the boundary of
  that force. I did not attempt a mutation matrix over the other four suites.
- **Process claims are marked, not verified.** Fresh context, the dispatched construction agent,
  the executor's hunk-by-hunk acceptance, and every user approval in `O-4` are recorded as claims.

**Coverage.** Read in full: both commits' complete diff, every hunk; `templates/run-v2/README.md`;
`make_paragraph_map.py`; the argv and derivation surfaces of the other four scripts;
`CONSTRUCTION-CHECKLIST.md`; `HARNESS-DECISIONS.md`; `HARNESS-LEDGER.md`; the A2 plan;
`HARNESS-RIDERS.md`; `review_freeze_check.py`; the new test class. Sampled: `EXECUTION.md`
(authoring gate, tiering, comparator rule, and every `copy` occurrence); the previous FULL record
`v3-review-full-eec4171.md`; the retired review contract at `7011916`. Probed: all nine battery
legs, three mutations with restoration verified by digest, four in-place invocations, and the
repo-wide `copy` sweep that produced `B-1`.

**Recompute list** — figures a later change invalidates: the nine battery numbers, the per-suite
counts `38 · 21 · 18 · 14 · 11`, the sha256 `2328d0d2…`, the 19 remaining rider rows, and the
nine-member unchanged-since-`3f19561` result.
