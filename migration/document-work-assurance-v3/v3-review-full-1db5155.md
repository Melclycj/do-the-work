# FULL review — round `CORE-SET-CODE`, subject `d3cda1a..1db5155`

**Verdict: `CHANGES_REQUIRED`** — 1 blocker, 3 lows, 3 observations.

Independent session. Dispatched, prompted, scoped and reported through the orchestrator, not the
executor (`R1`); the prompt handed me the range and nothing else, and everything below — round,
budget, authorization, obligations, every figure — was re-derived from the repository (`R2`). No
reported figure is carried forward unchecked. Every number in this record is followed by the
command that produced it, run at the tip unless a different revision is named.

---

## 1. What I read, and how far

`R4`, so the ceiling is visible rather than implied.

**Read end to end.** `migration/document-work-assurance-v3/v3-harness-review-contract.md` (6 lines,
which routed me to its successor) · `document-harness/CONSTRUCTION-CHECKLIST.md` (258 lines, both
sides) · `HARNESS-DECISIONS.md` `§live` (`HD-59` · `HD-44` · `HD-41` · `HD-36` · `HD-35` · `HD-34` ·
`HD-23` · `HD-9`, lines 30–162) plus `HD-45` and `HD-20`'s row · `HARNESS-RIDERS.md` (34 lines, all
24 rows) · `document-harness/journal/core-set-code-2026-08-27.md` (227 lines) · the three commit
bodies in full · the complete diff of the range, every hunk of all 17 paths ·
`tooling/rsclib/document_harness/review.py` at the tip (184 lines) ·
`tooling/hooks/layer_path_check.py` and `tooling/hooks/candidate_path_check.py` in full ·
`tooling/tests/document_harness_review/test_fix_round_locks.py` lines 230–390.

**Sampled.** `document-harness/plans/core-set.plan.md` — 625 of 824 lines (the rulings, the
constraints, items G and H, all eight round-3 acceptances, the resume pointer, the notes); items
A–F, rounds 1 and 2's work, were not read. The deleted suite `test_package_and_review.py` (1,461
lines at the base) — I read its class and method index, the two methods that moved, and grepped it
for every retired symbol; I did not read its body. The opening cold read record
`v3-cold-read-b737742.md` — its commit body, its member/blob table and its two `L` findings, not
its 451 lines. `CONSTRUCTION-LEDGER.md` — the round-3 entry only.
`tooling/rsclib/document_harness/cli.py`, `flow.py`, `review_subject.py`, `review_result_v2.py` —
the changed regions plus the surrounding function, not the whole files.

**Only probed.** The v2 review flow's end-to-end behaviour: I confirmed it through the suite that
drives the real command in a subprocess and through `dtw review --help`, and I did **not** build a
control plane and drive a review myself. `E8`'s "stage explicit paths, never `add -A`" is
**`UNVERIFIABLE`** — history does not record how the index was built. "Never amend" is likewise
`UNVERIFIABLE` from the committed state alone.

**Not a re-certification of anything earlier.** Rounds 1 and 2 are outside this subject.

---

## 2. What the round is, re-derived

The range is three commits on `main`: `56d1b17` (item G, candidate), `5a39945` (item H,
candidate), `1db5155` (round journal, record). Base `d3cda1a` is the orchestrator's round-3 open.
`git diff --name-only d3cda1a 1db5155` returns **17** paths — 16 at `5a39945`, which is the figure
item H's body claims and which checks out; the seventeenth is the journal.

**Budget.** `E9`'s own test, applied by me and not taken from the commit bodies: has a valid
independent FULL already occurred on this round? The only review-side event between the round's
open and its tip is the opening cold read at `7135cd2`, and I read its commit body — *"Result: no
verdict, because a read is not a round - 0 must-fix, 2 lows, 2 observations."* A read is not a
round and spends no budget (`R3`). So no FULL had occurred, both work commits are candidates, the
fix leg was unspent, and the round owed no VERIFY. The classification the two bodies state is
correct. **This record is that FULL.** From here the round has one user-approved fix and, if it is
taken, owes the targeted VERIFY.

**Authorization.** The plan carries user rulings 6, 7 and 24–26 for this round; ruling 9 slices
items G and H into it; step 12 orders item G in one commit and item H in one commit. That is what
landed. No `E2` authorization exists — `HD-60` and `HD-61` were consumed and retired at `a554c0b` —
and none was needed: `git diff --name-only` over the range names nothing under
`schema/document-assurance-v3/` and not `contract/Document-Work-Assurance-Contract-v4.md`.
Confirmed by enumeration, not by the bodies' assurance.

---

## 3. The blocker

### `B-1` — the note that replaced the sweep claims a binding the suite does not have

**Location.** `tooling/tests/document_harness_review/test_fix_round_locks.py:256-258`, the
`N2_MODULES_WITHOUT_CODES` docstring: *"listed rather than dropped, so the partition below still
accounts for them and **a code added to one later fails here** until someone says which sweep
covers it."*

**Ground truth it violates.** The class the enclosing guard exists to close, stated in its own
docstring at `:240`: *"F4 — no named issue code may exist without some test naming it."* And the
round's own journal §9 heading, *"Two guards changed shape, and neither was relaxed."*

**Measured.** I reproduced the real defect shape rather than a crash (`R8`): in a scratch worktree
at `1db5155` I added to `tooling/rsclib/document_harness/review.py` a module constant
`CODE = "V3-REVIEW"` and one call site `Issue(f"{CODE}-UNSWEPT-CODE", "x", "y")` — exactly the
shape `CODE_PATTERN` at `:248` is written to find — and ran the battery.

```
python -m pytest -q tooling/tests/document_harness_review/test_fix_round_locks.py
  21 passed in 0.49s
python -m pytest -q
  795 passed in 128.40s (0:02:08)
```

Nothing fires. `test_the_swept_set_and_the_n1_set_partition_the_package` compares module *names*
against the directory, so a new code inside a listed module changes nothing it looks at;
`named_codes()` at `:345` iterates `N2_MODULES` alone, so both the sweep test and
`test_every_named_code_is_named_by_at_least_one_test` are blind to `review.py`. The file was
restored from a `sha256`-checked copy, never by `git checkout`, and `sha256sum -c` returned OK.

**Not the same as the round's own mutation.** The journal's §8 row — *"`N2_MODULES_WITHOUT_CODES`
emptied → the module partition reddens"* — is real; I reproduced it (`1 failed, 20 passed`, the
failure being the partition test naming `review.py`). It proves the set is load-bearing for the
*module* partition. It does not touch the sentence's claim about a *code*, and `R4` is the reason
the distinction matters: mutation proves a test has binding force, not that its force is
sufficient.

**Why it blocks rather than banks.** The sentence is the round's compensating disclosure for
narrowing the sweep — the journal names the alternative (*"drop the module from the swept set and
say nothing"*) as the F4 defect class reappearing. What was written instead tells the next author
that the guard will catch them, and it will not. The narrowing is real: `review.py`'s coded
vocabulary is now unswept by anything, and the file says otherwise. That is F4's defect class
arriving with a note asserting its own absence.

**Minimum fix.** The sentence changes to state what holds (`E6`: when a finding names existing text
as wrong, the fix is that text changing) — the module is listed so the partition accounts for it,
nothing here fires if a coded vocabulary returns to `review.py`, and the compensating coverage is
`N2ValidatorTests` in `tooling/tests/document_harness_review/test_golden_review_views.py` for the
`V3-SCHEMA-<KIND>` vocabulary the module actually emits, which the regex structurally cannot see.
An alternative that also closes it — one assertion that `named_codes()` over
`N2_MODULES_WITHOUT_CODES` yields nothing — is acceptable **only** because it makes the existing
sentence true rather than adding a rule about the defect; it is not required, and taking it does
not license leaving the sentence unexamined.

---

## 4. The eight round-3 acceptances, each re-derived

| # | acceptance | my measurement | met |
|---|---|---|---|
| 1 | v1 package leg gone from its surfaces | `dtw review --help` offers `--subject` `--result` `--executor` `--repo-root`, no `--package`. `git grep -E "^\s*(def\|class) <name>" -- tooling/` for all nine retired callables plus `review_binding` exits 1 with no output. `REVIEW.md:93`'s pointer is retired and no path token replaces it. | ✅ |
| 2 | nothing the v2 path needs went with it | Battery green at the tip; the subprocess-driven `test_review_cli_v2_subject.py` builds a committed control plane and drives the real command. `review_result_v2.py` changed in exactly the two places a deleted symbol forced (the `SpecGap` message, the parity-ceiling paragraph), both named in the body. `_cmd_v3_review_subject` → `_cmd_v3_review` is wired: `set_defaults(func=_cmd_v3_review)` at `cli.py:600`, one definition, no stale reference. | ✅ |
| 3 | battery green, both counts stated, difference attributed | I ran both myself. Base `d3cda1a` in a scratch worktree: **854 passed in 129.49s**. Tip `1db5155`: **795 passed in 127.27s**. The 59 reconcile exactly: the retired suite carries **56** methods (`grep -c "    def test_"` on the base blob), `TheVersionOneModeIsUndisturbed` **4**, `TheReviewCommandReportsRatherThanCrashes` **1**, two moved in → 56+4+1−2 = 59. | ✅ |
| 4 | the default names no directory of this repository's own | `DEFAULT_REVIEW_RECORD_DIRS` holds the assurance review-records directory; the identifier is unchanged (ruling 24); `DEFAULT_SPECIFICATION_SURFACE`'s shape is matched. Prose sites: `caller.py`'s comment and `REVIEW.md`'s record channel both name the new one, the latter in words and not as a path token. `ONBOARDING.md` never named the old one — I re-derived that and the round is right (see `L-1`). | ✅ |
| 5 | migration advice here and nowhere else | The round's diff is 17 paths, every one inside this repository; no commit reaches a caller's tree. The advice is stated twice — `caller.py` beside the constant, `ONBOARDING.md` as a third pre-wiring bullet. | ✅ |
| 6 | three guards exit 0 on the staged tree, members resolve 9/9 | Reproduced per commit, not asserted: worktree at each commit, `git reset --soft <commit>~1` so `git diff --cached` is that commit's diff exactly, then each guard. `56d1b17`: 0/0/0. `5a39945`: 0/0/0. `1db5155`: 0/0/0. Members: `test -f` each of `E10`'s nine → **9/9**. | ✅ |
| 7 | stripped-tree residual falls to three | Recipe re-run from the round-2 journal's own wording, not from this round's report. Base `d3cda1a`: **123 files**, `LINK`+`PATHTOK` = **5** (`CONSTRUCTION-CHECKLIST.md:6`; both stubs at `:3`; `REVIEW.md:93` twice), `NAMETOK` 35. Tip `1db5155`: **122 files**, `LINK`+`PATHTOK` = **3**, `NAMETOK` 35. The three that remain are ruling 12's construction-side citations, and the two that closed are `REVIEW.md:93`'s pair. Every figure the journal reports here reproduces exactly. | ✅ |
| 8 | FULL returned no blocker, or → fix → VERIFY | Open. This record is the FULL and it returns `CHANGES_REQUIRED`. | ⏳ |

---

## 5. Implementation checks the acceptances do not cover

**The deletion set is forced, not chosen, and the correction to ruling 26 is right.**
`git grep -n -w package_digest d3cda1a -- tooling/ schema/` returns `flow.py:48`, `flow.py:727`,
`review.py:195`, `review.py:494`, `review.py:776`, plus four hits in the retired suite and the
frozen schema's description — so the second live call site inside `check_review_result` is real and
ruling 26's *"reached only through `flow.py`'s `review_binding`"* was wrong. The round writes the
correction forward and touches neither the plan nor the ruling, which is `HD-59`'s shape.

**Nothing kept is stranded, and nothing deleted was still reachable.** `render_result`,
`result_digest`, `accepted_findings` and `require_valid_n2` have no caller under `tooling/rsclib`
after this round — I grepped each, and the body's claim holds. `blocking_findings` and `validate_n2`
retain callers in `summary.py` and `issues.py`, `N2_SCHEMA_FILES` in `review_subject.py`,
`load_result` at `cli.py:398`. `flow.py` carries no residual reference to either digest function
after its import line went, so the import removal is clean.

**The two moved methods really are the two that survive on their own.** I diffed
`test_n2_a3_control_verdicts_are_exactly_the_contract_set` against the base blob: byte-identical.
`grep '\$ref' schema/document-assurance-v3/review.v2.schema.json` shows the v2 result schema
`$ref`s exactly the five `$defs` named — `reviewRound`, `instructionCompleteness`,
`perObligationDisposition`, `finding`, `verifyScope` — so three of the four enums the first method
pins are what the successor result is validated against today. The six that went with the leg
covered the frozen v1 result's own instance-level constraints, which no code checks any more.

**Guards, mutation-tested.** Four of the round's five staged mutations reproduced, each from a
`sha256`-checked scratch copy and restored from it, `sha256sum -c` OK every time:

| mutation | result | matches the round's claim |
|---|---|---|
| the old value restored to `DEFAULT_REVIEW_RECORD_DIRS` | `6 failed, 361 passed` — and they are the six the body names, by name, across `test_precommit_checks.py` and `test_init_command.py` | ✅ exactly |
| `--check-result` re-added to the parser | `test_an_input_of_the_retired_package_mode_is_refused_not_accepted` reddens | ✅ |
| the recursive `walk` neutered | `test_n2_a3_no_semantic_proof_field_exists_in_the_review_surface` reddens through its own reached-the-leaves assertion | ✅ |
| `N2_MODULES_WITHOUT_CODES` emptied | the partition test reddens, naming `review.py` | ✅ — but see `B-1` for what it does not prove |

`test_repo_root_discovery`'s literal is now 5 and
`grep -c "repo_root = _rooted(args)" cli.py` returns 5. `E5` holds where it matters: the
`test_precommit_checks.py` expectations are hand-written tuples compared whole, never the module's
own constant.

**The item-H hazard advice, re-run rather than believed.** `E3` obliges the round to run the
command that could falsify an assertion it writes into instruction text; I ran it independently in
a throwaway repository with no declaration:

- record staged under `migration/document-work-assurance-v3/`, carrying a broken token →
  `candidate_path_check.py` **exit 1** naming the token; with the freeze marker written,
  `review_freeze_check.py` **exit 1**, *"not a review record"*.
- the same record under the new default → both **exit 0**.
- one `review_record_dirs` line in that repository's own declaration naming the old directory →
  both **exit 0** again, record still where it was.

Break, control and repair all three reproduce. `review_record_dirs` does reach the freeze guard's
admission rule (`review_freeze_check.py:69`), so the six-test blast radius the round reports is the
real shape and not a coincidence.

**This repository's own exposure, confirmed.** No `.harness/scan-surfaces.json` exists here, and
`git ls-files` over the old directory returns **151** records of the `v3-review` / `v3-cold-read` /
`v3-checkpoint-read` families — both figures reproduce. The wired hook runs only
`layer_path_check.py`, so commits are unaffected. See `O-3` for what that means for this record.

---

## 6. Process and record conformance

Run second, per `R3`.

- **`E2`** — nothing on a frozen path. Enumerated, not assumed.
- **`E8`** — titles `V3-CORE-SET-CODE-{ITEM-G,ITEM-H,JOURNAL}-v1` name the round; each body opens by
  naming its kind; no trailers; the change boundary is items G and H plus the round journal, and
  `git diff --name-only` stays inside it. Not pushed: `origin/main` is at `2522ce1`, far behind.
  Staging method and non-amendment are `UNVERIFIABLE` from committed state.
- **`E9`** — walked above. Zero spent before this record.
- **`E10`** — one member changed, `document-harness/REVIEW.md`. The membership sentence is untouched,
  so `E10-sync` genuinely does not fall due, and both bodies say so. What is missing is `L-2`.
- **`R2`** — the decomposition is committed rather than session-held: the journal's §1 WorkSpec
  carries nine obligations each paired with its evidence. `HD-35` puts that on the executor and no
  plan supplied one, so writing it down is the right call and it removes what would otherwise have
  been chat-only load-bearing material.
- **`HD-41` ④** — the class sweep was run before anything was written and its output is in the
  commit body. The sweep itself is complete; its arithmetic is `L-1`.

---

## 7. Findings

### `L-1` — item H's two stated counts are each short by one, and its own list proves it

`5a39945`'s body: *"git grep -n over the whole tree for the old directory name, excluding history,
returns **23** lines; exactly **six** of them are the DEFAULT and move."*

Measured. `git diff 5a39945~1 5a39945 -U0 | grep "^-" | grep -c "migration/document-work-assurance-v3"`
returns **7** — `caller.py:50`, `test_precommit_checks.py` 31/32/419/430, `test_init_command.py:140`,
`test_caller_surfaces.py:206`. That is exactly the set the body names in the next two sentences; it
names seven token-carrying sites and calls them six. (`caller.py:47`, also named, is a comment
reading *"the migration directory"* and carries no token, so it is not one of the grep's lines.) The
seventeen that stay are correct — I re-derived them at the tip and all seventeen are present, in the
files and at the lines the body gives. 7 + 17 = **24**, not 23. The stated grep returns **30** lines
excluding `migration/`, the journal, the plans and the root registers, and **24** if the two
construction-side design documents `document-harness/split-design.md` and
`document-harness/split-travel-manifest.md` are excluded as well — the body's partition accounts for
neither, which is where the other six go.

The downstream decision: `HD-41` ①③ exist so a counted assertion can be re-run, and a later round
re-running this sweep to confirm the class is closed gets a different number and cannot tell whether
a site was missed or the arithmetic was wrong. **The class is closed** — every site is named and
every site that should have moved did — so the fix is the two figures, not the sweep. Wording-level
under `R9` by its own test: the accurate fact is recoverable from the adjacent enumeration and from
`git diff`.

### `L-2` — the round changes an `E10` member and records no read debt for it

`git rev-parse` on `document-harness/REVIEW.md`: `395995d4…` at the read subject `b737742` and at
the round base `d3cda1a`, `aad3dd83…` at `1db5155`. The opening cold read
`v3-cold-read-b737742.md` records that member at blob `395995d4…` (its §2 table, row 4, and its
closing blob table), and `E10`'s citation clause covers a member *only while its blob is unchanged
since a recorded end-to-end read*. So no recorded read is citable for the bytes that now stand, and
neither commit body nor the journal's §10 — a section titled *"Left open, and stated rather than
implied"* — says so.

This is not a novel obligation being invented here. Round 2's journal carried the same statement as
its own §9 bullet, and round 2's single fix leg was spent correcting that bullet's **count** after
its FULL found it short. The plan's resume pointer then wrote the debt forward — *"Three in-repo
members changed in round 2 … All three ride round 3's opening read."* Round 3 leaves the analogous
sentence unwritten, and the batch closes with this round, so there is no later round-open whose
sizing would surface it on its own.

The downstream decision that goes wrong: the next construction round's opening read sizes itself
from these records, and a reader who finds nothing recorded will cite `7135cd2` for
`document-harness/REVIEW.md` — a read the blob change has already invalidated. My FULL does not
discharge it: `E10` says the amendment's read *"is never banked as the round's FULL."*

Two edits are involved and neither adds a clause to any rule nor changes what any rule requires
outside what item G and item H were opened to change, so `E10`'s deferral is available on its face —
deferral, never exemption, and the deferral clause's own condition is that *the commit records both
facts*. Nothing in the range records them.

### `L-3` — item G's line figure names the wrong file

`56d1b17`'s body: *"In `flow.py` the `review_binding` indirection, which had no caller anywhere.
**That file** drops from 782 lines to 184…"*. `wc -l` at the base and the tip: `flow.py` is **770**
lines at both ends; `review.py` is what went **782 → 184**. The antecedent is the file named in the
preceding sentence, and it is the wrong one. Recoverable from the same paragraph's list of
`review.py` deletions and from the commit's own diffstat, so wording-level under `R9`.

---

## 8. Observations

`R5` — the question and the conclusion are the user's; I report the shape.

**`O-1` — the frozen-schema residual is real, correctly refused, and its recommended arm exists.**
`schema/document-assurance-v3/review.schema.json:281` still instructs a reviewer to reproduce a
package digest by importing `review.package_digest`, and that import now fails. Those bytes are
`E2`-frozen, both round-2 authorisations are retired, and `HD-20` overrides `R10`'s ordinary channel
for bytes on a frozen path, so the round could not write it and did not. I checked the recommended
route rather than taking it on trust: `HARNESS-RIDERS.md` rows `sig-write-once` and
`contract-wikilink-tier` both name *the next round holding a contract v4 `E2` write ruling* as their
redeem arm, so a third row on that arm is coherent. The executor declining to write it is right
under `E1` and `E8`; the routing is the orchestrator's act.

**`O-2` — four exported symbols now have no caller.** `render_result`, `result_digest`,
`accepted_findings`, `require_valid_n2`. Verified. Two of them had none at the base either, so this
round did not make them dead; `render_result` still carries two committed golden files and its
golden tests. Whether they should exist is not mine to conclude — the round names them rather than
sweeping them, which is the right disposal for a FULL to see.

**`O-3` — the hand-run exposure the round predicted is live right now, on this very record.**
`.harness/` currently holds `review-pending.json`, this repository has no scan-surface declaration,
and `R6` puts this record under `migration/document-work-assurance-v3/` — which the new default no
longer admits. So `review_freeze_check.py`, run by hand at the commit that lands this file, refuses
it as *"not a review record"*, and `candidate_path_check.py` scans it as a work product. Neither
blocks the commit, because `.githooks/pre-commit` runs `layer_path_check.py` and nothing else. The
round disclosed this outcome in both `5a39945`'s body and the journal's §7 and declined to work
around it, which is the correct call — the instrument's own record channel is `R6`'s, not the
caller default's. Flagged here so the orchestrator meets it as a known consequence rather than as a
surprise, and so that a hand-run guard exit 1 at this commit is read as the prediction landing
rather than as a defect.

---

## 9. What this record does not establish

- **Nothing about a product run.** No run directory was built, no instruction frozen, no reviewer
  dispatched from a mounted stripped tree. Round 1's step-6b honesty cap on the product-run leg is
  neither narrowed nor widened by this review, and the round correctly claims no more.
- **The v2 flow end to end by my own hand.** I confirmed it through the suite that drives the real
  command in a subprocess and through the command's help surface, not by building a control plane
  myself. Reachability is supported; a full product-shaped exercise of it is `UNVERIFIABLE` here.
- **`E8`'s staging method and non-amendment**, as stated in §1.
- **Sufficiency of any guard.** Four mutations reproduced and one claim was falsified; that is
  binding force where measured, never a certificate over the rest.

---

## 10. Disposition

`CHANGES_REQUIRED`. One blocker, whose minimum fix is a sentence in
`tooling/tests/document_harness_review/test_fix_round_locks.py`. Three lows, none of which I would
spend a fix leg on by itself: `L-1` and `L-3` are wording-level by `R9`'s own test and route to
`R9` or the bank; `L-2` names a downstream decision that goes wrong, so it is not wording-level, and
it is cheap enough to ride the same fix — but that is the orchestrator's weighing to put to the
user, not mine to assume.

Reproduce any finding here to write its fix correctly, never to adjudicate the reviewer (`E12`).
