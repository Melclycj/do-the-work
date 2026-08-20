# V3-N1 administrative record — obligation-to-evidence vertical slice

Node: `V3-N1` of [[document-work-assurance-harness-v3.plan|the v3 plan]] §9. Sole writer: the
execution session.

Write rules, stated in the same precise form the N0 record settled on: **§9 is the
append-only log** — entries are added, never rewritten or reordered. **§10 is a cumulative
register** — rows are appended and existing rows may be sharpened when a later finding
changes what must land, and every such change is itself logged in §9. **§§1–8 record this
node's own facts and are not rewritten once the node closes.** Nothing here weakens the rule
that signed contract and approved plan bytes are never modified.

> [!done] Node closed — user-signed 2026-07-20
> Signed candidate: `802e16a` (`V3-N1-REVIEW-FIX1-CANDIDATE-v1`). Plan §8 budget at close:
> **FULL used (1/1), user-approved fix used (1/1), targeted VERIFY NOT used (0/1).**
>
> The unused VERIFY is not an accounting detail and must not be read as one: plan §8 *permits*
> a targeted VERIFY, it does not require one, and the user exercised that discretion. The
> consequence is concrete — **the F1/F2 fix at `802e16a` was never independently verified.**
> It was reproduced, pinned by tests, mutation-checked and re-run green by the execution
> session, all of which is executor-side evidence. Recorded as residual N1-R1 (§10).
>
> Earlier §9 entries that state "no valid FULL review has occurred" and "the node awaits its
> targeted VERIFY" were true when written and are superseded by the entries below them; §9 is
> append-only, so they stand as written rather than being rewritten.
>
> **⚠ CORRECTED 2026-07-20 — this box is wrong about the VERIFY.** The targeted VERIFY *was*
> performed and returned `PASS`; the correct accounting is **VERIFY used (1/1)** and the F1/F2 fix
> **was** independently verified. The result had not reached the execution session when this box
> was written. The wrong text above is left standing rather than rewritten, exactly as this record
> treats every other superseded claim — **the §9 errata dated 2026-07-20 is authoritative**, and
> residual N1-R1 is discharged in §10. Read neither the numbers nor the "never independently
> verified" sentence above as current.

## 1. Authorization and base (plan §9, V3-N1 IN)

- **N0 closed and signed:** VERIFY `PASS`; the user signed V3-N0 on 2026-07-20, binding
  contract blob `b2dbdf752d8c155e4c65b14b5f420b880b8184a1`, payload candidate `85742ae`
  and closeout `9bda771` ([N0 record §8](../N0/N0-record.md)).
- **N1 authorization:** the user explicitly authorized V3-N1 on 2026-07-20, which is what
  the N0 stop gate required ("V3-N1 is not yet authorized — it requires an explicit user
  authorization at the start of the next session").
- **IN:** the signed N0 interfaces (Contract v3 + the seven N0 schemas) and the exact reuse
  decisions in [N0 record §4](../N0/N0-record.md).
- **OUT (not touched by this node):** ReviewResult, repair, final decision, cutover,
  P4 and any business content.

## 2. Change boundary actually used

The plan's V3-N1 allowlist is narrow, and one consequence is easy to miss:
**`.goals/LEDGER.md` is not on it.** The node's only permitted existing file is
`ResearchSystem/tooling/rsc.py`. This record is therefore N1's durable progress ledger; no
LEDGER pointer is written at this node.

| Path | Basis |
|---|---|
| `ResearchSystem/tooling/rsc.py` | allowed existing file, v3 subcommands only |
| `ResearchSystem/schema/document-assurance-v3/local-check-spec.schema.json` | allowed new file |
| `ResearchSystem/schema/document-assurance-v3/candidate-record.schema.json` | allowed new file |
| `ResearchSystem/tooling/rsclib/document_harness/**` | allowed new root (nine named modules) |
| `ResearchSystem/tooling/tests/document_harness/**` | allowed new root |
| `ResearchSystem/migration/document-work-assurance-v3/N1/**` | allowed new root |
| `ResearchSystem/generated/document-assurance/test/**` | allowed new root |

## 3. Interfaces handed forward

| Interface | Where | Note |
|---|---|---|
| validated `DocumentWorkSpec` | `document_harness/spec.py` | schema + the bidirectional unit↔obligation spine |
| `DocumentAssuranceProfile` promotion threshold | `document_harness/assurance_profiles.py` | one rule family, owner, reason to change, two distinct real witnesses |
| rebuildable `ResolvedAssurancePlan` | `document_harness/assurance_plan.py` | resolver `1.0.0`; byte-rebuildable; conflicts fail closed |
| `AssuranceWorkState` + cold resume | `document_harness/assurance_state.py` | pointers only; digest-verified resume |
| `InstructionCoverageAudit` + START binding | `document_harness/instruction.py` | exact plan + audit digests; one approval path |
| `CandidateRecord` partitions | `document_harness/candidate.py` + `candidate-record.schema.json` | controller envelope, executor `fulfillment`, diff-verifier `manifest` |
| `LocalCheckSpec` / `CheckResult` | `document_harness/checks.py` + `local-check-spec.schema.json` | closed six-kind union; unknown kind is `SPEC_GAP` |
| coverage view | `document_harness/views.py` | disposable three-column join; the review column is deliberately absent |

### 3.1 Why the shared primitives live in `__init__.py`

The plan fixes V3-N1's module list by name; no primitives module is authorized. Canonical
digesting and schema validation are needed by every module, so the package root is the only
place a shared foundation can sit. `__init__.py` therefore holds them and imports no
submodule, so no import cycle is possible.

## 4. Nominated reuse — how the adaptation actually landed

[N0 record §4](../N0/N0-record.md) assigned three of the five nominated primitives to this
node, all with disposition **adapt**. No primitive received `reuse` (verbatim import), and
the historical-only default (N0 record §3) makes importing `rsclib.harness` from v3 code a
`SPEC_GAP`. Every one is therefore re-implemented in `document_harness/` rather than
imported, and the differences are deliberate:

| # | Primitive | v1/v2 asset consulted | What v3 carries | What v3 deliberately drops |
|---|---|---|---|---|
| 1 | Canonicalization / content binding | `rsclib/harness/c14n.py` | NFC key+string normalization, duplicate-key rejection, float rejection, sorted keys, `,`/`:` separators, UTF-8 without BOM | the `sha256:` prefix form — the v3 schemas declare a **bare** 64-hex `sha256`, so a prefixed digest would not validate |
| 2 | Closed JSON-schema validation | `rsclib/harness/schemas.py` + the A2 fixture-runner pattern | frozen pack under `schema/document-assurance-v3/`, fail-closed unknown kind, per-file pack digest | the v2 report/fault types (`rsclib.harness.report` is not nominated); v3 defines its own `Issue`/`Report`/`SpecGap` |
| 3 | Git path/diff observation | `rsclib/harness/gitadapter.py` | exact-base `--name-status` diff, segment-boundary case-insensitive path containment, fail-closed git faults | enforcement-level vocabulary, capability/lease logic, and the `resource://` URI algebra — v3 uses normalized local paths and an **acceptance** boundary that never claims to have prevented a write (V3-D3) |

Two further behaviours were added rather than carried, because the v2 asset had no
equivalent: renames are disabled (`--no-renames`) so a moved file is observed honestly as a
delete plus an add, and every read states which tree it came from (§5, R1).

## 5. Residuals discharged at this node

[N0 record §9](../N0/N0-record.md) carried three residuals to V3-N1. A node that closes
without discharging its assigned residual is incomplete, regardless of its own acceptance
IDs.

### R1 — which tree did the check observe?

Discharged in the interface, not only in the code. `CheckResult.observed_tree` is a required
field carrying `{kind, revision}`, and `LocalCheckSpec.subject_tree` declares which tree the
request is entitled to observe. Two mechanical consequences:

- the five kinds whose claim is about the payload candidate (`file_exists`, `json_schema`,
  `markdown_link`, `locator_exists`, `git_diff_boundary`) return `WRONG_SUBJECT` — never
  `PASS` — when they declare the working tree;
- `command_exit` runs a real process against files on disk, so a command claiming to observe
  the candidate is honoured only when the checkout HEAD *is* the candidate commit, and
  returns `WRONG_SUBJECT` otherwise.

Candidate reads go through `git show <rev>:<path>`, so the candidate tree is read out of the
commit rather than off disk. `WorktreeReader.revision` records the HEAD at observation time
and its docstring states plainly that this does **not** certify the bytes that were read.

### R3 — the vocabulary guard was blind to `const`

The N0 fixture runner scanned property names, `$defs`, `required` lists and `enum` values but
never `const`, so a schema could express a forbidden surface term as a `const` literal and
pass. The N0 runner is frozen and was not touched. The extended scan lives in the N1 test
matrix, covers `const` in addition to the four original positions, and is applied to all nine
schema files — the two authored here and the seven inherited from N0. It carries its own
self-test: a synthetic schema containing a forbidden `const` must be flagged, so a guard that
silently scanned nothing could not masquerade as a passing guard.

### R4 — a governance document carrying its own approval status

The rule already existed in prose (contract §14, plan §0). It is now mechanical, in
`checks.governance_scan`, and reached through the existing `command_exit` kind — **not** a
seventh check kind, which would contradict the closed union frozen by Contract v3 §5.

All three specification constraints R4 declared mandatory are implemented:

- **(a) parsed frontmatter keys, never a raw text scan.** Only top-level keys of a leading
  `---` block are in scope. A document that merely *quotes* a forbidden field while
  explaining the defect is not flagged — which is exactly what the N0 record's own errata
  does.
- **(b) exact field-name match, never substring**, with an explicit `*_owner` whitelist.
  `approval_status_owner` and `signature_owner` are the *correct* pattern — they name who
  owns the approval state without carrying it — and must pass. A substring rule would turn
  the correct pattern into a false positive, and false positives are how a real check gets
  switched off.
- **(c) blob-keyed, enumerated grandfather list**, in
  [`governance-exemptions.json`](governance-exemptions.json), outside the checker. Two
  documents are exempted because the rules forbidding their edit are the same rules the check
  protects: the approved plan blob `8ad404b1…` (`status: candidate-plan`, plan §0/§13) and
  the signed contract blob `b2dbdf75…` (`status: candidate-awaiting-user-signature`,
  contract §13 plus the N0 §8 errata ruling). Both blobs were independently recomputed at
  this node with `git hash-object` and match the values the N0 record registered at
  signature. The exemption **fails closed**: edit one byte, the blob changes, and the
  exemption evaporates by itself. An entry grandfathers only the fields it lists; an
  additional self-approval field on an exempted blob is reported as
  `V3-GOVERNANCE-EXEMPTION-NARROWER` rather than passing.

## 6. Deliberate non-implementations

Each of these is scoped to a later node by the approved plan. Recording them here prevents a
later reader from mistaking an absence for an oversight.

| Not implemented | Owner | Why not now |
|---|---|---|
| `AssuranceWorkState` terminal status↔pointer conditionals (N0 residual R2) | **V3-N2** (`N2-A7`) | the pointers involved (`summary_ref`, `assurance_candidate_ref`, `repair_decision_ref`) point at objects V3-N2 creates; N1 does not preclude the rule |
| status transition legality | **V3-N2** (`flow.py`) | N1 stops before review, so a transition table written now would be a guess about statuses N1 cannot reach |
| per-obligation review disposition column in the coverage view | **V3-N2** | an empty review column would read as "reviewed, nothing found" — the unsupported-completion claim this product exists to prevent |
| `ReviewPackage`, `ReviewResult`, repair, `AssuranceCandidate`, `AssuranceSummary`, `HarnessIssue` | **V3-N2** | explicitly OUT for V3-N1 |
| any v3 default entry / cutover | **V3-N4** | conditional on the N3 adoption decision |

## 7. Honesty boundaries of what this node built

- Role separation is a workflow protocol, not an OS guarantee. The mechanical part — that
  the executor did not also author the manifest, the check results or the coverage
  certification — is enforced; nothing here prevents one operator from playing both roles.
- `require_publishable` checks that two reuse witnesses are *distinct* and that neither
  points into a test or fixture root. Whether the referenced work was real remains a human
  judgment.
- The `markdown_link` oracle resolves inline Markdown links only. Wiki-style double-bracket
  links need a vault index and are out of scope for the closed union; they are not silently
  reported as resolved — they are simply not inspected.

  (This sentence originally spelled that link form out literally, and `repo-audit.py` flagged
  the record as containing a broken link — a raw-text scanner flagging a document for
  *describing* the syntax. It is the same false-positive class R4 constraint (a) exists to
  prevent, arriving from the opposite direction. Worth recording: the v3 governance scan
  parses structure and would not have made this mistake; the audit tool does not, and that
  is a real limitation of the audit, not of this record.)
- A locator is a literal anchor that must occur exactly once. Zero occurrences and multiple
  occurrences both fail: an ambiguous anchor does not identify a location.

## 8. Deterministic results

Every figure below was produced by running the named command, not by inspection. Per residual
R1, each entry states **which tree it observed**.

### 8.1 N1 acceptance matrix — 110/110, exit 0

`python ResearchSystem/tooling/tests/document_harness/run_tests.py` → `Ran 110 tests` / `OK`.
Observed tree: **worktree** (the suite builds its own disposable Git repositories; it never
reads this repository's payload).

| File | Tests | Covers |
|---|---:|---|
| `test_spec_plan_state.py` | 33 | N1-A1, N1-A2, N1-A3, N1-A4, N1-A10, plan rebuildability §5.2, profile accumulation |
| `test_candidate_checks.py` | 72 | N1-A5, N1-A6, N1-A7, N1-A8, N1-A9 (seven named negatives), R1, R3, R4, emitted-result conformance |
| `test_golden_views.py` | 5 | the pinned user-facing coverage view and the disposable coverage document |

The two acceptance halves were authored in **fresh contexts that did not write the
implementation**, and the golden plus the conformance regressions were authored by the
execution session. That split is why the matrix found defects rather than confirming
assumptions (§9, D1/D2).

### 8.2 N1-A11 — the three retained suites stay green

Observed tree: **worktree**.

| Suite | Result |
|---|---|
| `tests/stage_control/run_tests.py` (v1) | 20 run, 0 failures, 0 errors |
| `tests/run_tests.py` (P2 compiler + shadow lint) | 29 passed, 0 failed |
| `tests/harness/run_tests.py` (v2 A3) | 39 run, `OK` |

**Zero repository writes by the suites themselves.** A `git status --porcelain` snapshot
taken before and after the verification run is byte-identical, which was checked explicitly
because two of the retained code paths (`generate.write_artifacts`,
`stage_control.write_control_view`) are capable of writing into the repository and a stray
write would have silently broken this node's changed-path verification.

### 8.3 Repository audit — exit 0, clean

`python Thesis/Work/Tooling/repo-audit.py` → `RESULT: clean (exit 0)`, scope **248 markdown
files**. Observed tree: **worktree** — the audit reads working-tree bytes, which is what this
node's uncommitted candidate content is; the same worktree-scope caveat R1 recorded at N0
applies unchanged.

One hard issue was found and fixed during this run, and it is worth recording rather than
quietly repairing: §7 of this record originally spelled out the wiki double-bracket link
syntax literally while *describing* it, and the audit's raw-text link scanner flagged the
record as containing a broken link. That is exactly the false-positive class R4 constraint
(a) exists to prevent — a scanner flagging a document for documenting a syntax — arriving
from the opposite direction. The v3 governance scan parses structure and does not have this
blind spot; `repo-audit.py` does. Soft findings: 56 orphan notes (55 pre-existing; this
record is the 56th and is necessarily orphaned, because nothing in the N1 allowlist may link
to it — the N0 record is outside this node's writable set).

### 8.4 Changed-path allowlist — 22 paths, zero out-of-boundary

`git diff --name-only 2b1983f` plus `git ls-files --others --exclude-standard` → **23 paths**,
of which 22 belong to this node and each maps to a §2 allowlist row:

| Bucket | Count |
|---|---:|
| `ResearchSystem/tooling/rsc.py` (v3 subcommands only) | 1 |
| `ResearchSystem/schema/document-assurance-v3/**` (the two nominated schemas) | 2 |
| `ResearchSystem/tooling/rsclib/document_harness/**` (the nine named modules) | 9 |
| `ResearchSystem/tooling/tests/document_harness/**` | 5 |
| `ResearchSystem/migration/document-work-assurance-v3/N1/**` | 2 |
| `ResearchSystem/generated/document-assurance/test/**` | 3 |

The 23rd path, `ResearchSystem/docs/General-Harness-v2-Design.md`, is **not** part of this
node: it is the untracked parallel-agent file that already existed before N1 opened. The
user ruled at N0 that it stays untracked and outside the candidate ([N0 record §3](../N0/N0-record.md)),
and this node did not touch it, does not stage it and does not retain it.

No controller code outside the nine named modules, no A4 import, no business content, no
old-file deletion and no `.goals/` write appears in the diff.

## 9. Append-only log

- 2026-07-20 — node opened. User signed V3-N0 and authorized V3-N1 in the same message.
  Boundary re-derived from plan §9 before any write; the absence of `.goals/LEDGER.md` from
  the N1 allowlist was found at that point and this record was made the node's ledger (§2).
- 2026-07-20 — interfaces frozen: `local-check-spec.schema.json` and
  `candidate-record.schema.json` authored and checked as valid Draft 2020-12 with resolving
  `$ref`s; the nine authorized modules implemented.
- 2026-07-20 — N1-A11 regression run early, before the acceptance matrix existed, to close
  the risk that a retained suite writes into the repository: v1 stage-control 20/20, P2
  compiler 29/29, v2 harness 39/39, all green, and a before/after `git status --porcelain`
  comparison showed **zero repository writes** by the suites themselves.
- 2026-07-20 — R4 exercised end-to-end through `rsc v3 governance-scan` against the two real
  immutable governance documents: flagged without the register (exit 1), clean with it
  (exit 2 blob matches, exit 0).
- 2026-07-20 — self-review during implementation found N1-A7 only half enforced: the
  manifest's sole-author rule was checked on the record, but nothing checked that a
  `CheckResult` was not authored by the executor. Enforcement added in `views.coverage_report`
  (`V3-COVERAGE-EXECUTOR-AUTHORED-RESULT`), which is the first point where the executor's
  identity and the results meet.
- 2026-07-20 — **two implementation defects found and fixed before submission.** Both are
  recorded because the way each was found matters more than the fix.
  - **D1 — an unvalidated escape path.** The independent test author reported that
    `run_check`'s wrong-subject ruling returned early and never reached
    `validate("check_result", …)`. For `git_diff_boundary` that emitted a schema-invalid
    result claiming neither `boundary_observed` nor `base_revision`. Reproduced directly
    before accepting the report. Fixed in two places: the subject-tree ruling now returns
    through the single validation point in `run_check`, and the schema requires
    `boundary_observed`/`base_revision` only when the check actually **ran** (`PASS`/`FAIL`)
    — the same rule already applied to `exit_code`, since naming a boundary as "observed"
    when no diff was taken would invent evidence. The defect was invisible at run time
    precisely because the unvalidated path was the one that never checked anything.
  - **D2 — a schema-valid request could crash the runner.** The regression written for D1
    was deliberately widened to the whole kind × subject_tree cross-product rather than the
    one reported case, and it immediately surfaced a second, independent defect: a
    `json_schema` request whose subject and schema paths coincide emitted the same subject
    twice, violating `uniqueItems` and raising `SpecGap` instead of reporting an outcome.
    Fixed by collapsing repeated observations of one path into one subject
    (`_dedupe_subjects`). A valid request must always produce a reported result; crashing
    would take the run down instead of recording what happened.
  - Method note worth keeping: D2 exists in this record only because the D1 regression was
    written against the defect **class** ("a result escaped without validation") rather than
    the reported instance. A test written to the report alone would have passed and left D2
    in place.
- 2026-07-20 — **D3, a third defect: two named invariants were permanently unreachable.**
  The second independent test author reported that `check_plan`'s
  `V3-PLAN-CANONICAL-FACT-COPIED` and `V3-PLAN-REPAIR-CAP` could never fire: the function
  validated the schema first and returned early, and the schema's `additionalProperties:
  false` and `repair_cap: {const: 1}` already reject those documents. Reproduced before
  accepting. The acceptance property itself always held — such a plan *is* rejected — so this
  was not a correctness bug; it was a **reporting** defect. Fixed by running both invariants
  first and unconditionally (both are plain key inspections that assume nothing about shape),
  so a report now carries the specific reason (a copied canonical fact drifts from the
  WorkSpec it claims to resolve, N0-A6; the repair cap is V3-D6's bounded-convergence
  guarantee) alongside the generic schema error. Deleting the dead code was the other option
  and was rejected: in a governance record the reason is the part worth reading, and a
  greppable code per invariant is what makes it auditable. The author's two tests were
  strengthened to assert both codes rather than documenting the shadowing.
- 2026-07-20 — deterministic results measured and recorded in §8: acceptance matrix 110/110,
  three retained suites 20/29/39 with zero repository writes, repository audit clean at exit 0
  after one hard issue in this record was found and fixed, changed-path set 21 in-node paths
  with zero out-of-boundary. The node now awaits its independent bounded review (plan §8).
- 2026-07-20 — **pre-submission correction of §8.4, and a terminology correction to this log.**
  Authorized by the user on 2026-07-20 as a **pre-submission correction, not the V3-D6 fix
  round**: no valid FULL review has occurred, so there is no review finding to respond to.
  **The fix round and the VERIFY remain unused; the review budget is intact.**

  **(1) The changed-path count was wrong.** §8.4 read 21 in-node paths / 23rd-path arithmetic
  of "22 paths"; the candidate `74e8154` actually contains **22** in-node paths, with **3**
  under `generated/document-assurance/test/**`, and 23 observed once the untracked
  pre-existing file is added. Corrected in §8.4 (§§1–8 are rewritable until the node closes).

  **How the wrong number was produced, which matters more than the number.** The paths were
  counted, and only afterwards was `.gitattributes` added to that directory — to stop Git
  rewriting the goldens' line endings, which would have broken the byte comparison on a fresh
  checkout. The count was never re-run, yet §8.4 opens by claiming "every figure below was
  produced by running the named command, not by inspection". For this figure that sentence was
  false: the figure came from a command run against an earlier state. **This is precisely the
  unsupported-completion-claim class the product exists to detect, committed by the product's
  own construction record** — and it is the one place the record failed to apply the standard
  it applies everywhere else. The general lesson is narrow and reusable: a measured figure is
  invalidated by any subsequent change to what it measures, so the measurement must be the
  *last* action before the claim, not an earlier one.

  Four numbers were corrected, not the three a first reading suggests: the §8.4 heading, the
  "of which N belong to this node" sentence, the `generated/**` bucket, and the ordinal in
  "The Nth path" below the table — that last one follows from the same off-by-one and would
  have left the section self-contradicting against its own bucket total.

  **(2) Terminology: the earlier subagent passes were executor self-checks, not reviews.**
  The user ruled that a subagent dispatched by, prompted by and reported through the execution
  session is **not** independent of the executor: it is an executor self-check, it carries no
  verdict, and it consumes no review budget. Under the append-only rule this log does not
  rewrite earlier entries, so the correction is issued here and the earlier entries are to be
  read through it:
  - the entry describing an "independent test author" (D1) and "the second independent test
    author" (D3) — read as **executor-side test authors**; their reports were self-check
    findings that the execution session reproduced and acted on, never review verdicts;
  - the entry beginning "self-review during implementation" — read as **executor self-check**;
  - a later subagent pass that produced a `CHANGES_REQUIRED`-shaped report on this candidate
    is likewise an **executor self-check**. It is the origin of finding (1) above. It is not
    recorded as a FULL review, did not consume the one permitted review, and no verdict from
    it binds anything.

  Nothing about the defects D1–D3 changes: they were real, they were reproduced independently
  of the report before being accepted, and their fixes stand. Only the standing of the agents
  that surfaced them is corrected.

  **Next step: one independent FULL review** (plan §8), not a targeted VERIFY.
- 2026-07-20 — **the FULL review happened, and this is the one bounded fix that answers it.**
  Budget accounting, which supersedes the preceding entry's "no valid FULL review has occurred"
  (true when written): the user's own review pass **is** the one FULL permitted by plan §8. It
  is independent of the executor by construction — the user is the trust terminal, not a
  subagent the execution session dispatched — and it was a real review pass, driving eight
  mutations through the candidate rather than reading it. It returned findings, which is
  `CHANGES_REQUIRED` in substance. **FULL used (1/1). This fix round used (1/1). One targeted
  VERIFY remains (1/1).** Per V3-D6 every deterministic check was re-run after the fix, which is
  the step that sits between the repair and the VERIFY; the VERIFY itself is a review verdict
  and is not the executor's to issue. The earlier correction at `c5d5535` remains correctly
  classified as a pre-submission correction: at that moment no FULL had occurred, so there was
  no finding for it to answer.

  **The two findings, both fail-open guards.** Both were reproduced against the candidate before
  being acted on. Both are the same defect shape: a guard that does not run, reported as though
  it had passed.
  - **F1 — auditor/executor distinctness was off by default.** `instruction.check_audit` took
    `executor` as an optional argument and only compared identities `if executor`, so the
    ordinary call `check_audit(audit, spec)` returned a clean report even when the audit's
    `audited_by` was the executor. Omitting an argument silently disabled the guard. Fixed by
    reporting the unchecked state instead of skipping it: a missing `executor` now yields
    `V3-AUDIT-AUDITOR-DISTINCTNESS-UNVERIFIED`. The alternative — making `executor` a required
    parameter — was rejected for two reasons: the pinning test shape (call without `executor`,
    assert `not ok`) is only expressible against a *report*, since a required parameter would
    raise `TypeError` instead; and forcing verification is the wrong endpoint (see below).
  - **F2 — cold resume rendered "not verified" as "ok".** `ResumePoint.resolved` collapsed two
    different facts: a pointer whose digest matched, and a pointer that merely existed because
    it carried no digest. Both printed `ok`, so a digest-less pointer whose target had been
    rewritten still read as sound — confirmed by rewriting one and watching `report.ok` stay
    `True`. Fixed inside N1 code only: `ResumePoint` now exposes `verified` and
    `present_unverified` separately, `render()` marks them `ok` and `??`, and a summary line
    states plainly that those bytes were **NOT** verified.

    **The cleaner fix was unavailable and must stay unavailable.** Making `digest_sha256`
    required on `pointerRef` would remove the ambiguity at the source, but that field lives in
    `common.schema.json` — N0-signed bytes, outside the V3-N1 allowlist. Touching it would
    have been an out-of-boundary write dressed up as a better fix.
  - **Both fixes were verified by mutation, not by the tests merely passing.** Each guard was
    neutered in place (`if executor is None:` → `if False:`; `present_unverified[field]` →
    `verified[field]`), the suite was re-run, and each pinning test failed as required — one
    `ERROR`, one `FAIL`. The sources were then restored from byte-checked copies. A test that
    cannot fail does not pin anything.
  - **Two permanent residuals, deliberately not pursued.** Comparing `audited_by` against the
    executor's name proves only that two declared *names* differ; an executor writing
    `audited_by: "Auditor Ada"` still passes. And a pointer that never carried a digest still
    cannot be verified at resume. Neither is a gap to close: Contract §1 already settles the
    first (role separation is a workflow protocol, not an OS guarantee) and the second is a
    consequence of a signed optional field. Trying to mechanize past either would be the
    regression class V3-N0 hit, where a check is stretched beyond what it can honestly
    establish.
  - **The principle these two share, worth keeping.** Neither fix makes anything *verified*;
    both make the *unverified* visible. That is the product's own position — V3-D3 says the
    boundary is an acceptance boundary and not hard enforcement, V3-D5 says a digest is a
    binding and not truth, contract §1 says no semantic truth is proved. It never promises
    guarantee; it promises visibility. The distinction decides what can be closed at all:
    "make X visible" is a boolean a test can assert, so it always closes; "guarantee X holds"
    requires excluding every counterexample, so it usually cannot.
- 2026-07-20 — **user signed V3-N1** (Melclycj). Signed candidate: `802e16a`
  (`V3-N1-REVIEW-FIX1-CANDIDATE-v1`), node base `2b1983f`. The signature is recorded here, in
  this append-only log, and this record carries no approval field of its own — the rule R4
  makes mechanical, applied to the record that discharged R4.

  **The targeted VERIFY was available and was not used (0/1).** Plan §8 permits one; it does
  not require one, and the user signed after the fix instead. Stated plainly because it is the
  one thing a later reader could otherwise get wrong: **the F1/F2 fix was never independently
  verified.** The FULL that preceded it reviewed the candidate at `c5d5535`, before that fix
  existed. Everything supporting the fix — reproduction, pinning tests, mutation checks, the
  green re-run — is executor-side evidence, and by V3-D5 the executor cannot verify its own
  repair. Carried as residual N1-R1 (§10); no record may call that fix verified.

  This signature closes **V3-N1 only**. It does not authorize V3-N2, which needs its own
  explicit user authorization, and it promotes nothing: the candidate stays on
  `document-work-assurance-v3`, unmerged and unpushed.

  Deliberate difference from N0, worth noting because the two look alike: at N0 the user signed
  after a VERIFY returned `PASS` **and** independently reproduced the three checks rather than
  accepting the reported numbers. Here the user signed on the strength of their own FULL, with
  the post-fix state re-run only by the execution session. Both are the trust terminal
  exercising judgment; the evidence behind them is not the same, and this record does not
  present it as if it were.

- 2026-07-20 — **errata: the targeted VERIFY did happen. The entry immediately above is factually
  wrong on this point and is superseded here** (append-only: the earlier entry stands as written,
  read through this one). Issued on user instruction after a pre-clear reconcile caught the
  mismatch.

  **What actually happened.** An independent targeted VERIFY of `802e16a` was performed by the
  review side and returned **`PASS`**. Its scope was V3-D6's: the two accepted findings, the entire
  repair diff, and the permanent boundaries. Specifically —
  - each of the three new guards was **mutation-tested**: neutering the
    `AUDITOR-DISTINCTNESS-UNVERIFIED` report, routing digest-less pointers into `verified`, and
    rendering `??` as `ok` each turned the named pinning test red. The first guard's mutation was
    redone after an initial attempt produced an `AttributeError` rather than a clean failure — a
    crash proves the test *touched* the function, not that it *binds the behaviour* — by restoring
    the pre-fix line exactly;
  - both fixes were probed directly: `check_audit` with no `executor` now reports
    `V3-AUDIT-AUDITOR-DISTINCTNESS-UNVERIFIED` instead of a clean report, and a tampered
    digest-less pointer stays out of `verified` and renders `??`;
  - every deterministic suite was re-run by the reviewer rather than read from this record —
    113 / 29 / 20 / 39 / 41, repo-audit `exit 0`;
  - the repair diff was checked for smuggling (four files; the four `.resolved` → `.verified`
    deletions are a 1:1 rename, and one pre-existing test gained a *stronger* assertion), and the
    permanent boundaries held (zero out-of-boundary paths; plan blob `8ad404b1…` and contract blob
    `b2dbdf75…` unchanged; no N0 artifact touched; A4 not an ancestor; no N2 work present).

  **Why the earlier entry says otherwise:** the VERIFY result had not reached the execution session
  when the closeout was written. Nothing was concealed; the record stated what its author knew.

  **Corrections that follow.** Budget: **VERIFY 1/1 used** — N1's review budget is fully spent, not
  2/3. The claim "the F1/F2 fix was never independently verified" is withdrawn. The N0-vs-N1
  contrast in the earlier entry — "the evidence behind them is not the same" — is also withdrawn:
  both nodes were signed after an independent VERIFY returned `PASS`. Residual N1-R1 is discharged
  (§10) and carries nothing to V3-N2.

## 10. Carried-forward residuals

None is a defect of the handed-forward interfaces; each is a real limitation of this node's
evidence or of what a guard can honestly establish. **A node that closes without discharging
its assigned residual is incomplete, regardless of its own acceptance IDs** — the rule N0 set
for itself applies to whichever node inherits each row below.

Two of the four are marked **permanent**. They are endpoints, not debt: a later node that
"closes" them would be stretching a check past what it can establish, which is the regression
class this project has already hit once. Do not schedule work against them. A third,
**N1-R1, is discharged** — it rested on a factual error, corrected by the §9 errata of
2026-07-20. **One row, N1-R2, actually carries to V3-N2.**

| # | Residual | Owner node | What must actually land |
|---|---|---|---|
| N1-R1 | ~~The F1/F2 fix at `802e16a` was never independently verified.~~ **DISCHARGED — the premise was false.** An independent targeted VERIFY of `802e16a` was performed and returned `PASS`: three new guards mutation-tested, both fixes probed directly, the whole repair diff checked for smuggling, every suite re-run by the reviewer, permanent boundaries confirmed. The row was written before that result reached the execution session; see the §9 errata for the full account. Sharpened rather than deleted, because the register is cumulative and *why* a row died is the auditable part | **none — discharged** | Nothing. V3-N2 must **not** re-verify `instruction.check_audit` or `assurance_state.resume` on the premise that no review covered them — the earlier instruction to do so is withdrawn. Their remaining limits are N1-R3 and N1-R4, both permanent |
| N1-R2 | **Nothing obliges a run to include the R4 governance scan.** It is mechanical and reachable — via `rsc v3 governance-scan` or a `command_exit` request — but N1 has no run orchestration, so an operator who never invokes it gets no signal. R4 only required that the rule be mechanical, which it is | **V3-N2** (`flow.py`) | When the flow controller lands, a governed run must either include the governance scan or record explicitly that it was skipped. A check nobody is obliged to run is a check that will eventually not be run |
| N1-R3 | **`check_audit` cannot prove the auditor and executor were independent contexts** — it compares declared names, so an executor writing `audited_by: "Auditor Ada"` passes | **none — permanent** | Nothing. Contract §1 settles it: role separation is a workflow protocol, not an OS guarantee. The reachable property is already met — an unsupplied executor now reports `V3-AUDIT-AUDITOR-DISTINCTNESS-UNVERIFIED` instead of silence, so the unverified state is visible |
| N1-R4 | **A pointer that carries no digest cannot be verified at resume** — existence is all `resume` can establish for it | **none — permanent** | Nothing. `digest_sha256` is optional on `pointerRef` in `common.schema.json`, which is N0-signed and outside any later node's reach without a versioned successor. The reachable property is already met — `present_unverified` and the `??` marker make the gap visible rather than printing `ok` |

### 10.1 What this node's signature does and does not cover

The signature binds the exact candidate `802e16a` and closes **V3-N1 only**. It does not
authorize V3-N2, does not authorize implementation beyond this node's allowlist, and does not
promote anything: the candidate remains on `document-work-assurance-v3` and nothing was
merged, pushed or made a default. V3-N2 requires its own explicit user authorization, exactly
as N1 did.
