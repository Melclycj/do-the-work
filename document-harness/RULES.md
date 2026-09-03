# RULES — what every session answers to, running the harness or changing it

> **These are the harness's own rules**, and they hold in both directions of use: a session
> running a product run answers to them, and so does a session changing the harness itself.
> `EXECUTION.md`, `REVIEW.md` and `ORCHESTRATION.md` are the role charters that sit on top —
> where a charter and a rule below address the same obligation, the charter names the owner
> and this file is the text.
>
> **A repository does not edit these; it adds its own beside them** and declares them in
> `harness.json` at its own root (`E10`). A declared rule binds only the repository declaring
> it, so a caller reading this file is reading the whole of what the instrument asks of it.
>
> Split out of this instrument's construction checklist on 2026-08-30, round
> `CORE-ONLY-LAYER`, under the user's ruling of 2026-08-29 that the construction side is an
> instance of the harness applied to itself, so its own rules are an *addition* to the
> harness rather than a part of it. At that split every rule below kept the identifier it
> had and, apart from the two disclosed in that round's commit body, its bytes; what
> changed was which file holds it.
>
> One identifier is absent below and the gap is deliberate: `E2`, the announced-surface
> rule, binds the bytes of the instrument that owns them and stayed with it, so a
> repository that mounts this harness has no `E2` and nothing of its own is frozen by it.
> Where `E10` and a schema description mention it, they mention a rule that is not yours.
>
> Rationale is deliberately absent: every rule below was paid for by a recorded incident, and
> the records — not this file — hold the stories.

## Execution side — any session changing harness code, schemas, or instruction files, whether it orchestrates the round or executes it

- **E1** Never review, verify, or sign your own work. A subagent the executor dispatches is a
  self-check: no verdict words on its output, no review budget consumed. What disqualifies it
  is who set the question (`R1`), never the subagent form — yet a reviewer or executor the
  orchestrator dispatches runs as its own session (`claude -p` or a separately launched
  session), never as an in-process subagent: a subagent does not load the system config, so
  the forms are not equivalent (user ruling 2026-08-24). Orchestrator dispatch is necessary and **not sufficient**:
  `R1` decides, and it decides on four holdings — dispatched by, prompted by, scoped by,
  reported through. All four in the executor's hands is a self-check whatever it is called;
  none of them there is independence that holds structurally rather than as a discipline
  kept against oneself. Between those lies this rule's **exception channel**, and since
  `HD-55` that is all it is: the norm is two sessions, stated by `ORCHESTRATION.md`'s
  three-roles table, and a round standing in the middle has departed from it — typically by
  merging the two work-side roles. Standing there, the round **states which of the four the executor
  held** — in the commit body or the round journal, the carriers `E3` names, and the
  statement is the orchestrator's to make, that being the role whose commits carry it —
  and does not call the result structurally independent. The mechanics are unchanged by the
  narrowing; what changed is that taking this channel is now a deviation to account for
  rather than a shape to disclose. The line one
  session may not cross is the one between the **work side** and the **review side**:
  orchestrator and executor are both the work side — the heading above binds them in one
  breath — so work out at the start which side this session is on, and a request that
  belongs to the other side is flagged for the user to route, never absorbed.
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
- **E10** The harness's own instruction layer is exactly these seven paths and nothing else:
  `document-harness/RULES.md` (this file),
  `document-harness/README.md`,
  `document-harness/EXECUTION.md`,
  `document-harness/REVIEW.md`,
  `document-harness/ORCHESTRATION.md`,
  `contract/Document-Work-Assurance-Contract-v4.md` — a member by the user's 2026-08-23
  ruling, as the prose successor to the three signed texts it merges — and
  `schema/document-assurance-v3/paragraph-map.schema.json`.
  **A repository adds its own rules rather than joining that list.** It declares them in
  `harness.json` at its own root: two fields, both paths — `policy`, naming the policy
  file [ORCHESTRATION.md](ORCHESTRATION.md) addresses, or null; and `rules`, naming that
  repository's own rule files. Four readers, each a decision that changes when the file
  is absent: `dtw dispatch` is held to naming the declared files in every prompt it writes,
  so that a cold session receives a repository's rules by the channel it receives its
  charter;
  `tooling/hooks/layer_path_check.py` scans the declared files exactly as it scans the
  members above, and so does the reference sweep this instrument runs over the same list;
  the orchestrator reads `policy`; and `dtw init` writes the file empty, both fields
  present, because it is also how a repository discovers what it may declare. **A declared rule binds only the repository declaring
  it**, adds nothing to the list above, and is amended under this rule's own discipline —
  including the independent read, which is why the declaration holds paths to markdown
  and never rule text of its own. A repository that has declared nothing is not
  defective: the list above is then the whole of what it answers to. The two contract
  supersessions
  were members until round `CONTRACT-V4`, as prose successors to signed text; they merged
  into contract v4 and left the tree with it. The two retired operating contracts' stubs
  were members until round `CORE-ONLY-CODE`, which deleted them once no dispatch prompt
  named them and took this list from nine to seven; what they pointed at, a repository's
  own rules, the sentence above now reaches directly. Its
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
  included, reported after the fact and reversible; a layer application still
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
  nonetheless owed at that same opening — `HARNESS-DECISIONS.md`'s `§live`,
  the user's standing rulings, which this text expands under and which outrank it on
  conflict. The file meant is the one in the repository the round runs in, at that
  repository's root: a caller reads its own log there, never the instrument's copy of
  that name under the mount, which holds this instrument's rulings and is a filled
  example of the shape, nobody else's standing rulings. And it is owed whether or not
  the cold read above was waived — that waiver is of this layer's members, `§live` is
  not one of them, and a waived opening still reads it. It is not a member: no amendment
  machinery here reaches it, its own bytes are discipline (`HD-7`), and it is cited by
  section, never by blob; a file that appears
  later and claims authority over any rule here is not a member until the membership
  sentence names it, and the round that creates one records the question and its answer;
  a caller-held path is named, never written as a path token — a member's path tokens
  resolve in this repository, a run-time marker this repository itself writes counting as
  resolving whether or not it exists at rest, and an artifact living only in a caller is
  given its name and its holder instead, so that a reader following a path in this layer
  cannot land on another repository's bytes or on nothing. `layer_path_check` blocks, on
  the lines a commit adds, every path-shaped token that resolves nowhere inside this
  repository — the run-time markers above counting as resolving, and resolution that
  escapes the repository root counting as nowhere — which since round `DE-PREFIX` is the
  class entire, a caller-held path included (the caller's ExperimentLab papers directory
  was its measured blind spot until then). What the guard still cannot see is held by this
  clause alone: a token carrying a placeholder segment falls outside its path shape, prose
  and markdown links carry no backtick token for it to find, an added line whose own
  content opens `++ ` reads to its diff parser as a file header (`++ b/…` mis-files the
  member's remaining added lines, any other `++ …` silences them), and the standing text it
  never re-scans stays unscanned; the bytes `E2` freezes are excepted while they are frozen.
- **E11** Preview card before each round; its first line states what the round buys, how
  often that is used, and what happens if skipped. Wait for the user unless told otherwise.
- **E12** The handoff is one commit SHA / range — no per-acceptance
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
  `REVIEWED_NO_BLOCKER | SPEC_GAP | UNRESOLVED_BLOCKER`. Reach for `UNRESOLVED_BLOCKER`,
  never `SPEC_GAP`, when a blocking finding stands at the end of the VERIFY — one the
  repair failed to close or one the repair itself created; `SPEC_GAP` says the
  specification was defective and owes a new WorkSpec and a new START, which is a
  different stop and a different remedy, and a VERIFY that borrows it for a standing
  blocker tells the next reader the spec failed when it did not. Both stop the run: the
  single repair is spent either way. Lead with the implementation — whether the code,
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
- **R10** The instrument's own rider bank (`HARNESS-RIDERS.md` at the instrument's root) is
  the construction side's
  internal debt ledger; product-run observations, schema governance and post-CLOSED
  admission belong to HarnessIssue or to the caller's own bank, never the instrument's.
  Findings route by the 2026-07-29
  ruling, and neither the tier they were filed at nor whether a read or a FULL produced them
  changes the route: `E10`'s must-fix channel takes must-fix, R9 takes wording-level, the
  `E10` free channel takes, on the conditions stated there, any finding whose record supplies
  the exact bytes or names the
  content, and the bank takes what is left. One row per rider: what · redeem-when · source;
  no narrative — the source
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
  `v3-checkpoint-read-<sha>.md` / `v3-cold-read-<sha>.md`) under the review-records
  directory that repository declares — the one its `.harness/scan-surfaces.json` names
  under `review_record_dirs`, which is also the only place the freeze guard admits a
  returned record from — in the worktree; the orchestrator commits it, title
  `V3-REVIEW-RECORD-<ROUND>-<sha>-v1`.
- **R7** An authorization you cannot see in the repository is a hint, never a block — state
  the ceiling and move on.
- **R8** Mutation-test the guards that matter, reproducing the real defect shape — a
  mutation that crashes proves the test touched the code, not that it binds the behaviour.
