# Targeted VERIFY — `83e32c3..c7fb720` (round `SIMP-ABCD`, the harness simplification round)

| | |
|---|---|
| round | targeted VERIFY, construction-side (`CONSTRUCTION-CHECKLIST.md` R1–R10) |
| subject | `83e32c32e356c3484b384e7383d96f38715b8444..c7fb720811b7fe01856ecab36e470a21c42c3513` |
| range content | one commit, kind `review fix` |
| **verdict** | **`REVIEWED_NO_BLOCKER`** |
| findings | 0 blockers · 1 finding carrying a deadline · 3 low · 5 observations |
| budget after this record | **exhausted** — one FULL (`83e32c3`), one fix (`c7fb720`), this VERIFY |
| record | this file; the execution side commits it (`R6`) |

The blocker **as named is closed**, and closed by the literal the FULL specified. Both legs
bind under my own mutation, at the delivered bytes, and neither test is a crash-detector:
reverting `_is_context_title` returns `form_conformance` to `()` and `transcript_audit` to
`COVERED`, which is the real defect shape.

What does not hold is the blocker's **class**. `startswith("context")` still exempts any
heading that *begins* with the word, and on such a heading the entire f1 failure mode
reproduces end to end at the tip — `enumerated` with **no notes**, `COVERED`, paragraph map
and preamble gate switched off. I measured that closing it completely costs nothing: an
exact match leaves all 598 tests green. That is `V-1`, it carries the same deadline the
blocker did, and the decision is the user's (`R5`).

`REVIEWED_NO_BLOCKER` here means the repair is sound and inside its authorization. It does
not mean the class is closed, and §2 is written so the two cannot be read as one.

---

## 1. Subject re-derivation (`R2` — every figure below is mine, none accepted)

| check | result |
|---|---|
| range resolves | `83e32c32e356c3484b384e7383d96f38715b8444..c7fb720811b7fe01856ecab36e470a21c42c3513` |
| range content | `git log --oneline` → exactly **1** commit, `c7fb720 V3-SIMP-ABCD-FIX-v1` |
| linear | `git log --merges` over the range: empty |
| HEAD == tip | `git rev-parse HEAD` = `c7fb720811b7fe01856ecab36e470a21c42c3513`, branch `document-work-assurance-v3` |
| worktree | `git status --porcelain` empty, before and after my mutations |
| not pushed | `git branch -r` → `origin/HEAD`, `origin/main` only; no remote for this branch |
| changed paths, classified by hand | **4** — resident code 1 (`instruction.py`), tests 2 (`test_instruction_form.py`, `test_transcript_audit.py`), record 1 (`journal/simp-abcd-2026-08-05.md`). No schema, no contract, no instruction-layer member, no template, no ledger |

**Which round this is, derived.** The range base `83e32c3` is itself a committed review
record, `V3-REVIEW-RECORD-SIMP-ABCD-3657687-v1`, whose subject is `31e291e..3657687` and
whose verdict is `CHANGES_REQUIRED`. The one commit in the range names its own kind as the
round's one review fix. Under `E9`'s discriminator — *has a valid independent FULL already
occurred?* — **yes**, so `c7fb720` is the fix and it obliges this VERIFY. No
`v3-review-verify-*` naming this round exists under `migration/document-work-assurance-v3/`.
Budget after this record: spent in full.

**Freeze window.** `.harness/review-pending.json` names this exact range,
`dispatched_at 2026-08-05T11:10:00+00:00`; `git log --since` that instant returns empty, so
the branch took no commit between dispatch and this read and this record is the only commit
the window admits. (`.harness/` is `.gitignore`d — line 19 — so the full tip SHA written
there is a dispatch marker, not a range recorded in a file, and `E12`'s written-tip
prohibition does not reach it.)

**Authorization, and its ceiling (`R7`).** The fix's own boundary — f1, f3, f4, f5, f6, O-2,
plus f2 on a later ruling — is asserted in the commit body and nowhere else I can read. What
*is* in the repository is the f2 ruling itself, written into
`journal/simp-abcd-2026-08-05.md` §1 item 4 by this very commit, dated 2026-08-05, with its
reasoning and the user's correction of the finding's shape. The three pre-round rulings sit
in the same section, committed before the round's base. **Ceiling:** I can confirm every
touched byte falls inside the FULL's finding IDs, and I can read the f2 ruling as committed
text; I cannot witness the approval conversation that set the fix boundary. Stated, not
treated as a block.

**Permanent boundaries — intact.**

- **`E2`.** The four frozen blobs are byte-identical at base and tip: `8ad404b1…`
  (`.goals/plans/document-work-assurance-harness-v3.plan.md`), `b2dbdf75…` (contract),
  `68031fa2…` (supersession-1), `e1a2f26b…` (supersession-2), each re-derived with
  `git ls-tree -r`. The schema pack is **15 files**, and every one of the fifteen has the
  same blob id at `83e32c3` and at `c7fb720`. The repair writes nothing under
  `ResearchSystem/schema/` or `ResearchSystem/contract/`.
- **`E10`.** None of the nine instruction-layer members appears in the repair diff. I
  re-derived all nine at base and tip: six unchanged across the whole round, three
  (`README.md`, `EXECUTION.md`, `REVIEW.md`) moved earlier in the round and not by this
  commit.
- **`E8`.** One commit, no merge, no amend inside the range, no trailers, single dense title
  naming the round (`V3-SIMP-ABCD-FIX-v1`), one dense paragraph, kind declared in the first
  line (`Kind: review fix`). No path appears that the body does not claim. I cannot witness
  `add -A` versus explicit paths, only that nothing stray landed.
- **`E12`.** The handoff was one range and nothing else; I reproduced the finding before
  judging the fix rather than adjudicating the FULL.

---

## 2. Did the repair close what was accepted (`R3` — implementation first)

### f1 — the blocker. Both legs bind; the class does not close.

**Leg 1, `form_conformance`.** `_is_context_title` (`instruction.py:156-171`) replaces the
substring test at the old `:267`. The reported instance is refused, and so is the real
p5a-shells heading:

```
REFUSED  form=prose       ## Appendix A - the frozen context bindings
REFUSED  form=prose       ## Appendix §A - wa: the 26 frozen bindings
REFUSED  form=prose       ## Additional context
```

**Leg 2, `transcript_audit`.** A unit anchoring text in neither a numbered section nor a
Context section is now `UNJUSTIFIED_CONTEXT` (`:405-419`). Probed against the resident
module, no fixtures:

| shape | result |
|---|---|
| context unit anchoring top-level Context prose | `COVERED` — no false positive |
| context unit anchoring a **nested** `###` subsection inside Context | `COVERED` — no false positive |
| context unit anchoring `## Appendix A - frozen bindings` | `SPEC_GAP` / `UNJUSTIFIED_CONTEXT` |
| unit anchoring the document title `# Work order` | `SPEC_GAP` / `UNJUSTIFIED_CONTEXT` |

**Mutation at the delivered bytes (`R8`, `E4`).** Baseline `instruction.py` sha256
`ce2a359e842d8dd864b02147a2ae0d3d0dcf69c2ef0ce24cecdddbbff0387520`, copied to a scratchpad,
restored from it after every mutation and re-hashed to the same digest; `git status` clean
after each. Never `git checkout --`.

| # | mutation | expected | actual |
|---|---|---|---|
| M1 | `_is_context_title` reverted to `"context" in title.casefold()` | both new tests red, nothing else | **2 failed, 596 passed** — exactly `test_a_heading_that_merely_mentions_context_is_not_the_context_section` (`AssertionError: False is not true : ()`) and `test_a_unit_anchored_outside_both_kinds_of_section_is_refused` (`'COVERED' != 'SPEC_GAP'`) |
| M2 | the `elif not any(anchor in text …)` branch neutered to `elif False:` — leg 2 alone | only the transcript test red | **1 failed, 220 passed** (`document_harness` subset), the audit test only; leg 1's test stays green, so the two tests are separable and neither is carrying the other |
| M3 | `_is_context_title` tightened all the way to `title.casefold() == "context (non-normative)"` | if the `startswith` looseness is pinned anywhere, red | **598 passed** — nothing pins it in either direction |

M1's failure *messages* are the point: the assertions fail on the real defect values (`()`
and `COVERED`), not on an exception, so the tests bind the behaviour rather than merely
touching the code. Both are paired with controls that already existed or were added with
them — `test_the_real_context_heading_still_passes` and
`TheConformingTranscript::test_a_context_unit_outside_the_sections_is_legitimate` — and
every expectation is a hand-written literal (`FORM-BLOCK-OUTSIDE-SECTIONS`,
`UNJUSTIFIED_CONTEXT`, the exact finding-id list `["audit-outside-unit-appendix"]`) over
test-local fixture text, never a module constant (`E5`). Two additions, not repairs, which
is what the FULL's own M1 predicted.

### `V-1` — the class the blocker named is narrowed, not closed. Carries a deadline.

`startswith("context")` matches a prefix, not the section. Measured at the tip:

```
EXEMPT   form=enumerated   ## Contextual appendix - the frozen bindings
EXEMPT   form=enumerated   ## Context bindings for the frozen shells
EXEMPT   form=enumerated   ## CONTEXTUALISED requirements addendum
```

Composed end to end on `## Contextual appendix — the frozen bindings` carrying a frozen
table plus *"Every row above is frozen; a shell that deviates from a key here is a defect"*:

```
resolve_form    : enumerated   notes=()
transcript_audit: COVERED      findings=0
authoring gate  : preamble gate + paragraph map SKIPPED
```

That is f1's failure mode verbatim, one word of the heading later. Three things make it a
finding rather than a nitpick:

1. `_is_context_title`'s own docstring (`:167-169`) says *"anything else falls to the prose
   form, which is the direction `resolve_form` promises for whatever it cannot decide."*
   Measured false. `form_conformance`'s docstring likewise still claims prose lives inside a
   numbered section or Context *"and nothing else"*; the lint still establishes something
   weaker. This is the `E3` assertion class, in delivered code text.
2. The round's justification for deleting the paragraph map and the preamble gate is that
   the structural property holds without them. On this heading shape it does not, and there
   is no leg left below FULL review.
3. **M3 measured the cost of closing it: zero.** An exact match leaves 598/598 green, and I
   independently confirmed the ground the fix rests on — all **seven** real instructions
   head the section exactly `## Context (non-normative)`
   (`grep -rn '^#\{1,6\}.*[Cc]ontext' ResearchSystem/assurance/runs/*/instruction.md` → 7
   hits, all identical). So the conforming vocabulary loses nothing from the tighter form
   either.

**Honest narrowing, stated because inflating a finding burns something.** The marker
backstop is unchanged and still fires under the exempt heading: `MUST` and `必须` inside it
raise `FORM-NORMATIVE-IN-CONTEXT`. What `V-1` exposes is *unmarked* normative prose under a
`context`-prefixed heading — the same class as the blocker, at materially narrower reach.
Its deadline is the blocker's: the first enumerated-form instruction, which
`HARNESS-LEDGER.md` names as the next item (the P5B batch).

**Why this is not the standing blocker.** The blocker as written was *"exempts any section
whose heading merely contains 'context'"*, and that sentence is now false of the code. The
executor applied precisely the literal the FULL named as its minimum fix. `V-1` is the gap
between that literal and the sentence it illustrated (*"Match the Context section rather
than search for the word"*) — a shortfall of the prescription, not a deviation from it.
Whether to spend a fresh round on it is the user's call (`R5`); the bytes are one line.

### f2, f3, f4, f5, f6, O-2 — all paid, each checked against ground truth, not against the claim

| id | what was owed | verified |
|---|---|---|
| f2 | record the §6 divergence and the ruling that settles it | module docstring (`:6-16`) now describes **both** forms and names the 2026-08-05 ruling with its ground; `check_audit` (`:531-538`) states the name comparison is satisfied by construction under the enumerated form and **that its passing is not evidence** — the vacuity is disclosed rather than papered over; the ruling itself is now in the journal §1 item 4. Prose form untouched |
| f3 | correct the journal's account of rider `PD` | `HARNESS-RIDERS.md` line 14 reads redeem-when *"I/O design 批一起议，或下一个碰 `E2` 冻结面的批，孰先"* — two clauses, exactly as the FULL said. The journal now reads **触发点火、用户裁决不兑**. Accurate; the row is correctly left unredeemed rather than smuggled into a fix leg |
| f4 | record `SIMP-A4`'s disposition | journal §3 now carries it. The quoted `EXECUTION.md` sentence exists verbatim at `EXECUTION.md:154-155`, and `git log -S` confirms it entered this round at `6f850db` |
| f5 | state that `COVERED` must omit the `findings` key | `transcript_audit` docstring `:358-360`. Checked against the schema: `findings` carries `minItems: 1` **and** `allOf` case 2 is `if result == COVERED then not required [findings]` — refused twice over, exactly as stated |
| f6 | four-vs-five defect classes | docstring `:344` now says five and the bullet list enumerates five; the code emits five distinct `auditFindingKind` values (`UNJUSTIFIED_CONTEXT` from two sites). Test class renamed `TheFourDefectClasses` → `TheDefectClasses` |
| O-2 | put the opening `E10` read citation somewhere readable | journal §3 now records it. **I re-derived the claim rather than accepting it:** all nine members' blobs at the round base `31e291e` are identical to the `v3-checkpoint-read-838c413.md` §1 table — `4d0c7330 · f3a31208 · bd490c8b · c19d8cb9 · 17ff31bb · 52a97a48 · 68031fa2 · e1a2f26b · 09aa8699`. The citation holds on the facts and is now readable |

**Boundary.** Every hunk in the diff maps to one of these IDs. Nothing outside them is
touched: no schema, no contract, no instruction-layer member, no template, no ledger, no
other resident module.

---

## 3. Baselines, re-run immediately before this record (`E3`)

Every figure is mine, from a clean restored worktree at `c7fb720`.

| suite | command | result |
|---|---|---|
| pytest, whole tree | `python -X utf8 -m pytest ResearchSystem/tooling/tests -q` | **598 passed** in 93.24s |
| P2 golden | `tests/run_tests.py` | tests 29, passed 29, failed 0 — `RESULT: OK` |
| P4 golden | `tests/run_p4_tests.py` | tests 80, passed 80, failed 0 — `RESULT: OK` |
| P5A | `tests/run_p5a_tests.py` | tests 32, passed 32, failed 0 — `RESULT: OK` |
| contract fixtures | `N0/fixtures/validate_fixtures.py` | `41/41 cases behaved as declared; failures=0` |
| compiler | `rsc.py compile --check` | `0 error(s), 0 warning(s)`, `generated output fresh; lint clean (exit 0)` |

595 → 598 is derivable rather than accepted: the repair adds exactly three test methods
(two in `test_instruction_form.py`, one in `test_transcript_audit.py`) and the FULL's own
re-derived baseline was 595. The pre-fix `instruction.py` blob hashes
`0d096044da02c80cf367d5519df066cbdeaf707f014c8bec7a5036481262fb89`, matching the digest the
FULL independently derived — the two review sessions agree on the baseline without either
taking it from the other.

---

## 4. Findings

### Finding, non-blocking, carries a deadline

**`V-1`** — §2. The blocker's class is narrowed, not closed; bytes are one line; cost of
closing measured at zero; deadline is the first enumerated-form instruction.

### Low

**`V-2` — `HARNESS-LEDGER.md:30` is stale at the dispatched tip, and stale in the one
direction `E9` warns about.** The single line naming this round reads
*"⛔ 断点 = 轮 `SIMP-ABCD` 构造完毕、欠 FULL（四提交，base `31e291e`、tip `HEAD`…）"*. At
`c7fb720` the FULL has occurred (`83e32c3`, `CHANGES_REQUIRED`), the one user-approved fix
has landed, and `git rev-list --count 31e291e..HEAD` is **6**, not four. No other line in
the file mentions the round. Named downstream decision: `CLAUDE.md` makes this file the
cold-start entry point and calls the whole file the live pointer, so a fresh session
resuming from it would conclude a FULL is owed and the fix leg unspent — which is exactly
the misattribution `E9` closes with *"Never self-classify which round consumed what: every
recorded escape from the cap was a renamed round."* In fairness: `E9`'s freeze window
forbade a ledger commit while the FULL was out, and precedent (`f8d17ee`, `e061e18`,
`e66caca`) advances the pointer in a separate `chore(ledger)` commit — so this may simply be
held for closeout. It is reported because at the dispatched tip the durable record is wrong,
and I cannot see an intention. Bytes: the state clause and the commit count.

**`V-3` — the round journal contradicts itself on the round's size.**
`journal/simp-abcd-2026-08-05.md:5` still reads *"范围 `31e291e..HEAD`，四个提交"* while §3's
table in the same file now lists **five** commit rows — the fifth added by this very commit
— and git reports six. Bytes: `四个提交` → the true count, or drop the count and keep the
range.

**`V-4` — the commit body's `E4` restore digest matches nothing that was delivered
(`UNVERIFIABLE`, `R4`).** The body records the scratchpad copy as sha256
`596c1ddf650f3a7d25a37b649d56cef0c839970120a50007dcc0c6bab58f85c4`. Measured: the delivered
`instruction.py` is `ce2a359e…` at the tip and `0d096044…` at the base, and neither matches
under LF or CRLF (`a9c0fc25…` / `7ea2fdbc…`); neither test file matches either. So the
mutated-and-restored file was an intermediate working state that changed before the commit,
and the mutation evidence as written cannot be checked against the delivered bytes — `E3`'s
*measure last*, since a figure is invalidated by any later change to what it measures. This
is a record defect, not a substance one: M1 and M2 in §2 supply, at the delivered bytes, the
evidence the sentence was reaching for, and they agree with its conclusion. Bytes: re-run
the mutation at the committed file and record that digest, or mark the recorded one as
pre-final.

### Observations (`R5` — reported; the conclusions are the user's)

**`O-1`** — the FULL's minimum fix asked for a test pinning `## Additional context` *or*
`## Appendix … context …`. The delivered test pins the appendix instance. `## Additional
context` is behaviourally refused (measured, §2) but pinned by nothing, so the `E7`
defect-class ask is met on one instance rather than on the class — which is the same shape
as `V-1`, one level down.

**`O-2`** — *"All seven real instructions head the section exactly `## Context
(non-normative)`"* is the ground both the fix and its negative control rest on. I measured
it true. No test binds it: the control asserts against the test file's own `CONFORMING`
fixture, not against `assurance/runs/*/instruction.md`. A future instruction heading its
Context section differently fails safe — it falls to prose and owes the derived artifacts —
but silently, and the docstring's claim would quietly stop being true.

**`O-3`** — `check_audit`'s new *"satisfied by construction"* is by **convention**, not by
mechanism: `audited_by` is written by each run's own `write_audit.py`, and the run-v2 README
(`:148`) prescribes naming the mechanism rather than enforcing it. An executor writing its
own name there would make the guard fire. The direction is fail-safe (a violation stops the
run), so no decision goes wrong; the phrase is stronger than the mechanism.

**`O-4`** — `_NORMATIVE_MARKERS` (`:142`) remains case-sensitive: measured at the tip, `MUST`
and `必须` inside an exempt section raise `FORM-NORMATIVE-IN-CONTEXT`, lower-case `must` does
not. The FULL disclosed this as its residual (3); this repair neither widened nor narrowed
it. Noted so the record does not read as if it were closed.

**`O-5`** — both the FULL and the journal call the `SIMP-A4` sentence *"EXECUTION.md's
closing sentence"*. It is the closing sentence of the section that added it
(`EXECUTION.md:154-155`); the file closes with *"What you are never asked to do"*. Verbatim
quote, imprecise pointer. `R9` wording-level: no actor's action changes and the accurate
fact is one `grep` away, so it rides the next batch touching either file and spawns nothing.

---

## 5. Coverage disclosure (`R4`)

**Read in full:** `CONSTRUCTION-CHECKLIST.md` (173, as standing instructions) and the
review-contract stub that points to it; `v3-review-full-3657687.md` (358) — the accepted
findings are its text, not the commit body's summary of them; `instruction.py` at the tip
(whole file, 680 lines by `wc -l`, not the diff); the entire repair diff, all four paths; the round
journal `simp-abcd-2026-08-05.md`; the fix commit body; `HARNESS-RIDERS.md` line 14;
`HARNESS-LEDGER.md` (107) around the round pointer; `instruction-coverage-audit.schema.json`;
`check_template_instance.py`'s form branch (`:214-240`); both repair-touched test files'
fixtures and headers.

**Re-executed:** the full battery (pytest, P2, P4, P5A, contract fixtures,
`rsc compile --check`); three mutations with sha256-checked scratchpad restore; seven
synthetic `form_conformance` heading probes; six `transcript_audit` probes; one composed
end-to-end probe across `resolve_form` → `transcript_audit` → gate branch; four
normative-marker probes; the nine-member `E10` blob table at three revisions; the seven real
instructions' Context headings; the four `E2` blobs and all fifteen pack members at base and
tip.

**Sampled:** `v3-checkpoint-read-838c413.md` §1 (the blob table `O-2` cites);
`REVIEW.md` §"The two rounds" and §"When the map is incomplete" for the verdict semantics;
`run-v2/README.md:138-160` for the `audited_by` prescription; `EXECUTION.md:145-162`.

**Only probed:** the rest of the resident package (`checks.py`, `views.py`, `spec.py`,
`flow.py`, `enumerations.py`) — reached only through the suite, untouched by this repair;
the four candidate commits of the round — the FULL's subject, not mine, and not re-certified
here.

**Not verified:** that any part of this repair ran in a fresh context — a process claim,
marked, not verified (`R4`). That the executor's own mutation happened as described — see
`V-4`; my M1/M2 establish the property independently, but a mutation is not witnessable
after restore, and here the digest does not even identify the artifact it covered. The
conversation that set the fix boundary and the f2 ruling — outside the repository (`R7`).

**`residual_uncertainty`:**

1. `V-1` — the blocker's class is open at a measured zero cost to close, with the same
   deadline the blocker carried. Nothing below FULL review catches the exempt shape.
2. The enumerated form still has **no real instruction** behind it. Every claim about it,
   the FULL's, the executor's and mine, rests on synthetic shapes; the first real
   enumerated-form run is also the first test of `V-1`, `O-2` and `O-4` at once.
3. A VERIFY is not a re-certification (`R4`). The FULL's verdict on the four candidate
   commits stands on its own record; I re-derived only the permanent boundaries and what
   the repair could have disturbed.
