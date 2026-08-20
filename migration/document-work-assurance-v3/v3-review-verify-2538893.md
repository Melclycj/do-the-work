# Targeted VERIFY — round `DE-PREFIX`, subject `4410899..2538893`

Verdict: **`REVIEWED_NO_BLOCKER`** — 3 low, 5 observations.

Independent session. I was handed a range and the path of my standing instruction, nothing
else; round, batch, budget, authorization, obligations and every figure below are re-derived
from this repository. Where a figure of mine and a figure of the round's differ, mine is the
one I ran and the command is shown.

## 0. Dispatch as received, and what I declined to take from it

The dispatch named the review contract at
`migration/document-work-assurance-v3/v3-harness-review-contract.md`. That file is a stub; it
names `document-harness/CONSTRUCTION-CHECKLIST.md` as its successor and its own counterpart,
and that is what I read end to end — both sides, `E1`–`E12` and `R1`–`R10`. `E10` also owes
`HARNESS-DECISIONS.md` `§live` at a round's opening; I read `HD-50` (the batch authorization)
and `HD-23` (the journal-number channel) there in full, and the `§live` index by grep.

The dispatch asserted that a FULL had already occurred and that my leg is the round's targeted
VERIFY. I took neither on report. `git log` over the range gives four commits; `953db34` is a
record commit whose single file is `v3-review-full-39a21a8.md`, and that record's own verdict
is `CHANGES_REQUIRED`. `E9`'s test — *has a valid independent FULL already occurred?* — is
therefore answered yes by the repository, which makes `2538893` the fix round and obliges this
VERIFY. Nothing about the round's identity came from the prompt.

`HD-50` is where I found that this is R3 of batch `DTW-INDEPENDENCE` and what its four
authorized items are; `CONSTRUCTION-LEDGER.md` confirms R3 is still the queue head and not
CLOSED.

## 1. Subject, re-derived

```
$ git log --oneline 4410899..2538893
2538893 V3-DE-PREFIX-FIX-v1
953db34 V3-REVIEW-RECORD-DE-PREFIX-39a21a8-v1
39a21a8 V3-DE-PREFIX-v1
c969109 V3-REVIEW-RECORD-DE-PREFIX-4410899-v1
$ git rev-parse HEAD          25388938330cfef0d9e8ac730d0866c183f3111b
$ git status --porcelain=v1   (empty)
$ git log --format='%h %p' -4
2538893 953db34 | 953db34 39a21a8 | 39a21a8 c969109 | c969109 4410899
```

Linear, no amend. `E9`'s sequencing clause holds on both review legs: each record commit
carries exactly one file and nothing else landed between dispatch and record.

```
$ git show --stat --format='' c969109    v3-cold-read-4410899.md   | 458 +++
$ git show --stat --format='' 953db34    v3-review-full-39a21a8.md | 485 +++
```

The member blob ids at `39a21a8` that the FULL recorded in its §2.4 are the ids I read at that
commit today — `c2674385 / 7de70e11 / 0d0c617b / 946b4beb / 6d571492 / 29bdc9fb` — so the
candidate was not rewritten under the FULL.

### 1.1 The repair diff, classified by hand

```
$ git show --stat --format='' 2538893
 document-harness/CONSTRUCTION-CHECKLIST.md          |  4 ++-
 document-harness/README.md                          |  2 +-
 document-harness/journal/de-prefix-2026-08-20.md    | 30 ++++++++-----
 tooling/hooks/candidate_path_check.py               | 19 +++++-----
 tooling/hooks/layer_path_check.py                   |  8 +++++-
 tooling/rsclib/document_harness/paths.py            |  9 ++++---
 tooling/tests/document_harness/test_precommit_checks.py | 15 +++++++-
 7 files changed, 63 insertions(+), 24 deletions(-)
```

Seven files, every one inside the approved boundary: `README.md` / `candidate_path_check.py` /
`paths.py` / the `CandidatePath` docstring are `B-1`; `layer_path_check.py` / the new test /
the `E10` clause are `B-2`; the journal's §2 and §5 are `L-1` and `L-2`. Nothing outside. No
record file was touched, and no governance file was:

```
$ git diff --stat 953db34 2538893 -- CONSTRUCTION-LEDGER.md HARNESS-RIDERS.md HARNESS-DECISIONS.md
(no output)
```

That is correct — the ledger and rider updates the candidate declared ride closeout, which has
not happened yet.

## 2. `B-1` — the four falsified sentences, checked one at a time

The blocker was that teaching the layer guard the whole class made four live sentences false,
one of them in an `E10` member, and left the two guards' relationship documented backwards. I
read all four at the tip.

**(a) `document-harness/README.md:36`, the *Local enforcement* row.** The old clause — *"which
takes the class the instruction-layer check skips as possibly illustrative"* — is gone.
Word-diff confirms the edit is bounded to that clause and re-types nothing else. The
replacement is examined in `V-1`; the falsified half `B-1` named is genuinely removed.

**(b) `tooling/hooks/candidate_path_check.py:8-13` and `:17-21`, `:27-29`.** Both sites now
state the post-`DE-PREFIX` fact: the layer guard *"blocks the nowhere-resolving class there
itself — the deliberate skip this paragraph used to describe is that guard's pre-`DE-PREFIX`
history"*, and the two rules *"now agree on the nowhere-resolving class … while this one still
carries the shorthand split the layer guard does not have"*. Accurate against the code. The
sentence stranded between those two rewrites is `V-2`.

**(c) `tooling/rsclib/document_harness/paths.py:15-22`.** Accurate, and I checked its one
historical claim rather than assuming it. The base guard is the falsifier:

```
$ git show 4410899:ResearchSystem/tooling/hooks/layer_path_check.py | sed -n '55,62p'
        from_root = (repo_root / token).exists()
        from_dir  = (file_dir  / token).exists()
        under_rs  = (repo_root / "ResearchSystem" / token).exists()
```

Three probes — so *"the three branches `layer_path_check.py` used for the instruction layer
until round `DE-PREFIX`"* is exact, and the new explanation of why the third branch survives
in `paths.py` (the caller trees this lint scans keep their `ResearchSystem/` directory) is the
right attribution.

**(d) `tooling/tests/document_harness/test_precommit_checks.py`, the `CandidatePath`
docstring.** Rewritten to the same fact. Accurate.

No machinery was added at any of the four, which is what `E6` asks of a fix to text.

### 2.1 The class, swept by me rather than taken on report

`E7` asks for the class, not the instance, and the fix commit claims only *"the four live
sentences"*. I ran the sweep the finding implies over the whole live tree:

```
$ grep -rn  "illustrative" . | grep -v "^./migration/" | grep -v "^./.git/"
$ grep -rni "waves through|skips|skipped class|deliberately skip|wave through" \
      --include=*.py --include=*.md . | grep -v "^./.git/" | grep -v "^./migration/"
$ grep -rn  "missing-prefix|prefix missing|缺前缀" --include=*.md --include=*.py . | …
```

Outside the four, the hits are: three journal files (`xrepo-refs-2026-08-20.md:275,302`,
`simp-a4-2026-08-06.md:22`, `de-prefix-2026-08-20.md`) — records written as-of their round,
which this repository's convention leaves as written, and the candidate already declared four
historical record sites left alone on the same principle; and **one live governance file**,
`HARNESS-RIDERS.md:11`, which is `O-3` below.

So the sweep is one site short of complete, and separately the paragraph the fix rewrote
carries a second falsified sentence it stepped over (`V-2`). Neither is a permission granted
that the true state withholds, so neither is filed above low.

### 2.2 The divergence probe, re-run at the repair tip

`B-1`'s sharpest evidence was a measurement: the two guards disagree in the direction opposite
to what the prose said. I re-ran it against the repaired tree, in a scratch clone, one staged
line added to `document-harness/REVIEW.md` — a surface **both** guards scan
(`scanned('document-harness/REVIEW.md')` is `True`):

```
staged added line:  run `tests/document_harness/run_tests.py` to check

$ python tooling/hooks/layer_path_check.py
pre-commit BLOCKED: … `tests/document_harness/run_tests.py` — resolves nowhere …   exit 1
$ python tooling/hooks/candidate_path_check.py
(no output)                                                                        exit 0
```

The divergence is unchanged by the repair — it was never a documentation bug, it is the actual
behaviour. What changed is only how it is described, and `V-1` is that the new description is
falsified by this same run.

## 3. `B-2` — the parser, fixed, pinned, and probed for what it still cannot see

### 3.1 The change

```python
-        elif line.startswith("+++"):
+        elif line.startswith("+++ "):
```

Exactly the minimum fix the FULL named, four characters including the space.

### 3.2 Mutation, against sha256-checked restores (`E4`, `R8`)

Scratch clone under the session scratchpad, pristine copy taken first, every restore verified
(`40d3fcd55818f2a9e354fcd226921691860c10e40d255bbc13ae8daa951d1c1e`).

| mutation | result | reads |
|---|---|---|
| `startswith("+++ ")` → `startswith("+++")` (the pre-fix defect shape) | **1 failed, 48 passed** — only `test_a_pasted_diff_header_does_not_silence_the_rest_of_the_member`, `AssertionError: 0 != 1` | the new test binds the exact reported shape, and introduces no false positive anywhere else in the class |
| the whole `elif … : current = None` branch deleted | **49 passed** | the header-reset branch is bound by nothing — see `O-2` |

The first row is the claim the commit body makes (*"reproduced red against the pre-fix parser
and green after"*) and it reproduces. `E5` holds: the test's expectation is the hand-written
literal `1`, not anything the module supplies, and the mutation proves the `1` comes from the
token below the pasted header rather than from the header line itself.

### 3.3 The disclosed residual, measured across seven shapes

The commit body, the guard docstring and the `E10` clause all assert the same residual. I
probed it directly against the fixed parser — disposable repository per case, one member
staged, content = a clean line + the probe line + a token resolving nowhere:

```
1  BLOCKED                     pasted diff header, content '+++ ...'
0  fail-open (NOT blocked)     content '++ b/x'
0  fail-open (NOT blocked)     content '++ silences'
1  BLOCKED                     content '++nospace'
1  BLOCKED                     content '++'
1  BLOCKED                     content '+++ /dev/null'
1  BLOCKED                     ordinary line (control)
```

The reported instance is closed and the residual is **exactly** the disclosed class — content
opening `++ ` (two plusses and a space) and nothing wider. `++ b/x` mis-files, any other
`++ …` silences, precisely as both the docstring and the clause say. The disclosure is
accurate, not approximate.

### 3.4 The fix passes its own guard

```
$ git checkout 953db34 && git cherry-pick -n 2538893
$ python tooling/hooks/layer_path_check.py
(no output)   exit 0
```

The `E10` amendment's own added lines carry `` `++ ` `` and `` `++ b/…` `` in backticks; both
contain whitespace, so `TOKEN` never matches them and the guard is not self-blocked. Checked
rather than assumed, because a clause that violated itself in its own example is the shape this
harness has paid for before.

### 3.5 The `E10` amendment is additive

```
$ git diff --word-diff=plain 39a21a8 2538893 -- document-harness/CONSTRUCTION-CHECKLIST.md
… {+an added line whose own content opens `++ ` reads to its diff parser as a file header
(`++ b/…` mis-files the member's remaining added lines, any other `++ …` silences them),+} …
```

Insertion only; no surrounding text re-typed. `E10`'s *additive or subtractive, never re-typed
with the same content* holds.

Whether the list it joins is now complete is `V-3`.

## 4. `L-1` and `L-2` — the two journal numbers, re-measured

`HD-23` puts a journal **number** correction outside the `E9` fix leg and outside the targeted
VERIFY it would otherwise owe, *provided the correction lands inside the next review's subject
range*. Both do — they are in `2538893` and `2538893` is my subject — so the routing is right,
and the numbers are still mine to check.

**`L-1`, the battery figures.** The journal now says 738 at the candidate, 733 collected at the
opening tip, +5 net (7 `LayerPath` tests out, 12 in: 10 from the class rewrite plus the 2
rename tests). Every one of those five figures re-measured in a scratch clone:

```
$ python -m pytest -q --collect-only   @ 4410899   733 tests collected
$ python -m pytest -q --collect-only   @ 39a21a8   738 tests collected
$ python -m pytest -q --collect-only   @ 2538893   739 tests collected
$ … --collect-only tests/document_harness/test_precommit_checks.py | grep -c "LayerPath::"
       @ 4410899   7        @ 39a21a8   12
```

7 out, 12 in, +5. The two rename tests are named
(`test_a_rename_into_the_layer_does_not_rescan_standing_text`,
`test_a_bad_line_added_on_top_of_a_rename_still_blocks`), so 10 + 2 is the real decomposition
and not a back-fit. The pre-correction 736/+3 is gone and the bullet names its own first
version as the `E3` shape it was.

**`L-2`, the sweep block.** The `After` block is now the command's own output. I ran the
command at the repair tree and diffed:

```
$ python tooling/sweep_refs.py . > sweep_now.txt
$ diff <journal block, prompt line dropped> sweep_now.txt
(identical: 18 lines, 17 rows + the tally)
```

Byte-for-byte. The annotated `LINK … <- fixed this round` row is gone, the tally reads 17, and
the `../../README.md` row is relocated to prose that says when it was real. `E3`'s *paste tool
output, never describe it from memory* is satisfied on the sentence that failed it.

**Battery at the repair tree, run by me immediately before writing this section:**

```
$ cd tooling && python -m pytest -q
739 passed in 105.45s (0:01:45)
```

739 — the commit body's figure exactly, and 738 + the one new test.

## 5. `L-3` and `L-4` — the two acknowledged-without-byte-fix items

Both are on immutable commits, so there was nothing to verify except that the disposition is
honest.

**`L-3` (trailers).** Re-measured:

```
$ git log --format='%h |%(trailers)|' -3
2538893 ||     953db34 ||     39a21a8 |Co-Authored-By: … / Claude-Session: …|
```

`39a21a8` remains the only commit in this repository carrying trailers, and the fix commit's
promise — *"this commit and every later one here carries none"* — holds for every commit in the
subject. `E8` also forbids amending, so a recorded deviation is the only available disposition.

**`L-4` (the `E1` disclosure wording).** The fix commit carries the standing correction: the
reviews were dispatched so that the executor held none of the four question-setting holdings.
That is the `R1` test stated correctly. I cannot verify the process claim itself — see §8.

## 6. Permanent boundaries (`R3`: run second)

- **`E2`.** `git diff 39a21a8 2538893 -- contract/ schema/document-assurance-v3/` returns
  nothing. At the tip the eighteen files are present and the three ids `E2` names literally are
  intact: contract `b2dbdf75…`, supersession-1 `68031fa2…`, supersession-2 `e1a2f26b…`. No
  frozen byte written.
- **`E9` budget.** One read (`c969109`, spends nothing), one FULL (`953db34`), one
  user-approved fix (`2538893`), this VERIFY. The cap is respected and no round was renamed to
  escape it. `L-1`/`L-2` rode the `HD-23` channel and consumed nothing extra.
- **`E8`.** Title `V3-DE-PREFIX-FIX-v1` names the round; the kind is named in the first four
  words (*"Review fix, the round's one user-approved repair"*); one dense paragraph; no
  trailers; no amend; no push — `git branch -a --contains 2538893` returns `main` only against
  a real `origin` (`https://github.com/Melclycj/do-the-work.git`). Explicit-path staging is not
  observable from a commit (§8).
- **`E6`.** Both blockers are answered by the thing changing, not by a rule about it: `B-1` is
  four sentences, `B-2` is one character plus a test. The `E10` clause addition is a disclosure
  of the residual the FULL explicitly asked to see disclosed, not a substitute for the code fix,
  so there is nothing here for a VERIFY to refuse.
- **`E10`, the layer read still owed.** Six members changed across the round and two changed
  again in the fix. This VERIFY does not discharge that read — `E10` says the read's subject is
  the amendment text itself, never the work it governs. Recorded so the next round's opening
  cold read can cite blob ids rather than re-derive them:

| member | `4410899` | `39a21a8` | `2538893` |
|---|---|---|---|
| `document-harness/CONSTRUCTION-CHECKLIST.md` | 92cbaea3 | c2674385 | **cacd99d4** |
| `document-harness/README.md` | be4766fc | 7de70e11 | **45ce38cf** |
| `document-harness/EXECUTION.md` | 6dc79f3f | 0d0c617b | 0d0c617b |
| `document-harness/REVIEW.md` | 4a407f65 | 946b4beb | 946b4beb |
| `document-harness/ORCHESTRATION.md` | 80f42658 | 80f42658 | 80f42658 |
| `…/v3-harness-operating-contract.md` | 70f3e5dd | 6d571492 | 6d571492 |
| `…/v3-harness-review-contract.md` | bc395e1c | 29bdc9fb | 29bdc9fb |
| supersession-1 | 68031fa2 | 68031fa2 | 68031fa2 |
| supersession-2 | e1a2f26b | e1a2f26b | e1a2f26b |
| `paragraph-map.schema.json` | 09aa8699 | 09aa8699 | 09aa8699 |

- **`E12`.** The handoff was a range, no per-acceptance argument. The freeze marker written at
  dispatch carries it verbatim (`.harness/review-pending.json`:
  `"subject": "4410899…..25388938…"`), which is also how I confirmed my own leg's identity
  without taking it from the prompt.
- **Whole-stock resolution, unchanged by the repair.** The guard predicate over the complete
  text of all ten members: 5 hits, all inside the two `E2`-frozen supersessions, the eight
  writable members clean. `sweep_refs.py` agrees at 17 with 5 PATHTOK rows. `dtw --help` lists
  seven operations at the new path.

## 7. Findings

### `V-1` (low) — the replacement sentence in the `E10` member states a relationship the round's own probe falsifies, and contradicts the docstring the same commit rewrote

**Location.** `document-harness/README.md:36`, *Local enforcement* row, tip:

> the candidate-side path lint, which covers work products — a surface the instruction-layer
> check never scans — and blocks a newly written path that exists nowhere in the index while
> passing unique-suffix shorthand; since round DE-PREFIX the instruction-layer check blocks the
> nowhere-resolving class on its own ten members too, **so the two guards differ by surface, not
> by class.**

**Ground truth, measured (§2.2).** On `document-harness/REVIEW.md` — a surface **both** guards
scan — one shorthand token is blocked by the layer guard (exit 1) and passed by the candidate
lint (exit 0), in the same tree, at the repaired tip. The guards differ by class on the shared
surface, and the shorthand split is the class they differ on. The same sentence supplies the
falsifying fact four clauses earlier (*"while passing unique-suffix shorthand"*) and then
generalizes past it.

The surfaces are not disjoint either: `[p for p in LAYER if candidate_path_check.scanned(p)]`
is **9 of 10** at this tip. `candidate_path_check.py:17-18`, rewritten in this same commit,
says so out loud — *"The two are **not** a partition of the tree"* — and `:28-29` closes with
*"a second rule applying on top, **not a division of territory**"*. `README.md` is the member;
the docstring is right and the member is wrong, which is the same asymmetry `B-1` blocked on,
pointing the other way.

**Why low and not inflated.** No permission is granted that the true state withholds: both
guards still run, both are advisory, and a writer who trusts the sentence meets the stricter of
the two at commit time rather than slipping past it. What is lost is the accuracy `E3` demands
of a factual assertion in instruction text, on the one sentence this fix leg exists to get
right.

**Named downstream decision (`R9`).** `ONBOARDING.md:130`'s Owner cell sends a new caller to
this exact row to learn *"what each guard does"*. A newcomer reads *differ by surface, not by
class*, concludes that knowing a file's surface tells them which rule applies, writes a
shorthand token into a member on the strength of the candidate lint's carve-out, and is blocked
by a guard the row told them was not in play there.

**Minimum fix — exact bytes, no machinery, no bound added.** Replace

> so the two guards differ by surface, not by class.

with

> the two overlap on the members this lint also scans, and there they still differ on
> shorthand: a unique tracked suffix passes this lint and not that one.

### `V-2` (low) — the sentence the `B-1` repair stepped over: the overlap's stated reason is false at this tip, and the de-prefixing is why

**Location.** `tooling/hooks/candidate_path_check.py:25-26`, between the two halves of the
paragraph the fix rewrote:

> `[p for p in layer_path_check.LAYER if candidate_path_check.scanned(p)]` — 7 at `2026a14`,
> **the two retired-contract stubs being the members a `RECORD_SURFACE` prefix exempts.**

**Ground truth, measured at the tip.**

```
members scanned by candidate_path_check at 2538893: 9
NOT scanned: schema/document-assurance-v3/paragraph-map.schema.json
```

Nine, not seven, and the one exempt member is exempt by **extension** (`scanned()` requires
`.md`), not by any prefix. The two retired-contract stubs now live at
`migration/document-work-assurance-v3/…` while `RECORD_SURFACE` still reads
`"ResearchSystem/migration/"` — the round removed the prefix and left every `NOT_SCANNED`
entry pointing at a path shape this repository no longer has. *"7 at `2026a14`"* is dated and
therefore fine; the clause after it is written as a standing structural fact and is false.

**Measured consequence, in the deadlock the comment itself names.** `RECORD_SURFACE`'s own
docstring says a record *"quotes the broken path it is reporting. Scanning one blocks the
returned review record, and `E9`'s freeze window admits only that record — leaving no legal
commit ordering."* At this tip:

```
staged:  migration/document-work-assurance-v3/v3-review-probe-record.md
         The FULL reported a broken token `no/such/file.md` at that site.
$ python tooling/hooks/candidate_path_check.py
pre-commit BLOCKED: … `no/such/file.md`                                   exit 1
```

The exemption that exists to prevent exactly this no longer applies here.

**Live damage today: zero.** `.githooks/pre-commit` in this repository runs
`layer_path_check.py` and nothing else, and says so in its own body. The finding is that the
docstring hides a real state change rather than that a commit is blocked — and rider
`self-caller-guards` is the open proposal to wire the other two guards here, at which point the
deadlock becomes live.

**Minimum fix — exact bytes.** Replace *"the two retired-contract stubs being the members a
`RECORD_SURFACE` prefix exempts"* with

> 9 at `2538893`, the schema member being the only one `scanned()`'s `.md` test drops —
> round `DE-PREFIX` removed the `ResearchSystem/` prefix from this repository while
> `NOT_SCANNED` still names it, so on this repository these prefixes exempt nothing and a
> record here would be scanned. The caller trees this lint actually runs against keep the
> prefix, which is why the constants were left alone.

The second half restates the round's own recorded scoping choice; whether the constants should
change is `R5`, the user's, and rider `submod-index` is where it already sits.

### `V-3` (low) — `E10`'s "what the guard still cannot see" list is still offered as complete and is still short, with a standing instance inside a member

**Location.** `document-harness/CONSTRUCTION-CHECKLIST.md:152-157`, the sentence this fix
amended:

> What the guard still cannot see is held by this clause alone: **a token carrying a placeholder
> segment falls outside its path shape**, prose and markdown links carry no backtick token for
> it to find, an added line whose own content opens `++ ` … and the standing text it never
> re-scans stays unscanned

**Ground truth.** Path-shape blindness is enumerated by *one instance*. The filter is
`PATHLIKE = ^[A-Za-z0-9_.\-/]+(?:\.(?:md|py|json|yaml|yml|txt|js)|/)$`, so it also drops every
extension-less path and every extension outside those seven. Paired probe, one staged commit,
positive control in the same run so the guard is proven reached:

```
staged added lines in document-harness/REVIEW.md:
  Paired probe: `tooling/no-such-script.sh` and `.githooks/no-such-hook` (both resolve nowhere).
$ python tooling/hooks/layer_path_check.py        (no output)   exit 0

then, one more line added:
  Positive control: `tooling/no-such-script.md`.
$ python tooling/hooks/layer_path_check.py
pre-commit BLOCKED: … `tooling/no-such-script.md` — resolves nowhere …   exit 1
```

Both shape-invisible tokens pass silently in the run whose control blocks.

**Standing instance, in a member, today.** Enumerating backticked slash-tokens across all ten
members that fail `PATHLIKE`: `` `.githooks/pre-commit` `` in `document-harness/README.md`
(resolves, so nothing is missed today), plus two brace/glob forms in the checklist. The class
is live, not hypothetical, and the `.sh` / `.toml` / `.html` / `.jsonl` / extension-less shapes
are all invisible.

**Why this and not the whole `B-2` ground truth again.** `B-2` blocked because the clause
*"is offered as complete and this is a fourth member of it, introduced by the same commit."*
The repair added the fourth member. The enumeration is still offered as complete, and the shape
filter's other half was already there. Low rather than must-fix because the omission predates
this round and grants no permission the true state withholds — the clause forbids the write
either way.

**Bytes, and a routing caveat that is not mine to settle.** The accurate form of the first item
is *"a token whose shape the check does not read — a placeholder segment, an extension outside
the seven it lists, or no extension at all — falls outside its path shape"*. But those bytes
widen what the clause holds, which is `E10`'s design test, and `E10` says design wins over the
free channel and opens a round. So this most likely banks as a rider naming a round-eligible
surface rather than riding a batch; the call is the orchestrator's under `R10`, and I record
the bytes so it is a routing decision rather than a re-derivation.

### `O-1` (observation) — the newly disclosed residual is the only one of the class's three ceilings that no test pins

`LayerPath`'s class docstring says *"Runtime markers and placeholder-bearing tokens are
deliberately out, and **each carve-out is pinned below so the module docstring's claims stay
honest**."* And they are: `test_a_runtime_marker_counts_as_resolving`,
`test_a_placeholder_token_is_invisible_by_shape`. The `++ ` residual, now asserted in the guard
docstring *and* in an `E10` member, has no such test. A later parser change that alters it would
falsify an instruction-layer clause silently — which is the drift the whole `E10-sync` rider
exists to name. Recorded rather than filed as a finding because adding a test is machinery and
`E6` argues against reaching for it reflexively; the asymmetry against the class's own stated
convention is the observation.

### `O-2` (observation) — deleting the header-reset branch entirely leaves 49/49 green, and the reason is that it is inert

Second mutation, §3.2. The branch is unpinned, but not by oversight: on real `-U0` output the
only header it can match is `+++ /dev/null`, which belongs to a deletion, and a deletion carries
no `+` lines. The whole of the fix's behavioural force is in the narrowing of the *first*
branch's fall-through. Recorded because *"never trust a guard you have not seen fail"* cuts both
ways — I saw this half not fail, and the honest reading is inert-by-construction rather than
untested-by-accident.

### `O-3` (observation) — `HARNESS-RIDERS.md:11` carries two `B-1`-class sentences beyond the count and home the FULL's `O-3` already named

Rider `frozen-path-prefix` says of the four tokens it tracks: *"以上三个属 `layer_path_check`
的 missing-prefix 类"* and, of `templates/run-v2/`, *"哪儿都解析不到，故被 `unresolved_tokens`
按设计跳过"*. Both are `B-1`'s exact shape. The guard has had no missing-prefix class since this
round (`layer_path_check.py:5-10`: *"One class is flagged now, and nothing else"*), and
`templates/run-v2/` is not skipped — it is one of the five hits my whole-stock predicate run
returns. The candidate declared *"rider `frozen-path-prefix` updates at closeout"*, but scoped
to the 4→5 token count and the changed home; the two behaviour sentences are not in that scope,
and this is the one live non-record site the `B-1` sweep did not reach.

### `O-4` (observation) — the fix leg met two riders' touch conditions and neither redemption nor its impossibility is recorded

Riders `submod-index` and `decited-paths` both name *"下一批碰 `paths.py` / `candidate_path_check.py`"*
as their redeem-when. `2538893` changed both files with real content. Neither row moved, and
nothing in the commit body, the journal or the bank says why. The structural reason is real —
both rows state *"无字节"* and that the fix is design (`R5`, the user's), and `R10` says a
design-fix rider *"names a redeem-when surface that may open one, never any batch"*, which a
fix leg bounded by a user-approved repair is not. So what is missing is the recorded
impossibility, not the redemption. This is the same shape the FULL filed as its own `O-2`
against `mount-inert`, recurring one commit later inside the same round; also worth noting that
`submod-index`'s redeem-when, as written, names *any* batch, which is the malformed shape `R10`
describes for a design-fix row.

### `O-5` (observation, `R5`) — three consecutive fix legs, one sentence family, the same failure

`XREPO-REFS`'s `B-1` was *the clause said more about the guard than the guard did*; that round's
fix leg drew VERIFY `V-1` for the same permissive error *"one shape smaller"*. `DE-PREFIX`'s
`B-1` was again a guard-description falsification, and its fix leg draws `V-1` above for a new
false characterization of the same relationship. The relationship between the two path guards
is currently asserted in prose in at least five live places — an `E10` member row, two docstring
paragraphs, a test-class docstring and a rider row — with no guard over any of them, which is
rider `E10-sync`'s prose-leg problem applied to behaviour rather than to membership. Whether
that relationship should be stated once, in one place, with the others pointing at it, is a
question about whether a thing should exist — `R5` puts that with the user, and I report only
the measured shape.

## 8. Disclosure (`R4`)

**Read in full:** `document-harness/CONSTRUCTION-CHECKLIST.md` (both sides); the FULL record
`v3-review-full-39a21a8.md`; the complete diff of all 7 repaired files; `layer_path_check.py`
at the tip; `candidate_path_check.py` at the tip; `.githooks/pre-commit`; the `LayerPath` and
`LayerMembership` test classes; the two review-side commit bodies and the two work-side ones;
the two retired contract stubs.

**Sampled:** `HARNESS-DECISIONS.md` (`HD-23` and `HD-50` in full, `§live` headings by grep);
`HARNESS-RIDERS.md` (rows `frozen-path-prefix`, `E10-sync`, `submod-index`, `mount-inert`,
`decited-paths`, `self-caller-guards`); `CONSTRUCTION-LEDGER.md` (the queue-head block);
`paths.py` (header and ceilings); `document-harness/README.md:36` and `ONBOARDING.md:130`; the
root `README.md` at `:51/:52/:78`; `journal/de-prefix-2026-08-20.md` §2 and §5 with their
surroundings; `journal/xrepo-refs-2026-08-20.md` at the two sweep hits;
`v3-review-verify-2937bcd.md` §`V-1` for tiering precedent.

**Only probed:** the base `layer_path_check.py` (the resolution block and `added_lines` only);
the 733-test battery beyond `test_precommit_checks.py` — executed, not read; every file outside
the 7-file repair diff, which I confirmed unchanged by the range diff rather than by reading.

**Re-executed:** the full battery at the repair tree (739); `--collect-only` at all three
revisions; `LayerPath` counts at two; `sweep_refs.py` with a mechanical diff against the journal
block; the whole-stock guard predicate over all ten members; the two-guard divergence probe; the
candidate-lint record-deadlock probe; a seven-shape adversarial probe of the fixed parser; the
shape-invisibility paired probe with positive control; the member-wide enumeration of
shape-invisible tokens; two mutations with sha256-checked restores; the guard run over the
cherry-picked fix; the frozen-blob tree diff; the member blob table; trailers, parents, branch
containment and remote; `dtw --help`.

**`UNVERIFIABLE`, not folded into supported:**

- The user approval of 2026-08-20 said to cover `B-1`, `B-2`, `L-1`, `L-2` — no carrier in the
  repository. `HD-50` records the batch's four items, not this approval, and `E11`'s preview
  card still has no home. `R7`: I state the ceiling and move on. The scope I *can* check —
  every changed file traces to a finding in the FULL — is clean.
- That the FULL record was committed unchanged. A process claim, marked, not verified.
- Whether the 7 files were staged as explicit paths rather than `add -A`. Not observable from
  a commit.
- The journal's `103.30s` battery timing at the candidate commit. The count (738) I verified;
  a wall-clock from a run I did not witness I cannot.
- Mutation proves these tests have binding force; it does not prove that force is sufficient.
  `O-1` names one place where a newly asserted behaviour has none at all.

## 9. Why `REVIEWED_NO_BLOCKER`

Both accepted blockers are answered, and answered in the shape `E6` asks for. `B-1`'s four
sentences are corrected at all four sites with no machinery added, and the two structural claims
they turn on — the base guard's three branches, the candidate lint's surface — I checked against
the code rather than against the commit body. `B-2`'s parser is fixed with the exact minimum the
FULL named, pinned by a must-fire test that goes red on precisely the pre-fix shape and takes
nothing else with it, and its residual is disclosed in two places and measured by me across
seven line shapes to be exactly the class disclosed and no wider. The two journal numbers now
say what the commands say, verified by re-running both commands and diffing. Every permanent
boundary holds: no frozen byte written, budget spent once, no amend, no push, no record touched,
the amendment additive, the handoff a range.

What I found is three low findings and five observations, and they share one direction: the
repair closed the sentences it was pointed at and did not sweep the class around them. One live
governance site kept a falsified sentence (`O-3`), one falsified sentence survived inside the
very paragraph the repair rewrote (`V-2`), the replacement for the flagged sentence introduced a
new characterization measurement contradicts (`V-1`), and the clause amended to close a
completeness gap is still offered as complete while short (`V-3`). None of them grants a
permission the true state withholds, none blocks, and none is worth inflating — but the pattern
across three consecutive fix legs is `O-5`, and that one is the user's to answer, not mine.
