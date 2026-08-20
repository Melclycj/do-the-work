# Checkpoint read — the `E10` amendment at `48b6c5f`

`E10` read, and specifically the **re-read half of a must-fix pair**: the amendment at `48b6c5f`
answers `v3-cold-read-69fc082.md`'s `M-1`, and `E10` fixes this read's subject as *"the amendment
text itself, never the work it governs"*. Not a round (`R3`): no verdict, no budget spent, output
is findings tiered must-fix / low / observation. Routing is `E10` / `R9` / `R10`'s, not mine.

**Findings: 0 must-fix, 2 low, 4 observations.** The amendment does what `M-1` asked and its
central claim is **true at every site in the layer** — I re-swept the class independently and
every hex token the ten members carry that this repository lacks resolves as a commit in the
repository the root README names (§3.3), including **two sites the read's own §3.7 table
missed**, which the single-sentence form covers for free and per-site labelling would have left
behind. Rule impact is nil as claimed: the paragraph sits in the header outside `E1`–`E12` /
`R1`–`R10`, adds no clause, and the membership sentence is byte-identical (§3.1). The two lows
are the amendment's own second sentence, whose *"read as written"* exemption misroutes the
layer's **only** labelled cross-repo citation for any reader who is not this machine's caller
(`L-1`), and the sweep evidence living nowhere in the repository (`L-2`, `E3` + `HD-41` ④).

**Named `checkpoint-read` rather than `cold-read`**, on the `v3-cold-read-69fc082.md` precedent
read in reverse: only two of the ten members were read end to end at this subject; the other
eight are **covered by citation**, which I verified rather than accepted (§2).

**Standing instructions read.** `…/v3-harness-review-contract.md` (the stub, 5 lines) →
`ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` in full, both sides, per the stub's
*"It is your standing instruction and its own counterpart; read all of it"*.
`ResearchSystem/HARNESS-DECISIONS.md` `§live` read in full as `E10`'s tail requires (`HD-49`,
`HD-50`, `HD-47`, `HD-44`, `HD-41`, `HD-36`, `HD-35`, `HD-34`, `HD-23`, `HD-9`) plus the file
header; from `§implemented`, `HD-38`, `HD-20`, `HD-5` by section, because claims I checked cite
them. Cited by section, never by blob, per that clause.

---

## 1. Subject, re-derived

```
$ git rev-parse --show-toplevel
D:/Thesis-stage-control-refactor/ResearchSystem/harness

$ git rev-parse HEAD
48b6c5f290320c7a7fe3bd53d48de7f6bb6f7bbd

$ git status --porcelain
(no output)

$ cat .harness/review-pending.json
{
 "subject": "48b6c5f290320c7a7fe3bd53d48de7f6bb6f7bbd",
 "dispatched_at": "2026-08-19T15:12:29+00:00"
}
```

Subject = branch tip, worktree clean, marker subject = dispatched SHA, so `E9`'s window opened at
that timestamp and closes when this record's commit lands. Falsified from the moment this file is
written by exactly one path — this record, untracked until the orchestrator commits it.

**What stands between the cited read and this subject** — the range this read is paying for:

```
$ git log --oneline 69fc082..48b6c5f
48b6c5f V3-XREPO-REFS-AMEND-M1-v1
1cb80bb V3-XREPO-REFS-FREE-L1-v1
d8a83b3 V3-REVIEW-RECORD-XREPO-REFS-69fc082-v1

$ git diff --stat 69fc082 48b6c5f -- <the ten members>
 ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md | 7 +++++++
 ResearchSystem/document-harness/README.md                 | 2 +-
 2 files changed, 8 insertions(+), 1 deletion(-)
```

Three commits, of which one is the read record itself (`E9`: from dispatch to the record's commit
the branch takes no commit but the record — held, and the two that follow are the pair `E10`
opens, not round commits). Two member sites changed, and both are this read's subject:

- `48b6c5f` — the **must-fix amendment**, `E10`'s must-fix channel, the finding having supplied
  the class and the sites and the executor the bytes (`HD-36` ①). Verified §3.
- `1cb80bb` — a **free-channel** application, its own commit per `HD-38`, answering the cited
  read's `L-1`; *"riding the next read of this layer at per-member digest cost"* is this read.
  Verified §4.

## 2. The member set, and each member's blob

The set is `E10`'s own enumeration read **at the subject blob**, never from the dispatch: ten
paths, and the sentence's self-count *"exactly these ten paths and nothing else"* reconciles with
the enumeration by hand. `E10` makes citation depend on these ids, so each is stated.

| # | member | blob at `48b6c5f` | vs `69fc082` | how read |
|---|---|---|---|---|
| 1 | `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` | `91556fd342932380469727133a4ea8460634b974` | **changed** (`48b6c5f`) | full, 219 lines |
| 2 | `ResearchSystem/document-harness/README.md` | `be4766fc1496b41eb6d8f0b3c0f50acb698fd934` | **changed** (`1cb80bb`) | full, 40 lines |
| 3 | `ResearchSystem/document-harness/EXECUTION.md` | `4a7b6eca3e8f4fd43c2887005c44a5e616d8b5da` | unchanged | citation + probes |
| 4 | `ResearchSystem/document-harness/REVIEW.md` | `3350bfac1b190cb1dac8566247f5382a7136f094` | unchanged | citation + probes |
| 5 | `ResearchSystem/document-harness/ORCHESTRATION.md` | `82f10c1bd173fb795c723df072a6357287d4d366` | unchanged | citation + probe |
| 6 | `ResearchSystem/migration/…/v3-harness-operating-contract.md` | `70f3e5dda9ce069489432a592a025b9da36cf0e0` | unchanged | citation + probe |
| 7 | `ResearchSystem/migration/…/v3-harness-review-contract.md` | `bc395e1c22af05aeacb0ed0b9813b66c8de75644` | unchanged | full (standing instruction, 5 lines) |
| 8 | `ResearchSystem/contract/…-v3-supersession-1.md` | `68031fa2ca31272e31da0d42a9a02189d28fcc21` | unchanged | citation + probe |
| 9 | `ResearchSystem/contract/…-v3-supersession-2.md` | `e1a2f26b1d8d323d11e900f8137dea222b6571c1` | unchanged | citation + probe |
| 10 | `ResearchSystem/schema/document-assurance-v3/paragraph-map.schema.json` | `09aa869962f592c2f86c9379be0ef3eb7d2232ff` | unchanged | citation |

**Citation checked, not accepted.** Rows 3–10 are byte-identical to
`v3-cold-read-69fc082.md`'s §2 table, which states *"all ten members were read end to end at this
subject, none by citation"* — so `E10`'s condition (*"a member whose blob is unchanged since a
recorded end-to-end read of it is covered by citing that record"*) is met for eight, and the
`git diff --stat` of §1 is the same fact from the other direction. Rows 1–2 are the subject and
were read in full at the subject blob; each was proven equal to its working-tree file
(`git hash-object` → `91556fd…`, `be4766f…` — **MATCH × 2**), so the bytes quoted below are the
subject's bytes.

`E2`'s frozen surface is untouched by this range: the diff of §1 names two paths, neither of them
one of `E2`'s three blobs or in the schema pack.

## 3. The amendment, clause by clause

The whole of it, `CONSTRUCTION-CHECKLIST.md:14–19`, inserted immediately after the choice-of-law
clause (`:9–12`) and before the *Rationale is deliberately absent* paragraph — a placement the
diff proves is a pure insertion, `7 +++++++` and nothing removed:

> **Where a cited commit id resolves.** A commit id cited in this file or in any other
> instruction-layer member (`E10`) that this repository does not have — `7011916` included —
> is a commit of the repository this one was extracted from; the root
> [`README.md`](../../README.md)'s *Where the bytes came from* names that repository and says
> why the history stayed there. A citation naming its own repository is read as written; a
> silent one means that one.

**3.1 Rule impact — none, re-derived not accepted.** The paragraph is inside the header
blockquote, above the `## Execution side` heading; no text inside `E1`–`E12` or `R1`–`R10`
changed, and the `E10` membership sentence is byte-identical (the diff touches only `:14–20`,
and the sentence lives at `:92–103`), so `E10-sync`'s per-touch obligation (`HD-22`) does not
fall due. The choice-of-law clause still names the retired contracts at `7011916` as the
reference of record; the new paragraph says which repository holds them and nothing more. That
is exactly the line `M-1` itself drew — *"Deleting or re-pointing the clause changes what a rule
requires and opens a round; labelling the id does not."* Independently, `HD-36` ② rules the
design test back out of the must-fix channel, so the amendment is safe on this axis twice over.

```
$ python -c "…; from hooks import layer_path_check as L; print(len(L.LAYER)); print([m for m in L.LAYER if not pathlib.Path(m).exists()])"
10
[]
```

**3.2 The link terminus resolves and says what the amendment says it says.**
`../../README.md` from `ResearchSystem/document-harness/` lands on the repository root's
`README.md`, which carries `## Where the bytes came from` at `:12`. That section names the
source — *"copied byte-for-byte out of `D:/Thesis` (worktree `D:/Thesis-stage-control-refactor`,
branch `document-work-assurance-v3`) at commit `e4ffa2b`"* — and states the history decision with
its authority: *"**History was deliberately not carried across** (`HD-40`, design §4)"*. The
route to the *why* resolves here too: `document-harness/split-design.md` carries
`## §4 切线机制（保历史 vs 从头）`. Both clauses of the amendment's second half hold.

**3.3 The universal claim, swept independently.** Scope declared (`HD-41` ①): every 7–40-char
hex token in all ten members at blob `48b6c5f`, unanchored so that an id inside a longer
backticked command cannot escape, each token resolved with `cat-file --batch-check` in **both**
repositories.

```
$ git grep -nEo "[0-9a-f]{7,40}" 48b6c5f -- <the ten members> | wc -l
24
```

| token | this repo | `D:/Thesis` | sites |
|---|---|---|---|
| `7011916` | missing | commit | checklist `:5`, `:10`, `:15`; both stubs `:4` |
| `cf51534` | missing | commit | supersession-2 `:32` |
| `ac1b383` | missing | commit | `EXECUTION.md:109`, `README.md:18`, `REVIEW.md:65` |
| `a22cca0` `838c413` `ddd773a` `a8af54c` `418b89c` `9ba9bbc` | missing | commit | `EXECUTION.md:249`, `:330`, `:376`, `:378`, `:404`, `:439` |
| `820b287` | missing | commit | `README.md:36` |
| `86defbc` | missing | commit | `EXECUTION.md:448` — **not in the cited read's §3.7** |
| `fef3a2e` | missing | commit | `REVIEW.md:45` ×2 — **not in the cited read's §3.7** |
| `6fd0ae3` | missing | commit | `EXECUTION.md:381` (labelled *caller*) |
| `0d73a5f` | **commit** | missing | `EXECUTION.md:380` (labelled *instrument*) |
| `b2dbdf75` `68031fa2` `e1a2f26b` | **blob** | blob | checklist `:43`, `:44` — `E2`'s frozen ids, and `E2` calls them blobs |

**The claim is true at every site.** Every token this repository lacks resolves as a **commit**
in `D:/Thesis`, and `git worktree list` run there confirms `D:/Thesis-stage-control-refactor` is
a worktree of `D:/Thesis` — the repository the root README names — so the amendment's terminus
and my resolution are the same repository, not two that happen to agree. The three blob ids are
correctly outside the sentence's scope word *commit id*, and this repository has them. The one
commit that resolves **here** is labelled, so no silent citation misroutes today.

**3.4 Reachability of the single-owner fix, re-derived.** The fix is one sentence at one owner
rather than fifteen per-site tokens (`HD-5`), which only discharges `E10`'s sweep obligation if a
reader at a site can find it.

```
$ git grep -n "CONSTRUCTION-CHECKLIST" 48b6c5f -- <the other nine members>
EXECUTION.md:13 · ORCHESTRATION.md:7 · REVIEW.md:8 · both stubs :3
```
plus `document-harness/README.md:27` (the *Construction-side rules* row). Six of the seven
site-carrying members link to the amended file from their own header or index row; **the
seventh, supersession-2, carries no link and no site-carrying member links back to it** — which
is also the one site the amendment may not write, `E2` freezing those bytes and `E10` sending
them to `HD-20`'s bank. The banking is correct; that the row does not exist yet is `O-3`.

**3.5 The one figure the commit body offers, re-run (`E3`).**

```
$ cd ResearchSystem/tooling && python -m pytest -q
733 passed in 98.54s (0:01:38)
```

Count exact against the body's `733 passed in 87.67s`; wall-clock differs as wall-clock does.

## 4. The free-channel byte at `1cb80bb`

The cited read's `L-1`: `document-harness/README.md:32` said the construction ledger is *"the
record side of the checklist below"* while the checklist row sits five rows **above**. The
applied phrase is *"the record side of the construction checklist (the *Construction-side rules*
row above)"*. All three clauses hold: the *Construction-side rules* row is `:27` and `:27 < :32`;
that row is the one that links `CONSTRUCTION-CHECKLIST.md`; and `CONSTRUCTION-LEDGER.md`'s own
header states the same relationship in the same words — *"the record side of
[`document-harness/CONSTRUCTION-CHECKLIST.md`] … which is the rule side"*. The read named the
content (*"'above', or naming `CONSTRUCTION-CHECKLIST.md`"*); the applied bytes do the first and
point at the row that does the second, which is inside what `E10`'s free channel admits.

`E10`'s conditions on that channel, checked: own commit (`HD-38`) ✓, one member and one line ✓,
adds no clause ✓, not a path `E2` freezes ✓, reported after the fact and reversible ✓, and *"no
round has relied on the text"* — consistent with §1, where the range holds no candidate commit.

## 5. Findings

### `L-1` (low) — the amendment's *"read as written"* exemption misroutes the layer's only labelled cross-repo citation

The paragraph's last sentence carves an exception out of its own rule: *"A citation naming its
own repository is read as written."* The layer has exactly one commit citation naming a
repository it does not itself live in — `EXECUTION.md:381`, *"its bases: instrument `0d73a5f`,
caller `6fd0ae3`"* — and **`caller` is a role, not a repository**. On this machine it resolves to
`D:/Thesis`, correctly. For any second caller — the reader the split exists to serve (`HD-34`,
`HD-50`) — *read as written* resolves `caller` to **themselves**, where `6fd0ae3` is missing
(§3.3). The paragraph's first sentence would have routed that site correctly; the last sentence
exempts it and sends it the wrong way.

The amendment's own commit body identifies the defect and then ratifies the form that carries it:
*"the layer's demonstrated token form ('caller `6fd0ae3`') is false for any second caller — their
repository does not hold these commits either."* That reasoning is why the executor rejected
per-site tokens; it applies with equal force to blessing the one token already there.

*Why low and not must-fix.* It does not bite today, and the accurate fact is recoverable from
adjacent text under `R9`: the same sentence says *"across both trees"*, and the amendment's own
link now puts the root README — which names exactly one other repository — one hop from the
reader. **Deadline (`R10`): the first external caller**, i.e. the moment `HD-50`'s R2–R4 or any
onboarding puts a second repository in the position of reading `EXECUTION.md:381`. That moment is
not inside the pair that writes this row.

*Bytes deliberately not supplied.* Two fixes are available and they are not the same size:
qualifying the exemption (*"…naming its own repository by name"*) versus relabelling the site
(`EXECUTION.md:381`, an unchanged member outside this pair's reach). Whether either replaces text
*so that what the paragraph directs changes* — `E10`'s design test — is the question, and
`HD-36` ② settles it only for the must-fix channel, which this finding is not in. Naming a
tiebreak myself would add the bound (`R5`).

### `L-2` (low) — the command that could falsify the amendment's claim left no output in the repository

`E3`'s last sentence is unconditional: *"A factual assertion written into instruction text runs
the command that could falsify it first, **output kept in the commit body or the round
journal**."* `HD-41` ④ says the same for finding fixes and names the check its 后果 line makes
possible: *"commit 正文里有没有 grep 输出"*. The amendment writes a universal factual assertion
into instruction text; the sweep was run; **its output is in neither place**. The body reports
figures and says the evidence was *"pasted in the executor's report"* — chat-only material, which
`R2` names a finding in its own right. There is no `XREPO-REFS` journal (`ls` on both journal
directories, §6).

*Downstream decision that goes wrong (`R9`):* the next reader of an amendment cannot see whether
the class sweep ran and must re-run it to find out — which is what this read did (§3.3), and what
`HD-41` ④ exists to make unnecessary. Nothing factual was lost: the sweep reproduces, and it
reproduces *wider* than the body reports.

*No appliable bytes* — a commit body cannot be edited (`E8`: new commits, never amend). The value
is precedent for the next amendment, so this banks rather than rides.

### Observations

- **`O-1` — the commit body misattributes three of the read's fifteen sites.** It says *"three of
  the read's fifteen were never in the class on re-derivation (`b2dbdf75` / `68031fa2` /
  `e1a2f26b` are blobs resolving in both repositories)"*. The cited read's §3.7 table lists twelve
  tokens and **none of them is a blob id**; its fifteen are 17 sites minus the two labelled ones,
  and enumerate to `7011916` ×4, `ac1b383` ×3, `418b89c`, `820b287`, `838c413`, `9ba9bbc`,
  `a22cca0`, `a8af54c`, `cf51534`, `ddd773a` = 15 exactly. The three blobs were never in that
  count. The disposition arithmetic downstream of the clause is unaffected — 15 − 1 banked = 14
  covered is right for the read's own fifteen. Record-side, and a commit body cannot be edited;
  recorded so the trace exists, with no action proposed (precedent: `v3-cold-read-69fc082.md`
  `O-4`).
- **`O-2` — the sweep is two sites wider than either the read or the body says, and the
  single-sentence form is why that costs nothing.** `86defbc` (`EXECUTION.md:448`) and `fef3a2e`
  (`REVIEW.md:45`, twice) are in-class by §3.3's own test and appear in neither the read's §3.7
  table nor the body's disposition. Both are review-record **filenames** carrying a subject SHA
  (`v3-review-full-86defbc.md`), which is how they escaped a standalone-token pattern. They are
  covered by the amendment as written, so the general sentence absorbed two sites a per-site
  labelling fix would have left for the next re-read to find — the outcome `HD-36` ①'s sweep
  clause is for. What the sentence does not settle is whether a SHA embedded in a record filename
  is *"a commit id cited"* at all; `REVIEW.md:45` is already filed under rider
  `layer-outbound-refs` as a broken link, so the two classifications now overlap on one site.
- **`O-3` — the one banked site has no row at this subject.** The body declares
  supersession-2 `:32`'s `cf51534` banked under `HD-20`;
  `git grep "cf51534\|xrepo\|XREPO\|crossrepo" -- ResearchSystem/HARNESS-RIDERS.md` returns only
  the unrelated `layer-crossrepo-token` row. Banking is closeout work the orchestrator has not
  reached, so this is a note and not a defect — but it is the **only** site of the swept class
  that the amendment does not cover, and if closeout does not write the row it has no home in any
  file. `R10`'s shape for it: target = supersession-2 `:32`; redeem-when = `E2`'s recorded ruling
  for those bytes.
- **`O-4` — `M-1`'s second-caller half is untouched, as `M-1` said it would be.** The amendment
  gives a reader *a statement of where the commit lives*; the statement's terminus identifies that
  repository as `D:/Thesis` — a filesystem path on one machine, in a repository whose own root
  README says *"**No remote.** The caller creates it."* So a second caller can now reach the
  statement and still not the commit. `M-1` routed exactly this to the user under `R5`
  (*"whether the reference of record should be reachable from the instrument at all"*), and it
  stays there: the amendment stayed on the labelling side, which is the side `M-1` said did not
  open a round. Reported as shape, not as conclusion.

## 6. Coverage, and the ceilings on it (`R4`)

**Read in full:** `CONSTRUCTION-CHECKLIST.md` (219 lines) and `document-harness/README.md`
(40 lines) at the subject blob; the repository-root `README.md` (99 lines, the amendment's link
terminus, not a member); `HARNESS-DECISIONS.md` `§live` plus header; `v3-cold-read-69fc082.md`
in full (the record this read cites for eight members and answers for one finding); both commit
bodies of §1 in full.

**Read to settle a specific claim, not in full:** `EXECUTION.md:370–385` and `:444–452`;
`REVIEW.md:43–47`; `CONSTRUCTION-LEDGER.md` header; `split-design.md` section headings;
`HARNESS-RIDERS.md` by grep for the banked token; both journal directory listings;
`layer_path_check.LAYER`.

**Probed only (blob-equality plus targeted grep, per §2's citation route):** members 3–6 and
8–10 — `git grep` for `CONSTRUCTION-CHECKLIST` and for the hex-token class across all ten.

**Ceilings, stated rather than folded into supported:**

- The whole of §3.3's right-hand column and `L-1`'s consequence rest on **the worktree
  `D:/Thesis-stage-control-refactor` on this machine at this moment**. That `7011916` and the
  other fourteen tokens are absent *here* is a property of this repository; that they are present
  *there* is a statement about one machine, and the amendment's claim inherits that ceiling —
  which is `O-4` from the other side.
- **`UNVERIFIABLE`:** whether `D:/Thesis` at `e4ffa2b` is the source of these bytes. `git worktree
  list` proves the worktree relationship; byte-identity of the 254 files against `e4ffa2b` is the
  root README's claim and I did not re-derive it, this read's subject being seven lines of header.
- Members 3–6 and 8–10 were **not** re-read end to end; their coverage is `E10`'s citation route,
  whose precondition (blob unchanged since a recorded end-to-end read) I verified two ways (§2).
  Any defect in those members that `v3-cold-read-69fc082.md` missed is missed here too.
- `L-2` reports that the sweep output is absent from the repository. That the sweep *was run* is
  the body's claim and I neither verified nor disputed it — I ran my own, which is the only reason
  §3.3 is evidence rather than a second report of someone else's.
- Process claims — fresh context, that nothing reached me but the dispatch — are marked, not
  verified. `R2`'s derive-everything rule was followed: the member set came from `E10`'s sentence
  at the subject blob, the citation coverage from `git diff`, every count from a command run here.

## 7. Already on the books, not re-filed

- Riders `layer-crossrepo-token`, `layer-outbound-refs`, `frozen-path-prefix`, `E10-sync`,
  `wl-route` — read, standing, none redeemed by this range.
- `v3-cold-read-69fc082.md`'s `L-2` (one round applying `HD-38` both ways) and `O-1`–`O-4` stand
  unchanged at this subject; `L-1` is redeemed (§4) and `M-1` is answered (§3).
- `EXECUTION.md`'s figures pinned to revisions this repository lacks remain `UNVERIFIABLE` here
  and the text says so (`HD-41` ③).
