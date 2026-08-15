# FULL review — `3b7ebe2..838c413` (the E2-verb / E10-pin amendment round)

| | |
|---|---|
| round | FULL, construction-side (`CONSTRUCTION-CHECKLIST.md` R1–R10) |
| subject | `3b7ebe21df45f023504d60ff90c953e4919a6b23..838c4132831a3961997977829959e259deb3d6be` |
| range content | exactly one commit, `838c413` (`V3-E2-VERB-E10-PIN-v1`, kind: candidate) |
| **verdict** | **`REVIEWED_NO_BLOCKER`** |
| findings | 0 blockers, 3 low, 2 observations |
| record | this file; the execution side commits it (`R6`) |

`REVIEWED_NO_BLOCKER` is scope-relative and here it means: the three edits say what they
claim to say, the E10 enumeration is item-for-item equal to the code it was pulled from,
and no member of the instruction layer is left holding a statement the amendment
falsified. That last check is the one the previous amendment round failed as its blocker,
so it was run exhaustively rather than sampled — §2 and §3.

The three lows are not defects in the bytes. They are, in order: an authorization for the
E2 half that exists nowhere I can read; an `E10` obligation this amendment creates and
that nothing in the round's record trail carries; and a sync surface the pin opens whose
prose leg no guard binds — demonstrated by mutation, not argued. Each names the decision
that goes wrong if it stays unfixed, per `R9`.

## 1. Subject, re-derived (`R2`)

I was handed one range and nothing else. Round name, budget, authorization, obligations
and every figure below are re-derived here; no number from the dispatch prompt, the plan,
the ledger or the commit body is accepted as reported.

```
$ git rev-parse HEAD              -> 838c4132831a3961997977829959e259deb3d6be
$ git rev-parse --abbrev-ref HEAD -> document-work-assurance-v3
$ git rev-list --count 838c413..HEAD -> 0
$ git status --porcelain          -> (empty)
$ git rev-list --count 3b7ebe2..838c413 -> 1
$ cat .harness/review-pending.json
  {"kind": "construction-round",
   "subject": "3b7ebe21df45f023504d60ff90c953e4919a6b23..838c4132831a3961997977829959e259deb3d6be",
   "dispatched_at": "2026-08-04T06:00:58+00:00"}
```

The subject tip is HEAD; the branch has taken no commit since dispatch, so `E9`'s window is
intact and this record is the only commit it admits. The marker file is untracked
(`git ls-files --error-unmatch` → no match; `git check-ignore -v` → `.gitignore:19`
`.harness/`), so its written tip SHA costs no commit inside the round and `E12`'s
"base written, tip `HEAD`" clause — whose stated reason is that a recorded range is short
by the commit that records it — is not engaged by it.

Changed paths, classified by hand, one line of `git diff --numstat`:

| path | +/− | class |
|---|---|---|
| `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` | 19 / 10 | instruction layer, member 1 |

One file, and the round's declared boundary in `.goals/plans/e2-verb-e10-pin.plan.md`
("只改 `CONSTRUCTION-CHECKLIST.md`，三处。其余一个字节不动") is met exactly. Blob
`2108635f` → `4d0c7330`, 164 → 173 lines, both re-derived. `git diff --word-diff` returns
three edit sites and no fourth token anywhere in the range.

**Round and budget, derived.** `HARNESS-LEDGER.md` names this round in advance —
"下一轮已备好（2026-08-04）：构造轮 `E2-VERB-E10-PIN`" — and the plan at `fd71c8e` scopes
it. No `v3-review-full-*` or `v3-review-verify-*` record exists for this round
(`ls` over the record directory), so this FULL is its first independent review and `E9`'s
budget stood untouched before it: one FULL, at most one user-approved fix, one targeted
VERIFY. The commit body's own accounting agrees, and `E9`'s test — has a valid independent
FULL already occurred — answers *no* at the moment the candidate landed, so the candidate
consumes nothing.

## 2. The amendment against the repository (`R3` — implementation first)

**Edit 3 is the one with a checkable referent, so it was checked mechanically.** The
sentence now claims the layer is "exactly these nine paths and nothing else". I parsed the
backticked tokens out of the amended sentence at the subject blob and compared them to the
code, in one script rather than by eye:

```
prose tokens (9)  == tuple(layer_path_check.LAYER) (9)   -> EQUAL ITEM-FOR-ITEM: True
```

Both nine-tuples, same order, same strings. The hand-written second pin,
`test_precommit_checks.py:176` `EXPECTED`, is a third copy and
`test_layer_equals_the_hand_written_membership` asserts it equal to `LAYER`; I read all
three by eye as well as by script. The commit body's "zero code delta" holds: `git diff`
shows no `.py` file in the range, so the prose moved to the code and not the reverse, as
claimed.

**Edit 1 and edit 2 are one change and were checked as one.** E2 now opens "Frozen bytes
are **not written without a recorded user ruling**" and the menu three paragraphs down
gained its third branch, "either take the in-boundary fix and record why, or obtain the
ruling and write under it, or stop with `SPEC_GAP`". Read together the rule is coherent:
the opening states a condition and the menu now contains the branch that satisfies it.
Had edit 2 been omitted the rule would have said a ruling suffices and then offered two
paths that do not include obtaining one — the dangling-neighbour shape the `22b27aa` FULL
blocked. It is not present here.

**The E2 list itself is untouched**, which matters because the list is what makes the rule
decidable by inspection: four blobs and one directory, the fifteen-file re-baseline
sentence, the "a path outside them is not frozen by this rule" sentence, and the
"declared anywhere else … never independently authoritative" sentence all survive
byte-identical in the word-diff. The loosening is to the verb only, not to the extent.

## 3. Does the amendment falsify any neighbour? (the previous round's blocker class)

The blocker at `22b27aa` was an amendment falsifying a present-tense assertion in another
layer member and leaving it standing. `E7` says test the class, so I swept all nine
members at the subject blob rather than the two the commit body reasons about.

Sweep 1 — absolute-freeze vocabulary that edit 1 would falsify
(`untouchable|immutab|must not be (written|modified|changed)`):

| member | hits |
|---|---|
| CONSTRUCTION-CHECKLIST.md | 0 |
| README.md | 0 |
| EXECUTION.md | **1** |
| REVIEW.md | 0 |
| both retired-contract stubs | 0 / 0 |
| supersession-1 / supersession-2 | 0 / 0 |
| paragraph-map.schema.json | 0 |

The EXECUTION.md hit is `| a HarnessIssue, after the run ends | optional, immutable,
evidence-linked |` — a run-artifact property, not the E2 freeze. Read in context, it is
untouched by the verb change. No member asserts the freeze is absolute; **the word
`untouchable` now appears nowhere in the layer**, so edit 1 leaves nothing dangling.

Sweep 2 — dependents of the deleted open tail (`prose successor|later prose|description
string|instruction layer`), across the layer and then the whole `ResearchSystem/` tree.
One live dependent exists: `supersession-2:107`, "Under `E10` it is a prose successor to
signed text and owes an independent read". Edit 3 keeps "prose successors to signed text"
as an appositive on members 7 and 8, so the cross-reference still lands on vocabulary E10
holds. Verified by reading both strings at the subject blob, not by trusting the commit
body's account of it. The remaining hits are journals and prior review records — records,
not instruction — and `README.md:33`, which describes the three tracked checks and makes
no membership claim.

**The `E10` citation-discharge claim, re-derived.** The commit body says members 1–8
discharge by citation against `v3-checkpoint-read-22b27aa.md` §1 and member 9 does not. I
re-derived all nine blobs at the subject tip and read that record's §1 table:

| # | member | record §1 | at subject | citable |
|---|---|---|---|---|
| 1 | CONSTRUCTION-CHECKLIST.md | `2108635f` | `4d0c7330` (this round's own edit; `2108635f` at base) | yes, at base |
| 2 | README.md | `f3a31208` | `f3a31208` | yes |
| 3 | EXECUTION.md | `bd490c8b` | `bd490c8b` | yes |
| 4 | REVIEW.md | `c19d8cb9` | `c19d8cb9` | yes |
| 5 | operating-contract stub | `17ff31bb` | `17ff31bb` | yes |
| 6 | review-contract stub | `52a97a48` | `52a97a48` | yes |
| 7 | supersession-1 | `68031fa2` | `68031fa2` | yes |
| 8 | supersession-2 | `e1a2f26b` | `e1a2f26b` | yes |
| 9 | paragraph-map.schema.json | `c2b713bf` | **`09aa8699`** | **no** |

Member 9 mismatches exactly as reported, and the executor's handling is stricter than the
record that predicted it: `v3-review-verify-c05d052.md` O-2 wrote "This record states the
new id so citation is available again from here", but `E10` conditions citation on *a
recorded end-to-end read*, and a VERIFY record is not a read. The executor read the file
end to end instead of citing the VERIFY. That is the correct reading of the rule over the
observation, and the file is 44 lines as stated. O-2's sentence is inaccurate against E10
as written; it sits in an immutable record and is noted in §5 as an observation only.

## 4. Do the guards bind (`R8`)

The three tracked guards and the suite, run by me after the edits, at HEAD:

```
$ python ResearchSystem/tooling/hooks/layer_path_check.py    -> exit 0
$ python ResearchSystem/tooling/hooks/ledger_cap_check.py    -> exit 0
$ python ResearchSystem/tooling/hooks/review_freeze_check.py -> exit 0
$ python -m unittest discover -s ResearchSystem/tooling/tests/document_harness \
      -p test_precommit_checks.py   -> Ran 20 tests ... OK
```

Green is not binding, so both directions were mutated. Originals were copied to the
scratchpad and sha256'd first; restore came from those copies, never `git checkout --`.

**Mutation A — falsify the prose, leave the code alone.** Deleted
`` `ResearchSystem/document-harness/README.md`, `` from the E10 sentence, so the layer
paragraph enumerates eight paths while still asserting "exactly these nine paths and
nothing else":

```
layer_path_check exit=0 · ledger_cap exit=0 · review_freeze exit=0 · Ran 20 tests ... OK
```

Every guard and every test stays green on an instruction-layer sentence that is now
false. **No guard binds the prose to `LAYER`.** The module docstring is honest about this
— "Mirrors E10's membership sentence. Drift here is caught by the next layer read" — and
the layer's instrument is the independent read, per `README.md:33` and N3-R10. This is not
a defect introduced by the round; it is the surface the round widens, and it is finding
L-3.

**Mutation B — negative control on the code side.** Dropped the same path from `LAYER`:

```
FAIL: test_layer_equals_the_hand_written_membership
FAIL: test_every_member_is_scanned (member='ResearchSystem/document-harness/README.md')
Ran 20 tests ... FAILED (failures=2)
```

Two failures, both the real defect shape rather than a crash, so the code-side double pin
the commit body relies on genuinely binds. Restored from the scratchpad copies; both files
re-hash to their pre-mutation sha256 (`3385fb1d…`, `67c04010…`), `git status --porcelain`
is empty, suite green again.

## 5. Findings

### Low (non-blocking — `R3`: not inflated; `R10` leaves spend-vs-bank to the user at closeout)

**L-1 — the E2 half's authorization is chat-only, and a committed ruling reads the other
way on its face.** `HARNESS-LEDGER.md` records, dated 2026-08-04: "**`E2` 第三出路不写进正文
（2026-08-04）**——只记这条：下轮菜单句看似推翻它而实未（那次裁的是"保留 untouchable 再加例外"）".
Edit 2 writes a third exit into the body. The reconciliation — that the earlier ruling
assumed `untouchable` was being kept, so replacing the verb makes the third branch the
normal path rather than an added exception — is sound reasoning, but every copy of it I
can read (that ledger line, the plan's "看起来矛盾、其实不矛盾" section, the commit body)
is executor-authored. What would close it is a user ruling naming the verb change; the
ledger's open column endorses direction only for the E10 half ("read O-1（E10 open-tail）
**方向=钉死九成员**", with its own honesty note that the user "未逐字裁"), and carries no
counterpart for E2. The commit body attests that an `E11` card was rendered and the user
resolved two literals on it; that attestation is the authorization, and it originates in
chat. `R7` makes this a ceiling to state, never a block, and `R2` makes chat-only
load-bearing material a finding — so it is reported as one and not treated as a defect.
**Decision that goes wrong unfixed:** a later reader reconciling E2 against the ledger
finds a ruling that appears to forbid the clause now in the rule, and re-opens a settled
question — the exact re-litigation that ledger line was written to prevent. **Minimum
fix:** one line, at closeout, recording the user's approval of the verb change as a
ruling, in the same column the 2026-08-04 rulings sit in. **This is the one finding only
the user can close.**

**L-2 — the amendment owes an independent read under `E10`, and nothing in the round's
record trail carries that obligation.** `E10`: "each amendment passes an independent read
before any round relies on it — that read's subject is the amendment text itself, never
the work it governs, **and it is never banked as the round's FULL**". This amendment
changes what two rules require, which is why it opened a round at all, so the deferral
arm ("neither adds a clause … nor changes what any rule requires") is unavailable. Two
things that look like the read are not: the opening cold read ran against blob `2108635f`,
the *pre*-amendment text, and this FULL is expressly disqualified by the clause above.
Nothing is violated yet — `E10` defines *relied* to exclude authoring, so the obligation
bites at the next round that relies on the new E2 or E10, not today. But the plan's steps
6–10 end at closeout with no read scheduled, and the ledger's open column does not name
one. The precedent is exact and recent: `v3-checkpoint-read-22b27aa.md` raised its single
must-fix for this same shape — "the obligation record stops one clause short of `E10`".
**Decision that goes wrong unfixed:** the next round writes a frozen byte under the new
E2 branch, or leans on the pinned membership, while the text authorising it has never been
independently read — and no artifact exists that would have reminded anyone.
**Minimum fix:** one line in the ledger's open column at closeout naming the read as owed.
**Deadline:** before any round relies on the amended E2 or E10 — whichever comes first,
and `O-2b`'s redemption is one such round.

**L-3 — the pin creates a three-place sync of which the prose leg is mechanically
unguarded, and a queued item will trip it.** After edit 3, membership must agree in three
places: the E10 sentence, `layer_path_check.LAYER`, and `test_precommit_checks.EXPECTED`.
Two of the three are pinned to each other by an assertion; the prose is pinned to neither,
as Mutation A demonstrates — a sentence claiming "exactly these nine paths and nothing
else" while listing eight passes every guard and all 20 tests. Before this round the prose
was open-ended and could not contradict `LAYER` by omission; now it can, and silently.
The trigger is not hypothetical: the ledger's backlog carries **contract v4** with user
intent dated 2026-08-04, merging s1 and s2 into one file. Under the deleted open tail v4
would have joined the layer automatically; under the pin it does not, and minting it now
requires editing E10, `LAYER` and `EXPECTED` together — with the E10 edit itself being
rule-requirement-changing, hence another round. The same holds for any future prose
successor and for the fourteen pack schemas whose `description` strings no longer pull
them into the layer when amended. **Decision that goes wrong unfixed:** contract v4 is
minted, s1/s2 leave the layer and v4 never enters it, and no read is owed on the file that
supersedes the signed contract — while E10 still reads "and nothing else" and every guard
stays green. **Minimum fix:** one rider row against `HARNESS-RIDERS.md` naming E10's
membership sentence plus the two code sites as the target. **Deadline:** the batch that
mints contract v4, or any batch adding a prose successor, whichever arrives first.
Whether the prose leg should instead be pinned by a check is a design question and
`E6` argues against new machinery — `R5` leaves the conclusion to the user; I report the
asymmetry, not a recommendation.

### Observations (`R5` — reported; the conclusions are the user's)

**O-1 — rider `O-2b`'s redeem-when is now stale, and the executor said so without fixing
it.** The row reads "特殊：属 `E2` 冻结面，须裁决重开才能兑" — a special act reopening the
freeze — where the amended E2 makes it an in-rule branch requiring a recorded ruling. The
commit body discloses the drift and declines to act, on the ground that the round's
boundary is one file. I agree that is the right call under `E8`, and the finding is `R9`
wording-level: either way the action is *obtain a user ruling*, and the accurate fact is
recoverable from E2 itself. It rides the next batch touching the bank; it spawns no round.

**O-2 — a review record asserts a citation route the rule does not offer.**
`v3-review-verify-c05d052.md` O-2 says of member 9 "This record states the new id so
citation is available again from here". `E10` conditions citation on a recorded end-to-end
*read*, and that file is a VERIFY. This round paid the difference correctly by reading the
schema rather than citing the VERIFY, so the practice is unharmed; but the sentence sits
in an immutable record and would mislead a session that followed it. Reported so the next
`E10` read of the layer knows the route is unavailable, not so anything is amended.

## 6. Boundary and record conformance — second (`R3`)

- **`E8`.** Title `V3-E2-VERB-E10-PIN-v1`, single dense line naming the round. One dense
  paragraph, no trailers. Kind named in the first two words — "Kind: candidate" — so
  attribution needed no asking. New commit, not an amend (`git log` shows `3b7ebe2` intact
  as parent). Inside the declared boundary: one file, the one the plan names. No push —
  `git rev-list --count origin/main..HEAD` = 440, unchanged and user-gated by the
  2026-07-30 ruling.
- **`E9`.** Budget intact as derived in §1: no prior FULL for this round, so the candidate
  consumed nothing and this FULL is the round's one independent review. Nothing in the
  range is a renamed round.
- **`E3`.** The commit body's factual assertions were re-run here rather than read: line
  counts, blob ids, the nine-tuple equality, the 44-line schema read, guard exits. All
  hold. The one figure I could not witness is the claim that the guards were run *after*
  the edits and before the commit — a process claim, marked under `R4`, not verified.
- **`E11` / `E12`.** The card is attested, not committed; see L-1 for the ceiling. The
  dispatch marker is untracked, so `E12`'s recorded-range clause is not engaged (§1).
- **Ledger cap.** 119 lines against `ledger_cap_check.MAX_LINES = 120`. The closeout owes
  at least the L-1 and L-2 lines and the `read O-1` redemption; one line of headroom means
  reclaim-before-add, as the plan already notes and as `c05d052`'s O-3 warned.
- **`R10` at closeout.** Three lows with `REVIEWED_NO_BLOCKER` are not banked by default:
  L-1 and L-2 have deadlines that arrive before the next round rather than on a touch
  condition, so the spend-the-fix-leg-versus-bank choice goes to the user before closeout.
  Note that `E9`'s test does not expire at closeout — activating the fix leg late still
  costs this round's one user-approved fix and still obliges the VERIFY.

## 7. Coverage disclosure (`R4`)

**Read in full:** the amended `CONSTRUCTION-CHECKLIST.md` at the subject blob (173 lines);
the range diff, plain and word-level; `layer_path_check.py` (105 lines); the
`LayerMembership` block of `test_precommit_checks.py`; `.goals/plans/e2-verb-e10-pin.plan.md`
(172 lines); `HARNESS-LEDGER.md` (119 lines); `HARNESS-RIDERS.md` (17 lines); the commit
bodies of `838c413` and `3b7ebe2`; §1 of `v3-checkpoint-read-22b27aa.md`; §5 observations
of `v3-review-verify-c05d052.md`; the header and section list of `v3-review-full-22b27aa.md`.

**Sampled:** the other eight layer members were swept by pattern for the two dependency
classes in §3 and read in context at every hit, not read end to end. This is a coverage
ceiling on §3's sweeps: a dependent phrased in vocabulary neither sweep used would have
been missed. I did not re-read the retired contracts at `7011916`.

**Only probed:** the wider `ResearchSystem/` tree, by grep, for open-tail dependents; run
artifacts and journals were classified as records and not audited.

**Not verified — process claims, marked per `R4`:** that this reviewing session is fresh
context; that the executor's session held one role throughout (`E1`); that the `E11` card
was rendered before the edits and that the user resolved its two literals as described
(L-1); that the guards were run after the edits and before the commit. Each is asserted in
the commit body and none is witnessable from the repository.

**`UNVERIFIABLE`, not folded into supported:** whether the user authorized the E2 verb
change. That is L-1 and it is stated as unverified rather than dropped, because a decision
turns on it.

Mutation proves the tests in §4 have binding force in the directions probed, not that
their force is sufficient. This FULL is not a re-certification of any earlier round; the
verdicts on `22b27aa` and `c05d052` stand as recorded and are not re-adjudicated here.
