# Phase C0 (M8 + M10) — FULL review of `a918e37..7572abd`

Review-side output for the Phase C0 construction round. Authored by the independent bounded
reviewer under [`../../document-harness/CONSTRUCTION-CHECKLIST.md`](../../document-harness/CONSTRUCTION-CHECKLIST.md)
(R1–R9), which supersedes [`v3-harness-review-contract.md`](v3-harness-review-contract.md) —
that file is now a stub pointing at the checklist, and the dispatch prompt's reference to it
resolves there. Not a node artifact, binds nothing. Written in-worktree, untracked; committing
it is the execution side's act (R6).

- **Round:** this range's one FULL. Derived, not accepted: no commit in `a918e37..7572abd`
  records an independent review, no `v3-review-{full,verify}-*` record exists for any commit in
  it, and the three non-candidate commits classify themselves as plan / pointer /
  pre-submission correction. Under E9's discriminator — *has a valid independent FULL already
  occurred?* — the answer is no, so everything in the range is pre-submission and consumes
  nothing, and this is the FULL. **Budget after this record: the one user-approved fix and the
  one targeted VERIFY are unspent.**
- **Verdict:** `CHANGES_REQUIRED` — two blocking findings. Both are on guards this round added
  and did not mutation-probe; neither is on the capability the round was authorized to build.
  M8 and M10 are implemented, and every guard the round *did* probe binds. The two it did not
  probe are exactly the two that do not bind.
- **Findings:** 2 must-fix, 4 low, 4 observations.

---

## 1. Subject re-derivation (R2 — every figure below is mine, none reported)

| Check | Result |
|---|---|
| range resolves | `a918e37a876d41909330f32f7a22b14d52f6f7b1..7572abd96af3bdeb3442f679fd6364f0ace355fe` |
| linear, no merges | `git log --merges` over the range: empty; 5 commits |
| base is the last accepted state | `a918e37 V3-E6-BOTH-SIDES-v1`, the last instruction-layer amendment; `git rev-list --all --children` gives it exactly one child, `8c5c968` |
| HEAD == tip | `7572abd96af3bdeb3442f679fd6364f0ace355fe`, branch `document-work-assurance-v3` |
| worktree carries no smuggled change | `git status --porcelain` → one line, `?? ResearchSystem/docs/` (untracked, present at prior rounds). No tracked modification |
| not pushed | no `origin/document-work-assurance-v3`; `git rev-list --count origin/main..HEAD` = 223 |
| changed paths, classified by hand | **7** — `A .goals/plans/harness-phase-c0-m8-m10.plan.md` · `M .goals/plans/harness-deletion-first-stabilization.plan.md` (1 line, adds the link to the C0 plan) · `M ResearchSystem/HARNESS-LEDGER.md` · `M ResearchSystem/assurance/templates/run-v2/run_evidence_v2.py` · `M ResearchSystem/tooling/rsc.py` · `A .../tests/document_harness_review/test_review_cli_v2_subject.py` · `A .../tests/document_harness_review/test_run_v2_template_fulfillment.py`. Net +778 / −18 |
| dispatch reproduces | `rsc.py v3 dispatch --range a918e37..HEAD` → `derived round : a918e37…..7572abd…`, exit 0, and the emitted prompt is byte-for-byte the one I was handed |

**Permanent boundaries — intact (E2).** `git diff a918e37 7572abd` restricted to
`ResearchSystem/schema/` and `ResearchSystem/contract/` is empty; recursive file counts at HEAD
are 14 and 11. The three signed blobs `8ad404b1` / `b2dbdf75` / `68031fa2` each still
`git cat-file -t` → `blob`. Both user-locked oracles
(`tooling/tests/fixtures/expected-construction-prompt.txt`,
`tooling/tests/document_harness/test_readme_enumeration.py`) appear in no diff in the range.
`ResearchSystem/document-harness/` and `ResearchSystem/migration/` are untouched, so the
instruction layer carries no bytes from this round.

**Baselines I re-ran, immediately before writing this (E3).** All five suites from a clean
worktree, restored and sha256-verified after every probe below:

| suite | invocation | result |
|---|---|---|
| `document_harness` | `python -m unittest discover -s tests/document_harness -t tests/document_harness` | Ran 137, OK |
| `document_harness_review` | same shape | Ran 314, OK |
| `harness` | `python tests/harness/run_tests.py` | Ran 39, OK |
| `stage_control` | `python tests/stage_control/run_tests.py` | 20 run, 0 failures |
| P2 golden | `python ResearchSystem/tooling/tests/run_tests.py` | tests: 29, passed 29 |
| repo audit | `python Thesis/Work/Tooling/repo-audit.py` | `RESULT: clean (exit 0)` |

The `+19 / baseline 295` figure is derivable rather than accepted: the two new files carry
7 + 12 = 19 test methods and `git diff --name-status` shows no *modified* test file in the
range, so 314 − 19 = 295.

**Authorization — as far as the repository carries it (R7).** The committed ledger records the
2026-07-28 rulings that scope this round: M10 scope = A (do the defect table's wording even
though half its premise was falsified), and the `E10` amendment read for
`079361f a07dec0 5937164 a918e37` waived. Both are recorded twice — ledger `▶ 当前指针` and the
C0 plan Step 0 — and both are labelled by the executor as an **explicit override** of `E10`
rather than an exit the rule provides, which is the honest form. Ceiling: I hold no session
message; committed bytes in the file the checklist designates for rulings is more than a hint
and less than proof of what was said.

---

## 2. Implementation (R3 — leads)

### M8 — "模板要求逐条显式 status；缺条目=拒绝"

Implemented as specified. `LOCATORS` becomes `FULFILLMENT`, one whole claim per obligation;
`build_claims` reads `status` from it, supplies none, and returns unanswered obligations as
`unfilled`; `main()` refuses on `unfilled` before the checks, the writes and the evidence
commit. Entries are copied through verbatim, so `candidate-record.schema.json` stays the only
home of the per-status shape rules — I confirmed the schema does carry them: `fulfillmentClaim`
is `additionalProperties: false`, requires `implementation_locators` for `IMPLEMENTED`, and
requires `note` (minLength 8) while forbidding locators for `NOT_IMPLEMENTED`. No schema byte
was needed and none was touched.

The two disclosures the round attached to M8 are accurate, checked here rather than accepted:

- `NOT_IMPLEMENTED` does not block a run. `check_record` (candidate.py:350–405) never reads
  `status`; `views.coverage_report` does not gate on it (`views.py` reads it only at line 52,
  to render); `check_locators` skips non-`IMPLEMENTED` at candidate.py:490. Correctly left out
  of scope — M8's wording is "explicit status; missing entry refused", not "NOT_IMPLEMENTED
  blocks".
- Nothing else in the template assumed implementation. I read the file whole; the `claims`
  comprehension was the only such site.

### M10 — "`--subject <SHA>` 模式接 v2 双检查"

Implemented as specified, and the derivation is genuinely reused rather than re-written: the
new `_cmd_v3_review_subject` calls `dispatch.resolve_subject`, `dispatch.control_root_of`,
`review_subject.read_control_plane` and `review_subject.subject_of`, and adds no second copy of
that logic. `--subject` / `--package` are a mutually exclusive required group; `--spec` /
`--record` drop out of argparse and are re-enforced inside the v1 branch. `--result` routes to
`check_review_result_v2`, which reaches `check_subject` itself (review_result_v2.py:108), and
the derived-subject call is correctly *not* also made in that branch — the two are different
documents and running both would double-report.

The round's disclosure that M10's premise is half false is correct and I re-derived it:
`check_subject` already had a CLI caller through `v3 dispatch --subject` → `dispatch_of` →
dispatch.py:298; only `check_review_result_v2` had none. Following the defect table's wording
anyway was the user's ruling with the falsification on the table, so it is not a finding.

The disclosed self-comparison is real and correctly characterised: with no `--result`, the
subject is rebuilt from the CandidateRecord it is then compared against, so four of
`check_subject`'s five identity rows compare a value with itself. `control_root` remains a real
comparison (derived from the commit's staged paths vs. the record's authored value), and the
completeness / freshness / containment halves are unaffected. It is the shape `dispatch_of` and
the run template already have, so E6 says leave it — agreed, and adding machinery for it would
be the wrong move.

I also probed the one branch the round disclosed but did not test — `subject_checked = False`,
which prints a warning and appends **no** Issue on the argument that the plane report already
refuses. I built two scenarios (CandidateRecord with `candidate_ref` dropped; with
`base_revision` dropped) and ran the real CLI: both print the `!!` disclosure line, both add
`V3-SUBJECT-DOCUMENT-INVALID … is a required property`, both exit 1. The argument holds. See O2
for what it rests on.

---

## 3. Do the guards bind? (R8 — every row below is a probe I ran)

Restore discipline: both files copied to a scratchpad before the first probe and restored from
those copies after each, never `git checkout --`. Post-restore sha256 matches the pre-probe
value byte for byte — `run_evidence_v2.py` `83560757637d8251e2deff2d97b78cd449239fd5de35ef74e1c4ea0f641e353f`,
`rsc.py` `76cae3b0d61c5fdcbc498c38d888686a17b0b060ae0d259f0361eaa162972ce5` — and
`git status --porcelain` is back to the single untracked line.

| # | guard this round added | probe (real defect shape) | outcome |
|---|---|---|---|
| G1 | `build_claims` never supplies a status | restored the original comprehension: `status: "IMPLEMENTED"` for every obligation, `unfilled = []` | **binds** — 5 value-level failures, e.g. `Lists differ: … 'status': 'IMPLEMENTED' … != … 'status': 'NOT_IMPLEMENTED', 'note': …`. Not a crash |
| G2 | `main()` refuses when `unfilled` | deleted the four-line `if unfilled: … return 1` | **does not bind** — 7/7 still OK → **F2** |
| G3 | CLI reaches `check_review_result_v2` | dropped its report (`report + …` → bare call) | **binds** — 3 failures, and the CLI prints `RESULT: sound subject (exit 0)` over a result answering for another commit, which is the fail-open shape M10 exists to close |
| G4 | CLI reaches `check_subject` | dropped its report | **binds** — exactly 1 failure, the test that names `V3-SUBJECT-CHECK-RESULT-MISSING` |
| G5 | v1 mode still requires `--spec` / `--record` | neutered the computation (`missing = []`) | **does not bind** — 12/12 still OK → **F1** |

G1, G3 and G4 reproduce probes the round reports; I ran them independently and reach the same
place, with G1 taken to the full original defect shape rather than a `setdefault` variant.
G2 and G5 are probes the round did not run.

---

## 4. Blocking findings

### F1 — the test that names the v1-input guard is satisfied without it

- **Location:** guard at `ResearchSystem/tooling/rsc.py:509–517`; test
  `ResearchSystem/tooling/tests/document_harness_review/test_review_cli_v2_subject.py:214–219`
  (`test_the_version_one_mode_still_requires_its_spec_and_record`, docstring: *"Making them
  non-required for `--subject` must not make them optional for v1"*).
- **Ground truth violated:** E4 — *never trust a guard you have not seen fail: mutation-test
  every new guard*; and E5 — *assert the whole line, never a substring unrelated content can
  satisfy*. The commit body states both fixes "were then mutation-probed by reproducing the
  real defect shape" and names three probes; this guard is a fourth and got none.
- **Evidence.** With `missing = []` substituted for the guard's computation, all 12 tests in the
  file still pass. The reason is the fixture: the test passes `--package whatever.json`, a path
  that does not exist, so `load_package` short-circuits to `FATAL: document not found:
  whatever.json`, exit 2, no traceback — identical with and without the guard. The defect the
  guard actually prevents needs a *readable* package: with the guard neutered,
  `rsc.py v3 review --package /tmp/pkg.json` (valid JSON, no `--spec`) raises
  `TypeError: argument should be a str or an os.PathLike object … not 'NoneType'` at
  `spec.py:67` and exits 1 with a full traceback — precisely what the test's
  `assertNotIn("Traceback", …)` was written to catch, and what it never reaches.
- **Minimum fix:** point the test at a package file that exists and parses — the sibling test at
  line 179 already writes one — and assert the whole emitted line,
  `FATAL: --package mode requires --spec and --record`, rather than an exit code an unrelated
  failure produces. No production code changes.

### F2 — M8's specified behaviour has no test; only its helper does

- **Location:** refusal at
  `ResearchSystem/assurance/templates/run-v2/run_evidence_v2.py:132–136`; test file
  `ResearchSystem/tooling/tests/document_harness_review/test_run_v2_template_fulfillment.py`.
- **Ground truth violated:** E4. M8's wording, quoted verbatim into the plan's Acceptance, is
  *"模板要求逐条显式 status；**缺条目=拒绝**"*, and the Acceptance claims "套件里有一个曾经红过的
  负向测试证明'缺条目会被拒绝'". What the suite proves is that `build_claims` *reports* the
  obligation as `unfilled`. The step that converts that report into a refusal is a new guard,
  and nothing exercises it.
- **Evidence.** Deleting the four-line `if unfilled:` block from `main()` leaves the suite fully
  green. `run_evidence_v2.py` is referenced by exactly one test module (grep over
  `tests/**/*.py` returns two hits: this file, and `test_review_v2_subject.py:51`, whose
  `TEMPLATE_DIR` is used only to load `check_template_instance.py` at line 696), and that module
  runs 7/7 OK under the mutation. So no test anywhere observes the refusal.
- **Minimum fix:** one test that calls `main()`. `EVIDENCE`, `CONTROL` and `FULFILLMENT` are
  module globals read at call time, so a test can point them at a temp dir holding a minimal
  `work-spec.json` / `resolved-plan.json`, leave one obligation unanswered, and assert
  `main() == 1` *and* that the temp evidence dir is empty — which pins both halves of the claim
  ("refused", and "before anything is written"). No production code changes.
  - Related, and cheaper to fix in the same edit than to argue about: `main()` calls
    `EVIDENCE.mkdir(parents=True, exist_ok=True)` at line 125, before the refusal at 132. The
    round's claim that the refusal precedes "anything is written" is true of documents and false
    of that directory. Moving the mkdir below the refusal makes the claim exactly true.

Both fixes are test-side. Note E6's both-sides clause does not bite here: neither finding names
existing text or code as wrong in a way a *new rule* could paper over — the fix is the test
changing, which is the thing itself.

---

## 5. Low (non-blocking; would ride an approved repair, never justify one)

- **L1 — the ledger's dispatch line is the stale one the round corrected twice elsewhere.**
  `ResearchSystem/HARNESS-LEDGER.md:28` still reads `rsc v3 dispatch --range a918e37..d9ff80a`.
  `baee1aa` and `7572abd` diagnosed exactly this recurrence — a written tip is structurally one
  commit short — and applied the derivation-not-result fix to the **plan only**. Not
  wording-level under R9, because a downstream decision goes wrong and can be named: `CLAUDE.md`
  designates this file as the harness track's live pointer and the first thing a cold session
  reads, so that session re-issues a range three commits short, omitting the very commit that
  carries this round's two user rulings. Fix: one line, `a918e37..HEAD`, matching the plan.
- **L2 — `--check-result` is accepted with `--subject` and silently dropped.** It is consumed
  only in the v1 branch (`rsc.py:527`). Nothing false is admitted as evidence — subject mode
  derives check results from the commit — but a reviewer who passes it gets no signal it was
  ignored, which sits oddly beside the same round's care to re-enforce `--spec`/`--record` and
  to test that `--executor` really reaches the checker. Fix: refuse the combination, or say it
  is unused in this mode.
- **L3 — `3e27b5f` does not name its kind from E8's set.** Its body says "Pointer update, not a
  code change"; E8 asks for candidate / pre-submission correction / review fix / closeout /
  errata *so the review side can attribute it without asking*. I could still attribute it (no
  FULL had occurred, so it is a pre-submission correction), but by derivation rather than by
  reading, which is what the rule exists to avoid. Its two siblings do name their kind.
- **L4 — the new command truncates the subject to 12 hex** in its header line
  (`rsc.py`, `evidence commit : …[:12]`), while `dispatch.resolve_subject`'s own docstring
  records why an abbreviated commit is a weaker binding than the custody chain assumes and why
  the routed document always carries 40. This output is a check result, not a dispatch document,
  so the exposure is small — but a reviewer copying the printed value into a record copies the
  weaker form.

---

## 6. Observations (no action implied; R5 — what should exist is not mine to conclude)

- **O1 — one line of the reused derivation is not reused.** The new command falls back with
  `record.get("repair_round", 0)`; `dispatch_of` (dispatch.py:294) falls back with
  `record.get("repair_round", state.get("repair_round", 0))`. Both defaults are unreachable
  while `candidate-record.schema.json` keeps `repair_round` required, so nothing turns on it
  today. Recorded only because "reuse, don't keep a second copy" was the round's own stated
  principle and this is the one place the copy differs.
- **O2 — the untested branch is safe *because of the schema*, not because of the branch.** The
  `subject_checked = False` path adds no Issue; it exits 1 solely because
  `read_control_plane` validates the record and `candidate-record.schema.json` lists
  `candidate_ref` and `base_revision` as required (verified empirically, §2). `dispatch_of`, at
  the same fork, appends an explicit `V3-DISPATCH-SUBJECT-UNCHECKED` Issue instead of relying on
  that. The two siblings therefore have different failure independence at the same fork.
- **O3 — where this round's defects landed.** M8 and M10 are implemented to their quoted
  wording, all five suites are green on my own runs, the frozen surface is untouched, and three
  of the round's five new guards bind under adversarial probes. Both blockers are in the
  test layer, on the two guards the round did not probe. The pattern — the capability lands, the
  postcondition policing it is what fails review — has appeared before in this line's records
  (`v3-review-full-dcfb2f2.md`, CHANGES_REQUIRED, "both about the *guard the fix added*"). I
  report the shape; whether it warrants anything is yours.
- **O4 — the round's five self-disclosures all survive checking.** M9's incompleteness, M10's
  half-false premise, the derived-subject self-comparison, the `E10` waiver as an explicit
  override, and `NOT_IMPLEMENTED` not blocking a run — each is stated accurately, in the right
  place, and none understates. Nothing in the range was hidden from me, and the two blockers
  above are not things the round claimed to have done and hadn't; they are things it claimed to
  have *proved* and hadn't.

---

## 7. Process and record conformance (R3 — boundary check, run second)

| Rule | State |
|---|---|
| E2 frozen bytes | intact — §1 |
| E3 measure last | figures in the plan and commit match mine on every item I could re-run: 137 / 314 / 39 / 20 / 29, repo-audit exit 0, 14 schema + 11 contract files, both oracle blobs unchanged, both scratchpad sha256 values. No unbacked characterization found |
| E4 / E5 guard discipline | **violated twice** — F1, F2 |
| E6 no new machinery | respected; two disclosed shapes (self-comparison, `NOT_IMPLEMENTED` not blocking) were correctly left alone rather than guarded |
| E7 defect class not instance | met on M8 — the test targets "status is never supplied by the template", not the one reported line |
| E8 git | explicit-path staging: consistent with the diff, not directly observable — **marked**. No amend, no push (no remote branch; 223 ahead of `origin/main`). In-boundary: all 7 paths are M8 / M10 / this round's own records. Titles `V3-PHASE-C0-*-v1`, one dense paragraph each, no trailers. Kinds named on 4 of 5 commits — L3 |
| E9 budget | this is the FULL; the three non-candidate commits consume nothing under the discriminator, and each says so except `3e27b5f`. Fix and VERIFY unspent |
| E10 instruction layer | untouched by this round. The outstanding amendment read was waived by the user and the waiver is disclosed in both the ledger and the plan as an override rather than a rule exit |
| E11 preview card | plan Step 2 records it as rendered and approved. Chat-only — **UNVERIFIABLE** (R4) |
| E12 handoff | one range, no per-acceptance argument. Confirmed by reproducing the dispatch |

---

## 8. Disclosure of what I read (R4)

- **In full:** `CONSTRUCTION-CHECKLIST.md`; the C0 plan; `HARNESS-LEDGER.md`; all five commit
  messages; `run_evidence_v2.py`; both new test files; the whole `rsc.py` diff;
  `dispatch.py` through `dispatch_of`; `review_subject.py` through `check_subject`'s identity
  block; `review_result_v2.check_review_result_v2` to line 160;
  `candidate-record.schema.json`'s top-level required list and `$defs.fulfillmentClaim`.
- **Sampled:** `candidate.py` (the `check_record` invariant block and `check_locators`'s status
  line); `views.py` (every `status` occurrence); the parent plan's one changed line; prior FULL
  records' verdict lines only.
- **Probed only:** the five mutations in §3; the two malformed-record scenarios in §2; the
  dispatch reproduction; the frozen-surface and count commands.
- **Not read:** `review_result_v2.py` past line 160; the rest of `rsc.py`; the other 300-odd
  tests individually (I ran them, I did not read them); `EXECUTION.md` / `REVIEW.md`, which
  govern product runs and not this round.
- **`UNVERIFIABLE`, not folded into supported:** that the preview card was rendered and approved
  (E11); that staging used explicit paths rather than `add -A` (E8) — the diff is consistent
  with it and that is all I can say; that the FULFILLMENT template shape survives a real run,
  since no run exercises it yet and M9 is out of scope by ruling, so only the single-round
  happy path is reachable.
- **Mutation ceiling:** the probes in §3 prove those tests have binding force or lack it. They
  do not prove the binding ones are *sufficient*, and this FULL is not a certification of the
  wave-2 checks themselves — only of what this range did to them.
