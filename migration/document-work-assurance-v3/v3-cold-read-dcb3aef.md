# Instruction-layer read — subject `dcb3aef77492ea1f58eb38f44732c412a0b70231`

An `E10` read. Not a round: no budget spent, no verdict carried, output is findings tiered
must-fix / low / observation (`R3`). Dispatched with the charter
`migration/document-work-assurance-v3/v3-harness-review-contract.md`, a stub whose named
successor `document-harness/CONSTRUCTION-CHECKLIST.md` was read in full as both the standing
instruction and its own counterpart, per that file's own opening line.

This read carries two jobs that arrive as one subject. It is the layer's cold read at the
subject commit, and it is the **independent re-read of the amended text** that `E10`'s
must-fix channel owes for the amendment `e578e70` — the pair that answers `M-1` of
`v3-cold-read-60bf9eb.md`. `document-harness/plans/v1-result-retire.plan.md`'s resume pointer
names that re-read as what item C is held back for. Three of the four amended sites are
members; the fourth, `schema/document-assurance-v3/review.v2.schema.json`, is not, and was
read at its amended bytes so the pair is discharged over the whole write and not over the
part that happens to be in the layer.

Record name: `v3-cold-read-`. `R6` offers two read filenames and the layer still defines no
criterion for choosing between them (rider `read-name-split`, not closed here). I took
`cold-read` for the same reason the previous record did — the subject is the whole layer,
read end to end — and note that the amendment-re-read half has no filename precedent of its
own, which is a second face of that rider rather than a new one.

## 1. The member set, derived — not received

The dispatch enumerated nothing. `E10`'s own sentence at the subject does, and reads
**exactly nine paths**. All nine resolve at the subject commit; blob ids from
`git rev-parse dcb3aef:<path>`, run here:

| # | member | blob at `dcb3aef` |
|---|---|---|
| 1 | `document-harness/CONSTRUCTION-CHECKLIST.md` | `5f77c3fdbc0f5fc5a04516a044292d9f35885068` |
| 2 | `document-harness/README.md` | `a9c388ca0e55c76991db863d08c83e4e29d99a50` |
| 3 | `document-harness/EXECUTION.md` | `234fdddf974e580d22a1a26b54587d11c24863b3` |
| 4 | `document-harness/REVIEW.md` | `444d9d29273aea94ba1b0b767d7e5c1ced24a287` |
| 5 | `document-harness/ORCHESTRATION.md` | `a9e9f75e484f40f4a1014e5d68ed6c73aa5fbdc2` |
| 6 | `migration/document-work-assurance-v3/v3-harness-operating-contract.md` | `6d5714923870b4e13e8928221a80df68e563a5ed` |
| 7 | `migration/document-work-assurance-v3/v3-harness-review-contract.md` | `29bdc9fbde6e8db38d601dd2340d4b46a24a296f` |
| 8 | `contract/Document-Work-Assurance-Contract-v4.md` | `1df7b8de5d83c81055cbaa589a7c8353cdb90e06` |
| 9 | `schema/document-assurance-v3/paragraph-map.schema.json` | `09aa869962f592c2f86c9379be0ef3eb7d2232ff` |

`git rev-parse HEAD` returns the subject and `git status --porcelain` returns only `?? .goals/`,
untracked and outside the layer, so the worktree bytes I read are these blobs.

`HARNESS-DECISIONS.md` (`f87639958c6a362938446d2fe4ba45d8d5501724`) is not a member and is
cited by section, never by blob; its `§live` — lines 30–217, nine entries: `HD-63`, `HD-62`,
`HD-59`, `HD-41`, `HD-36`, `HD-35`, `HD-34`, `HD-23`, `HD-9` — was read in full, as `E10`
requires at an opening whether or not the layer read itself is waived. `HD-63` is new since
the previous read and is the authorisation the amendment travels on.

**What moved since the last recorded end-to-end read.** That read is `v3-cold-read-60bf9eb.md`.
`git diff --stat 60bf9eb dcb3aef --` over the nine returns three files:

```
 contract/Document-Work-Assurance-Contract-v4.md | 14 ++++++++++++--
 document-harness/README.md                      |  2 +-
 document-harness/REVIEW.md                      |  4 +++-
 3 files changed, 16 insertions(+), 4 deletions(-)
```

Those numbers are `e578e70`'s own diffstat, so the amendment is the whole of the layer's
movement in the range; `git log --oneline 60bf9eb..dcb3aef --` over the member directories
returns `dcb3aef`, `e578e70` and `80fcd71`, and the two besides the amendment touch
`document-harness/plans/`, which is not a member. I did **not** rely on the citation channel:
all nine were read end to end in this session regardless of whether their blobs moved.

## 2. The amendment re-read (`E10` must-fix channel, `e578e70`)

Taken site by site against `M-1`'s minimum — *before item C lands, the sentence is adjudicated
on the record*. It is: `HD-63` (`01753f4`) is the recorded ruling, in the `HD-57` shape `M-1`
named as one of three admissible ones, and the choice among the three was the user's (`R5`),
not the executor's or mine.

- **`contract/Document-Work-Assurance-Contract-v4.md:285-297`** — the falsified promise is
  gone and what replaces it is checkable. `56d1b17` resolves in this repository as
  `V3-CORE-SET-CODE-ITEM-G-v1`, so the clause's account of where the checker functions went is
  right, and `git log --no-walk` confirms it here rather than in the extraction source. The
  claim that the schema half's ground was withdrawn by user ruling has a committed home —
  `document-harness/plans/v1-result-retire.plan.md:52`, ruling 2 — so it is not chat-only
  load-bearing material (`R2`). The clause's own boundary sentence, that a statement of what
  the contract *requires* still takes §13's versioned-successor route, matches `HD-63`'s
  boundary paragraph word for word in substance.
- **`document-harness/README.md:20`** — the row's new claim about the guard is true, and I
  established it against the guard rather than the prose: `test_readme_enumeration.py:37-53`
  computes `missing` from `schema_dir.glob("*.schema.json")` and asserts each stem appears in
  the README, so a schema file the table fails to name is caught and a name whose file is gone
  is not. "This entry leaves with the file, and it has to leave by hand" is therefore accurate.
  The row also still resolves: `review.schema.json` is present at the subject, and the three
  enumeration rows still name 8 + 2 + 4 + 1 = 15 stems against a directory of fifteen.
- **`schema/document-assurance-v3/review.v2.schema.json:5`** — the sibling sentence the
  class sweep found is corrected, and the two propositions `review.py:11-18` cites out of that
  description (v1 history readable, never migrated) survive the rewrite, so the module header
  is not made stale by it. Confirmed by reading both.
- **`document-harness/REVIEW.md:93-97`** — corrected, with one imprecision carried; see `L-1`.

`E2`'s disclosure is met: both announced paths this commit changed appear in its body as full
repo-relative paths, and no other announced path is touched. `E10`'s `E10-sync` obligation did
not fall due — the membership sentence is byte-unchanged, and `layer_path_check.py`'s `LAYER`
tuple is still the same nine paths in the same order.

**One thing the amendment relies on that the layer does not say.** Its body reasons that "the
design test does not reach this channel (`HD-36` ruling 2)". That is `§live`'s to say and
`§live` outranks the layer on conflict, so the reliance is legitimate — but `HD-36`'s own
status line asserts the layer carries not one word of it, and I confirmed that: `E10`'s design
sentence ("an amendment adding a clause to any rule, or replacing or deleting text so that what
a rule requires changes, is design and opens a round") is unqualified, and the tiebreak that
follows it limits itself to the free channel. `HD-36` is accurate and still open; nothing here
is new, and it is recorded because this round is the first to lean on it in signed text.

## 3. Findings

### `M-1` (must-fix) — the amendment corrected §13.1's second bullet; the **first** bullet prescribes the v1 validation path that items C and D remove, and it is the one class `HD-63` does not authorise fixing

`contract/Document-Work-Assurance-Contract-v4.md:277-283` (member 8, signed text), untouched
by the amendment:

> A successor **ReviewResult declares its own version**: root `schema_version` const `"2"` […]
> **A result with no `schema_version` key is a v1 result and is validated against pinned v1
> semantics**; `"2"` selects v2; a present-but-null or any other value is a `SPEC_GAP`, fail
> closed — **no cross-version fallback in either direction**.

**It is satisfiable today and stops being so inside this round.** The only live path that
validates a v1 result against v1 semantics is the `review_result` registration at
`review.py:71` (`"review.schema.json#/$defs/reviewResult"`), reached through
`validate_n2`. The plan's item D (`:242`) deletes that registration —
"`review.py:64-73` — both entries go" — and item C deletes the file it points into. After
both, no path in the tree validates a no-`schema_version` result against v1 semantics. The
v2 checker is already not that path: `review_result_v2.py:83-89` raises `SpecGap` on a v1
result rather than validating it.

**The plan routes the code decision and never reaches the clause.** Item D `:247-249` says
what `result_schema_kind` should do "once that kind cannot be validated (raise, or keep naming
something unvalidatable) is an explicit decision the executor makes and discloses". Both
offered options contradict the bullet: *raise* is not "validated against pinned v1 semantics",
and the clause's fail-closed branch is reserved for present-but-null or other values, not for
absence; *keep naming something unvalidatable* is not validation either.
`git grep -n "13\.1"` over the plan returns nothing, and its Constraints line "No `E10` member
is edited" was written before the amendment falsified it.

**Why this is not covered by `M-1` of the previous read, nor by `HD-63`.** That finding's
subject was a **statement of fact** that had become false — the class `HD-63` opens the
in-place channel for, in as many words, "for one class only: a signed statement of fact that
was true when signed and has since been made false elsewhere". This bullet states what the
harness **requires**, and both `HD-63`'s boundary and the amendment's own closing sentence send
that class to §13's versioned-successor route. So the channel that fixed the second bullet is
by its own terms unavailable for the first, and `E10`'s design test opens a round for changing
what a rule requires.

**Why the sweep did not catch it.** The amendment's class sweep ran
`git grep -n -E "pinned v1|v1 checker|frozen v1|the v1 schema|stays? frozen|remains? frozen|which is untouched"`
— which *does* match `:281`'s "pinned v1 semantics" — and triaged the hits to "live text
carrying the falsified promise", four sites. The triage is sound for the promise class and
correct as far as it goes; what it leaves unexamined is the requirement sitting three lines
above the promise it corrected, in the same subsection.

**A second horn, recorded because it changes which shape the fix takes.** The amendment
redefined where pinned v1 material lives ("what reads that history is the commits that hold
it"). Read forward into the untouched bullet, "pinned v1 semantics" may now denote the schema
as it stands in the commits that hold v1 history, reachable by `git show`. Under that reading
the bullet is not falsified by items C and D — but the amendment then changed what an
untouched rule requires, which is the design class on the other route. Either horn needs an
adjudication; neither is dischargeable by an executor.

**Minimum, and the part that is not mine.** Before items C and D land, `:280-281` is
adjudicated on the record. Precedent supports at least three shapes — a versioned successor
under §13; a further recorded user ruling extending `HD-63` to this bullet or settling the
second horn's reading; or a decision to narrow the round so the prescribed path survives.
Which one is the user's (`R5`), and I do not choose it. **I deliberately supply no bytes**, for
the reason the previous read gave for its own `M-1`: every live shape touches signed text.
What I assert is that closing this round without one of them leaves a signed member
prescribing a validation path this repository no longer has — the same silent route that
already took the clause's neighbour, one bullet down.

### `L-1` (low, bytes supplied) — `REVIEW.md`'s corrected sentence asserts in the present tense that an artifact still in the tree is not there

`document-harness/REVIEW.md:97`, added by the amendment:

> the commits carry the history, and no working-tree artifact is kept to read it.

`review.schema.json` **is** in the working tree at the subject — item C has not landed, and the
amendment's own body says so. The intended sense is the promise-level one, and the v4
counterpart says it precisely ("this clause promises no working-tree artifact for that
reading"); this sentence drops the promise scope and reads as a claim about the tree. The
accurate fact is recoverable from the same sentence's naming of §13.1 as the corrected
promise, so it is wording-level under `R9` — filed as low rather than folded into `M-1`
because its object is different and because the bytes are appliable.

**Bytes**: replace `and no working-tree artifact is kept to read it` with
`and no working-tree artifact is promised for that reading`. True at the subject and true
after item C either way, and it matches the phrasing the same amendment used in v4. This
finding supplies exact bytes, so by `E10`'s free channel and `R10`'s routing sentence it may
be applied immediately, instruction layer included, reported after the fact — it adds no
clause and changes no rule's requirement, so the design test does not take it.

## 4. Observations

- `O-1` — **checked and clean, and it exercises the header block's own rule.**
  `CONSTRUCTION-CHECKLIST.md:14-24` routes a cited commit id by whether this repository has it.
  Measured: of the ids cited across the nine, `56d1b17`, `0d73a5f`, `23ca45b` and `184387c`
  resolve here, while `6fd0ae3`, `7011916`, `418b89c`, `a22cca0`, `838c413`, `ddd773a`,
  `a8af54c`, `9ba9bbc`, `820b287` and `7db177d` do not and route to the extraction source. The
  interesting pair is `EXECUTION.md:413-414`'s "instrument `0d73a5f`, caller `6fd0ae3`": the
  clause's worked example is the one this repository lacks, and its twin — role word, id
  present here — resolves locally, exactly as "by the first sentence's test" requires.
  **Parse hazard, noted not filed**: the trailing "a silent one means that one" can be chained
  to read *role word → extraction source, always*, which would misroute `0d73a5f`. The
  disambiguator is adjacent and the rule as written gives the right answer, so no downstream
  decision goes wrong today; recorded here so the next reader can tell it from never-looked-at,
  and because `R9`'s terminal branch is the one rider `r9-terminal-no-carrier` measured losing
  an item.
- `O-2` — **path resolution over standing text, which no instrument does.**
  `layer_path_check.py` scans only the lines a commit adds (`added_lines_by_path`), so the
  standing stock is unscanned by design and by `E10`'s own clause. I ran the equivalent by hand
  over all nine members at the subject: every backtick path token containing `/` resolves —
  including `document-harness/plans/harness-deletion-first-stabilization.plan.md`,
  `assurance/templates/run-v2/README.md`, `tooling/hooks/layer_path_check.py`,
  `tooling/rsclib/document_harness/init_target.py`,
  `tooling/rsclib/document_harness/__init__.py`,
  `tooling/tests/document_harness/test_readme_enumeration.py`, `.githooks/pre-commit` and
  `assurance/templates/run-v2/`. One token resolves from neither the root nor its own
  directory but is below the guard's shape threshold and is not caller-held:
  `contract/…-v4.md:33`'s `` `contract-v4.plan.md` ``, which lives at
  `document-harness/plans/contract-v4.plan.md`. `E10` sanctions the bare-name form for
  artifacts a caller holds; this one is in this repository at another address, so a reader
  following it lands on nothing. Not filed — no `/`, so the guard's class does not reach it,
  and the same file already carries rider `contract-wikilink-tier` on the neighbouring
  reference; it belongs with that row's batch.
- `O-3` — **the four doc paths `EXECUTION.md`'s tiering exception says code and tests pin are
  real, verified at their pins**: `document-harness/README.md` at
  `test_readme_enumeration.py:36`; the member paths at `layer_path_check.py:37-47`; the two
  shipped instance templates at `init_target.py:40-53`, and `document-harness/templates/` holds
  exactly those two; `contract/Document-Work-Assurance-Contract-v4.md` at
  `__init__.py:41`. `E2`'s "fifteen files" still matches
  `schema/document-assurance-v3/` (15). `ORCHESTRATION.md`'s "nine obligations already law
  elsewhere" table has nine rows, its three own-text sections make `README.md:22`'s twelve, and
  `EXECUTION.md`'s six run-template sections are all present with the four it names as run-author
  sections. My charter stub's own claim checks out: `dispatch.py:548-549` hard-codes that path as
  `CONSTRUCTION_ROLE_INSTRUCTION`, it is what the read family hands out (`:703`, `:720`), and
  `test_dispatch.py:398/:463/:522` pins it in hand-written constants (`E5`).
- `O-4` — **`README.md:22`'s "added as the tenth member 2026-08-18" is unchanged, third cycle.**
  Reported by `v3-cold-read-b737742.md` `O-3`, re-observed by `v3-cold-read-60bf9eb.md` `O-2`,
  and rider `r9-terminal-no-carrier` exists because the first cycle's routing left no carrier.
  The amendment touched this member's line 20 and not line 22, which is within its boundary and
  not a criticism of it. Recorded so the third cycle is on the record too. The statement is true
  as dated history; `E10`'s membership sentence remains the only authority on the count, and it
  reads nine.
- `O-5` — **outside the subject, cheap to state**: `test_readme_enumeration.py:21-22`'s
  docstring says "all 14 delimited stems sit in the three enumeration rows today"; the directory
  now holds fifteen and the README names fifteen. The assertion is unaffected — it iterates the
  directory — so this is a stale figure in a test docstring, not a guard defect. Named because
  a reader reconciling `E2`'s fifteen against it would find a disagreement that is not one.
- `O-6` — riders `e10-freeze-exception`, `announced-set-anchor`, `e10-cannot-see`,
  `E10-sync`, `charter-qualifiers`, `e1-table`, `e1-reader`, `read-name-split`,
  `e9-pair-budget` and `checklist-cited-not-carried` all describe layer text I read at this
  subject; each is present as its row describes and none has been repaired, which is what those
  rows say to expect. Confirmed present, nothing added — re-filing any of them would be the
  duplication `R10` routes away from.

## 5. Coverage and ceilings (`R4`)

- **Read in full**: all nine members; `schema/document-assurance-v3/review.v2.schema.json` at
  its amended bytes; `HARNESS-DECISIONS.md` `§live` (lines 30–217); `HARNESS-RIDERS.md`;
  `tooling/hooks/layer_path_check.py`; `tooling/tests/document_harness/test_readme_enumeration.py`;
  `e578e70`'s full commit body and its diff over the four amended files.
- **Sampled**: `document-harness/plans/v1-result-retire.plan.md` (goal, rulings, measured
  starting state, work items A–H, and the resume pointer — not the whole file);
  `tooling/rsclib/document_harness/review.py` (header and the two kind tables);
  `review_result_v2.py:40-94`; `dispatch.py` and `test_dispatch.py` via grep with context.
- **Probed by command only**: the fourteen cited commit ids of `O-1`, via
  `git log --no-walk`; the schema pack and `document-harness/templates/`, via directory
  listing; `init_target.py` and `__init__.py`, via grep for the two pins.
- **Not done, stated rather than softened**: no test suite was run and nothing was
  mutation-tested in this session — every attempt to execute a Python interpreter was refused
  by the environment's permission layer, so `O-2`'s standing-text scan was performed with the
  repository search tools reproducing the guard's own predicates by hand, not by running the
  guard. A reader wanting binding force on `O-2` or on `M-1`'s "no path validates a v1 result"
  claim should demand the execution; `M-1` rests on reading `review.py:64-73`,
  `review_result_v2.py:83-89` and the plan's own item D, plus the plan's four named call sites,
  not on running them. The orchestrator addendum to `e578e70` records a 827-passing battery at
  that commit; I did not re-run it and do not restate it as my own measurement.
- **Process claims are marked, not verified** — that this session started cold and read nothing
  of the round beyond what is committed is a declaration with no evidence lock. What is
  checkable is that every fact above cites a command or a committed byte.
- **`M-1` deliberately supplies no bytes**; `L-1` supplies them. The tiering of `M-1` follows
  the previous read's own precedent — a clause true at the subject that the round in flight
  falsifies is filed at the opening rather than banked, because the moment it bites is inside
  that round.
