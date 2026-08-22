# FULL review — round `EXECUTOR-CHARTER` at `229f03f`

**Verdict: `REVIEWED_NO_BLOCKER`.** 5 low, 7 observations.

**The implementation is sound and I could not break it.** The fourth dispatch family does
exactly what it claims: two modes, two charters, three derived facts and four refusals on the
product side, one sentence and nothing derived on the construction side, and no freeze marker
from either. I mutated nine bindings — every new refusal code, the marker split and both
golden files — and all nine died on their own named test, none by crashing. The two figures
the commit reports as its own measurements (`790 passed`; `layer_path_check` exit 0) are the
figures I measured, the two module digests it pastes are the digests I computed, and the
drift guard's central design claim — that `git hash-object` against `rev-parse` cannot
false-positive on eol conversion — I reproduced on a repository with `core.autocrlf=true`,
where the worktree bytes are CRLF, the blob is LF, and the guard correctly says *no drift*.
Nothing `E2` freezes was touched, and the round's authorization is visible in the repository
rather than only in chat.

**The findings are all in the instruction text, and none of them burns the fix leg on its
own.** Two are claims the layer now makes about itself that a one-command grep falsifies
(`L-1`, `L-2`); one is a new standing obligation homed in the charter of a role that is not
its actor, justified by a delivery mechanism that does not reach the actors it names
(`L-3`); one is a rider row deleted while the co-disposition its own text named is still
undone, with two more sites of the class left untracked (`L-4`); one is a generated prompt
telling a cold executor to read "the counterpart it names" from a document that names none
(`L-5`). Each has an exact minimum fix. Two of them (`L-2`, `L-3`) have a second reading
whose choice is the user's under `R5`, and I have not made it.

---

## 1. Subject, round, budget and authorization — re-derived, nothing taken from the dispatch

The dispatch handed one range and two transport sentences (the repository root, and *write
into the worktree, do not commit*). Everything below is from the repository. I reproduced my
own prompt from the generator to confirm what I was handed:
`D.construction_dispatch_of('.', '693b692…', '229f03f…')` renders the `CONSTRUCTION_PROMPT`
verbatim, so the two transport sentences are the whole of what was added to it.

**Subject.** `693b692811b5958dbcda92a3cc722123c5f44337..229f03f166ae93029f8d219f04ac03d9a76fc0c3`,
two commits. `229f03f` is `HEAD`. The worktree was clean at the start of this review, after
every mutation restore, and at its end (`git status --porcelain` → empty each time).

| commit | title | kind (named in its own body) |
|---|---|---|
| `71f7567` | `V3-REVIEW-RECORD-EXECUTOR-CHARTER-693b692-v1` | record |
| `229f03f` | `V3-EXECUTOR-CHARTER-v1` | candidate |

**Round.** `EXECUTOR-CHARTER`. `git grep -ln 'EXECUTOR-CHARTER'` returns ten tracked files;
the load-bearing two are `CONSTRUCTION-LEDGER.md:126`, whose current pointer reads
**下一队首＝轮 `EXECUTOR-CHARTER`**, and `document-harness/plans/executor-charter.plan.md`,
committed at `5f7a772` — before this range opens — and named there as the cold session's
entry point.

**Budget (`E9`).** The test is *has a valid independent FULL already occurred?*
`migration/document-work-assurance-v3/` holds exactly one record whose subject falls in this
range, `v3-cold-read-693b692.md`, and `E10`/`R3` are explicit that a read is not a round and
spends no budget. No `v3-review-full-*` or `v3-review-verify-*` names this round. So **this
dispatch is the round's one FULL**, the budget was whole when it opened, and a fix arising
from this record would be the round's single user-approved fix and would oblige a targeted
VERIFY.

**Review window (`E9`).** `.harness/review-pending.json` records the subject as exactly this
range, dispatched `2026-08-22T08:35:06+00:00`; `229f03f` was committed
`2026-08-22T18:34:58+10:00` = `08:34:58Z`, eight seconds earlier. No commit has landed since.
`.harness/` is ignored (`git check-ignore -v` → `.gitignore:18:.harness/`), so the marker is
not itself a commit. The window is intact. I confirmed independently that the marker holds
the *review* subject and not one of mine: I ran `dtw dispatch --construction-executor` against
this repository during the review and the marker's `subject` field was unchanged afterwards —
which is the round's own claim, tested from outside its test suite.

**Authorization (`R7`) — narrower ceiling than usual.** Unlike recent rounds, the opening and
the central design change are **not** chat-only. `CONSTRUCTION-LEDGER.md:126` records the
user's 2026-08-22 re-ordering ruling and states the round's purpose in the same breath —
*给 `dtw dispatch` 加执行者模式，从而删掉「运行纪律走 Context 引用」那条写作规则，让 Context
只装背景、其中出现要求即缺陷* — and the plan's §*The four user rulings of 2026-08-22* carries
rulings 1 and 2 (the two modes and the two charters they point at) in full. What I cannot see
is the answer to the plan's own **open question**: the plan states it unanswered, with three
options, and the candidate acts on one of them. That is `O-6`.

## 2. Changed paths, classified by hand

`git diff --stat 693b692 229f03f` → 11 files, 1032 insertions, 69 deletions.

| path | class | note |
|---|---|---|
| `tooling/rsclib/document_harness/dispatch.py` | code | +259; the fourth dispatch family |
| `tooling/rsclib/document_harness/cli.py` | code | +63; two modes, the marker split, docstrings, help |
| `tooling/tests/document_harness_review/test_dispatch.py` | test | +160; two new classes, `NamedIssueReachability` 11 → 15 |
| `tooling/tests/document_harness_review/test_dispatch_freeze_marker.py` | test | +30; one new class, two tests |
| `tooling/tests/fixtures/expected-executor-prompt.txt` | fixture | new, 13 lines |
| `tooling/tests/fixtures/expected-construction-executor-prompt.txt` | fixture | new, 4 lines |
| `document-harness/EXECUTION.md` | **`E10` member** | authoring rule replaced; SIMP-C3/C4 edits; `HD-52` carrier; one new standing obligation |
| `document-harness/ORCHESTRATION.md` | **`E10` member** | thin-file paragraph; role paragraph; *Handing the executor*; policy-file quantifier |
| `HARNESS-DECISIONS.md` | register (not a member, `HD-19`) | `HD-52` moved §live → §implemented |
| `HARNESS-RIDERS.md` | register | two rows deleted |
| `migration/document-work-assurance-v3/v3-cold-read-693b692.md` | record | the whole of `71f7567` |

**`E2`.** All three frozen blobs are byte-identical at both ends of the range —
`b2dbdf75…`, `68031fa2…`, `e1a2f26b…` — and
`git diff --name-only 693b692 229f03f -- schema/ contract/` returns nothing. The pack still
holds 15 files at the tip. Nothing frozen was written.

**Change boundary (`E8`).** The plan's §*Change surface* names six surfaces; the candidate
touched five of them plus `HARNESS-RIDERS.md`, which the same row names. Nothing outside it
was touched. `CONSTRUCTION-LEDGER.md` and the round journal are named there too and are
untouched — see `O-4`; on the `PREVIEW-RENDER` and `TEMPLATE-LIB-ROOT` precedents those land
at closeout, so their absence here is not an escape.

**`E8` form.** Single dense title naming the round; kind named in the first two words; no
trailers; new commit, not an amend. `git log origin/main..main` = 6 and `origin/main` is still
`f084db4`, so nothing was pushed.

## 3. What I read, sampled and probed (`R4`)

**Read in full:** `document-harness/CONSTRUCTION-CHECKLIST.md`; both stubs at
`migration/document-work-assurance-v3/v3-harness-{operating,review}-contract.md`;
`document-harness/ORCHESTRATION.md`; `document-harness/plans/executor-charter.plan.md`; the
whole diff of the range; the new executor section of `dispatch.py` (`:732`–`:1006`) and
`_cmd_v3_dispatch` in `cli.py`; both new test classes and
`test_dispatch_freeze_marker.py` entire; both golden fixtures; `tooling/hooks/layer_path_check.py`.

**Sampled:** `document-harness/EXECUTION.md` (§1–§115, §204–§300, §433–§499 read; the
regression-tiering and audit-cadence sections skimmed); `document-harness/REVIEW.md` (headings
plus §1–§20, then grepped); `HARNESS-DECISIONS.md` (`HD-2`, `HD-4`–`HD-8`, `HD-41`, `HD-45`,
`HD-46`, `HD-51`, `HD-52` read; the rest grepped); `HARNESS-RIDERS.md` (the two deleted rows
and their neighbours); `CONSTRUCTION-LEDGER.md` (header, the conversation-only list, the
current pointer).

**Probed only, by command:** the caller repository at `D:/Thesis-stage-control-refactor`
(read-only, eight run instructions, grepped and section-classified — see the ceiling in §7);
a scratch git repository built for the executor mode's edge cases.

**Not read:** the run-v2 templates, the schema pack, the product review path
(`dispatch_of`/`read_control_plane`), everything the range does not touch.

## 4. The implementation — leading, per `R3`

### 4.1 It does what it claims, end to end

I drove both modes as a dispatcher would, outside the test suite.

- `dtw dispatch --construction-executor --repo-root .` → exit 0, one sentence naming
  `document-harness/CONSTRUCTION-CHECKLIST.md`, derivation line saying *nothing else is
  derived*, and **no `.harness/` write** (the pre-existing marker's `subject` was byte-identical
  before and after).
- `dtw dispatch --executor assurance/runs/nope --repo-root .` → exit 1, `NOT DISPATCHABLE`,
  `V3-DISPATCH-INSTRUCTION-MISSING`, and the refusal restates no run.
- Against a scratch repository holding `assurance/runs/run-alpha/instruction.md` committed at
  `483a44d4…`: exit 0, the three facts derived (`run-alpha`, the repo-relative instruction
  path, the 40-hex freeze), no marker written.

**The mount case, which the tests do not cover for this mode, is nevertheless correct.** With
`rsclib.document_harness.RS_ROOT` patched to `<root>/ResearchSystem/harness`,
`executor_dispatch_of` resolves the charter to
`ResearchSystem/harness/document-harness/EXECUTION.md` and the prompt carries it. This is the
deployment the product mode will actually run in, and it is the one without a test — `O-1`.

**The drift guard's design claim holds.** On a repository with `core.autocrlf=true` I checked
out the instruction so the worktree carried CRLF while the blob carried LF:
`sha256sum` differs from the blob, `git hash-object --no-filters` gives `89994b76…`, and
`git hash-object` gives `068101676be7515748b1deaa7f688081d18ea3cb` — exactly
`git rev-parse HEAD:<path>`. The dispatch derived cleanly. A byte comparison would have
refused this run; blob-id equality does not.

**No false-accept path found.** I looked for one: a symlinked run directory resolves outside
and is refused; a symlinked instruction hashes as a link and mismatches; a staged-but-uncommitted
edit mismatches; an instruction committed only on another branch returns no revision and is
refused; a run directory outside the repository, on another drive, raises `ValueError` and is
refused. Every failure mode I could construct lands on a refusal, never on a clean dispatch of
unfrozen bytes.

### 4.2 The guards bind — nine mutations, nine reds, no crashes

`E4`'s discipline, run from the review side per `R8`. Both modules were copied to a scratchpad
first and their sha256 verified before every restore; the digests are
`dispatch.py 7baa46feea3815e154392d4ef264838cc7cc6f27b23a4394738c54d4d6ad8278` and
`cli.py 7d22de6859bd6f611343849cd679b8c86c0803098bd85a7a2c421e165e129b5a`, identical before
the first mutation and after the last. Suite = `test_dispatch.py` +
`test_dispatch_freeze_marker.py`, baseline `73 passed`.

| # | what was neutered | result |
|---|---|---|
| G1 | `RUN-OUTSIDE-REPO` code string renamed | red: `…outside_the_repository_is_refused` + `NamedIssueReachability` |
| G1b | the `except ValueError` refusal made unreachable **without crashing** (a fabricated `rel` continues) | red: `…outside_the_repository_is_refused` — it binds the behaviour, not merely the code path |
| G2 | `instruction.md` existence check short-circuited to `False and …` | red: `…without_an_instruction_is_refused` |
| G3 | the freeze test `logged.returncode != 0 or len(revision) != 40` → `False` | red: `…uncommitted_instruction_is_not_frozen` |
| G4 | the whole drift comparison → `False` | red: `…drifted_from_the_frozen_bytes_is_refused` + `…refusal_is_not_a_prompt` |
| G5 | `and not executor_side` dropped from the marker condition | red: **both** executor-side tests; the review-side range test stayed green — the positive control the class docstring claims |
| G6 | the two fact lines of `EXECUTOR_PROMPT` **reordered** (nothing added or removed) | red: `…prompt_is_exactly_the_golden_file` |
| G7 | one word changed in `CONSTRUCTION_EXECUTOR_PROMPT` ("name" → "title") | red: `…prompt_is_exactly_the_golden_file` |
| G8 | `EXECUTOR_ROLE_INSTRUCTION` → `document-harness/REVIEW.md` (the other side's charter) | red: golden file + `…no_enumeration_of_work_reaches_the_executor` |
| G9 | `CONSTRUCTION_EXECUTOR_CHARTER` → `document-harness/EXECUTION.md` | red: all three of that class, including the mount test |

`G6` is the one worth naming: the whole-document golden equality catches a **reordering**,
which is the property the commit body claims for the shape and which a per-line `assertIn`
suite would miss. `G8`/`G9` are the recorded incident's own shape — citing the other side's
charter — and both constants are pinned against it.

`E5` holds: both new classes carry hand-written `CHARTER_OUTSIDE` literals, and the goldens are
committed fixtures, not the module's constants. `MARKER`, the marker's field set and the subject
form in the freeze-marker suite are likewise hand-written; the field set is asserted **whole**
(`sorted(document) == ["dispatched_at", "subject"]`), not by substring.

### 4.3 The figures, re-measured

| claim | my measurement |
|---|---|
| full battery `790 passed` | `python -m pytest -q` from `tooling/` → `790 passed in 136.40s`, run immediately before this record |
| 16 added tests are the whole delta | 10 + 4 + 2 = 16 new test methods counted by hand in the diff; no test removed. `790 − 16 = 774` is arithmetic, **not** a measurement at the base — see §7 |
| `NamedIssueReachability` 11 → 15 | `grep -o 'f"{CODE}-[A-Z-]*"' dispatch.py \| sort -u` → 15 distinct codes |
| `layer_path_check` exit 0 | re-ran the guard's own `unresolved_tokens` over the commit's added lines, using its own `LAYER` and parser: `EXECUTION.md` 41 added lines, `ORCHESTRATION.md` 26, unresolved = `[]` |
| `sweep_refs.py` = 17 | `python tooling/sweep_refs.py` → `17 caller-held or unresolvable references over 10 members`; none of the 17 falls inside a hunk this commit touched, so the "added none" half follows |
| the two module digests | identical to the pasted values |
| `grep 'by reference'` = two sites, both in scope | at `693b692`: `:235` and `:420`, no third. At `HEAD`: zero |
| `grep 'START card'` = three sites | at `HEAD`: five — the three named plus the round's two new ones. Consistent |

## 5. The instruction text

What the two members now say is largely accurate and the hard part is done well: the
supersession of p4-bridge f1's routed `WORKFLOW_FIX` is **named** rather than silently
performed, its surviving half is stated separately from its replaced half, `HD-52`'s carrier is
lifted out of the enumerated-form bullet into a paragraph that binds every product run, and
`HD-52` flips state in the same commit that lands that carrier, which is what `HD-2` and
`ORCHESTRATION.md:51` require. Rider `charter-prose-overreach` items ② and ③ are fixed
exactly as the row described them, and the absolute quantifier at `ORCHESTRATION.md:76` now
carries its scope. The five findings below are what is left.

### `L-1` (low, wording-level) — `EXECUTION.md:285` says four runs; it is five

> *…this one spent **four** runs hand-copied there for want of a home.*

The round's own plan, committed at `5f7a772`, already carries the correction and names the
miscount: *五个 separate runs parked the same item in Context … an earlier "四" missed
`p4-bridge`, whose wording differs*. I re-derived it rather than take either figure. Over the
caller's eight run instructions, classifying each hit by the heading it sits under:

```
p4-bridge    :18,:19 (preamble)  :87 '## Context (non-normative)'
p4-doc       :129,:131            '## Context (non-normative)'
p5a-firewall :94,:95,:96          '## Context (non-normative)'
p5a-shells   :227,:228,:229       '## Context (non-normative)'
p5b-firewall :171,:172            '## Context (non-normative)'
p5b-claims / p3-corr / w1-r1 : none
```

Five runs, all five reaching Context. `E3`'s last clause asks the command that could falsify
an assertion written into instruction text to be run first; the commit's scan-class evidence
covers `by reference` and `START card`, neither of which could.

**Minimum fix:** `four` → `five` at `EXECUTION.md:285`. **Route:** `R9`. I can name no
downstream decision that goes wrong if it stays — the figure is rhetorical support for a
placement, and the accurate fact is recoverable from a committed record in this repository —
so it rides the next batch touching this layer and spawns no round and no read.

### `L-2` (low) — `EXECUTION.md:440` claims a completeness the layer does not have

> *the rules the session runs under — gap banking, first-run obligations, map-filling
> disclosures — **live in this file***

The replaced text said *live in `EXECUTION.md` **and the governing plans***. The hedge was
dropped in the same edit that made the claim exhaustive. Measured across all ten `E10`
members:

```
'first-run' | 'first run'  -> EXECUTION.md:440 only
'gap bank'                 -> EXECUTION.md:440 only
```

Each of the two appears exactly once in the entire instruction layer: inside the sentence
asserting they live there. On the third item the round is right — *map-filling disclosures*
became true of this file in this same commit, at `:276`–`:286`. On the other two:

- **first-run obligations** are per-run by construction (p4-bridge's four, authored into its
  instruction), and nothing standing about them lives here.
- **gap banking** is half-carried: `EXECUTION.md:31` names the `HarnessIssue` artifact, and
  calls it *optional*; the discipline the caller's own runs glossed as *gap banking as
  `HarnessIssue`s, no silent workarounds* (p4-doc `:127`–`:128`) is written in
  `ORCHESTRATION.md`'s *executor's report back*, i.e. the **orchestrator's** charter, which the
  executor is not dispatched with.

**The downstream decision that goes wrong.** The rule's whole force is that the instruction
*no longer carries even the reference*. An instruction author whose run is governed by
standing discipline that does not live in `EXECUTION.md` now has no delivery path at all: the
dispatch names one file, and Context is closed to them. Under the old rule they wrote *and the
governing plans* and were compliant.

**Two readings, and the choice is the user's (`R5`).** Either the list is illustrative and the
fix is bytes (restore *and the governing plans*, or replace the two examples with items this
file does carry — `NOT_IMPLEMENTED` as a first-class answer, the measure-last rule, the
one-claim-per-obligation rule all qualify); or the claim is meant exhaustively and the round
intends every standing discipline to be migrated into `EXECUTION.md`, which is design and opens
a round. I have not chosen. Precedent for routing it this way: the opening cold read's `L-1`,
same shape.

### `L-3` (low) — the new standing obligation is homed where its own dispatch cannot reach its actors

`EXECUTION.md:276`–`:286` installs the C4 `O-1` recording obligation and justifies its
placement in its last sentence:

> *The obligation is written here because standing run-conduct arrives with the executor's
> dispatch (*Instruction authoring rules*), never from an instruction's Context section.*

But the obligation's actors are named in its own first sentence — *the run's **review/closeout**
records one line* — and neither is the executor:

- the **reviewer** of a product run is dispatched with `document-harness/REVIEW.md`
  (`dispatch.py:429`, `ROLE_INSTRUCTION`), and `R2` forbids it accepting anything else.
  `grep -i 'paragraph map|two[- ]map|classification|same-source' document-harness/REVIEW.md`
  returns **zero hits**;
- the **closeout** is the orchestrator's — `ORCHESTRATION.md:49` puts it *before closeout* on
  the orchestrator's obligation list and `:79` has it *state at closeout* — and
  `ORCHESTRATION.md:33`–`:35` states that nothing dispatches the orchestrator and none should.

So the paragraph reproduces, inside the round that exists to abolish it, the exact shape it
names: an obligation whose actor has no delivery path. The practical loss is bounded — the
orchestrator holds `ORCHESTRATION.md` and the ledger and can still do the closeout half, and
the reading falls due at the next product run's closeout on whatever was collected — which is
why this is a low and not a blocker.

**Minimum fix,** and all three branches are design, so `R5` routes the choice: re-home the
obligation where its actors are dispatched (`REVIEW.md` for the recording half, the
orchestrator's closeout material for the reading half); or keep it here and correct the
justifying sentence to say who is actually bound and how they learn of it; or drop the
justifying sentence and let the placement stand unargued.

### `L-4` (low) — rider `charter-prose-overreach` was deleted with its item ① half-done, and the class has two more sites

The row's own text says of item ①: *读者明说这条该摆给用户而非当场改，因为 `HD-46` ② 用了同一措辞*,
and its redeem-when says *① 与 `HD-46` 一并处置* — dispose of ① **together with** `HD-46`. The
candidate fixed the `ORCHESTRATION.md` half, deleted the row, and describes the redemption in
its body as *its first item — the `E10` half of the thin-file justification is dropped, `HD-5`
carrying the conclusion alone*, without noting what was left. `HARNESS-DECISIONS.md` in this
range changes only `HD-52`.

The scan `HD-41` ④ asks for before writing a finding's fix — which the commit body does not
show for this class — returns three sites, of which one was fixed:

```
HARNESS-DECISIONS.md:221            依据：`E10` 明写成员编辑 never re-typed "with the same content"，`HD-5` …
document-harness/ONBOARDING.md:7    are "never re-typed with the same content"; `HD-5` records transcription as a drift surface).
document-harness/plans/harness-layer-incorporation-round.plan.md:62   (describes E10's edit discipline correctly — not this class)
```

Both surviving sites make the same move the rider objected to: they cite `E10`'s
*edits are additive or subtractive* — a rule about **how this layer is amended** — as grounds
for **one member not restating another member's rule**, a conclusion `HD-5` carries on its own
in the very same sentence. Downstream is zero-change at each site, exactly as the rider said.
What is not zero-change is the bookkeeping: the row is gone, so nothing now names them, and
`R10` calls the bank *the construction side's internal debt ledger*.

**Minimum fix:** delete the `E10` half of `HARNESS-DECISIONS.md:221` and
`document-harness/ONBOARDING.md:6`–`:7` the same way it was deleted from `ORCHESTRATION.md:13`,
leaving `HD-5` to carry the conclusion — **or**, since the rider explicitly reserved the
`HD-46` half for the user, re-bank the two sites with `HD-46` named. Note that
`HARNESS-DECISIONS.md` is not an `E10` member (`HD-19`) and `ONBOARDING.md` says of itself that
it is not one, so neither fix is a layer amendment.

### `L-5` (low) — the construction-executor prompt sends a cold executor after a counterpart that does not exist

`CONSTRUCTION_EXECUTOR_PROMPT` (`dispatch.py:798`, and the golden at
`tooling/tests/fixtures/expected-construction-executor-prompt.txt`):

> *your standing instructions are `document-harness/CONSTRUCTION-CHECKLIST.md` … read it, **and
> the counterpart it names**, before anything else.*

`grep -i counterpart document-harness/CONSTRUCTION-CHECKLIST.md` returns **nothing**. The
phrase is inherited from `CONSTRUCTION_PROMPT` and `READ_PROMPT`, where it resolves: those
point at `migration/document-work-assurance-v3/v3-harness-review-contract.md`, whose stub says
in as many words *It is your standing instruction and its own counterpart; read all of it.*
Pointing the new mode straight at the checklist keeps the phrase and loses its referent.

This is not cosmetic for the role being dispatched. A cold construction executor obeying the
sentence looks for a counterpart in the checklist and finds two candidates: the retired
contracts at `7011916`, a commit this repository does not have (the checklist says so at its
own `:14`–`:19`), and `EXECUTION.md` / `REVIEW.md`, named there as the documents that govern
**product** runs — i.e. the other side's charter, which `dispatch.py:772`–`:775` records as the
incident both constants exist to prevent.

**Minimum fix,** exact bytes: drop `, and the counterpart it names` from the constant and from
the golden fixture, leaving *read it before anything else* — the form `EXECUTOR_PROMPT` already
uses. The whole-document golden equality means the fixture must move with it, which is the
shape working correctly.

## 6. Observations

**`O-1` — the product executor mode has no mount test, and it is the mode that will run
mounted.** `ConstructionExecutorDispatchGeneratesToo` gains
`test_a_caller_that_mounts_the_instrument_gets_the_path_through_the_mount`, for the mode that
runs inside this repository. `ExecutorDispatchesGenerateToo` has no equivalent, and the product
mode is the one dispatched from the caller, where the instrument *is* a submodule mount. I
verified the behaviour myself (§4.1) and it is correct, so this is coverage, not a defect.
`TheCharterIsNamedWhereTheReviewerCanOpenIt` pins `instrument_relative` generically, which is
why nothing broke.

**`O-2` — `E4`'s disclosure covers four of the round's new bindings; there are seven.** The
commit names M1–M4 (two goldens, the marker split, the drift comparison) and describes them as
*all four new bindings*. `RUN-OUTSIDE-REPO`, `INSTRUCTION-MISSING` and `INSTRUCTION-UNFROZEN`
are three further guards `E4` reads as new. I mutated all seven plus two constants and all nine
died on their own named test, so **the code is fine and the gap is in the account**. Recorded
because `E4`'s value is precisely that the account can be checked.

**`O-3` — an empty mode value falls through the `elif` chain into the product-review branch.**
`dtw dispatch --executor "" --repo-root .` prints a *review* refusal naming `None` as the
subject, because `getattr(args, "executor", None)` is falsy for `""` and the chain ends at
`else: dispatch_of(repo_root, args.subject)` with `args.subject is None`. `--read ""` and
`--subject ""` do the same, so the class predates this round; it is now reachable through two
more flags. No dispatcher hits this by accident, and `E6` argues against a guard for it —
recorded because the round touched the chain.

**`O-4` — `--executor` now means two different things on two subcommands.** On
`dtw dispatch` it is a run **directory** (`cli.py:593`); on `dtw review` it is the executor's
**identity string** (`cli.py:636`). Separate argparse namespaces, so nothing collides in code;
a human dispatcher gets no warning from either.

**`O-5` — three closeout carriers are outstanding, and one of them is now a second copy.** On
the `HD-51`/`HD-52` precedents (`39e395e`, `f084db4`) decision-log entries are created at
closeout, so the candidate not writing them is correct. What is owed:
(a) a `HARNESS-DECISIONS.md` entry for the ruling admitting the two executor modes — the plan's
§*Change surface* names it, with `HD-47` and `HD-51` as precedents;
(b) an entry for the C4 `O-1` reading-moment ruling (see `O-6`);
(c) `CONSTRUCTION-LEDGER.md`'s open-items line for the `ORCHESTRATOR-CHARTER` round's question
① (construction executor charter carrier), which this round answers, and its **conversation-only
C4 `O-1` row**, whose admission criterion is *层内确无别家* — no other home in the layer. That
criterion stopped holding at `EXECUTION.md:276`, and until the row moves, the same clause is
written out twice in two files, which is the `HD-5` drift surface `ORCHESTRATION.md:13` cites.

**`O-6` — the C4 `O-1` reading-moment ruling is chat-only, and it is load-bearing (`R2`).**
The plan's §*Open question* states it **unanswered**, lists three options (name a reading
moment, retire it now, leave it untouched) and says *The answer changes this round's shape*.
The candidate acts on the first option and adds a standing obligation to an `E10` member on its
authority. Nothing in the repository records the answer. Per `R7` I state the ceiling and move
on; per `R2` I record it as a finding. It is closed by `O-5`(b).

**`O-7` — the `E10` independent read for the two member edits is owed, and its trigger is
nameable.** The commit records the debt and cites the `PREVIEW-RENDER` precedent, matching
`HD-45:259`'s form. Worth naming because `E10`'s *may be relied upon before its read* clause
does **not** cover this round: the `EXECUTION.md` edit replaces a rule and changes what it
requires. No round has relied on it yet — *authoring, citing or recording it alone is not*
reliance — so nothing is violated. The moment it binds is the **first product-run instruction
written under the new authoring rule**, and the read is owed before then.

## 7. Honesty ceilings

- **My independence is not structural, and the round says so.** `229f03f`'s `E1` disclosure
  states that orchestrator and executor were one work-side session holding all four of `R1`'s
  holdings, and does not claim structural independence — the `HD-46` middle-state form, matching
  `15a53fe`'s wording, which the plan told the round to copy. I confirmed my own prompt was the
  generator's output verbatim plus two transport sentences, and I ran cold and re-derived
  everything in this record. That is a discipline, not a structure, and I do not certify it as
  more. The literal-reading tension in `E1`'s three tiers is the open rider
  `one-session-roles` ①, not a new defect of this round.
- **`UNVERIFIABLE`: that `71f7567` landed the reader's record unchanged.** `R1`'s *reported
  through* holding cannot be checked from inside the repository — I have the committed text and
  no independent copy of what was returned.
- **`UNVERIFIABLE`: `E11`'s preview card and the user's approval of it.** Chat-side. The
  ceiling is narrower than usual here (see §1), but the card itself I cannot see.
- **`774 passed` at the base is arithmetic, not a measurement.** I measured `790` at the tip and
  counted 16 new test methods by hand in the diff, with no test removed. I did not check out
  `693b692`, so I did not run the battery there.
- **The five-run count in `L-1` was measured in a different repository.** The caller at
  `D:/Thesis-stage-control-refactor` is machine-local and outside my subject; I read it and
  wrote nothing to it. A reviewer on another machine cannot reproduce that measurement, and the
  plan's own committed statement of *five* is the reproducible half.
- **Mutation proves binding force, not sufficiency.** Nine mutations dying says the new tests
  have force against the shapes I aimed at. It does not say the shapes I aimed at are all the
  shapes that matter.
- **`R5` observed, not concluded:** whether the round's answer to *who hands the executor its
  charter* should also have re-homed the standing obligations that arrive with it (`L-2`,
  `L-3`) is a question about what should exist, and it is the user's. I have reported the shape
  and stopped.

---

*Record written into the worktree per `R6`; not committed. Worktree clean at close
(`git status --porcelain` empty before this file was written); both mutated modules restored
and their sha256 verified identical to their pre-mutation values.*
