# FULL review — `05ae1b6..3deb304` (round `CORE-MOUNT`, batch `CORE-MOUNT`)

**Verdict: `CHANGES_REQUIRED`** — one blocker (`B-1`), one low, two observations.

The headline work is sound and I drove it rather than read it. The manifest, the ONBOARDING
step and the index row do what they claim: a `--no-checkout` clone narrowed by
`document-harness/product-tier.txt` materializes 61 tracked files and no more, the four
construction-side files stay off disk, the CLI still imports, and the new guard binds — six
mutations I ran myself each turned it red with a green control on both sides. Every figure the
two commit bodies paste, I re-ran; all of them matched.

The blocker is in the *other* commit. `4020efa` redeemed rider `protected-set-says-five` by
rewriting contract §13.2, and the sentence it wrote is false: it says two protected fields have
a live write path in the shipped template, and four do. The commit that existed to take a false
statement about the protected set out of the signed contract left a different false statement
about the protected set in the signed contract, and the ninth `CONTRACT-V4-SIGNATURE.md` entry
certifies a `HD-63` class claim ("both sentences were true when v4 was signed") that the tree
at the v4-creating commit refutes for one of the two sites.

> Subject received as a range and nothing else (`R2`). Round, budget, authorization, boundary
> and every figure below were re-derived from this repository; no reported figure was accepted
> as reported, and where a claim is reproduced, the reproduction is what is stated.
>
> Written by the reviewer and **not committed by it** — `R6`. `.harness/review-pending.json`
> is deliberately left in place; the commit that lands this file is what deletes it.
>
> **One artifact, not two.** `REVIEW.md`'s *Where the result lives* names a ReviewResult beside
> this record, written to a control root the caller holds. A construction round has no control
> root, no WorkSpec and no obligation list, so there is nothing for that document to be
> schema-valid against and nothing to bind it to. The record alone is returned, as every prior
> construction FULL in this directory returned it. The absence is stated rather than passed over.

## 1. Subject, re-derived

```
$ git rev-list --count 05ae1b63d8a49b6bced9acdd3b3f87d8be74efb0..3deb304353c7ebd93aa795a4bf9ecd797e7c7f06
6
$ git diff --numstat 05ae1b6 3deb304 | awk '{a+=$1;d+=$2;n++} END {print n" files, +"a" -"d}'
15 files, +1116 -25
$ git rev-parse HEAD ; git branch --show-current
3deb304353c7ebd93aa795a4bf9ecd797e7c7f06
dev
$ git status --porcelain
?? .goals/
```

The branch tip is the dispatched tip; nothing landed after the dispatch. The freeze marker's
own bytes agree with the prompt I received:

```
$ cat .harness/review-pending.json
{ "subject": "05ae1b63…..3deb304353…", "dispatched_at": "2026-09-03T08:13:30+00:00" }
```

`3deb304` is stamped `Thu Sep 3 18:13:20 2026 +1000` = `08:13:20Z`, ten seconds before the
marker. The window is empty.

Oldest first, kind taken from each commit's own body (`E8`):

| # | sha | title | kind |
|---|-----|-------|------|
| 1 | `73bfe1e` | `V3-CORE-MOUNT-OPEN-v1` | open — plan, journal, ledger entry |
| 2 | `d0d029a` | `V3-COLD-READ-RECORD-73bfe1e-v1` | record — the opening `E10` read |
| 3 | `8ecc7a5` | `V3-CORE-MOUNT-READ-DISPOSITION-v1` | disposition — L-1 banked, L-2 free-channel, `HD-70` flip |
| 4 | `4d2bf42` | `V3-CORE-MOUNT-MANIFEST-AND-STEP-v1` | candidate — manifest, test, ONBOARDING 1b, index row 9 |
| 5 | `4020efa` | `V3-CORE-MOUNT-PROTECTED-SET-SIX-v1` | candidate + rider redemption — `protected-set-says-five` |
| 6 | `3deb304` | `V3-CORE-MOUNT-POINTER-v1` | pointer — plan steps 3–4, journal |

`open` / `disposition` / `pointer` are not in `E8`'s enumerated kind list. They are established
practice here — `git log --format='%b' -200 | grep -o "Kind: [a-z-]*" | sort | uniq -c` returns
twenty-three distinct kinds, `disposition` three times before this round — and `E8`'s purpose
("so the review side can attribute it without asking") is served. Not a finding.

**Paths classified by hand** (`R2`), from `git diff --name-status 05ae1b6 3deb304` — 15 files,
10 `M` and 5 `A`, nothing deleted:

- **Announced (`E2`)** — 1: `contract/Document-Work-Assurance-Contract-v4.md`. No file under
  `schema/document-assurance-v3/` appears in the range at all, which is the other half of the
  announced set.
- **Instruction layer, `E10` members** — 2: the contract above, and
  `document-harness/REVIEW.md` (`:129`, one line).
- **Governance registers** — 4: `CONSTRUCTION-LEDGER.md` · `HARNESS-DECISIONS.md` ·
  `HARNESS-RIDERS.md` · `CONTRACT-V4-SIGNATURE.md`.
- **Product tier, non-member** — 2: `document-harness/ONBOARDING.md` ·
  `document-harness/product-tier.txt` (new).
- **Construction-side inventory** — 1: `CONSTRUCTION-INDEX.md`.
- **Code and tests** — 3: `tooling/rsclib/document_harness/summary.py` ·
  `tooling/tests/document_harness_review/test_run_v2_template_bind.py` ·
  `tooling/tests/document_harness/test_product_tier_manifest.py` (new).
- **Round records** — 3: the plan, the journal, and the read record
  `migration/document-work-assurance-v3/v3-cold-read-73bfe1e.md`.

## 2. Round, budget and authorization, re-derived

The round is `CORE-MOUNT`, one round in a batch of the same name, opened 2026-09-03 at base
`05ae1b6` — `CONSTRUCTION-LEDGER.md`'s current pointer carries the batch and the user's queue
ruling; `document-harness/plans/core-mount.plan.md` carries the goal, the eight design
decisions, the change boundary, six acceptance criteria and four rulings taken at the `E11`
card. `document-harness/CONSTRUCTION-CHECKLIST.md` is what `harness.json` declares under
`rules`; `document-harness/RULES.md` is the counterpart it names. I read both, plus
`document-harness/REVIEW.md`, plus `HARNESS-DECISIONS.md` `§live` in full — **eleven entries**
(`HD-69` `HD-66` `HD-65` `HD-62` `HD-59` `HD-41` `HD-36` `HD-35` `HD-34` `HD-23` `HD-9`),
unchanged by this range; `HD-70`'s flip happened inside `§implemented`.

**Budget (`E9`).** One FULL, at most one user-approved fix, one targeted VERIFY. No FULL has
occurred for this round: no `v3-review-full-*` record exists in
`migration/document-work-assurance-v3/` for any of this range's six shas. So everything in the
range is pre-submission and consumes nothing, exactly as the four bodies claim, and **this
review is the round's one FULL**. `E9`'s no-commit-inside-the-window clause holds for the read:
`d0d029a`'s parent is `73bfe1e`, the tip at which the read was dispatched, so nothing landed
between dispatch and record.

**Authorization ceiling (`R7`, `R4`).** The user's "ok" at the `E11` card, the four rulings, the
disposition instruction ("1 入 bank 2 用 3 记录 4 转") and the `HD-63` class confirmation are
recorded only as the orchestrator's own statement in the plan, the journal and the commit
bodies. That is this repository's settled position — the ledger's 2026-08-21 ruling declines to
build an approval carrier on the ground that an in-repo "the user approved" is a claim and never
evidence — so I state the ceiling and do not treat it as a finding. Everything the rulings
authorize is nonetheless written down before the work, which is what makes the boundary
checkable at all.

**Boundary.** The plan's *Change boundary* lists two adds, three edits and, conditionally on
ruling 2, five more paths including the contract. Every path in section 1 is inside it. Ruling 2
("Boundary grows by the five paths the *Change boundary* lists for it") is what reconciles that
list against the same section's general "Not touched: any `E10` member", and `4020efa`'s body
states the reconciliation rather than assuming it. I agree with the reading: a specific
conditional grant and a general exclusion in the same section, with a ruling naming the grant,
resolves the way the round resolved it.

**Acceptance 4, re-measured** — the criterion as the plan writes it forward:

```
$ git diff --stat 8ecc7a5 3deb304 -- <the seven E10 member paths>
 contract/Document-Work-Assurance-Contract-v4.md | 16 +++++++++-------
$ git diff --stat 05ae1b6 3deb304 -- <the seven E10 member paths>
 contract/Document-Work-Assurance-Contract-v4.md | 16 +++++++++-------
 document-harness/REVIEW.md                      |  2 +-
```

Two member changes over the round, both declared before I looked and neither discovered: the
contract by the authorised `4020efa`, `REVIEW.md:129` by the disposition's free-channel
application. Declared, not discovered — met.

## 3. The implementation, led with

### 3.1 The manifest and the step — sound, and I ran it

`document-harness/product-tier.txt` is fifteen lines, LF, no leading slash, directories with a
trailing slash, and it lists itself. Re-measured at the tip, output pasted (`E3`):

```
$ git ls-files -- <the manifest's 15 lines> | wc -l
61
$ git ls-files | wc -l
443
```

Per row of `CONSTRUCTION-INDEX.md`'s product-run table, measured one row at a time:
row 1 = 1, row 2 = 15, row 3 = 5, row 4 = 1, row 5 = 2, row 6 = 2, row 7 = 22, row 8 = 4 + 8,
row 9 = 1. Sum 61. Every *Files* cell in the table is right, and the header's **61 / 443** is
right at this tip as well as at the tip it was measured on. The movement paragraph checks out
too: `git ls-tree -r --name-only 8ce93f7 | wc -l` = 421, `git diff --diff-filter=A --name-only
8ce93f7 4d2bf42 | wc -l` = 22 with 0 deleted, and 421 + 22 = 443 — 20 before this commit, 2 in
it, which is what the paragraph says.

The tier is import-complete and I checked the reason rather than the symptom:
`git ls-files tooling/rsclib/ | grep -v document_harness/` is empty and `git ls-files schema/ |
grep -v document-assurance-v3/` is empty, so nothing under either prefix falls outside a manifest
line; every `import` in `tooling/rsclib/document_harness/*.py` resolves to stdlib, `jsonschema`,
`referencing`, or the package itself. `python tooling/dtw.py --help` exits 0.

`document-harness/ONBOARDING.md` gains item 1b as item 1's second half, not an eleventh item.
The premise holds: `document-harness/README.md:25` says "ten items" and enumerates nine
labels covering ten (instance files = items 3 and 4), so a sub-item leaves the member's sentence
true and the amendment channel unopened. `grep -c 'Nine items'` = 0, `grep -c 'product-tier.txt'`
= 2 in ONBOARDING and 3 in the index — all three as claimed. The 1b Owner cell names `HD-66` and
`HD-34` and no plan, which is what keeps it out of rider `onboarding-carries-construction`'s
class; that arm is touched and correctly not redeemed.

### 3.2 The guard — mutation-tested, and it binds (`R8`, `E4`)

`tooling/tests/document_harness/test_product_tier_manifest.py` holds five assertions across four
classes. Its expectation for the manifest comes from `CONSTRUCTION-INDEX.md` — a different file
from the one guarded — and its four construction-side paths are a hand-written literal, each
asserted *tracked in the clone's index* in the same breath as it is asserted absent from disk,
so absence cannot be satisfied by a path that stopped existing. That is `E5` met on both sides.

I ran the mutations myself rather than accepting the pasted ones. Because a `git clone` to a
scratch path outside this repository is not available in this session, I mutated the guard's two
readers (`manifest_lines`, `where_tokens_from_index`) instead of the bytes on disk — the same
inputs the assertions would have seen had the files been edited, and no tracked file was written.
Probe at `.harness/review-mutation-probe.py` (gitignored, deleted after the run); output verbatim:

```
baseline manifest lines : 15
baseline index tokens   : 15

control: unmutated, all five assertions                    GREEN  (0 failing)  as expected
M3: misspell a manifest path -> (a)                        RED    (1 failing)  as expected
M1: drop a manifest line -> (b)                            RED    (1 failing)  as expected
M4: corrupt an index *Where* token -> (b)                  RED    (1 failing)  as expected
M5: repeat an index *Where* token -> (b2)                  RED    (1 failing)  as expected
M6: manifest drops its own path -> (c)                     RED    (1 failing)  as expected
M2: append CONSTRUCTION-LEDGER.md -> (d)                   RED    (1 failing)  as expected
control again: readers restored                            GREEN  (0 failing)  as expected
```

Six mutations, six reds, controls green on both sides. The end-to-end case is real: it clones
this repository `--no-checkout`, feeds the manifest to `sparse-checkout set --no-cone --stdin`,
checks out, and compares what is on disk against what `git ls-files` matches from the same lines
— the two consumers against each other, which is the property the whole design turns on. The
parse fails safe in the directions I probed: a changed heading raises, a skipped row leaves the
token sets unequal, a non-path in a *Where* cell turns (a) red.

`E4`'s "never trust a guard you have not seen fail" is satisfied for this guard.

### 3.3 Battery and guards, re-run at this tip

```
$ python -m pytest tooling/tests -q
961 passed in 166.57s   (exit 0)
$ python tooling/hooks/layer_path_check.py   ; echo $?     -> 0
$ python tooling/ledger_cap_check.py         ; echo $?     -> 0
$ python tooling/announced_path_disclosure.py --before 05ae1b6… --after 3deb304…
  every announced path changed in this range is named by the commit that changed it   (exit 0)
```

961 = 956 + 5, none removed, as claimed. The ledger holds twelve top-level entries against a
bound of twenty and the cap check passes. `HARNESS-RIDERS.md` is 50 lines and
`grep -c 'protected-set-says-five'` returns 0 — the row is deleted in the commit that pays it
(`R10`), and the two touch records ride the commit whose change they record rather than a
commit of their own.

`E2`'s disclosure is mechanically complete over the whole range. `E2` itself says what that is
worth: "that a body names a path is mechanically decidable, and being decidable is the whole of
what it certifies — it says nothing about whether what the body says about that path is true".
`B-1` is exactly the residue that clause leaves to this review.

### 3.4 The disposition's free-channel application — correct

`document-harness/REVIEW.md:129` now reads "the whole dispatched subject — the committed control
plane as floor, and the tree at the pinned revisions", byte-for-byte the read record's supplied
replacement (`v3-cold-read-73bfe1e.md`, L-2, *The exact bytes*). `E10`'s free channel admits it:
the record supplies the exact bytes, the finding is below must-fix, and the design test does not
fire — the new cell adds no clause and changes no requirement, because `REVIEW.md`'s own *When
the subject is one commit* section already states both facts it now carries ("the committed
control plane is the guaranteed minimum, never a bound on what you may read at the pinned
revisions", `:113`). The reliance test also holds: the cell named a form the same file declares
retired, so no round's outcome could have turned on it. The owed independent re-read is recorded
in both the commit body and the journal as riding the next read of this layer.

## 4. Findings

### `B-1` (BLOCKER) — the commit that took one false statement about the protected set out of the signed contract put another one in, and the signature entry certifies a class claim the tree refutes

**Where.** `contract/Document-Work-Assurance-Contract-v4.md:335-340`, written by `4020efa`;
`CONTRACT-V4-SIGNATURE.md:186-217`, the ninth post-signature entry, same commit; and the same
false count standing unfixed at `assurance/templates/run-v2/README.md:80-82`.

**What the contract now says** (`:335-340`):

> **Two protected fields have a live write path**: of the six, `review_ref` and
> `bind_authorization_ref` are authored by `assurance/templates/run-v2/` (`run_bind_v2.py`); the
> other four are written by hand-authored run scripts, which this policy governs but no shipped
> template exercises — end-to-end demonstration covers two fields, unit tests the rest.

**What is true, measured at this tip:**

```
$ grep -rn -A2 "pointer_for(" assurance/templates/run-v2/ --include=*.py
run_bind_v2.py:252:  review_ref=assurance_state.pointer_for("review_ref", review_path, repo),
run_bind_v2.py:530:  bind_auth_ref = assurance_state.pointer_for(
run_bind_v2.py-531-      "bind_authorization_ref",
run_bind_v2.py:653:  final_ref = assurance_state.pointer_for(
run_bind_v2.py-654-      "final_decision_ref", f"{CONTROL_ROOT}/control/user-decision-final.json", REPO)
run_bind_v2.py:698:  assurance_candidate_ref=assurance_state.pointer_for(...)      # unprotected
run_evidence_v2.py:391,393,395,397:  fulfillment/manifest/check_results/coverage    # unprotected
run_repair.py:105:   repair_decision_ref=assurance_state.pointer_for(
run_repair.py-106-      "repair_decision_ref", f"{CONTROL_ROOT}/control/user-decision-repair.json", REPO),
```

**Four** of the six protected fields have a live write path in the shipped template, not two:
`review_ref`, `repair_decision_ref`, `bind_authorization_ref`, `final_decision_ref`. Only
`work_spec_ref` and `start_decision_ref` have none. Each of the four reaches disk:
`run_repair.py:103-110` passes its pointer to `flow.advance_checked` and then
`assurance_state.save`; `run_bind_v2.py:696-712` passes both `bind_auth_ref` and `final_ref` to
`assurance_state.advance` and then `save`. Both are also exercised end to end, not by unit tests
alone — `tooling/tests/document_harness_review/test_run_v2_template_repair.py:208` invokes
`run_repair.py` through `subprocess.run` and `:269`
(`test_with_emit_the_state_advances_and_carries_the_decision_pointer`) asserts the written
state carries `repair_decision_ref`. So "the other four … no shipped template exercises" and
"end-to-end demonstration covers two fields" are false in the same sentence as the count.

**Why the round's own class scan did not catch it.** `4020efa`'s body pastes an `HD-41` ④ scan
whose pattern is `(five|four|six)` near `digest-protected|protected field|…`. That pattern finds
the sites but measures only the *cardinality of the set*; nothing in the commit ran a command
over the write paths, which is the sentence's other claim. `E3`'s last clause is the one that
binds here — "a factual assertion written into instruction text runs the command that could
falsify it first, output kept in the commit body or the round journal" — and the contract is
instruction text by `E10`. One `grep -n pointer_for assurance/templates/run-v2/*.py` would have
falsified it. `E7` is the second: the reported instance was the count five→six; the class is
statements about the protected set that `97cc298` falsified, and `97cc298` added **two**
`pointer_for` call sites to `run_bind_v2.py`, not one — `bind_authorization_ref` at `:530` and
`final_decision_ref` at `:653`, confirmed by
`git log -S'"final_decision_ref", f"{CONTROL_ROOT}/control/user-decision-final.json"' --
assurance/templates/run-v2/run_bind_v2.py` → `97cc298`. The round closed one and left the other.

**The second half, and why it is a governance defect rather than a typo.** The signature entry
asserts: *"Both sentences were true when v4 was signed on 2026-08-23 and were made false
elsewhere"*, and rests the whole authorisation on that — `HD-63` covers "签字文本里「签署时为真、
后来变假」的字面". Measured at the v4-creating commit:

```
$ git log -1 --format='%h %ad' 23ca45b
23ca45b Sun Aug 23 16:31:31 2026 +1000        (V3-CONTRACT-V4-v1)
$ git show 23ca45b:assurance/templates/run-v2/run_repair.py | grep -n pointer_for
91:        repair_decision_ref=assurance_state.pointer_for(
$ git show 23ca45b:contract/Document-Work-Assurance-Contract-v4.md | sed -n '325,329p'
  **Only one protected field has a live write path**: of the five, only `review_ref` is authored
  by `assurance/templates/run-v2/` … no shipped template exercises …
```

`run_repair.py` was in the shipped template, writing `repair_decision_ref` through `pointer_for`,
on the day v4 was signed. Site 2 was therefore **already false at signing** with respect to
`repair_decision_ref` — that half is not `HD-63`'s class at all. It is the class the bank's
`enum-single-home` row already names ("a signed statement false at signing is a new class"), and
that row is banked precisely because it needs a family ruling or a v5 successor rather than an
in-place write. So part of `4020efa`'s in-place edit of signed text stands on an authorisation
whose stated class does not reach it, and the signature record certifies otherwise.

**The decision that goes wrong** — the same test the rider itself used, applied to what replaced
it. A caller or a run author reading §13.2 to learn who may author the digest-protected pointers
concludes that `repair_decision_ref` and `final_decision_ref` are written only by hand-authored
run scripts and that no shipped template exercises them. It then hand-authors a write that
`run_repair.py` and `run_bind_v2.py` already perform — the "run authored by copying an existing
precedent" failure the same paragraph warns about, two sentences earlier — or reasons about the
protected-pointer authoring boundary from a count that is half the real one. An actor's action,
so not wording-level (`R9`); a false statement in a signed `E10` member, so not a low.

**Minimum fix.**

1. `contract/Document-Work-Assurance-Contract-v4.md:335-340` — state the measured fact: four
   protected fields have a live write path (`review_ref`, `repair_decision_ref`,
   `bind_authorization_ref`, `final_decision_ref`), authored by `assurance/templates/run-v2/`
   (`run_bind_v2.py` and `run_repair.py`); the two without one are `work_spec_ref` and
   `start_decision_ref`. Drop or correct the "no shipped template exercises" and "covers two
   fields" clauses with it — they are the same assertion from the other side.
2. `assurance/templates/run-v2/README.md:80-82` — the same correction, in the same commit
   (`E7`: the class is the unit; this site was examined by `4020efa`'s scan and passed as
   already-correct, and it is not).
3. `CONTRACT-V4-SIGNATURE.md`'s ninth entry — corrected forward (`HD-59`), not rewritten: the
   `repair_decision_ref` clause of site 2 was false at signing, so that part is outside the
   class the entry claims. **Whether that half is written at all is the user's**, and the two
   routes are the ones the `enum-single-home` row already sets out — a new
   `HD-63`/`64`/`67`/`68`/`70`-family ruling admitting "false at signing" for this instance, or
   a correction confined to what `HD-63` does reach (`final_decision_ref`, falsified by
   `97cc298`) with the older falsity disclosed and banked. I name the fact and the two routes;
   the choice is not the reviewer's (`R5`, and `HD-63`'s family is the user's).
4. The fix commit pastes the command that could falsify its own assertion (`E3`):
   `grep -rn "pointer_for(" assurance/templates/run-v2/*.py`.

### `L-1` (low, non-blocking) — the guard omits the one property ONBOARDING 1b calls the check that matters

`ONBOARDING.md:97`'s *See* cell says: "`python tooling/dtw.py --help` still exits 0, **which is
the check that matters**: the tier is import-complete, so narrowing the tree did not break the
CLI." The committed guard does not carry that. Test (d) builds the narrowed clone and compares
the two consumers on it, then throws the clone away without ever running the CLI inside it. The
property was established once, by hand, by the executor at `4020efa`, and by me at this tip —
and by nothing thereafter.

What goes wrong if it stays: the two-copy drift the guard *does* catch is the cheap failure —
someone edits one file and not the other, and (b) turns red. The expensive one is a module added
under `tooling/` outside every manifest line, or a new third-party import; the manifest and the
index still agree, (a)–(d) stay green, the battery stays green, and the failure first appears in
a caller, after a gitlink bump, as a `ModuleNotFoundError` from `dtw` that reads like a local
environment problem rather than a tier that stopped being import-complete. Today the tier is
complete — I measured it in §3.1 — so this is drift insurance, not a present defect.

Not a blocker: the plan's design decision 5 enumerates exactly four assertions, the user ruled
the card as put, and nothing is violated. Not new machinery either (`E6`): the clone already
exists inside the (d) case, and the assertion is one `subprocess.run([sys.executable,
"tooling/dtw.py", "--help"], cwd=clone)` on a fixture the test already builds and already tears
down.

### `O-1` (observation) — the guard binds two copies of the list to each other; the tier's boundary has one anchor, and it holds four paths

Assertion (b) is a mutual-consistency check: manifest ↔ the index table's *Where* column. Neither
side is independent of the other in the sense that matters for a *boundary* — an edit made to
both files in one commit passes. The only independent anchor on what may not enter the tier is
(d)'s hand-written four (`CONSTRUCTION-LEDGER.md`, `HARNESS-DECISIONS.md`,
`document-harness/CONSTRUCTION-CHECKLIST.md`, `tooling/construction_dispatch.py`), against a
construction-side tier that is much larger — `CONTRACT-V4-SIGNATURE.md`, `HARNESS-RIDERS.md`,
`CONSTRUCTION-INDEX.md`, `document-harness/io-design.md`, `tooling/sweep_refs.py`, `migration/`,
the journals and the plans, none of them named by any assertion.

This is defensible as designed: `CONSTRUCTION-INDEX.md` declares its *Where* column the
definition of the tier, so a row deliberately added to both files **is** the tier changing, and
a guard that refused it would be guarding against a decision rather than a drift. Whether the
boundary should have an anchor that a single deliberate two-file edit cannot move is a question
about whether a further component should exist, which is `R5`'s and the user's, not mine. Recorded,
not concluded.

### `O-2` (observation) — the round's own class-scan pattern generalized over phrasing, not over the change that caused the defect

`B-1`'s mechanism is worth separating from `B-1`'s bytes, because it is the reusable part. The
`HD-41` ④ scan in `4020efa` was built from the *finding's wording* (`five|four|six` near
`protected`) rather than from the *commit that created the class* (`97cc298`). Scanning from the
wording finds every sentence that says a number; scanning from the cause — "what did `97cc298`
change that any standing text might assert?" — would have surfaced its two new `pointer_for`
call sites and the sentences that count them. The round found and edited the right lines and
still wrote a false one, which is a scan that located the sites without measuring them.

Whether `HD-41` ④'s scan discipline should say anything about deriving the pattern from the
falsifying change rather than from the finding's phrasing is a rule question and therefore the
user's (`R5`). Recorded here rather than banked (`CONSTRUCTION-LEDGER.md`'s header: an `R5`
observation is routed to the user at preclear, never filed by the session that received it).

## 5. Boundary check — process and record conformance, run second

| obligation | held? | how established |
|---|---|---|
| `E9` budget — one FULL, no prior spend | yes | no `v3-review-full-*` record for any sha in the range; every body classifies itself pre-submission |
| `E9` read window — no commit but the record between dispatch and record | yes | `d0d029a`'s parent is `73bfe1e`, the dispatched tip |
| `E9` FULL window — nothing lands after dispatch | yes | tip == dispatched tip; marker timestamp 10 s after the tip commit |
| `E8` staged paths, new commits, no push, in-boundary, `V3-…-v1` titles, dense body, kind named | yes | six commits, all titled `V3-…-v1`, all kinds named, no merges, no trailers |
| `E2` disclosure of announced paths | yes, mechanically | `announced_path_disclosure` exit 0 over the whole range; what that certifies is bounded by `E2`'s own clause, and `B-1` is the residue |
| `E3` measure-last, paste output | **no, at one site** | every figure in `4d2bf42` and `4020efa` re-ran and matched; the assertion `B-1` names had no falsifying command run |
| `E5` guard expectation independent of the guarded thing | yes | expectation parsed from `CONSTRUCTION-INDEX.md`; four construction paths a hand-written literal |
| `E4` / `R8` mutation-tested guard | yes | six mutations red, two controls green (§3.2) |
| `E7` defect class not instance | **no** | §4 `B-1`: the class scan closed on the reported phrasing |
| `E10` opening cold read of the layer + `§live` | yes | read record `d0d029a`, eight files end to end, 0 must-fix; `§live` eleven entries, unchanged |
| `E10` free channel for the read's L-2 | yes | §3.4 — bytes exact, no clause added, no reliance, re-read recorded as owed |
| `E10` membership question for a new governance-adjacent file | yes | recorded and answered in `4d2bf42`'s body and plan decision 7 |
| `E12` one SHA / range handoff | yes | freeze marker carries the range and nothing else |
| `R10` rider routing | yes | `protected-set-says-five` row deleted in the paying commit; two touch records not redeemed and both say why; `verify-specgap-precedence` banked with both targets and a deadline outside this round |
| ledger admission and cap | yes | twelve top-level entries, `ledger_cap_check` exit 0; the new entry is a pointer, not a narrative |
| `E1` / `R1` independence | declared, not verifiable | see ceilings below |

## 6. Coverage, and the honesty ceilings

**Read in full:** `document-harness/CONSTRUCTION-CHECKLIST.md`, `document-harness/RULES.md`,
`document-harness/REVIEW.md`, `CONSTRUCTION-LEDGER.md`, the round plan, the round journal,
`document-harness/ONBOARDING.md`, `CONSTRUCTION-INDEX.md`,
`tooling/tests/document_harness/test_product_tier_manifest.py`,
`document-harness/product-tier.txt`, all six commit bodies, and the complete diff of the range
for every file except the two long records.

**Sampled:** `HARNESS-DECISIONS.md` (`§live`'s eleven entry headings and the `HD-70` diff in
full; the `HD-63` entry's heading, not its body in full), `HARNESS-RIDERS.md` (the four rows
touched by this range, not all 50 lines), `v3-cold-read-73bfe1e.md` (its L-2 section verbatim
and its finding summary, not the whole 344 lines), `assurance/templates/run-v2/run_bind_v2.py`
(lines 505-574 and 630-727), `assurance/templates/run-v2/README.md` (lines 60-140),
`contract/Document-Work-Assurance-Contract-v4.md` (§13.2 and the diff; not the whole contract).

**Probed only:** the rest of `tooling/rsclib/document_harness/` (import surface by grep, not by
reading), `test_run_v2_template_repair.py` (its subprocess call and test names, not its bodies),
the historical commits `8ce93f7`, `23ca45b`, `97cc298`, `345acdd`, `39a21a8` (targeted
`git show` / `git log -S` only).

**Ceilings, stated rather than papered over (`R4`):**

- **Process claims have no evidence lock.** That the executor and the cold reader were separate
  `claude -p` sessions on `opus` with web tools disabled, at the session ids, turn counts and
  wall-clock the journal records; that the read record was committed unchanged as returned; that
  the `E1` statement's "the executor holds none of `R1`'s four holdings" is true — all of these
  are declared identities, and I mark them, I do not verify them.
- **The user's rulings are the orchestrator's own record of them.** §2 states why that is this
  repository's settled position and not a finding.
- **The mutation test replaced the guard's readers rather than the bytes on disk.** No scratch
  path outside this repository was writable in this session and `git clone` was not available to
  me, so I could not mutate the tracked files and restore from sha256-checked copies as `E4`
  prescribes. The inputs the assertions saw are identical either way, and I say so rather than
  claim the byte-level form.
- **The step was exercised on a clone of this repository, never inside a real submodule.** Test
  (d) and the executor's probe both narrow a plain clone. That `git sparse-checkout set --no-cone
  --stdin` behaves the same inside a submodule checkout, and that a gitlink bump followed by
  re-running the set works as ONBOARDING 1b describes, is **`UNVERIFIABLE` here** — no second
  caller exists in this range to walk it.
- **`dtw --help` proves import-completeness, not functional completeness.** No `dtw` subcommand
  other than `--help` was executed against a narrowed tree, by the round or by me.
- **One review round is bounded by one context.** I did not read the whole contract, the whole
  rider bank, or the whole read record; a reader who treats `REVIEWED_NO_BLOCKER` on the parts I
  did read as coverage of the parts I did not will over-trust this verdict — which is moot here,
  since the verdict is `CHANGES_REQUIRED`.

## 7. What the verdict means

`CHANGES_REQUIRED`: one blocking discrepancy was found within this subject and these review
dimensions. It is not a judgment on the round's headline work, which I drove and which holds —
the manifest, the step, the index row and the guard all do what they claim, and the guard binds
under six mutations. The blocker is one sentence in a signed instruction-layer member and the
signature entry that certifies it, written by the one commit in the range whose purpose was to
stop that same sentence being false.

`E9`'s single repair is unspent. The fix's boundary follows from `B-1`'s minimum fix above, and
item 3 of it carries a question that is the user's to answer before the fix is written, not
after.
