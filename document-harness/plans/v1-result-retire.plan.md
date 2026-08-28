# Plan — round `V1-RESULT-RETIRE`: the version-1 review schema is retired and its shared definitions rehoused

> **Status: OPEN since 2026-08-28** — opened by the cold read committed at `c04958a`. Written
> 2026-08-28, revised the same day after the scope question below.
> **base_commit**: **`e755d61`** — the `dev` tip after the ledger-cap batch, NOT `607ec17`.
> `607ec17` is where `main` stands; four commits sit between it and this round's start (the
> plan itself, its correction, and the two ledger-cap commits). A review dispatched from
> `607ec17` would pull all four into this round's range, which is why the number is stated
> here rather than derived from `main`. Every site and figure was measured at
> `c6454d3` and **must be re-derived before editing**: line numbers drift.
>
> **Correction, 2026-08-28, written forward rather than over the paragraph above (`HD-59`): the
> base is `60bf9eb`, not `e755d61`.** That paragraph was true when it was written and is left
> standing word for word. The commit that wrote it — `60bf9eb`, `V3-ROUND-BASE-FIX-v1` — is
> itself a fifth commit after `607ec17`, so recording the tip moved the tip. By that paragraph's
> own test, that a range must not pull in work belonging to an earlier batch, the base is the
> `dev` tip at the moment the round opens: **`60bf9eb`**. This does not regress: every commit
> written from the opening cold read onward belongs to this round and is meant to be inside its
> range, which is precisely what the four commits before `60bf9eb` were not. User ruling
> 2026-08-28.
>
> **This is a cleanup round, not a design round.** An earlier draft of this file called it design,
> on the ground that retiring a pack file forces `E2`'s announced clause to be rewritten. **That was
> wrong and the correction is recorded here rather than silently dropped** (`HD-59`): `E2`'s list
> names *the files the pack held at the 2026-08-03 re-baseline* — a historical snapshot — and the
> guard's copy is hand-written and deliberately not read back from the directory (`E5`, stated in
> `announced_path_disclosure.py`'s own comment). Deleting a file today does not change what the pack
> held then. **Neither the clause nor the guard list is edited by this round**, and the round keeps
> ordinary weight.
>
> **This file is the carrier of the nine user rulings of 2026-08-28** in *Rulings* below. Until they
> land here they live only in the conversation that took them, which is chat-only load-bearing
> material and a finding under `R2`: a reviewer starts cold from one commit and derives the rest
> from the repository, so a ruling that never reaches a commit is a ruling the reviewer cannot check.
>
> **All questions are answered. The round is ready to open.**
>
> A cold session reads this file, then `CONSTRUCTION-LEDGER.md`'s current pointer, then works.

## Goal (one line)

`schema/document-assurance-v3/review.schema.json` is retired: the five definitions the v2 schema
borrows from it move to `common.schema.json`, where this pack's shared definitions already live, and
everything else in it is measurably unreachable and goes with the file.

## Rulings (this file is their carrier)

1. **The registry decoupling joins the queue head's round rather than preceding it** (2026-08-28).
   The queue head's item ② as worded — *delete the v1 ReviewResult schema definition and its two
   registrations* — was not executable as written: one of those registrations was what loaded the
   schema file for the v2 validator.
2. **No v1 ReviewResult instance exists anywhere** (「任何地方都不存在 v1 活例」). This authorises
   deleting the v1 result definition outright rather than repairing it.
   **A ruling, not a measurement, and the distinction is load-bearing.** This repository can measure
   only its own tree, where the count is zero; the instances the v1 leg was kept for would live in
   the extracted source repository and in the caller, which this repository cannot see. The user's
   statement covers those. A reviewer who re-measures will find the local zero and **must not read
   it as confirmation of the wider claim** — the wider claim is the user's, and it is what
   authorises the deletion.
3. **The complete form, not the partial one** (option C of three). Presented as: **(A)** delete the
   v1 result definition only, leaving 125 lines of structure the same round makes unreachable;
   **(B)** also delete that structure, leaving a file named for v1 holding only shared parts;
   **(C)** also rehouse the shared parts and retire the file. C was chosen.
4. **The five borrowed definitions are not v1's.** They are shared definitions living in a file
   named for v1 for historical reasons only — v1 was written first, and v2 chose to reference rather
   than copy. Measured support: their only referent is v2, their own internal `$ref`s already point
   at `common.schema.json`, and that file is where this pack's shared definitions already live.
5. **`review.v2.schema.json`'s explanatory sentence is rewritten, not left dangling** (「改」).
6. **Rider `alarm-yaml-untested` redeems in this round** (「一起」).
7. **The round's name does not matter** (「随便」). `V1-RESULT-RETIRE` stands.
8. **`E2`'s clause and the guard's list are NOT updated** (2026-08-28, from the user's question
   *"删掉了一个之后，E2 的保护列要更新吗"*). They are not, and the reasoning is item E. The
   round-as-design framing that preceded this question is withdrawn with it.
9. **Rider `announced-set-anchor`: maintained, and it must be carried by the next design round**
   (「维持，但是下一次设计轮一定要走」). Its deadline — the pack first gaining or losing a file —
   **arrives in this round**, and a deadline requires an adjudication rather than a repair. This is
   that adjudication: the row stays, and its redeem-when is **re-pointed at the next round that
   opens as design**, which is stricter than the plan author's proposal (which was to wait for the
   pack's first *addition*). Precedent for maintaining rather than repairing at a deadline: rider
   `PD`, maintained three times.

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

- The five borrowed definitions have **exactly one referent between them**: for each,
  `grep -rl 'review.schema.json#/$defs/<name>' schema/ tooling/` returns `review.v2.schema.json`
  and nothing else.
- **Their own internal `$ref`s already point at `common.schema.json`** — `slug`, `frozenFileRef`,
  `locator` — and **none points back into `review.schema.json`**. Moving them breaks no link.
- `common.schema.json` holds 20 `$defs`, **none of the five names collides**, and it is already
  registered in the package root's `SCHEMA_FILES` (`__init__.py:48`), so both registries load it.

**What is measurably dead.**

- `grep -rn 'review_package' tooling --include=*.py` → **one hit, its own definition** at
  `review.py:65`. No caller, no test.
- `grep -rn 'reviewResult' schema/document-assurance-v3/` → **three hits, all prose, zero `$ref`**:
  the v1 file's title (`:4`), the definition (`:258`), the v2 `description` (`:5`).
- `review.schema.json:281`, inside `$defs/reviewResult`, tells the reader to reproduce a digest via
  `from rsclib.document_harness.review import package_digest`. Round `CORE-SET-CODE` deleted that
  function; the import raises `ImportError`. This is rider `v1-digest-recipe`.

**What still touches the file — items D and E's work.**

- `validate_n2("review_result", …)` — four call sites, all in
  `test_flow_repair_disposition.py:538 :539 :1144 :1147`.
- `review_result_v2.py:51-55` — `result_schema_kind` returns the literal `"review_result"` for an
  instance carrying no `schema_version`. That literal is the kind name being removed; nothing
  asserts the alignment.
- `test_flow_repair_disposition.py:1876` — `N2_SCHEMA_FILENAMES` lists the file.
- `test_golden_review_views.py:259-275` — `review_schema()` opens it, and `TheClosedReviewSurface`
  asserts against it; the docstring says it survives *because* v2 `$ref`s five of its `$defs`.
- `announced_path_disclosure.py:70` and its test twin (`test_announced_path_disclosure.py:33`,
  `:67`) name the path. **These do not change — see item E.**

**Why `E2` and the guard list are untouched (ruling 8), measured.**

- `E2`'s text (`CONSTRUCTION-CHECKLIST.md:55-82`) defines the set as *"every file the
  `schema/document-assurance-v3/` pack held **at the 2026-08-03 re-baseline**"*. A historical
  snapshot: deleting a file now does not change what the pack held then.
- `announced_path_disclosure.py:53-55` states the guard's list is *"hand-written and never read back
  from the directory (`E5`)… Listing the directory would enrol new schemas silently and make this
  guard's expectation a function of what it guards."* The list is **not** meant to equal today's
  directory.
- **No test asserts the announced paths exist on disk.** `test_announced_path_disclosure.py`'s
  `AnnouncedList` asserts only that `ANNOUNCED` equals its hand-written twin and has sixteen
  entries.
- Consequence, and it is the correct behaviour: the commit that deletes the file **does** change an
  announced path, so the guard fires on it and the body must name it. Afterwards no commit can
  change that path, so the entry never matches again — harmless. If the path is ever recreated, it
  is announced again automatically.

**The sweep blind spot (queue head ④), and the shape inside its substitute.**

- `test_fix_round_locks.py:277` — `N2_MODULES_WITHOUT_CODES = ("review.py",)`, consumed at `:379`.
  The comment at `:262-276` records the measurement: adding `CODE = "V3-REVIEW"` plus one
  `f"{CODE}-UNSWEPT-CODE"` call site left the battery **fully green**, so the blind spot is the
  module list, not the regex.
- Its substitute, `N2ValidatorTests` (`test_golden_review_views.py:218-227`), **iterates
  `(*review.N2_SCHEMA_FILES, *review.N2_SCHEMA_POINTERS)`** — the tables item D empties. It shrinks
  silently when they shrink, and it iterates the list it is meant to check: the **F4 defect class**
  that `test_fix_round_locks.py:370-374` names and fixed *for the module list* by comparing against
  the directory, never for the kind tables.

**The tree.** `python -m pytest tooling/tests -q --collect-only` → **813 tests**.
`git ls-files schema/document-assurance-v3/ | wc -l` → **15**; after item C, 14.
Rider `alarm-yaml-untested`, first arm: run `33140916037`, `event=pull_request`,
`BEFORE=57a31c1` `AFTER=c6454d3`, 4 non-merge commits judged, floor `1d4d9aa`. **Range correct.**

## Constraints

- **This round writes announced bytes on three of `E2`'s sixteen paths**: `common.schema.json`
  (gains the five definitions), `review.v2.schema.json` (its `$ref`s and one sentence), and
  `review.schema.json` (**deleted**). Under `E2` as amended 2026-08-27 nothing is owed *before* the
  write; what is owed is naming each changed path, in full and repo-relative, **in the body of the
  commit that changed it**. A deletion is a change.
- **No `E10` member is edited** (ruling 8), so this round is not design and the opening cold read
  takes its ordinary form. The read is still owed on its own terms: the previous batch edited
  `CONSTRUCTION-CHECKLIST.md`, and the baseline is *unchanged since some one recorded full read*,
  not pinned to a single record.
  - **False for this round's range since `e578e70`, corrected forward and not over (`HD-59`).**
    Three members were edited there — `contract/Document-Work-Assurance-Contract-v4.md`,
    `document-harness/REVIEW.md`, `document-harness/README.md` — by the amendment answering the
    opening read's `M-1` under `HD-63`. The line above anticipated this in its own notes: two of
    the three admissible shapes change it. **The round is still not design**: the amendment
    travels `E10`'s must-fix channel, which `HD-36` ruling 2 keeps the design test out of, and
    that channel is not a round and spends no `E9` budget. What it does owe is an independent
    re-read of the amended text, and item C does not land until that read's record is in.
- **Rider `announced-set-anchor`'s deadline arrives here and is discharged by adjudication, not
  repair** (ruling 9). Item F.
- **Rider `PD` does NOT fall due** — its redeem-when names `__init__.py`'s export surface; this
  round touches `review.py`'s `__all__`, a different file.
- **Riders `sig-write-once` and `contract-wikilink-tier` do NOT redeem here** — both ride the next
  batch touching contract v4, untouched here. Say so, so the next reconciler does not read their
  survival as an omission.
- **Rider `e10-freeze-exception` — check and disclose.** It rides the next round eligible to open
  that touches `E10`'s *"what the guard still cannot see"* list. This round touches neither, so on
  today's reading it does not fall due. Decide explicitly.
- **`HD-55` role form**: orchestrator, executor and reviewer are separate sessions; dispatch cold
  via `dtw dispatch`; the orchestrator hand-edits no work product.
- **`HD-59`**: committed conclusions are corrected forward. Two in this round — `review.py`'s header
  (item D) and this plan's own withdrawn design framing (status block).
- **`E9` budget**: one FULL, one user-approved fix leg, one VERIFY.
- **Landing**: commits go on `dev`, then a PR into protected `main`.

## Out of scope

- OUT: **rewriting `E2`'s clause or the guard's `ANNOUNCED` list** (ruling 8, reasoning in item E).
- OUT: **repairing rider `announced-set-anchor`** (ruling 9 — maintained, re-pointed at the next
  design round).
- OUT: redeeming `sig-write-once` and `contract-wikilink-tier` (contract v4 surface, untouched).
- OUT: the candidate-isolation design question (filed 2026-08-27; not yet ruled).
- OUT: CI dependency pinning and third-party Action restriction (a separate small piece).
- OUT: splitting the ledger's CLOSED block (a ledger batch gated by a user ruling, not a round).
- OUT: any change to what the five rehoused definitions *say*. They move byte-equal — a definition
  that changed meaning while changing address would be unreviewable, the diff showing a move and
  hiding an edit inside it.

## Work items

Sites are at `c6454d3` and must be re-derived before editing.

### A — the five shared definitions move to `common.schema.json`

`reviewRound`, `instructionCompleteness`, `perObligationDisposition`, `finding`, `verifyScope` move
**byte-equal**. Their internal `$ref`s already name `common.schema.json` and become same-file
references; no link breaks. **Announced path: named in full in the commit body.**

### B — `review.v2.schema.json` points at the new home

Five `$ref`s change from `review.schema.json#/$defs/…` to `common.schema.json#/$defs/…`, joining
`$ref`s that file already carries. **Ruling 5**: the `description` sentence *"verdict and
residual_uncertainty are restated inline because v1 holds them inline in reviewResult (no `$def` to
reference), kept byte-equal to v1's constraints"* is rewritten — the fields stay inline and
byte-equal, only the reason's wording changes. **Announced path: named in full.**

### C — `review.schema.json` is deleted

What remains after A is the ReviewPackage root, `memberRole`, `packageMember` and `reviewResult` —
215 lines that, once item D removes the two kinds, nothing can address. **Announced path: the commit
that deletes it names it in full.**

### D — the code stops knowing about it

- `review.py:64-73` — both entries go: `review_package` (zero callers) and `review_result`. With the
  file gone no registry needs to load it, so the decoupling an earlier draft proposed is unnecessary
  — the kind and its value disappear together.
- `review.py:1-21` — the header argues the present arrangement is deliberate. Corrected forward per
  `HD-59`, the original conclusion left standing beside the correction.
- `review_result_v2.py:51-55` — what `result_schema_kind` should do once that kind cannot be
  validated (raise, or keep naming something unvalidatable) is **an explicit decision the executor
  makes and discloses**, not a side effect.
- `test_flow_repair_disposition.py:538 :539 :1144 :1147` rewritten against the v2 result; `:1876`
  drops the file from `N2_SCHEMA_FILENAMES`.
- `test_golden_review_views.py:259-275` — `review_schema()` and `TheClosedReviewSurface` re-point at
  the definitions' new home. The docstring's stated reason still holds; only the address changes.

### E — the guard's list and `E2`'s clause are deliberately NOT changed *(ruling 8)*

`announced_path_disclosure.py:70` keeps `schema/document-assurance-v3/review.schema.json`, and so
does its test twin. **The commit body must say this was decided, not overlooked**, with the reason:
the list names the pack's 2026-08-03 membership, which deleting a file today does not alter, and it
is hand-written precisely so it is not a mirror of the directory (`E5`). A future reader who diffs
the list against the directory and finds fifteen versus fourteen must be able to find that sentence.

### F — rider `announced-set-anchor` is maintained and re-pointed *(ruling 9)*

Its deadline arrives with item C. It is **not** repaired. In `HARNESS-RIDERS.md`, the row stays and
gains a touch record naming this round, and its redeem-when becomes **the next round that opens as
design**. Not a redemption and not a refusal — the third thing a deadline admits, with rider `PD` as
precedent.

### G — the sweep blind spot *(queue head ④)*

`test_fix_round_locks.py:277`, two things, the second a finding this plan makes rather than inherits:

1. `review.py` is excluded from the code sweep because its vocabulary is built from an argument
   (`V3-SCHEMA-<KIND>`), so an added coded call site fires no test.
2. Its substitute iterates the very tables item D empties, so it shrinks silently — the F4 shape.
   The fix is to assert the kind tables against something that is not themselves. **Item D makes
   this urgent rather than theoretical**: those tables lose two entries this round and nothing would
   notice.

### H — rider redemption (two rows redeemed, one re-pointed)

Redemption = the row deleted in the commit that earns it.

- **`v1-digest-recipe`** — redeemed by item C; the recipe leaves with the file.
- **`alarm-yaml-untested`** (ruling 6) — redeemed carrying the evidence its first arm asks for: run
  `33140916037`, `event=pull_request`, `BEFORE=57a31c1` `AFTER=c6454d3`, 4 non-merge commits judged,
  floor `1d4d9aa`, **range correct**. Re-derive before writing; the assertion must be the reader's.
  **Scope note**: that arm asks only whether the range was right. The YAML wiring the headline names
  — `fetch-depth` and the two fallback expressions — still has no test. Whether that deserves a
  fresh row is the executor's call to raise.
- **`announced-set-anchor`** — not redeemed; re-pointed per item F.

## Steps

- [x] 0. Merge PR #1 and sync `main`. **DONE 2026-08-28** — merge commit `607ec17`. Work lands
      on `dev` (user ruling); this round's base is the `dev` tip **`e755d61`**, four commits later.
- [x] 1. Land this plan plus a `CONSTRUCTION-LEDGER.md` current-pointer entry, so the rulings are
      reachable by a reviewer (`R2`). **DONE** — `60989f9`, revised by the commit carrying this
      revision.
- [x] 2. Put the open questions to the user and record the answers here. **DONE 2026-08-28** — all
      answered; recorded as rulings 2 and 5–9. The design framing that question 5 rested on is
      withdrawn (ruling 8).
- [x] 3. Open the round under `HD-55` role form: cold layer read via `dtw dispatch --read`, then the
      `E11` preview card, then wait. **Ordinary weight** — no `E10` member is edited.
      **DONE 2026-08-28** — card approved; read dispatched cold over `60bf9eb`, record
      `migration/document-work-assurance-v3/v3-cold-read-60bf9eb.md` committed at `c04958a`.
      It returned one must-fix, one low and four observations. The must-fix is step 3.5.
- [x] 3.5. **`M-1` blocks item C and is the user's to answer (`R5`).** **ANSWERED 2026-08-28** —
      the user ruled in place, and ruled that the ruling say so: `HD-63` (`01753f4`) authorises
      correcting a signed literal that was true when signed and has since been made false
      elsewhere, states that it overrides §13, and records as measured that §13 had already been
      walked past twice without saying so (`1656e59`, `07ef526`). The amendment landed at
      `e578e70` over four sites — the three below plus `schema/document-assurance-v3/review.v2.schema.json:5`,
      which the class sweep found and the read had not named — with `CONTRACT-V4-SIGNATURE.md`
      gaining this write as the third post-signature write. **Item C stays blocked** until the
      must-fix channel's other half, the independent re-read of the amended text, has its record in.
      The original statement of the finding follows, left standing (`HD-59`). The read found that
      `contract/Document-Work-Assurance-Contract-v4.md:284-287` — signed text, and an `E10`
      member — promises `review.schema.json` and the v1 checker functions stay frozen for reading
      pinned v1 history. The checker half is already false (round `CORE-SET-CODE` deleted that leg
      at `56d1b17`, and nothing in the tree records it); the schema half is exactly what item C
      deletes, and the same deletion falsifies two prose siblings, `document-harness/REVIEW.md:95-96`
      and `document-harness/README.md:20`. Contract §13 (`:268`) forbids amending signed text in
      place, so the reader supplied no bytes and named three admissible shapes without choosing:
      a versioned successor under §13; a recorded ruling permitting in-place correction on the
      `HD-57` shape; or a recorded decision that the clause stands as history of what was true when
      it was signed, the two prose siblings carrying the correction. **Item C does not land until
      one is on the record.** Note that the plan's own Constraints line *"No `E10` member is
      edited"* is a change-boundary statement, and two of the three shapes would change it.
- [ ] 4. Execute A, B, C — the move, the re-point, the deletion. Each commit body names every
      announced path it touched.
- [ ] 5. Execute D, and E's disclosure sentence.
- [ ] 6. Execute G.
- [ ] 7. Execute F and H — one row re-pointed, two deleted in the commits that earn them.
- [ ] 8. FULL review via `dtw dispatch --range BASE..TIP`; one user-approved fix leg; VERIFY.
- [ ] 9. Close: update `CONSTRUCTION-LEDGER.md`, open the PR from `dev`, wait for
      `announced-path-disclosure` green, merge.

## Acceptance (done = ?)

Each shown by its command, not by a sentence.

1. `git ls-files schema/document-assurance-v3/ | wc -l` returns **14**, and
   `git ls-files schema/document-assurance-v3/review.schema.json` returns nothing.
2. From `tooling/`:
   `python -c "from rsclib.document_harness.review_subject import validate_w2; print(validate_w2('review_result_v2', {}).ok)"`
   prints `False` — the v2 validator still resolves all five `$ref`s from their new home. (Verified
   runnable in this form at `c6454d3`, where it already prints `False`: afterwards, `False` means the
   `$ref`s resolve; an unresolved-reference error means A or B broke v2.)
3. The five definitions are present in `common.schema.json` and **byte-equal** to what
   `git show <base>:schema/document-assurance-v3/review.schema.json` held.
4. `grep -rn 'review.schema.json' . --include=*.py --include=*.json --include=*.md` returns only
   deliberate references — the guard's list, its test twin, and historical records — each accounted
   for in a commit body. **Nothing resolves the file as a schema.**
5. `python -m pytest tooling/tests -q` green. Report the run; the count will differ from 813 and the
   difference is accounted for commit by commit.
6. No reachable text tells a reader to import `package_digest`.
7. Adding a coded call site to `review.py` by hand makes at least one test red — blind spot G closes,
   demonstrated the way `test_fix_round_locks.py:262-276` demonstrated it was open. Delete the
   scratch change.
8. Shrinking either kind table by one entry makes a test red — the F4 shape in G closes. Delete the
   scratch change.
9. `announced_path_disclosure.py`'s `ANNOUNCED` is **unchanged**, its test twin is **unchanged**, and
   a commit body says why (item E). This is an acceptance of *inaction*, and it is here because
   inaction is invisible in a diff.
10. `HARNESS-RIDERS.md` holds neither `v1-digest-recipe` nor `alarm-yaml-untested`;
    `announced-set-anchor` **is still there**, with a touch record naming this round and a
    redeem-when reading *the next design round*. `git show --stat` on the two deletion commits shows
    each row removed alongside the change that earned it — never in a commit of its own.
11. The three guards each exit 0 on the staged tree, and the `E10` members resolve 9/9.
12. The PR's `announced-path-disclosure` check is green, and every commit touching
    `common.schema.json`, `review.v2.schema.json` or `review.schema.json` names that path in its own
    body — the deletion commit included.

## Resume pointer

当前指针: **step 4, with item C held back** — the round is open; base is **`60bf9eb`** (the `dev`
tip when it opened, see the correction in the status block), work branch is `dev`. Done and
committed: the opening cold read (`c04958a`), the base correction (`80fcd71`), the user's ruling
`HD-63` (`01753f4`), and the `M-1` amendment (`e578e70`). **Owed before item C**: the independent
re-read of the amended text, `E10`'s must-fix channel's other half — not a round, no `E9` budget,
and the orchestrator's to dispatch. Items A, B, D, E, G, F and H are unblocked. Battery at
`e578e70` is **827 passed**, which supersedes the 813 recorded above.

## Notes

- **The design framing this plan carried for one draft, and why it was wrong.** An earlier revision
  made retiring the file force a rewrite of `E2`, and built a fourth work item and an open question
  around it. The user's question — *does E2's protected list need updating after a deletion* —
  produced the measurement that killed it: `E2` names a **2026-08-03 snapshot**, and the guard's
  list is hand-written specifically so it is *not* the directory (`E5`). Neither needs to change.
  The correction is recorded rather than dropped because the wrong framing was itself committed
  (`60989f9`), and because a future reader comparing a fifteen-entry list against a fourteen-file
  directory will ask exactly this question.
- **What is left of v1 when this round closes: nothing.** The 131 lines v2 borrows live in
  `common.schema.json` under their own names; the 215 that served only v1 are gone with the file.
- **Why ②③④ are one round.** All three converge on one module and one file. ③'s bytes live inside
  the definition ② deletes; ④'s excluded module is the module ② edits, and ④'s substitute coverage
  reads the very tables ② empties.
- **What this round settles that no earlier one could.** `CORE-SET-CODE` retired the v1 *code* on
  2026-08-27 and left the *schema* standing, on the stated ground that pinned v1 history must remain
  readable. Ruling 2 removes that ground. Two rounds, one retirement.
