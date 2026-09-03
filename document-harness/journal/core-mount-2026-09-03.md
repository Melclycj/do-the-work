# Round journal — `CORE-MOUNT` (batch `CORE-MOUNT`, one round)

Opened 2026-09-03 on the user's "ok" at the `E11` card, base `05ae1b6` (the `dev` tip at
opening; the plan's rulings 1–4 are the four answers taken off the card, every recommendation
as put). Chain so far: open (this commit) → read dispatched at that tip.

`HD-69` executor session id: recorded here by the orchestrator by hand when the executor is
dispatched (the command-face support belongs to batch `EXECUTOR-LIFECYCLE` and is not built).

Decision points, resumes and rulings are appended below as they happen, each dated. A
committed judgment in this file is corrected forward, never rewritten (`HD-59`).

## Measurements before the card (2026-09-03, at `05ae1b6`)

Kept here because the plan carries the conclusions and this is where the readings live.

- **Product tier and repository**: `git ls-files` over the fourteen product-tier paths →
  **60**; `git ls-files | wc -l` → **438**. `CONSTRUCTION-INDEX.md` says 59 / 421 at
  `8ce93f7`; the difference is `schema/document-assurance-v3/bind-declarations.schema.json`
  (round `PROMISE-PATH-ENGINE`) on the tier side and that batch's records and tests on the
  repository side.
- **The probe**: a `--no-checkout` clone in the session scratchpad; the fourteen paths as
  `--no-cone` patterns without a leading slash → 60 tracked files on disk;
  `CONSTRUCTION-LEDGER.md`, `HARNESS-DECISIONS.md`, `document-harness/CONSTRUCTION-CHECKLIST.md`
  and `tooling/construction_dispatch.py` absent; `python tooling/dtw.py --help` exit 0. A
  later `find` counted 62 — the two extras were `__pycache__/*.pyc` written by that `dtw`
  run, not tracked files. The same fourteen lines with CRLF endings on `--stdin` → 60 again
  (`git sparse-checkout list` shows the patterns without `\r`); the CRLF file expanded by
  the shell into a `git ls-files --` pathspec → **8 of 60**. This checkout runs
  `core.autocrlf=true`.
- **Where a caller could learn the step today**: `grep -n -i 'sparse\|core-only\|core only'`
  over `document-harness/ONBOARDING.md`, `README.md`, `document-harness/README.md` → 0 hits.
- **Members since the last read** (`v3-cold-read-c50362c.md`, committed `13fde05`): four
  blobs changed — `RULES.md` `f4d5698`→`a9cd92d`, `README.md` `1ddb7e0`→`f12d584`,
  `REVIEW.md` `71707a3`→`e6199bc`, contract `de21077`→`7cba2ac`; `EXECUTION.md` `08fa87f`,
  `ORCHESTRATION.md` `3f9cd61`, `paragraph-map.schema.json` `09aa869` and
  `CONSTRUCTION-CHECKLIST.md` `97ed956` unchanged.
- **Battery** at `05ae1b6`: `python -m pytest tooling/tests -q` → 956 passed, 199.77s.
- **`§live`**: eleven entries, read in full by the orchestrator before the plan was written.
- **Ledger**: `ledger_cap_check.py` exit 0 before this round's entry; eleven top-level
  entries, bound twenty, per-entry bound 1,000 characters.

## `E1` statement

This session is the orchestrator (work side). The executor is a separate cold `claude -p`
session; the reviewer and the reader are cold. The norm the three-roles table states; no
exception channel is taken. The executor holds none of `R1`'s four holdings.

**Read (2026-09-03).** Dispatched at tip `73bfe1e` (`python tooling/construction_dispatch.py
--read 73bfe1e`), one cold `claude -p` on `opus`, `--disallowedTools WebFetch WebSearch`,
`--permission-mode acceptEdits`, git allowed only as read-only subcommands (`log`, `show`,
`ls-tree`, `rev-parse`, `diff`, `ls-files`, `cat-file`, `status`, `grep`, `blame`,
`hash-object`, `rev-list`, `branch`, `describe`); session `1d4ccd50-4070-4b3f-a4a7-1718b4b7e75d`,
49 turns, 903 s. Record `v3-cold-read-73bfe1e.md` committed unchanged at `d0d029a`, the freeze
marker deleted in that act; no commit landed inside the window. **0 must-fix, 2 low, 2
observation**; the reader took nothing by citation — eight files end to end — and its §3
discharges the three deferrals `PROMISE-PATH`'s closeout named (`15e5ccc`, `61afc26`,
`b9710af`), each found standing. Battery 956 by the reader; 0 unresolved path tokens over the
whole standing text; 40 markdown links resolving; `sweep_refs` 13 NAMETOK unchanged.

**Disposition (2026-09-03), the user's "1 入 bank 2 用 3 记录 4 转".** L-1 (the `R3` /
`REVIEW.md:264-268` verdict collision at a VERIFY) is banked as rider
`verify-specgap-precedence` — design, no bytes, both targets named, deadline the first
product-run VERIFY that records `instruction_completeness: INCOMPLETE` with a blocker standing.
L-2 (`REVIEW.md:129`'s "the whole frozen package") takes `E10`'s free channel with the
record's exact bytes; the orchestrator's two findings: the application adds no clause and
changes no rule's requirement (the FULL's subject was already one dispatched SHA by `E12` and
by `REVIEW.md`'s own *When the subject is one commit*), and no round has relied on the cell
(an outcome would not have changed had it read otherwise); its independent read rides the
next read of this layer. This is the third arrival of rider `wl-route`'s deadline event; the
route taken is `E10`'s enumeration and `R10`'s routing sentence, as `1c18e4a` and `b9710af`
took it; the row stands. O-1 (the ReviewResult's commit has no named owner in `R6`'s text
after the `record-commit-owner` fix) and O-2 (a VERIFY's stated scope excludes the
instruction map while every result must carry an instruction-completeness recheck — `R5`'s
question, put to the user) stay in the record; the user chose to record O-2 and not open it.
`HD-70` flips `implemented` → `retired` in the disposition commit, its carrier being the read
record `d0d029a` (`HD-2`), every earlier word of its status line kept (`HD-59`). Acceptance 4
is written forward in the plan to name this commit's one member change. Plan step 2 checked.

**Executor (2026-09-03).** Dispatched at tip `8ecc7a5` (`python
tooling/construction_dispatch.py --construction-executor`, plus this plan as the instruction),
one cold `claude -p` on `opus`, `--disallowedTools WebFetch WebSearch`, `--permission-mode
acceptEdits`, git and the shell read/write tools allowed; session
`b2720689-5f0a-44d4-b1f4-668d7b018348`, 105 turns, 1816 s. **No decision-point stop**:
`HD-69`'s single-session form held but nothing in the work outran the plan's four rulings, so
the executor ran START-to-report without a resume. Two commits, both inside the *Change
boundary*:

- `4d2bf42` `V3-CORE-MOUNT-MANIFEST-AND-STEP-v1` — `document-harness/product-tier.txt` (15
  lines, self-including), `tooling/tests/document_harness/test_product_tier_manifest.py` (5
  assertions), `document-harness/ONBOARDING.md` item 1b and the "Nine items"→"Ten items"
  header fix, `CONSTRUCTION-INDEX.md` row 9 + row 3's five full paths + re-measured figures
  (61/443, row 2 → 15) + the manifest-reading *How to re-measure*, and the two rider touch
  records (`figure-units` fourth touch, `onboarding-carries-construction` arm (a) third
  touch), neither redeemed.
- `4020efa` `V3-CORE-MOUNT-PROTECTED-SET-SIX-v1` — ruling 2's own commit for rider
  `protected-set-says-five`: contract `:300-302` (the enum gains `bind_authorization_ref`)
  and `:335-340` (one live write path of five → two of six), `CONTRACT-V4-SIGNATURE.md`'s
  ninth post-signature entry, `summary.py:202`, `test_run_v2_template_bind.py:1041`, the row
  deleted. The commit body carries the `E2` disclosure site by site, the `HD-63` class
  argument (fact true at signing, falsified by `97cc298`; no new family entry), the `HD-41`
  ④ class scan, and a "BOUNDARY, STATED RATHER THAN ASSUMED" paragraph noting that ruling 2
  ("boundary grows by the five paths the *Change boundary* lists") governs over design
  decision 2's general "no member touched".

**Acceptance at `4020efa`, as the executor pasted it**: the probe clone materialized 61
tracked files == `git ls-files --` over the manifest's 15 lines, the four construction files
(`CONSTRUCTION-LEDGER.md`, `HARNESS-DECISIONS.md`, `document-harness/CONSTRUCTION-CHECKLIST.md`,
`tooling/construction_dispatch.py`) absent, `dtw --help` exit 0; the manifest test 5 passed
with four mutations red (drop a line → (b); append `CONSTRUCTION-LEDGER.md` → (d); misspell a
row path → (a); corrupt a *Where* token → (b)) and the unmodified control green, each restored
from sha256-checked scratch copies; battery 961 (956 + 5, none removed); both guards exit 0.
The orchestrator re-ran the manifest test (5 passed) and both guards (exit 0) at this tip, and
re-ran the whole battery before dispatching the FULL.

**Two member changes over the round range**, both declared not discovered, which is what the
FULL adjudicates:

```
$ git diff --stat 05ae1b6..4020efa -- <the seven E10 members>
 contract/Document-Work-Assurance-Contract-v4.md | 16 +++++++++-------
 document-harness/REVIEW.md                      |  2 +-
```

`REVIEW.md:129` is the disposition's free-channel L-2 application (`8ecc7a5`); the contract is
the authorised `protected-set-says-five` redemption (`4020efa`). Plan steps 3–4 checked.

