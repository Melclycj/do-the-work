# Instruction-layer read — subject `60bf9ebc735f9df011913dd652843f1ba3920f48`

An `E10` read. Not a round: no budget spent, no verdict carried, output is findings tiered
must-fix / low / observation (`R3`). Dispatched with the charter
`migration/document-work-assurance-v3/v3-harness-review-contract.md`, a stub whose named
successor `document-harness/CONSTRUCTION-CHECKLIST.md` was read in full as both the standing
instruction and its own counterpart, per that file's own opening line.

Record name: `v3-cold-read-`. `R6` offers two read filenames and the layer still defines no
criterion for choosing between them (rider `read-name-split`, not closed here). I took
`cold-read` because the subject is the whole layer at a commit that opens a round — the
queue head `V1-RESULT-RETIRE`, whose plan's resume pointer names the opening cold read as
the next action.

## 1. The member set, derived — not received

The dispatch enumerated nothing. `E10`'s own sentence at the subject does, and reads
**exactly nine paths**. All nine resolve at the subject commit; blob ids from
`git rev-parse 60bf9eb:<path>`, run here:

| # | member | blob at `60bf9eb` |
|---|---|---|
| 1 | `document-harness/CONSTRUCTION-CHECKLIST.md` | `5f77c3fdbc0f5fc5a04516a044292d9f35885068` |
| 2 | `document-harness/README.md` | `0a4da19b0d522d307997f681d5dec333b9349486` |
| 3 | `document-harness/EXECUTION.md` | `234fdddf974e580d22a1a26b54587d11c24863b3` |
| 4 | `document-harness/REVIEW.md` | `aad3dd83643a4656aa239e97afec8edb691228a6` |
| 5 | `document-harness/ORCHESTRATION.md` | `a9e9f75e484f40f4a1014e5d68ed6c73aa5fbdc2` |
| 6 | `migration/document-work-assurance-v3/v3-harness-operating-contract.md` | `6d5714923870b4e13e8928221a80df68e563a5ed` |
| 7 | `migration/document-work-assurance-v3/v3-harness-review-contract.md` | `29bdc9fbde6e8db38d601dd2340d4b46a24a296f` |
| 8 | `contract/Document-Work-Assurance-Contract-v4.md` | `5dfb7b64265c821c715f23de52824beeadea3405` |
| 9 | `schema/document-assurance-v3/paragraph-map.schema.json` | `09aa869962f592c2f86c9379be0ef3eb7d2232ff` |

`git rev-parse HEAD` returns the subject, and `git status --porcelain --untracked-files=no`
returns nothing, so the worktree bytes I read are these blobs. `.goals/` is untracked and
outside the layer.

`HARNESS-DECISIONS.md` (`c785dd635980ae4e8d75e8f3e0f4f3b696d3a4df`) is not a member and is
cited by section, never by blob; its `§live` — `HD-62`, `HD-59`, `HD-41`, `HD-36`, `HD-35`,
`HD-34`, `HD-23`, `HD-9`, lines 30–180 — was read in full, as `E10` requires at an opening
whether or not the layer read itself is waived.

**What moved since the last recorded end-to-end read.** That read is
`v3-cold-read-860401e.md`. `git diff --stat 860401e 60bf9eb --` over the nine returns one
file:

```
 document-harness/CONSTRUCTION-CHECKLIST.md | 54 ++++++++++++++++--------------
 1 file changed, 29 insertions(+), 25 deletions(-)
```

That is the `E2` rewrite at `184387c` (batch `FREEZE-TO-ALARM` item A) and nothing else;
`git log` over the nine confirms `184387c` is the newest layer-touching commit. I did **not**
rely on the citation channel: all nine members were read end to end in this session
regardless of whether their blobs moved.

## 2. Findings

### `M-1` (must-fix) — a signed clause promises two artifacts stay for reading pinned v1 history; one is already gone, the other is what the opening round deletes, and no record reconciles either

`contract/Document-Work-Assurance-Contract-v4.md:284-287` (member 8, signed text):

> Newly opened runs author v2 results. Closed runs and shadow rounds keep their frozen
> packages as **pinned v1 history**: no migration, no re-freeze, no retroactive script
> fixes; `review.schema.json` and the v1 checker functions stay frozen for reading that
> history […]

**Half of it is already false at the subject.** Round `CORE-SET-CODE` item G (`56d1b17`,
2026-08-27) deleted the version-1 package leg — `member`, `freeze_package`,
`package_digest`, `members_by_role`, `check_package`, `verify_member_bytes`, `load_package`,
and `check_review_result` with them. `git grep -n -w` over `tooling` and `assurance` for
those names returns only prose (docstrings and comments naming them in the past tense); no
definition survives. Stated exactly, because the overstatement is the failure mode here: what
died is the package-checking leg, not every path by which a v1 result can be validated —
`review.py:71` still registers `"review_result": "review.schema.json#/$defs/reviewResult"`
and `validate_n2` still resolves it. The clause is false as to its checkers, not as to all
checking.

**Nothing in the repository records that.** `git grep -i "v1 checker function"` over the
whole tree returns **one** hit: the clause itself. No rider row, no decision entry, no plan,
no journal, no review record names it. The nearest record, rider `v1-digest-recipe`, ran its
sweep with a declared scope of the frozen schema pack and a per-name `git grep -w` — a shape
that structurally cannot reach a prose clause naming the functions as a category.

**The other half is what the round this read opens will delete.**
`document-harness/plans/v1-result-retire.plan.md` item C deletes
`schema/document-assurance-v3/review.schema.json`. The plan is careful about every adjacent
surface — ruling 8 decides `E2`'s clause and the guard's `ANNOUNCED` list are deliberately not
changed, item F re-points rider `announced-set-anchor`, item H redeems `v1-digest-recipe` —
and its Constraints record "No `E10` member is edited". That is true as a change-boundary
statement and it is not an adjudication: `git grep -n -E "REVIEW\.md|document-harness/README|13\.1"`
over the plan returns nothing, and its only contract-v4 mentions (`:171-172`, `:189`) say two
riders do not redeem because that surface is untouched.

**Sibling sites, because the class is what matters and not the instance (`E7`).** Sweeping
the nine members at the subject for `review\.schema\.json|v1 schema|pre-wave-2|pinned v1`
returns three sites the same deletion falsifies:

| site | what it says today | after item C |
|---|---|---|
| `contract/…-v4.md:286` | `review.schema.json` stays frozen for reading pinned v1 history | names a deleted file, in signed text |
| `document-harness/REVIEW.md:95-96` | "What reads pre-wave-2 history now is that history's own commits and the frozen v1 schema, which is untouched" | the second of the two named readers is gone |
| `document-harness/README.md:20` | links `[review](../schema/document-assurance-v3/review.schema.json)` in the V3-N2 row | dangling link on the layer's navigation surface |

Only the checker-functions half is false **today**; the three above are true at the subject
and become false when item C lands. That is why this is filed at the layer's opening rather
than banked: the moment it bites is inside the round this read opens.

**Why not wording-level under `R9`.** `R9`'s test asks for a nameable downstream decision. It
is nameable and it is due now: whether the deletion may land while a signed member says the
file stays. Contract §13 (`:268`) forbids amending signed contracts in place — "corrections
create a versioned successor" — so this is not a byte the free channel can apply, and
`HD-57` is the standing precedent that the alternative exists (a recorded user ruling
permitting in-place correction of signed-then-stale literals, five sites, 2026-08-23).

**Minimum, and the part that is not mine.** Before item C lands, the sentence is adjudicated
on the record. Precedent supports three shapes — a versioned successor under §13; a recorded
ruling permitting the in-place correction under the `HD-57` shape; or a recorded decision
that the clause stands as history of what was true when signed, with the two prose siblings
carrying the correction. Which one is the user's to choose (`R5`), and I do not choose it.
What I do assert is that closing the round without any of the three leaves a signed member
naming a file this repository no longer has, by the same silent route that already took the
clause's first half.

### `L-1` (low) — none of the three sites is visible to any instrument this repository runs

Measured against the guards themselves, not inferred:

- `layer_path_check.py` scans only backticked tokens (`TOKEN`, `:49`) and skips any token
  without a `/` (`:63`). Contract v4's `` `review.schema.json` `` is backticked and
  slash-less → skipped. README's path sits inside a markdown link, no backticks → skipped —
  which is the blind spot `E10`'s own clause already claims ("prose and markdown links carry
  no backtick token for it to find"). `REVIEW.md`'s sentence names no path at all.
- `test_readme_enumeration.py` asserts one direction only: `missing` is computed from
  `schema_dir.glob("*.schema.json")`, so it catches a schema file the README fails to name
  and stays green on a README naming a file that no longer exists. Its own docstring says it
  closed the decay class; it closed one direction of it.

So after item C the layer's staleness on this point is reachable by nothing but the next
read. Recorded as low rather than folded into `M-1` because its fix is a different object —
`M-1` is adjudication of a clause, this is the absence of any mechanical backstop — and
because `E6` says a fix needing new machinery is a signal to re-question the guarded thing,
which makes "add a reverse-direction guard" a design question and not this read's to
prescribe.

## 3. Observations

- `O-1` — `schema/document-assurance-v3/paragraph-map.schema.json:5` says the file "is part
  of the **E2-frozen surface** as of the 2026-08-03 re-baseline". Item A's commit body ran a
  sweep for live text asserting `E2` forbids a write, cleared four sites that use
  *frozen* as a name (`CONSTRUCTION-INDEX.md:27-28`, `io-design.md:112`,
  `split-travel-manifest.md:51,56`, `test_candidate_checks.py:1726`), and named two sites its
  rewrite falsified. This member is in neither list — its wording matches none of that
  sweep's grep patterns. Under `E2`'s bridging sentence the site reads true, so no action
  changes; what is lost is the distinction that commit body deliberately preserved, between
  checked-and-clean and never-looked-at, for a site inside the layer itself.
- `O-2` — `README.md:22`'s "added as the tenth member 2026-08-18" is still there. It was
  reported by `v3-cold-read-b737742.md` `O-3`, routed under `R9`'s terminal branch, and rider
  `r9-terminal-no-carrier` records that the round which did touch that member left the bytes
  unchanged with no carrier anywhere. Re-observed here so the second cycle is on the record
  rather than the routing silently absorbing it again. The statement is true as dated history;
  `E10`'s membership sentence remains the only authority on the count, and it reads nine.
- `O-3` — rider `e10-freeze-exception` is accurate and still open: `CONSTRUCTION-CHECKLIST.md:185`
  reads "the bytes `E2` freezes are excepted while they are frozen", and `E2` since `184387c`
  says *frozen* is a name and never a prohibition. The queued plan decides explicitly that the
  row does not fall due this round. Confirmed present; nothing to add.
- `O-4` — checked and clean, so the next reader can tell it from never-looked-at:
  `layer_path_check.py`'s `LAYER` tuple is the same nine paths as `E10`'s sentence, in the same
  order (the `E10-sync` prose leg, verified by eye at this subject);
  `E2`'s "fifteen files" matches `ls schema/document-assurance-v3/` (15) and README's three
  enumeration rows (8 + 2 + 4 + 1 = 15); `ORCHESTRATION.md`'s "nine obligations already law
  elsewhere" table has nine rows and its three own-text sections make the twelve README:22
  claims; `EXECUTION.md`'s six run-template sections are all present, and the doc paths its
  tiering exception names are real — `document-harness/templates/` holds exactly the two
  instance templates, `__init__.py:41` pins the contract path, and
  `tooling/tests/document_harness/test_readme_enumeration.py` exists;
  my charter stub's own claim checks out — `dispatch.py:548-549` hard-codes that path as
  `CONSTRUCTION_ROLE_INSTRUCTION`, and `test_dispatch.py:398/:463/:522` pins it in hand-written
  constants; the checklist header's pointer resolves —
  `CONSTRUCTION-LEDGER.md:32-35` names the extraction-source repository as a single-machine
  worktree path.

## 4. Coverage and ceilings (`R4`)

- **Read in full**: all nine members; `HARNESS-DECISIONS.md` `§live` (lines 30–180);
  `HARNESS-RIDERS.md`; `tooling/hooks/layer_path_check.py`; `.githooks/pre-commit`.
- **Sampled**: `document-harness/plans/v1-result-retire.plan.md` (rulings, measured-state,
  constraints, out-of-scope, items C–H, notes, resume pointer — not the whole file);
  `tooling/rsclib/document_harness/review.py` (header and definition list);
  `tooling/tests/document_harness/test_readme_enumeration.py` (docstring and the assertion).
- **Probed by command only**: `dispatch.py` and the test files named in `O-4`, via grep;
  the schema pack, via directory listing.
- **Not done**: no test suite was run, and nothing was mutation-tested. `L-1`'s two claims
  rest on reading the guard's own predicates (`TOKEN`/`PATHLIKE`/the `missing` comprehension),
  not on a red-then-green demonstration; a reader wanting binding force should demand the
  mutation.
- **Process claims are marked, not verified** — that this session started cold and read
  nothing of the round it opens beyond what is committed is a declaration with no evidence
  lock. What is checkable is that every fact above cites a command or a committed byte.
- `M-1` deliberately supplies no bytes. Both live fix shapes touch signed text, and choosing
  between them is `R5`'s question, not a wording the reader may pre-empt.
