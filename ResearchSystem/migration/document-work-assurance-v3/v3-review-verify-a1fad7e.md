# VERIFY review — round `SIMP-A4` (repair `a1fad7e`)

| | |
|---|---|
| round | VERIFY, construction-side (`CONSTRUCTION-CHECKLIST.md` E1–E12 / R1–R10) |
| subject | `285c59646e229157f2671a4999fd3fc51a40d676..a1fad7ee1e2cbd1bcf4a848e41db59520c6ec2d8` |
| range content | two commits — `239f56a` (kind: record), `a1fad7e` (kind: review fix) |
| **verdict** | **`REVIEWED_NO_BLOCKER`** |
| findings | 5 low, 3 observations |
| record | this file; the execution side commits it (`R6`) |

The three accepted findings close, and they close for the reason the fix claims rather than by
assertion — I re-implemented the replay independently and reproduced the numbers before reading
the executor's. The fourth change, the one the FULL did not have, is the substantive one and it
is right: the scope error was real, my own replay reproduces **5 of 6** instruction freezes
blocked by the shipped-then form and **0 of 6** by the shipped-now form, with the one real
defect still caught. Nine of ten mutations of my own are killed by the round's own tests.

The lows are about **reach** again, and two of them are the same shape the FULL found, one level
down: a sentence in `EXECUTION.md` that the code contradicts, a docstring left describing the
scope the round replaced, and a defect class closed on two of its three invocations — where the
third now produces a false *block* rather than a silence.

## 1. Subject, re-derived (`R2`)

Handed one range and nothing else. Round, budget, authorization and every figure below are
re-derived here; no reported number is accepted.

```
$ git rev-parse HEAD              -> a1fad7ee1e2cbd1bcf4a848e41db59520c6ec2d8
$ git rev-parse 285c596           -> 285c59646e229157f2671a4999fd3fc51a40d676
$ git status --porcelain          -> (empty)
$ git rev-parse --abbrev-ref HEAD -> document-work-assurance-v3
$ git log --oneline 285c596..HEAD
  a1fad7e V3-SIMP-A4-CANDIDATE-LINT-FIX-v1
  239f56a V3-REVIEW-RECORD-SIMP-A4-CANDIDATE-LINT-285c596-v1
$ git diff --stat 285c596..HEAD
  ResearchSystem/HARNESS-LEDGER.md                                     |  14 +-
  ResearchSystem/document-harness/EXECUTION.md                         |   6 +-
  ResearchSystem/document-harness/README.md                            |   2 +-
  ResearchSystem/document-harness/journal/simp-a4-2026-08-06.md        |  54 +-
  ResearchSystem/migration/document-work-assurance-v3/…-full-285c596.md| 364 +
  ResearchSystem/tooling/hooks/candidate_path_check.py                 |  66 +-
  ResearchSystem/tooling/rsclib/document_harness/paths.py              |  28 +-
  .../tests/document_harness/test_precommit_checks.py                  |  70 +
  8 files changed, 567 insertions(+), 37 deletions(-)
$ cat .harness/review-pending.json
  {"kind": "construction-round",
   "subject": "285c5964…..a1fad7ee…", "dispatched_at": "2026-08-06T07:44:39+00:00"}
$ git check-ignore -v .harness/review-pending.json -> .gitignore:19 (untracked; marker is out-of-band)
```

**Changed paths, classified by hand** (not from any commit body):

| path | class | frozen by `E2`? |
|---|---|---|
| `document-harness/EXECUTION.md` | instruction layer (`E10` member 3) | no |
| `document-harness/README.md` | instruction layer (`E10` member 2) | no |
| `HARNESS-LEDGER.md` | control-plane pointer | no |
| `document-harness/journal/simp-a4-2026-08-06.md` | round record | no |
| `migration/…/v3-review-full-285c596.md` | review record (`R6` channel) | no |
| `tooling/rsclib/document_harness/paths.py` | product code | no |
| `tooling/hooks/candidate_path_check.py` | product code | no |
| `tooling/tests/document_harness/test_precommit_checks.py` | test | no |

**Round and budget (`E9`).** `E9`'s test applied myself, not accepted from the label: a valid
independent FULL *had* occurred (`239f56a`, verdict `REVIEWED_NO_BLOCKER`, subject
`a27022f..285c596`), so `a1fad7e` is the round's one user-approved fix and it obliges this
targeted VERIFY. The FULL's own §6 accounting agrees. The freeze window holds on both legs: from
the FULL's dispatch to `239f56a` the branch took no commit but that record, and from this
dispatch (07:44:39Z) to now the branch has taken none at all — `a1fad7e` committed 07:42:20Z,
two minutes *before* the marker was written, and the tip still equals the dispatched subject.

**Authorization.** The committed record of the fix decision is `HARNESS-LEDGER.md`'s pointer
line (`SIMP-A4` 欠 VERIFY) plus journal §9, which records the user framing the block/comply
dichotomy and ruling option A with four items in one batch. The rulings themselves are
chat-origin. `R7` ceiling stated, not treated as a block.

## 2. Do the accepted findings close (`R3` — implementation first)

### The fourth change — the scope error, replayed from scratch

This is the change that carried the round, and it did not come from the FULL, so I gave it the
most work. I extracted both module versions out of git into a scratch tree and drove each over a
reconstructed staged state (`git worktree` at `commit~1`, `git read-tree commit` — `check()`
reads only the index and the index-versus-HEAD diff, so no checkout is involved and the replay
is exact).

Every commit that first added a run `instruction.md`, both versions:

| freeze commit | run | pre-fix | post-fix | token it tripped on |
|---|---|---|---|---|
| `60e2f6f` | p4-bridge | **BLOCK** | pass | `…/contract/amendments/2026-08-01-a1-p4-activation-successor.md` |
| `9f0cc80` | p4-doc | **BLOCK** | pass | `handoffs/P4-close.md`, `…/inventory/amendments/2026-07-18-child-gap.md` |
| `2f07ce2` | p5a-firewall | **BLOCK** | pass | `…/contract/amendments/2026-08-02-a2-p5a-scoped.md` |
| `de8b286` | p5a-shells | **BLOCK** | pass | `…/inventory/amendments/2026-08-02-p5a-shells.md`, `fixtures/cases.json` |
| `71be9e1` | p5b-firewall | **BLOCK** | pass | `…/contract/amendments/2026-08-05-a3-p5b-scoped.md` |
| `2687d8c` | p3-corr + w1-r1 (home move) | block, but on other files | block, on other files | no `instruction.md` line in either output |

**5 of 6, exactly as claimed**, and the blocked token is in every case the R1 "a new file `…`
exists" sentence naming the amendment the run is *required to write*. The sixth is a directory
move, not a freeze, and neither version trips on its `instruction.md`.

Post-fix scan scope over the tracked tree, asserted per file rather than by prefix argument:
all nine `.md` under `assurance/runs/` — seven `instruction.md` plus two
`control/audit-rounds.md` — return `scanned=False`; `assurance/README.md`, the two
`shadow/round-3/dispatch-prompt-run-*.md` and `templates/run-v2/README.md` return `True` (`O-1`).

**The capture is intact.** Replaying both versions over the four candidate promotions:

```
                     pre-fix   post-fix
0e68377 p4-doc          0         0
3354777 p5a-firewall    0         0
d749406 p5a-shells      0         0
ad00fec p5b-firewall    1         1   ResearchSystem/contract/amendments/2026-08-05-a3-p5b-scoped.md:
                                        `Thesis/literature-analysis/sota-comparison.md`
```

Identical before and after — the scope change removes false positives and nothing else. Over the
80 most recent non-merge commits the post-fix code blocks **once**, on that same real defect; the
pre-fix code blocks **four** times over the same window — the same defect (twice, once in the
candidate and once in the promotion merge) plus two specification-surface false positives
(`p5b-firewall/instruction.md` at the freeze, `p5b-firewall/control/audit-rounds.md` at START).
That is independent corroboration of the fix's whole claim. Method dependency in `O-2`.

### `L-1` — non-ASCII filenames — **closed on the reported instance, open on the class** (see `L-3` below)

The reported instance is fixed and the fix is real, measured against git rather than reasoned:

```
$ git diff --cached --name-only                       -> "Thesis/\347\254\224\350\256\260/note.md"
$ git -c core.quotepath=off diff --cached --name-only -> Thesis/笔记/note.md
```

Without the flag the name loses its `.md` suffix, `scanned()` drops it, and the file is never
examined. With it, the round's own must-fire test blocks the planted token. Mutation V3 (drop the
flag from `check()` only) turns exactly that test red.

### `L-2` — the division of labour — **closed, and the corrected claim is exact**

The new docstring asserts "the six Markdown instruction-layer members outside `NOT_SCANNED` are
scanned by both". I did not count from the source; I staged an unresolvable token into each of
`layer_path_check.LAYER`'s nine members in a scratch repository and ran both guards:

```
  candidate=1  layer=0  scanned=True   document-harness/CONSTRUCTION-CHECKLIST.md
  candidate=1  layer=0  scanned=True   document-harness/README.md
  candidate=1  layer=0  scanned=True   document-harness/EXECUTION.md
  candidate=1  layer=0  scanned=True   document-harness/REVIEW.md
  candidate=0  layer=0  scanned=False  migration/…/v3-harness-operating-contract.md
  candidate=0  layer=0  scanned=False  migration/…/v3-harness-review-contract.md
  candidate=1  layer=0  scanned=True   contract/…-supersession-1.md
  candidate=1  layer=0  scanned=True   contract/…-supersession-2.md
  candidate=0  layer=0  scanned=False  schema/…/paragraph-map.schema.json  (not .md)
```

Six, exactly — and in all six the newer guard blocks where the older deliberately passes, which
is the override the corrected text now states. `README.md` row 33 carries the same correction and
carries it accurately. `EXECUTION.md` carries it and adds one sentence that does not hold —
`L-1` below.

### `L-3` — bare directory tokens — **closed; the stated figure is not (`L-5`)**

`_is_citation_shaped` now requires an interior slash for a trailing-slash token. Mutation V5
(back to one slash) reds the negative control; V6 (tightened to three) reds the must-fire
control; V7 (branch deleted entirely) reds the negative control. The rule is pinned from both
sides.

### `L-4`, `L-5` (from the FULL) — both landed

`README.md` row 33's run-on is gone — the clause was rewritten rather than patched with the one
supplied byte, and the rewrite is the `L-2` correction, so it rides the approved fix leg rather
than the free channel alone. `HARNESS-LEDGER.md` now reads 带进 P5B **三件** and carries the A3
`sota-comparison.md` divergence as the third; `wc -l` → **120**, at the cap, not over it.

## 3. Do the guards bind (`R8` / `E4`)

Ten mutations of my own, each written to reproduce a defect shape rather than to crash. Sources
copied to scratch and sha256-pinned, mutated in place, restored from the copy, digest re-checked
— never `git checkout --`.

```
pristine sha256 (working tree == git object at HEAD, both verified):
  candidate_path_check.py  9c7bfda39fbc839341998fbce29d4a505e1d8c3c336d61d1b39e011d18324b5d
  paths.py                 b0075d9bc903904fce7b67b31b3eb442c781ed55582c4479912171dbbd026ab5
  test_precommit_checks.py 09b6c8712e8668fdb759d94604e0863e3046aeb643b25d28e3dd2accb2456d6f
baseline 46 passed -> GREEN;  after restore 46 passed -> GREEN;  worktree clean
```

| # | mutation | result | red test(s) |
|---|---|---|---|
| V1 | `SPECIFICATION_SURFACE` emptied | KILLED | 4 |
| V2 | `SPECIFICATION_SURFACE` widened to `assurance/` (over-exclusion) | KILLED | 2 |
| V3 | `core.quotepath=off` dropped from `check()` | KILLED | `…non_ascii_named_work_product_is_still_scanned` |
| V4 | `core.quotepath=off` dropped from `staged_added_lines()` | **SURVIVED** | — (`L-4`) |
| V5 | directory rule `>=2` → `>=1` | KILLED | `…bare_single_segment_directory_is_prose` |
| V6 | directory rule `>=2` → `>=3` | KILLED | `…interior_slash_is_still_a_citation` |
| V7 | trailing-slash branch deleted | KILLED | `…bare_single_segment_directory_is_prose` |
| V8 | partition tuple reordered | KILLED | `…equals_the_hand_written_list` |
| V9 | fourth surface appended to `NOT_SCANNED` only | KILLED | 2 |
| V10 | fourth surface added to `NOT_SCANNED` **and** to the hand-written list | KILLED | `…three_kinds_partition_not_scanned` |

V2 matters on its own: the hand-written literal, not the module's tuple, is what catches an
over-wide exclusion — `E5` holds where it would have been easiest to break. V10 is the direct
test of the commit body's claim that "a fourth surface cannot be added without a reason": it
takes editing both the module and the expectation to get past the equality test, and the
partition test is then the one that fires. The claim is exact.

V4 is the one survivor and it is reported as `L-4`, not swept: it survives because that half of
the repair is inert, which I measured rather than argued.

## 4. Figures re-run (`E3`)

Every figure the commit body asserts, re-run now:

```
$ python -m pytest -q                                    -> 626 passed in 89.88s
$ python -m pytest tests/document_harness/test_precommit_checks.py -q -> 46 passed
$ python tests/run_tests.py      -> tests: 29  passed: 29  failed: 0  RESULT: OK
$ python tests/run_p4_tests.py   -> tests: 80  passed: 80  failed: 0  RESULT: OK
$ python tests/run_p5a_tests.py  -> tests: 32  passed: 32  failed: 0  RESULT: OK
$ python …/N0/fixtures/validate_fixtures.py -> 41/41 cases behaved as declared; failures=0
$ python rsc.py compile --check  -> live 153 | tombstone 0 | diagnostics 0 error(s), 0 warning(s)
$ wc -l ResearchSystem/HARNESS-LEDGER.md -> 120
```

All match. The suite total moved 619 → 626 and the file 39 → 46, which is the seven tests this
repair adds — the two arithmetic agree, so nothing was added or lost silently.

The one figure that does not reproduce is `412 → 373` (`L-5`).

## 5. Findings

No blocker. Five low, three observations. None inflated — a VERIFY has no second repair to
burn, and inflating any of these would strand a round whose repair leg is already spent.

### Low

**`L-1` `EXECUTION.md`'s new sentence puts a specification outside *both* homes, and this
harness's authoring gate reads exactly that document.**
Location: `ResearchSystem/document-harness/EXECUTION.md:157-159`. The passage reads:

> …it has two homes, neither of them the enum: the **authoring gate**, which reads the
> instruction, and the **pre-submission lint**, which reads the work product — the candidate, in
> a product run — and disposes of nothing… **A specification is neither**: it names the files the
> work is required to create, so those cannot exist when it is written.

Ground truth: `ResearchSystem/tooling/rsclib/document_harness/instruction.py:252` —
`def form_conformance(instruction_text: str)`. The authoring gate's argument *is* the
instruction, and a run's `instruction.md` — the very file `SPECIFICATION_SURFACE` was added to
protect — is the specification. So the sentence contradicts its own clause twenty words earlier.
On the only other reading, "neither of the two mechanisms", it is a category error that asserts
nothing. The commit body states the intent as "a sentence placing a specification outside both
homes", so the text says what was meant; what was meant is what is wrong.

The sibling edit in the same repair got it right — `README.md` row 33: "It judges work products
only: a record quotes the broken path it reports, and a specification … names the files the work
is required to create, so **neither is scanned**." There "neither" ranges over record and
specification, both unscanned *by the lint*, and it is accurate.

Downstream decision that goes wrong: whoever next needs mechanical help over a specification
reads that it belongs to neither existing home and builds a third — the `E6` shape ("a fix that
requires new machinery is the signal to re-question the guarded thing"). Also `E3`'s last clause:
this is a factual assertion about the harness's own mechanism written into instruction text, and
the command that falsifies it (`grep -n form_conformance rsclib/document_harness/instruction.py`)
is not in the commit body or the journal.
Exact bytes — replace `A specification is neither:` with
`A specification is not a work product — it is the authoring gate's subject:`. A low whose record
supplies the exact bytes takes `E10`'s free channel (`R10`), instruction layer included; it does
not open a round.

**`L-2` `scanned()`'s docstring still states the two-way split this round replaced.**
Location: `ResearchSystem/tooling/hooks/candidate_path_check.py:84` —
`"""Every staged Markdown file except the record surface and vendored documentation."""`
Ground truth: `NOT_SCANNED = RECORD_SURFACE + SPECIFICATION_SURFACE + VENDORED`, three lines
above it. This is the exact sentence the FULL's `L-1` cited as the ground truth the code
violated; the module docstring, `EXECUTION.md` and `README.md` were all corrected and this one
was left, so the round re-created its own `L-2` defect class — a stated scope the code does not
match — one scope level down. Grep confirms it is the only surviving two-way description in live
code. Downstream decision: the next reader of `scanned()`, including the next reviewer looking
for the ground truth to judge the scan against, is told the scope is two-way.
Exact bytes: `"""Every staged Markdown file outside the three surfaces of `NOT_SCANNED`."""`

**`L-3` The C-quoting defect class is closed on two invocations and open on the third, where it
now produces a false *block*.**
Location: `ResearchSystem/tooling/rsclib/document_harness/paths.py:117-121`,
`TrackedPaths.from_index` — `git ls-files` without `core.quotepath=off`. Ground truth: `E7`,
test the defect class rather than the reported instance. A C-quoted index entry never registers
its real ASCII ancestor directories, so a directory whose only tracked children are non-ASCII
named resolves nowhere. Measured, in a scratch repository:

```
tracked:      ResearchSystem/notes/笔记/x.md
git ls-files                        -> "ResearchSystem/notes/\347\254\224\350\256\260/x.md"
git -c core.quotepath=off ls-files  -> ResearchSystem/notes/笔记/x.md
work product citing `ResearchSystem/notes/`   -> check() = 1   BLOCKED
    pre-commit BLOCKED: …candidate.md: `ResearchSystem/notes/`
```

The directory exists and is tracked; the guard says it exists nowhere. Worse in kind than the
finding it descends from: a silence is missed, a false block is what earns `--no-verify` — which
is this repair's own argument for the specification-surface exclusion ("a lint that blocks the
normal opening move of every run … protects nothing"). Same deadline as the FULL's `L-1`, the
first non-ASCII tracked path; `git ls-files | grep -c '^"'` → **0** today, so it is inert.
Minimum fix: `-c core.quotepath=off` on that invocation, plus a negative control staging a work
product that cites a real directory with a non-ASCII-named child.

**`L-4` One half of the `L-1` repair is inert, and no test binds it.**
Location: `paths.py:189` — `core.quotepath=off` on `staged_added_lines`'s
`git diff --cached -U0`. Measured: quoting affects only the `+++ b/"…"` header line, which the
function filters out by the `+++` guard; the `+`-prefixed lines it keeps are content and are
byte-identical with and without the flag. Mutation V4 removing it leaves 46/46 green.
It is not wrong, and it follows the FULL's stated minimum fix literally ("on both git
invocations"). But `E4` — never trust a guard you have not seen fail — is unmet for that half,
and the commit body presents both invocations as the fix. Disposition is the user's: bind it, or
drop it as machinery no decision turns on (`E6`). It banks cleanly if neither.

**`L-5` The `412 → 373` figure mixes two metrics.**
Location: `a1fad7e`'s commit body and `journal/simp-a4-2026-08-06.md:152`. Measured over the
tracked corpus with the shipped rules, all four cells from the same script:

| | scanned `.md` | UNRESOLVED, globally distinct | UNRESOLVED, (file, token) pairs | files hit |
|---|---|---|---|---|
| pre-fix | 332 | **412** | 495 | 72 |
| post-fix | 323 | 332 | **373** | 54 |

`412` is the distinct-token count — it reproduces the FULL's `O-1` exactly, 412 across 72 files,
78 of them bare single-segment directories. `373` is the file-token pair count. Like for like the
reduction is 412 → 332, or 495 → 373; the stated pair is neither, and it understates the
improvement while being internally inconsistent. `E3`: a count is emitted by the command that
produces it. No decision turns on the number, so the correction is to the record, not to a rule.

### Observations (`R5` — reported; the conclusions are the user's)

**`O-1` The specification surface is recognised by path prefix, and the prefix cuts both ways.**
The journal's §9 honesty line states the outward half — a specification written outside the run
directory is still scanned as a work product — and I confirm it at HEAD:
`assurance/shadow/round-3/dispatch-prompt-run-{a1,p3}.md` and `templates/run-v2/README.md` are
scanned, and both blocked in the historical replay. The inward half is not stated: *any* `.md`
later added anywhere under `assurance/runs/` silently stops being scanned, whatever kind of
document it is. Today that tree holds only seven `instruction.md` and two
`control/audit-rounds.md`, so the fit is exact and no candidate lives there. Whether a prefix is
the right recogniser for a document *kind* — the module's own new docstring says the scope is
"decided by what a document IS, not by a list of places", and the implementation is a list of
places — is `R5`.

**`O-2` Method dependency in the 80-commit figure.** Over the last 80 commits *including* merges
the shipped lint blocks twice; over the last 80 *non-merge* commits it blocks once. Both blocks
are the same real defect, in the candidate `3687d56` and again in the promotion merge `ad00fec`,
so the substance holds either way and the claim reproduces under the second reading. Recorded
because the figure as written does not name its window.

**`O-3` The amended instruction-layer bytes have not had their `E10` read.** `README.md`
(`2191487b` → `70bd9f0b`) and `EXECUTION.md` (`ae8e60c9` → `8094a866`) changed in this repair.
`E10` requires each amendment to pass an independent read before any round relies on it; this
VERIFY is not that read (`R3`: a read is not a round; `E10`: the read's subject is the amendment
text itself and it is never banked as a round's leg). Nothing in this range relies on the amended
text, so the obligation is forward-looking — but it is owed before P5B opens, and `L-1` lands
inside it.

## 6. Boundary and record conformance — second (`R3`)

**`E2`** — nothing in the range is frozen, verified against the enumeration rather than the
commit body. The schema pack is untouched
(`git diff --name-only 285c596..HEAD -- ResearchSystem/schema/document-assurance-v3/` → empty;
15 files at HEAD, matching the 2026-08-03 re-baseline). The four blobs at HEAD:

```
8ad404b1  .goals/plans/document-work-assurance-harness-v3.plan.md      (signed plan)
b2dbdf75  ResearchSystem/contract/Document-Work-Assurance-Contract-v3.md
68031fa2  …-supersession-1.md            e1a2f26b  …-supersession-2.md
```

all four byte-identical to the ids `E2` names, and none is in the changed path set.

**`E10`** — two members changed, `README.md` and `EXECUTION.md`, both already amended by the
candidate and amended again here. The edits are additive or in-place replacement of the named
clause, not re-typing: `EXECUTION.md` extends one half-sentence and appends one new sentence;
`README.md` replaces the tail of row 33. Both changes were named by the FULL (`L-2`, `L-4`) and
both ride the round's one approved fix. The reliance clause is discharged forward, not here —
`O-3`.

**`E8`** — two commits. Titles `V3-SIMP-A4-CANDIDATE-LINT-FIX-v1` (naming the round, `V3-<ROUND>-v1`)
and `V3-REVIEW-RECORD-SIMP-A4-CANDIDATE-LINT-285c596-v1` (`R6`'s prescribed record form). Each
body is one dense paragraph opening with its kind — "Kind: review fix", "Kind: record" — so
attribution needed no asking. Author and commit timestamps are equal and strictly increasing
(16:59:15 → 17:42:20 +1000), so nothing was amended; no merges in the range;
`git rev-list --count origin/main..HEAD` → 497, unpushed, consistent with the standing user gate.

**`E9`** — accounted in §1. After this VERIFY the round's budget is fully spent: FULL `239f56a`,
fix `a1fad7e`, VERIFY this record.

**`E12`** — the handoff is a range and the marker holds it in resolved form, which `E12`
classifies as display rather than a recorded range; `.harness/` is gitignored, so nothing was
recorded into a tracked file. The journal header still records the round's range as
`a27022f..HEAD` — base written, tip unwritten, the required form.

**`E6`** — the repair adds no new machinery. `SPECIFICATION_SURFACE` and `VENDORED` are splits of
an existing tuple, `_is_citation_shaped` is an extraction of an existing predicate, and the two
git invocations gained a flag. The one thing that arguably fails the "what decision changes if it
is absent" test is the inert half of the quotepath change — `L-4`.

**`E1`** — this session held one role for its whole life; it authored no candidate file, and this
record is its only write.

## 7. Coverage disclosure (`R4`)

**Read in full:** `CONSTRUCTION-CHECKLIST.md` (standing instruction, both sides, arrived at via
the superseded review contract's stub); `REVIEW.md`; the complete diff of all eight changed
paths; `paths.py` and `candidate_path_check.py` at HEAD in full; `layer_path_check.py` in full;
`v3-review-full-285c596.md`; `HARNESS-LEDGER.md`; both commit bodies; the amended `EXECUTION.md`
section with its surrounding argument; the `CandidateScanScope` and `NonAsciiFilenames` test
classes.

**Re-derived by command:** the six-freeze replay against an independently reconstructed staged
state, both module versions, with the old/new contrast; the four candidate promotions, both
versions; the 80-commit sweep, both versions and both merge policies; the whole-corpus
UNRESOLVED measurement across four rule/scope combinations; the per-file scan scope of the
`assurance/` tree; the nine-member dual-coverage probe; the C-quoting behaviour of three git
invocations in scratch repositories; every battery figure; the ledger line count; the four `E2`
blobs and the nine `E10` member blobs at both ends of the range; commit timestamps, merge count
and push debt.

**Mutation:** ten runs, sources restored under sha256 and re-verified, suite green before and
after, worktree clean afterwards. One survivor, reported.

**Sampled, not re-verified:** the FULL's own §2–§4 re-derivations (the 47-token four-candidate
decomposition, the `v3-review-full-fef3a2e.md` zero-mention check) — I re-ran the *outcome* of
that measurement through the promotions rather than the token-level table; and the eleven riders
the journal lists as untriggered, whose conditions I did not each re-test. `HARNESS-RIDERS.md` I
read only for its line count and untouched status.

**Marked, not verified:** that this session is a fresh context. I can attest only that my subject
arrived as a range and nothing else, and that everything above came from the repository — `R4`
says a process claim is marked, never verified.

**Ceiling (`R7`):** the `E11` preview card for this repair is not in the repository, and the
2026-08-06 option-A ruling is chat-origin with its in-repo record in journal §9 and the ledger
pointer. Stated, not treated as a block.
