# V3 review — VERIFY — subject `293f657`

**Subject range** `f2507a5c..293f657b` — three commits: `V3-PHASE-C1.6-F4-DISPOSITION-v1`
(`bed6161`, pre-submission correction, **never reviewed by the FULL**),
`V3-REVIEW-RECORD-PHASE-C1.6-f2507a5-v1` (`10aeb10`, R6 channel work) and
`V3-PHASE-C1.6-REVIEW-FIX-v1` (`293f657`, the repair).

**Verdict: `REVIEWED_NO_BLOCKER`.**

All four accepted blockers are paid, and each one I reproduced against the repository before
judging the fix rather than reading the new sentence and agreeing with it. B-1's replacement is
now a statement about the code path, and I proved that property twice — by synthetic state and by
a mutation probe that turns the guard behind it red at value level. B-2's line 222 now agrees with
the Goal correction 200 lines above it, and both enumerate the same four additions, each of which
I verified exists. B-3's flat claim is qualified and the qualification is exhaustive against
`git grep`. B-4's attribution is corrected and that line was the file's only round attribution.
The code change is docstring-only at AST level, the frozen surface is intact, the three signed
blobs are unmoved, and all five suites plus repo-audit reproduce at the claimed counts.

Three non-blocking findings and four observations below. None of them is a blocker and I say so
rather than inflating one: a VERIFY carries no repair budget, and an inflated finding here would
buy nothing and cost the accuracy of the word.

---

## 1. What this round is, re-derived

Not taken from the dispatch, which carried the range and nothing else (R2).

| Question | Answer | Where I read it |
|---|---|---|
| Round | **Phase C1.6** — the targeted VERIFY obliged by its one user-approved fix | `HARNESS-LEDGER.md` pointer block (`NEXT = VERIFY`, base `f2507a5`); `.goals/plans/harness-digest-narrowing.plan.md` §"C1.6 的 FULL 与修复" |
| Governing instructions | `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` (E1–E12 / R1–R9); `v3-harness-review-contract.md` is a stub pointing there. Where the checklist is silent the retired contracts at `7011916` are the reference of record, by the checklist's own header | contract stub; checklist header |
| Budget position | C1.6's FULL occurred (`v3-review-full-f2507a5.md`, `CHANGES_REQUIRED`, committed `10aeb10`); the repair `293f657` is the round's one user-approved fix; **this is the VERIFY it obliges**. C1.5's own fix and VERIFY remain separately unspent | `git log`; `ls migration/document-work-assurance-v3/`; ledger |
| Accepted findings | The four blockers of §5 — B-1 `assurance_state.py:14-20`, B-2 `plan:222`, B-3 `supersession-2` §2, B-4 `supersession-2:3`. The four non-blocking findings F-a…F-d were **banked, not repaired**, which R3 requires of a repair bounded to §5 | `v3-review-full-f2507a5.md` §5–§6 |
| Verdict domain | VERIFY → `REVIEWED_NO_BLOCKER \| SPEC_GAP` (R3) | checklist R3 |

**Ceiling (R7).** Every authorization this round leans on is chat-only and I see only the
execution side's record of it: the user's approval of a repair **bounded strictly to §5**, the F-4
ruling recorded in `bed6161`, the earlier concurrency ruling, and the E11 preview card. I take
those at face value, state the ceiling, and treat none of them as verified. "Fresh context" is
marked, not verified (R4).

**What this VERIFY is not.** It is not a re-certification of Phase C1.6 (R4). It is not the E10
read `supersession-2` owes — and that read is now owed on the **amended** text, because this
repair changed that file's bytes. Until it happens the accurate statement remains the ledger's:
a written correction exists and is unread.

**Read coverage (R4).**

- *Read in full:* the complete diff of all five changed paths across all three commits; the
  post-change bodies of `assurance_state.py` and `Document-Work-Assurance-Contract-v3-supersession-2.md`;
  `HARNESS-LEDGER.md`; `harness-digest-narrowing.plan.md` §§Goal / 199–276; the whole of
  `v3-review-full-f2507a5.md`; `CONSTRUCTION-CHECKLIST.md`; `README.md`; the retired operating
  contract's rules 4–9 at `7011916`; the `PointerHelper` test class.
- *Ran myself, pasted below:* all five suites separately; `repo-audit.py`; an AST-equality test
  over the changed module; `resume` over all eight committed `state.json`; a three-case synthetic
  probe of the resume code path; a `coverage.py` run over **all five suites** measuring the run-v2
  template; `git grep "pointer_to("` and `"pointer_for("`; four frozen-path sweeps; the three
  signed-blob resolutions at both range ends; the sha256 of the committed review-record blob at
  `10aeb10` and at `HEAD`; one mutation probe with sha256-checked restore; E8 git-discipline greps.
- *Sampled / not re-reviewed:* every module the round does not touch. The AST test and the
  five-path `--name-only` prove it touches none of them.
- *`UNVERIFIABLE`:* (i) that `10aeb10` reproduces the review session's original bytes — I can show
  the committed blob hashes to the claimed value and is unchanged at `HEAD`, which proves
  self-consistency; I hold no independent copy. (ii) Whether the FULL had **returned** when
  `bed6161` was authored (O-B). (iii) Every chat-only authorization above.

---

## 2. The four accepted findings (R3 — lead)

### B-1 — paid, and the replacement is the first repaired sentence in this round with a guard behind it

The false clause (*"and `resume` verifies those into `verified` exactly as before"*) is deleted.
The surviving text states the code-path property and hands the corpus question to a command:

> *"a digest that is present is verified wherever it appears, on protected and unprotected fields
> alike … Whether any particular committed state still resolves is a question for a command, not
> for this docstring."*

I reproduced the ground truth first. `resume` over all eight committed states:

```
runs/p3-corr/control/state.json    verified=0 present_unverified=0 {'V3-STATE-POINTER-MISSING': 13}
runs/w1-r1/control/state.json      verified=0 present_unverified=0 {'V3-STATE-POINTER-MISSING': 12}
shadow/round-2/run-a1 · run-p3     verified=0 present_unverified=0 {'V3-STATE-POINTER-MISSING': 2}
shadow/round-3/run-a1 · run-p3     verified=0 present_unverified=0 {'V3-STATE-POINTER-MISSING': 2}
shadow/run-a1 · run-p3             verified=0 present_unverified=0 {'V3-STATE-POINTER-MISSING': 2}
```

Then the surviving claims, one at a time:

```
synthetic state, digests on protected AND unprotected fields:
  A verified            : ['resolved_plan_ref', 'summary_ref', 'work_spec_ref']
  A unprotected verified: ['resolved_plan_ref', 'summary_ref']
```

— so "verified wherever it appears, on protected and unprotected fields alike" is true of the code
path, which is what the sentence now claims and all it claims.

*"every state file committed to this repository predates the narrowing"* — true: all eight were
last written by `2687d8c` (2026-07-28), and the narrowing is `7052a89` (2026-07-29).
*"and carries digests on unprotected fields too"* — true and exhaustive, not sampled: 8 of 8
unprotected refs carry a digest on each of the two real runs, 1 of 1 on each of the six shadow
runs, and **zero** unprotected refs anywhere lack one.

**The property is under test, and I proved the test binds** (R8). The guard is
`tests/document_harness_review/test_review_v2_subject.py::PointerHelper::test_resume_still_refuses_a_hand_written_wrong_digest`,
whose last assertion is `assertIn("resolved_plan_ref", point.verified)`. Mutation — narrow
`verified[field] = ref["path"]` to protected fields only, the real shape of the defect that would
make the new sentence false:

```
PRE-SHA256    : b6f28f4dc6a2af8a38e19bf5ed1a3a675568ce0aa89efd13bd36e856dfa0dd41
MUTATION APPLIED: verified[] narrowed to protected fields only
>           self.assertIn("resolved_plan_ref", point.verified)
E           AssertionError: 'resolved_plan_ref' not found in {}
FAILED …::PointerHelper::test_resume_still_refuses_a_hand_written_wrong_digest
1 failed, 42 deselected in 0.30s
RESTORE-SHA256: b6f28f4dc6a2af8a38e19bf5ed1a3a675568ce0aa89efd13bd36e856dfa0dd41   MATCH: YES
negative control after restore: 43 passed in 21.19s
```

Value-level failure, not a crash — the test touches the behaviour and binds it. Restored from a
sha256-checked scratchpad copy; `git checkout --` was not used (E4).

### B-2 — paid, and the defect class is closed, not only the reported instance

Reproduced at the base first:

```
$ git show f2507a5:.goals/plans/harness-digest-narrowing.plan.md | sed -n '222p'
**为什么本轮是纯减法**：…所以不需要新增任何检查；唯一的新增物是一个 frozenset 加一个 helper…
```

Line 222 now names the net subtraction as one of **obligation** and enumerates four additions. I
verified each of the four exists rather than counting the words:

| claimed addition | verified |
|---|---|
| `DIGEST_PROTECTED_FIELDS` frozenset | added by `7052a89` (`git diff fb77e95 7052a89`), five members read back |
| `pointer_for` helper | added by the same diff |
| new issue code `V3-STATE-POINTER-UNVERIFIED` | added in `resume` by the same diff; **not** the pre-existing `V3-SUBJECT-POINTER-UNVERIFIED`, which that round *narrowed* |
| new non-zero `rsc v3 status` exit path | `rsc.py:267` returns `0 if point.report.ok else 1`; synthetic probe: protected field without digest → `issues=['V3-STATE-POINTER-UNVERIFIED']`, `report.ok=False` → **exit 1**, where the pre-narrowing code raised no issue |

`git grep "纯减法"` now returns only the Goal correction (lines 19–22), the fixed line 222, the
F-3/B-2 finding rows, and the FULL record quoting it. The Goal blockquote and line 222 enumerate
the *same* four — the two-places-one-claim shape B-2 was about is gone, not relocated.

### B-3 — paid, and the qualification is exhaustive rather than plausible

The successor text now reads *"no longer the authoring path for a newly opened run — closed-run
scripts under `assurance/runs/` and the helper's own tests still call it directly, and nothing here
asks them to change."* Every direct call site:

```
$ git grep -n "pointer_to("
ResearchSystem/assurance/runs/p3-corr/run_bind_candidate.py:161
ResearchSystem/assurance/runs/p3-corr/run_bind_v2.py:62
ResearchSystem/assurance/runs/p3-corr/run_evidence_v2.py:174 / 176 / 178 / 180
ResearchSystem/tooling/tests/document_harness_review/test_review_v2_subject.py:317 / 328 / 390
ResearchSystem/tooling/rsclib/document_harness/assurance_state.py:100 (def) / 135 (pointer_for delegation)
… plus prose in the plan, W2-design and the FULL record
```

Six run-script sites, all under `assurance/runs/p3-corr/` — a run the ledger records CLOSED — and
three test sites, all inside the `PointerHelper` class, two of them literally
`test_pointer_to_*`. So "the helper's own tests" is accurate, and the enumeration leaves nothing
out: no site outside those two categories exists, and `templates/run-v2/` contains none at all
(all five are `pointer_for` now). The claim it replaces is no longer falsifiable by that command.

### B-4 — paid, and the file carries no second attribution

Line 3 now reads *"authored at Phase C1.6 (2026-07-29)"*. Grepping the whole file for
`C1\.5|C1\.6|Phase C|round` returns line 3 plus six occurrences of "round" used generically
("Newly opened runs", "never banked as a round's FULL", "lives in the round record"). There is no
second round attribution to correct.

---

## 3. The whole repair diff, and the commit the FULL never saw (R3)

**The code change is docstrings, proved not assumed.** Parsing both revisions of the one changed
module and comparing ASTs with docstrings stripped:

```
ResearchSystem/tooling/rsclib/document_harness/assurance_state.py
   raw source identical               : False
   AST identical with docstrings kept : False
   AST identical, docstrings stripped : True
```

`git diff --numstat f2507a5 293f657` — five paths, and the whole of the largest is the review
record being committed verbatim:

```
15   2  .goals/plans/harness-digest-narrowing.plan.md
17   5  ResearchSystem/HARNESS-LEDGER.md
 4   2  ResearchSystem/contract/…-supersession-2.md
423  0  ResearchSystem/migration/…/v3-review-full-f2507a5.md
 7   6  ResearchSystem/tooling/rsclib/document_harness/assurance_state.py
```

**The repair did not touch what it banked.** `issues.py` is absent from the range entirely, so F-d
stands where the FULL left it (`issues.py:70` still reads *"Write one observation."*). Plan line 84
still carries F-b's live-tense clause verbatim; line 219 likewise; lines 247–248 (F-c's mis-indexed
boundaries) are unchanged; the ledger's 同批仍待裁 bullet still asserts the pre-fix `issues.py`
(F-a). Four for four banked, none quietly repaired, which is what a repair bounded to §5 owes.

**The review record was committed and left alone.** `10aeb10` adds the record and nothing else,
and its bytes are unchanged at `HEAD`:

```
$ git show 10aeb10:…/v3-review-full-f2507a5.md | sha256sum
c8b7c33ae5f07889bb0052853e7e74506d4b8a081771e991c814bd321d4517a1
$ git show HEAD:…/v3-review-full-f2507a5.md      | sha256sum
c8b7c33ae5f07889bb0052853e7e74506d4b8a081771e991c814bd321d4517a1
  claimed in 10aeb10's body and in plan:252: c8b7c33a…
```

Self-consistent, and no later commit edited the record it received. Byte-fidelity to the reviewer's
source stays `UNVERIFIABLE` per §1.

**`bed6161` — the commit outside the FULL's subject.** It records the F-4 ruling in the plan's
findings table and the ledger and changes no code. I checked its load-bearing premise rather than
accepting it, and the check is stronger than the one the commit offered: a `coverage.py --branch`
run across **all five suites** reports the five template `pointer_for` call sites as never
executed —

```
run_evidence_v2.py   99 stmts  37 miss  58%   Missing: 156-157, 163-249, 253
   (the four call sites are lines 212 / 214 / 216 / 218 — inside 163-249)
run_bind_v2.py       not measured at all — never imported by any suite
   (the fifth call site is line 62)
```

— while `pointer_for` the *function* is covered by two tests, exactly the distinction the ruling
insists on. The other half of the ruling's ground also holds: a protected field silently degraded
to path-only is caught at once (synthetic probe case B above → `V3-STATE-POINTER-UNVERIFIED`,
`report.ok=False`), so the harmless half is what would go unguarded. The E6 reasoning is sound and
the disposition is the user's, not mine to second-guess (R5).

---

## 4. Permanent boundaries (R3 — run second, however narrow the round)

**E2 — frozen surface intact.** Sweeps over the range, and the signed blobs resolved at *both*
ends:

```
git diff --name-status f2507a5 293f657 -- ResearchSystem/contract/
    M  …/Document-Work-Assurance-Contract-v3-supersession-2.md    (see V-b)
                      -- ResearchSystem/schema/                    → (empty)
                      -- ResearchSystem/assurance/{runs,shadow}/   → (empty)
                      -- both exact oracles                        → (empty)
                      -- '*.schema.json'                            → (empty)

f2507a5 → 293f657, unchanged:
  8ad404b12b3242e700d0ad215048dffccada7d9c  .goals/plans/document-work-assurance-harness-v3.plan.md
  b2dbdf752d8c155e4c65b14b5f420b880b8184a1  ResearchSystem/contract/…-v3.md
  68031fa2ca31272e31da0d42a9a02189d28fcc21  ResearchSystem/contract/…-supersession-1.md
```

All three match the digests E2 names. The one `contract/` modification is the round's own UNSIGNED
successor, edited because the FULL named two of its lines as the defect and E6's both-sides clause
says the fix is that text changing. The retired contract at `7011916` — the reference of record the
checklist header names — states the rule as *"**Signed bytes** are untouchable (approved plan,
contracts, N0 schemas…)"*, and this file is explicitly UNSIGNED. So the act is in boundary. The
wording of the compressed E2 is not, and that is V-b.

**E3 — figures re-derived and pasted, measured last.** Run immediately before this record was
written, on the worktree at `293f657` (clean but for the untracked `ResearchSystem/docs/`, which
predates this work):

```
document_harness            151 passed in 18.53s
document_harness_review     325 passed in 49.48s
tests/harness/run_tests.py  Ran 39 tests ... OK
stage_control               20 run, 0 failure(s), 0 error(s)
tooling/tests/run_tests.py  tests: 29   passed: 29   failed: 0   RESULT: OK
repo-audit.py (repo root)   RESULT: clean (exit 0)   EXIT=0   (exit read from the process, not a pipe)
git status --porcelain      ?? ResearchSystem/docs/
git rev-parse HEAD          293f657bd17c2ebcad02a7ea7b1802f8cbc4343e
```

Exactly the claimed counts, and unchanged from the FULL — the expected result for a round whose
payload is prose, and therefore weak evidence about this round specifically. The round says so
itself and does not let five green suites imply coverage they do not provide. See O-C for the one
place where that statement is now too modest.

**E8 — git discipline.** Three commits, all new (author date == committer date on each, no amend
evidence); titles `V3-PHASE-C1.6-F4-DISPOSITION-v1`, `V3-REVIEW-RECORD-PHASE-C1.6-f2507a5-v1`,
`V3-PHASE-C1.6-REVIEW-FIX-v1`; one dense paragraph each, trailer grep
(`co-authored|generated with|signed-off`) returns `0`; not pushed (`origin/main..HEAD` = 239, and
only the local `document-work-assurance-v3` contains `293f657`). Each body names its kind in its
first sentence — *"Pre-submission correction"*, *"Review record, committed by the execution side
per R6"*, *"Review fix for Phase C1.6"* — so attribution needed no asking. All five changed paths
sit inside the round's declared boundary.

**E9 — budget.** The FULL had occurred and returned `CHANGES_REQUIRED`, so `293f657` is the round's
one fix and it obliges this VERIFY, which is what happened. `10aeb10` is R6 channel work and
consumes nothing. `bed6161`'s classification as a pre-submission correction rests on a timing fact
the repository cannot show — see O-B; nothing in this round turns on it.

**E12 — range.** The dispatch wrote both endpoints again; see O-A. Verified harmless here.

**E1 — independence.** I set my own questions, re-derived every figure, and accepted no reported
number, including the ones I ended up agreeing with. Where a figure below matches the round's, it
is because I ran the command.

---

## 5. Non-blocking findings

**V-a — the repair's own line references were stale the moment they were written.** Plan line 263
and `HARNESS-LEDGER.md:58` both locate banked finding F-a at *"ledger 63-65"*. The same commit
rewrote the C1.6 bullet above it (`17/5`) and moved that bullet to **lines 68-70**. Wording-level
under R9: both sentences name the bullet by its content (*the 同批仍待裁 bullet's `issues.py`
immutability clause*) in the same breath, so the accurate fact is recoverable and no actor's action
changes — the cost is a moment's search when F-a is paid. Rides the next batch touching those
files, alongside F-a itself.

**V-b — `293f657`'s body says *"no existing file under `ResearchSystem/contract/` modified"*, and
one command returns `M`.** `git diff --name-status f2507a5 293f657 -- ResearchSystem/contract/`
lists `supersession-2`. The claim is substantively true — under the rule of record (`7011916`
rule 5) the freeze is on *signed* bytes and this file is UNSIGNED — and the same commit body
describes the two edits to that file at length, so no reader is misled. What it exposes is real
and is not this round's fault: **E2's compressed phrase "existing files under
`ResearchSystem/contract/`" reads more broadly than the rule it compresses.** The downstream
decision that goes wrong if it stays: a future round told by a FULL to correct its own unsigned
successor reads E2 literally, concludes the cleanest fix needs a frozen byte, and takes `SPEC_GAP`
or an in-boundary detour where a direct edit was always permitted. I do not raise this to
`SPEC_GAP` — the checklist header says silence is not a defect and points at `7011916`, which
resolves it — but it is worth a clause when the instruction layer is next opened. Naming which
rule should carry that clause is not mine to conclude (R5).

**V-c — a stray English word inside `bed6161`'s Chinese plan text.** `plan:235` reads *"并进 C0
复验already记下的那笔欠账"*. Pure typo; the ledger's parallel sentence is clean. Zero decision
impact; rides any batch touching the plan.

---

## 6. Observations (R5 — reported, not concluded)

**O-A — the dispatch wrote the range tip again.** E12 requires the tip be `HEAD`, never a written
SHA. This VERIFY's dispatch wrote `293f657`. Verified harmless: `git rev-parse HEAD` =
`293f657bd17c2ebcad02a7ea7b1802f8cbc4343e`, and the round's records (plan §"C1.6 的 FULL 与修复",
the ledger pointer) were written *inside* that commit, so nothing was dropped. Recorded because the
FULL already recorded the identical form as O-3 one round ago and the form recurred.

**O-B — the concurrency shape recurred, and its disposition rests on a fact the repository cannot
show.** `bed6161` landed on this branch at 13:24:40 while the C1.6 FULL was in flight — the FULL
records `git rev-parse HEAD` = `f2507a5`, so it measured before that commit, and its record was
committed twenty minutes after it at 13:44:42. The execution side classified `bed6161` as a
pre-submission correction on the ground that no FULL had *occurred*; whether the FULL had
**returned** at 13:24 is chat-timing and therefore `UNVERIFIABLE` (R4), not supported. Nothing in
this round turns on it: `bed6161` changes no code, touches no text any of the four blockers rest
on, and the fix round came afterwards and obliged this VERIFY. It is recorded because the user
ruling that created Phase C1.6 exists precisely because this shape happened once, and E9 warns that
"every recorded escape from the cap was a renamed round" — whether a second occurrence is
acceptable is the user's question, not mine.

**O-C — a correction to the FULL's O-4, in the round's favour.** O-4 said nothing tests this
round's payload. That is true of the *sentences* — no test reads a docstring, the template README
or `ResearchSystem/contract/`. It is now too modest about one of them: the *property* B-1's
replacement asserts is bound by a live guard, and §2 shows that guard going value-level red under
the mutation that would falsify the sentence. Of the four repaired claims, exactly one has a test
behind it; the other three remain enforced by nothing, which is the condition the FULL recorded and
which this round did not change.

**O-D — the standing fact of §4 of the FULL still holds at `293f657`.** None of the eight committed
`state.json` files is resumable: every pointer in every one still names the pre-2026-07-27
run-home path, `verified=0` across the corpus. Re-measured, unchanged, and still not this round's
doing — B-1's fix was to stop the docstring claiming otherwise, which it now does.

---

## 7. Verdict

`REVIEWED_NO_BLOCKER`.

The four accepted findings are paid at their locations and by their minimum fixes, and in two cases
by more than the minimum: B-2 closed the defect class rather than the cited line, and B-3's
qualification is exhaustive against the command that falsified its predecessor. The repair stayed
inside §5 — all four banked findings are demonstrably untouched — the code change is docstring-only
at AST level, the frozen surface is intact with all three signed blobs unmoved, and every figure
reproduces. `bed6161`, which no FULL had seen, checks out on its own premise and by a stronger
measurement than it claimed.

Two things this verdict does not do. It does not discharge the **E10 read `supersession-2` owes**,
and that read's subject is now the *amended* text, B-3 and B-4 included; until it happens the
accurate statement is that a written correction exists and is unread, never that the contract is
aligned. And it does not certify Phase C1.6 as a whole (R4) — it answers for the accepted findings,
the repair diff, and the permanent boundaries, and for nothing else.

---

*Record written by the independent review session in the worktree (R6); the execution side commits
it, title `V3-REVIEW-RECORD-PHASE-C1.6-293f657-v1`. Every figure above was produced by a command
run against the worktree at `293f657`; reproduce them there.*
