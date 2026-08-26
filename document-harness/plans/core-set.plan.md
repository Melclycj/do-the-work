# Plan — batch `CORE-SET`: take the instrument's own construction history off a product run's dependency surface

> **Status: round 1 CLOSED 2026-08-26; round 2 OPEN 2026-08-26; round 3 remains.** Written 2026-08-25 at batch open, base `5425fa2`, branch `main`. **This file
> is the carrier of the twenty-two user rulings of 2026-08-25/26** below — eight taken before the
> batch opened and fourteen while it ran: until they landed here they lived
> only in the conversation that took them and in a session-side briefing outside the tracked
> tree, which is chat-only load-bearing material and a finding under `R2`. A cold session reads
> this file, then `CONSTRUCTION-LEDGER.md`'s current pointer, then works.
>
> **Round 2 `CORE-SET-SIGNATURE` is open.** Its opening cold read ran at **full weight** — all
> nine members end to end, 1,644 lines, nothing resting on `E10`'s citation clause — and is
> committed unchanged at `fc9c008`: **0 must-fix, 1 low, 3 observations**, no verdict, no budget
> spent. The `E11` card was rendered and approved, and rulings 20–22 came off it. The commits
> that carry *this file* are orchestrator bookkeeping, whose gate is the user ruling rather than
> a round; the candidate commits beside them are the cold executor's.

## Goal (one line)

A repository that mounts this instrument must be able to carry the core set alone — no
construction journal, no plans, no review records, no decision log, no rider bank, no
construction ledger — and open, run and close a product round without any of them.

## The eight user rulings of 2026-08-25 (this file is their carrier)

1. **The `§live` reading obligation refers to the decision log of the repository the round runs
   in.** The harness's own `HARNESS-DECISIONS.md` is this instrument's internal file; a caller
   has its own, created by `dtw init`, and the layer may refer to it **directly by name**. The
   defect is the `../` prefix, not the name: written from inside the instruction-layer
   directory that prefix resolves to the instrument's own copy under the mount, never to the
   caller's.
2. **Onboarding no longer reads it at all.** `ONBOARDING.md`'s pre-start read obligation drops
   the decision log — it does not exist yet at that moment, since `dtw init` (its own item 3) is
   what creates it.
3. **The permission to move the decision log is revoked.** `ONBOARDING.md` item 3's "Move it if
   the caller wants it elsewhere" goes; the log is pinned to the repository root, the only place
   `init` writes and the only path every convention names.
4. **The C4 `O-1` sampling obligation is cut in two.** A product run's closeout writes its one
   comparison line and owes nothing else; reading the collected lines and taking the
   three-branch re-ruling is a construction round's work, not a product run's closeout.
5. **The contract v4 signature moves to a standalone signature file beside `contract/`**, out of
   `HARNESS-DECISIONS.md`.
6. **The v1 package-bound leg retires whole** — `REVIEW.md`'s pointer, the CLI's `--package`
   mode and `review.py`'s v1 half together. Distribution post-dates v3; no new caller can meet a
   package-bound run.
7. **`DEFAULT_REVIEW_RECORD_DIRS` is renamed**, and existing callers do a one-time migration.
8. **The 2026-08-24 ruling that closed §10.5 does not bind this batch** — it answered "submodule
   or plugin", not "what belongs in the mount". The user set it aside explicitly. Recorded here
   so a later reader does not read this batch as overturning that ruling.

## Measured starting state — this session, at `5425fa2` (`E3`: re-run before any claim)

`git ls-files | wc -l` → **384** tracked files; summed `stat -c%s` over them → **6,576,091 bytes
(6.27 MB)**. History buckets by `git ls-files <path> | wc -l`: `migration/` **199**, of which two
are the retired-contract stubs that are `E10` members and survive any strip, so **197** are
history; `document-harness/journal/` **34**; `document-harness/plans/` **24**.

**The mechanical layer is already history-free** — inherited from the batch briefing's
end-to-end measurement (a `git archive HEAD` tree with every history path deleted ran
`dtw --help`, `dtw init` into a fresh repository, `candidate_path_check.py`,
`review_freeze_check.py` and a 9/9 member resolve, all green) and **not re-run by this
session**; step 6 re-runs it. What this session did re-run: the nine members resolve **9/9** at
`5425fa2` (`test -f` each).

**What breaks when history is stripped — and which instrument measures it.** This session first
wrote a scratch script for the question and reported 38 newly broken / 29 already broken, against
the briefing's 32 / 24 on a third tokenizer. **All three are superseded, and the scratch script is
withdrawn**: `tooling/sweep_refs.py` already answers exactly this question, is committed, and
imports `LAYER`, `PATHLIKE`, `RUNTIME_PREFIX` and `TOKEN` from `layer_path_check` rather than
hand-copying them — which is what `E5` asks of an expectation and what `E6` says about writing new
machinery for a thing the repository already has. **The round measures with `sweep_refs.py` and
nothing else.**

At `ff4b749` on the unstripped tree it reports **13 non-resolving references over the nine
members**, every one of them a NAMETOK — a backticked bare filename, which is the *compliant*
form for a caller-held artifact and not a defect. Zero broken markdown links, zero broken path
tokens. This matches the opening cold read's independent finding that the layer is clean at this
commit. The stripped-tree figure is step 6's, run with the same instrument on a `git archive` tree
with the history paths deleted; **no number from the withdrawn scripts is carried forward.**

**The load-bearing subset — every site naming one of the three registers**, from
`grep -n -o -E '(\.\./)?(HARNESS-DECISIONS|HARNESS-RIDERS|CONSTRUCTION-LEDGER(-archive)?)\.md'`:

- `ORCHESTRATION.md:51` — one markdown link into the mount (item A)
- `EXECUTION.md:283`, `:285` — the construction ledger named twice (item E)
- `CONSTRUCTION-CHECKLIST.md:151` — bare `HARNESS-DECISIONS.md`; `:206` — bare `HARNESS-RIDERS.md`
- `ONBOARDING.md:16` — prefixed (item B); `:98` bare, `:100` prefixed, `:106` bare rider bank (item C)
- `document-harness/README.md` — 9 sites (item D)
- contract v4 `:16` and `:341` — 2 sites, each counted twice by the tokenizer (round 2, item F)
- `REVIEW.md` — **0**

## How acceptance 1 is read (stated, because ruling 1 makes the literal reading wrong)

The briefing's acceptance 1 asks for **zero** references to the three registers from the
product-facing documents. Ruling 1 keeps the **bare name** and removes only the `../` prefix and
the link target, so a literal zero would contradict the ruling that authorises the change.
**The test is therefore: zero path-shaped references — no link target, no `../`-prefixed
token — from `ORCHESTRATION.md`, `EXECUTION.md`, `CONSTRUCTION-CHECKLIST.md` or `ONBOARDING.md`
into the three registers. Bare names survive by design**, and `CONSTRUCTION-CHECKLIST.md:151`
and `:206` are expected to still hold theirs when the round closes.

## The fourteen further rulings taken while the batch ran (2026-08-25/26)

These were taken after the eight above — six at the batch's opening, ruling 15 off the `E11`
card, rulings 16 and 17 on the candidate the executor returned, rulings 18 and 19 at round 1's
preclear, answering the observation both reviews reported and then turning its test on this
round's own output, and rulings 20–22 off round 2's `E11` card. This file is their carrier
on the same terms.

9. **The slicing is three rounds.** Round 1 `CORE-SET-LAYER` = items **A B C D E I J K L M** — prose,
   one file deletion and two new files, no frozen bytes and no code; it is what delivers the
   goal. Round 2 `CORE-SET-SIGNATURE` = items **F and N** — frozen bytes plus a signature re-siting, its
   own `E2` ruling and its own review; item N joined by ruling 18. Round 3 `CORE-SET-CODE` = items **G H** — code, a
   large test surface, and a migration with a silent failure mode. (Items I through M did not
   exist when the slicing was ruled; they are round 1's by the same test that put A–E there —
   no frozen bytes, no code.)
10. **Moving contract v4's signature preserves it; v4 is not re-signed.** The signature object
    is the blob `614932de…`, and those bytes do not change when the carrier does. Precedent
    carries it: this contract family's signature has lived in four carriers already, none of
    which re-signed on the move. What the round must get right instead is `HD-56`'s transition
    to `superseded` with both directions of the pointer written in the same commit as the new
    carrier — the decision-log invariant is the only thing keeping the signature traceable.
11. **The core set is defined by an explicit list, and it has two tiers.** Not by directory,
    which measurement rules out. **The product-run tier does not include
    `CONSTRUCTION-CHECKLIST.md` or the two retired-contract stubs** — those are construction-side
    and a product run is not governed by them (the checklist says so in its own header). So the
    core set is *not* the `E10` member set: `E10` membership governs the amendment machinery,
    not what a caller has to carry. The list's exact membership is authored at round open and
    shown on the `E11` card before it is written.
12. **The test for a citation into construction history is who cites, not what is cited.** A
    construction-side document may depend on construction history; a product-facing one may not.
    Applied to the eleven member sites that cite `plans/` `journal/` `history/`:
    `CONSTRUCTION-CHECKLIST.md:6` and the two retired-contract stubs at `:3` — three sites —
    **are allowed and are not touched**; `EXECUTION.md:399` and `document-harness/README.md:37`
    are product-facing and are fixed in round 1; contract v4 `:32` is product-facing but
    `E2`-frozen, so it defers to round 2; the four README table sites are item D's already and
    `REVIEW.md:92` is ruling 13's.
13. **`document-harness/history/` is removed now, and the dangling link is accepted.** Its one
    file, the v1 package-flow document, no longer waits for item G. `REVIEW.md:92`'s markdown
    link is left pointing at nothing **by explicit ruling**, and the round records it rather
    than repairing it. Disclosed cost, measured: `layer_path_check` scans only the lines a
    staged diff **adds**, so deleting the target fires no guard and prints nothing — the dangling
    link is silent until a human cold read meets it.

14. **Of the three riders whose touch condition round 1 reaches, only `waiver-live` is
    redeemed.** `charter-qualifiers` and `e1-table` stay with the dispatch-economy batch and
    take a touch note.

15. **`io-design.md` stays construction-side, and round 1 re-points `ONBOARDING.md`'s Owner cells
    away from it** (item L). It is a construction round's deliverable — its own header says
    "批 B R2 交付物" and that it is not a member and has authority over nothing — so a caller
    should not have to carry it. Today six to seven of `ONBOARDING.md`'s Owner cells point at it,
    which makes the ownership chain for those items end in a document that disclaims ownership.
    **Bound, and it is the executor's hard limit**: re-point only the cells whose decision
    already has a home elsewhere; where a decision lives nowhere but `io-design.md`, **do not
    invent an owner** — inventing one adds a clause to a rule, which is design beyond the
    approved card. Those cells are reported and banked instead. Measured at `ff4b749`, the ones
    with no other home look like: item 4's empty-instance shape, item 5's *deliberately not
    pre-created*, item 6's *the harness provides no template*, and the §5 carrier decision behind
    the standalone policy file. The executor re-derives that split rather than trusting this list.

16. **The members' citations into `migration/`'s node records are collected in round 1** (item M).
    Ruling 12 named `plans/` `journal/` `history/` and its enumeration missed a class its own test
    already covers: `migration/`'s N0, W2 and supersession-2 records are administrative and review
    records, which is the half of this batch's goal sentence reading *no review records*, and
    `EXECUTION.md:110` and `REVIEW.md:90` are product-facing documents citing them. Five sites in
    three members — `document-harness/README.md:16` ×3, `EXECUTION.md:110`, `REVIEW.md:90`; the
    contract's four are round 2's, being frozen. Taken now rather than after the FULL because
    `E9`'s own test — has a valid independent FULL already occurred? — answers no, making this a
    **pre-submission correction that consumes no budget leg and owes no VERIFY**.
17. **`HD-6`'s archive question is answered: do not clear.** The decision-log archive stands at
    309 lines against the 100-line ask-the-user threshold, and item E's supersession of `HD-54`
    moved another entry in. Deletion needs `HD-6`'s two conditions together — never cited again
    **and** recoverable from a record — with the default being not to delete, and a `superseded`
    chain may never be deleted at all, which is exactly where `HD-54` now sits. Recorded also
    because this is the fourth time the threshold fired and **the first time the question actually
    reached the user**: the previous three were sessions noting *no answer received* to themselves.

18. **The two root files this round created are one file, and they merge in round 2** (item N);
    **the two `ONBOARDING.md` riders are one row, and they merged immediately.** The observation
    both the FULL (`O-1`) and the VERIFY (`O-3`) reported — successive rounds closing findings by
    adding a component — was put to the user at preclear, and this is the user's answer to it, in
    the only form that answers it: not a rule about adding, but two specific additions undone.
    The rider merge landed at once because it is one row of prose. The file merge waits for round
    2 because `CORE-SET.md` and `CONSTRUCTION-INDEX.md` were both just reviewed by a FULL and a
    VERIFY, and re-opening a settled surface inside a closed round is worse than scheduling it.
    **What made them two in the first place is worth keeping**: items D and K were drafted as
    separate work items and executed as separate commits, and nothing between them asked whether
    their outputs were the same object. The measured overlap: `CORE-SET.md`'s construction tier
    and `CONSTRUCTION-INDEX.md` partition the same material — plans and journals in both, the
    three registers in both, the migration records as one row in one and four in the other — and
    `CORE-SET.md:61` carries a row whose whole content is a pointer to the other file, noting it
    was "created alongside this file".

19. **Item N's scope widens from a structural merge to a reduction, because the consumer test was
    applied to `CORE-SET.md` itself and it failed.** Asked who reads it, the answer measured to
    nobody: zero machine references, no route to it from `ONBOARDING.md`, and every citation
    either its sibling file, a finding about its own defects, or itself. The list was written for
    an operation this batch put out of scope. So the merge also returns it to inventory form and
    sends its argumentation to this plan, where the reasoning already lives. **This is the same
    test the ledger's new admission rule states**, applied for once to a file this round created
    rather than to a finding it received — a thing with no reader and no moment when anyone would
    read it accumulates instead of resolving, whatever its subject.

20. **`document-harness/README.md:16` joins round 2's scope** — the `L-1` the opening cold read
    routed to the user under `R5`. That sentence says the v4 signature state is `HD-56` and lives
    in the decision log; it is **true at round 2's base** and goes false the moment round 2's
    signature commit lands, since that commit moves the signature to a new carrier and flips
    `HD-56` to `superseded`. Round 2's items reached it through none of their site lists — item F's
    is contract v4 only, `HD-60`'s is narrower still, and item N touches no member — so a residual
    round 1 disclosed and assigned to *this* round was assigned to a scope that did not contain it.
    The other route the reader named (defer with a deadline a later round outlives) was not taken.
    **The bank was never an option**: the deadline falls inside round 2 itself, which `R10` calls
    malformed. **The executor writes the replacement bytes** — the reader deliberately supplied
    none, because the sentence must name the new carrier and that file does not exist yet, so
    writing its name at read time would have put a non-resolving path token in a member.
21. **The `E2` write authorisation widens to the five citation sites, and round 2 writes the
    contract once.** Recorded as **`HD-61`**, a standalone one-shot entry beside `HD-60` rather
    than a supersession of it: the two authorise different objects — signature re-siting versus
    citation demotion — so `HD-60` is neither narrowed nor overturned, and `HD-30`'s successor
    machinery does not fall due. This closes the collision between this plan and `HD-60` that the
    orchestrator's opening measurement and the cold read found independently: round 1 routed **8**
    residuals here (7 in contract v4, 1 in `README.md:16`), item F carried in `:32` and item M
    carried in the contract's four `migration/` citations, while `HD-60` authorised 「站点三处」.
    Under `HD-61` all eight close in round 2. The reason for one write rather than two is `E10`'s
    own sentence about a channel narrowed to the reported instance leaving its siblings to be
    found one re-read at a time; two rounds writing the same class of bytes into the same frozen
    file is two write windows on one frozen surface.
22. **The merged file of item N keeps the name `CONSTRUCTION-INDEX.md`.** Ruling 19 already put
    the material on the construction side, so the surviving name should say so. Measured cost of
    each direction, which is what decided it: keeping `CONSTRUCTION-INDEX.md` re-points three
    rider rows whose 量程 anchors name `CORE-SET.md` (`checklist-cited-not-carried` ·
    `figure-units` · `onboarding-carries-construction`) and touches **no member bytes**; keeping
    `CORE-SET.md` would instead edit `document-harness/README.md:24`, a product-tier member.

Ruling 14 is recorded at length because the touch condition genuinely arrives in round 1 and the
choice not to redeem is a deviation a reviewer will otherwise flag: item A edits
`ORCHESTRATION.md`'s nine-obligation table and `E10`'s `§live` clause, which are those two rows'
recorded redeem-when surfaces, and round 1 is round-eligible. The reason for deferring is the
ruling of 2026-08-25 that the nine design rows are settled by dispatch-economy in one pass.
(`e1-reader` names the *three-roles* table, a different surface; it does not fall due at all.)

## Constraints

- **`E2` frozen bytes** = contract v4 (`dfc983d2…`, corrected under `HD-57`; the signed blob
  `614932de…` stays the object `HD-56` binds) plus the fifteen files of
  `schema/document-assurance-v3/`. Item F touches the contract → **needs a recorded user ruling
  before any byte is written**. Item G must **not** touch
  `schema/document-assurance-v3/review.schema.json`, which holds both ReviewPackage and
  ReviewResult and is frozen; that retirement is code and prose only.
- **`E10` design test.** Items A–E change what a rule requires *inside a caller* even where this
  repository sees no change → design, opens a round; the free channel does not apply.
- **`E10-sync` does NOT fall due.** No item touches the membership sentence. The three-site
  checklist is not applied, and the commit body says so, so the next reader does not wonder.
- **`HD-55` role form**: orchestrator, executor and reviewer are three sessions; dispatch cold
  via `dtw dispatch`, and the orchestrator hand-edits no work product.
- **`HD-34` caller discipline** is untouched: nothing here lets a caller modify instrument
  content.
- **`E10` already contains the rule items A–C enforce** — "a caller-held path is *named, never
  written as a path token* … an artifact living only in a caller is given its name and its
  holder instead". This is alignment to a stated rule, not new design of one. Two places already
  say the intended thing: `document-harness/templates/decision-log.md` is titled "user rulings
  for **this repository's** use of the harness", and `ONBOARDING.md` item 3's Owner cell already
  calls the harness's own copy "a filled **example** of the same".
- **`layer_path_check.py:63` skips tokens without a `/`**, so a bare `HARNESS-DECISIONS.md`
  token is never scanned; the guard cannot see whether ruling 1 was honoured. The round's
  evidence is the grep above, not the guard.

## Out of scope

- OUT: changing the distribution mechanism. Submodule stays; packaging as a plugin is not this
  batch (ruling 8 sets the 2026-08-24 §10.5 ruling aside rather than overturning it).
- OUT: producing a stripped or published core-set artifact or branch. This batch removes the
  *dependency*; how the core set is shipped is a later question.
- OUT: deleting any history from this repository — **one explicit exception, ruling 13**:
  `document-harness/history/`'s single file goes in round 1 (item I). Everything else stays;
  only the product run's reliance on it goes.
- OUT: `schema/document-assurance-v3/` — frozen, and item G is defined to avoid it.
- OUT: reorganising `tooling/tests/` beyond what items G and H break.

## Work items

Sites are at `5425fa2`.

### A — the `§live` obligation stops pointing into the mount

- `ORCHESTRATION.md:51` — drop the link, leave the bare name.
- `README.md:27` — drop the link target into the mount, keep the obligation sentence, and point
  the mechanism at `templates/decision-log.md`, where the rules actually live (`HD-19`).
- `CONSTRUCTION-CHECKLIST.md:151` — **no path change**; it already reads the bare name. Add only
  what ruling 1 makes explicit: the file meant is the one in the repository the round runs in.
- Redeem rider `waiver-live` in the same commit (same clause), deleting its row there.

### B — onboarding drops the read

- `ONBOARDING.md:16` — remove the decision log from the "Read once before starting" sentence,
  leaving the instrument's navigation surface.

### C — the decision log is pinned to the root

- `ONBOARDING.md` item 3 **Do** cell — remove "Move it if the caller wants it elsewhere; record
  that in the file itself"; state that the root is the only supported placement, and why: the
  layer refers to it by bare name and `init` writes only there. Keep the measured empty-log
  paragraph — it becomes the *reason* rather than a caveat.
- Item 4 (rider bank) says "Moving it carries item 3's cost unchanged" — make it consistent with
  whatever item 3 becomes.
- **Added by this session's measurement:** item 3's **Owner** cell carries a prefixed token into
  the mount at `:100`, a site the briefing's item C did not list. Either it goes the way of item
  A's or the round states the residual it leaves.

### D — `document-harness/README.md` splits

- Keep 10 rows: contract v4 · what else lives in `contract/` · the four schema rows · role
  instructions · construction-side rules · onboarding · local enforcement.
- Move 9 rows to a new tracked file at the repository root, beside the other construction
  registers: **`CONSTRUCTION-INDEX.md`** — v3 execution plan · N0 record · N1 record · N2 record
  · contract fixtures · journals · decision log · rider bank · construction ledger.
- Leave one row in `document-harness/README.md` pointing at it.
- **Not folded into `CONSTRUCTION-LEDGER.md`**: that file's header admits only two things
  (current pointer, construction rulings with no other home) and carries a 180-line bound.
- Row 27 is also item A's site → **A and D land in one commit**.

### E — the C4 `O-1` obligation is cut in two

- `EXECUTION.md:283-285` — a product run's closeout writes the one comparison line, full stop.
  Remove from the product-side charter the reach into the construction ledger's
  conversation-only line and the "next product run's closeout" reading moment.
- `CONSTRUCTION-LEDGER.md:110-114` conversation-only list — the three branches stay; the reading
  moment becomes a construction round's, not a product run's closeout.
- `HD-54` (`§implemented`, scope `one-shot`) states the reading moment as the next product run's
  closeout. Changing it needs a **successor entry carrying the narrowed text in full**, the
  original moved to `superseded`, both in the same commit as the carrier (decision-log
  invariant, `HD-30`).

### I — `document-harness/history/` is removed *(ruling 13)*

- Delete `document-harness/history/REVIEW-v1-package-flow.md`, the directory's only file. It no
  longer waits for item G's retirement of the v1 package leg.
- **`REVIEW.md:92`'s link is left dangling on purpose** and the round's commit body and journal
  say so, naming this ruling. Nothing is edited in `REVIEW.md` for it in round 1; item G retires
  the pointer in round 3.
- Measured cost, corrected by the executor's own run rather than left as this plan first wrote
  it. `layer_path_check` scans only the lines a staged diff adds, so the deletion fires no guard
  and prints nothing — that half held. But `sweep_refs.py` reads standing text and **does** see
  it, reporting `REVIEW.md:92` twice (LINK and PATHTOK) and moving the whole-tree count from 13
  to 15. The sweep always exits 0 and blocks nothing, so there is no consequence; the plan's
  original claim that the link was invisible to *every* machine was simply wrong, and the next
  reader of that count needs to know those two entries are ruled, not rot.
- This is the one exception to *Out of scope*'s "delete no history"; the user made it explicitly.

### J — the two product-facing citations into construction history *(ruling 12)*

- `EXECUTION.md:399` — cites `document-harness/journal/retro-2026-08-03.md` from the product-side
  executor charter. Demote to a bare name or the recorded commit id, the form `E10`'s
  caller-held-path clause already prescribes and which `CONSTRUCTION-CHECKLIST.md`'s header
  already uses for commit ids this repository does not hold.
- `document-harness/README.md:37` — the *Predecessors* sentence, outside the table and so not
  reached by item D's row move, cites `plans/general-harness-v2-architecture-revision.plan.md`.
  Same demotion.
- **Not touched, by ruling 12**: `CONSTRUCTION-CHECKLIST.md:6` and the two retired-contract stubs
  at `:3`. All three are construction-side, and a construction-side document may depend on
  construction history. The round states this rather than leaving a reader to wonder why three
  sites of the same shape were treated differently.
- Contract v4 `:32` is product-facing and would belong here, but its bytes are `E2`-frozen →
  round 2, listed under item F.

### K — the core set gets an explicit list *(ruling 11)*

- A new tracked file naming the core set outright, in **two tiers**: the product-run tier (what a
  caller must carry to open, run and close a round) and the construction-side tier (what only
  this repository's own rounds need). `CONSTRUCTION-CHECKLIST.md` and the two retired-contract
  stubs sit in the second tier, so **the list is deliberately not the `E10` member set** — `E10`
  governs the amendment machinery, not what travels.
- **`HD-21` falls due on this file and on item D's `CONSTRUCTION-INDEX.md` alike**: a file that
  appears later and claims authority over any rule here is not a member until the membership
  sentence names it, **and the round that creates one records the question and its answer**. The
  answer this round will record, for both: *not a member, claims authority over nothing* — an
  index and a manifest, the same shape `ONBOARDING.md` already occupies and states in its own
  header. Recording it is not optional; `HD-21` exists because the decision log itself once
  appeared with nobody asking.
- `E10-sync` still does not fall due: neither file touches the membership sentence.
- The list's exact membership is authored at round open and **shown on the `E11` card before it
  is written**, since it is the one item here whose content was ruled in shape but not in detail.

### L — `ONBOARDING.md`'s Owner cells stop ending at `io-design.md` *(ruling 15)*

- Ten citation lines at `ff4b749`, by `grep -n io-design document-harness/ONBOARDING.md`. Sort
  them into two piles before editing anything.
- **Re-point** every cell where `io-design.md` is named *alongside* an owner that already holds
  the decision — the header sentence and item 1 (both already name `HD-33` / `HD-34`), item 2
  (its own sentence says "`HD-33` rules the same"), item 3 (already names `HD-19` and `E10`'s
  tail; its See cell describes what `templates/decision-log.md`'s own header carries, which is
  the real holder), item 4's rules half (`R10`), item 8 (`ORCHESTRATION.md`). Dropping the
  redundant pointer changes no obligation.
- **Do not invent an owner** for a decision that lives nowhere else. That would add a clause to a
  rule — design, and beyond the card the user approved. Report those cells and bank them as one
  rider naming the surface. Expected members of that pile, to be re-derived rather than trusted:
  item 4's empty-instance shape · item 5's *deliberately not pre-created* · item 6's *the harness
  provides no template* · §5's carrier decision behind the standalone policy file.
- `EXECUTION.md`'s two citations are **not** in scope: they read `(`HD-35`, io-design §4)`, the
  decision-log id first and `io-design` as bare attribution, so no reader has to follow them.
- `io-design.md` itself is not edited, moved or deleted. It stays where it is, on the
  construction side of item K's list.

### M — the members stop citing `migration/`'s node records *(ruling 16)*

- Five sites, measured on the stripped tree at `eba47ad` with `sweep_refs.py`:
  `document-harness/README.md:16` (three LINKs — the N0 record, the W2 record, the
  supersession-2 signature record), `document-harness/EXECUTION.md:110` (the W2 record),
  `document-harness/REVIEW.md:90` (the W2 record).
- Same demotion as item J: the path form goes, the name and its holder stay. These records are
  this instrument's own construction record and a caller does not carry them.
- Contract v4's four sites of the same shape are **not** here — `E2`-frozen, so they ride round 2
  beside item F, and the round states them as its declared residual rather than implying none.
- This is a **pre-submission correction** under `E9`: no independent FULL has occurred on this
  round yet, so it consumes no budget leg and owes no targeted VERIFY. The commit body says so,
  because `E9` warns that every recorded escape from the cap was a renamed round.

### N — the two root files become one construction-side index, in inventory form *(round 2, rulings 18 and 19)*

**Measured before the scope was set, and it is the reason the scope changed.** `CORE-SET.md` has
**no consumer today**. No machine reads it — `git grep` over `tooling/`, `assurance/`, `.githooks/`
and `.github/` returns zero. `ONBOARDING.md`, the document a new caller actually walks, does not
mention it. Every reference to it is one of three things: the sibling file created in the same
commit, three rider rows recording its own defects, the round journal measuring it, and its own
line 62. The operation that would read such a list — building or shipping the core set — is
explicitly out of this batch's scope, so the list was written for a reader who does not exist yet.
And line 62 already settles which side it is on: *"it describes the split; it is not part of what
travels"*. A file a caller never receives cannot be for callers, so its only possible consumer is
this repository's own rounds — and what those read is the plan and the index.

- **Merge** `CORE-SET.md` into `CONSTRUCTION-INDEX.md`, **which is the name that survives**
  (ruling 22, taken off round 2's `E11` card). One file, construction side, two tiers plus the
  index rows. **The pointer surface that follows from that choice**: `CONSTRUCTION-INDEX.md:27`
  and `CORE-SET.md:61`–`:62` dissolve into the merge; `document-harness/README.md:24` already
  names `CONSTRUCTION-INDEX.md` and needs no edit — which is the point, since it is a
  product-tier member; and **three rider rows re-point**, their 量程 anchors naming `CORE-SET.md`
  today (`checklist-cited-not-carried` · `figure-units` · `onboarding-carries-construction`).
  Re-derive that list before editing rather than trusting it.
- **Reduce both tiers to inventory**: which files, and where. The *why* column goes or collapses
  to a clause — measured at **62% of the table's characters** today, 2,418 against 1,460 of actual
  locating information.
- **The two prose blocks move to this plan**: *Why an explicit list* (directory is not the
  boundary) and *What it is not*. This plan already carries the first — ruling 11 and the
  measurement under *Open questions* say it — so keeping a second copy is the drift the ledger
  header names.
- **`HD-21`'s question and answer stay**, in the surviving file: whether it is an
  instruction-layer member, and that it is not. That sentence is mandated, not optional.
- **Size is the check, not the intent**: `CORE-SET.md` is 82 lines / 7,646 characters today, of
  which 47 lines / 3,413 characters are prose around an 18-row list. The merged file should land
  well under 2,000 characters of its own prose; state the measurement rather than the aim.
- **Still not a licence to re-open what round 1 settled.** Tier membership, the bounded
  sufficiency claim and its stated gap carry over as written. A row whose *content* is wrong is a
  separate finding, not this item.

### F — contract v4's signature moves out of the decision log *(round 2)*

- New file beside the contract, shaped like the retired supersession-2 signature record.
- `contract/Document-Work-Assurance-Contract-v4.md` — the frontmatter `signature_owner:` field
  and the signature-semantics block both name the decision log today; both repoint.
- **The machine does not constrain the carrier**: `checks.py:489` rejects only a document
  carrying its *own* approval status; `_owner`-suffixed fields are whitelisted as the correct
  delegating form and nothing ever opens the delegate. Precedent: this contract family's
  signature has lived in four carriers — the N0 record §8 (v3) · the W2 record (s1) · the
  supersession-2 signature record (s2) · `HD-56` (v4).
- **The five citation demotions ride the same write (ruling 21, `HD-61`).** Contract v4 `:32`
  cites `document-harness/plans/contract-v4.plan.md` (carried in from item J by ruling 12), and
  `:25` `:27` `:30` `:253` cite this repository's N0 record, W2 record and supersession-2
  signature record (item M's shape, deferred here because the bytes are `E2`-frozen). Same
  demotion as items J and M: the path form goes, the name and its holder stay. **Site numbers
  here are this plan's measurement and not the authority** — the executor re-derives them before
  writing, as `HD-61` says in as many words.
- **`document-harness/README.md:16` lands in the signature commit (ruling 20).** It says the v4
  signature state is `HD-56` and lives in the decision log — true until this round's signature
  commit, false the instant after it, and reached by no other item's site list. It must therefore
  ride the *same* commit as the signature move, not a later one: any gap is a window in which the
  layer's navigation surface points at a superseded entry. The bytes are the executor's to write,
  because the replacement has to name the new carrier and the reader could not name a file that
  did not yet exist.
- **`CONSTRUCTION-CHECKLIST.md:56` is reached by adjacency, not by scope** — `HD-60` obligation ①
  forces this round to update `E2`'s v4 blob literal two lines above it, so the executor is
  editing that clause with `:56` in view. It says "the signed blob remains the signature object
  `HD-56` binds", which stays true under ruling 10; check it rather than assume it, and say so.
- **`HD-56`'s state transition is this round's real risk, not the new file.** Ruling 10 settles
  that the move preserves the signature; what it does not do is write the pointers. `HD-56` goes
  to `superseded` with a successor carrying the signature in full, both directions of the
  pointer, in the same commit as the new carrier — `HD-30`'s invariant. Get that wrong and the
  signature is traceable through nothing.
- **The `E2` authorisations exist and are two**: `HD-60` (signature re-siting, three sites) and
  `HD-61` (the five citation demotions). Both are one-shot and both are consumed by this round's
  contract write. `HD-60`'s obligation ① — update `E2`'s own v4 blob literal in the same commit —
  covers both sets of bytes and is discharged once if they land together.

### G — the v1 package-bound leg retires *(round 3)*

- `REVIEW.md:92` pointer. **The document it pointed at is already gone** — item I deleted it in
  round 1 under ruling 13, leaving this link deliberately dangling; retiring the pointer here is
  what closes it.
- `tooling/rsclib/document_harness/cli.py` — the `--package` option (`:662`) and
  `_cmd_v3_review`'s v1 branch (`:452` onward); `review` keeps its `--subject` mode.
- `tooling/rsclib/document_harness/review.py` — the package half: `member` · `freeze_package` ·
  `package_digest` · `members_by_role` · `check_package` · `verify_member_bytes` ·
  `load_package`. Decide per function whether the v2 path still calls it before deleting;
  `review_result_v2.py` is the v2 side.
- Tests: the package-and-review suite under `tooling/tests/document_harness_review/`, plus the
  v2-subject CLI suite and the fix-round-locks suite, which also reference the package.
- **Do not touch `schema/document-assurance-v3/review.schema.json`** — `E2`-frozen.
- Removing a CLI *option* has the shape `HD-47` rules per-case for a command; ruling 6 covers it.

### H — `DEFAULT_REVIEW_RECORD_DIRS` is renamed *(round 3)*

- `tooling/rsclib/document_harness/caller.py:50` — the old migration directory default becomes
  `("assurance/review-records/",)`, matching the shape of `DEFAULT_SPECIFICATION_SURFACE`.
- **Migration hazard, and it is silent.** `dtw init` writes the defaults into
  `.harness/scan-surfaces.json`, and `.harness/` is gitignored. An existing caller keeps working
  where the declaration already exists (`init` refuses to overwrite), but **any fresh clone
  loses the declaration**, and a re-run `init` writes the new default — at which point that
  repository's existing records stop being recognised, with nothing to say so. Ruling 7 accepts
  a one-time migration; the round states what it is — at minimum the known caller's declaration
  written explicitly and the advice recorded in its policy file.
- Prose sites naming the old directory need the same pass: `caller.py` docstrings, `REVIEW.md`'s
  record channel, and `ONBOARDING.md` where it appears.

## Steps

- [x] 1. Carry the eight rulings out of session-side material into committed state: this tracked
  plan plus a `CONSTRUCTION-LEDGER.md` current-pointer entry (batch name, queue position against
  the dispatch-economy batch). Until this is done the rulings are unreachable by any reviewer.
- [x] 2. **DONE.** Put the open questions to the user and record the answers here — rulings 9–14
  above, taken 2026-08-25/26. Nothing is now waiting on the user before the round opens.
- [x] 3. **DONE.** Round 1 is open under `HD-55`. The opening cold read ran as its own `claude -p`
  session, narrow form by user ruling — two members genuinely owed, seven citable, the reader
  correcting the dispatch's own arithmetic (`O-1`) — and its record is committed unchanged at
  `9f1de08`: **0 must-fix, 1 low, 3 observations**, no verdict, no budget spent. The low's bytes
  were applied through `E10`'s free channel in their own commit at `0420d99` per `HD-38`, closing
  the class rather than reducing it, so no rider was re-banked. The `E11` card was rendered
  carrying item K's two-tier list and approved; ruling 15 came off it.
- [x] 4. **DONE.** Landed as `c0b9316` (A+D) · `c39536b` (B+C) · `4f4dc4b` (E, with `HD-54`
  superseded and successor `HD-58` in the same commit) · `60d668f` (I+J) · `806efca` (K) ·
  `eba47ad` (L) · `c5f00f6` (M, pre-submission correction). Original text: execute items A+D in one commit; B+C in one commit; E in one commit with the `HD-54`
  successor entry in the same commit as its carrier; I+J in one commit; K in one commit with the
  `HD-21` question and answer recorded in its body; L in one commit; M in one commit, its body
  naming itself a pre-submission correction under `E9`.
- [x] 5. **DONE.** `waiver-live` deleted in `c0b9316`; bank stays at 16 rows, the new
  `onboarding-io-design-owners` row replacing it. Original text: redeem rider `waiver-live` in the item-A commit, deleting its row in that same commit.
  `charter-qualifiers` and `e1-table` take a touch note only and stay with dispatch-economy
  (ruling 14); the note goes in the same commit that touches their surface.
- [x] 6a. **DONE — the reference count only.** The reference count was re-run by the
  orchestrator with `sweep_refs.py` on `git archive` trees at `cc3b3ab` and `c5f00f6`: **31 → 13**
  real breaks over the nine members, `ONBOARDING.md` separately **2 → 0** by grep since the sweep
  does not scan non-members, every residual accounted. Recorded in
  `document-harness/journal/core-set-layer-2026-08-26.md`. **Not re-run**: the briefing's
  end-to-end mechanical check on a *stripped* tree; `dtw init` was exercised on the full tree
  only. Named as an honesty cap rather than implied — and carried below as its own open step,
  because a checkbox that reads done is how an honesty cap quietly stops being one.
- [x] 6b. **DONE 2026-08-26, and the honesty cap narrows rather than closes.** Run by the
  orchestrator at `d3ba221`, on a `git archive` tree with the history paths deleted — **120 files
  / 1,676,428 bytes (1.60 MiB)**, the file count reproducing the briefing's 120 exactly, so the
  strip is repeatable. All five checks green: `E10` members resolve **9/9**; `dtw --help` exit 0,
  eight commands; `dtw init --repo-root <fresh repo>` exit 0, "5 created, 0 left as found", and
  the decision log resolves to exactly one file there (this is also round 1's acceptance 5, on a
  stripped tree rather than the full one); `candidate_path_check.py` exit 0;
  `review_freeze_check.py` exit 0. `layer_path_check.py` was run beside them, also exit 0.
  **The guards were proved to engage rather than to pass vacuously** (`R8`'s shape, applied to
  the orchestrator's own evidence): the stripped tree was made a git repo, a member line naming
  a deleted journal path was staged, and `layer_path_check` blocked with exit 1 and named the
  token; reverted at once. Beyond the five: `dtw dispatch --construction-executor` exit 0 on the
  stripped tree, deriving the checklist as charter, and `assurance/templates/run-v2/` complete.
  **What is still not proved, stated rather than implied**: no product round ran end to end — no
  run directory built, no `instruction.md` frozen, no `preview` / `review` / `disposition`
  against a real run, no reviewer dispatched from a mounted stripped tree. That is a product run,
  which this batch puts out of scope. So what the cap now covers is the **product-run** leg
  alone; the mount-and-open leg is measured. Unchanged by this run: `CORE-SET.md`'s own measured
  gap — the product tier's five documents carry pointers and rule citations into the construction
  checklist, which does not travel — banked as rider `checklist-cited-not-carried`.
  Original text: re-run the briefing's end-to-end mechanical check on a *stripped* tree:
  `dtw --help`, `dtw init` into a fresh repository, `candidate_path_check.py`,
  `review_freeze_check.py`, and the member resolve. Until this runs, what is proven is that a
  stripped tree's references resolve — **not** that a caller can mount it and run a round.
- [x] 7. **DONE — round 1 CLOSED.** FULL `92cc514` → `CHANGES_REQUIRED` (2 blockers, 8 lows,
  3 observations) → one user-approved fix `0482a40` → VERIFY `0f0498f` → `REVIEWED_NO_BLOCKER`
  (4 findings, 3 observations). All three records committed unchanged. **The fix leg was consumed
  twice, and the closeout says so rather than renaming it**: the withdrawal in `0f0498f` rewrote
  this round's journal §6 *conclusion*, which `HD-23` does not route (its parenthesis excludes
  conclusions) and which was reviewed work product inside the FULL's range. User ruling
  2026-08-26 on the VERIFY's `V-4`. `E9`'s own sentence is why it is written down: every recorded
  escape from the cap was a renamed round.
- [x] 8. **DONE for round 2; round 3 still to open.** Round 2 `CORE-SET-SIGNATURE` is open under
  `HD-55`: the opening cold read ran at full weight in its own `claude -p` session and is
  committed unchanged at `fc9c008` (**0 must-fix, 1 low, 3 observations**, no verdict, no budget
  spent), the `E11` card was rendered and approved, and rulings 20–22 came off it. No separate
  plan file: round 2's shape is unchanged from the slicing of ruling 9 except for the two scope
  widenings the card took, and both are recorded above rather than in a second file. Original
  text: open rounds 2 and 3 per the ruling from step 2, each with its own plan file if their
  shape has changed by then.
- [ ] 9. Execute round 2. Dispatch a cold executor via `dtw dispatch --construction-executor`;
  **item F in one commit** — the new signature carrier, the contract write (three signature sites
  under `HD-60` plus five citation demotions under `HD-61`), `E2`'s v4 blob literal,
  `document-harness/README.md:16` per ruling 20, and `HD-56` → `superseded` with its successor
  carrying the signature in full and both directions of the pointer — and **item N in one
  commit**. The orchestrator hand-edits no work product (`HD-55`).
- [ ] 10. Dispatch the FULL over the round's range, walk the `E9` budget, land the record
  unchanged, close round 2.
- [ ] 11. Open round 3 `CORE-SET-CODE` (items G and H).

## Acceptance — round 1

Each shown by its command, not by a sentence.

1. On a tree with every history path removed, **zero path-shaped references** (link target or
   `../`-prefixed token — see *How acceptance 1 is read*) from `ORCHESTRATION.md`,
   `EXECUTION.md`, `CONSTRUCTION-CHECKLIST.md` or `ONBOARDING.md` into the decision log, the
   rider bank or the construction ledger. Residual pure-citation breaks in `REVIEW.md` and
   contract v4 belong to rounds 2 and 3; the round **states the count it leaves** rather than
   implying none.
2. `document-harness/README.md`'s table holds 10 rows; `CONSTRUCTION-INDEX.md` exists at the
   root and holds the other 9; the README-owned breaks measured above are gone.
2b. On that same stripped tree, of the eleven member sites citing `plans/` `journal/` `history/`,
   exactly **three remain** — `CONSTRUCTION-CHECKLIST.md:6` and the two retired-contract stubs at
   `:3` — and they remain **by ruling 12**, not by omission. `EXECUTION.md:399` and
   `document-harness/README.md:37` are gone; contract v4 `:32` is the one deferral and the round
   names it. `document-harness/history/` no longer exists, and `REVIEW.md:92`'s link is
   dangling **by ruling 13** with the commit body saying so.
2c. The core-set list exists, carries both tiers, and its commit body records the `HD-21`
   question and answer — for it and for `CONSTRUCTION-INDEX.md`. The product tier measures 59
   files / 0.73 MB against the repository's 386 at `ff4b749`, `io-design.md` **not** among them
   (ruling 15); re-measure rather than cite.
2d. `grep -n io-design document-harness/ONBOARDING.md` returns only cells whose decision has no
   other home, each of them named in the round's banked rider; every cell that had a real owner
   beside `io-design.md` now names that owner alone. `io-design.md`'s own bytes are unchanged.
3. `python -m pytest -q` green — report the run, not a remembered figure.
4. `layer_path_check.py`, `candidate_path_check.py` and `review_freeze_check.py` each exit 0 on
   the staged tree, and the `E10` members resolve 9/9.
5. `dtw init` into a fresh repository still exits 0, and in that repository the decision log
   resolves to exactly one file.
6. Rider `waiver-live`'s row is gone from `HARNESS-RIDERS.md`, in the same commit as its carrier.
7. The round's FULL returned `REVIEWED_NO_BLOCKER`, or `CHANGES_REQUIRED` → one approved fix →
   VERIFY `REVIEWED_NO_BLOCKER`, with all three records committed unchanged.

## Acceptance — round 2

Each shown by its command, not by a sentence. Figures are measurements and go stale — re-run.

1. **The eight residuals round 1 routed here are closed, and the count is stated rather than
   implied.** On a stripped tree, `sweep_refs.py`'s `LINK` + `PATHTOK` count over the nine members
   drops by the seven contract sites; `document-harness/README.md:16` is the eighth and is not a
   sweep hit but a truth claim, checked by reading it. The residual that **remains by ruling**
   is `REVIEW.md:93` (two entries, one site), which item G retires in round 3.
2. **The signature is traceable through the new carrier alone.** The new file exists beside
   `contract/`; `HD-56` is `superseded` with both directions of the pointer written, and the
   successor carries the signature in full — the signed blob still `614932de…`, unchanged by the
   move (ruling 10). `git log -1` on that commit shows carrier, successor and pointer flip
   **together**, per `HD-30` / `HD-2`.
3. **`E2`'s v4 blob literal matches the contract's new blob**, in the same commit that wrote it
   (`HD-60` obligation ①): `git rev-parse HEAD:contract/Document-Work-Assurance-Contract-v4.md`
   equals the literal in `document-harness/CONSTRUCTION-CHECKLIST.md`.
4. **`document-harness/README.md:16` is true after the signature commit, not before it**, and it
   landed in that same commit (ruling 20). Read the line; it must name the new carrier and no
   superseded entry.
5. **One file at the root, not two.** `CORE-SET.md` is gone, `CONSTRUCTION-INDEX.md` carries both
   tiers plus the index rows, its own prose measures well under 2,000 characters, `HD-21`'s
   question and answer survive in it, and the three rider rows anchored on the old name re-point.
   `document-harness/README.md:24` needs no edit — verify that it did not get one.
6. `python -m pytest -q` green — report the run, not a remembered figure.
7. `layer_path_check.py`, `candidate_path_check.py` and `review_freeze_check.py` each exit 0 on
   the staged tree, and the `E10` members resolve 9/9.
8. The round's FULL returned `REVIEWED_NO_BLOCKER`, or `CHANGES_REQUIRED` → one approved fix →
   VERIFY `REVIEWED_NO_BLOCKER`, with all three records committed unchanged.

## Resume pointer

当前指针: step 9 — **round 2 `CORE-SET-SIGNATURE` is OPEN and nothing is waiting on the user.**
The opening cold read is discharged at full weight (`fc9c008`, 0 must-fix), the `E11` card is
approved, and rulings 20–22 are recorded above. Step 6b is closed (see step 6b); the ledger's
CLOSED-roll split is still open and blocks nothing.

**The next action is to dispatch a cold executor** — `dtw dispatch --construction-executor` —
with items F and N, this plan, and the two `E2` authorisations. **Both are one-shot and both are
consumed by the same contract write**: `HD-60` (signature re-siting, three sites, three riding
obligations in the *same* commit — update `E2`'s v4 blob literal, keep `HD-56` binding the signed
blob `614932de…`, land the new carrier with `HD-56`'s supersession pointers) and `HD-61` (the
five citation demotions). `HD-59` also binds the round: a committed conclusion is never rewritten
in place, only corrected forward. Round 3 `CORE-SET-CODE` (items G, H) follows.

## Notes

- A second name collision exists, and item H is only half of it: `dtw init` creates a decision
  log and a rider bank at a caller's root under the same names this repository uses at its own
  root. That half dissolves by construction once the core set excludes the instrument's own
  registers, which is what items A–C make legal. **Verify it (acceptance 5) rather than editing
  anything for it.**
- Figures here are measurements at `5425fa2`, scope `git ls-files`, and go stale. Re-run rather
  than cite.
