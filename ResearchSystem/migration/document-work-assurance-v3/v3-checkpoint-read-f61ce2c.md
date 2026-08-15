# Instruction-layer read — `f61ce2c1ecd166127b03d086908db901d11b0146`

`E10` read of the instruction layer at `f61ce2c`. Not a round: no verdict, no budget consumed
(`R3`). Its subject is the amendment text itself — batch B R5's answer to the must-fix of the
read recorded at `bf2fd09`, plus the free-channel bytes that rode with it — and the layer that
text sits in, never the work the text governs. It is banked as nobody's FULL. This read is also
the independent re-read `E10` `:97` owes for that must-fix answer, and the read `E10` `:107-109`
owes for the free-channel layer application.

**Findings: 0 must-fix, 2 low, 3 observations carried forward, 1 unrouted wording-level note.**
The amendment applies the finding's named literal replacement byte for byte, applies `W-1`'s
supplied bytes, writes nothing else, and the class sweep reproduces: the layer states what the
amendment channel admits at exactly two sites, and both now speak the post-`HD-36` vocabulary.
`L-1` is that the replacement bytes, accurate about the vocabulary, are still short of the
channel by one limb — and the commit that wrote them is itself the counterexample, because it
carried a below-must-fix free-channel application alongside the must-fix answer.

## 1. Subject, re-derived (`R2`)

Handed one SHA and the phrase *an E10 read*. Member set, blobs, figures and obligations are
re-derived here; nothing is taken from the dispatch prompt, the commit body, the ledger or the
rider bank.

```
$ git rev-parse HEAD          -> f61ce2c1ecd166127b03d086908db901d11b0146
$ git status --porcelain      -> (empty; 0 lines)
$ cat .harness/review-pending.json
  {"subject": "f61ce2c1ecd166127b03d086908db901d11b0146",
   "dispatched_at": "2026-08-13T07:52:33+00:00"}
```

HEAD **equals** the subject and the tree is clean, so worktree reads are reads of subject bytes;
each member's worktree hash was re-derived with `git hash-object` and compared against
`git rev-parse f61ce2c:<path>` — nine of nine EQUAL, plus `HARNESS-DECISIONS.md`. Dispatch at
07:52:33Z = 17:52:33+10:00 is 1 s after the subject commit's 17:52:32+10:00, and the branch has
taken no commit since, so this record is the first it admits (`E9`).

`E10`'s sentence **at the subject blob** (`:78-88`) governs the member set: nine paths, closing
with "and nothing else". It is byte-unchanged by this amendment — the single hunk lands at
`:172-189`, inside `R10`'s rider paragraph — and it is still item-for-item equal to
`layer_path_check.LAYER` (`:30-40`) and to `test_precommit_checks.py`'s hand-written `EXPECTED`
(`:165-175`), the three mirrors `HD-22` keeps by discipline, each read directly.

| # | blob at `f61ce2c` | lines | member | how it is covered here |
|---|---|---|---|---|
| 1 | `15999875` | 204 | `document-harness/CONSTRUCTION-CHECKLIST.md` | **changed** (`289cc3a7` → here) — read end to end; also this session's standing instructions |
| 2 | `54dfef83` | 38 | `document-harness/README.md` | unchanged — **read end to end** (no citation used) |
| 3 | `62c55e4b` | 421 | `document-harness/EXECUTION.md` | unchanged — **read end to end** |
| 4 | `3350bfac` | 284 | `document-harness/REVIEW.md` | unchanged — **read end to end** |
| 5 | `17ff31bb` | 5 | `migration/…/v3-harness-operating-contract.md` (stub) | unchanged — **read end to end** |
| 6 | `b576a45e` | 5 | `migration/…/v3-harness-review-contract.md` (stub) | unchanged — **read end to end**; the dispatch entry point |
| 7 | `68031fa2` | 124 | `contract/…-v3-supersession-1.md` | unchanged — **read end to end** |
| 8 | `e1a2f26b` | 113 | `contract/…-v3-supersession-2.md` | unchanged — **read end to end** |
| 9 | `09aa8699` | 44 | `schema/document-assurance-v3/paragraph-map.schema.json` | unchanged — **read end to end** |

Blob ids from `git ls-tree f61ce2c -- <path>`, line counts `wc -l` at the subject (tree clean, so
worktree = subject). **1 238 lines read fresh, 0 cited.** `E10`'s citation mechanism was available
for the eight unchanged members and deliberately not used: the two prior reads' end-to-end claims
would otherwise be load-bearing here, and a read whose own cost is one file is the cheapest place
to retire that transfer of trust. Rows 2–9 are therefore first-hand, not inherited.

`ResearchSystem/HARNESS-DECISIONS.md` at blob `0320b8ef`, `§live` read in full (lines 1–174: the
file header plus §live up to the `§implemented` heading at line 175): **twelve** entries —
`HD-36`, `HD-37`, `HD-35`, `HD-28`, `HD-33`, `HD-34`, `HD-27`, `HD-24`, `HD-23`, `HD-10`,
`HD-15`, `HD-9`. `HD-36` (`:30-46`) and `HD-37` (`:48-60`) are the rulings the predecessor
commit implements and whose status lines name *this* read as their precondition ("待批 B R5 的
read 走完"). Where the layer is silent and §live is not, §live outranks (`E10`), and both `L-1`'s
routing and `O-1` turn on exactly that. The decisions book is cited by section, never by blob.

## 2. Is the amendment the answer the read's findings asked for, and nothing else?

The whole diff, read directly rather than from its body — `CONSTRUCTION-CHECKLIST.md`
`289cc3a7` → `15999875`, **5 insertions / 4 deletions**, 203 → 204 lines, one hunk at `:172-189`,
two semantic edits and a reflow:

- **`M-1`'s answer** (`:182-183`) — "an `E10` amendment commit admits deletions and named fixes
  only" → "an `E10` amendment commit admits only the answers to a read's must-fix findings".
  This is the finding's *Minimum fix* string for string, taken over the finding's own admissible
  alternative (deleting the premise). `E10` `:98-99` admits "the literal replacement the finding
  names", so the channel takes it.
- **`W-1`'s bytes** (`:178-180`) — "because by then the only surface still open is one that
  cannot act on it" → "because the surfaces a round still has open after the row is written need
  not include one that may act on it". Again the finding's exact bytes.

Nothing else changed: `git show --numstat f61ce2c` is one file, `5 4`, and the hunk contains no
third edit.

**Sweep completeness, re-measured.** `E10` `:99-100` requires the same fix at every other site of
the defect class the finding names. Grepping all nine members for statements of what the amendment
channel admits (`admits` / `literal replacement` / `amendment commit` / `named fix` / `free
channel`) returns seven lines, all in `CONSTRUCTION-CHECKLIST.md`, of which exactly two state what
the channel admits: `E10` `:98-100` (the definition) and `R10` `:182-183` (the fixed site).
`EXECUTION.md`, `REVIEW.md`, `README.md`, both stubs, both supersessions and the schema restate
none of it. The sweep is complete **inside the layer**, and `HD-37`'s own ground line
(`HARNESS-DECISIONS.md:54`, "只收删除与点名修") is correctly left untouched — not a member, no
amendment machinery reaches it (`E10` `:122-123`), and the commit says so rather than leaving the
omission to look like a miss.

**Was the `W-1` application admissible on the free channel?** Four conditions, each checked at the
subject: the finding is below must-fix and its record supplies exact bytes (`E10` `:102-104`); the
path is not one `E2` freezes (`:105-107` — `CONSTRUCTION-CHECKLIST.md` is outside `E2`'s three
blobs and one directory); no round had relied on the text (`:110-112` — the only commits between
the bytes' authoring at `136f27f` and here are the read record `bf2fd09` and this amendment, and
a read is not a round; the `tier-file-vs-clause` rewrite at `136f27f` was ordered by `HD-37` ② and
turns on the rule, not on the ground clause `W-1` replaced); and the supplied bytes add no clause
and change no requirement, so the design test does not take it (`:114-116`). It was reported after
the fact in the commit body and is reversible. Admissible — and `L-1` is the one thing that
follows from its riding *this* commit.

**Did anything rely on the amended text before this read?** `git log 136f27f~1..HEAD` returns three
commits — `136f27f`, the record `bf2fd09`, the amendment `f61ce2c` — and nothing after the subject.
No round has relied on these bytes. Mechanical, from the commit graph.

## 3. What I re-executed

- `git hash-object` × 10 vs `git rev-parse f61ce2c:<path>` × 10 — all EQUAL (§1).
- `git show --numstat --format='' f61ce2c` → `5 4 ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md`;
  `git show -U6 f61ce2c` read in full. The round's own figures reproduce.
- `git diff 8884f47 136f27f -- <checklist>` — the predecessor amendment, read to establish which
  bytes `W-1` and `M-1` were about and that "low or observation alike" (`:102`) is **pre-existing**,
  not this round's wording (it sat at `8884f47`).
- **Full-stock path scan over all nine members**, driving `layer_path_check.unresolved_tokens` over
  each member's complete bytes at the subject rather than over a staged diff — **3 flagged, all
  inside `E2`-frozen members**: `supersession-1:89`, `supersession-2:60`, `supersession-2:83`.
  **Zero in the four writable members**, so the amendment adds no path defect. The same three the
  prior reads measured; carried by bank row `frozen-path-prefix`, read in the bank at the subject.
- `python -m pytest -q tests/document_harness/test_readme_enumeration.py
  tests/document_harness/test_precommit_checks.py`, run from `ResearchSystem/tooling` —
  `43 passed in 11.12s`. The two pins that bind layer files, green at the subject blobs.
  Re-derived, not taken from the body.
- `layer_path_check.LAYER` `:30-40` and `test_precommit_checks.EXPECTED` `:165-175` read and
  compared item-for-item against `E10`'s membership sentence — equal, nine for nine, three ways.
- Line-width measurement at the subject and at `136f27f` (`awk length>96`): subject has six lines
  over the file's wrap — `:19` (136, a heading), `:71` (98), `:102` (123), `:110` (102), `:172`
  (107), `:183` (107) — against five at `136f27f`. `:183` is new this round; see §4's unrouted note.
- `HARNESS-RIDERS.md` read in full at the subject (37 lines): 27 rows, none of which already banks
  either finding below. **Not filed against the amendment** — the rows are work the text governs,
  outside this read's subject (`E10`); recorded only that I looked, and that `tier-file-vs-clause`
  is the row that already banks the unverified tier question named in §5.

## 4. Findings

### Low

**`L-1` — `R10` `:182-183`'s new premise is short of the channel by one limb, and the commit that
wrote it is the counterexample.**

*Location.* `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md:182-183`: "an `E10`
amendment commit **admits only the answers to a read's must-fix findings**, so it meets such a
row's touch condition while being unable to redeem it".

*Ground truth.* `E10` `:102-105` at the same blob: a finding below must-fix whose record supplies
the exact bytes "takes the same free channel — applied immediately, instruction layer included,
reported after the fact and reversible". `f61ce2c` did exactly that: alongside the `M-1` answer it
carries `W-1`'s bytes at `:178-180`, a wording-level application that is not the answer to any
must-fix finding. Read as written, `:182-183` is false of the very commit that wrote it — or, on
the other reading, that commit exceeded what `R10` says an amendment commit admits. One of the two
has to give.

*What goes wrong.* `R10` is the routing rule; an executor deciding where a finding goes reads this
paragraph, which is the hazard model `HD-36` was bought by. An executor holding a must-fix answer
and a byte-supplied low, reading `:182-183` as operative, refuses the low entry to the amendment
commit — pushing it to a separate commit (harmless) or, if they read "admits only" as a bar on the
channel rather than the commit, back to the bank, which is the immediacy `E10` `:104` grants being
quietly withdrawn. The conclusion the premise serves is unharmed either way: a banked
design-shaped fix answers no must-fix finding, and the free channel loses to the design test
(`:114-116`), so an amendment commit still cannot redeem such a row.

*Why low and not must-fix.* Unlike the `M-1` it descends from, no removed defect class is
reinstated and nothing that "may not wait" is delayed: the limb missing here governs findings
that are by definition below must-fix, and their fix still lands immediately, one commit over.
Inflating it would cost an amendment/re-read pair on a packaging question.

*Exact bytes (so the free channel may take it).* At `:182-183`, replace

> an `E10` amendment commit admits only the answers to a read's must-fix findings

with

> an `E10` amendment commit admits the answers to a read's must-fix findings and the
> free-channel bytes riding with them, and a banked design-shaped fix is neither — design
> beats the free channel

*Design test, applied to my own bytes (`E10` `:113-116`).* They add no clause to any rule and
change what no rule requires: the requirement ("a design-shaped rider names a redeem-when surface
that may open a round, never any batch") is untouched, and only the ground under it is restated —
the same shape as `W-1`, which this round routed to the free channel. If the executor reads it the
other way, the finding banks rather than being applied; and if the user's answer is instead that
the *conduct* was wrong — free-channel bytes owe their own commit — then no bytes should be
applied here and `R10` stands as written. Which of the two gives is not mine to conclude (`R5`).

**`L-2` — a wording-level finding whose record supplies bytes has two routes, and this round used
the one `E10`'s own enumeration does not name.**

*Location.* `E10` `:102-104` ("a finding below must-fix — **low or observation alike** — whose
record supplies the exact bytes … takes the same free channel") against `R9` `:155-156` ("A read's
**wording-level** findings are **banked**, never rounds") and `R10` `:166-168` ("`R9` takes
wording-level, the `E10` free channel takes … **any finding** whose record supplies the exact
bytes").

*Ground truth.* `W-1` was filed wording-level under `R9`, with a named downstream decision and
exact bytes. `E10`'s enumeration names low and observation, not wording-level; `R9`'s headline
sends wording-level findings to the bank and names only the *no-decision-nameable* case as riding
the next batch; `R10`'s route sentence keys the free channel on bytes-supplied and says the tier a
finding was filed at does not change the route. Two of the three answer "apply now", one answers
"bank", and this round applied.

*What goes wrong.* The decision that changes is whether a wording-level fix lands immediately —
and therefore sits in the layer unread until the next read — or waits for a batch. Both readings
have text behind them of equal standing, so two executors will split, exactly as the bank's
`E1-suff` and `chk-thin` rows record for other rule pairs.

*No bytes, deliberately.* Any tiebreak — naming wording-level in `E10`'s enumeration, or excepting
bytes-supplied findings in `R9` — adds a bound to one of the two rules, which is design and opens
a round (`E10` `:113-114`). Under `E10` `:110` a finding below must-fix without appliable bytes
banks, so this one banks. Not pre-existing in the bank: I read all 27 rows at the subject.

### Observations (`R5` — reported; the conclusions are the user's)

The three the predecessor read filed are **unfixed by design** (the commit body routes them to the
user with the round's close) and all three are still true at the subject. Re-stated only as
still-open, not re-litigated:

**`O-1` — the general design test at `:113-114` is still unqualified** ("an amendment adding a
clause to any rule … is design and opens a round"), while `HD-36` ② narrowed that test back to the
free channel. The narrowing is carried at the precedence sentence `:114-116` and nowhere else, so
the layer read alone still applies the test to a must-fix answer; §live supplies the exemption and
outranks. This read is a live instance rather than a hypothetical: `L-1`'s own routing turns on
which of the two an executor applies to my supplied bytes.

**`O-2` — a byteless must-fix whose fix would land on an `E2`-frozen path is still unrouted by
`E10` alone.** `:105-107` banks "a finding **supplying**" such bytes; `:110` banks findings
**below** must-fix without appliable bytes; the intersection falls between them, closed only by
`R10` `:169-171`.

**`O-3` — `E9` `:72-73`'s exception still names the free channel only**, while `E10` `:97-98`
grants the must-fix amendment/re-read pair the same zero-budget status. Unchanged this round.

**`O-4` — both rulings this pair of commits implements are now carried in the layer at the sites
their own status lines name**, which is the condition `HD-36` and `HD-37` set for being re-argued
as `implemented`: `HD-36` ① at `:98-101`, its 后果 at `:110`, ② at `:114-116`; `HD-37` ① at
`:176-180`, ② at `:180-184`. Stated as a fact for the close decision, not as a recommendation —
`O-1` is the reason the carriage is not clean, and whether a status flips is the user's.

### Wording-level, no downstream decision nameable (`R9`: rides the next batch, no route)

The amendment added a third over-wrap line while declining to rewrap the two the predecessor read
measured: `:183` runs 107 characters, joining `:102` (123) and `:110` (102) against a body whose
other outliers are `:19` (a heading, 136), `:71` (98) and `:172` (107). Cosmetic, and the round's
reason for not rewrapping — that it would be an edit dressed as formatting — applies to its own new
line too. Measured so that a later editor rewrapping all three knows it is rewrapping, not editing.

## 5. Coverage disclosure (`R4`)

- **Read in full at the subject blobs:** all nine members, 1 238 lines, **none by citation** (§1);
  `HARNESS-DECISIONS.md` `§live` (lines 1–174); `HARNESS-RIDERS.md` (37 lines); the predecessor
  read record `v3-checkpoint-read-136f27f.md` (290 lines); `layer_path_check.py`; the full diff and
  commit body of `f61ce2c` and the predecessor diff `8884f47..136f27f`.
- **Read in part:** `test_precommit_checks.py` — the `EXPECTED` block, its two assertions and the
  `CHECKLIST` fixture uses only; `HARNESS-DECISIONS.md` `§implemented`, only far enough to place
  `HD-20` / `HD-22` / `HD-7`.
- **Probed only:** the eight battery commands were **not** run — the tier the amendment declared
  (doc-only) stays unverified beyond the two pins, which is precisely the unwritten reading rider
  `tier-file-vs-clause` banks, and that row was rewritten one commit before the subject rather than
  redeemed. `layer_path_check` / `candidate_path_check` / `review_freeze_check` / `repo-audit` were
  not re-run as hooks: on a clean tree the staged-diff scan is vacuous, and §3's full-stock scan is
  a different and stronger measurement of the same property. No guard was mutation-tested (`R8`) —
  no guard changed this round.
- **Not established.** That this read ran in a fresh context is a process claim with no evidence
  lock (`R4`). That `HD-36` / `HD-37` were ruled as their entries state is `R7` territory: the
  rulings are dialogue, and I take the entries as the repository's record of them. Whether the
  free-channel bytes riding this commit is a text defect or a conduct defect is stated as an open
  fork in `L-1`, not decided.
- **Out of subject.** The rider rows themselves, the round's tier declaration, and the `HD-36` /
  `HD-37` status flips are work the text governs, not the amendment text (`E10`); §3 says what I
  looked at and why nothing is filed from it. Whether `R10` should carry both a routing sentence
  and a rider-format sentence at all remains an `R5` question for the user.
