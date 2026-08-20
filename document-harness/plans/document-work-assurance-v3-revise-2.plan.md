# Plan: V3 REVISE amendment 2 — five review-layer fixes from round-2 feedback, then shadow round 3

- **slug**: document-work-assurance-v3-revise-2
- **created**: 2026-07-21
- **complexity**: 复杂
- **status**: done (2026-07-21 — 13/13 steps; commits `eca4902` + `c07d682` out-of-node,
  `2672abf` in-node; adoption decision handed to the user)
- **base_commit**: 48d82b6df813af4b70539ae8105f954f60cb8749
- **base_branch**: document-work-assurance-v3

> [!important] This file is **out-of-node** (`.goals/` is excluded from the N1–N3 allowlists,
> approved plan §9) and was written at the user's explicit request, on the `6bad2b5`
> (`V3-REVISE-PLAN-HANDOFF-v1`) precedent. It carries no authorization of its own. Read this
> file, then `ResearchSystem/migration/document-work-assurance-v3/N3/N3-record.md` (§8 tail +
> §9 residuals), before executing.

## Goal (one line)

Fix the five review-layer defects that shadow round 2 exposed (three of them in the first
revise amendment itself), re-run both FULL reviews as **round 3** on de-contaminated
instructions, and put an honestly-caveated adoption-decision basis in front of the user
(round 3 measures the amended bundle as a whole — see step 12's confound caveat).

## Why / value

Round 2 broke the `INCOMPLETE`+`REVIEWED_NO_BLOCKER` deadlock and both branches of the new
criterion fired — but its routing evidence is **contaminated** (`REVIEW.md`'s worked examples
are the answers to the two subjects under review; N3-R6), and the reviewers found real defects
in the amendment's own wording (N3-R7) plus an undocumented digest trap (N3-R8). The adoption
decision the user must re-take should not rest on evidence a reviewer itself labelled
self-referential.

## Context to resume cold

### Where the work stands

Repo `D:\Thesis-stage-control-refactor`, branch `document-work-assurance-v3`. Working tree at
base: only pre-existing dirt (`.goals/LEDGER.md` modified — do NOT touch; untracked
`ResearchSystem/docs/`, two `v3-review-*` notes at the migration root — user routes those).

| Commit | What |
|---|---|
| `55133a9` | `V3-REVISE-REVIEW-DISCLOSURE-AMENDMENT-v1` — amendment 1 (disclosure instead of refusal; the round this plan repairs) |
| `48d82b6` | `V3-N3-SHADOW-ROUND-2-CANDIDATE-v1` — round 2 complete: both reviews, N3-R6/R7/R8 registered, burden measured |
| `8efe3e9` | the out-of-node amendment precedent (pattern for this plan's amendment commit) |
| `0ba649c` | V3-N2 commit where all four amendment-1 landing sites were first added (`git log --diff-filter=A` verified) |

**User rulings this session (2026-07-21), all binding on this plan:**

1. **`REVISE_V3` confirmed.** The revise round is a **derivative of N3** — amend, then re-do
   N3 — inheriting N3's allowlist and `N3-A1`–`A8`. No new acceptance bar is invented.
2. **Re-run approved** (round 3) after de-contaminating the examples.
3. **Package is a FLOOR, not a ceiling** (settled after long argument): the reviewer may read
   anything at the pinned revisions; disposition records the reviewer's real judgment of the
   obligation (world口径, which is how all four reviews actually filled it). The earlier
   "out-of-package evidence can only downgrade" rule is **wrong and withdrawn** — verdicts are
   driven by findings, and findings may use any pinned-revision evidence in either direction.
   No new fields (`established_from`/`missing_members` proposal was withdrawn — no consumer).
4. **What freezing is actually for** (settled by反事实分析): the ReviewPackage's only
   load-bearing function is pinning the **uncommitted control plane** (resolved plan,
   fulfillment/manifest, check results, coverage) so the executor cannot edit its own
   materials mid-review. Tree members are already content-addressed by the pinned commit —
   their digests are redundant. Payload immutability comes from reading pinned revisions, not
   from the package.
5. **Deferred to the 特例 bucket — OUT of this round** (user: "这三样之后再说"):
   (a) the `review_only` incentive-gradient fix (`document-work-spec.schema.json`, N0-signed);
   (b) obligations declaring their own required evidence (same file);
   (c) the commit-first workflow that would supersede the ReviewPackage (hits N2-signed
   acceptance N2-A1 → versioned successor, never an amendment). Also deferred: the two
   visibility items (START-surface `review_only` ratio; `EXECUTION.md` declaration
   discipline).
6. Earlier ruling still stands: the API-migration worked example drafted in-session was ruled
   "不写" **as a third example**. Reusing it as a *replacement* was not ruled on — see Open
   decisions.

### Key files

| File | Role | Signature status |
|---|---|---|
| `ResearchSystem/document-harness/REVIEW.md` | reviewer role instructions — 4 of 5 tasks land here | V3-N2-authored, no N0 signature |
| `ResearchSystem/schema/document-assurance-v3/review.schema.json` | disposition enum description + `package_ref` description | V3-N2-authored, no N0 signature |
| `ResearchSystem/tooling/rsclib/document_harness/review.py` | guards; likely **unchanged** this round (verify before assuming) | V3-N2-authored |
| `ResearchSystem/tooling/tests/document_harness_review/test_package_and_review.py` | pinning tests; update only if a guard/schema `required` changes | V3-N2-authored |
| `.goals/plans/document-work-assurance-harness-v3.plan.md` | approved plan — **immutable, blob `8ad404b1…`** | signed |
| `ResearchSystem/contract/Document-Work-Assurance-Contract-v3.md` | contract — **immutable, blob `b2dbdf75…`** | signed |
| 7 N0 schemas incl. `common.schema.json`, `document-work-spec.schema.json` | **untouchable** | N0-signed |
| `ResearchSystem/generated/document-assurance/shadow/**` (round 1) and `shadow/round-2/**` | **frozen evidence — never modify** (V3-D9) | committed |

### Round-2 facts a fresh session must not re-derive wrong

- run-a1: `REVIEWED_NO_BLOCKER` + `INCOMPLETE` (6 unmapped units, ids coined by reviewer),
  12 `SUPPORTED` + 1 `UNVERIFIABLE`. run-p3: `SPEC_GAP` (3 unmapped units, 1 blocker —
  ExperimentLab 51 vs declared 110, third independent reproduction).
- Packages were frozen **before** the reviews (`freeze_only.py`), digests handed to reviewers
  **out-of-band** in the dispatch prompts; binding guard exercised both ways after
  (accept correct / REFUSE tampered).
- Burden: authored control unchanged 14,811 B = **17%** (plan §10's effort criterion — not
  triggered); all control 115% (descriptive fact only — **no rule caps volume**; do not call
  it "过线").
- Reviewer runtime ~10 min each (626s / 792s measured), not the earlier 35-min estimate.

## Constraints / Out-of-scope

- **No signed byte**: approved plan, Contract v3, the 7 N0 schemas. Verify landing sites with
  `git log --diff-filter=A` and re-hash the two immutable blobs before committing — do not
  trust this plan's claims.
- **Round-1 and round-2 evidence frozen** (V3-D9). Round 3 gets its own root
  `ResearchSystem/generated/document-assurance/shadow/round-3/**`.
- **`.goals/LEDGER.md` untouched** (excluded at N1–N3; sync only at a node boundary, separate
  out-of-node commit, `1e34a1e` pattern). The durable ledger is the N3 record's resume pointer.
- **N3 record §8 is append-only; §9 rows may be sharpened but every change is logged in §8.**
- **Never `git checkout --`** (repo incident). Mutation-verify restores from byte-checked
  scratchpad copies.
- **Two commits, not one**: the amendment (out-of-node, `8efe3e9` pattern, kind in title) and
  round 3 + record updates (in-node — `N3/**` + `shadow/**` are N3's roots).
- **Round-3 dispatch prompts must contain no expected verdict and no worked-example answers.**
- OUT: everything in ruling 5 above; repairing the round-2 WorkSpec maps (the imperfect maps
  ARE the test subject); fixing N3-R3/R4/R5 or any pilot source; touching `rsc.py` /
  `EXECUTION.md` / `README.md`.

## Steps

- [x] 1. **Preflight**: confirm base `48d82b6`, working tree state as described, suites green
      (113 / 203 / 39 / 20 / 29), `repo-audit.py` exit 0. Re-verify landing-site signature
      status independently.
- [x] 2. **Task 1 (N3-R6) — de-contaminate the worked examples.** Replace both examples in
      `REVIEW.md` §"When the map is incomplete" with **synthetic cases drawn from neither
      shadow subject** (not the A1 amendment episode, not the P3 inventory batch). Same
      teaching shape: one disclose-and-continue, one stop. See Open decisions for material.
- [x] 3. **Task 2 — disposition semantics.** In `review.schema.json`
      `$defs/perObligationDisposition/properties/disposition/description`: rewrite so
      (a) `SUPPORTED` = the reviewer established the claim from evidence at the pinned
      revisions (package members or beyond — coverage disclosed via the **existing**
      `note` / `residual_uncertainty` fields, NO new fields; ruling 3 withdrew
      `established_from`/`missing_members`), matching how all four real reviews actually
      filled it; (b) the `NOT_SUPPORTED`/`UNVERIFIABLE` overlap
      is split — `NOT_SUPPORTED` = evidence **contradicts** the claim; `UNVERIFIABLE` = could
      not establish either, **including** "the needed evidence is not reachable" (previously
      ambiguous between the two — run-a1's `ob-child-id` vs this session's branch-B sketch
      proved two reviewers label the same state differently). Mirror the same split in
      `REVIEW.md`'s `UNVERIFIABLE` section.
- [x] 4. **Task 3 — floor, not ceiling.** In `REVIEW.md`: state the package is the
      **guaranteed minimum the executor must deliver**, not a bound on what the reviewer may
      read; recast the "refuse a package" list by what actually load-bears — KEEP digest
      mismatch (control-plane tamper evidence) and branch-instead-of-commit (payload
      identity). The missing-member downgrade is **scoped** (audit finding 1): the six
      schema-mandated roles (raw_instruction / resolved_plan / candidate_artifact /
      fulfillment / manifest / coverage) remain a freeze-time hard failure — the schema
      `allOf` makes such a package structurally invalid, so it can never be validly frozen
      and never legitimately reaches a reviewer; one that arrives anyway is refused as
      before. What is DOWNGRADED to finding-and-continue is **conditional/completeness
      membership** — `source_input` presence and `check_result` counts (the N3-R4
      `CHECKS-OMITTED` class) — which under floor semantics costs the reviewer effort, not
      validity. `check_package` tooling and the schema `allOf` stay unchanged.
- [x] 5. **Task 4 — evidence discipline (new section in `REVIEW.md`).** (a) Tree material is
      read ONLY at pinned revisions (`git show <rev>:<path>`), never the worktree — a check
      observed on the worktree says nothing about the reviewed bytes (round-2 f07 precedent);
      (b) the uncommitted control plane is read from the working tree and must be verified
      against the frozen package digests before being relied on; (c) the package digest itself
      must come **out-of-band from the dispatching party**, never from the package file (the
      chain is out-of-band digest → member digests → bytes); (d) **reconcile floor semantics
      with contract §5 explicitly** (audit finding 3): the verdict stays scope-relative to
      "the frozen subjects and review dimensions" (§5, immutable); disclosed out-of-package
      reads at pinned revisions widen the **declared review dimensions**, and the coverage
      disclosure in `residual_uncertainty` is what keeps §5 true of the result. Label this as
      REVIEW.md's reading of §5, not a derivation — same convention as the
      collision-precedence rule.
- [x] 6. **Task 5 — stopping criterion + `package_ref`.** (a) R7-ii: redraft the stop
      criterion — "nothing in the frozen package can settle it" becomes "cannot be established
      from any evidence at the pinned revisions" (coherent with floor semantics), with an
      explicit exemption: **process claims** (read order, review-record requirements) are
      honesty ceilings, never `SPEC_GAP` grounds. (b) R8: document in both the schema's
      `package_ref` description and `REVIEW.md` that the digest is
      `canonical_digest(package)` — a canonical-JSON digest, NOT the file's bytes
      (`sha256sum` will not reproduce it; CRLF checkouts must not change package identity) —
      with the one-line reproduction command.
- [x] 7. **Tests + mutation-verify.** If (and only if) any guard or schema `required`/enum
      changed: update pinning tests, then neuter → red → restore from byte-checked scratchpad
      copies. Expected: this round is description/instruction-layer only → likely NO
      guard change; verify that assumption by grep before skipping. Re-run all suites either
      way; update any golden-view test broken by description text.
- [x] 8. **Commit the amendment** — out-of-node, `V3-REVISE-REVIEW-CLARITY-AMENDMENT-v1` (or
      similar kind-in-title), exactly the changed review-layer paths. Re-hash the two
      immutable blobs first. → **`eca4902`**
- [x] 9. **Register N3-R9 in the N3 record** (§9 row + §8 log entry): the ReviewPackage's only
      load-bearing function is pinning the uncommitted control plane; tree-member digests are
      redundant (content-addressed by pinned commit); member-completeness loses consequence
      under floor semantics; a commit-first workflow would supersede the whole layer — hits
      N2-signed acceptance (N2-A1) → 特例 bucket, versioned successor only. Also log this
      session's floor/ceiling ruling and the withdrawn proposals so the reasoning survives.
- [x] 10. **Build round 3** (corrected per audit finding 2): derive **all 7** round-2 scripts
      — build_round2's five (`run-a1/build_run.py`, `run-a1/run_evidence.py`,
      `run-p3/run_shadow.py`, `freeze_packages.py`, `measure.py`) **plus `freeze_only.py`
      and `validate_review.py`**, which are round-2-only (no round-1 originals) yet required
      by steps 10 and 12. Substitution table is **two kinds only**: `round-2` → `round-3`
      paths and `-r2` → `-r3` run ids. Do **NOT** carry over build_round2's `parents[N]`
      increment — rounds 2 and 3 sit at equal directory depth, so bumping `parents` would
      break `RS_ROOT` resolution in every derived script. Assert round-2 unmutated (same
      check build_round2 runs for round 1). Run the mechanical layer (expect 8/8, 7/7 PASS
      again), then the derived `freeze_only.py` **before** any review. WorkSpec maps stay
      deliberately unrepaired.
- [x] 11. **Dispatch two FULL reviews** in fresh contexts (opus), one per run, round-3 roots,
      out-of-band package digests in the prompts, independence constraints as round 2 PLUS:
      do not read `shadow/round-2/**` (a previous reviewer's verdict on the same subject).
      Prompts name no expected verdict and quote no example content.
- [x] 12. **Validate both results** (`validate_review.py`), exercise the binding guard
      post-review (`freeze_packages.py` round-3 copy), re-run `measure.py` and every
      deterministic suite — **figures last** — then append the round-2 → round-3 comparison to
      N3 record §8 (append-only). **The comparison MUST state the confound** (audit finding
      4): round 3 differs from round 2 in the whole amendment-2 bundle (de-contaminated
      examples AND revised criteria), so a verdict delta is attributable to the bundle, never
      to de-contamination alone. In particular run-p3's verdict may legitimately move — the
      new stop wording reaches `P3-to-P4.md`, which amendment-1's wording let the reviewer
      decline (N3-R7(i): "materially affected my verdict") — report that as the criterion
      change working, not as noise. Then update the resume pointer.
- [x] 13. **Commit round 3** in-node (`V3-N3-SHADOW-ROUND-3-CANDIDATE-v1`), all paths under
      the two N3 roots. Then hand the adoption decision back to the user — this plan takes no
      decision. → **`2672abf`**

## Acceptance (done = ?)

- The five fixes landed; no signed byte touched (verified by re-hash, not assumed); changed
  paths classified per commit.
- Any behavior-bearing change mutation-verified (neuter → red → byte-checked restore); if none
  existed, the grep proving so is recorded.
- All suites green immediately before figures were written; `repo-audit.py` exit 0.
- N3-R9 registered; §8 entries record this session's rulings (floor/ceiling, withdrawn rules,
  freeze 反事实).
- Rounds 1 and 2 byte-untouched; round 3 under its own root with `-r3` run ids (V3-D9).
- Both round-3 reviews validate `check_review_result : clean`, produced in fresh contexts from
  contamination-free instructions; dispatch prompts contain no expected verdicts.
- Before/after (round 2 → round 3) comparison appended to §8 **with the bundle-confound
  caveat stated**; resume pointer current.
- Adoption decision re-taken **by the user** (plan ends at hand-off, not at a verdict).

## Resume pointer

当前指针: **DONE.** Round 3 complete and committed (`2672abf`). run-a1
`REVIEWED_NO_BLOCKER`+`INCOMPLETE`+disclosure (1 newly-coined unit); run-p3
`CHANGES_REQUIRED` — moved off round-2's `SPEC_GAP` via floor semantics, verdict driven by
the count blocker (4th reproduction; N3-R3 twice sharpened). §8 carries the comparison with
the bundle confound. **The adoption decision was taken: `ADOPT_DOCUMENT_V3`, 2026-07-21**
(N3 record §8; closeout committed as `V3-N3-ADMINISTRATIVE-CLOSEOUT-v1`). The three
migration-root review notes are committed (`f01502f`). Remaining out-of-node residue the
user routes: this plan file; `.goals/LEDGER.md` sync lands at N4.

## Notes

- **Execution deviation (2026-07-21, logged per §4):** the ceiling wording N3-R7(i) quotes —
  *"what the reviewer is entitled to review"* — lives in `review.schema.json`'s **root
  description**, not in `REVIEW.md`. Task 3 as written named only `REVIEW.md`; leaving the
  strongest ceiling statement standing in the schema while REVIEW.md declares floor semantics
  would recreate the two-readings defect at another surface, so the root description's opening
  phrase was corrected too. Same landing file, description-only, V3-N2-authored, no signed byte.
  **Ratified — approved-by-user: 2026-07-21** (追认, taken during the independent review-agent
  checkpoint; ratification is the user's act, the review agent only recommended).
- **Step 7 outcome:** description/instruction-layer only, as predicted. Schema diff = 6 lines,
  all inside description strings (grep count of non-description +/- lines: 0); zero guard /
  `required` / enum changes → no pinning-test update, no mutation-verify needed. All five
  suites re-run green after the edits.
- **Worked-example material:** fresh synthetic cases invented (plan default; the API-migration
  case was NOT reused, so no user ruling was needed).
- **Checkpoint outcome (2026-07-21):** the user's independent review agent evaluated
  `eca4902` + round-3 build + prompts before dispatch — 4/4 PASS, plus findings L1–L5 and
  F1–F5. Dispositions (user-approved): L1 + L2/L4/L5 → prompt hardening (history bars +
  shadow-tree allowlist); L3 → accepted; F4/F1/F2 → amendment 3 `c07d682`
  (`V3-REVISE-REVIEW-CHECKPOINT-AMENDMENT-v1`, REVIEW.md only); F3/F5 → registered in N3
  record §8. Round 3 therefore measures the amendment-2+3 bundle — the §8 confound statement
  and `build_round3.py` docstring updated to say so. Packages NOT re-frozen: REVIEW.md is not
  a package member, digests unchanged.

- **Audited 2026-07-21 by an independent agent** (~30 claims checked mechanically against the
  repo): 4 ERROR + 1 NIT, all folded into steps 3/4/5/10/12 and the Goal above. Everything
  else verified clean — all six commit hashes, both immutable blobs (`8ad404b1` / `b2dbdf75`),
  all four landing sites first-added at `0ba649c` (V3-N2), exactly 7 N0 schemas, round-2
  verdict facts, N3-R9 absent as expected, base == HEAD, and step 7's "description-only, no
  guard change" assumption (nothing outside the schema quotes the old wording; golden-view
  tests pin rendered values, not descriptions; the vocabulary sweep skips descriptions).
- **Considered and defaulted OFF**: splitting round 3 into an R6-only round plus a
  full-bundle round to de-confound attribution — doubles review cost for attribution
  precision the adoption decision does not strictly need. User may override before step 10.
- **Open decision (execution-time, ask the user only if reusing):** replacement example
  material. Default = invent fresh synthetic cases (no ruling needed). The in-session
  API-migration case is good material but was ruled "不写" when offered as a *third* example;
  reusing it as a *replacement* needs an explicit OK.
- Amendment 1's ceiling notes stay true and stay in place: the disclosure guard matches ids as
  substrings (traceability, not explanation); the collision-precedence rule in `REVIEW.md` is
  labelled as that document's rule, not derived from V3-D6/D7.
- The `ledger-reminder` Stop hook will fire and ask for `.goals/LEDGER.md` — it is a known
  false positive during N1–N3 (memory note `v3-ledger-lives-in-the-node-record`); the answer
  is the N3 record.
- Reviewer cost basis for estimates: ~10 min per FULL review (measured round 2).
