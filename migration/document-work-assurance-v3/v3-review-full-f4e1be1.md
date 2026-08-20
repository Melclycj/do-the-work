# FULL review — `da603da..f4e1be1` (HI-REDEEM-5, the five-HarnessIssue redemption round)

| | |
|---|---|
| round | FULL, construction-side (`CONSTRUCTION-CHECKLIST.md` R1–R10) |
| subject | `da603daa006e7086ccdbb4361da36a320e4eebcd..f4e1be1c64f5b7861535c5c20c24db21ba462e85` |
| range content | two commits: `b8fea97` (`V3-HI-REDEEM-5-v1`, kind: candidate) and `f4e1be1` (bookkeeping, self-declared non-work-product) |
| **verdict** | **`REVIEWED_NO_BLOCKER`** |
| findings | 0 blockers, 4 low, 4 observations |
| record | this file; the execution side commits it (`R6`) |

`REVIEWED_NO_BLOCKER` is scope-relative. Here it means: all five routed fixes are present
at their sources and each traces to its issue id; the two ported patches are byte-faithful
to the copies that ran a real round; the two new guards bind under mutation in the
directions they name; the one acceptance criterion that is a measurable property (#4's
byte-stability) reproduces **exactly** in this session, digest for digest; and no frozen
byte (`E2`) and no instruction-layer member (`E10`) is touched. Every figure the candidate
states about the battery reproduces here — one figure about the change set itself does not
(L-2).

The four lows are not defects in the shipped behaviour. In order: the half of fix #3 that
the issue's own harm statement names — *advances to REVIEWED* — is the half no test
exercises, shown by a surviving mutation rather than argued; a diffstat stated 89
insertions short in two places; a supporting sentence in the `E10` read is inaccurate twice
while its conservative conclusion stands; and the commit body is seven paragraphs where
`E8` says one and every recent construction round is one. Each names the decision that goes
wrong if it stays unfixed (`R9`).

## 1. Subject, re-derived (`R2`)

I was handed one range and nothing else. Round name, budget, authorization, obligations and
every figure below are re-derived here; no number from the dispatch prompt, the plan, the
ledger or the commit bodies is accepted as reported.

```
$ git rev-parse HEAD                      -> f4e1be1c64f5b7861535c5c20c24db21ba462e85
$ git rev-parse --abbrev-ref HEAD         -> document-work-assurance-v3
$ git rev-list --count f4e1be1..HEAD      -> 0
$ git status --porcelain                  -> (empty)
$ git rev-list --count da603da..f4e1be1   -> 2
$ git merge-base --is-ancestor da603da f4e1be1 -> yes
$ cat .harness/review-pending.json
  {"subject": "da603daa006e7086ccdbb4361da36a320e4eebcd..f4e1be1c64f5b7861535c5c20c24db21ba462e85",
   "dispatched_at": "2026-08-07T07:31:15+00:00"}
```

HEAD equals the range tip and the tree is clean, so worktree reads are reads of the subject
bytes. Dispatch (07:31:15Z = 17:31:15+10:00) post-dates the tip commit (17:30:57+10:00) by
18 seconds and the branch has taken no commit since — this record is the first it admits
(`E9`'s window).

The marker itself is the first piece of evidence in this round: it carries `subject` and
`dispatched_at` **and no `kind`**. That is fix (5)C observed in production, in the very act
that dispatched this review.

**Change set, classified by hand.** `git diff --numstat` over the range: **12 files, 293
insertions, 22 deletions**. Over `b8fea97` alone: **11 files, 256 insertions, 17
deletions**.

| path | class | frozen (`E2`)? | instruction layer (`E10`)? |
|---|---|---|---|
| `ResearchSystem/assurance/templates/run-v2/README.md` | template prose | no | no |
| `ResearchSystem/assurance/templates/run-v2/run_bind_v2.py` | template code | no | no |
| `ResearchSystem/assurance/templates/run-v2/run_evidence_v2.py` | template code | no | no |
| `ResearchSystem/assurance/templates/run-v2/run_repair.py` (**A**) | template code | no | no |
| `ResearchSystem/tooling/hooks/review_freeze_check.py` | hook code | no | no |
| `ResearchSystem/tooling/rsc.py` | CLI | no | no |
| `ResearchSystem/tooling/rsclib/document_harness/dispatch.py` | library | no | no |
| `ResearchSystem/tooling/tests/document_harness/test_precommit_checks.py` | test | no | no |
| `ResearchSystem/tooling/tests/document_harness_review/test_dispatch_freeze_marker.py` | test | no | no |
| `ResearchSystem/tooling/tests/document_harness_review/test_run_v2_template_bind.py` | test | no | no |
| `Thesis/Work/Tooling/repo-audit.py` | verifier script (outside `ResearchSystem/`) | no | no |
| `.goals/plans/harness-issue-redemption-batch.plan.md` (`f4e1be1` only) | plan / bookkeeping | no | no |

`E2` holds by inspection: the four frozen blobs are untouched and no path under
`ResearchSystem/schema/document-assurance-v3/` appears in the change set at all. `E10` holds:
none of the nine enumerated instruction-layer paths appears.

**Tier.** `ResearchSystem/tooling/**` and `Thesis/Work/Tooling/repo-audit.py` are tooling, so
under the run-v2 README's *Regression-battery tiering* (lines 187–196) this is
**tooling-touching, not doc-only**, and the full battery is owed. The candidate classifies it
the same way.

**Authorization, re-derived.** `git show 6078217` — five `user-decision-triage-*.json`
documents, `decided_by: Melclycj (user)`, `decided_at: 2026-08-07`, four `WORKFLOW_FIX` and
one `VERIFIER_FIX`, with the base half of issue 5 explicitly `DEFER`red in the triage
rationale. `HARNESS-LEDGER.md` line 31 carries this batch as breakpoint (b), and its
2026-08-03 ruling (lines 60–62) says ledger batches need no round while rule and template
changes do — so opening a round for this change set is the ruled-correct move. The DEFER's
revocation and the A+B′+C shape are recorded only in the plan Notes and the candidate body
(`R7`: I state the ceiling — I can read the DEFER in a committed triage file and the
revocation only in the executor's own prose; the revocation is not independently visible to
me).

**Budget (`E9`).** No review record for this round exists under
`migration/document-work-assurance-v3/`; `ls` returns nothing matching `b8fea97`, `f4e1be1`,
`da603da` or `redeem`. This is the round's first and only FULL, and its fix leg and VERIFY
are unspent.

## 2. The five fixes against their sources (`R3` — implementation first)

Read: the five issue files and their five triage decisions in full; `b8fea97`'s complete
diff; the three touched templates in full; `flow.py`'s transition table, `advance_checked`,
`check_transition` and `check_verify_outcome`; `assurance_state.advance`; the changed regions
of `rsc.py`, `dispatch.py` and `review_freeze_check.py`; the two touched test files in full.

**(1) `run_repair.py` + the README paragraph.** The template is a real adaptation of
`runs/p5b-claims/run_repair.py`, not a copy: `diff -u` shows the run-local docstring
(which findings were accepted, why f2/f3 were not) replaced by template guidance, `REPO =
RS_ROOT.parent` hoisted, and the hard-coded `CONTROL_ROOT` replaced by the
`RUN_ID`-parameterised f-string. That f-string form is byte-for-byte the convention the two
sibling templates already use (`run_bind_v2.py:56-57`, `run_evidence_v2.py:46,54`).
`RS_ROOT = HERE.parents[2]` resolves identically from `templates/run-v2/` and from
`runs/<run-id>/` — both are three levels under `ResearchSystem/`. The file parses and its
module level executes clean under an explicit-path import (`RUN_ID`, `CONTROL_ROOT`, `main`
all present). Its two substantive claims check out: `flow.advance_checked` is what moves
`repair_round` to 1 (`flow.py:305-306`), and the decision document is read and never
authored, which `EXECUTION.md`'s *What you may never author* requires. The README paragraph
names `run_repair.py`, p3-corr as precedent, and `runs/p5b-claims/run_repair.py` as the
worked instance, and closes the section's arithmetic ("three steps are templated") so the
count stays true.

**(2) `repair_round=REPAIR_ROUND`.** One keyword plus its comment, in the `advance()` call
that already names five other pointer fields. The candidate discloses — as CORRECTION D —
that the issue's own statement overstates the mechanism, and the disclosure is right:
`assurance_state.advance` merges (`updated = dict(state)`, `assurance_state.py:169`) rather
than rebuilding, and `flow.advance_checked` sets `updated["repair_round"] = 1` on entering
REPAIRING (`flow.py:305-306`), so on the ordered path the field is already 1 and the merge
preserves it. The ported line is redundant *there* and load-bearing only where the REPAIRING
transition was skipped — which is issue (1) of the same batch. Naming that narrowing rather
than shipping the issue's wider claim is the honest move, and the decision to add no
regression guard is argued from `E6` rather than omitted.

**(3) the round-0 blocked branch.** The condition and the whole `if blocked:` body are
**byte-identical** to `runs/p5b-claims/run_bind_v2.py:244-259`; the only delta beyond the
port is one comment clause and one docstring sentence naming `run_repair.py`. The branch is
placed after `subject_binding` and before the WorkSpec/CandidateRecord reads, so a blocked
round 0 never touches documents that do not exist yet. The transition it takes is legal:
`flow._SUCCESSORS` gives `EVIDENCED -> ('REVIEWED',)` and `REVIEWED -> ('REPAIRING',
'AWAITING_FINAL')`, so REVIEWED is reachable from where a round-0 bind stands and REPAIRING
is reachable from REVIEWED — which is exactly what the issue said the old code destroyed. It
uses `assurance_state.advance` rather than `flow.advance_checked`, matching the template's
own existing habit in the unblocked path four lines below; no gate is dropped relative to
what was there.

The one thing worth stating about the branch's *scope*: it fires for any non-`REVIEWED_NO_BLOCKER`
round-0 verdict, so a round-0 `SPEC_GAP` also lands at REVIEWED carrying the next_action
"user REPAIR decision (APPLY_ACCEPTED_FINDINGS / NO_REPAIR)", while `EXECUTION.md:74-77`
says a SPEC_GAP stops and is not patched inside the candidate. Nothing is stranded —
`STOPPED_REPLAN` is reachable from every status (`flow.py:191`) — so this is a recorded
sentence being verdict-agnostic, not a flow defect. Observation O-2.

At round 1 the same class is already closed elsewhere: the review v2 schema narrows a VERIFY
verdict to `REVIEWED_NO_BLOCKER | SPEC_GAP` (`review.v2.schema.json:68`) and
`check_verify_outcome` refuses SPEC_GAP (`flow.py:613-619`) before the branch is reached, so
the operative review at round 1 can only be clean. The fix therefore covers the whole live
surface of its class in this template.

**(4) the `repo-audit.py` scope line.** `print(f"...under {ROOT}")` → `"...under the
checkout root"`, with an eight-line comment recording the p5b-firewall incident. Its
acceptance criterion is a measurable property and I measured it rather than reading it:

```
$ python -X utf8 Thesis/Work/Tooling/repo-audit.py | head -4
  scope: 471 markdown files under the checkout root
$ sha256 of the captured stdout
  a92940f3d23c8472f21f0df8a36784653bebee7e9889edbd101e740a411ae07c   (18822 bytes)
$ grep for 'D:' / 'Thesis-stage-control-refactor' in the bytes -> both False
```

That digest is **identical** to the one the candidate reports from a different checkout —
independent reproduction of the acceptance criterion in a third context. Correction E is
also real and reproduces: with the `.pytest_cache/README.md` this session's own battery
created, the same command returns **472**; move that directory aside and it returns 471.
`repo-audit.py`'s `EXCLUDE` set does not name `.pytest_cache` and it enumerates with
`ROOT.rglob('*.md')`, so running the tests still perturbs the audit's own count. That is a
second, same-family, different-cause byte-stability hole, correctly left unrouted.

**(5) A + B′ + C.** *C* deletes `kind` from the marker in `rsc.py` and drops the display
token in `review_freeze_check.py`. I swept for other consumers: `grep -rn "review-pending"`
over the whole tree returns records, journals, plans and the two code sites, and no code
branches on `kind` anywhere. The live marker (§1) and the freeze hook run clean against each
other (`review_freeze_check.check()` → exit 0 on the current tree). The construction-prompt
fixture contains no `kind` token, so the prompt surface is untouched. *B′* appends the remedy
to `V3-DISPATCH-NOT-AN-EVIDENCE-COMMIT`: one string in an existing `Issue`, no new code path,
no branch. *A* is item (4). The **deferred base half is genuinely not built** — I read
`construction_dispatch_of` and the whole `_cmd_v3_dispatch` range branch and there is no
base-derivation, no run-shape heuristic, no new refusal. The withdrawn "every changed path
under one `runs/<id>/`" derivation appears nowhere in the code, only in the plan Notes as a
record of what was dropped.

**Immutability.** The five HarnessIssue blobs are identical at `6078217` and at `f4e1be1`
(`296993be`, `72d6d625`, `2380ed1c`, `6d7ff853`, `7f802514`) — redemption edited none of
them, as the plan's acceptance requires.

## 3. Do the guards bind (`R8`)

Every mutation below was applied to the working tree, run, and restored from a scratchpad
copy whose sha256 was compared before and after; `git status --porcelain` is empty at the
end of this record. Test target: `tests/document_harness_review/test_run_v2_template_bind.py`
unless noted.

| # | mutation | result |
|---|---|---|
| M1 | `blocked = False` | **RED** — `test_a_round_zero_changes_required_stops_before_the_candidate` |
| M2 | drop the round conjunct: `blocked = operative[...] != "REVIEWED_NO_BLOCKER"` | **green** — nothing fires |
| M3 | drop the verdict conjunct: `blocked = REPAIR_ROUND == 0` | **RED** — `test_a_clean_round_zero_is_not_stopped` |
| M4 | blocked branch advances to `AWAITING_FINAL` instead of `REVIEWED` | **green** — nothing fires |
| M5 | re-add `"kind": "construction-round"` to the marker | **RED** — `test_dispatch_freeze_marker` (+ consumer fixture) |
| M6 | revert the `repo-audit.py` scope line to `{ROOT}` | **green** — full `tests/`, nothing fires |
| M7 | strip the remedy clause from `NOT-AN-EVIDENCE-COMMIT` | **green** — full `tests/`, nothing fires |
| M8 | drop `repair_round=REPAIR_ROUND` from the evidence template | **green** — full `tests/`, nothing fires |
| M9 | repoint the repaired negative control back at `FULL_REVIEW` | **RED** — corroborates the candidate's account |
| M10 | `blocked = any(r[...] != "REVIEWED_NO_BLOCKER" for r in reviews)` | **RED** — `test_a_repaired_round_is_not_stopped_by_a_round_zero_blocker` |

Restore digests: `run_bind_v2.py` `708621e8…`, `rsc.py` `306aaa66…` — both equal to the
scratchpad digests the candidate reports for its own two mutations, which is an independent
check on that evidence.

**What this establishes.** All three claims the candidate makes about the new bind class are
true: M1 pins "a blocking round 0 stops", M3 pins "a clean round 0 is not stopped", and M10
pins "a repaired round is not stopped by the round-0 blocker it still binds" against exactly
the shape that comment names. The marker's whole-field-set assertion (M5) is a hand-written
literal and does stop a `kind` growing back. M9 corroborates the candidate's account of the
pre-existing negative control: with `FULL_REVIEW` the template now returns 0 at the branch,
`assertIsNone(code)` fails, and the `assertIsNone(gate.received)` half would indeed have held
by construction — the vacuity the repointing removes is real.

**What it does not establish.** M4 is the finding (L-1): no test in the repository drives
`--emit` on this template — `grep` for `--emit` and `sys.argv` in the test file returns
nothing, so under pytest `"--emit" in sys.argv` is always False and the entire emit block is
dead to the suite. The half of fix #3 that the issue's harm statement actually names —
*advances to REVIEWED* rather than AWAITING_FINAL — is unexercised, and swapping the target
status leaves 629 tests green. M2 is the weaker sibling: the `REPAIR_ROUND == 0` conjunct is
not independently pinned, though at round 1 the operative review can only be clean (§2), so
its removal changes no production behaviour.

## 4. Findings

### Low (non-blocking — `R3`: not inflated; `R10` leaves spend-vs-bank to the user at closeout)

**L-1 — the round-0 branch's state transition is guarded nowhere; only its printed sentence
is.** Location: `ResearchSystem/assurance/templates/run-v2/run_bind_v2.py:196-218` and
`ResearchSystem/tooling/tests/document_harness_review/test_run_v2_template_bind.py:322-372`.
Ground truth: `issue-p5b-claims-bind-round0-no-blocked-branch`'s harm is "binding a candidate
there **strands** a run … with REPAIRING unreachable", i.e. the wrong *status*, and
`E4` is the rule that a guard is not trusted until it has been seen fail. M4 shows the status
half fails nothing. The decision that goes wrong: the next edit to that block — reordering
the two advances, reusing the unblocked path's `AWAITING_FINAL` call, or a future refactor of
`assurance_state.advance`'s signature — reintroduces exactly the reported defect with a green
suite, and the class docstring's own framing ("a state transition taken without consulting
the verdict that licenses it") would still read as covered. Minimum fix: one test that drives
the emit path (set `sys.argv` around `run_main`, seed `control/state.json` with a valid
EVIDENCED state) and asserts the saved `status` is `REVIEWED`. Not blocking, and stated as
such deliberately: the shipped code is correct — I confirmed it three ways (byte-identical to
a branch that ran a real round in `p5b-claims`; legal against `flow._SUCCESSORS`; REPAIRING
reachable from where it lands) — the emit path has *never* been under test in this file, so
this is a pre-existing boundary the fix landed inside rather than coverage the round removed,
and a fixture rich enough to reach `assurance_state.save`'s schema validation is real
machinery whose worth is the user's call under `E6`.

**L-2 — the candidate's own diffstat is 89 insertions short, in two places.** Location:
`b8fea97` commit body, sentence 3 ("Eleven files, 10 modified and 1 added, 167 insertions and
17 deletions and nothing else in the range"), and `.goals/plans/harness-issue-redemption-batch.plan.md:125`
("11 files, 167+/17−"). Ground truth: `E3` — counts are emitted from the command that
produces them or omitted. `git diff --numstat da603da b8fea97` totals **256** insertions and
17 deletions across 11 files; 167 is the subtotal over the ten *modified* files, i.e. a
figure taken before `run_repair.py` (89 lines) was staged and then not re-run. The decision
that goes wrong: the sentence is the round's boundary claim ("and nothing else in the
range"), and its supporting count is the thing a later reader would reconcile against; a
reader who trusts 167 and finds 256 has to re-derive the whole boundary to learn that the
boundary claim is in fact true. The insertion count is the only figure in the candidate that
does not reproduce — every battery number does (§5). Minimum fix: state 256, or drop the
count.

**L-3 — the `E10` read's supporting sentence is inaccurate twice; its conclusion is not.**
Location: `b8fea97` commit body, final paragraph ("the only record naming either is
`v3-review-verify-a1fad7e.md`, a VERIFY record and not a read"). Ground truth: `E10` makes
citation depend on a record's blob ids, so which records name which blob is load-bearing for
the discharge decision. Two errors: (a) `ResearchSystem/document-harness/journal/simp-a4-2026-08-06.md:201`
names both current blobs (`README.md 70bd9f0b`, `EXECUTION.md 810f5081`) explicitly; (b)
`v3-review-verify-a1fad7e.md:355` does **not** name the current `EXECUTION.md` blob at all —
it records `ae8e60c9 → 8094a866`, and `810f5081` arrived later, at `8dae1e0`
(`V3-SIMP-A4-CANDIDATE-LINT-ERRATA-v1`). The conclusion is nonetheless correct and
conservative: neither a journal nor a VERIFY is a recorded end-to-end read, so neither
discharges citation, and both members were read end to end. The decision that goes wrong: the
next opening that reuses this sentence as its survey of what records exist would conclude the
survey was exhaustive when it was not, and would miss that `EXECUTION.md` moved twice in the
SIMP-A4 batch rather than once. Everything else in that paragraph reproduces exactly — see §5.

**L-4 — the commit body is seven paragraphs where `E8` says one.** Location: `b8fea97` body.
Ground truth: `E8`, "one dense paragraph, no trailers". Every recent construction-round body
is literally one paragraph (`214f743`, `c667d08`, `a1fad7e` — checked, each a single
paragraph, and `a1fad7e` carries comparably many items). The decision that goes wrong is
narrow and is about *this* clause's future: a rule that uniform precedent has just stopped
observing either wants restating or wants enforcing, and leaving one round silently outside
it makes the next round's choice a coin-flip. Nothing is lost from the record itself — the
content is complete and greppable — so if the user's reading is that `E8` means "dense, not
literally one block", this is the cheapest moment to say so and the finding dissolves.

### Observations (`R5` — reported; the conclusions are the user's)

**O-1 — two of the five fixes ship with no regression guard, and neither claims one.** M6
(`repo-audit.py`'s scope line) and M7 (the `NOT-AN-EVIDENCE-COMMIT` remedy) both survive the
full suite. For #4 the candidate substitutes something arguably stronger than a guard — a
reproducible output digest, which I independently reproduced byte-for-byte — and for B′ a
message assertion would be the machinery `E6` questions. Reported because the batch now has
three of five fixes whose regression story is "read the code", and whether that ceiling is
acceptable across a *set* rather than per item is a judgement, not a rule.

**O-2 — a round-0 `SPEC_GAP` inherits the CHANGES_REQUIRED next_action.** The new branch is
verdict-shaped but not verdict-*discriminating*: any non-clean round-0 verdict records
"user REPAIR decision (APPLY_ACCEPTED_FINDINGS / NO_REPAIR)", while `EXECUTION.md:74-77` says
a SPEC_GAP stops. Nothing is stranded (`STOPPED_REPLAN` is reachable from every status) and
the text is a faithful port of the instance that ran a real round, so this is a recorded
sentence, not a flow defect.

**O-3 — the dispatched range carries one more file than the candidate enumerates.** 12 files
over `da603da..f4e1be1` against `b8fea97`'s 11, the twelfth being the plan file in
`f4e1be1`, which self-declares "执行期记账，非本轮 work product". This is the shape `E12`
predicts — a recorded range's tip is `HEAD`, and what a written tip drops is the round's own
last-written records — so it is noted for completeness rather than as a boundary breach.

**O-4 — `run_repair` now lives under a heading that says the opposite.** The new paragraph
sits in the run-v2 README's *"Steps that did not change"*, which is precisely where the
triage decision directed it, and the section's new closing line reconciles the arithmetic.
Reported only because a reader scanning headings for "what is templated" will not look there,
and the run-v2 README's own layer question is already an open item in the ledger.

## 5. Boundary and record conformance — second (`R3`)

Re-ran, in this worktree at the subject tip, every figure the candidate states about the
battery:

```
$ python -X utf8 ResearchSystem/tooling/tests/run_tests.py      -> tests: 29  passed: 29  failed: 0   exit 0
$ python -X utf8 ResearchSystem/tooling/tests/run_p4_tests.py   -> tests: 80  passed: 80  failed: 0   exit 0
$ python -X utf8 ResearchSystem/tooling/tests/run_p5a_tests.py  -> tests: 39  passed: 39  failed: 0   exit 0
$ python -X utf8 ResearchSystem/migration/document-work-assurance-v3/N0/fixtures/validate_fixtures.py
                                                                -> 41/41 cases behaved as declared; failures=0
$ python -X utf8 -m pytest -q   (cwd ResearchSystem/tooling)    -> 629 passed in 108.05s
$ python -X utf8 ResearchSystem/tooling/rsc.py compile --check   -> live 173, diagnostics 0 error(s) 0 warning(s);
                                                                    generated output fresh; lint clean (exit 0)
$ python -X utf8 Thesis/Work/Tooling/repo-audit.py               -> RESULT: clean (exit 0)
```

Every one matches (629 passed, 29/29, 80/80, 39/39, 41/41, fresh + lint clean, exit 0). Two
further fixture validators exist and also pass (`schema/harness-v2` 93/93,
`schema/stage-control-fixtures` failures=0); neither is in the tiering rule's enumeration and
neither was claimed.

`E10` opening cold read, re-derived rather than accepted: the nine members at `f4e1be1` carry
blobs `4d0c7330`, `70bd9f0b`, `810f5081`, `3350bfac`, `17ff31bb`, `52a97a48`, `68031fa2`,
`e1a2f26b`, `09aa8699`. Against `v3-checkpoint-read-a5a04c3.md` §1's table, members 1 and 4–9
are **equal row for row**, so the seven-member citation is valid; members 2 and 3 differ
(`ae887dd4`→`70bd9f0b`, `df2a7834`→`810f5081`), so the claim that they needed reading is
correct, and their stated lengths reproduce exactly (`git show | wc -l` → 37 and 171). The
attribution "moved by the SIMP-A4 batch" holds at batch granularity (`a1fad7e` for
`README.md`, `8dae1e0` for `EXECUTION.md`); only the survey sentence about which records name
them is wrong (L-3). No instruction-layer member is written by this range, so no amendment
read is owed.

`E8` otherwise conforms: title `V3-HI-REDEEM-5-v1` names the round in the required form, the
kind is declared ("Kind: candidate"), no trailers, no amend (`f4e1be1` is a new commit on top,
not a rewrite of `b8fea97`), nothing outside the declared change boundary. `E9` conforms: this
is the round's first FULL and no commit landed between dispatch and this record. `E12`
conforms: the plan's resume pointer writes `--range da603da..HEAD` — base written, tip `HEAD`,
never a written SHA. `E11`'s preview card is asserted in the body and is not visible to me
(`R4`: marked, not verified).

## 6. Coverage disclosure (`R4`)

**Read in full:** `CONSTRUCTION-CHECKLIST.md` (my standing instruction, and its own
counterpart); the review-contract stub that names it; the five HarnessIssue files and five
triage decisions; `.goals/plans/harness-issue-redemption-batch.plan.md`; `HARNESS-LEDGER.md`;
`b8fea97`'s and `f4e1be1`'s complete bodies and complete diffs; `templates/run-v2/run_repair.py`;
the changed regions plus surrounding functions of `run_bind_v2.py`, `run_evidence_v2.py`,
`rsc.py:_cmd_v3_dispatch`, `dispatch.py:control_root_of`, `review_freeze_check.py`,
`repo-audit.py`; `test_run_v2_template_bind.py` (whole) and the changed classes of
`test_dispatch_freeze_marker.py` and `test_precommit_checks.py`;
`runs/p5b-claims/run_repair.py` and the blocked-branch region of `runs/p5b-claims/run_bind_v2.py`;
`flow.py`'s transition table, `check_transition`, `advance_checked`, `check_verify_outcome`;
`assurance_state.advance`; `v3-checkpoint-read-a5a04c3.md` §1; the run-v2 README's
battery-tiering and *Steps that did not change* sections.

**Sampled:** `EXECUTION.md` (the SPEC_GAP and *After a review* sections only); `REVIEW.md`
(the marker clause only); the three precedent commit bodies `214f743` / `c667d08` /
`a1fad7e`; `v3-review-full-838c413.md` (structure and §1); `simp-a4-2026-08-06.md` (the two
grep hits); the review schemas' verdict enums.

**Probed only:** `.harness/review-pending.json`; blob ids via `git rev-parse <rev>:<path>`;
`grep` sweeps for `review-pending`, `kind`, `control_root_of`, `NOT-AN-EVIDENCE-COMMIT`,
`--emit`; the construction-prompt fixture (token count, not content).

**Executed:** the seven battery commands in §5, two extra fixture validators, ten mutations
(§3), the byte-stability capture and digest (§2), an explicit-path import of the new
template, and `review_freeze_check.check()` against the live marker. All working-tree
mutations were restored and verified by sha256; `git status --porcelain` is empty.

**Not established.** `E11`'s preview card and the user's revocation of issue 5's DEFER exist
only in prose I cannot cross-check — marked, not verified (`R4`). Whether the emit path
*should* be brought under test, and whether `E8`'s "one dense paragraph" means what its
precedent has been doing, are the user's calls, not mine (`R5`).

**Independence ceiling, disclosed rather than asserted.** I ran as a fresh-context subagent
reached through `rsc v3 dispatch`, handed the subject range and two operational notes and no
per-acceptance argument — the channel the plan itself describes (line 76). I re-derived
round, budget, authorization, obligations and every figure from the repository. Two things I
cannot claim: I cannot verify my own context is fresh, and the harness surfaced the executor
session's task list into my context as a system reminder. Nothing in that list is
load-bearing here — it named no fact I used and no figure I report — but `R2` makes chat-only
material a disclosure, so it is disclosed.
