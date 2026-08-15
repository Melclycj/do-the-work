# FULL review — `a5a04c3..ca9c055` (round `V1-CONTEXT-EXACT`, the `V-1` redemption)

| | |
|---|---|
| round | FULL, construction-side (`CONSTRUCTION-CHECKLIST.md` E1–E12 / R1–R10) |
| subject | `a5a04c338decb9c61d0a94338455861f520f5f1b..ca9c055ded32c9332aa3571feed57327bb163860` |
| range content | three commits — one `record` (a returned read), one `record` (its disposition), one `candidate` |
| **verdict** | **`CHANGES_REQUIRED`** |
| findings | 1 blocker, 2 low, 1 observation |
| record | this file; the execution side commits it (`R6`) |

The code is right and the round's ground is real: `_is_context_title` now decides the
exempt heading by equality, the seven real instructions cost nothing, both legs that share
the predicate were closed together, and every figure the commit body reports reproduces at
the tip on this machine.

The blocker is that the round's own thesis does not hold. Its claim — commit body *"the
tests assert the class rather than the instance, which is `E7`"*, test docstring *"the ask
is the class, not whichever instance a finding happened to quote"*, docstring *"the heading
has to **be** the section"* — is measured false in the one direction that matters. The five
hand-written shapes in `NOT_THE_CONTEXT_SECTION` are drawn entirely from the two eras
already behind us. Loosen `_is_context_title` to `startswith("context (non-normative)")` —
the *same* substring→prefix slip that turned f1's repair into `V-1`, applied to the new
literal instead of the old one — and `## Context (non-normative) — the frozen bindings`
carrying a normative frozen table resolves `enumerated` with no notes, both derived
artifacts switch off, and the whole battery is **600 passed**. That is f1's failure mode a
third time, and the sweep written to end the cycle does not see it. §5 `b1`; reproduced in
§2.3; the minimum fix is one row of an existing tuple, verified drop-in in §2.4.

---

## 1. Subject, re-derived (`R2`)

Nothing below is taken from the dispatch prompt, the ledger, the journal or a commit body.

**Round and budget.** `HARNESS-LEDGER.md:34` at the tip carries
`⛔ 断点 = 构造轮 V1-CONTEXT-EXACT 构造完毕、欠 FULL`. `git log` over the range returns
exactly three commits — `562e948 · 288e36f · ca9c055` — linear from the base
(`562e948^ = a5a04c3`), each declaring its kind in the body's first line: `record`,
`record`, `candidate`. No `v3-review-full-*` or `v3-review-verify-*` naming this round
exists under `migration/document-work-assurance-v3/`. So by `E9`'s test — *has a valid
independent FULL already occurred?* — no. This is the round's one FULL; the fix leg is
unspent; a targeted VERIFY is owed if and only if a fix is authorized.

The one record commit inside the range that is a *review* record, `562e948`, is the
returned `E10` read dispatched at the base — not a round, no budget, no verdict (`R3`). Its
landing satisfies `E9`'s concurrency clause exactly: the branch took no commit between the
dispatch and that record, since `562e948`'s parent is the dispatch base itself.

**Authorization, and its ceiling (`R7`).** Three authorizations are load-bearing here.

1. *The `V-1` redemption itself* is visible in the repository: the rider row's own
   `redeem-when` carried **deadline = 任何一份指令被写成编号态之前**, and `R10` makes
   redemption-on-a-touching-batch the normal channel. Fully checkable.
2. *"the user ruled 2026-08-05 that P5B takes that form"* — committed, but only in this
   round's own journal (`journal/v1-context-exact-2026-08-05.md:3`), i.e. written by the
   party it authorizes. I can confirm the text exists and predates nothing; I cannot
   confirm the ruling. **Marked, not verified** (`R4`). See `L-2`.
3. *"Two bookkeeping items ride, on the user's approval"* (`journal` §6 header,
   *搭车，用户 2026-08-05 批准*) — same shape, same ceiling. `UNVERIFIABLE`; not folded
   into supported. It is consistent with two rulings that *are* durably recorded outside
   this round — the 2026-08-03 *ledger 记账批不开轮* and the 2026-08-04 *ledger/riders-only
   finding 修不算 `E9` 的一次修* (`HARNESS-LEDGER.md:59-60`, `:73-76`) — so I have no
   reason to doubt it, and I do not treat it as established.

**Changed paths, classified by hand** (`git diff --name-status a5a04c3 ca9c055`, seven
paths):

| class | count | paths |
|---|---|---|
| resident code | 1 | `tooling/rsclib/document_harness/instruction.py` |
| tests | 2 | `tooling/tests/document_harness/test_instruction_form.py`, `…/test_transcript_audit.py` |
| round record (new) | 1 | `document-harness/journal/v1-context-exact-2026-08-05.md` |
| review record (new) | 1 | `migration/…/v3-checkpoint-read-a5a04c3.md` |
| ledgers | 2 | `HARNESS-LEDGER.md`, `HARNESS-RIDERS.md` |
| schema · contract · instruction-layer member · template · run artifact | **0** | — |

That matches the boundary the candidate commit declares, and it is what makes `E2` and
`E10` decidable below without argument.

**Obligation.** From the redeemed rider's own text (`v3-review-verify-c7fb720.md` `V-1`,
quoted in `HARNESS-RIDERS.md` at the base): replace the prefix match with an exact match on
the section title, at zero cost to the conforming vocabulary. From `E7` and from the
VERIFY's `O-1` — which named the recurrence explicitly, *"the `E7` defect-class ask is met
on one instance rather than on the class — which is the same shape as `V-1`, one level
down"* — the tests must bind the **class**, not the instances a finding quoted. The first
obligation is met. The second is where the blocker sits.

---

## 2. The implementation (`R3` — leads)

### 2.1 The predicate, and that it is the whole surface

`_is_context_title` is `title.casefold() == "context (non-normative)"`
(`instruction.py:187`). It has exactly two callers, and the round closed both:

* `form_conformance:308` — decides whether a block outside every numbered section is
  nonetheless legitimate, and (when it is) whether a normative marker sits inside it;
* `transcript_audit:394-398` — assembles `context_text`, which decides whether a unit
  anchoring text outside every requirement section is `UNJUSTIFIED_CONTEXT` or silently
  legitimate.

I swept for a third leg and there is none: `grep -rniE "startswith\(.context|'context' in|\"context\" in" --include=*.py ResearchSystem/tooling/`
returns only the docstring's own historical quotations. The two-leg claim holds.

**The fix reaches the product path.** `resolve_form` is called at
`assurance/templates/run-v2/check_template_instance.py:214`, and that call is what switches
the preamble gate and the paragraph map off under `enumerated` (`:220-223` vs `:224-237`).
So `form_conformance`'s leg is wired into the run-v2 authoring gate, not merely into tests.

**The behaviour is what the docstring now says.** Probed at the delivered bytes:

```
False   'Context (non-normative) — the frozen bindings'
False   'Context'
True    'Context (non-normative)'
True    'CONTEXT (NON-NORMATIVE)'
False   'Context (non-normative) ##'
```

and on the appendix-carrying document, `resolve_form` → `prose` with
`FORM-BLOCK-OUTSIDE-SECTIONS` naming the offending heading. The docstring's replacement
sentence — *"It is now the rule rather than a claim about one"* — is true of this code, which
is more than either of its two predecessors could say.

### 2.2 The tests, on their own terms

`NOT_THE_CONTEXT_SECTION` (`:52-58`) is a hand-written tuple of five literals, not derived from the
module (`E5`). The sweep asserts three things per shape — exactly one
`FORM-BLOCK-OUTSIDE-SECTIONS`, `repr(heading)` inside it, and `resolve_form` → `FORM_PROSE`
— so no unrelated block can satisfy it; that is a fair reading of `E5`'s *assert the whole
line* even though the middle assertion is technically a containment. The case-tolerance test
is a proper negative control and pins a decision that would otherwise be invisible inside
`casefold`. The `transcript_audit` leg was widened from one heading to two in the same
shape. The `E4` mutations reproduce, scoped to those two modules (38 cases):

| mutation | expected red | measured (two modules) | measured (whole tree) |
|---|---|---|---|
| `.startswith("context")` (the `V-1` shape) | new sweep + audit leg | 2 failed, 36 passed | 2 failed, 598 passed |
| `"context" in title.casefold()` (the f1 shape) | + f1's own test | 3 failed, 35 passed | 3 failed, 597 passed |

Both agree with the journal's table. Restored from a sha256-checked scratchpad copy, never
`git checkout --`; the copy's digest is
`f2dee2480df86432a5e7408916f5dd026738ef1ebbb38e4c0309a271e0db398a`, which equals the
delivered file's — so unlike the `V-4` defect one round back, the recorded mutation evidence
*is* checkable against the delivered bytes. That correction landed without being asked for.

### 2.3 Where it fails — the mutation neither leg was pointed at

Both delivered mutations reproduce **historical** shapes. Neither probes the boundary the
*new* literal creates. I ran that one:

```
_is_context_title  →  return title.casefold().startswith("context (non-normative)")

$ python -m pytest -q                       # whole tree
600 passed in 88.20s

predicate on 'Context (non-normative) — the frozen bindings': True
resolve_form    : ('enumerated', ())
form_conformance: ()
```

on this document:

```markdown
---
form: enumerated
---
# Work order

## R1 Do the thing
Do the thing.

## Context (non-normative) — the frozen bindings
Every row above is frozen; a shell that deviates from a key here is a defect.

## Context (non-normative)
Background only.
```

A normative frozen table passes as non-normative; the paragraph map and the preamble gate
switch off; `resolve_form` returns `enumerated` with **no notes at all**. That is f1's and
`V-1`'s failure mode reproduced verbatim, a third time, one word later again — and the
regression battery is entirely green. The guard does not bind the class. `R8`: the two
delivered mutations prove the tests touch the code; they do not prove the tests bind the
behaviour the docstring now claims.

The shape is not outside the set's own scope. `NOT_THE_CONTEXT_SECTION`'s comment declares
it as *"Headings that mention or open with the word but are not the Context section"* — the
missing heading opens with the word (with the whole exempt title, in fact) and is not the
section. It belongs to the declared set and is simply absent from it.

A second, adjacent shape is also unpinned and behaves correctly today: bare `## Context`
was exempt through both earlier eras and is refused now. That change of behaviour is
recorded nowhere and asserted nowhere. It is fail-safe, so I do not make it part of the
minimum fix — but the executor closing `b1` is touching the exact tuple where it belongs.

### 2.4 The minimum fix, verified drop-in

Adding the shape costs one row and no machinery (`E6`). Verified against the **delivered**
code, so the executor need not discover it:

```
heading = "Context (non-normative) — the frozen bindings"
form leg  : len(outside)==1 · repr(heading) in outside[0] · resolve_form → prose · no other issue
audit leg : result == "SPEC_GAP" · ['audit-outside-unit-appendix'] · ['UNJUSTIFIED_CONTEXT']
```

Both existing assertions pass unchanged. Under the §2.3 mutation both go red, which is the
property the round is short of.

---

## 3. Measurements re-derived (`E3`, `R2` — no reported figure accepted)

Every leg re-run at the tip on this machine, worktree clean before and after:

| claim | command | measured |
|---|---|---|
| pytest 600 passed | `python -m pytest -q` (in `ResearchSystem/tooling`) | **600 passed in 86.08s** |
| P2 29/29 | `python tests/run_tests.py` | **tests: 29 passed: 29 failed: 0** |
| P4 80/80 | `python tests/run_p4_tests.py` | **tests: 80 passed: 80 failed: 0** |
| P5A 32/32 | `python tests/run_p5a_tests.py` | **tests: 32 passed: 32 failed: 0** |
| N0 contract fixtures 41/41 | `python migration/…/N0/fixtures/validate_fixtures.py` | **41/41 cases behaved as declared; failures=0** |
| `compile --check` 0/0 | `python ResearchSystem/tooling/rsc.py compile --check` | **0 error(s), 0 warning(s)**, `RESULT: … exit 0` |
| seven real instructions, all identical | `grep -rniE '^#{1,6}[[:space:]]*.*context' ResearchSystem/assurance/runs/*/instruction.md` | **7 hits in 7 files, all `## Context (non-normative)`** — and `cat -A` confirms no trailing whitespace on any of the seven |
| 598 → 600 derivable from two added methods | `git diff` on the two test modules | **+2 `def test_` in `test_instruction_form.py`, +0 in `test_transcript_audit.py`** — derivable as claimed |
| restore digest | `sha256sum` on delivered file and scratchpad copy | **`f2dee248…` on both** |
| ledger under cap | `wc -l` + `hooks/ledger_cap_check.py` | **119 lines**, exit 0 |
| three tracked checks exit 0 | `ledger_cap_check` · `layer_path_check` · `review_freeze_check` | **0 · 0 · 0** |

The one figure that does not reconcile on its face is the mutation table's — see `L-1`. It
is a labelling gap, not a wrong number: 36+2 = 35+3 = 38 = the two modules, which I
reproduced.

---

## 4. Process and record boundary (`R3` — second)

**`E2`.** Zero paths under `ResearchSystem/schema/` in the range; none of the four frozen
blobs touched; the pack still holds **15 files**, the 2026-08-03 re-baseline count. No
ruling was needed and none was claimed.

**`E10`.** No layer member appears in the range. I re-derived the member set from `E10`'s
own sentence rather than from any table, and computed each member's blob at both ends:

| # | blob at `a5a04c3` | blob at `ca9c055` | member |
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

Nine against nine, all unchanged across the range, and every one equal to the blob the
cited read (`562e948`) records for it. So the opening-read discharge-by-citation is valid
on its own terms, not merely asserted — and since that read returned **0 must-fix**
(`v3-checkpoint-read-a5a04c3.md:9`), no amendment-plus-re-read pair was owed before the
round could rely on the layer text.

**`E8`.** Titles `V3-V1-CONTEXT-EXACT-v1` / `V3-V1-CONTEXT-EXACT-READ-DISPOSITION-v1` /
`V3-REVIEW-RECORD-SIMP-ABCD-AMENDMENT-READ-a5a04c3-v1` — the round is named, the review
record follows `R6`'s form. One dense paragraph each, **no trailers**. Author date equals
committer date on all three, so nothing was amended or rebased. `origin/main..HEAD` is 485,
so nothing was pushed. Nothing outside the declared boundary appears, and the worktree is
clean at the tip.

**`E9`.** Accounted above: this is the FULL, the fix leg is unspent. Neither record commit
consumes budget — `562e948` is a returned read, `288e36f` touches only the two ledgers, and
the 2026-08-04 ruling (`HARNESS-LEDGER.md:73-76`) settles that ledger/riders-only edits are
not the round's one approved fix. I note without objecting that the round chose to carry the
SIMP-ABCD leftovers in the candidate commit rather than a separate one; the boundary the
commit declares covers them, and the 2026-08-03 ruling makes them open no round.

**`R10`.** The `V-1` row is deleted in `ca9c055` — the same commit as the fix, as the rule
requires. Four rows were added: `chk-thin` and `HI-route` in `288e36f` (from the read's two
lows), `ctx-ground` and `mark-case` in `ca9c055` (from the VERIFY's `O-2`/`O-4`). Every row
names a target file or clause, not merely *对应文件*, and carries a redeem-when. Routing of
the read's lows follows the 2026-07-29 ruling correctly: both are middle findings whose
record deliberately supplies no bytes, so the bank takes them and `E10`'s free channel does
not. The dispositions of `O-3` and `O-5` to `R9` are sound — I checked `O-5`'s substance
independently: the sentence at `EXECUTION.md:154-155` is indeed the end of the amendment's
new section, and the file's true last section is *What you are never asked to do*, so the
correction is right and the decision not to touch a layer member for it is right.

`ctx-ground` is the only row I would flag for form: its redeem-when opens with a moment
(*第一份编号态指令落地时*) but does not label it **deadline**, where the sibling `mark-case`
does. The moment is present, so this is a labelling nit and not a finding.

---

## 5. Findings

### Blocker

**`b1` — the class sweep binds the two eras behind it and not the boundary the new literal
creates; the round's `E7` claim is measured false.**

*Location.* `tooling/tests/document_harness/test_instruction_form.py:52-58`
(`NOT_THE_CONTEXT_SECTION`), consumed at `:146-173`; and the mirrored heading list in
`tooling/tests/document_harness/test_transcript_audit.py:137-140`.

*Ground truth violated.* `E7` (*test the defect class, not the reported instance*) and
`E4`/`R8` (*never trust a guard you have not seen fail*; the mutation must reproduce the
real defect shape). The round asserts it satisfies `E7` in three places — commit body,
journal §2's heading, and the sweep's own docstring — and the VERIFY finding it answers
(`O-1`) named this exact recurrence one level down.

*Measured.* With `_is_context_title` loosened to
`title.casefold().startswith("context (non-normative)")` — the identical substring→prefix
slip that produced `V-1` from f1, applied to the new literal — `python -m pytest -q` returns
**600 passed**, and `## Context (non-normative) — the frozen bindings` over a normative
frozen table gives `resolve_form` = `('enumerated', ())` and `form_conformance` = `()`. Full
reproduction in §2.3.

*Minimum fix.* Add one row to `NOT_THE_CONTEXT_SECTION` —
`("Context (non-normative) — the frozen bindings", "the new literal's own boundary: opens with the whole exempt title")`
— and add the same heading to `test_transcript_audit.py`'s loop. Then re-run the §2.3
mutation and record that both go red. Verified drop-in against the delivered code in §2.4:
no assertion changes, no new machinery, nothing else moves.

*Not asked for.* I am not asking for bare `## Context` to be pinned, nor for whitespace
variants, nor for any generalization of the tuple. One row is what closes the measured hole.

### Low

**`L-1` — the mutation counts are reported without the scope that makes them
reconcilable.** `journal/v1-context-exact-2026-08-05.md:54-55` gives *2 failed, 36 passed*
and *3 failed, 35 passed*; §4 of the same file gives the battery as *600 passed*. Nothing
states that the mutation runs were scoped to the two touched modules (38 cases), so a reader
comparing the two sections cannot tell whether 562 tests vanished or the scope changed, and
a later reader re-running the claim does not know which command to run. `E3` requires the
count to be emitted from the command that produces it; the command is what is missing.
Named downstream decision: the next executor re-verifying `V-1`'s closure reproduces the
wrong scope and reads a mismatch as a regression. *Bytes:* on §3's heading line, append the
scope — e.g. `（跑的是两个模块共 38 例：test_instruction_form.py + test_transcript_audit.py）`.

**`L-2` — the ruling that P5B takes the enumerated form is not in the pointer that a cold
session reads.** The base ledger's breakpoint block said P5B *may* go either way
(*走散文态则不受限，但本轮收益不落地*). `288e36f` removed that block, and the replacement at
`HARNESS-LEDGER.md:34-36` records the redemption but not the ruling that made it a
precondition — it says only *之后 **P5B 批次 → HarnessIssue f6/f7 → P5C***. So the ledger
went from stating the choice to stating nothing about it, while the ruling itself lives
only in this round's journal. Named downstream decision: a session opening P5B from the
ledger — which `CLAUDE.md` makes the cold-start entry and which calls itself the live
pointer — has no signal that P5B is to be authored in enumerated form, writes it in prose,
and this round's benefit does not land. It is recoverable by following the journal link on
the same line, which is why this is low and not a blocker. *Bytes:* `之后 **P5B 批次（用户
2026-08-05 裁：走编号态）→ HarnessIssue f6/f7 → P5C**。`

### Observation (`R5` — reported; the conclusion is the user's)

**`O-1` — three consecutive rounds have now been spent on one string predicate, and the
module rejects this pattern one function above it.** f1 → `V-1` → this round have each
repaired `_is_context_title` by quoting the shape a finding produced, and each repair has
been measured false of its own docstring by the next reader. Meanwhile `declared_form`'s
docstring, twenty lines up, records the opposite design choice for the *form*: *"the
instruction declares its own shape rather than having one inferred. The rejected alternative
was to have a model read the file and judge."* The Context section's non-normative status is
still inferred — from a heading string, by a predicate with no declaration behind it and no
test tying it to any real instruction (that tie is the freshly banked `ctx-ground`). Whether
the exempt section should be declared rather than inferred — and whether the recurrence is
telling you the predicate is the wrong instrument — is a design question, and `R5` puts both
the question and the conclusion with you, not with me. I report only that the shape is now
three deep and that closing `b1` will not, by itself, end it.

---

## 6. Coverage disclosure (`R4`)

**Read in full:** the range diff (all seven paths, both directions); `instruction.py` end to
end (696 lines); both changed test modules end to end; `journal/v1-context-exact-2026-08-05.md`;
`HARNESS-LEDGER.md`; the `HARNESS-RIDERS.md` diff; `CONSTRUCTION-CHECKLIST.md` (standing
instructions); `hooks/review_freeze_check.py`.

**Read in part:** `v3-checkpoint-read-a5a04c3.md` (§1 member table, §5 findings, tier
line); `v3-review-verify-c7fb720.md` §4; `run-v2/README.md` §§ on the enumerated form and
battery tiering; `check_template_instance.py:185-241`; `EXECUTION.md:145-160` and its tail.

**Probed only:** the rest of `EXECUTION.md` / `REVIEW.md` / the two supersessions — I
verified their blobs, not their contents, because no layer member is in the subject and
`REVIEW.md` governs product runs, not this round.

**Commands run live at the tip:** the eleven rows of §3; three mutations of
`_is_context_title` (prefix, substring, prefix-of-full-title), each restored from a
sha256-verified scratchpad copy, never `git checkout --`, with `git status --porcelain`
empty and the digest re-checked after the last restore; four direct probes of
`form_conformance` / `resolve_form` / `transcript_audit` on hand-built documents, including
the two that verify the proposed fix.

**Marked, not verified (`R4`).** The two user approvals in §1 — that P5B takes the
enumerated form, and that the SIMP-ABCD bookkeeping could ride — exist in the repository
only as this round's own prose. That is a ceiling on this review, not a finding against the
round; `R7` says state it and move on.

**`UNVERIFIABLE`, not folded into supported.** That the mutation runs, the grep and the
battery were performed *immediately before* the commit, as `E3` requires — I can confirm the
figures reproduce now and that the restore digest matches the delivered bytes, which is
strictly more than the last round could show, but ordering inside a session leaves no trace
I can read.

**Not in this subject.** `transcript_audit` still has no production caller — the four
existing `write_audit.py` scripts predate the enumerated form and none imports it, so that
leg's fix reaches production only when the first enumerated run is authored. This is
pre-existing, already recorded at `v3-review-full-3657687.md:270`, and openly disclosed by
the round itself (journal §7). I record it as scope, not as a finding.
