# Cold read — the instruction layer at `7701f03`

`E10` read. Not a round: no verdict, no budget spent (`R3`). Findings are tiered
must-fix / low / observation, and their routing is `E10` / `R9` / `R10`'s, not mine.

**Dispatch as received.** One SHA — `7701f03091a606bcee98340d708b5005745b6031` — plus the
characterization "the instruction layer … (an E10 read)" and a pointer to the standing
contract. Under `R2` the characterization is unverified until re-derived, and the repository
states it independently: the freeze marker names this SHA as the dispatched subject, and one
member's blob changed after the last recorded end-to-end read of the layer (§1). Nothing
below rests on the chat text. The member set comes from `E10`'s own sentence read at the
subject blob, never from a list I was handed. Every member's blob id is stated, because
`E10`'s citation route for the next read depends on it.

**Standing instructions read.**
`ResearchSystem/migration/document-work-assurance-v3/v3-harness-review-contract.md` (the stub)
→ `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` in full, both sides, per the
stub's "It is your standing instruction and its own counterpart; read all of it".
`ResearchSystem/HARNESS-DECISIONS.md` `§live` read in full as `E10`'s tail requires (HD-48,
HD-47, HD-44, HD-41, HD-36, HD-35, HD-34, HD-23, HD-9), plus the file header; from
`§implemented`, `HD-46` and `HD-2` by grep, because two claims I checked cite them.

## 1. Subject, re-derived

```
$ git rev-parse --show-toplevel
D:/Thesis-stage-control-refactor/ResearchSystem/harness

$ git rev-parse HEAD
7701f03091a606bcee98340d708b5005745b6031

$ git status --porcelain --untracked-files=all
(no output)

$ git log --oneline 7701f03..HEAD
(no output)
```

Subject = branch tip, worktree clean and with no untracked file, so blob = working-tree file
for every member; quotations that carry weight were still taken from the object store. That
status was true when the command ran and is falsified by exactly one path from the moment this
file was written — the record itself, which is untracked until the orchestrator commits it.

```
$ cat .harness/review-pending.json
{
 "subject": "7701f03091a606bcee98340d708b5005745b6031",
 "dispatched_at": "2026-08-19T05:37:48+00:00"
}
```

The marker's subject equals the dispatched SHA, so `E9`'s window opened at that timestamp and
closes when this record's commit lands. `git log 7701f03..HEAD` is empty — the branch has
taken no commit since dispatch, and the window held. `R4` ceiling: I re-derived that the
window held; I did not verify that any mechanism *made* it hold, and in this repository
none does (rider `self-caller-guards`).

**Why this read is owed.** The layer changed after the last recorded end-to-end read of it
(`v3-cold-read-c22e229.md`):

```
$ git diff --stat c22e229 7701f03 -- ResearchSystem/document-harness ResearchSystem/contract \
    ResearchSystem/schema/document-assurance-v3 \
    ResearchSystem/migration/document-work-assurance-v3/v3-harness-operating-contract.md \
    ResearchSystem/migration/document-work-assurance-v3/v3-harness-review-contract.md
 ResearchSystem/document-harness/ONBOARDING.md | 176 +++++++++++++++++++++
 ResearchSystem/document-harness/README.md     |   4 +-
 (ONBOARDING.md is not a member — §4)
```

The member change is `README.md` at `2026a14` (`V3-CALLER-ONBOARDING-v1`), two lines. That
commit's body records both `E10` deferral facts — the edit adds no clause and changes what no
rule requires, and its effect on every round in flight is nil — and states that "the bytes
ride the next read of this layer". **This is that read**, and those two lines get the closest
attention below.

## 2. The member set, and each member's blob

The set is `E10`'s own enumeration at the subject blob — "exactly these ten paths and nothing
else". All ten read in full at this subject; none by citation.

| # | member | blob at `7701f03` | lines | vs `c22e229` |
|---|---|---|---|---|
| 1 | `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` | `87add4cef021153e465aaf30ff0c674dc19b6a0b` | 212 | unchanged |
| 2 | `ResearchSystem/document-harness/README.md` | `fd9765d3256a1a8bfc6f529d14651c8724627d4a` | 38 | **changed** (`2026a14`) |
| 3 | `ResearchSystem/document-harness/EXECUTION.md` | `4a7b6eca3e8f4fd43c2887005c44a5e616d8b5da` | 465 | unchanged |
| 4 | `ResearchSystem/document-harness/REVIEW.md` | `3350bfac1b190cb1dac8566247f5382a7136f094` | 284 | unchanged |
| 5 | `ResearchSystem/document-harness/ORCHESTRATION.md` | `82f10c1bd173fb795c723df072a6357287d4d366` | 95 | unchanged |
| 6 | `ResearchSystem/migration/document-work-assurance-v3/v3-harness-operating-contract.md` | `17ff31bba177689bf22144603cecba533b5a4087` | 5 | unchanged |
| 7 | `ResearchSystem/migration/document-work-assurance-v3/v3-harness-review-contract.md` | `b576a45e142015e128f4ab9d1461667f991aa046` | 5 | unchanged |
| 8 | `ResearchSystem/contract/Document-Work-Assurance-Contract-v3-supersession-1.md` | `68031fa2ca31272e31da0d42a9a02189d28fcc21` | 124 | unchanged |
| 9 | `ResearchSystem/contract/Document-Work-Assurance-Contract-v3-supersession-2.md` | `e1a2f26b1d8d323d11e900f8137dea222b6571c1` | 113 | unchanged |
| 10 | `ResearchSystem/schema/document-assurance-v3/paragraph-map.schema.json` | `09aa869962f592c2f86c9379be0ef3eb7d2232ff` | 44 | unchanged |

Blob ids from `git ls-tree -r -l 7701f03 -- <the ten>`; the `c22e229` column is that record's
own blob table. Nine of the ten were citable and were read anyway, so this record may be cited
for any of the ten by the next read.

**`E2`'s frozen surface, checked rather than assumed.** Two of the three named blobs are
members 8 and 9 above; the third, the signed contract, matched exactly:

```
$ git ls-tree -r 7701f03 -- ResearchSystem/contract/Document-Work-Assurance-Contract-v3.md
100644 blob b2dbdf752d8c155e4c65b14b5f420b880b8184a1  …/Document-Work-Assurance-Contract-v3.md

$ git ls-tree 7701f03 ResearchSystem/schema/document-assurance-v3/ --name-only | wc -l
15

$ git log --format="%h %ad %s" --date=short -- ResearchSystem/schema/document-assurance-v3/ \
    ResearchSystem/contract/Document-Work-Assurance-Contract-v3*.md
345acdd 2026-08-15 initial: the v3 document-work assurance harness, extracted
```

Fifteen pack files, which is the count `E2`'s parenthesis states, and the whole frozen surface
is byte-untouched since this repository's first commit. No `E2` write occurred.

## 3. What I re-derived by command

**3.1 The membership sentence's three mirrors agree.** `E10`'s ten paths,
`layer_path_check.LAYER` (:30–41) and `test_precommit_checks.LayerMembership.EXPECTED`
(:164–175) are the same ten paths in the same order, compared by hand and then mechanically:

```
$ python -m pytest -q tests/document_harness/test_readme_enumeration.py \
    tests/document_harness/test_precommit_checks.py      # run from ResearchSystem/tooling
44 passed in 12.35s
```

`E10-sync`'s three named sites are in sync at this subject. Its *unnamed* sites are `L-2`.

**3.2 The README's schema enumeration is current**, pinned by the same suite: 15 schema files,
15 stems named across the README's four schema rows.

**3.3 The contract fixtures reproduce the README's figure.**

```
$ python validate_fixtures.py       # migration/document-work-assurance-v3/N0/fixtures
41/41 cases behaved as declared; failures=0
```

README :33 says "41/41 green" — re-run, not accepted.

**3.4 The README's rewritten Local-enforcement row is true in every checkable clause.** This
is the round's member edit, so each clause was taken separately:

```
$ git ls-tree 7701f03 .githooks/pre-commit
100755 blob 521e707be370d7fbbdbca491344686be42917cf5  .githooks/pre-commit

$ git log --format="%h %ad %s" --date=short -- .githooks/pre-commit
4029b43 2026-08-19 V3-CALLER-ONBOARDING-FIX-v1
2026a14 2026-08-19 V3-CALLER-ONBOARDING-v1

$ git config --get core.hooksPath
.githooks
```

- *"The third, instruction-layer path resolution, runs here"* — the tracked hook exists, calls
  `layer_path_check.py` and nothing else, and is mode `100755`, so a POSIX checkout would run
  it (the mode defect `ONBOARDING.md` :128 records against itself was repaired at `4029b43`).
- *"re-homed to this repository … on 2026-08-19"* — both commits touching the file are that
  day.
- *"where the ten do resolve"* — all ten paths resolve from this root (`git ls-tree` above
  returned all ten).
- *"the `git config core.hooksPath` that makes git run it does not [travel]"* — config, not
  tracked; set in this checkout, which is why the round's own commits were hook-checked.
- *"since 2026-08-17 it calls **two** of them, not three"* (caller side) — the caller's
  `.githooks/pre-commit` :61–62 loops over exactly `review_freeze_check.py` and
  `candidate_path_check.py`. Scope of this one clause: the caller worktree on this machine at
  this moment, not a repository property.
- *"The onboarding procedure a new caller follows states that per-machine step"* —
  `ONBOARDING.md` :128 states `git config core.hooksPath .githooks` as the per-machine half.
  The row does not name that file; see `L-3`.

**3.5 `EXECUTION.md`'s per-repository battery enumeration still partitions correctly.** None
of the five caller-side scripts exists here:

```
$ git ls-tree -r 7701f03 --name-only -- ResearchSystem/tooling/tests/run_tests.py \
    ResearchSystem/tooling/tests/run_p4_tests.py ResearchSystem/tooling/tests/run_p5a_tests.py \
    ResearchSystem/schema/fixtures/validate_fixtures.py ResearchSystem/tooling/rsc.py
(no output)
```

and the instrument's single leg's subject is present. The section's own instruction — re-run
the battery rather than trusting a written figure (`HD-41` ③) — is why I report no total here.

**3.6 `ORCHESTRATION.md`'s arithmetic and its nine citations hold.** Nine rows in the
already-law table, three sections written out, twelve total — which is what the README's
Role-instructions row says. Each cited rule was opened: `E9` carries both the budget and the
review-window sentence; `R6` carries the record title; `R10` carries the pre-closeout low
choice; `R5` carries the routing; `HD-2` (`§implemented`) carries the state-flip invariant.
`dtw dispatch` has exactly three modes (`--subject`, `--read`, construction range) and none
dispatches an executor, so *"none of them dispatches an executor"* holds; `dtw` is now seven
operations (`cli.py` :4) under `HD-47`, and no member states a command count.

**3.7 Outbound references from the layer, measured whole rather than sampled.** Scope: all ten
members at this subject, every markdown link target and every backtick path token.

```
$ python -X utf8 -c "<resolve every ]( … ) target in the 9 markdown members>"
BROKEN ResearchSystem/document-harness/README.md:16 -> ../../.goals/plans/document-work-assurance-harness-v3.plan.md
BROKEN ResearchSystem/document-harness/README.md:37 -> ../../.goals/plans/general-harness-v2-architecture-revision.plan.md
BROKEN ResearchSystem/document-harness/REVIEW.md:45 -> ../migration/document-work-assurance-v3/v3-review-full-fef3a2e.md
broken links: 3

$ python -X utf8 -c "<layer_path_check.unresolved_tokens over ALL lines of all ten members>"
EXECUTION.md:186  ResearchSystem/assurance/runs/p5a-shells/control/audit-rounds.md
EXECUTION.md:343  ResearchSystem/tooling/tests/run_tests.py
EXECUTION.md:345  ResearchSystem/tooling/tests/run_p4_tests.py
EXECUTION.md:346  ResearchSystem/tooling/tests/run_p5a_tests.py
EXECUTION.md:347  ResearchSystem/schema/fixtures/validate_fixtures.py
EXECUTION.md:449  ResearchSystem/assurance/runs/p5a-shells/control/audit-rounds.md
EXECUTION.md:452  ResearchSystem/assurance/runs/p4-doc/issues/user-decision-triage-comparator-environment-defects.json
supersession-1:89  schema/document-assurance-v3/review.v2.schema.json   -- prefix missing
supersession-2:83  schema/                                              -- prefix missing
total unresolved backtick tokens: 9
```

Every one of these is already banked and none is re-reported: the three links plus
`EXECUTION.md` :186/:449/:452 are `layer-outbound-refs`; the four battery scripts are
`layer-crossrepo-token` (deadline arrived, `HD-48` ①); the two prefix-missing tokens inside
`E2`-frozen bytes are `frozen-path-prefix`. The corroboration is the point — the bank's
enumeration reproduces under an independent measurement, with one counting ambiguity noted at
`O-2`.

## 4. `ONBOARDING.md`: the membership question was asked and answered

`E10`'s closing clause requires the round that creates such a file to record the question and
its answer. It is recorded in three places — the file's own header, the round journal
`journal/caller-onboarding-2026-08-19.md` §1, and the candidate commit body — and answered
**no**, on three grounds I checked rather than accepted:

1. The membership sentence does not name it, and the sentence is untouched (§2, §3.1).
2. It claims authority over no rule: every obligation it states cites an owner elsewhere, and
   it states that the cited rule governs on disagreement. I read its Owner column; the claim
   holds.
3. `io-design.md` and `split-travel-manifest.md` sit in the same directory on the same
   footing, so proximity has never been membership here.

The obligation is discharged. One record-side note about how it was cited is `O-3`.

## 5. Findings

**must-fix: 0.** Nothing in the layer at this subject is wrong in a way that may not wait.

### `L-1` (low) — member 7 names the wrong site as the reason its path is kept

`ResearchSystem/migration/document-work-assurance-v3/v3-harness-review-contract.md` :5 reads:

> Path kept: the construction dispatch fixture
> (`ResearchSystem/tooling/tests/fixtures/expected-construction-prompt.txt`) hard-codes this
> path; historical records point here too.

The fixture does **not** hard-code the path. Its charter line is `` `{charter}` `` — a
substitution — and `test_dispatch.py` :400–408 renders it with the test's own hand-written
constant, which is `E5` behaving exactly as intended. The path is actually pinned at
`rsclib/document_harness/dispatch.py` :545 (`CONSTRUCTION_ROLE_INSTRUCTION`) and,
independently of the module, at `test_dispatch.py` :398 / :520 (`CHARTER_OUTSIDE`) and :463
(`MEMBER`).

*Downstream decision that goes wrong* (so this is not `R9` wording-level): a batch asking
whether this stub path is still pinned checks the site the member names, finds a placeholder,
and concludes nothing pins it.

*Class swept, not the instance patched* (`E7`, `HD-36` ①, `HD-41` ④). Scope: all ten members
at this subject.

```
$ git grep -n -I -E -i "hard-code|hardcode|pins this path|Path kept" 7701f03 -- <the ten members>
…/v3-harness-operating-contract.md:5:> Path kept: historical records point here.
…/v3-harness-review-contract.md:5:> Path kept: the construction dispatch fixture (…) hard-codes this path; …
```

Two sites, one defective: the operating-contract stub makes no site claim, so the class has
exactly one instance and it is the one below.

*Minimum fix — exact bytes.* Replace that line with:

> Path kept: `dispatch.CONSTRUCTION_ROLE_INSTRUCTION`
> (`ResearchSystem/tooling/rsclib/document_harness/dispatch.py`) hard-codes this path, and
> `ResearchSystem/tooling/tests/document_harness_review/test_dispatch.py`'s hand-written
> `CHARTER_OUTSIDE` / `MEMBER` constants pin it independently (`E5`); the construction dispatch
> fixture carries `{charter}` as a substitution, not the path. Historical records point here
> too.

*Route.* Bytes supplied, no clause added, no bound changed, and this stub is **not** on `E2`'s
frozen surface — so `E10`'s free channel is open, subject to its own condition that no round
has yet relied on the sentence. Both replacement tokens resolve from this repository's root,
so the newly wired `layer_path_check` passes on the added line (checked).

### `L-2` (low) — the membership count's prose leg tripled this round; `E10-sync` still names three sites

`E10-sync` exists because the membership list lives in three places and only two of them
assert each other, leaving the prose leg unguarded. Its check-item names three sites plus one
caller-side fourth. Measured scope: `git grep -n -I -E "(ten|nine|eleven) (members|paths)"`
over all tracked files at `7701f03`, excluding `ResearchSystem/migration/` (review records)
and `document-harness/journal/` (journals). Live count-bearing sites, beyond the three named:

| site | new this round? |
|---|---|
| `ResearchSystem/document-harness/README.md` :34 — "It guards this layer's ten members" (**a member**) | no |
| `ResearchSystem/document-harness/ONBOARDING.md` :130 — "the repository whose ten members it names" | yes |
| `.githooks/pre-commit` :14 and :15 — "the instruction layer's ten members" / "Those ten members live here" | yes |
| root `README.md` :33 and :50 — "the instruction layer's ten members" | yes (rows rewritten) |

(`HARNESS-DECISIONS.md` :174 also carries the count, as a quotation inside the `HD-46` record;
records are not sync sites and it is excluded.)

*Downstream decision that goes wrong*: the next membership change follows `E10-sync`, updates
the three named sites, names three in the commit body — and leaves an instruction-layer member
and four other live files stating the wrong count, which is precisely the silent-prose-drift
the rider was opened for. The rider's own mutation evidence is that nothing goes red.

*Minimum fix*: extend `E10-sync`'s check-item to name these sites. That is a rider-bank row
edit, not a layer edit — no rule changes — so it is the bank's own to absorb rather than a
round's.

### `L-3` (low) — the layer refers to the onboarding procedure without naming it

README :34's new sentence, *"The onboarding procedure a new caller follows states that
per-machine step for its own side"*, is true (§3.4) but names no file. No member mentions
`ONBOARDING.md` at all:

```
$ grep -n "ONBOARDING" <the five document-harness members>
(no output)
```

*Downstream decision that goes wrong*: a reader who reaches the layer first — which is the
path `README.md` is written for — cannot get from this sentence to the procedure, and the
`Authoritative documents` table has no row for it either. This is thinner than `L-1`/`L-2`;
it is reported at low rather than observation only because the sentence was written this round
as part of the round whose subject was onboarding.

*Route*: naming the file supplies bytes and adds no clause, so the free channel is open — but
the fuller question, whether the table should gain a row (as it has for `io-design`'s
neighbours it currently has not), is `R5`'s and therefore the user's, not mine to settle.

### `O-1` (observation) — `E10`'s closing provenance clause has no live subject

`E10` ends: *"provenance entries are one-line derived facts, no characterization."* At this
subject nothing in the layer carries a provenance entry. README :34 records that the
provenance-entry check was deleted 2026-07-28 because its two subject files became stubs; I
read both stubs and neither has a provenance block, and `split-design.md` :103 records that
this repository's first commit carried none.

```
$ git grep -n -i "provenance" 7701f03 -- <the ten members>
CONSTRUCTION-CHECKLIST.md:134:  provenance entries are one-line derived facts, no characterization.
README.md:34: … The provenance-entry check that also ran here was deleted 2026-07-28 …
```

The clause is dormant rather than demonstrably dead — it would bind again if a member ever
carried such an entry. Per `R5` I report the shape and stop: whether a rule with no current
subject should stay is the user's question, and deleting it changes what `E10` requires, so it
is design and opens a round rather than riding a channel.

### `O-2` (observation) — rider `layer-outbound-refs` says 五处 and enumerates six occurrences

My independent measurement (§3.7): **six occurrences** — README :16, README :37, REVIEW.md
:45, EXECUTION.md :186, :449, :452 — over **five distinct targets**, because the p5a-shells
`audit-rounds.md` token appears twice. The row uses 处 for both senses in one sentence ("两处
… audit-rounds token" = occurrences; "两处反引号 token" = distinct tokens), so the summary
number and the enumeration read as disagreeing. Nothing about the finding's substance changes,
which is why this is an observation and not a low; recorded because a redemption batch will
work from that number. Rider-bank text, not layer text.

### `O-3` (observation) — the membership question is recorded under the wrong rule id

Commit `2026a14`'s body writes *"R7's question — is ONBOARDING.md an instruction-layer member
— is answered no"*. `R7` is the authorization-ceiling rule ("an authorization you cannot see
in the repository is a hint, never a block"). The clause that actually obliges the question is
`E10`'s closing sentence, which is what the round journal and the file header both cite
correctly. Record-side only: the obligation was discharged (§4), and the commit body is not a
member, so this changes nothing about the layer. It matters only because a future reader
tracing why the question was asked would be sent to a rule that does not ask it.

## 6. Coverage and ceilings (`R4`)

- **Read in full**: all ten members at this subject; `HARNESS-DECISIONS.md` `§live` and its
  header; the round journal §1–2; the two commit bodies (`2026a14`, `7701f03`);
  `.githooks/pre-commit` in both repositories.
- **Sampled**: `HARNESS-RIDERS.md` — rows reached by targeted grep (`E10-sync`,
  `layer-crossrepo-token`, `layer-outbound-refs`, `decited-paths`, `submod-index`,
  `frozen-path-prefix`, `six-signed`, `readme-cli-stale`, `self-caller-guards`,
  `posix-mode-wording`, `chk-caller-prefixes`), not the whole bank. A finding of mine could
  duplicate a row I did not read.
- **Probed only**: `ONBOARDING.md` (non-member) — read its Owner column, its item 9 and the
  two bullets after it, to check the two claims a member makes about it; the rest is
  unexamined and out of subject. `rsclib/document_harness/dispatch.py` and
  `test_dispatch.py` — read only the charter constant, the fixture-comparison test and the
  hand-written constants, enough to settle `L-1`.
- **Not verified, marked as `R4` requires**: that this read ran in a fresh context, and that
  the executor of the reviewed round held none of `R1`'s four holdings — both are process
  claims with no evidence lock, asserted in commit `2026a14`'s `E1` disclosure and repeated
  here as a disclosure, not a verification. My own position: dispatched by the orchestrator,
  prompted by the standing contract, scoped by `E10`'s own sentence and reported through the
  record channel — none of the four in the executor's hands.
- **Out of subject by construction**: everything the round changed outside the ten members
  (`ONBOARDING.md`, `init_target.py`, `cli.py`, the tests, the root README, the caller's half
  of the closeout). Those were the FULL's and the VERIFY's subject, not this read's.
- **Measure-last** (`E3`): the worktree-state and range commands in §1 were the last commands
  run before this file was written, and every figure quoted above is pasted from the command
  that produced it.
