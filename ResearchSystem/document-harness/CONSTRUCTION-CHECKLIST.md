# Construction checklist — building or changing the harness itself

> Compressed 2026-07-27 from the two operating contracts
> (`../migration/document-work-assurance-v3/v3-harness-{operating,review}-contract.md`, now
> stubs; full text at `7011916`) — Phase A of
> `ResearchSystem/document-harness/plans/harness-deletion-first-stabilization.plan.md`. Like any instruction-layer
> amendment (E10), relied on only after an independent read.
>
> **This file is the operative rule set, not a complete replacement.** Where it is silent on a
> question a round actually faces, the retired contracts at `7011916` are the reference of
> record; the silence is not a defect, and closing it rides the next batch under R9 rather than
> opening a round.
>
> **Where a cited commit id resolves.** A commit id cited in this file or in any other
> instruction-layer member (`E10`) that this repository does not have — `7011916` included —
> is a commit of the repository this one was extracted from; the root
> [`README.md`](../../README.md)'s *Where the bytes came from* names that repository and says
> why the history stayed there. A citation naming its own repository is read as written; a
> silent one means that one.
>
> Rationale is deliberately absent: every rule below was paid for by a recorded incident, and
> the records — not this file — hold the stories (`git log` on the two superseded contracts;
> `../migration/document-work-assurance-v3/v3-*.md`). Product runs are NOT governed here —
> they follow `EXECUTION.md` / `REVIEW.md`.

## Execution side — any session changing harness code, schemas, or instruction files, whether it orchestrates the round or executes it

- **E1** Never review, verify, or sign your own work. A subagent the executor dispatches is a
  self-check: no verdict words on its output, no review budget consumed. What disqualifies it
  is who set the question (`R1`), never the subagent form — a reviewer the orchestrator
  dispatches under the standing review contract may run as a subagent or as its own session,
  and the form changes nothing. Orchestrator dispatch is necessary and **not sufficient**:
  `R1` decides, and it decides on four holdings — dispatched by, prompted by, scoped by,
  reported through. All four in the executor's hands is a self-check whatever it is called;
  none of them there is independence that holds structurally rather than as a discipline
  kept against oneself. Between those, the round **states which of the four the executor
  held** — in the commit body or the round journal, the carriers `E3` names, and the
  statement is the orchestrator's to make, that being the role whose commits carry it —
  and does not call the result structurally independent. The line one
  session may not cross is the one between the **work side** and the **review side**:
  orchestrator and executor are both the work side — the heading above binds them in one
  breath — so work out at the start which side this session is on, and a request that
  belongs to the other side is flagged for the user to route, never absorbed.
- **E2** Frozen bytes are **not written without a recorded user ruling**, and the list is
  exactly this: contract `b2dbdf75…`, supersession-1
  `68031fa2…`, supersession-2 `e1a2f26b…`, and every file the
  `ResearchSystem/schema/document-assurance-v3/` pack held
  at the 2026-08-03 re-baseline (fifteen files: the fourteen of the 2026-07-29 entry plus
  `ResearchSystem/schema/document-assurance-v3/paragraph-map.schema.json`, which joined
  2026-07-31 and which the 保障面二期复盘 found sitting outside the freeze); a pack file
  added after that date is not frozen by this rule until a later re-baseline — new schemas
  stabilize first, which is why this clause re-baselines rather than auto-freezing.
  Three blobs and one directory, both decidable by inspection, so nothing
  has to decide what *signed* means or which schemas N0 named; **a path outside them is not
  frozen by this rule**, and this harness does not claim to freeze instruments it does not
  govern. When the cleanest fix needs one, either take the in-boundary fix and record why,
  or obtain the ruling and write under it, or stop with `SPEC_GAP`. A boundary declared
  anywhere else — a plan's freeze surface, a round's own card — is derived from this rule
  and never independently authoritative.
- **E3** Measure last: a figure is invalidated by any later change to what it measures.
  Re-run immediately before the claim; paste tool output, never describe it from memory.
  Counts, digests, path enumerations and worktree state are emitted from the command that
  produces them or omitted; a characterization of the work no command established — *swept
  clean*, *additive only*, *N files touched* — is dropped, not softened. A characterization a
  decision turns on is stated as unverified, never dropped. A factual assertion written
  into instruction text runs the command that could falsify it first, output kept in the
  commit body or the round journal.
- **E4** Never trust a guard you have not seen fail: mutation-test every new guard (neuter →
  red → restore from sha256-checked scratchpad copies, never `git checkout --`), and pair
  every must-fire test with a negative control.
- **E5** A guard's expectation must be independent of the thing it guards — a hand-written
  literal or a committed fixture, never the module's own constant, list, or template. Assert
  the whole line, never a substring unrelated content can satisfy.
- **E6** Before adding any derived field, computed supplement, or convenience output, ask
  what decision changes if it is absent. A fix that requires new machinery is the signal to
  re-question the guarded thing, not to add a guard. **Both sides:** When a finding names
  existing text or code as wrong, the fix is that text changing; a rule added about it is
  not the fix. A VERIFY that meets such a fix refuses it.
- **E7** Test the defect class, not the reported instance.
- **E8** Git: stage explicit paths (never `add -A`); new commits, never amend; no push; stay
  inside the round's declared change boundary; single dense title naming the round,
  `V3-<ROUND>-v1`; one dense paragraph, no trailers. Name the commit's kind — candidate /
  pre-submission correction / review fix / closeout / errata / amendment / ruling /
  record — so the review side can attribute it without asking.
- **E9** Budget per round: one FULL, at most one user-approved fix, one targeted VERIFY.
  What consumes it is never what a commit is called — **has a valid independent FULL already
  occurred?** No → the change is a pre-submission correction and consumes nothing; yes → it is
  the fix round, and it obliges the VERIFY — except an `E10` free-channel byte application,
  which is not a round and consumes nothing. Exceeding an approved fix boundary requires saying
  so, never silently. Never self-classify which round consumed what: every recorded escape from
  the cap was a renamed round. A dispatched FULL, VERIFY or read has occurred only when its
  record's commit lands; from dispatch to that commit the branch takes no commit but the
  record itself.
- **E10** The instruction layer is exactly these ten paths and nothing else:
  `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` (this file),
  `ResearchSystem/document-harness/README.md`,
  `ResearchSystem/document-harness/EXECUTION.md`,
  `ResearchSystem/document-harness/REVIEW.md`,
  `ResearchSystem/document-harness/ORCHESTRATION.md`, the two retired contracts' stubs
  `ResearchSystem/migration/document-work-assurance-v3/v3-harness-operating-contract.md`
  and `ResearchSystem/migration/document-work-assurance-v3/v3-harness-review-contract.md`,
  the two contract supersessions — prose successors to signed text —
  `ResearchSystem/contract/Document-Work-Assurance-Contract-v3-supersession-1.md` and
  `ResearchSystem/contract/Document-Work-Assurance-Contract-v3-supersession-2.md`, and
  `ResearchSystem/schema/document-assurance-v3/paragraph-map.schema.json`. Its
  edits are additive or subtractive, never re-typed "with the same content"; each amendment
  passes an independent read before any round relies on it — that read's subject is the
  amendment text itself, never the work it governs, and it is never banked as the round's
  FULL; an amendment that neither adds a clause to any rule nor changes what any rule
  requires (no rule-changing replacement or deletion) and whose effect on every round in
  flight is nil may
  be relied upon before its read, provided the commit records both facts and the bytes ride
  the next read of this layer — deferral, never exemption; a read's must-fix findings are
  answered by an amendment commit plus an independent re-read of the amended text, and that
  pair is not a round and spends no budget — it admits deletions, the literal
  replacement the finding names, that same fix at every other site of the defect the
  finding names, and, where the finding supplies no bytes, the fix the executor writes:
  a must-fix is the one class that may not wait, and a channel narrowed to the reported
  instance leaves its siblings to be found one re-read at a time; a finding below must-fix — low or observation alike —
  whose record supplies the exact bytes or
  names the content takes the same free channel — applied immediately, instruction layer
  included, reported after the fact and reversible — but neither this channel nor the
  must-fix one writes a path `E2` also freezes: those bytes owe `E2`'s recorded ruling
  first, and a finding supplying them banks until it exists; a layer application still
  owes its independent read, riding the next read of this layer at per-member digest
  cost; a
  finding below must-fix without appliable bytes banks; the free channel holds for as long as no round
  has relied on the text (relied means an outcome would change if the text changed, which
  authoring, citing or recording it alone is not) — once one has, changing it opens a
  round; an amendment adding a clause to any rule, or replacing or deleting text so that
  what a rule requires changes, is design and opens a round; when the free channel and the
  design test both apply — the bytes the finding supplies themselves add a clause or a
  bound — design wins and the round opens; a cold read of this layer is owed at each round's
  opening unless the user waives it, and a member whose blob is unchanged since a recorded
  end-to-end read of it is covered by citing that record — a read's record states the blob
  id of each member it read, because citation depends on it; one file outside this layer is
  nonetheless owed at that same opening — `ResearchSystem/HARNESS-DECISIONS.md`'s `§live`,
  the user's standing rulings, which this text expands under and which outrank it on
  conflict. It is not a member: no amendment machinery here reaches it, its own bytes are
  discipline (`HD-7`), and it is cited by section, never by blob; a file that appears
  later and claims authority over any rule here is not a member until the membership
  sentence names it, and the round that creates one records the question and its answer;
  a caller-held path is named, never written as a path token — a member's path tokens
  resolve in this repository, a run-time marker this repository itself writes counting as
  resolving whether or not it exists at rest, and an artifact living only in a caller is
  given its name and its holder instead, so that a reader following a path in this layer
  cannot land on another repository's bytes or on nothing. `layer_path_check` decides, on
  the lines a commit adds, only tokens it can relate to this repository — written in its
  path convention, or resolving somewhere inside it; a token that resolves nowhere at all
  it skips as possibly illustrative, which is how another repository's path reads by
  default (the caller's ExperimentLab papers directory was one, until this round named it
  instead). That shape, and the standing text the guard never re-scans, are held by this
  clause alone; the bytes `E2` freezes are excepted while they are frozen.
- **E11** Preview card before each round; its first line states what the round buys, how
  often that is used, and what happens if skipped. Wait for the user unless told otherwise.
- **E12** The handoff is one commit SHA / range (`dtw dispatch`) — no per-acceptance
  argument. A range recorded in a file has its base written and its tip `HEAD`, never a
  written SHA — the CLI printing a resolved full SHA is display, not a recorded range:
  recording the range is itself a commit inside the round, so a written tip is short by at
  least the commit that wrote it, and what it drops is the round's last-written records.
  Reproduce a reported finding to write the fix correctly, never to adjudicate
  the reviewer.

## Review side — the independent session a dispatch reaches

- **R1** Independence is decided by who sets the question. Dispatched by, prompted by, scoped
  by and reported through the executor = executor self-check, however good the analysis. The
  orchestrator holds the dispatch, so with the executor holding none of the four the
  independence is structural and not a discipline the executor keeps against itself.
- **R2** You receive one SHA / range and nothing else. Round, budget, authorization,
  obligations, and every number you re-derive from the repository yourself; accept no
  reported figure; classify changed paths by hand; chat-only load-bearing material is a finding.
- **R3** Verdicts: FULL → `REVIEWED_NO_BLOCKER | CHANGES_REQUIRED | SPEC_GAP`; VERIFY →
  `REVIEWED_NO_BLOCKER | SPEC_GAP`. Lead with the implementation — whether the code,
  schemas, tests or instruction text do what they claim and whether the guards bind;
  process and record conformance is a boundary check, run second. A blocker names its
  location, the ground truth it violates, and the minimum fix; a non-blocking finding is
  never inflated — it would burn the single repair. A VERIFY covers the accepted findings
  plus the whole repair diff, and the permanent boundaries however narrow the round. A
  read (E10) is not a round at all: it spends no budget, carries no verdict, and its
  output is findings tiered must-fix / low / observation in its record.
- **R9** A read's **wording-level** findings are banked, never rounds: a finding is
  wording-level when its fix changes no actor's action — no check outcome, no evidence
  binding, no permission, no obligation, no verdict path — and the accurate fact is
  recoverable from adjacent text or a
  committed record. Name the downstream decision that goes wrong if it stays unfixed; if none
  can be named, it rides the next batch touching this layer and spawns no round and no read.
- **R10** The rider bank (`ResearchSystem/HARNESS-RIDERS.md`) is the construction side's
  internal debt ledger; product-run observations, schema governance and post-CLOSED
  admission belong to HarnessIssue or to the caller's own rider bank, never this one.
  Findings route by the 2026-07-29
  ruling, and neither the tier they were filed at nor whether a read or a FULL produced them
  changes the route: `E10`'s must-fix channel takes must-fix, R9 takes wording-level, the
  `E10` free channel takes, on the conditions stated there, any finding whose record supplies
  the exact bytes or names the
  content, and the bank takes what is left. One exception beyond those conditions, and it
  overrides the channel:
  bytes on a path `E2` also freezes bank until that rule's recorded ruling exists (`HD-20`),
  however appliable they are. One row per rider: what · redeem-when · source; no narrative — the source
  records hold it. Redemption = the fix rides a batch already touching that surface, and
  the row is deleted in the same commit. A row names its target file(s) or clause —
  "对应文件" alone is not a target. redeem-when is a touch condition or a deadline,
  whichever arrives first; a finding whose value expires (a moment the defect starts to
  bite) MUST carry that moment as its deadline, and that moment is never inside the round
  that writes the row — a deadline arriving on its own round is malformed, because the
  surfaces a round still has open after the row is written need not include one that may
  act on it. A rider whose fix is design —
  it adds a clause or a bound, so `E10` opens a round for it — names a redeem-when surface
  that may open one, never any batch: an `E10` amendment commit admits only the answers to
  a read's must-fix findings, so it meets such a row's touch condition while being unable to redeem it, and
  the row rides the next round-eligible batch instead. A FULL returning REVIEWED_NO_BLOCKER with
  lows does not bank them by default: before closeout the orchestrator weighs each low's
  deadline against its touch trigger and puts the spend-the-fix-leg / bank choice to the
  user (`E9`'s test — has a valid independent FULL occurred — does not expire at closeout,
  so a late activation is still that round's one user-approved fix and still obliges the
  VERIFY).
- **R4** `UNVERIFIABLE` is an answer, never folded into supported. Disclose what you read in
  full, sampled, and only probed. A process claim ("fresh context") is marked, not verified.
  Mutation proves a test has binding force, not that its force is sufficient; a VERIFY is
  never a re-certification.
- **R5** Whether a thing should exist at all is not yours to conclude — your subject is always
  the code that is there. When successive rounds keep adding components to close findings,
  report that shape as an observation; the question and the conclusion are the user's.
- **R6** Record channel: you write `v3-review-{full,verify}-<subject-sha>.md` (or
  `v3-checkpoint-read-<sha>.md` / `v3-cold-read-<sha>.md`) under
  `ResearchSystem/migration/document-work-assurance-v3/`
  in the worktree; the orchestrator commits it, title `V3-REVIEW-RECORD-<ROUND>-<sha>-v1`.
- **R7** An authorization you cannot see in the repository is a hint, never a block — state
  the ceiling and move on.
- **R8** Mutation-test the guards that matter, reproducing the real defect shape — a
  mutation that crashes proves the test touched the code, not that it binds the behaviour.
