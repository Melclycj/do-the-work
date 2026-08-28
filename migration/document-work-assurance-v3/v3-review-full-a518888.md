# FULL review — subject `60bf9ebc735f9df011913dd652843f1ba3920f48..a5188887a9d1e148fc5d9461f672052e521bb287`

**Verdict: `REVIEWED_NO_BLOCKER`.** No blocking discrepancy found within the subject and the
review dimensions below. Three low findings and four observations follow; none is inflated to a
blocker, because none of them requires a code change to make the round's own claims true — the
one that touches an evidence claim is answered by citing evidence the round already produced.

Read this verdict against §6: **this session could execute no Python.** The battery, the two
guards, the three mutations and the acceptance-2 one-liner were all run by the orchestrator and
are reported here as *marked process claims*, never as my measurements (`R4`).

Dispatched with the charter `migration/document-work-assurance-v3/v3-harness-review-contract.md`,
a stub whose named successor `document-harness/CONSTRUCTION-CHECKLIST.md` I read in full as both
the standing instruction and its own counterpart, per that stub's own opening line.

---

## 1. What I derived from the repository, not from the dispatch (`R2`)

The dispatch handed me one range and nothing else. Everything below was re-derived here.

| question | answer | how |
|---|---|---|
| round | `V1-RESULT-RETIRE` | every commit title in the range carries it; plan `document-harness/plans/v1-result-retire.plan.md` |
| what the round is | the version-1 review schema is retired and its five shared `$defs` rehoused in `common.schema.json` | plan Goal, items A–H |
| base | `60bf9eb` — corrected forward from `e755d61` by user ruling 2026-08-28 | plan status block; the range's own base agrees |
| this event | the **FULL** of `E9`'s budget (plan step 8) | no valid independent FULL has occurred; the three review-side events in range are `E10` reads |
| budget state | **intact** — one FULL, one user-approved fix, one VERIFY, none consumed | `E9`'s test: no FULL had occurred, so all fifteen commits are pre-submission corrections, records, rulings or `E10`-channel amendments |
| authorization | nine user rulings carried by the plan (`:46-80`); `HD-63` (`01753f4`); `HD-64` (`4a380be`) | all committed — I found **no chat-only load-bearing material** |
| obligations | `E1`–`E12` execution side, `R1`–`R10` review side (`CONSTRUCTION-CHECKLIST.md`) | read in full |
| report channel | this file, `R6` name form, tip sha | matches the 60-odd sibling records |

Commands, output rather than description:

```
$ git rev-list --count 60bf9eb..a5188887
15
$ git diff --stat 60bf9eb a5188887
 19 files changed, 1455 insertions(+), 425 deletions(-)
$ git rev-parse HEAD
a5188887a9d1e148fc5d9461f672052e521bb287
$ git status --porcelain
?? .goals/
```

`.harness/review-pending.json` names this exact range, dispatched `2026-08-28T14:32:13+00:00`;
`HEAD` is the range's tip, so the branch has taken no commit since dispatch, as `E9` requires.
The last commit in range, `a518888`, is dated `2026-08-28T14:29Z` — three minutes before the
dispatch, not after it.

**Changed paths, classified by hand** (19 files; I did not accept the diffstat's grouping):

- *Schema pack, all three announced*: `common.schema.json` (+the five definitions), `review.v2.schema.json` (five `$ref`s + two description sites), `review.schema.json` (**deleted**, 347 lines).
- *Code*: `tooling/rsclib/document_harness/review.py`, `.../review_result_v2.py`.
- *Tests*: `test_flow_repair_disposition.py`, `test_golden_review_views.py`, `test_fix_round_locks.py`.
- *Instruction layer (`E10` members)*: `contract/Document-Work-Assurance-Contract-v4.md`, `document-harness/README.md`, `document-harness/REVIEW.md`.
- *Registers and records*: `HARNESS-DECISIONS.md`, `HARNESS-RIDERS.md`, `CONTRACT-V4-SIGNATURE.md`, `CONSTRUCTION-LEDGER.md`, the plan, and three read records under `migration/`.

---

## 2. The implementation — does it do what it claims, and do the guards bind (`R3`)

### 2.1 Item A — the move is byte-equal, and I re-derived it rather than reading the claim

The commit body and the plan's acceptance 3 both claim the five definitions moved byte-equal
with exactly one character of difference. Re-derived here, extracting both blocks mechanically
rather than by eye:

```
$ git show 60bf9eb:schema/document-assurance-v3/review.schema.json > old.json
$ sed -n '85,88p;131,257p' old.json > old_block.txt          # 131 lines
$ sed -n '142,272p' schema/document-assurance-v3/common.schema.json > new_block.txt   # 131 lines
$ git diff --no-index old_block.txt new_block.txt
@@ -128,4 +128,4 @@
         }
       },
       "description": "Required on a VERIFY result, absent on a FULL. ..."
-    },
+    }
```

One line, one character: the trailing comma on `verifyScope`'s closing brace, which is `$defs`'
separator and not part of any definition. The extraction ranges are the right ones — the base
file's `$defs` keys sit at `:85 reviewRound`, `:89 memberRole`, `:102 packageMember`,
`:131 instructionCompleteness`, `:164 perObligationDisposition`, `:195 finding`,
`:235 verifyScope`, `:258 reviewResult`, so `85-88` + `131-257` is exactly the five and nothing
else, and `memberRole` / `packageMember` / `reviewResult` are excluded rather than smuggled.
**Acceptance 3 holds in the precise sense the executor stated it, and I confirm the qualification
was necessary rather than defensive.**

`common.schema.json` now holds 25 top-level `$defs` (20 before, none of the five colliding), and
the plan's Out-of-scope requirement — that nothing about what the five *say* changed, so the diff
cannot show a move and hide an edit inside it — is met by the above.

### 2.2 Item B — the re-point, and whether it actually resolves

All five `$ref`s in `review.v2.schema.json` (`:29 :35 :40 :47 :56`) now name
`common.schema.json#/$defs/…`. Sweeping every cross-file `$ref` in the whole pack, **every one
of them targets `common.schema.json` and not one targets the retired file** — so no reference
dangles anywhere, not merely in the successor.

Resolution is structurally sound and I established it from the registries rather than the prose:
`review_subject._w2_registry` (`:81-88`) builds from `SCHEMA_FILES` + `N2_SCHEMA_FILES` +
`W2_SCHEMA_FILES`, and `common.schema.json` reaches it through the first
(`__init__.py:48 "common": "common.schema.json"`), which `review._n2_registry` and the package
root's `_registry` also load. The moved definitions' own internal `$ref`s — `slug`,
`frozenFileRef`, `locator` — still name `common.schema.json` and now resolve to the file they
live in, whose `$id` is `researchsystem/schema/document-assurance-v3/common.schema.json`, the key
the registry is built under.

**That the five actually resolve at validation time is established by the battery, not by the
acceptance the round cites for it.** See `L-1`.

### 2.3 Item C — the deletion, and what still names the file

```
$ git ls-files schema/document-assurance-v3/ | (14 paths)
$ git ls-files schema/document-assurance-v3/review.schema.json
(empty)
```

Acceptance 1 confirmed by me. Sweeping the whole tracked tree for `review.schema.json`, excluding
`migration/`, `document-harness/journal/` and the archives, **nothing resolves the file as a
schema**. The live hits are: the guard's `ANNOUNCED` list (`announced_path_disclosure.py:70`) and
its hand-written test twin (`:33`, `:67`) — item E, deliberate; `review.py:11` — the standing
conclusion kept word for word with its forward correction beside it at `:20-31`; two test
comments; `review.v2.schema.json:5`; `contract/…-v4.md:302` — past-tense history; and the
registers and closed plans, which `HD-59` corrects forward rather than rewrites.

The README second site landed where the plan and the third read said it had to — **inside the
deletion commit**, not before it (`test_readme_enumeration.py:37-53` builds `stems` from
`schema_dir.glob`, so removing the name early turns it red) and not after (removing the file
while the name stands turns nothing red). I checked the enumeration by hand: 14 stems on disk, 14
named across the four table rows, `[review.v2]` present as a link token. The row's own
parenthetical explains why the retired stem is written in neither delimiter — a real trap, since
either form would satisfy that guard in advance for a file that no longer exists.

`E10` members resolve **9/9** — checked by `git ls-files` over `E10`'s own membership sentence,
and `layer_path_check.py:37-47`'s `LAYER` is those same nine paths in the same order, so
`E10-sync` did not fall due.

### 2.4 Item D — the code stops knowing, and the fail-closed claim

`N2_SCHEMA_FILES` and `N2_SCHEMA_POINTERS` lose both v1 entries (`review.py:77-84`); an
unregistered kind reaches `_n2_validator`'s final branch and raises `SpecGap`
(`review.py:108`), so `validate_n2("review_result", …)` and `validate_n2("review_package", …)`
now stop. `check_review_result_v2` refuses any kind that is not `review_result_v2` with a message
naming why (`review_result_v2.py:120-126`). `review.py`'s header paragraph is corrected forward
under `HD-59` with the original left standing word for word, and it names how each of the two
grounds was *removed* rather than found wrong — the honest shape.

The executor decision `HD-64` routed here is made and disclosed: `result_schema_kind` keeps
classifying and the stop is raised downstream. Its docstring's caller census is accurate — I
re-derived it: `git grep -n result_schema_kind -- tooling` returns two package callers
(`review_result_v2.py:120`, `flow.py:333`) plus `test_review_v2_subject.py:237 :238 :244`, which
is what `review_result_v2.py:23-25` says after the earlier draft's wrong figure was corrected in
the bytes before they landed. `cli.py:320` computes its kind from the document, so no
command-line path presents a v1 result. See `O-1` for the one place the amended contract text
reaches further than the code does.

### 2.5 The tests — re-points, and whether coverage shrank

Five `validate_n2("review_result", …)` sites became `validate_w2("review_result_v2",
as_v2_review(…))`. I checked each against `review.v2.schema.json` rather than against the commit
body: the successor carries the same `reviewRound` enum (now via `common`), the same
VERIFY-narrowing `allOf`, the same FULL-has-no-`verify_scope` `allOf`, and the same
CHANGES_REQUIRED-requires-findings `allOf` — so `:1148-1160` (a `VERIFY` returning
`CHANGES_REQUIRED`, and a third `RE_VERIFY` round) and `:1984-1990` (a FULL declaring
`verify_scope`) pin the same properties they pinned before. `as_v2_review` moved up beside
`make_review` with a paragraph saying why; it is now the only route from this file's fixture to a
schema that exists. `test_review_v2_subject.py:237` is deliberately *not* re-pointed, which is
right: it pins the classifier, and changing it would have been the other item-D landing arriving
through a test.

`N2_SCHEMA_FILENAMES` (`:1898-1903`) replaces the retired file with **both** files that hold what
it held, rather than dropping it — which is the correct call and the one the plan's letter did not
require. Dropping it alone would have taken the whole review surface out of an N2-A11 property
scan that reads no other file naming a verdict, a finding or a disposition: the silent-shrink
shape this round exists to close, reappearing inside the round's own diff. The widening pulls
`common.schema.json`'s N0 vocabulary into that scan incidentally; I checked its property names and
enum values against the banned set and against
`test_candidate_checks.py:1589-1611`'s V3-N0 forbidden list, and nothing matches.

`TheClosedReviewSurface` re-points to two loaders and walks both documents; its two
reached-the-leaves assertions (`residual_uncertainty` as a name, `REVIEWED_NO_BLOCKER` as a value)
still land in `review.v2.schema.json`, so the scan is not silently walking an empty tree.

### 2.6 Item G — the guards the round adds, and whether they bind

Three new tests:

1. `test_the_registered_kinds_are_exactly_the_hand_written_set` — `EXPECTED_N2_KINDS` is a
   hand-written frozenset never read back from the module, which is `E5` observed rather than
   cited. It closes the real F4 shape: `test_every_n2_kind_resolves_to_a_real_schema` iterates the
   very tables it checks, so a table losing an entry loses the assertion with it. Landing this in
   the same commit as the table shrink is correct — a guard added after the change it was made
   urgent by would not have guarded it.
2. `test_the_retired_version_1_kinds_no_longer_resolve` — asserts both retired kinds raise. See
   `L-3`: this is the one new guard nobody has seen fail.
3. `test_the_no_code_listing_stays_true` — asserts `N2_MODULES_WITHOUT_CODES`' own precondition
   rather than adding a second sweep, which is `E6` answered rather than invoked, and it carries
   its negative control *inside itself*: `flow.py` must match both patterns before the exclusion
   list is judged clean, so a regex that had stopped matching could not report the list as empty.
   `PREFIX_PATTERN` is anchored at line start, so `review_result_v2.py`'s `RESULT_CODE` does not
   match it — and that module is in `SUCCESSOR_ROUND_MODULES` with its own sweep, so nothing falls
   between the two.

The two mutations the plan's acceptances 7 and 8 demand were run by the orchestrator and are
reported at `a518888` with the failure messages and a sha256-checked restore. I could not re-run
them (§6). `git status` is clean at the tip, which is consistent with the restore having worked
but does not establish that the mutations fired.

---

## 3. Findings

### `L-1` (low) — acceptance 2 is cited as what proves the `$ref`s resolve, and it is the one command that cannot prove it

**Location.** `document-harness/plans/v1-result-retire.plan.md:407-410` (Acceptance 2) and
`:370` (the measured result), plus `1f3e213`'s orchestrator addendum, which calls it *"the command
that settles what these bodies could only read"*.

**The claim.** Running
`validate_w2('review_result_v2', {})` and seeing it print `False` is said to prove the five
re-pointed `$ref`s resolve from `common.schema.json`, on the stated reasoning that *"an
unresolved-reference error would have raised instead"*.

**Why it does not.** The instance is `{}`. `jsonschema` resolves `$ref` lazily, at the moment a
subschema is applied. For an empty object: `required` yields eleven errors on its own, which is
the whole of why `ok` is `False`; `properties` applies a subschema only for keys present in the
instance, and there are none, so none of the five `$ref`s under `properties` is ever looked up;
each `allOf` member is an `if`/`then` whose `if` requires `review_round` or `verdict` and
therefore fails, so no `then` is descended into either; and `check_schema` validates the document
against the metaschema, which treats `$ref` as an opaque string. `False` is thus the answer a
correct re-point and a broken one both produce — which the plan half-notices when it records that
the same command already printed `False` **before** the round, at `c6454d3`.

**Ground truth.** `E3` — a characterization no command established is dropped, not softened; a
figure or a proof is emitted from the command that produces it.

**What is not in doubt.** The property itself holds, established by evidence the round already
produced: `test_flow_repair_disposition.py:556-565` validates two fully-populated v2 results and
expects zero codes, and `:1980-1990` puts `verify_scope` on a FULL — between them all five
`$ref`s are looked up, and an unresolvable one would raise rather than report. The 830-passing
battery therefore carries the claim. **This is a defect in which evidence was cited, not in the
schemas.**

**Minimum fix.** Re-point acceptance 2 at the assertions that exercise a populated instance, or
replace its one-liner with one that supplies the five fields. No schema or code change.

**Ceiling.** Established by reading `jsonschema`'s keyword semantics, **not by execution** — I
could reach no interpreter. The experiment that settles it: point one `$ref` in
`review.v2.schema.json` at a nonexistent file and re-run acceptance 2. My claim is that it still
prints `False`.

### `L-2` (low) — both of the round's designated cold-resume surfaces state a blocked state the tip has left behind

**Location.** `document-harness/plans/v1-result-retire.plan.md:438` — *当前指针: **step 4, with
items C and D held back***; `:447-450` — *Owed before items C and D: the independent re-read of
the second amendment*; `:452` — *Battery at `2aabd5a` is **827 passed***. And
`CONSTRUCTION-LEDGER.md:175` — ***item C 仍等该通道的另一半——对被改文本的独立复读***.

**At the subject all four are false.** Items C and D landed at `1f3e213`; the owed re-read landed
at `ff00a1d` (`migration/document-work-assurance-v3/v3-cold-read-006138e.md`); the battery is 830,
which the *same file* records at `:373`. The plan's Steps list at `:353-358` ticks steps 4–7 with
their commits, so the file contradicts itself.

**Why it is a finding and not bookkeeping.** The plan's own status block at `:38` names these two
as the entry point — *"A cold session reads this file, then `CONSTRUCTION-LEDGER.md`'s current
pointer, then works"* — so the stale text sits exactly where a cold session is told to start, and
both carriers say the same wrong thing rather than one correcting the other. The round has already
paid this once: `006138e` exists solely because the second amendment's executor caught the same
pointer naming the *first* amendment's re-read as what was owed.

**Ground truth.** `E3` — a figure is invalidated by any later change to what it measures.

**Minimum fix.** Refresh both at closeout. Plan step 9 already owns the ledger; the plan's resume
pointer and its `827` figure ride the same commit. **This does not need the fix leg.**

### `L-3` (low) — one of the three guards this round adds has never been seen to fail

**Location.** `tooling/tests/document_harness_review/test_golden_review_views.py:243-255`,
`test_the_retired_version_1_kinds_no_longer_resolve`.

**The gap.** The plan's acceptances 7 and 8 name mutations for the other two new tests, and
`a518888` reports both firing with their messages. This one gets only the negative-control line
at `:382-385`, which records it **passing** on the untouched tree. That is the vacuity control,
not the must-fire demonstration — and its docstring's stated control
(`test_every_n2_kind_resolves_to_a_real_schema`) likewise proves the validator does not raise for
everything, which is again the vacuity direction.

**Ground truth.** `E4` — *"Never trust a guard you have not seen fail: mutation-test every new
guard"*, unqualified.

**Minimum fix.** Re-add one retired kind and watch it go red, restoring from a sha256-checked
scratchpad copy. Worth noting for whoever runs it that the two available shapes fail differently
and both should turn it red: adding `review_result` back to `N2_SCHEMA_POINTERS` reaches
`Unresolvable` at lookup time (the file is gone but the registry never tries to load it), while
adding it to `N2_SCHEMA_FILES` reaches `_n2_registry`'s `AssuranceFault` missing-schema branch.
Neither is `SpecGap`, so `assertRaises(SpecGap)` fails either way — which is the demonstration
this test is owed and has not had.

**Severity.** Low rather than blocking: the assertion cannot pass vacuously, since `assertRaises`
fails when nothing raises.

---

## 4. Observations (`R5` — the question and the conclusion are the user's)

- **`O-1` — the amended contract clause's "not accepted" half has no enforcement site, and one
  production path reads a v1-shaped result and reports clean.**
  `contract/Document-Work-Assurance-Contract-v4.md:280-287`, written at `2aabd5a`, says a result
  with no `schema_version` key *"is not validated and not accepted, fail closed"*. The *not
  validated* half holds everywhere I checked. The *not accepted* half does not reach
  `flow.reviewed_candidate_ref` (`flow.py:333-336`), which falls through to the root
  `candidate_ref` for such a result, nor `flow.check_repair_decision`, which is exported at
  `flow.py:760`, is driven through the real function by the run-v2 repair template
  (`test_run_v2_template_repair.py:353-361`), and returns a **clean** report over a v1-shaped
  result — pinned as live behaviour by
  `test_flow_repair_disposition.py:885-888` (`test_the_v1_root_shape_is_unaffected`).
  `review_result_v2.py:33-39` discloses precisely this and argues §13.1 does not reach an
  accessor, and names the pre-existing gap that `check_repair_decision` reads a result it never
  validates. I record rather than file it because: the behaviour is unchanged by this round; the
  class is empty by the user's own ruling (plan ruling 2), so the clause is counterfactual; and
  whether *not accepted* was meant to bind a decision-binding check or only a validator is the
  user's to say, not mine. It is worth deciding at closeout because `HD-64` made
  contract-text-agrees-with-code an explicit condition of its own execution.
- **`O-2` — one clause of the new README row is arguably wrong, and by `R9` it banks.**
  `document-harness/README.md:20` says the five definitions moved into `common` *"which is where
  this row's remaining entries reach them"*. The row's remaining entries are `review.v2`,
  `assurance` and `harness-issue`; only `review.v2` references any of the five, which this round
  measures three times and writes into both schemas' own descriptions as *"this file is their only
  referent"*. Read with *them* bound loosely to shared definitions generally the sentence is true;
  read with *them* bound to the five it is not. No check outcome, evidence binding, permission,
  obligation or verdict path changes either way, and the accurate fact sits in
  `common.schema.json:5` and `review.v2.schema.json:5`. I can name **no** downstream decision that
  goes wrong, so by `R9` it rides the next batch touching this member and spawns no round and no
  read.
- **`O-3` — item C edited an `E10` member inside a candidate commit, and the body records one of
  the two facts the deferral proviso asks for.** `1f3e213` removes `README.md`'s version-1 row and
  its body records that the edit adds no clause and changes no rule's requirement — under the
  `E10-sync` rider heading rather than under `E10`'s amendment clause. It does not state that the
  effect on every round in flight is nil, nor that the bytes ride the next read of this layer. On
  my reading the deferral proviso is not the governing sentence, because nothing in the round
  *relies* on that row in `E10`'s sense (an outcome that would change if the text changed), so
  only the ordinary next-opening read is owed and the next cold read will see the blob move
  regardless. Recorded so the closeout decides this rather than inherits it.
- **`O-4` — the two-paragraph commit body is new in this round and is not disclosed as a
  departure.** `E8` says *"one dense paragraph, no trailers"*. Five commits in range carry a
  second paragraph, the orchestrator addendum. `git log --grep='Orchestrator addendum' --all`
  returns exactly those five — `e578e70`, `aa8d212`, `2aabd5a`, `1f3e213`, `57e1f23` — and no
  earlier commit in this repository, so the shape originates here. The addendum is disclosure this
  review benefited from and I am not asking for it to go; what is absent is any sentence saying it
  departs from `E8`'s letter, or a ruling admitting the form. Routed to the user.

**Not re-filed, confirmed present and routed.** The round's own disclosure that the orchestrator
is carrying the verification half of `E1`'s execution side — because a dispatched cold executor on
this machine can run neither `python` nor a `git` write, now measured four times counting this
session — is stated at `006138e` and in the plan's Notes, banked at closeout against
`ORCHESTRATION.md`'s three-roles table with the `R10` constraint that its fix is design. `HD-55`'s
split holds on the record: every work commit states that the orchestrator edited no byte of the
executor's work. Nothing added.

**On `R5`'s shape question.** This round added three tests to close blind spots. That is the
pattern `R5` asks me to report when successive rounds keep adding components — but here the `E6`
question was asked and answered in the bytes rather than skipped: item G explicitly refused a
second sweep in favour of asserting the existing exclusion list's own precondition, and item D
refused new machinery in `result_schema_kind`. I record it as sound rather than as the shape.

---

## 5. Process and record conformance — the boundary check, run second (`R3`)

- **`E2`.** Three commits touch announced paths and each names every one in full repo-relative
  form in its own body: `e578e70` (`contract/Document-Work-Assurance-Contract-v4.md`,
  `schema/document-assurance-v3/review.v2.schema.json`), `2aabd5a` (contract v4), `1f3e213`
  (`common.schema.json`, `review.v2.schema.json`, `review.schema.json` **as a deletion**). No
  other commit in range touches one. Checked against `git log --name-status`, not against the
  bodies' own lists.
- **`E9`.** Budget intact — see §1. The review-window rule held for all three reads: each record
  commit is the immediate successor of its subject (`60bf9eb`→`c04958a`, `dcb3aef`→`fad8df2`,
  `006138e`→`ff00a1d`), so the branch took no commit between dispatch and record.
- **`E10`.** The opening cold read is on the record (`c04958a`); `HARNESS-DECISIONS.md` `§live` was
  read at that opening as the clause requires. Two must-fix findings were raised and answered, each
  by a committed user ruling plus an amendment plus an independent re-read — `HD-63`/`e578e70`/
  `fad8df2`, then `HD-64`/`2aabd5a`/`ff00a1d` — and neither pair is a round nor spends budget. One
  free-channel byte application (`aa8d212`) applied exactly the bytes its record supplied, in its
  own commit, and its owed read is discharged by `ff00a1d`. The design test: the round edits four
  members and none of the edits adds a clause; the one that *does* change a requirement, the
  §13.1 first bullet, opens no round only because `HD-64` says so in as many words, records that
  set-aside as a cost, and refuses it any extension. That is `§live` outranking the layer, which
  `E10` itself concedes — legitimate, and the second consecutive round to lean on it.
- **`E8`.** Titles are `V3-<ROUND>-<part>-v1` throughout, the established form in this repository's
  history. Each body names its kind — candidate / amendment / ruling / record / pre-submission
  correction. No trailers. Staged path sets match the bodies' enumerations exactly. Paragraph count
  is `O-4`.
- **`R10` / riders.** `v1-digest-recipe` and `alarm-yaml-untested` are gone from
  `HARNESS-RIDERS.md`, each riding the commit that earned it rather than a bookkeeping commit of
  its own — the departure from the plan's expected two commits is disclosed in `1f3e213`'s body and
  serves what acceptance 10 protects. `announced-set-anchor` survives with a touch record naming
  this round, its falsified measurement left standing under `HD-59` with the new numbers beside it,
  and redeem-when re-pointed at *the next round that opens as design* — a surface that may open a
  round, as `R10` requires of a design-shaped fix. The new row `alarm-yaml-range-untested` carries
  only the residue its predecessor's redemption left, names its target lines, and its deadline
  falls outside the round that wrote it. `sig-write-once`, `contract-wikilink-tier`,
  `e10-freeze-exception`, `e10-cannot-see`, `PD`, `E10-sync` and `alarm-mutation-gaps` are each
  addressed explicitly as not falling due, which is what the plan's Constraints asked for.
- **`E1` / `HD-55`.** Orchestrator, executor and reviewer are separate sessions; the four `R1`
  holdings — dispatched by, prompted by, scoped by, reported through — are the orchestrator's, so
  the independence of this review is structural. The round does not stand in `E1`'s exception
  channel and does not claim to.

---

## 6. Coverage and ceilings (`R4`)

- **Read in full**: `CONSTRUCTION-CHECKLIST.md`; the round plan; `HARNESS-RIDERS.md`;
  `schema/document-assurance-v3/review.v2.schema.json`; `migration/…/v3-cold-read-006138e.md`;
  `tooling/tests/document_harness/test_readme_enumeration.py`; the full commit bodies of
  `1f3e213`, `57e1f23`, `e578e70`, `2aabd5a`, `4a380be`, `a518888`.
- **Read in part**: `common.schema.json` (`:1-20`, `:110-170`, and the whole moved block via the
  mechanical extraction above); `review.py:1-146`; `review_result_v2.py:1-150`;
  `flow.py:320-364`; `test_golden_review_views.py:190-407`; `test_fix_round_locks.py:225-430`;
  `test_flow_repair_disposition.py` at the changed sites and `:540-580`, `:840-905`, `:1850-1990`;
  `announced_path_disclosure.py:40-82`; `layer_path_check.py:25-90`;
  `test_candidate_checks.py:1585-1710`; `HARNESS-DECISIONS.md` at `HD-63`/`HD-64`;
  `CONTRACT-V4-SIGNATURE.md` and `CONSTRUCTION-LEDGER.md` at their diffs.
- **Probed by command only**: the range's commit list, count and diffstat; per-commit name-status;
  the schema-pack listing; the nine `E10` member paths; the byte-equality extraction and its
  `git diff --no-index`; every cross-file `$ref` in the pack; `review.schema.json` /
  `reviewResult` / `memberRole` / `packageMember` / `review_package` sweeps; `result_schema_kind`,
  `check_repair_decision`, `validate_n2` and `common.schema.json` call-site sweeps;
  `git log --grep='Orchestrator addendum' --all`; `git status`; `git rev-parse HEAD`.
- **NOT done — stated rather than softened.** **No test ran and nothing was mutation-tested in
  this session.** Every attempt to reach a Python interpreter beyond `python --version` was refused
  by this environment's permission layer, in the Bash tool and the PowerShell tool alike; a script
  written to the worktree and invoked as `python <file>` was refused too. This is the fourth
  measurement of the constraint the round records three times, and it now reaches the review side
  as well as the work side. Consequently:
  - `R8` is **not discharged**. I mutation-tested nothing. What I can say about the three new
    guards is that I read their predicates, their controls and their expectations, and that
    `EXPECTED_N2_KINDS` and `N2_MODULES_WITHOUT_CODES`' precondition are hand-written and
    independent of what they guard (`E5`). Whether the two mutations reported at `a518888` fired
    is **UNVERIFIABLE** here.
  - Acceptances 5, 7, 8, 11 and 12 are **UNVERIFIABLE** by me: the 830-passing battery, both
    mutations, `layer_path_check` / `ledger_cap_check` / `review_freeze_check` /
    `candidate_path_check` exiting 0, and the PR check. Reported as marked process claims.
  - Acceptance 2 I judge from reading rather than running, which is `L-1`.
  - Acceptances 1, 3, 4, 9, 10 and the `E10` 9/9 half of 11 I re-derived myself, above.
- **Process claims are marked, not verified.** That this session started cold, that the `E11`
  preview card was rendered and approved before the round opened, that the three executor sessions
  were separate `claude -p` sessions, and that the sha256 restore after each mutation was real, are
  declarations with no evidence lock available to me.
- **Not re-measured as if I could.** Plan ruling 2 — that no v1 ReviewResult instance exists
  anywhere — is a **user ruling, not a measurement**, and its own text says so. This repository can
  see only its own tree; I did not treat the local zero as confirmation of the wider claim, and the
  contract text correctly attributes it as a ruling rather than asserting it as measured fact.
- **Nothing in this record is self-applying.** `L-1`, `L-2` and `L-3` each name a minimum fix but
  supply no bytes for the instruction layer, and none of them takes `E10`'s free channel.
- **Worktree left as found.** I created four scratch files in the repository root to perform the
  byte-equality extraction — the interpreter being unreachable, `sed` and `git diff --no-index`
  were the only mechanical route — and deleted all four. `git status --porcelain` returns
  `?? .goals/` before and after, untracked and outside the subject.

---

## 7. What the orchestrator now owes

1. **Nothing is blocking.** No fix leg is required by this verdict.
2. Under `R10`, weigh the three lows before closeout rather than banking them by default. My
   reading: `L-2` rides step 9 and needs no fix leg; `L-1` is a one-sentence citation change that
   can ride the same commit; `L-3` is the only one that wants a command run, and it is a mutation
   plus a restore. Activating any of them as the round's one user-approved fix would oblige the
   VERIFY (`E9`'s test does not expire at closeout) — which is the trade to put to the user, not
   for me to decide.
3. `O-1` is worth an explicit decision at closeout, because `HD-64` made contract-text-agrees-with-
   code a condition of its own execution and the *not accepted* half reaches further than the code
   does.
4. The plan's `L-1` carried to closeout (`:389-398`) — the contract's present-tense *removes* — is
   **discharged by the tree**: items C and D landed, so the sentence is now true of tree state as
   well as of what the round does. The moment that finding named as biting has passed without
   biting.
