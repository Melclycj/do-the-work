# FULL review — `1c18e4a..38038ec` (round `PROMISE-PATH-ENGINE`, batch `PROMISE-PATH`)

**Verdict: `CHANGES_REQUIRED`** — one blocker (`B-1`), three lows, four observations.

The blocker sits inside the round's headline item and is cheap to close: `run_bind_v2.py`'s new
`R10` decision point reports a state transition it does not take, and leaves the run's stored
instruction contradicting the one the same run printed — in the exact sequence the decision
point exists to create. Everything else in the range holds. Five of the six plan items are
implemented, their guards were independently mutation-proven here, the new schema binds the cap
it claims to, no announced path was written, and the battery is green at 932 / 0.

> Subject received as a range and nothing else (`R2`). Round, budget, authorization, obligations
> and every figure below were re-derived from the repository; no reported figure was accepted
> without re-running the command that produces it, and where a claim is reproduced, the
> reproduction is what is stated.
>
> Written by the reviewer and **not committed by it** (`R6`: the orchestrator commits the
> record, and that commit is also what deletes `.harness/review-pending.json` — the marker is
> deliberately left in place). That split follows the user's ruling (c) of 2026-09-02, which
> downgraded the `R6`-versus-`REVIEW.md` conflict to the banked rider `record-commit-owner`.

## 1. Subject, re-derived

Seven non-merge commits. Base `1c18e4af8a3ba82ae87e16aee40d38f2f967ad8f`, tip
`38038ecbc54bc7814ea090bedd4fad9a2456d436`. Oldest first:

| # | sha | title | kind, from its own body |
|---|-----|-------|-------------------------|
| 1 | `09ed9ed` | `V3-PROMISE-PATH-ENGINE-VALIDATE-REVIEW-RESULTS-v1` | candidate — item 7 |
| 2 | `387edc2` | `V3-PROMISE-PATH-ENGINE-R10-LOWS-DECISION-POINT-v1` | candidate — item 3 |
| 3 | `dcde02a` | `V3-PROMISE-PATH-ENGINE-BIND-DECLARATIONS-SCHEMA-v1` | candidate — item 6 |
| 4 | `45b2737` | `V3-PROMISE-PATH-ENGINE-VERIFY-DECLARED-DIGESTS-v1` | candidate — item 5 |
| 5 | `aff6a85` | `V3-PROMISE-PATH-ENGINE-EVIDENCE-COMMIT-MESSAGE-v1` | candidate — item 4 |
| 6 | `887c576` | `V3-PROMISE-PATH-ENGINE-DISPOSITION-REACHABILITY-SUITE-v1` | candidate — the spine |
| 7 | `38038ec` | `V3-PROMISE-PATH-ENGINE-E10-AMENDMENT-README-ROW-v1` | `E10` amendment |

```
$ git diff --numstat 1c18e4a..38038ec | awk '{a+=$1;d+=$2;n++} END {print n" files, +"a" -"d}'
18 files, +2578 -145
```

**Paths classified by hand** (`R2`), from `git diff --name-status`:

- **Engine — `tooling/rsclib/document_harness/`** (3, all `M`): `flow.py` · `review.py` ·
  `review_result_v2.py`.
- **Run templates — `assurance/templates/run-v2/`** (2, both `M`): `run_bind_v2.py` ·
  `run_evidence_v2.py`.
- **Schema pack** (1, `A`): `schema/document-assurance-v3/bind-declarations.schema.json`.
- **Instruction layer, an `E10` member** (1, `M`): `document-harness/README.md` — one added
  enumeration entry on the *Review + disposition schemas (V3-N2)* row; `+1 −1`, one line.
- **Tests — `tooling/tests/document_harness_review/`** (11: 3 `A`, 8 `M`):
  `test_disposition_reachability.py` (A, 779 lines) · `test_run_v2_template_commit_message.py`
  (A) · `test_run_v2_template_declarations.py` (A) · `test_fix_round_locks.py` ·
  `test_flow_repair_disposition.py` · `test_golden_review_views.py` ·
  `test_run_v2_template_bind.py` · `test_run_v2_template_check_order.py` ·
  `test_run_v2_template_fulfillment.py` · `test_run_v2_template_repair.py` ·
  `test_run_v2_template_repo_root.py`.

**Freeze window re-derived rather than assumed** (`REVIEW.md`, *Where the result lives*, which
says the hook is advisory and per-machine): `.harness/review-pending.json` names exactly this
range and `git rev-parse HEAD` on `dev` is `38038ec…`, so branch tip equals dispatched tip and
no commit landed after dispatch. The worktree carried the same two untracked entries at the
start and the end of this review (`.goals/`,
`document-harness/journal/promise-path-engine-2026-09-02.md`) and nothing else; every mutation
probe below was restored from a sha256-checked scratchpad copy and re-verified with
`sha256sum -c`.

## 2. Round, budget, authorization, obligations — re-derived

**Which round.** `CONSTRUCTION-LEDGER.md`'s backlog names batch `PROMISE-PATH` as the queue
head, established by the user's ruling 2 of 2026-09-01, with round 1 = `ENGINE` carrying items
3–7. The plan is `document-harness/plans/promise-path.plan.md`; its *Rounds and budget* section
assigns round 1 items 3, 4, 5, 6, 7 plus the `E4`-inverse suite, and routes items 1 and 2 to
round 2 `PROMISE-PATH-VOCAB`. Every commit title in the range names `PROMISE-PATH-ENGINE`.

**Budget (`E9`).** One FULL, at most one user-approved fix, one targeted VERIFY. `E9`'s test —
*has a valid independent FULL already occurred?* — measured rather than assumed:

```
$ ls migration/document-work-assurance-v3/ | grep -E '38038ec|1c18e4a|09ed9ed|387edc2|dcde02a|45b2737|aff6a85|887c576|51bd4f6|f5d9741'
v3-cold-read-51bd4f6.md
```

The round's only prior review-side record is its opening cold read. **No FULL has occurred
before this one**, so the seven commits are the round's single candidate leg and consumed
nothing. This record consumes the FULL; one user-approved fix and one targeted VERIFY remain.

**Opening obligations.** The plan makes the opening `E10` cold read non-waivable (the batch is
design) and states that the read also pays `RULES.md`'s free-channel debt from `3060a23`. Both
are recorded as done: `b2f2c3b` committed `v3-cold-read-51bd4f6.md` unchanged, and `1c18e4a`
dispositioned its four findings. `HARNESS-DECISIONS.md` `§live` re-enumerated here rather than
inherited from the plan — **eleven** entries at this tip, in file order: `HD-69` · `HD-66` ·
`HD-65` · `HD-62` · `HD-59` · `HD-41` · `HD-36` · `HD-35` · `HD-34` · `HD-23` · `HD-9`. Same
eleven the plan names.

**Authorization I can see, and the ceiling (`R7`).** The six batch rulings and the two-round
split are in the plan under *Rulings*, dated 2026-09-01 with the user's own words quoted. The
round-1 boundary widening that let `38038ec` write an `E10` member is recorded in that commit's
body ("on the user's ruling of 2026-09-02: option (a)") and, more fully, in the untracked round
journal. I cannot see the conversation behind either; both are hints under `R7` and I state the
ceiling rather than treat them as verified. The ledger's standing entry of 2026-08-16 ④ says
construction-round rulings live in commit bodies by design, so the carrier is the sanctioned one.

**Change boundary.** The plan's **In** list enumerates `flow.py`, `review_result_v2.py`,
`assurance/templates/run-v2/` (both templates), `schema/document-assurance-v3/` additions plus
three named existing schema files, `tooling/tests/`, and — under *Rulings* 2 — `RULES.md`,
`REVIEW.md:129-135` and contract `:118`. Measured against the range: the three round-2 rule and
contract surfaces were **not** touched, correctly; `document-harness/README.md` was touched under
a disclosed widening; and `tooling/rsclib/document_harness/review.py` was touched, is not on the
In list, and is named as an escape nowhere — `L-2`.

**`E2`.** No announced path was written. Re-run rather than read out of a commit body:

```
$ python tooling/announced_path_disclosure.py --before 1c18e4af8a3... --after 38038ecbc5...
announced-path disclosure: range 1c18e4af8a3ba82ae87e16aee40d38f2f967ad8f..38038ecbc54bc7814ea090bedd4fad9a2456d436
  floor 1d4d9aa1f6b1daca3fbf1a7765985abaec350b18; 7 non-merge commit(s) judged
  every announced path changed in this range is named by the commit that changed it
(exit 0)
```

The new pack file is correctly **not** announced: `E2` re-baselines rather than auto-enrolling,
and the alarm's hand-written `ANNOUNCED` tuple carries the fifteen 2026-08-03 names — still
including the retired `review.schema.json` — and not `bind-declarations.schema.json`.

**`E8`.** Every title is one dense line naming the round in the `V3-<ROUND>-…-v1` form; every
body opens `Kind: …` (six *candidate*, one *E10 amendment*); no trailers. Bodies run to several
paragraphs, which the ledger's standing 2026-08-07 entry (`HI-REDEEM-5` `L-4`) admits: `E8` buys
density and the absence of trailers, not a literal single paragraph.

## 3. The implementation — what I checked, and what held

`R3`: implementation first. I read the diffs of all seven non-test source, schema and
instruction files in full, `test_disposition_reachability.py` in full, and the other test
modules by class and test-name index with targeted full reads of the classes each item turns on.
Then I ran the battery, re-ran three of the four pasted class scans, exercised the new schema
directly, and mutation-probed five guards myself.

**The battery, re-run rather than reported.**

```
$ python -m pytest tooling/tests -q
932 passed in 640.68s (0:10:40)
```

That reproduces `38038ec`'s claim of 932 passed / 0 failed. My wall clock is longer because
probe runs were competing for the host; the count is the figure. The three intermediate commits
that landed carrying `1 failed` each disclosed it as the same `test_readme_enumeration` failure
and did not gloss it, and `38038ec` closed it.

**Item 7 — validate a ReviewResult before deciding from it (`09ed9ed`). Holds.**
`review_result_v2.validate_result` is one entry keyed on `result_schema_kind`, and all three
`flow.py` consumers now pass through it: `reviewed_candidate_ref` (`flow.py:340`, via
`require(SpecGap)`), `check_repair_decision` (`:375-377`, the review's report returned on its
own rather than merged) and `check_verify_outcome` (`:616-618`). Fail-closed verified from the
plumbing rather than the docstring: `review_subject.validate_w2` raises `SpecGap` for an
unregistered kind and `result_schema_kind` raises for any declared version other than `"2"`, so
a version-1 root shape and an unknown version both **stop** rather than report. The `HD-41`
class scan pasted in the body reproduces here with only line numbers shifted, and its scope
statement is honest — `summary.check_assurance_candidate` is named as the same class in another
module and reported rather than silently fixed (`O-2`). The declared consequence that the
enforcement of "the review names no exact candidate commit" moved from
`V3-FLOW-REPAIR-BINDING-UNVERIFIED` to the schema is correct, and the branch it leaves standing
is `O-3`.

**Item 3 — the `R10` lows decision point (`387edc2`).** The mechanism is right; the failure is
in its follow-through (`B-1`). What holds: the trigger is the reviewer's own non-blocking
findings, read off the operative review at `run_bind_v2.py:392-396`, which is *after*
`check_review_result_v2` has validated it at `:319-325` — so the subscripts are safe, and a
`REVIEWED_NO_BLOCKER` carrying a blocking finding cannot reach the branch because verdict /
finding coherence stops it a gate earlier (`review_result_v2.py:275`). A clean FULL with no
findings walks straight through. The `NO_REPAIR` is **read, never authored**, and is gated by
the same `flow.check_repair_decision` that gates the APPLY path — and that gate really does bind
a decline, because its `work_id` / `run_id` and reviewed-candidate checks precede the
`NO_REPAIR` early return. No `repair_decision_ref` is written, which is correct rather than
merely asserted: `flow.check_state_pointers:266-274` reports one at repair round 0 as preceding
the repair it authorizes. The `emit_reviewed` no-op is right — `REVIEWED -> REVIEWED` is not in
`_SUCCESSORS` and `assurance_state.advance` does not check legality. The user-decision schema's
REPAIR branch enumerates exactly `APPLY_ACCEPTED_FINDINGS` and `NO_REPAIR`, so the
`!= "NO_REPAIR"` branch cannot capture a third value.

**Item 5 — declared digests recomputed, never copied (`45b2737`). Holds.**
`declared_ref_faults` runs after schema validation, so `scan.get("result_ref")` and
`entry["source_ref"]` are both safe (the schema makes `source_ref` required on a disclosure and
`result_ref` required only when `included: true`). An absent file is its own fault; faults are
collected and reported in one pass; the bind refuses rather than re-deriving. The `E7` class
scan pasted in the body reproduces exactly here — `governanceScanState -> ['/result_ref']`,
`disclosure -> ['/source_ref']`, no third `digestRef` reachable from a BindDeclarations
document — so the claim that the class has exactly two members is decidable from the schema and
is true.

**Item 6 — `bind-declarations.schema.json` (`dcde02a`). Holds**, and I exercised the schema
directly rather than trusting the tests that cover it:

```
over-500 disclosure ok?              False   ('…' is too long)
empty disclosures ok?                True
included:true without result_ref ok? False   ('result_ref' is a required property)
additionalProperties refused?        True
disclosure of exactly 500 ok?        True
```

The cap here is the candidate's own cap reached by `$ref`, not a second copy that can drift, and
it binds. The registration argument checks out too: `pack_digests()` (`__init__.py:241-244`)
hashes exactly `SCHEMA_FILES`, which this range does not touch, so the pack digest is unmoved —
`review.N2_SCHEMA_FILES` was the right shelf and the comment at the registration says why. The
evidence-step half is placed before the expensive checks and before the irreversible commit, and
refuses a malformed file while deliberately tolerating an absent one, with the reason stated:
`governance_scan.result_ref` names a CheckResult that step has not written yet.

**Item 4 — the evidence commit message (`aff6a85`). Holds.** Exactly one of
`--commit-message` / `--commit-message-file`, refused **first**, before the run directory is
resolved, with exit 1 and a sentence rather than argparse's `SystemExit(2)` and a usage block.
Only the structure is judged — title, blank line, body — and the refusal to judge *content* is
itself pinned by a test, so a later round cannot add a content rule and call it a bug fix.
`commit_control_plane` stages the named control root and never `-A`, and the verbatim property
is asserted against a real repository by reading the message back out of `git log`. One
approximation in the word *verbatim*, measured, is `O-1`.

**The spine — `test_disposition_reachability.py` (`887c576`). Sound.** The enumeration side is
read from the committed schema pack at run time (`user-decision.schema.json`'s FINAL branch,
`review.v2.schema.json`'s verdict enum and its VERIFY narrowing) and the table side is literals,
so the file cannot assert that the code equals itself. A reacher *returns* the disposition it
produced and the test compares that against the row's own key, which is what makes the table the
guard rather than a comment. The `no-path` branch, which has no real row, is exercised against
synthetic tables with a negative control for each must-fire case, and
`test_the_enumeration_is_not_vacuous` pins the family sizes so neither enumeration guard can
pass over nothing. Thirteen rows, fifteen tests, 1.01s. The module's own scoping is careful —
property 1 says "every disposition the **schemas enumerate**" — and what that scope leaves
uncovered, together with a claim in the commit body that is not so careful, is `L-1`.

**My own mutation probes (`R8`, `E4`).** Five, each neutering the **engine** and never the test,
each restored from a sha256-checked scratchpad copy. The three files' digests at `HEAD` —
`run_bind_v2.py` `dcd3a3efedb30d5ee220c980d54a20e3207636b14be4346173e234464ea889d2`,
`run_evidence_v2.py` `b3d230ef78e1a610dcedc7c3cbdf561f29f5fc4b5f2249b9d35671f56b151a6a`,
`flow.py` `32298fd1c05e643be3acd25ad0c2df783322d5237b760ced90d8b3f58312f98b` — are exactly the
digests three of the commit bodies name as their own probes' restore targets, which corroborates
those probe records independently of my believing them.

| probe | mutation | result |
|---|---|---|
| item 3 | the `R10` stop never fires | **7 red** across `TheLowsDecisionIsPutBeforeTheCandidateIsBound` and the reachability row |
| item 5 | `declared_ref_faults` → `return []` | **4 red**, `TheDeclaredDigestsAreRecomputedNeverCopied` entire |
| item 7 (a) | the `check_repair_decision` and accessor validations deleted | **5 red** across two modules |
| item 7 (b) | the `check_verify_outcome` validation deleted | **2 red** |
| item 6 | the bind falls back to the two-key presence test it used to run | **1 red** |
| item 4 | `commit_message_fault` → `return None` | **5 red** |

Every guard this round adds has now been seen to fail by someone other than its author. `R4`'s
ceiling stands: mutation proves the tests have binding force, never that their force is
sufficient.

## 4. Blocker

### `B-1` — the `R10` decision point reports a state write it does not make, and leaves the stored instruction contradicting the printed one

**Location.** `assurance/templates/run-v2/run_bind_v2.py`. The two `R10` stopping branches —
`:413` (no decision on disk) and `:445` (an `APPLY_ACCEPTED_FINDINGS` decision) — and the
round-0 blocked branch at `:375`. All three call `emit_reviewed(...)`, discard its return value,
and then print `emitted … -> state REVIEWED` unconditionally. The candidate act at `:539-547` is
the only one of the four call sites that honours the return.

**What it violates.** Two properties this round itself establishes.

1. `emit_reviewed`'s own docstring (`:205-215`): the return value "is not decoration… The return
   value is what gives the no-op a consequence a test can hold: the caller says on stdout which
   of the two passes this is, so deleting the no-op changes the output." Three of four callers
   do not say it, so at those sites deleting the no-op changes nothing — the shape `E4` refuses.
   The commit's own probe *the already-REVIEWED no-op deleted → 1 red* binds only through the
   candidate path.
2. The step's stored-instruction discipline, written into this very branch at `:407-410` and
   carrying rider `sg-print`'s lesson: the instruction is **printed and stored as one string**,
   because two rewrites of one fact diverge silently. In the second pass the printed and the
   stored instruction are different sentences, and the one that survives on disk is the stale one.

**Reproduced**, at this tip, against the round's own fixtures and the real template:

```
PASS 1  (no decision on disk, --emit)
  next action            : user REPAIR decision on the non-blocking findings (f-style):
                           APPLY_ACCEPTED_FINDINGS spends this round's one repair leg on them
                           and NO_REPAIR banks them; the AssuranceCandidate is bound only
                           after that decision is on disk
  emitted                : review-full.json -> state REVIEWED (…)
  state.json  status     : REVIEWED
  state.json  next_action: "user REPAIR decision on the non-blocking findings (f-style): …"

  ... the user now records APPLY_ACCEPTED_FINDINGS, which is exactly what PASS 1 asked for ...

PASS 2  (that decision on disk, --emit)
  lows decision          : APPLY_ACCEPTED_FINDINGS — the leg is spent
  next action            : user chose to spend the repair leg on the non-blocking findings;
                           the next act is run_repair.py, which gates the decision and
                           enters REPAIRING
  emitted                : review-full.json -> state REVIEWED (…)   <-- NOTHING was written
  state.json  status     : REVIEWED
  state.json  next_action: "user REPAIR decision on the non-blocking findings (f-style): …"
                                                                    <-- still PASS 1's sentence
```

The same probe on the blocked branch — a `CHANGES_REQUIRED` FULL with the bind run twice —
prints the same `emitted` line on the second pass with nothing written; there the two
`next_action` values happen to be identical, so only the false report survives. This is a class
of three sites, not one instance (`E7`).

**Why this is a blocker and not a low.** The sequence above is not operator misuse: it is the
sequence the decision point exists to produce. The first pass exists precisely to stop *before*
a decision is on disk, so a run that actually meets the decision point can only arrive at pass 2
with the state already `REVIEWED`. In that sequence item 3's feature never lands its instruction
on disk at all, and the step tells its operator it wrote a transition it did not write.
`state.json` is committed control-plane evidence that a later independent review reads, and a
controller stating a transition it did not take is V3-D5's "poor in claims" failing in the one
direction that matters. The round's own test asserts exactly the property that breaks —
`test_an_apply_decision_stops_too_and_names_the_repair_step` asserts
`saved["next_action"] == SPEND_ACTION` — but from a fixture that starts at `EVIDENCED`, i.e.
with the decision on disk before the first bind, which is the one ordering the decision point
cannot produce. The two-pass sequence is covered for `NO_REPAIR`
(`test_the_second_pass_resumes_from_the_reviewed_state_the_first_wrote`) and not for `APPLY`.

**Minimum fix.** At the three call sites, honour `emit_reviewed`'s return exactly as the
candidate act already does, so the `emitted` line is printed only when a transition was written;
and on the already-`REVIEWED` path make the branch's own `next_action` reach disk — a field
update saved without a status transition, since `REVIEWED -> REVIEWED` is not a legal successor —
so the stored instruction is the printed one. Plus one test that drives the real sequence
(pass 1 → `APPLY` → pass 2) and asserts both halves. `E7`: the fix belongs at all three sites,
not only the one reproduced.

## 5. Lows

Reported at their own weight. None is worth the single repair on its own; whether any rides
`B-1`'s fix leg is the orchestrator's `R10` call at closeout, and none of them touches a surface
`B-1`'s fix touches, so folding one in is a boundary decision rather than a free ride.

### `L-1` — the spine watches only the schema-enumerated families, and the batch's own open promise is a route it will never notice

`test_disposition_reachability.py`'s property 1 is scoped, correctly, to "every disposition the
schemas **enumerate**" — `enumerated()` reads three families and no more. The table's other
kind of row, which its own `Row` docstring calls "a bare name for the dispositions the rules name
in prose", has **no** enumeration guard: `STOPPED_REPLAN`, both `repair-leg-after-…` rows and
`ACCEPT_WITH_LIMITATIONS-from-residual-uncertainty` are covered only by whoever remembered to
hand-write them.

That matters concretely for this batch. `document-harness/EXECUTION.md:98-100` names, as one of
the two honest dispositions after a blocker still stands at VERIFY, "a user
`ACCEPT_WITH_LIMITATIONS` that names what is still open"; contract v4 `:105`/`:122` names it
too. That is item 1, ruled shape (a) and **not built** — round 2's work. It is a prose-named
route, so it adds no enum value; the table carries no row for it, and nothing in the suite will
turn red when round 2 builds it and forgets one. Item 2 is safe by contrast — growing the VERIFY
verdict enum makes `missing_rows` **and** `test_the_enumeration_is_not_vacuous` red — so the gap
is specifically the prose class.

Alongside it, one sentence overstates. `887c576`'s body says: "No row is `no-path` today — every
disposition the rules name is now reachable". The first clause is true of the table; the second
is false of the repository, and item 1 is the counter-example the batch itself is named for.
Under `HD-59` a committed conclusion is corrected forward, never in place.

**The downstream decision that goes wrong if this stays** (`R9`): a reader deciding what round 2
still owes the suite reads that clause and concludes nothing. **Minimum fix:** correct the claim
forward, and state in the module what the enumeration guard does *not* watch — the prose-named
rows — naming item 1's route as the row round 2 owes. Adding a `no-path` row now is not the
round-1 fix: a `no-path` row obliges its rule site to carry the absence in its own text, which
is an instruction-layer write and design.

### `L-2` — one file was written outside the plan's declared change boundary, and no commit names the write as an escape

`tooling/rsclib/document_harness/review.py` gains eight lines in `dcde02a` — the
`bind_declarations` entry in `N2_SCHEMA_FILES` and the comment explaining the shelf. The plan's
**In** list enumerates at file granularity, naming `flow.py` and, separately,
`review_result_v2.py` "(item 7's validation entry)"; `review.py` is not among them. `E8` requires
staying inside the round's declared change boundary and `E9` requires saying so when a boundary
is exceeded, "never silently". `dcde02a` discloses at length *what* it did to `review.py` and
*why that shelf and not the other*, but nowhere says the file is off the list — while the round's
other out-of-boundary write, `README.md`, is named as one and carries its ruling.

The write itself is right: a pack file nothing registers is inert, and `pack_digests()` would
have moved had it gone on the other shelf. **The downstream decision that goes wrong:** the
closeout's boundary accounting records this round as having stayed inside a boundary it did not
stay inside, and the next round inherits an In list that has grown by silent precedent.
**Minimum fix:** one sentence, in the fix commit's body or in the closeout, naming
`tooling/rsclib/document_harness/review.py` as written outside the plan's In list, and why.

### `L-3` — the round's durable resume carriers are stale and uncommitted at the dispatched tip

Two halves of one condition:

- `document-harness/plans/promise-path.plan.md` still shows Steps 3 and 4 unchecked, and its
  *Resume pointer* still reads "steps 1–2 done, next act = step 3, the executor dispatch" —
  while step 3's seven commits are the subject of this review. `CLAUDE.md` and the plan itself
  designate that pointer as where a cold session resumes, so a cold session reading it at this
  tip re-dispatches an executor whose work is already in the tree.
- `document-harness/journal/promise-path-engine-2026-09-02.md` is **untracked**
  (`git status --porcelain` → `??`). So `HD-69`'s requirement that the orchestrator record the
  executor session id in the round journal by hand is not in committed state at this tip, and
  the fuller account of the 2026-09-02 boundary ruling — that options (b) push-to-round-2 and
  (c) withdraw-the-schema were offered and not taken — lives only in the worktree. The operative
  facts survive in `38038ec`'s body, so nothing is lost; the carrier `HD-69` names is simply not
  yet a record.

This is a departure from the immediately preceding round, measured rather than felt: round
`CORE-ONLY-CODE` closed its executor leg with `70c82b4`
`V3-CORE-ONLY-CODE-CANDIDATE-CLOSE-v1`, a commit whose entire content is
`document-harness/plans/core-only.plan.md` (+21 −5), landed **before** its FULL was dispatched.
The window is real rather than theoretical, because `E9` allows the branch no commit but this
record between dispatch and its landing, so the pointer cannot be corrected until then.
**Minimum fix:** the closeout commit checks Steps 3–4, moves the resume pointer, and lands the
journal.

## 6. Observations — `R5`, for the user, not for me to conclude

### `O-1` — "used verbatim" is approximate, because `git commit -m` cleans the message

`run_evidence_v2.commit_control_plane`'s docstring says the message reaches git unedited, and
`aff6a85`'s body says it is used verbatim. Git's default cleanup for `-m` is `whitespace`:
leading and trailing empty lines stripped, trailing whitespace stripped, consecutive empty lines
collapsed. Measured against a throwaway repository at this tip:

```
supplied: 'title line\n\nbody paragraph one.\n\n\nbody paragraph two, after a doubled blank line.   \n'
stored  : 'title line\n\nbody paragraph one.\n\nbody paragraph two, after a doubled blank line.\n\n'
commit_message_fault(supplied) -> None
```

The practical exposure is small: `E8` asks for one dense paragraph, which survives cleanup
untouched, and the module's own fixture is such a message. So this is not a finding against the
implementation. What is worth knowing is that the asserted property holds for cleanup-stable
messages and that nothing refuses a message that will be altered. Whether to close it
(`--cleanup=verbatim`, or a fourth structure rule) or to record the ceiling in the docstring is a
design question and the user's.

### `O-2` — item 7's `E7` class was drawn at the module, and one live member sits outside it

`09ed9ed`'s scope statement names `summary.check_assurance_candidate` as "the same class in
another module and outside item 7's named files", reports it rather than fixing it, and observes
that at round 1 the round-0 FULL it also reads is not validated. That is honest, and the
narrowing is defensible — the plan named two `flow.py` sites, the scan found a third in the same
module, and all three are fixed. Recorded so the routing is the user's: the class "a function
that decides from a ReviewResult it never validated" has a known live member, and `E7` says the
class is what gets closed.

### `O-3` — a guard kept alive that can no longer fire for the only live result version

`flow.py:436-457`'s `V3-FLOW-REPAIR-BINDING-UNVERIFIED` on the reviewed-candidate binding is now
unreachable for a v2 result, because the review is validated first and `review.v2.schema.json`
requires `subject.candidate_ref` with a `commit` inside it. The commit declares this, annotates
the branch, and pins the issue code's one remaining reachable sibling (`run_id`) with a test of
its own. Nothing here is wrong. The shape is worth naming because `E4` cannot see this branch
fail, and the round that relaxes the schema is the round that would need it.

### `O-4` — the `NO_REPAIR` that now licenses the candidate binding is bound by nothing

After item 3, a `NO_REPAIR` on disk is what allows the bind to write the AssuranceCandidate and
advance `AWAITING_FINAL`. Nothing binds that document: `check_state_pointers` forbids a
`repair_decision_ref` at repair round 0, the candidate carries nothing about the banked lows by
deliberate choice (V3-D5), and no digest of the decision reaches either the state or the
candidate. So a later reader of an `AWAITING_FINAL` state cannot verify *which* decision unlocked
it — in a round whose item 5 exists because a digest nobody checks certifies nothing. Each half
of that choice is argued in `387edc2`'s body and each is individually right; the gap is what
falls between them. Whether it should be closed, and in what shape, is design — `R5` puts it to
the user rather than concluding it here.

## 7. Coverage and ceilings (`R4`)

- **Read in full:** the seven commit bodies; the diffs of `flow.py`, `review.py`,
  `review_result_v2.py`, `run_bind_v2.py`, `run_evidence_v2.py`,
  `bind-declarations.schema.json` and `document-harness/README.md`;
  `test_disposition_reachability.py`; `document-harness/RULES.md`;
  `document-harness/CONSTRUCTION-CHECKLIST.md`; `harness.json`;
  `document-harness/plans/promise-path.plan.md`; `CONSTRUCTION-LEDGER.md`'s header block and
  current pointer; the round journal.
- **Read in part:** `document-harness/REVIEW.md` (outline plus five sections);
  `HARNESS-DECISIONS.md` (`§live`'s entry list re-enumerated; individual entries not read
  end to end); the eight modified test modules (class and test-name index, with the classes each
  item turns on read in full); `assurance.schema.json`, `user-decision.schema.json` and
  `assurance-work-state.schema.json` (the `$defs` and branches this round depends on).
- **Not read:** `EXECUTION.md` beyond `:94-102`; `ORCHESTRATION.md`; contract v4; the two
  archives; `CONSTRUCTION-INDEX.md`.
- **Executed:** the full battery once; five mutation probes with digest-verified restores; the
  announced-path alarm; three of the four pasted class scans re-run; the new schema exercised
  directly at five points; `B-1`'s two-pass sequence and `O-1`'s cleanup behaviour driven
  against real fixtures and a real repository.
- **`UNVERIFIABLE`, stated rather than folded into supported:** that the executor ran as one cold
  `claude -p` session on `opus` per `HD-69`, and that the session id in the journal is that
  session's — a process claim, marked and not verified. That the 2026-09-02 boundary ruling was
  given as described — the `R7` ceiling stated in §2. That the `E4` probe *procedures* the commit
  bodies describe were carried out as written; what I can and do corroborate is that the files at
  `HEAD` carry exactly the digests those bodies name as their restore targets, and that the
  guards they claim to have proven do go red under my own independent mutations.
- **Platform ceiling:** everything above was measured on Windows with CPython 3.13. The CI
  matrix's Ubuntu legs were not exercised here.

## 8. What a VERIFY would cover

The accepted findings plus the whole repair diff, and the permanent boundaries however narrow
the round (`R3`). Concretely, if `B-1` is accepted: that the `emitted` line is printed only where
a transition was written, at all three sites and not only the reproduced one (`E7`); that the
stored `next_action` equals the printed one on the two-pass `APPLY` path; that the added test
drives the real two-pass sequence rather than a fixture that starts with the decision already on
disk; that the fix's own guard has been seen to fail (`E4`), with a negative control on the
one-pass path, which must keep reporting no resumed position; that nothing else in
`run_bind_v2.py` moved; that `E2` is still clean and no announced path was written; and that the
battery is green at a count re-measured immediately before the claim (`E3`).
