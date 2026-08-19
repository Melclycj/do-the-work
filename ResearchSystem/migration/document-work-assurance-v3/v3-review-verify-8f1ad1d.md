# Targeted VERIFY — round `LEDGER-SPLIT`, caller range `e74be07..8f1ad1d` (instrument `acbc553..b5fd58b`)

**Verdict: `REVIEWED_NO_BLOCKER`.** 0 blocker · 2 low · 3 observation.

---

## 0. Dispatch as received, and what I refused to take from it

One range — `e74be0764eccd8cbd8c29cec2216970d32f7f0a2..8f1ad1dcf6e6f0021de44ca691cff67740b0bdd7` —
plus the standing-contract pointer and one transport paragraph (Windows shell shape; where to
write this file, and that it is the orchestrator who commits it). No round name, no budget, no
authorization, no finding list, no statement that this is a VERIFY at all. Every one of those I
re-derived from the repository (`R2`); where a fact could only come from chat it is named as
such in §5 and folded into nothing (`R4`).

**Standing instructions read.**
`ResearchSystem/migration/document-work-assurance-v3/v3-harness-review-contract.md` — a stub,
which names `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` as both its successor
and its own counterpart, "read all of it": read in full, both sides, `E1`–`E12` and `R1`–`R10`.
Then, as the subject required: `ResearchSystem/HARNESS-DECISIONS.md` `§live` in full (HD-48,
HD-47, HD-44, HD-41, HD-36, HD-35, HD-34, HD-23, HD-9) plus the section index; `EXECUTION.md`
§*Regression-battery tiering* and §*Pre-freeze gate* in full; `document-harness/README.md`
`:31`/`:35`; `REVIEW.md` by grep; the instrument's `.githooks/pre-commit` in full;
`HARNESS-RIDERS.md` for the row this round rewrote and the four it cites; the caller's
`HARNESS-POLICY.md` §2/§4 and `HARNESS-LEDGER.md` in full; `io-design.md` §5;
`v3-review-full-e74be07.md` in full, because a VERIFY without the FULL's accepted findings has
no subject.

**What round this is, derived.** `8f1ad1d`'s title is `V3-LEDGER-SPLIT-FIX-CALLER-v1` and
`b5fd58b`'s is `V3-LEDGER-SPLIT-FIX-v1`; `v3-review-full-e74be07.md` is a `CHANGES_REQUIRED`
FULL over `7c54507..e74be07`, committed at `a960333` inside this very range. So a valid
independent FULL has occurred and this is the fix round's one targeted VERIFY (`E9`). Verdict
set is therefore `REVIEWED_NO_BLOCKER | SPEC_GAP` (`R3`).

## 1. Subject, re-derived

```
$ git -C D:/Thesis-stage-control-refactor rev-parse HEAD
8f1ad1dcf6e6f0021de44ca691cff67740b0bdd7

$ git -C D:/Thesis-stage-control-refactor status --porcelain --untracked-files=no
 M .claude/settings.local.json

$ git -C .../ResearchSystem/harness rev-parse HEAD
b5fd58b01e3ce2a3e62b5e6d6a790416d88631dc

$ git -C .../ResearchSystem/harness status --porcelain --untracked-files=all
(no output)
```

The instrument worktree is clean, so blob = working-tree file for every instrument measurement
below. The caller carries one modified path outside the subject. Both are falsified from the
moment this file is written, by exactly one path — this record, untracked until the
orchestrator commits it.

**The range carries two repositories.** One caller commit; its gitlink moves.

```
$ git diff e74be07 8f1ad1d -- ResearchSystem/harness
-Subproject commit acbc553ff2ab8971e0780f0ad0b317b91ca61c85
+Subproject commit b5fd58b01e3ce2a3e62b5e6d6a790416d88631dc

$ git -C .../harness log --oneline acbc553..b5fd58b
b5fd58b V3-LEDGER-SPLIT-FIX-v1
a960333 V3-REVIEW-RECORD-LEDGER-SPLIT-e74be07-v1
```

Three commits, twelve paths, classified by hand from `git diff --name-status` at both ends:

| repo | paths |
|---|---|
| caller (`8f1ad1d`) | `CLAUDE.md` · `AGENTS.md` · the gitlink — 3 |
| instrument (`b5fd58b`) | `CONSTRUCTION-LEDGER-archive.md` · `CONSTRUCTION-LEDGER.md` · `HARNESS-RIDERS.md` · 5 plan files — 8 |
| instrument (`a960333`) | `migration/…/v3-review-full-e74be07.md`, added, 493 lines — 1 |

**The review window held.** `.harness/review-pending.json` names exactly this range and
`2026-08-19T11:00:37+00:00`; the caller fix is committed `21:00:21 +1000` = `11:00:21Z`,
sixteen seconds before the window opened, and neither branch has taken a commit since. The
FULL's own window also held: dispatched `07:31:21Z`, record committed `a960333` at `07:50:13Z`,
and `git log` shows that commit alone in between on either side. `R4` ceiling unchanged from
the FULL: the instrument runs no `review_freeze_check` (its `.githooks/pre-commit` says so in
its own comment and I read the file), so on the instrument side nothing *made* the window hold.

## 2. The six accepted findings, checked one by one

The approved boundary is stated in `b5fd58b`'s body as "B-1 by prefix-strip plus L-1, L-2, L-3,
O-1 and O-2", approved 2026-08-19. That approval is not in either repository (`R7` — a hint,
never a block; see §5). What I can check is that the change set matches that description and
goes no further, and it does: every one of the twelve paths above is attributable to one of the
six, and nothing else is touched.

### 2.1 `B-1` — ten links: fixed, and the class genuinely swept

The fix strips the literal `../../ResearchSystem/harness/ResearchSystem/` to `../../` in ten
markdown links across five plan files. I did not read the executor's list; I measured the class
at both ends.

```
$ git grep -o -F -- "../../ResearchSystem/harness/ResearchSystem/" acbc553 | wc -l
10                                   ← whole repository, not just plans/
$ git grep -n -F -- "../../ResearchSystem/harness/ResearchSystem/" acbc553
(ten hits, all under ResearchSystem/document-harness/plans/, all in ](target) position)
$ git grep -n -F -- "ResearchSystem/harness/ResearchSystem/" b5fd58b -- .../plans
harness-repo-split.plan.md:236   ← prose inside a code span, `…/…/…` with an ellipsis, not a link
```

So the executor's "occurs exactly ten times" is right *and* its scope is right: the prefix
occurs nowhere else in the repository, so a plans-only sweep and a whole-repo sweep return the
same set. The one surviving token is a backticked sentence describing the mount, not a link.

Independent link resolution, my own resolver, with an escape guard (a `..` chain that leaves the
repository counts as unresolved, because it would land in the caller through the mount and
resolve there for the wrong reason):

```
16 files under document-harness/plans/, tip:        20 relative links, 0 unresolved, 0 escapes
whole ResearchSystem/ tree, base acbc553:           180 links, 30 unresolved
whole ResearchSystem/ tree, tip  b5fd58b:           184 links, 22 unresolved
```

30 → 22 is exactly the twelve this round fixed (ten plan links + archive `:559`/`:576`) minus
four *new* unresolved links that `a960333` introduced — all four inside
`v3-review-full-e74be07.md`, all four quotations of the defects it reports (`:248` quotes
README's `[plans/](plans/)`, `:280` quotes the dead `fef3a2e` link, `:303`/`:318` quote the
nested `L-2` construct). An immutable record quoting a broken path is the shape
`candidate_path_check`'s record carve-out exists for. **The repair introduces no new broken
link anywhere in either repository.**

Each of the seven distinct targets resolves, and to the same file it named before: from
`.goals/plans/`, `../../ResearchSystem/harness/ResearchSystem/X` was the instrument's
`ResearchSystem/X`; from `document-harness/plans/`, `../../X` is the same file. Display text
was left untouched in all ten and still matches.

**The ceiling stands.** Nothing in either repository would have caught this and nothing would
catch the next one: `repo-audit.py:48` excludes `ResearchSystem/harness/` by construction (read),
and the instrument's tracked hook runs `layer_path_check.py` alone (read in full), whose `LAYER`
is `E10`'s ten members. My resolver is the only link check that ran on this tree. Already banked
as rider `self-caller-guards`; not re-opened (`R5`).

### 2.2 `L-1` — the rider row: count independently reproduced, one sub-count still wrong

The row now claims 四处引用（三个不同目标）, measured over "十成员全文的 markdown 链接目标 +
反引号路径 token" with resolution meaning *lands inside this repository*. I ran that scope
myself over the ten `E10` members:

```
markdown links:                50 total,  1 unresolved  → REVIEW.md:45 → v3-review-full-fef3a2e.md
backticked ResearchSystem/ tokens: 43 total, 9 unresolved
backticked path-like tokens (any prefix): 38 total, 11 unresolved
```

Classifying the eleven by hand against the row: 3 in class (`EXECUTION.md:186`, `:449`, `:452`),
5 caller battery paths whose own sentence at `EXECUTION.md:342` disclaims resolution here, 2
`.harness/review-pending.json` runtime markers (`README.md:35`, `REVIEW.md:138` — line numbers
confirmed), 1 `<run-id>` placeholder (`:259`), and `supersession-1:89`, which is `E2`-frozen and
which rider `frozen-path-prefix` already holds. **1 link + 3 tokens = four occurrences over
three distinct targets. The row's headline reproduces exactly**, and every out-of-class shape it
names has a real destination — I opened `frozen-path-prefix` and it is there.

`ls` confirms `migration/document-work-assurance-v3/v3-review-full-fef3a2e.md` does not exist,
so `REVIEW.md:45` is genuinely dead. The partial-redemption claim also holds: grep for
`\.goals|HARNESS-LEDGER` over the ten members returns **zero** at the tip, so README's two
`.goals/plans/*` legs are paid and striking them from the enumeration is correct.

What did not survive the rewrite is `V-1` below: the row's closing clause still says 两处反引号
token while the row's own enumeration, three lines earlier, names three.

### 2.3 `L-2` — the nested link: exact bytes, mirror intact, class zero

Both files take the record's supplied replacement verbatim, and

```
$ diff <(sed -n '24p' CLAUDE.md) <(sed -n '24p' AGENTS.md)
(no output)
```

The mirror rule holds beyond that line too: a full `diff` of the two files returns only the four
expected name swaps (title, the Claude/Codex sentence, and the two self-references). Sweeping the
defect class rather than the reported instance (`E7`), `git grep -E '\[\[[^]]*\]\([^)]*\)\]\('`
returns **zero** in the caller and, in the instrument, only `v3-review-full-e74be07.md:303` —
the record quoting the defect. `repo-audit.py` runs clean at the tip (0 broken markdown links,
335 files), which was true before the fix too and is why it never covered this.

### 2.4 `L-3` — three figures corrected, and all three corrections reproduce

The erratum lives in `8f1ad1d`'s body, prose in the fix commit rather than an amendment to
`e74be07` (`E8` bars amending). All three:

```
1. $ git show 7c54507:ResearchSystem/HARNESS-LEDGER.md | grep -c ""
   113                                        ← not 120; 120 is HARNESS-POLICY.md:24's cap (read)
2. $ git grep -n -E '\]\([^)]*plans/(…the sixteen stems…)\.plan\.md\)' e74be07
   .goals/LEDGER-archive.md:76                (two links on this one line)
   .goals/plans/research-system-p5c-p8-revision.plan.md:51
   .goals/plans/research-system-stage-control-refactor.plan.md:20
   .goals/plans/research-system-stage-control-refactor.plan.md:608
   → three files, four lines, five links                        ← the erratum's exact claim
3. $ git grep -l -E '\.goals/plans/(…the sixteen stems…)' e74be07
   21 files = 14 under assurance/runs/ + 5 under migration/ + 2 under assurance/shadow/
```

14 + 5 + 2 = 21, and the shadow pair (`round-3/dispatch-prompt-run-{a1,p3}.md`) is the fourth
category the candidate's body omitted. Every figure reproduces at the revision named.

### 2.5 `O-1` — a declared bound, and no new machinery

`CONSTRUCTION-LEDGER.md`'s header gains a length rule: 180 lines, discipline only. The three
factual claims it rests on all reproduce — `ledger_cap_check.py:17` is `LEDGER =
"ResearchSystem/HARNESS-LEDGER.md"` and lives in the caller (read); the instrument's tracked hook
runs `layer_path_check.py` alone (read in full); this file is not an `E10` member (checked
against the membership sentence). `grep -c ""` returns **148** at the tip and **130** at
`acbc553`, so the body's "148 against 180" is measured at the declaring commit, and the struck
first figure of 150 is honestly recorded as struck. `io-design.md` §5 does say a ledger's
parameters and its cap script are the caller's, and `HARNESS-POLICY.md` §4 does make the same
`E6` refusal for the same reason — both read, both cited accurately. No second checker was
added, which is the right call and the one `E6` names.

### 2.6 `O-2` — two links, and the first licensed divergence

`:559`/`:576` lose the `harness/` mount segment and now resolve; both are absent from my tip
broken-link list and present in my base one. The provenance claim is exact:

```
$ git -C <instrument> rev-parse acbc553:ResearchSystem/CONSTRUCTION-LEDGER-archive.md
50d3e66edcadd4de553b1349d9a1c29abb32f02d
$ git -C <caller>     rev-parse 7c54507:ResearchSystem/HARNESS-LEDGER-archive.md
50d3e66edcadd4de553b1349d9a1c29abb32f02d
```

so identity to the source blob stays checkable forever at two immutable commits, and the header
restates its own byte-identity claim as identity-*at-`acbc553`* with the divergence named — the
unqualified form the fix had just made false. `git grep` finds no other surface still asserting
unqualified byte-identity for this file. `E2` is untouched: `git diff --stat acbc553 b5fd58b --
ResearchSystem/contract ResearchSystem/schema ResearchSystem/HARNESS-DECISIONS.md` is empty.

One thing to hand the user rather than to conclude (`R5`): the FULL's `O-2` said in terms "I am
not asking for them to change", and the round changed them under an approval that named `O-2`.
The result is defensible and disclosed; the ceiling is that I cannot see the approval that
turned an explicitly non-request into an edit.

### 2.7 `O-3` — disclosed as held back, and still false

All three surfaces the FULL reported are unchanged at the tip: `HD-28:275` still reads
`HARNESS-LEDGER.md` 与 `HARNESS-LEDGER-archive.md` 留调用者仓; `split-travel-manifest.md:75`
and `:127` still assign both to the caller; `.goals/LEDGER.md:24` still routes 未结项、开着的裁
决与 rider to the caller ledger, which holds none. `b5fd58b` states they stay false until the
closeout that owns them, and they do. Reported as state, not intent.

## 3. The rest of the repair diff

Everything in the twelve paths is attributable to one of the six findings; nothing is out of
boundary. Two paths carry more than the minimum, both disclosed:

- `HARNESS-RIDERS.md` — beyond striking the two paid legs and restating the figure, the row
  gains a measurement-scope declaration, an out-of-class enumeration, and a rewritten
  redeem-when. The additions are inside `L-1`'s surface and defensible (`R10` wants a row to name
  its target files, and the new redeem-when names `REVIEW.md` / `EXECUTION.md` where the old one
  named a table that has since been touched). The row is now long enough that `R10`'s "no
  narrative — the source records hold it" is under visible strain; I record the shape and do not
  file it, because the added text is what stops the next re-measure re-litigating the same eleven
  tokens I had to classify by hand in §2.2.
- `CONSTRUCTION-LEDGER.md` — the `O-1` bound and the `O-2` restatement land in the same header.

The instrument's tier call is right: eight markdown paths, none added, removed or renamed,
`document-harness/README.md` and the layer members untouched, so doc-only under
§*Regression-battery tiering*'s path-not-prose clause. The caller's is right too — the gitlink
moves, and the section's own sentence says a caller-side batch carrying a bump is never
doc-only. Both claimed batteries re-run here at the tip:

```
$ python ResearchSystem/tooling/tests/run_tests.py           tests: 29   passed: 29   failed: 0
$ python ResearchSystem/tooling/tests/run_p4_tests.py        tests: 80   passed: 80   failed: 0
$ python ResearchSystem/tooling/tests/run_p5a_tests.py       tests: 39   passed: 39   failed: 0
$ python ResearchSystem/schema/fixtures/validate_fixtures.py cases: 58   matched: 58
$ python ResearchSystem/tooling/rsc.py compile --check       RESULT: … (exit 0)
$ python Thesis/Work/Tooling/repo-audit.py                   RESULT: clean (exit 0)
$ cd ResearchSystem/tooling && python -m pytest -q           733 passed in 90.38s
```

Every claimed figure reproduces, including the instrument's 733.

## 4. Findings

### `V-1` (low) — `layer-outbound-refs` says 两处反引号 token where its own enumeration names three

**Location.** `ResearchSystem/HARNESS-RIDERS.md`, row `layer-outbound-refs`, closing clause of
the *what* column: `；两处反引号 token 早于本轮。`

**Ground truth.** The same row, three lines earlier, enumerates `EXECUTION.md:186` 与 `:449`
两处 … audit-rounds token · `EXECUTION.md:452` 一处 … issue JSON — three token occurrences, and
`四处引用` = 1 markdown link + 3 tokens. The row uses 处 as *occurrence* throughout (`余下一处是
markdown 链接`), so 两处 cannot be read as *two distinct targets* without contradicting the row's
own vocabulary. All three predate the round:
`git grep -c -E "assurance/runs/(p5a-shells/control/audit-rounds|p4-doc/issues)" 7701f03 --
ResearchSystem/document-harness/EXECUTION.md` → `3`.

**Why it is worth a line.** This is the defect `L-1` was: a rider row whose count and whose
enumeration disagree. The repair fixed the headline (六 → 四, correctly) and carried the stale
sub-count through — the clause was 两处 in the old row too, where it was already wrong against
the same three sites. A reader redeeming this row re-measures against 3+1, finds four, and meets
a sentence saying two.

**Minimum fix — exact bytes.** In that clause, `两处反引号 token 早于本轮` → `三处反引号 token
早于本轮`. Riders-only under the 2026-08-04 typing, so it costs no leg.

### `V-2` (low) — the licensing test that fixed the archive's two links was applied to the archive only

**Location.** `ResearchSystem/document-harness/journal/batch-a1-2026-08-08.md:8` →
`../../../.goals/plans/harness-record-layer-and-repo-split.plan.md`, and
`ResearchSystem/document-harness/journal/batch-b-2026-08-11.md:4` →
`../../../.goals/plans/harness-batch-b.plan.md`.

**Ground truth.** `b5fd58b`'s licensing test for `O-2` is "the record named a file of *this*
repository through the caller's mount, so strip the prefix and it resolves here". The body then
discloses three more sites that meet it — archive `:518`, `:544`, `:547` — and reserves them
for the user. Both journal links meet the same test and are named nowhere: their targets are two
of the sixteen plans that arrived in this repository this round, both now at
`../plans/<same-name>`, and `HD-23` puts journal corrections on the non-round route, so unlike
the signed and immutable surfaces there is no structural reason they were left out. My tip scan
also shows the shape in two files I am *not* reporting — `N3/N3-record.md:106` and
`v3-review-full-d532b3d.md:16` — because those are immutable records.

**No bytes supplied, deliberately.** Whether a history file's link target may be retargeted is
the decision the executor reserved for the user on `:518`/`:544`/`:547`, and these two belong to
the same decision, not to a sweep that pre-empts it. Route them together.

### `O-1` (observation) — `HD-41` ④ asks for the sweep's output; both fix commits give the number

`HD-41` ④ requires 把 grep 输出贴进 commit 正文, and says why in the ruling itself: 扫类是动作
不是自觉，贴证据是为了「跑没跑」可被评审员当场看见. `b5fd58b`'s body reports "occurs exactly ten
times across the sixteen plans", "21 relative links, 10 unresolved before, 0 after", "19
instrument targets, zero layer members, zero frozen" — figures with a declared scope, but no
command output and no per-site enumeration, so none of them is checkable without re-running.
I re-ran everything and it all holds (§2.1), which is the point: the discipline exists so that
this work is *confirmation* rather than *derivation*, and here it was derivation. The previous
fix commit `4029b43` read the same clause the other way in terms — "HD-41 clause 4 wants the
output rather than a number, so here it is" — and gave per-file breakdowns, so the standard is
this project's own and one round old. There is a real tension with `E8`'s single dense
paragraph, which is the user's to resolve if it is worth resolving.

### `O-2` (observation) — the FULL's §6 caveat rode `L-3` and the erratum did not carry it

The FULL's §6 recorded that `acbc553`'s `E10` deferral justification — "every changed token is a
location and its effect on rounds in flight is nil" — is contradicted one clause earlier by that
same body's disclosure that `README.md` "gains one navigation row naming the construction ledger
— an addition beyond the two named links", which carries prose, not a location. The FULL chose
not to file it separately: "It is the same absolute-quantifier shape as `L-3` and I count it
there rather than twice." `L-3` enumerates three figures and the erratum answers exactly those
three, so the caveat is uncorrected. The deferral's *outcome* is unaffected — no clause was added
to any rule and nothing in flight changed — only its stated reason is wrong, and it sits in an
immutable body where the only available fix is another erratum.

### `O-3` (observation) — the "21 relative links" figure counts a code span, and Windows hid it

`harness-deletion-first-stabilization.plan.md:65` contains the literal `` `](...)` `` inside a
code span — prose about editing link targets, not a link. A naive `\]\([^)]+\)` sweep counts it,
which is where 21 comes from; the real inline-link count in the sixteen plans is 20. It never
appeared as broken at either end because on Windows `Path('…/plans/...').resolve()` collapses to
`…/plans` and `exists()` returns `True` — I ran it to be sure rather than assume. Nothing turns
on it: 10 unresolved before and 0 after hold under either scope. Recorded so that a re-measure
on a POSIX host, where that path would *not* resolve, does not read the difference as a
regression.

## 5. Process and boundary check (run second, per `R3`)

| check | result |
|---|---|
| `E9` budget | Intact and now spent. One FULL (`a960333`, `CHANGES_REQUIRED`), one user-approved fix (`b5fd58b` + `8f1ad1d`, two repositories, one fix), this one targeted VERIFY. No commit in the range is a renamed round: `a960333` is the record of a FULL that had already occurred, and both fix commits name their kind in the first clause. |
| `E9` window (the FULL) | Dispatched `07:31:21Z`, record committed `07:50:13Z`, and `git log` over both repositories shows that commit alone in between. Held. |
| `E9` window (this VERIFY) | Marker names this exact range, opened `11:00:37Z`, sixteen seconds after `8f1ad1d`. Nothing since on either branch. Held so far. |
| `E2` | No write. Empty diff over `contract/`, `schema/` and the decision log across the repair range. |
| `E10` | No member touched by either fix commit — the eight instrument paths and the two caller files are all outside the ten. No amendment, so no amendment read owed; the round's opening cold read (`v3-cold-read-7701f03.md`) stands. |
| `E4` / `R8` | Not owed and not performed. The repair adds no guard; it changes ten link targets, two archive link targets, one rider row, one ledger header and two mirrored prose lines. `R8`'s live question here is the inverse — which guard *could* have caught `B-1` — and §2.1 answers it by reading both guards' own scopes. |
| `E6` | Respected, and visibly. `O-1`'s fix declares a bound in prose and argues against a second checker for a one-writer file rather than adding one; `B-1`'s fix is the ten links changing, not a rule about links. |
| `E7` | Met on `B-1` (whole-repository sweep for the literal, not the ten reported lines) and on `L-2` (nested-link grep across both repositories). Not met on `O-2`'s licensing test — that is `V-2`. |
| `E8` | Titles name the round and both bodies name the commit's kind in their first clause; single dense paragraph each (`grep -c '^$'` = 2, i.e. the title separator and the trailing newline); no trailers; nothing pushed (caller ahead 28, instrument ahead 35). |
| `E12` | One range, no per-acceptance argument. The marker's written tip is emitted by `dtw dispatch`, which the FULL already dispositioned as CLI display rather than a recorded range; the range it names is complete — `8f1ad1d` is the round's last commit and nothing was written after it. |
| `R6` | This file is `v3-review-verify-8f1ad1d.md` under `migration/document-work-assurance-v3/`, written in the instrument worktree and left uncommitted for the orchestrator. |
| `R1` (my side) | I was dispatched by the orchestrator over a committed range, prompted by the fixture-rendered prompt, scoped by the repository, and this record returns through the orchestrator. The executor holds none of the four. |

## 6. Disclosure — what I read in full, sampled, and only probed (`R4`)

**In full:** `CONSTRUCTION-CHECKLIST.md` (both sides); `v3-review-full-e74be07.md`;
`HARNESS-DECISIONS.md` `§live` + section index; the complete diffs of all twelve subject paths;
all three commit bodies plus `acbc553`'s and `4029b43`'s for calibration; the new
`CONSTRUCTION-LEDGER.md` header; the caller's `HARNESS-LEDGER.md`; `HARNESS-POLICY.md` §2/§4;
`EXECUTION.md` §*Regression-battery tiering* and §*Pre-freeze gate*; the instrument's
`.githooks/pre-commit`; `io-design.md` §5; the `layer-outbound-refs` row.

**Sampled:** `HARNESS-RIDERS.md` (all 34 rows by truncated first 220 characters, four read in
full); `document-harness/README.md` (`:31`, `:35`); `REVIEW.md` (grep + `:45`, `:138`);
`repo-audit.py` (`SUBMODULES` / `excluded` / the mount comment only); `ledger_cap_check.py`
(the `LEDGER` constant); `split-travel-manifest.md` (two lines); `.goals/LEDGER.md` (the harness
row).

**Probed by command only, not read:** the sixteen plans (link extraction and prefix counting
only — their content is unreviewed and unchanged apart from ten link targets);
`CONSTRUCTION-LEDGER-archive.md` (link extraction and blob identity only, 658 lines unread);
every other markdown file in the instrument's `ResearchSystem/` tree (link resolution only, 181
files at the tip and 179 at the base, the base extracted read-only with `git archive` into a
scratch directory rather than by creating a worktree).

**Not verified, marked (`R4`):** the fix boundary approved 2026-08-19 and its exact six items —
chat-only, `grep` for it returns nothing in either repository, and it is the one thing that
would let me check `E8`'s "stay inside the round's declared change boundary" against a written
boundary instead of against a description in the body it is meant to bind. Likewise the `E1`
disclosure (that the executor was the same orchestrator-dispatched subagent holding none of
`R1`'s four holdings), the "19 instrument targets, zero layer members, zero frozen" boundary
check, that the pre-commit hook actually fired on `8f1ad1d` (both repositories do have
`core.hooksPath=.githooks` set, so it could have; I re-ran the audit myself instead), and `E11`
— no preview card is in either repository, already a standing open item, noted and not
re-opened. `HD-48` still names a three-topic design round as the queue head and no committed
ruling reschedules it; that ceiling is unchanged from the FULL.

## 7. Verdict

**`REVIEWED_NO_BLOCKER`.**

Every one of the six accepted findings is answered, and answered at the level the FULL asked
for: `B-1` swept as a class over the whole repository rather than at the ten reported lines,
with the twelve fixed links and the four new record-quotation links accounting exactly for the
30 → 22 change in the tree's unresolved count and no new breakage anywhere; `L-1`'s
four-over-three re-derives from my own measurement of the declared scope; `L-2` takes the record's
bytes verbatim with the mirror intact and the class at zero; `L-3`'s three figures each
reproduce at the revision named; `O-1` declares a bound and refuses the checker `E6` would have
refused; `O-2` diverges from the archive's source blob for the first time, and does it licensed
and provenance-pinned rather than silently. Both tier calls are correct and all seven battery
commands reproduce.

`V-1` is a stale sub-count surviving inside the repair of a counting defect, and it has bytes.
`V-2` is the round's own new licensing test not swept past the file that provoked it, and it
belongs with the three sites the executor already reserved for the user. The three observations
are for the user: `O-1` that the evidence discipline this project bought a ruling for was met in
substance and not in form, `O-2` a caveat that fell between a finding and its erratum, `O-3` a
figure whose scope only reproduces on this operating system.

The one thing this round could not repair is the thing that let `B-1` happen: sixteen files now
live in a tree where no check can see a link, and the only link check that ran on them is the one
I wrote for this review.
