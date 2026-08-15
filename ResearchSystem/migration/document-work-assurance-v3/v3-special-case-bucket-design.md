# 特例-bucket design round — proposal

**Status: execution-side authored design proposal (2026-07-22). Not a node artifact; sits at
the migration root outside every node allowlist; bears on no verdict; changes nothing.**
Every item below is versioned-successor or amendment territory gated on user adjudication;
nothing here modifies a signed byte. Per the instruction-layer discipline's spirit, this
document itself goes through an independent checkpoint read before the user adjudicates it.
**Revision 2026-07-22 (same day): the checkpoint read occurred; its eight findings are
fixed in this revision and recorded in §11; the §9 adjudication (six points) is open.**

Inputs, per the `ADOPT_DOCUMENT_V3` ruling's queue (N3 record §8) and the N4 closeout:
**N3-R9** (commit-first supersession) and **N3-R10** (status: their N3 record §9 register
rows — never restated here),
[`v3-review-note-obligation-authoring.md`](v3-review-note-obligation-authoring.md),
[`v3-review-note-instruction-layer-custody.md`](v3-review-note-instruction-layer-custody.md),
plus the two "visibility items" the same §8 entry deferred alongside them (the START-surface
`review_only` ratio; the `EXECUTION.md` declaration discipline).

---

## 1. Evidence base — what is witnessed, not hypothesized

The project's own bar (N3 record §4.1): *a real occurrence is the evidence that justifies
amending a signed schema; no occurrence is the evidence that it should not be built.* The
occurrence exists:

- **The incentive gradient fired in both shadow runs.** 12 of 19 obligations (63%) were
  `review_only`; 0 were `local_check` alone. At least four of the twelve were
  script-verifiable with no judgement involved.
- **The one real defect the node found sat inside it.** `P3-inventory.md`'s 110-vs-51 count
  lived in `ob-scan`, declared `review_only` by its own author *for the reason the
  obligation-authoring note predicted* — `review_only` costs no `LocalCheckSpec`, no binding,
  no separately-authored `CheckResult`. A five-line script would have falsified it instantly;
  instead a reviewer spent ~60% of a FULL review hand-counting files (N3 record §4.1, §8 —
  the user's sharper framing: *that is the design failure*).
- **For item (c):** N3-R9's analysis — the ReviewPackage's only load-bearing function is
  pinning the **uncommitted control plane**; tree members are already content-addressed by
  the pinned commit, so member digests re-prove what `git show` guarantees, and amendment 2
  downgraded conditional membership to finding-and-continue, removing most of the layer's
  remaining consequence.

Ceilings on this evidence: the 63% is two runs by one author under shadow conditions (n=2,
same author as the harness); N3-R9 is an analysis of redundancy, not a witnessed failure.

## 2. Item (a) — `review_only` declares why no deterministic check is possible

**Change.** In the WorkSpec obligation object: `verification_mode: review_only` additionally
requires a non-empty `review_only_rationale` (string, minLength 8, maxLength 500) stating why
a deterministic check is not possible for this requirement. Deterministic modes forbid the
field (strict both-ways conditional, mirroring the existing `instructionUnit`
`context → rationale` / `obligation → obligation_ids` pattern — the schema's own established
move: *you claim the cheap path, so say why*).

**What it does and does not buy.** Presence and non-emptiness are mechanisable; truth is not.
A hollow rationale ("needs judgement") passes the schema — but it is now one honest sentence
on the cheap path, visible per-row in coverage, and challengeable at FULL review ("this could
have been a script" becomes a finding with a locator). This extends visibility only; it
raises no promise (consistent with contract §1 and the note's own §7 boundary).

## 3. Item (b) — obligations declare their falsification condition

**Change.** `review_only` obligations additionally require a non-empty
`not_supported_condition` (string, minLength 8, maxLength 500): the concrete condition under
which the obligation's disposition would be `NOT_SUPPORTED` — the mutation question asked at
authoring time (*break it: what does that look like?*). "Every internal link resolves"
answers easily; "reads well" cannot, and the inability to answer surfaces to the author
before review instead of after.

**Adjudication point (the one real design fork in this round).** The obligation-authoring
note's original move (§4) requires this of **every** obligation; this proposal narrows it to
`review_only` only. Grounds for narrowing: for `local_check` / `local_check_and_review` the
bound `LocalCheckSpec` *is* a demonstrated falsification condition (the check can fail), so a
universal field would double authoring cost where the property already holds mechanically;
and the witnessed failure class lives entirely in `review_only`. Grounds for the original
universal form: unfalsifiable *wording* can hide behind a weak bound check
(`local_check_and_review` with a trivial `file_exists`), and uniformity is simpler to state —
and, its strongest form (design-review F4): under the narrow scope, dressing an obligation as
`local_check_and_review` with a trivial check escapes **both** new fields at once, while
under the universal scope `not_supported_condition` still travels with the obligation,
halving the dodge's payoff.
**Recommendation: narrow (review_only-only), with the weak-check dressing risk handled by
visibility (§5) and review (§6), not by schema — witness-first: start narrow, upgrade to
universal if a real run witnesses the dressing.** The user picks.

Combined effect of (a)+(b): *the cheap path now costs two honest sentences* — why no script,
and what would refute it. Both are presence-checks (mechanisable); the difficulty falls on
the author, where a hollow entry exposes itself.

## 4. Carrier for (a)+(b) — a versioned successor of the WorkSpec schema

`document-work-spec.schema.json` is N0-signed; signed bytes are never modified (execution
contract hard rule 5), and the `8efe3e9` amendment pattern deliberately touches no signed
byte — so it cannot carry this. The carrier is a **versioned successor schema** in the same
directory (working name: `document-work-spec.v2.schema.json`, versioned `$id`), plus:

- **the version discriminator — a fork wave 1 must close (design-review F1):** a v1
  instance cannot declare its version (the v1 root is `additionalProperties:false` with no
  version field, and the loader's kind→file registry is unversioned). Two mechanisms:
  (i) v2's root adds a required `schema_version` const — the instance names its own schema
  — **recommended**; or (ii) the run state's schema-pack pin selects the version, in which
  case the version is pinned, not spec-declared. Either way the loader keys explicitly and
  **never falls back across versions on validation failure** (try-v1-then-v2 would silently
  mix versions); existing records stay valid against pinned v1 (contract §13: a live run
  pins exact schema versions; later changes never mutate it);
- positive + negative fixtures for the two conditionals (missing rationale rejected; field
  on a deterministic mode rejected; both-present accepted), mutation-tested per the
  established discipline;
- the schema-directory test already tolerates added files (the `8efe3e9` subset assertion),
  verified rather than assumed during implementation.

The successor is small by design: the obligation object's two conditional fields, plus the
root version discriminator if option (i) is chosen; nothing else re-opened.

## 5. Companion visibility items (cheap, non-schema)

- **START-surface mode ratio.** One generated line on the START decision surface and the
  coverage view: `N of M obligations review_only · K bind checks`. The raw signal already
  exists per-row (`verification_mode` is required and closed); nobody is currently asked to
  look at the column (obligation note §6.1). Pure visibility; no gate, no threshold, no
  blocker semantics — a number the user sees before saying START.
- **`EXECUTION.md` declaration discipline.** A worked counter-example for unfalsifiable
  wording (the note's obl-A/obl-B contrast) plus the incentive statement, explicitly marked
  as treating the *wording* half only — prose does not move an incentive (note §3, §6.2).
- **`REVIEW.md` hunt item.** One line in the reviewer's hunt list: for each `review_only`
  obligation, ask *could a script have verified this?* — a mechanisable-but-undeclared
  obligation is a finding. This treats the effort half at review time.

The two prose edits are instruction-layer amendments — per the standing discipline they land
batched, and pass an independent checkpoint read before use.

## 6. Item (c) — the commit-first successor to the ReviewPackage layer

**Direction (design outline only; implementation is its own later round).** Commit the
control plane before review; review everything at a commit.

- Today (invariant 9 / N2-A1): the controller freezes a ReviewPackage with logical
  membership (revision + locator + digest per member) because the control plane
  (resolved plan, fulfillment, manifest, checks, coverage) is *uncommitted* at review time —
  the freeze exists so the executor cannot edit its own materials mid-review.
- Successor: the controller **commits the control plane** (an evidence commit, distinct from
  the payload candidate, on the run's control root) before dispatching review. The review
  subject becomes **one commit SHA**; the reviewer re-derives everything from pinned
  revisions, exactly as the construction-side review contract §2 already works. The package
  reduces to a commit ref plus a member list — or dissolves into the ReviewResult's subject
  binding.
- **N2-A1 is re-satisfied by the successor's own acceptance, never amended:** "requires
  actual subjects" holds because subjects are read at pinned revisions from the commit;
  "summary-only substitution fails" holds because the reviewer derives from the repository,
  not from executor-supplied bytes. The property survives; its mechanism changes owner (from
  a bespoke freeze layer to Git content-addressing).
- The symmetry is the argument: the product converges on the process that verified its own
  construction — one-SHA handoff, parent-pinned subjects — which this migration exercised
  twice more this week (checkpoint reads #1/#2 of the discipline amendment).

Not designed here (deliberately): evidence-commit topology (same branch vs control ref),
legacy-package handling, `check_package`'s fate, the successor's full acceptance matrix.
Those belong to the successor round itself, behind its own user gate. N3-R9's register row
stands as the scope anchor — **with one scope correction from the design review (F2): the
ReviewPackage is fixed by the signed contract in three places — §7 invariant 9, the §4
storage topology, and §8 step 7 — not only by acceptance N2-A1. Wave 2 is therefore
versioned-contract-successor territory: the successor must re-home all three statements,
and §7's sizing and the §9 timing call are made on that larger scope.**

## 7. Packaging and sequencing — recommendation

**Two waves, each with construction-node discipline (candidate → independent review → user
sign), in this order:**

| Wave | Content | Size | Evidence strength |
|---|---|---|---|
| **1** | (a) + (b) schema successor + fixtures + loader; START ratio line; `EXECUTION.md`/`REVIEW.md` batch | small (one schema file + bounded code + prose batch) | witnessed twice, user-confirmed as the design failure |
| **2** | (c) commit-first review-layer successor | structural | redundancy analysis (N3-R9), no witnessed failure |

Rationale: wave 1 is cheap, evidence-backed, and independent of (c); wave 2 is bigger,
touches a signed acceptance, and loses nothing by waiting for wave 1's experience (each
wave's real run is itself the witnessed-case test for the next). Alternative (one combined
successor round) is available but couples a two-sentence schema change to a structural
rework — rejected on the evidence asymmetry itself (wave 1 witnessed twice; wave 2
analysis-only).

## 8. What this proposal does not do

- It does not detect hollow content — a dishonest sentence passes every check here; only
  review challenges it. No new promise is made (contract §1: visibility, never guarantee).
- It does not remove `review_only` or rank verification modes; `review_only` remains a legal,
  designed mode and `UNVERIFIABLE` a first-class disposition.
- It creates a **new incentive edge, stated honestly:** two required sentences may push an
  author toward `local_check_and_review` with a trivial check to dodge them. §5's ratio line
  and hunt item are the counterweights; if a run witnesses that dressing, it becomes
  the next design input — not speculatively pre-engineered now (the N2-R4 principle).
- It does not touch `common.schema.json`, the contract, the plan, or any other signed byte.

## 9. Open adjudication points for the user

1. **(b) scope:** review_only-only (recommended) vs every obligation (the note's original).
   The strongest universal-side argument is now stated in §3 (the trivial-check dodge
   escapes both fields under narrow, only one under universal); the witness-first path =
   start narrow, upgrade if a real run witnesses the dressing.
2. **Field names:** `review_only_rationale` / `not_supported_condition` (the design review
   suggests `not_supported_when` or `refutation_condition` as harder to misread;
   bikeshed-level, no blocker).
3. **Wave packaging:** two waves as §7 (recommended) vs one combined successor round — and
   whether the `REVIEW.md` hunt item rides wave 1's prose batch: it is the one §5 entry
   with no deferral-list ancestry (added by this proposal on the obligation note's §6
   logic); include or strike it consciously.
4. **Wave-1 authorization — the real fork:** (i) authorize wave-1 implementation in this
   same adjudication, or (ii) adjudicate the design only and gate implementation behind a
   separate go. The design's checkpoint read has now occurred, so either path satisfies
   the read-before-reliance discipline; wave 1 would in either case run under
   construction-node discipline with its own acceptance matrix and independent review.
5. **(c) timing:** park wave 2 until after wave 1's first real run (recommended), or
   schedule it now. Note §6's corrected scope (F2): wave 2 is versioned-contract-successor
   territory — three signed statements to re-home — which strengthens the case for its own
   precisely-scoped round.
6. **v2 version discriminator (new, design-review F1):** root `schema_version` const in the
   v2 schema (recommended — the instance names its own schema) vs run-state schema-pack pin
   (version pinned, not spec-declared). Either way: explicit keying, no cross-version
   fallback.

## 10. Honesty ceilings

- The 63% / four-scriptable figures are two shadow runs by one author (the harness's own
  executor); no independent authoring population exists.
- N3-R9's redundancy claim is analysis, not a witnessed failure; wave 2's justification is
  correspondingly weaker, which §7's ordering reflects.
- This document was unreviewed at authoring time; its independent checkpoint read occurred
  2026-07-22, its eight findings are fixed in this revision (§11), and nothing in it is
  load-bearing until the user adjudicates §9.
- Effort estimates ("small", "bounded") are judgements, not measurements.

## 11. Design review (2026-07-22) — findings and resolutions

Recorded **in condensed form** (the R1 lesson); the reviewer's full report was relayed by
the user in-session. The review verified §1's evidence line by line against N3 record
§4.1/§8, the conditional idiom against the v1 schema, the carrier against hard rule 5, and
the deferral-scope completeness — all held. Eight findings, all fixed in this revision:

| # | Finding | Resolution |
|---|---|---|
| F1 | v2 version discriminator unowned; "nothing else re-opened" contradicted adding one | §4 names the fork (root const recommended vs state pin) and bans cross-version fallback; end sentence corrected; §9.6 added |
| F2 | wave 2's signed surface under-counted — the ReviewPackage is fixed by invariant 9 + §4 topology + §8 step 7, not only N2-A1 | §6 corrected: wave 2 is versioned-contract-successor territory |
| F3 | "N3-R10 (closed)" — register-status assertion outside its home file (C1-class drift) | preamble reduced to pointer form |
| F4 | §3 lacked the strongest universal-side argument (the trivial-check dodge escapes both fields under narrow) | clause added in §3; carried into §9.1 |
| F5 | "rule 3" cited outside its scope — it governs instruction-layer prose edits, not wave packaging (citation drift) | citation deleted; the two-wave case rests on evidence asymmetry alone |
| F6 | header's read-before-adjudication promise vs §9.4's authorize-now branch — one rule, two readings | §9.4 rewritten as the real fork; the read has now occurred, dissolving the tension |
| F7 | the `REVIEW.md` hunt item had no deferral-list ancestry | marked as this proposal's addition; folded into §9.3 for conscious inclusion |
| F8 | checkpoint reads #1/#2 mis-attributed to this design round | re-attributed to the migration's discipline amendment |

Self-caught during the fix pass (not a review finding): §8's counterweight line anchored
the hunt item to §6; it lives in §5. Corrected.

Reviewer's §9 advisory, condensed: narrow scope defensible once F4 is stated, witness-first
path endorsed; field names — `not_supported_when` preferred as harder to misread; two waves
endorsed (F2 strengthens the separation); hold wave-1 authorization until after this read
(now satisfied — the fork in §9.4 is live); park (c) until after wave 1's first real run.
