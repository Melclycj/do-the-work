# FULL review — subject `464b7dce749d02ff29b2c07635ed151fe4cdc950..ad0663da83a3cef9bbdcd9056a727260eb917643`

**Verdict: `CHANGES_REQUIRED`** (2 blockers · 2 low · 6 observations).

Dispatched with the charter `migration/document-work-assurance-v3/v3-harness-review-contract.md`,
a stub; its operative successor `document-harness/CONSTRUCTION-CHECKLIST.md` was read end to end
as both the standing instruction and its own counterpart, per that file's own opening.

## 0. What I derived, and from what (`R2`)

The dispatch handed one range and nothing else. Everything below is re-derived here.

**The range holds six commits**, oldest first — `git log --format='%h %s' 464b7dc..ad0663d`:

| # | sha | title | kind, as its own body names it | files |
|---|---|---|---|---|
| 1 | `580d236` | `V3-FREEZE-TO-ALARM-AMEND-M1-v1` | amendment (`E10` must-fix channel) | `CONSTRUCTION-CHECKLIST.md` |
| 2 | `a2d3fb4` | `V3-FREEZE-TO-ALARM-B-v1` | candidate | `CONSTRUCTION-CHECKLIST.md` · `HARNESS-DECISIONS.md` |
| 3 | `184387c` | `V3-FREEZE-TO-ALARM-A-v1` | candidate | `CONSTRUCTION-CHECKLIST.md` |
| 4 | `1d4d9aa` | `V3-FREEZE-TO-ALARM-C-v1` | candidate | `ci.yml` · `announced_path_disclosure.py` · its test |
| 5 | `0355b36` | `V3-FREEZE-TO-ALARM-E-v1` | candidate | `HARNESS-RIDERS.md` |
| 6 | `ad0663d` | `V3-FREEZE-TO-ALARM-ERRATA-v1` | errata / pre-submission correction | `CONTRACT-V4-SIGNATURE.md` · `HARNESS-RIDERS.md` |

`git diff --stat` over the range, classified by hand: 7 files, 501 insertions, 31 deletions —
one workflow file, one new script, one new test, two register files, one instruction-layer
member, one signature record.

**The round.** Batch `FREEZE-TO-ALARM`, plan `document-harness/plans/freeze-to-alarm.plan.md`,
which that file's own header declares the carrier of the six user rulings of 2026-08-27 and of
the four answers that gated the opening. Work items A · B · C · D · E; this range delivers
A, B, C, E and not D.

**The budget.** `E9`: one FULL, at most one user-approved fix, one targeted VERIFY. Applying
`E9`'s own test — *has a valid independent FULL already occurred?* — the answer at the subject
is no: the only review record the round holds is the opening cold read `v3-cold-read-860401e.md`
(record commit `464b7dc`, the range base), which `E10` says is never banked as the round's FULL.
So **this is the round's FULL**, `580d236`'s amendment pair spends nothing (`E10`), and
`ad0663d` is correctly self-classified as a pre-submission correction obliging no VERIFY.

**Authorization.** Six rulings of 2026-08-27 plus four question-answers, all in the plan; two
further rulings of 2026-08-28 carried by `ad0663d`'s body. I can see all of these in the
repository. What I cannot see (`R7`, stated as a ceiling, not a block): any record that the
`E11` preview card was rendered and the user waited, and any record of item D's authorization.

**The review window.** `.harness/review-pending.json` records `dispatched_at`
2026-08-27T15:50:50+00:00; `ad0663d` is dated 2026-08-28 01:49:38 +1000 = 2026-08-27T15:49:38Z,
72 seconds before dispatch. No commit has landed inside the window. `git status --porcelain`
reports one untracked path (`.goals/`) and no modified tracked file, so the worktree bytes I
read are the subject's blobs.

---

## 1. The implementation (`R3` — this first)

### 1.1 The alarm binds, and I reproduced its numbers rather than accepting them

`tooling/announced_path_disclosure.py` does what its docstring and `1d4d9aa`'s body claim.
Read end to end; every figure below is from a command run here.

**The watched set is right.** `ANNOUNCED` holds sixteen paths: contract v4 plus fifteen
schemas. `git ls-files schema/document-assurance-v3/ | wc -l` returns **15**, and the fifteen
names match `ANNOUNCED`'s fifteen one for one. The test's `EXPECTED` is an independently
hand-written sixteen asserted as a whole tuple — `E5`-shaped, not read back from the module.

**The predicate is naming test (a), not the dominated (b).** `undisclosed()` searches the whole
message (`%B`) for the full repo-relative path. The docstring states that ceiling in its own
text rather than leaving it inferred, and states why the looser subject-line surface is vacuous
under `E8`'s title form. It also states the ceiling `E2` states: that a message names a path is
all this proves.

**Reproduced against real history, from a different direction than the plan's measurement.**
Driving `commits_to_judge`/`undisclosed` directly with the floor suppressed, over
`<root commit>..ad0663d`, **223 non-merge commits judged** and exactly **four red commits** —
`39a21a8`, `23ca45b`, `d0f185c`, `1656e59` — with `07ef526` green. That is `1d4d9aa`'s claim,
independently re-derived. With the floor live (`alarm_floor` → `1d4d9aa`), the same range
judges **2** commits (`0355b36`, `ad0663d`), both green: the floor works and history is not
re-judged.

**The battery.** `python -m pytest -q` here printed **`813 passed in 144.19s (0:02:24)`** — the
count `1d4d9aa` and `0355b36` claim. `tooling/tests/document_harness/test_announced_path_disclosure.py`
alone: `18 passed`. `layer_path_check.py`, `candidate_path_check.py` and `review_freeze_check.py`
each exit 0 on this tree, and the nine `E10` members resolve **9/9**.

**Mutation, run by me (`R8`, `E4` protocol: copy to a scratch file, mutate, run, restore,
re-hash).** Baseline sha256 of the script is
`242cc3818272a51a758280855c3f99f41427e249e7d78113023d7b99b0e61638` — the same baseline
`1d4d9aa`'s body records, which is itself a check on that record. Restored and re-hashed to the
baseline after every mutation; final hash equals baseline.

| mutation (real defect shape) | result |
|---|---|
| basename instead of the full path — the declined naming test (b) | **1 failed**, 17 passed |
| floor never applied (`if False:`) | **1 failed**, 17 passed |
| `%B` → `%b` (body only, subject dropped) | **2 failed**, 16 passed |
| `--no-merges` dropped from the range walk | **2 failed**, 16 passed |
| `alarm_floor` returns the newest add (`added[0]`) instead of the oldest | 18 passed — **not bound** |
| match made case-insensitive on both sides | 18 passed — **not bound** |

The four that matter bind. The two that do not are recorded as `O-6`; neither is a defect shape
I can construct a realistic path to.

**`E6` is answered rather than bypassed.** The question `E6` asks — what decision changes if
this is absent — has a real answer here: the disclosure `E2` now requires would have no
enforcement of any kind. This is the enforcement leg of a rule written the day before, not new
machinery added to close a finding about existing text.

**`pack_digests()` is correctly not used**, and the reason given is a measurement rather than a
preference. I checked it: the function returns one aggregate digest over the contract plus the
whole pack, read from the working tree, and the sentence the alarm must print names *which*
file *which* commit changed. `git grep -n 'pack_digests' -- '*.py'` returns the definition
(`tooling/rsclib/document_harness/__init__.py:238`), the `__all__` export (`:266`), and one
prose line in the new script explaining why it is not used — a mention, not a call. The thing
`HD-27` refused three times is still not done.

### 1.2 The instruction text does what it claims

`E2` (`184387c`) delivers ruling 1 and question 3's answer: a gate becomes an announcement,
disclosure is owed after the fact site by site in the commit body, the blob literals are
dropped, the clause states its own ceiling in its own text, and a bridging sentence keeps
*frozen* readable as the older name for the set. What the plan required kept is kept — one
path plus one directory as of the 2026-08-03 re-baseline, no auto-enrolment, a path outside
the list still not covered.

`B` (`a2d3fb4`) deletes both `E2` carve-outs and flips `HD-20` to `retired` in one commit, which
is what the plan required and what rider `wl-route` measured the cost of splitting. I re-ran the
commit's own sweep pattern (`E2. also freezes|owe .E2..s recorded ruling|overrides the channel`)
over live rule text: zero hits. Both edited sentences read correctly after deletion.

`E` (`0355b36`) delivers ruling 5. Acceptance 7 re-run here: `grep -c 'E2` 写入裁决'
HARNESS-RIDERS.md` → **0** (it returns **3** at the pre-batch base `51553bd`), and
`grep -c '下一个持有' HARNESS-RIDERS.md` → **0**. All four touched rows still name a target and
a touch condition; the three deadlines are unchanged.

`580d236`'s amendment is correct. The old terminus is genuinely gone —
`grep -c -i 'bytes came from' README.md` → **0** — and the new one exists and says what the
clause now says it says: `CONSTRUCTION-LEDGER.md:32` names the source repository as a
single-machine worktree path (`D:/Thesis`, worktree `D:/Thesis-stage-control-refactor`), and
the dropped half-claim ("says why the history stayed there") is dropped rather than written
onto a terminus that does not carry it. Both deferral facts are recorded in the body as `E10`
requires.

`ad0663d`'s second half corrects `CONTRACT-V4-SIGNATURE.md` forward per `HD-59`, original left
standing. Its two measurements reproduce here: the `E2` clause carries no hex literal, and
`obtain the ruling and write under it` returns 0 in the checklist. Its class sweep also
reproduces exactly — the same pattern over the same declared scope returns two hits,
`CONTRACT-V4-SIGNATURE.md:14` (corrected beside) and `HARNESS-RIDERS.md:13` (rider `PD`'s
history cell). Its freshness claim reproduces: `git diff --name-only 184387c..0355b36` returns
the four files it names.

### 1.3 Where the implementation does not reach

Two blockers below are not about the alarm's code, which is sound. They are about two texts
the round left standing that now contradict what the round did — one of them a text that
outranks the clause the round rewrote.

---

## 2. Findings

### Blockers

**`B-1` — `HD-44`, `§live`, still rules that changing the announced bytes owes a recorded
ruling, and `§live` outranks the clause item A rewrote.**

*Location.* `HARNESS-DECISIONS.md:65`, inside `HD-44` (`:51-67`, `2026-08-18 · user · scope:
standing · status: **live**`):

> 今后任何调用者删掉自己那份副本，按本条同样不欠裁决；**真的改动那些字节仍然照旧欠裁决**，
> 本条一个字都没放宽那一半。

*What is false.* Item A ended exactly that requirement. After `184387c` the announced paths may
be written and what is owed is post-hoc disclosure. `HD-44:65` says the opposite, in the present
tense, as a live standing ruling.

*The ground truth it violates.* Two texts, agreeing. `HARNESS-DECISIONS.md`'s own header:
「instruction 层反向 base on 这里的裁决展开细则；**细则与裁决冲突，细则错**」. And `E10`'s
closing clause, which owes `§live` at every round's opening whether or not the layer read is
waived, and calls it "the user's standing rulings, which this text expands under and **which
outrank it on conflict**". So this is not a stale mention in a peripheral file: it is the
higher authority saying the round's central deliverable is not in force.

*The downstream decision that goes wrong.* Ruling 5 rewrote three rider rows —
`sig-write-once`, `contract-wikilink-tier`, `v1-digest-recipe` — to redeem by *writing directly*
to `contract/Document-Work-Assurance-Contract-v4.md` and
`schema/document-assurance-v3/review.schema.json` "with the next batch", naming the path in the
commit body. That next batch's opening is obliged to read `§live`. It will meet `HD-44:65`,
apply the conflict rule the register states, and conclude the write still owes a recorded
ruling that ruling 1 abolished. That is the deadlock ruling 1 exists to end, reinstated one
file over.

*Why the round's own sweeps did not catch it, which is the reason to fix the class and not the
instance.* Item A's class sweep pattern was
`not written without a recorded user ruling|obtain the ruling and write under it|owe .E2..s recorded ruling|E2. 写入裁决|无裁决写入`,
re-declared verbatim by `ad0663d`. `HD-44:65`'s phrasing is 「欠裁决」, which none of those five
alternatives matches — an English-plus-two-Chinese-forms pattern missing a third Chinese form.
The repository has recorded this same pattern-coverage failure twice before (round
`PRERUN-RIDERS`'s journal; `RIDER-SETTLEMENT`'s `V-3`). Worse, the site was *visited*: item B's
body names "historical basis references in `HD-44` and `HD-57`" and leaves them standing. That
is right about `:67`, the basis line citing `HD-20` as precedent. It is the 裁决 body at `:65`
that is live and wrong, and it was not assessed.

*Minimum fix.* Only the user flips a decision's state (`HD-2`, and the register's own
invariant), so the round cannot do this by itself: put ruling 1's effect on `HD-44` to the user
and land the answer. Two admissible shapes, and the choice is the user's — either `HD-44` gains
a successor under `HD-30`'s partial-narrowing mechanism carrying the corrected full text
(original to `superseded`, both in the same commit), or `HD-44`'s status parenthesis records
that its last clause was narrowed by the 2026-08-27 ruling with the clause left standing per
`HD-59` and the correction written beside it. Either way, re-run the sweep with 「欠裁决」 and
「欠 `E2`」 added to the pattern set and paste the output (`HD-41` ④), because the class is
"live text asserting `E2` requires a ruling before a write" and this instance proves the
declared pattern did not cover it.

*Adjacent, same entry, not the blocker.* `HD-44:52-54`'s status parenthesis quotes `E2` as
「三个 blob 加一个目录」. That was already stale from round `CONTRACT-V4` (three blobs became
one) and item A makes it stale a second way (one becomes none). It rides the same fix.

---

**`B-2` — the two durable records a cold session is told to read first both state that this
round has not opened and that no work item has been executed.**

*Location.* `document-harness/plans/freeze-to-alarm.plan.md:3`, `:362-372`, `:458-459`; and
`CONSTRUCTION-LEDGER.md:210`.

- Plan `:3` — "**Status: batch scoped, no round open.**"
- Plan `:362-372` — steps 3 through 8 all `[ ]`, including "3. Open the round", "4. Execute item
  B", "5. Execute item A", "6. Execute item C", "8. Execute item E".
- Plan `:458-459` — "当前指针: **steps 1 and 2 done … No round is open and no work item has been
  executed.**"
- Ledger `:210` — "**▶ 队首已立项为批 `FREEZE-TO-ALARM`（2026-08-27，尚未开轮）**".

*What is false.* The round opened (its cold read is `464b7dc`), and items B, A, C and E have
landed as `a2d3fb4`, `184387c`, `1d4d9aa`, `0355b36`. `git diff --name-only 464b7dc..ad0663d`
contains neither file: **neither carrier has moved once in six commits.**

*The ground truth it violates.* The plan's own header contract — "A cold session reads this
file, then `CONSTRUCTION-LEDGER.md`'s current pointer, then works" — and the same header's own
statement of why that matters, that a ruling which never reaches a commit is a ruling the
reviewer cannot check (`R2`). This is the inverse of that failure: what reached the commits is
right, and the file the cold session is sent to first contradicts it.

*That this is the repository's own practice, not an obligation I am inventing.* The immediately
preceding batch ran a dedicated round-open commit that did exactly this work before any item
landed: `d3cda1a` (`V3-CORE-SET-ROUND-3-OPEN-v1`) touched `core-set.plan.md`,
`CONSTRUCTION-LEDGER.md` and `HARNESS-RIDERS.md`; `f5e1bc0` (`V3-CORE-SET-ROUND-2-OPEN-v1`)
did the same for round 2. `git log d3cda1a~1..418477a -- document-harness/plans/core-set.plan.md`
returns exactly two commits — the round-open and the closeout — so the plan carried "round is
open" for the whole of round 3. Batch `FREEZE-TO-ALARM` has no round-open commit at all.

*The downstream decision that goes wrong.* `HD-55`'s role form dispatches cold sessions. A cold
executor or a cold orchestrator resuming this batch reads the plan, is told no work item has
been executed, and re-executes item B or item A over text that has already changed — or the
closing orchestrator reconciles a round the ledger says never opened. The round is at exactly
the point where a fresh session is most likely to pick it up.

*Minimum fix.* One commit: set the plan's Status line and resume pointer to the measured state,
tick steps 3–6 and 8 naming the commit that landed each (the shape `core-set.plan.md`'s own
`[x]` entries use), and correct the ledger's queue-head line from 尚未开轮. Nothing about the
work needs to change.

### Low

**`L-1` — after item A, the sixteen announced paths are enumerated nowhere in this repository
except the guard's own list and its test twin, and the prose leg has no guard.**

*Location.* `document-harness/CONSTRUCTION-CHECKLIST.md` `E2`; `tooling/announced_path_disclosure.py:56-73`;
`tooling/tests/document_harness/test_announced_path_disclosure.py:53-70`.

*What is true.* `E2` names its set by reference — "every file the `schema/document-assurance-v3/`
pack held at the 2026-08-03 re-baseline (fifteen files: the fourteen of the 2026-07-29 entry
plus `paragraph-map.schema.json`)". Neither referent is reachable here. This repository's first
commit is `345acdd`, dated **2026-08-15** (`git log --reverse | head`), so the 2026-08-03 pack
state predates its history entirely; and `git grep -n '2026-07-29' -- HARNESS-DECISIONS.md
HARNESS-DECISIONS-archive.md` returns nothing enumerating fourteen schemas — the 2026-07-29
entry lives in the extraction-source repository. `HD-44:56` carries the count 「十五件」, not the
names. Item A then dropped the one literal that *was* checkable here (contract v4's blob), under
question 3's answer, and `CONTRACT-V4-SIGNATURE.md` records the **signed** blob, not the current
one.

So `ANNOUNCED` and its test twin are now the only enumeration of the set in this repository,
and they are pinned to each other and to nothing else. That is the `E10-sync` shape one surface
over — three copies, the prose leg unguarded — and this repository has mutation evidence in
that rider that a prose leg goes green when it is broken. `1d4d9aa`'s body invokes the
`test_precommit_checks.py` `EXPECTED` precedent by name and inherits its known gap without
noting it. Today the set is recoverable because the pack happens to hold exactly fifteen files.

*The decision that goes wrong.* The first time the pack gains or loses a file, an executor
asking "is this file announced?" has no repository-resolvable answer from `E2` and reads it off
the guard — the guard becomes its own authority, the inversion `E5` exists to prevent and which
the round deliberately avoided at the test level. If instead a re-baseline enrols a schema in
`E2`'s prose and `ANNOUNCED` is not updated, the alarm silently stops watching it and nothing
goes red.

*No bytes supplied, deliberately.* The two candidate fixes are a drift test (asserting
`ANNOUNCED`'s fifteen equal `git ls-files schema/document-assurance-v3/`, so a pack change goes
red and forces a deliberate re-baseline decision — note this is not the directory-listing
`ANNOUNCED` correctly refuses, which would make the expectation a function of the guarded
thing) and a bank row. Which, or neither, is a design call under `E6`, so it routes to `R10`'s
bank rather than the free channel.

---

**`L-2` — item C falsified `split-design.md` §5 and ran no class sweep; §5 is the surface rider
`PD`'s new redeem-when names.**

*Location.* `document-harness/split-design.md:119-133`, §5 「`pack_digests` 与 `E2` 守卫」.
Two of its three 提议 bullets are now false:

- `:127` 「**`E2` 维持不加守卫**」 — item C added machine enforcement to `E2`.
- `:132` 「rider `PD` 因此**兑付**（两半都有归宿：守卫不加、函数删）」 — `PD` was not redeemed.
  Item E re-scoped it and it is still row `PD` in `HARNESS-RIDERS.md`.

*What makes it more than a stale doc.* Item E's rewritten `PD` row points its redeem-when at
this very section — 「下一批碰 … `document-harness/split-design.md` §5 那条删除提议的批」 — so
the bank sends the next executor to a section that says the bank row is already redeemed and
that `E2` has no guard. The bank and the surface it names contradict each other.

*Why it survived.* `1d4d9aa` is the only commit in the range that ran **no** class sweep;
A, B, E and the errata each ran one. The class item C creates is "live text asserting `E2` has
no machine enforcement". I ran it — `git grep -n '维持不加守卫\|零机械 enforcement\|零机器'`
over tracked text excluding `migration/`, journals, archives and plans returns **four** lines:
`HARNESS-RIDERS.md:13` (rider `PD` — corrected by item E), `split-design.md:127` (this
finding), and `HARNESS-RIDERS.md:17` / `:28` (riders `delta-prose` and
`template-clause-unguarded`, both about other guards entirely and not in the class). So the
class holds two instances, one already corrected and one not; the plan's own `:149` is excluded
as a record.

*Weighing it down rather than up, honestly.* `split-design.md`'s header declares that sections
deliberately keep 「初稿的提议与被推翻的读法」 for traceability, with §10 governing on conflict —
and §10's table does not carry §5. So an overturned §5 proposal sitting there is within that
file's declared convention, which is why this is low and not a blocker. What the convention does
not cover is the contradiction with the live bank row, and the same file's own practice
elsewhere (§10.2's 「re-read 2 `M-1`(a)」 note, §10.4's 「**更正（R0 read `L-3`）**」 block) is to
write the correction beside the falsified text.

### Observations

**`O-1` — item D is absent, so the mechanism question 1 settled does not yet exist, and one
thing the plan required be *recorded* was not.** `1d4d9aa`'s body discloses that item D is not
its own and that until it lands the job "runs and reports but cannot block", and that
`on: pull_request` runs the workflow from the PR's own head. Measured here: `git rev-parse
origin/main` is **`0355b36`** — the errata is unpushed, and the round's commits went straight to
`main`, so the PR flow question 1 settled has not been adopted for this round's own work.
Separately, plan item D requires the round to "**Decide and record** whether protection is
applied before or after the round's own commits land". Two commit bodies (`1d4d9aa`, `0355b36`)
mention item D, and both say the same thing — that it is not in this commit, is not this
session's, and needs a repository-settings change the user runs. Neither states the before/after
decision, and `grep -c -i 'before or after the round'` returns **0** on both the plan and the
ledger. The decision the plan asked to be recorded is unrecorded. Acceptance 6 (read the protection endpoint back) is
**`UNVERIFIABLE`** from here — `gh` is not available to this session — and I am not folding it
into supported (`R4`). Whether item D belongs to this round or is severed from it is the user's,
not mine (`R5`); what I can say is that the round's own acceptance list is not met and the
alarm's teeth do not exist yet.

**`O-2` — the alarm's YAML wiring is unexercised by any test and unobserved by me; acceptance 5
asks for the job, and what exists is the script.** Acceptance 5 reads "a scratch commit touching
a frozen file **without** naming it in the body makes **the job** red; the same change **with**
the body naming the site makes it green. Paste both runs." What `1d4d9aa` pastes is the script
over real history (4 red / 1 green) plus the 18-test matrix and six mutations — strong evidence
for the *predicate*, none for the *wiring*. `git grep` finds no test anywhere that reads
`.github/workflows/ci.yml`. I read the YAML and the two expressions evaluate correctly under
GitHub's semantics on both events (`github.event.before` is absent on `pull_request` so the
`||` falls through; `github.event.pull_request` is null on `push` so property access yields
null), and inputs reach the script through `env` rather than `run:` interpolation, preserving
the repository's measured no-expression-in-shell posture. I could not run it. Note that renaming
or deleting the job fails *closed* once item D lands — a required check that never reports
blocks the merge — so the unguarded name is not itself a hole.

**`O-3` — this batch has no round journal, unlike every prior batch.**
`document-harness/journal/` carries one file per batch; `FREEZE-TO-ALARM` has none, and its plan's
step list does not call for one. `E3` and `E1` both name "the commit body **or** the round
journal" as carriers, so nothing is violated — the commit bodies carry the evidence in full.
Recorded because the absence is uniform across every prior batch and a closeout may expect one.

**`O-4` — `HD-57`'s subject was deleted by item A and its state was not raised.**
`HARNESS-DECISIONS.md:184-204`, `scope: standing · status: implemented`, authorises five stale
literals to be corrected 「在 `E2`/`HD-20` 意义下」, and its 后果 records that `E2`'s v4 blob
literal was updated in the same commit — the literal item A removed. Its authorisation was
consumed at the application batch, and the `HD-20` half of its frame retired in this round. This
is the same shape as the `HD-20` flip the user ruled, one entry over; whether it should retire is
the user's (`R5`, `HD-2`). It sits in `§implemented`, which no round is obliged to read, so it
does not carry `B-1`'s conflict weight.

**`O-5` — a squash-merge under item D's PR flow would land a commit on `main` whose message no
required check ever judged.** The PR run judges `base..head`, i.e. the branch's own commits; a
squash merge replaces them with one new commit carrying the PR's title and body, which the
`push` run on `main` judges only *after* it has landed. Merge-commit and rebase-merge flows do
not have this shape (the branch commits arrive intact and the merge commit is skipped by
design). Recorded because item D has to choose a merge method and the choice is not neutral.

**`O-6` — two mutations the test matrix does not bind.** From my own run (§1.1): `alarm_floor`
returning the newest add rather than the oldest leaves 18 green — the docstring states the
oldest-is-the-floor rule and no test pins it, and the defect is reachable only if the script is
deleted and restored; and making the substring match case-insensitive on both sides leaves 18
green. Neither is a defect shape I can construct a realistic path to. Recorded so the next
reader can tell checked-and-clean from never-looked-at, not as a request for tests.

---

## 3. What I checked that held

- **`E9` budget and window.** No prior FULL in this round; `580d236`'s amendment pair spends
  nothing and its body records both deferral facts `E10` requires; `ad0663d` is correctly a
  pre-submission correction obliging no VERIFY. No commit landed between dispatch and now.
- **`E8` form.** Six commits, six single dense titles naming the round, one dense paragraph
  each, no trailers, and each body names its own kind — amendment / candidate / errata.
- **`E2` compliance by this round's own commits.** No commit in the range writes an announced
  path: `git diff --name-only` per commit returns only the seven files tabulated in §0, none of
  which is `contract/Document-Work-Assurance-Contract-v4.md` or under
  `schema/document-assurance-v3/`. The batch did not use its own goal as its authorisation.
- **`E10-sync` does not fall due.** The membership sentence is untouched by every commit in the
  range, and `LAYER` in `tooling/hooks/layer_path_check.py` is unchanged and still holds nine
  paths, all of which resolve.
- **`layer_path_check` has no `E2` exception in code.** I read `tooling/hooks/layer_path_check.py`
  end to end: `LAYER`, `TOKEN`, `PATHLIKE`, `RUNTIME_PREFIX`, `unresolved_tokens`. Nothing
  excepts the announced bytes. So `E10`'s surviving tail exception — banked this round as rider
  `e10-freeze-exception` — is prose about the blind-spot list, and the rider's reading (the
  exception drops out silently and returns no wrong answer) holds against the code.
- **The new rider row is `R10`-shaped.** `e10-freeze-exception` names its target (the `E10` list
  sentence at `:185`), carries a touch condition, names a **round-eligible** surface as `R10`
  requires of a design-shaped row, and argues its no-deadline rather than omitting it.
- **`HD-20`'s live citations after the flip.** `git grep 'HD-20'` over live non-record text
  returns six sites: `HD-44:67` and `HD-57:187,190` (basis / historical), the ledger's batch
  entry, and the three rider rows item E rewrote. All historical or corrected; `HD-59` leaves
  them standing.
- **The errata's own arithmetic.** Both halves reproduce (§1.2). Its `E9`, `E2` and `E10`
  self-classifications are each correct on re-derivation.
- **Every acceptance I could run.** 1 ✔ (the rewritten clause is there, no surviving exception
  sentence at either former site) · 2 ✔ (`HD-20` reads `retired`; `git show --stat a2d3fb4`
  shows both files) · 3 ✔ (813 passed here) · 4 ✔ (three guards exit 0, members 9/9) ·
  7 ✔ (0 and 0) · 8 ✔ (rider `PD` answered and re-scoped, not left standing).
  5 partially (§`O-2`) · 6 `UNVERIFIABLE` (§`O-1`) · 9 pending this record.

## 4. Coverage and ceilings (`R4`)

- **Read in full:** `document-harness/CONSTRUCTION-CHECKLIST.md`; `document-harness/ORCHESTRATION.md`;
  `document-harness/plans/freeze-to-alarm.plan.md`; `migration/document-work-assurance-v3/v3-cold-read-860401e.md`;
  `HARNESS-RIDERS.md`; `tooling/announced_path_disclosure.py`;
  `tooling/tests/document_harness/test_announced_path_disclosure.py`; `.github/workflows/ci.yml`;
  `.githooks/pre-commit`; all six commit bodies; the full diff of each commit.
- **Read in part:** `HARNESS-DECISIONS.md` — the header, `§live` (`HD-59`, `HD-44`, `HD-41`,
  `HD-36` opening) and the specific entries `HD-20`, `HD-55`, `HD-57`; **not** `§implemented`
  end to end. `CONSTRUCTION-LEDGER.md` — the queue-head entry and the "Where the bytes came
  from" block, not the CLOSED roll. `document-harness/split-design.md` — the header, §5, §10.
  `tooling/hooks/layer_path_check.py` — through `unresolved_tokens`, not the diff parser.
  `document-harness/plans/core-set.plan.md` — its step list only, as precedent evidence for `B-2`.
- **Probed only:** `document-harness/README.md`, `EXECUTION.md`, `REVIEW.md`, `ONBOARDING.md`,
  `CONSTRUCTION-INDEX.md`, `io-design.md`, `split-travel-manifest.md`, `CONTRACT-V4-SIGNATURE.md`,
  contract v4 and the schema pack — by targeted `git grep` around the claim under test, never end
  to end. I did **not** re-read the nine `E10` members end to end; the opening cold read
  `464b7dc` did, and only `CONSTRUCTION-CHECKLIST.md`'s blob has moved since, which I read in
  full at this tip.
- **Not run, and not folded into supported:** anything requiring `gh` — `gh run list` and the
  branch-protection endpoint are both blocked by this environment's permission layer, so item D
  and acceptance 6 are `UNVERIFIABLE` here, and the CI job has never been observed executing by
  me. `origin/main`'s position I read from the local remote-tracking ref.
- **Mutation.** Six, on the alarm, by the `E4` protocol with a sha256-checked scratch copy and a
  verified restore (§1.1). I did **not** mutate the three pre-commit guards — they are unchanged
  by this range. Mutation proves these tests have binding force on those six shapes, not that
  their force is sufficient.
- **Process claims are marked, not verified.** That this review ran in a fresh context, that the
  `E11` preview card was rendered and the user waited, that the executor sessions were cold and
  dispatched per `HD-55`, and that `E8`'s explicit-path staging was honoured — none has an
  evidence lock in the repository and none is verified here. `1d4d9aa`'s and `ad0663d`'s bodies
  make provenance statements; I record that they were made.
- **`E1`'s four-holdings disclosure.** `ad0663d`'s body says "which of `E1`'s four holdings the
  executor held is the orchestrator's statement to make and is not claimed here" — correct
  routing. No commit in the range makes that statement, and no round journal exists to carry it.
  If this round took `E1`'s exception channel, the statement is still owed; if it ran the
  three-session norm, nothing is owed. I cannot tell which from the repository.
- **`R2` compliance.** The commit set came from `git log` run here; every count, sha, grep and
  test result above was produced by a command run here; no figure was taken from the dispatch,
  a commit body, the plan or a prior record. Where I cite a commit body's number it is because
  I re-derived the same number independently, and I say so.
- **Chat-only load-bearing material: none found.** The six rulings and four answers are in the
  plan; the two rulings of 2026-08-28 are in `ad0663d`'s body. `B-2` is the adjacent failure —
  not material living only in chat, but material living only in commit bodies while the
  designated carrier says the opposite.
