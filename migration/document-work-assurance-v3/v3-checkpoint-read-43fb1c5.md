# Amendment checkpoint read — `43fb1c5` (the checkpoint-read closure batch)

**Status: review-side authored, relayed by the user, committed by the execution side.** The
rule-1 read the user routed after catching, same day, that the closure batch's own
commit-message exemption claim ("registrational bookkeeping, swept by the next boundary
read") stretched the pointer-form exemption — the batch carries a guard fix, a new check
script and a README enforcement row, and every fix batch in this thread got its own read.
Authorized by the `ADOPT_DOCUMENT_V3` standing schedule; no plan-§8 budget, no node
verdict; delivered as the reviewer's final message per the banked record-channel issue and
routed by the user. Condensed reproduction; substance, severities, quotes and minimum
fixes preserved; the full relay lives in the routing session.

**Headline: 2 findings (0 must-fix / 2 low) + 6 observations. The F1 back-fill and F2
guard narrowing both land and were independently mutation-re-proven; the mechanization
(tracked script + README row) was red/green/idle-probed live by the reviewer; signed bytes
untouched. Both lows are registration-wording precision, not blocking reliance.**

## Subject, re-derived by the reviewer (no reported number accepted)

Range `c9a1ac1..43fb1c5` contains exactly one commit; parent = `c9a1ac1` (read-record
commit, provenance-excluded per the 94a97f5 precedent); `43fb1c5` the unique direct child;
HEAD == `43fb1c5`. Numstat self-computed: README +1/−0 · operating contract +13/−0 ·
review contract +12/−0 · `contract_provenance_check.py` +57 (new file, new `tooling/hooks/`
directory) · `test_readme_enumeration.py` +14/−2; the message's "25 added lines, zero
deletions" recomputed true (13+12/0). Signed bytes compared one by one at subject: plan
`8ad404b1…` ✓ · contract `b2dbdf75…` ✓ · supersession-1 `68031fa2…` ✓. A4 `f91a7c4` not an
ancestor ✓; A3 `7db177d` and `ac1b383` in ancestry ✓. Changed paths hand-classified: both
contracts (migration root, outside every node allowlist by design), README + script + test
— an explicit out-of-node closure commit; no pointer/LEDGER write. Worktree: only
` M .goals/LEDGER.md` + untracked `ResearchSystem/docs/General-Harness-v2-Design.md`
(O3); no smuggled subject content.

## Findings

**F1 — low — the review contract's new entry says "Additive only; no earlier line
changed", which is false for the two batches it registers.**

- Verbatim (review contract, 2026-07-27 entry, added by this commit): "Authorization: the
  user's dispositions of that cold read. Additive only; no earlier line changed."
- Ground truth: `git show 8d03563` → operating contract 5/3, review contract 3/1 — the
  "zero mechanical binding" sentence was reworded in place (incl. "Its only instrument is
  an" → "Its only instrument otherwise is an"); `git show 39e4136` → review contract 1/1
  (the §2 table row gained the third blob in place). In existing provenance usage the
  phrase means pure appends (the §12/§13/hunt-8 entries); here it is false.
- Mitigating facts: the same entry's preceding sentences name the modified sites precisely
  ("§12's … sentence gains …", "§2's signed-bytes row pins …") — self-contradiction, not
  clean misdirection; and the operating contract's parallel entry in the same closure batch
  correctly wrote only "Additive only" without the phrase — a drafting slip, not a
  systematic claim.
- Risk: the phrase is exactly what a fresh reader uses to decide "read only the new lines
  or re-read the whole text"; taken literally it skips §12/§2, whose semantics are what
  moved.
- Minimum fix: one corrective sentence in the next batch that touches provenance — delete
  the phrase, or restate as "insertions only, within the named sentence/row; nothing else
  changed".

**F2 — low — the F2 fix landed narrower than the ruled minimum-fix text: the region
qualifier was dropped without disclosure.**

- The read record's minimum fix: "narrow the match to delimited tokens **within the
  enumeration table region**". The implementation matches delimited tokens over the whole
  README; the closure message presents it as applied-as-ruled without mentioning the
  dropped qualifier.
- Current consequence is zero (reviewer recomputed): all 14 stems' delimited occurrences
  sit only in the three enumeration rows (README:20/21/22) — full-text matching is
  presently equivalent to region matching.
- Mutation re-proof (all reviewer-run, README byte-restore SHA-256-verified): M1 review.v2
  / M2 [review] / M3 [assurance] each removed → all RED naming the missing stem; reviewer
  added M4 (remove `document-work-spec` leaving the .v2 sibling) → RED, proving a prefix
  stem is not satisfied by its longer sibling; unmutated control green.
- Residual risk: future README prose containing a stem in delimited form silently
  re-weakens that stem's guard; plus the class risk — silent under-application of a ruled
  fix.
- Minimum fix: one disclosure sentence (test docstring, or the next provenance batch:
  full-text delimited matching deliberately chosen over a region parse, with the reason);
  if the user wants the letter of the ruling, add region scoping. Per scope discipline the
  reviewer recommends the former — a region parser is new machinery for zero current
  value.

## Observations (none owing a fix)

- **O1** — the closure message's "swept by the next node-boundary cold read per standing
  convention" understated rule 1's literal obligation for a batch that modifies both
  contracts; cured in fact — the user dispatched this read.
- **O2** — authorization ceiling (§10): the "user-ruled fix" and mechanization-ruling
  attributions exist only as commit-message/provenance assertions; consistent with
  everything visible (the read record's minimum fixes precisely prefigure this closure's
  shape), but the rulings themselves are not independently verifiable from the repository.
- **O3** — the worktree LEDGER live pointer is stale relative to HEAD (still says the cold
  read's four findings await ruling); same class as the previous round's O3; the user's
  own WIP, outside subject.
- **O4** — ratchet ledger (§10 duty): this round adds 1 tracked component + 1 README row
  to terminate a prose-omission class already paid for twice (`979a983`, this thread's
  F1). Checker-terminates-prose shape (N0-R4 precedent), user-ruled, honesty boundary
  declared consistently in three places (script docstring / README row / hook comment) — a
  benign direction; keep logging components-added vs components-alive next rounds.
- **O5** — the provenance script's inherent limit beyond its disclosed advisory boundary:
  a cut-paste move of an existing entry also satisfies `^\+> 20\d\d-\d\d-\d\d`; the check
  binds "an entry was added", not "the entry truthfully describes the change" (F1 is an
  instance of the latter, which the script cannot see — consistent with the declared "the
  layer's real instrument remains the independent read").
- **O6 (positive)** — hunt-8 sweep of the script: the CONTRACTS path list and date regex
  are hand-written literals independent of the guarded files; git failure is fail-closed
  via `check=True`; the only fail-open paths (fresh clone without the hook / branches
  without the script) are disclosed in the README row and hook comment.

## Negative results (checked, found nothing)

F1-fix fidelity: both entries' attributions verified item-by-item against the diffs — the
operating entry registering only `8d03563` is correct (`39e4136` did not touch that file);
the review entry's `8d03563`→§12 and `39e4136`→§2 attributions match the artifacts; the
headline "1 must-fix + 1 low + 5 observations" matches the read record; the record link
resolves; "Read same day" confirmed by commit timestamps (01:37/01:48 → 02:10 → 02:44, all
2026-07-27). README row factual claims verified live on this machine — the hook sits in
the main repo's git dir (`D:/Thesis/.git/hooks/pre-commit`; this directory is a linked
worktree, matching the row's "main repo" wording), runs repo-audit first, then the
existence-guarded provenance check; advisory/bypassable descriptions all true. Script
behavior: idle → exit 0; staged contract edit without entry → exit 1 with the correct
message; with a `> 2026-07-27` line → exit 0; index/worktree restore verified by hash +
git status after probes. Suite: 427 passed (72.5s, reviewer-run). No rewrite (the closure
is pure appends to the instruction layer: 25/0 + 1/0); no new self-referential prose
(reliance assertions pointer-backed to committed records); construction/product verdict
vocabularies unmixed; the commit kind is named in the title (closure).

## Coverage + recompute

Read in full: this commit's complete diff, both operating contracts (full text at HEAD),
`v3-checkpoint-read-39e4136.md`, `test_readme_enumeration.py`,
`contract_provenance_check.py`, the README, this machine's pre-commit hook. Sampled:
`8d03563`/`39e4136` contract-hunk diffs (fidelity cross-check; the rest was the previous
round's subject), `v3-cold-read-1df6245.md` (tail + grep), the LEDGER worktree diff
(preview). Not read: N-records in full, earlier read records (pointer targets). Recomputed:
range enumeration, unique-child, parent, 3 signed blobs, ancestry ×3 (A4 negative + A3 +
`ac1b383`), numstat ×3 commits, 25/0, 427, 14 stems, all 14 delimited locations
line-by-line, mutations ×5 (4 red + 1 green control), script probes ×3, restore hashes ×3,
commit timestamps ×6.

Dispositions belong to the user. Both lows' minimum fixes are one-sentence scale and can
ride the next batch that touches this layer; until then, the registered `8d03563`+`39e4136`
amended text (read clean last round) and this closure's substance may both be relied on —
F1/F2 affect the registration wording's precision, not the correctness of the registered
work.
