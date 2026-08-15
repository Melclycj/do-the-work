# VERIFY — `af2905c..f054a08` (instruction-layer amendment round: review fix)

**Verdict: `REVIEWED_NO_BLOCKER`.** All three accepted findings are paid. Four non-blocking
findings and three observations below; one of them corrects a sentence in my own FULL.

---

## 1. What this round is, re-derived

```
$ git log --oneline af2905c..f054a08
f054a08 V3-E10-E2-AMENDMENT-REVIEW-FIX-v1
9db2313 V3-REVIEW-RECORD-E10-E2-AMENDMENT-af2905c-v1

$ git diff --name-status af2905c..f054a08
M	.goals/plans/harness-digest-narrowing.plan.md
M	ResearchSystem/HARNESS-LEDGER.md
M	ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md
A	ResearchSystem/migration/document-work-assurance-v3/v3-review-full-af2905c.md

$ git rev-parse HEAD          f054a08bd0961d6c2198762c93f8eb3e83a70a9b
$ git status --porcelain      ?? ResearchSystem/docs/
```

This is the **targeted VERIFY** of the instruction-layer amendment round: `af2905c` was the
candidate, my FULL returned `CHANGES_REQUIRED` (record committed at `9db2313`), and `f054a08` is
the round's one user-approved fix, which under E9 obliges this VERIFY. Budget after this: spent.

**Approved fix boundary**, as the fix states it: the two blockers plus F-1, *"which the reviewer
named as the one non-blocking finding the fix round should carry rather than rediscover"*, with
F-2 / F-3 / F-4 / F-5 untouched. The user's approval of that boundary is chat-only; I state the
ceiling and move on (R7). What I can check is that the diff does not exceed it, and it does not.

**Scope of a VERIFY (R3/R4).** The accepted findings, the whole repair diff, and the permanent
boundaries. This is not a re-certification of the round, and I did not re-read the three clauses
as text — that judgment stands where the FULL left it.

---

## 2. The three accepted findings

### B-1 — paid, and the fix found one erratum more than the FULL did

The corrected inventory now appears in both places the FULL named:

- `HARNESS-LEDGER.md:105-113` — C1.7's scope restated as **M-1** (the record's only must-fix,
  §4 naming `instruction_ref` a `digestRef` when it is a `frozenFileRef` with nothing requiring
  or checking a digest) plus **L-1** in the same batch, with the four observations noted.
- `.goals/plans/harness-digest-narrowing.plan.md:197` — *"1 must-fix（`M-1`）/ 1 low（`L-1`）/
  4 observation"*, with the superseded figures explicitly voided in place.

Both match the record's own headings, which I re-derived rather than accepted:

```
$ grep -n "^### " …/v3-checkpoint-read-6e30c07.md
128:### M-1 (must-fix) …    190:### L-1 (low) …
$ grep -rn "R-1\|R-2" …/v3-checkpoint-read-6e30c07.md
(no match)
```

**L-1's substance, re-derived independently.** The ledger now asserts eight, split 5 + 3:

```
$ git show --name-status cf51534
… ResearchSystem/assurance/runs/p3-corr/issues/  6 issue-*.json + 5 user-decision-triage-*.json
… ResearchSystem/assurance/runs/w1-r1/issues/    3 issue-*.json + 3 user-decision-triage-*.json
```

Nine issue documents, **eight** triage decisions (five under `p3-corr`, three under `w1-r1`).
The ledger's number and its split are both correct.

**Errata.** The fix names three commit bodies carrying the wrong figures — `17e2b65`, `6618b84`,
`af2905c` — where my FULL named two. I checked the third myself and it is right: `17e2b65`'s body
states *"Findings are tiered 2 must-fix, 3 low, 4 observation"* and describes R-1 and R-2 at
length. I then swept for a fourth and found none; the strings survive in tracked text only inside
the void declarations and inside my own FULL record quoting them.

**Provenance, which R2 required.** The fix writes it down: the figures came from a conversational
relay that the execution side put into the ledger, the plan and three commit bodies without
checking them against the record. One measurement makes that account exact rather than merely
plausible, and it is the sharpest fact in this round:

```
$ git show 17e2b65:…/v3-checkpoint-read-6e30c07.md | sha256sum
847af38e2cc9753e01dda42875bb832705baced8147c72a14457aa50db4272c0
   claimed in 17e2b65's body: 847af38e2cc9753e01dda42875bb832705baced8147c72a14457aa50db4272c0
```

The same commit body that describes findings the file does not contain publishes a **correct**
digest of that file. The defect was never a missing or mis-transcribed record; it was a narrative
written beside a file the same commit was hashing.

One part of the disposition over-reaches — see **V-b**, which also corrects my own FULL.

### B-2 — paid on both halves, which is the right shape

E2 now reads (`CONSTRUCTION-CHECKLIST.md:23-26`):

> … existing N0 schema files, and the **signed bytes** under `ResearchSystem/contract/` — signed
> by any instrument, contract or amendment alike — because the source rule froze *signed bytes*
> by category (`7011916` rule 5: approved plan, contracts, N0 schemas), never a directory …

That is the first of the two fixes the FULL offered, and it is the better one: it matches hard
rule 5's category and the banked V-b's wording, and it needs no enumeration, so the class of
defect that produced B-2 cannot recur through a stale list. The `UNSIGNED successor … falls to
E10's read path` clause is preserved word for word, so the round's own purpose survives the
repair.

The derived statement was corrected too (`HARNESS-LEDGER.md:92-97`): the false enumeration is
quoted, marked **假的**, and replaced by the correction naming
`amendments/2026-07-18-a1-p4-scoped.md` as signed and **inside** the frozen surface. Doing both
halves rather than either is correct and the fix's reason is the right one — E2's closing sentence
makes a derived boundary non-authoritative, which is exactly why the derived sentence that
*scopes* the rule had to be corrected rather than out-ruled.

The signed file is untouched by the repair:

```
$ git show HEAD:…/amendments/2026-07-18-a1-p4-scoped.md | sha256sum
2d672d0d329e845cc598ff6089b3fa460118c382a66cb67635c910652e23f04c   (= the recorded signed digest)
```

**What the repair does not change, and should not be read as changing.** `block-grammar.md`,
`content-roots.yaml` and `baseline/P0-baseline.md` self-declare *FROZEN at P0*, are not signed,
and remain outside E2 — as they were under the source rule. That was O-3 of the FULL, reported and
not concluded; it is unchanged here.

### F-1 — paid; the guard is now decidable at the case that needed it

E10 now carries (`CONSTRUCTION-CHECKLIST.md:72`):

> — relied means took its governance from it, which authoring, citing or recording it is not —

I re-ran the grep that produced the finding. `assurance_state.py:113` is a docstring round C1.6
wrote, citing supersession-2 as superseding supersession-1 §3 — *citing or recording*, which the
qualifier now excludes by name. The decision Phase C1.7 faces is therefore answerable from the
text alone, in the direction the FULL judged better, and the difference of one FULL no longer
turns on a reader's instinct.

The fix also records, in its own body, that `af2905c` called the test *"greppable rather than
self-asserted"* and that the characterization does not hold — the right disposition, since that
body cannot be amended.

---

## 3. The whole repair diff (R3)

Four paths. Three edited, one added.

- **`CONSTRUCTION-CHECKLIST.md`** — exactly two hunks, one per finding (E2 = B-2, E10 = F-1).
  Nothing else in the file moved. Under E10's own edit rule the E2 hunk is a substitution plus an
  insertion and the E10 hunk is a pure insertion; both are permitted (*additive or subtractive*),
  and this commit body makes no claim about its edit form, so it does not repeat the
  mischaracterization F-2 recorded.
- **`HARNESS-LEDGER.md`** — the B-2 correction block, the B-1 inventory restatement, the void
  declaration and the errata bullet. All four are attributable to the approved boundary.
- **`harness-digest-narrowing.plan.md`** — one line, the resume pointer, B-1 only.
- **`v3-review-full-af2905c.md`** — my FULL record, added by `9db2313`.

**Verbatim custody of the review record.** `9db2313`'s body claims byte-identity at
`d8971ac0…`; the committed blob hashes to exactly that, the file is 448 lines as the diffstat
says, and I compared the committed text against what I authored across the whole of §4 and the
start of §5, plus every heading, the verdict line and both counts — identical, including the two
minimum-fix paragraphs. Nothing was softened and no response is embedded in it.

**Out-of-boundary work: none.** F-2, F-3, F-4 and F-5 are verifiably untouched — the two ledger
bullets are still a second copy of each other with item ① still described two ways (F-4), and the
bank list at `:57-63` still carries `VERIFY-②` as open while `:99` says it is paid (F-5). Both were
declared out of scope and both remain exactly as the FULL found them.

**Budget.** The fix could not have escaped this VERIFY through the clause it repaired: the
convergence clause is scoped to *a read's* must-fix findings, so a FULL's blockers still oblige a
targeted VERIFY under E9. The fix says so and it is right — I re-derived the reading rather than
accept it.

---

## 4. Permanent boundaries (R3 — however narrow the round)

Measured at `f054a08` with nothing changed after:

```
document_harness            Ran 151 tests   OK
document_harness_review     Ran 325 tests   OK
harness                     Ran  39 tests   OK
stage_control               Ran  20 tests   OK
tests/run_tests.py          tests: 29   passed: 29   failed: 0
repo-audit.py               RESULT: clean (exit 0)      [run from the repository root]

git rev-parse HEAD:…/document-work-assurance-harness-v3.plan.md   8ad404b12b32…
git rev-parse HEAD:…/Document-Work-Assurance-Contract-v3.md       b2dbdf752d8c…
git rev-parse HEAD:…-supersession-1.md                            68031fa2ca31…

git diff --stat af2905c..f054a08 -- ResearchSystem/contract ResearchSystem/schema \
    ResearchSystem/assurance ResearchSystem/tooling \
    .goals/plans/document-work-assurance-harness-v3.plan.md
(empty)
```

The empty diff covers both user-locked oracles. Every figure the fix reported reproduces exactly.
As the FULL said and the fix repeats, a green suite is weak evidence about a prose payload; it
establishes that nothing else broke, not that the payload is right.

---

## 5. Non-blocking findings

**V-a — the live pointer still says the FULL has not happened.** `HARNESS-LEDGER.md:85` still
reads *"指令层 amendment 轮已落候选，等 FULL + 它自己的 read"*, and the fix edited that very bullet
without touching its headline. The FULL has returned `CHANGES_REQUIRED`, the one fix is spent, and
what is now pending is this VERIFY plus the owed read. The reason this is worth a line rather than
none: E9's accounting turns on *"has a valid independent FULL already occurred?"*, and the pointer
a fresh session reads first now answers **no** where the answer is **yes, and the repair is
already spent**. The closeout is where this bullet is rewritten into the `CLOSED` form the file
uses for every earlier phase, so the fix is that the closeout does it — but until then the live
pointer contradicts the repository.

**V-b — the void declaration over-reaches, and so did the sentence of mine it rests on.**
`HARNESS-LEDGER.md:110-113` declares *"先前写的 `R-1` / `R-2` / 「2 must-fix / 3 low」全部不成立"*
— none of it holds — on two grounds: that the strings are absent from the record (true, and
sufficient for the labels and counts), and that the two subjects were in that record *verified
clean* and *`UNVERIFIABLE`* respectively.

The second ground does not carry the weight put on it, and my FULL's B-1 phrased it the same way,
so this corrects both. What changed my view is a document I had not read when I wrote the FULL:
`17e2b65`'s **commit body**, which I opened for the first time in this VERIFY to check the third
erratum. It describes R-1 as *"section 2 calls `pointer_for` the documented authoring path in the
present tense … the B-3 repair added a qualifier about a newly opened run but left the main clause
global"*. The record's verified-clean entry is *"the §2 qualification about **`pointer_to`** is
exhaustive"* — a different sentence of §2, about whether the concession enumerates all direct
`pointer_to` callers. Supersession-2 §2 does contain both: a global prescriptive main clause about
`pointer_for` and a scoped concession about `pointer_to`. Likewise for R-2: the record marks §3's
forward statement `UNVERIFIABLE` because no run has opened, which answers *can this be checked*,
not *is "newly opened" definable* — the question the body raises.

So the accurate disposition is narrower than the one committed: **the labels, the counts and the
claim that the record supports them are void; the substance described in `17e2b65`'s body has been
adjudicated by no committed review instrument at all.** Whether it deserves adjudication — and
whether C1.7 should carry it beside M-1 — is the user's question, not mine (R5). I record only
that "全部不成立" currently forecloses it, and that a one-line change to that sentence
(*"as findings of that record they are void; their substance is unadjudicated"*) would keep the
correction intact while leaving the question open.

**V-c — E10's new qualifier consumes the contrastive dash.** The clause now runs *"…for as long
as no round has relied on the text — relied means … is not — once one has, changing it opens a
round;"*. Before the fix the single dash introduced the contrast; the parenthetical's closing dash
now takes its place and the final clause follows unpunctuated. Meaning is unaffected and
recoverable on one reading. Wording-level under R9: no actor's action changes. Rides the next
batch touching this layer, which is the batch the owed read may open anyway.

**V-d — the round's remaining findings live only in commit bodies and one review record.** F-2
through F-5 and the six observations are currently tracked in `9db2313`'s body, `f054a08`'s body
and `v3-review-full-af2905c.md`; no ledger bullet or bank entry carries them. That is the same
custody shape whose failure produced B-1, on the same day, in the same round. The closeout is the
place, and the FULL's observations are the user's under R5, so this is a note about where they are
written down rather than a claim that any of them is unresolved.

---

## 6. Observations (R5 — reported, the conclusion is the user's)

**O-A — the round closed the loop its own defect opened, and the loop is short.** B-1's root
cause was an unread record; the fix's own account says the record *"was on disk at the time and
had just been committed verbatim by the same session"*, and `9db2313`'s body volunteers that the
FULL record *"was read in full before this commit was written, which is the discipline whose
absence produced blocker B-1"*. Recorded as the shape it is, not as a conclusion about whether the
discipline needs an instrument behind it.

**O-B — the owed E10 read has moved onto the repaired bytes.** O-5 of the FULL anticipated this
and the fix confirms it: the read this round owes is now owed on `f054a08`'s checklist, not on
`af2905c`'s. Neither the FULL nor this VERIFY may be banked as it. That is the same sequencing
C1.6 met when `293f657` changed supersession-2 after its FULL.

**O-C — three instruments now disagree about what read `17e2b65` found, and only one of them is
the read.** The record, the commit that carries it, and the ledger each said something different;
after this fix the ledger and the record agree and the commit body is named as erratum. The
residue is that a commit body can carry a finding inventory at all — nothing binds it to the file
it commits, as the matching digest beside the mismatched narrative shows.

---

## 7. Coverage (R4)

- **Read in full:** the whole repair diff; `f054a08`'s and `9db2313`'s commit bodies;
  `17e2b65`'s commit body; `HARNESS-LEDGER.md:85-124` at HEAD; the repaired E2 and E10 text;
  supersession-2 §2 and §3.
- **Re-read against my own authored text:** `v3-review-full-af2905c.md` §4 in full and §5 through
  F-2, plus every heading, the verdict and both counts.
- **Sampled:** `v3-checkpoint-read-6e30c07.md` — its finding headings, its verified-clean entries
  for §2, and its R4 coverage paragraph. I did **not** re-read the record in full this round.
- **Ran myself, output above:** the five suites; `repo-audit.py`; the three frozen-blob resolves;
  the A1 amendment digest; `git show --name-status cf51534`; the two sha256 custody checks; the
  boundary diff; a tracked-text sweep for the superseded figures.
- **Not run, not owed:** mutation probes. The repair adds no guard and no executable byte, so E4 /
  E5 / R8 remain vacuous against it.
- **`UNVERIFIABLE` (R4, R7), not folded into supported:** the user's approval of the fix boundary;
  whether the reading session ever produced findings labelled R-1 and R-2 — I can establish only
  that the record does not contain them and that `17e2b65`'s body describes them; and any claim
  about the execution session's context. `V-b`'s question — whether the substance behind those
  labels is a real defect in supersession-2 — I deliberately did not settle: it is outside a
  VERIFY's subject and, under R5, outside a reviewer's conclusions.

---

## 8. Verdict

**`REVIEWED_NO_BLOCKER`.**

B-1 is paid, with the inventory corrected in both files, C1.7's scope restated as M-1 plus L-1,
L-1's number independently re-derived as eight, and the errata extended to a third commit body the
FULL had not found. B-2 is paid on both halves, and the wording chosen — *signed bytes … by any
instrument, contract or amendment alike* — removes the enumeration that made the defect possible
rather than correcting one entry in it. F-1 is paid by a qualifier that makes the next round's
decision answerable from the text. The repair stayed inside its approved boundary, the four
findings left outside it are untouched exactly as declared, every reported figure reproduces, and
the permanent boundaries — the three signed blobs, the schema, contract, assurance and tooling
trees, both user-locked oracles, and the signed A1 amendment's bytes — are unchanged.

Two things go to the closeout rather than to a round: the live pointer still says the FULL is
pending (V-a), and the round's remaining findings are written only in commit bodies and the review
record (V-d). One thing goes to the user: the void declaration, and the sentence of my own FULL it
rests on, dispose of substance that no committed review instrument has adjudicated (V-b) — the
labels and counts are correctly void, the substance is unadjudicated, and which of those C1.7
should carry is not a reviewer's call.

And the read E10 owes on this layer is still owed, now on the repaired bytes. This VERIFY is not
it and cannot be banked as it.
