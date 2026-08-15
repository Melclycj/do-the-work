# Instruction-layer read — `8884f474a4d935698ff717df01c6a76d71364ec0`

`E10` read of the instruction layer at `8884f47`. Not a round: no verdict, no budget consumed
(`R3`). It is the independent re-read owed by the amendment at `8884f47`, so its subject is the
amended text itself and the layer it sits in — never the work that text governs — and it is
banked as nobody's FULL.

**Findings: 0 must-fix, 1 low, 0 wording-level, 4 observations.** The amendment is faithful and
admissible. `M-1`'s defect class is gone from `R10`: the deletion is one of the two answers the
prior read named, the diff carries that deletion plus exactly `W-1` and `W-2`'s supplied bytes
and nothing else, and the two writable members now carry zero paths of the class the layer's own
guard refuses. The chain that began at `be9878a` terminates here on the text. The one low is not
about the text: the commit body reports a routing outcome — that `O-1`'s three frozen-member
paths bank — which the repository does not hold, the bank standing at 26 rows on both sides of
the amendment.

## 1. Subject, re-derived (`R2`)

Handed one SHA and the phrase *an E10 read*. Member set, blobs, figures and obligations are
re-derived here; nothing is taken from the dispatch prompt, the commit bodies, the ledger or the
rider bank.

```
$ git rev-parse HEAD          -> 8884f474a4d935698ff717df01c6a76d71364ec0
$ git status --porcelain      -> (empty; 0 lines)
$ cat .harness/review-pending.json
  {"subject": "8884f474a4d935698ff717df01c6a76d71364ec0",
   "dispatched_at": "2026-08-13T04:23:06+00:00"}
```

HEAD **equals** the subject and the tree is clean, so worktree reads are reads of subject bytes;
each member's worktree hash was re-derived with `git hash-object` and compared against
`git rev-parse 8884f47:<path>` — nine of nine EQUAL. Dispatch at 04:23:06Z = 14:23:06+10:00 is
8 s after the subject commit's 14:22:58+10:00, and the branch has taken no commit since, so this
record is the first it admits (`E9`).

`E10`'s sentence **at the subject blob** governs the member set: nine paths, closing with "and
nothing else". The amendment's three hunks are `@@ -174,8 +174,7 @@` inside `R10`,
`@@ -405,7 +405,7 @@` in `EXECUTION.md` and the stub's `:5` — none touches the membership
sentence (`git diff be9878a 8884f47` on this file returns 0 hunks containing it), so rider
`E10-sync` does not come due. The sentence is still item-for-item equal to
`layer_path_check.LAYER` (`:30-40`), read directly rather than inferred from the test that
asserts two of the three mirrors.

| # | blob at `8884f47` | lines | member | how it is covered here |
|---|---|---|---|---|
| 1 | `7079fca5` | 194 | `document-harness/CONSTRUCTION-CHECKLIST.md` | **changed** (`de4bd9aa` → here) — **read end to end**; also this session's standing instructions |
| 2 | `54dfef83` | 38 | `document-harness/README.md` | unchanged — **covered by citation**, `v3-checkpoint-read-0aed595.md` §1 row 2 |
| 3 | `62c55e4b` | 421 | `document-harness/EXECUTION.md` | **changed** (`2ac5cc75` → here) — **read end to end** |
| 4 | `3350bfac` | 284 | `document-harness/REVIEW.md` | unchanged — **covered by citation**, same record row 4 |
| 5 | `17ff31bb` | 5 | `migration/…/v3-harness-operating-contract.md` (stub) | unchanged — **covered by citation**, same record row 5 |
| 6 | `b576a45e` | 5 | `migration/…/v3-harness-review-contract.md` (stub) | **changed** (`52a97a48` → here) — **read end to end** — the dispatch entry point |
| 7 | `68031fa2` | 124 | `contract/…-v3-supersession-1.md` | unchanged — **covered by citation**, same record row 7 |
| 8 | `e1a2f26b` | 113 | `contract/…-v3-supersession-2.md` | unchanged — **covered by citation**, same record row 8 |
| 9 | `09aa8699` | 44 | `schema/document-assurance-v3/paragraph-map.schema.json` | unchanged — **covered by citation**, same record row 9 |

Blob ids from `git ls-tree 8884f47`, line counts `wc -l` on `git show` at the subject. Six of
nine discharge by citation: `v3-checkpoint-read-0aed595.md` §1 states each of those six blobs
and marks each **read end to end**, and each is byte-identical here — that record is the
citation `E10` provides for. Rows 7, 8 and 9 are additionally blob-equal to
`v3-checkpoint-read-a5a04c3.md` §1, so a later read may cite either. The three changed members
were read outright: 194 + 421 + 5 = **620 lines fresh**, 608 cited, 1 228 total.

`ResearchSystem/HARNESS-DECISIONS.md` `§live` read in full (lines 1–142, the file header plus
§live up to the `§implemented` heading at line 143): ten entries — `HD-35`, `HD-28`, `HD-33`,
`HD-34`, `HD-27`, `HD-24`, `HD-23`, `HD-10`, `HD-15`, `HD-9`. Nothing in §live is contradicted
by the layer at this blob. `HD-20` (`:213-219`), which decides the routing this read tests, sits
in `§implemented` — in force, detail carried by `R10`. The decisions book is cited by section,
never by blob (`E10`).

## 2. Was the amendment what `E10` admits?

`E10`'s must-fix pair "admits only deletions and the literal replacement the finding names".
The prior read named a literal replacement **and** named deletion as the other admissible
answer; this commit took the deletion. The whole diff, read directly rather than from its body:

- `CONSTRUCTION-CHECKLIST.md` `de4bd9aa` → `7079fca5`, 1 insertion / 2 deletions, inside `R10`'s
  closeout sentence — "…puts the spend-the-fix-leg / bank choice to the user **— a choice
  reached only where no bytes were supplied, since supplied bytes take the free channel above**
  (`E9`'s test…" → "…puts the spend-the-fix-leg / bank choice to the user (`E9`'s test…". That
  is `M-1`'s target clause removed whole, nothing else in the sentence.
- `EXECUTION.md` `2ac5cc75` → `62c55e4b`, 1 / 1 — `:408`, `W-1`'s supplied byte string, verbatim.
- the review-contract stub `52a97a48` → `b576a45e`, 1 / 1 — `:5`, `W-2`'s supplied byte string,
  verbatim.

Nothing else changed. Both free-channel targets were checked to exist at the paths now written
(`git ls-tree 8884f47` on each: `2c80d25e` and `5cf970c1`), and the stub's premise was checked
rather than accepted — `expected-construction-prompt.txt:3` does hard-code the stub path, so
"Path kept" is true. The stub is a layer member and is **not** `E2`-frozen: `E2` freezes the
contract blob, the two supersessions and the fifteen-file pack, and the two retired-contract
stubs appear in none of those, so the free channel reaches it and `HD-20` is not engaged.

**Was the deletion itself inside the channel, or design?** The reliance test decides it, and it
is unmet: the deleted clause routed FULL-origin lows carrying supplied bytes, no FULL has
occurred in this round (`git log 2d14a65..8884f47` is six commits — candidate, read record,
amendment, bank, read record, amendment — and no `v3-review-{full,verify}-*.md` names `B-R4`),
and the three lows the `0aed595` bank commit wrote supplied no bytes by the prior reader's
deliberate choice. Nothing relied on the clause between `be9878a` and its deletion.

**What the deletion leaves, checked rather than assumed.** The clause was the only reconciliation
between `R10`'s routing sentence and its closeout sentence, so removing it restores an
unreconciled pair: the closeout sentence offers a FULL's lows two outcomes (spend the fix leg,
bank) and does not name the free channel as a third. This is not filed as a finding for three
reasons. The routing sentence three sentences earlier is general on its face — "neither the tier
they were filed at nor whether a read or a FULL produced them changes the route" — and governs;
the residual failure mode is over-approval (a byte-supplied low reaching the user as a
fix-leg-or-bank question), which costs a question and never lands a rule change unapproved,
where `M-1`'s was the reverse; and the pair stood in exactly this form before `be9878a`. Filing
it would also be re-litigating an answer the prior read named as admissible (`R3`: a
non-blocking finding is never inflated).

**Does the redundancy argument hold?** The commit body rests the deletion on the claim that the
fact the clause carried is already carried three sentences above. Checked against `be9878a`'s
own body, which records what rider `R10-route` was deleted for, and against the current text:
question one (the `HD-20` override) is carried by `:166-168`; question two (a FULL-origin
finding can take the free channel) by "nor whether a read or a FULL produced them changes the
route" at `:162-163`; question three (`E10` said "a low finding", `R10` said "a middle low") by
`E10` `:99-100`'s "a finding below must-fix — low or observation alike". All three survive the
deletion. The row's redemption is not hollowed.

## 3. What I re-executed

- `git hash-object` × 9 vs `git rev-parse 8884f47:<path>` × 9 — all EQUAL (§1).
- **A full-stock path scan over all nine members**, driving `layer_path_check.unresolved_tokens`
  over each member's complete bytes at the subject rather than over a staged diff — **3 flagged,
  all inside `E2`-frozen members**: `supersession-1:89`
  (`` `schema/document-assurance-v3/review.v2.schema.json` ``), `supersession-2:60`
  (`` `assurance/runs/` ``), `supersession-2:83` (`` `schema/` ``). **Zero in the four writable
  members** — `W-1` and `W-2` are gone from the stock, which is the amendment's effect measured
  rather than described.
- `python -m pytest -q tests/document_harness/test_readme_enumeration.py
  tests/document_harness/test_precommit_checks.py`, run from `ResearchSystem/tooling` —
  `43 passed in 13.30s`. The two pins that bind layer files, green at the subject blobs.
- `layer_path_check` exit 0, `candidate_path_check` exit 0, `review_freeze_check` exit 0,
  `repo-audit` exit 0. **Disclosure: the first is vacuous here.** It scans only staged
  instruction-layer files and only the lines a staged diff adds; the tree is clean, so it
  examined nothing. Its exit 0 in the commit body is evidence about the staged diff at commit
  time, not about the current stock — the scan above is what establishes the stock.
- Bank size: 26 rows at `0aed595` and 26 at `8884f47`, `git diff` on `HARNESS-RIDERS.md` between
  them empty. Read in full; `R10-route` is absent, deleted at `be9878a` as its body states.
- `layer_path_check.LAYER` `:30-40` read and compared item-for-item against `E10`'s membership
  sentence — equal, nine for nine.
- `git show 2d14a65:…CONSTRUCTION-CHECKLIST.md` vs the subject, on the closeout sentence — the
  measurement behind `O-2`.
- `ResearchSystem/templates/run-v2/` does not exist; `ResearchSystem/assurance/templates/run-v2/`
  does. The measurement behind `L-1`'s count.

## 4. Findings

### Low

**`L-1` — the commit body reports that `O-1`'s frozen-member paths bank; the bank does not hold
them, and the count it states drops a fourth path the prior read listed.**

*Location.* `8884f47`'s body ("The reader's `O-1` scan found three further prefix-missing paths,
all inside `E2`-frozen members, and those bank however appliable they are") against
`ResearchSystem/HARNESS-RIDERS.md` at the subject, and against `R10` `:168-169`.

*Ground truth.* `R10` routes what no channel takes to the bank and then fixes the bank's shape:
"One row per rider: what · redeem-when · source". `HD-20` `:216-218` says the same in the
direction that applies here — a byte-supplying finding on an `E2`-frozen path banks until the
ruling exists. The bank is 26 rows at `0aed595` and 26 at `8884f47`, the diff between them
empty, and no row names any of these paths. So the sentence describes a routing that the
repository did not receive.

*The count.* The prior read's `O-1` listed four paths beyond `W-1`/`W-2`; the body says three.
Three is right for the guard's class and my scan reproduces exactly those three — the fourth,
`supersession-2:99` (`` `templates/run-v2/` ``), resolves nowhere at all, so
`unresolved_tokens` skips it by design ("tokens resolvable nowhere are skipped — they may be
illustrative"). It is nonetheless a path token whose real home is
`ResearchSystem/assurance/templates/run-v2/`. Silently narrowing four to three inside the
sentence that routes them means the fourth is named in no forward-looking place at all.

*What goes wrong.* When `E2`'s recorded ruling arrives — the single event these bytes are
waiting on — the one ledger built to be consulted at that moment says nothing, and the items are
recovered only by someone re-reading `f3f31c0`. That is the failure mode the bank exists to
prevent, and the body's past-tense framing ("those bank … working as written") reads as though
the routing had been executed.

*Two admissible answers; the choice is the orchestrator's, because the prior read pointedly
declined to call these defects* ("two structural notes rather than a defect claim … 'defect' is
the guard's convention read backwards onto signed text"):

1. **Bank one row.** Content named, so this may take the `E10` free channel — the write target is
   `HARNESS-RIDERS.md`, which `E2` does not freeze, so the `HD-20` override is not engaged by the
   row even though it is engaged by the bytes the row describes. Row: `frozen-path-prefix` ·
   *four path tokens in the two `E2`-frozen supersessions do not resolve as written —
   `supersession-1:89` `` `schema/document-assurance-v3/review.v2.schema.json` ``,
   `supersession-2:60` `` `assurance/runs/` ``, `supersession-2:83` `` `schema/` `` (the three of
   the guard's missing-prefix class), and `supersession-2:99` `` `templates/run-v2/` `` (resolves
   nowhere; real home `ResearchSystem/assurance/templates/run-v2/`). The signed files use a
   ResearchSystem-relative convention consistently, so whether these are defects or a convention
   the guard reads backwards is the user's call — the row exists so the question is asked when
   the bytes become writable* · redeem-when: *`E2`'s recorded ruling for the supersessions, or
   the next batch touching either file's path tokens, whichever arrives first; no deadline — the
   defect cannot bite while the bytes are frozen* · source: `v3-checkpoint-read-0aed595.md` `O-1`.
2. **Record that nothing routes**, on the prior reader's own framing, in the next record this
   round writes. Then the body's "those bank" is the sentence to correct, not the bank.

Either closes it. What is not admissible is the present state, where the body says one and the
repository holds the other.

### Observations (`R5` — reported; the conclusions are the user's)

**`O-1` — `E10`'s design test and its must-fix channel disagree about a requirement-changing
deletion, and the reading that makes the channel usable has now been taken twice without being
written.** `E10` `:110-111` says "an amendment adding a clause to any rule, or **replacing or
deleting text so that what a rule requires changes**, is design and opens a round". This
amendment deleted text so that what `R10` requires changed — the constraint on when the user
choice is reached is gone — and it opened no round. The must-fix channel `:97-99` says the
opposite for its own case: the amendment-plus-re-read pair "is not a round and spends no budget
— it admits only deletions and the literal replacement the finding names". The precedence
sentence `:111-113` resolves the collision for exactly one shape — "when the free channel and
the design test both apply — **the named literal replacement itself adds a clause or a bound** —
design wins and the round opens" — which does not reach a deletion, since a deletion removes a
bound rather than adding one. Both `b9e6fd8` ("Neither adds a rule … which is why this is a
must-fix answer and not a second design round") and this commit reason from the adds-a-bound
test, i.e. both read the must-fix channel as exempt from the general design test except where
the precedence sentence bites. That reading is the coherent one — the alternative empties the
channel, since most must-fix findings are about what a rule requires — and the effect here is
conservative. It is also nowhere in the text. Note the precedence sentence itself mixes the two
channels: it opens with "the free channel and the design test" and then names "the **named
literal replacement**", which is the must-fix channel's phrase. Same family as `O-2` of the
prior read, which recorded `R10`'s "it overrides the channel" as singular where `E10` bars both.

**`O-2` — "the sentence now reads as it did before `be9878a`" is off by one word, and the word
is a deliberate change the amendment was right not to revert.** Measured:
`git show 2d14a65:…` gives "before closeout **the executor** weighs each low's deadline"; the
subject gives "before closeout **the orchestrator** weighs". `be9878a` changed `executor` →
`orchestrator` per io-design §3 item 9 and disclosed it in its own body, and `M-1` did not touch
it, so the amendment correctly left it. The claim is therefore inaccurate in the safe direction
— the sentence is the pre-`be9878a` sentence *plus* an unrelated ruling-backed substitution.
Recoverable from `be9878a`'s body, no actor's action changes, and a commit body cannot be
amended (`E8`), so this is recorded rather than routed: it exists so that a later auditor
diffing `2d14a65` against the subject on this line does not read the word difference as an
undisclosed edit.

**`O-3` — one paragraph of `R10` has now consumed two zero-budget amendment/re-read cycles, and
the net effect of one of `be9878a`'s edits is nil.** The chain is `be9878a` (clause added) →
read `2e43ecf` → `b9e6fd8` (sibling sentence conditioned) → re-read `f3f31c0` → `8884f47`
(clause deleted) → this read. `be9878a`'s closeout clause is now gone in full, so that edit's
lasting contribution to the layer is zero, and the price was two independent reads. `E10` places
no bound on the chain: each pair is "not a round and spends no budget", so a paragraph that
keeps yielding one must-fix per read can iterate indefinitely at no budget cost while the round
in hand still has all three `E9` legs unspent. This read terminates the chain — it finds no
must-fix in the amended text — so the shape is reported, not raised as a problem. Whether a
free channel should be metered is the user's question, not mine.

**`O-4` — rider `tier-file-vs-clause` reached its self-carried deadline on a commit that is
structurally barred from redeeming it.** The row's deadline is "下一个碰「code 枚举的层文件」的
doc-only 构造批". This amendment is doc-only and touches two files
`layer_path_check.LAYER` enumerates, so on the row's own words the deadline arrived; the body
names the row and re-banks rather than redeems. It could not have done otherwise: the row itself
records that both directions of the fix add a bound and are therefore design, and an `E10`
must-fix amendment admits only deletions and the named replacement. So a deadlined rider whose
fix is design can have its deadline arrive, and arrive again, during any amendment cycle, and
age past it without anyone being able to act — the only surface that touches the layer between
rounds is the one surface that may not redeem it. Reported because the deadline mechanism is
what `R10` relies on to stop rows from silently aging, and here it cannot fire. Whether the
deadline should instead read "the next batch that may open a round" is a question for the user.

## 5. Coverage disclosure (`R4`)

- **Read in full at the subject blobs:** the three changed members (`CONSTRUCTION-CHECKLIST.md`
  194, `EXECUTION.md` 421, the review-contract stub 5 = 620 lines);
  `HARNESS-DECISIONS.md` `§live` (lines 1–142); `HARNESS-RIDERS.md` (36 lines, 26 rows);
  `layer_path_check.py` (105 lines); `v3-checkpoint-read-0aed595.md` (238 lines); the full diffs
  and commit bodies of `be9878a`, `b9e6fd8` and `8884f47`.
- **Covered by citation, not re-read:** members 2, 4, 5, 7, 8, 9 (608 lines), each blob-identical
  to the row in `v3-checkpoint-read-0aed595.md` §1 that records an end-to-end read of it. If that
  record's end-to-end claim is wrong, this read inherits the error — citation is `E10`'s
  mechanism and I used it, but it is a transfer of trust and is marked as one.
- **Read in part:** the two dispatch fixtures, by grep on the stub path only;
  `v3-checkpoint-read-a5a04c3.md`, §1's blob rows only, to confirm the alternative citation for
  rows 7–9. `v3-checkpoint-read-be9878a.md` was **not read** — `M-1`'s history reaches me through
  `be9878a`'s body and `f3f31c0`'s record, and I did not independently re-derive the earlier
  read's findings.
- **Probed only:** the eight battery commands were **not run** — the tier the amendment declared
  (doc-only) is unverified beyond the two pins, the same unwritten reading rider
  `tier-file-vs-clause` banks and `O-4` revisits. `candidate_path_check`, `review_freeze_check`
  and `repo-audit` were run to exit code only, not mutation-tested; `layer_path_check`'s exit 0
  is vacuous on a clean tree, as §3 states.
- **Not established.** That this read ran in a fresh context is a process claim with no evidence
  lock (`R4`). That no round relied on the deleted clause is my reading of the four commits since
  `be9878a` plus the absence of any `B-R4` FULL record, not a mechanical result. Whether the
  three frozen-member paths are defects at all is expressly *not* concluded here (`R5`) — `L-1`
  is about the mismatch between the body and the bank, not about the paths.
- **Out of subject.** Whether `R10` should carry a closeout routing sentence at all, whether the
  free/must-fix split should be summarized in two members, and whether the amendment channel
  should be metered, are `R5` questions.
