# Cold read — the instruction layer at `3a6a10b`

**No verdict.** A read is not a round (`R3`): it spends no budget, carries no verdict, and its
output is findings tiered must-fix / low / observation. Nothing below certifies any text, and
nothing below is banked as any round's FULL.

**Findings: 0 must-fix, 0 low, 4 observations.** No member acts wrongly at this commit. The one
finding of the previous read (`v3-cold-read-693b692.md` `L-1`) is fixed, and the fix was
re-scanned for the whole class rather than the reported instance (`O-4`). The only new material
is `O-1`: a third site of the merged-role class `HD-55` was registered to carry, which `HD-55`'s
own status line does not name — a scan-class note (`HD-41` ④) for the design round that entry
says is owed, not a defect today.

**The citation channel was available for eight of ten and was not taken.** Eight member blobs
are byte-identical to those `v3-cold-read-693b692.md` §2 records, so `E10`'s citation clause
would have covered them; `EXECUTION.md` and `ORCHESTRATION.md` changed and were owed a read
regardless. All ten were read end to end anyway — the marginal product of a covered read is a
second independent judgement of the same bytes, and `O-1` sits in one of the eight.

**Standing instructions read.** `migration/document-work-assurance-v3/v3-harness-review-contract.md`
(the stub, member 7) → `document-harness/CONSTRUCTION-CHECKLIST.md` in full, both sides, per the
stub's *"It is your standing instruction and its own counterpart; read all of it."*
`HARNESS-DECISIONS.md` `§live` (lines 28–161, **eight** entries — `HD-55`, `HD-44`, `HD-41`,
`HD-36`, `HD-35`, `HD-34`, `HD-23`, `HD-9`) plus the file header (1–27) that states its own state
machine, which `E10`'s tail requires. Against the previous read's eight, `HD-52` left for
`§implemented` and `HD-55` arrived. `§implemented` and `HARNESS-DECISIONS-archive.md` were **not**
read end to end — they were grepped for the ids the members cite (§3.5). Cited by section, never
by blob.

---

## 1. What the subject is, and how it was derived

The dispatch supplied one commit and nothing else. Everything below was re-derived (`R2`).

```
$ git rev-parse HEAD
3a6a10bc62aae6e31f980ee05c67617b9a55bd1e

$ git status --porcelain
(empty)

$ git log -1 --format='%H%n%ad%n%s' 3a6a10bc62aae6e31f980ee05c67617b9a55bd1e
3a6a10bc62aae6e31f980ee05c67617b9a55bd1e
Sat Aug 22 21:51:23 2026 +1000
V3-HD55-ROLES-INDEPENDENT-v1
```

HEAD is the subject commit and the worktree is clean, so the worktree bytes are the subject
bytes — verified per member rather than inferred (§2).

**The subject commit touches no member.** `git show --stat` returns `HARNESS-DECISIONS.md` (+27)
and `HARNESS-RIDERS.md` (−1) and nothing else, so this is a cold read of standing layer text, not
a read of a diff. Neither file is a member (`HD-19`).

## 2. The member set and each member's blob

The set is `E10`'s own sentence, hand-transcribed from the checklist and not taken from the guard
that mirrors it; the transcription was then machine-compared against the guard (§3.3). Blob ids
per `E10`'s *"a read's record states the blob id of each member it read, because citation depends
on it"*. Sizes are `git ls-tree -l` object sizes; the worktree carries CRLF, so a byte count taken
there runs higher — the blob id, not the size, is the binding fact.

```
$ git ls-tree -l 3a6a10b -- <path>   /   git hash-object <path>
 #  blob                                       lines  bytes  path                                    worktree
 1  cacd99d49d80ce4bf33e94b733a07f1dd6b247e8     235  18531  document-harness/CONSTRUCTION-CHECKLIST.md  MATCH
 2  7591c5332d170a286a15ef6a699f69cc80def755      40  11021  document-harness/README.md                  MATCH
 3  ab261698e80b005869844f7ddb6bf441fa9b880b     505  35496  document-harness/EXECUTION.md               MATCH
 4  35fe0abcd7123f4a37a88ef4de605b3aad3cfe75     288  18209  document-harness/REVIEW.md                  MATCH
 5  48f665c4ea2f03dabc9a965d1156c7830cf8a3a7     101   6866  document-harness/ORCHESTRATION.md           MATCH
 6  6d5714923870b4e13e8928221a80df68e563a5ed       5    511  migration/…/v3-harness-operating-contract.md MATCH
 7  29bdc9fbde6e8db38d601dd2340d4b46a24a296f       5    924  migration/…/v3-harness-review-contract.md   MATCH
 8  68031fa2ca31272e31da0d42a9a02189d28fcc21     124   6480  contract/…-supersession-1.md                MATCH
 9  e1a2f26b1d8d323d11e900f8137dea222b6571c1     113   7421  contract/…-supersession-2.md                MATCH
10  09aa869962f592c2f86c9379be0ef3eb7d2232ff      44   2812  schema/…/paragraph-map.schema.json          MATCH
```

**Change since the previous recorded read.** Against `v3-cold-read-693b692.md` §2, members
3 (`27f4fc82` → `ab261698`) and 5 (`80f42658` → `48f665c4`) changed; the other eight are
byte-identical. The two changed under `229f03f` (`V3-EXECUTOR-CHARTER-v1`) and `3dd226b`
(`V3-EXECUTOR-CHARTER-FIX-v1`), and their diffs were read in full.

`HARNESS-DECISIONS.md` is **not** a member — `E10`'s tail owes it at a round's opening while
denying it membership, and `HD-19` records the same. It is cited by section, never by blob.

## 3. What was checked, and what the commands returned

Scope declaration (`HD-41` ①) precedes each assertion. Unless a line says otherwise, the scope is
**the ten member blobs at `3a6a10b`** and nothing else.

### 3.1 `E2`'s freeze surface

Scope: `git ls-tree` over `contract/` and `schema/document-assurance-v3/` at `3a6a10b`.

```
68031fa2ca31272e31da0d42a9a02189d28fcc21  contract/…-supersession-1.md
e1a2f26b1d8d323d11e900f8137dea222b6571c1  contract/…-supersession-2.md
b2dbdf752d8c155e4c65b14b5f420b880b8184a1  contract/Document-Work-Assurance-Contract-v3.md
schema/document-assurance-v3/ : 15 files
```

All three named blobs verify against `E2`'s text (`b2dbdf75…`, `68031fa2…`, `e1a2f26b…`), and the
pack holds exactly the fifteen the re-baseline clause names — `HD-44`'s eighteen items (3 + 15),
present and in this repository. `README.md:22`–`:25` enumerates those same fifteen across its four
schema rows; the enumeration and the freeze surface agree.

### 3.2 Every path reference in the layer, resolved

Two scopes, because the guard covers one and `E10`'s clause covers the other. Both were run over
the **whole standing text** of all ten members, which is precisely the stock `E10` says the guard
never re-scans.

**(a) Backtick path tokens**, driven through the guard's own predicate
(`layer_path_check.unresolved_tokens`) rather than through a staged diff:

```
CONSTRUCTION-CHECKLIST 0 · README 0 · EXECUTION 0 · REVIEW 0 · ORCHESTRATION 0
operating-contract 0 · review-contract 0 · paragraph-map.schema.json 0
supersession-1: 2   ResearchSystem/…/W2/W2-design.md · ResearchSystem/…/W2/W2-record.md
supersession-2: 3   assurance/runs/ · templates/run-v2/ · ResearchSystem/migration/document-work-assurance-v3/
TOTAL 5
```

All five sit inside the two `E2`-frozen supersessions, which `E10`'s final clause excepts *while
they are frozen*. **Outside the frozen bytes the count is zero**, the two changed members
included. The five are the rider `frozen-path-prefix` set, unchanged in number and location.

**(b) Relative markdown links** — the blind spot `E10` names by name:

```
53 links checked (http/https/anchor-only excluded); broken: 0
```

Zero broken, frozen bytes included. The count rose from the previous read's 51 by exactly the two
links `ORCHESTRATION.md` gained in `229f03f` (`[EXECUTION.md]`, `[CONSTRUCTION-CHECKLIST.md]`),
which is the arithmetic the diff predicts.

Spot-resolved by hand besides: `migration/…/W2/W2-record.md`, `…/N0/N0-record.md`,
`…/N1/N1-record.md`, `…/N2/N2-record.md`, `…/N0/fixtures/cases.json`,
`document-harness/history/REVIEW-v1-package-flow.md`, `document-harness/journal/retro-2026-08-03.md`,
`document-harness/plans/harness-deletion-first-stabilization.plan.md`,
`assurance/templates/run-v2/README.md`, `CONSTRUCTION-LEDGER.md`, `HARNESS-RIDERS.md` — all
present at `3a6a10b`.

### 3.3 The membership sentence and its mirrors (`HD-22`)

Scope: `E10`'s sentence as hand-transcribed by this reader against `layer_path_check.LAYER`.

```
E10 (hand-transcribed) == LAYER : True | n = 10
```

The guard's `LAYER` tuple and its docstring's *"The member list mirrors E10's membership
sentence"* both hold. `E5`'s independence requirement is met on the test side by
`test_precommit_checks.py`'s hand-written `EXPECTED`, which the previous read verified and whose
blob is unchanged.

### 3.4 Rule enumerations and the counts the members state about themselves

```
E-rules in CONSTRUCTION-CHECKLIST.md : 12  (E1…E12, all distinct)
R-rules in CONSTRUCTION-CHECKLIST.md : 10  (R1,R2,R3,R9,R10,R4,R5,R6,R7,R8 — complete)
ORCHESTRATION.md "nine obligations" table : 9 data rows
ORCHESTRATION.md "three obligations" subsections : 3
ORCHESTRATION.md roles table : 3 rows
```

9 + 3 = 12 matches `README.md:26`'s *"nine of its twelve obligations"*. `E10`'s *"exactly these
ten paths"* enumerates ten. The R-rules are written out of numeric order (R9 and R10 sit after
R3); the set is complete and the grouping is legible, so this is not reported as a finding — the
same reading the previous read reached independently.

### 3.5 `HD` ids and commit ids cited in the layer

Scope: every `HD-\d+` token, and every backtick token of 7–40 hex characters, in the ten members.

```
HD ids cited: 14 distinct — HD-1 HD-2 HD-5 HD-7 HD-14 HD-20 HD-28 HD-34 HD-35 HD-39
                            HD-41 HD-42 HD-47 HD-52.   Dangling: 0
  §live 3 (HD-34 HD-35 HD-41) · §implemented 7 · archive 4 (HD-14 HD-28 HD-39 HD-42)

commit ids: 12 distinct.  Resolves here: 0d73a5f (commit) — EXECUTION.md, the instrument base.
  Absent here (11): 418b89c 6fd0ae3 7011916 820b287 838c413 9ba9bbc a22cca0 a8af54c
                    ac1b383 cf51534 ddd773a
```

Thirteen ids were cited at the previous read; `HD-52` is the fourteenth, added by `EXECUTION.md`'s
new form-independence sentence, and it resolves. The commit-id split is exactly the shape `E10`'s
*Where a cited commit id resolves* clause predicts, and the root `README.md` §*Where the bytes
came from* (line 12) exists and names the repository the eleven belong to — both halves of that
clause re-derived, including that `7011916` is absent here.

### 3.6 Factual assertions in the layer, run rather than read (`E3`)

Scope: the assertions in the members that name a command or a countable property of *this*
repository.

```
$ python -m pytest -q            # run from tooling/, per EXECUTION.md's battery bullet
790 passed in 100.68s

$ python validate_fixtures.py    # migration/document-work-assurance-v3/N0/fixtures/
41/41 cases behaved as declared; failures=0
```

- **The instrument battery leg is green at the subject commit.** `790` is this read's own
  measurement; the previous read measured `774`, and the growth is the `EXECUTOR-CHARTER` round's
  tests. Not a finding: the same paragraph says *"Re-run the battery for a current figure rather
  than trusting any list written here (`HD-41` ③)"*, so the text disclaims its own tally.
- `README.md:35`'s *(41/41 green)* re-derives exactly.
- **Scope correction, recorded because it nearly produced a false finding** (`HD-41` ①): an
  earlier `git ls-tree | grep validate_fixtures` in this read returned nothing and appeared to
  show the runner absent. The command had been issued from `tooling/`, where `git ls-tree`
  scopes to the current subtree. Re-run from the repository root, the runner is present and
  green. The negative was the scope's, not the repository's, and no finding rests on it.

### 3.7 The claims the layer makes about the dispatch code

Both members that changed make new factual claims about `dtw dispatch`, so both were run (`E3`).

```
dispatch.py:548  CONSTRUCTION_ROLE_INSTRUCTION = "migration/…/v3-harness-review-contract.md"
dispatch.py:770  EXECUTOR_ROLE_INSTRUCTION     = "document-harness/EXECUTION.md"
dispatch.py:429  ROLE_INSTRUCTION              = "document-harness/REVIEW.md"
cli.py:582–598   --subject · --range · --read · --executor · --construction-executor   (5 modes)
test_dispatch.py:398,463,522  CHARTER_OUTSIDE / MEMBER — hand-written literals (E5)
test_dispatch.py:675,681      construction fixture formats {charter} as a substitution
```

- `ORCHESTRATION.md`'s *"three review-side modes, and two executor-side modes, one per side of
  the work"* verifies exactly: five flags, split 3/2 as stated.
- `ORCHESTRATION.md`'s *"the product-run executor's charter is `EXECUTION.md`, the
  construction-round executor's is `CONSTRUCTION-CHECKLIST.md`"* verifies:
  `EXECUTOR_ROLE_INSTRUCTION` is `EXECUTION.md`, and the construction fixture's
  `CHARTER_OUTSIDE` is `CONSTRUCTION-CHECKLIST.md`.
- The stub's own *"hard-codes this path"* and *"pin it independently (`E5`)"* both hold: the test
  pins the path with its own literal rather than importing the module constant, and the fixture
  carries `{charter}` as a substitution, not the path — all three claims the stub makes.
- The previous read's `O-1` (the `cli.py` help string calling a review dispatch *"the executor's
  cold entry"*) is gone: `cli.py:582` now reads *"PRODUCT run review: the evidence commit"*.

### 3.8 The guard's described blind spots, exercised rather than read

`E10` makes an unusually precise claim about what `layer_path_check` cannot see. Each half was
driven through the real predicates, not inspected:

| `E10` says | exercised result |
|---|---|
| a placeholder segment falls outside its path shape | `PATHLIKE.match("<control root>/control/paragraph-map.json")` → `False` ✔ |
| markdown links carry no backtick token | `TOKEN.findall("[a](docs/x.md)")` → `[]` ✔ |
| `++ b/…` mis-files the member's remaining added lines | added content `++ b/evil` → lines filed under `evil`, not the real member ✔ |
| any other `++ …` silences them | added content `++ other` → `{}`, lines dropped ✔ |
| the standing text it never re-scans stays unscanned | `check()` reads only `added_lines_by_path` ✔ (scanned here instead, §3.2a) |
| the bytes `E2` freezes are excepted while frozen | consistent with §3.2a's five ✔ |

The description is accurate in every detail, including the docstring's further claim that a
*pasted* header (content `+++ …`, rendering `++++ …`) is handled — exercised, and the following
lines stayed filed under the real member. `.harness/` exemption present (`RUNTIME_PREFIX`).

### 3.9 The closeout carriers the previous round left outstanding

Scope: the three carriers `v3-review-verify-3dd226b.md` `V-5` recorded as owed at closeout.

At `3a6a10b` they have landed: `HD-53` (the two executor dispatch modes) and `HD-54` (the C4
`O-1` reading moment, homing the obligation in the executor charter) both exist in
`§implemented`, and `CONSTRUCTION-LEDGER.md:106`–`:108` still carries the conversation-only C4
`O-1` row. That row is what `EXECUTION.md`'s new sampling paragraph points at, so the dependency
`V-3` flagged — *"if closeout moves or trims it, the layer sentence that now depends on it is
what breaks"* — is intact rather than broken. Rider `startcard-form` is redeemed and absent from
the bank, matching `HD-52`'s move to `§implemented` and the form-independence sentence landing in
`EXECUTION.md`.

## 4. Findings

### `O-1` (observation) — a third site of the merged-role class, not named by `HD-55`'s status line

`HD-55` (`§live`, the subject commit's own entry) rules executor and orchestrator to be
independent sessions and records that the layer carries no sentence saying so. Its status line
names two sites that still write the merged form as an ordinary state — `E1`'s intermediate-state
disclosure sentence and `HD-46`'s tiebreak rationale — and says a design round owns writing
*"independent is the norm, merging is the exception"* into **`E1` or the three-roles table**.

Scope: `(one session|same session|both roles|both work-side|a session holding|merg)`,
case-insensitive, over all ten member blobs. Three hits; one is a third site of the same class:

> `ORCHESTRATION.md:95`–`:97` — *"Where exactly the line runs — work side against review side,
> and what a session holding both work-side roles owes — is `E1`'s to state, and this file does
> not re-type it. Read `E1`."*

The other two are not: `EXECUTION.md:42` (*"nothing here stops one operator from playing both
roles"*) is the executor/verifier honesty ceiling grounded in contract §1, a different pair of
roles; `EXECUTION.md:236` is the word *merged* in an unrelated quotation.

**Why it is an observation and not a low.** It changes no actor's action today. The site
delegates rather than asserts — *"that rule is the text"* is `ORCHESTRATION.md`'s stated design —
so it inherits whatever `E1` says, and `HD-55` is on the mandatory reading path of every round
opening (`E10`'s tail), outranking the layer on conflict. Nothing acts wrongly.

**Why it is worth recording.** `HD-55` offers the design round a choice of carrier — `E1` **or**
the three-roles table. If that round writes the norm into the **table**, `E1` keeps its
neutral phrasing and this pointer keeps resolving to it, and the class closes at one site of
three. `HD-41` ④ is the discipline this note serves: the scan belongs to the round that writes
the fix, and it now has the third site enumerated rather than having to find it. Recorded for
that round, not routed anywhere else.

### `O-2` (observation) — the `plan-delivery` gap re-derives exactly and remains correctly banked

Scope: every occurrence of `plan` in `ORCHESTRATION.md`, and the delivery half-sentence in
`EXECUTION.md`'s *Instruction authoring rules*.

`EXECUTION.md` says standing discipline lives *"in this file and the governing plans"*, with
*"the plans arriving with the instruction and subject the orchestrator delivers"*.
`ORCHESTRATION.md`'s *Handing the executor its instruction* — the layer's text for that
obligation — enumerates charter, instruction and subject, and no plan. Measured: `plan` occurs in
`ORCHESTRATION.md` exactly once, at `:83`, inside the report-back section and not as a
deliverable. So discipline that lives in a plan has no written delivery path now that the Context
route is closed.

This is rider `plan-delivery` (`HARNESS-RIDERS.md:46`, source `v3-review-verify-3dd226b.md`
`V-2`), re-derived independently and found accurate in both halves. Its fix is design either way,
its row correctly names a round-eligible surface rather than a batch, and its deadline — the first
product-run instruction authored under the new rule — has not arrived. Recorded as a confirming
re-measurement so a future read need not re-open whether the row still describes the text.

### `O-3` (observation) — a wording-level finding that supplies bytes still matches two routes

`R10` routes findings in an ordered list: *"`E10`'s must-fix channel takes must-fix, R9 takes
wording-level, the `E10` free channel takes … any finding whose record supplies the exact bytes …
and the bank takes what is left."* A finding that is both wording-level **and** supplies exact
bytes matches two entries. `R9` says such a finding *"rides the next batch touching this layer"*;
the free channel says *"applied immediately … reported after the fact and reversible"*.

Reached independently here before the previous read's record was opened, and it is that read's
`O-3` unchanged — the text has not moved. The outcomes agree on what matters (neither opens a
round, neither spends budget), and reading the list as ordered resolves the timing, which the
sentence's construction supports. Recorded as a tension a reader may not resolve the same way,
not as a defect: no actor is currently acting on it.

### `O-4` (observation) — the previous read's `L-1` is fixed, and the fix closed the class, not the instance

`v3-cold-read-693b692.md` `L-1` reported that `EXECUTION.md`'s doc-only tier exception named two
code-pinned doc paths while the repository had five. At `3a6a10b` the bullet
(`EXECUTION.md:344`–`:355`) names all five and generalises the criterion to *"any doc path code
or a test pins"* — the *criterion* branch of the two the finding offered, which the user chose.

Independently re-verified rather than accepted, each pin run down to its line:

| path | pinned by | named now |
|---|---|---|
| the ten member paths | `hooks/layer_path_check.py` `LAYER` | yes |
| `document-harness/README.md` | `tooling/tests/document_harness/test_readme_enumeration.py` | yes |
| `document-harness/templates/decision-log.md` | `init_target.py:36,48` + `test_init_command.py:39` | yes |
| `document-harness/templates/rider-bank.md` | `init_target.py:37,48` + `test_init_command.py:40` | yes |
| `contract/Document-Work-Assurance-Contract-v3.md` | `__init__.py:41` `CONTRACT_PATH` | yes |

Re-scanned for a sixth (`HD-41` ④): scope = every `"…\.md"` string literal in `tooling/rsclib`,
`tooling/hooks` and `tooling/tests` at `3a6a10b`, cross-read against tracked paths. The only
repository-root doc names appearing besides the five are `HARNESS-DECISIONS.md` and
`HARNESS-RIDERS.md` at `init_target.py:36`–`:37` and throughout `test_init_command.py` — and
these are **destination** filenames written into a temporary target root, not pins on this
repository's own copies: the tests build their own root and never read the repository's. Renaming
this repository's ledgers would break nothing there, so they are correctly outside the
enumeration. Ceiling: a path assembled without any `.md` literal would be invisible to this scan.

No sixth path. The enumeration is complete at this commit, and the generalised criterion means a
sixth would be covered by the rule even before the text caught up.

## 5. Coverage — what was read in full, what was sampled, what was only probed (`R4`)

- **Read in full at the subject blobs:** all ten members, 1 460 lines as the worktree counts them.
  Blob ids in §2. No member was covered by citation, though eight were eligible.
- **Read in full outside the member set:** `HARNESS-DECISIONS.md` lines 1–161 (header + `§live`,
  eight entries); `tooling/hooks/layer_path_check.py`; `.githooks/pre-commit`;
  `v3-cold-read-693b692.md`; the subject commit's body and full diff.
- **Sampled:** `HARNESS-RIDERS.md` (the 33 rider ids, with `plan-delivery` read in full);
  `CONSTRUCTION-LEDGER.md:101`–`:109`; `v3-review-full-229f03f.md` (`L-3`, `O-5`, `O-6` and the
  changed-path table) and `v3-review-verify-3dd226b.md` (`V-2`–`V-5`, the blob table);
  `tooling/rsclib/document_harness/dispatch.py` (the three role-instruction constants),
  `cli.py` (the dispatch flags), `init_target.py` (`TEMPLATES`, `TEMPLATE_DIR`), `__init__.py`
  (`CONTRACT_PATH`), `test_dispatch.py` and `test_init_command.py` (the constants §3.7 and `O-4`
  name); the root `README.md` section headings.
- **Probed only:** `HARNESS-DECISIONS.md` `§implemented` and `HARNESS-DECISIONS-archive.md` —
  grepped for the fourteen ids the members cite (§3.5), never read end to end;
  `test_precommit_checks.py` — not re-opened, its blob being unchanged since the previous read
  verified its `EXPECTED` literal; `document-harness/plans/` — not read, deliberately, since `R2`
  says the read re-derives rather than inherits.
- **Not established:** whether the caller repository's five battery legs are green — their scripts
  are not in this repository and `EXECUTION.md` says they are not owed here. `UNVERIFIABLE` from
  this side, and stated rather than folded into the green result in §3.6.
- **Process claims are marked, not verified** (`R4`): that this read ran in a fresh context is a
  declared identity, not something the repository can lock.
