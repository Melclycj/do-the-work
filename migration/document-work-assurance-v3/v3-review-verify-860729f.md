# VERIFY — `ffe46e5..860729f`

**Verdict: `REVIEWED_NO_BLOCKER`.** Every accepted finding landed as the bytes its finding
supplied, and the whole repair diff holds against the permanent boundaries. This is not a
re-certification of the round (`R4`): it covers the repair and the boundaries, not the
candidate the FULL already reviewed.

**Findings: 1 low, 2 observations.** The low is the one thing the repair created rather than
inherited — `REVIEW.md` now reads the strict way and the frozen schema gloss it was quoted
against still reads the loose way, so two texts that agreed before this round disagree after
it, and nothing tracks the survivor.

Independence: this session was dispatched by the orchestrator with a range and nothing else,
derived round, budget, authorization and every number below from the repository, and reports
through the orchestrator. `R1`'s four holdings are the orchestrator's. That is a process claim
about *this* session and is not verifiable from the repository (`R4`); what is structural is
that nothing in the dispatch set the question.

---

## 1. What the subject is, derived

`git rev-list --count ffe46e5..860729f` → 1. The range is one commit.

| | |
|---|---|
| base | `ffe46e5baeae6bbce9691b80d15491540fb1507a` — `V3-REVIEW-RECORD-PRERUN-RIDERS-7cb7213-v1` |
| tip | `860729f9f7cbe58841b70cbfefc8e711881722ec` — `V3-PRERUN-RIDERS-FIX-v1` |
| kind, as the body names it (`E8`) | **review fix** |
| round | `PRERUN-RIDERS` |
| branch tip at review time | `860729f` — the dispatched tip, so the `E9` window has held |
| worktree | clean; `git status --porcelain --untracked-files=all` empty |
| freeze marker | `.harness/review-pending.json` carries this exact range, `dispatched_at` `2026-08-22T16:54:19+00:00` |
| push state | `main 860729f [origin/main: ahead 16]` — unpushed, as `E8` requires |

**Budget position, derived.** `v3-review-full-7cb7213.md` exists in
`migration/document-work-assurance-v3/`, committed at the base — **a valid independent FULL has
occurred**, so by `E9`'s own test the change under review is the round's one user-approved fix
and it obliges this VERIFY. No `v3-review-verify-*` record for `PRERUN-RIDERS` exists at the
subject; this is the first, and it closes the leg. The FULL returned `REVIEWED_NO_BLOCKER`, so
the fix is an `R10` late activation — which `E9` says is still the round's one fix and still
obliges the VERIFY. That is the configuration on the branch.

**What was authorized, derived.** `document-harness/plans/prerun-riders.plan.md` at
`6c5b039` carries the round's rulings and change surface. The fix package itself — the user's
all-in acceptance of `L-1`…`L-5` plus `O-3` on 2026-08-23, and the separate ruling keeping row
`io-hiroute-stale` — exists in the repository only as the commit body's own account of it.
Per `R7` this is a ceiling, not a block: **I cannot see either approval, and I do not treat
its absence as a defect.**

**Changed paths, classified by hand** (`git diff --numstat ffe46e5 860729f`, re-run here):

| path | + / − | class | inside the approved fix? |
|---|---|---|---|
| `document-harness/REVIEW.md` | 2 / 2 | `E10` member | yes — `L-3` |
| `document-harness/ORCHESTRATION.md` | 2 / 4 | `E10` member | yes — `L-4` |
| `HARNESS-DECISIONS.md` | 2 / 1 | decision log | yes — `L-5` |
| `HARNESS-RIDERS.md` | 1 / 2 | rider bank | `O-3` **plus two disclosed operations** — see §2.4 |
| `document-harness/journal/prerun-riders-2026-08-22.md` | 159 / 0 | round journal | yes — `L-1`/`L-2` errata, the carrier the package named |

Member blob ids at the tip: `31e785f8` · `7591c533` · `3908907a` · `c84b8288` · `9a67401f`.

**`E2`'s frozen bytes are untouched, verified by identity rather than by inspection.** The
three named blobs are byte-identical at base and tip — `b2dbdf75…`, `68031fa2…`,
`e1a2f26b…` — and the whole pack is one unchanged tree, `git rev-parse
{ffe46e5,860729f}:schema/document-assurance-v3` returning `1c33d26e…` both times, so all
fifteen files are covered by one comparison. `git diff --stat ffe46e5 860729f -- schema/
tooling/ contract/ migration/` is empty: no code, no schema, no contract, no record.
`E10`'s membership sentence is unedited, so no `E10-sync` is due.

---

## 2. Lead with the implementation

### 2.1 The accepted findings, each checked against the bytes its finding supplied

| finding | supplied bytes applied verbatim? | does it close the defect? |
|---|---|---|
| `L-3` | **yes** — `REVIEW.md:47`–`:48` now reads *"an issue recorded while the run is still in flight is unrepresentable"*, the reviewer's substitution, rewrapped and not paraphrased | **at the named site, yes** — see `V-1` for the sibling |
| `L-4` | **yes** — the em-dash gloss at `ORCHESTRATION.md:80`–`:82` is deleted and the remainder is the reviewer's sentence, rewrapped | yes |
| `L-5` | **yes** — `HARNESS-DECISIONS.md:291`–`:292` reads 当时的实际形态 with the appended dated note, exactly the two edits `L-5` specified | yes |
| `O-3` | **yes for the quotation** — `HARNESS-RIDERS.md:44` now carries 其**路由与 `observed_after` 窗口**… whole; the `:100` → `:99-100` citation widening is the executor's, disclosed in the journal's honesty boundaries and **correct** | yes |
| `L-1`, `L-2` | not appliable — carrier is an immutable commit body | errata landed; both re-derive, §2.2 |

**`L-4`'s deletion leaves one home, not none.** The bound survives at `EXECUTION.md:462` and
`:467`; class 2 below finds those two hits and nothing else, so `ORCHESTRATION.md`'s second
copy is gone and `HD-5`'s drift surface with it. The surviving sentence reads grammatically
and the pointer at `EXECUTION.md` resolves.

**`L-3`'s fix is the strict reading, and it is the reading the code already had.**
`issues.py:140`–`:141` raises on *"an issue **recorded** against a live run could influence the
run it is about"*, and the schema's own first sentence is *"the terminal status the run had
reached when this **was recorded**"*. `REVIEW.md` now agrees with both, and its after-the-run
route at `:50` is no longer barred by its own parenthetical. What the machine enforces is
only the `observed_after` enum and a terminal-status match (`issues.py:145`), so no code path
ever barred the route — the defect was always prose, and the prose at the named site is fixed.

**`L-5` is closed at the site rather than tracked, which is what `E6` asks.** Class 3 below,
run in both languages, finds no remaining site writing the merged form as current:
`ORCHESTRATION.md:26` `:31` `:114` and `CONSTRUCTION-CHECKLIST.md:39` are all exception-framed,
`HARNESS-DECISIONS.md:140` quotes `HD-55`'s own carrier, `:148` argues for separation, and
`HARNESS-RIDERS.md:20` is about two rounds reading a waiver differently. The residue the FULL
found untracked has no successor to track.

### 2.2 The errata, re-derived rather than read (`E3`)

Both figures the journal corrects reproduce exactly, and so do the journal's own new
measurements on the fixed tree.

| claim | re-run result |
|---|---|
| `L-1` — bank at `7cb7213` is 35 data rows, 32 citing, 3 not | **exact.** `grep -c '^\| '` → 36 = header + 35 data rows (the separator opens `\|-` and is not counted); 32 carry a `v3-{review-full,review-verify,checkpoint-read,cold-read}-<sha>` citation; the three that do not are `submod-index`, `chk-caller-prefixes`, `io-hiroute-stale` — the row that same commit added. The body's 34 / 32 / 2 is the stale figure. |
| `L-1` — same census on the fixed tree, 34 data rows, 31 citing, same 3 | **exact.** 35 table lines; the one row fewer is `fixleg-scan-paste`, which cited a record, so 32 − 1 = 31. |
| `L-2` — `plan` at `7cb7213` occurs at `:65 :75 :77 :80 :83 :102` | **exact.** The body's `:65 :72 :74 :77 :79 :102` is wrong in three positions. |
| `L-2` — the pre-round contrast at `3a6a10b` is exactly one hit at `:83` | **exact.** |
| `L-2` — on the fixed tree the enumeration is `:65 :75 :77 :80 :100`, five | **exact.** `L-4`'s deletion removed the `:83` occurrence and shifted the report-back hit two lines up. |
| `io-design.md:99`–`:100` carries the quoted sentence across the wrap | **exact.** `:99` ends 其**路由与 `observed_after`, `:100` carries 窗口**的未解问题仍挂在 rider `HI-route`，不因本设计关闭。 The row's widened citation is right and the old `:100` alone was not. |
| `HEAD:document-harness/io-design.md` = `8f3c82c2627cb678e520f46d3a47fdf1616fd8d9` | **exact**, still the blob `HD-35` binds. |
| staged change set, five paths, the numstat pairs | **exact**, all five. |
| battery = 790 passed | **exact.** `cd tooling && python -m pytest -q` → **790 passed in 133.27s**, run by me at the tip after every other measurement below. Same count as the plan's base figure at `ee3e05f` and the FULL's at `7cb7213`, so this leg moved no code. (My wall time differs from the body's 148.97s; the count is the claim.) |

No test pins the amended lines — `test_dispatch.py:298`–`:302` reads `REVIEW.md` live but
asserts only that it gains no numbered section — so 790 passing is consistent with the edit
rather than evidence the edit was inert.

### 2.3 The class scans, re-run rather than read (`HD-41` ④)

Rider `fixleg-scan-paste` recorded four fix legs that pasted nothing. This one pastes four
scans. All four reproduce at the tip.

| class | scope as declared | reproduces? |
|---|---|---|
| 1 — filing vs observing | ten `E10` members | **exactly.** 5 hits, byte-identical to the paste: `REVIEW.md:46`–`:48` plus two unrelated uses of *unrepresentable* in `supersession-1.md:25` and `paragraph-map.schema.json:23`, both `E2`-frozen. **The declared scope is what `V-1` is about.** |
| 2 — instruction-first re-typed | ten `E10` members | **exactly.** 2 hits, both `EXECUTION.md`; `ORCHESTRATION.md`'s copy is gone. |
| 3 — merged-role as current | ten members + `HARNESS-DECISIONS.md` + `HARNESS-RIDERS.md`, English **and** Chinese patterns | **exactly.** 7 English hits and 4 Chinese, byte-identical. The widening is real and was needed: the candidate's pattern was English-only and its range excluded the decision log, so `HD-46`'s site was reachable by neither — which is more than the FULL said, and the leg says so. |
| 4 — rider quotations of signed files | `HARNESS-RIDERS.md` | **exactly.** Four quoting rows, and I checked each against its source rather than accepting the check: `Document-Work-Assurance-Contract-v3.md:62` carries `wspec-owner`'s cell; `split-design.md:64` carries design-route's 「`EXCLUDE` 新增 submodule 目录」 and `:44` carries `six-signed`'s 「六命令原样」; `io-design.md:115` carries 「六个命令中五个纯读」. Three were exact already; the fourth is `O-3`, now exact. |

**The one elision is honest.** The class-3 Chinese paste cuts the `waiver-live` row to its
matching clause and marks the cut in place. Measured: the row is 391 characters, and the
clause the paste keeps — 分歧改变动作——豁免轮里一个 session 照读、另一个引豁免跳过，跳过会漏
live 裁决 — is present in it verbatim. Every other line in the four pastes is whole.

### 2.4 Do the guards still bind, and the two disclosed operations

No guard changed, so `E4` and `E5` have nothing new to bite on. Three things were executed
rather than read:

- **`layer_path_check`, replayed.** The guard reads a staged diff that no longer exists, so I
  imported the module, rebuilt `added_lines_by_path` from `git diff -M -U0 ffe46e5 860729f`,
  and ran `unresolved_tokens` per member. Added lines per path reproduce exactly —
  `HARNESS-DECISIONS.md` 2, `HARNESS-RIDERS.md` 1, `ORCHESTRATION.md` 2, `REVIEW.md` 2,
  journal 159 — and **zero failures** on the two members.
- **The guard's stated blind spots, closed by hand rather than asserted.** Markdown links carry
  no backtick token: the added lines contain **exactly one**, `EXECUTION.md` from
  `ORCHESTRATION.md`, and it resolves from `document-harness/`. Backtick path tokens across
  **all five** added-line sets including the non-member journal: **3, all resolve**
  (`document-harness/plans/prerun-riders.plan.md` twice, `migration/document-work-assurance-v3/`
  once).
- **The row deletion creates no dangling pointer.** `git grep -n fixleg-scan-paste HEAD`
  returns four hits, all records that read as history: `CONSTRUCTION-LEDGER.md:67`, the
  `EXECUTOR-CHARTER` journal, this round's own journal, and this round's plan. Nothing live
  names the deleted row — which is the defect class `io-hiroute-stale` exists for, checked
  rather than claimed.

**Operation one: `fixleg-scan-paste` deleted.** Its redeem-when at `7cb7213` reads *"下一次修腿
落地时——本行是核对项：修腿正文贴了扫类输出即兑付删行"*. This leg is a fix leg and its body
carries the paste, so the touch condition is met at this commit and `R10` deletes a redeemed
row in the same commit. Well-founded. The row's own unanswered half — *"四连是否值得比一行更重
的处置归用户"* — is preserved by the journal's offer to strike the deletion, so the deletion
does not quietly close the user's question.

**Operation two: `io-hiroute-stale`'s source column gains 用户 2026-08-23 裁定保留.** The
house-form precedent the body cites is real: `status-key` keeps 用户裁（2026-08-10）：不加机器
（`E6`），bank and appends **2026-08-22 复问，用户第二次维持**. The same shape is applied here,
and the candidate's historical offer is kept rather than overwritten. Both operations are
one line, reversible, and **said rather than silent**, which is what `E9` requires of a
widening.

---

## 3. Findings

### `V-1` (low) — the repair fixed the site and left the sibling the finding itself named, so `REVIEW.md` and the frozen schema now disagree where they used to agree

**Location.** `schema/document-assurance-v3/harness-issue.schema.json:45`, the second sentence
of `observed_after`'s description: *"an issue **claiming to be observed mid-run** is
unrepresentable, so it cannot be used to influence a run in flight (N2-A10)"*.

**Ground truth.** `L-3`'s own text named this file as the origin of the loose clause — *"The
schema's own field description carries the same looseness, so the candidate inherited it rather
than invented it"*. The repair changed `REVIEW.md` to the strict reading and did not name the
schema. The result at this tip:

| text | reading |
|---|---|
| `harness-issue.schema.json:45`, first sentence | strict — *"the terminal status the run had reached when this **was recorded**"* |
| `harness-issue.schema.json:45`, second sentence | **loose** — *"claiming to be **observed** mid-run"* |
| `REVIEW.md:47`–`:48` (repaired) | strict — *"**recorded** while the run is still in flight"* |
| `issues.py:140`–`:141` | strict — *"an issue **recorded** against a live run"* |

Before this round `REVIEW.md` and the schema gloss agreed, both loose. After it they disagree,
and the schema's description now also disagrees with its own first sentence one clause earlier.

**Why the class scan could not catch it.** Class 1's declared scope is the ten `E10` members,
and `harness-issue.schema.json` is not one — only `paragraph-map.schema.json` is. The scope is
declared one sentence before the result, so `HD-41` ① is satisfied and the scan is not
over-claimed. What the scope excluded, though, is the one sibling site the accepted finding had
already pointed at, and the conclusion drawn from it — *"Only `REVIEW.md` ever conflated the
two"* — reads as a closed class to anyone who does not carry the scope sentence forward.
`E7` asks for the defect class, not the reported instance; the class is not closed.

**Why it is low and not more.** Nothing in the machine acts on the gloss: the schema constrains
only the enum, and `issues.py` checks only that the issue's `observed_after` matches the run's
terminal status, so an issue observed mid-run and filed after it validates today. The failure is
a reader's: an orchestrator routing a reviewer's observation at closeout follows `REVIEW.md`'s
now-open route, opens the schema to fill the document, and is told the issue is unrepresentable.
The nameable downstream decision — `R9`'s test — is that they decline to file, and the
observation dies with the round, which is the exact outcome `REVIEW.md:51`–`:52` exists to
prevent (*"the observation survives the round that could not act on it"*). That it is nameable
is why this is not wording-level and does not ride the next batch under `R9`.

**Bytes, and where they must wait.** At `:45`, replace *claiming to be observed mid-run* with
*recorded while the run is still in flight* — the same substitution `L-3` made, and the reading
the description's own first sentence and `issues.py` already carry. **These bytes may not be
written now.** `schema/document-assurance-v3/harness-issue.schema.json` is one of the fifteen
pack files `E2` freezes — verified, the pack holds exactly fifteen at `HEAD` and this is one —
so `E2` requires a recorded user ruling and `R10`'s single exception applies: *bytes on a path
`E2` also freezes bank until that rule's recorded ruling exists (`HD-20`), however appliable
they are.* **Route: a row in `HARNESS-RIDERS.md`**, not an application. The precedent is exact
and already in the bank — `wspec-owner` banks stale prose inside two frozen pack schemas for
the same reason, and `six-signed` / `design-route` / `io-hiroute-stale` bank the same shape on
signed files. `R10`'s *"schema governance … never this one"* exclusion does not reach it:
that is the caller's schema evolution, whereas this is the instrument's own frozen prose
drifting from its own instruction layer, which is what `wspec-owner` establishes as
construction-side debt.

**On redeem-when and deadline, offered rather than written** — the row is the orchestrator's to
write at closeout. Touch: the packaged batch that re-signs the pack, or `E2`'s recorded ruling
for these bytes, whichever first. Deadline, since the value does expire: the first
`HarnessIssue` actually filed under `REVIEW.md`'s new route in a product run's closeout — the
moment the two texts are read together by someone acting. `R10` forbids a deadline inside the
round that writes the row, and that moment is outside it, this round having no product run.

### `O-1` (observation) — the FULL's `O-1` persists at this tip and is now the closeout's alone

`CONSTRUCTION-LEDGER.md:79` still reads *"`HI-route` 未闭：重扎根这条裁决同样只活在 commit 正文
/台账/本行"*, and `git grep HI-route` confirms the rider is gone from the bank, so the premise
is false at `860729f`. **Correctly untouched**: the plan's change-surface table puts that file
at closeout in the orchestrator's hands, and this leg had no boundary there — the journal says
so in those terms. I record it only because this is the last review leg of the round: after
this record, nothing else will re-derive it, and the closeout is the one surface that will
write that file anyway.

### `O-2` (observation) — what this VERIFY could not verify

Marked, never folded into supported (`R4`). None of these is a defect; each is a ceiling.

- **`E1`'s none-held disclosure**, and the journal's claim that orchestrator and executor were
  separate sessions on both legs — the first round under `HD-55`. All four holdings are process
  claims about sessions, and the git identity is the same on every commit in this history.
- **The user's approvals**: the all-in acceptance of the package on 2026-08-23, and the separate
  ruling keeping `io-hiroute-stale`. Both exist in the repository only as the commit body's
  account of them (`R7` ceiling, §1).
- **Ordering claims**: that the class scans and the battery were run after the last edit, and
  that paths were staged explicitly. The figures reproduce, which is consistent with the claim
  and does not establish it.
- **`R10`'s closeout weighing** — that each low's deadline was weighed against its touch trigger
  before the spend-the-fix-leg choice was put to the user. The outcome is on the branch; the
  weighing is not.

---

## 4. Coverage — read in full, sampled, only probed (`R4`)

**Read in full at the subject:** `document-harness/CONSTRUCTION-CHECKLIST.md` (the standing
instruction), `migration/document-work-assurance-v3/v3-harness-review-contract.md` (its stub),
`migration/document-work-assurance-v3/v3-review-full-7cb7213.md`,
`document-harness/journal/prerun-riders-2026-08-22.md`, `tooling/hooks/layer_path_check.py`,
the complete diff of all five changed paths, and the whole commit body.

**Read in part:** `document-harness/REVIEW.md` `:40`–`:55`; `document-harness/ORCHESTRATION.md`
`:70`–`:88`; `HARNESS-DECISIONS.md` `:286`–`:296` plus the scan hits at `:140` `:148`;
`HARNESS-RIDERS.md` — every row's id and source column parsed at both tips, rows `:13` `:18`
`:20` `:25` `:26` `:29` `:32` `:44` read in part, most row bodies not read end to end;
`document-harness/plans/prerun-riders.plan.md` `:95`–`:130`; `document-harness/io-design.md`
`:96`–`:102` and `:115`; `schema/document-assurance-v3/harness-issue.schema.json` `:36`–`:50`;
`tooling/rsclib/document_harness/issues.py` `:140`–`:155`;
`contract/Document-Work-Assurance-Contract-v3.md` `:62`;
`document-harness/split-design.md` `:44` `:64`; `CONSTRUCTION-LEDGER.md` `:67` `:79`.

**Probed only:** `tooling/tests/` and `tooling/hooks/` by grep for references to the two edited
members; git history, blob ids and tree ids.

**Not opened:** the two contract supersessions, the operating-contract stub,
`schema/document-assurance-v3/paragraph-map.schema.json`, `document-harness/EXECUTION.md`
(grep only), `document-harness/README.md`, `v3-cold-read-3a6a10b.md`, and every other review
record. This is a VERIFY, not an `E10` read, so no per-member blob table is owed; the five
member blob ids in §1 are recorded because the two amended members will need them at the next
layer read.

**Re-executed here, not accepted as reported:** the battery (790 passed in 133.27s); the rider
bank census at both tips, by parsing every row; the three `plan` enumerations at `3a6a10b`,
`7cb7213` and `860729f`; all four class scans on the fixed tree; the `waiver-live` elision
against the whole row; `layer_path_check` replayed over the commit's added lines; the markdown
links and every backtick path token on the added lines of all five files; the added-line counts
and the numstat; the `io-design.md` `:99`–`:100` span and its blob id; the three `E2` blob ids
and the pack tree id at base and tip; the `fixleg-scan-paste` and `HI-route` reference sweeps;
the pack file count; and the freeze marker's range.

**Process claims marked, never verified:** all of `O-2`.
