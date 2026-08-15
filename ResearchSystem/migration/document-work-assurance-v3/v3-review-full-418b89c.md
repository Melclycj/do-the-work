# V3 review — FULL — subject `418b89c`

**Subject range** `8e018e19..418b89c2` — 4 commits, of which **3 are this round's** (`6fcdc68`
R0.1 journal, `c55953f` `HD-24`, `418b89c` the R1 amendment) and one (`8ee2213`) belongs to the
product route (§5.2).

**Verdict: `REVIEWED_NO_BLOCKER`** — 0 blockers, 3 low findings, 5 observations.

This round is a move, and a move is reviewable to a standard almost nothing else is: I can
reconstruct both files from their parts and assert byte equality. I did. The claim is exactly
true — the six sections arrive in `EXECUTION.md` byte-for-byte except eight replacements at
seven sites, and those eight are precisely the eight the commit body discloses, no more and no
fewer. Nothing else in either file changed. The two guards the commit says intercepted the work
do bind: fed the unfixed bytes, they fire, and between them they cover six of the seven sites.
The three lows are all the same shape — text elsewhere that this move made stale and the round
did not sweep for — and none of them changes a check outcome, which is why none is a blocker.
The observation that matters most is not a defect at all (§4, `O-1`): the move put a known,
already-banked correction behind an `E10` round that it was free to make yesterday.

---

## 1. What this round is, re-derived

Not taken from the dispatch, which carried the range and nothing else (`R2`).

| Question | Answer | Where I read it |
|---|---|---|
| Round | **Batch A / A2 · R1** — `HD-14`: move the six rule sections out of `assurance/templates/run-v2/README.md` into `EXECUTION.md` | `.goals/plans/harness-a2-construction.plan.md` §Steps R1; `418b89c` body |
| Governing instructions | `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` (E1–E12 / R1–R10); the `v3-harness-review-contract.md` I was pointed at is a stub naming it as its own counterpart | review-contract stub `:3`; checklist header `:9-12` |
| Budget position (`E9`) | This **is** the FULL. No file under `migration/document-work-assurance-v3/` names `418b89c`, `c55953f` or `6fcdc68`; no prior independent FULL has occurred. One user-approved fix + one targeted VERIFY remain | `ls` + grep of the record directory (107 entries before this one); `git log` |
| Verdict domain | FULL → `REVIEWED_NO_BLOCKER \| CHANGES_REQUIRED \| SPEC_GAP` (`R3`) | checklist `R3` |
| Authorization | `HD-14` carries `· user ·` and 2026-08-08 and is `live` awaiting A2's T7; `HD-24` (this range) carries `· user ·` 2026-08-09. Preview-card approval and the reader-scope answer are asserted in `418b89c`'s body; I see the record, not the approval (`R7`) | `HARNESS-DECISIONS.md` §live; `418b89c` body |
| Obligations | Move six named sections; leave the README holding instantiation only; answer the reader-scope question in the round's own preview; revert unit = the single commit; `LAYER` unchanged because no member is added; opening `E10` cold read owed | plan §R1; `HD-14` 后果 |
| Ledger state | Batch A row records A2 open, R0.1 paid, `HD-24` landed, "下一步 = R1（`HD-14` 搬六节，开轮）" | `HARNESS-LEDGER.md:91-96` |

**Ceiling (`R7`).** `HD-14`, `HD-24` and the preview-card approval (including the reader-scope
answer that decided this round's scope did not shrink) were issued in chat. I see their
committed records and take them at face value. "Fresh context" is marked, not verified (`R4`).

**Read coverage (`R4`).**

- *Read in full:* `CONSTRUCTION-CHECKLIST.md`; `HARNESS-DECISIONS.md` (§live and §implemented)
  and its archive; both versions of `assurance/templates/run-v2/README.md`; both versions of
  `document-harness/EXECUTION.md`; `document-harness/README.md`; `HARNESS-LEDGER.md`;
  `HARNESS-RIDERS.md` (all 18 rows); `journal/batch-a2-2026-08-09.md`;
  `.goals/plans/harness-a2-construction.plan.md`; `hooks/layer_path_check.py`;
  `hooks/candidate_path_check.py`; `rsclib/document_harness/paths.py` (module docstring +
  token logic); `tests/document_harness/test_readme_enumeration.py`;
  `v3-checkpoint-read-bd77fd4.md` §1; all four commit bodies.
- *Ran myself, output pasted below:* the two-file reconstruction; the moved-block diff; the
  path-token census over `EXECUTION.md`; the negative control on both guards; the tracked-suffix
  ambiguity counts; pytest (632); `tests/harness/run_tests.py` (39); `rsc compile --check`;
  `repo-audit.py`; the seven-tree file/line re-derivation; the nine-member blob diff; the layer
  member size table; the `E2` blob ids.
- *Probed only:* `8ee2213`'s two plan files (classified, not reviewed — §5.2); the closed-run
  and `migration/` records that cite the old README by line number (counted, not swept).

---

## 2. The implementation (`R3` — this first)

### 2.1 The move is exactly what it claims, and nothing else moved

I reconstructed both files from their parts rather than reading the diff, because a diff can be
read to agree with a story and a reconstruction cannot.

```
README head 1-45 identical : True
README tail 269-290 identical: True
README inserted block (lines 46-50 of new):
   | > **The rule sections moved (R1, `HD-14`, 2026-08-09).** The six rule sections this README
   | > carried — *Pre-freeze gate* · *Instruction form* · *Authoring gate* · *Audit cadence —
   | > pre-START rounds* · *Regression-battery tiering* · *Instruction authoring rules* — are
   | > instruction-layer text now: read them in `ResearchSystem/document-harness/EXECUTION.md`.
   | > This file holds template instantiation only.

EXEC old body 13..165 == new 14..166 ?  True
EXEC tail: old[165:171] == new[398:404] ?  True
```

So the README is `old[1:45]` + a 5-line pointer + `old[269:290]`, and `EXECUTION.md` is `old[1]`
+ a rewritten 4-line reader sentence + `old[13:165]` unchanged + an 8-line stage marker + the
224-line moved block + `old[166:171]` unchanged. There is no third edit hiding anywhere in
either file. Line counts reproduce the commit's figures exactly: README 290 → 72,
`EXECUTION.md` 171 → 404.

### 2.2 Eight replacements at seven sites — the disclosure is exact

`git diff` of README `46-268` against `EXECUTION.md` `175-398` returns 17 changed lines: 8
replacement pairs and one added trailing blank (the separator before the closing section).

```
< (`../../runs/p5a-shells/control/audit-rounds.md`).
> (`ResearchSystem/assurance/runs/p5a-shells/control/audit-rounds.md`).
<    `tooling/tests/` to four named paths, ...
>    `ResearchSystem/tooling/tests/` to four named paths, ...
<   *by reference* — the rule this README already carries under *Instruction authoring
>   *by reference* — the rule this file already carries under *Instruction authoring
<   `control/paragraph-map.json` with `make_paragraph_map.py` ...
>   `ResearchSystem/assurance/runs/<run-id>/control/paragraph-map.json` with `make_paragraph_map.py` ...
<   (`document-harness/README.md` under `test_readme_enumeration.py`; the layer-path
<   mirror, `tooling/hooks/layer_path_check.py`) is tooling-load-bearing — treat the
>   (`ResearchSystem/document-harness/README.md` under `test_readme_enumeration.py`; the layer-path
>   mirror, `ResearchSystem/tooling/hooks/layer_path_check.py`) is tooling-load-bearing — treat the
< `../../../document-harness/journal/retro-2026-08-03.md` §3): the battery is **~85% of an
> `ResearchSystem/document-harness/journal/retro-2026-08-03.md` §3): the battery is **~85% of an
<   6 f1 (`../../runs/p5a-shells/control/audit-rounds.md`).
>   6 f1 (`ResearchSystem/assurance/runs/p5a-shells/control/audit-rounds.md`).
```

Eight replacements, seven numbered sites, the audit-rounds path twice — item for item what the
commit body discloses. Both original relative paths resolve correctly from the README's own
directory and would have resolved nowhere from `EXECUTION.md`'s, so the re-anchoring is a
repair, not a rewrite. All six re-anchored targets exist in the index; the seventh
(`<run-id>` placeholder) is deliberately unresolvable and is not path-shaped to either guard.

### 2.3 The defect class, not the reported instance (`E7`)

I enumerated every backtick path-shaped token in the whole of the new `EXECUTION.md` and
resolved each three ways. One token in the moved block resolves nowhere:
`runs/p4-doc/issues/user-decision-triage-comparator-environment-defects.json` (line 391). It
was already unresolvable from the README's directory before the move, so the move did not break
it, and `candidate_path_check` passes it as SHORTHAND because exactly one tracked file ends with
that suffix (verified: 1 match). Every other token resolves from the repo root. No path was
left behind.

For the class the guards cannot see — self-reference — I swept the moved block for
`this README | this file | this template | this section | above | below`. Every remaining
internal cross-reference ("the three artifacts above", "see *Instruction form* above", "the
rules below", "The three rounds below") still resolves, because the block moved as a unit with
its order preserved. The one sentence that stopped being true, `the rule this README already
carries`, is site (7) and was caught.

### 2.4 The guards bind — negative control on the unfixed bytes

`E4`/`R8`: I did not take "两 hook 离线复跑 exit 0" on trust in either direction. Feeding the
**unfixed** README block to both guards as if it were added to `EXECUTION.md`:

```
=== NEGATIVE CONTROL: unfixed bytes scanned as EXECUTION.md ===
layer_path_check fires on:
   `tooling/tests/` - resolves only under ResearchSystem/ — prefix missing
   `document-harness/README.md` - resolves only under ResearchSystem/ — prefix missing
   `tooling/hooks/layer_path_check.py` - resolves only under ResearchSystem/ — prefix missing
candidate_path_check fires on:
   `../../runs/p5a-shells/control/audit-rounds.md`
   `control/paragraph-map.json`
   `../../../document-harness/journal/retro-2026-08-03.md`
```

and the same two guards on the **actual** added lines of `418b89c`:

```
--- ResearchSystem/document-harness/EXECUTION.md  (235 added lines)
   layer_path_check : clean
   candidate_path   : clean
--- ResearchSystem/assurance/templates/run-v2/README.md  (5 added lines)
   layer_path_check : clean
   candidate_path   : clean
```

Red on the defect, green on the repair, in both guards. The ambiguity ruling behind site (6)
also reproduces: five tracked files end in `control/paragraph-map.json`
(`p4-bridge`, `p4-doc`, `p5a-firewall`, `p5a-shells`, `p5b-firewall`), so the token is
genuinely non-unique and the block is the designed behaviour, not an accident.

This is wider than the commit's account, which attributes only site (5) to `layer_path_check`
and only site (6) to `candidate_path_check`. Between them the guards cover six of the seven
sites; the account is consistent with sites (1)–(4) having been fixed by hand before the first
commit attempt, but the mechanical floor is higher than the narrative suggests. Recorded as
`O-3`, not as a correction — nothing in the commit body is false.

### 2.5 Battery

The commit classifies the change set as doc-only. Both changed paths are prose outside the
schema, tooling and generated trees, so the classification follows the rule as written, and it
follows a recorded precedent directly on point: `22b27aa` also touched an instruction-layer
member (`CONSTRUCTION-CHECKLIST.md`) and the ledger's `L3` correction ruled it doc-only on the
ground that the tiering criterion is "路径类型 + 树位置、无指令层项". No test reads
`EXECUTION.md`'s bytes — `test_precommit_checks.py:192` uses only its path, in the `LAYER`
mirror assertion — so the tooling-load-bearing exception does not reach it.

I ran the full battery anyway, because a classification that is right for the wrong reason and a
classification that is right look identical from the commit body:

```
632 passed in 110.71s                              (pytest, ResearchSystem/tooling/tests/)
Ran 39 tests in 3.643s / OK                        (tests/harness/run_tests.py, the v2 suite)
RESULT: generated output fresh; lint clean (exit 0) (rsc compile --check; 161 md, 173 objects)
RESULT: clean (exit 0)                             (Thesis/Work/Tooling/repo-audit.py)
```

Green. Skipping it cost nothing on this batch.

---

## 3. Findings

All three are the same shape: text outside the two changed files that this move made stale, and
which the round did not sweep for. None changes a check outcome, an evidence binding, a
permission, an obligation or a verdict path, which is why none is a blocker (`R3` — a
non-blocking finding is never inflated).

### `L-1` — three live-code citations now point at a file that no longer carries the rule

**Location.** `ResearchSystem/tooling/rsclib/document_harness/instruction.py:15` and `:382`;
`ResearchSystem/tooling/tests/document_harness/test_transcript_audit.py:83`.

**Ground truth.** All three cite "the run-v2 README" as the home of a rule that is now in
`EXECUTION.md`:

- `:15` — "What it costs is stated at `transcript_audit` and in the run-v2 README: coverage is
  established, faithful restatement is not."
- `:382` — "The disclosure belongs in the audit record's `audited_by` and in the run-v2 README".
- `test_transcript_audit.py:83` — "that is the shape the run-v2 README prescribes, not a defect."

The `audited_by` prescription and the faithful-restatement ceiling are moved-block lines
103–109; the standing context-unit shape is in the moved *Instruction form* section. The new
README carries none of them — I grepped it for `audited_by`, `faithful restatement` and
`coverage is established`: zero hits.

**Why it is not a blocker.** The README's new blockquote names all six sections and the target
file, so the chain still resolves in one extra hop, and no check reads any of these strings.

**Minimum fix.** Three tokens, `run-v2 README` → `EXECUTION.md`. Note the second-order cost
before choosing: these are `tooling/` paths, so applying the fix makes that batch
tooling-touching under the very rule this round moved.

**If banked.** what: three stale "run-v2 README" citations in live code · redeem-when: next
batch touching `rsclib/document_harness/instruction.py` or `test_transcript_audit.py` ·
deadline: the first instruction authored after this commit whose author follows `:382` to find
where the `audited_by` disclosure belongs.

### `L-2` — `EXECUTION.md` now disclaims the construction side and binds it in the same file

**Location.** `EXECUTION.md:10-12` (pre-existing) against `:313-314` (arrived this round).

**Ground truth.** The header says: *"This file describes a role inside a product run. It is not
the construction-side contract for building the harness itself — that lives at
`CONSTRUCTION-CHECKLIST.md`."* The imported *Regression-battery tiering* section opens:
*"Which verification a pass owes is tiered by the change surface — for a product run's evidence
pass **and for a construction batch's pre-commit verification alike**."* The file denies
construction-side authority on line 10 and exercises it on line 313. This round created the
contradiction: the rule previously lived in a template README that claimed no authority over
anything.

**Why it is not a blocker.** Discoverability actually improved — `E10` obliges every
construction round to cold-read all nine members at opening, so a construction session now
meets this rule every round, where before it had to know to open a template README. What is
left is a false sentence, not a lost rule. This round's own executor classified its tier from
the moved text correctly.

**Minimum fix.** Qualify the disclaimer (or the tiering section's scope line) so the file stops
denying what it does. Flagged with the fix: qualifying it adds a bound to what a rule requires,
so under `E10` it is design and opens a round — which is itself part of what the user should
weigh, and is the same trap as `O-1`.

**If banked.** what: header disclaims construction-side authority the tiering section exercises
· redeem-when: next batch touching `EXECUTION.md`'s header or the tiering section · deadline:
the next **doc-only** construction batch that classifies its own tier from this text.

### `L-3` — the layer's own navigation surface now under-describes `EXECUTION.md`

**Location.** `ResearchSystem/document-harness/README.md:26`.

**Ground truth.** The Role-instructions row reads "EXECUTION.md — what the executor owns and may
never author, plus the WorkSpec-author discipline". As of this commit it also holds the entire
run-template rule set: pre-freeze duties, instruction form, the authoring gate, audit cadence
and battery tiering. The commit body presents "`document-harness/README.md`（被
`test_readme_enumeration` 钉的那个）未碰" as a virtue; the untouched line is the layer's
navigation table, and a run author routed by that description has no reason to open the file
that now holds four sections addressed to them.

**Why it is not a blocker.** The run-v2 README's redirect is the path a run author actually
walks (they are instantiating the template), and `EXECUTION.md`'s own header now states the
multi-reader fact on first read.

**Minimum fix.** Extend that one cell to name the run-template rule set. `document-harness/README.md`
is an `E10` member but not an `E2` frozen path, and naming what a file contains adds no clause
to any rule — so this is free-channel eligible if the executor supplies the bytes.

**If banked.** what: Role-instructions row under-describes `EXECUTION.md` after `HD-14` ·
redeem-when: next batch touching `document-harness/README.md` · deadline: the next end-to-end
layer read that navigates by that table.

---

## 4. Observations

**`O-1` — the move put an already-banked correction behind a round, and the commit does not say
so.** Before this commit, `run-v2/README.md` was outside the instruction layer; the
digest-narrowing plan records that explicitly ("模板 README **不是 instruction layer**…可以同轮
改"). After it, every correction to these six sections is an `E10` amendment, and one that
changes what a rule requires is design and opens a round. Two corrections are already known and
now cost that:

1. This round's own R0.1 journal §2③/§4(c) records that the full-battery enumeration —
   "P2/P4/P5A goldens, schema fixtures, pytest, `compile --check`" — **does not name the two
   suites that actually run** (the 39-test `tests/harness/run_tests.py` and the 20-test
   `tests/stage_control`), and routed the fix to "`HD-14`（R1 搬六节时同一文件）或拆分批".
   R1 chose byte-verbatim and did not take it. The gap is still there at `EXECUTION.md:322-323`
   — I read it — and closing it now adds items to an enumeration, which is design.
2. The *Revert anchor* is a **user condition, part of the 2026-08-03 ruling**: "removing this
   whole section restores the prior rule (full battery on every pass); nothing else depends on
   it." Deleting a section from a layer member changes what a rule requires, so exercising the
   user's own revert condition is now a round.

Neither cost is disclosed in `418b89c`'s body, and both are consequences of `HD-14` — the user's
ruling — not of how the round executed it. Whether that price is acceptable is the user's
question, not mine (`R5`). I report the shape.

**`O-2` — one commit in the subject range belongs to another track.** `8ee2213`
("docs(research-system): plan Decision and DR migration") changes only
`.goals/plans/research-system-p5c-p8-revision.plan.md` and
`.goals/plans/research-system-p9-architecture.draft.md`. I verified it touches no
`ResearchSystem/` path and mentions no layer member (`git show | grep -c` for `EXECUTION.md`,
`CONSTRUCTION-CHECKLIST`, `HARNESS-DECISIONS` → 0), so it cannot contaminate the harness work.
I did **not** review its substance: the product route's gates are `.goals/LEDGER.md`'s, not this
ledger's, and reviewing it here would be me setting the question. Ceiling stated (`R4`).
`c55953f`'s body does disclose the commit's origin ("另一 session 的 p5c plan 脏文件已收").

**`O-3` — the guards' binding force is wider than the commit's account.** See §2.4. The
account attributes one site each to the two hooks; the negative control shows
`layer_path_check` catching all three missing-prefix sites and `candidate_path_check` catching
all three of the remaining path sites, including both relative paths the body presents as
hand-reasoned. Site (7), the `this README` self-reference, is caught by neither and never could
be — that class rests entirely on human reading, and on this round the reading was complete.

**`O-4` — the new stage marker's nested emphasis.** The R1 marker (`:167-173`) wraps the whole
block in `*…*` and then italicises each section name inside it; the file's existing W1 marker
(`:110-112`) uses `**bold**` inside the italic block for exactly this reason. Nested `<em>` is
visually inert, so the six section names lose the distinction the marker is using them for.
Cosmetic; noted because the fix is one character class and the convention already exists in the
file.

**`O-5` — size.** `HD-14` predicted `EXECUTION.md` at "约 350 行"; it landed at 404, which the
commit body discloses. At 404 lines it is the layer's largest member by 1.4× over `REVIEW.md`
(284) and 2.2× over `CONSTRUCTION-CHECKLIST.md` (182). Every `E10` cold read now pays that.
Reported as shape, per `R5`; the conclusion is the user's.

---

## 5. Boundary and record conformance (run second, `R3`)

### 5.1 The permanent boundaries

| Check | Result | How |
|---|---|---|
| `E2` freeze surface untouched | **clean** | contract `b2dbdf75`, supersession-1 `68031fa2`, supersession-2 `e1a2f26b` all equal `E2`'s literal ids at the tip; the schema pack is 15 files, `paragraph-map.schema.json` `09aa8699` unchanged |
| `E10` member set unchanged | **clean** | `layer_path_check.LAYER` is untouched in the range; `CONSTRUCTION-CHECKLIST.md` is untouched; no member added, so rider `E10-sync` correctly does not fire |
| Opening cold read citable | **valid** | `git diff bd77fd4 c55953f` over all nine members returns empty, and `v3-checkpoint-read-bd77fd4.md` §1 states a blob id per member — `E10`'s citation precondition is met |
| `E8` change boundary | **clean** | `418b89c` touches exactly the two files the plan names as R1's revert unit; explicit paths, new commit, no push, kind named ("指令层 amendment") |
| `E9` freeze window | **clean** | tip `418b89c` at `02:10:15Z`, marker `dispatched_at 02:11:22Z`; the branch has taken no commit since — this record is the first it admits |
| Ledger cap | **clean** | `HARNESS-LEDGER.md` at 120 lines, cap 120 |
| `HD-2` state machine | **clean** | `HD-17` leaves §live and enters the archive with `status: retired` and a consumption reason **in the same commit** as `HD-24`'s creation; basis preserved; §live keeps one entry per topic |
| Rider bank (`R10`) | **nothing owed** | I walked all 18 rows: no touch trigger names `EXECUTION.md`, `run-v2/README.md`, or any file in the range. `E10-sync`, `R10-route` and `waiver-live` all key on `CONSTRUCTION-CHECKLIST.md` text that this round did not touch |

### 5.2 What I verified in the two non-R1 harness commits

`6fcdc68` (R0.1 journal) carries the round's load-bearing measurements, so I re-derived its
central table rather than reading it:

```
tree                                              files    lines
ResearchSystem/harness/                              14      580
ResearchSystem/tooling/rsclib/harness/               11     1421
ResearchSystem/tooling/tests/harness/                 1      754
ResearchSystem/schema/harness-v2/                    81     3607
ResearchSystem/migration/general-harness-v2/         26     3192
ResearchSystem/migration/stage-control-refactor/      2      217
ResearchSystem/stages/                                2      365
SEVEN-TREE TOTAL                                    137    10136
+ tooling/rsc.py                                      1      856
= GRAND TOTAL                                       138    10992
```

Every cell reproduces exactly, including the 81-file recursive count that corrects A1 §13.5's
top-level 15, and the closure against A1 §13.3's `AMBIG 138 files / 10,992 lines` is exact — the
journal's central claim holds. The `stages/` link count also reproduces: four true markdown
links pin it, one of them in the signed `Stage-Control-Contract.md:23`, so "直接删" is indeed
not available. The §5 honesty boundaries are properly stated (git records writes not reads; the
fourth classification is disclosed as the auditor's own invention; the 32-file v1 grouping is
disclosed as a human judgement A1's lost sub-table cannot confirm).

`c55953f` records `HD-24` and retires `HD-17`. Its content is a user ruling, its
`basis` points at the journal sections that carry the measurements, and it changes no rule text.
Under the 2026-08-03 ledger ruling ("ledger 删减/记账批不开轮，user ruling 即 gate") it opens no
round of its own and consumes no budget; it rides this FULL's subject.

### 5.3 Where the pointers stand

Both `.goals/plans/harness-a2-construction.plan.md` (step 3 unticked, resume pointer still
"Next executable work is **R1**") and `HARNESS-LEDGER.md:94` ("下一步 = R1") describe R1 as not
yet started, while its candidate has landed. This is not a defect: `E9`'s freeze window forbids
the branch taking any commit but this record between dispatch and its landing, so the executor
could not have updated them. Closeout is where they move. Noted so the next cold start does not
read a stale pointer as an instruction to redo R1.

---

## 6. What this review does not establish (`R4`)

- **`UNVERIFIABLE`: the chat-side authorizations.** `HD-14`'s ruling, `HD-24`'s item-by-item
  confirmation, the preview card and the reader-scope answer that kept this round's scope from
  shrinking all exist to me only as committed assertions. I did not verify any conversation.
- **`UNVERIFIABLE`: the fresh-context claim.** Marked, not verified.
- **Not swept: line-number citations into the old README from closed records.** At least
  `v3-review-verify-c7fb720.md:322` ("`run-v2/README.md:138-160` for the `audited_by`
  prescription") now points into moved text. Records are immutable and cite as-of-then, so I
  counted this class rather than enumerating it, and raise no finding on it.
- **Mutation proves binding force, not sufficiency.** §2.4 shows both path guards fire on the
  real defect shape. It does not show they would catch a path token that resolves but names the
  wrong file — `paths.py`'s own docstring already declares that ceiling — nor anything about the
  self-reference class, which has no guard at all.
- **Not re-litigated: whether the six sections should have moved.** `HD-14` is the user's
  ruling; my subject is the text that is there (`R5`).

---

**Verdict: `REVIEWED_NO_BLOCKER`** — 0 blockers, 3 low findings (`L-1`, `L-2`, `L-3`), 5
observations (`O-1`…`O-5`).

Per `R10`, lows are not banked by default on a `REVIEWED_NO_BLOCKER` FULL: before closeout the
executor weighs each low's deadline against its touch trigger and puts the spend-the-fix-leg /
bank choice to the user. My reading of the three, offered as input and not as the decision:
`L-1` is the only one whose fix is unambiguously free of `E10` machinery and it is also the one
most likely to mislead a real reader, so it is the natural candidate for the fix leg; `L-3` is
free-channel eligible if bytes are supplied; `L-2` cannot be fixed without opening a round, so
banking it and letting it ride the batch that answers `O-1` is the cheaper shape.
