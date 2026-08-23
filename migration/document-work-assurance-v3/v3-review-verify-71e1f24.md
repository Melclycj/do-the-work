# VERIFY — `f7fcbe9..71e1f24`

**Verdict: `REVIEWED_NO_BLOCKER`.** Both accepted findings landed as the minimum fix the FULL
named, the whole repair diff holds against the permanent boundaries, and the guard `B-2` said
did not bind now binds under six mutations including the two that survived before. This is not
a re-certification of the round (`R4`): it covers the repair, the two findings, and the
boundaries — not the candidate the FULL already reviewed.

**Findings: 2 low, 4 observations.** Neither low is in the mechanism. One is a code comment
whose stated reason is falsified by one of the two lines it justifies (the behaviour is still
correct, for a different reason); the other is two wrong line references inside the fix's own
`HD-41` class-scan report, which pasting the grep output rather than summarising it would have
caught. The observations carry what this VERIFY measured outside its own remit and could not
verify at all.

Independence: this session was dispatched by the orchestrator with a range and nothing else,
derived round, leg, budget, authorization and every number below from the repository, and
reports through this record. No reported figure was accepted; each was re-run here.

---

## 1. What the subject is, derived (`R2`)

Handed one range and nothing else. Re-derived from `git log`:

```
$ git log --oneline f7fcbe9..71e1f24
71e1f24 V3-PUB-FACADE-FIX-v1
5e3feb5 V3-REVIEW-RECORD-PUB-FACADE-28dd80b-v1
28dd80b V3-PUB-FACADE-JOURNAL-v1
87004fb V3-PUB-FACADE-v1
dd9c465 V3-PUB-FACADE-PLAN-v1
```

- **Round:** `PUB-FACADE`, publicization batch A. Plan `document-harness/plans/publicization-a.plan.md`.
- **Leg: VERIFY.** A valid independent FULL has occurred — its record `5e3feb5` landed with
  verdict `CHANGES_REQUIRED` and two blockers. `71e1f24` names itself the round's one
  user-approved fix. By `E9`'s test (*has a valid independent FULL already occurred?* → yes)
  that is the fix round, and it obliges this targeted VERIFY. Verdict set is therefore
  `REVIEWED_NO_BLOCKER | SPEC_GAP` (`R3`).
- **Accepted findings:** `B-1` (the round's own defect class survives in, and was newly written
  into, its two reader-facing work files) and `B-2` (the new guard binds one of the three wrapper
  behaviours its docstring claims). Both from `migration/document-work-assurance-v3/v3-review-full-28dd80b.md`.
- **Repair diff:** `28dd80b..71e1f24` less the record commit — three paths.

```
$ git diff --stat 28dd80b 71e1f24
 README.md                                          |  5 ++
 document-harness/ONBOARDING.md                     |  5 +-
 tooling/tests/document_harness/test_precommit_hook.py | 85 ++++++++++++++++++----
 migration/document-work-assurance-v3/v3-review-full-28dd80b.md | 297 +++++  (the record, 5e3feb5)
```

- **Authorization (`R7`):** the fix's approval is a conversation act I cannot see. The commit
  body carries it ("approved 2026-08-23 in conversation against FULL v3-review-full-28dd80b.md")
  and the plan carries the round's four rulings. That is the ceiling; stated, not blocking.
- **Freeze marker:** `.harness/review-pending.json` holds
  `f7fcbe90…..71e1f241…`, `dispatched_at 2026-08-23T04:55:53+00:00` — the range I was handed,
  exactly. `HEAD` is `71e1f24`, worktree clean, nothing has landed since dispatch, so `E9`'s
  "from dispatch to that commit the branch takes no commit but the record itself" holds so far.

---

## 2. Lead with the implementation (`R3`)

### 2.1 `B-1` — redeemed. Re-derived, not read.

The FULL's minimum fix was one sentence at the head of the *State of this repository* table
naming the interpreter convention, redeeming all five README sites at once, plus the same
sentence or `python3` for `ONBOARDING.md`'s two. The repair is exactly that and nothing more:
`README.md` gains four lines (purely additive), `ONBOARDING.md` extends its read-once preamble.

**First, the premise, re-measured on a POSIX box rather than taken from the FULL:**

```
$ wsl -d Ubuntu -e bash -lc 'command -v python; echo "python3: $(command -v python3)"; git --version; echo "sh -> $(readlink -f /bin/sh)"'
python3: /usr/bin/python3
git version 2.43.0
sh -> /usr/bin/dash
```

`command -v python` printed nothing. The class `B-1` names is real on this platform, at this tip.

**My own scan, scope declared before the command (`HD-41` ①): every path the range changes,
class = a reader-facing bare-`python` invocation.** Both work files, at tip:

```
$ grep -n 'python' README.md
49:One convention before the commands: `python` below means whichever of `python3` / `python`
50:this platform actually runs — stock Ubuntu ships only `python3` (every `python` row below
51:fails there verbatim, measured 2026-08-23), stock Windows only `python`. Substitute
56:| Does the suite pass? | `python -m pytest -q` |
57:| Why does a test fail? | `python -m pytest -q --tb=line` |
58:| Do the instruction layer's ten members resolve here? | `python -c "import sys,pathlib; ...
62:| Is there a CLI? | `ls tooling/dtw.py`; `python tooling/dtw.py --help` ...
63:| What does the suite need? | Python ≥ 3.12 and `python -m pip install pytest "jsonschema>=4.18" referencing` ...

$ grep -n 'python' document-harness/ONBOARDING.md
18:convention: `python` in the commands below means whichever of `python3` / `python` this
19:machine actually runs — stock Ubuntu ships only `python3` (measured 2026-08-23), stock
20:Windows only `python` — and `.githooks/pre-commit` resolves the same choice by probing.
58:| **See** | ... and `python <mount-path>/tooling/dtw.py --help` lists the eight operations. ...
75:| **Do** | `python <mount-path>/tooling/dtw.py init --repo-root .` from the caller's root ...
```

All five README command rows (`:56 :57 :58 :62 :63`) sit below the convention sentence at
`:49-52`; both `ONBOARDING.md` sites (`:58 :75`) sit below the one at `:17-20`. The two sites
the round itself added — the CLI row and the suite-needs row — are covered. **Seven for seven.**

The remaining hits across the round's other touched paths, checked one by one and each a
quotation of the measured defect rather than an instruction to a reader: `.githooks/pre-commit`
`:30-33 :38 :45` (the probe loop and its comment), `document-harness/plans/publicization-a.plan.md`
`:50 :59-60 :70-73 :80 :83`, `document-harness/journal/pub-facade-2026-08-23.md` `:41 :50`, the FULL record itself,
`test_precommit_hook.py`'s docstring, and `test_candidate_checks.py:598` (schema-rejection
data, never executed — the FULL had already verified this and the POSIX green below re-proves
it). `.github/workflows/ci.yml:25,27` are machine-run under `actions/setup-python`, not
reader-facing; see `O-4` for the part of that I could not verify.

My scan and the fix's own agree on substance. Where they disagree is two line references — `V-2`.

### 2.2 `B-2` — redeemed. Seven mutations, digest-checked restore.

Method (`R8`, `E4` by the letter): scratch clone at `71e1f24`, hook copied to a sha256-checked
scratchpad file, restored from that copy — never `git checkout --` — and the digest re-checked
after every single mutation. Every restore printed
`66137d289517394ae9bacc6abd7d48cf79553519fb279bc74003b06f3a549bf0`, identical to the digest the
FULL and the fix commit both recorded. Baseline before any mutation: `3 passed in 0.98s`.

| # | mutation | expected | measured |
|---|---|---|---|
| 1 | hook reverted to the pre-fix bytes (`git show f7fcbe9:.githooks/pre-commit`, bare `python`) | GREEN on Windows — the docstring says this is **not** pinned | **`3 passed in 0.38s`** ✅ matches the disclaimer |
| 2 | whole hook → `#!/bin/sh` + `exit 0` (**survived before**) | RED | **`2 failed, 1 passed`** — blocking test + missing test |
| 3 | loud missing-check `echo` deleted (control) | RED | **`1 failed`** — `test_hook_is_loud_when_the_check_script_is_missing` |
| 4 | `if [ "$status" -ne 0 ]` → `if false` (**survived before**) | RED | **`1 failed`** — `test_hook_blocks_when_the_layer_check_fails` |
| 5 | whole hook → `#!/bin/sh` + `exit 1` (blocks everything, runs nothing) | RED | **`3 failed`** |
| 6 | `"$PY" "$CHK"` → `"$PY" "$CHK" >/dev/null` (check runs, status propagates, verdict silenced) | RED | **`1 failed`** — blocking test |
| 7 | `status=$?` → `status=0` (check runs and prints, status discarded) | RED | **`1 failed`** — blocking test |

Mutations 2 and 4 are the two the FULL measured as surviving. Both are now red, and 5–7 show
the new assertion is not carried by the return code alone: it separates *ran the check*,
*propagated its status*, and *let its verdict through* into three independently falsifiable
things. Mutation 1 going green is not a gap — it is the docstring's own stated limit, and the
disclaimer is accurate on the platform I could test it on.

**The mechanism, read rather than inferred.** `BLOCKED_LINE` is a hand-written literal
(`test_precommit_hook.py:51-53`) matching `layer_path_check.py:127` character for character;
`assertIn(BLOCKED_LINE, result.stdout.splitlines())` is a whole-line membership test, not a
substring — `E5` on both counts. `MEMBER` is a hand-written member path, not imported from
`LAYER`, and `BAD_LINE` is assembled from fragments so no committed file carries a live broken
token. The check reaches the token because the hook runs with `cwd=root` and
`layer_path_check` reads `pathlib.Path.cwd()`, and `document-harness/CONSTRUCTION-CHECKLIST.md`
is in `LAYER` while the staged token — a no-such-file name under document-harness, written
here without backticks so this record carries no live broken token — resolves neither from the
scratch root nor from the file's own directory. The test needs no git identity (it stages, it
never commits) and no `core.hooksPath` (it invokes `sh .githooks/pre-commit` directly), so it
is hermetic against ambient config.

**The docstring now matches what the tests buy.** The falsified "both halves are pinned" is
gone; three behaviours are claimed and all three bind (mutations 2–7), and the one that does
not is named as not pinned with its reason and its carrier. `E6` is respected: no machinery was
added — one helper, two constants, one test method inside the file the round already wrote.

### 2.3 The disclosed third change, reproduced

`E9` requires that exceeding an approved fix boundary be said, never done silently. The commit
body says it: `_run_hook` gains `errors="replace"`, discovered during the fix's own mutation
run. I did not take that on trust — I reproduced the failure it fixes by removing the argument
and running under an ANSI console locale:

```
$ python -c "import sys,locale; print('stdout',sys.stdout.encoding,'| preferred',locale.getpreferredencoding(False))"
stdout gbk | preferred cp936

$ PYTHONIOENCODING=gbk PYTHONUTF8=0 python -X utf8=0 -m pytest -q tooling/tests/document_harness/test_precommit_hook.py
>           self.assertIn(BLOCKED_LINE, result.stdout.splitlines())
E           AttributeError: 'NoneType' object has no attribute 'splitlines'
  ...
    File "C:\Python313\Lib\subprocess.py", line 1615, in _readerthread
      buffer.append(fh.read())
  UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa1 in position 189: invalid start byte
1 failed, 1 warning in 0.51s
```

Exactly the shape the body describes — a crashed reader thread, `stdout=None`, and a correctly
blocking hook reported as a broken test. The change is load-bearing, minimal, and inside the
file the fix already had open. Its stated *reason* is what `V-1` is about.

### 2.4 The suite, both platforms, at this tip

```
# Windows (Python 3.13.6), repository root
$ python -m pytest -q
793 passed in 101.43s (0:01:41)

# collected counts, same clone, base then tip
$ git checkout f7fcbe9 && python -m pytest -q --collect-only   → 790 tests collected
$ git checkout 71e1f24 && python -m pytest -q --collect-only   → 793 tests collected

# POSIX: fresh clone at 71e1f24, WSL Ubuntu, git 2.43.0, Python 3.12.3, jsonschema 4.26.0
$ python3 -m pytest -q tooling/tests/document_harness/test_precommit_hook.py
3 passed in 0.09s
$ python3 -m pytest -q
793 passed, 865 subtests passed in 10.94s
```

790 → 793 is the plan's own expectation (`790 + the new hook tests`) and the arithmetic closes.
The commit body offered a POSIX result taken at `87004fb` with the fix's test file copied in
and invited re-derivation at tip; the tip run above is the stronger form of that claim and it
holds. Note for the record that the hook's Windows working-copy digest (`66137d28…`) and its
POSIX one (`23096254…`) differ only by line endings — `core.autocrlf=true`, no `.gitattributes`
— while the committed blob `d39c6370` is LF on both. Same bytes, two checkouts.

---

## 3. Process and boundary (`R3` — second)

Each re-derived; none accepted as reported.

- **`E9` budget.** One FULL (record `5e3feb5`), one fix (`71e1f24`, named as such and named as
  the user-approved one), this VERIFY. Nothing renamed: `dd9c465`/`87004fb`/`28dd80b` all
  predate the FULL and are pre-submission by the rule's own test. Between the FULL's dispatch
  and its record commit the branch took no other commit; between this dispatch and now, none.
- **`E8`.** Title `V3-PUB-FACADE-FIX-v1` — single, dense, names the round. Body opens with its
  kind (`review fix`), one paragraph, **no trailers** (checked the raw `%B`). New commit, not an
  amend. **No push**: `git rev-list --left-right --count origin/main...HEAD` → `0	5`, and
  `origin/main` is still `f7fcbe9`. Three staged paths, all inside the plan's declared change
  surface (`README.md`, `document-harness/ONBOARDING.md`, `test_precommit_hook.py`).
- **`E2`.** No path under `contract/` or `schema/document-assurance-v3/` appears anywhere in the
  range. Both supersession blobs are byte-identical at base and tip and still carry the ids the
  rule names: `68031fa2ca31272e31da0d42a9a02189d28fcc21`,
  `e1a2f26b1d8d323d11e900f8137dea222b6571c1`.
- **`E10`.** All ten members checked individually against the range: none touched. No amendment
  machinery, no `E10-sync`, no read owed by this repair. `LAYER` still mirrors the membership
  sentence (ten entries, same order). The opening cold read was waived by the user, which the
  clause permits, and the member reads still owed from `PRERUN-RIDERS` remain owed — the plan
  says so and this repair does not touch them.
- **`E12`.** `.harness/review-pending.json` again records the range with a written tip rather
  than `HEAD`. I reach the FULL's conclusion independently and likewise do not file it:
  `.harness/` is gitignored (`.gitignore:23`), so writing it is not a commit inside the round,
  the rule's stated rationale (a written tip is short by the commit that wrote it) cannot arise,
  and the written tip equals `HEAD` exactly.
- **`E1`.** The round's disclosure — merged work-side roles, all four `R1` holdings in the
  executor's hands, "nothing about this candidate's authoring is independent" — is carried by
  the plan and the candidate body, the carriers `E1` names. The fix commit does not repeat it;
  it does not need to, the disclosure being the round's and not the commit's. The review side
  stayed structurally independent across both legs: the FULL was dispatched cold, and so was this.
- **`E6`.** No new machinery on either finding. `B-1` is text changing at the sites the scan
  should have reached; `B-2` is a stronger assertion inside an existing file. Neither answers a
  finding by adding a rule about it, so the refusal `E6` obliges me to make does not arise.
- **`E7` / `HD-41` ④.** The scan was run and its substance is right (§2.1). Its *form* is `V-2`.
- **`R10`.** The fix touches no rider row. `readme-cli-stale` and `posix-mode-wording` were
  deleted in the same commit as their fixes (`87004fb`) and `waiver-live` took a touch note
  rather than deletion, its fix being design — all three re-checked against the diff, all three
  correct, and all three already covered by the FULL.

---

## 4. Findings

### `V-1` (low) — the comment justifying `errors="replace"` is falsified by one of the two lines it justifies

**Location:** `tooling/tests/document_harness/test_precommit_hook.py:95-98`, added by `71e1f24`.

The comment closes: *"The asserted lines are ASCII, which every candidate encoding preserves."*
There are two asserted lines. `BLOCKED_LINE` is pure ASCII, and the claim is true and
load-bearing for it — the check prints it through a locale-encoded stdout, so replacement
characters are the risk the sentence is answering. `MISSING_LINE` (`:48-50`) is **not** ASCII:
it carries U+2014 EM DASH, which is why the check's own findings are the ones that trip the
strict decode in the first place.

The behaviour is nonetheless correct, for a reason the comment does not give: `MISSING_LINE` is
`echo`ed by the shell wrapper, so it reaches the pipe as the hook file's own UTF-8 bytes, which
no console locale re-encodes. Measured — under `PYTHONIOENCODING=gbk` with `errors="replace"`
removed, `test_hook_is_loud_when_the_check_script_is_missing` still passed while the blocking
test crashed (`1 failed, 2 passed`). So the em dash round-trips; the stated invariant just is
not the one doing the work.

**Why low, not a blocker.** No test outcome changes, no guard weakens, nothing a decision turns
on. It is an inaccurate justification for a change that was itself disclosed rather than smuggled.

**Bytes supplied**, replacing the sentence beginning `The` at the end of `:97`:

```
    # BLOCKED_LINE — the one this decode can mangle, because the check prints it through a
    # locale-encoded stdout — is pure ASCII; MISSING_LINE carries an em dash but the hook
    # echoes it as the file's own UTF-8 bytes, which no console locale re-encodes.
```

Routing is the orchestrator's (`R10`): the record supplies the exact bytes, the path is not one
`E2` freezes, and no round has relied on the text.

### `V-2` (low) — two wrong line references inside the fix's own `HD-41` class-scan report

**Location:** the commit body of `71e1f24`.

The body reports the fix-leg class scan as *"README five command rows all sit under the new
:48-51 convention sentence; ONBOARDING :58/:75 under the :18-20 sentence."* Re-derived at tip:
the README sentence occupies **`:49-52`**, not `:48-51`, and the `ONBOARDING.md` sentence begins
mid-**`:17`** ("One command / convention: …"), not at `:18`. The conclusion is right — I
enumerated all seven sites myself in §2.1 and every one is covered — but the two enumerations
supporting it are off.

`HD-41` ④ (a `§live` ruling, which outranks the checklist) requires the grep **output** be
pasted into the commit body precisely so a reviewer can see the scan ran; this body summarises
instead, and a pasted `grep -n` is exactly what would have carried the right numbers. `E3` says
the same thing from the other side: path enumerations are emitted from the command that produces
them or omitted.

**Why low.** The scan really ran and its result is correct; the accurate numbers are one command
away and I recovered them. Recorded rather than waved through because the same summary-instead-of-
output form passed unfiled on the candidate at the FULL, and a shape that survives two legs
becomes the convention by default.

**No bytes appliable** — a commit body cannot be corrected without an amend, which `E8` forbids.
The repository's own channel for this is an errata commit; whether it is worth one is the
orchestrator's call, and banking it is a defensible answer.

### `O-1` (observation) — the class `B-1` named survives outside the round's files, including inside an `E10` member

Declared scope: all tracked files **excluding** the eleven the range touches. Class: a
reader-facing bare-`python` invocation. Live sites (historical records, archives and journals
excluded as quotations, the same call §2.1 makes inside the round):

```
document-harness/EXECUTION.md:364           `python -m pytest -q` run from `tooling`
assurance/templates/run-v2/README.md:14,16,18,19   `python assurance/templates/run-v2/run_*.py …`
```

`EXECUTION.md` is one of `E10`'s ten members — the executor's own standing instruction, telling
a POSIX executor to run a command that on the box this round measured does not exist. The four
`assurance/templates/run-v2/README.md` sites are caller-facing.

This is **outside both accepted findings and outside the round's declared change boundary**, and
the fix's scan scope (every file this round touched) was the correct scope for a fix leg — I am
not reporting a scan that was run too narrowly, I am reporting where the class lives next.
Whether it should be closed, and by which batch, is not mine to conclude (`R5`); it is named
here so the routing decision is made rather than defaulted. Note for whoever takes it: the
`EXECUTION.md` site is a member, so its fix is `E10` machinery, not a free-channel edit.

### `O-2` (observation) — the repair adds a fourth machine-side copy of a layer membership path

`MEMBER = "document-harness/CONSTRUCTION-CHECKLIST.md"` (`test_precommit_hook.py:58`) is a
hand-written member path, which is correct `E5` practice and is why the test binds. It is also a
fourth place a layer membership path now lives in code. Rider `E10-sync` registers three
(`E10`'s membership sentence, `layer_path_check.LAYER`, `test_precommit_checks.EXPECTED`) and
obliges a batch touching the membership sentence to change all three and name them in the commit
body; this fourth is not on that list.

Bounded honestly: the exposure is narrow and fail-safe. It bites only if *that one file* leaves
the layer, and then this test goes loudly red rather than quietly wrong. Recorded because the
rider's site count is now stale, not because the guard is weak.

### `O-3` (observation, wording-level per `R9`) — "stock Windows only `python`" was not measured, and is false on the machine that measured the other half

`README.md:51` and `document-harness/ONBOARDING.md:19-20` both read *"stock Ubuntu ships only
`python3` (measured 2026-08-23), stock Windows only `python`."* The parenthetical binds to the
Ubuntu half, which is careful writing — but the Windows half is asserted, and on the Windows box
this round ran on it does not hold:

```
$ where python           $ where python3
C:\Python313\python.exe   C:\Users\…\AppData\Local\Microsoft\WindowsApps\python3.exe
C:\Users\…\WindowsApps\python.exe

$ python --version → Python 3.13.6      $ python3 --version → Python 3.12.10
```

Both names resolve and both run. Read strictly, *stock* Windows ships neither.

No actor's action changes: the sentence's own opening clause — *"means whichever of `python3` /
`python` this platform actually runs … Substitute accordingly"* — already carries the correct
instruction, and the accurate fact is recoverable from that same sentence. `R9` wording-level;
it rides the next batch touching this text and spawns no round.

### `O-4` (observation) — what this VERIFY could not verify (`R4`)

Not folded into supported:

- **The fix's approval.** That the user approved this fix, and approved it at the boundary the
  body claims, is a conversation act. The commit body is its carrier; `R7` makes that a ceiling,
  not a block. Marked, not verified.
- **`actions/setup-python` putting `python` on the runner's PATH.** The fix's scan calls
  `ci.yml:25,27` machine-run and safe on that basis. Nothing is pushed — `origin/main` is still
  `f7fcbe9` — so the workflow still has zero runs and the README badge still has no status
  behind it. The FULL's `O-2` persists at this tip unchanged, and the reasoning is sound either
  way (if `python` is absent the workflow fails at its own install step, loudly), but it is
  inference, not measurement.
- **The `571 failed` figure under `jsonschema` 4.10.3.** I did not rebuild a 4.10.3 environment.
  Same ceiling the FULL recorded; outside the repair diff and untouched by it.
- **Mutation 1's disclaimer on a platform without `python`.** The docstring says a hook reverted
  to bare `python` "still resolves an interpreter and passes all three tests" on any machine
  where `python` exists. I confirmed that on Windows. I did not run the reverted hook on the
  POSIX box, so the claim's other half — that only a platform without `python` observes the
  preference — is verified in one direction only. `E4`'s point is that mutation proves binding
  force, not that the force is sufficient; that holds here too.

---

## 5. Coverage (`R4`)

**Read in full:** `document-harness/CONSTRUCTION-CHECKLIST.md` (my standing instruction, reached
through the superseded `v3-harness-review-contract.md` stub) · all five commit bodies in the
range · `migration/document-work-assurance-v3/v3-review-full-28dd80b.md` ·
`document-harness/plans/publicization-a.plan.md` · the whole repair diff ·
`tooling/tests/document_harness/test_precommit_hook.py` at tip · `.githooks/pre-commit` at base
and tip · `tooling/hooks/layer_path_check.py` · `.github/workflows/ci.yml` ·
`HARNESS-DECISIONS.md` `§live` (`HD-44 / HD-41 / HD-36 / HD-35 / HD-34 / HD-23 / HD-9`).

**Sampled:** `HARNESS-RIDERS.md` (row ids in full; `waiver-live`, `decited-paths`, `E10-sync`,
`submod-index` read whole) · `README.md` (*State of this repository* whole, rest by targeted
grep) · `document-harness/ONBOARDING.md` (preamble and both command rows) ·
`document-harness/EXECUTION.md` around `:358-370` · `document-harness/journal/pub-facade-2026-08-23.md`
via the FULL's account and the commit bodies.

**Probed by command:** seven hook mutations with digest-checked restore · the battery on Windows
and on POSIX at tip · collected counts at base and tip · the POSIX interpreter and `sh` probe ·
the `errors="replace"` reproduction under a `gbk` console · the class scan inside and outside
the round's files · `E2` blob ids at base and tip · all ten `E10` members against the range ·
push state · worktree state · commit-body trailer check · line-ending provenance of the hook.
Output pasted above rather than described.

**Process claims, marked not verified:** that the fix was authored in the round form the plan
declares; that the preview card was rendered; that the four rulings and the fix approval were
uttered. `R7` ceiling on each.

---

## 6. Verdict

**`REVIEWED_NO_BLOCKER`.**

`B-1` is closed at all seven sites the FULL enumerated, by the minimum fix it named and no more.
`B-2` is closed on the two mutations that survived it and on three further ones I added, with
the one behaviour that is still unpinned now written down as unpinned instead of claimed. The
suite is green on both platform families at this tip, 790 → 793 closes, and the permanent
boundaries — frozen bytes, the ten members, the budget, the git rules, the disclosure — are
each intact and each re-derived rather than read.

The two lows are both in what the repair *says about itself* rather than in what it does: a
comment whose reason is wrong about one of the two lines it covers, and two line numbers in a
scan report whose conclusion I independently confirmed. Neither would have earned a repair leg,
which is why neither is inflated into one. What the round did with its fix leg is the thing
worth recording: it took the reviewer's named minimum fix on both blockers, added no machinery
to either, and where a fixture was judged too expensive it narrowed the claim instead of
quietly leaving it standing.
