# Checkpoint read — `Document-Work-Assurance-Contract-v3-supersession-2.md`, blob `a7d71215`

**No verdict.** A read is not a round (R3): it spends no budget, carries no verdict, and its output
is findings tiered must-fix / low / observation. This is the independent re-read E10's convergence
clause owes on the amended bytes, and **no round, FULL or VERIFY, is banked as it.** Nothing below
may be read as certifying the §3 rewrite; §5 O-1 records why that matters here specifically.

**Findings: 1 must-fix, 0 low, 1 banked wording-level, 5 observations.** The must-fix is on the §3
hunk — the one edit in this amendment that did not come from a read's finding. The two edits that
did (§4's `instruction_ref`, §1's count) are correct, and I re-derived both rather than accepting
them. Labels are local to this record; read `6e30c07`'s `M-1` / `L-1` are different findings.

---

## 1. Subject, re-derived

```
$ git cat-file -t a7d71215cfd7f312865c5414928f143978b396d0
blob
$ git rev-parse 4e80df7:…/Document-Work-Assurance-Contract-v3-supersession-2.md
a7d71215cfd7f312865c5414928f143978b396d0
$ git rev-parse HEAD:…/Document-Work-Assurance-Contract-v3-supersession-2.md
a7d71215cfd7f312865c5414928f143978b396d0
$ git hash-object <worktree copy>
a7d71215cfd7f312865c5414928f143978b396d0
$ git status --porcelain <path>
(empty)
$ git rev-parse --short HEAD          # start of read, and again at the end
4e80df7
$ git cat-file -p a7d7121 | wc -l
108
```

`HEAD` held still for the whole of this read, unlike the previous one. The worktree carries one
untracked path, `ResearchSystem/docs/`, which predates this work.

**The subject is not the checklist.** `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md`
remains my standing instruction, unchanged at blob `d3228163` (`git rev-parse HEAD:<path>`), which
is the blob I read end to end in the immediately preceding read. Supersession-2 is inside E10's
instruction layer as *"any prose successor to signed text"*, which its own §5 asserts and the prior
read verified; that is why C-3 applies to it at all. It is **not** in E2's frozen list — E2 names
supersession-**1** by blob `68031fa2`, and this file is a different object.

`git diff 6e30c07 a7d7121` is the amendment and nothing else: **three hunks**, in §1, §3 and §4.

- **A-1 (§1, line 33)** — *five* → *eight* committed ISSUE_TRIAGE decisions. Pays read `6e30c07`'s
  `L-1`, which that read banked as wording-level.
- **A-2 (§3, lines 66-70)** — the version boundary is rewritten from *"Newly opened runs author
  pointers under the successor text"* to an authoring-path test. **This answers no finding of read
  `6e30c07`**; §5 O-1 gives its provenance.
- **A-3 (§4, second bullet)** — `instruction_ref` removed from the `digestRef` list and explicitly
  excluded, with the reason. Pays read `6e30c07`'s `M-1`, its only must-fix.

---

## 2. The precondition, checked before anything else

C-3's route is available only *"for as long as no round has relied on the text."* R2 forbids
accepting the commit's assertion of it.

**Window.** Twenty-five commits between the authoring round's repair and this amendment:

```
$ git log --format='%h %s' 293f657..4e80df7 | wc -l
25
```

I classified each by its own `--stat`. They are: nine review records; three dispatch commits; seven
ruling / closeout / ledger commits; six `CONSTRUCTION-CHECKLIST.md` amendments; and this one. The
union of paths they touch is `HARNESS-LEDGER.md`, `CONSTRUCTION-CHECKLIST.md`, records and
dispatches under `migration/document-work-assurance-v3/`, `.goals/LEDGER.md`, two files under
`.goals/plans/`, and the subject. **No code, no schema, no test, no fixture byte in any of them.**

**One round occurred in the window** — the E10/E2 amendment round (`af2905c` candidate → `9db2313`
FULL → `f054a08` repair → `6798ebc` VERIFY → `5760f8b` closeout). Its subject was the checklist's
`E2`/`E10`, and its outcome turned on whether files under `ResearchSystem/contract/` are *signed*,
never on what this file says. Its two review records mention supersession-2, so I checked what the
mentions do rather than counting them: they classify it (an UNSIGNED successor, therefore outside
E2), which is citing, not taking governance from the text.

**The one code-side mention is a docstring.** `assurance_state.py` lines 112-115, inside
`pointer_to`'s docstring: *"Supersession-1 §3 named this helper as* the *authoring path …
supersession-2 (2026-07-29) supersedes that one statement."* No branch, no constant, no behaviour
reads this file. E10 excludes citing explicitly.

**The route was available.** For A-1 and A-3 it is also the right route; A-2 is a different question,
in §5 O-1.

---

## 3. What the two finding-driven edits do, re-derived (R3 — implementation first)

**A-3 is correct and its every predicate holds.** All four declarations of `instruction_ref` `$ref`
`frozenFileRef`, and that shape requires what the new sentence says:

```
$ git grep -A1 '"instruction_ref": {' -- 'ResearchSystem/schema/**'
document-work-spec.schema.json        → common.schema.json#/$defs/frozenFileRef
document-work-spec.v2.schema.json     → common.schema.json#/$defs/frozenFileRef
instruction-coverage-audit.schema.json→ common.schema.json#/$defs/frozenFileRef
review.schema.json                    → common.schema.json#/$defs/frozenFileRef
$ python -   (required sets from common.schema.json)
pointerRef    required: ['path']
digestRef     required: ['path', 'digest_sha256']
frozenFileRef required: ['path', 'revision']
```

*"nothing requires or checks a digest on it"* holds across every reader: `instruction.py:87`,
`review.py:647` and `review_result_v2.py:165` each compare `("path", "revision")` and nothing else.

**A-1's number is right, and I derived it without using the executor's method.** Rather than reading
`cf51534 --name-status` and counting, I recomputed every committed triage decision's
`target.harness_issue_ref.digest_sha256` against the bytes of the issue document it names:

```
$ python -   (recompute all user-decision-triage-*.json at HEAD)
triage decisions found: 10
at HEAD -> match: 2  stale: 8  unresolvable: 0
STALE p3-corr  command-exit-subject-tree / no-dispatch-generator /
               no-vocabulary-for-repaired-blocker / template-next-action-round-blind /
               template-write-text-newline                                        (5)
STALE w1-r1    freeze-check-paths / pointer-digest-kind / unmapped-preamble        (3)
MATCH p3-corr  digest-binds-nothing-against-the-only-writer / harness-knowledge-in-memory
```

Eight stale, split five and three, which is the figure the amendment now carries. Note the split is
not the same set `cf51534` *modified* — that commit touched seven triage decisions and nine issue
documents; the eighth decision went stale because the issue under it changed, not because the
decision did. The amended sentence says *invalidated the digests of*, which is the accurate
predicate for all eight.

---

## 4. Must-fix

### M-1 — §3's two branches are predicated on different objects, so a run can satisfy both; and the second branch classifies as *prior text* a script doing exactly what the successor text prescribes

**Location:** subject lines 66-68 (§3, first sentence). **Ground truth it violates:**
`assurance_state.pointer_for` and this file's own §4.

```
66  A run authors pointers under the successor text when its control plane is written by
67  `assurance_state.pointer_for`; a run whose scripts call `pointer_to` or `pointer` directly
68  is under the prior text.
```

Branch one is about **the control plane** being written by `pointer_for`. Branch two is about **the
run's scripts** calling `pointer_to` or `pointer` *anywhere*. Those are not complements, and the gap
is not theoretical.

**`pointer_for` emits `pointer(path)` itself.** Read back from
`ResearchSystem/tooling/rsclib/document_harness/assurance_state.py:133-139`:

```python
    if field in DIGEST_PROTECTED_FIELDS:
        return pointer_to(path, repo_root)
    if not (pathlib.Path(repo_root) / path).is_file():
        raise AssuranceFault(f"pointer target does not exist: {path}")
    return pointer(path)
```

For every unprotected field the policy's own output *is* a bare `pointer(path)`. So a hand-authored
script that writes `pointer(path)` for an unprotected field produces byte-for-byte what the
successor text prescribes — and branch two puts its run under the **prior** text, under which that
same pointer would be obliged to carry a digest. The rule classifies compliant behaviour as
non-compliant.

**Both branches fire on the configuration §4 says to expect.** The same file, two bullets down:

> **Only one protected field has a live write path.** Of the five, only `review_ref` is authored by
> `templates/run-v2/` (`run_bind_v2.py`); the other four are written by hand-authored run scripts…

> `assurance_state.pointer(path, digest)` still accepts a caller-supplied digest and is used
> directly by hand-written run scripts, so a run authored by copying an existing precedent will
> keep writing digests on unprotected fields.

A real run therefore has a template-derived control plane and hand-authored scripts beside it. I
confirmed the template half is clean — the only `pointer` occurrences under
`assurance/templates/run-v2/` besides its five `pointer_for` calls are two comment lines — so such
a run satisfies branch one, and §4 says its hand-authored half will satisfy branch two. §3 then
returns two answers, and what turns on the answer is whether the digest obligation applies to
thirteen state pointers or to five.

**Why this is must-fix rather than banked.** The whole purpose of this hunk, in the user's recorded
scope — *"§3 换可判定的界"* — was to replace a boundary nothing could decide with one that could.
The replacement is decidable per call site and undecidable per run, which is the unit the sentence
quantifies over ("A run authors…"). It changes an obligation, so R9's wording-level test fails at
its first condition. And the accurate answer is not recoverable from adjacent text: §4 is what makes
the collision, not what resolves it.

**Minimum fix — re-scope, no new machinery (E6).** Either make both branches the same object, which
is the smaller edit: *"A state pointer is authored under the successor text when it is written by
`assurance_state.pointer_for`; one written by `pointer_to` or `pointer` directly is under the prior
text"* — per pointer, which is the granularity §2's successor text already uses (*"A state pointer
carries…"*). Or keep the run as the unit and make branch two the strict complement of branch one —
*"a run whose control plane is written any other way is under the prior text"* — which is
subtractive and drops the helper enumeration that causes the collision.

---

## 5. Banked under R9

### §1 now says *eight* while the source it cites in the same sentence says *five*

Line 33 carries the corrected number and, four words later, its witness:
`issue-p3-corr-digest-binds-nothing-against-the-only-writer`. That issue is scoped to one run
(`"run_id":"p3-corr"`), where five is exact; the repo-wide figure is eight because w1-r1 contributes
three. The number is now right and the citation is now narrower than the number.

**Wording-level and banked:** no obligation turns on it — it is evidential background in *"witnessed
grounds"* — and the accurate fact is recoverable, since the three extra decisions are found by the
same recomputation that produced the eight, and my §3 above prints the split. The decision that
would go wrong without recovery is a reader checking the citation, finding five, and concluding the
contract overstates its own evidence; it does not survive the check. Rides the next batch touching
this file; it spawns no round and no read. Read `6e30c07` offered *"restore the scope (p3-corr's
five)"* as its alternative fix, which would also have closed this.

---

## 6. Observations (R5 — reported, the conclusion is the user's)

**O-1 — the §3 clause is the one edit here that answers no read finding, its own author recorded
that it needed a FULL, and the route taken cannot give it one.** Read `6e30c07`'s findings were
exactly `M-1` and `L-1` (its §4 has two `###` headings and no more); §3 appears in that record only
under `UNVERIFIABLE`, as a forward statement no opened run could exercise. The §3 rewrite came from
the user adding it to C1.7's scope, which `HARNESS-LEDGER.md:121-127` records —
*"**C1.7 范围因此 = `M-1` + `L-1` + §3 换可判定的界**，零额外轮次"* — so the authorization is visible
in the repository and this is not an unauthorized escape (R7). The same ledger block, two sentences
earlier, also records:

> **这是执行侧读法、不是裁定**（`E1` 不许自审自己写的文本），交 C1.7 的 FULL 复核。

C1.7's FULL did not happen: the work went down the C-3 route, which yields an amendment plus a read,
and R3 is explicit that a read *"carries no verdict."* So the independent check the execution side
itself asked for on its own reading of §3 has not occurred, and **this record cannot supply it** — I
can report a defect in the clause, which I have, but I cannot certify the clause. That E10's C-3
clause is scoped to *"a read's must-fix findings"* and says nothing about material folded in
alongside them is the same gap read `9f2ec9a` recorded as its `L-3`; there it was a low finding
riding along, here it is a substantive new clause. Whether a FULL is still owed on §3 is the user's
question, not mine (R5). What I can supply is the one fact that bears on it: the first independent
reader of the clause found a defect in it.

**O-2 — what verified clean, re-derived rather than accepted.** Beyond §3's two edits: 
`DIGEST_PROTECTED_FIELDS` holds exactly the five fields §2 names, read back member by member
(`assurance_state.py:81-89`); `pointer_for` applies the field policy and delegates to `pointer_to`
exactly as §2 describes; `templates/run-v2/` uses only `pointer_for`; the three blobs E2 freezes are
unchanged and this file is not among them. Read `6e30c07`'s much larger clean-verification table I
did not re-run in full — see §7.

**O-3 — the `M-1` fix took a third option, and it is the better one for a reader who saw the old
text.** Read `6e30c07` offered replacing `instruction_ref` with the START decision's
`target.instruction_audit_ref`, or dropping the name. The amendment kept the name and excluded it
explicitly, with the reason and an admission that it *"was named here in error"* — an erratum in the
document that made the error, which is where it belongs. One consequence: the `digestRef` list in
that bullet is now two items and does not include the START decision's `instruction_audit_ref`,
which is a genuine member. That the prior read accepted *"dropping the name entirely"* as a full fix
shows exhaustiveness was never the requirement, so this is reported, not raised.

**O-4 — this amendment touched no ledger, unlike every prior amendment in this chain.** The six
checklist amendments before it each carried a `HARNESS-LEDGER.md` hunk; `4e80df7` is one file. The
corrections it makes are recorded in the file itself and in the commit body, which for the §4
erratum is the right home. Recorded because the ledger is where a new session is told to start, and
the C1.7 scope item at line 109 still reads **挂起** with no note that it has now been executed.

**O-5 — read `d322816`'s must-fix has not landed, and is not yet overdue by its own terms.**
`grep` for the concurrency shape's third occurrence returns nothing in `HARNESS-LEDGER.md`; the item
at line 246 still reads 第二次, and the batching practice announced in `7615733`'s body is still in
no file. That finding said explicitly that it rides the next commit touching the ledger, and neither
`ee13860` (record only) nor `4e80df7` (this file only) touches it, so nothing is late. The practice
itself appears honoured on its first test: `HEAD` did not move during this read.

---

## 7. Disclosure (R4)

**Not a fresh context, and this is the first record to say so.** This read shares a session with the
three preceding checkpoint reads (`f9a6600`, `dcced4e`, `d322816`), whose texts and findings were in
context before this dispatch arrived. Earlier records marked *"fresh context"* as a process claim
that could not be verified; here I can state affirmatively that it does not hold. What that buys and
costs: I did not need to re-derive the E2 chain's history, and I carried forward my own reading of
`CONSTRUCTION-CHECKLIST.md` at blob `d3228163` rather than re-reading its 122 lines, having read
them in full one read earlier at the identical blob. What it costs is the independence R1 is
about — I am not blind to the previous three subjects, and O-5 above is a self-reference. Read
`6e30c07`, by contrast, was written by a different session, which is why §3's re-derivations here
are worth what they are.

**Read in full:** the subject (108 lines); the amendment diff `6e30c07..a7d7121`, all three hunks;
the commit body of `4e80df7`; read `6e30c07`'s record (265 lines); `HARNESS-LEDGER.md` lines
103-130; `assurance_state.py` lines 78-140; `instruction.py` lines 82-96.

**Sampled:** `HARNESS-LEDGER.md` elsewhere by grep only; `review.py` and `review_result_v2.py` at
the `instruction_ref` comparison sites and their field tuples, not their surrounding functions;
`templates/run-v2/` by grep for `pointer` rather than read; the twenty-five window commits by
`--stat` plus the bodies of the two that touch a plan file.

**Probed only:** call-site enumeration for `pointer_for` / `pointer_to` / bare `pointer(` across
`*.py`, which is how M-1's collision was established — a grep-derived inventory, so a call reaching
these helpers through an alias or a dynamic attribute would not appear in it.

**Not run, and not owed:** no test suites, no mutation probes. The subject adds no code, no guard
and no executable byte; E4/E5/R8 are vacuous against a prose subject. The commit's five suite counts
and `repo-audit exit 0` are described rather than emitted, the pattern `25f2916` declined to
mechanize — third consecutive read in which it recurs, and it bears on nothing in this subject, so I
have not banked it.

**Marked, not verified (R4):** that the user's 2026-07-29 adjudication narrowing state-pointer
digests, and the C1.7 scope addition, were put to and answered as the ledger records; I can see the
records, not the exchange, which is R7's ceiling and not a block.

**`UNVERIFIABLE`:** whether §3's boundary works in practice, unchanged from read `6e30c07` — no run
has opened under it, and §4 discloses that four of the five protected fields have no shipped write
path to exercise. M-1 does not depend on that: it is derived from the text against
`pointer_for`'s own return values and this file's own §4, both of which are present today.
