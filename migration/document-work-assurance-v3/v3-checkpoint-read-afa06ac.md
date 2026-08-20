# Amendment checkpoint read — `afa06ac` (V3-NARRATION-DIET-AMENDMENT-v1)

**Status: review-side authored, relayed by the user, committed by the execution side.** The
rule-1 read the batch's own provenance entries mark as owed ("Read: owed by this batch");
authorized by the `ADOPT_DOCUMENT_V3` standing schedule; no plan-§8 budget, no node verdict.
Condensed reproduction; the full relay lives in the routing session. Relay disclosure: the
pasted report duplicated the Finding F1 block, the first copy truncated mid-sentence and
spliced into an unrelated clause; the complete second copy was taken as authoritative (the
`e90243a` most-reasonable-reading precedent). Corruption occurred in relay, not in the
reviewer's conduct.

**Headline: 0 must-fix / 0 low / 1 banked wording-level finding / 7 observations. Both
riders (cr-F1 / cr-F2) verified landed per their ruled dispositions; suite 427
reviewer-run; guard red-tested; all three signed blobs verified. With the bank rule in
effect, the amended text may be relied on.**

## Subject, re-derived by the reviewer

Range `4b1f7e9..afa06ac` = exactly one commit; parent `4b1f7e9` (the 43fb1c5 read-record
commit), `afa06ac` its unique direct child (`rev-list --parents` full scan). Numstat
self-computed: operating contract +11/−0 · review contract +13/−1 · test +5/−1. Signed
blobs at subject: plan `8ad404b1…` ✓ · contract `b2dbdf75…` ✓ · supersession-1 `68031fa2…`
✓; A4 `f91a7c4` not an ancestor ✓. Changed paths hand-classified: both contracts
(migration root, out-of-node) + the test file (the layer's sole named exception file;
diff confirmed docstring-only, no behavior bytes). Worktree: ` M .goals/LEDGER.md` (+6/−2,
user WIP) + untracked `ResearchSystem/docs/` — no smuggled subject content. HEAD at
`a3054f9` (32s later, +1 generated issue JSON, touching no subject file); worktree
test/README blob-hash-identical to subject, so the suite run is representative of the
subject.

## Finding

**F1 — banked wording-level (classified per the bank rule this subject introduces;
otherwise low) — the discipline section's lead-in still says "The three rules below were
attached by the user to the `ADOPT_DOCUMENT_V3` ruling (N3 record §8; registered
N3-R10)", while the section now holds four rules and rule 4's authorization is the
2026-07-27 ruling, not `ADOPT_DOCUMENT_V3`.**

Ground truth: rule 4's own tail "(User ruling 2026-07-27.)" and the provenance entry
attribute its authorization accurately. Risk: an authorization audit reading only the
lead-in files rule 4 under N3-R10. Bank-rule test applied verbatim: the fix changes no
actor's action, and the accurate fact is recoverable in place → banked, rides the next
batch touching this layer; minimum fix then: "The three rules below" → "Rules 1–3 below"
(rule 4 per the 2026-07-27 ruling) or equivalent. The reviewer notes this is the
pattern-staleness class rule 4 itself targets — the lead-in was true when written and this
batch expired it; classification disposition belongs to the user.

## Rider fidelity (both verified)

- **cr-F1 ✓** — exactly the ruled option one ("delete the phrase"); the modified line's
  remaining bytes preserved verbatim; subtractive, rule-3 conformant.
- **cr-F2 ✓** — docstring disclosure matches the recommended shape (docstring option +
  reason); its factual claim independently recomputed: all 14 stems' delimited forms occur
  only at README lines 20/21/22 — whole-README ≡ region matching on today's bytes; the
  "today" qualifier honestly bounds the residual drift risk.

## Observations (none owing a fix)

- **O1** — §10 authorization ceiling: the rulings exist only as commit-message/provenance
  assertions; the burden assessment itself entered the repo one commit later (`a3054f9`).
  Consistent with everything visible; the rulings themselves not independently
  verifiable. Standing ceiling, not a block.
- **O2** — the two new provenance entries conform to the rule-4 format they introduce and
  are this file-pair's first entries that do not pre-assert their own read state — "Read:
  owed by this batch" marks unverified as unverified.
- **O3** — bootstrap ordering: the commit message pre-committed this read's wording-level
  findings to the bank rule the batch itself introduces, while rule 1 strictly bars
  relying on unread amended text; harmless here (the read found the rule text
  defect-free, and the alternative — a fix round for a stale count — is the recursion the
  ruling ended), but the ordering is flagged for the user's glance; F1's classification
  disposition is the user's regardless.
- **O4** — one-sided counterparts: rule 4 sits only in the execution contract, the bank
  rule only in the review contract; the banked-rider obligation lands on the execution
  side, which carries no pointer to it. Covered today by "each side reads the other" +
  the §13 one-sided precedent; recorded so the asymmetry is a choice, not an oversight.
- **O5** — rule 4's "pasted derived facts … have never been wrong" is a historical
  characterization (the rule bans characterization in provenance entries, not in rule
  text — no self-violation); instances spot-checked (3 signed blobs ✓, the 39e4136
  entry's finding counts vs its record ✓), not exhaustively re-verified across both
  files' history. Ceiling stated.
- **O6** — the bank rule's "(ending a 2→1→0 read recursion)" is not derivable from
  committed read records (several chains approximate, none exact); it refers to the
  in-session cascade; nothing depends on it.
- **O7** — ratchet ledger (§10): this round added zero mechanical components — two prose
  rules, one deletion, one disclosure sentence. The bank rule is itself an anti-ratchet
  mechanism; rule 4 shrinks the future narration surface. Direction: subtractive.

## Negative results (checked, found nothing)

Rewrite scan (hunt 7): no existing line retyped; the only non-append is the ruled phrase
deletion with in-line bytes preserved. Self-referential prose (hunt 6): no new
self-approving assertion; "Read: owed" is its honest opposite. Authorization-clause scan
(hunt 1): both new rules carry explicit attribution consistent with the commit message
(ceiling O1). SPEC_GAP scans: bank rule vs execution rule 1 (a banked rider's carrier
batch still owes its own read), bank rule vs §3 anti-renaming (the named-decision test
guards against downgrade abuse), rule 4 vs §13 (disjoint domains) — the two contracts do
not conflict. Verdict vocabularies unmixed; commit kind named in title. Suite: 427 passed
(84.9s, reviewer-run). Guard red-test: [review.v2] entry removed → red naming the stem,
restore hash verified; unmutated full suite = green control. Reviewer's own honesty
disclosure: their first mutation was a false negative — they removed a code-span form
while README line 22 uses the link form, leaving the file unchanged and the test trivially
green; redone per §5.2 (a mutation must reproduce the real defect shape) before being
counted.

## Coverage

Read in full: both contracts, the complete subject diff, the commit message,
`v3-checkpoint-read-43fb1c5.md` (subject revision), the test (worktree == subject,
hash-verified), the README enumeration region. Sampled: full README (programmatic
delimited-token scan per line, not sentence-by-sentence human read), LEDGER worktree diff
stat. Not read: N-records in full, earlier read records (pointer targets), `a3054f9`'s
issue JSON (outside subject). Recomputed: range enumeration, parent, unique-child,
numstat, 3 signed blobs, A4 ancestry negative, worktree/subject hash ×2, 14 stems with all
delimited line locations, suite 427, mutation red ×1 + control, restore hash.

Dispositions belong to the user. F1 rides the next batch touching the instruction layer
per the bank rule; until then the amendment text may be relied on — rule 4, the bank rule,
both provenance entries and both riders' substance all independently verified.
