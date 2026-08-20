# VERIFY review — round `E10-D-NARROWING` (repair `440e205`)

| | |
|---|---|
| round | VERIFY, construction-side (`CONSTRUCTION-CHECKLIST.md` E1–E12 / R1–R10) |
| subject | `9dcb783218739defff0facd9c796e6fd51a53499..440e205878776954c5e8009e13dc4cfd22a544e6` |
| range content | two commits — `120e8ec` (kind: record), `440e205` (kind: review fix) |
| **verdict** | **`REVIEWED_NO_BLOCKER`** |
| findings | 1 low, 2 observations |
| record | this file; the execution side commits it (`R6`) |

The repair is a whole withdrawal, and it is byte-exact. Both accepted blockers close, and they
close for the reason the fix claims rather than by assertion — I read the restored text, I did
not accept the claim. The one low is about what this round leaves *outside* the repository,
not about the bytes it restored.

## 1. Subject, re-derived (`R2`)

Handed one range and nothing else. Every figure below is emitted by the command that produces
it; no reported number accepted.

```
$ git rev-parse HEAD              -> 440e205878776954c5e8009e13dc4cfd22a544e6   (== subject tip)
$ git rev-parse --abbrev-ref HEAD -> document-work-assurance-v3
$ git status --porcelain          -> (empty)
$ cat .harness/review-pending.json
  {"kind": "construction-round",
   "subject": "9dcb783…..440e205…",
   "dispatched_at": "2026-08-03T14:51:15+00:00"}
```

Commit times, UTC, re-derived (`git show -s --format=%cd --date=iso-local` under `TZ=UTC`):

| commit | UTC | kind (from body) |
|---|---|---|
| `c8d9afa` | 2026-08-03 13:01:16 | record (the `22b27aa` read) |
| `9dcb783` | 2026-08-03 14:19:03 | candidate |
| `120e8ec` | 2026-08-03 14:37:22 | record (the FULL) |
| `440e205` | 2026-08-03 14:51:06 | review fix |

Changed paths across the range, classified by hand:

```
$ git diff --name-status 9dcb783 440e205
A  ResearchSystem/migration/document-work-assurance-v3/v3-review-full-9dcb783.md   (+325)
M  ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md                       (7 +, 7 -)
```

One record file under `migration/`, one instruction-layer member. No code, schema, test,
generated surface or product-run artifact.

**Which leg this is.** A valid independent FULL for round `E10-D-NARROWING` exists —
`v3-review-full-9dcb783.md`, committed at `120e8ec`, verdict `CHANGES_REQUIRED`. So by `E9`'s
test the answer is *yes*, `440e205` is the round's one user-approved fix, and this dispatch is
the VERIFY that fix obliges. Verdict set is `REVIEWED_NO_BLOCKER | SPEC_GAP` (`R3`).

**Not the `E10` read, and none is owed.** `E10` requires an amendment to pass an independent
read before any round relies on it. There is no longer an amendment: §2 shows the layer file
returns to its pre-round blob. The fix body says the same and draws the same consequence.

## 2. The repair, led (`R3`) — is the withdrawal real?

### 2.1 Byte-exactness, established by blob identity

```
$ for r in c8d9afa 9dcb783 120e8ec 440e205; do
    git rev-parse $r:ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md; done
c8d9afa  2108635ff2ba0b42e980e22f89e32cddcdaeba21
9dcb783  1836d4562c50f30720f4fc23b84f6837dd5c7361
120e8ec  1836d4562c50f30720f4fc23b84f6837dd5c7361
440e205  2108635ff2ba0b42e980e22f89e32cddcdaeba21

$ git diff c8d9afa 440e205 -- …/CONSTRUCTION-CHECKLIST.md
(empty)

$ wc -l …/CONSTRUCTION-CHECKLIST.md   -> 164
```

The file at the repair is the same blob as at the pre-round base. The commit body's blob claim
is correct.

### 2.2 Nothing else moved — the whole tree, not the declared boundary

```
$ git diff --stat c8d9afa 440e205
 .../v3-review-full-9dcb783.md | 325 +++++++++++++++++++++
 1 file changed, 325 insertions(+)
```

The **entire** net effect of round `E10-D-NARROWING` on the repository is one added review
record. This is a stronger statement than "the round stayed inside its boundary", and it is
the one that settles `E2`: no frozen path can have moved, because no path moved. Positive
spot-check of the surface this round orbited: `git ls-files
ResearchSystem/schema/document-assurance-v3/ | wc -l` → **15**, and
`paragraph-map.schema.json` is present — the 2026-08-03 re-baseline count, intact.

### 2.3 No dangling reference to the withdrawn wording

```
$ grep -rn "deleting a rule outright" .
./ResearchSystem/migration/document-work-assurance-v3/v3-review-full-9dcb783.md:102
```

The single surviving occurrence is inside the FULL record, where it is labelled as the
candidate's "after" text under a `CHANGES_REQUIRED` header. Nothing in the repository presents
the narrowed test as live.

### 2.4 B-1 — closed, and for the stated reason

The FULL's B-1 was that withdrawing the broad arm stranded the `or a bound` gloss, which had no
other anchor. Restored text at HEAD, lines 94–97:

> *…once one has, changing it opens a round; an amendment adding a clause to any rule, **or
> replacing or deleting text so that what a rule requires changes**, is design and opens a
> round; when the free channel and the design test both apply — the named literal replacement
> itself adds a clause **or a bound** — design wins and the round opens;*

A bound-adding literal replacement changes what the rule requires, so the broad arm reaches it,
so the collision clause's stated premise ("both apply") is satisfiable, so the gloss has work to
do. The two-way reading the FULL identified is gone. **Closed.** I verified this by reading the
restored clause, not by re-deriving the FULL's `feacb86` / `8ec4c60` citation chain — see §5.

### 2.5 B-2 — moot, and the fix says so without claiming more

B-2 was that the narrowed test still plausibly caught `22b27aa` through its surviving clause-add
arm, leaving the round's purpose unestablished. The narrowed test no longer exists (§2.3), so the
question it posed cannot arise. Under the restored broad arm, `22b27aa` is caught exactly as
`retro-2026-08-03.md` §7 ruling 6 states — *"该 amendment 改变了规则要求，按 `E10` 欠一次独立
read"* — and M-1 therefore stands undischarged.

The fix body records precisely that: *"M-1 against `22b27aa` stands undischarged, and the next
action is remedy (a) … not P5B."* That is the honest reading. **Closed by withdrawal**, with the
round's stated purpose abandoned rather than achieved, and the abandonment written down.

### 2.6 O-2 — moot, verified against the bank

`HARNESS-RIDERS.md` at HEAD holds five rows — `F-c`, `O-2b`, `SCC`, `RA`, `CLI-hist` — and no
`F-1r`. The file is untouched across the range (§2.2). Since `F-1r`'s redeeming text is restored
verbatim, no row is owed and `R10`'s missing un-redemption path is not exercised. **Moot.**

### 2.7 O-3 — still live at HEAD, correctly deferred, deadline now nameable

`HARNESS-LEDGER.md:33–37` at HEAD still presents P5B precondition ① as awaiting the dispatch
`rsc v3 dispatch --read 22b27aa`. That read returned at `c8d9afa`. The fix body names this the
round's closeout obligation, and the precedent supports the deferral — both prior closeouts
(`79787a7`, `1728997`) touched `.goals/LEDGER.md` + `ResearchSystem/HARNESS-LEDGER.md`, so
closeout is the established leg for ledger repair.

What I add: under `R10`, a finding whose value expires must carry the moment it starts to bite.
That moment is **the next session's first read**. The ledger is the documented entry point for
this track, and a fresh session following it would re-dispatch a read that has already returned
and been superseded — while the actual next action, remedy (a), appears nowhere in it. **Open,
owed at closeout.**

### 2.8 Guards

Nothing in this range adds, removes or alters a guard, so `E4` / `R8` mutation duty does not
arise. Re-run at HEAD:

```
$ python ResearchSystem/tooling/hooks/ledger_cap_check.py    -> exit 0
$ python ResearchSystem/tooling/hooks/layer_path_check.py    -> exit 0
$ python ResearchSystem/tooling/hooks/review_freeze_check.py -> exit 0
$ python Thesis/Work/Tooling/repo-audit.py                   -> RESULT: clean (exit 0)
```

**Marked, not verified (`R4`):** these ran against an empty index and confirm the current tree,
not a replay of the staged state at `14:51:06Z`. The body's *"each exit 0 over the staged
revert"* and *"`git diff --cached c8d9afa` over that path is empty"* are process claims with no
evidence lock available to me.

## 3. Boundary and record conformance — second (`R3`)

| requirement | state |
|---|---|
| `E2` frozen bytes | ✓ whole-tree diff `c8d9afa..440e205` = one added file; no frozen path in it. Schema pack = 15 files |
| `E3` blob assertion in the fix body | ✓ re-derived independently (§2.1) |
| `E3` guard-exit assertions | process claims, marked (§2.8) |
| `E8` explicit paths, no `add -A` | ✓ one file per commit |
| `E8` new commits, no amend | ✓ `440e205→120e8ec→9dcb783→c8d9afa`, linear |
| `E8` no push | ✓ `git rev-list --count origin/main..HEAD` = 428 (FULL recorded 426; +2 = this range) |
| `E8` inside declared boundary | ✓ only `E10`'s paragraph moved, and it moved back |
| `E8` title | ✓ `V3-E10-D-NARROWING-REVIEW-FIX-v1`; leg-suffix matches precedent (`…-CLOSEOUT-v1` at `79787a7`, `1728997`) |
| `E8` one dense paragraph, no trailers | ✓ body = 35 lines, one trailing blank, `%(trailers)` empty |
| `E8` kind named | ✓ "Kind: review fix" / "Kind: record" |
| `E9` budget | ✓ one FULL (`120e8ec`), one fix (`440e205`), this VERIFY. No commit between the FULL's dispatch (14:19:25Z) and its record (14:37:22Z) but the record |
| `E12` handoff | ✓ one range, no per-acceptance argument |
| `R6` record channel | this file, `v3-review-verify-440e205.md` |
| `R10` bank | ✓ untouched, five rows |

## 4. Findings

### Low

**V-1 — the round's load-bearing rulings and the measurement it calls its own durable finding
exist nowhere in the repository, and the recorded closeout obligation does not include them.**

Three items are load-bearing for this round and are attested only by the commit bodies that rely
on them:

1. the 2026-08-04 ruling selecting remedy (c) — already raised as an `R7` ceiling by the FULL §2;
2. the 2026-08-04 authorization to spend the fix leg on **withdrawal** rather than on either
   minimum fix the FULL wrote;
3. the *"a read and a FULL cost about the same"* measurement, which the fix body calls **"the
   durable finding of this round"** and routes to *"the queued I/O design batch."*

What the repository shows:

```
$ grep -rn "E10-D-NARROWING\|2026-08-04" --include='*.md' --include='*.json' ResearchSystem/ .goals/
  (only hits: an unrelated earlier round, V3-PHASE-C1.5-DIGEST-NARROWING)
$ grep -n "撤回\|withdraw\|E10.*narrow" ResearchSystem/HARNESS-LEDGER.md
  (none)
$ head -1 .harness/runs.jsonl | python -c "…print(list(d.keys()))"
  ['ledger_schema_version','ts','repo','repo_path','branch','commit_before','git_dirty',
   'subsystem','stage','decision','tools_used','agents_used','files_changed','edit_count',
   'turn_summary','run_id']
$ grep -o '"[a-z_]*token[a-z_]*"' .harness/runs.jsonl | sort -u   -> (none)
```

`HARNESS-LEDGER.md`'s own header (lines 11–12) states what belongs in it: *"the current pointer
… and **the user rulings that exist nowhere else**."* All three items meet that description and
none is there. The machine trail carries no token or cost field, so item 3 is not recoverable
from it either.

**Ground truth it sits against.** `retro-2026-08-03.md` §7 ruling 2 records the opposite state as
an explicit honesty boundary: *"**诚实边界：FULL 自身的 token 成本从未被测量过**——169 万全是
pre-START audit."* Item 3 is a new measurement that would close exactly that gap, asserted with
no figure, no method and no date. The checklist is silent on how a claim like this must be
recorded, so per its own header the retired contract at `7011916` is the reference of record;
its §6.2 says: *"For every present-tense factual claim in a record: which test locks it? If
none, and no node is assigned to verify it — finding."* Nothing locks it and no node is assigned.

**Why this is not wording-level (`R9`).** The accurate fact is not recoverable from adjacent text
or any committed record — that is what the greps above establish. Downstream decisions that go
wrong, each with its deadline:

- **Next session's first read** — a session entering by the ledger sees a superseded dispatch as
  the live next action (§2.7) and no trace of why the round it is standing on ended in a
  withdrawal.
- **When the I/O design batch opens** — that batch is told to carry item 3 forward. With no
  figure recorded it must either re-measure, in which case the round's designated durable output
  bought nothing, or re-design the read/FULL channel split on an unreproducible number that a
  committed evidence file contradicts.

**Minimum content — not bytes.** I cannot supply the text: only the user holds the rulings and
the figures. At closeout, record in `HARNESS-LEDGER.md`'s rulings section (a) the 2026-08-04
selection of remedy (c), (b) the 2026-08-04 authorization to spend the fix on withdrawal, and
(c) the read-vs-FULL cost comparison with whatever figure and method exist — or, if no figure
exists, state it as an estimate rather than as *"a measurement."*

**Routing is not mine.** `R10` routes lows from *reads*, and describes a FULL returning
`REVIEWED_NO_BLOCKER` with lows; it says nothing about a VERIFY's lows, and the fix leg is
already spent. The two live routes are the closeout commit — which already owes O-3 on the same
file, so the surface is being touched anyway — or the bank. The choice is the user's.

### Observations (`R5` — reported; the conclusions are the user's)

**V-2 — this round spent its entire `E9` budget to return the repository to its starting
state.** One FULL, one fix, one VERIFY, and a net instruction-layer diff of zero (§2.2). The
durable output is two review records and three commit bodies. `R5` and the retired contract §10
tell me to report the *ratchet* shape — successive rounds adding components to close findings.
This is the mirror image and I report it under the same clause: it is the second consecutive
round on one clause (`feacb86` broadened `E10`'s design test; this round narrowed it and then
withdrew), and the FULL had already attached `E6`'s signal — that closing B-1 and B-2 cleanly
tends toward *defining* "adding a clause", i.e. adding a clause. Whether that clause is worth a
third round, or whether `E6` applies to the design test itself, is the question I structurally
cannot answer.

**V-3 — the withdrawal restores the text but not the position.** `E9`'s budget for round
`E10-D-NARROWING` is now exhausted, and the work M-1 named is unstarted: the fix body's *"the
next action is remedy (a) — a round whose subject is `22b27aa`'s layer diff"* is a new round, not
a continuation of this one. Recorded so that the next session does not read the closed budget as
a closed obligation. This is a consequence of the round, not a defect in the repair.

## 5. Coverage disclosure (`R4`)

**Read in full:** the subject diff and all three commit bodies (`9dcb783`, `120e8ec`,
`440e205`); `v3-review-full-9dcb783.md` (326 lines); `CONSTRUCTION-CHECKLIST.md` at HEAD (164
lines); `HARNESS-LEDGER.md` (112 lines); `HARNESS-RIDERS.md`; the `v3-harness-review-contract.md`
stub; `retro-2026-08-03.md` lines 1–20 and 56–159 (§0 partial, §3–§7 whole).

**Sampled at cited lines:** the retired review contract at `7011916` — §4 verdicts, §5 procedure,
§6 hunt list, §10 ceilings (lines 145–200, 260–300) and a `verify` grep across the file; prior
closeout commits `79787a7` / `1728997` at `--stat` only.

**Probed only:** the four guards, by exit code — none of their sources read this round;
`.harness/runs.jsonl`, first-record keys plus a field grep, not read; `retro-2026-08-03.md`
§1–§2 (lines 21–55), not read.

**Not read, and not claimed:** `v3-review-full-feacb86.md` and `v3-review-full-8ec4c60.md`. The
FULL's B-1 rested on a citation chain through those two records; I did **not** re-derive it.
B-1's *closure* does not depend on it — closure turns on whether the restored clause is coherent,
which I read directly at §2.4 — but the FULL's account of *why* the gloss exists is carried
here on the FULL's authority, not re-verified. The other eight `LAYER` members were not read;
the range's diff against them is empty, so no blob-citation discharge was needed or attempted.

**Process claims marked, not verified:** the `E11` preview card; the 2026-08-04 authorization;
"guards exit 0 over the staged revert" and "`git diff --cached` empty" at commit time (§2.8).

**`UNVERIFIABLE`, stated as such rather than folded into supported:** whether the read-vs-FULL
cost comparison is accurate, and whether withdrawal was the authorized *shape* of the fix rather
than the executor's own election within a broader authorization. Neither is recoverable from the
repository (§4 V-1). Neither endangers the repair — the withdrawal restores a known-good prior
state and is safe under any cost model — which is why V-1 is a low and not more.

## 6. Next action

`REVIEWED_NO_BLOCKER`. `E9`'s budget for round `E10-D-NARROWING` is spent; closeout is the
remaining leg. Owed at closeout: O-3 (§2.7), and the user's route for V-1 (§4). M-1 against
`22b27aa` is undischarged and belongs to a new round, not to this one.
