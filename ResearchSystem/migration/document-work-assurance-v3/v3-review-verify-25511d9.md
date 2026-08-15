# VERIFY — `2d76629..25511d9` (round `V1-CONTEXT-EXACT`, the fix leg)

| | |
|---|---|
| round | VERIFY, construction-side (`CONSTRUCTION-CHECKLIST.md` E1–E12 / R1–R10) |
| subject | `2d76629fb66c8d35f9b422b11b0fa6fedc5cbf0b..25511d9e0b8fd489781fa54c464193370597ac81` |
| range content | two commits — one `chore` declared outside the round, one `review fix` |
| **verdict** | **`REVIEWED_NO_BLOCKER`** |
| findings | 0 blocker, 0 low, 3 observation |
| record | this file; the execution side commits it (`R6`) |

`b1` is closed and the closure is measured, not asserted. The mutation the FULL used to
falsify the round's `E7` claim — `startswith("context (non-normative)")` — now turns the
class sweep and the audit leg red where before the fix the identical mutation left the whole
battery green; the failing subtest identifies itself through the tuple's own `why` column, so
the evidence names the *shape*, not only the method. The two historical mutations still bind
at their recorded counts. `L-1` and `L-2` are closed, `L-2` byte-for-byte as proposed. The row
the user added beyond the reviewer's minimum binds independently under an isolating mutation,
and the widening was declared in the commit body rather than left to be discovered.
`instruction.py` is byte-identical to the reviewed bytes, so the repair narrowed the round's
change surface instead of widening it. Every figure the fix commit reports reproduces at the
tip on this machine.

Three observations, none of them findings: a fourth slip shape of the same predicate leaves
the battery green (evidence for the FULL's still-open `O-1`, not a re-certification — `R4`);
the out-of-round `chore` states its own budget conclusion where rule 7 of the retired
operating contract reserves that to the user; and the base commit's tree does not pass the
repo's own pre-commit gate, self-healing one commit later.

---

## 1. Subject, re-derived (`R2`)

Nothing below is taken from the dispatch prompt, a ledger line, a journal or a commit body.

**Round and budget.** `git log` over the range returns exactly two commits, linear from the
base:

| # | sha | title | kind, from its own body |
|---|---|---|---|
| 1 | `32cf220` | `chore(repo-audit): wikilink scan skips POSIX character classes` | declares itself *outside* the round and outside its boundary |
| 2 | `25511d9` | `V3-V1-CONTEXT-EXACT-FIX-v1` | `Kind: review fix.` |

`E9`'s test — *has a valid independent FULL already occurred?* — resolves **yes** from the
repository: `v3-review-full-ca9c055.md` exists under `migration/document-work-assurance-v3/`
and its commit `2d76629` is the base of this range. So `25511d9` is the round's one
user-approved fix, and it obliges exactly this VERIFY. No second fix commit exists. The
budget is now spent: one FULL, one fix, this VERIFY.

`E9`'s concurrency clause holds for the FULL: `2d76629` (02:01:52) is the record commit, and
the branch took nothing between the dispatch tip `ca9c055` and it — `2d76629`'s parent is
`ca9c055`. The `chore` landed at 02:02:17, *after* the record, not inside the window.

**Authorization, and its ceiling (`R7`).** The fix commit declares its boundary is wider than
the reviewer's minimum by one row, *"the user added when authorizing"*. That approval exists
in the repository only as the executor's own prose — the commit body and journal §2, both
written by the party they authorize. I can confirm the text exists; I cannot confirm the
ruling. **Marked, not verified** (`R4`) — the same ceiling the FULL recorded for the two
approvals it met, and the same disposition: state it and move on. The declaration itself is
what `E9` requires (*exceeding an approved fix boundary requires saying so, never silently*),
and it was made in the commit body rather than left for me to find, which is the point of
the clause.

**Changed paths, classified by hand** (`git diff --name-status 2d76629..25511d9`, five paths):

| class | count | paths |
|---|---|---|
| tests | 2 | `tooling/tests/document_harness/test_instruction_form.py`, `…/test_transcript_audit.py` |
| round record | 1 | `document-harness/journal/v1-context-exact-2026-08-05.md` |
| ledgers | 1 | `HARNESS-LEDGER.md` |
| thesis-side tooling (outside `ResearchSystem/**`) | 1 | `Thesis/Work/Tooling/repo-audit.py` |
| resident harness code · schema · contract · instruction-layer member · template · run artifact · rider bank | **0** | — |

**Obligation.** From the FULL: blocker `b1` (one row in `NOT_THE_CONTEXT_SECTION`, the same
heading in `test_transcript_audit.py`'s loop, then re-run the §2.3 mutation and record that
both go red), low `L-1` (the mutation counts' missing scope), low `L-2` (the enumerated-form
ruling absent from the ledger pointer). The FULL explicitly did **not** ask for bare
`## Context`, whitespace variants, or any generalization of the tuple.

---

## 2. The accepted findings, verified

### 2.1 `b1` — closed, and the closure is the property the round was short of

`instruction.py` is untouched: `sha256` at the tip is
`f2dee2480df86432a5e7408916f5dd026738ef1ebbb38e4c0309a271e0db398a`, which is the digest the
FULL recorded for the reviewed bytes. The predicate is still
`title.casefold() == "context (non-normative)"` (`instruction.py:187`). `b1` was a defect in
the tests, and the repair is confined to the tests — the boundary narrowed rather than widened.

`NOT_THE_CONTEXT_SECTION` goes from five rows to seven; `test_transcript_audit.py`'s loop
from two headings to three. Every mutation below was applied to `instruction.py`, then
restored from a scratchpad copy whose `sha256` matched the delivered file before and after,
never `git checkout --`; `git status --porcelain` is empty after the last restore.

| # | mutation | scope | measured | which row fired |
|---|---|---|---|---|
| M3 | `.startswith("context (non-normative)")` — the `b1` shape | two modules (38) | **2 failed, 36 passed** | `("FULL b1: the new literal's own boundary — opens with the whole exempt title", ())` |
| M3 | same | whole tree | **2 failed, 598 passed** | form sweep + `test_a_unit_anchored_outside_both_kinds_of_section_is_refused` |
| M3 | same, against the **pre-fix** test files (`2d76629` bytes) | two modules (38) | **38 passed** | — the hole the FULL measured |
| M1 | `.startswith("context")` — the `V-1` shape | two modules | **2 failed, 36 passed** | `('V-1: opens with it, one word later than f1', ())` |
| M2 | `"context" in title.casefold()` — the f1 shape | two modules | **3 failed, 35 passed** | + `test_a_heading_that_merely_mentions_context_is_not_the_context_section` |
| M4 | `in ("context (non-normative)", "context")` — isolates the user's added row | two modules | **1 failed, 37 passed** | `('the bare heading: exempt through both earlier eras, refused since the exact form — a behaviour change nothing else records', ())` |

Three things follow, and they are the ones that matter:

* **The delta is real.** The identical mutation is 38-green against the pre-fix tests and
  2-red against the delivered ones. The FULL's measurement (whole tree, 600 green before) and
  mine (598/2 after) bracket the same change.
* **The added row binds on its own**, not as a passenger of `b1`'s. M4 loosens the predicate
  in exactly the one direction that re-exempts bare `## Context` and nothing else, and exactly
  that subtest goes red. The user's addition is not decorative.
* **The evidence identifies the shape.** Each failing subtest carries the tuple's `why`
  column into the assertion message, so a later reader learns *which defect class* reopened,
  not merely that a method failed. That is a genuine improvement on both earlier eras.

`E5` holds on both legs. The form leg asserts `len(outside) == 1`, `repr(heading)` inside it,
and `resolve_form → FORM_PROSE`; `repr` carries its closing quote, so `'Context'` cannot be
satisfied by an issue naming `'Context (non-normative)'`. The audit leg is stronger still —
exact equality on the result, on the whole `finding_id` list, and on the kind. Both tuples are
hand-written literals, nothing derived from the module.

### 2.2 `L-1` — closed

`journal/v1-context-exact-2026-08-05.md` §3's heading now reads *三次；跑的是**两个被改模块共 38
例**：`test_instruction_form.py` + `test_transcript_audit.py`*, and the section adds the
reconciliation in its own words (*38 与 §4 的 600 是两条不同的命令*). §4 additionally explains
why the battery legitimately stays at 600 across the fix: the repair adds **data rows to
`subTest` loops** (form 5→7, audit 2→3), not test methods. I confirmed that independently —
`git diff` on the two modules adds no `def test_`, and the tip battery is 600. The named
downstream decision in `L-1` (a later reader reproducing the wrong scope and reading a
mismatch as a regression) is answered: the command and its case count are both on the heading
line that carries the numbers.

### 2.3 `L-2` — closed, byte-for-byte

The FULL proposed `之后 **P5B 批次（用户 2026-08-05 裁：走编号态）→ HarnessIssue f6/f7 → P5C**。`
The delivered breakpoint block carries exactly that clause (`HARNESS-LEDGER.md:34-37`,
reflowed to hold it). A cold session opening P5B from the pointer — which `CLAUDE.md` makes
the cold-start entry — now sees the form it must author in, without following the journal
link. The ledger is at **120 lines** against `MAX_LINES = 120`; `ledger_cap_check.py` exits 0,
and the fix commit states the consequence for the closeout rather than leaving it to be hit.

---

## 3. The rest of the repair diff

### 3.1 The out-of-round `chore` (`32cf220`) — correct, narrow, and tested by its negative control

It is in my subject range, so it is mine to review whatever it declares about budget.

*The defect it fixes is real and reproduces.* Neutering the one added line
(`if POSIX_CLASS.match(c): continue`) and re-running the audit gives:

```
[!!] Broken wikilinks: 1
     - ResearchSystem\migration\document-work-assurance-v3\v3-review-full-ca9c055.md | :space:
```

That is the reviewer's own `grep -rniE` command, quoted in a correct record, read by `WIKI` as
a link to a note named `:space:`. With the line restored: **0 broken wikilinks, orphans 213,
`RESULT: clean (exit 0)`** — both figures as the commit body reports them.

*The negative control holds.* I appended a genuine broken wikilink plus two further POSIX
classes to a journal file. The audit reported **exactly** the genuine one and skipped both
classes; the file was then restored from a scratchpad copy whose `sha256` matched before and
after.

*The carve-out is as narrow as claimed.* `^:[a-z]+:$` matches only the POSIX class names,
after the `|` and `#` splits; a colon is illegal in a Windows filename, so no real target is
dropped. The comment's two cross-references check out against the tree rather than against
its own prose: `strip_inline_code`'s docstring does scope itself to the markdown-link scan and
does record the 29% wikilink blinding, and `45cae29` is a real commit
(`V3-PHASE-B-REVIEW-FIX-v1`). Widening this into `strip_inline_code` — the tempting fix — is
the one the record already measured and rejected, and the comment says so where the next
reader will be standing.

*Its stated justification is verified, not accepted.* `.git/hooks/pre-commit` does run
`repo-audit.py` and does block on a hard finding, so the review record genuinely could not
land without either this fix or `--no-verify`. The hook documents the bypass; the executor
declined it and fixed the tool instead, with a measured negative control in place of a test
suite that does not exist. `E6` is satisfied on its own terms — standing up a suite for a
one-line predicate is the machinery that rule refuses, and the limit is stated in the commit
rather than left to be discovered.

### 3.2 Permanent boundaries (`R3` — second)

**`E2`.** Zero paths under `ResearchSystem/schema/` in the range. The pack still holds
**15 files**, the 2026-08-03 re-baseline count. Supersession-1 (`68031fa2`) and
supersession-2 (`e1a2f26b`) are unchanged at both ends. No ruling was needed and none was
claimed.

**`E10`.** No layer member appears in the range. Member set re-derived from `E10`'s own
sentence, blobs computed at both ends:

| # | blob at `2d76629` | blob at `25511d9` | member |
|---|---|---|---|
| 1 | `4d0c7330` | `4d0c7330` | `document-harness/CONSTRUCTION-CHECKLIST.md` |
| 2 | `ae887dd4` | `ae887dd4` | `document-harness/README.md` |
| 3 | `df2a7834` | `df2a7834` | `document-harness/EXECUTION.md` |
| 4 | `3350bfac` | `3350bfac` | `document-harness/REVIEW.md` |
| 5 | `17ff31bb` | `17ff31bb` | `migration/…/v3-harness-operating-contract.md` (stub) |
| 6 | `52a97a48` | `52a97a48` | `migration/…/v3-harness-review-contract.md` (stub) |
| 7 | `68031fa2` | `68031fa2` | `contract/…-supersession-1.md` |
| 8 | `e1a2f26b` | `e1a2f26b` | `contract/…-supersession-2.md` |
| 9 | `09aa8699` | `09aa8699` | `schema/…/paragraph-map.schema.json` |

Nine against nine, all unchanged, and every one equal to the blob the FULL recorded at
`ca9c055`. The round relied on layer text whose bytes have not moved since the opening read
(`562e948`) recorded them.

**`E8`.** Both commits name their kind in the body's first sentence. `V3-V1-CONTEXT-EXACT-FIX-v1`
names the round and follows the established suffix convention (`V3-SIMP-ABCD-CLOSEOUT-v1`,
`V3-PHASE-B-REVIEW-FIX-v1`). One dense paragraph each, **no trailers** on either
(`git log --format='%(trailers)'` returns empty for both). Author date equals committer date
on both, so nothing was amended or rebased. `origin/main..HEAD` is **488** — three more than
the FULL's 485, i.e. the record plus these two — so nothing was pushed. The worktree is clean
at the tip.

**`R10`.** `HARNESS-RIDERS.md` is untouched in the range: 0 paths. Consistent with a fix leg —
the FULL returned `CHANGES_REQUIRED`, so its lows were repaired rather than banked, and the
`R10` clause about weighing lows before closeout does not apply to this leg.

**`E3`.** Every figure the fix commit asserts reproduces at the tip on this machine:

| claim | command | measured |
|---|---|---|
| pytest 600 passed | `python -m pytest -q` (in `ResearchSystem/tooling`) | **600 passed in 86.98s** |
| P2 29/29 | `python tests/run_tests.py` | **tests: 29 passed: 29 failed: 0** |
| P4 80/80 | `python tests/run_p4_tests.py` | **tests: 80 passed: 80 failed: 0** |
| P5A 32/32 | `python tests/run_p5a_tests.py` | **tests: 32 passed: 32 failed: 0** |
| contract fixtures 41/41 | `python migration/…/N0/fixtures/validate_fixtures.py` | **41/41 cases behaved as declared; failures=0** |
| `compile --check` 0/0 | `python ResearchSystem/tooling/rsc.py compile --check` | **0 error(s), 0 warning(s)**, exit 0 |
| three guards exit 0 | `ledger_cap_check` · `layer_path_check` · `review_freeze_check` | **0 · 0 · 0** |
| ledger 120 against a cap of 120 | `wc -l` + `MAX_LINES` in `ledger_cap_check.py` | **120** vs **120** |
| repo-audit clean, 0 broken wikilinks, orphans 213 | `python Thesis/Work/Tooling/repo-audit.py` | **exit 0 · 0 · 213** |
| restore digest | `sha256sum` on delivered file and scratchpad copy | **`f2dee248…` on both** |

**A note, verified benign, not a finding.** The ledger's breakpoint still reads
*构造完毕、欠 FULL* although a FULL and a fix have landed. Precedent settles it: at
`c7fb720`, the `SIMP-ABCD` VERIFY commit, the same line still read *欠 FULL*, and the pointer
was corrected at the closeout (`214f743`). The pointer is not the load-bearing signal for
`E9` either — the FULL answered *has a FULL occurred?* from `git log` plus the presence or
absence of a `v3-review-*` file, which is what I did too.

---

## 4. Observations (`R5` — reported; the conclusions are the user's)

**`O-1v` — a fourth slip shape of the same predicate leaves the whole battery green.** Not a
finding, and deliberately not: `R4` says a VERIFY is never a re-certification, the accepted
blocker is closed exactly as specified, and the FULL bounded its own ask to one row. I report
it because it is *measured evidence for the FULL's `O-1`*, which is a design question the user
owns and which closing `b1` was explicitly said not to end. Loosening the predicate to
`title.casefold().endswith("(non-normative)")` — the suffix mirror of the substring→prefix
slip that has now bitten three times — gives:

```
predicate on 'Appendix A (non-normative)': True
resolve_form    : ('enumerated', ())
form_conformance: ()

$ python -m pytest -q     # whole tree
600 passed
```

So `## Appendix A (non-normative)` over a normative frozen table is again non-normative, the
paragraph map and the preamble gate again switch off, and the battery is again green. The
delivered set is written forwards for the *prefix* direction; the class of *a heading that is
not the section* is larger than the slip family the set enumerates, and no set of literals
closes it — which is the shape `O-1` asked you to look at, one measurement further along. The
banked `ctx-ground` row sits on the same ground.

**`O-2v` — the out-of-round commit states its own budget conclusion.** `32cf220`'s body says
*"it consumes no part of the E9 budget"*. `E9` says *never self-classify which round consumed
what*, and the retired operating contract — the reference of record where the checklist is
silent — is explicit: *"Naming the kind is description; deciding which round it consumed stays
the user's"* (`7011916` discipline rule 7). What makes this benign rather than a finding is
that everything needed to overturn it is on the face of the commit: the criterion is stated
(*thesis-side tooling, not the work product under review*), it is the criterion of the recorded
2026-08-04 ruling, and the changed path is outside `ResearchSystem/**` — decidable by
inspection, not by narrative, which is the difference between this and a renamed round. The
ratification is the closeout's, and the commit is immutable, so there is nothing to fix here;
I record it so the closeout ratifies rather than inherits it.

**`O-3v` — the base commit's tree does not pass the repo's own pre-commit gate.** `32cf220`'s
body says the audit fix *"had to exist in the working tree before the review record could land
at all"*. It follows that `2d76629` was committed while the fix was unstaged: the gate passed
on a working-tree state that is not the committed state, and a checkout of `2d76629` fails its
own audit — I measured exactly that in §3.1, where neutering the carve-out reproduces the
false positive against the record that commit introduced. It self-heals one commit later, and
the cheaper ordering (audit fix first, record second) was available and would have cost
nothing. Recorded as scope, not as a defect in the repair: the tip is clean and `R6` is
right that the reviewer's bytes were not the executor's to edit.

---

## 5. Coverage disclosure (`R4`)

**Read in full:** the range diff (all five paths, both directions); both changed test modules
end to end; `HARNESS-LEDGER.md`; `HARNESS-RIDERS.md`; `v3-review-full-ca9c055.md`;
`CONSTRUCTION-CHECKLIST.md` (standing instructions); the journal's diffed sections;
`.git/hooks/pre-commit`; `repo-audit.py`'s link-scan block and `strip_inline_code`.

**Read in part:** `instruction.py` `:170-200` (the predicate and its docstring);
`repo-audit.py` header and `:120-200`; `ledger_cap_check.py`; the retired operating contract
at `7011916` (discipline rules 6–9, the role-boundary and scope-discipline sections).

**Probed only:** the other eight instruction-layer members — I verified their blobs at both
ends of the range, not their contents, because none is in the subject and the FULL established
their equality with the opening read's record.

**Commands run live at the tip:** the ten rows of §3.2; six mutations of `_is_context_title`
(prefix-of-full-title against the delivered *and* the pre-fix tests, prefix, substring,
bare-title isolation, suffix), each restored from a `sha256`-verified scratchpad copy, never
`git checkout --`; one neutering of `repo-audit.py`'s carve-out and one injected-defect
negative control, each restored the same way; three direct probes of
`resolve_form` / `form_conformance` / `_is_context_title` on hand-built documents.
`git status --porcelain` is empty and all five delivered digests re-verified after the last
restore.

**Marked, not verified (`R4`).** The user's approval to add the bare-heading row exists in the
repository only as this round's own prose (commit body, journal §2). Same ceiling as the two
approvals the FULL marked; `R7` says state it and move on. It is a ceiling on this review, not
a finding against the round.

**`UNVERIFIABLE`, not folded into supported.** That the battery, the three mutations and the
audit runs were performed *immediately before* their commits, as `E3` requires. The figures
reproduce now and the restore digests match the delivered bytes, which is what I can
establish; ordering inside a session leaves no trace I can read.

**Not in this subject.** `transcript_audit` still has no production caller, so that leg's fix
reaches production only when the first enumerated instruction is authored — pre-existing,
already recorded at `v3-review-full-3657687.md:270`, disclosed by the round itself, and
unchanged by this repair. Whether the exempt section should be *declared* rather than inferred
is `O-1`'s question and remains the user's.
