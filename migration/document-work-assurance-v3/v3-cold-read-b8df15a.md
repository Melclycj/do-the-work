# Cold read — the instruction layer at `b8df15a`

**No verdict.** A read is not a round (`R3`): it spends no budget, carries no verdict, and its
output is findings tiered must-fix / low / observation. Nothing below certifies any text, and
nothing below is banked as any round's FULL.

**Findings: 0 must-fix, 1 low, 5 observations.** No member acts wrongly at this commit. The one
low (`L-1`) is a hole in `R6`: it offers two read-record filenames and no member states which
applies when — `E10` defines *cold read* and nothing defines *checkpoint read*, so the cheap
index into a prior read's coverage is unspecified. Its fix adds a criterion, which is design
under `E10`, so it banks rather than taking the free channel (`R10`).

**The citation channel was available for six of ten and was not taken.** Six member blobs are
byte-identical to those `v3-cold-read-3a6a10b.md` §2 records — re-derived here against
`3a6a10b` itself rather than read off that table (`R2`) — so `E10`'s citation clause would have
covered them; members 1, 3, 4 and 5 changed under round `PRERUN-RIDERS` and were owed a read
regardless. All ten were read end to end anyway. The previous read's `O-1` is closed: `HD-55`
left `§live` for `§implemented` and its carrier landed at all three sites, the third being the
one that read named.

**Standing instructions read.** `migration/document-work-assurance-v3/v3-harness-review-contract.md`
(the stub, member 7) → `document-harness/CONSTRUCTION-CHECKLIST.md` in full, both sides, per the
stub's *"It is your standing instruction and its own counterpart; read all of it."*
`HARNESS-DECISIONS.md` `§live` (lines 28–134, **seven** entries — `HD-44`, `HD-41`, `HD-36`,
`HD-35`, `HD-34`, `HD-23`, `HD-9`) plus the file header (1–27) that states its own state machine,
which `E10`'s tail requires. Against the previous read's eight, `HD-55` left for `§implemented`
and nothing arrived. `§implemented` and `HARNESS-DECISIONS-archive.md` were **not** read end to
end — they were grepped for the ids the members cite (§3.5). Cited by section, never by blob.

---

## 1. What the subject is, and how it was derived

The dispatch supplied one commit and nothing else. Everything below was re-derived (`R2`).

```
$ git rev-parse HEAD
b8df15a14229944270ae6ff720b14f57170f9b1a

$ git status --porcelain
(empty)

$ git log -1 --format='%H%n%ad%n%s' b8df15a14229944270ae6ff720b14f57170f9b1a
b8df15a14229944270ae6ff720b14f57170f9b1a
Sun Aug 23 15:18:54 2026 +1000
V3-PUB-FACADE-CLOSEOUT-v1
```

HEAD is the subject commit and the worktree is clean, so the worktree bytes are the subject
bytes — verified per member with `git hash-object` against `git rev-parse b8df15a:<path>`,
10/10 MATCH, rather than inferred (§2).

**The subject commit touches no member.** `git show --stat b8df15a` returns
`CONSTRUCTION-LEDGER.md`, `HARNESS-RIDERS.md` and
`document-harness/plans/publicization-a.plan.md` and nothing else, so this is a cold read of
standing layer text at a round's opening, not a read of a diff. None of the three is a member.

**The freeze window is intact, re-derived rather than assumed** (`REVIEW.md` says to). The
untracked marker `.harness/review-pending.json` names subject
`b8df15a14229944270ae6ff720b14f57170f9b1a`, dispatched `2026-08-23T05:48:15+00:00`; the branch
tip is that same commit, so no commit has landed since dispatch (`E9`). This repository's
tracked hook does not run `review_freeze_check.py` — its own comment says so and gives `E6` as
the reason — so the window here is discipline, held, not enforcement.

## 2. The member set and each member's blob

The set is `E10`'s own sentence, hand-transcribed from the checklist and not taken from the
guard that mirrors it; the transcription was then machine-compared against the guard (§3.3).
Blob ids per `E10`'s *"a read's record states the blob id of each member it read, because
citation depends on it"*. Sizes are git object sizes.

```
$ git rev-parse b8df15a:<path>  /  git cat-file -s  /  git show | wc -l
 #  blob                                       lines  bytes  path                                         vs 3a6a10b
 1  31e785f8f9dbe5d8712dd213b109357c77d115b4     240  18969  document-harness/CONSTRUCTION-CHECKLIST.md   CHANGED (was cacd99d4)
 2  7591c5332d170a286a15ef6a699f69cc80def755      40  11021  document-harness/README.md                   same
 3  3908907a73710fe6b3673da043d1cf521a7322f3     518  36625  document-harness/EXECUTION.md                CHANGED (was ab261698)
 4  c84b82889683f3865891776fe7f20cfb16fdd59c     318  20589  document-harness/REVIEW.md                   CHANGED (was 35fe0abc)
 5  9a67401f12da68b8990c4543867f204163d12e32     119   8382  document-harness/ORCHESTRATION.md            CHANGED (was 48f665c4)
 6  6d5714923870b4e13e8928221a80df68e563a5ed       5    511  migration/…/v3-harness-operating-contract.md same
 7  29bdc9fbde6e8db38d601dd2340d4b46a24a296f       5    924  migration/…/v3-harness-review-contract.md    same
 8  68031fa2ca31272e31da0d42a9a02189d28fcc21     124   6480  contract/…-supersession-1.md                 same
 9  e1a2f26b1d8d323d11e900f8137dea222b6571c1     113   7421  contract/…-supersession-2.md                 same
10  09aa869962f592c2f86c9379be0ef3eb7d2232ff      44   2812  schema/…/paragraph-map.schema.json           same
                                              -----
                                               1526  total lines read
```

**Where the four changes came from.** `git log 3a6a10b..b8df15a -- <the ten>` returns exactly
two commits, `7cb7213` (`V3-PRERUN-RIDERS-v1`) and `860729f` (`V3-PRERUN-RIDERS-FIX-v1`); their
diffs over the four members were read in full alongside the standing text. The round that ends
at the subject commit, `PUB-FACADE`, **touched no member** — including its free-channel
application `a3ef5ee`, which lands in `README.md` (root, not the member),
`document-harness/ONBOARDING.md` and `tooling/tests/document_harness/test_precommit_hook.py`.
So no layer application rides into this read at per-member digest cost (`E10`).

`HARNESS-DECISIONS.md` is **not** a member — `E10`'s tail owes it at a round's opening while
denying it membership. It is cited by section, never by blob.

## 3. What was checked, and what the commands returned

Scope declaration (`HD-41` ①) precedes each assertion. Unless a line says otherwise, the scope
is **the ten member blobs at `b8df15a`** and nothing else.

### 3.1 `E2`'s freeze surface

Scope: `git ls-tree b8df15a` over `contract/` and `schema/document-assurance-v3/`.

```
68031fa2ca31272e31da0d42a9a02189d28fcc21  contract/…-supersession-1.md
e1a2f26b1d8d323d11e900f8137dea222b6571c1  contract/…-supersession-2.md
b2dbdf752d8c155e4c65b14b5f420b880b8184a1  contract/Document-Work-Assurance-Contract-v3.md
schema/document-assurance-v3/ : 15 files
```

All three named blobs verify against `E2`'s text (`b2dbdf75…`, `68031fa2…`, `e1a2f26b…`), and
`contract/` holds exactly those three — which `document-harness/README.md:20` also asserts. The
pack holds fifteen, and `paragraph-map.schema.json` — the one `E2` names by path — is among
them. `README.md:22`–`:25` enumerates fifteen across its four schema rows (8 + 2 + 4 + 1); the
enumeration and the freeze surface agree.

**Ceiling, stated rather than folded in** (`R4`). `E2` freezes what the pack held **at the
2026-08-03 re-baseline**, and this repository's history begins `345acdd` (2026-08-15,
`initial: … extracted`). Whether today's fifteen are that day's fifteen is **`UNVERIFIABLE`
from here**. What *is* establishable: `git log --diff-filter=AD -- schema/document-assurance-v3/`
returns only `39a21a8`'s re-rooting (all fifteen added at the new path in one rename), so no
pack file has been added or removed anywhere in this repository's history, and the count `E2`
writes into itself matches.

### 3.2 Every path reference in the layer, resolved

Two scopes, because the guard covers one and `E10`'s clause covers the other. Both were run
over the **whole standing text** of all ten members, which is precisely the stock `E10` says
the guard never re-scans.

**(a) Backtick path tokens**, driven through the guard's own predicate
(`layer_path_check.unresolved_tokens`) rather than through a staged diff:

```
CONSTRUCTION-CHECKLIST 0 · README 0 · EXECUTION 0 · REVIEW 0 · ORCHESTRATION 0
operating-contract 0 · review-contract 0 · paragraph-map.schema.json 0
supersession-1: 2   ResearchSystem/…/W2/W2-design.md · ResearchSystem/…/W2/W2-record.md
supersession-2: 3   assurance/runs/ · templates/run-v2/ · ResearchSystem/migration/document-work-assurance-v3/
TOTAL 5
```

All five sit inside the two `E2`-frozen supersessions, which `E10`'s final clause excepts
*while they are frozen*. **Outside the frozen bytes the count is zero**, the four changed
members included. The five are the rider `frozen-path-prefix` set, unchanged in number and
location.

**(b) Relative markdown links** — the blind spot `E10` names by name:

```
56 links checked (http/https/anchor-only excluded); broken: 0
```

Zero broken, frozen bytes included. The count rose from the previous read's 53 by the links
`ORCHESTRATION.md`, `EXECUTION.md` and `REVIEW.md` gained under `PRERUN-RIDERS`.

**(c) Placeholder-segment tokens** — held by `E10`'s clause alone, since the path shape admits
no angle brackets (§3.8). Eleven in the layer, each checked by hand for the clause's
requirement that a caller-held artifact be *given its name and its holder*:

| token | member | holder / resolution |
|---|---|---|
| `V3-<ROUND>-v1`, `V3-REVIEW-RECORD-<ROUND>-<sha>-v1` | checklist | commit titles, not paths |
| `v3-review-{full,verify}-<subject-sha>.md`, `v3-checkpoint-read-<sha>.md`, `v3-cold-read-<sha>.md` | checklist | `R6` writes the directory: this repository |
| `R<n>` ×2, `<round>` | EXECUTION, REVIEW | section / value names, not paths |
| `<control root>/control/paragraph-map.json` | EXECUTION | *"the control root lives in the caller, not here"* — adjacent |
| `<control root>/evidence/review-full.json` | REVIEW | *"the control root lives in the caller"* — adjacent |
| `v3-review-<round>-<subject short SHA>.md` | REVIEW | *"The caller holds it; this layer does not write its path"* |

Spot-resolved by hand besides: `migration/…/W2/W2-record.md`, `…/N0/N0-record.md`,
`…/N1/N1-record.md`, `…/N2/N2-record.md`, `…/N0/fixtures/cases.json`,
`document-harness/history/REVIEW-v1-package-flow.md`,
`document-harness/journal/retro-2026-08-03.md`,
`document-harness/plans/harness-deletion-first-stabilization.plan.md`,
`document-harness/ONBOARDING.md`, `CONSTRUCTION-LEDGER.md`, `HARNESS-RIDERS.md`,
`HARNESS-DECISIONS.md` — all present at `b8df15a`.

### 3.3 The membership sentence and its mirrors (`E10-sync`)

Scope: `E10`'s sentence as hand-transcribed by this reader against `layer_path_check.LAYER`.

```
E10 (hand-transcribed) == LAYER : True | n = 10 | distinct = 10
```

The guard's `LAYER` tuple and its docstring's *"The member list mirrors E10's membership
sentence"* both hold. Machine-side copies of the member list re-derived by grepping
`tooling/` for two member paths: `layer_path_check.LAYER` and
`test_precommit_checks.py`'s `EXPECTED` carry the full list, and
`test_precommit_hook.py:58`'s `MEMBER` carries one member path — the fourth machine-side copy
the rider `E10-sync` already records from `v3-review-verify-71e1f24.md` `O-2`. All are
hand-written literals, which is `E5`'s independence requirement met.

### 3.4 Rule enumerations and the counts the members state about themselves

```
E-rules in CONSTRUCTION-CHECKLIST.md      : 12  (E1…E12, all distinct)
R-rules in CONSTRUCTION-CHECKLIST.md      : 10  (R1,R2,R3,R9,R10,R4,R5,R6,R7,R8 — complete)
ORCHESTRATION.md "nine obligations" table :  9 data rows
ORCHESTRATION.md "three obligations"      :  3 subsections
ORCHESTRATION.md roles table              :  3 rows
EXECUTION.md run-template sections        :  6  (:181 :204 :252 :289 :339 :438)
```

9 + 3 = 12 matches `README.md:26`'s *"nine of its twelve obligations"*. `E10`'s *"exactly these
ten paths"* enumerates ten. `README.md:26`'s six run-template sections — pre-freeze gate ·
instruction form · authoring gate · audit cadence · regression-battery tiering · instruction
authoring rules — are the six headings between `EXECUTION.md:181` and `:438`, in that order,
which is also the span its own stage marker at `:173` claims. The R-rules are written out of
numeric order; the set is complete and the grouping legible, so this is not reported.

Each of the nine obligation rows was read against the rule it names, and each holds — including
the two that are not simple pointers: row 6 splits *title* (`R6`) from *lands unchanged*
(`R1`'s **reported through** holding), and both texts bear that split; row 9 points outside the
layer to `HD-2`, which the decision log's header carries as its state-machine invariant.

### 3.5 `HD` ids and commit ids cited in the layer

Scope: every `HD-\d+` token, and every backtick token of 7–40 hex characters, in the ten
members.

```
HD ids cited: 15 distinct — HD-1 HD-2 HD-5 HD-7 HD-14 HD-20 HD-28 HD-34 HD-35
                            HD-39 HD-41 HD-42 HD-47 HD-52 HD-55.   Dangling: 0
  §live 3 (HD-34 HD-35 HD-41) · §implemented 8 · archive 4 (HD-14 HD-28 HD-39 HD-42)

commit ids: 12 distinct.  Resolves here: 0d73a5f (commit) — EXECUTION.md, the instrument base.
  Absent here (11): 418b89c 6fd0ae3 7011916 820b287 838c413 9ba9bbc a22cca0 a8af54c
                    ac1b383 cf51534 ddd773a
```

Fourteen ids were cited at the previous read; `HD-55` is the fifteenth, added by the
`PRERUN-RIDERS` carriers, and it resolves — in `§implemented`, having moved there in the same
commit as its carrier per `HD-2`. The commit-id split is exactly the shape `E10`'s *Where a
cited commit id resolves* clause predicts, and the root `README.md` §*Where the bytes came
from* (`:14`) exists and names the repository the eleven belong to — `D:/Thesis`, worktree,
branch and commit `e4ffa2b` — including that `7011916` is absent here. `EXECUTION.md:407`
names its two bases explicitly (*instrument* `0d73a5f`, *caller* `6fd0ae3`), which is the
clause's "a citation naming its own repository is read as written" half exercised.

### 3.6 Factual assertions in the layer, run rather than read (`E3`)

Scope: the assertions in the members that name a command or a countable property of *this*
repository.

```
$ python -m pytest -q            # run from tooling/, per EXECUTION.md's battery bullet
793 passed in 94.18s

$ python -m pytest -q            # run from the repository root (what .github/workflows/ci.yml runs)
793 passed in 97.27s

$ python validate_fixtures.py    # migration/document-work-assurance-v3/N0/fixtures/
41/41 cases behaved as declared; failures=0
```

- **The instrument battery leg is green at the subject commit.** `793` is this read's own
  measurement; the previous read measured `790`, and the growth is `PUB-FACADE`'s
  `test_precommit_hook.py` tests. Not a finding: the same paragraph disclaims its own tally
  (*"Re-run the battery for a current figure rather than trusting any list written here"*).
- `README.md:35`'s *(41/41 green)* re-derives exactly.
- The two invocation forms collect the same 793 here — see `O-2`.
- **`EXECUTION.md`'s name-collision warning re-derives.** Its five caller legs are *named, not
  written as paths*, and it warns *"A name here may also belong to an unrelated file in this
  repository."* Measured: `run_tests.py` matches two tracked files here
  (`tooling/tests/document_harness/`, `tooling/tests/document_harness_review/`) and
  `validate_fixtures.py` one (`migration/…/N0/fixtures/`) — the collision the sentence
  anticipates is real and present, and the sentence is what keeps it from misleading.

### 3.7 The claims the layer makes about the dispatch code

`ORCHESTRATION.md` is the member that makes factual claims about `dtw dispatch`, and all of
them were run (`E3`).

```
dispatch.py:429  ROLE_INSTRUCTION              = "document-harness/REVIEW.md"
dispatch.py:548  CONSTRUCTION_ROLE_INSTRUCTION = "migration/…/v3-harness-review-contract.md"
dispatch.py:770  EXECUTOR_ROLE_INSTRUCTION     = "document-harness/EXECUTION.md"
dispatch.py:776  CONSTRUCTION_EXECUTOR_CHARTER = "document-harness/CONSTRUCTION-CHECKLIST.md"
cli.py:580–601   mutually exclusive, required: --subject · --range · --read · --executor
                 · --construction-executor                                        (5 modes)
test_dispatch.py:398,463,522,570,675  CHARTER_OUTSIDE / MEMBER — hand-written literals (E5)
tooling/tests/fixtures/expected-{construction,read,executor,construction-executor}-prompt.txt
                 each carries `{charter}` exactly once, as a substitution
```

- *"three review-side modes, and two executor-side modes, one per side of the work"* verifies
  exactly: five flags in one mutually-exclusive group, split 3 / 2 as stated.
- *"the product-run executor's charter is `EXECUTION.md`, the construction-round executor's is
  `CONSTRUCTION-CHECKLIST.md`"* verifies against the two constants above.
- **The stub's three claims (member 7) all hold**: `dispatch.CONSTRUCTION_ROLE_INSTRUCTION`
  hard-codes its path; `CHARTER_OUTSIDE` (`:398`, `:522`) and `MEMBER` (`:463`) pin it with
  hand-written literals rather than importing the module constant; and the construction
  dispatch fixture carries `{charter}` as a substitution, not the path.
- **`"no dispatch prompt names it, and none should"` verifies, and the scope is the whole
  dispatch module, not the fixtures alone.** `grep -ri orchestrator tooling/rsclib/` returns
  zero hits, so none of the four prompt constants — `CONSTRUCTION_PROMPT`, `READ_PROMPT`,
  `EXECUTOR_PROMPT`, `CONSTRUCTION_EXECUTOR_PROMPT` — nor any other emitted text names the
  role. The prompt that produced this read matches
  `tooling/tests/fixtures/expected-read-prompt.txt` line for line; see `O-5` for what arrived
  around it.

### 3.8 The guard's described blind spots, exercised rather than read

`E10` makes an unusually precise claim about what `layer_path_check` cannot see. Each half was
driven through the real predicates:

| `E10` says | exercised result |
|---|---|
| a placeholder segment falls outside its path shape | `PATHLIKE.match("<control root>/control/paragraph-map.json")` → `False` ✔ |
| markdown links carry no backtick token | `TOKEN.findall("[a](docs/nowhere.md)")` → `[]` ✔ |
| `++ b/…` mis-files the member's remaining added lines | added content `++ b/evil` → `{'evil': ['`a/nowhere.md`']}` ✔ |
| any other `++ …` silences them | added content `++ other` → `{}` ✔ |
| the standing text it never re-scans stays unscanned | `check()` reads only `added_lines_by_path`, never a file ✔ (scanned here instead, §3.2a) |
| the bytes `E2` freezes are excepted while frozen | consistent with §3.2a's five ✔ |

The docstring's further claim that a *pasted* header (content `+++ …`, rendering `++++ …`) is
handled was exercised too: the following lines stayed filed under the real member.
`.harness/` exemption present (`RUNTIME_PREFIX`), and an escaping token (`../../README.md`)
is correctly reported as resolving nowhere.

**Scope correction, recorded because it nearly produced a false must-fix** (`HD-41` ①). The
first run of the two `++ ` rows fed the parser the added line's *raw content* where `git diff`
emits a `+`-prefixed *rendered* line; both rows came back "no mis-filing", which read as `E10`
over-claiming. The construction was wrong, not the claim: content `++ b/evil` renders as
`+++ b/evil`, which is what the parser sees. Re-run with the rendering applied, all three
branches behave exactly as `E10` describes. No finding rests on the first run.

### 3.9 The carriers and dependencies the previous round left outstanding

Scope: the three items the previous read and the `PRERUN-RIDERS` / `PUB-FACADE` records left
open against layer text.

- **`HD-55`'s carrier has landed at all three sites.** `ORCHESTRATION.md:26`–`:32` (the
  sentence under the three-roles table, its `home`), `E1`'s rewritten **exception channel**
  paragraph, and `ORCHESTRATION.md:112`–`:115` (*What the orchestrator may never do*, first
  bullet, no longer writing the merged form as ordinary). The third is the site the previous
  read's `O-1` enumerated. `HD-55` moved to `§implemented` in the carrier commit, per `HD-2`.
- **The C4 `O-1` dependency is intact.** `EXECUTION.md`'s *Authoring gate* sampling paragraph
  points at `CONSTRUCTION-LEDGER.md`'s conversation-only list for the three-branch re-ruling;
  that row is present at `CONSTRUCTION-LEDGER.md:107`–`:110`, carrying exactly those three
  branches. The dependency `v3-review-verify-3dd226b.md` `V-3` flagged has not been broken by
  two closeouts since.
- **The `plan-delivery` gap is closed, not banked.** `ORCHESTRATION.md`'s *Handing the executor
  its instruction* now enumerates *"instruction, subject and governing plans"* and gives the two
  reasons; `EXECUTION.md`'s delivery half-sentence now points back at it by name. Measured:
  `plan` occurs 5× in `ORCHESTRATION.md`, four of them in that section as a deliverable. The
  rider row is absent from `HARNESS-RIDERS.md`, which is redemption in the shape `R10` asks for.
  The previous read's `O-2` no longer describes the text.

## 4. Findings

### `L-1` (low) — `R6` names two read-record forms and no member says which applies when

`R6` writes the record channel as *"you write `v3-review-{full,verify}-<subject-sha>.md` (or
`v3-checkpoint-read-<sha>.md` / `v3-cold-read-<sha>.md`)"*. Scope: every occurrence of
`cold read`, `checkpoint` and `read` as a record kind across the ten members.

- `E10` defines **cold read** — *"a cold read of this layer is owed at each round's opening"*.
- **checkpoint read** is defined nowhere in the layer. The only other occurrence of the word in
  a member is inside frozen supersession-1 (`:21`, *"every checkpoint read of the v3
  construction itself"*), which uses it without defining it.
- `E10` separately describes a second read kind without naming it — the amendment read, whose
  *"subject is the amendment text itself, never the work it governs"*.

**The downstream decision that goes wrong** (`R9` requires it named). `E10`'s citation clause
covers *"a member whose blob is unchanged since a recorded **end-to-end** read of it"*. An
amendment read is by construction not end-to-end. The record filename is the cheap index a
later reader uses to find prior coverage; with no stated criterion, a partial read filed under
the cold-read name would look citable, and a full one filed under the checkpoint name would be
passed over. Nothing has gone wrong yet — the practice is unambiguous across the 57 committed
read records (40 checkpoint, 17 cold), and every record discloses its own coverage under `R4`,
which is what a citing reader must actually read. So this is a hole in the text, not a live
defect: **low, not must-fix**.

**Routing.** Not wording-level under `R9` — the fix changes which filename an actor writes, and
the fact it would fix is recoverable only from precedent, not from adjacent text. This record
supplies no bytes: writing the criterion adds a clause to `R6` or `E10`, and `E10` makes that
design, which opens a round. Per `R10` it therefore **banks** — a rider naming `R6` and `E10`'s
cold-read sentence as targets, redeem-when the next round-eligible batch touching the checklist
(`R10`'s rule that a design-fix rider names a round-eligible surface, never any batch). No
deadline: no moment can be named at which it starts to bite.

### `O-1` (observation) — rider `py-convention` still describes `EXECUTION.md:364` exactly

Scope: every bare `python` invocation in the ten members.

One hit, `EXECUTION.md:364`: the instrument battery leg is written `python -m pytest -q`. Stock
Ubuntu ships only `python3`, which is the measurement `PUB-FACADE` made on a wired clone when
the same bare form in `.githooks/pre-commit` failed every commit with exit 127 — that hook now
probes `python3` then `python` and the member does not. A POSIX executor following the member's
sentence verbatim runs a command that does not exist.

Already banked and correctly routed: `HARNESS-RIDERS.md:44` (`py-convention`, source the
`PUB-FACADE` closeout) names this exact line as an `E10` member, gives the fix shape (batch A's
one-sentence convention covering the file, as the root `README.md:49`–`:52` now carries), and
records that the member bytes ride `E10`'s free channel and owe a read. Re-derived here and
found accurate in both halves, so a future read need not re-open whether the row still
describes the text. Nothing to route.

### `O-2` (observation) — two invocation forms of the one enumerated battery leg, both green

Scope: `EXECUTION.md`'s *Regression-battery tiering* bullet against every in-tree invocation of
the instrument's leg.

The member enumerates the instrument's leg as `python -m pytest -q` **run from `tooling`**, with
the parenthetical reason *"from a repository root that also carries the product, collection
aborts"*, and closes *"One command, and nothing fewer."* Two in-tree callers now use the other
form: `.github/workflows/ci.yml:27` (added by `PUB-FACADE`) and the root `README.md:56` table
row, both `python -m pytest -q` from the repository root.

Measured rather than reasoned: **793 passed both ways** (94.18s from `tooling`, 97.27s from
root). The member's reason is caller-specific — this repository does not carry the product —
so the divergence is benign here and neither text is false. Recorded because `HD-42` treats
that enumeration as fixed and this is a second, differently-formed invocation of the one leg it
names, standing in the tree with no text acknowledging it; the day the CI form and the
enumerated form disagree, nothing in the layer says which is owed. Whether the enumeration
should acknowledge CI is a design question and therefore the user's (`R5`), not this read's.

### `O-3` (observation) — a wording-level finding that supplies bytes still matches two routes

`R10` routes findings in an ordered list: *"`E10`'s must-fix channel takes must-fix, R9 takes
wording-level, the `E10` free channel takes … any finding whose record supplies the exact bytes
… and the bank takes what is left."* A finding that is both wording-level **and** supplies exact
bytes matches two entries. `R9` says such a finding *"rides the next batch touching this
layer"*; the free channel says *"applied immediately … reported after the fact and reversible"*.

Reached independently here before the previous read's record was opened, and it is that read's
`O-3` unchanged — both rule texts are byte-identical at this commit. The outcomes agree on what
matters (neither opens a round, neither spends budget), and reading the list as ordered
resolves the timing. Recorded as a tension a reader may not resolve the same way, not as a
defect: no actor is currently acting on it.

### `O-4` (observation) — the bare-name class is outside the guard's shape by design, and its holders are carried by paragraph

Scope: every backtick token in the ten members that has a file extension but no `/`.

The guard skips them — `unresolved_tokens` requires `"/" in token` before `PATHLIKE` even runs,
exercised: `` `run_p4_tests.py` `` → `[]`, `` `a/nowhere.md` `` → flagged. That is correct and
deliberate: `E10` **requires** the bare-name form for a caller-held artifact (*"a caller-held
path is named, never written as a path token"*), so the class it is not scanning is the class
the rule mandates. `E10`'s *"What the guard still cannot see"* list is accurate as written —
this class is held by the clause, which is where the sentence puts it.

The ceiling is on the holder half, which nothing machine-checks. Of the bare names in the layer,
most carry their holder adjacently (`smoke_test.py` — *"in the caller that grew this harness,
the ExperimentLab papers tree"*; `run_p4_tests.py`, `run_p5a_tests.py`, `rsc.py` — *"their
scripts live in the caller's tree"*; `audit-rounds.md`, `v3-review-full-86defbc.md`,
`v3-review-full-fef3a2e.md` — each with an explicit *held in the caller* sentence). Three do
not, and inherit their holder from a section-opening sentence one or more bullets away:
`build_run.py` and `check_shells.py` (`EXECUTION.md:194`, `:199`, under the *Pre-freeze gate*
head at `:186`) and `write_audit.py` (`:304`, holder carried only by *"the run's"*). None is
wrong; all three would be invisible to every scan in §3.2 if they became so. Recorded as the
measured ceiling of this read's path coverage, not as a defect.

### `O-5` (observation) — the dispatch carried a wrapper the generated prompt says it does not

`R2` makes chat-only load-bearing material a finding, so this was checked rather than assumed.
The generated read dispatch is exactly `tooling/tests/fixtures/expected-read-prompt.txt`, whose
own closing sentence is *"none of it is restated here, because a fact you were handed is a fact
you did not check."* The prompt this reader received carried an additional trailing parenthetical
from the orchestrator's session, restating three things: where the repository is, that the
record is written to the worktree and committed by the orchestrator (`R6`), and that the final
message state the findings tiering (`R3`).

**Not a finding**, because none of it is load-bearing: every clause is re-derivable from `R6`
and `R3`, which this reader read first and independently, and the transport fact is checkable.
Recorded because the gap between what the generated prompt asserts about itself and what the
handoff actually carried is the kind of drift that would matter the first time such a wrapper
carried something the layer does not say — at which point it *is* the `R2` finding.

## 5. Coverage — what was read in full, what was sampled, what was only probed (`R4`)

- **Read in full at the subject blobs:** all ten members, 1 526 lines. Blob ids in §2. No member
  was covered by citation, though six were eligible.
- **Read in full outside the member set:** `HARNESS-DECISIONS.md` lines 1–134 (header + `§live`,
  seven entries) plus `HD-55`'s `§implemented` entry; `tooling/hooks/layer_path_check.py`;
  `.githooks/pre-commit`; `.github/workflows/ci.yml`;
  `tooling/tests/fixtures/expected-read-prompt.txt`; `v3-cold-read-3a6a10b.md`; the subject
  commit's body; the full member diffs `3a6a10b..b8df15a`.
- **Sampled:** `CONSTRUCTION-LEDGER.md` (header and the current-pointer tail `:100`–`:152` in
  full, the CLOSED roll skimmed); `HARNESS-RIDERS.md` (rows `E10-sync`, `py-convention`,
  `fixleg-scan-raw` in full, the rest by id); root `README.md:1`–`:96`;
  `document-harness/ONBOARDING.md:1`–`:12`;
  `migration/document-work-assurance-v3/supersession-2-signature.md:1`–`:25`;
  `schema/document-assurance-v3/harness-issue.schema.json` (the `observed_after` block);
  `tooling/rsclib/document_harness/dispatch.py` (four role constants, four prompt constants),
  `cli.py:575`–`:604`, `test_dispatch.py` (the `CHARTER_OUTSIDE` / `MEMBER` literals);
  `git show --stat` of `87004fb` and `a3ef5ee`.
- **Probed only:** `HARNESS-DECISIONS.md` `§implemented` and `HARNESS-DECISIONS-archive.md` —
  grepped for the fifteen ids the members cite (§3.5), never read end to end;
  `tooling/tests/document_harness/test_precommit_checks.py` — its `EXPECTED` located by grep,
  not re-opened, its blob being unchanged since the previous read verified it;
  `document-harness/plans/` — not read, deliberately, since `R2` says the read re-derives rather
  than inherits; the `PRERUN-RIDERS` FULL and VERIFY records — not opened, for the same reason.
- **Not established (`UNVERIFIABLE`, stated rather than folded in):** whether today's fifteen
  pack files are the 2026-08-03 re-baseline's fifteen — this repository's history begins
  2026-08-15 (§3.1); whether the caller repository's five battery legs are green — their scripts
  are not here and `EXECUTION.md` says they are not owed here; whether the caller's hook calls
  two checks and not three (`README.md:36`) — caller-side; whether CI passes — it has never run,
  the first push being the outstanding user action `PUB-FACADE`'s closeout records, so the badge
  in root `README.md:3` has no status behind it and this read makes no claim about it.
- **Process claims are marked, not verified** (`R4`): that this read ran in a fresh context is a
  declared identity, not something the repository can lock.
