# CORE SET — what a repository has to carry to run this instrument, and what it does not

> **Why an explicit list.** Directory is not the boundary and measurement rules it out:
> `document-harness/` holds five product-facing role documents beside a construction checklist,
> the construction-batch plans and the journals; `tooling/` holds the engine beside its test
> suite; `migration/` holds two instruction-layer members beside two hundred construction
> records. No prefix separates the two sides, so the two sides are listed.
>
> **What it is not.** Not an instruction-layer member. `E10`'s membership sentence in
> `document-harness/CONSTRUCTION-CHECKLIST.md` names the members and does not name this file,
> and this file claims authority over nothing: it says which files travel, and every rule about
> what those files *require* belongs to the file that states it. The product tier below is
> deliberately **not** the `E10` member set — `E10` governs the amendment machinery, which is a
> construction-side question, not what a caller has to carry. Two members sit outside the
> product tier for that reason, and one non-member sits inside it.
>
> **Both tiers are measurements, and they go stale.** Re-run the commands rather than citing
> the figures.

## Product-run tier — what a caller mounts

A repository that mounts this instrument needs these and nothing else to open, run and close a
round. Eight entries, **59 files, 0.730 MB**, measured 2026-08-26 at round `CORE-SET-LAYER`
against a repository of 386 tracked files and 6.33 MB (`git ls-files` scope, summed `stat -c%s`).

| # | What travels | Why it has to |
|---|---|---|
| 1 | `contract/Document-Work-Assurance-Contract-v4.md` (1 file) | The operative contract: one file merging the signed v3 contract and both signed supersessions. `E2` freezes its bytes |
| 2 | `schema/document-assurance-v3/` (15 files) | Every schema a run validates against, including `paragraph-map.schema.json`, which is also an instruction-layer member. `E2` freezes all fifteen |
| 3 | `document-harness/README.md` · `EXECUTION.md` · `REVIEW.md` · `ORCHESTRATION.md` (4 files) | The navigation surface plus the three role charters — executor, reviewer, orchestrator. Instruction-layer members, and the ones a product run is actually governed by |
| 4 | `document-harness/ONBOARDING.md` (1 file) | The nine items that take a repository from never having seen this harness to being able to open a round. Not a member and it says so; a caller needs it exactly once, and needs it before anything else works |
| 5 | `document-harness/templates/` (2 files) | The decision log and the rider bank a caller gets, verbatim, from `dtw init`. The decision log's own header is where the log's rules live (`HD-19`), so this template is the carrier of a rule, not a convenience |
| 6 | `tooling/dtw.py` · `tooling/do-the-work.py` (2 files) | The CLI entry points a caller invokes |
| 7 | `tooling/rsclib/document_harness/` (22 files) | The engine behind them — checks, review, dispatch, init, preview, candidate and spec handling |
| 8 | `tooling/hooks/` (4 files) + `assurance/templates/run-v2/` (8 files) | The two caller-side guards a caller wires into its own `pre-commit`, and the run template a run is copied from |

## Construction-side tier — what stays with this repository

Everything else. A caller does not carry it, and nothing a caller does depends on it.

| What | Where | Why it stays |
|---|---|---|
| The construction checklist | `document-harness/CONSTRUCTION-CHECKLIST.md` | `E1`–`E12` and `R1`–`R10` govern *changing* this harness. Its own header says product runs are not governed here. It is an instruction-layer member and still does not travel — which is the clearest case that the member set and this list are different questions |
| The two retired operating contracts | `migration/document-work-assurance-v3/v3-harness-{operating,review}-contract.md` | Stubs pointing at the checklist above, and members for the same construction-side reason |
| The I/O design, the split design, the travel manifest | `document-harness/io-design.md` · `split-design.md` · `split-travel-manifest.md` | Construction-round deliverables. `io-design.md` says so in its own header — a batch-B R2 deliverable, not a member, authority over nothing — so a caller should not have to carry a document that disclaims ownership of what it is cited for |
| Plans and journals | `document-harness/plans/` · `document-harness/journal/` | How this harness was built and why: analysis, reasoning, measurement |
| The migration records | `migration/document-work-assurance-v3/` apart from the two stubs | The N0–N4 administrative records, the review records, the read records, the fixtures |
| The three governance registers and their archives | `HARNESS-DECISIONS.md` · `HARNESS-DECISIONS-archive.md` · `HARNESS-RIDERS.md` · `CONSTRUCTION-LEDGER.md` · `CONSTRUCTION-LEDGER-archive.md` | This instrument's own rulings, banked findings and round pointer. A caller has its own decision log and rider bank, created by `dtw init` at its own root, and reads those — never these |
| The index over all of the above | `CONSTRUCTION-INDEX.md` | Navigation for the construction side; created alongside this file |
| This file | `CORE-SET.md` | It describes the split; it is not part of what travels |
| The test suite and the reference sweep | `tooling/tests/` · `tooling/sweep_refs.py` · `assurance/test/` · `assurance/review-test/` | Instruments for changing this harness, run by its own rounds |
| This repository's own wiring and front door | `.githooks/pre-commit` · `.github/workflows/` · `README.md` · `README.zh-CN.md` · `LICENSE` · `.gitignore` | A caller wires its own hook, per-machine, as onboarding item 9 states; the rest is this repository's own presentation |

## Two things the split deliberately does

**A member can sit outside the product tier.** Three do — the construction checklist and the
two retired-contract stubs. Membership decides whose bytes the amendment machinery in `E10`
governs; this list decides what a caller has to have on disk. Conflating them is what made the
question worth an explicit answer.

**A non-member can sit inside it.** `ONBOARDING.md` is not a member and carries no authority,
and a caller cannot get started without it.

## How to re-measure

```
git ls-files <each product-tier path> | wc -l        # file count per entry
git ls-files <each> | xargs stat -c%s | paste -sd+ | bc   # bytes per entry
git ls-files | wc -l                                 # the repository, for the ratio
```
