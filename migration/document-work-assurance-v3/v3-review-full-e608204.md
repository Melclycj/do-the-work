# FULL review — split batch R1, `a7437d3..e608204`

**Verdict: `CHANGES_REQUIRED`.**

Two blockers. Neither is in the deletion, the link repair, the battery, or the byte move — all
four hold under independent measurement. Both are in what the round **recorded about what it
delivered**: the new repository's guard posture is written down backwards, in three places
including the deliverable's own honesty section, and a rider that `HD-39` names R1 to retire is
still standing with its subject deleted out from under it.

Findings: 2 blockers, 6 low, 3 observations.

---

## 1. Subject, re-derived

Everything in this section is re-derived from the repository; nothing was accepted as reported
(`R2`).

| | |
|---|---|
| Range | `a7437d353093c86a94538492cf9cb62ffe652bd0..e60820480c3de323382051404ef4df589cf673fc` |
| Branch / worktree | `document-work-assurance-v3` @ `D:/Thesis-stage-control-refactor`; `git status --porcelain` empty; `HEAD` == range tip |
| Freeze marker | `.harness/review-pending.json` names this exact range, `dispatched_at 2026-08-15T01:23:10+00:00`; tip commit is `2026-08-15T11:23:03+10:00` = `01:23:03Z`, i.e. dispatch 7s after the last commit — `E9`'s "branch takes no commit but the record" holds so far |
| Commits | 4: `a1b80fa` `V3-SPLIT-R1-TRAVEL-MANIFEST-v1` · `a8af54c` `V3-SPLIT-R1-HD39-DELETE-HD42-ENUM-v1` · `e4ffa2b` `V3-SPLIT-R1-FREE-L1-v1` · `e608204` `V3-SPLIT-R1-PLAN-v1`. Author date == committer date on all four (no amend/rebase evidence) |
| Paths | 171 D · 1 A · 8 M, classified by hand below |
| Round | Split batch **R1** (construction: move the bytes), per `.goals/plans/harness-repo-split.plan.md`. Steps 10–13b claimed landed; step 14 (this FULL) open |
| Budget (`E9`) | No prior FULL or VERIFY record exists for this subject (`ls` over the migration directory: no `*-e608204*`, no `*-a7437d3*`, no `SPLIT-R1`). So every commit in the range is a pre-submission correction consuming nothing, and this is R1's one FULL. The fix leg and the VERIFY are unspent |
| Authorization | `HD-39` (delete 171), `HD-40` (design signed, R1 builds to §3/§4/§7), `HD-42` (one-shot 8→6 enumeration edit), `HD-28`/`HD-33` (membership), plus a user routing ruling of 2026-08-15 recorded in `e4ffa2b`'s body for the `L-1` free-channel application. The 2026-08-15 rulings on the 171 scope and the `L-1` route exist only in commit bodies and the plan — chat-only in origin, but committed, so not an `R2` chat-only finding |
| Out-of-repo | `D:/do-the-work`, one commit `345acdd`, 255 tracked, clean. In remit and reviewed |

Deletion set, classified by hand against `HD-39`'s enumeration — every one of the 171 falls
inside it and nothing else does:

```
14  ResearchSystem/harness/                          1  ResearchSystem/contract/Stage-Control-Contract.md
11  ResearchSystem/tooling/rsclib/harness/           1  ResearchSystem/tooling/rsclib/stage_control.py
 1  ResearchSystem/tooling/tests/harness/            1  ResearchSystem/tooling/rsclib/stage_close.py
81  ResearchSystem/schema/harness-v2/                1  ResearchSystem/schema/stage-record.schema.json
 1  ResearchSystem/contract/General-Harness-Contract-v2.md   1  .../review-result.schema.json
26  ResearchSystem/migration/general-harness-v2/     1  .../closure-receipt.schema.json
 2  ResearchSystem/migration/stage-control-refactor/ 24  ResearchSystem/schema/stage-control-fixtures/
 2  ResearchSystem/stages/                            2  ResearchSystem/tooling/tests/stage_control/
                                                      1  .claude/commands/rs-execute.md
--- total accounted --- 171     --- UNACCOUNTED --- (empty)
```

---

## 2. What I re-executed

The battery, in full, at the tip (not sampled, not taken from the commit body):

```
P2   tests/run_tests.py         tests: 29   passed: 29   failed: 0
P4   tests/run_p4_tests.py      tests: 80   passed: 80   failed: 0
P5A  tests/run_p5a_tests.py     tests: 39   passed: 39   failed: 0
fix  schema/fixtures/validate_fixtures.py   cases: 58   matched: 58   unexpected: 0
pytest -q (from ResearchSystem/tooling)     701 passed in 101.40s
rsc.py compile --check   173 live objects, 0 error(s), 0 warning(s), exit 0
repo-audit.py            RESULT: clean (exit 0)
```

Six legs, six green. The reported 29/80/39/58/701 reproduce exactly.

`E2`'s frozen surface reconciles — base, tip and new repo agree on all three signed blobs, and
the fifteen-file schema pack took zero changes in the range:

```
Document-Work-Assurance-Contract-v3.md               b2dbdf75… base = tip = new repo
…-supersession-1.md                                  68031fa2… base = tip = new repo
…-supersession-2.md                                  e1a2f26b… base = tip = new repo
schema/document-assurance-v3/  15 files @ base;  git diff base..tip -- <pack> = 0 changes
```

Instruction layer (`E10`, nine members): eight `SAME`, one `CHANGED` —
`EXECUTION.md` `62c55e4b` → `e56b1a3d`, which is the authorized `HD-42` edit plus the `L-1`
free-channel application. No unauthorized layer write.

The byte move, verified per file rather than in aggregate: for each of the 254 travelled paths I
took the new repo's blob id and `git rev-parse e4ffa2b:<path>` in the source —
**`checked=254 mismatch=0 missing=0`**. The claim reproduces.

The `C` membership rule, re-run rather than read: the design's §10.1 criterion over the migration
directory gives `top-level=123  product=29  construction=94`, and `diff` between the criterion's
29 outputs and the manifest's 29-row exception table is **empty**. None of the 29 leaked into the
new repo; the new repo holds 94 top-level + 49 subdirectory = 143. `C` is sound.

Guards: this round added none, so `E4` has no new subject. I mutation-probed the two that the
round's own claims turn on, inside a throwaway clone of the new repo — see `B-1`.

---

## 3. Blockers

### B-1 — the delivered repository's guard posture is recorded backwards, in the deliverable's own honesty section

**Location.**
`D:/do-the-work/README.md:42-44` (§*What does not work yet*, first bullet);
`ResearchSystem/document-harness/split-travel-manifest.md:123` and `:127`
(§*已知的未接线项*); `.goals/plans/harness-repo-split.plan.md:198` repeats it by reference.

**What they say.** The README: "`tooling/hooks/layer_path_check.py` matches staged paths against
a hard-coded member list; **a caller-shaped prefix means it matches nothing and passes silently
while looking green**." The manifest, harder: "新仓里这三处指向不存在的路径，**守卫匹配不到任何
staged path = 静默失效，而电池照样全绿**", and on that ground declares R1's delivery to
"**明确排除**「新仓的 pre-commit 守卫可用」这一条".

**Ground truth.** R1's own step-10 decision was to **keep** the `ResearchSystem/` prefix. That
decision is what makes the hard-coded list resolve. All nine `LAYER` members exist in the new
repository:

```
EXISTS  ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md   (…and the other eight)
```

And the guards bind. In a clone of `D:/do-the-work` I staged a broken path into an
instruction-layer file and ran them:

```
$ python ResearchSystem/tooling/hooks/layer_path_check.py
pre-commit BLOCKED: newly added instruction text names a repository path that does not resolve:
  ResearchSystem/document-harness/EXECUTION.md: `ResearchSystem/does-not-exist/nope.md`
EXIT=1

$ python ResearchSystem/tooling/hooks/candidate_path_check.py
pre-commit BLOCKED: newly written text names a repository path that exists nowhere:
  ResearchSystem/document-harness/EXECUTION.md: `ResearchSystem/does-not-exist/nope.md`
EXIT=1
```

Two of the three guards fire correctly. The third, `review_freeze_check.py`, exits 0 because
`.harness/review-pending.json` is the **caller's** file under `HD-33` — designed inertness, not
silent failure. And the membership tests pass there: `pytest tests/document_harness/
test_precommit_checks.py` in the new repo → **42 passed**, including
`test_layer_equals_the_hand_written_membership`. The claim that "电池照样全绿" is offered as the
*symptom* of silent failure; the battery is green there because the guard genuinely works.

The bullet's *heading* — "not wired here" — is separately true, but for a different and already
documented reason: no hook is installed in either repository's `.git/hooks`; the source repo's
`pre-commit` lives in the main repo's `.git/hooks` and `document-harness/README.md:34` already
records it as "per-machine, absent on a fresh clone". So the true state is *wiring absent, logic
sound*; the recorded state is *logic dead, wiring beside the point*.

**Why it is a blocker and not wording.** `R9`'s test is whether the fix changes an actor's
action. It does, and in the direction that costs most. The `E10-sync` debt does not bite now —
it bites **at the moment R2 re-roots**, because re-rooting is precisely what stops those nine
strings resolving. A reader who believes the guard is already dead has no reason to couple the
three-mirror edit to the re-rooting commit; a reader who knows it is live must couple them, in
the same commit, or ship a window in which the guard is silently dead — the exact shape `HD-42`
③ forced for the enumeration. The manifest also mis-scopes the delivery: it excludes a
capability that was in fact delivered.

`E3` is the rule breached — "a factual assertion written into instruction text runs the command
that could falsify it first". The falsifying command is one `test -f`. `HD-41` ①② compound it:
"匹配不到任何" and "静默失效" are absolute quantifiers asserted without running anything covering
their scope, and `HD-41` exists because this round's own predecessor kept doing this. Note the
manifest's sentence was a *prediction* when written at `a1b80fa` — the layout was still open. It
became false at `345acdd`, and nothing went back to check it; the README's version was false the
moment it was written, in the same commit as the decision that falsified it, two paragraphs below
a §Layout section that gives the correct mechanism.

**Minimum fix.** Replace the three passages with the measured state: the prefix was kept, so all
nine `LAYER` members resolve and `layer_path_check` / `candidate_path_check` bind in the new
repository today (mutation-proved), `review_freeze_check` is inert only because the freeze marker
is the caller's under `HD-33`, nothing is wired into `.git/hooks` in either repo per the
already-documented per-machine convention, and `E10-sync`'s three-site edit falls due **in the
same commit as R2's re-rooting**. Delete the manifest's delivery exclusion at `:127`, since the
thing it excludes was delivered.

### B-2 — rider `SCC` was not retired, and its subject no longer exists

**Location.** `ResearchSystem/HARNESS-RIDERS.md:18`; the same row, byte-identical, at
`D:/do-the-work/ResearchSystem/HARNESS-RIDERS.md:18`.

**Ground truth.** `HD-39`'s consequence clause names R1 by name: "rider `SCC` 随其 subject 删除
而在 R1 **retire**". R1 deleted the subject — `git ls-files
ResearchSystem/contract/Stage-Control-Contract.md` is empty at the tip. The row is still there.
`HARNESS-RIDERS.md` took **zero** changes in the range (`git diff --name-only a7437d3 e608204 --
ResearchSystem/HARNESS-RIDERS.md` → empty), and none of the four commit bodies mentions `SCC`
(`git log ... | grep -i SCC` → no hit, while `E10-sync`, `tier-scope`, `wl-route` and `CLI-hist`
all appear). So it was missed, not weighed and deferred — the round demonstrably does record
deliberate non-actions elsewhere, including for `tier-scope` ② in the same commit.

**Consequence.** The row's redeem-when is "下一批碰该契约或豁免册". The contract can never be
touched again, so under `R10`'s own format rules the row is now permanently unredeemable — a dead
entry in the bank whose whole purpose is that a later batch can act on it. It has also been
copied into the new repository, so the defect now exists twice. `HD-39` outranks the plan's
step-22 deferral: `HARNESS-DECISIONS.md`'s header states the layer bases on the rulings and
"细则与裁决冲突，细则错".

**Minimum fix.** Delete the `SCC` row in a commit whose body names `HD-39` as the authority, and
carry the same deletion into the new repository's copy so the two do not diverge on their first
day. If instead the row is judged to survive its subject — the exemption-register half of its
text — say so in the row and give it a redeem-when that can still fire.

---

## 4. Low

- **L-1 — one member of the deleted family survives, unrecorded.**
  `ResearchSystem/generated/stages/README.md` is still tracked. Its text is present-tense about
  machinery this round deleted: "deterministic, disposable metadata projections **emitted by the
  Stage controller**" and "a later authorized run **may rebuild** the views" — no controller
  exists and no run can. It is not in `HD-39`'s 171, and `split-design.md` §7 does not list it,
  so R1 could not have deleted it without exceeding its boundary (`E8`) — but nothing records it
  either, while the round *does* record a deliberate keep for the
  `rsclib/document_harness/__init__.py` docstrings. The harness's own A2 survival audit already
  knew about it (`journal/batch-a2-2026-08-09.md:105`: "`generated/stages/` 只有 README"), which
  is where it should have been caught. Compounding: the round's new
  `ResearchSystem/README.md` prose says `HD-39` "deleted **the whole family**" — an absolute
  quantifier (`HD-41` ②) with a surviving member.

- **L-2 — the deletion left a dead import.** `ResearchSystem/tooling/rsc.py:37` `import json` is
  now unused: `grep -n "json\." rsc.py` yields exactly one hit, `_json.dumps(` at `:320`, fed by
  a function-local `import json as _json` at `:309`. The module-level import's only consumers
  were `_cmd_stage_pause` / `_cmd_stage_resume`, both deleted in `a8af54c`. No guard catches it —
  `compile --check` is a content lint, and pytest is green. The round enumerated its rsc.py cuts
  precisely and missed this one.

- **L-3 — an absolute quantifier written into the instruction layer by the round that falsifies
  it.** `EXECUTION.md` now reads "test counts **only grow**" (`e4ffa2b`). This round removed 59
  tests from the battery — the two deleted runners, 39 + 20, as `HD-42`'s own criterion states.
  The sentence is defensible if silently scoped to the five named sub-tallies, which is exactly
  the scope `HD-41` ② requires be written rather than inferred, in a passage whose entire subject
  is that unscoped tallies go stale.

- **L-4 — the manifest's declared revision does not hold for its own headline number.**
  `split-travel-manifest.md:8-10` declares `revision = a7437d3` for every count in the file. Measured:

  ```
  ResearchSystem/document-harness/  a7437d3: 25   a1b80fa: 26   e4ffa2b: 26   new repo: 26
  A total @ a7437d3 = 107        A total @ e4ffa2b = 108
  ```

  A1's 26 and the A subtotal of 108 only hold from `a1b80fa` onward, because the manifest counts
  itself — it lives in `ResearchSystem/document-harness/`. The delivered set is right (108 at the
  move revision `e4ffa2b`, total 254); the revision label on those two numbers is not. In the one
  file whose declared purpose is to be the single authoritative membership definition, and whose
  header invokes `HD-41` ①③ by name.

- **L-5 — R2's own checklist step now names four deleted artifacts.**
  `.goals/plans/harness-repo-split.plan.md:147-148`, step 15: "摘 `rsc.py` 的 `harness`/`stage`
  命令组 + 两个活 CLI 测试（`tests/harness/run_tests.py` `test_cli_validate_and_resolve` ·
  `tests/stage_control/run_tests.py:181`）". All four were deleted by `a8af54c`. The Resume
  pointer was rewritten in `e608204` and correctly redirects `CLI-hist`'s remaining half to the
  v3 command group; the numbered step R2 will actually work from was left stale.

- **L-6 — reported line count off by one.** `a8af54c`'s body and plan step 11 both say `rsc.py`
  856→**687**. Measured: `git show a7437d3:…/rsc.py | wc -l` = 856,
  `git show e608204:…/rsc.py | wc -l` = **686**, file ends with a newline. Small, and named only
  because `E3` puts counts in the class that is emitted or omitted.

---

## 5. Observations

- **O-1 — the `HD-42` edit carries a sentence `HD-42` did not authorize, unclassified under
  `E10`.** Beyond changing "eight"→"six" and striking the two entries, `a8af54c` appends to
  `EXECUTION.md`: "That exception is one-shot and covers only those two entries — a subject
  disappearing does not license editing this enumeration again." `HD-42` authorizes the
  enumeration change under four narrowings, none of which reaches new prose. The bytes are benign
  — they restate what `E10`'s design test already requires, and `HD-42`'s own 后果 says so — and
  they are plausibly a free-channel amendment that "neither adds a clause to any rule nor changes
  what any rule requires". But `E10`'s deferral branch requires the commit to record **both**
  facts, and the body records only that the edit owes a read. So the sentence sits in the layer
  with no stated channel. The four narrowings themselves check out: only these two entries struck
  (the surviving six are untouched apart from the "and" that necessarily moves to the new last
  item), `nothing fewer` retained, same commit as the deletion, body names `HD-42` and both
  entries.

- **O-2 — nobody ran the delivered repository's own suite.** In `D:/do-the-work`:
  `python -m pytest -q` → **24 failed, 677 passed in 93.46s**. Every failure traces to one cause —
  `can't open file 'D:\do-the-work\ResearchSystem\tooling\rsc.py'` — because `rsc.py` is
  deliberately outside the travel set. So the README's "There is no CLI entry point here" names
  the cause correctly, and no claim in the round is falsified by this. What is missing is the
  magnitude: the README frames the whole section around "green-looking silence", and a reader who
  arrives expecting vacuous green meets a loud red suite instead. The figure was never measured
  by the round; it is offered here so R2 opens with it rather than discovering it.

- **O-3 — the `L-1` free-channel application is properly routed, and worth recording as a clean
  instance.** The read record `v3-cold-read-ddd773a.md` tiered it low, named the content without
  dictating bytes, and explicitly refused to settle the route ("Routing is not mine to settle"),
  which `R5` requires of it. The user ruled the route on 2026-08-15; `e4ffa2b` carries the bytes
  in its own commit per `HD-38` rather than riding `a8af54c`; the fix pins the old figures to
  their revision instead of hard-coding fresh ones, which is what the finding asked for. The one
  defect in it is `L-3` above.

---

## 6. Coverage and ceilings (`R4`)

**Read in full**: the four commit bodies; `CONSTRUCTION-CHECKLIST.md`; `HARNESS-DECISIONS.md`
`§live` and `§implemented`; `HARNESS-RIDERS.md`; `HARNESS-LEDGER.md`;
`.goals/plans/harness-repo-split.plan.md`; `split-travel-manifest.md`; `v3-cold-read-ddd773a.md`
§4; the diffs of all 8 modified files; `D:/do-the-work/README.md`;
`ResearchSystem/generated/stages/README.md`; `hooks/layer_path_check.py` and
`hooks/review_freeze_check.py` headers.

**Sampled**: `split-design.md` §7 and `journal/batch-a2-2026-08-09.md` §2–3 (the sections the
deletion rests on, not the whole documents); `rsc.py` by diff plus targeted greps, not end to end.

**Probed, not read**: the 171 deleted files — I verified the *set* against `HD-39` path by path
and did not read their contents; the 254 travelled files — verified by blob identity, which is
stronger than reading, and I did not read them.

**Executed**: the six battery legs, `repo-audit`, the new repo's full suite and its
`test_precommit_checks`, and two guard mutations in a scratch clone.

**Ceilings.**
- `R8`/`E4` had little to bite on: the round added no guard. The two mutations I ran prove those
  guards *bind in the new repo layout* — the precise claim `B-1` turns on — not that their force
  is sufficient for anything else.
- Whether the freeze marker's `dispatched_at` reflects a real `rsc v3 dispatch` invocation is a
  process claim; the marker's existence and contents are verified, the command that wrote it is
  **UNVERIFIABLE** from my side (`R4`).
- The 2026-08-15 user rulings (171 scope, `L-1` route, `ddd773a` re-read discharge) are visible
  only as executor-written prose in commit bodies and the plan. `R7`: I state the ceiling and move
  on — no authorization is contradicted by anything in the repository.
- `E9`'s "branch takes no commit but the record" is verified as of the moment of this read
  (`HEAD` == range tip, worktree clean); it cannot be verified for the interval after I stop.
- **Not concluded, by `R5`**: whether `generated/stages/README.md` should exist, whether the
  `SCC` row should be deleted or rewritten, and whether the appended `HD-42` sentence should stay
  — each names its location and the rule at stake; the disposition is the user's.

---

## 7. What holds

Stated plainly, because a `CHANGES_REQUIRED` on two recording defects should not be read as doubt
about the work itself. The deletion is exactly `HD-39`'s 171 files and nothing else. The 14
inbound links across 4 source files are all repaired, none by quoting the dead target — including
the wikilink, rewritten out of the sentence as the discipline required — and `repo-audit` exits
0. The `rsc.py` surgery is right, including the judgment call on `:850`: the `except
stage_control.StageControlFault` caught a type that no longer exists, and `grep` confirms no
surviving raiser. The `HD-42` edit met all four narrowings. The battery is six-for-six green and
the reported tallies reproduce exactly. `E2`'s frozen bytes are untouched in both repositories.
The move is byte-exact, 254 for 254, verified per file. The `C`-set criterion reproduces and its
29 exceptions stayed behind. `E9`'s budget is intact and unspent.
