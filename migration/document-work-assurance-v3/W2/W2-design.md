# Wave 2 — commit-first ReviewPackage successor: design proposal

**Status: execution-side authored design proposal (2026-07-22, wave-2 opening session).
Not a node artifact; sits at the migration root outside every node allowlist; bears on no
verdict; changes nothing.** Everything here is versioned-successor territory gated on user
adjudication (§8); nothing modifies a signed byte. Per the boundary-referent ruling landed
the same day (`e90243a`), this draft was authored during — and its commit held until — the
wave-2 opening cold read; that read returned the same day (3 low + 3 observations, none
touching this design's content; findings record
[`v3-cold-read-e90243a.md`](../v3-cold-read-e90243a.md), fixes `979a983`), lifting the
hold. **Its independent review ran 2026-07-22/23 (fresh context, subject `8c77f1e`): 2
must-fix + 8 further findings, all resolved in revision `3a12f04` (§10). The revision's
verify-shaped read returned 2026-07-23: nine of ten resolutions landed with no fix owed;
the one low residual (`work_id`/`run_id` orphaned — a prescription-side omission, per the
reviewer's own honesty note) is fixed in this second pass, which follows the verify's
verbatim prescription and is itself not re-read (§9 ceiling).**

**§8 ADJUDICATED by the user 2026-07-23 — all six points per recommendation:** same-branch
evidence commits (i) · package dissolves into the ReviewResult subject binding +
tree-derived enumeration (ii) · small versioned successor carrier
`…-v3-supersession-1.md` (iii) · legacy stays pinned v1, no migration, shadow scripts
untouched (iv) · **the design signature does NOT authorize implementation — the
implementation round opens only on its own explicit user go** (v) · working names stand
(vi). The §2 near-miss note is retained. This adjudication makes the design the
implementation round's governing input; it changes no signed byte and starts nothing.

Inputs, per the §9 adjudication of
[`v3-special-case-bucket-design.md`](../v3-special-case-bucket-design.md) (two waves per
recommendation; (c) parked until after wave 1's first real run — that run, w1-r1, is now
CLOSED): the design outline in its §6 with the F2 scope correction; register row **N3-R9**
(its N3 record §9 row — never restated here); the w1-r1 witnessed-case pool
(`../../../generated/document-assurance/runs/w1-r1/issues/` + the FULL review's
`residual_uncertainty` in `runs/w1-r1/evidence/review-full.json`); and the three
ISSUE_TRIAGE rulings of 2026-07-22 (`f4b7994`).

---

## 1. Evidence base — what is witnessed, what is analysis

- **N3-R9 (analysis, not a witnessed failure).** The ReviewPackage's only load-bearing
  function is pinning the **uncommitted control plane** at review time; tree members are
  already content-addressed by the pinned commit, so member digests re-prove what
  `git show` guarantees. Amendment 2 downgraded conditional membership to
  finding-and-continue, removing most of the layer's remaining consequence.
- **w1-r1 witnessed case 1 — the authored member list disagreed with reality**
  (`issue-w1-r1-freeze-check-paths`, triaged `CORE_CANDIDATE` into this round): the freeze
  step registered all eight CheckResults under one aggregate path; `check_package`'s
  distinct-path count collapsed 8→1 and the freeze correctly failed. The defect lived in
  the **hand-authored enumeration** — a second copy of what the run directory already
  states. The guard worked; the layer made the defect possible.
- **w1-r1 witnessed case 2 — nothing names which digest kind a pointer carries**
  (`issue-w1-r1-pointer-digest-kind`, triaged `CORE_CANDIDATE`): a CANONICAL digest was
  written where resume verifies BYTES; cold resume correctly refused. Convention exists
  only as folklore; wave 2 pins it.
- **w1-r1 witnessed case 3 — preamble-level run conditions escaped the unit map**
  (`issue-w1-r1-unmapped-preamble`, triaged `WORKFLOW_FIX`): authoring and the coverage
  audit both passed a map that omitted the instruction preamble's normative conditions;
  only FULL review caught it. The START approval surface was narrower on paper than the
  instruction.
- **w1-r1 conventions the successor inherits** (established in production, recorded at run
  close): real-run control root `ResearchSystem/generated/document-assurance/runs/<run-id>/`;
  one file per CheckResult in the package; state pointers carry BYTES digests. w1-r1 also
  already **committed its control plane** on the working branch (`2b59a3c`, `312481c`)
  while the payload sat isolated on `w1-r1-candidate` — the commit-first shape ran once in
  production before being designed here; what is missing is only that the *review subject*
  still bound the package object, not the commit.

Ceilings: N3-R9 remains analysis; no run has ever been *harmed* by the package layer — the
witnessed defects cost one freeze retry and one pointer correction, both caught by guards.
The case for wave 2 is redundancy-plus-witnessed-friction, not witnessed harm.

## 2. The signed surface — four statements, not three

The signed contract fixes the package layer in **four** places (design-review F2 counted
three; authoring this round found a fourth by exhaustive grep — all `[Pp]ackage`
occurrences in the contract body):

| # | Site | Signed text (condensed) |
|---|---|---|
| S1 | §4 storage topology | control root E(C) `-> frozen ReviewPackage / ReviewResult` |
| S2 | §7 invariant 9 | ReviewPackage logically includes raw instruction/sources, plan, actual candidate artifacts, fulfillment, manifest, checks and coverage; membership uses exact revision + locator + digest and never byte-copies; executor summary supplemental only |
| S3 | §7 invariant 11 | Repair regenerates manifest, fulfillment mapping, checks, coverage **and package** for C2 |
| S4 | §8 step 7 | controller freezes actual-subject ReviewPackage; reviewer runs one FULL |

The four-site count was independently re-verified by the design review (case-insensitive
sweep): exactly these four. The sweep's two near-misses — §3's "the controller may freeze
subjects and bind refs" and §12's nominated-reuse item "frozen review-subject binding" —
do not name the layer and correctly need no re-homing (the successor controller still
binds the review subject, by commit instead of by package; content recovered at verify
from the review's corrupted span, strikeable at adjudication). The successor must re-home
all four. Contract §13 sanctions the mechanism explicitly:
*"Signed contracts are never amended in place; corrections create a versioned successor."*
N2-A1 ("requires actual subjects; summary-only substitution fails") is **re-satisfied by
the successor's own acceptance, never amended** (bucket design §6): subjects are read at
pinned revisions from the commit; the reviewer derives from the repository, not from
executor-supplied bytes.

## 3. The successor design

**Core move.** The controller **commits the control plane** (an evidence commit, distinct
from the payload candidate) before dispatching review. The review subject becomes **one
commit SHA**; the reviewer re-derives everything from pinned revisions — exactly how the
construction-side review contract §2 already works, exercised by every checkpoint read this
month. The product converges on the process that verified its own construction.

### 3.1 Evidence-commit topology (open item i)

Two options:

- **(i) Same-branch evidence commits — recommended.** The evidence commit lands on the
  run's working branch (w1-r1's witnessed shape: control root committed on
  `document-work-assurance-v3` while the payload sat on its isolated candidate branch).
  Payload/evidence identity separation (§4) is preserved by *path*, not by ref: the
  evidence commit touches only the control root; the payload candidate stays on its own
  branch until FINAL promotion. No new machinery.
- (ii) A dedicated control ref (`refs/assurance/<run-id>`). Stronger namespace isolation,
  but new machinery with no witnessed need — the N2-R4 principle says do not
  pre-engineer it. Available as a later successor if same-branch topology witnesses a
  failure (e.g. evidence commits polluting branch history at scale).

Under either option the contract-§4 payload/evidence separation stays **checked**, never
hoped: the successor requires the evidence commit's changed-path set ⊆ the run's control
root (reusing `candidate.py`'s existing segment-boundary containment), a seeded violation
is reported, and the checker's home is `check_subject`, which reads the evidence commit
anyway (W2-A10; design-review must-fix 2).

### 3.2 What replaces the package (open item ii)

The package **dissolves into the ReviewResult's subject binding plus a derived
enumeration**:

- The ReviewResult (successor schema) binds:
  `subject = { evidence_commit, candidate_ref {branch, commit}, base_revision,
  control_root }` — three already exist in the CandidateRecord; `evidence_commit` is the
  only new field, recording the SHA w1-r1 already produced in practice. No digests per
  member, because the evidence commit content-addresses every member byte.
- Git replaces byte binding, **not verification. Two check classes survive the layer and
  must be re-homed** (design-review must-fix 1):
  1. **Completeness** re-homes as **`check_subject`**: it reads the control root **at the
     evidence commit** and checks completeness against the spec and record (every declared
     input present, every expected artifact accounted for, every CheckResult file present —
     one file per CheckResult, the w1-r1 convention, now load-bearing). There is **no
     hand-authored member list to get wrong**: the enumeration is derived from the
     committed tree. This kills witnessed case 1's defect class at the root rather than
     guarding it — the authored list was a second copy of the directory listing, and the
     duplication defect is the harness's own oldest enemy (N0-A6, V3-D8).
  2. **Identity and verdict binding** — today's `check_package` cross-checks
     (work/run/round, candidate commit + branch, base revision) and the package-coupled
     `check_review_result` binding checks (result answers the exact package bytes, round,
     candidate). `check_subject` re-homes the former: the subject's
     `candidate_ref`/`base_revision`/`control_root`/`repair_round` must agree with the
     CandidateRecord read **from the evidence commit**. A **v2-aware result checker**
     (successor path of `check_review_result`, version-keyed) re-homes the latter: the
     result's `subject.evidence_commit` must equal the commit under check, its
     `candidate_ref.commit` and `review_round` must match, its `work_id` must match the
     spec's and its `run_id` the CandidateRecord's at the evidence commit (verify finding
     1 — v1 checks run_id only in `check_package`, so dissolving the package would
     otherwise orphan it), and the obligation-coverage invariants (2, 10) are reused
     unchanged. Without this, "existing functions untouched"
     would leave a v2 ReviewResult with schema validation only — reopening the "check
     candidate A, report candidate B" class (V3-D5) at the result layer.
- The executor summary stays supplemental-only (S2's clause survives verbatim in the
  successor statement).
- Rejected alternative: a thin successor *object* (member list without digests). It keeps
  the authored-enumeration defect class alive to save one derived listing; nothing else
  distinguishes it.

### 3.3 Pointer convention (triage: `CORE_CANDIDATE`, witnessed case 2)

Pinned in the successor: **a state pointer carries the BYTES digest of the pointed-at
file.** Carried two ways: (a) guidance in the successor statement; (b) a pointer-writing
helper (`assurance_state.pointer_to(path)` computing the bytes digest itself) so the
convention is executable, with the existing resume guard as its negative control. The raw
`pointer(path, digest)` form stays for schema compatibility; the helper becomes the
documented authoring path.

### 3.4 Preamble mapping (triage: `WORKFLOW_FIX`, witnessed case 3)

Successor template + authoring guidance: **preamble-level normative run conditions must
appear in the unit map** (a process-classified unit is the established shape), so the START
approval surface is never narrower than the instruction. Enforced at authoring and audit
guidance level; enters the acceptance matrix (W2-A5). The `EXECUTION.md` sentence carrying
this is an instruction-layer amendment — batched, checkpoint-read before use (rule 3).

### 3.5 Legacy handling (open item iii)

Closed runs and shadow rounds keep their frozen packages as **pinned v1 history** (contract
§13: a live run pins exact schema versions; later changes never mutate it). No migration,
no re-freeze, no retroactive script fixes (per the freeze-check-paths triage: the shadow
round-2/3 freeze scripts stay historical, recorded here, untouched). `check_package` and
`review.schema.json`'s package definition stay frozen for reading that history.

### 3.6 Version keying (the W1 pattern, applied again)

Explicit keying, **no cross-version fallback**: the successor ReviewResult **declares its
own version** (an explicit version field selecting package-subject vs commit-subject
semantics). The state-pin alternative is deliberately not re-surfaced to §8: W1 already
adjudicated this fork class for the WorkSpec — instance self-declaration won (root
`schema_version` const, bucket design §9.6) — and the successor follows that precedent
(design-review finding 6; the user may still override at adjudication). Absence keys to
v1 semantics; a
present-but-null declaration is a SpecGap (the W1 `_ABSENT`-sentinel lesson, `8e681f8`).
New runs always declare the successor version (the v2-mandate pattern, `a22cca0`).

### 3.7 Carrier (open item iv)

Three signed-prose statements plus one diagram line must be re-homed without touching
signed bytes. Options:

- **(i) A small versioned successor document — recommended.** One file (working name:
  `contract/Document-Work-Assurance-Contract-v3-supersession-1.md` — renamed from "-S1"
  per design-review finding 10, which caught the collision with §2's site labels) that:
  names the
  four superseded statements S1–S4 by exact location; states each successor statement in
  full; declares explicit version keying + no-fallback; is signed at the wave-2 gate. The
  signed v3 contract stays byte-identical; the supersession lives in the successor file,
  mirroring the `document-work-spec.v2.schema.json` move at contract level (§13's
  sanctioned mechanism).
- (ii) A full `…Contract-v3.1.md`. Re-types ~250 lines to change four statements — the
  same rewrite-risk *mechanism* that rule 3 records for the instruction layer (an analogy,
  not a citation: rule 3's scope is prose no test holds, while the contract's semantics
  are partly held by fixtures; a full re-issue still re-types every statement, and 3
  defects per 79 careful lines is the only measured rate anywhere); rejected unless the
  user wants a consolidated contract for other reasons.
- Schema carrier alongside either option: a successor review schema (working name:
  `review.v2.schema.json`) for the subject-bound ReviewResult, plus fixtures; the v1
  `review.schema.json` untouched.

## 4. What implements it (change surface, for the implementation round's allowlist)

Full paths (this list feeds the implementation round's allowlist; design-review finding 9):

- `ResearchSystem/contract/Document-Work-Assurance-Contract-v3-supersession-1.md` (new,
  §3.7) — signed at the gate.
- `ResearchSystem/schema/document-assurance-v3/review.v2.schema.json` (new) + fixtures
  pos/neg.
- `ResearchSystem/tooling/rsclib/document_harness/review.py`: add `check_subject` **and
  the v2-aware result-checker path** (§3.2 point 2), version-keyed; existing v1 functions
  untouched (frozen for v1 history). If `review.py` cannot carry them in-boundary, a
  sibling module — implementation-round decision, recorded there.
- `ResearchSystem/tooling/rsclib/document_harness/assurance_state.py`: `pointer_to`
  helper (§3.3).
- Successor run template (the wave-2 equivalent of w1-r1's run scripts) carrying §3.1
  topology + §3.4 preamble mapping.
- `ResearchSystem/document-harness/EXECUTION.md` / `REVIEW.md` prose batch (instruction
  layer — amendment discipline, checkpoint read before use).
- Tests: acceptance matrix below, mutation-tested per the standing discipline.

## 5. Acceptance matrix draft (W2-A*)

| ID | Acceptance | Check shape |
|---|---|---|
| W2-A1 | Successor ReviewResult schema validates subject binding; fixtures reject a package-less, subject-less result and a both-present hybrid | fixtures pos/neg + mutation |
| W2-A2 | `check_subject` derives the enumeration from the committed tree; a CheckResult file missing from the tree is reported. Two claims, separately carried (design-review finding 4): (a) the authored member-**list** collapse is unrepresentable — the object no longer exists (constructive argument, untestable by design); (b) the aggregate-**storage** analogue (eight results written into one file) remains representable and, seeded, is reported | seeded-defect test + constructive argument |
| W2-A3 | Version keying explicit; no cross-version fallback; present-but-null = SpecGap; v1 package validation byte-for-byte unchanged on the existing suite | unit + golden |
| W2-A4 | `pointer_to` writes bytes digests only; the canonical-digest mistake is impossible via the helper; resume guard still fires on a hand-written wrong pointer | unit + mutation (probe restores byte-verified) |
| W2-A5 | Successor template maps preamble-level run conditions; a template instance omitting them fails its authoring check | template fixture |
| W2-A6 | S1–S4 re-homed by the successor carrier with exact supersession enumeration; signed v3 contract blob byte-identical before/after | blob comparison |
| W2-A7 | A cold session re-derives the full review subject from the evidence commit SHA alone (resume + `check_subject` from `git show`, no worktree state) | integration test |
| W2-A8 | Prose batch additive, few, batched; its checkpoint read occurs before any run relies on it | process (rule 1) |
| W2-A9 | v2 ReviewResult binding (must-fix 1): a result naming a different `evidence_commit`, a different candidate commit, the wrong round, a foreign `work_id`, or a foreign `run_id` is rejected; the subject's `candidate_ref`/`base_revision`/`control_root`/`repair_round` cross-check against the CandidateRecord read from the evidence commit, with a negative fixture per mismatch (incl. `work_id` and `run_id`, verify finding 1) | unit + negative fixtures + mutation |
| W2-A10 | Evidence-commit containment (must-fix 2): the evidence commit's changed-path set ⊆ the run's control root (`candidate.py` containment reuse); a seeded out-of-root path is reported by `check_subject` | seeded-defect test |

## 6. What this proposal does not do

- It proves no semantic truth and raises no promise (contract §1): the commit pins bytes,
  not honesty; review remains the only instrument for content.
- It does not migrate, re-freeze or repair any closed run or shadow script (§3.5).
- It does not introduce the dedicated control ref, a package v2 object, dedup registries,
  or any §12 removed-interface item.
- It does not decide the implementation node's module layout — that round derives its own
  allowlist and records its own trade-offs.
- It does not touch `common.schema.json`, the signed contract, the plan, or any signed
  byte; the carrier file is new bytes signed at its own gate.

## 7. Sequencing

Design (this file) → independent review → user adjudication of §8 → implementation round
under construction-node discipline (candidate → FULL → optional bounded fix → VERIFY →
user sign), with this file's §5 as its acceptance-matrix seed. The implementation round is
**not** authorized by adjudicating the design unless the user says so explicitly (§8.5) —
the wave-1 precedent (bucket §9.4) left that fork to the user and it stays the user's.

## 8. Adjudication points — RULED 2026-07-23, all six per recommendation

> The user's ruling is recorded in the header block; the points below stand as the
> decision record, each resolved to its stated recommendation.

1. **Evidence-commit topology:** same-branch (recommended, witnessed at w1-r1) vs
   dedicated control ref (defer per N2-R4).
2. **Package fate:** dissolve into ReviewResult subject binding + tree-derived enumeration
   (recommended) vs thin successor object with an authored member list.
3. **Carrier:** small versioned successor document `…-v3-supersession-1.md` (recommended)
   vs full v3.1 contract re-issue; successor review schema rides either.
4. **Legacy:** pinned v1 history, no migration, shadow scripts stay untouched
   (recommended — confirms the freeze-check-paths triage) vs retroactive fixes.
5. **Implementation authorization:** design-only now, implementation behind its own
   explicit go (recommended, mirrors wave 1) vs authorize implementation at design
   sign-off.
6. **Naming** (bikeshed, no blocker): `check_subject` / `pointer_to` /
   `…-Contract-v3-supersession-1.md` / `review.v2.schema.json`.

## 9. Honesty ceilings

- N3-R9's redundancy claim is analysis; the witnessed w1-r1 cases are friction caught by
  guards, not harm. The evidence for wave 2 is materially weaker than wave 1's was, which
  the two-wave ordering already priced in (bucket §7).
- The four-site count (§2) was one author's exhaustive grep at authoring time; the design
  review re-derived it independently (case-insensitive) and confirmed exactly four.
- Digest-strength narrowing, disclosed (design-review observation 8): v1 package members
  carry SHA-256 digests; the successor rests member binding on git content addressing,
  whose object format in this repository is SHA-1 (`git rev-parse --show-object-format`).
  Acceptable under contract §1's threat model — single writer, workflow protocol rather
  than OS guarantee — but a real strength change, stated rather than glossed.
- w1-r1 is n=1 production use; its conventions (§1) are one run's shape, promoted here by
  judgement.
- Effort words ("small", "no new machinery") are judgements, not measurements.
- This file was authored before the wave-2 opening cold read returned, with its commit held
  until the read came back (the boundary-referent rule's first application, kept clean).
  The read returned 2026-07-22 with no finding touching this design's content; the hold was
  honored and lifted at commit time.
- Revision `3a12f04` **was** verified (2026-07-23, same-reviewer continuation): nine of
  ten resolutions no-fix-owed, one low residual + one recovered observation, both landed
  in the second pass. The second pass follows the verify's verbatim prescription but is
  itself not re-read — the regress terminates by proportionality (two clauses and one
  note), and the user may still route a micro-verify before adjudicating.

## 10. Design review (2026-07-22/23) — findings and resolutions

Recorded in condensed form (the R1 lesson); the reviewer's full report was relayed by the
user in-session, with several paste-corruption spans disclosed as unreconstructable — the
resolutions below follow the recoverable substance, and nothing was invented to fill the
gaps. The review verified §1's evidence against the six issue/triage JSONs, the mechanism
claims against `review.py`/`assurance_state.py` in full, the four-site count by
independent sweep, the commit-hold from git history, and §5's binding of §3 — finding the
two holes below. Ten findings, all resolved in this revision:

| # | Severity | Finding | Resolution |
|---|---|---|---|
| 1 | must-fix | §3.2 undercounted what git cannot replace: `check_package`'s identity cross-checks and the package-coupled `check_review_result` verdict binding had no successor home — "existing functions untouched" would leave a v2 result schema-only, reopening V3-D5 at the result layer; §5 bound none of it | §3.2 point 2 names both homes (`check_subject` identity cross-checks vs the CandidateRecord at the evidence commit; a v2-aware result checker); §4 change surface updated; W2-A9 added with per-mismatch negative fixtures |
| 2 | must-fix | Same-branch topology would degrade contract-§4 payload/evidence separation from checked to hoped — no one reports an evidence commit that mixes in payload paths | §3.1 closing paragraph: changed-path set ⊆ control root, `candidate.py` containment reuse, checker home named; W2-A10 added (seeded violation reported) |
| 3 | low | "all four already exist in current objects" — false for `evidence_commit` | §3.2 corrected: three in the CandidateRecord; `evidence_commit` the only new field |
| 4 | low | W2-A2 self-contradicted: "unrepresentable by construction" cannot be "shown by a negative control" | W2-A2 split: list-collapse = constructive argument (untestable by design); aggregate-storage analogue = seeded-defect test |
| 5 | low | "the rule-3 rewrite risk" cited outside rule 3's scope (instruction layer) — the bucket-F5 citation-drift class | §3.7 rewritten as explicit analogy, scope difference stated |
| 6 | low | §3.6 left the version-discriminator fork (state pin vs instance field) dangling for the implementation round with no §8 row | Closed by W1 precedent (instance self-declaration, bucket §9.6), stated in §3.6 with an explicit user-override note |
| 7 | obs | Four-site count confirmed by independent sweep | Noted in §2 and §9; the reviewer's near-miss details fell in a corrupted span and are not restated here |
| 8 | obs | Digest-strength narrowing (member SHA-256 → git SHA-1 content addressing) absent from §9 | §9 ceiling added |
| 9 | obs | §4 used short paths while calling itself allowlist input; historical allowlists use full paths | §4 paths in full form |
| 10 | obs | Working name `…-v3-S1.md` collided with §2's site label S1 | Carrier renamed `…-v3-supersession-1.md` |

**Verify-shaped read of revision `3a12f04` (2026-07-23, same-reviewer continuation):**
structural re-derivation clean (numstat 107+/34− single file, blob = tip); all ten
resolutions checked against diff + ground truth — nine landed as prescribed with no fix
owed (incl. independent re-verification of the W1-precedent claim in §3.6 and of every §4
path against the tree); §10's condensation of the original report confirmed faithful, no
new defect outside the resolutions. Three verify findings, resolved in the pass carrying
this paragraph: **v1** (low) — must-fix 1's enumeration omitted `work_id`/`run_id`
(prescription-side residue, honestly attributed by the reviewer): fixed in §3.2 point 2 +
W2-A9; **v2** (observation) — the corrupted near-miss content restored from the reviewer's
session: landed as the §2 note, strikeable at adjudication; **v3** (observation, cosmetic,
no fix owed) — bold-span and ragged-line artifacts of the minimal diff, semantics intact.
The rider on `47b1cb4` returned fully confirmed, no fix owed — that batch's verify debt is
discharged.
