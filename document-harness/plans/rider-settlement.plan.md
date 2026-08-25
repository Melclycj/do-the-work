# Plan — round `RIDER-SETTLEMENT` (bank settlement: redeem ten, retire four)

> **Status: open.** Written 2026-08-25 on the user's direction ("先把 rider 结算一下吧，有点太多了").
> Queue position: head, taken directly after round `README-BILINGUAL` was recorded as
> exempted. A cold session reads this file, then `CONSTRUCTION-LEDGER.md`'s current pointer,
> then works. Role form: `E1` as amended — the executor is a cold `claude -p` session; the
> orchestrator lands no commit while it runs.

## Why this round exists

The bank held **thirty rows**. An inventory taken 2026-08-25 (each row re-measured against
today's tree, line numbers re-derived) sorts them four ways:

| class | rows | what they are | route |
|---|---|---|---|
| redeemable now | 10 | bytes already supplied, or the fix copies a shape already verified in this repository | this round |
| design | 13 | the fix adds a clause or a bound, so `R10` sends them to a round-eligible batch | deferred, see below |
| ruled-not-to-do / unreachable | 4 | the user has already ruled twice, or the touch condition can never arrive | retired this round |
| standing / re-scoped | 3 | not one-shot redemptions at all | untouched |

## Opening rulings (user, 2026-08-25 — this section is their carrier)

1. **Round form: light.** The opening cold read is waived; the independent FULL is kept. The
   layer is clean going in — cold read `21dad76` read all nine members end to end and
   discharged every outstanding debt, and no member has been edited since except
   `153302a`, which is an amendment paired with its own re-read. **Disclosed cost:** this
   round's own two member edits (`EXECUTION.md`, `document-harness/README.md`) are owed an
   independent read, which falls to the next round's opening.
2. **The four ruled-not-to-do rows are retired by deletion**, not left standing with a note.
   Each one's ruling already has a home in the decision log or the ledger; the row is a
   second copy.
3. **The thirteen design rows join the `dispatch-economy` batch**, which is already queued
   and already opens the same surfaces: nine of them (six on the checklist's `E9`/`E10`/`R9`/`R10`
   wording, three on `ORCHESTRATION.md`'s obligations table) are collectable there in one pass.
   The remaining four are machine questions (`pin-drift`, `delta-prose`, `argv-cap`,
   `freeze-audit`) and stay banked for a separate ruling.

## Change surface

| surface | rider(s) | what changes |
|---|---|---|
| `document-harness/EXECUTION.md:365` | `py-convention` | The bare `python -m pytest -q` gains the interpreter convention already established by batch A — one sentence covering the file, in the shape `README.md:100` uses. **`E10` member edit.** |
| `assurance/templates/run-v2/README.md:13,15,17,19,20` | `py-convention`, `readme-three` | Same convention sentence for the four bare-`python` invocations; and "the three step scripts" is qualified to the three round steps, so a reader counting scripts does not miss `run_retire.py`. |
| `document-harness/README.md:30` | `onboarding-labels`, `move-cost-member-site` | One line, two riders: the five parenthetical labels are completed to cover onboarding item 2, and the "a caller wanting them elsewhere moves them" clause gains the measured cost — a later `init` silently recreates an empty decision log at the default path, which is the path every convention names. **`E10` member edit.** |
| `document-harness/ONBOARDING.md:45,72` | `onboard-clone-decl`, `onboard-cmd-count` | The clone table's `.harness/` row states the consequence (a fresh clone has no declaration, so an edited `scan-surfaces.json` silently reverts to the factory default — re-run `init` in that checkout); and item 1's *See* line stops stating a command count, the same fix the root README took. |
| `assurance/templates/run-v2/run_bind_v2.py:291` | `decl-dup` | The independently rebuilt `"bind-declarations.json"` path uses the module constant at `:73`, closing the copy-class fork. |
| `tooling/rsclib/document_harness/caller.py:166` | `discover-root-env` | **The one real defect.** `discover_repo_root` asks git for the toplevel without clearing git's own location variables, so under `GIT_WORK_TREE` it answers about the environment's repository rather than the probe — the second site of the class round `SUBMOD-HOOKENV` closed. The fix copies that round's shape in `paths.py`: ask `git rev-parse --local-env-vars` for the names, clear them for the query. |
| `tooling/tests/…/test_repo_root_discovery.py` (or its home) | `discover-root-env` | A paired subprocess test pinning the defect class — red before, green after — with the negative control proving normal discovery still binds. |
| `tooling/tests/…/test_run_v2_template_retire.py:105,181` | `retire-suite` | The fixture stops giving every ordered id an `out.txt`, so the kept-count assertion binds its source predicate (deleting `.is_file()` must now turn a test red); and the docstring's `chk-<id>.out.txt` — the fourth double-prefix instance — matches the code. |
| `tooling/tests/…/test_dispatch.py` (class `ExecutorDispatchesGenerateToo`) | `exec-mount-test` | The product-side `--executor` mode gains the mount-layout regression the construction-side mode already has at `:703`. |
| `HARNESS-RIDERS.md` | all ten | Ten rows deleted in the same commit as their fixes (`R10`). |

**Retired by ruling 2, in a riders-only commit after the candidate** (the `STRANGER-GUARDS`
lesson: riders-only lands after the reviewed candidate, never inside it):

| row | why it is retired rather than redeemed |
|---|---|
| `ctx-ground` | user maintained twice (2026-08-06, and again 2026-08-22 at round `PRERUN-RIDERS`): the fix is new machinery, which is `E6`'s wrong direction. |
| `status-key` | user maintained twice (`PRERUN-RIDERS` ruling 4). |
| `self-caller-guards` | user ruled it out of the `HD-48` batch 2026-08-19; its deadline — this repository landing a non-record commit inside a freeze window — has not arrived. |
| `F-c` | its touch condition is `harness-digest-narrowing.plan.md`, a plan already fully consumed; no batch will ever touch it. |

**Out of boundary, deliberately:** the thirteen design rows and the three standing rows; the
seven `E10` members this round does not name; `E2`'s frozen files; the caller repository; any
`git push`.

## Review

Light form per ruling 1: **no opening cold read**; one **independent FULL** over the
candidate, base at the last reviewed tip. `E9` budget: that FULL, at most one user-approved
fix, one targeted VERIFY.

## Expectations the FULL can hold this round to

- The `caller.py` fix is proven by a paired measurement, not by inspection: the same tree
  answers differently with and without `GIT_WORK_TREE` before the fix, identically after,
  with the raw output pasted (`E3`).
- The new and strengthened tests are mutation-checked: deleting `.is_file()` from the retire
  count now turns a test red (it did not before), and the discovery test fails on the
  pre-fix tree.
- Every one of the ten rows is deleted in the commit carrying its fix, and no row is deleted
  whose fix is absent.
- The four retirements carry no fix and claim none.
- Battery green at the candidate revision, count stated against the 851 baseline.
- Candidate body carries kind, the `E1` disclosure, and the `HD-41` class scan for both text
  classes it touches (bare `python` in reader-facing commands; stated command counts).
