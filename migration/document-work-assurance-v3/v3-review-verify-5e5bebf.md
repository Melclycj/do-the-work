# VERIFY — `7d7eff5..5e5bebf` (round `CORE-SET-SIGNATURE`, batch `CORE-SET`, round 2, fix leg)

Independent targeted VERIFY. Subject received as one range and nothing else (`R2`); round identity,
budget, authorization, obligations and every figure below are re-derived from the repository, and
no figure reported by the subject is accepted as given. Standing instructions:
`migration/document-work-assurance-v3/v3-harness-review-contract.md`, a stub superseding to
`document-harness/CONSTRUCTION-CHECKLIST.md` — read whole at the subject tip (`wc -l` → 257, both
sides), and it is its own counterpart. `HARNESS-DECISIONS.md`'s header mechanism block (lines
1–29) and `§live` (lines 30–162) read whole at the tip: eight entries — `HD-59` `HD-44` `HD-41`
`HD-36` `HD-35` `HD-34` `HD-23` `HD-9`, unchanged in membership from what the FULL recorded at
`a554c0b`.

**Verdict: `REVIEWED_NO_BLOCKER`.** 2 lows, 2 observations. The accepted finding `L-1` is answered
correctly and every factual claim in the correction is exact; the residual is that the FULL's
minimum fix named a carrier this commit could not write, and that carrier is still empty.

---

## 1. Subject, budget and boundary, re-derived

```
$ git rev-parse HEAD                        -> 5e5bebf09ecfe37e58d99730dee1afd39c8ad1db
$ git status --porcelain                    -> ?? .goals/     (untracked only)
$ git rev-list --count 7d7eff5..5e5bebf     -> 1
$ git rev-list --count origin/main..HEAD    -> 47             (nothing pushed, E8)
$ cat .harness/review-pending.json          -> subject 7d7eff5..5e5bebf, dispatched 2026-08-26T14:32:02+00:00
```

One commit. The freeze window is intact and re-derived rather than assumed: the marker names this
range and the branch tip *is* the subject, so no commit has landed since dispatch (`E9`).

**`E9`, derived rather than read back.** The round's review-side events, in order and each pinned
to the commit that made it real: opening cold read at `fc9c008` (`v3-cold-read-d3ba221.md` — a
read, no verdict, no budget, `R3`); FULL on `8e576a1..a554c0b`, record landed `7d7eff5`
(`v3-review-full-a554c0b.md`, `REVIEWED_NO_BLOCKER`, 4 lows / 3 observations); this fix at
`5e5bebf`. `E9`'s own question — has a valid independent FULL already occurred? — answers yes, so
this is the fix leg and not a pre-submission correction, it consumes the round's one user-approved
fix, and it obliges this VERIFY. The commit self-classifies exactly that way and the
self-classification is correct rather than a renamed round. No commit landed between the FULL's
dispatch and its record (`7d7eff5`'s parent is `a554c0b`), which is `E9`'s no-commit-but-the-record
rule met on the leg before this one.

**Change boundary, classified by hand.**

```
$ git diff --name-status 7d7eff5 5e5bebf
M  HARNESS-RIDERS.md
M  document-harness/journal/core-set-signature-2026-08-26.md
$ git diff --stat 7d7eff5 5e5bebf   -> 2 files changed, 32 insertions(+)
```

Purely additive — zero deleted lines across the range, which is `HD-59`'s form met mechanically and
not merely asserted. Neither path is an `E10` member; neither is a byte `E2` freezes. `E2`'s
frozen surface is untouched: contract v4 is `5dfb7b64265c821c715f23de52824beeadea3405` at both ends
of the range, and `git diff --name-status 7d7eff5 5e5bebf -- schema/document-assurance-v3/` returns
nothing. No code, no tests, no schemas.

**Authorization, from committed state only.** The routing that activated the fix leg — `L-1` to
the fix, `L-2`/`L-3`/`L-4` to the bank — is a user ruling of 2026-08-27 recorded in the commit body
and in the journal paragraph itself. It is not chat-only load-bearing material (`R2`), because both
carriers are committed; that a user actually made it is a process claim, marked and not verified
(`R4`), the same treatment the FULL gave the `E11` card. It correctly took no `HD` entry: `R10`
puts the spend-versus-bank choice with the orchestrator per round, so it binds no later round and
narrows no standing ruling, and the register's own admission test is therefore not met.

---

## 2. The accepted finding, answered — every claim in the correction reproduced

`R3` puts the implementation first. The repair is one paragraph of prose, so its implementation
*is* its factual accuracy. Each figure below is my own run, not the correction's number read back.

### 2.1 The count is three, and three is complete for the round

The correction's core claim is that `07ef526` edited three `E10` members, not two. Per-commit file
lists over the whole round, so the claim is tested at round scope and not only at the commit the
finding named:

| commit | `E10` members touched |
|---|---|
| `07ef526` | `contract/Document-Work-Assurance-Contract-v4.md` · `document-harness/CONSTRUCTION-CHECKLIST.md` · `document-harness/README.md` |
| `cb4f22f` | none (`CONSTRUCTION-INDEX.md`, `CORE-SET.md`, `HARNESS-RIDERS.md`) |
| `66dfd30` | none (the journal) |
| `a554c0b` | none (two registers, the plan) |
| `5e5bebf` | none |

**Three, and no fourth anywhere in the round.** The correction is exact and it is complete — it
would have been possible to fix the reported instance and leave a sibling member uncounted, and
there is no sibling to leave.

### 2.2 The blob move and the citation baseline

```
$ git rev-parse 8e576a1:contract/Document-Work-Assurance-Contract-v4.md
  -> dfc983d2e3d9fb5ca67b053a16fcfb0e6715b11a
$ git rev-parse 07ef526:contract/Document-Work-Assurance-Contract-v4.md
  -> 5dfb7b64265c821c715f23de52824beeadea3405
$ git cat-file blob dfc983d2… | wc -l    -> 342
```

Both blob ids and the 342 are exact. `v3-cold-read-d3ba221.md` §2 member row 8 records the
contract at `dfc983d2…`, 342 lines, 22,185 bytes, and its §2 states in as many words *"All nine
were read end to end regardless"* — so a recorded end-to-end read does exist, at the old blob, and
`E10`'s citation clause ("a member whose blob is **unchanged** since a recorded end-to-end read of
it is covered by citing that record") therefore stops covering it the moment the blob moved. The
correction quotes that clause accurately and applies it correctly. Its "at per-member digest cost"
is `E10`'s own phrase for what a deferred layer application owes, used as written.

### 2.3 The two priors the correction leans on, checked rather than taken

- **`HD-57`** (`HARNESS-DECISIONS.md:184`, `status: implemented`) — its 后果 clause reads *"v4 与
  checklist 的成员编辑欠独立 read，随下一轮开轮冷读"*. The correction's claim that `HD-57` named
  the contract explicitly the last time v4 was written under an `E2` ruling is exact.
- **`CONSTRUCTION-LEDGER.md`** — the round-1 `CORE-SET-LAYER` entry carries *"下轮冷读若再走窄形态，
  基线须按 `E10` 取「自某一份已记录整读以来未变」…（本轮开轮读的 `O-1` 即栽在这里）"*. The claim
  that round 1's own opening read failed on this citation-baseline class is exact, and it is why
  the finding is worth a leg rather than a row.

### 2.4 Form — `HD-59` met, and the substitution disclosed rather than made silently

`HD-59` forbids rewriting a committed conclusion in place and admits *"原处另起一段紧挨着它，原文
逐字留着"*. The diff is 32 added lines and zero deleted, so the original bullet and both prior
commit bodies stand byte-for-byte. The paragraph sits immediately after the bullet it corrects, in
§9, which is one of the two locations the FULL's `L-1` named.

The FULL's **minimum fix** named a different carrier — *"one sentence in the closeout record"*. The
executor did not write there and said so in the paragraph and again in the commit body, on the
ground that the closeout is the orchestrator's commit. That is `E9`'s "exceeding an approved fix
boundary requires saying so, never silently" met from the other direction: a boundary the executor
declined to reach, disclosed rather than quietly substituted. The consequence is `V-1`.

### 2.5 The three banked rows, each figure re-measured

| row | claim | my run | verdict |
|---|---|---|---|
| `index-repo-count` | `git ls-tree -r --name-only` = 391 at `cb4f22f` | **391** | ✓ |
| | = 392 at `a554c0b` | **392** | ✓ |
| | = 393 at `7d7eff5` (the row's own base) | **393** | ✓ |
| `archive-header-selfcount` | `HARNESS-DECISIONS-archive.md` = 411 lines at `a554c0b`, header says 404 | **411**; header line 7 reads **404** | ✓ |
| `sig-write-once` | `append-only`/`write-once` return zero hits over the round's four commit bodies, the journal, the plan and the new carrier, measured at `7d7eff5` | both greps exit 1 (no match) over exactly that scope | ✓ |
| | `HD-60` names the *Signature semantics* sentence as one of its three sites | `HD-60` 裁决 clause: frontmatter `signature_owner:` · the header warning block's sentence pointing at the decision log · the closing "lives as an `HD` entry" sentence | ✓ |
| | `HD-60`'s exclusion list is 接口 / enum / invariant / 版本边界 / 依赖图 | archive entry, 授权**不含** clause, word for word | ✓ |
| | both carrying authorizations retired | `HD-60` and `HD-61` both `status: retired`, in `HARNESS-DECISIONS-archive.md` | ✓ |
| | `append-only` is the term every prior carrier uses | `N0-record.md:7` · `N1-record.md:7` · `N2-record.md:9` and `:635` all read "append-only log" | ✓ |
| bank size | 19 → 22 | rows at `7d7eff5` = **19**; at tip = **22** | ✓ |

Every path token newly written into the three rows resolves — checked by hand, because no machine
does (§3, `O-2`): `contract/Document-Work-Assurance-Contract-v4.md`, `CONSTRUCTION-INDEX.md`,
`HARNESS-DECISIONS-archive.md`, `CONTRACT-V4-SIGNATURE.md` resolve at the root;
`N0-record.md` / `N1-record.md` / `N2-record.md` resolve as unique tracked suffixes, at
`migration/document-work-assurance-v3/N0/N0-record.md` and its two siblings.

**`R10` conformance of the three rows, clause by clause.** Each names its target file or clause
(not "对应文件"): the contract's *Signature semantics* block, `HARNESS-DECISIONS-archive.md:7`,
`CONSTRUCTION-INDEX.md:22`. Each carries a source (`v3-review-full-a554c0b.md` `L-2`/`L-3`/`L-4`).
`sig-write-once`'s routing is `HD-20`'s rather than `R10`'s ordinary channel, correctly: the bytes
sit on a path `E2` freezes, so however appliable they are they bank until an `E2` recorded ruling
exists, and its deadline — the next `E2` write window on v4, or the next re-signature — is outside
the round that wrote the row, which `R10` requires. `archive-header-selfcount` and
`index-repo-count` carry no deadline, which is right: the FULL named no downstream decision for
either, so `R9`'s wording-level tier applies and there is no moment at which their value expires.
Neither is design-shaped, so naming a *batch* rather than a round-eligible surface as their
redeem-when is correct.

I checked whether `L-3` and `L-4` should instead have taken `E10`'s free channel, since both are
below must-fix and the FULL's text names the content. They should not: the FULL routed both
explicitly to the bank in its own findings ("rides the next batch touching this file", "no
deadline"), and their targets are neither `E10` members nor `E2` bytes, so `R10`'s "the bank takes
what is left" governs. The standing free-channel-versus-`R9` ambiguity that could have made this
contested is already banked as rider `wl-route` and is not re-opened by this diff.

### 2.6 Battery and guards, re-run at this tree rather than read back

```
$ python -m pytest -q          (from tooling/)   -> 854 passed in 181.50s   exit 0
$ python tooling/hooks/layer_path_check.py       -> exit 0
$ python tooling/hooks/candidate_path_check.py   -> exit 0
$ python tooling/hooks/review_freeze_check.py    -> exit 0
```

**854 matches the subject's claim exactly.** The 190.06s the commit body records is wall-clock and
not a figure anything turns on.

**Mutation-tested against the real staged diff, in a scratch clone so the subject tree was never
touched (`R8`).** Running the two path guards on a clean worktree proves nothing — both read
`git diff --cached`, so with nothing staged they return exit 0 on empty input. I reproduced the
commit's own staging (`git checkout 7d7eff5 && git cherry-pick -n 5e5bebf`) and ran them there:

| state | `candidate_path_check` |
|---|---|
| the diff as committed (negative control) | exit 0 |
| a nonexistent path token added to the **journal**'s added lines | **exit 1**, names the token |
| the same token added to **`HARNESS-RIDERS.md`**'s added lines | exit 0 — **blind** |

The guard binds on the journal half of this diff and is blind on the rider-bank half by
construction: `caller.DEFAULT_RECORD_SURFACE` exempts `HARNESS-RIDERS.md` as a record surface,
because a record quotes the broken paths it reports. `layer_path_check` contributes nothing here at
all — neither staged path is in its `LAYER`. Both exits are honest; what they cover is `O-2`.

---

## 3. Findings

### `V-1` — the closeout still owes the sentence the FULL's minimum fix named, and its carrier is empty

**Location.** `CONSTRUCTION-LEDGER.md` — no round-2 entry exists.
`git log -1 --format='%h %s' -- CONSTRUCTION-LEDGER.md` → `a19c9b4
V3-LEDGER-CORE-SET-ENTRY-TRIM-v1`, which is before this round's base.

**Ground truth.** The FULL's `L-1` minimum fix reads *"One sentence in the closeout record naming
contract v4 as a third edited member whose bytes ride the next read of this layer"*, deadline
*"round 3's opening"*. The executor correctly declined to write the orchestrator's commit and said
so. But the substitution is not neutral, because the ledger is demonstrably the carrier a next
round sizes from for exactly this fact: round 1's instance of it lives there and nowhere else —
*"本轮五个在仓成员全部改动，欠独立 read 随下轮开轮"*, in the `CORE-SET-LAYER` block. A reader
opening round 3 `CORE-SET-CODE` follows the batch's ledger entries, finds round 1's member-read
debt stated and round 2's absent, and has no reason to open a superseded round's journal §9.

**Downstream decision.** Round 3's opening cold read sizes its member-read obligation. If round 2's
ledger entry omits the contract, or repeats "two", the finding is un-fixed at precisely the moment
its deadline lands. The mechanical blob comparison still recovers it — which is why the FULL filed
a low and why this is a low too — but that is the second-mistake margin the FULL already spent
once.

**Minimum fix.** The round-2 closeout ledger entry states three edited members, contract v4 named,
bytes riding the next read of this layer at per-member digest cost. It is not a round and spends no
budget; it is the closeout commit doing what it was always going to do. **Deadline: round 3's
opening**, unchanged from the FULL's.

### `V-2` — §9 now contradicts itself two bullets apart, and the falsified half is the budget

**Location.** `document-harness/journal/core-set-signature-2026-08-26.md:173-175`, the last bullet
of the same §9 this diff edited: *"**`E9` is untouched.** No valid independent FULL has occurred on
this round, so both work commits are candidates by `E9`'s own test, the fix leg is unspent, and no
VERIFY is owed. The budget this round has spent is zero."*

**Ground truth.** All four assertions are false at the tip, and this diff is what made the last
three false. A valid independent FULL occurred and its record landed at `7d7eff5`; the fix leg is
spent by `5e5bebf`; a VERIFY is owed and is this document; the budget spent is one FULL plus one
fix. The paragraph inserted **two bullets above** says so itself — *"this round's one user-approved
`E9` fix leg"* — so a reader going down §9 in order meets the consumption and then, one bullet
later, meets "the budget this round has spent is zero".

**Not a `HD-59` breach, and I checked before writing this.** `HD-59` requires forward correction,
which `5e5bebf`'s own commit body supplies in as many words ("It consumes round
`CORE-SET-SIGNATURE`'s one user-approved fix under `E9`"), and a new commit is one of the four
forms `HD-59` admits. Nor was correcting it inside the executor's approved boundary: the fix was
routed to `L-1` and nothing else. The defect is that the adjacent-paragraph form was chosen for one
bullet of §9 on the express reasoning that *"round 3's opening cold read sizes itself from these
records"*, and the neighbouring bullet — which those same records make false — did not get it.

**Downstream decision.** `E9` says *"Never self-classify which round consumed what: every recorded
escape from the cap was a renamed round."* A committed statement that this round spent zero budget
is the exact artifact under which a cap escape goes unnoticed, and it now sits in the round's own
journal. Concretely: the closeout must state what round 2 spent, and §9 answers "zero".

**Minimum fix.** One clause in the closeout — or an adjacent paragraph in §9 in the same `HD-59`
form the fix already used — recording that the bullet was true when written at `66dfd30` and that
the round went on to spend one FULL and one fix. Rides `V-1`'s commit; no separate carrier needed.
**Deadline: the closeout**, because that is where the budget figure is written.

---

## 4. Observations (`R5` — the conclusion is the user's, not mine)

### `O-1` — `R10`'s "no narrative" clause and the bank's practice have now diverged in writing twice

`R10` reads *"One row per rider: what · redeem-when · source; no narrative — the source records
hold it."* Measured at the tip with `awk` over each row line, the three rows this diff adds are
**2,169**, **1,006** and **1,032** characters; each restates its FULL finding's reasoning, and
`sig-write-once` additionally re-argues `HD-60`'s
exclusion list, the `HD-35`/`HD-40` re-signature precedent and the four `N`-record citations. So do
all nineteen rows that preceded them — this diff is the newest instance, not the origin.

It has been recorded once before and routed nowhere: `v3-checkpoint-read-136f27f.md` §3 noted a row
carrying *"two sentences of deadline history into a bank `R10` `:172-173` says holds no
narrative"*, filed it under "recorded only that I looked", and observed that *"that tension
predates and outlives this round"*. That is the same shape as rider `e9-pair-budget`, which was
recorded twice with no route before the third recording became its home.

I am deliberately not prescribing. Either direction is design — tightening the rows means deleting
recorded reasoning whose source records are review documents a caller does not carry, and relaxing
the clause changes what `R10` requires — so `E10` opens a round for it either way, and `R5` puts
the question with the user rather than with me. What I can say is that the clause has now been
measured against practice twice and routed nowhere twice.

### `O-2` — the guard evidence in the commit body is true and covers less than it reads as covering

The commit body pastes *"layer_path_check and candidate_path_check both exit 0"* beside the battery
figure, in the position `E3` reserves for tool output. Both exits are real. What they establish, on
my mutation runs in §2.6:

- `layer_path_check`: **nothing about this diff.** Its `LAYER` is `E10`'s nine members and neither
  staged path is one, so it had no input. Its exit 0 is structurally guaranteed here.
- `candidate_path_check`: **the journal half only.** It fired red on a nonexistent token added to
  the journal and stayed green on the identical token in `HARNESS-RIDERS.md`, which
  `caller.DEFAULT_RECORD_SURFACE` exempts by design — records quote the broken paths they report.

So the three new rider rows' path tokens are held by no machine at all. I resolved all seven by
hand and all seven are good. The exemption is deliberate and documented in
`candidate_path_check.py`'s own docstring, and rider `freeze-audit` already sits on the deadlock
that motivates it — so this is not a defect, and `E6` says a fix needing new machinery is the
signal to re-question the guarded thing rather than to add a guard. Stated because the pasted line,
read as a whole, suggests coverage of a diff that one guard never saw and the other saw half of.

### Two things checked and deliberately not filed

- **`E8`'s "one dense paragraph".** This commit body is seven blank-line-separated blocks. So is
  every comparable one in this repository — `a554c0b` has five, `0f0498f` six, `5873840` sixteen —
  while the three single-purpose candidates of this round have one apiece. The body carries no
  bullets and no trailers, which is what the clause is defended against. Filing a divergence this
  settled would inflate a non-blocking finding, which `R3` forbids.
- **`O-3` of the FULL** (the plan's stale resume pointer at `document-harness/plans/core-set.plan.md:679-687`,
  still `[ ]` at step 9 and still pointing at a dispatch that happened at `07ef526`/`cb4f22f`).
  Unchanged at this tip, correctly — the fix's boundary was `L-1`, and the FULL flagged it to ride
  the closeout rather than filing it. Re-stated here only so the closeout has all three of `V-1`,
  `V-2` and it in one place.

---

## 5. Coverage (`R4`)

**Read in full** (line counts are `wc -l`): `document-harness/CONSTRUCTION-CHECKLIST.md` (257,
both sides) · `migration/document-work-assurance-v3/v3-harness-review-contract.md` (6) ·
`v3-review-full-a554c0b.md` (396) · the round journal (175, including the whole of the standing
text the diff did not touch) · `HARNESS-RIDERS.md` (32, all twenty-two rows) ·
`HARNESS-DECISIONS.md` lines 1–162 (header block and `§live`) · the `HD-57`, `HD-60` and `HD-61`
entries · the complete diff of the range · the commit body ·
`tooling/hooks/candidate_path_check.py` (155) · `tooling/hooks/layer_path_check.py` `LAYER`,
`PATHLIKE`, `unresolved_tokens`, `added_lines_by_path` and `check`.

**Sampled:** `v3-cold-read-d3ba221.md` (408 lines; §1–§2 at 70–124 read directly, plus the member
digest table at 371–373 and grep hits at 24, 89–96, 144–151, 170–185, 223–243 and 264 — the bulk
unread) · `CONSTRUCTION-LEDGER.md` (the `CORE-SET` batch block at 165–176 and the
`dispatch-economy` block at 158–162; the file's other ~600 lines only by grep) ·
`document-harness/plans/core-set.plan.md` (the resume pointer and step 9 only) ·
`tooling/rsclib/document_harness/caller.py` (the surface defaults and `load_scan_surfaces`) ·
`v3-checkpoint-read-136f27f.md` (§3 only, for `O-1`'s prior recording).

**Probed only:** contract v4 (lines 13–17, the *Signature semantics* block, to place
`sig-write-once` against `HD-60`) · the four `N`-record signature-log lines ·
`review_freeze_check.py` (run, not read) · the test suite (run, not read).

**Marked as process claims, not verified (`R4`):** that a user made the 2026-08-27 routing ruling ·
that the executor ran cold and ended while waiting on the suite, so that the orchestrator committed
its bytes unedited. Both live outside the tracked tree. The second is `E1`-relevant and I note
what committed state does show: the orchestrator ran the battery and the guards over the executor's
bytes and reported the result, which is measurement and not a verdict, and both roles are the work
side, which `E1`'s own heading binds in one breath. Whether the four holdings disclosure `E1`
requires of a round standing in the middle is owed here is not decidable from the tree — no round
journal entry states them for the fix leg — and it is the orchestrator's to make at closeout, not
mine to conclude.

**`UNVERIFIABLE`, stated rather than folded into supported (`R4`):** whether the fix's paragraph is
byte-identical to what the cold executor wrote before its session ended. The commit body asserts
"No byte of its work product was edited here", and nothing in a single-commit tree can confirm or
refute it — there is no intermediate object to compare against. It changes no finding above, since
every claim in the paragraph is independently reproduced.

**Not re-run, and the subject does not claim it:** no product run was exercised. Round 1's honesty
cap covers it and §9's product-run bullet narrows it no further.

**Mutation caveat (`R4`):** §2.6's mutations prove `candidate_path_check` has binding force on one
half of this diff and none on the other. They do not prove that force is sufficient, and this
VERIFY is not a certification of either guard. Nothing in this range re-tests the guards' behaviour
on instruction-layer members, because no member was touched.

---

## 6. Conclusion

`REVIEWED_NO_BLOCKER` — 2 lows, 2 observations, no `SPEC_GAP`. Every question this range raised had
an answer in the layer; none of it needed a rule that does not exist.

The accepted finding is answered well. The correction is exact on every checkable claim — both blob
ids, the 342 lines, the end-to-end read, `HD-57`'s wording, the ledger's round-1 record — and it is
complete rather than instance-shaped: three members is the true count for the whole round, not just
for the commit the finding named. It stayed additive, so `HD-59`'s form is met mechanically. The
three banked rows carry the FULL's own deadlines or its explicit absence of one, `sig-write-once`
is routed to `HD-20`'s `E2` override rather than `R10`'s ordinary channel and that is correct, and
every one of the nine figures across them reproduces exactly, as does 854.

Both lows are the same shape and both land in the same place: a record that will be written next
says less than the truth about this round. `V-1` is the FULL's own minimum fix, still owed at the
carrier it named. `V-2` is the sentence in the round's journal that now says the budget was never
spent. Neither is the executor's to have fixed — the first is the orchestrator's commit, the second
was outside the approved boundary — and both are one clause each in the closeout, alongside the
FULL's `O-3`.
