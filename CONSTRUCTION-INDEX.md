# CONSTRUCTION INDEX — what travels, what stays, and where the construction material lives

> **What this is.** One inventory in two tiers: the **product-run tier**, what a repository copies
> when it mounts this instrument, and the **construction-side tier**, everything else, which a
> caller neither carries nor depends on. Rows give the files and where they are; why the split is
> a list rather than a directory prefix is argued once in
> [core-set.plan.md](document-harness/plans/core-set.plan.md), rulings 11 and 19.
>
> **Not an instruction-layer member** — `E10`'s membership sentence does not name this file — and
> it claims authority over nothing: every rule a row mentions belongs to the file the row points
> at, and where the two disagree, that file governs. (`HD-21`'s question, answered by the round
> that created this file.)
>
> **The product tier is not a closed set, and the gap is measured rather than implied.** All five
> product-tier role documents cite the construction checklist, which stays below: **6 pointers**
> plus **35** backticked `E1`–`E12` / `R1`–`R10` citations over **26 lines**, measured 2026-08-26.
> On a tree carrying the product tier alone they reach nothing. Every way out is design, so no
> round of batch `CORE-SET` settles it; it is banked as rider `checklist-cited-not-carried`.

## Product-run tier — what a caller mounts

Nothing outside these rows travels. **59 files** against a repository of **391**, measured
2026-08-26 by the commands at the foot — re-run them rather than citing these.

| # | What travels | Where | Files |
|---|---|---|---|
| 1 | The operative contract; `E2` freezes its bytes | `contract/Document-Work-Assurance-Contract-v4.md` | 1 |
| 2 | Every schema a run validates against; `E2` freezes all fifteen, and `paragraph-map.schema.json` is also an instruction-layer member | `schema/document-assurance-v3/` | 15 |
| 3 | The navigation surface plus the three role charters — executor, reviewer, orchestrator; instruction-layer members | `document-harness/README.md` · `EXECUTION.md` · `REVIEW.md` · `ORCHESTRATION.md` | 4 |
| 4 | Onboarding, needed once and before anything else works; not a member, and it says so | `document-harness/ONBOARDING.md` | 1 |
| 5 | The decision log and rider bank a caller gets verbatim from `dtw init`; the decision log's own header is where the log's rules live (`HD-19`) | `document-harness/templates/` | 2 |
| 6 | The CLI entry points | `tooling/dtw.py` · `tooling/do-the-work.py` | 2 |
| 7 | The engine — checks, review, dispatch, init, preview, candidate and spec handling | `tooling/rsclib/document_harness/` | 22 |
| 8 | The two caller-side guards a caller wires into its own `pre-commit`, and the run template a run is copied from | `tooling/hooks/` · `assurance/templates/run-v2/` | 4 + 8 |

## Construction-side tier — what stays here

| What | Where |
|---|---|
| Construction checklist — `E1`–`E12` execution, `R1`–`R10` review, for *changing* the harness; an instruction-layer member that still does not travel | [CONSTRUCTION-CHECKLIST.md](document-harness/CONSTRUCTION-CHECKLIST.md) |
| The two retired operating contracts — stubs pointing at the checklist, members for the same construction-side reason | [operating](migration/document-work-assurance-v3/v3-harness-operating-contract.md) · [review](migration/document-work-assurance-v3/v3-harness-review-contract.md) |
| Contract v4's signature record — the exact signed blob and date; successor to `HD-56` since 2026-08-26 | [CONTRACT-V4-SIGNATURE.md](CONTRACT-V4-SIGNATURE.md) |
| Decision log — supreme source of truth for user rulings; instruction text expands under it, and on conflict the instruction text is what is wrong. **This instrument's own log, and only this one:** every round's opening MUST read its `§live` (and only `§live`), waiver of the layer's cold read or not, and a plan author reads all live entries and inherits them **verbatim**, never by transcription. The mechanism lives in the log's own header, which ships as the template in product-tier row 5 (`HD-19`). A caller keeps its own at its own root and reads that one | [HARNESS-DECISIONS.md](HARNESS-DECISIONS.md), dead entries read-only beside it in [HARNESS-DECISIONS-archive.md](HARNESS-DECISIONS-archive.md) |
| Rider bank — banked findings, redeemed on touch | [HARNESS-RIDERS.md](HARNESS-RIDERS.md) |
| Construction ledger — the pointer file for this instrument's own rounds (CLOSED / open / next queue head, and construction-side rulings with no other home) | [CONSTRUCTION-LEDGER.md](CONSTRUCTION-LEDGER.md), history read-only beside it in [CONSTRUCTION-LEDGER-archive.md](CONSTRUCTION-LEDGER-archive.md) |
| Construction-batch plans, including the v3 execution plan (user-approved 2026-07-20) | [plans/](document-harness/plans/document-work-assurance-harness-v3.plan.md), moved into this repository from the caller 2026-08-19 |
| Journals — construction narrative **or cross-round design judgment**: analysis, reasoning and measurement only (narrowed 2026-08-08, `HD-1`). **Not bound to a round (user ruling 2026-08-28)**: a journal may be written whenever detail needs a home — mid-round, between rounds, or before one opens — and it is the default landing place for reasoning that must not be compressed into the ledger, which takes pointers only. Historically one file per round, and since 2026-08-05 also one per design judgment spanning rounds; a ruling's *reasons* belong here, the ruling itself is a decision-log entry, and open items go to the rider bank or the plan backlog | [journal/](document-harness/journal/checker-and-map-2026-08-05.md), plus the earlier [migration/…/journal/](migration/document-work-assurance-v3/journal/reform-2026-07-29.md) |
| The N0 / N1 / N2 administrative records, the W2 and supersession-2 signature records, the review and read records, and the contract fixtures + runner (41/41 green) | [N0](migration/document-work-assurance-v3/N0/N0-record.md) · [N1](migration/document-work-assurance-v3/N1/N1-record.md) · [N2](migration/document-work-assurance-v3/N2/N2-record.md) · [fixtures](migration/document-work-assurance-v3/N0/fixtures/cases.json) · the rest of `migration/document-work-assurance-v3/` apart from the two stubs above |
| The I/O design, the split design, the travel manifest — construction-round deliverables; `io-design.md`'s own header says it is not a member and has authority over nothing | [io-design.md](document-harness/io-design.md) · [split-design.md](document-harness/split-design.md) · [split-travel-manifest.md](document-harness/split-travel-manifest.md) |
| The test suite and the reference sweep — instruments for changing this harness, run by its own rounds | `tooling/tests/` · [sweep_refs.py](tooling/sweep_refs.py) · `assurance/test/` · `assurance/review-test/` |
| This repository's own wiring and front door — a caller wires its own hook per-machine, as onboarding item 9 states, and writes its own entry file and declaration, as items 8 and 10 state | `.githooks/pre-commit` · `.github/workflows/` · [README.md](README.md) · `README.zh-CN.md` · `LICENSE` · `.gitignore` · [CLAUDE.md](CLAUDE.md) · [harness.json](harness.json) |
| This file | [CONSTRUCTION-INDEX.md](CONSTRUCTION-INDEX.md) |

## How to re-measure

```
git ls-files <each product-tier path> | wc -l        # files per row
git ls-files <the product-tier paths together> | wc -l   # the tier
git ls-files | wc -l                                 # the repository, for the ratio
```

Counts only, deliberately: a worktree byte figure is not a function of the tree — line endings
differ per checkout — so use `git cat-file -s` if bytes are ever needed (rider `figure-units`).
