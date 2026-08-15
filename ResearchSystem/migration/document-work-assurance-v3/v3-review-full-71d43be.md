# FULL review — `6f2fde95186bcb8cf6d540de89a9050cd05a748b..71d43bef96736ceee5f19b71592a5205855c29bc`

Independent FULL review of Phase C3 (product-entry group; M9 alone — M8/M10 were closed by
C0) of `harness-deletion-first-stabilization`. Verdict at the end; implementation first
(`R3`), process and boundary second. Every figure below was re-derived on this machine; no
number from the journal, the commit body or the ledger was accepted as reported (`R2`).

**Verdict: `REVIEWED_NO_BLOCKER`.** 0 blockers, 1 non-blocking finding (bank-shaped),
2 observations. The bind template now does what the defect table wrote for M9, every one of
its new guards was demonstrated to bind by mutation on this machine, the RED claim
reproduces exactly, and the round stayed inside every declared and permanent boundary.

## 1. Subject, re-derived

Handed one range and nothing else. `git log` over it: exactly one commit, `71d43be`
(`V3-PHASE-C3-M9-v1`), self-named a candidate commit (`E8` kind named). At session start
`git rev-parse HEAD` = `71d43be…` = the range tip and `git status --porcelain` was empty;
`.harness/review-pending.json` is live with kind `construction-round`, this exact range,
dispatched `2026-07-30T09:41:31+00:00` — 10 s after the candidate's commit timestamp, and
the branch has taken no commit since (`E9`'s window intact; this record is the only commit
it admits; `E12`'s tip-is-HEAD condition holds — nothing written after the range's tip is
dropped by it).

Changed paths, classified by hand (`git diff --name-only`): the template under repair
(`assurance/templates/run-v2/run_bind_v2.py`, +209/−20), its usage doc
(`assurance/templates/run-v2/README.md`, one sentence appended to bullet 4 — verified: the
three added lines are one sentence; that file is not among the eight instruction-layer
members and is no prose successor of governed text, so the commit's not-an-E10-member claim
holds), the round journal (`document-harness/journal/c3-2026-07-30.md`, new), and one new
review-side test module (`test_run_v2_template_bind.py`, 13 tests). Exactly the round's
declared boundary; no rsclib module, no schema, no contract, no instruction-layer file.

Round context re-derived from the repository: the ledger's NEXT pointer names Phase C3 with
only M9 remaining; the plan's defect-table row 36 carries M9 verbatim (写死读
`review-full.json`、只绑一个 ref，无 `repair_round` 分支 → 按 repair_round 读 full/verify，
`review_refs` 绑全) and Step 4.6's disclosure block confirms M9 was deliberately left to C3.
The journal records the opening rulings (card OK'd, cold read discharged by citation, M9
shape = as the defect table wrote it, riders dispositioned), so nothing load-bearing is
chat-only (`R2`; the card interaction and the user's "OK" are process claims, marked in §7).

## 2. M9 — the implementation does what the defect row says

The three defect clauses, each traced to committed code:

- **按 repair_round 读 full/verify** — `round_documents(repair_round)` returns
  `["review-full.json"]` at round 0 and appends `review-verify.json` from round ≥ 1; the
  operative review is `reviews[-1]` (round 0: the FULL; round 1: the VERIFY). The frozen
  candidate schema pins `repair_round` to `enum [0, 1]` and `review_refs` to
  `maxItems: 2`, so the "≥ 1" spelling cannot admit a third round past the faithfulness
  gate's `validate_n2`. A repaired round additionally loads
  `control/user-decision-repair.json` and runs `flow.check_verify_outcome(operative,
  repair)` — re-read in full at `flow.py:553-633`: it refuses a non-VERIFY document
  (NOT-VERIFY), reconciles the VERIFY's declared scope against the user's approved finding
  set in both directions (SCOPE-MISMATCH), refuses a VERIFY answering no repair
  (VERIFY-WITHOUT-REPAIR), and stops on SPEC_GAP or any blocker still standing. Round 0
  never demands a repair decision (its own negative-control test).
- **Refusal before anything else** — the missing-file check runs before any review, state
  or spec is read; the refusal fixtures deliberately create no control documents, so a
  template that consulted anything first would crash to `None` instead of returning 1
  (value-level, the C0 F2 lesson carried forward).
- **`review_refs` 绑全** — `review_refs_of` binds one ref per round that happened, each by
  canonical digest of the document in hand; `unresolved_finding_ids` is derived as the
  union of `review.blocking_findings` over every bound round, never authored. Both match
  the worked precedents (round 0 `runs/w1-r1/run_bind.py`; round 1
  `runs/p3-corr/run_bind_candidate.py` — read: same two-ref binding, same canonical-digest
  kind, same N2-A9 union semantics including the deliberately-listed repaired blocker) and
  the real gate: `summary.check_assurance_candidate` enforces the exact unresolved set in
  both directions (BLOCKER-DROPPED / BLOCKER-INVENTED), review binding by count AND by
  content digest (REVIEW-BINDING-INCOMPLETE / REVIEW-UNBOUND / REVIEW-INVENTED), and
  `repair_round` against the CandidateRecord (ROUND-MISMATCH) — so a bind step whose
  `REPAIR_ROUND` knob lies against a round-1 record is caught by the gate the template
  itself runs before emitting.
- **State re-point** — `review_ref` is advanced via
  `assurance_state.pointer_for("review_ref", …/names[-1], REPO)`; `review_ref` is in
  `DIGEST_PROTECTED_FIELDS` (`assurance_state.py:81-89`), so the operative review's pointer
  carries a bytes digest.
- **Assembly absorption** — the six spec/evidence digestRefs are computed over bytes in
  hand (`digest_ref_of`) because `common.schema.json#digestRef` requires `digest_sha256`
  while five of the six post-supersession-2 state pointers are path-only. For the sixth
  see finding F-1 below. `--emit` writes the candidate canonically and advances
  REVIEWED → AWAITING_FINAL; both the status and `assurance_candidate_ref` are legal under
  the frozen state schema (`assuranceStatus` enum carries AWAITING_FINAL; the field
  exists) — that chain is otherwise untested, disclosed, see §7.

## 3. The tests hold their own weight (`E5`)

All 13 assertions are hand-written literals or whole returned structures; the two STOP
lines are asserted as whole lines via `splitlines()`; the digests expected are computed by
rsclib's `canonical_digest` — the library under its own suites, never the template's own
constant. The template is loaded by explicit file path under a distinct module name. The
`run_main` helper converts any exception into `None`, so every guard failure lands as a
value mismatch, never a reachability-only ERROR. `check_review_result_v2` is a recording
stub in every main-path test (its real form needs a git repository behind the evidence
commit and has its own suites); what the stub pins — which document the template hands the
gate — is exactly the M9 property. The verify-outcome gate, the assembly and
`check_assurance_candidate` in the faithfulness test are the real functions, and the
green path through the real `check_verify_outcome` was confirmed by hand (scope f1 =
approved f1, APPLY_ACCEPTED_FINDINGS, no standing blocker).

## 4. RED and mutation claims, reproduced on this machine (`R8`, `E4`)

Baseline first: the committed template hashes to
`61D591F0E00D1F33603ECE994B71F87173E81862EE35C22424FA20AC7F6E5BB6` (matches the journal's
snapshot line) and the 13 tests run green. Then, template backed up to a scratchpad copy
and hash-verified before and after every probe; restored from that copy, never
`git checkout --`; worktree porcelain-clean at the end.

- **RED**: template reverted to the pre-fix bytes (`git show 6f2fde9:<path>`) → `Ran 13
  tests … FAILED (failures=6, errors=5)`; the eleven red are exactly the journal's list;
  the two greens are exactly the two named negative controls.
- **P1** (`round_documents` returns the FULL always): **5 value FAILs**, zero ERRORs —
  branch test, repaired-refusal test, both recorder tests, real faithfulness gate.
- **P2** (`review_refs_of` binds only the last ref): **2 value FAILs** — exact-list unit +
  faithfulness gate.
- **P3** (`unresolved_ids` reads only the last review): **2 value FAILs** — unit +
  faithfulness gate (BLOCKER-DROPPED f1).
- **P4** (refusal block deleted): **2 value FAILs** — both refusal tests (None != 1); the
  complete-set negative control stayed green.
- **P5** (round-≥1 outcome gate deleted): **1 value FAIL** — its dedicated
  reachability-by-value test.

5/5 probes and the RED all reproduce the journal's table exactly; every red is a FAIL, not
an ERROR. After the final restore: hash equal to the snapshot, 13 green, porcelain empty.

## 5. Figures, re-derived

- Suites, all run here: `tests` 29/29 OK · `tests/stage_control` 20 run, 0 fail ·
  `tests/harness` Ran 39 OK · `tests/document_harness` Ran 169 OK ·
  `tests/document_harness_review` Ran 351 OK. `repo-audit` exit 0.
- 338→351: the only test file the range touches is the new 13-test module, and it runs
  `Ran 13` standalone; 351 − 13 = 338 needs no checkout to verify.
- Frozen surface (`E2`): no path under `ResearchSystem/schema/` or `ResearchSystem/contract/`
  in the range; `git rev-parse 71d43be:<path>` yields `8ad404b1…` (signed plan),
  `b2dbdf75…` (contract), `68031fa2…` (supersession-1) at their paths; porcelain over
  schema + contract dirs empty; `git diff --stat HEAD` over both user-locked oracles empty.
- Cold-read-by-citation (`E10`): re-derived at the *tip* (stronger than the journal's
  base-time check): all eight member blobs identical between `ae4df09` and `71d43be`
  (`33126c19 / 4daab565 / bd490c8b / 70bc521e / 0ae222fd / 7dcdb817 / 68031fa2 /
  e1a2f26b`); `git diff --name-only ae4df09 71d43be` lists nothing under schema/ or
  contract/ and the range adds no prose successor, so the member set is still exactly
  eight and `v3-cold-read-ae4df09.md` (which tabulates these eight, itself end-to-end via
  the `d58969d`/`403fc9a` citations) covers the opening. The citation rule applied is the
  ledger's recorded one; no read was owed, none was dispatched, no budget consumed.

## 6. Findings

**F-1 (non-blocking, bank-shaped) — `digest_ref_of` discards the one protected digest it
has in hand, and the disclosure's premise is false for that field.** The commit body and
journal disclosure 4 justify bind-time recomputation with "post-supersession-2 states
carry path-only pointers on those fields". True for five of the six; false for
`work_spec_ref`, which is in `DIGEST_PROTECTED_FIELDS` (`assurance_state.py:81-89`): a
real state's `work_spec_ref` pointer carries a bytes digest (written via
`pointer_for`, consumed and verified at `review_subject.py:277`'s `_resolve_pointer`),
under the pre-narrowing regime as well. For that one field the template throws away a
digest that binds write-time bytes and substitutes one computed over bind-time disk bytes.
No check outcome changes today — the C2 M6 = option B ruling leaves all six refs
content-unchecked, and the candidate is schema-valid either way — and the state itself
retains the protected digest, so tamper-evidence survives outside the candidate. The named
consequence if never fixed: the AssuranceCandidate presented at FINAL can carry a clean
digest over a silently-rewritten WorkSpec — the user's authorization anchor — although a
binding digest was in hand at assembly. Minimum fix, riding the next batch that touches
`run_bind_v2.py` or the digest policy: `digest_ref_of` copies (or verifies against) a
`digest_sha256` already present on the pointer instead of recomputing, plus one test; and
the one clause in the journal/commit prose corrects to "five of the six" (that half is
wording-level and recoverable from `assurance_state.py` itself). Not inflated to a blocker:
it would burn the single repair on a change no current check can observe.

**O-1 (observation)** — By N2-A9's deliberate semantics a round-1 candidate lists
repaired-and-verified blockers in `unresolved_finding_ids`; the p3-corr precedent paired
that listing with an explanatory disclosure, and the template ships `DISCLOSURES: []`
with a comment that says "leave empty when there is nothing to disclose" — nothing tells a
round-1 author that there *is* something. A FINAL reader could misread "unresolved" as
"repair failed". Same wait-for-a-real-run class as banked F-4; no action this round.

**O-2 (observation)** — The faithfulness test's fixture state carries a path-only
`work_spec_ref`, which a real run's state would carry with a digest; harmless today
(`digest_ref_of` ignores it either way) but it papers over F-1's field. Rides with F-1.

## 7. Boundary, budget, riders, and what was not verified

- **`E9`**: this FULL is the round's first budget consumption; the range holds only the
  candidate; repair and VERIFY untouched.
- **`E8`**: single dense title naming the round; one-paragraph body; kind named
  ("Candidate commit"); parent is `6f2fde9` (no amend); four files, all in-boundary.
- **Riders** (due-claims verified, not accepted): F-a's named ledger text is already gone
  (`grep issues\.py ResearchSystem/HARNESS-LEDGER.md` → no match, exit 1) and this
  candidate does not touch the ledger, so redemption at closeout is the correct due date;
  F-5's owner `assurance_state.py` is untouched by the range and the one new same-shaped
  call site is disclosed; C0-V1's file `test_run_v2_template_fulfillment.py` is untouched
  by the range; F-4 is a ruled direction and the round's use of it is an analogy for the
  untested `--emit` chain, not a redemption.
- **Read in full**: the whole range diff (all four files), the committed template, the new
  test module, the journal, `CONSTRUCTION-CHECKLIST.md`, the ledger, `HARNESS-RIDERS.md`,
  the plan, `summary.py` (bind/check), `flow.check_verify_outcome`,
  `assurance_state.py` (pointer/advance/save/load + protected fields),
  `review.blocking_findings`, `runs/p3-corr/run_bind_candidate.py`, the candidate/state/
  common schema fields cited above. **Sampled**: `runs/w1-r1/run_bind.py` (ref-treatment
  lines), `v3-cold-read-ae4df09.md` (member tabulation), `v3-review-full-f2507a5.md` /
  `v3-review-verify-293f657.md` (F-a definition). **Probed only**: `rsc.py`,
  `review_result_v2.py` internals (its own suites were run, not re-read).
- **Marked, not verified** (`R4`): the preview card render and the user's "OK", the
  M9-shape ruling and the rider dispositions as *chat events* — the journal records them
  and the repository contradicts none of them, but the interactions themselves are process
  claims. **UNVERIFIABLE**: the `--emit` chain end-to-end (no test exercises it; I did not
  execute it either — static checks only: AWAITING_FINAL and `assurance_candidate_ref` are
  legal under the frozen state schema). Mutation results prove the 13 tests bind the
  behaviours probed, not that their force is sufficient beyond them.

## Verdict

`REVIEWED_NO_BLOCKER`. Zero blockers; repair and VERIFY budget untouched. F-1 is
bank-shaped (redeem when a batch next touches `run_bind_v2.py` or the digest policy);
O-1/O-2 require nothing this round. Disposition of F-1's banking is the execution side's
to record and the user's to confirm, per the riders file's own convention.
