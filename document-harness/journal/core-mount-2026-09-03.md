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
