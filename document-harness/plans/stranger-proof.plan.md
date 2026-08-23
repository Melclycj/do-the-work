# Plan — round `STRANGER-PROOF` (publicization batch C, second of two rounds)

> **Status: open.** Written 2026-08-24 at round open, on the user's word ("做 STRANGER-PROOF").
> The round's content was ruled at the batch C opening (2026-08-23, recorded in
> `stranger-guards.plan.md` ruling 1): the second-caller ONBOARDING proof and the
> audience-facing root README rewrite. The §10.5 pair (submodule-vs-plugin distribution,
> `.claude/` carriage) is ruled at **batch C closeout** with this round's walk as evidence —
> not in this round. A cold session reads this file, then `CONSTRUCTION-LEDGER.md`'s current
> pointer, then works.
>
> **Role form — `HD-55` norm under `E1` as amended 2026-08-24 (`1a0a200`).** Every dispatch
> this round — opening read, executor, FULL, fix leg, VERIFY — runs as its **own session**
> (`claude -p`), never as an in-process subagent: a subagent does not load the system config,
> so the forms are not equivalent. `R1`'s four holdings stay with the orchestrator; the
> orchestrator hand-edits no work product.

## What this round buys

The batch C promise unproven so far: that a repository which has never seen this harness can
follow the committed documentation and end up correctly wired — walked for real, not
asserted — and that a human stranger meeting the root README understands within the first
minute what this is, who it is for, and how to start. Round `STRANGER-GUARDS` fixed what
would have bitten that walk (hardcoded guard prefixes, root-resolution defaults); this round
performs the walk and turns its record into the README's quickstart.

## The two work items

1. **Second-caller proof.** The executor plays a second caller: create a fresh git
   repository in a directory outside this one (path recorded; layout unlike the first
   caller's — that is the point of the walk), then follow
   `document-harness/ONBOARDING.md`'s nine items **exactly as written**, in order, recording
   per item the command run, the pasted output (`E3`), and whether the item's own
   "how you see it took" check held. A local clone as the submodule source is acceptable
   (`CALLER-ONBOARDING` precedent); the pushed remote may be used if credentials allow.
   Deviations are findings, not silent adaptations: an item that does not work as written is
   recorded, and its fix (ONBOARDING.md is **not** an `E10` member) may land in the
   candidate with disclosure, or bank, by the usual routing. The walk record is a committed
   artifact: `document-harness/journal/stranger-proof-walk-2026-08-24.md`.
2. **Audience-facing root README rewrite.** The current root README opens agent-first (its
   own words: commands for agents). The rewrite gives the human stranger the first screen —
   what this instrument is, who it is for, what using it looks like, and a quickstart
   distilled from the walk record (real commands that were actually run, quoted from the
   walk — commands over claims). The agent-facing state table and its
   commands-over-claims rule stay; nothing true is deleted, and no claim is added that the
   walk did not measure. The terminus stays as ruled 2026-08-23 (private, no door offered).

## Honesty caps, declared up front

Same machine, and the walker is an agent, not a human stranger — this walk closes "the flow
works as documented on a second layout" and cannot close "a stranger on another machine
succeeds" (the `CALLER-ONBOARDING` caps stand; Windows long-path remains the standing
caveat). The record says so rather than overclaiming.

## Change surface

| surface | what changes |
|---|---|
| `document-harness/journal/stranger-proof-walk-2026-08-24.md` (new) | The walk record: nine items, each command + pasted output + check outcome; the fresh repo's path and layout; honesty caps. |
| Root `README.md` | Audience-first rewrite per item 2. |
| `document-harness/ONBOARDING.md` (conditional) | Only what the walk proves wrong as written, with disclosure; not a member, ordinary candidate surface. |
| `HARNESS-RIDERS.md` (conditional) | Any walk finding that banks; any row whose redeem-when this round touches. |
| `CONSTRUCTION-LEDGER.md` | At closeout only (orchestrator's) — including the stale "首跑等用户 push" note falsified by the measured three green CI runs of 2026-08-23. |

**Out of boundary, deliberately:** all nine `E10` members (the opening read covers the edits
owed from `STRANGER-GUARDS`, the `HD-57` application and the `E1` amendment — reading them
is the read's job, editing them is not this round's); `E2`'s sixteen frozen files; the
§10.5 pair (batch closeout); the caller-side `decited-paths` sites; any `git push` (`E8`).

## Expectations the FULL can hold the candidate to

- The walk record carries a pasted, re-runnable command per item — no item summarized from
  memory, no check outcome asserted without its output (`E3`).
- The fresh repository's wiring, as recorded, actually ends in the state ONBOARDING
  promises (hooks wired and seen to fire once, guards reachable, `dtw` commands resolving
  the second layout's root correctly — the surfaces `STRANGER-GUARDS` changed are exercised,
  not assumed).
- The README's quickstart quotes only commands the walk ran; the agent-facing table
  survives; no new unverified claim (the section's own rule).
- Rider rows touched in the same commit as their fixes; candidate body carries kind, `E1`
  disclosure, `HD-41` class-scan output where a finding is fixed, and re-run measurements.
