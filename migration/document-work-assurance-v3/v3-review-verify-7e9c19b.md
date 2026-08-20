# Targeted VERIFY — `f3d6226ea67c9e4fb61ecce466bf9a36b2cf41bc..7e9c19bb74a1c8aca5e8308c6d1b944a7df2f1f0`

Targeted VERIFY of the C3 fix round (`R3`: the accepted finding, the whole repair diff,
and the permanent boundaries). Implementation first, process second. Every figure below
was re-derived on this machine; no number from the journal, the commit body or the ledger
was accepted as reported (`R2`).

**Verdict: `REVIEWED_NO_BLOCKER`.** 0 blockers, 0 findings, 3 observations. The fix does
exactly what the accepted finding's minimum fix named, its guard was demonstrated to bind
by mutation on this machine, the RED reproduces exactly, the repair diff contains nothing
beyond the approved scope plus its own records, and every permanent boundary holds.

## 1. Subject, re-derived

Handed one range and nothing else. `git log` over it: exactly one commit, `7e9c19b`
(`V3-PHASE-C3-FIX-v1`), self-named a review-fix commit (`E8` kind named), parent
`f3d6226` (the C3 closeout — no amend), single dense title, one-paragraph body, no
trailers. At session start `git rev-parse HEAD` = `7e9c19b…` = the range tip and
`git status --porcelain` was empty; `.harness/review-pending.json` is live with kind
`construction-round` and this exact range, `dispatched_at 2026-07-30T12:30:00+00:00` —
13 s after the fix commit (12:29:47 UTC), and the branch has taken no commit since
(`E9`'s window intact; this record is the only commit it admits; `E12`'s tip-is-HEAD
condition holds).

Changed paths, classified by hand (`git diff --name-only`, six): the template under
repair (`assurance/templates/run-v2/run_bind_v2.py`), its test module
(`test_run_v2_template_bind.py`, 13 → 16 tests), the riders file (`HARNESS-RIDERS.md`,
header + one row deleted), and three records of the fix itself (plan Step 7 追记,
`HARNESS-LEDGER.md` NEXT block, journal `c3-2026-07-30.md` fix-round section). No rsclib
module, no schema, no contract, no instruction-layer file. Nothing in the diff exceeds
the scope the journal and commit record as user-approved (F-1 via the verify-against
option, O-2, the three bank-tightening rules, `F-1c3` deletion) — no silent boundary
exceed (`E9`).

Round context: the FULL (record `0576322`) returned `REVIEWED_NO_BLOCKER` with F-1
banked; the closeout banked it as rider `F-1c3`; the user then overturned the banking and
activated the round's one fix leg. On closeout-reopening the checklist is silent, and so
is the retired operating contract at `7011916` (searched: its budget clause is the same
"one FULL, at most one user-approved fix, one targeted VERIFY" with no expiry-at-closeout
term) — per the checklist's own preamble that silence is not a defect, and `E9`'s test
("has a valid independent FULL already occurred?") is answered yes by record `0576322`.
So this commit is the fix round and it obliges this VERIFY. The overturning itself is a
chat event: recorded in the journal, the commit body and riders rule ③, contradicted by
nothing in the repository, and marked — not verified — as an interaction (`R4`).

## 2. The accepted finding, answered by the code changing (`E6` both sides)

F-1 (FULL `71d43be` §6): `digest_ref_of` recomputed every field's digest over disk bytes,
discarding the binding digest a digest-protected `work_spec_ref` pointer carries; named
minimum fix "copies (or verifies against) a `digest_sha256` already present on the
pointer instead of recomputing, plus one test". The committed function now does the
verify-against form exactly: an authored `digest_sha256` is copied when the bytes in hand
match it, an `AssuranceFault` refuses the assembly when they contradict it (both sides in
hand at the call — the M7 reconcile-at-generation shape), and only a digestless pointer
gets the compute-from-disk rule. The docstring's false premise ("states carry no digest
on these fields") is gone, replaced by text that states the actual split. The fix is the
named code changing — the riders-header rules are a separately user-ruled process
tightening, not offered as F-1's fix — so `E6`'s refusal clause does not trigger.

Generality checked against the state module, not the journal: `DIGEST_PROTECTED_FIELDS`
(`assurance_state.py:81-89`) holds `{work_spec_ref, start_decision_ref,
repair_decision_ref, final_decision_ref, review_ref}`; of the six `digest_ref_of` call
sites only `work_spec_ref` is protected, so the journal's "in post-narrowing practice
only `work_spec_ref` carries an authored digest" is exact. The module's own policy line —
"a digest that is present is verified wherever it appears, on protected and unprotected
fields alike", with committed pre-narrowing states carrying digests on unprotected fields
— means the fix's general shape (any pointer digest is copied-or-refused, not just the
protected field's) is the policy-consistent one for old states too, not an
over-generalization.

O-2: the faithfulness fixture's `work_spec_ref` now carries
`bytes_digest(json.dumps({"work_id": "w-test"}).encode())`, and `make_run` writes
`work-spec.json` from the identical dict via the identical `json.dumps` — so the copy
path (authored present, bytes matching) runs through `main` and the real
`check_assurance_candidate`, which is exactly what O-2 asked.

## 3. The new tests hold their own weight (`E5`)

The three new tests in `TheAuthoredDigestIsNeverDiscarded` assert whole returned
structures against hand-written paths and `bytes_digest` over a hand-written payload —
rsclib under its own suites, never the template's constant. The refusal test binds by
exception type plus the phrase "changed after it was authored", which greps to exactly
two hits in the repository: the template's raise and this assertion — no unrelated
content can satisfy it, and the direct call to `digest_ref_of` leaves no other
`AssuranceFault` raiser in reach. Test count 16 = 13 (FULL-reviewed) + 3; the module
standalone: `Ran 16 tests … OK`.

## 4. RED and the P6 probe, reproduced on this machine (`R8`, `E4`)

Baseline: the committed template hashes to
`1faae6f4b50de51d35bfc21e903b9a02aa055a0498348de23cd9004f16996fb6` (equals the journal's
post-restore snapshot), backed up to a scratchpad copy and hash-verified before and after
every probe; restored from that copy, never `git checkout --`; porcelain empty at the end.

- **RED**: template replaced with the pre-fix bytes (`git show f3d6226:<path>`, sha256
  `61d591f0…` — the FULL's own baseline snapshot of the candidate) → `Ran 16 tests …
  FAILED (failures=1)`: only `test_a_pointer_digest_contradicted_by_disk_refuses_the_assembly`
  red; the matching-digest and digestless negative controls green. Exactly the journal's
  claim.
- **P6**: guard neutered to the unconditional recompute (the F-1 defect shape, two-line
  body) → the refusal test fails at VALUE (`AssertionError: AssuranceFault not raised`),
  `failures=1`, both controls green — the guard, not reachability, is what the test binds.
- **Restore**: hash equal to the committed bytes, `Ran 16 … OK`, `git status --porcelain`
  empty.

Mutation proves the refusal test has binding force, not that its force is sufficient
(`R4`): when authored and disk agree, copy and recompute are behaviorally
indistinguishable, so only the mismatch case pins the guard — which is the case that
matters and the case P6 exercised.

## 5. Figures, re-derived

- Suites, all run here: `tests` 29/29 OK · `tests/stage_control` 20 run, 0 failures ·
  `tests/harness` Ran 39 OK · `tests/document_harness` Ran 169 OK ·
  `tests/document_harness_review` **Ran 354 OK** (351 at the FULL; +3 authored here) ·
  bind module standalone Ran 16 OK · `repo-audit` exit 0.
- Frozen surface (`E2`): none of the six changed paths is under `ResearchSystem/schema/`
  or `ResearchSystem/contract/`; the schema pack tree is identical across the range
  (`ca47f575…` at both ends); at the tip `git rev-parse` yields `8ad404b1…` (signed
  plan), `b2dbdf75…` (contract), `68031fa2…` (supersession-1) at their paths;
  porcelain over schema + contract dirs empty; `git diff --stat HEAD` over both
  user-locked oracles (`expected-construction-prompt.txt`,
  `test_readme_enumeration.py`) empty, and neither is in the range.
- Instruction layer (`E10`): all eight member blobs at the tip are identical to the
  `v3-cold-read-ae4df09.md` tabulation (`33126c19 / 4daab565 / bd490c8b / 70bc521e /
  0ae222fd / 7dcdb817 / 68031fa2 / e1a2f26b`), and the range touches none of them. The
  fix's claim that `HARNESS-RIDERS.md` is outside the layer holds against that
  enumeration; the riders file has carried its own bank conventions since the 2026-07-29
  split, and a recorded user ruling living outside the layer has standing precedent (the
  ledger's citation rule). No read was owed, none was dispatched.
- Riders: `F-1c3` row gone (redeemed — and its touch trigger fired in the same commit
  regardless: the fix touches `run_bind_v2.py`); the three header rules landed as
  described; pre-existing rows with unnamed targets are deferred by rule ①'s own text,
  not violations of it.

## 6. Observations (non-blocking; none inflated, `R3`)

- **O-1v** — `digest_ref_of` reads disk before consulting the pointer, so an absent file
  raises bare `FileNotFoundError` rather than a refusal that names the situation.
  Pre-existing shape, unchanged by the fix, loud rather than silent — the assembly still
  stops — so no decision goes wrong; noted, not banked.
- **O-2v** — the ledger's "dispatch 已出等路由" was authored in the commit that precedes
  the dispatch marker by 13 s. Structurally anticipatory (the range tip must exist before
  `rsc v3 dispatch` can name it) and true by the time any reader consults the ledger; no
  actor's action changes. Same ordering the C3 candidate showed (marker 10 s after
  commit); wording-level at most.
- **O-3v** (shape, `R5`) — actor-binding conventions now accumulate outside the `E10`
  layer: the riders header ①–③ govern executor behavior at closeout, beside the ledger's
  citation rule. Consistent with the enumeration and with precedent, so no violation to
  report — but whether that governance surface should join the layer (and pay the layer's
  amendment discipline) is the user's question, not mine.

## 7. Disclosure (`R4`)

**Read in full**: the whole range diff (all six files), the committed template, the
committed test module, `HARNESS-RIDERS.md`, `CONSTRUCTION-CHECKLIST.md`, the review
contract stub, the FULL record `v3-review-full-71d43be.md`, the journal's fix-round and
GREEN/mutation sections, both closeout and fix commit messages,
`assurance_state.py` docstring + `DIGEST_PROTECTED_FIELDS`. **Sampled**: the retired
operating contract at `7011916` (budget/closeout language), `v3-cold-read-ae4df09.md`
(member tabulation), the C3 FULL/closeout commit stats, journal lines 70–99,
`.goals/plans/harness-deletion-first-stabilization.plan.md` (oracle declaration + Step 7
hunk). **Probed only**: `rsc.py --help` (locating repo-audit; the audit itself was run,
not read), the suite runners. **Marked, not verified**: the user's overturning of F-1's
banking and the approved fix scope as chat events — the journal, commit body and riders
rule ③ record them and the repository contradicts none of them. **UNVERIFIABLE,
unchanged from the FULL**: the `--emit` chain end-to-end (no test exercises it; the fix
does not touch it beyond `digest_ref_of` running earlier in `main`).

## Verdict

`REVIEWED_NO_BLOCKER`. The accepted finding is answered by the named code changing, the
guard binds, the repair diff stays inside the approved scope, and the permanent
boundaries hold. C3's budget is now fully spent: one FULL, one user-approved fix, this
targeted VERIFY. Nothing here blocks the closeout's advance to Phase C4.
