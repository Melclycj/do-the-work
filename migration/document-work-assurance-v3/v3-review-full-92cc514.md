# FULL review — `cc3b3ab..92cc514` (round `CORE-SET-LAYER`, batch `CORE-SET`, round 1)

Independent FULL. Subject received as one range and nothing else (`R2`); round identity,
budget, authorization, obligations and every figure below are re-derived from the repository.
Standing instructions: `migration/document-work-assurance-v3/v3-harness-review-contract.md`,
which is a stub superseding to `document-harness/CONSTRUCTION-CHECKLIST.md` — read whole, in
the form the subject tip carries, and it is its own counterpart. `HARNESS-DECISIONS.md`
`§live` read whole at the tip (`HD-56` `HD-44` `HD-41` `HD-36` `HD-35` `HD-34` `HD-23` `HD-9`,
plus the header's mechanism block).

**Verdict: `CHANGES_REQUIRED`.** 2 blockers, 8 lows, 3 observations. Both blockers are prose,
both sit inside deliverables this round authored or edited, and both are fixable inside the
round's declared change boundary.

---

## 1. Subject and round, re-derived

```
$ git rev-parse HEAD                         -> 92cc514cbbe3ed3e07992283ce35299b5dc2042c
$ git status --porcelain                     -> ?? .goals/        (untracked only)
$ git log --oneline cc3b3ab..92cc514 | wc -l -> 9
$ git rev-list --count origin/main..HEAD     -> 22                (nothing pushed, E8)
```

Nine commits, classified by hand from their own trees rather than from their titles:

| commit | items | kind, by `E9`'s test rather than by name |
|---|---|---|
| `c0b9316` | A + D | candidate |
| `c39536b` | B + C | candidate |
| `4f4dc4b` | E | candidate (the `HD-54`→`HD-58` supersession rides it) |
| `60d668f` | I + J | candidate |
| `806efca` | K | candidate |
| `eba47ad` | L | candidate |
| `6396468` | rulings 16/17 | orchestrator bookkeeping (plan only) |
| `c5f00f6` | M | pre-submission correction — correct: no independent FULL had occurred |
| `92cc514` | — | orchestrator bookkeeping (round journal + plan step marks) |

`E9` going in, derived: the round's only prior review-side event is the opening cold read at
`9f1de08` — a read, so no verdict and no budget. This is the round's one FULL, the fix leg is
unspent, and a targeted VERIFY falls due only if a fix is approved. Item M's self-classification
as a pre-submission correction is right by `E9`'s own question and is not a renamed round.

**Change boundary held.** Paths touched, classified by hand:

- **Instruction-layer members (5 of 9):** `CONSTRUCTION-CHECKLIST.md` · `README.md` ·
  `EXECUTION.md` · `REVIEW.md` · `ORCHESTRATION.md`.
- **Frozen bytes (`E2`): untouched.** `git rev-parse {cc3b3ab,92cc514}:contract/…-v4.md` both
  return `dfc983d2e3d9fb5ca67b053a16fcfb0e6715b11a`, the blob `E2` names;
  `git diff --name-status cc3b3ab..92cc514 -- schema/document-assurance-v3/` → 0 lines.
- **No code, no tests, no schemas:** `git diff --name-status cc3b3ab..92cc514 -- tooling/
  assurance/ .githooks/` → 0 lines.
- **One deletion:** `document-harness/history/REVIEW-v1-package-flow.md`, the single explicit
  exception the plan's *Out of scope* carves out under ruling 13.
- Registers, plan, journal and the two new root files complete the list.

Authorization, from committed state only: `document-harness/plans/core-set.plan.md` carries
seventeen user rulings and is named by `CONSTRUCTION-LEDGER.md` as the batch's carrier. The
`E11` card is not on disk — construction-round cards are ruled not to be committed (ledger,
2026-08-21) — so its approval is a process claim I mark rather than verify (`R4`, `R7`).

The freeze marker carries exactly this range and the branch has taken no commit since the
journal, so `E9`'s window holds:

```
$ cat .harness/review-pending.json
{"subject": "cc3b3abb…..92cc514c…", "dispatched_at": "2026-08-25T16:48:58+00:00"}
```

---

## 2. Implementation first (`R3`) — what the round claims, and what the commands say

### 2.1 The measurement the round exists to move — reproduced, and it holds

I rebuilt both stripped trees myself (`git archive` → delete `migration/` except the two member
stubs, `document-harness/journal/`, `document-harness/plans/`, the five root registers,
`CONSTRUCTION-INDEX.md` → `git init && git add -A`) and ran the committed
`tooling/sweep_refs.py`, counting only `LINK` and `PATHTOK`:

```
cc3b3ab stripped: 124 tracked, 52 total sweep hits, 31 LINK+PATHTOK
92cc514 stripped: 124 tracked, 41 total sweep hits, 13 LINK+PATHTOK
unstripped HEAD :                15 total sweep hits
```

**31 → 13 confirmed.** All thirteen residuals enumerated, and each matches the journal's
accounting exactly: 3 construction-side (`CONSTRUCTION-CHECKLIST.md:6`, both stubs `:3`), 2 for
the one ruled-dangling site (`REVIEW.md:93`, `LINK` + `PATHTOK`), 1 at
`document-harness/README.md:16`, 7 in contract v4 (`:16 :25 :27 :30 :32 :253 :341`). Nothing in
the residual set is unexplained.

`ONBOARDING.md` is not a member and the sweep never scans it, so I re-ran the register grep over
base and tip: `cc3b3ab` returns `:16 ../HARNESS-DECISIONS.md` and `:100 ../HARNESS-DECISIONS.md`
beside two bare names; the tip returns three bare names and zero prefixed tokens.
**2 → 0 confirmed.**

**Acceptance 1 holds.** Over `ORCHESTRATION.md`, `EXECUTION.md`, `CONSTRUCTION-CHECKLIST.md` and
`ONBOARDING.md`, zero path-shaped references into the decision log, rider bank or construction
ledger survive; the bare names ruling 1 preserved are still there (`ORCHESTRATION.md:51`,
`CONSTRUCTION-CHECKLIST.md:151` and `:212`, `ONBOARDING.md:99 :101 :107`).

**Acceptance 2b holds.** Member sites citing `plans/` `journal/` `history/` stand at five: the
three ruling-12 sites, contract v4 `:32` (deferred to round 2, `E2`), and `REVIEW.md:93`
(ruling 13). `EXECUTION.md:399` and `README.md:37` are gone.

### 2.2 The table split (item D) — counted, not accepted

```
README table rows: 19 at cc3b3ab -> 11 at HEAD   (10 kept + 1 naming the index)
CONSTRUCTION-INDEX.md rows: 9
```

Acceptance 2's arithmetic holds. I diffed each moved row against its source: eight moved with
link rebasing and the two relative-position rewrites only, the fixtures row's `41/41` carried as
a byte. The ninth — the decision-log row — was substantively rewritten by item A in the same
commit; that rewrite is disclosed, the sentence claiming otherwise is not (low L-8).

### 2.3 The supersession (item E) — the invariant is met by command

```
cc3b3ab : HD-54 in §implemented(1) archive(0) HD-58(0)
c39536b : HD-54 in §implemented(1) archive(0) HD-58(0)
4f4dc4b : HD-54 in §implemented(0) archive(1) HD-58(1)
```

`HD-54` leaves `§implemented`, lands in the archive whole with its original status text
preserved, and `HD-58` appears carrying the narrowed obligation in full with pointers both ways
— all in one commit, which is what `HD-30` and the log's own invariant require. The ledger stayed
at exactly 180 lines (`wc -l`: 180 at `cc3b3ab`, 180 at `4f4dc4b`, 180 at the tip) and the
archive moved 291 → 309, matching the `HD-6` note the same commit wrote.

### 2.4 The re-points (item L) — each followed to its claimed holder

`io-design.md` is provably untouched: blob `a1594eb27311cfe4cdc1aa32c32a521c0af4b65f` at
`cc3b3ab`, at `92cc514`, and by `git hash-object` on the worktree file.
`grep -n io-design document-harness/ONBOARDING.md` returns four lines — items 4, 5, 6 and 7 —
and each is named in the banked rider `onboarding-io-design-owners`. Acceptance 2d's shape holds.

I read each re-pointed target rather than trusting the citation:

- item 3 → `templates/decision-log.md`'s header: carries all eight things the See cell now lists
  (state machine, four scopes, three admission questions, the *Who reads it* inheritance block,
  deletion, narrowing, invariants, entry shape). ✓
- item 7 → `ORCHESTRATION.md` *Reading the caller's policy file*: carries the three properties
  verbatim in substance. ✓
- item 8 → same section: carries "the caller's own agent-facing entry file points at it, and that
  pointer is the only discovery path this layer gives a cold orchestrator". ✓
- item 5 → `HD-1`: carries what a journal is for; **does not carry the one-file-per-round
  shape** (low L-4).

### 2.5 Do the guards bind? (`R8`) — and one method correction

The commit bodies repeatedly say `layer_path_check.py exits 0 on the staged tree`. Run with
nothing staged that is a **vacuous pass** — the guard scans only the staged diff's added lines,
so an empty index exits 0 having scanned nothing. My own first invocation had the same defect and
I am not counting it.

What I ran instead: replayed every line this round **adds** to a member through
`layer_path_check.unresolved_tokens`, with a positive and a negative control.

```
POSITIVE CONTROL `document-harness/nope/missing.md` -> 1 hit  (guard fires)
NEGATIVE CONTROL `document-harness/EXECUTION.md`    -> []     (guard silent)
CONSTRUCTION-CHECKLIST.md   8 added lines -> []
README.md                   6 added lines -> []
EXECUTION.md               17 added lines -> []
REVIEW.md                   3 added lines -> []
ORCHESTRATION.md            1 added line  -> []
TOTAL unresolved added path tokens: 0
```

`review_freeze_check.py` also binds, checked by its own predicate rather than by an empty run:
`is_record("migration/document-work-assurance-v3/v3-review-full-92cc514.md")` → `True`,
`is_record("document-harness/README.md")` → `False`, marker present. Acceptance 4's substance
holds; the evidence the commit bodies offer for it does not, which is a method note rather than a
finding, since the substance checks out.

The round wrote no new guard, so `E4` does not fall due and there was nothing to mutate beyond
the controls above.

### 2.6 The rest of acceptance, by command

```
$ python -m pytest -q       -> 854 passed in 459.64s        (acceptance 3)
$ E10 members resolve       -> 9/9                          (acceptance 4)
$ dtw init into fresh repo  -> exit 0, "5 created"; decision logs found: 1   (acceptance 5)
$ grep waiver-live HARNESS-RIDERS.md -> (none)              (acceptance 6, row deleted in c0b9316)
```

Product tier re-measured rather than accepted: 1 + 15 + 4 + 1 + 2 + 2 + 22 + 12 = **59 files**,
**0.729798 MiB** — both figures correct. The repository denominator is not (low L-1).

---

## 3. Blockers

### B-1 — `CORE-SET.md` states a sufficiency its own contents falsify, and the round's instrument cannot see it

**Location.** `CORE-SET.md:22` — "A repository that mounts this instrument needs these and
nothing else to open, run and close a round" — reinforced by entry 3's "the ones a product run is
actually governed by".

**Ground truth it violates.** The same file's construction tier places
`document-harness/CONSTRUCTION-CHECKLIST.md` outside the product tier, and every one of the five
product-tier documents points into it:

```
$ grep -n CONSTRUCTION-CHECKLIST over the product tier
document-harness/README.md:23        [markdown link]
document-harness/EXECUTION.md:13     [markdown link]
document-harness/REVIEW.md:8         [markdown link]
document-harness/ORCHESTRATION.md:7 and :39    [markdown links]
document-harness/ONBOARDING.md:109   "`R10` in `CONSTRUCTION-CHECKLIST.md` for the rules"

$ backticked E*/R* rule citations in the five product-tier documents
README 1 · EXECUTION 4 · REVIEW 1 · ORCHESTRATION 20 · ONBOARDING 10   = 36 over 27 lines
```

`ORCHESTRATION.md`'s obligation table states its own contract as "It does not restate them — read
the rule", and the rules it points at are `E9` `E10` `E11` `E12` `R1` `R5` `R6` `R10`.
`ONBOARDING.md` item 4 tells a caller in words where its own rider-bank rules live. A repository
carrying the product tier and nothing else has five dead links and one dead instruction. `E3` is
the rule this lands under: a characterization no command established, written flat rather than
marked.

**Why nothing in the round caught it.** Acceptance 1's strip removes construction *history* and
keeps `CONSTRUCTION-CHECKLIST.md` — correctly, it is a member. So the round never once exercised
the manifest `CORE-SET.md` defines, and `sweep_refs.py` cannot: it scans the nine members against
a tree that still holds the checklist. The measurement and the claim are about different trees.

**Minimum fix.** `CORE-SET.md` states this residual the way this round states every other one —
the surface, the count, and which round settles it — or drops "and nothing else" for a bounded
claim. Moving the checklist into the product tier would contradict ruling 11 and is the user's
call, not the fix; and per `E6` a new rule about the citations is not the fix either.

### B-2 — rider `waiver-live` was deleted on a class-closure claim the grep falsifies, and the surviving carrier is the only one a caller has

**Location.** `c0b9316`'s body: "the class is closed rather than reduced and no row is
re-banked". Surviving carriers: `document-harness/templates/decision-log.md:11` and this
instrument's own instance `HARNESS-DECISIONS.md:7`.

**Ground truth it violates.** The deleted row (`git show cc3b3ab:HARNESS-RIDERS.md`) names
**three** sites, not two: the checklist's waiver clause, `README:29`'s "every cold read MUST", and
决策簿头部 — the decision-log header, which the row records as equally silent. Two were fixed.
The third is intact:

```
$ grep -rn "cold read MUST|每轮 cold read" --include=*.md .
document-harness/templates/decision-log.md:11  > **Who reads it.** Every cold read MUST read `§live`, and only `§live`.
HARNESS-DECISIONS.md:7                         > **谁读**：每轮 cold read **必读 §live**（且仅 §live）
```

That is verbatim the sentence the rider says dangles when the opening's cold read is waived, and
the rider's recorded harm is precisely this: one session reads `§live`, another cites the waiver
and skips, missing live rulings. `HD-41` ④ requires the scan-class grep output to sit in the
commit body before a finding is written off; `c0b9316` carries none, and `E3` drops rather than
softens a characterization no command established. `R10` makes redemption "the fix rides a batch
already touching that surface" — deleting the row without the fix loses the finding.

**What compounds it, and why this is not merely an unfixed sibling.**
`templates/decision-log.md` is what `dtw init` copies verbatim to a caller's root, and this same
round elevated its standing twice: `CORE-SET.md` entry 5 calls it "the carrier of a rule, not a
convenience", and item L rewrote `ONBOARDING.md:101` to say "The rules of the log live **in the
log's own header**, not in the instruction layer". Meanwhile item K puts
`CONSTRUCTION-CHECKLIST.md` — where the fix landed — outside the product tier. For a caller the
class is not reduced but untouched, and the only statement of the obligation it can read is the
un-amended one.

**Minimum fix.** Amend `templates/decision-log.md`'s *Who reads it* sentence to state the
obligation on the round's opening regardless of a layer cold-read waiver, mirroring the `E10`
clause this round wrote — or re-bank `waiver-live` naming that carrier. The template is not an
`E10` member and not an `E2` path, so neither channel is blocked. `HARNESS-DECISIONS.md:7` and
`HD-19`'s own ruling text are the same phrasing in this instrument's own register; whether they
ride is the orchestrator's call, not a condition of the fix.

---

## 4. Lows — none of these is worth the single repair on its own

- **L-1 · `CORE-SET.md:24` — the denominator is measured before the file it lives in.** It states
  386 tracked files. `git ls-tree -r --name-only 806efca | wc -l` — the commit that wrote the
  file — returns **387**; HEAD returns **388**; 386 is the count at `60d668f`, i.e. before
  `CORE-SET.md` was staged. `E3` measure-last. The 6.33 MB figure is right (worktree `stat` scope
  under `core.autocrlf=true`, MB read as MiB), as are 59 and 0.730. `806efca`'s body says all
  four were "re-measured on this tree"; three were.
- **L-2 · the round journal's stripped-tree file count is off by one.** §1 says "124 files
  before, 125 after (`CORE-SET.md` is the addition)". Both trees measure **124**: item I's
  deletion of the history file offsets `CORE-SET.md`, and the two trees differ by exactly that
  pair. `c5f00f6`'s body has it right at 124. `HD-23` routes a journal *number* correction
  outside the `E9` fix leg.
- **L-3 · `CORE-SET.md` contradicts itself on how many members sit outside the product tier.**
  `:14` says "Two members sit outside the product tier"; `:56` says "Three do — the construction
  checklist and the two retired-contract stubs", and `806efca`'s body says three. Three is right.
- **L-4 · `ONBOARDING.md:117` attributes to `HD-1` something `HD-1` does not say.** The cell now
  reads "`HD-1` states what a journal is for and its one-file-per-round shape". `HD-1`'s ruling
  text carries the narrowing to 分析/推理/实测 and nothing about one file per round; `grep` over
  `HARNESS-DECISIONS.md` and its archive returns no statement of that shape. The shape's only
  surviving home is `CONSTRUCTION-INDEX.md`'s journals row, which a caller does not carry.
  `eba47ad`'s body justifies the re-point as "what the row itself cited for the same fact" — the
  row cited `HD-1` for the narrowing, beside the shape, not for it. Ruling 15's bound was "do not
  invent an owner"; this cell names one that holds half of what is attributed to it.
- **L-5 · `CONSTRUCTION-INDEX.md:7` says the file "restates none of them".** Its decision-log row
  restates `E10`'s `§live` obligation, the waiver clause and the verbatim-inheritance rule; its
  journals row restates the one-file-per-round shape. The governance risk is capped two
  paragraphs later ("where this file and that file disagree, that file governs"), so the defect
  is the header sentence, not the rows.
- **L-6 · `CONSTRUCTION-LEDGER.md`'s `CORE-SET` entry is stale about its own round.** `:147`
  still reads 裁决自八条增至十四条 plus a fifteenth; the plan carries seventeen. `:152` reads
  轮 1 `CORE-SET-LAYER` 已开（item A–E + I/J/K/L）— item M is missing. `c5f00f6` records the entry
  as untouched (correct, the 180-line bound) but not as stale, so a cold session reading the
  pointer before the plan gets the wrong item list.
- **L-7 · `c5f00f6` calls itself "sixth and last candidate commit"; it is the seventh.**
  `eba47ad` already claims "last of six", and the plan's step 4 lists seven landed candidates.
  The "of six" numbering predates ruling 16.
- **L-8 · `c0b9316` says of the nine moved rows "nothing else in those rows changed".** The
  decision-log row was rewritten substantively in that same commit by item A, which the same body
  discloses one paragraph earlier. The two sentences disagree; the work is not undisclosed.

---

## 5. Observations (`R5` — the question and the conclusion are the user's)

- **O-1 · the repository root is accumulating construction-side registers.** `git ls-files` over
  root `*.md` now returns seven of them — decision log and archive, rider bank, construction
  ledger and archive, and this round's two new files — beside two READMEs. Successive rounds
  closing findings by adding a component is the shape `R5` asks me to report and not to judge.
- **O-2 · the `E10` amendment in `c0b9316` has not had its independent read.** `E10` requires one
  before any round relies on the text; authoring is not reliance, so nothing is violated here.
  But no record states that the read is owed, and the next round's opening is where it falls due.
- **O-3 · the batch briefing is untracked and still cited.** `.goals/plans/core-set.plan.md`
  exists in the worktree and is invisible to any reviewer. The tracked plan cites it for
  acceptance 1's wording; the journal cites it for the end-to-end mechanical measurement that
  step 6 did not re-run. The plan discloses it as chat-only load-bearing material and a finding
  under `R2`, and journal §7 names the un-re-run leg as an honesty cap — the disclosure is the
  right shape, and it is repeated here so it sits on the review record too.

---

## 6. `UNVERIFIABLE` and coverage (`R4`)

- **Read in full:** `CONSTRUCTION-CHECKLIST.md` (standing instruction), `HARNESS-DECISIONS.md`
  `§live` and the header, `CORE-SET.md`, `CONSTRUCTION-INDEX.md`, the round journal, the round
  plan, the whole subject diff, the nine commit bodies, `sweep_refs.py`, `layer_path_check.py`,
  and `review_freeze_check.py`'s docstring and predicate.
- **Read at the cited lines:** `ONBOARDING.md`, `EXECUTION.md`, `REVIEW.md`, `ORCHESTRATION.md`,
  `templates/decision-log.md`, `CONSTRUCTION-LEDGER.md`, `HARNESS-DECISIONS-archive.md`,
  `HARNESS-RIDERS.md`.
- **Probed only:** the 854-test battery (run to completion, not read); `contract/…-v4.md`
  (blob-compared, not re-read — `E2`-frozen and untouched).
- **`UNVERIFIABLE`, stated rather than folded into supported:**
  - The `E11` preview card and its approval. Ruled not to be committed, so there is nothing in
    the repository to check (`R7`: state the ceiling and move on).
  - The three-session role form (`HD-55`): that the candidate was written by a cold executor
    session and the opening read by another is a process claim. Marked, not verified (`R4`).
  - `c5f00f6`'s "41 non-resolving references both before and after". I verified the **after**
    figure (41) directly, and verified by inspection of the diff that the five `LINK` entries
    became five backticked `NAMETOK`s at the same lines, which is what makes the total unchanged;
    I did not build the `eba47ad` stripped tree, because the sandbox refused that command twice.
    The claim is consistent with everything I could measure and is load-bearing for no acceptance.
- **This is a FULL, not a re-certification.** The controls in §2.5 prove `layer_path_check` has
  binding force on the class it names; they do not prove that force is sufficient. The guard is
  blind by construction to standing text, to bare-name tokens, and to every file outside the nine
  — which is how B-1 and B-2 both survived a round that ran it at every commit.
