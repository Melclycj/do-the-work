# Checkpoint read — `CONSTRUCTION-CHECKLIST.md` blob `d3228163`, the E2 clause deletion

**No verdict.** A read is not a round (R3): it spends no budget, carries no verdict, and its output
is findings tiered must-fix / low / observation. This is the independent re-read the convergence
clause of E10 owes on the amended bytes, and **no round, FULL or VERIFY, is banked as it.**

**Findings: 1 must-fix, 0 low, 4 observations.** The must-fix is **not in the subject text** — the
amended `E2` is clean, and I could not construct a defect in it. It is a record defect in the same
commit, and its fix touches no instruction-layer byte, so it owes no further C-3 read. Labels are
local to this record.

---

## 1. Subject, re-derived

```
$ git cat-file -t d32281636aa7adf0bb897a081b7dc42bb8037d9a
blob
$ git rev-parse 7615733:ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md
d32281636aa7adf0bb897a081b7dc42bb8037d9a
$ git rev-parse HEAD:ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md
d32281636aa7adf0bb897a081b7dc42bb8037d9a
$ git hash-object ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md
d32281636aa7adf0bb897a081b7dc42bb8037d9a
$ git status --porcelain ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md
(empty)
$ git rev-parse --short HEAD
7615733
$ git cat-file -p d322816 | wc -l
122
```

`HEAD` held still for the whole of this read — checked at the start and again at the end. The
worktree carries one untracked path, `ResearchSystem/docs/`, unrelated to the subject and present
before this read began.

`git diff dcced4e d322816` is the amendment and nothing else: **one hunk in `E2`**, two lines out
and two in.

```
-  the `schema/document-assurance-v3/` pack, which `rsclib/document_harness` already treats as
-  one frozen object. Three blobs and one directory, both decidable by inspection, so nothing
+  the `ResearchSystem/schema/document-assurance-v3/` pack.
+  Three blobs and one directory, both decidable by inspection, so nothing
```

Two edits, both of them findings from read `dcced4e` being paid: **D-1**, the clause *"which
`rsclib/document_harness` already treats as one frozen object"* deleted (that read's `M-1`); **D-2**,
the pack path given its `ResearchSystem/` prefix (that read's banked wording-level finding). Nothing
was added. No other rule in the file moved.

---

## 2. The precondition, checked before anything else

C-3's route is available only *"for as long as no round has relied on the text."* R2 forbids
accepting the commit's assertion of it.

```
$ git log --format='%h %s' 11d147e..7615733
7615733 V3-E2-DELETE-FALSE-JUSTIFICATION-v1
956aa74 V3-REVIEW-RECORD-E2-SCHEMA-PACK-READ-dcced4e-v1
f854b72 V3-RULING-NEXT-ITERATION-THRESHOLD-v1
$ for c in f854b72 956aa74 7615733; do git show --stat --format='' $c; done
 ResearchSystem/HARNESS-LEDGER.md                   |  6 ++++++
 .../v3-checkpoint-read-dcced4e.md                  | 325 +++++++++++++++++++++
 ResearchSystem/HARNESS-LEDGER.md                   | 13 ++++++++++-
 .../document-harness/CONSTRUCTION-CHECKLIST.md     |  4 ++--
$ git diff --stat 11d147e..HEAD
 ResearchSystem/HARNESS-LEDGER.md                   |  19 +-
 .../document-harness/CONSTRUCTION-CHECKLIST.md     |   4 +-
 .../v3-checkpoint-read-dcced4e.md                  | 325 +++++++++++++++++++++
 3 files changed, 345 insertions(+), 3 deletions(-)
```

Three commits, three files: one ruling recorded in the ledger, one review record, one amendment.
**No code, no schema, no test, no fixture, no contract byte.** None is a FULL, a fix or a VERIFY.
I read `f854b72`'s ledger hunk rather than trusting its `--stat`: it is a threshold ruling that
*characterizes* the amended `E2` and takes no outcome from it, which E10 names as citing, not
reliance. The wider window back to `f054a08` I classified in the previous read and it is unchanged
— no commit was inserted into it.

**The route was available.**

---

## 3. The amendment against the finding it answers (R3 — implementation first)

Read `dcced4e`'s `M-1` said the deleted clause asserted as code behaviour something only a module
docstring said. I re-derived the numbers rather than accepting either the finding as previously
written or the commit's restatement of it, and re-measured now rather than carrying them (E3):

```
$ python -   (glob of the pack vs. SCHEMA_FILES parsed from __init__.py)
on disk: 14 | SCHEMA_FILES: 10
unregistered: ['assurance.schema.json', 'harness-issue.schema.json',
               'review.schema.json', 'review.v2.schema.json']
$ git ls-tree -r HEAD | grep -E "8ad404b12b32|b2dbdf752d8c|68031fa2ca31"
8ad404b12b32…  .goals/plans/document-work-assurance-harness-v3.plan.md
68031fa2ca31…  ResearchSystem/contract/Document-Work-Assurance-Contract-v3-supersession-1.md
b2dbdf752d8c…  ResearchSystem/contract/Document-Work-Assurance-Contract-v3.md
```

**D-1 is the right fix and is complete.** The clause is gone; the rule it was attached to is
untouched; nothing was added in its place. The two conditions that make a deletion safe here both
hold. Nothing else in the file referenced it —

```
$ git cat-file -p d322816 | grep -n -iE "rsclib|document_harness|frozen object|pack"
25:  the `ResearchSystem/schema/document-assurance-v3/` pack.
```

the sole surviving hit being `E2`'s own noun, whose referent is now the explicit path beside it. And
the rule still decides everything it needs to without the clause: three blob ids and one directory
path, `git ls-tree` and `ls` respectively.

**D-2 pays the banked finding in full.** Both unprefixed strings are gone — one prefixed, the other
carried out with the clause. No path in `E2` is now written in a form that fails to resolve from
where it sits.

**The ragged line is conformance, not sloppiness.** D-1 left *"the
`ResearchSystem/schema/document-assurance-v3/` pack."* short of the file's wrap width because the
following line was not re-flowed. Re-flowing it would have re-typed unchanged prose, which is what
E10's *"never re-typed 'with the same content'"* forbids. The diff is minimal in exactly the way
that rule asks for.

**I could not construct a defect in the amended text.** The list is four items in two kinds, both
kinds decidable by inspection; the closure sentence no longer asserts anything about other tracks;
the three blob literals resolve uniquely and are unchanged. Read `dcced4e`'s low finding — *existing*
not pinning a moment — survives untouched and the commit says so explicitly rather than quietly
dropping it. That is the correct handling and it is not re-raised here.

---

## 4. Must-fix

### M-1 — the ledger item the user will rule from still says the concurrency shape has happened twice; it has happened three times, and the mitigation adopted in response exists in no file

**Location:** `HARNESS-LEDGER.md:246-251`, against the commit body of `7615733`. **Ground truth it
violates:** the repository's own record of the shape.

The ledger carries an item explicitly parked for the user:

```
$ sed -n '246,251p' ResearchSystem/HARNESS-LEDGER.md
- **待用户裁（2026-07-29，C1.6 的 VERIFY 按 `R5` 交回，reviewer 不下结论）：并发形状第二次发生。**
  `bed6161` 在 C1.6 的 FULL 仍在跑时落到同一分支上（FULL 自记 HEAD 为 `f2507a5`…）
  …
  上下文两条：C1.6 这个轮次**本身**就是上一次同样的事逼出来的用户裁决；…
  **第二次是否可接受、以及要不要把「发生」的判据写进 `E9`，是用户的问题。**
```

It is open, it names the second occurrence, and it names its own context: the round it arose in was
itself forced by the first occurrence. `7615733`'s commit body reports a third — *"this execution
side moved HEAD during the read … the third occurrence of that shape"* — and I can evidence all
three from the repository: occurrences one and two in the lines above, occurrence three in
`v3-checkpoint-read-dcced4e.md` §5 O-a, committed at `956aa74`, where I recorded `HEAD` moving from
`11d147e` to `f854b72` mid-read.

**Two things are missing from where they will be looked for.**

*The count.* The ledger item still reads 第二次. Nothing in the file records a third:

```
$ grep -n -E "第三次|三次|并发形状" ResearchSystem/HARNESS-LEDGER.md
19:  - **状态 (2026-07-28)：Phase A 完成**（… 三次修复 → 四次独立 read …）
246:- **待用户裁（…）：并发形状第二次发生。**
309:    **计数不变：2026-07-28 以来 explicit override 共三次**（…）
341:    第三次 override。**排序：C2 之后**（…）
```

Lines 309 and 341 count a different thing (explicit overrides). The user is asked at line 251
whether the *second* occurrence is acceptable; they will answer that question with the third
already on the board and not in front of them.

*The mitigation.* The commit body states a new operating practice — *"while a read or review is
out, records wait and are batched afterwards"* — and it appears nowhere else:

```
$ git grep -rn -iE "batched afterwards|while a read.*out|records wait|批量.*提交" -- ResearchSystem/ .goals/
(no output)
```

E10 enumerates the instruction layer and a commit body is not in it; the ledger, which the project's
navigation makes the first thing a new session reads, does not carry it. A practice recorded only in
one commit body among many is a practice a future execution session will not find, which is the
failure mode this harness has an instruction layer to prevent.

**Why must-fix rather than low.** This is the same class as read `f9a6600`'s `M-2` and read
`dcced4e`'s `M-1`, both of which the user chose to correct: a fact in the basis of a user decision
being wrong while the decision itself stands. Here the decision is still pending, which makes it
cheaper to fix and worse to leave — the record goes stale *before* the ruling rather than after it.
Not wording-level under R9 on either half: the count changes what the user decides from, and the
practice changes what a future executor does.

**Precision, so this is not overstated.** Adopting a stricter voluntary practice is *not* the same
as answering the parked question, which asks whether the shape is acceptable and whether a criterion
for *occurred* belongs in `E9`. The executor tightening its own behaviour needs no ruling, and I am
not reporting it as one taken. What I am reporting is that neither the increment nor the tightening
reached the file where the question waits.

**Minimum fix — two lines in the ledger, no machinery, no instruction-layer byte (E6).** Append to
the existing `待用户裁` item: the third occurrence with its two citations (`f854b72` landing during
the read recorded at `956aa74`), and the adopted practice, marked as a voluntary tightening that
does not pre-empt the parked question. Because the fix touches no instruction-layer text, **it owes
no C-3 re-read and costs no further turn of this loop** — it rides the next commit that touches the
ledger.

---

## 5. Observations

**O-a — the dispatch's turn count and the commit's disagree by one; the commit's series is
internally consistent.** This dispatch says *"Sixth turn of the `E10` convergence route"*;
`7615733`'s body says *"fifth turn"*. Counting the C-3 amendments myself — `af2905c`, `87a4ced`,
`6f96139`, `11d147e`, `7615733`, excluding `f054a08` because it was a round's repair — gives five,
matching the commit and matching its two predecessors, which said *"third turn"* and *"fourth
turn"* at the right places. The two previous dispatches agreed with their commits; this is the first
to diverge. Nothing turns on it, and the dispatch says of itself that its facts are pointers to be
verified. Recorded so the number in circulation does not drift.

**O-b — what the amendment got right, re-derived.** Covered in §3 rather than repeated here, with
one addition: the ledger correction landed with the numbers rather than as a bare retraction —
`10` / `14` / the four unregistered files / the one-directional test / the `W1-record.md:100` bound
that keeps the digest exposure latent are all in it, and each is one I re-derived independently
before this read rather than accepted.

**O-c — the ledger correction again struck the false words in place and appended a note quoting
them.** *"与代码对上"* was removed from the ruling line and the appended `⚠ 事实更正` block quotes
it back verbatim before saying it is false. Identical shape to the correction one turn earlier,
which read `dcced4e` recorded as O-c and found lossless. It is lossless again. Repeated once so the
pattern is visible as a pattern; no rule I can find makes the live ledger append-only, so this is
not a finding.

**O-d — two consecutive turns have now ended with the ruling standing while a stated reason for it
did not.** Turn four corrected *"no live-code reader"*; turn five corrected *"matches the code"*.
The commit names this itself. The shape worth reporting under R5 is not that the executor made two
errors — it is that on this route the justification is written by the same session that wants the
ruling, and the only thing that has caught either was the read afterwards. The question of whether
that is an acceptable steady state is the user's; the count is what I can supply.

---

## 6. Disclosure (R4)

**Read in full:** the subject (`CONSTRUCTION-CHECKLIST.md`, 122 lines, read end to end this session
rather than carried from the previous read) — both my standing instruction and my subject, since
`v3-harness-review-contract.md` is a 6-line stub redirecting to it; the amendment diff
`dcced4e..d322816`; the commit body of `7615733` and its complete `HARNESS-LEDGER.md` hunk;
`f854b72`'s and `956aa74`'s stats and `f854b72`'s hunk; `HARNESS-LEDGER.md` lines 240-256.

**Sampled:** `HARNESS-LEDGER.md` elsewhere by grep only (`HEAD` / `worktree` / occurrence counts /
the batching phrase); my own prior record `v3-checkpoint-read-dcced4e.md` consulted for what it
asked for, not re-read in full; `rsclib/document_harness/__init__.py` re-parsed for `SCHEMA_FILES`
by script rather than re-read, its surrounding code having been read in full one read ago and
unchanged since (`git diff --stat 11d147e..HEAD` shows no `.py` path).

**Probed only:** the search for the batching commitment — one grep over `ResearchSystem/` and
`.goals/` in four phrasings, English and Chinese. Absence by grep is weak evidence of absence, not
proof, and M-1's second half is written to that ceiling. The dangling-reference check on the subject
was a single grep for four terms.

**Not verified.** The commit's five suite counts and `repo-audit exit 0`: described rather than
emitted, the pattern the `25f2916` ruling declined to mechanize; second consecutive read in which it
recurs, and this amendment touches two markdown files and no code, so the figures bear on nothing in
the subject and I have not banked them. That occurrences one and two of the concurrency shape
happened as the ledger describes — I read the ledger's account, not the underlying events.

**Marked, not verified (R4):** that this session is fresh context — a process claim, marked as such.
That the ledger's parked question at line 246 is genuinely still open rather than answered in
conversation; I can see the record, not the exchange, which is R7's ceiling and not a block, and it
is the reason M-1 asks for an append rather than asserting the user is uninformed.

**`UNVERIFIABLE`:** which of the three occurrences the commit counted, beyond the two I can place
from the ledger and the one I recorded myself — the mapping is consistent with three but the
repository does not timestamp a read's window, so I cannot exclude that the executor counted a
different set of three. Also unverifiable from the repository: whether *existing* in `E2` was meant
to freeze future additions, unchanged from the previous read and still carrying that read's low
finding.
