# V3 review — FULL — subject `7052a89`

**Subject range** `e8ca95c0..7052a89b` — three commits: `V3-PHASE-C1.5-PLAN-AND-RULINGS-v1`
(`6c39d92`), `V3-PHASE-C1.5-PLAN-REVISION-v1` (`fb77e95`), `V3-PHASE-C1.5-DIGEST-NARROWING-v1`
(`7052a89`, the candidate).

**Verdict: `REVIEWED_NO_BLOCKER`.**

The narrowing does what it claims. Both read-side gates key off one frozenset, a digest that is
present is still checked on **every** field, the write side stops computing digests only where the
round said it would, and all eleven guards bind at value level under independent mutation probes I
ran myself. The frozen surface is untouched, the five suites reproduce at exactly the claimed
counts, and the E2 override is disclosed in the shape the checklist demands rather than dressed up
as an in-rule exit. Five non-blocking findings follow in §4; none would survive as a blocker and
none should burn the round's single repair.

> ### ⚠ The worktree changed under this review, mid-session — read this before re-deriving anything
>
> At `04:19` a `git status` showed six tracked files modified and a **new untracked file inside the
> E2-frozen contract directory**, none of it mine:
>
> ```
>  M ResearchSystem/assurance/templates/run-v2/README.md
>  M ResearchSystem/assurance/templates/run-v2/run_bind_v2.py
>  M ResearchSystem/tooling/rsclib/document_harness/assurance_state.py
>  M ResearchSystem/tooling/rsclib/document_harness/issues.py
>  M ResearchSystem/tooling/rsclib/document_harness/review_subject.py
>  M ResearchSystem/tooling/tests/document_harness_review/test_review_v2_subject.py
> ?? ResearchSystem/contract/Document-Work-Assurance-Contract-v3-supersession-2.md
> ?? ResearchSystem/docs/
> ```
>
> The content identifies it: `issues.py`'s "immutable once written" is being reworded, and
> `Document-Work-Assurance-Contract-v3-supersession-2.md` is being drafted as a versioned successor
> narrowing supersession-1 §3. That is a **later round being authored in this same worktree while
> this round's FULL was unreturned**, and it edits the very two modules this verdict certifies.
>
> **My figures are unaffected, and I can show why rather than assert it.** Every concurrent write
> is stamped `≥ 04:17:31`; my last write to the worktree was the `checks.py` probe restore at
> `04:14:58`, and `checks.py` still hashes to my pre-probe baseline
> (`c093ad76e69d4ddc9d97c6a57d5aa5e7e87bf06f69a3e25fecd961d91495441e`). The two windows do not
> overlap, so no restore of mine clobbered a concurrent edit and no concurrent edit was inside any
> suite run or probe. All eleven probes reported `RESTORE-SHA256: MATCH` or ran on a disposable
> export.
>
> **What is affected is reproducibility.** Every count and probe below was measured against a
> worktree byte-identical to `7052a89`; that state no longer exists on disk. Re-running these
> commands today measures the *next* round. Verify against `git archive 7052a89`, not the worktree.
> Consequently probes M10/M11 were run on a pristine export rather than in place — I will not
> mutate files another session is holding open.
>
> Two things for the user, not adjudicated here (R5): whether a FULL should be in flight while its
> subject's modules are being rewritten, and whether authoring a **new** file under
> `ResearchSystem/contract/` — E2 freezes the *existing* files there, so this is arguably outside
> the letter — is meant to happen without a ruling. Neither is a defect in the subject.

---

## 1. What this round is, re-derived

Not taken from the dispatch, which carried the range and nothing else (R2).

| Question | Answer | Where I read it |
|---|---|---|
| Round | **Phase C1.5** — the digest-narrowing round inserted ahead of Phase C2, carried by `.goals/plans/harness-digest-narrowing.plan.md` | that plan's header + Goal; `HARNESS-LEDGER.md` pointer block |
| Governing instructions | `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` (E1–E12 / R1–R9); `v3-harness-review-contract.md` is a stub pointing there | contract stub banner; checklist header |
| Budget position | First review of this candidate → this **is** the FULL. No `v3-review-*-7052a89.md` exists; the three commits are plan, plan revision, candidate — all pre-FULL, so none consumed repair budget. One user-approved fix + one targeted VERIFY remain (E9) | `ls migration/document-work-assurance-v3/`; `git log` on the range |
| Verdict domain | FULL → `REVIEWED_NO_BLOCKER \| CHANGES_REQUIRED \| SPEC_GAP` (R3) | checklist R3 |
| Authorization | Scope approved by the user in the 2026-07-29 planning session (plan §Steps, all committed). Three rulings recorded for attribution: the **E2 explicit override**, the **E10 opening cold-read waive** (in-rule clause, correctly distinguished from C0's override), and the protected-set membership (5 fields / 3 file classes, HarnessIssue excluded) | plan §"⚠ E2 冲突" + §裁决链; `HARNESS-LEDGER.md` 2026-07-29 entries |
| Obligations | narrow digests to `DIGEST_PROTECTED_FIELDS`; stop writing them on every path the round reaches; keep a present digest checked everywhere; zero schema bytes; frozen surface intact; five suites green + `repo-audit` exit 0; a mutation probe per new guard; disclose four honest boundaries in the commit body | plan §Constraints, §Acceptance, §Notes |

**Ceiling (R7).** The user's approvals, the E10 waive and the E2 override were issued in chat; I see
only their committed *records* (plan §"⚠ E2 冲突", `HARNESS-LEDGER.md`, the commit body). I take
those at face value and state the ceiling. The **E11 preview card** is chat-only and therefore
`UNVERIFIABLE` — not folded into supported (R4). "Fresh context" is marked, not verified.

**Read coverage (R4).**

- *Read in full:* the complete diff of all 13 changed paths; `harness-digest-narrowing.plan.md`;
  `CONSTRUCTION-CHECKLIST.md`; `HARNESS-LEDGER.md`'s pointer block and all 2026-07-29 rulings; the
  post-change bodies of `pointer`/`pointer_to`/`pointer_for`/`resume`/`check_state` in
  `assurance_state.py`, `_resolve_pointer` and `read_control_plane` in `review_subject.py`,
  `_write_evidence` and its two call sites in `checks.py`; `common.schema.json`'s three ref
  definitions; supersession-1 §3 in place; `document-harness/REVIEW.md`.
- *Ran myself, pasted below:* all five suites; `repo-audit.py`; **eleven** mutation probes; the
  three signed-blob resolutions; four frozen-path `git diff` sweeps; a resume against a committed
  run state; a scripted audit of all 8 committed `state.json` files; greps for `pointer_to`
  call sites, `digest_sha256` readers, live docs asserting the old convention, and any documented
  N1 issue-code table.
- *Sampled / not re-reviewed:* the pre-existing bodies of `test_candidate_checks.py`,
  `test_spec_plan_state.py` and `test_review_v2_subject.py` outside the added lines and the one
  changed line; the `digestRef` comparison sites in `instruction.py` / `review.py` / `summary.py`,
  which the round explicitly did not touch — I read enough of each to confirm it is a `digestRef`
  (digest required by schema), not a narrowed `pointerRef`.
- *Not probed:* nothing in the subject. Two probes (M10/M11) ran on a `git archive` export rather
  than in place, for the reason in the box above.

---

## 2. Implementation (R3 — lead)

### What the change actually is

**Policy, one place.** `assurance_state.DIGEST_PROTECTED_FIELDS` is a five-name frozenset
(`work_spec_ref`, the three decision refs, `review_ref`) and `pointer_for(field, path, repo_root)`
is the single helper that consults it. The criterion is permission, not value, and the module
comment states it as such. I verified the criterion is applied consistently: the five are exactly
the fields whose current version the executor is not entitled to author, and the eight excluded
ones are files the executor legitimately produces.

**Read side, two gates, same frozenset — and both keep the STALE branch unconditional.** This is
the load-bearing distinction and the code holds it. In `review_subject._resolve_pointer` the
`UNVERIFIED` issue moved inside `if field in DIGEST_PROTECTED_FIELDS:` while the mismatch check
stayed on the `elif`, so it still runs for every field; `assurance_state.resume` has the same shape.
Read from the committed object, not the worktree:

```
$ git show 7052a89:.../review_subject.py | sed -n '226,248p'
    expected = ref.get("digest_sha256")
    if not expected:
        if field in DIGEST_PROTECTED_FIELDS:
            issues.append(Issue(f"{CODE}-POINTER-UNVERIFIED", …))
    elif bytes_digest(raw) != expected:
        issues.append(Issue(f"{CODE}-POINTER-STALE", …))
        return None
    return raw
```

The commit's claim — *"the narrowing removed an obligation to write one and never permission to
write one that does not match"* — is exactly what the control flow implements. M10/M11 prove it
binds on protected **and** unprotected fields.

**`resume` reports the issue *and* keeps the pointer in `present_unverified`.** The plan ruled this
under E6 rather than swapping one for the other. The ruling is correct and I did not have to take
it on trust: probe M5 reproduces the rejected shape and takes down the **pre-existing** N1-A10 test
alongside the new one — the recorded property really would have been deleted.

**Write side.** `checks._write_evidence` returns `{"path": rel}`; the four unprotected
`pointer_to` calls in `run_evidence_v2.py` and the one protected call in `run_bind_v2.py` become
`pointer_for`. `bytes_digest` remains imported in `checks.py` and is still used at line 176 for the
`subjects[]` digest — a different binding, correctly left alone.

**The existence fault survives the narrowing.** `pointer_for` keeps the write-time
`AssuranceFault` on *every* field, not just protected ones, because the unprotected branch never
reads the file and would otherwise have dropped it silently. This is the round's one self-ruled
deviation from the approved plan (Step 2 said "`pointer(path)` verbatim"), it is flagged in the
commit body for exactly this review, and **I endorse it**: taking the plan literally would have
deleted a committed, tested property to make a new rule pass, which is the same E6 anti-pattern the
Step 4 ruling refused. Probe M6 shows the guard catches its removal.

### Mutation probes — eleven, all mine, all value-level

M1–M9 ran in the worktree: neuter with an exactly-once string replacement → observe a value-level
failure → restore from a scratchpad copy and re-verify sha256. `git checkout --` was not used; every
restore printed `RESTORE-SHA256: MATCH`. M10/M11 ran on a `git archive 7052a89` export (see box).
Seven correspond to the round's own eight probes; **M5, M9, M10 and M11 are additional**, and the
round's P3 (STALE) I re-derived as M10/M11 rather than reproducing its exact form.

| # | Neutered | Guard that went red | Pasted failure |
|---|---|---|---|
| M1 | `review_subject` gate → unconditional (the pre-narrowing behaviour) | `test_an_unprotected_pointer_without_a_digest_is_reported_as_nothing_at_all` | `AssertionError: False is not true : V3-SUBJECT-POINTER-UNVERIFIED coverage_ref — pointer carries no digest, so the bytes at runs/run-one/evidence/coverage.json were NOT verified against what the state bound` |
| M2 | `review_subject` gate → never fires | `test_state_pointer_family` | `AssertionError: 'V3-SUBJECT-POINTER-UNVERIFIED' not found in []` |
| M3 | `resume` gate → never fires | `test_a_protected_pointer_without_a_digest_is_an_issue_and_still_unverified` | `AssertionError: True is not false` |
| M4 | `resume` gate → unconditional | `test_an_unprotected_pointer_without_a_digest_is_unverified_but_not_an_issue` | `AssertionError: False is not true : V3-STATE-POINTER-UNVERIFIED resolved_plan_ref — pointer carries no digest, so the bytes at docs/plan.json were NOT bound` |
| **M5** | `resume` reports the issue **instead of** keeping `present_unverified` (the E6 shape the plan rejected) | **two** tests, one of them pre-existing: `test_a_protected_pointer_without_a_digest_is_an_issue_and_still_unverified` + `test_n1_a10_pointer_without_a_digest_is_never_reported_as_verified` | `AssertionError: 'work_spec_ref' not found in {}` |
| M6 | `pointer_for` existence check deleted from the unprotected branch | `test_pointer_for_keeps_the_write_time_existence_fault_on_every_field` | `AssertionError: AssuranceFault not raised` |
| M7 | `pointer_for` → digest on every field | `test_pointer_for_writes_a_digest_on_exactly_the_protected_fields` | `AssertionError: {'path': 'doc.json', 'digest_sha256': 'fb6a8bcc…'} != {'path': 'doc.json'}` |
| M8 | `_write_evidence` digest restored | `test_written_evidence_is_pointed_at_by_path_alone` + `test_a_result_carrying_that_ref_is_still_schema_valid` | `AssertionError: {…'digest_sha256': '1b94cc54…'} != {'path': 'runs/run-one/evidence/check-command-evidence.out.txt'}` |
| **M9** | `review_ref` quietly dropped from `DIGEST_PROTECTED_FIELDS` | `test_pointer_for_writes_a_digest_on_exactly_the_protected_fields` (both suites run: `1 failed, 475 passed`) | `AssertionError: {'path': 'doc.json'} != {'path': 'doc.json', 'digest_sha256': 'fb6a8bcc…'}` |
| **M10** | `review_subject` STALE branch → `elif False` | `test_a_protected_pointer_with_a_wrong_digest_is_still_stale` **and** `test_state_pointer_family` | `AssertionError: 'V3-SUBJECT-POINTER-STALE' not found in []` |
| **M11** | `resume` STALE branch → `if False` | `test_n1_a10_changed_pointer_bytes_reports_pointer_stale_and_is_not_followed` | `AssertionError: True is not false` |

M10 is the one that matters most for the round's central promise, because it goes red on a
**protected** field (`work_spec_ref`) and an **unprotected** one (`coverage_ref`) simultaneously —
the surviving digest check really is field-independent, not a protected-only leftover.

M9 is worth naming separately: the frozenset's *membership* has exactly one guard, the `pointer_for`
policy test. That is sufficient because the two read-side gates consult the same object, but it does
mean a single test file carries the whole protected set. Not a defect; stated so the reliance is
visible.

### E5 — expectation independence: met

`test_pointer_for_writes_a_digest_on_exactly_the_protected_fields` types out all five protected and
all eight unprotected field names as literals and explains in its own docstring why importing
`DIGEST_PROTECTED_FIELDS` would defeat the test. Assertions compare whole dicts (`assertEqual` on
`{"path": …}`), never a substring. `test_an_unprotected_pointer_without_a_digest_is_reported_as_nothing_at_all`
asserts `report.ok` — the report as a whole — rather than the absence of one code, and says why. The
digest fixture is computed from the bytes that landed on disk rather than the string handed to
`write_text`, which is the correct call on Windows.

### Independent facts I established, none of them taken from the round

- **No existing evidence regresses.** I scripted all 8 committed `state.json` files: every one
  carries a digest on every protected field it has, so the new `V3-STATE-POINTER-UNVERIFIED` fires
  on none of them and `rsc v3 status` flips for none of them. The disclosed exit-code side effect is
  real but currently unreachable from committed state. (Separately: `resume` on
  `runs/p3-corr/control/state.json` already fails with 13 × `V3-STATE-POINTER-MISSING` because its
  pointers still name `ResearchSystem/generated/document-assurance/…`, a pre-existing consequence of
  the earlier run-home move — not this round's doing, and noted only so a future session does not
  attribute it here.)
- **Zero schema change was genuinely available.** `common.schema.json`'s `pointerRef` requires
  `["path"]` and its description says only *"Lightweight state pointer (V3-D8: pointers, never
  copied evidence)"* — no digest claim to falsify. `assurance-work-state.schema.json` contains no
  digest text at all. The round's "zero schema bytes" is not a boundary dodge; it is what the schema
  actually permits.
- **No live document was left falsified except the frozen one.** Grepping every non-frozen,
  non-historical markdown for the old convention returns only supersession-1 §3 (the E2 subject) and
  `HARNESS-LEDGER-archive.md` (read-only history). `document-harness/REVIEW.md` was already worded
  compatibly. The four documents the round did fix are the right four.
- **The "no in-library write point" claim for the other four `pointerRef` users holds.** I checked
  the one that looked like a counter-example: `review.py:143-159` builds a **`digestRef`** for
  package members, not `executor_summary_ref`, which `freeze_package` copies verbatim from the
  caller. The claim is accurate.
- **The E2 quote is verbatim.** supersession-1 §3, read in place, says *"A state pointer carries the
  **BYTES digest** of the pointed-at file … the documented authoring path is the
  `assurance_state.pointer_to` helper"* — exactly as the plan and commit reproduce it.
- **No documented N1 issue-code table was left incomplete** by adding
  `V3-STATE-POINTER-UNVERIFIED`. The code-reachability sweeps
  (`test_review_v2_subject.py::NamedIssueReachability`, `test_dispatch.py`) cover the N2 layer only;
  `git grep` at the range base confirms the code is genuinely new.

---

## 3. Boundary / process conformance (R3 — run second)

**E3 — figures re-derived, pasted not described.** Measured on a worktree byte-identical to
`7052a89` (see box). Exactly the claimed counts:

```
document_harness            151 passed in 20.52s
document_harness_review     325 passed in 53.22s
harness (run_tests.py)      Ran 39 tests … OK
stage_control               20 run, 0 failure(s), 0 error(s)
tooling/tests/run_tests.py  tests: 29   passed: 29   failed: 0   RESULT: OK
repo-audit.py (repo root)   RESULT: clean (exit 0)   EXIT=0
```

**E2 — frozen surface intact.** All three signed blobs resolve at the subject commit to the recorded
prefixes, and the four frozen-path sweeps are empty:

```
8ad404b12b3242e700d0ad215048dffccada7d9c  .goals/plans/document-work-assurance-harness-v3.plan.md
b2dbdf752d8c155e4c65b14b5f420b880b8184a1  ResearchSystem/contract/Document-Work-Assurance-Contract-v3.md
68031fa2ca31272e31da0d42a9a02189d28fcc21  ResearchSystem/contract/…-supersession-1.md

git diff --name-only e8ca95c..7052a89 -- ResearchSystem/schema/                            → (empty)
                                        -- ResearchSystem/contract/ + both exact oracles   → (empty)
                                        -- ResearchSystem/assurance/runs/ + shadow/        → (empty)
```

**The E2 override is disclosed correctly, and that matters more than the bytes.** The commit body
states the superseded sentence, says the round violates it, says *"E2 offers exactly two in-rule
exits … and NEITHER was taken"*, and names it the third explicit override since 2026-07-28. That is
the disclosure E2 requires of a round that takes neither exit — it does not describe itself as an
exception E2 allows, which is precisely what the plan warned a cold session must not do. The
divergence is also recorded in `pointer_to`'s own docstring, so the code carries it too. Per R5 the
question of whether a third override is acceptable is the user's; I record the shape.

**E8 — git discipline.** Single dense title `V3-PHASE-C1.5-DIGEST-NARROWING-v1`; one paragraph body;
no trailers (`grep -ciE "co-authored|generated with|signed-off"` → `0`); new commits, no amend; the
kind is named in the first sentence ("Candidate for Phase C1.5"). The 13 changed paths sit entirely
inside the declared boundary — three library modules, three run-v2 template files, three test files,
and four trackers.

**E9 — budget.** Correctly self-classified: no independent FULL had occurred, so plan, revision and
candidate consumed nothing. My FULL is the round's one FULL; one fix and one VERIFY remain.

**E10 — instruction layer.** The subject touches zero instruction-layer bytes and zero schema bytes.
The opening cold-read waive is therefore the within-rule clause E10 provides, and the ledger
explicitly distinguishes it from C0's amendment-read *override* — the distinction is drawn
correctly, not blurred.

**E12 — range.** Base written `e8ca95c`, tip `HEAD`. I confirmed `7052a89` is branch HEAD with no
commits after it, so the resolved tip drops no records.

**E1 — independence.** This review set its own questions, re-derived every figure, and ran its own
probes. No executor figure was accepted as an input. The planning-stage self-check agent's output
(6 must-fix / 9 low, plan §修订记录) carries no verdict words and consumed no review budget —
correct under E1.

**Tracker diffs.** All four are disclosed housekeeping: checkbox flips, the resume-pointer move, the
three 2026-07-29 rulings, and the parent plan's Step 6 warning that M6/M7's defect-table wording
("add a path+digest cross-check") is obsolete after this round. That warning is the right call and
is stated in both the parent plan and the ledger. No load-bearing change is smuggled in.

---

## 4. Findings (non-blocking; not inflated — R3)

**F-1 — `assurance_state.py`'s module docstring states the write policy as if it were a property of
the state document, and is false of every state file in this repository.** Lines 14–17 read *"Only
`DIGEST_PROTECTED_FIELDS` carry a digest to check (2026-07-29). The rest resolve by existence and
are reported as unverified."* All 8 committed states carry digests on all 8 unprotected fields, and
`resume` verifies those into `verified`, not `present_unverified` — as the round's own honest
boundary #4 concedes, since `pointer(path, digest)` stays open for hand-written runs. The
immediately preceding sentence ("re-verifies every digest a pointer carries") is correct, and
`_resolve_pointer`'s docstring says it correctly too, so the accurate fact is recoverable from
adjacent text and no actor's action changes — **wording-level under R9, bankable, no round.**
Minimum fix, when a batch next touches this layer: *"Only `DIGEST_PROTECTED_FIELDS` are **written**
with a digest; a digest that is present is checked on every field."*

**F-2 — "two pre-existing tests were repaired in the same round" is a count no command supports.**
`git diff --numstat` over `tests/` gives `61/0`, `69/0`, `75/1` — a single deleted line across all
three files, and exactly one modified test method (`test_state_pointer_family`'s mutation moving to
`work_spec_ref`). The other two tests the plan predicted would break were kept green by *placement*
(`test_every_declared_code_is_asserted_by_name_in_this_suite`) and by the Step 4 ruling
(`test_n1_a10_…`) — neither was repaired. E3 asks counts to come from the command that produces
them; this one does not. Non-blocking: the diff is authoritative and recoverable.

**F-3 — "A pure subtraction" is contradicted by the same paragraph that makes it.** The round adds a
frozenset, a helper, a new issue code, and a new non-zero exit path for `rsc v3 status`. Every one
of those additions *is* disclosed, in that same paragraph — it is only the summary characterization
that is unearned, and E3 targets exactly the characterization no command established. The narrowing
is a net subtraction of *behaviour*; it is not a pure subtraction of code.

**F-4 — the five `pointer_for` call sites in the run-v2 templates are exercised by no test
(observation, disclosed).** `test_run_v2_template_fulfillment.py` binds `run_evidence_v2.py` as a
module but only reaches its fulfillment helpers; `main()`, where the four calls live, never runs.
A regression there to `pointer_to`/`pointer` fires nothing. The plan states this limit
("'仍带 digest' 这条只能靠 `pointer_for` 的单测证明"), and the read-side gates are a real backstop for
the protected case — a `review_ref` regressed to path-only *would* be caught at resume/dispatch.
I confirmed the gap independently rather than accept it; adding a template guard would be new
machinery (E6) and is the user's call (R5), not a defect.

**F-5 — `pointer_for` duplicates the field identity, and nothing cross-checks the two copies
(observation).** Each call now names the field twice: once as the string argument, once as the
`advance()` keyword. `pointer_for("review_ref", …)` assigned to `coverage_ref=` — or a typo'd
literal — silently produces the wrong policy for that field. The failure is contained: a protected
field degraded to path-only is caught by the very gate this round added, and an unprotected field
given a digest is still checked. So the new API made a previously-impossible mismatch possible while
simultaneously making it detectable. Recorded because the containment is a consequence, not a
design statement, and it is worth knowing that is what holds it.

---

## 5. Verdict

`REVIEWED_NO_BLOCKER`.

The narrowing is implemented as described: one frozenset, one helper, two read-side gates keyed off
it, the STALE check deliberately left unconditional, and the write paths the round could reach
stopped. Eleven independent mutation probes — including four the round did not run, one of which
reproduces the E6 shape the plan rejected and takes a pre-existing test down with it — all failed at
value level, so every guard binds. The frozen surface is intact, the counts reproduce exactly, the
schema really did permit a zero-byte change, no live document was left falsified, and the E2
override is disclosed as a violation rather than laundered into an exception.

The five findings are non-blocking. F-1 is a wording-level docstring inaccuracy that R9 banks rather
than rounds; F-2 and F-3 are record-accuracy items in the commit narrative that the diff itself
corrects; F-4 and F-5 are coverage and API shapes I confirmed independently and report under R5
without concluding. None of them names a place where the code fails to do what it claims, and none
should burn the round's single repair.

Per E9, `REVIEWED_NO_BLOCKER` returns the plan to Step 6 · Phase C2 — where, as this round's own
trackers warn, M6/M7's defect-table wording must be re-decided with the user before the round opens.

**One thing needs the user before that, though:** the box at the top. A later round was being
written into this worktree while this FULL was outstanding, touching `assurance_state.py`,
`review_subject.py` and a new file under the frozen contract directory. This verdict covers the
committed range `e8ca95c..7052a89` and nothing on disk after `04:17:31`.

---

*Record written by the independent review session in the worktree (R6); the execution side commits
it, title `V3-REVIEW-RECORD-PHASE-C1.5-7052a89-v1`. Reproduce any figure here against
`git archive 7052a89`, never against the current worktree.*
