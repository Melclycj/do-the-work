# W2 — combined dispatch: targeted VERIFY of the fix + rule-1 checkpoint read of `3b50738`

**Routed by the user 2026-07-24.** Two independent subjects in one dispatch, deliberately
kept separate in the report: they answer different questions and neither may borrow the
other's confidence. The reviewer may take them in either order.

Both subjects are read from the repository at the pinned revisions. Nothing in this file is
evidence — it names what to look at and what each round is answerable for.

---

## Subject A — targeted VERIFY of the fix round

**Commit under check: `f751358` `V3-W2-REVIEW-FIX-v1`.** Parent: `eb3d7db`.

### What a VERIFY is answerable for (contract §5, V3-D6)

Three things, and the round is incomplete if any is skipped:

1. the accepted findings — did each land as prescribed, and did it actually close what it
   claimed to close;
2. **the entire repair diff**, not only the lines the findings named — an unrelated change
   riding along inside a fix commit is the failure this clause exists for;
3. the permanent boundaries — signed bytes, the declared allowlist, and whether anything
   outside the approved fix boundary moved.

A VERIFY may return `REVIEWED_NO_BLOCKER` or `SPEC_GAP`. It cannot return
`CHANGES_REQUIRED`: there is no second repair for it to request, and a remaining blocker
stops the round instead.

### The approved fix boundary

Three files, no others: `review_subject.py`, `test_review_v2_subject.py`,
`W2-record.md`. Anything else in the diff is out of boundary and is itself a finding.

### The four findings and what was claimed for each

| # | Finding as reported | What the fix claims |
|---|---|---|
| 1 | The reachability sweep read 33 of 38 codes: `check_subject`'s identity table built its five codes as `f"{CODE}-{code}"` from a loop variable, invisible to any source sweep. No silent surface existed — all five were asserted by hand — but a row added later would have carried no assertion obligation, so the record's and the test's "full surface" claims were wider than the guard | each row now carries its code as a whole `f"{CODE}-…"` literal and the raise site uses it directly; **behaviour, message text and condition are unchanged**; `test_the_sweep_reaches_the_identity_table_codes` pins the five by name; probe 7 reverts one row to the invisible form and the new test goes red |
| 2 | The round-opening §7 entry was edited in place inside `eb3d7db` (hard rule 6 forbids it) | corrected by **appending** a new §7 entry that names the earlier one, quotes each edit, separates the legitimate SHA back-fill from the wording rewrites, and points at `19cb882` for the pre-edit text |
| 3 | §5's "zero edits to any pre-existing assertion" was falsified by this round's own declared deviation | §5 now reads "outside the declared deviation" |
| 4 | Two figures wrong: deviation numstat +9/−3 vs a true +12/−3; §6's test count 37 vs 38 | both corrected; §2 records *why* the first figure was wrong (measured after the first of two edits, never re-taken) |

### Questions worth asking of this diff specifically

- **Is F1 genuinely behaviour-preserving?** The claim is that only the *form* of the code
  string changed. The condition, the message and the `where` field should be identical; the
  raise site now passes `code` where it built an f-string. Worth confirming from the diff
  rather than from this description.
- **Does the new test actually pin anything?** Probe 7 is the executor's evidence that it
  can fail; an independent mutation is worth more than the executor's own.
- **Does the F2 correction itself obey the rule it restores?** The correction must be an
  append. The one in-entry change to the *following* entry is a SHA back-fill, labelled as
  such in that entry — legitimate, but check that it is the only change to it.
- **The record now carries an *Independent FULL review* section describing the review that
  produced these findings.** It is the executor's summary of an independent report; check it
  does not overstate the verdict or quietly convert an observation into a discharged item.
- **Did the test count and the suite figures move as claimed?** pytest 373 total, 39 in the
  W2 file. Re-derive rather than accept.

### Executor-declared state at the fix commit

pytest 373 (W2 file 39) · compiler golden 29/29 · harness-v2 39/39 · stage-control 20/20 ·
fixture validators 36/36, 93/93, 41/41 and the stage-control matrix (6/15/20, 0 failures) ·
`repo-audit.py` exit 0 · probes 1–6 re-run red after the F1 edit, probe 7 added, all
restorations byte-verified by SHA-256, `git checkout --` never used. Signed bytes untouched
across the whole round. **These are the executor's figures; they are claims until
re-derived.**

---

## Subject B — rule-1 checkpoint read of the prose batch

**Commit under check: `3b50738` `V3-W2-PROSE-AMENDMENT-v1`.** Parent: `19cb882`.

### Why this read is owed

Instruction-layer rule 1: every instruction-layer amendment passes an independent checkpoint
read **before use** — commit first, because the read binds committed bytes, but no dispatch,
round or run may rely on the amended text until the read has occurred. **The read's subject
is the amendment text itself, never the work it governs.** This batch has not yet been read,
so nothing may rely on it; wave 2's first real run would be the first thing that would.

### What the batch does

Two additive sections, both scoped to successor runs and both stating that they govern only
once the user signs the carrier at the wave-2 gate:

- `REVIEW.md`, a new section after *Evidence discipline*: the shortened custody chain
  (out-of-band SHA → git object → bytes), the control plane read **at** the commit rather
  than verified against frozen digests from the working tree, the member list derived rather
  than delivered, refusal grounds restated in the new shape, and what does not change —
  scope-relative verdicts, `UNVERIFIABLE`, and that a commit pins bytes and never honesty.
- `EXECUTION.md`, a stage-marked paragraph under *After a review*: the repair regenerates no
  package and must land a **new** evidence commit.

Declared additive: 35+/0− and 9+/0−, no existing line rewritten (rule 3).

### Questions this read is for

- **Is it truly additive?** Rule 3 bans rewriting instruction prose; re-derive the numstat
  and confirm zero deletions.
- **Does the scoping actually hold?** Both sections claim they govern only after the
  carrier is signed. A reader who lands on the new section first must not come away thinking
  the successor semantics are already live.
- **Does it contradict anything it does not amend?** The surrounding package-bound sections
  stay unqualified by design. Is the boundary between them legible, or does a reader now
  face two live and conflicting accounts?
- **Does it raise a promise the product does not keep?** Particularly the claim that the
  commit discharges what the package's digest verification used to do — is that stated at
  the right strength?
- **Do the stage markers carry their provenance?** The W1 B3 finding asked for this.

---

## Reporting

Report the two subjects separately, each with its own verdict, its own findings and its own
residual uncertainty. If a finding in one bears on the other, say so explicitly rather than
merging them. Findings should name a minimum fix; a non-blocking finding is stated plainly
as a finding rather than inflated into a blocker.
