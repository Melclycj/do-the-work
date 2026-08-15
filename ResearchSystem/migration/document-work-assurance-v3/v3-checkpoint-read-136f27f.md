# Instruction-layer read — `136f27f5b36bea1128782f290637bb0e2dca3542`

`E10` read of the instruction layer at `136f27f`. Not a round: no verdict, no budget consumed
(`R3`). Its subject is the amendment text itself — batch B R5's widening of `E10`'s must-fix
channel and its two new `R10` rider clauses — and the layer that text sits in, never the work
the text governs, and it is banked as nobody's FULL.

**Findings: 1 must-fix, 0 low, 1 wording-level, 3 observations.** The amendment implements both
rulings it rests on, byte for byte, and introduces no path defect: the four writable members
carry zero flagged path tokens under a full-stock scan, and the class sweep `HD-36` ordered is
complete everywhere in the layer — except at the one site this same commit wrote. That site is
the must-fix: `R10` `:181-182` states the *superseded* definition of the `E10` must-fix channel
("admits deletions and named fixes only") as the premise of its new rider rule, twelve lines
after `E10` `:98-100` stopped saying it. The defect class the round opened to remove is
reproduced one rule below, in the same commit that removed it.

## 1. Subject, re-derived (`R2`)

Handed one SHA and the phrase *an E10 read*. Member set, blobs, figures and obligations are
re-derived here; nothing is taken from the dispatch prompt, the commit body, the ledger or the
rider bank.

```
$ git rev-parse HEAD          -> 136f27f5b36bea1128782f290637bb0e2dca3542
$ git status --porcelain      -> (empty; 0 lines)
$ cat .harness/review-pending.json
  {"subject": "136f27f5b36bea1128782f290637bb0e2dca3542",
   "dispatched_at": "2026-08-13T07:32:17+00:00"}
```

HEAD **equals** the subject and the tree is clean, so worktree reads are reads of subject bytes;
each member's worktree hash was re-derived with `git hash-object` and compared against
`git rev-parse 136f27f:<path>` — nine of nine EQUAL, plus `HARNESS-DECISIONS.md`. Dispatch at
07:32:17Z = 17:32:17+10:00 is 1 s after the subject commit's 17:32:16+10:00, and the branch has
taken no commit since, so this record is the first it admits (`E9`).

`E10`'s sentence **at the subject blob** governs the member set: nine paths, closing with "and
nothing else". The membership sentence is byte-unchanged by this amendment (all three hunks land
inside `E10`'s channel clauses and `R10`'s rider paragraph; `git diff 8884f47 136f27f` on this
file returns no hunk containing it), and it is still item-for-item equal to
`layer_path_check.LAYER` (`:30-40`) and to `test_precommit_checks.py`'s hand-written `EXPECTED`
(`:164-174`) — the three mirrors `HD-22` keeps by discipline, read directly rather than inferred
from the test that asserts two of them.

| # | blob at `136f27f` | lines | member | how it is covered here |
|---|---|---|---|---|
| 1 | `289cc3a7` | 203 | `document-harness/CONSTRUCTION-CHECKLIST.md` | **changed** (`7079fca5` → here) — **read end to end**; also this session's standing instructions |
| 2 | `54dfef83` | 38 | `document-harness/README.md` | unchanged — **covered by citation**, `v3-checkpoint-read-0aed595.md` §1 row 2 |
| 3 | `62c55e4b` | 421 | `document-harness/EXECUTION.md` | unchanged — **covered by citation**, `v3-checkpoint-read-8884f47.md` §1 row 3 |
| 4 | `3350bfac` | 284 | `document-harness/REVIEW.md` | unchanged — **covered by citation**, `0aed595` row 4 |
| 5 | `17ff31bb` | 5 | `migration/…/v3-harness-operating-contract.md` (stub) | unchanged — **covered by citation**, `0aed595` row 5 |
| 6 | `b576a45e` | 5 | `migration/…/v3-harness-review-contract.md` (stub) | unchanged — **covered by citation**, `8884f47` row 6 — the dispatch entry point |
| 7 | `68031fa2` | 124 | `contract/…-v3-supersession-1.md` | unchanged — **covered by citation**, `0aed595` row 7 |
| 8 | `e1a2f26b` | 113 | `contract/…-v3-supersession-2.md` | unchanged — **covered by citation**, `0aed595` row 8 |
| 9 | `09aa8699` | 44 | `schema/document-assurance-v3/paragraph-map.schema.json` | unchanged — **covered by citation**, `0aed595` row 9 |

Blob ids from `git ls-tree -r 136f27f`, line counts `wc -l` at the subject (tree clean, so
worktree = subject). Eight of nine discharge by citation, and the citations were checked rather
than assumed: `v3-checkpoint-read-0aed595.md` §1 marks rows 2, 4, 5, 7, 8, 9 **read end to end**
at exactly these blobs, and `v3-checkpoint-read-8884f47.md` §1 marks rows 3 and 6 **read end to
end** at exactly these blobs. Rows 7–9 are additionally blob-equal to
`v3-checkpoint-read-a5a04c3.md` §1. **1 034 lines cited, 203 read fresh, 1 237 total** — the
citation is `E10`'s mechanism and I used it, but it is a transfer of trust and is marked as one
in §5. All nine were nonetheless machine-scanned end to end for the two checks in §3.

`ResearchSystem/HARNESS-DECISIONS.md` at blob `0320b8ef`, `§live` read in full (lines 1–174, the
file header plus §live up to the `§implemented` heading at line 175): **twelve** entries —
`HD-36`, `HD-37`, `HD-35`, `HD-28`, `HD-33`, `HD-34`, `HD-27`, `HD-24`, `HD-23`, `HD-10`,
`HD-15`, `HD-9`. The two new ones, `HD-36` (`:30-46`) and `HD-37` (`:48-60`), are the rulings
this amendment implements. Nothing in §live is contradicted by the layer at this blob; where the
layer is silent and §live is not, §live outranks (`E10`), and `O-1` below turns on exactly that.
`HD-20` (`:245`) and `HD-22` (`:261`) sit in `§implemented` — in force, detail carried by `R10`
and by rider `E10-sync`. The decisions book is cited by section, never by blob (`E10`).

## 2. Is the amendment what the rulings say, and did anything rely on it early?

The whole diff, read directly rather than from its body — `CONSTRUCTION-CHECKLIST.md`
`7079fca5` → `289cc3a7`, 15 insertions / 6 deletions, 194 → 203 lines, three hunks:

- `E10` `:98-102` — "it admits **only** deletions and the literal replacement the finding names"
  → "it admits deletions, the literal replacement the finding names, **that same fix at every
  other site of the defect the finding names, and, where the finding supplies no bytes, the fix
  the executor writes**: a must-fix is the one class that may not wait, and a channel narrowed to
  the reported instance leaves its siblings to be found one re-read at a time". This is `HD-36` ①
  including its ruling-carried reason ("must-fix 是唯一不能等的一档").
- `E10` `:110` — "a finding without appliable bytes banks" → "a finding **below must-fix**
  without appliable bytes banks". `HD-36`'s 后果 clause, and the sweep is load-bearing: without
  it the literal text still routed a byteless must-fix to the bank, which is the outcome ① exists
  to prevent.
- `E10` `:115` — "the **named literal replacement** itself adds a clause or a bound" → "the
  **bytes the finding supplies** themselves add a clause or a bound". `HD-36` ②, verbatim.
- `R10` `:177-179` and `:179-183` — the two new rider clauses, matching `HD-37` ① and ②.

**Sweep completeness, measured.** `HD-36` ①'s whole point is that a fix reaches every site of the
defect class. I grepped all nine members for the class — statements of what the amendment channel
admits (`literal replacement` / `must-fix` / `free channel` / `admits … deletions`): the layer
holds exactly two, `E10` `:98-100` (fixed) and `R10` `:181-182` (**not** fixed — it is new bytes
this commit wrote, in the old vocabulary). `EXECUTION.md`, `REVIEW.md`, `README.md`, both stubs,
both supersessions and the schema restate none of it; `EXECUTION.md:299` mentions `E10` only for
the citation mechanism. Same for the sibling class "what spends budget": `E9` `:71-73`, `E10`
`:98`, `R3` `:153` — see `O-3`.

**Did the round rely on the text before this read?** `E10` requires the independent read before
any round relies on the amendment, and the same commit rewrote rider `tier-file-vs-clause`'s
redeem-when under the rule `R10` `:179-183` newly states — an outcome that would change if that
text changed. The defence is recorded and holds: `HD-37` ② is the user's ruling and orders that
rewrite by name ("rider `tier-file-vs-clause` 的 redeem-when 随 R5 按新判据重写"), and §live
outranks the layer, so the reliance is on the ruling, not on unread text. Marked as a judgment,
not filed: the reasoning is mine, not a mechanical result.

## 3. What I re-executed

- `git hash-object` × 10 vs `git rev-parse 136f27f:<path>` × 10 — all EQUAL (§1).
- **Full-stock path scan over all nine members**, driving `layer_path_check.unresolved_tokens`
  over each member's complete bytes at the subject rather than over a staged diff — **3 flagged,
  all inside `E2`-frozen members**: `supersession-1:89`, `supersession-2:60`, `supersession-2:83`.
  **Zero in the four writable members**, so the amendment adds no path defect. Those three are the
  same three the prior two reads measured; they are now carried by bank row `frozen-path-prefix`,
  which I read in the bank at the subject — the prior read's `L-1` is closed.
- `python -m pytest -q tests/document_harness/test_readme_enumeration.py
  tests/document_harness/test_precommit_checks.py`, run from `ResearchSystem/tooling` —
  `43 passed in 13.78s`. The two pins that bind layer files, green at the subject blobs.
  Re-derived, not taken from the body.
- `layer_path_check.LAYER` `:30-40` and `test_precommit_checks.EXPECTED` `:164-174` read and
  compared item-for-item against `E10`'s membership sentence — equal, nine for nine, three ways.
- `git show --numstat 136f27f` — three files, 32/0 + 1/1 + 15/6, zero code delta; the round's
  own figures reproduce.
- Line-width measurement across the file at `8884f47` and at the subject (`awk length > 96`) —
  the measurement behind the unrouted wording-level note in §4.
- `git log -S` on `"free-channel byte application"` (→ `5f029cd`) and on `"must-fix findings are"`
  (→ `af2905c`) — the dating behind `O-3`.
- `HARNESS-RIDERS.md` read in full at the subject (37 lines): the rewritten
  `tier-file-vs-clause` row does name round-eligible surfaces and does record the old deadline as
  void, so it conforms to the clause the same commit wrote. **Not filed** — the row is work the
  text governs, not the amendment text, so it is outside this read's subject (`E10`). Recorded
  only that I looked: the row also carries two sentences of deadline history into a bank `R10`
  `:172-173` says holds no narrative, and that tension predates and outlives this round.

## 4. Findings

### Must-fix

**`M-1` — `R10` `:181-182` states the superseded definition of the `E10` must-fix channel, in the
same commit that superseded it.**

*Location.* `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md:181-182`: "an `E10`
amendment commit **admits deletions and named fixes only**, so it meets such a row's touch
condition while being unable to redeem it".

*Ground truth.* `E10` `:98-100` at the same blob: the pair "admits deletions, the literal
replacement the finding names, that same fix at every other site of the defect the finding names,
and, **where the finding supplies no bytes, the fix the executor writes**." The executor-written
fix is by definition not a fix the finding names, so `:181`'s enumeration is short by one limb and
its "only" makes the shortfall exclusive. `HD-36` ① is the ruling that added that limb, on the day
this commit landed.

*What goes wrong.* `R10` is the routing rule — an executor deciding where a finding goes reads
exactly this paragraph. Reading `:181-182` as the operative statement of the channel, a byteless
must-fix is refused entry to an amendment commit, and `:110` no longer catches it (it was narrowed
to *below must-fix* this same round), so the finding is pushed to a round or to the bank. That is
the pre-`HD-36` behaviour, reinstated one rule below the fix, and it is the exact failure shape the
round's own body describes for R4: a channel narrowed to the reported instance leaves siblings to
be found one re-read at a time. Two sentences of one file now answer the same question differently.

*Minimum fix (literal replacement, so the channel takes it and no round opens — it changes what no
rule requires; the conclusion "unable to redeem it" survives, because a design-shaped rider's fix
is not the answer to any must-fix finding).* At `:181-182`, replace

> an `E10` amendment commit admits deletions and named fixes only

with

> an `E10` amendment commit admits only the answers to a read's must-fix findings

*Admissible alternative.* Delete the premise clause outright, leaving ":… never any batch: an
`E10` amendment commit meets such a row's touch condition while being unable to redeem it, and the
row rides the next round-eligible batch instead."

*Other sites of this defect class, enumerated as `E10` `:99-100` now requires.* Inside the layer:
none — §2's grep found `:181-182` and no other. Outside it, and **out of the channel's reach**:
`HARNESS-DECISIONS.md` `HD-37` `:54-55` carries the same characterization ("只收删除与点名修") as
the ground of its own ruling. That file is not a layer member — "no amendment machinery here
reaches it, its own bytes are discipline (`HD-7`)" — so the sweep must **not** be extended there;
whether the ruling's ground line is corrected is the user's, and it is named here only so the
executor does not either miss it or write into it under this finding.

### Wording-level (`R9`)

**`W-1` — the ground `R10` `:177-179` gives for the new deadline rule is contradicted by `R10`
`:183-188` four lines below.**

*Location.* `:177-179`: "that moment is never inside the round that writes the row — a deadline
arriving on its own round is malformed, **because by then the only surface still open is one that
cannot act on it**."

*Ground truth.* `:183-188`, same rule: a FULL's lows get a "spend-the-fix-leg / bank choice", i.e.
the round's fix leg **is** a surface that can act on a banked-or-not finding inside its own round.
The universal ground is therefore false for the general case; it is true for the case `HD-37`
actually reasons from, which is a rider whose fix is *design* — `HD-37`'s own text says so
("一轮里能兑付 design 形状 rider 的通常只有轮首那个候选 commit"). The rule itself is `HD-37` ① and
stands; only its stated reason over-generalizes.

*Why wording-level.* The fix changes no actor's action — the requirement ("never inside the round
that writes the row") is untouched — and the accurate fact is recoverable from adjacent text
(`:183-188`) and from `HD-37`. *Downstream decision named, as `R9` requires:* an author banking a
**non-design** rider tests the stated ground against their own case, finds a surface that can act,
reads the ground as inapplicable, and writes a deadline inside their own round — malformed under
the rule they just read past.

*Exact bytes.* At `:178-179`, replace "because by then the only surface still open is one that
cannot act on it" with "because the surfaces a round still has open after the row is written need
not include one that may act on it".

**Wording-level, no downstream decision nameable (`R9`: rides the next batch, no route).** The
amendment's two new long lines break the file's wrap: `:102` runs 123 characters and `:110` runs
102, against a body whose only pre-existing outliers were `:19` (a heading, 136), `:71` (98) and
`:172` (107). Cosmetic; measured so that a later editor rewrapping them knows it is rewrapping and
not editing.

### Observations (`R5` — reported; the conclusions are the user's)

**`O-1` — `HD-36` ② removed the must-fix channel's vocabulary from the precedence sentence, but the
*general* design test still reads over every amendment, so the exemption the ruling states now
lives only in §live.** `E10` `:113-114`: "an amendment adding a clause to any rule, or replacing or
deleting text so that what a rule requires changes, is design and opens a round" — unqualified, and
"an amendment" reaches the must-fix pair as plainly as it reaches a free-channel application. The
precedence sentence `:114-116`, which is the only place the two are reconciled, now speaks only of
"the bytes the finding supplies", i.e. of the free channel — which is precisely what `HD-36` ②
ordered ("把 design test 收窄回自由通道，不再伸进 must-fix 通道"). The ruling therefore states the
exemption; the layer does not. This matters more after ① than before it: an executor-written fix
for a byteless must-fix is far more likely to add a clause than a finding-supplied replacement was,
and whether that opens a round decides budget, the preview card and the user's approval. Reading
the layer alone gives a contradiction; reading `HD-36` with it gives the answer, and §live is owed
at every round's opening and outranks. Reported rather than filed because the fix — a qualifier on
`:113-114` — adds a bound and is therefore design (`E10` `:113-114` applied to itself), so it opens
a round rather than riding a channel. This is the residue of `v3-checkpoint-read-8884f47.md` `O-1`;
one half of that observation was answered by ②, the other half is still nowhere in the text.

**`O-2` — after `:110`'s narrowing, `E10` alone no longer routes one case: a byteless must-fix whose
fix would land on an `E2`-frozen path.** `:105-107` bars both channels from writing such a path and
routes "a finding **supplying** them" to the bank; `:110` now banks only findings **below**
must-fix without appliable bytes. A must-fix that supplies no bytes and whose fix is frozen falls
between the two. `R10` `:169` ("the bank takes what is left") and `:171` (`HD-20`'s override,
"however appliable they are") close it on a reasonable reading, which is why this is an observation
and not a finding — but `E10` used to close it on its own, and after this round it does not.

**`O-3` — `E9`'s exception list names the free channel only, while `E10` grants the must-fix pair the
same zero-budget status; ① widens what that pair may now write.** `E9` `:72-73`: "it obliges the
VERIFY — **except an `E10` free-channel byte application**, which is not a round and consumes
nothing." `E10` `:97-98` says the must-fix amendment/re-read pair "is not a round and spends no
budget", and `R3` `:153` says the same of a read. Pre-existing, not this round's doing: the pair
clause entered at `af2905c` and `E9`'s exception was written later at `5f029cd`, naming one of the
two. An orchestrator reading `E9`'s enumeration literally, in a round where a FULL has occurred,
counts a must-fix amendment as the round's one user-approved fix and obliges a VERIFY; `E10`'s
explicit clause says otherwise and is the specific rule. Recorded now because ① makes that pair
capable of carrying executor-written rule bytes, so the two readings diverge on more than they did.

## 5. Coverage disclosure (`R4`)

- **Read in full at the subject blobs:** `CONSTRUCTION-CHECKLIST.md` (203 lines, the changed
  member and this session's standing instructions); `HARNESS-DECISIONS.md` `§live` (lines 1–174);
  `HARNESS-RIDERS.md` (37 lines); `layer_path_check.py` (105 lines);
  `v3-checkpoint-read-8884f47.md` (290 lines) and §1 of `v3-checkpoint-read-0aed595.md`; the full
  diff and commit body of `136f27f`.
- **Covered by citation, not re-read:** members 2–9 (1 034 lines), each blob-identical to a row
  recording an end-to-end read in `v3-checkpoint-read-0aed595.md` §1 (rows 2, 4, 5, 7, 8, 9) or
  `v3-checkpoint-read-8884f47.md` §1 (rows 3, 6). If either record's end-to-end claim is wrong,
  this read inherits the error. All eight were nonetheless scanned end to end by machine for path
  tokens (§3) and grepped end to end for the two restatement classes (§2), so a *restatement* drift
  in them would have been caught; a defect of any other kind in their unread bytes would not.
- **Read in part:** `test_precommit_checks.py`, the `EXPECTED` block and its two assertions only;
  `v3-checkpoint-read-a5a04c3.md`, §1's blob rows only, to confirm the alternative citation for
  rows 7–9; `HARNESS-DECISIONS.md` `§implemented`, `HD-20` / `HD-22` / `HD-7` / `HD-2` only.
- **Probed only:** the eight battery commands were **not** run — the tier the amendment declared
  (doc-only) is unverified beyond the two pins, the same unwritten reading rider
  `tier-file-vs-clause` banks. `layer_path_check` / `candidate_path_check` / `review_freeze_check`
  / `repo-audit` were not re-run as hooks (a clean tree makes the first vacuous, as the prior read
  established); the full-stock scan in §3 is what establishes the layer's path state, and it is a
  different measurement from the guard's staged-diff scan. No guard was mutation-tested here
  (`R8`) — no guard changed this round.
- **Not established.** That this read ran in a fresh context is a process claim with no evidence
  lock (`R4`). That nothing relied on the amended text before this read is my reading of the one
  commit in question plus `HD-37` ②, not a mechanical result (§2). Whether `HD-36`/`HD-37` were
  ruled as the entries state is `R7` territory — the rulings are dialogue, and I take the entries
  as the repository's record of them without independent confirmation.
- **Out of subject.** The rider row's rewrite, the two rulings the body records as not-done, and
  the round's tier declaration are work the text governs, not the amendment text (`E10`); §3 says
  what I looked at and why nothing is filed from it. Whether the amendment channel should be
  metered at all, and whether `R10` should carry both a routing sentence and a closeout sentence,
  remain `R5` questions for the user.
