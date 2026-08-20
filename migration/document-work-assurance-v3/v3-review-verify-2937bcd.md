# Targeted VERIFY — round `XREPO-REFS`, subject `dd18226..2937bcd`

**Verdict: `REVIEWED_NO_BLOCKER`.** 0 blocker · 2 low · 4 observation.

Independent review session. Standing instruction:
`ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` — reached through the dispatch's
named stub `ResearchSystem/migration/document-work-assurance-v3/v3-harness-review-contract.md`,
which is superseded and points here; the checklist carries both sides (`E1`–`E12` execution,
`R1`–`R10` review) and is its own counterpart, so the whole file is the instruction and the
whole file was read. Verdict reasoning in §7.

## 0. Dispatch as received, and what I refused to take from it

The dispatch handed me one range and one sentence of role. It told me — correctly — that round,
budget, authorization, obligations and every number are mine to re-derive from the repository.
I did. No figure below is taken from a commit body, a journal, or the FULL record; where I
quote one it is to compare it against my own run.

The freeze marker confirms the subject and nothing else:

```
$ cat .harness/review-pending.json
{
 "subject": "dd1822655e3c84f06031b8fe255c369e9785ca0c..2937bcd1270f350e6fbfa2eb540ecf4206df847a",
 "dispatched_at": "2026-08-19T16:32:46+00:00"
}
```

## 1. Subject, re-derived

```
$ git rev-list --count dd18226..2937bcd
2

$ git log --oneline dd18226..2937bcd
2937bcd V3-XREPO-REFS-FIX-v1
55c36c9 V3-REVIEW-RECORD-XREPO-REFS-dd18226-v1

$ git diff --name-status dd18226 2937bcd
M	ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md
M	ResearchSystem/document-harness/ORCHESTRATION.md
M	ResearchSystem/document-harness/journal/xrepo-refs-2026-08-20.md
A	ResearchSystem/migration/document-work-assurance-v3/v3-review-full-dd18226.md

$ git diff --stat dd18226 2937bcd
 .../document-harness/CONSTRUCTION-CHECKLIST.md     |  15 +-
 ResearchSystem/document-harness/ORCHESTRATION.md   |   4 +-
 .../journal/xrepo-refs-2026-08-20.md               |  88 +++++
 .../v3-review-full-dd18226.md                      | 397 +++++++++++++++++++++
 4 files changed, 497 insertions(+), 7 deletions(-)

$ git status --porcelain
(no output)
```

**Classified by hand.** Two instruction-layer members modified (`CONSTRUCTION-CHECKLIST.md` —
`E10` only; `ORCHESTRATION.md` — one bullet in *What the orchestrator may never do*), one round
journal extended, one review record added. No tooling, no schema, no frozen path, no generated
path; no member added, removed or renamed. Doc-only tier, and it is the tier I derive
independently of the one the commit derives.

**What round this is, and what leg.** The range's first commit is the FULL's record
(`v3-review-full-dd18226.md`, verdict `CHANGES_REQUIRED`, 1 blocker / 2 low / 5 observation);
the second is titled `V3-XREPO-REFS-FIX-v1` and names itself a review fix answering that record.
So a valid independent FULL has occurred for round `XREPO-REFS` and this is the fix leg — which
under `E9` obliges exactly one targeted VERIFY, this one. Round identity and authorization from
the repository: `XREPO-REFS` is R2 of batch DTW-INDEPENDENCE, authorized by
`ResearchSystem/HARNESS-DECISIONS.md` `§live` `HD-50`. The decision log is not in the range diff
— the `HD-50` state flip stays reserved to closeout, correctly.

**The window held.** Commit order is FULL record, then fix; nothing else landed between them, and
nothing has landed since (`HEAD` is the subject tip, worktree clean). `E9`'s rule that from
dispatch to the record's commit the branch takes no commit but the record itself is satisfied on
both dispatches I can observe.

**Approved fix boundary, as the fix states it:** `B-1` by narrowing, `L-1`, `O-2`'s wording half,
`O-3`. I cannot see the approval; `R7` — I state the ceiling and review the diff against that
declared boundary.

## 2. `B-1` — the blocker, checked by re-running the experiment that made it

`B-1` held that the `E10` clause asserted `layer_path_check` **enforces** the caller-held-path
rule while the guard is blind to the class's central shape.

### 2.1 The text actually changed, and the assertion is gone

```
$ git diff dd18226 2937bcd -- ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md
@@ -144,5 +144,10 @@
-  resolve in this repository, and an artifact living only in a caller is given its name
-  and its holder instead, so that a reader following a path in this layer cannot land on
-  another repository's bytes or on nothing: `layer_path_check` enforces this on the lines
-  a commit adds, this clause binds the standing text that guard never re-scans, and the
-  bytes `E2` freezes are excepted while they are frozen.
+  resolve in this repository, a run-time marker this repository itself writes counting as
+  resolving whether or not it exists at rest, and an artifact living only in a caller is
+  given its name and its holder instead, so that a reader following a path in this layer
+  cannot land on another repository's bytes or on nothing. `layer_path_check` decides, on
+  the lines a commit adds, only tokens it can relate to this repository — written in its
+  path convention, or resolving somewhere inside it; a token that resolves nowhere at all
+  it skips as possibly illustrative, which is how another repository's path reads by
+  default (the caller's ExperimentLab papers directory was one, until this round named it
+  instead). That shape, and the standing text the guard never re-scans, are held by this
+  clause alone; the bytes `E2` freezes are excepted while they are frozen.
```

The word `enforces` and the sentence built on it are gone; the residue is assigned to the clause
("held by this clause alone"). The overclaim `B-1` named is not in the text any more.

### 2.2 The falsifying experiment, re-run by me against the repaired tip

Throwaway clone of `2937bcd`, real defect shape, not a crash (`R8`). One added line carrying
three caller-held tokens, none in this repository's `ResearchSystem/` form:

```
$ git add ResearchSystem/document-harness/EXECUTION.md          # staged added line:
+A caller-held example: `ExperimentLab/papers/` and `assurance/runs/p5a-shells/control/audit-rounds.md` and `.goals/plans/x.plan.md`.
$ python ResearchSystem/tooling/hooks/layer_path_check.py
exit=0   (no output)

POSITIVE CONTROL — the same run artifact, prefix restored, same staged file:
+Positive control: `ResearchSystem/assurance/runs/p5a-shells/control/audit-rounds.md`.
$ python ResearchSystem/tooling/hooks/layer_path_check.py
exit=1
pre-commit BLOCKED: newly added instruction text names a repository path that does not resolve:
  ResearchSystem/document-harness/EXECUTION.md: `ResearchSystem/assurance/runs/p5a-shells/control/audit-rounds.md` — does not resolve from the repo root
```

Identical to the FULL's run: three caller-held tokens pass, the prefixed one blocks. The repair
changed no behaviour, and it does not claim to have. **`B-1` is closed** — the layer no longer
promises cover the guard does not give. It is closed by narrowing the sentence, not by widening
the guard, and the clause now says so itself.

### 2.3 The two disclosed departures from the minimum fix, checked

- **The two decidable shapes are not enumerated.** Reason given: *missing-prefix* exists only
  while this repository carries the `ResearchSystem/` prefix that R3 is chartered to remove.
  Checkable half: the prefix is indeed what branch 2 keys on (`layer_path_check.py:60-66`), and
  R3's charter is `HD-50`'s third item. The reasoning is sound as far as it goes; where the
  substituted wording lands short of accuracy is `V-1`.
- **The witnessed instance is named in prose, not as a backtick token.** Correct under the
  clause's own rule — a token there would be the clause violating itself. I verified the
  repair diff staged alone passes the guard (the §2.2 clone, repair diff only, exit 0).

## 3. `L-1` — the runtime-marker exception, checked against the whole standing stock

The clause gained *"a run-time marker this repository itself writes counting as resolving whether
or not it exists at rest."*

**The marker is this repository's own.** `dtw dispatch` writes it — `rsclib/document_harness/cli.py:216`
constructs `repo_root / ".harness" / "review-pending.json"`, `hooks/review_freeze_check.py:25`
reads it, and `.gitignore:18` holds `.harness/` with the comment that the marker and the run log
are *"per-checkout, never committed."* So the exception describes a real property of this
repository, not a courtesy.

**Swept with my own instrument, not theirs.** `sweep_refs.py` is not in the repository (the FULL's
`O-4`, still unpaid — see `V-2`), so I wrote my own: markdown link targets plus backticked
`/`-bearing path-shaped tokens over the ten `E10` members, resolved against repo root, the file's
own directory, and under `ResearchSystem/`, with a target reachable only by escaping the repo root
counted as not resolving. Run in a **clean clone**, where `.harness/` does not exist — the true
at-rest state, and the reason the FULL's own sweep could not see these two sites:

```
$ python rsweep.py .            # at 2937bcd
PATHTOK ResearchSystem/document-harness/README.md:36    .harness/review-pending.json
PATHTOK ResearchSystem/document-harness/REVIEW.md:139   .harness/review-pending.json
PATHTOK …/Document-Work-Assurance-Contract-v3-supersession-2.md:60   assurance/runs/
PATHTOK …/Document-Work-Assurance-Contract-v3-supersession-2.md:99   templates/run-v2/
-- 4 unresolvable references over 10 members

$ python rsweep.py .            # same instrument at dd18226
(identical four lines)
-- 4 unresolvable references over 10 members
```

`LINK` is empty at both ends. Four `PATHTOK`s, all accounted for by the clause as repaired: two
runtime-marker sites (the new exception) and two `E2`-frozen sites (the standing exception). The
repair introduced no new unresolvable reference and removed none — consistent with a text-only
repair. **The sentence is true of the whole standing stock at rest**, which is what `L-1` asked
for and more than the round could have claimed before.

Both marker sites are genuine: `README.md:36` describes the review-freeze guard, `REVIEW.md:139`
tells a returning reviewer that the record commit deletes the marker.

**Corroboration the round did not claim.** A sibling guard already implements exactly this
exception in code: `rsclib/document_harness/paths.py:69` carries `UNTRACKABLE = (".git/", ".harness/")`
with the comment *"Trees git never tracks by design … the harness runtime state that `dtw dispatch`
writes"*, pinned by a hand-written `E5`-shaped test
(`tests/document_harness/test_precommit_checks.py:303-334`, including the negative control
`.harness/review-pending.json` and a must-fire case proving the exemption is prefix-bound). So
the new prose exception matches existing machinery rather than inventing a rule — `E6` held
without needing to be argued.

**The guard's own predicate over the same ten members** (the narrower instrument, which skips the
resolve-nowhere class by design and therefore cannot see the marker class at all):

```
$ python -c "<layer_path_check.unresolved_tokens over all ten members at 2937bcd>"
…supersession-1.md [('schema/document-assurance-v3/review.v2.schema.json', 'resolves only under ResearchSystem/ — prefix missing')]
…supersession-2.md [('schema/', 'resolves only under ResearchSystem/ — prefix missing')]
whole-stock scan complete -- members: 10
```

Two violations, both inside `E2`-frozen bytes, both excepted by the clause's last sentence.

## 4. `O-2`'s wording half and `O-3`, checked

**`O-2` wording half.** `ORCHESTRATION.md:89-90` now reads *"what a session holding both work-side
roles owes — is `E1`'s to state, and this file does not re-type it. Read `E1`."* The stale gloss
*"in its record"* is gone and nothing was copied back in — the correct direction for a cite-only
member. `E1` as amended names its carriers as *"the commit body or the round journal, the carriers
`E3` names"*, so the dropped gloss was indeed stale. Paid.

**`O-2`'s table half is not paid, and is reported as banking at closeout.** I checked the table
rather than the claim: `ORCHESTRATION.md:38-48` carries a header plus **nine** obligation rows
(`E10`, `E11`, `E12`, `E9`×2, `R6`, `R10`, `R5`, `HD-2`), and none of them is `E1`'s disclosure
duty. The gap is real and unbanked at the tip — `O-2` below.

**`O-3`, both pointers.** Reproduced:

```
$ grep -n "^## " ResearchSystem/document-harness/journal/xrepo-refs-2026-08-20.md
125:## 3. The whole standing stock against the guard's own criterion
143:## 4. The guard experiment — before, after, negative control

$ git log -1 --format=%b dd18226 | sed -n '16p'
(journal §3). R2: the four outbound references demote to names with their holder stated —

$ grep -n "733 passed" ResearchSystem/document-harness/journal/xrepo-refs-2026-08-20.md
229:  `733 passed in 100.67s`, unchanged in count from the two reads of the opening pair.
```

The candidate body's single `(journal §3)` does cite §3 for both the standing-stock scan and the
guard experiment, and §4 is the experiment. The two battery figures are two runs of the same leg;
my own run agrees on the count. Both corrections are accurate, and a commit body cannot be edited
(`E8`), so record-side prose is the only available carrier.

## 5. The rest of the repair diff, and the permanent boundaries

**The round's own figures, re-derived.** Every number the fix commit states that I could
reproduce, reproduced:

```
$ cd ResearchSystem/tooling && python -m pytest -q
733 passed in 103.44s (0:01:43)                     # commit says 733 in 101.21s — count agrees

$ python -c "<sha256 of E10's membership sentence, 'The instruction layer …paragraph-map.schema.json`.'>"
869 ab50782010cfa8e69cfecd10b30fe5e528bbfb4680e6ecbd2c15b493e1ccfe1b   # at 2937bcd
869 ab50782010cfa8e6…                                                   # at dd18226 — byte-identical
```

The reported `sha256 ab507820…, 869 chars` is exact, at both ends. Independently of the hash, the
diff's single hunk starts at `:144` while the membership sentence occupies `:94-105`, so
`E10-sync` does not fall due on structural grounds too. The battery run covers both membership
mirrors (`layer_path_check.LAYER` and the hand-written `EXPECTED` in
`tests/document_harness/test_precommit_checks.py:164-178`).

| Rule | Finding |
|---|---|
| `E2` frozen bytes | Held. `git ls-tree` at the tip returns `b2dbdf75…`, `68031fa2…`, `e1a2f26b…` for the three named blobs and fifteen files in the `document-assurance-v3` pack; none is in the diff. |
| `E3` measure-last | Held on every figure I could re-run (battery count, membership hash and length, the falsifying experiment, the standing-stock sweep, the guard's predicate scan). The one factual assertion the new text makes about the guard is where it still slips — `V-1`. |
| `E4` / `E5` new guards | No guard added or changed. Not owed. |
| `E6` no new machinery | Held. Text only, and the exception it adds already exists in a sibling guard's `UNTRACKABLE` tuple rather than being invented here. |
| `E7` defect class | Held for `L-1`: swept the whole standing stock with two instruments rather than fixing the two sites the FULL named. Partially short for `B-1` — `V-1`. |
| `E8` commit form | Held. `V3-XREPO-REFS-FIX-v1`, one dense paragraph, no trailers, kind named ("Review fix"), no amend visible, four explicit paths, inside the declared boundary. Not pushed — see `O-4` for the measurement, which is not the one the FULL used. |
| `E9` budget | Held. One FULL (record at `55c36c9`), one user-approved fix (`2937bcd`), this VERIFY. No commit inside either dispatch window but the record itself. |
| `E10` layer discipline | Held. The repair is design (it changes what the clause requires of a member's path tokens) and it rode the round's fix leg, which is the right channel; the membership sentence is byte-identical, so no `E10-sync` duty. The free channel was not used and not needed. |
| `E11` preview card | Caller-side, not visible to me. `UNVERIFIABLE`. |
| `E12` handoff | Held. One range, no per-acceptance argument. |
| `R6` record channel | Held. `55c36c9` touches exactly one file, title `V3-REVIEW-RECORD-XREPO-REFS-dd18226-v1`. That it landed unchanged is `UNVERIFIABLE` (`R4`) — I hold no independent copy. |
| `R10` rider routing | Held for this leg. `HARNESS-RIDERS.md` is untouched (31 data rows at both ends). No row's touch condition arrived: `E10-sync` keys on the membership sentence (untouched), `charter-qualifiers` and `charter-prose-overreach` key on `ORCHESTRATION.md`'s obligation table / §thin opening / *Handing the executor its instruction* (the edit is in *What the orchestrator may never do*), `chk-thin` keys on `REVIEW.md` (untouched here). Residuals: `O-2`, and `V-2`. |
| `HD-50` authorization | The round's substitution of its first enumerated item is now answered by a user ruling that exists in no file — `V-2`. |

## 6. Findings

### `V-1` (low) — the replacement sentence still describes the guard in terms measurement falsifies, in the same permissive direction as `B-1`, one shape smaller

**Location.** `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md`, `E10`, tip `:148-150`:

> `layer_path_check` decides, on the lines a commit adds, only tokens it can relate to this
> repository — **written in its path convention**, or resolving somewhere inside it; **a token
> that resolves nowhere at all it skips** as possibly illustrative …

**Ground truth, measured.** Two halves, two problems.

*(a) "written in its path convention" over-includes.* The guard's first branch is
`token.startswith("ResearchSystem/")` and nothing else (`layer_path_check.py:60-63`). This
repository's members also write root-relative tokens for its root-level trees —
`` `.harness/review-pending.json` `` at `README.md:36`, `` `.githooks/` `` in the same row — and
those the guard cannot relate at all. Paired probe on one added line, positive control included so
the guard is proven reached:

```
$ git add ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md   # staged added line:
+Paired probe: `.githooks/no-such-hook.md` (root convention, resolves nowhere) and `ResearchSystem/nope.md` (positive control).
$ python ResearchSystem/tooling/hooks/layer_path_check.py
exit=1
pre-commit BLOCKED: newly added instruction text names a repository path that does not resolve:
  ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md: `ResearchSystem/nope.md` — does not resolve from the repo root
```

`.githooks/no-such-hook.md` is an in-repository path written in a convention this layer uses, it
resolves nowhere, and the guard passes it silently in the same run in which it blocks the
prefixed control.

*(b) "a token that resolves nowhere at all it skips" is falsified by the round's own positive
control.* `` `ResearchSystem/assurance/runs/p5a-shells/control/audit-rounds.md` `` resolves nowhere
at all and is **blocked** (§2.2). Read as a standalone predicate the half is simply false; read as
the residue of the preceding "only", it is right. The sentence does not supply the word that
forces the second reading.

**Why low and not blocker, and not inflated.** The clause's closing sentence — *"That shape, and
the standing text the guard never re-scans, are held by this clause alone"* — means a reader who
misjudges the boundary still lands under a rule that forbids the write. No permission is granted
that the true state withholds, which is what made `B-1` a blocker. What is lost is the accuracy
`E3` demands of a factual assertion in instruction text, on the one sentence this round exists to
get right.

**Named downstream decision (`R9`).** An executor writing a new root-relative in-repository token
(`.githooks/…`, `.harness/…` — both live in the layer today) reads the first half as covering it
and skips the manual check the clause reserves to itself. That is the identical action-level error
`B-1` was paid for, on a smaller class.

**Minimum fix — exact bytes, no machinery, and neutral to R3's re-rooting.** In that sentence
replace

> — written in its path convention, or resolving somewhere inside it; a token that resolves
> nowhere at all it skips as possibly illustrative,

with

> — written with the single prefix it recognizes, or resolving somewhere inside it; a token it
> can relate neither way it skips as possibly illustrative,

That is exact against the code, still names no prefix (so re-rooting does not falsify it), and
adds no bound.

### `V-2` (low) — the ruling that moved `HD-50`'s first enumerated item out of this round exists in no file; the register still says the opposite

**Location.** `2937bcd`'s body: *"The guard-learns-the-class work and the tracking of
`sweep_refs.py` are ruled into R3's scope (user, 2026-08-20)."* Against
`ResearchSystem/HARNESS-DECISIONS.md` `§live` `HD-50`, which is untouched in the range and still
enumerates R2 as *"教 `layer_path_check` 认跨仓（rider `layer-crossrepo-token`）…"* and still
states *"**R2 必须先于 R3**：守卫先认跨仓，否则 R3 改 `EXECUTION.md` 按仓枚举句会被刚归位的守卫挡住."*

**Ground truth it violates.** `R2` — *chat-only load-bearing material is a finding*. The ruling is
load-bearing three ways: it is the answer to the FULL's `L-2`, whose `R5` half the FULL reserved to
the user; it is the sole ground on which the round's central design choice (text clause instead of
guard work) is legitimate rather than a silent substitution; and it binds a future round. The
decision log's own admission test (`§头` 准入三问, any one sufficient) admits it on two counts —
it binds R3 and later, and it narrows a live entry — and its third asks precisely whether the
ruling has a home besides conversation and a commit body. It does not.

This is distinct from the fix-boundary approval in the same body, which is a per-round
authorization I simply cannot see (`R7`: ceiling stated, moved on). `V-2` is about a ruling that
re-plans a registered batch.

**No bytes supplied, deliberately.** `HARNESS-DECISIONS.md` is not an `E10` member, its state is
flipped only by the user (`HD-2`), and writing the entry's content is not the reviewer's to do.
What must be recorded is: which of `HD-50`'s R2 items moved to R3, and what becomes of the
`R2-before-R3` ordering constraint once its stated reason is undelivered.

**Deadline (`R10`), if this banks:** this round's closeout — the commit that flips `HD-50`'s state
is the last moment at which the register and what actually happened can be reconciled without a
reader having to find a commit body — or R3's opening, whichever is first.

### `O-1` (observation) — the property `HD-50` named as R2's reason for going first is still undelivered, measured

Reported, not concluded (`R5`): whether the guard should still be taught is the user's question.
What is checkable today is that the guard's missing-prefix branch still blocks the exact token
shape R3 is chartered to write:

```
$ git add ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md   # staged added line:
+Post-re-rooting shape: `document-harness/EXECUTION.md` and `document-harness/REVIEW.md`.
$ python ResearchSystem/tooling/hooks/layer_path_check.py
exit=1
pre-commit BLOCKED: newly added instruction text names a repository path that does not resolve:
  …CONSTRUCTION-CHECKLIST.md: `document-harness/EXECUTION.md` — resolves only under ResearchSystem/ — prefix missing
  …CONSTRUCTION-CHECKLIST.md: `document-harness/REVIEW.md` — resolves only under ResearchSystem/ — prefix missing
```

Whether R3 dissolves this by moving the files in the same commit that rewrites the text is R3's
design question and not mine. `V-2` is the part that is not a design question: the record of the
decision.

### `O-2` (observation) — `O-2`'s table half is unbanked at the tip, and its only carriers are two commit bodies and the FULL record

Verified rather than taken on report: `ORCHESTRATION.md`'s obligation table has nine rows and none
is `E1`'s disclosure duty; `HARNESS-RIDERS.md` has no row for it — 31 rows, unchanged, and the two
that name `ORCHESTRATION.md` are `charter-qualifiers` (cite-only rows dropping a cited rule's
qualifiers) and `charter-prose-overreach` (argumentative prose exceeding its ground), neither of
which is about a missing row. The fix routes it to closeout with the same surface argument the candidate gave — that a table
row opens `charter-qualifiers`' surface — which is a routing claim about *where the fix rides*, not
a claim that `charter-qualifiers` carries the content. The FULL's objection was the latter and it
still stands until a row exists. Recorded so closeout does not lose it; no action proposed here.

### `O-3` (observation) — the clause's witnessed-instance parenthetical says the round "named it instead", and at the site the name is not what remains

`E10` now reads *"(the caller's ExperimentLab papers directory was one, until this round named it
instead)"*. At the site the round repaired, `EXECUTION.md:341` reads *"in the caller that grew this
harness, a papers tree holds two same-named `smoke_test.py`"* — holder given, name replaced by a
description; `grep -n ExperimentLab ResearchSystem/document-harness/EXECUTION.md` returns nothing.
The clause's own remedy is *"given its name and its holder instead"*, and every other site the round
demoted does exactly that — `v3-review-full-fef3a2e.md` at `REVIEW.md:45`, `audit-rounds.md` at
`EXECUTION.md:186` and `:449`, the five named caller commands at `:343-348`, and
`user-decision-triage-comparator-environment-defects.json` at `:452`. This one does not, and the
clause describes it as though it did. Nothing downstream turns on it — the clause
itself carries the name — so no action is proposed; it is recorded because the clause is now the
layer's precedent for how the remedy looks.

### `O-4` (observation) — `E8`'s no-push boundary holds, but not by the test the FULL used

The FULL recorded *"`HEAD -> main` with no remote-tracking ref: not pushed"*. There is a remote and
there is a remote-tracking ref:

```
$ git branch -a -v
* main                2937bcd [ahead 44] V3-XREPO-REFS-FIX-v1
  remotes/origin/HEAD -> origin/main
  remotes/origin/main f65dcf2 add this repository's own .gitignore: …
```

The conclusion is unchanged and in fact stronger — `main` is 44 commits ahead of `origin/main`, so
none of this round's commits is pushed — but a future round reusing "no remote-tracking ref" as the
test would be reading an absence that is not there. Recorded for the instrument, not against the
verdict.

## 7. Why `REVIEWED_NO_BLOCKER`

`B-1` is closed and closed by measurement, not by reading the commit body: the enforcement
assertion is gone from the text, and the experiment that falsified it re-runs identically against
the repaired tip, which is exactly what a text-only repair should produce. `L-1` is closed wider
than it was raised — the exception is grounded in code that already implements it, and my own
at-rest sweep in a clean clone shows the repaired sentence is true of all ten members, not only of
the two sites the FULL named. `O-2`'s wording half and both `O-3` pointers are paid and correct.
The repair stayed inside its declared boundary, touched no frozen byte, left the membership
sentence byte-identical, spent no budget it was not owed, and every figure it reports that can be
re-derived, re-derives.

Two lows remain and neither is inflated to reach a blocker: `V-1` is an accuracy residue on the
same sentence, in the same direction but without the permission consequence that made `B-1` a
blocker; `V-2` is a record gap whose natural home is closeout, days away. `R3`'s rule that a
VERIFY is never a re-certification applies: I re-derived the fix leg and the permanent boundaries,
not the round.

## 8. Disclosure — read in full, sampled, only probed (`R4`)

**Read in full:** `CONSTRUCTION-CHECKLIST.md` (both sides, end to end, at the tip);
`v3-review-full-dd18226.md` (397 lines); `layer_path_check.py` (106); both commit bodies in the
range in full; `HARNESS-DECISIONS.md` header + `§live` (`:1-195`); the complete diff of both
commits for every changed path; `v3-harness-review-contract.md` (the stub the dispatch named).

**Sampled:** `journal/xrepo-refs-2026-08-20.md` — §8 in full (the 88 added lines), section headings
and `:229` elsewhere, not §1-§7 end to end; `ORCHESTRATION.md` — `:18-96`, not the whole file;
`HARNESS-RIDERS.md` — the header and the eight rows matching `E10|CONSTRUCTION-CHECKLIST|ORCHESTRATION`
in full, the rest by row count only; `EXECUTION.md` — the three regions this round changed, via
`git diff 69fc082 2937bcd`, not end to end; `README.md` `:36`; `REVIEW.md` `:43-47` and `:137-141`;
`paths.py:50-88` and `test_precommit_checks.py:150-200,300-340`; `.gitignore` `:6-18`;
`cli.py:216` and `review_freeze_check.py:25` by grep hit.

**Only probed, not read:** the guard's behaviour (throwaway clone of `2937bcd`, four staged
experiments — three caller-held tokens, a prefixed positive control, a paired root-convention probe
with control, a post-re-rooting shape probe); the guard's predicate over the whole standing stock;
my own reference sweep at both ends of the range in a clean clone; the battery (733 passed); the
membership sentence's length and sha256 at both ends; rider row counts; frozen blob ids via
`git ls-tree`; git refs, remote-tracking state and worktree cleanliness.

**Instrument note.** My sweep and `layer_path_check` answer different questions and disagree by
design: mine asks *does this point at nothing*, so it passes `` `schema/…/review.v2.schema.json` ``
in supersession-1 (it resolves under `ResearchSystem/`); the guard asks *is this written in the
convention*, so it flags it. Both results are reported above, unreconciled on purpose.

**`UNVERIFIABLE`, not folded into supported.**
(a) That `55c36c9` committed the FULL record unchanged from what its reviewer wrote — I hold no
independent copy; one file per record commit is consistent with it and proves nothing.
(b) The fix commit's `E1` disclosure — *"the executor was a subagent this orchestrator dispatched,
holding none of `R1`'s four holdings"* — is a process claim about a session I cannot observe.
Marked, not verified. It is well-formed against `E1` as amended and does not call the result
structurally independent.
(c) The fix boundary approved 2026-08-20 and the `R3`-scope ruling of the same date. `R7` for the
first (ceiling stated, reviewed the diff against the declared boundary); `V-2` for the second,
because it binds beyond this round.
(d) The preview card (`E11`), a caller-side artifact.

**Ceiling on `V-1`.** My probes prove the guard skips the two token shapes I staged and fires on the
prefixed control. They do not enumerate every shape the sentence mis-describes, and `R4` holds: this
shows the sentence is inexact, not the full extent of what escapes it.
