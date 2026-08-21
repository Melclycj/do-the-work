# FULL review — round `PREVIEW-RENDER` at `57d1312`

**Verdict: `CHANGES_REQUIRED`.** 2 blockers, 4 low, 5 observations.

Both blockers are in the same new module and both have the same shape: `preview.py` renders
the START approval surface **narrower than the plane it claims to render**, silently, with
`coherent` still True and `dtw preview` still exiting 0. `B-1` bites on all eight committed
real planes today — the change boundary renders as the literal string `out, write_scope`,
dropping between 14 and 91 paths. `B-2` is the Context elision swallowing a numbered
section whole, which no real instruction currently triggers but which the harness's own
form gates accept without a word.

Neither is a design objection. The round buys what its ruling asked for: the render is
deterministic, LLM-free, re-derived rather than stored, and it drives off the plane's own
bytes. What it does not yet do is put *all* of those bytes in front of the user.

---

## 1. Subject, round and budget — re-derived, nothing taken from the dispatch

The dispatch handed one range and nothing else. Everything below comes from the repository.

**Subject.** `dd22789ef34c615f17e64f2df3b38301bc328896..57d13127ca60e66661c03f22458b6877b45b76f6`,
two commits. `57d1312` is `HEAD`; the worktree was clean at the start of this review and
clean at its end (`git status --short` → empty, run twice).

| commit | title | kind (named in its own body) |
|---|---|---|
| `c7c9081` | `V3-REVIEW-RECORD-PREVIEW-RENDER-dd22789-v1` | record — the round's opening cold read of the instruction layer |
| `57d1312` | `V3-PREVIEW-RENDER-v1` | candidate |

**Round.** `PREVIEW-RENDER`. Named as the queue head by `dd22789`
(`V3-E11-RULING-QUEUEHEAD-v1`, the range's base), which records the user's 2026-08-21
ruling 「脚本化要做」 and its scope: *a deterministic, LLM-free render of the pre-START
human-readable preview from a run's frozen control plane (instruction, WorkSpec, check
spec), re-derivable on demand so its output is not stored*. The same entry delegates one
sub-question to this round — 「加不加第八命令按 `HD-47` 判据由该轮裁」 — and `HD-47`
(`HARNESS-DECISIONS.md:157-179`, status `implemented`) routes it per-case to the user
under `R5`. That delegated answer is `L-3` below.

**Budget (`E9`).** The test is *has a valid independent FULL already occurred?* In this
round: no. The only prior review event is the opening cold read (`c7c9081`), and `E10`
states in terms that a read is not a round, spends no budget and carries no verdict. This
is therefore the round's one FULL. The single user-approved fix and the targeted VERIFY
are both still unspent, so the blockers below can be repaired inside the cap.

**Freeze window (`E12`).** `.harness/review-pending.json` records
`"subject": "dd22789…..57d1312…"`, `dispatched_at 2026-08-21T04:01:06+00:00` — the same
range I was handed, and its tip is `HEAD`. `.harness/` is untracked
(`.gitignore:18`), so the resolved tip written there is runtime display, not the recorded
range `E12` forbids; no finding.

**Authorization I can see.** The round itself: yes, in `dd22789`. The eighth command: only
in the candidate's own commit body and `cli.py`'s docstring — `L-3`. `E11`'s preview card
is chat-rendered by the `dd22789` ruling's own terms and is **`UNVERIFIABLE`** from here
(`R4`, `R7`); I state the ceiling and move on.

---

## 2. Changed paths, classified by hand

Classified by reading each hunk, not by trusting the body's account.

| path | +/− | class |
|---|---|---|
| `tooling/rsclib/document_harness/preview.py` | +225 / 0 | new module — the round's substance |
| `tooling/tests/document_harness/test_preview.py` | +290 / 0 | new test module |
| `tooling/rsclib/document_harness/cli.py` | +40 / −3 | `_cmd_v3_preview` + subparser + docstring count |
| `tooling/tests/document_harness/test_cli_entry.py` | +4 / −2 | hand-written `OPERATIONS` literal extends to eight (`E5`) |
| `tooling/tests/document_harness_review/test_fix_round_locks.py` | +6 / −1 | `preview.py` joins `SUCCESSOR_ROUND_MODULES` + roster comment |
| `document-harness/EXECUTION.md` | +4 / 0 | **instruction-layer member** — SIMP-C4 wiring sentence (design, under this round's ruling) |
| `document-harness/REVIEW.md` | +2 / −1 | **instruction-layer member** — the cold read's `O-1` bytes |
| `document-harness/ONBOARDING.md` | +1 / −1 | **not** a member (checked against `E10`'s ten paths) — count site |
| `migration/…/v3-cold-read-dd22789.md` | +439 / 0 | the read's record (`c7c9081`) |

**`E2`.** None of the nine paths is contract `b2dbdf75…`, supersession-1 `68031fa2…`,
supersession-2 `e1a2f26b…`, or anything under `schema/document-assurance-v3/`. Frozen bytes
untouched — confirmed by path, which is what `E2` says is decidable by inspection.

**`E10` membership sentence.** `document-harness/CONSTRUCTION-CHECKLIST.md` is not in the
diff; `E10-sync` does not trigger.

**`E10` path guard.** The only backtick token either member hunk adds is `` `dtw preview` ``,
which carries a space and so falls outside `TOKEN`'s shape (`layer_path_check.py:50`,
`` `([^`\s]+)` ``); `REVIEW.md`'s added clause carries no backticks at all. Nothing this
commit adds to a member is a path token. Verified by reading the guard, not by reading the
claim.

**`E10` routing of the two member edits.** `REVIEW.md` takes the free channel — the cold
read's `O-1` supplies the exact bytes *"— the control root lives in the caller"*
(`v3-cold-read-dd22789.md:375`) and the applied text is those bytes verbatim; the path is
not one `E2` freezes, so the `HD-20` exception does not bank it. `EXECUTION.md` is a design
edit made inside the round that authorizes it. Both owe an independent read before any
round *relies* on them; authoring is not relying, and the body defers the read to the next
round's opening layer read, which is what `E10` permits. Correct on both counts.

---

## 3. Re-executed, not accepted

### 3.1 The batteries

| what | reported in the body | measured here |
|---|---|---|
| full battery, `python -m pytest -q` from `tooling` | 763 passed | **763 passed** in 104.69s |
| targeted, `test_preview.py` + `test_fix_round_locks.py` | 37 passed | **37 passed** in 1.25s |

Both figures stand. `O-2` concerns the *superseded* figure in the same sentence, not these.

### 3.2 The real-plane render

`python dtw.py preview --run <the caller's p5b-claims run>` → exit 0, final line
`RESULT: coherent (exit 0)`. Two consecutive renders to separate files, `cmp` → identical.
The body's claim reproduces. I then rendered **all eight** of the caller's run directories,
which is how `B-1` surfaced.

### 3.3 Mutation of the new guards (`R8`, `E4` shape)

Restored from sha256-checked scratchpad copies after each, never `git checkout --`; the
three touched files were re-hashed to their pre-mutation digests
(`preview.py` `baf747b0…`, `cli.py` `812c5140…`, `test_fix_round_locks.py` `c8215ba9…`)
and `git status --short` is empty.

| # | mutation (real defect shape) | result |
|---|---|---|
| 1 | Context elision neutered — instruction rendered whole | **RED** — `test_context_is_named_but_its_body_is_not_rendered` |
| 2 | WorkSpec digest copied from the plan instead of recomputed | **RED** — `test_plan_binding_a_different_workspec_says_mismatch` |
| 3 | absent check spec skipped silently instead of a `MISSING` row | **RED** ×2 — unit + the subprocess exit-1 case |
| 4 | `preview` subparser silently renamed | **RED** ×6 — `TheSurface` ×2, `TheTwoNames`, all three `PreviewCommandLine` |
| 5 | `preview.py` dropped from `SUCCESSOR_ROUND_MODULES` | **RED** — the partition guard, naming `preview.py` (reproduces the body's account of the first battery) |
| 6 | a second `f"{CODE}-…"` code added with no test naming it | **RED** — `NamedIssueReachability` |
| 7 | the `unplanned`-checks coherence branch neutered | **GREEN — full battery, 763 passed** → `L-1` |
| 8 | the `boundary` line replaced by a constant | **GREEN** → feeds `B-1` |

Mutations 1–6 bind. 7 and 8 are the two branches with no binding force at all, and they are
where the two blockers live.

### 3.4 Probes

- **Elision vs numbered sections.** Two hand-built instructions, both accepted by
  `resolve_form` as `enumerated` with `form_conformance()` returning `()`, both listing
  `R0` in `numbered_sections`, both rendering `coherent=True`: `### R0` nested under
  `## Context (non-normative)`, and `## R0` under a level-1 `# Context (non-normative)`.
  In both the `R0` heading and its bound sentence are absent from the rendered body. → `B-2`.
- **Elision vs the eight real instructions.** For each, I intersected the Context span's
  elided line range with `numbered_sections`' start lines. Swallowed sections: **0 of 8**.
  Seven put Context last (its span runs to EOF), one (`p5b-claims`) puts it first with
  level-2 siblings after it. Nothing is broken today; `B-2` is about what the mechanism
  permits, and seven of the eight instructions author their requirements at `### R<n>`.
- **Boundary shape.** All eight plans carry `effective_change_boundary` as the schema's
  `changeBoundary` **object**; every one renders as `out, write_scope`. → `B-1`.
- **Fixture vs schema.** `validate("plan", <the test fixture's plan>)` →
  `V3-SCHEMA-PLAN effective_change_boundary … is not of type 'object'`, using the
  repository's own validator. → `B-1`'s test gap.
- **Optional `check_order`.** A plan without it is schema-valid (`validate("plan", …).ok`
  is True; the schema's `required` list omits it and its description says *"Absent when the
  run has no deterministic checks"*). `dtw preview` on it dies `KeyError: 'check_order'`,
  prints no `RESULT` line, exits **1**. → `L-2`.
- **Determinism.** The same plane copied to two differently-named directories renders
  differently; first differing line `run dir     : p5b-claims` vs `… : p5b-claims-copy`.
  → `O-1`.

### 3.5 The `HD-41` clause-4 scan, re-run

I re-ran the body's own `git grep -rniE …` at this tree. Findings in `O-3`.

---

## 4. Findings

### `B-1` (blocker) — the boundary line renders two dictionary keys in place of the change boundary, on every real plane, silently

**Location.** `tooling/rsclib/document_harness/preview.py:143`:

```python
put(f"boundary    : {', '.join(plan['effective_change_boundary'])}")
```

**Ground truth.** `schema/document-assurance-v3/common.schema.json:94-113` defines
`changeBoundary` as an **object** with `additionalProperties: false` and both `write_scope`
and `out` required arrays; `resolved-assurance-plan.schema.json:115-118` binds
`effective_change_boundary` to it and lists it as required. `', '.join(dict)` iterates keys.
So for every schema-valid plan the line renders literally `boundary    : out, write_scope`
and every path is dropped. Measured on all eight of the caller's committed planes:

```
p3-corr       15 entries  ->  "out, write_scope"
p4-bridge     27 entries  ->  "out, write_scope"
p4-doc        27 entries  ->  "out, write_scope"
p5a-firewall  25 entries  ->  "out, write_scope"
p5a-shells    91 entries  ->  "out, write_scope"
p5b-claims    34 entries  ->  "out, write_scope"
p5b-firewall  33 entries  ->  "out, write_scope"
w1-r1         14 entries  ->  "out, write_scope"
```

**Why it matters here rather than being cosmetic.** `EXECUTION.md`'s SIMP-C4 bullet — the
one this candidate amends — says the START card is what the user approves, and the change
boundary is one of the four things the plane binds: it is what the candidate is later
accepted or refused against (`git_diff_boundary`, `candidate_path_check`, the repair
boundary). A card that shows two field names in its place asks for approval of a boundary
it did not display. `coherent` stays True and the command exits 0, so nothing anywhere says
so.

**Why the tests are green.** `tests/document_harness/test_preview.py:114` gives the fixture
plan `"effective_change_boundary": ["docs/target.md"]` — a list. The repository's own
`validate("plan", …)` rejects that shape. The fixture has a shape that cannot occur, and no
test asserts anything about the boundary line: mutation 8 replaced it with a constant and
`test_preview.py` + `test_cli_entry.py` stayed green.

**Minimum fix.** Render the object's two lists as their own lines (`write_scope` / `out`),
and give the fixture the schema-valid object shape. Under `E7` the defect class is *the
renderer reads a plane field with a shape the schema does not permit and the fixture does
not have*, so the same pass should assert the fixture validates — that is what stops the
next fixture drifting off-shape rather than patching this one field. The fixture's
`change_boundary`, empty `expected_artifacts` / `inputs`, and `instruction_units[0]`
missing `unit_id` are the other `spec_v2` deviations I measured; only `change_boundary` is
load-bearing for this renderer, the rest are the same class.

### `B-2` (blocker) — the Context elision can swallow a numbered section whole, so "eliding cannot drop an obligation" is false of its own code

**Location.** `tooling/rsclib/document_harness/preview.py:69-90` (`_instruction_body`), with
the claim at `:26-27`: *"Everything else — preamble, title, every numbered section, any
unnumbered normative section — appears as its own bytes, so eliding cannot drop an
obligation."* The commit body repeats it, and `test_preview.py:11-12` states its sibling —
*"the one section that is non-normative by its own heading is named, never rendered"* —
which the same measurement falsifies, since more than that one section goes unrendered.

**Ground truth.** The elision range is the Context heading's `_heading_spans` span, which
ends at the next heading of the **same or higher** level (`instruction.py:204-226`). A
numbered heading matches at any level (`_NUMBERED_HEADING = ^#{1,6}\s+R(\d+)\b`,
`instruction.py:137`), and `form_conformance`'s `innermost()` resolves a nested `### R<n>`
to that section, so the form gate raises nothing. Both consequences measured:

```
NESTED   (### R0 under ## Context)   resolve_form=enumerated  form_conformance=()
                                     numbered_sections=['R0'] coherent=True
                                     'NESTED-BOUND-SENTENCE' in preview : False
TOPLEVEL (## R0 under # Context)     resolve_form=enumerated  form_conformance=()
                                     numbered_sections=['R0'] coherent=True
                                     'TOPLEVEL-BOUND-SENTENCE' in preview : False
```

In both, the rendered body is the frontmatter, the title, the Context heading, and one
`[lines N-M not rendered: the section above is non-normative by its own heading]` note. `R0`
is gone. The header line still prints `numbered sections: R0 (lines 11-13)`, so a trace
survives — pointing at line numbers whose content was not rendered.

**Why it matters.** `form_conformance`'s own docstring names this exact class: *"A block
sitting outside both is text no obligation can be a transcript of — the START approval
surface would be narrower than the instruction, which is exactly the defect w1-r1 and
p4-bridge each paid for once."* This candidate makes `dtw preview` that surface
(`EXECUTION.md` SIMP-C4, amended here), and the surface can now be narrower than the
instruction with no gate objecting: the form gate passes it, and the preview reports
`coherent`.

**Blast radius today.** Zero of the eight real instructions. Seven put Context last so its
span runs to EOF — which is the same swallow, currently swallowing nothing; seven of those
eight author their requirements as `### R<n>`, so a requirement appended after Context, or
an appendix like `p5a-shells`' `## Appendix §A — wa: the 26 frozen bindings` written after
it instead of before, disappears silently. The claim is what is false now; the drop is one
authoring motion away.

**Minimum fix.** Bound the elision so a heading nested inside the Context span is never
swallowed — eliding only lines whose innermost heading span *is* the Context heading
matches `form_conformance`'s existing `innermost()` notion and needs no new concept. Under
`E7` the class is both halves of the claim (numbered sections **and** unnumbered normative
sections after a Context heading), and the test to add is the nested shape with an
order-preserving negative control, since the current fixture uses the one layout where the
defect cannot appear. `E6`'s "both sides" clause applies to the alternative: narrowing the
docstring instead would leave a silent-drop path in the approval surface, so the text is
not the thing to change here — the code is. `EXECUTION.md`'s new sentence (*"what the user
reads is the plane's own bytes"*) becomes true once the code is fixed and needs no separate
edit.

### `L-1` (low) — the `unplanned`-checks branch decides coherence and has no binding force at all

**Location.** `preview.py:200-203`. An obligation referencing a check absent from
`check_order` sets `coherent = False` and prints a line — a verdict-shaped branch that
flips the command's exit code.

Neutering it (`unplanned: list[str] = []`) leaves the **entire 763-test battery green**.
The behaviour itself is correct — a hand-built plane with `check_order = ["chk-alpha"]` and
`ob-r0` still referencing `chk-beta` prints *"obligations reference checks absent from the
plan order: chk-beta"* and exits 1 — but nothing holds it there. `E4`: never trust a guard
you have not seen fail. Every sibling branch in this module (`MISSING`, `MISMATCH`,
elision, SpecGap) has a test; this one was missed.

**Minimum fix.** One test on that shape, paired with a negative control, in the repair leg
that carries `B-1`/`B-2`.

### `L-2` (low) — a schema-valid plane with no `check_order` crashes, and the crash exits with the code reserved for "incoherent"

`resolved-assurance-plan.schema.json:8-15` does not require `check_order`, and its
description says *"Absent when the run has no deterministic checks."* `preview.py:188`
indexes it directly. Measured: `validate("plan", …)` → `ok = True`; `dtw preview` on that
plane → `KeyError: 'check_order'`, no `RESULT` line, **exit 1**.

`_cmd_v3_preview`'s docstring and the `RESULT` line both define exit 1 as *"plane disagrees
with itself or is missing a check spec"*. A traceback exits 1 too, so a caller reading the
exit code cannot separate "the plane is incoherent" from "the renderer fell over". The same
shape covers any other schema-valid-but-sparse plane field the module indexes directly
(`plan['plan_id']`, `spec['obligations']`, `audit['result']` …); `check_order` is the one I
could prove reachable from the schema as written.

**Minimum fix.** Either treat an absent `check_order` as "no deterministic checks" and say
so in the rendering, or catch it into the existing `SpecGap` channel so it exits 2 with the
house `SPEC_GAP:` line. Either keeps exit 1 meaning what the `RESULT` line says.

### `L-3` (low) — the ruling that admitted the eighth command exists only in this round's own commit body

`HD-47` is `implemented` and its rule is that command additions go **per case to the user**
under `R5`; `dd22789` delegates the question to this round. The answer — that the user
admitted `preview` as the eighth on 2026-08-21 — appears in the repository only as
`57d1312`'s body and `cli.py:10-11`, both written by the executor. It is load-bearing: it
authorizes the command surface, the `OPERATIONS` literal, three count sites and the
`ONBOARDING.md` edit. `R2` names chat-only load-bearing material as a finding, and
`HARNESS-DECISIONS.md`'s own admission test (准入三问 ③ — *a user ruling with no home but
the conversation and the commit body*) is satisfied.

The precedent is exact and is `HD-47` itself: the seventh command got a register entry, and
that entry's `basis` records what happened without one — its date *「只能从对话核，仓里查不到」*,
a contradiction caught a round later by VERIFY `v3-review-verify-4029b43.md` `V-1`.

**Not a candidate defect.** Register entries land at closeout as often as in a candidate
(`e351a3b`, `762dd7b` vs `39a21a8`), and this round has its closeout ahead of it. Reported
so it cannot be forgotten there.

### `L-4` (low) — no commit in the range carries `E1`'s disclosure of which of the four holdings the executor held

`E1` requires the round to state, in the commit body or the round journal, which of `R1`'s
four holdings (dispatched by / prompted by / scoped by / reported through) sat with the
executor, and not to call the result structurally independent. The immediately preceding
round put that sentence in its candidate: `7f6e7f0`'s body ends *"E1: orchestrator and
executor are one work-side session this round; the round's reads were dispatched, prompted,
scoped and reported through it, stated here and in the round journal at closeout."*

Neither `57d1312` nor `c7c9081` says anything of the kind — grepping the candidate body for
`orchestrat|executor|independen|self-check` returns one line, and it is about the
instruction-layer read. `c7c9081` asserts the reader was independent but does not state
the executor's holdings.

`E1` permits the round journal as the carrier and the journal lands at closeout, so this is
not yet a violation. It is a low because it is the sentence I need in order to know whether
this FULL is structurally independent — see `O-5`.

### `O-1` (observation) — the determinism claim is one input wider than the code

`preview.py:14-16` says *"The output depends on the input files and nothing else — no clock,
no randomness, no environment, no absolute paths."* `:127` prints `root.name`. Measured: the
same plane copied into `p5b-claims/` and `p5b-claims-copy/` renders differently, at the
first line of the body. The honesty argument the module needs — re-rendering the same run
directory is byte-identical — survives intact; the sentence as written asserts more than the
code does, which is the scope class `HD-41` ①–② exists for. Naming the directory is useful
and I am not proposing it be dropped.

### `O-2` (observation) — the superseded battery figure and the final one differ by a test the narrative does not account for

The body reads *"763 passed … (the round's first full battery, run before the partition fix
and the docstring's ceiling sentence, measured 1 failed / 761 passed and is superseded by
this figure)"*. 761 + 1 = **762** tests then; **763** now. Neither named change adds a test:
the partition fix is one tuple entry, the ceiling sentence is prose. So one test was added
between the two batteries and the parenthetical does not say so. The final figure is the one
that matters and it reproduces exactly; this is about the account of the earlier one.

### `O-3` (observation, routed `R9`) — the scan-class evidence cites one pre-candidate locator and paraphrases rather than pastes

`HD-41` ④ asks for the grep **output** in the commit body so a reviewer can see whether it
ran. The body declares its scope as *"all tracked \*.md and \*.py in this repository at this
commit's tree"* and then gives a prose disposition of a subset. Re-running the same command
at this tree:

- `document-harness/EXECUTION.md` — the body cites `:337`; at this tree it is **`:341`**,
  moved by the four lines this same candidate adds above it. The locator is
  pre-candidate while the declared scope is post-candidate (`HD-41` ③).
- The enumeration omits sites that fall under no class the body names:
  `document-harness/split-design.md:44`, `document-harness/journal/batch-b-2026-08-11.md:239`,
  `document-harness/journal/caller-onboarding-2026-08-19.md:40,:42`, and four further lines
  in `harness-repo-split.plan.md` beyond the two cited. Every one is substantively covered
  — by the `six-signed` rider row, or by "records stay as written" — so the dispositions are
  right and the enumeration is short.

**Wording-level under `R9`:** I can name no downstream decision that goes wrong if this
stays unfixed — the accurate line number is one grep away and the omitted sites are all
covered by class. It rides the next batch touching this surface.

### `O-4` (observation) — `E8`'s "one dense paragraph" against a five-paragraph body

`57d1312`'s body runs five paragraphs. Recent precedent is one: `7f6e7f0`, `84dea06`,
`e351a3b` each a single paragraph; `39a21a8` two. No trailers, correct `V3-<ROUND>-v1`
title, kind named — the rest of `E8` is met, and the branch is 69 commits ahead of
`origin/main` with nothing pushed. Reported because it is a plain departure from an explicit
clause and from the round immediately before it; whether the clause or the practice is the
thing to move is the user's call (`R5`), not mine.

### `O-5` (observation, `R1`/`E1`) — this FULL's structural independence is `UNVERIFIABLE`

I ran in a fresh context and derived the subject, round, budget, obligations and every figure
above from the repository rather than from the dispatch. Whether that amounts to structural
independence turns on how many of `R1`'s four holdings sit with the executor, and the range
does not say (`L-4`). Under `R1` a discipline kept is not the same as independence that holds
structurally, so I claim neither: the answer is not in the repository, and `R4` says
`UNVERIFIABLE` is an answer.

---

## 5. Coverage disclosure (`R4`)

**Read in full.** `document-harness/CONSTRUCTION-CHECKLIST.md`;
`migration/document-work-assurance-v3/v3-harness-review-contract.md`;
`HARNESS-DECISIONS.md` `§live` (`:1-134`) plus `HD-49`/`HD-47`;
`tooling/rsclib/document_harness/preview.py`;
`tooling/tests/document_harness/test_preview.py`; both member hunks and every hunk of the
candidate diff; `.githooks/pre-commit`; `.gitignore`; the cold read's `O-1`/`O-2`.

**Read in part.** `tooling/rsclib/document_harness/instruction.py` (`:137-350`, the heading,
form and START-binding machinery `preview.py` depends on);
`tooling/rsclib/document_harness/__init__.py` (`:146-190`, the digest and load helpers);
`tooling/rsclib/document_harness/cli.py` (docstring, `_cmd_v3_governance_scan` as the house
idiom, `_cmd_v3_preview`, `build_parser` tail, `main`);
`tooling/tests/document_harness_review/test_fix_round_locks.py` (`:300-415`);
`tooling/hooks/layer_path_check.py` (`:1-80`);
`document-harness/EXECUTION.md` (`:222-250` and `:341` only);
`CONSTRUCTION-LEDGER.md` (grepped, plus the `PREVIEW-RENDER` queue-head entry);
`v3-cold-read-dd22789.md` (grepped and its findings section read);
`migration/document-work-assurance-v3/v3-review-full-7f6e7f0.md` (structure and its `O-1`);
the four schema files named above.

**Probed only.** The eight caller run directories under
`ResearchSystem/assurance/runs` — rendered and measured programmatically, not read as
documents; `HARNESS-RIDERS.md` (grepped for the two rows the body names, not read end to end).

**Not read.** `document-harness/README.md`, `ORCHESTRATION.md`, `REVIEW.md` beyond the
amended item and its neighbours, the two contract supersessions, the journals, and the
plans. This FULL's subject is the candidate; the layer's own end-to-end read was this
round's opening cold read (`c7c9081`), and I did not re-do it.

**Marked, not verified.** My own fresh context; `E11`'s preview card and the user's
approval of it; the 2026-08-21 in-round ruling; the executor's holdings (`L-4`, `O-5`).

**Mutation ceiling.** Mutations 1–6 prove those tests have binding force against the defect
shapes I chose. They do not prove that force is sufficient — mutations 7 and 8 are the
demonstration that a branch can sit in this module with none at all.

**Worktree.** Left as found. All eight mutations were applied to working-tree copies and
reverted from sha256-checked scratchpad copies, never `git checkout --`; the three touched
files hash to their pre-review digests (`preview.py` `baf747b0…`, `cli.py` `812c5140…`,
`test_fix_round_locks.py` `c8215ba9…`), and after the last restore `git status --short` was
empty. The only entry it shows now is this record file, untracked — the orchestrator commits
it (`R6`). I committed nothing.
