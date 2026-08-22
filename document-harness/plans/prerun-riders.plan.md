# Plan — round `PRERUN-RIDERS`

> **Status: executed — round CLOSED 2026-08-23.** Three legs full, all by independent
> sessions per `HD-55` (the round was itself the form's first exercise): cold read `3a6a10b`
> (0 must-fix) → FULL `7cb7213` `REVIEWED_NO_BLOCKER` (5 lows + 4 observations, the all-in
> fix `860729f` user-approved) → VERIFY `860729f` `REVIEWED_NO_BLOCKER` (its `V-1` banked as
> rider `hi-schema-gloss` — `E2`-frozen bytes wait for a recorded ruling). Ruling 5 was
> re-ruled within the day (word list untouched) — §5 below records both the initial ruling
> and the overturn. `HD-55` flipped implemented with its carrier. Records
> `v3-{cold-read-3a6a10b,review-full-7cb7213,review-verify-860729f}.md`; journal
> `prerun-riders-2026-08-22.md`.
>
> Originally: **Status: open.** Written 2026-08-22 at round open, after the opening cold read
> (`v3-cold-read-3a6a10b.md`, 0 must-fix / 0 low / 4 observations) landed at `ee3e05f`. This
> file is the carrier of the **seven user rulings of 2026-08-22** below until the round records
> them; a cold session reads this file, then `CONSTRUCTION-LEDGER.md`'s current pointer, then
> works. Queue note: the user approved inserting this round ahead of the re-rooting item's
> remaining ten resolution points (measured not to bite today; the first product run, which
> this round clears the path for, is imminent).
>
> **Role form — first round under `HD-55`.** Orchestrator and executor are separate sessions:
> the orchestrator (the session the user talks to) dispatched the opening read to an
> independent reader, dispatches the executor via `dtw dispatch --construction-executor`, and
> will dispatch FULL and VERIFY to independent reviewers. With the candidate authored by an
> independent executor and every review dispatched by the orchestrator, the executor holds
> **none** of `R1`'s four holdings — the candidate body states this in `15a53fe`'s disclosure
> form, adapted to the none-held case, and may for the first time state it as structural.

## Why this round

The first product run is approaching and seven text accounts fall due at its drafting, its
FULL, or its closeout. All seven were ruled by the user on 2026-08-22 in conversation; this
plan is where those rulings stop being chat-only. The round is **text-only**: after ruling 5's
re-ruling (below) no code, no schema and no test changes — the battery is expected to stay at
its base count, and the executor verifies that rather than assumes it.

## The seven user rulings of 2026-08-22 (this file is their carrier)

1. **`plan-delivery` — the governing plans ARE delivered; instruction-first priority.** The
   orchestrator's delivery (ORCHESTRATION.md, *Handing the executor its instruction*) gains
   the governing plans as a delivered item, alongside charter + instruction + subject. The
   user's ground, kept verbatim: 「留给开发自己规则的落脚点」— the plans are the caller's
   extension point for rules the instrument cannot know. **Bound, in the user's words:**
   「当现有的 instruction 无法承载的时候，就启用计划书」— what the instruction CAN carry
   (obligations, data, this-run demands) MUST go in the instruction and through the frozen,
   START-approved surface; the plans take only what the instruction cannot carry (conduct
   prose, which the 2026-08-01 ruling bars from instructions, and stage-standing discipline
   spanning runs). The plan channel is overflow, never a second instruction. The priority
   sentence's home is EXECUTION.md's authoring rules (it binds whoever writes instructions
   and plans); the delivery obligation's home is ORCHESTRATION.md's Handing section.
   Rider `plan-delivery` redeems by deletion.
2. **`chk-thin` — a thin check is a control-plane finding.** An obligation whose
   deterministic check decides almost nothing keeps its verdict untouched, and the thinness
   is reported as a finding against the check spec / WorkSpec — the exact mirror of the
   already-decided *`review_only` question* (script-decidable but declared review-only =
   control-plane finding). REVIEW.md's two sections (*What is not in the subject: the run's
   own checkers* and *`UNVERIFIABLE` is a real answer* — locate by heading, line numbers have
   drifted) are aligned to this one answer. Rider `chk-thin` redeems by deletion.
3. **`HI-route` — codify the existing practice.** A reviewer's out-of-scope observation is an
   observation finding in the review record — which is what every reviewer has in fact done
   (the rider bank's source column is made of exactly these). REVIEW.md's dangling
   `HarnessIssue` mention (its only occurrence, in *What is not in the subject*) is replaced
   by the explicit route: record it in your record's observations; at closeout the
   orchestrator routes it per the caller's policy (bank row, or a post-run `HarnessIssue`
   filed by an observer). No schema change, no deliverables change. Rider `HI-route` redeems
   by deletion.
4. **`status-key` — keep the ruling, add the discipline (re-asked, upheld).** No new machine
   (`E6`, upholding the 2026-08-10 ruling): `check_subject`'s CLOSED carve-out stays as it
   is. The compensating discipline is operational and named: **the orchestrator runs
   `dtw flow` against the run's state before dispatching a closeout subject**, so a mis-keyed
   commit is caught by the existing machine at the existing seam. The rider row is
   **rewritten, not deleted** — the machine-side gap remains by choice; the row carries the
   second upholding and the flow-command discipline, deadline unchanged (first real run's
   closeout).
5. **`mark-case` — re-ruled: the word list does not change.** The initial ruling of the same
   day (case-insensitive + word boundary) was **overturned by the user within the day** when
   the orchestrator surfaced `executor-charter.plan.md`'s measured evidence, which the first
   recommendation had been made blind to. The numbers that changed the conclusion: existing
   markers inside the eight closed runs' Context spans — 0 hits; lowercase must/shall/required
   there — 1 hit, a quoted section title, i.e. a false positive; uppercase markers anywhere in
   the eight instructions' full text — 0. Nobody writes demands the way the gate reads, and
   the defect class is owned by the bright line the `EXECUTOR-CHARTER` round installed
   (anything demand-shaped in Context is a defect on sight — a reviewer's judgement, not a
   word list). `_NORMATIVE_MARKERS` is untouched. The rider row redeems by deletion, the
   deletion citing that plan's evidence section and its own sentence that the row *"should
   not be redeemed by making the list case-insensitive"*.
6. **`ctx-ground` — keep the ruling (re-asked, upheld).** No test binds `_is_context_title`'s
   ground truth to real run artifacts (2026-08-10 ruling upheld: harness tests reading caller
   run artifacts is `E6`'s reverse). The failure direction is fail-safe and the residual risk
   is silence, accepted. Drafting discipline for the first run — write the Context title
   exactly as the predicate reads it — is recorded here as plan discipline. The rider row is
   **rewritten**: second upholding noted, deadline unchanged.
7. **`HD-55`'s carrier sentence — home is the three-roles table; fix the class, all three
   sites.** "Independent is the norm, one session holding both work-side roles is the
   exception" lands as prose in ORCHESTRATION.md's three-roles table (the table whose subject
   is role→session assignment; its carrier column already reads two full sessions). The class
   has **three sites** writing the merged form as ordinary — the cold read's `O-1` completed
   the list: `E1`'s middle-state sentence (reword as the exception channel: disclosure
   mechanics unchanged, application narrowed per `HD-55`), the three-roles table (gains the
   home sentence), and `ORCHESTRATION.md`'s *may-never-do* first bullet (the pointer sentence
   at the site `O-1` names — align so it does not point at the old reading). One home, the
   others point (`HD-5`). `HD-55` flips to **implemented in the same commit** as the carrier
   (`HD-2`), its status line updated to name the carrier.

## Change surface

| surface | what changes |
|---|---|
| `document-harness/ORCHESTRATION.md` | Handing section: delivery list gains the governing plans (ruling 1). Three-roles table: the `HD-55` home sentence (ruling 7). *May-never-do* first bullet: pointer aligned (ruling 7, `O-1`'s site). The **nine-obligations table is deliberately not touched** — riders `e1-table` / `charter-qualifiers` name that table and stay banked; redeeming them here would widen the round beyond its rulings. |
| `document-harness/EXECUTION.md` | Authoring rules: the instruction-first priority sentence (ruling 1's bound). The existing delivery half-sentence ("the plans arriving with the instruction and subject the orchestrator delivers") becomes true rather than dangling once ORCHESTRATION.md carries the obligation; adjust only if wording must name the obligation's home. |
| `document-harness/CONSTRUCTION-CHECKLIST.md` | `E1` middle-state sentence reworded as the exception channel (ruling 7). **The `E10` membership sentence is not touched** — no `E10-sync` due. |
| `document-harness/REVIEW.md` | The two sections of ruling 2 aligned; the `HarnessIssue` mention replaced by ruling 3's route. |
| `HARNESS-RIDERS.md` | Delete `plan-delivery`, `chk-thin`, `HI-route`, `mark-case`; rewrite `status-key`, `ctx-ground`. Same commit as the carriers. |
| `HARNESS-DECISIONS.md` | `HD-55` live → implemented, same commit as its carrier (`HD-2`); status line names the carrier. |
| `CONSTRUCTION-LEDGER.md` | At closeout only (orchestrator's, not the candidate's). |

**Out of boundary, deliberately:** all code and schemas (ruling 5's re-ruling makes this a
prose-only round); `E2` frozen bytes; the `E10` membership sentence; ORCHESTRATION.md's
nine-obligations table; the ten remaining resolution points; drafting the first product run.

## Opening conditions, measured 2026-08-22

- Opening cold read `v3-cold-read-3a6a10b.md` (independent session): 0 must-fix, 0 low,
  4 observations; `O-1` feeds ruling 7's site list. The `EXECUTOR-CHARTER` round's owed
  member read is paid by it.
- `HARNESS-DECISIONS.md` `§live` read at open (orchestrator; `HD-55` at its head).
- Battery at base `ee3e05f`: `python -m pytest -q` → **790 passed** (measured this session).
  Expected unchanged by this round; the executor re-runs it on the candidate.
- `E9` budget: one FULL, at most one user-approved fix, one targeted VERIFY.
- Disciplines binding the candidate and any fix leg: `E8` (dense commit body, **no
  trailers**); `HD-41` (scope before assertion; **fix legs paste the class-scan grep output
  into the commit body** — rider `fixleg-scan-paste` records a four-round miss streak, and
  this round's fix leg, if any, ends it); `HD-5` (no rule restated into a second member —
  one home, others point).
- Candidate commit title: `V3-PRERUN-RIDERS-v1`, on this branch, plain commit (no review
  window open at authoring time; the freeze marker comes with the FULL dispatch after it).
