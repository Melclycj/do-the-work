# Instruction-layer read — subject `006138eb40448bb1a0fbd0aab55ca89288004f4d`

An `E10` read. Not a round: no budget spent, no verdict carried, output is findings tiered
must-fix / low / observation (`R3`). Dispatched with the charter
`migration/document-work-assurance-v3/v3-harness-review-contract.md`, a stub whose named
successor `document-harness/CONSTRUCTION-CHECKLIST.md` was read in full as both the standing
instruction and its own counterpart, per that file's own opening line.

This read carries three jobs on one subject. It is the layer's cold read at the subject commit;
it is the **independent re-read of the amended text** that `E10`'s must-fix channel owes for the
second amendment `2aabd5a` — the pair that answers `M-1` of `v3-cold-read-dcb3aef.md`; and it is
the **independent read the free channel owes** for the byte application `aa8d212`, which
`E10` says rides the next read of this layer at per-member digest cost. Both owed reads are
discharged here, over members read end to end rather than at digest cost.

Record name: `v3-cold-read-`. `R6` offers two read filenames and the layer still defines no
criterion for choosing between them (rider `read-name-split`, not closed here). I took
`cold-read` for the reason the two previous records took it — the subject is the whole layer,
read end to end.

## 1. The member set, derived — not received

The dispatch enumerated nothing. `E10`'s own sentence at the subject does, and reads **exactly
nine paths**. All nine resolve at the subject commit; blob ids from
`git rev-parse 006138eb…:<path>`, run here:

| # | member | blob at `006138e` | vs `dcb3aef` |
|---|---|---|---|
| 1 | `document-harness/CONSTRUCTION-CHECKLIST.md` | `5f77c3fdbc0f5fc5a04516a044292d9f35885068` | same |
| 2 | `document-harness/README.md` | `a9c388ca0e55c76991db863d08c83e4e29d99a50` | same |
| 3 | `document-harness/EXECUTION.md` | `234fdddf974e580d22a1a26b54587d11c24863b3` | same |
| 4 | `document-harness/REVIEW.md` | `13f91419df0eaf607b5b15b8b6fe5c7e0369c775` | **moved** (`444d9d29…`) |
| 5 | `document-harness/ORCHESTRATION.md` | `a9e9f75e484f40f4a1014e5d68ed6c73aa5fbdc2` | same |
| 6 | `migration/document-work-assurance-v3/v3-harness-operating-contract.md` | `6d5714923870b4e13e8928221a80df68e563a5ed` | same |
| 7 | `migration/document-work-assurance-v3/v3-harness-review-contract.md` | `29bdc9fbde6e8db38d601dd2340d4b46a24a296f` | same |
| 8 | `contract/Document-Work-Assurance-Contract-v4.md` | `a90c90fde879039f6b0a7d8ca7917e6a06482117` | **moved** (`1df7b8de…`) |
| 9 | `schema/document-assurance-v3/paragraph-map.schema.json` | `09aa869962f592c2f86c9379be0ef3eb7d2232ff` | same |

`git rev-parse HEAD` returns the subject and `git status --porcelain` returns only `?? .goals/`,
untracked and outside the layer, so the worktree bytes I read are these blobs.

`HARNESS-DECISIONS.md` is not a member and is cited by section, never by blob; its `§live` —
lines 30–258, **ten** entries: `HD-64`, `HD-63`, `HD-62`, `HD-59`, `HD-41`, `HD-36`, `HD-35`,
`HD-34`, `HD-23`, `HD-9` — was read in full, as `E10` requires at an opening whether or not the
layer read itself is waived. `HD-64` is new since the previous read and is the authorisation the
second amendment travels on.

**What moved since the last recorded end-to-end read.** That read is `v3-cold-read-dcb3aef.md`.
`git diff --stat dcb3aef 006138e --` over the nine returns two files:

```
 contract/Document-Work-Assurance-Contract-v4.md | 21 +++++++++++++++++----
 document-harness/REVIEW.md                      |  2 +-
 2 files changed, 18 insertions(+), 5 deletions(-)
```

Those are exactly `2aabd5a`'s and `aa8d212`'s own diffstats over members.
`git log --oneline dcb3aef..006138e -- document-harness/ contract/ schema/ migration/` returns
four commits — `006138e`, `2aabd5a`, `aa8d212`, `fad8df2` — of which `006138e` touches
`document-harness/plans/` and `fad8df2` adds the previous read record, neither a member. I did
**not** rely on the citation channel: all nine were read end to end in this session regardless
of whether their blobs moved.

## 2. The two owed reads

### 2.1 The second amendment (`2aabd5a`, `E10` must-fix channel) — `M-1` is discharged

`M-1`'s minimum was: *before items C and D land, `:280-281` is adjudicated on the record.* It is.
`HD-64` (`4a380be`) is the recorded ruling, taken in the second of the three shapes that finding
named — a further recorded user ruling — and the choice among the three was the user's (`R5`),
not the executor's or mine. Checked site by site rather than against the amendment's prose:

- **Line drift.** `HD-64` cites the sentence as `:279-281`; the commit re-derived it as
  `:280-281` before writing. Confirmed against the pre-image: the amendment's hunk header is
  `@@ -277,10 +277,23 @@` and the removed sentence occupies pre-image lines 280–281. The
  post-write span `:280-296` the body states is also right — line 280 begins
  `in place of \`package_ref\`.` and line 296 ends `not the interpretation going forward.`
- **The requirement is gone and what replaced it is checkable.** `:280-287` now binds an outcome
  (not validated, not accepted, fail closed) and expressly leaves the mechanism to the
  implementation. The four preserved propositions — `"2"` selects v2, present-but-null or any
  other value is `SPEC_GAP`, fail closed, no cross-version fallback with the `_ABSENT` sentinel —
  survive the rewrite verbatim in substance. Confirmed against the diff.
- **`HD-64`'s consistency requirement — contract text must agree with the item D decision — is
  met under either candidate landing, and I established it from the code rather than the body.**
  `review_result_v2.py:53-55` returns the literal `"review_result"` for a key-absent instance;
  `check_review_result_v2:83-89` raises `SpecGap` on any kind that is not `review_result_v2`, so
  a v1 result presented to the v2 checker is refused before validation. The other landing —
  keep naming a kind that no longer resolves — reaches `_n2_validator:93-97`, whose final branch
  raises `SpecGap(f"unknown document kind: {kind}")`. Both are fail-closed, so the amended text
  forecloses neither, which is what it claims. Read, not executed; see §5.
- **The ground is committed, not chat-only (`R2`).** The claim that no v1 ReviewResult instance
  exists anywhere is plan ruling 2 at `document-harness/plans/v1-result-retire.plan.md:52`, and
  that ruling's own text marks itself *a ruling, not a measurement*, warning a re-measuring
  reviewer not to read the local zero as confirmation. The contract text attributes it as a
  ruling — *the user ruled on 2026-08-28* — rather than asserting it as measured fact. Correct
  attribution, and I did not re-measure it as if I could.
- **The second horn is closed, not left open.** `M-1` recorded an alternative reading that would
  have rescued the bullet untouched. `HD-64` declines it in as many words, and the amendment
  writes the declining into the contract at `:293-296` so it is not re-adopted later. Both halves
  of the finding are answered.
- **`E2`.** The commit stages three paths and its body names them; `git show --stat 2aabd5a`
  returns `CONTRACT-V4-SIGNATURE.md`, `HARNESS-DECISIONS.md`,
  `contract/Document-Work-Assurance-Contract-v4.md`. One is announced, it is named in full
  repo-relative form in the body, and no other announced path is touched — the schema pack is
  untouched by this commit.
- **`E10-sync` did not fall due.** The membership sentence is byte-unchanged (member 1's blob is
  unmoved), and `layer_path_check.py:37-47`'s `LAYER` is still the same nine paths in the same
  order. Verified by reading both.
- **Path shape.** Of the added lines, the backtick tokens are `package_ref`, `schema_version`,
  `SPEC_GAP`, `_ABSENT`, `V1-RESULT-RETIRE`, `HD-64` and `"2"`; none contains `/`, so
  `layer_path_check`'s `PATHLIKE` cannot reach any of them. Hand-derived from the diff, and it
  agrees with the orchestrator addendum's reported exit 0.

**The set-aside, recorded because signed text now rests on it.** `HD-64` rules that no design
round opens, against `E10`'s unqualified design sentence. That is `§live`'s to say and `§live`
outranks the layer on conflict, so the reliance is legitimate. `HD-64`'s own status line says the
layer carries not one word of the proposition that a user may rule a design change out of a
round, and I confirmed that: `E10`'s design sentence is unqualified and the tiebreak that follows
it limits itself to the free channel. This is the same shape `HD-36` has held open for cycles;
nothing here is new, and it is recorded because this is the second consecutive round to lean on
it and the first to lean on it for a **requirement**.

### 2.2 The free-channel application (`aa8d212`) — applied exactly as supplied

`git show --stat aa8d212` returns one file, `document-harness/REVIEW.md`, one insertion and one
deletion. The record's supplied bytes were *replace `and no working-tree artifact is kept to read
it` with `and no working-tree artifact is promised for that reading`*. `REVIEW.md:98` now reads
`carry the history, and no working-tree artifact is promised for that reading.*` — the exact
replacement, no more. The free-channel conditions hold as the commit states: the sentence adds no
clause and changes no rule's requirement, so the design test does not take it, and no round had
relied on it in `E10`'s sense. `HD-38`'s requirement that such bytes carry their own commit is
met — it is a separate commit from the amendment answering the same read. The independent read
this application owed is discharged by this record.

## 3. Findings

### `M-1` (must-fix) — item C deletes `review.schema.json`, and the one live reference to it inside the layer is a `README.md` link that no guard can see and the plan does not name

`document-harness/README.md:20` (member 2), the *Review + disposition schemas (V3-N2)* row,
carries a followable markdown link:

> `[review](../schema/document-assurance-v3/review.schema.json)`

**Scoped sweep, run here.** `review.schema.json` across the nine members at the subject returns
exactly two sites: this one, and `contract/Document-Work-Assurance-Contract-v4.md:302`. The
contract site is a past-tense historical statement — *Until 2026-08-28 this bullet promised
instead that `review.schema.json` and the v1 checker functions stay frozen* — which stays true
after the file is deleted, and is a backtick token with no `/`, outside `PATHLIKE` entirely. The
README link is the only live one. The class has one member and this is it.

**Nothing catches it.** I established each leg against the instrument rather than the prose:

1. `test_readme_enumeration.py:37-53` builds `stems` from `schema_dir.glob("*.schema.json")` and
   reports only stems the README fails to name. Delete the file and `review` leaves `stems`, so
   the assertion never looks at the README's naming of it. README:20's own sentence — *this entry
   leaves with the file, and it has to leave by hand, because that test catches a schema file this
   table fails to name and never a name whose file is gone* — is exactly right, and it is a
   warning nothing acts on.
2. `layer_path_check` cannot reach it twice over. It scans only the lines a commit adds
   (`added_lines_by_path`), and this line is standing text the deleting commit does not touch;
   and its `TOKEN` regex requires backticks, which a markdown link does not have. `E10`'s own
   *what the guard still cannot see* clause names both blind spots — *prose and markdown links
   carry no backtick token for it to find*, and *the standing text it never re-scans stays
   unscanned*.
3. The plan's acceptance 11 — *the `E10` members resolve 9/9* — is about the members' own paths,
   not about links inside them.

**The plan does not name the site, and its Constraints steer away from it.** Item C
(`document-harness/plans/v1-result-retire.plan.md:234-238`) names the deletion and nothing else;
`git grep README` over the plan returns two hits, at `:180` and `:324`, both records of what the
*first* amendment did, neither an item C site. Meanwhile the Constraints line at `:174` reads
**No `E10` member is edited (ruling 8)** — corrected forward at `:178-185` only to record the
amendment's three member edits, not to admit one for item C. An executor of item C following the
plan has an explicit instruction not to touch this file.

**One net exists and it is not enough to rely on.** Acceptance 4 greps `review.schema.json` over
`*.py`, `*.json` and `*.md` and admits only *the guard's list, its test twin, and historical
records*. README:20 is none of those, so a correct triage catches it — but the same executor is
reading a Constraints line telling it that no member is edited, which is a ready reason to
classify the hit as untouchable rather than as a defect. An acceptance step whose right answer
contradicts a Constraint is not a net I can report as holding.

**Why this may not wait.** Items C and D are unblocked the moment this record lands — that is
what `HD-64`'s consequences paragraph and the plan's resume pointer both say — and no further
read is owed before item C. The moment it bites is inside this round, which is the previous
read's own stated ground for filing at the opening rather than banking.

**Minimum fix, and it is not an amendment.** Before item C lands, the plan's item C site list
names `document-harness/README.md:20`, and the Constraints line is corrected forward (`HD-59`) to
admit that item C edits that member and to state why the edit is not design — removing a
navigation row adds no clause and changes no rule's requirement, so `E10`'s design test does not
reach it. The shape is already established in this round: `006138e` corrected the plan forward in
exactly this way when the same class was found at item D's site list. **I supply no bytes for
README:20 itself, deliberately**, because the edit cannot be made now — `review.schema.json` is
still in the tree at this subject, so removing its name today makes
`test_readme_enumeration.py` red. The correction belongs in item C's own commit, which is why the
thing to fix now is the plan that dispatches it.

### `L-1` (low, no bytes) — the amended bullet reports the removal in the present tense while the path it names is still in the tree, and neither authorisation reaches the correction that would then be owed

`contract/Document-Work-Assurance-Contract-v4.md:288-290`, added by the amendment:

> Round `V1-RESULT-RETIRE` removes that path on the strength of the same ruling — the
> requirement had no object left to act on.

At the subject the path is not removed: `review.py:71` still registers
`"review_result": "review.schema.json#/$defs/reviewResult"` and the file is still in
`schema/document-assurance-v3/` (15 files, `git ls-files` count unchanged). The sentence is true
read as a description of what the round does and false read as a report of tree state, and a
reader checking a clause checks the tree.

**Why it is low and not wording-level-only.** The accurate fact is recoverable from the plan and
the commit record, and the bullet's operative content — no validation path, fail closed — does
not depend on the removal having happened, so no actor's action changes today. What keeps it off
`R9`'s terminal branch is a nameable moment: **if this round closes without items C and D**, the
sentence stands in signed text as a false statement of fact, and the correction it would then
need has no channel. `HD-63` opens the in-place route for *a signed statement of fact that was
true when signed and has since been made false elsewhere*; this one was not true when written.
`HD-64` authorises *only this one bullet, only on this one ground* — the ground being that the
prescribed object does not exist, which is not this ground. So the correction would fall back to
§13's versioned-successor route for a tense.

**No bytes, on the previous read's reasoning.** Every live shape touches signed text, and which
of them applies is the user's (`R5`). Stating the exposure is mine; choosing between correcting
the tense now, letting items C and D make it true, or recording that the sentence is
round-relative, is not.

## 4. Observations

- `O-1` — **the amended clause's guarantee already holds on every path a result can actually be
  presented on, and the residual is test scaffolding.** `git grep` over `tooling/` for
  `validate_n2(` and `"review_result"` returns the registration itself (`review.py:71`), the
  kind literal (`review_result_v2.py:55`), and five test call sites
  (`test_flow_repair_disposition.py:538 :539 :1144 :1147 :1964`) — **no production caller**.
  `cli.py:321` computes its kind from the document (`assurance_summary` / `assurance_candidate`),
  so no command-line path presents a v1 result for validation. So the divergence the amendment
  opens between contract text and tree is confined to a dormant registration and test
  scaffolding, both already on item D's list. Recorded because it bounds `L-1` and because item
  D's executor should know the behaviour it is about to change has no caller to break.
- `O-2` — **`E9`'s review window is intact and the subject is HEAD.** `.harness/review-pending.json`
  names `006138eb40448bb1a0fbd0aab55ca89288004f4d`, dispatched `2026-08-28T13:23:09+00:00`, which
  is ten seconds after the subject commit's own timestamp; `git rev-parse HEAD` returns the same
  SHA, so the branch has taken no commit since dispatch, as `E9` requires.
- `O-3` — **the enumerations the layer states still hold at this subject.**
  `schema/document-assurance-v3/` holds **15** files, matching `E2`'s *fifteen files*;
  `layer_path_check.py`'s `LAYER` holds the same nine paths in the same order as `E10`'s
  sentence; `ORCHESTRATION.md`'s *nine obligations already law elsewhere* table has nine rows and
  its three own-text sections make `README.md:22`'s twelve; `EXECUTION.md`'s six run-template
  sections are all present. `CONTRACT-V4-SIGNATURE.md:43-54` carries the fourth post-signature
  write exactly as the amendment body claims, and its `:11-33` block already answers the
  signed-blob-versus-current-blob question, so nothing new is owed there.
- `O-4` — **the round's own disclosure that the orchestrator is carrying the verification half of
  `E1`'s execution side is present and routed, and I am not re-filing it.** `006138e`'s body
  states it plainly, gives the measured cause — a dispatched cold executor on this machine can
  run neither python nor git — and marks it for banking at closeout against
  `ORCHESTRATION.md`'s three-roles table with the `R10` constraint that its fix is design.
  `HD-55`'s split does hold on the record: both amendment bodies state that the orchestrator
  edited no byte of the executor's work. Confirmed present, nothing added.
- `O-5` — **outside the subject, routed to the user rather than asserted.** `HD-64` carries
  `scope: standing`, and `standing` in this register's own taxonomy means *can only be
  superseded*, while the entry's boundary paragraph says it authorises **only this one bullet, on
  only this one ground, and opens no channel** — which is the register's description of
  `one-shot`, *consumed and retired*. The entry also proposes its own flip to `implemented`,
  a section marked *not required reading*, while its status line gives the ground for staying
  `live`: the layer carries not a word of the set-aside. Whether the scope and the proposed flip
  are right is the user's (`R5`), and both live in a file that is not a member; recorded so the
  closeout decides it rather than inherits it.
- `O-6` — **riders re-confirmed, none repaired, none re-filed.** `wl-route`, `E10-sync`,
  `charter-qualifiers`, `e1-table`, `e1-reader`, `read-name-split`, `e9-pair-budget`,
  `e10-cannot-see`, `e10-freeze-exception`, `announced-set-anchor`, `contract-wikilink-tier`,
  `sig-write-once`, `v1-digest-recipe` and `r9-terminal-no-carrier` all describe layer text or
  adjacent surfaces I read at this subject; each is present as its row describes. Two notes.
  `read-name-split` governed this record's filename again, unchanged. `README.md:22`'s *added as
  the tenth member 2026-08-18* is unchanged for a **fourth** cycle — reported by
  `v3-cold-read-b737742.md` `O-3`, `v3-cold-read-60bf9eb.md` `O-2` and `v3-cold-read-dcb3aef.md`
  `O-4` — which is what rider `r9-terminal-no-carrier` exists to make visible. The statement is
  true as dated history; `E10`'s membership sentence remains the only authority on the count, and
  it reads nine.

## 5. Coverage and ceilings (`R4`)

- **Read in full**: all nine members; `HARNESS-DECISIONS.md` `§live` (lines 30–258);
  `HARNESS-RIDERS.md`; `CONTRACT-V4-SIGNATURE.md`;
  `tooling/tests/document_harness/test_readme_enumeration.py`;
  `tooling/rsclib/document_harness/review.py:1-110`;
  `tooling/hooks/layer_path_check.py:25-84`; the full commit bodies of `2aabd5a`, `aa8d212`,
  `4a380be` and `006138e`, and `2aabd5a`'s diff over contract v4.
- **Sampled**: `document-harness/plans/v1-result-retire.plan.md` (rulings, measured starting
  state, Constraints, Out of scope, items A–H, Acceptance, resume pointer — not the whole file);
  `review_result_v2.py:40-99`; `cli.py:295-334`;
  `schema/document-assurance-v3/review.schema.json:85-134`.
- **Probed by command only**: the nine blob ids, via `git rev-parse`; the range's member
  diffstat and commit list, via `git diff --stat` and `git log --oneline`; the staged path sets
  of `2aabd5a` and `aa8d212`, via `git show --stat`; the schema pack count, via directory
  listing; `validate_n2` / `"review_result"` call sites, via grep; `review.schema.json`
  references across `*.md`, via grep.
- **Not done, stated rather than softened**: **no test suite was run and nothing was
  mutation-tested in this session.** Every attempt to reach a Python interpreter or a
  non-read-only git subcommand was refused by this environment's permission layer, so
  `M-1`'s three no-guard-sees-it legs were established by reading each guard's own predicate and
  reproducing it by hand, not by neutering the guard and watching it stay green. A reader wanting
  binding force on `M-1` should demand that mutation: delete `review.schema.json` on a scratch
  branch and run `test_readme_enumeration.py` plus `layer_path_check.py` — my claim is that both
  stay green with the README link dangling. The same ceiling covers `O-1`: that
  `validate_n2("review_result", …)` has no production caller rests on grep over `tooling/`, not
  on execution. The orchestrator addendum to `2aabd5a` records an 827-passing battery and exit 0
  from both guards at that commit; I did not re-run it and do not restate it as my own
  measurement.
- **Process claims are marked, not verified** — that this session started cold and read nothing
  of the round beyond what is committed is a declaration with no evidence lock. What is checkable
  is that every fact above cites a command or a committed byte.
- **`M-1` supplies no bytes and says why** (the edit is not applicable at this subject; the
  applicable fix is to the plan, which is not a member). **`L-1` supplies no bytes and says why**
  (every live shape touches signed text; the choice is the user's under `R5`). Neither finding
  takes `E10`'s free channel, so nothing in this record is self-applying.
