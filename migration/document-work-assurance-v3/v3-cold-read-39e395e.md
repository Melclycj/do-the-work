# Cold read — the instruction layer at `39e395e`

**No verdict.** A read is not a round (`R3`): it spends no budget, carries no verdict, and its
output is findings tiered must-fix / low / observation. This is the read `E10` owes at a
round's opening, and it is also the read the two member edits of round `PREVIEW-RENDER` owe —
both commit bodies defer it here by name. Nothing below certifies any text, and nothing below
is banked as any round's FULL.

**Findings: 0 must-fix, 1 low, 3 observations.** The low is the one edit this round made to a
rule's substance: `EXECUTION.md`'s new SIMP-C4 wiring sentence carries the 2026-08-21 ruling
only for the **enumerated** form, while the ruling as journaled is unscoped and the command it
names refuses no form. No must-fix: nothing in the layer's bytes acts wrongly today.

**The deferred read is discharged here.** Members 3 and 4 changed at `57d1312`; no round relied
on either before this read (§3.6), so `E10`'s general rule — *an independent read before any
round relies on it* — is met without the deferral clause being needed.

**Standing instructions read.** `migration/document-work-assurance-v3/v3-harness-review-contract.md`
(the stub, member 7) → `document-harness/CONSTRUCTION-CHECKLIST.md` in full, both sides, per the
stub's *"It is your standing instruction and its own counterpart; read all of it."*
`HARNESS-DECISIONS.md` `§live` (lines 28–133, **seven** entries — `HD-44`, `HD-41`, `HD-36`,
`HD-35`, `HD-34`, `HD-23`, `HD-9`) plus the file header (1–27) that states its own state
machine, which `E10`'s tail requires. `§implemented` (135–487) and
`HARNESS-DECISIONS-archive.md` were **not** read end to end — they were grepped for the ids the
members cite (§3.5). Cited by section, never by blob, per that clause.

---

## 1. What the subject is, and how it was derived

The dispatch supplied one commit and nothing else. Everything below was re-derived (`R2`).

```
$ git rev-parse HEAD
39e395e5221f5cbf0a1ab729c0822e20f6873994

$ git log -1 --format="%H%n%ci%n%s" 39e395e5221f5cbf0a1ab729c0822e20f6873994
39e395e5221f5cbf0a1ab729c0822e20f6873994
2026-08-21 16:03:58 +1000
V3-PREVIEW-RENDER-CLOSEOUT-v1

$ git status --porcelain
(no output)
```

The subject is the branch tip and the worktree is clean, so working-tree bytes and subject
bytes coincide; every quotation below was nonetheless taken from the object store
(`git show <sha>:<path>` / `git ls-tree`), not from the working tree.

The dispatch prompt I was handed is byte-identical to `READ_PROMPT` in
`tooling/rsclib/document_harness/dispatch.py:668-681` — checked because a hand-written dispatch
handing the reader a wrong member table is the recorded failure (`v3-cold-read-451e8b0.md`
`M-1`) that generator path exists to prevent. `render_read_dispatch` (`:704-718`) returns that
constant and nothing else, and its docstring says so; the two sentences appended to my prompt
(repository root, *write into the worktree, do not commit*) are transport, hand me no member
set and no figure, and are consistent with `R6` giving the record's commit to the orchestrator.

## 2. The member set and each member's blob

The member set was parsed out of `E10`'s own sentence in member 1, not taken from the dispatch,
and not taken from the guard that mirrors it. Blob ids per `E10`'s *"a read's record states the
blob id of each member it read, because citation depends on it"*.

```
1  cacd99d49d80ce4bf33e94b733a07f1dd6b247e8   235 lines   18531 B  document-harness/CONSTRUCTION-CHECKLIST.md
2  7591c5332d170a286a15ef6a699f69cc80def755    40 lines   11021 B  document-harness/README.md
3  27f4fc82a556f26804ee5236204f746bd99da5bd   474 lines   32987 B  document-harness/EXECUTION.md
4  35fe0abcd7123f4a37a88ef4de605b3aad3cfe75   288 lines   18209 B  document-harness/REVIEW.md
5  80f42658a2961eeb10a168bd7bd729121c6c05ae    95 lines    6389 B  document-harness/ORCHESTRATION.md
6  6d5714923870b4e13e8928221a80df68e563a5ed     5 lines     511 B  migration/document-work-assurance-v3/v3-harness-operating-contract.md
7  29bdc9fbde6e8db38d601dd2340d4b46a24a296f     5 lines     924 B  migration/document-work-assurance-v3/v3-harness-review-contract.md
8  68031fa2ca31272e31da0d42a9a02189d28fcc21   124 lines    6480 B  contract/Document-Work-Assurance-Contract-v3-supersession-1.md
9  e1a2f26b1d8d323d11e900f8137dea222b6571c1   113 lines    7421 B  contract/Document-Work-Assurance-Contract-v3-supersession-2.md
10 09aa869962f592c2f86c9379be0ef3eb7d2232ff    44 lines    2812 B  schema/document-assurance-v3/paragraph-map.schema.json
total lines: 1423
```

Ten paths enumerated, ten present, none missing.

**All ten were read end to end. No citation is claimed for any of them**, although eight were
citable: `v3-cold-read-dd22789.md` §2 records all ten as read end to end, and members 1, 2, 5,
6, 7, 8, 9, 10 are byte-identical here. Citation was available and is **not** taken: the
cross-member checks in §3 need the text of every member, and a read whose value is the
cross-check buys nothing by declining to open the files.

**Two members changed since that read**, and both changes arrived on a channel `E10` names:

```
$ git log --oneline --name-only dd22789..39e395e -- <the ten member paths>
57d1312 V3-PREVIEW-RENDER-v1
document-harness/EXECUTION.md
document-harness/REVIEW.md
```

`57d1312` is round `PREVIEW-RENDER`'s candidate. The round's other four commits touch no
member: `15a53fe` (the one user-approved fix) and `93dc1f0` / `3797786` / `c7c9081` (records)
appear nowhere in that log, and the free-channel application `76ebf4a` changes
`tooling/rsclib/document_harness/preview.py` and
`tooling/tests/document_harness/test_preview.py` only (`git show --stat`), so it carries no
deferred layer-read debt — its own body says so and the stat bears it out. The closeout
`39e395e` changes `CONSTRUCTION-LEDGER.md`, `HARNESS-DECISIONS.md`, `HARNESS-RIDERS.md` and the
round journal. **There is no outstanding deferred read against this layer** once this record
lands.

**Not a member, read by section:** `HARNESS-DECISIONS.md` `§live`, per `E10`'s tail clause. It
is not listed above and is cited by section, never by blob, exactly as that clause requires.

## 3. What was checked, and what the commands returned

Scope declaration (`HD-41` ①): unless a line says otherwise, every enumeration below is over the
**ten member blobs at `39e395e`** and nothing else.

### 3.1 `E2`'s freeze surface — three blobs and one directory

```
$ git ls-tree 39e395e -- contract/
100644 blob 68031fa2ca31272e31da0d42a9a02189d28fcc21  …-supersession-1.md
100644 blob e1a2f26b1d8d323d11e900f8137dea222b6571c1  …-supersession-2.md
100644 blob b2dbdf752d8c155e4c65b14b5f420b880b8184a1  Document-Work-Assurance-Contract-v3.md

$ git ls-tree -r --name-only 39e395e -- schema/document-assurance-v3/   |   wc -l
15

$ git diff --stat dd22789 39e395e -- contract/ schema/document-assurance-v3/
(no output)
```

All three named blobs verify against `E2`'s text (`b2dbdf75…`, `68031fa2…`, `e1a2f26b…`), and
the pack holds exactly the **fifteen** files `E2`'s parenthesis states — no file has joined the
pack since the 2026-08-03 re-baseline, so the "not frozen until a later re-baseline" branch is
dormant. The round touched none of it. README `:20`'s *"that directory holds exactly the three
files the rows above name"* holds on the same output.

README's four schema rows (`:22-25`) enumerate 8 + 2 + 4 + 1 = 15 schema names; the fifteen
tracked filenames match them one for one, with no name in either list absent from the other.

### 3.2 Every path reference in the layer, resolved

```
$ python tooling/sweep_refs.py
NAMETOK document-harness/EXECUTION.md:186  audit-rounds.md
NAMETOK document-harness/EXECUTION.md:194  build_run.py
NAMETOK document-harness/EXECUTION.md:199  check_shells.py
NAMETOK document-harness/EXECUTION.md:288  write_audit.py
NAMETOK document-harness/EXECUTION.md:347  smoke_test.py
NAMETOK document-harness/EXECUTION.md:351  run_p4_tests.py
NAMETOK document-harness/EXECUTION.md:351  run_p5a_tests.py
NAMETOK document-harness/EXECUTION.md:456  v3-review-full-86defbc.md
NAMETOK document-harness/EXECUTION.md:457  audit-rounds.md
NAMETOK document-harness/EXECUTION.md:460  user-decision-triage-comparator-environment-defects.json
NAMETOK document-harness/REVIEW.md:45  v3-review-full-fef3a2e.md
NAMETOK document-harness/REVIEW.md:133  review-verify.json
PATHTOK contract/Document-Work-Assurance-Contract-v3-supersession-1.md:7  ResearchSystem/…/W2/W2-design.md
PATHTOK contract/Document-Work-Assurance-Contract-v3-supersession-1.md:123  ResearchSystem/…/W2/W2-record.md
PATHTOK contract/Document-Work-Assurance-Contract-v3-supersession-2.md:60  assurance/runs/
PATHTOK contract/Document-Work-Assurance-Contract-v3-supersession-2.md:99  templates/run-v2/
PATHTOK contract/Document-Work-Assurance-Contract-v3-supersession-2.md:110  ResearchSystem/…/document-work-assurance-v3/
-- 17 caller-held or unresolvable references over 10 members
```

Same seventeen as at `dd22789`; the six `EXECUTION.md` line numbers that moved (`:284→:288`,
`:343→:347`, `:347→:351`, `:452→:456`, `:453→:457`, `:456→:460`) are the +4 shift of the
SIMP-C4 insert and nothing else. **All five PATHTOK hits sit inside `E2`-frozen bytes**
(members 8 and 9), which `E10`'s clause excepts *while they are frozen*, and which rider
`frozen-path-prefix` already banks against `E2`'s recorded ruling. **The eight non-frozen
members carry zero unresolved backtick path tokens**, the two amended ones included: nothing
`57d1312` added to a member is a path token.

**Markdown links**, a class the guard has no backtick token to find: every relative link target
in all ten members was resolved from the repository root — **51 targets, 0 broken, 0 escaping
the repository root**. Decoded as explicit UTF-8, never through the console locale, per
REVIEW.md `:148-152`'s own rule; the first attempt died on a `gbk` codec error, which is that
rule earning itself.

**Each NAMETOK carries the holder sentence `E10` requires.** Eleven were already established at
`dd22789`. The twelfth — REVIEW.md `:133` `review-verify.json`, which that read filed as its
`O-1` — now does too: item 1 ends *"— the control root lives in the caller"*, the exact bytes
that read supplied. See `O-3`.

**Line-number self-references inside the members: zero.** Checked because the SIMP-C4 insert
shifted everything after EXECUTION.md `:243` by four lines; no member cites another member (or
itself) by line, so the shift falsified nothing inside the layer. It did move two surfaces the
rider bank points at — see `O-2`.

### 3.3 The membership sentence and its two mirrors (`HD-22`)

`E10`'s sentence names ten paths. The mirrors were compared against it by hand, not by diffing
one against another:

- `tooling/hooks/layer_path_check.py:37-48` `LAYER` — ten, in the same order.
- `tooling/tests/document_harness/test_precommit_checks.py:225-236` `EXPECTED` — a hand-written
  literal, `E5`-shaped, ten, same order, asserted equal to `LAYER`
  (`test_layer_equals_the_hand_written_membership`) and separately proved to reach every member
  (`test_every_member_is_scanned`).
- `tooling/sweep_refs.py:36` imports `LAYER` rather than copying it, so it is not a third
  mirror.

No drift. Member 1 is byte-identical to `dd22789`, so the membership sentence was untouched
this round and rider `E10-sync`'s touch condition did not arrive — `git diff dd22789 39e395e --
document-harness/CONSTRUCTION-CHECKLIST.md` is empty.

### 3.4 Rule enumerations and the counts the members state about themselves

```
$ grep -oE "^- \*\*(E|R)[0-9]+\*\*" document-harness/CONSTRUCTION-CHECKLIST.md
E1 E2 E3 E4 E5 E6 E7 E8 E9 E10 E11 E12 R1 R2 R3 R9 R10 R4 R5 R6 R7 R8
```

Twelve `E` and ten `R`, complete, no duplicates, no gaps — README `:27`'s *"E1–E12 execution,
R1–R10 review"* holds. `R9` and `R10` sit between `R3` and `R4` rather than in numeric order;
that is presentation, and both are present and reachable.

`ORCHESTRATION.md`: nine cite-only rows and three own-text `###` sections, so README `:26`'s
*"nine of its twelve obligations are already stated by rules elsewhere"* holds. `ONBOARDING.md`
has nine numbered items (`### 1`–`### 9`), matching README `:30`.

EXECUTION.md `:341`'s battery enumeration is internally consistent: *"these six commands"* =
*"One command, and nothing fewer"* (`:347`) + *"Five commands, and nothing fewer"* (`:352`).

**No member states a `dtw` command count**, so the eighth command this round added falsifies
nothing in the layer. `:341`'s *"six commands"* counts regression-battery legs, a different
enumeration — the candidate's own scan-class evidence said so and the grep bears it out. The
count sites that did move (`ONBOARDING.md`, `cli.py`, `test_cli_entry.py`) are all outside the
layer.

`ORCHESTRATION.md:27` asserts `dtw dispatch` has **three** modes and that none dispatches an
executor. Run rather than trusted:

```
$ python dtw.py dispatch --help          # run from tooling/
usage: do-the-work dispatch [-h] (--subject SUBJECT | --range RANGE | --read READ) …
```

Three, mutually exclusive: product evidence commit, construction range, `E10` layer read. None
is an executor dispatch.

### 3.5 `HD` ids the members cite

Thirteen distinct ids are cited across the ten members; all thirteen resolve.

```
HD-1 implemented   HD-2 implemented   HD-5 implemented   HD-7 implemented
HD-14 archive      HD-20 implemented  HD-28 archive      HD-34 live
HD-35 live         HD-39 archive      HD-41 live         HD-42 archive
HD-47 implemented
```

`§live` is unchanged at seven entries. `HD-51` was added to `§implemented` at the closeout and
is cited by no member, so nothing in the layer went dangling. Both files were grepped, not read
end to end; that is the ceiling on this line.

### 3.6 The two member edits — routing, and whether anything relied on them

`EXECUTION.md` +4/−0 (the SIMP-C4 wiring sentence, `:244-247`) and `REVIEW.md` +2/−1 (item 1's
holder clause, `:133-134`). Both landed in the candidate `57d1312`.

**`REVIEW.md`** is the `dd22789` read's `O-1` bytes applied verbatim. That read disposed `O-1`
as `R9` wording-level; the candidate body routes it *"per `R9`"* and the FULL routes it to
`E10`'s free channel. Both channels permit the identical act — apply the bytes in a batch
already touching this layer — and the path is not one `E2` freezes, so `HD-20` does not bank
it. The divergence has no outcome; see `O-1`.

**`EXECUTION.md`** is a design edit: it changes what a rule requires, so `E10` opens a round for
it, and the round it rode is the one whose user ruling authorized it (journal
`preview-render-2026-08-21.md`, in-round ruling 2). Correct on that count.

**Did any round rely on either before this read?** `E10` requires the independent read *before
any round relies on it*, and defines relying as *an outcome would change if the text changed*.
No:

- The FULL (`v3-review-full-57d1312.md:89-95`) names both edits, states that *"authoring is not
  relying"*, and defers the read here.
- The VERIFY (`v3-review-verify-15a53fe.md:169-172`) observes that the new sentence *"was the
  text the FULL said would become true once the code was fixed… it needed no edit"* — a
  statement **about** the text. Its verdict rests on the code (`:283-290` says it did not
  re-adjudicate the member edits). Change the sentence and no verdict moves.

So the general rule is satisfied on its own terms and the deferral clause — which buys the
stronger permission to *rely* before reading, at the price of two recorded facts — was never
the operative channel. Nothing is owed on that account.

### 3.7 The new sentence's factual assertions, run rather than read

`E3` binds a factual assertion written into instruction text to the command that could falsify
it. EXECUTION.md `:244-247` asserts the START card *"is rendered by `dtw preview` from the
frozen control plane — deterministic, re-derivable at any time and therefore never stored"*.

```
$ python dtw.py --help                   # run from tooling/
{governance-scan,status,flow,dispatch,disposition,review,init,preview}
    preview             deterministic pre-START rendering of a run's frozen control plane

$ python dtw.py preview --help
usage: do-the-work preview [-h] --run RUN
  --run RUN   the run directory (holds instruction.md and control/)

$ python -m pytest -q tests/document_harness/test_preview.py
22 passed in 1.44s
```

The command exists, is the eighth operation, and takes the run directory. Determinism is bound
by `test_rendering_twice_is_byte_identical` (`test_preview.py:295`), and `preview.py`'s module
docstring states the same two properties in the same terms. **Ceiling:** I did not re-render a
real control plane — the run directories live in the caller, not here — so "byte-identical on a
real plane" is the candidate's measurement, not mine; what I establish is that the module's
determinism has a test with binding force asserted over it, not that the test's force is
sufficient (`R4`).

`preview.py:178` reads `form = declared_form(instruction_text)` and `:182` prints
`form: {form or '(undeclared)'}` — it **renders any form and refuses none**. That is the fact
`L-1` turns on.

### 3.8 The guard, exercised rather than trusted

`E10` asserts what `layer_path_check` blocks. Tested with positive controls, because a probe
that blocks nothing may simply have failed to reach the code (`R8`):

```
PASSED   pathlike=False  .githooks/post-commit
PASSED   pathlike=False  document-harness/no-such-hook
PASSED   pathlike=False  tooling/hooks/no_such.sh
PASSED   pathlike=False  tooling/pyproject-nope.toml
PASSED   pathlike=False  docs/<placeholder>/x.md
BLOCKED  pathlike=True   document-harness/no-such-file.md      <- positive control
BLOCKED  pathlike=True   tooling/no_such_module.py             <- positive control
PASSED   pathlike=True   .harness/review-pending.json          <- runtime marker, E10 provides
```

The guard binds, the runtime-marker exemption behaves as `E10` states, and the blind-spot class
reproduces exactly — see `O-4`.

```
$ python -m pytest -q tests/document_harness/test_precommit_checks.py   # run from tooling/
49 passed in 18.76s
```

### 3.9 Commit ids cited in the layer

Twelve distinct commit-id-shaped backtick tokens are cited (scope: the ten member blobs; `E2`'s
`b2dbdf75…` / `68031fa2…` / `e1a2f26b…` are blob ids carrying an ellipsis and are excluded by
shape, not overlooked). Eleven are absent from this repository and are covered generically by
the checklist header's *Where a cited commit id resolves* clause, whose own referent was
checked: root `README.md:12` carries a *Where the bytes came from* section. The twelfth,
`0d73a5f` in EXECUTION `:387`, does resolve here and is written *"instrument `0d73a5f`"* — a
citation naming its own repository, read as written, exactly as the clause provides. The
caller-side id beside it is written *"caller `6fd0ae3`"*. No silent id is ambiguous.

### 3.10 README `:36`'s "single home" claim

Grepping the ten members for the two guards by module name returns two hits besides the README
row itself: CONSTRUCTION-CHECKLIST `:147` (describing `layer_path_check`'s own behaviour, which
is its own subject) and EXECUTION `:333` (naming it as a path-pinning file for the battery
tier). No second statement of the division of labour survives inside the layer, and the module
`preview.py` this round added restates nothing about it. The claim holds on the sweep that
would falsify it.

## 4. Findings

### `L-1` (low) — the SIMP-C4 wiring sentence carries an unscoped ruling inside a form-scoped bullet

**Location.** `document-harness/EXECUTION.md:244-247` (blob `27f4fc82`), inside the bullet
opening at `:240`.

**What the bytes say.** The bullet is the second of *"Two authoring consequences"* of the
**Instruction form** section, and its own second sentence sets its scope: *"**Under the
enumerated form** the WorkSpec is a transcript…"*. The sentence added this round continues in
that scope: *"Since round `PREVIEW-RENDER` (2026-08-21 ruling) the card is rendered by `dtw
preview` from the frozen control plane…"*.

**What it is scoped against.** Three things, none of them enumerated-only:

1. **The ruling.** The round journal states it unqualified — *"**a product run's** authorization
   body is its frozen control plane, and the plane's human-readable rendering is scripted"*
   (`document-harness/journal/preview-render-2026-08-21.md:3-7`). `HD-1`'s standing discipline
   is that instruction text expands under the ruling and, on conflict, the instruction text is
   what is wrong.
2. **The code.** `preview.py:178,182` reads the declared form and prints
   `form: (undeclared)` rather than refusing; §3.7. `dtw preview` renders a prose-form run.
3. **The sibling obligation.** `ORCHESTRATION.md:58` gives the orchestrator *"the START card for
   a product run"* with no form qualifier — and names no mechanism, because the mechanism is
   supposed to be the sentence above.

Grepping all ten members for `START card` / `dtw preview` returns exactly the sites in §3.2's
companion sweep: `EXECUTION.md:240,244` and `ORCHESTRATION.md:58`. **The layer's only statement
of how the START card is produced is the form-scoped one.**

**Ground truth violated.** `E3`'s standing on assertions in instruction text is met — the
sentence is true of what it says. What is not met is `HD-1`'s carrier discipline: the ruling's
scope and its carrier's scope differ, and the journal's own record of in-round ruling 2 (*"the
sentence is the carrier"*, no register entry) means this sentence is the **only** thing carrying
it.

**The downstream decision that goes wrong.** A **prose-form** product run's orchestrator, reading
the layer cold, has the obligation (`ORCHESTRATION.md:58`) and no sentence directing it to the
script — so it renders the START card the pre-`PREVIEW-RENDER` way, by session transcription:
exactly the failure the ruling removed, and the one `preview.py`'s own docstring names as *"a
transcription, with a transcription's failure mode"*. The bite is sharper than the frequency
suggests, because the same section makes prose *"the default, and the fallback"* and makes the
form resolution *fail-heavy*: a run that **declared** `enumerated` and failed the structural
check lands in prose, and would lose the script-rendered card precisely when its instruction is
least trustworthy.

**Why low and not must-fix.** Nothing acts wrongly today: no product run is open in this
repository, the caller holds the run directories, and `dtw preview` refuses no form, so an
orchestrator that reaches for it is not blocked — only un-instructed. It can wait for a round.

**Routing, and why I supply no bytes.** The fix widens what prose-form runs owe, which adds a
bound — so `E10`'s design test applies and the free channel is closed to it even though bytes
would be easy to write; per `R10` a rider for it names a **round-eligible** redeem-when surface,
never any batch, and `E10`'s amendment commit could meet its touch condition while being unable
to redeem it. It is also not wording-level, so `R9` does not take it: the bank does. And the
prior question is not mine (`R5`) — **was the 2026-08-21 ruling scoped to the enumerated form
or general?** I can see the journal's unscoped phrasing; I cannot see the conversation. If the
ruling was general the carrier is too narrow; if it was enumerated-only, then
`ORCHESTRATION.md:58`'s unqualified obligation is the half that wants a qualifier. Either way
one sentence moves, and which one is the user's call.

### `O-1` (observation) — two channels were named for the same bytes, with different read obligations attached

`REVIEW.md`'s edit is routed *"per `R9`"* by the candidate body and to *"the free channel"* by
the FULL (`v3-review-full-57d1312.md:89-92`). `R10` lists them in order — *"`R9` takes
wording-level, the `E10` free channel takes … any finding whose record supplies the exact
bytes"* — and this finding is both, so the order settles it for `R9`. The two attach different
read obligations: the free channel says *"a layer application still owes its independent read,
riding the next read of this layer"*, while `R9` says the finding *"rides the next batch
touching this layer and spawns no round and no read"*.

**Disposition — `R9` wording-level, banked, no round and no read.** Read in context, `R9`'s
clause means the finding spawns no *dedicated* read, not that member bytes escape the layer's
read cycle; `E10`'s free-channel clause states the general principle in adjacent text, so the
accurate fact is recoverable. **I can name no downstream decision that goes wrong**, because a
cold read derives its changed-member set by comparing blobs against the last recorded read
(§2), not from what a commit body claims it owes — which is how these bytes reached this read
regardless of which channel was named. Per `R9` it rides the next batch touching this layer and
spawns nothing.

### `O-2` (observation) — the rider bank points at two surfaces by line, and both lines have moved

Reported because a redeemer following either pointer lands on the wrong text. Neither file is a
member, so neither is in this read's subject; both were met while checking members.

- `HARNESS-RIDERS.md:17` (`E10-sync`) locates `EXPECTED` at
  `tooling/tests/document_harness/test_precommit_checks.py:176`. It is at **`:225-236`**
  (§3.3). The row's substance — three prose/code sites must move together — is unaffected.
- `HARNESS-RIDERS.md:42` (`amend-exempt-caller`) names *"`EXECUTION.md:380-381` 的角色标注"* as
  a redeem-when surface. The role annotations (*"instrument `0d73a5f`, caller `6fd0ae3`"*) are
  at **`:387-388`**, four of those lines moved by this round's insert (§3.2, §3.9). The touch
  condition itself did **not** arrive: `57d1312` edited `:244-247`, not the annotation.

### `O-3` (observation) — the previous read's `O-1` is discharged, and its `O-2` datum landed

Reported so the reproduction is on the record, not because either is new.

- `v3-cold-read-dd22789.md` `O-1` (REVIEW.md item 1 naming a caller-held artifact without its
  holder) is **closed**: `:133-134` now ends *"— the control root lives in the caller"*, the
  exact bytes that read supplied, and item 1 now matches its sibling item 2's *"The caller holds
  it; this layer does not write its path."* All twelve NAMETOKs carry a holder sentence (§3.2).
- That read's `O-2` datum **is** on rider `e10-cannot-see` — read off row 46 itself, not taken
  from the journal's disposition list: the row now carries the `` `tooling/hooks/no_such.sh` ``
  probe and the note that redemption edits two sentences.

### `O-4` (observation) — the guard's path-shape blind spot reproduces exactly

§3.8's probe lands on live rider `e10-cannot-see` (`HARNESS-RIDERS.md:46` — `:47` in the
previous read, shifted by this round's deletion of `review-record-loc`; source
`v3-review-verify-2538893.md` `V-3`): the extensionless form (`.githooks/post-commit`,
`document-harness/no-such-hook`), the outside-the-seven-extensions form (`.sh`, `.toml`) and the
placeholder-segment form all pass silently. The row's own live instance — README `:36`'s
`` `.githooks/pre-commit` `` — is still the only one in the layer, and it resolves, so nothing
is broken today. **Not a new finding**, and the row already carries the `dd22789` `O-2`
annotation that its redemption edits two sentences rather than one.

## 5. Coverage — what was read in full, what was sampled, what was only probed (`R4`)

- **Read in full at the subject blobs:** all ten members, 1 423 lines. Blob ids in §2. No
  citation is claimed for any member, although eight were citable.
- **Read by section:** `HARNESS-DECISIONS.md` header (1–27) and `§live` (28–133) in full, per
  `E10`'s tail. `§implemented` (135–487) and `HARNESS-DECISIONS-archive.md` were **grepped
  only**, for the thirteen ids §3.5 resolves — an `HD` entry whose *text* contradicted a member
  would not have been seen unless its id was cited.
- **Read in full outside the layer** (because a member's assertion turned on them):
  `tooling/hooks/layer_path_check.py`; `document-harness/journal/preview-render-2026-08-21.md`
  (its opening and ruling list, `:1-60`).
- **Sampled:** `tooling/rsclib/document_harness/preview.py` (module docstring, the form and
  SpecGap lines); `tooling/rsclib/document_harness/dispatch.py` (`READ_PROMPT`,
  `render_read_dispatch`, `CONSTRUCTION_ROLE_INSTRUCTION`);
  `tooling/tests/document_harness/test_precommit_checks.py` and `test_preview.py` (the
  hand-written constants and the test-name roster); `tooling/sweep_refs.py` (docstring and
  imports); `HARNESS-RIDERS.md` (row ids in full, three rows read in full);
  `v3-review-full-57d1312.md` and `v3-review-verify-15a53fe.md` (the passages §3.6 quotes, plus
  their coverage sections); `document-harness/ONBOARDING.md` (heading count only);
  `CONSTRUCTION-LEDGER.md` (line count only).
- **Only probed:** the guard's behaviour, by eight synthetic tokens with two positive controls
  (§3.8). Eight probes are not the class; they establish that the class is not empty, never its
  size.
- **Not attempted:** the full regression battery, and any render of a real control plane. This
  read changes nothing, so no tier is owed; two modules (22 + 49 tests) were run because the
  code they cover is the subject of §3.7 and §3.8. Every battery figure quoted in EXECUTION.md
  is explicitly revision-pinned and was not re-measured — a current figure would require running
  the battery, which `E3` says to do at the moment of the claim, and I make none.
- **Marked, not verified (`R4`):** that this read ran in a fresh context. It did, and that is a
  process claim with no evidence lock.
- **Authorization ceiling (`R7`):** the round's five in-round user rulings are visible to me only
  as the journal and the commit bodies record them — including ruling 2, on which `L-1` turns. I
  did not treat those records as anything more than the work side's own statement of what the
  user said, and `L-1` routes the scope question back to the user rather than resolving it
  against them. The closeout also reports caller-side obligations (gitlink bump, the caller's
  five battery legs, a router line) that I cannot see from this repository at all.
