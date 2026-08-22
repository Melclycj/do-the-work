# Cold read — the instruction layer at `693b692`

**No verdict.** A read is not a round (`R3`): it spends no budget, carries no verdict, and its
output is findings tiered must-fix / low / observation. This is the read `E10` owes at the
opening of round `EXECUTOR-CHARTER`. Nothing below certifies any text, and nothing below is
banked as any round's FULL.

**Findings: 0 must-fix, 1 low, 4 observations.** The low is a drift the round that created it
did not notice: `EXECUTION.md`'s doc-only tier exception names two code-pinned doc paths, and
the repository now has **five** — the two it names plus three the `dtw init` round and the
shipped resolver added. `HD-45` ②'s criterion already covers all five, so the text, not the
rule, is what is behind. No must-fix: nothing in the layer's bytes acts wrongly today, and the
low does not bite this round (its change surface is tooling-touching regardless).

**The citation channel was available and was not taken.** All ten member blobs are
byte-identical to those `v3-cold-read-39e395e.md` records (§2), so `E10`'s citation clause
would have covered every member. This read re-read all ten end to end anyway: the marginal
product of a covered read is a second independent judgement of the same bytes, and that is
what found `L-1`.

**Standing instructions read.** `migration/document-work-assurance-v3/v3-harness-review-contract.md`
(the stub, member 7) → `document-harness/CONSTRUCTION-CHECKLIST.md` in full, both sides, per the
stub's *"It is your standing instruction and its own counterpart; read all of it."*
`HARNESS-DECISIONS.md` `§live` (lines 28–151, **eight** entries — `HD-52`, `HD-44`, `HD-41`,
`HD-36`, `HD-35`, `HD-34`, `HD-23`, `HD-9`) plus the file header (1–27) that states its own
state machine, which `E10`'s tail requires. `§live` gained `HD-52` since the previous read's
seven. `§implemented` (152–519) and `HARNESS-DECISIONS-archive.md` were **not** read end to
end — they were grepped for the ids the members cite (§3.5). Cited by section, never by blob.

---

## 1. What the subject is, and how it was derived

The dispatch supplied one commit and nothing else. Everything below was re-derived (`R2`); no
figure from the queue-head brief was accepted as given, and the two that this read re-measured
independently (ten-member byte-identity, `774 passed`) are reported in §3 with their commands.

```
$ git rev-parse --show-toplevel
D:/Project/Ongoing/do-the-work

$ git rev-parse HEAD
693b692811b5958dbcda92a3cc722123c5f44337

$ git status --porcelain=v1
(empty)

$ git log -1 --format='%H%n%ci%n%s' 693b692811b5958dbcda92a3cc722123c5f44337
693b692811b5958dbcda92a3cc722123c5f44337
2026-08-22 03:08:54 +1000
V3-EXECUTOR-CHARTER-BRIEF-COLDCHECK-v1
```

HEAD is the subject commit and the worktree is clean, so the worktree bytes are the subject
bytes — verified per member rather than inferred (§2).

## 2. The member set and each member's blob

The set is `E10`'s own sentence, hand-transcribed from the checklist and not taken from the
guard that mirrors it; the transcription was then machine-compared against the guard (§3.3).
Blob ids per `E10`'s *"a read's record states the blob id of each member it read, because
citation depends on it"*.

```
$ git rev-parse "693b692:<path>"   /   git cat-file -s   /   wc -l
1  cacd99d49d80ce4bf33e94b733a07f1dd6b247e8   235 lines   18531 B  document-harness/CONSTRUCTION-CHECKLIST.md
2  7591c5332d170a286a15ef6a699f69cc80def755    40 lines   11021 B  document-harness/README.md
3  27f4fc82a556f26804ee5236204f746bd99da5bd   474 lines   32987 B  document-harness/EXECUTION.md
4  35fe0abcd7123f4a37a88ef4de605b3aad3cfe75   288 lines   18209 B  document-harness/REVIEW.md
5  80f42658a2961eeb10a168bd7bd729121c6c05ae    95 lines    6389 B  document-harness/ORCHESTRATION.md
6  6d5714923870b4e13e8928221a80df68e563a5ed     5 lines     511 B  migration/document-work-assurance-v3/v3-harness-operating-contract.md
7  29bdc9fbde6e8db38d601dd2340d4b46a24a296f     5 lines     924 B  migration/document-work-assurance-v3/v3-harness-review-contract.md
8  68031fa2ca31272e31da0d42a9a02189d28fcc21   124 lines    6480 B  contract/Document-Work-Assurance-Contract-v3-supersession-1.md
9  e1a2f26b1d8d323d11e900f8137dea222b6571c1   113 lines    7421 B  contract/Document-Work-Assurance-Contract-v3-supersession-2.md
10 09aa869962f592c2f86c9379be0ef3eb7d2232ff    44 lines    2812 B  schema/document-assurance-v3/paragraph-map.schema.json
                                             1423 lines total
```

**Worktree identity, per member.** `git hash-object <path>` equals `git rev-parse
693b692:<path>` for all ten (`MATCH` × 10). The read was therefore performed on the worktree
bytes with the subject bytes established, not assumed.

**Byte-identity with the previous recorded read.** All ten ids above equal the ten
`v3-cold-read-39e395e.md` §2 records. The brief's opening condition holds; it was re-derived,
not taken.

`HARNESS-DECISIONS.md` (blob `602df01438cf8530268b82459153efda73abcc88`, 519 lines) is **not**
a member — `E10`'s tail owes it at a round's opening while denying it membership, and `HD-19`
records the same. It is listed here for the record's completeness and is cited by section,
never by blob, exactly as that clause requires.

## 3. What was checked, and what the commands returned

Scope declaration (`HD-41` ①) precedes each assertion. Unless a line says otherwise, the
scope is **the ten member blobs at `693b692`** and nothing else.

### 3.1 `E2`'s freeze surface — three blobs and one directory

Scope: `git ls-tree 693b692` over `contract/` and `schema/document-assurance-v3/`.

```
100644 blob 68031fa2ca31272e31da0d42a9a02189d28fcc21  contract/…-supersession-1.md
100644 blob e1a2f26b1d8d323d11e900f8137dea222b6571c1  contract/…-supersession-2.md
100644 blob b2dbdf752d8c155e4c65b14b5f420b880b8184a1  contract/Document-Work-Assurance-Contract-v3.md

$ git ls-tree --name-only 693b692 schema/document-assurance-v3/ | wc -l
15
```

All three named blobs verify against `E2`'s text (`b2dbdf75…`, `68031fa2…`, `e1a2f26b…`), and
the pack holds exactly the fifteen the re-baseline clause names — `HD-44`'s eighteen items
(3 + 15), present and in this repository, which is the fact `HD-44` exists to keep true after
the split. `contract/` holds exactly three files, which is `README.md:20`'s claim, re-derived.

### 3.2 Every path reference in the layer, resolved

Two scopes, because the guard covers one and `E10`'s clause covers the other.

**(a) Backtick path tokens, whole standing text of all ten members** — the guard's own
predicate (`layer_path_check.unresolved_tokens`) driven over complete files rather than over a
staged diff's added lines. This is precisely the stock `E10` says the guard never re-scans and
the clause alone holds.

```
CONSTRUCTION-CHECKLIST.md 0 · README.md 0 · EXECUTION.md 0 · REVIEW.md 0 · ORCHESTRATION.md 0
operating-contract 0 · review-contract 0 · paragraph-map.schema.json 0
supersession-1: 2   :7  ResearchSystem/migration/document-work-assurance-v3/W2/W2-design.md
                    :123 ResearchSystem/migration/document-work-assurance-v3/W2/W2-record.md
supersession-2: 3   :60  assurance/runs/
                    :99  templates/run-v2/
                    :110 ResearchSystem/migration/document-work-assurance-v3/
TOTAL 5
```

All five sit inside the two `E2`-frozen supersessions, which `E10`'s final clause excepts
*while they are frozen*. **Outside the frozen bytes the count is zero.** The five are the
rider `frozen-path-prefix` set, unchanged in number and location since that row was written —
a re-measurement that confirms the row's scope rather than a new finding.

**(b) Relative markdown links, whole standing text of all ten members** — the blind spot
`E10` names by name (*"prose and markdown links carry no backtick token for it to find"*).

```
51 links checked (http/https/anchor-only excluded); broken: 0
```

Zero broken, frozen bytes included.

### 3.3 The membership sentence and its mirrors (`HD-22`)

Scope: `E10`'s sentence as hand-transcribed by this reader, `layer_path_check.LAYER`, and
`test_precommit_checks.py`'s `EXPECTED`.

```
E10 (hand-transcribed by this reader) == LAYER : True | n = 10
test_precommit_checks.py:226-239  EXPECTED  — hand-written literal, asserted == LAYER (E5)
```

Three mirrors, all agreeing, and the test-side one is a hand-written literal rather than the
module's own tuple, which is what `E5` requires and what its docstring claims. `HD-22`'s
three-mirror shape holds.

### 3.4 Rule enumerations and the counts the members state about themselves

```
E-rules in CONSTRUCTION-CHECKLIST.md : 12  (E1…E12, all distinct)
R-rules in CONSTRUCTION-CHECKLIST.md : 10  (R1,R2,R3,R9,R10,R4,R5,R6,R7,R8 — complete)
ORCHESTRATION.md "nine obligations" table : 9 data rows
ORCHESTRATION.md "three obligations" subsections : 3
ORCHESTRATION.md roles table : 3 rows
```

9 + 3 = 12 matches `README.md:26`'s *"nine of its twelve obligations"*. `E10`'s *"exactly
these ten paths"* enumerates ten. The R-rules are written out of numeric order (R9 and R10 sit
after R3); the set is complete and the grouping is legible — R3 introduces the read's finding
tiers and R9/R10 say where those findings go — so this is not reported as a finding.

### 3.5 `HD` ids the members cite

Scope: every `HD-\d+` token in the ten member blobs.

```
HD-1 HD-2 HD-5 HD-7 HD-14 HD-20 HD-28 HD-34 HD-35 HD-39 HD-41 HD-42 HD-47   (13 distinct)
§live: HD-34 HD-35 HD-41                                      (3)
§implemented: HD-1 HD-2 HD-5 HD-7 HD-20 HD-47                 (6)
archive: HD-14 HD-28 HD-39 HD-42                              (4)
```

Thirteen cited, thirteen resolve, none dangling.

### 3.6 Commit ids cited in the layer

Scope: backtick tokens of 7–40 hex characters without an ellipsis, in the ten member blobs.
`E2`'s `b2dbdf75…` / `68031fa2…` / `e1a2f26b…` carry ellipses, are blob ids, and are excluded.

```
12 distinct.  Resolves here: 0d73a5f (commit) — EXECUTION.md:387, the instrument-side base.
Absent here (11): 418b89c 6fd0ae3 7011916 820b287 838c413 9ba9bbc a22cca0 a8af54c ac1b383
                  cf51534 ddd773a
```

This is exactly the shape `E10`'s *Where a cited commit id resolves* clause predicts, and the
root `README.md` §*Where the bytes came from* (lines 12–20) names the repository the eleven
belong to and why the history stayed there. The one that resolves is the one the text calls
the instrument's own base, and the caller-side base beside it (`6fd0ae3`) does not — the
sentence at `EXECUTION.md:387-388` is right about both halves.

### 3.7 Factual assertions in the layer, run rather than read (`E3`)

Scope: the assertions in the members that name a command or a countable property of *this*
repository.

```
$ python -m pytest -q            # run from tooling/, per EXECUTION.md:344-346
774 passed in 104.18s (0:01:44)

$ python validate_fixtures.py    # migration/document-work-assurance-v3/N0/fixtures/
41/41 cases behaved as declared; failures=0     exit=0
```

- **The instrument battery leg is green at the subject commit**, and `774` is this read's own
  measurement, not the brief's figure repeated.
- `EXECUTION.md:383-392` states `712 passed` at the 2026-08-18 measurement. `774` now. This is
  **not** a finding: that same paragraph says *"Re-run the battery for a current figure rather
  than trusting any list written here (`HD-41` ③)"*, so the text disclaims its own tally
  rather than asserting it.
- `README.md:35`'s *(41/41 green)* re-derives exactly. Note the runner exists **here** as well
  as in the caller, and `EXECUTION.md:353-355` anticipates precisely that name collision
  (*"A name here may also belong to an unrelated file in this repository"*) — the disclaimer is
  load-bearing and correct.
- `EXECUTION.md:344-347`'s parenthetical scopes the collection abort to *"a repository root
  that also carries the product"*, i.e. the caller. Checked here: `pytest --collect-only` from
  this repository's root collects `774 tests` and does not abort. The text is accurate because
  it scoped the claim; had it been unscoped it would have been wrong here.

### 3.8 The guard's described blind spots, verified against the parser

`E10` makes an unusually precise claim about what `layer_path_check` cannot see. Each half was
checked against `tooling/hooks/layer_path_check.py`:

| `E10` says | the code |
|---|---|
| a placeholder segment falls outside its path shape | `PATHLIKE` admits `[A-Za-z0-9_.\-/]` only — no angle brackets ✔ |
| markdown links carry no backtick token | `TOKEN = re.compile(r"`([^`\s]+)`")` ✔ |
| `++ b/…` mis-files the member's remaining added lines | added line `++ b/x` renders `+++ b/x` → `current = "x"` ✔ |
| any other `++ …` silences them | renders `+++ …` → `current = None`, later `+` lines dropped ✔ |
| the standing text it never re-scans stays unscanned | `check()` reads only `added_lines_by_path` ✔ (scanned here instead, §3.2a) |
| the bytes `E2` freezes are excepted while frozen | consistent with §3.2a's five ✔ |

The description is accurate in detail. `.harness/` exemption present (`RUNTIME_PREFIX`), which
is the run-time-marker clause.

### 3.9 The two claims the stub and `ORCHESTRATION.md` make about dispatch code

Both are factual assertions inside instruction text, so both were run (`E3`).

```
dispatch.py:545  CONSTRUCTION_ROLE_INSTRUCTION =
                 "migration/document-work-assurance-v3/v3-harness-review-contract.md"
test_dispatch.py:398,463,522  CHARTER_OUTSIDE / MEMBER — hand-written literals (E5)
cli.py:549-560   dispatch modes, mutually exclusive, required:
                 --subject (PRODUCT run) · --range (CONSTRUCTION round) · --read (E10 layer read)
```

The stub's *"hard-codes this path"* and *"pin it independently (`E5`)"* both hold: the test
imports `dispatch as D` but pins the path with its own literal, so the expectation is
independent of the thing it guards. `ORCHESTRATION.md:26-32`'s *"its three modes are
review-side by construction, and none of them dispatches an executor"* holds: three modes,
each handing a cold **reviewer or reader** its subject, none an executor. This read's own
dispatch is `READ_PROMPT` rendered verbatim (`dispatch.py:668-681`), which is consistent with
the member set having been derived here rather than handed over.

### 3.10 Code-pinned doc paths versus the doc-only tier exception

Scope: string literals matching `"[A-Za-z0-9_./-]+\.md"` in every `tooling/**/*.py` at the
subject commit, cross-referenced against `git ls-files` for tracked `.md` paths, plus
basename matches to catch paths composed segment-by-segment. Ceiling: a path assembled
without any `.md` literal at all would be invisible to this scan; `grep -rnE 'glob\(|rglob\(|
iterdir\('` over `tooling/rsclib` and `tooling/hooks` returns nothing, so no directory walk
hides one there.

Tracked repository doc paths pinned by shipped code or by tests:

| path | pinned by | in `EXECUTION.md`'s exception? |
|---|---|---|
| the ten member paths | `hooks/layer_path_check.py` `LAYER` | **yes** — named |
| `document-harness/README.md` | `test_readme_enumeration.py` | **yes** — named |
| `document-harness/templates/decision-log.md` | `rsclib/…/init_target.py:34,48` (**code**) + `test_init_command.py:39` | **no** |
| `document-harness/templates/rider-bank.md` | `rsclib/…/init_target.py:35,48` (**code**) + `test_init_command.py:40` | **no** |
| `contract/Document-Work-Assurance-Contract-v3.md` | `rsclib/document_harness/__init__.py:41` (**code**) + `test_candidate_checks.py:1721` | **no** |

The pins are hard, not incidental: `test_init_command.py:72` is
`hashlib.sha256(path.read_bytes())` applied to the two template sources at lines 152/155, so a
rename raises rather than silently passing. This is `L-1`.

## 4. Findings

### `L-1` (low) — the doc-only tier exception names two code-pinned doc paths; the repository has five

**Location.** `document-harness/EXECUTION.md:330-339` (blob `27f4fc82`), the *Doc-only change
set* bullet of *Regression-battery tiering*:

> Exception, and what it turns on is the **path**, not the prose: code and tests pin the
> *paths* of certain doc files — `document-harness/README.md` under
> `test_readme_enumeration.py`, and the member paths in the layer-path mirror,
> `tooling/hooks/layer_path_check.py` — so a change that adds, removes or renames one of those
> paths is tooling-load-bearing and the batch is tooling-touching …

**Ground truth it is behind.** `HD-45` ② (`HARNESS-DECISIONS.md:247-248`), the ruling this
sentence carries, states the criterion without limiting it to two instances: *"代码与测试钉住
的是那些 doc 文件的**路径**，故增删或改名这些路径算 tooling-touching"* — the paths that code
and tests pin. Three tracked doc paths now meet that criterion and are not in the text (§3.10):
`document-harness/templates/decision-log.md`, `document-harness/templates/rider-bank.md` and
`contract/Document-Work-Assurance-Contract-v3.md`. Two of the three are pinned by **shipped
code**, not only by tests. The decision log outranks instruction text on conflict by its own
header (*"细则与裁决冲突，细则错"*), so the rule already covers all five and the text is what
is behind.

**How it arose.** `HD-45` wrote the exception on 2026-08-18 with the two paths that existed
then. The `dtw init` round created `templates/decision-log.md`, `templates/rider-bank.md` and
`init_target.py` on 2026-08-19/20 and did not extend it; its FULL
(`v3-review-full-2026a14.md:74-75`) lists both templates as added paths without reaching the
tier sentence. The contract path was already outside the enumeration when `HD-45` was written.
No rider carries this — the tier riders `tier-file-vs-clause` / `tier-scope` /
`battery-travel` were redeemed and deleted by `HD-45`'s own commit, and none of the 39 current
rows names it.

**The downstream decision that goes wrong** (`R9`'s test, so this is *not* wording-level): a
batch that renames, moves or deletes one of the three unlisted paths reads itself as doc-only
— all three are markdown outside the schema, tooling and generated trees — runs batch-specific
checks only, and ships a red `test_init_command.py` (a `FileNotFoundError`, not an assertion)
or a red contract governance scan, undetected until the next tooling-touching batch. That is
the same under-run shape the bullet's own history records for batch B R1 and R3, where *"only
the executor's private knowledge caught it"*.

**Why not must-fix.** It does not act wrongly today, and it does not bite the round now
opening: `EXECUTOR-CHARTER`'s change surface includes `dispatch.py` / `cli.py` / tests, so that
batch is tooling-touching on the code alone and never reaches the doc-only branch.

**Minimum fix, and the reading question under it.** Two readings are available and the choice
is not this reader's (`R5`):

- *criterion* — the em-dash list illustrates a stated general rule, and the fix is to make the
  sentence self-evidently open. Exact bytes: replace `— \`document-harness/README.md\` under
  \`test_readme_enumeration.py\`, and the member paths in the layer-path mirror,
  \`tooling/hooks/layer_path_check.py\` — so a change that adds, removes or renames one of
  those paths` with `— today \`document-harness/README.md\` under
  \`test_readme_enumeration.py\`, the member paths in the layer-path mirror,
  \`tooling/hooks/layer_path_check.py\`, the two shipped instance templates under
  \`document-harness/templates/\` that \`init_target.py\` copies, and
  \`contract/Document-Work-Assurance-Contract-v3.md\` under
  \`rsclib/document_harness/__init__.py\` — so a change that adds, removes or renames **any doc
  path code or a test pins** `. Under this reading the fix states what `HD-45` ② already
  requires, changes no rule, and is therefore free-channel-eligible under `E10`.
- *closed enumeration* — the list is fixed like the battery's *nothing fewer*, and extending it
  is design that opens a round.

`HD-45` ②'s wording favours the first; the battery bullet three lines below it, and `HD-42`'s
*"a subject disappearing does not license editing this enumeration again"*, are the precedent
for the second. Which one governs is the user's, on the precedent of `HD-52`, where this
layer's previous read routed the same shape of question and the user answered it as a ruling.

### `O-1` (observation) — `dtw dispatch`'s CLI help calls it "the executor's cold entry"

`tooling/rsclib/document_harness/cli.py:547`:
`help="derive a review dispatch from an evidence commit (the executor's cold entry)"`.
`ORCHESTRATION.md:26-32` states that the three modes are review-side and **none dispatches an
executor**, which §3.9 confirms of the code. The help line is loose twice over: it names the
executor for what is a reviewer's or reader's cold entry, and it says *evidence commit* when
two of the three modes take a range and a read subject instead. The **member text is correct**
and the CLI string is what disagrees with it, so this is not a finding against the layer; it is
recorded because the round now opening is exactly about who hands an executor a charter and
will touch this file, making it the cheapest possible moment to correct. Outside the member
set, so outside this read's subject proper.

### `O-2` (observation) — `HD-52`'s carrier is still owed, and this round touches the file that owes it

`HD-52` (`§live`, 2026-08-22, *已裁未落实*) rules that START-card rendering by script applies
to **every** product run, form-independent, while the layer's only sentence on how a START card
is produced remains inside a bullet opening *"Under the enumerated form"* (`EXECUTION.md:240-247`).
That divergence is known, user-ruled, and carried both by `HD-52` and by rider
`startcard-form`; it is **not** a new finding. It is recorded here because `HD-52` says the
carrier requires *"一个轮次把那句话移出编号态范围、或补一句盖住散文态"*, and `EXECUTOR-CHARTER`
is a round that already opens `EXECUTION.md` — an `R10` touch condition the orchestrator may
want to weigh at preview rather than at closeout. Widening the sentence is design by `HD-52`'s
own terms, so it needs the round's authorization, not the free channel.

### `O-3` (observation) — a wording-level finding that supplies bytes has two channels

`R10` routes findings in an ordered list: *"`E10`'s must-fix channel takes must-fix, R9 takes
wording-level, the `E10` free channel takes … any finding whose record supplies the exact bytes
… and the bank takes what is left."* A finding that is both wording-level **and** supplies
exact bytes matches two entries. `R9` says such a finding *"rides the next batch touching this
layer"*; the free channel says *"applied immediately … reported after the fact and reversible"*.
The outcomes agree (neither opens a round) and the list's order resolves the timing if it is
read as ordered — which the sentence's construction supports. Recorded as a tension a reader
may not resolve the same way, not as a defect; no actor is currently acting on it.

### `O-4` (observation) — the frozen-path rider's set is unchanged and still exactly five

§3.2a re-measured the five unresolved backtick tokens inside the two `E2`-frozen supersessions
and found them identical in number and location to what rider `frozen-path-prefix` records.
The rider's *redeem when* is *"`E2` 对两份 supersession 的 recorded ruling，或下一批碰这两个
文件的路径 token，孰先；**无 deadline**"*, and neither condition has arrived. Recorded as a
positive re-derivation confirming the row's scope, so a future read need not re-open the
question of whether the set drifted.

## 5. Coverage — what was read in full, what was sampled, what was only probed (`R4`)

- **Read in full at the subject blobs:** all ten members, 1 423 lines. Blob ids in §2. No
  member was covered by citation, although all ten were eligible.
- **Read in full outside the member set:** `HARNESS-DECISIONS.md` lines 1–151 (header +
  `§live`, eight entries) and `HD-45` at 239–261; `HARNESS-RIDERS.md` header and the 39 rider
  ids, with rows `frozen-path-prefix`, `startcard-form`, `one-session-roles`, `mark-case` read
  in full; `tooling/hooks/layer_path_check.py`; the root `README.md` §*Where the bytes came
  from*; the four `EXECUTOR-CHARTER-BRIEF` commit bodies.
- **Sampled:** `tooling/rsclib/document_harness/dispatch.py` (the two role-instruction
  constants, `READ_PROMPT`, `render_read_dispatch`); `cli.py` (subcommand registrations only);
  `init_target.py` (`TEMPLATES`, `TEMPLATE_DIR`); `__init__.py` (`CONTRACT_PATH`);
  `test_dispatch.py`, `test_precommit_checks.py`, `test_init_command.py`,
  `test_readme_enumeration.py` (the constants and assertions §3.3/§3.9/§3.10 name);
  `v3-cold-read-39e395e.md` (§2 blob table and the findings headings);
  `v3-review-full-2026a14.md` (changed-path table and coverage section).
- **Probed only:** `HARNESS-DECISIONS.md` `§implemented` and `HARNESS-DECISIONS-archive.md` —
  grepped for the thirteen ids the members cite (§3.5), never read end to end;
  `plans/executor-charter.plan.md` — not read, deliberately: the brief's conclusions are the
  work side's and `R2` says the read re-derives rather than inherits.
- **Not established:** whether the caller repository's five battery legs are green — their
  scripts are not in this repository and `EXECUTION.md:348-355` says they are not owed here.
  `UNVERIFIABLE` from this side, and stated rather than folded into the green result above.
- **Process claims are marked, not verified** (`R4`): that this read ran in a fresh context is
  a declared identity, not something the repository can lock.
