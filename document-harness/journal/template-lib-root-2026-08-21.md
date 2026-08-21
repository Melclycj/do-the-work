# Round journal — TEMPLATE-LIB-ROOT (2026-08-21)

The construction round that repaired the two run-v2 template scripts which could not import
the harness library at all when pointed at a caller's run directory. It is the narrowed
first slice of the re-rooting item's third piece: the user ruled the queue head on
2026-08-21 after the defect surfaced while the two queued candidates were being scoped.

**Root cause.** In `check_template_instance.py` and `make_paragraph_map.py` a single
variable, `repo_root`, did two jobs — it located the library as
`repo_root/ResearchSystem/tooling`, and it was the repository the instruction is pinned in,
handed to `git -C`. Before the repository split those were one tree. Since the split the
argument names the **caller's** repository, which holds run data and no library, so the two
jobs need two answers. The four `run_*.py` siblings already separate them, computing the
library from `__file__` and keeping the root argument for git; the fix is that shape applied
to the other two.

## The chain

cold read `v3-cold-read-39e395e.md` (0 must-fix · 1 low · 4 observations; all ten members
read end to end, discharging the read PREVIEW-RENDER deferred for `EXECUTION.md` and
`REVIEW.md`), record `3067efc` → candidate `83e3191` → FULL `v3-review-full-83e3191.md`
**CHANGES_REQUIRED** (`B-1` blocker · 2 lows · 4 observations), record `08665d3` → one
user-approved fix, this commit → targeted VERIFY, owed.

`E9`: one FULL, one user-approved fix, one targeted VERIFY — nothing else consumed.

## In-round user rulings (2026-08-21, two cards, in session)

1. **Queue head: repair the break first, as a narrowed round.** The alternatives put to the
   user were the re-rooting item's third piece entire (12 resolution points across 7 files;
   the ledger's figure of 11 was stale, `cli.py` having gained one with the `init` and
   `preview` commands) and contract v4. Neither was chosen; both stay queued.
2. **Fix boundary: the blocker plus both lows** — the `E1` errata, this journal with its
   evidence pasted, and the docstring's falsified quantifier. `O-1` was excluded on the
   reviewer's own reasoning that it would burn the repair for no change in what the guard
   catches (`E6`).

## `E1` — which of the four holdings the executor held (the `B-1` errata)

**This section is the errata `B-1` requires.** The candidate `83e3191`'s body stated that
orchestrator and executor were one work-side session and then concluded that "the executor
held none of the four, so the read's independence is structural, and the same will hold for
the FULL". That conclusion is withdrawn. It is not available: `R1`'s premise for structural
independence is that *the orchestrator holds the dispatch*, and where one session holds both
roles there is no separate orchestrator for the premise to name. `HD-46` records the user's
tiebreak for exactly this middle state — record which holdings were held, and do not claim
structural independence.

**What was actually held.** Orchestrator and executor were one work-side session. All four
of `R1`'s holdings sat with it in the operational sense: it ran `dtw dispatch` for both the
read and the FULL (*dispatched by*); it handed each reviewer the CLI's derived text plus two
operational sentences of its own — the repository root, and the instruction to write without
committing (*prompted by*); the range `39e395e..HEAD` was machine-resolved but from a base
and tip that session chose (*scoped by*); and it commits each returned record (*reported
through*). **The round does not call its reviews structurally independent.** Both reviewers
started cold, took the member set and every figure from the repository rather than from the
dispatch, and re-executed the battery and the mutations rather than accepting them — which
is a discipline kept against oneself, not a structure. The pre-declaration of the FULL's
independence, written before that review existed, is withdrawn with the rest: it was the
anchoring `R2` exists to refuse, and the FULL refused it.

## Evidence, pasted rather than described (`E3`)

All of it re-run at the fix commit's tree, not recalled from the candidate's session.

### RED — the pre-fix bytes, recovered with `git show 39e395e:`

Against a disposable caller-shaped repository (a temp git repo with the instruction pinned
at a real commit and the run directory at `ResearchSystem/assurance/runs/run-red`):

```
$ python -X utf8 check_template_instance.py <run-dir> <repo-root>
ModuleNotFoundError: No module named 'rsclib'
exit=1
$ python -X utf8 make_paragraph_map.py <run-dir> <repo-root>
ModuleNotFoundError: No module named 'rsclib'
exit=1
```

Against the caller's own `p5b-claims` run directory — the read-only gate only, because
`make_paragraph_map.py` writes and is never pointed there again (see the boundary section):

```
$ python -X utf8 <pre-fix check_template_instance.py> <caller run-dir> <caller root>
ImportError: cannot import name 'load_json' from 'rsclib.document_harness' (unknown location)
exit=1
```

The two diagnostics differ only in what the tree being reached into holds: the fixture has
no `rsclib` at all, while the caller still has one whose `document_harness` package was
removed by the split, leaving a namespace package with no `load_json`.

### GREEN — the same invocations at the fixed tree

```
$ python -X utf8 assurance/templates/run-v2/make_paragraph_map.py <run-dir> <repo-root>
instruction read from: pinned revision
wrote 3 paragraph(s) to ...\run-red\control\paragraph-map.json
exit=0
$ python -X utf8 assurance/templates/run-v2/check_template_instance.py <run-dir> <repo-root>
TEMPLATE-PREAMBLE-UNMAPPED: ...
TEMPLATE-PARAGRAPH-MAP-MISSING: ...
authoring gate: 2 issue(s)
exit=1
$ python -X utf8 assurance/templates/run-v2/check_template_instance.py <caller run-dir> <caller root>
form-conditional   : preamble gate and paragraph map skipped (SIMP-B1) ...
authoring gate: PASS
exit=0
```

The fixture's gate exits 1 on its own merits — that fixture has an unmapped preamble and no
paragraph map — which is the point: it reaches a verdict of its own instead of dying at
import. The caller's real run passes.

### Mutation (`E4`, `R8`) — three, each applied alone

Two of the three use the exact pre-fix bytes rather than a synthetic break.

```
### M — make_paragraph_map.py restored to its pre-fix bytes (git show 39e395e:)
FAILED ...::RepairedScriptsFindTheLibraryFromTheirOwnTree::test_make_paragraph_map_writes_the_skeleton
1 failed, 3 passed in 1.44s

### M — check_template_instance.py restored to its pre-fix bytes (git show 39e395e:)
FAILED ...::RepairedScriptsFindTheLibraryFromTheirOwnTree::test_the_authoring_gate_reaches_its_own_verdict
1 failed, 3 passed in 1.45s

### M — run_repair.py RS_ROOT depth parents[2] -> parents[1]
FAILED ...::SelfLocatingScriptsStayThatWay::test_each_prints_its_usage_after_importing_the_library
1 failed, 3 passed in 1.28s
```

Restoration was from sha256-checked scratchpad copies, never `git checkout --`, and checked
twice over — by hash and against the committed blobs:

```
9b774fe2a5a6891a1616b08e4e4ee425fdedc50bc3eb9a07e11349d4270a0f2a *check_template_instance.py
b68516af76b2bc0b7cd2ebf7e3a206468dc872b21b99b8f0c36370ca2c8f7097 *make_paragraph_map.py
c02c542753f1a36a02e979e7af03ffd29c874fd963fad1b89549c4fe3d91bd5d *run_repair.py

check_template_instance.py  worktree=692773ff5519  HEAD=692773ff5519
make_paragraph_map.py       worktree=27bb7e0149e5  HEAD=27bb7e0149e5
run_repair.py               worktree=c72edabe4c10  HEAD=c72edabe4c10
```

The third mutation is what makes the four `--help` cases a guard rather than decoration: a
sibling that was already correct goes red when its depth is wrong.

### The battery

```
$ python -m pytest -q
774 passed in 124.69s (0:02:04)
```

770 at the round's base `39e395e`; the four added are this round's new file.

## The boundary, and the breach inside it

The declared surface was the two scripts plus tests, with the caller repository at **zero
writes**. While verifying the fix the work-side session ran `make_paragraph_map.py` against
the caller's real `p5b-claims` run directory, and it wrote `control/paragraph-map.json`
there — a file git had never tracked. It was deleted immediately and the caller's
`git status` confirmed back to the two modifications that predated the session. Every
verification since has used disposable fixtures, which is also what the new test file does,
and the read-only gate is the only script pointed at the caller above.

The FULL's `O-3` records the structural point rather than the fault: `ORCHESTRATION.md`
routes "a boundary it would have to exceed" from executor to orchestrator to **user**,
before the fact. With both roles in one session that route had nowhere to go, and the breach
was disclosed after rather than approved before. Whether the route should have a form for
one-session rounds is the user's question under `R5`; it is carried to the closeout, not
answered here.

## Finding dispositions

- **cold read `L-1`** (the SIMP-C4 wiring sentence carries an unscoped ruling inside a
  form-scoped bullet): banks. Its prior question — was the 2026-08-21 rendering ruling scoped
  to the enumerated form or general? — is the user's under `R5` and goes to the closeout; the
  fix adds a bound either way, so `E10`'s design test closes the free channel to it and the
  row names a round-eligible surface.
- **cold read `O-2`** (two stale line pointers in the rider bank): both corrected at closeout.
- **cold read `O-1` / `O-3` / `O-4`**: no action — a routing note that changes nothing, a
  reproduction of the previous read's discharged findings, and a known rider's blind spot.
- **FULL `B-1`**: this journal's `E1` section is the errata.
- **FULL `L-1`** (RED cited to a journal that did not exist): this file, with the commands
  pasted; the test docstring now names it and states both diagnostics.
- **FULL `L-2`** (a falsified absolute quantifier, the `HD-41` ② shape): the docstring now
  gives the real reason nothing reaches the `parents[3]` default — two invocations pass a
  root, four exit at argparse, one is a standalone probe.
- **FULL `O-1`** (a substring assertion where a whole line was available): excluded from the
  fix by user ruling 2, on the reviewer's own reasoning. The record carries it.
- **FULL `O-2`** (mutation evidence described, not pasted): answered by the evidence section
  above, which is the carrier its root cause was missing.
- **FULL `O-3`**: see the boundary section; the `R5` question goes to the closeout.
- **FULL `O-4`**: the reviewer's own `R4` ceiling — the preview card and the user's approval
  are chat-side and unverifiable from the repository. Stated, not folded into supported.

## Layer debt this round leaves

None. No instruction-layer member changed, and the opening cold read read all ten end to end
at `39e395e`, so nothing rides the next round's opening read.
