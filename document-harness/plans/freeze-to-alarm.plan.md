# Plan — batch `FREEZE-TO-ALARM`: the freeze stops blocking writes and starts announcing them

> **Status: round CLOSED and batch `FREEZE-TO-ALARM` CLOSED, 2026-08-28.** All nine steps done, all
> nine acceptance criteria met, `E9` budget walked in full — FULL `CHANGES_REQUIRED` → one approved
> fix leg → VERIFY `REVIEWED_NO_BLOCKER`. Written 2026-08-27 at batch scoping, base
> `51553bdcb4f341b8b87bec4c0207f9d049d25141`, branch `main`. **This file is the carrier of the six
> user rulings of 2026-08-27** below. Until they landed here they lived only in the conversation
> that took them and in a session-side briefing outside the tracked tree, which is chat-only
> load-bearing material and a finding under `R2`: a reviewer starts cold from one commit and
> derives the rest from the repository, so a ruling that never reaches a commit is a ruling the
> reviewer cannot check. That briefing is now **upstream and superseded by this file**; nothing
> further is derived from it.
>
> A cold session reads this file, then `CONSTRUCTION-LEDGER.md`'s current pointer, then works.
>
> **The four questions that blocked the round are answered** (user, 2026-08-27) and recorded inline
> in *Open questions* below. They bind the round exactly as the six rulings do.
>
> **This status block, and the Steps below, went stale for six work commits and the round's FULL
> made that a blocker (`v3-review-full-ad0663d.md`).** The stale text said no round was open and
> nothing had executed, which is what a cold session reads first — under `HD-55` a cold executor
> working from it would have redone item B or item A. Corrected forward here rather than quietly:
> the omission was the orchestrator's, the previous batch opened each round with an explicit
> round-open commit to this file and the ledger, and this round had none.
>
> **complexity** 复杂 — an instruction-layer amendment on two rules, a decision-log state flip, new
> CI machinery, and a repository-settings change.

## Goal (one line)

`E2` stops being a gate that forbids writing sixteen files without a recorded user ruling, and
becomes an alarm that announces when those files change — so the freeze catches the slip it was
built for instead of blocking the deliberate repairs it has actually been blocking.

## The six user rulings of 2026-08-27 (this file is their carrier)

1. **The floor keeps post-write disclosure only.** `E2` no longer requires a recorded user ruling
   before frozen bytes are written. What survives is: a write to those files is named site-by-site
   in the commit body, and the independent review must see it.
2. **The freeze becomes an alarm, and the alarm hangs on CI.** Not on pre-commit — that is advisory
   and a hook-skipping commit bypasses it, so it cannot catch the slip this mechanism exists for.
3. **The free channel stays; the exception goes.** The user's words on hearing the measurement:
   keep the channel, delete the carve-out. `E10`'s and `R10`'s two `E2`-exception sentences are
   deleted and the channel returns to the unqualified form of the 2026-07-29 routing ruling.
4. **`HD-20` retires.** Its only subject is the free-channel-versus-`E2` conflict; with `E2` no
   longer blocking, the conflict is gone. State flips are the user's, never a session's — this
   ruling is that flip, to be applied in the same commit as the two sentence deletions.
5. **The three `E2`-banked rider rows redeem with the next batch.** Their redeem-when today reads
   「下一个持有 contract v4 `E2` 写入裁决的轮次」, and after this batch no such round exists. It
   becomes: rides the next batch.
6. **Branch protection on `main` joins this batch.** Not as generic hardening but because it is the
   precondition for ruling 2: a `pull_request` event runs the workflow file from the PR's own head,
   so a PR can delete the alarm job. Only a required status check makes deleting it visible as a
   missing check. Dependency pinning and third-party-Action restriction were considered in the same
   conversation and are explicitly **not** in this batch (see *Out of scope*).

## Open questions — answered before the round opens, recorded here

**All four were answered by the user on 2026-08-27** and the answers are recorded inline below.
They are user rulings in their own right — the round is bound by them exactly as it is bound by the
six above.

1. **Does `main` move to a PR flow, or does branch protection cover force-push only?**
   A required status check gates a *merge*; it does not gate a direct push. On today's
   direct-to-`main` flow the alarm job would run and report but could not block, so the teeth
   ruling 6 exists to provide would not exist. The two shapes: **(a)** work lands via PR — the
   alarm genuinely binds, at the cost of a PR per round on a single-author repository;
   **(b)** protection forbids force-push and deletion only — history becomes immutable (which is
   what `HD-59` and `R6` actually rest on) and the alarm stays advisory.
   *Blocks item C's job design and item D.*
   > **Answer (user, 2026-08-27): shape (a) — `main` moves to a PR flow.** Protection forbids
   > force-push and branch deletion, requires a pull request, and makes the alarm job a **required
   > status check**. The alarm then genuinely binds: deleting the job from a PR's own head shows up
   > as a missing required check rather than as silence. The cost — a PR per round on a
   > single-author repository that has used none in 215 commits — is accepted.
   > The basis the user endorsed: ruling 2 moved the alarm off pre-commit precisely because a
   > hook-skipping commit bypasses it; leaving direct push open would reproduce that same bypass one
   > layer up.
2. **What is the alarm's pass condition?** A job that fails whenever frozen bytes change has
   re-created the block in a new place. A job that only prints is invisible as a status check. The
   shape that matches ruling 1 is: **fail when frozen bytes changed AND the commit body does not
   name the changed sites** — the predicate is disclosure, not authorisation, and it is one a
   machine can actually evaluate. Confirm or replace before the job is written.
   *Blocks item C.*
   > **Answer (user, 2026-08-27): the disclosure predicate, with naming test (a).**
   >
   > The job is red when a commit changed a frozen path and that commit's **own body does not
   > contain the full repo-relative path** of the file it changed. The predicate is disclosure, not
   > authorisation.
   >
   > The surrounding mechanism is forced, not chosen: `actions/checkout` with `fetch-depth: 0` (the
   > range and the bodies must be reachable); evaluate **per commit**, each commit against its own
   > body, over the range (push `before..after`, PR `base..head`); **skip merge commits**; report
   > sha plus path plus the miss.
   >
   > **Two alternatives were measured and declined, recorded so they are not re-proposed blind.**
   > *(b) basename appears in the body* is **dominated**: across every frozen-surface commit in
   > history it scores identically to (a) (1/5 green), so it is looser at no gain.
   > *(c) a required `E2-write: <path>` trailer, one line per site* was declined for adding a format
   > the ruling did not ask for. What it would have bought and (a) does not: one command
   > (`git log --grep='^E2-write:'`) recovering the whole write history of the frozen surface —
   > under (a) the paths sit inside prose, so grepping a path also returns commits that merely
   > mention it. If that recall is ever wanted, this is the trade to revisit.
   >
   > **Measured against all 215 commits**: only **5** ever touched a frozen path
   > (`07ef526`, `1656e59`, `d0f185c`, `23ca45b`, `39a21a8`), and **4 of the 5 would be red** under
   > (a) — their bodies describe the work without spelling the paths. History is **not** re-judged;
   > the alarm binds commits made after it lands. The number is recorded because it says plainly
   > that this is a new habit rather than existing practice being ratified, and the rewritten `E2`
   > is what teaches it.
3. **Do the pinned blob literals survive in the rewritten `E2`?** If the alarm compares against the
   previous commit, the pinned expectation in the clause is a second copy that must be maintained —
   the maintenance burden `E3` has been bitten by repeatedly. Dropping the literals is a real
   simplification but changes what the clause states, so it is the user's.
   *Blocks item A.*
   > **Answer (user, 2026-08-27): the literals are dropped.** The rewritten clause names the
   > sixteen paths and stops pinning their blob hashes. The alarm compares against the previous
   > commit, so a pinned expectation inside the clause would be a second copy needing a hand edit on
   > every legitimate write — the maintenance shape `E3` has been bitten by repeatedly. The signed
   > blob `614932de…` keeps its own carrier in `CONTRACT-V4-SIGNATURE.md`, so dropping the literals
   > here loses no record of what was signed.
4. **Is this batch the ledger's queue head, or one item split out of it?**
   `CONSTRUCTION-LEDGER.md`'s current pointer declares the queue head as **one batch of four
   items**: ① dismantle the freeze ② delete the v1 ReviewResult schema definition and its two
   registrations ③ clear the dead digest recipe in the frozen schema ④ close the sweep blind spot.
   This plan scopes ① only, and adds two items the ledger entry does not mention (the CI alarm,
   branch protection). The user ruled the *additions* in (「并进来」); nobody ruled the
   *subtraction*. Two ways out: widen this batch back to the ledger's four, or keep it at ① and
   amend the ledger entry to say the four were split. Opening against a scope the ledger
   contradicts is the drift `R2` exists to catch.
   Argument for splitting, not a decision: items ②③ write frozen bytes, which under the *old* `E2`
   still owe a recorded ruling — so running them in the same round as item A means the round
   changes the rule it is simultaneously operating under.
   *Blocks the round's opening.*
   > **Answer (user, 2026-08-27): the batch stays at ① plus the two additions, and the ledger entry
   > is amended to say the four were split.** The basis the user endorsed: items ②③ write frozen
   > bytes, which under the *old* `E2` still owe a recorded ruling, so running them beside item A
   > would make the round operate under a rule it is simultaneously rewriting. Item ④ touches no
   > frozen path and can ride any batch. Items ②③④ therefore remain queued and their ledger line
   > now says so explicitly rather than implying a four-item batch nobody is running.

## Measured starting state — 2026-08-27 at `51553bd` (`E3`: re-run before any claim)

**The frozen surface — 16 files.**

| object | count | note |
|---|---|---|
| `contract/Document-Work-Assurance-Contract-v4.md` | 1 | current blob `5dfb7b64…`; signed blob is `614932de…` |
| `schema/document-assurance-v3/` | 15 | the 2026-08-03 re-baseline; the pack still holds exactly 15, so there is no unfrozen remainder |

Two of the sixteen are also `E10` members (contract v4, `paragraph-map.schema.json`) — that
intersection is the whole of `HD-20`'s literal scope. All 15 schemas are
`additionalProperties: false`, so any extension of an evidence document is a write to a frozen file.

**The measured case against the freeze as it stands.**

- **`E2` has zero machine enforcement.** The tracked pre-commit hook runs `layer_path_check.py`
  **and nothing else** — its own header says so. `review_freeze_check.py` is `E9`'s review-window
  guard, a different mechanism. A genuine slip (an editor stroke, a commit that skips the hooks)
  meets nothing. The only actor `E2` can stop is one who has read the rule and intends to obey it.
- **No machine could enforce it as written.** `document-harness/journal/batch-b-2026-08-11.md`:
  「`E2` 的谓词是『有没有裁决』，digest 只看得见『字节变没变』。守卫拦下的是*变化*，而 `E2`
  允许有裁决的变化」。That predicate mismatch is why a guard was proposed and refused three times
  under `E6` (rider `PD`'s touch record).
- **It does not protect the signed bytes.** The signature binds blob `614932de…`
  (`CONTRACT-V4-SIGNATURE.md:8`); the file on the tree today is `5dfb7b64…`. The immutable object
  is the git blob, which needs no rule to stay immutable; `E2` guards a working copy that keeps
  moving.
- **It converts the highest-tier repairs into waiting.** Via `HD-20`, a finding landing on a frozen
  path banks however appliable it is. Three rows sit in `HARNESS-RIDERS.md` today for that reason
  alone — `sig-write-once`, `contract-wikilink-tier`, `v1-digest-recipe`.
- **It has never been recorded stopping a wrong write.** A grep of the journals for `E2` plus any
  blocking verb returns one hit, and it is the reverse case: round `DE-PREFIX`'s own candidate
  commit was blocked by the frozen supersessions it was moving, and passed only because `HD-44`
  ruled that a move is not a write.
- **The cost is visible in round structure.** Batch `CORE-SET`'s slicing table gives item F its own
  round with this reason in as many words: "`E2` frozen bytes plus a signature re-siting; needs its
  own user ruling and its own review."

**The free channel is the construction side's main repair route, not a bypass.**

| measure | value |
|---|---|
| commits named as free-channel applications (`V3-*-FREE-*`) | 12 |
| findings they carry | ~21 |
| `E10` amendment commits (`*AMEND*`) over the same history | 5 |
| commits whose body cites the free channel at all | 24 |

The routing general rule is dated **2026-07-29** (`R10` says so in its own text); `HD-20`'s
exception is **2026-08-08**. The general rule is older than the carve-out.

**The mechanism lives in three places, and `HD-20` is the narrowest of them.**

| site | file | scope |
|---|---|---|
| `E10` free-channel sentence | `document-harness/CONSTRUCTION-CHECKLIST.md:139` | any `E2`-frozen path |
| `R10` routing sentence | `document-harness/CONSTRUCTION-CHECKLIST.md:224` | any `E2`-frozen path (cites `HD-20`) |
| `HD-20` itself | `HARNESS-DECISIONS.md:555` | only paths both `E2`-frozen **and** `E10` members — 2 files |

That width difference is not inferred: rider `v1-digest-recipe` measured it, its defect sitting in
`review.schema.json`, which is frozen but not a member, so `HD-20`'s letter does not reach it. The
pair at `:139` / `:224` has already drifted once — rider `wl-route` records the free-channel routing
reading as 「三句规则二比一」, two executors necessarily disagreeing.

**The alarm's candidate mounting point, and the three rulings standing against it.**
`pack_digests()` (`tooling/rsclib/document_harness/__init__.py:238`) hashes the contract plus the
whole schema pack and has **zero callers** — re-measured at this commit: the definition at `:238`
and the `__all__` export at `:266`, nothing else under `tooling/`. But it is not free to use:

- **`HD-27` refused to wire it to `E2` three times** (2026-08-11 · 2026-08-17 · 2026-08-20), each
  time under `E6`, and rider `PD` carries the touch record. The refusals' stated basis is that a
  **pre-commit** guard 守的是「不得无裁决写入」 — a predicate no machine can see.
- **`document-harness/split-design.md:131` proposes deleting it outright** (「`E6`：无任何决定依赖
  的机器」), which is the opposite disposition from wiring it.
- Item C's job runs on **CI**, and its predicate under question 2 is disclosure rather than
  authorisation — a different question from the one refused three times. **That difference must be
  argued in the round's commit body, not assumed**, or a reader who finds the three refusals reads
  this batch as overturning them silently.
- **Rider `PD`'s surviving redeem-when arm is 「下一个碰 `E2` 冻结面的批」, and this batch is it.**
  The row must be answered at this batch's closeout — redeemed, re-scoped, or refused a fourth
  time — not left standing.

**Repository security posture (measured 2026-08-27 via `gh`; repo is PUBLIC, 0 forks, 0 stars).**

| already correct | value |
|---|---|
| CI trigger | `on: push, pull_request` — **not** `pull_request_target`; fork PRs get no secrets and a read-only token |
| secrets used by any workflow | none |
| default workflow token permission | `read`; `can_approve_pull_request_reviews: false` |
| fork PR approval policy | `first_time_contributors` |
| expression interpolation into `run:` | none — no script-injection surface |
| committed credentials | pattern scan returns nothing |

| gap | value |
|---|---|
| `main` branch protection | **absent** — the protection endpoint returns `Branch not protected` (404), re-measured at this commit |
| dependency pinning in CI | absent — `pip install pytest "jsonschema>=4.18" referencing` resolves latest at run time |
| third-party Actions | `allowed_actions: all`, `sha_pinning_required: false`; the workflow uses mutable tags `actions/checkout@v4`, `actions/setup-python@v5` |

**The repository has never used a pull request: 215 commits on `main`, `gh pr list --state all`
returns empty.** This is the crux of question 1.

**The ledger is at its entry bound.** `CONSTRUCTION-LEDGER.md` holds exactly **20** top-level
entries against a bound of ≤ 20, so this batch's pointer **amends the existing queue-head entry**
rather than adding a twenty-first. Precedent for amending a pointer entry in place: `51553bd`.

## Constraints

- **This is design and it opens a round.** `E2`, the `E10` free-channel sentence and the `R10`
  routing sentence all live in `document-harness/CONSTRUCTION-CHECKLIST.md`, an `E10` member;
  changing what a rule requires is design by `E10`'s own test, so the free channel does not apply
  to this work. `E11` preview card, and a cold read at opening.
- **`E10-sync` does NOT fall due.** No item touches the membership sentence, and `LAYER` in
  `tooling/hooks/layer_path_check.py` is unchanged. Say so in the commit body so the next reader
  does not wonder.
- **`HD-55` role form**: orchestrator, executor and reviewer are three sessions; dispatch cold via
  `dtw dispatch`; the orchestrator hand-edits no work product.
- **The decision-log invariant**: only the user flips a decision's state. Ruling 4 is that flip for
  `HD-20`; a session records the proposal, never the flip. Precedent: `HD-60`/`HD-61` at `a554c0b`.
- **`HD-59`**: a committed conclusion is never rewritten in place. Every correction in this batch is
  written forward, with the original left standing beside it.
- **Branch-protection and repository-settings changes are outward-facing.** Do not apply them
  unilaterally: present the exact `gh` command and let the user run it, or take explicit
  authorisation first.
- **This batch writes no frozen bytes.** It changes the rule about them. If a frozen file needs
  editing mid-round, that is still the old regime until the amendment lands — do not use this
  batch's own goal as its authorisation.

## Out of scope

- OUT: **dependency pinning in CI** and **restricting third-party Actions**. Both are real gaps
  (measured above) and both are unrelated to `E2`; folding them in dirties this round's review
  surface. User ruled them a separate small piece. **They were tracked nowhere before this batch** —
  the ledger entry written with this plan gives them a home so they survive this file.
- OUT: rewriting git history to replace the author email. The address is public across all 215
  commits; changing it retroactively is exactly the history rewrite branch protection exists to
  prevent. A switch to a noreply address for *future* commits is a separate, non-blocking choice.
- OUT: redeeming the three `E2`-banked riders. This batch only rewrites their redeem-when; the
  fixes ride the next batch (ruling 5).
- OUT (**pending question 4**): deleting the v1 ReviewResult schema, clearing the dead digest
  recipe, and closing the `N2_MODULES_WITHOUT_CODES` sweep blind spot. These are the ledger queue
  head's items ②③④ and this exclusion is **the plan author's judgment, not a user ruling** —
  question 4 resolves it.
- OUT: the candidate-isolation design question (filed 2026-08-27, not yet ruled whether it opens a
  round).
- OUT: touching frozen bytes (see *Constraints*).

## Work items

Sites are at `51553bd` and must be re-derived before editing — line numbers drift.

### A — `E2` is rewritten from gate to alarm *(ruling 1)*

- `document-harness/CONSTRUCTION-CHECKLIST.md:53-72` — the `E2` clause. What changes: frozen bytes
  may be written; what is owed is **disclosure after the fact**, site by site, in the commit body,
  and visibility to the independent review. What stays: the list of sixteen (the alarm needs to
  know what it watches), and the fact that a path outside the list is not covered.
- **The pinned blob literals are dropped** (question 3). The clause names the sixteen paths and
  stops carrying their hashes; the signed blob keeps its carrier in `CONTRACT-V4-SIGNATURE.md`.
- **The clause must state its own limit.** The alarm can see that the body names a path; it cannot
  see whether what the body says about that path is true. Write that ceiling into the clause rather
  than letting the next reader infer a guarantee that is not there.
- The clause's own name should stop saying "frozen" if the word no longer describes what it does;
  that is a wording call for the round, not a separate item.

### B — the two exception sentences are deleted and `HD-20` retires *(rulings 3 and 4)*

- `document-harness/CONSTRUCTION-CHECKLIST.md:139` — delete the `E2` carve-out from the `E10`
  free-channel sentence.
- `document-harness/CONSTRUCTION-CHECKLIST.md:224` — delete the `E2` override from the `R10`
  routing sentence.
- `HARNESS-DECISIONS.md:555` — `HD-20` to `retired` (subject gone), carrying ruling 4 as its basis.
- **All three in one commit.** Splitting them leaves the layer saying three different things about
  the same route, which is the drift rider `wl-route` already measured on this exact pair.

### C — the CI alarm *(ruling 2)*

- `.github/workflows/ci.yml` — a new job. **Settled by question 2**: red when a commit changed a
  frozen path and that commit's own body does not contain the file's full repo-relative path.
  `fetch-depth: 0`; per-commit over the range (push `before..after`, PR `base..head`); merge
  commits skipped; the failure prints sha + path.
- **The job must be a required status check** (question 1), which is item D's half of the same
  mechanism — a job that is not required can be deleted in the PR that needs it gone.
- Edge cases the writer owns: a push whose `before` is the all-zeros SHA (new branch / no range) —
  fall back to the head commit alone rather than scanning all history; and a range that reaches
  commits made before this job landed, which are **not** re-judged.
- Mounting point: `pack_digests()` is the ready-made hook, **but see the three rulings standing
  against it** in *Measured starting state*. Whether the job calls it, re-implements the hash, or
  compares blobs against the previous commit is the round's call, and the round owes rider `PD` an
  answer either way.
- The job needs a test. The battery is the repository's own evidence standard; a guard with no test
  is the shape `E6` refuses.
- Note for whoever writes it: `on: pull_request` runs the workflow from the PR's head, so the job
  cannot defend itself — that is what item D is for.

### D — branch protection on `main` *(ruling 6)*

- **Shape settled by question 1: `main` moves to a PR flow.** Protection forbids force-push and
  branch deletion, requires a pull request, and lists item C's job as a **required status check**.
- Consequence the round must absorb rather than discover: from the moment protection lands, this
  batch's own remaining commits cannot be pushed straight to `main` either. Decide and record
  whether protection is applied **before** or **after** the round's own commits land.
- Produce the exact `gh api` command; **the user runs it, or authorises it explicitly.** Record what
  was actually applied, measured by re-reading the protection endpoint afterwards rather than by
  asserting it.
- Whatever shape is chosen, forbidding force-push and branch deletion is the part that `HD-59`
  ("a committed conclusion is never rewritten in place") and `R6` (records are immutable) have been
  resting on with nothing underneath them.

### E — the three rider rows' redeem-when *(ruling 5)*

- `HARNESS-RIDERS.md` rows `sig-write-once` (`:30`), `contract-wikilink-tier` (`:33`),
  `v1-digest-recipe` (`:37`).
- Replace 「下一个持有 contract v4 `E2` 写入裁决的轮次」 with the next batch (ruling 5). Keep each
  row's deadline arm as written; `R10` requires a touch condition or a deadline, and this ruling
  supplies the touch condition.
- These rows' *content* is not re-litigated here.

## Steps

- [x] 1. Carry the six rulings and the open questions out of the session-side briefing into
      committed state: this tracked plan, plus a `CONSTRUCTION-LEDGER.md` current-pointer entry
      naming the batch and its queue position. Until this is done the rulings are unreachable by
      any reviewer (`R2`).
- [x] 2. Put the four open questions to the user and record the answers **in this file**.
      **DONE 2026-08-27** — all four answered and recorded inline under *Open questions*: PR flow
      with the alarm as a required status check · the disclosure predicate with naming test (a) ·
      the pinned blob literals dropped · the batch stays at ① plus the two additions, with the
      ledger entry amended to say the queue head's four were split.
- [x] 3. Open the round under `HD-55` role form: cold layer read via `dtw dispatch --read`, then
      render the `E11` preview card and wait for the user. The read is full-weight unless the user
      waives it — `CONSTRUCTION-CHECKLIST.md` is the member this batch edits and it has changed
      since the last recorded end-to-end read.
      **DONE**: card rendered and approved; full-weight cold read of all nine members returned and
      committed unchanged at **`464b7dc`** (`v3-cold-read-860401e.md`). Its one must-fix — a
      pointer into a README section deleted on 2026-08-24 — was answered under `E10`'s deferral
      clause at **`580d236`**.
- [x] 4. Execute item B in one commit (two sentences + the `HD-20` flip together). **`a2d3fb4`.**
- [x] 5. Execute item A (**`184387c`**). Landing it after B is deliberate: B removes the references to `E2`'s old
      form, so A rewrites a clause nothing else is quoting.
- [x] 6. Execute item C, with its test (**`1d4d9aa`** — job `announced-path-disclosure`, 18 tests).
      Rider `PD` answered in **`0355b36`**: re-scoped, neither redeemed nor refused a fourth time.
- [x] 7. Item D — produce the `gh` command, hand it to the user, record what was applied by
      re-reading the endpoint.
      **DONE 2026-08-28.** The user ran it after the alarm had been observed green on GitHub twice
      (runs `33089379131` and `33096441363`, the second judging 8 commits), so the check name was
      registered and could not deadlock. **Measured by re-reading
      `repos/Melclycj/do-the-work/branches/main/protection`, not asserted from the command's own
      response**: required status check `announced-path-disclosure` (strict `false`),
      `enforce_admins` **`true`**, required pull request with `required_approving_review_count` `0`
      (GitHub forbids approving one's own PR, so any higher count deadlocks a single-author
      repository), force-push `false`, deletion `false`.
      **Consequence, in force from this moment**: nothing reaches `origin/main` without a pull
      request whose `announced-path-disclosure` check is green — the repository owner included.
- [x] 8. Execute item E. **`0355b36`.**
- [x] 9. **Budget walked in full.** FULL over `464b7dc..ad0663d` returned `CHANGES_REQUIRED`
      (2 blockers, 2 low, 6 observations), record unchanged at **`9580ca9`**. The one approved fix
      leg: **`013483f`** (blocker 2, orchestrator bookkeeping), **`1830d47`** (`HD-44` → superseded,
      successor `HD-62` carries the narrowed text), **`34d63cc`** (`split-design.md` §5 corrected
      forward), **`629cff5`** (the announced-set anchor banked as rider `announced-set-anchor`,
      judged design rather than repair). VERIFY over `9580ca9..629cff5` returned
      **`REVIEWED_NO_BLOCKER`**, record unchanged at **`a8bfe5b`**. Walk the `E9` budget (one FULL, at most one approved fix, one VERIFY),
      land the records unchanged, close the round.

## Acceptance (done = ?)

Each shown by its command, not by a sentence.

1. `grep -n "E2" document-harness/CONSTRUCTION-CHECKLIST.md` shows the rewritten clause and **no**
   surviving exception sentence at the former `:139` / `:224` sites.
2. `HD-20` reads `retired` in `HARNESS-DECISIONS.md`, in the same commit as those deletions
   (`git show --stat` on that one commit shows both files).
3. `python -m pytest -q` green, including the new alarm's test. Report the run, not a figure copied
   from here.
4. `layer_path_check.py`, `candidate_path_check.py` and `review_freeze_check.py` each exit 0 on the
   staged tree, and the `E10` members resolve 9/9.
5. The alarm demonstrably fires: a scratch commit touching a frozen file **without** naming it in
   the body makes the job red; the same change **with** the body naming the site makes it green.
   Paste both runs. (Delete the scratch commits — they are the test's evidence, not history.)
6. `gh api repos/Melclycj/do-the-work/branches/main/protection` returns a protection object rather
   than 404, and that object shows the PR-flow shape question 1 settled: force-push and deletion
   forbidden, a pull request required, and item C's job listed among the required status checks.
   Read the endpoint back — do not assert it from the command that was run.
   **MET 2026-08-28**, endpoint re-read: contexts `["announced-path-disclosure"]`, strict `false`,
   `enforce_admins` `true`, `required_approving_review_count` `0`, `allow_force_pushes` `false`,
   `allow_deletions` `false`.
7. The three rider rows' redeem-when no longer names an `E2` write authorisation:

   ```sh
   grep -c 'E2` 写入裁决' HARNESS-RIDERS.md   # → 0
   ```

   **The command is corrected here.** The session-side briefing wrote it as
   `grep -c "E2 写入裁决"` — without the closing backtick after `E2` — and that form already
   returns 0 at `51553bd`, so the acceptance would have passed without anything being done. The
   corrected form returns **3** today (rows at `:30`, `:33`, `:37`).
8. Rider `PD`'s row is answered rather than left standing — redeemed and deleted, or re-scoped with
   a new redeem-when, or refused a fourth time with the basis recorded.
9. The round's FULL returned `REVIEWED_NO_BLOCKER`, or `CHANGES_REQUIRED` → one approved fix →
   VERIFY `REVIEWED_NO_BLOCKER`, all records committed unchanged.

## What else is queued behind this batch (read-only inventory, 2026-08-27)

Not this batch's work. Recorded so a fresh session can see the whole board without re-deriving it.

| item | where it is recorded | state |
|---|---|---|
| the ledger queue head's items ②③④ | `CONSTRUCTION-LEDGER.md` current pointer | all three **not started, zero commits**; detail below. Whether they are in or out of this batch is question 4 |
| batch `dispatch-economy` | ledger, same entry | queued behind the head, no deadline; holds 8 design riders (the ninth, `waiver-live`, redeemed in `CORE-SET` round 1) |
| splitting the ledger's CLOSED roll | ledger header + its own entry | its own ledger batch, gated by a user ruling; the roll breaches the per-entry bound the day it was written (16,171 characters against 2,500) |
| candidate isolation is a lost mechanism | ledger | design question filed 2026-08-27, **not yet ruled whether it opens a round**; today the executor's commits land on the one branch before any review sees them, so `CHANGES_REQUIRED` cannot be enacted by declining to promote |
| rider bank | `HARNESS-RIDERS.md` | 28 rows |
| CI dependency pinning + third-party Action restriction | **the ledger entry this batch writes** — it had no home before | measured 2026-08-27 (unpinned `pip install`; `allowed_actions: all`, mutable action tags). User ruled it a separate small piece |
| author email exposed in all 215 public commits | this file only | not an action item; the only forward option is a noreply address for future commits (history rewrite is excluded) |

**The queue head's other three items, measured at `51553bd` — they are 2+1, not four of a kind.**
Two write frozen bytes and are therefore gated by the very rule this batch is changing; one touches
no frozen path and can ride anything. That shape is an input to question 4.

- **② delete the v1 ReviewResult schema definition + its two registrations** — not started.
  Definition at `schema/document-assurance-v3/review.schema.json:258` (`$defs/reviewResult`, named
  again in the file title at `:4`); registrations at
  `tooling/rsclib/document_harness/review.py:65` and `:71`. **Harder than the ledger line reads**:
  `review.py:11-18` records that both registrations stay deliberately, because
  `review.v2.schema.json` `$ref`s five of this file's `$defs` (`reviewRound`,
  `instructionCompleteness`, `perObligationDisposition`, `finding`, `verifyScope`), so the *file*
  must keep resolving through the registry or the v2 validator does not run. Measured: v2 does
  **not** `$ref` `reviewResult`, so the `$defs/reviewResult` block and the `review_result` pointer
  can go — the file cannot. The fallback the ledger wants turned into an error is
  `result_schema_kind()` at `tooling/rsclib/document_harness/review_result_v2.py:51-60` (absent
  `schema_version` returns `"review_result"`). **Frozen bytes.**
- **③ clear the dead digest recipe** — not started, and already broken rather than merely stale:
  the `package_ref` description in `review.schema.json:281` tells the reader to run
  `from rsclib.document_harness.review import package_digest`, and round `CORE-SET-CODE`'s item G
  deleted it (`def package_digest` now returns zero hits repo-wide). **Doubly stale, and this half
  is recorded nowhere else**: the same sentence says to reproduce it from `ResearchSystem/tooling`,
  a path `DE-PREFIX` removed. Banked as rider `v1-digest-recipe`. **Frozen bytes.** Likely absorbed
  by ② — the description lives inside the `$defs/reviewResult` block ② deletes.
- **④ close the sweep blind spot** — not started; **the only one of the three touching no frozen
  path**. `N2_MODULES_WITHOUT_CODES = ("review.py",)` at
  `tooling/tests/document_harness_review/test_fix_round_locks.py:277` is consumed only by the
  partition assertion at `:379` (every module belongs to one of four lists); nothing asserts that a
  module *on this list* carries no coded vocabulary, so a code returning to `review.py` leaves the
  suite green. **Path correction**: the ledger names `test_fix_round_locks.py` without its
  directory; it is under `tooling/tests/document_harness_review/`, not
  `tooling/tests/document_harness/`.

## Resume pointer

当前指针: **done. Round CLOSED, batch CLOSED, 2026-08-28.** Nothing in this plan is outstanding.

The chain, base `51553bd` → tip: `a0a5595` (rulings landed) · `860401e` (four answers) · `464b7dc`
(opening cold read) · `580d236` (its must-fix) · `a2d3fb4` (B) · `184387c` (A) · `1d4d9aa` (C) ·
`0355b36` (E) · `ad0663d` (errata) · `9580ca9` (FULL `CHANGES_REQUIRED`) · `013483f` `1830d47`
`34d63cc` `629cff5` (the one fix leg) · `a8bfe5b` (VERIFY `REVIEWED_NO_BLOCKER`) · `57a31c1` (`V-1`).

**What changed for anyone working in this repository, in one line each.**

- The sixteen announced paths may be written. What is owed is naming each changed path, in full and
  repo-relative, in the body of the commit that changed it.
- A CI job checks exactly that, per commit, and it is a required status check on `main`.
- `main` is a PR flow. Force-push and deletion are refused, and `enforce_admins` is true, so this
  binds the repository owner too.

**Banked rather than fixed — read these as open, not delivered.**

- `announced-set-anchor`: the sixteen paths have no enumeration this repository can resolve on its
  own. Judged design rather than repair by the fix leg and confirmed by the VERIFY. Deadline: the
  first time the `schema/document-assurance-v3/` pack gains or loses a file.
- `e10-freeze-exception`: `E10`'s list of what the guard cannot see still excepts bytes "while they
  are frozen", a state item A ended.
- `archive-header-selfcount`: touched by `HD-44`'s move into the archive and deliberately left
  standing, the fix leg's boundary being the four approved findings.
- The three `E2`-banked riders (`sig-write-once`, `contract-wikilink-tier`, `v1-digest-recipe`) now
  ride the next batch — nothing in this batch redeemed them.

**Recorded because it will not be true again**: every commit in this round went straight to `main`.
Protection landed after them, so the PR flow this batch installed did not govern the batch that
installed it.

## Notes

- **Batch `CORE-SET` is CLOSED** (2026-08-27, `418477a` / `51553bd`). This batch is its successor in
  the queue, taken from the "What the user directed next" section of
  `document-harness/plans/core-set.plan.md`, whose first bullet is this one: the freeze was meant
  to prevent a slip, not to keep blocking deliberate change.
- **The user's hypothesis about the free channel was measured and did not hold**, and the
  measurement is why ruling 3 is "keep the channel". The hypothesis was that the free channel might
  be an escape route invented because `E2` was obstructing development; the routing general rule is
  2026-07-29 and `HD-20`'s exception is 2026-08-08, so the channel predates the carve-out, and it
  carries ~21 findings across 12 commits against 5 amendment commits total. Deleting it would push
  every low-tier finding into the bank and put standing pressure on `R3`'s ban on tier inflation,
  since the only remaining route to a landed fix would be must-fix, which burns the round's single
  repair. Recorded here because a rejected hypothesis is knowledge and the next reader may form it
  again.
- **Why a post-write alarm is buildable where the pre-write guard was not.** The guard was refused
  three times under `E6` because its predicate ("was there a ruling?") is invisible to a machine.
  The alarm's predicate is "did the bytes change, and does the commit body name the sites?" — both
  mechanically decidable. This is not a reversal of those refusals so much as a different question;
  say so in the round's commit body, because a reader who finds the three refusals will otherwise
  read this batch as overturning them.
- **This repository keeps no second, session-side ledger.** Its durable tracker is
  `CONSTRUCTION-LEDGER.md`; an untracked ledger beside it is the drifting copy that file's own
  header forbids.
- **Numbers here are measurements at `51553bd`.** Re-run rather than cite.
