# V3 review — VERIFY — subject `418b89c..fbcb035`

**Subject range** `418b89c2..fbcb035e` — 4 commits, linear, no merge: `fa4f357` (the FULL
record), `0e802c8` (plan pointer), `87cadf0` (bank row + one free-channel byte application),
`fbcb035` (the round's one user-approved fix). Six files, 446 insertions, 14 deletions.

**Verdict: `REVIEWED_NO_BLOCKER`** — 0 blockers, 1 low finding, 5 observations.

The repair is three tokens and it is the right three. `L-1`'s minimum fix was "`run-v2 README`
→ `EXECUTION.md`" at three live-code sites; exactly those three changed, nothing else in
either file moved, and — the part a VERIFY has to check and a FULL could not — the substituted
claims are now **true**: `EXECUTION.md` really does carry the `audited_by` prescription, the
faithful-restatement ceiling, and the standing context-unit shape that the three citations
send a reader to find. The defect class is closed, not just the three instances: no live-code
citation of the moved rules survives anywhere in the tooling, schema or role-instruction
trees. The full battery reproduces figure for figure on the tip tree, all nine legs. The
free-channel application to `README.md:26` is eligible, accurate against the file it
describes, and clean through both path guards with a negative control on each. The single
low is not about the repair at all: it is that the bank row this round wrote banks three
things and carries one deadline.

---

## 1. What this round is, re-derived

Not taken from the dispatch, which carried the range and nothing else (`R2`).

| Question | Answer | Where I read it |
|---|---|---|
| Round | **Batch A / A2 · R1** — `HD-14`: the six run-template rule sections move into `EXECUTION.md`. This range is its **disposition + VERIFY leg**, not new construction | `.goals/plans/harness-a2-construction.plan.md` §R1; the four commit bodies |
| Governing instructions | `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` (E1–E12 / R1–R10). The `v3-harness-review-contract.md` I was pointed at is a 5-line stub naming the checklist as its own counterpart | review-contract stub `:3`; checklist header `:9-12` |
| Budget position (`E9`) | This is the **targeted VERIFY**. The FULL occurred and its record landed (`fa4f357`); the one user-approved fix is `fbcb035`. Cap reached exactly, nothing exceeded — see §5.2 | `fa4f357`; `fbcb035` body; `E9` |
| Verdict domain | VERIFY → `REVIEWED_NO_BLOCKER \| SPEC_GAP` (`R3`) | checklist `R3` |
| Authorization | User ruling 2026-08-09, asserted identically in both dispositive commit bodies: `L-1` fix leg · `L-2` + `O-1` bank · `L-3` free channel. That triple is verbatim the FULL record's own closing recommendation, which `R10` makes input and not the decision | `87cadf0` / `fbcb035` bodies; `v3-review-full-418b89c.md:423-429` |
| Obligations of this leg | `R3` — cover the accepted findings, the whole repair diff, and the permanent boundaries however narrow the round. `R10` — the executor weighs each low and puts the fix-leg / bank choice to the user before closeout. `E9` — the fix obliges this VERIFY | `R3`; `R10`; `E9` |
| Ledger / plan state | Both still describe R1 as open with disposition pending; `HD-14` is still `live`. Expected — see §5.3 | `HARNESS-LEDGER.md:90-94`; plan `:170-176`; `HARNESS-DECISIONS.md:114-121` |

**Dispatch conformance and what arrived by chat (`R2`).** My prompt is byte-for-byte the
committed dispatch template with `{base}..{tip}` filled — `render_construction_dispatch`'s
12 lines, fixture `ResearchSystem/tooling/tests/fixtures/expected-construction-prompt.txt`,
sha256 `4f98d417ab2b5b6fc4a0985e05c8bfba3fdcc42a598fb24887ff015d45c9a089`. Appended to it was
one operational note from the dispatching executor, declared subordinate to my instructions:
the repository root, and that I write the record into the worktree without committing it.
Both are already `R6`'s text. **No load-bearing material arrived by chat**, so `R2`'s finding
does not fire.

**Ceiling (`R7`).** The user's 2026-08-09 approval of the three-way disposition exists to me
only as a committed assertion, repeated in two commit bodies. I take it at face value and
state the ceiling. "Fresh context" is marked, not verified (`R4`).

**Read coverage (`R4`).**

- *Read in full:* `CONSTRUCTION-CHECKLIST.md`; the review-contract stub; `v3-review-full-418b89c.md`
  (all 429 lines); `HARNESS-RIDERS.md` (all 19 rows); `HARNESS-DECISIONS.md` header and all of
  `§live`; `document-harness/README.md`; `.goals/plans/harness-a2-construction.plan.md`;
  `tests/document_harness/test_readme_enumeration.py`; both dispatch prompt fixtures; all four
  commit bodies and all four diffs.
- *Read in part:* `EXECUTION.md` — the stage marker, the six moved section headings, and
  `:105-210` / `:262-300` / `:300-380`, the passages the three repaired citations and the two
  banked items turn on. I did **not** re-walk all 404 lines; the FULL did.
  `HARNESS-LEDGER.md:85-120`; `hooks/layer_path_check.py` (docstring, `LAYER`,
  `unresolved_tokens`, `check`); `hooks/candidate_path_check.py` (docstring, the three
  `NOT_SCANNED` surfaces, `scanned`); `hooks/review_freeze_check.py:1-60`;
  `hooks/ledger_cap_check.py`; `rsclib/document_harness/paths.py:140-200`;
  `rsclib/document_harness/dispatch.py` (the three prompt renderers).
- *Ran myself, output pasted below:* the nine-leg battery; both path guards on the added
  README line, each with a negative control; the defect-class sweep at base and at tip; the
  `## ` heading enumeration of `EXECUTION.md`; the `E2` blob ids and the 15-file pack; the
  `EXECUTION.md` name-collision check; freeze marker and worktree state; the prompt-fixture
  digest; commit parentage and the bank-to-fix tree identity.
- *Probed only:* the two batch journals (grep hits, not read); the decisions archive
  (`HD-20`'s heading only); the closed-run and `assurance/runs/` citations of the old README
  (counted in the sweep, not swept).

---

## 2. The repair (`R3` — this first)

### 2.1 Three tokens, and they are the three the record named

`fbcb035` changes two files. `instruction.py` `:15` and `:382`, `test_transcript_audit.py`
`:83` — the exact three locations of `v3-review-full-418b89c.md` §`L-1`. Each replaces
`the run-v2 README` with `EXECUTION.md`, dropping the now-ungrammatical article. Diff totals
4 insertions / 4 deletions across the two files; there is no fourth edit. The commit declares
its own revert unit ("revert unit = 本 commit"), and `git diff 87cadf0 fbcb035` returns
exactly those two paths, so the bank commit's claim that the fix commit's tree is the tree
the battery ran on is true by construction.

### 2.2 The substituted claims are true — this is what a VERIFY adds

A FULL can check that a citation is stale. Only the leg after it can check that the new
target actually carries the thing. All three do:

```
$ grep -n "audited_by|faithful restatement|standing context-unit"  ResearchSystem/document-harness/EXECUTION.md
277:  naming the mechanism in `audited_by` (e.g. `mechanical transcript audit —
282:  text is a faithful restatement of that section is *not* checked, and FULL review's
361:  **The dispatch paragraph gets a standing context-unit**: a work order's opening
```

- `instruction.py:15` now says the cost is stated "at `transcript_audit` and in EXECUTION.md:
  coverage is established, faithful restatement is not" — `EXECUTION.md:280-283` states
  exactly that ceiling.
- `instruction.py:382` now says the disclosure belongs "in the audit record's `audited_by` and
  in EXECUTION.md" — `:276-278` is the `audited_by` prescription.
- `test_transcript_audit.py:83` now says the dispatch paragraph's out-of-section context unit
  "is the shape EXECUTION.md prescribes" — `:361-364` is that prescription, inside the moved
  *Instruction authoring rules* section.

The bare name is unambiguous: `git ls-files` finds one `EXECUTION.md` in the harness
(`ResearchSystem/document-harness/EXECUTION.md`); the only other matches are
`.claude/commands/*sandbox-execution.md`, a different basename.

### 2.3 The defect class, not the reported instance (`E7`)

At the base, over the tooling, schema and role-instruction trees, the citation appears
exactly three times — the three the record found:

```
$ git grep -in "run-v2 README" 418b89c -- ResearchSystem/tooling ResearchSystem/schema ResearchSystem/document-harness
  tooling/rsclib/document_harness/instruction.py:15
  tooling/rsclib/document_harness/instruction.py:382
  tooling/tests/document_harness/test_transcript_audit.py:83
  (+ 14 hits, all in document-harness/journal/ — immutable narrative, cites as-of-then)
```

At the tip, widening the pattern to `run-v2 README | run-v2/README | template README |
templates/run-v2` over the same trees plus `assurance/templates/`, no live-code citation of
the moved rules survives. Two hits are not the class: `EXECUTION.md:170` is this round's own
correct pointer at the README that now holds instantiation only, and
`test_precommit_checks.py:155` is a fixture string (`"an illustrative \`templates/run-v2/\`
mention"`), not a rule citation. Everything else is journals. **The class is closed, not just
the instances.**

### 2.4 The battery reproduces, figure for figure

The change set touches `ResearchSystem/tooling/`, so the tier is tooling-touching and the
full battery is owed — which the commit body states, and which is the second-order cost the
FULL warned about before the user chose this low for the fix leg. I re-ran it on the tip
tree, worktree clean, HEAD `fbcb035`:

```
tests: 29   passed: 29   failed: 0     RESULT: OK   tests/run_tests.py            (P2 compiler + shadow lint)
tests: 80   passed: 80   failed: 0     RESULT: OK   tests/run_p4_tests.py
tests: 39   passed: 39   failed: 0     RESULT: OK   tests/run_p5a_tests.py
cases: 58   matched: 58  unexpected:0  RESULT: OK   schema/fixtures/validate_fixtures.py
Ran 39 tests in 3.044s                OK           tests/harness/run_tests.py     (the v2 suite)
Ran 20 tests in 7.787s                OK           tests/stage_control/run_tests.py  (20 run, 0 failure)
632 passed in 107.78s                              pytest, ResearchSystem/tooling/tests/
RESULT: generated output fresh; lint clean (exit 0) rsc.py compile --check
RESULT: clean (exit 0)                             Thesis/Work/Tooling/repo-audit.py
41/41 cases behaved as declared; failures=0        N0 contract fixtures (not a battery leg; run for completeness)
```

Every count in `fbcb035`'s body reproduces exactly — 29, 80, 39, 58, 39, 20, 632, exit 0,
exit 0. Only the pytest wall time differs (107.78s against the recorded 105.65s), which is
not a figure anything depends on. Note which legs those are: the executor ran **six** test
legs where `EXECUTION.md:322-323` enumerates four. That is `V-1`.

### 2.5 The free-channel byte application (`L-3`) is eligible, accurate and guard-clean

`87cadf0` rewrites one cell of `ResearchSystem/document-harness/README.md:26` — an `E10`
member — under `E10`'s free channel. Each condition holds:

- *A low finding whose record names the content.* The FULL's `L-3` minimum fix: "Extend that
  one cell to name the run-template rule set."
- *Not an `E2` frozen path.* `E2` freezes three contract blobs and the 15-file schema pack;
  `README.md` is in neither.
- *Adds no clause, changes no requirement.* The cell is a navigation table row describing what
  a file contains. It creates no obligation, so `E10`'s design test does not convert it into a
  round.
- *Applied immediately, reported after the fact, reversible.* One line replaced by one line;
  38 lines before and after, 7,288 → 7,484 bytes; the commit body reports it.

And it is accurate. The claim it writes into instruction text is that `EXECUTION.md` holds six
named run-template rule sections:

```
$ grep -n "^## " ResearchSystem/document-harness/EXECUTION.md   (the six, in file order)
175: ## Pre-freeze gate            197: ## Instruction form        238: ## Authoring gate
261: ## Audit cadence              311: ## Regression-battery tiering   350: ## Instruction authoring rules
```

Six headings, same six names, same order as the cell writes them. Both guards on the one
added line, with a negative control on each — the guards fire on the real classes and pass
the real bytes:

```
layer_path_check    actual: clean
                    negative: `document-harness/EXECUTION.md`  resolves only under ResearchSystem/ — prefix missing
                              `ResearchSystem/nope/gone.md`     does not resolve from the repo root
candidate_path_check  scanned('…/README.md') -> True
                    actual: clean
                    negative: ('ResearchSystem/document-harness/GONE.md', 'control/paragraph-map.json')
```

`test_readme_enumeration.py` reads this file's prose and is the reason a doc-only edit here
would be tooling-touching anyway; it pins schema stems as delimited tokens, and the edited row
carries none, so it is unaffected — confirmed green inside the 632.

### 2.6 The bank row (`L-2` + `O-1`)

`87cadf0` adds one row, `tier-scope`, to `HARNESS-RIDERS.md` — 18 rows to 19. Against `R10`'s
row format: it is one row per rider; it names its targets by clause and line
(`EXECUTION.md:10` header, `:313` tiering section, the *Revert anchor*), not by "对应文件";
its source cell points at `v3-review-full-418b89c.md L-2 + O-1`. Its density matches the
file's own established practice — rows `E10-sync`, `chk-thin`, `HI-route`, `sg-print` and
`bind-emit2` are all comparably long. The redeem-when cell is where the gap is (`V-1`).

I walked all 19 rows against the six changed paths: **nothing was owed redemption by this
range.** Two rows deserve the explicit negative — `ctx-ground` and `mark-case` both name
symbols inside `rsclib/document_harness/instruction.py`, which `fbcb035` touched. Their
redeem-when conditions are symbol-level (`_is_context_title`; `_NORMATIVE_MARKERS` /
`form_conformance`), the fix touched only the module docstring at `:15` and
`transcript_audit`'s docstring at `:382`, and both rows' deadlines (the first enumerated-form
instruction) are unreached. Neither fires. `E10-sync`, `R10-route` and `waiver-live` all key
on `CONSTRUCTION-CHECKLIST.md` text this range did not touch.

---

## 3. Finding

### `V-1` — the `tier-scope` row banks three items and carries one deadline

**Location.** `ResearchSystem/HARNESS-RIDERS.md:29`, the redeem-when cell.

**Ground truth.** `R10`: "redeem-when is a touch condition or a deadline, whichever arrives
first; a finding whose value expires (a moment the defect starts to bite) MUST carry that
moment as its deadline." The row banks three things and gives one touch condition — the next
batch touching `EXECUTION.md`'s header or the tiering section — plus one deadline, explicitly
scoped: "**`L-2` 的 deadline** = 下一个按此文本自判档位的 doc-only 构造批".

- **`L-2` is correct.** Its bite moment is a doc-only construction batch classifying its tier
  from the contradicting text, and that is the deadline written.
- **① (the battery enumeration) is not bounded.** It bites at the next **tooling-touching**
  batch whose executor runs the four legs `EXECUTION.md:322-323` names and stops — skipping
  `tests/harness` (39) and `tests/stage_control` (20). That moment is reachable without ever
  touching `EXECUTION.md`'s header or its tiering section, so the row's touch trigger does not
  bound it, and the deadline written is for a *doc-only* batch, which is the branch ① does not
  live on. Measured on this very range: it is tooling-touching, the enumeration would have
  licensed four legs, and the executor ran six. The gap did not bite here because this
  executor knew about it — which is exactly the knowledge a bank row exists to outlive.
- **② (the *Revert anchor*) is not bounded.** Its bite moment is written into
  `EXECUTION.md:341-345` as the ruling's own condition: reviews after adoption returning
  `SPEC_GAP`s or blockers whose ground a skipped battery would have caught. That is the moment
  the user's revert condition is needed, and therefore the most expensive moment to discover
  that exercising it now costs a round.

**Why it is not a blocker.** Nothing in the range behaves wrongly today, the row's touch
trigger will eventually reach all three, and no check, evidence binding, permission or verdict
path depends on the cell. What is absent is a bound on how long "eventually" may run for ①
and ②.

**Minimum fix.** Add ①'s and ②'s bite moments to the redeem-when cell as their own deadlines.
Free-channel eligible if taken: `HARNESS-RIDERS.md` is neither an `E10` member nor an `E2`
frozen path, and a deadline on a bank row adds no clause to any rule.

**Honest boundary, stated because it may govern.** `R10`'s MUST is phrased about "a finding".
① and ② arrived as halves of an *observation* (`O-1`), not as findings, so a strict reading
leaves them outside the MUST and the row conformant as written. I report both readings; which
one governs is the user's (`R5`).

---

## 4. Observations

**`O-1v` — a FULL's low took the `E10` free channel, which `R10`'s FULL sentence does not
name.** `R10` routes lows *from reads* three ways, then says a FULL returning
`REVIEWED_NO_BLOCKER` with lows puts "the spend-the-fix-leg / bank choice" to the user — a
binary. `E10`'s free-channel sentence is unscoped: "a low finding whose record supplies the
exact bytes or names the content takes the same free channel." `L-3` came from a FULL and took
the free channel. `E10` admits it, `R10`'s named option set does not contain it, and the user
approved the route, so nothing went wrong. This is a **second instance on exactly the surface
rider `R10-route` already banks** ("下一批碰 `R10` 文本或 `E10` 自由通道句，孰先"), so
redeeming that row answers both. No bytes offered: any tiebreak adds a bound to one of the two
rules, which is design under `E10`.

**`O-2v` — the FULL's `O-4` has no recorded disposition.** The disposition covered `L-1`,
`L-2`, `L-3` and `O-1`. `O-4` — the R1 stage marker's nested emphasis — was neither applied
nor banked nor declined. It reproduces: `EXECUTION.md:167-173` wraps the marker in `*…*` and
italicises the six section names inside it, while the file's W1 marker at `:110-112` uses
`**bold**` inside the same italic wrapper for exactly that reason. Cosmetic, no decision turns
on it, and `O-2`/`O-3`/`O-5` genuinely needed no disposition — but `O-4` was the one that named
its own bytes ("one character class"), so it was the one the free channel could have taken.

**`O-3v` — `E3`'s falsifying command was not run for the assertion written into an `E10`
member.** `E3`: "A factual assertion written into instruction text runs the command that could
falsify it first, output kept in the commit body or the round journal." `87cadf0` wrote into
`README.md:26` the assertion that `EXECUTION.md` holds six named run-template rule sections;
its body argues the edit is descriptive but pastes no output. I ran it — §2.5 above — and the
assertion is exactly true, six headings in the order written. So nothing is owed forward: this
record carries the output the rule wanted. The observation is about the step, not the fact.

**`O-4v` — the README's own read obligation is not in the human-readable pointer.** `E10`: "a
layer application still owes its independent read, riding the next read of this layer at
per-member digest cost." The plan's resume pointer names only `EXECUTION.md` as owing one,
because `0e802c8` was written 35 minutes before `87cadf0` changed `README.md`. The obligation
is not lost — `E10` lets a cold read cite a prior record only for a member whose blob is
unchanged, and `README.md` moved `dd1c7c3` → `dab9f71` — but the pointer a resuming session
reads now understates what is owed. Closeout is where that is repaired.

**`O-5v` — the "marker's own instruction" does not exist on this route.** The construction
dispatch prompt is 12 lines and carries no freeze-marker bullet; that bullet belongs to
`render_dispatch`, the product-run renderer. The instruction that the commit landing the
record deletes the marker lives in `hooks/review_freeze_check.py`'s docstring and in `E9`.
Both `v3-review-full-418b89c.md` and this VERIFY's dispatch note attribute it to the marker
itself, whose 152 bytes hold only `subject` and `dispatched_at`. Nothing goes wrong — the
deletion is owed either way — but the attribution is to a text that is not there.

---

## 5. The permanent boundaries (`R3` — run second)

### 5.1 Checks

| Check | Result | How |
|---|---|---|
| `E2` freeze surface untouched | **clean** | contract `b2dbdf752d8c…`, supersession-1 `68031fa2ca31…`, supersession-2 `e1a2f26b1d8d…` all equal `E2`'s literal ids at the tip; the pack is 15 files with `paragraph-map.schema.json` at `09aa869962f5…`; no path under `schema/` or `contract/` appears in the range's name-status |
| `E10` member set unchanged | **clean** | `CONSTRUCTION-CHECKLIST.md` untouched in the range; `layer_path_check.LAYER` still lists the same nine; no member added, so `E10-sync` correctly does not fire |
| `E10` free channel used within bounds | **clean** | §2.5 — named content, non-`E2` path, no clause added, reported, reversible; owed read tracked by blob, see `O-4v` |
| `E8` git hygiene | **clean** | four new commits, linear, no amend, no push; each stages explicit paths; each body is one dense paragraph with no trailers and names its kind (record / pointer / bank / 修腿). Three titles are `V3-<ROUND>-v1`; `0e802c8` uses `chore(plans):`, matching branch-wide practice for bookkeeping commits — the same practice under which the FULL passed `418b89c`'s own `feat(harness):` title as clean |
| `E9` change boundary | **clean** | the fix stays inside the record's stated minimum fix (two files, three tokens) and declares its own revert unit; nothing exceeded, so `E9`'s "requires saying so" does not arise |
| `E9` freeze window | **clean** | marker `.harness/review-pending.json` names this exact range, `dispatched_at 2026-08-09T03:09:36Z`; tip `fbcb035` committed `03:09:26Z`; `HEAD` is `fbcb035` and `git status --porcelain` is empty — the branch has taken no commit since dispatch, and the FULL's record commit `fa4f357` was likewise the only commit in its own window |
| `E12` handoff | **clean** | the dispatch is one range through the CLI's committed template, digest matched in §1; no per-acceptance argument |
| `E3` measure-last | **clean, with `O-3v`** | `fbcb035`'s body pastes tool output rather than describing it, and discloses that the battery ran on the tree of the final commit; `87cadf0` discloses that its own tree was not separately tested and that the two commits differ by nothing else — verified: `git diff 87cadf0 fbcb035` is exactly the two tooling files |
| Ledger cap | **clean** | `ledger_cap_check.MAX_LINES` is 120; `HARNESS-LEDGER.md` is 120 lines and unchanged in the range |
| `HD-2` state machine | **clean** | no decision-log entry moved in this range, which is correct: `HD-14` implements at closeout, and `HD-2` requires the `§live` → `§implemented` move to ride the implementing commit's own closeout |
| Rider bank (`R10`) | **clean, with `V-1`** | all 19 rows walked; none owed redemption by the six changed paths (§2.6); the new row's format conforms except the redeem-when gap |
| `§live` rulings (`E10`, outranks) | **no conflict** | `HD-24`, `HD-23`, `HD-10`, `HD-18`, `HD-15`, `HD-16`, `HD-11`, `HD-12`, `HD-13`, `HD-14`, `HD-9` read; none bears on this disposition. `HD-20` (`E2` freeze beats the `E10` free channel) is in `§implemented` and is satisfied — `README.md` is not an `E2` path |

### 5.2 Budget accounting (`E9`)

| Commit | Kind | Consumes |
|---|---|---|
| `fa4f357` | the FULL's record landing | the round's one FULL (occurred when this commit landed) |
| `0e802c8` | plan pointer, bookkeeping | nothing |
| `87cadf0` | `E10` free-channel byte application + bank row | nothing — `E9` names the free-channel application as not a round |
| `fbcb035` | the one user-approved fix | the round's one fix; obliges this VERIFY |
| this record | the targeted VERIFY | the round's one VERIFY |

Cap reached exactly, nothing exceeded, and nothing is self-classified in a way that renames a
round: the fix is called a fix, the free-channel application is called one, and `E9`'s own
test — has a valid independent FULL already occurred — answers yes for `fbcb035`, which is why
it is the fix leg and not a pre-submission correction.

### 5.3 Where the pointers stand

`.goals/plans/harness-a2-construction.plan.md:170-176` still reads "the three lows' disposition
is with the user … `E9`'s one user-approved fix + one targeted VERIFY are unconsumed", and
`HARNESS-LEDGER.md:94` still reads "下一步 = R1". Both are now stale, and neither is a defect:
`0e802c8` was written before the disposition landed, and `E9`'s freeze window has forbidden the
branch any commit but this record since `03:09:36Z`. `HD-14` likewise remains `live`, correctly,
because `HD-2` binds its move to the closeout commit. Closeout is where all four move —
recorded here so the next cold start does not read them as an instruction to redo R1 or to
re-open a disposition that is closed.

---

## 6. What this VERIFY does not establish (`R4`)

- **`UNVERIFIABLE`: the user's disposition ruling.** The 2026-08-09 "按建议" approval of the
  `L-1` / `L-2`+`O-1` / `L-3` split exists to me only as an assertion in two commit bodies. I
  verified no conversation.
- **`UNVERIFIABLE`: the fresh-context claim.** Marked, not verified.
- **Mutation proves binding force, not sufficiency.** §2.5 shows both path guards firing on the
  two real defect classes and passing the real bytes. It says nothing about a token that
  resolves but names the wrong file — and that is precisely the class `L-1` belonged to. **No
  guard exists for it**; the assurance that it is closed rests entirely on §2.3's sweep and on
  my reading of §2.2, not on any instrument.
- **Not a re-certification of the FULL.** I did not reconstruct `418b89c` or re-derive the
  move's byte equality. I took the FULL's §2 as the record it is and checked only what the
  repair and the disposition changed.
- **Not swept: the rest of `EXECUTION.md`.** I read the six moved headings and four passages,
  not all 404 lines. If the move left stale text outside the moved block and outside what
  `L-1`/`L-2`/`L-3` name, this leg would not have seen it.
- **Not re-litigated: whether the six sections should have moved, or whether `HD-14`'s price
  (`O-1`) is acceptable.** Both are the user's (`R5`). My subject is the text that is there.

---

**Verdict: `REVIEWED_NO_BLOCKER`** — 0 blockers, 1 low finding (`V-1`), 5 observations
(`O-1v`…`O-5v`).

`V-1` names bytes and is free-channel eligible; `O-1v` rides rider `R10-route`; `O-2v` is
`O-4`'s unfinished disposition and names one character class; `O-3v` is discharged by this
record; `O-4v` and `O-5v` are for closeout and for whoever next touches the dispatch prose.
None of them is the round's to repair — `E9` is spent, and a VERIFY re-opens nothing.
