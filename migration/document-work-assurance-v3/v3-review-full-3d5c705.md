# FULL review — `153302a..3d5c705` (the shared FULL: `STRANGER-PROOF` + `SUBMOD-HOOKENV`)

**Verdict: `CHANGES_REQUIRED`.** Two blockers, four lows, five observations. The code fix at the
centre of `SUBMOD-HOOKENV` is correct and I reproduced both directions of the defect it closes on
a tree the executor did not use for that measurement. Both blockers are in what the round
*recorded*, not in what it *built* — one in the audience-facing deliverable the round exists to
produce, which fails its own stated outcome when executed verbatim; one in the mutation evidence
the guard fix rests on, two of whose four signatures do not reproduce and whose summary sentence
about the must-fire controls is false.

Everything below was re-derived from the repository (`R2`). No figure in any commit body, plan or
record was accepted as given; where one is quoted it is because I re-ran the command that
produces it and the output is pasted.

---

## 1. The subject, derived

The dispatch supplied one range and nothing else.

```
$ cat .harness/review-pending.json
{
 "subject": "153302a1546a3cad91dbc552cce9edc27c123629..3d5c7050825f0d7459cb6e8c0702d3884b44562b",
 "dispatched_at": "2026-08-23T17:03:09+00:00"
}

$ git rev-parse HEAD
3d5c7050825f0d7459cb6e8c0702d3884b44562b

$ git status --porcelain
(empty)
```

**The review window is intact, re-derived rather than assumed.** The branch tip equals the
dispatched tip, and the tip commit is `2026-08-23 17:02:06` UTC against a dispatch of `17:03:09`
UTC — one minute later, nothing since. This repository's tracked hook runs `layer_path_check.py`
alone, so the window here is discipline held, not enforcement (rider `self-caller-guards`).

**Seven commits, classified by hand.**

```
$ git log --oneline 153302a..3d5c705
3d5c705 V3-SUBMOD-HOOKENV-v1                            candidate (SUBMOD-HOOKENV)
af002e2 V3-SUBMOD-HOOKENV-PLAN-v1                       plan / batch-open carrier
e620b43 V3-STRANGER-PROOF-CANDIDATE-DISCLOSURE-v1       pre-submission correction
0133d1b V3-LEDGER-DISPATCH-ECONOMY-BACKLOG-v1           declares ledger-only; carries the candidate (O-1)
be03c55 V3-STRANGER-PROOF-PLAN-ECONOMY-v1               plan amendment
001816f V3-REVIEW-RECORD-STRANGER-PROOF-153302a-v1      read record (verdictless)
912f837 V3-STRANGER-PROOF-RIDERS-BANK-v1                riders-only bookkeeping
```

**Ten paths, classified by hand.**

```
$ git diff --name-status 153302a..3d5c705
M  CONSTRUCTION-LEDGER.md
M  HARNESS-RIDERS.md
M  README.md
M  document-harness/ONBOARDING.md
A  document-harness/journal/stranger-proof-walk-2026-08-24.md
M  document-harness/plans/stranger-proof.plan.md
A  document-harness/plans/submod-hookenv.plan.md
A  migration/document-work-assurance-v3/v3-checkpoint-read-153302a.md
M  tooling/rsclib/document_harness/paths.py
A  tooling/tests/document_harness/test_submodule_paths_in_hook.py
```

## 2. Round, budget, authorization, obligations — derived

**Round.** Two work units under one FULL. `document-harness/plans/submod-hookenv.plan.md` §Review
states it: *"No FULL of its own. The shared FULL dispatched after this batch's candidate lands
covers `153302a..<tip>` — both work units."* `CONSTRUCTION-LEDGER.md`'s pointer has
`STRANGER-PROOF` as the queue head of publicization batch C; `SUBMOD-HOOKENV` is the small fix
batch opened inside it.

**Budget (`E9`).** One FULL, at most one user-approved fix, one targeted VERIFY, for the combined
subject. `E9`'s test — *has a valid independent FULL already occurred?* — answers **no**, and I
checked rather than accepted it: no `v3-review-full-*.md` record names any commit in the range,
and the only record commit in the range is the verdictless checkpoint read. So every commit in the
range is a pre-submission unit that consumed nothing, and **this record is the round's one FULL**.

**Authorization.** Four user rulings of 2026-08-24 are load-bearing here: postpone
`STRANGER-PROOF`'s FULL and consolidate into one shared FULL; open the `SUBMOD-HOOKENV` fix batch;
remove the cancelled FULL's freeze marker; and treat the plan's *Dispatch economy* section as an
ineffective scheduling carrier so the ledger backlog line becomes it. None has a decision-log
entry — `HARNESS-DECISIONS.md` still tops out at `HD-57` and contains no 2026-08-24 date. Per `R7`
I state the ceiling and move on: **every authorization in this round is an orchestrator-authored
assertion in a plan or a commit body, never independent evidence**, which is the standing shape
the 2026-08-21 `E11` carrier ruling chose deliberately. The read record's `L-1` already routed
this to the user; `912f837` records the deliberate decision not to bank it. Open, not lost —
see `O-5`.

**Obligations.** From the two plans' *Expectations the FULL can hold the candidate to* sections,
plus `E1`–`E12` for the execution side. I use them as the question list, never as the verdict
basis (`REVIEW.md`).

---

## 3. Implementation — the `SUBMOD-HOOKENV` fix

This is the part of the round I can hold to hard evidence, and it holds.

### 3.1 The defect, reproduced independently on the real second caller

The walk (`F-1`) and the candidate measured the defect on scratch trees. I re-measured it on the
second caller the walk left behind, `D:/Project/Ongoing/stranger-proof-work/second-caller` — a
tree neither measurement used for this — driving `TrackedPaths.from_index` directly with each of
the three environment shapes, pre-fix module against candidate module, restored by checksum
between runs:

```
PRE-FIX (blob at 153302a, sha256 5e29f825…20b7ca)
  unset                  entries= 382 unlistable=() real=True  shadow=False classify=DIRECT
  relative .git/index    entries=  13 unlistable=() real=False shadow=False classify=UNRESOLVED
  absolute super index   entries=  26 unlistable=() real=False shadow=True  classify=UNRESOLVED

CANDIDATE (sha256 9089dc6769af29d63eb3b9c244cb71147bca474f347363c2012dbf2ac86144ba)
  unset                  entries= 382 unlistable=() real=True  shadow=False classify=DIRECT
  relative .git/index    entries= 382 unlistable=() real=True  shadow=False classify=DIRECT
  absolute super index   entries= 382 unlistable=() real=True  shadow=False classify=DIRECT

  real   = lib/vendor/assurance-harness/tooling/hooks/candidate_path_check.py   (real, under the mount)
  shadow = lib/vendor/assurance-harness/manuscript/chapter-01.md                (superproject file, cited under the mount)
```

Both halves of the candidate's claim are confirmed, and the second half is the worse one exactly
as claimed: under an absolute `GIT_INDEX_FILE` the superproject's own file **falsely resolves
under the mount** (`shadow=True`) while the mount's real files do not. The candidate's sha256 in
its own commit body matches the bytes it committed — checked, not accepted.

### 3.2 The fix reads correctly

`git rev-parse --local-env-vars` is the right instrument and I confirmed it answers outside a
repository as well as inside (exit 0 in a non-repo directory), so the `None` branch is a genuine
git-cannot-answer branch and not a routine one. The asymmetry — `_submodule_files` clears,
`from_index` keeps — is argued in both docstrings and is right: inside a hook the inherited
`GIT_INDEX_FILE` names the index the commit is building, which is precisely `from_index`'s
subject and precisely wrong for the mount.

`R5` boundary: whether the empty-listing fail-open should exist at all is the user's question, not
mine. I record only that it widens `OUT_OF_INDEX` to any mount whose index lists nothing, and that
the module's ceiling list and `_submodule_files`' docstring both now say so (`O-4`).

### 3.3 The battery, re-run

`EXECUTION.md`'s tiering owes this repository one command; the change surface is tooling, so the
full tier applies. Run from `tooling` as the text requires, immediately before this claim:

```
$ cd tooling && python -m pytest -q
851 passed in 133.36s (0:02:13)
```

851 confirms the candidate's figure. The claimed 844 before is confirmed by construction: the new
file collects exactly 7 (`pytest --collect-only` → `7 tests collected`), and no other test count
changed. The new module also passes when pytest is invoked from the repository root, which is what
`.github/workflows/ci.yml` does — so CI will actually run it.

### 3.4 Red-before, and mutation

Red-before, pre-fix bytes swapped in from a sha256-checked scratchpad copy and restored the same
way, never `git checkout --`:

```
pre-fix module   5 failed, 2 passed      the 2 are the two negative controls
fixed module     7 passed
```

Five single-point mutations against the candidate bytes, each restored by checksum
(`9089dc67…44ba` verified after every one). Per-test outcomes, measured, not described:

```
                                                          plain  all  shadow  work-tree  empty  ctl-mount  ctl-super
M1  drop env= on the ls-files call                        PASS   FAIL  FAIL    FAIL      PASS   FAIL       PASS
M2  drop env= on the toplevel probe                       PASS   PASS  PASS    FAIL      PASS   PASS       PASS
M3  return listed, unguarded again                        PASS   PASS  PASS    PASS      FAIL   PASS       PASS
M4  drop GIT_INDEX_FILE from git's own answer             PASS   FAIL  FAIL    PASS      PASS   FAIL       PASS
M5  make _repo_local_env_names always return None         PASS   PASS  FAIL    FAIL      PASS   FAIL       PASS

plain     = test_a_real_submodule_path_survives_a_plain_commit
all       = test_a_real_submodule_path_survives_an_all_commit
shadow    = test_the_superprojects_own_files_do_not_answer_for_the_mount
work-tree = test_a_redirected_work_tree_does_not_reach_the_mounts_own_question
empty     = test_a_mount_whose_index_lists_nothing_is_out_of_index
ctl-mount = test_a_nowhere_path_under_the_mount_is_still_blocked          (must-fire control)
ctl-super = test_a_nowhere_path_in_the_superproject_is_still_blocked      (must-fire control)
```

M5 is mine, not the candidate's: it is the blinding failure mode — a "fix" that makes every mount
unlistable — and `ctl-mount` and `shadow` kill it, which is the property the candidate claims for
its controls and which does hold. Every mutation dies. **The guard binds.** What does not
reproduce is the candidate's *description* of M1 and M4, and its summary sentence about the
controls — `B-2`.

Two things this table shows that the candidate's does not, and that a repairer needs:

- **`ctl-mount` goes red under M1 and M4.** The candidate says both controls "stay green under all
  four". They do not.
- **`plain` is killed by no single-point mutation.** It goes red only on the pre-fix tree, where
  both halves of the fix are absent. With the environment cleared it passes because the listing is
  right; with the environment not cleared it passes because `return listed or None` turns the
  relative-index branch's empty listing into `OUT_OF_INDEX`. So for that branch the two halves are
  not independent: the empty-listing guard alone converts a false block into a **silent blind
  spot**, and only the environment clearing makes the answer correct. The suite is not vacuous —
  `plain` is red pre-fix — but it does not independently pin either half of that branch, and the
  misdescribed M1/M4 signatures are what hid this.

### 3.5 The `HD-41` class scan, re-derived

I re-enumerated every `subprocess` git call site in shipped (non-test) tooling rather than
checking the candidate's list:

```
$ grep -rn '"git"' --include='*.py' tooling/ | grep -v '/tests/' | wc -l
20
```

Twenty, and the membership matches the candidate's twenty rows exactly — the enumeration is
complete and `caller.py:167` really is the single unfixed class member. All three hook entry
points do pass `pathlib.Path.cwd()` (`candidate_path_check.py:155`, `layer_path_check.py:134`,
`review_freeze_check.py:109`). The `discover_repo_root` reachability claim holds: its only
non-test caller is `cli.py:49` from cwd, and nothing under `tooling/hooks/` or `.githooks/`
reaches it. **Five of the twenty line numbers are wrong** — `L-1`.

### 3.6 Riders

`submod-hookenv` is deleted in the fixing commit (`R10`, verified per-commit). The two
beyond-plan edits are disclosed rather than folded in, which is the right shape: `decited-paths`
gains a third touch record, and `discover-root-env` banks `caller.py:167` with its bytes named and
the reason they are unapplied (outside the declared surface, `E8`). I re-derived the
`GIT_WORK_TREE` behaviour that row records and it is as stated.

---

## 4. Implementation — the `STRANGER-PROOF` work unit

### 4.1 The walk record measures what it says it measures

I spot-checked the walk against the second caller it left in place, and every number I could
re-derive reproduced:

```
$ git -C <second-caller> log --oneline
fbda824 / 271910c / 3a53531 / 519fb1b / f5e1f8e / d0a4d45      six commits, the six named
$ git -C <second-caller> submodule status
 1a0a200dc24b14ccd48c32d9aa9c8513031c5ce2 lib/vendor/assurance-harness (heads/main)
$ git -C <second-caller> config --get core.hooksPath        .githooks
$ git -C <second-caller> ls-files -s .githooks/pre-commit   100755 a48e9035…
$ cat <second-caller>/.gitmodules                            url = https://github.com/Melclycj/do-the-work.git

longest path under the mount: 182   root prefix: 52   relative: 129
$ git diff --name-only 1a0a200..001816f | wc -l              5   (the five named, none under tooling/ schema/ contract/ assurance/)
```

The "first ceiling closed" claim is therefore established, not asserted: the mount source is the
published remote URL and the pinned revision is a published one. The layout is genuinely unlike
the first caller's. The honesty caps (same machine, agent not human, Windows only) are stated up
front and are the right ones.

`F-1` through `F-4` are all real defects and all correctly classified. `F-2` and `F-3` are fixed
in the candidate and the fixes are correct — I verified the import chain by hand:
`candidate_path_check` and `review_freeze_check` both reach `jsonschema` through
`rsclib.document_harness.__init__:35` via `caller.py:35`, while `layer_path_check` imports nothing
third-party. That is exactly what the new ONBOARDING paragraph and the corrected README row say.

### 4.2 The advisory-guard disclosure reproduces

I re-ran the candidate-side path lint's logic over the whole range's added lines:

```
CONSTRUCTION-LEDGER.md                              0 unresolved
README.md                                           0 unresolved
document-harness/ONBOARDING.md                      1 unresolved   `docs/policy/`
document-harness/journal/…walk-2026-08-24.md        7 unresolved   (the second caller's real paths)
plans, records, code                                exempt or 0
TOTAL                                               8
```

Eight, matching the candidate's disclosed figure, all of them the second caller's real paths —
the accepted class `FULL 7f6e7f0` `O-6` already measured here.

### 4.3 The README rewrite — where it fails

The rewrite is a real improvement on the agent-first original and most of it holds: no network
imports exist anywhere in shipped tooling (checked, so "no server, no account, no telemetry" is
true), the agent-facing commands-over-claims table survives, the `dtw --help` count is still
deliberately unwritten, and the corrected dependency row is accurate. **The quickstart is not**,
and that is `B-1`.

---

## 5. Findings

### `B-1` — blocker. The README quickstart cannot produce the outcome its own step 4 promises

**Where.** Root `README.md`, *Quickstart — mounting it in a repository that has never seen it*,
steps 3 and 4, under the preamble "Every command below was run end to end against a fresh
repository on 2026-08-24".

**What.** The block never creates a hook script. `dtw init` does not write one — it prints, in as
many words, that it did not: *"NOT done by this command … wire a pre-commit hook, and run the
per-machine core.hooksPath step"*. Step 3 then sets `core.hooksPath` to a directory that does not
exist, and step 4 tells the reader to expect a refusal. Executed verbatim from a fresh repository
(local clone standing in for the private remote, which changes nothing about the hook):

```
$ python <mount>/tooling/dtw.py init --repo-root .
RESULT: 5 created, 0 left as found (exit 0)
$ ls -la .githooks
ls: cannot access '.githooks': No such file or directory
$ git config core.hooksPath .githooks
$ printf 'See `docs/no-such-file-quickstart-probe.md` for details.\n' > docs/note.md
$ git add … && git commit -m "quickstart step 4: cite a path that does not exist"
 4 files changed, 6 insertions(+)
commit exit=0                        <-- it did not refuse, and said nothing
```

Silent, not loud: git warns nothing about a `core.hooksPath` that resolves nowhere, so the reader
following the quickstart ends with a hook that never runs **and every reason to believe it does** —
which is the exact failure `ONBOARDING.md` item 9's *See* row names ("A hook that has never been
seen to block is a hook nobody has tested"), arriving through the document that was written to
prevent it.

**Ground truth it violates.** The walk this block cites performed the omitted step and pasted its
check (`git ls-files -s .githooks/pre-commit` → `100755`); `ONBOARDING.md` item 9 states the
tracked half and the per-machine half as **two halves**, and the caller's hook is 13 lines the
caller must author (the second caller's is in its tree). The plan's own expectation is *"The
README's quickstart quotes only commands the walk ran … no new unverified claim (the section's own
rule)"* — step 4 is a new claim, carries no command, and does not hold. `E3`: a factual assertion
written into reader-facing instruction text runs the command that could falsify it first; the
block as a sequence was never run. `HD-41` ②: "Every command below" is an absolute quantifier over
a block whose stated outcome was not measured.

**Minimum fix.** Insert the tracked half of item 9 as its own numbered step **before** the
`core.hooksPath` step — author `.githooks/pre-commit` calling the guards from the mount, then
`git update-index --chmod=+x .githooks/pre-commit`, checked with `git ls-files -s` printing
`100755` — then re-walk steps 0–4 as a block and paste the result, so the preamble's claim becomes
true of the sequence and not only of the individual lines. While correcting it: the sentence
"That is four of the nine items. The other five are judgment — which revision to pin, …" offers as
an example of the uncovered five a decision that lives inside item 1, which the block does cover;
the covered/remaining split needs restating once the step is added.

### `B-2` — blocker. Two of the four mutation signatures do not reproduce, and the control claim is false

**Where.** `3d5c705` commit body, *VERIFICATION* section, the four-mutation table and the sentence
beginning "The two must-fire controls".

**What.** Measured against the candidate's own bytes (§3.4 above, restored by checksum after each
mutation):

| claimed | measured |
|---|---|
| M1 → "4 failed (both commit forms, shadowing pin, work-tree pin)" | 4 failed, but the **plain-commit form passed**; the fourth failure is the `ctl-mount` must-fire control |
| M4 → "3 failed (both commit forms, shadowing pin)" | 3 failed, same swap: plain-commit passed, `ctl-mount` failed |
| "The two must-fire controls … stay green under all four" | **false** — `ctl-mount` goes red under M1 and M4 |
| M2 → "1 failed (the work-tree pin, and only it)" | reproduces exactly |
| M3 → "1 failed (the empty-mount pin, and only it)" | reproduces exactly |

The counts are right; the identities are not, in the same direction both times.

**Ground truth it violates.** `E3` — *"Re-run immediately before the claim; paste tool output,
never describe it from memory"* and *"a characterization of the work no command established … is
dropped, not softened"*. These four signatures are descriptions, not output, and two are wrong.
`E4`/`R8` make mutation evidence the load-bearing proof that a new guard binds; a reader who
trusts the recorded signatures draws the wrong conclusion about what the controls establish, and
in particular cannot see §3.4's second consequence — that `plain` is killed by no single-point
mutation and so pins neither half of the relative-index branch on its own.

**Minimum fix.** An errata in the round journal (`E1` names it as the alternative carrier and the
commit body cannot be amended under `E8`) pasting the actual per-mutation, per-test output,
withdrawing the "stay green under all four" sentence, and stating the mechanism: under M1 and M4
the surviving `return listed or None` converts the relative-index branch from a false block into a
silent blind spot, which is why the defect pin passes and the control fails.

### `L-1` — low. Five of the twenty class-scan line numbers do not resolve

`3d5c705` commit body, *HD-41 CLASS SCAN*. All five `paths.py` rows are off by exactly three at
the candidate revision; the other fifteen rows are correct.

```
claimed  121  166  181  240  327
actual   124  169  184  243  330
$ sed -n '121p;166p;181p;240p;327p' tooling/rsclib/document_harness/paths.py
answers nothing. / return None / except OSError: / """ / shorthand.
```

The enumeration itself is complete and correct — I re-derived all twenty sites and the membership
matches — so what is lost is navigability, not the claim. But the scan exists, in the commit
body's own words, "so that *the only site that asks one repository about another* is checkable
rather than claimed", and five of its rows are not checkable as written. Same `E3` clause as
`B-2`, measured against an intermediate state of the file rather than the staged bytes. Fix: the
corrected offsets, in the same errata as `B-2`.

### `L-2` — low. The long-path threshold is off by one, in the under-warning direction

`document-harness/ONBOARDING.md`, *Second execution* section: "a caller whose repository root
**exceeds 130** characters still needs `-c core.longpaths=true`". The walk's own derivation, in
the same candidate, says "the first root prefix that trips it is **130** characters". I re-measured
on the second caller: longest absolute 182 = 52 prefix + 1 + 129 relative, so total = prefix + 130
and the limit is met at prefix 130, not 131. A caller sitting at exactly 130 is told it does not
need the flag. Not wording-level under `R9`: the fix changes an actor's action. Fix: "reaches 130"
or "130 or more", matching the walk.

### `L-3` — low. The README states as absolute a discipline the layer states as norm-plus-exception

Root `README.md`, *What using it looks like*: "the discipline is that **they are three different
sessions, never one wearing three hats**". `ORCHESTRATION.md`'s three-roles table — the carrier for
`HD-55` — says "Independent is the norm; one session holding both work-side roles is the
exception", and `E1`'s exception channel exists for exactly that. This repository's own ledger
records round `PUB-FACADE` (2026-08-23) taking it: "工作侧两角色单 session 合并（`E1` 例外通道）".
`HD-41` ② asks an absolute quantifier to carry its scope. The README is not an instruction-layer
member and governs nothing, which is why this is low rather than a blocker; but it is the
audience's only account of the discipline, and it currently promises more than the instrument
does. Fix: a half-clause ("the exception is disclosed, never silent") or drop "never".

### `L-4` — low. A carrier for this round's operating rules was placed outside the repository

`be03c55` body: "Session-side mirror saved to the orchestrator memory layer same day", for two
rules the same commit calls "binding on this round's remaining dispatches". That mirror no longer
exists — the session-side memory directory now holds only its index, and that index records a user
ruling of 2026-08-24 disabling memory carriage for this repository, citing `R2` by name. Two
consequences, both inside this subject:

- the commit body asserts a carrier that was already gone before the subject tip (`E3`: a figure
  is invalidated by any later change to what it measures);
- the ruling that removed it has **no repository carrier at all** — not a decision-log entry, not a
  ledger line, not a commit body. It binds later rounds, so `HD-1`'s admission test would take it.

This is the class `document-harness/plans/harness-memory-lessons-integration.plan.md` closed
(*"知识在 memory 里 ≠ 知识生效"*), reappearing. It is low rather than a blocker because the
operative content did land in the repository — the plan section at `be03c55` and the ledger backlog
line at `0133d1b` — so nothing load-bearing is only outside. Fix: the ruling gets a home, and the
memory-mirror sentence is withdrawn in the closeout note.

### `O-1` — observation. The swallowed candidate

`0133d1b` declares `Kind: ledger-only bookkeeping` and describes two backlog lines while carrying
587 of its 592 insertions across four files as the `STRANGER-PROOF` candidate. `E8` requires a
commit to name its kind "so the review side can attribute it without asking", and a reviewer
handed this range does indeed find no candidate commit for that work unit. It is fully disclosed —
`e620b43` and the journal's closing section state the cause, verify the content byte-for-byte, and
name the two secondary consequences (the 2026-08-04 ledger-only ruling turns on a distinction a
mixed commit cannot be sorted by on inspection; the `STRANGER-GUARDS` riders-after-candidate lesson
is inverted). **Not a blocker: no repair is available.** `E8` forbids amending, the commit is
another session's, and the disclosure already exists in the carrier `E1` names. Recorded so the
attribution is on the review side's record too, and routed to the user.

### `O-2` — observation. The executor no-commit window is relied on and written nowhere

`be03c55`'s rule 2 and `af002e2`'s "the orchestrator lands no commit while it runs" both depend on
an executor no-commit window. `E9`'s window is a **review** window only — from a review dispatch to
its record's commit — and no rule creates the executor one. `SUBMOD-HOOKENV`'s plan declared it and
it held (the candidate checked the tip was `af002e2` at open and at stage); `STRANGER-PROOF`'s plan
did not, and three orchestrator commits landed inside its executor's window, one of which is
`O-1`. Whether the window should become a rule is a design question and therefore the user's, not
mine (`R5`) — reported as the shape, not as a conclusion.

### `O-3` — observation. `plain` pins no half of its own branch

Stated in §3.4 and repeated here so it survives the record it was found in: among the five
single-point mutations, none kills
`test_a_real_submodule_path_survives_a_plain_commit`. It is not vacuous — it is red on the pre-fix
tree — but it goes green under either half of the fix alone, so it does not distinguish "correct"
from "blind" for the relative-`GIT_INDEX_FILE` branch. `ctl-mount` is what distinguishes them, and
it does. No action proposed: adding a mutation is machinery (`E6`), and the property is now
recorded.

### `O-4` — observation. The empty-listing fail-open widened

A mount whose index lists nothing is now `OUT_OF_INDEX` for everything under it, where before its
paths were simply absent from the set. Disclosed in the module docstring, the ceiling list and the
commit body's own *CEILINGS* paragraph, and argued rather than asserted. `R5`: whether it should
exist is the user's question. Recorded because a reader of the M1/M4 rows needs it to follow them.

### `O-5` — observation. Two 2026-08-24 rulings still owe their register entry

The read record's `L-1` surfaced this and `001816f` records the user's answer — the entries are
**not** to be created, and the disposition is to be noted in the round journal at closeout. The
journal in this subject carries no such note, because closeout has not happened. Open and routed,
not re-filed and not to be banked (the read record says so explicitly, and I am honouring that).
`L-4`'s ruling is a third one of the same shape and is *not* covered by that answer, which is why
it is filed separately.

---

## 6. Boundary check (run second, per `R3`)

- **`E2`.** Zero frozen paths touched: `git diff --name-only 153302a..3d5c705 -- schema/document-assurance-v3/ contract/` returns nothing. The freeze surface is intact at sixteen — v4 at blob `dfc983d2e3d9fb5ca67b053a16fcfb0e6715b11a` (the corrected literal `E2` names) and `git ls-tree --name-only HEAD schema/document-assurance-v3/ | wc -l` → **15**.
- **`E10`.** Zero of the nine members touched, checked one path at a time, not inferred from the file list. The two member-side fixes the walk found (`move-cost-member-site`, and `onboarding-labels` examined and not redeemed) were banked rather than taken — correct, since the plans declare the members out of boundary.
- **Change boundary.** All ten changed paths fall inside the two plans' declared surfaces. `CONSTRUCTION-LEDGER.md` is the orchestrator's closeout-only surface and took one backlog line under the 2026-08-03 ledger-batch ruling, which is that ruling's shape.
- **`E8`.** No merges, no trailers on any of the seven commits, one author, titles all `V3-…-v1`. The kind is named on every commit; on `0133d1b` it is named **wrongly** — `O-1`.
- **`E9`.** Window intact (§1). Budget unspent before this record; this FULL is the first leg.
- **`E12`.** One range, no per-acceptance argument. Where the range is written into a file it is written base-plus-`<tip>`/`HEAD`, never a written tip SHA — `submod-hookenv.plan.md` and `3d5c705`'s body both do this correctly.
- **`R6`.** This record is `migration/document-work-assurance-v3/v3-review-full-3d5c705.md`; the orchestrator commits it, suggested title `V3-REVIEW-RECORD-SUBMOD-HOOKENV-3d5c705-v1`. I have **not** deleted `.harness/review-pending.json` — deletion is part of the commit act that lands this record, as `001816f` did it.

---

## 7. Coverage and honesty ceilings (`R4`)

**Read in full, end to end.** `document-harness/CONSTRUCTION-CHECKLIST.md` (both sides),
`REVIEW.md`, `ORCHESTRATION.md`, `document-harness/README.md`, the two retired stubs;
`HARNESS-DECISIONS.md` header and `§live` (eight entries: `HD-56`, `HD-44`, `HD-41`, `HD-36`,
`HD-35`, `HD-34`, `HD-23`, `HD-9`); both plans; the whole walk journal including the disclosure
section; `migration/…/v3-checkpoint-read-153302a.md`; all seven commit bodies;
`tooling/rsclib/document_harness/paths.py` and
`tooling/tests/document_harness/test_submodule_paths_in_hook.py` at the candidate;
`tooling/hooks/layer_path_check.py` and `candidate_path_check.py`; `.githooks/pre-commit`; the
full diffs of `README.md` and `ONBOARDING.md`.

**Sampled.** `EXECUTION.md` — the battery-tiering section in full, the rest probed.
`CONSTRUCTION-LEDGER.md` — the current-pointer block and the three batch lines this round sits in,
not end to end (it is ~41 KB). `HARNESS-RIDERS.md` — the six changed rows, not the file.
`contract/Document-Work-Assurance-Contract-v4.md` and the paragraph-map schema — **not read**;
neither is touched and both were confirmed byte-unchanged, which is what my boundary check needed.

**Probed only.** `caller.py`, `cli.py`, `candidate.py`, `dispatch.py`, `sweep_refs.py`,
`review_freeze_check.py`, `rsclib/document_harness/__init__.py` — for the named claims (call-site
enumeration, import chain, `discover_repo_root` reachability) and never end to end. The second
caller repository — its log, config, index, `.gitmodules`, hook and path lengths; its documents
were not read.

**Ceilings.**

- **Process claims are marked, not verified.** That the executor and the reader ran as separately launched `claude -p` sessions rather than in-process subagents, that `R1`'s four holdings were all the orchestrator's, and that the reader reached its findings before opening the prior record, have no evidence lock at any revision. `E1`'s disclosure is present and correctly shaped; that is the whole of what I can say.
- **Authorization is assertion, not evidence.** §2. Every user ruling in this round reaches me as orchestrator-authored prose.
- **One platform.** Everything I ran is Windows, git 2.48.1.windows.1, Python 3.13 (the battery's interpreter here) and 3.12. I did not re-measure git's hook environment table, and I did not run anything on POSIX. The candidate's own ceiling on this is correctly stated and I inherit it. I did confirm the new module collects and passes when pytest runs from the repository root, which is the CI invocation, so the ubuntu legs will exercise it — whether they pass there is unmeasured here.
- **Mutation proves binding force, not sufficiency.** Five mutations died. That establishes the seven new tests bind against those five defect shapes, not that they are enough.
- **`B-1`'s reproduction used a local clone** as the submodule source instead of the published remote. That substitution changes the mount's provenance and nothing about hook wiring, which is what the finding is about; the omitted step is absent from the text regardless of where the mount came from. The scratch caller is at `C:/Users/j3236/AppData/Local/Temp/v3rev/qs/caller`, outside this repository and disposable.
- **The worktree was left as found.** `paths.py` was swapped seven times (pre-fix once, five mutations, restore each time) and its sha256 was re-checked after every restore; `git status --porcelain` is empty at the time of writing, and the file is back to `9089dc67…44ba`.
