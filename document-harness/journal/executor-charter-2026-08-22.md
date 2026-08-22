# Round journal — `EXECUTOR-CHARTER` (2026-08-22)

> Narrative and in-round rulings' reasoning only; the rulings themselves live in
> `HARNESS-DECISIONS.md` (`HD-53`, `HD-54`) and the ledger. Records:
> `v3-cold-read-693b692.md` (opening read) · `v3-review-full-229f03f.md` (FULL) ·
> `v3-review-verify-3dd226b.md` (VERIFY) — all under `migration/document-work-assurance-v3/`.
> Plan: `document-harness/plans/executor-charter.plan.md`.

## What the round did

`dtw dispatch` gained the fourth dispatch family — two executor-side modes (`HD-53`) — and
the authoring rule that had every product instruction hand-copy a charter pointer into its
Context section was deleted with a named partial supersession of the 2026-08-01 routed
decision that installed it. Context carries background only now; anything demand-shaped
there is a defect on sight. The reviewer-executor asymmetry the plan opened on is gone:
both cold roles now start from a generated document.

## In-round rulings (all 2026-08-22, at the preview card)

1. **Open per the card** — the round's shape as previewed, six phases, `E9` budget stated.
2. **Sampling obligation: a reading moment, not retirement and not indefinite collection**
   (`HD-54`). The user's framing was kept: the category question — may an instrument charge
   its own research to the instruction surface of the work it measures — is answered by
   giving the research a charter home and an expiry, not by leaving it in Context.
3. **`HD-52` taken in this batch** — the START-card sentence moved out of the
   enumerated-scoped SIMP-C4 bullet into a standalone form-independent paragraph; flipped
   live→implemented in the candidate commit (`HD-2`), rider `startcard-form` redeemed in
   the same commit.

## Candidate design decisions (executor's, within the rulings)

- **Run id = the run directory's own name.** At dispatch time (START, pre-WorkSpec per
  `HD-35`) the only committed identity is the path `assurance/runs/<run-id>/instruction.md`;
  reading any control file would be reading what does not yet exist.
- **Revision = the last commit touching the instruction** (its freeze); **drift judged by
  blob-id equality** (`git hash-object` vs `rev-parse <rev>:<path>`) so eol conversion
  cannot false-positive — the same comparison the cold reads use per member. The FULL
  reproduced this claim on an `autocrlf=true` repository.
- **Executor dispatches write no freeze marker.** The marker opens `E9`'s review window; an
  executor dispatch starts precisely the work that window would freeze. Bound by two
  must-fire tests with the review-side marker tests as positive controls.
- **The nine-obligation table in `ORCHESTRATION.md` was deliberately not touched**, so
  riders `e1-table` and `charter-qualifiers` (both naming that table) did not open. The
  charter delivery is carried by the *Handing the executor its instruction* own-text
  section.
- **`mark-case` deliberately not redeemed** — the plan's measurement stands (a
  case-insensitive marker list would have flagged one thing in eight runs, wrongly).

## The FULL, the triage, and the fix

FULL `v3-review-full-229f03f.md`: `REVIEWED_NO_BLOCKER` — 0 blockers, 5 lows, 7
observations. The implementation half survived nine mutations (nine reds on named tests, no
kill-by-crash); every commit-body figure re-measured identically. Correction the FULL's
`O-2` asked to be on the record: the candidate's `E4` account named four bindings as "all
four new bindings" where seven were new — the code was fine, the account was short, and the
FULL mutated all nine bindings itself.

The `R10` triage put six choices to the user; all six answered 2026-08-22:

1. **Spend the one fix leg once, on the whole package** (FULL `L-1`–`L-5` + cold read
   `L-1`), obliging the targeted VERIFY.
2. **`L-2`: restore the hedge** — "live in this file **and the governing plans**". Asked
   and answered after the user first asked what the sentence is and where it lives; the
   explanation preceded the choice.
3. **`L-4`: fix `ONBOARDING.md`, the decision log stays as history** — `HD-46`'s basis line
   is a record of the reasoning as it was, read as history, not corrected and not
   re-banked (downstream zero-change at that site, as the deleted rider itself recorded).
   This is the disposal moment rider `charter-prose-overreach` ① reserved for "together
   with `HD-46`": the derivative sites are corrected or left as history, and `HD-46`'s own
   recorded text is history by the user's ruling.
4. **Cold read `L-1`: the criterion reading** — `HD-45` ②'s clause is the rule, the em-dash
   list is examples; the reader's bytes landed with the fix, bare module names widened to
   repository-resolvable paths.

Fix `3dd226b` (four files) — VERIFY `v3-review-verify-3dd226b.md`: `REVIEWED_NO_BLOCKER`,
2 lows, 3 observations; every accepted finding re-executed, five further mutations (with a
green negative control), all four reported figures reproduced — the guard figure only after
the VERIFY discarded its own first null measurement and re-fed the commit's added lines to
the guard's predicate directly.

## Closeout dispositions of the VERIFY findings

- `V-1` (fix legs not pasting `HD-41` ④'s class-scan output; four legs, one paste) →
  bank, row `fixleg-scan-paste` — the work product is an immutable commit body, so no
  bytes exist; whether four-in-a-row warrants more than a row stays the user's.
- `V-2` (the plans' delivery path unnamed in `ORCHESTRATION.md`) → bank, row
  `plan-delivery`, deadline = the first product-run instruction authored under the new
  rule (the same moment FULL `O-7` names for the layer read).
- `V-3` bounded the ledger trim executed at this closeout: the conversation-only C4 `O-1`
  row keeps its three re-ruling branches — the layer sentence points at the row for
  exactly that — and sheds the recording-obligation half to a pointer at `EXECUTION.md`.
- `V-4` (golden equality pins agreement, not truth) and FULL `O-1` (the product executor
  mode lacks a mount test; behaviour verified correct) → `O-1` banks as `exec-mount-test`;
  `V-4` needs no carrier beyond its record — `E6` argues against a guard and the class is
  held by human reading.
- FULL `O-3` (empty mode value falls through the elif chain — a class predating this
  round) and `O-4` (`--executor` means a run directory on dispatch, an identity string on
  review): recorded in their record, no action — `E6` on both.

## Honesty boundaries

- `ONBOARDING.md:74` and `:152` say "the marker is written by `dtw dispatch`" — still true
  of the review-side modes those sentences describe, so not falsified; left untouched.
- One work-side session held orchestrator and executor throughout (`E1` disclosure in the
  candidate body, `15a53fe` form). All three review legs ran as cold dispatched sessions;
  their independence is disciplinary, not structural, and none claimed otherwise.
- The construction-side executor mode has not yet been exercised by a real construction
  round's opening — this round's own executor was the session already in conversation. Its
  first live use will be the next round that dispatches a separate executor session.
- The two member edits (candidate and fix alike) owe their independent `E10` read, riding
  the next read of this layer; the binding moment FULL `O-7` names is the first
  product-run instruction written under the new authoring rule.
- This session wrote nothing into the caller's tree this round. The FULL's five-run count
  was measured in the caller by the reviewer, read-only.
