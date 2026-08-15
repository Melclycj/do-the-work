# Instruction-layer read — `838c4132831a3961997977829959e259deb3d6be`

`E10` read of the instruction layer at `838c413` (`V3-E2-VERB-E10-PIN-v1`). Not a round: no
verdict, no budget consumed (`R3`). This is the independent read the ledger's open column
owes — "`E2`/`E10` amendment 欠一次 `E10` 独立 read … 来源 `v3-review-full-838c413.md` L-2" —
whose subject is the amendment text itself and which the round's FULL is expressly
disqualified from being.

**Findings: 0 must-fix, 1 low, 1 observation.** The three edits say what they claim; the
nine-path enumeration is item-for-item equal to both code pins; no member is left holding a
statement the amendment falsified; and the open tail the pin deleted had realized nothing
the enumeration drops. The low is a rule-versus-rule collision that edit 1 moved from
text-decided to undecided, on the one path that sits in both registers.

## 1. Subject, re-derived (`R2`)

I was handed one SHA and the phrase *the instruction layer*. Round, obligations, member set
and every figure below are re-derived from the repository; nothing is accepted as reported
from the dispatch prompt, the ledger, the commit body, or the round's FULL.

```
$ git rev-parse HEAD              -> 0c19dcaae1a114fe43ef4e0a8d0ad5d5ab1c692c
$ git status --porcelain          -> (empty)
$ git rev-list --count 838c413..HEAD -> 2
$ cat .harness/review-pending.json
  {"kind": "layer-read", "subject": "838c4132831a3961997977829959e259deb3d6be",
   "dispatched_at": "2026-08-04T11:10:46+00:00"}
```

The two post-subject commits are `c667d08` (2026-08-04T20:41:33+10:00, the round's FULL
record) and `0c19dca` (20:49:57+10:00, closeout) — both landed before the dispatch
(11:10:46Z = 21:10:46+10:00), so `E9`'s window is intact and this record is the only commit
it admits. `git diff --name-only 838c413 HEAD` over the nine members returns empty, so the
layer at the subject equals the layer at HEAD and worktree reads are reads of the subject
bytes; the range's other paths are `.goals/LEDGER.md`, the round plan, `HARNESS-LEDGER.md`,
`HARNESS-RIDERS.md` and the FULL record — ledgers and records, no member.

`E10`'s sentence **at the subject blob** governs the member set, and at this subject that
sentence is itself the thing amended: it now enumerates nine paths and closes with "and
nothing else", so the set is decidable by reading it and no open tail has to be swept.

| # | blob at `838c413` | lines | member | coverage |
|---|---|---|---|---|
| 1 | `4d0c7330` | 173 | `document-harness/CONSTRUCTION-CHECKLIST.md` | **changed** (`2108635f` → here) — read in full this session at the subject blob, also as standing instructions; the delta is this read's subject |
| 2 | `f3a31208` | 37 | `document-harness/README.md` | cited: end-to-end read `v3-checkpoint-read-d01615b.md` (§1 row `f3a31208`, disclosure "members 1 … and 2 (37) at the subject blobs"); blob equality re-derived here |
| 3 | `bd490c8b` | 153 | `document-harness/EXECUTION.md` | cited: `v3-checkpoint-read-d58969d.md` (§1 row `bd490c8b`, disclosure "I read all eight in full anyway"); equality re-derived |
| 4 | `c19d8cb9` | 259 | `document-harness/REVIEW.md` | **read in full this session** — its citation ran through a chain, closed here (below) |
| 5 | `17ff31bb` | 5 | `migration/…/v3-harness-operating-contract.md` (stub) | read in full this session (5 lines); also cited at `v3-checkpoint-read-784e49b.md` (§1 row, disclosure "both stubs (5 each)") |
| 6 | `52a97a48` | 5 | `migration/…/v3-harness-review-contract.md` (stub) | read in full this session as the standing-instruction entry point; also cited at `784e49b` |
| 7 | `68031fa2` | 124 | `contract/…-v3-supersession-1.md` | cited: `v3-checkpoint-read-d58969d.md` (§1 row `68031fa2`, same disclosure); equality re-derived |
| 8 | `e1a2f26b` | 113 | `contract/…-v3-supersession-2.md` | cited: `v3-checkpoint-read-403fc9a.md` (§1 row `e1a2f26b`, disclosure "README.md (36) and supersession-2.md (113)"); equality re-derived; §5 read at the bytes here (below) |
| 9 | `09aa8699` | 44 | `schema/document-assurance-v3/paragraph-map.schema.json` | **changed** (`c2b713bf` → at `c05d052`) — read in full this session; no read record names `09aa8699` |

Blob ids from `git rev-parse 838c413:<path>`, line counts `wc -l` on `git show` at the
subject. Each citation was verified in the cited record's own text, not taken from an
intermediate table. Per-member `git log 22b27aa..838c413` shows exactly two members moved
since the last layer read: member 1 (`9dcb783` → `440e205` → this subject) and member 9
(`c05d052`). Member 1's trail is `2108635f` → `1836d456` → `2108635f` → `4d0c7330`: the
middle pair is the withdrawn `E10-D-NARROWING` round returning to its own base, so the only
un-read delta is `2108635f` → `4d0c7330`, the amendment.

**Member 4's citation was a chain and is closed here.** The last end-to-end read of
`REVIEW.md` is `v3-checkpoint-read-9541e1e.md` at predecessor blob `7b553516` (256 lines);
the single delta since, `1cfeeac`, was read in full at `v3-checkpoint-read-22b27aa.md` §3.
No record read `c19d8cb9` whole, and `E10` conditions citation on "a recorded end-to-end
read **of it**". Rather than report the gap I read the 259 lines: nothing in the file is
touched by the amendment (its "frozen" uses are the run subject and the dispatch marker, not
the `E2` surface, and it makes no membership claim), and the blob now has a direct
end-to-end read a later reader can cite.

## 2. The amendment against the repository (`E3`)

`git rev-list --count 3b7ebe2..838c413` = 1; `git diff --numstat` = one file, 19/10.
`git diff --word-diff` returns exactly three edit sites and no fourth token, so every
other line in the hunks is reflow carrying identical words — `E10`'s "never re-typed with
the same content" is not engaged by them.

| edit | from → to | checked |
|---|---|---|
| 1 | `Frozen bytes are untouchable,` → `Frozen bytes are **not written without a recorded user ruling**,` | word-diff isolates the verb; the list that follows is byte-identical |
| 2 | `take the in-boundary fix and record why, or stop with SPEC_GAP` → `either take the in-boundary fix and record why, or obtain the ruling and write under it, or stop with SPEC_GAP` | two insertions, no deletion; the opening now states a condition the menu contains a branch for, so the dangling-neighbour shape is absent |
| 3 | eight descriptors + open tail → nine full paths + "and nothing else" | reconciled by script, below |

**Edit 3, mechanically.** I parsed the backticked tokens out of the amended sentence at the
subject blob and compared them against both code pins in one script, written here rather
than taken from the round:

```
prose tokens: 9   LAYER: 9   EXPECTED: 9
prose == LAYER      : True
LAYER == EXPECTED   : True
(item-for-item, same order; 'and nothing else' present; all nine resolve at the subject tree)
```

`layer_path_check.LAYER` and `test_precommit_checks.LayerMembership.EXPECTED` are asserted
equal by `test_layer_equals_the_hand_written_membership`, and `test_every_member_is_scanned`
reaches each path, so the code side carries two pins and the prose is now the third. The
"zero code delta" claim holds: the range contains no `.py` file, so the prose moved to the
code and not the reverse. **The prose leg is bound by nothing mechanical** — already
established by the FULL's Mutation A and banked as rider `E10-sync`; not re-reported.

**The `E2` list is untouched and still true at the subject.** `8ad404b1…` =
`.goals/plans/document-work-assurance-harness-v3.plan.md`, `b2dbdf75…` =
`contract/Document-Work-Assurance-Contract-v3.md`, `68031fa2…` = member 7, `e1a2f26b…` =
member 8, all re-derived by `git rev-parse` at `838c413`; the pack is 15 files by
`git ls-tree -r … | wc -l`. Four blobs and one directory, decidable by inspection, as the
rule's own sentence claims. Edit 1 loosens the verb, never the extent.

## 3. What the pin closed — the realization sweep

The FULL swept for **dependents** of the deleted tail (text that refers to it). The
complementary question — had the tail already pulled anything in that "exactly these nine
… and nothing else" now excludes — is in no record, so it was run here.

The tail entered at `cf8e1b1` (2026-07-28, `git log -S"description\` strings when amended"`),
so only material post-dating it can have been realized. Since then:

- **Pack:** `git log cf8e1b1..838c413 -- <pack>` returns exactly three commits — `d50d9e5`,
  `34cf85b`, `c05d052` — all to `paragraph-map.schema.json`, which the enumeration keeps as
  member 9. The other fourteen pack files are byte-unchanged over that window. The three
  earlier description-touching commits (`eca4902`, `55133a9` on `review.schema.json`;
  `39e4136` on `review.v2.schema.json`) all predate the tail and were never "later".
- **Prose successors:** the only files added under `ResearchSystem/contract/amendments/`
  after 2026-07-28 are `2026-08-01-a1-p4-activation-successor.md` (`7b79f14`) and
  `2026-08-02-a2-p5a-scoped.md` (`8f6d872`). Read at the subject bytes, both are successors
  to the **ResearchSystem Contract v1 / amendment A1** — not to the Document-Work-Assurance
  contract `b2dbdf75…`. That contract is outside `E2`'s list, and `E2` says in terms that
  "this harness does not claim to freeze instruments it does not govern", so neither file is
  a successor to text this harness governs. No read record names either file; the sweeps
  covering their windows classified them at a coarser grain and concluded "nothing new
  supersedes prose this harness governs" (`v3-checkpoint-read-22b27aa.md` §1).

So the tail's realized set at the moment of the pin was exactly `{member 9}`, and the
enumeration preserves it. `LAYER` reached nine at `ace0845` (2026-08-01) — a free-channel
bytes application touching only a journal, the hook module and the test, no member — so the
code has been closed at nine for three days and this edit pulls the prose to it.

**Staleness, at the bytes.** Grepping all nine members at the subject for
`untouchable|open tail|prose successor|description string|instruction layer|frozen`: the
word *untouchable* occurs **zero** times in the layer, so edit 1 leaves nothing dangling.
The one live dependent of the deleted tail is `supersession-2:107`, "Under `E10` it is a
prose successor to signed text and owes an independent read"; edit 3 keeps "prose successors
to signed text" as an appositive on members 7 and 8, so the cross-reference still lands on
vocabulary `E10` holds. `README.md:33` names the three tracked checks and makes no
membership claim. Member 9's own description — read in full here — states it "joined the
pack 2026-07-31, and is part of the E2-frozen surface as of the 2026-08-03 re-baseline",
which agrees with `E2` at the subject.

## 4. Ledger bindings, checked

- **The open item is this read's warrant.** "`E2`/`E10` amendment 欠一次 `E10` 独立 read
  （本轮 FULL 明文顶不了；deadline = 下一轮依赖新 `E2` 或 `E10` 之前）". Subject = the
  amendment text, dispatched with a SHA and nothing else, not banked as any round's FULL.
  Reliance has not occurred: the two post-subject commits are a record and a closeout, and
  `E10` excludes authoring, citing and recording from *relied* — the closeout cites the
  amended `E2` when it rewrites rider `O-2b`'s redeem-when cell, which changes no outcome.
  This read therefore lands before the deadline, not after it.
- **Nothing else rides this read.** The ledger's bytes-channel entry says an in-layer
  application "仍欠 read（随下次 layer read 搭车）". Since `22b27aa` the only member deltas
  are member 1 (withdrawn round, net zero; then this amendment) and member 9 (`c05d052`, a
  round's review fix applied under the user's 松冻结裁决, not a free-channel application).
  Both are read in full here, so the ride is discharged at per-member cost and no
  application is left outstanding.
- **The round's three lows landed where the FULL asked.** L-1 → the rulings block, replacing
  the 2026-08-04 entry the amendment made false; L-2 → the open column (this read's warrant);
  L-3 → rider `E10-sync`, naming all three membership sites; O-1 → redeemed in place in
  `O-2b`'s cell. Verified against `HARNESS-LEDGER.md` and `HARNESS-RIDERS.md` at HEAD.
- **Budget**: this read spends nothing (`R3`); since dispatch the branch admits only this
  record (`E9`).

## 5. Findings

### Low

**L-1 — for the one path that is both an `E2` frozen file and an `E10` member, the free
channel and `E2` now give opposite answers of the same modality, and no committed record
resolves the new configuration.** Location: `CONSTRUCTION-CHECKLIST.md` at `4d0c7330`, the
`E2` opening clause and `E10`'s free-channel clause ("a low finding whose record supplies the
exact bytes or names the content takes the same free channel — applied immediately,
**instruction layer included**, reported after the fact and reversible"). Ground truth:
`paragraph-map.schema.json` is named inside `E2`'s fifteen files *and* enumerated ninth in
`E10`; it is the only path in both registers. Before edit 1 the collision had a
text-decided answer — bytes that are *untouchable* cannot be written immediately by anyone,
so the free channel could not reach member 9 at all. After edit 1 both rules are conditional
permissions of the same shape, neither names the other, and they resolve the same act in
opposite directions: `E10` says apply now and report after, `E2` says not without a recorded
user ruling first. This is not hypothetical — the act has already occurred once: `c05d052`
applied a named literal replacement to member 9's `description` (exactly the free channel's
shape) and it took the user's 松冻结裁决, which the ledger records as **"只为该文件、只此一次"**,
so the single precedent states in terms that it does not generalize. **Decision that goes
wrong unfixed:** the next low arriving with appliable bytes against member 9 is applied
immediately by one session and stopped by another, with equal textual support — and the
reversibility `E10` offers does not undo a freeze written without the ruling `E2` requires.
**Deadline:** the earlier of (a) the next finding supplying appliable bytes or naming content
for `paragraph-map.schema.json`, and (b) the next batch touching `E2`'s or `E10`'s text.
**No bytes are supplied, deliberately:** any tiebreak adds a bound to one of the two rules,
which `E10` sends to design and opens a round ("when the free channel and the design test
both apply … design wins and the round opens"). Supplying bytes would convert a narrow,
currently inert collision into a round; reported without them so it banks (`R10`, and the
2026-07-29 routing ruling for a middle low without appliable bytes).

### Observation (`R5` — reported; the conclusion is the user's)

**O-1 — the pin removed the criterion, not just the tail.** Under the deleted clause a new
file's membership was a question with a test: *is this a later prose successor to text this
harness governs?* §3 answers it for the only two candidates that ever arose, and the answer
is no — but the answer required reading two amendment files and locating which contract they
succeed. Under "exactly these nine paths and nothing else" there is no test at all: a file is
a member if it is on the list. That is the pin working as intended and it is what makes the
membership decidable by inspection; the cost is that the next file of that kind — the ledger's
⛔ block makes a **P5B owner-batch firewall amendment** the next thing to be drafted — is
answered by silence rather than by a criterion, and nothing prompts anyone to ask. Rider
`E10-sync` carries the drift risk for the three sites; it does not carry this. Whether the
criterion should survive somewhere is the user's question, not a defect in the bytes.

## 6. Coverage disclosure (`R4`)

**Read in full:** members 1 (173 lines at `4d0c7330`, also as standing instructions), 4 (259
at `c19d8cb9`), 5 (5), 6 (5, standing-instruction entry) and 9 (44 at `09aa8699`) at the
subject blobs; the amendment diff, plain and word-level; `v3-checkpoint-read-22b27aa.md` (219);
`v3-review-full-838c413.md` (345); `layer_path_check.py`'s docstring and `LAYER`; the
`LayerMembership` block of `test_precommit_checks.py`; `HARNESS-LEDGER.md` (118 at HEAD) and
`HARNESS-RIDERS.md` (17); the commit bodies of `838c413` and `0c19dca`; `supersession-2`'s
`E10` sentence at :107 and member 9's `description` at the bytes.

**Sampled:** the cited read records `d01615b`, `d58969d`, `403fc9a`, `784e49b`, `9541e1e` —
their §1 blob rows and coverage disclosures, grepped and read in context, not re-read whole;
`v3-review-verify-c05d052.md` §2; the headers of the two `contract/amendments/` files;
`eca4902`'s commit body.

**Only probed:** members 2, 3, 7, 8 — blob equality against their cited records plus the
`untouchable`/open-tail vocabulary sweep; they were **not** read end to end here, which is
what `E10`'s citation clause permits and is a real ceiling: a dependent phrased in vocabulary
neither sweep used would have been missed. Pack `ls-tree` counts and per-file histories;
`git log -S` for the tail's introduction; the dispatch marker; commit timestamps.

**Not verified:** that this read ran in a fresh context — a process claim, marked, not
verified. That the executor pulled the nine paths out of `layer_path_check.py` rather than
from memory, and that the guards ran after the edits — asserted in the commit body, not
witnessable from the repository; the *result* is verified either way by §2's reconciliation.
The user rulings behind edit 1 and behind `c05d052`'s freeze reopening exist in the ledger's
rulings block; their originals are chat (`R7` — ceiling stated, not a block).

**Ceiling:** what is established here is that the amendment's three edits say what they claim,
that its enumeration equals both code pins item for item, that no member is left holding a
statement it falsified, and that the deleted tail had realized nothing the enumeration drops.
Whether the membership criterion should survive somewhere (O-1), and how the `E2`/free-channel
collision on member 9 should be resolved (L-1), are the user's.
