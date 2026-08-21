# Cold read — the instruction layer at `dd22789`

**No verdict.** A read is not a round (`R3`): it spends no budget, carries no verdict, and its
output is findings tiered must-fix / low / observation. This is the read `E10` owes at a
round's opening — the next round's, `PREVIEW-RENDER`, whose queue-head position the subject
commit itself sets. Nothing below certifies any text, and nothing below is banked as any
round's FULL.

**Findings: 0 must-fix, 1 low, 3 observations.** The low is a rider row the round just closed
left unreconciled: the amendment that fixed the previous read's `M-1` deleted the exact bytes
rider `review-record-loc` names, and the bank was edited three times in the same round without
the row being touched. No must-fix: the layer's own bytes carry no defect that cannot wait.

**Standing instructions read.** `migration/document-work-assurance-v3/v3-harness-review-contract.md`
(the stub, member 7) → `document-harness/CONSTRUCTION-CHECKLIST.md` in full, both sides, per the
stub's *"It is your standing instruction and its own counterpart; read all of it."*
`HARNESS-DECISIONS.md` `§live` (lines 28–133, **seven** entries — `HD-44`, `HD-41`, `HD-36`,
`HD-35`, `HD-34`, `HD-23`, `HD-9`) plus the file header (1–27) that states its own state
machine, which `E10`'s tail requires. `§implemented` (135–487) and
`HARNESS-DECISIONS-archive.md` were **not** read end to end — they were grepped for the ids the
members cite (§3.6). Cited by section, never by blob, per that clause.

---

## 1. What the subject is, and how it was derived

The dispatch supplied one commit and nothing else. Everything below was re-derived
(`R2`).

```
$ git log -1 --format="%H%n%ad%n%s" dd22789ef34c615f17e64f2df3b38301bc328896
dd22789ef34c615f17e64f2df3b38301bc328896
Fri Aug 21 12:31:02 2026 +1000
V3-E11-RULING-QUEUEHEAD-v1

$ git log --oneline -1
dd22789 V3-E11-RULING-QUEUEHEAD-v1

$ git status --porcelain
(no output)
```

The subject is the branch tip and the worktree is clean, so working-tree bytes and subject
bytes coincide; every quotation below was nonetheless taken from the object store
(`git show <sha>:<path>` / `git ls-tree`), not from the working tree.

The dispatch prompt I was handed is byte-identical to `READ_PROMPT` in
`tooling/rsclib/document_harness/dispatch.py:668-681`, including its refusal to enumerate the
member set — checked because a hand-written dispatch handing the reader a wrong member table
is the recorded failure (`v3-cold-read-451e8b0.md` `M-1`) that generator path exists to
prevent.

## 2. The member set and each member's blob

The member set was parsed out of `E10`'s own sentence in member 1, not taken from the
dispatch, and not taken from the guard that mirrors it. Blob ids per `E10`'s *"a read's record
states the blob id of each member it read, because citation depends on it"*.

```
1  cacd99d49d80ce4bf33e94b733a07f1dd6b247e8   235 lines   18531 B  document-harness/CONSTRUCTION-CHECKLIST.md
2  7591c5332d170a286a15ef6a699f69cc80def755    40 lines   11021 B  document-harness/README.md
3  0bf48fa0ce5a15fd341772de31e5f46fab60a4d9   470 lines   32701 B  document-harness/EXECUTION.md
4  4cae5ce76d84571f1bf92ab89001f3e8f2c98ae3   287 lines   18165 B  document-harness/REVIEW.md
5  80f42658a2961eeb10a168bd7bd729121c6c05ae    95 lines    6389 B  document-harness/ORCHESTRATION.md
6  6d5714923870b4e13e8928221a80df68e563a5ed     5 lines     511 B  migration/document-work-assurance-v3/v3-harness-operating-contract.md
7  29bdc9fbde6e8db38d601dd2340d4b46a24a296f     5 lines     924 B  migration/document-work-assurance-v3/v3-harness-review-contract.md
8  68031fa2ca31272e31da0d42a9a02189d28fcc21   124 lines    6480 B  contract/Document-Work-Assurance-Contract-v3-supersession-1.md
9  e1a2f26b1d8d323d11e900f8137dea222b6571c1   113 lines    7421 B  contract/Document-Work-Assurance-Contract-v3-supersession-2.md
10 09aa869962f592c2f86c9379be0ef3eb7d2232ff    44 lines    2812 B  schema/document-assurance-v3/paragraph-map.schema.json
total lines: 1418
```

Ten paths enumerated, ten present, none missing.

**All ten were read end to end. No citation is claimed for any of them**, although seven were
citable: `v3-cold-read-17ce3ed.md` §2 records members 1–7 as read end to end at blobs
`cacd99d4`, `3a49e032`, `0d0c617b`, `946b4beb`, `80f42658`, `6d571492`, `29bdc9fb`, and members
8–10 as covered by citation at `68031fa2`, `e1a2f26b`, `09aa8699`. Of those, members 1, 5, 6, 7
are byte-identical here, and 8–10 are unchanged blobs whose citation chain runs back to
`v3-cold-read-4410899.md`. Citation was available and is **not** taken: the cross-member checks
in §3 need the text of every member, and a read whose value is the cross-check buys nothing by
declining to open the files. Members 2, 3 and 4 changed and were owed a read regardless.

**Three members changed since the last recorded read**, and each change arrived on a channel
`E10` names:

```
$ git log --oneline --name-only 17ce3ed..dd22789 -- <the ten member paths>
84dea06 V3-INIT-SURFACE-FIX-v1
document-harness/README.md
7f6e7f0 V3-INIT-SURFACE-v1
document-harness/EXECUTION.md
document-harness/README.md
bba6f94 V3-INIT-SURFACE-AMEND-M1-v1
document-harness/REVIEW.md
```

`bba6f94` is the `E10` must-fix amendment answering `v3-cold-read-17ce3ed.md` `M-1`, paired
with its independent re-read `v3-checkpoint-read-bba6f94.md`; `7f6e7f0` is the round's
candidate and `84dea06` its one user-approved fix, each with its own review record. The
round's free-channel commit `9fe60b9` touched `tooling/rsclib/document_harness/paths.py` and
`tooling/tests/document_harness/test_precommit_checks.py` and **no member**, so it carries no
deferred layer-read debt — its own commit body says so and `git show --stat` bears it out.
**There is no outstanding deferred read against this layer**; the debt `DE-PREFIX` recorded was
paid by `v3-cold-read-17ce3ed.md`.

**Not a member, read by section:** `HARNESS-DECISIONS.md` `§live`, per `E10`'s tail clause.
It is not listed above and is cited by section, never by blob, exactly as that clause requires.

## 3. What was checked, and what the commands returned

Scope declaration (`HD-41` ①): unless a line says otherwise, every enumeration below is over
the **ten member blobs at `dd22789`** and nothing else.

### 3.1 `E2`'s freeze surface — three blobs and one directory

```
$ git ls-tree dd22789 -- contract/
100644 blob 68031fa2ca31272e31da0d42a9a02189d28fcc21  …-supersession-1.md
100644 blob e1a2f26b1d8d323d11e900f8137dea222b6571c1  …-supersession-2.md
100644 blob b2dbdf752d8c155e4c65b14b5f420b880b8184a1  Document-Work-Assurance-Contract-v3.md

$ git ls-tree -r --name-only dd22789 -- schema/document-assurance-v3/   |   wc -l
15
```

All three named blobs verify against `E2`'s text (`b2dbdf75…`, `68031fa2…`, `e1a2f26b…`), and
the pack holds exactly the **fifteen** files `E2`'s parenthesis states — so no file has joined
the pack since the 2026-08-03 re-baseline, and the "not frozen until a later re-baseline"
branch is dormant. Two of the three blobs are members 8 and 9. README `:20`'s *"that directory
holds exactly the three files the rows above name"* holds on the same output.

README's four schema rows (`:22-25`) enumerate 8 + 2 + 4 + 1 = 15 schema names; the fifteen
tracked filenames match them one for one, with no name in either list absent from the other.

### 3.2 Every path reference in the layer, resolved

The committed sweep was used rather than a hand-rolled one, and its result was reproduced
independently first by driving the guard's own `unresolved_tokens` over each member's **full
standing text** — the stock `E10` says the guard never re-scans.

```
$ python tooling/sweep_refs.py
NAMETOK document-harness/EXECUTION.md:186  audit-rounds.md
NAMETOK document-harness/EXECUTION.md:194  build_run.py
NAMETOK document-harness/EXECUTION.md:199  check_shells.py
NAMETOK document-harness/EXECUTION.md:284  write_audit.py
NAMETOK document-harness/EXECUTION.md:343  smoke_test.py
NAMETOK document-harness/EXECUTION.md:347  run_p4_tests.py
NAMETOK document-harness/EXECUTION.md:347  run_p5a_tests.py
NAMETOK document-harness/EXECUTION.md:452  v3-review-full-86defbc.md
NAMETOK document-harness/EXECUTION.md:453  audit-rounds.md
NAMETOK document-harness/EXECUTION.md:456  user-decision-triage-comparator-environment-defects.json
NAMETOK document-harness/REVIEW.md:45  v3-review-full-fef3a2e.md
NAMETOK document-harness/REVIEW.md:133  review-verify.json
PATHTOK contract/Document-Work-Assurance-Contract-v3-supersession-1.md:7  ResearchSystem/migration/document-work-assurance-v3/W2/W2-design.md
PATHTOK contract/Document-Work-Assurance-Contract-v3-supersession-1.md:123  ResearchSystem/migration/document-work-assurance-v3/W2/W2-record.md
PATHTOK contract/Document-Work-Assurance-Contract-v3-supersession-2.md:60  assurance/runs/
PATHTOK contract/Document-Work-Assurance-Contract-v3-supersession-2.md:99  templates/run-v2/
PATHTOK contract/Document-Work-Assurance-Contract-v3-supersession-2.md:110  ResearchSystem/migration/document-work-assurance-v3/
-- 17 caller-held or unresolvable references over 10 members
```

**All five PATHTOK hits sit inside `E2`-frozen bytes** (members 8 and 9), which `E10`'s clause
excepts *while they are frozen*, and which rider `frozen-path-prefix` already banks against
`E2`'s recorded ruling. The count is 5, matching that row's re-measured figure. **The eight
non-frozen members carry zero unresolved backtick path tokens.**

**Markdown links**, a class the guard has no backtick token to find: every link target in all
ten members was resolved from the repository root and from the member's own directory —
**0 broken**, 0 escaping the repository root.

**Each NAMETOK was checked for the holder sentence `E10` requires**, which is the reason the
sweep prints them (its docstring says a bare name is the *compliant* form). Eleven of the
twelve carry one in the same or an adjacent sentence — *"held with its run in the caller that
grew this harness"* (`:186`, `:453`, `:456`, `:452`), *"the ExperimentLab papers tree"*
(`:343`), *"the caller repository, the product tree … named here rather than written as paths
(`E10`) because their scripts live in the caller's tree"* (`:347`), *"the run's"* (`:284`),
*"held with that run's records in the caller that grew this harness rather than here"*
(REVIEW `:45`). The twelfth is `O-1` below.

EXECUTION `:349-351`'s disclosure that a battery name *"may also belong to an unrelated file in
this repository"* is not hypothetical and is load-bearing:

```
$ git ls-tree -r --name-only dd22789 | grep -E "/(run_tests|validate_fixtures|rsc)\.py$"
migration/document-work-assurance-v3/N0/fixtures/validate_fixtures.py
tooling/tests/document_harness/run_tests.py
tooling/tests/document_harness_review/run_tests.py
```

Two of the caller's five battery command names collide with unrelated files here. The text
already forbids identification by name-matching; the collision is real.

### 3.3 The membership sentence and its three mirrors (`HD-22`)

`E10`'s sentence names ten paths. The mirrors were compared against it by hand, not by
diffing one against another:

- `tooling/hooks/layer_path_check.py:37-48` `LAYER` — ten, in the same order.
- `tooling/tests/document_harness/test_precommit_checks.py:225-236` `EXPECTED` — a
  hand-written literal, `E5`-shaped, ten, same order, asserted equal to `LAYER` and separately
  proved to reach every member.
- `tooling/sweep_refs.py:36` imports `LAYER` rather than copying it, so it is not a fourth
  mirror; its docstring says exactly that.

No drift. `tooling/rsclib/document_harness/dispatch.py:545-547`'s
`CONSTRUCTION_ROLE_INSTRUCTION` holds member 7's path and is pinned independently by
hand-written literals at `test_dispatch.py:398`, `:463`, `:522`; the construction and read
prompts both carry `{charter}` as a substitution, never the path — the stub's own claim about
itself, verified.

### 3.4 Rule enumerations

```
$ grep -oE "^- \*\*(E|R)[0-9]+\*\*" document-harness/CONSTRUCTION-CHECKLIST.md
E1 E2 E3 E4 E5 E6 E7 E8 E9 E10 E11 E12 R1 R2 R3 R9 R10 R4 R5 R6 R7 R8
```

Twelve `E` and ten `R`, complete, no duplicates, no gaps — README `:27`'s *"E1–E12 execution,
R1–R10 review"* holds. `R9` and `R10` sit between `R3` and `R4` rather than in numeric order;
that is presentation, and both are present and reachable.

`ORCHESTRATION.md`'s nine cite-only rows were counted (nine) and its three own-text sections
counted (three), so README `:26`'s *"nine of its twelve obligations are already stated by rules
elsewhere"* holds. `ONBOARDING.md` has nine numbered items (`### 1`–`### 9`), matching README
`:30` and the file's own heading.

### 3.5 `dtw init`, against the boundary README `:30` newly states

The clause added this round says the tree half may enter `init` and the machine half never
does, and that the two instance files land at the target root as a default, `init` taking no
placement option.

`init_target.py:35-38` `TEMPLATES` holds exactly two entries, written to `target / dest_name`
at the target root, with the default-not-requirement point and its `HD-34` citation in the
constant's own comment. `cli.py:574-578` gives `init` one argument, `--repo-root` — which
target, never where inside it. `init_target.py` creates `.harness/`, its `.gitignore` entry and
the two files, and nothing per-machine: no `git config`, no revision pinning, no policy file,
no hook wiring. The boundary as written is what the code does.

### 3.6 `HD` ids the members cite

Thirteen distinct ids are cited across the ten members; all thirteen resolve.

```
HD-1 implemented   HD-2 implemented   HD-5 implemented   HD-7 implemented
HD-14 archive      HD-20 implemented  HD-28 archive      HD-34 live
HD-35 live         HD-39 archive      HD-41 live         HD-42 archive
HD-47 implemented
```

`§live` shrank from ten entries to seven between `17ce3ed` and the subject — `HD-47` turned
`implemented` at the round's closeout, `HD-50` retired into the archive, and `HD-49` moved to
`§implemented` at `762dd7b`, that last one executing the previous read's `O-1`. No member cites
`HD-49` or `HD-50`, so nothing in the layer went dangling. Both files were grepped, not read
end to end; that is the ceiling on this line.

### 3.7 The guard, exercised rather than trusted

`E10` asserts what `layer_path_check` blocks. The assertion was tested with a positive control,
because a probe that blocks nothing may simply have failed to reach the code (`R8`):

```
PASSED  .githooks/post-commit          pathlike=False
PASSED  document-harness/no-such-hook  pathlike=False
PASSED  tooling/hooks/no_such.sh       pathlike=False
PASSED  tooling/pyproject-nope.toml    pathlike=False
BLOCKED document-harness/no-such-file.md   pathlike=True    <- positive control
```

The guard binds, and four nowhere-resolving tokens pass it, none of them a placeholder. This
reproduces a live rider rather than reporting a new defect — see `O-2`.

```
$ python -m pytest -q tests/document_harness/test_precommit_checks.py   # run from tooling/
49 passed in 14.64s
```

`.githooks/pre-commit` runs `layer_path_check.py` and nothing else, and fails loudly rather
than silently if the script is absent — README `:36`'s *"The third, instruction-layer path
resolution, runs here"* holds on the file's bytes.

### 3.8 Commit ids cited in the layer

Fourteen commit-id-shaped tokens are cited. Thirteen are absent from this repository and are
covered generically by the checklist header's *Where a cited commit id resolves* clause, whose
own referent was checked: root `README.md:12-21` carries a *Where the bytes came from* section
that names the source repository and says why the history stayed there. The fourteenth,
`0d73a5f` in EXECUTION `:383`, does resolve here and is written *"instrument `0d73a5f`"* — a
citation naming its own repository, read as written, exactly as the clause provides. The
caller-side id beside it is written *"caller `6fd0ae3`"*. No silent id is ambiguous.

### 3.9 The "single home" claim README `:36` newly makes

Grepping the ten members for the two guards by name returns three hits: README `:36` (the home
itself), CONSTRUCTION-CHECKLIST `:147` (describing `layer_path_check`'s own behaviour, which is
its own subject) and EXECUTION `:329` (naming it as a path-pinning file for the battery tier).
No second statement of the division of labour survives inside the layer. Outside it,
`candidate_path_check.py:8-10`, `paths.py:18`, and `test_precommit_checks.py:251` and `:350` all
point at the README row instead of restating it. The claim holds on the sweep that would
falsify it.

## 4. Findings

### `L-1` (low) — the round deleted the bytes rider `review-record-loc` names, and left the row standing

**Location.** `HARNESS-RIDERS.md:45`, against `document-harness/REVIEW.md:134-138` (blob
`4cae5ce7`).

**What the row says.** *「`REVIEW.md:134-136` 把评审记录落盘位置硬编码为
`migration/document-work-assurance-v3/...`——只在本仓与长出它的调用者两处为真；新调用者的
reviewer 照读会把记录写进人家不存在的目录。」* Source: `v3-cold-read-69fc082.md` `O-3`.

**What the bytes now say.** The amendment `bba6f94` — answering `v3-cold-read-17ce3ed.md`
`M-1`, which is the *same defect at the same three lines* — replaced them:

```
$ git show dd22789:document-harness/REVIEW.md | sed -n '134,138p'
2. **The review record** — the prose record of what you read, re-executed and found: a file
   named `v3-review-<round>-<subject short SHA>.md` (`<round>` = `full` | `verify`; repo
   naming precedent), written beside that run's other records in the caller's own
   document-work-assurance-v3 migration directory. The caller holds it; this layer does not
   write its path.
```

The hardcoded path token the row quotes is gone; §3.2's sweep confirms REVIEW.md now carries
no unresolved path token at all.

**Ground truth violated.** `R10`: *"Redemption = the fix rides a batch already touching that
surface, and the row is deleted in the same commit."* The surface was touched, by three
separate commits, and the bank was itself edited twice in the same round:

```
$ git diff 17ce3ed dd22789 -- HARNESS-RIDERS.md | grep -c "^-| "
4
```

Four rows changed — `guard-division-home` deleted on redemption, `submod-index`,
`decited-paths` and `self-caller-guards` rewritten. `review-record-loc` was neither deleted nor
annotated.

**Why this is low and not must-fix.** Nothing acts wrongly today: the layer's bytes are
correct, and the stale row is in the bank, not in a member. It is not wording-level under `R9`
either, because the fix changes an actor's action — the next batch touching `REVIEW.md`'s
record channel will either re-apply a fix already applied or, reading the row's quoted bytes
against text that no longer contains them, conclude the row is unintelligible and skip it.

**Minimum fix, and why I supply no bytes.** Two readings are open and the choice is not mine
(`R5`). Either the row is redeemed and is deleted; or it is *partly* redeemed — the `E10`
path-token half is fixed while the substantive half survives in weaker form, since *"the
caller's own document-work-assurance-v3 migration directory"* still assumes a directory naming
convention true only in this repository and the caller that grew it, and the row's deadline
(第二個真調用者的第一次評審派發) has not arrived — in which case the `what` column is rewritten
to quote the current bytes. Both are one-line edits to a non-member file; which one is correct
is a question about what the row is still for.

### `O-1` (observation) — REVIEW.md's deliverable item 1 gives a caller-held artifact its name but not its holder, where its just-amended sibling gives both

**Location.** `document-harness/REVIEW.md:131-133`: *"written to
`<control root>/evidence/review-full.json`"*.

`<control root>` is caller-held — EXECUTION.md `:260` says so in as many words, *"the control
root lives in the caller, not here"* — and the token is invisible to `layer_path_check` because
its path shape admits no angle brackets, so it is held by `E10`'s clause and by nothing else.
Item 2, four lines below, was amended this round to end *"The caller holds it; this layer does
not write its path."* Item 1 was not.

**Disposition — `R9` wording-level, banked, no round and no read.** The clause's stated purpose
is that *"a reader following a path in this layer cannot land on another repository's bytes or
on nothing"*; a placeholder root cannot be followed anywhere, so nothing is mis-led, and item 1
already tells the reviewer the run's control plane names the schema — the same control plane
that fixes the root. **I can name no downstream decision that goes wrong if it stays
unfixed**, so per `R9` it rides the next batch touching this layer and spawns nothing. Bytes,
if a batch wants them: append *"— the control root lives in the caller"* to item 1, mirroring
EXECUTION.md `:260`.

### `O-2` (observation) — the guard's path-shape blind spot reproduces exactly, and one datum can be added to the row that banks it

§3.7's probe was run before the bank was read, and it lands precisely on live rider
`e10-cannot-see` (`HARNESS-RIDERS.md:47`, source `v3-review-verify-2538893.md` `V-3`): the
blind-spot list in `E10`'s clause names only the placeholder class, and both the extensionless
form and the outside-the-seven-extensions form pass silently. The row's own live instance —
README `:36`'s `` `.githooks/pre-commit` `` — is still the only one in the layer, and it
resolves, so nothing is broken today. **This is not a new finding**, and it is reported only so
that the reproduction is on the record.

One datum the row does not carry: the mismatch is not confined to the clause's blind-spot
list. The sentence above it asserts the guard blocks *"every path-shaped token that resolves
nowhere inside this repository … which since round `DE-PREFIX` is **the class entire**, a
caller-held path included"*. That absolute quantifier is itself falsified by the same probe —
`` `tooling/hooks/no_such.sh` `` is a caller-shaped, nowhere-resolving path token that passes.
Whoever redeems the row will be editing two sentences, not one. The routing is unchanged: the
row states the fix may trip `E10`'s design test and so does not take the free channel.

### `O-3` (observation) — two further live riders were independently reproduced during this read

Reported because reproduction is evidence the rows are still live, not because either is new:

- `e1-table` (`:41`) — `ORCHESTRATION.md`'s nine-obligation table has no row for `E1`'s
  disclosure duty (*"the round states which of the four the executor held … and the statement
  is the orchestrator's to make"*). Counted directly off member 5: nine rows, none of them that
  one.
- `onboarding-labels` (`:44`) — README `:30`'s five-label parenthetical over nine
  `ONBOARDING.md` items. The row is accurate; the sentence's *"anything … requiring judgment"*
  framing means the uncovered item is not thereby mis-stated, only unlisted.

## 5. Coverage — what was read in full, what was sampled, what was only probed (`R4`)

- **Read in full at the subject blobs:** all ten members, 1 418 lines. Blob ids in §2. No
  citation is claimed for any member, although seven were citable.
- **Read by section:** `HARNESS-DECISIONS.md` header (1–27) and `§live` (28–133) in full, per
  `E10`'s tail. `§implemented` (135–487) and `HARNESS-DECISIONS-archive.md` were **grepped
  only**, for the thirteen ids §3.6 resolves — a `HD` entry whose *text* contradicts a member
  would not have been seen unless its id was cited.
- **Read in full outside the layer** (because a member's assertion turned on them):
  `tooling/hooks/layer_path_check.py`, `tooling/rsclib/document_harness/init_target.py`,
  `.githooks/pre-commit`.
- **Sampled:** `tooling/rsclib/document_harness/dispatch.py` (the two prompt constants, the
  charter constant, `read_dispatch_of`, `render_read_dispatch`);
  `tooling/hooks/candidate_path_check.py` (docstring only, lines 1–40);
  `tooling/sweep_refs.py` (docstring and imports); `tooling/tests/…/test_precommit_checks.py`
  and `test_dispatch.py` (the hand-written constants and the class docstrings that carry the
  pointer claims); `HARNESS-RIDERS.md` (row ids in full, three rows read in full, the rest by
  their `what` column's opening); `CONSTRUCTION-LEDGER.md` (grepped, not read).
- **Only probed:** the guard's behaviour, by five synthetic tokens with one positive control
  (§3.7). Five probes are not the class; they establish that the class is not empty, never its
  size.
- **Not attempted:** the full regression battery. This read changes nothing, so no tier is
  owed; one module (49 tests) was run because the guard it covers is a subject of §3.7. Every
  battery figure quoted in EXECUTION.md is explicitly revision-pinned and was not re-measured —
  a current figure would require running the battery, which `E3` says to do at the moment of
  the claim, and I make none.
- **Marked, not verified (`R4`):** that this read ran in a fresh context. It did, and that is a
  process claim with no evidence lock.
- **Authorization ceiling (`R7`):** the subject commit sets `PREVIEW-RENDER` as the queue head
  and records the `E11` carrier ruling. I can see that in the repository; I cannot see the
  conversation those rulings were given in, and I did not treat the commit body as anything
  more than the executor's own statement of them.
