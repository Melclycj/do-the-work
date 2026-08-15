# W2 — dispatch: rule-1 checkpoint read of the B1 prose amendment

**Subject: commit `6f7b2dc3e79b14b2655de34126fcf1e8850cd7ef`
(`V3-W2-PROSE-INFULL-AMENDMENT-v1`), parent `6b55d10`.** Routed by the user 2026-07-24 —
the last carried debt of the (now CLOSED) wave-2 implementation round.

You are an **independent reviewer**. The executor authored this amendment; its framing
below is context, not ground truth — verify everything from the committed bytes yourself.
Nothing here is evidence.

## Why this read is owed

Instruction-layer rule 1: every instruction-layer amendment passes an independent
checkpoint read **before use** — commit first (the read binds committed bytes), but no
dispatch, round or run may rely on the amended text until the read has occurred. **The
read's subject is the amendment text itself, never the work it governs.** This amendment
has not yet been read, so nothing may rely on it; wave 2's first real run would be the
first thing that would. This read discharges that obligation (or names what must change
first).

## What the amendment is

A **two-word** instruction-layer change to `ResearchSystem/document-harness/REVIEW.md`, in
the successor-run section's custody-chain sentence:

```
- ...custody chain shortens: out-of-band evidence commit SHA →
+ ...custody chain shortens: out-of-band evidence commit SHA (in full) →
```

Its stated purpose: the v1 custody-chain bullet directly above (REVIEW.md line 68, added by
the O2 fix in `979a983`) already requires the digest to reach the reviewer "**out-of-band
and in full**" — the O2 lesson being that w1-r1 once dispatched an 8-hex SHA prefix (a 2^32
collision space). The successor section swapped the package digest for a commit SHA but did
not carry the "in full" qualifier over, and an abbreviated SHA is git's daily default
(`git rev-parse --short` returns 7 hex in this repo), so the same escrow-strength gap
transferred silently. The amendment restores the qualifier.

## Reproduce independently

- `git show 6f7b2dc3e79b14b2655de34126fcf1e8850cd7ef -- ResearchSystem/document-harness/REVIEW.md`
- `git diff --numstat 6f7b2dc~1 6f7b2dc -- ResearchSystem/document-harness/REVIEW.md`
- the mirrored v1 bullet: `grep -n 'out-of-band and in full' ResearchSystem/document-harness/REVIEW.md` (line 68)
- the amended successor sentence in context: read REVIEW.md around line 92 at commit `6f7b2dc`

## What this read should confirm (or refute)

1. **Additive, nothing corrupted.** Is the change purely the `(in full)` insertion? The
   numstat is 2/2 — confirm the second changed line is only a line-wrap of the same
   sentence, with no other content altered and no line deleted (rule 3 bans rewriting
   instruction prose).
2. **Does it actually close the gap it names?** Does "(in full)" placed on the evidence
   commit SHA carry the same escrow requirement the v1 bullet's "in full" carries — and is
   the wording consistent with the v1 bullet it mirrors?
3. **Contradiction check.** Does it conflict with anything it does not amend — the v1
   custody-chain bullet above, or the rest of the successor section?
4. **Over-promise check.** Does it raise a promise the product does not keep? It should be
   *tightening a requirement* (dispatch the full SHA), not asserting a new guarantee.
5. **Clean in context.** Does the sentence still read correctly with the insertion, and is
   there anything in the amendment beyond the two-word change that the executor's framing
   above did not mention?

## Reporting

An instruction-layer checkpoint read, not a product review: report a verdict (clean / or
findings with a minimum fix each) plus any residual uncertainty. A non-blocking nit is
stated as a finding, not inflated. If clean, say so plainly — that is what discharges the
rule-1 obligation and unblocks the amendment for use.
