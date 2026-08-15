# Review-side note — the instruction layer has no custody

**Status: authored by the review side, uncommitted, not a node artifact, bears on no verdict.**
Committing it is the execution session's act, not the reviewer's. It sits at the migration root,
outside every node's `N<n>/**` allowlist, for the same reason the two agent contracts do.

Produced 2026-07-21 at the user's request, by reading the v3 **prose layer** cold — not out of any
node's review round. It names **no acceptance ID**, and nothing below is a finding against N0, N1,
N2 or N3: no acceptance ID or signed clause is violated by any item here. Like
[`v3-review-note-obligation-authoring.md`](v3-review-note-obligation-authoring.md), this is a
**property of the product** that has never been claimed at any node.

It is written to be **self-contained for a reader with zero shared context** — the execution side
does not share this session's context, so the reasoning is included, not just the conclusions.
Read §7 first if you only need the routing.

---

## 0. What was read, and what was not

| Read **in full** | Lines |
|---|---|
| `ResearchSystem/document-harness/README.md` | 29 |
| `ResearchSystem/document-harness/EXECUTION.md` | 92 |
| `ResearchSystem/document-harness/REVIEW.md` (at `c07d682`) | 214 |
| `ResearchSystem/contract/Document-Work-Assurance-Contract-v3.md` | 255 |

**Not read in full:** `.goals/plans/document-work-assurance-harness-v3.plan.md` (712 lines) — the
largest prose artifact, and the one the contract calls *"the locked design authority"* for
V3-D1–D10. It was only searched by keyword. **So this note does not cover whether the plan holds a
fourth statement of any rule discussed below.** That is the main coverage gap in it.

Line references are against the working tree at `c07d682`. Where a line number is cited it was
re-derived at that revision; earlier drafts of this analysis used the `eca4902` numbering, which is
offset by one after L140.

`C1`–`C5` below are **note-local labels only**. They are not register IDs and must never be
referenced as acceptance IDs.

---

## 1. The core property: no mechanical binding, and no scheduled read

v3 has three enforcement mechanisms. Every one of them operates on **JSON instances**:

| Mechanism | Binds |
|---|---|
| JSON Schema (8 schemas under `schema/document-assurance-v3/`) | the structure of data objects |
| 316 v3 tests across two suites (113 `document_harness` / 203 `document_harness_review`) | code behaviour |
| `check_review_result` + the coverage joins in `views.py` | result completeness |

(The executor's regression set runs five suites — 404 tests, 113 / 203 / 39 / 20 / 29 — but the
other three suites bind sibling products: harness-v2, stage-control v1, the P2 compiler. v3's own
mechanical surface is the 316.)

**Not one of them reads `REVIEW.md`, `EXECUTION.md`, `README.md`, or the contract prose.**

This is not inference. It was measured twice:

- `eca4902` changed **79 lines** of `REVIEW.md` (+79 / −24) and three schema `description` strings
  → all five suites green, **zero test edits**.
- `c07d682` changed a further **13 lines** (+13 / −12) → all five suites green, zero test edits.

The only occurrence of a prose filename anywhere in `tooling/` is a **docstring citation** at
`tests/document_harness_review/test_package_and_review.py:806`. It tests JSON-level behaviour
(that both the disclose and the stop route stay reachable); it does not read the file.

So a defect in the instruction layer can be caught by exactly one thing: **an independent human or
agent reading it.** And there is no scheduled such read of the instruction layer itself:

- an independent FULL review's subject is **one product run's work**, not the harness's own role
  instructions;
- [`v3-harness-review-contract.md`](v3-harness-review-contract.md) §7 forbids requiring the
  unfinished harness to certify its own construction (plan §8).

Every instruction-layer defect caught before this note — the **five** that shadow round 2
exposed (N3-R6, N3-R7 (i), N3-R7 (ii), N3-R8, the disposition-boundary ambiguity) — was found
**incidentally**: three by round-2 reviewers tripping over them while reviewing a product run
(R7 (i)+(ii) by both reviewers independently; R8 by run-p3's reviewer failing to reproduce the
digest), and two by the execution side comparing the two reviewers' outputs afterwards (R6; the
disposition split). Not one came from a read whose *subject* was the instruction layer. That is
incidental discovery, not coverage.

**The instruction layer is the only layer of v3 with zero mechanical binding and zero scheduled
review, and it is simultaneously the layer that decides what every human and agent in the system
does.** That asymmetry is the subject of this note. The individual wordings below are its
symptoms.

---

## 2. The five defects

### C1 — `README.md` contradicts itself and is three nodes stale

**Evidence.** `README.md` L8–10:

> **Status: V3-N0 CLOSED — … V3-N1 is not yet authorized and no runtime exists yet.**

The **same file**, L20–24, links *"Evidence schemas (**V3-N1**)"*, *"Review + disposition schemas
(**V3-N2**)"*, *"**N1** administrative record"*, *"**N2** administrative record"*.

Reality: N1 and N2 are both closed and user-signed; N3 is open; a runtime exists with 316 tests.
Last touched at `0ba649c` (V3-N2) — **that node updated the table and not the banner**.

**Root cause.** Nothing derives the banner. It is hand-written state in a file that no node owns:
`document-harness/README.md` is outside the N1–N3 allowlists, so every node *may* leave it alone
and every node *did*.

**Class.** Pointer drift. This is the **second file** to exhibit the same failure mode —
`.goals/LEDGER.md` had drifted in four places by V3-N2 (reported in
[`v3-review-handoff-2026-07-21.md`](v3-review-handoff-2026-07-21.md) §1, since repaired) — five
drifted state assertions across two files. Two independent instances of one mechanism failing is
a pattern, not an accident. *(While this note was being handed off, a **third file** surfaced:
the repo-root `CLAUDE.md` / `AGENTS.md` pair — auto-loaded into every session — still states
"There is no code, build, or tests here", false since P2 (2026-07-12), was last touched
2026-07-11, before **all** ResearchSystem work, and carries no pointer to `ResearchSystem/` at
all beyond one incidental clause naming `.goals/LEDGER.md`. Same mechanism, third surface. It is
also a **leakage-relevant** surface: being auto-injected, it can never be put on a shadow-run
ban list — so whatever is ever written there must stay purpose-only, never verdicts, rounds or
node state.)*

**The fix is subtractive, not corrective.** Correcting the banner buys one node of accuracy and
then drifts again. **Delete the status assertion**: a file that does not claim node state cannot go
stale about node state. Node state already has exactly one home per the execution contract — the
node record. The schema/record link table is structural, not state, and can stay.

### C2 — the contract violates its own rule, in its own signed bytes

**Evidence.** Contract L16–20 (a `> [!warning]` block):

> …this file **never carries its own approval status or digest**

Contract L8, frontmatter:

> `status: candidate-awaiting-user-signature`

The contract is signed; the line is both self-referential *and* factually wrong. It is patched in
prose — in a **third file** — at `README.md` L17: *"its frontmatter `status:` is an authoring
residue; the N0 record §8 errata is authoritative for approval state."*

**Root cause.** Two correct rules collide. *Signed bytes are immutable* (contract §13: corrections
create a versioned successor; execution contract hard rule 5) meets *a document must not assert its
own approval state*. The collision was resolved by adding a pointer — and the pointer was placed on
`README.md`, which is the file in this set with the demonstrated drift problem (C1).

**Class.** Self-referential prose. `v3-harness-review-contract.md` §6.6 records that this class
cascaded five levels deep at V3-N0 and was **terminated only by building a checker (R4), never by
more prose**. C2's patch is more prose.

**Disposition.** The contract itself must not be touched — issuing a versioned successor contract
for one frontmatter line is grossly disproportionate. The authoritative statement already lives in
the right place (N0 record §8). `README.md` L17 is a **duplicate of it**. Delete the duplicate and
point at the record. Same subtractive shape as C1.

### C3 — one trigger, three statements, no stage marker

**Evidence.** Three files state what happens when an instruction unit maps to no obligation:

| Where | What it says |
|---|---|
| Contract §6 (L137–141) | Before START, one `InstructionCoverageAudit`; `SPEC_GAP` requires a new WorkSpec revision and a new user START; **the audit has no repair loop** |
| `EXECUTION.md` §*When the instruction itself is the problem* (L64–69) | *"If an instruction unit cannot be mapped to an obligation or an explicit context rationale, that is a `SPEC_GAP`. It stops."* — **unconditional** |
| `REVIEW.md` §*When the map is incomplete* (L105–168) | a two-row criterion + a process-claims exemption — **conditional**: `SPEC_GAP` only if the work was never done or cannot be established at the pinned revisions, and **never** for process instructions |

These are reconcilable **by stage** — pre-START audit / during execution / post-hoc review recheck
— but **no file carries the qualifier**. A reader who reads `EXECUTION.md` and then `REVIEW.md`
sees one trigger produce two different rules with no bridge between them.

**Root cause.** The same rule was restated in three places by three different nodes, and no
mechanism compares restatements. See C5.

**Class.** This is the **same defect class as N3-R7 (i)** — one rule, two readings, no marker —
except that here the divergence is *between* files, so a round-2 reviewer could not trip over it:
the reviewer reads only `REVIEW.md`.

**C3 is the only one of the five that no script can ever catch.** All three statements are
individually legal, well-formed and internally coherent; only understanding them reveals that they
address different stages. If it is not fixed by a deliberate read, it will not be found again.

**Fix.** Additive and one line each: mark `EXECUTION.md` §*When the instruction itself is the
problem* as applying **during execution**, and `REVIEW.md` §*When the map is incomplete* as
applying to the **post-hoc recheck**.

### C4 — the contract has an escape hatch for conflict, none for silence — and a private law grew into the gap

**Evidence.** Contract L25–26:

> Plan §2 decisions V3-D1–D10 are the locked design authority; a genuine conflict between this
> contract and the plan is a `SPEC_GAP`, not a reinterpretation opportunity.

`REVIEW.md` now carries **two** self-declared local rules that resolve places where the upstream
documents are *silent* rather than in conflict:

- L167 — the collision-precedence rule: *"This precedence is stated here rather than derived: V3-D6
  and V3-D7 do not settle the collision, and a reader should treat it as this file's rule, not the
  plan's."*
- L80 — the contract-§5 reading: *"This is this file's reading of §5, stated rather than derived."*

**This is not a violation.** Under-determination is not conflict, so the contract's `SPEC_GAP`
clause does not reach these. And **both are honestly labelled**, which is genuinely good practice —
it puts the private law on the surface instead of smuggling it in. This note records it as an
observation, not a defect.

**What is worth watching.** The contract prepared an escalation path for *contradiction* and none
for *silence*; `REVIEW.md` filled that gap with a local convention, and the convention is
**growing** (one at V3-N2, two after `eca4902`). Nothing counts them, audits them, or defines the
threshold at which accumulated local readings should be folded back into a contract revision.
That threshold is a governance question for post-v3, not a defect to fix now.

### C5 — duplication without derivation

**Evidence.** The sentence *"no blocking discrepancy found within the frozen subjects and review
dimensions"* exists in **7 copies across 5 files** (whitespace-normalized count): contract §5 ×1,
`REVIEW.md` ×2 (L112, L198), `review.schema.json` ×2, the v3 plan ×1,
`v3-harness-review-contract.md` ×1. The executor-independence rule (*"cannot author check
outcomes or reviewer verdicts"*) appears verbatim in **4 files** (the plan, contract §3,
`REVIEW.md`, the construction-side review contract), plus paraphrases in `EXECUTION.md` and the
operating contract.

**Assessment, split honestly:**

- Duplicating a **fixed sentence** is cheap. The contract copy is immutable, so it functions as an
  anchor the others can be compared against — a checker could assert byte-equality.
- Duplicating a **rule** is where drift lives, and C3 is exactly that: one rule restated three times
  with **different content**, compared by nothing.

**Why this matters more than it looks.** v3's own design decision **V3-D8 / N0-A6** is that *a
second copy drifts the moment the node moves* — that is the stated reason the harness refuses to
duplicate node state anywhere. **The instruction layer is built out of precisely the duplication the
product forbids in the work it governs, on the one surface where the product does not look.**

---

## 3. Diagnosis: the disorder is custody, not content

The content is largely good. The two role files have a clean own/never-author split and each opens
with a one-sentence charter; the contract is tight and enumerable with a single home for enums; the
layering (contract = frozen interface, role files = behaviour, records = state) is right in
principle; the self-labelling convention in C4 is better than most harnesses manage.

Every defect above has the same shape — three questions that were never answered for any sentence
in this layer:

1. **Who owns this sentence?** (`README.md`'s banner belongs to no node's allowlist, so every node
   may change it and no node must.)
2. **What re-derives it?** (Nothing. All of it is hand-written.)
3. **What breaks if it goes stale, and who finds out?** (Nothing breaks; nobody finds out — §1.)

A useful restatement, in the product's own vocabulary: **the instruction layer is v3's own
`review_only` class.** It is declared to require judgement, carries no mechanical evidence, and has
nobody assigned to look at it. The question
[`v3-review-note-obligation-authoring.md`](v3-review-note-obligation-authoring.md) §6.3 asks to be
carried into the shadow runs —

> *What fraction of this run's obligations are `review_only`, and how many of those could a script
> have verified?*

— turned on the harness itself answers: **100 % of the instruction layer is `review_only`.** The
second half of that question is answered in §4, and the answer is not the one this note originally
expected.

Stated at its sharpest — the product's own prescription for assuring a document, held against
what its own instruction prose receives:

| What the product does for the documents it governs | What `REVIEW.md` / `EXECUTION.md` / the contract prose receive |
|---|---|
| One FULL review is **structural** — step 7 of the product flow, never optional | No scheduled read, ever |
| A **named reader** exists (`reviewed_by`, bound into the result) | Nobody is assigned |
| Every obligation carries a disposition; not-established is **recorded** (`UNVERIFIABLE`, coverage, `residual_uncertainty`) | Whether anyone has ever read a given section is recorded nowhere |
| Unread coverage is **disclosed** to the deciding user at FINAL | The state "unread" does not exist |

All five witnessed defects (§4) live in the right-hand column. None of this says scripts are the
wrong instrument — scripts pin the boolean facts (digest identity, locator resolution, boundary
conformance) precisely so that the reading budget is spent only where reading is the sole
instrument: meaning. That split is the product's own (`local_check` vs `review_only`; contract §7's
closing line — digests are *"never substitutes for source inspection"*). The defect is only that
**the product never applied its own remedy to the layer that steers it.**

---

## 4. What round 2 actually witnessed — and why it inverts the obvious fix

**Round 2 is complete.** Both subjects were reviewed by independent reviewers in fresh contexts:

| Run | Verdict | Findings | `instruction_completeness` |
|---|---|---|---|
| `round-2/run-a1` | `REVIEWED_NO_BLOCKER` | 6 | `INCOMPLETE` |
| `round-2/run-p3` | `SPEC_GAP` | 8 | `INCOMPLETE` |

So the witnessed cases this note needs **already exist**, and they are strong ones. Round 2 produced
**five** measured consequences of instruction-layer defects:

1. **N3-R7 (i)** — the frozen package was described as *"what you are entitled to review"* without
   saying whether that was a ceiling or a floor. The two reviewers read it oppositely, and **one of
   them states the choice materially changed its verdict.**
2. **N3-R7 (ii)** — the stop criterion (*"nothing in the frozen package can settle whether it
   was"*), read literally, made every process instruction a `SPEC_GAP`, contradicting the same
   file's *"process claims have no evidence lock"* ceiling. **run-a1's reviewer had to resolve the
   contradiction itself, and recorded that it had to.**
3. **The disposition-boundary ambiguity** — `NOT_SUPPORTED` said *"they contradict it **or do not
   reach it**"*, which overlapped `UNVERIFIABLE`. **Two real reviewers labelled the same state
   differently.**
4. **N3-R6** — `REVIEW.md`'s two worked examples were the verbatim answers to the two subjects under
   review. **A full round's headline evidence was contaminated by the role instructions.**
5. **N3-R8** — `package_ref` is a canonical-JSON digest, not the file's bytes, and nothing said so.
   **run-p3's reviewer computed `sha256sum`, got a mismatch, and notes that a reviewer deriving the
   digest independently *"would have concluded the package was corrupt"*.**

That is more than enough to establish that this layer is load-bearing and unchecked.

**But now the uncomfortable part.** Sort those five by the instrument that would have caught them:

| Witnessed defect | Would a cheap checker have caught it? |
|---|---|
| N3-R7 (i) ceiling/floor ambiguity | **No** — single-file semantic ambiguity |
| N3-R7 (ii) stop-criterion contradiction | **No** — semantic contradiction between two clauses of one file |
| disposition-boundary overlap | **No** — single-file semantic ambiguity |
| N3-R6 example contamination | **No** — requires knowing the subjects |
| N3-R8 missing digest semantics | **No** — the defect is an *absence* of documentation; an existence checker has nothing to key on |
| C1 stale pointer | Yes |
| C2 self-referential status | Yes |
| C5 copy divergence | Yes (normalized equality against the immutable contract copy) |
| **C3 cross-file stage divergence** | **No** |

**Every defect that has actually caused a measured problem falls in the class no script catches.
Every defect a cheap checker would catch has never caused a measured problem.**

So the intuitive remedy — build staleness / self-assertion / duplicate-sentence checkers — **treats
the half that has never bitten.** That is worth stating plainly because it is the opposite of what
this note's own §2 first suggested.

**The instrument with a demonstrated yield already exists, and this project invented it this week:**
the independent checkpoint read inserted between amendment 2 and the round-3 dispatch (recorded in
`c07d682`'s message, on the round-2 lesson that an unreviewed amendment contaminated a full round's
evidence). Its measured yield was **3 defects in one 79-line amendment**.

One distinction keeps that claim honest — and preempts the natural objection that the round-2
reviewers *did* read `REVIEW.md` line by line. They read it **to follow it**, not **to review
it**, and the yield difference is measured: reading-as-execution surfaced all five defects only
incidentally, when the text happened to bite the reader; the checkpoint read — whose question was
the text itself — caught 3 in 79 lines on the first pass. Eyes passing over every line is not
coverage; **the reader's question decides the yield**. This is the review contract's own §1
principle (*independence is decided by who sets the question*) applied to prose: the scheduled
read must have the instruction layer as its **subject**, never merely as its manual.

**Conclusion.** What this layer needs is a **scheduled independent read**, not a checker. Checkers
remain a cheap optional supplement for C1 / C2 / C5 — they cost little and remove a recurring
irritation — but they must not be presented as addressing the class that has actually caused harm,
and they should not be built ahead of the read.

---

## 5. The base rate, and the ruling against rewriting

`eca4902` was a careful, deliberately-improving, 79-line edit to `REVIEW.md` by an experienced
executor. **It introduced three defects** (F1 negative-only exemption, F2 an over-broad exemption
example, F4 a worked example that shared its subject's skeleton), all found by the checkpoint read
and all repaired in `c07d682`.

**79 lines → 3 defects** is the only quantitative evidence anyone has about edit risk in this layer.
It carries two consequences:

1. **Do not rewrite the instruction layer, even "with the same content."** In a layer with tests, a
   rewrite is safe because the tests hold the semantics; here nothing does (§1). A rewrite means
   re-typing ~20 rules, many purchased with a real defect (N3-R6, R7 i, R7 ii, R8, the
   disposition split, N1's two fail-open lessons, the floor semantics) — with **nothing** to catch a
   dropped nuance. The failure is silent and undetectable. Scaling the observed rate to a 214-line
   rewrite makes the expected defect count worse than the disorder being fixed.
2. **Prefer few, batched, additive or subtractive edits over many small ones.** Three out-of-node
   amendments landed in 72 hours (`55133a9`, `eca4902`, `c07d682`); only one boundary between them
   carried an independent read. The edit rate, not the edit size, is what outran the review.

---

## 6. Open items carried in from earlier rounds, still undisposed

These are not part of the instruction-layer analysis; they are recorded here because they were
reported in earlier rounds and have not yet been dispositioned anywhere durable.

| Item | What it is | Why it still needs an action |
|---|---|---|
| **L3** | `shadow/round-3/validate_review.py:9` reads *"Given to the round-2 reviewers…"* — and the round-3 dispatch prompt **orders the reviewer to run that file** | Repair looks more expensive than the leak: the file is header-marked *"derived from ../round-2/… Do not hand-edit"*, rounds 1–2 are frozen (V3-D9), and adding a third substitution kind to `build_round3.py` would falsify its own claim that two kinds are *"the complete and only difference from round 2."* Recommendation: **do not repair; disclose as a known residual in the N3 record**, so round-3's independence claim does not silently carry an undisclosed hole |
| **F3** | Contract §7 invariant 9 lists `checks` as ReviewPackage content; the schema `allOf` mandates only six roles (checks not among them); `REVIEW.md` L50–56 now declines to refuse on missing `check_result` members | Not a contradiction — the three address different parties, the omission must still be recorded as a finding, and invariant 8's obligation↔`CheckResult` binding is enforced elsewhere via the coverage `NO_RESULT` join. But the net effect is that *"packages contain checks"* is enforced by nothing, which will mislead a future implementer reading the contract. Belongs in a residual, or in a post-v3 schema revision |
| **F5** | The five `eca4902` fixes have **zero mechanical binding** — proven: descriptions changed, no test moved, all suites green | The N3 record must not let *"all five suites green"* be read as *"the fixes are guarded."* It means only *"nothing else was broken."* Belongs in the record's honesty-ceiling section |

---

## 7. Routing — reported, not assigned

The review side may not set the execution side's agenda, update a pointer, or write a node
candidate. Everything below is **reported for the user to route**. Committing this file is the
execution session's act, never the reviewer's.

**Nothing here is an adoption blocker.** Under `v3-harness-review-contract.md` §4, an item that
violates no acceptance ID and no signed clause is a *finding*, not a blocker. All of C1–C5 are
findings; treating them as revise triggers would be inflating them.

Suggested sequencing, in the order that minimises interference with work in flight:

1. **Do not modify `REVIEW.md` before the round-3 dispatch.** None of C1–C5 is *consequential*
   for a round-3 reviewer: C3's divergence is between files and the reviewer reads only
   `REVIEW.md`; the one prose surface a reviewer might follow out of it (the reconciliation note
   cites contract §5, where C2's false frontmatter `status:` sits) leaks no verdict and touches
   nothing the review depends on. So none of them justifies delaying or disturbing the round.
   `REVIEW.md` should stay frozen from dispatch to the end of the round.
2. **In-node, and available now:** L3, F3 and F5 (§6) are dispositions *inside the N3 record*, which
   is in N3's own allowlist. They are the only writes this analysis calls for that do not require a
   new out-of-node authorization.
3. **Everything in §2 lands in `document-harness/` and `contract/`, outside the N1–N3 allowlists.**
   Every fix is therefore an out-of-node amendment requiring its own user authorization. Three have
   been spent in 72 hours. **Batch C1 + C2 + C3 into one commit at a node boundary; do not open a
   fourth ad-hoc amendment.** The three edits are: delete `README.md`'s status banner; delete
   `README.md` L17's duplicate of the N0 §8 errata; add a stage qualifier to `EXECUTION.md` §*When
   the instruction itself is the problem* and to `REVIEW.md` §*When the map is incomplete*.
4. **C4 and C5 are records, not tasks.** Register them; take no action in v3.
5. **The item that belongs in the adoption adjudication is §1 + §4**, not the individual defects: the
   instruction layer is load-bearing, unbound and unread, round 2 measured the consequence three
   times, and the effective instrument is a scheduled independent read rather than a checker. That
   question shares a home with
   [`v3-review-note-obligation-authoring.md`](v3-review-note-obligation-authoring.md) — it is the
   same question about the `review_only` class, asked of the harness instead of the work.

---

## 8. Honesty ceilings

- **Coverage.** Four prose files read in full (590 lines); the 712-line plan was searched by keyword
  only (§0). A fourth statement of any rule may exist there and would not have been seen.
- **No evidence lock.** Every claim in §2–§5 is a judgement about text. **None of it is backed by a
  test** — which is the subject of the note, and applies to the note itself.
- **The base rate is n = 1.** "79 lines → 3 defects" is one observation of one amendment by one
  author. It is the only measurement available; it is not a statistic.
- **C4's growth rate is observed, not projected.** Two labelled local rules exist. Whether that
  number will keep growing is a guess.
- **Consistency with contract §1.** Everything above is a **property that is not measured**, never a
  property that is violated. v3 promises bounded assurance and visibility, never guarantee. Nothing
  proposed here raises that promise; it only extends what is made visible.
