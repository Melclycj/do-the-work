# Round journal — `PROMISE-PATH-VOCAB` (batch `PROMISE-PATH`, round 2)

Opened 2026-09-03 on the user's "ok" at the `E11` card, base `2db6d87` (the `dev` tip at
opening; the plan's rulings 7–9 are the three answers taken off the card). Chain so far: open
(this commit) → `HD-70` transcription (the next commit) → read dispatched at that tip.

`HD-69` executor session id: recorded here by the orchestrator by hand when the executor is
dispatched (the command-face support belongs to batch `dispatch-economy` and is not built).

Decision points, resumes and rulings are appended below as they happen, each dated. A
committed judgment in this file is corrected forward, never rewritten (`HD-59`).

**Read (2026-09-03).** Dispatched at tip `c50362c` (`python tooling/construction_dispatch.py
--read c50362c`), one cold `claude -p` on `opus` without web tools, session
`c07ef2ee-6969-45cb-af69-7a916e97a360`, 70 turns; record `v3-cold-read-c50362c.md` committed
unchanged at `13fde05`, the freeze marker deleted in that act. **0 must-fix, 2 low, 2
observation**; both deferrals (`1c18e4a`, `38038ec`) discharged; battery 938 by the reader.

**Disposition (2026-09-03), the user's "1a 2a".** L-1 (`README.md:20`'s count sentence)
takes `E10`'s free channel with the record's exact bytes; the orchestrator's two findings: the
application adds no clause and changes no rule's requirement, and no round has relied on the
sentence; its independent read rides the next read of this layer. This is also the moment
rider `wl-route`'s deadline names (O-1): the route taken is the one `E10`'s enumeration and
`R10`'s routing sentence give, as `1c18e4a` took it; the row's tiebreak is design and the row
stands. L-2 (contract §5's heading) is banked as rider `enum-single-home`, no sixth family
ruling — measured before the ruling: the heading was false at v3's own signing
(`common.schema.json` never held a verdict or decision enum; `git log -S` over its history
returns nothing), so it is not `HD-63`'s class. O-2 recorded; the `E2` re-baseline question
is deferred to the batch's closeout. Plan step 2 checked in the disposition commit.

**Executor dispatched (2026-09-03).** At tip `b9710af`, cold `claude -p` on `opus` without
web tools; `HD-69` session id, recorded by hand: **d8f5d450-a3cf-495a-86c5-99840b0c8ca6**.
First work block: `61afc26` (rider `record-commit-owner` redeemed at `REVIEW.md:46,156`, row
deleted, battery 938). Stopped at the first decision point — the value's name and the
sibling contract sites — as plan rulings 2 and 8 said it would.

**Resume 1 (2026-09-03).** The user ruled "1b 2 同意" — plan rulings 10 and 11: the value is
`UNRESOLVED_BLOCKER`; contract `:127-128` and `user-decision.schema.json:44` lose the ordinal
(the schema file joins the boundary by this ruling), `:195-196` and `:200-201` stand. Forward
correction (`HD-59`): `HD-70` cites the remaining-blocker sentence as `:196-197`; at `b9710af`
it is `:195-196`, `:197` being blank — the entry is left as written. `E1`: the round stands in
the norm, two sessions, and the executor holds none of `R1`'s four holdings (dispatched by,
prompted by, scoped by and reported through the orchestrator). Same session resumed with the
rulings; no cold correction executor.

Asked at this stop by the user — could these decision points have been foreseen at START? —
and answered in conversation: four of the five sites and the name's candidates were
derivable at the `E11` card (the schema-description sibling was in the orchestrator's own
second scan and mis-triaged as a restatement); only `:200-201` needed the wider class
reading the executor made. Whether the card must carry candidate names and a written class
definition is batch `dispatch-economy`'s question, not filed here (`R5`).

**Executor complete (2026-09-03).** The resumed session ran to the end of step 3 without a
second stop: `15e5ccc` (item 2) and `97cc298` (item 1 + rider `no-repair-unbound` + the
touch record), 130 turns in all across the cold start and one resume. Executor-reported and
not yet independently reproduced: battery 951 at `97cc298`, 16 mutation probes fired, riders
table at 32 data rows by id column after two redemptions and this round's one banking. Three
judgments the executor flagged for the review: no new decision phase or value (the FINAL
decision itself is the licence); the companion guard refusing an unqualified `ACCEPT` over a
standing blocker, which ruling 1's enumeration implied but did not name; and
`check_verify_outcome` left logically unchanged. Plan step 3 checked in this commit.

**FULL range.** `b9710af..97cc298`: base = the executor's dispatch tip, tip = its last
candidate commit, the shape round 1 used (`1c18e4a..38038ec`). The plan's step-4 placeholder
said "HD-70 tip", which would have put the read record and the disposition commit inside the
subject; the plan is corrected in the same commit as this note.

**FULL (2026-09-03).** Dispatched on `b9710af..97cc298` at branch tip `f0143c8`; cold
`claude -p` on `opus` without web tools, session `da96703b-e90f-4f7b-a65e-f427310cb490`, 91
turns; record `v3-review-full-97cc298.md` committed unchanged at `67dbb08`, the marker deleted
in that act. **`CHANGES_REQUIRED`**: B-1 (the companion guard refuses an ordinary successful
repair — its predicate is the union of every review's blockers, closed ones included), B-2
(the new licence pointer is written with a digest no reader checks: absent from
`POINTER_FIELDS` and from `read_control_plane`'s field tuple), L-1, L-2, L-3, O-1, O-2, O-3.
Item 2 clean at every site; the branch itself driven end to end by the reviewer; battery 951
reproduced.

**Design or execution — asked by the user, answered before the leg was ruled.** B-1:
execution, with a design gap — ruling 1 named three FINAL outcomes and was silent on bare
`ACCEPT`; the executor filled the gap, reasonably, and chose the wrong predicate, misreading a
field whose own docstring says the controller has no vocabulary for "repaired"; its tests
pinned the intent, not the population the predicate covers. B-2: execution — half a mechanism
(a writer with a digest, no reader); the class scan for "every place a new pointer field is
registered" was not run although the tuple's docstring says "every pointer-shaped field"; the
rider row was deleted while its stated defect (a later reader cannot verify) was still open;
all nine executor probes were on the write side, and no test pinned the two tables'
consistency.

**Resume 2 (2026-09-03), the user's "同意".** Plan ruling 12: leg (ii) B-1 + B-2 + L-2, B-2's
fix carrying a class assertion; O-2 banked as `bound-at-digest-gate`; O-1 and L-1 corrected
forward below; L-3 answered by the plan's boundary line; O-3 recorded. Same executor session
resumed for the one fix; it obliges the targeted VERIFY.

**Forward corrections (`HD-59`; the number under `HD-23`).** O-1: the figure "riders table at
32 data rows by id column" in `f0143c8`'s body and in the *Executor complete* note above is
wrong — the pattern used required lowercase ids and skipped `RA`, `PD` and `E10-sync`; counted
by the id column with the header and separator rows excluded, the table holds **35** rows at
`97cc298` (37 at `b9710af`, 36 after the first redemption, 35 after the second), the
reviewer's figure, re-measured here. L-1: `97cc298`'s class-scan section cites
`document-harness/REVIEW.md:215` for the promise sentence at its declared anchor `15e5ccc`,
where that sentence sits at `:226`; `:215` was its line at `61afc26`. Both bodies stand as
written.

**VERIFY (2026-09-03).** Dispatched on `97cc298..d56def4` at tip `d56def4`; cold `claude -p` on
`opus` without web tools, session `35818543-4607-44ae-b3af-e309ae4eccde`, 64 turns; record
`v3-review-verify-d56def4.md` committed unchanged at `da1aac3`, the marker deleted in that
act. **`REVIEWED_NO_BLOCKER`**: both blockers closed by driving the repaired code, L-2 closed at
four sites; V-1 (four sites still say the protected set is five, two in the signed contract),
V-2 (`review_subject`'s tuple pinned by nothing), V-O-1..3. `E9` spent in full: FULL `67dbb08`,
fix `d56def4`, VERIFY `da1aac3`.

**Closeout (2026-09-03), the user's 「按建议」.** V-1 banked as `protected-set-says-five`, the
two contract sites confirmed `HD-63`'s class (true at signing, falsified by `97cc298`), so the
redeeming write goes under `HD-63` with `E2` disclosure and a ninth signature-record entry and
opens no family entry; V-2 banked as `subject-tuple-unpinned`; V-O-1 banked as
`check-summary-reviews-undocumented`; V-O-2 and V-O-3 stay in the record. `HD-70` flipped to
`implemented` in this commit (carrier `15e5ccc`, reviewed by `67dbb08` + `da1aac3`); its
`retired` follows the next opening cold read, which is also the carrier of the independent
re-read the round's commit bodies promised for `RULES.md` `R3`, `REVIEW.md`, contract
`:118`/`:127` and `README.md:20` — FULL O-3: the phrase "this round's next read of that layer"
named a read the round did not perform, corrected forward here with the bodies standing. `E2`
re-baseline not opened; rider `announced-set-anchor` holds it. L-3's second occurrence in two
rounds — engine modules written outside the plan's *In* list with the escape unnamed — is
answered by the plan's boundary line and left here for the next plan's author. Batch
`PROMISE-PATH` CLOSED; the ledger row moved verbatim to the archive; queue head = candidate
isolation, whether it opens being a separate 开轮 question. The user's question at the
executor's first stop — whether decision points are foreseeable at START — stays with this
journal; the `dispatch-economy` backlog row is untouched (`R5`). `E1`: the round ran in the
norm, two sessions, the executor holding none of `R1`'s four holdings. Sessions: reader
`c07ef2ee…`, executor `d8f5d450…` (cold start + two resumes), FULL `da96703b…`, VERIFY
`35818543…`.
