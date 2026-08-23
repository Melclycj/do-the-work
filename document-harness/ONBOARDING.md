# ONBOARDING — taking a repository that has never seen this harness to one that can run a round

Nine items. They are the ones `HD-33` / `HD-34` and `io-design.md` §5–§7 imply, written out in
the order they are actually done, each with **the command or edit**, **how the caller sees that
it took**, and **which rule or decision owns it**. Ownership is by pointer: this file never
re-types a rule, because a second copy is a second thing that has to stay true (`HD-5`
records transcription as a drift surface).

**This file is not an instruction-layer member.** It has authority over nothing: every "must"
below belongs to the rule named in its Owner column, and where this file and that rule disagree
the rule governs. `E10`'s membership sentence names the members, and it does not name this one.
The round that created this file recorded that question and its answer —
`journal/caller-onboarding-2026-08-19.md`.

**Read once before starting:** `README.md` beside this file (the instrument's navigation
surface) and `../HARNESS-DECISIONS.md`'s `§live`. Onboarding is not a round and spends no
review budget; what it produces is a repository in which a round can be opened.

**Install the instrument's runtime dependencies first, for the interpreter the hook will
use.** `python -m pip install "jsonschema>=4.18" referencing` — every `dtw` command and both
caller-side guards import `jsonschema` through `rsclib.document_harness`, so without it item
1's own `--help` check exits 1 on `ModuleNotFoundError` and item 9 ends with a hook that
fails every commit. Measured 2026-08-24 on the second caller's walk, which is where this step
was found missing. The instrument's own hook never revealed it: that hook runs
`layer_path_check.py` alone, which is the one guard with no third-party import.

One command convention: `python` in the commands below means whichever of `python3` /
`python` this machine actually runs — stock Ubuntu ships only `python3` (measured
2026-08-23), Windows typically `python`. `.githooks/pre-commit` probes `python3` first and
`python` second, so **on a machine that has both the two do not resolve alike** — measured
2026-08-24, where the probe took a Python 3.12 with no site-packages while a reader typing
`python` got a 3.13 that had them, and nothing said so until a guard tried to import. Install
into whichever the probe picks, or make the caller's own hook name one interpreter and record
that choice in the caller's decision log.

## What a clone carries, and what it does not

The two are not the same thing, and the caller that grew this harness got the line wrong twice
in the same place — both times on hooks.

| carried by a clone / checkout | **not** carried — per-machine, done once per checkout |
|---|---|
| the gitlink: which revision of the instrument this caller pins | the instrument's **contents** — a plain `git clone` leaves the submodule directory empty until `git submodule update --init` |
| the caller's hook **script**, if it is tracked (a file in the tree) | `git config core.hooksPath` — the pointer that makes git run that script. Config is not tracked |
| the caller's `.gitignore` entry for `.harness/` | `.harness/` itself and everything in it: the freeze marker, the run log. Ignored on purpose, per checkout |
| the four instance files, once committed | nothing about them is per-machine — but see item 5: the journal is not created until the first round writes one |

Measured on 2026-08-19 by cloning the onboarded throwaway caller: the clone carried
`.githooks/pre-commit`, all four instance files, the policy file, the pointer line and the
`.gitignore` entry; `git config --get core.hooksPath` exited 1 (unset), `.harness/` was absent,
and the submodule directory was empty. Setting `core.hooksPath` in that clone *without*
initialising the submodule then made the very next commit fail loudly — which is item 9's
`-f`-versus-loud choice, seen rather than argued.

The two incidents this table is paid for, both recorded in the caller's
`ResearchSystem/HARNESS-POLICY.md` §3: (1) the caller's hook was **untracked**, living in
`.git/hooks/`, so a check script deleted from the tree on 2026-07-28 kept being called from it
for weeks with nobody able to see the call; tracking the hook (2026-08-16) put it inside review
subjects. (2) `core.hooksPath` is written in one `.git/config` that **all worktrees of a
repository share**, so pointing it at a tracked `.githooks/` on one branch left every other
branch and worktree of that repository committing with no hook at all until the directory
reached their base. Neither is a defect in the harness; both are what "config is not tracked"
does when it is assumed away.

## The nine items

### 1 — Mount the instrument as a submodule, and pin a revision

| | |
|---|---|
| **Do** | `git submodule add <instrument-url> <mount-path>` in the caller's repository root, then commit the gitlink and `.gitmodules`. On the caller that grew this harness the mount path is `ResearchSystem/harness`; any path works — nothing in the instrument reads its own mount point, and the 2026-08-19 execution mounted it at `vendor/dtw` to test exactly that (`init` finds its templates from `__file__`, and the guards resolve the repository root from the cwd git gives a hook). |
| **See** | `git submodule status` prints one line: the pinned SHA and the mount path. `ls <mount-path>/tooling/dtw.py` finds the CLI, and `python <mount-path>/tooling/dtw.py --help` lists the eight operations. After a later `git clone` of the caller, that directory is **empty** until `git submodule update --init`, which is the clone-carries line above. |
| **Owner** | `HD-33` (the calling model is a submodule; the gitlink is what makes "which version of the instrument checked this round" answerable) and `io-design.md` §7. `HD-34` adds the caller's side of the discipline: a caller never edits or upgrades the instrument in place, and any adaptation is recorded in the caller's own decision log — item 3. A copy instead of a submodule is the escape hatch `HD-34` names, at the price it names. |

An upgrade is a gitlink change: `cd <mount-path> && git fetch && git checkout <rev>`, then commit
the pointer in the caller. That commit is the whole record of the upgrade, which is the point.

Two things the 2026-08-19 execution ran into here, both environmental and both real:
`git clone` and `git submodule add` refused this tree with `Filename too long` under a deep
path on Windows until `-c core.longpaths=true` was passed (three N0 fixture paths are the ones
that trip it); and a submodule whose source is a local directory rather than a URL additionally
needs `-c protocol.file.allow=always`, which git has refused by default since 2022 — that one is
an artefact of testing without a network, not a step a caller with a real remote performs.

### 2 — `.harness/`, and its ignore entry

| | |
|---|---|
| **Do** | `python <mount-path>/tooling/dtw.py init --repo-root .` from the caller's root — it creates `.harness/` with the default scan-surface declaration `scan-surfaces.json` inside it (the file both caller-side guards read — the second note under item 9 says what it declares), appends `.harness/` to `.gitignore` (creating that file if absent), and does items 3 and 4. By hand it is `mkdir .harness` plus one line in `.gitignore`; the declaration is only needed once the caller's layout leaves the defaults. |
| **See** | `git check-ignore -v .harness/x` names the `.gitignore` line that ignores it. `dtw init` prints every path it created and every one it left alone. |
| **Owner** | `io-design.md` §7: the run directory and the freeze marker `.harness/review-pending.json` belong to the caller and may be gitignored; `HD-33` rules the same. The marker is written by `dtw dispatch` and is `E9`'s review window — not `E2`'s byte freeze, which is a different thing with a similar name. Which of these nine items `init` may absorb at all is bounded by the criterion in the onboarding row of `README.md` beside this file: the tree half may enter `init`, the machine half never does. |

### 3 — The decision log

| | |
|---|---|
| **Do** | `dtw init` copies `templates/decision-log.md` verbatim to `HARNESS-DECISIONS.md` at the caller's root. Move it if the caller wants it elsewhere; record that in the file itself, since it is the log of exactly such decisions. **A move costs something, and the cost is silent:** `init` takes no placement option (`HD-47` ruled `--into` not worth adding), so it only ever looks at the root, and a later run writes a *fresh empty log* there beside the moved one — measured 2026-08-24 on the second caller's walk, exit 0, reported as `created`. Two logs then exist and the empty one is the one at the path every convention names, so a cold read discharging `E10`'s `§live` obligation reads no rulings at all. If the log is moved, either do not re-run `init`, or delete what it recreates; the caller's policy file is where to say which. |
| **See** | The file exists and has no entries, and its header carries `io-design.md` §6's five — the state machine, the four scopes, the three admission questions, **inheritance** (the block beginning *"Who reads it"*, which carries the `§live` required-reading rule and the verbatim-inheritance rule), and the deletion discipline — plus narrowing (`HD-30`), which the template ships as an extra. `dtw init` refuses to overwrite an existing one and names it in its report — a second run cannot clobber rulings. |
| **Owner** | `io-design.md` §6 (this file ships as an empty instance, header included). The rules of the log live **in that header**, not in the instruction layer: `HD-19` ruled the decision log is not an instruction-layer member, while `E10`'s tail makes its `§live` required reading at every round's opening. The harness's own instance, `../HARNESS-DECISIONS.md`, is a filled example of the same shape. |

### 4 — The rider bank

| | |
|---|---|
| **Do** | `dtw init` copies `templates/rider-bank.md` verbatim to `HARNESS-RIDERS.md` at the caller's root. Moving it carries item 3's cost unchanged — measured on the same walk, both files recreated at the root by one `init` run — and the same two answers apply. |
| **See** | The file exists, carries the four-column table header and no rows, and points at the rule rather than restating it. |
| **Owner** | `io-design.md` §6 for the empty instance; `R10` in `CONSTRUCTION-CHECKLIST.md` for the rules — what banks here rather than becoming a `HarnessIssue` or a round, the row format, and what redemption is. Note which bank: `R10`'s last clause reserves the construction side's bank for construction findings, so a caller's product-run observations belong in the caller's own bank, which is this file. |

### 5 — The journal (deliberately not pre-created)

| | |
|---|---|
| **Do** | Nothing, now. Create `journal/<round>-<date>.md` when the first round has something to record. There is no template and `dtw init` does not make the directory. |
| **See** | Nothing to see, which is the point: an empty journal directory would assert that a journal is owed before any round exists. |
| **Owner** | `io-design.md` §6 states the non-creation; the journal row of `README.md` beside this file states what a journal is for and its one-file-per-round shape (`HD-1`, narrowed 2026-08-08; SIMP-D1 added the cross-round design-judgment kind). Why not pre-create: a journal holds a round's analysis, reasoning and measurement, so a file with none of those is a file that will be filled to justify its existence. |

### 6 — The ledger (deliberately without a template)

| | |
|---|---|
| **Do** | Write one, in whatever form the caller already keeps durable state — and declare its parameters (where it lives, what may go in it, any size cap and what enforces it) in the policy file of item 7. The harness ships no template for this one. |
| **See** | The policy file names the ledger and its rules; the ledger exists and holds the current pointer. |
| **Owner** | `io-design.md` §6: "the harness provides no template", because a ledger is where the caller records what it did with a round's conclusions and that is the caller's business, not the instrument's. `io-design.md` §5 is the reason it is the policy file that declares its parameters. The caller that grew this harness keeps two ledgers and states both, with a line cap and the script that enforces it, in its `ResearchSystem/HARNESS-POLICY.md` §2 — one worked example, not a requirement. |

### 7 — The caller's policy file

| | |
|---|---|
| **Do** | Write a file that says what this machine does with a round's conclusions: where the conclusions come from (command output), which ledgers get written, where rulings and unresolved findings go at closeout, and which mechanical checks the caller runs. Any path, any name. |
| **See** | The orchestrator reads it at closeout and can act on it without asking. It is prose for a session, never a script: **harness code never executes it**, and if it did, the boundary between an instrument and its caller would be gone. |
| **Owner** | `ORCHESTRATION.md`, *Reading the caller's policy file* — three properties, none optional: it belongs to the caller, it has no authority over any rule in the instruction layer, and a caller that has not written one is not defective (the absence is stated at closeout, not filled by inventing policy). `io-design.md` §5 is where the carrier decision was taken (a standalone file, ruled 2026-08-12, replacing an earlier "a section inside `CLAUDE.md`"). |

### 8 — The one-line pointer to it, in the caller's agent-facing entry file

| | |
|---|---|
| **Do** | Add one line to the file an agent reads first in that repository — `CLAUDE.md`, `AGENTS.md`, or whatever plays that role — naming the policy file and what it is for. If the repository keeps mirrored entry files, both change in the same edit. |
| **See** | Grep the entry file for the policy file's name and find it. The real test is colder: a session that starts in this repository knowing nothing about the harness reaches the policy file by reading only the entry file. |
| **Owner** | `io-design.md` §5 (the pointer is what makes the policy file discoverable) and `ORCHESTRATION.md`, same section — the caller's entry file points at it, and a cold orchestrator has no other stated discovery path. Nothing enforces this line; it is the one item whose failure is silent, because a missing pointer looks exactly like a caller that never onboarded. |

### 9 — Hook wiring

| | |
|---|---|
| **Do** | Two halves. **Tracked half:** put the hook script in the tree (`.githooks/pre-commit` is the convention both repositories use) and call the guards the caller wants from `<mount-path>/tooling/hooks/`. Commit it **executable** — git records the mode and runs a hook only if it has one, while Windows with `core.fileMode=false` hides the difference until a POSIX clone skips it — with a hint (`hint: The '.githooks/pre-commit' hook was ignored because it's not set as executable.`, measured on git 2.43.0; `advice.ignoredHook` can suppress it, so the reliable signal is the commit landing unchecked, not the message): `git update-index --chmod=+x .githooks/pre-commit`, checked with `git ls-files -s`, which must print `100755`. This file's own round shipped `100644` by following this row while that sentence was missing from it, which is why it is here. **Per-machine half:** `git config core.hooksPath .githooks`, once per checkout, by every person and every worktree. |
| **See** | `git config --get core.hooksPath` prints the directory. Then prove it fires rather than asserting it: stage a work product naming a path that exists nowhere, attempt a commit, read the exit code, and restore the file from a checksummed copy. A hook that has never been seen to block is a hook nobody has tested (`E4`). |
| **Owner** | `README.md`'s *Local enforcement* row states what each guard does and that all of it is advisory and bypassable with `--no-verify` — automation, never a harness guarantee. Which guards a caller runs is the caller's choice: `candidate_path_check.py` (a path newly written into a work product resolves nowhere) and `review_freeze_check.py` (`E9`'s window: while `.harness/review-pending.json` exists, only record-family paths may land) are the two the caller that grew this harness runs from the submodule. `layer_path_check.py` is the instrument's own and runs **here**, in the repository whose nine members it names — the hook is `.githooks/pre-commit` at this repository's root, and a caller does not wire it. |

Two things worth knowing before wiring, both measured rather than argued:

- **An existence-guarded call can fail silently.** The caller's hook guards each call with
  `-f` and skips a missing script with no output at all — which is how a deleted check kept
  being "run" for weeks, and what rider `mount-inert` banks about a mount path that stops
  resolving. This repository's own hook keeps the guard and makes the missing case **loud**
  instead, at a price paid in the 2026-08-19 run: a fresh clone with `core.hooksPath` set but
  the submodule not yet initialised cannot commit at all until it runs
  `git submodule update --init`. Pick one deliberately; the failure modes are opposite.
- **Both guards read their surfaces from the caller's `.harness/scan-surfaces.json`**
  (round STRANGER-GUARDS; item 2's `init` writes the defaults). `candidate_path_check.py`
  exempts the declared record and specification surfaces from the work-product scan, and
  `review_freeze_check.py` admits returned records only in the declared directories — so a
  caller whose records live off the defaults edits that declaration, a file in its own
  tree, which is exactly the adaptation `HD-34` tells it to record rather than the
  in-place instrument edit `HD-34` forbids. Until then its records are scanned as work
  products, and a record quoting the broken path it reports is blocked from landing — the
  deadlock the declaration exists to end. A declaration with a typo blocks loudly and
  never silently falls back to the defaults; the guards' refusal names the file.

## When the nine are done

The caller can open a round: the orchestrator reads the instruction layer and `§live`, the
executor works, `dtw dispatch` writes the freeze marker and prints the dispatch, the reviewer
returns a record, and the policy file says what happens to the conclusions. Nothing in this
file certifies that state; there is no `onboarded` flag and deliberately no command that emits
one — what a caller has is nine checkable facts, each verified by the *See* row above.

## Execution record

Written first, then executed end to end on 2026-08-19 against a throwaway caller repository
outside both repositories, then corrected to match what happened — the notes above about long
paths, local-directory submodule sources, the `vendor/dtw` mount and what a clone carried are
all from that run, not from intention. All nine items were reached; items 2–4 by `dtw init`,
5 by doing nothing, 6–9 by hand. Both caller-side guards were seen to block and then seen to
pass on a clean control, and `init` was re-run against a decision log with content in it to
confirm it kept what was there.

Three ceilings, stated because a step silently skipped is not an answer: the instrument's real
remote is private and this run had no network, so the submodule source was a local clone
carrying this round's uncommitted work — the run exercised these bytes, not a published
revision; the procedure was executed by its own author on the machine that grew the harness, so
it is not evidence that a stranger can follow it; and nine items were confirmed executable and
sufficient *for this run*, which is not evidence that a tenth is not missing. A real second caller was what
would close the last two; the section below is that run, and closes one of them. The run, its command outputs, and the membership
question this round was obliged to record are in `journal/caller-onboarding-2026-08-19.md`.

## Second execution — 2026-08-24, a second caller on a different layout

Walked again, end to end, against a fresh repository outside both trees, on a layout chosen to
share nothing with the first: the mount three directories deep at `lib/vendor/assurance-harness`
rather than two, the entry file `AGENTS.md` rather than `CLAUDE.md`, the policy file, ledger,
decision log and returned records all under `docs/policy/` rather than at the root, and the
scan-surface declaration edited away from the shipped defaults because of it. The full record —
every command, its pasted output, and whether each item's own *See* check held — is
`journal/stranger-proof-walk-2026-08-24.md`.

**What that run changed in this file.** Three of the nine items were wrong or short as written,
and all three are fixed above: the runtime dependencies were never installed by any item (item
1's own `--help` check exits 1 without them, and item 9 ends with a hook that fails every
commit); the interpreter convention claimed the hook's probe and a reader typing `python`
resolve alike, which is false on a machine that has both; and item 3's offer to move the
decision log did not say that a later `init` silently recreates an empty one at the root, where
a cold read then finds no rulings.

**What it closes, and what it does not.** The first ceiling above is closed: the submodule source
was the published remote at revision `1a0a200`, not a local clone of uncommitted work. The third
is answered rather than closed — a tenth item *was* missing, it is now written, and that is still
not proof an eleventh is not. The second stands: same machine, and the walker was an agent
following the file, not a human stranger meeting it cold. Windows long paths remain a caveat and
were measured rather than assumed — the longest path under the mount came to 182 characters
against the 260 limit, so a caller whose repository root reaches 130 characters still needs
`-c core.longpaths=true`. Nothing here was executed on POSIX; the CI matrix covers the test
suite there, not this procedure.
