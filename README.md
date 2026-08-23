# do-the-work

![CI](https://github.com/Melclycj/do-the-work/actions/workflows/ci.yml/badge.svg)

A document-work assurance harness: an instrument that makes a piece of document work
reviewable — a frozen instruction, a candidate, machine-checked evidence, and an independent
review whose verdict nobody in the loop can grant themselves.

It is **v3 of the Document Work Assurance harness**, extracted from the repository that grew
it. `HD-10` ruled the extraction necessary on the ground that the harness does not depend on
that repository to exist; a caller pins a version of this repo and runs it against its own
work.

## Where the bytes came from

The 254 files in this repository's first commit were copied byte-for-byte out of
`https://github.com/Melclycj/Thesis-Work`, branch `document-work-assurance-v3` — the
historical record names it by its single-machine paths, `D:/Thesis` (worktree
`D:/Thesis-stage-control-refactor`), which are where the work happened and stay as
recorded — at commit `e4ffa2b`, from under its `ResearchSystem/` directory. Both that
commit and `7011916`, the other id this repository's instruction layer sends readers
there for, are on the branch as pushed (verified 2026-08-23, `git merge-base
--is-ancestor` against `origin/document-work-assurance-v3`). That repository answers
anonymous access with an authentication challenge — private, as measured the same day —
so the name is a durable address to request access to, not an open door; whether it opens
is its owner's, not this file's. **History was deliberately
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

This section deliberately carries commands instead of claims. Its only readers are agents, and
an agent can run a command; a sentence about the state goes stale the day something changes,
and two of this extraction's three review legs were spent falsifying sentences that lived here.

One convention before the commands: `python` below means whichever of `python3` / `python`
this platform actually runs — stock Ubuntu ships only `python3` (every `python` row below
fails there verbatim, measured 2026-08-23), Windows typically `python`. Substitute
accordingly; `.githooks/pre-commit` resolves the same choice by probing.

| Question | Command |
|---|---|
| Does the suite pass? | `python -m pytest -q` |
| Why does a test fail? | `python -m pytest -q --tb=line` |
| Do the instruction layer's nine members resolve here? | `python -c "import sys,pathlib; sys.path.insert(0,'tooling'); from hooks import layer_path_check as L; print([m for m in L.LAYER if not pathlib.Path(m).exists()])"` |
| Do the pre-commit guards bind? | stage a path that resolves nowhere into an instruction-layer file, then run each of `tooling/hooks/{layer_path_check,candidate_path_check,review_freeze_check}.py` and read the exit codes |
| Is a hook wired in THIS checkout? | `git config --get core.hooksPath` — exit 1 means nothing runs, whatever the tree carries; then `ls .githooks/pre-commit` for what would run |
| How do I onboard a repository that has never seen this? | `document-harness/ONBOARDING.md` — nine items, each with its command, its check, and the rule that owns it |
| Is there a CLI? | `ls tooling/dtw.py`; `python tooling/dtw.py --help` lists its commands — a count written here went stale twice (rider `RA`), so none is written |
| What does the suite need? | Python ≥ 3.12 and `python -m pip install pytest "jsonschema>=4.18" referencing` — the floor is measured, not decorative: Ubuntu 24.04's system jsonschema 4.10.3 fails 571 of these tests |
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
