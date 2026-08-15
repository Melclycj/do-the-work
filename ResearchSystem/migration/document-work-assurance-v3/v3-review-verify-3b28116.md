# Targeted VERIFY — `ca61820..3b28116` (HI-REDEEM-5, the round's one approved fix)

| | |
|---|---|
| round | VERIFY, construction-side (`CONSTRUCTION-CHECKLIST.md` R1–R10) |
| subject | `ca61820720bbf1351db92b19c23ac9920a4099aa..3b28116f5c932e8362fb7519a54fb92db6da19ec` |
| range content | one commit: `3b28116` (`V3-HI-REDEEM-5-FIX-v1`, kind: review fix) |
| answers | FULL `v3-review-full-f4e1be1.md` — accepted items **L-1**, **O-2**, and the executor-side *correction E* |
| **verdict** | **`REVIEWED_NO_BLOCKER`** |
| findings | 3 low, 4 observations |
| record | this file; the execution side commits it (`R6`) |

**`REVIEWED_NO_BLOCKER` here does not mean all three accepted items are closed.** Two are:
L-1 is closed and over-delivered, and correction E is closed and independently
re-measured. **O-2 is closed on the persisted channel and still open on the printed one** —
a round-0 `SPEC_GAP` is still told, on stdout, that it "owes a repair decision" (V-1,
measured by driving the shipped template, not read). It is a low rather than a blocker
because the FULL itself classified O-2 as an observation and "a recorded sentence, not a
flow defect", the durable channel a cold resume reads is now correct, and nothing strands.
`VERIFY`'s verdict vocabulary has no value meaning *the repair is incomplete* (`R3`:
`REVIEWED_NO_BLOCKER | SPEC_GAP`), and this is not a specification failure — so the verdict
is the clean one and this paragraph, not the verdict, carries the qualification (O-4v).

The repair diff is entirely attributable: three files, one per accepted item, nothing else.
Every figure the fix commit states about itself and about the battery reproduces here,
including the two the FULL had found short in the previous commit — the `E3` lesson is
applied, not merely acknowledged. The permanent boundaries hold: no frozen byte (`E2`), no
instruction-layer member (`E10`), no amend, no trailer, no path outside the declared
boundary.

## 1. Subject, re-derived (`R2`)

One range was handed to me and nothing else. Round, budget, authorization, obligations and
every figure below are re-derived from the repository; no number from the dispatch prompt,
the plan, the ledger or any commit body is accepted as reported.

```
$ git rev-parse HEAD                       -> 3b28116f5c932e8362fb7519a54fb92db6da19ec
$ git rev-parse --abbrev-ref HEAD          -> document-work-assurance-v3
$ git status --porcelain                   -> (empty)
$ git rev-list --count ca61820..3b28116    -> 1
$ git rev-list --count 3b28116..HEAD       -> 0
$ git merge-base --is-ancestor ca61820 3b28116 -> yes
$ git rev-parse 3b28116^                   -> ca61820720bbf1351db92b19c23ac9920a4099aa
$ cat .harness/review-pending.json
  {"subject": "ca61820720bbf1351db92b19c23ac9920a4099aa..3b28116f5c932e8362fb7519a54fb92db6da19ec",
   "dispatched_at": "2026-08-07T08:15:54+00:00"}
```

HEAD equals the range tip and the tree is clean, so worktree reads are reads of the subject
bytes. Dispatch (08:15:54Z = 18:15:54+10:00) post-dates the tip commit (18:15:46+10:00) by
8 seconds and the branch has taken no commit since — this record is the first it admits
(`E9`'s window). The base is its own parent, so this is a new commit on top of the FULL's
record, never a rewrite of it.

**Which leg this is, derived rather than assumed (`E9`).** The test is *has a valid
independent FULL already occurred?* — `v3-review-full-f4e1be1.md` exists and was landed by
`ca61820`, this range's base, so `3b28116` is not a pre-submission correction: it is the
round's one user-approved fix, and it obliges exactly this VERIFY. `ls` over
`migration/document-work-assurance-v3/` matches nothing on `3b28116` or `redeem`, so no
review record for this leg exists yet and this is the first. The round's budget — one FULL,
one fix, one VERIFY — is spent with this record.

**Change set, classified by hand.** `git diff --numstat ca61820 3b28116`: **3 files, 112
insertions, 3 deletions**. The commit body states the same three numbers, and they were
measured from the staged index rather than an unstaged tree — which is the FULL's L-2
lesson applied at its first opportunity.

| path | class | serves | frozen (`E2`)? | instruction layer (`E10`)? |
|---|---|---|---|---|
| `ResearchSystem/assurance/templates/run-v2/run_bind_v2.py` (+16 −2) | template code | O-2 | no | no |
| `ResearchSystem/tooling/tests/document_harness_review/test_run_v2_template_bind.py` (+89 −0) | test | L-1 | no | no |
| `Thesis/Work/Tooling/repo-audit.py` (+7 −1) | verifier script | correction E | no | no |

Each accepted item maps to exactly one file and each file to exactly one item; no fourth
path appears. The test file's **zero deletions** matter on their own — nothing existing was
weakened to make room.

**Tier.** `ResearchSystem/tooling/**`, `assurance/templates/**` and
`Thesis/Work/Tooling/repo-audit.py` are tooling, so under the run-v2 README's
*Regression-battery tiering* this is **tooling-touching, not doc-only**, and the full
battery is owed. The commit classifies it the same way and ran it.

**Authorization (`R7`).** The fix boundary — L-1, O-2, correction E — is stated as
user-approved in the commit body and is visible to me nowhere else; likewise the L-4 ruling
that `E8`'s "one dense paragraph" buys density and no trailers rather than one literal
block. Both are prose I cannot cross-check. I state the ceiling and move on: the diff does
not exceed the boundary it declares, whoever set it.

## 2. The three accepted items against their sources (`R3` — implementation first)

### L-1 — closed, and past the minimum the FULL asked for

The FULL's minimum fix was one test driving the emit path and asserting the saved `status`
is `REVIEWED`. `TheBlockedRoundLandsOnReviewed` does that and four things more: it pins
`repair_round` still 0, the **whole** `next_action` line, the **absence** of an
`assurance_candidate_ref`, and carries a negative control showing a clean round 0 leaves the
seeded state at `EVIDENCED`. The seeded state is hand-written JSON, not built by the module
under test (`E5`), and every expectation is a hand-written literal asserted with
`assertEqual` over the whole string, never a substring (`E5`; V6 below proves the whole-line
form binds).

The fixture reaches real machinery rather than a stub: `assurance_state.save` calls
`check_state(state).require()`, so the saved document is schema-validated on the way to disk,
and `pointer_for("review_ref", …)` is a `DIGEST_PROTECTED_FIELDS` member that computes a
real bytes digest over a file that must exist. The test would fail if either refused.

The counterfactual the commit claims is the one I most wanted to check, and it holds:

```
mutation "REVIEWED" -> "AWAITING_FINAL", against the PRE-FIX test file (git show ca61820:…)
  -> 19 passed, 0 failed          the defect was completely unguarded before this commit
mutation "REVIEWED" -> "AWAITING_FINAL", against the SHIPPED test file
  -> 2 failed, 20 passed          AssertionError: 'AWAITING_FINAL' != 'REVIEWED'
```

The failure is a **value** mismatch, not an error — the C0 F2 / `R8` property the file's
docstring claims for itself.

### O-2 — closed on the persisted channel, open on the printed one

Both load-bearing claims of the fix are true, and I re-derived each from the code rather
than accepting the reviewer's or the executor's reading:

- `EXECUTION.md:74-77` says a `SPEC_GAP` "is not patched inside the candidate… a new
  WorkSpec revision and a new user START decision are required (V3-D7)". The new
  `SPEC_GAP` sentence is faithful to it.
- `REVIEWED` is right for both verdicts: `flow.py:191` reads
  `elif next_status != "STOPPED_REPLAN" and next_status not in _SUCCESSORS[current]:`, so
  `STOPPED_REPLAN` is exempted from the successor check and is reachable from every
  non-terminal status; `_SUCCESSORS` gives `EVIDENCED -> ("REVIEWED",)`. Neither verdict
  strands.

What the fix did **not** reach is the print two lines below the new conditional. Driving the
shipped template directly, at round 0, in both modes:

```
verdict=SPEC_GAP  --emit=False
  STDOUT| verdict : SPEC_GAP — no AssuranceCandidate is bound at round 0;
                    the run advances to REVIEWED and owes a repair decision
  STATE | next_action = <none>                       (nothing is written without --emit)

verdict=SPEC_GAP  --emit=True
  STDOUT| verdict : SPEC_GAP — … the run advances to REVIEWED and owes a repair decision
  STATE | next_action = 'user decision on the SPEC_GAP: the specification is what failed,
                         so a new WorkSpec revision and a new START decision are owed,
                         not a bounded repair'
```

The persisted sentence is now right and the printed one is still the CHANGES_REQUIRED
sentence — the exact wording O-2 named. Finding V-1.

### Correction E — closed, and the measurable property independently reproduced

`repo-audit.py`'s `EXCLUDE` gains `.pytest_cache`. Its acceptance is a measurable property,
so I measured it in four tree states rather than reading the argument:

```
0 cache dirs present                          -> scope: 472
after the full battery (1 cache dir created)  -> scope: 472
2 cache dirs present                          -> scope: 472
2 cache dirs present, EXCLUDE reverted (V7)   -> scope: 474
```

The audit's output is now invariant across the battery, which is the whole claim; before the
fix it was not. `RESULT: clean (exit 0)` throughout. One factual sentence inside the new
comment does not survive the same measurement — finding V-3.

## 3. Do the guards bind (`R8`)

Every mutation was applied to the working tree, run, and restored from a scratchpad copy
outside the worktree whose sha256 was compared before and after; `git status --porcelain` is
empty at the end of this record. Scratchpad digests: `run_bind_v2.py`
`84f7c449f22dac42b1be22e59050b4756dcb20fb8fe5bab36e557056417fa86e` — **equal to the digest
the fix commit reports for its own mutations**, an independent check on that evidence;
test file `09ebf5ec…`; `repo-audit.py` `5b126c24…`. Baseline: the target file is 22 tests
green (19 before this commit — three added).

| # | mutation | scope run | result |
|---|---|---|---|
| V1 | blocked branch advances to `AWAITING_FINAL` | target file | **RED** — 2 failed, on a value |
| V1′ | V1 against the **pre-fix** test file | target file | green — 19 passed (the counterfactual) |
| V2 | collapse the verdict conditional to one sentence | target file | **RED** — 1 failed (`SPEC_GAP` test) |
| V3 | `repair_round=1` added to the blocked advance | target file | **RED** — 1 failed |
| V4 | an `assurance_candidate_ref` written in the blocked branch | target file | **RED** — 1 failed |
| V5 | `blocked = True` always | target file | **RED** — 5 failed (negative control binds) |
| V6 | CHANGES_REQUIRED sentence reworded, same meaning | target file | **RED** — 1 failed (whole-line assertion) |
| V7 | `.pytest_cache` removed from `EXCLUDE` | repo-audit | 474 vs 472 over the identical tree |
| V8 | **unblocked** emit lands on `REVIEWED` not `AWAITING_FINAL` | whole suite | green — 632 passed |
| V9 | **unblocked** emit writes no `assurance_candidate_ref` | whole suite | green — 632 passed |
| V10 | **unblocked** emit never writes `assurance-candidate.json` | whole suite | green — 632 passed |

**What this establishes.** Every individual assertion in the new class has independent
binding force — V1 pins the status, V2 the verdict discrimination, V3 the repair round, V4
the absence of a candidate pointer, V6 the whole-line form of the sentence, V5 the negative
control. That is unusually complete for a new class: no assertion is decorative.

**What it does not establish.** V8–V10 are finding V-2. The template has **two** `--emit`
blocks (`:223` and `:278`); the repair brought the first under test and the second is still
dead to the suite. Landing the whole run on the wrong terminal status, dropping the
`assurance_candidate_ref`, and never writing `assurance-candidate.json` at all each leave all
632 tests green. That is the same defect shape L-1 named, still open on the branch whose
output a FINAL decision is taken against.

## 4. Findings

### Low (non-blocking — `R3`: not inflated; disposition is the user's at closeout, `R10`)

**V-1 — a round-0 `SPEC_GAP` is still told on stdout that it "owes a repair decision"; only
the persisted sentence was branched.** Location:
`ResearchSystem/assurance/templates/run-v2/run_bind_v2.py:221-222`. Ground truth: the
accepted finding O-2 itself — "a round-0 `SPEC_GAP` inherits the CHANGES_REQUIRED
next_action… told to author a repair decision" — against `EXECUTION.md:74-77`. The fix's own
comment says "the sentence is branched where the transition is not", but there are two
sentences at this branch and only the persisted one was branched. Measured above by driving
the shipped template. The decision that goes wrong: without `--emit` **no state is written at
all**, so the printed line is the executor's only signal, and it names an act the run does not
owe and points at a document nobody will author — precisely the harm O-2 stated. With
`--emit` the two channels now contradict each other, which is worse than either being wrong
alone: the terminal says repair decision, the state file says new WorkSpec revision.
Minimum fix: interpolate `next_action` into the printed line (it is already computed three
lines above), or branch the print the same way; and assert the printed line in
`TheBlockedRoundLandsOnReviewed`, which already captures stdout and discards it (O-2v).

**V-2 — the repair covers one of the template's two `--emit` blocks; the one that binds the
AssuranceCandidate remains unguarded.** Location:
`ResearchSystem/assurance/templates/run-v2/run_bind_v2.py:278-299`; the new class at
`test_run_v2_template_bind.py:374-462`. Ground truth: `E7`, test the defect class not the
reported instance — and the FULL's own diagnosis of the class was "the **entire** emit block
is dead to the suite". Shown by V8–V10, three mutations of increasing severity, all green
across 632 tests. The decision that goes wrong: the unblocked block performs the two-step
`REVIEWED -> AWAITING_FINAL` advance and writes the document a FINAL decision is taken
against, so a future edit there reintroduces a strictly worse version of the reported defect
with a green suite — and the class docstring's framing ("a state transition taken without
consulting the verdict that licenses it") would still read as covered. Stated as a low, not a
blocker: the FULL's stated minimum fix was met exactly and this is a pre-existing boundary the
repair landed inside rather than coverage it removed. Worth naming now because the expensive
part is already built — `seed_state` plus the `sys.argv` handling is the fixture the FULL
called "real machinery whose worth is the user's call", and the marginal cost of extending it
to the second block is now small.

**V-3 — the new `repo-audit.py` comment states a delta its own author measured as two.**
Location: `Thesis/Work/Tooling/repo-audit.py:32-34` — "a pass after the tests counted **four**
markdown files a pass before them did not". Ground truth: `E3`, a figure is emitted from the
command that produces it. Measured: from a clean tree the documented battery creates exactly
**one** cache markdown (`ResearchSystem/tooling/.pytest_cache/README.md`); the maximum
observed in this worktree is **two**, and the fix commit's own body says two ("the two cache
READMEs present right now", 474 vs 472). The four appears to come from the earlier
two-checkout comparison (475 vs 471), which mixed two trees and so established no cache
count. The decision that goes wrong: the comment is the durable explanation — the commit body
is not — and a later maintainer checking whether the exclusion is still earning its place
measures a delta of one or two, fails to find four, and either goes hunting for a third cause
that does not exist or distrusts the exclusion and removes it. Minimum fix: state two, or
state "one per cache directory pytest creates" and drop the absolute count.

### Observations (`R5` — reported; the conclusions are the user's)

**O-1v — three of the FULL's four lows are still undispositioned, and one of them sits in a
file that can still be edited.** The fix leg answered L-1 and O-2; L-4 is reported dissolved
by a user ruling I cannot see (`R7`), which leaves **L-2 and L-3**. `HARNESS-RIDERS.md`
carries no HI-REDEEM-5 row, so neither is banked yet. This is not yet a breach — `R10` puts
the spend-vs-bank choice at **closeout**, which is after this VERIFY — but it is worth
carrying into that conversation that the two are not symmetric. L-3 lives only in `b8fea97`'s
body, which `E8` forbids amending, and the FULL's record and `ca61820`'s body already correct
it in the durable record, so it is arguably answered. L-2 has a **second, still-editable
site**: `.goals/plans/harness-issue-redemption-batch.plan.md:125` still reads "11 files,
167+/17−" where the range is 256+/17−. That one will persist silently unless closeout routes
it.

**O-2v — the new class captures stdout and throws it away, which is the gap V-1 came
through.** `emit()` returns `(code, out, saved)` and all three tests bind it as `code, _,
saved`. The file's own docstring says "Assertions are made against WHOLE returned structures
and whole printed lines", and the sibling class `ARoundZeroBlockerBindsNoCandidate` does
assert the printed line. Had the new class kept that habit, V-1 would have been caught while
the fix was being written rather than after it.

**O-3v — two of the three items still ship with no regression guard, and the set-level
question the FULL raised as O-1 is now sharper, not softer.** Correction E is defended by a
reproducible measurement rather than a test (V7 changes no test outcome), which is a
deliberate `E6` call the commit states plainly. Combined with the FULL's O-1 — three of five
fixes in the parent round whose regression story is "read the code" — the batch's ceiling is
unchanged by this repair. Reported, not judged; whether that ceiling is acceptable across a
*set* remains the user's call.

**O-4v — a VERIFY has no verdict for "the repair is incomplete".** `R3` allows
`REVIEWED_NO_BLOCKER | SPEC_GAP`. V-1 is a genuine residual on an accepted finding, but it is
not a specification failure, so the only honest verdict is the clean one and the qualification
has to live in prose where a reader may skim past it. Noted as a shape (`R5`); the question
and the conclusion are the user's.

## 5. Boundary and record conformance — second (`R3`)

Re-ran every figure the fix commit states about the battery, in this worktree at the subject
tip, after the last mutation was restored:

```
$ python -X utf8 ResearchSystem/tooling/tests/run_tests.py      -> tests: 29  passed: 29  failed: 0  OK
$ python -X utf8 ResearchSystem/tooling/tests/run_p4_tests.py   -> tests: 80  passed: 80  failed: 0  OK
$ python -X utf8 ResearchSystem/tooling/tests/run_p5a_tests.py  -> tests: 39  passed: 39  failed: 0  OK
$ python -X utf8 …/N0/fixtures/validate_fixtures.py             -> 41/41 cases behaved as declared; failures=0
$ python -X utf8 -m pytest -q   (cwd ResearchSystem/tooling)    -> 632 passed in 103.18s
$ python -X utf8 ResearchSystem/tooling/rsc.py compile --check   -> live 173, 0 error(s) 0 warning(s);
                                                                    generated output fresh; lint clean (exit 0)
$ python -X utf8 Thesis/Work/Tooling/repo-audit.py               -> scope: 472; RESULT: clean (exit 0)
```

Every one matches, including the count: **632 = the FULL's 629 + the three tests this commit
adds**, which is itself a check that nothing was quietly disabled to keep the suite green.

**`E2`.** The frozen surface is untouched by inspection. All **fifteen** files under
`ResearchSystem/schema/document-assurance-v3/` carry byte-identical blobs at base and tip
(`b4ddfcf1`, `1bdb2cc2`, `6e87fe9b`, `bb2faacc`, `419a767f`, `42658e19`, `9133a3bc`,
`ed8dd969`, `19ab2c86`, `b8e2cafd`, `09aa8699`, `2350ff96`, `3617b74e`, `fe436c6a`,
`0e3447f5`) — fifteen is the count the 2026-08-03 re-baseline names. Supersession-1
`68031fa2` and supersession-2 `e1a2f26b` are unchanged and equal to the ids `E2` writes down.
No path in the change set is a frozen one.

**`E10`.** All nine instruction-layer members are byte-identical at base and tip:
`4d0c7330`, `70bd9f0b`, `810f5081`, `3350bfac`, `17ff31bb`, `52a97a48`, `68031fa2`,
`e1a2f26b`, `09aa8699`. The range writes no member, so no amendment read is owed and no
opening read is at issue on this leg.

**`E8`.** Title `V3-HI-REDEEM-5-FIX-v1` names the round; the kind is declared in the first
words ("Kind: review fix"); no trailers (`grep` for `Co-Authored-By` / `Signed-off-by` /
`Claude-Session` / `Generated with` returns nothing); the parent is the base, so no amend;
nothing outside the declared boundary. The body is **five** paragraphs — conformant under the
L-4 reading the commit reports the user ruled, and non-conformant under the literal reading;
that ruling is prose I cannot see (`R7`), so I record the fact and not a verdict on it.

**`E9`.** Accounted above: the fix leg is the round's one approved repair and this record
closes the VERIFY. No commit landed between dispatch and this record.

**`E12`.** The plan's resume pointer writes `--range da603da..HEAD` — base written, tip
`HEAD`, never a written SHA. The dispatch marker carries a resolved tip, which is the CLI's
display of a range and not a recorded one; it cannot be short here in any case, since
`git rev-list --count 3b28116..HEAD` is 0. I reproduced V-1, V-2 and V-3 before writing them,
to write them correctly rather than to adjudicate the executor.

**`E3` applied by the commit.** The two figures the FULL found short are re-measured and
correct here: 112 insertions and 3 deletions reproduce from the range exactly, and the
`repo-audit` digest claim is replaced by a before/after count I could repeat.

## 6. Coverage disclosure (`R4`)

**Read in full:** `CONSTRUCTION-CHECKLIST.md` (my standing instruction and its own
counterpart) and the review-contract stub that names it; `v3-review-full-f4e1be1.md`;
`3b28116`'s and `ca61820`'s complete bodies; the complete repair diff;
`rsclib/document_harness/assurance_state.py`; `run_bind_v2.py`'s `main()` from the round
branch to the end; the new test class and the test file's fixture layer
(`BindTemplateCase`, `run_main`, the hand-written review fixtures);
`HARNESS-RIDERS.md`; the run-v2 README's battery-tiering section.

**Sampled:** `.goals/plans/harness-issue-redemption-batch.plan.md` (Steps, Acceptance,
Resume pointer, correction B); `EXECUTION.md` (the *instruction itself is the problem*
section); `flow.py` (`_SUCCESSORS`, `TERMINAL_STATUSES`, the transition check at `:174-196`,
every `STOPPED_REPLAN` site); `v3-review-verify-275da5b.md` (format conventions only).

**Probed only:** `.harness/review-pending.json`; blob ids via `git rev-parse <rev>:<path>`
across the schema pack and the nine `E10` members; `.gitignore` for `.pytest_cache`;
`grep` for `--emit` sites and for commit-body trailers; the test file's length (570 lines).

**Executed:** the seven battery commands in §5; ten mutations plus one counterfactual (§3),
each restored and verified by sha256 from a scratchpad **outside** the worktree; a direct
drive of the shipped template at round 0 across `{CHANGES_REQUIRED, SPEC_GAP} ×
{--emit, no --emit}` capturing stdout and the saved state (§2); four `repo-audit` scope
measurements across four tree states; a from-clean battery to count the cache markdown files
it creates. `git status --porcelain` is empty and all three subject files carry their
committed digests.

**Not established.** The user's approval of the fix boundary and the L-4 ruling exist only in
prose — marked, not verified (`R7`, `R4`). Whether V-2's second emit block *should* be
brought under test, and whether the no-guard ceiling (O-3v) is acceptable across the set, are
the user's calls, not mine (`R5`). Mutation shows the new class has binding force; it does
not show that force is sufficient, and this VERIFY is not a re-certification of the FULL.

**Independence ceiling, disclosed rather than asserted.** I ran as a fresh-context subagent
reached through `rsc v3 dispatch`, handed the subject range and two operational notes and no
per-acceptance argument. I re-derived round, budget, authorization, obligations and every
figure from the repository. Two things I cannot claim. I cannot verify my own context is
fresh. And — as in the FULL, so this is now the second consecutive leg — the harness
surfaced the executor session's task list into my context as a system reminder, outside
either session's control; its item 8 names this round's fix scope and its item 9 the ledger
step. Nothing in it was load-bearing: every accepted item I verified was read from
`v3-review-full-f4e1be1.md` and the commit body, and no figure here comes from it. `R2` makes
chat-only material a disclosure regardless, so it is disclosed — and I did not write to that
list, since it belongs to the session under review.
