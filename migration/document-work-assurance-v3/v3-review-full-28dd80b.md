# V3 FULL review — round `PUB-FACADE`

- **Subject:** `f7fcbe906b3de29b6b52f64395d41d95a2779fad..28dd80b452c45a1224e4b87b78727b189bc37f86`
  (3 commits: `dd9c465` plan · `87004fb` candidate · `28dd80b` journal record)
- **Leg:** FULL. Derived from the repository: no FULL has occurred for this round, so `E9`'s
  budget is intact and this is the one FULL. If a fix is approved it is the one fix leg and
  obliges the targeted VERIFY.
- **Verdict: `CHANGES_REQUIRED`** — two blockers, both in the implementation.

---

## 0. What I read, and how (`R4`)

**In full:** `document-harness/CONSTRUCTION-CHECKLIST.md` (my standing instruction, reached via
the superseded `v3-harness-review-contract.md` stub) · the three commit bodies · the whole diff
of all 10 changed paths · `document-harness/plans/publicization-a.plan.md` ·
`document-harness/journal/pub-facade-2026-08-23.md` · `tooling/tests/document_harness/test_precommit_hook.py` ·
`.githooks/pre-commit` at both revisions · `HARNESS-DECISIONS.md` `§live` ·
`tooling/tests/document_harness/_harness.py`.

**Sampled:** `HARNESS-RIDERS.md` (the three rows this round touches, plus the rows my findings
route against) · `CONSTRUCTION-LEDGER.md` (current-pointer tail) · root `README.md` (the whole
*State of this repository* section; the rest by targeted grep).

**Probed by command:** the battery on Windows and on Linux · four mutations of the hook · the
README's own commands on POSIX · git's 644-hook behaviour on git 2.43.0 · the `readme-cli-stale`
site sweep · push state · `E2` surface · collected-test arithmetic. Output pasted below.

**Not verified, and not folded into supported:** the `571 failed` figure under Ubuntu's system
`jsonschema` 4.10.3 (I did not rebuild a 4.10.3 environment; I did confirm the *mechanism* — the
suite really does pass `registry=` to `Draft202012Validator`, at `tooling/rsclib/document_harness/review.py:113,116`
and `review_subject.py:96,99`, so a floor above 4.18 is real, not decorative) · that the CI
workflow passes (it has never run — see `O-2`) · that the preview card was rendered and the four
user rulings were actually uttered (`E11`, process claims; the plan is their committed carrier,
which is what the repository can show, and `R7` says an authorization I cannot see is a ceiling,
not a block).

---

## 1. Implementation (`R3` — led with, as required)

### `B-1` — blocker. The round's own defect class survives in, and was newly written into, its two reader-facing work files.

**Location:** `README.md:57` and `README.md:58` (both **added by this round**, `87004fb`);
same class pre-existing at `README.md:51`, `:52`, `:53`, and at
`document-harness/ONBOARDING.md:55`, `:72` (a file this round also edits).

**Scope of my scan** (`HD-41` ①, declared before the command): every path the subject range
changes, grepping for a *runnable* bare-`python` invocation addressed to a reader. Result — 7
human-facing sites in 2 work files, 2 of them new this round:

```
--- README.md
51:| Does the suite pass? | `python -m pytest -q` |
52:| Why does a test fail? | `python -m pytest -q --tb=line` |
53:| Do the instruction layer's ten members resolve here? | `python -c "import sys,pathlib; ...
57:| Is there a CLI? | `ls tooling/dtw.py`; `python tooling/dtw.py --help` lists its commands ...
58:| What does the suite need? | Python >= 3.12 and `python -m pip install pytest "jsonschema>=4.18" referencing` ...
--- document-harness/ONBOARDING.md
55:| **See** | ... and `python <mount-path>/tooling/dtw.py --help` lists the eight operations. ...
72:| **Do** | `python <mount-path>/tooling/dtw.py init --repo-root .` from the caller's root ...
```

**Measured, at the subject tip, in a fresh clone, on the same POSIX box this round used to
discover the defect:**

```
$ wsl -e bash -lc 'command -v python'
(prints nothing)
$ command -v python3
/usr/bin/python3

# fresh clone at 28dd80b, running the README's rows verbatim:
--- README:57  python tooling/dtw.py --help
bash: line 1: python: command not found
--- README:58  python -m pip install pytest "jsonschema>=4.18" referencing
bash: line 1: python: command not found
--- README:51  python -m pytest -q
bash: line 1: python: command not found
```

**Ground truth violated.**

1. `E7` — *test the defect class, not the reported instance*. The class this round discovered is
   "this repository's own artifacts invoke a `python` that the platform does not have." The round
   found it twice (the hook, the `command_exit` fixture argv), fixed both, and stopped. The class
   scan it ran was declared over `tooling/*.py` and is honest at that scope — I re-derived its
   count and it is exactly right (4 remaining hits, none executed). But that scope structurally
   cannot see the two files the round was editing at the same time.
2. `HD-41` ④ (`§live`, and the decision register outranks the checklist) — *修 finding 先扫类后
   落笔：改动前 grep 该断言的关键字串在**本轮全部工作文件**里的命中*. The obligation names the
   round's whole work-file set; the scan covered one directory of it.
3. The round's own plan, *Expectations the FULL can hold the candidate to*: "no new unverified
   claim replaces them (the section's own rule: commands over claims)." The section's contract is
   its own heading — **"State of this repository — run these, do not trust a sentence."** Two new
   commands were added that do not run on one of the two platforms this same commit wired into CI.
   That is the defect the section exists to prevent, committed inside the round that de-rusted it.

**Why this is a blocker and not a low.** The round's declared purpose is the facade — "what a
stranger meets in the first minute" — and batch A's whole content is the first minute. The failure
lands on the newly added *"What does the suite need?"* row, which is setup instruction and nothing
else. And this is the round's own freshly measured defect class, reproduced by the round in its
headline deliverable.

**Honest bound on the claim:** `python` does exist on plenty of Linux installs (`python-is-python3`,
a venv, pyenv, conda). The assertion I am making is not "these always fail on POSIX" — it is that
on the exact environment this round measured, and on which it based the hook fix, all seven sites
fail, and two of them are new.

**Minimum fix.** The text changes, and no machinery is added (`E6`). One sentence at the head of
the *State of this repository* table naming the interpreter convention — that `python` there means
whichever of `python3` / `python` runs on the reader's platform, the same probe `.githooks/pre-commit`
now performs — redeems all five README sites at once; `ONBOARDING.md`'s two sites take the same
sentence or `python3` directly, since a second caller is by assumption not on the author's machine.

---

### `B-2` — blocker. The new guard does not bind two of the three wrapper behaviours it says it pins.

**Location:** `tooling/tests/document_harness/test_precommit_hook.py`, specifically
`test_hook_resolves_an_interpreter_and_runs_the_check` (`:76-86`) and the file docstring's claim
at `:12-16` — *"Both halves of the hook's contract are pinned: the working half (an interpreter is
resolved and the layer check runs …)"*.

**Method** (`R8` — mutation reproducing the real defect shape, never a crash): scratch clone at
`28dd80b`, hook preserved to a sha256-checked copy and restored to a verified digest after every
mutation. Restore digest checked identical before and after each run:
`66137d289517394ae9bacc6abd7d48cf79553519fb279bc74003b06f3a549bf0`.

| # | mutation | expected if the guard binds | measured |
|---|---|---|---|
| 1 | hook reverted to the pre-fix bytes (`git show f7fcbe9:.githooks/pre-commit`, bare `python`) — **the exact defect this round exists to fix** | RED | **`2 passed`** (Windows) |
| 2 | whole hook replaced by `#!/bin/sh` + `exit 0` — resolves nothing, runs nothing | RED | **test 1 passes** (only test 2 fails) |
| 3 | the loud missing-check `echo` deleted | RED | **RED** — `test_hook_is_loud_when_the_check_script_is_missing` FAILED |
| 4 | `if [ "$status" -ne 0 ]` → `if false` — **a failing layer check no longer blocks the commit** | RED | **`2 passed`** |

Mutation 3 is the control and it works: the hand-written `MISSING_LINE` literal is correct `E5`
practice (independent of the hook, whole-line assertion) and it does bind.

**What the table means.**

- **Mutation 2 falsifies the docstring directly.** A hook that resolves no interpreter and runs no
  check satisfies `test_hook_resolves_an_interpreter_and_runs_the_check`. The test's only assertion
  is `returncode == 0`; nothing in it can distinguish "the check ran and passed" from "nothing ran
  at all." The name and the docstring claim the first; the assertion buys the second.
- **Mutation 4 is the more consequential half.** Propagating a non-zero status from
  `layer_path_check.py` is the entire reason the hook exists — it is what makes it a guard rather
  than a script. It is unpinned here, and unpinned everywhere: grepping `tooling/tests/` for any
  other test touching the wrapper returns nothing but this file. The docstring's out-of-scope note
  defers "the check's own semantics" to `test_precommit_checks.py`, which is right — but status
  propagation is *wrapper* semantics, which this file claims to own.
- **Mutation 1 is not caught in any environment this repository runs on its own.** It goes RED only
  where `python` is absent. I confirmed both directions:

```
# Windows (where the battery runs):        2 passed
# POSIX (WSL, no `python`):
FAILED tooling/tests/document_harness/test_precommit_hook.py::...::test_hook_resolves_an_interpreter_and_runs_the_check
1 failed, 1 passed in 0.08s
# bytes restored:                          2 passed in 0.06s
```

  The new CI does not close this, and the workflow's own bytes settle it without needing a CI run.
  `.github/workflows/ci.yml:25,27` themselves invoke bare `python` after `actions/setup-python@v5`.
  So either (a) `python` is on PATH on the ubuntu runner — in which case the reverted hook resolves
  it and mutation 1 stays green in CI too — or (b) it is not, in which case the workflow fails at
  its own install step. Either way the interpreter pin binds nowhere automated; the only place it
  ever went red was a manual WSL run that nothing re-creates.

**Ground truth violated.** `R3` — the guards must bind, and the implementation must do what it
claims; `E4` — *never trust a guard you have not seen fail*, whose point is a guard that stays red
when the defect returns. `E4`'s letter was met at authoring time (the journal records neuter → red →
restore, and I reproduced that RED myself); what fails is durability and the docstring's scope claim.

**Minimum fix.** Inside the test file the round already wrote — no new machinery (`E6`):
(i) make test 1 assert something only a hook that actually ran the check can produce, rather than
`exit 0`. The round already performed exactly this experiment by hand in WSL and recorded it in the
journal (stage a resolve-nowhere token into an instruction-layer member, expect exit 1 and the
check's own `pre-commit BLOCKED:` line); committing that as the assertion closes mutations 2 and 4
together, since a hook that swallows a non-zero status can no longer produce it. (ii) If the
python3-preference is to be pinned rather than merely fixed, it needs a case that runs the hook with
a PATH holding `python3` but not `python`; if the round judges that fixture not worth its cost, the
honest move is to narrow the docstring's "both halves" claim to what is actually pinned.

---

### What is correct, and verified

Recorded because a FULL that lists only defects misreports the round.

- **The suite.** 790 collected at base → 792 at tip; `792 passed in 99.54s` on Windows
  (re-derived, matches the commit body's 792/99.04s), and **`792 passed, 865 subtests passed in
  11.22s` on Linux** in a fresh clone at `28dd80b` — the round's central POSIX claim, independently
  reproduced.
- **`test_candidate_checks.py:523`.** `sys.executable` is correct and `import sys` is already
  present at `:37`, so the module-level `VALID_CONFIGS` evaluates. The Linux green above is the
  proof this was the sole executed site.
- **The hook fix itself is right,** independently of `B-2`: probing `command -v` *and* `"$CAND" -c pass`
  is the correct shape, and the comment's reason for the second probe (a PATH name that resolves but
  does not run) is a real Windows failure mode, not a guess.
- **`ONBOARDING.md` item 9 — verified verbatim.** I reproduced it on git 2.43.0:

```
hint: The '.githooks/pre-commit' hook was ignored because it's not set as executable.
hint: You can disable this warning with `git config advice.ignoredHook false`.
[main (root-commit) 8329806] t
```

  The rewritten sentence is accurate on all three counts — the hint text is verbatim, the commit
  does land unchecked, and `advice.ignoredHook` really can suppress it. The hedge ("the reliable
  signal is the commit landing unchecked, not the message") is the right one. Rider
  `posix-mode-wording` is properly redeemed, in the review record's favour as the plan says.
- **Rider `readme-cli-stale` fully redeemed — all four sites, not the three the plan's change-surface
  table listed.** I swept each named string at the tip: `Re-rooting` → GONE, `The CLI is not here`
  → GONE, `will not make the suite green` → GONE, `No remote` → one hit at `:84`, which is this
  round's own disclosed historical quotation and not an assertion. Scan B in the commit body called
  that hit correctly.
- **`README.md`'s surviving `RS_ROOT = parents[3]` claim is true** — I checked, expecting drift after
  the de-prefix round: `tooling/rsclib/document_harness/__init__.py:38` really is `parents[3]`.
- **CI dependency floor is right and the matrix matches the measurements** (3.12/3.13 = the two
  interpreter versions actually measured). No third-party import outside `jsonschema` / `referencing`;
  `TempRepo` sets `user.email` / `user.name` / `commit.gpgsign false`, so a runner with no git identity
  will not break the suite; nothing in the suite reads this repository's own history, so
  `actions/checkout@v4`'s shallow default is safe. The `sh`-absent leg degrades to skip, not failure.

---

## 2. Process and boundary (`R3` — run second)

All clean; each re-derived, none accepted as reported.

- **`E9` budget.** No prior FULL → all three commits are pre-submission and consume nothing. Intact.
- **`E8`.** Titles `V3-PUB-FACADE-{PLAN,,JOURNAL}-v1` name the round and match the repository's
  established suffix practice; each body opens with its kind (`plan (ruling carrier)` / `candidate` /
  `record`); one dense paragraph each; **no trailers**. **No push** — `git rev-list --left-right
  --count origin/main...HEAD` → `0	3`, and `origin/main` is still `f7fcbe9`.
- **`E2`.** No path under `contract/` or `schema/document-assurance-v3/` appears in the range. The
  frozen surface is untouched.
- **`E10`.** No member is touched, so no amendment machinery and no `E10-sync` is due — the
  membership sentence, `LAYER`, and `EXPECTED` all stand unchanged. The opening cold read was waived
  by the user, which the clause permits.
- **`E1`.** The `HD-55` exception channel is taken, and taken correctly: the candidate body states
  that the executor held **all four** of `R1`'s holdings and says "nothing about this candidate's
  authoring is independent" rather than claiming otherwise. Carrier is the commit body, statement is
  the orchestrator's — both as `E1` requires. The FULL was dispatched cold with the range and nothing
  else, so the review side is structurally independent.
- **`E12`.** `.harness/review-pending.json` records the range with a **written tip**, which the rule
  forbids for a range recorded in a file. It is nonetheless conformant in substance and I am not
  filing it: `.harness/` is gitignored (`.gitignore:18`), so writing it is not a commit inside the
  round, the rationale the rule states ("a written tip is short by at least the commit that wrote it")
  does not arise, and I confirmed the written tip equals `HEAD`. Nothing is dropped.
- **`E3`.** Every figure I could re-derive matched: 790 → 792, the Windows tail, the Linux tail, the
  scan-A count of 4, the `readme-cli-stale` site sweep. The commit body pastes output rather than
  describing it, and the journal's discipline of voiding a broken measurement channel rather than
  quietly keeping its conclusions is the correct behaviour under this rule.
- **`R10` routing.** `readme-cli-stale` and `posix-mode-wording` are deleted in the same commit as
  their fixes; `waiver-live` takes a touch note and is not deleted, correctly, since its fix is design.

---

## 3. Observations (`R5` — reported, not concluded)

- **`O-1` — `E4`'s restoration route, disclosed in advance.** The journal states plainly that the
  RED evidence was restored by `git checkout --` in a disposable clone rather than from sha256-checked
  scratchpad copies, and names it "so the FULL can weigh the letter of `E4` against that substance
  rather than discover it." I weigh it as sound: the mutated bytes never existed in this repository
  and the clone was discarded. Recorded with no action asked, because disclosing a departure before
  the reviewer finds it is the behaviour the rule wants.
- **`O-2` — the CI has never run, and cannot have.** `origin/main` is at the base and nothing is
  pushed, so the workflow has zero runs and the new README badge currently renders a workflow with no
  status. This is not a false claim — a badge self-corrects on first push — but it means no leg of
  this round can certify the CI passes. What I could substitute, I did: the suite is green at this
  tip on both platform families the matrix names.
- **`O-3` — a prose count survives in a file this round edited.** `document-harness/ONBOARDING.md:55`
  says `dtw --help` "lists the eight operations." I checked: it is **true today** (8 subcommands).
  It is nevertheless the same count-in-prose shape the round's own README change just refused for
  itself ("a count written here went stale twice … so none is written"). Recorded, not filed, because
  it is accurate — the next round touching `ONBOARDING.md` can decide whether the refusal generalises.
- **`O-4` — shape.** No component-accretion pattern in this round; it removed more claim surface than
  it added. Noted so the absence is on the record rather than unexamined.

---

## 4. Verdict

**`CHANGES_REQUIRED`** — `B-1` and `B-2`.

Both are implementation findings and both fit one repair leg. Neither asks for new machinery: `B-1`
is text changing at the sites the class scan should have reached, and `B-2` is a stronger assertion
inside a test file the round already wrote. `E9`'s test does not expire at closeout, so whichever of
these the user accepts becomes this round's one user-approved fix and obliges the targeted VERIFY.

Nothing here disturbs the round's substance: the hook fix, the fixture fix, the ONBOARDING rewrite,
the rider redemptions, the license and the CI matrix are all correct, and the POSIX result the whole
batch rests on reproduced exactly. What both blockers share is the last step — the round measured a
defect class precisely and then stopped one file short of sweeping it, and pinned one of three
behaviours while writing that it had pinned two.
