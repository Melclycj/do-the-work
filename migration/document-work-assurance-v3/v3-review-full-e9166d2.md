# FULL review — `e9166d287c0db8ed611ada6efa2f3be87deaacb5` (batch B, round R1)

**Verdict: `CHANGES_REQUIRED`.** 2 blockers, 4 lows, 5 observations.

The implementation is right. `run_all` is wired at the one product call site `HD-25` names, the
order comes from the plan, the `SpecGap` is routed into the script's existing STOP contract, and
the `.get` form is the correct reading of a schema field that is genuinely OPTIONAL — I verified
each of those against the code and the schema rather than against the commit's account of them.
Six of the eight new tests bind their properties under mutations I wrote myself.

What fails is narrower and exact: **the one test written for the defect class this round
discovered cannot fail for that defect** — I applied the subscript form the round says it wrote
first, and `test_no_order_means_no_check_runs` passed. And the reason it slipped is measurable:
**the recorded mutation evidence does not describe the delivered artifact.** The restore digest
`a59cc546…` matches no digest of the delivered file under any of eight constructions I tried,
and the recorded `M1` kill count (6 of 7) is arithmetically the count for a **seven**-test suite
— the delivered suite has eight. The mutations were run before the eighth test existed, so the
eighth was never mutation-tested, which is exactly the state `E4` exists to prevent.

Both close in one repair leg; the fix to the test is one line, and I verified it reddens under
the defect and stays green on the delivered bytes.

## 1. Subject, re-derived (`R2`)

Handed one range and nothing else. Round, budget, authorization, obligations and every number
below are re-derived here; nothing is taken from the dispatch prompt, the ledger, the plan, or
the commit body.

```
$ git rev-parse HEAD              -> e9166d287c0db8ed611ada6efa2f3be87deaacb5
$ git status --porcelain          -> (empty)
$ git log --format=%H%n%P 2f8c48f..e9166d2
  e9166d287c0db8ed611ada6efa2f3be87deaacb5   parent 2f8c48fd7705cbf1c70950e2e95f8a8f05775358
$ cat .harness/review-pending.json
  {"subject": "2f8c48fd…..e9166d28…", "dispatched_at": "2026-08-11T15:28:54+00:00"}
```

HEAD equals the range tip and the tree is clean, so worktree reads are reads of the subject
bytes. Dispatch (15:28:54Z = 01:28:54+10:00) post-dates the tip commit (01:27:37+10:00) by 77
seconds and the branch has taken no commit since — this record is the first it admits (`E9`).

One commit, three paths, classified by hand:

| path | status | class |
|---|---|---|
| `ResearchSystem/assurance/templates/run-v2/run_evidence_v2.py` | M | work product (the cut `HD-25` authorizes) |
| `ResearchSystem/tooling/tests/document_harness_review/test_run_v2_template_check_order.py` | A | work product (the guard) |
| `.goals/plans/harness-batch-b.plan.md` | M | bookkeeping — see `L-3` |

**Round and budget.** `HARNESS-DECISIONS.md` `§live` `HD-25` (2026-08-11, standing, live "待批 B
R1 执行") is the authorization; `.goals/plans/harness-batch-b.plan.md` §R1 steps 4–7 are the
obligations and §Acceptance the test. No `v3-review-*-e9166d2*` record exists, so no valid
independent FULL has occurred for this round: by `E9` this is the FULL, and one user-approved
fix plus one targeted VERIFY remain.

**Frozen and instruction surfaces.** `git ls-tree -r e9166d2 ResearchSystem/schema/document-assurance-v3/`
returns exactly fifteen files, as `E2`'s 2026-08-03 re-baseline states; none is in the diff, nor
is any contract blob. The nine `E10` members are likewise untouched, and I re-derived their
blobs at the subject rather than accepting the plan's claim — all nine equal the ids recorded in
`v3-checkpoint-read-3f19561.md` §1, so the citation route the plan takes for the opening cold
read holds:

```
44d622b9 CONSTRUCTION-CHECKLIST.md   dab9f71a README.md      8bbd330f EXECUTION.md
3350bfac REVIEW.md                   17ff31bb operating-contract stub
52a97a48 review-contract stub        68031fa2 supersession-1  e1a2f26b supersession-2
09aa8699 paragraph-map.schema.json
```

Blobs 7 and 8 equal `E2`'s frozen ids, as they must.

## 2. What I read, and how (`R4`)

**In full:** `CONSTRUCTION-CHECKLIST.md` (standing instructions, plus the stub that names it);
the subject's three diffs and the full post-image of the template and the new suite;
`HARNESS-DECISIONS.md`; `HARNESS-LEDGER.md`; `HARNESS-RIDERS.md`; `harness-batch-b.plan.md`;
`checks.py` `run_check` / `run_all` / `_wrong_subject`.
**Sampled:** `review_subject.py` `check_subject`'s completeness block (:425-470);
`resolved-assurance-plan.schema.json`; `v3-checkpoint-read-3f19561.md` §1;
`test_run_v2_template_fulfillment.py`'s `deriv-bind` class; the run-v2 template directory and
the eight run directories.
**Probed only:** the six `assurance/shadow/**` scripts (grep for call sites, not read).
**Not verifiable from the repository (`R7`):** the `E11` preview card is chat-only. The commit
discloses one narrowing against it (partial results not written); I can check that the delivered
code does not write them, not that the card said it would. `E3`'s "no `git checkout --`" and
"fresh context" are process claims — marked, not verified (`R4`).

## 3. Does the implementation do what it claims

Every claim below I checked against the code or the schema, not against the commit body.

- **`run_all` is the engine, plan order is the order.** `checks.py:452-475` takes
  `(checks: Mapping[str, …], order: Sequence[str], ctx)`; the template builds the mapping keyed
  by `check_id` and passes `plan.get("check_order", [])`. Both stop paths in `run_all` raise
  `SpecGap` — `-MISSING-REQUEST` for an ordered id the mapping lacks, `-SPEC-GAP` after appending
  an uninterpretable result — and the template catches exactly that type, prints the refusal and
  returns 1 without committing or advancing state. **Holds.**
- **`check_order` is OPTIONAL, so `.get` is required, not defensive.** The schema's `required`
  list is `[plan_id, work_id, work_spec_ref, resolver_version, effective_change_boundary,
  repair_cap]`; `check_order` carries `minItems: 1` and the description "Absent when the run has
  no deterministic checks". Absent, not empty, is the legal way to say zero checks, and the
  `.get` default reproduces that. **Holds**, and it is the same reading `check_subject` takes —
  `plane.plan.get("check_order", [])` at `review_subject.py:437`, so the template's "the two
  agree by reading one place" is true of the code, not just of the comment.
- **Fail-closed on a malformed request.** A document with no `check_id` keys `None`, which no
  order entry names, and the entry that wanted it takes `-MISSING-REQUEST`. **Holds.**
- **The eight closed runs are untouched and do not inherit.** No path under
  `assurance/runs/` is in the diff, and all eight run directories carry their own
  `run_evidence_v2.py` copy — I listed them. **Holds** (acceptance criterion 3).
- **Battery.** Every figure re-run by me, immediately before writing this, on the subject tree:
  `tests/run_tests.py` **29 passed** · `pytest -q` at `ResearchSystem/tooling` **705 passed in
  113.80s** · `tests/harness/run_tests.py` **39, OK** · `tests/stage_control/run_tests.py` **20,
  OK** · `rsc.py compile --check` **exit 0, live 173, tombstone 0**. All five match the commit.
  Six legs for a tooling-touching change is the right tier, and the round correctly declined to
  amend `EXECUTION.md`'s four-leg enumeration sentence (that is a rule change; it would open a
  design round). The new file is picked up by `discover(pattern="test_*.py")` in the directory
  runner as well as by pytest, so the guard is registered in both legs.

## 4. Guard binding — my own mutations (`R8`)

Applied to the worktree, one at a time, each restored from a sha256-checked scratchpad copy
(`ae3f6c78…`), never `git checkout --`; `git status --porcelain` empty after each.

| # | mutation | result |
|---|---|---|
| M-A | the exact pre-change shape (`run_check` per file over `sorted(glob(...))`) | **8 failed** |
| M-A2 | order source only, engine and stop kept (`sorted(requests)`) | **7 failed, 1 passed** |
| M-B | plan order kept, immediate stop removed (per-id `run_check` loop) | **4 failed, 4 passed** — exactly the stop family |
| M-C | engine and order kept, the `except SpecGap` routing removed | **4 failed, 4 passed** — the catch is load-bearing |
| M-D | `plan["check_order"]` — the defect this round found | **new suite 8/8 green**; the sibling fulfillment suite reddens 2 |

M-B reproduces the round's `M2` exactly, including that
`test_a_request_the_plan_orders_but_the_control_root_lacks_is_refused` reddens by `KeyError` —
the round's own `R8` disclosure of that is accurate. M-C is mine and the round did not run it;
the STOP routing binds.

M-A2 is the round's `M1`, and it kills **7 of 8**, not 6 of 7. The survivor is
`test_the_refusal_names_the_uninterpretable_request`. Remove the eighth test from my run and the
count is exactly 6 of 7 — see `B-2`.

## 5. Blockers

### `B-1` — the guard for this round's own defect class cannot fail for it

**Location:** `ResearchSystem/tooling/tests/document_harness_review/test_run_v2_template_check_order.py:206-212`,
`APlanWithNoCheckOrderRunsNoChecksAndDoesNotCrash::test_no_order_means_no_check_runs`.

**Ground truth:** `E4` — never trust a guard you have not seen fail. The class exists, by its own
docstring and the plan's step 5, to hold the line against `plan["check_order"]` crashing a run
the schema calls legal. It asserts `seen == []` and the absence of the gap refusal. `drive()`
collapses every exception into `code = None` (`:141-142`), and a crash at the subscript produces
`seen == []` and no refusal line — so both assertions are satisfied *by the defect*. Measured:
with `plan.get("check_order", [])` replaced by `plan["check_order"]`, this test **passes**.

**Failure scenario:** the regression is caught today only by
`test_run_v2_template_fulfillment.py::TheEvidenceStepDerivesRepoRootAndControlRootFromRunDir`,
whose subject is rider `deriv-bind` (REPO / CONTROL_ROOT derivation) and whose fixture plan omits
`check_order` incidentally — its failure message names a derivation that never ran, not an
optional field. Give that fixture a `check_order` for any unrelated reason and the defect class
loses every guard silently, with the class named for it still green.

**Minimum fix (verified):** add one whole-line assertion on a hand-written literal (`E5`) —

```python
self.assertIn("deterministic checks : 0/0 PASS", output.splitlines(), output)
```

That line is printed only after the loop returns. I ran it both ways: green on the delivered
bytes, `AssertionError: 'deterministic checks : 0/0 PASS' not found in []` under the subscript
form. (`assertEqual(code, 1)` would also bind, but only because this fixture's synthetic record
is schema-invalid — incidental, and it would go green again if the fixture were ever repaired.)

### `B-2` — the recorded mutation evidence does not describe the delivered artifact

**Location:** commit body of `e9166d2` ("both restored from sha256-checked scratchpad copies …
the file hashing back to `a59cc546` after each: **M1** … kills 6 of 7"), and the same text at
`.goals/plans/harness-batch-b.plan.md:69-76`.

**Ground truth:** `E3` — measure last; a figure is invalidated by any later change to what it
measures, and digests are emitted by the command that produces them.

**Measured.** `a59cc546…` matches none of these:

```
ae3f6c78…  delivered template, sha256 (bytes on disk, LF)
a5504c97…  delivered template, sha256 with CRLF
e43cfa33…  delivered template, git blob (== HEAD, == --no-filters)
414d21ac…  delivered template, md5
51bbed32… / 14e4095f…   the subscript variant, sha256 LF / CRLF
1df40f04… / 1c277774… / b80fedc9…   the new test file, sha256 / blob / md5
```

**Failure scenario, and it already happened.** The kill count fixes the timing independently of
the digest: `M1` on the delivered eight-test suite kills 7 (measured above), and the single test
whose removal turns 7-of-8 into 6-of-7 is `test_no_order_means_no_check_runs` — the test added
after, when step 5 hit the schema fact. So the mutation battery ran against a template and a
suite that no longer exist, and the eighth guard was never mutation-tested. `B-1` is what that
gap contained. Left as is, the round's central `E4` evidence certifies bytes nobody shipped, and
a reader trusting it re-derives nothing.

**Minimum fix:** re-run both mutations against the delivered bytes, add one for the third class
(the subscript form), and record the digest the command actually prints. `E8` forbids amending,
so the corrected evidence belongs in the repair commit's body and this round's record — not in a
rewritten `e9166d2`.

## 6. Lows

- **`L-1` — the plan's status and resume pointer are stale in the same commit that completes its
  steps.** `.goals/plans/harness-batch-b.plan.md:6` still reads `status: DRAFT — 等用户过预览卡`
  and `:144-145` still reads `当前指针: DRAFT，等预览卡确认 … 下一步 = R0 第 1 步建三条 HD 条目`,
  while steps 1–7 are `[x]` in this very commit. Not wording-level under `R9`: the file's stated
  purpose is cold resume, so the decision that goes wrong is concrete — a fresh session resuming
  R2 (which is gated on R1 landing, so it is next) reads the plan as unapproved and re-opens R0.
  Bytes are supplied: status → `IN PROGRESS — R0 + R1 landed (e9166d2), R2 next`; pointer → the
  same fact plus `下一步 = R2 第 8 步`. Deadline: the next session that resumes this plan.
- **`L-2` — rider `RA` now states a false fact.** `HARNESS-RIDERS.md:13` reads "`run_all` 全仓零
  调用者"; after this commit `run_all` has one caller. The row is what the R2 / I-O-design batch
  will read to scope itself, and its redeem-when ("I/O design 批一起议") is still right — only the
  *what* column is wrong. Bytes: say one caller (the run-v2 evidence template, `HD-25`) and that
  the CLI half is what remains. Under the 2026-08-04 ruling this is riders-only and does not
  consume the fix leg. Deadline: R2's opening.
- **`L-3` — rider `tier-scope` ①'s deadline fired here and the row records nothing.** Its own
  deadline is "下一个 tooling-touching 批按枚举句自选电池腿的那一刻" — this batch. The round did
  the right thing (six legs, no `EXECUTION.md` edit) and said so in the commit, but the bank row
  is unchanged, so the next tooling-touching batch meets the identical row and identical deadline
  with no trace that it already bit once and was survived only because the executor knew. Bytes:
  append the fired-and-deferred fact to the redeem-when column, or take the user's ruling on the
  design round the plan's §待用户裁 item 2 asks for. Riders-only.
- **`L-4` — the commit carries a path outside the round's declared revert unit, undisclosed.**
  The plan declares R1's revert unit as `assurance/templates/run-v2/` plus its suite under
  `tooling/tests/document_harness_review/`, "一个 commit"; the commit also carries the plan file.
  Reverting the round now also reverts step bookkeeping. The A2 precedent separates them —
  `de8f4ef` (fix) carries no plan, `4e80c17` (closeout) carries it. `E8` asks the round to stay
  inside its declared boundary; if the preview card widened it, that is chat-only and I cannot
  see it (`R7`), which is itself the ceiling on this finding.

## 7. Observations

- **`O-1`** `run_all`'s docstring (`checks.py:458-465`) justifies producing the `SPEC_GAP` result
  before raising because "the evidence that the request was uninterpretable is itself worth
  keeping (plan §8)" — but it raises with `results` local, so no caller can keep it. This round is
  the first caller to meet that contract, and the commit's disclosure treats the loss as its own
  narrowing under `E6`. The narrowing is sound; what the round inherited is a docstring in
  `checks.py` whose stated reason its only caller cannot serve. Outside the template-only cut.
- **`O-2`** The pre-`run_all` shape survives in six `assurance/shadow/**` scripts and in the eight
  run-local copies. `HD-25` scopes the cut to the template, so this is authorized, not a defect —
  but `E7`'s "test the defect class" is discharged only within that cut, and the class is not
  repo-wide closed.
- **`O-3`** Two `check-chk-*.json` files declaring the same `check_id` now collapse silently
  (dict last-wins) where the old shape ran both. It needs a malformed control root and
  `uniqueItems` keeps the plan from ordering the id twice, so nothing today reaches it; no guard
  exists either.
- **`O-4`** `requests: dict[str, Any]` is annotated `str` while `document.get("check_id")` can key
  `None` — the comment two lines above explains why `None` is the fail-closed outcome, so this is
  an inaccurate annotation, not a hazard.
- **`O-5` (wording-level, `R9` — named here, spawning nothing)** The commit says "Three test
  classes, eight tests". The file has four test-bearing classes; three, if the negative control is
  excluded, which the sentence does not say. No actor's action changes and the count is one
  `--collect-only` away, so it rides the record and no more. I raise it only because the same
  sentence is where `B-2`'s stale counts live.

## 8. Record and boundary conformance (`R3`, run second)

`E8`: single commit, title `V3-B-R1-v1` matching `V3-<ROUND>-v1`, kind named in the first clause
("Construction commit (batch B, round R1)"), one dense paragraph, no trailers, no push (subject
tip is HEAD). Boundary: see `L-4`. `E2` and `E10` surfaces untouched, verified above. `E12`: the
handoff was one range; base written, tip at HEAD.

Out of subject but disclosed by the round, and confirmed here for the record: `2f8c48f`'s title
is literally `@ V3-B-R0-RULINGS-v1`, with a stray `@` line at both ends of the message — a
PowerShell here-string leaking into a POSIX shell. Its content is intact. It is outside the range
I was handed, and `E8` forbids amending, so it stands as an errata question for the user, not a
finding of this round.

## 9. Worktree integrity after review

```
$ sha256sum run_evidence_v2.py               -> ae3f6c789dd4b4c5e5e72bae76f478d2262f39713507b872ad60ab50afe3f393
$ sha256sum test_run_v2_template_check_order.py -> 1df40f040fd5df3d9293007aee34cdc8c3636359e59abb78aa086912d9023146
$ git status --porcelain                     -> (empty)
$ git rev-parse HEAD                         -> e9166d287c0db8ed611ada6efa2f3be87deaacb5
```

Every mutation restored from the checksummed copy; no `git checkout --` was used, and the branch
has taken no commit during this review.
