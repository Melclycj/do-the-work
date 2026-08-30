# Journal — round `CORE-ONLY-CODE`, the executor's work block (2026-08-30)

Round 2 of batch `CORE-ONLY`, base_commit `fff2203`, opened at tip `d771cc4`. Items **C**, **D**,
the dispatch half of **H**, and **K**. This file is the home for the detail the four commit
bodies could not hold without becoming unreadable, and for the measurements `E3` asks to be
pasted rather than described. It is not a member, no sweep or guard scans it, and no test
enumerates `document-harness/journal/` — so nothing in it changes what any figure below
measures, except the repository's own tracked-file count, which this file moves 421 → 422.

Every figure was taken by the executor on its own machine, at the commit named beside it. The
commits are `7bcdace` (items C + H's dispatch half), `08d3137` (item D), `8ce93f7` (item K) and
the commit carrying this file.

## 1. What the round did, in one table

| item | what landed | commit |
|---|---|---|
| C | the three modes only a construction round uses left the product tier for `tooling/construction_dispatch.py`; both hard-coded charter constants went with them | `7bcdace` |
| H (dispatch half) | every prompt `dtw dispatch` still writes names what the repository declares under `rules` in its `harness.json` | `7bcdace` |
| D | the two retired-contract stubs deleted; the membership sentence nine → seven, with `LAYER`, `EXPECTED` and eleven prose counts following in the same commit | `08d3137` |
| K | the seven bare `R1` citations in product-tier code, and the `.githooks/pre-commit` token at `document-harness/README.md:26` | `8ce93f7` |

## 2. Item C — where it landed, and why that place

**The proposal, for the user to rule on before the FULL (plan ruling 35).**
`tooling/construction_dispatch.py`: one file, 462 lines, a standalone script at `tooling/`.

The bound is acceptance 6 — *no file in the harness tree holds a construction-only code path* —
and three measured facts pick the place inside it:

1. `tooling/rsclib/document_harness/` is **one product-tier row and travels whole**:
   `git ls-files tooling/rsclib/document_harness | wc -l` returns **22**, which is that row's own
   count. A module inside it would travel whatever its docstring said, so the split cannot be
   made by naming.
2. `tooling/hooks/` holds **pre-commit checks a repository wires into its own hook**, each
   exposing `check(repo_root) -> int`. A dispatch generator is not that, and putting it there
   would make the row's prose false a second time in the same round.
3. `tooling/` itself is already where this instrument keeps **the instruments its own rounds
   run** — `sweep_refs.py`, `ledger_cap_check.py`, `announced_path_disclosure.py`. The
   construction-side tier of `CONSTRUCTION-INDEX.md` already carries that class in one row, so
   this round extends a row by a path rather than opening a new one.

**What the module imports rather than copies**, so the derivation stays in one live copy:
`resolve_subject`, `write_freeze_marker`, `declared_rules`, `declared_rules_phrase` and the
private `_value`. The last is imported under its private name deliberately — re-typing its
marker text would be a second copy of it, and promoting it to the package's public surface
would widen what a caller receives for a reason no caller has any part in.

**The charter, which is the other half of the proposal.** Until this round the two review-side
modes named `migration/document-work-assurance-v3/v3-harness-review-contract.md` by constant and
the executor mode named `document-harness/CONSTRUCTION-CHECKLIST.md` by another. After item D
neither stub exists, so nothing would name the construction reviewer's and reader's standing
instruction. All three modes now derive it from what the repository declares under `rules` in
its `harness.json`. That is not an invention of this round: `document-harness/REVIEW.md:5-9`
already says it from the other side —

> This file describes a role inside a *product run*. … what is left of the construction-side
> contract for reviewing the harness itself is that instrument's own rule file, declared under
> `rules` in its `harness.json` and not carried by a repository that runs against it.

— and this repository's declared rule file carries both a `## Execution side` and a `## Review
side` heading, so one file serves reviewer, reader and executor, and names `RULES.md` as the
counterpart each of them must also read.

Ruling 9 gives two options where the charter and a declared rule are one file — *the prompt
names it twice or the generator folds them* — and this **folds them**: naming the same path
twice, once as charter and once as declaration, says less than naming it once and saying which
it is. A repository that declares nothing gets a refusal, `V3-DISPATCH-NO-DECLARED-RULES`,
rather than a prompt naming no charter.

**What a reader should check about this proposal, since I do not get to conclude it.** It rests
on the plan's own measurement that these three modes are construction-only (*The code the caller
receives and cannot use*, item 1) and on ruling 9's *every dispatch mode that stays in the
product tier*, which presupposes that some do not. If the user reads the modes as generic —
a caller amending its own declared rules owes `E10`'s independent read and now has no generator
for that read's dispatch — the answer changes, and §7 states that consequence as a question
rather than answering it.

## 3. Item H's dispatch half — the line, and both of its forms

`E10`'s second sentence holds `dtw dispatch` to naming the declared files in every prompt it
writes. Both prompts the command still writes carry a generated line, and it is emitted in two
forms rather than omitted when there is nothing to name:

```
**This repository's own rules:** `rules/CALLER-RULES.md` — declared under `rules` in its
`harness.json`, to be read after the charter above. They bind this repository alone.

**This repository's own rules:** none. Its `harness.json` declares no rule files, which E10
makes a repository that has declared nothing rather than a defective one.
```

The second exists because an absent line reads the same as a generator that failed, and `E10`
says a repository that has declared nothing is not defective — so the prompt says which of the
two it is. `E6`'s test, asked before the line was written: with the line absent, a cold session
cannot tell "no declared rules" from "an old generator", and that is a decision that changes.

## 4. `E4` — every guard change seen red once, with its negative control

Run by `.goals/mutate.py` (a scratchpad, not committed): copy the subject, record its sha256,
assert the named tests **green first**, mutate in place, run them again, restore from the copy,
re-check the digest, run them a third time. Never `git checkout --`: a restore through git
cannot tell "the file came back" from "the file was already what git holds".

### 4.1 The declared-rules prompt line (item H)

```
subject   : tooling/rsclib/document_harness/dispatch.py
sha256    : 9b32c304c0390d98c53eb96b73b9b06d81fb75250ef05603f84bd2dddabb24b4

--- baseline (unmutated): must be GREEN ---
$ tests/document_harness_review/test_dispatch.py::EveryPromptNamesWhatTheRepositoryDeclares
6 passed in 2.62s
exit=0

--- MUTATED (declared_rules_line returns ""): must be RED ---
FAILED …::test_the_executor_prompt_names_the_declaration
FAILED …::test_the_executor_prompt_says_so_when_nothing_is_declared
FAILED …::test_the_product_review_prompt_names_the_declaration
FAILED …::test_the_product_review_prompt_says_so_when_nothing_is_declared
FAILED …::test_two_declarations_are_both_named
5 failed, 1 passed in 2.94s
exit=1

restored  : sha256 9b32c304c0390d98c53eb96b73b9b06d81fb75250ef05603f84bd2dddabb24b4  (MATCHES)
--- restored: must be GREEN again ---
6 passed in 2.82s
exit=0
VERDICT: the guard binds
```

The one survivor is the pair's **negative control** and is supposed to survive:
`test_the_declaration_is_the_swept_repositorys_and_not_this_ones` asserts that this
repository's own declared path is *absent* from a prompt derived elsewhere, which stays true
when the line disappears. A mutation that took it red too would mean it was asserting presence
by accident.

### 4.2 The construction charter, derived instead of constant (item C)

```
subject   : tooling/construction_dispatch.py
sha256    : ccfc57b39b8729d076ace534370540b7378dfda1ae2e53110621cf8971f61ede

--- baseline: 24 passed in 10.17s  exit=0
--- MUTATED (_charter returns the hard-coded checklist path): 11 failed, 13 passed  exit=1
      FAILED ReadDispatchesGenerateToo::test_the_prompt_is_exactly_the_golden_file
      FAILED ConstructionExecutorDispatchGeneratesToo::test_a_repository_that_declares_nothing_is_refused
      FAILED ConstructionExecutorDispatchGeneratesToo::test_nothing_is_derived_beyond_the_charter
      FAILED ConstructionExecutorDispatchGeneratesToo::test_the_prompt_is_exactly_the_golden_file
      FAILED NoCharterIsNamedFromThisRepositorysOwnLayout::test_the_swept_repositorys_declaration_is_the_one_named
restored  : sha256 ccfc57b39b8729d076ace534370540b7378dfda1ae2e53110621cf8971f61ede  (MATCHES)
--- restored: 24 passed in 10.12s  exit=0
VERDICT: the guard binds
```

### 4.3 The membership change (item D), both directions

```
subject   : tooling/hooks/layer_path_check.py
sha256    : b828cdf2d481919545d855f02e47ed0dd4634ed2acd3020a5a8d447308e70c12   (both runs)

A — a member ADDED back (the review stub returns to LAYER)
--- baseline: 55 passed  exit=0
--- MUTATED: 1 failed, 54 passed  exit=1
      FAILED LayerMembership::test_layer_equals_the_hand_written_membership
--- restored: 55 passed  exit=0

B — a member DROPPED (document-harness/RULES.md leaves LAYER)
--- baseline: test_precommit_hook 3 passed · test_precommit_checks 55 passed  exit=0
--- MUTATED: test_precommit_hook 1 failed, 2 passed
      FAILED PrecommitHookAsProcessTests::test_hook_blocks_when_the_layer_check_fails
             test_precommit_checks 8 failed, 47 passed
      FAILED LayerPath::test_a_stale_prefixed_token_blocks
      FAILED LayerPath::test_a_token_resolving_nowhere_blocks
      FAILED LayerPath::test_resolution_escaping_the_repo_root_does_not_count
      FAILED LayerMembership::test_every_member_is_scanned
      FAILED LayerMembership::test_layer_equals_the_hand_written_membership
--- restored: 3 passed / 55 passed  exit=0
VERDICT: the guard binds (both)
```

Direction B is what `E10-sync`'s row calls the fail-safe: `test_precommit_hook.py`'s
single-member `MEMBER` goes **loudly red** rather than the member going silently unscanned.
That is why `MEMBER` needed no edit this round and why saying so is not an excuse — its value
has been `document-harness/RULES.md` since round `CORE-ONLY-LAYER`, neither deleted path is it,
and B proves the constant still binds.

## 5. The acceptances, with their output

The harness-only tree below is built the way acceptance 1 names: `git archive` of the
product-tier paths from `git write-tree` (so it is the staged bytes, not the last commit's),
extracted into a fresh directory, `git init`, `git add -A`, one commit. It comes to **59**
tracked files at every point in this round.

### Acceptance 1 — zero instrument-held non-resolving sites, caller-held reported separately

At `fff2203` the harness-only tree's instrument-held class stood at **four**: the two `PATHTOK`
stub paths in `RULES.md` and the two members `MISSING`. After item D:

```
$ python tooling/sweep_refs.py          # harness-only tree, final
NAMETOK document-harness/RULES.md:10  harness.json
NAMETOK document-harness/RULES.md:96  harness.json
NAMETOK document-harness/RULES.md:146  HARNESS-DECISIONS.md
NAMETOK document-harness/RULES.md:207  HARNESS-RIDERS.md
NAMETOK document-harness/README.md:23  harness.json
NAMETOK document-harness/README.md:25  harness.json
NAMETOK document-harness/EXECUTION.md:14  harness.json
NAMETOK document-harness/EXECUTION.md:188  audit-rounds.md
NAMETOK document-harness/EXECUTION.md:196  build_run.py
NAMETOK document-harness/EXECUTION.md:201  check_shells.py
NAMETOK document-harness/EXECUTION.md:306  write_audit.py
NAMETOK document-harness/EXECUTION.md:369  smoke_test.py
NAMETOK document-harness/EXECUTION.md:375  run_tests.py
NAMETOK document-harness/EXECUTION.md:376  run_p4_tests.py
NAMETOK document-harness/EXECUTION.md:376  run_p5a_tests.py
NAMETOK document-harness/EXECUTION.md:377  validate_fixtures.py
NAMETOK document-harness/EXECUTION.md:394  run_tests.py
NAMETOK document-harness/EXECUTION.md:504  v3-review-full-86defbc.md
NAMETOK document-harness/EXECUTION.md:505  audit-rounds.md
NAMETOK document-harness/EXECUTION.md:508  user-decision-triage-comparator-environment-defects.json
NAMETOK document-harness/REVIEW.md:9  harness.json
NAMETOK document-harness/REVIEW.md:69  v3-review-full-fef3a2e.md
NAMETOK document-harness/REVIEW.md:161  review-verify.json
NAMETOK document-harness/ORCHESTRATION.md:9  harness.json
NAMETOK document-harness/ORCHESTRATION.md:40  harness.json
NAMETOK document-harness/ORCHESTRATION.md:54  HARNESS-DECISIONS.md
NAMETOK document-harness/ORCHESTRATION.md:95  harness.json
NAMETOK contract/Document-Work-Assurance-Contract-v4.md:279  review.schema.json
-- 28 caller-held or unresolvable references over 7 members and declared rule files
```

**Zero `MISSING`, zero `PATHTOK`, twenty-eight `NAMETOK`.** Classed by hand, not by prefix,
because collapsing the two classes is how the defect hid: `harness.json` (8) is the caller's own
file at its own root; `HARNESS-DECISIONS.md` (2) and `HARNESS-RIDERS.md` (1) are what `dtw init`
writes into a caller's root; `audit-rounds.md` (2), `build_run.py`, `check_shells.py`,
`write_audit.py`, `smoke_test.py`, `run_tests.py` (2), `run_p4_tests.py`, `run_p5a_tests.py`,
`validate_fixtures.py`, `user-decision-triage-comparator-environment-defects.json` and
`review-verify.json` are the caller's own run artifacts and the five battery commands the plan's
forward correction re-classified; `v3-review-full-86defbc.md` and `v3-review-full-fef3a2e.md`
are the caller's own review records; `review.schema.json` is the contract's past-tense sentence
under plan ruling 19. **Every one is the compliant caller-held form, reported separately and
still present.**

The class this measurement cannot see is §6's rider `caller-cannot-resolve-ids`: a seven-hex
commit id is neither path-shaped nor a basename, so the zero above is silent about nine of them.

### Acceptance 2 — the sweep on both trees

```
this repository : -- 13 caller-held or unresolvable references over 8 members and declared rule files
harness-only    : -- 28 caller-held or unresolvable references over 7 members and declared rule files
```

The 13 here is unchanged from the round's base and from every commit inside it. What moved is
the number of paths swept: 10 → 8 here (seven members plus the declared rule) and 9 → 7 there,
both by item D's two deletions. On the harness tree 32 → 28, the four being item D's.

### Acceptance 3 — on the harness-only tree

```
$ python tooling/dtw.py --help                     exit=0
$ python tooling/dtw.py init --repo-root <fresh>   exit=0
  created  : .harness/  ·  .harness/scan-surfaces.json  ·  harness.json
             HARNESS-DECISIONS.md  ·  HARNESS-RIDERS.md  ·  .gitignore
  RESULT: 6 created, 0 left as found (exit 0)
  harness.json written: {"policy": null, "rules": []}   — both fields present
$ python tooling/dtw.py init --repo-root <fresh>   exit=0   (again)
  RESULT: 0 created, 5 left as found (exit 0)        — idempotent, nothing overwritten
$ python tooling/hooks/candidate_path_check.py     exit=0
$ python tooling/hooks/review_freeze_check.py      exit=0
$ python tooling/hooks/layer_path_check.py         exit=0
```

`tooling/construction_dispatch.py` is **absent** from that tree, which is the point of item C
and is itself part of acceptance 6's evidence.

### Acceptance 5 — `CONSTRUCTION-CHECKLIST` on the harness tree

```
$ grep -rn 'CONSTRUCTION-CHECKLIST' . --exclude-dir=.git
(no match)
```

At the round's base this returned one line, `tooling/rsclib/document_harness/dispatch.py:776`,
which round 1's closeout accounted for as item C's. It is now zero with nothing to account for.

### Acceptance 6 — the line counts either side of the split

```
                                              fff2203    at 8ce93f7   delta
tooling/rsclib/document_harness/dispatch.py     1005         845       -160
tooling/rsclib/document_harness/cli.py           631         560        -71
tooling/construction_dispatch.py                   0         462       +462
```

231 lines left the two product-tier files. The 462 is larger than the 231 because the new file
carries its own module docstring, its own argparse entry and its own root resolution, none of
which existed separately while the modes were `dtw dispatch`'s. What remains in the product tier
after the move: `dispatch.py` holds a product run's review and that run's executor;
`cli.py`'s `dispatch` handler branches on two modes, `--subject` and `--executor`.

### Acceptance 7 — the suite

```
base fff2203 / round tip d771cc4 : 853 passed in 161.63s
after 7bcdace                    : 873 passed in 157.70s
after 08d3137                    : 873 passed in 159.32s
after 8ce93f7                    : 873 passed in 173.54s
```

Delta **+20**, accounted exactly by file rather than estimated:

| file | at base | now | delta |
|---|---|---|---|
| `test_dispatch.py` | 70 | 61 | −9 (three classes out, one class of 6 in) |
| `test_dispatch_freeze_marker.py` | 4 | 3 | −1 (the construction executor case moved) |
| `test_repo_root_discovery.py` | 11 | 12 | +1 (the new script's own root resolution pinned) |
| `test_construction_dispatch.py` | — | 24 | +24 |
| `test_construction_dispatch_freeze_marker.py` | — | 5 | +5 |
| | | | **+20** |

Items D and K changed no test count: D's edits are `EXPECTED` entries inside an existing test,
and K's are docstrings and comments no test names — checked rather than assumed, by grepping
`tooling/tests/` for each of the eight edited strings, which returns nothing.

### Acceptance 8 — `CONSTRUCTION-INDEX.md` re-measured by its own commands

At `8ce93f7`, by `git ls-files <row paths> | wc -l`:

```
row 1 contract/Document-Work-Assurance-Contract-v4.md ....... 1
row 2 schema/document-assurance-v3 .......................... 14
row 3 the five role documents ............................... 5
row 4 document-harness/ONBOARDING.md ........................ 1
row 5 document-harness/templates ............................ 2
row 6 tooling/dtw.py · tooling/do-the-work.py ............... 2
row 7 tooling/rsclib/document_harness ....................... 22
row 8 tooling/hooks ......................................... 4
      assurance/templates/run-v2 ............................ 8
tier total .................................................. 59
repository .................................................. 421
```

**Row 8's prose now agrees with its count.** It said *the two caller-side guards a caller wires
into its own `pre-commit`* over a count of 4, which counted three guards and the package marker
`tooling/hooks/__init__.py`. Under plan ruling 5 `layer_path_check.py` became a general guard
that reads the harness members plus the local declaration rather than moving to the construction
side, so the tier genuinely carries three guards; the row now says *the three tracked pre-commit
guards and the package marker they are called through*, and points at
`document-harness/README.md`'s *Local enforcement* row, which that row's own text declares the
single home of which guard does what. The count is untouched, because the count was right.

### Acceptance 9 — guards exit 0 and the membership resolves N/N, both trees

```
this repository : layer_path_check 0 · candidate_path_check 0 · review_freeze_check 0 · ledger_cap_check 0
                  7 of 7 members resolve; missing=[]
harness-only    : layer_path_check 0 · candidate_path_check 0 · review_freeze_check 0
                  7 of 7 members resolve; missing=[]
```

The `layer_path_check` exit is vacuous on a clean index — the guard scans `git diff --cached`
added lines of members and declared rules, so with nothing staged it scans nothing. On item D's
staged bytes it was not vacuous, and the replay says what it actually scanned:

```
$ replay of unresolved_tokens / scanned_paths over exactly the lines 08d3137 stages
document-harness/RULES.md: 6 added lines, scanned
document-harness/README.md: 2 added lines, scanned
document-harness/CONSTRUCTION-CHECKLIST.md: 3 added lines, scanned
GUARD REPLAY -> failures: 0
```

### Acceptance 11 (the dispatch half)

`dtw init` on the harness-only tree writes `harness.json` with both fields present (§ acceptance
3 above). With one rule file declared, both modes `dtw dispatch` still carries name it in the
prompt, and the construction-side dispatch's three modes do too; both guards scan it, which
`scanned_paths` shows directly:

```
$ python -c "... layer_path_check.scanned_paths('.')"
('document-harness/RULES.md', 'document-harness/README.md', 'document-harness/EXECUTION.md',
 'document-harness/REVIEW.md', 'document-harness/ORCHESTRATION.md',
 'contract/Document-Work-Assurance-Contract-v4.md',
 'schema/document-assurance-v3/paragraph-map.schema.json',
 'document-harness/CONSTRUCTION-CHECKLIST.md')
```

`sweep_refs.py` imports that same function, which is why its tally line reads *over 8 members
and declared rule files*. Each guard change was seen red once with a negative control — §4.

### The announced-path alarm

```
$ python tooling/announced_path_disclosure.py --before fff2203 --after HEAD
announced-path disclosure: range fff2203..HEAD
  floor 1d4d9aa1f6b1daca3fbf1a7765985abaec350b18; 5 non-merge commit(s) judged
  every announced path changed in this range is named by the commit that changed it
exit=0
```

No commit of this round changes an announced path, and none was expected to (`E2`; the contract
and the schema pack are the announced set). §7 names the one place where a fix would have had
to, and why it did not happen.

### Re-measured after the correction pass under ruling 37 — written forward, every block above left word for word (`HD-59`)

Every figure below was taken at `6c93c98`, the correction pass's last content commit, by the same
two instruments and the same two trees as the blocks above. The harness-only tree is `git archive`
of the product-tier paths out of `git write-tree` into a fresh git repository: **59 files**, the
same 59. Nothing between that commit and this file changes what any of them measures — this
journal is neither an instruction-layer member nor a declared rule file, so no sweep and no guard
reads it, and no test enumerates `document-harness/journal/`.

**Acceptance 1 — the instrument-held class is still zero.** The harness-only tree returns
**0 `MISSING`, 0 `PATHTOK`, 28 `NAMETOK`**, the same 28 as the block above and the same hand
classification: `harness.json` (8) is the caller's own file at its own root, `HARNESS-DECISIONS.md`
(2) and `HARNESS-RIDERS.md` (1) are what `dtw init` writes into a caller's root, twelve are the
caller's own run artifacts and battery commands, two are the caller's own review records, and
`review.schema.json` is the contract's past-tense sentence under plan ruling 19. Four of the 28
moved line: `document-harness/ORCHESTRATION.md` `:40` to `:41`, `:54` to `:55` and `:95` to `:96`,
because ruling 37 (a)'s first replacement is one line longer than what it replaced, while `:9` is
above the edit and did not move. No site was added and none was removed.

**Acceptance 2 — the sweep on both trees.**

```
this repository : -- 13 caller-held or unresolvable references over 8 members and declared rule files
harness-only    : -- 28 caller-held or unresolvable references over 7 members and declared rule files
```

Both unchanged from the block above. Neither number could have moved: the five bare `R<n>`
citations live in files no sweep scans, the `ONBOARDING.md` token was never in the swept set —
which is rider `e10-cannot-see`'s whole point — and `ORCHESTRATION.md`'s two replacements name no
artifact at all.

**The battery.**

```
after 6c93c98 : 873 passed in 148.18s
```

Delta zero against `8ce93f7`'s 873 and against the figure taken inside this pass at `691ddff`. The
pass changes four code and schema strings and no behaviour, and the suite holds no `__doc__`
assertion for any of them to break.

**The two class scans, either side of the write (`HD-41` ④).** The widened bare-`R<n>` key over the
product tier's code, schemas, contract, run template and six documents — `document-harness/RULES.md`
excluded, its `R` tokens being the identifiers collided *with* — returned **40** lines before and
**36** after; the class ruling 37 (b) names, five sites, is **zero**, and the 36 survivors are the
four families the commit body enumerates, every one correct as written. The `.githooks` key over
`document-harness/ONBOARDING.md` returned **5** before and **4** after, the instrument-held count in
that file going 1 to 0; over the seven members and this repository's declared rule file it returns
**0** either side, which item K already brought about.

**The announced-path alarm, over the range this pass sits inside.**

```
$ python tooling/announced_path_disclosure.py --before fff2203 --after HEAD
announced-path disclosure: range fff2203..HEAD
  floor 1d4d9aa1f6b1daca3fbf1a7765985abaec350b18; 12 non-merge commit(s) judged
  every announced path changed in this range is named by the commit that changed it
exit=0
```

One commit of this pass changes an announced path — `691ddff`, at
`schema/document-assurance-v3/assurance.schema.json` — and its body names that path in full, which
is what the alarm confirms and the whole of what it certifies.

**Corrected forward, the block above left word for word (`HD-59`; a journal number, so `HD-23`).**
Two of its figures are labelled with a commit they were not taken at, and the opening sentence
*every figure below was taken at `6c93c98`* is too wide to be true of all of them. **The alarm
output.** Its `12 non-merge commit(s) judged` was produced with `HEAD` at `691ddff`, not at
`6c93c98`, where the same command reports **14**; at this pass's actual tip `c08de13` it reports
**15**. The count is the number of commits in the range the alarm judged and moves with every
commit the pass adds, so only the verdict line is invariant — and that line is identical at all
four points, `every announced path changed in this range is named by the commit that changed it`,
exit 0, floor `1d4d9aa`. Re-run at the tip and pasted rather than described:

```
$ python tooling/announced_path_disclosure.py --before fff2203 --after HEAD    # HEAD = c08de13
announced-path disclosure: range fff2203..HEAD
  floor 1d4d9aa1f6b1daca3fbf1a7765985abaec350b18; 15 non-merge commit(s) judged
  every announced path changed in this range is named by the commit that changed it
exit=0
```

**The two class scans.** A before-and-after pair cannot be taken at one commit by construction: the
40 was taken at `c042017`, the round's tip when this pass opened, and the 36 at the worktree
carrying ruling 37 (b)'s edits before `691ddff` committed them; likewise `.githooks` 5 at `c042017`
and 4 at the worktree before `65ecdac`. Both after-figures were re-run at `c08de13` and are
unchanged — 36 lines, the five-site class at 0, and 4 tokens in `document-harness/ONBOARDING.md`.
**Unaffected**, because each was in fact taken at `6c93c98` on a clean worktree: acceptance 1's
`0 MISSING / 0 PATHTOK / 28 NAMETOK` over 59 files, acceptance 2's 13 and 28, and the battery's
873. All three were re-run at `c08de13` as well and are identical, the battery at 873 passed in
165.50s. The same mislabel is in `c08de13`'s own commit body, which quotes the 12; it is corrected
by this paragraph and not rewritten there.

### Written forward after the FULL, under the fix gate (plan ruling 38) — every block above left word for word (`HD-59`)

The FULL over `fff2203..70c82b4` returned `CHANGES_REQUIRED` (record
`v3-review-full-70c82b4.md`, committed at `affacc2`) and the user's fix gate is plan ruling 38.
Three of its four lows are this journal's text; they are corrected here rather than in place, and
the one fix commit carries this section.

**`L-1` — acceptance 1's classification, corrected.** The acceptance 1 block above closes *Every
one is the compliant caller-held form, reported separately and still present*, and the
re-measured block repeats that classification. The 28 are not all caller-held. The twenty-eighth,
`contract/Document-Work-Assurance-Contract-v4.md:279`'s past-tense `review.schema.json`, is
**instrument-held**: the same contract sentence says of that schema *that schema was this
instrument's own rather than any caller's: it left the tree*, and it is reachable only in this
repository's git history. It stands not because a caller holds it but because plan ruling 19's
holder-or-history clause admits it. So acceptance 1 reads, corrected: **twenty-seven caller-held,
and one — the contract's past-tense `review.schema.json` — instrument-held and standing under
plan ruling 19's holder-or-history clause**. Read literally against acceptance 1's own words —
*zero non-resolving sites naming an instrument-held artifact* — the count is **one**, admitted by
a ruling rather than being absent. The measurement does not move (`0 MISSING`, `0 PATHTOK`, `28
NAMETOK` over 59 files, unchanged at every point in this round); what moves is one site's
category. This matters because `HD-66` reads acceptance 1 to decide whether core distribution is
achievable, and a category recorded wrong there is read as a clean zero by whoever asks that
question next.

**`L-2` — the widened bare-`R<n>` survivor report, corrected.** `691ddff`'s body says the 36
survivors *are all correct as written* and files seven `assurance/templates/run-v2/` sites under
*construction round and batch names, always qualified*. **Five of the 36 are bare and
unqualified**: `assurance/templates/run-v2/README.md:48` and `:100`, and
`assurance/templates/run-v2/compare_blocks.py:29` and `:68`, name a construction round of this
instrument's own history by a bare `R2`, in files that travel to every caller; and
`tooling/hooks/candidate_path_check.py:83`'s *the ordinary R1 sentence* was filed under *a product
run's own requirement identifiers, which plan ruling 29 keeps*, while ruling 29's vocabulary is
the prefixed `V3-D5` / `N0-A5` family and a bare `R1` is not in it. All five are **reported and
left standing** under ruling 30's report-don't-widen instruction, which is what authorizes their
staying; the fix gate's boundary (ruling 38) does not admit editing them. What was wrong is the
report, and this paragraph is the report corrected.

**`L-4` — what authorized `c08de13`.** Its body opens *Kind: pre-submission correction, round 2
CORE-ONLY-CODE, plan ruling 37 (e)*. Ruling 37 has (a), (b) and (c) and no (e). The
journal-forward write that commit carries is authorized by the plan's **step 4b**, which names
*the journal's §7 written forward* among that pass's work. The commit body is not rewritten
(`HD-59`); this sentence is its correction, and an audit tracing each correction-pass commit to
its authorization lands here.

## 6. The rider bank against this round's change list

Read row by row against the files this round touched. Four rows are touched, one row is new, and
none is redeemed — every fix in reach is design, which `R10` says may not ride a batch.

| row | touched? | disposition |
|---|---|---|
| `E10-sync` | **yes** | its three bound sites changed in `08d3137` and are named in that body; the fourth machine-side copy `MEMBER` needed no change and §4.3 proves it still binds; the prose census is corrected from seven sites to eleven, and the non-membership `nine`s are listed in the row so the next round need not re-derive them. A per-touch check, never a redemption — the row says so itself |
| `e10-cannot-see` | **yes** | the live instance it named inside a member — the README hook token — is deleted by item K, so the blind spot now has **zero** instances in the layer (measured: backticked tokens containing `.githooks` over the seven members and the declared rule = 0). The blind spot itself is untouched: `E10`'s clause and `PATHLIKE` are unchanged, and adding an item to that enumeration is design. Row stays, with five surviving same-shape tokens in `ONBOARDING.md` recorded for whoever redeems it |
| `dispatch-exec-perms` | **yes** | its premise is **falsified for this round**: this executor ran `python` and `git` write itself — the battery, three guards, `ledger_cap_check`, `announced_path_disclosure`, four mutations, the `git archive` trees, and all four work commits. The row is not deleted: its subject is that `HD-55`'s role separation *can* collapse on the verification half, its carriers are unchanged, and permissions are a per-machine accident that ran the other way in round `V1-RESULT-RETIRE`. Restated in the row: neither the three-roles table nor `HD-55` says a dispatched executor must be able to run its own verification, so both situations conform while differing sharply in consequence — closing that needs a clause, which is design |
| `figure-units` | **yes** | third touch. The index's figure paragraph moved again (tier 59, repository 415 → 421, anchor `4b81dd9` → `8ce93f7`) and still writes **no byte figure**, which is this row's redemption condition. Site (a) stays closed, (b) and (c) stay open in journals under `HD-23` |
| `caller-cannot-resolve-ids` | **new row** | the opening cold read's `L-1`. Nine hex commit ids in travelling members, re-measured at `8ce93f7` and all nine still `MISSING`; target, redeem-when and deadline are the record's §4, transcribed with the sites re-derived rather than copied |
| `e1-reader` | **noted** | its subject is written as `dtw dispatch --read`, which from `7bcdace` is `python tooling/construction_dispatch.py --read`; recorded in that commit's body. Its redeem-when names `E1`'s form clause and `ORCHESTRATION.md`'s roles table, neither touched |
| `read-name-split` | no | touch condition is `R6`'s record-channel sentence or `E10`'s citation clause. This round changes `E10`'s membership sentence, which is neither |
| `itemh-sweep-count` | no | touch condition is a batch re-scanning the `migration/` directory or re-dividing item H's sites. This round does item H's dispatch half and re-scans nothing |
| `itemg-linecount-file` | no | touch condition is a line-count figure for `flow.py` or `review.py`. This round writes line-count figures for `dispatch.py`, `cli.py` and the new file, which are different files |
| `onboarding-carries-construction` | no | touch condition is `ONBOARDING.md`'s Owner cells or its enumeration. This round changes one word in `:150` (`nine` → `seven`), which is neither cell content nor the enumeration |
| `PD` | no | touch condition is `__init__.py`'s export surface or `split-design.md` §5. Neither touched |
| `RA` | no | `run_all`'s signature untouched; `dtw` still has eight commands, none added or removed |
| `wl-route`, `hd38-both-ways`, `e9-pair-budget`, `charter-qualifiers`, `e1-table`, `e10-freeze-exception`, `announced-set-anchor` | no | all name `RULES.md` clauses (the free-channel enumeration, `R9`'s opener, `R10`'s routing sentence, `HD-38`'s deferral clause, `E9`/`E10`'s budget vocabulary, `ORCHESTRATION.md`'s cite-only lines, `E2`'s anchor). This round changes exactly one `RULES.md` passage, the `E10` membership sentence and one added history sentence beside it; none of those clauses is touched |
| `freeze-audit`, `pin-drift`, `delta-prose`, `argv-cap`, `template-clause-unguarded`, `archive-header-selfcount`, `r9-terminal-no-carrier`, `alarm-mutation-gaps`, `alarm-yaml-range-untested` | no | none of their named surfaces is in this round's change list |

### The bank after the correction pass — written forward, the table above left word for word (`HD-59`)

Two changes, one row each, and still no redemption. `e10-cannot-see` is touched a second time at
`65ecdac` and its row gains a second touch record: the instance its first record named, the
`ONBOARDING.md:150` hook path, is de-named there, so same-shape instrument-held tokens in that file
go 1 to 0 while the four caller-side siblings at `:32`, `:52`, `:63` and `:148` stay by instruction;
the blind spot itself — `E10`'s *what the guard still cannot see* enumeration, the *the class
entire* sentence above it, and `layer_path_check`'s `PATHLIKE` — is unchanged, so the row keeps its
redeem-when and its deadline. And one row is **new** at `6c93c98`: `caller-rule-read-no-generator`,
plan ruling 36's banked consequence, carrying §7.2 below into the bank with the redeem-when and
deadline that ruling gave it.

One further row is **touched and reported rather than written to**, because acting on it is outside
ruling 37: `onboarding-carries-construction` names `ONBOARDING.md`'s Owner column as one of three
touch surfaces for its (a) arm, and `:150` is an Owner cell, so `65ecdac` reaches that condition.
Its (a) arm is design — a clause carrying the four Owner cells at items 4 to 7 whose owner is
`io-design.md` — and none of those four cells is touched. Whether the row owes a touch note for
this pass is the orchestrator's to route.

## 7. Reported up — questions and boundaries, decided by nobody here

`ORCHESTRATION.md`'s *The executor's report back* is the text these answer to: a boundary the
executor would have to exceed, or an authorization it cannot see, goes to the orchestrator,
which puts it to the user. None of the four below is acted on.

### 7.1 `document-harness/ORCHESTRATION.md:37-38` is made false by item C, and I did not touch it

The sentence reads *something must hand each its charter at startup, and `dtw dispatch` does:
three review-side modes, and two executor-side modes, one per side of the work*. After `7bcdace`
the command has **one of each**. Its continuation at `:39-43` enumerates the two executor-side
charters, one of which is now the construction dispatch's.

Two reasons I did not write the fix, and I do not get to weigh them against each other. My
instruction says the amendment at `:40-42` stays true as written and that I touch neither
sentence. And `:40-42` sits **inside the same sentence** that would have to be rewritten — the
bytes the `E10` must-fix channel landed at `5a9c0fd` and whose independent re-read landed one
commit later at `d771cc4`.

The minimum bytes, if the user rules them, replacing

> and `dtw dispatch` does: three review-side modes, and two executor-side modes, one per side of
> the work

with

> and a dispatch generator does: `dtw dispatch`, one review-side mode and one executor-side mode
> for a product run, and a repository's own construction-side dispatch for the rounds it runs
> against its own rules

which leaves `:40-42`'s clause — *the one its `harness.json` declares, which the command is held
to deriving from the declaration rather than from a constant of its own* — standing word for
word, and true of both generators.

Two smaller sites of the same shape: `:69-70` names `dtw dispatch --construction-executor`,
which is now the construction dispatch's flag and not that command's; and `document-harness/
ONBOARDING.md:200`'s *`dtw dispatch` writes the freeze marker and prints the dispatch* stays
true for a caller, whose only review-side mode is `--subject`.

**Answered 2026-08-30 — plan ruling 37 (a), written forward; both paragraphs above stand word for
word (`HD-59`).** The user ruled the minimum bytes above and they are applied verbatim at
`23e69d6`, a pre-submission correction: `:37-38` now says *and a dispatch generator does: `dtw
dispatch`, one review-side mode and one executor-side mode for a product run, and a repository's
own construction-side dispatch for the rounds it runs against its own rules*. The `:40-42` clause
the `E10` must-fix amendment `5a9c0fd` landed stands unchanged in bytes inside that same sentence,
as the ruling required, and is now true of both generators; the re-read that cleared it at
`d771cc4` is not disturbed. The second site went with it: `:69-70`, which named a
`--construction-executor` flag `dtw dispatch` no longer has, now reads *a repository's own
construction-side dispatch in its executor mode (construction round)* — the same shape, and
deliberately no path token, because the construction-side dispatch is instrument-held while this
file travels, so writing its path would create exactly the class ruling 24 deletes and acceptance 1
measures at zero. `document-harness/ONBOARDING.md:200` stands, as the ruling directed. Two things
that commit discloses rather than leaves to be inferred: three further lines of the second
paragraph are re-wrapped with no change of content, because the shorter replacement would otherwise
have left a 105-character line beside a 27-character one; and the change owes the independent
re-read `E10` requires of an amended member, which rides the next opening read of this layer and
which the round's closeout states as read debt.

### 7.2 A caller amending its own declared rules now has no read-dispatch generator

`E10` binds a declared rule to the layer's amendment discipline *including the independent
read*. The mode that generated a read dispatch left the product tier with item C. A caller that
amends its own rule file therefore still owes the read and has no command to dispatch it with.

This is `R5`'s shape — whether the mode should be there at all is the user's question, not
mine — and it is the strongest argument against §2's proposal, which is why it is stated beside
it rather than under it.

**Answered 2026-08-30 — plan ruling 36, written forward; the paragraph above stands word for word
(`HD-59`).** The user accepted §2's proposal and **banked** this consequence rather than answering
it: it is a design rider, so `E10` opens a round for it and no batch may carry it. The row
`caller-rule-read-no-generator` lands at `6c93c98` with the redeem-when and deadline the ruling
gave — redeem-when the `dispatch-economy` batch's **first item**, the must-fix pair's narrow-subject
read dispatch, which is `CONSTRUCTION-LEDGER.md`'s `dispatch-economy` backlog entry clause ①, and
that item is itself the command-surface design that opens a round under `HD-47`, so `R10`'s rule
that a design-shaped row names only a round-eligible **surface** is met rather than skirted;
deadline the first caller that amends a declared rule file, a moment `HD-37` ① requires to fall
outside the round that writes the row, which it does, no caller having amended one yet. The row
supplies no bytes on purpose: both fixes in reach — a narrow-subject read mode added back to the
product tier, or a clause in `E10` saying how a caller discharges the read — add a command surface
or a clause, and `R5` puts that question to the user.

### 7.3 A sibling class item K did not widen to, because a fifth site is announced

Four bare `R4` citations name the N1 record's governance-scan requirement by number alone and
collide with `RULES.md`'s own `R4` exactly as the seven `R1`s collide:
`tooling/rsclib/document_harness/checks.py:1` and `:633`,
`tooling/rsclib/document_harness/cli.py:58`, `tooling/rsclib/document_harness/flow.py:27`.
A fifth is `schema/document-assurance-v3/assurance.schema.json:109` — **an announced path**,
which this round's instruction says to stop and report rather than touch. Fixing four of five
and leaving the announced one is the half-done shape ruling 30's own reason warns about, so
none of the five was touched. The bytes, if ruled: the four drop the number from their
parenthetical or say *the governance scan*; the schema description says *the governance scan*
while keeping *Discharges N1-R2*, which is prefixed and stays under ruling 29.

**Answered 2026-08-30 — plan ruling 37 (b), written forward; the paragraph above stands word for
word (`HD-59`).** All five go together, which is what refusing to fix four of five asked for, and
the bytes this section drafted are applied at `691ddff` as a pre-submission correction. Line
numbers were re-derived at `23e69d6` before writing rather than copied from above (`E3`) and had
not moved. `checks.py:1` drops `R4` from its citation list and keeps *plan §5.3, N1-A8*;
`checks.py:633` drops its whole trailing parenthetical; `cli.py:58` keeps `V3-N1` and drops `R4`;
`flow.py:27` says *the governance scan*, its own *(N1 residual R2)* untouched under ruling 29; and
`schema/document-assurance-v3/assurance.schema.json:109` says *the governance scan* while keeping
*Discharges N1-R2*. That schema is an announced path, so `691ddff`'s body names it in full under
`E2` and the alarm over `fff2203..HEAD` returns exit 0. The class scan ran with the widened key as
ruled — every bare `R<n>` in the product tier, not only `R4` — and found **nothing beyond the
five**: the 36 survivors are qualified construction round and batch names, a product run's own
requirement identifiers, correct citations of `RULES.md`'s own rules, and ruling 29's prefixed
record identifiers. One thing outside that range is reported and not fixed, because the range is
the product tier and this is not in it: the phrase *R4 governance scan* survives three times in
`tooling/tests` — `run_tests.py:6` and `test_flow_repair_disposition.py:31` and `:1600`, all prose
in test docstrings. `tooling/tests` is construction-side and does not travel, so no caller ever
holds a tree where those collide.

### 7.4 `document-harness/ONBOARDING.md:150` names an instrument-held hook path

*the hook is `.githooks/pre-commit` at this repository's root, and a caller does not wire it* —
an instrument-held path token in a product-tier file. `ONBOARDING.md` is product-tier row 4 but
is **not** an instruction-layer member, so neither `sweep_refs` nor `layer_path_check` reaches
it, and ruling 24's measured nine did not include it. Four sibling tokens in the same file
(`:32`, `:52`, `:63`, `:148`) are instructions to a caller to create its own hook and are
caller-held. Recorded in rider `e10-cannot-see`, not fixed.

**Answered 2026-08-30 — plan ruling 37 (c), written forward; the paragraph above stands word for
word (`HD-59`).** The token is de-named at `65ecdac` on ruling 24's principle, the sentence being
one that can stand without the reference: `:150` now ends *the hook that calls it is the
instrument's own, at the instrument's own root, and a caller does not wire it* — no path and no
name, and the whole of its meaning kept. The four siblings at `:32`, `:52`, `:63` and `:148` stay,
each an instruction to a caller about the hook it writes for itself and so caller-held. Rider
`e10-cannot-see`'s touch note is updated in the same commit and the row is kept: what it banks is
that the guard cannot see this token shape at all, which is unchanged, and adding an item to
`E10`'s enumeration is design.

## 8. Disclosed rather than softened

- **A freeze marker was written and deleted by hand.** Smoke-testing the new script's two
  review-side modes against this repository wrote `.harness/review-pending.json`. No session was
  dispatched on it, no commit landed while it existed, and I deleted it in the same working
  block. The marker is per-checkout and gitignored; nothing committed carries it. Same shape as
  the disclosure the plan's *Disclosed at opening, not softened* paragraph records.
- **`.goals/` is untracked and is not this round's.** It held two plan copies and five
  `.commitmsg` drafts when this round opened; this executor added its edit scripts, its mutation
  harness and its four commit-message files there. Nothing in it is staged, and no commit of
  this round names it.
- **What the `layer_path_check` exits are worth** is stated at acceptance 9 rather than left to
  be inferred: three of the four are vacuous on a clean index, and the replay is the one that
  carries weight.
- **The FULL has not run.** Every commit of this round is a candidate under `E9`: no independent
  review has occurred, so nothing here is verified by anyone but its author, and the mutation
  results above prove that tests bind, never that they are sufficient.
