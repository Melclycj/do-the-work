# VERIFY — round `EXECUTOR-CHARTER`, repair at `3dd226b`

**Verdict: `REVIEWED_NO_BLOCKER`.** 2 low, 3 observations.

**The repair answers all six accepted findings, and I re-executed each rather than reading
it.** The construction-executor prompt no longer sends a cold executor after a counterpart
that does not exist, and I closed that class myself: all four prompt constants now agree —
the two that still say *the counterpart it names* point at a charter that names one, the two
that do not, do not. The doc-only tier exception is the criterion the user ruled rather than
a longer closed list, and its five named paths all resolve and are all really pinned — the
two templates by a `sha256` a rename turns into a `FileNotFoundError`, the contract path by
shipped code. The `four`→`five` correction is right: I re-derived it from the caller's eight
instructions myself and got the same five runs the FULL got, all five reaching Context. The
`E10`-half of the never-re-types justification is gone from `ONBOARDING.md`, and a
whole-repository scan of that class returns only the one site the user ruled stays as
history. Five mutations: the golden equality dies from either side alone, the charter
constant still dies three ways on the recorded incident's own shape, and the negative control
stayed green. All four figures the commit reports reproduce on this tree, and every permanent
boundary holds — `E2` untouched, budget and window intact, nothing pushed, two members
amended and their read debt correctly deferred.

**The two lows are both about the account rather than the act.** One is the class-scan paste
`HD-41` ④ obliges, absent from this fix leg as from the two before it — I ran all five scans
and every class is closed, so nothing acts wrongly, but that is the part a reader should not
have to re-run (`V-1`). The other is a new sentence asserting that the orchestrator delivers
*the plans* alongside the instruction and subject, which the member that owns what the
orchestrator delivers does not say (`V-2`).

---

## 1. Subject, round, budget and window — re-derived, nothing taken from the dispatch

The dispatch handed one range and two transport sentences (the repository root, and *write
your record into the worktree; do not commit*). Everything below is from the repository. I
reproduced my own prompt from the generator to confirm what was added to it:
`construction_dispatch_of('..', '693b692…', '3dd226bc…')` renders `CONSTRUCTION_PROMPT`
verbatim, so those two sentences are the whole of the addition and `E12`'s *no per-acceptance
argument* holds.

**Subject.** `693b692811b5958dbcda92a3cc722123c5f44337..3dd226bc6507ccd7abcf9175ff6b2051c34bfbd9`,
four commits. `3dd226bc` is `HEAD`. The worktree was clean at the start of this review, after
every mutation restore, and at its end (`git status --porcelain` → empty each time).

| commit | title | kind (named in its own body) |
|---|---|---|
| `71f7567` | `V3-REVIEW-RECORD-EXECUTOR-CHARTER-693b692-v1` | record (the opening cold read) |
| `229f03f` | `V3-EXECUTOR-CHARTER-v1` | candidate |
| `c06e807` | `V3-REVIEW-RECORD-EXECUTOR-CHARTER-229f03f-v1` | record (the FULL) |
| `3dd226bc` | `V3-EXECUTOR-CHARTER-FIX-v1` | review fix |

**Which leg this is, derived rather than assumed.** `E9`'s test is *has a valid independent
FULL already occurred?* `migration/document-work-assurance-v3/v3-review-full-229f03f.md`
exists and its record commit `c06e807` landed, so the answer is yes and `3dd226bc` is the
round's one user-approved fix, which obliges this targeted VERIFY. No
`v3-review-verify-*` names this round. The cold read at `693b692` spends nothing (`E10`,
`R3`), so the budget entering the fix was FULL-spent and repair-whole.

**The subject is wider than the repair, and wider than the precedent.** The two most recent
VERIFY subjects (`83e3191..627df95`, `7f6e7f0..84dea06`) were candidate-to-fix. This one is
based at the commit before the round's first record, so it re-covers the candidate and the
FULL's own record commit. `R3` scopes a VERIFY to *the accepted findings plus the whole
repair diff, and the permanent boundaries however narrow the round*, so I led on the repair
(§3) and ran the boundaries across the whole range (§4); I did not re-open the candidate's
implementation, which the FULL covered.

**Review window (`E9`).** `.harness/review-pending.json` records the subject as exactly this
range, dispatched `2026-08-22T09:37:44+00:00`; `3dd226bc` was committed
`2026-08-22 19:37:33 +1000` = `09:37:33Z`, eleven seconds earlier, and `HEAD` is still
`3dd226bc`, so no commit has landed since. `.harness/` is ignored
(`git check-ignore -v` → `.gitignore:18:.harness/`), so the marker is not itself a commit.
I also ran `dtw dispatch --construction-executor` against this repository during the review
and the marker's bytes were identical before and after (§3.1), so my own probing did not
disturb the window.

**Authorization (`R7`).** The fix's boundary is chat-held: the commit states the user
approved the full package on 2026-08-22 against the FULL, and that the `R10` spend-or-bank
triage of each low was put to the user before closeout. I cannot see that exchange. What I
can see is that the package the commit acts on matches the two committed records exactly —
the FULL's five lows and the cold read's one — and that the two places where the FULL
explicitly reserved the choice for the user under `R5` (`L-2`'s two readings, `L-4`'s
`HD-46` half) are the two places the commit reports a user ruling rather than an executor
judgement. That is consistent, not proof. Ceiling stated, moving on.

## 2. Changed paths, classified by hand

**The repair.** `git show --stat 3dd226bc` → 4 files, 22 insertions, 18 deletions.

| path | class | note |
|---|---|---|
| `document-harness/EXECUTION.md` | **`E10` member** | three hunks: the C4 `O-1` justifying sentence, the doc-only tier exception, the authoring rule's completeness claim |
| `document-harness/ONBOARDING.md` | doc, **not** a member (says so at its own `:9`) | the `E10` half of the never-re-types justification deleted |
| `tooling/rsclib/document_harness/dispatch.py` | code | `CONSTRUCTION_EXECUTOR_PROMPT` only |
| `tooling/tests/fixtures/expected-construction-executor-prompt.txt` | fixture | the golden moves with the constant |

**The whole range.** 13 files, 1518 insertions, 76 deletions — the four above plus the
candidate's `cli.py`, two test files, two fixtures, `HARNESS-DECISIONS.md`,
`HARNESS-RIDERS.md`, `ORCHESTRATION.md`, and the two review records.

**The fix's surface extends past the plan's, and says so.**
`document-harness/plans/executor-charter.plan.md` §*Change surface* names six surfaces and
does **not** name `ONBOARDING.md`. The repair touches it. This is not a silent escape: the
fix's boundary is the approved finding package, not the candidate's plan surface, the file
is named in the FULL's `L-4` as one of the two surviving sites of that class, and the commit
body enumerates all four changed files in its second sentence. `E9`'s requirement is that
exceeding a boundary be said rather than hidden, and it was said.

## 3. The accepted findings, each re-executed rather than accepted

### 3.1 `L-5` — the counterpart the checklist does not name

The constant and the golden both drop `, and the counterpart it names`, leaving *read it
before anything else* — the exact bytes the FULL's minimum fix specified, and the form
`EXECUTOR_PROMPT` already used at `dispatch.py:785`.

I closed the **class**, not the instance. Four prompt constants say *read it*:

```
dispatch.py:559  CONSTRUCTION_PROMPT           "…and the counterpart it names…"  → review-contract stub
dispatch.py:675  READ_PROMPT                   "…and the counterpart it names…"  → review-contract stub
dispatch.py:785  EXECUTOR_PROMPT               "read it before anything else"    → EXECUTION.md
dispatch.py:801  CONSTRUCTION_EXECUTOR_PROMPT  "read it before anything else"    → CONSTRUCTION-CHECKLIST.md

grep -ci counterpart  →  review-contract stub 1 · CONSTRUCTION-CHECKLIST.md 0
```

Every prompt that sends its reader after a counterpart points at a charter that names one;
the one that pointed at a charter naming none no longer says it. That is `E7` satisfied. My
own dispatch carries the phrase and it resolved — the stub's *"It is your standing
instruction and its own counterpart; read all of it"* is what sent me to the checklist — which
is the asymmetry `L-5` was about.

**Driven end to end, outside the test suite.** `dtw dispatch --construction-executor
--repo-root .` → exit 0, the fixed sentence, the derivation line saying *nothing else is
derived*, and **no `.harness/` write** (marker byte-identical before and after).

### 3.2 `L-2` — the completeness claim

`EXECUTION.md:445-447` now reads *live in this file and the governing plans; `dtw dispatch
--executor` names this file to the executor at startup, the plans arriving with the
instruction and subject the orchestrator delivers*. The hedge the candidate dropped is
restored — I checked it against the pre-round bytes at `693b692:document-harness/EXECUTION.md`,
where the same sentence read *live in `EXECUTION.md` and the governing plans*. So the claim
is no worse than the round found it, which is what the FULL's first branch asked for.

Re-measured across all ten `E10` members at the tip:

```
'gap bank'                 -> EXECUTION.md:445 only
'first-run' | 'first run'  -> EXECUTION.md:445 only
'HarnessIssue'             -> CONSTRUCTION-CHECKLIST.md 1 · EXECUTION.md 1 (:31, "optional") · REVIEW.md 1 · ORCHESTRATION.md 0
```

Both examples still appear exactly once in the layer, inside the sentence asserting where
they live, so the restored disjunction's truth now rests on the *plans* half, which is
caller-held and unverifiable here. The delivery half of the same sentence is `V-2`.

### 3.3 `L-3` and `L-1` — the sampling paragraph

The justifying sentence is rewritten, taking the FULL's second branch (*correct it to say
who is actually bound and how they learn of it*). Both halves check out:

- **Placement by adjacency is true.** The paragraph sits at `:276`-`:287` under *Authoring
  gate (W2-A5 + M11)*, whose immediately preceding bullet (`:265`-`:274`) is the M11 Phase-C4
  gate that generates `paragraph-map.json` and takes the one human `classification` column.
  It is literally beside the gate that authors the map it samples.
- **The ledger line exists.** `CONSTRUCTION-LEDGER.md:106`-`:109` carries the C4 `O-1`
  conversation-only row, stating both the per-run recording and the three re-ruling branches.
- **The old justification's defect is gone.** The removed sentence claimed the obligation
  arrived with the executor's dispatch; the new one says the opposite in as many words —
  *rather than through this file's dispatch* — and names the orchestrator instead. `EXECUTION.md`
  is the product executor's charter (`EXECUTOR_ROLE_INSTRUCTION`, `dispatch.py:770`), and
  `ORCHESTRATION.md:33-35` says nothing dispatches the orchestrator, so a claim of dispatch
  delivery for an orchestrator obligation would have been false; it is no longer made.

**`four` → `five`, re-derived from the primary source rather than inherited.** The caller at
`D:/Thesis-stage-control-refactor` is reachable from this machine; I read it and wrote
nothing. Eight run instructions, grepped for the disclosure and each hit classified by its
governing heading:

```
p4-bridge    :18,:19 (preamble — its four first-run obligations)  :87 '## Context (non-normative)'
p4-doc       :129,:131                                                '## Context (non-normative)'
p5a-firewall :94,:95                                                  '## Context (non-normative)'
p5a-shells   :227,:228                                                '## Context (non-normative)'
p5b-firewall :171,:172                                                '## Context (non-normative)'
p3-corr / p5b-claims / w1-r1 : no instance (their 'classification' hits are unrelated)
```

Five runs, and all five reach Context — so *where it spent five runs hand-copied* is exactly
right, including for `p4-bridge`, whose differing wording is what the earlier `four` missed.
This matches the FULL's table and the plan's committed statement; I took neither on trust.

### 3.4 Cold read `L-1` — the doc-only tier exception

The exception now opens *today*, names five paths, and closes on *any doc path code or a test
pins*. That is `HD-45` ②'s criterion made self-evidently open, which is the reading the user
chose; the enumeration is no longer load-bearing, so its completeness is no longer a defect
surface. Each named path checked at the tip:

| named | pinned by | verified |
|---|---|---|
| `document-harness/README.md` | `test_readme_enumeration.py` | pre-existing |
| member paths | `hooks/layer_path_check.py` `LAYER` (10 literals, `:38`-`:47`) | pre-existing |
| the two templates under `document-harness/templates/` | `init_target.py:35-37` `TEMPLATES` + `:48` `TEMPLATE_DIR` + `:76-77` copies them; `test_init_command.py:38-41` hand-writes both source paths and `:71-72` `sha256` them | the directory holds **exactly two** files, so "the two" is accurate; a rename raises rather than passing |
| `contract/Document-Work-Assurance-Contract-v3.md` | `__init__.py:41` `CONTRACT_PATH`, read at `:249-250` | hard pin |

**The executor's widening of the reader's supplied bytes is right, and its stated reason is
right.** The cold read supplied `init_target.py` and `rsclib/document_harness/__init__.py`.
The second has a slash and would have been scanned — and would have failed, since the real
path is `tooling/rsclib/…`. I confirmed the guard's behaviour directly (§4.4). Taking the
supplied bytes with that correction, and disclosing it, is the free-channel discipline
working.

### 3.5 `L-4` — the never-re-types justification, and the class

`ONBOARDING.md:5-7` now reads *…because a second copy is a second thing that has to stay true
(`HD-5` records transcription as a drift surface)* — the `E10` half deleted, `HD-5` carrying
the conclusion alone, the same deletion the candidate made at `ORCHESTRATION.md:13` and the
same form that sentence now takes. `ONBOARDING.md` is not an `E10` member (its own `:9`, and
`E10`'s membership sentence does not name it), so this is not a layer amendment.

**I ran the class scan the fix does not paste** (`HD-41` ④), over all tracked markdown:

```
HARNESS-DECISIONS.md:221                      `E10` 明写成员编辑 never re-typed "with the same content"
document-harness/CONSTRUCTION-CHECKLIST.md:106  E10 itself stating its own rule — not the class
plans/harness-layer-incorporation-round.plan.md:62  describes E10's edit discipline correctly — not the class
```

One site of the class survives, and it is the one the user ruled stays as a historical record
of the reasoning as it was. Nothing else in the repository makes the move the retired rider
objected to. The class is closed, and since the rider's `HD-46` reservation was answered by a
ruling rather than deferred, `R10` leaves nothing owed here.

## 4. The permanent boundaries

### 4.1 `E2` — nothing frozen was written

All three blobs are byte-identical at both ends of the range: `b2dbdf752d8c…`,
`68031fa2ca31…`, `e1a2f26b1d8d…`, matching the rule's own text.
`git diff --name-only 693b692 3dd226bc -- contract/ schema/` returns nothing, and the pack
still holds 15 files at the tip.

### 4.2 `E10` — two members amended, eight citable, the debt correctly deferred

Blob ids for all ten, computed at both ends and against the worktree
(`git hash-object` == `git rev-parse 3dd226bc:<path>` for all ten, so the review was
performed on the subject bytes):

```
                                                        @693b692   @tip
CONSTRUCTION-CHECKLIST.md                               cacd99d4   cacd99d4   unchanged
README.md                                               7591c533   7591c533   unchanged
EXECUTION.md                                            27f4fc82   ab261698   AMENDED
REVIEW.md                                               35fe0abc   35fe0abc   unchanged
ORCHESTRATION.md                                        80f42658   48f665c4   AMENDED (candidate, not the fix)
v3-harness-operating-contract.md                        6d571492   6d571492   unchanged
v3-harness-review-contract.md                           29bdc9fb   29bdc9fb   unchanged
supersession-1.md                                       68031fa2   68031fa2   unchanged
supersession-2.md                                       e1a2f26b   e1a2f26b   unchanged
paragraph-map.schema.json                               09aa8699   09aa8699   unchanged
```

The eight unchanged are byte-identical to what `v3-cold-read-693b692.md` §2 records, so the
next read of this layer may cover them by citation and owes a real read of two — which is the
per-member digest cost `E10` names. The fix touched only `EXECUTION.md`, already inside the
debt the candidate recorded, so the commit's *the member edits here join the independent-read
debt* is accurate. `E10`'s *may be relied upon before its read* clause does not cover this
round, and does not need to: no round has relied on the amended text — authoring, citing and
recording it are not reliance — so nothing is violated, and the FULL's `O-7` trigger (the
first product-run instruction written under the new authoring rule) still names the moment
the read falls due.

### 4.3 `E8`, `E9`, `E12` — form, budget, handoff

- Single dense title naming the round, `V3-EXECUTOR-CHARTER-FIX-v1`; kind named in the body's
  first two words (*Kind: review fix*); one dense paragraph; **no trailers**; new commit, not
  an amend (author and commit timestamps identical, as on the two commits before it).
- `git log origin/main..main` = 8 and `origin/main` is still `f084db4`, so nothing was pushed.
- The commit applies `E9`'s own test — *has a valid independent FULL already occurred* — rather
  than naming its own consumption, which is the discipline `E9` asks for when it forbids
  self-classifying which round consumed what.
- `E1`'s middle-state disclosure is carried once for the round, in the candidate's body, and
  names all four of `R1`'s holdings explicitly. `E1` puts it on the round, not on each commit,
  so the fix not repeating it is correct; nothing in the fix contradicts it.
- `E12`'s *never a written SHA* clause concerns a **recorded** range, whose defect is that the
  recording is itself a commit. `.harness/review-pending.json` is a gitignored run-time marker,
  not a commit, and `E9` depends on it holding the resolved subject — so the full tip SHA
  there is display, not a recorded range. Not a finding.

### 4.4 The figures, re-measured on this tree

| claim | my measurement |
|---|---|
| targeted `tests/document_harness_review/` = 480 passed | `480 passed in 79.83s` |
| full battery from `tooling/` = 790 passed | `790 passed in 141.86s` |
| unchanged in count from the candidate | the fix diff touches no test file, only the fixture — so no test was added or removed |
| `sweep_refs.py` = 17 | `17 caller-held or unresolvable references over 10 members`; the ten in `EXECUTION.md` are at `:186 :194 :199 :304 :367 :371 :371 :487 :488 :491`, none inside a hunk this fix touched, so the "added none" half follows |
| `layer_path_check` exit 0 | see below — my first attempt was vacuous and I re-ran it properly |

**The guard measurement, done twice.** Running `layer_path_check.py` directly on a clean tree
returns exit 0 for the trivial reason that its `__main__` reads `git diff --cached` and
nothing is staged. That number would have been worthless, so I drove its own
`unresolved_tokens` over the commit's actual added lines with its own `LAYER` and parser:

```
paths with added lines : EXECUTION.md · ONBOARDING.md · dispatch.py · expected-construction-executor-prompt.txt
LAYER members among them: document-harness/EXECUTION.md  (18 added lines, 6 path-shaped tokens)
  OK contract/Document-Work-Assurance-Contract-v3.md      OK document-harness/README.md
  OK document-harness/templates/                          OK tooling/hooks/layer_path_check.py
  OK tooling/rsclib/document_harness/__init__.py          OK tooling/rsclib/document_harness/init_target.py
unresolved_tokens = []   →   exit 0
```

`CONSTRUCTION-LEDGER.md` on the added line `:284` carries no slash, so `PATHLIKE`'s
`"/" not in token` guard skips it — but `E10`'s clause requires it resolve and it does, at the
repository root. `test_readme_enumeration.py` is skipped the same way; it is pre-existing
prose and outside this fix's obligation.

### 4.5 Registers

`HARNESS-RIDERS.md` 34 rows → 32, the two the candidate redeemed (`charter-prose-overreach`,
`startcard-form`); the fix adds and deletes none, which is right — the one disposition that
could have owed a row was ruled rather than banked. `HARNESS-DECISIONS.md` changes only
`HD-52`, moved `§live` → `§implemented`, and its carrier is real: `EXECUTION.md:245` now
carries *However the form resolves, the START card of every product run is rendered by `dtw
preview` from the frozen control plane* as a paragraph outside the enumerated-form bullet,
which is what `HD-52`'s transition condition required and what `HD-2` requires land in the
same commit as the flip. `§live` now holds eight entries.

### 4.6 `E6` — no new machinery

The repair adds no guard, no test, no field, no derived output. Every accepted finding was
answered by the named text changing, which is what `E6`'s *both sides* clause requires and
what a VERIFY meeting a rule-instead-of-fix would have to refuse. There is nothing here to
refuse.

## 5. The guards still bind — five mutations (`R8`)

Both files were copied to a scratchpad and their sha256 verified before every restore
(`dispatch.py e138785f16f4…`, `golden 020a9f82d33a…`, identical before the first mutation and
after the last; restores from the checked copies, never `git checkout --`). Suite =
`test_dispatch.py`, baseline `69 passed`.

| # | what was changed | result |
|---|---|---|
| M1 | the constant only — the removed phrase put back, golden untouched | red: `ConstructionExecutorDispatchGeneratesToo::test_the_prompt_is_exactly_the_golden_file`, 1 failed |
| M2 | the golden only — the phrase put back, constant untouched | red: same single test, 1 failed |
| M3 | **negative control**: one word of an unrelated `#:` comment | **green, 69 passed** — no false fire |
| M4 | `CONSTRUCTION_EXECUTOR_CHARTER` → `document-harness/EXECUTION.md` (the other side's charter) | red ×3: golden equality, `…nothing_is_derived_beyond_the_charter`, and the mount test |
| M5 | the trailing clause dropped from constant **and** golden consistently | **green** — the ceiling, see `V-3` |

M1 and M2 together are the point: the whole-document equality binds in both directions after
the fix moved its bytes, so neither side can drift alone. M4 re-proves that the recorded
incident's own shape — citing the other side's charter — is still pinned after the fix
touched that constant's neighbourhood. No mutation died by crashing; each died on a named
assertion, which is what `R8` asks.

## 6. Findings

### `V-1` (low) — `HD-41` ④'s class-scan grep is pasted nowhere in the repair, for the third fix leg running

`HD-41` is `live` and `standing`, re-affirmed by the user on 2026-08-17 as pure discipline
with no machine behind it. Its fourth clause obliges a fix to grep the assertion's keyword
strings across the round's work files **before** writing and to paste that output into the
commit body — *扫类是动作不是自觉，贴证据是为了「跑没跑」可被评审员当场看见*.

`3dd226bc`'s body pastes four verification figures and no grep output at all. The tally,
re-derived rather than taken from the `627df95` VERIFY that first named this drift:

```
84dea06  V3-INIT-SURFACE-FIX-v1        grep-mentions = 1
15a53fe  V3-PREVIEW-RENDER-FIX-v1      grep-mentions = 0
627df95  V3-TEMPLATE-LIB-ROOT-FIX-v1   grep-mentions = 0
3dd226bc V3-EXECUTOR-CHARTER-FIX-v1    grep-mentions = 0
229f03f  V3-EXECUTOR-CHARTER-v1        grep-mentions = 1   ← this round's own candidate
```

Four fix legs, one paste — and this round is the sharpest instance yet, because its
**candidate** pasted scan-class evidence for its two classes (`by reference`, `START card`)
and its fix leg, acting on five different classes, pasted none. The discipline was in view.

I ran all five scans myself: the counterpart class (§3.1), the never-re-types class (§3.5),
the code-pinned doc-path class (§3.4), the hand-copy count (§3.3) and the completeness claim
(§3.2). **Every class is closed and nothing acts wrongly today.**

**Downstream decision that goes wrong if unfixed.** The paste is what lets the next reader
tell *the class was swept* from *the reported instance was patched* — the `E7` question.
Absent it that reader either re-runs the scans, as I did, or takes the sweep on trust; and
`HD-41`'s own recorded history is that the second happens. Note also that citing the FULL's
scans is not equivalent even where they exist: a pre-fix scan establishes a class's extent,
while what a fix owes is the scan showing the class **closed** at the fix tree — which for
`L-4` is a different measurement, since the fix itself changed one of the three sites.

**Route.** The work product here is an immutable commit body and `E8` forbids amending, so
there are no bytes to apply. It is a discipline finding about a repeating pattern, and the
pattern — not this round — is what is worth naming. `R10`'s bank is the natural home; the
choice of whether four-in-a-row warrants more than a row is the user's.

### `V-2` (low) — `EXECUTION.md` now says the orchestrator delivers the plans; `ORCHESTRATION.md`, which owns what the orchestrator delivers, does not

`EXECUTION.md:445-447`, the delivery half of `L-2`'s repair:

> *`dtw dispatch --executor` names this file to the executor at startup, **the plans arriving
> with the instruction and subject the orchestrator delivers**, so the instruction no longer
> carries even the reference.*

`ORCHESTRATION.md`'s *Handing the executor its instruction* is the section this layer makes
the text for that obligation (`:53` — *The three obligations this file is the text for*), and
it enumerates the delivery twice without ever naming a plan:

```
:57  "The orchestrator delivers the round's **instruction and subject**, and stops there."
:58  "the delivery opens with a generated half: dtw dispatch --executor … hands the executor
      its charter at startup"
:61  "It does not hand over a decomposition: …"
```

So that member's delivery set is charter + instruction + subject. `grep -i plan
document-harness/ORCHESTRATION.md` returns one hit, `:83`, which is *something that changes
the plan* in the report-back section — not a delivered artifact. Across the whole layer, *the
governing plans* occurs at `EXECUTION.md:446` and nowhere else.

**The downstream decision that goes wrong.** This is exactly the decision `L-2` was raised to
protect. An instruction author governed by plan-resident discipline now writes nothing in
Context — a demand there is a defect on sight under the same bullet — and relies on the plans
reaching the executor. An orchestrator reading its own charter delivers the charter, the
instruction and the subject, and has no line telling it to deliver plans. The discipline then
reaches nobody, which is the gap the repair was meant to close. A second, smaller instance of
the same shape sits in the sentence's first half: the FULL located the gap-banking discipline
in `ORCHESTRATION.md`'s *executor's report back*, and the restored disjunction — *this file
and the governing plans* — names neither that file nor that section, so one of the two
examples still has a home the sentence does not point at (§3.2's measurement).

**Not inflated.** The repair took the FULL's own first branch verbatim, so the sentence is no
worse than the pre-round text on the half the finding was about; what is new is only the
delivery clause. A VERIFY has no `CHANGES_REQUIRED` verdict, and on the merits nothing acts
wrongly until a product run is authored under the new rule — the same moment `O-7` names for
the layer read.

**Minimum fix, and both branches are design, so `R5` routes the choice.** Either
`ORCHESTRATION.md`'s delivery section names the plans as part of what the orchestrator hands
over — which adds to an obligation and so opens a round under `E10` — or `EXECUTION.md` drops
the delivery assertion and says only where the rules live, leaving how they arrive to the
orchestrator's own reading. Because the fix is design either way, the row it banks under
`R10` names a round-eligible surface, never a batch; its natural deadline is the first
product-run instruction authored under the new rule, the same moment `O-7` already carries.

### `V-3` (observation) — the sampling paragraph routes its own delivery through a ledger row whose admission criterion it falsifies

`EXECUTION.md:283-285` names `CONSTRUCTION-LEDGER.md`'s conversation-only line as how the
obligation reaches the orchestrator. That row exists (`:106`-`:109`) and the statement is
honest. Two couplings are worth having on the record before closeout:

- The list the row sits in states its own admission criterion at `:101` — *层内确无别家*, no
  other home in the layer. `EXECUTION.md:278-280` is now such a home for the recording half,
  and states it in nearly the same words the row does, which is the `HD-5` drift surface
  `ORCHESTRATION.md:13` cites. The row still passes the criterion on its **other** half —
  the three re-ruling branches are stated there and nowhere in the layer, and `:281` points at
  the row for exactly that — so the row is not redundant. But the FULL's `O-5`(c) records the
  move of this row as owed, and if closeout moves or trims it, the layer sentence that now
  depends on it is what breaks.
- The paragraph's first sentence still reads *the run's review/closeout records one line*,
  with the actor supplied two sentences later. The ambiguity `L-3` was raised about is
  resolved by the new sentence rather than by the sentence that states the obligation.

Recorded, not concluded: whether a standing obligation binding the orchestrator should live
in the executor's charter at all is a *should this exist* question, and `R5` puts it to the
user. The FULL offered re-homing as its first branch and the user chose the second; I am
noting the residue of that choice, not reopening it.

### `V-4` (observation) — what the golden equality can and cannot prove, measured

`M5` is the ceiling stated as a measurement: changing the constant and the fixture
consistently in one commit leaves the suite green, because a whole-document golden pins
agreement between two artifacts, not the truth of the sentence they agree on. That is the
design working — `M1`/`M2` show neither side can drift alone, which is the property it exists
for — and it is precisely what this fix legitimately did. The consequence worth naming is
that no automated check could have caught `L-5`, or would catch its recurrence: the
prompt-sentence class is held by human reading, of which this review and the FULL are the
whole enforcement. Not a defect, and `E6` argues against building a guard for it; recorded so
that a future round does not mistake the green suite for coverage of the sentence.

### `V-5` (observation) — the closeout carriers the FULL named are still outstanding, unchanged by the repair

At the tip, `CONSTRUCTION-LEDGER.md` and the round journal are untouched, and
`HARNESS-DECISIONS.md` carries no entry for the ruling admitting the two executor modes. On
the `HD-51`/`HD-52` precedents those land at closeout, so their absence from a fix leg is
correct, not an escape. Listed because `R10`'s triage and the closeout are the next steps and
the FULL's `O-5` list — the modes ruling, the C4 `O-1` reading-moment ruling, and the ledger's
open-items line for the `ORCHESTRATOR-CHARTER` question ① — is still exactly as long as it was.

## 7. Coverage and honesty ceilings (`R4`)

**Read in full:** the whole repair diff at `-U6`; `document-harness/CONSTRUCTION-CHECKLIST.md`;
`migration/document-work-assurance-v3/v3-harness-review-contract.md`;
`document-harness/ORCHESTRATION.md`; both records in the range
(`v3-cold-read-693b692.md`, `v3-review-full-229f03f.md`); `tooling/hooks/layer_path_check.py`;
the four commit bodies; `ConstructionExecutorDispatchGeneratesToo` and its neighbours;
both golden fixtures for this family.

**Sampled:** `document-harness/EXECUTION.md` (the three changed regions and their surrounding
sections read; the rest grepped); `document-harness/REVIEW.md` (grepped);
`HARNESS-DECISIONS.md` (`HD-41`, `HD-45` ②, `HD-52` read; `§live` headings enumerated; the rest
grepped); `HARNESS-RIDERS.md` (the two deleted rows and the row count);
`CONSTRUCTION-LEDGER.md` (the conversation-only list and the current pointer);
`document-harness/plans/executor-charter.plan.md` (§*Change surface*, §*Opening conditions*,
the two hand-copy-count paragraphs); `init_target.py`, `__init__.py`, `test_init_command.py`
(the pins §3.4 names); `v3-review-verify-627df95.md` (its `V-1` and structure).

**Probed only, by command:** the caller repository at `D:/Thesis-stage-control-refactor`
(read-only — eight instructions grepped and each hit heading-classified; nothing written);
the CLI driven once in each relevant mode.

**Not read:** the candidate's `cli.py` and test additions beyond the classes I mutated — the
FULL covered them and this repair does not touch them; the product review path; the schema
pack; the run-v2 templates.

- **`UNVERIFIABLE`: the user's approval of the fix boundary and of the `R10` triage.**
  Chat-side. §1 states what corroborates it in the repository and what does not.
- **`UNVERIFIABLE`: `E11`'s preview card.** Chat-side.
- **`UNVERIFIABLE`: that this record lands unchanged.** `R1`'s *reported through* holding
  cannot be checked from inside the repository.
- **My independence is not structural, and the round says so.** The candidate's `E1`
  disclosure states that orchestrator and executor were one work-side session holding all four
  of `R1`'s holdings in the operational sense, and does not claim structural independence. I
  confirmed my prompt was the generator's output verbatim plus two transport sentences, ran
  cold, and re-derived every figure. That is a discipline, not a structure, and I do not
  certify it as more. The literal-reading tension in `E1`'s tiers is the open rider
  `one-session-roles` ①, not a defect of this round.
- **The five-run count was measured in a different repository.** `D:/Thesis-stage-control-refactor`
  is machine-local and outside my subject. A reviewer on another machine cannot reproduce it;
  the plan's committed statement of *five* is the reproducible half. I wrote nothing there.
- **The `790` figure at the base is not mine.** I measured 790 at the tip and confirmed the
  fix touches no test file; I did not check out `693b692` or `229f03f` to run the battery there.
- **A process claim is marked, not verified** (`R4`): that this VERIFY ran in a fresh context
  is a declared identity the repository cannot lock.
- **Mutation proves binding force, not sufficiency.** Five mutations behaving says these tests
  have force against the shapes I aimed at, and `M5` says explicitly what shape they have none
  against. It does not say the shapes I aimed at are all the shapes that matter.
- **A VERIFY is not a re-certification** (`R4`). I did not re-review the candidate's
  implementation; the FULL did, and my subject range being wider than the repair does not make
  this record a second FULL.

---

*Record written into the worktree per `R6`; not committed. Worktree clean at close
(`git status --porcelain` empty before this file was written), `HEAD` still `3dd226bc`; both
mutated files restored from sha256-checked scratchpad copies and re-verified identical to
their pre-mutation digests.*
