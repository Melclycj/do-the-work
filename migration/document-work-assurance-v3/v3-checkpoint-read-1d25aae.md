# Amendment checkpoint read — `1d25aae` (`V3-CONTRACT-SCOPE-DISCIPLINE-AMENDMENT-v1`)

The rule-1 / §12 checkpoint read the amendment itself declares it owes. **Not a round in §3's
sense:** it consumes no plan-§8 budget and carries **no verdict** — findings only, tiered
must-fix / low / observation. Its authorization is the `ADOPT_DOCUMENT_V3` standing-discipline
entry (N3 record §8; N3-R10), not my own initiative.

**Subject:** the amendment text, read as the subject rather than as a manual. Both files:
execution contract +53/−0 ("Scope discipline", two rules), review contract +29/−0 (hunt-list
item 8, a §10 ceiling). No earlier line changed in either.

**Yield:** 6 findings in 82 added lines. The §12 precedent is 3 defects per 79 careful lines;
this is roughly double, and the concentration is worth naming — the *rules* are sound and I
would adopt both unchanged, but nearly every **factual claim about the record that justifies
them** is overstated in the same direction. That direction matters: this layer has no
mechanical binding, so a number written here is what a later round will cite as established.

---

## Findings

### C1 — must-fix — "every one of that artifact's findings existed only to hold churn up" is not true

**Locators:** execution contract, Scope discipline rule 1, ratchet paragraph, verbatim —

> Every one of that artifact's findings existed only to hold churn up

and its counterpart, review contract §10, verbatim —

> eleven findings across two reviews, of which **five existed only to hold up one derived
> field**

**Derivation, finding by finding** (from the two committed reports):

| Finding | What it was about | Caused by churn? |
|---|---|---|
| F1 | the construction renderer had no anti-anchoring guard, and already leaked `commit_count` | **no** — the mutation that exposed it was a generic sentence; the concrete leak was the commit count |
| V1 | the partition guard is one-directional | **no** — that guard existed to fix F1; its directionality is independent of what it guards |
| V2 | index drift through the sliced constant | **yes** — the slicing existed because the churn section was conditional and its caveat doubly so |
| V3 | `assertIn("2", …)` in the commit-count test is vacuous | **no** — the commit count, not churn |
| V4 | `merge_count` fails open into "no merge" | **yes** — `merge_count` exists only for churn's caveat |

Two of five are clearly churn-caused. The category the rule actually names — *derived
supplements* — does cover all five, and rule 1's own headline ("Derivability is not a reason
to derive") is stated at exactly that level. The overstatement is only in the evidence
sentence.

**Minimum fix:** replace "churn" with "a derived supplement" in both sentences, or state the
split. The rule survives either way; the ratchet argument does not need "every one" to hold.

### C2 — must-fix — F1 was fixed, not made moot

**Locator:** review contract §10, verbatim: *"all five made moot rather than fixed when the
field was deleted"*; and `c6d4eb4`'s own message, *"Deleting churn makes all five moot rather
than fixed."*

The sequence in the repository is:

1. FULL of `4440fa2..0439efe` → F1–F7;
2. **fix round `9956231` + `d55d5ce` → F1 fixed** (structural guard built; `commit_count`
   dropped from the reviewer prompt by user ruling), along with F2, F3, F6;
3. VERIFY of `0439efe..d55d5ce` → V1–V4, all raised *against the fix*;
4. deletion round `c6d4eb4` → V1–V4 mooted.

So four were mooted and one was fixed a round earlier. This matters to the ratchet argument
rather than weakening it: F1's fix is precisely the machinery whose additions then earned
V1–V4, which is the ratchet, stated correctly.

**Minimum fix:** "the four VERIFY findings made moot" and F1 named as fixed-then-superseded.

### C3 — low — the component count undercounts, against the round's own argument

**Locator:** rule 1, verbatim: *"Five components were added to close two findings, and **four**
were deleted one round later; that ratio was the alarm."*

Counted mechanically off the diffs. The fix round added five: `merge_count`,
`CONSTRUCTION_FIXED_LINES`, `_MERGE_CAVEAT`, `construction_subject_line`, and the partition
guard test. `c6d4eb4` deleted **all five** — the only surviving mention of any of them is one
explanatory comment at `test_dispatch.py:391`, not code.

The true ratio is five of five, which is a stronger alarm than the one written.

**Minimum fix:** "and all five were deleted one round later".

### C4 — low — the guard defect shipped once, not three times

**Locator:** rule 2, verbatim: *"The same defect shipped three times in one day, each looking
stronger than the last"*, then a list whose third entry is *"a hand-written literal, against
which five probes went red."*

Two problems in one sentence:

- **The third entry is the fix, not an instance of the defect.** A list of three occurrences of
  "the same defect" whose last member is the thing that cured it will be misread later.
- **"Shipped" is wrong for the second.** Only the partition allowlist reached a commit
  (`9956231`). The `CONSTRUCTION_PROMPT.format(...)` version never did — `c6d4eb4`'s own
  message says it was "caught only by re-running the reviewer's probes", and the range
  `d55d5ce..c6d4eb4` contains exactly one code commit, so there was no commit for it to ship
  in.

**Minimum fix:** "The same defect was built twice in one day, each looking stronger than the
last — shipped once, caught pre-commit the second time — and cured on the third attempt by a
hand-written literal, against which five probes went red."

### C5 — low — the two counterpart edits disagree about what a review may raise

This is a counterpart pair, so agreement between them is the property that makes the pair
worth having.

- Execution contract, rule 1, verbatim: *"**a review is structurally incapable of raising
  it.** A reviewer's subject is always the code that exists, so no finding will ever say
  *delete this*. Both reviewers were exact and neither could have."*
- Review contract §10, verbatim: *"**When successive rounds on one artifact keep adding
  components to close findings, say so as an observation.** I cannot conclude it should go; I
  can report the shape…"*

One says the reviewer cannot raise it; the other instructs the reviewer to raise the shape of
it. The review-side wording is the correct one — raising and concluding are different acts,
and the review contract's own tier vocabulary (§13) has an observation tier for exactly this.
As written, an execution session reading only its own contract would treat a reviewer's
ratchet observation as out of role.

**Minimum fix:** on the execution side, "a review is structurally incapable of **concluding**
it… no finding will ever say *delete this*", and drop or qualify "neither could have".

### C6 — low — "both reviewers did exactly that" rests on half the evidence claimed

**Locator:** rule 1, verbatim: *"so a supplied list **must be recomputed by its recipient**,
and both reviewers did exactly that."*

The FULL was supplied a six-path churn list and recomputed it independently — that half is
solid and is in its report's recompute list. **The VERIFY was supplied no list at all:** its
range contained no churn, so the prompt carried no Churn section. It recomputed the quantity
anyway (finding it empty) and separately re-derived the *previous* range's list as a
regression check.

The claim is defensible but the evidence for "both" is weaker than the sentence implies, and
the sentence is load-bearing for rule 1's central argument.

**Minimum fix:** "…and the one reviewer who was supplied a list recomputed it; the other
recomputed the quantity unprompted."

---

## What I checked and found sound

Stated by dimension, because a silent dimension is indistinguishable from an unchecked one.

- **Additive-only, as claimed.** `git diff --numstat` gives 53/0 and 29/0. No earlier line
  changed in either file; hard rule 4 is cross-referenced, not edited — verified by reading it
  at tip (`v3-harness-operating-contract.md:127-130`), and the characterisation of it (*says
  how to detect a powerless guard, not how to avoid building one*) is accurate.
- **Both quoted sources are verbatim.** §8's opening reads *"**One commit SHA. Nothing else.**
  Everything else I read from the repository myself: the plan's node section…"* — the
  amendment's truncation at "myself" is faithful. §5.1 does forbid accepting a reported number,
  in those terms.
- **"eleven findings across two reviews"** — recounted: F1–F7 (7) plus V1–V4 (4). Correct.
- **"built 2026-07-25 and largely deleted 2026-07-26"** — `43ea599` is 2026-07-25 23:18,
  `c6d4eb4` is 2026-07-26 02:51. "Largely" is right: the construction half survives as a
  constant prompt and three checks.
- **The DAG argument is correct and I verified it myself** at the VERIFY: count the merge and a
  path revised once on the merged branch is reported as churn; do not and the merge's content
  is invisible; there is no third answer.
- **Item 8's account of the guard shape is accurate**, including that the second instance sat
  inside the fix for the first, and that both instances were in the same file. Its instrument —
  *mutate, and green is the finding* — is exactly how V1, V2 and G1 were found, and it is the
  most useful sentence in the amendment.
- **The `assertIn("2", …)` example is accurate.** That is V3, and I proved it by removing the
  `commits` line entirely from the dispatcher view and watching the test stay green.
- **Both provenance notes correctly flag the owed read**, in the right shape — they state what
  is owed, not that it was done. Neither asserts a satisfied state about itself.
- **No instruction-layer rewrite (§6.7 / discipline rule 3).** Purely additive, two new blocks,
  nothing re-typed.
- **Nothing mechanical moved.** `repo-audit` exit 0; `pytest` still 426. Correct for an
  instruction-only change, and the point of discipline rule 3 — a green suite is not evidence
  about this layer.

---

## Observations — no fix owed

1. **The §10 ceiling creates a real new obligation on me**, and its start date should be
   unambiguous: *"When successive rounds on one artifact keep adding components to close
   findings, say so as an observation."* My FULL of `d55d5ce..c6d4eb4` was authored before this
   amendment existed and is not bound by it; it endorsed the deletion and corrected my earlier
   position on churn, but it did not state the ratchet as an observation. From this read
   forward I will.
2. **The amendment's evidence links point at two committed reports**
   (`v3-review-full-0439efe.md`, `v3-review-verify-d55d5ce.md`). The third,
   `v3-review-full-c6d4eb4.md`, is still **untracked** — the round it reviews has an unspent fix
   and VERIFY. Not a defect in the amendment; recorded because C1–C4 are all claims about
   findings whose full record is not yet in the repository.
3. **Yield rate.** Six findings in 82 lines against the §12 precedent of three in 79. All six
   are factual claims about the record rather than defects in the rules themselves — which is
   itself the finding worth carrying: this amendment argues from a history the writer had just
   lived, and lived history is exactly where a writer stops checking.

---

*Authored by the review side. Not a node artifact; outside every node allowlist; bears on no
verdict. Committing it is the execution session's act, not the reviewer's.*
