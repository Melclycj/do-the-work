# VERIFY — subject `9580ca97a1ede617605478b9ba9c0389a30f1d7c..629cff5636fb0f08622153b6453d27cd5e32e793`

**Verdict: `REVIEWED_NO_BLOCKER`** (0 blockers · 1 low with a named closeout deadline · 2 wording-level · 4 observations).

All four accepted findings are answered. Nothing in the repair broke anything: the battery, the
three pre-commit guards, the round's own new alarm and the `E10` member set are all green here, and
no announced path was written. The one finding worth acting on before closeout is that the repair
for blocker `B-2` reproduced `B-2`'s own shape at smaller scale — the plan of record still describes
finding `L-1`'s disposition as a fix that will be written, when the leg's last commit banked it.

Dispatched with the charter `migration/document-work-assurance-v3/v3-harness-review-contract.md`,
a stub; its operative successor `document-harness/CONSTRUCTION-CHECKLIST.md` was read end to end as
both the standing instruction and its own counterpart, per that file's own opening.

## 0. What I derived, and from what (`R2`)

The dispatch handed one range and nothing else. Everything below is re-derived here.

**The range holds four commits**, oldest first — `git log --format='%h %s'` run here:

| # | sha | title | kind, as its own body names it | files |
|---|---|---|---|---|
| 1 | `013483f` | `V3-FREEZE-TO-ALARM-ROUND-STATE-v1` | "Orchestrator bookkeeping" | `CONSTRUCTION-LEDGER.md` · `freeze-to-alarm.plan.md` |
| 2 | `1830d47` | `V3-FREEZE-TO-ALARM-FIX-HD44-v1` | review fix, 1 of 3 | `HARNESS-DECISIONS.md` · `HARNESS-DECISIONS-archive.md` · `HARNESS-RIDERS.md` |
| 3 | `34d63cc` | `V3-FREEZE-TO-ALARM-FIX-SPLIT-DESIGN-v1` | review fix, 2 of 3 | `document-harness/split-design.md` |
| 4 | `629cff5` | `V3-FREEZE-TO-ALARM-FIX-ANNOUNCED-SET-BANK-v1` | review fix, 3 of 3 | `HARNESS-RIDERS.md` |

`git diff --stat` over the range, classified by hand: **6 files, 158 insertions, 69 deletions** —
two governance registers, one register archive, one rider bank, one plan of record, one design
document. No code, no schema, no test, no instruction-layer member.

**The round.** Batch `FREEZE-TO-ALARM`, plan `document-harness/plans/freeze-to-alarm.plan.md`. The
range is its single `E9` fix leg, opened by the FULL `v3-review-full-ad0663d.md` (record commit
`9580ca9`, my range base) which returned `CHANGES_REQUIRED` over `B-1`, `B-2`, `L-1`, `L-2` plus six
observations.

**The budget.** `E9`: one FULL, at most one user-approved fix, one targeted VERIFY. Applying `E9`'s
own test — *has a valid independent FULL already occurred?* — yes, at `9580ca9`. So every commit in
this range is fix-round work and the leg obliges this VERIFY. `git show --stat 9580ca9` is
record-only (one file, 478 insertions), so `E9`'s "from dispatch to that commit the branch takes no
commit but the record itself" holds. I found no second fix and no commit outside the leg.

**Authorization.** A user ruling of 2026-08-28 approving all four findings, and choosing the
successor-entry shape for `HD-44` over an in-place status note. I *can* now see this in the
repository — plan `:477-483` carries it, and `1830d47` records the state flip as the user's under
`HD-2`. That is an improvement the round should get credit for: at the FULL, this material was
commit-body-only. What I still cannot see (`R7`, a ceiling, not a block): any record that the `E11`
preview card was rendered and the user waited, and any record of item D's authorization.

**The review window.** `.harness/review-pending.json` records `dispatched_at`
2026-08-27T16:40:14Z; `629cff5` is dated 2026-08-28 02:39:24 +1000 = 2026-08-27T16:39:24Z, **50
seconds before dispatch**. `git rev-parse HEAD` is the subject tip and `git status --porcelain`
reports one untracked path (`.goals/`) and no modified tracked file, so the worktree bytes I read
are the subject's blobs. `.harness/` is gitignored (`git check-ignore -v` → `.gitignore:18`), so the
dispatch marker is a run-time artifact and its written tip SHA is not a recorded range under `E12`.

---

## 1. The implementation (`R3` — this first)

### 1.1 `B-1` is answered, as a class fix, by the mechanism the register itself prescribes

The blocker was `HD-44:65`, live in `§live`, still ruling that changing the announced bytes owes a
recorded ruling — the requirement item A abolished — at an authority that outranks the clause item A
rewrote.

**The live requirement is gone and the mechanism is right.** `HD-44` no longer appears in `§live`;
`HD-62` stands at its head. Enumerated here rather than taken on trust — `§live` now holds
`HD-62 · HD-59 · HD-41 · HD-36 · HD-35 · HD-34 · HD-23 · HD-9`, and `HD-44` appears once, in
`HARNESS-DECISIONS-archive.md`, status `superseded`. `HD-62` is a fresh id: it collides with nothing
in `§live`, `§implemented` (33 entries) or the archive (21 entries). Bidirectional pointers exist and
landed in the same commit, which is what `HD-30` requires.

**The archived copy is byte-verbatim, and I proved it mechanically rather than by eye.** I extracted
the `HD-44` block from `HARNESS-DECISIONS.md` at the range base `9580ca9` and from
`HARNESS-DECISIONS-archive.md` at the tip and ran a unified diff. The **only** hunk is the status
line: `**live**` → `**superseded**` plus the new supersession parenthesis, which then quotes the
original parenthesis verbatim. The 裁决, 后果 and basis bullets are identical, character for
character. `HD-59` is honoured: nothing was rewritten in place.

**`HD-62` carries the narrowing and nothing more in the requirement.** The dropped text is the
trailing half (「真的改动那些字节仍然照旧欠裁决…」) and the clause 「因而不欠 `E2` 的记录裁决」.
The caller-deletion sentence is re-rendered 「按本条同样**不是写**」 where `HD-44` wrote 「同样不欠
裁决」, and the rejected reading is re-rendered 「`E2` 意义上的写」 where `HD-44` wrote 「未经裁决的
写」 — both disclosed in the commit body, both with the original verbatim in the archive.

**The class fix is real, and it closed the class.** The FULL's minimum fix asked for the sweep to be
re-run with 「欠裁决」 and 「欠 `E2`」 added and the output pasted (`HD-41` ④). I ran the declared
pattern myself at the tip over the declared scope. Every surviving hit is history that says so in
its own text — `CONSTRUCTION-LEDGER.md:217` (「旧 `E2` 下仍欠裁决」, explicitly past tense),
`CONTRACT-V4-SIGNATURE.md:14` (corrected beside it by this round's errata under `HD-59`),
`HARNESS-DECISIONS.md:44` (`HD-62`'s own note quoting the sentence it declines to carry), and
`HARNESS-RIDERS.md:13` (rider `PD` quoting the *old* `E2` verb inside `HD-27`'s historical basis, and
that row's own touch record now states the guard was added). **No live requirement that `E2` needs a
ruling before a write survives anywhere in this repository.** The count in the commit body is one
short — see `V-2` — but the holding is correct.

**The FULL's "adjacent, same entry" note is answered too, by carrying corrected text rather than by
editing.** `HD-62`'s status parenthesis records that `HD-44`'s quotation of `E2` as 「三个 blob 加一
个目录」 went stale twice, and states today's `E2` as one path plus one directory pinning no hash. I
checked that against `E2`'s live bytes: the list is `contract/Document-Work-Assurance-Contract-v4.md`
plus the `schema/document-assurance-v3/` pack, and the clause says in its own words that no blob hash
is pinned. Correct.

**And `HD-62` adds a boundary note that is genuinely load-bearing**, marked as not part of the
ruling: this entry judges what counts as a write under `E2`, not the alarm's mechanical predicate —
`git diff-tree` cannot see that a change is a wholesale move, so a commit that really moves these
paths is judged red like any other and the answer is to name the paths in its own body. That is
right, and it is the kind of thing that is only obvious once written down.

### 1.2 `B-2` is answered, and its two measurements reproduce exactly

Plan `:1-3` now reads "Status: round OPEN and worked; FULL returned `CHANGES_REQUIRED`; the one fix
leg is in flight." Steps 3, 4, 5, 6 and 8 are ticked, each naming the commit that landed it; step 7
is marked STILL OPEN (item D) and step 9 IN FLIGHT. I checked every tick against `git log`: the
chain `464b7dc` → `580d236` → `a2d3fb4` → `184387c` → `1d4d9aa` → `0355b36` → `ad0663d` → `9580ca9`
is the range the FULL derived, and each step points at the right one. The ledger's queue-head line no
longer says 尚未开轮.

Both of `013483f`'s own figures reproduce here, from commands run on this tree:

- **the queue-head entry measures 1,352 characters** — I re-derived it by splitting the ledger on
  top-level `- ` entries and measuring that block: **1352**. Exact.
- **the file stays at 20 top-level entries against its bound of 20** — I counted: **20**. Exact.
  The one entry over the 2,500-character bound is the CLOSED roll (line 79, 17,128 characters),
  which the ledger's own header excepts and which the plan's queued inventory already tracks as its
  own batch.

The commit also records, in both carriers, the before/after decision the FULL's `O-1` said was
unrecorded: protection lands after this round's commits, and every commit in this round went
straight to `main`, so question 1's PR flow did not govern this round's own work. That answers the
half of `O-1` that was actionable from inside the repository.

### 1.3 `L-2` is answered from the side the finding named, and the contradiction is closed on both

`split-design.md` §5 gains a correction block between the last 提议 bullet and 边界照记. The three
original proposal bullets stand verbatim; the block corrects forward beside them, which is `HD-59`
and is this file's own established practice.

I verified the three things the block asserts:

- **The distinction it draws is the one that matters.** `HD-27` refused a guard whose predicate was
  pre-write authorisation — a predicate no machine can see — and item C's job's predicate is
  post-hoc disclosure on CI. The block states this rather than assuming §5's surviving inference
  still holds, which is the honest move: the inference held under a predicate that has since been
  replaced.
- **`PD` was not redeemed and is still a live row.** Confirmed — `HARNESS-RIDERS.md:13`, and its own
  touch record for this batch says the same, so the bank and the surface it points at now agree.
  That was the whole of `L-2`'s bite.
- **The `pack_digests` measurement reproduces exactly.** `git grep -n 'pack_digests' -- '*.py'` run
  here returns three lines and only three:
  `tooling/rsclib/document_harness/__init__.py:238` (definition), `:266` (the `__all__` export), and
  `tooling/announced_path_disclosure.py:24` (one line of prose explaining why it is not used). Zero
  callers. The deletion proposal stands unexecuted, which is exactly where `PD`'s redeem-when points.

I also checked the block's justification for existing at all: §0 routes conflicts to §10 and `HD-39`,
and §10's subsections are §10.1–§10.5 — none of them §5. So nothing upstream catches those two
proposals, and the correction block is the only thing that can. Correct.

The commit deliberately did **not** reword `PD`'s redeem-when, on the ground that neither arm was met
(the export surface is untouched and the deletion proposal's own bytes are unchanged). I agree: the
commit adds a block discussing the proposal and moves none of it.

### 1.4 `L-1` banked, and the banking judgment holds up

`629cff5` adds one row, `announced-set-anchor`, and its substance is the judgment that all three
candidate fixes are design. I tested that judgment rather than accepting it:

- **Adding an anchor sentence to `E2`** adds a clause to a rule. `E10`'s design test makes that
  design outright. Correct.
- **Replacing the two referents with fifteen literal names** changes what the rule requires — the
  set's authority moves from a historical fact to the clause's own bytes — and manufactures a fourth
  unguarded copy. That is the `E10-sync` shape, and this repository has mutation evidence of a prose
  leg staying green while broken. Correct.
- **Asserting `ANNOUNCED == git ls-files schema/document-assurance-v3/`** makes the guard's
  expectation a function of the thing it guards, which is the inversion `E5` exists to prevent. I
  read the module: its own docstring at `:52-55` says exactly this, and says listing the directory
  would silently enrol new schemas — which `E2` explicitly refuses. Correct.

`E10` settles the tie in the same direction (where the free channel and the design test both apply,
design wins and a round opens), and the FULL itself routed `L-1` to `R10`'s bank rather than the free
channel. So bank is the right disposition, and it is the one the FULL asked for.

**The row is `R10`-shaped**, checked clause by clause: it names a target clause rather than a file
(`E2`'s announced list sentence in `CONSTRUCTION-CHECKLIST.md`); its redeem-when names a
**round-eligible** surface, as `R10` requires of a design-shaped row; and its deadline is the first
addition to or removal from `schema/document-assurance-v3/` — a moment the defect starts to bite,
and outside the round that writes the row, since no commit in this range or the FULL's range touches
an announced path. One row, three columns plus id, appended at the table's end.

The row's own measurement reproduces: `git ls-files schema/document-assurance-v3/` returns **15**
files here, and I compared them one for one against `ANNOUNCED` at
`tooling/announced_path_disclosure.py:56-73` — sixteen entries, contract v4 plus those exact fifteen,
all matching. The cited line ranges are right. The row's markdown is well formed: it is the only row
in the bank using an escaped pipe, and honouring escapes every one of the 30 table lines has exactly
4 columns.

### 1.5 Nothing broke

Every figure below is from a command run here, on this tree, after the tip commit.

| check | result |
|---|---|
| `python -m pytest -q` | **`813 passed in 153.72s (0:02:33)`** — the count the FULL re-derived and the leg claims |
| `tooling/hooks/layer_path_check.py` | exit **0** |
| `tooling/hooks/candidate_path_check.py` | exit **0** |
| `tooling/hooks/review_freeze_check.py` | exit **0** |
| the round's own alarm, over my subject range | **green** — "4 non-merge commit(s) judged; every announced path changed in this range is named by the commit that changed it" |
| `E10` members resolve | **9/9**, `LAYER` in `layer_path_check.py` unchanged at nine paths |
| announced paths written | **none** — the six changed paths are not `contract/Document-Work-Assurance-Contract-v4.md` and none is under `schema/document-assurance-v3/` |
| `E10-sync` | **not due** — the membership sentence is untouched and no changed file is a member |

The leg touched no code, no test and no guard, so the battery count moving by zero is the expected
result rather than a reassuring one; I record it because a text-only leg that moved it would have
been the alarm. Running the alarm over the leg's own commits is the check that has teeth: the alarm
is live from floor `1d4d9aa`, it judged all four commits, and it passed.

---

## 2. Findings

### Low — carries a deadline

**`V-1` — the repair for `B-2` reproduced `B-2`'s shape: the plan of record still says finding
`L-1` will be fixed, when the leg banked it as design.**

*Location.* `document-harness/plans/freeze-to-alarm.plan.md:477-483` (resume pointer, item 1), and
the same shape at `CONSTRUCTION-LEDGER.md:209-211`.

*What is false.* Plan `:481` lists, among the four approved fix-leg items, "**the sixteen announced
paths gain a locally resolvable enumeration**". That did not happen and, by the leg's own ruling,
must not happen inside this round: `629cff5`'s body says "THE ANSWER IS BANK, NOT FIX" and argues at
length that every candidate enumeration is design and opens a round. The plan is the only place in
the repository that describes `L-1`'s disposition as a fix, and `git grep` over the plan finds no
other mention of it — nothing corrects it downstream. The ledger has the milder version of the same
thing: its 未结四件 list still carries ② (the announced-set defect) and ③ (`split-design.md` §5) as
open, when ③ was fixed 61 seconds later at `34d63cc` and ② was banked at `629cff5`.

*Not merely stale — wrong when written.* The FULL had already routed `L-1`: "Which, or neither, is a
design call under `E6`, so it routes to `R10`'s bank rather than the free channel"
(`v3-review-full-ad0663d.md`, `L-1`, *No bytes supplied, deliberately*). `013483f` landed after that
record and under the same 2026-08-28 approval, so the plan text contradicted the FULL's own routing
at the moment it was typed. The alternative reading — that the leg genuinely intended to write the
enumeration and changed course at `629cff5` — does not rescue the tip: on that reading the carrier
needed correcting when the course changed, and `629cff5`'s body says "SITE CHANGED, exactly one".

*The ground truth it violates.* The plan's own header contract, quoted in the very commit that fixed
`B-2`: "A cold session reads this file, then `CONSTRUCTION-LEDGER.md`'s current pointer, then works."
`013483f`'s body states why that matters — "these are the two files a cold session reads first, and
`HD-55` dispatches every executor cold."

*The downstream decision that goes wrong.* The closeout is step 4 and the round is at a handoff
point. A closing orchestrator reconciling the leg against the plan meets an item the leg did not
deliver and has three moves, all wrong: record the round as having delivered it; conclude the leg is
incomplete and spend a second fix, which `E9` forbids; or do what the line literally directs and
write the enumeration into `E2`, which the bank row and `E5` both say may only happen in a round of
its own.

*Weighing it down rather than up, honestly.* The accurate fact is recoverable — from the rider row
`announced-set-anchor`, from `629cff5`'s body, and from the plan's own "fix leg is in flight" framing
— which is why this is a low and not the blocker `B-2` was. What it is not is self-correcting: the
carrier a cold session reads first is the one that is wrong, and that was the entire content of
`B-2`.

*Minimum fix, and its route.* The content is named here, so under `E10`'s free channel this is
applied immediately, reported after the fact, reversible, and spends no budget. In plan `:481`,
replace the enumeration clause with the disposition that actually landed — `L-1` banked as rider
`announced-set-anchor`, every candidate fix being design under `E10`, redeemable only by a
round-eligible batch touching `E2`'s announced list sentence. In the ledger entry, move ② to banked
and ③ to fixed at `34d63cc`. **Deadline: this round's closeout**, since that is the reconciliation
the defect misleads, and it is the surface that must touch both files anyway.

*Adjacent, same commit, wording-level.* Plan `:488` writes the item-D decision in the past tense —
"it landed after" — while step 7 two lines above says item D is STILL OPEN and the ledger says
未做. The decision content is unambiguous and adjacent text corrects the tense, so it rides the
same fix rather than earning its own line.

### Wording-level (`R9`)

**`V-2` — `1830d47`'s pasted post-fix class sweep says 3 lines; the command it declares returns 4,
and the fourth is a line its own pre-fix list had enumerated.**

*Location.* `1830d47`'s commit body, THE CLASS SWEEP paragraph.

*What is false.* The body declares a pattern — item A's five alternatives plus 「欠裁决」 and
「欠 `E2`」 — a scope (all tracked files, excluding `migration/`, `document-harness/journal/`,
`document-harness/plans/` and the two archives), and two figures: 6 lines before, 3 after. I ran the
declared command over the declared scope at `1830d47` itself and at the tip. Both return **4 lines /
5 occurrences**: the three the body names, plus `HARNESS-RIDERS.md:13`, which matches 「无裁决写入」
twice. `1830d47` does not touch that line, and `629cff5` appends a row at the table's end, so nothing
in the leg could have removed it. The pre-fix list of 6 *does* include it, described correctly as
rider `PD`'s quotation of `HD-27`'s historical basis; it is simply absent from the list of 3.

*Why it is wording-level and not more.* The substantive claim survives intact. `HARNESS-RIDERS.md:13`
quotes what a pre-commit guard *would* have guarded, inside a rider row whose own touch record for
this batch states that a guard was added with a different predicate — history, not a live
requirement. So `B-1`'s class is genuinely closed, which is what the sweep was for.

*Why it is worth a line anyway.* `HD-41` ④ requires the output be pasted precisely because a class
fix stands or falls on the sweep, and `E3` requires counts be emitted by the command that produces
them. A reader auditing this class fix by re-running the command gets a different number than the
body promises and has to work out which of them is wrong. The correction is one figure and one
clause: 4 lines, and the fourth is `HARNESS-RIDERS.md:13`, historical. Content named → `E10` free
channel.

**`V-3` — `HD-62` carries one clause less than `1830d47` says it carries.**

*Location.* `HARNESS-DECISIONS.md:44` and `:49`; the dropped bytes are at
`HARNESS-DECISIONS-archive.md:55-57`.

*What is false.* `HD-44`'s 后果 carried a parenthetical recording that the 十八→十六 count
correction landed 2026-08-23 under the user's ruling of that day, and that signature commit `3b25f3c`
had claimed the same change while its diff lacked it (`v3-cold-read-cf54a79.md` `L-3`). `HD-62` does
not carry it. `1830d47`'s body says "Dropped: the trailing half, and that is the whole of the
narrowing", and `HD-62:44` says 「本条对 `HD-44` 的收窄只有一处」. `HD-30` requires the successor
carry 收窄后的全文.

*Stated fairly.* `HD-62:49`'s enumeration is precise — it says it carries 「主题、判据、反读法被
否、后果里的**住址与件数**、以及基线」, and the parenthetical is neither address nor count, so a
careful reader can see it is not claimed. And dropping a provenance note narrows no requirement, so
「收窄只有一处」 is defensible on its own terms. What overstates is the head clause 「其余全文承接」
and the body's "that is the whole of the narrowing".

*Why wording-level.* No actor's action changes, and the bytes survive verbatim one file over in the
same repository, `grep`-reachable, in a block whose status line points at `HD-62`. Fix: either carry
the parenthetical into `HD-62`'s 后果, or replace 「其余全文承接」 with the enumeration that follows
it, which is already accurate. Content named → free channel.

### Observations

**`V-4` — `013483f` departs from `E8`'s commit form in two ways, alone among the four.** Measured
here: body paragraph counts are `013483f` **6**, `1830d47` **1**, `34d63cc` **1**, `629cff5` **1**.
`E8` says "one dense paragraph, no trailers". Separately, `E8` requires the body name the commit's
kind from its list — candidate / pre-submission correction / review fix / closeout / errata /
amendment / ruling / record — "so the review side can attribute it without asking". `013483f` opens
"Orchestrator bookkeeping", which is not one of the eight; the other three each say "Review fix"
and their ordinal. Nothing was hidden — the body says plainly that it answers the FULL's second
blocker — and I had no trouble attributing it. Recorded because the form exists so that attribution
never depends on a reviewer's willingness to infer.

**`V-5` — `629cff5` self-classifies which commits the leg consumed, which is the shape `E9` names.**
Its body says the leg is "three commits" and that `B-2`'s answer "was orchestrator bookkeeping
already landed at `013483f` **before this leg began**". By `E9`'s own test — has a valid independent
FULL already occurred? yes, at `9580ca9` — `013483f` is a fix-round commit: it lands after the FULL,
answers one of its blockers, and rides the same 2026-08-28 approval the other three cite. `E9` says
"Never self-classify which round consumed what: every recorded escape from the cap was a renamed
round." **No cap was escaped here** — `013483f` is inside this VERIFY's subject, the leg is closed,
and no second fix is claimed anywhere — so this is the shape without the consequence. Recorded
because the shape is what `E9` asks the review side to notice, and because a closeout that carries
"the fix leg was three commits" forward will have dropped one.

**`V-6` — rider `archive-header-selfcount`'s touch condition fired and the row was not redeemed.**
`1830d47` added the seventh `HD-6` asking block to `HARNESS-DECISIONS-archive.md`'s header, which is
that row's redeem-when surface, and `R10` redeems on touch. The commit declined on boundary grounds
and said so on the row and in the body, which is what `E9` requires of a boundary it will not
exceed; and the ground is real, since the fix is a figure sitting in a committed record and whether
it is corrected in place or forward turns on the `HD-59`/`HD-23` line. The new block also declines to
reproduce the defect — it writes no post-move line count and says to run `wc -l` instead, which is
the second of the two remedies the row itself prescribes. I think the call is right. Recorded because
the row's touch condition has now fired once without redeeming, and a bank whose touch conditions
fire without redemption is the accumulation `R10` exists to prevent; the row carries no deadline
(`R9`, no nameable downstream decision), so nothing forces the next firing to resolve it either.

**`V-7` — item D and its evidence are `UNVERIFIABLE` from here, and I am not folding them into
supported (`R4`).** Both carriers now assert that the alarm has been observed running green on
GitHub (run `33089379131`, 7s) and that the check name is registered so protection may be applied.
`gh` is blocked by this session's permission layer, so I could read neither the workflow run nor the
branch-protection endpoint, and I have not observed the CI job execute. The claim is recorded as
made, not as verified. Item D remains the round's one untouched work item, correctly marked STILL
OPEN at plan step 7 and 未做 in the ledger; whether it belongs to this round or is severed from it
is the user's (`R5`).

---

## 3. What I checked that held

- **The accepted findings, one by one.** `B-1` answered as a class fix with the right mechanism and
  a byte-verbatim archive copy (§1.1) · `B-2` answered with both measurements reproducing exactly
  (§1.2) · `L-2` answered from the section's side, with both sides of the contradiction now agreeing
  (§1.3) · `L-1` banked with a well-formed `R10` row and a design judgment that survives testing
  (§1.4).
- **`E9` budget and window.** One FULL, one fix leg, this VERIFY. No second fix, no commit between
  dispatch and now, the FULL's record commit is record-only.
- **`E2` compliance by the leg's own commits.** No commit writes an announced path; classified by
  hand from `git show --name-only` per commit against `ANNOUNCED`'s sixteen. Nothing was owed under
  the disclosure clause, and all four bodies nonetheless say so explicitly.
- **`E10` and `E10-sync`.** No changed file is a member; the membership sentence is untouched;
  `LAYER` still holds nine paths and all nine resolve on disk.
- **`E12`.** The recorded range is a gitignored run-time marker, not a committed record, so the
  written tip SHA is display rather than a recorded range.
- **`E8` form on three of four.** Single dense titles naming the round, one paragraph, no trailers,
  each naming its kind. The fourth is `V-4`.
- **Register integrity after the move.** `§live` 8 entries · `§implemented` 33 · archive 21; `HD-62`
  a fresh id; `HD-44` appears exactly once, in the archive, `superseded`.
- **The rider bank's shape.** 29 rows, every one 4 columns with escapes honoured; the new row names a
  target clause, a round-eligible redeem-when and a deadline outside this round.
- **The ledger's own bounds.** 20 top-level entries against a bound of 20; the only entry over 2,500
  characters is the CLOSED roll, which its own header excepts.
- **The plan's queued inventory is not falsified by the new row.** Its "rider bank — 28 rows" cell
  is inside a table declared "read-only inventory, 2026-08-27", so it is a dated snapshot and the
  29th row does not make it wrong.

## 4. Coverage and ceilings (`R4`)

- **Read in full:** `document-harness/CONSTRUCTION-CHECKLIST.md`;
  `migration/document-work-assurance-v3/v3-harness-review-contract.md`;
  `migration/document-work-assurance-v3/v3-review-full-ad0663d.md`; all four commit bodies and the
  full diff of each; `HD-62` and the archived `HD-44` in full and diffed against each other
  mechanically; `HD-30`; `split-design.md` §5 and its new correction block; the three rider rows
  touched (`archive-header-selfcount`, `announced-set-anchor`, `PD`);
  `tooling/announced_path_disclosure.py:50-79`.
- **Read in part:** `CONSTRUCTION-LEDGER.md` — the header and the queue-head entry, not the CLOSED
  roll. `document-harness/plans/freeze-to-alarm.plan.md` — status block, step list, resume pointer,
  queued inventory; not end to end. `HARNESS-DECISIONS.md` — `§live` in full, `§implemented` by id
  enumeration only. `split-design.md` — §0 and the §10 heading map, not §1–§4 or §6–§11.
  `tooling/hooks/layer_path_check.py` — its `LAYER` constant only.
- **Probed only:** everything else, by targeted `git grep` around the claim under test —
  `CONTRACT-V4-SIGNATURE.md`, `CONSTRUCTION-LEDGER-archive.md`, `.github/workflows/ci.yml`, the
  contract and the schema pack (enumerated by `git ls-files`, not read). I did **not** re-read the
  nine `E10` members end to end: no member's blob moved in this range, and the FULL read
  `CONSTRUCTION-CHECKLIST.md` in full at `ad0663d`, whose blob is unchanged here — I read it in full
  at this tip regardless, as the standing instruction.
- **No mutation, and why.** The repair diff contains no code, no test and no guard, so there is
  nothing new to mutate; the FULL mutation-tested the alarm at six shapes and a VERIFY is never a
  re-certification (`R4`). What I did instead is run the alarm over my own subject range, which
  exercises it live against four commits it had never judged. `E4`'s scratchpad protocol was not
  invoked and no file in the worktree was modified by me at any point.
- **Not run, and not folded into supported:** anything requiring `gh`. The branch-protection
  endpoint and the workflow run cited in both carriers are blocked by this session's permission
  layer — blocked, not absent — so item D is `UNVERIFIABLE` here (§`V-7`). `origin/main` I read from
  the local remote-tracking ref: it sits at `0355b36`, so **`git rev-list --count origin/main..HEAD`
  is 6** — the errata, the FULL's record and all four leg commits are unpushed. The ledger's
  FREEZE-TO-ALARM entry records no push debt, where the preceding batch's entry recorded
  「push 债：`origin/main..HEAD` = 58」; I note the asymmetry without calling it an obligation.
- **Process claims are marked, not verified.** That this review ran in a fresh context, that the
  `E11` preview card was rendered and the user waited, that the executor and orchestrator sessions
  were cold and dispatched per `HD-55`, that `E8`'s explicit-path staging was honoured, and that the
  three guards and the battery were run before each commit as the bodies state — none has an
  evidence lock in the repository and none is verified here. I re-ran the battery and the guards
  myself at the tip and report those as my own measurements.
- **`E1`'s four-holdings disclosure.** No commit in this range makes the statement, and the batch
  still has no round journal, so neither `E3` carrier holds it. `ad0663d` had routed the question
  correctly to the orchestrator at the FULL. If this round took `E1`'s exception channel the
  statement is still owed; if it ran the three-session norm nothing is owed. I still cannot tell
  which from the repository, and the fix leg did not change that.
- **`R2` compliance.** The commit set came from `git log` run here; every count, sha, grep, diff,
  character count and test result above was produced by a command run in this session; no figure was
  taken from the dispatch, a commit body, the plan or the FULL. Where I cite a body's number it is
  because I re-derived it independently, and I say so — including the two places where mine and the
  body's disagree (`V-2`) and the several where they agree exactly (813 · 1,352 · 20 · 15 · 3 ·
  9/9).
- **Chat-only load-bearing material: none found, and one improvement.** The 2026-08-28 approval that
  authorises this leg now lives in the plan at `:477-483` as well as in the four commit bodies,
  where at the FULL it lived only in bodies. `V-1` is the adjacent failure — not material living
  only in chat, but the tracked carrier describing one of the four approved items as something other
  than what landed.
