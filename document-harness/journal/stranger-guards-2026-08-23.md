# Round journal — `STRANGER-GUARDS` (2026-08-23)

> Narrative and closeout dispositions. The round's rulings live in
> `document-harness/plans/stranger-guards.plan.md` (four opening rulings + five fix-gate
> rulings, all 2026-08-23) and in `HARNESS-DECISIONS.md` (`HD-57`). Records:
> `v3-cold-read-cf54a79.md` (opening read) · `v3-review-full-c2e955b.md` (FULL) ·
> `v3-review-verify-53ec1a6.md` (VERIFY) — all under `migration/document-work-assurance-v3/`.
> Written by the orchestrator at closeout; every figure below is quoted from a record or a
> commit body, none is a new measurement.

## What the round did

First round of publicization batch C (陌生人可用性). The guard scan surfaces stopped being
the first caller's hardcoded directory names: `caller.py` loads a caller-side declaration
(`.harness/scan-surfaces.json`, written by `dtw init` with defaults and never overwritten;
malformed input refuses loudly, never falls back silently), both guards read it, and the
first caller's `ResearchSystem/…` entries survive as that caller's declaration, pinned
byte-for-byte in tests. `TrackedPaths` sees submodule-internal paths (rider `submod-index`
redeemed — the ruled design answer). All twelve repo-root resolution points (six `cli.py`
cwd defaults, six template `parents[3]` defaults) now discover via git or refuse loudly —
the `review_freeze_check.py` extension beyond the plan table was class-scanned into scope
and disclosed with its cost in the candidate body. The layer's correction paragraph stopped
reading role-annotated citations backwards for a second caller (rider `amend-exempt-caller`
redeemed); the README terminus, after the user rejected the request-access proposal, returned
to the single-machine historical form with one plain clause that the caller's repository is
private. Riders `chk-caller-prefixes`, `submod-index`, `amend-exempt-caller` redeemed by
deletion in the candidate; `decited-paths` touch-noted, its redemption caller-side. Battery
792 → 838 (candidate) → 844 (fix leg).

## Role form

`HD-55` norm, no exception: opening read, candidate executor, FULL, fix executor and VERIFY
were five separately dispatched cold sessions (`dtw dispatch` 出单), `R1`'s four holdings
the orchestrator's throughout, orchestrator hand-editing no work product. Process claim,
marked not verified (`R4`): the git identity is the same on every commit.

## The dispatch-range lesson (FULL Low-2, recorded here per fix-gate ruling 2)

The riders-bank commit `95ca8d2` relied on "covered by the next review subject" for its
budget exemption, yet the FULL's range was dispatched with that very commit as its base —
excluding it. The reviewer read the two rows proactively and found them conforming, so
substance was covered, but by grace rather than by construction. Standing lesson for every
future dispatch: **subject base = the last reviewed tip** (so bookkeeping commits land
inside the reviewed range, which the 2026-08-04 ruling's exemption presumes), and
riders-only commits land **after** the candidate where the ordering allows. This round's own
VERIFY already ran that way (base `c2e955b`, covering the plan amendment, the fix leg and
the register commit).

## VERIFY observations, recorded without action

- The fix commit's pasted class-scan output is one line short of the command's real output
  (`review_freeze_check.py:74`), the gap covered in adjacent prose — an `E3`
  paste-don't-describe wobble, on the books as the fifth entry in that family of drift.
- One of the three must-fire tests lacks its `# must fire` comment label; the mutation
  evidence itself is complete.

## Honesty boundaries

- The private-repository measurement (anonymous API 404, anonymous `ls-remote` challenged)
  was reproduced by the FULL and the API half again by the VERIFY; it is a statement about
  2026-08-23, not a standing property.
- The second-caller items this round exists for are still unproven against a real second
  caller: `STRANGER-PROOF` (next round) carries that burden, and only a stranger on another
  machine closes it fully (the `CALLER-ONBOARDING` honesty caps stand).
- Member edits owing their independent read at the next opening: the checklist correction
  paragraph (candidate), plus whatever the post-closeout `HD-57` application batch touches
  (contract v4 and the checklist `E2` blob literal) — the `STRANGER-PROOF` opening read
  collects all of them.
