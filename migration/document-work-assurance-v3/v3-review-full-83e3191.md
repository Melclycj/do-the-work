# FULL review — round `TEMPLATE-LIB-ROOT` at `83e3191`

**Verdict: `CHANGES_REQUIRED`.** 1 blocker, 2 low, 4 observations.

**The implementation is clean and I could not break it.** The fix is a deletion plus six
lines that make two scripts locate their library exactly as their four siblings already do;
it adds no machinery, it closes the defect class repository-wide rather than the two reported
instances, and its new guard binds under every mutation I could aim at it — four mutations,
four distinct reds, each restore verified by sha256. The battery figure the round claims is
the figure I measured. Nothing frozen was touched.

The blocker is in the boundary check, and it is not about the code. Commit `83e3191`'s body
discloses in one breath that **orchestrator and executor were one work-side session** and
that **the executor held none of `R1`'s four holdings, so independence is structural**. Those
two clauses cannot both be true, `E1` forbids the second in exactly this shape, `HD-46`'s
recorded user tiebreak names this shape when it forbids it, and the two immediately preceding
rounds — one of them acting on a FULL finding about this very sentence — wrote the opposite
and correct form. This is a regression in a governance claim, not a wording slip: it is the
claim that decides whether this review counts as structurally independent, and it was made
about my review before my review existed.

---

## 1. Subject, round and budget — re-derived, nothing taken from the dispatch

The dispatch handed one range and nothing else. Everything below is from the repository.

**Subject.** `39e395e5221f5cbf0a1ab729c0822e20f6873994..83e3191697ace9cf65cc8625b1ef4ea69fdc6a99`,
two commits. `83e3191` is `HEAD`. The worktree was clean at the start of this review and clean
at its end (`git status --porcelain` → empty, run at open, after every mutation restore, and
at close).

| commit | title | kind (named in its own body) |
|---|---|---|
| `3067efc` | `V3-REVIEW-RECORD-TEMPLATE-LIB-ROOT-39e395e-v1` | record |
| `83e3191` | `V3-TEMPLATE-LIB-ROOT-v1` | candidate |

**Round.** `TEMPLATE-LIB-ROOT`, taken from the two commit titles, which are the only place in
the repository that names it — `grep -rln "TEMPLATE-LIB-ROOT"` outside `.git` returns the new
test file and its `__pycache__` sibling, nothing else. There is **no round journal**
(`document-harness/journal/` holds no `template*` or `*lib-root*` file), no ledger entry, and
no plan naming the round. That absence is load-bearing for `L-1` below.

**Budget (`E9`).** The test is *has a valid independent FULL already occurred?* No
`v3-review-full-*` or `v3-review-verify-*` record exists for this round —
`migration/document-work-assurance-v3/` holds exactly one record whose subject falls in this
range, `v3-cold-read-39e395e.md`, and `E10`/`R3` are explicit that a read is not a round and
spends no budget. So **this dispatch is the round's one FULL**, the budget is whole, and a
fix arising from this record would be the round's single user-approved fix and would oblige a
targeted VERIFY.

**Review window (`E9`).** `.harness/review-pending.json` records the subject as exactly this
range, dispatched `2026-08-21T11:37:23+00:00`; `83e3191` was committed `2026-08-21 21:37:13
+1000` = `11:37:13Z`, ten seconds earlier. No commit has landed since dispatch, and
`.harness/` is ignored (`git check-ignore -v` → `.gitignore:18:.harness/`), so the marker is
not itself a commit. The window is intact.

**Authorization (`R7`).** `E11`'s preview card and the user's approval of it are chat-side and
are not in the repository. I state the ceiling and move on: **I cannot see that this round was
authorized**, and I have treated that as a hint, not a block.

**Instruction layer (`E10`).** No changed path is a member of the ten, so the candidate owes
no amendment and no independent read. The round's opening cold read was dispatched and its
record landed at `3067efc` before the candidate — the correct order, and it discharges the
read the previous round deferred.

**Frozen bytes (`E2`).** `git diff --name-only 39e395e 83e3191 -- contract/ schema/` returns
**0 paths**. At `HEAD` the three frozen blobs still hash to their named ids —
`b2dbdf752d8c155e…` (contract), `68031fa2ca31272e…` (supersession-1), `e1a2f26b1d8d323d…`
(supersession-2) — and `schema/document-assurance-v3/` holds **15** files, the re-baselined
count. Nothing frozen was written, so no `E2` ruling was owed.

## 2. Changed paths, classified by hand

Four paths, classified by reading them, not by trusting the body:

| path | class | in the declared boundary? |
|---|---|---|
| `assurance/templates/run-v2/check_template_instance.py` | product-run template script | yes |
| `assurance/templates/run-v2/make_paragraph_map.py` | product-run template script | yes |
| `tooling/tests/document_harness_review/test_run_v2_template_library_path.py` | new guard | yes |
| `migration/document-work-assurance-v3/v3-cold-read-39e395e.md` | review record (`R6` channel) | record commit, not the candidate |

`git diff --stat` over the range: 693 insertions, 2 deletions across the four. The two script
diffs are each `+7 / −1`.

## 3. Re-executed, not accepted

### 3.1 The fix is the siblings' shape, and the shape is right for how these scripts run

Both scripts gain the same module-level block and lose the argument-derived insert. I checked
the claim that this is the four siblings' shape by reading all six:

```
run_bind_v2.py:48-50      HERE / RS_ROOT = HERE.parents[2] / sys.path.insert(0, str(RS_ROOT / "tooling"))
run_evidence_v2.py:36-38  (same)
run_repair.py:44-46       (same)
run_retire.py:54-56       (same)
check_template_instance.py:48-50  (added this round)
make_paragraph_map.py:27-29       (added this round)
```

`HERE.parents[2]` is correct **because these scripts are invoked in place**, which I confirmed
from `assurance/templates/run-v2/README.md:6-10`: since `HD-11` part two the six shared
scripts "are called **in place** from `assurance/templates/run-v2/` against the run directory,
zero copies", and `compare_blocks.py` is "the one template member still copied". I confirmed
`compare_blocks.py` imports no `rsclib` (stdlib only), so its exclusion from the guard is
correct, not an oversight — the class is scripts that must locate the library, and it has six
members, not seven. Because the resolution is relative to `__file__`, it also survives the
submodule mount and the `HD-34` copy escape hatch, which the argument-derived form did not.

### 3.2 The defect class is closed repository-wide

Two sweeps, scope = all tracked `*.py` outside `__pycache__`:

```
$ grep -rn "sys.path.insert\|sys.path.append" --include=*.py .    → 13 sites
$ grep -rn '"ResearchSystem"' --include=*.py .                    → 4 sites, all test fixtures
```

Every one of the 13 inserts now derives from `__file__`; **no argument-derived library path
remains anywhere in the repository**. Cross-checking from the other direction, every file
importing `rsclib` either carries a `__file__`-based insert (the six templates plus
`do-the-work.py`, `dtw.py`, `candidate_path_check.py`) or is library-internal / a test whose
path comes from `_harness`. `E7` is satisfied on the class, not the instance.

### 3.3 The battery

Re-run by me at `HEAD`, immediately before this claim:

```
$ python -m pytest -q
774 passed in 122.10s (0:02:02)
```

That is the round's claimed figure exactly. The claimed base of 770 I confirmed transitively:
mutations 1 and 2 below each returned `1 failed, 773 passed`, so the file contributes 4 tests
and the base was 770.

### 3.4 Mutation of the new guard (`R8`, `E4` shape)

Four mutations, each applied alone, each restored from a sha256-checked scratchpad copy taken
before any mutation, never `git checkout --`. Mutations 1 and 2 use the **exact pre-fix bytes**
(`git show 39e395e:<path>`), so they reproduce the real defect shape rather than a synthetic
break.

| # | mutation | result | red test |
|---|---|---|---|
| 1 | `check_template_instance.py` → pre-fix bytes (byte-identical to base, verified by `diff`) | `1 failed, 773 passed in 142.00s` | `…::RepairedScriptsFindTheLibraryFromTheirOwnTree::test_the_authoring_gate_reaches_its_own_verdict` |
| 2 | `make_paragraph_map.py` → pre-fix bytes | `1 failed, 773 passed in 143.04s` | `…::RepairedScriptsFindTheLibraryFromTheirOwnTree::test_make_paragraph_map_writes_the_skeleton` |
| 3 | `run_repair.py` `RS_ROOT = HERE.parents[2]` → `parents[1]` | `1 failed, 773 passed in 141.54s` | `…::SelfLocatingScriptsStayThatWay::test_each_prints_its_usage_after_importing_the_library` |
| 4 | `assert_library_was_found` body → `return  # NEUTERED` | `1 failed, 3 passed in 2.23s` | `…::TheProbeCanFail::test_a_process_that_cannot_find_the_library_is_observed_failing` |

Four distinct reds, no overlap. Mutation 1's failure text is the whole point of the round:

```
AssertionError: 'ModuleNotFoundError' unexpectedly found in 'Traceback (most recent call last):
  File "…\check_template_instance.py", line 190, in main
    from rsclib.document_harness import load_json, validate  # noqa: E402
ModuleNotFoundError: No module named 'rsclib''
```

Mutations 1 and 2 also independently establish the round's central claim about why the defect
was invisible: with a dead script in the tree, **773 other tests stayed green**. Mutation 3 is
the one that matters most for durability — it proves the four regression pins are not
decoration: a wrong depth on a script nobody touched this round is caught. Mutation 4 proves
the negative control is a control and not a comment.

Restores verified by sha256 equality against the pre-mutation copies:
`check_template_instance.py` `9b774fe2a5a6891a…`, `make_paragraph_map.py` `b68516af76b2bc0b…`,
`run_repair.py` `c02c542753f1a36a…`, each identical before and after.

### 3.5 The negative control's premise, probed

`TheProbeCanFail` is only meaningful if `rsclib` is not ambiently importable — otherwise every
assertion in the file would pass vacuously. Run from outside the repository:

```
$ cd /c/Users/…/Temp && python -c "import rsclib"
ModuleNotFoundError: No module named 'rsclib'
```

The premise holds. The guard's `IMPORT_DIAGNOSTICS` tuple covers `ModuleNotFoundError`,
`ImportError` and `Traceback`, so it is not over-fitted to the single error string the caller
reported; the fixture reproduces a different one and is caught all the same.

### 3.6 `E5` — the guard's expectations are independent of the guarded thing

`PARAGRAPH_COUNT = 3`, `SELF_LOCATING`, `INSTRUCTION` and `IMPORT_DIAGNOSTICS` are all
hand-written literals, and the file says so at the point it matters. The one structural
coupling to check is `TEMPLATE_DIR`, which is built from `_harness.RS_ROOT = TEST_DIR.parents[2]`
while the scripts compute `HERE.parents[2]` from their own `__file__` — different anchors,
different depths, computed independently. Mutation 3 confirms this experimentally: breaking
the script-side depth reddens the test, which it could not do if the two derived from one
source.

### 3.7 The counted assertions in the body

`E3`/`HD-41` ③ make counts checkable, so I checked the one that is not a battery figure. The
body defers "the other ten repo-root resolution points across `cli.py` and the six templates".
Enumerated by hand: `parents[3]` fallbacks in the six templates = 6
(`check_template_instance.py:195`, `make_paragraph_map.py:37`, `run_bind_v2.py:170`,
`run_evidence_v2.py:121`, `run_repair.py:63`, `run_retire.py:98`); `cwd()` defaults in
`cli.py` = 6 (lines 43, 80, 147, 329, 414, 462). Twelve total, minus the two the sentence
names separately, **is ten**. The figure is right.

### 3.8 Stale-documentation sweep

Scope = all tracked `*.md`. Every surviving `ResearchSystem/tooling` string sits in a
historical journal, an archived ledger or a `history/` file — immutable records of what was
true then, not documentation of current behaviour. `assurance/templates/run-v2/README.md`
says nothing about how the scripts locate their library, so no documentation update was owed
by this change.

## 4. Findings

### `B-1` (blocker) — the round claims structural independence in the same sentence that rules it out

**Location.** `83e3191`, commit body, final sentence:

> "E1 disclosure: orchestrator and executor were one work-side session, and of R1's four
> holdings the review side has none of them here — … the executor held none of the four, so
> the read's independence is structural, and the same will hold for the FULL."

**The ground truth it violates.** `E1` decides independence on four holdings — dispatched by,
prompted by, scoped by, reported through — and states the disposition for the middle case:
"the round **states which of the four the executor held** … and **does not call the result
structurally independent**." `R1` supplies the premise for the other case: "**The orchestrator
holds the dispatch**, so with the executor holding none of the four the independence is
structural." When orchestrator and executor are one session — which this very sentence
discloses — there is no separate orchestrator for that premise to refer to, so "the executor
held none of the four" is not available.

This is not my reading imposed on the text. `HD-46` records the user's tiebreak on precisely
this ambiguity, and names precisely this shape:

> 全占＝失格 · 一项不占＝结构性独立 · 中间态＝独立但该轮在记录里写明 executor 占了哪几项，
> **且不得自称结构性独立**。…它直接作用于今天的实际形态——**一个 session 同时持 orchestrator
> 与 executor 两个角色**。

On the round's own facts the single work-side session held at least **dispatched by** (it ran
`dtw dispatch`; the marker is stamped ten seconds after its own candidate commit) and
**reported through** (it commits my record, per `R6` and `ORCHESTRATION.md`'s table), and the
prompt I received is the generator's `CONSTRUCTION_PROMPT` verbatim **plus two operational
sentences that session appended** — the repository root, and where to write without
committing. Scope was machine-resolved by `construction_dispatch_of`, but from a base and tip
that session chose. That is the middle state, not "none".

**Why this is a blocker and not a low.** `R9`'s wording-level test requires *both* that the fix
change no actor's action *and* that the accurate fact be recoverable nearby. The second prong
passes — the same sentence discloses the one-session shape. The first fails: `E1` imposes an
obligation not to call the result structurally independent, and that obligation is currently
breached rather than merely unstated. The distinction matters because the two immediately
preceding rounds got this right, one of them *because a FULL told it to*:

- `v3-review-full-57d1312.md` `L-4` — "no commit in the range carries `E1`'s disclosure of
  which of the four holdings the executor held";
- `15a53fe` (the fix that answered it) — "in this round the orchestrator and the executor are
  one work-side session. **All four of R1's holdings** — … Per `E1` this is stated rather than
  hidden, and **the round does not call its reviews structurally independent; the reviewers
  ran cold and re-derived everything, which is a discipline, not a structure**";
- `7f6e7f0` — "orchestrator and executor are one work-side session this round; the round's
  reads were dispatched, prompted, scoped and reported through it".

A missing disclosure is an omission a reader can notice. This one asserts the opposite of what
the rule permits, in the carrier `E1` designates, about a round whose predecessors had already
been corrected onto the right form. It also pre-declares my independence — "the same will hold
for the FULL" — before this review existed, which is the anchoring `R2` exists to refuse.

**Minimum fix.** An errata commit (`E8` names the kind) restating the disclosure in the shape
`15a53fe` used: name the holdings the single work-side session held, and state that the round
does not call its reviews structurally independent. No code changes. The candidate's bytes are
untouched by this.

### `L-1` (low) — the RED evidence is cited to a round journal that does not exist

`test_run_v2_template_library_path.py:25` states: "RED evidence (2026-08-21, **commands and
output pasted in the round journal**)". There is no round journal for `TEMPLATE-LIB-ROOT` —
`document-harness/journal/` holds no matching file, and no commit in the range creates one.
The citation resolves nowhere, in a permanent artifact rather than a commit body.

The claim it points at is true in substance: my mutations 1 and 2 establish that the pre-fix
bytes genuinely fail as a subprocess. What is missing is the carrier. `E3` allows either the
commit body or the round journal; the body **describes** the RED run rather than pasting it,
and the journal does not exist, so neither carrier holds it. Downstream decision that goes
wrong if unfixed: a later reader auditing why this guard exists follows the pointer, finds
nothing, and cannot tell whether the evidence was captured and lost or never captured.

Cheapest redemption is the closeout journal — write it and paste the commands, and the
citation becomes true without touching the test file.

### `L-2` (low) — "every invocation below passes the root explicitly" is false of five of seven

Same docstring, lines 30-32, explaining why the out-of-scope `run_dir.parents[3]` default is
never exercised: "every invocation below passes the root explicitly." Counted by hand, the
file makes seven invocations: four `--help` calls that pass no root, two that pass
`str(self.repo.root)`, and the probe that passes no arguments at all.

The **conclusion** is correct — the `parents[3]` default really is never reached, because the
four `--help` calls exit at argparse before root resolution and the probe is a standalone
file — but the stated reason is not the reason. This is the absolute-quantifier-without-its-
scope shape `HD-41` ② is a standing ruling about. Downstream decision: a later round trusting
this sentence would believe the default is covered by explicit roots and could drop the
`--help` pins while re-rooting.

### `O-1` (observation) — one substring assertion where a whole line was available

`test_the_authoring_gate_reaches_its_own_verdict` asserts
`any("TEMPLATE-PARAGRAPH-MAP-MISSING" in line for line in lines)` while its two neighbours
assert whole lines. `E5` says to assert the whole line. I checked whether one was available by
running the gate against a fixture: the line is fully deterministic, carrying no run-specific
path — but it does carry a non-ASCII em-dash, which is a plausible reason to avoid pinning it
byte-for-byte on a Windows console. The token is a unique diagnostic code that no unrelated
content emits, and the test also pins the exit code and one whole line, so the binding force
is real. Recorded because `E5`'s letter says whole line; **not** proposed as a fix — it would
burn the repair for no change in what the guard catches.

### `O-2` (observation) — the mutation evidence is described, not pasted

`E3` says to paste tool output and never describe it from memory. The body's mutation account
— "three mutations, three distinct reds, sha256 equality confirmed on every restore" — is a
characterization; no command and no output is pasted, and there is no journal to hold them
(same root cause as `L-1`). I re-ran all three plus a fourth and the characterization is
**true in every particular**, so this is a record-form observation and nothing more. Noted
because the round's ability to prove it later depends on the carrier `L-1` says is missing.

### `O-3` (observation) — the disclosed caller-repository write had nowhere to be routed

The body discloses that verifying the fix wrote `control/paragraph-map.json` into the caller's
real run directory, against a declared surface of "the caller repository at zero writes", and
that it was deleted immediately. Disclosing it satisfies `E9`'s "requires saying so, never
silently", and the round's own remedy — disposable fixtures thereafter, which is what the test
file does — is the right one.

What I record is the structural point, not a fault: `ORCHESTRATION.md` routes "a boundary it
would have to exceed" from executor to orchestrator to **user**, before the fact. With
orchestrator and executor being one session, that route had nowhere to go, and the breach was
disclosed after rather than approved before. Whether that route should have a form for
one-session rounds is the user's question under `R5`, not mine.

### `O-4` (observation, `R4`) — what this review could not verify

- **`E11`'s preview card and the user's approval**: chat-side, not in the repository.
  `UNVERIFIABLE`, ceiling stated per `R7`.
- **The caller-repository RED evidence**, and the claim that the stray file was deleted and the
  caller's `git status` returned to two pre-existing modifications: the caller repository is
  not reachable from here. `UNVERIFIABLE`. Note the fixture reproduces a *different* import
  failure (`ModuleNotFoundError: No module named 'rsclib'`) than the one reported against the
  caller (`ImportError: cannot import name 'load_json' … (unknown location)`); the guard
  catches both, but I could not reproduce the caller-specific shape.
- **That `3067efc` landed the read record unchanged**: I have no copy of what the reader
  returned. `UNVERIFIABLE`; the record is well-formed for its channel (`R6` path and title,
  no verdict, findings tiered must-fix / low / observation per `R3`).
- **That one session held both roles**: taken from the round's own disclosure, which is the
  statement `E1` asks it to make. `B-1` is an argument from that admission, not against it.

## 5. Coverage disclosure (`R4`)

**Read in full**: `document-harness/CONSTRUCTION-CHECKLIST.md`;
`document-harness/ORCHESTRATION.md`; `migration/document-work-assurance-v3/v3-harness-review-contract.md`;
the complete diff of both changed scripts; `test_run_v2_template_library_path.py` (all 172
lines); `tooling/tests/document_harness_review/_harness.py`; `HARNESS-DECISIONS.md` §live
(lines 1-136) and `HD-46` in full; both commit bodies in the range.

**Sampled**: `assurance/templates/run-v2/README.md` (opening 35 lines plus a targeted sweep);
the four sibling scripts (path blocks and root-resolution lines, not their whole bodies);
`check_template_instance.py`'s docstring and `main`; `tooling/rsclib/document_harness/dispatch.py`
(construction and read dispatch sections); `cli.py` (dispatch command, lines 145-230);
`compare_blocks.py` (header and imports); `document-harness/EXECUTION.md` (grep only);
`v3-review-full-57d1312.md` (headings plus the `L-4` line); `15a53fe` and `7f6e7f0` bodies
(independence sentences).

**Only probed**: `v3-cold-read-39e395e.md` — section headings and targeted greps, not read end
to end; `HARNESS-RIDERS.md` — opening rows only, its output exceeded what I pulled;
`document-harness/REVIEW.md` — not read (it governs product runs, not this round);
`HARNESS-DECISIONS.md` §implemented beyond `HD-46` — not read.

**Executed by me**: `python -m pytest -q` four times in full (once clean, three times mutated)
plus once scoped to the new file; four mutations with sha256-verified restores; the ambient
`rsclib` probe; a live fixture run of `check_template_instance.py` to inspect its output line;
`git status --porcelain` at open, after each restore, and at close — empty every time.

**Process claims are marked, not verified** (`R4`): that this review ran in fresh context is a
process claim I assert and cannot prove. Its structural independence is `UNVERIFIABLE` for the
reasons `B-1` sets out — which is the finding, not a caveat on it.
