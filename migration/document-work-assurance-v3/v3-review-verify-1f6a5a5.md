# VERIFY review — `38038ec..1f6a5a5` (round `PROMISE-PATH-ENGINE`, batch `PROMISE-PATH`)

**Verdict: `REVIEWED_NO_BLOCKER`.**

The one accepted blocker is closed at all three sites and closed in the shape the finding
named; the two lows folded onto the same leg are closed too. The repair diff contains nothing
the findings did not ask for, no announced path was written, no `E10` member was touched, and
the battery is green at a count re-measured immediately before this claim. Two observations go
to the user under `R5`; neither is in the repair diff and neither stands in the way of this
verdict.

> Subject received as a range and nothing else (`R2`). Round, budget, authorization, the
> accepted-finding set, the change boundary and every figure below were re-derived from the
> repository; no reported figure was accepted without re-running the command that produces it.
>
> Written by the reviewer and **not committed by it** — the orchestrator commits the record and
> that commit is what deletes `.harness/review-pending.json`, which is deliberately left in
> place here (`R6` read against the user's ruling (c) of 2026-09-02, which downgraded the
> `R6`-versus-`REVIEW.md` conflict to the banked rider `record-commit-owner`).

## 1. Subject, re-derived

Two non-merge commits. Base `38038ecbc54bc7814ea090bedd4fad9a2456d436`, tip
`1f6a5a54f5a1a9968a3cec570b4b6041bb46313d`. Oldest first:

| # | sha | title | kind, from its own body |
|---|-----|-------|-------------------------|
| 1 | `09daa7e` | `V3-REVIEW-RECORD-PROMISE-PATH-ENGINE-38038ec-v1` | record — the round's independent FULL |
| 2 | `1f6a5a5` | `V3-PROMISE-PATH-ENGINE-FIX-v1` | review fix — the round's one user-approved repair |

```
$ git rev-list --no-merges --count 38038ec..1f6a5a5
2
$ git diff --numstat 38038ec 1f6a5a5
42	24	assurance/templates/run-v2/run_bind_v2.py
501	0	migration/document-work-assurance-v3/v3-review-full-38038ec.md
26	0	tooling/tests/document_harness_review/test_disposition_reachability.py
141	2	tooling/tests/document_harness_review/test_run_v2_template_bind.py
```

**Paths classified by hand** (`R2`), from `git diff --name-status`:

- **Review record** (1, `A`): `migration/document-work-assurance-v3/v3-review-full-38038ec.md`
  — the FULL's own record, committed unchanged as returned. Not part of the repair diff.
- **Run template** (1, `M`): `assurance/templates/run-v2/run_bind_v2.py`.
- **Tests** (2, `M`): `tooling/tests/document_harness_review/test_run_v2_template_bind.py` ·
  `tooling/tests/document_harness_review/test_disposition_reachability.py`.

No schema file, no `E10` member, no engine module, no instruction text. **The repair diff is
those three files and nothing else**, which is exactly the boundary the fix's body claims.

**Freeze window re-derived rather than assumed** (`REVIEW.md`, *Where the result lives*: the
hook is advisory and per-machine). `.harness/review-pending.json` names as its subject
`38038ecbc54bc7814ea090bedd4fad9a2456d436..1f6a5a54f5a1a9968a3cec570b4b6041bb46313d`,
dispatched `2026-09-02T14:29:59+00:00`, and `git rev-parse HEAD` on `dev` is
`1f6a5a54f5a1a9968a3cec570b4b6041bb46313d` — branch tip equals dispatched tip, so no commit
landed after dispatch and `E9`'s no-commit-but-the-record window held. The worktree carried the
same two untracked entries at the start and the end of this review (`.goals/`,
`document-harness/journal/promise-path-engine-2026-09-02.md`) and nothing else; every mutation
probe below was restored from a sha256-checked scratchpad copy held outside the repository and
re-verified with `sha256sum -c`, never with `git checkout --`.

## 2. Round, budget, authorization, boundary — re-derived

**Which round.** `CONSTRUCTION-LEDGER.md`'s backlog names batch `PROMISE-PATH` as the queue
head (user ruling 2 of 2026-09-01). The plan is `document-harness/plans/promise-path.plan.md`;
its *Rounds and budget* section assigns round 1 `PROMISE-PATH-ENGINE` items 3–7 plus the
`E4`-inverse suite. Both commit titles name that round.

**Budget (`E9`), measured rather than assumed.** `E9`'s test is *has a valid independent FULL
already occurred?*

```
$ ls migration/document-work-assurance-v3/ | grep -E '1f6a5a5|38038ec|1c18e4a|51bd4f6'
v3-cold-read-51bd4f6.md
v3-review-full-38038ec.md
```

One cold read (the round's opening) and one FULL. So: the FULL leg is spent by `09daa7e`;
`1f6a5a5` is the round's **one user-approved fix** and, being a change to the reviewed work
after a valid FULL, obliges this targeted VERIFY; this record spends the third and last leg.
After it the round's `E9` budget is exhausted, and the only commits the round still owes are
its closeout records.

**Authorization I can see, and the ceiling (`R7`).** The repair's scope — "ruled option (ii) by
the user 2026-09-03 … B-1 with L-1 and L-2 folded in", with option (i) B-1-only offered and not
taken — is stated in `1f6a5a5`'s own body, and more fully in the untracked round journal. I
cannot see the conversation behind it; it is a hint under `R7` and I state the ceiling rather
than treat it as verified. The carrier is the sanctioned one: the ledger's standing 2026-08-16
④ entry puts construction-round rulings in commit bodies by design. What I *can* check is
whether the repair exceeds what a ruling of that shape would authorize, and it does not — §4.

**Change boundary.** The plan's **In** list names `assurance/templates/run-v2/` (both
templates) and `tooling/tests/`; all three written files are inside it, and no round-2 surface
(`document-harness/RULES.md`, `document-harness/REVIEW.md:129-135`, contract `:118`) was
touched.

**`E2`.** No announced path was written. Re-run rather than read out of a commit body:

```
$ python tooling/announced_path_disclosure.py --before 38038ecbc54... --after 1f6a5a54f5a...
announced-path disclosure: range 38038ecbc54bc7814ea090bedd4fad9a2456d436..1f6a5a54f5a1a9968a3cec570b4b6041bb46313d
  floor 1d4d9aa1f6b1daca3fbf1a7765985abaec350b18; 2 non-merge commit(s) judged
  every announced path changed in this range is named by the commit that changed it
(exit 0)
```

Corroborated by hand from the four-path classification above: neither
`contract/Document-Work-Assurance-Contract-v4.md` nor anything under
`schema/document-assurance-v3/` is in the range at all.

**`E8`.** Both titles are one dense line naming the round in the `V3-…-v1` form; both bodies
open `Kind: …` (*record*, *review fix*), which is the attribution `E8` asks for; a trailer grep
over `1f6a5a5`'s body returns nothing. The fix's body is long, which the ledger's standing
2026-08-07 entry admits — `E8` buys density and the absence of trailers, not a literal single
paragraph.

**`E12`.** The handoff was one range and nothing else; no per-acceptance argument reached me.

## 3. The accepted findings — did the repair meet them

`R3`: implementation first. I read `run_bind_v2.py`'s diff and the changed regions of the
current file in full, both test diffs in full, and `emit_reviewed`'s four call sites and the
candidate act as the file now stands. Then I mutation-probed the fix myself six ways, each time
neutering the **engine** and never the test.

### `B-1` — closed, at all three sites, in the shape the finding named

The finding asked for three things. Each is present and each was independently made to fail.

**(a) The `emitted` line is printed only where a transition was written — at all three sites.**
`emit_reviewed`'s return is now honoured at `:384` (round-0 blocked branch), `:425` (`R10`, no
decision on disk) and `:460` (`R10`, an `APPLY_ACCEPTED_FINDINGS` decision), the same way the
candidate act at `:557` already honoured it. Where nothing was written the branch prints its
resumed position instead. `E7` is met at the class rather than at the reproduced instance, and
the class has no member outside this module: a scan for a printed state-write claim across the
run templates leaves only `run_bind_v2.py:583` and `run_repair.py:111`, both of which follow an
unconditional `assurance_state.save` on the immediately preceding lines.

**(b) The stored `next_action` equals the printed one on the two-pass `APPLY` path.** Inside
`emit_reviewed`, already-`REVIEWED` stops being a no-op and saves
`{**state, "next_action": next_action}` — a field update with the status left where it is. I
checked the argument the body makes for that shape rather than accepting it:
`flow._SUCCESSORS["REVIEWED"]` is `('REPAIRING', 'AWAITING_FINAL')`, so `REVIEWED -> REVIEWED`
is not legal and `assurance_state.advance` does not check legality — while
`assurance_state.save` calls `check_state(state).require()` (`assurance_state.py:184-187`), so
the field update really is schema-validated on its way to disk. Taking the transition would
have written an illegal one; this does not.

**(c) A test that drives the real ordering.** `TheSecondPassReportsWhatItActuallyWrote`, six
methods, and the ordering is the point: `two_passes()` runs the step, writes the user's decision
**between** the passes, and runs it again — the sequence the decision point exists to produce
and the one the class's older `EVIDENCED`-with-the-decision-already-present fixtures cannot.
Both halves are asserted at each site, and `E5` holds: `WROTE` and `RESUMED` are hand-written
class literals, every positive assertion is whole-line membership in `out.splitlines()`, and the
`APPLY` site additionally pins the stored sentence against a literal rather than only against
stdout.

**My own mutation probes (`R8`, `E4`).** Six. `run_bind_v2.py` digests
`dcd3a3efedb30d5ee220c980d54a20e3207636b14be4346173e234464ea889d2` at `38038ec` and
`a430f83ee397f8957dd7a4ba9ebdc41311139e320675d59959e3558c3d10441b` at `1f6a5a5` — the second is
exactly the restore target the fix's body names for its own probes, and the first is exactly the
digest the FULL recorded, which corroborates both records independently of my believing them.
Every probe below was restored to `a430f83e…` and `sha256sum -c`-verified before the next one.

| # | mutation (engine only) | result |
|---|---|---|
| 0 | the **whole pre-fix template** (`dcd3a3ef…`) put back under the new tests | **4 red** — all three positive members of the new class, plus the pre-existing candidate-act assertion the fix reworded; the three negative controls green |
| 1 | site `:384` forced back to the unconditional report | **1 red** — `test_a_second_pass_on_a_blocking_round_zero_reports_no_transition`, and nothing else |
| 2 | site `:425` the same | **1 red** — `test_a_second_pass_with_no_decision_yet_reports_no_transition` |
| 3 | site `:460` the same | **1 red** — `test_the_apply_pass_reports_no_transition_and_stores_its_own_instruction` |
| 4 | the field-update `save` deleted, back to a pure no-op | **1 red** — the same `APPLY` test, on its stored==printed half |
| 5 | `emit_reviewed` returns `False` on the transition path — the `emitted` line **gone** rather than conditional | **7 red**, including all three one-pass negative controls |

Probe 0 is the one that matters most: the new guard goes red against the exact bytes the FULL
reported the defect in, so it binds the reported defect and not a paraphrase of it. Probes 1–3
show the three sites bound **independently** — each isolates its own test — which is what `E7`
at the class asks for and what one shared assertion would not have given. Probe 5 is the
negative controls' own proof: they are not decoration, they go red the moment the emitted line
stops being printed at all, which is the failure a careless fix would have produced.

`R4`'s ceiling stands: mutation proves these tests have binding force, never that their force is
sufficient.

**One sentence in the fix's own account generalises one site too far — reported as an accuracy
note, not a finding.** The body says both halves are asserted at each of the three sites. They
are *written* at each site, but at sites `:384` and `:425` the stored==printed half cannot fail
on its own: pass 1 and pass 2 compute the same sentence there, so the equality already held
before the fix. Probe 4 measures exactly that — deleting the field update turns one test red,
the `APPLY` one, the only site where the two sentences differ. The body says as much about the
blocked branch ("there pass 1 and pass 2 store the same words so only the false report
survives") and then states the general form. Nothing in the tree is wrong: the guard is as
strong as probe 4 shows, and the false-report half binds at all three sites.

### `L-1` — closed, both halves

**The module now states its ceiling.** `test_disposition_reachability.py`'s module docstring
gains a paragraph naming what property 1 does not watch, and `enumerated()`'s docstring gains
three lines pointing back at it. I re-measured the two factual claims it makes rather than
reading them:

```
enumerated families: ['final', 'full-verdict', 'verify-verdict']
total rows: 13
prose-named rows   : ['STOPPED_REPLAN', 'repair-leg-after-CHANGES_REQUIRED',
                      'repair-leg-after-REVIEWED_NO_BLOCKER',
                      'ACCEPT_WITH_LIMITATIONS-from-residual-uncertainty']
```

Three families and no more; thirteen rows, nine enumerated and four prose-named — the four the
docstring names, exactly. The route it singles out as the row round 2 owes checks out too:

```
$ sed -n '98,100p' document-harness/EXECUTION.md
There is one repair. If a blocker still stands after the VERIFY, the run stops — the honest
dispositions left are `STOPPED_REPLAN` or a user `ACCEPT_WITH_LIMITATIONS` that names what is
still open.
```

And the decision to add no `no-path` row is right on the finding's own terms: property 4 makes a
`no-path` row oblige its named rule site to carry the absence in its own text, those sites are
`E10` members, so writing one is design and design opens a round (`E10`).

**The over-claim is corrected forward.** `887c576`'s body still reads, word for word,
``No row is `no-path` today -- every disposition the rules name is now reachable`` (checked with
a grep over that commit's message). The correction is a new paragraph in `1f6a5a5`'s body naming
the counter-example, the original untouched — which is `HD-59`'s prescribed form, a forward
entry that leaves the earlier judgement greppable, not a workaround of it.

### `L-2` — closed

The finding asked for one sentence naming `tooling/rsclib/document_harness/review.py` as written
outside the plan's In list, and why. `1f6a5a5`'s body carries it, with the shelf argument
restated. I re-checked the underlying fact rather than the sentence: the plan's In list
enumerates at file granularity and names `flow.py` and `review_result_v2.py` but not
`review.py`, so the escape is real and the disclosure is accurate. `E9`'s "never silently" is
now satisfied for this round.

## 4. The whole repair diff — anything the findings did not ask for

`R3` makes the entire repair diff my subject, not only the accepted findings. Walking it:

- **`run_bind_v2.py`, +42 −24.** Four hunks and no fifth: `emit_reviewed`'s docstring and its
  already-`REVIEWED` branch; the three call sites; and the candidate act's resumed-position
  line, reworded to add `next_action updated`. Nothing else in the module moved — no other
  function, no import, no constant.
- **`test_run_v2_template_bind.py`, +141 −2.** The new class, plus the two-line rewording of the
  pre-existing assertion that quoted the line the fix changed. That edit is named in the body
  rather than folded in silently, which is what `E9` asks at a boundary edge; and it does not
  weaken the assertion — probe 0 turns it red against the pre-fix template, so it still binds,
  and it now pins the new wording as well.
- **`test_disposition_reachability.py`, +26 −0.** Docstrings only; no test added, none changed.
  That accounts for the whole battery delta: 938 − 932 = 6 = the new class's six methods.
- **The docstring rewrite of `emit_reviewed`** is the one change no finding asked for by name.
  It is the fix's own obligation rather than scope creep: the old docstring's central claims —
  that already-`REVIEWED` is a **no-op**, and that "the caller says on stdout which of the two
  passes this is" — are false of the new code at the first and were false of the old code at the
  second. Leaving it would have left the module asserting what the fix had just made untrue.

**`E6`, both clauses, checked because a repair is where they bite.** The finding named code as
wrong and the code changed — no rule was added about it, no guard was added in place of the fix,
and nothing derived, computed or convenient was introduced. There is no new machinery in this
diff at all: one `save` call, three `if`s, three `else` branches, and a test class.

## 5. Permanent boundaries, however narrow the round

| boundary | how checked | result |
|---|---|---|
| `E2` announced surface | alarm re-run on the range + hand classification of all four paths | clean; no announced path in the range |
| `E10` instruction layer | the four changed paths against the seven-member list and this repository's declared rules file | no member touched; no amendment owed |
| `E10` path resolution | `python tooling/sweep_refs.py` | exit 0; 13 NAMETOK bare-name references, all the compliant caller-held form, none introduced by this range |
| `E8` git form | titles, `Kind:` lines, trailer grep, explicit paths implied by the four-path diff | conforming |
| `E9` budget | records directory enumerated; range holds exactly the record + the fix | FULL · one fix · this VERIFY — no leg double-spent, no round renamed |
| `E9` change boundary | plan's In list vs the three written files | inside |
| `E3` measure-last | battery re-run at the verified worktree digests immediately before §6's claim | green |
| `E4` / `E5` guard discipline | six independent probes; expectations are hand-written literals asserted whole-line | binding |
| `R6` record channel | `.harness/scan-surfaces.json` → `review_record_dirs: ["migration/document-work-assurance-v3/"]` | this record written there, left uncommitted |

## 6. The battery

Re-run immediately before this claim, at the worktree digests below and with
`git status --porcelain` showing only the two pre-existing untracked entries:

```
$ git rev-parse HEAD
1f6a5a54f5a1a9968a3cec570b4b6041bb46313d
$ sha256sum assurance/templates/run-v2/run_bind_v2.py \
            tooling/tests/document_harness_review/test_run_v2_template_bind.py \
            tooling/tests/document_harness_review/test_disposition_reachability.py
a430f83ee397f8957dd7a4ba9ebdc41311139e320675d59959e3558c3d10441b *assurance/templates/run-v2/run_bind_v2.py
d62ed075011ef45a1dfbf259f7ea5d0602aceccb44d6465ad49909f3a3d3ba0b *tooling/tests/document_harness_review/test_run_v2_template_bind.py
65a2e707dd3b059a09247a32935e04b1c65e78c6a399919aab95471d74de0ecd *tooling/tests/document_harness_review/test_disposition_reachability.py
$ python -m pytest -q
938 passed in 194.67s (0:03:14)
```

That reproduces `1f6a5a5`'s claim of 938 passed. Every test lives under `tooling/tests`
(`find . -name 'test_*.py'` outside it returns nothing), so the repository-root invocation CI
uses and the `tooling/tests` invocation the round's bodies quote collect the same set. The
`932 before` half of the fix's `E3` line I did not re-measure by checking out the parent; it is
corroborated instead by the FULL's own independent run at `38038ec` (932 passed) and by the
delta being fully accounted for in §4.

## 7. Observations — `R5`, for the user, not for me to conclude

Neither is in the repair diff. Both were measured here, not reasoned.

### `V-O-1` — `emit_reviewed` guards on one status, not on transition legality; an `AWAITING_FINAL` state walks back through `REVIEWED`

The helper special-cases `REVIEWED` and treats every other status as a transition to take.
Reached with an `AWAITING_FINAL` state it therefore writes `REVIEWED` — a step
`flow._SUCCESSORS["AWAITING_FINAL"]`, which is `('CLOSED',)`, does not admit — and returns
`True`:

```
state after a completed bind : AWAITING_FINAL
emit_reviewed(AWAITING_FINAL) returned: True
state.json status now                 : REVIEWED
```

In a real re-run of the bind step the run walks straight back out to `AWAITING_FINAL`, so the
committed artifact ends where it started and nothing is lost — but the illegal step reaches disk
on the way:

```
pass 1: exit=0 status=AWAITING_FINAL
pass 2: exit=0 status=AWAITING_FINAL
pass 3: exit=0 status=AWAITING_FINAL
```

**This predates the round and is untouched by the repair.** The same three passes on the pre-fix
template (`dcd3a3ef…`) behave identically, and before `387edc2` created the helper the candidate
act advanced to `REVIEWED` unconditionally at the same place — the shape is older than
`emit_reviewed`. `B-1`'s property is not violated by it either: the helper returns `True`
because it really did write. I report it because the fix's new docstring now makes a positive
claim about *when a transition is owed*, and that claim is answered by a status test rather than
by a legality test; whether the guard should be widened, replaced by a legality check, or left
alone is design, and the question and the conclusion are the user's. If it is not taken up, its
home is the instrument's own rider bank (`R10`).

### `V-O-2` — on the candidate act the new field update is written and superseded inside the same block

Putting the `save` inside the shared helper means the candidate act's second pass now writes
`state.json` twice, the first write overwritten before the step returns:

```
pass 2 writes to state.json: 2
  write 1: REVIEWED / next_action=controller binds the AssuranceCandidate for th…
  write 2: AWAITING_FINAL / next_action=user FINAL decision (ACCEPT / ACCEPT_WITH_LIMI…
final status: AWAITING_FINAL
```

So the words `next_action updated` in that branch's printed line describe a value no later
reader of `state.json` can find — accurate at the instant, uninformative about the artifact. On
the three `R10` sites the same phrase *is* the end state, which is why it is right there and
merely idle here. The alternative shapes (drop the phrase at this one site; or have the
candidate act skip a field update it is about to overwrite) both cost more than they buy on
their face, which is why this is an observation and not a low.

### Still open from the FULL, carried forward rather than re-raised

- **`L-3`** — the plan's *Resume pointer* still reads "steps 1–2 done, next act = step 3", Steps
  3 and 4 are unchecked, and `document-harness/journal/promise-path-engine-2026-09-02.md` is
  still untracked at this tip. That is the state the FULL described, and the finding's own
  minimum fix routes it to the closeout, which cannot land until this record does; it is not a
  new condition and not this leg's to close. One line here only so the closeout is not the first
  place anyone checks: `HD-69`'s executor session id, and the fuller account of both the
  2026-09-02 and the 2026-09-03 rulings, still live only in the worktree.
- **`O-1`–`O-4`** — the FULL's four observations remain unruled; the round journal records them
  as owed to the user before closeout.

## 8. Coverage and ceilings (`R4`)

- **Read in full:** both commit bodies; the diffs of all three repaired files; the FULL record
  `v3-review-full-38038ec.md`; `document-harness/RULES.md`;
  `document-harness/CONSTRUCTION-CHECKLIST.md`; `harness.json`; `.harness/scan-surfaces.json`;
  `emit_reviewed`, all four of its call sites and the candidate act in the current template;
  `document-harness/plans/promise-path.plan.md`; the untracked round journal; `HD-59` and
  `HD-69`.
- **Read in part:** `document-harness/REVIEW.md` (the two-rounds table, *What every result must
  carry*, *Where the result lives*); `CONSTRUCTION-LEDGER.md` (header block and current
  pointer); `HARNESS-DECISIONS.md` (`§live`'s entry list plus the two entries above);
  `assurance_state.py` (`advance` / `save` / `check_state` / `pointer_for`);
  `test_run_v2_template_bind.py` (the two classes this repair touches, in full; the rest by name
  index); `test_disposition_reachability.py` (the changed docstrings and the table); the
  pre-`387edc2` bind template (the candidate-act block only).
- **Not read:** `document-harness/EXECUTION.md` beyond `:96-102`;
  `document-harness/ORCHESTRATION.md`; contract v4; the two archives; `CONSTRUCTION-INDEX.md`;
  the round's other six commits, whose subject was the FULL's and not mine.
- **Executed:** the full battery twice (once on arrival, once immediately before §6's claim);
  six mutation probes with digest-verified restores; the announced-path alarm; the
  instruction-layer reference sweep; the reachability module's enumeration introspected
  directly; the `AWAITING_FINAL` re-entry and the double write of `V-O-1` / `V-O-2` driven
  against real fixtures on both the fixed and the pre-fix template.
- **`UNVERIFIABLE`, stated rather than folded into supported:** that the user's ruling of
  2026-09-03 was given as option (ii) with option (i) offered and not taken — the `R7` ceiling
  of §2. That the repair was written by the same executor session resumed under `HD-69` — a
  process claim, marked and not verified; what I can corroborate is that the file at `HEAD`
  carries exactly the digest the fix's body names as its probes' restore target. That the `E4`
  probe *procedures* the body describes were carried out as written; what I do corroborate is
  that the guards it claims to have proven go red under my own independent mutations, in the
  same places and with the isolation it claims.
- **Platform ceiling:** measured on Windows with CPython 3.13. The CI matrix's Ubuntu legs and
  its 3.12 legs were not exercised here.
