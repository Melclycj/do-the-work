# Checkpoint read — Phase A instruction diet (`820b287`)

Subject: `2b5fa2803f840970ceae5164cb2d9c99893b4917..820b287da5a2624b7d4da65f6d50f8ae13758340`
(one commit, `V3-PHASE-A-INSTRUCTION-DIET-v1`). Round derived from the repository: Step 2 of
`.goals/plans/harness-deletion-first-stabilization.plan.md`; the read it owes is that plan's
Step 3. Performed under the two contracts as they stood at `7011916` — the checklist's own
header withholds reliance until this read, so it is the subject here, not the authority.

**This is a read, not a FULL.** Review contract §12: a checkpoint read consumes no plan-§8
budget, carries no node verdict, and "is never banked as a node's FULL". Phase A's FULL is
therefore unspent. Findings are tiered per §13. If the user instead classifies this dispatch
as Phase A's FULL, the corresponding verdict on the must-fix set below is `CHANGES_REQUIRED`
— but that classification is the user's, not mine (execution contract, role table).

## Subject re-derivation

| Item | Re-derived value |
|---|---|
| tip == `HEAD`, branch | `820b287da5a2624b7d4da65f6d50f8ae13758340`, `document-work-assurance-v3` |
| changed paths | 8 (7 M, 1 A) — classified by hand below |
| worktree | clean except untracked `ResearchSystem/docs/` (Phase D disposition per `2b5fa28`; not smuggled into the subject) |
| suite | `432 passed in 60.65s` — re-run, matches the claim |
| repo-audit | `exit=0`, `RESULT: clean` — re-run, matches the claim |
| plan blob | `8ad404b12b3242e700d0ad215048dffccada7d9c` ✓ |
| contract blob | `b2dbdf752d8c155e4c65b14b5f420b880b8184a1` ✓ |
| supersession-1 blob | `68031fa2ca31272e31da0d42a9a02189d28fcc21` ✓ |
| both oracles + `schema/document-assurance-v3/` + `ResearchSystem/contract/` | `git diff` empty across the range ✓ |
| checklist E1–E12 + R1–R8 content lines | **51** (lines 16–69 less blanks and the one heading) — the disclosed overage of 1 over the plan's ≤50 is accurate |
| stub length | 5 lines each ✓; first line dated ✓ |
| `7011916` as full-text anchor | `git diff 7011916 2b5fa28` on both contracts is empty ✓ |
| REVIEW.md → history move | `REVIEW.md:25-81` @`2b5fa28` == `history/REVIEW-v1-package-flow.md:9-65`, **diff empty, 57 lines** ✓ |
| bank clearance | `nd-F1`'s lead-in and `O3`'s two read flags were sentences of the retired text; both gone with it, and neither is reproduced in the checklist ✓ |

Per-path classification: plan (tracker + resume pointer), HARNESS-LEDGER (status + NEXT,
bank bullet deleted), CONSTRUCTION-CHECKLIST (banner + E8/R2/R8), EXECUTION.md (1 pointer),
REVIEW.md (2 sections out, stage marker shrunk, 1 pointer), history/REVIEW-v1-package-flow.md
(new), 2 contracts → stubs. All inside the round's declared boundary.

## Must-fix

**MF-1 — E2 forbids what this plan's own remaining steps require, and this commit already did it.**
E2: *"Frozen bytes are untouchable: … existing files under `ResearchSystem/contract/` and
`.goals/plans/`."* The subject modifies `.goals/plans/harness-deletion-first-stabilization.plan.md`
(an existing file under `.goals/plans/` since `2b5fa28`), and plan Step 11 mandates
*"本 plan 状态改 done"* — so Steps 3–11 each violate E2 as written. The source (plan line 46,
*"`.goals/plans/` 既有文件"*) carries the same over-breadth, but E2 is what will govern.
**Minimum fix:** scope E2's clause to signed/approved plan bytes, or except the active plan's
tracker and resume pointer.

**MF-2 — R5 inverts the honesty ceiling it compresses, with no authorization in the repository.**
R5: *"You may report that a mechanism should not exist and recommend its deletion; the
conclusion is the user's."* Source review §10: *"`this needs no guard because it should not
exist` is not [available to me] … I cannot conclude it should go; I can report the shape, and
the user can ask the question I structurally cannot."* Source execution contract, scope rule 1:
*"a review is structurally incapable of concluding it … no finding will say delete this."*
The sources bar the reviewer from the claim on evidentiary grounds (the subject is always the
code that exists); R5 converts that into a permission and keeps only the authority half. This
position was specifically litigated (C5, `1d25aae`) and settled the other way. The plan's Step 2
asserts the widening (*含"reviewer 可建议删除"R5*) but no ruling for it appears in
HARNESS-LEDGER's rulings block — chat-only load-bearing material, which R2 itself makes a
finding. **Minimum fix:** restore the ceiling's direction (report the shape as an observation;
the question and the conclusion are the user's), or record the ruling that widened it.

**MF-3 — the checklist uses "instruction layer" as an operative term and never defines its extent.**
E10 governs *"Instruction-layer edits"* and owes *"a cold read of this layer … at each round's
opening"*. Both sources defined the membership — *"`document-harness/README.md`, `EXECUTION.md`,
`REVIEW.md`, these two operating contracts, and any versioned successor to signed prose
(including prose carried in schema `description` strings when amended)"* — and the definition
sits in the preamble of "Instruction discipline 1–4", a listed compression source. A reader of
the checklist alone cannot tell whether editing a schema `description` owes a read.
**Minimum fix:** one clause in E10 naming the layer's members, with the checklist itself
substituted for the two retired contracts.

**MF-4 — the instruction layer's mechanized reminder now guards two dead files, passes vacuously on them, and does not cover the file that replaced them.**
`tooling/hooks/contract_provenance_check.py` pins `CONTRACTS` to the two contract paths and
requires an added `^\+> 20\d\d-\d\d-\d\d` line. Run against this very commit:

```
v3-harness-operating-contract.md: guard PASSES=True   lines deleted=305
v3-harness-review-contract.md:    guard PASSES=True   lines deleted=360
   matched-line: +> 2026-07-27 superseded by [`ResearchSystem/document-harness/CONSTRUC…
CONSTRUCTION-CHECKLIST.md: path in CONTRACTS tuple = False   (edited this round: 18 lines)
```

The guard passed on a commit that deleted both provenance blocks entirely, because the stub's
permanent supersession line matches the "new entry" pattern — the expectation is now satisfied
by the guarded file's own standing content (E5's shape). Meanwhile the live governing file is
outside the tuple, and it carries no provenance block for future entries to land in.
`document-harness/README.md:27` still presents this as the instruction layer's mechanized
reminder. **Minimum fix is a disposition, not a line:** either retarget `CONTRACTS` to
CONSTRUCTION-CHECKLIST.md and give it a provenance block, or delete the guard. E6 argues for
the latter — *"a fix that requires new machinery is the signal to re-question the guarded
thing"* — and the guard is self-declared advisory, per-machine, untracked, bypassable and
untested. Reporting the shape only; the conclusion is yours. Either way `README.md:27` must
follow.

**MF-5 — nothing on the construction side now says what a VERIFY covers.**
R3 gives VERIFY its verdict set and E9 calls it *"one targeted VERIFY"*; neither states scope.
Dropped from review §5.4 (a listed compression source, and not in the commit body's
judged-dropped list): *"Check the permanent boundaries even when the round is narrow. VERIFY is
scoped to the accepted findings plus the whole repair diff — the boundaries are checked
regardless."* A VERIFY reading only the checklist would plausibly check the accepted findings
and stop, which is where a repair's own new defects live. **Minimum fix:** append the scope
sentence to R3.

**MF-6 — the anti-conflation clause is gone, three commits after a round was reverted partly for breaching it.**
Dropped from execution rule 1 (*"The read's subject is the amendment text itself, never the
work it governs"*) and from review §12 (*"a checkpoint read is never banked as a node's FULL,
and a node FULL is never stretched to claim it covered the instruction layer"*). `7011916`'s
message records the cost: one of the three must-fix in the reverted round was *"the clause the
round wrote to let its own FULL discharge its rule-1 read, which the review contract's §12
forbids."* E10 now says only that an amendment *"passes an independent read"* — nothing stops
that read being the round's own FULL. **Minimum fix:** one clause in E10.

## Low

- **L-1** E8 lost hard rule 7's commit-**kind** naming (*"candidate / pre-submission correction
  / review fix / closeout / errata — so the review side can attribute it without asking"*).
  E8 now names the *round*, which is a different axis. Not disclosed as dropped.
- **L-2** *"Never self-classify which round consumed what"* is disclosed as carried by
  "E9's user-approved wording plus R1". E9 states the cap, R1 is about independence; neither
  bans the executor from classifying. Given that every recorded escape from the cap took the
  form of renaming a round, the ban is worth its clause.
- **L-3** E5 lost *"assert the whole line, never a substring other content can satisfy"*
  (`assertIn("2", …)` against 40-hex SHAs) — a shape that produced a real finding at `39e4136`.
- **L-4** Review §10 ceilings dropped without disclosure: test strength (*"mutation testing
  proves a test has binding force, not that its force is sufficient"*) and *"a `VERIFY PASS` is
  not a re-certification of the node."*
- **L-5** The operating stub's path-retention reason — *"the review-side stub's dispatch fixture
  names its neighbour"* — is not a fact. The fixture names only the review-contract path, and
  the review stub names no counterpart. The true reason is the clause before it (historical
  records). E10 rule 4's class: a characterization where a derived fact belongs.
- **L-6** E10 gains *"unless the user waives it"*, which the source rule 2 does not contain.
  Waiver is precedented (round ⑤, and this round) but codifying it in the rule is a widening,
  undisclosed in the commit body.

## Observations — no fix owed

1. 51 content lines confirmed against the plan's ≤50; the overage is R8 and the disclosure is
   accurate. Trim-or-accept is yours; R8 closes a real §5.2 omission and I would keep it.
2. R3's `PASS` → `REVIEWED_NO_BLOCKER` is **not** a re-introduction of the reverted `9c13008`
   vocabulary work. It aligns the construction side with signed contract v3 lines 113–114
   (blob `b2dbdf75`, frozen); the old review contract's §4 was the outlier. Undisclosed, but
   a correction.
3. Hard rules 1 (derive `.goals/LEDGER.md` from the node allowlist) and 6 (append-only log
   section) dropped as node-era artifacts. Defensible — there are no node allowlists left and
   HARNESS-LEDGER is declared a live pointer — and E8's change-boundary clause carries the
   general form.
4. `dispatch.py:362`'s comment still says the numbered `§n` form *"belongs to the
   construction-side `v3-harness-review-contract.md`"*; that file no longer numbers sections.
5. `contract_provenance_check.py` has no tests (`grep -rln contract_provenance tests/` → none).
   Predates this round; noted because MF-4 turns on its behaviour.
6. `UNVERIFIABLE` appears in R4 with no slot in R3's verdict sets. It reads as the honest-answer
   discipline rather than a verdict, which is how REVIEW.md:58 uses it.
7. The fixture's *"read it, and the counterpart it names"* now has no referent in the review
   stub. The chain still delivers both sides because the successor is two-sided — but it
   resolves by luck, not by construction. The fixture is user-locked; the stub is not.
8. Review §8's *"which code was churned late"* supplement is absent from both sides. Checked
   and **not** a finding: `dispatch.py:497-505` records the deliberate non-emission and its
   reasoning (ill-defined on a DAG).
9. §1's *"self-check is encouraged, not tolerated"* lost its encouragement framing; E1 now reads
   purely as a prohibition.

## Negative results by dimension

Checked, found nothing: frozen-blob integrity (3/3); both user-locked oracles byte-identical;
schema and `ResearchSystem/contract/` trees untouched; the REVIEW.md extraction is verbatim to
the byte; the history file's forward-reference note (*"cross-references to sections 'below'
resolve in `../REVIEW.md`"*) is accurate — `REVIEW.md:153` still carries the
collision-precedence rule; REVIEW.md's surviving text has no dangling reference to the moved
sections (`:49`'s "floor-versus-ceiling rule is unchanged" reads as continuity with history,
not as a pointer to a present section); no live file outside `migration/`, the archive and the
plan still treats the two contracts as governing; both stub links resolve; `7011916` is the
correct full-text anchor; E10's own additive/subtractive rule is satisfied by this commit's
checklist diff (banner replaced, three clauses added, nothing re-typed); the bank subjects
genuinely ceased to exist rather than being silently carried.

## Coverage

**Read in full:** CONSTRUCTION-CHECKLIST.md; both retired contracts at `7011916` (308 + 375
lines); both stubs; the stabilization plan; HARNESS-LEDGER.md; REVIEW.md (lines 1–75) and the
new history file; contract_provenance_check.py; document-harness/README.md; the dispatch
fixture. **Sampled:** REVIEW.md beyond line 75 (grepped for cross-reference residue);
dispatch.py (the two contract-referencing regions); `.goals/LEDGER.md` (harness row).
**Probed only:** the 432-test suite (run, not read); HARNESS-LEDGER-archive.md (grep).

**Recomputed, never accepted as reported:** suite count, audit exit, all three signed blobs,
oracle and tree diffs, checklist line count, stub lengths, the verbatim-move diff, the
full-text anchor, and the provenance guard's behaviour on this commit.

**Ceilings.** The claim that this round ran in a fresh context is marked, not verified. The
user's approval of the preview card and the cold-read waiver are stated in the commit body and
appear nowhere in the repository; per R7 that is a hint, not a block — I note only that the
waiver's own precedent (round ⑤) is recorded in the ledger while this one is not. Whether the
51-line checklist is *sufficient* governance is not something a read of it can establish; the
first round to run under it is the test.
