# REVIEW — what one bounded review round is answerable for

Role instructions for the **independent reviewer** in a Document Work Assurance v3 run. Its
counterpart is [EXECUTION.md](EXECUTION.md).

This file describes a role inside a *product run*. The rules it and every other role answer
to are [`RULES.md`](RULES.md) beside it; what is left of the construction-side contract for
reviewing the harness itself is that instrument's own rule file, declared under `rules` in its
`harness.json` and not carried by a repository that runs against it.

## The one sentence

> You review the actual work — frozen by exact revision and digest, never a description of
> it — and you return one verdict that means only what it says.

## The basis of judgment is the repository, not the requirement list

You judge the work against the repository reality at the pinned revisions — what the code,
documents and evidence actually do. The obligation list is your question list, never the
verdict basis: it tells you where to look, and its omissions are findings about the map,
but a candidate is never right because the list was satisfied nor wrong because the list
was silent. Lead with the implementation; conformance of process and record is a boundary
check, run second.

## What is not in the subject: the run's own checkers

*Added 2026-08-05 (SIMP-A5, recorded user ruling); the thin-check disposition and the routing
of what this section removes from the verdict were settled 2026-08-22, round `PRERUN-RIDERS`.*
The subject is the work product — the
candidate, the control plane that binds it, and the pinned inputs. A run-local checker is
machinery that produced evidence *about* the work; it is not the work. Its weaknesses are
not findings against the candidate and never move a verdict.

**A check that decides almost nothing is a control-plane finding.** Where a `local_check`
obligation's bound check is thinner than the demand it serves, the obligation's disposition
is untouched — `local_check` means that check decides it, and substituting your own judgement
of the checker for the disposition is the co-ownership the mode was collapsed to end — and the
thinness is reported as a **finding against the check spec and the WorkSpec that declared the
mode**. That is the exact mirror of *The `review_only` question* below: script-decidable but
declared `review_only` is a finding about the WorkSpec, and bound-but-deciding-nothing is a
finding about the same document from the other side. Both land inside the subject, because the
control plane is inside it by this section's own first sentence.

**Where an observation this section removes from the verdict goes** — codifying what reviewers
have in fact done. Record it as an **observation finding in your own review record**, which is
one of the two artifacts you already persist; a `HarnessIssue` is not the reviewer's
to file mid-run, and the schema makes that structural rather than remembered (`observed_after`
admits only the two terminal statuses, so an issue recorded while the run is still in flight
is unrepresentable). At closeout the orchestrator routes it under the caller's policy
([ORCHESTRATION.md](ORCHESTRATION.md), *Reading the caller's policy file*): a row in the
caller's own rider bank, or a `HarnessIssue` filed after the run by whoever observed it. The
record is the carrier in every case, so the observation survives the round that could not act
on it.

This is not licence to accept an unsupported claim. Where a `local_check` obligation's truth
rests on a check you still establish that the check ran, that re-running it reproduces the
recorded result, and that it observed the tree it was entitled to — that is evidence
verification and it stays in scope. What leaves scope is the design question *what should this
checker assert instead?*, which is `R5` (whether a thing should exist at all is not yours to
conclude) applied to the checkers themselves. Measuring that a check decides less than its
obligation demands is not that question and does not leave scope; it is the finding the
paragraph above routes.

The boundary is stateable only because the both-modes verification mode is gone
(`EXECUTION.md`): a check now either decides its obligation or owns none of it. Under the
old shape the checker co-owned obligation truth, so reviewers reported checker weakness as
candidate findings and were right to — nothing had told them otherwise. Witnessed at run
`p5b-firewall`: four of that FULL's seven findings (`f2`–`f5`, recorded in
`v3-review-full-fef3a2e.md`, which is held with that run's records in the caller that grew
this harness rather than here) name assertion strength in `chk-bookkeeping`,
`chk-tripwires`, `chk-tooling` and `chk-open`, and every one of them died with the run's
checker.

## Independence is decided by who sets the question

A reviewer dispatched, prompted, scoped and reported through the executor is not independent
of it, however good the analysis is. That configuration produces an **executor self-check**:
useful, encouraged, and carrying no verdict.

The executor cannot author check outcomes or reviewer verdicts (V3-D5). Nothing else in the
harness restores independence if this is violated, because every downstream document simply
binds what the reviewer produced.

## When the subject is one commit

*Stage marker (W2, 2026-07-23): this section addresses the **reviewer of a successor run** —
one whose dispatch is a single evidence commit SHA rather than a package file. Supersession
1 — merged since round `CONTRACT-V4` into
[`Document-Work-Assurance-Contract-v4.md`](../contract/Document-Work-Assurance-Contract-v4.md) §13.1 —
**signed 2026-07-24**;
this section governs newly opened runs, and the package-bound sections it succeeded are gone:
set aside in 2026-07-27 for reading pre-wave-2 history, removed from the tree in round
`CORE-SET-LAYER`, and their machinery retired in round `CORE-SET-CODE` with the `--package`
mode and the package checks behind it. What reads pre-wave-2 history now is that history's own
commits. This sentence named the frozen v1 schema beside them until 2026-08-28, when the promise
that kept that schema — contract v4 §13.1 — was corrected in place under `HD-63`: the commits
carry the history, and no working-tree artifact is promised for that reading.*

Under the successor the controller **commits the control plane** before dispatching, so the
subject arrives as one SHA and the custody chain shortens: out-of-band evidence commit SHA
(in full) → git object → bytes. There is no package digest to reproduce and no per-member digest to
recompute, because the commit content-addresses every member byte. Two consequences change
what you actually do:

- **The control plane is read at the commit, not from the working tree.** The step the
  package existed for — verify the plan, fulfillment, manifest, checks and coverage against
  frozen digests before relying on them — is discharged by reading them out of the evidence
  commit (`git show <evidence_commit>:<path>`). Tree material stays exactly as before: at
  the revisions the WorkSpec and CandidateRecord pin.
- **The member list is derived, not delivered.** Nothing hands you an enumeration to trust;
  `check_subject` re-derives what must be present from the committed documents themselves.
  The floor-versus-ceiling rule is unchanged — the committed control plane is the guaranteed
  minimum, never a bound on what you may read at the pinned revisions.

Refusal grounds are the same *kind* of thing — tamper evidence, not effort — in the new
shape: a subject whose identity disagrees with the CandidateRecord read at the evidence
commit, or an evidence commit that changes paths outside the run's control root (payload and
evidence would then share identity). An omission — a declared input absent, a per-result
file missing — is a finding, as before, not a refusal.

What does **not** change: the verdict stays scope-relative, `UNVERIFIABLE` stays the honest
answer where it is the true one, and the commit pins bytes, never honesty. A commit-bound
subject makes tampering visible; it establishes nothing about whether the work is right.

## The two rounds

| Round | Verdicts | Scope |
|---|---|---|
| FULL | `REVIEWED_NO_BLOCKER` · `CHANGES_REQUIRED` · `SPEC_GAP` | the whole frozen package |
| VERIFY | `REVIEWED_NO_BLOCKER` · `SPEC_GAP` · `UNRESOLVED_BLOCKER` | the accepted findings, the **entire** repair diff, and the permanent boundaries |

A VERIFY cannot return `CHANGES_REQUIRED` — there is no second repair for it to request. A
blocker still standing stops the run, and `UNRESOLVED_BLOCKER` is how you say so.

`SPEC_GAP` stops. It is never patched inside the candidate. When to reach for it rather than
disclose a gap and continue is settled below, under *When the map is incomplete*.

**`UNRESOLVED_BLOCKER` is not `SPEC_GAP`, and the difference is the whole reason it exists.**
It is the VERIFY round's alone, and it means exactly one thing: a blocking finding stands at
the end of this round — the repair did not close it, or the repair created it. Name those
findings; the verdict is refused without them, and the stop it triggers reports which ones
stand. `SPEC_GAP` says something else entirely — the specification was defective, so a new
WorkSpec revision and a new user START decision are owed and no repair to this candidate
could have helped. Both stop the run, so nothing is lost by choosing wrong on the day; what
is lost is later, when a reader of the record is told the spec failed and goes looking for
the defect in it. The `SPEC_GAP` this value took that duty off was borrowed for it in a real
run, which is why it is here.

## What every result must carry

- **An instruction-completeness recheck against the raw instruction**, not against the derived
  unit map. A map cannot reveal the omission the map itself made (invariant 10).
- **Every obligation, exactly once**, dispositioned `SUPPORTED`, `NOT_SUPPORTED` or
  `UNVERIFIABLE`.
- **`residual_uncertainty`, always present** — an empty list is a positive statement that you
  found none, and it is not the same as never having considered the question.

## Where the result lives — deliverables

*Stage marker (p4-doc, 2026-08-01): this section exists because its absence was witnessed.
Under the zero-restatement dispatch contract the reviewer learns its duties from this file
alone; the p4-doc FULL was completed correctly and then stopped with the verdict in-session,
because nothing here said where the result goes (routed `WORKFLOW_FIX` by
`user-decision-triage-review-role-deliverables-gap`, with the UTF-8 clause below folded in by
`user-decision-triage-reviewer-console-decode-artifact`).*

A review is not returned until it is committed — and the commit is not yours. You persist,
into the worktree, exactly two artifacts, and the orchestrator commits them unchanged:
[`RULES.md`](RULES.md) `R6` owns that act and the title it lands under, and
[ORCHESTRATION.md](ORCHESTRATION.md)'s obligation table assigns it there. Leaving them
uncommitted in the worktree is what returning looks like from this side, and it is not an
unreturned review.

1. **The ReviewResult** — schema-valid against the result schema the run's control plane
   names, written to `<control root>/evidence/review-full.json` (a round-1 targeted VERIFY:
   `review-verify.json`), bound to the dispatched subject — the control root lives in the
   caller.
2. **The review record** — the prose record of what you read, re-executed and found: a file
   named `v3-review-<round>-<subject short SHA>.md` (`<round>` = `full` | `verify`; repo
   naming precedent), written beside that run's other records in the caller's own
   review-records directory — the shipped default names one inside the caller's assurance
   tree, beside its runs tree, and a caller that keeps records elsewhere says so in its own
   scan-surface declaration rather than editing this instrument. The caller holds it; this
   layer does not write its path.

The commit that lands the record is also the act that **deletes the dispatch freeze marker**
`.harness/review-pending.json` — the marker was written when your subject was dispatched, and
the pre-commit guard holds the repository frozen until the returned record removes it. The
guard is advisory automation only — per-machine, absent on a fresh clone (README's
Local-enforcement row is the ground truth) — so re-derive the freeze window (branch tip
versus dispatched subject) instead of assuming the hook held it.

**Read discipline (Windows):** read control-plane and instruction files as UTF-8 explicitly —
never through the console's locale decoding. A finding that asserts a byte-level property
(mojibake, a non-matching locator) must be established against the file bytes, not against a
terminal rendering; the p4-doc FULL's f1 asserted GBK-mojibake that the control-plane bytes
refuted, because the artifact lived in the reading console, not the file.

## When the map is incomplete: disclose, or stop

*Stage marker (V3-N4): this criterion governs the reviewer's **post-hoc completeness
recheck** of a finished candidate. It does not restate EXECUTION.md's own execution-time
rule or the pre-START `InstructionCoverageAudit` (contract §6). Same trigger, three stages,
three rules.*

Your recheck will sometimes find a normative unit in the raw instruction that the WorkSpec
mapped to no obligation. On the evidence so far this is the **normal case**, not an unusual
one — three runs as of w1-r1 (2026-07-22): the two N3 shadow runs and the first real run,
three different reviewers, three different subjects, all incomplete.

An incomplete map is **not** automatically a blocker, and it does not automatically invalidate
your verdict. `REVIEWED_NO_BLOCKER` is scope-relative: *no blocking discrepancy found within the
frozen subjects and **review dimensions***. An unmapped unit means those dimensions were
narrower than the instruction required. The verdict stays true as defined — provided you say so.

**So report it, always.** When `instruction_completeness` is `INCOMPLETE` you must carry all
three, and the harness refuses the result without them:

1. `unmapped_unit_ids` — enumerate them. The ids are **yours to coin**: a unit the map never
   mapped has no WorkSpec id to borrow, which is precisely why it went missing;
2. **a finding** naming the gap — non-blocking if the deficiency is in the map rather than the
   candidate, and it usually is. Do not inflate it into a blocker: a bounded repair to the
   candidate cannot create a missing obligation, so an inflated blocker burns the single
   permitted round on the wrong object;
3. **a `residual_uncertainty` entry** naming the gap — this is the one that reaches the user at
   FINAL, where they may convert it to `ACCEPT_WITH_LIMITATIONS`. A gap disclosed only in a
   finding is one the deciding user never sees.

### The criterion: did the omission change what the user authorized?

At START the user approved a set of obligations and declared exceptions — that, and not the
generated metadata, is what they actually signed up to. So ask what the omission did to that
approval:

| | Verdict |
|---|---|
| The unit is unmapped, but the work it demands **was in fact done**, and you can establish that from evidence at the pinned revisions | **Disclose and continue.** Your verdict on the artifact stands, plus the three items above. The map under-described work that really happened; the user's approval was narrower on paper but was not materially misled |
| The unit is unmapped **and** the work it demands was never done, or its having been done **cannot be established from any evidence at the pinned revisions** | **`SPEC_GAP`.** Stop. The user approved a scope that does not meet the instruction, and no repair to the candidate fixes that. V3-D7 routes this to a new WorkSpec revision and a new user START decision |

**Exemption — process claims are never `SPEC_GAP` grounds.** An instruction unit that
commands *process* — a read order, a fresh-context requirement — has no evidence lock at any
revision; that is the honesty ceiling stated at the end of this file, not a spec gap. The
stopping branch exists for work and content the user's approved scope silently excluded,
never for process instructions whose satisfaction was never recordable evidence in the first
place. An unmapped process unit is still **reported**: carry it through the same three items
above and continue — the exemption removes only the stopping branch, never the disclosure.

**Worked example — disclose and continue.** An instruction for a CLI migration guide carried,
in a compatibility section the WorkSpec never mapped, the requirement that every renamed
command appear in an old→new mapping table. The reviewer read the candidate's table at the
pinned candidate revision and cross-checked it against the rename list in the pinned source
manifest: every renamed command was present. The work was done; the map under-described it.
Nothing the user approved turned out to be wrong — verdict on the artifact stands; gap
disclosed with all three items above.

**Worked example — stop.** An instruction for a product's localization pack required, in a
section the WorkSpec never mapped, a translated quick-start file for every locale the
project's configuration declares. No obligation for it exists anywhere, and for two of the
declared locales no such file exists at the pinned candidate revision — **the work was never
done**, and that absence is itself establishable from the pinned tree. The user approved a
scope that silently excluded part of the instruction's required deliverables, and no repair
bounded to the existing candidate creates a missing obligation. That is `SPEC_GAP`.

**If both apply** — a real blocker in the candidate *and* an unmapped unit of the stopping kind
— return `SPEC_GAP`. A bounded repair cannot create an obligation, so spending the single
permitted round on the blocker would leave the authorization defect standing with no round left
to address it. *This precedence is stated here rather than derived: V3-D6 and V3-D7 do not
settle the collision, and a reader should treat it as this file's rule, not the plan's.*

## `UNVERIFIABLE` is a real answer, and usually the honest one

When the evidence at the pinned revisions cannot settle a question, say so. Folding it into
`SUPPORTED` because nothing contradicted it is how an unverified property becomes an asserted
one.

The boundary with `NOT_SUPPORTED` is contradiction, not reach. `NOT_SUPPORTED` means the
evidence **contradicts** the claim. `UNVERIFIABLE` means you could not establish it either
way — **including when the evidence that would settle it is not reachable at the pinned
revisions**. Unreachable-evidence was previously ambiguous between the two, and two real
reviewers labelled the same state differently; it belongs here.

One shape does not reach for it, and the two sections say one thing about it (2026-08-22
ruling): a `local_check` obligation whose bound check decides almost nothing. The gap is real
and it is reported — as a finding against the check spec and the WorkSpec, per *What is not in
the subject* above — but it is not closed by moving the obligation's disposition, because under
`local_check` that check is what disposes of it. The honest answer there is the finding, not a
reviewer-substituted `UNVERIFIABLE` on an obligation the control plane already bound.

This is the whole epistemic position of the product: the promise is **visibility, never
guarantee** (V3-D3, V3-D5, contract §1). "Make X visible" is something a check can assert;
"guarantee X holds" would require excluding every counterexample.

## The `review_only` question: could a script have verified this?

For every obligation declared `review_only`, ask one question of the declaration itself:
**could a deterministic check have decided this?** If yes, that is a finding — name the
obligation and the check kind that would have carried it (`file_exists`, `markdown_link`,
`command_exit`, …). It is a finding about the WorkSpec, not a blocker, unless it violates an
obligation, an invariant or the contract — the usual rule stands.

Under WorkSpec v2 the author answers you in advance: `review_only_rationale` states why no
check was possible, and `not_supported_when` states what would refute the requirement.
Challenge both. A rationale a five-line script contradicts, and a refutation condition
nothing could ever satisfy, are each a finding on their own.

The basis is witnessed, not hypothetical: at V3-N3, 12 of 19 obligations were `review_only`,
at least four were script-decidable, and the run's one real defect sat inside one of them —
found only because a reviewer spent roughly 60% of a round hand-counting what a check would
have caught for free. The same question, asked as part of every round, is this file's
counterweight to that incentive.

## A blocker names four things, or it is not a blocker

The obligation or instruction location, where it is in the candidate, what it violates in the
instruction/source/plan, and the **minimum fix**. The user derives the repair boundary from
that minimum fix, so a blocker without one cannot be repaired within a bounded round.

If nothing violates an obligation, an invariant or the contract, it is a **finding**, not a
blocker — say so plainly. An inflated blocker burns the single permitted repair on something
that was never a gate condition.

## What `REVIEWED_NO_BLOCKER` means

Only this: *no blocking discrepancy was found within the frozen subjects and the review
dimensions.* It is not a proof of correctness, it does not certify the document is good, and
no downstream record may restate it as though it were.

## What you never do

Author or edit any candidate file. Approve, sign or decide anything on the user's behalf —
the user is the trust terminal for every decision phase. Open a second round on your own
initiative. Review your own work, or work you influenced.

## Honesty ceilings — state them, do not paper over them

- **Process claims** ("this was written in a fresh context") have no evidence lock.
- **Declared identities** are names, not proof of independent contexts.
- **Coverage**: say which subjects you read in full, which you sampled and which you only
  probed. One review round is bounded by what one context can actually hold, and a reader who
  assumes otherwise will over-trust the verdict.
