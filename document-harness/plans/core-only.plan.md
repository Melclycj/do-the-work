# Plan — batch `CORE-ONLY`: the construction side becomes an ordinary caller of the harness

> **Status: NOT OPENED.** Rewritten 2026-08-29 after the framing below replaced the one this file
> carried at `18d120d`. **base_commit**: the `dev` tip when the first round opens — stated then,
> not derived from `main`, for the reason `V1-RESULT-RETIRE`'s own base correction records.
>
> **This file is the carrier of the user's rulings of 2026-08-29** in *Rulings*. Until they land
> here they live only in the conversation that took them, which is chat-only load-bearing material
> and a finding under `R2`.
>
> **Every figure was measured 2026-08-29 at `607728a`** with `tooling/sweep_refs.py`, `git ls-files`
> and `grep`. Re-run them before any claim; line numbers drift.
>
> **This is design.** It changes what the instruction-layer membership rule says, so a round opens
> and the opening cold read is not waivable by this file.
>
> A cold session reads this file, then `CONSTRUCTION-LEDGER.md`'s current pointer, then works.

## What changed from the version at `18d120d`, written forward rather than over

That version framed the work as three shapes — repair the dangling references, split the code, or
let the construction checklist travel — and asked the user to pick. **The user replaced the frame
rather than picking from it**: *如果按照开发层自己是 harness 的一个实例来看，需要做到所有库自己的
规则都是 harness 的附加*. That is not shape C, and it subsumes shape B. Everything below follows
from it. Four things the earlier version got wrong or too small, each corrected here and left
visible because it was committed:

1. **The citation count was 37; it is 36.** `EXECUTION.md:235`'s `` `R0` `` is a product run's own
   review-dimension name, not a citation of a construction rule. No such rule exists.
2. **The contract work was stated as "seven sites needing a ruling"; that is the wrong unit.**
   Three of the seven already carry the holder clause the rule asks for. The real object is three
   blocks of provenance, not seven lines — see *The contract's provenance*.
3. **"The layer guard follows the construction side" was wrong.** Under ruling 5 it becomes a
   general guard that both sides use. Stated in the earlier version's item C; withdrawn here.
4. **The A/B/C framing is withdrawn entire.** It is preserved in this paragraph because a future
   reader will re-derive it, and because ruling 2's reason is not "B was cheapest".

## Goal (one line)

**The construction side stops being a special case and becomes an ordinary caller**: the harness
carries the rules every caller needs, each caller — this instrument included — declares its own
additions, and a repository that mounts only the harness can open, run and close a real run.

## Rulings (this file is their carrier)

1. **Core-only usability comes before the first product run** (2026-08-29). Overturns the queue
   order committed hours earlier at `689ae5d`. Recorded at `607728a`.
2. **The construction side is an instance of the harness applied to itself, so its own rules are an
   *addition* to the harness rather than part of it** (2026-08-29). This is the frame, and the
   reason is structural rather than economic. Consequence: the construction checklist splits — the
   part every caller needs travels as harness text, the part that is only this instrument's own
   working discipline stays as this instrument's caller-side addition.
3. **Acceptance is the mechanical check *and* a real product run** (2026-08-29, 机械检查 + 产品
   run 实测). This pulls the product run — queue position ② until now — into this batch, and with
   it the 2026-08-23 ruling that a first product run happens in a caller repository rather than
   here. The batch therefore spans two repositories.
4. **The contract's provenance goes with this batch** (2026-08-29, 要一起做了). A product contract
   carrying this instrument's construction history is pollution of the rule text; the earlier
   answer — label each citation with its holder — treated the symptom.
5. **The instruction-layer membership rule does not cover the construction side** (2026-08-29).
   It names the harness's own members; every caller, this instrument included, declares its own
   additions. The guard reads the union.
6. **The two retired-contract stubs may be removed if the work permits** (2026-08-29, 可以看着
   情况移除). Not mandated — item D states the condition.
7. **How a caller declares its additions is decided at round open, not here** (2026-08-29, answer
   to *这个留到开轮再做吗*). This file enumerates the candidate shapes so the decision is one
   sitting rather than research, and records what `E6` asks of any of them.

## Measured starting state — 2026-08-29 at `607728a`

### What the harness carries today: 58 files of 409

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
| | **total** | **58** |

**Row 8 disagrees with itself**: its prose says *"the two caller-side guards a caller wires into its
own `pre-commit`"* while its count takes all four files in `tooling/hooks/`. Under ruling 5 the
disagreement dissolves rather than being repaired — see item C.

### The rule surface: 36 citations, and 26 of them are shared

Counted over the five product documents with
`grep -ohE '`(E[0-9]{1,2}|R[0-9]{1,2})`'`, minus the one false positive named above:

| what the cited rule says | citations | does a product run obey it? |
|---|---|---|
| never review, verify or sign your own work | 5 | **yes** |
| the per-round review budget: one FULL, at most one approved fix, one VERIFY | 5 | **yes** |
| how findings route — bank, HarnessIssue, or the caller's own bank | 4 | **yes** |
| whether a thing should exist at all is the user's question, not the reviewer's | 3 | **yes** |
| the preview card before starting, and waiting for the user | 3 | **yes** |
| independence is decided by who set the question | 2 | **yes** |
| what a review record is called and where it goes | 2 | **yes** |
| measure last; a figure is invalidated by any later change | 1 | **yes** |
| the handoff is one commit or range, with no per-acceptance argument | 1 | **yes** |
| **subtotal — shared** | **26** | |
| the instruction layer is exactly these nine files, and how to amend them | 8 | **no** — this instrument's own rule text |
| the announced/frozen surface | 1 | **no** — this instrument's own bytes |
| never trust a guard you have not seen fail | 1 | construction-leaning |
| **subtotal — this instrument's own** | **10** | |

**This is the measurement ruling 2 rests on.** The checklist is not a construction file with
product rules leaking into it; it is the *only home* of rules both sides obey, and that home was
filed on the construction side.

### The reference breakage: 48 sites, of which 34 are this batch's

Three trees, one instrument (`tooling/sweep_refs.py`), over the nine members:

| tree | files | non-resolving sites |
|---|---|---|
| this repository | 409 | **14** |
| history-stripped (batch `CORE-SET`'s) | 120 | 3 |
| **harness-only** | **58** | **48** |

**The 14 are not defects and must not be "fixed".** All are a backticked bare filename, which is
the form the membership rule *requires* for a caller-held artifact — *a caller-held path is named,
never written as a path token*. Twelve name a caller's own run artifacts (`build_run.py`,
`check_shells.py`, `write_audit.py`, `smoke_test.py`, `run_p4_tests.py`, `run_p5a_tests.py`,
`audit-rounds.md` ×2, `v3-review-full-86defbc.md`,
`user-decision-triage-comparator-environment-defects.json`, `v3-review-full-fef3a2e.md`,
`review-verify.json`); two are deliberate history (`Document-Work-Assurance-Contract-v3.md`, left
in git history by `HD-62`, and `review.schema.json`, which round `V1-RESULT-RETIRE` retired and the
contract names in the past tense). That count moved 13 → 14 in that round, the new one being the
past-tense sentence it wrote.

**34 break only because the tree was stripped.** 3 members absent · 5 markdown links · 2 path
tokens · 24 bare names carrying 14 distinct targets: `CONSTRUCTION-CHECKLIST.md`,
`CONSTRUCTION-INDEX.md`, `CONTRACT-V4-SIGNATURE.md`, `HARNESS-DECISIONS.md`, `N0-record.md`,
`W2-record.md`, `supersession-2-signature.md`, `retro-2026-08-03.md`,
`v3-review-verify-2538893.md`, `contract-v4.plan.md`,
`general-harness-v2-architecture-revision.plan.md`, `run_tests.py`, `test_readme_enumeration.py`,
`validate_fixtures.py`.

**The judge for every one is who holds the thing.** A caller holds its own run artifacts, so a bare
name is complete. Nobody on the caller's side holds this instrument's construction history, so the
sentence the rule demands — *its name and its holder* — cannot be completed at all.

**The 34, verbatim at `607728a`. Re-derive before editing.**

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
NAMETOK  contract/…-v4.md:16   CONTRACT-V4-SIGNATURE.md
NAMETOK  contract/…-v4.md:27   N0-record.md
NAMETOK  contract/…-v4.md:28   W2-record.md
NAMETOK  contract/…-v4.md:31   supersession-2-signature.md
NAMETOK  contract/…-v4.md:33   contract-v4.plan.md
NAMETOK  contract/…-v4.md:254  N0-record.md
NAMETOK  contract/…-v4.md:365  CONTRACT-V4-SIGNATURE.md
```

### The contract's provenance — ruling 4's object, in blocks rather than lines

| block | size | what it is | verdict |
|---|---|---|---|
| §12 *Dependency and historical map*, first two paragraphs | ~12 lines | v1/v2 immutability, A4 as accepted v2 history, the nominated reuse candidates recorded in `N0-record.md` | **construction history** |
| §12's third paragraph | ~6 lines | what was removed from the v3 default interface and may never return without an approved amendment | **operative for a caller — stays** |
| `:24-33`, the merged-sources paragraph | 10 lines | which three documents v4 merged, their blob hashes, signature dates and record filenames | **construction history** |
| the signature-semantics header and §14 | a few lines | that a signature binds and where the record lives | **operative, but the record can be named by holder rather than by filename** |

Three of the seven sites already carry *held by this instrument's own construction record*. **That
is the compliant form, and it is also the evidence that whoever wrote it already knew the caller
could not reach these** — and answered by labelling rather than by removing. Ruling 4 chooses
removal.

### The code the caller receives and cannot use

Measured by reading the modules. Three of the four hits a grep for *construction* produced
(`checks.py`, `instruction.py`, `review_subject.py`) are the ordinary English word and are **not**
coupling.

| # | site | size | note |
|---|---|---|---|
| 1 | `dispatch.py` | **≈423 of 1,005 lines** — `--range` ≈123, `--read` ≈105, `--construction-executor` ≈195 | three modes only a construction round uses |
| 2 | `cli.py` | the `dispatch` handler from `:167`, 23 construction references | their command-line entry |
| 3 | `tooling/hooks/layer_path_check.py` | 134 lines | **under ruling 5 this becomes general rather than moving** — it reads the harness members plus the local declaration |

One hard-coded constant in product-tier code names a file that does not travel: `dispatch.py:776`,
`CONSTRUCTION_EXECUTOR_CHARTER = "document-harness/CONSTRUCTION-CHECKLIST.md"`. A second,
`dispatch.py:549`, names the retired review-side stub as every cold reviewer's standing
instruction, and `test_dispatch.py` pins it in three hand-written constants.

### The declaration precedent this repository already has

`.harness/scan-surfaces.json` — `{"review_record_dirs": ["migration/document-work-assurance-v3/"]}`
— is a per-repository declaration of a repo-local surface, read by `caller.py:42` and written by
`dtw init`. **Membership additions could take the same shape.** It is per-checkout and gitignored,
which is a known cost: every fresh clone rewrites it.

## Open questions — answered at round open, before any work

1. **What is the shared half called and where does it live?** It decides what a dispatch prompt
   points at, and therefore whether the two stubs survive (ruling 6's condition).
2. **How does a caller declare its additions?** Ruling 7 defers the choice; the candidates are:
   **(a)** a new declaration file; **(b)** a key added to `.harness/scan-surfaces.json`, which
   already exists and is already read; **(c)** no machine at all — the addition is declared in the
   caller's own addition document as prose, and the guard reads that. **`E6` must be answered
   first for whichever is chosen: what decision changes if the declaration is absent?** If the
   honest answer is *none*, (c) wins by that rule.
3. **How does the split membership rule read?** One sentence naming harness members and a second
   naming the mechanism for additions — or something else. This is the sentence the round exists to
   change, and changing it is why the round is design.
4. **Which route do the contract's provenance blocks take?** Removing pure history does not change
   what the contract requires, which is a different class from the two in-place corrections round
   `V1-RESULT-RETIRE` obtained rulings for. **Whether that difference earns a lighter route is the
   user's**, and the round must ask rather than assume.
5. **Where does the product run happen and who builds it?** Ruling 3 makes it acceptance; the
   2026-08-23 ruling puts it in a caller repository. Which repository, and whether it is a scratch
   one or a real piece of work, is unanswered.
6. **How is the batch cut into rounds?** The rule split, the code split, the contract, and the
   product run are plausibly four; nothing here fixes that.

## Out of scope

- OUT: the candidate-isolation design question (queue ③, still unruled).
- OUT: `dispatch-economy` (queue ④).
- OUT: declaring `HD-66`'s plugin trigger fired. This batch is that entry's option two; failure is
  evidence toward the plugin, and the declaration stays the user's.
- OUT: sparse-checkout as a substitute — it materialises fewer files and makes no reference resolve.
- OUT: repairing the 14 sites that fail on the full repository. Repairing them breaks the rule they
  satisfy.

## Sketch of the work — not a decomposition; the executor writes its own

- **A — the rule split.** The checklist divides along the 26/10 line measured above. The five
  product documents' 11 path references and 36 code citations follow whichever names result.
- **B — the membership rule and its guard.** The sentence per question 3; `layer_path_check.py`'s
  `LAYER` and `sweep_refs.py` both import from it rather than being edited in parallel, so they
  follow.
- **C — the code split.** `dispatch.py`'s three construction modes, `cli.py`'s branches, and both
  hard-coded constants. `CONSTRUCTION-INDEX.md`'s tier table changes with every one, row 8 included.
- **D — the stubs.** Removable once no dispatch prompt names them (ruling 6's condition); that
  frees `dispatch.py:549` and three hand-written test constants.
- **E — the contract.** The two provenance blocks, under whatever question 4 rules. §12's third
  paragraph stays.
- **F — the product run.** Ruling 3's acceptance, in a caller repository.
- **G — riders.** `checklist-cited-not-carried` redeemed; `onboarding-carries-construction` checked
  for whether it redeems with it.

## Acceptance (done = ?)

1. A harness-only tree, built by `git archive` and made a git repository, reports **zero**
   non-resolving sites naming an instrument-held artifact. Caller-held bare names are reported
   **separately and still present** — collapsing the two classes is how this defect hid.
2. `python tooling/sweep_refs.py` on both trees, output pasted.
3. On that tree: `dtw --help` exit 0 · `dtw init` into a fresh repository exit 0 · the caller-side
   guards exit 0.
4. **A real product run completes on that tree** (ruling 3): a run directory built, an instruction
   frozen, a reviewer dispatched from the mounted harness, a verdict recorded, the run closed.
   Which repository it runs in is question 5's.
5. `grep -rn 'CONSTRUCTION-CHECKLIST' <harness tree>` returns nothing, or only what a ruling
   admitted, each accounted for in a commit body.
6. No file in the harness tree holds a construction-only code path; `dispatch.py`'s and `cli.py`'s
   line counts re-measured either side of the split.
7. `python -m pytest tooling/tests -q` green on the full repository, delta accounted.
8. `CONSTRUCTION-INDEX.md` re-measured by its own commands, and row 8's prose agreeing with its
   count.
9. The guards exit 0 and the membership rule resolves N/N for whatever N it ends up naming, on
   **both** trees.
10. Rider `checklist-cited-not-carried` deleted in the commit that earns it.

## Resume pointer

当前指针: **not opened.** The six open questions go to the user first; question 2 is the one ruling
7 deliberately left for that moment, and question 5 gates acceptance 4.

## Notes

- **Why the A/B/C framing died.** It asked which repair to buy. The user asked a different question
  — what the construction side *is* — and answered it: an instance of the harness applied to
  itself. Repairs follow from that; they do not substitute for it.
- **Why the 14 full-repository sites stay.** The rule requires a caller-held artifact be named
  rather than pathed. A round that "fixes" them breaks the rule it thinks it serves. The number
  looks like a defect and is not one, which is exactly why it is written down.
- **What this batch is evidence for.** `HD-66` made the distribution form conditional on core
  distribution being shown impossible. This is the attempt. Neither its success nor its failure is
  this file's to declare.
