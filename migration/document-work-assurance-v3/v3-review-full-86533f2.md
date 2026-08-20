# FULL review — `ae4df09d810ad24ea6e76043c94fe75b716f1757..86533f2eafbf8fbf7f06f9d79264a165bf7e44b7`

Independent FULL review of Phase C2 (flow/summary group, defects M5+M6+M7 of
`harness-deletion-first-stabilization`). Verdict at the end; implementation first (`R3`),
process and boundary second. Every figure below was re-derived on this machine; no number
from the journal, the commit bodies or the ledger was accepted as reported (`R2`).

**Verdict: `REVIEWED_NO_BLOCKER`.** 0 blockers, 3 observations, no wording-level findings.
The three bindings do what the commit claims, each was demonstrated to bind by mutation on
this machine, the RED claim reproduces exactly, and the round stayed inside every declared
and permanent boundary.

## 1. Subject, re-derived

Handed one range and nothing else. `git log` over it: two commits —
`853fe4c` (`V3-REVIEW-RECORD-C2-COLD-READ-ae4df09-v1`, adds only
`v3-cold-read-ae4df09.md`, 201 lines) and `86533f2`
(`V3-PHASE-C2-FLOW-SUMMARY-BINDINGS-v1`, the candidate). At session start
`git rev-parse HEAD` = `86533f2…` = the range tip and `git status --porcelain` was empty;
`.harness/review-pending.json` is live with kind `construction-round`, this exact range,
dispatched `2026-07-30T04:30:40+00:00` — 13 s after the candidate's commit timestamp, and
the branch has taken no commit since (`E9`'s window intact; this record is the only commit
it admits).

Changed paths, classified by hand (`git diff --name-only`): two rsclib modules
(`flow.py`, `summary.py`), their two review-side test files
(`test_flow_repair_disposition.py`, `test_fix_round_locks.py`), the round journal
(`document-harness/journal/c2-2026-07-30.md`), and the cold-read record. Exactly the
candidate's declared boundary plus the read's record; nothing else.

Round context re-derived from the repository: the ledger's NEXT pointer named Phase C2 and
obliged an opening cold read (discharging `a6b87ad`'s in-layer read debt) plus a re-ruling
of the M6/M7 shapes with the user; the plan's defect table rows 32–34 carry M5/M6/M7 and
its Step 6 note marks the M6/M7 wording stale post-C1.5. The journal records the three
opening rulings (read=dispatch, M6=option B, M7=confirmed, digest kind canonical); the
rulings are in-repo in journal and commit body, so nothing load-bearing is chat-only (`R2`;
the preview-card interaction itself is a process claim, marked under §6).

## 2. M5 — `flow.check_repair_decision` binds a decline (flow.py)

The `NO_REPAIR` early return that sat before every binding check now sits after two of
them: a new work_id/run_id reconciliation of decision against review (absent side →
`V3-FLOW-REPAIR-BINDING-UNVERIFIED` naming which side and which field; mismatch →
`V3-FLOW-REPAIR-WORK-MISMATCH` / `V3-FLOW-REPAIR-RUN-MISMATCH`) and the pre-existing
candidate binding. The moved return carries `report_of(issues)`, so a decline reports what
it failed to bind instead of bare `schema_report`.

Shape checks that could have silently defeated this, each run against the frozen pack:

- `user-decision.schema.json`: `work_id` required, `run_id` optional — matching the
  code's absent-side UNVERIFIED path exactly.
- Both review shapes carry `work_id`/`run_id` **required at root** — v1
  (`review.schema.json` `$defs/reviewResult`) and v2 (`review.v2.schema.json`), so
  `review.get(field)` reads the same place under both versions. The v2 shape-mismatch
  class this very module recorded at `reviewed_candidate_ref` (candidate_ref moved into
  `subject`) does **not** recur for these two fields, and the v2 decline test
  (`RepairDecisionBindingAcrossResultVersions`) covers the cross-version class per `E7`.

## 3. M6 (option B) — `summary.check_assurance_candidate` content-binds review_refs

On top of the retained count check: canonical digests of the in-hand reviews vs
`review_refs` digests — a review with no binding ref → `V3-ASSURANCE-REVIEW-UNBOUND`, a
ref binding bytes no review has → `V3-ASSURANCE-REVIEW-INVENTED`. The six evidence/spec
refs stay stored-without-content-check with the reason in the comment at the check site,
as the ruling required.

Digest-kind consistency verified end-to-end, because a kind mismatch here would false-flag
every real run: the check compares `canonical_digest(review)`; the authoring precedent
writes the same kind (`runs/w1-r1/run_bind.py:45` `review_digest = canonical_digest(review)`
into `review_refs`); the fixtures' `review_refs_for` uses `result_digest`, which is
`canonical_digest` (`review.py:707-708`). The historical w1-r1 run would pass the new
enforcement.

`entry["digest_sha256"]` cannot KeyError: the check sits after
`validate_n2("assurance_candidate", …)` returns ok, and `review_refs` items are
`common.schema.json#/$defs/digestRef` with `path` + `digest_sha256` **required**.

## 4. M7 — decision binding at generate and at check (summary.py)

`generate_summary` refuses (`SpecGap`, `V3-ASSURANCE-DECISION-BINDING-MISMATCH`) a
`decision_ref` whose `digest_sha256` ≠ `canonical_digest(decision)` — `.get` on the ref
side, so an absent digest refuses rather than crashes. `check_summary` names a
`final_decision_ref` carrying different decision bytes than the decision supplied (same
code, Issue form, after schema validation — `digestRef` again makes the subscript safe).
The authoring precedent (`run_final.py:87-90`) writes `canonical_digest(decision)` — the
enforced kind.

## 5. Tests and evidence, re-derived (`E3`, `R8`)

**GREEN on the committed bytes, this machine:** tests 29/29 OK · stage_control 20 run 0
fail · harness 39 OK · document_harness 169 OK · document_harness_review 338 OK ·
`repo-audit.py` exit 0. All five figures match the commit body's 29 / 20 / 39 / 169 / 338.

**RED reproduced:** with `flow.py` + `summary.py` checked out from `ae4df09` under the
new test files, the full review suite ran 338 with **exactly 10 failures**, and the ten
names match the journal's `^FAIL:` list one-for-one; zero pre-existing failures. The ten
new assertions are the round's authored tests; the renamed
`test_negative_control_a_well_bound_no_repair_reports_nothing` pairs them as the `E4`
negative control.

**Mutation probes, run by me** (sha256-snapshotted to scratchpad, restored by copy, both
files re-hashed to `431f351d…` / `d09439eb…` — which also equal the journal's reference
snapshots — worktree `git status` clean after):

| guard neutered | my result |
|---|---|
| M5: early `NO_REPAIR` return reinserted ahead of the binding checks | 4 red (the 3 NO_REPAIR binding tests, value-level `[] != [(code, location)]`, + the pinned-layer reachability test). Journal's probe reported 3 for its stated targeted scope — both figures are right for their scopes |
| M6: `bound_digests = set(known)` (content check → count-only) | 3 red (both content tests + pinned layer) |
| M7 generate: `if False:` on the comparison | 1 red (`SpecGap not raised`) |
| M7 check: `if False:` on the comparison | 2 red (the citing test, value-level, + pinned layer) |

Each mutation was assertion-red, not crash-red (`R8`). The pinned-layer test
(`EnforcementLayerIsPinned`) extends its **hand-written** expected list with the five new
codes — an `E5`-conformant independent literal — and `EveryNamedCodeIsAssertedSomewhere`
sweeps codes out of module source by regex, so the pair covers both directions
(independence and completeness). Fixture upgrades from junk digests to computed ones were
load-bearing as claimed: the RED run proves the old fixtures now refuse wholesale.

## 6. Process, boundary, record conformance

- **E2:** at the range tip the three frozen blobs sit at their frozen ids
  (`8ad404b1…` plan, `b2dbdf75…` contract, `68031fa2…` supersession-1, each re-derived via
  `ls-tree`/`rev-parse`) and `git diff` over the range for the schema pack and the
  instruction layer returns nothing.
- **E8:** title names the round; kind named ("Candidate"); one dense paragraph, no
  trailers; explicit paths (6 files across two commits, matching the declared boundary);
  no amend (two new commits).
- **E9:** the cold read is a read, not a round — no budget consumed (`R3`); between its
  dispatch (`03:49:24Z`) and its record only the record landed; the candidate followed.
  This FULL is the round's first budget consumption. Timeline re-derived from `%cI`.
- **E12:** one range handed, tip == HEAD verified before anything else.
- **Cold-read record (`853fe4c`), spot-checked rather than re-run:** naming and title
  conform to `R6`; its §1 blob table holds where probed (README `4daab565`, checklist
  `33126c19`, supersession-2 `e1a2f26b`, each re-derived at `ae4df09`); its two cited
  read-record commits exist (`38008a1`, `9ddaff6`); its 0-must-fix outcome and the
  `a6b87ad` debt discharge match the ledger's binding. Its "freeze marker deleted in this
  same act" concerns an untracked worktree file — unverifiable from git, consistent with
  the freeze hook's design and with the candidate landing after it (marked, not verified).
- **Ledger:** untouched by the round, correctly — the pointer moves at closeout, and the
  C0 residual low's test file (`test_run_v2_template_fulfillment.py`) is untouched as
  declared.

## 7. Findings

### Observations (non-blocking; none inflated, `R3`)

**O-1 — generate-side asymmetry: `candidate_ref` is still stored verbatim.**
`generate_summary` now reconciles `decision_ref` against the decision in hand, but
`candidate_ref` — in hand at the same moment, same verbatim-storage shape M7 named for
decision_ref — is stored uncompared. The class is netted: `check_summary`'s pre-existing
`CANDIDATE-BINDING-MISMATCH` catches the mismatch at check time, so the difference is
refuse-at-generate vs report-at-check, not guarded vs unguarded. The defect table named
decision_ref only; recording the residual shape under `E7`'s lens for whatever batch next
touches `generate_summary`.

**O-2 — `V3-FLOW-REPAIR-BINDING-UNVERIFIED` now fires from two sites** (absent
work/run field; absent reviewed commit) with distinct location fields. The pinned expected
set carries the code once — it is a set of codes, and both sites are separately
test-asserted — so nothing is uncovered; noted so the shared code is not later mistaken
for a single check.

**O-3 — component shape (`R5`).** C2 adds three enforcement sites and five codes, closing
the last rows (M5–M7) of the plan's seven-row defect table — plan-enumerated work, not
finding-driven accretion. The ledger already schedules the 保障面二期复盘 after C2 close as
the venue for the accumulation-vs-deletion question; this is a data point for it, no
conclusion here.

### Unverifiable, disclosed (`R4`)

Fresh-context process claims (the cold read's and the executor session's); the untracked
freeze-marker worktree acts; the executor's own probe executions (I reproduced equivalent
probes rather than auditing theirs); the preview-card interaction beyond its recorded
outcomes. Each marked, none folded into supported.

## 8. Coverage disclosure (`R4`)

**Read in full:** the range diff, all six files; `summary.py` (470 lines);
`flow.py:300-500` (the repair section) plus its module docstring and
`reviewed_candidate_ref`; `v3-cold-read-ae4df09.md` (201); the journal (87);
`CONSTRUCTION-CHECKLIST.md` and the review-contract stub (standing instructions);
`HARNESS-LEDGER.md` (75); the three commit messages; `.harness/review-pending.json`.

**Sampled:** the two test files via their diffs plus targeted greps
(`EveryNamedCodeIsAssertedSomewhere` header, fixture helpers) — not the full ~2300 lines;
the plan file via its C2/M5–M7 sections; `review.py:700-740`; `run_bind.py:40-70` and
`run_final.py:80-95`; schema pack via targeted field probes of five schemas
(`user-decision`, `review`, `review.v2`, `assurance`, `common`).

**Probed only:** the five suite runners and `repo-audit.py` (executed, results pasted);
`rsc.py --help`; the pytest cache.

**Ceiling:** whether option B's deliberate non-coverage of the six evidence/spec refs is
the right policy is the user's settled ruling, not re-adjudicated here (`R5`); this review
checked that the code implements the ruling as recorded and says so at the check site.

## Verdict

**`REVIEWED_NO_BLOCKER`** — FULL, Phase C2, subject range
`ae4df09..86533f2`. No fix round is obliged; the three observations carry no rider
motion of their own (O-1/O-2 ride whatever batch next touches their files; O-3 feeds the
scheduled retrospective).
