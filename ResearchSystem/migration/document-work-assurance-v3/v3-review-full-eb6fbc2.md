# FULL review — split batch R3, `f9786a8..eb6fbc2`

**Verdict: `CHANGES_REQUIRED`.**

Two blockers. Neither is in the wiring. The wiring is sound and I proved it rather than read it:
the gitlink resolves to a commit that is on the new repository's `origin/main`, all nine
instruction-layer members and all three relocated guards are byte-identical between the caller
and the pin, the tracked hook is mode `100755` and `git` itself resolves and runs it, and each of
the three guards fires from the submodule on a real defect and stays silent on a negative
control. The `SUBMODULES` exclusion is must-fire under mutation, reproducing the executor's
figures exactly. The six-command battery is green at the range tip, not at an earlier commit.

Both blockers are in what the round **wrote down about its own measurements**, and they are one
defect class: an empirical enumeration narrower than the command that would falsify it — the
class `HD-41` exists for. The round says it swept that class and confirmed zero residuals; the
sweep instrument it names (the candidate path checker) reads staged Markdown only, and the
surviving residual is in a `.py` comment, where it is the sole recorded justification for the
shape of the change this round makes. The second is the enumeration that ruling ② rests on:
the two sites it names are four and five, and the under-count is what a later round will size
step 19 from.

**Findings: 2 blockers, 4 low, 5 observations.**

---

## 1. Subject, re-derived

Everything below is re-derived from the repository. No reported figure was accepted (`R2`).

| | |
|---|---|
| Range | `f9786a8fe7359ca77b865b903a351b3ae4b2e4fe..eb6fbc21d8a38fe7a955ebe5fbe0b078fa3d1885` |
| Branch / worktree | `document-work-assurance-v3` at `D:/Thesis-stage-control-refactor`; `HEAD` == range tip. `git status --porcelain` empty at entry and at exit |
| Commits | 2, linear, author-date == committer-date on both (no amend or rebase evidence). `a14d203` `V3-SPLIT-R3-WIRING-v1` 2026-08-16 23:37:21 +1000, parent `f9786a8`, Kind: candidate · `eb6fbc2` `V3-SPLIT-R3-POINTER-v1` 23:38:50 +1000, parent `a14d203`, Kind: ledger/riders-only |
| Paths | 8: **3 A**, **5 M**, 0 D. Classified by hand below |
| Freeze marker | `.harness/review-pending.json` names this exact range, `dispatched_at 2026-08-16T13:42:51+00:00`. The tip commits at 13:38:50 UTC, i.e. dispatch 4m01s after the last commit, and the branch has taken no commit since. `E9`'s "from dispatch to that commit the branch takes no commit but the record itself" holds |
| Round | Split batch **R3**, caller-side wiring, per `.goals/plans/harness-repo-split.plan.md` (steps 18 / 18b / 20 marked done, 19 struck, 21 = this FULL) |
| Budget (`E9`) | No record of any family for this subject exists under `migration/document-work-assurance-v3/`: no `*eb6fbc2*`, no `*a14d203*`, no `*f9786a8*`, and no file mentioning `SPLIT-R3`. So no valid independent FULL has occurred, both commits are pre-submission corrections consuming nothing, and this is R3's one FULL. The fix leg and the targeted VERIFY are unspent |
| Authorization | `HD-18` (split is its own batch), `HD-10` / `HD-15` (split must happen, as a submodule), `HD-33` (gitlink pins the instrument; run dir, freeze marker and the four instance files stay with the caller), `HD-28` (membership), `HD-40` (`split-design.md` signed; R3 builds to §2 / §6 / §8), `HD-41` (scope discipline plus scan-class evidence), `HD-31` (accounting assurance moved caller-side). The three user rulings of 2026-08-16 exist in `a14d203`'s body and in the plan — committed, so not an `R2` chat-only finding. `E11`'s preview card for R3 is nowhere in the repository: `R7` ceiling, stated in §6, not a block |
| Push | 2 commits unpushed to `origin/document-work-assurance-v3`. `E8`'s "no push" holds |

Paths by hand, against the round's declared boundary (plan steps 18 / 18b / 20 plus their named
consequential edits):

```
A  .githooks/pre-commit                       +61      tracked hook; mode 100755 in the index
A  .gitmodules                                 +3      one entry, url https://github.com/Melclycj/do-the-work.git
A  ResearchSystem/harness                      +1      gitlink, mode 160000, f65dcf203cb0379e4d80bf445d3817def3a0d744
M  Thesis/Work/Tooling/repo-audit.py       +13 -5      SUBMODULES constant, excluded() clause, EXCLUDE header comment
M  ResearchSystem/HARNESS-POLICY.md        +30 -9      §3 rewritten, §4 made final
M  ResearchSystem/HARNESS-RIDERS.md         +1 -2      two rows deleted, one added
M  .goals/plans/harness-repo-split.plan.md +54 -6      steps 18/18b/20 closed, 19 struck, Resume pointer
M  ResearchSystem/HARNESS-LEDGER.md         +1 -1      split-batch pointer line (second commit)
```

Everything is inside the boundary, and the claim that carries the round — **zero bytes land in
the harness repository** — is true. The gitlink names `f65dcf2`, whose subject is the new
repository's own `.gitignore` commit recorded against plan step 17c, i.e. a commit that predates
R3; `git -C ResearchSystem/harness status --porcelain` is empty and `git -C ResearchSystem/harness
log --oneline -3` shows `f65dcf2` on top of `8e6f3cb` / `a97d578`, the R2 chain. R3 added no
commit there.

`E2` and `E10` are both untouched, checked rather than assumed: the contract blob is `b2dbdf75`
at base and at tip, supersession-1 `68031fa2`, supersession-2 `e1a2f26b`, and
`git diff --name-only f9786a8 eb6fbc2 -- ResearchSystem/schema/document-assurance-v3/` returns
zero paths against a pack of 15 tracked files. None of `E10`'s nine members appears in the range.

## 2. What I re-executed

All at the range tip, worktree clean, immediately before writing this (`E3`).

**The battery — six commands, all green, none accepted as reported.**

```
$ python ResearchSystem/tooling/tests/run_tests.py
tests: 29   passed: 29   failed: 0        RESULT: OK

$ python ResearchSystem/tooling/tests/run_p4_tests.py
tests: 80   passed: 80   failed: 0        RESULT: OK

$ python ResearchSystem/tooling/tests/run_p5a_tests.py
tests: 39   passed: 39   failed: 0        RESULT: OK

$ python ResearchSystem/schema/fixtures/validate_fixtures.py
cases: 58   matched: 58   unexpected: 0   RESULT: OK

$ cd ResearchSystem/tooling && python -m pytest -q
708 passed in 83.78s (0:01:23)

$ python ResearchSystem/tooling/rsc.py compile --check
RESULT: generated output fresh; lint clean (exit 0)
```

29 / 80 / 39 / 58 / 708 / fresh — the round's figures reproduce exactly, and the tier is right:
the range touches `Thesis/Work/Tooling/repo-audit.py` and adds a tracked hook, so the
tooling-touching branch of the tiering section applies and the doc-only exemption does not. The
`707 -> 708` attribution is also right for the reason that matters here: this range changes no
test file, so the delta is not R3's.

**The exclusion is must-fire under mutation.**

```
$ python Thesis/Work/Tooling/repo-audit.py          # as committed
scope: 496 markdown files under the checkout root
[OK] Broken markdown links: 0
[~~] Orphan notes (no inbound link): 250
RESULT: clean (exit 0)

# mutation: SUBMODULES = ()
$ python Thesis/Work/Tooling/repo-audit.py
scope: 643 markdown files under the checkout root
[!!] Broken markdown links: 15
[~~] Orphan notes (no inbound link): 357
RESULT: hard issues found (exit 1)

# restore from a sha256-checked scratchpad copy, never git checkout --
$ sha256sum Thesis/Work/Tooling/repo-audit.py
2346c2beb8601d2b8f3ce68fbc4eec361854d83581b62d9278feb8a060cee541
$ python Thesis/Work/Tooling/repo-audit.py > /dev/null; echo $?
0
$ git status --porcelain                            # empty
```

496 / 643, 0 / 15, 250 / 357, and the same restore digest `2346c2be…` the round records. The
clause is not inert, and it is correctly written: `excluded()` is called exactly once, at
`repo-audit.py:70`, with `p.relative_to(ROOT)`, so `as_posix()` yields a repository-relative
POSIX string and `startswith` on a tuple is the right test. An absolute path would have made the
clause silently dead; it is not.

**All three relocated guards fire from the submodule, each with a negative control** (`E4`,
`R8`). Baseline: hook on an empty index, exit 0. Then a real defect of the shape each guard
exists for — one unresolvable `ResearchSystem/`-rooted token added to the staged instruction-layer
member `document-harness/README.md`:

```
$ sh .githooks/pre-commit
...repo-audit clean (exit 0)...
pre-commit BLOCKED: a review/read is out (E9: ...)
  marker : ...\.harness\review-pending.json  (subject f9786a8...eb6fbc2)
  staged : ResearchSystem/document-harness/README.md  (not a review record)
exit 1                                    # review_freeze_check, from the submodule

$ python ResearchSystem/harness/.../hooks/layer_path_check.py
pre-commit BLOCKED: newly added instruction text names a repository path that does not resolve:
  ResearchSystem/document-harness/README.md: `ResearchSystem/no-such-file-zz9.md`
exit 1

$ python ResearchSystem/harness/.../hooks/candidate_path_check.py
pre-commit BLOCKED: newly written text names a repository path that exists nowhere:
  ResearchSystem/document-harness/README.md: `ResearchSystem/no-such-file-zz9.md`
exit 1

# negative control — same file, benign added line, no path token
layer_path_check  exit 0
candidate_path_check  exit 0

# restore
$ sha256sum ResearchSystem/document-harness/README.md
3833c63919c08fe0be994cea5346ec1c9176c3a86d4d37ff26959c42ab89dade
$ git status --porcelain                            # empty, index reset
```

The freeze guard blocking first is itself the proof that the chain runs in order and that it
resolves the caller's marker while living in the submodule. All three read the repository root
from the process cwd (`check(pathlib.Path.cwd())` in each `__main__`), which is why living under
the mount still guards **this** repository's staged paths, and
`candidate_path_check.py:52`'s `sys.path.insert(parents[1])` lands on the submodule's own
`ResearchSystem/tooling`, where `rsclib` is — the import resolves. The restore digest matches the
one the round records.

**`git` itself honours the tracked hook**, not just a manual `sh` invocation:

```
$ git --version
git version 2.48.1.windows.1
$ git hook run pre-commit          # runs .githooks/pre-commit, repo-audit output appears
RESULT: clean (exit 0)             exit 0
$ git ls-files -s .githooks/pre-commit
100755 024c1998... 0   .githooks/pre-commit
$ git config --show-origin --get core.hooksPath
file:D:/Thesis/.git/config      .githooks
```

Mode `100755` matters and is right: a tracked hook committed `100644` is skipped with a warning
on any POSIX clone, which would have made the whole "it travels now" claim hollow.

**Parity and reachability.**

```
$ git ls-files -s ResearchSystem/harness
160000 f65dcf203cb0379e4d80bf445d3817def3a0d744 0  ResearchSystem/harness
$ git submodule status
 f65dcf203cb0379e4d80bf445d3817def3a0d744 ResearchSystem/harness (heads/main)
$ git -C ResearchSystem/harness remote -v
origin  https://github.com/Melclycj/do-the-work.git   # == .gitmodules url
$ git -C ResearchSystem/harness branch -r --contains f65dcf2
  origin/main                                          # a clone can materialise the pin
```

Nine instruction-layer members, caller vs pin: **9 SAME, 0 DIFF** (`3af69265` `e5c205ac`
`9f80e728` `3350bfac` `17ff31bb` `b576a45e` `68031fa2` `e1a2f26b` `09aa8699`). Three guards:
`e6ce4941` / `468381fe` / `3e8a2b1e`, all SAME. `cli.py`: `e7308dc7` both sides. The round's
blob claims hold, and so does the `E10` citation discount: six members equal the blobs
`v3-checkpoint-read-f61ce2c.md` records in its own member table, three have moved since
(checklist and README by the one-token `rsc v3 dispatch` to `dtw dispatch` rename, `EXECUTION.md`
by `+16 -7` = the `HD-42` eight-to-six enumeration plus the stale-tallies correction).

**Bookkeeping.** `HARNESS-LEDGER.md` 120 lines at base and at tip, `ledger_cap_check.py` exit 0.
`HARNESS-RIDERS.md` 37 to 36 lines; rows 27 to 26. Both rider redemptions are real:
`cache-count`'s redeem-when named "the next batch touching `repo-audit.py`'s `EXCLUDE` or its
header comment" and this range touches both, and the byte fix it asked for (stop writing a
standing count) is applied; `ledger-assert`'s redeem-when named `HARNESS-POLICY.md` §4, which is
rewritten from "undecided, a todo not a terminus" to final, with the three reasons written out
and traceable to `split-design.md` §6's `已裁（用户 2026-08-14）`. I checked §6 and §2 in the
signed design and both rulings are there as cited, including §2's "落在 R3". The §4 reason ②
tally is right too: `chk-ledger-note` appears in exactly one of the eight run directories
(`p4-bridge`).

## 3. Blockers

### B-1 — `repo-audit.py:44-45` records, as the reason for the new exclusion's shape, a counterexample this same commit retracted twice elsewhere

**Location.** `Thesis/Work/Tooling/repo-audit.py:44-45`, added by `a14d203`:

> Path-scoped rather than a name in `EXCLUDE`, because `ResearchSystem/tooling/rsclib/harness/`
> must stay in scope.

**Ground truth it violates.** The directory holds nothing the audit could keep in scope:

```
$ git ls-files ResearchSystem/tooling/rsclib/harness/ | wc -l
0
$ ls -a ResearchSystem/tooling/rsclib/harness/
.  ..  __pycache__                     # no .md, so not in all_md either way
$ git ls-files | grep -cE '(^|/)harness(/|$)'
1                                      # only the gitlink
```

`HD-39` emptied that tree. So the stated reason is false twice over — nothing there is tracked,
and nothing there is Markdown, which is the only thing `EXCLUDE` can remove from this audit's
scope. `a14d203`'s own body says exactly this ("`HD-39` 早把它的 tracked 内容删光了…论证因此重写为
不依赖那个反例的版本"), and the plan's step 18 says it again. The general argument that replaced
it — a name in `EXCLUDE` matches by path part at any depth, present or future, while a path-scoped
tuple pins one mount — is sound, and it is the argument in the commit body and in the plan. It is
not the argument in the code.

The commit also asserts the class was swept: "第三次才对三个改动文件跑了完整扫描（即 checker 本身，
它扫的正是这个类）并确认零残留". The named instrument is `candidate_path_check.py`, whose
`scanned()` is `path.endswith(".md") and not path.startswith(NOT_SCANNED)` — staged Markdown only.
It cannot see a `.py` comment, so "zero residuals" is asserted at a scope the instrument does not
cover, which is `HD-41` ②, and no grep output is pasted, which is `HD-41` ④'s explicit
requirement ("把 grep 输出贴进 commit 正文"). `E3` names this shape directly: a characterization
no command established — *swept clean* — is dropped, not softened.

**The sweep, run.** The class is "the retracted `rsclib/harness` counterexample", over the
round's eight changed paths:

```
$ for f in <the 8 changed paths>; do printf '%-42s %s\n' "$f" "$(grep -c 'rsclib/harness' "$f")"; done
.githooks/pre-commit                       0
.gitmodules                                0
.goals/plans/harness-repo-split.plan.md    0
ResearchSystem/HARNESS-LEDGER.md           0
ResearchSystem/HARNESS-POLICY.md           0
ResearchSystem/HARNESS-RIDERS.md           0
Thesis/Work/Tooling/repo-audit.py          1
```

One residual, and it is the one site the named instrument structurally could not reach. (Tree-wide,
the other hits are historical records citing the directory for unrelated reasons; none of them is
this claim.)

**Why it is a blocker rather than a low.** It is not a stale figure recoverable from adjacent
text — it is the *recorded reason* for the design decision this round makes, and it is false. A
maintainer who does what a good maintainer does, checks the stated reason, finds it does not hold,
and the conclusion that invites is to collapse `SUBMODULES` back into `EXCLUDE` — the design this
round deliberately rejected. `E6`: when a finding names existing code as wrong, the fix is that
text changing.

**Minimum fix.** Replace the `because …` clause with the general reason already written in the
commit body and the plan: a name in `EXCLUDE` is matched against every path part at any depth, so
it would also exclude any directory of that name that appears later anywhere in the tree, while a
path-scoped prefix pins this one mount and stays enumerable. Do not substitute a different
example.

### B-2 — ruling ②'s enumeration is narrower than the tree: "two sites" is four scripts and five resolution points, and step 19 is now scoped from it

**Location.** `.goals/plans/harness-repo-split.plan.md:245-249` (step 19, rewritten by this
round) and the same sentence in `a14d203`'s body:

> 实测推翻了本步的排期假设：两处都已在 harness 仓——`rsclib/document_harness/cli.py`（R2 把六命令
> 连同 6 处 `--repo-root` parser 一并摘走）与 `assurance/templates/run-v2/run_evidence_v2.py:121`

**Ground truth it violates.** Both counts are wrong, and the second one under-scopes the work:

```
$ grep -c '"--repo-root"' ResearchSystem/tooling/rsclib/document_harness/cli.py
4                                  # parser sites; the args.repo_root resolution points are 5,
                                   # at :38 :75 :142 :324 :409 — neither number is 6

$ grep -n 'REPO = args.repo_root' ResearchSystem/assurance/templates/run-v2/*.py
run_bind_v2.py:170:    REPO = args.repo_root.resolve() if args.repo_root else run_dir.parents[3]
run_evidence_v2.py:121: REPO = args.repo_root.resolve() if args.repo_root else run_dir.parents[3]
run_repair.py:63:      REPO = args.repo_root.resolve() if args.repo_root else run_dir.parents[3]
run_retire.py:98:      REPO = args.repo_root.resolve() if args.repo_root else run_dir.parents[3]
```

`run_evidence_v2.py:121` is exactly right as a line number — it is the `parents[3]` depth
assumption `io-design` §7 names. It is wrong as an inventory: **four** run-v2 template scripts
carry that identical default, not one. This is `HD-41` ① (declare the range, then run a command
covering it) and `E7` (test the defect class, not the reported instance).

**What survives and what does not.** The *ruling* survives: every one of these sites is inside a
travel prefix, so doing step 19 in R3 would indeed have meant opening a construction round inside
the harness repository, and moving it out was right. What does not survive is the enumeration as
a work order. Step 19 is now a struck checkbox whose text is the only record of its scope, and it
is scheduled into the re-rooting round. A round sizing it from this text edits one file and leaves
three siblings carrying the identical defect — which is precisely how `M-2` and `M-1D`, the
incidents `HD-41` ④ was built from, went.

**Minimum fix.** Rewrite step 19's site list from command output: `cli.py`'s four
`add_argument("--repo-root")` parser sites and five `args.repo_root` resolution points, and all
four run-v2 template scripts with their line numbers, noting that all of them sit in travel
prefixes so the ruling is unchanged.

### Both blockers are one class, and the fix should be swept as one

They are the same defect: an assertion whose scope exceeds the command behind it. `L-2` below is
a third instance. `HD-36` extends the must-fix channel to the same fix at every other site of the
named class, and `HD-41` ④ requires the grep output in the commit body — so the repair should
carry a scope-declared sweep of this range's records for empirical enumerations, with the output
pasted, rather than three point edits.

## 4. Low

- **`L-1` — the mutation's 15 broken links are characterized by a target set that covers 12 of
  them.** `a14d203`'s body: "断链 15（全部落在 `ResearchSystem\harness\` 内、指向调用者仓的 plans 与
  `assurance/shadow/`，即跨仓后本来就该断的那类）". All 15 are indeed inside the mount, but three
  point at review records, not plans or shadow:
  `v3-review-full-c6d4eb4.md` to `v3-review-full-0439efe.md` and to `v3-review-verify-d55d5ce.md`,
  and `W2/W2-design.md` to `v3-cold-read-e90243a.md`. Those three targets are among the 29 records
  that `split-travel-manifest.md` §C deliberately leaves with the caller
  (`comm` over the two indexes returns exactly 29, matching the manifest's rule). The conclusion
  — the class that should break after the split — holds for all 15; the enumeration of what they
  point at does not. Same class as the blockers, but nothing downstream turns on it.
- **`L-2` — the rider tally is 25, measured 26.** `bank 37→35→36 行（删 2 加 1，25 条 rider）`. The
  line arithmetic is right; the row count is not: `awk 'NR>10 && /^\| /' | wc -l` returns 27 at
  base and 26 at tip, and the 26 ids enumerate cleanly ending in `submod-index`. R4 step 22
  reconciles riders row by row rather than by total, so nothing breaks — but it is the third
  instance of the class in the same range.
- **`L-3` — ③'s reason for deferring the instruction-layer read is not the reason that carries
  it.** The round defers the independent read owed on the three changed members, arguing it did
  not rely on them because it "不动用 tiering 节去省档". But the branch it *did* use is the same
  section's second bullet, and that bullet is what the `HD-42` amendment changed: `these eight
  commands` to `these six commands and nothing fewer`. That is a rule-changing replacement, so
  `E10`'s deferral channel — open only to an amendment that changes what no rule requires — does
  not cover it, and `HD-42` itself records the layer read as still owed. What actually makes the
  deferral harmless is a fact the round does not state: `HD-39` deleted both struck runners' trees
  in the same commit, so the runnable battery is the same six under either text, and the
  verification performed is not in doubt (I ran it). The debt riding forward is correct; the
  stated ground for it is not. The checklist and README changes, being a one-token command rename
  that changes what no rule requires, do sit squarely in the deferral channel.
- **`L-4` — the signed design still routes this through `EXCLUDE`.** `split-design.md` §2's
  proposal reads "**`EXCLUDE` 新增 submodule 目录**", and `HD-40` makes the ten sections the
  execution basis for R1 through R4. The implementation chose a separate path-scoped constant
  instead — better, and disclosed in both the commit body and the plan — but the signed text now
  describes a route not taken, with no marker, and `HD-40` says substantive edits to that file owe
  a re-signature, so it cannot simply be corrected in passing. Anyone later reconciling
  implementation against the signed design meets a mismatch whose resolution lives only in a
  commit body. Routing is the orchestrator's; I only note that the gap has no carrier today.

## 5. Observations

- **`O-1` — after re-rooting, all three guards go silently inert, and nothing carries that.**
  `.githooks/pre-commit` hard-codes `H=ResearchSystem/harness/ResearchSystem/tooling/hooks`, and
  each invocation is `-f`-guarded, so a path that stops resolving is skipped without a word. The
  re-rooting round is scheduled to drop the `ResearchSystem/` prefix inside the harness repository,
  at which point `$H` resolves nowhere and the caller loses all three guards silently — the exact
  failure mode `HARNESS-POLICY.md` §3 says those three lines are written down to prevent, except
  that the policy tells a human what *should* run and emits no signal when nothing does. The same
  round deletes the caller's own copies, after which `layer_path_check.LAYER`'s nine caller paths
  and `E10`'s membership sentence describe files that exist only under the mount. Rider
  `submod-index` has that round as its deadline but covers only the false-block half. Nothing in
  the range names the `$H` breakage or the `LAYER` one.
- **`O-2` — the hooksPath switch is repository-wide, and the stale predecessor is still on disk.**
  `core.hooksPath` is set in `D:/Thesis/.git/config`, which is shared across worktrees, and
  `.githooks/` is absent from `origin/main` (`git cat-file -e origin/main:.githooks/pre-commit`
  fails). So every other branch and worktree of that repository now commits with **no** hook at
  all, where before they ran the untracked one. The round discloses this in the hook header and in
  policy §3 and calls it a transition cost, which is fair. Two things it does not say: the loss is
  repository-wide rather than "other branches", and `D:/Thesis/.git/hooks/pre-commit` still exists,
  still contains the dead `contract_provenance_check` block, and would silently resume being the
  hook if `core.hooksPath` were ever unset.
- **`O-3` — a non-recursive clone loses three guards whose scripts are sitting in its own tree.**
  The caller still tracks `ResearchSystem/tooling/hooks/*.py` (ruling ①), but nothing invokes them
  any more; a clone without `--recursive` has the scripts and runs none of them, because the `-f`
  guards test the mount. Strictly weaker than the pre-R3 state for that case, and it resolves
  itself when the re-rooting round deletes the caller copies.
- **`O-4` — the two trees are identical at the pin, and nothing keeps them so.** Caller vs
  submodule: 9 of 9 instruction-layer members SAME, 3 of 3 guards SAME, `cli.py` SAME. That is
  worth recording as measured rather than assumed, and worth recording that it is a coincidence of
  timing: an `E10` amendment lands caller-side, and until a resync commit plus a gitlink bump the
  guards that run are the pin's, not the amended ones. `HD-34`'s discipline covers the reverse
  direction (do not edit harness content caller-side); this direction has no carrier.
- **`O-5` — the batch Acceptance line for the submodule entry point is not yet exercisable as
  written.** It asks for one `dtw.py status` and one `dtw.py dispatch` through the mount. The entry
  point does load and parse through the mount — `python ResearchSystem/harness/.../dtw.py --help`
  lists all six commands, `dispatch --help` shows `--subject | --range | --read`, so the PEP 420
  namespace import the travel manifest depends on holds across the mount — but `status` requires
  `--state`, which only a product run has, and a construction round has none. Whether that line
  should be reworded or discharged at R4 with the two halves separated is the user's call (`R5`).

## 6. Unverifiable, and ceilings

Stated, never folded into supported (`R4`).

- **`E11`'s preview card, and the three rulings of 2026-08-16 as approvals.** The rulings' content
  is committed in `a14d203`'s body, so it is in the repository; the card itself, and the user's
  approval of it, are not. `R7`: a ceiling, not a block. The ledger already carries this as open
  from R2's FULL and VERIFY.
- **"本 session end-to-end 真读" of the three changed members.** A process claim about a session I
  cannot inspect. Marked, not verified. What I *can* verify and did is the arithmetic it rests on:
  six blobs equal `f61ce2c`'s recorded ids, three do not.
- **`E8`'s "stage explicit paths, never `add -A`".** Not observable after the fact.
- **The three consecutive hook rejections during authoring**, and the negative control the round
  says it constructed. No artifact survives; I reproduced the guard behaviour independently instead
  (§2), which establishes the guards fire but says nothing about what happened during authoring.
- **Which entry point ran the dispatch that produced my marker.** The marker records subject and
  timestamp only, and both `dtw.py` copies exist. Unverifiable.
- **Mutation caveat.** Everything in §2 proves the guards and the exclusion have binding force. It
  does not prove that force is sufficient, and this FULL is not a certification of anything outside
  the range.

## 7. Coverage

**Read in full:** `CONSTRUCTION-CHECKLIST.md`, the review-contract stub, `HARNESS-LEDGER.md`,
`HARNESS-DECISIONS.md` (including all 11 `§live` entries), `HARNESS-POLICY.md`, `.githooks/pre-commit`,
`repo-audit.py`, `rsclib/document_harness/paths.py`, `candidate_path_check.py`,
`review_freeze_check.py`, `.gitmodules`, `.harness/review-pending.json`, the full diff of all 8
changed paths, and the complete rider table.

**Sampled:** `EXECUTION.md` (the tiering section and its neighbours, plus the full diff since
`62c55e4b` — not end to end), `layer_path_check.py` (header, `LAYER`, `unresolved_tokens`),
`split-design.md` (§2, §6, and the section index), `split-travel-manifest.md` (rules, §A, §B, the
head of §C), the plan (its full diff plus R3 / R4 / Acceptance / Resume pointer — not the whole
file), `v3-checkpoint-read-f61ce2c.md` and `v3-cold-read-50c2b31.md` (member tables and citation
sections), `test_precommit_checks.py` (the `UNTRACKABLE` and scan-scope classes).

**Probed only:** the six battery legs, the `SUBMODULES` mutation and its restore, the three guard
must-fire and negative-control pairs, `git hook run`, blob parity across the two trees, `E2` blob
stability, the `--repo-root` and `rsclib/harness` sweeps, rider and ledger line counts, submodule
remote reachability, and the record-set difference between the two repositories.

**Worktree at exit:** `git status --porcelain` empty apart from this record, which is untracked
until the orchestrator commits it (`R6`).
