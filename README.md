# do-the-work

![CI](https://github.com/Melclycj/do-the-work/actions/workflows/ci.yml/badge.svg)

**An instrument that makes a piece of document work reviewable.** Not a linter and not a writing
assistant: a harness that freezes the instruction before the work starts, keeps the person doing
the work from also certifying it, runs machine checks whose output nobody edits, and ends in a
verdict from a reviewer who was handed one commit and nothing else.

The thing it is built against is simple and hard to avoid otherwise: whoever produced a piece of
work is the worst possible judge of whether it is done, and every informal process eventually lets
them be the judge anyway — by summarising their own evidence, by choosing which checks count, or
by being the only one who read the requirement. This harness takes those three moves away.

## Who it is for

A repository with **document work that has to survive someone checking it** — a thesis chapter, a
specification, a regulatory submission, a report a client will audit. It is useful when three
things are true: the work is text, "done" is contestable, and there is a reason to be able to
prove later what was asked, what was delivered, and who signed it off.

It is **v3 of the Document Work Assurance harness**, extracted from the repository that grew
it. `HD-10` ruled the extraction necessary on the ground that the harness does not depend on
that repository to exist; a caller pins a version of this repo and runs it against its own
work.

It is **not** for source code review (that is what a code reviewer is for), and it is not a
project-management tool. It has no server, no account, no telemetry, and nothing to log into: it
is a Python CLI, a set of git hooks, and a body of instruction text that a repository mounts as a
submodule and pins to a revision.

## What using it looks like

Three roles, and the discipline is that **they are three different sessions**, never one wearing
three hats:

| role | does | may never do |
|---|---|---|
| **orchestrator** | starts the work, dispatches the review, keeps the budget, carries questions to the human | review its own round's work, or answer a question the rules send to the human |
| **executor** | writes the candidate and one honest claim per obligation | write any check result, any verdict, or the decision |
| **reviewer** | starts cold from one commit SHA, derives everything else from the repository, writes the record | be handed a summary — a fact you were handed is a fact you did not check |

A round runs: the instruction is frozen → the executor produces a candidate → machine checks run
and their raw output is kept → the orchestrator dispatches one commit range to a cold reviewer →
the reviewer returns `REVIEWED_NO_BLOCKER`, `CHANGES_REQUIRED` or `SPEC_GAP` → the finding is
fixed once, verified once, and the round closes. The budget is deliberately small — one full
review, at most one approved fix, one targeted re-check — because an unbounded review loop is how
a process stops being a gate.

The harness runs this on itself. Every rule in it was paid for by something that went wrong,
which is why the instruction text keeps citing incidents rather than principles.

## Quickstart — mounting it in a repository that has never seen it

Every command below was run end to end against a fresh repository on 2026-08-24; the full record,
with each command's output, is
[`document-harness/journal/stranger-proof-walk-2026-08-24.md`](document-harness/journal/stranger-proof-walk-2026-08-24.md).
`python` means whichever of `python3` / `python` your machine runs — and if it has both, see the
note in the onboarding file, because they can resolve differently.

```sh
# 0. the runtime dependencies, for the interpreter your git hooks will pick
python -m pip install "jsonschema>=4.18" referencing

# 1. mount the instrument and pin a revision
git submodule add https://github.com/Melclycj/do-the-work.git <mount-path>
git submodule status          # prints the pinned SHA and the mount path

# 2. the mechanical half of onboarding: .harness/, its ignore entry, two instance files
python <mount-path>/tooling/dtw.py init --repo-root .

# 3. wire a pre-commit hook — this half is per checkout, and a clone does not carry it
git config core.hooksPath .githooks

# 4. prove the guard fires, rather than believing it does:
#    name a file that does not exist in something you commit, and watch it refuse
```

That is four of the nine items. The other five are judgment — which revision to pin, what your
policy file says, what your ledger holds — and
[`document-harness/ONBOARDING.md`](document-harness/ONBOARDING.md) walks all nine, each with its
command, how you see it took, and which rule owns it.

## Where the bytes came from

The 254 files in this repository's first commit were copied byte-for-byte out of
`D:/Thesis` (worktree `D:/Thesis-stage-control-refactor`, branch `document-work-assurance-v3`)
at commit `e4ffa2b`, from under its `ResearchSystem/` directory; that repository is
private, and its history is not publicly reachable. **History was deliberately
not carried across** (`HD-40`, design §4): the caller's repository keeps every commit that
built these bytes — 335 of them touching this material — and `git log` there remains the way
to ask *why* any line reads as it does. The reasons live in commit bodies, which is this
harness's own discipline; the review records that travelled with the bytes carry what review
*found*, which is a different thing and not a substitute.

That pointer also answers a dangling reference: `tooling/rsclib/document_harness/__init__.py`
describes v3's lineage in terms of three v1/v2 modules that `HD-39` deleted, and which — this
repository having no history — never existed here either. They existed in the caller's
repository and are reachable there.

## Layout

Everything sits at the repository root: `document-harness/` (the instruction layer and its
records), `tooling/`, `schema/`, `contract/`, `migration/`, `assurance/`, and the governance
registers beside this file. Until round `DE-PREFIX` (batch DTW-INDEPENDENCE R3, `HD-50`,
2026-08-20) everything sat under `ResearchSystem/`, the path it occupied in the caller's
tree — the split's first round moved bytes only, because moving and re-rooting at once would
have made a byte move indistinguishable from a content change. The byte-identity claim
against the caller's `e4ffa2b` therefore holds at this repository's first commit, not at
`HEAD`; `git log --follow` crosses the rename. The instrument still locates its **own
files** by directory depth from `__file__`, not by name, and that depth survived the
re-rooting because each resolving file moved up together with its target; the repository a
command *targets* stopped being depth- or cwd-guessed in round `STRANGER-GUARDS` — it is
the git toplevel of where the command is pointed, or a loud refusal, never a wrong root
taken quietly.

## State of this repository — run these, do not trust a sentence

This section deliberately carries commands instead of claims. Its readers are agents and anyone
checking up on the paragraphs above; a sentence about the state goes stale the day something
changes, and two of this extraction's three review legs were spent falsifying sentences that
lived here.

One convention before the commands: `python` below means whichever of `python3` / `python`
this platform actually runs — stock Ubuntu ships only `python3` (every `python` row below
fails there verbatim, measured 2026-08-23), Windows typically `python`. If **both** are
present they need not be the same interpreter, and the hook's probe takes `python3` first
while you typing `python` may get the other — measured 2026-08-24, where only one of the two
had the dependencies installed and nothing said so until a guard tried to import. Substitute
accordingly; `.githooks/pre-commit` resolves its own choice by probing.

| Question | Command |
|---|---|
| Does the suite pass? | `python -m pytest -q` |
| Why does a test fail? | `python -m pytest -q --tb=line` |
| Do the instruction layer's nine members resolve here? | `python -c "import sys,pathlib; sys.path.insert(0,'tooling'); from hooks import layer_path_check as L; print([m for m in L.LAYER if not pathlib.Path(m).exists()])"` |
| Do the pre-commit guards bind? | stage a path that resolves nowhere into an instruction-layer file, then run each of `tooling/hooks/{layer_path_check,candidate_path_check,review_freeze_check}.py` and read the exit codes |
| Is a hook wired in THIS checkout? | `git config --get core.hooksPath` — exit 1 means nothing runs, whatever the tree carries; then `ls .githooks/pre-commit` for what would run |
| How do I onboard a repository that has never seen this? | `document-harness/ONBOARDING.md` — nine items, each with its command, its check, and the rule that owns it |
| Is there a CLI? | `ls tooling/dtw.py`; `python tooling/dtw.py --help` lists its commands — a count written here went stale twice (rider `RA`), so none is written |
| What do the CLI, the guards and the suite need? | Python ≥ 3.12 and `python -m pip install pytest "jsonschema>=4.18" referencing` — not the suite's alone: every `dtw` command and both caller-side guards import `jsonschema` too, so without it a wired hook fails every commit (measured 2026-08-24). The floor is measured, not decorative: Ubuntu 24.04's system jsonschema 4.10.3 fails 571 of these tests |
| Which files travelled and which stayed? | `document-harness/split-travel-manifest.md` — it carries the rule, not just the list |

What stays true of this repository regardless of when you read it:

- **The CLI is `tooling/dtw.py`** (alias `dtw`), extracted from the caller's `rsc.py` by the
  split batch's R2 on 2026-08-17. What commands it has is `--help`'s answer, never this
  file's: two sentences here counted them and both went stale.
- **Guard wiring is per-machine, and that half is all of it.** Since 2026-08-19 this
  repository carries a tracked `.githooks/pre-commit` running the instruction layer's path
  check — the extraction installed none, and the re-homing that closed that gap put the script
  in the tree, not in anyone's `.git/`. A clone carries the file; it does not carry the one
  `git config core.hooksPath .githooks` that makes git run it, so every checkout starts with
  nothing running until that command. The caller side works the same way. Whether a hook is
  wired in the checkout you are reading is the table row above, not this paragraph.
- **`E10-sync` falls due whenever the membership sentence is touched** — `HD-22` made it a
  per-touch checklist item; the 2026-08-18 charter round was one such moment, and round
  `DE-PREFIX`'s re-rooting was another — the act that stopped all ten of that day's members
  from resolving is exactly why that round changed all three mirrors in the commit that
  re-rooted (the count is nine since round `CONTRACT-V4` merged the two supersessions into
  contract v4 and admitted v4 as a member). The nine
  member paths are hard-coded in three places — the `E10` membership sentence in
  `document-harness/CONSTRUCTION-CHECKLIST.md`, the `LAYER` constant in
  `tooling/hooks/layer_path_check.py`, and the `EXPECTED` tuple in
  `tooling/tests/document_harness/test_precommit_checks.py`. Whether
  they resolve *today* is the third row of the table above; do not take this paragraph's word
  for it.
- **Licensed MIT** (`LICENSE`, user ruling 2026-08-23). The remote is whatever `git remote -v`
  prints in your checkout — a predecessor of this bullet asserted "No remote" and was the
  fourth of four false claims rider `readme-cli-stale` recorded against this section.

> This section previously asserted the guard state twice and got it wrong both times — once in
> each direction. Both corrections cost a review leg. The table replaced the assertions rather
> than a third attempt at wording them correctly (user ruling, 2026-08-15).

## Reading order

- `document-harness/README.md` — the instrument's own navigation surface.
- `document-harness/EXECUTION.md` and `REVIEW.md` — the two role instructions.
- `document-harness/CONSTRUCTION-CHECKLIST.md` — the `E`-rules a construction
  batch runs under.
- `HARNESS-DECISIONS.md` — the decision log; its `§live` section is required
  reading before opening a round.
- `document-harness/split-travel-manifest.md` — exactly which files travelled
  here and which stayed with the caller, with the rule that decided each.
- `document-harness/ONBOARDING.md` — if you are a repository that has never
  used this harness, start there instead: nine items, in order, each with how you see it took.
