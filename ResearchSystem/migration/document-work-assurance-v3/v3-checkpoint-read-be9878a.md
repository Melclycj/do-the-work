# Instruction-layer read — `be9878af283b0bc70492d6583f1a727d8b32aeab`

`E10` read of the instruction layer at `be9878a`. Not a round: no verdict, no budget consumed
(`R3`). Its subject is the amendment text itself — batch B R4's re-pointing of the rule text at
the three-role model — not the work that text governs, and it is not banked as anyone's FULL.

**Findings: 1 must-fix, 3 low, 1 wording-level, 2 observations.** The re-pointing is faithful to
the signed design at every one of the eleven sites, and both facts it newly writes into
instruction text reproduce under command. The must-fix is on the sentence the round rewrote to
close rider `R10-route`: its new "One exception" claims the `E10` free channel has exactly one
override, while `E10` states two more — including the design test that rider `F-1r` was
redeemed to install. Routing by `R10` alone now licenses an immediate instruction-layer write
where `E10` requires a round.

## 1. Subject, re-derived (`R2`)

Handed one SHA and the phrase *an E10 read*. Member set, blobs, figures and obligations are
re-derived here; nothing is taken from the dispatch prompt, the commit body, the ledger or the
rider bank.

```
$ git rev-parse HEAD          -> be9878af283b0bc70492d6583f1a727d8b32aeab
$ git status --porcelain      -> (empty)
$ git rev-parse be9878af…     -> be9878af283b0bc70492d6583f1a727d8b32aeab
$ cat .harness/review-pending.json
  {"subject": "be9878af283b0bc70492d6583f1a727d8b32aeab",
   "dispatched_at": "2026-08-13T03:28:28+00:00"}
```

HEAD **equals** the subject and the tree is clean, so worktree reads are reads of subject bytes,
and the branch has taken no commit since dispatch — this record is the first it admits (`E9`).
Dispatch (03:28:28Z = 13:28:28+10:00) post-dates the commit (13:28:12+10:00) by 16 seconds.

`E10`'s sentence **at the subject blob** governs the member set: nine paths, closing with "and
nothing else", so the set is decidable by reading it. The sentence is byte-unchanged in this
commit (the diff touches `E10` only at its free-channel clause), and it is still item-for-item
equal to `layer_path_check.LAYER` and to `test_precommit_checks.py`'s hand-written `EXPECTED`.

| # | blob at `be9878a` | lines | member | how it is covered here |
|---|---|---|---|---|
| 1 | `0602bc6c` | 193 | `document-harness/CONSTRUCTION-CHECKLIST.md` | **changed** (`44d622b9` → here) — **read end to end**; also this session's standing instructions |
| 2 | `54dfef83` | 38 | `document-harness/README.md` | unchanged here but changed at `c7e0ba0` (R3) and never independently read at this blob — **read end to end** |
| 3 | `85198e8f` | 421 | `document-harness/EXECUTION.md` | **changed** (`8bbd330f` → here) — **read end to end** |
| 4 | `3350bfac` | 284 | `document-harness/REVIEW.md` | unchanged — end-to-end read at `v3-checkpoint-read-a5a04c3.md` §1; §*Independence* re-read here |
| 5 | `17ff31bb` | 5 | `migration/…/v3-harness-operating-contract.md` (stub) | **read end to end** (5 lines is cheaper than the citation) |
| 6 | `52a97a48` | 5 | `migration/…/v3-harness-review-contract.md` (stub) | **read end to end** — the dispatch entry point |
| 7 | `68031fa2` | 124 | `contract/…-v3-supersession-1.md` | unchanged — `a5a04c3` §1 |
| 8 | `e1a2f26b` | 113 | `contract/…-v3-supersession-2.md` | unchanged — `a5a04c3` §1 |
| 9 | `09aa8699` | 44 | `schema/document-assurance-v3/paragraph-map.schema.json` | unchanged — `a5a04c3` §1 |

Blob ids from `git ls-tree be9878af`, line counts `wc -l` on `git show` at the subject. The
three cited rows are blob-equal to the table in `v3-checkpoint-read-a5a04c3.md` §1, whose text
states **all nine were read end to end there regardless of citation eligibility**; equality was
re-derived from `git ls-tree` here, not read off that record. Members 4–9 are therefore covered
by a single citation, not a chain.

`ResearchSystem/HARNESS-DECISIONS.md` `§live` read in full (lines 1–142): ten entries — `HD-35`,
`HD-28`, `HD-33`, `HD-34`, `HD-27`, `HD-24`, `HD-23`, `HD-10`, `HD-15`, `HD-9`. `HD-20`, which
`R10` now cites inline, sits in `§implemented` (in force, detail carried elsewhere) — and after
this round the detail is carried by `R10`'s own sentence, which is what that state means.

## 2. The amendment against its signed source (`E3`)

The round re-points at `document-harness/io-design.md`. At the subject that file is blob
`8f3c82c2` / sha256 `730fddf4…8157` — **exactly** the bytes `HD-35`'s re-signature binds
(`git show be9878af:… | sha256sum`). So the re-pointing rests on signed bytes, and the fidelity
check below is against the signed revision, read in full (128 lines).

io-design §8 lists five re-point items for R4. All five landed, and nothing else moved:

| §8 item | landed at | faithful? |
|---|---|---|
| "Execution side" section-head scope | checklist `:19` | yes — the head now binds a session "whether it orchestrates the round or executes it", which is what makes every `E` rule reach the orchestrator role §2 introduces |
| `E1` subagent sentence (in direct conflict with *reviewer 可为 subagent*) | checklist `:21-25` | yes — keys on the dispatcher, not the process form; §2's reviewer row is now textually supported |
| `R1`/`R6`/`R10` appellations | `:137-139`, `:189`, `:173` | yes — "the orchestrator commits it" and "the orchestrator weighs" match §3 obligations ⑥ and ⑨; `E9` carries no such appellation and is correctly untouched |
| `R10` "never here" re-pointed | `:160` | yes — "belong to HarnessIssue or to the caller's own rider bank, never this one" is what `HD-33` (每库用自己的四件) requires once two repositories exist |
| WorkSpec inside the round | `EXECUTION.md` `:6-9`, `:114-118` | yes — "the executor of this run, decomposing the instruction it was handed … before the START card" is §4's chain verbatim in substance, and the "what changed is who decomposes, not when" note matches §4's own caveat |

Sweep for sites the list would have missed: `execution side` now occurs exactly once in the
whole layer (the section head, as the side's name); no member says "the executor commits"; and
`REVIEW.md` §*Independence is decided by who sets the question* (`:49-56`) states a
**disqualifying configuration**, not a sufficiency claim, so it needed no re-point and has not
gone stale.

Every figure in the commit body reproduces on the subject tree, re-run here immediately before
writing: `--numstat` gives 23/12 (checklist), 27/10 (`EXECUTION.md`), 1/2 (`HARNESS-RIDERS.md`);
parent blobs `44d622b9` / `8bbd330f` / `8f9c0a02`; line counts 182→193, 404→421, 34→33; three
files in the commit, all markdown, zero code delta.

## 3. Facts newly written into instruction text — measured

`E3` binds a factual assertion written into instruction text to the command that could falsify
it. Two are new here; both hold.

**The eight-command battery enumeration** (`EXECUTION.md` `:328-340`). All eight resolve at the
subject (`git cat-file -e` on each of the seven paths; the eighth is the same `rsc.py` with a
subcommand). The count is eight. `tests/run_tests.py`'s own docstring opens *"ResearchSystem P2
golden tests"*, so the "(P2 goldens *only*, per its own docstring)" qualifier is the docstring's
own claim, not an inference. The "under-ran twice" clause is carried by records, not by the
executor's word: `v3-review-full-c7e0ba0.md` `B-1` establishes the R3 under-run ("five commands
ran, and three of the legs … green" against a body claiming six), and the R1 instance is that
same finding's correction of `e9166d2`.

**The repository-root collection abort** (`EXECUTION.md` `:333-334`). Measured, not described:

```
$ python -m pytest -q --collect-only            # from the repository root
ERROR collecting ExperimentLab/papers/guardagent/replication/smoke_test.py
import file mismatch: imported module 'replication.smoke_test' has this __file__ attribute:
  D:\Thesis-stage-control-refactor\ExperimentLab\papers\agentspec\replication\smoke_test.py
!!!!! Interrupted: 1 error during collection !!!!!
701 tests collected, 1 error in 1.00s
```

Two same-named `smoke_test.py` under `ExperimentLab/papers/`, exactly as the sentence says, and
the abort is real rather than a slowdown. The scope qualifier the sentence adds is load-bearing.

## 4. What the amendment may have falsified elsewhere — swept

- **The pins that could bind on these bytes are green.** `python -m pytest -q
  tests/document_harness/test_precommit_checks.py tests/document_harness/test_readme_enumeration.py`
  from `ResearchSystem/tooling` → `43 passed in 15.81s`. `test_readme_enumeration.py` exists and
  does read `document-harness/README.md`, so the tiering exception's first example is real (a
  grep for its content string finds nothing — the string lives in the filename; checked twice).
- **No code depends on the changed bytes.** The only code-side references to the two changed
  members are path enumerations (`layer_path_check.LAYER`, the hand-written `EXPECTED`) and
  fixture strings in `test_instruction_form.py` / `test_transcript_audit.py` — none reads the
  files. The role-distinctness checks in `rsclib/document_harness/` are auditor/executor
  (`instruction.py:599`) and reviewer/executor (`review.py:690`, `review_result_v2.py:270`);
  there is no spec-author/executor distinctness, so moving WorkSpec authoring onto the executor
  breaks no check. It does leave three prose carriers pointing the other way — finding `L-3`.
- **Path tokens across the whole layer.** Running `layer_path_check.unresolved_tokens` over the
  *full* text of all nine members (the shipped guard scans only staged added lines) returns the
  same four pre-existing missing-prefix tokens the `d58969d` read recorded — the review stub's
  `tooling/tests/fixtures/expected-construction-prompt.txt`, supersession-1's
  `schema/document-assurance-v3/review.v2.schema.json`, supersession-2's `assurance/runs/` and
  `schema/` — and nothing new. Confirmation of a recorded residual under its recorded
  disposition ("un-repaired until a batch writes those tokens anew"), not a finding; three of
  the four sit in `E2`-frozen bytes and would bank regardless.

## 5. Process boundary — second (`R3`)

- `E10`: this amendment changes what rules require, so opening a round is right, and the
  independent read is owed before any round relies on the text. No commit follows the subject,
  so nothing has relied on it: the read lands ahead of the deadline, not after it.
- `E9`: from dispatch to this record the branch takes no commit but the record itself —
  satisfied at the moment of writing (HEAD is still the subject). A read spends no leg.
- `E8`: single dense title `V3-B-R4-v1`, one paragraph, no trailers, kind named ("amendment
  (instruction layer)"), three declared paths.
- **Tier.** The batch ran the four batch-specific checks and not the eight-command battery. I
  cannot re-derive those four from a clean tree — both hooks read the *staged* diff — so their
  exit codes stay an executor claim (`R4`). What I could test instead is whether the tier choice
  hid anything: the two test modules that bind on these files pass, and `HD-22` has already
  ruled that the membership mirror gets no machine, so nothing mechanical was skipped. The
  *text*, though, does not say what the round did — finding `L-2`.
- Rider bank conformance: `R10-route` deleted in the same commit that fixed it, which is the
  redemption rule; `tier-scope` re-scoped rather than deleted because item ② is unpaid, with its
  self-carried deadline intact — the `HD-22`/`HD-27` precedent for re-scoping. Both rows name a
  target and a redeem-when.

## 6. Findings

### Must-fix

**`M-1` — `R10`'s "One exception" contradicts the `E10` channel it routes into, and the
contradiction points at an unauthorized write.**

*Location.* `CONSTRUCTION-CHECKLIST.md` `0602bc6c` `:161-167` (`R10`'s routing sentence) against
`:106-112` (`E10`'s free channel).

*Ground truth.* `R10` now reads: "the `E10` free channel takes **any** finding whose record
supplies the exact bytes or names the content, and the bank takes what is left. **One
exception**, and it overrides the free channel: bytes on a path `E2` also freezes bank …".
`E10`, at the same blob, states two further conditions on that channel: it "holds for as long as
no round has relied on the text — once one has, changing it opens a round"; and "when the free
channel and the design test both apply — the named literal replacement itself adds a clause or a
bound — **design wins and the round opens**". The second is not incidental: rider `F-1r` existed
precisely because that seam was undecided, and it was redeemed at `feacb86` by installing that
clause. `R10`'s new sentence asserts exhaustiveness where the old one merely omitted it, so this
round replaced one summary-vs-channel conflict (`HD-20`, correctly closed) with another.

*What goes wrong.* An orchestrator routing a finding by `R10` — the sentence written to be the
route — applies design-shaped supplied bytes "immediately, instruction layer included" when
`E10` requires a round with its preview card and user approval. That is a rule change landing
with no round, and the free channel's reversibility does not undo the reliance in between.

*Minimum fix* (two literal replacements; both point at conditions that already bind, so neither
adds a rule):

- `:164-165` — "the `E10` free channel takes any finding whose record supplies the exact bytes
  or names the content" → "the `E10` free channel takes, **on the conditions stated there**, any
  finding whose record supplies the exact bytes or names the content".
- `:165` — "One exception, and it overrides the free channel:" → "One exception **beyond those
  conditions**, and it overrides the channel:".

### Low

**`L-1` — `E1` states orchestrator dispatch as sufficient for independence; `R1` states it as
holding when the executor holds none of four.** `E1` `:21-25`: "a reviewer the orchestrator
dispatches under the standing review contract is independent whether it runs as a subagent or as
its own session." `R1` `:136-139`: the disqualifying configuration is "dispatched by, prompted
by, scoped by **and** reported through the executor", and independence is structural "with the
executor holding none of the four". The mixed configuration — orchestrator dispatches, executor
drafts the prompt or the scope — takes "independent" from `E1` and no answer from `R1`. The
decision that goes wrong is whether that review carries a verdict and whether it spent the
round's review leg (`E9`). This is **not** the four-conjunction question the commit body
discloses as deliberately unopened (whether one of four should disqualify); it is the new
sentence's sufficiency claim, which io-design §2 supports as written ("前提是 dispatch 由
orchestrator 发") but which the layer now carries beside a conjunctive test. Bytes deliberately
not supplied: any qualifier adds a bound, so it is design (`E10`). Redeem-when: the next batch
touching `E1`'s subagent sentence or `R1`; **deadline = the first round that dispatches a
reviewer as a subagent**, the moment the mixed case can exist.

**`L-2` — the tiering exception is written file-wise and was applied clause-wise, and the text
says nothing about the difference.** `EXECUTION.md` `:324-327`: "a doc file that code enumerates
or tests pin (… the layer-path mirror, `layer_path_check.py`) is tooling-load-bearing — treat
the batch as tooling-touching." Both members edited this round are enumerated in
`layer_path_check.LAYER` and in `test_precommit_checks.py`'s `EXPECTED`, so the sentence as
written puts this batch in the tooling-touching tier and its own eight-command battery. The
round took doc-only on the narrower reading that what is enumerated is the *path*, and the paths
did not change — a reading that appears nowhere in the text. The narrow reading is substantively
right (I ran the two binding pins: 43 passed; and `HD-22` already rules the mirror gets no
machine), which is what makes the gap a text defect rather than a verification defect. The
decision that goes wrong: the next construction batch self-classifying its tier off this
sentence gets one answer from the text and the opposite from two rounds of precedent (`838c413`,
this one). No bytes — a qualifier either way is a bound. Redeem-when: the next batch touching
the tiering section; **deadline = the next doc-only construction batch that touches a layer file
code enumerates**.

**`L-3` — the WorkSpec re-point leaves three carriers naming the superseded reading, and all
three are frozen or signed.** `EXECUTION.md` `:6-9` / `:114-118` now make the executor the
WorkSpec author and call the stage-author reading "pre-`HD-35` history". Still live elsewhere:
the signed contract §3 interface-ownership table — "`DocumentWorkSpec` | stage author / planning
agent" (`Document-Work-Assurance-Contract-v3.md:62`, blob `b2dbdf75`, the contract `E2` freezes)
— and the titles of both `document-work-spec.schema.json` and `document-work-spec.v2.schema.json`
("sole owner: stage author / planning agent"), inside the `E2`-frozen pack. The charitable
reading holds and I verified it: "stage author" is a role label whose carrier `HD-35` reassigns,
the contract's V3-D5 prohibition list does not include the WorkSpec, and no code compares a spec
author to the executor. But nothing in the layer says any of that. The decision that goes wrong:
a reviewer comparing a run's declared spec author against a table that says **sole owner** reads
a role-separation violation and has three signed or frozen instruments behind them. No bytes:
the disclosure sentence is design, and the other three carriers are `E2`-frozen, so their bytes
bank until that ruling exists — which is `R10`'s one stated exception working exactly as
written. **Deadline = the first run whose WorkSpec is authored under the new model.**

### Wording-level (`R9` — no actor's action changes)

**`W-1` — "says so at its own head" is off by one sentence.** `EXECUTION.md` `:13-14` says the
exception section "says so at its own head"; the heading line reads "## Regression-battery
tiering (2026-08-03 ruling — this section is the revert unit)", and what says it binds the
construction side is the sentence immediately after it. No downstream decision changes — the
fact is recoverable from the adjacent line. Bytes supplied: "and says so at its own head" → "and
says so in its own opening sentence".

### Observations (`R5` — reported; the conclusions are the user's)

**`O-1` — the rewritten route is ordered, and `R9` still overlaps the free channel.** `R10`'s
new sentence removed the tier and the producer as route keys, which was its job. What remains is
that a wording-level finding whose record supplies bytes satisfies both "R9 takes wording-level"
and "the free channel takes any finding whose record supplies the exact bytes" — `W-1` above is
an instance. The two differ only in *when* (rides the next batch vs applied immediately), never
in what, so nothing is wrong; it is simply the one place where the route still depends on which
clause is read first.

**`O-2` — `E1`'s routing sentence is written for a two-role world and now binds three.** With
the section head extended to the orchestrator, `E1`'s "a request that belongs to the other role
is flagged for the user to route, never absorbed" binds a session whose own obligation (io-design
§3 ②) is to start the executor and hand it the instruction. "The other role" is singular where
there are now two others, and routing to the executor is the orchestrator's job rather than
something it flags. In practice `E11`'s card keeps the user in the loop either way, which is why
this is an observation and not a finding.

## 7. Coverage disclosure (`R4`)

- **Read in full:** members 1, 2, 3, 5, 6 at the subject blobs (193 + 38 + 421 + 5 + 5 lines);
  `document-harness/io-design.md` (128, signature-verified); `HARNESS-DECISIONS.md` §live
  (lines 1–142); `HARNESS-RIDERS.md` (33).
- **Covered by citation** (blob-equal to a recorded end-to-end read, equality re-derived here):
  members 4, 7, 8, 9 via `v3-checkpoint-read-a5a04c3.md` §1. Member 4 was additionally re-read
  at §*Independence* and grepped for role appellations; members 7–9 were not opened here.
- **Probed, not read:** `Document-Work-Assurance-Contract-v3.md` (§2–§3 block only);
  the two work-spec schemas (title lines); `v3-review-full-c7e0ba0.md`, `-e9166d2.md`,
  `v3-checkpoint-read-d58969d.md`, `-3f19561.md` (targeted greps); the tooling tree by grep plus
  the two test modules actually executed.
- **Marked, not verified:** that this read ran in fresh context (`R4` — a process claim); that
  the four batch-specific checks exited 0 before the commit (not re-derivable post-commit from a
  clean tree — both hooks read the staged diff); that no *earlier* round relied on the amended
  text (established only by there being no commit after the subject).
- Mutation testing does not apply — the round's delta is prose, and the guards that touch these
  paths were not changed. The two modules I ran prove the pins still hold at these bytes, not
  that their force is sufficient.
