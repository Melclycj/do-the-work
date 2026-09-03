# Plan — batch `CORE-MOUNT`: the core-only mount becomes a step a caller can repeat from the mount alone

> **Status: OPEN 2026-09-03, one round, `CORE-MOUNT`.** Established by the user's ordering ruling
> of 2026-09-03 (conversation, after the orchestrator's assessment of the three open concerns):
> the queue is **`CORE-MOUNT` → batch `EXECUTOR-LIFECYCLE`** (candidate isolation and
> dispatch-economy merged into one batch, isolation first). Base for every figure: `05ae1b6`,
> branch `dev`. A cold session reads this file, then `CONSTRUCTION-LEDGER.md`'s current
> pointer, then works.
>
> **Not design.** No clause is added to any rule, no rule's requirement changes, and no `E10`
> member is edited (acceptance 4 measures it). The opening cold read is still owed (`E10`:
> at each round's opening unless the user waives it) and this one also carries a debt the user
> cannot waive away: batch `PROMISE-PATH`'s closeout (`05ae1b6`) named "the next round's
> opening cold read" as the carrier of the independent re-read owed on `RULES.md` `R3`,
> `REVIEW.md`, contract `:118`/`:127` and `README.md:20` — deferral, never exemption. A waived
> layer read would carry that debt one round further; `§live` is read either way.
>
> **Every figure below was measured 2026-09-03 at `05ae1b6`** with `git ls-files`, `git
> rev-parse`, `grep -n`, a scratch clone, and `python -m pytest tooling/tests -q` (**956
> passed**, 199.77s). Re-run before any claim (`E3`); line numbers drift.

## Goal (one line)

**A repository that mounts this harness can materialize the product-run tier and nothing
else, from what the mount itself carries**: the list of what travels travels, the step is
written where onboarding is, and a test binds the list to the table that defines the tier —
so `HD-66`'s path ① (sparse-checkout) is repeatable rather than a one-off ruling.

## What exists, and what does not — measured

- **The path exists once, as a ruling.** `document-harness/plans/core-only.plan.md` ruling 39
  (2026-08-30): inside the caller's submodule checkout, `git sparse-checkout set --no-cone
  --stdin` over the product-tier paths, and `--disallowedTools WebFetch,WebSearch` on every
  cold session the run dispatches. Used once, for round `CORE-ONLY-RUN` in the caller
  (mount `3060a23`, sparse 59, three runs, promotion `d6a5919`). Per-checkout, untracked,
  the instrument untouched (`HD-34`).
- **The list a caller needs lives only where a caller cannot reach it.** The tier is defined
  by `CONSTRUCTION-INDEX.md`'s product-run table — a construction-side file, not in any
  product-tier row. `grep -n -i 'sparse\|core-only\|core only'` over
  `document-harness/ONBOARDING.md`, `README.md` and `document-harness/README.md` → **0 hits**.
  A caller bumping its gitlink today re-derives the path list by reading this repository,
  which is what "no path to call core only" names.
- **The index's figures are stale by the batch after them.** `CONSTRUCTION-INDEX.md` says
  59 product-tier files against 421 at `8ce93f7`; at `05ae1b6` the same commands return
  **60** and **438** — `bind-declarations.schema.json` joined the schema pack in round
  `PROMISE-PATH-ENGINE` (2026-09-02), so row 2's "14" is fifteen. The file's own header
  says to re-run rather than cite, and this round touches that paragraph anyway.
- **`HD-66` stays live and is not judged here.** Submodule is the default; plugin only if
  core distribution is proven impossible, and the ruling names three paths to walk first:
  ① sparse-checkout, ② the checklist design round (done, rider
  `checklist-cited-not-carried` redeemed), ③ a core-only release artifact (untried). This
  round makes ① repeatable. It does not walk ③ and does not open the plugin question.

### The probe — a scratch clone at `05ae1b6`, 2026-09-03

`git -c core.longpaths=true clone --no-checkout` into the session scratchpad, then the
fourteen product-tier paths as `--no-cone` patterns, one per line, **no leading slash**
(a gitignore-style pattern with a slash in the middle is root-anchored):

```
contract/Document-Work-Assurance-Contract-v4.md
schema/document-assurance-v3/
document-harness/RULES.md
document-harness/README.md
document-harness/EXECUTION.md
document-harness/REVIEW.md
document-harness/ORCHESTRATION.md
document-harness/ONBOARDING.md
document-harness/templates/
tooling/dtw.py
tooling/do-the-work.py
tooling/rsclib/document_harness/
tooling/hooks/
assurance/templates/run-v2/
```

| measured | result |
|---|---|
| tracked files on disk after `git sparse-checkout set --no-cone --stdin` + checkout | **60** (the two extra files `find` later saw were `__pycache__` from running `dtw`) |
| `git ls-files -- $(cat patterns)` at the same tip | **60** — the two consumers agree |
| `CONSTRUCTION-LEDGER.md` · `HARNESS-DECISIONS.md` · `document-harness/CONSTRUCTION-CHECKLIST.md` · `tooling/construction_dispatch.py` on disk | **absent**, all four |
| `python tooling/dtw.py --help` | **exit 0** — `tooling/rsclib/` has no `__init__.py` outside `document_harness/`, so the package resolves as a namespace and the tier is import-complete |
| the same fourteen lines with **CRLF** endings fed to `--stdin` | **60** — git strips the CR (`git sparse-checkout list` shows clean patterns) |
| the CRLF file expanded into a `git ls-files --` pathspec by a shell | **8 of 60** — the shell does not strip CR; this checkout has `core.autocrlf=true` |

Two consequences carried into the design: the manifest's lines are root-anchored paths
without a leading slash, usable by both consumers; and every shell command this round
documents that expands the file into arguments strips CR first.

## Design decisions — the orchestrator's, stated so the FULL can dispute them

1. **The manifest is a pattern list, not an expanded file list.** `document-harness/product-tier.txt`:
   one repo-relative path per line, the product-tier table's *Where* tokens verbatim
   (directories with a trailing slash), **self-including** (its own path is a line, so a
   sparse mount carries the list it was made from and can redo the step after a gitlink
   bump). Not taken: sixty expanded paths — the index's own count went stale by one within
   four days of being written, and a per-file list needs an edit for every file added inside
   a row directory while saying nothing the row does not.
2. **The step lives in `ONBOARDING.md` item 1 as its second half, not as an eleventh item.**
   `document-harness/README.md`'s onboarding row says "ten items"; an eleventh would make an
   `E10` member's sentence false and open the amendment channel for a count (`E6`: no). The
   half states Do (initialize the submodule, then `git sparse-checkout set --no-cone --stdin
   < <mount-path>/document-harness/product-tier.txt` inside it; cold sessions dispatched
   from such a mount run with `--disallowedTools WebFetch,WebSearch`, since the instrument
   is public and a session could fetch what the checkout hides; after any gitlink bump,
   re-run the set from the new revision's manifest), See (file count on disk equals
   `git ls-files -- $(tr -d '\r' < manifest)`; the four construction files above absent;
   `dtw --help` exit 0), and the ceiling ruling 39 stated: **the seal is of the filesystem,
   not the object store** — `git show HEAD:CONSTRUCTION-LEDGER.md` still answers. The
   file's header "Nine items" (stale against its own "The ten items" heading since round
   `CORE-ONLY-LAYER`) is corrected in passing; not a member, no channel.
3. **The half's Owner cell names `HD-66` and `HD-34`, never a plan.** Rider
   `onboarding-carries-construction` arm (a) is exactly an Owner cell pointing at
   construction-side material; citing `core-only.plan.md` ruling 39 as owner would add a
   fifth instance. `HD-66` owns the shape (submodule default, this is path ①), `HD-34` the
   discipline (per-checkout adaptation, instrument untouched, recorded in the caller's own
   log).
4. **`CONSTRUCTION-INDEX.md` gains row 9 and becomes machine-checkable.** Row 9: the
   manifest — what the table is measured by and what a core-only mount's sparse checkout
   reads. Row 3's *Where* cell is written as five full paths (today it holds one path and
   four bare names), so that every product-tier *Where* token is a repo-relative path and
   the test below can parse the column. Header figures re-measured at the executor's tip
   by the commands the file prints; *How to re-measure* reads the manifest
   (`git ls-files -- $(tr -d '\r' < document-harness/product-tier.txt) | wc -l`).
5. **One test file binds the two copies and exercises the real consumer.**
   `tooling/tests/document_harness/test_product_tier_manifest.py`: (a) every manifest line
   matches at least one tracked file; (b) the manifest's set equals the set of *Where*
   tokens parsed from `CONSTRUCTION-INDEX.md`'s product-run table — the expectation comes
   from a different file than the one guarded (`E5`), and drift between the two copies is
   what turns red; (c) the manifest lists itself; (d) end to end: a `--no-checkout` clone of
   this repository into a temp dir, `sparse-checkout set --no-cone --stdin` from the
   manifest, checkout — the on-disk tracked set equals `git ls-files --` over the lines,
   and a **hand-written literal** list of four construction-side files is absent.
   Mutation (`E4`), each restored from sha256-checked scratch copies: drop a manifest line
   → (b) red; append `CONSTRUCTION-LEDGER.md` to the manifest → (d) red; misspell a row
   path in the manifest → (a) red; and a negative control that the unmodified pair is green.
6. **No `dtw` subcommand.** A file plus two git commands is the whole mechanism; a command
   face change is a per-case user ruling (`HD-47`) and `E6` asks what decision changes if it
   is absent — none does. Open question 1 puts it to the user anyway.
7. **`E10` membership question, recorded as `E10` asks of a round that creates a new file:**
   the manifest claims authority over no rule — it is a list the index's table defines and a
   test binds — so it is not a member and the membership sentence is not touched. The
   executor's commit body records the same.
8. **`E1`:** this session orchestrates (work side); the executor is a separate cold session;
   the reviewer is cold. The norm, no exception channel.

## Riders this round meets

| rider | what arrives | this round does |
|---|---|---|
| `figure-units` | its touch condition — the index's figure paragraph is rewritten | touch record, not redemption: its open sites (b)(c) are journal byte figures routed under `HD-23`, outside this boundary — the same form as its three prior touches |
| `onboarding-carries-construction` | `ONBOARDING.md` is edited; arm (b) was redeemed 2026-08-30, arm (a) is design (a clause on a rule to carry four decisions) and not authorized here | touch record on arm (a); decision 3 above keeps the new Owner cell out of its class |
| `protected-set-says-five` | its redeem-when names *the next round's pre-FULL window (any round)* — this round qualifies, bytes supplied in the row, class ruled `HD-63` by the user 2026-09-03 | open question 2: fold as its own commit (contract `:300` gains `bind_authorization_ref`; `:334-338` → six, two live write paths; `summary.py:202` and `test_run_v2_template_bind.py:1041` five → six; `E2` disclosure site by site; ninth entry in `CONTRACT-V4-SIGNATURE.md`; row deleted in that commit) or leave standing |
| `dispatch-exec-perms` · `e10-fifth-reader` · `caller-rule-read-no-generator` | surfaces this round does not touch | stand; their home is batch `EXECUTOR-LIFECYCLE` |

## Opening read — narrow form

At `05ae1b6`, `git rev-parse` over the seven `E10` members and this repository's declared
rule file against the blobs `v3-cold-read-c50362c.md` records (the last end-to-end read,
committed `13fde05`):

| member | blob at `05ae1b6` | since `c50362c` |
|---|---|---|
| `document-harness/RULES.md` | `a9cd92d` | **changed** (was `f4d5698`) — `R3` gained `UNRESOLVED_BLOCKER`, round 2 |
| `document-harness/README.md` | `f12d584` | **changed** (was `1ddb7e0`) — `:20` free-channel application |
| `document-harness/REVIEW.md` | `e6199bc` | **changed** (was `71707a3`) — verdict table, `:46,156` |
| `contract/Document-Work-Assurance-Contract-v4.md` | `7cba2ac` | **changed** (was `de21077`) — `:118`, `:127` under `HD-70` |
| `document-harness/EXECUTION.md` | `08fa87f` | same |
| `document-harness/ORCHESTRATION.md` | `3f9cd61` | same |
| `schema/document-assurance-v3/paragraph-map.schema.json` | `09aa869` | same |
| `document-harness/CONSTRUCTION-CHECKLIST.md` (declared rule) | `97ed956` | same |

So: the four changed members end to end — which discharges every deferral `PROMISE-PATH`'s
closeout named — and the other four covered by citing `v3-cold-read-c50362c.md`. The reader
derives this coverage itself; the dispatch carries no member table (`R2`).
`HARNESS-DECISIONS.md` `§live` in full — **eleven entries** at `05ae1b6`: `HD-69` · `HD-66` ·
`HD-65` · `HD-62` · `HD-59` · `HD-41` · `HD-36` · `HD-35` · `HD-34` · `HD-23` · `HD-9` —
inherited by this plan as they stand, not transcribed. `HD-70`'s flip from `implemented` to
`retired` follows this read and is the user's; the disposition commit carries it if ruled.

## Executor form

`HD-69` binds: **one cold `claude -p` session on `opus`, no web tools, from START to FULL**;
it stops at a decision point and the same session resumes; the orchestrator records the
session id in the round journal by hand (the command-face support is `EXECUTOR-LIFECYCLE`'s).
Live rulings shaping the work: `HD-59` (correct forward), `HD-41` (scope before assertion;
class-scan grep output in commit bodies), `HD-62`/`E2` (announced-surface disclosure — only
if question 2 folds the rider), `HD-34` (nothing here writes outside this repository).

## Change boundary

- **Adds:** `document-harness/product-tier.txt` ·
  `tooling/tests/document_harness/test_product_tier_manifest.py`.
- **Edits:** `document-harness/ONBOARDING.md` (item 1's second half; header count) ·
  `CONSTRUCTION-INDEX.md` (row 9; row 3's *Where*; header figures; *How to re-measure*) ·
  `HARNESS-RIDERS.md` (two touch records).
- **If question 2 folds `protected-set-says-five`, one more commit:**
  `contract/Document-Work-Assurance-Contract-v4.md` `:300`, `:334-338` (announced — `E2`
  disclosure in the body) · `CONTRACT-V4-SIGNATURE.md` (ninth post-signature entry) ·
  `tooling/rsclib/document_harness/summary.py:202` ·
  `tooling/tests/document_harness_review/test_run_v2_template_bind.py:1041` ·
  `HARNESS-RIDERS.md` (row deleted).
- **Not touched:** any `E10` member; `harness.json`; `tooling/hooks/`; `dtw`'s command face;
  anything in the caller.

## Acceptance — measured at the executor's tip, output pasted in the commit body

1. **The step works from the tree alone.** A fresh `--no-checkout` clone of the tip, the
   manifest read with `git show <tip>:document-harness/product-tier.txt`, `sparse-checkout
   set --no-cone --stdin`, checkout: tracked files on disk == `git ls-files --` over the
   manifest's lines; the four construction files absent; `python tooling/dtw.py --help`
   exit 0.
2. **The test binds.** Its assertions green at the tip; the three mutations each red and
   the control green, all pasted; battery = 956 + the new tests, none removed.
3. **The words are where a caller reads.** `grep -c 'product-tier.txt'` ≥ 1 in
   `document-harness/ONBOARDING.md` and in `CONSTRUCTION-INDEX.md`; `grep -c 'Nine items'
   document-harness/ONBOARDING.md` → 0.
4. **No member moved.** `git diff --stat 05ae1b6..<tip> -- <the seven E10 paths>` → empty.
   *Forward note, 2026-09-03 (step 2):* the disposition commit applied the read's L-2 bytes
   to `document-harness/REVIEW.md:129` by `E10`'s free channel, so over `05ae1b6..<tip>` that
   command returns exactly that one file and one line; the criterion is read as **no member
   moved by the executor's commits** — `git diff --stat <disposition commit>..<tip>` over the
   seven paths → empty — and the FULL meets the `REVIEW.md` change declared, not discovered.
5. **The index is true at its own tip**: header figures re-measured by the commands it
   prints; row 3's five tokens and row 9 present; the test's parse of the table equals the
   manifest.
6. `tooling/hooks/layer_path_check.py` and `tooling/ledger_cap_check.py` exit 0.

## Open questions — put at the `E11` card, ruled before the read is dispatched

1. **A `dtw` subcommand for the mount step?** Recommend **no** (`E6`, `HD-47`): a tracked
   file and two git commands; the command face stays at eight.
2. **Fold rider `protected-set-says-five`?** Recommend **fold, as its own commit** — its
   redeem-when names this window, the bytes are in the row, the class is ruled, and its
   deadline is a product-run event outside this repository's control.
3. **Opening read in the narrow form above, not waived?** Recommend **yes** — the read
   carries `PROMISE-PATH`'s deferral debt.
4. **The merged batch's name, `EXECUTOR-LIFECYCLE`**, for the ledger's queue line —
   candidate isolation first (write target + promotion form), then `HD-69`'s resume and the
   narrow re-read subject, then the nine design riders as the packaging round.

## Steps

- [x] 1. **Open — the commit that checks this box (2026-09-03).** Round opened on the user's
  "ok" at the `E11` card, base `05ae1b6`; rulings 1–4 written above; journal
  `document-harness/journal/core-mount-2026-09-03.md` opened tracked; ledger entry for the
  batch carrying the queue ruling.
- [x] 2. **Read + disposition — DONE 2026-09-03.** Read dispatched at `73bfe1e` (`python
  tooling/construction_dispatch.py --read 73bfe1e`), one cold `claude -p` on `opus` without
  web tools and with git restricted to read-only subcommands, session
  `1d4ccd50-4070-4b3f-a4a7-1718b4b7e75d`, 49 turns, 903 s; record `v3-cold-read-73bfe1e.md`
  committed unchanged at `d0d029a`, marker deleted in that act. **0 must-fix, 2 low, 2
  observation**; all eight files read end to end (the narrow form was available and not
  used); all three `PROMISE-PATH` deferrals discharged (§3); battery 956 by the reader.
  Disposition (user "1 入 bank 2 用 3 记录 4 转"): **L-1 banked** as rider
  `verify-specgap-precedence` (design; deadline the first product-run VERIFY recording
  `instruction_completeness: INCOMPLETE` with a blocker standing); **L-2 applied** to
  `REVIEW.md:129` by `E10`'s free channel with the record's bytes — adds no clause, changes
  no requirement, no round relied on the cell; its read rides the next layer read; rider
  `wl-route`'s deadline event a third time, row stands; **O-1, O-2 stay in the record**, no
  rows (O-2 is `R5`'s question, put and answered "record"); **`HD-70` → `retired`** in the
  disposition commit (carrier: the read record `d0d029a`). No amendment/re-read pair owed:
  nothing above low. **Acceptance 4 is read accordingly** — see its forward note.
- [x] 3. **Executor — DONE 2026-09-03.** One cold `claude -p` on `opus` without web tools,
  session `b2720689-5f0a-44d4-b1f4-668d7b018348`, 105 turns, 1816 s; **no decision-point
  stop** (`HD-69`'s form held but was not exercised — nothing outran the plan's rulings).
  Two commits inside the boundary: `4d2bf42` (`V3-CORE-MOUNT-MANIFEST-AND-STEP-v1` — manifest,
  test, ONBOARDING 1b, INDEX row 9, the two rider touch records) and `4020efa`
  (`V3-CORE-MOUNT-PROTECTED-SET-SIX-v1` — ruling 2's own commit: contract `:300`/`:335-340`,
  `CONTRACT-V4-SIGNATURE.md` ninth entry, `summary.py:202`, `test_run_v2_template_bind.py:1041`,
  row deleted). Acceptance measured at `4020efa` and pasted in the commit bodies: the probe
  clone materialized 61 == `git ls-files --` 61, the four construction files absent,
  `dtw --help` exit 0; the manifest test 5 passed with all four mutations (three the plan
  named plus a fourth on a *Where* token) red and the control green; battery 961 (956 + 5);
  both guards exit 0; `announced_path_disclosure --before 8ecc7a5 --after HEAD` exit 0.
- [x] 4. **Pointer — the commit that checks this box.** Steps 3–4 checked; journal appended
  with the executor dispatch, its session id, the two commits and the boundary note;
  `git diff --stat 05ae1b6..4020efa` over the seven members pasted into the journal — two
  member changes, both declared (`REVIEW.md:129` by the disposition `8ecc7a5`, the contract
  by the authorised `4020efa`), which is what the FULL reviews.
- [ ] 5. **FULL → (fix → VERIFY) → closeout** — `--range 05ae1b6..<tip>`, record committed
  unchanged; lows' spend-or-bank put to the user (`R10`); closeout moves the ledger pointer
  to `EXECUTOR-LIFECYCLE`, touch records land, `HD-66` stays live (this round is path ①
  made repeatable, not a judgment that ① suffices).

## Rulings — 2026-09-03, taken at the `E11` card

The user's word against the card's four numbered questions: **"ok"** — every recommendation
as put.

1. **No `dtw` subcommand.** The mount step is a tracked file plus two git commands; the
   command face stays at eight (`E6`, `HD-47`).
2. **Rider `protected-set-says-five` is folded, as its own commit.** The executor writes the
   row's bytes at its four sites under `HD-63` — the two contract sites with `E2` disclosure
   site by site in the body and a ninth post-signature entry in `CONTRACT-V4-SIGNATURE.md` —
   and deletes the row in that commit. Boundary grows by the five paths the *Change boundary*
   lists for it.
3. **The opening read is dispatched in the narrow form above and not waived.**
4. **The merged batch is `EXECUTOR-LIFECYCLE`**: candidate isolation first (the executor's
   write target and the promotion form), then `HD-69`'s same-session resume and the narrow
   re-read subject, then the nine design riders as the packaging round. The ledger's queue
   line carries the name; its plan is written when it opens.

## Resume pointer

**Round `CORE-MOUNT` OPEN 2026-09-03** at base `05ae1b6`. Next: step 2, the opening read, once
the four questions above are ruled and the opening commit has landed.

## Out of scope

- The distribution form — `HD-66`'s plugin question and its path ③ (a `git archive` artifact).
- Any `E10` member, `harness.json`, the `dtw` command face.
- Applying the step in the caller — the caller runs it in its own checkout and records the
  adaptation in its own decision log (`HD-34`).
- Candidate isolation and dispatch-economy — batch `EXECUTOR-LIFECYCLE`, next in the queue.
