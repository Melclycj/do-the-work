# do-the-work — entry file

This repository is a caller of the harness it holds, and this file is its entry point and
nothing more: it points, and every rule belongs to the file it points at.

- **What this repository declares** — `harness.json` at this root: its `policy` field names the
  policy file whose header block says what a round's conclusions do here, and its `rules` field
  names this repository's own rule file, an addition to the harness's own instruction layer
  rather than a member of it (`E10`).
- **Where a round resumes** — `CONSTRUCTION-LEDGER.md`'s current-pointer entry: which
  construction batches are CLOSED, which are open, and what the next queue head is. A cold
  session reads the open batch's plan under `document-harness/plans/`, then that pointer.
- **The governance registers, beside this file** — `HARNESS-DECISIONS.md` (user rulings; every
  round's opening reads its `§live`), `HARNESS-RIDERS.md` (banked findings), and
  `CONSTRUCTION-INDEX.md` (which files travel to a caller and which stay here).
