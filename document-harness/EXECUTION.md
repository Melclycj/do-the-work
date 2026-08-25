# EXECUTION — what the executor owns, and what it may never author

Role instructions for the **executor** of a Document Work Assurance v3 run: the ordinary
instruction-following agent that writes the document changes. Its counterpart is
[REVIEW.md](REVIEW.md). Not every section addresses the executor: four of the six run-template
sections (moved here by `HD-14`) address the run author at authoring time — stage markers say
so where they begin. *Authoring obligations under WorkSpec v2* used to be one of those; since
the three-role model (`HD-35`, io-design §4) the WorkSpec author is the executor of this run,
so that section addresses you.

This file describes a role inside a *product run*. It is not the construction-side contract
for building the harness itself — that lives at
[`CONSTRUCTION-CHECKLIST.md`](CONSTRUCTION-CHECKLIST.md). One section below is the exception
and says so in its own opening sentence: *Regression-battery tiering* binds a construction batch's
pre-commit verification as well as a run's evidence pass, because the 2026-08-03 ruling that
produced it decided one tier question for both sides.

## The one sentence

> You write the payload candidate and one honest claim per obligation. You do not author the
> manifest, any CheckResult, any review verdict, the coverage certification or the decision.

Every rule below follows from that split (V3-D5).

## What you own

| Artifact | Your obligation |
|---|---|
| the payload candidate `C` | only the declared document changes, on an isolated branch rooted at the exact base |
| `FulfillmentReport` | exactly one claim per obligation, and at least one resolvable locator behind every `IMPLEMENTED` |
| a `HarnessIssue`, after the run ends | optional, immutable, evidence-linked |

## What you may never author

The manifest (the diff verifier owns it), any `CheckResult` (the verifier that ran it owns
it), any `ReviewResult` (the reviewer owns it), the `AssuranceCandidate` or `AssuranceSummary`
(the controller binds them), and any `UserDecision` (the user owns every one).

This is enforced, not merely asked for: a manifest or check result whose author matches the
executor of the same run is reported as a defect. Role separation is a workflow protocol, not
an OS guarantee (contract §1) — the check compares declared names, and nothing here stops one
operator from playing both roles. It stops the *artifact* from silently claiming otherwise.

## `NOT_IMPLEMENTED` is a first-class answer

An obligation you did not implement is recorded as `NOT_IMPLEMENTED`, explicitly, and it can
never become unqualified success (invariant 4). This is the single most important habit in the
role, because the failure this product exists to catch is not a wrong answer — it is a missing
one that looked like a passing one.

The same applies to a locator you are unsure of. A claim is not evidence: `IMPLEMENTED`
requires a locator that resolves **uniquely** in the exact candidate, and both zero matches
and several matches fail. An ambiguous anchor does not identify a location.

## Before you say the work is done

1. **Every obligation has exactly one claim.** Not zero, not two.
2. **Every `IMPLEMENTED` claim has a locator that resolves in the candidate commit**, not in
   your working tree. The working tree is mutable and is not the candidate.
3. **No control or evidence file is inside the payload.** Evidence about the candidate must
   not live in the candidate (V3-D9).
4. **The observed change set is inside the declared boundary.** This is an acceptance
   boundary, not enforcement: nothing prevented an out-of-boundary write, so nothing but this
   check will notice one.
5. **Measure last.** Any figure you report is invalidated by a later change to what it
   measures. Re-run the command immediately before the claim rather than reusing an earlier
   number — a stale figure presented as a fresh measurement is exactly the unsupported
   completion claim this product detects, and it has happened inside this project's own
   records.

## When the instruction itself is the problem

*Stage marker (V3-N4): this rule governs **execution time** — the executor meeting an
unmappable unit while working against the WorkSpec. It is not the pre-START
`InstructionCoverageAudit` (contract §6), and it is not the reviewer's post-hoc recheck of a
finished candidate, which follows REVIEW.md's conditional criterion (*When the map is
incomplete*). Same trigger, three stages, three rules.*

If an instruction unit cannot be mapped to an obligation or an explicit context rationale,
that is a `SPEC_GAP`. It stops. It is not patched inside the candidate, and it is not
smoothed over by picking the most likely reading: a new WorkSpec revision and a new user
START decision are required (V3-D7).

## After a review

You may repair **only** what the user authorized: the accepted finding IDs, inside the
minimum repair boundary bound to that decision. A repair boundary may narrow the run's
boundary and never widen it — a wider one is a second, broader authorization obtained by
calling it a fix.

The repair produces a new candidate `C2`, and **every** piece of evidence is regenerated
against it: manifest, fulfillment mapping, all checks, coverage and the review package.
Carrying a round-0 document forward is not a shortcut, it is a document describing a candidate
that no longer exists.

There is one repair. If a blocker still stands after the VERIFY, the run stops — the honest
dispositions left are `STOPPED_REPLAN` or a user `ACCEPT_WITH_LIMITATIONS` that names what is
still open.

*Stage marker (W2, 2026-07-23): under a **successor run** — one dispatched as a single
evidence commit SHA rather than a package file, governed by
[`Document-Work-Assurance-Contract-v4.md`](../contract/Document-Work-Assurance-Contract-v4.md)
§13.1 (the commit-bound boundary; merged from supersession 1, signed 2026-07-24) — the
sentence above reads the same with one substitution and one
addition: there is no review package to regenerate, and the repair must land a **new
evidence commit**. Reusing round 0's is the same defect in a new place: the subject would
name a control plane that describes the candidate the repair replaced. Until that
signature, every run is package-bound and the paragraph above stands unqualified.
Signature state: **signed 2026-07-24** — recorded at
[W2-record §log](../migration/document-work-assurance-v3/W2/W2-record.md) (`ac1b383`);
newly opened runs are successor runs, and the package-bound form is pre-wave-2 history.*

## Authoring obligations under WorkSpec v2 — what the two sentences are for

*Stage marker (W1, 2026-07-22; re-pointed by batch B R4): this section addresses the **WorkSpec
author**, which since the three-role model (`HD-35`, io-design §4) is the executor of this run,
decomposing the instruction it was handed — inside the round, before the START card and before
any document change. The earlier reading, an upstream stage author or planning agent wearing an
earlier hat, is pre-`HD-35` history: what changed is who decomposes, not when.*

**Newly authored WorkSpecs declare `schema_version: "2"` — always** (user mandate,
2026-07-22). The version-less shape stays legitimate only for WorkSpecs that predate
wave 1 (the loader itself is date-blind — absence still keys to v1); it is a historical
form, not an authoring choice. The two sentences this section explains exist only in v2,
and the loader never upgrades a spec that did not declare itself — a new spec authored
version-less silently opts out of them, which is exactly what this mandate forbids —
nothing mechanical refuses it; it is caught, if at all, by whoever reads the spec before
START.

WorkSpec v2 makes `review_only` cost two sentences: `review_only_rationale` (why no
deterministic check can decide this) and `not_supported_when` (what state of the world would
make the disposition `NOT_SUPPORTED`). Write them as answers, not as filler — the schema can
only check that they are present; whether they are true is challenged at review.

A worked contrast — both are legal v2 shapes, and only one is a requirement:

| | requirement | `not_supported_when` |
|---|---|---|
| falsifiable | "every internal link between the two notes resolves" | "any link target missing at the pinned revision" |
| not a requirement | "the document reads well" | — nothing can be written here — |

If you cannot answer the second column, the obligation is an impression occupying a
requirement's slot: no fact can conflict with it, so the only honest disposition review can
return on it is `UNVERIFIABLE` — and a `SUPPORTED` spent there certifies nothing. Reword it
until it can fail — or bind a check and let the check be the answer.

One honesty boundary. This guidance treats **wording** only; the *incentive* to declare
`review_only` where a five-line script exists is treated by the schema fields, the coverage
ratio line and the reviewer's `review_only` question, never by this prose (witnessed at
V3-N3: 12 of 19 obligations were `review_only` and the run's one real defect sat among
them).

**The mode is a two-way choice, and the test is whether the machine's answer is the whole
answer** (SIMP-A1, recorded user ruling 2026-08-05). `local_check` means a deterministic
check decides the obligation outright; `review_only` means it does not, and the two
sentences say why. The both-modes value is deleted from the enum: an obligation whose check
decided half of it made the checker a part-owner of that obligation's truth, so no reviewer
could dispose of the obligation without first judging the checker — which is how run-local
checkers, written fresh each round and discarded with it, became a standing review subject
that accumulated nothing. When a demand has a script-decidable half and a semantic residue,
split it into two obligations rather than write one obligation in two minds: the equality is
`local_check`, the residue is `review_only`. Mechanical help that decides no obligation's
truth is not a mode at all, and it has two homes, neither of them the enum: the **authoring
gate**, which reads the instruction, and the **pre-submission lint**, which reads the work
product — the candidate, in a product run — and disposes of nothing (SIMP-A4, recorded user
ruling 2026-08-06). A specification is not a work product — it is the authoring gate's
subject: it names the files the work is required to create, so those cannot exist when it is
written. The split is
not taxonomy. The authoring gate runs before START, when no candidate exists — so a defect
written into the candidate is one it structurally cannot see, and the reviewer pays for it.
A lint never becomes a `CheckResult`, is never cited by a claim, and its silence is never
evidence; the moment it would decide an obligation it is a check and belongs in the enum.

*Stage marker (R1, 2026-08-09, `HD-14`): the six sections from here through **Instruction
authoring rules** are the run-template rule set, moved verbatim (path re-rootings and one
self-reference disclosed in the moving commit) from
`assurance/templates/run-v2/README.md`, which now holds instantiation only.
Four address the **run author** at authoring time — **Pre-freeze gate**, **Instruction form**,
**Authoring gate**, **Instruction authoring rules**; **Audit cadence** governs the executor-side
pre-START gate, and **Regression-battery tiering** governs what verification a pass owes.*

## Pre-freeze gate (2026-08-02/03 rulings)

Two duties gate the instruction freeze commit itself — run them before freezing and record
the command output in the freeze commit's body (measure-last form: the output, never a
description of it). Both were bought by p5a-shells' pre-START history, recorded in that
run's `audit-rounds.md` — a run artifact held with its run in the caller that grew this
harness, not in this repository.

1. **Mechanical reconciliation (2026-08-02 ruling).** Every enumeration the instruction
   text states — module lists, path lists, counts — is reconciled by command-output diff,
   never by eye, against both the registry or tree it derives from and the `write_scope`
   the WorkSpec/build script grants. A discrepancy blocks the freeze until text or scope
   is corrected. Witnessed cost: audit round 3 f1 — the v2 instruction narrowed the caller's
   own tests tree to four named paths, `build_run.py`'s list never received it, and the
   miss cost one full from-scratch round (~176k tokens).
2. **Checker dry-run self-check (2026-08-03 ruling).** Every bound check argv is executed
   once against the base tree and three-way classified: PASS /
   fails-for-the-expected-reason / crashes-or-fails-for-the-wrong-reason. The third class
   blocks the freeze. Witnessed cost: the v2 freeze froze `check_shells.py` without ever
   executing it — `load_shells` crashed on any real index — and the jointly-unsatisfiable
   expectation surfaced only at the FULL as `SPEC_GAP`, costing the whole cycle; the v3
   cycle ran this dry-run and the crash signature surfaced immediately.

## Instruction form — the branch that decides what a run owes (SIMP-B/C, 2026-08-05)

The instruction **declares its own form** in frontmatter, and the form decides which
derived artifacts the run owes. Both halves are ruled: the declaration is the
instruction's (`form: enumerated`), never a model's reading of it — having an agent judge
the shape would be an unrecorded judgment with no evidence lock, and the same
interpret-the-prose step this branch exists to delete, moved earlier.

| | `enumerated` | `prose` (the default, and the fallback) |
|---|---|---|
| WorkSpec (件 2) | **kept**, produced by mechanical transcription: one `R<n>` section, one obligation | kept, derived by reading |
| paragraph map | **not owed** — no classification column exists to fill | owed |
| preamble gate | **not owed** — there is no preamble left to map | owed |
| InstructionCoverageAudit | **kept**; its full walk is replaced by the transcript check (see Audit cadence) | kept, full walk |

**The declaration is verified, not believed** (`resolve_form`, one place). Under the
enumerated form every block of prose must live inside a numbered `R<n>` section or inside
the non-normative Context section, and nothing else — that structural property is what
makes the three artifacts above objectless, and it is what the lint establishes. The
resolution is **fail-heavy**: no declaration, a misspelled one, or one the structure does
not bear out all resolve to `prose`, and the run owes everything again with the reasons
printed. What the lint cannot see is stated where it lives: an unmarked normative
declarative *inside* Context. FULL review's instruction re-walk remains the backstop it
already was.

Two authoring consequences:

- **The preamble is split, not demoted** (SIMP-C3). A normative preamble is exactly the
  defect w1-r1 and p4-bridge each paid for, so under the enumerated form it stops
  existing: the round-specific normative sentences become **`R0`**, an ordinary numbered
  section with an ordinary obligation, and the standing discipline is not written into
  the instruction at all — the executor receives it with its dispatch (*Instruction
  authoring rules*). Today's typical preamble splits cleanly: "isolated branch / nothing merged
  before FINAL" is standing discipline, "do not activate `P5B-CLAIMS-v1`" is this round's
  and becomes R0. This applies to instructions written after the ruling; closed rounds are
  not retrofitted.
- **The START card presents the numbered list itself** (SIMP-C4). Under the enumerated
  form the WorkSpec is a transcript, so asking the user to read it is asking them to
  proof-read a mechanical copy. They approve the `R0…Rn` list — the bytes they were going
  to be bound by anyway — and the transcript check is what says the WorkSpec matches it.

However the form resolves, **the START card of every product run is rendered by
`dtw preview` from the frozen control plane** (round PREVIEW-RENDER, 2026-08-21 ruling;
scope ruled form-independent by `HD-52`, 2026-08-22) — deterministic, re-derivable at any
time and therefore never stored — so what the user reads is the plane's own bytes, not a
session's transcription of them. What differs by form is only what those bytes contain:
under the enumerated form the card presents the `R0…Rn` list itself, per the bullet above.

## Authoring gate (W2-A5 + M11)

`check_template_instance.py` must pass before START (legs 2 and 3 are owed by the prose
form only — see *Instruction form* above):

- the WorkSpec declares `schema_version: "2"` (the v2-mandate, `a22cca0`);
- **preamble-level normative run conditions appear in the unit map**: if the frozen
  instruction has a non-trivial preamble (content before its first `## ` heading), at
  least one instruction unit must anchor into that preamble. w1-r1's FULL review caught
  exactly this omission (issue-w1-r1-unmapped-preamble, triaged WORKFLOW_FIX): authoring
  and the coverage audit both passed a map whose START approval surface was narrower than
  the instruction. The check forces the map to face the preamble; whether the mapping is
  *adequate* stays a review question.
- **the paragraph map exists, is current, and survives the three-way cross-check**
  (M11, Phase C4 — the p3-corr omission made mechanical): generate the run's
  `<control root>/control/paragraph-map.json` — the control root lives in the caller, not
  here — with `make_paragraph_map.py` (every derived column is
  machine-written), fill the one human column — `"classification": "obligation" |
  "context"` per entry — and the gate then checks instruction bytes ⟷ map (exact
  skeleton match, stale maps refused), map ⟷ unit map (every obligation-classified
  paragraph has a unit anchoring into it), and unit map ⟷ instruction bytes (no
  dangling anchors). A paragraph can be misclassified but never silently absent;
  whether a *classification* is right stays a review question.

One standing observation rides each run past this gate (C4 `O-1` observation clause,
2026-08-01; obligation sited by user ruling 2026-08-22, cut in two by user ruling
2026-08-25): the run's review/closeout records one line comparing the two maps'
classifications — paragraph map against unit map — naming who or which session filled
each; same-source filling is not independent and joins no sample. **That one line is the
whole of it.** Reading the collected lines and taking the three-branch re-ruling is a
construction round's work, and it is stated where this instrument keeps construction-side
rulings; a product run neither performs that reading nor waits on it, and collection does
not stop because it has not happened yet. The recording falls to the work side at the run's
review/closeout — the orchestrator's station — and the obligation is written beside the gate
that authors the map it samples, not in an instruction's Context section, where it spent five
runs hand-copied for want of a home.

## Audit cadence — pre-START rounds (2026-08-02 ruling)

The InstructionCoverageAudit (V3-D7) stays mandatory before START; what is tiered is how
many full walks it costs, because the independent full walk lives downstream anyway —
REVIEW.md's instruction-completeness recheck walks the raw instruction against the unit
map from scratch at every FULL, and is the backstop none of the rules below touches.
Witnessed cost that bought this ruling: run p5a-firewall spent four from-scratch opus
rounds (~525k tokens, ~28 min) on a two-file prose candidate whose rounds 2–4 re-walked
a spec that changed by 1–4 lines each time.

**Under the enumerated form there is no walk at all** (SIMP-B1, 2026-08-05 ruling). The
audit stays mandatory and the artifact, its digest and the START binding are untouched;
what disappears is the fresh-context round, because once the instruction is a numbered
list the question *was anything left unmapped* is answered by a diff.
`rsclib.document_harness.instruction.transcript_audit(spec, instruction_text)` returns
`(result, findings)` and the run's `write_audit.py` puts them into the audit document,
naming the mechanism in `audited_by` (e.g. `mechanical transcript audit —
transcript_audit @ <blob>`). That name is a **disclosure, not an independence claim**: the
distinctness check still runs and still compares declared names, and what makes the string
honest is that it says what produced the verdict. The ceiling travels with it — every
numbered section is shown to reach an obligation, but whether the obligation's requirement
text is a faithful restatement of that section is *not* checked, and FULL review's
instruction re-walk is the unchanged backstop. The three rounds below are the prose form's
cadence.

1. **Round 1 is always a full walk** — fresh-context auditor, the p4-doc shape. A round
   here is the contract's exactly-one audit of one frozen WorkSpec/instruction revision;
   successive rounds exist only because a repair produced a new revision.
2. **Delta re-audit after a repair.** When the repair's diff over the WorkSpec (and, if
   touched, the instruction) is cleanly enumerable, the re-audit hands the next auditor
   the prior round's report plus that exact diff, and re-walks only the changed units,
   everything the repair touched, and whatever the prior round flagged; byte-unchanged
   units are covered by citing the prior round — the E10 citation trick applied to audit
   rounds. From-scratch stays the fallback whenever the diff is not cleanly enumerable,
   and stays the rule for every round of a run whose write scope touches code, schema or
   generated surfaces — doc-only runs (write scope entirely prose/markdown) are the tier
   this rule relaxes. One carve-out crosses the tiers (2026-08-02 ruling): a repair whose
   diff touches only the WorkSpec and control-plane map artifacts — the frozen
   instruction byte-unchanged — takes the delta path in any tier, because what a from-scratch walk re-reads is precisely the
   frozen instruction, and those bytes did not change. Witnessed cost: p5a-shells round 6
   re-walked byte-identical freeze v3 from scratch (~212k tokens / 14 min) to clear
   repairs that were all WorkSpec/map-side.
3. **One repair batch per round.** Before dispatching any re-audit, triage every open
   observation from the round in hand and land the accepted fixes as one batch — never
   fix-one-redispatch-one.

The audit is an executor-side gate (a subagent auditor is V3-D7-distinct, never
review-independent — the N1 ruling), which is why handing the prior report to a delta
auditor is admissible where handing a reviewer anything would not be.

## Regression-battery tiering (2026-08-03 ruling — this section is the revert unit, at the price the revert note states)

Which verification a pass owes is tiered by the change surface — for a product run's
evidence pass and for a construction batch's pre-commit verification alike:

- **Doc-only change set** (every changed path is prose/markdown outside the schema,
  tooling, and generated trees): run the batch-specific checks only; the full battery
  is not owed. Exception, and what it turns on is the **path**, not the prose: code and
  tests pin the *paths* of certain doc files — today `document-harness/README.md`
  under `test_readme_enumeration.py`, the member paths in the layer-path mirror,
  `tooling/hooks/layer_path_check.py`, the two shipped instance templates under
  `document-harness/templates/` that `tooling/rsclib/document_harness/init_target.py`
  copies, and `contract/Document-Work-Assurance-Contract-v4.md` under
  `tooling/rsclib/document_harness/__init__.py` — so a change that adds, removes or
  renames **any doc path code or a test pins** is tooling-load-bearing and the batch is
  tooling-touching, while a change to the *content* of such a file, its path unchanged,
  stays doc-only.
  Two accepted rounds had already read it this way before any text said so (`838c413`,
  and batch B R4, which changed two enumerated members and took the doc-only tier);
  rider `tier-file-vs-clause` carried the gap, and the user ruled the clause reading into
  the text 2026-08-18.
- **Schema, tooling, or generated surfaces touched**: the full battery runs, and it is
  these six commands and nothing fewer — owed by **the repository that holds each one's
  subject**, because since the 2026-08-17 split the instrument and the product it grew
  inside are two repositories:
  - *this repository, the instrument*: `python -m pytest -q` **run from
    `tooling`** (from a repository root that also carries the product,
    collection aborts — in the caller that grew this harness, the ExperimentLab papers tree
    holds two same-named `smoke_test.py`). One command, and nothing fewer. `python` in this
    file means whichever of `python3` / `python` the machine actually runs: stock Ubuntu
    ships only `python3`, so an executor on a POSIX machine typing the command as written
    finds nothing (measured 2026-08-23, round `PUB-FACADE`).
  - *the caller repository, the product tree* — five commands owed by the caller and not
    by this repository, **named here rather than written as paths** (`E10`) because their
    scripts live in the caller's tree: the P2 golden runner `run_tests.py` (P2 goldens
    *only*, per its own docstring), `run_p4_tests.py`, `run_p5a_tests.py`, the schema
    fixture runner `validate_fixtures.py`, and `rsc.py compile --check`. Five commands,
    and nothing fewer. A name here may also belong to an unrelated file in this
    repository, so a caller identifies each command by its battery leg inside its own
    tree and never by name-matching against this one.
  - A command whose subject is not in the repository being verified is not owed there,
    and the verification record names the repository it ran in, so review can
    re-classify. **This addresses the enumeration; it does not shorten it** — each of the
    six is still owed by the tree that holds what it tests, so `HD-42`'s "a subject
    disappearing does not license editing this enumeration again" is not spent here: no
    entry is struck. What is genuinely given up is the incidental coverage a construction
    round in one repository used to take from the other's legs — bounded, though not by any
    rule here, by how the two trees move: a gitlink bump is not a prose/markdown path, so a
    caller-side batch carrying one is never doc-only, and the caller's five legs run at every
    bump. Enumerated at all because
    the earlier four-item phrasing authorized less than the battery is: it under-ran
    twice (batch B R1 and R3) and both times only the executor's private knowledge caught
    it. It was eight until `HD-42` (2026-08-15): the two struck entries were the v1
    stage-control and v2 harness `run_tests.py` runners, whose trees `HD-39` deleted in
    that same commit.
- The tier is derived from the actual diff and stated where the verification is
  recorded (commit body or CandidateRecord), so review can re-classify it.

Witnessed cost, **corrected 2026-08-03 under `E3`** by the 保障面二期复盘 (journal
`retro-2026-08-03.md` §3, held by this instrument's own construction history and not by a
repository that runs against it): the battery is **~85% of an
evidence pass, and a pass is ~2.4 minutes, not ~10**. Measured — the p5a-shells pass ran
its 17 checks in 2m22s (`chk-*.out.txt` mtimes `00:08:34`→`00:10:56`), the pytest leg
alone ~108s of it; the battery run directly totalled 130s **at the p5a-shells revision**
(P2 29 + P4 80 + P5A 32 + fixtures 58 + pytest 556). Those sub-tallies are a measurement
pinned to that revision, not a standing fact — these five legs have only gained tests
since (deleting a battery command removes its tests from the battery, which `HD-42` did
to two other legs in this same batch), and the sentence that used to end this
parenthesis, "tallies reproduce exactly", was false by `ddd773a`: P5A had reached 39 and
pytest 701. Re-run the battery for a current figure rather than
trusting any list written here (`HD-41` ③). Measured again at `a8af54c`, six legs:
107s total, of which pytest is 106s. Measured once more 2026-08-18 across both trees, on
the tree this round's candidate was cut from (its bases: instrument `0d73a5f`, caller
`6fd0ae3`) — this is the measurement that made the bullet above address repositories
rather than one list: the instrument's single leg is `712 passed in 93.67s`, while
`pytest` in the caller collects `no tests ran`; the caller's five legs are 29, 80 and 39
tests, 58 fixture cases, and `compile --check` exit 0, and none of those five scripts
exists in the instrument. The ruling's original
figure, "~7–8 of the ~10 minutes", was right in ratio and wrong in magnitude by ~4×; that
FULL's O2 had already marked the minutes half as carrying no repo lock. **So what this
tiering buys is ≈2 minutes per doc-only pass, not ≈8** — weigh the revert anchor below
against that number, not the original one.
Until this ruling, doc-only construction batches skipped the battery by precedent
(AUDIT-CADENCE, PRE-START-OPT — each accepted by its FULL); this section makes the
practice a rule and extends it to evidence passes.

**Revert anchor (user condition, part of the ruling):** this trades the battery's
incidental coverage on doc-only passes for time. If reviews after its adoption start
returning `SPEC_GAP`s or blockers whose ground a skipped battery would have caught,
this section is the part to suspect and the unit to delete — **removing this whole
section restores the prior rule (full battery on every pass); nothing else depends on
it.** The deleting commit's body must state that the AUDIT-CADENCE / PRE-START-OPT /
BATTERY-TIERING precedent is retired with the section — after the revert, a doc-only
pass owes the full battery notwithstanding those records.

**What exercising it costs now (2026-08-18 user ruling, rider `tier-scope` ②).** The
anchor stands; the price the 2026-08-03 ruling implied does not. `HD-14` (`418b89c`)
moved this section into the instruction layer, and deleting an instruction-layer section
changes what a rule requires — so the revert is a design round under `E10`, not a
one-commit revert, and the moving commit disclosed no such cost. Read the anchor as it
now is: still the single unit to delete, still nothing else depending on it, and a round
to exercise.

## Instruction authoring rules (routed from run findings)

- **Standing run-conduct discipline arrives with the dispatch, never inside the
  instruction** (round `EXECUTOR-CHARTER`, user ruling 2026-08-22 — a partial supersession
  of p4-bridge finding f1's routed WORKFLOW_FIX,
  `user-decision-triage-conduct-prose-in-normative-preamble`, 2026-08-01, which had the
  instruction carry the reference from its Context section): the rules the session runs
  under — gap banking, first-run obligations, map-filling disclosures — live in this file
  and the governing plans; `dtw dispatch --executor` names this file to the executor at
  startup, the plans arriving with the instruction and subject the orchestrator delivers
  ([ORCHESTRATION.md](ORCHESTRATION.md)'s *Handing the executor its instruction* is that
  obligation's text, and since 2026-08-22 it enumerates the plans),
  so the instruction no longer carries even the reference. What survives of the 2026-08-01
  decision is strengthened, not replaced: conduct prose still never enters normative
  preamble — a restated conduct sentence sits in no obligation and no context-unit, and
  narrows the START approval surface invisibly, the defect p4-bridge's same-source maps
  both missed — and the Context section now carries **background only**: anything
  demand-shaped in Context is a defect on sight, whether it restates standing discipline
  or originates a demand of its own, because a demand written there anchors no instruction
  unit, is representable as no obligation, and therefore reaches no check, no review
  disposition and no evidence. The half replaced is "reference it from Context"; that
  delivery job is the dispatch's now. One rendering consequence follows and is settled
  here: `dtw preview`'s elision of the Context body from the START card is correct, not
  merely honest — nothing normative may legitimately sit in the elided span.
- **Instruction first: the plan channel is overflow, never a second instruction** (round
  `PRERUN-RIDERS`, user ruling 2026-08-22, the bound the same ruling attached to making the
  governing plans a delivered item). What an instruction **can** carry goes in the
  instruction — obligations, the run's own data, the demands this run makes — because that
  is the surface the freeze pins, the START card presents, the user approves, and a check, a
  disposition and a review verdict all reach. The plans take only what the instruction
  cannot: conduct prose, which the bullet above bars from preamble and from Context alike,
  and stage-standing discipline that spans runs and so is no single instruction's to state.
  The failure this bound exists against is a demand the instruction could have carried,
  written into a plan instead: it is then outside the approved surface by a route the
  executor has no reason to distrust and the reviewer has no reason to walk.
- **The dispatch paragraph gets a standing context-unit**: a work order's opening
  "produce, and route for signature" paragraph carries an imperative; give it a
  context-unit whose rationale names where each half is carried (the obligations
  restating the produce half; the workflow step carrying the route half).
- **Mechanically comparable demands bind a comparison, not a locator proxy**
  (p4-bridge finding f2, routed WORKFLOW_FIX by
  `user-decision-triage-locator-checks-proxy-verbatim-demands`, 2026-08-01): when an
  obligation's deterministic half is an equality question — a verbatim quote of a signed
  clause, structural equivalence with a pinned source — bind a `command_exit` check
  running a comparison script against the materialized candidate and the pinned
  revision; keep `locator_exists` for presence demands only, because a locator is a
  presence oracle and passes for any paraphrase containing its anchor words. Since
  SIMP-A1 the two halves are **two obligations**, not one obligation in two minds: the
  equality is a `local_check` its comparator decides outright, and the semantic residue
  is a separate `review_only` whose rationale names what the comparator cannot see.
  Review still reads the comparator once (right passage, right file, right pinned
  revision; normalization whitespace-only) — that is evidence verification and it stays.
- **Checker authoring rules** (banked at the p5a-shells closeout `9ba9bbc`; user-activated
  2026-08-03): a check that parses a column asserts it — parse-and-discard leaves the
  parsed property review-borne (p5a-shells' checker parsed appendix §A's host column and
  discarded it, so declared-host/owner placement was hand-carried across 148 shells);
  additive and prose modes pair added and removed lines per file, never pooled repo-wide
  (a removed line in one file must not be excusable by an unrelated append in another); a
  declared-order demand compares the whole order, not the first key; and every
  script-decidable demand the WorkSpec leaves review-borne is named in the freeze-time
  disclosure (instruction text or the audit round history), so the FULL inherits a list,
  not a discovery. Sources, both held in the caller that grew this harness rather than
  here: the FULL record `v3-review-full-86defbc.md` f1–f2, and audit rounds 4 o1–o2 and
  6 f1 in p5a-shells' `audit-rounds.md`.
- **The comparator is a template member: `compare_blocks.py`** (first instantiated by
  p4-doc; templated with two `VERIFIER_FIX` repairs routed by that run's
  `user-decision-triage-comparator-environment-defects.json`, an issue record held with its
  run in the caller that grew this harness, 2026-08-01 — explicit UTF-8 subprocess
  decoding, and `--rebuild` judged against
  `git show` blob bytes instead of eol-sensitive working-tree status). Copy it beside
  the instruction and **freeze both in the base commit**: the materialized candidate
  tree must carry the comparator for `subject_tree: candidate_commit` checks to reach
  it. Run every python `command_exit` argv with `-X utf8` on Windows (the p4-doc
  precedent).

## What you are never asked to do

Prove that your work is correct. The assurance statement is bounded on purpose (contract §1):
every obligation is accounted for, one independent challenge occurred, residual uncertainty
was disclosed. Nothing in v3 claims semantic truth was proved — so the goal is never to make
the report look clean, it is to make the real state of the work visible.
