# do-the-work

A document-work assurance harness: an instrument that makes a piece of document work
reviewable — a frozen instruction, a candidate, machine-checked evidence, and an independent
review whose verdict nobody in the loop can grant themselves.

It is **v3 of the Document Work Assurance harness**, extracted from the repository that grew
it. `HD-10` ruled the extraction necessary on the ground that the harness does not depend on
that repository to exist; a caller pins a version of this repo and runs it against its own
work.

## Where the bytes came from

The 254 files in this repository's first commit were copied byte-for-byte out of
`D:/Thesis` (worktree `D:/Thesis-stage-control-refactor`, branch `document-work-assurance-v3`)
at commit `e4ffa2b`, from under its `ResearchSystem/` directory. **History was deliberately
not carried across** (`HD-40`, design §4): the caller's repository keeps every commit that
built these bytes — 335 of them touching this material — and `git log` there remains the way
to ask *why* any line reads as it does. The reasons live in commit bodies, which is this
harness's own discipline; the review records that travelled with the bytes carry what review
*found*, which is a different thing and not a substitute.

That pointer also answers a dangling reference: `tooling/rsclib/document_harness/__init__.py`
describes v3's lineage in terms of three v1/v2 modules that `HD-39` deleted, and which — this
repository having no history — never existed here either. They existed in the caller's
repository and are reachable there.

## Layout — and why it still says `ResearchSystem/`

Everything sits under `ResearchSystem/`, the path it occupied in the caller's tree. That is
temporary and deliberate. The instrument resolves its own roots **by directory depth**, not by
name (`RS_ROOT = parents[3]`, `REPO_ROOT = parents[4]`), and three separate places hard-code
the instruction layer's ten members as strings beginning `ResearchSystem/`. Moving the bytes
and re-rooting them at once would have made a byte move indistinguishable from a content
change, so R1 moved bytes only: **the 254 files here are byte-identical to their sources**,
verifiable by comparing blob ids against the caller's repository at `e4ffa2b`.

Re-rooting is R2's work, together with this repository's own command-line entry point.

## State of this repository — run these, do not trust a sentence

This section deliberately carries commands instead of claims. Its only readers are agents, and
an agent can run a command; a sentence about the state goes stale the day something changes,
and two of this extraction's three review legs were spent falsifying sentences that lived here.

| Question | Command |
|---|---|
| Does the suite pass? | `python -m pytest -q` |
| Why does a test fail? | `python -m pytest -q --tb=line` |
| Do the instruction layer's ten members resolve here? | `python -c "import sys,pathlib; sys.path.insert(0,'ResearchSystem/tooling'); from hooks import layer_path_check as L; print([m for m in L.LAYER if not pathlib.Path(m).exists()])"` |
| Do the pre-commit guards bind? | stage a path that resolves nowhere into an instruction-layer file, then run each of `ResearchSystem/tooling/hooks/{layer_path_check,candidate_path_check,review_freeze_check}.py` and read the exit codes |
| Is a hook wired in THIS checkout? | `git config --get core.hooksPath` — exit 1 means nothing runs, whatever the tree carries; then `ls .githooks/pre-commit` for what would run |
| How do I onboard a repository that has never seen this? | `ResearchSystem/document-harness/ONBOARDING.md` — nine items, each with its command, its check, and the rule that owns it |
| Is there a CLI? | `ls ResearchSystem/tooling/dtw.py` |
| Which files travelled and which stayed? | `ResearchSystem/document-harness/split-travel-manifest.md` — it carries the rule, not just the list |

What stays true of this repository regardless of when you read it:

- **The CLI is not here.** `rsc.py` is the caller's by design; extracting the six v3 commands
  into `do-the-work` (alias `dtw`) is R2's work, riders `RA` / `CLI-hist`.
- **Some travelled tests read the caller's tree**, so the CLI extraction alone will not make the
  suite green. Whether an instrument's test may depend on its caller's content, and what
  replaces it if not, is R2's design question — this README does not settle it.
- **Guard wiring is per-machine, and that half is all of it.** Since 2026-08-19 this
  repository carries a tracked `.githooks/pre-commit` running the instruction layer's path
  check — the extraction installed none, and the re-homing that closed that gap put the script
  in the tree, not in anyone's `.git/`. A clone carries the file; it does not carry the one
  `git config core.hooksPath .githooks` that makes git run it, so every checkout starts with
  nothing running until that command. The caller side works the same way. Whether a hook is
  wired in the checkout you are reading is the table row above, not this paragraph.
- **`E10-sync` falls due whenever the membership sentence is touched** — `HD-22` made it a
  per-touch checklist item, so R2's re-rooting is one such moment and not the only one; the
  2026-08-18 charter round was another, and complied. The ten member paths are hard-coded
  with the caller's prefix in three places — the `E10` membership sentence in
  `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md`, the `LAYER` constant in
  `ResearchSystem/tooling/hooks/layer_path_check.py`, and the `EXPECTED` tuple in
  `ResearchSystem/tooling/tests/document_harness/test_precommit_checks.py`. Re-rooting is
  exactly the act that stops them resolving, so **R2 must change all three in the commit that
  re-roots**, or ship a window in which the guard passes without matching anything. Whether
  they resolve *today* is the third row of the table above; do not take this paragraph's word
  for it.
- **No remote.** The caller creates it.

> This section previously asserted the guard state twice and got it wrong both times — once in
> each direction. Both corrections cost a review leg. The table replaced the assertions rather
> than a third attempt at wording them correctly (user ruling, 2026-08-15).

## Reading order

- `ResearchSystem/document-harness/README.md` — the instrument's own navigation surface.
- `ResearchSystem/document-harness/EXECUTION.md` and `REVIEW.md` — the two role instructions.
- `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` — the `E`-rules a construction
  batch runs under.
- `ResearchSystem/HARNESS-DECISIONS.md` — the decision log; its `§live` section is required
  reading before opening a round.
- `ResearchSystem/document-harness/split-travel-manifest.md` — exactly which files travelled
  here and which stayed with the caller, with the rule that decided each.
- `ResearchSystem/document-harness/ONBOARDING.md` — if you are a repository that has never
  used this harness, start there instead: nine items, in order, each with how you see it took.
