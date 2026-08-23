# Plan — round `PUB-FACADE` (publicization batch A: the facade pieces)

> **Status: open.** Written 2026-08-23 at round open. This file is the carrier of the **four
> user rulings of 2026-08-23** below until the round records them; a cold session reads this
> file, then `CONSTRUCTION-LEDGER.md`'s current pointer, then works. Queue note: the queue
> head became the publicization batches by user direction of 2026-08-23 (ledger commit
> `V3-LEDGER-PUBLICIZATION-QUEUE-v1`); the ledger's two open questions — LICENSE choice and
> batch order — are answered by rulings 1 and 2 below.
>
> **Role form — lightweight round, ruled by the user (ruling 3).** Orchestrator and executor
> are ONE session this round: `E1`'s exception channel, taken deliberately. The merged
> session holds **all four** of `R1`'s holdings over the candidate — dispatched by, prompted
> by, scoped by, reported through — so nothing about the candidate's authoring is
> independent, and the candidate commit body states exactly that instead of claiming
> otherwise. What stays independent is the review side: one FULL, dispatched cold by this
> session with the commit range and nothing else, and the `E9` budget is otherwise intact —
> any fix needs the user's approval and obliges the targeted VERIFY.

## The four user rulings of 2026-08-23 (this file is their carrier)

1. **LICENSE = MIT.** Chosen over Apache-2.0. Copyright line: `Copyright (c) 2026 Melclycj`
   (the default offered; the user did not override it).
2. **Batch order = A → B → C.** Facade first (this round), re-signing/packaging second
   (contract v4 batch), stranger-usability third. The ledger's backlog entry is the map.
3. **Lightweight round form.** Three parts, all ruled together when the user chose the
   middle of three offered weights: (a) the opening layer cold read is **waived** — the
   first real exercise of `E10`'s waiver clause, which is rider `waiver-live`'s recorded
   deadline moment. It did not bite this round: the orchestrator had read
   `HARNESS-DECISIONS.md` `§live` in full *before* the waiver was given, so no live ruling
   was missed — but the rider's question (does the waiver reach the `§live` read?) is now
   live and its row takes a touch note, unredeemable here because its fix is design. The
   member reads still owed from round `PRERUN-RIDERS` remain owed and ride the next opening
   read — deferral, never exemption. (b) Work-side roles merged, as the header states.
   (c) One independent FULL retained; `E9` otherwise intact.
4. **`claude-env-bootstrap` declined** for this repository (generic scaffolding on top of a
   repo that carries its own governance would be a second layer with no owner). Recorded so
   the SessionStart hint has an answer on file; no harness surface changes.

## Why this round

The user's direction: make this repository fit to publish as a public git repo. Batch A is
the facade — what a stranger meets in the first minute: a license (legal vacuum otherwise),
CI proving the suite runs on more than the machine that grew it, and a root README whose
assertions are true. Two banked riders fall due exactly here (`readme-cli-stale`,
`posix-mode-wording`), and this round's own opening measurements found two more POSIX
defects that belong to the same facade (see below).

## Opening measurements (this session, base `f7fcbe9` — `E3`: re-run before any claim)

- Windows (Python 3.13.6): `python -m pytest -q` → **790 passed** in 101.56s.
- WSL Ubuntu (git 2.43.0, Python 3.12.3), fresh clone of `f7fcbe9` — the repository's
  **first POSIX run**:
  - With Ubuntu's system `jsonschema` 4.10.3: **571 failed, 483 passed, 30 errors** — every
    failure one root cause, `Draft202012Validator(..., registry=...)` needs
    `jsonschema >= 4.18`. An environment floor, not a code defect; the CI and README must
    carry it.
  - After `pip install -U jsonschema` (4.26.0): **1 failed, 790 passed** — the one failure
    is `test_candidate_checks.py` `VALID_CONFIGS["command_exit"]` executing the literal
    `["python", "-c", "pass"]`; POSIX has `python3`, not `python`. Class scan of literal
    `python` in `tooling/` (5 hits): `:523` is the only *executed* site; `:598` is
    schema-rejection data (never executed); the three comparator sites are refusal-path
    argv data. One fix site: `sys.executable`.
  - Hook at mode 644, `core.hooksPath` set, commit attempted: git 2.43 prints
    `hint: The '.githooks/pre-commit' hook was ignored because it's not set as executable.`
    and commits — **skipped with a hint, not silent**. `ONBOARDING.md` item 9's "silently
    stops running it" is the wrong half of the pair rider `posix-mode-wording` recorded;
    the review record's "skipped with a warning" was right (hint text is suppressible via
    `advice.ignoredHook`, which the fixed sentence should not overclaim against).
  - Positive control (hook at 755, bad path token staged into a layer member):
    `.githooks/pre-commit: 30: python: Permission denied`, exit 127 — the hook itself
    invokes bare `python`, so on a POSIX clone **every commit fails once the hook is
    wired**. Fail-closed by accident, broken in substance. Fix: resolve `python3` first,
    fall back to `python`, loud failure if neither.

## Change surface

| surface | what changes |
|---|---|
| `LICENSE` (new) | MIT, ruling 1. |
| `.github/workflows/ci.yml` (new) | Push/PR: `python -m pytest -q` on `ubuntu-latest` + `windows-latest` × Python 3.12/3.13 (the two measured interpreter versions); deps `pytest jsonschema referencing` with the `>=4.18` floor the measurement established. |
| `README.md` (root) | De-rust per rider `readme-cli-stale`: the CLI-is-not-here bullet, the suite-will-not-be-green bullet, and "No remote." are false today (re-scan the whole file at fix time, `HD-41` — the rider's own line numbers have drifted). Add a suite-dependencies row (pytest + `jsonschema>=4.18`) to the State table and a CI badge under the title. |
| `document-harness/ONBOARDING.md` | Item 9's mode sentence rewritten to the measured behaviour (rider `posix-mode-wording`). |
| `.githooks/pre-commit` | Interpreter resolution: `python3` first, `python` fallback, loud failure if neither (defect found by this round's positive control). |
| `tooling/tests/document_harness/test_candidate_checks.py` | `:523` `sys.executable` for the executed `command_exit` fixture. |
| `tooling/tests/document_harness/test_precommit_hook.py` (new) | Pins the hook-interpreter defect class: runs `.githooks/pre-commit` via `sh` in a scratch repo (exit 0 on a clean tree; exit 1 + loud message when the check script is absent); skips where `sh` is unavailable. Same shape as `test_run_v2_template_library_path.py` — subprocess, because in-process green was exactly how the last dead-script defect hid. |
| `HARNESS-RIDERS.md` | Delete `readme-cli-stale` and `posix-mode-wording` in the same commit as their fixes; touch note on `waiver-live` (deadline arrived 2026-08-23, did not bite, fix stays design — row rides on). |
| `CONSTRUCTION-LEDGER.md` | At closeout only (orchestrator's, not the candidate's). |

**Out of boundary, deliberately:** all ten `E10` members (no `E10-sync` due — the membership
sentence is not touched); `E2` frozen bytes; contract v4 and the signed-file de-rusting
(batch B); `chk-caller-prefixes`, `amend-exempt-caller`, the second-caller onboarding proof,
the ten remaining resolution points (batch C); flipping the GitHub repository to public (the
user's own act, after the batches or whenever the user chooses); any `git push` (`E8`).

## Expectations the FULL can hold the candidate to

- Battery: 790 + the new hook tests, green on Windows; green in the WSL clone at the
  candidate revision (re-measured there, output in the commit body).
- The four README claims named false above are gone; no new unverified claim replaces them
  (the section's own rule: commands over claims).
- Rider rows deleted in the same commit as their fixes; `waiver-live` touched, not deleted.
- Candidate commit body carries: kind, `E1` disclosure (all four holdings held), `HD-41`
  class-scan grep output, and the re-run measurements (`E3`).
