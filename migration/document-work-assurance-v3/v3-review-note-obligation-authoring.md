# Review-side note — the obligation-authoring gap

**Status: authored by the review side, uncommitted, not a node artifact, bears on no verdict.**
Committing it is the execution session's act, not the reviewer's. It sits at the migration root,
outside every node's `N<n>/**` allowlist, for the same reason the two agent contracts do.

Raised out of the V3-N2 FULL/VERIFY rounds but **not** a finding against V3-N2: nothing here
violates an N2 acceptance ID or a signed contract clause. N2's own acceptance is met. This is a
property of the **product** (what v3 does to document work), located upstream of everything N2
built, and it has never been claimed by any acceptance ID at any node.

---

## 1. The property that is not measured

Every obligation declares a closed `verification_mode`:

| mode | meaning |
|---|---|
| `local_check` | judged by a deterministic script |
| `local_check_and_review` | script **and** human/agent review |
| `review_only` | review judgement only, no mechanical evidence |

v3 enforces **"if you declared it deterministic, produce the evidence"** — invariant 8 binds every
deterministic obligation to an exact `CheckResult`, and `views.py`'s coverage join surfaces
`NO_RESULT` when one is missing.

It does **not** ask whether the obligation *could have been* deterministic, nor whether it can be
contradicted at all. `verification_mode` is chosen by the WorkSpec author, and both failure modes
below are reached simply by choosing `review_only`.

## 2. Two distinct failure modes, often conflated

**(a) Mechanisable, but declared `review_only` — a *choice* problem.**
The incentive gradient is real and structural: `local_check` obliges the author to write a
`LocalCheckSpec`, bind it via `local_check_refs`, and obtain a `CheckResult` that — by
invariant 5/7 — cannot carry the executor's own name. `review_only` costs none of that. The
requirement is still falsifiable; it is just no longer falsified by anything reproducible.

**(b) Worded so that nothing could falsify it — a *wording* problem.**
Example contrast, both legal, both `review_only`, structurally identical to every check in v3:

```
obl-A  "every internal link between the two notes resolves"     review_only
obl-B  "the document reads well"                                review_only
```

obl-A can be refuted by a diligent reviewer (find one broken link). obl-B cannot be refuted by
anyone, however honest or careful — no fact conflicts with it. It is not a requirement; it is an
impression that occupies a requirement's slot and consumes a `SUPPORTED` disposition.

(b) is the worse of the two: (a) degrades the *kind* of evidence, (b) removes the possibility of a
negative outcome entirely.

## 3. Why prose alone is only half a fix

The two have different causes, so they need different instruments:

- **(b) is caused by not having thought about it.** A competent author who reads one worked
  counter-example will fix it. Role-instruction prose is on-target.
- **(a) is caused by effort.** The author *knows* a script is possible; that is exactly why the
  cheaper declaration is attractive. Prose does not move an incentive.

**Prose treats ignorance, not effort.**

## 4. The shape that would work, in the product's own idiom

v3 already uses one move twice, and it is not prose — it is the schema forcing a companion field
that a hollow entry cannot honestly fill:

| existing precedent | rule |
|---|---|
| `instructionUnit.classification: context` | `if/then` **requires** `rationale`, and forbids `obligation_ids` — *you claim this needs no obligation, so say why* |
| `finding.blocking: true` | **requires** `candidate_locator` + `ground_truth_locator` + `minimum_fix`; the schema's own words: *"A blocker names where it is, what it violates and the smallest fix — or it is not a blocker"* |

The two corresponding moves:

- **(a)** `verification_mode: review_only` → **require a stated reason why a deterministic check is
  not possible.** Identical in shape to `context → rationale`. It does not forbid the cheap path;
  it puts one mandatory sentence on it.
- **(b)** every obligation → **require a stated condition that would make it `NOT_SUPPORTED`.**
  This is the mutation question asked at authoring time: *break it — what does that look like?*
  "every internal link resolves" answers easily; "reads well" cannot be answered, and the
  inability to answer is the signal — surfacing to the author, before review, not after.

Neither requires judging whether a requirement is *good* (not mechanisable). Both only require
checking that a field is present and non-empty (mechanisable). The difficulty falls on the author,
where a hollow entry exposes itself.

## 5. Hard constraint on doing it

`ResearchSystem/schema/document-assurance-v3/document-work-spec.schema.json` is an **N0 signed
schema**. Signed bytes are never modified (execution contract hard rule 5) — this is the same wall
V3-N2 hit at its own `SPEC_GAP` on the schema-directory pin. So neither change above is a small
edit: each needs an explicit out-of-node amendment (the `8efe3e9` pattern) or a post-v3 revision.

Doing that on a hypothesis is what this project repeatedly declines to do (N2-R4 is parked on
V3-N3 for exactly this reason: *inventing that coupling without a witnessed case would be
speculative*).

## 6. Recommended sequencing

1. **Now, zero-cost and in-boundary:** treat it as a *reading* obligation, not a new mechanism.
   The raw signal is already on the table — `verification_mode` is required, closed, and printed
   per row by the coverage view. Nobody is currently asked to look at that column.
2. **Now, if anything is written:** a worked counter-example for **(b)** in the WorkSpec-author
   role instructions (`EXECUTION.md` or its successor). It touches no signed byte, costs almost
   nothing, and treats the half that prose can treat. It must not be presented as covering (a).
3. **V3-N3:** the shadow runs are the witnessed-case test. The concrete question to carry in —
   plan §9's N3 measure list already asks for `obligation omissions` and `unused mechanisms`:

   > **What fraction of this run's obligations are `review_only`, and how many of those could a
   > script have verified?**

   A real occurrence is the evidence that justifies amending a signed schema. No occurrence is
   the evidence that it should not be built.

## 7. Honesty boundary

An earlier oral form of this note over-claimed that v3 "cannot distinguish a checked `SUPPORTED`
from a hollow one". That is too strong and is withdrawn: `verification_mode` plus the
`NO_RESULT` column *do* make the category visible. The accurate claim is narrower — **within the
`review_only` class**, a falsifiable requirement and an unfalsifiable one are structurally
identical to every mechanism in v3.

Consistent with contract §1, this is a **property that is not measured**, not a property that is
violated. v3 promises bounded assurance and visibility, never guarantee; `review_only` is a
legal designed mode and `UNVERIFIABLE` is a first-class disposition. What is proposed above only
extends what is *made visible* — it does not raise the promise.
