# VERIFY review — round `STRANGER-GUARDS` at `c2e955b..53ec1a6`

**Verdict: `REVIEWED_NO_BLOCKER`.** 0 blockers, 2 observations.

**The repair does what the accepted findings required, the new tests bind, and every
boundary held.** The trailing-slash normalization ends the measured guard divergence at the
site the ruling named, and killing it kills exactly the three tests that claim to guard it;
the README terminus reads as the user ruled and nowhere else performs the rejected framing;
the two register commits do exactly what fix-gate rulings 3, 4 and 5 authorize and nothing
more. Every figure the fix commit reports as its own measurement that I could re-run, I
re-ran and matched: 844 at tip, both mutation red-counts on exactly the claimed tests, all
three guards' zero over the re-staged range diff with a planted-bad-path control firing,
both HD-41 class scans, and the anonymous-404 half of the private-repo measurement.

## 1. Subject, round, budget — re-derived (`R2`)

- **Subject**: `c2e955b..53ec1a6` — four commits, classified by hand: `18bb2bf` (record:
  the FULL's review record, 1 file +232), `8f68d1e` (plan amendment: fix-gate ruling
  carrier, 1 file +40), `54f7fa7` (review fix: `README.md` −13/+6-line region,
  `tooling/rsclib/document_harness/caller.py` +27/−16-region,
  `tooling/tests/document_harness/test_caller_surfaces.py` +65), `53ec1a6` (register
  corrections and ruling entry: `CONSTRUCTION-LEDGER.md` +6/−2,
  `HARNESS-DECISIONS.md` +25/−1). HEAD = `53ec1a6`, worktree clean, branch `main` ahead of
  `origin/main` by 9 (5 pre-FULL + these 4) — nothing pushed (`E8`).
- **Round**: the targeted VERIFY of `STRANGER-GUARDS`, obliged by `E9` once the fix leg was
  spent. The FULL (`v3-review-full-c2e955b.md`, read in full) returned
  `REVIEWED_NO_BLOCKER` with 2 lows and 4 observations; per `R10` the spend-or-bank choice
  went to the user, whose five fix-gate rulings of 2026-08-23 are committed in
  `document-harness/plans/stranger-guards.plan.md` (`8f68d1e`) — the authorization is
  visible in the repository, not chat-only.
- **Budget** (`E9`): one FULL (record landed alone in its window — `18bb2bf`'s parent is
  the candidate, and the trail shows dispatch 12:26Z → record 12:45Z with nothing
  between), one user-approved fix (`54f7fa7`, a late activation after the no-blocker FULL,
  which `R10` explicitly keeps inside `E9`'s test), and this VERIFY. The plan amendment is
  a ruling carrier, not a work product; the registers commit is budget-exempt per the
  2026-08-04 ruling as extended by `HD-23`, whose condition — lands inside the next review
  subject range — this dispatch's base satisfies: base `c2e955b` is the last reviewed tip,
  which is also FULL L-2's lesson applied (ruling 2). My window: marker
  `.harness/review-pending.json` carries exactly this subject, `dispatched_at`
  2026-08-23T13:18:05Z, seven seconds after the registers commit; no commit has landed
  since — the branch held.
- **Commit form** (`E8`): all four titles name the round, all four bodies name their kind
  (record / plan amendment / review fix / register corrections and ruling entry), one
  dense body each, no trailers (checked all four), no amend, linear parentage. The FULL's
  record file is byte-identical from `18bb2bf` to tip — no later commit touched it.

## 2. Accepted finding L-1 — fixed, and the fix binds (`R3` lead)

- **The fix, read whole**: `caller.py` at tip read in full. `ScanSurfaces` gains
  `__post_init__` normalizing `review_record_dirs` and `specification` entries to
  `/`-terminated; `record` is deliberately excluded (it holds file entries —
  `HARNESS-RIDERS.md` normalized to `HARNESS-RIDERS.md/` would exempt nothing) and the
  docstring now states exactly that contract. The site is right: both the loader's only
  return path (`ScanSurfaces(**fields)`) and `DEFAULTS` construct through the dataclass,
  so every declaration is normalized before any matcher composes — the FULL's "normalize
  once" option, one construction site deeper than the loader, which also covers direct
  construction. In-boundary: ruling 1a says "where the surface groups build their
  matching", which is this site.
- **Probe re-run** (function level, this tree): declaration
  `specification=('work/runs',)` normalizes to `('work/runs/',)`; freeze `is_record` on
  `work/runs/p9/evidence/review-full.json` → **True** (the FULL's measured **False** is
  gone); non-result under the tree → False; result in sibling `work/runsx/` → False;
  candidate guard scans the sibling (True) and exempts the declared tree (False). Both
  guards read one declaration one way, and both guard files re-read in full to confirm no
  other composition path exists.
- **Tests** (`E7` — the class, not the instance): six tests in
  `ASlashlessDirectoryEntryReadsTheSameToBothGuards`, covering both directory-kind groups
  and both guards, with two negative controls pinning that normalization narrows to the
  tree and never widens to the leading string; `6 passed, 23 deselected` re-run. The
  record-dir keeps-working pin's not-a-must-fire label is honest (that group's
  `startswith` already agreed pre-fix).
- **Mutations** (`R8`, my own patches in a throwaway worktree at tip, removed after):
  slash-append neutered (`normalized = tuple(entries)`) → **exactly 3 red**, exactly the
  three claimed must-fires (the probe test, the candidate-guard one-tree pin, the direct
  normalization pin) — this is also equivalent-strength evidence for the claimed pre-fix
  red, since the neutered form is the pre-fix behavior for these tests; field loop
  extended to `record` → **exactly 2 red**, the new pin plus
  `test_every_old_exemption_holds_under_the_declaration`, whose expectation I confirmed is
  the hand-typed `FIRST_CALLER_DECLARATION` fixture in the test file, derived from no
  module constant (`E5`).
- **Battery**: `844 passed` at tip, re-run — 838 at the candidate plus the 6 added, sum
  exact.

## 3. Accepted item 1b — the README terminus reads as ruled

`README.md` terminus region read at tip: the `github.com/Melclycj/Thesis-Work` URL, the
as-pushed ancestry sentence and the durable-address sentence are gone; the single-machine
historical form (`D:/Thesis`, worktree, branch, commit `e4ffa2b`) returns; exactly one
plain clause — "that repository is private, and its history is not publicly reachable" —
is added; the Layout-section hunk from the candidate is untouched (the fix's README diff
is one hunk, the terminus). Scan (b) re-run at tip, scope all tracked files: two surviving
`Thesis-Work` sites (the plan's ruling carrier naming what to remove; the immutable FULL
record describing the candidate) and one `request access|durable address` hit (the same
carrier line) — each records the rejected framing, none performs it. The
`CONSTRUCTION-CHECKLIST.md` header's routing sentence still resolves: the README section
still names the extraction-source repository and says why history stayed there.

## 4. The registers commit — exactly what rulings 3, 4, 5 authorize

Word-level diffs read in full. **(3)** `HD-44`'s consequence line now dates the
enumeration — eighteen at the entry's own date, sixteen since `HD-56` — with the note
naming signature commit `3b25f3c`'s unperformed-edit claim (cold read `cf54a79` L-3), and
the ledger's CONTRACT-V4 entry corrects its repetition of the same claim in the same act.
The sixteen I verified by inspection: `contract/Document-Work-Assurance-Contract-v4.md`
plus fifteen files under `schema/document-assurance-v3/` (counted at tip); eighteen then
was v3 + two supersessions + fifteen — coherent. **(4)** the ledger's "public 仓" sentence
now states the measured 2026-08-23 private state and marks the old record as corrected
rather than erasing it; I re-measured the anonymous API today — 404 — and did not re-run
the `ls-remote` half. **(5)** `HD-57` enters §live as the recorded ruling `HD-20` requires
over the five stale-literal `E2` sites, application batch correctly deferred to after
closeout, four rider redemptions bound to that commit — and the four rows (`v4-verifmode`,
`v4-plan-digest`, `wspec-owner`, `hi-schema-gloss`) verified still standing in
`HARNESS-RIDERS.md` at tip, correctly unredeemed. Both cited exemption rulings exist in
the decision log (`HD-23` carries the 2026-08-04 ruling and its in-range condition).

## 5. Permanent boundaries, however narrow the round

- **`E2`**: no path under `contract/` or `schema/document-assurance-v3/` in the range —
  the seven changed paths enumerated and classified by hand in §1. The five frozen-literal
  corrections `HD-57` authorizes are scheduled, not performed, here.
- **`E10`**: no instruction-layer member touched (root `README.md` is not the member —
  `document-harness/README.md` is; the ledger, decision log, rider bank and plan are
  non-members). No member edit, no independent read due from this range, no `E10-sync`.
- **Guards over the range**: all three tracked guards exit 0 over the full range diff
  re-staged at base `c2e955b` in a throwaway worktree; a planted nowhere-resolving path in
  `README.md` makes the candidate guard fire, and `scanned('README.md') = True` re-derived
  — the zeros are not vacuous.
- **HD-41 scan (a)** re-run at tip: every composition site of the two guards consumes
  `ScanSurfaces` fields after normalization; no in-scope site composes a matcher from a
  raw declared string (see O-1 for a paste-fidelity note).
- **Riders**: no standing row's touch condition was met by this range's surfaces
  unredeemed (`freeze-audit`, `decl-dup`, `readme-three`, `decited-paths`,
  `self-caller-guards`, `e9-pair-budget` each checked against the changed paths;
  `self-caller-guards`' deadline — a non-record commit inside a freeze window — did not
  occur: both windows in this range held).

## 6. Observations (non-blocking; neither changes any actor's action)

- **O-1 (paste fidelity, `E3` shape)**: the fix commit's pasted scan (a) output shows
  eight hit lines; the command emits nine at that tree — `review_freeze_check.py:74`
  (`for prefix in surfaces.specification`) is omitted from the paste and supplied in the
  immediately following prose parenthetical instead. The site is fully accounted for and
  consumes normalized fields, so no decision goes wrong; recorded because `E3`'s
  discipline is paste-not-describe, and a dropped line reconciled in prose is the shape
  that one day drops one that isn't. Rides here (`R9`), no bank row.
- **O-2 (label drift)**: of the three tests the commit correctly names as must-fires, two
  carry the `# must fire` comment and the third (`test_record_entries_are_not_normalized`)
  does not. Mutation evidence — not the comment — is the binding claim, and mine confirms
  all three fire; a label-scanning reader would under-count. Rides here, no bank row.

## 7. What I read, ran, and could not verify (`R4`)

- **Read in full**: `CONSTRUCTION-CHECKLIST.md` (current tip, all E/R rules), the review
  contract stub, `v3-review-full-c2e955b.md`, the complete range diff for all seven files
  (registers word-level), `caller.py`, `review_freeze_check.py`, `candidate_path_check.py`,
  the plan's fix-gate section, the six added tests plus the fixture class and header of
  `test_caller_surfaces.py`.
- **Sampled/probed**: the rest of `stranger-guards.plan.md` (change-surface table greps;
  the FULL read it whole), `HARNESS-DECISIONS.md` (HD-23/45 regions whole, HD-20/55/57
  located and headers confirmed), `HARNESS-RIDERS.md` (row ids enumerated; six
  plausibly-touching rows read whole), README terminus and Layout regions, `runs.jsonl`
  (today's entries).
- **Ran**: full battery at tip (844); the 6-test subset (6 passed, 23 deselected); the
  five-shape function-level probe; two self-written mutations in a throwaway worktree
  (3 red / 2 red on exactly the claimed tests, worktree removed after); three guards over
  the re-staged range diff plus one negative control; both HD-41 scans; the anonymous
  GitHub API measurement (404); the schema-pack count; marker, branch and worktree state.
- **Marked, not verified** (process claims): the fix executor's cold dispatch on the
  construction charter with all four `R1` holdings at the orchestrator (`HD-55` — the
  commit says so, the trail is consistent, the tree cannot prove it); the executor's
  sha256-checked scratchpad restore mechanics (I mutated and restored independently
  instead); the pre-fix `3 failed, 3 passed, 23 deselected` pytest line as literally run
  (my neutering mutation reproduces its substance exactly); the `ls-remote`-challenged
  half of the private-repo measurement; the FULL's own base-battery figure (792 — outside
  this subject). A VERIFY is never a re-certification of the candidate; the FULL's
  verdict stands on its own record.

**Verdict: `REVIEWED_NO_BLOCKER`.** The round's three legs are spent; nothing here blocks
closeout. Still open for the orchestrator, none of it mine to rule: the closeout entry
(recording FULL L-2's dispatch-range lesson per ruling 2), the post-closeout `HD-57`
application batch with its four rider redemptions and the `E2` v4-blob-literal update, and
the two member-edit reads CONTRACT-V4 left riding the next opening.
