# ORCHESTRATION — what the orchestrator owns, and what it may never decide

Role instructions for the **orchestrator**: the session that runs the round: transport,
budget and the review window. Its counterparts are [EXECUTION.md](EXECUTION.md), which addresses the
executor of a product run, and [REVIEW.md](REVIEW.md), which addresses the reviewer one
dispatch reaches. The construction-side rules both sides answer to are
[CONSTRUCTION-CHECKLIST.md](CONSTRUCTION-CHECKLIST.md), and its *Execution side* heading
already binds this role by name — "any session changing harness code, schemas, or instruction
files, whether it orchestrates the round or executes it".

**This file is deliberately thin, and that is the design.** Most of what the orchestrator owes
is already written in this layer; this file names the owner and points at the rule rather than
restating it. `HD-5` records transcription as a drift surface, so a second copy of a rule is a
second thing that has to stay true. Where a line below cites a rule, **that rule is the
text**. Three obligations had no text anywhere in this layer before this file existed; those
are written out.

## The three roles

| role | what it does | carrier |
|---|---|---|
| **orchestrator** | transport and flow: starts the executor, dispatches the reviewer, keeps the budget and the review window, takes questions to the user | a full session — the one the user is talking to |
| **executor** | takes the instruction, decomposes it, does the work, produces the candidate | a full session |
| **reviewer** | starts cold from one dispatch, works alone, writes the record | a full session **or** a subagent — what decides independence is who set the question (`R1`), not the form |

**Independent is the norm; one session holding both work-side roles is the exception.** This
sentence is the layer's carrier for the 2026-08-22 ruling `HD-55`, and it belongs to this table
because the table's subject is which session carries which role. The carrier column already read
two full sessions before that ruling; what the ruling settles is that they are also two sessions
*in fact* — the orchestrator dispatches a cold executor rather than becoming one, since two roles
that see the same context are two names for one role. A round that merges them is a deviation,
disclosed through `E1`'s exception channel, and the disclosure mechanics are `E1`'s to state.

Why this role had no charter until now: the **reviewer, the reader and — since round
`EXECUTOR-CHARTER` (2026-08-22 ruling) — the executor** start cold, so something must hand
each its charter at startup, and `dtw dispatch` does: three review-side modes, and two
executor-side modes, one per side of the work — the product-run executor's charter is
[EXECUTION.md](EXECUTION.md), the construction-round executor's is
[CONSTRUCTION-CHECKLIST.md](CONSTRUCTION-CHECKLIST.md), whose *Execution side* heading
already binds that role by name, and what each mode may emit is the dispatch module's to
state, not this file's. The orchestrator is the session already in the conversation, so
nothing ever had to hand it a file. Nothing dispatches the orchestrator, and this file does
not change that: no dispatch prompt names it, and none should.

## The nine obligations that are already law elsewhere

This table assigns them. It does not restate them — read the rule.

| the obligation | where the text is |
|---|---|
| open the round with the layer's cold read, and with [HARNESS-DECISIONS.md](../HARNESS-DECISIONS.md)'s `§live` | `E10` |
| render the preview card before the round, and wait for the user | `E11` |
| hand the reviewer one commit SHA or range and no per-acceptance argument | `E12` |
| keep the budget — one FULL, at most one user-approved fix, one targeted VERIFY — and never self-classify what consumed it | `E9` |
| hold the review window: from dispatch until the record's commit lands, the branch takes no commit but that record | `E9` |
| commit the reviewer's record unchanged, under the title the rule names | `R6` for the title; that it lands unchanged is `R1`'s *reported through* holding, not `R6`'s text |
| before closeout, put each low's spend-the-fix-leg / bank choice to the user | `R10` |
| route a "should this exist at all" conclusion to the user rather than answering it | `R5` |
| flip a decision entry's state only in the commit that lands its carrier | `HD-2`, which lives in the decision log — outside this layer |

## The three obligations this file is the text for

### Handing the executor its instruction

The orchestrator delivers the round's **instruction, subject and governing plans**, and stops
there. Since round `EXECUTOR-CHARTER` the delivery opens with a generated half: `dtw dispatch
--executor` (product run) or `dtw dispatch --construction-executor` (construction round) hands
the executor its charter at startup — the orchestrator runs the command rather than
hand-copying the pointer. It does not hand over a decomposition: since the three-role model
(`HD-35`) the WorkSpec author is the executor of that run, and a decomposition supplied from
outside is an answer the executor would be checking instead of writing. What the orchestrator
does with the result is render it for the user's approval — the START card for a product run,
the preview card for a construction round (`E11`).

The plans joined that list on 2026-08-22 (round `PRERUN-RIDERS`) for two reasons that arrive
together. Standing discipline lives in them, and since round `EXECUTOR-CHARTER` closed the
Context route the instruction may no longer carry even the reference — so a plan nobody hands
over reaches a cold executor by no path at all. And they are the caller's extension point on
the work side: rules this instrument cannot know are written there rather than into an
instrument the caller may not edit (`HD-34`). What may legitimately sit in a plan rather than
in the instruction is [EXECUTION.md](EXECUTION.md)'s *Instruction authoring rules* to state,
and this file does not re-type it.

### Reading the caller's policy file

A caller may keep a policy file saying what to do, on that machine, with a round's
conclusions — which ledgers to write, which pointers to move, what to do at closeout. Reading
it and acting on it is the orchestrator's obligation; **harness code never executes it**, and
if harness code did, the boundary between an instrument and its caller would be gone.

Three properties, none of them optional. The file belongs to the caller, so this layer does
not say where it lives or what it is called — the caller's own agent-facing entry file points
at it, and that pointer is the only discovery path this layer gives a cold orchestrator. It
has **no authority over any rule here**: where it conflicts with this layer, this layer
governs and the policy file is what is wrong. And a caller that has not written one is not defective — the
absence is a fact to state at closeout, not a gap to fill by inventing policy.

### The executor's report back

When the executor meets something that changes the plan — a boundary it would have to exceed,
an authorization it cannot see in the repository, an instruction unit it cannot map — it
**reports to the orchestrator, which puts it to the user**. The executor does not decide it,
and the orchestrator does not decide it either.

One shape of this is mechanized: an unmappable unit is a `SPEC_GAP`, which stops and re-opens
START (`EXECUTION.md`, *When the instruction itself is the problem*). Everything else is
discipline, so it belongs in the words the executor is dispatched with, and this paragraph is
what those words are answerable to.

## What the orchestrator may never do

- **Review its own round's work.** Where exactly the line runs — work side against review
  side — is `E1`'s to state, and this file does not re-type it. Read `E1`. What a session
  that has merged both work-side roles owes is that rule's **exception channel**, reached
  only by a round that has already deviated from the norm the three-roles table states above.
- **Answer a question the rules route to the user.** `R5`, `R10` and `E11` each send a
  specific shape of question to the user; the orchestrator carries it and carries the answer
  back. Automating the transport is allowed. Automating the answer is signing for the user,
  and no session may do that.
