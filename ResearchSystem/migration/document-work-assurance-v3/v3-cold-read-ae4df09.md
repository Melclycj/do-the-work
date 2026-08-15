# Instruction-layer read — `ae4df09d810ad24ea6e76043c94fe75b716f1757`

`E10` cold read of the instruction layer at the C2 opening. Not a round: no verdict, no
budget consumed (`R3`). Findings tiered must-fix / low / observation. This read also
discharges the layer-read debt `a6b87ad` recorded for its in-layer application — the ledger's
binding *"C2 开轮的 cold read 顺带清偿 `a6b87ad` 所欠的层内 read"* — at per-member digest
cost: the one member that application touched (`README.md`) is read in full below.

**Findings: 0 must-fix, 1 wording-level (rides under `R9`), 5 observations.** Every factual
assertion in the changed bytes was re-derived by command and holds: the §13 ground README
row 19 now cites exists verbatim in the signed contract, the row-20 catch-all is true of
every non-v3 file in the directory, and the two applied edits are byte-for-byte the fixes
`v3-checkpoint-read-403fc9a.md` L-1 and L-2 named. The rider bookkeeping around the
application conforms, including same-commit deletion of the redeemed row.

## 1. Subject, re-derived

`R2`: I was handed one SHA and the phrase *the instruction layer*. Everything below is
re-derived; no figure in the dispatch, the ledger or any prior record is accepted as reported.

```
$ git rev-parse ae4df09d810ad24ea6e76043c94fe75b716f1757 -> ae4df09d810ad24ea6e76043c94fe75b716f1757
$ git rev-parse HEAD                                     -> ae4df09d810ad24ea6e76043c94fe75b716f1757
$ git status --porcelain                                 -> (empty)
```

`E10`'s sentence at the subject commit governs the member set. Enumerated against the
repository: **eight** members. The open tail adds none — `git ls-tree -r ae4df09
ResearchSystem/contract/` shows exactly two supersessions; `git diff --name-only d58969d
ae4df09 -- ResearchSystem/schema/` returns 0 paths, so no schema `description` was amended;
the one new prose file since the last read chain, `migration/general-harness-v2/
General-Harness-v2-Design.md` (added `8497e0e`), is a v2-track design document by its own
frontmatter, not a successor to text this harness governs. `layer_path_check.LAYER` (the
hook's tuple, lines 30–39) is the same eight paths.

| # | blob at `ae4df09` | lines | member | vs. last recorded read |
|---|---|---|---|---|
| 1 | `33126c19` | 131 | `document-harness/CONSTRUCTION-CHECKLIST.md` | same since `d58969d` read |
| 2 | `4daab565` | 36 | `document-harness/README.md` | **changed** (`fceabf8d` → at `a6b87ad`) |
| 3 | `bd490c8b` | 153 | `document-harness/EXECUTION.md` | same since `d58969d` read |
| 4 | `70bc521e` | 218 | `document-harness/REVIEW.md` | same since `d58969d` read |
| 5 | `0ae222fd` | 5 | `migration/…/v3-harness-operating-contract.md` (stub) | same since `d58969d` read |
| 6 | `7dcdb817` | 5 | `migration/…/v3-harness-review-contract.md` (stub) | same since `d58969d` read |
| 7 | `68031fa2` | 124 | `contract/…-v3-supersession-1.md` | same since `d58969d` read |
| 8 | `e1a2f26b` | 113 | `contract/…-v3-supersession-2.md` | same since `403fc9a` read |

Blob ids from `git ls-tree ae4df09 <dir>` / `git rev-parse ae4df09:<path>` per member; line
counts from `git cat-file -p ae4df09:<path> | wc -l`. One member changed since the last read
of it, in one commit:

```
$ git diff --name-only d58969d ae4df09 -- <the eight members>
ResearchSystem/contract/Document-Work-Assurance-Contract-v3-supersession-2.md   (read at 403fc9a)
ResearchSystem/document-harness/README.md                                       (read at 403fc9a, changed again at a6b87ad)
$ git log --format='%h %s' 403fc9a..ae4df09 -- ResearchSystem/document-harness/README.md
a6b87ad V3-BYTES-CHANNEL-A-FIRST-APPLICATIONS-v1
```

**Dispatch, checked rather than assumed.** `.harness/review-pending.json` is live and reads
`{"kind": "layer-read", "subject": "ae4df09d810ad24ea6e76043c94fe75b716f1757",
"dispatched_at": "2026-07-30T03:49:24+00:00"}` — the subject I was handed. The branch has
taken no commit since the subject; `E9`'s window is intact and this record is the only
commit it admits.

## 2. Coverage — `E10` citation clause, per-member

Members 1, 3, 4, 5, 6, 7 are blob-unchanged since `v3-checkpoint-read-d58969d.md`, whose §6
states *"Read in full: all eight layer members at the blobs tabulated in §1"* and whose §1
table carries these six ids. Member 8 is blob-unchanged since `v3-checkpoint-read-403fc9a.md`,
whose §7 lists `supersession-2.md` (113) under *Read in full* and whose §1 table carries
`e1a2f26b`. I verified both citations against git rather than against the records' tables:
`git rev-parse <read-commit>:<path>` equals `git rev-parse ae4df09:<path>` for each of the
seven. Both cited records' commits landed (`38008a1`, `9ddaff6` — `git log --diff-filter=A`).
Coverage discharged by citation for seven; member 2 read in full here (checklist and the
review stub also read in full as standing instructions). Staleness the byte-key cannot see:
the six unchanged prose members were grepped for the delta's vocabulary (`residue`,
`UNSIGNED line`, `by its own §5`, `§5 design`) — zero hits; nothing restates the re-grounded
corrective.

## 3. What the delta does (`a6b87ad`), against the fixes it claims to apply

Two row rewrites in `README.md`, nothing else in the layer (`git diff 403fc9a a6b87ad`
touches rows 19–20 only). Form is a correction plus a replacement, not a re-type with the
same content (`E10`). Both are the bytes-channel's first two applications under the user's
(a) ruling, whose ledger line lands in the same commit.

| edit | named fix it applies | checked |
|---|---|---|
| row 19: residue ground "by its own §5" → "the contract's own §13 (signed text is never amended in place) bars the in-place correction, so this row and the record … state the signature" | `403fc9a` L-1 minimum fix: *"naming §13 plus the row-and-record convention rather than §5"* | matches — §4 first row |
| row 20: four-name enumeration → *"Everything else under `ResearchSystem/contract/` is either v1/v2 historical-only for v3 (N0 record §3) or a P0–P14 instrument governed there"* | `403fc9a` L-2 minimum fix, second option, verbatim shape | matches — §4 second row |

The fix's other two limbs landed one commit earlier (`a9297ee`, outside the layer): the
signature record's ground rewritten to §13 with the misread §5 named as corrected, and rider
`E2-s2` annotated *"carrier 的 UNSIGNED 残留受 §13 约束、in-place 修已不可行"*. Rider motion
conforms: `L1-g` (README half pending) added at `a9297ee`, then deleted at `a6b87ad` — the
same commit that lands its fix, as the riders-file header requires; `BC-1` (the channel's
clause text for the next `E10` batch) added at `a6b87ad`.

## 4. Assertions re-derived by command

| assertion | command | result |
|---|---|---|
| §13 exists and says what row 19 cites | `git cat-file -p ae4df09:…Contract-v3.md` → `:240` "## 13. Versioning, rollback and supersession", `:243` *"Signed contracts are never amended in place; corrections create a versioned successor."* | holds (row's parenthetical is a gloss, not a quote) |
| row 20 catch-all true of every non-v3 file | `git ls-tree -r ae4df09 ResearchSystem/contract/` = 12 files; 3 v3 texts; the other 9: `Stage-Control-Contract.md` (v1, N0 §3), `General-Harness-Contract-v2.md` (v2, N0 §3 default), `ResearchSystem-Contract.md` + `amendments/`×2 (P0–P14, headers), `adapter-map.md` ("reviewed at P1"), `block-grammar.md` ("frozen at P0"), `content-roots.yaml` ("frozen at P0"), `baseline/P0-baseline.md` ("FROZEN at P0") | holds for all 9 |
| "the live v3 contract texts are exactly the three rows above" | same `ls-tree` | holds — exactly three v3-named texts, rows 17–19 |
| every README link target resolves | script over all 24 relative targets at the subject tree | 0 unresolved |
| "narrows state-pointer digests to the five protected fields" (row 19) | `assurance_state.py:81` `DIGEST_PROTECTED_FIELDS` present; no path under `ResearchSystem/tooling/` changed in `d58969d..ae4df09`, so the five names verified by the `403fc9a` read are these bytes | holds |
| local-enforcement row: three tracked checks | `git ls-tree ae4df09 ResearchSystem/tooling/hooks/` = the three checks + `__init__.py`; `ledger_cap_check.py:18` `MAX_LINES = 120` | holds |
| fixtures "41/41 green" | `python …/N0/fixtures/validate_fixtures.py` → `41/41 cases behaved as declared; failures=0` | holds (this machine) |
| `E2` frozen blob ids | `git rev-parse ae4df09:<path>` ×3 → `8ad404b1…`, `b2dbdf75…`, `68031fa2…` | holds; signed supersession-2 blob `e1a2f26b…` still not on the list, consistent with rider `E2-s2` |
| signature record's signed blob | `git rev-parse ae4df09:…supersession-2.md` = `e1a2f26b1d8d323d11e900f8137dea222b6571c1` | holds — the carrier's bytes are the blob the record names |

No assertion in the layer was found false at this commit. (The carrier's two UNSIGNED lines
remain false statements inside signed bytes — the known, dispositioned residue; see W-1 for
the one imprecision the correctives still carry.)

## 5. Findings

### Wording-level (rides under `R9` — no rider row, no round)

**W-1 — the correctives scope the residue to "top-of-file", but the carrier asserts UNSIGNED
twice, and the second is not top-of-file.** `supersession-2.md:3` (top) and `:107` (§5
*Signature*, near end: *"This file is **UNSIGNED**."*) both still assert the pre-signature
state; README row 19 says *"the carrier's top-of-file UNSIGNED line"* (singular) and the
signature record says *"top-of-file UNSIGNED lines"* (plural but same scope). §5's paragraph
also still carries the pre-`8ec4c60` `E10` phrasing ("prose successor to signed text") and
states its read obligation as open, though that read has since occurred and its records are
committed. All of it sits in signed bytes §13 bars fixing in place. **No downstream decision
goes wrong**: row 19 leads with "signed 2026-07-30", the record carries the exact blob and
date, and §5's own closing sentence directs the reader to the signature record — every path
from `:107` reaches the correction. Fix changes no actor's action, and the accurate fact is
adjacent — wording-level. Minimum fix when a batch next touches `README.md` or the signature
record: replace "top-of-file" with a both-lines scope (`:3` and `:107`/§5).

### Observations

**O-1 — the channel this batch executes is not yet visible in the layer it edits.** The
bytes-channel's authority at this commit is the ledger ruling line plus the commit body;
`BC-1` banks the `E10` clause text for the next `E10` batch. A reader of the eight members
alone cannot learn that byte-supplied lows apply immediately. The authorization is in-repo
(`R7` satisfied — ledger line landed in `a6b87ad` itself); the gap is rule-location, and it
closes when `BC-1` redeems.

**O-2 — third amendment batch with no `E8` kind name.** `a6b87ad` self-describes as
*"Executes the user's (a) ruling…"*; none of `E8`'s five kinds fit an amendment batch, the
same shape `403fc9a` O-2 recorded for `8ec4c60` and `403fc9a`. Third instance of the
unreconciled category set; no re-bank.

**O-3 — a commit-body count uses items, not files.** `a6b87ad`'s body says the catch-all
covers *"all eight non-v3 files"*; `ls-tree -r` shows nine non-v3 files (twelve minus three).
Eight is right only counting `amendments/` as one item — the frame the source finding's own
4+4 enumeration used. The row text itself carries no count, which is the `E3`-safe shape;
the loose figure lives only in the commit body.

**O-4 — residual path tokens unchanged.** The only changed member resolves 24/24 link
targets; the other seven are blob-identical to states already measured, so the recorded
residual (four tokens in three files — review stub, supersession-1, supersession-2) stands
as `d58969d` O-3 / `403fc9a` O-5 left it. Confirmation, not a finding.

**O-5 — `L-2r` stays true by convention.** This record, too, tabulates blob ids because
coverage-by-citation needs them, not because any rule requires a read record to carry them.

## 6. Ledger bindings, checked

- *"C2 开轮的 cold read 顺带清偿 `a6b87ad` … 所欠的层内 read"* — discharged: `README.md` read
  in full at `4daab565`, the applied delta re-derived against the named fixes (§3–§4).
- *"按新 `E10` 逐成员 digest 覆盖"* — applied (§1–§2), seven members by verified citation.
- The `a6b87ad` deferral was clean before this read: nothing relied on the applied bytes —
  `536174c` and `ae4df09` touch only the plan file and ledgers (`git log --name-status`),
  and no round opened between application and this read.
- Rider motions at `a9297ee`/`a6b87ad` conform (§3). The ledger's open-user-question slot is
  empty at this commit.

## 7. Coverage disclosure (`R4`)

**Read in full:** `README.md` (36) at `4daab565`; `CONSTRUCTION-CHECKLIST.md` (131) and the
review-contract stub (5) as standing instructions; the diffs `403fc9a→a6b87ad` (README) and
`9ddaff6→a9297ee` (signature record); `supersession-2-signature.md` at `ae4df09`;
`HARNESS-RIDERS.md` (33) with its `a9297ee`/`a6b87ad` diffs; `HARNESS-LEDGER.md` (75);
`v3-checkpoint-read-403fc9a.md` (265); `v3-checkpoint-read-d58969d.md` (239); the commit
bodies of `a6b87ad` and the `d58969d..ae4df09` name-status listing.

**Sampled:** `supersession-2.md` — coverage by citation (§2), then lines 1–8 and 103–113
read directly plus a whole-file `grep -n UNSIGNED`; `Contract-v3.md` — §13 (`:240–243`) and
the digest passage (`:159–162`) only; `EXECUTION.md`, `REVIEW.md`, the operating stub,
`supersession-1.md` — citation plus the §2 staleness grep; `layer_path_check.py:30–42`;
`ledger_cap_check.py:18,37–39`; `assurance_state.py:14–21,81–82`; headers (≤3 lines) of the
four P0–P14 instruments and `General-Harness-v2-Design.md`.

**Probed only:** the schema pack (diff-emptiness only, no content read); the hooks directory
(enumeration); the fixture runner (executed, output pasted, internals unread).

**Not verified:** that this read ran in a fresh context — a process claim with no evidence
lock, marked rather than asserted. The (a) ruling's chat text beyond its ledger line and
commit-body statement (`R7` — ceiling stated, not a block). Fixture and hook behaviour on
any machine but this one.

**Ceiling:** whether the bytes channel is good policy, and whether the UNSIGNED residue
should be tolerated, are the user's questions under `R5`; what is checked here is that the
layer's text matches the repository, that the applied bytes are the fixes their source
record named, and that the bookkeeping around them did what its own rules say.
