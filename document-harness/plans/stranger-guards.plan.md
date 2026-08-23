# Plan — round `STRANGER-GUARDS` (publicization batch C, first of two rounds)

> **Status: executed — round CLOSED 2026-08-23.** All three `E9` legs walked: FULL `c2e955b`
> `REVIEWED_NO_BLOCKER` (2 lows) → the one user-approved fix `54f7fa7` (Low-1 trailing-slash
> normalization + README terminus per the user's rejection of the request-access proposal) →
> VERIFY `REVIEWED_NO_BLOCKER` (2 observations, record `v3-review-verify-53ec1a6.md`).
> Registers `53ec1a6` (`HD-44` correction, ledger private-repo correction, `HD-57` entry);
> the `HD-57` byte-application batch follows closeout. Records
> `v3-{cold-read-cf54a79,review-full-c2e955b,review-verify-53ec1a6}.md`; journal
> `stranger-guards-2026-08-23.md`.
>
> Originally: **Status: open.** Written 2026-08-23 at round open. This file is the carrier of the **four
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

## Fix-gate rulings of 2026-08-23 (after FULL `c2e955b`, record `18bb2bf` — this section is their carrier)

The FULL returned `REVIEWED_NO_BLOCKER` with two lows; per `R10` the spend-or-bank choice
on each, plus the pending register questions, went to the user, who ruled five things:

1. **The fix leg is approved** (`E9`'s one user-approved fix, a late activation after a
   no-blocker FULL — it still obliges the targeted VERIFY). Boundary, exactly two items,
   nothing else: **(a)** FULL Low-1 — trailing-slash normalization where the record /
   specification surface groups build their matching, so both guards read one declaration
   one way, plus the must-fire test the finding names; **(b)** the README terminus — the
   user **rejected** the request-access proposal ("不写，thesis 就是 private"): the
   `github.com/Melclycj/Thesis-Work` URL and the "durable address to request access"
   sentence are removed; the terminus returns to the single-machine historical form
   (`D:/Thesis`, worktree, commit — recorded history), with at most one plain clause that
   the caller's repository is private and its history is not publicly reachable. No door
   is offered, closed or otherwise.
2. **FULL Low-2 takes no code change.** The dispatch-range lesson (subject base = the last
   reviewed tip, so bookkeeping commits are covered rather than excluded; riders-only
   commits land after the candidate) is recorded in the closeout ledger entry and the
   round journal; this round's own VERIFY dispatch already applies it (base `c2e955b`).
3. **`HD-44` correction lands** (user: 落) — the consequence line's eighteen becomes
   sixteen with a dated note, and the ledger's repetition of the signature commit's
   unperformed-edit claim is corrected in the same act. Register class (decision log is
   the user's register, orchestrator lands the ruled edit; ledger correction per the
   2026-08-03 ledger-batch ruling), outside the fix boundary, landed before the VERIFY
   dispatch so it falls inside the reviewed range (the 2026-08-04 ruling's condition).
4. **The ledger's "public 仓" sentence is corrected** (user: 改) — the caller repository
   measured private on 2026-08-23 (anonymous API 404, anonymous `ls-remote` challenged);
   same register commit.
5. **The `E2` stale-literal class may be fixed** (user: 可以改) — one recorded ruling
   covering the five sites: contract v4's §5 Verification-mode row, v4's plan-digest
   provenance sentence, the two WorkSpec schema titles (rider `wspec-owner`), and
   `harness-issue.schema.json`'s `observed_after` gloss (rider `hi-schema-gloss`). The
   ruling enters the decision log in the same register commit as ruling 3; the **byte
   application is scheduled after this round's closeout** as its own reported application
   batch — rider rows (`v4-verifmode`, `v4-plan-digest`, `wspec-owner`,
   `hi-schema-gloss`) redeem in that commit, the `E2` clause's v4 blob literal updates in
   the same act, and the member edits owe their independent read at the next opening
   (`STRANGER-PROOF`'s cold read).

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
