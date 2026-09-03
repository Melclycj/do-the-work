# VERIFY review — `97cc298..d56def4` (round `PROMISE-PATH-VOCAB`, batch `PROMISE-PATH`)

**Verdict: `REVIEWED_NO_BLOCKER`.**

Both accepted blockers are closed, in the shape their findings named, and I established each by
driving the repaired code rather than by reading it: `B-1`'s ordinary repaired run now closes on
a bare `ACCEPT` while the standing-blocker case still fires, and `B-2`'s licence pointer is now
resolved and digest-verified by both readers that were blind to it. The accepted low is closed at
its three named sites and at a fourth the executor found and disclosed. The repair diff contains
nothing the findings did not ask for, no announced path was written, no `E10` member was touched,
the budget is conformant, and the battery reproduces at 956.

Two findings stand, neither blocking. The larger one is that `L-2`'s class was declared closed and
is not: the scan's pattern was narrower than the class it swept, and **four** sites still describe
the digest-protected set as five — two of them in the signed contract, where one is not a count at
all but an enumeration by name asserted to equal `assurance_state.DIGEST_PROTECTED_FIELDS`. It is
not a blocker: the text was falsified by `97cc298`, not by this repair; its failure mode is a loud
refusal rather than a false pass; and its remedy is a signed-text ruling in the `HD-63/64/67/68`
family, which the executor was forbidden to take inside the leg. It needs the user at closeout,
not a stopped run.

> Subject received as a range and nothing else (`R2`). Round, budget, authorization, the accepted
> finding set, the change boundary and every figure below were re-derived from this repository; no
> reported figure was accepted without re-running the command that produces it. Three reported
> figures were re-run and all three matched.
>
> **One artifact, not two.** `REVIEW.md` names a ReviewResult beside the record, written to a
> control root the caller holds. A construction round has no control root, no WorkSpec and no
> obligation list, so there is nothing for that document to be schema-valid against; round 1's
> VERIFY (`07da6b1`, `v3-review-verify-1f6a5a5.md`) returned the record alone and this follows it.
>
> Written by the reviewer and **not committed by it** (`R6`). `.harness/review-pending.json` is
> deliberately left in place; the commit that lands this file is what deletes it.

## 1. Subject, re-derived

```
$ git rev-list --no-merges --count 97cc298..d56def4
4
$ git rev-parse 97cc298 d56def4
97cc2981532320ddc6de7db43839752619f2d96b
d56def4fd7331b2dd1d1e621e5c46c8ab90435a1
$ git diff --numstat 97cc298 d56def4 | awk '{a+=$1;d+=$2;n++} END {print n" files, +"a" -"d}'
12 files, +645 -71
```

Oldest first, kind taken from each commit's own body (`E8`):

| # | sha | title | kind |
|---|-----|-------|------|
| 1 | `f0143c8` | `V3-PROMISE-PATH-VOCAB-EXECUTOR-DONE-v1` | record — orchestrator pointer move, no work product |
| 2 | `67dbb08` | `V3-REVIEW-RECORD-PROMISE-PATH-VOCAB-97cc298-v1` | record — the round's independent FULL |
| 3 | `06f0b4f` | `V3-PROMISE-PATH-VOCAB-FULL-DISPOSITION-v1` | ruling record, orchestrator |
| 4 | `d56def4` | `V3-PROMISE-PATH-VOCAB-FIX-v1` | review fix — the round's one user-approved repair |

**Paths classified by hand** (`R2`), from `git diff --name-status 97cc298 d56def4` — 12 files, one
`A` (the FULL record) and eleven `M`:

- **Announced (`E2`)** — **none**. Neither `contract/Document-Work-Assurance-Contract-v4.md` nor
  any file under `schema/document-assurance-v3/` appears in the range.
- **`E10` instruction-layer members, and this repository's own declared rule file** — **none**.
  `git diff --name-only` over all eight paths returns empty.
- **Engine — `tooling/rsclib/document_harness/`** — 3: `summary.py` · `assurance_state.py` ·
  `review_subject.py`.
- **Tests** — 4: `tooling/tests/document_harness/test_spec_plan_state.py` ·
  `tooling/tests/document_harness_review/{test_flow_repair_disposition,test_review_v2_subject,test_disposition_reachability}.py`.
- **Run template** — 1: `assurance/templates/run-v2/README.md` (prose only; no script changed).
- **Registers and records** — 4: `HARNESS-RIDERS.md` · `document-harness/plans/promise-path.plan.md` ·
  `document-harness/journal/promise-path-vocab-2026-09-03.md` ·
  `migration/document-work-assurance-v3/v3-review-full-97cc298.md`.

Only `d56def4` is the reviewed work product. The other three are records and a ruling; under `E9`'s
test and the 2026-08-04 ruling on ledger/riders-only fixes they consume nothing, and each says so in
its own body.

**Freeze window re-derived, not assumed** (`REVIEW.md`: the hook is advisory and per-machine). The
marker names exactly the range I was dispatched on, and the branch tip is the dispatched tip:

```
$ cat .harness/review-pending.json
{ "subject": "97cc2981532320ddc6de7db43839752619f2d96b..d56def4fd7331b2dd1d1e621e5c46c8ab90435a1",
  "dispatched_at": "2026-09-03T04:52:58+00:00" }
$ git log -1 --format='%h %cI' HEAD
d56def4 2026-09-03T14:51:39+10:00      # = 04:51:39Z, ~1 min BEFORE the marker
$ git status --porcelain
?? .goals/
```

Nothing landed inside the window; the worktree is byte-identical to `d56def4` over the tracked tree,
which is what lets every measurement below be taken in the worktree. `.goals/` is untracked and is
`Out` by the plan's change boundary.

**Authorization, read out of the repository.** Round 2 of batch `PROMISE-PATH`, opened 2026-09-03 at
`2db6d87`. The accepted set is **plan ruling 12** (`document-harness/plans/promise-path.plan.md`,
written by `06f0b4f`): leg **(ii) = B-1 + B-2 + L-2**, one user-approved fix obliging this VERIFY,
against the user's word "同意" of 2026-09-03. `B-2`'s fix carries, at the user's word, one class
assertion that `DIGEST_PROTECTED_FIELDS ⊆ POINTER_FIELDS`; option (i) was offered and not taken.
Off the leg and consuming nothing: `L-1` and `O-1` corrected forward in the journal, `L-3` answered
by the plan's *Change boundary* growing, `O-2` banked, `O-3` recorded. `HARNESS-DECISIONS.md`
`§live` holds twelve entries; `HD-41` (scope before assertion; class-scan evidence pasted into
commit bodies), `HD-59` (correct forward, never in place) and `HD-23` (journal numbers) are the ones
this round's work turns on, and `HD-70` authorises contract `:118` and nothing else.

## 2. The accepted findings, one at a time

### `B-1` — closed. Reproduced through the controller's own derivation, not argued

The record's minimum fix was to give the guard the standing-blocker **fact** — the operative
review's verdict — instead of inferring it from `unresolved_finding_ids`. That is what
`summary.py:289-294` and `:402-455` now do: a fourth parameter `reviews`, `operative = reviews[-1]`, and the
issue fires only on `UNRESOLVED_BLOCKER`.

The definition of *operative* is not invented for this guard — it is the template's own, which is
the only thing that makes the fix safe to rely on:

```
$ python -c "... run_bind_v2.main source ..."
run_bind_v2.main: ['operative = reviews[-1]']
```

Driving the real derivation and then the real check over one candidate, with the operative verdict
as the only difference:

```
1. run_bind_v2.unresolved_ids([FULL-with-blocker, VERIFY-clean]) = ['f-changelog']
   (the REPAIRED run's candidate carries the closed finding id — B-1's premise, reproduced)

2. check_summary over that same candidate:
   ACCEPT  | VERIFY REVIEWED_NO_BLOCKER (ordinary success) -> [] CLEAN
   ACCEPT  | VERIFY UNRESOLVED_BLOCKER  (blocker stands)   -> ['V3-ASSURANCE-ACCEPTED-OVER-BLOCKER']
   ACCEPT  | reviews OMITTED                               -> ['V3-ASSURANCE-STANDING-BLOCKER-UNVERIFIED']
   ACCEPT  | reviews EMPTY                                 -> ['V3-ASSURANCE-STANDING-BLOCKER-UNVERIFIED']
   AWL     | VERIFY UNRESOLVED_BLOCKER                     -> [] CLEAN
```

The first line is the one the finding was about, and it is the line the record's own reproduction
returned `ACCEPTED-OVER-BLOCKER` on. The harness's ordinary success now closes.

**The population the guard can no longer be wrong about**, established by mutation rather than by
reading (`E4`/`R8`). Each probe: neutered, run, restored from a sha256-checked scratchpad copy with
the restore digest re-verified — never `git checkout --`; the driver aborts if a restore does not
reproduce. Baseline green before each (`test_flow_repair_disposition.py` 141 passed).

| probe | expectation | result | test that answered |
|---|---|---|---|
| the old predicate restored (`elif True:` — fire whenever unresolved is non-empty) | RED | **RED** | `test_the_ordinary_repaired_run_closes_on_accept` |
| the guard never fires | RED | **RED** | `test_an_unqualified_accept_over_a_blocker_that_still_stands_is_refused` |
| absent reviews read as "nothing stands" (fail open) | RED | **RED** | `test_without_the_reviews_the_question_is_unverified_never_satisfied` |

The first probe is the direct evidence that the blocker is **closed rather than moved**: putting
`B-1`'s original defective predicate back turns the new negative control red, on the exact
population the old tests could not see. The old test pair is gone and four separated populations
stand in its place; that replacement is right, and `E7`'s shape is satisfied — the tests now
construct the population the predicate meets, not the intent it was written with.

**The one judgement inside the fix, and what it actually costs.** `reviews` defaults to absent and
absence is reported as `STANDING-BLOCKER-UNVERIFIED`, never as satisfied. I re-ran the executor's
measurement rather than accepting it:

```
$ git grep -n "check_summary" -- . ':!migration/'
  → tooling/rsclib/document_harness/summary.py:289 (definition), :517 (__all__), tests only;
    the two other hits are prose in a journal and a plan. No production caller in this repository.
```

So no shipped code path is broken by the loud default, and the first real caller — the caller's own
FINAL step, which this repository does not hold — is told loudly rather than quietly passed. That is
the right side to fail on and it is disclosed in the commit body. What it does not do is make the
ordinary success reachable for a caller that has not been updated: such a caller still cannot close
an `ACCEPT`, now under a different code. That consequence is real, is outside this repository, and is
recorded as `V-O-1` below rather than as a finding against the repair.

### `B-2` — closed at both sites. Each reproduced with its negative control

`bind_authorization_ref` is now in `assurance_state.POINTER_FIELDS` (`:60`, between
`assurance_candidate_ref` and `final_decision_ref`, matching `flow._EARLIEST_POINTER`) and in
`review_subject.read_control_plane`'s field tuple (`:296`, same position). Both readers walk their
list generically, so the fix is the whole mechanism and not a special case. Driven against the
repaired bytes, with the same bogus pointer (nonexistent path, all-zero digest) on the new field and
on `final_decision_ref` as the control:

```
# review_subject.read_control_plane — the half that made this a blocker
  bind_authorization_ref     -> ['V3-SUBJECT-POINTER-MISSING/bind_authorization_ref']
  final_decision_ref         -> ['V3-SUBJECT-POINTER-MISSING/final_decision_ref']

# assurance_state.resume + ResumePoint.render
  bind_authorization_ref     -> ['V3-STATE-POINTER-MISSING/bind_authorization_ref'] | render names it: True
  final_decision_ref         -> ['V3-STATE-POINTER-MISSING/final_decision_ref']     | render names it: True
```

The record measured all three of those as clean / `False` before the fix. The digest that certified
nothing now has two readers, so the rider `no-repair-unbound`, deleted at `97cc298` with its stated
defect still open, is honestly redeemed as of this commit.

**`flow._REQUIRED_POINTERS` is correctly not a sixth list.** I checked the claim rather than taking
it: `AWAITING_FINAL` requires `assurance_candidate_ref` only, so requiring the licence there would
refuse the clean path, on which no licence is owed. The five lists a state pointer must appear in
all carry it, at the lines the commit body names — `assurance-work-state.schema.json:36`,
`assurance_state.py:60` and `:92`, `flow.py:119`, `review_subject.py:296` — verified by
`git grep -n bind_authorization_ref -- schema/ tooling/rsclib/ assurance/templates/`.

**The class assertion binds, and it binds the class** (`E4`, same scratchpad discipline;
`test_review_v2_subject.py` 48 passed at baseline):

| probe | expectation | result |
|---|---|---|
| the licence pointer leaves `POINTER_FIELDS` (the reported instance) | RED | **RED** — `test_every_digest_protected_field_is_a_pointer_field` |
| a **different** protected field (`final_decision_ref`) leaves `POINTER_FIELDS` (the class) | RED | **RED** — same test |

Reading both sets from the module is not an `E5` lapse here, and the reasoning the docstring gives is
sound: the property is a **relation** between two sets, and hand-writing either side would pin the
one name this finding reported. `E5` still binds the membership question, and it is satisfied one
test below — `test_pointer_for_writes_a_digest_on_exactly_the_protected_fields` types out all six
names by hand and checks every other field carries the path alone. The pair is right.

**The measured residual is real, and I re-measured it rather than believing it.** The commit body
states that `review_subject.py`'s field tuple — the site that made `B-2` a blocker — is pinned by
nothing. Confirmed, against the whole battery:

```
probe: bind_authorization_ref removed from review_subject.read_control_plane's tuple
       $ python -m pytest tooling/tests -q  ->  956 passed in 189.54s     (GREEN — SILENT)
       restore sha256 a5fb91dd… == recorded
```

The code is correct and nothing holds it there. That is `V-2` below.

### `L-2` — closed at the three named sites and one more; the **class** is not closed

The record's bytes (`five` → `six`) are applied at all three sites it named —
`assurance_state.py:69`, `review_subject.py:200`, `test_spec_plan_state.py:933` — and
`review_subject.py:358` ("these five", error codes) is correctly left alone. The executor's own
`HD-41` ④ scan found a fourth, `assurance/templates/run-v2/README.md:77-81`, and fixed all three of
its clauses rather than the one word, on the ground that the sentence enumerates the set inline and
then states "only `review_ref` is written by these scripts", which this round falsified. That
judgement is right and the boundary question it raises is named in the commit body rather than taken
silently (`E9`), which is what that clause asks for.

The scan itself ran and its pasted output is accurate — I replayed the exact pattern at the exact
revision and got the same 9 hits. What is wrong is the pattern, not the paste: it cannot see the
same assertion written any other way, and four sites are. That is `V-1` below.

## 3. The whole repair diff — what else is in it

Nothing the findings did not ask for, with one file the body does not mention and one it does.

- `test_disposition_reachability.py:696` — the `ACCEPT_WITH_LIMITATIONS`-after-a-blocking-VERIFY
  reacher now passes `[full, verify]` to `check_summary`. Unmentioned in the body, and **forced**:
  the three-argument call would now return `STANDING-BLOCKER-UNVERIFIED` and the reacher asserts a
  clean report. It strengthens the batch's spine rather than weakening it — the reacher exercises the
  call a real caller must now make — and `tooling/tests/` is inside the plan's declared boundary, so
  no escape was taken and none had to be named.
- `assurance/templates/run-v2/README.md` — the disclosed fourth `L-2` site. The plan's `In` entry is
  `assurance/templates/run-v2/` **(both templates)**, and this file is neither template script, so
  the executor is right that it sits beside rather than inside the entry. It named the site, the
  reason and the ruling it read (`E7` + `HD-41` ④), and offered the judgement to be judged. I would
  have made the same call: leaving a false statement about the exact mechanism this round changed, in
  the file that teaches a caller how state pointers work, is the shape the scan exists to catch.
- No script under `assurance/templates/run-v2/` changed; no schema changed; no contract text changed.

The battery, at these exact bytes, immediately before this claim (`E3`):

```
$ python -m pytest tooling/tests -q
956 passed in 185.38s
```

which is the fix commit's reported 956, independently reproduced, and `+5` on the 951 the FULL
reproduced at `97cc298`. The per-file figures reproduce too — `test_flow_repair_disposition.py`
**141 passed**, `test_review_v2_subject.py` **48 passed**, against the body's 137 → 141 and 47 → 48.

## 4. The permanent boundaries

- **`E2`** — no announced path is in the range, so nothing was owed. Confirmed mechanically as well
  as by hand: `python tooling/announced_path_disclosure.py --before 97cc298 --after d56def4` → "every
  announced path changed in this range is named by the commit that changed it", 4 commits judged.
- **`E8`** — four commits, every title `V3-PROMISE-PATH-VOCAB-…-v1` or `R6`'s record form, every body
  naming its kind in its first words, no trailers, no amends, no push. `.goals/` untracked throughout
  and no unrelated path in any of the four file lists.
- **`E9`** — one FULL (record `67dbb08`), one user-approved fix (`d56def4`), one targeted VERIFY (this
  record). The FULL's dispatch window is clean: the branch tip at dispatch was `f0143c8` and the
  record's own parent is `f0143c8`, so no commit landed between dispatch and record. The disposition
  commit `06f0b4f` touches only the plan, the journal and the rider bank and consumes nothing. After
  this record the budget is spent in full.
- **`E10`** — no member touched, and no member's added lines to scan.
- **`E12`** — I received one range and nothing else.
- **`R10`** — the rider bank moved **35 → 36** rows by the id column, header and separator excluded
  (37 at `b9710af`, 36, 36, 35 at `97cc298`, 36 here), which reproduces the disposition commit's
  figure. The new row `bound-at-digest-gate` is well formed: it names its target file, its redeem-when
  is a touch condition plus a deadline, that deadline (the first product run whose pass 2 runs on a
  later day than its pass 1) falls outside this round, and because its fix is design it names a
  round-eligible surface rather than any batch.
- **Bookkeeping** — the plan's step 4 is correctly still unchecked; the pointer moves at closeout, not
  here. The journal's two forward corrections (`HD-59`) are accurate, and I re-measured both rather
  than reading them: the rider table holds **35** rows at `97cc298`, not the 32 `f0143c8`'s body
  reports; and `REVIEW.md`'s promise sentence sits at `:226` at `15e5ccc`, at `:215` at `61afc26`,
  exactly as the correction states. Both original bodies stand as written, which is what `HD-59`
  requires.

## 5. Findings — neither blocking

### `V-1` — `L-2`'s class was declared closed and four sites still say five, two of them in the signed contract

**Where.** `contract/Document-Work-Assurance-Contract-v4.md:299-301` and `:334-338`;
`tooling/rsclib/document_harness/summary.py:202`;
`tooling/tests/document_harness_review/test_run_v2_template_bind.py:1041`.

**What it violates.** `HD-41` ④ and `E7` bind the fix to the defect **class**, and the commit body
asserts the class is swept: "9 hits. Four are this class, all four fixed … Five are other referents
and are left." The scan ran — I replayed
`git grep -nEi "(these|those) (five|six)"` at `06f0b4f` over the declared scope and got the same 9
hits — but its pattern cannot match the same assertion written any other way, and four sites are.
`HD-41`'s own 起因 names this failure mode by name (半径不够: fixing the phrasing the finding
reported and not the others), which is what ④ exists to prevent.

Site by site, measured at `d56def4`:

1. **`contract:299-301` — an enumeration, not a count, and the worst of the four.** §13.2 lists the
   protected set by name — `work_spec_ref`, `start_decision_ref`, `repair_decision_ref`,
   `final_decision_ref`, `review_ref` — and asserts it **is** `assurance_state.DIGEST_PROTECTED_FIELDS`.
   The module holds six. Measured across the round: the set was 5 at `b9710af` and `15e5ccc` and
   became 6 at `97cc298`, while contract `:301` is byte-identical from `f5d9741` to `d56def4`. A
   caller deriving the digest policy from the signed text concludes `bind_authorization_ref` is
   unprotected and may carry a bare path — and `assurance_state.resume` and
   `review_subject._resolve_pointer` now both report `POINTER-UNVERIFIED` on exactly that. That is
   an actor's action changing, so this is **not** wording-level under `R9` and should not be banked
   as though it were.
2. **`contract:334-338`** — "**Only one protected field has a live write path**: of the five, only
   `review_ref` is authored by `assurance/templates/run-v2/` (`run_bind_v2.py`); the other four are
   written by hand-authored run scripts". Three of its four clauses are now false: the set is six,
   two protected fields have live write paths, and `bind_authorization_ref` is authored by
   `run_bind_v2.py`. This is the same sentence-pair the executor deliberately fixed in
   `assurance/templates/run-v2/README.md:77-81`, standing verbatim in the signed text.
3. **`summary.py:202`** — "supersession-2 narrowed state-pointer digests to the five protected
   fields", in the very file the repair edited.
4. **`test_run_v2_template_bind.py:1041`** — "`review_ref` is one of the five digest-protected
   fields".

Triaged and correctly **left**: `review_subject.py:358` (error codes) and
`test_run_v2_template_bind.py:944` ("the other five" = the five other pointers in that fixture).

**Why this is not a blocker.** The falsification happened at `97cc298`, which the FULL passed on this
point; the repair did not create it. Its failure mode is a loud refusal, not a false pass. And the
remedy for the two contract sites is a per-site ruling in the `HD-63/64/67/68` family — the plan's
own *Change boundary* forbids the executor from touching signed text without one, so a blocker
demanding it would demand what the round's boundary refuses. `HD-63`'s family exists for exactly this
class: literal text that was true at signing and became false.

**Minimum fix.** Sites 3 and 4: `five` → `six`, ordinary files, a batch already touching them.
Sites 1 and 2: a sixth `HD-63/64/67/68`-family ruling naming both sites, then `bind_authorization_ref`
added to `:300`'s enumeration and `:334-338` corrected to six / two live write paths — an announced-path
write, so `E2` disclosure site by site in the writing commit and a `CONTRACT-V4-SIGNATURE.md` record of
the post-signature write. The scan that finds the class rather than the phrasing is
`git grep -nEi "protected field|digest-protected|DIGEST_PROTECTED"`, which returns all six candidate
sites and the two false positives above.

### `V-2` — the site that made `B-2` a blocker is now correct and pinned by nothing

**Where.** `tooling/rsclib/document_harness/review_subject.py:293-297`.

**What it violates.** Nothing yet — the code is right. `E4`'s discipline is the point: the executor
mutation-tested it and **saw it not fail**, which is the honest outcome and is disclosed. Removing the
name from that tuple leaves all 956 tests green, measured above. `read_control_plane` is how an
independent reviewer derives a run's control plane out of an evidence commit, and it declares its
coverage to be the whole control plane; the next edit to that tuple can silently narrow it back, and
the class assertion added this round does not reach it — it relates `DIGEST_PROTECTED_FIELDS` to
`POINTER_FIELDS`, and this is a third hand-maintained copy.

**Why this is not a blocker.** `B-2` asked for the field to be resolved and verified, and it is. The
user's ruling specified one class assertion and the executor correctly did not write a second outside
the approved boundary; the exposure is stated in the commit body rather than closed silently.

**Minimum fix.** One assertion that `review_subject`'s tuple covers every `POINTER_FIELDS` member the
state can carry at review time — the same relation shape as the class assertion, one list over. It is
one line, but it is a new guard and the single repair is spent, so it rides the bank or the next round
touching this surface.

## 6. Observations (`R5` — routing is the user's, not mine)

**`V-O-1` — the fail-loud default relocates `B-1`'s consequence rather than removing it, for callers
this repository cannot see.** A caller still on the three-argument call gets
`STANDING-BLOCKER-UNVERIFIED` on precisely the population the old guard fired on, so an ordinary
repaired run still cannot close an `ACCEPT` there. Inside this repository the point is moot — there is
no production caller, measured — and the fail-closed choice is the right one. What it means is that
the caller's FINAL step is now **obliged** to supply the reviews, and nothing in this repository says
so to it: the run-v2 template README documents the pointer policy but not this call, and no template
script performs it. Whoever writes that step learns the obligation from a refusal.

**`V-O-2` — the ordinary repaired run reaches `ACCEPT` in a unit test, not in the reachability
suite.** The batch's spine asserts that every disposition the rules name has been *seen reached*
through the real engine. `Reachers._final` drives all four FINAL outcomes over a candidate with an
empty `unresolved_finding_ids`, so the population `B-1` was about — `ACCEPT` over a candidate carrying
a repaired blocker — is reached only in `test_flow_repair_disposition.py`. The suite's own header
already states this exposure for prose-named routes; this is a second instance of it, on the route the
round's one blocker was found in.

**`V-O-3` — `E9`'s spend is complete and the batch's closeout is the last gate.** With this record the
round's budget is exhausted: the FULL occurred, the one user-approved fix landed, this is the targeted
VERIFY. `V-1`'s contract half cannot be redeemed by any batch — only by a round or a signed-text
ruling — so if it is banked at closeout its redeem-when must name a round-eligible surface (`R10`),
and the batch is scheduled to close immediately after this round, with candidate isolation next.

## 7. Coverage — what I read in full, sampled, and only probed (`R4`)

**In full**: `document-harness/CONSTRUCTION-CHECKLIST.md`, `document-harness/RULES.md`,
`document-harness/REVIEW.md`, `harness.json`, `.harness/scan-surfaces.json`, `HARNESS-RIDERS.md`,
`CONSTRUCTION-LEDGER.md`'s current-pointer block, `document-harness/plans/promise-path.plan.md`,
`migration/document-work-assurance-v3/v3-review-full-97cc298.md`, all four commit bodies, and the
entire diff of the range for every file in it.

**Sampled**: the surrounding unchanged bodies of `summary.py`, `assurance_state.py`,
`review_subject.py`, `flow.py` and `run_bind_v2.py` where the diff or a claim reaches them;
`test_disposition_reachability.py` by its module header, its `Reachers` entry points and the changed
call; `test_run_v2_template_bind.py` at the two sites the class scan reaches.
`HARNESS-DECISIONS.md` was read at `§live`'s heading list and in full at `HD-41`; `HD-70` was read
through the FULL's account of it and the plan's rulings 6, 8 and 11, not at its own bytes.
`document-harness/journal/promise-path-vocab-2026-09-03.md` was read at the range's added lines.

**Only probed**: everything else under `tooling/`, which the battery exercises and I did not read;
`contract/Document-Work-Assurance-Contract-v4.md` was read only at §13.2 and the two `V-1` sites, by
targeted grep — I did not read it end to end, so `V-1`'s enumeration of contract sites is bounded by
the pattern I ran and stated above, not by a full reading.

**Not verified, and named as such**: the round's `E1` statement and the "same executor session
resumed" claim (`HD-69`) are process claims with no evidence lock (`R4`); the fix commit's "six probes"
and its `layer_path_check` exit-0 against a staging state that no longer exists are process claims
about a session I cannot inspect — I ran six probes of my own instead of checking theirs, and they are
what §2 reports.

**`residual_uncertainty`.** Four, and the list is a positive statement that I found no others:

1. Whether a caller outside this repository already calls `check_summary` with the old signature is
   not measurable here (`V-O-1`); this repository holds no runs.
2. `V-1`'s site list is bounded by the patterns I ran over the tracked tree excluding `migration/`,
   `document-harness/journal/`, `document-harness/plans/` and both archives. A site phrased without
   the words "five", "protected field" or `DIGEST_PROTECTED` would not appear in it.
3. Whether a third consumer of state pointers exists outside `tooling/` and `assurance/` — the FULL
   left this open at `B-2` and my probes did not close it; I established the two readers by the same
   grep it did.
4. `test_review_v2_subject.py` takes 28 s for 48 tests, almost all of it in one class that builds real
   git repositories. I ran it four times under mutation and read the tests my probes turned red; I did
   not audit the rest of that file's assertions.
