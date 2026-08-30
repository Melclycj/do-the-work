# FULL review — `db1bfa1..8f6b3ef` (round `CORE-ONLY-LAYER`)

Independent FULL of round 1 of batch `CORE-ONLY`. Subject received as one range and nothing
else (`R2`); round, budget, authorization, obligations and every figure below are re-derived
from the repository, and no reported figure is accepted. Standing instruction as dispatched:
`migration/document-work-assurance-v3/v3-harness-review-contract.md`, read first, then the
file it names — `document-harness/CONSTRUCTION-CHECKLIST.md` — and then the counterpart *that*
file names, `document-harness/RULES.md`. That third hop is not in the dispatched chain's own
description, which is blocker **B-1** below.

**Verdict: `CHANGES_REQUIRED`.** 2 blockers, 5 lows, 4 observations.

Both blockers are text-level, non-design, and fit one repair leg. Neither touches an announced
path. Neither is about whether the round's design is right — that question is not mine (`R5`);
both are about a statement this layer now makes that the repository contradicts.

---

## 1. Subject, re-derived

```
$ git rev-parse HEAD
8f6b3ef0467f5cfe77b590c4da399eb322d1285d
$ git status --porcelain
?? .goals/
$ git rev-list --count db1bfa1..8f6b3ef
23
$ cat .harness/review-pending.json
{
 "subject": "db1bfa1f78df8f26c634918d1ca1a444861877d4..8f6b3ef0467f5cfe77b590c4da399eb322d1285d",
 "dispatched_at": "2026-08-30T01:34:56+00:00"
}
```

The marker carries exactly this range; the branch tip is the range tip, so `E9`'s window holds
and nothing but this record is owed to it.

Twenty-three commits, classified by hand from their own bodies and diffs — no reported list
used:

| kind | commits |
|---|---|
| plan / round-open | `257235b` |
| ruling (orchestrator) | `a542c6d` `eecca7e` `ff3c37f` `5f4ce81` `d6221bd` `8532979` `8f6b3ef` |
| record (opening cold read) | `ac39d35` |
| candidate | `cbaee8e` `4b81dd9` `228df32` `eadcfe0` |
| pre-submission correction | `b235701` `322fd1c` `70839b1` `40f20eb` `110924f` `360cff5` `02bb0bc` `2f6743e` `0290eb9` `a5b1dc2` |

Every one of the twenty-three names its kind in its own first sentence (`E8`), checked by
reading each body. Titles are `V3-CORE-ONLY-LAYER-<what>-v1` — the round name is in every
title, which is what `E8` asks.

Tracked-file counts per commit, measured rather than cited:
`db1bfa1` 410 · `257235b`/`a542c6d` 410 · `ac39d35`/`eecca7e` 411 · `cbaee8e` 414 ·
`4b81dd9`…`228df32` 415 · `eadcfe0`…`8f6b3ef` 416.

## 2. Round, budget, authorization, obligations — re-derived

**Round.** `CORE-ONLY-LAYER`, round 1 of three, from `document-harness/plans/core-only.plan.md`'s
status block: opened 2026-08-29, `base_commit` `db1bfa1`, which is the range base I was handed.

**Budget (`E9`).** One FULL, at most one user-approved fix, one targeted VERIFY. Spend at
dispatch: **virgin**. The opening cold read `ac39d35` is an `E10` read, not a round, and spends
nothing; the ten pre-submission corrections each state in their own body that no valid
independent FULL has occurred, which is the correct test and the correct conclusion — I confirm
it independently: no `v3-review-full-*` record exists for any commit in this range. This FULL is
the first spend.

**Authorization.** Thirty rulings carried in the plan (its *Rulings* section is the declared
carrier, so they are committed and not chat-only — `R2` satisfied on that axis), plus `HD-67`
and `HD-68` in `HARNESS-DECISIONS.md` `§live`, both landed inside the range. `HD-67` carries its
own forward correction under `HD-59`. Ruling 13 cuts the batch: this round is items A, B, E, G,
the guards' half of H, and I; item J joined by ruling 24; items C, D and the dispatch half of H
are round 2's; item F is round 3's, in a caller.

**Obligations.** The plan's twelve acceptance items, of which 1, 2, 3, 5, 7, 9, 10, 11 (guard
half) and 12 are due now; 4, 6, 8 and 11's dispatch clause are later rounds'.

## 3. Implementation (`R3`, run first)

### 3.1 The rule split is byte-preserving, and I measured it rather than reading the claim

`4b81dd9`'s body claims a byte-preserving move with exactly two rules changed. I re-derived it
independently: extracted every `- **E<n>** / - **R<n>**` block from
`db1bfa1:document-harness/CONSTRUCTION-CHECKLIST.md` and from the two landed files, and compared
block by block.

```
old ids: E1..E12, R1..R10  (22)
new ids: E1..E12, R1..R10  (22)
E1 IDENTICAL(1951)  E2 IDENTICAL(2290)  E3 IDENTICAL(664)   E4 IDENTICAL(230)
E5 IDENTICAL(250)   E6 IDENTICAL(419)   E7 IDENTICAL(58)    E8 IDENTICAL(413)
E9 IDENTICAL(758)   E10 DIFFERS         E11 IDENTICAL(180)  E12 IDENTICAL(534)
R1 IDENTICAL(356)   R2 IDENTICAL(267)   R3 IDENTICAL(766)   R4 IDENTICAL(303)
R5 IDENTICAL(272)   R6 DIFFERS          R7 IDENTICAL(118)   R8 IDENTICAL(175)
R9 IDENTICAL(479)   R10 IDENTICAL(2112)
```

Twenty of twenty-two byte-identical; the two that differ are exactly the two the commit body
discloses, and their diffs are exactly what it describes. No rule was lost, none gained, none
silently re-typed. Twenty-one live in `RULES.md`; `E2` alone stays in
`CONSTRUCTION-CHECKLIST.md`, with `R6`'s instance value beside it under a *Review side* heading.

### 3.2 The membership sentence and its three mirrors agree

`E10`'s nine paths, read out of `RULES.md`, against `LAYER` read out of the guard:

```
LAYER n=9 — every one exists in the working tree:
  document-harness/RULES.md · README.md · EXECUTION.md · REVIEW.md · ORCHESTRATION.md
  migration/document-work-assurance-v3/v3-harness-operating-contract.md
  migration/document-work-assurance-v3/v3-harness-review-contract.md
  contract/Document-Work-Assurance-Contract-v4.md
  schema/document-assurance-v3/paragraph-map.schema.json
```

Same nine, same order, in `E10`'s sentence. `EXPECTED` in `test_precommit_checks.py` and
`MEMBER` in `test_precommit_hook.py` moved with them and are still hand-written literals, not
imports of the guarded constant (`E5` holds).

### 3.3 The guards bind — mutation-tested here, not taken from the journal (`R8`, `E4`)

I ran two mutations of my own, each restored by copy from a sha256-checked scratchpad, never
`git checkout --`:

```
$ sha256sum tooling/hooks/layer_path_check.py
a3e182dde034aff7e2c392bcbddc2e16922d392d3a0ec6bdbf3d6af3671d81d8
# scanned_paths neutered to `return LAYER`
$ python -m pytest tooling/tests/document_harness/test_harness_config.py -q
4 failed, 17 passed
  ScannedSurface::test_a_declared_rule_joins_the_scanned_surface
  GuardReadsTheDeclaration::test_a_dangling_path_in_a_declared_rule_is_blocked
  GuardReadsTheDeclaration::test_a_malformed_declaration_stops_the_guard_rather_than_emptying_it
  SweepReadsTheDeclaration::test_a_declared_rule_file_is_swept
# restored from the checked copy
$ sha256sum tooling/hooks/layer_path_check.py
a3e182dde034aff7e2c392bcbddc2e16922d392d3a0ec6bdbf3d6af3671d81d8
$ python -m pytest tooling/tests/document_harness/test_harness_config.py -q
21 passed
```

The three must-fire cases go red and the two *undeclared is not blocked / not swept* negative
controls stay green in both states — so the pair proves the declaration is load-bearing, not
that the tests merely touch the code.

Second mutation, end-to-end on a **fresh caller built from the harness-only tree** rather than
on this repository, which is the shape acceptances 11 and 12 actually claim:

```
$ python <harness-only>/tooling/dtw.py init --repo-root .     # in a fresh git repo
RESULT: 6 created, 0 left as found (exit 0)
# docs/MY-RULES.md staged, carrying a backticked path that resolves nowhere
rules=['docs/MY-RULES.md'] -> exit 1
  pre-commit BLOCKED: ... docs/MY-RULES.md: `docs/no-such-rule.md` — resolves nowhere ...
rules=[]                   -> exit 0
```

Same repository, same staged bytes, one field changed. The guard reads the declaration.

### 3.4 `harness.json` and its readers

`load_harness_config` refuses loudly on unreadable or wrongly-typed input and returns the empty
declaration when the file is absent — the right split, and the docstring's reason (a typo that
quietly emptied `rules` would stop both instruments while every check stayed green) is the real
failure mode. Unknown-field rejection is the part I would have expected to be missing and it is
present and tested. `render_harness_config` is pinned by hand-written bytes in two modules
(`E5`).

Three of `E10`'s four named readers exist and work: `layer_path_check` (with the sweep riding on
`scanned_paths`), the orchestrator (`ORCHESTRATION.md` now names `policy` as a discovery path),
and `dtw init`. The fourth, `dtw dispatch`, does not — see observation **O-1**.

### 3.5 Acceptance, re-measured

Every figure below is my own run at the subject tip, immediately before writing this section.

```
$ python -m pytest tooling/tests -q
853 passed in 178.58s                                   # acceptance 7 — exit 0
$ python tooling/sweep_refs.py
-- 13 caller-held or unresolvable references over 10 members and declared rule files
$ python tooling/sweep_refs.py <harness-only tree>
-- 33 caller-held or unresolvable references over 9 members and declared rule files
$ python tooling/hooks/layer_path_check.py      -> 0
$ python tooling/hooks/candidate_path_check.py  -> 0
$ python tooling/hooks/review_freeze_check.py   -> 0   # acceptance 9
$ python tooling/announced_path_disclosure.py --after 8f6b3ef --before db1bfa1
  23 non-merge commit(s) judged
  every announced path changed in this range is named by the commit that changed it
```

The harness-only tree is my own, built with `git archive 8f6b3ef` over the eight product-tier
rows and made a git repository: **59 files**, which is the tier count `CONSTRUCTION-INDEX.md`
states. On it:

```
$ python tooling/dtw.py --help                  -> 0
$ python tooling/hooks/layer_path_check.py      -> 0
$ python tooling/hooks/candidate_path_check.py  -> 0
$ python tooling/hooks/review_freeze_check.py   -> 0
$ python <harness-only>/tooling/dtw.py init --repo-root <fresh repo>
                                                -> 0, harness.json written empty
                                                       # acceptance 3, 11 first half
$ grep -rn 'CONSTRUCTION-CHECKLIST' <harness-only tree>
tooling/rsclib/document_harness/dispatch.py:776         # acceptance 5 — the one line item C owns
```

The thirteen sites on this repository are all the compliant caller-held bare-name form plus the
contract's one past-tense history site, which ruling 19's holder-or-history clause now covers — I
read `contract/…-v4.md:275-282` and the clause is there. The thirty-three on the stripped tree
resolve into: four that are item D's (two stub `PATHTOK`s at `RULES.md:87`/`:88`, two `MISSING`
stub members), twenty-eight caller-held bare names, and one that is neither — see low **L-1**.

Acceptance 10 holds: rider `checklist-cited-not-carried` is deleted in `4b81dd9`, the commit that
earns it; `sig-write-once` in `228df32` and `contract-wikilink-tier` in `322fd1c`, each in the
commit that spends its authorization. Five rows leave in total and I diffed the id set to confirm
no sixth row vanished quietly.

### 3.6 The contract and the schema pack — the announced surface

Three contract commits and one schema commit change announced paths. Each names its paths site by
site in its own body, and `announced_path_disclosure.py` confirms the whole range mechanically
(above). I read the full contract diff against the disclosures: the removals are the
merged-sources paragraph, §12 ¶1 and ¶2, the wikilink's parenthetical, and the two stale
literals; the survivals are §12's *Removed from the v3 default interface* paragraph and the
`SPEC_GAP` sentence about plan §2 — exactly what `HD-67`, ruling 22, `HD-68` and `HD-63`
authorize, no more. `CONTRACT-V4-SIGNATURE.md` gains three append-only blocks (fifth, sixth,
seventh post-signature writes) and rewrites none of the four above them; the signed blob is not
re-pointed, which is what ruling 20's `O-1` disposal requires. The schema edit is two description
lines with no structural change, and the pack still parses.

## 4. Blockers

### B-1 — two instruction-layer members still say the construction checklist carries all twenty-two rules, and one of them is the standing instruction every dispatched construction reviewer reads first

**Location.** `migration/document-work-assurance-v3/v3-harness-review-contract.md:3` and
`migration/document-work-assurance-v3/v3-harness-operating-contract.md:3`. Neither file was
touched by this round (`git log db1bfa1..8f6b3ef --` over both returns nothing).

**What they say.** Review-side stub: *"superseded by `document-harness/CONSTRUCTION-CHECKLIST.md`,
which carries both sides in one file: R1–R10 review, E1–E12 execution … It is your standing
instruction and its own counterpart; read all of it."* Operating-side stub: the same sentence
with the two halves reversed.

**Ground truth it violates.** `document-harness/RULES.md`'s own header and `E10`'s membership
sentence, both landed in this range: twenty-one of the twenty-two rules now live in `RULES.md`;
`CONSTRUCTION-CHECKLIST.md` carries `E2` and one `R6` instance value, is no longer an
instruction-layer member, and is no longer its own counterpart. Both stubs *are* members (`E10`
names them as paths 6 and 7), so this is a member stating a falsehood about the layer.

**Failure scenario, and it is not hypothetical — it is this session.**
`dispatch.CONSTRUCTION_ROLE_INSTRUCTION` (`tooling/rsclib/document_harness/dispatch.py:549`)
substitutes the review-side stub into `CONSTRUCTION_PROMPT` as `{charter}`, so it is the first
file a dispatched construction reviewer opens. It told me my standing instruction carried
`R1`–`R10`. The file it named carries `R6`'s instance value and nothing else of the review side.
I reached the actual rules only because `CONSTRUCTION-CHECKLIST.md`'s rewritten header names its
counterpart — a link the stub does not describe and does not know about. A reviewer that took the
stub at its word, opened the checklist, found `E2` plus one `R6` value and concluded the mount
was broken or the layer had been gutted would be acting reasonably on what a member told it.

**Minimum fix.** Both lines name the real carrier. For the review-side stub, replacing the first
sentence with content of this shape is enough — no rule changes, no clause added, so it is not
design:

> 2026-07-27 superseded by [`document-harness/CONSTRUCTION-CHECKLIST.md`](../../document-harness/CONSTRUCTION-CHECKLIST.md),
> which since round `CORE-ONLY-LAYER` carries only what this repository obeys alone — `E2` and
> one `R6` instance value — and names [`document-harness/RULES.md`](../../document-harness/RULES.md)
> as its counterpart, where `E1`, `E3`–`E12` and `R1`–`R10` live. It is your standing
> instruction; read it and the counterpart it names.

and the same correction, mutatis mutandis, in the operating-side stub. The bytes are supplied, so
`E10`'s free channel can take this without spending the fix leg — a layer application still owing
its ride-along independent read. Note that ruling 6 makes both stubs *removable* in round 2 once
no dispatch prompt names them; that does not discharge this, because they are members today and a
round-2 removal is not guaranteed (`dispatch.py:549` is item D's own condition, and item D is not
yet done).

### B-2 — the product tier still cites `E2`, the one rule that stayed behind, and the rider that recorded exactly this defect was deleted as redeemed on a measurement whose scope excluded the file the round created

**Location.** `document-harness/RULES.md:164` (inside `E10`): *"…the standing text it never
re-scans stays unscanned; the bytes `E2` freezes are excepted while they are frozen."* And
`schema/document-assurance-v3/paragraph-map.schema.json:5`: *"…is part of the E2-frozen surface
as of the 2026-08-03 re-baseline."* Both files travel; `E2` does not.

**Measured on my own harness-only tree** — the only two hits in 59 files:

```
$ grep -rn '`E2`' <harness-only tree>
document-harness/RULES.md:164
$ grep -rnw 'E2' <harness-only tree> | grep -v '`E2`'
schema/document-assurance-v3/paragraph-map.schema.json:5
```

**Ground truth it violates.** Two things at once. (a) `CONSTRUCTION-INDEX.md`'s header, written
in this range, opens *"The gap that made the product tier an open set is closed, and the closure
is measured rather than asserted."* The closure is asserted for a scope — *"Re-measured at
`cbaee8e` over the same five documents"* — that excludes `document-harness/RULES.md`, which did
not exist at `cbaee8e` and is the sixth product-tier document and the one this round created.
(b) `R10`: redemption is the fix riding a batch that touches the surface. Rider
`checklist-cited-not-carried` recorded *"产品档五份文档反过来引它的 `E*`/`R*` 规则 … 35 处规则引用
够不着被引文本"* — a product-tier document citing a rule identifier its reader cannot resolve.
That defect still has two live instances in the product tier, and the row is gone. `E7` names
this failure mode by name: test the defect class, not the reported instance.

**Failure scenario.** A cold executor or reviewer in a caller reads `E10`'s closing clause, which
tells it that a class of bytes is excepted from what the layer guard rescans and that the
exception is defined by `E2`. It greps its whole mount for `E2` and finds a schema description
asserting that one of its own files is *"part of the E2-frozen surface"* and no rule `E2`
anywhere. It cannot tell whether the exception applies to it, whether its mount is incomplete, or
whether the numbering gap between `E1` and `E3` in `RULES.md` is a deletion it should report.
Nothing in `RULES.md` says a rule stayed behind: its header says *"Every rule below carries the
identifier it has always carried"*, which reads as a complete list. The one place the product
tier discloses the absence — `document-harness/README.md`'s `RULES.md` row, *"less the one
announced-surface rule that names this instrument's own bytes and stayed with it"* — does not
name `E2`, so the reader cannot connect the two.

**Minimum fix.** Name the residue in `RULES.md`'s own header, one sentence, adding no clause to
any rule and changing no requirement — content of this shape:

> One identifier is absent below and the gap is deliberate: `E2`, the announced-surface rule,
> binds the bytes of the instrument that owns them and stayed with it, so a repository that
> mounts this harness has no `E2` and nothing of its own is frozen by it. Where `E10` and a
> schema description mention it, they mention a rule that is not yours.

The schema site is an announced path, so editing it would owe an `E2` disclosure and a schema
touch this round has no reason to make; naming the residue in `RULES.md` closes the reader's
question for both sites without touching frozen bytes. Alternatively the rider may be re-banked
with the two measured sites as its scope — but the row must then exist again, because deleting it
while the class is live is what `R10` forbids.

## 5. Lows

- **L-1 — acceptance 1's "zero except item D" rests on a classification `E10` does not admit.**
  On the harness-only tree the sweep reports `PATHTOK document-harness/README.md:26 .githooks/`.
  The journal (§4, fourth re-measure) puts it in the list of *"the compliant caller-held form"*.
  It is not that form: `E10` says a caller-held path *"is named, never written as a path token"*,
  and this is a path token. Read the other way — as a path token, which `E10` requires to resolve
  in this repository, which `.githooks/` does — it names **this instrument's** own hook directory
  from a travelling file, which is the class acceptance 1 requires to be zero. The plan's own
  34-site table listed it as one of the two `PATHTOK`s that are *"this batch's"*, and ruling 24's
  enumeration named only the other one (`:20`, into `tooling/tests/`). So it belongs to no item:
  not J, not D, not C. **Downstream decision that goes wrong:** round 2 or the batch closeout
  declares acceptance 1 met at "four sites, all item D's" and ships a fifth. *No bytes supplied* —
  which of the two readings applies is a ruling, not a repair, so this banks rather than taking
  the free channel.

- **L-2 — `README.zh-CN.md` still describes a nine-item onboarding.** `cbaee8e` updated the five
  parallel sites in `README.md` (nine→ten, and the `dtw init` step comment gaining `harness.json`)
  and did not touch the Chinese twin, which `4b81dd9` then edited for a different reason — so the
  file was inside the round's change boundary and the counts were missed rather than deferred.
  Stale sites: `README.zh-CN.md:107` (`# 2. create .harness/, its ignore entry, and the two
  instance files`), `:140` (`九项里的五项`), `:141` (`九项按`), `:204` (`——九项，每项带…`),
  `:248` (`从这里开始：九项`). **Downstream decision that goes wrong:** a person onboarding a
  caller from the Chinese front door counts nine items, never writes `harness.json`, and gets a
  repository whose declared rules no guard scans — the exact capability this round exists to add;
  the step-2 comment also contradicts what the command actually prints. **Bytes supplied:** the
  five edits `cbaee8e` made to `README.md`, transposed — `九项里的五项`→`十项里的六项`, the three
  remaining `九项`→`十项`, and `:107`→`# 2. create .harness/, its ignore entry, harness.json, and
  the two instance files`.

- **L-3 — `tooling/rsclib/document_harness/init_target.py:5-7` says "Five of them are judgment"
  and enumerates five, while `NOT_DONE` beside it now holds six.** The round added
  `"declare the caller's own rule files in harness.json's rules field"` to `NOT_DONE` and updated
  the sentence above it from nine items to ten, but not the judgment count or its enumeration —
  and the new entry is a judgment item by the file's own definition. Before this round the
  docstring's five and `NOT_DONE`'s five matched one-for-one; the round broke that. **Downstream
  decision:** a reader deciding whether a seventh `NOT_DONE` entry belongs uses an enumeration
  that already omits one. **Bytes supplied:** *"Six of them are judgment: what the caller's policy
  file says, which rules it declares, where its pointer line goes, which guards its hook runs,
  which revision the submodule pins, and when its first journal is written."*

- **L-4 — `CONSTRUCTION-INDEX.md:27` anchors its figures to a commit where they do not hold.**
  The line reads *"**59 files** against a repository of **415**, measured 2026-08-30 at
  `cbaee8e`"*. Measured:

  ```
  $ git ls-tree -r cbaee8e --name-only | wc -l        -> 414
  $ git ls-tree -r 4b81dd9 --name-only | wc -l        -> 415
  product tier at cbaee8e -> 58 ;  at 4b81dd9 -> 59
  ```

  Both figures hold at `4b81dd9`, the commit that wrote the line — plausibly because the new
  `RULES.md` was staged when `git ls-files` was run against `HEAD=cbaee8e`. `E3` says a figure is
  invalidated by any later change to what it measures and is emitted from the command that
  produces it; an anchor naming a commit the command does not reproduce at is the same defect one
  step removed. **Downstream decision:** the next re-measure checks out `cbaee8e`, gets 414/58,
  and reports a drift that never happened. **Bytes supplied:** replace `cbaee8e` with `4b81dd9`.

- **L-5 — `document-harness/plans/core-only.plan.md:524`, step 2's box is unchecked though the
  commit that discharges it landed.** `a542c6d V3-CORE-ONLY-LAYER-HD67-RULING-v1` is the `HD-67`
  ruling commit step 2 names, and `HD-67` is in `§live`. The plan's own rule is *"Checked off as
  each lands; a box that reads done names the commit that made it so"*, and its own resume rule is
  *"a cold session reads it … then continues at the first unchecked box"*. **Downstream decision:**
  a cold session resuming by the step list writes `HD-67` a second time; the Resume pointer
  paragraph says steps 1–5e are done, so the two carriers now disagree about where the round
  stands. **Bytes supplied:** `- [x] 2. **DONE.** `HD-67` written at `a542c6d`, before the read,
  per plan ruling 18; corrected forward the same day under `HD-59` for ruling 20's `M-1`.`

## 6. Observations

- **O-1 — `E10`'s second sentence states as present fact something the code does not do, and the
  statement is now in two travelling files with no marker in either.** *"`dtw dispatch` names the
  declared files in every prompt it writes, so a cold session receives a repository's rules by the
  channel it receives its charter"* (`RULES.md`, `E10`), repeated in `ONBOARDING.md` item 10's
  **Owner** cell. Measured: `git grep` for `harness.json` across `tooling/` returns `caller.py`,
  `init_target.py`, `layer_path_check.py`, `sweep_refs.py` and their tests — nothing in
  `dispatch.py`. `4b81dd9`'s body discloses this in as many words and routes it to round
  `CORE-ONLY-CODE`, and ruling 13 authorizes the deferral, so this is not a finding against the
  round's boundary. It is an observation because the disclosure lives in a commit body while the
  claim lives in the layer, and the reader of the layer has no way to reach the disclosure. The
  harm window closes when round 2 lands, and round 3 (the first product run) is after it — so
  nothing can act on it before it becomes true. I am recording the shape, not asking for a change.

- **O-2 — five successive pre-FULL correction passes each found the next form of one defect class
  before any FULL had run.** Steps 5b–5e produced rulings 24, 26, 27, 28 and 30: product-tier
  references to instrument-held artifacts, `historical-only` survivors, `N0 record` references,
  `N0-record R1` citations in the schema pack, and bare `R1` citations in code — five scan keys
  for one class, each found by changing the key after the previous pass closed. The user stopped
  the loop at ruling 30 and routed the remainder to round 2. `R5`: whether a process that finds
  its own next instance five times before an independent read has run should keep running is the
  user's question, not mine. I report only that the shape is there, and that the sixth key (`E2`,
  blocker B-2) was still open when the loop stopped.

- **O-3 — the contract amendments took `E10`'s deferred-read channel, and one of them deleted an
  obligation.** `322fd1c` deletes §12 ¶1 entire, including *"referencing any non-nominated old
  component from v3 is a `SPEC_GAP`"* — text that imposed a requirement. `E10`'s deferral is
  available to an amendment that *"neither adds a clause to any rule nor changes what any rule
  requires (no rule-changing replacement or deletion)"*; a deletion of an obligation is outside
  that. The three contract commits do not claim the deferral's two facts: they say instead that
  the changed text *"owes `E10`'s independent re-read, riding this round's next read of that
  layer, and until it returns no conclusion of this round may rest on the changed bytes"* — which
  is the honest handling and withholds exactly the reliance the deferral would have bought. So
  nothing is wrong today; what is owed is a read, and the round says so. Recorded so the next
  opening read knows the contract's changed text is on its list and why.

- **O-4 — `document-harness/journal/core-only-layer-2026-08-30.md:456` and `:621` record a range
  with a written tip** (`8532979..0290eb9`). `E12`'s clause — *"A range recorded in a file has its
  base written and its tip `HEAD`, never a written SHA"* — is written without qualification, but
  its stated reason (a written tip is short by the commit that wrote it, and what it drops is the
  round's last-written records) does not reach a closed historical interval used as a measurement
  argument, which is what these two are. Wording-level under `R9`: no actor's action changes and
  the fact is recoverable from the sentence around it. It rides the next batch touching this
  journal and spawns nothing.

## 7. What I read, and the ceilings (`R4`)

**Read in full:** `document-harness/RULES.md`; `document-harness/CONSTRUCTION-CHECKLIST.md`; both
retired-contract stubs; `harness.json`; `CLAUDE.md`; `CONSTRUCTION-INDEX.md`;
`document-harness/plans/core-only.plan.md`; `tooling/tests/document_harness/test_harness_config.py`;
the `harness.json` half of `tooling/rsclib/document_harness/caller.py`; the whole diff of
`tooling/hooks/layer_path_check.py`, `tooling/sweep_refs.py`,
`tooling/rsclib/document_harness/init_target.py`, `__init__.py`, and the four touched test
modules; the whole diff of the five product-tier role documents, the contract,
`CONTRACT-V4-SIGNATURE.md`, both root READMEs, `CONSTRUCTION-LEDGER.md` and `HARNESS-RIDERS.md`;
all twenty-three commit bodies; `HD-67` and `HD-68` in full.

**Sampled:** `HARNESS-DECISIONS.md` — the two new entries in full, `§live`'s other entries by
heading only. The journal — §1, §4's fourth re-measure block, §5, §7's first item and §8 in full;
the rest by heading. Rider rows — the five deleted rows and the ten claiming touch records, read
against the commit bodies that claim them; the remaining eighteen by id only.

**Probed only:** `tooling/rsclib/document_harness/dispatch.py` (two constants and the prompt
template, to establish B-1's failure path — the module is item C's and this round does not change
it). `assurance/templates/run-v2/`. The N0/N1/N2 records.

**`UNVERIFIABLE`, stated rather than folded into supported:**

- That the opening cold read's record was *committed unchanged* (`ac39d35`), and that the five
  executor dispatches ran as separate cold `claude -p` sessions on `opus` under ruling 17. These
  are process claims about sessions I cannot inspect; marked, not verified (`R4`).
- The `E4` mutation table in journal §5: I independently reproduced rows 1 and 4's shapes (§3.3
  above). Rows 2 and 3 (`load_harness_config` defaulting on malformed input; `init_target`'s
  config write deleted) I did not re-run — the corresponding tests exist and are in the green 853.
- The claim that the one-shot split script compared each rule block against the source: not
  verified as a process, but its *result* is verified independently and completely in §3.1.

**Ceilings on my own coverage:**

- I did not run any `dtw dispatch` mode, and did not build a product run. Acceptances 4, 6 and 8
  are not this round's and I did not evaluate them.
- My harness-only tree is `git archive` over the eight product-tier rows as
  `CONSTRUCTION-INDEX.md` defines them. If a row's definition is wrong, my tree is wrong the same
  way; I checked the file count (59) against the index and the two agree, which is a consistency
  check and not an independent derivation of what ought to travel.
- Mutation proves a test has binding force, never that its force is sufficient (`R4`). Nothing
  here is a re-certification of the guards' coverage.
- Line numbers in this record were re-derived at `8f6b3ef` and drift with the next commit.

## 8. Process and record conformance (boundary check, run second)

- **`E8`** — every commit names its kind; titles carry the round; no amend inside the range; no
  `add -A` evidence — each body enumerates its explicit paths, and the enumerations match
  `--name-only` on the four I spot-checked; the change boundary is the round's declared items plus
  the registers.
- **`E2`** — machine-confirmed for the whole range (§3.5). The four announced-path commits each
  disclose site by site, and I read all four disclosures against the diffs.
- **`E9`** — budget virgin at dispatch; the read at `ac39d35` landed as the very next commit after
  its dispatch subject `a542c6d`, so the branch took no commit but the record; the ten
  pre-submission corrections each state and correctly apply the has-a-valid-FULL-occurred test.
- **`E1` / `R1`** — the executor commits disclose, once per dispatch, that the executor held none
  of `R1`'s four holdings. My own independence: dispatched by, prompted by, scoped by and reported
  through the orchestrator, not the executor; I received the range and nothing else.
- **`R2`** — no chat-only load-bearing material found. The thirty rulings are carried in the
  committed plan, `HD-67`/`HD-68` in the committed log, and the executor's questions and their
  answers are carried in the committed journal §7 with the answers written forward.
- **`R10`** — five rows deleted, each in the commit that earns it; the id-set diff shows no sixth.
  B-2 is the exception, and it is a blocker rather than a routing complaint.
- **`R6`** — this record is `v3-review-full-8f6b3ef.md` under
  `migration/document-work-assurance-v3/`, which is what `.harness/scan-surfaces.json` declares
  under `review_record_dirs` and what `CONSTRUCTION-CHECKLIST.md`'s `R6` instance value states.
  Written in the worktree, uncommitted; the orchestrator commits it.

## 9. Disposal, for the orchestrator

Both blockers are text corrections in the instruction layer that add no clause and change no
requirement, and both supply their content here — so `E10`'s free channel can take them without
spending `E9`'s fix leg, each owing the ride-along independent read. If the fix leg is spent
instead, one leg covers both, and this FULL's VERIFY covers the accepted findings plus the whole
repair diff.

L-2, L-3, L-4 and L-5 supply exact bytes and take the same free channel or ride the closeout
commit; L-1 supplies none — it needs a ruling on which reading of `E10` `.githooks/` falls under —
and banks. `R10`'s last clause applies to the lows: their deadlines against their touch triggers
are the orchestrator's to weigh with the user before closeout, and a late activation is still this
round's one fix and still obliges the VERIFY.
