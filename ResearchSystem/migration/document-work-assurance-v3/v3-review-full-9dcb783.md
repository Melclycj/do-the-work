# FULL review — round `E10-D-NARROWING` (candidate `9dcb783`)

| | |
|---|---|
| round | FULL, construction-side (`CONSTRUCTION-CHECKLIST.md` E1–E12 / R1–R10) |
| subject | `c8d9afa097908a4e5f74ec511a74c345ef6d3547..9dcb783218739defff0facd9c796e6fd51a53499` |
| range content | exactly one commit, `9dcb783` (`V3-E10-D-NARROWING-v1`, kind: candidate) |
| **verdict** | **`CHANGES_REQUIRED`** |
| findings | 2 blocking, 0 low, 3 observations |
| record | this file; the execution side commits it (`R6`) |

`CHANGES_REQUIRED` here is not a judgment on whether the narrowing should have happened —
`R5` puts that outside my reach, and the user ruled it. Both blockers say the landed bytes
do not decide a question they are the sole text for.

## 1. Subject, re-derived (`R2`)

Handed one range and nothing else. Every figure below is re-derived; no reported number
accepted.

```
$ git rev-parse HEAD              -> 9dcb783218739defff0facd9c796e6fd51a53499  (== subject tip)
$ git rev-parse --abbrev-ref HEAD -> document-work-assurance-v3
$ git status --porcelain          -> (empty)
$ git rev-list --count c8d9afa..9dcb783 -> 1
$ cat .harness/review-pending.json
  {"kind": "construction-round",
   "subject": "c8d9afa097908a4e5f74ec511a74c345ef6d3547..9dcb783218739defff0facd9c796e6fd51a53499",
   "dispatched_at": "2026-08-03T14:19:25+00:00"}
```

Subject tip committed `2026-08-04T00:19:03+10:00` = `14:19:03Z`, twenty-two seconds before
the dispatch; the branch has taken no commit since. `E9`'s window is intact and this record
is the only commit it admits (`review_freeze_check.py` re-read, not assumed: it refuses any
staged path outside the four `v3-*` record families while the marker exists).

Changed paths, classified by hand — one file, one hunk:

```
$ git diff --name-status c8d9afa 9dcb783
M	ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md    (7 +, 7 -)
```

That path is an instruction-layer member (`layer_path_check.py:31`, first of the nine-entry
`LAYER` tuple). No code, schema, test, generated surface or product-run artifact is in the
range. File length is unchanged at 164 lines on both sides, so the hunk is one semantic
edit plus reflow.

**Which leg this is.** No `v3-review-full-9dcb783.md` or any other FULL record for round
`E10-D-NARROWING` exists in the repository, so by `E9`'s test — *has a valid independent
FULL already occurred?* — the answer is no and this dispatch is that FULL. Verdict set is
`REVIEWED_NO_BLOCKER | CHANGES_REQUIRED | SPEC_GAP` (`R3`).

**Not the `E10` read.** `E10` requires this amendment to pass an independent read of the
amendment text before any round relies on it, and bars that read from being banked as a
round's FULL. The converse binds too: this FULL is not that read. The amendment still owes
one.

## 2. What the round is, and its authorization

Re-derived chain, all in-repo:

| step | commit | what the repository shows |
|---|---|---|
| the amendment that started it | `22b27aa` | `E2` re-baselined to fifteen pack files; added `until a later re-baseline` + a rationale clause |
| its ruling of record | `journal/retro-2026-08-03.md` §7 ruling 6 | *"该 amendment 改变了规则要求，按 `E10` 欠一次独立 read"* |
| errata | `cd4c09e` | rider `E2-rb` was a misclassification; the read is a precondition, not a ride-along |
| the read | `c8d9afa` | `v3-checkpoint-read-22b27aa.md`, 1 must-fix (M-1), 0 low, 2 observations |
| M-1's remedy set, as the reader wrote it | same record | **(a)** open the amendment round, or **(b)** rule that retro ruling (6) covers the process channel |
| this round | `9dcb783` | remedy **(c)** — narrow the clause doing the catching — invented by the executing session, not offered by the reader |

**Round-vs-free-channel classification is correct, and I checked it rather than took it.**
`E10`'s must-fix free pair "admits only deletions and the literal replacement the finding
names." M-1 names no bytes — the read record says in terms that "the finding's remedy is a
ruling, not bytes." So the free pair does not admit this, and the pre-amendment design test
("replacing … text so that what a rule requires changes, is design and opens a round")
catches this very edit. Opening a round is right, and the commit says so itself.

**Authorization ceiling (`R7`).** The 2026-08-04 ruling that selected remedy (c) exists in
the repository only as this commit's own body — the executor attesting to its own
authorization. `HARNESS-LEDGER.md` (the file whose header claims "the user rulings that
exist nowhere else") does not carry it, and no journal entry for this round exists. I state
the ceiling and move on: I cannot corroborate the ruling, and I do not treat its absence as
a block.

## 3. Implementation, led (`R3`) — does the landed text do what it claims?

### 3.1 The edit, and the arithmetic in the commit body

```
$ git diff --word-diff=porcelain c8d9afa 9dcb783 -- …/CONSTRUCTION-CHECKLIST.md
-replacing or
-text so that
-  what
-requires changes,
+outright,
```

Four deletions, one insertion — exactly the accounting the commit body states. Verified.

- before: *"an amendment adding a clause to any rule, **or replacing or deleting text so that what a rule requires changes**, is design and opens a round"*
- after: *"an amendment adding a clause to any rule, **or deleting a rule outright**, is design and opens a round"*

### 3.2 Provenance claims — all four hold

| claim in the commit body | re-derived |
|---|---|
| rider `E10-d` born at `717e547`, source "checklist read chain", no verbatim minimum fix | ✓ `git diff 717e547~1 717e547 -- HARNESS-RIDERS.md` shows the row; `v3-review-full-feacb86.md:41` records "no verbatim minimum fix exists in any record — designed this round" |
| its fix designed inside `feacb86`, disclosed as a SPEC-gap | ✓ same row |
| that round's FULL left low `L-2` saying the fix closed the routing, not the named clause | ✓ `v3-review-full-feacb86.md:136-149` |
| `E10-d` already deleted from the bank at `feacb86`, so no row is redeemed here | ✓ absent from `HARNESS-RIDERS.md` at `feacb86` and at HEAD |

### 3.3 What the narrowing does not reopen — verified, the body is right

The deferral clause still reads *"an amendment that neither adds a clause to any rule nor
changes what any rule requires **(no rule-changing replacement or deletion)** … may be
relied upon before its read."* That parenthetical landed at `5f029cd`
(`git log -S "no rule-changing replacement or deletion"`) and is untouched by this diff. So
rider `E10-d`'s own named defect — the deferral clause failing to govern
replacements/deletions — stays closed, and a rule-changing replacement still owes its read
before reliance. The body's claim here is accurate.

### 3.4 Opening cold read, discharged by citation — verified at zero budget

The nine `LAYER` members re-derived at the base:

```
$ for p in <LAYER>; do git rev-parse c8d9afa:$p; done
2108635f  document-harness/CONSTRUCTION-CHECKLIST.md
f3a31208  document-harness/README.md
bd490c8b  document-harness/EXECUTION.md
c19d8cb9  document-harness/REVIEW.md
17ff31bb  migration/…/v3-harness-operating-contract.md
52a97a48  migration/…/v3-harness-review-contract.md
68031fa2  contract/…-supersession-1.md
e1a2f26b  contract/…-supersession-2.md
c2b713bf  schema/document-assurance-v3/paragraph-map.schema.json
```

Nine for nine identical to the commit body's list and to `v3-checkpoint-read-22b27aa.md`
§1 rows 1–9, which state a blob id per member as `E10`'s citation clause requires. The
citation discharge is sound.

### 3.5 Guards

Nothing in this range adds, removes or alters a guard, so `E4`/`R8` mutation duty does not
arise — there is no new binding force to prove. Re-run at HEAD:

```
$ python ResearchSystem/tooling/hooks/ledger_cap_check.py    -> exit 0
$ python ResearchSystem/tooling/hooks/layer_path_check.py    -> exit 0
$ python ResearchSystem/tooling/hooks/review_freeze_check.py -> exit 0
$ python Thesis/Work/Tooling/repo-audit.py                   -> RESULT: clean (exit 0)
```

**Marked, not verified (`R4`):** these ran against an empty index, so they confirm the
current tree, not a replay of the staged state at `14:19:03Z`. The commit body's "each exit
0 over the staged diff" is a process claim I cannot reproduce. I did check the one thing
that would have made it false at commit time — `review_freeze_check` blocks only while
`.harness/review-pending.json` exists, and the prior marker was deleted in `c8d9afa`, so no
marker existed when `9dcb783` landed. Consistent.

### 3.6 Where the text stops working

The design test is referenced nowhere else in the instruction layer — I grepped all six
prose members for `design` / `opens a round` / `amendment`; every hit outside `E10` is
unrelated. So the blast radius is lines 94–96 of one file. Both blockers live there.

## 4. Boundary and record conformance — second (`R3`)

| `E8` requirement | state |
|---|---|
| explicit paths, no `add -A` | ✓ one file in the diff |
| new commit, not amended | ✓ |
| no push | ✓ `git rev-list --count origin/main..HEAD` = 426, the standing user-gated debt; unchanged shape |
| inside the declared change boundary | ✓ the round declares `E10`; only `E10`'s paragraph moved |
| title `V3-<ROUND>-v1` | ✓ `V3-E10-D-NARROWING-v1` |
| one dense paragraph, no trailers | ✓ |
| kind named | ✓ "Kind: candidate" |
| `E2` frozen bytes untouched | ✓ no frozen path in the range |
| `E3` — factual assertions carry their command | ✓ token accounting and the nine blob ids are in the body; the landed text adds no new factual assertion |
| `E11` preview card | **process claim, not verifiable from the repository** (`R4`) — marked, not counted against the round |

## 5. Findings

### Blocking

**B-1 — the narrowing strands the collision clause, and reopens the seam rider `F-1r` was
deleted for.**

`CONSTRUCTION-CHECKLIST.md:95-96`, unchanged by this diff and now sitting against a
narrower test:

> *"when the free channel and the design test both apply — the named literal replacement
> itself adds a clause **or a bound** — design wins and the round opens"*

**Ground truth it violates.** That clause is the verbatim redemption of rider `F-1r`.
`v3-review-full-feacb86.md:41` records the row as *"design clause moved after the relied
qualifier + collision rule (F-1r) … 'design wins and the round opens' answers who-wins"*,
against the minimum fix written at `v3-review-full-8ec4c60.md:223-241`, whose named case is
verbatim *"a literal replacement the finding named (free path admits it) that **tightens a
rule by adding a bound**"* and whose named downstream decision is *"whether a read's
must-fix whose named minimum fix narrows a rule spends a round."* `F-1r`'s bank row said the
same in one line: *"字面替换同时加界时谁赢未定."* Both the design test's broad arm and the
`or a bound` gloss entered together in one hunk at `feacb86` (`git log -S` on each returns
`feacb86`); this round withdrew the arm and left the gloss.

**The failure, concretely.** `bound` in this sense occurs exactly once in the file — line
96. It has no other anchor. So a named literal replacement that adds a bound to a rule now
reads two ways that command different actions:

- If a bound-add is not a clause-add — which is how `E10`'s own deferral clause reads, since
  it lists *"adds a clause to any rule"* and *"changes what any rule requires"* as two things
  joined by *nor* — then the design test no longer reaches it, the collision clause's stated
  premise ("both apply") is false, the free channel wins, and the fix is **applied
  immediately at zero budget, reported after the fact**. Line 96 nonetheless says a round
  opens.
- If a bound-add is a clause-add, line 96 survives — and B-2 below fires instead.

Either way one of the two clauses in this rule is wrong about the same case. Under `R9` this
is not wording-level: the actor's action changes (a round opens or does not; the fix leg is
spent or is not).

**Minimum fix.** Delete `or a bound` from line 96. It is subtractive, matches `E10`'s
"additive or subtractive, never re-typed", and settles the case in the direction the ruling
took — bound-adding replacements ride the free channel. If the user instead intends
bound-adds to remain design, that is a re-broadening the ruling excluded, and it is the
user's call, not mine (`R5`).

**B-2 — the round's purpose is not established by its own bytes: the narrowed test still
plausibly catches `22b27aa`.**

Remedy (c) was chosen to "narrow the clause doing the catching" so that the `E2` re-baseline
is no longer caught, and the ledger's blocking P5B precondition ① can close. After the
narrowing, the only arm that could still reach `22b27aa` is *"adding a clause to any rule."*
What `22b27aa` added, by command:

```
$ git diff --word-diff=porcelain 22b27aa~1 22b27aa -- …/CONSTRUCTION-CHECKLIST.md
+rule until a later re-baseline — new schemas
+  stabilize first, which is why this clause re-baselines rather than auto-freezing.
```

`until a later re-baseline` is a provision `E2` did not previously carry: before it, a
later-added pack file was permanently outside the freeze; after it, a re-baseline can bring
it in. On the natural reading that is a clause added to `E2`, and the narrowed test catches
it exactly as the old one did. Ruling 6's own words — *"该 amendment 改变了规则要求"* — sit
on the other side of the same line.

I do **not** conclude which reading is right; `R5` and the fact that this is the harness's
own vocabulary both put that with the user. What I report is that the amendment neither
defines the term nor records the determination for the one case it was landed to decide, so
the round's stated purpose is unestablished by the text it landed. The commit body stops
short of claiming discharge ("the consequence for M-1 arrives only upon this amendment's own
independent read"), which is honest — but it also means precondition ① is no closer than it
was at `c8d9afa`, and the next session should not read the narrowing as having cleared it.

**Minimum fix.** In the same amendment, record the determination for `22b27aa` against the
narrowed test — or narrow *"adding a clause to any rule"* so the determination follows from
the text. Which, and whether remedy (a) or (b) is taken instead, is the user's (`R7`).

**`E6` note attached to both.** Closing B-1 and B-2 cleanly tends toward *defining* "adding
a clause", i.e. adding a clause — `E6`'s stated signal to re-question the guarded thing
rather than add machinery. I surface the signal; the conclusion is the user's.

### Observations (`R5` — reported; conclusions are the user's)

**O-1 — the whole design/no-design boundary now rests on one undefined term.** Before this
round, *"replacing or deleting text so that what a rule requires changes"* swept up
everything requirement-changing, so how loosely *"adding a clause"* was read rarely mattered.
It is now one of only two arms, and the layer's own records read it both ways:
`v3-review-full-8ec4c60.md:229-235` treats a bound-add as caught by the then-only clause-add
test, while `E10`'s deferral clause distinguishes the two. B-1 and B-2 are the same root
surfacing at two sites.

**O-2 — a redemption was withdrawn without its row returning.** `feacb86` deleted
`F-1r` from the bank on redeeming it. This round withdrew the text that redeemed it, and
`HARNESS-RIDERS.md` is untouched in the range. `R10` describes redemption (fix rides, row
dies) but not un-redemption, so nothing currently obliges the row's return and nothing
tracks the seam. Whether the bank should have an un-redemption path is a design question I
do not answer.

**O-3 — the ledger's blocking block is stale against the repository.**
`HARNESS-LEDGER.md:33-37` still presents precondition ① as awaiting the dispatch
`rsc v3 dispatch --read 22b27aa`. That read returned at `c8d9afa` and this round followed it.
The staleness is expected mid-round — `E9`'s window barred any other commit during the read
— and is a closeout obligation, not a candidate defect. Flagged so it is not missed, and
because the ledger is where the 2026-08-04 ruling would otherwise be recoverable (see §2).

## 6. Coverage disclosure (`R4`)

**Read in full:** the subject diff and both commit bodies (`9dcb783`, `c8d9afa`);
`CONSTRUCTION-CHECKLIST.md` at HEAD (164 lines); `HARNESS-LEDGER.md` (112 lines);
`HARNESS-RIDERS.md`; `review_freeze_check.py`; `retro-2026-08-03.md` §7 (all six rulings);
the `v3-harness-review-contract.md` stub.

**Sampled at cited lines:** `v3-review-full-feacb86.md` (30-50, 130-150);
`v3-review-full-8ec4c60.md` (218-248); `v3-checkpoint-read-22b27aa.md` §1 blob table;
`feacb86`, `22b27aa`, `717e547`, `5f029cd` diffs restricted to the paths at issue.

**Probed only:** `layer_path_check.py` (`LAYER` tuple and main path), `rsc.py` dispatch
section, `ledger_cap_check.py` behaviour by exit code, the journal directory listing.

**Not read, and not claimed:** the other eight `LAYER` members end-to-end. Their blobs were
re-derived at the base and matched the cited read record; blob equality is not a re-read,
and I did not perform one. `v3-checkpoint-read-22b27aa.md` was read in its §1 only, not its
219 lines.

**Process claims marked, not verified:** the `E11` preview card; the 2026-08-04 user ruling;
"three guards exit 0 over the staged diff" at commit time (§3.5).

**UNVERIFIABLE, stated as such rather than folded into supported:** whether a bound-adding
literal replacement is caught by the narrowed test (B-1); whether `22b27aa` is caught by it
(B-2). Both are questions the subject text was landed to answer and does not.

## 7. Next action

`CHANGES_REQUIRED`. The fix leg is `E9`'s one user-approved fix for this round, and it
obliges a targeted VERIFY covering the accepted findings plus the whole repair diff. B-1's
minimum fix is two words out of line 96; B-2's is a determination the user owns and may
resolve by taking remedy (a) or (b) after all. If both are taken they belong in one fix
commit — one leg, not two.

Whatever lands, this amendment still owes its independent `E10` read of the amendment text
before any round relies on it. That read is not this FULL and cannot be discharged by it.
