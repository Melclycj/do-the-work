# Journal — round `CORE-SET-CODE` (batch `CORE-SET`, round 3), 2026-08-27

Analysis, reasoning and measurement. The round's obligations, rulings and acceptance live in
`document-harness/plans/core-set.plan.md`; its narrative lives in the two candidate commit bodies.
Neither is restated here. This is the batch's first round to touch code and tests.

## 1. The WorkSpec, because nothing else carries it

`HD-35` puts the decomposition on the executor and no plan supplied one, so it is written down
here rather than left in a session that ends. Nine obligations, each with the evidence that
answers it — which is also the shape a reviewer can walk without accepting a reported figure.

| # | Obligation | Evidence |
|---|---|---|
| G1 | The `--package` mode and every input that only fed it leave the CLI | `dtw review --help` offers `--subject` / `--result` / `--executor` / `--repo-root` and nothing else |
| G2 | The package half leaves `review.py`, together with whatever its removal forces | no `def` line for any of the nine retired callables under `tooling/rsclib/` |
| G3 | The dead `review_binding` indirection leaves `flow.py` | no definition, no `__all__` entry, no importer |
| G4 | Live pointers to retired symbols are repaired; provenance is kept | three repaired, two kept — §4 |
| G5 | `REVIEW.md`'s ruled-dangling pointer retires | the sweep's two entries at that site are gone — §2 |
| G6 | Tests retire with the leg; surviving coverage moves rather than dropping | battery 854 → 795, every unit accounted — §3 |
| H1 | The constant's **value** moves, identifier unchanged | the tuple, plus six hand-written literals across three suites |
| H2 | The prose sites naming the old directory say the new one | re-derived: two, not the three the item lists — §6 |
| H3 | The migration advice exists here and nowhere else | the round's own diff is sixteen paths, all inside this repository |

## 2. The measurement the round exists to move

Instrument `tooling/sweep_refs.py` and nothing else — round 1's rule, kept. Method: the round-2
recipe unchanged, `git archive <commit>` into a scratch tree, delete what a caller does not carry
(`document-harness/journal/`, `document-harness/plans/`, all of `migration/` except the two
retired-contract stubs that are `E10` members, and the root registers), `git init && git add -A &&
commit` so the sweep's basename resolution works, then count **only `LINK` and `PATHTOK`** —
`NAMETOK` is a backticked bare filename, the compliant form for an artifact held elsewhere.

| stripped tree at | files | real breaks over the nine members |
|---|---|---|
| `d3cda1a` — the round's base | 123 | **5** |
| `5a39945` — after items G and H | 122 | **3** |

The file count moves by one because `test_package_and_review.py` is deleted; the recipe did not
change. `NAMETOK` is 35 on both trees.

**The three that remain are ruling 12's, and remain by ruling rather than by omission**:
`CONSTRUCTION-CHECKLIST.md:6` and the two retired-contract stubs at `:3`, all three citing the same
deletion-first plan. Construction-side documents may depend on construction history; the test is
who cites, not what is cited.

**The two that closed are `REVIEW.md:93`'s** — one site reported twice, as a `LINK` and as a
`PATHTOK`. Round 1 deleted the document under ruling 13 and left the pointer dangling on purpose;
item G retires the pointer, which is what the ruling scheduled. That is acceptance 7 met exactly as
the plan predicted it, which is worth saying because the round-2 acceptance sentence had to be
corrected in the other direction.

## 3. The battery, and where all 59 tests went

`python -m pytest -q` returned **854 passed in 145.17s** at `d3cda1a` and **795 passed in 142.74s**
on the item-G tree, each run immediately before its figure was written. Item H moves literals and
retires nothing, so the tip figure is **795 passed in 140.57s**, unchanged. User ruling 26 asks for
both figures precisely so a drop from 854 does not read as lost coverage; the accounting is
therefore per unit and not per file.

| change | tests | why |
|---|---|---|
| `test_package_and_review.py` deleted | −56 | 1,461 lines, re-derived by `git show` on the base rather than taken from the plan |
| `TheVersionOneModeIsUndisturbed` | −4 | `E4`'s negative control for M10, proving `--subject` did not replace `--package`; nothing left to be a control for |
| `TheReviewCommandReportsRatherThanCrashes` | −1 | F5's pin that a schema-invalid package reached the command as a report; there is no package to hand it |
| moved into `test_golden_review_views.py` | +2 | see below |

**Why exactly two moved, and not zero or eight.** The retiring suite's `ClosedVerdictSurfaceTests`
held eight N2-A3 methods. Six needed the retired fixture builders or `check_review_result` and went
with the leg; what they covered — an unknown kind failing shut, every registered kind resolving —
is already asserted by `N2ValidatorTests` in the file the survivors moved to. The two that moved
assert against the v1 review schema alone: the contract-set enum pin and the proof-vocabulary scan.
They are kept rather than dropped because **most of what they pin is still live**. The v2 review
schema `$ref`s five `$defs` out of the v1 file — `reviewRound`, `instructionCompleteness`,
`perObligationDisposition`, `finding`, `verifyScope` — so three of the four enums in the first
method, and every leaf the second method's scan walks, are what the *successor* result is validated
against today. Dropping them would have removed live coverage under cover of a retirement.

## 4. Live pointer versus provenance — the test applied to five sites

Deleting a symbol strands every sentence naming it, and the two kinds of stranding are not the
same. A **live pointer** tells a reader to go somewhere; when the destination is gone it is simply
wrong, and it is repaired. **Provenance** says why the surviving code has the shape it has; the
retired name is part of the history that explains it, and it is kept with the retirement written in
beside it. Applied:

- repaired — `review_result_v2`'s `SpecGap` message told a user that v1 results *belong to*
  `review.check_review_result`; `review_subject.subject_binding`'s docstring called itself *the v2
  analogue of* `flow.review_binding`; `review_result_v2`'s parity-ceiling paragraph said v1's copy
  *lives in* one function and is frozen, which stopped being true when the function went.
- kept — `flow.check_repair_decision`'s comment about the fail-open shape `check_package` reported,
  and `review_subject.check_subject`'s note that it re-homes v1's `check_package` identity
  cross-checks. Both are statements about a design that really happened.

## 5. The four symbols that went beyond the plan's list, and the four that stayed inside it

Item G names seven functions and instructs the executor to decide per function. What that decision
actually turned on was reachability after the named deletions, not judgment about worth.

**Forced out.** `check_review_result` takes a package positionally and its first act is
`package_digest(package)`; deleting `package_digest`, which the plan orders, leaves it unable to
run. `PACKAGE_CODE` and `CODE` are used only inside the deleted bodies. `REQUIRED_ROLES` is the
ReviewPackage's own required-role tuple and its comment says it exists for the completeness rules
in `check_package`.

**This corrects user ruling 26's premise, and the correction is worth its own sentence.** The
ruling says `package_digest` "is reached only through `flow.py`'s `review_binding`". It was also
called at `review.py:494`, inside `check_review_result`. `git grep -n -w package_digest` on the
base returns `flow.py:48`, `flow.py:727`, `review.py:195`, `review.py:494`, `review.py:776`, plus
tests and the frozen schema's description. Nothing in the round changes as a result — the plan
still orders `package_digest` deleted and the deletion set widens by exactly what that order
forces — but a reader who takes the ruling's clause at face value will not be able to reconstruct
why four unnamed symbols left.

**Kept, deliberately.** `result_digest`, `render_result` and `accepted_findings` are result-side,
not package-bound; their subject is a ReviewResult, which v2 still has. `render_result` also
carries two committed golden files and three golden tests, so removing it would have taken pinned
user-facing output with it for nothing the round asked for. `require_valid_n2` and
`accepted_findings` had no caller at the round's base either — they are not this round's dead
surface, and a deletion this round did not cause belongs to whichever round questions them.
**Stated rather than implied:** after this round `render_result`, `result_digest`,
`accepted_findings` and `require_valid_n2` are exported by `review.py` with no caller anywhere
under `tooling/rsclib/`.

**Both v1 schema kinds stay registered, for a mechanical reason.** `N2_SCHEMA_FILES` is what puts
the v1 review schema into the N2 registry *and* into `review_subject._w2_registry`; dropping the
`review_package` entry would break the v2 validator outright, because the v2 schema `$ref`s five of
that file's `$defs`. The `review_result` pointer stays for the reason the v2 schema gives in its
own description: pinned v1 history is readable and was never migrated.

## 6. Item H: two corrections and one demonstration

**The site list is corrected by measurement.** Item H names `caller.py`'s docstrings, `REVIEW.md`'s
record channel and `ONBOARDING.md` as the prose sites naming the old directory. `ONBOARDING.md`
never named it — it speaks only of "the defaults" and of the declaration, which is the right shape
and needed no repair. It is still where the migration advice belongs, since user ruling 25 asks for
the advice where a caller meets it, so the round **adds** there instead of substituting.

**The class was swept before anything was written** (`HD-41` ④). `git grep` for the old directory
name over the whole tree, excluding history, returns 23 lines. Six are the default and move; the
other seventeen are different things wearing the same name — this repository's own construction
record channel and the stubs' own paths in `CONSTRUCTION-CHECKLIST.md`, `E10` member paths in
`layer_path_check.py`, `dispatch.py` and two test suites, and the **first caller's declaration** in
`test_caller_surfaces.py`, whose whole point since round `STRANGER-GUARDS` is that those entries
are that caller's declared surface and not anybody's default. Moving them would have deleted the
test that proves the two are different.

**The hazard was demonstrated, not argued.** `E3` requires running the command that could falsify
an assertion before writing it into instruction text, and the advice asserts a break. In a
throwaway repository outside both trees, with no declaration present and a returned review record
staged under the old directory — carrying a broken path token, which is the real shape of a record
that reports one — `candidate_path_check.py` blocked with exit 1 naming the token, and with the
freeze marker written `review_freeze_check.py` blocked with exit 1 saying "not a review record".
The same record under the new default: both exit 0. Then the stated fix, one `review_record_dirs`
line in that repository's own declaration naming the old directory: both exit 0 again with the
record still where it was. Break, control and repair, all three positions measured.

## 7. This repository's own exposure to item H

It has **no `.harness/scan-surfaces.json`** — `ls` shows only the run log — so it runs on the
values this round changed, and **151** of its own review, cold-read and checkpoint-read records sit
under the old directory. Its commits are unaffected, and not by luck: `.githooks/pre-commit` runs
`layer_path_check.py` and nothing else, and says in its own text that whether this repository
should also run the two caller-side guards was not part of the round that wired it.

What does change is the **hand-run** case, which the round acceptance asks for. Anyone running
`candidate_path_check.py` or `review_freeze_check.py` by hand here now has guards that no longer
recognise this repository's own record directory. During this round that is inert — both exit 0 on
both staged trees, because the staged paths are code and members and no freeze marker was out. **It
stops being inert at the closeout**, when a review record is staged under the old directory while
the marker is open. The instrument's own record channel is `R6`'s and
`CONSTRUCTION-CHECKLIST.md`'s, not this default's, so nothing here moves it; the consequence is
reported instead of being worked around.

## 8. `E4` — every guard this round moved or changed, seen failing

Five, each neutered from a `sha256`-checked scratch copy and restored from it, never by `git
checkout`; `sha256sum -c` returned OK for every touched file afterwards.

| mutation | what reddened | what that proves |
|---|---|---|
| expected verdict enum literal perturbed | the contract-set pin | it compares against the real file, not against itself |
| the recursive `walk` neutered | the proof-vocabulary scan, through its own reached-the-leaves assertion | the scan is not vacuous |
| `N2_MODULES_WITHOUT_CODES` emptied | the module partition | the new fourth set is load-bearing |
| `--check-result` re-added to the parser | the retired-input refusal | the refusal is asserted, not merely absent |
| the old directory restored to `DEFAULT_REVIEW_RECORD_DIRS` | **six** tests across two suites | the value reaches the candidate lint's exemptions, the freeze guard's admission rule and the bytes `init` writes — a change reaching only some of them would fail here |

A sixth was observed rather than staged: `test_repo_root_discovery`'s six-call-site pin returned
red at 6 against 5 real sites in the full battery, before it was updated. That is the mutation
evidence for it, and it is named because a pin updated without ever being seen to fire is a pin
nobody tested.

## 9. Two guards changed shape, and neither was relaxed

`test_fix_round_locks`'s named-code sweep read `review.py` as one of four V3-N2 modules and required
each to yield codes. `review.py` now names none: its whole coded vocabulary was the v1 leg's, and
what it still emits is built from the kind argument and is invisible to that regex. The tempting
move — drop the module from the swept set and say nothing — would have shrunk a sweep silently,
which is the F4 defect class the sweep exists to close and which already reappeared once inside the
fix for F4. So a fourth set holds it, the partition test unions four sets instead of three, and the
note says which sweep covers `review.py` instead. `test_repo_root_discovery`'s literal goes from
six to five because `review` had two modes with one `_rooted` call site each and now has one; the
class name is corrected with it, since a class called *TheSix* asserting five is the drift these
pins exist to prevent.

## 10. Left open, and stated rather than implied

- **A residual this round creates and may not fix.** Line 281 of the v1 review schema tells a
  reviewer to reproduce a package digest by importing `review.package_digest`; that import now
  fails. The bytes are `E2`-frozen, round 2 consumed and retired both authorisations at `a554c0b`,
  and `HD-20` routes a fix to a fresh recorded user ruling only the user can give. **Recommended
  route, for the orchestrator to take or reject**: a rider row on the same `E2` write arm
  `sig-write-once` and `contract-wikilink-tier` already share, so one write window closes all
  three. Not written here — routing a finding into the register is not the executor's act
  (`E1`), and the bank is outside this round's declared change boundary (`E8`).
- **Four exported symbols now have no caller** — named in §5 rather than swept, because two of them
  had none at the round's base either and this round did not make them dead.
- **Nothing about a product run is proved here.** Round 1's step 6b narrowed its honesty cap to the
  product-run leg and this round narrows it no further: no run directory built, no instruction
  frozen, no reviewer dispatched from a mounted stripped tree. The v2 review flow *is* exercised end
  to end — `test_review_cli_v2_subject.py` builds a committed control plane in a throwaway
  repository and drives the real command through a subprocess — but that is the command, not a run.
- **`E9` is untouched.** No valid independent FULL has occurred on this round, so both work commits
  are candidates by `E9`'s own test, the fix leg is unspent and no VERIFY is owed. The budget this
  round has spent is zero.
- **`E10-sync` does not fall due**: no item touches the membership sentence. `E2` was not written
  and no authorisation was sought, which is what the round's opening required.
- **Written by this round's one user-approved fix leg (2026-08-27), answering `L-2` of FULL
  `v3-review-full-1db5155.md`. The bullets above stand word for word — `HD-59` forbids rewriting a
  committed conclusion in place, and this is the adjacent form it admits. This round edited an
  `E10` member and this section owed the statement it did not make.** `document-harness/REVIEW.md`
  moved from blob `395995d45991670dc67e2eb616624c44b30ec123` to
  `aad3dd83643a4656aa239e97afec8edb691228a6`. Re-derived rather than copied from the finding:
  `git rev-parse {b737742,d3cda1a,1db5155}:document-harness/REVIEW.md` at this fix's base
  `fccadfb`, and the same command over all nine members returns the same blob at both ends for the
  other eight, so **the count is one**. Two hunks: item G retiring the ruled-dangling `:93` pointer
  (obligation G5 in §1), and item H's pass over the record channel (H2 in §1). The opening cold
  read `v3-cold-read-b737742.md` read that member end to end at `395995d4…`, 320 lines — its §2
  member table row 4 and its closing blob table both pin it — so **no recorded read is citable for
  the bytes that now stand**, which is `E10`'s citation clause working exactly as written.
  **The two facts `E10`'s deferral clause asks a commit to record, stated here because `HD-59`
  puts `56d1b17`'s and `5a39945`'s bodies out of reach.** Neither hunk adds a clause to any rule
  nor changes what any rule requires beyond what items G and H were opened to change; and no other
  round is in flight — rounds 1 and 2 are CLOSED and this batch closes with this one — so the
  effect on every round in flight is nil. That is the FULL's own reading of the two hunks,
  reproduced against the diff rather than adjudicated (`E12`). **Deferral, never exemption**: the
  bytes ride the next read of this layer at per-member digest cost, and this sentence is what a
  later read sizes from.
  **Why this was worth the fix leg and not a rider row.** The batch closes here, so no later
  round-open exists whose sizing would surface the debt on its own — round 2's analogous statement
  was surfaced by round 3's opening, and there is no round 4. Round 2 carried the same statement as
  its own journal §9 bullet and spent its single fix leg correcting that bullet's count when its
  FULL found it short, which is the same defect class one step earlier. And the round's own FULL
  cannot stand in for the read: `E10` says the amendment's read "is never banked as the round's
  FULL".

## 11. The fix leg — its WorkSpec, its reproduction, and what it refused to widen into

`HD-35` puts the decomposition on the executor, and no plan supplied one for the fix leg any more
than it did for the round, so it is written here on §1's terms. Five obligations, each with the
evidence that answers it.

| # | Obligation | Evidence |
|---|---|---|
| F1 | `B-1`'s sentence states what holds, and the fix is that text changing rather than a rule added about it (`E6`) | the `N2_MODULES_WITHOUT_CODES` comment: the claim about a *code* is gone, replaced by the measured boundary and the one move that restores a sweep |
| F2 | The finding is reproduced before its fix is written — to write it correctly, never to adjudicate the reviewer (`E12`) | the mutation below, its negative control, and a `sha256` restore |
| F3 | The defect class is swept before anything is written, not the reported instance (`E7`, `HD-41` ④) | two live sites carry the phrase; the sibling measured true and was left alone — grep output in the commit body |
| F4 | `L-2`'s read debt is recorded at the location the finding names, in `HD-59`'s forward form | §10's closing bullet, on a `git rev-parse` over all nine members re-run at this fix's base |
| F5 | Three findings bank as rows rather than edits, on the user's routing ruling of 2026-08-27 | `HARNESS-RIDERS.md` 24 → 27, each row carrying its own deadline or its explicit absence |

**The mutation, and the distinction it establishes.** In a scratch worktree at `fccadfb`, from a
`sha256`-checked copy: `CODE = "V3-REVIEW"` at module level and one
`Issue(f"{CODE}-UNSWEPT-CODE", "x", "y")` call site added to `review.py` — the exact shape
`CODE_PATTERN` is written to find, naming a code no test asserts.

```
negative control, unmutated tree : 21 passed in 0.65s
mutated, this class              : 21 passed in 0.09s
mutated, whole battery           : 795 passed in 125.98s
CODE_PATTERN against review.py   : ['-UNSWEPT-CODE']
named_codes() keys               : ['flow.py', 'issues.py', 'summary.py']
```

Restored from the copy, never by `git checkout`; `sha256sum -c` returned OK and both trees were
clean afterwards. **The regex sees the code; nothing hands it the file.** That is the distinction
§8's own mutation could not reach — emptying `N2_MODULES_WITHOUT_CODES` reddens the *module*
partition, a different claim about a different object — and `R4` is why the difference is not a
quibble: mutation proves a test has binding force, never that its force is sufficient.

**The class, swept first.** The phrase lives at two places in the suite. The sibling is about a
*module* that names codes trying to hide behind the no-sweep precedent; a module in no set fails
the partition, which is what §8's mutation demonstrated, so that sentence is true and was not
touched. The one this leg answers was about a *code* inside an already-listed module, which nothing
reads. A third hit is inside a committed review record, which `HD-59` and `R6` both put out of
reach.

**The scope held, and the second arm was refused.** `B-1`'s record offers one — an assertion that
`named_codes()` over `N2_MODULES_WITHOUT_CODES` yields nothing — and calls it acceptable but not
required. Taking it means changing `named_codes()`, which iterates `N2_MODULES` by construction, so
the arm is machinery outside the sentence the finding names. `E6` says the fix is the text changing
and that a fix needing new machinery is the signal to re-question the guarded thing rather than to
add a guard. The sentence was the wrong thing; the sentence is what changed.

**What this leg leaves behind, stated rather than implied.** The three banked rows are debt and not
repair. `L-1`'s and `L-3`'s figures stay wrong where they are, inside committed commit bodies that
`HD-59` puts beyond editing, and the rows exist so a later reader meets the correction rather than
the figure. The frozen v1 schema's stranded digest recipe stays stranded until an `E2` recorded
ruling that names `review.schema.json` exists — and that row records a measured qualifier the
recommendation it came from did not carry, which §10's first bullet and the row itself both name.
Nothing else in the FULL was opened.
