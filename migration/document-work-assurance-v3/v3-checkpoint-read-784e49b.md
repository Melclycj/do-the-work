# Instruction-layer read — `784e49b2aa6b6f18b20d5955fbef509f00b2f404`

`E10` amendment read of the instruction layer at the layer-incorporation round's final
bytes (plan Step 9). Not a round: no verdict, no budget consumed (`R3`). Findings tiered
must-fix / low / observation. This read also discharges the ride-along read the three
`7463229` layer applications owe — the L1 commit's own binding *"the round's own closing
layer read (plan Step 9, not yet dispatched) covers the final bytes"* — at per-member
digest cost: all three touched members (`README.md`, both stubs) are read in full below.

**Findings: 0 must-fix, 1 low (banks — no appliable bytes without tripping the design
test), 4 observations.** Every factual assertion in the changed bytes was re-derived by
command and holds: `E2`'s new pin facts (pack joined 2026-07-29 at `11d147e`, fourteen
files then and now, zero diff between), the fourth frozen blob is the carrier's actual
blob, the R10 migration is deletions-and-stitching against the `c61d82d` header line for
line, and the three applied L1 sites are byte-for-byte the fix the FULL record's L-1
supplied. The banked residue `L-2li` is verified in place and is not re-raised.

## 1. Subject, re-derived

`R2`: I was handed one SHA and the phrase *the instruction layer*. Everything below is
re-derived; no figure in the dispatch, the ledger or any prior record is accepted as
reported.

```
$ git rev-parse HEAD       -> 784e49b2aa6b6f18b20d5955fbef509f00b2f404
$ git status --porcelain   -> (empty)
```

`E10`'s sentence at the subject commit governs the member set. Enumerated against the
repository: **eight** members. The open tail adds none — `git diff --name-only ae4df09
784e49b -- ResearchSystem/schema/` returns 0 paths, so no schema `description` was
amended; the prose files added since the last layer read (`v3-cold-read-ae4df09.md`,
three round journals, four review records, one plan) are records and plans by their own
headers, not successors to text this harness governs. `layer_path_check.LAYER`
(lines 30–39) is the same eight paths, riders not among them.

| # | blob at `784e49b` | lines | member | vs. last recorded read |
|---|---|---|---|---|
| 1 | `dff584d9` | 156 | `document-harness/CONSTRUCTION-CHECKLIST.md` | **changed** (`33126c19` → at `feacb86`) |
| 2 | `bb84e6f2` | 36 | `document-harness/README.md` | **changed** (`4daab565` → at `7463229`) |
| 3 | `bd490c8b` | 153 | `document-harness/EXECUTION.md` | same since `d58969d` read |
| 4 | `d050b05a` | 227 | `document-harness/REVIEW.md` | **changed** (`70bc521e` → at `feacb86`) |
| 5 | `17ff31bb` | 5 | `migration/…/v3-harness-operating-contract.md` (stub) | **changed** (`0ae222fd` → at `7463229`) |
| 6 | `52a97a48` | 5 | `migration/…/v3-harness-review-contract.md` (stub) | **changed** (`7dcdb817` → at `7463229`) |
| 7 | `68031fa2` | 124 | `contract/…-v3-supersession-1.md` | same since `d58969d` read |
| 8 | `e1a2f26b` | 113 | `contract/…-v3-supersession-2.md` | same since `403fc9a` read |

Blob ids from `git ls-tree 784e49b <dir>`; line counts from `git cat-file -p
784e49b:<path> | wc -l`. Five members changed since the last read of each, in exactly two
commits (`git log ae4df09..784e49b -- <member>` per member): `feacb86`
V3-LAYER-INCORPORATION-v1 (members 1, 4) and `7463229` V3-LAYER-INC-L1-BYTES-APPLIED-v1
(members 2, 5, 6). No other commit in `ae4df09..784e49b` touches a member.

**Dispatch, checked rather than assumed.** `.harness/review-pending.json` is live and
reads `{"kind": "layer-read", "subject": "784e49b2aa6b6f18b20d5955fbef509f00b2f404",
"dispatched_at": "2026-07-30T15:49:07+00:00"}` — the subject I was handed, which is the
branch tip. The branch has taken no commit since the subject; `E9`'s window is intact and
this record is the only commit it admits.

## 2. Coverage — `E10` citation clause, per-member

Members 3 and 7 are blob-unchanged since `v3-checkpoint-read-d58969d.md`, whose §1 table
carries `bd490c8b` (row 3) and `68031fa2` (row 7) and whose closing disclosure states
*"Read in full: all eight layer members at the blobs tabulated in §1"*. Member 8 is
blob-unchanged since `v3-checkpoint-read-403fc9a.md`, whose §1 table carries `e1a2f26b`
(row 8, 113 lines) and whose disclosure lists it under read-in-full; its §"assertions"
table re-derives that very blob as the signed carrier. I verified all three citations
against git rather than against the records' tables: `git rev-parse d58969d:<path>` /
`403fc9a:<path>` equals `git rev-parse 784e49b:<path>` for each. Both cited records'
commits landed (`38008a1`, `9ddaff6`). Coverage discharged by citation for three; the
five changed members read in full here at the subject blobs.

Staleness the byte-key cannot see: the three unchanged members were grepped for the
delta's vocabulary (`R1.R9`, `Three blobs`, `rider`, `HARNESS-RIDERS`, `R10`, `free
channel`, `errata`) — zero hits; nothing in them restates or contradicts the amended
content. A whole-layer sweep for a leftover `R1–R9` enumeration returns zero sites — the
L1 propagation is complete.

## 3. What the deltas do, against the fixes and rulings they claim to apply

**`feacb86` (members 1, 4).** The FULL (`v3-review-full-feacb86.md`, committed `6132828`)
traced all nine edits to sources; this read's subject is the landed amendment text
itself, so the load-bearing traces were re-derived here rather than cited:

- `E2` pin (E2-t): the pack entry joined `E2`'s list at `11d147e` (2026-07-29,
  V3-E2-SCHEMA-PACK-AND-FACT-CORRECTION-v1); `git ls-tree -r 11d147e …/schema/
  document-assurance-v3/` → 14 files; same count at `784e49b`; `git diff 11d147e
  784e49b -- <pack>` → 0 paths. Both facts in the new parenthetical hold.
- `E2` fourth blob (E2-s2): `git rev-parse 784e49b:…supersession-2.md` =
  `e1a2f26b1d8d323d11e900f8137dea222b6571c1` — the list line names the carrier's actual
  blob; the carrier's bytes are untouched (member 8 blob-identical since the `403fc9a`
  read). "Three blobs" → "Four blobs" agrees with the list it counts. The other three:
  `8ad404b1…` (signed plan), `b2dbdf75…` (contract), `68031fa2…` (supersession-1), each
  re-derived by `git rev-parse 784e49b:<path>`.
- `E10` seam (BC-1 / F-1r / V-c / E10-d / L-2r): read whole against the pre-amendment
  form in the diff. The design clause now follows the relied qualifier; the collision
  rule answers who-wins ("design wins and the round opens"); the relied definition sits
  in parentheses restoring the contrastive dash; the design test catches replacements
  and deletions; the citation clause now requires read records to state blob ids — the
  property §1–§2 of this record exercise. Internally coherent; the one known residue
  (the deferral clause's own precondition still reading "adds no new clause") is banked
  as `L-2li` and verified in place — not re-raised.
- `E8` kinds (O-6): the list gains amendment / ruling / record. The round's own four
  commits self-name on-list kinds (candidate `feacb86`, record `6132828`, amendment
  `7463229`, ruling `784e49b` — each body's closing "Kind:" read directly).
- `E12` (O-4r): the qualifier scopes never-a-written-SHA to ranges recorded in a file;
  consistent with the round's own `rsc v3 dispatch --range 0224176..HEAD` usage.
- new `R10`: compared line against line with the riders header at `c61d82d` (read here,
  not taken from the FULL): routing sentence kept with the dead `C-3` reference replaced
  by `E10`'s must-fix channel; tightenings ①–③ verbatim (① minus its executed transition
  tail; ③ including the spend-the-fix-leg / bank rule, which therefore pre-existed the
  incorporation as a 2026-07-30 user ruling); the bank/HarnessIssue division sentence is
  the one new limb, per the 2026-07-31 ruling (`bf73536`).
- `REVIEW.md` (VB-1): the verdict-basis section states repository reality as the verdict
  basis and the obligation list as the question list — read in the whole file; it agrees
  with `R3`'s implementation-first / conformance-second order and contradicts nothing
  downstream in the same file.

**`7463229` (members 2, 5, 6).** Three sites, each `R1–R9` → `R1–R10`, byte-for-byte the
fix `v3-review-full-feacb86.md` L-1 supplied ("at each of the three sites, `R1–R9` →
`R1–R10`"), nothing else in the diff. First use of the byte-supplied-low channel on layer
text; the ride-along read debt is discharged in §5 below.

**`784e49b` (no member).** Adds rider row `L-2li` and checks plan boxes; touches no layer
byte. The row conforms to R10: what / redeem-when (touch: next batch on `E10`'s deferral
clause) / source; no deadline, and none owed — pure wording, no moment at which the
defect starts to bite, given the design clause blocks the practical path.

## 4. Assertions re-derived by command

| assertion in the changed bytes | command | result |
|---|---|---|
| `E2`: pack joined the list 2026-07-29 with fourteen files | `git log -1 11d147e` (2026-07-29); `ls-tree -r` ×2; `diff 11d147e 784e49b -- <pack>` | holds — 14/14, zero diff |
| `E2`: four frozen blobs | `git rev-parse 784e49b:<path>` ×4 | holds — `8ad404b1…` / `b2dbdf75…` / `68031fa2…` / `e1a2f26b…` |
| `R10`: bank lives at `ResearchSystem/HARNESS-RIDERS.md`, rows what·redeem-when·source | file read at `784e49b` | holds — pure data table, 9 rows (8 remainder + `L-2li`), header a pointer back to R10 |
| README row 26: checklist carries E1–E12 / R1–R10 | checklist read in full | holds |
| README row 31: fixtures 41/41 green | `python …/N0/fixtures/validate_fixtures.py` | holds (this machine) — `41/41 cases behaved as declared; failures=0` |
| every relative link target in members 1, 2, 4 resolves | script over all targets at the subject tree | 29/29 resolve |
| stubs line 3: checklist "carries both sides in one file" | checklist read in full | holds |
| opening cold read's citation base (candidate's commit body) | `git diff --name-only ae4df09 c61d82d -- <8 members>` | 0 paths — the citation to `ae4df09`'s table was valid |

No assertion in the layer was found false at this commit.

## 5. Ledger bindings, checked

- *L1's three layer applications owe the ride-along read* — discharged: members 2, 5, 6
  read in full at `bb84e6f2` / `17ff31bb` / `52a97a48`, the applied delta verified
  byte-for-byte against the L-1 fix (§3).
- The deferral was clean before this read: between application (`7463229`) and dispatch,
  the branch took exactly one commit (`784e49b` — plan boxes + one rider row, `git log
  --name-status`), which records and rules but does not rely; no round opened.
- Plan Step 9 names this read and `R6` its record naming; the dispatch marker's kind is
  `layer-read` with the branch tip as subject.
- Round budget state as this read finds it: FULL spent (`6132828`); fix leg unspent —
  L-1 took the byte channel, L-2 banked by user ruling; no VERIFY obliged. This read
  spends nothing (`R3`).

## 6. Findings

### Low (banks — the fix would trip the design test, so no bytes are supplied)

**L-1 — two rules' letters predate the byte-supplied-low channel and, read alone,
misroute it.** The channel (BC-1, in `E10` since `feacb86`) makes a record-supplied low
applicable immediately at zero budget, instruction layer included. Two adjacent letters
were not adjusted: **(a)** `E9`'s two-branch test ("has a valid independent FULL already
occurred? … yes → it is the fix round, and it obliges the VERIFY") admits no third
outcome, so `7463229` — a post-FULL layer change — is the fix round by `E9` alone,
obliging a VERIFY that `E10`'s channel says is not owed; **(b)** `R10`'s routing sentence
("…the bank takes the middle") routes by the 2026-07-29 ruling and predates the channel,
so a byte-carrying middle low read from R10 alone banks instead of applying. Downstream
decisions that go wrong: a future executor demands (or a reviewer expects) a VERIFY
after a byte application, or banks a low whose record already supplies its bytes. The
practical path is settled today — `E10`'s "the same free channel" inherits
not-a-round-spends-no-budget, R10 rule-3's parenthetical names the spend path
explicitly, and this round's three commit bodies plus the FULL's L-1 record the working
precedent; the exercised instance conforms. Not wording-level: the mistaken readings
change an obligation (a phantom VERIFY) and an action (bank vs apply), so `R9` does not
take it. No bytes supplied deliberately: any acknowledgment sentence added to `E9` or
`R10` adds a clause to a rule — the design test the collision rule says wins — so the
named fix cannot ride the free channel. Banks under R10: target `E9`'s budget-test
sentence and `R10`'s routing sentence; redeem when a batch next touches either; no
deadline — the seam's bite is the next post-FULL byte application, a touch event, not a
calendar moment. Same genus as `L-2li` (letter lags a landed rule), one clause further
out.

### Observations

**O-1 — the round invoked two just-landed clauses before this read, and the reliance
test resolves it.** `7463229` names the BC-1 channel; `784e49b` names R10 rule-3. Under
the amended relied-definition ("an outcome would change if the text changed"), neither is
reliance: the channel's authority is the standing 2026-07-30 (a) ledger ruling and rule-3
pre-existed verbatim as the riders-header tightening ③ (both re-read here at `c61d82d`),
so every outcome stands on pre-incorporation authority even if the incorporated text
were reverted. This read now closes the question for the final bytes; recorded because
the configuration — a round exercising its own amendments between candidate and closing
read — will recur, and the pre-existing-authority test is what made it clean this time.

**O-2 — this record tabulates member blob ids because `L-2r` now requires it.** The
first read for which the §1 table is rule-bound rather than convention (`v3-cold-read-
ae4df09.md` O-5 recorded the convention; the rule landed at `feacb86`).

**O-3 — the supersession-2 residue stands as dispositioned.** Member 8 is
blob-unchanged; the two in-carrier UNSIGNED lines and the ae4df09 W-1 scoping imprecision
ride under `R9` as recorded there. Confirmation, not a finding.

**O-4 — kind coverage worked where it was extended and stayed open where it was not.**
The round's four principal commits all self-name on-list kinds under amended `E8`; the
six pre-candidate bookkeeping commits' off-list self-descriptions remain the FULL's O-1
question, which is the user's.

## 7. Coverage disclosure (`R4`)

**Read in full:** the five changed members at the subject blobs — `CONSTRUCTION-
CHECKLIST.md` (156, also as standing instructions), `README.md` (36), `REVIEW.md` (227),
both stubs (5 each, the review stub also as standing-instruction entry); the full diffs
and bodies of `feacb86`, `7463229`, `784e49b`; `v3-review-full-feacb86.md` (202);
`v3-cold-read-ae4df09.md` (202); `HARNESS-RIDERS.md` at `784e49b` and its pre-migration
header at `c61d82d`; `HARNESS-LEDGER.md` (93).

**Sampled:** `v3-checkpoint-read-d58969d.md` and `v3-checkpoint-read-403fc9a.md` — the
§1 blob rows, read-in-full statements and blob-assertion lines only (grep-anchored);
`harness-layer-incorporation-round.plan.md` — Step boxes, read-set list, Notes;
`journal/layer-inc-2026-07-31.md` — structure, per-rider source table, rulings section;
`layer_path_check.py:25–45`; `6132828`'s body tail.

**Probed only:** the schema pack (ls-tree counts at `11d147e` and `784e49b` plus
diff-emptiness, no content read); the fixture runner (executed, output pasted, internals
unread); `.harness/review-pending.json`.

**Not verified:** that this read ran in a fresh context — a process claim, marked. The
card renders and chat replies behind the three rulings, beyond their in-repo records
(`R7` — ceiling stated, not a block). The five suites the three commit bodies report
green — not re-run here (the FULL re-ran them at the candidate; this read ran only the
fixture runner, per the `ae4df09` precedent); their binding force is prior rounds'
property. Fixture behaviour on any machine but this one.

**Ceiling:** whether the byte channel should reach post-FULL round time, and whether
`E9` should acknowledge it, are the user's questions under `R5`; what is checked here is
that the layer's text matches the repository, that the amendments are the fixes and
rulings their sources named, and that the bookkeeping around them did what its own rules
say.
