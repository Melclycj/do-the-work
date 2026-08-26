# FULL review — `8e576a1..a554c0b` (round `CORE-SET-SIGNATURE`, batch `CORE-SET`, round 2)

Independent FULL. Subject received as one range and nothing else (`R2`); round identity, budget,
authorization, obligations and every figure below are re-derived from the repository. Standing
instructions: `migration/document-work-assurance-v3/v3-harness-review-contract.md`, a stub
superseding to `document-harness/CONSTRUCTION-CHECKLIST.md` — read whole at the subject tip (257
lines, both sides), and it is its own counterpart. `HARNESS-DECISIONS.md` `§live` read whole at
the tip plus the header's mechanism block: eight entries — `HD-59` `HD-44` `HD-41` `HD-36`
`HD-35` `HD-34` `HD-23` `HD-9`. (`§live` carried ten at the round's opening read; `HD-56`,
`HD-60` and `HD-61` left it inside this subject, and `HD-59` is new since round 1.)

**Verdict: `REVIEWED_NO_BLOCKER`.** 4 lows, 3 observations. No blocker. Every measurement the
round claims was reproduced independently and every one of the round's own headline figures is
exact; the four lows are all in the record layer, not the implementation.

---

## 1. Subject and round, re-derived

```
$ git rev-parse HEAD                          -> a554c0bc39b1dbb964df4ff28215e41798534d3c
$ git status --porcelain                      -> ?? .goals/     (untracked only)
$ git rev-list --count 8e576a1..a554c0b       -> 4
$ git rev-list --count origin/main..HEAD      -> 45             (nothing pushed, E8)
```

Four commits, classified by hand from their own trees rather than from their titles:

| commit | scope | kind, by `E9`'s test rather than by name |
|---|---|---|
| `07ef526` | item F | candidate |
| `cb4f22f` | item N | candidate |
| `66dfd30` | round journal | round record (doc-only, one added file) |
| `a554c0b` | `HD-60`/`HD-61` → `retired`; plan correction | ruling (orchestrator/user bookkeeping) |

**`E9` going in, derived.** The round's only prior review-side event is the opening cold read at
`fc9c008`, recorded in `v3-cold-read-d3ba221.md` — a read, so no verdict and no budget (`R3`).
No `v3-review-{full,verify}-*` record exists for any SHA in this range. **This is the round's one
FULL; the fix leg is unspent; a targeted VERIFY falls due only if a fix is approved.** Both work
commits self-classify as candidates consuming no leg, and by `E9`'s own question — has a valid
independent FULL already occurred? — that is correct, not a renamed round.

**Change boundary, paths classified by hand (11 paths):**

- **Instruction-layer members (3 of 9):** `contract/Document-Work-Assurance-Contract-v4.md` ·
  `document-harness/CONSTRUCTION-CHECKLIST.md` · `document-harness/README.md`. See `L-1`.
- **`E2` frozen bytes: written, and under ruling.** Contract v4 moved
  `dfc983d2…` → `5dfb7b64…` (`git rev-parse {8e576a1,07ef526}:contract/…-v4.md`).
  `git diff --name-status 8e576a1..a554c0b -- schema/document-assurance-v3/` → 0 lines; the
  pack stands at 15 files, `E2`'s re-baselined count.
- **No code, no tests, no schemas:**
  `git diff --name-status 8e576a1..a554c0b -- tooling/ assurance/ .githooks/ .github/` → 0 lines.
- **One deletion:** `CORE-SET.md`, merged into `CONSTRUCTION-INDEX.md` under ruling 22.
- **One addition outside the registers:** `CONTRACT-V4-SIGNATURE.md` at the root.
- Registers (`HARNESS-DECISIONS.md`, its archive, `HARNESS-RIDERS.md`), the plan and the journal
  complete the list. `CONSTRUCTION-LEDGER.md` untouched (last written `a19c9b4`, before the base).

**Authorization, from committed state only.** `document-harness/plans/core-set.plan.md` carries
twenty-two user rulings and is named by `CONSTRUCTION-LEDGER.md` as the batch's carrier. The two
`E2` write authorizations are `HD-60` (signature re-siting, three sites) and `HD-61` (five
citation demotions), both `one-shot`, both now `retired` and archived by `a554c0b`. The `E11`
card is not on disk — construction-round cards are ruled not to be committed — so its approval is
a process claim, marked and not verified (`R4`).

---

## 2. Implementation — every claim reproduced

`R3` puts the implementation first. Each figure below is my own run at the stated commit, not the
round's number read back.

### 2.1 The headline measurement: 13 → 5, exact

Strip recipe rebuilt from the journal's §1 description, not copied from a script: `git archive`
into a scratch tree; delete `document-harness/journal/`, `document-harness/plans/`, all of
`migration/` except the two retired-contract stubs, the root registers, `CORE-SET.md` and
`CONTRACT-V4-SIGNATURE.md`; `git init && add -A && commit`; run the committed
`tooling/sweep_refs.py`.

| stripped tree | files | `LINK`+`PATHTOK` | `NAMETOK` | total |
|---|---|---|---|---|
| `8e576a1` base | 123 | **13** | 28 | 41 |
| `a554c0b` tip | 123 | **5** | 35 | 40 |

**13 → 5 confirmed to the site.** The eight closed are exactly the eight round 1 routed here —
contract v4 `:16` `:25` `:27` `:30` `:32` `:253` `:341` and `document-harness/README.md:16`. The
five remaining are exactly the journal's table: `CONSTRUCTION-CHECKLIST.md:6` and both stubs at
`:3` (allowed, ruling 12), and two entries at the single `REVIEW.md:93` site (dangling, ruling
13). The `NAMETOK` column is `O-1`.

The journal's §3 correction is **right and the plan's original acceptance sentence was wrong**: my
base run shows `PATHTOK document-harness/README.md:16 ../HARNESS-DECISIONS.md`, so that line was
a sweep hit as well as a truth claim, and the arithmetic is 13 → 5, not 13 → 6.

On the unstripped tip the sweep returns 15 with two real breaks (`REVIEW.md:93` twice) — the
commit bodies' figure, unchanged, as expected.

### 2.2 The signature chain

- `git rev-parse HEAD:contract/…-v4.md` → `5dfb7b64265c821c715f23de52824beeadea3405`; `E2`'s
  literal in `CONSTRUCTION-CHECKLIST.md:54` reads `5dfb7b64…`, **written in the same commit**
  (`07ef526` touches both). `HD-60` obligation ① discharged. **Acceptance 3 met.**
- `git cat-file blob 614932de… | wc -l` → **339**; `| sha256sum` →
  `1b1061cbdeb6585ee5b33f3dcf91c2ee376f60f3e92076998d7930b70f7a23fa`. Both match
  `CONTRACT-V4-SIGNATURE.md` exactly. The signed object is unchanged by the move (ruling 10).
- `07ef526`'s file list is the whole test of `HD-30`/`HD-2`: `CONTRACT-V4-SIGNATURE.md` (created),
  `HARNESS-DECISIONS-archive.md` (`HD-56` moved in, `superseded`, forward pointer),
  `HARNESS-DECISIONS.md` (`HD-56` removed from `§live`) — **one commit**. Back pointer present in
  the new file (§*Why this file exists*). `HD-56` is absent from `§live` at the tip.
  **Acceptance 2 met.**
- The successor is the carrier file, not a new `HD` entry. The journal's §4 reasoning holds: an
  entry carrying the signature in full would leave a second copy in the register ruling 5 empties.
- Every claim inside the new carrier is checkable and checks out: `v3-review-full-5f849da.md` and
  `v3-review-verify-d0f185c.md` exist; the three merged-source blobs `b2dbdf75…` `68031fa2…`
  `e1a2f26b…` all resolve (`git cat-file -t` → `blob`).
- `document-harness/README.md:16` names the new carrier and no superseded entry, and the **whole**
  README diff over the range is that one line — so row 17 (`contract/` holds exactly one file,
  verified: `git ls-tree -r --name-only HEAD contract/` → 1 path) and row 24 are untouched, as
  ruling 22's cost argument required. **Acceptances 4 and 5's last clause met.**

### 2.3 The frozen write, hunk by hunk

`git diff --word-diff` over contract v4 gives exactly eight changed sites and nothing else:

- **`HD-60`'s three**, matching its enumeration word for word: frontmatter `signature_owner:`;
  the *Signature semantics* sentence pointing at the decision log; §14's "lives as an `HD` entry".
- **`HD-61`'s five**: `:25` `:27` `:30` `:253` (N0 record ×2, W2 record, supersession-2 record)
  and `:32` (`contract-v4.plan.md`).

**Every one of the eight carries a holder sentence**, checked by hand — including
`contract-v4.plan.md`, which is covered by "like the plan named below" in the sentence above it.
No interface, enum (§5), invariant (§7), version boundary (§13) or dependency-map (§12) byte
moved; the diff does not touch those sections at all. One substitution inside an authorized site
is unaccounted for — `L-2`, and it is *not* an `E2` breach.

### 2.4 Item N

- `CORE-SET.md` gone; `CONSTRUCTION-INDEX.md` carries both tiers plus the index rows.
- Own prose, my count with table rows and the fenced block excluded: **1,605 characters excluding
  headings / 1,803 including** (round claims 1,609 / 1,804 — a 4-character delta from blank-line
  handling, immaterial). Item N's "well under 2,000" met, and stated as a measurement.
- `HD-21`'s question and answer survive (`CONSTRUCTION-INDEX.md:9-12`), as mandated.
- Product tier re-measured per row: 1+15+4+1+2+2+22+4+8 = **59**. ✓
- The bounded-sufficiency gap re-measured at the tip: **6** pointers into the checklist from the
  five product-tier role documents (`README.md:23` · `EXECUTION.md:13` · `REVIEW.md:8` ·
  `ORCHESTRATION.md:7` and `:39` · `ONBOARDING.md:109`) and **35** backticked `E1`–`E12` /
  `R1`–`R10` citations over **26** lines. Exact. ✓
- Three rider rows re-point (`checklist-cited-not-carried` · `figure-units` ·
  `onboarding-carries-construction`); every 量程 and redeem-when anchor now names
  `CONSTRUCTION-INDEX.md` or "核心集清单", and the three surviving `CORE-SET.md` strings are
  inside 触碰记录 narrating the merge — correct, those are history, not pointers. The stale
  `onboarding-io-design-owners` cross-reference is corrected. Bank: **19 rows at base and tip**,
  unchanged, as claimed.
- One figure went stale — `L-4`.

### 2.5 Guards and battery

```
$ python tooling/hooks/layer_path_check.py       -> exit 0
$ python tooling/hooks/candidate_path_check.py   -> exit 0
$ python tooling/hooks/review_freeze_check.py    -> exit 0
$ python -m pytest -q          (from tooling/)   -> 854 passed in 151.01s   exit 0
$ E10 members resolve                            -> 9/9
```

**Acceptances 6 and 7 met.** My 854 matches the round's test count on both work commits.

**Mutation-tested, in a scratch clone so the subject tree was never touched (`R8`):**

| mutation | `layer_path_check` |
|---|---|
| add to a member a backticked token naming a nonexistent file under the `document-harness` directory | **exit 1**, names the token |
| add `` `NO-SUCH-SIGNATURE-FILE.md` `` to contract v4 | exit 0 — **blind** |
| unmutated (negative control) | exit 0 |

(The first mutation's token is described rather than quoted: quoting it draws a
`candidate_path_check` block, the record-quotes-the-broken-path-it-reports class rider
`freeze-audit` banks. Met and worked around, not argued with — the same thing this round's
journal reports at its §3, which is how I knew to expect it.)

The guard binds for the shape it claims and is blind to the bare-name shape, exactly as
`layer_path_check.py:63` says and as the plan's *Constraints* records. The sweep sees the second
as advisory `NAMETOK` and blocks nothing. This is `O-1`.

---

## 3. Findings

### `L-1` — contract v4 is omitted from the members owing the layer's next independent read

**Location.** `07ef526` commit body: *"Two members are edited here and both edits ride `E10`'s
deferral channel"*; round journal §9: *"Two member edits are relied on before their independent
read."*

**Ground truth.** Three `E10` members were edited in `07ef526`: `CONSTRUCTION-CHECKLIST.md`,
`document-harness/README.md`, and `contract/Document-Work-Assurance-Contract-v4.md` — a member by
the user's 2026-08-23 ruling, named in `E10`'s own membership sentence. `E10` requires each
amendment to pass an independent read, and its citation clause covers a member only while its
blob is *unchanged* since a recorded end-to-end read. Contract v4's blob moved
`dfc983d2…` → `5dfb7b64…`, so no prior read of it is citable. The round's records never say the
contract's bytes ride the next read of this layer; they say two members do.

The charitable reading — that "two" counts only the members taking `E10`'s *deferral* channel,
the contract having taken `E2`'s ruling channel — still leaves the substantive gap: the deferral
sentence's conclusion ("the bytes ride the next read of this layer") is attached to two members
and never to the contract.

**Why it matters, and why it is not new.** `HD-57`, the last time v4 was written under a recorded
`E2` ruling, named it explicitly: *"v4 与 checklist 的成员编辑欠独立 read，随下一轮开轮冷读"*. And
`CONSTRUCTION-LEDGER.md` records round 1's opening read failing on precisely this class —
*"下轮冷读若再走窄形态，基线须按 `E10` 取「自某一份已记录整读以来未变」…（本轮开轮读的 `O-1` 即栽在这里）"*.

**Downstream decision.** Round 3 `CORE-SET-CODE`'s opening cold read, sizing itself from these
records, could cite a prior read for contract v4 that the blob change has invalidated. The
mechanical blob-comparison test recovers it, so harm needs a second mistake — which is why this
is a low and not a blocker.

**Minimum fix.** One sentence in the closeout record naming contract v4 as a third edited member
whose bytes ride the next read of this layer. Corrected forward per `HD-59`; the commit bodies
stand. **Deadline: round 3's opening.**

### `L-2` — `append-only` → `write-once` is a semantic substitution no record accounts for

**Location.** `contract/Document-Work-Assurance-Contract-v4.md`, *Signature semantics* block.

Base: *"The signature is recorded **append-only** as an `HD` entry in [`HARNESS-DECISIONS.md`]…"*
Tip: *"The signature is recorded, **write-once and after review**, in `CONTRACT-V4-SIGNATURE.md`…"*

**Not an `E2` breach, and I checked before writing this.** `HD-60` names this exact sentence as
one of its three sites, and its exclusion clause enumerates the contract's interfaces (§3), enums
(§5), invariants (§7), version boundaries (§13) and dependency map (§12) — the *Signature
semantics* block and §14 are in none of them. The rewrite was authorized.

**What is wrong is that the substitution is unrecorded.** A pure re-siting was available —
"recorded append-only in `CONTRACT-V4-SIGNATURE.md`" — and was not taken; a different durability
property was substituted instead, and `git grep -i 'append-only\|write-once'` over the round's
commit bodies, journal, plan and the new carrier returns nothing. Every other changed byte in the
frozen file is accounted for in `07ef526`'s body site by site; this one is not. §14's parallel
edit ("appended after review" → "written after review") is carrier-neutral and fine.

**Downstream decision.** At the next re-signature of contract v4 — a real event in this family:
`HD-35` re-signed `io-design.md` three times and `HD-40` re-signed `split-design.md` three times,
each recorded by **appending** a re-signature block to the existing carrier — the executor reads
"write-once" and has no sanctioned form for appending. The available reading is a sixth carrier
file, which is the add-a-component shape this batch's own ruling 18 was taken to stop.
"append-only" is also the term every prior carrier in this family uses for its signature log
(`N0-record.md:7`, `N1-record.md:7`, `N2-record.md:9` and `:635`).

**Minimum fix.** Restore `append-only`, or record that the property was deliberately changed and
what now governs correction of the signature record.

**Routing, stated because `R10` overrides the channel here.** The bytes sit on a path `E2`
freezes, so this **banks until an `E2` recorded ruling exists** (`HD-20`), however appliable it
is — and both authorizations that could have carried it are now `retired`. **Deadline: the next
`E2` write window on contract v4, or the next re-signature, whichever arrives first.** Both are
outside this round.

### `L-3` — the archive header's own line count is short by exactly the block that states it

**Location.** `HARNESS-DECISIONS-archive.md:7`, written by `a554c0b`: *"`HD-6` 的询问第六次已付…
移入后本档 **404** 行"*.

```
$ git show a554c0b:HARNESS-DECISIONS-archive.md | wc -l   -> 411
```

The added header block is 7 lines; 404 + 7 = 411. The figure was measured before the last change
to what it measures — `E3`'s exact shape, self-referentially.

**No decision changes:** `HD-6`'s threshold is 100 lines and both figures are far past it, so the
trigger fires and the "do not clear" answer is unaffected. Worth recording because the contrast
is inside the same header — the fifth ask's figure, written by the cold executor one commit
earlier at `07ef526`, is **345 and exact**. **Wording-level under `R9`; no deadline.**

### `L-4` — `CONSTRUCTION-INDEX.md`'s repository count went stale inside the round

**Location.** `CONSTRUCTION-INDEX.md:22` — *"59 files against a repository of **391**"*.

```
$ git ls-tree -r --name-only cb4f22f | wc -l   -> 391     (item N's own tree — correct when written)
$ git ls-tree -r --name-only a554c0b | wc -l   -> 392
```

Invalidated by the round's own journal commit `66dfd30` two commits later, which added a file.
`E3`: a figure is invalidated by any later change to what it measures. The 59 is still exact.
The file's own *"re-run them rather than citing these"* plus the printed commands are the
mitigation. **Wording-level under `R9` — no downstream decision turns on 391 vs 392; rides the
next batch touching this file. No deadline.**

---

## 4. Observations (`R5` — the conclusion is the user's, not mine)

### `O-1` — the round converts eight guarded references into eight unguarded ones

Real breaks fall 13 → 5, which is what the round claims and what I reproduced. The fuller picture
from the same two runs: `NAMETOK` rises 28 → 35, and the **total** references a caller cannot
follow moves 41 → 40.

This is not a criticism of the arithmetic — the journal's §1 states the counting rule plainly
(*"count only `LINK` and `PATHTOK`"*), and name-plus-holder is the form `E10` prescribes and
`sweep_refs.py`'s own docstring calls compliant. **The improvement is real**: a bare name with a
holder sentence tells a caller honestly that it does not have the artifact, where a `../` path
would have resolved through a mount into another repository's bytes.

What follows from it is worth the user's attention rather than mine: after this round, all eight
sites are held by **no machine at all**. My mutation test above shows `layer_path_check` is blind
to the bare-name shape by construction, and the sweep that does see it always exits 0. I checked
all eight by hand — every one names a file that exists and carries its holder sentence — but that
is a human read, and the next one is owed at round 3's opening. Whether the round's headline
should state both readings of the count is the user's call.

### `O-2` — nothing mechanical guards `E2`'s frozen-byte literal

`grep -rn '5dfb7b64\|dfc983d2\|614932de' tooling/` returns nothing: no test pins the blob literal
that `E2` names. `HD-60` obligation ① — update the literal in the same commit as the write — is
pure discipline, and this round discharged it correctly. The exposure is that the *next* contract
write has the same shape with no backstop. Stated, not prescribed: `E6` says a fix that needs new
machinery is the signal to re-question the guarded thing, and rider `freeze-audit` already sits on
this surface.

### `O-3` — the plan's resume pointer is stale at the tip, and `E9` is why it could not be fixed later

`document-harness/plans/core-set.plan.md` step 9 is still `[ ]` and the *Resume pointer* reads
*"The next action is to dispatch a cold executor … with items F and N"* — which happened, at
`07ef526` and `cb4f22f`. `CONSTRUCTION-LEDGER.md:177` says the same thing independently. Both
carriers now point a cold session at a dispatch that has occurred, whose `E2` authorizations are
`retired`.

**This is not negligence and I am not filing it as a finding.** `E9` forbids the branch taking any
commit but the record between dispatch and its landing, so the orchestrator cannot fix it while
this FULL is out. The one window where it was free — `a554c0b`, already editing this file — was
missed. Flagged so it rides the closeout, where step 9, the pointer and the ledger row all update
together.

---

## 5. Coverage (`R4`)

**Read in full:** `CONSTRUCTION-CHECKLIST.md` (257 lines, both sides) · `core-set.plan.md` (703) ·
the round journal (146) · `CONTRACT-V4-SIGNATURE.md` (60) · `CONSTRUCTION-INDEX.md` (64) ·
`sweep_refs.py` (92) · `layer_path_check.py` (135) · all four commit bodies · the complete diff of
the range, and contract v4's diff additionally at word level · `HARNESS-DECISIONS.md` header and
`§live` · the `HD-56`, `HD-60` and `HD-61` archive entries and the archive header.

**Sampled:** `HARNESS-DECISIONS.md` `§implemented` (lines 163–488 of 641; the remainder unread) ·
`HARNESS-RIDERS.md` (the three re-pointed rows in full via diff; the other sixteen only as row
names) · `CONSTRUCTION-LEDGER.md` (header and the `CORE-SET` / dispatch-economy entries).

**Probed only:** contract v4's standing text outside the diff (section headings and an
`invariant` grep, to place `L-2` against `HD-60`'s exclusion) · `review_freeze_check.py` and
`candidate_path_check.py` (docstrings; run, not read) · the test suite (run, not read) ·
`EXECUTION.md`, `REVIEW.md`, `ORCHESTRATION.md`, `ONBOARDING.md`, `README.md` (only the specific
lines the round's claims turn on, plus the two greps behind §2.4's gap figures).

**Not verified, marked as process claims:** the `E11` card's rendering and approval; the
executor's cold-start and the `dispatch.CONSTRUCTION_EXECUTOR_PROMPT` form the journal's §8
describes; that `HD-60`/`HD-61`'s retirement in `a554c0b` reflects a user ruling — each of these
lives outside the tracked tree and `R2` marks it rather than accepting it.

**`UNVERIFIABLE`, stated rather than folded into supported (`R4`):** whether the strip recipe I
rebuilt from the journal's prose is byte-identical to the one the round ran. My file counts (123
at both ends) match the journal's, and my real-break counts match to the site, which is strong
concordance — but the recipe is prose in a journal, not a committed script, so two readers can
agree by luck. This is the same gap the journal's own §6 met from the other side.

**Not re-run, and the round does not claim it:** no product run was exercised — no run directory,
no frozen `instruction.md`, no `preview`/`review`/`disposition`, no reviewer dispatched from a
mounted stripped tree. Round 1's honesty cap covers it and this round narrows it no further.

**Mutation caveat (`R4`):** the mutation in §2.5 proves `layer_path_check` has binding force for
one shape and none for another. It does not prove that force is sufficient, and this FULL is not a
certification of the guard.

---

## 6. Conclusion

`REVIEWED_NO_BLOCKER` — 4 lows, 3 observations, no blocker.

All eight acceptance criteria for round 2 are met, each shown by its own command above. The
round's own figures are unusually exact: 13 → 5 to the site, 59 files, 6 pointers, 35 citations
over 26 lines, 19 rider rows, the signed blob's 339 lines and sha256, and the `E2` literal
matching the blob it names in the same commit. Where the round's records disagreed with the
plan — `README.md:16` being both a sweep hit and a truth claim — the records are right and the
plan was wrong, and the round corrected forward rather than in place.

The four lows are all in the record layer and none touches whether the implementation works.
`L-2` banks under `R10`'s `E2` override whatever else is decided. `L-1` is the one I would spend
the least on and value the most: one sentence at closeout, on a defect class this repository has
already been bitten by once.

Per `R10`, a `REVIEWED_NO_BLOCKER` with lows does not bank them by default — the spend-the-fix-leg
versus bank choice for `L-1`, `L-3` and `L-4` is the orchestrator's to put to the user before
closeout, and `E9`'s test does not expire at closeout, so a late activation is still this round's
one user-approved fix and still obliges the VERIFY.
