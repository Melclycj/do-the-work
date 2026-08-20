# Cold read — the instruction layer at `17ce3ed`

**No verdict.** A read is not a round (`R3`): it spends no budget, carries no verdict, and its
output is findings tiered must-fix / low / observation. This is the read `E10` owes at a
round's opening; nothing below certifies any text, and nothing below is banked as any round's
FULL.

**This read also redeems a deferred obligation.** Round `DE-PREFIX` applied bytes to six of
the ten members under `E10`'s deferral channel and recorded the debt — `CONSTRUCTION-LEDGER.md:67`,
*「层欠一次独立 read，随下一轮开轮（tip 十成员 blob id 列在 VERIFY 记录）」*. The layer text those
applications produced is read end to end here (§2, §3.6).

**Findings: 1 must-fix, 1 low, 3 observations.** The must-fix is a caller-held location written
as a repository path token in `REVIEW.md`'s deliverables section — the same defect class
`v3-cold-read-4410899.md` `L-1` reported one round ago, whose class sweep counted one sibling
where there were two, and which `DE-PREFIX`'s de-prefixing then turned from *resolves only in
the caller* into *resolves only in the instrument*.

**Standing instructions read.** `migration/document-work-assurance-v3/v3-harness-review-contract.md`
(the stub, member 7) → `document-harness/CONSTRUCTION-CHECKLIST.md` in full, both sides, per the
stub's *"It is your standing instruction and its own counterpart; read all of it."*
`HARNESS-DECISIONS.md` `§live` (lines 28–195, ten entries — `HD-49`, `HD-50`, `HD-47`, `HD-44`,
`HD-41`, `HD-36`, `HD-35`, `HD-34`, `HD-23`, `HD-9`) plus the file header (1–27) that states its
own state machine, which `E10`'s tail requires; `§implemented` (197–505) was **not** read end to
end — it was grepped for the ids the members cite. The members cite eleven distinct `HD` ids
(`HD-1 2 5 7 14 20 28 35 39 41 42`); all eleven resolve — two in `§live` (`HD-35`, `HD-41`),
five in `§implemented`, four in `HARNESS-DECISIONS-archive.md`. Cited by section, never by
blob, per that clause.

---

## 1. Subject, re-derived

```
$ git rev-parse HEAD
17ce3edbb5ba52c4b8b096f0cc4dd506c92922da

$ git rev-parse --abbrev-ref HEAD
main

$ git status --porcelain --untracked-files=all
(no output)

$ git log --oneline -6
17ce3ed V3-DE-PREFIX-O5-RULING-v1
668e26e V3-DE-PREFIX-PD-RULING-v1
41672f8 V3-DE-PREFIX-CLOSEOUT-v1
f8b4ef3 V3-DE-PREFIX-FREE-V1-V2-v1
73c169a V3-REVIEW-RECORD-DE-PREFIX-2538893-v1
2538893 V3-DE-PREFIX-FIX-v1
```

The tip is the one the dispatch names. The worktree is clean and untracked-free, so the
working-tree bytes are the subject bytes; every quotation that carries weight below was
nonetheless taken from the object store (`git cat-file -p <blob>` / `git ls-tree`), not from the
worktree.

**No freeze marker exists** (`.harness/` holds `runs.jsonl` alone), so this read was not
dispatched through `dtw dispatch --read`, which is the only writer of one
(`tooling/rsclib/document_harness/cli.py:216`). Recorded as `O-2`, not as a defect in any member.

## 2. The member set and each member's blob

Derived from `E10`'s own sentence at the subject (`CONSTRUCTION-CHECKLIST.md:94-105`), which
reads *"exactly these ten paths and nothing else"* and then enumerates them. Nothing was taken
from the dispatch. Blob ids per `E10`'s *"a read's record states the blob id of each member it
read, because citation depends on it"*:

```
$ git ls-tree -r -l HEAD -- <the ten paths>
 1  cacd99d49d80ce4bf33e94b733a07f1dd6b247e8   235 lines   18531 B  document-harness/CONSTRUCTION-CHECKLIST.md
 2  3a49e0328cbd6e0bc36b331d43f32f33f8bf36ab    40 lines    9946 B  document-harness/README.md
 3  0d0c617ba09c8e37013545776bc517c54dede439   470 lines   32690 B  document-harness/EXECUTION.md
 4  946b4beb831c2cb76967fe64ca6ab7fb48f8c612   285 lines   18021 B  document-harness/REVIEW.md
 5  80f42658a2961eeb10a168bd7bd729121c6c05ae    95 lines    6389 B  document-harness/ORCHESTRATION.md
 6  6d5714923870b4e13e8928221a80df68e563a5ed     5 lines     511 B  migration/document-work-assurance-v3/v3-harness-operating-contract.md
 7  29bdc9fbde6e8db38d601dd2340d4b46a24a296f     5 lines     924 B  migration/document-work-assurance-v3/v3-harness-review-contract.md
 8  68031fa2ca31272e31da0d42a9a02189d28fcc21   124 lines    6480 B  contract/Document-Work-Assurance-Contract-v3-supersession-1.md
 9  e1a2f26b1d8d323d11e900f8137dea222b6571c1   113 lines    7421 B  contract/Document-Work-Assurance-Contract-v3-supersession-2.md
10  09aa869962f592c2f86c9379be0ef3eb7d2232ff    44 lines    2812 B  schema/document-assurance-v3/paragraph-map.schema.json
```

Ten paths enumerated, ten present, none missing. How each was covered:

| # | member | blob at `17ce3ed` | how covered |
|---|---|---|---|
| 1 | `document-harness/CONSTRUCTION-CHECKLIST.md` | `cacd99d4` | **read end to end** — changed at `2538893`; no read record names this blob |
| 2 | `document-harness/README.md` | `3a49e032` | **read end to end** — changed at `f8b4ef3`; no read record names this blob |
| 3 | `document-harness/EXECUTION.md` | `0d0c617b` | **read end to end** — changed at `39a21a8`; no read record names this blob |
| 4 | `document-harness/REVIEW.md` | `946b4beb` | **read end to end** — changed at `39a21a8`; no read record names this blob |
| 5 | `document-harness/ORCHESTRATION.md` | `80f42658` | **read end to end** — citation to `v3-cold-read-4410899.md` §2/§5 was available and is not claimed |
| 6 | `…/v3-harness-operating-contract.md` | `6d571492` | **read end to end** — changed at `39a21a8` |
| 7 | `…/v3-harness-review-contract.md` | `29bdc9fb` | **read end to end** — changed at `39a21a8` |
| 8 | `contract/…-supersession-1.md` | `68031fa2` | **covered by citation** — `v3-cold-read-4410899.md`, whose §2 records this same blob and whose §5 discloses all ten *"read in full at the subject blobs"* |
| 9 | `contract/…-supersession-2.md` | `e1a2f26b` | **covered by citation** — same record, same blob |
| 10 | `schema/…/paragraph-map.schema.json` | `09aa8699` | **covered by citation** — same record, same blob |

The citation was verified before it was relied on, not accepted:
`v3-cold-read-4410899.md:88-93` lists `80f42658`, `68031fa2`, `e1a2f26b` and `09aa8699` for
members 5, 8, 9 and 10, and its §5 line 421 reads *"**Read in full at the subject blobs:** all
ten members (1 411 lines total, blob ids in §2)"*. Those four blobs are byte-identical here; the
`ResearchSystem/` prefix that record's path column carries was removed by `DE-PREFIX` without
touching the bytes (`git log --follow` crosses the rename, and members 8–10 appear in `39a21a8`
as pure renames). Members 5 and 8–10 were therefore citable; member 5 was read anyway because
the cross-member checks in §3 need its text, so **no citation is claimed for it**.

The four members `2538893` and later commits did not touch (3, 4, 6, 7) were also unchanged
since `39a21a8`, but **no read record covers those blobs** — `v3-cold-read-4410899.md` predates
them, and `v3-review-verify-2538893.md` is a VERIFY, not an end-to-end read. They are read here.

**Not a member, read by section:** `HARNESS-DECISIONS.md` `§live`, per `E10`'s tail clause. It
is not listed above and is cited by section, never by blob, exactly as that clause requires.

## 3. What was checked, and what the commands returned

Scope declaration (`HD-41` ①): every enumeration below is over the **ten member blobs at
`17ce3ed`**, whole-file, unless a narrower scope is written on the line.

### 3.1 `E2`'s freeze surface — three blobs and one directory

```
$ git rev-parse HEAD:contract/Document-Work-Assurance-Contract-v3.md
b2dbdf752d8c155e4c65b14b5f420b880b8184a1

$ git ls-tree HEAD contract/
100644 blob 68031fa2ca31272e31da0d42a9a02189d28fcc21  …-supersession-1.md
100644 blob e1a2f26b1d8d323d11e900f8137dea222b6571c1  …-supersession-2.md
100644 blob b2dbdf752d8c155e4c65b14b5f420b880b8184a1  Document-Work-Assurance-Contract-v3.md

$ git ls-tree HEAD schema/document-assurance-v3/ | wc -l
15
```

All three ids equal the literals `E2` names (`:45-46`), and the pack is the fifteen files
`E2`'s parenthesis states. Two of the three blobs are members 8 and 9, so for those the freeze
list and the tree agree by inspection, which is what `E2` says it wants. `contract/` holds
exactly three files, which is what `README.md:20` asserts.

### 3.2 The `E10-sync` three mirrors

`E10`'s membership sentence, `layer_path_check.LAYER` and
`test_precommit_checks.LayerMembership.EXPECTED` were compared mechanically after being read by
hand. The membership sentence was parsed out of the member blob, not typed:

```
 layer_path_check.LAYER  == EXPECTED (hand-written test tuple): True
 E10 membership sentence == LAYER: True | n = 10
 all three mirrors identical, in order, n=10: True
```

`HD-22`'s per-touch obligation is met at this tip. The test tuple is hand-written and is not the
module's own list, which is `E5` (`test_precommit_checks.py:225`, docstring states it).

### 3.3 The path-token class — the sweep, and what the sweep cannot see

Whole-file scan of all ten members with the guard's own resolver
(`layer_path_check.unresolved_tokens`), i.e. wider than the guard runs (it sees added lines
only):

```
contract/Document-Work-Assurance-Contract-v3-supersession-1.md: `ResearchSystem/migration/document-work-assurance-v3/W2/W2-design.md`
contract/Document-Work-Assurance-Contract-v3-supersession-1.md: `ResearchSystem/migration/document-work-assurance-v3/W2/W2-record.md`
contract/Document-Work-Assurance-Contract-v3-supersession-2.md: `assurance/runs/`
contract/Document-Work-Assurance-Contract-v3-supersession-2.md: `templates/run-v2/`
contract/Document-Work-Assurance-Contract-v3-supersession-2.md: `ResearchSystem/migration/document-work-assurance-v3/`
TOTAL unresolved backtick path tokens across the ten members (whole file): 5
```

All five sit in the `E2`-frozen supersessions, which `E10` excepts *"while they are frozen"* and
which `R10`/`HD-20` bank until `E2`'s recorded ruling exists. Rider `frozen-path-prefix` already
carries them (its fact was rewritten 4→5 at the `DE-PREFIX` closeout). **Banked, not a finding.**
The eight mutable members carry **zero** unresolved backtick path tokens.

Residual `ResearchSystem/` tokens anywhere in the ten, by grep: seven — the five above, plus the
two `git show 7011916:ResearchSystem/…` full-text citations in the stubs, which are source-repo
paths and correct as written. The de-prefixing was complete on the mutable members.

What the guard cannot see was swept separately:

- **Markdown links** (no backtick token to find). All relative link targets in the seven prose
  members were resolved from each file's own directory: `TOTAL broken relative markdown links
  across the 7 prose members: 0`.
- **Placeholder-bearing tokens** (angle brackets fall outside `PATHLIKE`). Three exist in the
  layer: `REVIEW.md:132` `` `<control root>/evidence/review-full.json` ``,
  `EXECUTION.md:260` `` `<control root>/control/paragraph-map.json` `` — both in the compliant
  name-the-holder form — and `REVIEW.md:135` `` `migration/document-work-assurance-v3/v3-review-<round>-<subject short SHA>.md` ``,
  which is **`M-1`**. `v3-cold-read-4410899.md` `L-1` §"Class sweep" asserted *"Exactly one other
  placeholder-bearing path token exists in the layer, `REVIEW.md:132`"*; the measured count is
  two, and the one it missed is the one that now misdirects.
- **`.harness/` run-time markers**: two sites (`README.md:36`, `REVIEW.md:139`), carved out by
  `E10` and by `RUNTIME_PREFIX` in the guard.

The guard's own description in `E10:147-157` was checked clause by clause against
`tooling/hooks/layer_path_check.py` and holds on every clause: single nowhere-resolving class
(`unresolved_tokens`), escape-the-root counting as nowhere (`is_relative_to(root)`),
`.harness/` exemption (`RUNTIME_PREFIX`), added-lines-only (`added_lines_by_path`), rename
pairing via `-M`, and the `++ ` header ambiguity — an added line whose content opens `++ b/`
matches the `"+++ b/"` branch and mis-files what follows, any other `++ ` matches the `"+++ "`
branch and sets `current = None`, silencing it. Accurate as written.

`README.md:36`'s newly applied claim about the two guards' relationship was probed rather than
read:

```
'see `hooks/layer_path_check.py` here'      layer guard -> BLOCKED   candidate lint -> ()
'see `no/such/file.md` here'                layer guard -> BLOCKED   candidate lint -> ('no/such/file.md',)
'see `document-harness/README.md` here'     layer guard -> ok        candidate lint -> ()

[p for p in layer_path_check.LAYER if candidate_path_check.scanned(p)] -> 9
```

*"the two overlap on the members this lint also scans, and there they still differ on shorthand:
a unique tracked suffix passes this lint and not that one"* — reproduced exactly, and the
overlap is 9 (the schema member being the one `scanned()`'s `.md` test drops), which is the
number `candidate_path_check.py`'s docstring computes for `2538893`.

### 3.4 Commit ids cited in members

Every hex id in the seven prose members was resolved in both repositories:

```
token        instrument caller     first site
0d73a5f      commit     -          document-harness/EXECUTION.md:383
418b89c      -          commit     document-harness/EXECUTION.md:407
68031fa2     blob       blob       document-harness/CONSTRUCTION-CHECKLIST.md:46
6fd0ae3      -          commit     document-harness/EXECUTION.md:384
7011916      -          commit     document-harness/CONSTRUCTION-CHECKLIST.md:5 (+4)
820b287      -          commit     document-harness/README.md:36
838c413      -          commit     document-harness/EXECUTION.md:332
86defbc      -          commit     document-harness/EXECUTION.md:452
9ba9bbc      -          commit     document-harness/EXECUTION.md:442
a22cca0      -          commit     document-harness/EXECUTION.md:250
a8af54c      -          commit     document-harness/EXECUTION.md:381
ac1b383      -          commit     document-harness/README.md:18 (+2)
b2dbdf75     blob       blob       document-harness/CONSTRUCTION-CHECKLIST.md:45
ddd773a      -          commit     document-harness/EXECUTION.md:379
e1a2f26b     blob       blob       document-harness/CONSTRUCTION-CHECKLIST.md:46
fef3a2e      -          commit     document-harness/REVIEW.md:45
```

The preamble's rule holds on every one. Exactly one id resolves here and not in the caller —
`0d73a5f` — and it is the one site that *names its repository* (`EXECUTION.md:383-384`,
*"its bases: instrument `0d73a5f`, caller `6fd0ae3`"*), which is the preamble's
*"A citation naming its own repository is read as written"* branch. The fifteen silent ones all
resolve in the caller, which is the *"a silent one means that one"* branch. The escape hatch was
executed, not assumed:

```
$ git -C D:/Thesis-stage-control-refactor show 7011916:ResearchSystem/migration/document-work-assurance-v3/v3-harness-operating-contract.md | head -4
# V3 harness — execution-side operating contract

The standing instructions of the **execution agent** for Document Work Assurance Harness v3
construction nodes.
```

### 3.5 Assertions re-run rather than read

Every factual claim in the eight mutable members that a command could falsify was executed.

| claim | site | result |
|---|---|---|
| `contract/` holds exactly the three named files | `README.md:20` | 3 tracked files — **holds** |
| the schema pack's fifteen stems are all named in the README | `README.md:22-25` | 15 files, 15 stems; `test_readme_enumeration.py` pins it and is green — **holds** |
| contract fixtures `41/41 green` | `README.md:35` | `41/41 cases behaved as declared; failures=0` — **holds** (the JSON's `schema_cases` array is 34; the runner expands bundles, and 41 is the runner's own figure) |
| `test_readme_enumeration.py` pins `document-harness/README.md`'s path | `EXECUTION.md:330` | the test computes `root / "document-harness" / "README.md"` — **holds** |
| the layer-path mirror pins the member paths | `EXECUTION.md:330-332` | §3.2 — **holds** |
| the instrument's single battery leg is `python -m pytest -q` run from `tooling` | `EXECUTION.md:341-343` | `739 passed in 107.29s` at `17ce3ed` — **green**; the text's `712 passed in 93.67s` is pinned to instrument base `0d73a5f` and the text itself says to re-run rather than trust it (`HD-41` ③), so it is not falsified and was not re-derived at that base (**UNVERIFIED** at `0d73a5f`) |
| the caller's five battery scripts live in the caller's tree, and a name here may also belong to an unrelated file in this repository | `EXECUTION.md:344-351` | all five present in the caller (`ResearchSystem/tooling/rsc.py`, `…/tests/run_tests.py`, `run_p4_tests.py`, `run_p5a_tests.py`, `ResearchSystem/schema/fixtures/validate_fixtures.py`); the instrument's own `migration/…/N0/fixtures/validate_fixtures.py` is the different file the caveat anticipates — **holds, caveat load-bearing** |
| `assurance/templates/run-v2/README.md` now holds instantiation only | `EXECUTION.md:176` | its only headings are *Run template v2*, *What changed from the w1-r1 shape*, *Steps that did not change* — **holds** |
| `check_template_instance.py`'s three legs | `EXECUTION.md:246-267` | `spec_version_issues`, `preamble_issues`, `paragraph_map_issues` present, legs 2–3 form-conditional — **holds** |
| `transcript_audit(spec, instruction_text)` returns `(result, findings)` | `EXECUTION.md:283-284` | signature `(Mapping, str) -> tuple[str, tuple[dict, ...]]` — **holds** |
| `dtw dispatch`'s three modes are review-side and none dispatches an executor | `ORCHESTRATION.md:27-30` | `--subject` / `--range` / `--read`, one mutually-exclusive required group — **holds** |
| `dispatch.CONSTRUCTION_ROLE_INSTRUCTION` hard-codes the stub path, and the test's `CHARTER_OUTSIDE` / `MEMBER` pin it independently | member 7, line 5 | constant equals the path; `test_dispatch.py:398,463,522` carry the literal by hand — **holds** |
| the tracked hook runs the layer path check and nothing else | `README.md:36`, `.githooks/pre-commit` | one `CHK=tooling/hooks/layer_path_check.py`, loud failure if absent; `git config --get core.hooksPath` → `.githooks`, so it is wired **in this checkout** — **holds** |
| `HARNESS-RIDERS.md` is where the bank lives | `R10` | present at repo root — **holds** |

### 3.6 What round `DE-PREFIX` wrote into the layer — the deferred obligation

```
$ git diff --name-status 2538893 HEAD
M  CONSTRUCTION-LEDGER.md
M  HARNESS-DECISIONS.md
M  HARNESS-RIDERS.md
M  document-harness/README.md
A  migration/document-work-assurance-v3/v3-review-verify-2538893.md
M  tooling/hooks/candidate_path_check.py
```

Across the whole round (`39a21a8^..HEAD`) six members took bytes: 1, 2, 3, 4, 6, 7. The
substantive edits, read against their diffs rather than only in final form:

- **`E10:147-157`** replaced the guard's two-prefix description with the single
  nowhere-resolving class. Verified against the code, clause by clause (§3.3).
- **`E10`, `E2`, `R6`, `R10`, the preamble** de-prefixed. All resolve (§3.3).
- **`EXECUTION.md:258-262`** applied `v3-cold-read-4410899.md` `L-1`'s exact bytes
  (`<control root>` + holder). Confirmed landed verbatim.
- **`README.md:20`** rewritten from a population that had emptied (`v3-cold-read-4410899.md`
  `O-1`) to *"Nothing: … exactly the three files"*. Re-measured true (§3.1).
- **`README.md:36`** rewritten to describe the two guards' new relationship. Probed and
  reproduced (§3.3).
- **`REVIEW.md:135`** de-prefixed. This is `M-1`.

### 3.7 `§live`, read by section

Ten entries, lines 28–195. Each was read against the members for drift:

- `HD-49` (product-run records stay with the caller) — the ground truth `M-1` violates, and the
  only entry whose own status line disagrees with the section it sits in (`O-1`).
- `HD-50` (batch DTW-INDEPENDENCE) — R1–R3 CLOSED, R4 open; matches
  `CONSTRUCTION-LEDGER.md:123`'s queue head. No member claims a round state.
- `HD-47` (`dtw init` as the seventh command) — `cli.py`'s parser carries `init` and
  `test_cli_entry.py`'s hand-written `OPERATIONS` is seven long, both as the entry's 后果 says.
  No member states a command count, so no drift.
- `HD-44` (`E2` freezes bytes, not this repository's paths) — `E2` still names the pack by a
  path token and says nothing about which repository holds it. That is exactly the gap the
  entry's status parenthesis declares it exists to carry; not a drift, and not mine to close
  (`R5`).
- `HD-41` (scope-before-assertion + class-sweep evidence) — applied to this record's own
  assertions (scope line at the head of §3). Its ④ is the discipline `M-1` records a miss of.
- `HD-36` (`E10` must-fix channel) — both halves are carried in `E10`'s current bytes: the
  channel admits the class sweep and the executor-written fix (`:113-118`, the admits-list at `:115-117`), and the priority
  sentence reads *"the bytes the finding supplies"* (`:132`). The exemption ② declares to have
  no carrier in the layer still has none: `E10:130-131`'s design test is unqualified. Consistent
  with the entry staying `live`.
- `HD-35`, `HD-34`, `HD-23`, `HD-9` — no member states anything they bear on.

## 4. Findings

### `M-1` (must-fix; bytes supplied) — `REVIEW.md:134-136` sends a product-run reviewer's record to a path that is the instrument's, against `E10`, `HD-49`, and `REVIEW.md`'s own text

**Location.** `document-harness/REVIEW.md:134-136` (blob `946b4beb`), the *Where the result
lives — deliverables* section, item 2:

```
$ git cat-file -p 946b4beb831c2cb76967fe64ca6ab7fb48f8c612 | sed -n '134,136p'
2. **The review record** — the prose record of what you read, re-executed and found, at
   `migration/document-work-assurance-v3/v3-review-<round>-<subject short
   SHA>.md` (`<round>` = `full` | `verify`; repo naming precedent).
```

**Ground truth violated.**

1. `CONSTRUCTION-CHECKLIST.md:143-147` (`E10`): *"a caller-held path is named, never written as
   a path token — a member's path tokens resolve in this repository … and an artifact living
   only in a caller is given its name and its holder instead, so that a reader following a path
   in this layer cannot land on another repository's bytes or on nothing."*
2. `HARNESS-DECISIONS.md` `§live` `HD-49` (standing, and it outranks the checklist on conflict):
   *「**产品 run 的记录与产物仍留调用者**（承 `HD-28`——记录跟着被记录的对象走：产品 run 的对象是调用者的树）」*.
3. `REVIEW.md` itself, twice. Its opening (`:6-8`) declares *"This file describes a role inside a
   product run. It is not the construction-side contract for reviewing the harness itself"*, and
   `:44-46` says of a product-run FULL record that it *"is held with that run's records in the
   caller that grew this harness rather than here"*. The same member therefore states both that
   the artifact is caller-held and, ninety lines later, a repository path token for it.

**Measured, not reasoned.** Product runs execute in the caller's tree.

```
$ ls -d D:/Thesis-stage-control-refactor/migration
ls: cannot access 'D:/Thesis-stage-control-refactor/migration': No such file or directory   (exit 2)

$ ls D:/Thesis-stage-control-refactor/ResearchSystem/migration/document-work-assurance-v3/v3-review-full-{86defbc,fef3a2e}.md
…/ResearchSystem/migration/document-work-assurance-v3/v3-review-full-86defbc.md
…/ResearchSystem/migration/document-work-assurance-v3/v3-review-full-fef3a2e.md
```

From the caller's root the token resolves **nowhere**; the run's sibling records — including the
two this layer names by hand at `EXECUTION.md:452` and `REVIEW.md:45` — live one directory
deeper, under the caller's `ResearchSystem/`. And where the instrument is mounted, the token
resolves **in the instrument**, into the construction record home `HD-49` reserves for the
instrument's own development history. Both outcomes are the pair `E10`'s clause names: another
repository's bytes, or nothing.

**Nothing else carries the instruction.** `dispatch.py` names the product reviewer's charter
(`ROLE_INSTRUCTION = "document-harness/REVIEW.md"`, `:426`) and no record path; grep for
`v3-review` across `dispatch.py` returns only the charter constant. This section's own stage
marker says why that matters: *"Under the zero-restatement dispatch contract the reviewer learns
its duties from this file alone; the p4-doc FULL was completed correctly and then stopped with
the verdict in-session, because nothing here said where the result goes"* (`:121-126`). The
bytes are the whole of the instruction, and `:128` makes acting on them an obligation — *"A
review is not returned until it is committed. You persist, and commit, exactly two artifacts"*.

**How it got here.** `39a21a8` de-prefixed a token that had been caller-correct:

```
-   `ResearchSystem/migration/document-work-assurance-v3/v3-review-<round>-<subject short
+   `migration/document-work-assurance-v3/v3-review-<round>-<subject short
```

One round earlier, `v3-cold-read-4410899.md` `L-1` reported this exact defect class at
`EXECUTION.md:260` and asserted, under its *Class sweep* heading, *"Exactly one other
placeholder-bearing path token exists in the layer, `REVIEW.md:132`"*. The measured count is two
(§3.3). The sibling it missed is this one, and the round that fixed the reported instance then
mechanically de-prefixed the missed one. This is the failure mode `E10` names when it says a
channel *"narrowed to the reported instance leaves its siblings to be found one re-read at a
time"*, and the one `HD-41` ④ exists to prevent.

**Why must-fix and not low, stated so it can be overruled.** `v3-cold-read-4410899.md` tiered
its instance low on an explicit test — *"no actor is misdirected today"*, because the shipped
`make_paragraph_map.py` assumed precisely the layout the sentence spelled, so a run author
following the text got a working invocation. That test fails here in both directions: from the
caller root the path does not exist, and from a mount it exists but is the wrong repository's,
which `HD-49` forbids. The wrong outcome is not presentational; it is where a returned review
lands.

**Minimum fix.** Stop writing a repository path token for a caller-held artifact — name it and
name its holder, the form `EXECUTION.md:452` and `REVIEW.md:45` already use for product-run
records. Replacing lines 134-136 with:

```
2. **The review record** — the prose record of what you read, re-executed and found: a file
   named `v3-review-<round>-<subject short SHA>.md` (`<round>` = `full` | `verify`; repo
   naming precedent), written beside that run's other records in the caller's own
   document-work-assurance-v3 migration directory. The caller holds it; this layer does not
   write its path.
```

is sufficient and changes no other clause. **Class sweep for the fix** (`E7`, `HD-36` ①):
`grep -c migration/document-work-assurance-v3` over the seven prose members returns
`5 · 8 · 1 · 2 · 0 · 1 · 1` = **18 lines**. Seventeen are construction-side or
instrument-internal and resolve correctly here (`CONSTRUCTION-CHECKLIST.md:4,23,100,101,230`,
`README.md:17,18,19,21,28,33,34,35`, `EXECUTION.md:109`, `REVIEW.md:66`, and the two stubs'
`git show 7011916:` citations, which are source-repo paths). `REVIEW.md:135` is the only
product-run-audience site, so the replacement above is the whole of the class. The wider
placeholder-token class is three sites (§3.3), the other two already in the compliant form.

**Routing is not mine** (`R10`). The record supplies bytes; whether the fix reads as changing
what the deliverables rule *requires* — and so trips `E10`'s design test into a round rather
than the must-fix channel — is the orchestrator's call.

### `L-1` (low; wording-level under `R9`; bytes supplied) — `EXECUTION.md:194` names the instrument's `tooling/tests/` for a fact about the caller's

**Location.** `document-harness/EXECUTION.md:193-195`, inside *Pre-freeze gate* item 1:

> Witnessed cost: audit round 3 f1 — the v2 instruction narrowed `` `tooling/tests/` `` to four
> named paths, `` `build_run.py` ``'s list never received it, and the miss cost one full
> from-scratch round (~176k tokens).

**Ground truth.** The witnessed cost is p5a-shells', a product run in the caller; its
`write_scope` named the caller's `ResearchSystem/tooling/tests/`, and every `build_run.py` in
existence lives under the caller's `ResearchSystem/assurance/runs/*/`. `39a21a8` stripped the
prefix, so the token now resolves to the instrument's own `tooling/tests/` — a different
directory, though a largely mirroring one (the caller's additionally holds `run_tests.py`,
`run_p4_tests.py`, `run_p5a_tests.py`).

**Why low, and why it spawns nothing** (`R9`). The fix changes no actor's action: the
reconciliation rule — *every enumeration the instruction text states is reconciled by
command-output diff against the tree it derives from and the `write_scope` granted* — is
identical whichever tree the anecdote named. No check outcome, evidence binding, permission,
obligation or verdict path moves. The accurate fact is recoverable from the committed record the
same section names (p5a-shells' `audit-rounds.md`, held with its run in the caller) and from the
pre-round blob `6dc79f3f`. **I can name no downstream decision that goes wrong if it stays
unfixed**, so under `R9` it rides the next batch touching this layer and spawns no round and no
read.

**Bytes.** `` `tooling/tests/` `` → `the caller's own tests tree` (or any wording that drops the
token; the sentence needs no path at all).

### `O-1` (observation) — `HD-49` carries `status: implemented` while sitting in `§live`

`HARNESS-DECISIONS.md:30-31`. The file's own header states the invariant *「supersession 与
live→implemented 的挪节都在**同一 commit**」* and defines `§live` as 必读 and `§implemented` as
不必读. `HD-49` is the only one of the ten `§live` entries whose status line reads
`**implemented**`; the other nine read `**live**`, and `§implemented`'s entries read
`**implemented**`. The effect is over-inclusion — a cold reader is required to read an entry the
file's own state machine says is not required reading — and, for a later reader, a false signal
that `HD-49`'s substance still lacks a carrier when `README.md:32` carries part of it.
`HARNESS-DECISIONS.md` is not an `E10` member, its bytes are discipline (`HD-7`), and only the
user flips a state, so this is reported and not routed.

### `O-2` (observation) — this read had no dispatch marker, so `E9`'s window has no mechanical carrier for it

`.harness/` holds `runs.jsonl` alone; `review-pending.json` is absent, and `dtw dispatch --read`
is its only writer (`cli.py:216`). Independently, the tracked hook this checkout runs
(`core.hooksPath` → `.githooks`) calls `layer_path_check.py` and nothing else, so
`review_freeze_check.py` would not have held the window here even had a marker existed — which
`.githooks/pre-commit`'s own comment states as deliberate (*"adding a guard nobody asked for is
what E6 refuses"*). Recorded as the ceiling `R4` asks for and the hint `R7` says not to treat as
a block; the round's authorization is not visible in the repository and I did not look for it
beyond `CONSTRUCTION-LEDGER.md:67`'s recorded debt.

### `O-3` (observation) — the `E2`-frozen exception is doing real work, at five sites

The only unresolved path tokens anywhere in the ten members are the five inside the two frozen
supersessions (§3.3). `E10`'s *"the bytes `E2` freezes are excepted while they are frozen"* is
therefore not a theoretical carve-out but the sole reason the layer's token sweep is not clean,
and `E2`'s recorded-ruling requirement plus `HD-20`/`R10` are what keep them banked. Recorded so
the count is on the record and so that a future re-baseline of the pack is understood to inherit
them. `R5` applies: whether the frozen bytes should carry a repository-path form at all is the
user's question, not mine.

## 5. Coverage disclosure (`R4`)

- **Read in full at the subject blobs:** members 1–7 (1 135 lines), plus member 5 which was
  citable and read anyway. Blob ids in §2.
- **Covered by citation, not re-read:** members 8, 9 and 10 (281 lines) — `v3-cold-read-4410899.md`,
  whose §2 records the same three blob ids and whose §5 discloses all ten read in full. The
  citation was checked against `git ls-tree` before being relied on; it holds on blob identity,
  and the path-column prefix difference is the `DE-PREFIX` rename, which moved no bytes.
- **Read by section, not in full:** `HARNESS-DECISIONS.md` — header (1–27) and `§live` (28–195)
  end to end; `§implemented` (197–505) **grepped only**, for the eleven `HD` ids the members
  cite. `HARNESS-DECISIONS-archive.md` grepped only, for the four of those that resolve there.
- **Read in full outside the layer, because a member's claim turned on it:**
  `tooling/hooks/layer_path_check.py`, `.githooks/pre-commit`, `README.md` (root, 100 lines),
  `document-harness/README.md`'s targets by existence only.
- **Sampled:** `tooling/rsclib/document_harness/cli.py` (dispatch/marker/parser regions),
  `dispatch.py` (constants and prompt), `candidate_path_check.py` (docstring + `NOT_SCANNED`),
  `paths.py` (`TrackedPaths`), `test_precommit_checks.py`, `test_cli_entry.py`,
  `test_dispatch.py`, `test_readme_enumeration.py`, `check_template_instance.py`,
  `instruction.py` (`transcript_audit` only) — each opened at the lines a member's claim names,
  not end to end.
- **Only probed:** the two path guards, by calling `unresolved_tokens` and
  `unresolved_path_tokens` directly on hand-written inputs. I staged nothing and committed
  nothing, so **the hook was never observed firing on a real commit**; that it reaches every
  member rests on `test_precommit_checks.LayerMembership.test_every_member_is_scanned`, which is
  green in the 739-test run above. No mutation testing was performed — a read owes none, and
  `R8`/`E4` bind the round, not this record.
- **Not established:** `EXECUTION.md:385`'s `712 passed in 93.67s` at instrument base `0d73a5f`.
  Re-deriving it needs a checkout of another revision, which would dirty the subject worktree.
  **UNVERIFIABLE at this subject**; the figure is explicitly pinned to that base and the text
  itself instructs re-running rather than trusting it.
- **Marked, not verified:** that this session read cold. It is a process claim with no evidence
  lock (`R4`).
- **Wrote:** this file only. No other file in either repository was created, edited, staged,
  committed or pushed.
