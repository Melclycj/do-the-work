# Targeted VERIFY — `8aa9f6e..5873840` (round `RIDER-SETTLEMENT`, fix leg)

**Verdict: `REVIEWED_NO_BLOCKER`.** Every one of the seven accepted findings is delivered, and
the two that carried code were re-verified by re-running the mutations under them rather than by
reading the fix against the FULL record: all three wrong implementations of the retire kept count
now turn the suite red, the whole-message refusal assertion now dies on a reword that the old
substring assertion survived, and the two-file `init` cost was re-measured on a fresh scratch
caller to the byte. The repair diff contains nothing outside the approved boundary, the round's
core defect still binds after the repair, and the permanent boundaries are intact.

**Five residual findings, none blocking, in §5.** Two of them matter more than their tier
suggests, and they share a shape with the blockers they answer. `V-1`: the `B-1` fix narrowed the
kept-count coincidence from two id lists to one — `out_files = list(already_gone)` still leaves
all twelve tests green, because `RAW_IDS` was set to the same tuple `ALREADY_GONE_IDS` already
held. `V-2`: the `B-2` errata's replacement absolute — *every one of the 23 sits under one of
seven convention sentences* — is false for one of the 23 inside its own declared scope, and the
`ONBOARDING.md` convention it cites scopes itself, in its own words, to *the commands below*
while the site sits above it.

Everything below was re-derived from the repository (`R2`); no figure in any commit body, plan,
ledger or review record was accepted as given.

---

## 1. The subject, derived

```
$ cat .harness/review-pending.json
{
 "subject": "8aa9f6efd78fed1a0276e0c17aa73e1b10398788..5873840f54951e69699c667e226af83d65e5c00e",
 "dispatched_at": "2026-08-25T03:43:08+00:00"
}
$ git rev-parse HEAD
5873840f54951e69699c667e226af83d65e5c00e
$ git status --porcelain
(empty)
```

The worktree was clean at the start of this review, after every mutation restore, and at its end.
Every restore was from a sha256-checked scratch copy, never `git checkout --`.

**Window intact.** The tip commit is `2026-08-25 03:42:54` UTC against a dispatch of `03:43:08`
UTC; `git reflog` shows `5873840` as the newest commit on the branch, so the branch has taken
nothing since. The marker is untracked runtime state
(`git check-ignore -v .harness/review-pending.json` names `.gitignore:18:.harness/`), so no
committed file carries a written tip SHA (`E12`).

**Two commits, classified by hand; parentage linear, zero merges**
(`git rev-parse 9c6c950^ 5873840^` returns `8aa9f6e`, `9c6c950`; `git log --merges` over the range
is empty).

```
9c6c950  V3-REVIEW-RECORD-RIDER-SETTLEMENT-8aa9f6e-v1   review record (R6; lands alone)
5873840  V3-RIDER-SETTLEMENT-FIX-v1                     review fix (the one user-approved leg)
```

**Six paths, classified by hand** (`git diff --name-status 8aa9f6e..5873840`):

| path | class |
|---|---|
| `migration/document-work-assurance-v3/v3-review-full-8aa9f6e.md` | review record (added by `9c6c950`) |
| `CONSTRUCTION-LEDGER.md` | record — `O-3` |
| `assurance/templates/run-v2/README.md` | template doc — `L-3` |
| `document-harness/README.md` | **`E10` member** — `L-2` |
| `tooling/tests/document_harness/test_repo_root_discovery.py` | test — `O-1` |
| `tooling/tests/document_harness_review/test_run_v2_template_retire.py` | test — `B-1` |

`B-2` and `L-1` changed no file: both are answered in the fix commit's body, which is where the
FULL's minimum fix for each of them pointed.

## 2. Round, budget, authorization — derived

**Round.** `RIDER-SETTLEMENT`, plan `document-harness/plans/rider-settlement.plan.md`, status
open. The FULL over `2522ce1..8aa9f6e` returned `CHANGES_REQUIRED` and its record landed at
`9c6c950`; `5873840` is the fix leg it obliged.

**Budget (`E9`).** One FULL — spent at `9c6c950`. One user-approved fix — spent at `5873840`.
One targeted VERIFY — this record. Nothing else landed: the range is exactly the record plus the
fix, so `E12`'s rule that the branch takes no commit but the record between dispatch and landing
holds for the FULL leg as well (`8aa9f6e` to `9c6c950` directly, in the reflog).

**Authorization.** The fix boundary is stated in `5873840`'s own body: *"Boundary approved all-in
by the user on 2026-08-25: both blockers, all three lows, and observations O-1 and O-3."* That is
the carrier `E1` and `E9` name, and it is the only carrier — I cannot see the approval
independently, so per `R7` I state the ceiling and move on rather than treat it as a block. The
set it names matches the changed paths exactly: `O-2` and `O-4` are untouched, and nothing outside
the seven was changed.

**`E2`.** `git diff --name-only 8aa9f6e..5873840 -- contract/ schema/document-assurance-v3/`
returns nothing. Neither the frozen contract blob nor any pack file was written.

## 3. The accepted findings, each re-verified independently

### `B-1` — delivered, and the defect it named is narrowed but not closed

The fixture now reads `RAW_IDS = ("chk-c",)` with the expectation at `:207` changed to
`+ 1 raw output(s)`. I re-ran the executor's three rows against the shipped tree, restoring
`assurance/templates/run-v2/run_retire.py` from a sha256-checked copy (`8e6129d8...88978`) after
each and re-checking the digest:

```
shipped fixture + real template                       : 12 passed
shipped fixture + out_files = list(check_order)       : 1 failed
shipped fixture + out_files = list(to_delete)         : 1 failed
shipped fixture + .is_file() predicate deleted        : 1 failed
shipped fixture + out_files from glob("*.out.txt")    : 1 failed
```

Every failure is on the right test —
`SurvivorsAreLeftAlone::test_the_summary_reports_the_kept_counts` — and the other eleven stay
green each time, which is the negative control (`E4`). The `.is_file()` row is the rider's own
original shape and it is red now; the glob row is the alternative the template's comment warns
against, and the fixture's `chk-stray.out.txt` is what kills it. `chk-c` also restores the `HD-12`
case the rewritten docstring asserts: its per-result JSON is gone (`ALREADY_GONE_IDS`) while its
raw output survives.

**What still reproduces is `V-1` in §5.** A sixth derivation — `out_files = list(already_gone)` —
leaves all twelve green.

### `B-2` — delivered as a re-scoped errata; two residuals

The fix withdraws both original claims, restates the class as *a command written for a reader to
type — not a statement about a command that once ran*, declares the scope as every tracked `*.md`
with no exclusions, and enumerates 23 in-class sites plus the out-of-class hits. I re-ran the
first scan verbatim:

```
$ git grep -n -E "(^|[^3a-zA-Z_.-])python " -- '*.md' | grep -v python3 | cut -d: -f1 | sort | uniq -c
      7 README.md
      7 README.zh-CN.md
      4 assurance/templates/run-v2/README.md
      3 document-harness/ONBOARDING.md
      2 document-harness/EXECUTION.md
      1 HARNESS-DECISIONS.md
      1 document-harness/history/REVIEW-v1-package-flow.md
      (plus migration/, document-harness/journal/, document-harness/plans/, the two archives)
```

Every line number the errata lists is exact — `README.md:105,112,213,214,215,219,220`;
`README.zh-CN.md:101,108,199,200,201,205,206`; `ONBOARDING.md:20,72,89`;
`assurance/templates/run-v2/README.md:18,20,22,23`; `EXECUTION.md:365,514`. 7+7+3+4+2 = 23, and
the per-file counts above confirm the class is the whole of those five files' hits. The
out-of-class enumeration is complete at directory level: no file the scan touches falls outside
the five in-class files, `HARNESS-DECISIONS.md`, `document-harness/history/`, `migration/`,
`document-harness/journal/`, `document-harness/plans/` and the two archives. The Chinese mirror's
two convention sentences, which the withdrawn claim omitted entirely, are real and cover their
file's four hits (`README.zh-CN.md:96` covers `:101` and `:108`; `:192` covers `:199`, `:200`,
`:201`, `:205`, `:206`).

**Two residuals: `V-2` (one of the 23 is not under a convention sentence) and `V-3` (the second
scan's pasted command cannot be run, and neither scan pastes output).**

### `L-1` — delivered

`5873840`'s body carries the sentence the FULL asked for, naming `paths.py` as outside the plan's
declared change surface and giving the reason the extraction happened. I re-checked the invariant
rather than taking it: `env_without_repo_scope()` still returns `None` only when git cannot name
the variables (`caller.py:176-182`), and an empty-but-not-`None` environment is still distinct, so
`_submodule_files`' fail-open is unchanged. No file was reverted, which is what the FULL said the
fix should not be.

### `L-2` — delivered, and re-measured from scratch

`document-harness/README.md` now reads *"a later `init` finds nothing at the default paths and
silently recreates **both** instance files there as empty templates (exit 0, reported as
`2 created`)"*. I re-ran the walk on a fresh scratch caller — `git init`, `dtw init`, move both
files into a subdirectory, `dtw init` again:

```
first init                  : RESULT: 5 created, 0 left as found (exit 0)
second init, after the move : RESULT: 2 created, 2 left as found (exit 0)
$ wc -c HARNESS-DECISIONS.md HARNESS-RIDERS.md
3521 HARNESS-DECISIONS.md
 657 HARNESS-RIDERS.md
```

Both figures in the commit body are exact. The sharp consequence the sentence keeps is also
correct: the recreated `HARNESS-DECISIONS.md` carries the heading
`## §live — required reading` with nothing under it, so a cold read discharging `E10`'s `§live`
obligation reads an empty decision log. The word *empty* is now qualified as *empty templates*,
which removes the reading the FULL had to defend.

### `L-3` — delivered; one residual

`assurance/templates/run-v2/README.md:15-17` now names the two that take refs. Against the
sources (`grep -n add_argument` on each):

```
run_evidence_v2.py : run_dir, --repo-root, --base, --candidate, --candidate-branch
run_bind_v2.py     : run_dir, --repo-root, --evidence-commit, --bound-at, --emit
run_repair.py      : run_dir, --repo-root, --emit
run_retire.py      : run_dir, --repo-root
```

The false attribution the FULL named is gone: `run_repair.py` is no longer listed as taking round
refs. **Residual `V-4`:** the replacement says `run_repair.py` takes *only* the `--emit` mode flag
and `run_retire.py` *nothing beyond the run directory*; both take `--repo-root`, and the fix
commit's own body says so.

### `O-1` — delivered, and it buys something measurable

`test_repo_root_discovery.py:114-119` now asserts the whole message with `assertEqual` against a
hand-written literal, interpolating only the test's own fixture value (`E5`: the expectation is
independent of the module — no module constant is read). It matches `caller.py:178-182` exactly.
Two mutations of `caller.py`, restored from a sha256-checked copy (`e9a4385b...6cf3`) and the
digest re-checked after each:

```
reword the message, KEEP the "--local-env-vars" substring : 1 failed
replace the None-sentinel refusal with a dead branch      : 1 failed
```

The first row is the point: the old `assertIn` would have passed it. This is not a consistency
tidy — the assertion binds strictly more than it did.

### `O-3` — delivered

`CONSTRUCTION-LEDGER.md`'s `dispatch-economy` paragraph now carries ruling 3's routing and the
`R5` observation with the user's 2026-08-25 disposition. I re-derived the arithmetic from
`HARNESS-RIDERS.md` rather than reading it off: 16 rows; the six named for the checklist surface
(`wl-route`, `hd38-both-ways`, `e9-pair-budget`, `e10-cannot-see`, `read-name-split`,
`waiver-live`), the three for `ORCHESTRATION.md`'s table (`charter-qualifiers`, `e1-table`,
`e1-reader`) and the four machine questions (`pin-drift`, `delta-prose`, `argv-cap`,
`freeze-audit`) are all present and disjoint — 13 design rows, leaving `RA`, `PD` and `E10-sync`
as the three standing rows. 16 minus 9 is 7, which matches the deferred re-evaluation point the
paragraph names. Each of the nine names a round-eligible surface in its own `redeem when`, and
`dispatch-economy` is a construction batch, so `R10`'s bar for a design-shaped row is met.

## 4. The whole repair diff, and the fix commit's own claims

Reviewed line by line; nothing in it is outside the seven approved findings. The `E10` member edit
(`document-harness/README.md`) is one clause inside one table row — a targeted replacement, not a
re-type — and it neither adds a clause to any rule nor changes what any rule requires, so it is
not *design* under `E10`. It is also the same file the plan's opening ruling 1 already listed as
owing an independent read at the next round's opening, so the layer debt set is unchanged.
`layer_path_check.unresolved_tokens` over the added lines of that member returns the empty list,
and all nine members resolve at the tip.

The body's own figures, re-derived:

| claim | measured here |
|---|---|
| "Battery 854 green after" | `python -m pytest -q` at `5873840` gives `854 passed in 140.47s` |
| test count unchanged by the repair | `def test_` across `tooling/tests/`: 854 at `8aa9f6e`, 854 at `5873840` |
| `B-1`'s three-row mutation table | reproduced exactly (§3) |
| `L-2`'s two `init` runs and two byte counts | reproduced exactly (§3) |
| `L-3`'s "no refs at all" for `run_repair.py` | confirmed against `run_repair.py:56,58,60` |

**The round's core defect still binds after the repair.** Dropping `env=env` from the toplevel
query in `discover_repo_root` turns `test_the_environment_cannot_redirect_the_answer` red, the
other ten passing — so the repair did not weaken the thing the round existed to fix.

## 5. Residual findings — none blocking

### `V-1` — the `B-1` class is narrowed, not closed: `out_files = list(already_gone)` is still green

**Location.** `tooling/tests/document_harness_review/test_run_v2_template_retire.py:90-91`
(`RAW_IDS = ("chk-c",)` immediately above `ALREADY_GONE_IDS = ("chk-c",)`), read by `:207`.

**Measured.** Same protocol as §3, same digest restore:

```
shipped fixture + out_files = list(already_gone)  : 12 passed
```

**Why it is the same defect.** Three id lists are in scope where the kept count is built
(`run_retire.py:148-155`): `check_order` (3), `to_delete` (2), `already_gone` (1). The fix's own
docstring enumerates the first two — *"must equal neither `len(check_order)` (3) nor the size of
the deletion set (2)"* — and is silent on the third, which is now the same tuple as `RAW_IDS`. The
fixture docstring's standing absolute at `:116-117`, *"the kept count can only be right if the
template asks the filesystem"*, is falsified by the row above: that derivation never touches
`<check_id>.out.txt` at all and the printed count is still 1. Semantically `already_gone` is the
most on-point wrong answer of the three, because confusing per-result JSON with raw output is
exactly the `HD-12` independence the fixture exists to instantiate.

**Why it is a residual and not a blocker.** The verdict vocabulary for a VERIFY admits no
`CHANGES_REQUIRED` (`R3`), and the guard is strictly stronger than it was: three derivations that
were green are now red, and this is the one left. But the rider row is deleted, so nothing else
points at the class.

**Fix direction (the executor's to choose, `E12`).** With `check_order` at 3, `present` at 2 and
`already_gone` at 1, every non-zero raw count collides with one of the three, so no choice of
`RAW_IDS` alone escapes — the fixture needs a fourth ordered check. One shape that clears all
three: `CHECK_ORDER = ("chk-a","chk-b","chk-c","chk-d")`, `PRESENT_IDS` the first three,
`ALREADY_GONE_IDS = ("chk-d",)`, `RAW_IDS = ("chk-a","chk-d")` — count 2 against 4 / 3 / 1, with
`chk-d` still carrying the `HD-12` case. I did not measure that shape; I measured only that the
current one leaves a green wrong implementation.

### `V-2` — one of the errata's 23 sits above its file's only convention sentence

**Location.** `document-harness/ONBOARDING.md:20` — the `python -m pip install "jsonschema>=4.18"
referencing` command, in the *Install the instrument's runtime dependencies first* paragraph.

**Ground truth.** `HD-41` ②: an absolute quantifier carries its scope. The errata's claim is *"The
class has 23 instances and every one of them now sits under one of seven convention sentences ...
ONBOARDING.md:20,72,89 under :27."*

**Measured.** `grep -n python3 document-harness/ONBOARDING.md` returns lines 27, 28 and 29 only —
the file has exactly one convention sentence, at `:27`, and its own words are *"`python` in the
commands below means..."*. Line 20 is nine lines above it. `:72` and `:89` are below it and are
covered; `:20` is not, by the sentence's own scoping.

**Why it is nameable rather than cosmetic.** The site is the first command in the file and the
paragraph's whole point is that it must be run *first*, for the interpreter the hook will use; a
reader on stock Ubuntu types it before reaching `:27`. And a later round redeeming a sibling of
`py-convention` reads this errata as *class closed* and skips it — which is the downstream
decision `B-2` was raised on.

**Minimum fix.** Move the convention sentence above the dependency paragraph, or drop *below* from
its scope, or give `:20` the interpreter note inline.

### `V-3` — the second scan is pasted in a form that cannot be run, and neither scan pastes output

**Location.** `5873840`'s body, the two indented command lines.

**Ground truth.** `HD-41` ④ and `E3`: paste the grep output into the commit body, because the scan
is an action rather than a good intention and the evidence is what lets a reviewer see on the spot
whether it ran. This is the clause `B-2` was raised under, and it is the half of `B-2`'s minimum
fix — *"paste both greps' actual output"* — that was not taken.

**What is there instead.** Scan 1 pastes a runnable command and then an enumeration of the 23
in-class sites; that enumeration is verifiable and I verified it, but it is a filtered conclusion
rather than the roughly 450-line output, so the filtering step is not itself visible. Scan 2
pastes `git grep -n -E "(^|[^a-zA-Z])(One|Two|...|[0-9]+) (commands|operations)" -- '*.md'` — the
literal `...` is an elision, so the command as written does not run, and no output follows it.

**And the claim it supports does not survive a runnable expansion.** Two things. First, the pasted
regex is ASCII-only and case-sensitive, so it cannot return `README.zh-CN.md:92` and `:229` — the
two Chinese sites the body reports — and it does not return `README.md:245` either, whose *five*
is lowercase; those were found some other way, and the pasted command does not evidence them.
Second, inside the scope the paragraph declares (every tracked `*.md`, no exclusions), a runnable
expansion returns three further non-record hard-coded command counts:

```
$ git grep -n -iE "(^|[^a-z])(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|[0-9]+) (commands|operations|subcommands)" -- '*.md'
  (records and archives filtered out)
README.md:95                        Five commands stand between a repository that has never seen ...
README.md:245                       Today the five commands in the
document-harness/EXECUTION.md:362   these six commands and nothing fewer -- owed by ...
document-harness/EXECUTION.md:372   five commands owed by the caller and not ...
document-harness/EXECUTION.md:376   ... and `rsc.py compile --check`. Five commands,
```

The three `EXECUTION.md` sites are benign for exactly the reason the body gives for leaving the
four alone — each enumerates its commands in place, so the count is checkable where it stands —
but *four* is the wrong number for the class as `B-2` framed it, and the pasted command cannot be
run to settle which framing is meant.

**Minimum fix.** Paste the actual output of a runnable command for scan 2, or state the class
narrowly enough (*the Quickstart step-count sentence family*) that the count it carries is the
count of that family.

### `V-4` — the `L-3` replacement says *only* and *nothing beyond*, and both are short by `--repo-root`

**Location.** `assurance/templates/run-v2/README.md:16-17`.

The sentence now reads *"`run_repair.py` takes only the `--emit` mode flag and `run_retire.py`
nothing beyond the run directory"*. Both scripts also take `--repo-root` (`run_repair.py:58`,
`run_retire.py:95`), and `5873840`'s own body names it: *"it takes run_dir, --repo-root and the
--emit mode flag"*. This is the class `L-3` named — a vague sentence made specific and slightly
false — reappearing at the site of its own fix, though far smaller: the paragraph elides
`--repo-root` uniformly for all six scripts and the invocation list below does the same, so a
reader is not misled about any one of them in particular. Minimum fix: drop *only* and *nothing
beyond the run directory*, or say once that `--repo-root` is common to all six.

### `V-5` — two convention-sentence line citations point above the sentence they name

`5873840`'s body cites *"the sentence this round added at :10"* for
`assurance/templates/run-v2/README.md` — the sentence begins on `:11`, and `:10` is the line above
it — and *"the one added at :365"* for `document-harness/EXECUTION.md`, where the sentence begins
on `:368` and `:365` is the class instance it covers. Both sentences exist and both cover the
sites claimed; `EXECUTION.md`'s says *"`python` in this file means ..."*, which is file-scoped and
so reaches `:514` as well. Wording-level under `R9`: no actor's action changes, and the accurate
line is one hop from the cited one.

## 6. Boundary check (run second, per `R3`)

| boundary | state |
|---|---|
| `E2` | Clean. No path under `contract/` or `schema/document-assurance-v3/` in the range. |
| `E8` | Six explicit paths, all accounted for; new commits, no amend (the reflog shows two plain `commit:` entries); no push — `origin/main..HEAD` is five commits, so nothing left the machine. Title `V3-RIDER-SETTLEMENT-FIX-v1` names the round in the established `-FIX-` form, and both bodies name their kind. |
| `E9` | Three legs, three commits, no fourth. The fix names its approved boundary and does not exceed it. |
| `E10` | One member edited (`document-harness/README.md`), not design, already on the plan's disclosed read debt; `layer_path_check` clean on its added lines; all nine members resolve. |
| `E12` | No range recorded in a commit; the marker is untracked. Between the FULL's dispatch and its record the branch took no other commit. |
| `R6` | The FULL record landed alone at `9c6c950`, title `V3-REVIEW-RECORD-RIDER-SETTLEMENT-8aa9f6e-v1`. |
| `R10` | `HARNESS-RIDERS.md` is untouched by the fix leg, which is right: every approved finding was fixed, and `O-4` was routed to the ledger rather than the bank by the ruling recorded there. |
| chat-only load-bearing material (`R2`) | None found. The fix boundary, the three opening rulings, ruling 3's routing and `O-4`'s disposition all have committed carriers. |

## 7. Coverage and honesty ceilings (`R4`)

**Read in full.** `document-harness/CONSTRUCTION-CHECKLIST.md`;
`migration/document-work-assurance-v3/v3-harness-review-contract.md`; `HARNESS-DECISIONS.md`
`§live` (all six entries) plus the `§implemented` titles;
`migration/document-work-assurance-v3/v3-review-full-8aa9f6e.md`;
`document-harness/plans/rider-settlement.plan.md`; both commit bodies in the range; the entire
repair diff, all five files; `HARNESS-RIDERS.md` (all sixteen rows);
`tooling/tests/document_harness_review/test_run_v2_template_retire.py:70-135` and `:200-212`;
`assurance/templates/run-v2/run_retire.py:110-168`;
`tooling/rsclib/document_harness/caller.py:150-196`; `assurance/templates/run-v2/README.md:1-32`;
`document-harness/ONBOARDING.md:14-45` plus its item-1 and item-2 blocks;
`tooling/hooks/layer_path_check.py:1-60`.

**Sampled.** `README.md` — the two convention paragraphs, the commands table, Install.
`README.zh-CN.md` — the same four regions. `document-harness/EXECUTION.md:355-382` and `:505-518`.
`CONSTRUCTION-LEDGER.md` — the changed line reconstructed against its predecessor plus the two
neighbouring queue paragraphs; not the CLOSED roll.

**Not read.** `document-harness/REVIEW.md`, `document-harness/ORCHESTRATION.md`,
`contract/Document-Work-Assurance-Contract-v4.md`, and every prior review record except
`v3-review-full-8aa9f6e.md` and the header of `v3-review-verify-3149581.md`. This is a targeted
VERIFY of one fix leg, not a re-certification of the layer (`R4`).

**Probed by execution.** `python -m pytest -q` at `5873840` gives `854 passed in 140.47s`. Eight
mutations: five of `run_retire.py`'s kept-count derivation and three of `caller.py` (message
reword, refusal branch, `env=` dropped), each restored from a sha256-checked scratch copy with the
digest re-checked. `dtw init` twice on a fresh scratch caller with the instance files moved between
runs. Both `HD-41` class scans re-run, the second in a runnable expansion of the elided form.
`layer_path_check.unresolved_tokens` over the member edit's added lines, and an existence check on
all nine members.

**Not verifiable from the repository, and not folded into supported.** Whether the user's fix
approval was given as the commit body states; whether `E11`'s preview card was rendered; whether
the executor session was cold; whether this fix leg was written in a session separate from the one
that produced the candidate. All are process claims, marked (`R4`). `E1`'s disclosure for the
candidate — all four holdings in the executor's hands, the exception channel taken — was made in
`fd525e4` and stands for the round; the fix leg's body does not restate it, which `E1` does not
require of a second commit in the same round.

**Mutation caveat (`R4`).** The eight mutations prove these tests have binding force against the
shapes I chose. `V-1` is the demonstration that binding force is not sufficiency: the same suite
was green against a shape nobody had chosen yet.
