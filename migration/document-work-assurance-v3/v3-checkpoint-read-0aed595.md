# Instruction-layer read — `0aed5950cf7cae5edb987529fb6b37450de3616c`

`E10` read of the instruction layer at `0aed595`. Not a round: no verdict, no budget consumed
(`R3`). It is the independent re-read owed by the amendment at `b9e6fd8`, so its subject is the
amended text itself and the layer it sits in — never the work that text governs — and it is
banked as nobody's FULL.

**Findings: 1 must-fix, 0 low, 2 wording-level, 3 observations.** The amendment is faithful:
both of `M-1`'s named literal replacements and `W-1`'s supplied bytes landed verbatim, and the
diff carries nothing else. The must-fix is that the defect `M-1` named survives one clause
later in the same paragraph: `R10`'s closeout sentence — added by the same round, at
`be9878a`, and untouched by the amendment because the minimum fix named the other sentence —
still states the `E10` free channel as unconditional, so a low whose supplied bytes are
design-shaped is applied at closeout without the round `E10` requires.

## 1. Subject, re-derived (`R2`)

Handed one SHA and the phrase *an E10 read*. Member set, blobs, figures and obligations are
re-derived here; nothing is taken from the dispatch prompt, the commit bodies, the ledger or the
rider bank.

```
$ git rev-parse HEAD          -> 0aed5950cf7cae5edb987529fb6b37450de3616c
$ git status --porcelain      -> (empty; 0 lines)
$ cat .harness/review-pending.json
  {"subject": "0aed5950cf7cae5edb987529fb6b37450de3616c",
   "dispatched_at": "2026-08-13T03:53:55+00:00"}
```

HEAD **equals** the subject and the tree is clean, so worktree reads are reads of subject bytes;
each member's worktree hash was re-derived with `git hash-object` and compared against
`git rev-parse 0aed595:<path>` — nine of nine EQUAL. The branch has taken no commit since
dispatch (03:53:55Z = 13:53:55+10:00, 14 s after the subject commit's 13:53:41+10:00), so this
record is the first it admits (`E9`).

`E10`'s sentence **at the subject blob** governs the member set: nine paths, closing with "and
nothing else". The sentence is byte-unchanged by the amendment (its diff touches `E10`'s
enclosing rule nowhere — the `CONSTRUCTION-CHECKLIST.md` hunk is `@@ -161,8 +161,10 @@`, inside
`R10`), and it is still item-for-item equal to `layer_path_check.LAYER` and to
`test_precommit_checks.py`'s hand-written `EXPECTED` — the three mirrors `HD-22` keeps by
discipline. I re-derived that equality by reading all three, not by running the test that
asserts two of them.

| # | blob at `0aed595` | lines | member | how it is covered here |
|---|---|---|---|---|
| 1 | `de4bd9aa` | 195 | `document-harness/CONSTRUCTION-CHECKLIST.md` | **changed** (`0602bc6c` → here) — **read end to end**; also this session's standing instructions |
| 2 | `54dfef83` | 38 | `document-harness/README.md` | unchanged — **read end to end** |
| 3 | `2ac5cc75` | 421 | `document-harness/EXECUTION.md` | **changed** (`85198e8f` → here) — **read end to end** |
| 4 | `3350bfac` | 284 | `document-harness/REVIEW.md` | unchanged — **read end to end** |
| 5 | `17ff31bb` | 5 | `migration/…/v3-harness-operating-contract.md` (stub) | **read end to end** |
| 6 | `52a97a48` | 5 | `migration/…/v3-harness-review-contract.md` (stub) | **read end to end** — the dispatch entry point |
| 7 | `68031fa2` | 124 | `contract/…-v3-supersession-1.md` | unchanged — **read end to end** |
| 8 | `e1a2f26b` | 113 | `contract/…-v3-supersession-2.md` | unchanged — **read end to end** |
| 9 | `09aa8699` | 44 | `schema/document-assurance-v3/paragraph-map.schema.json` | unchanged — **read end to end** |

Blob ids from `git ls-tree 0aed595`, line counts `wc -l` on `git show` at the subject. **No
member is covered by citation this time**: the layer is ~1 229 lines and reading it outright
costs less than establishing coverage eligibility for six of nine, so every row above is a
fresh end-to-end read at the stated blob. Members 7, 8 and 9 are blob-equal to the rows in
`v3-checkpoint-read-a5a04c3.md` §1 and could have been cited; that is recorded so a later read
may cite either record.

`ResearchSystem/HARNESS-DECISIONS.md` `§live` read in full (lines 1–142, which is the file
header plus §live up to the `§implemented` heading at line 143): ten entries — `HD-35`, `HD-28`,
`HD-33`, `HD-34`, `HD-27`, `HD-24`, `HD-23`, `HD-10`, `HD-15`, `HD-9`. Nothing in §live is
contradicted by the layer at this blob. `HD-20` and `HD-22`, both cited below, sit in
`§implemented` — in force, detail carried by `R10` and by the rider row respectively, which is
what that state means. The decisions book is cited by section, never by blob (`E10`).

## 2. Was the amendment what `E10` admits?

`E10` allows the must-fix pair only "deletions and the literal replacement the finding names".
The whole diff of `b9e6fd8`, read directly rather than from its body:

- `CONSTRUCTION-CHECKLIST.md` `0602bc6c` → `de4bd9aa`, 4 insertions / 2 deletions, all inside
  `R10` — "the `E10` free channel takes any finding whose record supplies the exact bytes or
  names the content" → "…takes, **on the conditions stated there**, any finding whose record
  supplies the exact bytes or names the content"; and "One exception, and it overrides the free
  channel:" → "One exception **beyond those conditions**, and it overrides the channel:".
  Both are `M-1`'s two named replacements, character for character.
- `EXECUTION.md` `85198e8f` → `2ac5cc75`, 1 / 1 — "and says so at its own head" → "and says so
  in its own opening sentence", which is `W-1`'s supplied byte string.

Nothing else changed. I checked `W-1`'s premise rather than accepting it: the tiering section's
heading line is `## Regression-battery tiering (2026-08-03 ruling — this section is the revert
unit)`, and the sentence that follows it — "Which verification a pass owes is tiered by the
change surface — for a product run's evidence pass **and for a construction batch's pre-commit
verification alike**" — is what carries the construction-side claim. The new wording is
accurate.

The three lows banked at `0aed595` (`E1-suff`, `tier-file-vs-clause`, `wspec-owner`) reproduce
`L-1`–`L-3` of the prior read, one row each, each naming a target clause and carrying both a
touch condition and the deadline the reader set — `R10`'s row format holds. The bank is 26 rows.

## 3. What I re-executed

- `git hash-object` × 9 vs `git rev-parse 0aed595:<path>` × 9 — all EQUAL (§1).
- `python -m pytest -q tests/document_harness/test_readme_enumeration.py
  tests/document_harness/test_precommit_checks.py`, run from `ResearchSystem/tooling` —
  `43 passed in 12.91s`. These are the two pins that bind layer files; both green at the
  subject blobs.
- `python ResearchSystem/migration/document-work-assurance-v3/N0/fixtures/validate_fixtures.py`
  → `41/41 cases behaved as declared; failures=0`, which is the figure README `:33` asserts.
- `git ls-tree 0aed595 --name-only ResearchSystem/schema/document-assurance-v3/` → 15 files,
  which is `E2`'s re-baseline count and the pack README `:22`–`:25` enumerates in four rows
  (8 + 2 + 4 + 1).
- Existence check on the eight battery commands `EXECUTION.md` `:329`–`:338` enumerates —
  seven distinct files, all present (`run_tests.py`, `run_p4_tests.py`, `run_p5a_tests.py`,
  `validate_fixtures.py`, `tests/harness/run_tests.py`, `tests/stage_control/run_tests.py`,
  `rsc.py`; the eighth command is the root `pytest` invocation, which names no new file).
- `ResearchSystem/tooling/hooks/` → exactly the three tracked checks README `:34` names.
- `REVIEW.md` `:44`–`:47` asserts that four of seven findings in `v3-review-full-fef3a2e.md`
  name checker assertion strength: that record carries `f1`–`f7`, and `f2`–`f5` are
  `chk-bookkeeping`, `chk-tripwires`, `chk-tooling`, `chk-open`. Exact.
- A path scan over all nine members for the two classes `layer_path_check` decides, plus every
  markdown link target. No link is broken. Path results are finding `W-1`, `W-2` and `O-1`.

## 4. Findings

### Must-fix

**`M-1` — `R10`'s closeout clause states the free channel unconditionally, one clause after the
sentence the amendment just conditioned.**

*Location.* `CONSTRUCTION-CHECKLIST.md` `de4bd9aa` `:177-178`, inside `R10`'s last sentence,
against `E10` `:107-113`.

*Ground truth.* `R10` `:174-180` reads: "A FULL returning `REVIEWED_NO_BLOCKER` with lows does
not bank them by default: before closeout the orchestrator weighs each low's deadline against
its touch trigger and puts the spend-the-fix-leg / bank choice to the user — **a choice reached
only where no bytes were supplied, since supplied bytes take the free channel above** (…)."
`E10` conditions that channel three ways: it "holds for as long as no round has relied on the
text" (`:107-110`); "an amendment adding a clause to any rule, or replacing or deleting text so
that what a rule requires changes, is design and opens a round" (`:110-111`); and "when the free
channel and the design test both apply … **design wins and the round opens**" (`:111-113`).

*Why this is not the finding already fixed.* It is the same defect class in a sibling clause.
`git log -L 170,181` on this file shows the clause was **added at `be9878a`**, the same commit
whose read produced `M-1`; `M-1`'s minimum fix named the earlier sentence only, and `E10`
confines the amendment to "the literal replacement the finding names", so the amendment was
right to leave this alone and the class survived. `E7`'s discipline — the class, not the
instance — is the reason a re-read exists.

*What goes wrong.* At closeout of a FULL that returned `REVIEWED_NO_BLOCKER` with lows, one
low's record supplies bytes whose fix adds a bound. `E10` `:111-113` says design wins and a
round opens, which means an `E11` preview card and the user's approval. `R10` says the user
choice is "reached **only** where no bytes were supplied" and that supplied bytes take the free
channel — so the orchestrator applies the bytes immediately, instruction layer included, and
never reaches the user. That is a rule change landing with no card and no approval. Unlike the
`E2` branch of the same sentence, nothing else guards it: `E2` independently refuses a write to
a frozen path, but no rule independently refuses a design-shaped free-channel application. The
round in hand demonstrates the case is live rather than hypothetical — all three of its lows
were banked precisely because "each fix would add a bound and is therefore design".

*Minimum fix* (one literal replacement; it adds no rule, and points only at conditions `R10`
already references three sentences earlier):

- `:177-178` — "— a choice reached only where no bytes were supplied, since supplied bytes take
  the free channel above" → "— a choice the free channel pre-empts only where the supplied
  bytes meet its conditions above".

Deleting the clause outright is the other admissible answer (`E10` admits deletions): it
restores the sentence as it stood before `be9878a`, which carried no such claim.

### Wording-level (`R9` — no actor's action changes)

Both name a repository path missing its `ResearchSystem/` prefix, in a member that is not
`E2`-frozen. In each case the correct prefix is recoverable from adjacent text in the same
file, so no downstream decision goes wrong and neither spawns a round or a read. Bytes are
supplied, so `R10` also lets the `E10` free channel take them at the orchestrator's option;
otherwise they ride the next batch touching these files.

**`W-1` — `EXECUTION.md` `:408` writes a run-issue path without its prefix.** The token
`` `runs/p4-doc/issues/user-decision-triage-comparator-environment-defects.json` `` resolves
from neither the repo root, nor the file's own directory, nor `ResearchSystem/`. The file
exists at `ResearchSystem/assurance/runs/p4-doc/issues/user-decision-triage-comparator-environment-defects.json`,
and the same file uses the full prefix for sibling references at `:186`, `:259` and `:405`.
Bytes: `runs/p4-doc/issues/user-decision-triage-comparator-environment-defects.json` →
`ResearchSystem/assurance/runs/p4-doc/issues/user-decision-triage-comparator-environment-defects.json`.

**`W-2` — the review-contract stub `:5` writes the dispatch fixture without its prefix.** The
token `` `tooling/tests/fixtures/expected-construction-prompt.txt` `` resolves only under
`ResearchSystem/`, which is exactly the missing-prefix class `layer_path_check` blocks — inside
a layer member, in the sentence that explains why the stub's path is kept. Bytes:
`tooling/tests/fixtures/expected-construction-prompt.txt` →
`ResearchSystem/tooling/tests/fixtures/expected-construction-prompt.txt`.

### Observations (`R5` — reported; the conclusions are the user's)

**`O-1` — the layer carries five paths its own guard would refuse today, and the guard can see
none of them.** Besides `W-1` and `W-2`: `supersession-1:89`
(`` `schema/document-assurance-v3/review.v2.schema.json` ``), `supersession-2:60`
(`` `assurance/runs/` ``), `supersession-2:83` (`` `schema/` ``) and `supersession-2:99`
(`` `templates/run-v2/` ``, whose real home is `ResearchSystem/assurance/templates/run-v2/`).
Those four sit in `E2`-frozen members, so their bytes owe `E2`'s recorded ruling and bank
however appliable they are — `R10`'s stated exception and `HD-20` behaving exactly as written,
and the reason I supply no bytes for them. Two structural notes rather than a defect claim:
the contract files use a ResearchSystem-relative convention consistently, so "defect" is the
guard's convention read backwards onto signed text; and `layer_path_check` scans only the lines
a staged diff **adds**, which is a recorded position (`v3-review-full-8ec4c60.md` B1), so the
layer's path-resolution property is guarded forward only and its current stock was never
checked. This scan is that check, and it is now on the record.

**`O-2` — `R10`'s "it overrides the channel" is singular where `E10` names two channels.** The
immediate antecedent is the free channel, while `E10` `:102-104` bars **both** the free channel
and the must-fix one from writing an `E2`-frozen path, and `HD-20` says the same in both
directions. The exception's own body is unconditional and gets it right ("bytes on a path `E2`
also freezes bank until that rule's recorded ruling exists … however appliable they are"), and
dropping "free" was the prior read's deliberate generalization, so I record this rather than
file it: the sentence is under-specified, not wrong, and `E2` refuses the write on its own.

**`O-3` — the amendment commit carries two channels' bytes, and `E10` does not say whether it
may.** `E10` scopes the must-fix pair to "only deletions and the literal replacement the
finding names", which reads as a constraint on the amendment commit; the free channel
independently authorizes `W-1`'s byte, and `b9e6fd8` carries both. In fact the pair's property
holds — I verified the diff is `M-1`'s two replacements plus `W-1`'s one and nothing else — but
a later auditor asking "did that pair stay a non-round?" has to read the commit body to know
which byte belongs to which channel, where the diff alone would otherwise settle it.

## 5. Coverage disclosure (`R4`)

- **Read in full at the subject blobs:** all nine members (195 + 38 + 421 + 284 + 5 + 5 + 124 +
  113 + 44 = 1 229 lines, the nine rows of §1's table in order);
  `HARNESS-DECISIONS.md` `§live` (lines 1–142); `HARNESS-RIDERS.md` (36 lines, 26 rows);
  `layer_path_check.py`; the `EXPECTED` block and its two tests in `test_precommit_checks.py`;
  `test_readme_enumeration.py`'s docstring and test; both dispatch fixtures.
- **Read in part:** `v3-checkpoint-read-be9878a.md` — §6 Findings and §7 coverage, to establish
  that the amendment applied the named bytes and nothing more; `v3-review-full-fef3a2e.md` —
  its findings table only; `dispatch.py` — the read-dispatch family, by grep and excerpt.
- **Probed only:** the eight battery commands were checked for existence, **not run**; the tier
  the amendment declared (doc-only) is therefore unverified beyond the two pins, which is the
  same unwritten reading `tier-file-vs-clause` banks.
- **Not established.** That this read ran in a fresh context is a process claim with no evidence
  lock (`R4`). That the free channel's reliance condition is unmet for `M-1`'s target clause is
  my reading of the two commits since `be9878a`, not a mechanical result — it does not affect
  the finding, since a must-fix takes `E10`'s must-fix channel either way.
- **Out of subject.** Whether `R10` should carry a closeout routing sentence at all, and whether
  the free/must-fix channel split should be summarized in two places, are `R5` questions.
