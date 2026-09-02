# Plan — batch `PROMISE-PATH`: every disposition the rule layer names has a tested engine path or a recorded absence

> **Status: all six questions ruled 2026-09-01 — the batch is open; next act = round 1
> `PROMISE-PATH-ENGINE`'s opening read (its `E11` card owes its own user confirmation).** The
> batch was established by the user's ruling 2 of 2026-09-01 (`a6207e5`: six observations
> routed here entire, queue head ahead of candidate-isolation and dispatch-economy). The same
> day's second sitting briefed the VERIFY flow in full and took all six rulings (*Rulings*
> below), the fifth of which routes in a seventh item. Base for every figure: `f5d9741`,
> branch `dev`. A cold session reads this file, then `CONSTRUCTION-LEDGER.md`'s current
> pointer, then works.
>
> **This is design.** Items 1 and 2 change what `R3` and the disposition sentences require, so
> a round opens and its opening cold read is not waivable by this file (`E10`). The opening
> read also pays the `RULES.md` free-channel debt: `3060a23`'s two applications (`L-1`
> `:99-102` appositive deleted; `L-2` `:16-18` header made historical) still owe their
> independent read, riding this batch's opening read at per-member digest cost.
>
> **Every figure below was measured 2026-09-01 at `f5d9741`** with `grep -n`, `git log` and
> `python -m pytest tooling/tests -q` (**873 passed**, 187.70s). Re-run before any claim;
> line numbers drift.

## Goal (one line)

**Close the rule-promises-what-the-engine-cannot-do class**: for every disposition the rule
layer names, the engine either has a path a test exercises, or the absence is written down
where the rule names the disposition — measured by an `E4`-inverse suite, so the claim "this
disposition is reachable" is itself a guard that has been seen to fail.

## Where the six came from

All six are instrument-side observations recorded verbatim in the caller's three closeout
bodies — its `1a634fe` (run p5c-firewall, STOPPED_REPLAN, observations 1–4), `fe9f36a` (run
p5c-firewall-r2, STOPPED_REPLAN, the two bind defects), `c184681` (run p5c-firewall-r3,
CLOSED FINAL ACCEPT, the ISSUE_TRIAGE restatement of all six). Routing to one standalone
batch is the user's ruling 2 of 2026-09-01; contract §11 makes that routing a user decision
and it is taken. Two real runs stopped on this class — each stop cost the caller a full
successor run.

## Rulings — 2026-09-01, taken in conversation after the full-context briefing

The user's words, against the numbered questions this plan's first version put: **"1a 2a 3确认"**.

1. **Item 1 takes shape (a) — the path is built.** After a blocking VERIFY the engine gains a
   user-authorized branch: bind may construct an AssuranceCandidate carrying the standing
   blocker verbatim as a disclosed limitation, so FINAL — `ACCEPT_WITH_LIMITATIONS`, `REJECT`
   or `REPLAN` — becomes representable. The rule sites change nothing: the promise they
   already make becomes true. Shape (b), recording the absence, was offered and not taken.
2. **Item 2 takes shape (a) — the VERIFY verdict vocabulary gains a value** meaning "a blocker
   stands after the one repair", so `SPEC_GAP` returns to its defined meaning (spec defective,
   new WorkSpec, new START). Touches `R3`, `REVIEW.md`'s verdict table and its
   cannot-return-`CHANGES_REQUIRED` sentence (`:129-135`), `review.v2.schema.json` (announced),
   `flow.check_verify_outcome`, tests — and the signed contract's VERIFY verdict row (`:118`),
   which is open question 6's subject. The value's name: the executor proposes at round 2's
   decision point and the user ratifies (`HD-69` makes that a same-session stop, not a new
   dispatch). Shapes (b) and (c) were offered and not taken.
3. **Item 3's direction is confirmed** — the engine follows `R10`: bind stops at `REVIEWED`,
   the lows decision point becomes real, and candidate + `AWAITING_FINAL` follow only the
   user's choice not to spend the leg.

Coupling now explicit: item 1's branch fires on item 2's new verdict value — it is the
machine-readable form of "blocker stands" — which is why both stay in one round.

The same day's third exchange answered questions 4–6, the user's words: **"两轮，并入，6 i"**.

4. **Two rounds** (`ENGINE` then `VOCAB`), as proposed.
5. **The adjacent seventh is routed in** — item 7 below, joining round 1. This is the "own
   ruling" `HD-65`'s boundary reserved ("要修要另裁"); the batch now carries seven items.
6. **Path (i)** — a fifth `HD-63/64/67/68`-family ruling authorizes the in-place contract
   change item 2's value needs: the VERIFY verdict row (`:118` at `f5d9741`) plus whatever
   sibling sites the executor's `HD-41` ④ class scan enumerates, each named before the
   executor writes. The orchestrator transcribes this into the decisions register as the
   fifth family entry at round 2's opening, sites enumerated; scope = this one vocabulary
   change, no precedent expansion — the family's own discipline. Obligations unchanged from
   the family form: `E2` disclosure in the writing commit's body,
   `CONTRACT-V4-SIGNATURE.md` records the post-signature write, `E10` independent re-read of
   the changed text.

## The six defects, each pinned to the tree

Numbering below is the ledger row's order and is the batch's item vocabulary.

### Item 1 — `ACCEPT_WITH_LIMITATIONS` after a blocking VERIFY has no path

- **Rule promise**: `document-harness/EXECUTION.md:98-100` ("the honest dispositions left are
  `STOPPED_REPLAN` or a user `ACCEPT_WITH_LIMITATIONS` that names what is still open");
  `document-harness/REVIEW.md:210-212` (residual_uncertainty reaches the user at FINAL, "where
  they may convert it to `ACCEPT_WITH_LIMITATIONS`"); contract v4 `:105` and `:122`;
  `tooling/rsclib/document_harness/flow.py:571` (docstring).
- **Engine fact**: a FINAL-phase UserDecision binds one exact AssuranceCandidate (invariant 12)
  and after a blocking VERIFY none exists — `flow.check_verify_outcome` (`:553`) reports
  `V3-FLOW-VERIFY-SPEC-GAP` / `V3-FLOW-BLOCKER-AFTER-VERIFY` and the flow admits only
  `REVIEWED` or `STOPPED_REPLAN` from `EVIDENCED` at round 1. The engine mentions the
  disposition in two strings only (`run_bind_v2.py:356` next-action text, `flow.py:571`
  docstring). The caller hit this in run 1 and the user's earlier `ACCEPT_WITH_LIMITATIONS`
  ruling had to be superseded by `STOPPED_REPLAN` on evidence the first ruling did not have.
- **Ruled — shape (a), 2026-09-01** (*Rulings* 1): build the path. A supporting fact the
  ruling weighed: the disposition is already alive and tested on the clean path
  (residual_uncertainty → FINAL conversion; `assurance.schema.json:180` forces limitations to
  be listed), so what is missing is only the blocking-VERIFY branch of bind, the flow
  admitting it, and tests.

### Item 2 — the VERIFY verdict vocabulary has no value for "a blocker stands after the one repair"

- **Rule promise**: `document-harness/RULES.md` `R3` (`:191-199`) — VERIFY →
  `REVIEWED_NO_BLOCKER | SPEC_GAP`; `schema/document-assurance-v3/review.v2.schema.json:68`
  (VERIFY-round narrowing), `:32` (closed verdict enum); contract v4 `:117-118` (both verdict
  tables).
- **Engine fact**: `SPEC_GAP` is borrowed for the standing-blocker outcome, and its name tells
  a later reader the specification failed when it did not — the caller's run 1 VERIFY returned
  `SPEC_GAP` for a defect the approved repair created and could not legitimately reach.
- **Ruled — shape (a), 2026-09-01** (*Rulings* 2): a new verdict value. The FULL vocabulary is
  untouched; only the VERIFY row grows. The touched-surfaces list and the contract question
  live in *Rulings* 2 and open question 6.

### Item 3 — after a clean FULL the repair leg is unreachable (engine violates `R10`)

- **Rule promise**: `document-harness/RULES.md` `R10` (`:227-232`) — a FULL returning
  `REVIEWED_NO_BLOCKER` with lows does not bank them by default; the orchestrator puts the
  spend-the-fix-leg / bank choice to the user; a late activation is still that round's one
  user-approved fix and still obliges the VERIFY.
- **Engine fact**: `assurance/templates/run-v2/run_bind_v2.py:244` stops at `REVIEWED` only
  when `REPAIR_ROUND == 0` and the verdict is not `REVIEWED_NO_BLOCKER`; a clean verdict takes
  the other branch (`:352-363`), which advances `REVIEWED`, writes the candidate and advances
  `AWAITING_FINAL` **in one act**; `flow.py:53-63` `_SUCCESSORS` gives `AWAITING_FINAL`
  exactly one successor (`CLOSED`) and makes `REPAIRING` reachable only from `REVIEWED`. So
  the choice `R10` orders never gets a moment to be put. The caller's run 2 stopped exactly
  here: a clean FULL, the user accepted f1–f3 for repair, and the decision could not be
  executed. No rule change is needed — the engine catches up with the rule. **Direction
  confirmed 2026-09-01** (*Rulings* 3); the shape (bind stopping at `REVIEWED` to surface the
  decision point, candidate + `AWAITING_FINAL` as a separate act) is the executor's.

### Item 4 — `run_evidence_v2.py` writes its own commit message (`E8` surface)

- **Rule promise**: `E8` (`RULES.md:72-76`) — single dense title naming the round, one dense
  paragraph, the commit's kind named so the review side can attribute it without asking.
- **Engine fact**: `assurance/templates/run-v2/run_evidence_v2.py:304-305` commits with a
  hard-coded one-line f-string (`{RUN_ID} evidence commit (control plane; candidate …)`), so a
  title and body the orchestrator is obliged to require cannot land on an evidence commit —
  the caller's `2c6ed15` carries a one-line template string and no tier declaration.
- **Fix shape**: the script accepts the message (argument or file) and refuses its absence;
  what stays hard-coded is at most a validated fallback structure, not the message. Engine +
  template only; no rule change.

### Item 5 — bind copies the governance digest forward and nothing verifies it

- **Rule promise**: the AssuranceCandidate's `governance_scan` block exists so the candidate
  states what was scanned (`run_bind_v2.py:64-65` docstring); a digest nobody checks certifies
  nothing.
- **Engine fact**: `run_bind_v2.py:293-320` loads `control/bind-declarations.json` and copies
  `governance_scan` (including `result_ref.digest_sha256`) verbatim into the generated
  candidate; at the caller's `2c6ed15` it declared a round-0 digest for a file whose bytes had
  changed. Nothing recomputes the digest against the named file's bytes at bind time.
- **Fix shape**: bind recomputes and refuses on mismatch. Engine + tests; no rule change.

### Item 6 — `bind-declarations.json` is validated by nothing and the 500-character cap bites only at bind

- **Rule promise**: implicit in the bind chain — a hand-authored file feeding a schema-capped
  generated document (`schema/document-assurance-v3/assurance.schema.json:95/:116/:179`,
  `maxLength: 500`) should fail where it is authored, not after the independent review has
  read those bytes, when correcting them means changing what was reviewed.
- **Engine fact**: nothing under `schema/` names `bind-declarations.json` (grep over the pack,
  14 files, zero hits); `run_bind_v2.py:73` names it and `:293-302` checks only key presence.
  The caller's run 2 had three disclosures at 541 / 843 / 513 characters, `check_assurance_candidate`
  refused, and the bind exited 1 having moved nothing — with no FINAL representable
  (invariant 12).
- **Fix shape**: a `bind-declarations.schema.json` in the pack plus an authoring-time
  assertion (validate at write and at bind's load, both). A pack file added now is **not
  announced** — `E2` re-baselines rather than auto-enrolling — so the new schema carries no
  disclosure obligation until a later re-baseline; writes to the three existing schema files
  and the contract, if any, are announced-path writes and their commits name the full paths
  site by site.

### Item 7 — `flow.check_repair_decision` validates nothing it reads (routed in by ruling 5)

- **Where it came from**: not one of the caller's six. `HD-65`'s boundary paragraph recorded
  it 2026-08-29 — the function "对任何 result 都不验证，v2 的也不验证；v1 只是它今天最显眼的
  一个面" — and reserved the repair for its own ruling; ruling 5 of this plan is that ruling.
- **Engine fact**: `flow.check_repair_decision` (`flow.py:339`) uses the review result it
  reads to decide and validates none of it — a v1-shaped result returns a clean report,
  pinned live by `test_the_v1_root_shape_is_unaffected`, and
  `tooling/rsclib/document_harness/review_result_v2.py:33-39` states the property in code.
  `HD-65`'s measurement named the accessor (`flow.reviewed_candidate_ref`) as the same
  class's second site; `E7` binds the executor to the class, so both sites are in scope.
- **Fix shape**: validate before use — keyed on `schema_version` (the W1 pattern, no
  cross-version fallback, fail closed); the pinning test flips from "unaffected" to
  "refused". Round 1; sibling of items 5–6 on the bind chain. No contract change: `HD-65`
  interpreted §13.1's "not accepted" as verification-path only, and adding engine validation
  contradicts nothing it ruled.

## The spine — the `E4`-inverse suite

`E4` says never trust a guard you have not seen fail. The inverse this batch builds: **never
trust a disposition you have not seen reached.** One test module (under
`tooling/tests/document_harness_review/`) that carries a hand-written table (`E5`: the
expectation is a committed fixture, never derived from `flow.py`'s own constants) of every
disposition the rule layer names — the FINAL enum, both verdict enums, `STOPPED_REPLAN`, the
repair leg in both FULL outcomes, the `ACCEPT_WITH_LIMITATIONS` conversion — and asserts for
each: either a test in the suite exercises the engine path end-to-end (mutation-tested per
`E4`: neuter the path, watch the suite go red), or the table row says `no-path` and the rule
site that names the disposition carries the absence in its own text. A disposition in the
rules but absent from the table fails the suite; so does a `no-path` row whose rule site says
nothing. The table's rows are settled by the rulings below; the suite is what keeps the class
closed after this batch — a future rule promising a new disposition meets a red test until
the engine or the table answers it.

## Change boundary

- **In**: `tooling/rsclib/document_harness/flow.py` ·
  `tooling/rsclib/document_harness/review_result_v2.py` (item 7's validation entry) ·
  `assurance/templates/run-v2/` (both
  templates) · `schema/document-assurance-v3/` additions and, under the rulings, the three
  existing schema files · `tooling/tests/` · under *Rulings* 2: `document-harness/RULES.md`
  (`R3`'s VERIFY vocabulary), `document-harness/REVIEW.md:129-135`, and — under question 6's
  ruling only — contract v4 `:118`. `EXECUTION.md:98-100`, `REVIEW.md:210-212` and contract
  `:105`/`:122` now stay as written: shape (a) makes them true rather than changing them.
- **Announced paths** (`E2`): the contract and the fifteen re-baselined pack files — every
  write disclosed in its commit body, path by path. New pack files are not announced.
- **Signed text**: any contract touch is a per-site user ruling in the `HD-63/64/67/68`
  family (or a versioned successor if the touches are more than sites); the executor writes
  nothing there without the ruling landing in this file first.
- **Out**: candidate isolation (its own ledger entry, unruled) · dispatch-economy (carries
  `HD-69`'s landing) · the caller's run scripts (`run_stop.py` etc. are run-authored; the
  templates here are the instrument's face) · any `.goals/` content.

## Rounds and budget (ruled — *Rulings* 4)

Two rounds, each with the full `E9` budget (one FULL · at most one user-approved fix · one
targeted VERIFY):

- **Round 1 `PROMISE-PATH-ENGINE`** — items 3, 4, 5, 6, 7 plus the suite's first standing:
  engine catches up with rules nobody is changing. Touches code, templates, one new schema,
  tests.
- **Round 2 `PROMISE-PATH-VOCAB`** — items 1, 2 as ruled: the new VERIFY verdict value (name
  ratified at the round's decision point), `R3` and `REVIEW.md:129-135`, the blocking-VERIFY
  bind branch that fires on it, and the contract site under question 6's ruling. The suite's
  table rows for these two items land here.

Rationale: items 3–7 are executable now; items 1–2 carry the fifth family ruling's
transcription and site enumeration (ruling 6), and coupling the rounds would hold five ready
fixes hostage to it.

## Opening read

At round 1's opening: `E10` cold read, not waivable (this batch is design), dispatched via
`tooling/construction_dispatch.py --read` — the seven members plus this repository's declared
rules file (`document-harness/CONSTRUCTION-CHECKLIST.md`), unchanged blobs covered by citing
their recorded reads. **This read pays the free-channel debt**: `RULES.md`'s blob changed at
`3060a23` (two free-channel applications, both disclosed, both unread), so `RULES.md` is read
end-to-end and the record states its blob id. `HARNESS-DECISIONS.md` `§live` in full at the
same opening — eleven entries at `f5d9741`: `HD-69` · `HD-66` · `HD-65` · `HD-62` · `HD-59` ·
`HD-41` · `HD-36` · `HD-35` · `HD-34` · `HD-23` · `HD-9` — inherited by this plan as they
stand, not transcribed.

## Executor form

`HD-69` is live and binds this batch: **one executor session from START to FULL** — the
executor stops at decision points, the orchestrator routes the ruling, and the same session
resumes (`claude -p --resume <session-id>`); cold start belongs only to a round's first
dispatch. The command-face support (recording session ids) is batch `dispatch-economy`'s and
is not built; until then the orchestrator records the executor's session id in the round
journal by hand. Live rulings that shape the work besides `HD-69`: `HD-59` (committed
conclusions corrected forward, never in place) · `HD-41` (scope before assertion; class-scan
grep output pasted into commit bodies) · `HD-65` (its boundary is open question 5's subject) ·
`HD-62`/`E2` (announced-surface disclosure).

## Open questions

None. All six were put and ruled 2026-09-01 — *Rulings* above. Question 6's background, kept
for the record: §13 forbids in-place amendment of the signed contract; the `HD-63/64/67/68`
family overrode it one class at a time, each ruling refusing precedent expansion; the
vocabulary change item 2 needs is none of their classes and larger than each, which is why it
takes a fifth family ruling (path (i), taken) rather than riding any existing one — the
alternative offered and not taken was a versioned successor (v5) for one table row.

## Steps — round 1 `PROMISE-PATH-ENGINE`

- [x] 1. **Open + read — DONE 2026-09-02.** Round 1 opened on the user's "开轮" at the `E11`
  card; `python tooling/construction_dispatch.py --read 51bd4f6`, one cold `claude -p` session
  on `opus` without web tools; record `v3-cold-read-51bd4f6.md` committed unchanged at
  `b2f2c3b`, the freeze marker deleted in that act. **1 must-fix, 1 low, 2 observation**; the
  `RULES.md` free-channel debt from `3060a23` discharged by the record's §3.
- [x] 2. **Disposition — the commit that checks this box.** `M-1` (the record-commit owner
  split between `R6` and `REVIEW.md`) ruled **(c)** by the user 2026-09-02: downgraded to low
  and banked as rider `record-commit-owner`, deadline before the next product-run review
  dispatch, redeem surface includes round 2. `L-1`'s named content applied to `R10`'s first
  sentence by `E10`'s free channel on the orchestrator's finding that it adds no clause and
  changes no rule's requirement (the requirement was already "not the instrument's bank") and
  that no round has relied on the sentence; its independent read rides the next read of this
  layer at per-member digest cost. `O-1`/`O-2` stay recorded in the read record, no rows. No
  amendment/re-read pair is owed: nothing above low was fixed in the layer.
- [ ] 3. Executor dispatch — one cold `claude -p` session on `opus` (`HD-69`: it stops at
  decision points and is resumed with rulings, same session; the orchestrator records its
  session id in the round journal by hand). Scope: items 3–7 + the `E4`-inverse suite, round
  1's change boundary (no rule-layer or contract bytes — those are round 2's).
- [ ] 4. FULL (cold, dispatched with `--range`) → user gate on findings → at most one
  user-approved fix (same-session resume) → targeted VERIFY → closeout, ledger pointer in the
  closeout commit.

## Resume pointer

Round 1 `PROMISE-PATH-ENGINE` in flight: steps 1–2 done, next act = step 3, the executor
dispatch. A cold session: read this file, the steps above, then `CONSTRUCTION-LEDGER.md`'s
pointer.
