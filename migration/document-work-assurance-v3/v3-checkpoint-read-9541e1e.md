# Instruction-layer read — `9541e1e1ac91673df1d811aae0d7ce0f682a154e`

`E10` read of the instruction layer at the branch tip after the maintenance + rider-redemption
round's closeout. Not a round: no verdict, no budget consumed (`R3`). Findings tiered
must-fix / low / observation. This dispatch discharges the ledger's **O-5** debt — the two
layer members amended inside the `f4836f7..5f029cd` round (the checklist's three clause edits
at `5f029cd`; REVIEW.md's deliverables section at `991b744`) each owed an independent read
before any round or product run relies on them (`v3-review-full-5f029cd.md` O-5; closeout
`f6c7a74` body; ledger pointer row).

**Findings: 0 must-fix, 1 low (wording-level — R9 ride), 3 observations.** The three
checklist clause edits close exactly the seams their two rider sources name (sources
re-sampled here, not taken from the FULL); the REVIEW.md section's factual claims hold
against the repository; nothing relied on the amended text between amendment and this read.

## 1. Subject, re-derived

`R2`: I was handed one SHA and the phrase *the instruction layer*. Everything below is
re-derived from the repository; no figure from the dispatch prompt, the ledger, or any prior
record is accepted as reported.

```
$ git rev-parse HEAD       -> 9541e1e1ac91673df1d811aae0d7ce0f682a154e   (== subject)
$ git status --porcelain   -> (empty)
$ cat .harness/review-pending.json
  {"kind": "layer-read", "subject": "9541e1e1ac91673df1d811aae0d7ce0f682a154e",
   "dispatched_at": "2026-08-01T15:01:52+00:00"}
```

The subject commit dates 2026-08-01T14:46:54Z; dispatch follows it and the branch has taken
no commit since — `E9`'s window is intact and this record is the only commit it admits.

`E10`'s sentence at the subject commit (checklist blob `02461be7`, read in full) governs the
member set: eight enumerated members plus the open tail realized at Phase D
(`v3-checkpoint-read-d01615b.md` O-1 — the paragraph-map schema's amended `description`
strings). The open tail was re-swept, not inherited: `git diff --name-only d01615b 9541e1e
-- ResearchSystem/schema/` returns `fixtures/cases.json`, `object.schema.json`,
`persisted-index.schema.json` — all outside the `document-assurance-v3` pack; their
classification is settled at O-1 below (outside the layer). No other prose added in the
window supersedes text this harness governs: the run-v2 template README's new
authoring-rules section (`57dbaa0`) registers rules that *live* in EXECUTION.md and the
governing plans and forbids restating them — template documentation, per the `d01615b`
precedent classification; contract-side changes (`ResearchSystem-Contract.md`,
`adapter-map.md`, A1 amendments, activation signature) are the ResearchSystem product's
instruments; the rest are records, data, code, plans and thesis files by their own headers.

| # | blob at `9541e1e` | lines | member | vs. last recorded read |
|---|---|---|---|---|
| 1 | `02461be7` | 161 | `document-harness/CONSTRUCTION-CHECKLIST.md` | **changed** (`1ced10a1` → at `5f029cd` only) |
| 2 | `f3a31208` | 37 | `document-harness/README.md` | same since `d01615b` read |
| 3 | `bd490c8b` | 153 | `document-harness/EXECUTION.md` | same since `d58969d` read |
| 4 | `7b553516` | 256 | `document-harness/REVIEW.md` | **changed** (`d050b05a` → at `991b744` only) |
| 5 | `17ff31bb` | 5 | `migration/…/v3-harness-operating-contract.md` (stub) | same since `784e49b` read |
| 6 | `52a97a48` | 5 | `migration/…/v3-harness-review-contract.md` (stub) | same since `784e49b` read |
| 7 | `68031fa2` | 124 | `contract/…-v3-supersession-1.md` | same since `d58969d` read |
| 8 | `e1a2f26b` | 113 | `contract/…-v3-supersession-2.md` | same since `403fc9a` read |
| 9 | `c2b713bf` | 44 | `schema/document-assurance-v3/paragraph-map.schema.json` (open tail) | same since `d01615b` read |

Blob ids from `git ls-tree 9541e1e` / `git rev-parse 9541e1e:<path>`; line counts from
`wc -l` at the identical worktree (`git hash-object` of the working checklist = `02461be7`,
worktree clean). Each changed member changed in exactly one commit
(`git log --oneline d01615b..9541e1e -- <member>`): member 1 only at `5f029cd`, member 4
only at `991b744`. The three commits after the round's FULL record was dispatched touch no
member: `02f24bb` (the FULL record file only), `f6c7a74` (`HARNESS-LEDGER.md` + the run-v2
template comparator), `9541e1e` (`.goals/LEDGER.md` router row only).

## 2. Coverage — `E10` citation clause, per-member

Seven members are blob-unchanged since a recorded end-to-end read of each; every citation
verified against git, not against the records' tables:

- Members 2, 9 — read in full by `v3-checkpoint-read-d01615b.md` (§1 rows `f3a31208`,
  `c2b713b`; §7 *Read in full*). `git rev-parse 9541e1e:<path>` equals each cited blob.
- Member 3 — read in full by `v3-checkpoint-read-d58969d.md` (row `bd490c8b`), citation
  chain verified by the `d01615b` read; blob equality re-checked here.
- Members 5, 6 — read in full by `v3-checkpoint-read-784e49b.md` (rows `17ff31bb`,
  `52a97a48`); blob equality re-checked here. Member 6 additionally read this session as the
  standing-instruction entry point.
- Member 7 — read in full by `v3-checkpoint-read-d58969d.md` (row `68031fa2`); member 8 —
  by `v3-checkpoint-read-403fc9a.md` (row `e1a2f26b`); blob equality re-checked here.

Members 1 and 4 read in full here at the subject blobs (member 1 additionally as this
session's standing instructions). Staleness the byte-key cannot see: the unchanged members
were grepped for the deltas' vocabulary (`review-pending`, `freeze marker`, `deliverab`,
`review-full.json`, `utf-8`) — the only hit is README's Local-enforcement row, which
describes the same marker/hook consistently (and grounds low F-1 below).

## 3. What the deltas do, against the sources they claim to apply

**`5f029cd` → member 1 (three clause edits + two rider rows deleted).** Commit body declares
kind: amendment, declares all three edits design, and submits them to the same independent
FULL as the batch (`v3-review-full-5f029cd.md`, `REVIEWED_NO_BLOCKER`, record `02f24bb`) —
conduct conforms to `E10`'s design test. The seams were re-sampled at their sources:

- `E10` deferral precondition now reads "neither adds a clause to any rule nor changes what
  any rule requires (no rule-changing replacement or deletion)" — exactly the residue
  `v3-review-full-feacb86.md` L-2 names (the precondition's letter still passing a
  rule-changing deletion), nothing else.
- `E9` gains "— except an `E10` free-channel byte application, which is not a round and
  consumes nothing" — kills the phantom-VERIFY misread `v3-checkpoint-read-784e49b.md` L-1(a)
  names.
- `R10` routing now sends "a middle low whose record supplies the exact bytes or names the
  content" to the free channel, never the bank — L-1(b)'s misroute, closed.

Read against the whole checklist: the amended E9 branch is consistent with `E10`'s
pre-existing channel sentence ("applied immediately … reported after the fact and
reversible"; "that pair is not a round and spends no budget"); the amended precondition is
now the complement of `E10`'s design sentence; the amended R10 arm restates the channel's
own trigger. No verdict path, permission or budget rule conflicts anywhere in the layer.
Rows `L-2li` / `L-1lr` deleted in the same commit (`R10` redemption form); the bank at
`9541e1e` holds five rows (F-c, O-2b, SCC, RA, F-f3), neither deleted row present.

**`991b744` → member 4 (deliverables section).** Purely additive (29 lines). Stage marker
cites its two triage decisions by file name; both exist under `runs/p4-doc/issues/`. Its
factual claims re-derived: `runs/p4-doc/evidence/review-full.json` exists at the tip;
record-naming precedent `v3-review-full-fd0e2ed.md` exists; the marker path matches the live
marker this dispatch wrote; the committing-reviewer duty does not collide with construction-
side `R6` ("the execution side commits it") because REVIEW.md governs product runs only —
its own header and the checklist's header both draw that boundary. The Windows read-
discipline clause contradicts nothing in the layer (E3's "never describe it from memory" is
the execution-side analog, not a conflict).

**`f6c7a74` (closeout, after the FULL).** Applies the FULL's L-1 bytes to the run-v2
template comparator — diff matches the record's named content exactly (the four exhaustive
diff-header forms) — and correctly states the template is not a layer member, so no read is
owed for that application. Reliance check for `E10`: the application's outcome stands on the
channel sentence `E10` carried *before* the amendment plus the 2026-07-30 (a) ruling and
precedent (`d01615b` O-2's recorded reading); reverting `5f029cd` would not change it, so
nothing relied on the amended text before this read.

## 4. Assertions re-derived by command

| assertion in / about the changed bytes | command | result |
|---|---|---|
| `E2`: four frozen blobs | `git ls-tree 9541e1e -- contract/` + `git cat-file -t 8ad404b1` | holds — `b2dbdf75` / `68031fa2` / `e1a2f26b` in tree; `8ad404b1` is a blob |
| `E2`: pack = frozen 14 + later-born addition | `ls-tree -r 9541e1e -- <pack> | wc -l` → 15; `diff 11d147e 9541e1e -- <pack>` → exactly `paragraph-map.schema.json` | holds |
| member set == `layer_path_check.LAYER` mirror | script `LAYER` read (:30–41) | holds — nine paths, exactly this table (Phase D's L-1 line applied at `ace0845`) |
| `5f029cd` = 3 clause hunks + 2 row deletions, nothing else | full diff read | holds |
| `991b744` REVIEW.md hunk purely additive | full diff read (29 insertions, 0 deletions in the member) | holds |
| FULL→tip commits touch no member | `git show --stat` `02f24bb` `f6c7a74` `9541e1e` + per-member log | holds |
| REVIEW.md section: ReviewResult path / record naming / marker path | file existence + live marker | holds (enforcement wording: low F-1) |
| rider rows deleted == rider sources' seams | `feacb86` L-2 and `784e49b` L-1 blocks re-read | holds — letter for letter |

No assertion in the layer was found false at this commit.

## 5. Ledger bindings, checked

- **O-5** (`v3-review-full-5f029cd.md` O-5; `f6c7a74` body; ledger pointer) — discharged:
  both amended members read in full at the final bytes (§3). The window audit (§1, §3)
  confirms the deferral-free path the rule demands: no round and no product run relied on
  the amended clauses between `5f029cd` and this read; P5A has not opened.
- **L-3** (the round opened without a written cold-read citation; wording-level, rides the
  next batch) — not this read's to redeem; it is opening conduct for the *next* round. This
  record is the fresh coverage that round can cite, which is the ride's substance.
- **L-1 of the FULL** — verified applied at `f6c7a74` with the record's exact bytes (§3);
  the CLOSED p4-doc lineage copy untouched, as the record required.
- **L-2 / L-4 of the FULL** — L-2 recorded-only (immutable commit); L-4 closed inside the
  FULL by its own probes. Nothing outstanding from either.
- Round budget state as this read finds it: the maintenance round's FULL spent
  (`02f24bb`, `REVIEWED_NO_BLOCKER`); fix leg unspent; `f6c7a74`'s byte application obliged
  no VERIFY under the (now-written) E9 exception. This read spends nothing (`R3`).
- Riders: five rows, none due on a read (a read touches no surface).

## 6. Findings

### Low (wording-level — `R9`: rides the next batch touching this layer; no round, no read)

**F-1 — REVIEW.md states the freeze as a mechanism; the layer's own enforcement row brands
it advisory.** The new section's closing sentence — "the pre-commit guard holds the
repository frozen until the returned record removes it" — reads as a harness guarantee.
README's Local-enforcement row (member 2, unchanged) states the ground truth: the hook is
per-machine, absent on a fresh clone, bypassable with `--no-verify`, "Advisory automation
only — the instruction layer's instrument is the independent read." Under the section's own
zero-restatement premise the product-run reviewer learns duties from REVIEW.md alone, so the
downstream slip is a reviewer treating the freeze as mechanically enforced instead of
re-deriving the window (`R2`) — a trust misplacement, not a changed duty: no check outcome,
obligation, permission or verdict path moves, and the accurate fact is recoverable from the
adjacent member. Content for the ride: qualify the sentence with the hook's advisory,
per-machine status (or point it at README's Local-enforcement row).

### Observations (`R5` — reported; conclusions are the user's)

**O-1 — the open tail's scope question is now live, and this read classifies rather than
assumes.** This window amended `description` strings in `ResearchSystem/schema/
object.schema.json` and `persisted-index.schema.json` (Stage 3, `7bf705b`/`05ddf45`). They
are **not** enumerated here: `E10`'s tail takes prose successors *to text this harness
governs*, and those schemas are the ResearchSystem product's instruments — governed by the
ResearchSystem Contract and A1, changed under Stage 3's own independent code review; the
harness's schema surface is the `document-assurance-v3` pack. But the `d01615b` precedent's
sweep command (`git diff -- ResearchSystem/schema/`) is wider than that classification, and
this is the first window where the difference returns paths. Applied mechanically, the wide
scope would have swept product schemas into the layer — and thereby made Stage 3 retroactively
non-conformant (reliance before read), a consequence arguing the narrow reading matches how
the harness has actually operated. The next reader inherits this classification as a checked
fact; pinning it into `E10`'s sentence would be design and is the user's call.

**O-2 — the byte-channel seam's third exercise, first with the letters aligned.**
`f6c7a74` is a post-FULL byte application obliging no VERIFY — the configuration `L-1lr`
recorded as misreadable. It navigated by the channel + ruling + precedent (as the two prior
exercises did) and, because `5f029cd` landed in the same round, the letters (`E9`'s
exception, `R10`'s bytes arm) now carry what practice carried. Seam closed; rider correctly
deleted; no reliance-before-read occurred on the way (§3).

**O-3 — REVIEW.md's product-run reviewer now commits its own record; the construction-side
record channel is unchanged.** The new section assigns commit-and-marker-deletion to the
product-run reviewer, while `R6` keeps construction-side records committed by the execution
side. The two regimes are cleanly bounded by the files' own headers, and this read conformed
to `R6` (record written to the worktree; the committing act is the execution side's). Noted
so the asymmetry is inherited as intentional, not drift — the FULL's O-2 (the hook
docstring's "deleted by the executor") already rides the next hook touch.

## 7. Coverage disclosure (`R4`)

**Read in full:** members 1 (161 lines, also as standing instructions) and 4 (256) at the
subject blobs; the complete diffs and bodies of `991b744`, `5f029cd`, `f6c7a74`;
`v3-review-full-5f029cd.md` (178); `v3-checkpoint-read-d01615b.md` (285); the review-contract
stub (standing-instruction entry); `HARNESS-LEDGER.md` and `HARNESS-RIDERS.md` at `9541e1e`.

**Sampled:** `v3-review-full-feacb86.md` — the L-2 block; `v3-checkpoint-read-784e49b.md` —
the L-1 block; `layer_path_check.py` :1–60 (docstring + `LAYER`); `57dbaa0`'s README diff
and commit body; `02f24bb` / `9541e1e` stats; the window's `--name-status` path list,
classified by hand.

**Probed only:** `.harness/review-pending.json`; `8ad404b1` object type; pack `ls-tree`
count; existence of `runs/p4-doc/evidence/review-full.json`, the two triage decision files,
and `v3-review-full-fd0e2ed.md` (by name, from the committed tree listing).

**Not verified:** that this read ran in a fresh context — a process claim, marked. The user
rulings beyond their in-repo records (`R7` — ceiling stated, not a block). The suites the
round's commits report green (pytest 556 / compile --check) — not re-run: no code this read
enumerates as layer changed, and the FULL re-ran them at the candidate; their binding force
is that round's property. The fixture runner — not re-run: README is blob-unchanged and its
41/41 claim was verified at its recorded read on this machine.

**Ceiling:** whether the open tail's scope should be pinned, whether the freeze wording
should be qualified, and every consolidation choice remain the user's questions under `R5`;
what is checked here is that the layer's text matches the repository, that the amendments
are exactly the fixes their sources named, and that the bookkeeping around them did what its
own rules say.
