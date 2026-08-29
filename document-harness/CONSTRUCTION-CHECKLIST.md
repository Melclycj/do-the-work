# Construction checklist — building or changing the harness itself

> **Split 2026-08-30, round `CORE-ONLY-LAYER`.** The rules both sides obey moved to
> [RULES.md](RULES.md) beside this file, keeping their identifiers and their bytes; what stays
> here is what only this instrument obeys. **Read this file and the counterpart it names** —
> a construction session dispatched with this file as its charter answers to both, and the
> `E*` / `R*` identifiers cited anywhere resolve there unless they appear below. This file is
> not an instruction-layer member any more: it is this repository's own rule file, declared
> under `rules` in the `harness.json` at this repository's root, and it binds this repository
> alone.
>
> Compressed 2026-07-27 from the two operating contracts
> (`../migration/document-work-assurance-v3/v3-harness-{operating,review}-contract.md`, now
> stubs; full text at `7011916`) — Phase A of
> `document-harness/plans/harness-deletion-first-stabilization.plan.md`. Like any instruction-layer
> amendment (E10), relied on only after an independent read.
>
> **This file is the operative rule set for what only this instrument obeys, not a complete
> replacement.** Where it is silent on a
> question a round actually faces, the retired contracts at `7011916` are the reference of
> record; the silence is not a defect, and closing it rides the next batch under R9 rather than
> opening a round.
>
> **Where a cited commit id resolves.** A commit id cited in this file or in any other
> instruction-layer member (`E10`) that this repository does not have — `7011916` included —
> is a commit of the repository this one was extracted from;
> [`CONSTRUCTION-LEDGER.md`](../CONSTRUCTION-LEDGER.md)'s header block *Where the bytes came
> from* names that repository — as a single-machine worktree path, so it identifies that
> repository without making it reachable from here. A citation naming its own repository
> **by name** is read as
> written; a role word — *caller*, *instrument* — is not such a name and routes like
> silence, by the first sentence's test, so `EXECUTION.md`'s "caller `6fd0ae3`" reaches the
> extraction-source repository for every reader, not whichever repository is reading; a
> silent one means that one.
>
> Rationale is deliberately absent: every rule below was paid for by a recorded incident, and
> the records — not this file — hold the stories (`git log` on the two superseded contracts;
> `../migration/document-work-assurance-v3/v3-*.md`). Product runs are NOT governed here —
> they follow `EXECUTION.md` / `REVIEW.md`.

## Execution side — any session changing harness code, schemas, or instruction files, whether it orchestrates the round or executes it

- **E2** The announced paths **may be written, and a write to them is disclosed after the
  fact rather than authorised before it** (user ruling 2026-08-27, which ended this clause's
  gate): the commit that writes one **names, in its own body, the full repo-relative path of
  every announced file it changed**, site by site, and that body is what the independent
  review reads, so the disclosure already sits where the review looks and owes no second
  carrier. The list is exactly this:
  `contract/Document-Work-Assurance-Contract-v4.md`, and every file the
  `schema/document-assurance-v3/` pack held
  at the 2026-08-03 re-baseline (fifteen files: the fourteen of the 2026-07-29 entry plus
  `schema/document-assurance-v3/paragraph-map.schema.json`, which joined
  2026-07-31 and which the 保障面二期复盘 found sitting outside the freeze); a pack file
  added after that date is not announced by this rule until a later re-baseline — new schemas
  stabilize first, which is why this clause re-baselines rather than auto-enrolling.
  One path and one directory, both decidable by inspection, so nothing
  has to decide what *signed* means or which schemas N0 named; **a path outside them is not
  announced by this rule**, and this harness does not claim to watch instruments it does not
  govern. No blob hash is pinned here — what was signed is `CONTRACT-V4-SIGNATURE.md`'s to
  record, and a hash written here too is a second copy needing a hand edit on every
  legitimate write. **What the disclosure is worth, and what it is not:** that a body names
  a path is mechanically decidable, and being decidable is the whole of what it certifies —
  it says nothing about whether what the body says about that path is true, or whether the
  write should have happened at all. Those stay the independent review's to judge, and this
  clause buys the review a place to start rather than a verdict. *Frozen*, and *the frozen
  surface*, are the older names for this same set — a name for which paths these are, never a
  prohibition, now that the gate has ended — and are still what the riders, the decision log
  and the round records call it. A boundary declared
  anywhere else — a plan's freeze surface, a round's own card — is derived from this rule
  and never independently authoritative.

## Review side — the independent session a dispatch reaches

- **R6 — this repository's own review-records directory** is
  `migration/document-work-assurance-v3/`, which is what its `.harness/scan-surfaces.json`
  declares under `review_record_dirs` and where the four `v3-*` record families land. `R6`
  itself is in the counterpart named above; this is the value it reads here, written down
  because the counterpart may not name a directory only this repository has.
