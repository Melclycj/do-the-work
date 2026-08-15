# Instruction-layer read — `d58969d3c0a3829f247c0a2f780764ff9556883e`

E10 amendment read of the instruction layer. Not a round: no verdict, no budget consumed
(`R3`). Findings tiered must-fix / low / observation.

**Findings: 0 must-fix, 2 low, 7 observations.** The amendment text is true where it asserts
fact — every assertion it writes into instruction text was re-derived here by command, and
all of them hold. The two lows are outside the amended bytes: one is a stale routing
statement in `HARNESS-LEDGER.md` that contradicts `HARNESS-RIDERS.md` about where a read's
low findings go, and one is a dependency the new coverage clause has on a record property no
rule requires.

## 1. Subject, re-derived

`R2`: I was handed one SHA and the phrase *the instruction layer*. Everything below is
re-derived; no figure in the dispatch, ledger or any prior record is accepted as reported.

```
$ git rev-parse d58969d3c0a3829f247c0a2f780764ff9556883e   -> d58969d3c0a3829f247c0a2f780764ff9556883e
$ git rev-parse HEAD                                        -> d58969d3c0a3829f247c0a2f780764ff9556883e
$ git status --porcelain=v1
?? ResearchSystem/docs/          # untracked, single file dated 2026-07-19, not in the subject
```

`E10`'s sentence at the subject commit governs the member set. It reads:

> The instruction layer is this file, `README.md`, `EXECUTION.md`, `REVIEW.md`, the two
> retired contracts' stubs, the contract supersessions under `ResearchSystem/contract/`
> (`supersession-1`, `supersession-2`), and any later prose successor to text this harness
> governs, including schema `description` strings when amended.

Enumerated against the repository at the subject commit: **eight** members. The open tail
("any later prose successor…", "schema `description` strings when amended") adds none —
`git ls-tree ResearchSystem/contract/` shows exactly two supersessions, and no schema
`description` has been amended (see O-5).

| # | blob | lines | member | vs. `451e8b0` |
|---|---|---|---|---|
| 1 | `33126c19` | 131 | `document-harness/CONSTRUCTION-CHECKLIST.md` | **changed** (`d3228163` →) |
| 2 | `fb732374` | 34 | `document-harness/README.md` | **changed** (`b344d807` →) |
| 3 | `bd490c8b` | 153 | `document-harness/EXECUTION.md` | same |
| 4 | `70bc521e` | 218 | `document-harness/REVIEW.md` | same |
| 5 | `0ae222fd` | 5 | `migration/…/v3-harness-operating-contract.md` (stub) | same |
| 6 | `7dcdb817` | 5 | `migration/…/v3-harness-review-contract.md` (stub) | same |
| 7 | `68031fa2` | 124 | `contract/…-v3-supersession-1.md` | same |
| 8 | `2cf4983c` | 110 | `contract/…-v3-supersession-2.md` | same |

Blob ids from `git ls-tree -r d58969d --format='%(objectname) %(objectsize) %(path)'`; line
counts from `git cat-file -p d58969d:<path> | wc -l`; the comparison column from
`git rev-parse 451e8b0:<path>` against `git rev-parse d58969d:<path>`, run per member.

Both changed members changed in one commit, and nothing after it touched the layer:

```
$ git log --format='%h|%ad|%s' --date=short 451e8b0..d58969d
d58969d|2026-07-30|V3-REFORM-CLOSEOUT-v1
fbee895|2026-07-30|V3-REVIEW-RECORD-REFORM-VERIFY-49d9829-v1
49d9829|2026-07-30|V3-REFORM-BANK-F1-F3-v1
1c45e24|2026-07-30|V3-REFORM-REPAIR-B1-B2-B3-F2-v1
1592181|2026-07-30|V3-REVIEW-RECORD-REFORM-FULL-8ec4c60-v1
8ec4c60|2026-07-29|V3-REFORM-A-INSTRUCTION-AMENDMENTS-v1
717e547|2026-07-29|V3-REFORM-B-GUARDS-GENERATOR-RECORD-HOMES-v1
8e9b60b|2026-07-29|V3-REVIEW-RECORD-INSTRUCTION-LAYER-COLD-READ-451e8b0-v1

$ git diff --name-only 8ec4c60 d58969d -- <all eight members>
(empty)
```

**Dispatch, checked rather than assumed.** `.harness/review-pending.json` is live and reads
`{"kind": "layer-read", "subject": "d58969d3c0a3829f247c0a2f780764ff9556883e", …}` — written
by `rsc.py::_cmd_v3_dispatch` (line 383), matching the subject I was handed. `.harness/` is
gitignored (`.gitignore:19`), so the marker is untracked and deleting it stages nothing;
the E9 window cannot deadlock on its own release.

## 2. Coverage — the new `E10` clause, first application

The amendment added: *"a member whose blob is unchanged since a recorded end-to-end read of
it is covered by citing that record."* Members 3–8 qualify against `v3-cold-read-451e8b0.md`
(committed `8e9b60b`), whose §1 states **"All eight were read end to end this session"** and
whose §7 lists all eight under *Read in full*. I verified that citation rather than taking
it: the record's §1 blob table names `bd490c8b` / `70bc521e` / `0ae222fd` / `7dcdb817` /
`68031fa2` / `2cf4983c`, which are byte-for-byte the ids I re-derived above.

Coverage was therefore dischargeable by citation for six of eight members. **I read all eight
in full anyway** — the clause is new and its first use is the wrong place to economise. The
disclosure in §6 reports what I actually read, not what the clause would have permitted.

## 3. The amendment text (`8ec4c60`), checked

Six edits to `CONSTRUCTION-CHECKLIST.md`, two added rows plus one extended row in `README.md`.
The form is additive/subtractive per `E10`; no passage is re-typed with the same content —
the only re-emitted line is the `Its` fragment reflowed inside the E10 sentence being changed.

| edit | what it does | checked |
|---|---|---|
| `E3` +clause | factual assertion in instruction text must run the falsifying command first, output kept in the commit body or round journal | self-applied — see §4 |
| `E9` +clause | a dispatched FULL/VERIFY/read has occurred only when its record's commit lands | guard exists and is wired; strictness gap at O-1 |
| `E10` membership | sentence becomes an enumeration; adds the two supersessions; "prose successor to signed text" → "later prose successor to text this harness governs" | enumeration matches the repository exactly (§1); answers `451e8b0` M-1 by changing the text, which is the fix `E6` requires |
| `E10` no-round pair | pair admits only deletions and the literal replacement the finding names; a clause-adding amendment opens a round | seam already banked as `F-1r` — O-4 |
| `E10` coverage | per-member discharge by citing a recorded end-to-end read | applied in §2; dependency at L-2 |
| `R6` +family | adds `v3-cold-read-<sha>.md` | family exists (3 files); `review_freeze_check.py`'s regex independently admits all four families — O-6 |
| `README` +2 rows | round journal, rider bank | both targets exist at the subject commit |
| `README` local-enforcement row | three tracked checks, existence-guarded | verified in §4 |

The amendment adds clauses to `E3`, `E9`, `E10` and `R6`, and it opened a round — which is
what its own new `E10` clause requires of a clause-adding amendment. Self-consistent.

## 4. Factual assertions in the layer, re-derived by command

`E3`'s new clause makes this the load-bearing part of the read. Every assertion below was
checked against the repository, not against a record.

| assertion (member) | command | result |
|---|---|---|
| hook "calls three tracked checks, existence-guarded, from `ResearchSystem/tooling/hooks/`" (README) | read `D:/Thesis/.git/hooks/pre-commit` lines 37–50; `git ls-tree ResearchSystem/tooling/hooks/` | holds — loop over exactly those three, each `-f` guarded; the directory holds exactly those three plus `__init__.py` |
| review-freeze: "`rsc v3 dispatch` writes `.harness/review-pending.json`" (README) | `rsc.py:383`; live marker contents | holds — producer keys `kind`/`subject`/`dispatched_at` match what `review_freeze_check.py` reads |
| review-freeze: "while it exists only record-family paths may land" (README) | `review_freeze_check.py:41-65` | holds as written (see O-1 for E9 vs. guard) |
| ledger cap: "staged `HARNESS-LEDGER.md` ≤ 120 lines" (README) | `ledger_cap_check.py:17-38` (`MAX_LINES = 120`, measures `git show :<path>`) | holds — staged bytes, whole file, 120 |
| "instruction-layer path resolution" (README) | `layer_path_check.py` | holds; its `LAYER` tuple matches E10's eight members exactly |
| "The provenance-entry check … was deleted 2026-07-28" (README) | `git ls-tree` of the hooks dir | holds — script absent (O-7 on the hook's residual branch) |
| "Contract fixtures + runner … (41/41 green)" (README) | `python …/N0/fixtures/validate_fixtures.py` | holds — `41/41 cases behaved as declared; failures=0` |
| supersession-1 "signed 2026-07-24 … (`ac1b383`)" (README, EXECUTION, REVIEW) | `git cat-file -t ac1b383`; `git show --stat` | holds — commit `V3-W2-SIGN-OFF-CLOSEOUT-v1`, 2026-07-24, touching `W2-record.md` alone |
| `E2` frozen blob ids `8ad404b1…` / `b2dbdf75…` / `68031fa2…` | `git rev-parse d58969d:<path>` ×3 | holds — `8ad404b12b3242e7…`, `b2dbdf752d8c155e…`, `68031fa2ca31272e…` |
| every README link target | `git cat-file -e d58969d:<path>` ×6 | all resolve |

No assertion in the layer was found false.

## 5. Findings

### Low

**L-1 — `HARNESS-LEDGER.md` and `HARNESS-RIDERS.md` contradict each other on where a read's
low findings go, and the ledger's version is the stale one.** `HARNESS-RIDERS.md:5-7` states
*"lows from reads route here by the 2026-07-29 ruling (`C-3` takes must-fix, `R9` takes
wording-level, this file takes the middle)"*. `HARNESS-LEDGER.md:34-35`, in the
already-adjudicated list, still states *"read 的 low findings 无路由（`C-3` 管 must-fix、`R9`
管 wording-level，中间是空的）"* — the gap the riders file says it closed. Both are current at
the subject commit. **Downstream decision that goes wrong:** a reader who consults the ledger
concludes a read's low findings have no home and drops them, which is exactly what happens to
the two lows in this record if the ledger is believed. Minimum fix: delete the stale ledger
clause; the riders file already carries the rule. *Both files are outside the instruction
layer, so this is not a layer defect — reported because the read hit it while routing its own
findings.*

**L-2 — the new coverage clause depends on a record property no rule requires.** Discharging
coverage by citation requires knowing which blob the cited record read end-to-end. Neither
`E10` nor `R6` requires a read record to state the blob ids it read; `v3-cold-read-451e8b0.md`
happens to tabulate them, which is the only reason §2 above is checkable. Nothing makes that
a property of the next record. **This fails safe** — a record without blob ids cannot be cited,
so the next reader re-reads. No decision goes wrong, only cost rises; under `R9` it rides the
next batch touching `E10` rather than opening anything. Named here because the clause's
usability, not its safety, is what degrades silently.

### Observations

**O-1 — `E9`'s sentence is strictly tighter than the guard that carries it.** `E9` says the
branch "takes no commit but the record itself"; `review_freeze_check.py` admits any path
matching the four record families, and never compares the staged record against the
`subject` it has already parsed from the marker (`pending` is read at line 52 and used only
for the failure message at lines 58–61). A record for a different subject would pass. The
instruction text is not false — the guard is advisory by README's own row, and the layer's
stated instrument is the independent read. Flagged rather than proposed: `E6` treats "a fix
that requires new machinery" as the signal to re-question the guarded thing, and under `R5`
whether the guard should tighten is the user's question, not mine.

**O-2 — the coverage clause keys on a member's own bytes, but a member can go stale without
its bytes changing.** `R6` gained a record family at `8ec4c60`; had any unchanged member
restated `R6`'s family list, its byte-identical blob would now be wrong while still qualifying
for citation. I checked all six unchanged members for restatements of the amended passages and
found none at this commit — `EXECUTION.md` and `REVIEW.md` are product-run role files, the
stubs only point at the checklist, and supersession-2 §5 names the record directory without a
family list. Reported as a shape, not a defect: nothing is stale here.

**O-3 — the three pre-existing missing-prefix path tokens reproduce exactly.** Running
`layer_path_check`'s own `unresolved_tokens` over the *full* text of all eight members (the
shipped guard scans only staged added lines) returns, and only returns:
`v3-harness-review-contract.md` → `tooling/tests/fixtures/expected-construction-prompt.txt`;
`supersession-1.md` → `schema/document-assurance-v3/review.v2.schema.json`;
`supersession-2.md` → `assurance/runs/`, `schema/`. Identical to the set the round's FULL
reported and the journal recorded with the disposition *"the three pre-existing hits stay
un-repaired until a batch writes those tokens anew."* Confirmation of a recorded residual, not
a new finding. The review stub's substantive claim is separately true: the fixture at
`ResearchSystem/tooling/tests/fixtures/expected-construction-prompt.txt` does hard-code the
stub's path (line 3). The supersession-1 token sits in `E2`-frozen bytes.

**O-4 — the `F-1r` seam survives in the landed text, and I read it as non-decisive.** The
reliance qualifier *"for as long as no round has relied on the text"* now sits after the
clause-adding sentence rather than after *"that pair is not a round and spends no budget"*,
so the free channel reads unqualified on its nearest-antecedent parse. Both parses converge in
practice because the trailing *"once one has, changing it opens a round"* is unconditional and
catches the pair either way. Independent agreement with the round's own decision to bank it
(`HARNESS-RIDERS.md` `F-1r`), recorded so the bank has a second reading behind it rather than
one.

**O-5 — the schema-`description` tail of `E10` is unreachable, and this is already banked.**
`E2` freezes "every existing file in the `ResearchSystem/schema/document-assurance-v3/` pack",
so a `description` in an existing pack file cannot be amended into the instruction layer; the
tail has live application only for a pack file added later. `HARNESS-RIDERS.md` `E2-t` already
carries this, citing `451e8b0` O-3. No re-bank.

**O-6 — `R6`'s four families do not cover every reviewer-side artifact in the record
directory.** `v3-review-note-instruction-layer-custody.md`, `v3-review-note-obligation-authoring.md`
and `v3-review-handoff-2026-07-21.md` are reviewer-side files matching no `R6` family. All
three predate the freeze guard. Consequence if the shape recurs: during an open window
`review_freeze_check.py` would block writing such a file, since it admits only the four
families. Worth knowing before someone needs a note mid-window.

**O-7 — the local hook keeps a dead branch for the deleted provenance check.** Lines 26–35 of
`D:/Thesis/.git/hooks/pre-commit` still call `contract_provenance_check.py`, which no longer
exists; the `-f` guard makes it a no-op. README's claim that the check was deleted is correct
about the script. Untracked per-machine file, outside the subject commit — noted only because
the read was in the file.

## 6. Coverage disclosure (`R4`)

**Read in full:** all eight layer members at the blobs tabulated in §1 (131 / 34 / 153 / 218 /
5 / 5 / 124 / 110 lines) — six of them beyond what §2's citation required. The full diff of
`8ec4c60` for both changed members. `v3-harness-review-contract.md` and
`CONSTRUCTION-CHECKLIST.md` as the standing instructions. `HARNESS-LEDGER.md` (66 lines),
`HARNESS-RIDERS.md` (34 lines), the three hook scripts (`review_freeze_check.py`,
`ledger_cap_check.py`, `layer_path_check.py`) and the local `pre-commit` hook, all end to end.

**Sampled:** `v3-cold-read-451e8b0.md` — §1 blob/provenance tables and the §7 coverage
disclosure read directly, the rest by grep for coverage vocabulary. The round journal
`reform-2026-07-29.md` lines 1–140. `rsc.py` lines 360–400 only (the marker-writing path).

**Probed only:** the schema pack (existence and path resolution, no content read). The FULL and
VERIFY records of the reform round were **not** read as review subjects — a read is not a
re-review of the round (`R3`), and their findings entered here only where a rider row or the
journal named them, so that this record would not double-report what is already banked.

**Not verified:** that this read ran in a fresh context — a process claim with no evidence lock
(`R4`), marked rather than asserted. That `41/41` and the guard behaviours hold on any machine
but this one: the hook is per-machine and untracked, and the fixture run is mine alone.

**Ceiling on §3's judgement:** whether each amendment clause is *good policy* is not a read's
question. What is checked here is that the text says what the repository shows, that its
enumerations match, and that its new obligations are satisfiable — not that the rules are the
right rules.
