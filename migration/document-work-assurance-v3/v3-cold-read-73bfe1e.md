# Instruction-layer read — subject `73bfe1ede2d57808373f317b75edf7ee29645456`

An `E10` read of the harness's own instruction layer. **Not a round** (`R3`): no budget spent, no
verdict carried; the output is findings tiered must-fix / low / observation. Dispatched with the
charter this repository declares under `rules` in the `harness.json` at its root —
`document-harness/CONSTRUCTION-CHECKLIST.md` — read in full, then the counterpart that file names,
`document-harness/RULES.md`, also in full. `HARNESS-DECISIONS.md`'s `§live` was read in full at
this repository's root, as `E10`'s last clause requires of the opening.

Record name: `v3-cold-read-`. `R6` offers two read filenames and the layer still defines no
criterion for choosing between them (rider `read-name-split`, open, re-derived here and not
re-banked). Taken for the reason every previous whole-layer opening record took it.

**Findings: 0 must-fix, 2 low, 2 observation.**

---

## 1. The member set and the coverage, both derived

The dispatch enumerated no members and no scope (`R2`). `E10`'s own sentence at the subject
(`document-harness/RULES.md:86-94`) reads **exactly seven paths**. Blob ids from
`git ls-tree -r 73bfe1ede2d57808373f317b75edf7ee29645456`, run here:

| # | member | blob at `73bfe1e` | last recorded end-to-end read | this read |
|---|---|---|---|---|
| 1 | `document-harness/RULES.md` | `a9cd92dd8132493ffa50f368c90fa14e54068843` | `v3-cold-read-c50362c.md`, blob `f4d5698d…` — **changed** (`15e5ccc`) | **end to end** |
| 2 | `document-harness/README.md` | `f12d584c829d11c8afa44affad18832df2c26fe5` | `v3-cold-read-c50362c.md`, blob `1ddb7e04…` — **changed** (`b9710af`) | **end to end** |
| 3 | `document-harness/EXECUTION.md` | `08fa87f8380b60a0af4e125e1bfe88747d26f0e4` | `v3-cold-read-c50362c.md`, **same blob** | **end to end** |
| 4 | `document-harness/REVIEW.md` | `e6199bc5fa4fb197d86bad9153d9042d62748b77` | `v3-cold-read-c50362c.md`, blob `71707a3a…` — **changed** (`61afc26`, then `15e5ccc`) | **end to end** |
| 5 | `document-harness/ORCHESTRATION.md` | `3f9cd61ca42c94ca2a3080d13412741173bd73b4` | `v3-cold-read-c50362c.md`, **same blob** | **end to end** |
| 6 | `contract/Document-Work-Assurance-Contract-v4.md` | `7cba2ac405618f874f450521a50eea26f50032e7` | `v3-cold-read-c50362c.md`, blob `de210772…` — **changed** (`15e5ccc`) | **end to end** |
| 7 | `schema/document-assurance-v3/paragraph-map.schema.json` | `09aa869962f592c2f86c9379be0ef3eb7d2232ff` | `v3-cold-read-c50362c.md`, **same blob** | **end to end** |

Plus, not a member, read for the reason `E10`'s second sentence gives:

| — | this repository's declared rule | blob at `73bfe1e` | this read |
|---|---|---|---|
| — | `document-harness/CONSTRUCTION-CHECKLIST.md` | `97ed956be92864dda125cb2ac8970b1375bcc8bc` | **end to end** |

**Nothing was taken by citation.** Four member blobs moved since the last recorded read and three
did not; all seven were read end to end anyway, so the narrow form was available and not used.
That four moved and which four is re-derived here, not accepted from the opening commit's body:

```
$ git diff --name-status c50362c 73bfe1e -- document-harness contract schema harness.json
M  contract/Document-Work-Assurance-Contract-v4.md
M  document-harness/README.md
M  document-harness/REVIEW.md
M  document-harness/RULES.md
A  document-harness/journal/core-mount-2026-09-03.md
M  document-harness/journal/promise-path-vocab-2026-09-03.md
A  document-harness/plans/core-mount.plan.md
M  document-harness/plans/promise-path.plan.md
M  schema/document-assurance-v3/assurance-work-state.schema.json
M  schema/document-assurance-v3/review.v2.schema.json
M  schema/document-assurance-v3/user-decision.schema.json
```

`harness.json` is not in that list: it is byte-unchanged at `8320c2c4…` and still reads
`{"policy": "CONSTRUCTION-LEDGER.md", "rules": ["document-harness/CONSTRUCTION-CHECKLIST.md"]}`,
which is why the eighth row is here and why `CONSTRUCTION-CHECKLIST.md` is not among the seven.

The worktree is clean apart from an untracked `.goals/` (`git status --porcelain` → `?? .goals/`),
and `git hash-object` on the eight paths returns the eight blob ids above — so the bytes read are
the bytes at the subject.

## 2. What was run

- **Path-token resolution over the whole standing text**, not only added lines — the class `E10`'s
  clause says the guard never re-scans. `unresolved_tokens` and `LAYER` imported from
  `tooling/hooks/layer_path_check.py`, applied to each scanned path's bytes at the subject:
  `unresolved path tokens over WHOLE standing text: 0` over all eight files. `LAYER` is still the
  same seven paths in the same order as `E10`'s sentence.
- **Markdown links**, which carry no backtick token for the guard to find: `relative markdown
  links: 40 | unresolvable: 0`, every target resolving from the file's own directory inside this
  repository. Two more than the 38 at the last read; both were added by `61afc26` to
  `REVIEW.md`'s deliverables paragraph.
- **`python tooling/sweep_refs.py`** from the repository root:
  `-- 13 caller-held or unresolvable references over 8 members and declared rule files`, all 13
  NAMETOK, the same 13 sites as at `c50362c` (line numbers in `REVIEW.md` shifted by this round's
  amendments; the sites did not). Each carries the holder `E10` requires.
- **The battery leg `EXECUTION.md` names for this repository**: `python -m pytest -q` run from
  `tooling` → `956 passed in 180.91s (0:03:00)`, exit 0, at this subject with the worktree clean.
- **Reachability of the incomplete-map criterion at a VERIFY** — the measurement behind `L-1`.
  `review.v2.schema.json`'s root `required` is
  `['schema_version', 'result_id', 'work_id', 'run_id', 'review_round', 'subject', 'verdict',
  'instruction_completeness', 'per_obligation_disposition', 'residual_uncertainty', 'reviewed_by']`
  — `instruction_completeness` is required of **every** result, and neither round branch
  (`:65-78`) removes it. The VERIFY branch admits `REVIEWED_NO_BLOCKER · SPEC_GAP ·
  UNRESOLVED_BLOCKER`, so both verdicts the two texts command are schema-legal and nothing
  mechanical chooses between them.
- **The new value's propagation, checked rather than assumed**: `contract:118`, `RULES.md:192`,
  `REVIEW.md:130`, `review.v2.schema.json:32,68` (root enum the union, VERIFY narrowing three,
  FULL narrowing added and closed at three), `:88-92` (findings required on the new verdict),
  `dispatch.py:191`, `review_result_v2.py:289` (a blocking finding must exist), and the golden /
  reachability suites. `REVIEW.md`'s claim that *the verdict is refused without them* therefore
  binds in two places, not one.
- **The ordinal class, swept for residue**: `grep -n "fourth\|third value\|two verdicts\|three
  verdicts\|closed at three\|the two rounds"` over the eight files returns **nothing** — the
  ordinal `15e5ccc` removed from `contract:127` has no surviving sibling in the layer.
- **`E2` disclosure on the one announced-path commit in the range** (`15e5ccc`): its body names
  `contract/Document-Work-Assurance-Contract-v4.md` site by site (`:118`, `:127`, and the three
  sites left unchanged with the ruling that ratified leaving them) and both written pack files.
  Mechanically decidable and decided; what the body says about those sites is judged in §3.
- **Two factual claims `E10` makes about code**, both re-derived: `dtw dispatch` names the
  declared files in the prompts it writes (`dispatch.py:102-138`, `declared_rules_line`, read from
  `harness.json` rather than a constant), and `dtw init` writes the file empty with both fields
  present (`caller.render_harness_config`, `json.dumps({"policy": …, "rules": …})`, and
  `init_target.py:145-146` on why the two fields are left empty). Both hold.
- **The freeze window, re-derived rather than assumed** (`REVIEW.md`'s deliverables section):
  `.harness/review-pending.json` carries subject `73bfe1ede2d57808373f317b75edf7ee29645456`,
  dispatched `2026-09-03T07:14:58+00:00`; the branch tip is that same commit, so no commit has
  landed inside this read's window.

## 3. The three deferrals, discharged

Every commit that moved a member's bytes since the last read recorded that those bytes owed an
independent read and would ride the next read of this layer. All three are read here, at the bytes
above, end to end.

- **`15e5ccc` — the `UNRESOLVED_BLOCKER` design, in `contract:118`/`:127`, `RULES.md` `R3` and
  `REVIEW.md`.** Authorised for the contract site by `HD-70`, which overrides §13's
  never-amended-in-place clause for one row and one value and refuses precedent; the ordinal at
  `:127` and `user-decision.schema.json:44` are the sibling sites `HD-70`'s own forward correction
  ratifies, and `:117`, `:195-196`, `:200-201` are the sites it ratifies leaving alone — measured
  unchanged here. The vocabulary is consistent across all eight sites listed in §2, and the value
  does what the text says it does. **The design stands**, with one residue in `R3`'s new sentence,
  which is `L-1`.
- **`61afc26` — rider `record-commit-owner`'s fix in `REVIEW.md`'s *Where the result lives* and
  `:46`.** The two texts that commanded opposite acts now command one: the reviewer persists into
  the worktree, the orchestrator commits. `R6` is unchanged and the row is deleted in that same
  commit (`R10`), leaving 36 rows — re-counted here: `grep -c "^| [a-z0-9-]* |" HARNESS-RIDERS.md`
  → `37`, one of which is the header. **The fix stands**, with one attribution residue, which is
  `O-1`.
- **`b9710af` — the `E10` free-channel application to `README.md:20`.** The applied bytes are the
  ones the `c50362c` record supplied, and both of the channel's conditions were recorded. Its two
  measured claims re-derived here independently: `bind-declarations.schema.json` has exactly two
  `$ref`s, both into `assurance.schema.json` (`governanceScanState`, `disclosure`) and none into
  `common`; `assurance.schema.json` reaches `common` for `actorName · candidateRef · digestRef ·
  gitRev · isoDate · slug` and `harness-issue.schema.json` for `actorName · assuranceStatus ·
  digestRef · isoDate · slug` — other definitions entirely, none of them among the five moved.
  **The application stands.**

The debt of all three is discharged by this record. Whether `HD-70` now moves state is the user's
(`R5`, `HD-2`); what this read supplies is the re-read it named as the condition.

## 4. Findings

**No must-fix.**

### L-1 (low) — `R3`'s new *never `SPEC_GAP`* is unqualified, and `REVIEW.md` still commands `SPEC_GAP` for one VERIFY state in which a blocker stands

**Where.** `document-harness/RULES.md:192-194`, the sentence `15e5ccc` added:

> Reach for `UNRESOLVED_BLOCKER`, **never `SPEC_GAP`**, when a blocking finding stands at the end
> of the VERIFY

against `document-harness/REVIEW.md:264-268`, which is unchanged and which settles the same
question the other way:

> **If both apply** — a real blocker in the candidate *and* an unmapped unit of the stopping kind
> — return `SPEC_GAP`. […] *This precedence is stated here rather than derived: V3-D6 and V3-D7 do
> not settle the collision, and a reader should treat it as this file's rule, not the plan's.*

**Measured — the state is reachable, and reachable at a VERIFY specifically.** `REVIEW.md`'s
incomplete-map section is not FULL-scoped: its stage marker (`:201-204`) governs the reviewer's
post-hoc recheck of *a finished candidate*, `C2` included; *What every result must carry*
(`:149-157`) puts the recheck on every result; and `review.v2.schema.json` requires
`instruction_completeness` on every result with no round branch removing it (§2). So a VERIFY
reviewer who re-walks the raw instruction, finds a stopping-kind unmapped unit the FULL's reviewer
missed, and also has a blocker standing after the repair is commanded `UNRESOLVED_BLOCKER` by the
rule file and `SPEC_GAP` by the charter. Both are schema-legal for a VERIFY, so nothing downstream
refuses either.

**The class, not the instance** (`E7`). Sites that command `SPEC_GAP` for a condition able to
co-occur with a standing blocker at the VERIFY, scope = the seven members plus the declared rule
file at this subject (`grep -n "SPEC_GAP"`, 27 hits, each read):
`REVIEW.md:264-268` (above) and `contract:30` (*a genuine conflict between this contract and the
plan is a `SPEC_GAP`, not a reinterpretation opportunity*). The other 25 are enumerations, the
audit result, the execution-time rule, or flow descriptions, and none commands a verdict choice.

**Why the round did not see it.** `15e5ccc`'s `HD-41` (4) class scan was scoped to *sites
enumerating the VERIFY verdict vocabulary*, and executed as `git grep -n REVIEWED_NO_BLOCKER … |
grep SPEC_GAP`. A site that **commands** one of the values without enumerating them cannot appear
in that scope. The scan was run and reported honestly; the class it defined was narrower than the
class the change created.

**The downstream decision that goes wrong.** Which verdict a VERIFY returns in that state, and
therefore what the record tells the next reader is owed: `SPEC_GAP` says a new WorkSpec revision
and a new user START are required, `UNRESOLVED_BLOCKER` says the run stops on named standing
findings. That is exactly the confusion the round was opened to end, reintroduced at the one place
where `SPEC_GAP` was still correct despite a standing blocker.

**Tier, stated so it can be overruled.** Low rather than must-fix: both verdicts stop the run, so
no work is wrongly accepted; the state needs a stopping-kind unit that the FULL missed, so it is a
conjunction rather than a routine path; and `RULES.md`'s own header gives a reader a tiebreak
(*where a charter and a rule below address the same obligation, the charter names the owner and
this file is the text*). Low rather than observation: applying that tiebreak silently overrides a
precedence `REVIEW.md` states as its own rule, which no ruling has withdrawn.

**Explicitly not wording-level** (`R9`): the fix changes a **verdict path**, which is one of the
five things `R9`'s test excludes, so the bank-and-ride route `R9` gives wording-level findings is
not available on its own terms.

**No bytes, deliberately.** The minimum fix is one qualifier, and either place it can go changes
what a rule requires: qualifying `R3`'s *never* to the borrowed-`SPEC_GAP` state alone, or scoping
`REVIEW.md`'s both-apply precedence to the FULL round its own rationale argues from (*spending the
single permitted round on the blocker*). Both add a bound, so `E10`'s design test opens a round for
either, and the free channel is closed to it. What this read supplies is the collision and its
scope; which qualifier, and where, is design.

**Route.** A finding below must-fix without appliable bytes banks (`R10`). Target = `RULES.md`
`R3`'s VERIFY sentence and `REVIEW.md:264-268`; redeem-when = the next **round-eligible** batch
touching either, since the fix is design and an `E10` amendment commit could not redeem it;
deadline = the first product-run VERIFY that records `instruction_completeness: INCOMPLETE` with a
blocking finding standing — the moment the disagreement can first bite, and outside the round that
writes the row, since no product run is in flight in this repository.

### L-2 (low) — `REVIEW.md`'s FULL scope cell still calls the subject *the whole frozen package*, a form the same file says is gone

**Where.** `document-harness/REVIEW.md:129`, the *two rounds* table:

```
$ grep -rn "the whole frozen package" <the seven members + the declared rule file>
document-harness/REVIEW.md:129:| FULL | `REVIEWED_NO_BLOCKER` · `CHANGES_REQUIRED` · `SPEC_GAP` | the whole frozen package |
$ grep -c "the whole frozen package" document-harness/REVIEW.md
1
```

**Measured.** Every other occurrence of *package* in the layer is either explicitly historical or
inside a stage marker that says so: `REVIEW.md:87,91,93,94,101,106` (*the package-bound sections it
succeeded are gone*; *there is no package digest to reproduce*), `EXECUTION.md:94` under its own
marker at `:102-112` (*there is no review package to regenerate … newly opened runs are successor
runs, and the package-bound form is pre-wave-2 history*), and `contract:257,275,281,291` (v1
history and the version boundary). `:129` is the single site that describes a **live** round's
scope in the retired vocabulary — and it sits two sections below the one that retires it. The
VERIFY cell beside it is form-neutral and was not affected when `15e5ccc` grew its verdict list.

**The downstream decision that goes wrong.** A cold FULL reviewer's first act is to locate its
subject. The dispatch hands one SHA (`E12`); this cell says the scope is a package. The
reconciliation is available two sections up, so the cost is a detour rather than a wrong scope —
which is why this is low and why it is wording-level.

**Wording-level under `R9`'s test**: no check outcome, evidence binding, permission, obligation or
verdict path changes, and the accurate fact is recoverable from adjacent text (*When the subject is
one commit*, `:84-123`).

**The exact bytes** (`REVIEW.md:129`, substring unique in the file, `grep -c` → 1):

- replace `the whole frozen package`
- with `the whole dispatched subject — the committed control plane as floor, and the tree at the pinned revisions`

Any wording carrying the same two facts — the subject is the evidence commit, and the committed
plane is a floor rather than a ceiling — is equivalent; the bytes are supplied so the free channel
has something exact if that is the route taken.

**Route note.** This is again the event rider `wl-route`'s deadline names — a read record supplying
bytes for a finding it classifies wording-level. The row is **not re-banked** (`R10`): it stands,
its tiebreak is still design, and the route the last two applications took (`1c18e4a`, `b9710af`)
is `E10`'s free channel.

### O-1 (observation) — the amended deliverables sentence attributes to `R6` an act covering two artifacts; `R6`'s text covers one

`REVIEW.md:166-170` now reads *"You persist, into the worktree, exactly two artifacts, and the
orchestrator commits them unchanged: `RULES.md` `R6` owns that act and the title it lands under"*.
`R6` (`RULES.md:246-252`) names one artifact — the review record — and one title,
`V3-REVIEW-RECORD-<ROUND>-<sha>-v1`; `ORCHESTRATION.md:60`'s row likewise says *commit the
reviewer's record unchanged*. So the ReviewResult's commit has no named owner and no title anywhere
in the layer, and the sentence that closed rider `record-commit-owner` covers the gap by citation
rather than by text.

Recorded, not banked: the reviewer's action is unchanged either way (persist both, commit neither),
and in practice the two ride one commit. It is written down because the residue was created by the
fix, and the next batch touching either text is where it is cheapest to close.

### O-2 (observation) — a VERIFY's stated scope excludes the instruction map, and its result is required to carry an instruction-completeness recheck

`R3` and `REVIEW.md:130` both give the VERIFY the scope *the accepted findings, the entire repair
diff, and the permanent boundaries*. `REVIEW.md:149-157` (*What every result must carry*) and
contract invariant 10 put an instruction-completeness recheck against the **raw instruction** on
every result, and `review.v2.schema.json` requires the field of both rounds (§2). A VERIFY reviewer
is therefore told its scope stops short of the instruction map and that its result must report on
it.

This is the substrate `L-1` stands on and it exists at bytes this round did not touch. Whether the
VERIFY should re-walk the instruction at all is a *should this exist* question and is the user's,
not this read's (`R5`); what is reportable is that the two statements sit in the same file and only
one of them is visible from the scope column a VERIFY reviewer reads first.

## 5. Re-derived independently, already banked — no new rows

Each was reached from the bytes before the bank was opened; none is re-banked (`R10`).

- **`e10-fifth-reader`** — `E10`'s *Four readers* is still short one: `tooling/construction_dispatch.py`
  reads `rules` from `harness.json` (`:150-153`), refuses to dispatch without it, and holds the
  `--read` mode that produced this read's own prompt. `ORCHESTRATION.md:39-45` names that
  construction-side dispatch as a declaration-deriving command while `E10`'s count does not.
- **`read-name-split`** — no criterion between `checkpoint-read` and `cold-read`; `checkpoint`
  still appears in the layer only inside `R6`'s filename list.
- **`wl-route`** — see `L-2`'s route note.
- **`enum-single-home`** — contract §5's *single home* heading, banked from the last read under the
  user's ruling 2a; re-derived unchanged, and this round's verdict-row change does not trigger its
  deadline (a decision-value enum change does).
- **`charter-qualifiers`**, **`e10-freeze-exception`**, **`e9-pair-budget`**,
  **`orch-caller-rule-counterpart`**, **`e10-its-referent`** — re-derived from the bytes each names;
  all sit in members whose blobs are unchanged since the last read.

Checked and **not** stale: `layer_path_check.LAYER` is `E10`'s seven paths in `E10`'s order;
`README.md`'s member-count row defers to that sentence and reads seven; `README.md`'s schema rows
name all 15 files of the pack; `ORCHESTRATION.md`'s two tables hold nine and three obligations, the
twelve `README.md` counts; the ordinal class `15e5ccc` closed has no residue in the layer; the
`E2` announced list in `tooling/announced_path_disclosure.py` still matches `E2`'s text.

## 6. Coverage and honesty ceilings (`R4`)

- **Read in full**: all seven members, the declared rule file, and `HARNESS-DECISIONS.md`'s `§live`
  — **eleven** live entries, counted here (`sed -n '/^## §live/,/^## §implemented/p' … | grep -c
  '^### HD-'` → `11`): `HD-69`, `HD-66`, `HD-65`, `HD-62`, `HD-59`, `HD-41`, `HD-36`, `HD-35`,
  `HD-34`, `HD-23`, `HD-9`. One fewer than the twelve at `c50362c`: `HD-70` moved to
  `§implemented` inside this round, and its entry was read there in full because this read
  discharges the deferral it names.
- **Sampled**: `HARNESS-RIDERS.md` — the rows named above plus every row whose id matched a finding
  of mine, not all 36; the three commit bodies that moved member bytes (`15e5ccc`, `61afc26`,
  `b9710af`), read in full; `v3-cold-read-c50362c.md`, read in full to know what the deferrals owed;
  the review-record corpus by targeted grep only.
- **Probed only**: `tooling/` and `schema/` — `layer_path_check.py`, `sweep_refs.py`, `caller.py`,
  `init_target.py`, `dispatch.py`, `construction_dispatch.py`, `review_result_v2.py`,
  `review.v2.schema.json`, `bind-declarations.schema.json`, `assurance.schema.json`,
  `harness-issue.schema.json`, `user-decision.schema.json`, each read at the sites a member's claim
  named. The rest of both trees was not read; the battery was run whole but its 956 assertions were
  not inspected.
- **`UNVERIFIABLE` from here**: everything on the caller's side — whether a product run is in
  flight, whether a caller's hook calls two tracked checks, the five battery legs whose scripts live
  in the caller's tree, and `REVIEW.md:146`'s claim that a real run borrowed `SPEC_GAP` for a
  standing blocker (its evidence is a caller-held closeout body). `L-1`'s consequence is stated as a
  property of the texts and the schema, not as an observed failure.
- **Process claims are marked, not verified**: byte-level properties were established from the
  files' bytes at the clean worktree, whose hashes equal the subject's blobs, and every read of a
  JSON member was decoded as UTF-8 explicitly — this machine's default codec is GBK and refused
  `review.v2.schema.json` outright, which is `REVIEW.md`'s Windows read discipline paying for
  itself. That this session began cold is a process claim with no evidence lock.
- This repository's own `.githooks/pre-commit` was not re-derived here; the freeze window in §2 is
  established from the marker and the branch tip rather than from any assumption that a hook held
  it.
