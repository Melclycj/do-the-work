# Targeted VERIFY — `3d5c705..3149581` (round `SUBMOD-HOOKENV`, fix leg)

**Verdict: `REVIEWED_NO_BLOCKER`.** All five items of the fix-gate ruling are delivered and every
one of them re-verified independently — not by comparing the fix's text to the FULL record, but by
re-running the commands under it: the corrected quickstart executed end to end in a fresh scratch
repository and seen to refuse; all four mutation rows of the errata re-applied to the candidate
bytes and reproduced per-test, exactly; the corrected line numbers re-derived by grep against the
same digest. The repair diff contains nothing outside the approved boundary, and the permanent
boundaries are intact. One non-blocking observation (a `HD-41` ④ discipline gap whose measured
effect is nil) is recorded in §5.

Everything below was re-derived from the repository (`R2`); no figure in any commit body, plan or
journal was accepted as given — where one is quoted, I re-ran the command that produces it.

---

## 1. The subject, derived

```
$ cat .harness/review-pending.json
{
 "subject": "3d5c7050825f0d7459cb6e8c0702d3884b44562b..314958129c9be56168d054af8e11d01ceef7f19b",
 "dispatched_at": "2026-08-23T18:15:55+00:00"
}
$ git rev-parse HEAD
314958129c9be56168d054af8e11d01ceef7f19b
$ git status --porcelain
(empty)
```

Window intact: the tip commit is `2026-08-23 18:15:00` UTC against a dispatch of `18:15:55` UTC,
nothing since, worktree clean at open and at close. The dispatch marker is an untracked runtime
file (`git check-ignore` confirms), so no committed file carries a written tip SHA (`E12`).

**Three commits, classified by hand; parentage linear, zero merges
(`git rev-parse 0732620^ 2629c56^ 3149581^` → `3d5c705`, `0732620`, `2629c56`).**

```
0732620  V3-REVIEW-RECORD-SUBMOD-HOOKENV-3d5c705-v1   record (the shared FULL; lands alone)
2629c56  V3-SUBMOD-HOOKENV-PLAN-FIXGATE-v1            plan amendment (ruling carrier)
3149581  V3-SUBMOD-HOOKENV-FIX-v1                     review fix (the one user-approved leg)
```

**Five paths, classified by hand** (`git diff --name-status 3d5c705..3149581`): the FULL record
(added, `migration/…/v3-review-full-3d5c705.md`), the plan's fix-gate section (modified), and the
repair proper — `README.md` (M), `document-harness/ONBOARDING.md` (M),
`document-harness/journal/submod-hookenv-2026-08-24.md` (A). The repair diff is exactly the three
files the fix commit names.

## 2. Round, budget, authorization — derived

The shared FULL over `153302a..3d5c705` returned `CHANGES_REQUIRED` (2 blockers, 4 lows,
5 observations; record `0732620`). `E9`'s test — has a valid independent FULL occurred? — now
answers **yes**, so `3149581` is the round's one user-approved fix leg and this record is the
obliged targeted VERIFY, the budget's last leg. The approval is carried by the plan's fix-gate
section at `2629c56`, which draws the boundary as exactly five items (B-1, B-2, L-1, L-2, L-3) and
places L-4, `0133d1b` and the five observations outside it. FULL-dispatch window re-checked: after
tip `3d5c705` (17:02:06Z, dispatch 17:03:09Z) the only commit is the record itself (17:31:04Z);
the fix-gate and fix commits both predate this VERIFY's dispatch. Per `R7`: the fix-gate ruling
("全包吧", 2026-08-24) reaches me as orchestrator-authored prose in a committed plan — the standing
shape this track has accepted; ceiling stated, moving on. Nothing load-bearing is chat-only: the
ruling has its plan carrier, the errata its journal carrier.

## 3. The accepted findings, each re-verified independently

### 3.1 `B-1` — the quickstart now delivers its own promise. CLOSED, re-executed rather than re-read

The README gains step 3 (the tracked half of hook wiring — a ten-line `.githooks/pre-commit`
invoking both mounted guards, staged, `--chmod=+x`, checked by `git ls-files -s` printing
`100755`), placed **before** the `core.hooksPath` step (now 4), proof step now 5 — the FULL's
minimum fix, in the required order. I executed the corrected block end to end as one sequence in a
fresh scratch repository (one prior commit, mount via local `file://` clone of this repository —
the same substitution the FULL used for the defect direction, irrelevant to hook wiring):

```
$ git submodule status
 314958129c9be56168d054af8e11d01ceef7f19b vendor/dtw (heads/main)
$ python vendor/dtw/tooling/dtw.py init --repo-root .   → RESULT: 5 created, 0 left as found (exit 0)
$ wc -l < .githooks/pre-commit                          → 10
$ git ls-files -s .githooks/pre-commit                  → 100755 7f672c4dff68687328f7a72c800a89d75198350b
$ git commit -m "quickstart step 5: cite a path that does not exist"
pre-commit BLOCKED: newly written text names a repository path that exists nowhere:
  docs/note.md: `docs/no-such-file-quickstart-probe.md`
must-fire commit exit=1
$ git commit -m "caller: mount the instrument, wire the tracked hook"
[master 57e8ab8]  3 files changed, 14 insertions(+)
 create mode 100755 .githooks/pre-commit / 100644 .gitmodules / 160000 vendor/dtw
negative-control commit exit=0
```

The FULL's failure shape — `core.hooksPath` naming a directory nothing creates, the "refusal"
committing silently at exit 0 — is closed: the refusal fires and names the planted path, the clean
commit lands the hook. One byte-level corroboration of the journal's own re-walk: my authored hook's
blob id `7f672c4d…` is **identical** to the one the journal's step 3 pastes — same content, same
blob — so the hook the re-walk ran is exactly the README's ten lines with `<mount-path>`
substituted. The preamble now cites the re-walk record and discloses the first form's failure in as
many words; the covered/remaining sentence's restated split is accurate against `ONBOARDING.md`'s
nine items — covered five are the mechanical ones (1 mount/pin, 2 `.harness/`, 3 decision log and
4 rider bank both created by `dtw init`'s "5 created", 9 hook wiring), remaining four named are
exactly items 5–8 (journal, ledger, policy file, entry-file pointer), and the wrong
which-revision-to-pin example is gone.

### 3.2 `B-2` — the errata's mutation table is true and the withdrawal is warranted. CLOSED, re-measured

I re-applied all four mutations to the candidate bytes myself — scratchpad copy, sha256
`9089dc67…44ba` verified before first swap and after every restore, never `git checkout --` — and
ran the seven-test module under each. Measured, per test:

```
M1  drop env= on ls-files call     plain PASS  all FAIL  shadow FAIL  work-tree FAIL  empty PASS  ctl-mount FAIL  ctl-super PASS   4 failed, 3 passed
M2  drop env= on toplevel probe    work-tree FAIL, six PASS                                                                        1 failed, 6 passed
M3  return listed, unguarded       empty FAIL, six PASS                                                                            1 failed, 6 passed
M4  drop GIT_INDEX_FILE from list  plain PASS  all FAIL  shadow FAIL  work-tree PASS  empty PASS  ctl-mount FAIL  ctl-super PASS   3 failed, 4 passed
post-restore                       7 passed in 8.42s
```

Every row of the journal's §1 table reproduces **exactly** — including the two corrections that
were the blocker: the plain-commit pin passes under M1 and M4, and `ctl-mount` goes red under
both, so the candidate's "stay green under all four" sentence was false and is rightly withdrawn.
The errata's characterization of what the candidate claimed is itself accurate — I re-read
`3d5c705`'s VERIFICATION section: its M1/M4 rows do list the plain-commit form among the failures,
and the both-controls sentence is there verbatim. The stated mechanism (the surviving
`return listed or None` turning the relative-index branch's empty listing into `OUT_OF_INDEX`, a
blind spot only `ctl-mount` distinguishes from correctness) is consistent with every measured
cell, and the journal's independence claim ("nothing is copied from the review record") is a
process claim I mark rather than verify — nothing turns on it, since the content is now
established by my own run regardless of provenance.

### 3.3 `L-1` — the corrected class-scan rows resolve. CLOSED

```
$ sha256sum tooling/rsclib/document_harness/paths.py   → 9089dc67…44ba  (blob unchanged 3d5c705 → HEAD)
$ grep -n '\["git"' tooling/rsclib/document_harness/paths.py
124 / 169 / 184 / 243 / 330                            → the five sites, exactly the errata's corrected offsets
```

The stale numbers (121/166/181/240/327) survive nowhere in the round's work files outside the
errata's own "claimed" line and the immutable candidate body — scanned across `README.md`,
`ONBOARDING.md`, both plans, both journals, ledger and riders; zero sibling sites.

### 3.4 `L-2` — the threshold now reads "reaches 130 characters". CLOSED

`ONBOARDING.md:220` carries the corrected form, matching the walk journal's own derivation ("the
first root prefix that trips it is 130"). Class scan: no "exceeds 130" remains anywhere; the only
other "130 characters" hit is the walk's derivation, which was already correct.

### 3.5 `L-3` — the README absolute is aligned to the layer. CLOSED

`README.md:34-36` now reads "independent is the norm, and a round that merges the two work-side
roles is the exception, disclosed rather than silent" — the same norm-plus-exception reading as
`ORCHESTRATION.md:26` ("Independent is the norm; one session holding both work-side roles is the
exception") and `HD-55`. Class scan: no other "three different sessions" absolute exists in
README or the layer.

## 4. The whole repair diff, and the fix commit's own claims

Every hunk maps to an approved item and to nothing else: README — one hunk L-3, three hunks B-1
(preamble, step 3–5 block, covered/remaining); ONBOARDING — one hunk L-2; the journal — B-2 + L-1
errata (§1–2) and the B-1 re-walk record (§3), with ceilings stated in both. No edit falls outside
the five items; the plan hunk is the ruling carrier, not repair. The fix commit's verification
claims, re-derived rather than accepted:

- **Battery**: `cd tooling && python -m pytest -q` → **`851 passed in 128.95s`** (their 136.64s —
  count identical, timing theirs).
- **Staged diff exactly three files**: confirmed by the commit's own tree diff (§1).
- **Candidate-lint, 2 unresolved tokens**: replicated with the module's own logic
  (`path_like_tokens` + `classify_path_token` over the repair's added lines, then the hook's
  per-file de-duplication that `unresolved_path_tokens` applies). Unique unresolved tokens: 2 —
  `docs/note.md` and `docs/no-such-file-quickstart-probe.md`, both the scratch caller's own paths
  quoted in the journal, the accepted class. The figure is exact under the instrument's own
  counting convention (de-duplicated; raw occurrences are 3, the probe path appearing twice).
- **`layer_path_check` exit 0**: true by construction — the repair adds lines to no `E10` member,
  so the guard has nothing to scan; not independently re-run.

## 5. Residual findings — none blocking

- **Observation — `HD-41` ④ not carried by the fix commit body.** The discipline ("修 finding
  先跑扫类 grep 并贴证据…把 grep 输出贴进 commit 正文") is met nowhere for L-2/L-3 and only in the
  record channel (journal §2, the corrected values' own grep) for L-1; the commit body describes
  scans, pastes none. Measured effect nil: my own class scans over the round's work files (§3.3–3.5)
  found zero unfixed sibling sites for all three classes, so no downstream decision changes. No
  tree fix is available (`E8` forbids amending the body), and `HD-41`'s 2026-08-17 追认 records the
  user deliberately keeping this as pure discipline after watching it bypassed — the compensating
  control it chose is exactly a reviewer running the scan, which is what happened. Recorded, not
  inflated.
- **Open items outside this round's boundary, unchanged and correctly parked**: L-4's closeout
  journal note and O-5's register disposition are owed at closeout, which has not happened; the
  fix-gate section states both. Not this leg's to demand.

## 6. Boundary check (run second, per `R3`)

- **`E2`.** Zero frozen paths in range (`git diff --name-only 3d5c705..3149581 --
  schema/document-assurance-v3/ contract/` → empty). At HEAD: v4 at blob `dfc983d2…` (the corrected
  literal `E2` names), schema pack **15** files.
- **`E10`.** Zero of the nine members touched, checked path by path — the repaired `README.md` is
  the repository root's, not the member `document-harness/README.md`; `ONBOARDING.md`, the journal,
  the plan and the record are non-members.
- **`E8`.** Linear, zero merges, one author, no trailers, single-paragraph bodies; kinds named on
  all three commits (record / plan amendment / review fix) and named **correctly** this time.
  Branch is `ahead 13` of `origin/main` — nothing pushed.
- **`E9`.** Accounting closed: one FULL (record `0732620`), one user-approved fix (`3149581` under
  the `2629c56` ruling), this VERIFY. Both review windows held (§1, §2). No exceeding of the fix
  boundary, silent or otherwise.
- **`R6`.** This record is `migration/document-work-assurance-v3/v3-review-verify-3149581.md`; the
  orchestrator commits it (suggested title `V3-REVIEW-RECORD-SUBMOD-HOOKENV-VERIFY-3149581-v1`).
  The dispatch marker's deletion belongs to that commit act.

## 7. Coverage and honesty ceilings (`R4`)

**Read in full**: `CONSTRUCTION-CHECKLIST.md` (both sides), the review-contract stub it supersedes,
`HARNESS-DECISIONS.md` header + `§live` (eight entries `HD-56`…`HD-9`), the FULL record `0732620`
end to end, all three commit bodies, the whole repair diff hunk by hunk, the new journal end to
end, the fix-gate section, the rendered README quickstart at HEAD. **Sampled**: `3d5c705`'s body
(VERIFICATION and class-scan sections — the errata's subject), `ONBOARDING.md` (the nine-item
headings and the corrected Second-execution paragraph), `ORCHESTRATION.md` (the three-roles norm
lines), `paths.py` (the two mutated functions and the token/lint functions),
`candidate_path_check.py` (docstring and imports). **Probed only**: `submod-hookenv.plan.md`
outside the fix-gate section; prior verify records for naming convention. **Not read**: the
contract v4 text and schema pack (byte-unchanged, which is all my boundary check needs);
`EXECUTION.md` / `REVIEW.md` (product-run charters; this is a construction round).

**Ceilings.** One platform — everything I ran is Windows, same machine that grew the harness; the
POSIX legs are CI's, unmeasured here. My quickstart re-execution mounted a local `file://` clone
pinned at the tip `3149581`, not the published remote at `1a0a200` — provenance and revision both
differ from the journal's re-walk, and neither difference touches hook wiring, which is the
finding's subject; between the FULL (local clone, pre-fix defect direction), the executor's re-walk
(published remote at `1a0a200`) and this run (local clone at tip), the block has now held under
three provenance/revision combinations. The journal's interpreter caveat (probe's `python3` vs
step 0's `python`) was not re-measured — my hook ran green under its own probe, which is all this
leg needs. Mutation reproduction establishes the errata's table is true, not that the suite is
sufficient (`R4`); the FULL's `O-3` on `plain` remains the recorded shape. Process claims — the fix
executor as a separately launched session holding none of `R1`'s four holdings, its tip checks at
open and stage, the errata's fresh-run provenance — are marked, not verified; `E1`'s disclosure is
present and correctly shaped on the fix commit. The worktree was left as found: `paths.py` swapped
five times (four mutations + restores against the scratchpad copy), sha256 re-checked after every
restore, `git status --porcelain` empty at close.
