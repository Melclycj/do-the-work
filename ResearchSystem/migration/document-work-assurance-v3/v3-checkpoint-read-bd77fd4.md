# Instruction-layer read — `bd77fd47a5cbf0cf3e929e3a70a1f66fabbbb7ba`

`E10` read of the instruction layer at `bd77fd4`. Not a round: no verdict, no budget consumed
(`R3`). It discharges the independent reads owed for the four amendments outstanding since the
last end-to-end layer read (`v3-checkpoint-read-a5a04c3.md`, 2026-08-05): `55fe4e9` (C1 — `E2`
retires the signed plan blob), `cfc6a91` (decision-log round — `README.md` leg), `85c1225`
(route-b) and `45858d5` (rider redemption). It also answers the one question both the route-b
commit body and the ROUTEB-REDEEM FULL (`v3-review-full-065a9b8.md` §4.5) left expressly to
this read: whether `fd058aa`'s superseded text still owes a read of its own (§3 — it does not).

**Findings: 0 must-fix, 1 low, 2 observations.** The four amendment texts say what their
recorded rulings say; every factual assertion I could falsify reproduces at the subject; the
nine-path enumeration is item-for-item and order-for-order equal to both code pins; no member
is left holding a statement the amendments falsified; and no round or product run relied on any
of the four texts before this read, so it lands before `E10`'s deadline, not after it. The low
is a genuine silence in the new (b) obligation sentence: whether the opening waiver reaches the
`§live` read is unstated on both carriers, and the two readings diverge on an action.

## 1. Subject, re-derived (`R2`)

Handed one SHA and the phrase *an E10 read*. Everything below is re-derived from the
repository; no figure is taken from the dispatch prompt, the ledger, the commit bodies, or the
round's own FULL.

```
$ git rev-parse HEAD              -> bd77fd47a5cbf0cf3e929e3a70a1f66fabbbb7ba
$ git status --porcelain          -> (empty)
$ cat .harness/review-pending.json
  {"subject": "bd77fd47a5cbf0cf3e929e3a70a1f66fabbbb7ba",
   "dispatched_at": "2026-08-08T14:37:04+00:00"}
```

HEAD **equals** the subject and the tree is clean, so worktree reads are reads of the subject
bytes; dispatch (14:37:04Z = 00:37+10:00) post-dates the tip commit (00:21+10:00) by 16
minutes, and the branch has taken no commit since — this record is the first it admits (`E9`).
The subject commit itself (`V3-ROUTEB-REDEEM-FIX-B1-v1`) writes `HARNESS-LEDGER.md` and
`HARNESS-RIDERS.md` only — no member — so the layer state below is the ROUTEB-REDEEM range's.

`E10`'s sentence **at the subject blob** governs the member set: nine paths, closed with "and
nothing else". The decision log is named inside the bullet but expressly as a non-member
("It is not a member"), so the set stays nine and decidable by reading the membership sentence.

| # | blob at `bd77fd4` | lines | member | since the last end-to-end read |
|---|---|---|---|---|
| 1 | `44d622b9` | 182 | `document-harness/CONSTRUCTION-CHECKLIST.md` | **changed** (`4d0c7330` → here via `55fe4e9`·`fd058aa`·`85c1225`·`45858d5`) — read end to end here; also this session's standing instructions |
| 2 | `dd1c7c3e` | 38 | `document-harness/README.md` | **changed** (`ae887dd4` → `70bd9f0b` at `a1fad7e`, read end-to-end per `v3-review-full-f4e1be1.md`; → here at `cfc6a91`) — read end to end here |
| 3 | `810f5081` | 171 | `document-harness/EXECUTION.md` | **changed** since `a5a04c3` (SIMP-A4: `37804a6`/`a1fad7e`/`8dae1e0`); blob named and verified read end-to-end in `v3-review-full-f4e1be1.md` — **also read end to end here**, which moots the journal-vs-record citation question that FULL had to litigate |
| 4 | `3350bfac` | 284 | `document-harness/REVIEW.md` | unchanged — cited to `v3-checkpoint-read-a5a04c3.md` §1 |
| 5 | `17ff31bb` | 5 | `migration/…/v3-harness-operating-contract.md` (stub) | unchanged — cited to `a5a04c3` |
| 6 | `52a97a48` | 5 | `migration/…/v3-harness-review-contract.md` (stub) | unchanged — cited to `a5a04c3`; also read here as the dispatch entry point |
| 7 | `68031fa2` | 124 | `contract/…-v3-supersession-1.md` | unchanged — cited to `a5a04c3` |
| 8 | `e1a2f26b` | 113 | `contract/…-v3-supersession-2.md` | unchanged — cited to `a5a04c3` |
| 9 | `09aa8699` | 44 | `schema/document-assurance-v3/paragraph-map.schema.json` | unchanged — cited to `a5a04c3` |

Blob ids from `git ls-tree bd77fd4`, line counts `wc -l` on `git show` at the subject
(`\n`-counts; blobs 7 and 8 equal `E2`'s frozen ids, as they must). The six unchanged rows are
byte-identical to `a5a04c3`'s table, which read all nine end to end — citation is valid for
members 4–9. The complete set of member-touching commits in `a5a04c3..bd77fd4`, classified by
hand, is exactly eight: the three SIMP-A4 commits (members 2–3, end-to-end read recorded in
`v3-review-full-f4e1be1.md`) and the five named above (`fd058aa` included; §3 disposes of it).
The ledger's two-blob binding (`HARNESS-LEDGER.md:94-96`, the durable `B-1` correction) is
therefore **re-derived here, not accepted** — and it reproduces: the checklist and README are
the only members whose current blobs no prior read record covers.

## 2. The four amendments against the repository (`E3`)

**`55fe4e9` — `E2` retires the signed plan blob.** The enumeration sentence drops
`8ad404b1…` and the count sentence changes "Four blobs and one directory" to "Three" in the
same commit — the dangling-neighbour shape the body cites is avoided. At the subject the
sentence enumerates exactly three blobs (`b2dbdf75…`, `68031fa2…`, `e1a2f26b…`) plus one
directory, so count equals enumeration; the pack directory holds exactly **15** files
(`git ls-tree bd77fd4 ResearchSystem/schema/document-assurance-v3/ | wc -l → 15`), matching
the re-baseline parenthesis it retains. The body's sweep claim reproduces: grepping all nine
members for `8ad404b1|b2dbdf75` returns one hit — `E2`'s own sentence — so no member restates
the freeze list.

**`cfc6a91` — the README leg of the decision-log round.** Two rows: the journal row narrowed
to analysis/reasoning/measurement (HD-1), and a new decision-log row. Both hrefs resolve at
the subject tree (`journal/checker-and-map-2026-08-05.md`,
`migration/…/journal/reform-2026-07-29.md`, `../HARNESS-DECISIONS.md`). The row's content
matches the decision log's own header mechanism sentence for sentence — supreme source of
truth, instruction text expands under it, conflict means the instruction text is wrong, cold
reads read `§live` and only `§live`, plan authors inherit live entries verbatim — and `HD-1`
exists (`HARNESS-DECISIONS.md:163`).

**`85c1225` — route-b.** The membership sentence returns to nine; route-(a)'s inserted clause
is deleted and `…paragraph-map.schema.json`. Its` is byte-restored; the new (b) obligation
sentence carries exactly what `HD-19` says it carries (not a member · no amendment machinery
reaches it · its own bytes are discipline (`HD-7`, exists at `:201`) · cited by section, never
by blob). The three-site discipline the rewritten `E10-sync` row demands was honored: the
membership sentence, `LAYER` and `EXPECTED` changed in the same commit and the body names all
three.

**`45858d5` — the rider round's two clauses.** The `E2`-exception clause sits inside the free
channel it restricts and covers the must-fix channel too; it carries `HD-20`. The
membership-question sentence carries `HD-21`, in the "membership sentence" wording whose
one-word deviation from the approved card the body disclosed with its reason. The `E10-sync`
row rewrite matches `HD-22` (no machine, per-touch discipline, deadline moved). Rider count:
18 → 16 in that commit, 17 at the subject after `bd77fd4` adds `R10-route` — recounted by hand.

**Membership, mechanically.** `layer_path_check.LAYER` and `LayerMembership.EXPECTED`
(`test_precommit_checks.py:189-199`) each list nine paths; compared item by item and in order
against the membership sentence's nine backticked paths — equal on all three legs. Both guards
run clean at the subject:

```
$ python ResearchSystem/tooling/hooks/layer_path_check.py   -> exit 0
$ python ResearchSystem/tooling/hooks/ledger_cap_check.py   -> exit 0
```

A naive token parse of the whole `E10` bullet now yields 10 path tokens — the (b) sentence
names the decision log — which is `HD-22`'s recorded ground for not building a prose parser;
the prose leg remains bound by nothing mechanical. Rider `E10-sync`, not re-reported. The
pin's bite was mutation-proven at `065a9b8` by the FULL's own probe (s1 removed from `LAYER` →
2 value-level failures); the two commits since touch no guard, no member, no test, so that
result stands and was not re-run here.

## 3. The `fd058aa` question, adjudicated as asked

Route-b's body: "`fd058aa` 的文本已被本轮取代、读它已无对象——**这是判断不是规则明写**，留给
下一次层 read 判." The FULL's §4.5 carries the same deferral. This is that read; the answer is
**no fourth read is owed**, on three grounds, each checked:

- **Zero residue.** The net member diff `a5a04c3..bd77fd4` for the checklist contains only the
  four amendments' surviving text: the two `E2` lines, the free-channel `E2` exception, and
  the (b) obligation + membership-question sentences. Nothing of `fd058aa`'s insertion (the
  ten-path sentence, the member clause, the archive clause) survives at the subject — the
  stale-vocabulary sweep (`Four blobs|ten paths|十成员`) returns zero across members 1–4.
- **Zero reliance.** `git log fd058aa..85c1225` contains exactly `7a08265` (A1 errata) and
  `2d833cd` (the A1 VERIFY record) — both are review *of* the amendment, which `E10`'s
  reliance definition excludes ("authoring, citing or recording it alone is not"). No round
  opened and no product-run commit landed in the window.
- **No remaining object.** The amendment read exists so text passes an independent read
  "before any round relies on it". Text replaced before any reliance can never be relied on;
  the read's subject — the amendment text itself — no longer exists, and its successor is
  exactly what this read reads.

Consequence: the outstanding set was exactly {`55fe4e9`, `cfc6a91`, `85c1225`, `45858d5`},
all four discharged here; the ledger's three-commit 盖-list plus the README leg was complete
and correct, and the route-b executor's "三笔" reading is confirmed.

## 4. What the amendments may have falsified elsewhere — swept

- **Cross-references.** `supersession-2:107`'s `E10` citation ("prose successor to signed
  text") still lands on vocabulary the enumeration holds. `README.md:29` is the only other
  member reference to the decision log and matches the (b) sentence. `EXECUTION.md`,
  `REVIEW.md`, both stubs and supersession-1 carry no reference to `E2`'s list, the free
  channel, or `§live` — nothing to go stale.
- **Reliance to date, the other direction.** `assurance/runs/` commits since `3657687` are
  the p5b-claims closure chain and HarnessIssue triage; none is governed by `E2`'s blob list,
  the `§live` obligation, or the channel exception, so no product run relied on the amended
  text before this read either.
- **`HD-21`'s question duty, exercised for the window.** Files that appeared near the layer
  since the last read: `HARNESS-DECISIONS-archive.md` (out-of-force entries only — claims no
  authority, not a member), the journal files (analysis only, HD-1), the A2/P5C plan files
  (inherit rulings verbatim, claim none). None triggers the membership question beyond the
  decision log itself, which the (b) sentence answers in place.
- **`EXECUTION.md` fresh read** (171 lines): the SIMP-A4 authoring-gate/lint paragraph is
  internally consistent with `README.md:34`'s description of the candidate-side lint (both
  state the lint judges work products only and why a specification is not one). No finding.

## 5. Process boundary — second (`R3`)

- **`E10` sequencing holds.** All four amendments took the design route and were reviewed:
  C1 under the A1 FULL, route-b and the rider round under the ROUTEB-REDEEM FULL
  (`CHANGES_REQUIRED`; its `B-1` fixed by `bd77fd4`'s ledger rewrite, ruled budget-free under
  the 2026-08-04 ledger/riders-only ruling with `HD-23` adjacent). None of those FULLs banks
  as the amendment read (`E10` forbids it); this read is that read, for all four, and §4 shows
  it lands before any reliance — deadline met, not merely deferred.
- **`E9`.** This read spends no budget and carries no verdict. Per `E9`'s occurrence rule it
  has occurred only when this record's commit lands; from dispatch to that commit the branch
  takes no commit but the record itself.
- **Boundary.** This session writes exactly one path — this record — and nothing else.

## 6. Findings

### Low

**L-1 — whether the opening waiver reaches the `§live` read is unstated on both carriers, and
the two readings diverge on an action.** Location: `CONSTRUCTION-CHECKLIST.md` at `44d622b9`,
`E10` `:109-116` ("a cold read of this layer is owed at each round's opening **unless the user
waives it**, and a member … is covered by citing that record …; one file outside this layer is
**nonetheless owed at that same opening** — …'s `§live` …") against `README.md` at `dd1c7c3e`
`:29` ("**every cold read** MUST read its `§live`"). Ground truth: the waiver clause attaches
syntactically to the layer cold read; the `§live` clause names no waiver of its own; the README
ties `§live` to cold reads that happen, which goes moot when one is waived; the decision log's
own header ("每轮 cold read 必读 §live") is silent the same way, so the outranking file does
not settle it. **Decision that goes wrong unfixed:** a round opens under a user waiver — one
session reads `§live` anyway (strict reading), another skips it citing the waiver (loose
reading); a skipped `§live` can miss a live ruling (`HD-23`'s budget criterion is one a fix
classification turns on), so the two sessions diverge on an obligation and on budget
accounting — an actor's action changes, which is why this is not wording-level under `R9`.
**No bytes are supplied, deliberately:** any clarifier adds a bound to `E10`'s obligation,
which the design test sends to a round. Per the 2026-07-29 routing a middle low without
appliable bytes **banks**. Redeem-when: the next batch touching `E10`'s cold-read /`§live`
sentences; **deadline: the first opening for which the user grants a waiver** — the moment the
divergence bites. Honest note: the checklist header tolerates silences whose answer the
retired contracts hold; they predate the decision log and cannot answer this one, which is why
it is reported rather than dropped.

### Observations (`R5` — reported; the conclusions are the user's)

**O-1 — the dispatch marker carries no `kind` field.** The `a5a04c3` layer-read marker
carried `"kind": "layer-read"`; this one carries subject and timestamp only. Nothing
load-bearing is chat-only — the read's kind is committed in the ledger's A-batch line — and
the freeze hook does not read the field; noted because process reconstruction loses one field
if the marker format regressed rather than the invocation differing.

**O-2 — where this read leaves the next opening.** When this record's commit lands, the
ledger's "A2 开工前唯欠一次 `E10` 层 read" binding is discharged and the line is due its
rewrite (execution-side bookkeeping, ledger-only). If the nine members are unchanged when A2
opens, that opening's cold read is covered by citing this record — the blob table is §1. The
`§live` read is not: it is owed fresh at each opening (and is where `L-1` waits).

## 7. Coverage disclosure (`R4`)

**Read in full at the subject:** members 1 (182), 2 (38), 3 (171), 6 (5, as dispatch entry
point); the complete diffs and bodies of `55fe4e9`, `fd058aa`, `cfc6a91` (README leg + stat),
`85c1225`, `45858d5`, `bd77fd4`; the net member diff `a5a04c3..bd77fd4`;
`v3-checkpoint-read-a5a04c3.md` (the citation source, all 243 lines);
`v3-review-full-065a9b8.md` (all 275 lines); `HARNESS-DECISIONS.md` header + `§live` complete
+ the `HD-19`/`HD-20`/`HD-21`/`HD-22` entries; `HARNESS-RIDERS.md` (28 lines, 17 rows);
`HARNESS-LEDGER.md` (121); the `LAYER` and `EXPECTED` tuples;
`v3-harness-review-contract.md`'s stub.

**Sampled:** `v3-review-full-f4e1be1.md` — the passages establishing `EXECUTION.md`'s
end-to-end read and blob id (`:278-286`, `:350-359`); `v3-review-verify-3b28116.md`
`:316-321`; commit dates via `git log --format`.

**Only probed:** the non-member commits in `a5a04c3..bd77fd4` — classified by title for the
member enumeration, not read; `assurance/runs/` commits since `3657687` — titles only, for
the reliance question; `HARNESS-DECISIONS-archive.md` — existence and role, not read;
member 5's stub — cited, not re-read this session.

**Not verified:** that this read ran in a fresh context — a process claim, marked (`R4`). The
preview cards, their approvals and any waivers are chat-only (`R7` — ceiling stated, not a
block). The executors' recorded probes (P1/P2, sha256-checked restores) were reviewed by the
ROUTEB-REDEEM FULL and are not re-run here; my only guard claim is the two exit-0 runs above
plus the FULL's mutation standing unchanged since `065a9b8`.

**Ceiling:** what is established is that the four amendment texts match their recorded
rulings, that every repository assertion checked reproduces at the subject, that the
enumeration equals both code pins, that no member holds a statement the amendments falsified,
that no reliance preceded this read, and that the amendment-read debt standing at the subject
is fully discharged by this record. What is **not** established: which reading of the waiver's
reach a future session will take (`L-1` — both have textual support); whether a
path-resolution scan is sufficient guarding for a prose charter (no one claims it — rider
`E10-sync`); and anything about the work the amendments govern, which `E10` expressly excludes
from this read's subject.
