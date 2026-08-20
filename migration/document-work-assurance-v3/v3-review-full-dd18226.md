# FULL review — round `XREPO-REFS`, subject `69fc082..dd18226`

Independent review session. Standing instruction:
`ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` (`R1`–`R10` review side, `E1`–`E12`
execution side — one file carrying both, reached through the two retired-contract stubs the
dispatch named). Verdict in §8.

## 0. Dispatch as received, and what I refused to take from it

The dispatch handed me one range and one sentence of role. It also told me — correctly — that
round, budget, authorization, obligations and every number are mine to re-derive. I did. Nothing
below rests on a figure the round reported; where I quote one it is to compare it against my own.

The freeze marker confirms the subject and nothing else:

```
$ cat .harness/review-pending.json
{
 "subject": "69fc0827c445b64bec99d7b8a5745eba1784f2d9..dd1822655e3c84f06031b8fe255c369e9785ca0c",
 "dispatched_at": "2026-08-19T15:52:30+00:00"
}
```

## 1. Subject, re-derived

```
$ git rev-list --count 69fc082..dd18226
5

$ git log --oneline 69fc082..dd18226
dd18226 V3-XREPO-REFS-v1
c53fc4e V3-REVIEW-RECORD-XREPO-REFS-48b6c5f-v1
48b6c5f V3-XREPO-REFS-AMEND-M1-v1
1cb80bb V3-XREPO-REFS-FREE-L1-v1
d8a83b3 V3-REVIEW-RECORD-XREPO-REFS-69fc082-v1

$ git diff --stat 69fc082 dd18226
 ResearchSystem/HARNESS-RIDERS.md                          |   3 -
 ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md |  20 +-
 ResearchSystem/document-harness/EXECUTION.md              |  36 +-
 ResearchSystem/document-harness/README.md                 |   2 +-
 ResearchSystem/document-harness/REVIEW.md                 |   9 +-
 .../document-harness/journal/xrepo-refs-2026-08-20.md     | 238 +++++++
 .../v3-checkpoint-read-48b6c5f.md                         | 351 +++++++++++
 .../v3-cold-read-69fc082.md                               | 423 +++++++++++++
 8 files changed, 1055 insertions(+), 27 deletions(-)

$ git status --porcelain
(no output)

$ git log --oneline --all --decorate -1
dd18226 (HEAD -> main) V3-XREPO-REFS-v1
```

**Classified by hand.** Instruction-layer members changed: `CONSTRUCTION-CHECKLIST.md` (`E1`,
`E10`, and the amendment's header paragraph), `EXECUTION.md`, `REVIEW.md`, `README.md`. Bank:
`HARNESS-RIDERS.md`. Records: one round journal (new), two read records. No schema, no tooling,
no generated path, no frozen path, no member path added / removed / renamed — the doc-only tier
the round derives is the tier I derive. `HEAD -> main` with no remote-tracking ref: not pushed
(`E8`).

Round identity, budget and authorization, from the repository: the round is `XREPO-REFS`, R2 of
batch DTW-INDEPENDENCE, authorized by `HARNESS-DECISIONS.md` `§live` `HD-50`. No FULL for this
round exists at the subject — the two record commits in the range are `E10` reads, which `R3`
says are not rounds and spend no budget. This is therefore the round's one FULL, its fix leg
unspent.

## 2. What the round claims, checked against what it did

### 2.1 The outbound references are gone — verified with my own sweep, not theirs

I wrote my own enumeration (markdown link targets plus backticked `/`-bearing path-like tokens
over the ten `E10` members, resolved against repo root / the file's own directory / under
`ResearchSystem/`, with a target reachable only by escaping the repo root counted as not
resolving), and ran it at both ends:

```
$ python sweep.py 69fc082
PATHTOK EXECUTION.md:186  ResearchSystem/assurance/runs/p5a-shells/control/audit-rounds.md
PATHTOK EXECUTION.md:340  ExperimentLab/papers/
PATHTOK EXECUTION.md:343  ResearchSystem/tooling/tests/run_tests.py
PATHTOK EXECUTION.md:345  ResearchSystem/tooling/tests/run_p4_tests.py
PATHTOK EXECUTION.md:346  ResearchSystem/tooling/tests/run_p5a_tests.py
PATHTOK EXECUTION.md:347  ResearchSystem/schema/fixtures/validate_fixtures.py
PATHTOK EXECUTION.md:449  ResearchSystem/assurance/runs/p5a-shells/control/audit-rounds.md
PATHTOK EXECUTION.md:452  ResearchSystem/assurance/runs/p4-doc/issues/user-decision-triage-comparator-environment-defects.json
LINK    REVIEW.md:45      ../migration/document-work-assurance-v3/v3-review-full-fef3a2e.md
PATHTOK …supersession-2.md:60  assurance/runs/
PATHTOK …supersession-2.md:99  templates/run-v2/
-- 11 unresolvable references over 10 members at 69fc082

$ python sweep.py dd18226
PATHTOK …supersession-2.md:60  assurance/runs/
PATHTOK …supersession-2.md:99  templates/run-v2/
-- 2 unresolvable references over 10 members at dd18226
```

Both survivors are `E2`-frozen. The `LINK` class is empty at the tip, and every writable member
is clean. **The round's central claim holds under an independently written instrument.**

My 11 and the journal's 20 reconcile exactly: the journal also counts bare `NAMETOK`s (7) and the
two `.harness/review-pending.json` sites (2), which my run resolved because a dispatch marker
exists in the tree right now. 11 + 9 = 20. I take that as corroboration of the journal's sweep
rather than a discrepancy.

The two named review records are genuinely not here, so the demotions state a true holder:

```
$ git ls-files | grep -c "v3-review-full-fef3a2e\|v3-review-full-86defbc"
0

$ ls ExperimentLab
ls: cannot access '…/harness/ExperimentLab': No such file or directory
```

### 2.2 The whole-stock guard scan reproduces

```
$ python -c "<layer_path_check.unresolved_tokens over all ten members at dd18226>"
…supersession-1.md [('schema/document-assurance-v3/review.v2.schema.json', 'resolves only under ResearchSystem/ — prefix missing')]
…supersession-2.md [('schema/', 'resolves only under ResearchSystem/ — prefix missing')]
whole-stock scan complete at dd18226 -- members: 10
```

Two violations, both frozen — exactly what journal §3 reports. The measurement is honest. What it
establishes is narrower than the sentence it is offered in support of; see `B-1`.

### 2.3 The bank arithmetic reproduces

```
$ git show 69fc082:ResearchSystem/HARNESS-RIDERS.md | grep -c "^| "
35
$ grep -c "^| " ResearchSystem/HARNESS-RIDERS.md
32
$ grep -n "layer-crossrepo-token\|layer-outbound-refs\|e1-disclose-home" ResearchSystem/HARNESS-RIDERS.md
(no output)
```

35 − 1 header = 34 data rows at the base; 32 − 1 = 31 at the tip. Three rows, the three named
ones, deleted in the same commit as their fixes (`R10`). The opening read independently counted
34 at the base.

### 2.4 The provenance deletion is safe

```
$ git grep -n "provenance" 69fc082 -- <the ten members>
CONSTRUCTION-CHECKLIST.md:134:  provenance entries are one-line derived facts, no characterization.
README.md:36: … The provenance-entry check that also ran here was deleted 2026-07-28 …
```

One clause, and one narration of the 2026-07-28 deletion. Nothing in `ResearchSystem/tooling/`
mentions provenance at all (`grep -rn` → no output), so no code reads it. The membership sentence
is untouched by the diff, so `E10-sync` does not fall due — I verified that from the hunk headers
rather than from the reported hash.

### 2.5 The battery reproduces

```
$ cd ResearchSystem/tooling && python -m pytest -q
733 passed in 104.83s (0:01:44)
```

Same count as the round reports. Not owed at the doc-only tier; run anyway, as they did.

### 2.6 `E2` untouched, decision log untouched, `ORCHESTRATION.md` untouched

No path in the diff is a frozen blob or a file of the `ResearchSystem/schema/document-assurance-v3/`
pack; `paragraph-map.schema.json` is both a member and frozen and is not in the diff.
`HARNESS-DECISIONS.md` is not in the diff — the `HD-50` state flip is correctly reserved to the
user at closeout. `git diff --name-only 69fc082 dd18226 -- …/ORCHESTRATION.md` returns nothing.

### 2.7 The `E10` pair and the free channel are inside their channels

Commit order in the range puts each record commit immediately after the commit it was dispatched
on, with nothing else between (`E9`'s window). `d8a83b3` and `c53fc4e` each touch exactly one file
— their own record — so the record channel (`R6`) was not used to carry work. The free-channel
byte at `1cb80bb` is its own commit (`HD-38`), on a non-frozen member, and applies content the
opening read's `L-1` named; I checked the applied bytes against the README table and they are
directionally true: row `:27` is *Construction-side rules*, and the ledger row now points at it by
name.

## 3. Blocker

### `B-1` — `E10`'s new clause tells every future executor that `layer_path_check` enforces the caller-held-path rule; measured, the guard is blind to the class's central shape

**Location.** `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md`, `E10`, the clause this
round adds (tip `:141–148`):

> a caller-held path is named, never written as a path token — a member's path tokens resolve in
> this repository, and an artifact living only in a caller is given its name and its holder
> instead, so that a reader following a path in this layer cannot land on another repository's
> bytes **or on nothing**: `layer_path_check` **enforces this** on the lines a commit adds, this
> clause binds the standing text that guard never re-scans, and the bytes `E2` freezes are
> excepted while they are frozen.

**Ground truth it violates.** The guard flags two mechanically decidable shapes and skips
everything else — its own docstring says so: *"Tokens resolvable nowhere at all are skipped — they
may be illustrative."* A caller-held path token that does not begin with `ResearchSystem/` and
does not resolve under it is exactly that skipped class, and it is the ordinary way to write
another repository's path. Reproduced in a throwaway clone of the subject, real defect shape, not
a crash (`R8`):

```
$ git add ResearchSystem/document-harness/EXECUTION.md          # staged added line:
+A caller-held example: `ExperimentLab/papers/` and `assurance/runs/p5a-shells/control/audit-rounds.md` and `.goals/plans/x.plan.md`.
$ python ResearchSystem/tooling/hooks/layer_path_check.py
exit=0   (no output)

POSITIVE CONTROL — the same target, prefix restored:
+Positive control: `ResearchSystem/assurance/runs/p5a-shells/control/audit-rounds.md`.
$ python ResearchSystem/tooling/hooks/layer_path_check.py
exit=1
pre-commit BLOCKED: newly added instruction text names a repository path that does not resolve:
  …EXECUTION.md: `ResearchSystem/assurance/runs/p5a-shells/control/audit-rounds.md` — does not resolve from the repo root
```

Three caller-held tokens on an added line pass silently; the *same* run artifact, written with the
prefix, is blocked. The guard's entire binding force on this class is the accident that the
caller's tree happens to share this repository's top-level directory name. Drop the prefix — which
is what a writer naming another repository's tree does by default — and the check has nothing to
say. The clause's own stated purpose, *"cannot land … on nothing"*, names precisely the branch the
guard declines to implement.

This is not a hypothetical. `ExperimentLab/papers/` at `EXECUTION.md:340` is a member site of that
exact shape, it survived every prior sweep, and the round removed it by hand. The opening read
this round was answering says so in as many words (`v3-cold-read-69fc082.md` `O-1`):
*"`layer_path_check` skips it by design — it neither starts with `ResearchSystem/` nor resolves
under it, so it falls in the may-be-illustrative class."* The fact was in the round's own subject
material and the clause was written against it.

**Why blocker and not low (`R9`).** The fix changes an actor's action. An executor reading `E10`
is told the pre-commit hook covers newly written caller paths; the true state is that it covers
them only when they carry this repository's prefix, and that the rest rests on the clause and a
manual sweep. That is a check outcome and an obligation, not a wording preference, and the
accurate fact is recoverable from no adjacent text — `E10` is where a reader goes to learn what
the layer's path rule is backed by. It also breaks `E3`'s last sentence on the sentence `E3` was
written for: *a factual assertion written into instruction text runs the command that could
falsify it first*. Journal §4's two negative controls exercise the broken-absolute and
missing-prefix branches — the two the guard implements — and never the class the clause defines.

**Minimum fix.** Bound the assertion to what the guard decides; no machinery (`E6`). One
replacement inside the same clause, e.g.: *"`layer_path_check` catches, on the lines a commit
adds, the two shapes it can decide — a `ResearchSystem/`-prefixed token that does not resolve, and
a token that resolves only under that prefix; a caller-held token in neither shape (as
`ExperimentLab/papers/` was) is caught by this clause alone."* That keeps the clause, keeps the
guard, and stops the layer promising cover it does not have. Nothing else in the diff needs to
move.

## 4. Low

### `L-1` — the clause's flat sentence *"a member's path tokens resolve in this repository"* is falsified at rest by two standing member sites, and only the journal rescues them

`README.md:36` and `REVIEW.md:139` both write `` `.harness/review-pending.json` `` — the marker
`dtw dispatch` writes. At rest the target exists at no path of this repository; the directory does,
the file does not. Under the clause's own words those two sites are violations. Under journal §2's
reasoning they are not, because *"the target's home is this repository and it is simply absent at
rest"* — a distinction the clause does not carry and the journal is not a member.

*Downstream decision that goes wrong.* The next round sweeping the layer against `E10` either
"repairs" two correct in-repository references, or re-derives the runtime-marker exception from
scratch, as the retired rider `layer-outbound-refs` and this round's journal each had to. Bytes
are available and add no bound — the exception is a description of existing practice, not a new
rule ("…resolve in this repository, a run-time marker written here counting as resolving"), so
this can ride the fix leg with `B-1` if the user prefers.

### `L-2` — `HD-50` authorizes R2 to teach the guard; the round substituted a text clause, deleted the rider that recorded the gap, and the property the batch ordering rests on is not in the tree

`HD-50`, the only authorization for this round that exists in the repository, enumerates R2 as
*"教 `layer_path_check` 认跨仓（rider `layer-crossrepo-token`）+ B 类断链降名（`REVIEW.md:45`、
`EXECUTION.md:186/:449/:452`，用户裁「降成名字，不做链接」）+ `e1-disclose-home` 落座 + `E10` 结尾
provenance 死从句顺带删"*, and attaches the batch ordering to the first item:
*"**R2 必须先于 R3**：守卫先认跨仓，否则 R3 改 `EXECUTION.md` 按仓枚举句会被刚归位的守卫挡住。"*

The round did items 2, 3 and 4 and replaced item 1 with the `E10` clause, disclosing the
substitution in the candidate body and grounding it in the user's ruling **for the sibling class**
plus `E6`. The guard file is not in the diff. So after this round the guard still does not
recognize cross-repository references, and its missing-prefix branch still fires on the shape R3
is chartered to write (measured: `` `document-harness/EXECUTION.md` `` → *"resolves only under
ResearchSystem/ — prefix missing"*). Whether R3's re-rooting dissolves that is R3's design
question; what is checkable today is that the property `HD-50` names as R2's reason for going
first was not delivered.

Compounding it, `layer-crossrepo-token` — the row whose text records the guard experiment and the
"no bytes, both forks are design" analysis — is deleted in the same commit. If closeout lands as
written, the repository's only remaining statement about the guard's reach is the `E10` sentence
`B-1` shows to be false in the permissive direction.

*Why low.* Whether the guard should still be taught is a should-this-exist question and `R5`
reserves it to the user; the substitution was disclosed, not silent (`E9`). Naming the tiebreak
myself would add the bound. `B-1`'s fix is what keeps the underlying fact recorded either way.
*Deadline (`R10`), if this banks:* the opening of R3, the first round that writes tokens the
guard's second branch judges.

## 5. Observations

- **`O-1` — rider `chk-thin`'s touch condition arrived on this commit and was not redeemed.** Its
  redeem-when is *"下一个 product run 的 FULL …，或下一批碰 `REVIEW.md` 上述两节文本，孰先"*, and
  this commit edits `REVIEW.md:44–47`, inside the named §*What is not in the subject: the run's own
  checkers* (`:24–47`). The candidate body reports it and defers to closeout on the ground that the
  fix is a review-semantics tiebreak outside this round. That is a defensible scope call and the
  disclosure is where `R10` can see it — recorded so closeout does not lose that the row is now in
  the reached-and-unpaid state its own text describes for others.
- **`O-2` — `e1-disclose-home`'s row is deleted while one third of the defect it recorded has no
  home but a commit body.** The row named three gaps: no carrier, no owner, and
  *"`ORCHESTRATION.md` 的九条义务表没有收这一条"*. The first two are fixed in `E1`. The third is
  reported in the candidate body as routed to rider `charter-qualifiers`' surface — but
  `charter-qualifiers` is about cite-only rows dropping a cited rule's qualifiers, not about a
  missing row, so nothing in the bank will carry it once this body scrolls past. Related and
  smaller: the body says `ORCHESTRATION.md:89–91` is *"already pointing at `E1` without restating
  it"*; `:90` does gloss the carrier — *"what a session holding both work-side roles owes **in its
  record**"* — which is the wording `E1` just replaced. Both are closeout's to route.
- **`O-3` — two record-side pointers in the candidate body are off; neither changes a fact
  (`HD-23` shape).** The guard experiment with its two negative controls is journal **§4**, not §3
  as the body cites (§3 is the whole-stock scan, also cited to §3 in the same sentence). And the
  body reports the battery as `733 passed in 103.73s` while the journal's §6 reports the same leg
  as `733 passed in 100.67s`; the count agrees with my own run (`733 passed in 104.83s`), so these
  are two executions and nothing factual is lost. A commit body cannot be edited (`E8`); recorded
  so the trace exists, no action proposed.
- **`O-4` — the sweep instrument is not in the repository.** Journal §2 names `sweep_refs.py` and
  gives its three patterns and its output, which is what `E3` asks for and is enough to re-derive.
  But `git ls-files | grep -i sweep` returns nothing, so the next round re-writes the instrument
  rather than re-running it, and the two sweeps' comparability rests on the patterns being
  transcribed correctly. I re-derived independently and reconciled to the entry (§2.1), so this is
  a note about repeatability, not about this round's numbers.
- **`O-5` — successive rounds are adding text to `E10` faster than they are adding force (`R5`
  shape, reported not concluded).** `E10` is now the layer's longest rule by a wide margin and
  absorbed three distinct duties in the last two rounds (caller-held paths here; the membership /
  amendment / free-channel machinery before). The clause added here is the second in a row whose
  enforcement is asserted rather than demonstrated. Whether the rule should be split, or whether
  the layer wants a guard that matches it, is the user's question; I report only that the shape is
  the one `R5` says to surface.

## 6. Process and boundary check (run second, per `R3`)

| Rule | Finding |
|---|---|
| `E2` frozen bytes | Untouched. No frozen blob and no pack file in the diff. |
| `E3` measure-last | Held for the counts (sweep output, rider counts, battery, hashes all emitted). **Not held** for the one factual assertion the clause makes about the guard — `B-1`. Two pointer slips — `O-3`. |
| `E4` / `E5` new guards | No new guard; not owed. |
| `E6` no new machinery | Held, and deliberately so — the round's stated reason for the text fork. |
| `E8` commit form | Held. One dense title per commit, one paragraph, no trailers, kind named in every body, explicit paths, no amend, no push (`HEAD -> main`, no remote ref). |
| `E9` budget | Held. Two `E10` reads and one free-channel application spend nothing; no prior FULL exists for `XREPO-REFS`; this FULL is the first. Each dispatch window carries only its own record commit. |
| `E10` layer discipline | Amendment + independent re-read pair completed before the round's work began; free-channel byte in its own commit on a non-frozen member; cold read at the opening. The round is correctly classified as design (a clause added, a clause deleted). Content correctness — `B-1`, `L-1`. |
| `E11` preview card | Not visible to me; a caller-side artifact. `UNVERIFIABLE`. |
| `E12` handoff | Held. One range, no per-acceptance argument. |
| `R6` record channel | Held on both record commits — one file each, correct title form. |
| `R10` rider routing | Three rows redeemed with their fixes in the same commit; count reproduces. Two residuals — `O-1`, `O-2`. |
| `HD-50` authorization | One of four enumerated items delivered by substitution — `L-2`. |

## 7. Disclosure — read in full, sampled, only probed (`R4`)

**Read in full** at the tip: `CONSTRUCTION-CHECKLIST.md` (226 lines), `layer_path_check.py` (106),
`journal/xrepo-refs-2026-08-20.md` (238), `document-harness/README.md` (40), both retired-contract
stubs, `HARNESS-DECISIONS.md` header + `§live` (lines 1–195); the complete diff of all five commits
for every changed path; all five commit bodies.

**Sampled:** `v3-cold-read-69fc082.md` and `v3-checkpoint-read-48b6c5f.md` — outlines plus their
findings sections in full, not their §1–§3 derivations; `EXECUTION.md` (469 lines) — the three
changed regions and their surroundings, not end to end; `REVIEW.md` (285) — `:20–50`;
`ORCHESTRATION.md` (95) — `:80–100`; `HARNESS-RIDERS.md` — the three deleted rows via diff, the
`chk-thin` row, and the header.

**Only probed:** the guard's behaviour (throwaway clone, three caller-held tokens + one positive
control), its predicate over the whole standing stock, my own reference sweep at both ends, the
battery, the rider counts, the provenance grep, git refs and worktree state.

**`UNVERIFIABLE`, not folded into supported.**
(a) That the two read records were committed unchanged from what their reviewers wrote — I hold no
independent copy; the record channel's shape (one file per commit) is consistent with it and
proves nothing.
(b) `E1`'s disclosure in the candidate body — *"the executor was a subagent this orchestrator
dispatched, holding none of `R1`'s four holdings"* — is a process claim about a session I cannot
observe. Marked, per `R4`, not verified. It is well-formed against `E1` as amended and does not
call the result structurally independent.
(c) The preview card (`E11`) and any user approval of the substitution in `L-2` beyond `HD-50`.
`R7` applies: I state the ceiling and move on.

**Ceiling on `B-1`.** The clone experiment proves the guard does not bind on the three token shapes
I staged and does bind on the prefixed one. It does not enumerate every shape it misses, and
`R4`'s rule holds: this shows the guard's force is insufficient for the clause, not the full extent
of what escapes it.

## 8. Verdict

**`CHANGES_REQUIRED`.**

One blocker (`B-1`): the instruction layer now asserts a guard coverage that measurement
contradicts, on the exact class this round exists to govern, and the contradicting fact was
already in the read the round was answering. The fix is one bounded replacement inside the clause
the round just wrote — no machinery, no second round of design.

Everything else the round claims, I re-derived and it held: the outbound references are gone under
an independently written sweep, the whole-stock guard scan reproduces, the bank arithmetic
reproduces at both ends, the provenance clause is dead text safe to delete, the battery is green at
the same count, and the frozen surface, the decision log and the orchestrator charter are untouched.
The two lows and five observations are named above; `L-1` supplies bytes and can ride the same fix
leg, `L-2` carries an `R5` half that is the user's alone.
