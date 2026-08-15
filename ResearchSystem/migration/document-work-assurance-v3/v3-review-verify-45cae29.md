# V3 review — VERIFY — subject `45cae29`

**Subject range** `3ca107a..45cae29` — one commit, `V3-PHASE-B-REVIEW-FIX-v1`.

**Verdict: `REVIEWED_NO_BLOCKER`.**

Both accepted findings are genuinely repaired and the permanent boundaries are intact. Three
findings are recorded below. The VERIFY vocabulary has no `CHANGES_REQUIRED` (R3), so the
verdict word carries less than V-1 deserves: **V-1 is a measured reduction in the binding force
of a live gate, and the commit's own disclosure states the opposite.** Whether it opens a round
is the user's call, not mine.

**The tip moved during this review.** A commit outside my range — `9ca025a`
`V3-PHASE-B-README-COUNT-ERRATA-v1`, 03:04, ten minutes after the subject — corrects the
subject's `assurance/README.md` count. It is not part of my subject and I did not review it as
one, but it changes a file the subject introduced, so §3 V-3 records what I found and what the
errata already fixed, and every figure below is stamped with the revision it was taken at.

---

## 1. What this round is, re-derived

Not taken from the dispatch, which carried the range and nothing else (R2).

| Question | Answer | Where I read it |
|---|---|---|
| Round | The fix for the Phase B FULL, Step 4 of the deletion-first stabilization plan | plan Resume pointer; commit body |
| Governing instructions | `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` (E1–E12 / R1–R9). The review-side contract at the dispatched path is a 5-line supersession stub | the stub; checklist header |
| Budget position | A valid independent FULL occurred (`3ca107a`), so the subject is **the fix round** and obliges this VERIFY (E9). `9ca025a` names its own kind, "errata", which E8 lists | `v3-review-full-2687d8c.md`; `git log` |
| Authorization | Plan Step 4 authorizes Phase B. The 2026-07-28 user ruling on the frozen scripts is cited in the commit body and the new README; it exists in chat, not in the repository | plan; commit body; ledger |
| Obligations | Repair B-1 and B-2; add a probe that would have caught them; suite green; audit exit 0; freeze surface intact | FULL §7; plan Acceptance line 10 |

**Ceiling (R7).** The 2026-07-28 ruling on the 38 frozen scripts, and the routing of this VERIFY,
are chat-only. I state the ceiling and move on. "Fresh context" is marked, not verified (R4).

**Read coverage (R4).** Read in full: the complete repair diff (8 files), the new guard module,
`assurance/README.md` at both `45cae29` and `9ca025a`, the template's four files, `repo-audit.py`
across every region that consumes `strip_fences`, `v3-review-full-2687d8c.md`,
`CONSTRUCTION-CHECKLIST.md`, the plan's freeze surface and Phase B/E steps, the ledger pointer.
Sampled: `N3-record.md` §4 and its later burden restatements. Probed by execution: the suite
(three clean runs, two mutated), the audit (seven runs), all three template scripts, all 38
frozen scripts, six mutations. The 235 renamed blobs were not re-read — re-verified by digest.

---

## 2. The accepted findings — verified repaired

**B-1 — positional root resolution off by one. Repaired.** All three scripts now reach their own
logic instead of dying on the import. Run at `45cae29`, pasted:

```
run_bind_v2.py      -> AssuranceFault: document not found: ...\run-v2\evidence\review-full.json  (exit 1)
run_evidence_v2.py  -> AssuranceFault: document not found: ...\run-v2\control\work-spec.json      (exit 1)
check_template_instance.py -> prints its usage banner                                             (exit 2)
```

The corrected indices are arithmetically right at the intended instantiation depth as well:
`ResearchSystem/assurance/runs/<id>` has `parents[3]` = repo root, which is what
`check_template_instance.py` now uses.

**B-2 — template routed a new run back under `generated/`. Repaired.** The joined form is gone
from the whole template directory:

```
$ git grep -n "generated/document-assurance" 45cae29 -- 'ResearchSystem/assurance/templates/*'
(no output)
```

Both fixes are minimal and add no machinery (E6-safe). The FULL's L-1 correction is carried in
the plan's Resume pointer, which is inside the plan's own writable tracker under the freeze
surface's 2026-07-28 narrowing.

---

## 3. Findings from the repair diff

### V-1 — the `repo-audit` widening silently narrowed two checks it was not aimed at, and the disclosure says it did not

**Location.** `Thesis/Work/Tooling/repo-audit.py:41-48` (`strip_fences`).

**What the commit claims.** *"the change was proven not to weaken the check by planting a real
broken link and watching it go red."* That probe covers one consumer. `strip_fences` has three:
the markdown-link scan (line 89), the **wiki-link scan** (line 108, sharing the same stripped
`text`), and the **dangling fragment-ID scan** (line 196, an independent call). Only the first
was probed. The function's own new docstring says *"before any link scan"*, which is not what
line 196 is.

**Measured at the tip.** Planting one undefined fragment ID, the only variable being backticks:

```
`SBX-F99` in backticks  ->  [OK] Dangling fragment-ID references: 0     RESULT: clean (exit 0)
 SBX-F99  bare          ->  [!!] Dangling fragment-ID references: 1     RESULT: exit 1
```

Same shape for a non-existent wiki target: backticked → exit 0, bare → exit 1. Both went from
red to green. Reproduced at `45cae29` and again at `9ca025a`.

**Why this is not a corner case.** Backticks are how this repository writes fragment IDs.
Measured over the 400 tracked markdown files at `9ca025a` (worktree content read as UTF-8; my
own untracked record excluded):

| Scan | Visible before | After | Lost |
|---|---:|---:|---|
| fragment-ID mentions (381 ID-checked files) | 622 | 560 | **62 (10%)** |
| wiki links | 50 | 35 | **15 (30%)** |
| markdown links | 1354 | 1349 | 5 (the intended class) |

The loss is concentrated exactly where the check matters most — the intake packet ledgers that
are the authoritative home of fragment state:

```
-34  Thesis/Work/Intake/2026-06-01-workload-per-engine-sandboxing/README.md
-16  Thesis/Work/Intake/2026-07-02-shared-sandbox-identity-scout/README.md
 -4  Thesis/Work/Design/sandbox-mediated-agent-execution/source-dependencies.md
 -1  Thesis/Work/Intake/INDEX.md          (and 5 further files at -1/-2)
```

**Ground truth violated.** E4 — the guard was not seen fail across the surface it actually
governs. E7 — the fix was written against the reported instance (a `](...)` in a review record)
rather than the defect class, which here is *what else reads this helper*. The audit is the
repository's pre-commit link-graph gate, and `CLAUDE.md`'s intake rules rest the fragment-ID
discipline on it.

**Minimum fix.** Strip inline spans for the two link scans only, leaving line 196 on the
fence-only strip — `REF_RE` is documented as matching *a fragment-ID mention in prose*, and a
backticked ID is this repository's normal prose form. That is a boundary change to an existing
helper, not new machinery (E6-safe).

### V-2 — the new guard binds two of the three indices it was added to protect

**Location.** `ResearchSystem/tooling/tests/document_harness_review/test_run_v2_template_usable.py:52`.

Run bare, `check_template_instance.py` hits `print(__doc__)` / `return 2` at lines 73–74 —
**before** line 76 computes `run_dir.parents[3]` and line 78 imports `rsclib`. So for that script
both assertions are satisfied by a path that never touches the thing under test:
`test_scripts_import_rsclib` passes vacuously, and the negative control passes through its
`"Usage:"` branch, which is that same early return.

**Demonstrated.** Restoring the pre-repair defect in that one file — `run_dir.parents[3]` back to
`parents[4]` — leaves the guard and the whole suite green:

```
guard only  : 5 passed
full suite  : 437 passed
```

Restored byte-identically (`sha256 57697d6e…` before and after).

The commit body states the guard *"runs each script and asserts it never dies on a missing
rsclib"*; that is true of two scripts. The FULL asked for a probe that executes *"the template,
or an instantiated copy of it"* — the instantiated-copy branch is the one that reaches this
script's `main()`. The consequence is narrow but is this round's own defect class: if the tree
moves again, that index breaks and the suite stays green.

The guard's force over the other two scripts is real, not assumed. All four claimed mutations
reproduce independently, each restored from sha256-checked scratchpad copies:

| Mutation | Result |
|---|---|
| `run_bind_v2` index back to the defect | 2 failed (import assertion + negative control) |
| `run_evidence_v2` CONTROL_ROOT back to old path | 1 failed (control-root test) |
| template README back to old run home | 1 failed (readme test) |
| `run_bind_v2` body gutted to `sys.exit(0)` | 2 failed — negative control fires; import assertion correctly still passes |
| *(mine)* `EXPECTED_RUN_HOME` pointed at a non-existent tree | 3 failed — reverse control fires |

### V-3 — the "38" count: found here, already corrected by the errata outside my range

At `45cae29`, `assurance/README.md` and the commit body both said 38 scripts *"now fail with
`ModuleNotFoundError`"*. 38 is the number of `.py` files under `runs/` and `shadow/`; the number
that fails on `rsclib` is **36**, which is what the FULL reported.

I derived 36 by execution rather than inspection. All 38 guard `main()`, so module-level
execution has no side effects; each was run with its own directory on `sys.path`, as a real
invocation would have it:

- **35** fail at module level with exactly that error;
- **1** (`runs/p3-corr/check_template_instance.py`) imports `rsclib` lazily inside `main()` under
  the same broken `parents[4]`, so it fails the same way when invoked — 36 total;
- **2** (`shadow/round-2/build_round2.py`, `shadow/round-3/build_round3.py`) contain **zero**
  references to `rsclib` (`grep -c rsclib` → 0 for both) and import cleanly.

`9ca025a` corrects the file to exactly this breakdown, by static derivation, reaching the same
36/35/1/2 split I measured by execution. I re-checked each of its new claims and all hold,
including the one it volunteers — that `build_round2.py`'s copy-rewrite table still encodes the
pre-move depths (lines 55–56). Its "no other file touched" is accurate: `git diff --stat` over
`45cae29..9ca025a` is one file, 8 insertions, 2 deletions.

What the errata does **not** reach is the heading above the corrected paragraph, *"The scripts
under `runs/` and `shadow/` do not run in place"*, which remains false for the two builders —
and those are the two a reader is most likely to try, because `build_round3.py`'s own docstring
invites re-running it to diff output against what is committed. Recorded as low: no check
outcome turns on it, and the corrected body text now immediately below it says which files
break.

The rest of that README is supported. I verified the ruling's stated basis rather than accepting
it: `N3-record.md` §4 does carry `measure.py`'s output table in full, its figures are restated
unchanged at three later points in the same record, and stabilization plan Step 10 asks Phase E
to compare against *the recorded old reading* and to record `measure.py`'s methodological defect
— neither of which requires executing it. The link to `N3-record` resolves.

### V-4 — low: one guard assertion is a substring where E5 asks for the whole line

`test_control_root_points_at_the_run_home` asserts the expected prefix is *in* the `CONTROL_ROOT`
line. Replacing that line with `CONTROL_ROOT = "ResearchSystem/assurance/runs/"` — right prefix,
`{RUN_ID}` dropped, so every run would collide on one directory — keeps the guard green
(`5 passed`). Restored. Low: the hand-written-literal half of E5 is honoured and explicitly
reasoned about in the module, and `check_template_instance.py` validates real instances
separately.

---

## 4. Permanent boundaries — re-derived, not accepted

Every frozen blob by `git rev-parse <rev>:<path>`, across the repair **and** the errata:

| Blob | `3ca107a` → `45cae29` → `9ca025a` |
|---|---|
| signed plan `document-work-assurance-harness-v3.plan.md` | `8ad404b1` unchanged |
| contract v3 | `b2dbdf75` unchanged |
| supersession-1 | `68031fa2` unchanged |
| `CONSTRUCTION-CHECKLIST.md` | `0af94caa` unchanged |
| oracle `expected-construction-prompt.txt` | `5cf970c1` unchanged |
| oracle `test_readme_enumeration.py` | `57cecbb0` unchanged |

- `git diff --stat` over `ResearchSystem/schema/` and `ResearchSystem/contract/` is **empty**.
- **Closed runs byte-identical**, on the FULL's own recipe (sorted blob ids of all 103 files),
  reproduced across every revision of this phase: `76914a32` at `33fac6f`, `2687d8c`, `3ca107a`,
  `45cae29`. The repair touched no frozen evidence — consistent with the ruling it records.
- The stabilization plan **is** writable for its own tracker under the freeze surface's
  2026-07-28 narrowing, so the Resume-pointer edit is in boundary.
- `Thesis/Work/Tooling/repo-audit.py` sits outside the round's subject. It was disclosed in the
  commit body rather than folded in, which is what E9 requires; V-1 is about its substance, not
  its disclosure.
- **Suite** `437 passed` (was 432; the new module contributes exactly 5 tests), at `45cae29` and
  again at `9ca025a`. **Audit** exit 0 at both.
- **Commit hygiene (E8).** Single dense title, one paragraph, no trailers, kind named ("Review
  fix for the FULL committed at 3ca107a"). Untracked `ResearchSystem/docs/` was not swept in.

---

## 5. Probe hygiene

Six mutations were applied to the worktree and reverted from sha256-checked scratchpad copies,
never `git checkout --`, with the hash printed before and after each. Four temporary probe files
were created at the repo root and deleted. Final state: suite `437 passed`, audit
`RESULT: clean (exit 0)`, `git status --porcelain` showing only the pre-existing
`?? ResearchSystem/docs/` and this record.

One measurement was corrected before publication rather than after. My first V-1 figures came
from two recipes that disagreed on hidden markdown links (5 vs 11). The git-based recipe was
wrong: `subprocess.run(text=True)` decodes with the machine locale (GBK), which mangles the
Chinese-heavy files and moves where backticks pair. The table in V-1 is the surviving recipe —
tracked files read from the worktree as UTF-8 — and both runs of it agree.

---

## 6. What this VERIFY does not claim (R4)

A VERIFY is not a re-certification. Mutation showed the new guard has binding force over two
scripts; it does not show that force is sufficient. I did not re-derive the 235 renames or
re-read the moved tree — the FULL did that and the digests hold. `9ca025a` is outside my subject
and is reported, not adjudicated. The 2026-07-28 ruling itself is beyond my reach (R7); I
verified only the two factual premises the repair rests on it — that `measure.py` has no
downstream execution need (supported) and that the frozen scripts fail loudly (true of 36 of 38,
which the errata now states correctly).
