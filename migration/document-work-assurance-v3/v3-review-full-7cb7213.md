# FULL — `6c5b039..7cb7213`

**Verdict: `REVIEWED_NO_BLOCKER`.** No blocking discrepancy was found within the frozen
subject and the review dimensions below. That is not a proof of correctness and certifies
nothing about the text being good.

**Findings: 0 blockers, 5 low, 4 observations.** Every ruling the round set out to record is
recorded, in the home its own plan named, and the two mechanical facts a reader would want —
that no code moved and that the layer's path guard still passes — reproduce exactly. The five
lows are two stale figures in the commit body, two clauses of new instruction text that say
slightly more or less than they mean, and one site of the merged-role class that this round's
own decision-log edit left standing and simultaneously stopped tracking.

Independence: this session was dispatched by the orchestrator with a range and nothing else,
derived round, budget, authorization and every number below from the repository, and reports
through the orchestrator. `R1`'s four holdings are the orchestrator's. Whether that is so in
fact is a process claim about *this* session and is not verifiable from the repository either
(`R4`) — what is structural is that nothing in the dispatch set the question.

---

## 1. What the subject is, derived

`git rev-list --count 6c5b039..7cb7213` → 1. The range is one commit.

| | |
|---|---|
| base | `6c5b03932e5ecde14de285549569b2c6cfae52cb` — `V3-PRERUN-RIDERS-PLAN-v1` |
| tip | `7cb721353eba95c1076c3a313bacaf4dfbfcfa7b` — `V3-PRERUN-RIDERS-v1` |
| kind, as the body names it (`E8`) | **candidate** |
| round | `PRERUN-RIDERS` |
| branch tip at review time | `7cb7213` — the dispatched tip, so the `E9` window has held |
| worktree | clean; `git status --porcelain --untracked-files=all` empty |
| freeze marker | `.harness/review-pending.json` carries this exact range, `dispatched_at` `2026-08-22T13:53:19+00:00` |

**Budget position, derived.** No `v3-review-full-7cb7213.md` and no `v3-review-verify-*`
record for this round exist in `migration/document-work-assurance-v3/` at the subject. The
only record between base and the round's opening is `v3-cold-read-3a6a10b.md`, committed at
`ee3e05f` — an `E10` read, which by `R3` is not a round and spends no budget. **This is the
round's FULL and consumes the FULL leg.** One user-approved fix and one targeted VERIFY
remain. `R10`'s closeout obligation applies to the five lows below: the spend-the-fix-leg /
bank choice is the user's, put to them by the orchestrator, and `E9`'s test does not expire at
closeout — a late activation is still this round's one fix and still obliges the VERIFY.

**What was authorized, derived.** `document-harness/plans/prerun-riders.plan.md`, committed at
the base, is the in-repository carrier of seven user rulings of 2026-08-22 and of the round's
change surface. The preview card (`E11`) and the user's approval of it are not in the
repository — construction-round cards are ruled not to be persisted
(`CONSTRUCTION-LEDGER.md`, the `E11`-carrier ruling of 2026-08-21). Per `R7` this is a
ceiling, not a block: **I cannot see the approval, and I do not treat its absence as a
defect.** The rulings themselves were chat-only until the base commit; the plan is what ended
that, and `R2`'s chat-only complaint therefore does not fire against this round.

**Changed paths, classified by hand** (`git diff --numstat 6c5b039 7cb7213`, re-run here):

| path | + / − | class | inside the plan's change surface? |
|---|---|---|---|
| `document-harness/CONSTRUCTION-CHECKLIST.md` | 7 / 2 | `E10` member | yes — `E1` reword |
| `document-harness/EXECUTION.md` | 14 / 1 | `E10` member | yes — authoring rules |
| `document-harness/ORCHESTRATION.md` | 31 / 11 | `E10` member | yes — three sites |
| `document-harness/REVIEW.md` | 37 / 7 | `E10` member | yes — two sections |
| `HARNESS-RIDERS.md` | 4 / 7 | rider bank | yes as a file; **one operation beyond the six enumerated** — see `O-2` |
| `HARNESS-DECISIONS.md` | 29 / 27 | decision log | yes — `HD-55` flip |

Blob ids at the tip: `31e785f8` · `3908907a` · `26f64cac` · `684717ba` · `5de5acb3` ·
`3e0f6b07`.

No path under `schema/`, `tooling/`, `contract/` or `migration/` changed — verified by an
empty `git diff --stat 6c5b039 7cb7213 -- schema/ tooling/ contract/ migration/`. **`E2`'s
frozen bytes are untouched**: the three named blobs and the whole
`schema/document-assurance-v3/` pack are outside the change set by inspection. `E10`'s
membership sentence is unedited, so no `E10-sync` is due and the rider stays banked, as the
plan says.

---

## 2. Lead with the implementation

### 2.1 The seven rulings, each checked against the text that now carries it

| ruling | carrier at the tip | holds? |
|---|---|---|
| 1 — plans are a delivered item | `ORCHESTRATION.md:65` delivery list; `:75`–`:84` reason | yes |
| 1's bound — instruction first | `EXECUTION.md:462`–`:472`, a new authoring-rules bullet | yes, with `L-4` |
| 2 — a thin check is a control-plane finding | `REVIEW.md:33`–`:41` and the mirror at `:260`–`:265` | yes |
| 3 — the reviewer's route is the record | `REVIEW.md:43`–`:52` | yes, with `L-3` |
| 4 — `status-key` upheld, discipline named | `HARNESS-RIDERS.md` row rewritten | yes |
| 5 — `mark-case` re-ruled, word list untouched | row deleted; `_NORMATIVE_MARKERS` unchanged | yes |
| 6 — `ctx-ground` upheld | row rewritten | yes |
| 7 — `HD-55` home + class fix + flip | `ORCHESTRATION.md:26`–`:32`, `E1`, `ORCHESTRATION.md:114`–`:117`, `HD-55` moved | yes, with `L-5` |

**Ruling 1 closes the gap it names, and closes it everywhere.**
`git grep -n -E "instruction and subject\|instruction, subject\|delivers"` over the ten
members, the plans and `tooling/rsclib/` returns exactly two live enumerations —
`ORCHESTRATION.md:65` (*instruction, subject and governing plans*) and `EXECUTION.md:447`
(*the plans arriving with the instruction and subject the orchestrator delivers*) — and they
agree. Every other hit is a review record or `executor-charter.plan.md:24` quoting the
superseded wording historically. The executor-side dispatch prompts
(`dispatch.py:781`, `:798`) enumerate no deliverables at all, so no code contradicts the new
obligation. The gap rider `plan-delivery` recorded is genuinely gone, not merely re-worded.

**Ruling 2's mirror is real.** `REVIEW.md:38`–`:41` claims to mirror *The `review_only`
question* at `:271`–`:282`, and the two do land on the same object: a finding about the
WorkSpec. One asymmetry, recorded not as a defect: the `review_only` sentence carries an
explicit *"not a blocker, unless it violates an obligation, an invariant or the contract"*
and the new one does not. The general rule at `:296` governs both, so nothing acts wrongly —
but the mirror is slightly less exact than the text says it is. See `O-4`.

**Ruling 5's deletion is well-founded and its fact survives the row.**
`_NORMATIVE_MARKERS` at `instruction.py:142` is byte-identical to its pre-round form, and the
`_is_context_title` docstring at `:181`–`:185` still states, in delivered code, that the list
is case-sensitive and that lower-case `must` in Context raises nothing, citing the rider's own
source. Deleting the row therefore does not close the record. **The measured evidence the
deletion cites is `UNVERIFIABLE` from here** (`R4`): the eight closed runs' instructions are
caller-held, and `assurance/` in this repository holds only `templates/`, `test/` and
`review-test/` — no `instruction.md` exists in the tree. I neither confirm nor dispute the
0 / 1 / 0 figures; I record that they cannot be re-run at this subject.

**Ruling 7's `E1` reword changes the mechanics by not one word.** Diffed clause by clause:
from *"states which of the four the executor held"* through *"does not call the result
structurally independent"* is byte-identical across the edit; only the lead-in changed from
*"Between those, the round"* to *"Standing there, the round"*, with the exception-channel
framing added before it. `HD-55`'s status-line claim *"披露机制一字未改"* is exact.

**The `HD-55` flip is `HD-2`-conformant.** Diffing the entry across the move: the ruling,
consequence and basis paragraphs are byte-identical; only the status line and one basis clause
changed. §live is lines `28`–`134` and holds exactly seven entries after the move — HD-44,
HD-41, HD-36, HD-35, HD-34, HD-23, HD-9 — reproducing the commit body's count. §implemented
opens at `135` with `HD-55` at `137`, in descending order ahead of `HD-54`.

### 2.2 Do the guards still bind

No guard changed, so `E4` and `E5` have nothing new to bite on. Two things were re-run rather
than read:

- **Regression battery.** `cd tooling && python -m pytest -q` → **790 passed in 134.21s**,
  identical to the base figure the plan measured at `ee3e05f`. Run by me at the subject tip,
  after every other measurement below. This is the evidence that the round touched no code,
  and it is the reported figure re-derived, not accepted.
- **`layer_path_check`.** The guard reads a *staged* diff, which no longer exists, so I
  replayed it: imported the module, rebuilt `added_lines_by_path` from
  `git diff -M -U0 6c5b039 7cb7213`, and ran `unresolved_tokens` for each of the ten `LAYER`
  members. **Zero failures.** The one non-member backtick token the body names,
  `document-harness/plans/prerun-riders.plan.md`, exists.
- **The guard's stated blind spot, closed by hand rather than asserted.** Markdown links
  carry no backtick token, so I resolved every one myself from its own file's directory:
  **16 distinct (file, target) pairs across the four changed members, 16 resolve.** That
  count reproduces the body's "16 checked, 16 OK" once you see it is deduplicated per file —
  the raw occurrence count is 19.

### 2.3 The class scans, re-run rather than read (`HD-41` ④)

| class | reproduces? |
|---|---|
| 1 — merged-role, over the ten members | **exactly.** Six hits at `CONSTRUCTION-CHECKLIST.md:39`, `EXECUTION.md:42`, `:236`, `ORCHESTRATION.md:26`, `:31`, `:116` — the pasted output is byte-identical to what the pattern returns at the tip. The two out-of-class `EXECUTION.md` hits are untouched and are what the cold read said they were. Measured last, as claimed. |
| 2 — `HarnessIssue` routing, over the ten members | **exactly.** `CONSTRUCTION-CHECKLIST.md:199`, `EXECUTION.md:31`, `REVIEW.md:45`, `:50`. The dangling occurrence is gone; the three survivors all say post-run, filed by the observer. |
| 3 — `plan` as a delivered item | **count yes, positions no.** See `L-2`. |
| 4 — the four deleted rider ids | **exactly, within the range the body declares.** Two live references inside *the bank, the decision log, the ten members and io-design.md*, both handled. The range omits one surface that carries a third — see `O-1`. |

### 2.4 The factual assertions the body says it ran first (`E3`)

| assertion | re-run result |
|---|---|
| `harness-issue.schema.json:44` reads `"enum": ["CLOSED", "STOPPED_REPLAN"]` under `observed_after` | **exact**, line and content |
| `3a6a10b:ORCHESTRATION.md` rows 22–23 read *"a full session — the one the user is talking to"* and *"a full session"* | **exact** |
| `HEAD:document-harness/io-design.md` = `8f3c82c2627cb678e520f46d3a47fdf1616fd8d9` | **exact**, and it is the blob `HD-35` binds |
| `io-design.md:100` still hangs the question on rider `HI-route` | **true**, and the quotation of it is inexact — see `O-3` |
| the rider bank census supporting *"codifying what reviewers have in fact done"* | **falsified** — see `L-1` |
| staged change set, six paths, the numstat pairs | **exact**, all six |

---

## 3. Findings

### `L-1` (low) — the rider-bank census in the commit body is stale, and the row this commit added is the counterexample it did not count

**Location.** Commit body, the `E3` paragraph: *"of the bank's 34 data rows at this commit, 32
cite a review or read record in the source column; the two that do not are submod-index … and
chk-caller-prefixes"*.

**Ground truth.** Parsed at the subject tip: `HARNESS-RIDERS.md` holds one table, header at
`:9`, separator at `:10`, **35 data rows**. Classifying each source column for a
`v3-{review-full,review-verify,checkpoint-read,cold-read}-<sha>` citation: **32 cite one, and
three do not** — `submod-index`, `chk-caller-prefixes`, and **`io-hiroute-stale`, the row this
same commit adds**, whose source column is the round's own deletion scan.

**Why it is `E3` and not arithmetic.** The figure was taken before the last edit, and the last
edit changed the thing measured. That is the precise failure *"Measure last: a figure is
invalidated by any later change to what it measures"* names, and it happened to the one figure
in the round that `E3`'s final sentence binds hardest — the command run to keep a factual
assertion written into instruction text from being false.

**Why it is low and not a blocker.** The assertion it supports survives: 32 of 35 is the
practice as strongly as 32 of 34, and the body itself already hedges to *"the practice and not
an absolute"*. `REVIEW.md:43`–`:44` is true as written. Nothing in the tree acts wrongly, and
there is no fix a bounded repair can land in the subject — `E8` forbids the amend that would
correct a commit body.

**Bytes.** None appliable to the subject. The correcting record is either an errata commit
(`E8` names the kind; `d1782e8` is the precedent) or this record, which now holds the
re-derived figures. Bank if the user prefers the cheaper route: the numbers live here either
way.

### `L-2` (low) — the class-3 line enumeration does not reproduce

**Location.** Commit body: *"plan/plans now occurs in `ORCHESTRATION.md` at :65 :72 :74 :77
:79 :102"*.

**Ground truth.** `git grep -n -i plan 7cb7213 -- document-harness/ORCHESTRATION.md` returns
**`:65 :75 :77 :80 :83 :102`**. The count (6) and the file are right; **three of the six
positions are wrong**, and the two anchors that agree do so by coincidence of position, not of
line. The pre-round measurement it contrasts against — *"exactly one, at the old :83"* —
**does** reproduce exactly at `3a6a10b`.

**Why it matters at all.** The class-1 scan two paragraphs earlier states it was *"run after
the last edit"*, and it was — it reproduces byte for byte. This one was not, and a reader has
no way to tell the two apart from the body. The short line at `ORCHESTRATION.md:81` (*"in the
instruction is"*) is the unrewrapped seam of the edit that happened after the count.

**Why it is low.** Same shape as `L-1`: the substance — `plan` now occurs as a deliverable in
the delivery section, where before it occurred once in the report-back section — is true, and
the enumeration is re-derivable in one command. No actor acts on the line numbers.

**Bytes.** None appliable; the corrected enumeration is above.

### `L-3` (low) — `REVIEW.md`'s parenthetical forbids the route its own paragraph gives two sentences later

**Location.** `document-harness/REVIEW.md:46`–`:48`, inside the ruling-3 paragraph.

**Ground truth.** The paragraph says three things in order:

1. `:45` — *"a `HarnessIssue` is not the reviewer's to file **mid-run**"*. Correct, and it is
   what the schema constrains: `observed_after` is *"the terminal status the run had reached
   when this **was recorded**"*.
2. `:46`–`:48` — *"so an issue claiming a **mid-run observation** is unrepresentable"*. The
   subject has shifted from *filing* to *observing*.
3. `:50` — *"a `HarnessIssue` filed **after the run** by whoever **observed it**"*.

Taken at its word, (2) bars (3) in exactly the case the paragraph exists for: an observation
made during a review, which is mid-run by construction. The schema's own field description
carries the same looseness, so the candidate inherited it rather than invented it — but the
candidate is the first text to put the loose clause next to a route that depends on the strict
reading.

**Why it is low and not a blocker.** The reviewer's own action is unambiguous — *"Record it as
an observation finding in your own review record"* — and (1) scopes the bar correctly. What is
at risk is the second of two routes at closeout, and the orchestrator reading it has (3) in the
same paragraph and the schema one file away. Nothing is unrecoverable.

**Minimum fix, bytes supplied.** At `:47`–`:48`, replace

> so an issue claiming a mid-run observation is unrepresentable

with

> so an issue recorded while the run is still in flight is unrepresentable

which is what `observed_after` actually constrains and leaves `:50` reachable.

### `L-4` (low) — `ORCHESTRATION.md` re-types the bound in the same sentence that says it does not

**Location.** `document-harness/ORCHESTRATION.md:80`–`:84`.

**Ground truth.** The sentence reads *"What may legitimately sit in a plan rather than in the
instruction is `EXECUTION.md`'s Instruction authoring rules to state — **instruction first,
the plan channel taking only what the instruction cannot carry** — and this file does not
re-type it."* The em-dash clause is a compression of `EXECUTION.md:462` (*"Instruction first:
the plan channel is overflow, never a second instruction"*) and `:467` (*"The plans take only
what the instruction cannot"*). This file's own opening states the design it breaks: *"this
file names the owner and points at the rule rather than restating it. `HD-5` records
transcription as a drift surface, so a second copy of a rule is a second thing that has to
stay true."*

**Why it is worth a row rather than nothing.** The gloss drops the operative half — the
enumeration of *what* the plans may take (conduct prose; cross-run standing discipline) — so it
is a copy that is both incomplete and, if `EXECUTION.md`'s bullet is ever narrowed, silently
stale. That is `HD-5`'s failure mode arriving on the day the sentence was written.

**Why it is low.** The two texts agree today, and the pointer is right there, so no actor is
misled now.

**Minimum fix, bytes supplied.** Delete the em-dash clause:

> What may legitimately sit in a plan rather than in the instruction is
> [EXECUTION.md](EXECUTION.md)'s *Instruction authoring rules* to state, and this file does
> not re-type it.

### `L-5` (low) — `HD-46`'s rationale still writes the merged form as today's shape, and the flip retired the only thing tracking it

**Location.** `HARNESS-DECISIONS.md:291`, inside `HD-46`'s *「本条留下的 tiebreak，如实记」*
paragraph: *"它直接作用于今天的实际形态——一个 session 同时持 orchestrator 与 executor 两个角色"*.

**Ground truth.** `HD-55`'s **own pre-round status line**, which this commit rewrote, named
exactly two sites still writing the merged form as an ordinary daily shape: *"`E1` 中间态披露句
与 `HD-46` 的中间态 tiebreak 理由段"*. The round closed `E1`, added the home, and closed
`ORCHESTRATION.md`'s may-never-do bullet — three sites, none of them `HD-46`. The `HD-46`
clause is unedited, in the very file this commit was editing, about 145 lines from the entry it
was rewriting.

**Two things follow, and the second is the reason this is a row.** First, `HD-46` is now the
only place in the repository that states the merged form as current. Second, `HD-55` moved to
§implemented in the same commit, and §implemented is *"不必读"* — so the entry that was
tracking this residue (*"剩余「层内落一句」由本条 status 行追踪"*) has left the mandatory read
path, and nothing else names the site.

**On the round's own account of the site list.** The new status line's *"本条原 status 行只点
了两站"* is defensible read as *the two carrier candidates the flip condition offered* (`E1` or
the three-roles table), which the original did name. I do not read it as a false statement.
The finding is the untracked residue, not the sentence.

**Why it is low and not a blocker.** The operative rule is carried correctly at three sites,
one of which — `E1` — is on every construction round's mandatory reading path and now says
plainly that taking the channel *"is now a deviation to account for rather than a shape to
disclose"*. A round in the middle reads `E1` before it greps `HD-46`. The class scan could not
have caught this: its declared scope is the ten `E10` members, and the decision log is not one
(`HD-19`).

**Minimum fix, bytes supplied.** At `:290`–`:291`, replace *"它直接作用于今天的实际形态"* with
*"它直接作用于当时的实际形态"*, and append after the clause: *"——该形态自 `HD-55`（2026-08-22）
起不再是常规，只余 `E1` 的例外通道"*. `HARNESS-DECISIONS.md` is neither `E2`-frozen nor an
`E10` member, so no freeze or membership rule reaches these bytes; `HD-7` makes the file pure
discipline.

### `O-1` (observation) — a third stale reference to a deleted rider, outside the declared scan range and outside the candidate's boundary

`CONSTRUCTION-LEDGER.md:79` reads *"`HI-route` 未闭：重扎根这条裁决同样只活在 commit 正文/台账/
本行"*. `HI-route` is deleted by this commit and its question answered by ruling 3, so the
premise is false at the tip. This is the same defect shape the round found in `io-design.md`
and banked as `io-hiroute-stale` — a dangling pointer to a deleted rider plus an answered
question written as unanswered.

Two reasons this is an observation and not a finding against the candidate. The class-4 scan
declares its range in the same sentence as its result (*"across the bank, the decision log, the
ten members and io-design.md"*), so `HD-41` ① is satisfied and *"two live references remained"*
is not over-claimed. And the plan puts `CONSTRUCTION-LEDGER.md` at closeout, orchestrator's,
not the candidate's — the executor could not have fixed it inside its boundary.

**Recorded for the closeout that will write that file anyway**, where the fix costs nothing.
Whether the scan's range should have included the ledger — a surface the round's own rulings
bear on — is a scoping judgement, and `R5` puts it to the user rather than to me.

### `O-2` (observation) — the seventh operation, and what it does to the round's independence claim

The plan's change surface enumerates six operations on `HARNESS-RIDERS.md`; the commit performs
seven, adding row `io-hiroute-stale`. **The candidate discloses this in its own body, in the
row's own source column, and offers the reversal** (*"用户可一行划掉"*). That is what `E8` and
`E9` ask of a boundary widening — said, never silent — and the ground it gives is real: I
verified `io-design.md:100` and `HD-35`'s blob binding myself, and leaving the finding in the
executor's report only is the defect `R2` names. Correctly handled; the accept-or-strike call
is the user's, exactly as the row asks.

What I record beside it is a tension the same body creates. It states, *for the first time as
structural*, that the executor held **none** of `R1`'s four holdings, one of which is *scoped
by*. A round that widens its own change surface has taken a share of its own scoping — a small
and fully-disclosed share, and I do not read it as making the executor the scoper. But all four
holdings are process claims about sessions, and **none of them is verifiable from the
repository** (`R4`): the git identity is the same on every commit in this history, and I mark
the four rather than confirming them. The body's own boundary sentence — that what is
established is the authoring configuration, not any review's — is the honest half and is
accurate.

### `O-3` (observation) — the new rider row's quotation of a signed file is inexact

`HARNESS-RIDERS.md:45` presents `io-design.md:100` in quotation marks as *「**窗口**的未解问题
仍挂在 rider `HI-route`，不因本设计关闭」*. The signed line reads *「其**路由与 `observed_after`
窗口**的未解问题仍挂在 rider `HI-route`，不因本设计关闭」*. The quotation drops *路由与* and the
`observed_after` qualifier while keeping quotation marks around the remainder.

Immaterial to the row's substance — both halves it names are the two ruling 3 addresses, and
routing is if anything the half more clearly closed. Recorded because the row's whole value is
as a pointer into a signed file that may not be edited, and a pointer whose quotation does not
match the bytes is worth one line to a later reader holding both open.

### `O-4` (observation) — two rationale clauses that generalize further than the round's own case supports

Neither changes any obligation; both are recorded so a later reader is not surprised.

- `ORCHESTRATION.md:78`–`:80` gives as the second reason for delivering the plans that *"they
  are the caller's extension point on the work side"*. True of a product run. **This round's own
  governing plan, `document-harness/plans/prerun-riders.plan.md`, lives in this repository and
  is the orchestrator's, not the caller's** — and the Handing section governs both dispatch
  modes, naming `--executor` and `--construction-executor` in the same paragraph. The delivery
  obligation is stated broadly enough (*"governing plans"*) that nothing breaks; the rationale
  is narrower than the rule it justifies.
- `REVIEW.md:38` calls the new thin-check finding *"the exact mirror"* of *The `review_only`
  question*. The mirror sentence at `:276` carries an explicit *"not a blocker, unless it
  violates an obligation, an invariant or the contract"*; the new one carries no such
  qualifier. `:296` governs both, so the omission changes no outcome — but *exact* is stronger
  than the pair of texts is.

---

## 4. Routing, stated without adjudicating it

`R10` routes findings by the 2026-07-29 ruling, and the tier does not change the route. Four
of the five lows supply exact bytes or name the content, which puts them at the junction rider
`wl-route` records as unresolved — `E10`'s free channel says *applied immediately*, `R9` says
*rides the next batch*, and two readings of equal textual strength diverge on timing. **I do not
resolve it**, per that row's own construction; I note that my record is a FULL and not a read,
so `wl-route`'s deadline — *"下一份对 wording-level finding 供字节的 read 记录"* — is not
reached by this document.

What is decidable and worth stating:

- `L-3` and `L-4` sit on `E10` members. No round has *relied* on either clause in `E10`'s sense
  — this round authored them, and authoring is expressly not relying — so **the free channel is
  open for both**, at the cost of the per-member digest in the next layer read.
- `L-5` sits on `HARNESS-DECISIONS.md`, which is not an `E10` member (`HD-19`) and not
  `E2`-frozen. No layer machinery reaches it.
- `L-1` and `L-2` have no appliable bytes: their carrier is an immutable commit body. Errata or
  bank.
- `O-1` redeems at the closeout that touches `CONSTRUCTION-LEDGER.md` regardless.
- None of the five is on a path `E2` freezes, so `HD-20` does not bank anything here.

---

## 5. Coverage — read in full, sampled, only probed (`R4`)

**Read in full at the subject:** `document-harness/CONSTRUCTION-CHECKLIST.md`,
`document-harness/ORCHESTRATION.md`, `document-harness/REVIEW.md`,
`document-harness/plans/prerun-riders.plan.md`, `migration/document-work-assurance-v3/v3-harness-review-contract.md`,
the complete diff of all six changed paths, and the whole commit body.

**Read in part:** `document-harness/EXECUTION.md` — `:415`–`:494` in full, the rest reached
only by targeted grep. `HARNESS-DECISIONS.md` — §live and §implemented boundaries by
enumeration, `HD-2`–`HD-7`, `HD-19`, `HD-46`, and the `HD-55` entry diffed line by line; the
other entries not read. `HARNESS-RIDERS.md` — the full diff plus every row's id and source
column, parsed; most row bodies not read end to end. `CONSTRUCTION-LEDGER.md` — `:53`–`:90`
plus grep hits. `migration/document-work-assurance-v3/v3-cold-read-3a6a10b.md` — the outline
and §4 findings; §1–§3 and §5 not read.

**Probed only:** `tooling/hooks/layer_path_check.py` (read in full and executed);
`tooling/rsclib/document_harness/dispatch.py` (the five prompt constants and the charter
constants); `tooling/rsclib/document_harness/instruction.py` (`_NORMATIVE_MARKERS` and
`_is_context_title`); `schema/document-assurance-v3/harness-issue.schema.json` (`:38`–`:50`);
`document-harness/io-design.md` (`:95`–`:105`); `document-harness/README.md` (grep only);
`document-harness/plans/executor-charter.plan.md` (`:75`–`:100`, `:248`–`:262`).

**Not opened:** the two contract supersessions, the operating-contract stub,
`schema/document-assurance-v3/paragraph-map.schema.json`, and every other review record. This
is a FULL, not an `E10` read, so no per-member blob table is owed and none was built beyond the
six changed paths.

**Re-executed here, not accepted as reported:** the battery (790 passed), `layer_path_check`
replayed over the commit's added lines, all four class scans, the 16 markdown-link resolutions,
the rider-bank census, the §live entry count, the `HD-55` entry diff, the numstat, and the four
`E3` blob and schema assertions.

**Process claims marked, never verified.** The `E1` four-holdings disclosure; that the executor
started cold; that `dtw dispatch --construction-executor` was the dispatch path; the preview
card and the user's approval of the plan (`E11`, `R7` ceiling stated in §1); `HD-55`'s own
cold-start measurement, which its entry already marks as living only in a conversation; and the
`mark-case` evidence figures, whose subjects are caller-held and absent from this tree.
