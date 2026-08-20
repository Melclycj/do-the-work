# Phase C0 (M8 + M10) — targeted VERIFY of `a918e37..fbe0b63`

Review-side output for the Phase C0 repair round. Authored by the independent bounded reviewer
under [`../../document-harness/CONSTRUCTION-CHECKLIST.md`](../../document-harness/CONSTRUCTION-CHECKLIST.md)
(R1–R9), which supersedes [`v3-harness-review-contract.md`](v3-harness-review-contract.md) —
that file is a stub pointing at the checklist, and the dispatch prompt's reference to it
resolves there. Not a node artifact, binds nothing. Written in-worktree, untracked; committing
it is the execution side's act (R6).

- **Round:** the round's **targeted VERIFY**. Derived, not accepted: the range contains
  `bff5f39`, a committed review record whose subject is `a918e37..7572abd` and whose verdict is
  `CHANGES_REQUIRED`, and `fbe0b63`, which names its own kind as the round's one review fix.
  Under E9's discriminator — *has a valid independent FULL already occurred?* — the answer is
  yes, so `fbe0b63` is the fix round and it obliges this VERIFY. **Budget after this record:
  exhausted.** One FULL, one fix, one VERIFY, all spent.
- **Verdict:** `REVIEWED_NO_BLOCKER`. Both accepted blockers are closed, and closed by the
  minimum fix the FULL specified rather than by something adjacent to it. Every guard the
  repair created or moved binds under my own probes, with value-level failures and zero errors.
- **Findings:** 2 low, 3 observations. None is a blocker; none would have justified a round.
- **Scope (R3):** the accepted findings, the **entire** repair diff, and the permanent
  boundaries. Not a re-certification of the round (R4) — the FULL's verdict on M8/M10 stands on
  its own record, and I re-derived only what the repair could have disturbed.

---

## 1. Subject re-derivation (R2 — every figure below is mine, none accepted)

| Check | Result |
|---|---|
| range resolves | `a918e37a876d41909330f32f7a22b14d52f6f7b1..fbe0b631950d60bebd7598a447333a2e16682d9d` |
| linear, no merges | `git log --merges` over the range: empty; `git rev-list --count` = **7** |
| HEAD == tip | `fbe0b631950d60bebd7598a447333a2e16682d9d`, branch `document-work-assurance-v3` |
| worktree carries no smuggled change | `git status --porcelain` → one line, `?? ResearchSystem/docs/`; `git diff --stat HEAD` empty. That directory holds exactly one file, `General-Harness-v2-Design.md`, which the ledger already records as parked pending a disposition ruling. Nothing in this round depends on it |
| not pushed | no `origin/document-work-assurance-v3` |
| changed paths, classified by hand | **8** — the FULL's 7, plus `A ResearchSystem/migration/document-work-assurance-v3/v3-review-full-7572abd.md` (the review record, committed by the execution side per R6). Repair-diff subset: 6 paths, all already inside the round's boundary |
| dispatch reproduces | `rsc.py v3 dispatch --range a918e37..HEAD` → `derived round : a918e37…..fbe0b63…`, exit 0, and the emitted prompt is byte-for-byte the one I was handed (E12) |

**Permanent boundaries — intact (E2).** `git diff a918e37 fbe0b63` restricted to
`ResearchSystem/schema/` and `ResearchSystem/contract/` is empty. The three signed blobs
`8ad404b1` / `b2dbdf75` / `68031fa2` each still `git cat-file -t` → `blob`. The N0 schema
directory holds 14 files and `contract/` holds 11, unchanged. Both user-locked oracles hash
identically at HEAD and in the worktree — `expected-construction-prompt.txt`
`5cf970c17ad509e7517f59fb9421a2de4cb9bd68`, `test_readme_enumeration.py`
`57cecbb0c467485b692308ebb13cc64dfeb630b7`. `ResearchSystem/document-harness/` and the rest of
`ResearchSystem/migration/` are untouched by the repair, so the instruction layer carries no
bytes from it.

**Baselines, re-run immediately before this record (E3).** From the restored worktree:

| suite | result |
|---|---|
| `document_harness` | Ran 137, OK |
| `document_harness_review` | Ran 321, OK |
| `harness` | Ran 39, OK |
| `stage_control` | 20 run, 0 failures, 0 errors |
| P2 golden | tests: 29, passed 29 |
| repo audit | `RESULT: clean (exit 0)` |

The review side's 314 → 321 is derivable rather than accepted: the repair adds three test
methods to `test_review_cli_v2_subject.py` (L4 print, L2 refusal, the `--record`-only case) and
four to `test_run_v2_template_fulfillment.py` (`TheRunIsRefusedNotMerelyReported`), and
`git diff --name-status` shows no other test file changed. 314 + 7 = 321.

**Authorization — as far as the repository carries it (R7).** The C0 plan's Step 7, committed in
`fbe0b63`, records the fix as *"`E9` 的那一次 user-approved fix，用户 2026-07-28 批「show me the
findings first, then fix」"*, and the ledger's `▶ 当前指针` independently records that the round's
budget is now down to the VERIFY alone. Ceiling: I hold no session message. Committed bytes in
the two files the checklist designates for rulings is more than a hint and less than proof of
what was said. The approval as recorded does not enumerate finding IDs, so the boundary of what
"the fix" covered is derived from the FULL's own tiering (F1/F2 must-fix; L1/L2/L4 explicitly
*"would ride an approved repair, never justify one"*), and the repair commit states its riders
rather than landing them silently, which is what E9 asks for.

---

## 2. Are the accepted findings closed? (R3 — leads; R8 — every row is a probe I ran)

Restore discipline: both mutated files were copied to a scratchpad **before** the first probe and
restored from those copies after each, never `git checkout --`. Pre-probe and post-probe sha256
are identical byte for byte — `rsc.py`
`167772b0ca834bd9469b7c39ded509d001212467ee2967cb2826550ea4025597`, `run_evidence_v2.py`
`607210bfe7ab536e1364d57c11278b479e3482290a9305a00e4c7156e1c80df3` — and `git status --porcelain`
is back to the single untracked line.

### F1 — closed

The FULL's minimum fix was: point the test at a package that exists and parses, and assert the
whole emitted line. Both were done, and a second case omitting only `--record` was added for the
class rather than the instance (E7).

Probe: `missing = [name for name in ("spec", "record") if not getattr(args, name)]` → `missing = []`.
**Binds** — 2 failures, both value-level, in exactly the shape F1 named: with the guard neutered
the command reaches `load_spec(None)` and raises
`TypeError: argument should be a str or an os.PathLike object … not 'NoneType'` at `spec.py:67`,
and in the one-supplied case it reaches `load_package(args.record)` and raises the same at
`__init__.py:179`. The traceback the assertion was written to catch is now actually produced,
which it never was against the nonexistent-path fixture.

E5 holds on the replacement: `"FATAL: --package mode requires --spec and --record"` and
`"FATAL: --package mode requires --record"` are hand-written literals, each the whole emitted
line, and neither is a prefix of the other, so the one-missing case cannot be satisfied by the
both-missing message.

### F2 — closed

The FULL's minimum fix was: one test that calls `main()` against a temp run directory, asserting
`main() == 1` *and* that the evidence dir is empty; plus, as the cheaper-than-arguing rider,
moving `EVIDENCE.mkdir` below the refusal. All of it was done, as four tests.

| # | guard | probe (real defect shape) | outcome |
|---|---|---|---|
| G2 | `main()` refuses when `unfilled` | deleted the four-line `if unfilled: … return 1` | **binds** — 3 failures, all value-level (`AssertionError: None != 1`), zero errors |
| G2-over | the same guard must not over-fire | `if unfilled:` → `if True:` | **binds** — the declared negative control `test_a_complete_map_does_not_trip_the_refusal` fails, `AssertionError: 1 is not None` |
| G2b | `EVIDENCE.mkdir` follows the refusal | moved the mkdir back above the refusal (the pre-repair order) | **binds** — exactly 1 failure, `AssertionError: True is not false : the refused run created …\evidence` |
| G6 | `--check-result` is refused in subject mode | deleted the refusal (the pre-repair silent-drop) | **binds** — 1 failure, and the CLI prints `result checked : none supplied` / `RESULT: sound subject (exit 0)`, which is the silent-drop shape L2 named |
| G7 | the subject prints in full | restored `[:12]` | **binds** — 1 failure, `'evidence commit : e4aa42f3…94fa2' not found in '… evidence commit : e4aa42f3459f …'` |

The executor's self-report that its own probes produced value-level failures and zero errors is
reproduced here on the five guards the repair created or moved; I did not re-probe G1, G3 and G4,
which the repair did not touch and the FULL already found binding.

The `run_main` helper that converts a run-past-the-guard crash into `None` is the right shape and
I verified it does that rather than swallowing a real refusal: under G2 the failure message
carries the captured stdout (`deterministic checks : 0/0 PASS`), so the reason the code is `None`
is visible in the failure, not hidden by the `except`.

E5 holds: `OBLIGATIONS`, `LOCATOR_ONE`, the work-spec and resolved-plan fixtures are hand-written
in the test module and never read from the template; the STOP lines are asserted as whole
hand-written literals.

### The riders — L1, L2, L4 closed; L3 correctly not

L1: `HARNESS-LEDGER.md:29` now reads `rsc v3 dispatch --range a918e37..HEAD`, and the parenthetical
states the derivation-not-result reason. The dispatch I reproduced from that line is the prompt I
was handed, so the ledger no longer sends a cold session to a short range. L2 and L4 are the G6 and
G7 rows above. L3 is not fixed and the commit says why — `3e27b5f` does not name its kind from
E8's set, E8 forbids amending, and `fbe0b63` names its own kind instead. That is the only honest
move available; I confirmed the other five commits in the range each name a kind.

**E6, both sides.** No finding here was answered by adding a rule about the named thing: F1's fix
is the test changing, F2's is the missing test existing and the mkdir moving, L1/L2/L4 are the
named lines changing. Nothing in the repair diff triggers E6's refusal clause.

---

## 3. Low (non-blocking; there is no repair left for them, and neither warrants one)

- **V1 — `test_nothing_is_written_before_the_refusal` passes for two different reasons, one of
  them a defect.** It asserts `EVIDENCE.exists()` is false after a refused run. That is satisfied
  by the fixed ordering *and* by `EVIDENCE.mkdir` not existing at all. Probed: deleting
  `EVIDENCE.mkdir(parents=True, exist_ok=True)` outright leaves the whole `document_harness_review`
  suite at **321 tests, OK**. E4 asks that every must-fire test be paired with a negative control,
  and the G2b must-fire direction has none — nothing anywhere asserts the directory *is* created on
  the path that proceeds. Not inflated to a blocker for three reasons: the accepted F2 fix meets the
  FULL's stated minimum fix exactly; the uncontrolled line is pre-existing, relocated rather than
  introduced by this round, so nothing regressed; and its absence is not silent — line 189
  (`(EVIDENCE / "check-results.json").write_text(…)`) raises `FileNotFoundError` on the first real
  run. Cheapest close, if it is ever wanted: one assertion in
  `test_a_complete_map_does_not_trip_the_refusal` that `EVIDENCE.exists()` is true.
- **V2 — the plan's Acceptance still carries the pre-repair measurement.** The repair rewrote the
  plan's status line and Steps 6–8, where Step 7 records `137 / 321 / 39 / 20 / 29`; the Acceptance
  bullet ten lines below still reads *"五 suite：137 / **314**（+19）/ 39 / 20 / 29 = **539**"*. Two
  figures for the same measurement in one file, and the checkbox is ticked against the stale one
  (E3: a figure is invalidated by any later change to what it measures). Low rather than blocking
  because the accurate value sits in adjacent text in the same file and no decision turns on which
  is read — but it is a *number*, so R9's wording-level exemption does not reach it, and it should
  be corrected rather than banked.

## 4. Observations (no action implied; R5 — what should exist is not mine to conclude)

- **O1 — the L4 comment claims slightly more than the code delivers.** `print(f"evidence commit :
  {evidence_commit or args.subject}")` prints in full only when `resolve_subject` resolved; on the
  fallback it prints whatever the caller typed, which may be abbreviated. The comment above it says
  "Printed in full, never abbreviated". Exposure is small — the fallback only happens on a run that
  is already reporting issues and exiting 1 — and the test correctly pins the resolved case.
- **O2 — the defect class for the v1 refusal is half-covered.** The added case omits only
  `--record`. The mirror instance — `--record` supplied, `--spec` omitted — is not exercised, so the
  message-building `" and ".join(...)` is proven on two of its three reachable outputs.
- **O3 — the new temp directories are never cleaned up.** `readable_package()` and
  `TheRunIsRefusedNotMerelyReported.setUp` each `mkdtemp` with no `tearDown`; a full review-suite
  run leaves roughly seven directories in the system temp area. Harmless, and noted only because
  the suite is run often.
- **O4 — where this round's defects landed, restated once.** The FULL's O3 reported that the
  capability landed and the postcondition policing it was what failed review. The repair fixed the
  postconditions and the one low finding it could not fix is again in the same layer (V1, a missing
  negative control). I report the shape; whether it warrants anything is yours.

---

## 5. Process and record conformance (R3 — boundary check, run second)

| Rule | State |
|---|---|
| E2 frozen bytes | intact — §1 |
| E3 measure last | the repair's own figures match mine on every item I could re-run: 137 / 321 / 39 / 20 / 29, repo-audit exit 0, both scratchpad sha256 values, both oracle blob hashes, 14 + 11 frozen files. One stale figure left behind in the plan — V2 |
| E4 / E5 guard discipline | the two violations the FULL found are repaired and re-probed here. One uncontrolled direction remains — V1 |
| E6 no new machinery | respected, both halves; §2 |
| E7 defect class not instance | met on F1 (a second omission case added) and F2 (the property tested is "an unanswered obligation refuses the run", not the one reported line). Half-covered on one axis — O2 |
| E8 git | explicit-path staging: consistent with the diff, not directly observable — **marked**. No amend, no push. In-boundary: the repair's 6 paths are all inside the round's existing footprint, so the repair boundary narrowed rather than widened. Title `V3-PHASE-C0-REVIEW-FIX-v1`, one dense paragraph, no trailers, kind named |
| E9 budget | FULL (`bff5f39`) + one fix (`fbe0b63`) + this VERIFY = the cap exactly. The four pre-FULL commits classify themselves as plan / candidate / pointer / pre-submission correction and consume nothing; the record commit `bff5f39` is R6 channel work and consumes nothing |
| E10 instruction layer | untouched by the repair. The amendment read was waived by the user; the waiver is recorded in both the ledger and the plan and labelled an explicit override rather than a rule exit, which is the honest form |
| E11 preview card | not recorded for the repair round. Chat-only — **UNVERIFIABLE** (R4) |
| E12 handoff | one range, no per-acceptance argument. Confirmed by reproducing the dispatch byte-for-byte |

---

## 6. Disclosure of what I read (R4)

- **In full:** `CONSTRUCTION-CHECKLIST.md`, `README.md`, `EXECUTION.md`, `REVIEW.md` and the review
  contract stub (the round's opening cold read of the instruction layer); `v3-review-full-7572abd.md`;
  `HARNESS-LEDGER.md`; the C0 plan; all seven commit messages; the whole repair diff, every hunk;
  `run_evidence_v2.py`; `_cmd_v3_review_subject` and the v1 branch of `_cmd_v3_review` in full; the
  head and both new classes of the two test modules.
- **Sampled:** the C0 plan's pre-repair sections (goal, boundary, reading list, resume pointer); the
  FULL record's §3 and §7 against my own probe results; `ResearchSystem/schema/` subtree counts.
- **Probed only:** the seven mutations in §2 and §3; the dispatch reproduction; the frozen-surface,
  oracle-hash and worktree commands; the five suites and repo-audit.
- **Not read:** `review_result_v2.py`, `review_subject.py`, `dispatch.py` — the repair touches none
  of them, and the FULL covered their call sites; the rest of `rsc.py`; the other 300-odd tests
  individually (I ran them, I did not read them).
- **`UNVERIFIABLE`, not folded into supported:** that a preview card was rendered and approved for
  the repair round (E11); that staging used explicit paths rather than `add -A` (E8) — the diff is
  consistent with it and that is all I can say; that the user's fix approval covered L1/L2/L4 by
  name rather than by the FULL's tiering, since the recorded quote does not enumerate; that the
  FULFILLMENT template shape survives a real run, since M9 is out of scope by ruling and no run
  exercises it.
- **Mutation ceiling (R4).** The probes in §2 prove those five guards have binding force. They do
  not prove that force is *sufficient*, and V1 is a concrete instance of the difference. This VERIFY
  is not a re-certification of the round: M8 and M10 were judged on the FULL's record, and what I
  re-derived is what the repair could have disturbed.

---

## 7. Residual uncertainty

1. V1 — one direction of the mkdir ordering claim has no test; deleting the line entirely is
   invisible to all 321 review tests.
2. V2 — the plan carries two different values for the same suite measurement, and the ticked
   checkbox is against the stale one.
3. E11 for the repair round, and E8's explicit-path staging, are process claims with no evidence
   lock at any revision (REVIEW.md's honesty ceiling), not gaps.
4. The scope of the user's fix approval is recorded as a quoted sentence, not as a list of accepted
   finding IDs; the riders are attributable only through the FULL's own tiering.
