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

- **The pre-commit guards are not wired here.** `tooling/hooks/layer_path_check.py` matches
  staged paths against a hard-coded member list; a caller-shaped prefix means it matches
  nothing and passes silently while looking green. Rider `E10-sync` requires its three mirrors
  — the `E10` membership sentence, that `LAYER` constant, and the `EXPECTED` tuple in
  `tooling/tests/document_harness/test_precommit_checks.py` — to change together and be named
  in the commit body. That is a change to instruction-layer rule text, which R1 had no
  authority to make.
- **There is no CLI entry point here.** The six v3 commands still live in the caller's
  `rsc.py`; extracting them is R2 (`rider RA` / `CLI-hist`). The command names will be
  `do-the-work` with the short alias `dtw`.
- **No remote.** The caller creates it.

## Reading order

- `ResearchSystem/document-harness/README.md` — the instrument's own navigation surface.
- `ResearchSystem/document-harness/EXECUTION.md` and `REVIEW.md` — the two role instructions.
- `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` — the `E`-rules a construction
  batch runs under.
- `ResearchSystem/HARNESS-DECISIONS.md` — the decision log; its `§live` section is required
  reading before opening a round.
- `ResearchSystem/document-harness/split-travel-manifest.md` — exactly which files travelled
  here and which stayed with the caller, with the rule that decided each.
