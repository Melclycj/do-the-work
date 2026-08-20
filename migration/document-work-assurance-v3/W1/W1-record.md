# W1 record — special-case bucket wave 1: the review_only successor fields

**Status: CLOSED — user sign-off 2026-07-22 (§7 final entry).** Not a v3 node (the migration is complete); a successor construction
round run under construction-node discipline by analogy: candidate → independent review →
user decision. Structure: §§1–6 are rewritable facts until the round closes; §7 is the
append-only log.

## 1. Authorization and adjudicated parameters

Authorized by the user's six-point adjudication of the reviewed design
([`../v3-special-case-bucket-design.md`](../v3-special-case-bucket-design.md) §9, revision
`9405bed`), all recommendations adopted verbatim ("都以推荐为准"):

| # | Adjudication | Ruling |
|---|---|---|
| 1 | (b) scope | **narrow** — `review_only` only; witness-first (upgrade to universal only if a real run witnesses the trivial-check dressing) |
| 2 | field names | `review_only_rationale` + **`not_supported_when`** (reviewer-preferred over `not_supported_condition`) |
| 3 | wave packaging | two waves; the `REVIEW.md` hunt item **included** in wave 1's prose batch |
| 4 | wave-1 authorization | **granted in the same adjudication** (design checkpoint read had occurred) |
| 5 | (c) timing | parked until after wave 1's first real run |
| 6 | v2 version discriminator | **root `schema_version` const** — the instance names its own schema; explicit keying, no cross-version fallback |

## 2. Change boundary

Declared allowlist for the implementation candidate:

- `ResearchSystem/schema/document-assurance-v3/document-work-spec.v2.schema.json` (new)
- `ResearchSystem/tooling/rsclib/document_harness/{__init__,spec,views}.py`
- `ResearchSystem/tooling/tests/document_harness/test_workspec_v2.py` (new)
- `ResearchSystem/generated/document-assurance/test/coverage-view.golden.txt` (deliberate regen)
- `ResearchSystem/migration/document-work-assurance-v3/W1/W1-record.md` (this record)

Actual changed set = exactly those paths (`git status` re-derived before commit; the
untracked `ResearchSystem/docs/` predates this round and is user-ruled ignored). The prose
batch (`document-harness/EXECUTION.md` + `REVIEW.md`) is a **separate commit** — it is an
instruction-layer amendment and follows that discipline (checkpoint read before use), not
this candidate's.

**Signed bytes untouched (W1-A7):** the N0-signed v1 schema, `common.schema.json`, the
contract and the plan appear nowhere in the diff. The v1 → v2 relationship is supersession
for newly authored WorkSpecs only; existing records stay valid against pinned v1
(contract §13).

## 3. Acceptance matrix

| ID | Property | Evidence |
|---|---|---|
| W1-A1 | A `review_only` obligation missing `review_only_rationale`, `not_supported_when`, or both is rejected; both present (≥ minLength 8) is accepted; empty/short values rejected | `ReviewOnlyFields` (4 tests) |
| W1-A2 | Deterministic modes forbid both new fields — full mode × field cross-product rejected, with a passing negative control proving the fields cause the failures | `DeterministicModesForbidTheFields` (2 tests, 4 subtests + 2 controls) |
| W1-A3 | v2 root requires `schema_version` const `"2"`; keying is explicit — absent → v1, `"2"` → v2, anything else present (incl. `"1"`, `"3"`, non-strings, **and explicit `null`** — review finding A1: a present key is a declaration whatever its value) → `SpecGap`, fail closed | `VersionKeying` (4 tests, incl. the `None` case) + `ReviewOnlyFields.test_v2_requires_its_version_const` |
| W1-A4 | **No cross-version fallback, both directions:** a declared-v2 document failing v2 reports `V3-SCHEMA-SPEC_V2` issues and is never re-tried on v1; a version-less document carrying v2 fields lands on v1 and is rejected by its closed root | `test_v2_failure_is_reported_against_v2_never_retried_on_v1`, `test_v1_never_accepts_v2_fields`; mutation probe 1 (§4) |
| W1-A5 | v1 surface unchanged: all pre-existing tests pass with zero assertion edits; the frozen N0 fixture runner is unaffected (41/41 — it names its files explicitly); the v1 cross-document spine rules govern v2 unchanged | suite counts in §5; `SpineRulesApplyToV2` (2 tests) |
| W1-A6 | The coverage view opens with the mode-ratio line (`N of M obligations review_only · K bind checks`), counts are correct, the line carries no verdict/threshold vocabulary, and the golden pins it | `ModeSummaryLine` (4 tests) + regenerated golden (diff = exactly the one added line; the coverage-document JSON golden is byte-unchanged) |
| W1-A7 | No signed byte changed; changed-path set ⊆ the declared allowlist | §2; `git diff --numstat` re-derived at commit |

The schema-directory hygiene scan (`test_r3_every_v3_schema_present_is_clean...`) covers the
new v2 file automatically (the `8efe3e9` subset assertion held — adding the file tripped
nothing) and confirms it declares no forbidden surface vocabulary.

## 4. Executor self-checks (no verdict, no review budget — operating contract)

Three mutation probes, each restored from a byte-verified scratchpad copy (never
`git checkout --`), each with the unmutated control green before and after:

| Probe | Mutation | Result |
|---|---|---|
| 1 | `spec_schema_kind` unknown-version stop replaced by a silent `return "spec"` fallback — the exact fail-open shape the design bans | RED: `test_unknown_versions_stop` + `test_check_spec_stops_on_unknown_version` (2 failed, 16 passed) |
| 2 | v2 schema's review_only required pair neutered to `review_only_rationale` alone | RED: `test_review_only_missing_either_or_both_fields_is_rejected` (its `missing not_supported_when` subtest) |
| 3 | mode-ratio line removed from `render_coverage` | RED twice over: `test_render_coverage_opens_with_the_line` + the golden pin |

Every "must fire" guard fired; every restoration verified by SHA-256 equality against the
pre-mutation copy.

Fix-round probe (2026-07-22, after the independent review's A1 fix):

| Probe | Mutation | Result |
|---|---|---|
| 4 | the `_ABSENT` sentinel reverted to plain `.get()` — the exact A1 defect re-introduced | RED: `test_unknown_versions_stop`'s `None` subtest |

## 5. Measured results (re-derived immediately before the candidate commit)

- pytest `tests/`: **334 passed** (316 pre-existing + 18 new W1 tests), zero edits to any
  pre-existing assertion
- compiler golden suite: **29/29** · harness-v2 suite: **39/39** · stage-control matrix:
  **20/20**
- fixture validators: schema **36/36** · harness-v2 **93/93** · N0 frozen runner **41/41**
- `repo-audit.py`: exit 0 (run again by the pre-commit hook at commit time)
- golden regen diff: `coverage-view.golden.txt` +1 line, `coverage-document.golden.json`
  byte-unchanged

## 6. Honesty ceilings and deliberate non-scope

- **Presence, not truth.** The two fields are presence-checks; a hollow sentence passes the
  schema and is challengeable only at review. This is the design's stated boundary
  (visibility, never guarantee) — no new promise exists.
- **The START surface has no single code owner in `rsclib`.** The shadow runs assembled it
  in dispatch scripts; those rounds are frozen (V3-D9). Wave 1 therefore lands the ratio on
  the coverage view (golden-pinned) and exports `mode_summary_line` for any future START
  assembler. Wiring it into a live START surface is observable only at the next real run.
- **`pack_digests()` output changes** — the schema-pack digest now covers ten files. It is a
  generated binding, not signed material; no test pins its value (verified by grep + green
  suites). Runs that recorded the nine-file digest recorded the pack that validated them;
  nothing rebinds them.
- **The new incentive edge stands as designed:** an author can dodge both sentences by
  declaring `local_check_and_review` with a trivial check. Counterweights are the ratio
  line and the review-side hunt item; if witnessed, it is the next design input
  (witness-first, adjudication point 1).
- The 18 new tests are executor-authored; their independent challenge is this round's
  review, not this record.
- **Known-stale comment left in place (review finding A3):**
  `rsclib/document_harness/review.py`'s V3-N2 registry comment still says `validate()` "can
  only reach the nine schemas" (now ten) and that `__init__.py` "was frozen when V3-N1
  closed and no later node may write it" — this round, which is a successor round and not a
  node, wrote exactly that registry under its own user-adjudicated allowlist. The path is
  outside this round's boundary, so the comment is recorded here rather than edited; it
  belongs to whichever round next owns that file. *(Discharged 2026-07-22: the comment was
  refreshed in the user-authorized residual-hygiene batch — see §7.)*

## 7. Log (append-only)

- 2026-07-22 — round opened on the user's six-point adjudication (all recommendations
  adopted); implementation authored; three mutation probes run and restored (§4); all
  suites re-derived green (§5); candidate committed as
  `V3-W1-REVIEW-ONLY-FIELDS-CANDIDATE-v1` (the commit carrying this record — a commit
  cannot contain its own SHA; find it as the branch tip at this title). Prose batch
  committed separately as an instruction-layer amendment awaiting its checkpoint read.
  **Awaiting: independent review of the candidate + user sign-off, both user-routed at
  catch-up.**
- 2026-07-22 — **independent review returned (dual-subject round: candidate `cabf539` +
  prose `041cc1b`).** Reviewer independently re-ran every suite, re-classified every path,
  re-verified signed blobs, and re-did 8 mutations (the record's 3 + 5 of its own) — all
  RED as required. Findings: **A1** explicit `schema_version: null` silently keyed to v1,
  contradicting this record's W1-A3 statement (net behaviour still fail-closed via v1's
  closed root, but the acceptance statement was false and untested); **A2** the
  `ModeSummaryLine` fixture was symmetric — two semantic mutants (count inversion;
  checks-vs-rows) survived the unit tests and were held only by the golden; **A3** the
  `review.py` stale-comment item now in §6; **B1** the prose taught the banned
  fold-to-`SUPPORTED` (honest disposition: `UNVERIFIABLE`); **B2** "dressing is visible in
  the ratio line" over-claimed (dressing moves the obligation *out* of that count); **B3**
  stage-marker provenance; **B4** missing "or the contract". User approved the fix
  boundary (A1 as code fix — a present key is a declaration). Fixed:
  `V3-W1-REVIEW-ONLY-FIELDS-FIX-v1` (A1 sentinel + `None` test + probe 4; A2 asymmetric
  fixture; this record's §3/§4/§6 updates) and `V3-W1-PROSE-AMENDMENT-FIX-v1` (B1–B4).
  **Awaiting: targeted VERIFY (same reviewer) + user sign-off.**
- 2026-07-22 — **targeted VERIFY of `8e681f8` + `7640709` returned clean** (same reviewer;
  for `7640709` the VERIFY doubled as its rule-1 checkpoint read). All seven fixes verified
  landed as prescribed: the reviewer executed the three keying paths directly (absent → v1,
  `"2"` → v2, explicit null → `SpecGap`, message now fully accurate), re-did probe 4 itself
  in an isolated copy (exactly the `None` subtest red, restore byte-compared), re-ran its
  two A2 semantic mutants (both now killed at unit level — the golden is no longer the sole
  net), matched §6's quotations verbatim against `review.py`, and confirmed B1's
  disposition semantics and B2's "if at all" honestly carry the signed F4 risk. No new
  defect; both numstats re-derived with zero out-of-site changes (record edits enumerated
  as round sync); signed blobs byte-identical across `417b55a`↔`7640709`; the 316
  pre-existing tests untouched; full suites re-run green post-fix; mutations isolated from
  the worktree. **Awaiting: user sign-off — the round's final gate.**
- 2026-07-22 — **residual-hygiene batch (user-authorized at catch-up):** the §6
  known-stale `review.py` registry comment refreshed in place (ten schemas; the frozen-
  `__init__` claim now names the W1 successor-round write and points at this record §6) —
  comment-only, no behaviour, all suites re-run green; and the `EXECUTION.md` header
  broadened to name the WorkSpec-author section (the B3 remainder the reviewer routed to a
  future batch) — that edit is instruction-layer and awaits its rule-1 checkpoint read in
  its own commit. Two commits, one concern each.
- 2026-07-22 — **hygiene-batch checkpoint read returned: one low non-blocking finding.**
  `e9e06c1` clean (additive re-derived, the named section and its stage marker match the
  header's claim, B3 fully discharged — no remainder); `50d5480` accurate (schema count
  re-derived at ten, N2 reasoning preserved); batch boundary exact, signed blobs
  byte-identical, all suites green at the batch tip. The finding: the refreshed comment's
  bare "ten" repeats the same count-decay shape that made "nine" stale. Fixed same day per
  the reviewer's prescription — pinned as a dated statement ("ten as of W1, 2026-07-22");
  comment-only, not instruction-layer, no further read owed.
- 2026-07-22 — **ROUND CLOSED: user sign-off** (Melclycj, in session: "wave 1 i sign
  off"). The sign-off covers the wave-1 chain: candidate `cabf539` + prose amendment
  `041cc1b` + fix round `8e681f8`/`7640709`, independently reviewed (7 findings, all
  fixed) and target-VERIFIED clean (empty findings list; the VERIFY doubled as the prose
  fix's rule-1 read). The residual-hygiene batch (`50d5480`/`e9e06c1`/`2c8f8bd`) closed
  separately the same day under its own checkpoint read. Next per the standing
  adjudication: wave 1's first real run is the next witnessed-case source; wave 2 stays
  parked until after it. Open at close: the v2-mandate go/no-go (recommended to land
  before the first real run); the "node boundary" referent ruling due at wave-2 opening.
