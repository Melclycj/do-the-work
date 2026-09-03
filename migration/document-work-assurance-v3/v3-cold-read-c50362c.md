# Instruction-layer read — subject `c50362cce992a1ee24329e90da5399e8f1da30a8`

An `E10` read of the harness's own instruction layer. **Not a round** (`R3`): no budget spent, no
verdict carried; the output is findings tiered must-fix / low / observation. Dispatched with the
charter this repository declares under `rules` in the `harness.json` at its root —
`document-harness/CONSTRUCTION-CHECKLIST.md` — read in full, and then the counterpart that file
names, `document-harness/RULES.md`, also in full. `HARNESS-DECISIONS.md`'s `§live` was read in
full at this repository's root, as `E10`'s last clause requires of the opening.

Record name: `v3-cold-read-`. `R6` offers two read filenames and the layer defines no criterion
for choosing between them (rider `read-name-split`, open, re-derived here and not re-banked). I
took `cold-read` for the reason every previous whole-layer opening record took it.

**Findings: 0 must-fix, 2 low, 2 observation.**

---

## 1. The member set and the coverage, both derived

The dispatch enumerated no members (`R2`). `E10`'s own sentence at the subject
(`document-harness/RULES.md:86-94`) reads **exactly seven paths**. Blob ids from
`git ls-tree -r c50362cce992a1ee24329e90da5399e8f1da30a8`, run here:

| # | member | blob at `c50362c` | last recorded end-to-end read | this read |
|---|---|---|---|---|
| 1 | `document-harness/RULES.md` | `f4d5698d6c84dfd793796a765c7b4c5af2115ce4` | `v3-cold-read-51bd4f6.md`, blob `c47dbc5f…` — **changed** (`1c18e4a`, the free-channel application below) | **end to end** |
| 2 | `document-harness/README.md` | `1ddb7e044d3ae38b211aee1f953f223fb4bfe5fb` | `v3-cold-read-51bd4f6.md`, blob `7decb095…` — **changed** (`38038ec`, the `E10` amendment below) | **end to end** |
| 3 | `document-harness/EXECUTION.md` | `08fa87f8380b60a0af4e125e1bfe88747d26f0e4` | `v3-cold-read-51bd4f6.md`, **same blob** | **end to end** |
| 4 | `document-harness/REVIEW.md` | `71707a3a01016e86b63238d494df98abbd2408c3` | `v3-cold-read-51bd4f6.md`, **same blob** | **end to end** |
| 5 | `document-harness/ORCHESTRATION.md` | `3f9cd61ca42c94ca2a3080d13412741173bd73b4` | `v3-cold-read-51bd4f6.md`, **same blob** | **end to end** |
| 6 | `contract/Document-Work-Assurance-Contract-v4.md` | `de210772994ee49bf8fa7d7a68510ca49e290a88` | `v3-cold-read-51bd4f6.md`, **same blob** | **end to end** |
| 7 | `schema/document-assurance-v3/paragraph-map.schema.json` | `09aa869962f592c2f86c9379be0ef3eb7d2232ff` | `v3-cold-read-51bd4f6.md`, **same blob** | **end to end** |

Plus, not a member, read for the reason `E10`'s second sentence gives:

| — | this repository's declared rule | blob at `c50362c` | this read |
|---|---|---|---|
| — | `document-harness/CONSTRUCTION-CHECKLIST.md` | `97ed956be92864dda125cb2ac8970b1375bcc8bc` | **end to end** |

Nothing was taken by citation: every member was read end to end at these bytes. The worktree is
clean apart from an untracked `.goals/` (`git status --porcelain` → `?? .goals/`), so the bytes
read and the bytes at the subject are the same objects — `git hash-object` on the eight paths
returns the eight blob ids above, and on `harness.json` returns `8320c2c4…`.

`harness.json` at this repository's root reads
`{"policy": "CONSTRUCTION-LEDGER.md", "rules": ["document-harness/CONSTRUCTION-CHECKLIST.md"]}`,
which is why the eighth row is here and why `CONSTRUCTION-CHECKLIST.md` is not among the seven.

Only two member blobs moved since the last recorded read, and both moves are the two deferrals
this read was told to carry — §3 below.

## 2. What was run

- **Path-token resolution over the whole standing text**, not only added lines — the class
  `E10`'s clause says the guard never re-scans. `unresolved_tokens` and `LAYER` imported from
  `tooling/hooks/layer_path_check.py`, applied to each scanned path's bytes at the subject:
  `0 unresolved` for all eight files. `LAYER` is the same seven paths in the same order as
  `E10`'s sentence.
- **Markdown links**, which carry no backtick token for the guard to find: 38 relative link
  targets over the eight files, every one resolving from the file's own directory inside this
  repository (37 at the previous read; the `38038ec` amendment added the thirty-eighth).
- **`python tooling/sweep_refs.py`** from the repository root:
  `-- 13 caller-held or unresolvable references over 8 members and declared rule files`, all 13
  NAMETOK (bare filenames), the same 13 sites as at `51bd4f6`. Each was re-read for the holder
  `E10` requires; all 13 have one. Eleven carry it in their own clause (`in the caller that grew
  this harness`, `the run's`, `scripts live in the caller's tree`, `the control root lives in the
  caller`, and for `review.schema.json` a blob id in this repository's history); two —
  `build_run.py` at `EXECUTION.md:196` and `check_shells.py` at `:201` — take theirs from the
  paragraph's governing sentence at `:187-188` (*p5a-shells' pre-START history … held with its
  run in the caller that grew this harness, not in this repository*), which is a weaker carrier
  than the other eleven but a carrier.
- **The battery leg `EXECUTION.md` names for this repository**: `python -m pytest -q` run from
  `tooling` → `938 passed in 189.43s (0:03:09)`, exit 0, at this subject with the worktree clean.
- **Contract §5's closed enums against the schema pack** — the audit behind `L-2`. Row by row:
  WorkState status (`assuranceStatus`), Audit result (`auditResult`), Decision phases
  (`decisionPhase`), LocalCheckSpec kinds (`checkKind`) and Verification mode
  (`verificationMode`) are `$defs` of `common.schema.json`; the two verdict rows are inline in
  `review.v2.schema.json:32,68`; the four decision-value rows are inline in
  `user-decision.schema.json:22-37` and its four phase branches at `:55,64,73,83`, and the
  FINAL list is inline a second time in
  `assurance.schema.json:171`. `common.schema.json`'s `$defs` were enumerated
  programmatically and contain no verdict and no decision-value enum.
- **`E2`'s announced list against the tree** — the measurement behind `O-2`.
  `tooling/announced_path_disclosure.py:ANNOUNCED` holds 16 entries (the contract plus the 15
  pack files of the 2026-08-03 re-baseline), hand-written per `E5` and matching `E2`'s text
  exactly; `schema/document-assurance-v3/` holds 15 files today, of which 14 are announced.
- **The two new-surface claims of the `38038ec` amendment**, both verified rather than taken:
  `assurance/templates/run-v2/run_bind_v2.py:97,484-517` reads `control/bind-declarations.json`,
  validates it as `bind_declarations` and copies `governance_scan` and `disclosures` into the
  candidate beside it; and `bind-declarations.schema.json` is absent from `ANNOUNCED`, so
  "not an announced path until a later `E2` re-baseline" holds.
- **The freeze window, re-derived rather than assumed** (`REVIEW.md`'s deliverables section):
  `.harness/review-pending.json` carries subject `c50362cce992a1ee24329e90da5399e8f1da30a8`,
  dispatched `2026-09-03T01:08:56+00:00`; the branch tip is that same commit, so no commit landed
  inside this read's window. The marker was written by `tooling/construction_dispatch.py --read`
  through `dispatch.write_freeze_marker`, which that module imports.

## 3. The two deferrals, discharged

Both commits since the last read recorded that their bytes owed an independent read and would
ride the next read of this layer. Read here, at per-member cost — both members were read end to
end anyway.

- **`1c18e4a` — the `E10` free-channel application to `R10`'s first sentence.** The applied
  bytes are the content the `51bd4f6` read named, in `E10`'s own mirror-image form: *"The
  instrument's own rider bank (`HARNESS-RIDERS.md` at the instrument's root) is the construction
  side's internal debt ledger; … belong to HarnessIssue or to the caller's own bank, never the
  instrument's."* Re-derived here: `init_target.py:43-44` maps `rider-bank.md → HARNESS-RIDERS.md`
  at a caller's root, so the bare token did resolve to the forbidden referent in a caller, and
  the holder qualifier removes that. The commit records the two facts the channel requires (adds
  no clause, changed no rule's requirement; no round had relied on the sentence). **The
  application stands.**
- **`38038ec` — the `E10` amendment adding the `bind-declarations` entry to `README.md`'s
  *Review + disposition schemas* row**, taken under the rely-before-read deferral. The commit
  records both facts that deferral requires and both hold: the entry adds no clause and changes
  what no rule requires, and no round in flight reads the row. The entry's own two claims are
  measured true above. **The amendment stands** — with one stale sentence it left behind in the
  same row, which is `L-1`.

The debt of both is discharged by this record.

## 4. Findings

**No must-fix.** The `51bd4f6` read's `M-1` was downgraded to low by the user on 2026-09-02
(ruling (c), recorded in `1c18e4a`) and banked as rider `record-commit-owner`; the two texts
still command opposite acts, and the row's redeem surface — a design round touching `R6` or
`REVIEW.md`'s *Where the result lives* — is round `PROMISE-PATH-VOCAB`, whose plan step 3 folds
it. Nothing found here rises to must-fix.

### L-1 (low) — `README.md`'s row now enumerates four entries and its count sentence still says two, and the third of the three is not what the sentence says it is

**Where.** `document-harness/README.md:20`, the *Review + disposition schemas (V3-N2)* row:
*"… it is the only entry in this row that references any of the five, measured rather than
inferred, and **the other two** reach `common` for other definitions entirely) · [assurance] …
· [harness-issue] … · [bind-declarations] …"*.

**Measured.** The row enumerates four entries since `38038ec`. `$ref` targets, counted
programmatically at the subject:

- `review.v2.schema.json` references all five moved definitions (`finding`,
  `instructionCompleteness`, `perObligationDisposition`, `reviewRound`, `verifyScope`), so the
  *only entry … references any of the five* half is still **true**;
- `assurance.schema.json` reaches `common` for `actorName`, `candidateRef`, `digestRef`,
  `gitRev`, `isoDate`, `slug` — other definitions entirely;
- `harness-issue.schema.json` reaches `common` for `slug`, `digestRef`, `assuranceStatus`,
  `actorName`, `isoDate` — other definitions entirely;
- `bind-declarations.schema.json` reaches `common` **not at all**: its only two `$ref`s are
  `assurance.schema.json#/$defs/governanceScanState` and `…#/$defs/disclosure`.

So "the other two" is short by one, and the one it is short by is the one entry of which the
sentence's predicate is false.

**Why it is a finding and not noise.** The row is what a reader consults to learn which schema
holds what; the sentence's whole purpose is to say that the row's other entries do not reach the
five, and it now under-counts the set it is quantifying over. The defect class is the one
`HD-41` ④ and `E7` exist against — an enumeration grew and the sentence counting it did not — and
it landed in the amendment commit whose deferral this read discharges, which is the moment it is
cheapest to catch.

**Tier, stated so it can be overruled.** Low, and **wording-level by `R9`'s test**: the fix
changes no check outcome, evidence binding, permission, obligation or verdict path, and the
accurate fact is recoverable from adjacent text — the row itself lists its four entries, so a
reader who counts sees the "two" is stale. That classification is what makes `O-1` live.

**The exact bytes** (`README.md:20`, the substring is unique in the file — `grep -c` returns 1):

- replace `and the other two reach \`common\` for other definitions entirely`
- with `and of the other three, \`assurance\` and \`harness-issue\` reach \`common\` for other definitions entirely while \`bind-declarations\` reaches it for nothing — its only two \`$ref\`s are into \`assurance\` beside it`

Any wording that carries the same two measured facts — three others, and one of them referencing
`common` not at all — is equivalent; the bytes above are supplied so the free channel has
something exact to apply if that is the route taken.

### L-2 (low) — contract §5 says these closed enums have a single home in `common.schema.json`; 5 of its 11 rows do, and the round now open is a vocabulary change

**Where.** `contract/Document-Work-Assurance-Contract-v4.md:111`, the section heading
*"## 5. Closed enums (single home: common.schema.json)"*, over a table of eleven rows.

**Measured** (the row-by-row audit is in §2). Five rows are `$defs` of `common.schema.json`.
Six are not: the two verdict rows live inline in `review.v2.schema.json` — those two rows
**disclose it themselves**, each ending "(schema at N2)" — and the four decision-value rows
(START, REPAIR, FINAL, ISSUE_TRIAGE) live inline in `user-decision.schema.json` and carry no such
annotation. The FINAL list additionally has a **second** inline home in
`assurance.schema.json:171`, whose own description calls it "a copy of the user's own decision …
the one restatement that is not a strengthening (V3-D4, N2-A9)" — so the duplicate is deliberate
and disclosed where it sits, but it is a second place a value has to be added.

**The downstream decision that goes wrong.** An author expanding or renaming a closed-enum value
reads this heading to learn where the vocabulary lives. Round `PROMISE-PATH-VOCAB` is exactly
that act: `HD-70` authorises adding a third VERIFY verdict value. For the verdict class the
heading is corrected by the row's own "(schema at N2)", which is why this is low and not
must-fix; for the decision-value class it is not corrected anywhere in §5, and an author who
trusted it would edit a file where the enum does not exist and would not be told that FINAL has
two homes. The plan's step-3 site list for this round is correct as written — it names
`review.v2.schema.json` and not `common.schema.json` — so nothing is failing right now; what is
wrong is the map, not this round's route.

**No bytes, deliberately.** The contract is signed; §13 forbids amendment in place, and every
correction in this family so far took an explicit user ruling that says so in as many words
(`HD-63`, `HD-64`, `HD-67`, `HD-68`, `HD-70`). Whether this is a sixth such ruling, a versioned
successor, or left standing with the annotation the two verdict rows already carry is the user's,
carried by the orchestrator. What this read supplies is the measurement, not the route.

**Forward correction of a committed conclusion** (`HD-59`; the record it corrects is not edited).
`v3-cold-read-51bd4f6.md` §2 recorded that "WorkState status, audit result, **both verdict
lists**, the four decision phases, the six `LocalCheckSpec` kinds and the two verification modes
each match `common.schema.json` exactly". Measured here, `common.schema.json` carries no verdict
enum at all and no decision-value enum; the four items that are `$defs` there do match exactly.
The correction is forward and this paragraph is where it lives.

### O-1 (observation) — this record is the moment rider `wl-route`'s deadline names, and the two routes still disagree

`wl-route` (banked at `v3-checkpoint-read-f61ce2c.md` `L-2`) records that a wording-level finding
whose record supplies bytes has two routes and three sentences, two to one: `E10`'s free-channel
enumeration and `R10`'s routing sentence say apply it now; `R9`'s opening sentence says a read's
wording-level findings are banked and ride the next batch. Its deadline is written as *the next
read record that supplies bytes for a wording-level finding* — the moment the disagreement can
first bite.

`L-1` above is that finding, and this is that record: it is classified wording-level by `R9`'s own
test, in as many words, and exact bytes are supplied. So the orchestrator has to pick a route
today, and the layer gives two answers. (The `51bd4f6` read's `L-1` came close — the free channel
was taken for it in `1c18e4a` without the `R9` route being named — but that record never
classified the finding as wording-level, so whether the deadline had fired then was a judgement
nobody had to make. Here it is on the face of the record.)

**Not re-banked** (`R10`): the row exists, its target and redeem-when stand, and the fix is design
— any tiebreak adds a bound to `E10`'s enumeration or to `R9`, which opens a round. What is new
is only that the deadline has arrived, which is the orchestrator's to act on and the user's to
rule.

### O-2 (observation) — `E2`'s announced set is no longer decidable by inspecting the pack directory

`E2` (`document-harness/CONSTRUCTION-CHECKLIST.md:43-70`) announces
`contract/Document-Work-Assurance-Contract-v4.md` and *"every file the
`schema/document-assurance-v3/` pack held at the 2026-08-03 re-baseline (fifteen files …)"*, and
says of the pair "One path and one directory, **both decidable by inspection**". Measured at the
subject: the directory holds **15** files, of which **14** are announced —
`bind-declarations.schema.json` joined 2026-09-02 and is carved out by `E2`'s own next clause —
while one announced file, `review.schema.json`, is not in the tree at all (it left in round
`V1-RESULT-RETIRE`). Inspecting the directory therefore returns neither the announced set nor its
size; the operative list is the hand-written `ANNOUNCED` tuple in
`tooling/announced_path_disclosure.py`, which matches `E2`'s text exactly and is hand-written
precisely so it does not read the directory back (`E5`).

Recorded rather than banked, for three reasons: the drift is in this repository's own declared
rule file rather than in a member; the direction is safe — the only announced file missing from
the tree cannot be changed again unless it is recreated, so nothing can be under-disclosed by
this gap; and `README.md`'s new row states the carve-out for the one file it applies to, so a
reader is told. What it does name is a question the user owns: the pack has drifted twice since
the 2026-08-03 baseline, and `E2` re-baselines by ruling rather than automatically.

## 5. Re-derived independently, already banked — no new rows

Each was reached from the bytes before the bank was opened; none is re-banked (`R10`).

- **`record-commit-owner`** — the `R6` / `REVIEW.md` split described above. Still live in the
  bytes; row correct, and its named redeem surface is this round.
- **`wl-route`** — see `O-1`.
- **`read-name-split`** — no criterion between `checkpoint-read` and `cold-read`. Confirmed:
  `checkpoint` appears in the layer only inside `R6`'s filename list.
- **`e10-fifth-reader`** — `E10`'s "Four readers" is short one here:
  `tooling/construction_dispatch.py` reads `rules` and refuses to dispatch without it; the prompt
  that produced this read is that command's output.
- **`charter-qualifiers`** — `ORCHESTRATION.md`'s cite-only table drops qualifiers the cited rules
  carry, including `E10`'s "unless the user waives it" on the opening cold read (row 1).
- **`e10-freeze-exception`**, **`e9-pair-budget`**, **`orch-caller-rule-counterpart`**,
  **`e10-its-referent`** — re-derived unchanged from the `51bd4f6` read; the bytes each names are
  byte-identical at this subject.

Checked and **not** stale, against the sentence each mirrors: `layer_path_check.LAYER` is `E10`'s
seven paths in `E10`'s order; `README.md`'s member-count row defers to that sentence and reads
seven; `ORCHESTRATION.md`'s two tables hold nine and three obligations, the twelve `README.md`
counts; `README.md`'s onboarding row's ten items match `ONBOARDING.md`'s ten numbered sections
(the row names nine, "instance files" covering items 3 and 4, and says so later in its own text);
all 15 files of the schema pack are named in `README.md`; `caller.DEFAULT_REVIEW_RECORD_DIRS` is
`assurance/review-records/` beside `DEFAULT_SPECIFICATION_SURFACE` `assurance/runs/`, which is
what `REVIEW.md`'s deliverables section says the shipped default is; `EXECUTION.md`'s
tier-exception list names `document-harness/templates/` and
`tooling/rsclib/document_harness/init_target.py`, and both exist at the subject.

One class-sweep result recorded for the round now open rather than as a finding: the layer's
statements about a blocker still standing after the VERIFY are `R3`, `REVIEW.md:129-135`, contract
`:118` / `:127-129` / `:196-197` — all of which `HD-70` or the plan's step 3 already names — plus
`EXECUTION.md`'s *After a review* ("*the honest dispositions left are `STOPPED_REPLAN` or a user
`ACCEPT_WITH_LIMITATIONS`*"), which no site list names. Measured against the change `HD-70`
authorises, that sentence stays true either way: it describes what the run may do after such a
VERIFY, not what the VERIFY returns. Nothing is owed there; it is written down so the executor's
sweep need not re-derive it.

## 6. Coverage and honesty ceilings (`R4`)

- **Read in full**: all seven members, the declared checklist, and `HARNESS-DECISIONS.md`'s
  `§live` (twelve live entries: `HD-70`, `HD-69`, `HD-66`, `HD-65`, `HD-62`, `HD-59`, `HD-41`,
  `HD-36`, `HD-35`, `HD-34`, `HD-23`, `HD-9` — one more than at `51bd4f6`, `HD-70` having been
  transcribed by the subject commit itself).
- **Sampled**: `HARNESS-RIDERS.md` — the rows named above plus every row whose id matched a
  finding of mine, not all of them; `document-harness/plans/promise-path.plan.md` at its
  round-2 sections, read to test whether `record-commit-owner`'s named redeem surface is real
  (it is); the review-record corpus by targeted grep and one record read in full
  (`v3-cold-read-51bd4f6.md`, to know what the deferrals owed).
- **Probed only**: `tooling/` and `schema/` — `layer_path_check.py`, `sweep_refs.py`,
  `review_freeze_check.py`, `caller.py`, `init_target.py`, `construction_dispatch.py`,
  `announced_path_disclosure.py`, `run_bind_v2.py` and the schema pack, each read at the sites a
  member's claim named. The rest of both trees was not read.
- **`UNVERIFIABLE` from here**: everything on the caller's side — whether a product run is in
  flight, whether a caller's hook calls two tracked checks, and the five battery legs whose
  scripts live in the caller's tree. `L-2`'s consequence is stated as a property of the texts and
  of the schema pack, not as an observed failure.
- **Process claims are marked, not verified**: byte-level properties were established from the
  files' bytes at the clean worktree, whose hashes equal the subject's blobs, rather than from a
  console rendering (`REVIEW.md`'s Windows read discipline); that this session began cold is a
  process claim with no evidence lock.
- **One measurement correction is carried forward, not applied in place** — see `L-2`'s last
  paragraph. `HD-59` is why it sits here rather than in the record it corrects.
- This repository's own `.githooks/pre-commit` does not call `review_freeze_check.py`, so the
  window above is discipline rather than machine — re-derived from the marker and the branch tip
  rather than assumed.
