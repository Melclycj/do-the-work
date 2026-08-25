# VERIFY — `92cc514..0f0498f` (round `CORE-SET-LAYER`, batch `CORE-SET`, round 1)

Targeted VERIFY. Subject received as one range and nothing else (`R2`); round identity, budget,
authorization, obligations and every figure below are re-derived from the repository. Standing
instructions: `migration/document-work-assurance-v3/v3-harness-review-contract.md`, a stub
superseding to `document-harness/CONSTRUCTION-CHECKLIST.md` — read whole at the subject tip, and
it is its own counterpart. `HARNESS-DECISIONS.md` `§live` read whole at the tip (`HD-56` `HD-44`
`HD-41` `HD-36` `HD-35` `HD-34` `HD-23` `HD-9`, plus the header's mechanism block), owed at the
opening whether or not the layer's cold read was waived.

**Verdict: `REVIEWED_NO_BLOCKER`.** Every accepted finding is answered, and answered correctly;
the repair introduces no false statement I could falsify; the frozen bytes, the guards, the
suite and the caller-facing surface all hold. 4 findings, 3 observations. The first finding is a
budget classification, not an implementation defect, and a VERIFY has no vocabulary to block on
it — it is routed to the user because only the user rules on `E9` legs.

---

## 1. Subject and budget, re-derived

```
$ git rev-parse HEAD                          -> 0f0498f3a6b7df54f488c441bc8b763d4e1755a5
$ git status --porcelain                      -> ?? .goals/       (untracked only)
$ git log --oneline 92cc514..0f0498f | wc -l  -> 3
$ git rev-list --count origin/main..HEAD      -> 25               (nothing pushed, E8)
$ cat .harness/review-pending.json
  {"subject": "92cc514cbbe3ed3e07992283ce35299b5dc2042c..0f0498f3a6b7df54f488c441bc8b763d4e1755a5",
   "dispatched_at": "2026-08-25T17:45:32+00:00"}
```

Three commits, classified by hand from their own trees rather than from their titles:

| commit | committed | what it is |
|---|---|---|
| `166ee51` | 03:13:48 +1000 | the FULL's record, one file, 365 insertions, nothing else touched |
| `0482a40` | 03:42:56 +1000 | the round's one user-approved fix — six findings answered |
| `0f0498f` | 03:45:22 +1000 | two findings routed outside the fix leg under `HD-23`, plus a withdrawal |

`E9`, derived: the round's prior review-side events are the opening cold read (`9f1de08`, no
verdict, no budget) and the FULL at `166ee51`. The FULL is spent. `0482a40` is the fix leg and
is correctly self-classified — a valid independent FULL had occurred, which is `E9`'s own test —
and it is what obliges this VERIFY. The marker was written 10 s after the tip commit and the
branch has taken no commit since, so `E9`'s window holds for this dispatch as it did for the
FULL's (`92cc514` at 16:48:45Z, dispatch 16:48:58Z, record `166ee51` at 17:13:48Z, nothing
between).

**Change boundary held.** Paths touched across the range, classified by hand:

```
$ git diff --name-status 92cc514..0f0498f
M CONSTRUCTION-INDEX.md          M CORE-SET.md              M HARNESS-DECISIONS.md
M HARNESS-RIDERS.md              M CONSTRUCTION-LEDGER.md   M document-harness/ONBOARDING.md
M document-harness/templates/decision-log.md
M document-harness/journal/core-set-layer-2026-08-26.md
A migration/document-work-assurance-v3/v3-review-full-92cc514.md
```

- **Instruction-layer members (`E10`): none.** `layer_path_check.LAYER` holds 9 paths; the
  intersection with the 9 touched paths is empty. So no amendment, no independent read owed for
  this repair, and `E10-sync` does not fall due — all three as the fix's body states.
- **Frozen bytes (`E2`): untouched.** `git rev-parse {92cc514,0f0498f}:contract/...-v4.md` both
  return `dfc983d2e3d9fb5ca67b053a16fcfb0e6715b11a`, the blob `E2` names;
  `git diff --name-status 92cc514..0f0498f -- schema/document-assurance-v3/` returns 0 lines over
  a pack of 15 files.
- **No code, no tests, no schemas, no hooks:** the same command over `tooling/ assurance/
  .githooks/` returns 0 lines.
- `166ee51` adds one path and it is the record (`--stat`: 1 file changed, 365 insertions).
  Title `V3-REVIEW-RECORD-CORE-SET-LAYER-92cc514-v1` is `R6`'s form.

Authorization, from committed state only: `document-harness/plans/core-set.plan.md` carries
seventeen numbered user rulings and is named by `CONSTRUCTION-LEDGER.md` as the batch's carrier.
That the user approved this particular fix is a process claim I mark rather than verify
(`R4`, `R7`).

---

## 2. Implementation first (`R3`) — the six findings the fix leg answers

### B-1 — cured, and its arithmetic corrected upward against the record itself

`CORE-SET.md`'s sufficiency claim is gone. "needs these and nothing else to open, run and close a
round" is replaced by a bounded claim plus an explicit non-closure, which is what the blocker's
minimum fix named. Entry 3's reinforcing clause took the same bound. Ruling 11 was kept, so the
checklist stays construction-side, and per `E6` no new rule about the citations was added.

Both counts re-derived at the tip rather than accepted:

```
$ grep -n CONSTRUCTION-CHECKLIST over the five product-tier documents
  README.md:23 . EXECUTION.md:13 . REVIEW.md:8 . ORCHESTRATION.md:7 and :39 . ONBOARDING.md:109
  -> 6 sites, in 5 of 5 files                                             [matches]

$ backticked E1-E12 / R1-R10 citations, same five files
  README 1/1 . EXECUTION 3/3 . REVIEW 1/1 . ORCHESTRATION 20/13 . ONBOARDING 10/8
  -> 35 citations over 26 lines                                           [matches]
```

The fix corrects the FULL's own 36/27 to 35/26 and attributes the difference to
`EXECUTION.md:235`'s `R0`. I read that line: it is a product run's own requirement numbering
(`R0...Rn`, the list a user approves), not a review-side rule. **The correction is right**, it is
disclosed as a correction, and it does not weaken the finding — which is `E12`'s instruction
exactly: reproduce to write the fix correctly, never to adjudicate the reviewer.

The design residual is banked as `checklist-cited-not-carried`. `R10` conformance checked by
hand: one row, three fields, target named as a clause (the checklist header sentence) rather than
"the corresponding file", redeem-when a round-eligible surface as `HD-37` (2) requires for a
design-shaped fix, and a deadline (the first caller that cold-starts on the product tier alone)
that is outside the round writing the row, as `HD-37` (1) requires. Bank 16 -> 17 rows.

### B-2 — cured for the caller, and the pinned literal survives

The obligation now stands on the round's opening in both carriers, mirroring the `E10` clause
this round wrote. I compared the mirror against `CONSTRUCTION-CHECKLIST.md:151` word by word; it
is faithful in substance in the template and in the Chinese instance.

The technique matters and it worked: the template's line 11 is pinned verbatim as a hand-written
literal in `DECISION_LOG_HEADER_LINES` (`tooling/tests/document_harness/test_init_command.py:59`,
`E5`), and the fix appended after that line rather than rewriting it. Extracted all six pinned
literals by AST and matched them against the template: **6/6 present**. The caller-facing half
verified end to end rather than inferred:

```
$ python tooling/dtw.py init --repo-root <fresh git repo>
  RESULT: 5 created, 0 left as found (exit 0)
  decision logs found: 1
  shipped instance line 13: "> surface. **The obligation is the round's opening, not the cold
                             read**: `§live` is owed at"
```

I re-ran the `HD-41` (4) scan class myself over all tracked `*.md` rather than accepting the
pasted one. It reproduces the fix's five-way division: `CONSTRUCTION-INDEX.md` (now `:38`) and
root `README.md:259` with its Chinese counterpart at `README.zh-CN.md:241` are already
waiver-independent and untouched; `HARNESS-DECISIONS.md:623` is `HD-5`'s own ruling sentence and
is reported rather than reworded — correct, and its status line does delegate the carrying to the
header this commit amends, which I checked; the rest are committed records and a superseded plan.
The `283` in the body is the count **before** the edit, which is what the body says it is:

```
$ git grep -c "§live" <rev> -- '*.md'   ->  166ee51: 283   0482a40: 287   0f0498f: 287
```

### L-1, L-3, L-4, L-5 — each followed to its ground truth

- **L-1.** 389 tracked files is right and stable at both `0482a40` and the tip. The product tier
  measures **59 files / 765,900 B / 0.730419 MiB** on this checkout — both figures reproduce
  exactly. The repository byte figure does not; see `V-1`.
- **L-3.** `:14` now reads "Three members sit outside the product tier", agreeing with `:56`.
  Three is right: the checklist and the two retired-contract stubs.
- **L-4.** Verified against `HD-1` itself, not against the citation. `HD-1`'s ruling text reads
  "journal 收窄为分析/推理/实测" and says nothing about one file per round; the archive holds no
  `HD-1` at all. The replacement's own claim also holds: over the whole tracked tree the shape has
  exactly three carriers outside the review records — `CONSTRUCTION-INDEX.md:37`, `README.md:169`,
  `README.zh-CN.md:160` — and `CORE-SET.md` puts all three on the construction side, so a caller
  carries none. Ruling 15's bound held: no owner was invented.
- **L-5.** The false header sentence is gone and the governing sentence ("where this file and that
  file disagree, that file governs") is kept, which is what caps the risk. The rows are unchanged,
  which is what the finding asked for.

### L-2 and L-6, routed outside the fix leg

Both corrections are accurate. The stripped trees do both measure 124 — the FULL was right and
`c5f00f6` was right. The plan carries seventeen numbered rulings (I counted them in the file) and
item M exists, so `十七条` and `item A-E + I/J/K/L/M` are both correct now. The entry's own policy
("全部落在该 plan，本行不复述") is why rulings 16 and 17 are not enumerated there, which is
consistent rather than short.

### L-7, L-8 sit in committed commit bodies and are immutable. Correctly left.

---

## 3. Do the guards still bind? (`R8`, `E4`)

The round wrote no guard, so `E4` falls due on nothing new. What I checked is that the guards the
fix leans on behave as its body claims, and that the fix's own bytes are covered — one of them is
not.

**`layer_path_check`.** Its pass on this diff is genuinely vacuous and the body says so: `LAYER`
holds 9 paths and none of the 9 touched paths is one, so the guard scans nothing. Replayed the
predicate over every line the range adds, with both controls:

```
POSITIVE CONTROL `document-harness/nope/missing.md`  -> 1 hit   (guard fires)
NEGATIVE CONTROL `document-harness/EXECUTION.md`     -> []      (guard silent)
added lines in range: 416   of which outside the review record: 51
unresolved added path tokens over those 51: 0
(the 3 hits in the range all sit inside the FULL's own record, which names deleted paths by design)
```

**`sweep_refs.py`** stands at 15 over 9 members, exit 0 — unchanged, as claimed, since no member
was touched. Two of the fifteen are the one ruled-dangling site (`REVIEW.md:93`, LINK + PATHTOK).

**`review_freeze_check`** binds by its own predicate rather than by an empty run:
`is_record("migration/document-work-assurance-v3/v3-review-verify-0f0498f.md")` -> `True`;
`is_record("CORE-SET.md")` -> `False`; `is_record("document-harness/README.md")` -> `False`;
marker present.

**Full battery, run last:**

```
$ python -m pytest -q     ->  854 passed in 413.91s
```

---

## 4. Findings

### V-1 · the fix's own byte figures are written in units and checkout states that do not reproduce

`E7`: the class, not the instance. Three sites in the repair diff, one class — a byte or
character figure whose stated scope does not determine its value.

**(a) `CORE-SET.md:34-36`.** "389 tracked files and 6.37 MiB. Scope of every figure here:
`git ls-files` at the tree this round's fix commit writes, worktree bytes summed by `stat -c%s`
under `core.autocrlf=true`." Worktree bytes are not a function of the tree in this checkout:

```
$ git ls-files --eol | awk '{print $1}' | sort | uniq -c   ->  389 i/lf
$ git ls-files --eol | awk '{print $2}' | sort | uniq -c   ->  315 w/crlf  73 w/lf  1 w/mixed
$ git ls-files | xargs stat -c%s | sum  (at HEAD)          ->  6,686,040 B = 6.3763 MiB -> 6.38
  reconstructed at 0482a40 (HEAD total minus the two files 0f0498f changed,
  each measured at both revs by git cat-file)               ->  6,684,800 B = 6.3751 MiB -> 6.38
  the executor's figure                                     ->  6,684,667 B = 6.3750 MiB -> 6.37
  all-389-CRLF, i.e. a fresh clone under the setting the scope names
  (sound because every tracked file is i/lf)                ->  6,704,068 B = 6.3935 MiB -> 6.39
```

The 133 B between the executor's total and the reconstruction is the LF count of the round
journal, which sat LF on disk when the figure was taken and CRLF afterwards. Nobody mis-measured:
the recipe simply does not pin a value. The product tier moves the same way — **0.730** here,
**0.732** (767,862 B) on a fresh clone. The file count, 389, is correct and stable.

**(b) journal `:121` and `0f0498f`'s body.** "The file is 180 lines and 53,607 bytes." The ledger
is **53,609 B** at the tree that sentence lives on, because the same commit added 2 B to it —
`L-1`'s own defect class, measure-last, recurring inside the commit that answers `L-1`'s sibling.
180 lines is right at both ends.

**(c) journal `:122` and the same body.** "one line — the CLOSED roll — is 26,110 characters, 49%
of the file". 26,110 is that line's **UTF-8 byte** length; its character length is **16,171**.
49% is right because both sides of that ratio are bytes. But the comparison in the next clause,
"the next largest being 2,405 characters", is a genuine character count, so the sentence sets a
byte figure beside a character figure: like for like the gap is 16,171 vs 2,405 by characters, or
27,357 vs 4,060 by bytes — 6.7x, not the 10.9x the sentence reads as. "57% of all entry content"
is right (56.7% by characters; 55.6% by bytes).

**What changes if it stays.** Nothing an actor does. Every conclusion each figure supports —
a caller carries a small fraction of this repository; a line-count bound cannot see growth inside
a line — survives the correction intact, and `CORE-SET.md`'s header already tells a reader to
re-run rather than cite. Reported because `L-1` was a finding of exactly this class one commit
earlier and the round's own standard is that a figure is emitted by the command that produces it.
Minimum fix, if taken: state the byte figures in **blob bytes** (`git cat-file`), which the tree
does determine, or drop the third digit. (b) and (c) are journal numbers, so `HD-23` routes their
correction outside the fix leg.

### V-2 · `CORE-SET.md`'s new "the gap is measured" measures one surface; the manifest it defines has more

The repair added: "**They are not a closed set, and the gap is measured**: all five product-tier
documents point back into the construction checklist below..." The FULL noted that nothing in the
round had ever exercised the manifest `CORE-SET.md` defines. I built it — the 59 product-tier
files and nothing else — and resolved every markdown link and every path-shaped backticked token
in its markdown against that set:

```
product-tier-only tree: 59 files, 29 references resolving nowhere
  6  the construction checklist            -> named by the new sentence
  7  contract v4 (:16 :25 :27 :30 :32 :253 :341) -> round 2's, E2-frozen, accounted in the journal
  1  document-harness/README.md:16         -> round 2's, accounted in the journal
  1  document-harness/REVIEW.md:93         -> dangling by ruling 13, accounted
 11  caller-held or run-time (control/ evidence/ .git/hooks/ .githooks/ docs/policy/
      ResearchSystem/HARNESS-POLICY.md ../../runs/...) -> compliant by design
  3  document-harness/ONBOARDING.md:12 :196 :206 -> `journal/caller-onboarding-2026-08-19.md` x2
                                                   and `journal/stranger-proof-walk-2026-08-24.md`
```

Those last three are a product-tier file citing this instrument's construction journals, which
`CORE-SET.md`'s own construction tier holds and a caller does not carry. Ruling 12's **test** — a
product-facing document may not depend on construction history — condemns them; its
**enumeration** was the eleven *member* sites, and `ONBOARDING.md` is not a member, so
`sweep_refs.py` never scans it and acceptance 1's grep was scoped to the three registers only.
That is the same shape the round's own journal §3 records as the lesson worth keeping: a ruling
stated as a test and illustrated by a list gets executed against the list. They predate the round
(`git grep -c` returns 3 at `cc3b3ab`, `92cc514` and the tip), so the round did not create them —
but they appear in no plan, no journal section, no rider row and no `CORE-SET.md` sentence.

The new sentence is not false: its colon defines "the gap" as the checklist dependency. It is
narrower than the standard this round set for itself, which is journal §2's "every one of the
thirteen residuals is accounted for". Minimum fix: either widen the sentence's scope statement to
the surface it actually measured, or account for the three the way the round accounts for
everything else.

### V-3 · the `B-2` fix's bytes are unguarded, and the run offered as its evidence is the proof

Mutation, both controls, on `document-harness/templates/decision-log.md`, restored from a
sha256-checked scratchpad copy (never `git checkout --`):

```
NEUTERED: the whole added waiver clause removed (3,805 -> 3,524 B)
  test_init_command.py                            -> 23 passed
  test_caller_surfaces.py + test_precommit_checks -> 84 passed        = 107 green
POSITIVE CONTROL: the pinned line 11 deleted instead
  test_init_command.py                            -> 1 failed, 22 passed
RESTORED sha256 2928910c14c20d835928fe8598a93820772c8867cf4179a80c904c5e36b96248  MATCH
$ git status --porcelain -> ?? .goals/    $ git diff --stat -> (empty)
```

107 is exactly the number the fix's body offers as its evidence, and it is unchanged by deleting
the sentence the fix exists to add. The pin reaches the *block* — delete line 11 and the suite
goes red — but not the clause appended after it, and the only machine references to this template
anywhere are `DECISION_LOG_HEADER_LINES` and a byte-identity test that compares the copy to the
template and so cannot pin content. This is the shape of the defect the test's own comment
records (`v3-review-full-2026a14.md` `B-2`: the inheritance line was absent for weeks with the
whole suite green). The fix disclosed the constraint that produced it — the round's boundary
admits no test change — but not that its bytes end up unguarded. Reported, not prescribed:
extending the literal is new machinery on a surface `E6` says to re-question rather than fence.

### V-4 · `0f0498f` routes three edits outside the `E9` fix leg; `HD-23` reaches two of them

`HD-23` covers 「journal 里的**数字**（**非结论**、非被评审的推理本身）」 and, through its
2026-08-04 parent, ledger/riders-only edits, on the condition that the correction lands inside the
next review's subject range. `L-2` is a journal number and `L-6` is ledger-only; both land in this
range. Both are correctly routed, and the FULL's `L-2` says so in as many words.

The third edit is not either of those. The withdrawal rewrites the round journal's §6 **conclusion**
— "the two instructions cannot both be followed" becomes "that was wrong" plus a measurement — and
`HD-23`'s own parenthesis excludes conclusions from what it routes. The journal is reviewed work
product: it was inside `cc3b3ab..92cc514`, the FULL read it in full and filed `L-2` against it. So
the 2026-08-04 criterion ("是不是被评审的 work product") does not carve it out either, and `E9`'s
test — has a valid independent FULL occurred? yes, `166ee51` — puts a post-FULL change to reviewed
work product in the fix leg, which `0482a40` already spent. `E9`'s closing sentence is the one at
issue: never self-classify which round consumed what.

**What is and is not wrong here.** Nothing is hidden: the commit states the withdrawal in full,
names it as its own thing and explains why it stands alone, which is `E9`'s "exceeding requires
saying so, never silently" met on the disclosure half. Nothing the FULL relied on moved — §6's
contradiction claim carried no finding, and the correction is substantively right (I read the
archive's own first line, "Moved verbatim, nothing deleted, nothing retyped", and the header's
remedy is indeed available). What is missing is a rule that puts it outside the leg; the commit
asserts "the fix leg stays spent exactly once" and cites `HD-23`, which does not reach this third
edit.

**Minimum fix**, and it is one sentence either way: the closeout records that the fix leg was
consumed a second time, **or** a recorded ruling extends `HD-23` to a round's withdrawal of its
own committed journal conclusion. There is a third reading I name without taking: `E8` lists
**errata** as a commit kind and `E9`'s budget vocabulary has no slot for one, which would make
correcting a conclusion you already committed structurally impossible after a FULL without
spending the leg — neighbouring the divergence rider `e9-pair-budget` already banks. Whether that
is a gap to open a round on is the user's, not mine (`R5`). I did not return `SPEC_GAP` because
the layer does answer as written: `E9`'s default catches it.

`R7` ceiling: if the user approved this withdrawal in conversation, I cannot see it.

---

## 5. Observations (`R5` — the question and the conclusion are the user's)

- **O-1 · `document-harness/README.md:24` says "this file is on the construction side of the core
  set".** Outside my subject range — it landed at `c0b9316`, inside the FULL's — and reported here
  only because I met it while following `CORE-SET.md`'s tiers. In a cell whose subject is
  `CONSTRUCTION-INDEX.md`, "this file" is true of the index; read as the file one is in, it is
  false, because `CORE-SET.md` entry 3 puts `document-harness/README.md` in the product tier. The
  intended reading is the correct one and no action changes either way.
- **O-2 · the new rider's declared scope is the five documents; the fix leg made a sixth.**
  `checklist-cited-not-carried` states its 量程 as "`CORE-SET.md` 产品档那五份文档".
  `templates/decision-log.md` is also product tier, and the sentence the fix added to it names
  "the instruction layer's cold read" — a concept defined in `E10`, in a file a caller does not
  carry. The instruction itself is self-contained, so a caller can act on it; the rider's scope
  simply does not reach the sixth carrier.
- **O-3 · the shape, restated because the repair extended it.** The FULL reported the root
  accumulating construction-side registers. The fix leg closed two blockers by adding one rider
  row (16 -> 17) and one disclosed-residual paragraph, and `CORE-SET.md` now records a gap it
  states no round of this batch settles. That is successive rounds closing findings by adding
  components, which `R5` asks me to report and not to judge.

---

## 6. `UNVERIFIABLE` and coverage (`R4`)

- **Read in full:** `document-harness/CONSTRUCTION-CHECKLIST.md` (standing instruction),
  `HARNESS-DECISIONS.md` `§live` and the header, `CORE-SET.md`, `CONSTRUCTION-INDEX.md`,
  `HARNESS-RIDERS.md`, the round journal, the whole subject diff, the three commit bodies, the
  FULL's record `v3-review-full-92cc514.md`, `sweep_refs.py`, `layer_path_check.py`,
  `review_freeze_check.py`'s predicate, `templates/decision-log.md`.
- **Read at the cited lines:** `document-harness/ONBOARDING.md`, `EXECUTION.md`, `REVIEW.md`,
  `ORCHESTRATION.md`, `document-harness/README.md`, `CONSTRUCTION-LEDGER.md`, the root
  `README.md` / `README.zh-CN.md`, `plans/core-set.plan.md` (rulings, steps, acceptance),
  `test_init_command.py`.
- **Probed only:** the 854-test battery (run to completion, not read);
  `contract/...-v4.md` (blob-compared and reference-scanned, not re-read — `E2`-frozen and
  untouched); `HARNESS-DECISIONS-archive.md` (grepped for `HD-1` only).
- **`UNVERIFIABLE`, stated rather than folded into supported:**
  - **That the user approved this fix, and its boundary.** Construction-round `E11` cards are ruled
    not to be committed, so there is nothing in the repository to check (`R7`).
  - **That `166ee51` committed the record unchanged.** Only the committed copy exists; the claim is
    unfalsifiable from here. Marked, not verified.
  - **The role form (`HD-55`)** — that the fix was written by a session other than the one that
    orchestrates. A process claim, marked, not verified. No commit states which of `E1`'s four
    holdings the executor held, and none is owed unless the round stood in the exception channel.
  - **The reconstruction in `V-1`(a)** of the worktree byte total at `0482a40`. It is arithmetic
    over measurements (HEAD's measured total, and the two changed files measured at both revs), not
    a direct measurement, because measuring it directly would mean mutating the tree under review.
    The fresh-clone figure is a computation warranted by `git ls-files --eol` reporting all 389
    files `i/lf`, not an observation of an actual clone.
- **This is a VERIFY, not a re-certification.** The mutations in §3 and `V-3` prove where the
  template pin has binding force and where it has none; they do not prove that force is sufficient
  anywhere. `layer_path_check` scanned nothing on this diff by construction, so nothing here
  re-tests it beyond the replayed predicate — and it remains blind to standing text, to bare-name
  tokens and to every file outside the nine, which is how `V-2`'s three sites survive every guard
  this repository owns.
