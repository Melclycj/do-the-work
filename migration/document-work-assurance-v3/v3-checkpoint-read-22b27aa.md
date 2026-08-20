# Instruction-layer read — `22b27aa2e9ae3d10539d93a75f1339726af04a67`

`E10` read of the instruction layer at `22b27aa` (V3-RETRO-RULINGS-v1). Not a round: no
verdict, no budget consumed (`R3`). This dispatch discharges the ledger's ⛔ P5B
precondition ① — the E2 re-baseline changed what a rule requires, so its independent read
must land before any round relies on E2 (`cd4c09e` errata reclassified it from rider
`E2-rb` to a blocking precondition; this record is that read).

**Findings: 1 must-fix, 0 low, 2 observations.** The amendment's every factual assertion
holds against the repository, the member set matches its mirror, nothing has relied on the
amended text, and the citation chain for the eight unchanged members is sound end to end.
The must-fix is not in the amendment's bytes: the obligation record stops one clause short
of `E10` — a rule-requirement-changing amendment "is design and opens a round", and no
round exists or is planned for this one (§6 M-1).

## 1. Subject, re-derived

`R2`: I was handed one SHA and the phrase *the instruction layer*. Everything below is
re-derived from the repository; no figure from the dispatch prompt, the ledger, or any
prior record is accepted as reported.

```
$ git rev-parse HEAD       -> cd4c09e28fc7b9d82c7fd0c09d6a5703d93148ab
$ git status --porcelain   -> (empty)
$ cat .harness/review-pending.json
  {"kind": "layer-read", "subject": "22b27aa2e9ae3d10539d93a75f1339726af04a67",
   "dispatched_at": "2026-08-03T12:41:18+00:00"}
```

Two commits sit between the subject and HEAD — `7fde391` (2026-08-03T21:59:01+10:00,
ledger pointers) and `cd4c09e` (22:18:35+10:00, errata) — both before the dispatch
(22:41:18+10:00); since dispatch the branch has taken no commit, so `E9`'s window is
intact and this record is the only commit it admits. Neither post-subject commit touches
a layer member (`git diff --stat 22b27aa cd4c09e`: `.goals/LEDGER.md`,
`HARNESS-LEDGER.md`, `HARNESS-RIDERS.md`, the retro journal), so the layer at the subject
equals the layer at HEAD, and worktree reads are reads of the subject bytes
(`git rev-parse HEAD:…CONSTRUCTION-CHECKLIST.md` = `2108635f` = the subject blob).

`E10`'s sentence at the subject blob governs the member set: eight enumerated members
plus the open tail realized at Phase D (the paragraph-map schema's amended `description`
strings). The open tail was re-swept, not inherited: the window `9541e1e..22b27aa`'s
paths, classified by hand, are thesis/Paper/Knowledge files (not harness-governed),
`p5a-firewall`/`p5a-shells` run artifacts (run data and records), ledgers and the retro
journal (records), tooling and tests (code), and the run-v2 template README — whose new
battery-tiering rule mass stays template documentation under the standing classification
(`v3-checkpoint-read-9541e1e.md` §1; incorporation parked in the I/O design batch,
inherited deliberately — §6 O-2). Nothing new supersedes prose this harness governs.

| # | blob at `22b27aa` | lines | member | coverage |
|---|---|---|---|---|
| 1 | `2108635f` | 164 | `document-harness/CONSTRUCTION-CHECKLIST.md` | **changed** (`02461be7` → here only) — read in full this session at the subject blob (also as standing instructions); the delta is the single E2 hunk, read as the amendment subject |
| 2 | `f3a31208` | 37 | `document-harness/README.md` | cited: end-to-end read `v3-checkpoint-read-d01615b.md` (row `f3a31208` grepped in that record); blob equality re-checked here |
| 3 | `bd490c8b` | 153 | `document-harness/EXECUTION.md` | cited: `v3-checkpoint-read-d58969d.md` (row `bd490c8b`); equality re-checked |
| 4 | `c19d8cb9` | 259 | `document-harness/REVIEW.md` | cited: end-to-end at `7b553516` (`v3-checkpoint-read-9541e1e.md` §7) **plus** the one delta commit `1cfeeac`, whose REVIEW.md diff is read in full here (§3) |
| 5 | `17ff31bb` | 5 | `migration/…/v3-harness-operating-contract.md` (stub) | cited: `v3-checkpoint-read-784e49b.md` (row `17ff31bb`); equality re-checked |
| 6 | `52a97a48` | 5 | `migration/…/v3-harness-review-contract.md` (stub) | cited: `784e49b` (row `52a97a48`); also read in full this session as the standing-instruction entry point |
| 7 | `68031fa2` | 124 | `contract/…-v3-supersession-1.md` | cited: `v3-checkpoint-read-d58969d.md` (row `68031fa2`); equality re-checked |
| 8 | `e1a2f26b` | 113 | `contract/…-v3-supersession-2.md` | cited: `v3-checkpoint-read-403fc9a.md` (row `e1a2f26b`); equality re-checked |
| 9 | `c2b713bf` | 44 | `schema/document-assurance-v3/paragraph-map.schema.json` (open tail) | cited: `v3-checkpoint-read-d01615b.md` (row `c2b713b`); equality re-checked |

Blob ids from `git ls-tree 22b27aa` / `git rev-parse`; line counts `wc -l` at the subject.
Each citation was verified in the cited record's own text (`grep` of the blob id in that
file), not taken from an intermediate record's table. Per-member `git log
9541e1e..22b27aa` shows exactly two member changes in the window: member 1 at `22b27aa`
(this subject), member 4 at `1cfeeac`. The member set equals `layer_path_check.py`'s
`LAYER` tuple at the subject (nine paths, read at :30–41) — the mirror holds.

## 2. The amendment text, against the repository

The whole layer delta is one hunk in E2 (−2/+5 lines):

> ~~when the pack entry joined this list (2026-07-29, fourteen files); a pack file added
> later is not frozen by this rule.~~
> → at the 2026-08-03 re-baseline (fifteen files: the fourteen of the 2026-07-29 entry
> plus `ResearchSystem/schema/document-assurance-v3/paragraph-map.schema.json`, which
> joined 2026-07-31 and which the 保障面二期复盘 found sitting outside the freeze); a pack
> file added after that date is not frozen by this rule until a later re-baseline — new
> schemas stabilize first, which is why this clause re-baselines rather than auto-freezing.

Every factual assertion in it re-derived by command (`E3`):

| assertion | command | result |
|---|---|---|
| fifteen pack files at the re-baseline | `git ls-tree -r 22b27aa --name-only -- …/document-assurance-v3/ \| wc -l` | 15 — holds |
| "the fourteen of the 2026-07-29 entry" | `git show -s 11d147e` (dated 2026-07-29) + `ls-tree \| wc -l` at it | 14 — holds |
| fifteen = those fourteen + the named file, nothing else | `git diff --name-status 11d147e 22b27aa -- <pack>` | exactly `A paragraph-map.schema.json` — the fourteen are byte-unchanged since the 2026-07-29 entry |
| "which joined 2026-07-31" | `git log --diff-filter=A -- <pack>/paragraph-map.schema.json` | `d50d9e5`, Fri Jul 31 2026 — holds |
| "found sitting outside the freeze" | retro journal §1 at the subject | the discovery block ("一处未冻结缺口（新发现）") — holds |
| only other pack touch in the window | `git log 11d147e..22b27aa -- <pack>` | `34cf85b` — the W-1 wording fix to the then-unfrozen 15th file (its commit body; scheduled by the C4 FULL), frozen fourteen untouched |
| the one added backtick path resolves | file existence | holds (`layer_path_check` also ran at commit per the body) |
| "the only layer member in this diff" | diff stat + member classification by hand | holds — riders, run-v2 README, journal are non-members |

Internal consistency: "Four blobs and one directory, both decidable by inspection" still
holds — the boundary stays four blob ids plus one directory-at-a-commit, and the fifteen
are now pinned by enumeration (fourteen-by-dated-entry + one named). The escape clause's
"added after that date" referent was probed for ambiguity: under either candidate reading
(the re-baseline date vs the parenthetical's 07-31), the frozen set is identical — the
fifteen are enumerated, no file joined the pack between 07-31 and the re-baseline, and
any future addition postdates both — so no decision can diverge; not a finding. Ruling
(6)'s record (journal §7 item 6) covers this content shape: re-baseline chosen over
deleting the escape clause, "新 schema 先稳定再冻" preserved.

Reliance check: the commits since the subject are ledger pointers and the errata —
recording and citing, which `E10`'s parenthesis excludes from reliance; no round has
opened; P5B has not opened. This read therefore lands before any reliance on the amended
E2, the deferral-free path the precondition demands.

**Member 4's window delta (`1cfeeac`), verified at the bytes:** the REVIEW.md hunk is
exactly the `9541e1e` read's F-1 named content — the freeze-marker sentence gains the
advisory / per-machine qualification pointing at README's Local-enforcement row — plus a
closing clause ("re-derive the freeze window … instead of assuming the hook held it")
that restates the re-derivation duty F-1's own body already named as the existing rule's
demand; no check outcome, obligation, permission or verdict path moves. Its
no-round-no-read classification was adjudicated at `v3-review-full-1cfeeac.md` §4 and
re-checked at `v3-review-full-4f88dce.md` §4; not reopened here — the bytes were.

Staleness the byte-key cannot see: the eight unchanged members were grepped for the
delta's vocabulary (fourteen/fifteen/十四/paragraph-map/re-baseline/frozen). No member
states the old count or contradicts the re-baseline; README's paragraph-map row and
Local-enforcement row describe the same instruments consistently.

## 3. Ledger bindings, checked

- **⛔ P5B precondition ①** — this record is the owed independent read, landed before any
  reliance (§2). It discharges the amendment-read obligation. Whether that closes the
  precondition is exactly what M-1 puts to the user: the read cannot stand in for the
  round `E10`'s design sentence names, and `E10` forbids banking it as one ("never banked
  as the round's FULL").
- **`cd4c09e` errata, verified applied**: rider `E2-rb` absent from the bank at HEAD
  (five rows: F-c, O-2b, SCC, RA, CLI-hist); journal §7 item 6 carries the errata inline;
  the obligation sits in the ledger's P5B block. Nothing retroactively tainted — the
  no-reliance claim re-derived here, not taken from the errata.
- **No other in-layer application rides this read**: the window's only member deltas are
  `1cfeeac` (R9 ride — owes no read by its adjudicated classification) and the subject
  amendment itself. The bank holds no row redeemable by a read (a read touches no surface).
- **Budget**: this read spends nothing (`R3`); since dispatch the branch admits only this
  record (`E9`).

## 4. Findings

### Must-fix

**M-1 — the obligation record stops one clause short of `E10`: a rule-requirement-changing
amendment "is design and opens a round", and no round exists or is planned for the E2
re-baseline.** Location: HARNESS-LEDGER ⛔ P5B precondition ① (whose remedy is this read
alone); `cd4c09e`'s errata (same scope); journal §7 item 6 (channel sentence). Ground
truth: the errata's own quoted test — "neither adds a clause to any rule nor changes what
any rule requires … and whose effect on every round in flight is nil" — is `E10`'s
*deferral* test, and the errata correctly finds the re-baseline outside it; the very next
clause of `E10` is the *design* test: "an amendment adding a clause to any rule, or
replacing or deleting text so that what a rule requires changes, **is design and opens a
round**." The errata applied the first and stopped before the second. The letter is
corroborated by the same-day 批分型 ruling ("规则变更批照旧走轮", ledger 2026-08-03) and
by uniform precedent — every prior rule-changing layer amendment passed an independent
FULL (`af2905c` round with review+fix legs; `8ec4c60` FULL; `feacb86` FULL, whose
authorizing ruling itself says "是一个 amendment 轮"; `5f029cd` submitted to its batch's
FULL, which `v3-checkpoint-read-9541e1e.md` §3 records as what "conforms to `E10`'s
design test"; `34cf85b`'s E1 sentence rode Phase D's round). This read cannot absorb the
gap: an amendment read "is never banked as the round's FULL" (`E10`). Downstream decision
that goes wrong if unfixed: P5B opens treating precondition ① as satisfied and relies on
the re-baselined E2 — the first reliance on a layer rule change that never passed an
independent FULL, the defect class the design sentence exists to block. Minimum fix: a
user ruling before P5B relies on E2 — either (a) open the amendment round (an independent
FULL over `22b27aa`'s layer diff; `E9`'s legs then apply), or (b) record that ruling (6)
covers the process channel for this amendment, making the ruling itself the gate for this
instance. Which of the two is the user's call (`R5`; `R7` — the rulings live in chat and
§7's record covers the content shape; the channel sentence beside it was executor
classification, already errata'd once). Channel note: `E10`'s must-fix answer channel
(amendment + re-read) fits text defects; this finding's remedy is a ruling, not bytes —
flagged so the executor routes it to the user, not the free channel.

### Observations (`R5` — reported; conclusions are the user's)

**O-1 — the 15th frozen file is also a layer member; the two registers now overlap.**
`paragraph-map.schema.json` is simultaneously an `E10` member (the open tail's amended
`description` strings) and, since this amendment, an `E2` frozen file. A future amendment
to its description strings is a layer edit that first needs the freeze reopened by ruling
— the pattern the bank's O-2b row already records for `local-check-spec`
("属 `E2` 冻结面，须裁决重开才能兑"). A consequence of ruling (6) inherited knowingly from
this record on; whether it is intended is the user's question.

**O-2 — the run-v2 README again grew rule mass under the parked not-a-member
classification** (the battery-tiering section, this window). Nothing new to decide here —
the ledger already carries it three deep ("BATTERY-TIERING O1 三度加注") for the I/O
design batch; noted so the inheritance stays visible in the read chain.

## 5. Coverage disclosure (`R4`)

**Read in full:** member 1 (164 lines at `2108635f`, also as standing instructions);
member 6 (5 lines, standing-instruction entry); the subject's E2 hunk and complete commit
body; the complete bodies and member diffs of `1cfeeac`, `cd4c09e`, `34cf85b`;
`v3-checkpoint-read-9541e1e.md` (239 lines); journal §7 at the subject and at HEAD
(errata inline); `HARNESS-LEDGER.md` (111 lines) and `HARNESS-RIDERS.md` (16 lines) at
HEAD.

**Sampled:** `v3-review-full-4f88dce.md` §4; retro journal §0–§1 (the discovery block);
`layer_path_check.py` :1–60 (docstring + `LAYER`); the window's `--name-only` path list,
classified by hand; the four cited read records — grepped for their member blob-id rows,
not re-read whole.

**Probed only:** `.harness/review-pending.json`; pack `ls-tree` counts at `22b27aa` and
`11d147e`; `d50d9e5` / `11d147e` / `7fde391` / `cd4c09e` dates; per-member `git log` over
the window; blob equalities via `ls-tree` / `rev-parse`; `wc -l` line counts.

**Not verified:** that this read ran in a fresh context — a process claim, marked. The
six rulings beyond their in-repo records (`R7` — ceiling stated, not a block). The
interiors of the four cited end-to-end read records beyond their blob-id rows — citation
under `E10` rests on the stated blob id, verified in each record's own text, plus blob
equality at the subject, re-derived here. The battery and suites — not re-run: no code,
schema or generated surface is in the subject's layer diff, and the subject commit's own
tier declaration records the batch-specific checks it ran; their binding force is that
commit's property, not this read's.

**Ceiling:** whether the design-round obligation attaches (M-1's two arms), whether the
freeze/member overlap is intended (O-1), and every consolidation choice remain the user's
questions under `R5`; what is checked here is that the amendment's text matches the
repository, that the member set matches its mirror, that nothing relied on the amended
rule before this read, and that the bookkeeping around it did what its own rules say —
except the one clause M-1 names.
