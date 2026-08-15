# W2 record — commit-first ReviewPackage successor: implementation round

**Status: CLOSED — user sign-off 2026-07-24 (§7 final entry), which also signed the carrier.
Candidate authored 2026-07-23; independent FULL returned 0 must-fix / 4 low (all fixed); the
targeted VERIFY and the prose rule-1 read returned `REVIEWED_NO_BLOCKER` / clean with 3
further non-blocking low, all handled in a second user-approved cleanup. Wave-2 implementation
round COMPLETE; the commit-bound successor semantics now govern newly opened runs.** Not a
v3 node (the migration is complete); a successor construction round run under
construction-node discipline by analogy: candidate → independent FULL → optional bounded
fix → targeted VERIFY → user sign. Structure: §§1–6 are rewritable facts until the round
closes; §7 is the append-only log.

## 1. Authorization and governing input

Authorized by the user's explicit go 2026-07-23 (executor session; the §8 point 5 gate of
the adjudicated design). Governing input: [`W2-design.md`](W2-design.md) at `19d1bf7`,
adjudicated `d9c4b1e` — all six §8 points per recommendation. The implementation preview
card (allowlist derived from design §4, four in-round decisions D1–D4 surfaced) was
rendered and user-approved in the same session before any write.

## 2. Change boundary

Declared allowlist for the implementation candidate (derived from design §4):

- `ResearchSystem/contract/Document-Work-Assurance-Contract-v3-supersession-1.md` (new —
  the §3.7 carrier; enters the signed surface at the wave-2 gate, **unsigned until then**)
- `ResearchSystem/schema/document-assurance-v3/review.v2.schema.json` (new)
- `ResearchSystem/tooling/rsclib/document_harness/review_subject.py` and
  `review_result_v2.py` (new sibling modules — decision D1 below)
- `ResearchSystem/tooling/rsclib/document_harness/assurance_state.py` (additive:
  `pointer_to` helper only; existing functions untouched)
- `ResearchSystem/generated/document-assurance/templates/run-v2/` (new — successor run
  template, decision D2)
- `ResearchSystem/tooling/tests/document_harness_review/test_review_v2_subject.py` (new)
- `ResearchSystem/migration/document-work-assurance-v3/W2/W2-record.md` (this record)

**Declared deviation — one path outside the allowlist, and why no in-boundary route
exists.** `ResearchSystem/tooling/tests/document_harness_review/test_fix_round_locks.py`
was edited (**+12/−3** across the round, re-derived at the fix round; the earlier "+9/−3"
was measured after the first of two edits and never re-taken — the "measure last" rule
broken in the record rather than in the code). Its
`EveryNamedCodeIsAssertedSomewhere::test_the_swept_set_and_the_n1_set_partition_the_package`
asserts that **every** module in `rsclib/document_harness/` belongs to either the swept
V3-N2 set or the V3-N1 exclusion list — so adding any module to that package necessarily
fails it. The guard is correct and was left with its teeth: a `SUCCESSOR_ROUND_MODULES`
tuple was added to the partition union, carrying the same reasoning the N1 exclusion
carries (the round that authored the module runs its own reachability sweep — wave 2's is
`NamedIssueReachability` in `test_review_v2_subject.py`, which reads the codes out of the
source and requires each to be asserted by name). The alternatives considered were worse,
not smaller: renaming the module does not help (the guard globs `*.py`), and homing the
module outside the package would break the import surface the design names. The deviation
is surfaced here and to the user rather than absorbed silently (operating contract hard
rule 9).

The prose batch (`ResearchSystem/document-harness/EXECUTION.md` + `REVIEW.md`) is a
**separate commit** — instruction-layer amendment discipline (checkpoint read before use,
W2-A8), never part of this candidate. `.goals/LEDGER.md` is likewise outside the candidate
and rides its own pointer-sync commit (the established wave-2 pattern).

**Signed bytes untouched (W2-A6):** the N0-signed schemas incl. `common.schema.json` and
`review.schema.json`, the v3 contract, and the approved plan appear nowhere in the diff —
`git diff HEAD` over those paths is empty, re-derived at commit time. The v1 → v2
relationship is supersession for newly opened runs only; closed runs and shadow rounds
stay valid against pinned v1 (contract §13).

### In-round decisions (recorded per design §6 "does not decide the module layout")

| # | Decision | Rationale |
|---|---|---|
| D1 | v2 machinery lives in **two** new sibling modules — `review_subject.py` (the subject) and `review_result_v2.py` (the verdict); `review.py` is untouched | `review.py` is at 782 lines; the <800-line rule cannot absorb this layer, and the design names the sibling-module fallback explicitly. v1 stays frozen for pinned history. **The two-module split was itself forced by that same rule and found by the executor after the first candidate commit** — see the correction note below |
| D2 | Successor template home: `ResearchSystem/generated/document-assurance/templates/run-v2/` | Adjacent to the runs root (`…/runs/<run-id>/`) the template instantiates into; surfaced on the preview card, user-approved |
| D3 | `review.v2.schema.json` reuses v1 `$defs` by `$ref` (`reviewRound`, `instructionCompleteness`, `perObligationDisposition`, `finding`, `verifyScope`) | Referencing changes no v1 byte and keeps shared semantics in one home instead of restating them (N0-A6) |
| D4 | The invariant-11 successor check (`check_repair_regeneration_v2`) also lives in `review_subject.py` | v1's `flow.check_repair_regeneration` compares a package digest v2 does not have; leaving the v2 repair path checker-less would reopen the class at the subject layer |

**Pre-submission correction (same day, before review).** The first candidate `19cb882`
shipped the whole layer as one 821-line `review_subject.py` — **over the 800-line hard
rule**, and over it in the very round whose D1 rationale invokes that rule against
`review.py`. Nothing mechanical caught it: `repo-audit.py`'s split tripwire scopes to
Markdown, and PowerShell's `Measure-Object -Line` under-reports (it gave `review.py` 694
against a true 782), so the first count taken was itself wrong. The module was split by
**object** — `review_subject.py` (is this commit a dispatchable, complete, self-consistent
subject?) at 559 lines, `review_result_v2.py` (does this verdict bind that subject?) at
292 — with the result module importing the subject module and never the reverse. All
callers were rewired (the suite, the partition classification, `run_bind_v2.py`), the
reachability sweep now names both modules and asserts it reaches each, and every true
line count was re-derived in Python rather than PowerShell. True counts at correction time:
every module in the package under 800; the largest are `review.py` 782,
`test_review_v2_subject.py` 783 (both pre-existing-or-new but under, and both close enough
to the tripwire to be worth a future round's attention), `flow.py` 709.

## 3. Acceptance matrix

| ID | Property (design §5) | Evidence |
|---|---|---|
| W2-A1 | Successor ReviewResult schema validates subject binding; a package-less/subject-less result and a both-present hybrid are rejected | `SchemaShape` (4 tests): valid v2 accepted; subject-less, package-bound and hybrid all rejected; each of the five subject fields individually required; v1's round conditionals (VERIFY⇒scope, FULL⇒no scope, CHANGES_REQUIRED⇒findings) carried over and asserted |
| W2-A2 | `check_subject` derives the enumeration from the committed tree; a CheckResult file missing from the tree is reported. **(a)** the authored member-**list** collapse is unrepresentable — the object no longer exists (constructive argument, untestable by design); **(b)** the aggregate-**storage** analogue remains representable and, seeded, is reported | (b) `test_missing_per_check_result_file` + `test_aggregate_only_storage_is_reported` + `test_check_result_file_with_foreign_check_id` — the expected set is read from the committed plan's `check_order`; probe 3 (§4) proves the loop is load-bearing. (a) is stated, not tested: no code path constructs a member list |
| W2-A3 | Version keying explicit; no cross-version fallback; present-but-null = SpecGap; v1 surface unchanged | `VersionKeying` (4 tests): absent→v1, `"2"`→v2, `None`/`"1"`/`"3"`/`2`/dict→`SpecGap`; a v1 result handed to the v2 checker raises rather than being re-keyed; a v2 failure reports only `V3-SCHEMA-REVIEW_RESULT_V2` codes. Probe 1 (§4). v1 surface: 334 pre-existing tests pass with zero assertion edits |
| W2-A4 | `pointer_to` writes bytes digests only; the canonical-digest mistake is impossible via the helper; the resume guard still fires on a hand-written wrong pointer | `PointerHelper` (3 tests) — the fixture is deliberately an indent-formatted document whose canonical and bytes digests **differ** (asserted), so the claim is not established from a document where the two coincide; a missing target is an `AssuranceFault` at write time; `resume` still reports `V3-STATE-POINTER-STALE` for a hand-written canonical digest while the `pointer_to` sibling verifies. Probe 4 (§4) |
| W2-A5 | Successor template maps preamble-level run conditions; a template instance omitting them fails its authoring check | `TemplateAuthoringGate` (4 tests) against `templates/run-v2/check_template_instance.py`: an unmapped non-trivial preamble fails, mapping it passes, a version-less spec fails, a trivial preamble (title + blanks only) requires no mapping |
| W2-A6 | S1–S4 re-homed by the successor carrier with exact supersession enumeration; signed v3 contract blob byte-identical | Carrier §2 names all four sites by exact location, quotes each signed text and states each successor text in full; `git diff HEAD` over the contract, `common.schema.json`, `document-work-spec.schema.json`, `review.schema.json` and the approved plan is **empty** (re-derived at commit) |
| W2-A7 | A cold session re-derives the full review subject from the evidence commit SHA alone | `ColdRederivation`: the control root is **deleted from the worktree**, then `read_control_plane`, `check_subject` and `check_review_result_v2` all run clean from the SHA — no worktree state participates |
| W2-A8 | Prose batch additive, few, batched; its checkpoint read occurs before any run relies on it | Process (rule 1) — **not yet discharged**: the batch is a separate commit and its read is owed before any run relies on the amended text. Open at this record's writing |
| W2-A9 | A result naming a different `evidence_commit`, candidate commit, round, `work_id` or `run_id` is rejected; subject fields cross-check against the CandidateRecord read from the evidence commit | `SubjectAgainstCleanPlane` — per-mismatch cases for candidate commit, candidate branch, base revision, repair round, control root, `work_id`, `run_id`, round, and a wrong `evidence_commit` **against a second commit that is otherwise clean**, so only the binding distinguishes them. Probe 5 (§4) |
| W2-A10 | Evidence-commit containment: the changed-path set ⊆ the run's control root; a seeded out-of-root path is reported | `test_evidence_commit_touching_outside_the_control_root` (seeded: the evidence commit also writes `docs/notes.md`) → `V3-SUBJECT-EVIDENCE-OUT-OF-ROOT`; a parentless commit reports `V3-SUBJECT-CONTAINMENT-UNVERIFIED` rather than passing silently. Probe 2 (§4) |

Beyond the matrix: `NamedIssueReachability` pins the layer's whole issue-code surface —
every `f"{CODE}-…"` / `f"{RESULT_CODE}-…"` string in `review_subject.py` **and**
`review_result_v2.py` (38) must be asserted by name somewhere in the suite, so a code
added later without a test fails here rather than becoming silent surface. Two tests keep
the sweep from narrowing silently: one asserts it actually reaches both modules (the F4
defect class, borrowed from the N2 suite), the other asserts it reaches the `check_subject`
identity-table codes specifically.

**That second test exists because the claim above was false when first written** (W2 review
finding 1). The identity table built its codes as `f"{CODE}-{code}"` from a loop variable,
so the sweep read 33 of 38 and silently exempted the five identity codes. They were raised
correctly and each was asserted by hand, so no silent surface existed — but a row added to
that table later would have carried no assertion obligation at all, which is exactly what
the guard is for. Fixed at the fix round by moving the whole code into the literal
(behaviour identical); the sweep now reads 38.

## 4. Executor self-checks (no verdict, no review budget — operating contract)

Seven mutation probes (six at the candidate, one added at the fix round). Each ran its control **before**
mutating (a probe whose control was already red is refused as meaningless), was restored
from a byte-verified scratchpad copy — never `git checkout --` — with restoration asserted
by SHA-256 equality, and ran its control again after. All three touched files were
confirmed byte-identical to their pre-probe state at the end of the batch.

| Probe | Mutation | Result |
|---|---|---|
| 1 | `_ABSENT` sentinel in `result_schema_kind` reverted to plain `.get()`/`is None` — the exact W1-A1 defect class re-introduced | RED: `VersionKeying` (1 failed, 3 passed) |
| 2 | the containment condition in `check_subject` replaced by `if False` | RED: `test_evidence_commit_touching_outside_the_control_root` |
| 3 | the `check_order` derivation loop replaced by an empty iterable | RED: `test_missing_per_check_result_file` |
| 4 | `pointer_to` switched to a canonical digest — the exact w1-r1 pointer-digest-kind mistake | RED: `test_pointer_to_writes_the_bytes_digest_not_the_canonical_one` |
| 5 | the `subject.evidence_commit == evidence_commit` binding replaced by `if False` | RED: `test_result_answering_a_different_evidence_commit_is_refused` |
| 6 | the committed-pointer staleness comparison in `_resolve_pointer` replaced by `elif False` | RED: `test_state_pointer_family` |

**Two defects were found by the executor's own checks and fixed before review.** (a) The
first form of W2-A4's resume test used `{}` as its document, whose canonical and bytes
digests are identical — so it asserted the stale-pointer guard from a case carrying no
mismatch at all; replaced by an indent-formatted document with the inequality asserted.
(b) The 821-line module over the hard rule, described in §2 — found by a true line count
after the first candidate commit, fixed by the object split.

| 7 | the first identity-table row reverted to a non-f-string (the exact pre-fix invisible form) | RED: `NamedIssueReachability` |

Probes 1–6 re-run in full after the F1 fix round (that edit touches `check_subject`, so
probes 2, 3 and 6 anchor in the changed function): every one still red, every restoration
still byte-verified. Probe 7 was added by that round to pin the fix itself — without it, the
new sweep test would assert a property nothing could break.

## Independent FULL review (2026-07-24) and the fix round

<!-- Un-numbered on purpose (VERIFY finding A2): §4 uses lettered items (a)/(b), so a
"§4a" or "§4b" heading collides with §4's own item references — e.g. entry 1's "(§4a)"
means §4 item (a). A heading with no "§4x" token leaves those references unambiguous. -->


**Verdict: no must-fix; the implementation body and all ten acceptance items came back with
zero defects found.** Four low findings, all about the precision of claims in this record
and in the reachability test rather than about behaviour, plus five observations carrying no
fix. The reviewer independently re-ran every suite, re-derived every figure, re-verified the
signed blobs against their pinned hashes, confirmed the carrier's four quotations verbatim
against the signed contract, and ran nine mutation probes of its own construction — all red,
all restored by SHA-256 comparison.

| # | Finding | Fix (user-approved boundary, 2026-07-24) |
|---|---|---|
| 1 | the reachability sweep read 33 of 38 codes: the `check_subject` identity table built its five codes as `f"{CODE}-{code}"` from a loop variable, invisible to any source sweep. No silent surface existed — all five were asserted by hand — but a row added later would have carried no assertion obligation, so this record's and the test's "full surface" claims were wider than the guard | code moved into whole `f"{CODE}-…"` literals (behaviour identical), plus `test_the_sweep_reaches_the_identity_table_codes` pinning the five; §3 rewritten to state what happened |
| 2 | §7's first entry was edited in place inside `eb3d7db`, which hard rule 6 forbids | a new §7 entry naming the earlier one, per the rule's prescribed form; the SHA back-fill is separated out as legitimate. Its first attempt also hand-enumerated the edits — that enumeration was incomplete (VERIFY A1) and, on reflection, unnecessary: the authoritative complete record is the diff `19cb882→eb3d7db`, so it is superseded by a pointer to that diff rather than a longer list (see the later §7 entries) |
| 3 | §5's "zero edits to any pre-existing assertion" was falsified by this round's own declared deviation | §5 qualified with "outside the declared deviation" |
| 4 | two figures wrong: the deviation numstat (+9/−3 vs a true +12/−3, measured after the first of two edits and never re-taken) and §6's test count (37 vs 38) | both corrected; §2 records why the first figure was wrong — the "measure last" rule broken in the record rather than in the code |

The five observations were reproduced and need no fix: the `checks=()` fail-open shape in
`check_repair_regeneration_v2` is verbatim parity with v1's frozen `flow.py` and the repair
path has never run (§6); the malformed-subject schema guard has no direct negative test but
the reviewer probed it by hand and confirmed it has teeth; W2-A8's prose-batch checkpoint
read is honestly open and is the user's gate; `read_control_plane`'s pointer-field list is a
second copy of a signed, frozen schema enumeration so it cannot drift forward; and no
mechanical gate stops premature adoption of v2 semantics while the carrier is unsigned,
which §6 already declares as a ceiling.

Root cause shared with the design round's must-fix 1, worth naming: **an enumerated claim
outrunning the mechanism that backs it.** There it was the design's successor coverage; here
it was a sweep's regex. Both were found by an independent read, neither by a test.

## 5. Measured results (re-derived immediately before the fix commit)

- pytest `tests/`: **373 passed** (334 pre-existing + 39 new W2 tests), zero edits to any
  pre-existing assertion **outside the declared deviation** — the partition assertion in
  `test_fix_round_locks.py` was edited, which §2 declares; the unqualified earlier wording
  was falsified by this round's own deviation (W2 review finding 3)
- compiler golden suite: **29/29** · harness-v2 suite: **39/39** · stage-control matrix:
  **20/20**
- fixture validators: schema **36/36** · harness-v2 **93/93** · stage-control (6 positive /
  15 named-negative / 20 other-negative, 0 failures) · N0 frozen runner **41/41**
- `repo-audit.py`: exit 0 (run again by the pre-commit hook at commit time)
- `git diff HEAD` over every signed path: empty; changed-path set = the §2 allowlist plus
  the one declared deviation

## 6. Honesty ceilings and deliberate non-scope

- **The carrier is unsigned.** `Document-Work-Assurance-Contract-v3-supersession-1.md`
  states four supersessions but carries no signature; until the user signs it at the
  wave-2 gate, the signed v3 statements are what governs. Nothing in this candidate
  changes that, and no run may rely on the successor semantics before the gate.
- **W2-A2(a) is an argument, not a test.** "The authored member-list collapse is
  unrepresentable" is established by the absence of a member-list object, not by a
  negative control — the design's own split (finding 4). Only the aggregate-storage
  analogue is seeded and reported.
- **Parity by re-implementation, not by import.** The result-internal checks shared with
  v1 (obligation coverage, finding coherence, INCOMPLETE disclosure, verify scope,
  reviewer distinctness) are re-implemented in `review_result_v2.py` because v1's live in
  one function that requires a package and is frozen. The duplication is against a frozen
  artifact so it cannot drift forward, but a defect later found in the shared semantics
  must be fixed in both places — stated in the module docstring as well.
- **The line-count rule has no mechanical guard for Python here.** `repo-audit.py`'s split
  tripwire is Markdown-scoped, so the 821-line violation this round shipped and then
  corrected would not have been caught by any check in the repository. Building one is out
  of this round's boundary; it is named here as a witnessed gap rather than silently
  survived. `review.py` (782) and `test_review_v2_subject.py` (783) sit close enough to
  the ceiling that the next round touching either should expect to split it.
- **Digest-strength narrowing** (design §9, carried): v1 package members carried SHA-256
  digests; the successor rests member binding on git content addressing, SHA-1 in this
  repository. Acceptable under contract §1's threat model, a real strength change.
- **The template is not exercised end-to-end.** `check_template_instance.py`'s pure core
  is tested; `run_evidence_v2.py` and `run_bind_v2.py` are compile-checked and read for
  correctness but have **never run a real run** — their first real use is wave 2's first
  real run, and that run is its own observation (the N3-A5 shape).
- **The preamble gate checks facing, not adequacy.** It establishes that some unit anchors
  into a non-trivial preamble; whether the mapping actually captures the preamble's
  normative content stays a FULL-review question. Its trivial/non-trivial split is a
  heuristic (blank lines and a `# ` title), not a semantic judgement.
- **`check_subject` reads the evidence commit against its first parent.** A merge-commit
  evidence commit would compare against one side only; no run has produced one, and the
  parentless case is reported rather than assumed. Not designed for, disclosed.
- The 39 new tests are executor-authored; their independent challenge is this round's
  review, not this record.

## 7. Log (append-only)

- 2026-07-23 — round opened on the user's explicit go (design §8 point 5); preview card
  rendered and approved (allowlist from design §4 + decisions D1–D4); record skeleton
  written; implementation authored: carrier + `review.v2.schema.json` + the v2 module(s) +
  `pointer_to` + `templates/run-v2/` + the acceptance suite. Mutation probes run and
  restored (§4); one authoring-time test defect found by the suite and fixed (§4a); one
  declared deviation outside the allowlist (§2, `test_fix_round_locks.py` partition
  classification). Candidate committed as `V3-W2-COMMIT-FIRST-CANDIDATE-v1` = `19cb882`;
  the instruction-layer prose batch separately as `V3-W2-PROSE-AMENDMENT-v1` = `3b50738`
  (additive 9+/0− and 35+/0−, its rule-1 checkpoint read owed before any run relies on it).
- 2026-07-23 — **pre-submission correction** (executor-found, before any review). A true
  line count showed the shipped `review_subject.py` at 821 lines, over the <800 hard rule
  and in the round whose own D1 rationale invokes it; the first count taken had been wrong
  because PowerShell's `Measure-Object -Line` omits blank lines. Split by object into
  `review_subject.py` (559) + `review_result_v2.py` (292), all callers rewired, the
  reachability sweep extended to both modules with a test that it reaches each, one probe
  added (6 total), every probe re-run red and restored byte-identical, every suite re-run
  green (§5). Committed as `V3-W2-PRE-SUBMISSION-CORRECTION-v1` = `eb3d7db` (SHA back-filled
  at the fix round; a commit cannot contain its own SHA).
  **Awaiting: independent FULL review of the corrected candidate, then the user's
  fix-boundary and sign-off decisions. The review subject is the corrected tip, not
  `19cb882`.**
- 2026-07-24 — **correction to this log, entered by appending as the rule requires.** The
  entry of 2026-07-23 above (the round-opening entry) was **edited in place** inside the
  pre-submission correction commit `eb3d7db`, which hard rule 6 forbids: "the append-only
  log section is append-only; correct by appending an entry that names the earlier one,
  never by rewriting." The edits were `the 37-test acceptance suite` → `the acceptance
  suite`, `Five mutation probes` → `Mutation probes`, `(§4)` → `(§4a)`, and the closing
  "Awaiting …" sentence moved out of that entry into the one following it. Back-filling the
  candidate SHA `= 19cb882` into the same entry was legitimate (a commit cannot contain its
  own SHA, so it can only be recorded afterwards) and is not part of this correction. The
  pre-edit wording is recoverable verbatim from `git show
  19cb882:ResearchSystem/migration/document-work-assurance-v3/W2/W2-record.md`. Reported as
  W2 review finding 2; no entry is edited in place from here on. One honest note on how
  easy the rule is to break: while writing this very correction the executor re-worded the
  *following* entry as well, caught it before committing, and reverted everything except the
  SHA back-fill — which is labelled as such in that entry. The pull toward tidying an
  earlier entry is exactly what the rule exists against.
- 2026-07-24 — **fix round (user-approved boundary, all four review findings).** F1: the
  `check_subject` identity table now carries whole `f"{CODE}-…"` literals so the layer's own
  reachability sweep reaches all 38 codes instead of 33, with a new test pinning the five
  formerly-invisible ones (behaviour identical — no issue text, code or condition changed).
  F2: the correction entry above. F3: §5's "zero edits to any pre-existing assertion" now
  reads "outside the declared deviation", which §2 has always declared. F4: the deviation
  numstat corrected to +12/−3 (re-derived, with the reason the first figure was wrong
  recorded in §2) and §6's test count to 39. Probes re-run after the F1 edit; all suites
  re-derived. Committed as `V3-W2-REVIEW-FIX-v1` (the commit carrying this record — a commit
  cannot contain its own SHA; find it as the branch tip at this title). **Awaiting: the
  targeted VERIFY of this fix, dispatched together with the rule-1 checkpoint read owed on
  the prose batch `3b50738` (user's routing decision, 2026-07-24).**
- 2026-07-24 (later) — **VERIFY returned + a second, user-approved cleanup.** The targeted
  VERIFY of `f751358` returned `REVIEWED_NO_BLOCKER` (all four fixes effective, the whole
  repair diff and the boundaries clean) and the rule-1 read of `3b50738` returned clean;
  both surfaced non-blocking low findings, all handled here inside a user-approved boundary.
  - **A1 — the enumeration is dropped, not completed.** The 2026-07-23 correction entry
    above claimed to quote each edit made to the round-opening entry; the list was incomplete
    (it named four of six edits) *and* unnecessary. The authoritative, complete record of
    what changed in that entry is `git diff 19cb882 eb3d7db`; a hand-list is a second copy of
    that canonical fact (N0-A6), and it drifted — the same defect class this harness exists to
    prevent, appearing a third time (after the design round's must-fix 1 and F1), inside the
    very entry that named it. **Standing rule from here, and the durable lesson of this whole
    round: an append-only correction states the *nature and reason* of an in-place edit and
    *points at the diff* for the exact bytes — it never hand-enumerates the edits as
    authoritative.** The earlier entry stands unedited (append-only); this entry supersedes
    its enumeration claim, and the enumeration in it is to be read as illustrative, never
    complete.
  - **A2 — the `## 4a.` heading collided with entry 1's `(§4a)` item reference** (which means
    §4 item (a)). Renamed to an un-numbered heading; `## 4b` was rejected because §4 uses
    lettered items and `4b` would collide with §4 item (b). One consequential edit outside the
    record: `W2-dispatch-verify-and-read.md`'s single `§4a` reference was updated to name the
    section, since the completed handoff should not point at a renamed heading.
  - **B1 — the successor section of `REVIEW.md` had dropped the "in full" qualifier** the v1
    custody-chain bullet carries; restored as a two-word instruction-layer amendment,
    committed separately as `V3-W2-PROSE-INFULL-AMENDMENT-v1` = `6f7b2dc`, which owes its own
    rule-1 checkpoint read before any run relies on it (rides the next dispatch; nothing
    relies on it yet — carrier unsigned).
  This cleanup touches only prose — the record, the completed dispatch, and `REVIEW.md` — so
  no code, schema, test, fixture or golden changed and the suites and mutation probes are
  unaffected since `f751358`; pytest was re-run once to confirm no regression (**373**), and
  `repo-audit.py` runs at each commit via the pre-commit hook (exit 0). This record + the A2
  dispatch edit committed as `V3-W2-REVIEW-FIX-v2` = `8a165bc`.
- 2026-07-24 — **ROUND CLOSED: user sign-off (Melclycj, in session: "签字"), which also signs
  the carrier.** The signature covers the wave-2 implementation round at its reviewed-and-
  cleaned state and signs `Document-Work-Assurance-Contract-v3-supersession-1.md`. Recorded
  here, never in the carrier's bytes, exactly as the carrier's own §5 prescribes:
  - **Signed carrier blob** (git object) `68031fa2ca31272e31da0d42a9a02189d28fcc21`,
    **byte-identical since the candidate `19cb882`** — `git log 19cb882..HEAD -- <carrier>` is
    empty, so the object the FULL and VERIFY reviewed and the object signed are the same bytes;
    sha256 of those bytes
    `c3925b5a01362f032030ec70d227c2b66b26b6846470476b7375ce919d9d31ed`.
  - **Signed at** the round's reviewed+cleaned tip `6b43057`; the sign-off commit carrying
    this line is its child.
  - The carrier's own header still reads "UNSIGNED until the wave-2 gate": that line is now an
    **authoring residue**, superseded by this signature record and deliberately left unedited
    so the signed blob stays byte-identical to the reviewed one (the N0 §8 precedent for a
    frontmatter-status residue). The authoritative signature is this entry.
  - **Effect:** the four supersessions S1–S4 and the §3 version boundary of the carrier now
    govern; from here the commit-bound successor semantics apply to newly opened runs, and the
    package-bound form is pre-wave-2 history.
  - **Carried debt, not blocking:** the B1 prose amendment `6f7b2dc` still owes its rule-1
    checkpoint read before any run relies on it (rides the next dispatch; nothing relies on it
    yet). Wave 2's first real run is the next witnessed-case source; the I/O-boundary design
    round stays parked until after it.
  **WAVE-2 IMPLEMENTATION ROUND COMPLETE.** Full chain: `19cb882` candidate →
  `3b50738` prose → `eb3d7db` pre-submission correction → independent FULL (0 must-fix, 4 low)
  → `f751358` fix → targeted VERIFY (`REVIEWED_NO_BLOCKER`) + prose read (clean) → `6f7b2dc`
  (B1) + `8a165bc` (A1/A2) → this sign-off.
- 2026-07-25 — **B1 rule-1 checkpoint read DISCHARGED** (independent reviewer, user-routed;
  subject `6f7b2dc`, dispatch `W2-dispatch-b1-checkpoint-read.md`). Verdict **clean, no fix
  owed** — every claim re-derived from committed bytes: the amendment is purely the two-word
  "(in full)" insertion (numstat 2/2, the second changed line a wrap of the same sentence,
  zero deletions), it restores the escrow requirement the v1 custody bullet (REVIEW.md line 68)
  carries — the qualifier placed on the chain itself, the successor section's only available
  anchor, semantically equal (dispatch the full SHA) — contradicts nothing it does not amend,
  raises no new promise (the section's "the commit pins bytes, never honesty" ceiling
  untouched), and REVIEW.md is byte-identical from `6f7b2dc` to the tip (no later commit
  touched it). Three residuals, all pre-known instruction-layer ceilings and none a fix:
  "(in full)" is a prose-only constraint with no mechanical gate (the *same* ceiling as the v1
  bullet it mirrors — consistent, not a regression); the read covered only `6f7b2dc`; the
  amendment's provenance lives only in its commit message (the corrective-batch precedent).
  **The B1 amendment may now be relied upon.** This was the wave-2 programme's one carried
  debt — it is now cleared, and **nothing in the wave-1 + wave-2 special-case-bucket programme
  remains open.**
