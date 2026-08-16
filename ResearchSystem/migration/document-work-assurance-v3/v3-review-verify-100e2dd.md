# VERIFY — split batch R1, second repair leg, `dd7a27c..100e2dd`

**Verdict: `REVIEWED_NO_BLOCKER`** — every accepted finding is discharged, the A10 supplement is
correct in substance and mechanically confirmable, and the permanent boundaries hold.

Not `SPEC_GAP`. I opened one, then closed it: `E9` caps a round at three legs and R1 has now taken
four, which the checklist alone does not resolve. The checklist's own preamble sends a question it
is silent on to the retired contracts, and there the answer is explicit — budget classification
belongs to the user, and the executor's duty is to *propose* the accounting, never to self-classify
(`7011916` operating contract, role table line 119 and the budget paragraph at 138–140). The second
leg therefore rests on a ruling the user is entitled to make. What is wrong is the arithmetic of the
proposal, and that is `F-1` below, at low.

Findings: 2 low, 4 observations. No blocker, and none inflated to reach one (`R3`).

---

## 1. Subject, re-derived

Nothing accepted as reported (`R2`).

| | |
|---|---|
| Range | `dd7a27c1551cd34a49e923df3ec27c227630a479..100e2ddf42e1ca4232a50f0c4c35cc39a16d3d73` |
| Branch / worktree | `document-work-assurance-v3` @ `D:/Thesis-stage-control-refactor`; `git status --porcelain` empty; `HEAD` == range tip; no upstream configured, so nothing is pushed (`E8`) |
| Commits | 1: `100e2dd` `V3-SPLIT-R1-FIX2-A10-F1-F2-F3-F4-F5-v1`. Parent `dd7a27c`. Author date == committer date (no amend/rebase evidence) |
| Paths | 2 `M`, 0 `A`, 0 `D`, classified by hand: `.goals/plans/harness-repo-split.plan.md` · `ResearchSystem/document-harness/split-travel-manifest.md`. 46 insertions, 12 deletions |
| Freeze marker | `.harness/review-pending.json` names this exact range, `dispatched_at 2026-08-15T03:51:22+00:00`. Tip commit `13:50:34 +1000` = `03:50:34Z` (48 s before dispatch); the out-of-repo commit `13:51:16 +1000` = `03:51:16Z` (6 s before). Both round writes precede the dispatch |
| Round / leg | Split batch **R1**, the **second** repair leg. Base `dd7a27c` is the first VERIFY's own record commit (`v3-review-verify-e6b4d2c.md`, `REVIEWED_NO_BLOCKER` carrying a blocker-shaped `F-1`) |
| Budget (`E9`), re-derived | Four legs taken: FULL `0792a89` → fix `22264b5` → VERIFY `dd7a27c` → fix `100e2dd`; a fifth (this VERIFY) owed. `E9` budgets three. See `F-1` — the overrun is disclosed, its size is not |
| Authorization | The user's 2026-08-15 「甲 + 花」 ruling appears in the commit body, plan steps 14/14b, and the manifest's A10 row — executor prose, not a signed artifact. `R7` ceiling; nothing in the repository contradicts it. It is *not* chat-only, so `R2`'s clause is not engaged. Its absence from `HARNESS-DECISIONS.md` is correct: both halves are within-round, which `HD-4`'s reverse exclusion (轮内约束 / 可重算事实) keeps out |
| Out-of-repo | `D:/do-the-work`, now 3 commits (`345acdd`, `8cd0b9c`, `f7966c4`), 260 tracked, `git status` clean, no upstream. In remit and reviewed in full |

---

## 2. What I re-executed

The battery, in full, at the tip — not sampled, not taken from the commit body:

```
P2   ResearchSystem/tooling/tests/run_tests.py        tests: 29   passed: 29   failed: 0
P4   ResearchSystem/tooling/tests/run_p4_tests.py     tests: 80   passed: 80   failed: 0
P5A  ResearchSystem/tooling/tests/run_p5a_tests.py    tests: 39   passed: 39   failed: 0
fix  ResearchSystem/schema/fixtures/validate_fixtures.py   cases: 58   matched: 58   unexpected: 0
pytest -q (run from ResearchSystem/tooling)                701 passed in 93.04s
rsc.py compile --check    RESULT: generated output fresh; lint clean (exit 0)
Thesis/Work/Tooling/repo-audit.py                          RESULT: clean (exit 0)
```

Six legs, six green, plus repo-audit. The reported 29 / 80 / 39 / 58 / 701 reproduce exactly.

**The new repository**, in a throwaway clone (`git clone D:/do-the-work`), verified byte-identical to
its source before use — 260 tracked paths, every blob equal:

```
@ f7966c4 (tip)   python -m pytest -q   ->  20 failed, 681 passed in 80.10s
@ 8cd0b9c (pre-A10)                     ->  24 failed, 677 passed in 87.34s      [255 tracked]
```

Both figures reproduce exactly. Classification of the surviving 20, by `--tb=line`, grouped by
traceback rather than assumed:

```
15   can't open file '…/ResearchSystem/tooling/rsc.py'
 3   AssertionError: unexpectedly None : governance document not readable at
     <root>/.goals/plans/document-work-assurance-harness-v3.plan.md
 2   AssertionError: 2 != 1        (subprocess that runs rsc.py exits 2, not 1)
----
20
```

That is the round's own 15 / 2 / 3 split, independently derived, and it is the split the new
repository's README table now prints. The four cleared failures are exactly the A10 tests:

```
test_golden_views.py + test_dispatch.py   @ 8cd0b9c ->  4 failed, 52 passed
                                          @ f7966c4 -> 56 passed
```

`pytest -q -rs` over the whole tip suite reports **no skips and no xfails**, so nothing passes
vacuously — the count 681 is 681 tests that ran.

**Guard posture after A10** (five files were added to that repository, so the check is not free):

```
LAYER count: 9   missing: []                                     # all nine E10 members resolve
pytest ResearchSystem/tooling/tests/document_harness/test_precommit_checks.py -> 42 passed
```

I did not re-mutate the two path guards. The `B-1` repair they belong to was mutation-proved by the
previous VERIFY, this leg does not touch them, and `R4` forbids treating a VERIFY as a
re-certification.

---

## 3. Accepted findings — discharge

| Finding | Discharged | Evidence |
|---|---|---|
| `F-1` new repo README's failure account false | **Yes, and beyond the minimum fix** | the "and nothing else" sentence is gone; the replacement table prints 15 / 2 / 3, which is my own measurement; it states in bold that extracting the CLI does not by itself green the suite; it names the caller-side plan as the remaining dependency and warns that following the printed `--regen` instruction would overwrite a pinned surface. The `R5` boundary the finding drew is respected — the README says the caller-coupling question is R2's and does not settle it. The user's 「甲」 went further and moved the four fixtures, so the delivered state is the post-fix one |
| `F-2` false hook assertion in the manifest | **Yes** | measured: `D:/Thesis/.git/hooks/pre-commit` exists (executable, 2674 B) and its lines 52–54 invoke `review_freeze_check.py`, `layer_path_check.py`, `candidate_path_check.py`; `core.hooksPath` unset; `D:/Thesis/.git/worktrees/Thesis-stage-control-refactor/hooks` does not exist; `D:/do-the-work/.git/hooks` holds no non-sample entry. The replacement text says exactly this asymmetry |
| `F-3` two revision labels left at `a7437d3` | **Yes** | `:22` and `:112` both now read `e4ffa2b`. The three surviving `a7437d3` occurrences (`:11–12`, `:73`, `:121`) are deliberate historical or measurement references and each is true at that revision — I re-derived `:73`'s claim: top-level `.md` = **117** @ `0db52a1` and **123** @ `a7437d3`, i.e. 29 + 88 and 29 + 94 |
| `F-4` struck plan step cites the wrong finding | **Yes** | step 15 now cites `L-5`; read at the source, the FULL's `L-5` is "R2's own checklist step now names four deleted artifacts" and `L-6` is the line count, so the new citation is the right one |
| `F-5` Resume pointer still says the FULL is owed | **Yes in substance, wrong in one figure** — see `F-1` below | step 14 is `[x]` and spells out the FULL → fix → VERIFY → second-leg chain; 14b is new and records the A10 supplement with before/after measurements; the pointer paragraph is replaced and states a second targeted VERIFY is owed |

**A10 itself, verified mechanically rather than read.** I applied the manifest's own rules — the ten
A prefixes/files, the three B files, and the C directory minus the 29 names its exception table
lists (parsed from the file, all 29 present at the revision) — to `e4ffa2b`:

```
A: 26 + 18 + 4 + 11 + 17 + 15 + 8 + 6 + 3 + 5            = 113
B:                                                        =   3
C: 123 top-level - 29 exceptions = 94, + 49 sub-dir       = 143
                                                    total = 259
```

Every sub-count re-derived by `git ls-tree`, none taken from the file. Then, against the delivery:

```
manifest-derived travel set          259
new repo tracked minus its own README 259
in manifest not in new repo:  []
in new repo not in manifest:  []
```

The membership definition and the delivered contents agree **exactly**, path for path. Per-blob
against the caller at the range tip: 260 tracked in the new repository, **259 matched, 1 mismatch,
0 only-in-new** — the mismatch being the new repository's own authored `README.md`, whose path
collides with the caller's unrelated root README and which is not a travelled file.

The A10 rationale checks out at the level the finding cared about: `assurance/test/` and the two
`expected-*-prompt.txt` files were **0 in the new repository** at `345acdd` and `8cd0b9c` and are
3 and 2 at `f7966c4`; the whole `tooling/tests/fixtures/` prefix is **98** in the caller at every
revision in this round. Both `.gitattributes` and the two goldens travel as part of the prefix, and
the `-text` attribute the directory carries is the reason the byte comparison survives a Windows
checkout.

**The `E7` sweep, tested rather than trusted.** The finding's real question was whether the same
ruler had been run over the whole class, not the reported instance. I scanned every travelled file
under `tooling/tests/`, `tooling/hooks/` and `tooling/rsclib/` for repo-relative path literals and
resolved each against the new repository. After A10 exactly one class of real cross-tree read
survives — `.goals/plans/document-work-assurance-harness-v3.plan.md`, read by
`test_candidate_checks.py`, which is the 3 disclosed failures. Everything else that fails to resolve
is either a synthetic path a test builds inside its own tmpdir (`docs/guide.md`,
`docs/instruction.md`, …) or a string constant in `candidate_path_check.py`'s caller-owned-paths
list, never a file read. Combined with the zero skips, the class is closed for this repository as it
stands.

---

## 4. Findings

### F-1 — the budget accounting handed to the user understates what the round has spent

**Low.** Not inflated to blocker: the correct chain is stated in the same block, the fact of a
second fix leg is disclosed in the same sentence, and the user authorized the leg and therefore
knows it exists. What is wrong is the count, and a blocker here would burn the round's repair on an
arithmetic label while the substance is sound.

**Location.** `.goals/plans/harness-repo-split.plan.md` §Resume pointer — "**FULL 与 targeted VERIFY
各跑一次，两条修腿花掉 `E9` 三腿中的两腿，欠第二次 targeted VERIFY**" — and `100e2dd`'s commit body,
"R1 第二条修腿（`E9` 三腿的第二腿…）" and "本腿花掉 `E9` 第二腿".

**Ground truth, re-derived from the branch.** R1's legs, in order, each identified by the commit
whose landing makes it have occurred (`E9`):

```
0792a89  V3-REVIEW-RECORD-SPLIT-R1-e608204-v1   FULL      leg 1
22264b5  V3-SPLIT-R1-FIX-B1-L1-L3-L4-L5-L6-v1   fix       leg 2
dd7a27c  V3-REVIEW-RECORD-SPLIT-R1-e6b4d2c-v1   VERIFY    leg 3
100e2dd  V3-SPLIT-R1-FIX2-A10-…-v1              fix       leg 4
(this record)                                   VERIFY    leg 5, owed
```

`E9` budgets three. `io-design.md:19` says the same in the harness's own words — 评审预算至多三腿,
预算是轮的属性. So "the second of `E9`'s three legs" is not what this leg is, and "two fix legs spent
two of `E9`'s three legs" cannot be true of a round that has also run a FULL and a VERIFY. Under
every reading the sentence admits, R1 is past the cap and the text does not say so.

**Why it is not wording (`R9`).** Two decisions turn on it. ① The retired operating contract makes
budget the user's classification and the executor's *proposal* — "Propose the accounting; let the
user correct it. Never self-classify which round consumed what." A proposal that reports two of
three spent is asking the user to correct an accounting that conceals its own overrun; the one
number the user needs in order to classify is the wrong one. ② The plan names this pointer as the
cold-start entry. A fresh session reads "two of three" and concludes a leg remains inside budget,
when in fact the next spend is the second past the cap and needs the user before it is taken.

**Rule breached.** None outright — `E9`'s "exceeding an approved fix boundary requires saying so,
never silently" is satisfied in substance, since the leg is openly called a second fix leg. What
fails is `E3`: a count written into a delivered record that no command establishes, and which the
commands above falsify.

**Minimum fix.** State the count as measured — four legs taken, a fifth owed, past `E9`'s three
under the user's 2026-08-15 classification — in the Resume pointer. One sentence; the chain beside
it already carries the evidence.

### F-2 — the sentence added to carry `F-3`'s repair names the wrong commit for its own row

**Low, and wording-level under `R9`** — it banks rather than opening anything. No check outcome, no
binding, no permission, no obligation and no verdict path changes, and the accurate fact is one
`git log` away.

**Location.** `ResearchSystem/document-harness/split-travel-manifest.md:22` — "量程 = 全仓 tracked …
@ `e4ffa2b`（A10 一行于 `dd7a27c` 补入，其 5 件在 `e4ffa2b` 上同样存在，故该 revision 对整表成立）".

**Measured.**

```
git log --oneline -- ResearchSystem/document-harness/split-travel-manifest.md
  100e2dd  a1b80fa  22264b5              # three writes; dd7a27c is not among them
git show dd7a27c:…/split-travel-manifest.md | grep -c A10   ->  0
git show 100e2dd:…/split-travel-manifest.md | grep -c A10   ->  6
```

`dd7a27c` is the VERIFY *record* commit. The A10 row was added by `100e2dd` — this commit, the one
the sentence is in. The load-bearing half of the claim is separately true and I verified it: all
five A10 files exist at `e4ffa2b`, so pinning the whole table to that revision does hold.

**Minimum fix.** One token: `dd7a27c` → `100e2dd`.

**Worth more than the token.** `F-3`'s entire subject was wrong revision labels in this file, and
its repair introduced a new wrong commit label into the same header block — while the same commit's
body states "**本轮第三次同一形状**（`B-1` · `F-1` · `F-2`）：写下绝对量词而没先跑那条能证伪它的
命令". Counting this one it is the fourth, and the self-diagnosis that names it as the third is
itself the carrier. The class the previous VERIFY drew — a factual claim about the delivery written
into a delivered document without running the command that could falsify it — is what `F-1` above
and this finding both are. That makes six instances in one round.

---

## 5. Permanent boundaries

**`E2` — frozen bytes.** Untouched across the range and identical in both repositories:

```
Document-Work-Assurance-Contract-v3.md   b2dbdf75   base = tip = new repo
…-supersession-1.md                      68031fa2   base = tip = new repo
…-supersession-2.md                      e1a2f26b   base = tip = new repo
schema/document-assurance-v3/            15 files;  git diff base..tip -- <pack> = 0 changes
```

**`E10` — instruction layer, nine members.** All nine `SAME` from base to tip: no layer write in
this range at all, so no channel question arises and the leg owes the layer nothing new. All nine
are byte-identical between the caller tip and the new repository, so the two layers have still not
diverged. The independent read the round already owes (`a8af54c`'s `HD-42` enumeration edit,
`e4ffa2b`'s `L-1` bytes, `22264b5`'s `L-3` edit) is unchanged by this leg — same `EXECUTION.md`
blob `9f80e728`.

**`E9` — budget.** Four legs taken, a fifth owed, against a cap of three. Authorized by a user
ruling recorded as executor prose (`R7` ceiling), and the classification is the user's to make under
the retired contract's role table. The count as written is wrong — `F-1`.

**`E8` — git.** One new commit, no amend evidence, two explicit paths both inside R1's declared
surfaces, title `V3-SPLIT-R1-FIX2-…-v1` naming round and kind, dense multi-paragraph body carrying
no trailers (the 2026-08-07 ruling buys density and no-trailer, not a literal single paragraph),
branch has no upstream so nothing was pushed. The out-of-repo commit is likewise single, unamended
and unpushed.

**`E12` / freeze window.** The marker names exactly this range; `HEAD` == tip; worktree clean; both
of the round's writes precede the dispatch timestamp.

---

## 6. Observations

- **O-1 — the previous VERIFY's own figure was silently corrected, and correctly.** `F-1` said the
  `tooling/tests/fixtures/` prefix holds "100 files in the caller". Measured, it is **98** — at
  `a7437d3`, `a1b80fa`, `a8af54c`, `e4ffa2b`, `e608204`, `22264b5`, `e6b4d2c`, `dd7a27c` and the
  tip, and 98 on disk as well as tracked. Both the manifest and the new repository's commit body
  write 98. That is `E12` behaving as designed — reproduce the finding to write the fix correctly,
  not to adjudicate the reviewer — and I name it only because a reader auditing the fix against the
  finding meets an unexplained 100 → 98 with nothing to tell them which is right.

- **O-2 — the ledger's split-batch row is still false.** `HARNESS-LEDGER.md:98` still reads
  "**执行零进度：171 文件一个没删、新仓不存在**" and "**R1 开轮前三件**". 171 files are deleted, the
  new repository exists with 260 tracked paths, and all three pre-round items are paid. The previous
  VERIFY raised this as `O-3` and routed it to the closeout; it is outside this range too, and
  ledger fixes consume no `E9`. Named a second time only so the closeout cannot lose it — the file
  is the harness track's live pointer, and it has now been wrong across two reviews.

- **O-3 — half this leg's work is in no range at all.** `f7966c4` in `D:/do-the-work` carries the
  `F-1` README fix and the five A10 files, and by `HD-33` that repository is outside every SHA the
  dispatch can name. I reviewed it because it is reachable and the plan points at it, and the
  membership and blob comparisons above are what stands in for a diff. The arrangement works while
  the two repositories are resynced by hand in the same session; it has no mechanical guard, and R3
  is where the gitlink is meant to supply one.

- **O-4 — a shape, reported not concluded (`R5`).** This round has now produced six instances of one
  defect class — `B-1`, `F-1`, `F-2` from the first review pair, and `F-1`, `F-2` here plus the
  miscount they sit on — where each correction of the class introduced a fresh instance of it inside
  the corrective text. The previous VERIFY put the same shape to the user as its `O-5` and the round
  answered with a sentence counting the instances, which is itself now one of them. Whether that
  calls for machinery, a checklist clause, or nothing, is the user's question. My subject is the
  text that is there, and the text that is there is substantively correct — every load-bearing
  number in this leg re-derives.

---

## 7. Coverage and ceilings (`R4`)

**Read in full**: `CONSTRUCTION-CHECKLIST.md`; the retired operating contract at `7011916` (role
boundary and budget sections; the rest sampled by grep); `v3-review-verify-e6b4d2c.md`;
`v3-review-full-e608204.md` §4 Low and §5 Observations; `split-travel-manifest.md` at the tip;
`.goals/plans/harness-repo-split.plan.md`; `HARNESS-LEDGER.md`; `100e2dd`'s commit body and all
three commit bodies in `D:/do-the-work`; the full diffs of both changed files and of `f7966c4`.

**Sampled**: `HARNESS-DECISIONS.md` — the `§live` / `§implemented` heading map plus `HD-1`–`HD-8`
end to end and `HD-4`'s admission rule specifically, not the whole file; `HARNESS-RIDERS.md` by grep
for `E9`; `EXECUTION.md` by grep for the battery enumeration; `D:/Thesis/.git/hooks/pre-commit` by
grep for its check invocations.

**Probed, not read**: the 259 travelled files — compared by blob id, which is stronger than reading,
and not read; the caller's 1749 tracked paths, likewise; the 29 C exceptions — parsed as names and
existence-checked at the revision, contents not read.

**Executed**: the six battery legs and `repo-audit` at the tip; in a throwaway clone of the new
repository, its full suite three times (tip, tip grouped by failure cause, and `8cd0b9c`), the two
A10 test files at both revisions, a skip census, `test_precommit_checks`, and the `LAYER` resolution
probe; the membership derivation and the two-repository blob comparison; every count in §3.

**Ceilings.**
- The new-repository measurements were taken in a **clone**, to leave the subject worktree
  untouched. I verified the clone's 260 blobs equal the source's before using it. `RS_ROOT` /
  `REPO_ROOT` resolve by depth *within* the repository, not by its absolute location, so the
  different path string is not read by anything I exercised — but as before the equivalence is
  argued, not proved, and the exact reproduction of 24/677 and 20/681 is corroboration rather than
  proof.
- I did not mutation-test any guard this round. The two path guards were proved binding by the
  previous VERIFY on the claim the `B-1` repair turns on; this leg does not touch them, and `R4`
  bars re-certification. The `LAYER`/42-passed checks above show only that A10's five new files did
  not disturb them.
- The user's 「甲 + 花」 ruling is visible only as executor prose in the commit body, the plan and
  the manifest. `R7`: ceiling stated, nothing in the repository contradicts it. Whether the second
  fix leg was classified by the user in those words is **`UNVERIFIABLE`** from my side; that the
  leg exists and is past the cap is not.
- Whether `.harness/review-pending.json` was written by a real `rsc v3 dispatch` invocation is a
  process claim: contents verified, the command **`UNVERIFIABLE`**.
- `E9`'s "the branch takes no commit but the record" is verified as of this read and cannot be
  verified for the interval after I stop.
- **Not concluded, by `R5`**: whether the three caller-coupled governance tests should be excluded,
  re-pointed or left red in the new repository (the round routed it to R2 and I agree it is not
  this leg's to settle); whether the remaining 96 files of `tooling/tests/fixtures/` have any claim
  on the travel set — none is read by a travelled test today, which is a fact about today's tests,
  not a membership ruling; and `O-4`'s question.

---

## 8. What holds

The A10 supplement is right, and right for the stated reason. The manifest's rules, applied
mechanically at `e4ffa2b` by a script that never reads the file's own totals, yield 259 paths, and
the new repository contains those 259 and nothing else, each byte-identical to the caller. Its
sub-counts re-derive one by one — A 113, B 3, C 94 + 49 — and the C reproduction record checks out at
both revisions it cites. The suite moved 24/677 → 20/681 exactly as claimed, the four cleared tests
are exactly the two A10 files, the surviving 20 split 15 / 2 / 3 exactly as the README now prints,
and nothing in that suite is skipped. `F-1`'s honesty repair says more than the minimum fix asked
and stops where `R5` says to stop; `F-2`'s hook asymmetry is true in every particular I could
measure; `F-3` leaves no mislabelled revision behind; `F-4` now cites the finding that exists.
`E2`'s frozen bytes are untouched in both repositories, `E10`'s nine members took no write and remain
in sync across them, `E8` holds on both commits, and the battery is six-for-six green at the tip with
every tally reproducing exactly. What the leg gets wrong is the count of its own cost.
