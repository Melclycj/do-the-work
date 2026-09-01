# Instruction-layer read — subject `51bd4f677ba1bca021c960b08ee560d762f4d2b3`

An `E10` read of the harness's own instruction layer. **Not a round** (`R3`): no budget spent, no
verdict carried; the output is findings tiered must-fix / low / observation. Dispatched with the
charter this repository declares under `rules` in the `harness.json` at its root —
`document-harness/CONSTRUCTION-CHECKLIST.md` — which was read in full, and then the counterpart
that file names, `document-harness/RULES.md`, also in full. `HARNESS-DECISIONS.md`'s `§live` was
read in full at this repository's root, as `E10`'s last clause requires of the opening.

Record name: `v3-cold-read-`. `R6` offers two read filenames and the layer defines no criterion
for choosing between them (rider `read-name-split`, open, re-derived here and not re-banked). I
took `cold-read` for the reason every previous whole-layer opening record took it.

**Findings: 1 must-fix, 1 low, 2 observation.**

---

## 1. The member set and the coverage, both derived

The dispatch enumerated no members (`R2`). `E10`'s own sentence at the subject
(`document-harness/RULES.md:86-94`) reads **exactly seven paths**. Blob ids from
`git ls-tree -r 51bd4f677ba1bca021c960b08ee560d762f4d2b3`, run here:

| # | member | blob at `51bd4f6` | last recorded end-to-end read | this read |
|---|---|---|---|---|
| 1 | `document-harness/RULES.md` | `c47dbc5f256e7888f8bb74c8adde5ba0425f0acb` | `v3-cold-read-006d0d5.md`, blob `5ab152ad…` — **moved** (`3060a23`) | **end to end** |
| 2 | `document-harness/README.md` | `7decb095ff8d93aa209f460805465288f7f973cf` | `v3-cold-read-006d0d5.md`, **same blob** | **end to end** |
| 3 | `document-harness/EXECUTION.md` | `08fa87f8380b60a0af4e125e1bfe88747d26f0e4` | `v3-cold-read-e88094c.md`, **same blob** | **end to end** |
| 4 | `document-harness/REVIEW.md` | `71707a3a01016e86b63238d494df98abbd2408c3` | `v3-cold-read-e88094c.md`, **same blob** | **end to end** |
| 5 | `document-harness/ORCHESTRATION.md` | `3f9cd61ca42c94ca2a3080d13412741173bd73b4` | `v3-cold-read-006d0d5.md`, **same blob** | **end to end** |
| 6 | `contract/Document-Work-Assurance-Contract-v4.md` | `de210772994ee49bf8fa7d7a68510ca49e290a88` | `v3-cold-read-e88094c.md`, **same blob** | **end to end** |
| 7 | `schema/document-assurance-v3/paragraph-map.schema.json` | `09aa869962f592c2f86c9379be0ef3eb7d2232ff` | `v3-cold-read-e88094c.md`, **same blob** | **end to end** |

Plus, not a member, read for the reason `E10`'s second sentence gives:

| — | this repository's declared rule | blob at `51bd4f6` | this read |
|---|---|---|---|
| — | `document-harness/CONSTRUCTION-CHECKLIST.md` | `97ed956be92864dda125cb2ac8970b1375bcc8bc` | **end to end** |

Nothing was taken by citation: every member was read end to end at these bytes. The worktree is
clean apart from an untracked `.goals/` (`git status --porcelain` → `?? .goals/`), so the bytes
read and the bytes at the subject are the same objects — `git hash-object` on each of the eight
paths returns the blob id in the table above.

`harness.json` at this repository's root reads
`{"policy": "CONSTRUCTION-LEDGER.md", "rules": ["document-harness/CONSTRUCTION-CHECKLIST.md"]}`,
which is why the eighth row is here and why `CONSTRUCTION-CHECKLIST.md` is not among the seven.

## 2. What was run

- **Path-token resolution over the whole standing text**, not only added lines — the class
  `E10`'s clause says the guard never re-scans. `unresolved_tokens` and `scanned_paths` imported
  from `tooling/hooks/layer_path_check.py`, applied to each scanned path's bytes at the subject:
  `0 unresolved` for all eight.
- **Markdown links**, which carry no backtick token for the guard to find: 37 link targets over
  the eight files, every one resolving from the file's own directory inside this repository.
- **`python tooling/sweep_refs.py`** from the repository root:
  `-- 13 caller-held or unresolvable references over 8 members and declared rule files`, all 13
  NAMETOK (bare filenames). Each was checked by hand for the holder sentence `E10` requires; all
  13 have one (`the caller that grew this harness`, `the run's`, `the control root lives in the
  caller`, and for `review.schema.json` a blob id in this repository's history).
- **The battery leg `EXECUTION.md` names for this repository**: `python -m pytest -q` run from
  `tooling` → `873 passed in 205.14s (0:03:25)`, exit 0.
- **Contract §5's closed enums against the schemas it claims a single home for**: WorkState
  status, audit result, both verdict lists, the four decision phases, the six `LocalCheckSpec`
  kinds and the two verification modes each match `common.schema.json` exactly; `kind` in
  `local-check-spec.schema.json` is a `$ref` to `common`, so the single-home claim holds.
- **Guard-coverage probe** for the last clause of `E10`'s blind-spot list: both announced-path
  members are inside `scanned_paths`, and `unresolved_tokens` flags a non-resolving token added to
  either (§5, `e10-freeze-exception`).

## 3. The free-channel debt from `3060a23`, discharged

`3060a23` applied two `E10` free-channel byte changes to `document-harness/RULES.md` and recorded
that both still owed their independent read, riding the next read of this layer. Read here, at
per-member cost — the member was read end to end anyway.

- **`:16-18`** (the header's split sentence). `git diff 006d0d5 3060a23` shows a present-tense
  claim — every rule "carries the identifier it has always carried and … the bytes it has always
  carried" — replaced by a historical one about the split. The present-tense claim was false and
  the correction is right: `git log -L` on `E12`'s block returns `894bc92 V3-CORE-ONLY-CODE-FIX-v1`
  removing `` (`dtw dispatch`) `` from its first line — a byte change *after* the split
  (`4b81dd9`) and not one of the two that round disclosed. Adds no clause; changes no rule's
  requirement.
- **`:99-102`** (the appositive deleted from `E10`'s first reader). The deleted words called the
  `dtw dispatch` obligation "stated as an obligation on the command rather than as behaviour
  already built". The behaviour is built: `dispatch.py` defines `declared_rules_line`, and both
  prompts it writes carry it — the review-side prompt at `:579` and `EXECUTOR_PROMPT` at
  `:799-801`. Deletion of a false appositive; adds no clause.

**Both applications stand.** The debt is discharged by this record.

## 4. Findings

### M-1 (must-fix) — the layer names two different actors for the act of committing a returned review record, and both texts reach the same reader

**Where.** `document-harness/RULES.md:240-245` (`R6`): *"you write `v3-review-{full,verify}-…` …
in the worktree; **the orchestrator commits it**, title `V3-REVIEW-RECORD-<ROUND>-<sha>-v1`."*
Against `document-harness/REVIEW.md:150-165` (*Where the result lives*): *"A review is not
returned until it is committed. **You persist, and commit,** exactly two artifacts … The commit
that lands the record is also the act that **deletes the dispatch freeze marker**."*
`document-harness/ORCHESTRATION.md:56` takes `R6`'s side: *"commit the reviewer's record
unchanged, under the title the rule names."*

**Why both bind one reader.** `RULES.md`'s own header says these rules "hold in both directions of
use", and `R6` sits under *Review side — the independent session a dispatch reaches*, which is the
product-run reviewer as much as a construction one. `REVIEW.md:6-9` sends its reader to `RULES.md`
by name. `dispatch.py`'s `ROLE_INSTRUCTION` hands a product reviewer `REVIEW.md`; that file hands
it `RULES.md`; the two then command opposite acts of the same session.

**How it got here, measured.** Before round `CORE-ONLY-LAYER` this clause lived at
`document-harness/CONSTRUCTION-CHECKLIST.md:254-257` (`git show 4b81dd9^`), where it bound the
construction reviewer only and no product-side text contradicted it. `4b81dd9` moved `R6` into
`RULES.md` under the criterion "does a product run obey it", and its own body records *"Nothing
else in R6 moves: the four record filenames, the worktree, and the
`V3-REVIEW-RECORD-<ROUND>-<sha>-v1` title are the source's bytes"* — the bytes were preserved and
the scope widened, and whether the clause is true on the product side was not asked. It has stood
since 2026-08-30 and was not reported by the reads at `e88094c` or `006d0d5`.

**The failure it produces.** A product-run reviewer that follows `R6` leaves the record in the
worktree — which `REVIEW.md`'s own first sentence in that section defines as a review **not
returned** — and the freeze guard then holds the caller's branch (while the marker exists only
record-family paths may land, `review_freeze_check.py`) until some other session commits it. That
is the p4-doc failure the section was written to prevent; its stage marker says so in as many
words. The reverse choice is milder but not free: the reviewer commits, and `ORCHESTRATION.md`'s
obligation to commit the record unchanged — the mechanism `R1`'s *reported through* holding relies
on — has nothing to act on.

**Minimum fix.** One owner, named once. Either `R6`'s clause is qualified to the side it came
from, or `REVIEW.md`'s item 2 and its freeze-marker sentence are changed to match `R6`, with
`ORCHESTRATION.md:56` left as the orchestrator's. **Which of the two is right is not this read's
to conclude** — it decides who performs an act in every future run, so it is the user's, carried
by the orchestrator. No bytes are supplied here for that reason.

**Why must-fix and not low, stated so it can be overruled.** No product run is in flight that this
repository can see (a caller-side fact, `UNVERIFIABLE` from here), so nothing is failing at this
moment. It is tiered must-fix because the defect is not a stale description but two live
imperatives to one session; because either choice breaks an obligation the layer states elsewhere;
and because the cost of the wrong choice is a stranded review and a frozen caller branch rather
than a wrong sentence. If the orchestrator judges that no product run can begin before this
batch's rounds close, low is defensible and the row belongs in the bank.

### L-1 (low) — `R10` identifies the instrument's rider bank by a path token that names the caller's own bank in a caller

**Where.** `document-harness/RULES.md:206`: *"The rider bank (`HARNESS-RIDERS.md`) is the
construction side's internal debt ledger; product-run observations … belong to `HarnessIssue` or
to the caller's own rider bank, **never this one**."*

**Why it misreads in a caller.** `dtw init` writes the caller's own rider bank at the caller's
root under exactly that name — `init_target.py:43-44` maps `rider-bank.md → HARNESS-RIDERS.md` —
and the shipped template's header sends its reader to *"`R10` in the instrument's `RULES.md`"*. So
in a caller the token resolves, at that caller's root, to the very file the sentence's second half
calls "the caller's own rider bank" and its last two words forbid. `REVIEW.md`'s *What is not in
the subject* routes product-run observations to *"a row in the caller's own rider bank"*, so the
two texts point at one file and disagree about it.

**Class sweep** (`E7`, `HD-41` ④), declared scope: every backticked token in the six prose members
naming a file that exists at both this repository's root and a caller's — `HARNESS-RIDERS.md`,
`HARNESS-DECISIONS.md`, `harness.json`, `.harness/…`. Sixteen sites. Fifteen carry a holder
qualifier in the same clause (`at its own root`, `its harness.json`,
`its .harness/scan-surfaces.json`), and `E10:145-152` handles the identical hazard for
`HARNESS-DECISIONS.md` explicitly — *"The file meant is the one in the repository the round runs
in … never the instrument's copy of that name under the mount"*. `RULES.md:206` is the **one** site
without it. `ORCHESTRATION.md:55` names `HARNESS-DECISIONS.md` unqualified but cites `E10`, which
states the qualifier, so the fact is recoverable there.

**The content of the fix** (no clause added, no requirement changed — the requirement is already
"not the instrument's bank"): name the holder instead of relying on the token, in `E10`'s own
mirror-image form — e.g. *"The instrument's own rider bank … is the construction side's internal
debt ledger; product-run observations, schema governance and post-CLOSED admission belong to
`HarnessIssue` or to the caller's own bank, never the instrument's."* Routing is the orchestrator's
under `R10`; this record names the content, which is what `E10`'s free channel asks of a finding
below must-fix.

### O-1 (observation) — the tier enumeration in `EXECUTION.md` does not reach this repository's own doc-path pins

*Regression-battery tiering* binds "a construction batch's pre-commit verification" as well as a
run's evidence pass, and its exception lists the doc paths code or tests pin — "today
`document-harness/README.md` …, the member paths in the layer-path mirror,
`tooling/hooks/layer_path_check.py`, the two shipped instance templates …, and
`contract/Document-Work-Assurance-Contract-v4.md` under
`tooling/rsclib/document_harness/__init__.py`". Measured at the subject, two live pins sit outside
that list: `tooling/ledger_cap_check.py:69` (`LEDGER = "CONSTRUCTION-LEDGER.md"`) and
`tooling/rsclib/document_harness/caller.py:70`
(`DEFAULT_RECORD_SURFACE = ("HARNESS-RIDERS.md", "journal/")`). Both name files this repository
keeps and a caller does not, and `e755d61` ruled that machine out of the travelling tier
deliberately — so naming them in a travelling member would be the defect that commit corrected.
The operative clause is general ("any doc path code or a test pins"), so a batch renaming the
ledger is still tooling-touching; what is missing is any enumeration a construction executor can
consult on this side. Recorded rather than banked: the gap is in this repository's own rule file
rather than in a member, and no decision goes wrong that the general clause does not already catch.

### O-2 (observation) — `R6`'s commit title assumes the record belongs to a round

`R6` gives one title, `V3-REVIEW-RECORD-<ROUND>-<sha>-v1`, and `E8` requires "a single dense title
naming the round". A read is not a round (`R3`), and this read belongs to none: batch
`PROMISE-PATH` runs as two rounds (`ENGINE`, `VOCAB`) and neither has opened. Measured over the 21
commits that added a read record: 19 used the `<ROUND>` form, one rode a round commit
(`V3-DE-PREFIX-v1`), and the most recent — `0ef455c`, the opening read of round 3
`CORE-ONLY-RUN` — used `V3-COLD-READ-RECORD-006d0d5-v1`, a form no rule states. Adjacent to rider
`read-name-split`, which treats the same sentence's *filename* half; if that row is redeemed, this
belongs in the same fix.

## 5. Re-derived independently, already banked — no new rows

Each of these was reached from the bytes before the bank was opened, and each already has a row
with a touch record; none is re-banked (`R10`).

- **`e10-freeze-exception`** — `RULES.md:171`, *"the bytes `E2` freezes are excepted while they
  are frozen"*. Probed rather than argued: both announced-path members are inside `scanned_paths`,
  and `unresolved_tokens` flags a non-resolving token added to either, so no exception exists in
  the guard; and `E2`'s own text says the 2026-08-27 ruling ended the gate, leaving *frozen* a
  name rather than a state. The row already carries the new address after the split.
- **`read-name-split`** — no criterion between the two read filenames. Confirmed: `checkpoint`
  appears in the layer only inside `R6`'s filename list; `cold read` is defined by `E10`.
- **`e10-fifth-reader`** — `E10`'s "Four readers" is short one in this repository:
  `tooling/construction_dispatch.py` reads `rules` and refuses to dispatch without it. The prompt
  that produced this read is that command's output.
- **`e9-pair-budget`** — `E9`'s exception names only the free-channel application while `E10`
  gives the amendment + re-read pair the same zero-budget status.
- **`orch-caller-rule-counterpart`** — `ORCHESTRATION.md:41-44` asserts of any caller's declared
  rule file that it names `RULES.md` as its counterpart.
- **`e10-its-referent`** — the pronoun at `RULES.md:116`.

Checked and **not** stale, against the sentence each mirrors: `layer_path_check.LAYER` is the same
seven paths in the same order as `E10`'s sentence; `README.md`'s row saying how many members there
are defers to that sentence and reads seven; `ORCHESTRATION.md`'s two tables hold nine and three
obligations, which is the twelve `README.md` counts; `README.md`'s onboarding row's ten items
match `ONBOARDING.md`'s ten numbered sections; the fourteen schema files in
`schema/document-assurance-v3/` are each named in `README.md`.

## 6. Coverage and honesty ceilings (`R4`)

- **Read in full**: all seven members, the declared checklist, and `HARNESS-DECISIONS.md`'s
  `§live` (eleven live entries: `HD-69`, `HD-66`, `HD-65`, `HD-62`, `HD-59`, `HD-41`, `HD-36`,
  `HD-35`, `HD-34`, `HD-23`, `HD-9`).
- **Sampled**: `HARNESS-RIDERS.md` — the six rows named above plus every row whose id matched a
  finding of mine, not all 33; the review-record corpus by targeted grep, not read.
- **Probed only**: `tooling/` — `layer_path_check.py`, `sweep_refs.py`, `review_freeze_check.py`,
  `caller.py`, `init_target.py`, `dispatch.py`, `construction_dispatch.py`, `ledger_cap_check.py`
  and the two tests that pin doc paths, each read at the sites a member's claim named. The rest of
  the tree was not read.
- **`UNVERIFIABLE` from here**: everything on the caller's side — whether a product run is in
  flight, whether a caller's hook calls two tracked checks, and the five battery legs whose
  scripts live in the caller's tree. `M-1`'s consequence is stated as a property of the texts, not
  as an observed failure.
- **Process claims are marked, not verified**: byte-level properties were established through
  `git show` at the subject SHA rather than through a console rendering (`REVIEW.md`'s Windows
  read discipline); that this session began cold is a process claim with no evidence lock.
- The freeze marker `.harness/review-pending.json` carries subject
  `51bd4f677ba1bca021c960b08ee560d762f4d2b3`, matching the dispatched subject; the branch tip is
  that same commit, so no commit landed inside this read's window. This repository's own
  `.githooks/pre-commit` does not call `review_freeze_check.py` (its own comment says why), so the
  window here is discipline, not machine — re-derived rather than assumed, as `REVIEW.md` asks.
