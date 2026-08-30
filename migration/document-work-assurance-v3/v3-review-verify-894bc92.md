# VERIFY — `70c82b4..894bc92` (round `CORE-ONLY-CODE`)

Targeted VERIFY of round 2 of batch `CORE-ONLY`. Subject received as one range and nothing
else (`R2`); round, budget, authorization, obligations and every figure below are re-derived
from the repository, and no reported figure is accepted — including the fix commit's own,
which the FULL's §7 asked this VERIFY to re-derive rather than read. Standing instruction as
dispatched: `document-harness/CONSTRUCTION-CHECKLIST.md`, the file this repository declares
under `rules` in its `harness.json`, read first, then the counterpart it names,
`document-harness/RULES.md`.

**Verdict: `REVIEWED_NO_BLOCKER`.** 2 findings, both low; 2 observations.

Everything plan ruling 38 authorized is in the tree, in the reviewer's own bytes where the
ruling said reviewer's bytes, with `HD-59` respected at every forward correction and the two
deliberate non-edits named in the body as ruling 34's alternative requires. Both accepted
blockers' class scans re-run clean at the tip against the two commands the FULL named. The
suite, both sweeps, the four guards and the announced-path alarm are unmoved. A VERIFY is not a
re-certification (`R4`).

The two findings are small and neither is inflated: one is a site of `B-1`'s own class that the
FULL did not find and that the repair's class-scan statement classified away in passing, and one
is a wrong file count in the repair's body. Neither would have justified the repair leg, which
is spent.

---

## 1. Subject, re-derived

```
$ git rev-parse HEAD
894bc92004fd6936c33b7279627c59eadf922b12
$ git status --porcelain
?? .goals/
$ cat .harness/review-pending.json
{
 "subject": "70c82b4776ed2861a25c41192fd0209dc8b6c929..894bc92004fd6936c33b7279627c59eadf922b12",
 "dispatched_at": "2026-08-30T07:36:18+00:00"
}
$ git rev-list --count 70c82b4..894bc92
3
```

The marker carries exactly the range I was handed and the branch tip is the range tip, so
`E9`'s window holds and nothing but this record is owed to it. `.goals/` is untracked, was
untracked at the FULL, and no commit in the range names it — which is also the evidence that
`E8`'s *stage explicit paths, never `add -A`* was kept: an `add -A` in this worktree would have
swept it in.

Three commits, classified by hand from their own bodies and diffs:

| kind | commit | what it is |
|---|---|---|
| record, committed unchanged (`R6`) | `affacc2` | the FULL over `fff2203..70c82b4`, verdict `CHANGES_REQUIRED` |
| plan, fix-gate carrier (orchestrator) | `8d59758` | step 5 checked, plan ruling 38 written, resume pointer moved |
| review fix (`E9`'s one user-approved fix) | `894bc92` | the repair — the whole of what this VERIFY covers as a diff |

Each names its kind in its own first sentence. `Kind: plan` is not one of `E8`'s eight listed
words, but it is attributable without asking — the same sentence says *fix-gate carrier,
orchestrator* and names ruling 38 — and it has four prior uses in the last forty commits, so it
is this repository's established form and not a novelty introduced here.

## 2. Round, budget, authorization, obligations — re-derived

**Round.** `CORE-ONLY-CODE`, round 2 of three, from
`document-harness/plans/core-only.plan.md`. Its *Steps — round 2* checklist now has box 5
checked (**FULL DONE**, `CHANGES_REQUIRED`) and box 6a — the fix gate — as the first unchecked
box at the moment `8d59758` landed; the resume pointer reads *steps 1–5 done, FULL
`CHANGES_REQUIRED`; step 6a — the one fix under ruling 38 — is next, then the VERIFY*. So this
is that VERIFY, and it is box 6b.

**Budget (`E9`).** One FULL, at most one user-approved fix, one targeted VERIFY. `E9`'s test —
*has a valid independent FULL already occurred?* — is now **yes**: `affacc2` landed it. So
`894bc92` is the round's one user-approved fix, it consumes the fix leg, and it obliges this
VERIFY. Counted rather than assumed: exactly one commit in the range changes the work product
(`894bc92`); `8d59758` changes `core-only.plan.md` alone, which is the round's own gate record
and not the work product; `affacc2` adds the review record alone. The FULL's window closed when
its record landed, and between that record and the fix gate the branch took nothing. My own
window is open and empty: nothing has landed since `894bc92`.

**Authorization.** Plan ruling 38, written at `8d59758`, is the fix gate. It spends the one fix
leg on `B-1`, `B-2` and all four lows in one commit with the reviewer's bytes, and it makes
three choices inside that boundary: `document-harness/io-design.md:8` and `:42` are **not**
edited and are named in the body with why not; the six committed conclusions `B-2` lists are
corrected **forward in one paragraph under `HD-69`**, the originals left word for word and the
ledger's two lines untouched; the four lows ride the same commit. `O-1` and `O-3` owe nothing
now; `O-4` enters the closeout's read-debt statement. I checked every changed path against that
boundary and found no stray — §4.

**`R7`.** Nothing here rests on an authorization I cannot see. Ruling 38's text is in the
repository; the user's words behind it are not, and I state that as the ceiling rather than
treating it as a gap.

**`R4` — what I read.** In full: `CONSTRUCTION-CHECKLIST.md`, `RULES.md`, `harness.json`,
`.harness/scan-surfaces.json`, the FULL record `v3-review-full-70c82b4.md`, plan ruling 38 and
the plan's step-5 and resume-pointer hunks, `CONSTRUCTION-INDEX.md`, the complete diffs of all
three commits in the range, and all three commit bodies. Sampled: `HARNESS-DECISIONS.md` (the
new forward paragraph and `HD-66` end to end; `HD-69`, `HD-55`, `HD-53`, `HD-35`, `HD-19` and
`HD-46` at their cited lines), `HARNESS-RIDERS.md` (row 15 byte-compared against its
predecessor, every row's redeem-when cell, `e1-reader` and `caller-rule-read-no-generator` in
full), the round journal (the new section in full, the rest by targeted grep),
`contract/Document-Work-Assurance-Contract-v4.md` (`:276-284` only). Probed only:
`tooling/rsclib/document_harness/dispatch.py` (the two changed hunks and thirty lines around
them, not the whole module), the test suite (the two assertions the body names, plus a grep of
`tooling/tests/` for the changed message text), `EXECUTION.md` / `REVIEW.md` /
`ORCHESTRATION.md` (not read this round; only their sweep output). **Marked, not verified**
(`R4`): that the fix executor ran as its own cold session, and that `E1`'s four holdings sat
where the body says. I have no instrument for either; I can see only that the commits and
records are consistent with it, and that the body states the holding explicitly, which is what
`E1`'s exception channel would require had it been taken.

## 3. The accepted findings, one by one

Re-derived at the tip. Each row is what ruling 38 authorized, then what the repository shows.

### `B-1` — the membership counts

| what ruling 38 directed | what the tree shows |
|---|---|
| `CONTRACT-V4-SIGNATURE.md:197` stops stating a count, in the reviewer's bytes | `:197` now reads *`E10`'s membership sentence does not name this one, and this file claims* — the reviewer's bytes exactly, one line changed, nothing else in the file |
| `HARNESS-RIDERS.md:15`'s residual enumeration corrected forward | done, and `HD-59` held — see below |
| `io-design.md:8` and `:42` **not** edited, named in the body with why | both unedited; the body names both, quotes both, and gives the signature reason |

The signature reason is not taken on trust. `io-design.md`'s blob at this tip is
`a1594eb27311cfe4cdc1aa32c32a521c0af4b65f` by `git rev-parse HEAD:` and identical by
`git hash-object` on the worktree file; the file is 135 lines; and `HARNESS-DECISIONS.md:247`
records `HD-35`'s third signature (2026-08-23, round `CONTRACT-V4`) as binding blob
`a1594eb2…`, sha256 `6fc29c11…b9c2`, **135 lines**. So the two sites do sit inside a signed blob
and editing them would owe a re-signature, which is the user's to give. Ruling 34's alternative
is the route taken, and taking it is what the body does.

`HD-59` on the rider row, checked mechanically rather than by eye: the old row 15 and the new
one split into six table cells; cells 0, 1, 2, 4 and 5 are byte-identical, and cell 3 — the
finding text — is the old cell as a **strict prefix** (3111 chars) with 818 chars appended.
Nothing was re-typed and nothing was removed.

**The class scan, re-run at the tip, over the scope `08d3137` declared:**

```
$ git grep -ni -e nine -e 九 -- ':!migration/' ':!document-harness/journal/' \
      ':!document-harness/plans/' ':!CONSTRUCTION-LEDGER-archive.md'

per-file hit table, both sides of the write:
  before (70c82b4): 14 files       after (894bc92): 13 files
  delta: CONTRACT-V4-SIGNATURE.md:1 leaves; no other file's count moves
```

That is exactly what the body claims for this key, and it is right. Reading the 13 files' hits
by hand: `io-design.md:8` and `:42` are the two membership counts left standing by ruling 38;
`RULES.md:115` is the narrative of the list going nine to seven and is true; `ONBOARDING.md`'s
four, `ORCHESTRATION.md:49`, `document-harness/README.md:22` and `:24`, and `flow.py:99` are the
non-counts the corrected row enumerates; `CONSTRUCTION-LEDGER.md`'s four,
`HARNESS-DECISIONS-archive.md:432`, `HARNESS-DECISIONS.md:83`, `:593`, `:597`, `:601`, `:854`,
`:859`, `HARNESS-RIDERS.md:19`, `:20`, `:21`, `:24`, `:31`, `:38`,
`test_harness_config.py:5` and `:7`, and three test files' fixtures are each dated, past-tense,
or not about membership at all — I read every one. **One is not**, and it is `F-1` below.

### `B-2` — the `dtw dispatch` attributions

| what ruling 38 directed | what the tree shows |
|---|---|
| `RULES.md:175`'s parenthetical deleted | `E12` now opens *The handoff is one commit SHA / range — no per-acceptance argument.* — the reviewer's bytes, one line |
| `dispatch.py:269`'s trailing clause deleted | done; the refusal now ends *…then dispatch that commit* |
| six committed conclusions corrected forward in **one** paragraph under `HD-69` | one paragraph, 18 added lines, **0 deleted** — so all six originals are untouched by construction |
| the ledger's two lines untouched | `CONSTRUCTION-LEDGER.md` is not in the commit's path list |

The repaired refusal is exercised rather than read — `control_root_of` on a commit carrying no
control plane:

```
Issue(code='V3-DISPATCH-NOT-AN-EVIDENCE-COMMIT',
      message='no path in 894bc92 ends in control/state.json, so this commit does not carry a
               run's control plane and is not a review subject; re-stage the run's whole
               control root and commit it, then dispatch that commit', where='evidence_commit')
```

The deletion did not strip the remedy, which is what the comment above it says the message
exists to carry.

**The class scan, re-run at the tip:**

```
$ git grep -n "dtw dispatch" -- ':!migration/' ':!document-harness/journal/' \
      ':!document-harness/plans/' ':!*archive*' ':!tooling/tests/'

  before (70c82b4): 26 lines over 17 files
  after  (894bc92): 33 lines over 17 files
  per-file delta:  HARNESS-DECISIONS.md 3 → 11 (+8);  document-harness/RULES.md 2 → 1 (−1)
  file sets:       identical — diff of the two sorted lists returns nothing
```

The delta is entirely the correction, as the body says. The file count is not, and that is
`F-2`.

I did not stop at the reported key. `E7` asks for the class, so I ran the flags themselves —

```
$ git grep -n -e '--construction-executor' -e '`--range`' -e '`--read`' \
      -- ':!migration/' ':!document-harness/journal/' ':!document-harness/plans/' \
         ':!*archive*' ':!tooling/tests/'
```

— and every hit is accounted for: `HD-69`'s own sentence and `HD-55` (left word for word,
corrected forward), the correction paragraph itself, `construction_dispatch.py`'s own flags,
`CONSTRUCTION-LEDGER.md:143` (the dated history of round `EXECUTOR-CHARTER`'s closure, which the
body reports rather than fixes and which is outside ruling 38), `HARNESS-RIDERS.md:40` (which
states the post-move fact correctly), and `dispatch.py:259` — `O-1` below. The phrase
*construction-round door* returns nothing outside `migration/`, `journal/` and `plans/`.

The two usage lines the body quotes are what the commands print:

```
$ python tooling/construction_dispatch.py --help
usage: construction_dispatch [-h] (--range RANGE | --read READ | --construction-executor)
                             [--repo-root REPO_ROOT]
$ python tooling/dtw.py dispatch --help
usage: do-the-work dispatch [-h] (--subject SUBJECT | --executor RUN) [--repo-root REPO_ROOT]
```

### The four lows

* **`L-1`** — the journal's new section restates acceptance 1 as *twenty-seven caller-held, and
  one — the contract's past-tense `review.schema.json` — instrument-held under plan ruling 19*,
  and says the count acceptance 1 states as zero is one. Checked against the ground truth rather
  than the report: `contract/Document-Work-Assurance-Contract-v4.md:279-284` says of that schema
  *that schema was this instrument's own rather than any caller's: it left the tree with the
  same round and is reachable in this repository's git history*. The correction is right, and it
  correctly leaves the measurement itself unmoved.
* **`L-2`** — the journal names the five bare unqualified sites. All five are where it says and
  read as it says: `run-v2/README.md:48` *a knob in each script before R2*, `:100` *no CONFIG
  knob since R2*, `compare_blocks.py:29` *what R2 adds*, `:68` *the failure mode R2's
  no-defaults rule closes*, and `candidate_path_check.py:83` *the ordinary R1 sentence*. All
  five are left standing, which is ruling 30 and ruling 38 both.
* **`L-3`** — `dispatch.py:517-518` and `:522-523` carry the reviewer's two sentences verbatim.
  The present tense about a deleted file is gone, *neither half* is gone, and the pointer to a
  section that moved is gone.
* **`L-4`** — checked at both ends: `c08de13`'s body does open *plan ruling 37 (e)*, and ruling
  37 has `(a)`, `(b)`, `(c)` and nothing else. The journal's forward note names step 4b, and
  step 4b does name *the journal's §7 written forward*. The commit body is not rewritten, which
  is `HD-59`.

## 4. The whole repair diff

Six files, `+72 −10`, and nothing else:

```
CONTRACT-V4-SIGNATURE.md                                1 +   1 −
HARNESS-DECISIONS.md                                   18 +   0 −
HARNESS-RIDERS.md                                       1 +   1 −
document-harness/RULES.md                               1 +   1 −
document-harness/journal/core-only-code-2026-08-30.md  44 +   0 −
tooling/rsclib/document_harness/dispatch.py             7 +   7 −
```

Every path is inside ruling 38. `CONSTRUCTION-LEDGER.md`, the plan's Steps checklist, every
`HD` status and every review record are untouched, as the body says. The one code file changes a
refusal string and a comment block; no signature, no control flow and no test changes.

**Measured after every write, on the tip:**

```
$ python -m pytest tooling/tests -q
873 passed in 160.60s (0:02:40)                    # delta zero against the FULL's 873

$ python tooling/sweep_refs.py
-- 13 caller-held or unresolvable references over 8 members and declared rule files

$ python tooling/hooks/layer_path_check.py       exit=0     (8 declared paths scanned)
$ python tooling/hooks/candidate_path_check.py   exit=0
$ python tooling/hooks/review_freeze_check.py    exit=0
$ python tooling/ledger_cap_check.py             exit=0

$ python tooling/announced_path_disclosure.py --before 70c82b4 --after 894bc92
  floor 1d4d9aa…; 3 non-merge commit(s) judged
  every announced path changed in this range is named by the commit that changed it
exit=0
```

**On my own harness-only tree**, built the way acceptance 1 names — `git archive` of the eight
product-tier rows at `894bc92`, extracted, `git init`, committed, **59** tracked files against
this repository's **423**:

```
$ python tooling/sweep_refs.py <that tree>
-- 28 caller-held or unresolvable references over 7 members and declared rule files
   0 MISSING · 0 PATHTOK · 28 NAMETOK

$ layer_path_check 0 · candidate_path_check 0 · review_freeze_check 0
$ python tooling/dtw.py --help                                exit=0
$ grep -r CONSTRUCTION-CHECKLIST .                            nothing
$ grep -r -e --range -e --read -e --construction-executor --include=*.py .
   one hit: tooling/rsclib/document_harness/dispatch.py:259   (a comment — O-1)
```

Acceptance 1's own classification, re-derived by hand and not by prefix, lands where `L-1`'s
correction puts it: twenty-seven caller-held (`harness.json` ×8, `HARNESS-DECISIONS.md` ×2 and
`HARNESS-RIDERS.md` ×1 at a caller's own root, twelve caller run artifacts and battery commands,
two caller review records) and one instrument-held under plan ruling 19.

**No new site of either class was created by the repair itself.** Both scans above are re-runs
at the tip, not readings of the body, and the only lines the repair added to either scan's
output are the correction paragraph that names what it corrects.

## 5. Findings

Neither would have justified the repair leg. The leg is spent, so neither can be repaired inside
this round without the user explicitly exceeding ruling 38's boundary, which `E9` says must be
said rather than done silently. Routing is not mine.

### `F-1` (low) — `HARNESS-DECISIONS.md:88-91`, inside `HD-66` (`status: live`), is a fourth site of `B-1`'s class: a present-tense membership claim, a count of nine, and a pointer to a rider that no longer exists

**Location.** `HARNESS-DECISIONS.md:88-91`, the bullet beginning *结构性的那一条，值得单独看见*.

**What it says.**

```
:88  `CONSTRUCTION-CHECKLIST.md` 与两个 retired contract stub **本身
:89   就是 `E10` 的九成员**，而按 `CONSTRUCTION-INDEX.md` 它们**是构造侧、不 travel**。
      九分之三不 travel，所以「只带 core」在**定义上**就与 `E10` 的成员集冲突
:91  已 banked 为 rider `checklist-cited-not-carried`
```

**What the repository says.** Three of its assertions are false at this tip, each falsified by a
different act of this batch:

* **the count.** `RULES.md`'s membership sentence names **seven** paths. Nine has not been the
  count since item D landed in this round.
* **the members.** None of the three files it names is a member. `CONSTRUCTION-CHECKLIST.md`
  left the layer in round `CORE-ONLY-LAYER` and is now this repository's declared rule file; the
  two retired contract stubs were **deleted** by this round — `git ls-files` returns neither.
* **the rider.** `checklist-cited-not-carried` was redeemed and its row deleted in round
  `CORE-ONLY-LAYER` (`4b81dd9`, `322fd1c`), which `CONSTRUCTION-INDEX.md`'s own header records:
  *Rider `checklist-cited-not-carried` is redeemed and its row is gone.*

**Why it is a finding and not just a stale line.** `HD-66` is `live`, and `E10` makes reading
`§live` an obligation at **every** round's opening, waiver or not. The bullet does not merely
carry a stale number: it states as a standing structural conclusion that *「只带 core」在定义上
就与 `E10` 的成员集冲突——这不是漏了几个链接，是两张清单互不相容* — that the goal this batch
exists to reach is incompatible **by definition** with `E10`'s member set. That incompatibility
is exactly what rounds 1 and 2 dissolved. So the next round's opening read finds a live ruling
asserting the work is impossible by construction, resting on a premise the work removed, and
pointing at a bank row that is gone. `HD-66` is also the entry `L-1` names as the reader of
acceptance 1 — the same entry, now carrying a corrected input and an uncorrected premise.

**Why the repair did not catch it.** It is outside ruling 38's boundary, so the executor was
right not to edit it. What is inside the repair is the statement about it: the body's `B-1` leg
says *before, the three membership counts were `CONTRACT-V4-SIGNATURE.md:197`,
`document-harness/io-design.md:8` and `:42`* — an absolute over a scan whose declared scope
returns this line — and *every non-count is unchanged*, which counts this line among the
non-counts. And the corrected rider row, whose stated purpose is *逐条列出以免下一轮重扫*, now
reads its residual enumeration as eight non-counts plus the two signed sites, and this line is in
neither list. That is the same failure mode `B-1` was raised about: a class declared clean at the
sites someone looked at, with the durable carrier under-enumerating the rest.

**Honest ceiling on this finding.** The bullet sits directly beneath one that is explicitly dated
and attributed (*今日实测…orchestrator 2026-08-29 用 `tooling/sweep_refs.py` 跑的*), and it opens
by pointing back into that measurement (*结构性的那一条*). A reader can argue the whole bullet
inherits that date and is therefore history, like `CONSTRUCTION-LEDGER.md:143`, which the body
reports rather than fixes for exactly that reason. I do not think that reading survives the last
two sentences — they draw a standing conclusion in the present tense and name a bank row as
currently banked, neither of which reads as a measurement snapshot — but the ambiguity is real
and I state it rather than resolving it. The `已 banked` pointer is the leg that does not survive
under any reading: that row is gone.

**Bytes, if the route allows them.** `HD-59` forbids editing a committed conclusion in place, so
this is a forward correction appended under `HD-66`, the four lines left word for word:

> **向前更正（2026-08-30，轮 `CORE-ONLY-CODE` 之后）：本条「结构性的那一条」所记的冲突已经消失，
> 三处事实均已被本批推翻。** `E10` 的成员数自轮 `CORE-ONLY-CODE` 起为 **七**（item D 删掉两份
> retired contract stub）；`CONSTRUCTION-CHECKLIST.md` 自轮 `CORE-ONLY-LAYER` 起不是成员，而是本仓
> 在 `harness.json` 里声明的自有规则文件；两份 stub 已不在树上。故本条所说的「九分之三不 travel、
> 两张清单互不相容」不再成立，rider `checklist-cited-not-carried` 亦已于轮 `CORE-ONLY-LAYER` 兑付
> 删行（见 `CONSTRUCTION-INDEX.md` 抬头）。**本段只更正措辞与事实，不动本条裁决实质**：分发形态仍
> 是「submodule 为默认、core 分发若最终做不到就上 plugin」，本条仍 `live`，边界段的三条路仍未走完。

**Route (`R10`, not mine to choose).** The bytes are supplied, so the finding qualifies for the
free channel by `R10`'s wording — but the decision log is not an instruction-layer member
(`HD-19`), so `E10`'s machinery does not reach it and `HD-59` governs the shape. The fix leg is
spent. The live choices are the bank, a free-channel application if the orchestrator reads the
route that way, or round 3.

### `F-2` (low, wording-level under `R9`) — the repair body's `B-2` class scan reports *16 files before*; the true figure is 17, and the file set does not move at all

**Location.** `894bc92`'s commit body, the `B-2` class-scan sentence: *26 lines over 16 files
before, 33 lines over 17 files after.*

**The ground truth it violates.** `E3` — counts are emitted from the command that produces them.

**What the command returns.** The line counts are right (26 → 33). The file counts are not:

```
$ git grep -l "dtw dispatch" <the body's own scope> | wc -l
  70c82b4: 17        894bc92: 17        diff of the two sorted lists: empty
```

`document-harness/RULES.md` does not leave the scan when `:175` is deleted, because `:99` still
carries the key — the `E10` clause naming `dtw dispatch` as one of the four readers of `rules`,
which is true as written and not a `B-2` site. And `HARNESS-DECISIONS.md` was already in the set
before the write. So no file could have joined, and the body's own delta account — *eight new
matching lines in `HARNESS-DECISIONS.md` … less `RULES.md:175`* — does not close against a
16 → 17 move.

**Downstream decision, named honestly: I cannot name one.** Nothing acts on this figure. Under
`R9` that makes it wording-level and terminal — it rides the next batch touching this text and
spawns no round and no read. It is recorded because `E3` binds a body's figures whether or not
anything reads them, and because the neighbouring figure in the same paragraph — the `B-1` key's
*14 files to 13* — is exactly right, which is the reason to say which of the two was measured and
which was not.

## 6. Observations — `R5`, for the user

### `O-1` — `dispatch.py:259`'s comment carries a present-tense clause about `--range` on a tree where that flag does not exist; the FULL adjudicated it may stay, and I do not overturn that

The comment above the repaired refusal reads *…p5b-firewall met exactly this message and
dispatched its product run through `--range`, **which is** the construction-round entry…
(issue-p5b-firewall-…, 2026-08-07)*. The FULL's `B-2` said this comment *may keep the p5b
history: it is explicitly about what happened on 2026-08-07 and reads that way*, and ruling 38
carried that. Reading it fresh, the dated narrative does read as history; the relative clause
does not — it is present tense about a flag that is not on `dtw dispatch` on any tree, and on the
harness-only tree it is the **only** surviving mention of any of the three construction flags in
a file every caller mounts. Reproducing a finding to write it correctly is not adjudicating the
reviewer (`E12`), and I am not reopening `B-2`: the accepted fix is in place and correct. Whether
the clause is worth a word is the user's, not mine.

### `O-2` — process and record conformance, where I could measure it

`E2`: the six changed paths include neither `contract/Document-Work-Assurance-Contract-v4.md` nor
any file of `schema/document-assurance-v3/`, so no announced path is touched, and the alarm is
green over the range independently. `E8`: title `V3-CORE-ONLY-CODE-FIX-v1`, kind named in the
first sentence, body one paragraph — `git log --format=%b` returns exactly one blank line for
each of the three commits — no amend (all three carry distinct author and commit timestamps in
sequence), no push (`origin/dev` is still at `fff2203`, the round's base, so nothing in this
round has left the machine), explicit paths (`.goals/` still untracked). `E9`: one fix, one
commit, window clean at both ends. `E12`: the range in the marker and in the record names is the
dispatched one, and the plan's forward declarations still use `<this commit>` rather than a
written tip. `R6`: the FULL record's name and title are the required forms and this record
follows them. `R10`: I checked each rider row's redeem-when against the six changed files and
agree with the body — no row's touch condition is met, `E10-sync`'s write is a correction of its
residual enumeration and not a touch record (the membership sentence is untouched), and
`onboarding-carries-construction` is correctly left to the closeout.

On `E10`'s read debt: `RULES.md` is a member and the fix changed it, so a read is owed. The
change is subtractive, adds no clause and changes nothing `E12` requires — the body says so — and
no outcome in this round turns on the amended bytes, so nothing here relies on unread text;
`E10`'s ordinary rule (a read before any round relies on it) is satisfied by the debt riding
round 3's opening, which is where `O-4` and ruling 38 put it. This is stated because it would be
easy to read the deferral as `E10`'s two-fact exemption clause, and it does not need to be one.

### What I did not verify

No guard was added or changed by the repair, so there was no new binding force to mutation-test
(`E4`, `R8`); I did not re-run the round's four earlier mutations, which belong to round 1 and
the candidate, not to this leg. I confirmed by grep that no test in `tooling/tests/` binds the
refusal message's text — the two assertions the body names pin the code
`V3-DISPATCH-NOT-AN-EVIDENCE-COMMIT` and nothing else — which is what makes the string edit safe,
and also means the string has no guard, as it did not before.
