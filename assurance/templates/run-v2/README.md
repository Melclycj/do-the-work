# Run template v2 — commit-first review subject (wave 2)

The successor run shape for document-assurance runs, per contract supersession-1
(`contract/Document-Work-Assurance-Contract-v3-supersession-1.md`) and the
adjudicated wave-2 design. Instantiate at `ResearchSystem/assurance/runs/<run-id>/`; as of
the shared-core round (A2-R3, `HD-11` part two, 2026-08-09) that no longer means copying
the step scripts in. The six shared scripts — `run_evidence_v2.py`, `run_bind_v2.py`,
`run_repair.py`, `run_retire.py`, `check_template_instance.py`, `make_paragraph_map.py` —
are called **in place** from
`assurance/templates/run-v2/` against the run directory, zero copies. None
of the six has **a CONFIG block to fill** (`HD-11` part one, R2): every one takes the run
directory as its first argument, and the three step scripts additionally take the round's
refs as CLI flags
(`python assurance/templates/run-v2/run_evidence_v2.py <run-dir> --base
--candidate --candidate-branch`;
`python assurance/templates/run-v2/run_bind_v2.py <run-dir> --evidence-commit
--bound-at [--emit]`;
`python assurance/templates/run-v2/run_repair.py <run-dir> [--emit]`;
`python assurance/templates/run-v2/run_retire.py <run-dir>`) — and every
one of the six reads its per-run constants from the run's own `control/` JSON.
`run_retire.py` is the retirement step (`HD-12`): once `state.json` reaches `CLOSED` it
deletes each per-CheckResult file the committed plan's `check_order` names, leaving the
aggregate `check-results.json`, every raw `<check_id>.out.txt`, and
`assurance-candidate.json`'s `check_result_refs` alone — a retired file's digest still
verifies against the evidence commit in git history.

Instantiating a run still means creating or copying three things. **`compare_blocks.py`**
is the one template member still copied — beside the instruction and frozen with it,
because the instruction authoring rule requires the materialized candidate tree to carry
the comparator itself (`document-harness/EXECUTION.md`'s frozen rule,
unchanged; see below). **The run's own scripts** — `build_run.py`, and, following the
w1-r1 precedent, `run_start.py` / `run_final.py` / `run_triage.py` — stay self-authored per
run rather than templated (see "Steps that did not change" below), alongside whatever
one-off checker a run needs for its own local questions. Two of the eight closed runs also
carry a self-authored `run_closeout.py` (p4-doc, p4-bridge): that name is the run-own
**post-run issue step** — filing HarnessIssues and burden figures — and has nothing to do
with the template's `run_retire.py`, which retires CheckResults. And **three files under
`runs/<run-id>/control/`** carry the per-run constants named above — they are the run's to
create, so they are named here as the specification they are, not as paths that resolve
today:

- `state.json`'s `repair_round` is the round every step acts on, so the round lives in one
  place instead of in two hand-synced copies (it was a knob in each script before R2);
- `fulfillment.json` is the executor's per-obligation status map, one entry per
  `obligation_id`, with no default and no derived status;
- `bind-declarations.json` carries the two things the bind step may not derive:
  `governance_scan` (whether the governance-frontmatter scan ran, and the honest
  `skip_reason` when it did not) and `disclosures`.

A missing file or a missing key refuses the step; nothing is defaulted.

`compare_blocks.py` takes no run directory: the instruction
authoring rule has the comparator copied **beside the instruction** and frozen with it, so
the materialized candidate tree carries it, and every mode runs with the repo root of that
materialization as its working directory. Its per-run constants — pinned source, owner files, object sites, declared prose
suffixes, generated files and their rebuild command — are CLI arguments too, carried after
the mode flag by the frozen `argv` of the check spec that binds that mode; a mode invoked
without the declarations it needs refuses rather than comparing nothing.

w1-r1 established the layout conventions this template inherits; they are
**load-bearing** here:

- control root = `ResearchSystem/assurance/runs/<run-id>/`, with
  `control/` (state, work-spec, resolved-plan, check specs, decisions) and `evidence/`
  (candidate-record, coverage, check results) beneath it;
- state at `runs/<run-id>/control/state.json`; **one file per CheckResult** at
  `evidence/check-<check_id>.json` (`review_subject.CHECK_RESULT_PATH`) for the run's
  life — retired at closeout (`HD-12`);
- state pointers are authored via `assurance_state.pointer_for`, which writes a **BYTES**
  digest — never a hand-supplied canonical one — on the fields in
  `assurance_state.DIGEST_PROTECTED_FIELDS` (`work_spec_ref`, the three decision refs,
  `review_ref`) and the path alone on every other field. Those five name files whose
  current version the executor is not entitled to produce; elsewhere a digest the executor
  computes over a file it may legitimately rewrite binds no one, so it is not written
  (2026-07-29 narrowing). Of the five, only `review_ref` is written by these scripts
  (`run_bind_v2.py`); the other four are authored outside this template.

## What changed from the w1-r1 shape

1. **No ReviewPackage.** After the evidence layer is clean, the controller **commits the
   control plane** — an *evidence commit* on the run's working branch, touching only the
   control root (same-branch topology, design §3.1; the payload candidate stays on its own
   isolated branch until FINAL promotion). `check_subject` verifies the commit is
   complete, identical to what its CandidateRecord records, and contained in the control
   root. The dispatched review subject is **that commit's SHA and nothing else**.
2. **The reviewer re-derives.** There is no member list to hand over; the reviewer reads
   the committed control plane and the pinned revisions the WorkSpec and CandidateRecord
   name (`read_control_plane` is the cold-start entry: SHA in, control plane out).
3. **The ReviewResult is v2** (`review.v2.schema.json`): root `schema_version` `"2"`,
   `subject` binding in place of `package_ref`. The bind step runs
   `check_review_result_v2(result, repo_root, evidence_commit=...)`.
4. **Repair (round 1)** regenerates every evidence document AND commits a **new** evidence
   commit (`check_repair_regeneration_v2`); the round-0 evidence commit is never reused.
   The round is carried by `repair_round` in the run's state file (`runs/<run-id>/control/`
   — no CONFIG knob since R2); it drives the CandidateRecord,
   the review subject **and** the state's `next_action` (below). In the bind step it also
   decides the operative review (round 1 validates the targeted VERIFY and reconciles it
   against the user's repair decision) and re-points `review_ref` at it, while the
   AssuranceCandidate binds every round that happened (`run_bind_v2.py`, defect M9).

> **The rule sections moved (R1, `HD-14`, 2026-08-09).** The six rule sections this README
> carried — *Pre-freeze gate* · *Instruction form* · *Authoring gate* · *Audit cadence —
> pre-START rounds* · *Regression-battery tiering* · *Instruction authoring rules* — are
> instruction-layer text now: read them in `document-harness/EXECUTION.md`.
> This file holds template instantiation only.

## Steps that did not change

`run_start` (START decision), `run_final` (FINAL decision + explicit promotion),
`run_triage` (HarnessIssue triage) keep the w1-r1 shape — see
`../../runs/w1-r1/run_start.py`, `run_final.py`, `run_triage.py` as the worked precedent
rather than a copy here that would drift (N0-A6).

**`run_repair` — the step a repaired path owes, and the only one this list used to omit**
(issue-p5b-claims-repair-step-unnamed-in-readme, routed WORKFLOW_FIX 2026-08-07). Between
the round-0 bind stopping at REVIEWED and the round-1 evidence pass there is one transition:
record the user's REPAIR decision, run `flow.check_repair_decision`, advance to REPAIRING.
It is templated here as `run_repair.py` rather than left to precedent, because unlike the
three above it has no w1-r1 instance — w1-r1 was never repaired — and because its omission
is *silent*: nothing refuses at the time, and the run learns of it rounds later when
`dtw dispatch` declines the VERIFY for a state carrying no `repair_decision_ref`. p3-corr
wrote the transition by hand; `../../runs/p5b-claims/run_repair.py` is the worked instance,
and its docstring shows the run-local habit of recording which findings were accepted and
which were carried to FINAL unrepaired.

So four steps are templated — evidence, bind and repair because the supersession changes what
each of them owes, and retire because `HD-12` created it; the three named at the top of this
section are not.
