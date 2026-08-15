# V3 review — FULL — subject `f2507a5`

**Subject range** `7052a89b..f2507a5c` — two commits: `V3-REVIEW-RECORD-PHASE-C1.5-7052a89-v1`
(`7ff29b3`, R6 channel work) and `V3-PHASE-C1.6-CONTRACT-SUCCESSOR-AND-WORDING-v1` (`f2507a5`,
the candidate).

**Verdict: `CHANGES_REQUIRED`.**

The round's mechanical claims all hold and I proved each of them rather than accepting one: the
two module diffs are docstring-only at AST level, the frozen surface is untouched, the three
signed blobs still resolve, the five suites reproduce at the claimed counts, and the
versioned-successor mechanism the round invokes is real and quoted verbatim. The `issues.py`
wording correction is exactly right and is the best thing in the round.

It is blocked on what the round exists to do. This is a record-accuracy round: its whole payload
is making written sentences true. Four sentences it shipped are falsified by a one-line command,
and two of the four are the *replacements* for findings it says it paid — F-1's fix introduces a
new false claim about the same eight files F-1 was about, and F-3's fix corrects the cited line
while leaving the identical claim, in a stronger and more wrong form, 200 lines below in the same
file. That is not four typos; it is the reported instance being fixed and the defect class being
left (E7's discipline applied to a fix). §5 names all four with locations and minimum fixes; all
four land in one edit.

---

## 1. What this round is, re-derived

Not taken from the dispatch, which carried the range and nothing else (R2).

| Question | Answer | Where I read it |
|---|---|---|
| Round | **Phase C1.6** — contract successor + wording corrections, carried by the C1.6 section of `.goals/plans/harness-digest-narrowing.plan.md` | that plan §"C1.6 内容"; `HARNESS-LEDGER.md` pointer block |
| Governing instructions | `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` (E1–E12 / R1–R9); `v3-harness-review-contract.md` is a stub pointing there | contract stub banner; checklist header |
| Budget position | No `v3-review-*-f2507a5.md` existed → this **is** C1.6's FULL. `7ff29b3` is R6 channel work and consumes nothing. One user-approved fix + one targeted VERIFY remain for C1.6 (E9) | `ls migration/document-work-assurance-v3/`; `git log` on the range |
| Why C1.6 is a round at all | User ruling of 2026-07-29: the edits were authored in this worktree while C1.5's FULL was unreturned; the user ruled that concurrency their own side's problem and ruled the changes be treated as occurring after the FULL ended, which makes them a new round rather than C1.5's single repair | `HARNESS-LEDGER.md` 2026-07-29 entry; plan §"并发问题的用户裁决"; `f2507a5` body |
| Obligations | write `supersession-2` as a one-statement versioned successor with zero frozen bytes; pay F-1 and F-3; record F-2's correction; reword `issues.py`'s two immutability sentences into obligations without adding a mechanism; add the `run-v2/README.md` sentence; disclose the self-reversal; zero behaviour, zero schema, zero frozen existing bytes; five suites + repo-audit green | plan §"C1.6 内容"; `f2507a5` body |
| Verdict domain | FULL → `REVIEWED_NO_BLOCKER \| CHANGES_REQUIRED \| SPEC_GAP` (R3) | checklist R3 |

**Ceiling (R7).** Every authorization this round leans on — the concurrency ruling, the ruling
that a new file under `ResearchSystem/contract/` may be authored, the `issues.py` re-ruling, the
per-finding dispositions — was issued in chat. I see only the execution side's *records* of them
(`HARNESS-LEDGER.md`, the plan, the commit body). I take those at face value, state the ceiling,
and do not treat any of them as verified. The **E11 preview card** is chat-only and therefore
`UNVERIFIABLE` (R4). "Fresh context" is marked, not verified.

**One thing this FULL is explicitly not.** `supersession-2` is UNSIGNED prose successor to signed
text, so under E10 it owes an **independent read whose subject is that text alone, never banked as
a round's FULL** — the ledger states the mutual exclusion itself. This review is C1.6's FULL. It
does **not** discharge that read, and nothing here may be cited as having done so. Until that read
happens the accurate statement remains the ledger's: a written correction exists and is unread.

**Read coverage (R4).**

- *Read in full:* the complete diff of all 8 changed paths; `CONSTRUCTION-CHECKLIST.md`;
  `HARNESS-LEDGER.md`; `harness-digest-narrowing.plan.md`; the whole of
  `Document-Work-Assurance-Contract-v3-supersession-2.md`; the whole post-change bodies of
  `assurance_state.py` and `issues.py`; `v3-review-full-7052a89.md` (the C1.5 record, to establish
  what F-1…F-5 actually said); supersession-1 §3 and signed contract §13 in place; the C1.5 commit
  body (for its four-boundary enumeration).
- *Ran myself, pasted below:* all five suites; `repo-audit.py`; an AST equality test over both
  changed modules; a scripted digest audit of all 8 committed `state.json` files; `resume` against
  **all 8**; a synthetic-state probe of the unprotected-digest code path; four frozen-path sweeps;
  the three signed-blob resolutions; the sha256 of the committed review-record blob; call-site
  greps for `pointer_to` / `pointer_for` / `pointer`; the C1.5 test-diff numstat.
- *Sampled / not re-reviewed:* the unchanged bodies of `checks.py`, `review_subject.py`,
  `flow.py`, `summary.py` — the round touches none of them and the AST test proves it.
- *Not probed:* **no mutation probes were run and none were owed.** The round adds no guard, no
  test and no executable byte; there is nothing to mutate. E4/E5/E8-probe obligations are
  vacuous here, and I say so rather than let their absence read as an omission.
- *`UNVERIFIABLE`:* that `7ff29b3` reproduces the review session's original bytes. I can show the
  committed blob hashes to the value the commit body claims (§4), which proves the claim is
  self-consistent; I hold no independent copy of the source, so byte-fidelity to the reviewer's
  file is unverified, not supported.

---

## 2. Implementation (R3 — lead)

### The change is docstrings, and I proved it rather than reading the diff and agreeing

`git diff --numstat` reports `11/11` on `assurance_state.py` and `11/3` on `issues.py`. Parsing
both revisions and comparing the ASTs with docstrings stripped:

```
ResearchSystem/tooling/rsclib/document_harness/assurance_state.py
   raw source identical                : False
   AST identical with docstrings kept  : False
   AST identical, docstrings stripped  : True
ResearchSystem/tooling/rsclib/document_harness/issues.py
   raw source identical                : False
   AST identical with docstrings kept  : False
   AST identical, docstrings stripped  : True
```

So "zero behaviour changes" is established, not asserted. The one comment edit inside `resume`
("on these five" → "on a protected field") never reaches the AST at all. No test file changed
(`git diff --name-status` over the range lists none), so no guard was weakened and no guard was
added — which is why §1 records the probe obligations as vacuous rather than unmet.

### `issues.py` — the one thing in this round that is wholly right

The correction is the correct shape and for the correct reason. Line 5 now reads *"a written
issue is never edited"*, `record_issue`'s docstring reads *"never amend it afterwards"*, and an
added paragraph states plainly that nothing enforces it, that the module offers no edit path
"only because it declines to", and that the wording was what changed. I checked the load-bearing
half of that claim: `issues.py` exposes `record_issue`, `check_issue`, `check_triage`,
`triage_route`, `issue_digest`, `render_issue`, `load_issue` — there is no update, amend, patch or
write-back function, and `triage_route`'s own docstring says the absence is the design. The E6
reasoning is right and is the reasoning I would have applied: a sentence asserting as fact
something no code checks is the defect, and building enforcement to make the sentence true guards
the wrong thing.

It also correctly does **not** launder history. `cf51534` edited eleven p3-corr and w1-r1 issue
documents; the new text makes that a violated obligation rather than an impossible event, which is
the honest description.

### `assurance_state.py` — F-1's fix is right in its operative half and false in its supporting half

The operative sentence is now correct, and matches the minimum fix the C1.5 record proposed
verbatim: *"Only `DIGEST_PROTECTED_FIELDS` are **written** with a digest; a digest that is present
is checked on every field."* I confirmed both halves against the code — `pointer_for` gates only
the digest on the frozenset, and `resume`'s `expected = ref.get("digest_sha256")` branch is
field-independent — and against a synthetic state:

```
synthetic state, unprotected field WITH digest:
  verified          : ['resolved_plan_ref', 'work_spec_ref']
  present_unverified: []
  -> resolved_plan_ref (unprotected) in verified: True
```

The supporting sentence is where it breaks. See **B-1** in §5: the new text quantifies over *every
state file committed to this repository* and asserts `resume` verifies their unprotected digests
into `verified`. Running `resume` over all eight returns `verified=0` on every one of them.

### `run-v2/README.md` and the two contract claims

The README's added sentence — *"Of the five, only `review_ref` is written by these scripts
(`run_bind_v2.py`); the other four are authored outside this template"* — is **true**, and I
checked it exhaustively rather than spot-checking: every `*_ref=` assignment in
`templates/run-v2/` is `review_ref` (protected, `run_bind_v2.py:62`) plus the four unprotected
fields in `run_evidence_v2.py:212-218`. No other protected field is written anywhere in the
template.

`supersession-2`'s mechanism is sound and its quotations are exact. Signed contract §13 reads
*"Signed contracts are never amended in place; corrections create a versioned successor"* — the
file quotes it word for word, and supersession-1's own header cites the same rule. The superseded
bullet is reproduced verbatim from supersession-1 lines 100–102. E2 freezes the *existing* files
under `ResearchSystem/contract/`; a new file touches none of them, and the sweep below confirms it.
Its `cf51534` witness matches the issue document it cites (*"invalidating the digests held by all
five ISSUE_TRIAGE decisions"* — `git show --name-status cf51534` lists exactly five modified
p3-corr `user-decision-triage-*.json`).

Two of its statements are not sound. See **B-3** (a flat claim about `pointer_to` that `git grep`
falsifies) and **B-4** (the file attributes itself to the wrong round, contradicting the very
ruling that makes it C1.6 work).

---

## 3. Boundary / process conformance (R3 — run second)

**E3 — figures re-derived, pasted not described.** Measured on the worktree at `f2507a5` (clean
but for the untracked `ResearchSystem/docs/`, which predates this work):

```
document_harness            151 passed in 23.15s
document_harness_review     325 passed in 61.14s
tests/harness/run_tests.py  Ran 39 tests ... OK
stage_control               20 run, 0 failure(s), 0 error(s)
tooling/tests/run_tests.py  tests: 29   passed: 29   failed: 0   RESULT: OK
repo-audit.py (repo root)   RESULT: clean (exit 0)   EXIT=0
```

Exactly the claimed counts, and unchanged from C1.5 — which is the expected result for a
docstring-only round and is therefore weak evidence about this round specifically. I state that
rather than let five green suites imply coverage they do not provide: **nothing in this round's
payload is under test.** No test reads `__doc__`; no test reads the changed README; no test reads
`ResearchSystem/contract/`. The accuracy of every sentence this round shipped is enforced by
nothing. Whether that should change is not mine to conclude (R5, E6) — I record that it is the
condition under which B-1 through B-4 reached a commit.

**E2 — frozen surface intact.** All four sweeps empty, all three signed blobs unmoved:

```
git diff --name-status 7052a89 f2507a5 -- ResearchSystem/contract/
    A  ResearchSystem/contract/Document-Work-Assurance-Contract-v3-supersession-2.md   (add only)
git diff --name-only  -- ResearchSystem/schema/                              → (empty)
                      -- ResearchSystem/assurance/{runs,shadow}/             → (empty)
                      -- both exact oracles                                  → (empty)
                      -- '*.schema.json'                                      → (empty)

8ad404b12b3242e700d0ad215048dffccada7d9c  .goals/plans/document-work-assurance-harness-v3.plan.md
b2dbdf752d8c155e4c65b14b5f420b880b8184a1  ResearchSystem/contract/…-v3.md
68031fa2ca31272e31da0d42a9a02189d28fcc21  ResearchSystem/contract/…-supersession-1.md
```

The E2 reading is correct on its own terms: E2 freezes *existing* files there, and the round did
not touch one. I reached that reading independently before seeing that C1.5's FULL had referred
the same question to the user under R5, and the ledger records the user ruling it may proceed. My
ceiling on that ruling is §1's.

**The round does not launder C1.5.** It states in the plan, the ledger and the commit body that
C1.5 shipped as an explicit E2 override, that the override count since 2026-07-28 stays at three,
and that supersession-2 aligns the contract *going forward only*. I checked the commit body of
`7052a89` and it does describe itself as a violation rather than an E2-permitted exception. The
non-revision is real, and it is the correct call.

**E8 — git discipline.** Two commits, both new (author date == committer date on each, no
amend evidence); titles `V3-REVIEW-RECORD-PHASE-C1.5-7052a89-v1` and
`V3-PHASE-C1.6-CONTRACT-SUCCESSOR-AND-WORDING-v1`; one dense paragraph each; trailer grep
(`co-authored|generated with|signed-off`) returns `0`; not pushed (`origin/main..HEAD` = 237, and
no remote branch contains `f2507a5`). Each commit names its kind in its first sentence
("Candidate for Phase C1.6"; "Review record, committed by the execution side per R6"). All 8
changed paths sit inside the declared boundary.

**E9 — budget.** Correctly classified *for C1.6*: no FULL had occurred on this round, so the
candidate consumed nothing, and this FULL is C1.6's one FULL. The classification of C1.6 as a
round distinct from C1.5 is the user's, recorded, and not the execution side's own — which is what
E9's "never self-classify" clause requires. I report the resulting shape as an observation (O-1),
not a finding.

**E12 — range.** The dispatch wrote both endpoints. E12 requires the tip be `HEAD`, never a
written SHA, because a written tip is short by the commit that recorded the range. Here it cost
nothing — `git rev-parse HEAD` = `f2507a5c0fb6bc33b3a163271d0d1bdf1c8d3ee4`, and the round's own
records (plan, both ledgers) were written *inside* `f2507a5`, so no record was dropped. Recorded
as O-3 because the form, not the outcome, is what the rule governs.

**R6 — record channel.** `7ff29b3` committed the C1.5 record under the required title, and the
commit body's claimed digest matches the committed bytes exactly:

```
$ git show f2507a5:…/v3-review-full-7052a89.md | sha256sum
27d4033fef6ae14989027f7af8704bbb2cc3a6e3a4b95b6817797c5b9c169b7e
  claimed in 7ff29b3's body: 27d4033fef6ae14989027f7af8704bbb2cc3a6e3a4b95b6817797c5b9c169b7e
```

Per §1 this proves self-consistency, not byte-fidelity to the source.

**E1 — independence.** This review set its own questions, re-derived every figure from the
repository, and accepted no reported number. Where a figure of mine agrees with the round's, it is
because I ran the command.

---

## 4. Facts I established that the round does not claim

- **No committed state file is resumable at HEAD — none of the eight.** Every pointer in every
  committed `state.json` still names `ResearchSystem/generated/document-assurance/…`, a path the
  2026-07-27 run-home move retired:

  ```
  runs/p3-corr/control/state.json          verified=0 present_unverified=0 {POINTER-MISSING: 13}
  runs/w1-r1/control/state.json            verified=0 present_unverified=0 {POINTER-MISSING: 12}
  shadow/round-2/run-a1 · run-p3           verified=0 present_unverified=0 {POINTER-MISSING: 2}
  shadow/round-3/run-a1 · run-p3           verified=0 present_unverified=0 {POINTER-MISSING: 2}
  shadow/run-a1 · run-p3                   verified=0 present_unverified=0 {POINTER-MISSING: 2}
  ```

  **This is pre-existing and is not this round's doing** — C1.5's FULL noted it for p3-corr alone,
  parenthetically. I extend it to the whole corpus because it is the ground truth B-1 collides
  with, and because "the committed evidence corpus resolves to nothing" is a fact about the harness
  worth having stated once, in a place that is not a parenthesis.

- **The digest half of B-1's sentence is true.** All 8 committed states carry a digest on every
  unprotected pointer they have (8 of 8 on the two real runs, 1 of 1 on each shadow run) and on
  every protected one. Scripted, not sampled.

- **F-2's correction is supported by the command it names.** `git diff --numstat` over C1.5's
  `tests/` gives `61/0`, `69/0`, `75/1`, and the single deleted line is
  `{"state_mut": lambda state: state["coverage_ref"].pop("digest_sha256")}` — one modified test
  method, exactly as the plan now says.

- **The self-reversal disclosure is accurate.** `DIGEST_PROTECTED_FIELDS` reads back five members
  (`final_decision_ref`, `repair_decision_ref`, `review_ref`, `start_decision_ref`,
  `work_spec_ref`), and the AST equality above proves the frozenset region did not move in this
  round. Disclosing a reversal the reviewer would otherwise never have seen is the right instinct
  and I record that it checked out.

- **No live document was newly falsified.** Grepping every tracked file for the unqualified
  convention returns only: the plan and ledger (quoting it), `HARNESS-LEDGER-archive.md`
  (read-only history), closed-run scripts under `assurance/runs/` (pinned history), supersession-1
  (the superseded text) and supersession-2 (quoting to supersede). That is the correct set.

---

## 5. Blockers

All four are one-line edits and all four fit inside a single approved fix.

**B-1 — `assurance_state.py:14-20`. F-1's replacement text states a new falsehood about the same
eight files F-1 was about.** The new docstring reads *"every state file committed to this
repository predates the narrowing and carries digests on unprotected fields too, **and `resume`
verifies those into `verified` exactly as before**."* The antecedent of "those" is those files'
digests. Ground truth (§4): `resume` over all eight returns `verified=0`, `present_unverified=0`
and only `V3-STATE-POINTER-MISSING`, because their targets were relocated. The clause is true only
as a statement about the code path in the abstract — which I verified separately and which the
*preceding* sentence already says correctly. **Why this blocks rather than banks:** F-1 was banked
under R9 precisely because it was wording-level, and its payment re-created a wording error of the
same class in the same paragraph. A reader asking F-1's own question — "does committed evidence
still verify?" — is told yes; the answer is no, and that is not recoverable from adjacent text.
*Minimum fix:* delete the clause, or restate it as the code-path property it actually is ("a
digest that is present is verified wherever it appears") and leave claims about the committed
corpus to a command.

**B-2 — `.goals/plans/harness-digest-narrowing.plan.md:222`. F-3 was paid at the cited line and
left standing 200 lines below, in a stronger form.** The Goal now reads "行为上的净减" with a
blockquote listing all four additions. Line 222 still reads *"**为什么本轮是纯减法**：…所以不需要
新增任何检查；唯一的新增物是一个 frozenset 加一个 helper…"* — the heading still asserts a pure
subtraction, "no new checks were needed" is contradicted by the new `V3-STATE-POINTER-UNVERIFIED`
issue code, and "the only additions are a frozenset and a helper" is contradicted by the round's
own correction four paragraphs above it, which lists four. The surviving instance is the more
detailed and the more wrong one, and it undercounts exactly the two additions (a new issue code, a
new non-zero `rsc v3 status` exit path) that Phase C2's M6/M7 re-decision will need to know about.
*Minimum fix:* correct or delete line 222.

**B-3 — `Document-Work-Assurance-Contract-v3-supersession-2.md` §2, successor text. A flat claim in
contract prose that one command falsifies.** The successor text ends *"`pointer_to` remains
correct for what it does and **is no longer called directly**."* `git grep "pointer_to("` returns
six direct call sites in tracked run scripts — all under `assurance/runs/p3-corr/`:
`run_bind_candidate.py:161`, `run_bind_v2.py:62`, `run_evidence_v2.py:174/176/178/180` — and three
in live tests (`test_review_v2_subject.py:317/328/390`). The file holds itself to a higher standard
than this three bullets later: §4 qualifies the analogous claim about `pointer()` ("still accepts a
caller-supplied digest and is used directly by hand-written run scripts"), and its last bullet says
outright that *"a contract implying uniform coverage would be the same kind of defect this file
corrects"*. *Minimum fix:* qualify it — no longer the authoring path for new runs; closed-run
scripts and the helper's own tests still call it directly.

**B-4 — `…supersession-2.md:3`. The file attributes itself to the round the whole ruling says it is
not.** The status line reads *"authored at the Phase C1.5 round (2026-07-29)"*. Every other record
— the commit body, the plan's C1.6 section, the ledger — says these changes constitute C1.6
precisely so that they are not C1.5's single repair. "Round" is a term with budget consequences
here; a permanent contract file saying C1.5 is durable evidence that C1.5 took a post-FULL fix,
which is the opposite of the ruling that preserved its repair and VERIFY. Of the four this is the
one that outlives the plan and both ledgers. *Minimum fix:* "authored at Phase C1.6 (2026-07-29)".

---

## 6. Non-blocking findings

**F-a — `HARNESS-LEDGER.md:63-65` still asserts the pre-fix `issues.py`.** The 同批仍待裁 bullet
reads *"且 `issues.py` 声明 issue *immutable once written* 而 `cf51534` 编辑了它们"* — presented as
an open matter awaiting a ruling. It was ruled on and fixed by this very commit; `issues.py` no
longer says it. The live pointer block is the one file whose job is to be current. (The same bullet
also says "digest 删掉后", superseded by the 2026-07-29 narrow-don't-delete re-ruling — that half
is **pre-existing**, not this round's.) *Minimum fix:* strike the clause; the `check_triage` half of
the bullet stands and is still open.

**F-b — the plan still frames the same matter as unfixed, twice.** Line 84: *"（`issues.py` 那句
"immutable once written" 是代码里的声明…**这是一条发现，本轮不动**）"*. Line 219, honest boundary 3:
*"**这条声明与流程的矛盾仍然悬着**，不在本轮修"*. Both are live-tense and both are now false. The
round recorded the re-ruling at line 246 instead of changing the text — which is the shape E6's
both-sides clause names ("the fix is that text changing"). Defensible if the boundary list is read
as a frozen spec for C1.5's commit body; not defensible for line 84, which is not.

**F-c — the boundary indices in the C1.6 notes point at the wrong items.** Line 247 says
*"诚实边界 3 降级"* and quotes the closed-run item — which is #2 in the plan's list (line 218) **and**
#2 in `7052a89`'s commit-body enumeration. There is no reading under which it is 3. (Line 248's
*"诚实边界 4 改判"* for the `issues.py` item is correct against the commit body, where it is fourth,
but wrong against the plan's list, where it is third — the two enumerations order boundaries 3 and
4 oppositely, which is worth knowing before either is cited again.) A future session applying
"downgrade boundary 3" lands on the wrong boundary in both documents.

**F-d — `issues.py:70` keeps a verb the function does not perform.** The rewritten docstring reads
*"Write one observation."* `record_issue` builds and returns a dict; it never touches disk. This is
pre-existing wording, but the round rewrote that exact line while correcting a sentence for
asserting something the code does not do, and left a second one on the same line. Low.

---

## 7. Observations (R5 — reported, not concluded)

**O-1 — the budget shape.** C1.5's findings F-1 and F-3 were paid by a round that is not C1.5, so
C1.5 retains an unspent fix and VERIFY while C1.6 opened a fresh FULL, fix and VERIFY. E9 names
this shape by name — *"every recorded escape from the cap was a renamed round"* — and also supplies
the guard that was met: the classification was a user ruling, not a self-classification. Both facts
are true at once. I report the shape and its ceiling (§1: I see the ruling only as the execution
side recorded it); whether one body of work drawing two round budgets is acceptable is the user's
question, not mine.

**O-2 — successive rounds are accumulating documents around one narrowing.** C1.5 changed the code;
C1.6 added a contract successor, and that successor now owes an E10 read, which will produce its
own record, and B-3/B-4 mean it will produce findings. R5 asks me to report that shape when I see
it. I see it. The question of whether the correction chain is converging is the user's.

**O-3 — the dispatch wrote the range tip.** E12 requires `HEAD`. Verified harmless here (HEAD ==
the written tip; the round's records were written inside the tip commit), so this cost nothing —
recorded because the rule governs the form.

**O-4 — nothing tests this round's payload.** Stated in §3 and repeated here because it is the
standing condition, not a one-round accident: docstrings, the template README and
`ResearchSystem/contract/` are read by no test. Whether any of that should acquire a guard is
exactly the question E6 says to answer by re-questioning the guarded thing, and R5 says is the
user's to close.

---

## 8. Verdict

`CHANGES_REQUIRED`.

Nothing here is a code defect; there is no code in this round, and I proved that rather than
assuming it. The frozen surface is intact, the suites reproduce, the `issues.py` correction is
right in substance and in reasoning, the versioned-successor mechanism is real and correctly
invoked, and the round is scrupulous about not rewriting C1.5's override into an in-boundary act.

But this round's deliverable *is* the truth of written sentences, and it shipped four that a single
command falsifies — two of them inside the fixes for findings about exactly that. B-1 and B-2 are
the reported instance being repaired and the defect class being left; B-3 and B-4 put a falsifiable
claim and a wrong round attribution into the one artifact here meant to outlive every plan and
ledger in the repository. Passing them would mean a correction round can close while carrying
forward the class of error it was opened to remove.

All four fixes are one line each and fit a single repair. Two constraints on what comes next: the
repair is bounded to §5 and anything it touches is fair subject for the VERIFY; and **the E10 read
`supersession-2` owes is still owed** — this FULL is not it, may not be banked as it, and until it
happens the accurate statement is that a written correction exists and is unread, never that the
contract is aligned.

---

*Record written by the independent review session in the worktree (R6); the execution side commits
it, title `V3-REVIEW-RECORD-PHASE-C1.6-f2507a5-v1`. Every figure above was produced by a command
run against the worktree at `f2507a5`; reproduce them there.*
