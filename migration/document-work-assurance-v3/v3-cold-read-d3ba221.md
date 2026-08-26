# Cold read — the instruction layer at `d3ba221` (batch `CORE-SET`, round 2 opening)

**No verdict.** A read is not a round (`R3`): it spends no budget, carries no verdict, and its
output is findings tiered must-fix / low / observation. Nothing below certifies any text, and
nothing below is banked as any round's FULL.

**Findings: 0 must-fix, 1 low, 3 observations.** The low is a member sentence that is true today
and goes false when the round now opening lands, and that round's enumerated scope reaches it
through no item (`L-1`). The observations: one clause of `E10`'s guard-blind-spot list is
falsified by paired probe, in the safe direction (`O-1`); the layer's one non-resolving path
token is a ruled state and not decay, but nothing a cold round is *obliged* to read says so
(`O-2`); and `README.md`'s ordinal for `ORCHESTRATION.md` is stale against a membership that has
since moved (`O-3`).

**All nine members were read end to end** — 1,644 lines — so nothing here rests on `E10`'s
citation clause. The citable set was computed anyway (§2) and would have been four.

**The dispatch withheld what it should withhold.** The prompt is `dispatch.READ_PROMPT`
(`tooling/rsclib/document_harness/dispatch.py:671-684`) verbatim, with `{charter}` and `{commit}`
substituted and nothing appended — no member table. `v3-cold-read-ff4b749.md`'s `O-2`, which
recorded hand-scoping re-supplying the enumeration the generator deliberately withholds, does not
recur; the member set below was derived from `E10`'s own sentence.

**Standing instructions read.** `migration/document-work-assurance-v3/v3-harness-review-contract.md`
(the stub, member 7) → `document-harness/CONSTRUCTION-CHECKLIST.md` in full, both sides, per the
stub's *"It is your standing instruction and its own counterpart; read all of it."*
`HARNESS-DECISIONS.md` lines 1–205: the header (1–29) plus `§live` (30–205), which `E10`'s tail
owes at a round's opening. **`§live` now carries ten entries, not the eight the previous read
recorded** — `HD-60` and `HD-59` were added 2026-08-26, ahead of `HD-56`, `HD-44`, `HD-41`,
`HD-36`, `HD-35`, `HD-34`, `HD-23`, `HD-9`. `§implemented` and `HARNESS-DECISIONS-archive.md`
were **not** read end to end — probed by id only. Cited by section, never by blob.

---

## 1. What the subject is, and how it was derived

Everything below was re-derived from the repository (`R2`).

```
$ git rev-parse HEAD
d3ba22109413408a6deadec02ca6531f4dcad76c

$ git status --porcelain
?? .goals/

$ git log -1 --format='%H%n%ad%n%s' d3ba221
d3ba22109413408a6deadec02ca6531f4dcad76c
Wed Aug 26 21:01:56 2026 +1000
V3-CORE-SET-PLAN-POINTER-REFRESH-v1
```

HEAD is the subject commit. The one worktree entry is untracked and outside every member path,
so the tracked worktree bytes are the subject bytes — verified per member with `git hash-object`
against `git rev-parse d3ba221:<path>`, **9/9 MATCH** (§2), rather than inferred.

**The subject commit touches no member.**

```
$ git show --stat --format='' d3ba221
 document-harness/plans/core-set.plan.md | 15 +++++++++++----
 1 file changed, 11 insertions(+), 4 deletions(-)
```

Its body calls itself bookkeeping and says so: *"No instruction-layer member is touched."* It
refreshes the plan's resume pointer, which had said round 2 could not open until the `E2` ruling
was recorded — false since `HD-60` landed seven commits earlier, and false in the direction that
stops work. The refreshed pointer names the next action as *"open round 2 `CORE-SET-SIGNATURE`,
scope items F and N … cold read at full weight, then the `E11` card."* **This is that read.**

The plan `document-harness/plans/core-set.plan.md` is not a member. It was probed, not relied on
for any finding, except where `L-1` treats round 2's declared scope as an object — there the
plan's own text is the evidence and is quoted.

**The freeze window is intact, re-derived rather than assumed.** The gitignored marker
`.harness/review-pending.json` names subject `d3ba22109413408a6deadec02ca6531f4dcad76c`,
dispatched `2026-08-26T11:38:38+00:00`. The branch tip is the subject, so no commit has landed
since dispatch (`E9`).

## 2. The member set, each member's blob, and the coverage arithmetic

The set is `E10`'s own sentence — **"exactly these nine paths and nothing else"** — hand-
transcribed from the checklist at the subject blob, then machine-compared against the guard's
mirror. Both agree; the prose leg has no guard, which is banked as rider `E10-sync`.

```
$ git rev-parse d3ba221:<path>   /   git rev-parse ff4b749:<path>

 #  blob @ d3ba221                              lines  bytes  path                                            vs ff4b749
 1  3d049a1392c3bc73cd39fb328bd75501535a3560     255  20342  document-harness/CONSTRUCTION-CHECKLIST.md      CHANGED (was c0e3e2dd)
 2  c43b8e879cdff6b2760f24a1596921c00b919b21      30   9028  document-harness/README.md                      CHANGED (was 7e279835)
 3  234fdddf974e580d22a1a26b54587d11c24863b3     524  37011  document-harness/EXECUTION.md                   CHANGED (was 9c61051d)
 4  395995d45991670dc67e2eb616624c44b30ec123     320  20688  document-harness/REVIEW.md                      CHANGED (was 86e5ed7a)
 5  a9e9f75e484f40f4a1014e5d68ed6c73aa5fbdc2     119   8352  document-harness/ORCHESTRATION.md               CHANGED (was ae641325)
 6  6d5714923870b4e13e8928221a80df68e563a5ed       5    511  migration/…/v3-harness-operating-contract.md    same
 7  29bdc9fbde6e8db38d601dd2340d4b46a24a296f       5    924  migration/…/v3-harness-review-contract.md       same
 8  dfc983d2e3d9fb5ca67b053a16fcfb0e6715b11a     342  22185  contract/Document-Work-Assurance-Contract-v4.md same
 9  09aa869962f592c2f86c9379be0ef3eb7d2232ff      44   2812  schema/…/paragraph-map.schema.json              same
```

The membership mirror in the guard, compared rather than assumed:
`tooling/hooks/layer_path_check.py:37-47` `LAYER` — nine entries, identical to `E10`'s prose,
in the same order.

**Citable set, computed and then not used.** Five members changed since
`v3-cold-read-ff4b749.md`, so four would have been citable against it (members 6–9). All nine
were read end to end regardless; no finding below rests on a citation.

**Where the five changes came from.** `git log ff4b749..d3ba221 -- <the nine>` returns exactly
six commits out of the range's twenty-eight, all of round `CORE-SET-LAYER`:

- `0420d99` `…-L1-FREE-v1` — member 2, one line: the free-channel application of the previous
  read's `L-1` (the onboarding row's label list). **Checked**: the row now reads *"mount, the
  `.harness/` ignore entry, instance files, journal, ledger, policy file, pointer line, hook
  wiring"* — eight labels covering `ONBOARDING.md`'s nine items with *instance files* plural for
  items 3 and 4. That is the byte the record supplied, and it closes the class the previous read
  measured. No finding.
- `c0b9316` `…-A-D-v1` — members 1, 2, 5. `E10`'s `§live` clause gains the repository-of-the-round
  sentence and the waiver sentence; `ORCHESTRATION.md:51` drops the mount-reaching link; nine
  README rows move to `CONSTRUCTION-INDEX.md`.
- `c39536b` `…-B-C-v1` — member 2, one line.
- `4f4dc4b` `…-E-v1` — member 3: the C4 `O-1` sampling obligation is cut in two.
- `60d668f` `…-I-J-v1` — members 2, 3, and the deletion of `document-harness/history/`.
- `c5f00f6` `…-M-v1` — members 2, 3, 4: three product-facing citations demoted to name + holder.

## 3. The read

### 3.1 The `§live` amendment (member 1, `:151-158`) — checked against its two mirrors

The new clause says the decision log meant is *"the one in the repository the round runs in, at
that repository's root … never the instrument's copy of that name under the mount"*, and that the
obligation survives a waiver of the layer's cold read. Both halves were checked against the other
two places the same obligation is written, rather than against the amendment's claim:

- `HARNESS-DECISIONS.md:9-10` — 「指令层的 cold read 被豁免时 §live 照读——豁免的是那一层的成员，
  本文件不是成员，被豁免的开轮仍读 §live」;
- `CONSTRUCTION-INDEX.md:38` — *"every round's opening MUST read its `§live` (and only `§live`),
  waiver of the layer's cold read or not."*

Three sites, one rule, no divergence. Rider `waiver-live`, which recorded that neither carrier
said whether a waiver reached `§live`, is genuinely closed rather than reduced.

**The referent-scoped fix was scoped correctly, which a string-scoped fix would have got wrong.**
Class sweep over all nine members for `HARNESS-DECISIONS` returns five sites. Three are bare names
and compliant (`CONSTRUCTION-CHECKLIST.md:151`, `ORCHESTRATION.md:51`, contract v4 `:9`
frontmatter). Two are mount-reaching links in contract v4 (`:16`, `:341`) and one is a
mount-reaching token in `README.md:16`. The round changed `ORCHESTRATION.md` and left the other
three — correctly: `ORCHESTRATION.md:51`'s referent is *whichever* log the reader's round runs
under, so a `../` link would reach the wrong file for every caller, while contract v4's and
`README.md`'s referent is **this instrument's** log, where `HD-56` actually lives, so `../`
reaches the intended bytes. The distinction is by referent, not by string. `HD-60` schedules
contract v4's two; `README.md:16` is `L-1`.

### 3.2 The C4 `O-1` split (member 3, `:279-289`) — the claimed carrier exists

The rewritten clause moves the reading and the three-branch re-ruling off the product run and says
it *"is stated where this instrument keeps construction-side rulings"*. That is a factual
assertion in instruction text, so it was checked (`E3`): `CONSTRUCTION-LEDGER.md:134-137` carries
it, and says of itself 「读数与改判 2026-08-25 裁归构造轮，**本行是它唯一的家**」. `HD-58` names the
same two carriers. The product-side residue is one line per run, and a caller that never sees the
construction ledger loses nothing, because the clause tells it explicitly that a product run
*"neither performs that reading nor waits on it"*. No finding.

### 3.3 The layer's factual assertions about code, schemas and counts

Each of these is a claim written into instruction text that a command could falsify. Every one was
run; all hold.

| member claim | check | result |
|---|---|---|
| `E2`: contract v4 is blob `dfc983d2…` | `git rev-parse d3ba221:contract/…v4.md` | `dfc983d2e3d9fb5c…` ✓ |
| `E2`: the pack is **fifteen** files | `git ls-tree -r --name-only d3ba221 schema/document-assurance-v3/ \| wc -l` | `15` ✓ |
| README: `contract/` holds exactly one file | `git ls-tree -r --name-only d3ba221 contract/` | one path ✓ |
| README: `CONSTRUCTION-INDEX.md` has **nine rows** | row count excluding header | 9 ✓ |
| README: nine of `ORCHESTRATION.md`'s **twelve** obligations are law elsewhere | 9 cite-only + 3 own-text | 12 ✓ |
| `ORCHESTRATION.md`: **three** review-side and **two** executor-side dispatch modes | `dispatch.py` families | `dispatch_of` · `construction_dispatch_of` · `read_dispatch_of` / `executor_dispatch_of` · `construction_executor_dispatch_of` ✓ |
| stub 7: `dispatch.CONSTRUCTION_ROLE_INSTRUCTION` hard-codes its path | `dispatch.py:548` | ✓ |
| stub 7: `test_dispatch.py`'s hand-written `CHARTER_OUTSIDE` / `MEMBER` pin it (`E5`) | `test_dispatch.py:398,463,522` | ✓ literal strings, not the module's constant |
| `EXECUTION.md`: `README.md` pinned by `test_readme_enumeration.py` | file + grep | ✓ |
| `EXECUTION.md`: two shipped templates under `document-harness/templates/`, copied by `init_target.py` | `git ls-tree` + `TEMPLATES`/`_copy_templates` | 2 ✓ |
| `EXECUTION.md`: contract v4 pinned by `document_harness/__init__.py` | `CONTRACT_PATH`, `:41` | ✓ |
| contract §5: `checkKind` six values | `common.schema.json:115` | exact match ✓ |
| contract §5 + `EXECUTION.md` SIMP-A1: verification mode is two values | `common.schema.json:119` | `["local_check","review_only"]` ✓ both-modes gone |
| contract §5: WorkState status nine values | `common.schema.json:123` | exact match ✓ |

`HD-60`'s three named sites in contract v4 were confirmed present and distinct — `:9`
frontmatter, `:16-17` the *Signature semantics* block, `:340-341` the closing sentence — so the
authorisation is actionable as written.

**Read-discipline note (`REVIEW.md`, *Read discipline (Windows)*).** The first attempt to load the
schemas decoded through the console locale and died with `UnicodeDecodeError: 'gbk' codec`. Re-run
under explicit UTF-8. Recorded because the rule earned itself on this read.

### 3.4 Mechanical scan of standing text — the stock the guard never re-scans

`layer_path_check` reads only the lines a staged diff adds (`added_lines_by_path`, verified by
reading it: `git diff --cached -M -U0`, `+` lines only), so all standing text was scanned here
instead, by applying the guard's own `unresolved_tokens` to each member's full bytes, and by
resolving every relative markdown-link target independently.

```
$ python tooling/sweep_refs.py
… 15 lines …
-- 15 caller-held or unresolvable references over 9 members
```

Thirteen are `NAMETOK` bare filenames — the compliant form for a caller-held artifact — and one
site accounts for the remaining two entries: `document-harness/REVIEW.md:93`, reported once as
`LINK` and once as `PATHTOK` (13 + 2 = 15, counted by command, not by eye). That is the layer's **only** non-resolving path token, and it is
`O-2`. The count reproduces what `60d668f`'s body recorded (13 → 15).

## 4. Findings

### `L-1` (low) — `README.md:16` is true today and goes false when round 2 lands, and round 2's scope reaches it through no item

**Location.** `document-harness/README.md:16`, the Contract v4 row:

```
its signature state is `HD-56` in `../HARNESS-DECISIONS.md`, never this row
```

**Ground truth.** Round `CORE-SET-SIGNATURE` — the round this read opens — moves the v4 signature
out of the decision log. `document-harness/plans/core-set.plan.md` item F: *"New file beside the
contract … `HD-56` goes to `superseded` with a successor carrying the signature in full, both
directions of the pointer, in the same commit as the new carrier."* `HD-60` authorises the write
and its obligation ③ requires the new carrier file and `HD-56`'s supersession pointers in one
commit. After that commit both halves of the sentence above are wrong: `HD-56` is no longer the
live entry, and the signature state no longer lives in `../HARNESS-DECISIONS.md`.

**Why it is not covered.** Round 2's scope is items **F and N** (plan `:110`, `:560`). Item F's
site list is contract v4 only — the frontmatter `signature_owner:` field, the signature-semantics
block, and, carried in from item J, contract v4 `:32`. `HD-60` is narrower still: 「站点三处」, all
three in contract v4. Item N merges `CORE-SET.md` into `CONSTRUCTION-INDEX.md` and touches no
member. **`document-harness/README.md` appears in neither item's site list, and in no `HD-60`
site.**

**Class sweep, per `HD-41` ④ / `E7`** — the finding must not repeat the defect it reports. Scanning
all nine members for assertions about where the v4 signature lives returns five sites:

```
$ git grep -nE 'HD-56|signature (state|record|owner)|signature_owner' -- <the nine>
contract/…v4.md:9      signature_owner: HARNESS-DECISIONS.md            → item F site list ✓
contract/…v4.md:16     the Signature semantics block                    → item F / HD-60 site 2 ✓
contract/…v4.md:340    "lives as an `HD` entry in …"                    → item F / HD-60 site 3 ✓
CONSTRUCTION-CHECKLIST.md:56  "the signed blob remains the signature object `HD-56` binds"
                                                                        → reached incidentally ✓
document-harness/README.md:16  "its signature state is `HD-56` in …"    → reached by nothing ✗
```

`CONSTRUCTION-CHECKLIST.md:56` is reached even though no item names it, because `HD-60`'s
obligation ① forces round 2 to update `E2`'s v4 blob literal two lines above it (`:54`), so the
executor is editing that clause with `:56` in view. That is luck of adjacency, not scope, but it
holds. `README.md:16` has no such adjacency: nothing else in that file is in round 2's path.

**How it came to be deferred here.** `c0b9316`'s body discloses it and names its home:
*"That one is line 16 … it is left standing deliberately — the sentence it sits in is what round
CORE-SET-SIGNATURE rewrites when the signature moves out of the decision log, and item A's site
list does not name it. It is the round's disclosed residual in this member."* The disclosure is
exemplary; the assignment is to a round whose item list does not in fact reach the file. A
residual disclosed to a round is only as good as that round's scope, and this is the gap between
the two.

**The downstream decision that goes wrong (`R9`).** Round 2's executor works items F and N, lands
the new carrier and flips `HD-56`, and the layer's own navigation surface then tells its next
reader that the signature of the `E2`-frozen contract lives in a file where it does not, under an
entry that is superseded. `document-harness/README.md` is the member `test_readme_enumeration.py`
exists to guard *because* — in that test's words — *"the instruction layer's navigation surface …
decayed silently"*; this is that class, one round ahead of itself.

**Why this is low and not must-fix.** At the subject the sentence is **true**: `HD-56` is `live`
and does hold the signature. Nothing acts wrongly on it today. It becomes false only when round 2
writes, which is why it is reported now rather than after.

**Why the bank cannot take it (`R10`).** Its deadline is the moment round 2's signature commit
lands. `R10` requires a rider's deadline to fall outside the round that writes the row, and
「a deadline arriving on its own round is malformed」; a row written at round 2's opening would
carry a deadline inside round 2. So the two honest routes are: add the site to round 2's scope, or
defer it explicitly to a later round and give it a deadline that round can outlive.

**No bytes supplied, deliberately.** The replacement sentence has to name the new carrier, and that
file does not exist yet — item N records that even its name is 「the round's to pick」. Writing a
name for it now would put a path token in a member that resolves nowhere, which is the defect
`E10` names two clauses later. **Routing is the orchestrator's and the user's, not this reader's
(`R5`)**: this finding names the site, the moment and the gap, and stops there.

### `O-1` (observation) — `E10`'s guard-blind-spot list: the markdown-link clause is falsified by measurement

**Location.** `document-harness/CONSTRUCTION-CHECKLIST.md:173-174` — *"a token carrying a
placeholder segment falls outside its path shape, **prose and markdown links carry no backtick
token for it to find**, …"*

**Measured, with both controls, against the guard's own `unresolved_tokens`:**

```
A bare markdown link, bad target          -> silent
B backticked-label link, bad target       -> FLAGGED  history/NO-SUCH-FILE.md
C the actual standing line at REVIEW.md:93 -> FLAGGED  history/REVIEW-v1-package-flow.md
D positive control, plain bad token       -> FLAGGED  document-harness/NO-SUCH-FILE.md
E negative control, good token            -> silent
```

The clause is right about the bare form (A) and wrong about the backticked-label form (B) —
`` [`a/b.md`](a/b.md) `` — which is the style this layer overwhelmingly uses, and in which the
label *is* a backtick token containing a slash. `sweep_refs.py` demonstrates it independently: it
imports the guard's own `TOKEN` and `PATHLIKE` and reports `REVIEW.md:93` as a `PATHTOK`, which is
precisely that label being seen.

**Consequence, and its direction.** The error understates the guard's reach, so a reader relying on
the clause over-checks rather than under-checks — safe. What it does cost is the diagnosis of the
one site it matters at: a reader asking why `REVIEW.md:93` survives would take this clause's answer
(*markdown links are invisible*) and be wrong. The real reason is the clause's **last** item — the
standing text the guard never re-scans — which was verified correct by reading
`added_lines_by_path`. Two clauses in one sentence, one false, one true, and the false one is the
one that looks like it applies.

**Not re-filed as a new row.** Rider `e10-cannot-see` already banks two falsifications of this same
sentence (the path-shape list is short; the *"class entire"* quantifier was disproved) and its
redeem-when is 「下一个碰 `E10` 该条款或 `layer_path_check` `PATHLIKE` 的有资格开轮的批」 — the same
surface. This is a third instance of a banked class and belongs as a note on that row, not beside
it. Whether to annotate is the orchestrator's call.

**Stated as unverified (`R4`).** The third item in the same list — an added line whose content opens
`` ++ `` confusing the diff parser — was **not** established either way. It lives in
`added_lines_by_path`'s diff parsing, not in token matching, so the probe above reaches the wrong
function; testing it needs a real staged diff. `layer_path_check.py`'s own docstring documents it
with a FULL citation, and that citation was not re-verified here.

### `O-2` (observation) — the layer's one dangling path token is ruled, not decayed; nothing a round is obliged to read says so

`document-harness/REVIEW.md:93` carries
`` [`history/REVIEW-v1-package-flow.md`](history/REVIEW-v1-package-flow.md) ``, and the target does
not exist. Derived rather than assumed: `39a21a8` (round `DE-PREFIX`) created both the file and
the pointer; `60d668f` (item I) deleted the file and left the pointer, under user ruling 13. The
plan's item G assigns retiring the pointer to **round 3** `CORE-SET-CODE`, with the CLI option and
the review module's package half it belongs to. So it is authorised, recorded in three places, and
scheduled. **It is not a defect at this commit, and it is not `L-1`'s shape** — `L-1` is a sentence
with no scheduled home, this one has one.

Recorded for a different reason. A round's *owed* opening reading is the nine members plus
`§live`. Neither reveals that this token is ruled: the authorisation lives in a plan, a commit body
and prior read records, none of them owed. A cold round that reads only what it must, finds a
member path token resolving nowhere, and applies `E10`'s own resolution clause has grounds to file
a must-fix and spend an amendment-plus-re-read pair on something already settled. That exposure is
bounded in practice — round 2 is the only opening between the deletion and item G, and this record
is that opening's read — so it is an observation, not a finding, and it asks for nothing.

### `O-3` (observation) — `README.md:22` still calls `ORCHESTRATION.md` the tenth member

The row reads *"added as the tenth member 2026-08-18"*. That is accurate as history — `HD-46`
established the charter as the tenth — but membership went 10 → 8 → 9 at round `CONTRACT-V4` when
the three signed sources merged, and this phrase was not revisited. A reader meets *"the tenth
member"* in the layer's navigation surface while `E10`, two files away, says *"exactly these nine
paths and nothing else"*.

**No downstream decision goes wrong (`R9`).** `E10`'s sentence is the sole authority on membership,
`READ_PROMPT` sends every reader to it by name, and the phrase carries its own date. So this rides
the next batch touching this member and spawns no round and no read. Reported because
`README.md` is the member whose silent decay bought its own pinning test, and an ordinal that has
outlived its arithmetic is that class.

## 5. Coverage — what was read in full, sampled, and only probed (`R4`)

**Read in full, end to end** — all nine members, 1,644 lines:

| blob | lines | path |
|---|---|---|
| `3d049a1392c3bc73cd39fb328bd75501535a3560` | 255 | `document-harness/CONSTRUCTION-CHECKLIST.md` (both sides, as standing instruction) |
| `c43b8e879cdff6b2760f24a1596921c00b919b21` | 30 | `document-harness/README.md` |
| `234fdddf974e580d22a1a26b54587d11c24863b3` | 524 | `document-harness/EXECUTION.md` |
| `395995d45991670dc67e2eb616624c44b30ec123` | 320 | `document-harness/REVIEW.md` |
| `a9e9f75e484f40f4a1014e5d68ed6c73aa5fbdc2` | 119 | `document-harness/ORCHESTRATION.md` |
| `6d5714923870b4e13e8928221a80df68e563a5ed` | 5 | `migration/…/v3-harness-operating-contract.md` |
| `29bdc9fbde6e8db38d601dd2340d4b46a24a296f` | 5 | `migration/…/v3-harness-review-contract.md` |
| `dfc983d2e3d9fb5ca67b053a16fcfb0e6715b11a` | 342 | `contract/Document-Work-Assurance-Contract-v4.md` |
| `09aa869962f592c2f86c9379be0ef3eb7d2232ff` | 44 | `schema/document-assurance-v3/paragraph-map.schema.json` |

Also read end to end: `HARNESS-DECISIONS.md` lines 1–205 (header plus `§live`, ten entries);
`HARNESS-RIDERS.md` in full, all 19 rows; `CORE-SET.md` in full (82 lines);
`v3-cold-read-ff4b749.md` in full; the commit bodies of `d3ba221`, `60d668f` and `c0b9316` in
full; the aggregate member diff `ff4b749..d3ba221` in full.

**Sampled:** `CONSTRUCTION-INDEX.md` — the nine table rows and the header, not the whole file.
`CONSTRUCTION-LEDGER.md` — `:128-146` (the conversation-only list) read closely; `:81`, `:91`,
`:134` located; not read end to end. `document-harness/plans/core-set.plan.md` — items F, G, I, J
and N, the scope lines `:110` / `:560`, and the resume-pointer diff; the rest not read.
`tooling/hooks/layer_path_check.py` — read in full (`:1-110` plus `added_lines_by_path`).

**Probed only, for named claims, never read end to end:**
`tooling/rsclib/document_harness/dispatch.py` (`:548`, `:659-729`, the family list),
`tooling/sweep_refs.py` (docstring and invocation),
`tooling/rsclib/document_harness/init_target.py` (`TEMPLATES`, `_copy_templates`),
`tooling/rsclib/document_harness/__init__.py` (`:41`),
`tooling/tests/document_harness_review/test_dispatch.py` (the constant lines),
`tooling/tests/document_harness/test_readme_enumeration.py` (docstring and the pinned path),
`schema/document-assurance-v3/common.schema.json` (`:114-124`),
`local-check-spec.schema.json` and `document-work-spec.v2.schema.json` (the `$ref`s only).
`§implemented` and `HARNESS-DECISIONS-archive.md` were probed by id only.

**Marked, not verified (`R4`).** That this session ran with fresh context and as its own session is
a process claim this reader cannot verify from inside. The round's declared form is `HD-55` /
independent sessions; rider `e1-reader` already records that `E1`'s form clause names *reviewer or
executor* and omits the reader, which is the role this dispatch filled. Not re-filed.

**Not done, and why.** **No guard was mutation-tested in `E4`'s sense** — neuter → red → restore
from sha256-checked scratchpad copies. What §3.4 and `O-1` report are paired probes against
`unresolved_tokens` with a positive and a negative control: they establish how that function
behaves on synthetic input, not that any committed test binds it. The subject commit changes no
code and adds no guard, so there is no new binding force to prove. The full battery was not run:
`E9`'s window is open and this read lands one record.
