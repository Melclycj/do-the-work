# Plan: Redeem the five routed HarnessIssues at their sources

- **slug**: harness-issue-redemption-batch
- **created**: 2026-08-07
- **complexity**: 复杂
- **status**: done — round `HI-REDEEM-5` closed and routed 2026-08-07
- **base_commit**: 069c4e949f5aa28b0af74b0257b81862ed8f3d4f
- **base_branch**: document-work-assurance-v3

## Goal (one line)

Port five already-routed HarnessIssue fixes into the run-v2 templates, the README, `repo-audit.py`
and the dispatch marker, through one construction round, so the next product run stops inheriting
three defects that this run paid for.

## Why / value

`p5b-claims` walked into three template defects and spent roughly an hour and a half on them. The
issues are filed and the user routed all five on 2026-08-07, but **routing fixes nothing** — every
source still carries its defect. Two of the three template fixes have already run a full round
inside `p5b-claims`'s own copies, so this batch is mostly *porting verified patches*, not deriving
new ones. Until it lands, any run copying `templates/run-v2/` inherits all three, and the worst of
them fails silently.

## Context to resume cold

**The five issues and their routes** (each pair: the observation, and the user decision that routed
it — read both, they are the authorization):

| # | Issue file | Route |
|---|---|---|
| 1 | `ResearchSystem/assurance/runs/p5b-claims/issues/issue-p5b-claims-repair-step-unnamed-in-readme.json` | `WORKFLOW_FIX` |
| 2 | `ResearchSystem/assurance/runs/p5b-claims/issues/issue-p5b-claims-template-round-field-unwritten.json` | `WORKFLOW_FIX` |
| 3 | `ResearchSystem/assurance/runs/p5b-claims/issues/issue-p5b-claims-bind-round0-no-blocked-branch.json` | `WORKFLOW_FIX` |
| 4 | `ResearchSystem/assurance/runs/p5b-firewall/issues/issue-p5b-firewall-evidence-not-byte-stable.json` | `VERIFIER_FIX` |
| 5 | `ResearchSystem/assurance/runs/p5b-firewall/issues/issue-p5b-firewall-dispatch-types-product-run-as-construction.json` | `WORKFLOW_FIX` (**split — see Constraints**) |

Triage decisions sit beside each issue as `user-decision-triage-<slug>.json`, commit `6078217`.

**The exact sites, and where the verified patch already exists:**

| # | Source to change | Working patch to port from |
|---|---|---|
| 1 | `ResearchSystem/assurance/templates/run-v2/README.md` § *Steps that did not change* + copy a `run_repair.py` into `templates/run-v2/` | `ResearchSystem/assurance/runs/p5b-claims/run_repair.py` (written 2026-08-07, ran clean) |
| 2 | `ResearchSystem/assurance/templates/run-v2/run_evidence_v2.py` — the `assurance_state.advance(...)` call at **line 210** takes `next_action=` but no `repair_round=` | `runs/p5b-claims/run_evidence_v2.py`, same call — one line `repair_round=REPAIR_ROUND,` plus its comment |
| 3 | `ResearchSystem/assurance/templates/run-v2/run_bind_v2.py` — round-0 emit binds an AssuranceCandidate and advances to `AWAITING_FINAL` unconditionally | `runs/p5b-claims/run_bind_v2.py` — the `blocked = REPAIR_ROUND == 0 and operative["verdict"] != "REVIEWED_NO_BLOCKER"` branch |
| 4 | `Thesis/Work/Tooling/repo-audit.py` **line 288**: `print(f"scope: {len(all_md)} markdown files under {ROOT}")` — `ROOT` is an absolute machine-local path | none — new, but one line (render relative to the checkout root) |
| 5 | `ResearchSystem/tooling/rsc.py` **line 404** | none — new, see the correction below |

**Correction to carry (found 2026-08-07 while pinning sites, AFTER the issue text was written).**
Issue 5's statement and the triage rationale both describe the label defect as "one wrong value".
The actual site is `rsc.py:404`:

```python
if args.range:
    kind, subject = "construction-round", f"{derived.base}..{derived.tip}"
```

The kind is derived from **which flag was used**, not from what the run is — `--subject` already
yields `"product-run"` correctly. So the defect is narrower and differently shaped than the issue
says: a range dispatch of a *product* run is mislabelled, because range-ness is being read as
construction-ness. The fix is to derive the kind from the control plane the dispatch already read,
not from `args`. This is slightly more than one value; it is still small. **Do not silently
re-scope — state this correction in the round's instruction so the reviewer sees the issue text and
the site disagree, and can judge whether the route still fits.**

**How a construction round runs in this repo** (the shape, from precedent):

- Round records live at `ResearchSystem/migration/document-work-assurance-v3/v3-review-full-<sha>.md`;
  recent construction rounds: `E2-VERB-E10-PIN` (`c667d08`), `SIMP-ABCD` (`214f743`).
- Review-side conduct is governed by `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md`
  (R1–R10), **not** by `REVIEW.md` (that governs product runs).
- Dispatch is `python -X utf8 ResearchSystem/tooling/rsc.py v3 dispatch --range BASE..TIP`. It writes
  `.harness/review-pending.json`, which freezes the repo until the commit that lands the review
  record deletes it.
- The reviewer is a fresh-context subagent handed the dispatch text and nothing else.

**Governing ruling (this is why the batch cannot just be edited in):** 2026-08-03, recorded in
`ResearchSystem/HARNESS-LEDGER.md` — ledger/bookkeeping batches need no round, but **rule and
template changes go through a round**. These are template and tooling changes.

## Constraints / Out-of-scope

- **This opens a round.** Do not edit the five sources and commit them as a maintenance batch. The
  2026-08-03 ruling is explicit and this session's whole point was that an executor does not get to
  quietly change the rules it runs under.
- **Issue 5 is split and only half is authorized.** The routed half is the run-kind label. What a
  `--range` dispatch should take as its **base** is `DEFER`red to the open I/O design batch — the
  triage rationale says so in writing. Fixing the label must not touch or settle the baseline.
- **Redemption deletes nothing from the issue files.** HarnessIssues are immutable; a fix does not
  amend or close them. (Contrast with riders, where redemption deletes the row in the same commit —
  these are not riders, and three of them were misrouted as riders once already.)
- **Port, do not re-derive** for #2 and #3. The patches ran a full round in `p5b-claims`'s copies;
  rewriting them from scratch throws away the only evidence they work.
- OUT: fixing the range-dispatch baseline (deferred, above).
- OUT: opening P5C. That is a separate user decision and is not implied by this batch.
- OUT: the run-v2 README's own layer question (`run-v2 README 归层`, BATTERY-TIERING O1) — a
  standing open item in the ledger, not this batch's.

## Steps

- [x] 1. Read the five issue files and their five triage decisions. They are the authorization; the
      route on each decides what kind of change is licensed.
- [x] 2. Re-verify each of the five sites still looks as recorded above (line numbers drift). Note
      any that moved — a plan that pins a line is wrong the moment someone edits above it.
      *(2026-08-07: no site moved — `run_evidence_v2.py:210`, `repo-audit.py:288`, `rsc.py:404` all
      exact; `templates/run-v2/` confirmed to carry no `run_repair.py`; the bind round-0 branch is
      absent as recorded. One correction found — see Notes, correction B.)*
- [x] 3. ~~Write the round instruction under a new run/round directory~~ — **superseded, correction C
      below.** A construction round has no instruction directory and no WorkSpec; the reviewer
      receives one range and nothing else (`R2`). What the opening actually owes and what was done:
      the `E11` preview card (rendered 2026-08-07, before any edit; the user resolved its one open
      question — see correction B), and `E10`'s opening cold read of the instruction layer (7 of 9
      members discharge by citing `v3-checkpoint-read-a5a04c3.md` §1; `document-harness/README.md`
      `70bd9f0b` and `EXECUTION.md` `810f5081` drifted since it and were read end to end, 37 + 171
      lines). The corrections travel in the work commit body, which is inside the range.
- [x] 4. ~~Run the pre-freeze duties the run-v2 README names~~ — **superseded, correction C.** That
      gate governs a *product run's* instruction freeze: mechanical reconciliation of the
      enumerations an instruction states, and a dry-run of every bound check argv. This round
      freezes no instruction and binds no checks. Its analogue is `E3` (every figure re-run
      immediately before the claim, output in the commit body), which step 6 discharges.
- [x] 5. Apply the fixes on an isolated branch: port #2 and #3 from `p5b-claims`'s copies, copy
      `run_repair.py` into the template and name it in the README (#1), make `repo-audit.py`'s scope
      line relative (#4), and land #5 as **A + B′ + C** (correction B below). *(landed `b8fea97`,
      11 files, **256+/17−** — corrected from the 167 first written here and in the commit body,
      which was the unstaged subtotal over the ten modified files and omitted the added
      `run_repair.py`'s 89 lines; FULL finding L-2, and this is its one still-editable site. Two E4
      mutations run and restored by sha256; corrections D and E below.)*
- [x] 6. Run the full battery — this touches tooling, so the doc-only tier does not apply:
      `rsc compile --check`, P2/P4/P5A goldens, `pytest -q` in `ResearchSystem/tooling`, repo-audit.
      *(P2 29/29, P4 80/80, P5A 39/39, fixtures 41/41 failures=0, pytest 629 passed 103.76s,
      compile --check fresh + lint clean, repo-audit clean exit 0 — output in `b8fea97`'s body.)*
- [x] 7. Dispatch ONE independent review of the round (`rsc v3 dispatch --range BASE..TIP`) to a
      fresh-context reviewer; ~~let it commit its own record~~ — `R6` gives the record's commit to
      the execution side on the construction track, so the reviewer wrote and this session
      committed. *(FULL `da603da..f4e1be1` → `REVIEWED_NO_BLOCKER`, 0 blocker / 4 low / 4
      observation, record `v3-review-full-f4e1be1.md` landed `ca61820` with the marker deleted.)*
- [x] 8. Triage findings, take the user's decision on any repair, then close the round out.
      *(User 2026-08-07 spent the one fix leg on L-1 + correction E + O-2 and ruled on L-4 that
      `E8`'s "one dense paragraph" buys density, not one literal block — L-4 dissolved, ruling in
      the journal §1. Repair `3b28116`, 3 files 112+/3−, two E4 mutations. Targeted VERIFY
      `ca61820..3b28116` → `REVIEWED_NO_BLOCKER`, 3 low / 4 observation, record landed `f3741e3`.
      Budget now spent in full, so V-1 / V-2 / V-3 banked as riders `sg-print` / `bind-emit2` /
      `cache-count` with their bytes named. L-2's editable site fixed above; L-3 is errata in the
      journal and the record commit body.)*
- [x] 9. Update `ResearchSystem/HARNESS-LEDGER.md`: the shared-file writer replaced the stale batch
      breakpoint with the CLOSED anchor and copied journal §1's `E8` ruling into the ledger after
      the concurrent review window ended. The root router now records that the P5C external
      prerequisite is satisfied.

## Acceptance (done = ?)

- All five sources changed, each traceable to its issue id.
- A fresh copy of `templates/run-v2/` into a new run directory would carry: the `repair_round` line,
  the round-0 blocked branch, and a `run_repair.py` named in the README.
- `repo-audit.py`'s scope line contains no absolute path — two runs over the same tree from different
  checkouts produce byte-identical output.
- The marker carries no `kind` field at all (C); `--subject`'s refusal names the remedy (B′); and
  `repo-audit.py` no longer splits an evidence commit (A). No range **base** default is added —
  there is nothing to derive one from.
- Full battery green, and the greenness is command output in the round record, not a description.
- One independent review round completed with its record committed; the freeze marker is gone.
- The five HarnessIssue files are byte-unchanged (immutable — redemption does not edit them).

## Resume pointer

当前指针: **CLOSED；不要恢复执行。** FULL 与 targeted VERIFY 均为
`REVIEWED_NO_BLOCKER`，`E9` 预算用尽，三条 VERIFY low 已入 rider bank。收轮锚点：
[`hi-redeem-5-2026-08-07.md`](../../ResearchSystem/harness/ResearchSystem/document-harness/journal/hi-redeem-5-2026-08-07.md)
以及本计划；当前 harness 指针回到 `ResearchSystem/HARNESS-LEDGER.md`。

## Notes

**Correction B — issue 5's fix is not the shape this plan assumed (found 2026-08-07, step 2).**
The plan says "derive the kind from the control plane the dispatch already read". There is no
such control plane on the range path: `construction_dispatch_of` (`dispatch.py:531-572`) resolves
two revisions, checks ancestry and non-emptiness, and returns `ConstructionDispatch(base, tip,
report)` — it reads no control plane at all, unlike `dispatch_of`. Worse, the two obvious narrow
substitutes both reproduce the defect **on the very run that produced the issue**:

- `control_root_of(repo, tip)` — p5b-firewall's dispatched tip `fef3a2e` changed exactly one file
  (`ResearchSystem/assurance/runs/p5b-firewall/evidence/chk-repo-audit.out.txt`) and carries no
  path ending in `review_subject.STATE_PATH`, which is *why* `--subject` refused it. Returns
  `NOT-AN-EVIDENCE-COMMIT` → still typed construction.
- the same scan widened over the range — `git log --name-only f2c449a..fef3a2e` contains zero
  state-pointer paths (verified). Still typed construction.

A candidate derivation existed — *a range is `product-run` when every changed path in `base..tip`
lies under one and the same `ResearchSystem/assurance/runs/<run-id>/`* (verified against four real
ranges: `3b7ebe2..838c413`, `8e9b60b..8ec4c60`, `c8d9afa..9dcb783` stay `construction-round`;
`f2c449a..fef3a2e` becomes `product-run`). **It was proposed and then withdrawn**, first as a label
and then as a refusal guard, on the user's push-back 2026-08-07. Teaching the construction door to
recognise a product run is a guard bolted beside the real failure, which was an executor **routing
around a correct refusal**: `--subject` was right to decline `fef3a2e`, and `E6` says a fix needing
new machinery is the signal to re-question the guarded thing. Re-questioned, the defect is that the
refusal states the fact and omits the remedy, so an executor reasonably tries the other door.

**Ruling — the user revoked the DEFER on the range base (2026-08-07) and approved this shape:**

- **A** — `repo-audit.py`'s scope line goes relative (this batch's #4). The root cause: it is what
  split one evidence commit into three and forced the run off `--subject`.
- **B′** — `dispatch.control_root_of`'s `NOT-AN-EVIDENCE-COMMIT` message names the remedy
  (re-stage the run's whole control root, commit, dispatch that commit; a range is the
  construction-round door). One string in an existing Issue, no new code path, no guard.
- **C** — delete the `kind` field from the marker. It drives nothing (`review_freeze_check.py`
  reads it only for the display line `pending.get('kind', '?')`; nothing branches on it) and `R2`
  forbids a reviewer trusting it, so a field that can only ever mislead is removed rather than
  taught.

**The base half is closed with nothing to build.** Three real construction rounds' bases each
bound their round exactly; the one bad base was a product run that should never have been on
`--range`, which A and B′ close. A construction round has no control plane, so a base cannot be
derived without inventing a round-marker artifact — the machinery `E6` refuses. A dispatch-time
"N commits / M files" self-check was drafted and dropped: two of the three correct construction
ranges also changed exactly one file, so the figure does not discriminate.

**Correction D — issue 2's own statement overstates its mechanism.** The issue says the evidence
template "never writes `repair_round` into the state itself", so a repaired run dispatches a
round-1 subject under a FULL role. Read against the code that is not the whole story:
`assurance_state.advance` merges (`updated = dict(state)`) rather than rebuilding, and
`flow.advance_checked` sets `updated["repair_round"] = 1` on entering REPAIRING (`flow.py:306`),
so on the ordered path the field is already 1 and the merge preserves it — the ported line is
redundant there. What it buys is that the round the pass *ran under* becomes authoritative for the
state field instead of the state depending on the REPAIRING transition having happened. p5b-claims
skipped exactly that transition — which is issue 1 of this same batch. So 1 and 2 are two sides of
one incident, and the issue text attributes to the template a staleness the skipped step produced.
The fix is still worth porting; the claim behind it is narrower than written. No regression guard
was added, deliberately: pinning it means driving `run_evidence_v2.main()` (git commits + a check
run) to hold a line that is redundant whenever the preceding step was taken, and issue 1 closes the
skip at its source — `E6`'s question answers itself.

**Correction E — a second byte-stability cause, found while proving #4's acceptance, NOT fixed
here.** The two-checkout comparison first returned 475 vs 471 markdown files. The cause was not the
scope line: four README files under pytest's `.pytest_cache` directories — gitignored, untracked,
and created by **this session's own battery**. `repo-audit.py` enumerates with `ROOT.rglob('*.md')`
and its `EXCLUDE` set does not name `.pytest_cache`, so *running the tests changes the audit's own
output by four*. With
those caches removed the two checkouts produce byte-identical output (sha256
`a92940f3d23c8472f21f0df8a36784653bebee7e9889edbd101e740a411ae07c` from both paths), so #4's
acceptance holds as measured. This is the same *family* as #4 — evidence differing for reasons
unrelated to the candidate — but a different cause, outside the routed fix, and a one-word change
to a set literal is still a change nobody authorized. Left for the user to route at closeout.

**Correction C — plan steps 3 and 4 describe a product run, not a construction round.** Step 3 asks
for an enumerated instruction under a run directory; a construction round has neither, and `R2`
gives the reviewer one range and nothing else. Step 4's pre-freeze gate governs a product run's
instruction freeze. Both are superseded in place above; what the opening does owe (`E11` card,
`E10` cold read) is recorded there.


- Suggested order within step 5: **#1 first**. It is the only `PROCESS_BURDEN` of the five and the
  only one that fails *silently* — #2 and #3 announce themselves (dispatch refuses, the flow strands),
  while #1 is what made `p5b-claims` skip a whole step and find out two rounds later.
- `.goals/` is tracked in this repo (not gitignored), so this plan file is committable.
- Rough size: five edits, none large; the cost is the round around them, not the diff.
- If a fresh session is tempted to skip the round because "the patches are already verified" — that
  is precisely the reasoning the 2026-08-03 ruling exists to refuse. Verified ≠ authorized.
