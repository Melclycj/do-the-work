# Targeted VERIFY — round `PREVIEW-RENDER` at `15a53fe`

**Verdict: `REVIEWED_NO_BLOCKER`.** 2 low, 3 observations.

Both blockers are closed, and closed in the code rather than in the prose that described it
(`E6`). `B-1`: the change boundary now renders as the object the schema declares — measured on
all eight of the caller's committed planes, where the FULL measured eight copies of the literal
string `out, write_scope`, I measure the real path lists at 15/27/27/25/91/34/33/14 entries, the
same totals the FULL counted. `B-2`: a heading nested inside the Context span is no longer
swallowed — I rebuilt the FULL's two probe shapes and a third it named but did not build (an
appendix written under Context), and all three now render their bound sentence while Context's own
body stays elided. The elision on all eight real instructions is byte-for-byte what it was before
the fix, so the correction widened what renders without disturbing anything that renders today.

`L-1`, `L-2` and `O-1` landed as described. The `unplanned` branch — the one verdict-shaped branch
the FULL's mutation 7 left green across the whole battery — is now red under the same mutation. A
schema-valid plane with no `check_order` renders the absence and exits 0 instead of dying with a
`KeyError` at the exit code the `RESULT` line reserves for incoherence; I built that plane, checked
it against the repository's own `validate()`, and drove it through `dtw preview`. The determinism
docstring now names the run directory's name, which I confirmed is the *only* input beyond the
files' bytes: two differently-named copies of the same plane differ in exactly one line.

`L-4` is discharged, and discharging it settles what the FULL had to leave `UNVERIFIABLE`. The fix
body carries `E1`'s disclosure, and its answer is that **all four** of `R1`'s holdings sat with one
work-side session. So this VERIFY is not structurally independent either, and I do not claim it —
see §6.

What I found is narrower than either blocker and lives in the new tests rather than the new code.
Five of the eleven mutations I ran turned red on exactly the intended test; two stayed green, and
both sit on the repair's own new bindings: the boundary assertion is a substring over a fixture
whose two lists are the same length, so a count read from the wrong list and a dropped
`boundary` label both survive (`V-1`); and the nested-elision fixture carries exactly one nested
heading, so clamping to the *last* nested heading instead of the first survives too (`V-2`).

---

## 1. Subject, round, budget and leg — re-derived, nothing taken from the dispatch

The dispatch handed one range and nothing else. Everything below is from the repository.

```
$ git rev-parse HEAD
15a53fe8abc8921b33ff39ef8d5152d2456795ca
$ git branch --show-current
main
$ git status --porcelain
(empty)
$ git rev-list --left-right --count origin/main...HEAD
0	71
```

HEAD is the subject tip, the tree was clean at the start of this review and clean at its end, and
the branch is 71 commits ahead of `origin/main` with nothing pushed (`E8`). The four commits in
range, oldest first, with the kind each names in its own body:

| commit | title | kind |
|---|---|---|
| `c7c9081` | `V3-REVIEW-RECORD-PREVIEW-RENDER-dd22789-v1` | record — the round's opening cold read of the layer |
| `57d1312` | `V3-PREVIEW-RENDER-v1` | candidate |
| `3797786` | `V3-REVIEW-RECORD-PREVIEW-RENDER-57d1312-v1` | record — the round's FULL, `CHANGES_REQUIRED` |
| `15a53fe` | `V3-PREVIEW-RENDER-FIX-v1` | review fix |

**Round.** `PREVIEW-RENDER`, set as the queue head by the range's base `dd22789`
(`V3-E11-RULING-QUEUEHEAD-v1`, a ledger-only ruling record spending no budget) carrying the user's
2026-08-21 ruling 「脚本化要做」: a deterministic, LLM-free render of the pre-START human-readable
preview from a run's frozen control plane, re-derivable on demand so its output is not stored. The
same entry is in `CONSTRUCTION-LEDGER.md:126` as the queue head.

**Which leg this is (`E9`).** The test is *has a valid independent FULL already occurred?*
`3797786` records one, returning `CHANGES_REQUIRED` on `57d1312`. So `15a53fe` is the round's **one
user-approved fix** and obliges exactly this **targeted VERIFY**. Nothing before the FULL consumed
a leg: `c7c9081` is the opening cold read, which `E10` states is not a round, spends no budget and
carries no verdict. Ordering holds — the branch took no commit between each dispatch and its
record:

```
$ git log --format='%h %ad %s' --date=format:'%H:%M:%S' dd22789..15a53fe --reverse
c7c9081 13:46:13 V3-REVIEW-RECORD-PREVIEW-RENDER-dd22789-v1
57d1312 14:00:53 V3-PREVIEW-RENDER-v1
3797786 14:29:23 V3-REVIEW-RECORD-PREVIEW-RENDER-57d1312-v1
15a53fe 14:52:45 V3-PREVIEW-RENDER-FIX-v1
```

**Freeze window (`E12`).** `.harness/review-pending.json` records
`"subject": "dd22789…..15a53fe…"`, `dispatched_at 2026-08-21T04:52:56+00:00` — the same range I was
handed, opened 11 seconds after the fix commit landed (`14:52:45 +1000` = `04:52:45Z`). `.harness/`
is untracked (`.gitignore:18`), so the resolved tip written there is runtime display, not the
recorded range `E12` forbids; no finding, and the FULL read it the same way.

**Authorization I can see.** The fix boundary is declared in `15a53fe`'s own body — *the full
package against FULL `v3-review-full-57d1312.md`: B-1 + B-2 + L-1 + L-2 + O-1 + the E1 disclosure*,
approved by the user on 2026-08-21, two files. The user's approval itself is chat-only and
`UNVERIFIABLE` from here (`R4`, `R7`): I state the ceiling and move on. What I *can* check is that
the repair stayed inside the boundary it declares, and it did — §3.

---

## 2. The accepted findings, one by one — re-executed, not accepted

### `B-1` — closed. The boundary renders the object, on every real plane

`preview.py:152-155` replaces the `', '.join(...)` over a dict with the two lists on their own
lines. Rendered across all eight of the caller's committed planes (rendering programmatically
through `render_preview`, boundary lines truncated here at 150 characters):

```
p3-corr        type=dict ws=2  out=13 total=15  coherent=True
p4-bridge      type=dict ws=4  out=23 total=27  coherent=True
p4-doc         type=dict ws=9  out=18 total=27  coherent=True
p5a-firewall   type=dict ws=2  out=23 total=25  coherent=True
p5a-shells     type=dict ws=73 out=18 total=91  coherent=True
p5b-claims     type=dict ws=15 out=19 total=34  coherent=True
p5b-firewall   type=dict ws=3  out=30 total=33  coherent=True
w1-r1          type=dict ws=2  out=12 total=14  coherent=True

p5b-claims:
  boundary    : write_scope (15): Thesis/Research-Direction.md, Thesis/Work/Design/sandbox-…
                out (19): .goals/LEDGER.md, .goals/plans/research-system-agent-integration.…
```

The eight totals are exactly the eight the FULL measured (15 / 27 / 27 / 25 / 91 / 34 / 33 / 14).
The literal `out, write_scope` no longer appears on any plane.

The fixture is now schema-valid, which was the other half of the FULL's minimum fix, and the new
`test_fixture_is_schema_valid` runs the repository's own `validate("spec_v2", …)` and
`validate("plan", …)` against it — an expectation independent of the fixture it guards (`E5`). I
mutated both halves: reverting `effective_change_boundary` to the pre-fix list turns it red (with
17 other tests, the fixture being load-bearing throughout), and deleting one `unit_id` turns it red
alone. The `E7` widening the FULL asked for is real: the fixture's `change_boundary`,
`expected_artifacts` and `instruction_units` deviations are all repaired in the same pass, not only
the one field the renderer reads.

### `B-2` — closed, and closed against a wider shape than the one reported

`_instruction_body` now clamps each Context elision at the first heading nested inside its span
(`preview.py:81-83`). I rebuilt the FULL's two probe shapes and added a third the FULL named as
part of the class but did not build — `p5a-shells`-style appendix prose under a Context heading:

```
NESTED    (### R0 under ## Context)   NESTED-BOUND-SENTENCE rendered: True
                                      CONTEXT-BODY-MARKER rendered: False
TOPLEVEL  (## R0 under # Context)     TOPLEVEL-BOUND-SENTENCE rendered: True
                                      CONTEXT-BODY-MARKER rendered: False
APPENDIX  (### Appendix A under ## Context)
                                      APPENDIX-SENTENCE rendered: True
                                      CONTEXT-BODY-MARKER rendered: False
```

All three keep the elision note for Context's own body and render the section that owns the bytes
after it. The module docstring's claim at `:27-28` — *everything else … appears as its own bytes,
so eliding cannot drop an obligation* — is now true of the code for every shape I could construct.

**No collateral on live planes.** I reimplemented the pre-fix elision beside the current one and
diffed the rendered instruction body for all eight real runs:

```
p3-corr        elision unchanged by the fix
p4-bridge      elision unchanged by the fix
p4-doc         elision unchanged by the fix
p5a-firewall   elision unchanged by the fix
p5a-shells     elision unchanged by the fix
p5b-claims     elision unchanged by the fix
p5b-firewall   elision unchanged by the fix
w1-r1          elision unchanged by the fix
```

Consistent with the FULL's *0 of 8 swallowed today*: the repair widens correctness and moves
nothing that is already correct.

`EXECUTION.md`'s new SIMP-C4 sentence — *what the user reads is the plane's own bytes, not a
session's transcription of them* — was the text the FULL said would become true once the code was
fixed. With `B-1` and `B-2` closed it is true, and it needed no edit, which is `E6`'s "both sides"
resolved the right way round.

### `L-1` — closed. The `unplanned` branch now has binding force

`test_a_check_the_plan_does_not_order_is_loud` plus its negative control
`test_all_planned_checks_leave_no_unplanned_line`. Under the FULL's mutation 7 — the branch
neutered to `unplanned: list[str] = []`, which left the entire 763-test battery green — the
targeted module now fails:

```
=== M1 unplanned branch neutered ===
  exit: 1 | 2 failed, 19 passed in 0.86s
  red tests: ['test_a_check_the_plan_does_not_order_is_loud',
              'test_a_plan_without_check_order_renders_the_absence_instead_of_crashing']
```

### `L-2` — closed, and the defect *class* is closed with it

`plan.get("check_order")` with an explicit absence line, and `unplanned` computed against the local
`check_order` rather than re-indexing the plan. I built a schema-valid plane with no `check_order`
and no obligation referencing a check, and drove it end to end:

```
spec schema-valid: True   []
plan schema-valid: True   []
coherent: True
rendered: (the plan records no check order — absent when the run has no deterministic checks)
dtw preview exit: 0
```

The FULL flagged this as one reachable instance of a wider class — *any other schema-valid-but-
sparse plane field the module indexes directly*. I enumerated every direct index in `preview.py`
and checked each against its schema's `required` list:

| document | direct-index fields in `preview.py` | schema-optional? |
|---|---|---|
| plan | `plan_id`, `resolver_version`, `repair_cap`, `effective_change_boundary`, `work_spec_ref` | none — all five required |
| spec_v2 | `obligations`, `instruction_ref`, `work_id`, `objective` | none — all four required |
| audit | `result`, `audited_by`, `audited_at` | none — all three required |
| check | `kind`, `subject_tree` | none — both required |
| nested | `ref['path']` (`frozenFileRef.required`), `boundary['write_scope']`/`['out']` (`changeBoundary.required`), `obligation['obligation_id']`/`['requirement']` (`obligation.required`) | none |

`check_order` was the class's only member and it is fixed; nothing else in the module can reach a
`KeyError` from a schema-valid plane. `E7` is satisfied here on measurement, not on assertion.

### `O-1` — closed, and the new sentence is exactly true

`preview.py:14-17` now names the run directory's name as *the one input beyond their bytes*. I
copied one plane into two differently-named directories:

```
differing lines between two differently-named copies: 2
    -run dir     : p5b-claims
    +run dir     : p5b-claims-copy
same directory rendered twice, byte-identical: True
```

One line, and it is the one the sentence names. The honesty argument the module rests on — re-render
instead of store — holds.

### `L-4` / the `E1` disclosure — carried, and it answers `O-5`

`15a53fe`'s body states that in this round the orchestrator and the executor are one work-side
session and that **all four** of `R1`'s holdings — dispatched by, prompted by, scoped by, reported
through — sat with it, and it explicitly declines to call the round's reviews structurally
independent. That is the sentence `E1` requires and the sentence the FULL's `L-4` found missing.
Its consequence for this VERIFY is in §6.

### `O-2` — corrected in the fix body; the arithmetic checks out

The correction names `NamedIssueReachability` as the test separating the superseded 762 from the
final 763. That class collects exactly one test
(`test_preview.py::NamedIssueReachability::test_no_code_is_silent_surface`), so 761 passed + 1
failed + 1 = 763 is consistent. Whether it was added *between* the two batteries is a process claim
about a tree that no longer exists; I mark it, I do not verify it (`R4`).

---

## 3. Boundary and permanent-rule conformance

**The declared fix boundary held.** The repair leg touches exactly the two files it declares:

```
$ git diff --stat 3797786..15a53fe
 tooling/rsclib/document_harness/preview.py     | 56 +++++++++++++------
 tooling/tests/document_harness/test_preview.py | 77 ++++++++++++++++++++++++--
 2 files changed, 109 insertions(+), 24 deletions(-)
```

Every hunk maps to an approved finding: the docstring paragraph to `O-1`, `_instruction_body` and
the deleted `_context_spans` helper to `B-2`, the boundary lines to `B-1`, `check_order` and the
`unplanned` line to `L-2`, and the six new tests to `B-1`/`B-2`/`L-1`/`L-2`. The fixture's other
`spec_v2` deviations (`change_boundary`, `expected_artifacts`, the undeclared `inputs`, the missing
`unit_id`s) are the ones the FULL's `B-1` minimum fix names as the same class. Nothing outside the
package moved. `_context_spans` has no remaining reference anywhere in the repository, and
`preview.py`'s only non-test importer is `cli.py:491`, untouched.

**`E2` frozen bytes.** Untouched across the whole range, not merely the fix leg:

```
$ git diff --stat dd22789..15a53fe -- contract/ schema/
(empty)
$ git ls-tree -r 15a53fe -- contract/
100644 blob 68031fa2ca31272e31da0d42a9a02189d28fcc21	…-supersession-1.md
100644 blob e1a2f26b1d8d323d11e900f8137dea222b6571c1	…-supersession-2.md
100644 blob b2dbdf752d8c155e4c65b14b5f420b880b8184a1	…-Contract-v3.md
$ git ls-tree -r 15a53fe -- schema/document-assurance-v3/ | wc -l
15
```

Three blob ids matching `E2`'s list exactly, and the pack at the fifteen files the 2026-08-03
re-baseline names.

**`E10`.** The repair touches no member, so the path guard has nothing to scan and the membership
sentence is untouched. The candidate's two member edits (`EXECUTION.md` design under this round's
ruling, `REVIEW.md` the cold read's `O-1` bytes on the free channel) were the FULL's subject and I
did not re-adjudicate them; the independent read those bytes owe rides the next round's opening
layer read, as the candidate body says and as `E10` permits.

**`E8`.** Title `V3-PREVIEW-RENDER-FIX-v1` — the established fix-leg form (`V3-INIT-SURFACE-FIX-v1`,
`V3-DE-PREFIX-FIX-v1`, `V3-XREPO-REFS-FIX-v1`, `V3-LEDGER-SPLIT-FIX-v1`), kind named in the first
line, no trailers, nothing pushed, inside the declared boundary. The paragraph clause is `V-4`.

**`E4` / `R8`.** Eleven mutations, restored from sha256-checked scratchpad copies after each, never
`git checkout --`. Both files hash to their pre-review digests afterwards
(`preview.py` `334ecdeb…`, `test_preview.py` `73221bbe…`) and `git status --porcelain
--untracked-files=all` is empty.

| # | mutation (real defect shape) | result |
|---|---|---|
| M1 | `unplanned` branch neutered | **RED** ×2 — `…does_not_order_is_loud`, `…without_check_order…` |
| M2 | boundary reverted to the pre-fix `join` | **RED** — `…renders_both_lists_not_the_field_names` |
| M3 | nested clipping removed (pre-fix elision) | **RED** — `…nested_inside_context_is_not_swallowed` |
| M4 | `check_order` back to a direct index | **RED** — `…renders_the_absence_instead_of_crashing` |
| M5 | fixture reverted to the off-schema list shape | **RED** ×18, incl. `test_fixture_is_schema_valid` |
| M6 | `min(nested)` → `max(nested)` | **GREEN — 21 passed** → `V-2` |
| M7 | boundary counts read from the opposite list | **GREEN — 21 passed** → `V-1` |
| M8 | the two boundary lists swapped | **RED** — `…renders_both_lists_not_the_field_names` |
| M9 | the `boundary    : ` label replaced | **GREEN — 21 passed** → `V-1` |
| M10 | fixture `instruction_units` lose `unit_id` | **RED** — `test_fixture_is_schema_valid` |
| M11 | elision note replaced by an empty string | **RED** — `test_context_is_named_but_its_body_is_not_rendered` |

**Batteries, measured last on the restored tree** (`E3`):

```
$ python -m pytest -q tests/document_harness/test_preview.py
21 passed in 0.75s
$ python -m pytest -q          # from tooling/
769 passed in 108.97s (0:01:48)
```

Both reproduce the fix body's figures. 763 (the FULL's re-measured battery) + the 6 test methods
this diff adds = 769, and `test_preview.py` collects 21 where it collected 15.

---

## 4. Findings

### `V-1` (low) — the new boundary assertion is a substring over a fixture whose two lists are the same length, so two real defect shapes survive

**Location.** `tooling/tests/document_harness/test_preview.py`,
`test_boundary_renders_both_lists_not_the_field_names`:

```python
self.assertIn("write_scope (1): docs/target.md", text)
self.assertIn("out (1): docs/", text)
```

**Ground truth.** `E5` — *Assert the whole line, never a substring unrelated content can satisfy.*
The rendered lines are `boundary    : write_scope (1): docs/target.md` and
`              out (1): docs/`; neither assertion reaches the label or the leading columns. And the
fixture gives both lists length 1, so the two counts are interchangeable.

**Measured.** M9 replaces the `boundary    : ` label with `XXXXXXXX    : ` — 21 passed. M7 reads
each count from the opposite list (`write_scope (len(out))`, `out (len(write_scope))`) — 21 passed.
Both are shapes the fix's own value depends on: the counts are the summary the user reads first on
a 91-entry plane, and a count taken from the wrong list is exactly the silent narrowing `B-1` was
about. The core binding does hold — M2 (pre-fix `join`) and M8 (the two lists swapped) are both red.

**Adjacent, same location (`E6`).** The counts are a computed supplement the FULL's minimum fix did
not ask for (*render the object's two lists as their own lines*). `E6` asks what decision changes
if a derived output is absent; here the answer is plausibly *none*, since the list is on the same
line — and M7 shows nothing binds the count. Whether the count should exist is the user's call
(`R5`); if it stays, it should be bound.

**Minimum fix / content.** Assert the two whole rendered lines rather than substrings, and give the
fixture lists of different lengths — e.g. `{"write_scope": ["docs/target.md"], "out": ["docs/",
"drafts/"]}` in both `change_boundary` and `effective_change_boundary`, then assert
`"boundary    : write_scope (1): docs/target.md"` and `"              out (2): docs/, drafts/"` as
whole lines. Two-line change, no new machinery.

### `V-2` (low) — the nested-elision fixture carries one nested heading, so the clamp's direction is unbound and the claim's second half is untested

**Location.** `test_preview.py`, `NESTED_INSTRUCTION` + `test_a_section_nested_inside_context_is_
not_swallowed`; the code it guards is `preview.py:81-83`.

**Ground truth.** `E7` — test the defect class, not the reported instance. The FULL named the class
as *both halves of the claim (numbered sections **and** unnumbered normative sections after a
Context heading)*, and the code's own docstring names *a numbered section, an appendix*.

**Measured.** Two shapes inside that class have no test:

- M6 changes `end = min(nested) - 1` to `max(nested) - 1` — 21 passed. With one nested heading the
  two are identical, so the fixture cannot see the difference. On an instruction with `## Context`
  followed by `### Background` and `### R5`, the mutant elides `### Background` and its body whole
  while `### R5` renders — the same silent drop `B-2` named, one heading over.
- M3 (the clamp removed entirely) turns exactly one test red, the numbered one. The appendix half
  has no test at all. I confirmed by probe that it *behaves* correctly today (§2, `APPENDIX`), so
  this is coverage, not behaviour.

**Minimum fix / content.** Give `NESTED_INSTRUCTION` a second nested heading before the numbered
one — an `### Background (non-normative)` block with its own marker — and assert both that marker
and `NESTED-BOUND-SENTENCE` render; add one appendix-shaped case asserting an `### Appendix …`
under a trailing Context renders its body. The negative control the round already relies on (the
existing normal-layout Context tests) stays as it is.

### `V-3` (observation) — the `RESULT` line's exit-1 meaning is now exact for the reachable class, but nothing outside `SpecGap` / `AssuranceFault` is caught

`_cmd_v3_preview` (`cli.py:481-504`) catches `SpecGap` and `AssuranceFault` into exit 2 and returns
1 only for `coherent is False`. Any other exception still leaves Python's own exit 1 with a
traceback and no `RESULT` line — the shape `L-2` was an instance of. I established in §2 that no
schema-valid plane can now reach one through this module, so the gap is closed *for the class the
schemas permit*; it is not closed structurally. Recorded, not proposed: whether the command should
have a catch-all is a design question and `R5` puts it with the user.

### `V-4` (observation) — `E8`'s "one dense paragraph" against a six-paragraph fix body, the FULL's `O-4` recurring one leg later

```
15a53fe paragraphs=6  V3-PREVIEW-RENDER-FIX-v1
84dea06 paragraphs=1  V3-INIT-SURFACE-FIX-v1
2538893 paragraphs=1  V3-DE-PREFIX-FIX-v1
2937bcd paragraphs=1  V3-XREPO-REFS-FIX-v1
b5fd58b paragraphs=1  V3-LEDGER-SPLIT-FIX-v1
```

The FULL reported the same departure against the candidate at five paragraphs (`O-4`) and routed
the clause-vs-practice question to the user under `R5`; the repair leg widened it to six against
four consecutive single-paragraph predecessors. I add only the second data point — the conclusion
is still the user's, and it is the same conclusion, not a new one.

### `V-5` (observation) — two of the FULL's findings fall due at a closeout that is still ahead

Neither is a defect in the repair; both were routed to closeout by the round itself and this is the
last review leg before it, so they are recorded where the closeout will see them.

- **`L-3`** — the ruling admitting `preview` as the eighth command. `HARNESS-DECISIONS.md` at
  `15a53fe` carries no entry for it (`HD-47`, the seventh-command ruling, is the last such entry,
  `:157-179`), so the authorization for the command surface, the `OPERATIONS` literal and three
  count sites still lives only in `57d1312`'s body and `cli.py`'s docstring.
- **The `RA` rider row's count** — `HARNESS-RIDERS.md:15` still reads 「`dtw` 七命令无一是它」,
  made stale again by the eighth command with the row's substance unchanged. The candidate body
  itself says this annotation lands at closeout.

---

## 5. Routing of the findings above (`R10`)

None is must-fix, so `E10`'s must-fix channel is not in play. `V-1` and `V-2` each name the exact
content of their fix and touch no path `E2` freezes, so both meet the `E10` free channel's stated
condition — applied immediately, reported after the fact, reversible — and neither adds a clause or
a bound to any rule, so the design test does not open a round for them. Neither is wording-level
under `R9`: each names a downstream decision that goes wrong unfixed (a count read from the wrong
list, or an elision clamped the wrong way, ships silently into the START approval surface with a
green battery behind it). `V-3` and `V-4` carry no bytes and belong with the user under `R5`;
`V-5` is a pointer to work the round already routed to its own closeout. The choice among these is
the orchestrator's to put to the user before closeout, not mine to make.

---

## 6. Coverage disclosure (`R4`)

**Read in full.** `document-harness/CONSTRUCTION-CHECKLIST.md` (both sides, E1–E12 and R1–R10);
`migration/document-work-assurance-v3/v3-harness-review-contract.md` (the stub and the supersession
it names); `migration/document-work-assurance-v3/v3-review-full-57d1312.md`;
`tooling/rsclib/document_harness/preview.py` at `15a53fe`; both hunks of the repair diff and the
whole of `57d1312`'s diff for the two files the repair touches; the four commit bodies in range and
`dd22789`'s.

**Read in part.** `tooling/rsclib/document_harness/cli.py` (`_cmd_v3_preview` and its neighbours,
`build_parser` head); `tooling/rsclib/document_harness/instruction.py` (`_heading_spans` and
`numbered_sections`, `:195-245`); `tooling/rsclib/document_harness/dispatch.py` (`:545-601`, the
prompt constant and range resolution); `tooling/tests/document_harness/test_preview.py` (the diff in
full, the rest by collection and by mutation response); the four schema files named in §2;
`CONSTRUCTION-LEDGER.md` (`:88`, `:126`, `:139`); `HARNESS-DECISIONS.md` (grepped, `HD-47` read);
`HARNESS-RIDERS.md` (`:15`, `:36`); `document-harness/EXECUTION.md` and `REVIEW.md` at their amended
lines only.

**Probed only.** The eight caller run directories under the caller's own `assurance/runs` — rendered
and measured programmatically, never read as documents. Three synthetic instructions and two
synthetic planes built in a temp directory, never in the worktree.

**Not read.** `document-harness/README.md`, `ORCHESTRATION.md`, the two contract supersessions, the
journals, the plans, and the rest of the test suite beyond its pass/fail. This is a VERIFY, not a
re-certification (`R4`): its subject is the accepted findings and the repair diff, and the layer's
own end-to-end read was this round's opening cold read (`c7c9081`), which I did not re-do.

**Mutation ceiling.** M1–M5, M8, M10 and M11 prove those tests have binding force against the
defect shapes I chose. They do not prove that force is sufficient — M6, M7 and M9 are the
demonstration that shapes inside the same classes still sit unbound.

**Marked, not verified.** The user's approval of the fix boundary and of the round's preview card
(`E11`); the 2026-08-21 in-round rulings; that the pre-commit hook ran on each commit; that
`NamedIssueReachability` was added between the candidate's two batteries; my own fresh context.

**My independence, stated rather than claimed (`R1`, `E1`).** I ran cold, was handed one range and
nothing else, and re-derived the round, the budget, the authorization, the obligations and every
figure above from the repository. But `15a53fe`'s `E1` disclosure now answers what the FULL had to
leave `UNVERIFIABLE`: all four of `R1`'s holdings — dispatched by, prompted by, scoped by, reported
through — sat with one work-side session, so under `R1`'s test this VERIFY is **not structurally
independent**, and I do not call it that. Two things about the question I was set are nonetheless
checkable and check out: the prompt I received is `dispatch.CONSTRUCTION_PROMPT` (`dispatch.py:552`)
with only `{charter}`, `{base}` and `{tip}` substituted — committed bytes, not session-authored
text — and it names `CONSTRUCTION_ROLE_INSTRUCTION` (`:545`) as my standing instruction. So the
session held the buttons; the committed text set the question. Under `R5` whether that is enough is
the user's conclusion, not mine.

**Worktree.** Left as found. All eleven mutations were applied to working-tree copies and reverted
from sha256-checked scratchpad copies, never `git checkout --`; both files hash to their pre-review
digests (`preview.py` `334ecdeb001b72a7bade12111c3916e7b1b7c82822a33a2c4e487e7d164444ad`,
`test_preview.py` `73221bbed05a79e693891986973e7510b32eea8c1dcf599590bf7ba42f7b70f1`), `cli.py` is
untouched at `812c5140…`, and `git status --porcelain --untracked-files=all` was empty after the
last restore. The only entry it shows now is this record file, untracked — the orchestrator commits
it (`R6`). I committed nothing.
