# Plan — round `STRANGER-GUARDS` (publicization batch C, first of two rounds)

> **Status: open.** Written 2026-08-23 at round open. This file is the carrier of the **four
> user rulings of 2026-08-23** below until the round records them; a cold session reads this
> file, then `CONSTRUCTION-LEDGER.md`'s current pointer, then works. Queue note: batch C
> (陌生人可用性) became the queue head when round `CONTRACT-V4` closed batch B
> (`V3-CONTRACT-V4-CLOSEOUT-v1`); the ledger's batch C entry lists six items, and ruling 1
> below slices them into two rounds, of which this is the first.
>
> **Role form — `HD-55` norm, no exception taken.** Orchestrator and executor are separate
> sessions; the opening layer read, the FULL, the fix leg and the VERIFY are each dispatched
> cold (`dtw dispatch` 出单), and `R1`'s four holdings stay with the orchestrator throughout.
> The orchestrator hand-edits no work product; its own commits are this plan, review records
> (`R6`), and the closeout.

## The four user rulings of 2026-08-23 (this file is their carrier)

1. **Batch C is sliced into two rounds.** First `STRANGER-GUARDS` (this round): the
   `chk-caller-prefixes` design question, `amend-exempt-caller`, and the ten remaining
   resolution points. Then `STRANGER-PROOF` (own plan at its own open): the second-caller
   ONBOARDING proof and the audience-facing root README rewrite. Order is deadline-driven:
   `chk-caller-prefixes` and `amend-exempt-caller` both carry "the second caller" as their
   recorded deadline moment, so the guard and the layer text are fixed **before** the proof
   walk that would otherwise arrive exactly at those deadlines; the README rewrite consumes
   the proof walk's record as its quickstart material (commands over claims), so it can only
   follow.
2. **Rider `submod-index` is taken — the guard SHALL recognize submodule-internal paths.**
   The design question that row banks (should `candidate_path_check` /
   `TrackedPaths.from_index` see inside a mounted submodule, where `git ls-files` shows only
   a gitlink) is answered yes, in this round, which touches its redeem-when surface. Rider
   `decited-paths` depends on it: its caller-side broken-link texts (re-count at the
   redemption base — the recorded "ten" was stale when written) become fixable once the guard
   stops mis-blocking real submodule-internal paths; that fix lands **caller-side**, per the
   `mount-inert` precedent (跨仓兑付, row deletion and site fix per repository), and is out
   of this round's change boundary.
3. **The §10.5 pair is deferred to batch C closeout.** Distribution form (submodule vs
   plugin install) and whether `.claude/` should carry harness files are ruled **after** the
   `STRANGER-PROOF` walk, with that walk as evidence — the second-caller proof is itself an
   experiment in the current distribution form. Until then the ledger's batch C entry
   remains their home.
4. **The opening layer cold read is dispatched, not waived.** Contract v4 is a 339-line
   member with no prior end-to-end read to cite, and round `CONTRACT-V4`'s member edits
   (free-channel `f112135` included) owe their independent read — this opening read
   discharges both. The reader derives which members' blobs changed since their last
   recorded read from the records themselves (`E10`: citation depends on recorded blob ids).

## Why this round

Batch C buys "the first external caller does not crash on contact". Three banked riders pin
their deadlines to that caller's arrival: `chk-caller-prefixes` (its review records would be
scanned as work product, replaying the `freeze-audit` deadlock on a stranger),
`amend-exempt-caller` (the layer's own correction paragraph reads wrong for any repository
that is not the first caller), and the `submod-index`/`decited-paths` chain (the guard
mis-blocks real submodule-internal paths, inviting `--no-verify`). The ten resolution points
are the same class one layer down: defaults that only resolve on the first caller's layout.

## Opening measurements (orchestrator session, base `1bce371` — `E3`)

- `tooling/hooks/candidate_path_check.py:68-89`: `RECORD_SURFACE` is nine hardcoded entries,
  eight of them prefixed `ResearchSystem/…` plus `.goals/LEDGER*.md`;
  `SPECIFICATION_SURFACE` is the single hardcoded entry `ResearchSystem/assurance/runs/`.
  These are the first caller's directory names, not this repository's own (its records live
  at `migration/…`, `document-harness/journal/…`, and root-level ledgers).
- `tooling/rsclib/document_harness/cli.py`: six sites of
  `pathlib.Path(args.repo_root).resolve() if args.repo_root else pathlib.Path.cwd().resolve()`
  at `:45 :82 :152 :359 :444 :492` (the ledger's recorded line numbers have drifted; the
  count of six holds). The run-v2 template scripts' `parents[3]` defaults are the other six
  points; the two that bit on contact were already fixed by round `TEMPLATE-LIB-ROOT`.
- Root `README.md:17` names `D:/Thesis` (a single-machine path) as the history terminus;
  the ledger records the caller's branch was pushed to a public repository, so a reachable
  terminus exists to point at (rider `amend-exempt-caller`'s second half, `R5` — proposal
  below, user ratifies at the fix gate or earlier).

## Change surface

| surface | what changes |
|---|---|
| `tooling/hooks/candidate_path_check.py` | `chk-caller-prefixes`: the two hardcoded surface constants become caller-declarable, with the current entries surviving as the first caller's declaration, not as universal truth. Proposed direction (candidate's to finalize, FULL reviews): a caller-side declaration under `.harness/` written by `dtw init` with sane defaults, read by the guard; a caller with no declaration gets defaults that at least cover its own `dtw init` layout. Also the `submod-index` fix if its natural seam lies here rather than in `paths.py`. |
| `tooling/rsclib/document_harness/paths.py` | `submod-index` (ruling 2): `TrackedPaths.from_index` sees submodule-internal paths — a path under a gitlink that `git -C <submodule> ls-files` confirms is not "resolves nowhere". |
| `tooling/rsclib/document_harness/cli.py` | The six cwd defaults stop silently mis-resolving: either correct discovery (git toplevel of cwd) or loud refusal — never a wrong root taken quietly. |
| run-v2 template scripts (six) | Same treatment for the `parents[3]` repo-root defaults (library imports are already `__file__`-relative since `TEMPLATE-LIB-ROOT`; this is the git-target half only). |
| `document-harness/CONSTRUCTION-CHECKLIST.md` (member) | `amend-exempt-caller` first half: the correction paragraph's closing exemption sentence stops reading role-annotated citations (`EXECUTION.md`'s "caller `6fd0ae3`") backwards for a second caller — the paragraph's own first sentence already routes them. Member edit; owes its independent read at the next opening. |
| `document-harness/EXECUTION.md` (member, only if needed) | The `:387-388` role annotation site, if the checklist-side fix alone leaves it ambiguous. |
| Root `README.md` | `amend-exempt-caller` second half (`R5`): the *Where the bytes came from* terminus gains the reachable name (the public repository the caller's branch was pushed to) beside the historical single-machine path, which stays as recorded history. |
| `tooling/tests/…` | New tests pinning the defect classes, not the instances (`E7`): guard reads a caller declaration / falls back sanely; submodule-internal path accepted, resolve-nowhere still blocked (negative control); cli root default loud-or-correct. Subprocess form where in-process green is how the class hides (precedent `TEMPLATE-LIB-ROOT`); mutation per `E4`. |
| `HARNESS-RIDERS.md` | Delete `chk-caller-prefixes`, `submod-index`, `amend-exempt-caller` in the same commit as their fixes (`R10`). `decited-paths`: touch note here; its deletion rides the caller-side fix commit (per-repo redemption, ruling 2). |
| `CONSTRUCTION-LEDGER.md` | At closeout only (orchestrator's, not the candidate's). |

**Out of boundary, deliberately:** `E2`'s sixteen frozen files; the `E10` membership
sentence (untouched → no `E10-sync` due); the second-caller proof and the audience README
(round `STRANGER-PROOF`); the §10.5 pair (ruling 3); the caller-side `decited-paths` sites
(cross-repo, after this round); any `git push` (`E8`).

## Expectations the FULL can hold the candidate to

- Battery green at the candidate revision, new tests included, with mutation evidence and
  negative controls (`E4`) — the guard seen to fail before it is trusted.
- After the change, no load-bearing hardcoded first-caller name decides what the guard
  scans for a caller that declared otherwise; the class is scanned (`HD-41` ④, grep output
  in the commit body), not just the two named constants.
- No cli or template invocation resolves a wrong repository root silently: each of the
  twelve sites either discovers correctly or refuses loudly, and a test distinguishes the
  two.
- Rider rows deleted in the same commit as their fixes; member edits enumerated in the
  commit body for the next opening read; candidate body carries kind, `E1` disclosure,
  `HD-41` class-scan output, and re-run measurements (`E3`).
