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
