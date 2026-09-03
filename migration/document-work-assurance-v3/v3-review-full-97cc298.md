# FULL review — `b9710af..97cc298` (round `PROMISE-PATH-VOCAB`, batch `PROMISE-PATH`)

**Verdict: `CHANGES_REQUIRED`** — two blockers (`B-1`, `B-2`), three lows, three observations.

Both blockers sit in the round's own headline commit `97cc298`, and neither is in the branch it
built. The branch itself is right: I drove it end to end through the real engine and it does
what four rule sites promise. What is wrong is the two things that were added *beside* it — the
companion guard, whose predicate is wider than the thing it means to catch and now refuses the
harness's ordinary success path; and the new state pointer, which is written with a digest that
nothing in this repository ever reads, in the batch whose item 5 exists because a digest nobody
checks certifies nothing. Item 2 (the `UNRESOLVED_BLOCKER` vocabulary) is clean at every site I
could find, the announced-path disclosure is complete and mechanically confirmed, the guards I
mutation-tested all bind, and the battery is green at 951 / 0.

> Subject received as a range and nothing else (`R2`). Round, budget, authorization, boundary
> and every figure below were re-derived from this repository; no reported figure was accepted,
> and where a claim is reproduced the reproduction is what is stated. Two reported figures were
> re-run and matched; one was re-run and did not (`O-1`).
>
> Written by the reviewer and **not committed by it** — `R6`, and now `REVIEW.md`'s *Where the
> result lives* as this round's own `61afc26` rewrote it. `.harness/review-pending.json` is
> deliberately left in place; the commit that lands this file is what deletes it.
>
> **One artifact, not two.** `REVIEW.md` names a ReviewResult beside the record, written to a
> control root the caller holds. A construction round has no control root, no WorkSpec and no
> obligation list, so there is nothing for that document to be schema-valid against and nothing
> to bind it to; round 1's FULL (`09daa7e`, `v3-review-full-38038ec.md`) returned the record
> alone and this follows it. The absence is stated rather than passed over.

## 1. Subject, re-derived

```
$ git rev-list --count b9710af..97cc298
4
$ git rev-parse b9710af 97cc298
b9710afaca8fa260ff43b3d1c6f582cd49b69201
97cc2981532320ddc6de7db43839752619f2d96b
$ git diff --numstat b9710af..97cc298 | awk '{a+=$1;d+=$2;n++} END {print n" files, +"a" -"d}'
21 files, +913 -68
```

Oldest first, kind taken from each commit's own body (`E8`):

| # | sha | title | kind |
|---|-----|-------|------|
| 1 | `61afc26` | `V3-PROMISE-PATH-VOCAB-RECORD-COMMIT-OWNER-v1` | candidate — rider `record-commit-owner` |
| 2 | `b8a2183` | `V3-PROMISE-PATH-VOCAB-RESUME-1-RULINGS-v1` | ruling record (orchestrator) |
| 3 | `15e5ccc` | `V3-PROMISE-PATH-VOCAB-UNRESOLVED-BLOCKER-v1` | candidate — item 2 |
| 4 | `97cc298` | `V3-PROMISE-PATH-VOCAB-LIMITATIONS-PATH-v1` | candidate — item 1 + rider `no-repair-unbound` |

**Paths classified by hand** (`R2`), from `git diff --name-status b9710af 97cc298` — 21 files,
every one `M`, nothing added and nothing deleted:

- **Announced (`E2`)** — 4: `contract/Document-Work-Assurance-Contract-v4.md` ·
  `schema/document-assurance-v3/review.v2.schema.json` ·
  `schema/document-assurance-v3/user-decision.schema.json` ·
  `schema/document-assurance-v3/assurance-work-state.schema.json`.
- **Instruction layer, `E10` members** — 2: `document-harness/RULES.md` (`R3`) ·
  `document-harness/REVIEW.md` (verdict table + the new `UNRESOLVED_BLOCKER` paragraph +
  *Where the result lives*).
- **Engine — `tooling/rsclib/document_harness/`** — 4: `flow.py` · `review_result_v2.py` ·
  `summary.py` · `assurance_state.py` · plus `dispatch.py` (5).
- **Run template** — 1: `assurance/templates/run-v2/run_bind_v2.py`.
- **Tests — `tooling/tests/document_harness_review/`** — 5: `test_disposition_reachability.py` ·
  `test_flow_repair_disposition.py` · `test_golden_review_views.py` ·
  `test_review_v2_subject.py` · `test_run_v2_template_bind.py`.
- **Registers and records** — 4: `CONTRACT-V4-SIGNATURE.md` · `HARNESS-RIDERS.md` ·
  `document-harness/plans/promise-path.plan.md` · `document-harness/journal/promise-path-vocab-2026-09-03.md`.

**Freeze window re-derived, not assumed** (`REVIEW.md` says the hook is advisory and
per-machine). The marker names exactly the dispatched range:

```
$ cat .harness/review-pending.json
{ "subject": "b9710afaca8fa260ff43b3d1c6f582cd49b69201..97cc2981532320ddc6de7db43839752619f2d96b",
  "dispatched_at": "2026-09-03T03:18:45+00:00" }
$ git log -1 --format='%h %cI' HEAD
f0143c8 2026-09-03T13:16:55+10:00     # = 03:16:55Z, ~2 min BEFORE the marker
$ git status --porcelain
?? .goals/
```

The branch tip `f0143c8` is one commit ahead of the dispatched tip and landed **before** the
dispatch, as its own body says it would; nothing has landed since, and the worktree is
byte-identical to `97cc298` over `tooling/ schema/ assurance/ contract/`
(`git diff --name-only 97cc298 -- tooling/ schema/ assurance/ contract/` → empty), which is
what lets every measurement below be taken in the worktree.

**Authorization, read out of the repository.** Round 2 of batch `PROMISE-PATH`, opened
2026-09-03 at `2db6d87`; `E9` budget untouched at dispatch (no FULL has occurred on this round),
so all four commits are candidate work and consume nothing. The authorising texts are plan
`document-harness/plans/promise-path.plan.md` rulings 1, 2, 4, 6 (2026-09-01), 7–9 (the `E11`
card), and 10–11 (the executor's first stop, carried inside the subject at `b8a2183`), plus
`HARNESS-DECISIONS.md` `§live` `HD-70` — twelve `§live` entries, which is what ruling 9 predicted.
`HD-70` authorises contract `:118` and nothing else; ruling 11 adds contract `:127-128` and
`schema/document-assurance-v3/user-decision.schema.json:44`; ruling 7 adds `REVIEW.md`'s *Where
the result lives* and "whatever state or candidate field carries the decision's digest".

## 2. The blockers

### `B-1` — the companion guard refuses an ordinary successful repair

**Where**: `tooling/rsclib/document_harness/summary.py:401-425` (`check_summary`, the new
`V3-ASSURANCE-ACCEPTED-OVER-BLOCKER`), added by `97cc298`.

**What it violates**: its own stated scope, and with it the harness's ordinary terminal path.
The block's comment says the case it catches was *structural* until this round — "no
AssuranceCandidate could exist over a standing blocker, so no summary could accept one, and
nothing had to say this" — and the round's commit body repeats it. That is false. The predicate
is `candidate["unresolved_finding_ids"]` being non-empty, and that field is **not** "a blocker
that stands": `run_bind_v2.unresolved_ids` (`:152-167`) is the union of blocking findings over
*every* bound review, and says so — "the controller has no vocabulary for 'repaired' — whether a
repair worked is the reviewer's judgment, carried by the VERIFY, not a controller edit to the
FULL's claim". So the ordinary successful repair — FULL `CHANGES_REQUIRED` naming a blocker, the
user approves the repair, the targeted VERIFY returns `REVIEWED_NO_BLOCKER` — produces a
candidate carrying that closed finding, and its FINAL `ACCEPT` is now refused.

**Reproduced end to end through the real engine**, not argued. Driving `run_bind_v2.main`
itself over a round-1 run whose VERIFY is clean:

```
bind exit: 0 | state: AWAITING_FINAL
unresolved_finding_ids: ['f-changelog']
[promoted / ACCEPT]                   issues= ['V3-ASSURANCE-ACCEPTED-OVER-BLOCKER']
[promoted / ACCEPT_WITH_LIMITATIONS]  issues= []
[not promoted / ACCEPT]               issues= ['V3-ASSURANCE-ACCEPTED-OVER-BLOCKER']
[not promoted / ACCEPT_WITH_LIMITATIONS] issues= []
```

The bind is clean, the promotion is legitimate, the reviewer said no blocker stands, and the
user's `ACCEPT` is the correct FINAL — and the summary that terminates the run cannot be
generated. The only way to close such a run now is `ACCEPT_WITH_LIMITATIONS` naming a limitation
that is not open, which is the controller pushing a false claim onto the user's decision.

**That the new code is what refuses it**, established by neutering only that block and re-running
the same probe (scratchpad copy sha256 `ab3613c3…`, restore verified byte-identical):

```
WITH the new guard   : RESULT: ['V3-ASSURANCE-ACCEPTED-OVER-BLOCKER']
guard NEUTERED       : RESULT: []
```

**Why the round's own tests do not see it.** `test_flow_repair_disposition.py:1489-1527` pairs
`make_candidate(unresolved_finding_ids=["f-changelog"])` against `make_candidate()` and reads the
first as "a standing blocker" and the second as "nothing stands". Both controls assert the
*intent*; neither constructs the population the predicate actually meets — a candidate whose
`unresolved_finding_ids` came from a blocker the repair closed. `E7`'s shape, from the other
side: the test pins the reported instance, not the class the predicate covers.

**Minimum fix.** The guard must fire only when a blocker *stands at the end of the round*. The
fact that says so is the operative review's verdict — `UNRESOLVED_BLOCKER`, this round's own new
value, or equivalently `flow.BLOCKER_AFTER_VERIFY`, which is exactly what item 1's branch keys on
in `run_bind_v2.py:381`. `check_summary(summary, candidate, decision)` does not receive it;
`check_assurance_candidate(candidate, record, reviews)` beside it does. So the minimum fix is to
give the guard that fact — the reviews the sibling already takes, or the standing-blocker
condition item 1's branch already computes — rather than inferring a standing blocker from
`unresolved_finding_ids`. Narrowing `unresolved_ids` instead would change what
`check_assurance_candidate` enforces about the reviewer's claim and is a larger change than this
finding needs.

### `B-2` — the new licence pointer is verified by nothing, in the batch about unverified digests

**Where**: `tooling/rsclib/document_harness/assurance_state.py:48-63` (`POINTER_FIELDS`, not
amended) against `:81-96` (`DIGEST_PROTECTED_FIELDS`, amended) and
`schema/document-assurance-v3/assurance-work-state.schema.json:36-39`, all in `97cc298`; second
site `tooling/rsclib/document_harness/review_subject.py:293-297`.

**What it violates**: two universals the code states about itself, and the redemption the commit
claims. `POINTER_FIELDS` is documented as "Every pointer-shaped field on the state, in the order
the flow reaches them" and `bind_authorization_ref` is not in it. It is the tuple both readers
iterate: `assurance_state.resume` (`:257-300`) checks each pointer's target exists and its digest
matches, and `ResumePoint.render` (`:228-252`) is what prints them. `review_subject.py:293-294`
says "Every remaining pointer the state carries must also resolve inside the commit — the subject
is the whole control plane, not the three documents this module joins", and its field list omits
the same name. So the field is written **with** a digest (`pointer_for` honours
`DIGEST_PROTECTED_FIELDS`) that nothing in this repository ever reads.

**Reproduced, both sites, each with a negative control** — the same bogus pointer (nonexistent
path, all-zero digest) on the new field and on `final_decision_ref`:

```
# assurance_state.resume
check_state           : []
check_state_pointers  : []
resume issues         : []
rendered names bind_authorization_ref? False
negative control (final_decision_ref bogus) -> ['V3-STATE-POINTER-MISSING']

# review_subject.read_control_plane
bind_authorization_ref     -> issues: NONE (clean)
final_decision_ref         -> issues: ['V3-SUBJECT-POINTER-MISSING']
```

The second site is the one that makes this a blocker rather than a low: `read_control_plane` is
how an independent reviewer derives a run's control plane out of the evidence commit, it declares
its own coverage to be the whole control plane, and it now silently skips a digest-protected
user-decision pointer.

**Against what the round claims for it.** Rider `no-repair-unbound`, deleted in this same commit
under `R10`, states the defect as "no digest of it reaches the state or the candidate, and …a
later reader of an `AWAITING_FINAL` state cannot **verify** which decision unlocked it". The
pointer now reaches the state; the verification does not exist, the resume view does not print
it, and the row that recorded the debt is gone. The commit body invokes "a digest nobody checks
certifies nothing" twice — item 5 of this very batch — and the new field is a fresh instance of
it.

**Minimum fix.** Add `"bind_authorization_ref"` to `assurance_state.POINTER_FIELDS` (between
`assurance_candidate_ref` and `final_decision_ref`, matching `flow._EARLIEST_POINTER`) and to
`review_subject.py:294-296`'s field tuple. I ran the first half as a control: with the name added
to `POINTER_FIELDS`, `tooling/tests/document_harness_review/` + `test_spec_plan_state.py` stay at
**566 passed** — nothing pins the omission, and nothing breaks when it is closed. The stale count
in the two docstrings rides the same fix (`L-2`).

## 3. What holds — the implementation, led with

**Item 2 — the vocabulary — is clean at every site I could find.** I re-ran the class scan
myself rather than reading the executor's, over the whole tracked tree at `97cc298` excluding
`migration/`, `document-harness/journal/`, `document-harness/plans/` and both archives. Eight
VERIFY-row sites, all eight carrying the new value: contract `:118`, `REVIEW.md:130`,
`RULES.md:192`, `review.v2.schema.json:68`, `dispatch.py:191`, and the golden-view and
reachability suites' three. The FULL row is untouched at three everywhere. The two READMEs'
mermaid line is a FULL return and the VERIFY leg one line below reads `verified once` and
enumerates nothing — measured, not accepted: `README.md:76` / `README.zh-CN.md:73` against
`README.md:79`. The ordinal deletion is at both sibling sites ruling 11 named and nowhere else.

**The schema change is shaped right, and the FULL narrowing it had to add is load-bearing.** The
root enum is now the union of the two rounds, so a root-only constraint would have let a FULL
return the VERIFY-only value. Removing that narrowing (added this round) turns **6 tests red**.

**The branch works.** `test_disposition_reachability.Reachers.accept_with_limitations_after_a_blocking_verify`
drives the real bind twice, the real candidate gate, the real summary generator and the real
terminal check, with only the user's decision as a fixture. I re-ran it and read it; the route
the batch exists for is genuinely reached.

**Guards mutation-tested independently** (`R8`/`E4`). Eight probes, each neutered, run, and
restored from a sha256-checked scratchpad copy with the restore digest re-verified — never
`git checkout --`:

| probe | result |
|---|---|
| mixed-issue refusal removed (`run_bind_v2.py:382`) | RED |
| `ACCEPTED-OVER-BLOCKER` guard neutered | RED |
| FINAL decision need not bind THIS digest | RED |
| FINAL decision need not be phase FINAL | RED |
| FULL verdict narrowing (added this round) removed | RED (6 tests) |
| `UNRESOLVED-BLOCKER-NAMES-NONE` neutered | RED |
| `bind_authorization_ref` dropped from `flow._EARLIEST_POINTER` | RED |
| **control**: `bind_authorization_ref` **added** to `POINTER_FIELDS` (`B-2`'s fix) | GREEN |

Every must-fire probe fired. The last row is a control for `B-2` and is the only reason it is
stated as safe.

**Announced-path disclosure is complete, and mechanically confirmed** rather than read:

```
$ python tooling/announced_path_disclosure.py --before b9710af --after 97cc298
announced-path disclosure: range b9710af..97cc298
  floor 1d4d9aa1f6b1daca3fbf1a7765985abaec350b18; 4 non-merge commit(s) judged
  every announced path changed in this range is named by the commit that changed it
```

Four announced paths written, each named site by site in its own commit body, and the
announced-set arithmetic in `15e5ccc`'s body reproduces: `git ls-files
schema/document-assurance-v3/` → 15 files, of which `bind-declarations.schema.json` is not
announced and `review.schema.json` (announced) is absent, so fourteen announced pack files exist
plus the contract. `CONTRACT-V4-SIGNATURE.md` records the eighth post-signature write and does
not re-point the signed blob.

**`layer_path_check`'s class holds on the added member lines.** I extracted every backtick
path-shaped token on lines the range ADDS to the seven `E10` members plus this repository's
declared rule file, and resolved each from the repo root and from its own file's directory: one
token (`RULES.md` in `REVIEW.md`), resolves.

**The battery reproduces.** At the subject's exact bytes, immediately before this claim:

```
$ python -m pytest tooling/tests -q
951 passed in 179.09s
```

which is the executor's reported 951, independently reproduced. The intermediate figure
reproduces too: a detached worktree at `15e5ccc` gives `941 passed in 193.37s`, so item 2's three
added tests and item 1's ten are both real counts.

**`E1`, `E8`, `E9`, `E11`, `E12` conformance.** The `E1` statement for this round is inside the
subject (`b8a2183`, and the journal): two sessions in the norm, the executor holding none of
`R1`'s four holdings — a process claim, marked and not verified (`R4`). Every commit title is
`V3-PROMISE-PATH-VOCAB-<…>-v1` and every body names its kind. No FULL had occurred, so nothing
consumed the fix leg; the branch took no commit between dispatch and this record. The rider bank
moved 37 → 36 → 35 data rows across the range, and both redemptions deleted their row in the
commit carrying the fix, as `R10` requires; the touch record on `emit-reviewed-legality` is a
touch record and says so.

## 4. Lows

**`L-1` — a class-scan locator that resolves at no revision the scan declares.** `97cc298`'s
`HD-41` ④ section declares its scope as "the whole tracked tree at this commit's parent
`15e5ccc`" and cites `document-harness/REVIEW.md:215` as one of the four PROMISE sites left
byte-identical. Measured: at `15e5ccc` that sentence is at `:226`; `:215` is where it sat two
commits earlier at `61afc26`, and `:211` at both `b9710af` and `f5d9741`. The substantive claim
is true — I verified `EXECUTION.md` is untouched across the range and that the sentence's bytes
did not change. The decision that goes wrong: the next round re-running this scan against the
declared anchor lands on a different sentence and cannot tell whether a site moved or was missed.
No bytes supplied for in-place application — `HD-59` puts a committed conclusion beyond in-place
edit, so this is a forward correction if the user wants one.

**`L-2` — the protected-pointer set is six and three sites still say five.** `97cc298` added a
sixth member to `DIGEST_PROTECTED_FIELDS` and left the prose that counts it:
`tooling/rsclib/document_harness/assurance_state.py:68` ("Yes for these five"),
`tooling/rsclib/document_harness/review_subject.py:200` ("Those five name files whose current
version…") and `tooling/tests/document_harness/test_spec_plan_state.py:933` ("those five files
have no legitimate digest-less shape"). The round did update the one hand-written test that
enumerates the names (`test_review_v2_subject.py:369-376`, five → six), so this is the same edit
finished at three more sites. **Bytes**: `five` → `six` at each. (`review_subject.py:357`'s
"these five" is a different referent — error codes — and is correct.)

**`L-3` — three engine modules written outside the plan's declared "In" list, with the escape
never named.** The plan's *Change boundary* names `flow.py`, `review_result_v2.py`,
`assurance/templates/run-v2/`, `schema/document-assurance-v3/`, `tooling/tests/`, `RULES.md`,
`REVIEW.md:129-135` and contract `:118`. Written and not in it:
`tooling/rsclib/document_harness/summary.py`, `dispatch.py` and `assurance_state.py`. Each is
defensible — ruling 7 authorises "whatever state or candidate field carries the decision's
digest", ruling 2 authorises the vocabulary — and `97cc298` argues at length for the
`summary.py` guard. What is missing is the sentence saying the boundary was exceeded. `E9` makes
that explicit for a fix leg and the plan makes the boundary the round's; round 1's own FULL
raised this exact class as its `L-2` (`review.py` written outside the "In" list, escape never
named), so this is the second occurrence in two rounds. **Bytes**: none — the fix is a sentence
in a closeout record naming the three, or the plan's boundary line growing.

## 5. Observations (`R5` — routing is the user's, not mine)

**`O-1` — a reported figure that does not reproduce, outside the subject.** `f0143c8` (the
branch tip, one commit past the dispatched tip) and the journal note it carries record the
executor's figures, correctly marked as not yet reproduced: "battery 951, sixteen mutation
probes, riders table at **32 data rows** by id column". The battery reproduces exactly. The rider
count does not: counting the table body by its id column gives **37** at `b9710af`, **36** at
`61afc26`, **36** at `15e5ccc` and **35** at `97cc298`. `61afc26`'s in-subject claim of "leaving
36 rows" is right; the 32 is not, and it is the figure a later reader would use to check that two
redemptions and one banking landed. It sits outside the range I was given, which is why it is an
observation and not a low.

**`O-2` — the two-pass digest comparison rests on an operator-supplied date.** Pass 2 re-assembles
the candidate and promotes only if the FINAL decision binds that digest; the comment calls
deterministic assembly "what makes the comparison mean something". `bound_at` comes from
`--bound-at`, which `run_bind_v2.py:299` makes required and which the operator types. A pass 2 run
on a later day than pass 1 produces a different digest and refuses a perfectly valid
authorization, telling the user to "re-decide against the candidate in hand". It fails closed and
prints the remedy, and the round-0 `R10` two-pass path has carried the same dependency since round
1 — but this round is the first to make the digest comparison the gate on a user decision, so it
is worth someone's attention.

**`O-3` — the owed `E10` re-read is promised to a carrier this round does not schedule.** Three
commit bodies (`61afc26`, `15e5ccc`, and `HD-70` itself) say the changed `RULES.md` / `REVIEW.md`
/ contract text "owes `E10`'s independent re-read, riding this round's next read of that layer".
Round 2's only read was its opening one at step 2, before these bytes existed, and step 4 is
FULL → fix → VERIFY → closeout with no read in it; the batch then closes. The real carrier is the
*next* round's opening cold read, which covers a changed blob by definition — so nothing is lost,
but the phrase names a read this round will not perform. Same shape as rider
`r9-terminal-no-carrier`, one clause over.

## 6. Coverage — what I read in full, sampled, and only probed (`R4`)

**In full**: `document-harness/CONSTRUCTION-CHECKLIST.md`, `document-harness/RULES.md`,
`document-harness/REVIEW.md`, `harness.json`, `HARNESS-RIDERS.md`,
`CONSTRUCTION-LEDGER.md`'s current-pointer block, `document-harness/plans/promise-path.plan.md`,
`document-harness/journal/promise-path-vocab-2026-09-03.md`, all four commit bodies, and the
whole diff of the range for `tooling/rsclib/`, `schema/`, `contract/`,
`assurance/templates/run-v2/run_bind_v2.py`, `CONTRACT-V4-SIGNATURE.md`, `RULES.md` and
`REVIEW.md`.

**Sampled**: the five changed test files — I read every added test in
`test_disposition_reachability.py`, `test_review_v2_subject.py`, `test_golden_review_views.py` and
`test_flow_repair_disposition.py`, and read `test_run_v2_template_bind.py` by its added test names
plus the parts `B-1` and the mutation probes touched. `HARNESS-DECISIONS.md` was read at `§live`'s
`HD-70` in full and by heading elsewhere. The surrounding unchanged bodies of `summary.py`,
`flow.py` and `run_bind_v2.py` were read where the diff reaches them.

**Only probed**: everything else in `tooling/`, which the battery exercises and I did not read.

**Not verified, and named as such**: the round's `E1` statement is a process claim with no
evidence lock (`R4`); the executor's "sixteen mutation probes fired" is a process claim about
work done in a session I cannot inspect — I ran eight of my own instead of checking theirs, and
they are what §3's table reports. The intermediate battery count *was* re-run — in a detached
worktree at `15e5ccc`, `python -m pytest tooling/tests -q` → **941 passed in 193.37s**, matching
that commit's own body, which makes item 1's "+10 tests" real; the earlier `938` at `b8a2183` was
not re-run, and it is the figure round 1's VERIFY already reproduced.

**`residual_uncertainty`.** Three, and the list is a positive statement that I found no others:
(1) whether `B-1`'s right fix is the guard's predicate or `unresolved_ids`' semantics is a design
question I deliberately did not answer (`R5`); (2) I established `B-2` against `resume` and
`read_control_plane`, the two readers I could find by grep — whether a third consumer of state
pointers exists outside `tooling/` and `assurance/` I did not establish; (3) the caller-side
consequences of `B-1` — how many closed runs carry a candidate with a non-empty
`unresolved_finding_ids` — are not measurable from this repository, which holds no runs.
