# VERIFY — `b8df15a..d0f185c`

**Verdict: `REVIEWED_NO_BLOCKER`.** 1 finding above low (`V-1`), 1 low (`V-2`), 6
observations. Every accepted finding landed, and every one of them landed as the bytes its
finding supplied or as an equivalent I checked against the source rather than read. The
merge's restored statements are byte-identical to the frozen sources they came from, the
new member is really guarded (probed, both controls), and the battery is green at 792 on my
own run.

`V-1` is the reason the verdict word is worth reading twice. `R3` gives a VERIFY only
`REVIEWED_NO_BLOCKER` or `SPEC_GAP`, and there is no spec gap here — the ground truth
settles the question without ambiguity. But `V-1` is the accepted blocker's own defect class,
alive at a fifth site, and that site was **created by the repair**: the same commit that
struck *the signed contract v4* out of `E10`'s neighbourhood wrote *the operative contract*
into `E10`'s membership sentence. The word the verdict lacks is the one the FULL had.

Independence: this session received the range and nothing else. Round, budget, authorization,
obligations and every number below were derived from the repository; no reported figure was
accepted, including the two sweeps the fix commit pastes. `R1`'s four holdings are the
orchestrator's. That this session was cold is a process claim about itself and is not
verifiable from the repository (`R4`).

---

## 1. What the subject is, derived

`git rev-list --count b8df15a..d0f185c` → **6**.

| | |
|---|---|
| base | `b8df15a14229944270ae6ff720b14f57170f9b1a` — `V3-PUB-FACADE-CLOSEOUT-v1` |
| tip | `d0f185c04269a40f48e5a75ae10191b170cb085d` — `V3-CONTRACT-V4-FIX-v1` |
| round | `CONTRACT-V4` (publicization batch B) |
| commits, kinds as their bodies name them (`E8`) | `f0b891d` record (opening `E10` read) · `0616fcf` plan (ruling carrier) · `23ca45b` candidate · `5f849da` record (round journal) · `28852a6` record (FULL) · `d0f185c` review fix |
| branch tip at review time | `d0f185c` — the dispatched tip |
| worktree | clean; `git status --porcelain` empty |
| freeze marker | `.harness/review-pending.json` carries this exact range, `dispatched_at` `2026-08-23T07:31:48+00:00`; `d0f185c` committed `07:31:34+00:00`, i.e. 14s before dispatch |
| push state | `main...origin/main [ahead 6]` — nothing pushed (`E8`) |

**Budget position, derived.** `v3-review-full-5f849da.md` exists under
`migration/document-work-assurance-v3/` and is committed at `28852a6` with verdict
`CHANGES_REQUIRED`. A valid independent FULL has therefore occurred, so `d0f185c` is the
round's **one user-approved fix**, and it obliges this VERIFY — which it says. `f0b891d` is
an `E10` read and by `R3` spends nothing. **This is the targeted VERIFY and closes the
round's budget.** No `v3-review-verify-*` record for this round existed at the subject.
`E9`'s last clause holds: from dispatch to now the branch has taken no commit at all.

**Authorization, derived.** Four rulings of 2026-08-23 carried by the plan (`0616fcf`), and
four more folded into the fix and carried only by `d0f185c`'s commit body: the fix itself,
restoring the three dropped statements, confirming v3's retirement, and admitting contract
v4 to the instruction layer. `HARNESS-DECISIONS.md` carries no entry for any of the eight.
Per `R7` that is a ceiling stated, not a block: they are recorded *in the repository*, so
`R2`'s chat-only test is not tripped. `O-6` is what I do with the ceiling.

**Obligations, derived.** The accepted findings of `v3-review-full-5f849da.md`; the whole
repair diff; the permanent boundaries `E1`–`E12` / `R1`–`R10`. `HARNESS-DECISIONS.md`
`§live` read end to end this session (`HD-44`, `HD-41`, `HD-36`, `HD-35`, `HD-34`, `HD-23`,
`HD-9`), plus `HD-20`, `HD-21`, `HD-22` from `§implemented` by grep.

---

## 2. Lead with the implementation

### 2.1 The four `B-1` sites, checked as bytes

| site | now reads | verdict |
|---|---|---|
| `CONSTRUCTION-CHECKLIST.md` | "they merged / into contract v4 and left the tree with it" (across a line break) | **paid** — `git grep "the signed contract v4"` returns nothing |
| `document-harness/README.md:17` | row label `Contract v4 (candidate — awaiting signature)` | **paid**, the reviewer's exact bytes |
| `README.md:82-83` | "the count is nine since round `CONTRACT-V4` merged the two supersessions into contract v4 and admitted v4 as a member" | **paid**, and the count corrected in the same stroke |
| `governance-exemptions.json` retired `why` | "…the removing decision is round `CONTRACT-V4`'s signature entry in HARNESS-DECISIONS.md, owed at the signing checkpoint and not yet written." | **paid**, the reviewer's exact bytes |

The ground truth is unchanged and was re-derived, not carried over:
`grep -n -E "v4|CONTRACT-V4|614932de" HARNESS-DECISIONS.md` returns no v4 entry; v4's own
header says *"This contract becomes binding only when the user signs it"*; the plan says
*"until it lands v4 is candidate text, not a contract"* (`:16`).

**The class, swept my way rather than theirs.** Two patterns over all tracked files, then
classified by hand: `signed contract` (43 hits, all in records, journals, archive, or v4's
own §13 rule text — none asserting v4's state) and `v4` within 80 chars of `signed|operative`.
The second pattern returns two live non-record sites the fix's own SWEEP A could not see,
because it keyed on the signature word and the class does not. One of them is `V-1`.

### 2.2 The lows

- **`L-1`** — `document-harness/README.md:18` now says "exactly the one file the row above
  names". `ls contract/` returns **1**. Paid.
- **`L-2`** — the register note is rewritten to one grandfathered document, and its new
  factual claims were checked rather than read: the exempted blob
  `8ad404b12b3242e700d0ad215048dffccada7d9c` is **not reachable in this repository**
  (`git cat-file -e` fails), consistent with its `path_hint` `.goals/plans/…` being the
  caller's tree; the in-tree copy `document-harness/plans/document-work-assurance-harness-v3.plan.md`
  is blob `ccc34923…`, **a different blob**, exactly as the note now says; and
  `git grep governance-exemptions` returns eight hits, every one prose — no loader, so the
  file moves no check outcome. The retired entry no longer over-quotes: note line 24 reads
  *"Adding an entry here requires a user decision"*, and the entry now says the note
  *"reserves adding an entry to a user decision, and removal follows the same authority"* —
  the inference is now marked as an inference. `json.load` parses clean. Paid.
- **`L-3`** — the parenthetical is gone; the supersession sentence stands alone after the
  list, so nothing now reads as describing the paragraph-map schema. Paid.
- **`L-4`** — applied. The executor asked this VERIFY to re-route it to the bank if the
  bytes change what `E2` governs. They do not; reasoning in `O-5`.
- **`L-5`** — both sweeps are pasted with `path:line 'content'` for every hit, which is what
  makes `HD-41` ④'s stated purpose ("跑没跑可被评审员当场看见") achievable, and rider
  `fixleg-scan-raw` is deleted in the same commit as its redemption, per `R10`. Paid **as a
  discipline** — and `V-1` is what that discipline caught nothing of, because the pattern was
  narrower than the class.

### 2.3 `O-5`, byte-checked against the frozen sources

Not read as restored — diffed against the blobs `E2` names.

| statement | source | v4 today |
|---|---|---|
| `(wave-2 design §9)` | `68031fa2:112` | `:283`, identical run of text |
| `nothing requires or checks a digest on it` | `e1a2f26b:88` | `:318` |
| `it was named here in error` | `e1a2f26b:88-89` | `:318-319` |

All three land inside the `instruction_ref` clause exactly where the source put them,
including the `is **not** among them` lead-in that makes the sentence read as the source's
correction rather than as a new claim. The one divergence from `s1` at `:285` —
"the signed contract §1's threat model" → "§1's threat model" — is `D8`'s declared
self-reference adaptation, already in boundary.

### 2.4 Do the guards still bind — the new member especially

The membership change is the round's one genuinely new mechanism, so it was probed rather
than argued. Every mutation restored from sha256-checked scratchpad copies, never
`git checkout --` (`E4`); digests re-verified after each restore, and
`git status --porcelain` confirmed empty afterwards.

| # | probe | expected | result |
|---|---|---|---|
| A | unresolvable token staged into `contract/…-v4.md` | red | **red** — exit 1, naming the new member and the token |
| B | resolving token staged into the same file (negative control) | green | **green** — exit 0 |
| C | drop `contract/…-v4.md` from `LAYER` | red | **red** — `test_layer_equals_the_hand_written_membership` and `test_every_member_is_scanned` both fail; the other 50 cases in those two files stayed green |
| D | grep `614932de` / `a775e28f` anywhere under `tooling/` or `.githooks/` | — | **no hit** — the `E2` literal is bound by nothing (`O-1`) |

A and B together prove the membership has mechanical force and not merely prose force: the
new member is really scanned, and the guard does not simply block everything. C proves the
`E10-sync` machine leg binds at nine; `EXPECTED` is hand-written and not imported from the
module it guards (`E5`).

### 2.5 Re-derived measurements (`E3`, `R2` — no reported figure accepted)

| claim | where claimed | re-derived |
|---|---|---|
| battery green | fix commit body ("792 passed in 93.81s") | **792 passed in 97.57s**, Windows, `python -m pytest -q` from `tooling/` |
| the layer-mirror test now asserts nine | fix commit body | mutation C — it does |
| nine members resolve | `README.md:58` row | `len(LAYER)` = **9**, all nine `.exists()` |
| membership sentence == `LAYER` == `EXPECTED` | fix commit body | hand-compared: same nine paths, **same order**, all three |
| `E2` literal equals the blob | `E2` clause | `git rev-parse HEAD:contract/…-v4.md` → `614932de40b841ec9777719aea88de04864eb67b`; clause reads `614932de…` |
| `governance-exemptions.json` re-parses | fix commit body | `json.load` clean; `exemptions` 1, `retired` 1 |
| schema pack still fifteen and untouched | `E2` clause | `ls schema/document-assurance-v3/` → **15**; `git diff --name-only b8df15a d0f185c -- schema/` → **empty** |
| no unresolved path token in a member | — | `unresolved_tokens` replayed over the **whole standing text** of all nine members: **0** |
| the new member's guard-blind shapes | — | 0 placeholder-segment path tokens; 13 relative markdown links, **0 broken** |
| `contract/` holds one file | `L-1` fix | `ls contract/` → 1 |
| the two review records are unedited since landing | `R6` | `git log --` on both returns exactly one commit each |

### 2.6 Process and record conformance (boundary check, run second)

`E8`: title `V3-CONTRACT-V4-FIX-v1`, the round's established form; body one paragraph, one
trailing blank, zero git trailers (the single `Kind:`-shaped line is `E8`'s own kind
naming); explicit paths, ten of them, nothing pushed. `E9`: the objective test is applied
correctly — a valid independent FULL had occurred, so this is the fix round and it says it
obliges the VERIFY; no round is self-classified. `E9`'s "exceeding an approved fix boundary
requires saying so" is **met**: the membership admission was not in the plan's change
surface and the body says so in its first sentence, naming all four folded rulings.
`E6`: no finding was answered with new machinery — every accepted finding is the named text
changing, and the one line added to `LAYER` / `EXPECTED` is `E10-sync`'s mirror of a
membership change, not a guard invented to close a finding. `E1`: the round-scoped
disclosure lives in the candidate (`23ca45b`, all four `R1` holdings named as the
executor's); the fix leg carries none of its own, which is adequate at round scope but is a
process claim I cannot verify either way (`R4`). `E10`: the amendment is design (it changes
what `E10` requires) and landed inside an already-open round under a user ruling, with its
independent read deferred to the next opening cold read, as precedent establishes — and
`HD-21`'s obligation on the round that creates a member is discharged in the commit body,
which records both the question (the FULL's `O-2`, routed via `R5`) and the answer.
`R10`: `fixleg-scan-raw` deleted in its redeeming commit; 27 rows remain; `O-4` is the one
row this round should have written to and did not.

---

## 3. Findings

### `V-1` — `B-1`'s class survives at a site the repair created, in the membership sentence

**Location.** `document-harness/CONSTRUCTION-CHECKLIST.md:109`:

> `contract/Document-Work-Assurance-Contract-v4.md` — **the operative contract**, a member by
> the user's 2026-08-23 ruling as the prose successor to the three signed texts it merges

**Why this is inside the accepted finding and not a fresh one.** The FULL's `B-1` site table
lists, as its second of four, `document-harness/README.md:17`'s row label
*"Contract v4 (operative)"* — so the bare word **operative** is inside the class `B-1` named,
on the FULL's own enumeration, and the reviewer's bytes for that site replaced it with
*candidate — awaiting signature*. The fix took those bytes at that site and wrote the word
into the `E10` membership sentence in the same commit. `E10`'s must-fix channel admits "that
same fix at every other site of the defect the finding names"; `E7` says test the class, not
the instance; `HD-41` ④ says scan the class before writing. The scan ran (`L-5` is paid) but
keyed on *signed*, and *operative* is the half of the class it could not match.

**Ground truth it violates.** Unchanged and re-derived in §2.1: no v4 entry in
`HARNESS-DECISIONS.md`, v4's own header conditions binding force on signature, the plan
calls it candidate text. Two `E10` members now contradict each other on the same fact, and
both sentences were written by this one commit: `document-harness/README.md:17` says
*candidate — awaiting signature*, `CONSTRUCTION-CHECKLIST.md:109` says *the operative
contract*.

**Why it binds an action rather than reading as a wording slip.** It is the same permission
`B-1` turned on. v4 §13, carried unchanged from v3, is *signed contracts are never amended
in place; corrections create a versioned successor*. Text calling v4 operative says an
in-place correction is barred and a v5 is owed; the truth says it is free — and this round
exercised that freedom fourteen commits' worth of minutes ago, writing v4's bytes for `O-5`.
The round's remaining legs (closeout, then the signing checkpoint the user must reach by
reading v4 in full) may need it again. The site also carries more weight than the one the
FULL found: it is not a navigation row but the `E10` membership sentence, the first thing a
cold executor reads, sitting six lines below `E2`'s clause listing v4 as frozen bytes — so
*frozen* and *operative* read together as *signed and locked*.

**Minimum fix** (a deletion, so the leg is cheap; no clause added, no bound changed):

- `CONSTRUCTION-CHECKLIST.md:109` → `` `contract/Document-Work-Assurance-Contract-v4.md` — a
  member by the user's 2026-08-23 ruling as the prose successor to the three signed texts it
  merges — and ``

**Routing, stated without adjudicating it (`R10`).** The site is an `E10` member and is
**not** a path `E2` freezes, so `HD-20` does not gate it and both of `E10`'s channels are
open on their own terms; either way the application is not a round and spends no budget, so
`E9`'s closed budget does not stand in the way. Whether it is must-fix or below is the
orchestrator's call, not mine.

**Two sibling sites, named and deliberately not asked for.** `contract/…-v4.md:21`
("into one operative text") carries the same word unconditionally in its own sentence, but
the warning callout four lines above says binding force waits on signature, so a reader
cannot be misled; and v4 is `E2`-frozen, so under `HD-20` bytes for it bank until a recorded
ruling exists. `contract/…-v4.md:335-336` is guarded by its own lead-in, *"User signature
means:"*, and is correct as written. `tooling/tests/document_harness/test_candidate_checks.py:1983`
carries the word in a docstring where no permission turns on it. I name all three so the
class is enumerated, and ask for none of them.

### `V-2` (low) — the plan says "one signed v4"

`document-harness/plans/contract-v4.plan.md:37`: *"Batch B merges the three into one signed
v4, retires the residue…"*. Same class, but the plan is not an `E10` member, the sentence is
the batch's stated goal rather than a claim about today, and the accurate fact is two dozen
lines above it (`:16`, "until it lands v4 is candidate text, not a contract"). That makes it
wording-level under `R9`: recoverable from adjacent text, and I can name no downstream
decision that goes wrong if it stays. It rides the next batch touching this plan, and it
expires with the round's closeout.

---

## 4. Observations

### `O-1` — the `E2` blob literal is bound by nothing (measured)

`git grep` for `614932de` or `a775e28f` under `tooling/` and `.githooks/` returns nothing:
no test, no hook, no CLI command compares `E2`'s literal against
`git rev-parse HEAD:contract/…-v4.md`. Today they agree — I checked, and the literal is
right. The reason to record it anyway is that this round already wrote it wrong once: the
journal's self-catch 1 says the literal was first written from a pre-correction staging
(`b1f651a2`) and updated only after the lineage paragraph changed, and the fix leg had to
move it again. Two writes, two chances, no guard either time. This is a **measurement, not a
request for machinery** — `E6` points the other way and `HD-27` has refused an `E2` guard
three times — and it is the same shape the FULL measured at `CONTRACT_PATH` (`O-1` there).

### `O-2` — v4 now sits in the `HD-20` intersection, and `HD-20`'s own text has gone stale

`HD-20` governs paths that are simultaneously `E2`-frozen and `E10` members: their bytes
"先欠 `E2` 的 recorded ruling", neither the free channel nor the must-fix channel writes
them, and a finding supplying bytes banks until the ruling exists. Its text says
"现仅 `paragraph-map.schema.json`". As of `d0f185c` there are **two**, and the second is a
339-line contract. The consequence is real and forward-looking: from now on a reviewer who
finds a defect in v4 and supplies the exact bytes cannot have them applied on any cheap
channel — they bank until an `E2` ruling exists, and the ruling that would unblock them is
the signature the round is walking toward. `HARNESS-DECISIONS.md` is the user's file and
carries no amendment machinery (`HD-7`), so this is stated for the user, not filed.

### `O-3` — the next opening cold read gains a 339-line member with no citation available

`E10` lets a read cite a prior record instead of re-reading, but only for "a member whose
blob is unchanged since a recorded end-to-end read **of it**", with the blob id recorded.
No such record exists for v4: the FULL read it in full, but at blob `a775e28f` (now
`614932de`), and `E10` bars banking an amendment's read as a round's FULL in any case. So
the next round's opening read owes v4 a fresh end-to-end read at full cost. This is a price,
not a defect — and it is the exact price that answers the FULL's `O-2` worry that after this
round nothing would oblige an independent read of the merged prose. The user's ruling bought
the obligation; this is what it costs.

### `O-4` — the `E10-sync` rider row was not written to by the round that touched the sentence twice

`HARNESS-RIDERS.md:16` exists to be checked at every touch of the membership sentence
("本行是每次触碰时的核对项，非一次性兑付"), and its latest recorded touch is still
2026-08-18's `ORCHESTRATOR-CHARTER` (九→十). This round touched the sentence twice — ten→eight
in `23ca45b`, eight→nine in `d0f185c` — and the row says neither. The **substantive**
obligation was met both times and I verified it (three sites in one commit, named in the
body); what is stale is the row's own narrative and its enumerated prose sites, whose line
numbers have drifted (root `README.md` `:33/:50` → today `:58/:83`; `ONBOARDING.md:130` →
`:133`). Nothing is unenforced; the next toucher just gets a worse map.

### `O-5` — `L-4` adjudicated: transcription, not design, and the residual is the user's

The executor applied `L-4` and asked this VERIFY to re-route it if the bytes change what
`E2` governs. They do not. `HD-44`'s holding is that `E2` freezes **bytes, not this
repository's paths**; a blob that lives only in history is immutable by construction, so
`E2`'s "not written without a recorded user ruling" can never bite on it, and the new
wording ("their bytes are immutable in history at those blobs and are not what this list
governs") says exactly that. `HD-44`'s parenthetical enumeration of the three blobs
describes `E2`'s list as of 2026-08-18; it is not independently constitutive, and ruling 3
of this round authorised the list to re-point. The clause also stops contradicting itself,
which was the whole of the finding.

The residual is not mine to close: `HD-44` `§live` still enumerates three blobs whose
governance the clause now disclaims, so a reader holding both open sees an eighteen-item
freeze surface in one and a sixteen-item one in the other. `§live` outranks the instruction
layer on conflict and only the user may change it (`R5`, `HD-7`).

### `O-6` — a ruling that binds every future round has a commit body as its only home

`HARNESS-DECISIONS.md`'s own admission test takes an entry when the ruling "绑下一轮及以后".
Admitting v4 to the instruction layer does precisely that: it changes `E10`'s membership,
the next cold read's scope, and — via `O-2` — which repair channels are open on that file
forever. `HD-21`'s narrower obligation is discharged (the question and its answer are in
`d0f185c`'s body), and the round does record an `HD` entry as owed — but for the
**signature**, not for the **membership**. After closeout the commit body is the only carrier,
and `§live`, not `git log`, is what each round's cold read is sent to. Whether the membership
ruling earns its own entry is the user's call, and I state it rather than conclude it (`R5`).
The same ceiling covers all eight of this round's rulings (`R7`): I verified they are
recorded in the repository, never that they were given.

---

## 5. Coverage — read in full, sampled, only probed (`R4`)

**In full:** the six commit bodies; the whole `b8df15a..d0f185c` diff at `-U6`;
`v3-review-full-5f849da.md`; `document-harness/CONSTRUCTION-CHECKLIST.md`;
`tooling/hooks/layer_path_check.py`; `migration/document-work-assurance-v3/N1/governance-exemptions.json`
(as parsed JSON, every note line and both entries); `HARNESS-DECISIONS.md` `§live`;
`.harness/review-pending.json`; the four `B-1` sites and the `L-1`/`L-3` sites in context;
the `O-5` restoration sites in v4 against `68031fa2` and `e1a2f26b`.

**Sampled:** `contract/Document-Work-Assurance-Contract-v4.md` — header, §13.1, §13.2, §14,
and every path token and markdown link programmatically, but **not** its 339 lines end to
end; `HD-20` / `HD-21` / `HD-22` by grep with context, not the whole `§implemented` section;
`document-harness/plans/contract-v4.plan.md` at `:14-18`, `:30-42`, `:69`;
`document-harness/README.md`, root `README.md`, `ONBOARDING.md`, `.githooks/pre-commit`,
`HARNESS-RIDERS.md` at the diff plus surrounding context; the journal via `5f849da`'s body;
`HARNESS-DECISIONS-archive.md` by grep only.

**Only probed:** the rest of the 792-case battery (run, not read); the 31 prior
`v3-review-verify-*.md` records (verdict lines only, to derive the record convention).
`document-harness/EXECUTION.md`, `REVIEW.md`, `ORCHESTRATION.md` not read this session — no
change touched them; their path tokens were scanned programmatically.

**`UNVERIFIABLE` from here, not folded into supported:** whether the eight rulings were
given (only that they are recorded — `R7`); whether the fix leg was authored by the same
merged-role session the candidate disclosed (`E1`/`R4`); the caller repository, including
whether `ac1b383` is what `document-harness/README.md` says — it does not resolve here,
which the checklist's preamble makes the expected reading for a caller-repo id; POSIX
behaviour, since this session ran Windows only and the round's WSL figures are the journal's,
not mine.

**What mutation proved and did not.** A–C show those guards bind on the defect shapes I
reproduced — the new member is genuinely scanned, and the mirror test genuinely fails when
the mirror breaks. They do not show that force is sufficient, and D shows one literal with no
force at all. A VERIFY is never a re-certification: this record says the accepted findings are
paid and the repair diff is sound, not that contract v4 is text worth signing. That reading
is the user's leg, and it is still ahead of him.
