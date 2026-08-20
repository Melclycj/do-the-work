# Cold read — the instruction layer at `28501fe`

**No verdict.** A read is not a round (`R3`): it spends no budget, carries no verdict, and its
output is findings tiered must-fix / low / observation. This is the read `E10` owes over the
instruction layer; nothing below certifies any text, and nothing below is banked as any round's
FULL.

**Findings: 0 must-fix, 2 low, 5 observations.** The subject commit's central factual claims
were re-derived by command and **hold**: the instrument's single battery leg returns
`712 passed` at the subject itself (§3.1), and none of the five caller-side scripts the new text
names exists in this repository (§3.2). Both lows are consequences of the 2026-08-17 split that
the split has not yet paid for, and they point in opposite directions: the layer's own path
guard would now **block correct text** (`L-1`, demonstrated red and green in a scratch clone),
and five of the layer's own cross-references now resolve nowhere in this repository (`L-2`).
Neither supplies bytes — both fixes are design — so both bank.

---

## 1. Subject, re-derived

```
$ git log -1 --format='%h %ad %s' --date=short 28501fecdb4eca7b0380c75d493eca35c4bae5c2
28501fe 2026-08-18 V3-BATTERY-REPO-SCOPE-v1
$ git rev-parse HEAD
28501fecdb4eca7b0380c75d493eca35c4bae5c2
$ git status --porcelain
                                              # clean
```

The subject is HEAD and the worktree is clean, so the worktree bytes **are** the subject bytes.
Proven per member rather than assumed — `git hash-object <member>` against
`git rev-parse 28501fec:<member>`, **MATCH × 9**.

The member set is enumerated from `E10`'s own sentence read **at the subject** (not from the
dispatch, not from memory) — nine paths, and the sentence's self-count "exactly these nine paths
and nothing else" reconciles with the enumeration.

| # | blob | lines | path | read |
|---|---|---|---|---|
| 1 | `3af69265` | 204 | `document-harness/CONSTRUCTION-CHECKLIST.md` | end to end — also this session's standing instruction |
| 2 | `73808732` | 38 | `document-harness/README.md` | end to end |
| 3 | `78ab56b8` | 462 | `document-harness/EXECUTION.md` | end to end — the member this round changed |
| 4 | `3350bfac` | 284 | `document-harness/REVIEW.md` | end to end |
| 5 | `17ff31bb` | 5 | `migration/…/v3-harness-operating-contract.md` (stub) | end to end |
| 6 | `b576a45e` | 5 | `migration/…/v3-harness-review-contract.md` (stub) | end to end — the dispatch entry point |
| 7 | `68031fa2` | 124 | `contract/…-v3-supersession-1.md` | end to end |
| 8 | `e1a2f26b` | 113 | `contract/…-v3-supersession-2.md` | end to end |
| 9 | `09aa8699` | 44 | `schema/document-assurance-v3/paragraph-map.schema.json` | end to end |

**1 279 lines, none by citation.** Six of the nine are byte-unchanged since the last recorded
end-to-end read (`v3-cold-read-50c2b31.md`): members 4–9. Three changed — `CONSTRUCTION-CHECKLIST`
`682c413a`→`3af69265`, `README` `54dfef83`→`73808732`, `EXECUTION` `3dade026`→`78ab56b8`. The
citation channel was available for the six and **was not used**; all nine were read in full.

Outside the layer but owed at the same opening (`E10`): `ResearchSystem/HARNESS-DECISIONS.md`
at blob `c464877f`, `§live` read in full (lines 28–134: `HD-44`, `HD-41`, `HD-36`, `HD-35`,
`HD-34`, `HD-23`, `HD-9`). Cited by section, never by blob, per that clause — the blob id here
is provenance for this record, not a binding.

## 2. What the round changed, re-classified by hand (`R2`)

```
$ git show --stat --format='' 28501fec
 ResearchSystem/HARNESS-DECISIONS.md          | 24 ++++++++++
 ResearchSystem/HARNESS-RIDERS.md             |  3 --
 ResearchSystem/document-harness/EXECUTION.md | 72 ++++++++++++++++++++--------
```

Three paths, all Markdown, none under the schema, tooling or generated trees. One is a layer
member (`EXECUTION.md`, content only — its path is unchanged), so by the doc-only rule **as this
very commit rewrites it** the change set is doc-only and the full battery is not owed. The rider
bank now carries 25 data rows, down from 28; `battery-travel`, `tier-file-vs-clause` and
`tier-scope` are gone from it, and `HD-45` is present at status `implemented` with its four
carriers all located in `EXECUTION.md`'s tiering section.

## 3. Claims re-derived by command

### 3.1 The battery figure holds at the subject, not merely at the base

`EXECUTION.md` pins its measurement to the round's base (`0d73a5f`). Re-run at the **subject**:

```
$ cd ResearchSystem/tooling && python -m pytest -q
712 passed in 93.44s (0:01:33)
```

The count matches the text's `712 passed in 93.67s` exactly; the wall-clock differs as wall-clock
does. Because the change set is doc-only (§2), nothing the figure measures moved between base and
subject, so `E3` is satisfied both as written and at the tip.

*Noted and deliberately not filed as a finding:* `HD-45`'s 判据 line records the same 2026-08-18
measurement as `712 passed / 92.87s` against the member's `93.67s`. The load-bearing half — the
count — agrees in both, and my own re-run returning a third wall-clock (`93.44s`) is the
demonstration that the seconds are not a reproducible quantity. Chasing it would burn attention
on the one part of the figure that carries nothing.

### 3.2 The five caller-side scripts are absent here, as the text says

```
$ git ls-tree -r --name-only 28501fec | grep -E "tests/run_tests.py|run_p4_tests.py|run_p5a_tests.py|schema/fixtures/validate_fixtures.py|tooling/rsc.py"
ResearchSystem/tooling/tests/document_harness/run_tests.py
ResearchSystem/tooling/tests/document_harness_review/run_tests.py
```

Neither hit is one of the five: both sit a directory deeper than
`ResearchSystem/tooling/tests/run_tests.py`. None of the five enumerated paths resolves here —
the new text's assertion stands.

### 3.3 The other assertions checked, all holding

| Claim, and where | Command | Result |
|---|---|---|
| `E2`'s three frozen blobs | `git ls-tree -r 28501fec -- ResearchSystem/contract/` | `b2dbdf75` · `68031fa2` · `e1a2f26b` — all three exact |
| `E2`'s "fifteen files" pack | `git ls-tree -r … schema/document-assurance-v3/` | exactly 15 |
| README's schema enumeration | the 15 stems against README's three rows | all 15 named; `test_readme_enumeration` green inside §3.1's run |
| README's "41/41 green" | `python …/N0/fixtures/validate_fixtures.py` | `41/41 cases behaved as declared; failures=0` |
| README: "this repository … installs no hook at all" | `ls .git/hooks` (non-sample) + `git config core.hooksPath` | empty; unset |
| README: caller "calls **two** of them, not three" | `grep` on the caller's `.githooks/pre-commit` | exactly `review_freeze_check.py` and `candidate_path_check.py` |
| README: "this repository, where they do resolve" | the nine member paths at the subject | all nine resolve |
| `E10` membership ↔ its two mirrors | `layer_path_check.LAYER` and `test_precommit_checks.EXPECTED` | all three identical, same order — rider `E10-sync`'s check-item passes this round |
| Every backticked `E<n>`/`R<n>` in the layer | resolved against the checklist's own definitions | all resolve (one namespace collision, `O-2`) |

**The E2 pack across the split.** The pack's 15 files at the subject differ in three blobs from
the caller's last pre-2026-08-04 pack revision (`common`, `local-check-spec`,
`document-work-spec.v2`). I read all three diffs: they are the SIMP-A1 both-modes deletion and a
`COMMAND_TIMEOUT_SECONDS` clarification, all dated after that anchor, and the first carries its
own ruling inside the bytes ("deleted 2026-08-05 under a recorded user ruling (SIMP-A1)"). **Not
a finding.** Ceiling stated: I did not audit each pack write for its ruling — that is caller-side
round history, outside this subject.

## 4. Findings

### `L-1` (low) — the layer's own path guard would now block the layer's own correct text

`layer_path_check.py` flags "a backtick token starting with `ResearchSystem/` that does not
resolve from the repo root". The subject commit deliberately writes four such tokens into
`EXECUTION.md` — the caller-side battery scripts — and says so in the same sentence ("the five
paths that follow are the caller's and **do not resolve here**"). The text is correct. The guard
disagrees with it. Reproduced end to end in a scratch clone with the member change staged:

```
$ python ResearchSystem/tooling/hooks/layer_path_check.py
pre-commit BLOCKED: newly added instruction text names a repository path that does not resolve:
  …/EXECUTION.md: `ResearchSystem/tooling/tests/run_tests.py` — does not resolve from the repo root
  …/EXECUTION.md: `ResearchSystem/tooling/tests/run_p4_tests.py` — does not resolve from the repo root
  …/EXECUTION.md: `ResearchSystem/tooling/tests/run_p5a_tests.py` — does not resolve from the repo root
  …/EXECUTION.md: `ResearchSystem/schema/fixtures/validate_fixtures.py` — does not resolve from the repo root
exit=1
```

Negative control, same clone, same staging, the four tokens' backticks removed: **exit=0**. So the
guard's entire binding force on this class is the backtick, and the one workaround available
silences it without changing whether anything resolves — the shape rider `decited-paths` already
records in the mirror direction.

The guard's premise, "a repository path written into instruction text must resolve", was true
while one tree held everything. Post-split the layer must legitimately name paths in the other
repository, and now does.

*Why not must-fix:* it does not bite today. README's own Local-enforcement row records that this
check "currently runs nowhere", and §3.3 confirms it — no hook here, and the caller calls only
the other two. *No bytes:* both candidate fixes (teach the guard a cross-repo form; or forbid the
text from naming caller paths) change what a rule requires, so `E10` opens a round for either.
**Deadline = the re-homing README calls open** — the moment the guard is wired into this
repository is the moment it blocks a correct commit. Redeem-when: the next round-eligible batch
touching `layer_path_check`'s rule or `EXECUTION.md`'s per-repository enumeration.

### `L-2` (low) — five of the layer's cross-references resolve nowhere in this repository

Same root cause, opposite direction: layer text pointing at material that stayed with the caller.
Three are Markdown links, two are backtick tokens; the backtick pair predates this round, the
links have been dead since the extraction commit (`345acdd`, the repo's first).

| site | target | note |
|---|---|---|
| `README.md`, *Authoritative documents* | `../../.goals/plans/document-work-assurance-harness-v3.plan.md` | the user-approved execution plan — the table's authority row |
| `README.md`, *Predecessors* | `../../.goals/plans/general-harness-v2-architecture-revision.plan.md` | |
| `REVIEW.md` `:45` | `../migration/…/v3-review-full-fef3a2e.md` | the witness for *What is not in the subject* |
| `EXECUTION.md` ×2 | `ResearchSystem/assurance/runs/p5a-shells/control/audit-rounds.md` | the pre-freeze gate's two witnessed costs |
| `EXECUTION.md` | `ResearchSystem/assurance/runs/p4-doc/issues/user-decision-triage-comparator-environment-defects.json` | |

All five exist in the caller repository; none is reachable from here, in either mount context —
the harness is mounted at `ResearchSystem/harness/`, so `../../` from a `document-harness/` file
lands inside the harness repo, not above it. **No bytes:** a relative path out of a submodule
depends on where it is mounted, which is exactly the unsolved problem riders `submod-index` and
`decited-paths` already carry; choosing the substitute form (name-not-path, an explicit
"in the caller repository" annotation, or de-linking) is design. Redeem-when: the batch that
redeems `decited-paths` / `submod-index`, or the next batch touching README's
*Authoritative documents* table. **Deadline: already arrived** — unlike `L-1` these are dead now,
and the `REVIEW.md` one is the sole citation behind a rule a reviewer is asked to apply.

*`R5` half, for the user and not for me:* whether the layer should point at caller-owned
authorities at all now that they are two repositories is a question about what should exist, not
about what is there.

### Observations

- **`O-1` — what carries the coverage the new rule gives up is not stated.** The per-repository
  split means a tooling-touching construction batch **here** owes one leg where it used to owe
  six. The text names the loss ("the incidental coverage a construction round in one repository
  used to take from the other's legs"), which is the honest half. What no text says is that the
  loss is mostly repaired by construction: a caller-side gitlink bump changes a path that is not
  prose/markdown, so it is not doc-only, so the caller's five legs run at every bump. That
  reasoning is load-bearing for the new rule's adequacy and currently lives nowhere.
- **`O-2` — `R<n>` means three different things inside the layer.** Review rules (`R1`–`R10`),
  construction batch rounds (`EXECUTION.md`'s stage markers, README's "since `HD-14` (R1)"), and
  instruction sections under the enumerated form (`R0…Rn`). The convention that separates them is
  backticks-for-rules, and `EXECUTION.md` breaks it once by backticking **`R0`** in the
  instruction-section sense. Local context disambiguates every instance I read.
- **`O-3` — README's "What else lives in `ResearchSystem/contract/`" row is now vacuous here.**
  That directory holds exactly three files at the subject, and they are precisely the three the
  row's own last sentence names as the live v3 texts. The row directs a reader to a set that is
  empty in this repository.
- **`O-4` — the guard's class excludes the form the layer's navigation surface uses.**
  `layer_path_check` matches backtick tokens only, so Markdown link targets — what README's
  authority table is built from — were never in its class. Three of `L-2`'s five sites are
  invisible to it by construction, not by the unwiring.
- **`O-5` — a stale figure in the guarding test's docstring.** `test_readme_enumeration.py` says
  "all 14 delimited stems sit in the three enumeration rows today"; the pack holds 15. The test
  itself globs the directory, so its binding force is unaffected and it passes — only the prose
  count is stale. Outside the layer; noted because it is that member's guard.

## 5. Coverage and ceilings (`R4`)

- **Read in full:** all nine members (1 279 lines) and `HARNESS-DECISIONS.md` `§live`.
- **Read in full as corroboration:** `layer_path_check.py`, `test_readme_enumeration.py`,
  `test_precommit_checks.py`'s membership block, `HARNESS-RIDERS.md`, the caller's
  `.githooks/pre-commit`.
- **Executed:** the instrument's pytest leg (712 tests), the N0 fixture runner, the layer path
  scan over full member text and over the round's added lines, and the `L-1` reproduction with
  its negative control in a throwaway clone. No command touched the subject worktree.
- **Sampled, not exhaustive:** the caller repository. I confirmed the five scripts and the three
  `L-2` targets exist there, and did **not** re-run the caller's five battery legs — those
  figures in `EXECUTION.md` are **`UNVERIFIED` by me**, not verified-and-agreed.
- **Not established:** that each write to the `E2` pack since 2026-08-04 carried its recorded
  ruling (§3.3). Reachable only through caller-side round history, outside this subject.
- **Process claims are marked, not verified** — that this read ran in a fresh context is a
  declared identity, not evidence.
- **Not mine to conclude (`R5`):** whether the layer should reference caller-owned authorities
  at all; whether `layer_path_check` should learn a cross-repo form or be retired.
