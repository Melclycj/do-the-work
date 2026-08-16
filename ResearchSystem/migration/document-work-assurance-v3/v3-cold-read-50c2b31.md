# Cold read — the instruction layer at `50c2b31`

**No verdict.** A read is not a round (`R3`): it spends no budget, carries no verdict, and its
output is findings tiered must-fix / low / observation. This is the read `E10` owes over the
instruction layer; nothing below certifies any text, and nothing below is banked as any round's
FULL.

**Findings: 0 must-fix, 3 low, 4 observations.** The subject commit's central claim — that the
`E10` sub-clause numbering "added no clause, removed none, and changed no requirement" — was
re-derived clause by clause from the pre-amendment bytes and **holds** (§3.1). The three lows
are all in the class the same round installed rules about: one stale enumeration in three layer
members, one refuted causal sentence inside the numbering amendment itself, and one sentence
that the `E13` insertion silently re-parented out of `E12`. Every low supplies exact bytes.

---

## 1. Subject, re-derived

```
$ git log -1 --format='%h %ad %s' --date=short 50c2b3194689efc210c3d1c63eea0791bfaec4d6
50c2b31 2026-08-15 V3-ASSERT-OWNER-AMEND-E10-NUMBER-v1
$ git rev-parse HEAD
50c2b3194689efc210c3d1c63eea0791bfaec4d6
$ git status --porcelain
                                              # clean
```

The subject is HEAD, and the worktree is clean, so the worktree bytes **are** the subject bytes.
That was proven per member rather than assumed:

```
$ git hash-object <member>   vs   git rev-parse 50c2b319:<member>
MATCH × 9                                     # all nine identical
```

The member set is enumerated from `E10`'s own sentence read **at the subject** (not from a
dispatch, not from memory) — nine paths, and the sentence's self-count "exactly these nine paths
and nothing else" reconciles with the enumeration.

| # | blob | lines | path | read |
|---|---|---|---|---|
| 1 | `682c413a` | 241 | `document-harness/CONSTRUCTION-CHECKLIST.md` | end to end — also this session's standing instruction |
| 2 | `54dfef83` | 38 | `document-harness/README.md` | end to end |
| 3 | `3dade026` | 436 | `document-harness/EXECUTION.md` | end to end |
| 4 | `3350bfac` | 284 | `document-harness/REVIEW.md` | end to end |
| 5 | `17ff31bb` | 5 | `migration/…/v3-harness-operating-contract.md` (stub) | end to end |
| 6 | `b576a45e` | 5 | `migration/…/v3-harness-review-contract.md` (stub) | end to end — the dispatch entry point |
| 7 | `68031fa2` | 124 | `contract/…-v3-supersession-1.md` | end to end |
| 8 | `e1a2f26b` | 113 | `contract/…-v3-supersession-2.md` | end to end |
| 9 | `09aa8699` | 44 | `schema/document-assurance-v3/paragraph-map.schema.json` | end to end |

**1 290 lines, none by citation.** Blob ids and line counts emitted by
`git rev-parse --short=8 50c2b319:<path>` / `git show 50c2b319:<path> | wc -l`.

Outside the layer but owed at the same opening (`E10.13`): `ResearchSystem/HARNESS-DECISIONS.md`
at blob `6081efd3`, `§live` read in full (lines 28–290: `HD-43`, `HD-42`, `HD-41`, `HD-40`,
`HD-39`, `HD-36`, `HD-35`, `HD-28`, `HD-33`, `HD-34`, `HD-27`, `HD-23`, `HD-10`, `HD-15`,
`HD-9`). Cited by section, never by blob, per that clause — the blob id above is provenance for
this record, not a binding.

## 2. Citation status and riding debts

Two members moved since the last recorded end-to-end read of the layer
(`v3-cold-read-ddd773a.md`); seven did not:

```
$ git rev-parse ddd773a:<member> vs 50c2b319:<member>
CHANGED  682c413a  CONSTRUCTION-CHECKLIST.md      # 15999875 -> 682c413a  (cf1e3ee, 50c2b31)
CHANGED  3dade026  EXECUTION.md                   # 62c55e4b -> 3dade026  (a8af54c, cf1e3ee)
SAME     × 7       the other seven members
```

**Nothing here was taken by citation.** All nine were read end to end at the subject, so this
read is independent of that record rather than resting on it. Three consequences, stated rather
than assumed:

- **The two amendment reads `E10.2` owes are discharged by this record**: `cf1e3ee`
  (`E3`/`E7`/`E13`) and `50c2b31` (`E10` numbering). Both commit bodies say so explicitly and
  both are correct that the debt existed.
- **Every per-member digest debt riding on this layer is discharged**, whatever its origin,
  because no member was cited. That covers `a8af54c`'s `HD-42` enumeration edit (which
  `HD-42` itself records as still owing a layer read), and `e4ffa2b` / `22264b5`'s free-channel
  byte applications — all three touched `EXECUTION.md`, read here at its current blob.
- **`cf1e3ee`'s round-opening cold read does not substitute for this one.** It was the
  executor's own read (fine — `E10.12`'s cold read is an executor obligation), and it covered
  `EXECUTION.md` at `9f80e728`, the blob *before* `cf1e3ee` changed it. The amendment's own
  bytes had had no read until this one.

## 3. What was re-executed

Everything ran against the worktree, proven byte-identical to the subject for all nine members
(§1) and clean overall, so no measurement below is affected by drift.

### 3.1 The subject commit's central claim — re-derived, and it holds

`50c2b31` converted `E10`'s amendment protocol from one semicolon chain into fifteen numbered
clauses, claiming "the numbering added no clause, removed none, and changed no requirement."
The pre-amendment `E10` bullet was extracted by its own bullet boundaries and split
mechanically:

```
$ python … split the cf1e3ee^ E10 amendment-protocol chain on ';'
MECHANICAL SEMICOLON-SPLIT: 14 segments
SENTENCE-ENDING FULL STOPS INSIDE THE CHAIN: count: 1
  >>> …which this text expands under and which outrank it on conflict. It is not a member: …
```

Mapping every old segment onto the new numbering, by reading both:

| old segment | new clause | |
|---|---|---|
| 1–4 | 1–4 | one-to-one, requirement identical |
| **5** | **5 + 6** | the one split: old segment 5 carried both the free channel and the `E2` carve-out, joined by "— **but** neither this channel nor the must-fix one…" |
| 6–14 | 7–15 | one-to-one, requirement identical |

14 old segments → 15 new clauses, the difference being that single split. **No requirement was
added, removed or changed**; the edits are sentence-splitting and connective repair — em-dash
→ full stop at clauses 4 and 9, colon → semicolon and `this channel` → `that channel` at
clause 6, em-dash → semicolon at clause 12. The claim holds. The *stated reason* for 14-vs-15 does not — see `L-2`.

### 3.2 `E2`'s frozen surface reconciles

```
$ git ls-tree -r --name-only 50c2b319 -- ResearchSystem/schema/document-assurance-v3/ | wc -l
15                                             # E2: "fifteen files"
$ git rev-parse 50c2b319:<the three contracts>
b2dbdf752d8c155e4c65b14b5f420b880b8184a1       # E2: contract b2dbdf75…
68031fa2ca31272e31da0d42a9a02189d28fcc21       # E2: supersession-1 68031fa2…
e1a2f26b1d8d323d11e900f8137dea222b6571c1       # E2: supersession-2 e1a2f26b…
```

### 3.3 The three membership mirrors are in sync (rider `E10-sync`'s standing check-item)

`E10`'s sentence, `tooling/hooks/layer_path_check.py`'s `LAYER`, and
`tooling/tests/document_harness/test_precommit_checks.py`'s `LayerMembership.EXPECTED` carry the
same nine paths in the same order; read all three. The two code copies are bound to each other
by `test_layer_equals_the_hand_written_membership`, whose expectation is a hand-written literal
(`E5`-conforming). The prose leg remains unguarded — rider `E10-sync` already owns that fact,
mutation-proven there; **not re-proven here** (`R4`).

```
$ python -m pytest -q tests/document_harness/test_readme_enumeration.py \
                      tests/document_harness/test_precommit_checks.py
43 passed in 12.51s
```

### 3.4 Counts and paths the layer asserts

```
$ python validate_fixtures.py                  # README:33 "(41/41 green)"
41/41 cases behaved as declared; failures=0

$ the six battery commands EXECUTION.md enumerates                # all targets exist
EXISTS tests/run_tests.py · run_p4_tests.py · run_p5a_tests.py
EXISTS ../schema/fixtures/validate_fixtures.py · rsc.py

$ git ls-tree -r --name-only 50c2b319 -- tests/harness tests/stage_control | wc -l
0 · 0     # EXECUTION.md: the two struck battery entries' trees are indeed gone
```

The `HD-42` narrative in `EXECUTION.md`'s tiering section — eight commands reduced to six
because `HD-39` deleted those two trees in the same commit — reconciles with the tree.

### 3.5 Scope of what was NOT run

No candidate exists; this is a read, not a pass. The full six-command battery was **not** run —
only the two suites that pin layer members plus the contract fixtures. No guard code changed, so
nothing was mutation-tested and no suite's binding force is re-certified here (`R4`, `R8`).

## 4. Coverage and honesty ceilings (`R4`)

- **Read in full:** all nine members (1 290 lines); `HARNESS-DECISIONS.md` `§live`;
  `HARNESS-RIDERS.md` (to avoid re-filing banked findings); `layer_path_check.py`;
  `test_readme_enumeration.py`; the `LayerMembership` block of `test_precommit_checks.py`.
- **Probed only:** prior read records and review records — reached by targeted grep and line
  ranges, not read whole. `v3-review-full-feacb86.md` §6 was read closely because it is the
  precedent that settles `L-1`'s tier.
- **Not verified, marked as such:** that this session is a fresh context, and that the executor's
  round-opening read happened as its commit body describes. Process claims have no evidence lock.
- **Deliberately not concluded:** whether the three lows should be applied now or banked. Rider
  `wl-route` already owns that dispute — `E10.5`'s free channel and `R9`'s banking rule give
  different answers for a byte-supplied wording-level finding — and its row says any tiebreak is
  design. I supply bytes and stop (`R5`).

## 5. Findings

### Must-fix

None.

### Low

**L-1 — three layer members still enumerate the execution side as "E1–E12" after `E13`
landed.** `cf1e3ee` added `E13`; the checklist now carries 23 rules —
`git show 50c2b319:…/CONSTRUCTION-CHECKLIST.md | grep -c -E '^- \*\*(E|R)[0-9]+\*\*'` → `23`,
being `E1`–`E13` + `R1`–`R10`. Three members still say twelve:

| site | current | bytes |
|---|---|---|
| `document-harness/README.md:27` | "— E1–E12 execution, R1–R10 review;" | `E1–E12` → `E1–E13` |
| `v3-harness-operating-contract.md:3` | "one file: E1–E12 execution, R1–R10 review" | `E1–E12` → `E1–E13` |
| `v3-harness-review-contract.md:3` | "one file: R1–R10 review, E1–E12 execution" | `E1–E12` → `E1–E13` |

This is a **recurrence at the identical three sites**, not a first offence. `v3-review-full-feacb86.md`
`L-1` reported the same sentence stale on the R-side (`R1–R9` after `R10` landed) and supplied
the same shape of fix; that record in turn cites `cf040af`, where the same three sites were
corrected `R1–R8` → `R1–R9` when `R9` entered at `377d591`. Its ruling — "precedent says this
propagation belongs to the amendment" — is the standing practice `cf1e3ee` did not follow.

Two rules the same round installed name this exact path in: `E3`'s new clause about "a sentence
**inherited** from an earlier document whose premise this round itself reversed — a reversal
re-derives every claim that rested on it before the round closes", and `E7`'s new
same-commit sweep. The sweeps `cf1e3ee`'s body records (`measure.last|re-run the command
immediately|stale figure` and `one section below|the exception and says so|only section`)
could not have found this class; a sweep on the rule-range string would have. Repo-wide sweep
(scope: all tracked files at `50c2b319`) finds these three live sites plus four plans and two
journals; the plans and journals are dated narrative, and the many review-record hits are
history, so neither is proposed for change.

**Tier rationale, following precedent:** all three sites direct the reader into the checklist,
which carries `E13`; the README oracle asserts nothing about that row; no check outcome, binding,
permission, obligation or verdict path changes. `feacb86` tiered the identical class Low and said
it must not burn a repair. Same call here.

**L-2 — the numbering sentence's stated reason for "fourteen" is refuted by the bytes it
describes.** `CONSTRUCTION-CHECKLIST.md:105-108` reads: "…a mechanical split on semicolons
returns fourteen because **two of these are separated by a full stop instead**."

The split does return fourteen (§3.1) — that half is right. The reason is wrong under both
readings of the phrase. Mechanically, the pre-amendment chain contains **exactly one**
sentence-ending full stop, and it sits *inside* what is now clause 13 ("…outrank it on conflict.
It is not a member: …"), where it separates no two clauses. The extra clause is the split of old
segment 5 into new clauses 5 and 6, whose separator in the old prose was an **em-dash plus
"but"**, not a full stop. So there is no pair of clauses separated by a full stop, and a reading
that wanted two such pairs would predict a split of thirteen, not fourteen.

**Exact bytes** — replace "because two of these are separated by a full stop instead" with:
`because clauses 5 and 6 were one segment, joined by an em-dash and *but* rather than a
semicolon`.

Why it is Low, not must-fix: the numbering itself, the clause count and every requirement are
correct (§3.1), so no actor's action changes; and the accurate fact is recoverable in one step
from the subject commit's own diff. The reason to fix it anyway is that this sentence is the
reconciliation a later reader would use to check the amendment's null-effect claim, and it is a
factual assertion inside instruction text — `E3`'s last clause, installed one commit earlier.

**L-3 — the `E13` insertion silently re-parented `E12`'s trailing sentence.**
`CONSTRUCTION-CHECKLIST.md:171-172` now reads as the tail of `E13` ("One fact, one owner"):

```
  they act on.
  Reproduce a reported finding to write the fix correctly, never to adjudicate
  the reviewer.
```

That sentence has belonged to `E12` since the checklist was created: at `820b287` it was `E12`'s
second sentence, immediately after "no per-acceptance argument."; at `cf1e3ee^` it was still
inside `E12`'s bullet, pushed to its tail by the range clause. `cf1e3ee` inserted the `E13`
bullet **between** `E12`'s body and this sentence, so a rule about fact-ownership now ends with
an unrelated instruction about reproducing findings, and `E12` has lost it. The commit body
describes `E13`'s content and never mentions the sentence, so the re-parenting reads as an
artefact of the insertion point rather than a decision.

**Exact bytes:** delete lines 171–172 from the end of `E13` and re-insert them, unchanged, after
line 157 ("…and what it drops is the round's last-written records."), restoring the
pre-`cf1e3ee` structure. Whether `E12` is the sentence's *right* home is a separate question I
do not decide (`R5`) — the minimal fix is restoration, not relocation.

### Observations

**O-1 — the layer's one bare count has no revision and no recompute command.**
`README.md:33` carries "(41/41 green)". `E3`, as amended one commit before the subject, now
requires that "a count carries the revision it was taken at, and a count that grows with the
tree says so and names the command that recomputes it, rather than being carried forward as a
standing fact." This count is carried forward as a standing fact. **It is currently true** — I
re-ran the runner and got `41/41 cases behaved as declared; failures=0` — so nothing here is
false today; the observation is that the round which installed the clause did not sweep its own
layer for instances. Sweep scope: the nine member blobs at `50c2b319`; this is the only hit.

**O-2 — `cf1e3ee`'s recorded read-coverage figure is off by one.** Its body states the
`EXECUTION.md` re-read covered "431 行". The blob it names (`9f80e728`, at `cf1e3ee^`) is **430**
lines by every method — `wc -l`, `grep -c ""` and `awk END{NR}` all return 430, and the file
ends with a newline, so no counting convention yields 431. Nothing depends on the figure and it
lives in a commit body rather than instruction text, but it is the same `E3` class the round is
about.

**O-3 — routing of all three lows falls inside an already-banked dispute; not re-filed.** Each
supplies exact bytes and each is wording-level, which is precisely the case rider `wl-route`
records as having two rules pointing one way (`E10.5`, `R10`) and one the other (`R9`). No new
rider is proposed for it; that row already names its redeem-when and deadline.

**O-4 — the R-side rules are not in numeric order in the file.** They appear `R1`, `R2`, `R3`,
`R9`, `R10`, `R4`…`R8` (lines 176, 180, 183, 192, 198, 227–240). The grouping is intelligible —
`R9` and `R10` are finding-routing rules and sit with `R3`'s verdict-and-tiering material — and
this is not proposed as a defect. Noted only because a reader scanning for `R4` after `R3`
lands on `R9`, and because nothing in the file says the ordering is deliberate.
