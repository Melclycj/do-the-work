# Targeted VERIFY — round `INIT-SURFACE` at `84dea06`

**Verdict: `REVIEWED_NO_BLOCKER`.** 1 low, 5 observations.

`B-1` is closed. The three restatements the FULL located are gone or reduced to pointers, and the
`README.md:36` sentence they falsified — *the guards' and their tests' docstrings name their own
subject and point here instead of restating the relationship* — is now true. I did not establish
that with the round's keyword grep, which still cannot reach a phrasing it does not list; I
extracted every docstring of the two guards and their two test modules (22 docstrings, 13 055
characters) and read the corpus end to end. That is the command the sentence's quantifier needs,
and the round did not run it (`O-1`).

The three approved riders (`L-2`, `O-3`, `O-4`) landed correctly, nothing outside the declared
scope moved, the frozen surface is byte-identical from range base to tip, and both batteries, the
sweep tally, the class sweep and the one code-shaped edit in the repair were re-executed here
rather than accepted.

What the repair introduced is `L-1` below: two new pointer sentences hand *why the two guards must
agree on what a path is* to the `README.md` home row, and that row does not carry the fact — it
carries the opposite-flavoured one, that the two **differ**. One of the two then restates the
handed-away fact four lines under its own *not restated here*, which is the same internal shape
`B-1` named at `candidate_path_check.py`.

---

## 1. Subject, round, budget and leg — re-derived, nothing taken from the dispatch

```
$ git rev-parse HEAD
84dea0678b2e43f3f5072b6c283d3f0e742c8afb
$ git branch --show-current
main
$ git status --porcelain
(empty)
$ git rev-list --left-right --count origin/main...HEAD
0	62
```

HEAD is the subject tip, the tree is clean, and the branch is 62 commits ahead of `origin/main`,
unpushed (`E8`) — 60 at the FULL plus the FULL's record and this round's fix. The six commits in
range, oldest first, with the kind each names in its own body:

| commit | title | kind |
|---|---|---|
| `32f24b8` | `V3-REVIEW-RECORD-INIT-SURFACE-17ce3ed-v1` | record — opening cold read of the layer |
| `bba6f94` | `V3-INIT-SURFACE-AMEND-M1-v1` | amendment — answers that read's `M-1` |
| `a4b5565` | `V3-REVIEW-RECORD-INIT-SURFACE-bba6f94-v1` | record — independent re-read of the amendment |
| `7f6e7f0` | `V3-INIT-SURFACE-v1` | candidate |
| `e80538f` | `V3-REVIEW-RECORD-INIT-SURFACE-7f6e7f0-v1` | record — the round's FULL |
| `84dea06` | `V3-INIT-SURFACE-FIX-v1` | review fix |

**Which leg this is.** `E9`'s test is *has a valid independent FULL already occurred?* `e80538f`
records one, returning `CHANGES_REQUIRED` on `7f6e7f0`, so `84dea06` is the round's **one
user-approved fix** and obliges exactly this **targeted VERIFY**. Nothing before the FULL consumed
a leg: the cold read and the amendment+re-read pair are `E10` machinery. Ordering holds — the
branch took no commit between each dispatch and its record:

```
$ git log --format='%h %ad %s' --date=format:'%H:%M:%S' 17ce3ed..84dea06 --reverse
32f24b8 22:51:29 V3-REVIEW-RECORD-INIT-SURFACE-17ce3ed-v1
bba6f94 22:52:39 V3-INIT-SURFACE-AMEND-M1-v1
a4b5565 23:05:33 V3-REVIEW-RECORD-INIT-SURFACE-bba6f94-v1
7f6e7f0 23:37:38 V3-INIT-SURFACE-v1
e80538f 00:12:01 V3-REVIEW-RECORD-INIT-SURFACE-7f6e7f0-v1
84dea06 00:18:34 V3-INIT-SURFACE-FIX-v1
```

**Round.** `INIT-SURFACE`, batch `DTW-INDEPENDENCE` **R4**, chartered by `HD-50` in
`HARNESS-DECISIONS.md` `§live` (`R1`–`R3` CLOSED, *R4 未开*). Read from the repository, not the
dispatch.

**Freeze marker.** `.harness/review-pending.json` names this exact subject and no other:

```
{"subject": "17ce3edbb5ba52c4b8b096f0cc4dd506c92922da..84dea0678b2e43f3f5072b6c283d3f0e742c8afb",
 "dispatched_at": "2026-08-20T14:18:43+00:00"}
```

Nine seconds after the fix commit's authored time. Left in place.

**Trailers:** `git log --format='%h |%(trailers)|' 17ce3ed..84dea06` returns empty brackets for all
six (`E8`).

## 2. What a targeted VERIFY covers here

`R3`: the accepted findings, the whole repair diff, and the permanent boundaries. The fix body
declares its scope as *B-1 plus the three approved riders L-2, O-3, O-4 of `v3-review-full-7f6e7f0.md`;
nothing else touched* — approval dated 2026-08-21. The FULL's `L-1` (the `--into` disposition) is
**not** in the fix and is not this VERIFY's to close; see `O-3`.

## 3. Changed paths of the repair, classified by hand

```
$ git show --stat --format= 84dea06
 document-harness/ONBOARDING.md                           | 2 +-      not a member (own header)   L-2
 document-harness/README.md                               | 2 +-      E10 member                  L-2
 tooling/hooks/candidate_path_check.py                    | 3 +--     docstring only              B-1
 tooling/rsclib/document_harness/paths.py                 | 3 ++-     comment only                B-1
 tooling/tests/document_harness/test_precommit_checks.py  | 4 +++-    class docstring only        B-1
 tooling/tests/document_harness/test_sweep_refs.py        | 7 ++++--- module docstring + 1 assert O-3, O-4
 6 files changed, 12 insertions(+), 9 deletions(-)
```

Every path maps to an approved finding and nothing else appears. The only **executable** line the
repair changes anywhere is `test_sweep_refs.py:119` (`O-4`); the other five hunks are inside
docstrings or a `#:` comment. (`git diff --shortstat 7f6e7f0 84dea06` reports 7 files / 452
insertions because it also spans `e80538f`'s 440-line record file — the repair itself is the 6
above.)

**`E2`'s freeze surface is untouched**, by tree comparison across the whole range rather than by
reading the diff:

```
$ for c in 17ce3ed 7f6e7f0 84dea06; do git ls-tree -r $c -- contract/ schema/document-assurance-v3/ | md5sum; done
f7e2901936585e0dfb736320d21b4ea1  -
f7e2901936585e0dfb736320d21b4ea1  -
f7e2901936585e0dfb736320d21b4ea1  -
```

**`E10`-sync is correctly not triggered**: `CONSTRUCTION-CHECKLIST.md` is absent from the repair,
`layer_path_check.LAYER` is unchanged, and `test_precommit_checks.py`'s edit is in
`OneNotionOfAPath`, not `LayerMembership.EXPECTED`.

## 4. Re-executed, not accepted

### 4.1 The two batteries

```
$ python tooling/tests/document_harness/run_tests.py
Ran 288 tests in 42.422s
OK
$ python tooling/tests/document_harness_review/run_tests.py
Ran 460 tests in 65.759s
OK
```

288 + 460 = **748**, the figure the fix body claims. The wall clocks it reports (44.5 s / 68.0 s)
are from a run I did not witness — `UNVERIFIABLE`, and immaterial.

### 4.2 The sweep tally

```
$ python tooling/sweep_refs.py .
… -- 17 caller-held or unresolvable references over 10 members
```

Unchanged, as claimed. `sha256(tooling/sweep_refs.py)` is
`7996057ddf4522d7b1581b61965bf752f949c117d9c122225f014aaf347a9d22` — byte-identical to the value
the FULL recorded at `7f6e7f0`, so the repair did not touch the instrument its new tests pin.

### 4.3 The class sweep, run wider than the round ran it

The fix extends the keyword set with the two phrases the FULL showed the old five could not reach.
I ran the extended set over **the whole repository** (`--include=*.md --include=*.py`, excluding
only `migration/…/v3-*.md` records and the two journal directories as immutable history) — a wider
scope than the round's declared 11 live sites:

```
$ grep -rniE "never scans|partition of the tree|division of territory|division of labour|divide the work|share no verdict|agree on what a path" …
document-harness/README.md:36                                  (the declared home)
tooling/hooks/candidate_path_check.py:8                        (pointer)
tooling/rsclib/document_harness/paths.py:18                    (pointer)
tooling/tests/document_harness/test_precommit_checks.py:251    (pointer)
tooling/tests/document_harness/test_precommit_checks.py:350    (pointer)
```

Exactly 5 lines — the home plus four pointers, none carrying a relationship fact. The fix's figure
reproduces, and reproduces at a scope larger than the one it declared.

### 4.4 The scope-covering read the sentence actually needs (`B-1`'s ground truth)

`README.md:36` quantifies over *the guards' and their tests' docstrings*. A keyword grep cannot
falsify that; an enumeration of the corpus can. Every docstring of the two guards and their two
test modules, extracted with `ast.get_docstring` over `Module` / `ClassDef` / `FunctionDef`:

```
tooling/hooks/layer_path_check.py:                       2 docstrings,  2830 chars
tooling/hooks/candidate_path_check.py:                   2 docstrings,  3424 chars
tooling/tests/document_harness/test_precommit_checks.py:14 docstrings,  5432 chars
tooling/tests/document_harness/test_sweep_refs.py:        4 docstrings,  1369 chars
```

22 docstrings, 13 055 characters, dumped and **read in full** (229 printed lines). Result: no
docstring restates the division of labour. `layer_path_check.py` never mentions the other guard at
all; `candidate_path_check.py`, `CandidatePath` and `OneNotionOfAPath` carry pointers; the
remaining nineteen are about their own subject. **`B-1` is closed** — at all three sites it named,
and across the class its quantifier covers.

Site by site against the FULL's minimum fix:

1. `candidate_path_check.py:12-13` — `; the two hooks keep separate rules on purpose and share no
   verdict` deleted verbatim, as the FULL specified. The paragraph now ends at *`rsclib.document_harness.paths`
   holds the whole decision*, a local fact.
2. `tooling/rsclib/document_harness/paths.py:55` — the relationship clause *so the two guards agree
   on what a path is* is gone; what remains, *Mirrors `layer_path_check.PATHLIKE`, kept identical by
   hand*, is this constant's own subject. Accepted as pointer form. Its replacement clause is
   `L-1`.
3. `test_precommit_checks.py:349` — *The two guards disagree on verdicts by design* is gone; the
   opening line is now the class's own subject (the pattern-equality pin), and the stdlib-only
   rationale kept below is what the class itself tests. Accepted. Its new parenthetical is `L-1`.

### 4.5 `L-2` — applied, and applied everywhere

```
$ grep -rn "of the wiring\|onboarding items\|onboarding work" --include=*.md .   (records excluded)
document-harness/README.md:30   … ruled 2026-08-20: of the onboarding items, the **tree half** …
```

One hit; no `of the wiring` survives in any live file. `ONBOARDING.md:74`'s pointer dropped the
same three words in the same commit, so the two now read consistently. The bytes differ from the
`of the onboarding work` the FULL offered — permissible: `L-2` was tiered wording-level, so `R9`
routes it (*rides the next batch*), and only the `E10` free channel demands the record's exact
bytes. The substitute is at least as accurate: `README.md:30`'s own row opens *nine items*, and
the criterion's machine-half examples span items 1, 5, 7 and 9, so *the onboarding items* is the
quantifier the parentheticals already implied.

I checked whether this counts as `E10` design rather than wording — it does not. What `init` may
absorb is unchanged; the FULL had already established the general reading was recoverable from the
sentence, so no rule's requirement moved.

### 4.6 `O-3` — the docstring's negative-control claim is now bounded and true

*Each reference-form must-report case is paired with a clean baseline asserted in the same test …;
the MISSING case's baseline is the clean-layer test beside it.* Verified against the module: the
three reference forms are asserted with their clean siblings inside
`test_each_reference_form_is_reported_exactly_when_broken`, and
`test_a_clean_layer_reports_zero_and_exits_zero` sits immediately after
`test_a_missing_member_is_reported_and_exit_stays_zero` and supplies the present-member baseline
the MISSING case lacks in its own body. Both halves of the new sentence hold.

### 4.7 `O-4` — the dead `.replace()` is gone and the control still binds (`R8`, `E4` shape)

`test_sweep_refs.py:119` is now `self.assertNotIn("target.md", out)`. The removal is
behaviour-identical (the removed string `phantom.md` does not contain `target.md`), so the risk is
not weakening but vacuity — a control that can never fire. Mutation, with the module copied to a
scratchpad and `sha256` checked before and after, never `git checkout --`:

```
mutation: resolves() returns False unconditionally
$ python -m unittest test_sweep_refs
FAILED (failures=4)
  AssertionError: 'target.md' unexpectedly found in 'LINK    docs/member.md:1  target.md
  LINK    docs/member.md:1  gone.md …'
restore: sha256 7996057ddf4522d7b1581b61965bf752f949c117d9c122225f014aaf347a9d22 (identical)
$ python -m unittest test_sweep_refs   →  Ran 9 tests … OK
$ git status --porcelain                →  (empty)
```

The control fires on the real defect shape (a whole sibling wrongly reported), so it binds. `R4`:
this proves force, not sufficiency.

### 4.8 Both guards replayed over the repair's added lines

Added lines extracted per path with the guard's own `-M -U0` parser and fed to
`layer_path_check.unresolved_tokens` and `paths.unresolved_path_tokens`:

```
document-harness/ONBOARDING.md                           added=1  LAYER not-a-member  CAND OK
document-harness/README.md                               added=1  LAYER OK            CAND OK
tooling/hooks/candidate_path_check.py                    added=1  LAYER not-a-member  CAND not-scanned
tooling/rsclib/document_harness/paths.py                 added=2  LAYER not-a-member  CAND not-scanned
tooling/tests/document_harness/test_precommit_checks.py  added=3  LAYER not-a-member  CAND not-scanned
tooling/tests/document_harness/test_sweep_refs.py        added=4  LAYER not-a-member  CAND not-scanned
```

Clean. Note the guards are structurally blind to the whole repair except its two Markdown lines:
the four `.py` files fail `scanned()`'s `.md` test and are not members. Nothing in `L-1` below
could have been caught by machine, which is why it is a review finding and not a guard gap.

## 5. Findings

### `L-1` (low; wording-level by `R9`'s test, exact bytes supplied) — two new pointers send *why the two guards must agree* to a home row that does not say it, and one of them restates the fact four lines below its own *not restated here*

**Locations**, both written by `84dea06`:

1. `tooling/rsclib/document_harness/paths.py:55-56` —
   *"Mirrors `layer_path_check.PATHLIKE`, kept identical by hand — **why the two guards must agree
   is the home row's to say** (`document-harness/README.md`, *Local enforcement*)."*
2. `tooling/tests/document_harness/test_precommit_checks.py:350-351` —
   *"(**Why they must agree**, and how the two divide the work, is the *Local enforcement* row of
   `document-harness/README.md` — not restated here.)"*

**Ground truth violated.** The home row does not carry that fact. Measured on the row itself:

```
$ sed -n '36p' document-harness/README.md | grep -oiE "agree[a-z]*|identical|same (path|token|notion)|notion of a path|pattern|differ[a-z]*|overlap" | sort | uniq -c
      1 differ
      1 overlap
```

No `agree`, no `identical`, no `pattern`. What the row does say about the pair's agreement is the
opposite-flavoured fact — *the two overlap on the members this lint also scans, and there they
still **differ** on shorthand* — so a reader following either pointer for *why they must agree*
lands on a sentence about how they differ. This is a factual assertion newly written into text
without running the command that could falsify it (`E3`), and it is the second-order form of the
defect `B-1` reported: `B-1` was a claim about docstrings that the docstrings falsified; this is a
claim about the home row that the home row falsifies.

Compounding it at location 2: the parenthetical hands *why they must agree* away as *not restated
here*, and the paragraph four lines below states it — *"That robustness is worth one duplicated
pattern; what it is not worth is a **silent divergence**"* is precisely why they must agree. That
is the same internal contradiction the FULL found at `candidate_path_check.py:12-13` (a *does not
restate it* sentence with a restatement four lines under it), reproduced by the commit repairing
it. The rationale itself belongs where it is — it is what the class tests — so the defect is the
sentence that gives it away, not the sentence that states it.

**`R9`'s test, answered.** No actor's action changes: no check outcome (§4.8 — neither guard reads
`.py`), no evidence binding, no permission, no obligation, no verdict path. The accurate fact is
recoverable from adjacent text — the paragraph immediately below location 2 states it. So this is
**wording-level**, and I do not inflate it. The downstream decision I can name is a maintenance
one rather than an actor's: the next reader who wants that *why* follows the pointer, finds
nothing, and either widens the home row with a fact it was never ruled to hold, or reads the pin as
obsolete because the row says the two differ. Named, not asserted as certain.

**Exact bytes** (so whichever channel takes it needs no drafting):

`paths.py:54-56` →

```
#: Path-shaped: a slash, plus either a known extension or a trailing slash. Mirrors
#: `layer_path_check.PATHLIKE`, kept identical by hand; what keeps them equal is the
#: `OneNotionOfAPath` pin in `tooling/tests/document_harness/test_precommit_checks.py`.
```

`test_precommit_checks.py:349-351` →

```
    """The two guards' token and path patterns must stay equal — this class pins that.
    (How the two divide the work is the *Local enforcement* row of
    `document-harness/README.md` — not restated here; why they must stay equal is below,
    being this class's own subject.)
```

### `O-1` (observation, `HD-41` ①, `E3`) — the fix answers `B-1` with a wider keyword list, which is still narrower than the sentence it supports

`B-1`'s second half was that the evidence could not falsify the assertion, not only that the
assertion was false. The repair extends the grep from five phrasings to seven — the two the FULL
happened to quote. The sentence at `README.md:36` still quantifies over *the guards' and their
tests' docstrings*, and a seven-string grep still cannot reach an eighth phrasing. The claim is
true today; I established that by enumerating the corpus (§4.4), which the round did not do. The
scope-covering command is cheap — 22 docstrings, one `ast` walk — and is the one `HD-41` ① asks
for. Related, and not filed separately: `HD-41` ④ asks for the grep **output** in the commit body,
and the body gives a prose enumeration of the five hit locations instead; the candidate did the
same and the FULL passed it, so this is a standing practice question rather than this fix's defect.

### `O-2` (observation, `R7`) — the approval this fix rests on is not visible in the repository

The fix body dates the user approval 2026-08-21 and declares its scope. Neither the approval nor an
`E11` preview card for `INIT-SURFACE` exists in the repository; `CONSTRUCTION-LEDGER.md` already
carries the missing-card ceiling as an open item. I state the ceiling and move on. What I *can*
check I did: every changed path traces to `B-1`, `L-2`, `O-3` or `O-4`, and nothing else moved
(§3).

### `O-3` (observation) — the FULL's `L-1` is still chat-only at this tip

`v3-review-full-7f6e7f0.md` `L-1` filed the `--into` disposition (*root placement is a default not
a requirement; `init` takes no placement option; relocation is the caller's move*) as load-bearing
material living only in a commit body. At `84dea06` that is unchanged: `HD-47` still reads
`status: live` with its flip condition unmet, and `HD-50` still reads *R4 未开*. The candidate body
declared the closeout as the channel, which is correct and still pending. Recorded so the closeout
has a reviewer-visible predicate; not this VERIFY's to close.

### `O-4` (observation, the `B-1` class) — one overlap statement survives in `candidate_path_check.py`, deliberately without a number

`candidate_path_check.py:14-18` states that this lint also scans instruction-layer members and
refuses to write the count, handing the reader a computation instead. The home row states the same
overlap in its own words (*the two overlap on the members this lint also scans*). Under a literal
reading of the single-home ruling this is a second phrasing of a homed relationship; under the
ruling's purpose it is not, because the drift surface a duplicate creates is a **fact that can go
stale**, and this passage exists precisely to refuse to write one — its own history (*"six" until
`ORCHESTRATION.md` became the tenth member*) is why. The FULL did not name it and I do not treat it
as unfinished work. Recorded so the next touch of that docstring decides deliberately rather than
by omission.

### `O-5` (observation, `R1` / `E1`) — this VERIFY is not structurally independent

`7f6e7f0` discloses that orchestrator and executor are one work-side session this round. That seat
also dispatched, prompted and scoped this VERIFY and will commit this record, so all four of `R1`'s
holdings sit with the work side. I ran fresh-context and re-derived the subject, the round, the
budget, the leg and every figure above from the repository rather than from the dispatch — under
`R1` that is a discipline kept, not structural independence, and I do not claim otherwise. The
round's disclosure is present and correctly worded; this extends it to the VERIFY.

## 6. Coverage disclosure (`R4`)

**Read in full:** `document-harness/CONSTRUCTION-CHECKLIST.md` (`wc -l` 235, both sides);
`migration/…/v3-harness-review-contract.md`; `v3-review-full-7f6e7f0.md` (`wc -l` 440, entire);
the complete diff of all 6 repaired paths at `-U6`; the 22-docstring corpus of §4.4;
`tooling/tests/document_harness/test_sweep_refs.py`; `tooling/hooks/layer_path_check.py`
(docstring, `LAYER`, `unresolved_tokens`); `document-harness/README.md:24-38`;
`document-harness/ONBOARDING.md:1-12` and `:68-74`; `.githooks/pre-commit`; the six commit bodies.

**Read by section, not in full:** `HARNESS-DECISIONS.md` — `HD-41`, `HD-47`, `HD-49`, `HD-50` in
`§live`; no blob claimed. `tooling/rsclib/document_harness/paths.py:1-60` and `:160-185`;
`tooling/tests/document_harness/test_precommit_checks.py:243-260` and `:345-375`;
`tooling/sweep_refs.py:1-30` and `resolves()`; `CONSTRUCTION-LEDGER.md` — not read this round,
cited only through the FULL.

**Only probed:** the 748-test battery beyond `test_sweep_refs.py` — executed, not read. The four
pre-fix commits' contents, already the FULL's subject; I re-derived their order, kinds, trailers
and the frozen-tree digest at the range base, and took the FULL's per-commit analysis of them as
recorded rather than re-running it. Every file outside the repair, confirmed unchanged by
`--name-status` rather than by reading.

**Re-executed rather than accepted:** both batteries; `sweep_refs.py` at the tip and its `sha256`;
the seven-keyword class sweep at repository scope; the docstring-corpus enumeration; the
`of the wiring` residual sweep; the home-row word probe of §5; the base/candidate/tip frozen-tree
digests; both guards replayed over the repair's added lines; one mutation of `sweep_refs.py` with
`sha256`-checked restore and a clean-worktree check after; trailers, branch containment, remote
state and the freeze marker.

**`UNVERIFIABLE`, not folded into supported:**

- The 2026-08-21 user approval and its scope, and the `E11` card (`O-2`). `R7`: ceiling stated.
- That the fixing session ran fresh-context, and that the FULL's record was committed unchanged
  from what the reviewer wrote. Process claims, marked.
- Whether the six paths were staged explicitly rather than with `add -A`, and whether `84dea06` is
  a new commit rather than an amend. Not observable after the fact.
- The fix body's `44.5s` / `68.0s` battery wall clocks. The counts I verified; a wall clock from a
  run I did not witness I cannot.
- Whether `paths.py:55`'s surviving *Mirrors … kept identical by hand* is the constant's own
  subject or a residual relationship statement. A reading, not a measurement. I accept it as
  subject; `L-1` does not turn on it, and the bytes it offers leave that clause standing either
  way.
- Mutation proves the `O-4` control binds; it does not prove the module's force sufficient. This
  VERIFY is not a re-certification (`R4`).

## 7. Already on the books, not re-filed

- The `E2`-frozen five `PATHTOK` sites — rider `frozen-path-prefix`, `HD-20`. Reproduced in §4.2.
- `layer_path_check`'s blindness to placeholder-bearing and line-split tokens — stated in `E10`,
  in the guard's docstring, and in `v3-checkpoint-read-bba6f94.md` `O-2`.
- This repository running only one of the three guards — the FULL's `O-6`, rider
  `self-caller-guards`, and `.githooks/pre-commit`'s own comment. §4.8 re-measures the consequence
  for this repair: four of its six paths are unscannable by construction.
- The `E10` design-test-versus-must-fix routing gap — the re-read's `O-1`, homed in `HD-36`.
- `HD-49` carrying `status: implemented` inside `§live` — the cold read's `O-1`.

## 8. Why `REVIEWED_NO_BLOCKER`

The one blocker is closed at every site it named and across the class its sentence quantifies over,
verified by enumeration rather than by the round's grep. The three approved riders landed, one of
them everywhere its phrase occurred. The repair's only executable change binds under mutation. The
frozen surface, the member set, the batteries and the sweep are unchanged. `L-1` is a wording-level
residue of the repair with its bytes supplied, and a VERIFY carries no verdict that would spend a
leg on it (`R3`) — it routes by `R10` like any other finding of its tier.
