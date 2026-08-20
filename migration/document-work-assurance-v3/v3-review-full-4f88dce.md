# FULL review — round `BATTERY-TIERING` (candidate `4f88dce`)

| | |
|---|---|
| round | FULL, construction-side (`CONSTRUCTION-CHECKLIST.md` R1–R10) |
| subject | `17289971a46b15dd7c8b0dc4d4c38cfcdfb30d25..4f88dce662eff10c82b7b22f753975a3b68a225b` |
| range content | exactly one commit, `4f88dce` (`V3-BATTERY-TIERING-v1`, kind: candidate) |
| **verdict** | **`REVIEWED_NO_BLOCKER`** |
| findings | 2 low (non-blocking), 3 observations |
| record | this file; the execution side commits it (`R6`) |

`REVIEWED_NO_BLOCKER` means only this: no blocking discrepancy was found within the subject
range and the dimensions below. It is not a proof of correctness.

## 1. Subject, re-derived (`R2`)

Handed one range and nothing else. Everything below re-derived from the repository; no
reported figure accepted.

```
$ git log 1728997..4f88dce --format='%H %s'
  4f88dce662eff10c82b7b22f753975a3b68a225b V3-BATTERY-TIERING-v1        (the only commit)
$ git rev-parse HEAD     -> 4f88dce662eff10c82b7b22f753975a3b68a225b   (== subject tip)
$ git status --porcelain -> (empty)
$ cat .harness/review-pending.json
  {"kind": "construction-round",
   "subject": "17289971a46b15dd7c8b0dc4d4c38cfcdfb30d25..4f88dce662eff10c82b7b22f753975a3b68a225b",
   "dispatched_at": "2026-08-02T17:33:50+00:00"}
```

Tip committed 2026-08-02T17:33:42Z; dispatch follows it by 8 seconds; the branch has taken
no commit since — `E9`'s window is intact and this record is the only commit it admits.

Changed paths, classified by hand: one file, prose/markdown —
`assurance/templates/run-v2/README.md`, +28 lines, one new section ("Regression-battery
tiering"), inserted whole between the Audit-cadence section and the Instruction authoring
rules. No code, schema, or generated surface in the range. The batch's own battery skip
rests on the AUDIT-CADENCE / PRE-START-OPT precedent, explicitly **not** on the rule it
lands ("the landed rule governs future passes once its round closes") — the circularity a
self-application would have created is avoided, and the conduct matches what the
PRE-START-OPT FULL called "the honest ground available".

## 2. What the round is, and its authorization — in-repo trail

A one-ruling round activating ledger item ⑤ (regression-battery tiering). The chain:

- `a4c4d62` (2026-08-03) recorded item ⑤ **for deliberation** — "noted for deliberation
  … not confirmed" — with the tier shape and the ~7–8-of-~10-minutes figure already in its
  body.
- The ledger pointer row lists "⑤ 回归电池分层（`a4c4d62` 正文）——仍待议".
- The candidate's body states the activating ruling is in-chat, 2026-08-03, and **declares
  itself the ruling's record**. Per `R7` that is the ceiling: the ruling's content is now
  in-repo (the commit body plus the section's own "user condition, part of the ruling"
  paragraph), the act of ruling is not independently visible. Stated, not a block — this is
  the same shape AUDIT-CADENCE and PRE-START-OPT were accepted under, and nothing
  load-bearing rests on chat alone.

## 3. Implementation, led (`R3`) — does the added text do what it claims?

**The tier rule.** Decidable in both directions it needs to be: the tier "is derived from
the actual diff and stated where the verification is recorded … so review can re-classify
it" — re-classification is exactly what §1 above performs, and the venue (commit body or
CandidateRecord) is where every prior round has put it. One letter-level conflict inside
the two-bullet partition: finding L1.

**The battery enumeration is the operative one.** "P2/P4/P5A goldens, schema fixtures,
pytest, `compile --check`" matches the battery legs of the latest evidence pass one for
one — the p5a-shells evidence commit `86defbc` binds `chk-p2-golden`, `chk-p4-golden`,
`chk-p5a-golden`, `chk-schema-fixtures`, `chk-pytest`, `chk-compile-check` (plus
run-specific checks, which the rule correctly leaves untiered: "batch-specific checks
only" still run). No standing leg is omitted — P1 goldens, present in Stage-3 construction
tallies, are not part of the evidence-pass battery anywhere in the p5a-shells record.

**Witness figures.** The suite tallies were re-derived at the source: the p5a-shells FULL
(`v3-review-full-86defbc.md`) tables exactly P2 29/29 · P4 80/80 · P5A 32/32 · schema
fixtures 58/58 · `pytest -q` 556 — the README's "P2 29 + P4 80 + P5A 32 + fixtures 58 +
pytest 556" holds letter for letter. The minutes figure (~7–8 of ~10) is carried by the
ruling record `a4c4d62` only; the one repo-locked duration is the pytest leg —
`chk-pytest.out.txt` at `86defbc` ends "556 passed in 102.02s (0:01:42)" — which neither
confirms nor refutes a multi-leg wall-clock total. Marked per `R4`: observation O2.

**The precedent sentence is accurate.** Both cited rounds re-verified: `0b8b824`
(AUDIT-CADENCE) changed only `HARNESS-LEDGER.md` + run-v2 `README.md`; its FULL
(`v3-review-full-0b8b824.md`) states "No product-run suite was re-run: the batch ships
prose and ledger lines" and returned `REVIEWED_NO_BLOCKER`. `1cfeeac` (PRE-START-OPT)
changed three prose files, claimed "no suite re-run is owed (AUDIT-CADENCE precedent)",
and its FULL accepted that ground while noting the batch did **not** invoke the un-ruled
item ⑤ — which makes "this section makes the practice a rule" the exactly right
description of what this round does.

**The tooling-load-bearing exception's two anchors are real.**
`tooling/tests/document_harness/test_readme_enumeration.py` exists and pins
`document-harness/README.md` by delimited-stem enumeration — a prose edit there can flip
pytest red, so the exception's first instance is genuine content coupling. "The
layer-path mirror" resolves to the `LAYER` tuple in `tooling/hooks/layer_path_check.py`
(its docstring and the tuple's comment both say "mirrors E10's membership sentence"; the
tuple is itself pinned against a hand-written fixture at
`test_precommit_checks.py:189`). The referent is findable — one grep — but the clause
names no path; wording-level looseness, folded into L1's named content rather than
counted twice.

**The revert anchor is self-contained in the locate-and-delete sense.** The section is
one contiguous block (README lines 125–151); grep over the repository for
battery/tiering references finds, outside the section itself, only the ledger's item-⑤
deliberation row, the `a4c4d62` body, and one unrelated use of "tiering"
(finding-tiering, `v3-review-verify-fbe0b63.md`). Nothing operative references the
section — "nothing else in the harness references it" holds today. What deletion would
*restore* is finding L2.

## 4. Boundary and record conformance — second (`R3`)

- **E2.** The single changed path is not among the four frozen blobs and not under
  `schema/document-assurance-v3/`. Frozen surface untouched.
- **E10 opening coverage, independently re-verified.** `git ls-tree` at `4f88dce` over the
  nine members: `02461be7` (checklist) / `f3a31208` (README) / `bd490c8b` (EXECUTION.md) /
  `c19d8cb9` (REVIEW.md) / `17ff31bb` / `52a97a48` (stubs) / `68031fa2` / `e1a2f26b`
  (supersessions) / `c2b713bf` (paragraph-map schema). The eight the body cites equal the
  checkpoint-read table (`v3-checkpoint-read-9541e1e.md`, record `10c040b`, title
  verified); REVIEW.md moved `7b553516 → c19d8cb9` and `git log 9541e1e..4f88dce --
  REVIEW.md` shows exactly one commit, `1cfeeac` — the banked R9 ride, which owes no round
  and no read by the banked classification's own terms (adjudicated in
  `v3-review-full-1cfeeac.md` §4; not reopened here). "Read in full by this session before
  that edit" is a process claim — marked, not verified. No layer member is in this diff.
- **E8.** Title `V3-BATTERY-TIERING-v1` conforms; kind named (candidate); one dense
  paragraph; no trailers. Staging method leaves no trace — unverifiable post-hoc,
  disclosed.
- **E9.** No prior review record exists for this subject (no `v3-review-*4f88dce*`); this
  dispatch is the round's FULL; fix leg and VERIFY unspent. Same-session authorship of the
  PRE-START-OPT closeout and this candidate keeps one role (executor) — `E1` conformant.
- **Ledger.** This candidate, unlike both precedent batches, touches no ledger line: item
  ⑤ still reads "仍待议" at the tip while the activating ruling lands in this commit.
  Within-round staleness the closeout owes; observation O3.

## 5. Findings

### Low (non-blocking — `R3`: not inflated; the user weighs spend-vs-bank at closeout per `R10`)

**L1 — the two tiers' letters conflict for prose files inside tooling/generated trees,
and the conflict's losing side is the section's only non-conservative failure.** Bullet 1
keys on path type ("every changed path is prose/markdown"); bullet 2 keys on surface
("schema, tooling, or generated surfaces touched"). A `.md` under
`tooling/tests/fixtures/` (P4 fixture corpus), or a golden under `assurance/test/` /
`assurance/review-test/` (byte-compared, per those directories' own `.gitattributes`),
satisfies bullet 1's letter while sitting on a surface bullet 2 names — and such files
are battery *inputs*: an edit can flip goldens or pytest red. An executor classifying by
bullet 1 alone reaches "skip" for exactly the change class the battery exists to catch;
the breakage then surfaces at the next tooling-touching batch, attributed to the wrong
round. The exception clause shows the authors knew extension alone is insufficient, but
its instance list stops at two prose files outside tooling trees. Ground: the section's
own tier test admits under-verification for a nameable path class. Named content for the
fix (one clause, either form): scope bullet 1 — "every changed path is prose/markdown
**outside the schema, tooling, and generated trees**" — or mark the exception's
parenthetical exemplary and add the class ("likewise any file under
`tooling/tests/fixtures/`, `assurance/test/`, `assurance/review-test/`, or any path a
bound check reads"; the same edit is the natural place to give "the layer-path mirror"
its path, `tooling/hooks/layer_path_check.py`). Non-blocking because the misread needs a
batch shape no round has yet presented (fixture/golden edits offered as doc-only), and
the rule's own re-classification clause hands every FULL the chance to catch it — §1's
hand classification is the standing backstop.

**L2 — deletion cannot by itself restore "full battery on every pass", because the
precedent ground survives the section it was absorbed into.** The revert anchor promises
that removing the section "restores the prior rule (full battery on every pass)". But
the section's own history sentence establishes that the prior state for construction
batches was the opposite — skipping, sanctioned by two FULL-accepted precedents
(AUDIT-CADENCE, PRE-START-OPT), records that are immutable and remain citable after any
deletion; this round, once accepted, is a third. Post-revert, a doc-only batch citing
that precedent — precisely what `1cfeeac` did, with its FULL's blessing — re-opens the
practice the revert was ruled to end, and the only thing standing against it is the
deleted section's anchor text, recoverable by archaeology but no longer operative.
Ground: the revert unit's restoration claim depends on text outside the unit staying
un-cited, which nothing enforces. Named content for the fix (one clause in the revert
anchor): "the deleting commit's body must state that the AUDIT-CADENCE / PRE-START-OPT /
BATTERY-TIERING precedent is retired with the section — after the revert, a doc-only
pass owes the full battery notwithstanding those records." Non-blocking because the
defect bites only inside a future revert the user personally adjudicates, and the
deleting commit is a natural venue to carry the retirement even without this clause.

### Observations (`R5` — reported; conclusions are the user's)

**O1 — the file now binds every construction batch's conduct, from outside the
instruction layer.** The prior two sections added by this file's recent batches govern
*run authoring* (freeze gates, audit cadence); this one's scope sentence reaches "a
construction batch's pre-commit verification" — every future maintenance batch —
while living in a file no construction session has a standing obligation to open:
`CONSTRUCTION-CHECKLIST.md` does not reference run-v2 README, and the E10 cold read
covers the nine members only. The file's layer membership is the question already parked
to the I/O design batch (ledger row; cadence FULL O-1), and this round raises its stakes
a third time. Unlike `1cfeeac`, whose body disclosed "adds rule mass under the parked
classification, inherited deliberately", this body carries no such sentence. The shape is
reported, not judged; the escalation is the fact worth the user's eye.

**O2 — the minutes witness has no repo lock.** "~7–8 of the ~10 minutes" traces to the
ruling record `a4c4d62` and stops there; the sole committed duration
(`chk-pytest.out.txt`: 102.02s for the pytest leg) covers one leg of six. The tallies —
the half of the witness that the rule's tiers actually turn on — are fully locked
(§3). Same shape as the PRE-START-OPT FULL's O3; marked per `R4`.

**O3 — the ledger's item-⑤ row is stale as of the tip.** "⑤ …——仍待议" stands in
`HARNESS-LEDGER.md` while the commit it points at is superseded by this round's ruling.
Both precedent rounds settled their ledger lines in the candidate; this round evidently
leaves it to the closeout. Noted so the closeout does not miss it — the row's next state
should also record where ④ (audit layer-split) now stands alone in the 待议 list.

## 6. Coverage disclosure (`R4`)

**Read in full:** the subject commit's complete diff and body; `CONSTRUCTION-CHECKLIST.md`
(standing instruction); the review-contract stub (entry point); run-v2 `README.md` at
`4f88dce` (207 lines); `HARNESS-LEDGER.md` at the tip (119 lines);
`v3-review-full-1cfeeac.md` (233); `test_readme_enumeration.py`;
`tooling/hooks/layer_path_check.py`.

**Sampled:** `v3-review-full-0b8b824.md` (§6 suite sentence + §7 verdict);
`v3-review-full-86defbc.md` (tally table); `v3-checkpoint-read-9541e1e.md` (§ member
table); commit bodies `a4c4d62`, `0b8b824`, `1cfeeac`, `86defbc` (body + full stat);
titles `adc480c`, `9ba9bbc`, `1728997`, `10c040b`; `chk-pytest.out.txt` at `86defbc`;
`test_precommit_checks.py` (LAYER-pinning region); `v3-review-verify-fbe0b63.md`
(the unrelated "tiering" hits).

**Probed only:** `.harness/review-pending.json`; `git ls-tree` at `4f88dce` for the nine
members; `git log 9541e1e..4f88dce -- REVIEW.md`; `git status`; absence of any prior
record for this subject; repository-wide greps (battery / tiering / goldens / mirror /
`.md` references under `tooling/tests/`).

**Not verified:** that this review ran in a fresh context (process claim about itself —
the dispatch shape is the evidence); the executor's staging method (`E8`, no trace); the
in-chat ruling as an event (`R7` ceiling, §2); the "read in full by this session before
that edit" process claim; the wall-clock minutes figure (O2); the golden legs' durations
— not re-run: no code, schema, or generated surface is in this range, per §1's hand
classification.

## 7. Next action

The user's call on L1/L2 (spend the fix leg, take the bytes channel — both findings name
their content — or bank per `R10`) and on the observations, O1 in particular since it
feeds the parked I/O design batch. A fix leg, if activated, obliges the targeted VERIFY
(`E9`). The closeout owes the ledger's item-⑤ settlement (O3).
