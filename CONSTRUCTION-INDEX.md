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
> **The gap that made the product tier an open set is closed, and the closure is measured rather
> than asserted.** Until round `CORE-ONLY-LAYER` all five product-tier role documents pointed at
> the construction checklist, which does not travel — 6 pointers plus 35 backticked `E1`–`E12` /
> `R1`–`R10` citations over 26 lines, measured 2026-08-26 — so on a tree carrying the product tier
> alone they reached nothing. The rules both sides obey now travel as `document-harness/RULES.md`,
> product-tier row 3, and what stays below is only what this instrument obeys alone. Re-measured
> at `cbaee8e` over the same five documents: **0** pointers to the checklist, and **39** rule
> citations over **31** lines of which every one resolves to a rule in `RULES.md` — the fortieth
> hit is `EXECUTION.md`'s `R0`, a product run's own requirement number and not a rule. Rider
> `checklist-cited-not-carried` is redeemed and its row is gone.

## Product-run tier — what a caller mounts

Nothing outside these rows travels, and since round `CORE-MOUNT` the rows have a machine-readable
twin: row 9's `document-harness/product-tier.txt` holds one *Where* token per line, travels with
the tier, and is what a caller feeds to `git sparse-checkout` to materialize this tier and nothing
else (`document-harness/ONBOARDING.md` item 1b). The two copies are held equal by
`tooling/tests/document_harness/test_product_tier_manifest.py`, which parses the *Where* column
below and compares it with that file, so a *Where* cell edited here without the manifest — or the
reverse — turns red. The *Files* column is not guarded and is a measurement, not a definition.

**61 files** against a repository of **443**, measured 2026-09-03 on the tree this commit creates,
by the commands at the foot — re-run them rather than citing these, because a count is invalidated
by the next commit (`E3`). No tip SHA is written for the same reason `E12` gives about a recorded
range: writing these figures is itself the commit they are measured on, so a SHA here would name
the commit before them. Where the movement since the 2026-08-30 measurement at `8ce93f7` came
from, measured by `git diff --diff-filter=A --name-only 8ce93f7..` before this commit: **20 files
added and none deleted**, 421 → 441 — 10 review and read records, 4 journals, 2 plans, 3 test
files, and one schema, `bind-declarations.schema.json`, which joined the pack in round
`PROMISE-PATH-ENGINE` (2026-09-02) and is why row 2 reads **15** where it read 14. This commit
adds the other two: the row-9 manifest, which is in the tier, and the test that binds it, which
is not.

| # | What travels | Where | Files |
|---|---|---|---|
| 1 | The operative contract; `E2` freezes its bytes | `contract/Document-Work-Assurance-Contract-v4.md` | 1 |
| 2 | Every schema a run validates against; `E2` freezes the fifteen the pack held at the 2026-08-03 re-baseline, a dated snapshot the pack no longer equals, and `paragraph-map.schema.json` is also an instruction-layer member | `schema/document-assurance-v3/` | 15 |
| 3 | The rules every session answers to, the navigation surface, and the three role charters — executor, reviewer, orchestrator; instruction-layer members | `document-harness/RULES.md` · `document-harness/README.md` · `document-harness/EXECUTION.md` · `document-harness/REVIEW.md` · `document-harness/ORCHESTRATION.md` | 5 |
| 4 | Onboarding, needed once and before anything else works; not a member, and it says so | `document-harness/ONBOARDING.md` | 1 |
| 5 | The decision log and rider bank a caller gets verbatim from `dtw init`; the decision log's own header is where the log's rules live (`HD-19`) | `document-harness/templates/` | 2 |
| 6 | The CLI entry points | `tooling/dtw.py` · `tooling/do-the-work.py` | 2 |
| 7 | The engine — checks, review, dispatch, init, preview, candidate and spec handling | `tooling/rsclib/document_harness/` | 22 |
| 8 | The three tracked pre-commit guards and the package marker they are called through — which of them a repository wires is its own choice, and `document-harness/README.md`'s *Local enforcement* row is the single home of that division of labour — and the run template a run is copied from | `tooling/hooks/` · `assurance/templates/run-v2/` | 4 + 8 |
| 9 | This table's *Where* column, one token per line and self-including — what the tier is measured by and what a core-only mount's `git sparse-checkout` reads, so a caller can redo the step from the mount alone after a gitlink bump without reading this file | `document-harness/product-tier.txt` | 1 |

## Construction-side tier — what stays here

| What | Where |
|---|---|
| This repository's own rule file — what only this instrument obeys, `E2` and one instance value, on top of the harness's own `document-harness/RULES.md`. Since round `CORE-ONLY-LAYER` it is **not** an instruction-layer member: it is declared under `rules` in [harness.json](harness.json) at this root and binds this repository alone | [CONSTRUCTION-CHECKLIST.md](document-harness/CONSTRUCTION-CHECKLIST.md) |
| Contract v4's signature record — the exact signed blob and date; successor to `HD-56` since 2026-08-26 | [CONTRACT-V4-SIGNATURE.md](CONTRACT-V4-SIGNATURE.md) |
| Decision log — supreme source of truth for user rulings; instruction text expands under it, and on conflict the instruction text is what is wrong. **This instrument's own log, and only this one:** every round's opening MUST read its `§live` (and only `§live`), waiver of the layer's cold read or not, and a plan author reads all live entries and inherits them **verbatim**, never by transcription. The mechanism lives in the log's own header, which ships as the template in product-tier row 5 (`HD-19`). A caller keeps its own at its own root and reads that one | [HARNESS-DECISIONS.md](HARNESS-DECISIONS.md), dead entries read-only beside it in [HARNESS-DECISIONS-archive.md](HARNESS-DECISIONS-archive.md) |
| Rider bank — banked findings, redeemed on touch | [HARNESS-RIDERS.md](HARNESS-RIDERS.md) |
| Construction ledger — the pointer file for this instrument's own rounds (CLOSED / open / next queue head, and construction-side rulings with no other home) | [CONSTRUCTION-LEDGER.md](CONSTRUCTION-LEDGER.md), history read-only beside it in [CONSTRUCTION-LEDGER-archive.md](CONSTRUCTION-LEDGER-archive.md) |
| Construction-batch plans, including the v3 execution plan (user-approved 2026-07-20) | [plans/](document-harness/plans/document-work-assurance-harness-v3.plan.md), moved into this repository from the caller 2026-08-19 |
| Journals — construction narrative **or cross-round design judgment**: analysis, reasoning and measurement only (narrowed 2026-08-08, `HD-1`). **Not bound to a round (user ruling 2026-08-28)**: a journal may be written whenever detail needs a home — mid-round, between rounds, or before one opens — and it is the default landing place for reasoning that must not be compressed into the ledger, which takes pointers only. Historically one file per round, and since 2026-08-05 also one per design judgment spanning rounds; a ruling's *reasons* belong here, the ruling itself is a decision-log entry, and open items go to the rider bank or the plan backlog | [journal/](document-harness/journal/checker-and-map-2026-08-05.md), plus the earlier [migration/…/journal/](migration/document-work-assurance-v3/journal/reform-2026-07-29.md) |
| The N0 / N1 / N2 administrative records, the W2 and supersession-2 signature records, the review and read records, and the contract fixtures + runner (41/41 green) | [N0](migration/document-work-assurance-v3/N0/N0-record.md) · [N1](migration/document-work-assurance-v3/N1/N1-record.md) · [N2](migration/document-work-assurance-v3/N2/N2-record.md) · [fixtures](migration/document-work-assurance-v3/N0/fixtures/cases.json) · `migration/document-work-assurance-v3/` entire — the two retired-contract stubs that were the one exception were instruction-layer members until round `CORE-ONLY-CODE` deleted them |
| The I/O design, the split design, the travel manifest — construction-round deliverables; `io-design.md`'s own header says it is not a member and has authority over nothing | [io-design.md](document-harness/io-design.md) · [split-design.md](document-harness/split-design.md) · [split-travel-manifest.md](document-harness/split-travel-manifest.md) |
| The test suite, the reference sweep and the construction-side dispatch — instruments for changing this harness, run by its own rounds. The dispatch generator holds the three cold entries a round uses (a range review, an `E10` layer read, that round's executor); it was three modes of `dtw dispatch` until round `CORE-ONLY-CODE` moved it here, under acceptance 6's bound that no file a caller mounts holds a construction-only code path | `tooling/tests/` · [sweep_refs.py](tooling/sweep_refs.py) · [construction_dispatch.py](tooling/construction_dispatch.py) · `assurance/test/` · `assurance/review-test/` |
| This repository's own wiring and front door — a caller wires its own hook per-machine, as onboarding item 9 states, and writes its own entry file and declaration, as items 8 and 10 state | `.githooks/pre-commit` · `.github/workflows/` · [README.md](README.md) · `README.zh-CN.md` · `LICENSE` · `.gitignore` · [CLAUDE.md](CLAUDE.md) · [harness.json](harness.json) |
| This file | [CONSTRUCTION-INDEX.md](CONSTRUCTION-INDEX.md) |

## How to re-measure

```
git ls-files <each product-tier path> | wc -l        # files per row
git ls-files -- $(tr -d '\r' < document-harness/product-tier.txt) | wc -l   # the tier
git ls-files | wc -l                                 # the repository, for the ratio
```

The tier command reads row 9's manifest rather than a re-typed path list, so it cannot disagree
with what a caller's sparse checkout materializes. `tr -d '\r'` is not decoration: a checkout with
`core.autocrlf=true` gives that file CRLF endings, and while `git sparse-checkout --stdin` strips
the CR itself, a shell expanding the file into `git ls-files` arguments does not. Measured
2026-09-03 by handing `git ls-files --` the manifest's lines with a `\r` appended to each — the
shape a CRLF checkout produces — against the same lines stripped: **0** files matched against
**61**. The failure is silent, which is why the strip is written into the command rather than
left to the reader.

Counts only, deliberately: a worktree byte figure is not a function of the tree — line endings
differ per checkout — so use `git cat-file -s` if bytes are ever needed (rider `figure-units`).
