# Instruction-layer read — `3f19561978b4f87d086f2d7f0a6b29c2f7ed4d0d`

`E10` read of the instruction layer at `3f19561`. Not a round: no verdict, no budget consumed
(`R3`). It discharges the independent read owed for the `A2-R1` amendment (`418b89c`, the
`HD-14` move of six run-template rule sections into `EXECUTION.md`), and the read the two
free-channel byte applications of that round ride — `87cadf0` (`README.md:26`) and `7ea3566`
(`EXECUTION.md:167-173`) — which `E10` grants "at per-member digest cost … riding the next read
of this layer". `7ea3566`'s bytes have had no independent look before this one: they landed
after the VERIFY record.

**Findings: 0 must-fix, 1 low, 1 wording-level (`R9`), 3 observations.** The moved block is
byte-identical to its source except the eight disclosed substitutions at seven sites — I
reconstructed and diffed it rather than reading the commit's account — and every re-anchored
path resolves at the subject. The amendment says what `HD-14` says, and `HD-14`'s carrier claim
holds. Both free-channel applications add no clause, change no requirement, and write no `E2`
path. The nine-path enumeration is untouched, both code pins still equal it, and the guards and
the two tests that read the layer are green. The low is a tier boundary the round crossed
twice: `E10` grants the free channel to "a low finding", and the second application came from an
**observation**.

## 1. Subject, re-derived (`R2`)

Handed one SHA and the phrase *an E10 read*. Member set, blob ids, the commits in scope, the
citation anchors and every count below are re-derived here; nothing is taken from the dispatch
prompt, the ledger, the plan, the commit bodies, or the round's own FULL and VERIFY.

```
$ git rev-parse HEAD              -> 3f19561978b4f87d086f2d7f0a6b29c2f7ed4d0d
$ git status --porcelain          -> (empty)
$ cat .harness/review-pending.json
  {"subject": "3f19561978b4f87d086f2d7f0a6b29c2f7ed4d0d",
   "dispatched_at": "2026-08-09T03:36:39+00:00"}
```

HEAD **equals** the subject and the tree is clean, so worktree reads are reads of the subject
bytes. Dispatch (03:36:39Z = 13:36:39+10:00) post-dates the tip commit `3f19561`
(13:35:28+10:00) by 71 seconds, and the branch has taken no commit since — this record is the
first it admits (`E9`). The tip itself (`V3-A2-R1-CLOSEOUT-v1`) writes no member.

`E10`'s sentence **at the subject blob** governs the member set: nine paths, closed with "and
nothing else". `HARNESS-DECISIONS.md` is named inside the bullet but expressly as a non-member,
so the set stays nine and is decidable by reading the membership sentence.

| # | blob at `3f19561` | lines | member | state, and where a citation may anchor |
|---|---|---|---|---|
| 1 | `44d622b9` | 182 | `document-harness/CONSTRUCTION-CHECKLIST.md` | unchanged — end-to-end read recorded at `v3-checkpoint-read-bd77fd4.md` §1; also this session's standing instructions, read in full |
| 2 | `dab9f71a` | 38 | `document-harness/README.md` | **changed** (`dd1c7c3e` → here, at `87cadf0`) — **read end to end here** |
| 3 | `8bbd330f` | 404 | `document-harness/EXECUTION.md` | **changed** (`810f5081` → `7cd5a28` at `418b89c` → here at `7ea3566`) — **read end to end here** |
| 4 | `3350bfac` | 284 | `document-harness/REVIEW.md` | unchanged — end-to-end read at `v3-checkpoint-read-a5a04c3.md` §1 |
| 5 | `17ff31bb` | 5 | `migration/…/v3-harness-operating-contract.md` (stub) | unchanged — `a5a04c3` §1 |
| 6 | `52a97a48` | 5 | `migration/…/v3-harness-review-contract.md` (stub) | unchanged — `a5a04c3` §1; also read here as the dispatch entry point |
| 7 | `68031fa2` | 124 | `contract/…-v3-supersession-1.md` | unchanged — `a5a04c3` §1 |
| 8 | `e1a2f26b` | 113 | `contract/…-v3-supersession-2.md` | unchanged — `a5a04c3` §1 |
| 9 | `09aa8699` | 44 | `schema/document-assurance-v3/paragraph-map.schema.json` | unchanged — `a5a04c3` §1 |

Blob ids from `git ls-tree 3f19561`, line counts `wc -l` on `git show` at the subject. Blobs 7
and 8 equal `E2`'s frozen ids, as they must; the third frozen blob, the contract itself, is
`b2dbdf75` at the subject and is not a layer member.

**The anchors are per member, and they are not all the same record** — see `O-2`. Rows 4, 5, 7,
8 and 9 are byte-identical to `bd77fd4`'s table, whose own cells record them as *cited* to
`a5a04c3`; `a5a04c3` §1 states their blob ids and says all nine were read end to end there, so
that is the record where the reading happened. Row 1 was read end to end at `bd77fd4` itself.

**Commits in scope, classified by hand.** `git log bd77fd4..3f19561` is 14 commits; restricting
`--name-only` to the nine members returns exactly three, and they are the only commits this read
answers for:

| commit | member written | kind |
|---|---|---|
| `418b89c` | `EXECUTION.md` | amendment (design; opened round `A2-R1`) |
| `87cadf0` | `README.md` | `E10` free-channel application of FULL `L-3` |
| `7ea3566` | `EXECUTION.md` | `E10` free-channel application of FULL `O-4` |

No `ResearchSystem/assurance/runs/` path is touched anywhere in the range, and no `E2`-frozen
path is (`git log --name-only … | grep 'ResearchSystem/\(contract\|schema\)/'` → empty). The
schema pack holds 15 files at the subject, matching `E2`'s re-baseline parenthesis.

## 2. The amendment against the repository (`E3`)

**"Moved verbatim" is exact, and I did not take the account for it.** I extracted the source
block from the pre-move README (`418b89c^:…/run-v2/README.md`, lines 46–268, 223 lines) and the
destination block from the subject (`EXECUTION.md` 175–397, 223 lines) and diffed them:

```
$ diff -u /tmp/old_block.md /tmp/new_block.md
  6 hunks, 8 changed lines, no additions and no deletions:
   ../../runs/p5a-shells/control/audit-rounds.md      -> ResearchSystem/assurance/runs/…   (×2)
   tooling/tests/                                     -> ResearchSystem/tooling/tests/
   control/paragraph-map.json                         -> ResearchSystem/assurance/runs/<run-id>/control/…
   document-harness/README.md                         -> ResearchSystem/document-harness/README.md
   tooling/hooks/layer_path_check.py                  -> ResearchSystem/tooling/hooks/layer_path_check.py
   ../../../document-harness/journal/retro-2026-08-03.md -> ResearchSystem/document-harness/journal/…
   the rule this README already carries                -> the rule this file already carries
```

Eight substitutions, seven sites, the audit-rounds path twice — item for item what the stage
marker claims and what the moving commit disclosed. Nothing else in 223 lines differs. Every
re-anchored target is tracked at the subject (five checked individually); the seventh carries a
`<run-id>` placeholder and is deliberately unresolvable, and five tracked files end in
`control/paragraph-map.json`, which is why the bare token was ambiguous before the re-rooting.

**The rest of the amendment.** `EXECUTION.md` = old head + a rewritten reader sentence + old
`13:165` + the R1 stage marker + the moved block + old tail; the source README is 290 → 72 lines
and now carries instantiation, the two unchanged descriptive sections, and a five-line pointer
blockquote naming all six moved sections and their new home. The stage marker's claim that it
"now holds instantiation only" is a fair characterization of that residue. `EXECUTION.md` is
171 → 404 lines and is the layer's largest member.

**`HD-14`'s carrier claim holds.** The ruling is "`templates/run-v2/README.md` 的六节规则移入已受
`E10` 保护的 `EXECUTION.md`，README 只留「怎么实例化这个模板」", and its `§implemented` status
names `EXECUTION.md`'s six sections as the carrier. The six headings exist at the subject, in the
order the ruling and `README.md:26` name them:

```
$ grep -n '^## ' ResearchSystem/document-harness/EXECUTION.md
175 Pre-freeze gate   197 Instruction form   238 Authoring gate
261 Audit cadence     311 Regression-battery tiering   350 Instruction authoring rules
```

**Assertions the move made cross-member, checked.** The moved *Audit cadence* section says
"REVIEW.md's instruction-completeness recheck walks the raw instruction against the unit map from
scratch at every FULL" — `REVIEW.md:111-112` carries exactly that recheck, against the raw
instruction and not the derived map. The moved *Authoring gate* section requires
`check_template_instance.py` before START and `make_paragraph_map.py` for the map; both are
tracked template members at the subject, which also keeps `README.md:25`'s "enforced by its
authoring gate" true after the rule sections left that README. `EXECUTION.md:72-73`'s pointer to
`REVIEW.md`'s *When the map is incomplete* lands (`REVIEW.md:150`).

**Membership and its pins.** The membership sentence is untouched (member 1's blob is unchanged),
so rider `E10-sync`'s three-site discipline is not triggered; `layer_path_check.LAYER` and
`test_precommit_checks`' `EXPECTED` were not touched in the range either, and both guards run
clean at the subject:

```
$ python ResearchSystem/tooling/hooks/layer_path_check.py  -> exit 0
$ python ResearchSystem/tooling/hooks/ledger_cap_check.py  -> exit 0
$ python -m pytest …/test_readme_enumeration.py …/test_precommit_checks.py -q -> 47 passed
```

## 3. The two free-channel applications

`E10` admits them only on conditions, and the conditions are decidable by inspection. Both:
write a member that `E2` does not freeze (`E2`'s list is three contract blobs plus the schema
pack; neither file is in either); are one line or five emphasis pairs, reversible; are reported
in their own commit bodies after the fact; and add no clause and change nothing any rule
requires — `README.md:26` is a navigation-table cell describing what a file contains, and
`7ea3566` converts nested `*…*` to `**bold**` inside the R1 stage marker, adopting the
convention the file's own W1 marker at `:110-112` already uses. I diffed both and there is no
third edit in either: `87cadf0` replaces one line, `7ea3566` five, and the `HARNESS-RIDERS.md`
halves of both touch a file that is neither a member nor frozen.

`README.md:26`'s new content is also **true**: it asserts that `EXECUTION.md` holds six named
run-template rule sections, and the heading grep above returns those six names in that order.

What does not hold cleanly is the tier the second one came from — `L-1` below.

## 4. What the amendment may have falsified elsewhere — swept

- **Members.** Only two of the nine mention the run-v2 template at all: `EXECUTION.md:170` (the
  stage marker's own source pointer) and `README.md:25` (the paragraph-map row, still true — the
  generator and the gate are scripts and stayed in the template). `REVIEW.md`,
  `CONSTRUCTION-CHECKLIST.md`, both stubs, both supersessions and the schema carry no statement
  about where the six rule sections live. `paragraph-map.schema.json:5` names "the run-v2
  authoring gate", which is the script, not a README section — unaffected, and in any case its
  bytes owe `E2`'s recorded ruling first (`HD-20`).
- **Live code.** The three stale "run-v2 README" citations the FULL found (`instruction.py:15`,
  `:382`, `test_transcript_audit.py:83`) all read `EXECUTION.md` at the subject — the `L-1`
  repair landed. I grepped `tooling/` for member references: nothing reads either changed
  member's bytes except `test_readme_enumeration.py`, which pins delimited schema stems in
  `README.md` and is green.
- **Reliance, the other direction.** No round has relied on the amended text before this read.
  Nothing in the range touches `assurance/runs/`; the FULL, the VERIFY and their records are
  review *of* the amendment, which `E10`'s reliance definition excludes; the fix leg `fbcb035`
  re-points three docstrings at the new home, which is citation, not reliance. The round did
  classify its own battery tier from the moved text, but the same rule applied identically
  before the move from outside the layer, so no outcome turns on the amendment. Deadline met,
  not merely deferred.
- **`HD-21`'s question duty, exercised for the window.** Four files were added in the range —
  one journal and three review/read records. None claims authority over any rule here, so the
  membership question is not triggered and the set stays nine.

## 5. Process boundary — second (`R3`)

- **`E10` sequencing.** `418b89c` took the design route and opened a round; its FULL is the
  round's, not the amendment read (`E10` forbids banking it as one). This record is that read,
  and it also carries the read the two applications owe.
- **`E9`.** This read spends no budget and carries no verdict. Per the occurrence rule it has
  occurred only when this record's commit lands; from dispatch to that commit the branch takes
  no commit but the record itself.
- **Boundary.** This session writes exactly one path — this record — and nothing else.

## 6. Findings

### Low

**`L-1` — the free channel's tier boundary: an observation's bytes were written into a layer
member, and `E10` grants the channel to "a low finding".** Location:
`CONSTRUCTION-CHECKLIST.md` at `44d622b9`, the `E10` free-channel clause ("a low finding whose
record supplies the exact bytes or names the content takes the same free channel"), and `R10`'s
routing sentence ("a middle **low** whose record supplies the exact bytes … takes the `E10` free
channel"), against `7ea3566`, which applied the FULL's `O-4` — tiered an **observation** by the
record that raised it — to `EXECUTION.md:167-173`. **Ground truth:** the two tier words `E10`
and `R10` use are must-fix and low; observation is the third tier `R3` names for read output and
the one the FULL used, and no clause routes it. The VERIFY's `O-2v` closed the gap by reasoning
from a different property — `O-4` "was the one that named its own bytes … so it was the one the
free channel could have taken" — and the application followed. **Decision that goes wrong
unfixed:** a session holding an observation that names its bytes has two textually supported and
opposite actions — apply immediately to an `E10` member (precedent: `7ea3566`, approved by the
user and reasoned for by an independent VERIFY) or refuse and bank (text: "a low finding"). Which
it takes decides whether instruction-layer bytes get written outside any named channel, so an
actor's action changes and this is not wording-level under `R9`. **No bytes are supplied,
deliberately:** naming which tiers the channel serves adds a bound to `E10`, which the design
test sends to a round — and `E10` says design wins when both apply. **Routing:** this is the
*third* question on the surface rider `R10-route` already banks ("下一批碰 `R10` 文本或 `E10`
自由通道句，孰先"), after that row's own `R10`-summary-vs-`HD-20` conflict and the VERIFY's
`O-1v` (a FULL's low taking a channel `R10`'s FULL sentence does not name). It belongs in that
row's scope rather than a new row; widening the row is a riders-only edit, which the 2026-08-04
ruling puts outside `E9`. **Deadline:** the next review record that tiers an item as an
observation while naming its bytes — the moment the divergence bites, reachable at any round.

### Wording-level (`R9` — rides the next batch, spawns no round and no read)

**`W-1` — one by-name self-reference in the moved block was not converted.**
`EXECUTION.md:355-356`: "the rules the session runs under — gap banking, first-run obligations,
map-filling disclosures — live in `EXECUTION.md` and the governing plans". The sentence now
sits inside `EXECUTION.md` and points at it by name. It is the same class as the one
self-reference the move *did* convert (site 7, "the rule this README already carries" → "this
file"); it survived because the sweep that caught site 7 was deictic — `this README | this file
| this template | this section | above | below` — and a by-name reference matches none of those.
I re-ran the sweep and reproduce both halves: every deictic reference in the file still
resolves, and `grep -n 'EXECUTION\.md' ResearchSystem/document-harness/EXECUTION.md` returns
exactly one hit, `:356`. Of the three disciplines it forwards to, only gap banking has a visible
home in the file (`:27`, the `HarnessIssue` row); "first-run obligations" and "map-filling
disclosures" appear nowhere in it — so the sentence was already imprecise before the move, which
made it circular as well. **No downstream decision goes wrong:** "and the governing plans" is
the adjacent forwarding address, and the one real instruction that exercises this bullet
(`assurance/runs/p4-doc/instruction.md:126-131`) states the three items in its Context section,
which is where the bullet wants them. Minimum fix, if a batch touches this text: `EXECUTION.md`
→ `this file`, matching site 7.

### Observations (`R5` — reported; the conclusions are the user's)

**`O-1` — the self-reference sweep is narrower than its defect class.** `W-1` is the instance;
the class is "a statement whose truth depends on which file the text lives in", and it has at
least two syntactic forms — deictic and by-name. The round swept only the first, which is why
two independent reviews passed over `:356`. Any future move into this layer that reuses the same
pattern inherits the same blind spot; the destination file's own name is the cheapest addition
to it. Reported as shape (`E7`'s framing), with no row proposed — `W-1` rides the next batch.

**`O-2` — after this record the citation anchors differ per member, and two pointers say
otherwise.** `HARNESS-LEDGER.md:94-96` and `.goals/plans/harness-a2-construction.plan.md:174-181`
both tell the next opening it may cite `v3-checkpoint-read-bd77fd4.md` §1 for the seven unchanged
members. `bd77fd4` §1 records that it read members 1–3 end to end (and member 6 as its dispatch
entry point) and **cited `a5a04c3`** for members 4, 5, 7, 8 and 9; `E10` licenses citing "a
recorded end-to-end read **of it**", so for those five the record where the reading happened is
`v3-checkpoint-read-a5a04c3.md` §1, which states their blob ids and says all nine were read end
to end there. The chain is sound and one hop long — `bd77fd4`'s own cells name `a5a04c3` — so
nothing is unsupported today; what the pointer loses is the property the blob-id requirement was
bought for, that a citation names the record where the reading actually happened. §1 above states
the anchor per member. Rewriting the two pointer lines is execution-side bookkeeping.

**`O-3` — the dispatch marker still carries no `kind` field.** The `a5a04c3` layer-read marker
carried `"kind": "layer-read"`; `bd77fd4`'s did not and neither does this one, which holds
`subject` and `dispatched_at` only. Nothing load-bearing is chat-only — the read's kind is
committed in the ledger's A-batch line and the plan's resume pointer — and the freeze hook does
not read the field. Noted because it is now the second consecutive read with the field absent,
which makes it a format change rather than a one-off.

## 7. Coverage disclosure (`R4`)

**Read in full at the subject:** members 1 (182 lines, as standing instructions), 2 (38), 3
(404), 6 (5, as the dispatch entry point); the complete diffs and bodies of `418b89c`,
`87cadf0` and `7ea3566`; the reconstructed 223-line source block from `418b89c^` and its diff
against the destination; `v3-checkpoint-read-bd77fd4.md` (all 249 lines); the findings,
observations and implementation sections of `v3-review-full-418b89c.md` (`:60-196`, `:197-346`)
and `v3-review-verify-fbcb035.md` (`:160-309`); `HARNESS-DECISIONS.md` header + `§live` complete
+ `HD-14`; `HARNESS-RIDERS.md` (19 rows); `HARNESS-LEDGER.md` (120); the run-v2 README at the
subject (72); `layer_path_check.py` (105); the A2 plan's resume pointer.

**Sampled:** `v3-checkpoint-read-a5a04c3.md` — its §1 blob table and the sentence establishing
that all nine were read end to end there (`:1-80`); `REVIEW.md` — the passages the moved text
asserts about (`:107-112`, `:150`), not the whole file, which is cited to `a5a04c3`;
`p4-doc/instruction.md:123-133`; commit dates and stats via `git log --format` / `--stat`.

**Only probed:** the eleven non-member commits in the range — classified by title and changed
paths for the enumeration, not read for substance; the template scripts — existence in the index,
not their code; `HARNESS-DECISIONS-archive.md` — existence and role; the journal
`batch-a2-2026-08-09.md` — not read.

**Not verified:** that this read ran in a fresh context — a process claim, marked (`R4`). The
preview cards, their approvals, and the user's 2026-08-09 approval of the three-low allocation
are chat-only (`R7` — ceiling stated, not a block). The executors' and reviewers' own probes
(guard negative controls, the 632-test battery, the reconstruction in FULL §2.1) were reviewed
where they belong and are not re-run here; my guard claims are the two exit-0 runs and the
47-test run above, and my verbatim claim is my own diff.

**Ceiling.** What is established: the moved block is byte-identical to its source but for eight
disclosed substitutions at seven sites; the amendment says what `HD-14` says and its carrier
claim holds; every repository assertion I could falsify reproduces at the subject; the
enumeration and both code pins are untouched and equal; no member is left holding a statement
the amendment falsified; both free-channel applications are accurate, clause-free and outside
`E2`; and no round relied on any of the three texts before this read. What is **not**
established: which reading of the free channel's tier boundary a future session will take
(`L-1` — both have support, one of them precedential); whether prose sweeps are sufficient
guarding for a prose charter (no one claims it — rider `E10-sync`); whether the three
disciplines `:356` forwards to have a correct home anywhere (`W-1` names the gap, not its fix);
and anything about the work the amendment governs, which `E10` expressly excludes from this
read's subject.
