# Cold read — the instruction layer at `ff4b749` (batch `CORE-SET`, round 1 opening)

**No verdict.** A read is not a round (`R3`): it spends no budget, carries no verdict, and its
output is findings tiered must-fix / low / observation. Nothing below certifies any text, and
nothing below is banked as any round's FULL.

**Findings: 0 must-fix, 1 low, 3 observations.** The low is a redemption that closed one
instance of a three-instance class and deleted the row that named it, so the bank no longer
carries the remaining two (`L-1`, bytes supplied). The observations are the dispatch's own
shape: one entry of the hand-scoped coverage claim is wrong in the safe direction (`O-1`), the
hand-scoping re-introduced the member enumeration the generator deliberately withholds (`O-2`),
and one file-scope convention sentence sits inside a sub-bullet (`O-3`).

**The orchestrator's scope claim, checked rather than accepted (`R2`).** Its changed/unchanged
split against `21dad76` is correct — verified per member by `git rev-parse` at both commits
(§2), not read off the claim. Its *coverage* conclusion is not: `E10`'s test is a blob unchanged
since **a** recorded end-to-end read of it, not since that one record. `ORCHESTRATION.md` is
covered by `v3-checkpoint-read-153302a.md`, which read all nine end to end and records
`ae641325…` — the subject blob. **Seven of nine were citable, not six**; two were genuinely
owed, which is what `CONSTRUCTION-LEDGER.md:67` itself says. Both cited records were checked to
be end-to-end reads stating each member's blob id, as `E10` makes citation depend on: both do,
both are committed, both are byte-unchanged in the worktree (§2). The read was widened to
`ORCHESTRATION.md` anyway — over-reading is the safe direction and the file is 119 lines.

**What this read discharges.** The member-edit debt round `RIDER-SETTLEMENT` disclosed when it
waived its opening cold read — `document-harness/EXECUTION.md` and `document-harness/README.md`,
named at `CONSTRUCTION-LEDGER.md:67` as 「成员编辑欠独立 read 随下轮开轮（豁免冷读的代价）」. Both
were read end to end at full-member cost, and so was `ORCHESTRATION.md` beside them.

**Standing instructions read.** `migration/document-work-assurance-v3/v3-harness-review-contract.md`
(the stub, member 7) → `document-harness/CONSTRUCTION-CHECKLIST.md` in full, both sides, per the
stub's *"It is your standing instruction and its own counterpart; read all of it."*
`HARNESS-DECISIONS.md` lines 1–162: the header (1–27, its own state machine) plus `§live`
(28–162, **eight** entries — `HD-56`, `HD-44`, `HD-41`, `HD-36`, `HD-35`, `HD-34`, `HD-23`,
`HD-9`), which `E10`'s tail owes at a round's opening. Unchanged in membership against the
previous read's eight. `§implemented` and `HARNESS-DECISIONS-archive.md` were **not** read end to
end — probed by id only. Cited by section, never by blob.

---

## 1. What the subject is, and how it was derived

The dispatch supplied one commit plus a hand-written scope claim. Everything below was
re-derived from the repository (`R2`); the claim is treated in §4 as a subject, not as input.

```
$ git rev-parse HEAD
ff4b74985fe581a41500c9fb2c282a55781e7045

$ git status --porcelain
?? .goals/

$ git log -1 --format='%H%n%ad%n%s' ff4b749
ff4b74985fe581a41500c9fb2c282a55781e7045
Tue Aug 25 2026
V3-CORE-SET-RULINGS-v1
```

HEAD is the subject commit. The one worktree entry is untracked and outside every member path,
so the tracked worktree bytes are the subject bytes — verified per member with `git hash-object`
against `git rev-parse ff4b749:<path>`, 9/9 MATCH (§2), rather than inferred.

**The subject commit touches no member.**

```
$ git show --stat --format='' ff4b749
 CONSTRUCTION-LEDGER.md                  |   7 +-
 document-harness/plans/core-set.plan.md | 186 ++++++++++++++++++++++++--------
 2 files changed, 148 insertions(+), 45 deletions(-)
```

Its body says so in as many words — *"No round opens here, no instruction-layer member is
touched, and E10-sync does not fall due"* — and names the next action as *"round 1's opening
cold read and the E11 card"*. This is that read: a cold read of standing layer text at a round's
opening, not a read of a diff. The plan `document-harness/plans/core-set.plan.md` is not a member
and was deliberately not relied on for any finding; it was probed once, for the round's declared
role form (`:170-171`, `:403` — `HD-55`, three sessions, cold dispatch via `dtw dispatch`), which
is what keeps banked rider `e1-reader` from biting on this very dispatch.

**The freeze window is intact, re-derived rather than assumed.** The gitignored marker
`.harness/review-pending.json` names subject `ff4b74985fe581a41500c9fb2c282a55781e7045`,
dispatched `2026-08-25T14:32:35+00:00`. The branch tip is the subject, so no commit has landed
since dispatch (`E9`).

## 2. The member set, each member's blob, and the coverage arithmetic

The set is `E10`'s own sentence — **"exactly these nine paths and nothing else"** — hand-
transcribed from the checklist at the subject blob, then machine-compared against the guard's
mirror and the test's hand-written mirror. All three agree; the prose leg has no guard, which is
banked as rider `E10-sync`.

```
$ git rev-parse ff4b749:<path>   /   git rev-parse 21dad76:<path>

 #  blob @ ff4b749                              lines  bytes  path                                           vs 21dad76
 1  c0e3e2dd8960a00f0074d98b9ff79b85dcfb933b     249  19869  document-harness/CONSTRUCTION-CHECKLIST.md     same
 2  7e2798351335d3a722789bac06c5b5e9d6b1aa43      38  10863  document-harness/README.md                     CHANGED (was 0454c8a5)
 3  9c61051dd1b88fef683bda072f7abbda4988ace0     522  36893  document-harness/EXECUTION.md                  CHANGED (was b187af5c)
 4  86e5ed7ad6792a7548ce968dea3cbcfcc3ee9f3e     319  20627  document-harness/REVIEW.md                     same
 5  ae641325c2f880347f187e9003cc494077de9c1e     119   8377  document-harness/ORCHESTRATION.md              CHANGED (was 9a67401f)
 6  6d5714923870b4e13e8928221a80df68e563a5ed       5    511  migration/…/v3-harness-operating-contract.md   same
 7  29bdc9fbde6e8db38d601dd2340d4b46a24a296f       5    924  migration/…/v3-harness-review-contract.md      same
 8  dfc983d2e3d9fb5ca67b053a16fcfb0e6715b11a     342  22185  contract/Document-Work-Assurance-Contract-v4.md same
 9  09aa869962f592c2f86c9379be0ef3eb7d2232ff      44   2812  schema/…/paragraph-map.schema.json             same
```

The three-site cross-check, all nine paths identical in all three:

```
tooling/hooks/layer_path_check.py:37-47                          LAYER    (9 entries)
tooling/tests/document_harness/test_precommit_checks.py:229-239  EXPECTED (9 entries)
document-harness/CONSTRUCTION-CHECKLIST.md E10 prose             (9 paths, hand-transcribed here)
```

**Which members are citable, derived rather than accepted.** `E10`: *"a member whose blob is
unchanged since a recorded end-to-end read of it is covered by citing that record — a read's
record states the blob id of each member it read, because citation depends on it."* Two records
qualify, and both were checked against that sentence rather than assumed:

| record | landed at | blob ids stated? | end to end? | committed + unchanged |
|---|---|---|---|---|
| `v3-cold-read-21dad76.md` | `c48c070` | yes, §2 table, all nine | yes — *"All nine were read end to end anyway"* | `79a21112…`, worktree MATCH |
| `v3-checkpoint-read-153302a.md` | `001816f` | yes, §2 table, all nine | yes — §5 *"Read in full, end to end: all nine members at their subject blobs, 1640 lines"* | `d4f4259d…`, worktree MATCH |

The later record is the operative one: it read every member at the blob it still carries today,
except the two that moved afterwards. So the citable set is **seven** — members 1, 4, 5, 6, 7, 8,
9 — and the owed set is **two**, members 2 and 3. That matches what the ledger says the
`RIDER-SETTLEMENT` waiver cost, and does not match the dispatch's three (`O-1`).

**Where the three changes came from.** `git log 21dad76..ff4b749 -- <the nine>` returns exactly
three commits out of the range's twenty-eight:

- `153302a` `V3-STRANGER-PROOF-M1-AMENDMENT-v1` — member 5 only, one line: the three-roles
  table's reviewer carrier. This is the `E10` must-fix amendment answering
  `v3-cold-read-21dad76.md`'s `M-1`, and its paired independent re-read is
  `v3-checkpoint-read-153302a.md` — the record that now covers this member.
- `fd525e4` `V3-RIDER-SETTLEMENT-v1` — members 2 and 3, one clause each.
- `5873840` `V3-RIDER-SETTLEMENT-FIX-v1` — member 2 only, that round's one user-approved fix.

## 3. The read

### 3.1 `ORCHESTRATION.md` (member 5) — the `M-1` amendment as standing text

Read end to end at `ae641325…`. The amended cell now reads *"a full session, in the form `E1`
requires — what decides independence is who set the question (`R1`)"*, replacing a carrier column
that still offered the subagent form `E1` had stopped allowing. Checked against `E1` at the
subject blob rather than against the amendment's claim: `E1` does say *"runs as its own session
(`claude -p` or a separately launched session), never as an in-process subagent"*, so the table
now points at the rule instead of contradicting it, which is the file's own stated contract
(*"Where a line below cites a rule, that rule is the text"*).

Three things the file's arithmetic asserts were checked and hold: nine cite-only obligations plus
three own-text obligations is twelve, which is what `README.md:24` independently says
(*"nine of its twelve obligations"*); the *may never do* section adds two pointers and claims no
obligation of its own. `E1`'s disclosure obligation still has no row in the obligations table —
already banked as rider `e1-table`, not re-filed. Three cite-only rows still compress the cited
rule's own qualifier — already banked as `charter-qualifiers`, not re-filed.

### 3.2 `EXECUTION.md` (member 3) — the `py-convention` redemption

Read end to end at `9c61051d…`. The added sentence at `:368-371` declares a file-scope reading of
`python` and attributes it: *"measured 2026-08-23, round `PUB-FACADE`"*. The attribution was
checked rather than taken — `document-harness/journal/pub-facade-2026-08-23.md:76-77` holds the
command and its output:

```
$ wsl -d Ubuntu -e bash -lc 'command -v python; echo "python3: $(command -v python3)"; …'
python3: /usr/bin/python3
```

`command -v python` returned nothing and `python3` resolved, so *"stock Ubuntu ships only
`python3`"* is measured, not asserted. The rider named two site classes — the member and the four
caller-facing invocations in `assurance/templates/run-v2/README.md` — and both received the
convention; the second is outside this layer and outside this read's subject, noted only because
the rider's class spanned it. Inside the member the class is two `python` tokens
(`:365` the command, `:514` prose about argv), and the file-scope sentence covers the one that is
typed. Placement is `O-3`.

### 3.3 `README.md` (member 2) — the `move-cost-member-site` and `onboarding-labels` redemptions

Read end to end at `7e279835…`. Two clauses changed in the onboarding row, across two commits.

The **move-cost** clause is sound. `fd525e4` wrote the singular form (*"an empty decision log …
reported as `created`"*); the round's own FULL caught it and `5873840` corrected it to *"recreates
**both** instance files there as empty templates (exit 0, reported as `2 created`)"*. That is
supported by `ONBOARDING.md:106` — *"both files recreated at the root by one `init` run"* — and
the corrected clause is the stronger, not the weaker, reading. No finding.

The **labels** clause is not. It is `L-1`.

### 3.4 Probes on the seven citable members

`REVIEW.md:88-95` was probed for one reason: `ff4b749`'s body rules that round 1 will delete
`document-harness/history/` and *"REVIEW.md:92's link is left dangling by explicit ruling"*. At
this subject the target still exists (`git ls-tree -r ff4b749 -- document-harness/history/` returns
`document-harness/history/REVIEW-v1-package-flow.md`), so the member is intact now and the
dangling link is a ruled future state, not a defect at this commit. Recorded so the next read does
not mistake an authorised deletion for decay.

Mechanically, across all nine members' **standing** text — the stock `E10` says
`layer_path_check` never re-scans, because it reads only the lines a commit adds:

```
$ python -c "<apply layer_path_check.unresolved_tokens to each member's full text>"
document-harness/CONSTRUCTION-CHECKLIST.md: 0 unresolved
document-harness/README.md: 0 unresolved
document-harness/EXECUTION.md: 0 unresolved
document-harness/REVIEW.md: 0 unresolved
document-harness/ORCHESTRATION.md: 0 unresolved
migration/…/v3-harness-operating-contract.md: 0 unresolved
migration/…/v3-harness-review-contract.md: 0 unresolved
contract/Document-Work-Assurance-Contract-v4.md: 0 unresolved
schema/…/paragraph-map.schema.json: 0 unresolved
```

And for the second blind spot the same clause names — markdown links, which carry no backtick
token for the guard to find — every relative link target in all nine members resolves: 0 dangling
across the layer. This is a byte-level scan, not a reading; it is reported as such under `R4`.

## 4. Findings

### `L-1` (low) — `onboarding-labels` was redeemed against the reported instance, and the row that named the class was deleted with it

**Location.** `document-harness/README.md:28`, the onboarding row's opening parenthesis.

**Ground truth.** `document-harness/ONBOARDING.md:66-142` — *"## The nine items"*, nine numbered
headings: 1 mount · 2 `.harness/` and its ignore entry · 3 the decision log · 4 the rider bank ·
5 the journal · 6 the ledger · 7 the policy file · 8 the pointer line · 9 hook wiring.

**What the member says.**

```
(nine items: mount, the `.harness/` ignore entry, instance files, policy file, pointer line, hook wiring)
```

Mapping the labels onto the nine: mount→1, `.harness/` ignore entry→2, instance files→3+4 (the
two `dtw init` copies), policy file→7, pointer line→8, hook wiring→9. **Seven of nine.** Items 5
(the journal) and 6 (the ledger) have no label. Item 6 is not a no-op — `ONBOARDING.md:122` says
*"Write one … and declare its parameters … in the policy file of item 7"*, a caller action with
no representative in the list.

**Why this is a class, not an instance.** The retired rider read, at `fd525e4^`:

> `onboarding-labels` | 指令层 README `:30` ONBOARDING 表行的五个标签只盖住九条中的**八条**：条目 2
> （`.harness/` + gitignore 条目）无标签对应。纯导航行，不改任何规则

That premise is false as measured: the five labels covered **six** of nine (1, 3, 4, 7, 8, 9), and
three items lacked one — 2, 5 and 6. The redemption applied the rider's named byte, closing item 2
only, and deleted the row in the same commit as `R10` requires. The other two instances are now
recorded nowhere.

**The downstream decision that goes wrong (`R9`).** Not the caller's — the row links
`ONBOARDING.md`, which is correct and complete, so nobody onboards wrongly and this is below
must-fix. The decision that goes wrong is the **bank's**: `R10` redemption presumes the row's
disappearance means its debt is gone, and the next batch touching this surface will see no row
and have no reason to look. The defect survives its own ledger entry. This is the shape the same
round's FULL raised as `B-1` against `retire-suite`'s redemption; it recurred in the same round
against a second rider, and was not caught.

**Class sweep inside the layer, per `HD-41` ④ / `E7`** — the fix must not repeat the defect it
reports:

```
$ <scan all nine members for /nine items|nine checkable|onboarding items/>
document-harness/README.md:28   — the only site inside the layer
```

`ONBOARDING.md:92,183,192,207` say *"nine items"* without enumerating labels, so they carry no
instance; and `ONBOARDING.md` is not a member. One site, one fix.

**Minimum fix — exact bytes.** In `document-harness/README.md:28`, replace

```
(nine items: mount, the `.harness/` ignore entry, instance files, policy file, pointer line, hook wiring)
```

with

```
(nine items: mount, the `.harness/` ignore entry, instance files, journal, ledger, policy file, pointer line, hook wiring)
```

Eight labels for nine items, one of them (*instance files*) plural by design and matching
`ONBOARDING.md`'s own grouping of items 3 and 4.

**Routing, stated but not decided here.** `R10`: below must-fix, record supplies exact bytes,
`document-harness/README.md` is not on a path `E2` freezes (`E2`'s list is contract v4 plus the
fifteen-file schema pack), and the bytes add no clause and change what no rule requires, so the
design test does not fire. That is `E10`'s free channel on its face. Whether to take it is the
orchestrator's call, not this reader's.

### `O-1` (observation) — the dispatch's coverage claim classified `ORCHESTRATION.md` as owed; `E10`'s test says otherwise

The claim's stated basis was *changed since `21dad76`*. `E10`'s basis is *unchanged since a
recorded end-to-end read of it*. `ORCHESTRATION.md` changed at `153302a` and has been at
`ae641325…` since; `v3-checkpoint-read-153302a.md` read it end to end at exactly that blob and
records it. Applying one record as the baseline rather than the most recent qualifying record can
only over-read, never under-read, so the error is in the safe direction and cost 119 lines.
Recorded because the arithmetic, not the outcome, is what the next round will reuse — and because
`CONSTRUCTION-LEDGER.md:67` already names the correct two, so it is the dispatch that drifted from
the ledger, not the ledger that is stale.

### `O-2` (observation) — the hand-scoping re-supplied the member enumeration the generator withholds by design

`dispatch.py:668-669`: *"The member set is NOT enumerated here: E10's own sentence owns it, and
the reader derives it there"*, and `:664-666` records why — a hand-written dispatch once handed a
reader a member table that was wrong (`v3-cold-read-451e8b0.md` `M-1`). The prompt this read
received reproduces `READ_PROMPT` verbatim and then appends a nine-path table. It is explicitly
flagged *"yours to verify, never to accept (`R2`)"*, it was verified, and it was correct as to
membership — so nothing was anchored wrongly here. The point is that the missing narrow `--read`
form is what forced hand-scoping at all, and hand-scoping brought the withheld table back with it.
That is a second cost of the same gap, beside the wall-clock one already recorded, and it belongs
with item ① of the `dispatch-economy` batch at `CONSTRUCTION-LEDGER.md:134` rather than in the
bank as a new row. No bytes supplied: the fix is a command-surface change, which `HD-47` routes to
the user per case.

### `O-3` (observation) — a file-scope convention sentence placed inside one battery leg's sub-bullet

`EXECUTION.md:368-371` declares its own scope — *"`python` in this file"* — so it is not false,
and `HD-41` ①'s declare-the-scope-first discipline is met. But it sits inside the *this repository,
the instrument* sub-bullet of *Regression-battery tiering*, three levels deep in one section, while
the convention it states governs the whole file. The parallel sentence in
`assurance/templates/run-v2/README.md` sits at the top of the invocation block it governs. Nothing
misfires today: the file's only other `python` token (`:514`) is prose about argv, not a command
to type. Noted for whichever batch next touches that section; no route requested.

## 5. Coverage — what was read in full, sampled, and only probed (`R4`)

**Read in full, end to end** — 928 lines of member text:

| blob | lines | path |
|---|---|---|
| `c0e3e2dd8960a00f0074d98b9ff79b85dcfb933b` | 249 | `document-harness/CONSTRUCTION-CHECKLIST.md` (both sides, as standing instruction) |
| `7e2798351335d3a722789bac06c5b5e9d6b1aa43` | 38 | `document-harness/README.md` |
| `9c61051dd1b88fef683bda072f7abbda4988ace0` | 522 | `document-harness/EXECUTION.md` |
| `ae641325c2f880347f187e9003cc494077de9c1e` | 119 | `document-harness/ORCHESTRATION.md` |

Also read end to end: `HARNESS-DECISIONS.md` lines 1–162 (header plus `§live`, eight entries);
`HARNESS-RIDERS.md` in full, all 16 rows; `document-harness/ONBOARDING.md` items 2–9
(`:86-145`) plus its item headings; the commit bodies of `ff4b749` and `89fd736` in full; the
aggregate member diff `21dad76..ff4b749` in full.

**Covered by citation, not read here** — five members, unchanged since
`v3-checkpoint-read-153302a.md` read them end to end at these same blobs:
`86e5ed7a…` `REVIEW.md` · `6d571492…` and `29bdc9fb…` the two stubs · `dfc983d2…` contract v4 ·
`09aa8699…` `paragraph-map.schema.json`. Their bytes were scanned mechanically for the two
`E10` blind spots (§3.4); a byte scan is not a reading and no finding about their content is
offered.

**Sampled:** `v3-cold-read-21dad76.md` — header, §1, §2 and the citation paragraph read in full;
its findings section and §3/§5 **not** read, deliberately, so this read's own checks were derived
rather than replayed. `v3-checkpoint-read-153302a.md` — header, §2 table and §5 coverage read in
full; the rest not read. `REVIEW.md:88-95`. `document-harness/plans/core-set.plan.md` — probed for
the round's role form only. `CONSTRUCTION-LEDGER.md` — the two lines that carry the disclosures
(`:67`, `:134`), not read end to end. `HARNESS-RIDERS.md` at `fd525e4^` — the four rows the round
retired that touch members.

**Probed only, for named claims and never read end to end:**
`tooling/rsclib/document_harness/dispatch.py` (the read family, `:659-729`),
`tooling/hooks/layer_path_check.py` (`:37-110`),
`tooling/tests/document_harness/test_precommit_checks.py` (`:220-245`),
`tooling/tests/document_harness/test_readme_enumeration.py` (in full — it pins schema stems only
and binds nothing in `L-1`'s clause), `document-harness/journal/pub-facade-2026-08-23.md`
(`:70-90`), `assurance/templates/run-v2/README.md` (its diff only). `§implemented` and
`HARNESS-DECISIONS-archive.md` were probed by id only.

**Marked, not verified (`R4`).** That this session ran with fresh context and as its own session
is a process claim this reader cannot verify from inside. The round's declared form is
`HD-55`/three sessions, recorded at `document-harness/plans/core-set.plan.md:170-171` and `:403`;
that declaration is what banked rider `e1-reader` relies on, since `E1`'s form clause names
*reviewer or executor* and omits the reader. Not re-filed — the row already carries it.

**Not done, and why.** No guard was mutation-tested (`E4`, `R8`). The subject commit changes no
code and adds no guard, and the three member edits are prose, so there is no new binding force to
prove. The full battery was not run: `E9`'s window is open and this read lands one record.
