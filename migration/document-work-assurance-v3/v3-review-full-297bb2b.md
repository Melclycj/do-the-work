# FULL review — split batch R2, `4546835..297bb2b`

**Verdict: `CHANGES_REQUIRED`.**

Two blockers. Neither is in the move. The move is the cleanest thing in the range: I re-derived
both slice claims line by line and both are exactly true, the six commands answer through both
new names, the two rider redemptions are real and one of them is must-fire under mutation, and
the full battery reproduces at the tip rather than at the commit that measured it. Both blockers
are in what the round **wrote down about reaching outside itself**: the scan-class evidence for
"every `rsc v3` writing is rewritten" consists in part of two grep commands that cannot return a
non-zero count, and the one valid grep was scoped to a tree that excludes this batch's own plan —
where the batch's Acceptance still tells R3/R4 to run a command this round deleted. Separately,
the ledger's split-batch line still says R2 has not opened.

Findings: 2 blockers, 3 low, 5 observations.

---

## 1. Subject, re-derived

Everything here is re-derived from the repository; nothing was accepted as reported (`R2`).

| | |
|---|---|
| Range | `454683508741f077e192b8be756daf47dcbfe12c..297bb2befb3effa0784e3d3bded973ff530f8d40` |
| Branch / worktree | `document-work-assurance-v3` @ `D:/Thesis-stage-control-refactor`; `HEAD` == range tip. `git status --porcelain` at entry: empty. At exit: one line, `.claude/settings.local.json`, written by my own session's permission approvals — see §6 |
| Commits | 3, all author-date == committer-date (no amend/rebase evidence): `0643229` `V3-SPLIT-R2-CLI-EXTRACTION-v1` 17:21:09 +1000 · `8d137da` `V3-SPLIT-R2-LAYER-COMMAND-NAME-v1` 17:21:42 · `297bb2b` `V3-SPLIT-R2-PLAN-v1` 17:23:32 |
| Base | `4546835` `V3-SPLIT-R2-CHORE-SETTINGS-v1`, 17:08:11, declared out of boundary in its own body (caller tool config). Excluding it is right under `E8` and it is disclosed, so the boundary claim holds |
| Freeze marker | `.harness/review-pending.json` names this exact range, `dispatched_at 2026-08-16T07:23:57+00:00`; the tip commits at `07:23:32Z`, i.e. dispatch 25s after the last commit. `E9`'s "from dispatch to that commit the branch takes no commit but the record" holds so far |
| Paths | 23: **4 A**, **19 M**, 0 D — classified by hand below |
| Round | Split batch **R2** (construction: lift the CLI), per `.goals/plans/harness-repo-split.plan.md`. Steps 15/16 claimed landed, step 17 open on this FULL |
| Budget (`E9`) | No prior FULL or VERIFY record exists for this subject: over `migration/document-work-assurance-v3/`, no `*297bb2b*`, no `*4546835*`, no `*0643229*`, no `SPLIT-R2` record of any family. So every commit in the range is a pre-submission correction consuming nothing, and this is R2's one FULL. The fix leg and the targeted VERIFY are unspent. `8d137da` is an `E10` free-channel layer application, which `E9` says is not a round and consumes nothing |
| Authorization | `HD-40` (`split-design.md` signed; §1 is R2's build order), `HD-28`/`HD-33` (membership), `HD-34` (no caller-side shim), `HD-38` (free-channel bytes get their own commit), `HD-41` (scope discipline + scan-class evidence), `HD-36` (channel test). The 甲 ruling of 2026-08-16 — CLI only, no re-rooting — exists in `0643229`'s and `297bb2b`'s bodies and in the plan; chat in origin but committed, so not an `R2` chat-only finding. `E11`'s preview card for R2 is nowhere in the repository: `R7`, stated as a ceiling, not a block |
| Out-of-repo | `D:/do-the-work` @ `a97d578`, 260 tracked, clean. Two commits beyond the chain the plan's R1 account records. Measured in §5 O-3; nothing in this range changes it |

Paths by hand, against the round's declared boundary (`split-design.md` §1 = lift the six v3
commands into the instrument's own entry; plus the two rider redemptions the plan names):

```
A  ResearchSystem/tooling/rsclib/document_harness/cli.py        552  the six command bodies + parser
A  ResearchSystem/tooling/do-the-work.py                          21  shim
A  ResearchSystem/tooling/dtw.py                                  19  shim (short alias)
A  ResearchSystem/tooling/tests/document_harness/test_cli_entry.py 90  the new guard
M  ResearchSystem/tooling/rsc.py                            685->164  the lift, caller side
M  .../document_harness/paths.py                                 +1/-2  riders qp-index, qp-inert
M  .../tests/document_harness/test_precommit_checks.py            +17  qp-index negative control
M  .../tests/document_harness/test_candidate_checks.py         +14/-7  drop the caller-tree fixture
M  .../tests/document_harness_review/{test_dispatch_freeze_marker,
       test_fix_round_locks,test_review_cli_v2_subject}.py            drive the new entry
M  ResearchSystem/HARNESS-RIDERS.md                             -2 rows, 1 rewritten
M  ResearchSystem/document-harness/split-travel-manifest.md      A-row for the two shims
M  ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md     E12 command name   (8d137da)
M  ResearchSystem/document-harness/README.md                     :34 command name   (8d137da)
M  ResearchSystem/{HARNESS-POLICY.md,README.md,tooling/README.md}        command name
M  ResearchSystem/assurance/templates/run-v2/{README.md,run_evidence_v2.py,
       run_repair.py}                                                    command name, prose only
M  ResearchSystem/tooling/hooks/review_freeze_check.py                   command name, docstring
M  .goals/plans/harness-repo-split.plan.md                              (297bb2b)
```

Every path is inside the declared boundary. Nothing in the range touches `E2`'s frozen surface:
`Document-Work-Assurance-Contract-v3.md` `b2dbdf75`, `-supersession-1.md` `68031fa2`,
`-supersession-2.md` `e1a2f26b` are blob-identical at base and tip, and
`git diff --name-only 4546835 297bb2b -- ResearchSystem/schema/document-assurance-v3/` returns
zero lines. `8d137da` writes two `E10` members, neither of them `paragraph-map.schema.json`, so
`HD-20` does not bite.

---

## 2. The implementation (`R3`: this leads)

**The move is mechanical, and I checked it rather than believing it.** Both slice claims are
exactly true at the line level:

- function block — `rsc.py@4546835` lines 129–549 vs `cli.py@297bb2b` lines 25–445: 421 lines
  each, `diff` empty.
- parser block — `rsc.py@4546835` lines 586–670 with `s/\bv3_sub\b/sub/g` vs `cli.py` lines
  453–537: 85 lines each, `diff` empty.
- `wc -l`: `rsc.py` 685 -> 164. `rsc.py` at the tip contains no `v3`, no `_cmd_v3`, no
  `document_harness` (grep, whole file, zero hits), and its `main()` is byte-identical to the
  base's.

The one edit `cli.py`'s docstring does not enumerate is the subparser `dest`
(`v3_operation`/`mode` -> `operation`), which sits in the newly written seven-line preamble
rather than in the moved block. It is dead-safe: `git grep v3_operation` over
`ResearchSystem/tooling` returns zero readers. "The parser's own plumbing" covers it.

**Both names reach the same six operations, and a real command runs through them.** `--help` on
each shim prints the six; `python ResearchSystem/tooling/dtw.py governance-scan --path
ResearchSystem/contract/Document-Work-Assurance-Contract-v3.md` returns
`V3-GOVERNANCE-SELF-APPROVAL` and exit 1 — the lazy imports inside the moved bodies resolve
through the shims' `sys.path` insertion. The handoff that produced this review is itself the
proof for `dispatch`: the freeze marker names this range.

**Guards bind, mutation-tested by me** (neuter -> observe -> restore from sha256-checked
scratchpad copies; never `git checkout --`; baseline digests `241303ac` `cli.py` / `6c84c6a9`
`dtw.py` / `4157cae2` `paths.py`, all three verified `OK` after each restore — the same three the
executor cited, which corroborates their restore claim):

| mutation | result |
|---|---|
| delete the `flow` subparser registration from `cli.py` | **3 red** — `test_the_six_operations_are_the_ones_named`, `test_every_operation_binds_a_distinct_function`, `test_both_names_print_the_same_help`. Reproduces the executor's figure |
| `dtw.py` forked: own `main`, imports only `build_parser`, drops the UTF-8 reconfigure | **1 red** — `test_both_names_print_the_same_help`. Red only because the help text carries an em dash and this console is cp1252; see `L-1` |
| `dtw.py` forked: own `main` copied verbatim, reconfigure included | **all 5 green** — see `L-1` |
| remove `core.quotepath=off` from `TrackedPaths.from_index` | **1 red**, and it prints the real defect: `pre-commit BLOCKED: ... 'ResearchSystem/notes/'`. The rider's exact shape, not a crash (`R8`) |

`test_cli_entry.py`'s expectation is a hand-written literal tuple, not read back off
`build_parser()` — `E5` satisfied. `assertIs(func, getattr(cli, func.__name__))` additionally
pins each operation to a function defined in `cli.py` rather than merely to something callable.

**`qp-inert` deletion is correct.** `staged_added_lines` filters with
`line.startswith("+") and not line.startswith("+++")`, and `core.quotepath` only affects
pathnames, which appear only in the header lines that filter removes. Deleting rather than
binding it is the `E6` direction the rider itself preferred.

**The fixture narrowing in `test_candidate_checks.py` is sound and its stated compensation is
real.** `GovernanceRealDocumentTests` drops the caller-side plan and keeps the `E2`-frozen
contract, which travels. I verified the claim that the plan's shape stays covered rather than
taking it: `approval_status_owner` is asserted at `:1784`, `:1793` and `:1821` of the same file,
including the `assertNotIn(..., SELF_APPROVAL_FIELDS)` line that was removed from the real-document
test. Nothing was lost.

**Full battery, six legs, re-run by me at the tip `297bb2b`** (not at the commit that measured
them — see `L-3`):

```
run_tests.py            tests: 29   passed: 29   failed: 0        RESULT: OK
run_p4_tests.py         tests: 80   passed: 80   failed: 0        RESULT: OK
run_p5a_tests.py        tests: 39   passed: 39   failed: 0        RESULT: OK
validate_fixtures.py    cases: 58   matched: 58  unexpected: 0    RESULT: OK
python -m pytest -q     707 passed in 79.46s      (from ResearchSystem/tooling)
rsc.py compile --check  RESULT: generated output fresh; lint clean (exit 0)
```

707 is the reported figure and it reproduces; 701 + 5 CLI cases + 1 quotepath case = 707 checks
out arithmetically and against the diff.

---

## 3. Blockers

### `B-1` The scan-class evidence cannot fail, and the obligation it stands for is not discharged

**Where.** `0643229`'s body, the `HD-41` ④ 扫类留痕 block; consequence at
`.goals/plans/harness-repo-split.plan.md:203`.

**Ground truth.** `split-design.md` §1, signed under `HD-40`: 「既有文档里的 `rsc v3 <cmd>`
写法随之全部改写，落在 R2」. And `HD-41` ④: paste the grep output *so that whether it ran can be
seen by the reviewer on the spot*.

**What I measured.** The block pastes three commands. Two of them are `grep` basic regular
expressions containing `|`, which is a literal in BRE, so each searches for one impossible string
and returns 0 whether or not instances exist:

```
$ git grep '"rsc.py", "v3"|rsc\.py v3'          -> exit 1, zero lines
$ git grep -E '"rsc\.py", "v3"|rsc\.py v3'      -> 18 tracked lines

$ grep -c "_cmd_v3_|v3_sub" ResearchSystem/tooling/rsc.py                       -> 0
$ grep -cE "_cmd_v3_|v3_sub" ResearchSystem/tooling/rsc.py                      -> 0
  negative control, same two forms against a file that does contain both tokens:
$ grep -c  "_cmd_v3_|v3_sub" .../document_harness/cli.py                        -> 0
$ grep -cE "_cmd_v3_|v3_sub" .../document_harness/cli.py                        -> 19
```

The control settles it: the pasted form returns 0 on a file with 19 matching lines. The `rsc.py`
conclusion happens to be right — `-E` also gives 0 — but nothing in the record establishes it.
The other one is simply unrun: 18 tracked lines exist that its `-E` form finds.

The third command is a valid pattern, but its pathspec is `-- ResearchSystem`, i.e. narrower than
the obligation's 「既有文档」. Re-run repo-wide, the first live-surface casualty is **this
batch's own plan**:

```
.goals/plans/harness-repo-split.plan.md:203
  - 产品仓在**不改 harness 内容**的前提下能跑通一次 `rsc v3 status` / `dispatch`（`HD-34` …）
```

That is the batch's Acceptance — what R3 and R4 measure "done" against — and it names a command
this round deleted. It is not a stale mention in a closed record: `297bb2b` edited this very file
and left the line standing. Post-split the criterion is also substantively different, because
`HD-34` forbids a caller-side shim: the caller must reach the instrument through the submodule's
`dtw`, never through `rsc`, so the fix is not only a rename.

Two smaller facts belong to the same block. Re-running the valid sweep verbatim at the tip returns
**two** lines, not one: `split-design.md:54` as disclosed, plus `cli.py:14`. `cli.py:14` is a
correct historical sentence and should stay — but 「仅剩」 is an absolute quantifier (`HD-41` ②)
over an output that had two rows when it was written.

**Minimum fix.**
1. Rewrite `.goals/plans/harness-repo-split.plan.md:203` to the post-split invocation.
2. Re-run both alternation sweeps as `-E` (or as separate patterns) at a declared repo-wide-tracked
   scope minus the immutable record families, paste the real output, and give every remaining
   live-surface hit a disposition — rewrite, or "history, stays". The ones my re-run found, offered
   as the population to dispose of rather than as a list to edit blindly:
   `ResearchSystem/assurance/shadow/measure.py:147`, `shadow/round-2/measure.py:151`,
   `shadow/round-3/measure.py:156` and the three sibling `run_shadow.py` argv builders — these are
   **executable code** that invokes `rsc.py v3 …` and can no longer run;
   `.goals/plans/harness-deletion-first-stabilization.plan.md:22` and `:168`;
   `.goals/plans/research-agent-dev-p3corr-p4.plan.md:99` (its closing cold-resume how-to);
   `.goals/plans/harness-memory-lessons-integration.plan.md:42`;
   `Thesis/Work/Tooling/repo-audit.py:299`. Closed-run control JSON under `assurance/shadow/*/run-p3/`
   is immutable and wants no edit — only a stated disposition.
3. Correct the 「仅剩」 count where corrections for this round land.

### `B-2` The ledger's split-batch line says R2 has not opened

**Where.** `ResearchSystem/HARNESS-LEDGER.md:98`.

**What it says at the tip.** 「**R2 未开，且卡在一个未答的岔口**：只摘 CLI（甲）还是摘 CLI +
重扎根（乙）」.

**Both halves are false at the tip.** R2 is built and dispatched — `.harness/review-pending.json`
carries `4546835..297bb2b`, `dispatched_at 2026-08-16T07:23:57+00:00` — and the fork was ruled 甲
by the user on 2026-08-16, recorded in `0643229` and `297bb2b`. `297bb2b` deleted this exact
sentence from the plan's own status header and left the ledger's copy of it standing.

**Ground truth.** The file's own header: only two things belong here, and one of them is *the
current pointer*. The caller's `CLAUDE.md` names this file as the whole live pointer for the
harness track and tells a new session to read it first — so a cold session at this tip is told R2
is unopened and the fork unanswered, which is the one thing a pointer must not do.

**Why deferring buys nothing.** `HD-23` and the 2026-08-04 ruling make a ledger-only correction
free: it consumes no `E9` leg and owes no targeted VERIFY. The round already edited two caller-side
governance files in the same commit (`HARNESS-POLICY.md`, `HARNESS-RIDERS.md`), so the family was
in reach. And this is the second consecutive round in which this one line has carried a flat
falsehood: R1's 「执行零进度」 was found by two successive reviews and fixed at `022fac5`. `E7`
asks for the class, not the instance; the instance was fixed and the class recurred one round
later.

**Minimum fix.** One clause: replace the 「R2 未开…」 sentence with what is true at the tip — R2
built, 甲 ruled, FULL dispatched. The CLOSED transition still belongs to R4 and should not be
pre-written.

---

## 4. Low

### `L-1` The two-names guard cannot tell a shim from a fork, and its docstring says it can

`ResearchSystem/tooling/tests/document_harness/test_cli_entry.py:12-14` claims 「Nothing but a
comparison of what they actually print can tell a shim from a fork, and a fork is the drift that
ruling exists to prevent」. Mutation says otherwise: I replaced `dtw.py` with a fork that imports
only `build_parser` and carries its own copy of `main()` verbatim — no longer one entry under two
names, exactly the `HD-40` §10 drift — and **all five tests passed**.

The weaker fork (own `main`, reconfigure dropped) *is* caught, but the reason is incidental: the
help text carries an em dash, this console is cp1252, and the two stdout byte streams therefore
differ. On a UTF-8 console that mutation passes too.

So the property actually bound is "the two entries' help output currently agrees", not "one entry,
two names" — and the expectation for each entry is the other entry's output, which is the
dependence `E5` warns about. The claim is the defect, not the test: the test is useful.

Minimum fix, no machinery (`E6`): say what the comparison binds. If a binding is wanted instead,
one assertion does it — import both shims and assert `mod.main is cli.main`.

### `L-2` The `cli.py` sweep exemption cites a suite that does not drive the CLI

`ResearchSystem/tooling/tests/document_harness_review/test_fix_round_locks.py:330-331` justifies
adding `cli.py` to `SUCCESSOR_ROUND_MODULES` with 「the three suites that drive real commands
through it — `test_dispatch.py`, `test_dispatch_freeze_marker.py` and
`test_review_cli_v2_subject.py`」. `test_dispatch.py` drives nothing through the CLI: it contains
no `subprocess`, no reference to `dtw` or `cli`, and works in-process off
`from rsclib.document_harness import dispatch as D`. Two suites, not three.

This matters because the comment *is* the recorded warrant for an exemption, and the partition
above it says in as many words that a later module must not hide behind the precedent — it fails
until someone says which sweep covers it. The substantive compensation is real (`test_cli_entry.py`
plus two genuine subprocess suites), so this is the warrant being overstated, not absent.

The rest of the exemption checks out: `cli.py` originates no coded issue —
`named_codes()` scans for `CODE = "…"` / `f"{CODE}-…"` and `cli.py` has neither; its only `V3-`
tokens are one docstring reference, one `startswith("V3-SCHEMA-")` consumer test, and one comment.

### `L-3` The battery figure at the tip was measured two commits earlier, across a change the tiering section itself classifies as tooling-touching

`.goals/plans/harness-repo-split.plan.md:181` asserts the six-leg battery green as of `297bb2b`.
The measurement was taken on `0643229`'s tree and is recorded in `0643229`'s body. Between them,
`8d137da` modified `ResearchSystem/document-harness/README.md` — the file `EXECUTION.md:325`
names by path as the tiering exception, "a doc file that code enumerates or tests pin … treat the
batch as tooling-touching" — and `8d137da`'s body records no battery at all.

`E3` is explicit: re-run immediately before the claim. I re-ran all six at the tip and every figure
reproduces (§2), so the harm this time is zero and the finding is the discipline, not the number.

Worth noting for disposition rather than as a new problem: this is the file-versus-clause shape
rider `tier-file-vs-clause` already banks. The changed line is a command name inside a prose row,
and the test that pins that README pins schema stems, not that row — I checked. So the honest
reading is "the section says file, the executor read clause", which is that rider, not a fresh one.

---

## 5. Observations

**`O-1` — the `E10` classification of `8d137da` is right, and I was invited to overturn it.** I
do not. `E12` requires the handoff to be one commit SHA or range with no per-acceptance argument;
renaming the command in its parenthetical leaves that requirement identical, adds no clause, and
deletes nothing rule-changing. `README.md:34` is a descriptive clause in the Local-enforcement
row, same shape. Both facts `E10` demands are recorded in the body, including that the bytes ride
the next read of this layer. One tension I record rather than resolve: the carve-out also wants
the effect on every round in flight to be nil, and the round in flight is the one whose own
handoff uses the renamed command — but the obligation is met either way, `dtw dispatch` having
produced a range, so nil is the right reading. `HD-38`'s discipline is kept exactly: the
amendment commit carries the two layer members and nothing else.

**`O-2` — four of the six battery legs do not travel.** `tooling/tests/run_tests.py`,
`run_p4_tests.py`, `run_p5a_tests.py`, `schema/fixtures/validate_fixtures.py` and `rsc.py compile
--check` are all outside `split-travel-manifest.md`, while `EXECUTION.md` — which mandates "these
six commands and nothing fewer" — travels. The instrument's own repository therefore cannot
satisfy its own instruction layer's battery. This predates R2 (R1 created the repository; this
round changes neither side of it), and per `R5` whether it should be so is the user's question,
not mine. I report the shape because the round that just gave the instrument its own command line
is the round after which it starts to matter.

**`O-3` — the new repository, measured.** `D:/do-the-work` @ `a97d578`, 260 tracked, clean, two
commits (`001c01a`, `a97d578`) beyond the `345acdd -> 8cd0b9c -> f7966c4` chain the plan's R1
account records. Against the caller at this tip: 0 of its 260 paths are absent from the caller;
18 blobs differ — 14 are this round's own bytes, 1 is the repository's own README, and 3 are
pre-round divergence (`HARNESS-DECISIONS.md`, `HARNESS-DECISIONS-archive.md`,
`hooks/candidate_path_check.py`). The four files R2 creates are absent there. All of this is
consistent with the disclosed post-FULL resync. One imprecision in that disclosure: the pointer
calls the pre-round divergence 「5 个文件：三本治理登记 + `candidate_path_check.py` +
`test_precommit_checks.py`」, and measured it is 3 — `HARNESS-RIDERS.md` and
`test_precommit_checks.py` are in the set only because this round also touched them. The named set
is a superset, so nothing gets missed by resyncing to it.

**`O-4` — `rsclib/__init__.py` is an undeclared dependency of the entry R2 just built.** The
shims do `from rsclib.document_harness.cli import main`, and the travel prefix is
`tooling/rsclib/document_harness`, so `rsclib/` arrives in the new repository without its
`__init__.py` and works only as a PEP 420 namespace package. Nothing breaks today: over the five
travel prefixes, `from rsclib import` / `import rsclib` / `SCHEMA_VERSION` return zero hits, and
the new repository's pytest already imports the package this way. Recorded because the manifest
does not say so anywhere and the property is silent when it fails.

**`O-5` — `test_an_ascii_directory_holding_one_resolves` is labelled `# must fire` but asserts
exit 0.** It is the inverse shape — a false-positive regression test. Its force is real (it goes
red under the neutering mutation, reproduced in §2), so this is the label, not the test; but
`E4`'s "pair every must-fire test with a negative control" reads strangely against a must-fire
that must *not* fire, and the paired control directly above it exercises a different mechanism
(`scanned()`, not `from_index`).

---

## 6. What I read, and what I could not verify (`R4`)

**In full:** `CONSTRUCTION-CHECKLIST.md` (and the stub that names it); `HARNESS-DECISIONS.md`
§live and §implemented; `HARNESS-LEDGER.md`; `HARNESS-RIDERS.md`; `split-design.md`;
`split-travel-manifest.md`; `harness-repo-split.plan.md`; the three commit bodies; `cli.py`,
`do-the-work.py`, `dtw.py`, `rsc.py` at both ends, `test_cli_entry.py`, `test_readme_enumeration.py`,
and the whole diff of the range.

**Sampled:** `EXECUTION.md` (the tiering section and the battery enumeration; not the other 360
lines); `test_candidate_checks.py` and `test_precommit_checks.py` around the changed regions;
`test_fix_round_locks.py`'s `EveryNamedCodeIsAssertedSomewhere`; `paths.py` around both hunks.

**Probed only:** `REVIEW.md` and `io-design.md` — grepped, not read; `HARNESS-DECISIONS-archive.md`
— only to confirm that `HD-24`, `HD-39`, `HD-42`, `HD-43` exist, so that no live document cites a
decision id with no entry (`HD-1..HD-43` are all present across the two files).

**Executed:** all six battery legs at the tip; both shims' `--help`; one real `governance-scan`;
four mutations with sha256-checked restore; the sweeps of `B-1` including a negative control; the
blob comparison against `D:/do-the-work`.

**`UNVERIFIABLE`, not folded into supported:**

- `E11`'s preview card for R2. Nothing in the repository records one. `R7`: a ceiling, not a block.
- The claim in `297bb2b` that the new repository holds 「21 个 `.py` 含 110 处硬编码
  `ResearchSystem/`，两处 `parents[4]`」, which is the stated support for the 甲 ruling. It is a
  measurement of a tree outside every range; I did not re-derive it, and the ruling it supports is
  the user's in any case.
- Whether `8d137da` was preceded by a battery run. Its body records none; I established only that
  the figures reproduce at the tip, which is a different fact (`L-3`).
- Freshness of context. A process claim; marked, not verified.

**Worktree state on exit.** The four mutations were reverted from sha256-checked scratchpad copies,
never `git checkout --`, and `sha256sum -c` returns `OK` for all three touched files. One line
remains in `git status --porcelain`: `.claude/settings.local.json`, appended to by Claude Code as
my own session's Bash permissions were approved. It is the same caller tool-config file the base
commit `4546835` exists to keep out of the boundary, it is not mine to commit, and no harness byte
in the worktree differs from `297bb2b`.
