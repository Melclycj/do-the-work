# Amendment checkpoint read — `6e30c07` (`Document-Work-Assurance-Contract-v3-supersession-2.md`)

**Subject, re-derived before reading any content:** blob
`6e30c07f42268c9e7ad28dac2b6ed07cc6324d35`, read with `git cat-file -p` — 6482 bytes, 102
lines. It is the current state of
`ResearchSystem/contract/Document-Work-Assurance-Contract-v3-supersession-2.md` and has been
since `293f657`:

```
git rev-parse HEAD                       7ae4a76d7f2e266a049a985409dab539c93dced2
git rev-parse HEAD:…supersession-2.md    6e30c07f42268c9e7ad28dac2b6ed07cc6324d35
git rev-parse 293f657:…supersession-2.md 6e30c07f42268c9e7ad28dac2b6ed07cc6324d35
git hash-object <worktree copy>          6e30c07f42268c9e7ad28dac2b6ed07cc6324d35
git log --follow --oneline <path>        293f657 V3-PHASE-C1.6-REVIEW-FIX-v1
                                         f2507a5 V3-PHASE-C1.6-CONTRACT-SUCCESSOR-AND-WORDING-v1
git status --porcelain                   ?? ResearchSystem/docs/   (untracked, predates this work)
```

The subject is a text, not a range, so `7ae4a76` and `afd80ef` — the two commits on this
branch after `293f657` — do not touch it and are outside this read.

**This is a read, not a FULL or a VERIFY.** E10: the read's *"subject is the amendment text
itself, never the work it governs"*, and it *"is never banked as a round's FULL"*. R3: it
*"spends no budget, carries no verdict, and its output is findings tiered must-fix / low /
observation"*. There is no verdict below and none may be inferred from the absence of
must-fix findings beyond the one recorded.

**Governing instructions.** `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md`
(E1–E12 / R1–R9). The path the dispatch named,
`v3-harness-review-contract.md`, is a stub whose banner points there and names it *"its own
counterpart"*; where the checklist is silent the retired contracts at `7011916` are the
reference of record, by the checklist's own header.

---

## 1. The three dispatch pointers, verified

The dispatch said they are pointers, not conclusions. Each was checked against the
repository; two hold as written, one needs correcting.

**(1) The `E10` obligation exists and is undischarged — holds.** E10 covers *"any prose
successor to signed text"* and requires that *"each amendment passes an independent read
before any round relies on it."* The subject is such a successor (§5 says so itself) and the
text it succeeds is genuinely signed — see §3 below. No discharging record exists:
`grep -rl "supersession-2\|supersession 2\|6e30c07"` over
`migration/document-work-assurance-v3/` returns four files — this read's dispatch, and the
three review records of the authoring round — and **no** `v3-checkpoint-read-*.md`. Reading
the subject line of all twelve existing checkpoint reads confirms none takes this text as its
subject.

**(2) Both reviews of the authoring round declined to be this read — holds, in their own
words.** `v3-review-full-f2507a5.md` §1, under *"One thing this FULL is explicitly not"*:
*"This review is C1.6's FULL. It does not discharge that read, and nothing here may be cited
as having done so."* `v3-review-verify-293f657.md` says it twice — §1 (*"It is not the E10
read `supersession-2` owes — and that read is now owed on the amended text, because this
repair changed that file's bytes"*) and again in its §7 verdict.

**(3) The subject is the post-repair text — holds; its section attribution does not.**
`git diff f2507a5 293f657` on this path is two hunks: the **header status line** (line 3,
*"authored at the Phase C1.5 round"* → *"authored at Phase C1.6"*) and a passage **inside
§2**, in the S1 successor blockquote, where *"is no longer called directly"* became the
qualified *"is no longer the authoring path for a newly opened run — closed-run scripts under
`assurance/runs/` and the helper's own tests still call it directly."* **This file's §3
("Version boundary", lines 64–69) is byte-unchanged since `f2507a5`.** The heading of the
changed passage is `### S1 — §3 "Version boundary"`, which names *supersession 1's* §3, not
this file's; that is the likely source of the slip. Recorded so the next reader is not sent to
the wrong section — the dispatch is not instruction-layer and says so.

---

## 2. Read coverage (R4)

- *Read in full:* the whole subject blob; `CONSTRUCTION-CHECKLIST.md`; supersession 1 §3 and
  its header; the signed contract's §13 line; `assurance_state.py`;
  `assurance-work-state.schema.json`; `common.schema.json`'s three ref shapes; `check_triage`
  in `issues.py`; the relevant passages of `v3-review-full-f2507a5.md` and
  `v3-review-verify-293f657.md`; the triage issue and decision documents behind §1's
  witnessed grounds.
- *Ran myself, output pasted below:* blob/history resolution; the frozen-blob sweep over
  `ResearchSystem/contract/`; a scripted digest audit of all eight committed `state.json`
  files; a scripted before/after recomputation of every `user-decision-triage-*` digest at
  `cf51534^`, `cf51534` and `HEAD`; call-site enumeration for `pointer_to` / `pointer_for` /
  bare `pointer`; a `digest_sha256` read-site sweep across the whole `document_harness`
  package; schema shape extraction for `pointerRef` / `digestRef` / `frozenFileRef` and every
  declaration of `instruction_ref` and `instruction_audit_ref`.
- *Not run, and not owed:* no test suites and no mutation probes. The subject adds no code,
  no guard and no executable byte; E4/E5/R8 are vacuous against a prose subject and their
  absence is not an omission. Where I needed to know whether a claim about the code holds, I
  read and exercised the code directly rather than inferring it from a suite result.
- *`UNVERIFIABLE` (R4, R7):* the *"user's 2026-07-29 adjudication narrowing state-pointer
  digests"* that the header cites as its authorization. It is chat-only; I see the execution
  side's records of it (`HARNESS-LEDGER.md`, `harness-digest-narrowing.plan.md`, commit
  bodies) and take those at face value without treating them as verified. Also unverifiable
  by construction: §3's forward statement that *"newly opened runs author pointers under the
  successor text"* — no run has opened since, and §4 discloses that four of the five protected
  fields have no shipped write path to exercise.

---

## 3. What verified clean

Listed because a read that reports only defects misrepresents the text. Each was re-derived,
not accepted.

| Claim in the subject | Verified how |
|---|---|
| Signed contract and supersession 1 stay **byte-identical** | `git ls-tree -r HEAD ResearchSystem/contract/` → `b2dbdf75…` and `68031fa2…`, the two blobs E2 names |
| The §13 quote, *"Signed contracts are never amended in place; corrections create a versioned successor"* | verbatim at the signed contract's line 243 (also quoted at its line 20) |
| Supersession 1 was written under that same rule | its own header carries the identical quotation |
| S1's **"Signed text"** blockquote | byte-faithful to supersession 1 §3's final bullet, modulo list-marker → blockquote |
| …and that text really is *signed* | supersession 1's in-file header still reads *"UNSIGNED until the wave-2 gate"*, but the gate closed: `ac1b383` (`V3-W2-SIGN-OFF-CLOSEOUT-v1`) records the user's 2026-07-24 sign-off of carrier blob `68031fa2`, kept in `W2-record.md` §7 and never in the carrier's bytes — the same convention this file's §5 prescribes for itself |
| *"exactly one statement supersession and nothing else"* | one `### S` heading in the file |
| `DIGEST_PROTECTED_FIELDS` holds exactly the five named fields | `assurance_state.py:81–89`, read back member by member |
| *"`pointerRef` requires only `path`, so this needs no schema change"* | `common.schema.json` → `pointerRef` required `['path']`; **all 13** state pointer fields in `assurance-work-state.schema.json` are `pointerRef`. (`assurance.schema.json` does declare six same-named fields as `digestRef`, but that file is the AssuranceCandidate/Summary, not the state — it does not govern this write) |
| `pointer_for` applies the field policy and delegates to `pointer_to` | `assurance_state.py:122–138` |
| The §2 qualification about `pointer_to` is **exhaustive** | `git grep "pointer_to("` → six run-script sites, all under `assurance/runs/p3-corr/` (a closed run), plus three test sites, all in the `PointerHelper` class. No site outside those two categories; `templates/run-v2/` has none |
| *"a wrong digest on any field remains `POINTER-STALE`"* | `resume` (`assurance_state.py:271–300`) reads `digest_sha256` **before** any protection test: present-and-mismatched → `POINTER-STALE` for every field alike. Protection only gates the *absent*-digest branch → `POINTER-UNVERIFIED` |
| *"only `review_ref` is authored by `templates/run-v2/`"* | the template's five `pointer_for` sites are `run_bind_v2.py:62` (`review_ref`, protected) and `run_evidence_v2.py:212/214/216/218` (`fulfillment_ref` / `manifest_ref` / `check_results_ref` / `coverage_ref`, all unprotected) |
| *"`pointer(path, digest)` … is used directly by hand-written run scripts"* | 30 bare `pointer(` call sites across `runs/w1-r1`, `runs/p3-corr` and all six shadow runs, several writing digests onto unprotected fields — so §4's disclosure that the narrowing's coverage is partial is accurate and understated, not glossed |
| *"thirteen state pointers carried digests"* | `runs/p3-corr/control/state.json` — 13 pointer-shaped refs, 13 carrying a digest |
| *"four pointer-ref families carried digests no code in the v3 package ever read back"* | exactly four `pointerRef` uses exist outside the state schema — profile `evidence_ref`, CheckResult `evidence_ref`, `executor_summary_ref`, `harness_issue_ref` — and a `digest_sha256` read-site sweep across the whole `document_harness` package hits none of them. `check_triage` confirms it directly: it tests phase, route, target-path presence, `work_id` and schema, and the string `digest` does not occur in its body |
| *"`cf51534` moved evidence paths"* | it rewrote `evidence_refs[].path` from `ResearchSystem/generated/document-assurance/runs/…` to `ResearchSystem/assurance/runs/…` inside nine issue documents, leaving each ref's own `digest_sha256` untouched |

---

## 4. Findings

### M-1 (must-fix) — §4 names `instruction_ref` as a `digestRef`; it is a `frozenFileRef`, and nothing requires or checks a digest on it

**Location:** lines 75–78, the second bullet of *"§4. What this supersession does not touch"*:

> **The `digestRef` side is untouched.** `instruction_ref`, the plan's `work_spec_ref`
> binding, and the review/summary/profile digest comparisons continue to require and check a
> digest; those refs require `[path, digest_sha256]` by schema and are outside this statement
> entirely.

**Ground truth.** Every schema that declares `instruction_ref` declares it `frozenFileRef`:

```
document-work-spec.schema.json:20-21          "instruction_ref": { "$ref": …/frozenFileRef }
document-work-spec.v2.schema.json:25-26       "instruction_ref": { "$ref": …/frozenFileRef }
instruction-coverage-audit.schema.json:24-25  "instruction_ref": { "$ref": …/frozenFileRef }
review.schema.json:140-141                    "instruction_ref": { "$ref": …/frozenFileRef }

common.schema.json  frozenFileRef  required: ['path', 'revision']   (digest_sha256 OPTIONAL)
                    digestRef      required: ['path', 'digest_sha256']
```

So all three predicates in that sentence are false of `instruction_ref`: it is not on the
`digestRef` side, it does not *"require … a digest"* (`digest_sha256` is optional on
`frozenFileRef`; `revision` is what is required), and no code *"checks a digest"* on it —
`instruction.py` compares the WorkSpec's and the audit's `instruction_ref` field by field over
`("path", "revision")`, never over a digest. Committed instances confirm the shape:
`runs/p3-corr/control/instruction-audit.json` carries
`"instruction_ref":{"path":…,"revision":"cb6bf7cb…"}` and no digest.

**The other items in the same sentence check out**, which is why this reads as one wrong name
rather than a wrong bullet: the plan's `work_spec_ref` is `digestRef`
(`resolved-assurance-plan.schema.json:19-20`) and is read back at `review_subject.py:308`; the
review / summary / profile comparisons are real (`review.py:446`, `review.py:494`,
`summary.py:292`, `assurance_profiles.py:131`).

**Minimum fix.** Replace `instruction_ref` with the START decision's
`target.instruction_audit_ref`, which satisfies every predicate as written — `digestRef`, and
`required` on `startTarget` (`user-decision.schema.json:109–112`), checked by digest at
`instruction.py:160–172`. It must be named as the **decision's** ref, because the *state's*
`instruction_audit_ref` is a `pointerRef` that this very supersession stops digesting; an
unqualified swap would trade one wrong statement for an ambiguous one. Dropping the name
entirely also fixes it.

**Why must-fix rather than banked under R9.** R9 asks me to name the downstream decision that
goes wrong. The adjudication this file records is `CORE_CANDIDATE` — more rounds are expected
— and the triage decision authorizing it scopes those rounds explicitly **by ref class**:
*"ceasing to write digests into pointerRef-shaped refs needs no schema change; documents whose
refs are digestRef cannot omit the field without editing frozen N0 bytes, which is a user
decision against E2 and not the round's; where a binding is load-bearing the replacement is
commit binding, and frozenFileRef (path plus revision) is already that shape."* §4 is the
contract-level statement of that inventory. A successor round taking it at face value places
`instruction_ref` in the class that needs a user decision against E2, when it is in fact
already in the third class — the commit-bound `frozenFileRef` the same decision names as *the
replacement*. The mis-statement therefore lands on the one distinction the whole adjudication
turns on, and points the wrong way: it makes the strongest example of the intended end-state
look like an obstacle to it. The accurate fact is not recoverable from adjacent text, which
asserts the wrong class positively.

Stated plainly: this changes **no check outcome today** and no code path — no code reads this
sentence. The cost is a mis-stated boundary in the one document whose stated job in §4 is to
state the boundary.

### L-1 (low) — the `cf51534` blast radius is eight ISSUE_TRIAGE decisions, not five

**Location:** line 33, in §1's witnessed grounds — *"`cf51534` … invalidated the digests of
five committed ISSUE_TRIAGE decisions while the whole test suite stayed green."*

**Measured.** Recomputing every `user-decision-triage-*.json`'s
`target.harness_issue_ref.digest_sha256` against the bytes of the issue document it names, at
three revisions:

```
cf51534^   8 triage decisions   8 not matching (target path unresolvable at that revision)
cf51534    8 triage decisions   8 STALE
HEAD      10 triage decisions   8 STALE, 2 MATCH
```

`cf51534` rewrote paths inside **nine** issue documents — six under `runs/p3-corr/issues/`
and three under `runs/w1-r1/issues/` — and the eight decisions holding digests over them all
went stale together and are stale today. The source the sentence compresses,
`issue-p3-corr-digest-binds-nothing-against-the-only-writer`, says *"all five ISSUE_TRIAGE
decisions"* and is scoped to one run (`"run_id":"p3-corr"`), where five is exact; the contract
sentence dropped the run scope while keeping the run-scoped number.

**Fix:** either `five` → `eight`, or restore the scope (*"p3-corr's five"*). **Wording-level
under R9** — no actor's action changes, and the direction is an *understatement* of the
evidence supporting this file's own thesis, so it cannot mislead toward over-claiming. Rides
the next batch touching this layer; it spawns no round and no read.

---

## 5. Observations (R5 — reported, not concluded)

**O-1 — `POINTER-STALE` is written bare where the emitted codes are qualified.** The code
family is `V3-STATE-POINTER-STALE` (`assurance_state.py:296`) and `V3-SUBJECT-POINTER-STALE`
(`review_subject.py:241`). The bare form is established house shorthand, not this file's
invention — it appears the same way in `harness-digest-narrowing.plan.md:86`, in
`templates/run-v2/run_evidence_v2.py:190`, and in a test docstring at
`test_spec_plan_state.py:858`. Recorded so a future reader greping for the literal token knows
why it resolves to two codes; not a finding.

**O-2 — the E2 shape recurs on exactly this file, and the recurrence is now three rounds
old.** E2's compressed phrase freezes *"existing files under `ResearchSystem/contract/`"*.
`supersession-2` is a file under that path, and `293f657` — the commit that produced this
subject — modified it. The act is in boundary: the rule of record at `7011916` freezes
**signed** bytes, and this file is UNSIGNED by its own §5 and by `ac1b383`'s convention. The
VERIFY recorded the same thing as its V-b, and `HARNESS-LEDGER.md:61` records it again. I add
only that this read's subject is itself the artifact of that edit, so the question is no longer
hypothetical: the next round told by a review to correct its own unsigned successor will read
E2 literally and face the same choice. Whether E2 should carry a clause, and which file should
carry it, is the user's question, not mine (R5).

**O-3 — §4's honesty about its own coverage is the strongest thing in the file, and it
survives measurement.** The last two bullets disclose that `pointer(path, digest)` still lets
hand-authored scripts write digests on unprotected fields, and that four of the five protected
fields have no shipped write path. Both check out independently, and the second is stricter
than it needed to be — the template's four *unprotected* `pointer_for` sites are the only ones
a run would exercise. A contract bullet that volunteers *"a contract implying uniform coverage
would be the same kind of defect this file corrects"* is doing the thing E3 asks for, on a
surface no command was going to check.

**O-4 — one file, two conventions for its own signature status, and both are right.**
Supersession 1's header still reads *"UNSIGNED until the wave-2 gate"* although it was signed
at that gate on 2026-07-24; the signature lives in `W2-record.md` §7 because the carrier's own
§5 forbids putting it in the bytes. Supersession 2 §5 repeats that rule for itself. The
consequence is that **neither carrier's header can ever be trusted for its own current
status** — the round record is the only place that answers it. That is a deliberate
consequence of keeping the signed object byte-identical to the reviewed one, not a defect;
recorded because this read had to go to `ac1b383` to learn that the text S1 calls *"Signed
text"* is in fact signed, and the next reader will have to do the same.

---

*Record written by the independent review session in the worktree (R6); the execution side
commits it, title `V3-REVIEW-RECORD-SUPERSESSION-2-READ-6e30c07-v1`. Every figure above was
produced by a command run against the worktree at `7ae4a76` with the subject blob re-confirmed
as `6e30c07f42268c9e7ad28dac2b6ed07cc6324d35`; reproduce them there. This read spends no
budget and carries no verdict.*
