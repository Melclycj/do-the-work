# CONSTRUCTION INDEX — where this instrument's own construction history lives

> **What this is.** The navigation surface for the material that belongs to *building* this
> harness rather than to *running* it: the construction-batch plans, the node administrative
> records, the journals, the contract fixtures, and the three governance registers
> (decision log, rider bank, construction ledger). It holds pointers only — every row's
> target is the thing that speaks, and this file restates none of them.
>
> **Why it exists.** These nine rows sat in `document-harness/README.md`, which is a
> product-facing file a caller mounts. Each of them pointed out of the instruction layer
> and into this repository's own construction history, so a caller carrying only what it
> needs to run a round carried nine references to material it does not have. Batch
> `CORE-SET` moved them here (round `CORE-SET-LAYER`, 2026-08-26); the product-facing
> README keeps one row naming this file and nothing else.
>
> **What it is not.** Not an instruction-layer member — `E10`'s membership sentence names
> the members and does not name this one — and it claims authority over nothing: every rule
> a row mentions belongs to the file the row points at, and where this file and that file
> disagree, that file governs. It is an index, the same shape `document-harness/ONBOARDING.md`
> already occupies and states in its own header. The round that created it recorded that
> question and its answer, as `E10`'s tail requires; the record is in this round's commit
> bodies.
>
> **Which side it sits on.** The construction side of [CORE-SET.md](CORE-SET.md): a caller
> does not carry this file, and nothing a caller does depends on it.

| What | Where |
|---|---|
| Execution plan (user-approved 2026-07-20) | [v3 plan](document-harness/plans/document-work-assurance-harness-v3.plan.md) — with the other construction-batch plans in [plans/](document-harness/plans/), moved into this repository from the caller 2026-08-19 |
| N0 administrative record (approval + signature binding, reuse decisions, carried-forward residuals) | [N0-record.md](migration/document-work-assurance-v3/N0/N0-record.md) |
| N1 administrative record (vertical slice, reuse adaptation, residuals) | [N1-record.md](migration/document-work-assurance-v3/N1/N1-record.md) |
| N2 administrative record (review/repair/disposition, inherited residuals) | [N2-record.md](migration/document-work-assurance-v3/N2/N2-record.md) |
| Contract fixtures + runner | [fixtures](migration/document-work-assurance-v3/N0/fixtures/cases.json) (41/41 green) |
| Journals — construction narrative **or cross-round design judgment**: analysis, reasoning and measurement only (narrowed 2026-08-08, HD-1) | [journal/](document-harness/journal/checker-and-map-2026-08-05.md) under `document-harness/`, plus the earlier [migration/…/journal/](migration/document-work-assurance-v3/journal/reform-2026-07-29.md). One file per round, and since 2026-08-05 (SIMP-D1) also one per design judgment that spans rounds — a ruling's *reasons* belong here; the ruling itself is a decision-log entry, and open items go to the rider bank / plan backlog, not here |
| Decision log — supreme source of truth for user rulings; instruction text expands under it, and on conflict the instruction text is what is wrong | [HARNESS-DECISIONS.md](HARNESS-DECISIONS.md) — **this instrument's own log, and only this one.** A caller keeps its own at its own root and reads that one; the obligation the layer states is on whichever log belongs to the repository the round runs in — every round's opening MUST read its `§live` (and only `§live`), waiver of the layer's cold read or not, and a plan author reads all live entries and inherits them **verbatim**, never by transcription. The mechanism is in the log's own header, which ships as [templates/decision-log.md](document-harness/templates/decision-log.md) (`HD-19` — the rules of the log live there, not in the instruction layer); established 2026-08-08 (HD-1), earlier rulings stay where they already are |
| Rider bank (banked findings, redeemed on touch) | [HARNESS-RIDERS.md](HARNESS-RIDERS.md) |
| Construction ledger — the pointer file for this instrument's own rounds (CLOSED / open / construction-side rulings with no other home); the record side of the construction checklist (the *Construction-side rules* row of `document-harness/README.md`) | [CONSTRUCTION-LEDGER.md](CONSTRUCTION-LEDGER.md), history read-only beside it in [CONSTRUCTION-LEDGER-archive.md](CONSTRUCTION-LEDGER-archive.md). Both arrived from the caller 2026-08-19, the round that overturned `HD-28`'s "ledger 留调用者" half; a caller keeps its own separate account of *using* the instrument, and nothing of that kind enters here |
