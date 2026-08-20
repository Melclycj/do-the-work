# Amendment checkpoint read — `b953b3c` (the checkpoint-read-2 fix batch)

The rule-1 / §12 checkpoint read this batch's own provenance entries declare it owes. **Not a
round in §3's sense:** it consumes no plan-§8 budget and carries **no verdict** — findings
only, tiered must-fix / low / observation. Its authorization is the `ADOPT_DOCUMENT_V3`
standing-discipline entry (N3 record §8; N3-R10) plus the user's dispatch of this read to an
independent review session — the question was set by the dispatch, not by the execution
session, so §1's standing test is met and the one-time dispensation of the previous read is
not repeated.

**Subject, re-derived before reading any content:**

- `b953b3c` (`V3-SCOPE-DISCIPLINE-CHECKPOINT-FIX-2-v1`), parent `f7bd8f6` — the
  checkpoint-read-record commit, as required. `git rev-list --all --parents` shows it is the
  **unique** child of that parent, and it is the branch tip: nothing has relied on the
  amended text before this read.
- Numstat 28+/14− (execution contract) and 19+/8− (review contract); total 47+/22−, matching
  `--stat`.
- `git diff b953b3c` over both contracts is empty — the worktree text is the amendment text,
  so the current files were read as the subject. Only worktree deviation: untracked
  `ResearchSystem/docs/General-Harness-v2-Design.md` (carried; see O5).
- Changed paths are exactly the two operating contracts — migration root, outside every
  node's `N<n>/**` allowlist, an explicit out-of-node commit as both contracts' openings
  require.
- Signed bytes untouched at the subject tree: plan blob `8ad404b1…`, contract blob
  `b2dbdf75…` (`ResearchSystem/contract/Document-Work-Assurance-Contract-v3.md`). A4
  (`f91a7c4`) is not an ancestor.

**Yield: 0 must-fix + 0 low + 5 observations** in ~47 new lines. First batch in the
scope-discipline sequence to come in below the §12 rate (~3 per 79 careful lines) — and
consistent with the previous read's O4 mechanism: the defect-prone zone is the
self-description of the just-lived act, and this batch's only overstatement sits in the
immutable commit message, not in the instruction text (O1 below).

---

## Findings — observations only, no fix owed on any

1. **O1 — the commit message's "this time under a disposition the repository actually
   holds" overstates what a repository can hold.** What the repository holds, after this
   commit, is the batch's own provenance assertion — the same *form* the false-authorization
   incident also had; the committed text of that incident's fix batch likewise asserted a
   disposition. The distinction that actually matters — that this disposition occurred — is
   a chat fact with no evidence lock (review contract §10 ceiling), raised here as
   *consistent, not verified*: the applied edits match the findings record's minimum-fix
   shapes exactly, which a fabricated disposition would have no reason to do. The in-file
   provenance entries use the standard honest form ("authorization: the user's dispositions
   of that checkpoint read") and are clean. Messages are immutable — recorded, per the O1
   convention of the previous read, so a later reader does not take "the repository holds"
   at evidence strength.
2. **O2 — the recast pointer paragraph keeps the possessive the record's F1 minimum fix
   asked to drop.** "…paid for it at **its** checkpoint read" still attributes the read to
   the section, where the read's subject was both files. Under the deletion disposition the
   harm F1 named — the false count and the findings-attribution — is gone, and the sentence
   is accurate in substance (the earlier version was part of that read's subject). Residue
   only; no fix owed.
3. **O3 — F3 was applied beyond its literal instance, declared.** The second 2026-07-26
   entries' flags — discharged by the very read being applied — were closed along with the
   first entries' flags the finding named. Defect-class treatment (the standing flag *is*
   the stale-pointer shape), declared in the commit message with its rationale rather than
   done silently; the visibility gives the user the overrule. Consistent with the harness's
   own rules; recorded so the boundary extension is attributed.
4. **O4 — hunt-list item 8's mini-narration stands, out of scope.** "Found this way on the
   dispatch rounds, twice in the same file within one day…" — the previous read's O2,
   untouched here because no disposition covered it. Still a candidate for the same
   denarration treatment at the next instruction-layer batch. The provenance chains have
   meanwhile grown to eight entries (execution) and seven (review); they are the layer's
   only custody record, so no fix is proposed — growth noted.
5. **O5 — untracked `ResearchSystem/docs/General-Harness-v2-Design.md`** still sits in the
   worktree, unchanged in membership since the previous read's O3. Not a smuggled change to
   the subject files (byte-identical to tip); re-attributed here so it stays accounted for.

---

## What I checked and found sound

Stated by dimension, because a silent dimension is indistinguishable from an unchecked one.

- **F1 applied per its deletion disposition, at all three sites.** The false count clause
  ("every one of them in the narration, none in the rules" / "All six findings…moots five")
  is gone from the execution pointer paragraph and from both files' second entries. The
  replacement text is count-free and accurate: "the findings that sat in the narration"
  were mooted (C1–C4, C6 — C2's site was review-§10 narration, also part of what was
  deleted), C5 sat in the rules and its correction stands. Residual grep for the deleted
  claims across both contracts at tip: **empty** — recomputed, not accepted.
- **F2 applied.** The review contract's copy now reads "the no-duplication discipline
  stated in the execution contract's opening, applied to this file as well" — pointing
  where the discipline actually lives; the execution copy keeps "this file's own opening
  discipline", which is true there. Hunt-item-6 shape closed.
- **F3 applied.** Both first-entry flags closed to pointer form ("**Read same day** —
  findings: […]"), matching the 94a97f5 note convention; the new third entries open their
  own "Owes a checkpoint read" flag — the flag this read discharges. Closing *that* flag is
  the execution side's next act, not the reviewer's.
- **F4 applied per option (a), and its premise re-verified at tip.** Rule 2's closing now
  prefers externalizing the expectation into a committed fixture — naming honestly that the
  risk moves to the update procedure — with the in-file source-reading check kept for where
  the literal must stay. Recomputed the premise myself: no `import ast` and no
  self-source-reading guard under `ResearchSystem/tooling`;
  `tooling/tests/fixtures/expected-construction-prompt.txt` tracked at tip. The one
  remaining `inspect.getsource` (`test_package_and_review.py:1226`) is the **opposite
  polarity** — a hand-written expected list checked against source-derived actuals — not
  the guarded class, so the message's "deleted the only instance of that check" stands.
  The record's "next instruction-layer batch" timing is also satisfied: this batch *is*
  that batch.
- **Counterpart agreement holds.** The third entries cross-attribute consistently ("F2 is
  the review contract's copy only" / "F4 is the execution contract's rule 2 only"); the
  intentional divergence in the second entries is exactly the F2 fix; C5's agreement
  (review reports the shape, cannot conclude deletion) is untouched. **No SPEC_GAP.**
- **Every hunk sits inside the stated edit permission.** Corrections touch only text the
  reviewed batches (`e3c7446` + `3ade2ce`) added — pointer paragraph, second entries,
  rule 2's closing — and the first-entry flag closures follow the established note
  convention, per F3's explicit minimum fix. No rewrite; discipline rule 3 respected. No
  count, date or finding ID entered the rules themselves.
- **The new entries' self-description matches the diff.** Each per-file claim ("deleted
  from the entry above and from the section's pointer paragraph", "the first 2026-07-26
  entry and the entry above", the per-file F2/F4 attributions) was checked hunk by hunk;
  all accurate. The defect class the previous read's O4 predicted for this zone did not
  recur in the instruction text.
- **Nothing mechanical moved, re-derived myself at tip:** pytest **426 passed**; compiler
  golden **29/29**; `repo-audit.py` **exit 0**. Correct for an instruction-only change; per
  discipline rule 3, green suites are not evidence about this layer — this read is.

---

## Coverage and recompute list

- **Read in full:** the subject diff (119 lines); both contracts at tip (the operative
  amendment text); `v3-checkpoint-read-3ade2ce.md` (the F1–F4 ground truth and disposition
  reference).
- **Probed:** `test_package_and_review.py` around line 1226 (the surviving `getsource`);
  tooling tree listing; `ResearchSystem/docs/` listing.
- **Not read:** `v3-checkpoint-read-1d25aae.md` and the three dispatch-round review
  records' bodies — pointer targets, not the subject; tracked status verified
  (`1d25aae` blob `d4507f52…`, `3ade2ce` blob `88634946…` at tip).
- **Recomputed myself, accepting no reported number:** parent and unique-child derivation
  (`rev-list --all --parents`); both numstats against `--stat`; plan and contract blob
  identities; A4 non-ancestry; the empty `git diff b953b3c` over both contracts; residual
  greps for every deleted F1 clause; guard-absence grep and fixture tracked-status; pytest
  426; golden 29/29; repo-audit exit 0.

---

*Authored by the review side. This read discharges the third 2026-07-26 entries' "Owes a
checkpoint read" flags; with zero must-fix and zero low findings, the amended text may be
relied on as it stands, and the flag closure — plus any disposition of the observations —
is the execution session's act under the user's routing. Not a node artifact; outside every
node allowlist; bears on no verdict. Committing this file is the execution session's act,
not the reviewer's.*
