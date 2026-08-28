# Plan — round `V1-RESULT-RETIRE`: the version-1 review schema is retired, its shared definitions rehoused, and `E2`'s announced set re-anchored

> **Status: NOT OPENED.** Written 2026-08-28 as the round's tracked plan.
> **base_commit**: not yet fixed — this round starts from `main` *after* PR #1 merges (*Steps*
> step 0). Every site and figure below was measured at `c6454d3`, the head of
> `freeze-to-alarm-closeout`, and **must be re-derived before editing**: line numbers drift.
>
> **This round has two natures and the heavier one governs.** Items A–E and G are code and schema
> cleanup. **Item F rewrites `E2`, a clause in an `E10` member**, which is design by `E10`'s own
> test — so this round carries design-round weight throughout: full-weight opening cold read, the
> `E11` preview card, and no use of the free channel for the clause change. It is not the small
> cleanup round the queue head described; the user chose the complete form (option C, 2026-08-28)
> knowing that.
>
> **This file is the carrier of the user rulings of 2026-08-28** in *Rulings* below. Until they land
> here they live only in the conversation that took them, which is chat-only load-bearing material
> and a finding under `R2`: a reviewer starts cold from one commit and derives the rest from the
> repository, so a ruling that never reaches a commit is a ruling the reviewer cannot check.
>
> **One question is open and blocks the round** — question 5, how `E2`'s set is re-anchored. It is
> the round's heaviest single decision and all three candidate answers are design.
>
> A cold session reads this file, then `CONSTRUCTION-LEDGER.md`'s current pointer, then works.

## Goal (one line)

`schema/document-assurance-v3/review.schema.json` is retired: the five definitions the v2 schema
borrows from it move to `common.schema.json` where shared definitions already live, everything else
in it is measurably unreachable and goes with the file, and `E2`'s announced set — which today can
be resolved only because the pack happens to hold exactly fifteen files — is re-anchored to survive
the fourteen it will hold afterwards.

## Rulings (this file is their carrier)

1. **The registry decoupling joins the queue head's round rather than preceding it** (user,
   2026-08-28). The queue head's item ② as worded — *delete the v1 ReviewResult schema definition
   and its two registrations* — was not executable as written, because one of those two
   registrations was what loaded the schema file for the v2 validator.
2. **No v1 ReviewResult instance exists anywhere** (user, 2026-08-28: 「任何地方都不存在 v1 活例」).
   This authorises deleting the v1 result definition outright rather than repairing it.
   **This is a user ruling, not a measurement, and the distinction is load-bearing.** This
   repository can measure only its own tree, where the instance count is zero; the instances the v1
   leg was kept for would live in the extracted source repository and in the caller, which this
   repository cannot see. The user's statement covers those. A reviewer who re-measures will find
   the local zero and must not read it as confirmation of the wider claim — the wider claim is the
   user's, and it is what authorises the deletion.
3. **The complete form, not the partial one** (user, 2026-08-28: option C of three presented).
   Presented as: **(A)** delete the v1 result definition only, leaving 125 lines of unreachable
   structure standing; **(B)** also delete that structure, leaving a file named for v1 that holds
   only shared parts; **(C)** also rehouse the shared parts and retire the file, which takes the
   pack from fifteen files to fourteen and **forces `E2` to be rewritten**. The user chose C with
   that cost stated.
4. **The five borrowed definitions are not v1's** (user, 2026-08-28, in the question that produced
   ruling 3). They are shared definitions that live in a file named for v1 for historical reasons
   only — v1 was written first and v2 chose to reference rather than copy. Measured support below:
   their only referent is v2, their own internal `$ref`s already point at `common.schema.json`, and
   `common.schema.json` is where this pack's shared definitions already live.
5. **`review.v2.schema.json`'s explanatory sentence is rewritten, not left standing** (user,
   2026-08-28: 「改」). See item B.
6. **Rider `alarm-yaml-untested` redeems in this round** (user, 2026-08-28: 「一起」). See item H.
7. **The round's name does not matter** (user, 2026-08-28: 「随便」). `V1-RESULT-RETIRE` stands.

## Open questions

**Questions 1–4 were answered 2026-08-28** and are recorded as rulings 2, 5, 6 and 7 above.
**Question 5 is open and the round does not open until it is answered.**

5. **How is `E2`'s announced set re-anchored?** Item C takes the pack from fifteen files to
   fourteen, and `E2` today defines its set as *"every file the `schema/document-assurance-v3/` pack
   held at the 2026-08-03 re-baseline (fifteen files: the fourteen of the 2026-07-29 entry plus
   `paragraph-map.schema.json`…)"*. Only one of those fifteen is named in the clause; the other
   fourteen rest on a 2026-07-29 entry that lives in the extracted source repository, which this
   repository cannot reach. The set resolves today for one reason only: the directory happens to
   hold exactly fifteen files, so counting the directory reproduces it. **After item C it will not.**
   Rider `announced-set-anchor` records three candidate repairs and judges **all three design**:
   - **(a) add a clause this repository can resolve** — adding a subordinate clause to a rule is
     design by `E10`'s own test.
   - **(b) replace the two references with a literal enumeration** of the fourteen — moves the
     set's authority from a historical fact into the clause's own bytes, and creates a fourth
     unguarded copy alongside the guard, its test twin and the directory (the `E10-sync` shape).
   - **(c) assert the guard's list equals `git ls-files schema/document-assurance-v3/`** — makes the
     guard's expectation a function of the thing it guards, and presses on the auto-enrolment `E2`
     explicitly refuses (*"a pack file added after that date is not announced by this rule until a
     later re-baseline"*).

   **A fourth shape exists and the plan author raises it rather than recommending it**: perform a
   **new re-baseline** — `E2` already re-baselines by design rather than auto-enrolling, so dating a
   fresh baseline at this round and enumerating the fourteen is (b) carried out through the
   mechanism the clause itself provides. It has (b)'s copy problem and none of (b)'s novelty.

   **This decision is the user's.** Every answer changes what a rule requires.

## Measured starting state — 2026-08-28 at `c6454d3` (`E3`: re-run before any claim)

Every line is a command and its result. Re-run them; do not cite these figures.

**The file, by what actually reaches each part.** `review.schema.json` is **347 lines**:

| Part | Lines | Count | Reached by |
|---|---|---|---|
| ReviewPackage root | `:1-83` | 83 | the `review_package` kind alone — which has **zero callers** |
| `reviewRound` | `:85-88` | 4 | **v2**, and the root |
| `memberRole` | `:89-101` | 13 | `packageMember` only |
| `packageMember` | `:102-130` | 29 | the root only |
| `instructionCompleteness` | `:131-163` | 33 | **v2** |
| `perObligationDisposition` | `:164-194` | 31 | **v2** |
| `finding` | `:195-234` | 40 | **v2** |
| `verifyScope` | `:235-257` | 23 | **v2** |
| `reviewResult` | `:258-347` | 90 | the `review_result` kind |

**The rehousing is mechanical, not a refactor.** Three measurements, all supporting ruling 4:

- The five borrowed definitions have **exactly one referent between them**: for each of
  `reviewRound`, `instructionCompleteness`, `perObligationDisposition`, `finding`, `verifyScope`,
  `grep -rl 'review.schema.json#/$defs/<name>' schema/ tooling/` returns
  `review.v2.schema.json` and nothing else.
- **Their own internal `$ref`s already point at `common.schema.json`** — `slug`, `frozenFileRef`,
  `locator` — and **none points back into `review.schema.json`**. Moving them breaks no link.
- `common.schema.json` holds 20 `$defs` and **none of the five names collides**. It is also already
  registered in the package root's `SCHEMA_FILES` (`__init__.py:48`), so both registries load it
  today.

**What is measurably dead.**

- `grep -rn 'review_package' tooling --include=*.py` → **one hit, its own definition** at
  `review.py:65`. No caller, no test.
- `grep -rn 'reviewResult' schema/document-assurance-v3/` → **three hits, all prose, zero `$ref`**:
  the v1 file's title (`:4`), the definition (`:258`), the v2 `description` (`:5`).
- `review.schema.json:281`, inside `$defs/reviewResult`, tells the reader to reproduce a digest via
  `from rsclib.document_harness.review import package_digest`. Round `CORE-SET-CODE` deleted that
  function; the import raises `ImportError`. This is rider `v1-digest-recipe`.
- No v1 ReviewResult instance exists in this repository (see ruling 2 for the scope of that fact).

**What still touches the file, and is therefore item D's and E's work.**

- `validate_n2("review_result", …)` — four call sites, all in
  `test_flow_repair_disposition.py:538 :539 :1144 :1147`.
- `review_result_v2.py:51-55` — `result_schema_kind` returns the literal `"review_result"` for an
  instance carrying no `schema_version`. That literal is the kind name being removed; nothing
  asserts the alignment.
- `test_flow_repair_disposition.py:1876` — `N2_SCHEMA_FILENAMES` lists `review.schema.json`.
- `test_golden_review_views.py:259-275` — `review_schema()` opens the file and
  `TheClosedReviewSurface` asserts against it; its own docstring says it survives *because* the v2
  schema `$ref`s five of this file's `$defs`, naming them.
- `announced_path_disclosure.py:70` and its test twin
  `tooling/tests/document_harness/test_announced_path_disclosure.py:33` and `:67` name the path.

**The sweep blind spot (queue head ④), and the shape inside its substitute.**

- `test_fix_round_locks.py:277` — `N2_MODULES_WITHOUT_CODES = ("review.py",)`, consumed at `:379`.
  The comment at `:262-276` records the measurement that put it there: adding `CODE = "V3-REVIEW"`
  plus one `f"{CODE}-UNSWEPT-CODE"` call site to `review.py` left the battery **fully green**, so
  the blind spot is the module list, not the regex.
- Its substitute, `N2ValidatorTests` (`test_golden_review_views.py:218-227`), **iterates
  `(*review.N2_SCHEMA_FILES, *review.N2_SCHEMA_POINTERS)`** — the tables item D empties. It shrinks
  silently when they shrink, and it iterates the list it is meant to check: the **F4 defect class**
  that `test_fix_round_locks.py:370-374` names and fixed *for the module list* by comparing against
  the directory, never for the kind tables.

**The tree.**

- `python -m pytest tooling/tests -q --collect-only` → **813 tests collected**.
- `git ls-files schema/document-assurance-v3/ | wc -l` → **15**. After item C: 14.
- `git rev-list --left-right --count origin/main...HEAD` → `0 4`. PR #1 OPEN, MERGEABLE, CLEAN.
- Rider `alarm-yaml-untested`, first arm: run `33140916037`, `event=pull_request`,
  `BEFORE=57a31c1` `AFTER=c6454d3`, 4 non-merge commits judged, floor `1d4d9aa`. **The range was
  correct.**

## Constraints

- **This round writes announced bytes on three of `E2`'s sixteen paths**:
  `schema/document-assurance-v3/common.schema.json` (gains the five definitions),
  `schema/document-assurance-v3/review.v2.schema.json` (its `$ref`s and one sentence), and
  `schema/document-assurance-v3/review.schema.json` (**deleted**). Under `E2` as amended 2026-08-27
  nothing is owed *before* the write; what is owed is naming each changed path, in full and
  repo-relative, **in the body of the commit that changed it**. A deletion is a change: the commit
  that removes the file names it.
- **Rider `announced-set-anchor` falls due in this round.** Its deadline is *the first time the pack
  gains or loses a file*, and item C is that moment. Item F is the response; question 5 is its
  content. This is the one rider this round cannot defer.
- **Item F is design and it governs the round's weight.** `E2` lives in
  `document-harness/CONSTRUCTION-CHECKLIST.md`, an `E10` member; changing what a rule requires is
  design by `E10`'s own test, so the free channel does not apply. Full-weight opening cold read,
  `E11` preview card, and the executor must check whether `E10-sync`'s three mirrored sentences are
  touched — that check is owed explicitly in the commit body either way.
- **Rider `PD` does NOT fall due.** Its redeem-when names a batch touching
  `tooling/rsclib/document_harness/__init__.py`'s export surface. This round touches `review.py`'s
  `__all__`, a different file and surface.
- **Riders `sig-write-once` and `contract-wikilink-tier` do NOT redeem here.** Both ride *the next
  batch touching contract v4*, which this round does not touch. Say so, so the next reconciler does
  not read their survival as an omission.
- **Rider `e10-freeze-exception` — the executor must check.** It rides *the next round eligible to
  open that touches `E10`'s "what the guard still cannot see" list*. This round touches `E2`, not
  that list, so on today's reading it does not fall due; but item F may reach it, and if it does the
  row redeems. Decide explicitly, disclose either way.
- **`HD-55` role form**: orchestrator, executor and reviewer are separate sessions; dispatch cold
  via `dtw dispatch`; the orchestrator hand-edits no work product.
- **`HD-59`**: a committed conclusion is corrected forward, never rewritten in place. This round
  corrects one — `review.py`'s header argues both v1 kinds stay registered and *"that is not an
  oversight"*. The measurement shows `review_package` has no caller, and item A removes the reason
  the other half rested on. The original stays standing beside the correction.
- **`E9` budget**: one FULL, one user-approved fix leg, one VERIFY.
- **Landing is a PR.** `main` is protected with `enforce_admins: true`; direct pushes are refused.

## Out of scope

- OUT: redeeming `sig-write-once` and `contract-wikilink-tier` (contract v4 surface, untouched).
- OUT: the candidate-isolation design question (filed 2026-08-27; not yet ruled whether it opens a
  round).
- OUT: CI dependency pinning and third-party Action restriction (user ruled these a separate small
  piece, 2026-08-27).
- OUT: splitting the ledger's CLOSED block (a ledger batch gated by a user ruling, not a round).
- OUT: any change to what the five rehoused definitions *say*. They move byte-equal. A definition
  that changes meaning while changing address is unreviewable — the diff would show a move and hide
  an edit inside it.

## Work items

Sites are at `c6454d3` and must be re-derived before editing.

### A — the five shared definitions move to `common.schema.json`

`reviewRound`, `instructionCompleteness`, `perObligationDisposition`, `finding`, `verifyScope` move
**byte-equal** into `schema/document-assurance-v3/common.schema.json`. Their internal `$ref`s
already name `common.schema.json` and become same-file references; no link breaks (measured).
**Announced path: the commit body names `common.schema.json` in full.**

### B — `review.v2.schema.json` points at the new home

Five `$ref`s change from `review.schema.json#/$defs/…` to `common.schema.json#/$defs/…`, joining
`$ref`s that file already carries. **Ruling 5**: the `description` sentence *"verdict and
residual_uncertainty are restated inline because v1 holds them inline in reviewResult (no `$def` to
reference), kept byte-equal to v1's constraints"* is rewritten — the two fields stay inline and
byte-equal, only the reason's wording changes, because the definition it cites will not exist.
**Announced path: named in full.**

### C — `review.schema.json` is deleted

With A and B landed, what remains in the file is the ReviewPackage root, `memberRole`,
`packageMember` and `reviewResult` — 215 lines that, after item D removes the two kinds, nothing can
address. The file goes. **Announced path: the commit that deletes it names it in full.** The pack
goes from fifteen files to fourteen; that fact is item F's trigger and must be stated in the same
body.

### D — the code stops knowing about it

- `review.py:64-73` — both entries go: `review_package` (zero callers) and `review_result`. With the
  file gone, no registry needs to load it, and **the decoupling an earlier draft of this plan
  proposed is no longer needed** — the kind and its value disappear together.
- `review.py:1-21` — the header argues the current arrangement is deliberate. Rewritten per `HD-59`,
  forward, with the original conclusion left standing beside the correction.
- `review_result_v2.py:51-55` — `result_schema_kind` returns `"review_result"` for a
  `schema_version`-less instance. What it should do once that kind cannot be validated — raise, or
  keep naming something unvalidatable — is **an explicit decision the executor makes and discloses**,
  not a side effect of the deletion.
- `test_flow_repair_disposition.py:538 :539 :1144 :1147` — rewritten against the v2 result;
  `:1876` — `N2_SCHEMA_FILENAMES` drops the file.
- `test_golden_review_views.py:259-275` — `review_schema()` and `TheClosedReviewSurface` re-point at
  the definitions' new home. Its docstring states the reason it survived, and that reason still
  holds; only the address changes.

### E — the alarm's own list

`announced_path_disclosure.py:70` and its test twin (`test_announced_path_disclosure.py:33`, `:67`)
drop `review.schema.json`. **Both, in the same commit** — they assert against each other and
nothing else, so a one-sided edit leaves them agreeing about a file that is gone.

### F — `E2`'s announced set is re-anchored *(design; gated by open question 5)*

`document-harness/CONSTRUCTION-CHECKLIST.md`, the `E2` clause (`:55-82` at `c6454d3`; `E3` opens at
`:83`). Content is
question 5's answer. Whatever the shape, two things are owed in the commit body: **what the set now
is**, and **how a reader of this repository alone can resolve it** — the property whose absence rider
`announced-set-anchor` records. Check `E10-sync` (see *Constraints*).

### G — the sweep blind spot *(queue head ④)*

`test_fix_round_locks.py:277`, two things, the second a finding this plan makes rather than inherits:

1. `review.py` is excluded from the code sweep because its vocabulary is built from an argument
   (`V3-SCHEMA-<KIND>`) rather than a module constant, so an added coded call site fires no test.
2. Its substitute (`N2ValidatorTests`) iterates the very tables item D empties, so it shrinks
   silently — the F4 shape. The fix is to assert the kind tables against something that is not
   themselves. **Item D makes this urgent rather than theoretical**: those tables lose two entries
   this round, and nothing today would notice.

### H — rider redemption (three rows)

Redemption = the row deleted in the commit that earns it.

- **`v1-digest-recipe`** — earned by item C (the recipe leaves with the file).
- **`announced-set-anchor`** — earned by item F. This is the row's deadline arriving, not a
  hitchhike.
- **`alarm-yaml-untested`** (ruling 6) — carrying the evidence its first arm asks for: run
  `33140916037`, `event=pull_request`, `BEFORE=57a31c1` `AFTER=c6454d3`, 4 non-merge commits judged,
  floor `1d4d9aa`, **range correct**. Re-derive before writing; the assertion must be the reader's.
  **Scope note**: that arm asks only whether the range was right. The YAML wiring the rider's
  headline names — `fetch-depth` and the two fallback expressions — still has no test. Whether that
  deserves a fresh row is the executor's call to raise.

## Steps

- [ ] 0. **Merge PR #1** and sync `main`. User action. This round's base is the resulting `main`
      tip; record it in this file's header before step 3.
- [ ] 1. Land this plan plus a `CONSTRUCTION-LEDGER.md` current-pointer entry naming the round and
      its queue position, so the rulings and question 5 are reachable by a reviewer (`R2`).
- [ ] 2. Put question 5 to the user and record the answer **in this file**.
- [ ] 3. Open the round under `HD-55` role form: **full-weight** cold layer read via
      `dtw dispatch --read` (item F edits an `E10` member), then the `E11` preview card, then wait.
      Baseline for the read is *unchanged since some one recorded full read*, not pinned to a single
      record.
- [ ] 4. Execute A, B and C — the move, the re-point, the deletion. Each commit body names every
      announced path it touched.
- [ ] 5. Execute D and E.
- [ ] 6. Execute F per the answer to question 5.
- [ ] 7. Execute G.
- [ ] 8. Execute H — three rider rows, each deleted in the commit that earns it.
- [ ] 9. FULL review via `dtw dispatch --range BASE..TIP`; one user-approved fix leg; VERIFY.
- [ ] 10. Close: update `CONSTRUCTION-LEDGER.md`, open the PR, wait for `announced-path-disclosure`
      green, merge.

## Acceptance (done = ?)

Each shown by its command, not by a sentence.

1. `git ls-files schema/document-assurance-v3/ | wc -l` returns **14**, and
   `git ls-files schema/document-assurance-v3/review.schema.json` returns nothing.
2. From `tooling/`:
   `python -c "from rsclib.document_harness.review_subject import validate_w2; print(validate_w2('review_result_v2', {}).ok)"`
   prints `False` — the v2 validator still resolves all five `$ref`s from their new home.
   (Verified runnable in this form at `c6454d3`, where it already prints `False`: after the change,
   `False` means the `$ref`s resolve; an `ImportError` or unresolved-reference error means A or B
   broke v2.)
3. `python -c "import json;d=json.load(open('schema/document-assurance-v3/common.schema.json'));print([n for n in ('reviewRound','instructionCompleteness','perObligationDisposition','finding','verifyScope') if n in d['\$defs']])"`
   lists all five, and each is byte-equal to what `git show <base>:schema/document-assurance-v3/review.schema.json` held.
4. `grep -rn 'review.schema.json' . --include=*.py --include=*.json --include=*.md` returns only
   deliberate historical references, each one accounted for in a commit body. Nothing executable
   names the file.
5. `python -m pytest tooling/tests -q` green. Report the run; the count will differ from 813 and the
   difference is accounted for commit by commit.
6. Following whatever replaces the digest recipe reproduces a digest instead of raising
   `ImportError` — or, if the recipe left with the file, no reachable text names `package_digest`.
7. Adding a coded call site to `review.py` by hand makes at least one test red — blind spot G closes,
   demonstrated the way `test_fix_round_locks.py:262-276` demonstrated it was open. Delete the
   scratch change.
8. Shrinking either kind table by one entry makes a test red — the F4 shape in G closes. Delete the
   scratch change.
9. **`E2`'s set is resolvable from this repository alone.** State the command or the passage a
   reader follows, and follow it: it must yield the fourteen paths without reference to any
   repository this one cannot reach. This is the acceptance rider `announced-set-anchor` exists for.
10. `HARNESS-RIDERS.md` holds none of `v1-digest-recipe`, `announced-set-anchor`,
    `alarm-yaml-untested`, and `git show --stat` on each of those three commits shows the row
    deleted alongside the change that earned it — never in a commit of its own.
11. The three guards each exit 0 on the staged tree, and the `E10` members resolve 9/9.
12. The PR's `announced-path-disclosure` check is green, and every commit touching
    `common.schema.json`, `review.v2.schema.json` or `review.schema.json` names that path in its own
    body — the deletion commit included.

## Resume pointer

当前指针: **step 0** — PR #1 is not merged, and nothing starts before it does. Questions 1–4 are
answered and recorded as rulings 2 and 5–7; **question 5 (how `E2`'s set is re-anchored) is open**
and blocks step 3.

## Notes

- **Why the complete form is not more work than the partial one.** Option A would have left 125
  lines of structure that item D's deletions make structurally unreachable, and a second round would
  have had to touch the same announced file, pay a second disclosure and a second review budget to
  remove them. The one cost the complete form adds is item F — and item F's trigger, rider
  `announced-set-anchor`, has a deadline that arrives the first time the pack changes size. That
  deadline is reached by any version of this work that ever deletes the file; option C reaches it
  while the measurements are fresh.
- **What this round settles that no earlier one could.** `CORE-SET-CODE` retired the v1 *code* in
  2026-08-27 and left the *schema* standing, on the stated ground that pinned v1 history must remain
  readable. Ruling 2 removes that ground. The two rounds are one retirement in two steps, and this
  is the second.
- **Why ②③④ are one round.** All three converge on one module and one file. ③'s bytes live inside
  the definition ② deletes; ④'s excluded module is the module ② edits, and ④'s substitute coverage
  reads the very tables ② empties. Split, they would pay three review budgets for one surface — and
  item F would still be owed by whichever of them deleted the file.
