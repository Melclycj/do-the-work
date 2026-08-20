# V3 review — FULL — subject `2687d8c`

**Subject range** `33fac6f..2687d8c` — one commit, `V3-PHASE-B-RUN-HOME-MOVE-v1`.

**Verdict: `CHANGES_REQUIRED`.**

---

## 1. What this round is, re-derived

Not taken from the dispatch, which carried the range and nothing else (R2).

| Question | Answer | Where I read it |
|---|---|---|
| Round | Phase B (Step 4) of `.goals/plans/harness-deletion-first-stabilization.plan.md` | plan Step 4; commit body's first sentence |
| Governing instructions | `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` (E1–E12 / R1–R9); the two `v3-harness-*-contract.md` are 5-line stubs pointing at it | `v3-harness-review-contract.md`, `README.md` row 24 |
| Budget position | First review of this candidate → this is the FULL. One user-approved fix and one targeted VERIFY remain (E9) | no prior `v3-review-*-2687d8c.md`; `git log` shows no fix commit after the candidate |
| Authorization | plan Step 4 (committed) authorizes the move; the preview-card approval is chat-only | plan; commit body |
| Obligations | `git mv`; rewrite the 3 named live test modules; leave history unchanged; suite green; `repo-audit` exit 0; freeze surface intact | plan Step 4 + plan §Constraints + §冻结面 |

**Ceiling (R7).** The preview-card approval and the "this date" claim exist only in chat. I state the ceiling and move on; they are not treated as blocking. Likewise "fresh context" is marked, not verified (R4).

**Read coverage (R4).** Read in full: the six modified files' diffs, `CONSTRUCTION-CHECKLIST.md`, `document-harness/README.md`, `HARNESS-LEDGER.md` pointer block, the stabilization plan, `templates/run-v2/{README.md,run_bind_v2.py,run_evidence_v2.py,check_template_instance.py}`, `test_golden_views.py`. Sampled: `review_subject.py`, `assurance_state.pointer_to`, `rsclib/config.py`, `generate.py`. Probed by execution: the suite, `repo-audit`, two mutation probes, the two moved scripts below. The 235 renamed blobs were verified by rename-detection and digest, not read.

---

## 2. Blockers

Both facets below are one defect class — *a reference to the run tree's location that survived the move* — and one repair. The move shortened the path by exactly one segment (`ResearchSystem/generated/document-assurance/X` → `ResearchSystem/assurance/X`), and the round swept only the textual form outside the moved tree.

### B-1 — the live run-v2 template no longer executes: positional root resolution is off by one

**Location.** `ResearchSystem/assurance/templates/run-v2/run_bind_v2.py:22`, `run_evidence_v2.py:26` (`RS_ROOT = HERE.parents[3]`), `check_template_instance.py:76` (`repo_root = run_dir.parents[4]`).

**Ground truth violated.** These files are live product, not history: `document-harness/README.md` mandates the v2 shapes for newly opened runs; `research-agent-dev-p3corr-p4.plan.md` lists the run-v2 template under *"Harness product — this uses the built product, not an improvised one"* and records that it *"has never been run for real — Stage 1 is its maiden voyage"*; stabilization plan Step 10 (Phase E) requires the next real run to use the product and forbids hand-copying historical scripts. This same commit rewrote that plan's pointer to the new template path, so the round treated the template as live in one place and as history in another.

**Evidence — run at the tip, pasted, not described:**

```
$ python ResearchSystem/assurance/templates/run-v2/run_bind_v2.py
Traceback (most recent call last):
  File "D:\...\ResearchSystem\assurance\templates\run-v2\run_bind_v2.py", line 26, in <module>
    from rsclib.document_harness import load_json  # noqa: E402
ModuleNotFoundError: No module named 'rsclib'
```

The arithmetic, both sides of the move:

```
OLD parents[3] = D:\Thesis-stage-control-refactor\ResearchSystem
NEW parents[3] = D:\Thesis-stage-control-refactor   (correct index is now 2)
OLD run parents[4] = D:\Thesis-stage-control-refactor
NEW run parents[4] = D:\
```

`sys.path.insert(0, RS_ROOT / "tooling")` therefore points at a directory that does not exist, and `REPO = RS_ROOT.parent` becomes the drive root. The same holds at the intended instantiation depth (`assurance/runs/<id>/` is the same number of segments from the repo root as `assurance/templates/run-v2/`), so copying the template into a new run does not repair it.

**Why the round's own instruments did not see it.** The suite (432 green) does not import these scripts; `test_review_v2_subject.py` loads `check_template_instance.py` by explicit path and calls its check functions, never `main()`, so the broken `parents[4]` default is unreachable from the suite. `repo-audit` checks markdown links, not Python root resolution. The E4 probe covered the goldens only. A green suite here is silence, not evidence.

**Minimum fix.** `parents[3] → parents[2]` in the two template run scripts and `parents[4] → parents[3]` in `check_template_instance.py`. Per E7 the sweep, not the three instances, is the fix unit: 39 `.py` files in the moved tree resolve a root positionally (`grep -rlE "^(RS_ROOT = HERE\.parents\[|.*repo_root = .*parents\[)" ResearchSystem/assurance --include=*.py | wc -l` → 39); 3 are the live template. The other 36 are closed-run and shadow evidence — see O-2, which is a user ruling, not part of this repair.

### B-2 — the template still routes a new run back under `generated/`

**Location.** `ResearchSystem/assurance/templates/run-v2/README.md:6` (*"Instantiate by copying into `ResearchSystem/generated/document-assurance/runs/<run-id>/`"*) and `:10` (*"control root = `ResearchSystem/generated/document-assurance/runs/<run-id>/` … they are **load-bearing** here"*); `run_bind_v2.py:36` and `run_evidence_v2.py:50` (`CONTROL_ROOT = f"ResearchSystem/generated/document-assurance/runs/{RUN_ID}"`).

**Ground truth violated.** The round's stated purchase is that `ResearchSystem-Contract.md` E1.3 becomes true — *"Deleting everything under `ResearchSystem/generated/` loses no research content."* An operator following the template README puts the next run's control plane and evidence back under `generated/document-assurance/runs/`, re-breaking E1.3 the first time the harness is used. The alternative branch — instantiating under `assurance/runs/<id>/` while leaving `CONTROL_ROOT` stale — fails loudly (`assurance_state.pointer_to` raises `AssuranceFault` on a non-existent target), so the quiet failure is the one that reverses the round.

**This was inside the round's own measured surface, not outside it.** The commit body states *"residue was hunted with the segment form and the joined form, both clean."* The joined form is not clean:

```
$ git grep -n "generated/document-assurance" 2687d8c -- 'ResearchSystem/assurance/templates/*'
templates/run-v2/README.md:6
templates/run-v2/README.md:10
templates/run-v2/run_bind_v2.py:36
templates/run-v2/run_evidence_v2.py:50
```

And the reported "16 files / 46 occurrences" reconciles exactly as *matching lines in markdown files, repo-wide* (`git grep -c … -- '*.md'` → 46 lines over 16 files at the base). That 16-file set **includes `templates/run-v2/README.md`**. The file was counted and then classified as prose-history.

**Minimum fix.** Repoint those four lines to `ResearchSystem/assurance/runs/<run-id>/`. No new machinery (E6-safe).

---

## 3. Non-blocking findings

Recorded, deliberately not inflated — none of them changes an actor's action.

- **L-1 — commit-body characterization.** "both clean" is false of the joined form (B-2). The message is immutable; the correction belongs in plan Step 4's record, which currently repeats the same claim.
- **L-2 — "the three remaining generated segment hits belong to the harness and stages subtrees."** One of the three is `rsclib/config.py:23` `GENERATED_DIR = RS_ROOT / "generated"`, the root `generated/` directory that `rsc generate` writes `object-index.json` / `relation-graph.json` / `coverage.json` into — neither the harness nor the stages subtree. The other two (`harness/cli.py:21`, `stage_control.py:942`) match the description.
- **L-3 — figure label.** "46 occurrences" is a matching-**line** count. Over the same surface the occurrence count is 47; outside the moved tree and across all file types it is 13 files / 38 lines / 39 occurrences. The number is reproducible once the definition is named; the label is not the measurement.

---

## 4. Observations (R5 — shape reported, conclusion is the user's)

- **O-1 — E1.3 is restored for the machine output, not literally for the directory.** `ResearchSystem/generated/` still holds two hand-authored files (`README.md`, `stages/README.md`) alongside the three regenerable JSON files. The plan's Acceptance pre-declares the READMEs outside the research-content reading, so this is disclosed, not silent. Noted only because `generated/README.md` asserts *"Every file in this directory is machine-generated and must never be edited by hand"*, which is untrue of itself — pre-existing, untouched by this round.
- **O-2 — the closed-run and shadow scripts are now non-executable for the same reason as B-1.** 36 files under `runs/p3-corr`, `runs/w1-r1`, `shadow/**`. They are frozen evidence (`document-work-assurance-v3-revise-2.plan.md`: *"frozen evidence — never modify (V3-D9)"*), so repairing them and leaving them broken are both defensible and neither is mine to choose. One consequence is concrete rather than theoretical: stabilization plan Step 71 names `shadow/measure.py` as Phase E's burden-comparison anchor, and N3-record §4 links it as the instrument that produced the recorded figures. It fails identically:

  ```
  $ python ResearchSystem/assurance/shadow/measure.py
  ModuleNotFoundError: No module named 'rsclib'
  ```
- **O-3 — instrument reach.** Suite and audit were both green over a tree whose live template did not import. Neither instrument reaches script-level root resolution, and the round's guard probe was scoped to the goldens. Reporting the shape; whether a probe of the moved scripts belongs in the standing E4 discipline is the user's call.

---

## 5. Verified and sound — so the next round does not re-litigate it

Every figure below is re-derived here, not accepted from the commit body.

- **Rename purity.** `git diff --name-status -M` → 235 `R100` + 6 `M`. No rename below 100% similarity. The 21 insertions / 14 deletions account exactly across the six modified files.
- **Closed-run byte identity.** 103 files under `runs/` both sides; sorted blob-id digest identical:
  `76914a328ee7999870b1a1a32b4cdd12d70eca4ec33780901b8bf374fbe2396b` at `33fac6f` and at `2687d8c`. The commit's `76914a32` is its prefix.
- **Freeze surface intact**, each by `git rev-parse <rev>:<path>` at both ends: plan `8ad404b1…`, contract `b2dbdf75…`, supersession-1 `68031fa2…`, `expected-construction-prompt.txt` `5cf970c1…`, `test_readme_enumeration.py` `57cecbb0…`, `CONSTRUCTION-CHECKLIST.md` `0af94caa…`. `git diff --stat` over `ResearchSystem/schema/` and `ResearchSystem/contract/` is empty — the same-named `schema/document-assurance-v3/` was correctly left alone.
- **Suite.** `python -m pytest ResearchSystem/tooling/tests -q` → `432 passed in 59.28s`.
- **Audit.** `python Thesis/Work/Tooling/repo-audit.py` → `RESULT: clean (exit 0)`, `Broken markdown links: 0`.
- **The golden guard binds — reproduced independently, not accepted.** Repointing `GOLDEN_DIR` back to the old path yields a genuine assertion failure, not a crash:
  `AssertionError: False is not true : golden missing: run this file with --regen` — 2 failed, 3 passed. Restored from a scratchpad copy; `sha256 ac842c14…` identical before and after.
- **The N3 link repair was necessary and is minimal — reproduced.** Reverting only the four `](…)` targets turns the audit red with exactly those four:
  ```
  [!!] Broken markdown links: 4
       N3-record.md | ../../../generated/document-assurance/shadow/freeze_packages.py
       N3-record.md | ../../../generated/document-assurance/shadow/measure.py
       N3-record.md | ../../../generated/document-assurance/shadow/round-2/build_round2.py
       N3-record.md | ../../../generated/document-assurance/shadow/round-3/build_round3.py
  RESULT: hard issues found (exit 1)
  ```
  Restored; `sha256 79b0fc67…` identical before and after. The diff confirms prose and tables — including the §-allowlist declaration — are byte-unchanged; only the four targets moved, plus one dated note. Both disclosed deviations are genuinely disclosed, in the commit body and in plan Step 4.
- **No collateral path breakage.** No `.gitignore` entry touches either root. Both `.gitattributes` files (`* -text`, protecting the goldens from CRLF) moved with their directories and remain path-adjacent. No JSON in the moved tree encodes a relative path; no markdown in it uses a relative link — so the audit's clean link result is genuinely covering for that class. `review_subject.py` addresses run files relative to the control root (`STATE_PATH`, `CHECK_RESULT_PATH`), so no harness module hard-codes either root.
- **Commit hygiene (E8).** Single dense title `V3-PHASE-B-RUN-HOME-MOVE-v1`, one paragraph, no trailers, kind named ("Candidate for Phase B"). The pre-existing untracked `ResearchSystem/docs/` was not swept in — evidence against `git add -A`.

---

## 6. Probe hygiene

Two mutations were applied to the worktree and reverted from sha256-checked scratchpad copies (never `git checkout --`), with the hash printed before and after each. `git status --porcelain` at the end of this review shows only the pre-existing `?? ResearchSystem/docs/`.

---

## 7. What the fix round owes

One repair covering B-1 and B-2 — the four template path strings and the three template depth indices — and a probe that would have caught it: execute the template, or an instantiated copy of it, rather than inferring from a green suite. The VERIFY then covers that repair diff in full plus the permanent boundaries (freeze surface, closed-run digests, suite, audit). O-2's disposition for the 36 frozen scripts is a user ruling and is not part of the repair unless the user says so.
