# FULL review — maintenance batch `PRE-START-OPT` (candidate `1cfeeac`)

| | |
|---|---|
| round | FULL, construction-side (`CONSTRUCTION-CHECKLIST.md` R1–R10) |
| subject | `aa0dc9278b05c004017dbc99adaf744e99f953b5..1cfeeac2e8da42ae7f4db7244acca8e36675ca87` |
| range content | exactly one commit, `1cfeeac` (`V3-PRE-START-OPT-v1`, kind: candidate) |
| **verdict** | **`REVIEWED_NO_BLOCKER`** |
| findings | 2 low (non-blocking), 3 observations |
| record | this file; the execution side commits it (`R6`) |

`REVIEWED_NO_BLOCKER` means only this: no blocking discrepancy was found within the subject
range and the dimensions below. It is not a proof of correctness.

## 1. Subject, re-derived (`R2`)

Handed one range and nothing else. Everything below re-derived from the repository; no
reported figure accepted.

```
$ git rev-parse HEAD    -> 1cfeeac2e8da42ae7f4db7244acca8e36675ca87   (== subject tip)
$ git status --porcelain -> (empty)
$ cat .harness/review-pending.json
  {"kind": "construction-round",
   "subject": "aa0dc9278b05c004017dbc99adaf744e99f953b5..1cfeeac2e8da42ae7f4db7244acca8e36675ca87",
   "dispatched_at": "2026-08-02T16:25:45+00:00"}
```

Subject tip committed 2026-08-02T16:25:23Z; dispatch follows it; the branch has taken no
commit since — `E9`'s window is intact and this record is the only commit it admits. The
freeze window was re-derived (tip vs dispatched subject), not assumed from the hook — per
the subject's own amended REVIEW.md sentence.

Changed paths, classified by hand: three files, all prose/markdown — `HARNESS-LEDGER.md`
(one sentence deleted), `assurance/templates/run-v2/README.md` (+40, three insertions),
`document-harness/REVIEW.md` (one sentence extended). No code, schema, or generated surface
in the range, so the "no suite re-run owed" claim rests on a correctly classified boundary
(and on the AUDIT-CADENCE precedent's conduct — `0b8b824` was likewise a README+ledger
batch with no suite run, accepted by its FULL). The batch does **not** invoke the un-ruled
ledger item ⑤ (regression-battery layering, recorded await-deliberation only); it cites
precedent, which is the honest ground available.

## 2. What the round is, and its authorization — all in-repo

A harness maintenance batch landing the confirmed pre-START optimizations. The
authorization chain never leaves the repository:

- Rulings ① (mechanical reconciliation) and ② (WorkSpec-only-diff delta re-audit):
  `assurance/runs/p5a-shells/control/audit-rounds.md` §"User rulings" (2026-08-02) +
  ledger pointer row ("①②③ 确认要做、归下个维护批").
- Ruling ③ (checker dry-run self-check): ledger commit `adc480c` (2026-08-03), whose body
  carries the full rule and the full witness sentence — including "the v3 cycle ran the
  dry-run and the crash signature surfaced immediately", which the README restates.
- Checker authoring rules: banked in-repo at the p5a-shells closeout `9ba9bbc`
  ("Checker-hardening material for the next batch: review f1 …, f2 …, f3 …"); the router
  row `aa0dc92` names this batch that next batch. The 2026-08-03 chat re-confirmation is
  corroborated by these records; nothing load-bearing rests on chat alone (`R7` — ceiling
  stated, not a block).

## 3. Implementation, led (`R3`) — does the added text do what it claims?

**Pre-freeze gate section (README lines 46–66).** Both duties transcribe their rulings
accurately, and every witness figure was re-derived at the sources:

- Round 3 f1: audit-rounds.md row 3 reads `175,886 tok / 8.6 min` — the README's "~176k"
  holds; the finding text ("executor failed to apply the v2 instruction narrowing to
  build_run's list … cost one full round — the direct motivator of the 2026-08-02
  pre-freeze reconciliation ruling") matches the README's witness sentence letter for
  letter in substance.
- The v2-checker witness: the cycle-0 SPEC_GAP record (`v3-review-full-d4769f8.md` §3)
  establishes the mechanism — the frozen `check_shells.py::load_shells` calls
  `objects.items()` while the pre-batch compiler emitted a list, so it fails on any real
  base-tree index; the jointly-unsatisfiable expectation surfaced only at the FULL as
  `SPEC_GAP` (`86defbc` record, preamble). The "froze it without ever executing it" and
  "v3 ran the dry-run" halves are carried by the recorded ruling (`adc480c`), which the
  README cites faithfully; as process claims they are marked, not verified (`R4`).
- The "record the command output in the freeze commit's body (measure-last form)" duty is
  the E3 discipline applied to the freeze act — consistent with the layer, adds no
  conflicting obligation.
- Placement: the run-v2 README was ruled "the operative home of the authoring gate" by the
  AUDIT-CADENCE ruling (`0b8b824` body); the new section sits in freeze-chronological
  order before the Authoring gate. Coherent.

**Audit-cadence rule 2 carve-out (README lines 111–116).** Witness accurate: row 6 reads
`211,625 tok / 14.0 min`, verdict COVERED, over freeze v3 that `01a71db`'s body and the
`86defbc` record both state is byte-identical in `check_shells.py` and differs from v2 by
one R1 sentence + a revision note; round 5's header says "repairs all WorkSpec/map-side
(freeze v3 untouched)". The rationale (a from-scratch walk's marginal cost over delta is
re-reading unchanged instruction bytes) is sound, and the named backstop — every FULL's
instruction-completeness recheck — is real (REVIEW.md "What every result must carry").
One letter-level residue: finding L1 below.

**Checker authoring rules bullet (README lines 151–161).** All four rules traced to their
claimed sources, letter for letter:

- parse-must-assert / declared-host: `86defbc` f1 ("parses appendix §A's host column and
  then discards it, so declared-host placement is unchecked … I carried all four by hand:
  zero defects across 148 shells") + audit round 4 o1 and round 6 f1. The 148 figure is
  the candidate's actual shell count (`86defbc` §1) — round 6 f4's "54" is the `frag:`
  namespace count, not a conflict.
- per-file pairing, never pooled: `86defbc` f2 + round 4 o2, verbatim substance.
  "additive and prose modes" generalizes beyond `mode_additive`: grounded — the template
  comparator (`compare_blocks.py`) carries a `--prose` diff mode in the same family;
  defect-class generalization (`E7`), not an unfounded claim.
- whole-order comparison: `86defbc` f1 ("R2's field order is checked only at its first
  key").
- freeze-time disclosure of review-borne script-decidables: f1's fourth item +
  round 6's "Auditor residuals recorded for the FULL reviewer" and round 6 f1's
  disclosure-venue language.
- Both relative links (`../../runs/p5a-shells/control/audit-rounds.md`) resolve from the
  README's directory. The provenance note "banked at `9ba9bbc`; user-activated 2026-08-03"
  matches §2 above.

**REVIEW.md F-1 fix (lines 114–117).** The qualification's factual content is exactly what
README's Local-enforcement row states (per-machine, absent on a fresh clone, "Advisory
automation only"), and the fix does both things the ride's named content offered ("qualify
… or point it at README's Local-enforcement row" — it does both). Observation O1 on the
trailing imperative.

**Ledger edit.** The deletion removes the ride sentence ("随下批 rides：L-3 … + F-1 …")
and nothing else — the surrounding sentences rejoin intact. `git show
1cfeeac:ResearchSystem/HARNESS-LEDGER.md | wc -l` → `119` (cap 120, hook-enforced staged).

## 4. Boundary and record conformance — second (`R3`)

- **Rides redeemed in proper form (`R10`).** F-1: fix applied + sentence deleted in the
  same commit. L-3: the ride's substance was "the next round's opening cites the fresh
  coverage" — the commit body carries the opening cold-read citation with all nine
  per-member blob ids. Both sentences deleted same commit.
- **E10 opening coverage, independently re-verified.** All nine members enumerated at
  `aa0dc92` by `git ls-tree`; blob ids equal the nine the commit body states **and** the
  nine in `v3-checkpoint-read-9541e1e.md`'s table (record commit `10c040b`, title
  verified): `02461be7 / f3a31208 / bd490c8b / 7b553516 / 17ff31bb / 52a97a48 /
  68031fa2 / e1a2f26b / c2b713bf` — the ninth is
  `schema/document-assurance-v3/paragraph-map.schema.json`, the Phase-D open-tail member.
  REVIEW.md (`7b553516` → `c19d8cb`) is the only member touched; its edit is the banked
  R9 ride, which owes no round and no read by the banked classification's own terms.
  "Read in full before the edit" is a process claim — marked, not verified.
- **E8.** Title `V3-PRE-START-OPT-v1` conforms; kind named (candidate); one dense
  paragraph, no trailers. Staging method (explicit paths vs `add -A`) leaves no trace —
  unverifiable post-hoc, disclosed.
- **E9.** No prior FULL exists for this subject (no `v3-review-full-1cfeeac*` before this
  file); this dispatch is the round's FULL; fix leg and VERIFY unspent.
- **Run-v2 README layer status.** The commit's claim (not a layer member; incorporation
  parked to the I/O design batch) matches the ledger's open-question row and the cadence
  FULL's O-1 disposition. Adding rule mass under the parked classification is disclosed
  in the commit body — conduct, not concealment. See O2.

## 5. Findings

### Low (non-blocking — `R3`: not inflated; the user weighs spend-vs-bank at closeout per `R10`)

**L1 — the carve-out's letter excludes its own witness case.** README line 111: "a repair
whose diff touches only the WorkSpec — the frozen instruction byte-unchanged — takes the
delta path in any tier." The witness (round 6) cleared repairs that were "all
WorkSpec/**map**-side" — round 5's f2 flipped `control/paragraph-map.json`
classifications, a file that is neither the WorkSpec nor the instruction. Read strictly,
the next WorkSpec+map repair on a code/schema-tier run fails the "only the WorkSpec" test
and falls back to from-scratch — recreating the witnessed ~212k-token cost the carve-out
was bought to prevent. The ambiguity is inherited from the ruling's own letter
(audit-rounds.md: "touches only the WorkSpec, never the frozen instruction"), so this is
faithful transcription of an ambiguous source, not a transcription error; the failure
mode is conservative (wasted tokens, never a wrong verdict). Named content for the fix
(one clause): make the operative test explicit — e.g. "touches only the WorkSpec and
control-plane map artifacts — the frozen instruction byte-unchanged —", or state the test
as "the frozen instruction is byte-unchanged" alone, which is what the rationale sentence
already argues from and what the commit body's own gloss says ("delta path in any tier
when the frozen instruction is byte-unchanged").

**L2 — f3 of the banked material received no disposition in its designated batch.**
`9ba9bbc` banked three items "for the next batch": f1, f2, and f3 (the stale p4-doc
comparator on the keyed index, `runs/p4-doc/compare_blocks.py:289`, flagged in `86defbc`
f3 precisely because "nobody else is tracking it now"). This batch — the named next batch
— landed f1/f2 as rules and is silent on f3: no fix (out of a doc-only boundary,
correctly), but also no disposition line saying where f3 rides instead. It survives only
in immutable records and the ledger pointer's "素材（review f1/f2/f3）在 record" clause,
which the next ledger compression can drop. f3 is product-run review material, which per
`R10` routes to HarnessIssue, never the rider bank; none is filed. Named content for the
fix (one line, any of): a HarnessIssue triage row for f3, or a disposition clause in the
ledger pointer / closeout channel naming its touch trigger (next comparator or
index-consumer code touch, or P5B intake).

### Observations (`R5` — reported; conclusions are the user's)

**O1 — the F-1 fix's trailing imperative slightly exceeds the ride's named bytes.** "so
re-derive the freeze window (branch tip versus dispatched subject) instead of assuming
the hook held it" is not in the banked finding's named content, but it is the finding's
own named correct behavior ("instead of re-deriving the window") made explicit, and the
duty already follows from REVIEW.md's basis-of-judgment section. No check outcome,
permission, or verdict path moves. Noted for the R9-boundary bookkeeping, not as a
defect. (This review followed the sentence and found it operable.)

**O2 — rule mass continues to accrete on a file whose layer membership is parked.** The
run-v2 README gains its third rules section in three batches (AUDIT-CADENCE, this batch)
while its incorporation question waits in the I/O design batch. The commit discloses the
inheritance deliberately. Under `R5` the shape is reported, not judged: the file now
carries freeze-gating duties and authoring rules that bind executor conduct, governed
outside the instruction layer's read/amendment discipline.

**O3 — the witness's process halves have no evidence lock.** "v2 froze the checker
without ever executing it" and "the v3 cycle ran this dry-run" are carried by the
recorded ruling (`adc480c`), not by any repo artifact that could falsify them (no freeze
commit body records a dry-run either way). The rules stand on the rulings and the
in-repo SPEC_GAP mechanism regardless; marked per `R4`.

## 6. Coverage disclosure (`R4`)

**Read in full:** the subject commit's complete diff and body; `CONSTRUCTION-CHECKLIST.md`
(standing instruction); the review-contract stub (entry point); run-v2 `README.md` at
`1cfeeac` (179 lines); `HARNESS-LEDGER.md` at `1cfeeac` (119); `HARNESS-RIDERS.md` (4
rows); `v3-checkpoint-read-9541e1e.md` (239); `v3-review-full-86defbc.md` (202);
`audit-rounds.md` (137); REVIEW.md lines 1–130 including the amended section.

**Sampled:** `v3-review-full-d4769f8.md` (§2–§3, the load_shells mechanism);
commit bodies `9ba9bbc`, `adc480c`, `0b8b824`, `01a71db`, `a09921b`, `dac74e1` (title);
`document-harness/README.md` (Local-enforcement row); template `compare_blocks.py`
(CONFIG + `mode_prose`); `check_shells.py` (mode inventory by grep).

**Probed only:** `.harness/review-pending.json`; `git ls-tree` at `aa0dc92`/`1cfeeac`
for the nine members and rider file; absence of a p5a-shells `issues/` directory;
absence of any prior record for this subject; `git status` (clean).

**Not verified:** that this review ran in a fresh context (process claim about itself —
the dispatch shape is the evidence); the executor's staging method (`E8`, no trace); the
"read in full before the edit" and dry-run process claims (marked above); the suites the
prior rounds report green — not re-run: no code, schema, or generated surface is in this
range, per §1's hand classification.

## 7. Next action

The user's call on L1/L2 (spend the fix leg, take the bytes channel where its terms are
met, or bank/route per `R10`) and on the observations. A fix leg, if activated, obliges
the targeted VERIFY (`E9`).
