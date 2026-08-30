# Targeted VERIFY — `8f6b3ef..c7f9c8d` (round `CORE-ONLY-LAYER`)

Targeted VERIFY of round 1 of batch `CORE-ONLY`, over the round's one user-approved fix leg.
Subject received as one range and nothing else (`R2`); round, budget, authorization, obligations
and every figure below are re-derived from the repository, and no reported figure is accepted.
Standing instruction as dispatched: `migration/document-work-assurance-v3/v3-harness-review-contract.md`,
read first, then the file it names — `document-harness/CONSTRUCTION-CHECKLIST.md` — and then the
counterpart *that* file names, `document-harness/RULES.md`. That the dispatched stub itself now
describes this three-hop chain is the subject's own blocker **B-1**, and my arrival is the first
end-to-end evidence its repair works.

**Verdict: `REVIEWED_NO_BLOCKER`.** All seven accepted findings landed and each is verified by my
own measurement. 1 low, 1 observation, neither blocking.

---

## 1. Subject, budget and authorization, re-derived

```
$ git rev-parse HEAD
c7f9c8db09cebb0f976042f91aae2bd9e0d7707f
$ git status --porcelain
?? .goals/
$ git rev-list --count 8f6b3ef..c7f9c8d
3
$ cat .harness/review-pending.json
{
 "subject": "8f6b3ef0467f5cfe77b590c4da399eb322d1285d..c7f9c8db09cebb0f976042f91aae2bd9e0d7707f",
 "dispatched_at": "2026-08-30T02:39:29+00:00"
}
```

The marker carries exactly this range and the branch tip is the range tip, so `E9`'s window holds
and nothing but this record is owed to it.

Three commits, classified by hand from their own bodies and diffs:

| kind | commit | what it touches |
|---|---|---|
| record (independent FULL) | `8997d94` | adds `v3-review-full-8f6b3ef.md`, one file |
| ruling (orchestrator) | `15fa949` | `document-harness/plans/core-only.plan.md`, one file |
| review fix (executor) | `c7f9c8d` | nine files, listed in §3 |

**Budget (`E9`), re-derived.** One FULL, at most one user-approved fix, one targeted VERIFY.
A valid independent FULL has occurred — `v3-review-full-8f6b3ef.md`, subject `db1bfa1..8f6b3ef`,
verdict `CHANGES_REQUIRED`, landed at `8997d94` — so `E9`'s test resolves the other way for
`c7f9c8d`: it is the fix round, it is the single user-approved fix, and it obliges this VERIFY.
No second fix commit exists in the range. I confirm independently that no `v3-review-verify-*`
record exists for any commit in this range, so this VERIFY is the third and last spend.

**Authorization.** Plan ruling 31, carried in the committed plan at `15fa949` — a committed
carrier, not chat (`R2` satisfied on that axis). It is the fix gate after the FULL and it names
what the one leg carries: **B-1**, **B-2**, **L-1** (with the ruling the FULL said L-1 needed —
delete the token), and **L-2**–**L-5** with the reviewer's bytes as supplied. `O-1`, `O-3`, `O-4`
are recorded and owe nothing; `O-2` was answered at ruling 30. The user chose `E9`'s route over
`E10`'s free channel for the two blockers, on the ground that a FULL's blockers taken through a
channel that spends nothing is the renamed-round shape `E9` warns of.

`HARNESS-DECISIONS.md` `§live` read at this tip: twelve entries (`HD-68` `HD-67` `HD-66` `HD-65`
`HD-62` `HD-59` `HD-41` `HD-36` `HD-35` `HD-34` `HD-23` `HD-9`). Two bear on this leg and both are
obeyed: `HD-59` (corrections go forward, never in place) governs the rider touch note and the
step-2 box; `HD-41` ④ (class-scan before writing a fix, grep output pasted into the body) is
where finding **V-1** below sits.

## 2. Implementation (`R3`, run first) — each accepted finding, measured

Every figure in this section is my own run at the subject tip.

### B-1 — both stubs now name the real carrier, and the claim they make is true

The two members' first sentences were replaced. What they now assert I checked against the tree
rather than reading:

```
$ grep -oE '^- \*\*(E|R)[0-9]+' document-harness/RULES.md
E1 E3 E4 E5 E6 E7 E8 E9 E10 E11 E12 R1 R2 R3 R9 R10 R4 R5 R6 R7 R8      # 21
$ grep -oE '^- \*\*(E|R)[0-9]+' document-harness/CONSTRUCTION-CHECKLIST.md
E2 R6                                                                    # 2
```

So "`E2` and one `R6` instance value" in the checklist and "`E1`, `E3`–`E12` and `R1`–`R10`" in
`RULES.md` are both exactly right. The review-side stub keeps its standing-instruction sentence,
rewritten to send the reader on; the operating side takes the same correction without one, which
matches its pre-image — it never carried that sentence.

The executor retained the true Phase A provenance clause rather than dropping it with the
falsehood. That is beyond the literal supplied bytes and it is the right call: `E6` says the fix
is the wrong text changing, the provenance is not the wrong text, and nothing authorized deleting
it. Disclosed in the commit body, so it is not a silent widening.

**The failure path is closed at its source, and I am the test.**
`dispatch.CONSTRUCTION_ROLE_INSTRUCTION` (`tooling/rsclib/document_harness/dispatch.py:548-550`)
is the review-side stub, substituted into `CONSTRUCTION_PROMPT` as `{charter}` at `:587` / `:703`.
It is the first file I opened. It told me to read the checklist *and the counterpart it names*,
and both hops were named with resolving links. The reviewer the FULL described — one that opens
the checklist, finds two rules, and concludes the mount is broken — cannot arise from these bytes.

**Class scan, my own, at this tip over all tracked files** (the FULL's scan excluded the journal
and the plans; mine excludes nothing):

```
$ git grep -nE 'carries both sides|R1[–-]R10|E1[–-]E12' | wc -l      -> 5
$ git grep -n 'own counterpart' | wc -l                              -> 41
```

Every one of the 46 hits is in `migration/document-work-assurance-v3/v3-*.md` — committed read and
review records quoting the old text, and one scan key inside a prior VERIFY. No live descriptive
site survives, and none of the nine instruction-layer members nor this repository's declared rule
file carries one.

### B-2 — the residue is named, and the class it belongs to is now empty

The sentence landed as its own paragraph at `document-harness/RULES.md:20-23`, immediately after
the paragraph claiming every identifier is present — which is where the reader forms the false
belief — and its bytes are the FULL's, word for word. It adds no clause to any rule and changes no
requirement; the schema site is untouched, so no announced path moved.

I checked the whole class rather than the two reported sites. On **my own harness-only tree** —
`git archive c7f9c8d` over `CONSTRUCTION-INDEX.md`'s eight product-tier rows, extracted, made a
git repository, 59 tracked files, which is the tier count the index states — I extracted every
backticked `E<n>`/`R<n>` citation in all 59 files and resolved each against the rules `RULES.md`
actually defines:

```
defined in RULES.md: 21 — E1 E3..E12 R1..R10
total backticked E*/R* citations in the harness-only tree: 62
UNRESOLVED E2 -> document-harness/RULES.md:20, :22, :169
UNRESOLVED R0 -> document-harness/EXECUTION.md:235
```

Two of the three `E2` hits *are* the new sentence, and the third is `E10`'s freeze exception, which
that sentence explicitly covers. `R0` is a product run's own requirement number, not a rule — the
FULL said the same and I re-derived it. The unbackticked site the FULL measured
(`schema/document-assurance-v3/paragraph-map.schema.json:5`, "part of the E2-frozen surface") is
covered by the sentence's "a schema description". So a cold reader in a caller who greps `E2` now
lands, in the same file, on a sentence saying what `E2` is, where it went, and that nothing of
theirs is frozen by it. The rider `checklist-cited-not-carried` was correctly not re-banked: the
alternative was conditional on the class staying live, and it does not.

### L-1 — the token is gone, and acceptance 1 is item D's four sites, measured

`document-harness/README.md:26` lost `` `.githooks/` ``; the parenthetical now reads only
"(reached by a per-machine `core.hooksPath`, so a fresh clone still starts with none)", which is
what ruling 31 authorized. Sweep on my harness-only tree at this tip:

```
$ python tooling/sweep_refs.py <harness-only tree at c7f9c8d>
PATHTOK document-harness/RULES.md:92  migration/document-work-assurance-v3/v3-harness-operating-contract.md
PATHTOK document-harness/RULES.md:93  migration/document-work-assurance-v3/v3-harness-review-contract.md
MISSING migration/document-work-assurance-v3/v3-harness-operating-contract.md
MISSING migration/document-work-assurance-v3/v3-harness-review-contract.md
-- 32 caller-held or unresolvable references over 9 members and declared rule files
```

Four sites naming an instrument-held artifact, **all four item D's**, and no fifth; the remaining
28 are `NAMETOK` caller-held bare names, the compliant form. Down from the FULL's 33 by exactly
one, and the one removed is the one deleted. Acceptance 1 as re-stated is true as stated.

The sibling token `` `.githooks/pre-commit` `` in the same row survives, and the executor reported
it rather than deleting it — ruling 31 named one token, so a second deletion was unauthorized. I
confirm both halves of its claim: `document-harness/README.md` holds exactly one `.githooks`
occurrence, and neither guard can see it —

```
$ python -c "from layer_path_check import PATHLIKE; ..."
'.githooks/pre-commit' -> False        # no admitted extension, no trailing slash
'.githooks/'           -> True         # the shape that was deleted
```

so it is invisible to `layer_path_check` and, carrying a `/`, to the sweep's `NAMETOK` form as
well. It is rider `e10-cannot-see`'s named member-internal instance, which is why that row needed
nothing and correctly got nothing.

### L-2 to L-5 — the four supplied-byte fixes

- **L-2.** All five sites in `README.zh-CN.md` corrected; `grep -c 九项 README.zh-CN.md` returns
  **0**. The step-2 comment is now byte-identical to `README.md`'s, and I checked it against
  behaviour rather than against the twin: `python tooling/dtw.py init --repo-root <fresh repo>`
  prints `created  : harness.json` among six creations, exit 0. The `十项里的六项` framing matches
  that count.
- **L-3.** `init_target.py:4-11` now says ten items and six judgment, and I matched the six named
  against `NOT_DONE`'s six one for one — policy file / rules declared / pointer line / hook guards
  / submodule revision / first journal. The same six are what the command actually printed above.
- **L-4.** Anchor `cbaee8e` → `4b81dd9`. Measured:

  ```
  cbaee8e: repo=414 tier=58
  4b81dd9: repo=415 tier=59      <- both stated figures reproduce here, and only here
  c7f9c8d: repo=417 tier=59
  ```

- **L-5.** Step 2's box is checked with the supplied bytes. `a542c6d` is
  `V3-CORE-ONLY-LAYER-HD67-RULING-v1`, touching `HARNESS-DECISIONS.md` alone, and `HD-67` is in
  `§live` at `:59` — so the box names the commit that made it so, as the plan's own rule requires.

### The guard that stands over the amended members still binds (`R8`)

The repair changes no guard code, so there is no new guard to prove. What matters instead is that
the guard covering the three amended instruction-layer members still catches the defect class
those members were amended to fix. Mutation on my own hand, restored by copy from a
sha256-checked scratchpad, never `git checkout --`:

```
$ sha256sum migration/document-work-assurance-v3/v3-harness-review-contract.md
0d886d7d69bd2ea33585df834d23334b198396b174b9c140018a60d437961507
# the new sentence's `document-harness/RULES.md` token bent to `document-harness/RULE.md`, staged
$ python tooling/hooks/layer_path_check.py
pre-commit BLOCKED: ... `document-harness/RULE.md` - resolves nowhere in this repository ...
exit=1
# restored; a resolving token appended on a genuinely added line instead, staged
+ > Control line: `document-harness/EXECUTION.md`
$ python tooling/hooks/layer_path_check.py            exit=0
# restored from the checked copy
$ sha256sum ... -> 0d886d7d69bd2ea33585df834d23334b198396b174b9c140018a60d437961507
$ git status --porcelain -> ?? .goals/
```

Must-fire red, negative control green on an added line the guard genuinely scanned — so the pair
proves the guard reaches the repaired file and discriminates, not merely that it ran.

### Whole-tree state at the subject tip

```
$ python -m pytest tooling/tests -q
853 passed in 155.50s
$ python tooling/hooks/layer_path_check.py       -> 0
$ python tooling/hooks/candidate_path_check.py   -> 0
$ python tooling/hooks/review_freeze_check.py    -> 0
$ python tooling/sweep_refs.py
-- 13 caller-held or unresolvable references over 10 members and declared rule files
$ python tooling/announced_path_disclosure.py --after c7f9c8d --before 8f6b3ef
  3 non-merge commit(s) judged
  every announced path changed in this range is named by the commit that changed it
```

## 3. The whole repair diff — nothing outside the leg

Ten paths change across the range; nine are `c7f9c8d`'s, one is the FULL record itself. Classified
by hand against ruling 31:

| path | which accepted finding | in ruling 31 |
|---|---|---|
| the review-side and operating-side retired-contract stubs | B-1 | yes |
| `document-harness/RULES.md` | B-2 | yes |
| `document-harness/README.md` | L-1 | yes |
| `README.zh-CN.md` | L-2 | yes |
| `tooling/rsclib/document_harness/init_target.py` | L-3 | yes |
| `CONSTRUCTION-INDEX.md` | L-4 | yes |
| `document-harness/plans/core-only.plan.md` | L-5 | yes |
| `HARNESS-RIDERS.md` | `R10` bookkeeping for L-4's touch | rides the change it records |

The one path not on ruling 31's list is the rider bank, and it is in bounds: `figure-units`'s touch
condition is a batch touching `CONSTRUCTION-INDEX.md`'s figure paragraph, L-4 is that touch, and
`R10` requires the touch to be answered where it lands. It was recorded and not redeemed, with the
reason given as boundary rather than judgment — its two live sites are journal byte figures routed
by `HD-23` and outside this leg. I checked that no row left quietly:

```
rider id set at 8f6b3ef  ==  rider id set at c7f9c8d   (24 rows, identical)
diff over HARNESS-RIDERS.md: 1 row changed, 0 added, 0 deleted
```

No announced path is touched anywhere in the range — neither the contract nor any file under
`schema/document-assurance-v3/` appears in `git diff --name-only`, and the disclosure alarm
confirms the range mechanically.

## 4. Findings

### V-1 (low) — the counting class L-2 and L-3 named survives at two live sites, because `HD-41` ④'s class scan was run for the blockers and not for the lows

**Location.** `tooling/rsclib/document_harness/cli.py:10` and
`tooling/tests/document_harness/test_init_command.py:343`.

**What they say, and the ground truth.** `cli.py:10`: "`init` writes into a target repository being
onboarded — the mechanical slice of onboarding's **nine items**, and nothing else
(`init_target.py`; …)". Onboarding is ten items — `document-harness/ONBOARDING.md:68` heads them
"The ten items", `:189` is item 10, and `init_target.py:4`, which this very sentence names, says
ten after this leg's L-3 fix. The two files disagree in the same breath.
`test_init_command.py:343`: "the **five** items it does not perform", immediately above a
hand-written list of **six** literals — the round added the sixth to that list and to `NOT_DONE`
and left the comment's count. Both counts were true before this round and were falsified by it.

**Measured, my own scan over every tracked file outside the records, journals and plans:**

```
$ git grep -nE '(nine|ten|five|six)[ -](items|of them)|(九|十|五|六)项'
tooling/rsclib/document_harness/cli.py:10                  nine items   <- stale
tooling/tests/document_harness/test_init_command.py:343    five items   <- stale
document-harness/ONBOARDING.md:210, :219, :236             nine items   <- correct: past-tense
                                                    records of the 2026-08-19 / 08-24 walks
README.md:144,146,218,267 · README.zh-CN.md:140,141,204,248 · ONBOARDING.md:68,94 ·
document-harness/README.md:25 · init_target.py:4                        <- all ten, correct
```

Two stale sites, and no third. `cli.py` was not inside the round's change boundary and went stale
because the round added the tenth item; `test_init_command.py` **was** inside it — the round edited
that file twice (`cbaee8e`, `4b81dd9`) to add the sixth literal — so its count was missed rather
than deferred, which is the exact shape the FULL used to justify L-2.

**Why it survived.** `HD-41` ④ requires a class-scan grep before writing a fix, with the output
pasted into the commit body. The body pastes four scans for B-1 and B-2 and one for L-2 scoped
"in that file"; there is none for the class either low belongs to. The scan that would have found
both is the one above, and it takes one command.

**Downstream decision that goes wrong.** `cli.py` travels to every caller. A reader working out
what `init` covers reads "onboarding's nine items", and the item missing from that count is
`harness.json` — the one this round exists to add, and the one whose omission leaves a caller's
declared rules unscanned. The test comment is milder: a reader deciding whether a seventh
`NOT_DONE` entry belongs reads a count one short of the list directly beneath it.

**Bytes supplied.** `cli.py:10`: `nine items` → `ten items`. `test_init_command.py:343`:
`the five items it does not perform` → `the six items it does not perform`. Neither file is an
instruction-layer member, so neither fix owes a read. Not a blocker: no check outcome, no guard,
no verdict path and no acceptance turns on either, and inflating it would burn a leg that is
already spent (`R3`).

### V-2 (observation) — the `E10` read debt on the three amended members is recorded and routed, but the reliance it withholds is not stated

`c7f9c8d` amends three instruction-layer members (`document-harness/RULES.md`
`63958f0`→`47a7fbe`; the review-side stub `29bdc9f`→`b79ebb2`; the operating-side stub
`6d57149`→`729313a`).
`E10` requires each amendment to pass an independent read before any round relies on it, and offers
a deferral to an amendment that adds no clause, changes no requirement, and whose effect on every
round in flight is nil — **provided the commit records both facts** and the bytes ride the next
read. The body records the first fact for B-2 only ("No clause is added to any rule and no
requirement changes") and records the ride-along for all three ("The `E10` read debt on the two
stubs and on `RULES.md` rides the next opening read of this layer"). The second fact is stated for
none of the three, and the deferral is therefore not fully claimed.

Nothing is wrong today, and the obligation is not lost: plan step 6d, written at `15fa949` before
the fix, already carries "the `E10` read debt on the changed members recorded for round 2's
opening". What is missing is the sentence this round's three contract commits did write in the
same position, and which the FULL's `O-3` called the honest handling — that until the read returns,
no conclusion of this round rests on the changed bytes. I record the shape rather than asking for
a change: which of the two dispositions closeout takes is the orchestrator's and the user's
(`R5`), and my own verification of these bytes is a VERIFY of a repair, not the `E10` read, whose
subject is the amendment text itself and which is never banked as a round's review.

## 5. What I read, and the ceilings (`R4`)

**Read in full:** the whole of `c7f9c8d`'s diff, hunk by hunk, all nine files; all three commit
bodies in the range; `v3-review-full-8f6b3ef.md`; `document-harness/RULES.md`;
`document-harness/CONSTRUCTION-CHECKLIST.md`; both retired-contract stubs;
`.harness/scan-surfaces.json`; `CONSTRUCTION-INDEX.md`; plan ruling 31 and the plan's step list and
resume pointer; `tooling/hooks/layer_path_check.py`; the docstring and `NOT_DONE` of
`init_target.py`; `tooling/tests/document_harness/test_init_command.py`'s `ThroughTheCommandLine`;
`HD-41` in full.

**Sampled:** `HARNESS-DECISIONS.md` — `§live`'s twelve headings, `HD-41` in full, `HD-67`'s and
`HD-68`'s headings, the rest by heading. `HARNESS-RIDERS.md` — the changed row in full, the other
23 by id. `document-harness/ONBOARDING.md` — the item headings and the two execution-record
sections. `tooling/sweep_refs.py`'s docstring and resolution rules. `CONSTRUCTION-LEDGER.md` — the
current-pointer section by heading and its queue-head paragraphs.

**Probed only:** `tooling/rsclib/document_harness/dispatch.py` (the charter constant and its three
call sites, to establish B-1's failure path is closed at source).
`tooling/rsclib/document_harness/cli.py` (the module docstring). `README.md` (the step-2 block and
the four count sites).

**`UNVERIFIABLE`, stated rather than folded into supported:**

- That `c7f9c8d` ran as a cold `claude -p` executor session holding none of `R1`'s four holdings.
  The commit body states it; it is a process claim about a session I cannot inspect. Marked, not
  verified (`R4`). What I can say structurally is that this VERIFY was dispatched by, prompted by,
  scoped by and reported through the orchestrator, and I received the range and nothing else.
- That the FULL's freeze marker was deleted in the act that committed its record, closing `E9`'s
  window before `15fa949` landed. `.harness/` is gitignored, so the deletion leaves no tracked
  trace; the marker's absence at the time the two later commits landed is not reconstructible from
  the repository.
- That the executor staged explicit paths rather than `add -A`. The body enumerates nine and
  `--name-only` returns those nine, which is consistent with either; I did not verify the mechanism.

**Ceilings on my own coverage:**

- **A VERIFY is never a re-certification** (`R4`). I did not re-derive the rule split, the guard's
  end-to-end behaviour on a fresh caller, or the contract diff against its disclosures — those were
  the FULL's, they are not in the repair diff, and nothing in this leg disturbs them. The only
  permanent boundaries I re-measured are the ones the repair could have moved: the announced
  surface, the layer guard over the amended members, the sweep, the rider set, and the tier counts.
- My harness-only tree is `git archive` over the eight product-tier rows as `CONSTRUCTION-INDEX.md`
  defines them; if a row's definition is wrong, my tree is wrong the same way. The 59-file count
  agrees with the index, which is a consistency check, not an independent derivation of what ought
  to travel.
- Mutation proves a test has binding force, never that its force is sufficient. One guard was
  mutated, on the shape this repair could have introduced; the other two were run, not mutated.
- No `dtw dispatch` mode was exercised and no product run was built. Acceptances 4, 6, 8 and 11's
  dispatch clause are not this round's and I did not evaluate them.
- Line numbers in this record were re-derived at `c7f9c8d` and drift with the next commit.

## 6. Process and record conformance (boundary check, run second)

- **`E9`** — the budget is exactly spent: FULL `8997d94`, one user-approved fix `c7f9c8d` under
  ruling 31, this VERIFY. No second fix, and no commit landed inside my window but this record.
- **`E8`** — title `V3-CORE-ONLY-LAYER-FIX-v1`, round named, single dense paragraph, no trailers,
  and the kind named in the first sentence ("Review fix"); the other two name theirs ("ruling
  commit", "record"). Author and committer timestamps are equal on all three commits, so no amend
  or rebase inside the range. `origin/dev` is four commits behind `dev`: not pushed.
- **`E2`** — no announced path is touched; the disclosure alarm confirms the range, floor
  `1d4d9aa`, three commits judged, exit 0. The fix commit says so and the claim reproduces.
- **`E3`** — the body's figures are measured, pasted, and anchored to the staged tree `409e1e8`
  immediately before it was written. Every one I re-ran reproduces: 853 tests, four guard exits,
  both sweep tallies, and the harness-only tree's 59 files and 32 references.
- **`E1` / `R1`** — the fix commit discloses that the executor held none of `R1`'s four holdings,
  which is the norm rather than the exception channel, and does not call the result structurally
  independent. Marked as a process claim above.
- **`R2`** — no chat-only load-bearing material. Ruling 31 is in the committed plan; the accepted
  findings are in the committed FULL record; the rider decision is in the committed bank.
- **`R10`** — one row touched, none deleted, none added; the touch recorded forward under `HD-59`
  rather than rewritten in place; the non-redemption's reason stated as boundary.
- **`E10`** — three members amended; blob ids recorded in `V-2` above so the owed read can cite
  them, since a read's record must state the blob id of each member it read.
- **`R6`** — this record is `v3-review-verify-c7f9c8d.md` under
  `migration/document-work-assurance-v3/`, which is what `.harness/scan-surfaces.json` declares
  under `review_record_dirs` and what `CONSTRUCTION-CHECKLIST.md`'s `R6` instance value states.
  Written in the worktree, uncommitted; the orchestrator commits it.

## 7. Disposal, for the orchestrator

The fix leg is discharged: all seven accepted findings landed, each verified by measurement, and
nothing outside ruling 31's boundary changed except the rider row that `R10` required the change
to carry. `E9`'s three legs are spent and the round is clear to close on the review side.

`V-1` supplies exact bytes at two non-member sites, so it takes `E10`'s free channel and owes no
read; if it is banked instead, its touch condition is the next batch touching `cli.py`'s docstring
or `test_init_command.py`, and its deadline is the first caller onboarding from the CLI module's
own documentation. `V-2` asks for nothing and is recorded so closeout can choose its disposition
knowingly; the read debt it names is already on plan step 6d for round 2's opening, and the three
blob ids are above.
