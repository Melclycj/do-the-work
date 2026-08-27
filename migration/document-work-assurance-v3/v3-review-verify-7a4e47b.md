# VERIFY — round `CORE-SET-CODE`, subject `fccadfb..7a4e47b`

**Verdict: `REVIEWED_NO_BLOCKER`** — the repair holds; 2 residual findings, neither in the repair's
substance, one of them in the repair commit's own evidence.

Independent session. Dispatched, prompted, scoped and reported through the orchestrator, not the
executor (`R1`); the prompt handed me the range and nothing else. Round, budget, authorization,
obligations and every figure below were re-derived from the repository (`R2`); no reported figure is
carried forward unchecked. Every number is followed by the command that produced it, run at the tip
unless a different revision is named.

---

## 1. What I read, and how far

`R4`, so the ceiling is visible rather than implied.

**Read end to end.** `migration/document-work-assurance-v3/v3-harness-review-contract.md` (6 lines,
which routed me to its successor) · `document-harness/CONSTRUCTION-CHECKLIST.md` (258 lines, both
sides) · `migration/document-work-assurance-v3/v3-review-full-1db5155.md` (347 lines, the FULL this
repair answers) · `HARNESS-DECISIONS.md` `§live` (lines 30–162: `HD-59` · `HD-44` · `HD-41` ·
`HD-36` · `HD-35` · `HD-34` · `HD-23` · `HD-9`) plus `HD-38`, `HD-37`, `HD-20`, `HD-21`, `HD-22`,
`HD-19`, `HD-1`–`HD-8`, and `HD-60` / `HD-61` in the archive · the fix commit body in full · the
complete diff of the range, all three paths, every hunk ·
`tooling/tests/document_harness_review/test_fix_round_locks.py` lines 228–400 at the tip ·
`document-harness/REVIEW.md`'s two round-3 hunks.

**Sampled.** `document-harness/plans/core-set.plan.md` — the status header, steps 11–14, and the
round-3 acceptances; items A–F and rounds 1–2 were not read. `CONSTRUCTION-LEDGER.md` — the
`CORE-SET` entry and the round-3 block only. `v3-cold-read-b737742.md` — its member/blob table rows
and its closing blob table, not its 451 lines. `tooling/rsclib/document_harness/review.py` — the
module docstring, the imports and the one `Issue` call site, not its 184 lines.
`schema/document-assurance-v3/review.schema.json` — the `package_ref` description at `:281` and the
sweep hits, not the file.

**Only probed.** No product run was built or driven. The v2 review flow end to end is untouched by
this leg and was not re-exercised; the FULL's ceiling on it stands unchanged.

**`UNVERIFIABLE` from committed state.** `E8`'s "stage explicit paths, never `add -A`" and "never
amend" — history does not record how the index was built. The user approval this leg claims for its
fix and its routing is likewise not independently visible; see §5.

**Not a re-certification.** Items G and H were the FULL's subject, not mine. Where the FULL
adjudicated a question, I verified that the repair implements the FULL's finding, not that the
finding was correctly decided (`R4`: a VERIFY is never a re-certification).

---

## 2. What this leg is, re-derived

The range is **one** commit on `main`: `7a4e47b`, title `V3-CORE-SET-CODE-FIX-v1`, body opening
`Kind: review fix.` Base `fccadfb` is the commit that landed the FULL record.

```
$ git diff --name-status fccadfb..7a4e47b
M	HARNESS-RIDERS.md
M	document-harness/journal/core-set-code-2026-08-27.md
M	tooling/tests/document_harness_review/test_fix_round_locks.py
```

Three paths, classified by hand: one rider bank, one round journal, one test file. The test-file
change is comment-only — every added line opens `    #: `.

**Budget.** `E9`'s own test, applied by me and not taken from the commit body: has a valid
independent FULL already occurred on this round? Yes — `v3-review-full-1db5155.md` landed unchanged
at `fccadfb`, and its §1 records it as dispatched, prompted, scoped and reported through the
orchestrator. So this is the fix leg, it consumes the round's one user-approved fix, and it obliges
the targeted VERIFY. **This record is that VERIFY.** The classification the body states is correct.
`E9`'s no-other-commits clause also holds: between the FULL record's commit and this one the branch
took nothing else, and between this one and now it has taken nothing at all
(`git log --oneline fccadfb..HEAD` → two commits, `git status` clean but for the pre-existing
untracked `.goals/`).

**Authorization.** Round 3 is OPEN per the plan's status header and step 11; steps 12–13 remain
unchecked, which is where this leg sits. The routing of the FULL's findings — fix `B-1` and `L-2`,
bank `L-1`, `L-3`, `O-1` — is `R10`'s explicit user decision, and the leg attributes it to a user
ruling of 2026-08-27. No such entry exists in `HARNESS-DECISIONS.md` (`grep 2026-08-27` over that
file returns nothing). That is the **ruled** carrier, not a gap: the ledger records the user's
2026-08-16 ruling ④ that a construction batch's rulings "继续只活在 commit 正文", with the cost
recorded. So the ruling lives where it was ruled to live, and `R7` applies to the rest — I state the
ceiling and move on: **the fact of user approval is `UNVERIFIABLE` from committed state**, being a
first-person claim by the work side.

No `E2` authorization exists or was needed: `HD-60` and `HD-61` are `retired` in the archive, and
enumeration of the range names nothing under `schema/document-assurance-v3/` and not
`contract/Document-Work-Assurance-Contract-v4.md`.

---

## 3. `B-1` — verified closed, and mutation-tested in both directions

The FULL's minimum fix was that the sentence change to state what holds. It does.
`test_fix_round_locks.py:256-267` now says the partition "reacts to a *module*, never to a *code*",
that `named_codes()` reads `N2_MODULES` alone, that "a coded vocabulary returning to a module listed
here is swept by nothing and stays green", and that the way back is to move the module into
`N2_MODULES`. The compensating coverage the FULL asked the comment to name — `N2ValidatorTests` in
`test_golden_review_views.py` for the `V3-SCHEMA-<KIND>` vocabulary the regex structurally cannot
see — is at `:273-276`, unchanged and pre-existing; the leg is right that it did not need writing.
The second arm the FULL offered and did not require was refused on `E6`; the refusal is sound, since
`named_codes()` iterates `N2_MODULES` by construction and the arm would need that signature changed.

**Reproduced, `R8`, at the fix tip in a scratch worktree, from a `sha256`-checked copy.**
`CODE = "V3-REVIEW"` at module level plus one `Issue(f"{CODE}-UNSWEPT-CODE", "x", "y")` call site
added to `review.py` — the exact shape `CODE_PATTERN` is written to find, named by no test:

```
negative control, unmutated class : 21 passed in 0.09s
mutated, this class               : 21 passed in 0.43s
mutated, whole battery            : 795 passed in 121.39s (0:02:01)
CODE_PATTERN matches              : ['-UNSWEPT-CODE']
named_codes() keys                : ['flow.py', 'issues.py', 'summary.py']
```

The regex sees the code; nothing hands it the file. Every figure the comment states reproduces
exactly.

**The way back, which the comment asserts and the leg did not test.** I ran it: with the mutation in
place and `review.py` moved from `N2_MODULES_WITHOUT_CODES` into `N2_MODULES`,

```
2 failed, 19 passed in 0.17s
FAILED …::EveryNamedCodeIsAssertedSomewhere::test_every_named_code_is_named_by_at_least_one_test
FAILED …::EveryNamedCodeIsAssertedSomewhere::test_the_sweep_actually_finds_codes_in_every_v3n2_module
```

A sweep is restored, so the claim holds. Restored from the checksummed copy, never by
`git checkout --`; `sha256sum -c` returned `OK` and the worktree was clean before removal. See
`V-2` for the one word in that sentence I do not think the measurement supports.

**The class sweep's conclusion is right, its evidence is not.** Two live sites carry the phrase in
the suite; the sibling at `:309-310` is about a *module* that names codes, and a module belonging to
no set does fail the partition — I confirmed the partition test compares `RSCLIB.glob("*.py")`
against the union of the four sets, so the sibling is true and correctly left alone. That analysis
is sound. What does not reproduce is the pasted output offered as proof it was run before writing;
`V-1`.

**Battery at the tip, run by me, `E3`.** `795 passed in 122.03s (0:02:02)` against the body's
`795 passed in 121.09s`. Unchanged from the round's tip, as a comment-only change requires.

---

## 4. `L-2` — verified closed, every stated fact re-derived

The journal's new §10 closing bullet records the read debt at the location the finding named, in
`HD-59`'s forward form: the prior bullets stand word for word and the statement is a new adjacent
paragraph, which is exactly what that ruling admits. `E1` names the round journal as a carrier for
statements of this kind, so the location is right.

Every fact in it reproduces:

| claim | my measurement | ✓ |
|---|---|---|
| `REVIEW.md` moved `395995d4…` → `aad3dd83…` | `git rev-parse` at `b737742` / `d3cda1a` / `1db5155` / `fccadfb` / `7a4e47b`: `395995d4` `395995d4` `aad3dd83` `aad3dd83` `aad3dd83` | ✅ |
| the same command over all nine members returns the same blob at both ends for the other eight, so **the count is one** | ran it over all nine `E10` paths at all five revisions; the other eight are byte-identical across every column | ✅ |
| two hunks, item G's at the `:93` pointer and item H's at the record channel | `git diff d3cda1a 56d1b17` on that file → one hunk `@@ -89,9 +89,11 @@`; `git diff 56d1b17 5a39945` → one hunk `@@ -162,8 +162,10 @@` | ✅ |
| the opening cold read read it end to end at the old blob, **320 lines** | `git show b737742:document-harness/REVIEW.md \| wc -l` → 320; `v3-cold-read-b737742.md:95` and `:405` both pin `395995d4…` at 320 | ✅ |
| no other round is in flight — rounds 1 and 2 CLOSED, the batch closes here | plan header line 3 and steps 7 / 10 | ✅ |
| this leg adds no read debt of its own | all nine members identical at `fccadfb` and `7a4e47b` | ✅ |

The two facts `E10`'s deferral clause asks for are now stated, and stated as deferral rather than
exemption. The leg reproduces the FULL's reading of the two hunks rather than adjudicating it
(`E12`), which is the correct posture; I read the hunks and record only that the leg's
characterization is the FULL's, unchanged — whether those hunks are design was the FULL's question,
not this VERIFY's.

The leg's reason for spending the fix on this rather than banking it is sound on its face and I
verified its load-bearing half: there is no round 4 whose opening would surface the debt, and `E10`
forecloses the alternative of letting the round's own FULL discharge it.

---

## 5. The rest of the repair diff — three banked rows

`R10` routing, re-derived rather than accepted. Bank **24 → 27** (`HARNESS-RIDERS.md` data rows at
`fccadfb` and `7a4e47b`: 24 and 27, header excluded). Each row names a target and carries a
redeem-when plus a deadline or its explicit absence.

- **`itemh-sweep-count`** (`L-1`). Figures re-derived, not accepted:
  `git diff 5a39945~1 5a39945 -U0 | grep "^-" | grep -c "migration/document-work-assurance-v3"` →
  **7**. The seventeen survivors reproduce per file exactly as the row's arithmetic states —
  `CONSTRUCTION-CHECKLIST.md` 5, `layer_path_check.py` 2, `dispatch.py` 1,
  `test_precommit_checks.py` 2, `test_dispatch.py` 3, `test_caller_surfaces.py` 4 = **17**. So
  7 + 17 = **24**, not 23. (The tip's `caller.py` hit is the round's newly written migration-advice
  comment, not a survivor — `git diff` confirms it replaced the deleted constant.) Correctly a row
  and not an edit: the figure lives in a committed commit body, which `E8` forbids amending and
  `HD-59` forbids rewriting in place, so the free channel has no bytes to apply.
- **`itemg-linecount-file`** (`L-3`). `wc -l` at `d3cda1a`, `1db5155` and `7a4e47b`: `flow.py`
  **770** at all three, `review.py` **782 → 184**. The row is right and its "no deadline" is
  defensible on `R9`'s own test.
- **`v1-digest-recipe`** (`O-1`). `review.schema.json:281` does carry the recipe importing
  `review.package_digest`; the import raises
  `ImportError: cannot import name 'package_digest'`. The class sweep reproduces: over the frozen
  pack, `package_digest` hits **exactly one** line, the other retired callables hit **zero**, and
  `member`'s 5 hits across 2 files are all inside `"description"` strings, none the retired
  callable. `paragraph-map.schema.json:5`'s `rsclib paragraph_skeleton` is present and
  `canonical_digest` still imports from the package root, so the row is right that only the import
  path broke. The frozen pack is **15** files, matching `E2`. Both measured corrections the row
  adds to the FULL's `O-1` are correct and improve on it: `HD-20`'s entry is scoped to the
  frozen-**and**-`E10`-member intersection, which this file is not in — what operates is `E2` plus
  `R10`'s own override sentence, which is not so limited; and `HD-61` / `HD-60` are both scoped in
  the archive to contract v4 sites, so neither could have carried these bytes even while live.
  Banking is compelled: bytes on a frozen path bank until an `E2` recorded ruling exists, however
  appliable.

---

## 6. Permanent boundaries

Run second, per `R3`.

- **`E2`** — nothing on a frozen path. Enumerated: the three changed paths are not
  `contract/Document-Work-Assurance-Contract-v4.md` and none is under
  `schema/document-assurance-v3/`. Contract v4's blob is `5dfb7b64…` at both ends, matching `E2`'s
  named blob.
- **`E10`** — no member edited by this commit; all nine identical at `fccadfb` and `7a4e47b`, and
  all nine resolve (9/9). The membership sentence is untouched, so `E10-sync` does not fall due.
- **`E8`** — title `V3-CORE-SET-CODE-FIX-v1` names the round; the body opens by naming its kind
  (`review fix`); no trailers. Not pushed: `origin/main` is at `2522ce1`, far behind. Staging
  method and non-amendment are `UNVERIFIABLE`. Writing the bank is not a boundary excursion — `R10`
  makes `HARNESS-RIDERS.md` the standing carrier for banked findings, and the round's own opening
  wrote it at `7135cd2`.
- **Guards, reproduced per commit rather than asserted.** Worktree at `7a4e47b`,
  `git reset --soft HEAD~1` so `git diff --cached` is this commit's diff exactly:

  ```
  layer_path_check.py     exit=0
  candidate_path_check.py exit=0
  review_freeze_check.py  exit=0
  ```

  Matching the body. Note this does not contradict the FULL's `O-3`: that prediction is about the
  commit that lands a *review record* under `migration/document-work-assurance-v3/`, which this
  commit is not — but it is what the commit landing **this** file will meet, and it should be read
  as the prediction landing rather than as a defect.
- **`E12`** — the finding was reproduced to write the fix, and the body says so. Confirmed by the
  shape of the mutation, which matches `B-1`'s and extends it.
- **`E9`** — one fix, and this VERIFY discharges the obligation it created. Nothing beyond the two
  accepted findings and the approved banking was opened; the diff bears that out.

---

## 7. Residual findings

Neither blocks. `R3`: a non-blocking finding is never inflated.

### `V-1` — the sweep evidence pasted as proof of "swept before anything was written" is a post-fix re-run

**Location.** `7a4e47b`'s commit body, the `HD-41` ④ / `E7` block: *"The class was swept before
anything was written … and the output is here rather than described"*, followed by two pasted
command outputs.

**Ground truth it violates.** `E3` — *"Re-run immediately before the claim; paste tool output, never
describe it from memory"* — and `HD-41` ④, whose whole purpose is that a reviewer can see on the
spot whether the sweep ran: *"贴证据是为了「跑没跑」可被评审员当场看见"*.

**Measured.** The body pastes, for the line-based arm, two lines — `v3-review-full-297bb2b.md:269`
and `test_fix_round_locks.py:310`. Re-run at the only tree that can be "before anything was
written", the fix's base `fccadfb`:

```
$ git grep -n -E "which sweep covers it" fccadfb
migration/document-work-assurance-v3/v3-review-full-297bb2b.md:269
tooling/tests/document_harness_review/test_fix_round_locks.py:258
tooling/tests/document_harness_review/test_fix_round_locks.py:301
  3 lines
```

Three, not two — and the second is the defective site itself, which the pasted output does not
contain because after the fix it no longer exists. The pasted line number `:310` is the sibling's
line **after** the fix's net +9 lines (`301 + 9`); the tolerant arm's `:309` is likewise the
post-fix start of a phrase that begins at `:300` before it. At `7a4e47b` the line-based command
returns exactly the body's two lines. So the output is a post-write re-run presented as the
pre-write sweep. The stated reason for escalating to a line-break-tolerant search — *"A line-based
grep misses one of the two live sites because the phrase wraps"* — is also only true post-fix: at
`fccadfb` the defective site sits entirely on `:258` and the line-based grep finds both. My own
tolerant sweep at `fccadfb` returns **4** hits, the fourth being the FULL record at
`v3-review-full-1db5155.md:78`, so "the third hit is inside a committed review record" undercounts
the record hits at that revision as well.

**What is not wrong.** The conclusion the sweep reached. Two live sites in the suite, one defective
and one true; I verified the sibling independently and it is true. The repair's substance is
untouched by this.

**Why it is not wording-level under `R9`.** `R9` excludes anything whose fix changes an evidence
binding, and this *is* the evidence binding — it is the artifact `HD-41` ④ exists to make checkable.
The downstream decision that goes wrong: a later reader auditing whether the class was swept before
the change gets output that cannot answer the question, and one re-running the stated command at the
stated revision gets a different count with no way to tell whether a site was missed or the output
was captured late.

**Route.** Not mine to choose (`R5` / `R10`), but the shape is constrained: the defect is inside a
committed commit body, which `E8` forbids amending and `HD-59` puts beyond rewriting, so no bytes
exist for the `E10` free channel to apply. That leaves a forward correction — a bank row, or a
statement in the closeout — which is the orchestrator's call.

### `V-2` — "the only thing that restores a sweep" is an absolute without its scope

**Location.** `test_fix_round_locks.py:261-262`: *"The way back is to move that module into
`N2_MODULES`, which is **the only thing** that restores a sweep."*

**Measured.** True within this class — `named_codes()` reads `N2_MODULES` alone, and I confirmed the
move does restore a sweep (§3). Not true of the repository: the same comment block documents eight
modules whose coverage is a named sweep living in another test file — `preview.py`'s in
`test_preview.py`, `enumerations.py`'s in `test_transcript_audit.py`, and so on — which is the
established alternative for a vocabulary this regex cannot reach, and is in fact `review.py`'s own
present disposition four lines below (`N2ValidatorTests`).

`HD-41` ② requires an absolute quantifier to carry its 量程, and this one does not. The scope is
recoverable from the immediately preceding sentence, which names `named_codes()` and the partition,
so it is **wording-level under `R9`'s own test** and I can name no downstream decision that goes
wrong — a reader who follows it takes a correct action. Reported because the sentence is the repair
for an over-claim, and because the discipline that would have caught it is live and standing. It
rides the next batch touching this file; it spawns no round and no read.

---

## 8. What this record does not establish

- **Nothing about a product run.** No run directory was built, no instruction frozen, no reviewer
  dispatched. The FULL's ceiling on the product-run leg is neither narrowed nor widened here.
- **Nothing about items G and H.** They were the FULL's subject. Where the FULL adjudicated —
  notably whether `REVIEW.md`'s two hunks change what a rule requires — I verified only that the
  repair implements the FULL's reading, and a VERIFY is not a re-certification (`R4`).
- **`E8`'s staging method and non-amendment**, and **the fact of user approval** for this leg and
  its routing, as stated in §1 and §2.
- **Sufficiency of any guard.** Two mutations reproduced in opposite directions with a negative
  control; that is binding force where measured, never a certificate over the rest.

---

## 9. Disposition

`REVIEWED_NO_BLOCKER`. Both accepted findings are closed and each was re-derived rather than
believed: `B-1`'s sentence now states what holds, mutation-tested in both directions, and `L-2`'s
read debt is recorded with every stated fact reproducing. The three banked rows are correctly routed
and their figures check out, including two measured corrections the leg makes to the FULL's own
`O-1` wording. Two residuals stand, neither in the repair's substance: `V-1`, an evidence defect in
the commit body that `HD-59` puts beyond editing and so routes forward; `V-2`, wording-level under
`R9`.

Reproduce any finding here to write its fix correctly, never to adjudicate the reviewer (`E12`).
