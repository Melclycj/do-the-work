# FULL review — `fff2203..70c82b4` (round `CORE-ONLY-CODE`)

Independent FULL of round 2 of batch `CORE-ONLY`. Subject received as one range and nothing
else (`R2`); round, budget, authorization, obligations and every figure below are re-derived
from the repository, and no reported figure is accepted. Standing instruction as dispatched:
`document-harness/CONSTRUCTION-CHECKLIST.md`, the file this repository declares under `rules`
in its `harness.json`, read first, then the counterpart it names, `document-harness/RULES.md`.

**Verdict: `CHANGES_REQUIRED`.** 2 blockers, 4 lows, 4 observations.

Both blockers are the same shape and neither is about whether the round's design is right —
that question is not mine (`R5`). Both are about a class this round closed at the sites it
looked at and left open at sites its own declared scope covers, with the round's records
asserting the class is clean. Both fit one repair leg; neither touches an announced path.

The implementation itself — the split, the deletion, the declared-rules charter, the guards
and the tests — I could not fault. Section 3 records what I checked and how.

---

## 1. Subject, re-derived

```
$ git rev-parse HEAD
70c82b4776ed2861a25c41192fd0209dc8b6c929
$ git status --porcelain
?? .goals/
$ git rev-list --count fff2203..70c82b4
17
$ cat .harness/review-pending.json
{
 "subject": "fff2203cebdf1b70e17eba27b0b1d6319f65d7c0..70c82b4776ed2861a25c41192fd0209dc8b6c929",
 "dispatched_at": "2026-08-30T05:58:57+00:00"
}
```

The marker carries exactly the range I was handed and the branch tip is the range tip, so
`E9`'s window holds and nothing but this record is owed to it. `.goals/` is untracked and no
commit in the range names it, which the round's journal §8 discloses and which I confirmed
against the range's own name lists.

I also confirmed the prompt I received was generated rather than composed: running
`construction_dispatch.construction_dispatch_of` on this range and rendering it returns the
dispatch I was given, byte for byte, charter line included.

Seventeen commits, classified by hand from their own bodies and diffs — no reported list used:

| kind | commits |
|---|---|
| plan / round-open (orchestrator) | `e88094c` `c042017` `70c82b4` |
| record, committed unchanged (`R6`) | `69a9a71` `d771cc4` |
| amendment (`E10` must-fix channel) | `5a9c0fd` |
| candidate | `7bcdace` `08d3137` `8ce93f7` `e8b120c` |
| ruling (orchestrator) | `1a24140` |
| pre-submission correction | `23e69d6` `691ddff` `65ecdac` `6c93c98` `c08de13` |
| errata | `90c62a9` |

Every one names its kind in its own first sentence (`E8`), checked by reading each body.
Every title is `V3-CORE-ONLY-CODE-<what>-v1` or, for the two records, the
`V3-REVIEW-RECORD-<ROUND>-<sha>-v1` form `R6` requires. Every body is one paragraph with no
trailer — measured, not eyeballed: `git log --format=%b` returns exactly one blank line (the
terminator) for all seventeen.

```
$ git ls-files | wc -l
422
$ git ls-files <the eight product-tier rows> | wc -l
59
```

## 2. Round, budget, authorization, obligations — re-derived

**Round.** `CORE-ONLY-CODE`, round 2 of three, from
`document-harness/plans/core-only.plan.md`'s status block: opened 2026-08-30, `base_commit`
`fff2203`, which is the range base I was handed. The ledger's current-pointer entry names the
same round as open at the same base. The plan's *Steps — round 2* checklist has boxes 1–4b
checked and box 5, **the FULL**, unchecked; the resume pointer says the FULL over
`fff2203..<this commit>` is next. So this is that FULL.

**Budget (`E9`).** One FULL, at most one user-approved fix, one targeted VERIFY. `E9`'s test is
*has a valid independent FULL already occurred?* — no, so every commit in the range is a
candidate or a pre-submission correction and consumes nothing. Two reads occurred and reads
spend nothing: the opening read at `e88094c` (record `69a9a71`) and the re-read the `E10`
must-fix channel owes for amendment `5a9c0fd` (record `d771cc4`). I checked `E9`'s no-commit
window on both: between each dispatch and its record's commit the branch took nothing but the
record. The fix leg and the VERIFY are both unspent, so `CHANGES_REQUIRED` is affordable.

**Authorization.** Thirty-seven rulings in the plan, of which this round executes 32–37;
`HD-69` was ruled inside the round and assigned away from it. The work items are ruling 13's
cut — C, D, the dispatch half of H — plus item K (ruling 30) and ruling 37's three correction
sites. Every changed path falls inside that boundary; I classified all 37 changed paths by hand
against it and found no stray.

**Obligations I checked against.** `E2` (announced-path disclosure), `E3` (measure last),
`E4`/`E5`/`E7`/`E8`/`E9`/`E12` on the execution side, `R6`/`R10` on the record side, plus the
plan's twelve acceptances and rider `E10-sync`'s per-touch check.

**`R7`.** Nothing here rests on an authorization I cannot see. `HD-69`'s ruling text and the
plan's rulings 32–37 are all in the repository; the user's words behind them are not, and I
state that as the ceiling rather than treating it as a gap.

**`R4` — what I read.** In full: `CONSTRUCTION-CHECKLIST.md`, `RULES.md`, `harness.json`,
`tooling/construction_dispatch.py`,
`tooling/tests/document_harness_review/test_construction_dispatch.py`, the complete diffs of
`cli.py`, `dispatch.py`, `layer_path_check.py`, `.githooks/pre-commit`, `CONSTRUCTION-INDEX.md`,
both root READMEs, `ORCHESTRATION.md`, `document-harness/README.md`, `ONBOARDING.md`, the five
item-K / bare-`R4` files, and all seventeen commit bodies. Sampled: `HARNESS-DECISIONS.md`
(`§live` end to end, `§implemented` by targeted grep), `HARNESS-RIDERS.md` (the four changed
rows in full, the rest by grep), `core-only.plan.md` (rulings, steps, acceptances and
measured-state sections in full), the round journal (§4, §5, §7, §8 in full),
`CONSTRUCTION-LEDGER.md` (header, current pointer, backlog head). Probed only: the two read
records (headers, tiering and subject derivation — not end to end), `test_dispatch.py` (diff
and test-name inventory, not the whole body), `EXECUTION.md` / `REVIEW.md` (the sections the
findings touch). **Marked, not verified** (`R4`): that the executor, reader and reviewer
sessions were separate cold `claude -p` sessions on `opus` (plan rulings 32–33). I have no
instrument for that; I can see only that the commits and records are consistent with it.

## 3. The implementation — what I checked, and what held

Everything in this section is a re-run, not a reading of the round's own figures.

**The battery.**

```
$ python -m pytest tooling/tests -q
873 passed in 155.66s (0:02:35)
```

**Both sweeps.**

```
$ python tooling/sweep_refs.py                      # this repository
-- 13 caller-held or unresolvable references over 8 members and declared rule files
$ python tooling/sweep_refs.py                      # harness-only tree, 59 files
-- 28 caller-held or unresolvable references over 7 members and declared rule files
```

The harness-only tree is my own, built the way acceptance 1 names: `git archive` of the eight
product-tier rows at `70c82b4`, extracted, `git init`, committed, 59 tracked files. The 28 are
**0 `MISSING`, 0 `PATHTOK`, 28 `NAMETOK`**. I classified them by hand rather than by prefix:
`harness.json` ×8 is the caller's own file at its own root; `HARNESS-DECISIONS.md` ×2 and
`HARNESS-RIDERS.md` ×1 are what `dtw init` writes into a caller's root — confirmed by running
`dtw init` into a fresh repository and reading what landed; twelve are the caller's own run
artifacts and the five battery commands, and `EXECUTION.md:373-380` carries the holder sentence
the compliant form requires; two are the caller's own review records, and no tracked file here
carries either basename. The twenty-eighth is contract `:279`'s `review.schema.json`, which is
**not** caller-held — see `L-1`.

Comparing the two sorted outputs gives exactly 15 sites present on the harness tree and absent
here, and none the other way, so the delta is fully accounted and the 13 here are the same 13
as at the base.

**The guards, both trees.**

```
harness-only :  layer_path_check 0 · candidate_path_check 0 · review_freeze_check 0
here         :  layer_path_check 0 · candidate_path_check 0 · review_freeze_check 0
                ledger_cap_check 0
```

**Acceptance 3 and the `dtw init` half of 11, on the harness-only tree.**

```
$ python tooling/dtw.py --help                                  exit=0
$ python tooling/dtw.py init --repo-root <fresh repo>           exit=0
   6 created, including harness.json = {"policy": null, "rules": []}
```

**Acceptance 5.** A recursive grep for `CONSTRUCTION-CHECKLIST` on the harness-only tree
returns nothing.

**Acceptance 6.** `dispatch.py` 1005 → 845 lines, `cli.py` 631 → 560, and the new
`tooling/construction_dispatch.py` is 462. No `--range`, `--read` or `--construction-executor`
survives in the product tier — the parser's mutually exclusive group now holds `--subject` and
`--executor` and nothing else. One residue of the split is `L-3`.

**Acceptance 8.** Row 8's prose now says *the three tracked pre-commit guards and the package
marker they are called through*; `tooling/hooks/` holds exactly those four. The tier is 59
against 422 here; the table's own 421 declares the revision it was taken at (`8ce93f7`), which
is what `E3` asks of a count.

**The announced-path alarm, over the whole range rather than the correction pass's.**

```
$ python tooling/announced_path_disclosure.py --before fff2203 --after 70c82b4
  floor 1d4d9aa…; 17 non-merge commit(s) judged
  every announced path changed in this range is named by the commit that changed it
exit=0
```

One commit writes an announced path — `691ddff`, at
`schema/document-assurance-v3/assurance.schema.json` — and its body names that path in full,
site by site, and states what did and did not change inside it. That is what `E2` asks and the
whole of what it certifies; whether the write should have happened I judge separately, and it
should: ruling 37 (b) authorizes it and the change is three words inside one `description`
string, with no property, type, constraint or `$defs` entry touched. The file still parses.

**The behaviour the round exists to create, exercised rather than read.** Against a disposable
repository that declares nothing, all three construction modes return
`V3-DISPATCH-NO-DECLARED-RULES`, print `# NOT DISPATCHABLE`, name no subject, exit 1 and write
**no** freeze marker. Declare one rule file and the same call derives the commit, prints a
prompt naming that repository's declaration and not this repository's, writes the marker into
the *target* repository, and exits 0. That is the defect class item C closes, and it is closed.

**The guards' binding force (`R8`).** The round's `E4` records in journal §4 are the shape `E4`
asks for — copy, sha256, assert green first, mutate, assert red, restore from the copy,
re-check the digest, assert green again, never `git checkout --`, each mutation paired with a
stated negative control. I did not re-run the four mutations; I read them and checked that each
survivor named as a control is a survivor for the reason given. What I checked directly is
`E5`: the four prompt expectations are committed fixture files carrying `{}` placeholders, not
the module's own constants, and the tests format the fixture and assert whole-document
equality. `test_construction_dispatch.py` additionally asserts the defect class rather than the
instance (`E7`) — it sweeps a repository declaring one thing while this one declares another,
and separately checks the premise that this repository still declares what that test assumes.
`NamedIssueReachability` pins the code surface at three.

**Coverage moved, not lost.** `test_dispatch.py` goes 70 → 61 test functions, the new file adds
24, the freeze-marker files go 4 → 3 + 5; +20 net against the suite's 853 → 873. One test was
not carried across — `test_a_caller_that_mounts_the_instrument_gets_the_path_through_the_mount`
in the construction executor class — and that is correct rather than a loss: the construction
charter is no longer an instrument path needing `instrument_relative`, and the product side's
own mount test still stands at `test_dispatch.py:549`. Coverage also **improved** in one place:
the product review dispatch's freeze marker had no test of its own before this round and has
one now.

**Rider rows.** The two new rows — `caller-cannot-resolve-ids` and
`caller-rule-read-no-generator` — both name their target files or clause, both name a
round-eligible surface rather than a batch for a design-shaped fix, both carry a deadline
falling outside the round that wrote them, and both deliberately supply no bytes with a stated
reason. That is `R10` and `HD-37` met. The two touch records on `E10-sync` and
`dispatch-exec-perms` are per-touch checks, correctly not redemptions.
`dispatch-exec-perms`'s touch record disproves its own premise for this round and narrows
itself instead of deleting the row — the right move, and worth naming as such.

---

## 4. Blockers

### `B-1` — the membership count moved nine → seven and three statements of it were left false, while this round's own records assert the residual class is clean

**Location.** `CONTRACT-V4-SIGNATURE.md:197`, `document-harness/io-design.md:8`,
`document-harness/io-design.md:42`; and the claims about them in `08d3137`'s body and in
`HARNESS-RIDERS.md:15`, the `E10-sync` row's new touch record.

**The ground truth it violates.** `E3` — a characterization no command established is dropped,
not softened — and `HD-41` ② and ④ (an absolute quantifier carries its scope; a class scan is an
action whose output is pasted so a reviewer can see it was run). Also ruling 34's own terms:
*the sites that count nine … change in that commit or are named in its body with why not*.
These three are neither.

**What the repository says.** All three read `nine` at `fff2203` and were true then. All three
read `nine` at `70c82b4` and are false now:

```
CONTRACT-V4-SIGNATURE.md:197      `E10`'s membership sentence names nine paths and does not name this one
document-harness/io-design.md:8   `E10` 九成员句未点名它
document-harness/io-design.md:42  ① 开轮 cold read（`E10` 九成员 + `§live`）
```

All three are present tense. `io-design.md:42` is not incidental prose: it is item ① of the
orchestrator's eleven obligations, describing what a round's opening read covers.

**Why it is not covered by what the round did check.** `08d3137`'s body declares its scan scope
as *this repository's tracked files excluding `migration/`, `document-harness/journal/`,
`document-harness/plans/` and the ledger archive*, and then says *everything the same scan still
returns is not a membership count and is listed in the rider row so the next round need not
re-derive it*. Both files are tracked and inside that declared scope. Re-running that key over
that scope —

```
$ git grep -ni -e nine -e 九 -- ':!migration/' ':!document-harness/journal/' \
      ':!document-harness/plans/' ':!CONSTRUCTION-LEDGER-archive.md'
```

— returns, besides the sites the round enumerated, exactly these three membership counts. The
rider row's enumeration of residuals — *`ONBOARDING.md`'s nine onboarding items,
`ORCHESTRATION.md`'s nine obligations, `document-harness/README.md:22`'s nine of its twelve
obligations and `:24`'s nine rows, and `flow.py:99`'s nine unguarded statuses* — omits them, so
the next batch that touches the membership sentence and trusts the row will not re-derive them
either. That is the exact failure `E10-sync` exists to prevent: the prose leg has no guard, and
the row is the only thing standing in for one.

The eleven sites the round **did** change I verified one by one against the diffs, and they are
right. This is not a claim that the sweep was not run; it is that its declared scope and its
reported result do not match, and three files were left saying something the round made untrue.

**Minimum fix.** Each of the three sites either states the current count or stops stating one,
and `HARNESS-RIDERS.md:15`'s residual enumeration is corrected forward to match. Two notes that
should shape the route rather than be discovered during it:

* `document-harness/io-design.md`'s blob is `a1594eb27311cfe4cdc1aa32c32a521c0af4b65f`, which is
  byte-identical to the blob `HD-35`'s third signature binds. Editing it owes a re-signature.
  Ruling 34's own alternative — *named in its body with why not* — is the cheaper route here,
  and taking it is the user's call, not mine.
* `CONTRACT-V4-SIGNATURE.md:197` carries no such constraint. The smallest true form deletes the
  count rather than updating it: **`E10`'s membership sentence does not name this one, and this
  file claims** — which is the reasoning `document-harness/README.md:22` already carries one
  file over (*how many members there are is `E10`'s membership sentence to say and never this
  row's*), and removes a fourth prose copy instead of resynchronising it.

### `B-2` — the "made false by item C" class was closed only where the executor's report named it; eight further sites survive, one in an instruction-layer member and one in a live ruling this round wrote after the change

**Location.** `document-harness/RULES.md:175` (`E12`); `HARNESS-DECISIONS.md:49-50` (`HD-69`,
status **live**), `:462` (`HD-55`), `:482` (`HD-53`'s title); `HARNESS-RIDERS.md:25`
(`e1-reader`); `CONSTRUCTION-LEDGER.md:190` and `:254`;
`tooling/rsclib/document_harness/dispatch.py:269`.

**The ground truth it violates.** `E7` — test the defect class, not the reported instance — and
`HD-41` ④, which makes the class scan an action rather than an intention. Ruling 37 (a)
answered the three sites journal §7.1 happened to notice; no scan for the class itself was run.
The key is one command:

```
$ git grep -n "dtw dispatch" -- ':!migration/' ':!document-harness/journal/' \
      ':!document-harness/plans/' ':!*archive*' ':!tooling/tests/'
```

**What the repository says.** After `7bcdace`, `dtw dispatch` has two modes, `--subject` and
`--executor`. Every site below still attributes a construction-round dispatch to it:

| site | what it says | why it is now false |
|---|---|---|
| `RULES.md:175` (`E12`) | *The handoff is one commit SHA / range (`dtw dispatch`)* | the range handoff is not that command's on any tree — and this is an instruction-layer member whose header says its rules hold in both directions of use, so a construction round in **any** repository is told the wrong instrument |
| `HARNESS-DECISIONS.md:49-50` (`HD-69`, live) | *`dtw dispatch --construction-executor` 要不要记 session id 以便续接* | that flag left the command at `7bcdace`, three commits before `1a24140` wrote this entry |
| `HARNESS-DECISIONS.md:462` (`HD-55`) | *跑 `dtw dispatch --executor`（产品侧）/ `--construction-executor`（构造侧）* | same |
| `HARNESS-DECISIONS.md:482` (`HD-53`, title) | *`dtw dispatch` 收两个执行者模式* | it has one |
| `HARNESS-RIDERS.md:25` (`e1-reader`) | *`dtw dispatch --read` 的第三个派发家族* | that mode is not that command's |
| `CONSTRUCTION-LEDGER.md:190` | *`dtw dispatch --read` 只有全层形态* | same |
| `CONSTRUCTION-LEDGER.md:254` | *评审走 `dtw dispatch --range`* | same |
| `dispatch.py:269` | the refusal text a caller receives: *a range is the construction-round door and does not carry a product run* | there is no such door in that command on any tree a caller mounts; this is emitted text, not a comment |

**Why `HD-69` is the sharpest of the eight.** The decision log is the supreme source of truth
and `§live` is read at every round's opening. This entry was written *inside* this round, after
the change that falsified it, and `1a24140`'s own commit body gets it right — it says *whether
the **construction dispatch** records a session id*. So the carrier and the entry it carries
disagree, and the one with authority is the wrong one. The batch that lands `HD-69` will look
for a command surface that is not there.

**Minimum fix.** Run the scan above and make each hit true. Concretely:

* `RULES.md:175`: delete the parenthetical, leaving *The handoff is one commit SHA / range — no
  per-acceptance argument.* Deleting it adds no clause and changes nothing any rule requires, so
  it is not design; naming the construction generator instead would write a path or a name for
  an instrument a caller does not hold into a travelling member, which is the class ruling 24
  deletes and acceptance 1 measures at zero.
* `dispatch.py:269`: delete the trailing clause, leaving *…re-stage the run's whole control root
  and commit it, then dispatch that commit*. The comment above it may keep the p5b history: it
  is explicitly about what happened on 2026-08-07 and reads that way.
* `HD-69`, `HD-55`, `HD-53`, `e1-reader` and the two ledger lines are committed conclusions, so
  `HD-59` forbids editing them in place: the fix is a sentence written forward beside each, or
  one forward correction naming all six. `HD-69`'s is the one that cannot wait, since it is live
  and its correct wording already exists in `1a24140`'s body.

---

## 5. Lows

Not inflated — none of these would justify the repair leg on its own, and each names the
downstream decision that goes wrong if it stays.

### `L-1` — acceptance 1 classes contract `:279`'s `review.schema.json` as caller-held; the contract's own sentence classes it as this instrument's

`08d3137`'s body lists the 28 sites and says *every one caller-held*, naming *the contract's
past-tense `review.schema.json` under plan ruling 19* inside that list; journal §5's acceptance
1 block closes with *every one is the compliant caller-held form*. Contract `:279-282` says of
that same schema: *that schema was **this instrument's own rather than any caller's**: it left
the tree*. So the count acceptance 1 states as zero is, read literally, one: a non-resolving
site naming an instrument-held artifact, standing under ruling 19's holder-or-history admission
rather than because it is caller-held. **Downstream decision:** acceptance 1 is the measurement
`HD-66` reads to decide whether core distribution is achievable, and a category recorded wrong
there is read as a clean zero by whoever asks that question next. **Bytes:** replace *every one
caller-held* with *twenty-seven caller-held, and one — the contract's past-tense
`review.schema.json` — instrument-held and standing under plan ruling 19's holder-or-history
clause*, and the same in journal §5's closing sentence, written forward under `HD-59`.

### `L-2` — the widened bare-`R<n>` survivor list is reported as clean and is not

`691ddff`'s body: *the 36 survivors classify into four families that are all correct as written.
Construction round and batch names, **always qualified** — …
`assurance/templates/run-v2/README.md:14, :48, :100, :106, compare_blocks.py:7, :29, :68`…*.
Four of those are unqualified bare `R2`s naming a construction round of this instrument's own
history, in files that travel:

```
run-v2/README.md:48     it was a knob in each script before R2
run-v2/README.md:100    — no CONFIG knob since R2
compare_blocks.py:29    what R2 adds after the mode is that run's own constants
compare_blocks.py:68    which is the failure mode R2's no-defaults rule closes
```

`tooling/hooks/candidate_path_check.py:83`'s *the ordinary R1 sentence* is filed under *a
product run's own requirement identifiers, which plan ruling 29 keeps* and is not one of those
— ruling 29's vocabulary is the prefixed `V3-D5` / `N0-A5` family. **Downstream decision:** the
next batch that re-runs this scan either re-adjudicates 36 sites the body says are settled, or
trusts *all correct as written* and stops. Ruling 30's instruction was to report, not widen, so
the sites staying is authorized; what is wrong is the report. **Bytes:** a sentence written
forward naming these five as bare and unqualified, and left standing under ruling 30's
report-don't-widen instruction.

### `L-3` — `dispatch.py`'s comment block was corrected for the stub deletion at one sentence and left false at three

`08d3137` rewrote `dispatch.py:513` from naming `v3-harness-review-contract.md` to *the retired
construction-side review contract*. Four and nine lines below, in the same block:

```
:518  The construction-side contract's §8 names one supplement as useful — which code was
      churned late — and neither half of this module emits it.
:522  The construction half derived it for a while and the attempt is written up at that section;
```

Present tense about a file this round deleted; *neither half* of a module that now has one; and
*that section* is the construction section, which left for `construction_dispatch.py` — whose
docstring does not carry the churn write-up, so the pointer resolves to nothing. **Downstream
decision:** a reader asking why churn is not derived is sent to a section that does not exist,
in a file every caller mounts. **Bytes:** *The retired construction-side review contract named
one supplement as useful — which code was churned late — and this module does not emit it.* and
*The construction half derived it for a while; that half and its write-up left this module in
round `CORE-ONLY-CODE`.*

### `L-4` — `c08de13` cites plan ruling 37 (e), which does not exist

Ruling 37 has (a), (b) and (c). The journal-forward write that commit carries is authorized by
the plan's step 4b, not by a sub-item (e). **Downstream decision:** an audit tracing each
correction-pass commit to its authorization finds one that points nowhere. The accurate fact is
recoverable from the adjacent text in the same body, so this is wording-level under `R9` and
routes to the bank rather than the fix leg unless it rides for free.

---

## 6. Observations — `R5`, for the user and not for me to conclude

### `O-1` — `E10`'s *four readers* no longer enumerates every reader of `rules` here

The construction dispatch is a fifth, and the only one that **refuses** rather than degrading
when the declaration is absent — the strongest of the *decisions that change when the file is
absent* the clause is built around. Leaving it out may well be right: naming
`tooling/construction_dispatch.py` in a travelling member would write an instrument-held path
into it, which is the class this round measures at zero. Whether a repository's own reader
belongs in that enumeration, and how the clause should read if not, is design and is yours.

### `O-2` — process and record conformance is clean where I could measure it

`E8`'s title, kind and single-paragraph form on all seventeen commits; `E9` unspent with both
read windows respected; `E2`'s disclosure with the alarm green over the whole range; `E12`'s
recorded-range discipline (the plan writes `fff2203..<this commit>`, never a written tip);
`R6`'s record names and titles; `R10`'s row format on both new riders. Stated explicitly because
both blockers are about reporting, and it would be easy to read them as a verdict on the round's
discipline generally. They are not.

### `O-3` — the shape, not the instance: six pre-FULL correction passes across the batch, each finding the next form of one class

Round 1 ran five (plan steps 5b–5e plus the FULL's fix leg), round 2 one. Every pass closed the
class *its instrument could see*, and the next pass found the form that instrument was blind to:
`sweep_refs` sees paths and basenames, so it missed bare identifiers; a grep for filenames missed
bare `R<n>`; a grep for `nine` missed the two files outside the list someone had already written
down; and rider `caller-cannot-resolve-ids`, banked this round, names a form — backticked hex
commit ids — that neither instrument can see at all. `B-1` and `B-2` are the seventh and eighth
instances. `HD-69` answers the session-shape half of this. Whether a tool-keyed class scan can
ever close a class defined by *what a caller cannot resolve*, or whether that needs a different
instrument, is the question, and it is the user's.

### `O-4` — the `E10` read debt this round leaves, and what `B-2`'s fix does to it

`ORCHESTRATION.md` and `RULES.md` both changed in this range and both are members; the round's
records say the re-read rides round 3's opening. `B-2`'s fix touches `RULES.md` again, so the
debt grows by that commit rather than being discharged by it — worth carrying into the
closeout's statement rather than discovered at round 3's opening.

---

## 7. What a VERIFY would cover

The accepted findings plus the whole repair diff (`R3`), and specifically: that the three `nine`
sites and the residual enumeration are each true or accounted for; that the eight `dtw dispatch`
sites are each true or corrected forward; that no new site of either class was created by the
repair itself, re-derived with the two commands in §4 rather than from the fix commit's body;
and that the suite, both sweeps, the three guards and the announced-path alarm are unmoved. A
VERIFY is not a re-certification (`R4`).
