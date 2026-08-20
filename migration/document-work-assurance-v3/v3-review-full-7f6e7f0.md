# FULL review — round `INIT-SURFACE` at `7f6e7f0`

**Verdict: `CHANGES_REQUIRED`.** 1 blocker, 2 low, 6 observations.

The blocker is in the round's own headline deliverable: the `README.md` *Local enforcement* row
now declares itself the single home of the two path guards' division of labour and asserts, in
the same breath, that the guards' and their tests' docstrings no longer restate that
relationship. Three live sites still do, and one of them is the sentence immediately after the
pointer that says it does not. The class sweep the commit body pastes cannot falsify that
assertion — its five keywords do not appear at any of the three sites — which is the `HD-41` ①
shape (absolute quantifier, narrower command) and the `E3` shape (a factual assertion written
into instruction text without running the command that could falsify it).

Everything else in the round holds up under re-execution. Both records' bytes, both batteries,
the sweep tally, the class sweep, the frozen surface, the member blobs, the guard replays and
ten mutations of the new test module were re-run here rather than accepted.

---

## 1. Subject, round and budget — re-derived, nothing taken from the dispatch

```
$ git rev-parse HEAD
7f6e7f091e07a64bf2cf9dd6c97842330924362d
$ git branch --show-current
main
$ git status --porcelain
(empty)
$ git rev-list --left-right --count origin/main...HEAD
0	60
```

HEAD is the subject tip, the tree is clean, and the branch is 60 commits ahead of `origin/main`
— unpushed, as `E8` requires. The four commits in range, oldest first:

| commit | title | kind (named in its own body) |
|---|---|---|
| `32f24b8` | `V3-REVIEW-RECORD-INIT-SURFACE-17ce3ed-v1` | record — opening cold read of the layer |
| `bba6f94` | `V3-INIT-SURFACE-AMEND-M1-v1` | amendment — answers the cold read's `M-1` |
| `a4b5565` | `V3-REVIEW-RECORD-INIT-SURFACE-bba6f94-v1` | record — the independent re-read of that amendment |
| `7f6e7f0` | `V3-INIT-SURFACE-v1` | candidate |

**Round.** `INIT-SURFACE`, batch `DTW-INDEPENDENCE` **R4**, chartered by `HD-50` in
`HARNESS-DECISIONS.md` `§live`: *"**R4** `dtw init` 命令面（`--into` 与「树里那半接线可进 init、
机器那半不进」的判据）＋分工收拢（…rider `guard-division-home`）"*. `CONSTRUCTION-LEDGER.md`'s
queue-head block names the same thing as *"下一队首 = R4"*, R1–R3 CLOSED.

**Budget** (`E9`). One FULL, at most one user-approved fix, one targeted VERIFY. No valid
independent FULL had occurred at dispatch, so **this is the round's one FULL** and nothing before
it consumed a leg: the cold read and the amendment+re-read pair are `E10` machinery and spend
nothing. The `E9` ordering clause holds — the branch took no commit between each dispatch and its
record, and the amendment sits between the two records rather than inside either window:

```
$ git log --format='%h %ad %s' --date=format:'%H:%M:%S' 17ce3ed..7f6e7f0 --reverse
32f24b8 22:51:29 V3-REVIEW-RECORD-INIT-SURFACE-17ce3ed-v1
bba6f94 22:52:39 V3-INIT-SURFACE-AMEND-M1-v1
a4b5565 23:05:33 V3-REVIEW-RECORD-INIT-SURFACE-bba6f94-v1
7f6e7f0 23:37:38 V3-INIT-SURFACE-v1
```

`.harness/review-pending.json` exists and names this subject, dispatched `2026-08-20T13:38:01+00:00`
— one minute after the candidate. Left in place.

**Trailers:** `git log --format='%(trailers)'` returns empty for all four (`E8`).

## 2. Changed paths, classified by hand

```
$ git diff --name-status 17ce3ed..7f6e7f0
M	HARNESS-RIDERS.md                                           rider bank — one row deleted
M	document-harness/EXECUTION.md                               E10 member
M	document-harness/ONBOARDING.md                              not a member (its own header says so)
M	document-harness/README.md                                  E10 member
M	document-harness/REVIEW.md                                  E10 member (amendment only)
A	migration/…/v3-checkpoint-read-bba6f94.md                   record
A	migration/…/v3-cold-read-17ce3ed.md                         record
M	tooling/hooks/candidate_path_check.py                       docstring only
M	tooling/rsclib/document_harness/paths.py                    docstring only
M	tooling/tests/document_harness/test_precommit_checks.py     class docstring only
A	tooling/tests/document_harness/test_sweep_refs.py           new tests
$ git diff --shortstat 17ce3ed..7f6e7f0
 11 files changed, 1194 insertions(+), 38 deletions(-)
```

The three `.py` edits under `tooling/` are inside triple-quoted docstrings in every hunk; **no
executable line changed anywhere in the range**, and the only new code is a test module. The
candidate itself touches 8 files, matching its body.

**`E2`'s freeze surface is untouched**, by tree comparison rather than by inspection of the diff:

```
$ for c in 17ce3ed 7f6e7f0; do git ls-tree -r $c -- contract/ schema/document-assurance-v3/ | md5sum; done
f7e2901936585e0dfb736320d21b4ea1  -
f7e2901936585e0dfb736320d21b4ea1  -
$ git ls-tree -r 7f6e7f0 -- schema/document-assurance-v3/ | wc -l
15
```

**`E10`-sync is correctly not triggered**: `CONSTRUCTION-CHECKLIST.md` is absent from the range,
`layer_path_check.LAYER` is unchanged, and `test_precommit_checks.py`'s edit is in `CandidatePath`,
not `LayerMembership.EXPECTED`.

## 3. Re-executed, not accepted

### 3.1 The two batteries

```
$ python tooling/tests/document_harness/run_tests.py
Ran 288 tests in 41.729s
OK
$ python tooling/tests/document_harness_review/run_tests.py
Ran 460 tests in 64.610s
OK
```

288 + 460 = **748**, the figure the commit body claims, and 288 − 279 = the 9 new tests.

### 3.2 The sweep tally

```
$ python tooling/sweep_refs.py .
NAMETOK document-harness/EXECUTION.md:186  audit-rounds.md
… (10 NAMETOK in EXECUTION.md, 2 in REVIEW.md) …
PATHTOK contract/…-supersession-1.md:7    ResearchSystem/migration/document-work-assurance-v3/W2/W2-design.md
PATHTOK contract/…-supersession-1.md:123  ResearchSystem/migration/document-work-assurance-v3/W2/W2-record.md
PATHTOK contract/…-supersession-2.md:60   assurance/runs/
PATHTOK contract/…-supersession-2.md:99   templates/run-v2/
PATHTOK contract/…-supersession-2.md:110  ResearchSystem/migration/document-work-assurance-v3/
-- 17 caller-held or unresolvable references over 10 members
```

17 = 12 NAMETOK + 5 PATHTOK, exactly as reported, and all 5 PATHTOK sit inside the `E2`-frozen
supersessions (rider `frozen-path-prefix`, banked under `HD-20`). **Zero introduced by this
round**, checked rather than assumed: `REVIEW.md:133`'s `` `review-verify.json` `` is pre-existing
(`git show 17ce3ed:document-harness/REVIEW.md | sed -n '133p'` is byte-identical), and the
amendment's replacement text carries only placeholder-bearing and non-path tokens, which no
pattern here matches.

### 3.3 The class sweep of the ruled item

Re-run over the round's own declared scope (the 11 live sites), verbatim keywords:

```
$ grep -rniE "never scans|partition of the tree|division of territory|division of labour|divide the work" <the 11>
document-harness/README.md:36                       (the declared home)
tooling/hooks/candidate_path_check.py:8             (pointer)
tooling/rsclib/document_harness/paths.py:18         (pointer)
tooling/tests/document_harness/test_precommit_checks.py:251  (pointer)
```

Exactly 4 lines, as claimed. **The sweep reproduces; what it cannot do is support the sentence
the round built on it — see `B-1`.**

### 3.4 The `M-1` bytes

sha256 of the fenced replacement block in `v3-cold-read-17ce3ed.md` versus the landed
`REVIEW.md:134-138`:

```
supplied sha256: 8dcd01b818d27955d013c84695480745ca558283403810ed434bdba5e9c0f616
landed   sha256: 8dcd01b818d27955d013c84695480745ca558283403810ed434bdba5e9c0f616
identical: True
```

The `L-1` bytes likewise: `` `tooling/tests/` `` → `the caller's own tests tree`, applied at
`EXECUTION.md:193-194` with no token left. Routing checked against `R10`'s order — `L-1` is tiered
wording-level, so `R9` takes it before the `E10` free channel is reached, and `HD-38`'s
own-commit rule (which binds the free channel, and forbids riding a **must-fix amendment**) is
not engaged. The re-read record independently reached the same conclusion and kept `L-1` out of
`bba6f94`. Correct on both legs.

### 3.5 Member blobs and the citation for members 8–10

`git ls-tree -r 17ce3ed` over the ten members returns exactly the ten blob ids the cold read's §2
table records. Its citation of `v3-cold-read-4410899.md` for members 5, 8, 9 and 10 was checked
at the source: that record's §2 lists `80f42658`, `68031fa2`, `e1a2f26b`, `09aa8699` and its §5
line 421 reads *"Read in full at the subject blobs: all ten members"*. The `E10` citation
condition (unchanged blob since a recorded end-to-end read that states the blob id) is met.

### 3.6 Both guards replayed over every commit in the range

Added lines extracted per commit with the guard's own `-M -U0` parser, then fed to
`layer_path_check.unresolved_tokens` and `paths.unresolved_path_tokens`:

```
32f24b8  CAND  v3-cold-read-17ce3ed.md          8 unresolved tokens
bba6f94  LAYER document-harness/REVIEW.md       OK      CAND  OK
a4b5565  CAND  v3-checkpoint-read-bba6f94.md    1 unresolved token
7f6e7f0  LAYER README.md OK · EXECUTION.md OK   CAND  README.md OK · EXECUTION.md OK · ONBOARDING.md OK
```

The layer guard is clean on every added line the range writes into a member. The two record
commits would be blocked by the candidate lint if this repository ran it — it does not (`O-6`).

### 3.7 The divergence claim the README row makes, re-measured at the tip

```
see `hooks/layer_path_check.py` here      layer->BLOCKED  candidate->()
see `no/such/file.md` here                layer->BLOCKED  candidate->('no/such/file.md',)
see `document-harness/README.md` here     layer->ok       candidate->()
[p for p in layer_path_check.LAYER if candidate_path_check.scanned(p)] -> 9
```

*"the two overlap on the members this lint also scans, and there they still differ on shorthand:
a unique tracked suffix passes this lint and not that one"* — reproduced at this tree, overlap 9.
The row's factual core is sound; the blocker is in the sentence added beside it.

### 3.8 Mutation of the new test module (`R8`, `E4` shape)

`tooling/sweep_refs.py` copied to a scratchpad with `sha256 7996057d…`, ten behaviours neutered
one at a time, `test_sweep_refs` run against each, restored from the checked copy each time:

| mutation | result |
|---|---|
| root-escape guard dropped (`is_relative_to`) | RED |
| runtime-marker (`.harness/`) branch dropped | RED |
| member-relative resolution base dropped | RED |
| `tracked_basenames` stops asking the index | RED |
| NAMETOK never reported | RED |
| LINK never reported | RED |
| PATHTOK never reported | RED |
| MISSING member silently skipped | RED |
| sweep exits non-zero on hits (becomes a guard) | RED |
| placeholder blindness removed (`PATHLIKE` admits `<>`) | RED |

**10/10 bind.** Final `sha256 7996057ddf4522d7b1581b61965bf752f949c117d9c122225f014aaf347a9d22`
— identical to the pre-mutation copy; `git status --porcelain` empty afterwards. Mutation proves
these tests have binding force, not that the force is sufficient (`R4`).

## 4. Findings

### `B-1` (blocker) — the single-home row asserts a state of the docstrings that three of them do not have, and the round's own sweep cannot falsify the assertion

**Location.** `document-harness/README.md:36` (`E10` member), the sentence this round added:

> **This row is the single home of the two path guards' division of labour** (ruled 2026-08-20):
> the guards' and their tests' docstrings name their own subject and point here instead of
> restating the relationship — …

**Ground truth violated.** Three live sites restate the relationship, all inside the round's own
declared 11-site sweep scope:

1. `tooling/hooks/candidate_path_check.py:12-13` — *"…and `rsclib.document_harness.paths` holds
   the whole decision; **the two hooks keep separate rules on purpose and share no verdict**."*
   This clause is in the commit's **added** lines: it was re-typed into the new pointer paragraph,
   four lines after that paragraph's own *"this docstring does not restate it"*. The fact it
   carries — that the two guards' verdicts are separate — is the same fact the README row now
   homes (*"they still differ on shorthand: a unique tracked suffix passes this lint and not that
   one"*), phrased differently. A second phrasing of a homed fact is exactly the drift surface the
   ruling removes.
2. `tooling/rsclib/document_harness/paths.py:55` — *"Mirrors `layer_path_check.PATHLIKE`; kept
   identical so **the two guards agree on what a path is**."*
3. `tooling/tests/document_harness/test_precommit_checks.py:349` (`OneNotionOfAPath` docstring) —
   *"**The two guards disagree on verdicts by design**, and must agree on what a path IS."* A
   test's docstring, which the README sentence quantifies over by name.

Sites 2 and 3 fall outside the rider row's five named sites but inside the scope the commit body
declares, and both are relationship statements about the pair.

**Why the evidence does not reach.** The commit body's `HD-41` ④ sweep uses five keyword strings
(`never scans|partition of the tree|division of territory|division of labour|divide the work`).
None occurs at any of the three sites, so the grep returns 4 and cannot see them. `HD-41` ①/②
require an absolute quantifier to carry a scope the command covers; the README sentence quantifies
over *"the guards' and their tests' docstrings"* while the command covers five phrasings.
`E3` requires that a factual assertion written into instruction text first run the command that
could falsify it — this one has not been run, and the assertion is false as written.

**Downstream decision that goes wrong** (this is why it is a blocker and not `R9` wording-level):
the next change to the division of labour will update the declared home and leave three unguarded
restatements behind, because the layer says there are none. That is precisely the shape `O-5` of
`v3-review-verify-2538893.md` measured across three consecutive fix legs, and the shape this
round exists to end. The commit body's own claim — *"replaced by pointer sentences carrying no
relationship facts"* — is falsified at site 1.

**Minimum fix** (text changing, not a rule and not a guard, per `E6`):

- Delete `; the two hooks keep separate rules on purpose and share no verdict` from
  `candidate_path_check.py:12-13`, leaving the pointer paragraph with local subject only.
- Bound the README sentence to what the sweep covers — name the sites brought to the pointer form
  rather than quantifying over all docstrings — **or** extend the pointer treatment to
  `paths.py:55` and `test_precommit_checks.py:349`. Either closes it; asserting them away does not.

### `L-1` (low) — the `--into` disposition is a load-bearing ruling with no repository carrier but this round's own commit body

`HD-50` R4 names two items for this round: *"`dtw init` 命令面（**`--into`** 与「树里那半接线可进
init、机器那半不进」的判据）＋分工收拢"*. The **criterion** half is in the repository already —
`HD-50`'s own text states it, and this round wrote it into `README.md:30`. The **`--into`** half's
answer is not: *"the two instance files' root placement is a default not a requirement, `init`
takes no placement option and relocation is the caller's move"* exists only in `7f6e7f0`'s body
and in the new README sentence that reports the outcome. `HD-47` still carries `status: live`
with its flip condition unmet, and `HD-50` still reads *"R4 未开"*.

`R2` makes chat-only load-bearing material a finding, and `HD-1`'s admission test (does it bind
the next round and after? does it answer an open batch item?) is met on both counts. The
precedent is `HD-47`'s own basis line, which records FULL `v3-review-full-2026a14.md` `L-3`
flagging exactly this shape — a ruling alive only in a commit body while signed text says
otherwise.

The commit body declares this *"recorded at closeout"*, which is the right channel. Filed so the
declaration is not the only place it exists, and so the `HD-47` flip has a reviewer-visible
predicate. Verified as implemented: `init_target.py` exposes only `--repo-root`
(`cli.py:577`), so the README's *"init takes no placement option"* is true of the code today.

### `L-2` (low; wording-level under `R9`) — the criterion says "of the wiring" and is invoked to govern all nine items

`README.md:30` opens the criterion *"of the wiring, the tree half … may enter `init`"*, while
`ONBOARDING.md:74`'s new pointer invokes it as *"Which of these **nine items** `init` may absorb
at all is bounded by the criterion…"*. In `ONBOARDING.md`, *Hook wiring* is item 9's own heading,
so a reader arriving by that pointer can read the criterion as addressed to one of the nine while
being told it bounds all nine. The parentheticals resolve it — *which revision to pin* is item 1,
*what the policy file says* is item 7, *when the first journal is written* is item 5 — so the
general reading is recoverable from the sentence itself.

Per `R9` I can name no downstream decision that certainly goes wrong: `init`'s behaviour is fixed
and the criterion's outcome is recorded either way. It therefore **rides the next batch touching
this layer** and spawns no round and no read. Bytes, if wanted: `of the wiring` → `of the
onboarding work`.

### `O-1` (observation, `R1`/`E1`) — this FULL is not structurally independent

`7f6e7f0`'s body discloses that orchestrator and executor are one work-side session this round.
That seat also dispatched, prompted and scoped this review and will commit its record, so all
four of `R1`'s holdings sit with the work side. I ran fresh-context and derived the subject, the
round, the budget, the member set and every figure above from the repository rather than from the
dispatch — but under `R1` that is a discipline kept, not structural independence, and I do not
claim otherwise. The round's disclosure is present and correctly worded; this records that it
extends to the FULL as well as to the two reads.

### `O-2` (observation, `R5`/`E6`) — the settlement of `O-4` chose 152 lines of tests over writing the cross-check down

`v3-review-full-39a21a8.md` `O-4` diagnosed `sweep_refs.py` as *"a diagnostic whose output is
banked as a round's evidence"* whose *"cross-check exists and simply is not written down"*, and
named `E6` as arguing against building machinery around a thing that decides nothing. The round
answered with a 152-line test module. The tests do bind (§3.8, 10/10) and they make the banked
17-hit tally trustworthy, which is real value; the finding's own minimum answer was narrower.
Whether it should exist at this size is a `R5` question and the user's, not mine.

### `O-3` (observation) — `test_sweep_refs.py`'s docstring overclaims its negative-control shape

*"Every must-report case is paired with a clean baseline asserted in the same test (`E4`'s
negative-control shape, applied to a reporter)."* The MISSING-member case
(`test_a_missing_member_is_reported_and_exit_stays_zero`) has no present-member baseline in its
own test; the clean layer is asserted in a separate test. The three reference forms do carry
same-test controls, so the claim holds for them and not for the fourth reported class.

### `O-4` (observation) — a dead no-op in a new negative control

`test_sweep_refs.py:118`: `self.assertNotIn("target.md", out.replace("phantom.md", ""))`. The
replacement removes a string that does not contain `target.md`, so it changes nothing the
assertion sees. The control is sound without it; the `.replace` reads as guarding against
something it cannot guard against.

### `O-5` (observation, `R7`) — `E11`'s preview card still has no carrier

No preview card for `INIT-SURFACE` exists in the repository, and neither does the user approval
the two 2026-08-20 rulings rest on. `CONSTRUCTION-LEDGER.md` already carries this as an open item
(*"`E11` 预览卡在仓内无承载"*). I state the ceiling and move on; nothing in the round's changed
files traces to anything outside `HD-50` R4 and the two reads' findings, which is the scope check
I can perform.

### `O-6` (observation) — this repository's own records are work products to the candidate lint

Replaying `candidate_path_check` over the range (§3.6), the two record commits carry 8 and 1
unresolved tokens and would be blocked: `RECORD_SURFACE` still names `ResearchSystem/`-prefixed
paths, which round `DE-PREFIX` removed here. Nothing fired, because `.githooks/pre-commit` in this
repository runs `layer_path_check` alone — the gap rider `self-caller-guards` banks.
`candidate_path_check.py`'s docstring states this exactly. Recorded here because this round makes
`README.md:36` the **single home** of what each guard covers, and that row states the record
exemption as a general rule (*"a record quotes the broken path it reports … so neither is
scanned"*) without the qualification that on this repository it exempts nothing.

## 5. Coverage disclosure (`R4`)

**Read in full:** `document-harness/CONSTRUCTION-CHECKLIST.md` (235 lines, both sides);
`migration/…/v3-harness-review-contract.md`; the complete diff of all 11 changed paths;
`tooling/sweep_refs.py`; `tooling/tests/document_harness/test_sweep_refs.py`;
`tooling/hooks/layer_path_check.py`; `tooling/hooks/candidate_path_check.py`;
`tooling/rsclib/document_harness/paths.py`; `tooling/rsclib/document_harness/init_target.py`;
`.githooks/pre-commit`; `document-harness/ONBOARDING.md`; `CONSTRUCTION-LEDGER.md`; the four
commit bodies.

**Read by section, not in full:** `HARNESS-DECISIONS.md` — header and `§live` entire (`:1-196`),
plus `HD-46`/`HD-38`/`HD-37`/`HD-32` in `§implemented`; no blob claimed, per `E10`'s tail.
`document-harness/README.md` `:27-38`; `document-harness/REVIEW.md` `:125-146`;
`document-harness/EXECUTION.md` `:186-200`; `HARNESS-RIDERS.md` (the deleted row plus grep hits);
`tooling/tests/document_harness/test_precommit_checks.py` `:240-370`;
`tooling/rsclib/document_harness/cli.py` (the `init` wiring only).

**Records in the subject, read partially:** `v3-cold-read-17ce3ed.md` — §1 heading map, §2 entire,
§3.3, and `M-1`/`L-1` in full; **not its 524 lines entire**.
`v3-checkpoint-read-bba6f94.md` — heading map, §4 and §5 in full; **not its 490 lines entire**.
`v3-review-verify-2538893.md` `O-5` and §8; `v3-review-full-39a21a8.md` `O-4`;
`v3-cold-read-4410899.md` `:86-93` and `:419-423`.

**Only probed:** the 748-test battery beyond `test_sweep_refs.py` — executed, not read; every file
outside the range, confirmed unchanged by `diff --name-status` rather than by reading.

**Re-executed rather than accepted:** both batteries; `sweep_refs.py` at the tip; the 11-site
class sweep; the sha256 comparison of the `M-1` bytes; the base-versus-tip frozen-tree digest; the
ten-member `ls-tree` blob table at `17ce3ed`; the cited record's §2/§5 lines; both guards replayed
over all four commits' added lines; the two-guard divergence probe with its three-shape control;
the overlap count; ten mutations of `sweep_refs.py` with sha256-checked restores; trailers, branch
containment and remote state.

**`UNVERIFIABLE`, not folded into supported:**

- The user approval of 2026-08-20 behind both ruled items, and the `E11` card (`O-5`, `L-1`).
  `HD-50` records the batch, not these two answers. `R7`: ceiling stated.
- That the executing session ran fresh-context, and that the two records were committed unchanged.
  Process claims, marked.
- Whether the 8 files were staged as explicit paths rather than `add -A`. Not observable.
- The commit body's `43.7s` / `68.5s` battery timings. The counts I verified (288 / 460); wall
  clocks from a run I did not witness I cannot.
- Mutation proves the new tests bind; it does not prove the force sufficient. `O-3` names one
  reported class whose negative control is weaker than the module claims.
- Whether `paths.py:55` and `test_precommit_checks.py:349` are *the division of labour* or *the
  path-shape agreement* is a reading, not a measurement. `B-1` does not turn on it: site 1 alone
  falsifies the sentence, and the fix admits either answer.

## 6. Already on the books, not re-filed

- The `E2`-frozen five PATHTOK sites — rider `frozen-path-prefix`, `HD-20`. Reproduced in §3.2.
- `layer_path_check`'s blindness to placeholder-bearing and line-split tokens — stated in `E10`,
  in the guard's docstring, and in `v3-checkpoint-read-bba6f94.md` `O-2`.
- `HD-49` carrying `status: implemented` inside `§live` — the cold read's `O-1`, unchanged here.
- The `E10` design-test-versus-must-fix routing gap — the re-read's `O-1`, homed in `HD-36`'s
  status note.
- Rider `guard-division-home` was redeemed correctly: the fix and the row's deletion are in the
  same commit (`R10`), and the row named a round-eligible surface (`HD-37` ②).

## 7. Why `CHANGES_REQUIRED`

The round's second ruled item is a claim about the state of the tree, written into an `E10`
member. The claim is false at three sites, one of which the same commit wrote, and the evidence
offered for it is a grep whose keywords cannot reach any of them. That is `E3` and `HD-41` ① at
the one place this round was chartered to make drift-proof, and the failure mode it inherits —
a guard-relationship sentence falsified by the leg that touches it — is now on its fourth
consecutive occurrence. The fix is small, is text changing rather than machinery, and does not
disturb the round's first ruled item, its riding accounts, or its tests.
