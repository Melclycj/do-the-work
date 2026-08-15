# FULL — `2d833cd..065a9b8` (rounds V3-B1-ROUTE-B + V3-E10-RIDER-REDEEM, plus the A1 V-5/V-8 errata)

| | |
|---|---|
| round | FULL, construction-side (`CONSTRUCTION-CHECKLIST.md` E1–E12 / R1–R10) |
| subject | `2d833cd1d103da7983e00471bb8d82e7d4276698..065a9b8f72d86c1baa3ea203459dd49a4a333953` |
| range content | three commits: `85c1225` (`V3-B1-ROUTE-B-v1`, kind: amendment) · `45858d5` (`V3-E10-RIDER-REDEEM-v1`, kind: amendment + redemption) · `065a9b8` (`V3-REVIEW-ERRATA-A1-V5-V8-v1`, kind: errata + ruling) — 6 files, all named by hand in §4.1 |
| answers | the whole of `v3-review-verify-7a08265.md` — `V-1`–`V-8` and its §4.3 process finding |
| **verdict** | **`CHANGES_REQUIRED`** |
| findings | 1 blocker · 3 low · 4 observations |
| record | this file; the execution side commits it (`R6`) |

**What this verdict does and does not mean.** The work itself is sound and I verified it deeply:
the revert restores a nine-member layer whose three copies agree to the byte and whose pin I broke
and watched fail; all eight of the VERIFY's findings are disposed of, each by the mechanism its
class demands; every number the errata corrected reproduces to the digit under my own commands.
The blocker is one sentence of forward-pointing accounting in `45858d5`'s body: it tells the next
layer read that one blob discharges every outstanding amendment-read debt, and that is false — the
decision-log round's amendment bytes live in `README.md`, which that instruction never touches. A
read that follows it voids an owed independent read silently. The sentence is immutable; the fix is
one durable correcting line, and nothing else in the range needs to move.

---

## 1. What this round is, re-derived (`R2`)

Nothing below is taken from the dispatch, which carried the range and nothing else.

| Question | Answer | Where I read it |
|---|---|---|
| Round(s) | **Two amendment rounds sharing one FULL** — `V3-B1-ROUTE-B` (revert of A1's route-(a) fix to route (b)) and `V3-E10-RIDER-REDEEM` (three rider dispositions) — plus the budget-free A1 errata `065a9b8` riding in the same window | all three commit bodies; `45858d5`: "下一次 FULL 的 subject 范围 `2d833cd..HEAD` 同时覆盖两轮" |
| Governing instructions | `CONSTRUCTION-CHECKLIST.md` E1–E12 / R1–R10, reached via the stub the dispatch names | stub `:3`; checklist header |
| Which leg (`E9`) | No valid independent FULL has occurred for either round — **this is it**, for both. The errata consumes nothing (`HD-23`, precondition checked in §4.3) | `E9`; `HD-23`; commit bodies |
| Verdict domain | FULL → `REVIEWED_NO_BLOCKER \| CHANGES_REQUIRED \| SPEC_GAP` | `R3` |
| Authorization | Revert ruling, three rider rulings and the errata ruling all carry registry entries (`HD-19`–`HD-23`) — unlike A1's `V-2`, no ruling in this range is chat-only. Preview cards and their approvals are chat-only (`E11` requires no committed copy); ceiling stated in §5 | `HARNESS-DECISIONS.md`; commit bodies |
| Dispatch (`E12`) | `.harness/review-pending.json` present, subject equal to my range verbatim, `dispatched_at` 11 s after the tip commit; branch has taken no commit since `065a9b8` | marker file; `git log 065a9b8..HEAD` empty |
| Ledger state | A2 still gated on the owed layer read + this review; both amendment rounds add read debt (§4.5) | `HARNESS-LEDGER.md:92-96` |

Worktree at `065a9b8`, `git status --porcelain` empty before and after every probe.

---

## 2. Implementation (`R3` — lead)

### 2.1 The revert (`85c1225`) does what it claims

- **Nine members, three copies, byte-identical order.** `E10`'s sentence enumerates exactly nine
  paths; `layer_path_check.LAYER` and `LayerMembership.EXPECTED` list the same nine in the same
  order. I extracted the sentence's paths with the guard's own token regex and compared by hand.
- **The pin bites at the current state (`R8`).** My probe, a different member from the executor's P1:
  removed supersession-1 from `LAYER` only →
  `2 failed, 44 passed` — `test_layer_equals_the_hand_written_membership` (tuple diff, value-level)
  and `test_every_member_is_scanned`. Restored from a sha256-checked scratchpad copy
  (`67c04010…` identical before and after); `git status --porcelain` empty.
- **The prose leg is exactly as exposed as disclosed.** Structural verification in place of
  re-running P2: repo-wide grep shows the only code binding `CONSTRUCTION-CHECKLIST.md` is the
  path-token scan of staged added lines, the membership tests, and `test_dispatch.py:470`'s
  *negative* assertion (the checklist must NOT appear in the dispatch prompt). Nothing reads its
  prose. The rider row and `HD-22` state this correctly.
- **`V-1`/`V-3`/`V-7` dissolve rather than close, as designed.** The decision log is out of the
  member set (so blob-level citation vs `§live`-only reading no longer collide; so `HD-nn` writes
  are no longer amendments); the inserted clause is deleted and
  `…paragraph-map.schema.json`. Its` is restored to the pre-amendment bytes `V-7` judged
  unambiguous. `V-2`'s two halves: `HD-7`'s title is accurate again, and the ruling that has no
  entry is superseded inside `HD-19`, which is the entry. Sweep: no `"these ten paths"` / `十成员`
  survives at the tip outside the journal's corrected history and the VERIFY record itself.
- **`HD-19` matches the landed bytes** — the (b) obligation sentence carries exactly what the entry
  says it carries (not a member · no amendment machinery reaches it · bytes are discipline (`HD-7`)
  · cited by section, never by blob), and it landed in the same commit as the nine-member sentence.

### 2.2 The rider round (`45858d5`) redeems what it says it redeems

- **`R10` held:** `E2-FC` and `E10-crit` rows deleted in the same commit as the clauses that
  discharge them; `E10-sync` rewritten in place, not deleted, because its defect survives — the row
  now carries the per-touch discipline and the `HD-22` deadline. 18 rows → 16, recounted by hand.
- **`HD-20`** is carried by the new free-channel exception, and the clause sits *inside* the channel
  it restricts, so the mechanism decides correctly whatever the reader arrives through (but see
  `L-1`: `R10`'s routing summary was not updated and now contradicts it in wording).
- **`HD-21`** is carried by the membership-question sentence. The one-word deviation from the
  approved card ("this sentence" → "the membership sentence") is disclosed in the body with its
  reason; the landed wording is the one that avoids the `V-7` antecedent class, and the ruling text
  in `HD-21` matches the landed bytes, not the card's.
- **`HD-22`'s stated ground reproduces:** a naive path-token parse of the `E10` bullet yields **10**
  items (nine members + the decision log named by the (b) sentence) — I ran it. A parser guard over
  that prose would indeed bind on punctuation.
- **Route-b itself obeyed the three-site discipline** the rewritten row demands: membership sentence,
  `LAYER`, `EXPECTED` changed together and named in the commit body.

### 2.3 The errata (`065a9b8`), every figure re-derived (`R2` — no reported number accepted)

- **`V-5` block — exact.** Ten-member **blob** totals at `fd058aa`, from `git show` per member:
  **1,125 lines / 75,424 chars / 81,048 bytes** — all three reproduce. The 176 delta reproduces
  from the other side: every member blob carries CR=0 (git normalizes; `core.autocrlf=true`), the
  checklist blob is 176 lines, and the CRLF worktree copy adds exactly one CR per line:
  75,424+176 = 75,600 and 81,048+176 = 81,224 — the worktree figures §14.3 originally printed.
  `HARNESS-DECISIONS.md` at 165 L / 8,292 ch / 13,415 B, exact.
- **`V-6` block — exact.** `check-chk-governance` exists as exactly **3** files, all under
  `assurance/shadow/{run-p3,round-2/run-p3,round-3/run-p3}/control/`; **0** under
  `assurance/runs/`; the closed-run set is the eight directories the block implies. Distinct
  `check-chk-*` stems: runs-only **78**, repo-wide **89**, **90** counting the `check-results`
  aggregate.
- **`V-8` block — the supplied bytes landed verbatim** ("两处就地加注、两处另加更正块；错的数字一律
  不删"), the wrong original line stays visible above it per the `2c3cc99` discipline, and the block
  self-reports the §4.3 over-read and rehangs the four A1 corrections on `HD-23`.
- **`HD-23` placement is right:** the criterion sentence has no other carrier (`E9`'s text does not
  hold it; the 2026-08-04 ledger ruling is narrower and stays put per `HD-8`), so `§live` under
  `HD-2`'s test; the ledger header routes new rulings to the decisions file, and it went there.
- **No reviewed conclusion moved.** Each block corrects a measurement convention, a stated reason,
  or the errata's own discipline description; each states, and I confirm, that the conclusion it
  annotates is unchanged.

### 2.4 Battery, run at the tip on a clean tree

```
ResearchSystem/tooling$ python -m pytest -q            → 632 passed in 110.32s
python Thesis/Work/Tooling/repo-audit.py               → RESULT: clean (exit 0)
python tooling/hooks/ledger_cap_check.py               → exit 0
python tooling/hooks/layer_path_check.py               → exit 0
git status --porcelain                                 → empty
```

---

## 3. Findings

### Blocker

#### `B-1` — `45858d5`'s read-debt consolidation drops the `README.md` leg, and the next layer read that follows it under-covers silently

**Location.** `45858d5` commit body, 欠账与预算 paragraph: "独立读义务并入下一次层 read——读当前
`CONSTRUCTION-CHECKLIST.md` blob 即一次覆盖 `C1` 以来全部未读 amendment 文本（decision-log 轮 ·
route-b `85c1225` · 本轮；`fd058aa` 的文本已被取代无对象）。"

**Ground truth it violates.** The decision-log round (`cfc6a91`) amended the layer in
`document-harness/README.md` and **did not touch the checklist** (`git show cfc6a91 --stat`: seven
files, no `CONSTRUCTION-CHECKLIST.md`); its own body says so ("本轮改了 `E10` 成员（README），欠开轮
cold read 与一次独立评审"). `README.md`'s current blob is `dd1c7c3e` (from `cfc6a91`); the last
recorded layer read (`v3-checkpoint-read-838c413.md`, 2026-08-04) covers README at the **old** blob
`f3a31208`, so no citation discharge exists. Reading the current checklist blob therefore covers the
`C1`, route-b and rider amendments — all checklist-resident — and **not** the decision-log round's.
The claim is falsifiable by one command that was not run (`E3`), and what it mis-states is the scope
of an owed verification act (`E10`'s independent amendment read), whose subject includes the
`HD-1`/`HD-5` carrier text — the very lines every round's opening obligation now hangs on. The
sentence is the most recent, most specific statement of how the debt gets paid; the accurate sources
(`cfc6a91`'s body; the ledger's `欠 step 8` line, which names the round but no file) are older and
less specific, so the wrong one is the one a future session will reach for.

**Minimum fix.** The body is immutable; the fix is **one durable correcting line where the next
read's scoper will look** — the natural site is the ledger's `欠 step 8` bullet (a ledger-only edit,
budget-free under the 2026-08-04 ruling): state that the owed layer read covers the current
`CONSTRUCTION-CHECKLIST.md` blob **and** `README.md` blob `dd1c7c3e` (per `cfc6a91`), and that
`45858d5`'s "one blob covers all" sentence is not to be relied on. A journal correction block naming
the same facts is an acceptable alternative site. Nothing else in the range needs to change.

### Low

#### `L-1` — `R10`'s routing summary now contradicts the `HD-20` exception it points into

`R10` still reads "a middle low whose record supplies the exact bytes or names the content takes the
`E10` free channel, **never the bank**"; the free channel it routes into now answers, for an
`E2`-frozen path, "banks until [the ruling] exists". The mechanism resolves correctly — the
exception lives inside the channel being taken, and `HD-20` outranks the stale summary — but a
reader applying `R10`'s sentence without entering the channel mis-routes the one path that is both
frozen and a member. The fix adds a qualifier to `R10`, which is a clause on a rule: `E10`'s design
test wins over the free channel, so these bytes cannot be applied now — **banks**, redeem-when =
the next batch touching `R10`'s text or the `E10` free-channel sentence.

#### `L-2` (wording-level, `R9`) — the errata's header block cites a `§14.6` that does not exist

`journal/batch-a1-2026-08-08.md:775`: "本节四条更正与 §14.6 三条自此站在 `HD-23` 上" — the journal
ends at §14.5 (878 lines; heading grep confirms no §14.6). The "三条" are the three correction
blocks this errata placed at the §14 header, §14.2 and §14.3; each is marked `(V-x, 2026-08-08)`, so
the accurate fact is recoverable from adjacent text and the commit body. No actor's action changes.
Bytes: replace "§14.6 三条" with "本 errata 的三条更正块". Rides the next batch touching the
journal; no round, no read.

#### `L-3` (wording-level, `R9`) — the `V-5` block's validity interval is wrong at both endpoints under git range semantics

Same file, §14.3 correction block: "「十成员」只对 `fd058aa..85c1225` 区间为真". As a git range that
set excludes `fd058aa` and includes `85c1225` — the exact complement of the truth at both ends: the
layer is ten members **at** `fd058aa` (where the block's own figures were measured, "测于
`fd058aa`") and nine **at** `85c1225`. Adjacent text recovers the intent. In an errata whose whole
lesson is that numbers must carry their measurement conventions, the interval should too. Bytes:
"自 `fd058aa` 起、至 `85c1225` revert 止". Rides with `L-2`.

### Observations

- **`ob-1`** — Neither amendment round records an opening cold read, a citation, or a user waiver
  (`E10`: owed at each round's opening unless waived). The waiver, if given, is chat-only — a hint,
  not a block (`R7`); stated here so the pattern is visible. Related: the ledger's owed-read line
  still names only `C1` and the decision-log round; after this range the outstanding set is four
  amendments over two blobs (checklist + README) — `B-1`'s fix is the natural place to make that
  line current.
- **`ob-2`** — Two rounds share one FULL, declared to the user on the preview card per `45858d5`'s
  body. `E9`'s caps are per-round maxima; one review covering two disjoint-purpose amendment rounds
  under-consumes rather than escapes, and the disclosure duty was met. Approval is chat-only (`R7`).
- **`ob-3`** — `HD-23`'s wording covers "journal **数字** 更正"; the errata's `V-8` block and the
  §4.3 rehang correct the journal's *description of its own correction discipline* and its *cited
  authority* — not numbers. Benign here: both landed inside this FULL's subject range (the ruling's
  own precondition) and are now reviewed; noted because the next journal errata will read `HD-23`'s
  "数字" and must decide whether the class includes corrections *to the correction apparatus*. The
  question and answer are the user's (`R5`).
- **`ob-4`** (`R5`, the shape) — Unlike the rounds `R5` warns about, this range **removed**
  machinery: route (a)'s member entry, guard line and test line are gone, and the three governance
  questions the VERIFY opened died with them; the rider round resolved two banked debts by clauses
  and re-scoped a third without adding a guard (`E6` honored, per `HD-22`). Net instruction-layer
  growth for the whole range: one exception clause, one obligation sentence, one membership-question
  sentence.

---

## 4. Boundary and process (`R3` — second)

**4.1 Change boundary — held.** Classified by hand from `git diff --name-status` over the range:
`HARNESS-DECISIONS.md` · `HARNESS-RIDERS.md` · `document-harness/CONSTRUCTION-CHECKLIST.md` ·
`document-harness/journal/batch-a1-2026-08-08.md` · `tooling/hooks/layer_path_check.py` ·
`tooling/tests/document_harness/test_precommit_checks.py`. No product path, no run directory, no
ledger edit, no plan, no schema, no contract.

**4.2 Frozen surface (`E2`) — intact.** No path under `schema/document-assurance-v3/` or
`contract/` appears in the range; `paragraph-map.schema.json` — the one path that is both frozen
and a member — is untouched, and the round that wrote the `HD-20` clause about it did not write it.

**4.3 `E9` — accounted, with one scope note.** A1's budget was exhausted before this range; the
errata is the only commit touching A1's product and rides `HD-23`, whose precondition — the
correction lands in the next review's subject range — is satisfied by this very review. The two new
rounds carry no FULL before this one, so nothing in the range could be a fix leg; both rounds'
kinds are named (`E8`), and from my dispatch to this record the branch has taken no commit. The
scope note is `ob-3`.

**4.4 `E8` — form.** Titles `V3-B1-ROUTE-B-v1` / `V3-E10-RIDER-REDEEM-v1` /
`V3-REVIEW-ERRATA-A1-V5-V8-v1`, each naming its kind in the body's first line; explicit-path
staging is asserted and consistent with the per-commit file lists; dense bodies, no trailers.

**4.5 `E10` debt — real, disclosed, and mis-consolidated (`B-1`).** Outstanding independent
amendment reads after this range: `C1` (`55fe4e9`), the decision-log round (`cfc6a91`, README leg),
route-b (`85c1225`), the rider round (`45858d5`) — the checklist-resident three are discharged by
one read of the current checklist blob; the README leg needs `dd1c7c3e` read too. `fd058aa`'s text
is superseded; route-b's "读它已无对象" is flagged in its body as judgment, not rule, and I leave it
to the next read as it asks. Neither this FULL nor anything in it banks as any of those reads
(`E10`: an amendment read's subject is the amendment text, never the work it governs).

**4.6 `E12`/freeze — held.** Marker present with my exact range as subject; `review_freeze_check`
will refuse any non-record path while it stands; the record you are reading is the only path this
session writes.

---

## 5. Honesty ceilings (`R4`)

1. **Read in full:** `CONSTRUCTION-CHECKLIST.md` (worktree = HEAD) · `v3-review-verify-7a08265.md`
   (all 378 lines) · `HARNESS-DECISIONS.md` · `HARNESS-RIDERS.md` · `HARNESS-LEDGER.md` ·
   `hooks/layer_path_check.py` · `hooks/review_freeze_check.py:1-60` · the complete diffs and
   bodies of all three subject commits · `cfc6a91`'s stat and body · `55fe4e9`'s stat.
   **Sampled:** the journal — §12.4, §13.4, §14 complete, heading map of the rest; the ~640 other
   lines not read. `test_precommit_checks.py` — the `LayerMembership` region and `:150-215`.
   **Not read:** `EXECUTION.md`, `REVIEW.md` (unchanged in range), both plans, the other review
   records except where named, `HARNESS-DECISIONS-archive.md`.
2. **`UNVERIFIABLE`, not folded into supported:** that the preview cards said what the bodies say
   they said, and that the user's five rulings (`HD-19`–`HD-23`) were given as recorded — I read
   committed records only; every ruling now has an entry, which is evidence of process, not proof of
   the conversation. Likewise "fresh context" for this session is marked, not verified.
3. **Structural verification stood in for one mutation:** P2's negative result (prose leg unguarded)
   I confirmed by exhaustive grep of what binds the checklist, not by re-running the deletion; the
   executor's own P2 and the VERIFY's P3 are the recorded mutations of that leg. My one live
   mutation (§2.1) proves the pin binds; it does not prove a path-resolution scan is sufficient
   guarding for an instruction charter — no one claims it is (`E10-sync` row).
4. **Counting rules:** member figures are committed-blob bytes/decoded-chars/`\n`-counts at the
   named revision; stem counts are distinct basenames over `git ls-files` under the stated prefix;
   the naive-parse count uses the guard's own `TOKEN`/`PATHLIKE` regexes over the `E10`–`E11` span.
   All commands run at `065a9b8` on a clean tree.
5. **What I did not re-judge:** A1's measurement layer beyond the errata's corrected figures; the
   FULL/VERIFY verdicts of prior rounds; whether route (b) is the right design (`R5` — the user
   ruled it; my subject is that the landed bytes do what the ruling says).
