# FULL review — round `DE-PREFIX`, subject `4410899..39a21a8`

Verdict: **`CHANGES_REQUIRED`** — 2 blockers, 4 low, 6 observations.

Independent session. I was handed a range and the path of my standing instruction, nothing
else; round, batch, budget, authorization, obligations and every figure below are re-derived
from this repository. Where a figure of mine and a figure of the round's differ, mine is the
one I ran and the command is shown.

## 0. Dispatch as received, and what I declined to take from it

The dispatch named the review contract at
`migration/document-work-assurance-v3/v3-harness-review-contract.md`. That file is a stub;
it names `document-harness/CONSTRUCTION-CHECKLIST.md` as its successor and its own
counterpart, and that is what I read end to end (both sides, `E1`–`E12` and `R1`–`R10`),
followed by `HARNESS-DECISIONS.md` `§live`, which `E10` owes at a round's opening and which
outranks the checklist on conflict.

The dispatch also asserted that the subject was a range and that a record belongs at a named
path. Those are transport. It asserted nothing about the round, and I took nothing on
report: `HD-50` in the decision log is where I found that this is R3 of batch
`DTW-INDEPENDENCE`, that its authorized content is *去 `ResearchSystem/` 前缀 + `E10-sync`
三处同 commit + 守卫认全类 + `sweep_refs.py` 入仓*, and that the last two of those four were
moved into R3 from R2 by a user ruling of 2026-08-20. `CONSTRUCTION-LEDGER.md` line 123
confirms R3 as the queue head and carries the *"实测只 2 处 `parents[4]` 会断"* figure the
round re-measures.

## 1. Subject, re-derived

```
$ git log --oneline 4410899..39a21a8
39a21a8 V3-DE-PREFIX-v1
c969109 V3-REVIEW-RECORD-DE-PREFIX-4410899-v1
$ git rev-parse HEAD
39a21a8d7ee469cee966be5ccc63817c6dc3c071
$ git status --porcelain=v1
(empty)
```

Two commits. `c969109` is the record of the `E10` opening cold read, which under `E9` is not
a round and spends no budget; `39a21a8` is the round's candidate. `E9`'s sequencing clause —
*"from dispatch to that commit the branch takes no commit but the record itself"* — holds
exactly: the record is the only commit between the opening tip and the candidate. No FULL
had occurred before this one, so the guard correction described in journal §3.5 is correctly
classified as a pre-submission correction consuming nothing.

### 1.1 What the move actually did, classified by hand

The clean way to check a 300-file rename is not to read the renames. It is to strip the
prefix from the base tree and compare mode+blob:

```
base files: 316   tip files: 319
identical mode+blob after prefix strip: 294
content or mode changed: 22
only in base: []
only in tip: ['document-harness/journal/de-prefix-2026-08-20.md',
              'migration/document-work-assurance-v3/v3-cold-read-4410899.md',
              'tooling/sweep_refs.py']
```

Nothing was lost, nothing changed silently, and the 22 changed files are exactly the
declared edits (the two contract stubs, six of the ten members, the hook, `dispatch.py`,
`init_target.py`, `sweep_refs.py`'s absence aside, and nine test files). Independently:

```
$ git ls-tree -r 4410899 -- ResearchSystem/ | wc -l     313
$ git ls-tree -r 39a21a8 -- ResearchSystem/ | wc -l     0
```

313 is right, and `ResearchSystem/` is gone from the tree. `.githooks/pre-commit` is `100755`
on both sides — `ONBOARDING.md` item 9's executable-mode rule survived the round that
rewrote its contents.

### 1.2 `E2` — frozen bytes, checked per file

```
$ git ls-tree -r 4410899 -- ResearchSystem/contract/ ResearchSystem/schema/document-assurance-v3/ \
    | awk '{print $3,$4}' | sed 's#ResearchSystem/##' | sort  > base
$ git ls-tree -r 39a21a8 -- contract/ schema/document-assurance-v3/ | awk '{print $3,$4}' | sort > tip
$ diff base tip     (no output)      $ wc -l tip     18
```

Eighteen files, blob-for-blob identical, paths differing only by the stripped prefix.
Supersession-1 is still `68031fa2`, supersession-2 still `e1a2f26b` — the two ids `E2` names
literally. `HD-44` rules that moving those bytes is not a write; a rename inside one
repository is the weaker case of the same ruling, and the blob equality above is the proof
rather than the assertion. `E2`'s own text carried the pack path *without* the prefix
already, so the side effect of the move is that `E2`'s path token now resolves where it did
not before.

## 2. The round's claims, checked against what it did

### 2.1 The depth re-measurement reproduces, and the structural reason holds

```
$ git checkout 4410899 && grep -rn "parents\[" ResearchSystem/tooling/ --include=*.py
```

Nineteen hits; the eight `__file__`-rooted ones are the journal's list, and exactly two —
`test_candidate_checks.py:83` and `test_readme_enumeration.py:34` — were `parents[4]`
reaching for the *repository* root across the old instrument/repository boundary. Both
became `parents[3]`. Every other site names the instrument root and kept its depth, because
the resolving file and its target moved up together. I checked the four sites the journal's
`tooling/`-scoped grep does not reach — `assurance/templates/run-v2/{run_evidence_v2,
run_bind_v2,run_repair,run_retire}.py`, each `RS_ROOT = HERE.parents[2]` — and each survives
for the same reason; the `run_dir.parents[3]` defaults in the same tree are caller-layout
facts and are correctly untouched. The ledger's "only 2" figure holds at today's tree.

### 2.2 `E10-sync` (`HD-22`): three mirrors, one commit

Membership sentence (`CONSTRUCTION-CHECKLIST.md` `E10`), `LAYER`
(`tooling/hooks/layer_path_check.py`) and `EXPECTED`
(`tooling/tests/document_harness/test_precommit_checks.py`) all changed in `39a21a8`, and
the commit body names all three, which is what `HD-22` asks for beyond the change itself.
`test_layer_equals_the_hand_written_membership` pins two of the three legs; the prose leg
still has no guard, which is the standing rider and not this round's defect.

### 2.3 The whole-stock scan reproduces

```
$ python -c "... unresolved_tokens over the complete text of all ten members ..."
HIT contract/…-supersession-1.md | ResearchSystem/migration/…/W2/W2-design.md
HIT contract/…-supersession-1.md | ResearchSystem/migration/…/W2/W2-record.md
HIT contract/…-supersession-2.md | assurance/runs/
HIT contract/…-supersession-2.md | templates/run-v2/
HIT contract/…-supersession-2.md | ResearchSystem/migration/document-work-assurance-v3/
members 10 hits 5      missing []
```

Five residual sites, all inside the two `E2`-frozen supersessions, all excepted by `E10`'s
own clause while frozen; the eight writable members carry no non-resolving path token. The
4→5 flip the journal describes is real — two frozen tokens started resolving, three stopped.
10/10 members resolve.

### 2.4 Member blobs across the round

```
CHANGED CONSTRUCTION-CHECKLIST.md 92cbaea3 -> c2674385   CHANGED README.md   be4766fc -> 7de70e11
CHANGED EXECUTION.md              6dc79f3f -> 0d0c617b   CHANGED REVIEW.md   4a407f65 -> 946b4beb
CHANGED v3-harness-operating-contract.md 70f3e5dd -> 6d571492
CHANGED v3-harness-review-contract.md    bc395e1c -> 29bdc9fb
same    ORCHESTRATION.md 80f42658   same supersession-1 68031fa2
same    supersession-2 e1a2f26b     same paragraph-map.schema.json 09aa8699
```

`ORCHESTRATION.md` crossed a whole-tree re-rooting with zero bytes changed, which is what
`XREPO-REFS`'s de-naming bought. Six members changed, so this round owes the layer an
independent read before any round relies on the amended text; the next round's opening cold
read discharges it if its record states these blob ids.

### 2.5 The guard, mutation-tested against my own restores (`E4`, `R8`)

Scratch clone under the session scratchpad, pristine copy taken first and every restore
verified by sha256 (`ba11c329f444f4bfbf72d4c60e95d3db05412cdb74305803d4404a5a020e5689`).

| mutation | result | reads |
|---|---|---|
| `if not resolved:` → `if False:` | **6 failed, 8 passed** — every must-fire red, every negative control green | the tests bind the class, not an instance |
| `candidate.exists() and candidate.is_relative_to(root)` → `candidate.exists()` | **1 failed** — only `test_resolution_escaping_the_repo_root_does_not_count` | the escape branch has its own binding test |
| `-M` dropped from the staged diff | **2 passed** — rename tests stay green | reproduces the journal's own honest negative; `-M` is a pin against `diff.renames=false`, not what the test binds |
| pathspec limitation restored (the original defect shape) | **1 failed, 1 passed** | the rename test binds the actual fix |

The round's four mutation claims all reproduce, including the one it declined to claim as
tested. The battery reproduces too: `738 passed in 102.10s` from `tooling/`, and
`--collect-only` gives **733 at `4410899`, 738 at `39a21a8`** — the delta is +5, not +3.

### 2.6 `sweep_refs.py`

Runs, imports membership and path shape from the guard rather than mirroring them a fourth
time, decides nothing, exits 0. Its PATHTOK half agrees exactly with the guard predicate I
ran in §2.3. Its live tally is **17**, not the 18 the journal prints (see `L-2`).

### 2.7 The read's findings, carried as the record commit promised

`L-1`'s exact bytes are at `EXECUTION.md:258-262` in the supplied form
(`<control root>/control/paragraph-map.json` plus the holder sentence), and the placeholder
shape is invisible to the guard by design, pinned by
`test_a_placeholder_token_is_invisible_by_shape`. `L-2` is answered inside the clause
rewrite. Read `O-1`'s vacuous `contract/` row is restated as today's fact and I confirmed
that directory holds exactly the three files. `L-3` is declared as banking at closeout.

## 3. Blockers

### `B-1` — the round falsified the description of `layer_path_check` in four live places and swept none of them; one of the four is an `E10` member, and the two guards' relationship is now documented backwards

**Locations.**

- `document-harness/README.md:36` (**`E10` member**, *Local enforcement* row): *"the
  candidate-side path lint, **which takes the class the instruction-layer check skips as
  possibly illustrative** and blocks a newly written path that exists nowhere in the index"*
- `tooling/hooks/candidate_path_check.py:8-10`: *"`layer_path_check.py` deliberately skips a
  token that resolves nowhere, because it *may be illustrative*. This one takes exactly that
  skipped class…"* — and `:23-25`, *"the class the older guard waves through is exactly where
  the defect this lint exists for was found … a stricter rule applying on top"*
- `tooling/rsclib/document_harness/paths.py:15-19`: *"the three branches
  `tooling/hooks/layer_path_check.py` has always used … That guard then stops: a token
  resolving nowhere is skipped, because it *may be illustrative*."*
- `tooling/tests/document_harness/test_precommit_checks.py:239` (in a file this round
  rewrote 130 lines above): *"SIMP-A4: the class `layer_path_check` skips as *may be
  illustrative*, split."*

**Ground truth violated.** `tooling/hooks/layer_path_check.py:68-77` now blocks that class,
and `CONSTRUCTION-CHECKLIST.md` `E10` — written in this same commit — says so: *"blocks … every
path-shaped token that resolves nowhere inside this repository … which since round
`DE-PREFIX` is the class entire."* Two members of the ten-file instruction layer now
contradict each other about the same guard. `E3` binds the assertion side of this
(*"a factual assertion written into instruction text runs the command that could falsify it
first"*), and `E7` / `HD-41` ④ bind the sweep side: the fix is the class, not the instance,
and the grep for it is one command.

**This is not only stale prose — the stated relationship is now inverted.** Measured in the
scratch clone at `39a21a8`, one staged line added to `document-harness/REVIEW.md`:

```
run `tests/document_harness/run_tests.py` to check

$ python tooling/hooks/layer_path_check.py
pre-commit BLOCKED: … `tests/document_harness/run_tests.py` — resolves nowhere …    exit 1
$ python tooling/hooks/candidate_path_check.py
(no output)                                                                          exit 0
```

The older guard blocks what the newer one passes as SHORTHAND. "A stricter rule applying on
top" and "takes exactly that skipped class" describe the pre-`DE-PREFIX` world; in the
post-round world the two guards disagree in the opposite direction, and nothing in the tree
says so.

**Why blocking.** `ONBOARDING.md` item 9's Owner cell sends a new caller to exactly the
`README.md` row that is wrong, to learn *"what each guard does"*. A construction session
reading it will believe the layer guard waves through the caller-held-path class that this
round exists to close. And it is the same defect shape the previous round's FULL blocked on
(`v3-review-full-dd18226.md` `B-1`: the clause said more about the guard than the guard did)
— reappearing one round later on the other side of the same sentence.

**Minimum fix.** Rewrite the four sentences to the post-`DE-PREFIX` division of labour: the
layer guard blocks non-resolving tokens on added lines of the ten members; the candidate lint
covers work products, where its shorthand carve-out still applies and where the layer guard
never looks. No new machinery, no rule added — `E6`'s test is satisfied because the fix is
the text changing.

### `B-2` — the new whole-diff parser fail-opens: one `++`-leading added line silences the rest of that member, and `E10`'s clause claims an exhaustive list of what the guard cannot see

**Location.** `tooling/hooks/layer_path_check.py:98-105`, the loop in `added_lines_by_path`:

```python
if line.startswith("+++ b/"):
    current = line[len("+++ b/"):]
elif line.startswith("+++"):
    current = None
```

A content line beginning with `++` renders in the diff as `+++…`, misses the first branch
(4th char is `+`, not a space), hits the second, and sets `current = None` — so **every
remaining added line of that file is dropped from the scan**. Reproduced in a disposable
repository, same file, same bad token, one line of difference:

```
clean / +++ a pasted diff header / see `no/such/file.md`     ->  exit 0   (NOT blocked)
clean / an ordinary line         / see `no/such/file.md`     ->  exit 1   (blocked)
```

**Ground truth violated.** `E10`, this commit: *"What the guard still cannot see is held by
this clause alone: a token carrying a placeholder segment falls outside its path shape, prose
and markdown links carry no backtick token for it to find, and the standing text it never
re-scans stays unscanned."* That enumeration is offered as complete and this is a fourth
member of it, introduced by the same commit. `E4` is the other half: the round mutation-tested
the resolution predicate thoroughly and did not probe the parser it had just rewritten under
the pressure of its own blocked commit.

**Scope of live damage.** Zero today — I scanned all ten members and no line begins with
`++`. The defect is latent, and the guard is advisory and bypassable; that is why it is
reported as a guard defect rather than as a missed defect. It is also a regression: the
per-file parser this round replaced (`added_lines`, base `layer_path_check.py`) dropped only
the offending line and kept scanning.

**Minimum fix.** `elif line.startswith("+++ ")` — four characters including the space. That
routes `"++++ b/…"` to the content branch where it belongs while `"+++ /dev/null"` still
resets. One residual ambiguity survives any text parse of `-U0` output (a content line
literally reading `++ b/x`); disclose it in the docstring rather than claim it away.

## 4. Low

### `L-1` — journal §5's battery figure is not the figure at the candidate commit, and it carries an `E3` re-run claim

§5 states **736 passed** with *"733 before the round, +3 net from the LayerPath rewrite
(7 tests out, 10 in). **Re-run green immediately before the candidate commit.**"* Measured:

```
$ python -m pytest -q                                  738 passed in 102.10s
$ python -m pytest -q --collect-only  @ 39a21a8         738 tests collected
$ python -m pytest -q --collect-only  @ 4410899         733 tests collected
```

The delta is +5 (7 out, 12 in), not +3. §3.5 and the commit body both say 738; §5 is the
pre-correction measurement left in place with a re-run claim attached to it, which is exactly
the shape `E3` names. `HD-23` puts a journal number's correction outside the `E9` fix leg, so
this is cheap to close.

### `L-2` — journal §2's "After" block is edited tool output under a command prompt, and its tally is one no run of that command returns

The block is headed `$ python tooling/sweep_refs.py .` and captioned *"this round's tree,
immediately before the candidate commit"*, contains a `LINK … ../../README.md` row annotated
inline `<- fixed this round (see §4)`, and totals **18**. Run at the candidate tip:

```
$ python tooling/sweep_refs.py .
… 17 rows, no LINK row …
-- 17 caller-held or unresolvable references over 10 members
```

Either the run predates the §4 fix (so the caption is wrong) or the row was carried in by
hand (so it is not tool output). `E3` asks for the output of the command that produces the
figure, or no figure. Adjacent to this: the commit body's *"whole-stock run plus the guard
predicate leave the eight writable members clean"* is true of the guard predicate and not of
the sweep, whose 12 NAMETOK rows sit in two writable members; journal §2 disambiguates it,
the commit body does not.

### `L-3` — `E8`'s *no trailers* is broken by the candidate, and by nothing else in this repository's history

```
$ git log --format='%h %(trailers:key=Co-Authored-By,valueonly)' --all | grep -c Claude
1
```

That one is `39a21a8`, which carries `Co-Authored-By:` and `Claude-Session:`. The read record
`c969109`, committed by the same session minutes earlier, carries neither. `E8` also forbids
amending, so there is no in-place repair: the honest disposition is a recorded deviation at
closeout, on the precedent of `HD-38`'s *"已落地的三个混装 commit 照记不回改"*. The rest of
`E8` holds — title `V3-DE-PREFIX-v1`, one dense paragraph, the kind named ("Candidate commit
of round `DE-PREFIX`"), and no push (`git branch -a --contains 39a21a8` returns `main` only,
against a real `origin`).

### `L-4` — the `E1` disclosure sentence asserts the condition `E1` defines as a self-check

The commit body reads: *"this session held orchestrator and executor (all four dispatch
holdings for the work side); the opening read `c969109` and the FULL to follow are dispatched
to sessions holding none of the four."* `R1`'s four holdings — dispatched by, prompted by,
scoped by, reported through — are properties of the **review**, and `E1` says *"All four in
the executor's hands is a self-check whatever it is called."* Read literally the first clause
claims that condition; the second clause then applies the four to the *reviewer*, which is
not the `R1` test. There is no such thing as "four dispatch holdings for the work side" in
the layer.

What `HD-46`'s recorded tiebreak asks for in this shape is an enumeration: on my reading the
executor held **dispatched-by, scoped-by and reported-through**, while **prompted-by** sits
with the standing contract through `dtw dispatch` — a middle state, disclosed, not called
structurally independent. The sentence's direction of error is conservative (it claims less
independence than the round has), but a later audit reading `E1` against it would void a
round that was in fact independently reviewed. Rider `e1-disclose-home` is where this
sentence was placed one round ago; the wording is what needs the fix, not the home.

## 5. Observations

**`O-1` — measurement scope in the journal's two absolute claims.** §1 calls its eight-site
list a *"Full enumeration"* with *"(comment-only sites omitted here)"*, but two of the omitted
sites are code, not comments (`test_dispatch.py:394` and `:518`, both `parents[1]` fixture
paths); the grep also stops at `tooling/`, and four more depth sites live under
`assurance/templates/run-v2/`. I checked all of them and the conclusion is unaffected — this
is `HD-41` ①/② about declaring the range an absolute quantifier is claimed over, not about
the answer. Same shape in §4: *"A second sweep for broken (non-escaping) relative links across
all live tracked markdown, records excluded, returned zero"* — my run returns **4 escaping**
(exactly the four named, all in records/archives) and **one** non-escaping broken link outside
`migration/`, at `document-harness/journal/simp-a4-2026-08-06.md:125`. It is a pre-existing
missing target rather than a casualty of the move, and it turns on whether a journal counts as
a record, which the sentence does not say.

**`O-2` — rider `mount-inert`'s deadline arrived in this round and is recorded nowhere in the
subject.** Its deadline is written as *"去前缀那一件（`$H` 第一次解析不到的那一刻）"*, and one of
the two surfaces it names — `layer_path_check`'s `LAYER` — was touched by this commit. Neither
redemption nor its impossibility appears in the commit body, the journal, or the bank. The
structural fact underneath: the `$H` in question lives in the **caller's**
`.githooks/pre-commit`, outside this repository, so no commit here can redeem a row that names
an in-repository surface as its trigger. This repository's own hook is not exposed — it fails
loudly (`echo` + `exit 1`) when `CHK` is missing. *Ceiling (`R4`, outside subject):* the
caller's hook already reads the post-move path as an **uncommitted** working-tree edit; that is
the caller's closeout, not mine to adjudicate.

**`O-3` — rider `frozen-path-prefix` is stale at the tip.** The row counts four tokens in two
classes and gives `templates/run-v2/`'s true home as
`ResearchSystem/assurance/templates/run-v2/`; measured now it is five tokens and
`assurance/templates/run-v2/`. The round declares the update rides closeout, which is the
right channel; recorded so the declaration is not the only place it exists.

**`O-4` — `sweep_refs.py` entered `tooling/` with no test, and journal §2's evidence table is
its output.** It decides nothing and always exits 0, so `E6` argues against building machinery
around it, and its PATHTOK half agrees exactly with the guard predicate when I ran both. Noted
because a diagnostic whose output is banked as a round's evidence has the same
untested-instrument shape this harness usually names out loud — here the cross-check exists
and simply is not written down.

**`O-5` — the root `README.md` now contradicts itself across twenty lines.** `:55` answers
*"Is there a CLI?"* with `ls tooling/dtw.py` — I ran `python tooling/dtw.py --help` and it
lists seven operations — while `:60` still says *"**The CLI is not here.**"* and `:62` that
*"the CLI extraction alone will not make the suite green"*. Both are rider
`readme-cli-stale`, `HD-50` explicitly banks the human-facing root README, and leaving them is
authorized; recorded because this round did edit that file's adjacent sections and the
falsified sentences are now the nearest neighbours of a de-prefixed truth.

**`O-6` — one piece of load-bearing scoping is chat-only (`R2`).** Journal §1 justifies leaving
`candidate_path_check`'s surface constants untouched by *"the user's R3-scoping choice on the
preview card (2026-08-20)"*. `HD-50` records the 2026-08-20 ruling that moved two items into
R3, but not the choice to keep rider `submod-index`'s surface closed. `E11`'s preview card has
no carrier in the repository — the ledger already lists that as open — so this is `R7`: I state
the ceiling and move on. The round's four authorized items are all visible in `HD-50` and all
were done.

## 6. Process and boundary check (run second, per `R3`)

- **`E9` budget.** One FULL (this one), no fix leg spent, no VERIFY owed yet. The read spent
  nothing; the guard correction was pre-submission and spent nothing. Correct.
- **`E2`.** No frozen byte written (§1.2). Correct.
- **`E10` amendment channel.** The clause rewrite adds bounds and changes what the guard
  sentence asserts, so it is design and opens a round — which is what happened. The layer read
  it owes is still owed (§2.4).
- **`E12`.** Handoff was a range via `dtw dispatch`, no per-acceptance argument. Correct.
- **`E8`.** Title, kind, single paragraph, explicit staging, no amend, no push — all correct;
  trailers are `L-3`.
- **`E1`.** Disclosure present and in an allowed carrier; wording is `L-4`.
- **Change boundary.** Every one of the 22 content changes is inside *去前缀 / 守卫认全类 /
  `sweep_refs.py` 入仓 / `E10-sync`*, including the root `README.md` *Layout* rewrite, whose
  previous heading was literally *"and why it still says `ResearchSystem/`"*. Nothing outside.
- **`R10` routing.** `B-1` and `B-2` are implementation, not bank material. `L-1` and `L-2` are
  journal numbers (`HD-23`). `L-3` is a recorded deviation. `L-4` and the observations are the
  orchestrator's to route; `O-2` names a row whose redeem surface may be structurally
  unreachable, which is a question for the user under `R5`, not a conclusion of mine.

## 7. Disclosure (`R4`)

**Read in full:** `CONSTRUCTION-CHECKLIST.md`; `HARNESS-DECISIONS.md`; `HARNESS-RIDERS.md`;
`CONSTRUCTION-LEDGER.md`; root `README.md`; `.githooks/pre-commit`; `.gitignore`;
`tooling/hooks/layer_path_check.py` at both revisions; `tooling/sweep_refs.py`;
`document-harness/journal/de-prefix-2026-08-20.md`; the full diff of all 22 changed files;
the two commit bodies.

**Sampled:** `v3-cold-read-4410899.md` (§4 findings and the outline in full, §§1–3 by
heading); `document-harness/README.md`, `EXECUTION.md`, `REVIEW.md`, `ONBOARDING.md` and
`assurance/templates/run-v2/README.md` at their changed hunks plus the sections those hunks
sit in; `candidate_path_check.py` and `paths.py` docstrings; `v3-review-full-dd18226.md` at
the `ExperimentLab` citation.

**Only probed:** the 294 unchanged files — verified by mode+blob equality after prefix strip,
not by reading; `ORCHESTRATION.md` (blob unchanged, and clean under both instruments);
`dispatch.py` beyond `instrument_relative` and `CONSTRUCTION_ROLE_INSTRUCTION`; the run-v2
template scripts beyond their `parents[n]` lines.

**Re-executed:** the battery (738, and 733/738 collect-only across the range); the whole-stock
guard predicate; `sweep_refs.py`; the escape/broken link sweep; the `parents[` enumeration at
base; four guard mutations with sha256-checked restores; two adversarial probes of the new
parser; the two-guard divergence probe of `B-1`; `dtw --help`; the frozen-blob diff.

**`UNVERIFIABLE`, not folded into supported:**

- The `E11` preview card and the scoping choice cited from it (`O-6`) — no carrier in the
  repository.
- *"Battery re-run green immediately before the candidate commit"* — I can show the tree at
  `39a21a8` is green, not that a run happened before the commit was written. A process claim,
  marked, not verified.
- Whether the 22 content edits were staged as explicit paths rather than `add -A` — not
  observable from a commit.
- Journal §2's "Before: 16 hits" — `sweep_refs.py` does not exist at `c969109` and imports
  `RUNTIME_PREFIX`, which the base guard does not define, so the figure is not reproducible as
  written. It is not load-bearing for any conclusion here.
- Mutation proves these tests have binding force; it does not prove that force is sufficient,
  and `B-2` is one measured place where it was not.

## 8. Verdict

**`CHANGES_REQUIRED`.**

The re-rooting itself is the strongest part of this round and I could not fault it: 294 files
identical byte-for-byte after the prefix strip, zero losses, the frozen eighteen untouched at
their named blob ids, the depth argument structural rather than lucky, the three `E10-sync`
mirrors in one commit, the guard's own first live firing caught and its correction pinned both
ways with mutations that reproduce — including one the round honestly declined to claim.

What it did not do is finish the class it opened. Teaching the guard the whole class made four
standing sentences false, one of them in an `E10` member that `ONBOARDING.md` points a new
caller at, and left the two guards' relationship documented in the reverse of what it now is —
measured, not inferred. And the parser written to unblock the round's own commit fail-opens on
one line shape, in a commit whose clause tells every future reader that what the guard cannot
see is now a closed list of three.

Both fixes are text and one character. Neither needs new machinery, which is the shape `E6`
asks a fix to have.
