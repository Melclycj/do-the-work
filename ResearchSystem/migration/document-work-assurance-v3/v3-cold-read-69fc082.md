# Cold read — the instruction layer at `69fc082`

`E10` read. Not a round (`R3`): no verdict, no budget spent, and the output is findings tiered
must-fix / low / observation. Routing is `E10` / `R9` / `R10`'s, not mine.

**Findings: 1 must-fix, 2 low, 4 observations.** The must-fix is the one the split left in the
layer's own header and nobody has looked for: `CONSTRUCTION-CHECKLIST.md` names the retired
contracts at `7011916` as **the reference of record for every question it is silent on**, and
that commit exists in no repository the instruction layer lives in — this repository's history
begins at `345acdd` and holds 44 commits. Sixteen of the layer's seventeen commit citations are
in the same state; only two sites anywhere say which repository a commit id belongs to. The
three deferred member edits this read is owed for — `30b33a9`, `acbc553`, `69fc082` — were
checked clause by clause and **hold**: the corrected pinning sentence in member 7 is true in all
three of its clauses (§3.5), and the two new navigation rows are accurate but for one wrong
direction word (`L-1`). The battery figure the subject commit reports reproduces exactly
(`733 passed`, §3.2).

**Named `cold-read` rather than `checkpoint-read`** on the `v3-cold-read-50016a8.md` precedent:
all ten members were read end to end at this subject, none by citation.

**Standing instructions read.** `…/v3-harness-review-contract.md` (the stub) →
`ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` in full, both sides, per the stub's
*"It is your standing instruction and its own counterpart; read all of it"*.
`ResearchSystem/HARNESS-DECISIONS.md` `§live` read in full as `E10`'s tail requires (`HD-49`,
`HD-50`, `HD-47`, `HD-44`, `HD-41`, `HD-36`, `HD-35`, `HD-34`, `HD-23`, `HD-9`) plus the file
header; from `§implemented`, `HD-38`, `HD-37`, `HD-46`, `HD-45`, `HD-21`, `HD-20`, `HD-2` by
grep, because claims I checked cite them. Cited by section, never by blob, per that clause.

---

## 1. Subject, re-derived

```
$ git rev-parse --show-toplevel
D:/Thesis-stage-control-refactor/ResearchSystem/harness

$ git rev-parse HEAD
69fc0827c445b64bec99d7b8a5745eba1784f2d9

$ git status --porcelain --untracked-files=all
(no output)

$ git log --oneline 69fc0827..HEAD
(no output)

$ cat .harness/review-pending.json
{
 "subject": "69fc0827c445b64bec99d7b8a5745eba1784f2d9",
 "dispatched_at": "2026-08-19T14:24:30+00:00"
}
```

Subject = branch tip, worktree clean and untracked-free, so the working-tree bytes **are** the
subject bytes for every member; that is proven per member in §2 rather than assumed, and
quotations that carry weight were taken from the object store. The statement is falsified by
exactly one path from the moment this file is written — this record, untracked until the
orchestrator commits it.

The marker's subject equals the dispatched SHA, so `E9`'s window opened at that timestamp and
closes when this record's commit lands; `git log 69fc0827..HEAD` is empty, so the branch has
taken no commit since dispatch and the window held. `R4` ceiling: I re-derived **that** it held,
not that any mechanism *made* it hold — in this repository none does (`.githooks/pre-commit`
runs `layer_path_check` and nothing else; rider `self-caller-guards`).

**Why this read is owed, and what it is paying for.** Three commits wrote instruction-layer
members after the last recorded end-to-end read of the layer (`v3-cold-read-7701f03.md`), and
each deferred its read to "the next read of this layer". This is that read.

```
$ git log --oneline --stat 7701f03..69fc0827 -- <the ten members>
69fc082 V3-LEDGER-SPLIT-CLOSEOUT-v1     document-harness/README.md | 1 +
acbc553 V3-LEDGER-SPLIT-v1              document-harness/CONSTRUCTION-CHECKLIST.md | 2 +-
                                        document-harness/README.md | 5 +-
                                        …/v3-harness-operating-contract.md | 2 +-
                                        …/v3-harness-review-contract.md | 2 +-
30b33a9 V3-LEDGER-SPLIT-FREE-L1-v1      …/v3-harness-review-contract.md | 2 +-
```

- `30b33a9` — a **free-channel** application (`E10`), its own commit per `HD-38`, replacing the
  false pinning sentence the `7701f03` read's `L-1` supplied bytes for. Verified §3.5.
- `acbc553` — five member sites, relied on under `E10`'s **deferral**, both facts recorded in
  the body ("adds no clause to any rule and changes what no rule requires", "its effect on
  rounds in flight is nil"). Verified §3.4.
- `69fc082` — one member site, same deferral, both facts recorded. Verified §3.4, with `L-1`,
  `L-2` and `O-2`.

## 2. The member set, and each member's blob

The set is `E10`'s own enumeration read **at the subject blob**, never from the dispatch: ten
paths, and the sentence's self-count *"exactly these ten paths and nothing else"* reconciles
with the enumeration. `E10`'s citation route for the next read depends on these ids, so each is
stated.

| # | member | blob at `69fc082` | lines | vs `7701f03` |
|---|---|---|---|---|
| 1 | `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` | `6ebbedabe544a84e60b98c347ee118c0c3b0aad7` | 212 | **changed** (`acbc553`) |
| 2 | `ResearchSystem/document-harness/README.md` | `49d7338fe759bb24c5f036a3d214d19b3489c84e` | 40 | **changed** (`acbc553`, `69fc082`) |
| 3 | `ResearchSystem/document-harness/EXECUTION.md` | `4a7b6eca3e8f4fd43c2887005c44a5e616d8b5da` | 465 | unchanged |
| 4 | `ResearchSystem/document-harness/REVIEW.md` | `3350bfac1b190cb1dac8566247f5382a7136f094` | 284 | unchanged |
| 5 | `ResearchSystem/document-harness/ORCHESTRATION.md` | `82f10c1bd173fb795c723df072a6357287d4d366` | 95 | unchanged |
| 6 | `ResearchSystem/migration/…/v3-harness-operating-contract.md` | `70f3e5dda9ce069489432a592a025b9da36cf0e0` | 5 | **changed** (`acbc553`) |
| 7 | `ResearchSystem/migration/…/v3-harness-review-contract.md` | `bc395e1c22af05aeacb0ed0b9813b66c8de75644` | 5 | **changed** (`30b33a9`, `acbc553`) |
| 8 | `ResearchSystem/contract/…-v3-supersession-1.md` | `68031fa2ca31272e31da0d42a9a02189d28fcc21` | 124 | unchanged |
| 9 | `ResearchSystem/contract/…-v3-supersession-2.md` | `e1a2f26b1d8d323d11e900f8137dea222b6571c1` | 113 | unchanged |
| 10 | `ResearchSystem/schema/document-assurance-v3/paragraph-map.schema.json` | `09aa869962f592c2f86c9379be0ef3eb7d2232ff` | 44 | unchanged |

**1 387 lines, none by citation.** Six of the ten (3, 4, 5, 8, 9, 10) were citable against
`v3-cold-read-7701f03.md`'s blob table and were read in full anyway, so this record may be cited
for any of the ten. Each row's blob was proven equal to the working-tree file:
`git rev-parse 69fc0827:<member>` against `git hash-object <member>` — **MATCH × 10**.

**`E2`'s frozen surface, checked rather than assumed.** The three named blobs are exact at the
subject — contract `b2dbdf752d8c…`, supersession-1 `68031fa2ca31…`, supersession-2
`e1a2f26b1d8d…` — and `git ls-tree 69fc0827 ResearchSystem/schema/document-assurance-v3/` returns
**15** files, the count `E2`'s parenthesis states. No `E2` write occurred in this range: the
diff of §1 touches none of those eighteen paths.

## 3. What I re-derived by command

**3.1 The membership sentence's three mirrors agree.** `E10`'s ten paths,
`layer_path_check.LAYER` (`:30–41`) and `test_precommit_checks.LayerMembership.EXPECTED`
(`:164–175`) are the same ten paths in the same order, compared by hand and then mechanically by
the suite in §3.2. Rider `E10-sync`'s three named sites are in sync at this subject; its
*unnamed* prose sites are that row's own business and I did not re-count them.

**3.2 The battery figure the subject commit reports reproduces.**

```
$ cd ResearchSystem/tooling && python -m pytest -q
733 passed in 97.71s (0:01:37)
```

The commit body's `733 passed in 110.72s`: count exact, wall-clock differs as wall-clock does.
`EXECUTION.md`'s own figures are pinned to revisions absent from this repository (`a8af54c`,
`ddd773a`, base `0d73a5f`) and the text tells the reader to re-run rather than trust them
(`HD-41` ③), so the drift from `712` to `733` is the rule working, not a defect.

**3.3 The README's other checkable figures hold.**

```
$ python …/N0/fixtures/validate_fixtures.py
41/41 cases behaved as declared; failures=0
```

- README `:35` "41/41 green" — re-run, not accepted.
- README `:22–25` schema enumeration — 15 pack files, 15 stems named across the four schema
  rows; pinned by `test_readme_enumeration.py`, green inside §3.2's run.
- README `:36` "it calls **two** of them, not three" (caller side) — the caller's
  `.githooks/pre-commit` `:61–62` loops over exactly `review_freeze_check.py` and
  `candidate_path_check.py`. Scope: the caller worktree on this machine at this moment.
- README `:36` "The third, instruction-layer path resolution, runs here … It guards this
  layer's ten members" — this repository's tracked `.githooks/pre-commit` calls
  `layer_path_check.py` and nothing else, and its `LAYER` is the ten (§3.1).
- README `:20` "What else lives in `ResearchSystem/contract/`" — that directory holds exactly
  three files, which are the three the row's own last sentence names as live v3 texts. The row
  is vacuous here; already reported (`v3-cold-read-28501fe.md` `O-3`) and not re-filed.

**3.4 The two deferred navigation rows, clause by clause.** Both are additions to the
*Authoritative documents* table, and both were disclosed as additions beyond the links their
commits set out to retarget.

| clause | result |
|---|---|
| `:30` "nine items" | `ONBOARDING.md` has nine numbered items under *The nine items* ✓ |
| `:30` "mount, instance files, policy file, pointer line, hook wiring" | five labels over nine items; item 2 matches none — `O-2` |
| `:30` "was executed against a throwaway caller on 2026-08-19" | `ONBOARDING.md` *Execution record* states it, with three ceilings of its own ✓ |
| `:30` "not an instruction-layer member … its own header saying so" | `E10` does not name it; the header says exactly that, and `journal/caller-onboarding-2026-08-19.md` §1 records the `HD-21` question and its answer ✓ |
| `:32` "Both arrived from the caller 2026-08-19" | `acbc553` ✓ |
| `:32` "the record side of the checklist below" | the checklist row is `:27`, five rows **above** — `L-1` |
| `:16` plan link + `plans/` | resolves; the directory holds 16 plans ✓ |
| `:39` Predecessors v2-plan link | resolves ✓ |

**3.5 The free-channel byte at `30b33a9` is true in all three clauses.** This is the correction
`7701f03`'s `L-1` bought, and it is the one member sentence this read most owed:

- `dispatch.CONSTRUCTION_ROLE_INSTRUCTION` (`…/rsclib/document_harness/dispatch.py:545–547`)
  hard-codes the member — instrument-relative, resolved per subject repository by
  `instrument_relative` ✓;
- `test_dispatch.py` pins it independently by hand: `CHARTER_OUTSIDE` (`:398`, `:520`) and
  `MEMBER` (`:463`), none read back from the module — `E5` as designed ✓;
- `tests/fixtures/expected-construction-prompt.txt` carries the literal `{charter}`, not the
  path ✓.

The dispatch I received is itself the demonstration: it is `READ_PROMPT` verbatim with the
charter resolved to `ResearchSystem/migration/…/v3-harness-review-contract.md`, one SHA and no
per-acceptance argument (`E12`).

**3.6 Path resolution across the whole layer, re-derived not accepted.** Scope declared: every
Markdown link target and every backticked path-shaped token in all ten members; "resolves" means
lands inside **this** repository. Result — 13 sites:

| site | token / target | status |
|---|---|---|
| `REVIEW.md:45` | `…/v3-review-full-fef3a2e.md` (link) | rider `layer-outbound-refs` |
| `EXECUTION.md:186`, `:449` | `ResearchSystem/assurance/runs/p5a-shells/control/audit-rounds.md` | rider `layer-outbound-refs` |
| `EXECUTION.md:452` | `…/p4-doc/issues/user-decision-triage-comparator-environment-defects.json` | rider `layer-outbound-refs` |
| `EXECUTION.md:343`, `:345`, `:346`, `:347` | the caller battery scripts | self-disclosed in the same sentence |
| `supersession-1:89`, `supersession-2:60`, `:83`, `:99` | four missing-prefix tokens | rider `frozen-path-prefix`, `E2`-frozen (`HD-20`) |
| `EXECUTION.md:340` | `ExperimentLab/papers/` | **accounted for by nothing** — `O-1` |

This reproduces the `layer-outbound-refs` row's own enumeration exactly — four references, three
targets — which is the rider byte the subject commit landed (the row had said 两处 backtick
tokens where its enumeration names three). The one site the bank does not account for is `O-1`.

**3.7 Commit citations across the whole layer — the scan that found `M-1`.** Same discipline
applied to the other citation form. Scope: every backticked 7–40-char hex token in the ten
members, resolved with `git cat-file -t` in **both** repositories.

| token | this repo | caller | sites |
|---|---|---|---|
| `0d73a5f` | commit | – | `EXECUTION.md:380` |
| `6fd0ae3` | – | commit | `EXECUTION.md:381` |
| `7011916` | – | commit | `CONSTRUCTION-CHECKLIST.md:5`, `:10`; both stubs `:4` |
| `418b89c` | – | commit | `EXECUTION.md:404` |
| `820b287` | – | commit | `README.md:36` |
| `838c413` | – | commit | `EXECUTION.md:330` |
| `9ba9bbc` | – | commit | `EXECUTION.md:439` |
| `a22cca0` | – | commit | `EXECUTION.md:249` |
| `a8af54c` | – | commit | `EXECUTION.md:378` |
| `ac1b383` | – | commit | `README.md:18`, `EXECUTION.md:109`, `REVIEW.md:65` |
| `cf51534` | – | commit | `supersession-2:32` |
| `ddd773a` | – | commit | `EXECUTION.md:376` |

Seventeen sites, twelve tokens. **Sixteen sites name a commit this repository does not have**;
all sixteen resolve in the caller worktree on this machine. Two sites — `EXECUTION.md:380–381`,
*"its bases: instrument `0d73a5f`, caller `6fd0ae3`"* — say which repository they mean; the
other fifteen do not. `layer_path_check` cannot see any of them: its class is backtick tokens
that look like paths.

## 4. Findings

### `M-1` (must-fix) — the reference of record for the checklist's own silences is in no repository the layer lives in

`CONSTRUCTION-CHECKLIST.md:9–12` is not a citation; it is a **choice-of-law clause**:

> **This file is the operative rule set, not a complete replacement.** Where it is silent on a
> question a round actually faces, the retired contracts at `7011916` are the reference of
> record; the silence is not a defect, and closing it rides the next batch under R9 rather
> than opening a round.

Four sites depend on that commit — `:5` ("full text at `7011916`"), `:10` (above), and both
retired-contract stubs at `:4` (`git show 7011916:…`, the only route to 683 lines of text the
stubs exist to point at). It does not exist here:

```
$ git cat-file -t 7011916
fatal: Not a valid object name 7011916

$ git rev-list --max-parents=0 HEAD
345acdd19dd73ecace4d1a122e290298b8c8a4c8

$ git rev-list --count HEAD
44
```

This is structural, not a bad abbreviation: the instrument repository was created by extraction
(`345acdd`, 2026-08-15) and carries none of the caller's history. The commit is reachable in the
caller worktree on this machine (`git -C D:/Thesis-stage-control-refactor cat-file -t 7011916`
→ `commit`), and **nothing in this repository says so**:

```
$ grep -rn "7011916" <this repo, *.md *.py> | grep -iE "caller|调用者|D:/Thesis|do-the-work"
(no output)
```

*Why must-fix rather than low.* `R9`'s wording-level test fails on both halves. The fix changes
an actor's action — where a session goes when the operative rule set is silent, which is the
case this clause exists to legislate for — and the accurate fact, which repository holds the
commit, is **not** recoverable from adjacent text or from any committed record here (the command
above is that check). It is also not the `layer-outbound-refs` class: those are witnesses behind
claims, this one is the named governing text. And every previous confirmation of it was made in
the caller before the split — `v3-checkpoint-read-377d591.md:203` says "`7011916` still resolves
and still carries both contracts in full" — so the property was inherited across the extraction
and never re-established here, which is the shape `E3` and `HD-41` exist for.

*Minimum fix, and the defect class it must sweep.* No bytes supplied; the disclosure form is the
executor's to write, and the layer already demonstrates one at `EXECUTION.md:380–381` (label the
repository beside the id). `E10`'s must-fix channel admits "that same fix at every other site of
the defect the finding names", and the defect named here is **a commit id in an instruction-layer
member that resolves in no repository the layer lives in** — §3.7 is the list, so the sweep is
not a discovery: fifteen unlabelled sites, four of them `7011916`. A channel narrowed to the four
would leave eleven siblings to be found one re-read at a time (`HD-36` ①).

*`R5` half, for the user and not for me:* whether the reference of record should be **reachable
from the instrument at all** — copied in, or replaced, or the clause dropped — is a question
about what should exist. A second caller, which is what the split was for, can reach neither the
commit nor any statement of where it lives. Deleting or re-pointing the clause changes what a
rule requires and opens a round; labelling the id does not.

### `L-1` (low) — `README.md:32` points the wrong way to the checklist

The construction-ledger row describes itself as *"the record side of the checklist below"*. The
checklist row is `:27`; the ledger row is `:32`. Everything below it is N1, N2, fixtures and
local enforcement — a reader following the direction word finds no checklist. The row also never
names the file, so the direction word is the whole pointer.

*Downstream decision:* none nameable — the row five above is unmissable in a 21-row table, and
`CONSTRUCTION-LEDGER.md`'s own header states the same relationship naming the file. So this is
**wording-level under `R9`** and rides the next batch touching this layer; it is filed at low
rather than observation only because the row was written by the round immediately preceding this
read, and is one of the bytes this read is paying for. Bytes are available and add no clause
("above", or naming `CONSTRUCTION-CHECKLIST.md` as the ledger's own header does), so the `E10`
free channel is open if the orchestrator prefers it.

### `L-2` (low) — one round applied `HD-38` both ways, three commits apart

`HD-38` rules that free-channel bytes travel in **their own commit**. The `LEDGER-SPLIT` round
did that for `7701f03`'s `L-1` — `30b33a9`, whose body cites `HD-38` by name — and then landed
`7701f03`'s `L-3` fix inside `69fc082`, a nine-path closeout that also carries two decision-log
entries, the ledger roll, the records batch and a rider byte.

The two are the same shape. `L-3` is a low finding whose record **names the content** ("naming
the file supplies bytes and adds no clause, so the free channel is open"), and `R10` states the
route explicitly: the `E10` free channel takes any finding whose record supplies the exact bytes
or names the content, and *"neither the tier they were filed at nor whether a read or a FULL
produced them changes the route"*. The closeout body routes it elsewhere — "disclosed under
`E10`'s deferral" — but the deferral clause governs *when an amendment may be relied on before
its read*, not *which channel a finding's fix travels*; an amendment can satisfy both, and this
one did.

*What changed:* which commit a free-channel byte landed in, and therefore whether it is separable
at the diff level — the property `HD-38`'s 后果 line names as the point of the rule. Nothing
about the bytes themselves; §3.4 finds them accurate.

**Bytes deliberately not supplied.** The two readings of `HD-38` — "own commit, period" versus
"the mischief is bundling with must-fix answers" — are both available in its text, and its one
instruction-layer carrier (`R10`'s "an `E10` amendment commit admits only the answers to a read's
must-fix findings") speaks about a different artifact. Any tiebreak adds a bound, which is design
and opens a round (`E10`). Same shape as rider `wl-route`, which already records a two-versus-one
routing split for exactly this class of finding; this is that ambiguity observed in the wild, and
it belongs with that row rather than beside it.

### Observations

- **`O-1` — `EXECUTION.md:340`'s `ExperimentLab/papers/` is accounted for by no row in the
  bank.** Scope: §3.6's sweep, the same scope rider `layer-outbound-refs` declares for itself
  (link targets + backticked path tokens in the ten members, resolving inside this repository).
  It is not among that row's four, and not among its explicit *不属本行* list either (the five
  caller battery paths, the two `.harness/review-pending.json` runtime sites, the four
  `E2`-frozen tokens). `layer_path_check` skips it by design — it neither starts with
  `ResearchSystem/` nor resolves under it, so it falls in the may-be-illustrative class. The
  sentence is **not false**: it reads "from a repository root that also carries the product,
  collection aborts", and that root is not this one. Measured, because the bullet states the
  instrument's own obligation: `python -m pytest -q --collect-only` from **this** repository's
  root returns `733 tests collected in 0.24s` — the named failure mode cannot occur here, and the
  working-directory constraint the parenthesis justifies is a caller-context fact. `HD-50`'s R2
  B-class scan names `REVIEW.md:45` and `EXECUTION.md:186/:449/:452`; this site is not in that
  list and would survive it.
- **`O-2` — `README.md:30`'s five labels do not cover the nine items they gloss.** "nine items:
  mount, instance files, policy file, pointer line, hook wiring" maps onto items 1, 3–6, 7, 8, 9.
  Item 2 — `.harness/` and its `.gitignore` entry — matches none of the five, and it is the one
  item a caller most easily leaves undone (the directory is ignored on purpose, so nothing about
  it travels with a clone). The count "nine" is right and the link is right, so this is
  wording-level; bytes are available and add no clause.
- **`O-3` — `REVIEW.md:134–135` gives a product-run reviewer one hard-coded record path.** The
  `ReviewResult` is placed relative to the control root and travels; the prose record is
  `ResearchSystem/migration/document-work-assurance-v3/v3-review-<round>-<sha>.md`, justified as
  "repo naming precedent" — a directory that exists in this repository and in the caller that
  grew the harness, and in no other caller. Rider `chk-caller-prefixes` already records the
  mirror half (the candidate-path checker's hard-coded record-surface prefixes break for a caller
  that puts records elsewhere) and gives the biting moment as "第二个真调用者接线该守卫的时刻".
  This is the same moment and the same cause, one layer up: the rider names the checker, no row
  names the instruction that tells the reviewer where to write. Fix is design either way (naming
  a caller-configurable location adds a bound), so no bytes.
- **`O-4` — the subject commit's body attributes the `ONBOARDING.md` row to the wrong read.** It
  says "closing the CALLER-ONBOARDING opening read's `L-3`". `CALLER-ONBOARDING`'s opening read is
  `v3-cold-read-c22e229.md`, which has no `L-3` (`grep -n "L-3"` → no output); the finding is
  `v3-cold-read-7701f03.md`'s `L-3`, the `LEDGER-SPLIT` opening read. One hop, recoverable by
  grep, and a commit body cannot be edited — recorded here so the trace exists, with no action
  proposed. Also noted and **not** filed: the same body reports the construction ledger at "149
  lines against its declared 180"; `wc -l` returns 148 and the file ends in a newline, so the
  count is off by one. Neither is a member; both are record-side.

## 5. Coverage, and the ceilings on it (`R4`)

**Read in full:** all ten members at the subject blob (1 387 lines, §2); `HARNESS-DECISIONS.md`
`§live` in full plus its header; `HARNESS-RIDERS.md` in full (34 data rows, to route findings
rather than re-file banked ones); the three commit bodies of §1 in full;
`v3-cold-read-7701f03.md` §1–§2 and its `L-3`/`O-1`, `v3-cold-read-28501fe.md` in full, and
`v3-cold-read-50016a8.md`'s naming paragraph — all as routing evidence, never as verdict basis.

**Read to settle a specific claim, not in full:** `layer_path_check.py`,
`test_precommit_checks.py` `LayerMembership`, `test_readme_enumeration.py`,
`dispatch.py` (`instrument_relative`, the three dispatch families, both prompts),
`test_dispatch.py` by grep, `expected-construction-prompt.txt`, `ONBOARDING.md` (header,
item list, execution record), `journal/caller-onboarding-2026-08-19.md` §1,
`CONSTRUCTION-LEDGER.md` header, both `.githooks/pre-commit` files.

**Probed only:** the run-v2 template directory listing; the `rsclib` instruction module
(`resolve_form`, `transcript_audit` presence).

**Ceilings, stated rather than folded into supported:**

- Every figure `EXECUTION.md` pins to `a8af54c`, `ddd773a` or the caller's five battery legs is
  **`UNVERIFIABLE` from here** — those revisions and scripts are not in this repository. The text
  says so for the scripts and tells the reader to re-run for the figures; I re-ran the one leg
  this repository owes (§3.2) and left the rest unverified rather than reasoning about them.
- The caller-side clauses in README `:36` were checked against **the caller worktree on this
  machine at this moment** (`D:/Thesis-stage-control-refactor`). That is not a repository
  property and not a claim about any published revision.
- `EXECUTION.md:283`'s "the run's `write_audit.py`" names a run-local script; the run-v2 template
  ships eight files and none is that one. Whether a run authored from the template has such a
  script is a caller-side fact — `UNVERIFIABLE` here, and not filed.
- `M-1`'s caller-side half rests on the same worktree. That `7011916` is absent **here** is a
  property of this repository and is proven by `rev-list`; that it is present *there* is a
  statement about one machine.
- Process claims — that this read ran in a fresh context, that no material reached me but the
  dispatch — are marked, not verified. `R2`'s derive-everything rule was followed: the member set
  came from `E10`'s sentence at the subject, every count from a command re-run here.

## 6. Already on the books, not re-filed

Standing at this subject and reported by earlier reads or carried in the bank; re-stating them as
new findings would inflate the count:

- `E10`'s closing provenance clause still has no live subject (`v3-cold-read-7701f03.md` `O-1`);
  `HD-50` schedules its deletion on R2/R3's design surface.
- `R<n>` names three different things inside the layer, and `EXECUTION.md:232` backticks `R0` in
  the instruction-section sense (`v3-cold-read-28501fe.md` `O-2`).
- README `:20`'s contract-directory row is vacuous here (`28501fe` `O-3`, re-measured §3.3).
- Riders `layer-crossrepo-token`, `layer-outbound-refs`, `frozen-path-prefix`, `E10-sync`,
  `e1-disclose-home`, `charter-qualifiers`, `charter-prose-overreach`, `waiver-live`, `wl-route`,
  `chk-thin`, `HI-route` — all read, all still standing, none redeemed by this range.
