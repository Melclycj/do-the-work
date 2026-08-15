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
the instruction layer's nine members as strings beginning `ResearchSystem/`. Moving the bytes
and re-rooting them at once would have made a byte move indistinguishable from a content
change, so R1 moved bytes only: **the 254 files here are byte-identical to their sources**,
verifiable by comparing blob ids against the caller's repository at `e4ffa2b`.

Re-rooting is R2's work, together with this repository's own command-line entry point.

## What does not work yet

- **There is no CLI entry point here.** The six v3 commands still live in the caller's
  `rsc.py`, which is deliberately outside the travel set. Extracting them is R2 (riders `RA` /
  `CLI-hist`); the command will be `do-the-work`, short alias `dtw`.
- **The suite here is red, not vacuously green.** Measured: `python -m pytest -q` →
  **20 failed, 681 passed**. Broken down by traceback rather than assumed:

  | failures | cause | cleared by |
  |---|---|---|
  | 15 | traceback names the absent `ResearchSystem/tooling/rsc.py` | R2's CLI extraction |
  | 2 | a subprocess that runs `rsc.py` exits 2 instead of 1 — caused by it, does not name it | R2's CLI extraction |
  | 3 | `governance document not readable at <root>/.goals/plans/document-work-assurance-harness-v3.plan.md` | **nothing yet** — see below |

  **Extracting the CLI does not by itself green this suite.** Three tests read a document that
  lives in the caller's tree and was never part of the travel set. Whether an instrument test may
  depend on its caller's content — and if not, what replaces it — is a design question for R2,
  deliberately not settled by this README.

  It was 24 failed / 677 passed at `8cd0b9c`; four of those were travelled tests whose goldens had
  not travelled, closed by adding travel-set row `A10` (`assurance/test/` plus the two
  `expected-*-prompt.txt` files). Two of them printed *"golden missing: run this file with
  --regen"* — following that instruction here would have overwritten a pinned user-visible
  surface with whatever this repository currently renders, which is exactly what the pin exists
  to prevent.
- **No hook is installed in `.git/hooks`.** That is the harness's standing per-machine
  convention (`ResearchSystem/document-harness/README.md`, "Local enforcement"), not a
  property of this extraction: a fresh clone of the caller's repository has no hook either.
- **No remote.** The caller creates it.

### The guards themselves are live — and that is what schedules `E10-sync`

Keeping the `ResearchSystem/` prefix (see §Layout) is what makes the hard-coded member list
resolve. Measured here, not assumed: all nine `LAYER` members exist; staging a path that
resolves nowhere into an instruction-layer file makes `tooling/hooks/layer_path_check.py` and
`tooling/hooks/candidate_path_check.py` both exit 1 and block. `review_freeze_check.py` exits 0
because `.harness/review-pending.json` is the **caller's** file under `HD-33` — designed
inertness. `pytest tests/document_harness/test_precommit_checks.py` → 42 passed.

So the member list is correct today and **stops being correct the moment R2 re-roots**, because
re-rooting is exactly what stops those nine strings resolving. Rider `E10-sync` requires its
three mirrors — the `E10` membership sentence in
`ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md`, that `LAYER` constant, and the
`EXPECTED` tuple in `ResearchSystem/tooling/tests/document_harness/test_precommit_checks.py` —
to change together and be named in the commit body. **R2 must put that edit in the same commit
as the re-rooting**, or ship a window in which the guard is silently dead. R1 left the three
alone because editing the `E10` membership sentence is editing rule text and R1 had no
authority for it — not because they were broken.

> An earlier version of this section claimed the guards here "match nothing and pass silently
> while looking green". That was written in the same commit as the decision that made it false,
> and no one ran the one-line check that would have caught it. Corrected under FULL `B-1`.

## Reading order

- `ResearchSystem/document-harness/README.md` — the instrument's own navigation surface.
- `ResearchSystem/document-harness/EXECUTION.md` and `REVIEW.md` — the two role instructions.
- `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` — the `E`-rules a construction
  batch runs under.
- `ResearchSystem/HARNESS-DECISIONS.md` — the decision log; its `§live` section is required
  reading before opening a round.
- `ResearchSystem/document-harness/split-travel-manifest.md` — exactly which files travelled
  here and which stayed with the caller, with the rule that decided each.
