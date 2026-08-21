# VERIFY — round `TEMPLATE-LIB-ROOT`, repair at `627df95`

**Verdict: `REVIEWED_NO_BLOCKER`.** 1 low, 3 observations.

**The repair answers all three accepted findings and I could falsify none of it.** The
carrier `L-1` said was missing now exists, and I rebuilt its evidence from scratch rather
than reading it: both RED diagnostics reproduce byte-for-byte — including the `ImportError`
variant, which I obtained from the mechanism the journal names rather than from the caller
repository I cannot reach — both GREEN runs reproduce, two of the three pasted mutations
reproduce with their exact red tests, the three sha256 and blob restore checks are correct
at this tree, and the battery returns the pasted figure. `L-2`'s replacement reason is true
on a hand count of all seven invocations and on the argparse ordering in all six scripts.
`B-1`'s errata is in both carriers `E1` names, matches the disposition `HD-46` records, and
its one claim I could test independently — what the reviewers were prompted with — checks
out against the generator's own template. No source file changed, `O-1` is untouched as the
boundary required, and every permanent boundary holds.

The low is that `HD-41` ④'s class-scan grep is not pasted anywhere in the repair. I ran both
scans myself and the classes are closed, so nothing acts wrongly — but that is the part that
was supposed to be visible without a reviewer re-running it.

---

## 1. Subject, round, budget and window — re-derived, nothing taken from the dispatch

The dispatch handed one range and nothing else. Everything below is from the repository.

**Subject.** `83e3191697ace9cf65cc8625b1ef4ea69fdc6a99..627df958d8ebff8604d4a95ffa4ee9f8912fdd86`,
two commits. `627df95` is `HEAD`. The worktree was clean at open, after every mutation
restore, and at close (`git status --porcelain` → empty each time).

| commit | title | kind (named in its own body) |
|---|---|---|
| `08665d3` | `V3-REVIEW-RECORD-TEMPLATE-LIB-ROOT-83e3191-v1` | record |
| `627df95` | `V3-TEMPLATE-LIB-ROOT-FIX-v1` | review fix |

**Round.** `TEMPLATE-LIB-ROOT`, from the commit titles and from the journal this repair
creates. The round's four commits are `3067efc` (read record) → `83e3191` (candidate) →
`08665d3` (FULL record) → `627df95` (fix), a linear chain with no amend:

```
$ git log --format='%h %ci %p' -4
627df95 2026-08-21 22:58:54 +1000 08665d3
08665d3 2026-08-21 22:00:46 +1000 83e3191
83e3191 2026-08-21 21:37:13 +1000 3067efc
3067efc 2026-08-21 21:28:15 +1000 39e395e
```

**Budget (`E9`).** `E9`'s test is *has a valid independent FULL already occurred?* Yes —
`v3-review-full-83e3191.md` landed at `08665d3`, and a dispatched review has occurred when
its record's commit lands. So `627df95` is the round's **one user-approved fix**, and this
dispatch is the **targeted VERIFY** it obliges. One FULL, one fix, one VERIFY: the cap is
met exactly, and no commit in the round is a second fix under a different name.

**Window (`E9`).** `.harness/review-pending.json` records the subject as exactly this range,
dispatched `2026-08-21T12:59:06+00:00`; `627df95` was committed `22:58:54 +1000` = `12:58:54Z`,
twelve seconds earlier. No commit has landed since. `.harness/` is ignored
(`git check-ignore -v` → `.gitignore:18:.harness/`), so the marker is not itself a commit.
The window is intact. The same holds for the FULL: dispatched `11:37:23Z` per that record,
its record landed at `08665d3`, and nothing else landed in between.

**Not pushed (`E8`).** `git status -sb` → `## main...origin/main [ahead 4]` — the round's four
commits, unpushed.

**Authorization (`R7`).** The fix boundary — "the blocker plus both lows, `O-1` excluded" —
is a chat-side user ruling, recorded in the journal by the work side but not independently
visible to me. I state the ceiling and move on: **I cannot see the boundary ruling or the
preview card in the repository**, and I have treated that as a hint, not a block. What I
*can* check is whether the repair stayed inside the boundary it declares, and it did (§3.4).

## 2. Changed paths, classified by hand

```
$ git diff --stat 83e3191..627df95
 document-harness/journal/template-lib-root-2026-08-21.md   | 202 +++++++++++
 migration/document-work-assurance-v3/v3-review-full-83e3191.md | 385 +++++++++++++
 tooling/tests/document_harness_review/test_run_v2_template_library_path.py | 16 +-
 3 files changed, 598 insertions(+), 5 deletions(-)
```

| path | class | which commit |
|---|---|---|
| `migration/document-work-assurance-v3/v3-review-full-83e3191.md` | review record (`R6` channel) | `08665d3`, the record commit |
| `document-harness/journal/template-lib-root-2026-08-21.md` | round journal — carrier for `B-1` and `L-1` | `627df95`, the fix |
| `tooling/tests/document_harness_review/test_run_v2_template_library_path.py` | guard docstring — `L-2` and the `L-1` citation | `627df95`, the fix |

**No source file changed.** Both repaired scripts are byte-identical to the candidate:

```
check_template_instance.py  worktree=692773ff5519  HEAD=692773ff5519
make_paragraph_map.py       worktree=27bb7e0149e5  HEAD=27bb7e0149e5
run_repair.py               worktree=c72edabe4c10  HEAD=c72edabe4c10
```

That is the right shape for this repair: `B-1` was a boundary finding, not a code one, and
`L-1`/`L-2` were a missing carrier and a false sentence about code that was already correct.

## 3. The accepted findings, each re-executed rather than accepted

### 3.1 `B-1` — the errata

`E1` requires the round to state which of `R1`'s four holdings the executor held, in the
commit body or the round journal, and **not** to call the result structurally independent.
The repair puts the statement in **both** carriers: the `E1` section of
`document-harness/journal/template-lib-root-2026-08-21.md:38-60`, and the fix commit body.
It withdraws the candidate's conclusion explicitly, names all four holdings with what each
one consisted of, states in bold that the round does not call its reviews structurally
independent, and withdraws the pre-declaration about the FULL by name — which was the part
`R2` exists to refuse.

Against `HD-46`'s recorded tiebreak (`HARNESS-DECISIONS.md:196`, `§implemented`), read in
full: *全占＝失格 · 一项不占＝结构性独立 · 中间态＝独立但该轮在记录里写明 executor 占了哪几项，
且不得自称结构性独立*, followed by the sentence that this middle-state disposition
*直接作用于今天的实际形态——一个 session 同时持 orchestrator 与 executor 两个角色*. The
one-session form is the middle state by that ruling's own words, and the errata's disposition
is the one it prescribes. It is also verbatim in shape with `15a53fe`, the precedent the FULL
named as the minimum fix.

**The one claim in it I could test independently, I tested.** The errata says the session
handed each reviewer *"the CLI's derived text plus two operational sentences of its own — the
repository root, and the instruction to write without committing"*. `CONSTRUCTION_PROMPT`
(`tooling/rsclib/document_harness/dispatch.py:552`) is:

```
You are the independent bounded reviewer for Document Work Assurance Harness v3.

Your standing instructions are `{charter}`;
read it, and the counterpart it names, before anything else. It governs this round.
This prompt does not — it exists only to hand you the subject.

**Subject: `{base}..{tip}`**

Everything else you derive from the repository: which round this is and what budget
it carries, what was authorized and by whom, what the work was obliged to do, and how
to report. All of it is committed; none of it is restated here, because a fact you
were handed is a fact you did not check.
```

My own dispatch is that text verbatim, plus exactly two appended sentences: the repository
root, and *"Write your record into the worktree; do not commit it — the orchestrator commits
it."* The claim is true of this dispatch, which is the one I can see; that it was equally
true of the FULL's is `UNVERIFIABLE` and recorded as such below.

### 3.2 `L-1` — the carrier, and whether what it carries is real

The citation now resolves: `test_run_v2_template_library_path.py:26` names
`document-harness/journal/template-lib-root-2026-08-21.md`, and that file exists at `HEAD`.
The question a VERIFY has to ask is not whether a file appeared but whether the evidence in
it is genuine, so I rebuilt every item of it at this tree.

**RED, both diagnostics.** I recovered the pre-fix bytes with `git show 39e395e:` into a
scratch directory and built a disposable caller-shaped repository (a temp git repo, the
instruction pinned at a real commit, the run directory at
`ResearchSystem/assurance/runs/run-red`), never touching the caller repository or this
worktree:

```
=== RED: pre-fix make_paragraph_map.py against caller-shaped fixture ===
    from rsclib.document_harness import load_json  # noqa: E402
ModuleNotFoundError: No module named 'rsclib'
exit=1

=== RED: pre-fix check_template_instance.py against caller-shaped fixture ===
    from rsclib.document_harness import load_json, validate  # noqa: E402
ModuleNotFoundError: No module named 'rsclib'
exit=1
```

The second diagnostic the journal pastes was taken against the caller's own run directory,
which I cannot reach. So I tested the **mechanism it names** instead — *"the caller still has
one whose `document_harness` package was removed by the split, leaving a namespace package
with no `load_json`"* — by giving a third fixture a bare `ResearchSystem/tooling/rsclib/
document_harness/` directory and nothing in it:

```
=== fixture: rsclib/document_harness/ exists as bare dir (namespace pkg, no load_json) ===
  ResearchSystem/tooling/rsclib/document_harness
=== RED variant: pre-fix check_template_instance.py against split-shaped caller ===
    from rsclib.document_harness import load_json, validate  # noqa: E402
ImportError: cannot import name 'load_json' from 'rsclib.document_harness' (unknown location)
exit=1
```

Byte-identical to the journal's line, from the stated cause. That also makes the docstring's
new sentence — the two diagnostics *"differ only in whether the tree being reached into still
holds an `rsclib` package at all"* — a verified claim rather than an asserted one: the
fixture with no `rsclib` gives `ModuleNotFoundError`, the one with a namespace `rsclib` gives
`ImportError`, and nothing else differs between them.

**GREEN, same invocations at this tree.**

```
=== GREEN: fixed make_paragraph_map.py, same invocation ===
instruction read from: pinned revision
wrote 3 paragraph(s) to ...\run-red\control\paragraph-map.json
exit=0

=== GREEN: check_template_instance.py on a fresh fixture (no map) ===
instruction read from: pinned revision
TEMPLATE-PREAMBLE-UNMAPPED: the instruction's preamble carries content but no instruction unit anchors into it; ...
TEMPLATE-PARAGRAPH-MAP-MISSING: control/paragraph-map.json does not exist; ...
authoring gate: 2 issue(s)
exit=1
```

Both match the journal, including `authoring gate: 2 issue(s)`. (Run sequentially against one
fixture the gate returns 7 issues instead, because the map now exists and is unclassified —
the journal's two blocks were taken against separate fixtures, which is also what the test
file's `setUp` does. Not a discrepancy; recorded so the next reader who runs them in one
directory is not surprised.)

**Mutation, two of the three, with checked restores.** Scratchpad copies taken before any
mutation, restored from those copies, never `git checkout --`:

| # | mutation | result | red test |
|---|---|---|---|
| 1 | `run_repair.py` `RS_ROOT = HERE.parents[2]` → `parents[1]` | `1 failed, 3 passed in 1.67s` | `…::SelfLocatingScriptsStayThatWay::test_each_prints_its_usage_after_importing_the_library` |
| 2 | `make_paragraph_map.py` → pre-fix bytes (`git show 39e395e:`) | `1 failed, 3 passed in 1.88s` | `…::RepairedScriptsFindTheLibraryFromTheirOwnTree::test_make_paragraph_map_writes_the_skeleton` |

Both are the journal's pasted results exactly, red test included. I ran mutation 1 in
particular because it is the one that binds the four `--help` pins that `L-2`'s sentence is
about. Restores checked twice over, matching the journal's own figures:

```
c02c542753f1a36a02e979e7af03ffd29c874fd963fad1b89549c4fe3d91bd5d *run_repair.py
b68516af76b2bc0b7cd2ebf7e3a206468dc872b21b99b8f0c36370ca2c8f7097 *make_paragraph_map.py
run_repair.py         worktree=c72edabe4c10bca50dd789d129ce35bc17fc8bb3  HEAD=c72edabe4c10bca50dd789d129ce35bc17fc8bb3
make_paragraph_map.py worktree=27bb7e0149e524d187187aea7d0279a1945ee793  HEAD=27bb7e0149e524d187187aea7d0279a1945ee793
```

Per `R4` this proves the tests still bind after the repair; it is not a re-certification of
the candidate, which the FULL already mutation-tested four ways.

**The battery**, re-run by me at `HEAD` immediately before this claim:

```
$ python -m pytest -q
774 passed in 131.13s (0:02:11)
```

The journal's figure (774) is the figure I measured; its 124.69s is that session's clock and
mine is mine. The journal's `770 at the round's base` follows transitively — both scoped runs
above report 4 tests in the new file.

### 3.3 `L-2` — the replacement reason, hand-counted

Counted by reading the file, not by trusting the sentence. Seven subprocess invocations:

| where | how many | root? |
|---|---|---|
| `SelfLocatingScriptsStayThatWay:115` — `run_template(name, "--help")` over `SELF_LOCATING` (4 names) | 4 | none passed |
| `:135` `make_paragraph_map.py` and `:147` `check_template_instance.py`, each `str(self.repo.root)` | 2 | passed explicitly |
| `TheProbeCanFail:169` — `run_script(probe)` | 1 | standalone file, no arguments |

2 + 4 + 1 = 7, which is the file's total. The new sentence is therefore true where the old
one was false of five.

The reason it gives is also true, and I checked the half a reader would have to take on
trust. In all four `SELF_LOCATING` scripts `parse_args` precedes root resolution by three
lines, so `--help` raises `SystemExit` inside argparse and `parents[3]` is never evaluated:

```
run_evidence_v2.py:118 args = parser.parse_args(argv)   :121 REPO = ... else run_dir.parents[3]
run_bind_v2.py    :167 args = parser.parse_args(argv)   :170 REPO = ... else run_dir.parents[3]
run_repair.py     : 60 args = parser.parse_args(argv)   : 63 REPO = ... else run_dir.parents[3]
run_retire.py     : 95 args = parser.parse_args(argv)   : 98 REPO = ... else run_dir.parents[3]
```

The two repaired scripts take no argparse at all — `repo_root = pathlib.Path(argv[2]) if
len(argv) > 2 else run_dir.parents[3]` (`check_template_instance.py:195`,
`make_paragraph_map.py:37`) — so "pass one explicitly" means the positional the two tests
pass, which they do. The conclusion the sentence supports, that nothing below reaches the
`parents[3]` default, is unchanged and correct, and the sentence no longer supports it with a
falsehood.

The journal's neighbouring figure is right too: `parents[3]` sites in the six templates = 6,
`cwd()` defaults in `cli.py` = 6 (lines 43, 80, 147, 329, 414, 462) — **12 across 7 files**,
as the in-round ruling records.

### 3.4 The boundary the repair declared, and whether it stayed inside it

Declared: the blocker plus both lows; `O-1` excluded. Checked against the tree rather than
the claim — `O-1`'s site is untouched:

```
$ sed -n '152p' tooling/tests/document_harness_review/test_run_v2_template_library_path.py
        self.assertTrue(any("TEMPLATE-PARAGRAPH-MAP-MISSING" in line for line in lines),
```

Still the substring assertion the FULL declined to propose. Three paths changed, all three
accounted for by an accepted finding or by the `R6` record channel; nothing rode along. `E9`'s
"exceeding an approved fix boundary requires saying so" is not engaged, because the boundary
was not exceeded.

`O-3` and the cold read's `L-1` are carried to closeout rather than answered here, which is
where this harness writes rider rows — both preceding closeouts (`39e395e`, `e351a3b`) touch
`HARNESS-RIDERS.md`, and neither fix commit does. So the absence of a rider row today is the
practice, not a gap.

## 4. The permanent boundaries

**Frozen bytes (`E2`).** `git diff --name-only 83e3191..627df95 -- contract/ schema/` returns
**0 paths**. At `HEAD` the three frozen blobs still hash to their named ids —
`b2dbdf752d8c155e…` (contract), `68031fa2ca31272e…` (supersession-1), `e1a2f26b1d8d323d…`
(supersession-2) — and `schema/document-assurance-v3/` holds **15** files, the 2026-08-03
re-baselined count. Nothing frozen was written, so no ruling was owed and none of `HD-20`'s
banking rule is engaged.

**Instruction layer (`E10`).** No member changed. I checked all ten by blob rather than by
diff, and against the blob ids the opening cold read recorded at `39e395e`
(`v3-cold-read-39e395e.md:65-74`) — every one is identical:

```
cacd99d49d80ce4bf33e94b733a07f1dd6b247e8  document-harness/CONSTRUCTION-CHECKLIST.md
7591c5332d170a286a15ef6a699f69cc80def755  document-harness/README.md
27f4fc82a556f26804ee5236204f746bd99da5bd  document-harness/EXECUTION.md
35fe0abcd7123f4a37a88ef4de605b3aad3cfe75  document-harness/REVIEW.md
80f42658a2961eeb10a168bd7bd729121c6c05ae  document-harness/ORCHESTRATION.md
6d5714923870b4e13e8928221a80df68e563a5ed  …/v3-harness-operating-contract.md
29bdc9fbde6e8db38d601dd2340d4b46a24a296f  …/v3-harness-review-contract.md
68031fa2ca31272e31da0d42a9a02189d28fcc21  …-supersession-1.md
e1a2f26b1d8d323d11e900f8137dea222b6571c1  …-supersession-2.md
09aa869962f592c2f86c9379be0ef3eb7d2232ff  schema/…/paragraph-map.schema.json
```

That verifies the journal's closing claim — *"Layer debt this round leaves: None"* — on both
of its legs: no member changed, and the cold read's record does state the blob id of each
member, which is the precondition `E10` sets for citing it instead of re-reading. `layer_path_check`
is not engaged, no member having added a line. The `HARNESS-DECISIONS.md` `§live` read owed at
the round's opening I performed myself (lines 1-135, `HD-44` / `HD-41` / `HD-36` / `HD-35` /
`HD-34` / `HD-23` / `HD-9`), plus `HD-46` in full from `§implemented`.

**Git form (`E8`).** Both commits name their kind in the first words ("Kind: record.",
"Kind: review fix, carrying the B-1 errata."), each is one dense paragraph with no trailers,
each stages explicit paths, the chain is linear with no amend, and nothing is pushed. Titles
follow the round's established `V3-<ROUND>[-FIX]-v1` and `V3-REVIEW-RECORD-<ROUND>-<sha>-v1`
forms.

**Range recording (`E12`).** The one range the journal writes is `39e395e..HEAD`
(`:53`) — base written, tip `HEAD`, exactly as the rule requires; the chain elsewhere is
individual commit ids, not a range.

**Record channel (`R6`).** `v3-review-full-83e3191.md` under
`migration/document-work-assurance-v3/`, committed by the work side under
`V3-REVIEW-RECORD-TEMPLATE-LIB-ROOT-83e3191-v1`. Correct path, correct name, correct title.

## 5. Findings

### `V-1` (low) — `HD-41` ④'s class-scan grep is pasted nowhere in the repair

`HD-41` is `live` and `standing`, and the user re-affirmed it on 2026-08-17 as pure
discipline with no machine behind it. Its fourth clause obliges a fix to grep the assertion's
keyword strings across the round's work files **before** writing, and to paste that grep
output into the commit body — *扫类是动作不是自觉，贴证据是为了「跑没跑」可被评审员当场看见*.
Neither `627df95`'s body nor the journal contains any grep output (`grep -c "grep "` → 0 on
both). `L-2` is explicitly identified in both as "the `HD-41` part two shape", so the ruling
was in view.

I ran both scans myself over the round's four work files (the two scripts, the test file, the
journal). The absolute-quantifier class: every surviving instance is either scoped in
adjacent text (`test_…:21` "All six are exercised" against six members I counted) or true as
written; I could falsify none. The dangling-citation class that `L-1` belongs to: the only
non-resolving tokens are deliberate placeholders and run-relative paths
(`<repo-root>/ResearchSystem/tooling`, `repo_root/ResearchSystem/tooling`, `run_*.py`,
`control/paragraph-map.json`), none of them a pointer to a permanent artifact that does not
exist. **So the classes are closed and nothing acts wrongly today.**

**Downstream decision that goes wrong if unfixed.** The paste is what lets the next reader
distinguish "the class was swept" from "the reported instance was patched" — the `E7`
question. Absent it, that reader either re-runs the scans, as I did, or takes the sweep on
trust; `HD-41`'s own recorded history is that the second happens. Precedent within this
harness is already split: `84dea06` (`INIT-SURFACE` fix) pastes one, `15a53fe`
(`PREVIEW-RENDER` fix) does not, and now `627df95` does not — three fix legs, one paste. That
drift is the thing worth naming, not this round alone.

Not inflated to a blocker: a VERIFY has no such verdict, and on the merits the outcome is
unchanged because I verified the sweep's conclusion by hand.

### `V-2` (observation) — the pasted evidence placeholders its command lines

`E3` says to paste tool output and never describe it from memory. The journal's RED and GREEN
blocks paste the diagnostics, the verdict lines and the exit codes, but the command lines
themselves carry placeholders (`<run-dir>`, `<repo-root>`, `<pre-fix check_template_instance.py>`,
`<caller run-dir>`) and several output lines are elided with `...`. That is a large
improvement on the candidate, which described the runs and pasted nothing — the finding is
answered — but it is a partial paste: a later reader cannot copy a line and re-run it.

It held up under test, which is why this is an observation and not a low: I rebuilt all three
fixtures from the surrounding prose alone and got byte-identical diagnostics on every one. So
the carrier does its job. Recorded because the reason it worked is that the prose around the
placeholders was unusually precise, which is a property of this journal rather than of the
form.

### `V-3` (observation, `R5`) — the errata records "all four" without naming which branch of `E1` the round lands in

The errata states that all four of `R1`'s holdings sat with the single work-side session, and
declines structural independence. Both halves are what `E1`'s middle-state clause and `HD-46`
prescribe, and it is verbatim in shape with the precedent the FULL named, so this is not a
defect in the fix — the fix did what it was told to do.

What I record is the shape underneath it. `E1`'s three dispositions key on a count: *"All four
in the executor's hands is a self-check whatever it is called"* / *"none of them there is
independence that holds structurally"* / *"Between those"*, state the holdings. A round that
discloses all four and then claims the middle-state disposition is legible only if the reader
also has `HD-46`'s rationale, which is where the reconciliation actually lives — the
one-session form *is* the middle state because there is no separate orchestrator for either
extreme to describe. `E1`'s own text does not carry that, and neither does the errata. A
reader with the checklist and not the decision register reads "all four held" straight into
the disqualifying branch.

Whether `E1` should carry the reconciliation is design and the user's under `R5`, not mine.
It sits next to the question the round already carried to closeout (the FULL's `O-3`: that
`ORCHESTRATION.md` routes a boundary excess through an orchestrator that, in a one-session
round, is the same session). Both are the same underlying question — what form the harness's
role separation takes when one session holds both work-side roles — and they would be
answered together or not at all.

### `V-4` (observation, `R4`) — what this VERIFY could not verify

- **The fix-boundary ruling and `E11`'s preview card**: chat-side. The journal records them
  as in-session user rulings, but that record is the work side's own attestation, not
  independent evidence. `UNVERIFIABLE`; ceiling stated per `R7`. What I could check — that
  the repair stayed inside the boundary it declares — I checked (§3.4).
- **The `ImportError` RED against the caller's real `p5b-claims` run directory**: the caller
  repository is not reachable from here. `UNVERIFIABLE` as an observation of that tree. I
  reproduced the diagnostic exactly from the mechanism the journal names, which supports the
  claim's substance without confirming the run happened.
- **That the FULL's dispatch was the CLI text plus those two sentences**: I verified the
  generator's template and my own dispatch, not the FULL's. `UNVERIFIABLE` for that review;
  the errata's claim is consistent with everything I can see.
- **That `08665d3` landed the FULL record unchanged**: I have no copy of what the reviewer
  returned. `UNVERIFIABLE`; the record is well-formed for its channel.
- **That this review ran in fresh context**: a process claim I assert and cannot prove
  (`R4`), marked rather than verified.

## 6. Coverage disclosure (`R4`)

**Read in full**: `document-harness/CONSTRUCTION-CHECKLIST.md`;
`migration/document-work-assurance-v3/v3-harness-review-contract.md`;
`migration/document-work-assurance-v3/v3-review-full-83e3191.md`;
`document-harness/journal/template-lib-root-2026-08-21.md`;
`tooling/tests/document_harness_review/test_run_v2_template_library_path.py` (all 177 lines);
`HARNESS-DECISIONS.md` lines 1-135 (`§live`) plus `HD-46` in full; both commit bodies in the
range; the complete diff of the range.

**Sampled**: the six run-v2 template scripts (path blocks, argparse blocks and
root-resolution lines, not their whole bodies); `tooling/rsclib/document_harness/dispatch.py`
(the construction dispatch section, `CONSTRUCTION_PROMPT` in full);
`tooling/rsclib/document_harness/cli.py` (the six `cwd()` lines only);
`migration/document-work-assurance-v3/v3-cold-read-39e395e.md` (the member-blob table, the
freeze section, the findings tally); `HARNESS-RIDERS.md` (a targeted search plus the last 25
rows); the bodies of `15a53fe`, `84dea06`, `39e395e`, `e351a3b`.

**Only probed**: `document-harness/EXECUTION.md`, `document-harness/REVIEW.md`,
`document-harness/ORCHESTRATION.md` — not read this round; their blobs are unchanged since
the recorded end-to-end read at `39e395e`, which is the citation `E10` permits.
`HARNESS-DECISIONS.md` `§implemented` beyond `HD-46` — not read.

**Executed by me**: `python -m pytest -q` in full once (774 passed) plus twice scoped to the
new file under mutation; two mutations with sha256- and blob-verified restores; three
disposable caller-shaped fixtures built from scratch, carrying two RED reproductions of the
pre-fix bytes, one RED reproduction of the namespace-package variant, and two GREEN runs at
this tree; two class-scan greps over the round's four work files; blob and sha256 checks on
the three scripts, the three frozen contract blobs and all ten instruction-layer members;
`git status --porcelain` at open, after each restore and at close — empty every time. No
write touched this worktree or any caller repository; every fixture lived in a scratch
directory and was disposed of.
