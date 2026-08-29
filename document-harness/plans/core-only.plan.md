# Plan — batch `CORE-ONLY`: a repository that mounts only the core set can actually run

> **Status: NOT OPENED.** Written 2026-08-29 by the orchestrator, after batch `V1-RESULT-RETIRE`
> closed. **base_commit**: the `dev` tip at the moment the first round opens — stated then, not
> derived from `main`, for the reason `V1-RESULT-RETIRE`'s own base correction records.
>
> **This file is the carrier of the user's rulings of 2026-08-29** in *Rulings* below. Until they
> land here they live only in the conversation that took them, which is chat-only load-bearing
> material and a finding under `R2`.
>
> **Every figure below was measured on 2026-08-29 at `607728a`** with `tooling/sweep_refs.py` and
> `git ls-files`. `E3`: re-run them before any claim; line numbers drift.
>
> **This is design.** Rider `checklist-cited-not-carried`'s own header says every way out is design,
> and the work below changes what `E10`'s membership sentence and `CONSTRUCTION-INDEX.md`'s tier
> table say. It opens a round, and the opening cold read is not waivable by this file.
>
> A cold session reads this file, then `CONSTRUCTION-LEDGER.md`'s current pointer, then works.

## Goal (one line)

A repository that mounts **only the 58-file core set** can open a run, run it, and close it — with
no reference in what it carries pointing at something it does not have, and no code in what it
carries existing solely to serve rounds it will never open.

## Rulings (this file is their carrier)

1. **Core-only usability comes before the first product run** (2026-08-29). The queue order
   committed hours earlier at `689ae5d` put a real product run first; the user overturned it the
   same day — *不需要着急跑 run，而是先让库能只跑 core*. Recorded at `607728a`.
2. **Option B, not A and not C** (2026-08-29, *做 B 吧*). The three shapes were put to the user as:
   **(A)** repair the 34 dangling references only; **(B)** actually split — divide the code and the
   documents along the product/construction line the tier table already claims; **(C)** let
   `CONSTRUCTION-CHECKLIST.md` travel, making the breaks vanish by abandoning the goal. B was
   chosen. **A was refused with its reason on the record**: it makes the tree *look* clean while a
   caller still receives 42% of `dispatch.py`, the matching branches of `cli.py`, all of
   `layer_path_check.py`, and a constant naming a file it does not have.
3. **The distribution form is conditional, and this batch is the test of it** (`HD-66`,
   2026-08-29). submodule is the default and not the end state; if core distribution is finally
   shown impossible, the answer is a plugin. `HD-66`'s boundary names three untried paths, and this
   batch **is** its option two. If this batch fails, that is evidence toward `HD-66`'s trigger —
   **but declaring the trigger fired is the user's, not this batch's.**

## Measured starting state — 2026-08-29 at `607728a`

### What "core" is: 58 files, and the row that is wrong about itself

| # | row of `CONSTRUCTION-INDEX.md` | files |
|---|---|---|
| 1 | `contract/Document-Work-Assurance-Contract-v4.md` | 1 |
| 2 | `schema/document-assurance-v3/` | 14 |
| 3 | README · EXECUTION · REVIEW · ORCHESTRATION | 4 |
| 4 | `ONBOARDING.md` | 1 |
| 5 | `document-harness/templates/` | 2 |
| 6 | `tooling/dtw.py` · `tooling/do-the-work.py` | 2 |
| 7 | `tooling/rsclib/document_harness/` | 22 |
| 8 | `tooling/hooks/` 4 + `assurance/templates/run-v2/` 8 | 12 |
| | **total** | **58** against a repository of **409** |

**Row 8 contradicts its own description.** Its prose says *"the two caller-side guards a caller
wires into its own `pre-commit`"* while the count takes the whole of `tooling/hooks/`, which is
four files: `__init__.py`, `candidate_path_check.py`, `review_freeze_check.py` and
`layer_path_check.py`. The third of those is not caller-side — see item C.

### The reference breakage, by whose fault it is

Three trees, one instrument (`tooling/sweep_refs.py`), over `E10`'s nine members:

| tree | files | non-resolving sites |
|---|---|---|
| this repository | 409 | **14** |
| history-stripped (batch `CORE-SET`'s) | 120 | 3 |
| **product tier only** | **58** | **48** |

**14 of the 48 also fail on the full repository and are not this batch's business.** All fourteen
are NAMETOK — a backticked bare filename — and `E10` requires exactly that form for a caller-held
artifact: *"a caller-held path is named, never written as a path token"*. Twelve name a caller's own
run artifacts (`build_run.py`, `check_shells.py`, `write_audit.py`, `smoke_test.py`,
`run_p4_tests.py`, `run_p5a_tests.py`, `audit-rounds.md` ×2, `v3-review-full-86defbc.md`,
`user-decision-triage-comparator-environment-defects.json`, `v3-review-full-fef3a2e.md`,
`review-verify.json`); two are deliberate history (`Document-Work-Assurance-Contract-v3.md`, which
`HD-62` leaves in git history, and `review.schema.json`, which round `V1-RESULT-RETIRE` retired and
contract v4 names in the past tense). **Repairing any of these would violate `E10`, not satisfy
it.** The count moved 13 → 14 in that round, the new one being the past-tense sentence it wrote.

**34 sites break only because the tree was stripped to core.** That set is this batch's subject:

| type | count | what it means |
|---|---|---|
| `MISSING` | 3 | an `E10` member absent from the tree entirely |
| `LINK` | 5 | a markdown link whose target is not there |
| `PATHTOK` | 2 | a backticked path with a `/` that resolves nowhere |
| `NAMETOK` | 24 | a backticked bare name matching no file — **and, unlike the 14 above, naming something the caller has no holder for at all** |

The 24 NAMETOK sites carry **14 distinct targets**: `CONSTRUCTION-CHECKLIST.md`,
`CONSTRUCTION-INDEX.md`, `CONTRACT-V4-SIGNATURE.md`, `HARNESS-DECISIONS.md`, `N0-record.md`,
`W2-record.md`, `supersession-2-signature.md`, `retro-2026-08-03.md`,
`v3-review-verify-2538893.md`, `contract-v4.plan.md`,
`general-harness-v2-architecture-revision.plan.md`, `run_tests.py`,
`test_readme_enumeration.py`, `validate_fixtures.py`.

**The distinction that decides every one of them is who holds the thing.** A caller-held artifact
named by bare name is compliant and stays. An *instrument-construction*-held artifact named by bare
name is not compliant on a core tree, because the caller has no holder for it — the sentence
`E10` demands ("its name and its holder") cannot be completed.

### The 34 sites verbatim

Re-derive before editing; these are at `607728a`.

```
MISSING  document-harness/CONSTRUCTION-CHECKLIST.md
MISSING  migration/document-work-assurance-v3/v3-harness-operating-contract.md
MISSING  migration/document-work-assurance-v3/v3-harness-review-contract.md
LINK     document-harness/README.md:23        CONSTRUCTION-CHECKLIST.md
LINK     document-harness/EXECUTION.md:13     CONSTRUCTION-CHECKLIST.md
LINK     document-harness/REVIEW.md:8         CONSTRUCTION-CHECKLIST.md
LINK     document-harness/ORCHESTRATION.md:7  CONSTRUCTION-CHECKLIST.md
LINK     document-harness/ORCHESTRATION.md:39 CONSTRUCTION-CHECKLIST.md
PATHTOK  document-harness/README.md:20        tooling/tests/document_harness/test_readme_enumeration.py
PATHTOK  document-harness/README.md:26        .githooks/
NAMETOK  document-harness/README.md:16        CONTRACT-V4-SIGNATURE.md · N0-record.md · W2-record.md · supersession-2-signature.md
NAMETOK  document-harness/README.md:24        CONSTRUCTION-INDEX.md
NAMETOK  document-harness/README.md:26        v3-review-verify-2538893.md
NAMETOK  document-harness/README.md:29        general-harness-v2-architecture-revision.plan.md
NAMETOK  document-harness/EXECUTION.md:13     CONSTRUCTION-CHECKLIST.md
NAMETOK  document-harness/EXECUTION.md:110    W2-record.md
NAMETOK  document-harness/EXECUTION.md:350    test_readme_enumeration.py
NAMETOK  document-harness/EXECUTION.md:375    run_tests.py
NAMETOK  document-harness/EXECUTION.md:377    validate_fixtures.py
NAMETOK  document-harness/EXECUTION.md:394    run_tests.py
NAMETOK  document-harness/EXECUTION.md:400    retro-2026-08-03.md
NAMETOK  document-harness/REVIEW.md:8         CONSTRUCTION-CHECKLIST.md
NAMETOK  document-harness/REVIEW.md:89        W2-record.md
NAMETOK  document-harness/ORCHESTRATION.md:51 HARNESS-DECISIONS.md
NAMETOK  contract/…-v4.md:16                  CONTRACT-V4-SIGNATURE.md
NAMETOK  contract/…-v4.md:27                  N0-record.md
NAMETOK  contract/…-v4.md:28                  W2-record.md
NAMETOK  contract/…-v4.md:31                  supersession-2-signature.md
NAMETOK  contract/…-v4.md:33                  contract-v4.plan.md
NAMETOK  contract/…-v4.md:254                 N0-record.md
NAMETOK  contract/…-v4.md:365                 CONTRACT-V4-SIGNATURE.md
```

**Seven of the 34 sit in signed contract text** — contract v4 at `:16`, `:27`, `:28`, `:31`, `:33`,
`:254` and `:365`. (The sweep reports nine contract sites on a core tree; the other two,
`Document-Work-Assurance-Contract-v3.md` and `review.schema.json`, fail on the full repository too
and belong to the fourteen this batch leaves alone.) Round `V1-RESULT-RETIRE` established the only
routes into signed text: a recorded user ruling of the `HD-63` shape for a stale statement of fact,
the `HD-64` shape for a requirement, or §13's versioned successor. **Whichever is chosen, it is a
ruling this batch must obtain and never assume** — and the user has already ruled twice on this
surface in one round, so a third is not automatic.

### The code the caller receives and cannot use

Measured by reading the modules, not by grepping the word *construction* — three of the four small
hits that grep produced (`checks.py`, `instruction.py`, `review_subject.py`) are the ordinary
English usage (*Result construction*, *by construction*) and are **not** coupling.

| # | site | size | why a caller cannot use it |
|---|---|---|---|
| 1 | `tooling/rsclib/document_harness/dispatch.py` | **≈423 of 1,005 lines (42%)** — `--range` ≈123, `--read` ≈105, `--construction-executor` ≈195 | all three modes exist only for construction rounds; a caller opens none |
| 2 | `tooling/rsclib/document_harness/cli.py` | the `dispatch` handler from `:167`, 23 construction references | the command-line entry to the three modes above |
| 3 | `tooling/hooks/layer_path_check.py` | **the whole file, 134 lines** | it guards `E10`'s nine members, three of which do not travel; **unwired from the caller on 2026-08-17** with 0 of 9 resolving there, stated in this repository's own `.githooks/pre-commit` |

Plus one hard-coded constant in product-tier code naming a file that does not travel:
`dispatch.py:776` — `CONSTRUCTION_EXECUTOR_CHARTER = "document-harness/CONSTRUCTION-CHECKLIST.md"`.

## Open questions — the user's, and the batch does not open until they are answered

1. **Where do the product-side rules live once the checklist stays behind?** The five product
   documents carry 11 path references to `CONSTRUCTION-CHECKLIST.md` and 37 backticked `E1`–`E12` /
   `R1`–`R10` citations across 33 lines. Three shapes: **(i)** the product tier gets its own rule
   file holding the clauses it actually cites; **(ii)** the citations are rewritten to state the
   rule inline and stop naming a code; **(iii)** the checklist is split, its product-relevant half
   travelling under a new name. Each changes what `E10`'s membership sentence must say.
2. **What happens to `E10`'s membership sentence?** It names nine paths, three of which are
   construction-side. Does the layer become two layers, one per side, or does membership become
   tier-aware? This is the question `HD-21` asked about a different file and it now returns for the
   sentence itself.
3. **The seven contract v4 sites.** `HD-63` shape (a recorded ruling permitting in-place
   correction), `HD-64` shape (the same for a requirement), or §13's versioned successor. The user
   ruled twice on this surface in one round; a third ruling is not automatic.
4. **Does `layer_path_check.py` leave the product tier, and does `tooling/hooks/`'s row get split?**
   Row 8 takes a whole directory and describes two files.
5. **How is "it runs" verified?** Proposal: batch `CORE-SET` step 6b's mechanical check, re-run on a
   58-file tree — `dtw --help`, `dtw init` into a fresh repository, the caller-side guards exiting
   0. It needs no run directory and does not depend on the product run this batch now precedes.
   **Confirm or replace.**

## Out of scope

- OUT: running a product run. It is queue position ②, behind this batch by the user's 2026-08-29
  direction.
- OUT: the candidate-isolation design question (queue ③, still unruled).
- OUT: `dispatch-economy` (queue ④).
- OUT: declaring `HD-66`'s plugin trigger fired. This batch produces evidence; the declaration is
  the user's.
- OUT: sparse-checkout as a substitute. It materialises fewer files and makes not one reference
  resolve — ruling 2's stated reason for refusing shape A applies to it in full.

## Sketch of the work — not a decomposition, and the executor writes its own

The shape follows from the questions above and firms up when they are answered.

- **A** — the rule surface: whatever question 1 settles, applied to the five product documents' 11
  path references and 37 code citations.
- **B** — `E10`'s membership sentence, per question 2. `layer_path_check.py`'s `LAYER` tuple and
  `sweep_refs.py` both import from it, so they follow rather than being edited in parallel.
- **C** — the three code sites: `dispatch.py`'s construction modes, `cli.py`'s matching branches,
  and `layer_path_check.py`'s tier. Every one of them changes `CONSTRUCTION-INDEX.md`'s tier table.
- **D** — the seven contract v4 sites, under whatever question 3 rules.
- **E** — `CONSTRUCTION-INDEX.md` itself: row 8's prose against its count, and every row this batch
  moves.
- **F** — rider `checklist-cited-not-carried` redeemed, and `onboarding-carries-construction`
  checked for whether it redeems with it.

## Acceptance (done = ?)

Each a command, not a sentence.

1. A 58-file (or whatever this batch makes it) product-tier tree, built by `git archive` and made a
   git repository, reports **zero** non-resolving sites that name an instrument-construction-held
   artifact. Caller-held bare names remain and are counted separately — the two classes are
   reported apart, because collapsing them is how this defect hid.
2. `python tooling/sweep_refs.py <core tree>` and the same on the full repository, both pasted.
3. On that tree: `dtw --help` exit 0 · `dtw init` into a fresh repository exit 0 · the caller-side
   guards exit 0. (Question 5 may replace this.)
4. `grep -rn 'CONSTRUCTION-CHECKLIST' <core tree>` returns nothing, or returns only what a ruling
   admitted, each accounted for in a commit body.
5. No file in the core tree contains a construction-only code path. Demonstrated by naming what
   moved and re-measuring `dispatch.py`'s and `cli.py`'s line counts either side.
6. `python -m pytest tooling/tests -q` green on the full repository, with the delta accounted.
7. `CONSTRUCTION-INDEX.md`'s counts re-measured by its own *How to re-measure* commands, and row
   8's prose agreeing with its count.
8. The three guards exit 0 and `E10`'s members resolve N/N for whatever N the membership sentence
   ends up naming.
9. Rider `checklist-cited-not-carried` deleted in the commit that earns it.

## Resume pointer

当前指针: **not opened — the five open questions above go to the user first.** Nothing is measured
that has not been measured here, and nothing is decided that is theirs.

## Notes

- **Why A was refused, kept because a future reader will re-propose it.** A repairs 34 references
  and leaves a caller holding 42% of `dispatch.py`, `cli.py`'s matching branches, all 134 lines of
  `layer_path_check.py`, and `dispatch.py:776`'s constant naming a file it does not have. It buys a
  clean sweep output and nothing else.
- **Why the 14 full-repository sites are not a defect, kept because the number looks like one.**
  `E10` requires a caller-held artifact be named rather than pathed, so those bare names are the
  compliant form. A round that "fixes" them breaks the rule it thinks it is serving.
- **What this batch is evidence for.** `HD-66` made distribution conditional on core distribution
  being shown impossible. This batch is the attempt. Its failure would be evidence toward the
  plugin; its success closes the question. Neither conclusion is this file's to draw.
