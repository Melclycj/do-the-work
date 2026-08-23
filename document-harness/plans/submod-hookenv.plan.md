# Plan — batch `SUBMOD-HOOKENV` (paths.py hook-environment fix; shares one FULL with `STRANGER-PROOF`)

> **Status: open.** Written 2026-08-24 on the user's approval ("批开小批修"). Queue position:
> immediately after round `STRANGER-PROOF`'s candidate (`e620b43`, complete, unreviewed) and
> **before** the shared review — the user postponed `STRANGER-PROOF`'s FULL (2026-08-24) so
> that **one FULL covers both work units** in a single subject range, base at the last
> reviewed tip `153302a`. A cold session reads this file, then `stranger-proof.plan.md`, then
> `CONSTRUCTION-LEDGER.md`'s current pointer, then works. Role form: `E1` as amended —
> executor is a cold `claude -p` session; the orchestrator lands no commit while it runs.

## The defect (found by the `STRANGER-PROOF` walk; evidence in its walk record and rider `submod-hookenv`)

Round `STRANGER-GUARDS`' submodule-path recognition does not hold **inside a pre-commit
hook** — the only place the guard actually runs. Root cause, located with controls by the
walk: git invokes hooks with a **relative `GIT_INDEX_FILE`** in the environment; the code
lists a submodule's index without clearing or resolving it, reads a nonexistent index, and
gets **zero lines with exit 0** — silently bypassing its own fallback. Measured: same tree,
with the variable 0 lines, without it 369. Manual runs are unaffected, which is why the
defect survived that round's tests. It also re-blocks rider `decited-paths`' caller-side
redemption and affects the original caller, which runs these guards from the submodule.

## Change surface

| surface | what changes |
|---|---|
| `tooling/rsclib/document_harness/paths.py` | Clear or absolutize `GIT_INDEX_FILE` (and any sibling `GIT_*` path vars the class scan shows matter) around the submodule `ls-files` invocation, so hook-context listing sees the real index; a zero-line listing with a gitlink present stops passing silently if the fix's shape makes that reachable. |
| `tooling/tests/…` | A subprocess test that **reproduces the hook environment** (relative `GIT_INDEX_FILE` set, cwd as git sets it) and pins the defect class — red before the fix, green after — plus a negative control proving the in-repo scan still binds (`E4`/`E7`; precedent `TEMPLATE-LIB-ROOT`: in-process green is how this class hides). |
| `HARNESS-RIDERS.md` | Redeem `submod-hookenv` by deletion in the same commit (`R10`). `decited-paths` untouched here — its redemption is caller-side and follows once this lands. |

**Out of boundary, deliberately:** the nine `E10` members; `E2`'s sixteen frozen files;
everything `STRANGER-PROOF` owns (README, ONBOARDING, walk record); the caller-side link
fixes; any `git push`.

## Review

No FULL of its own. The **shared FULL** dispatched after this batch's candidate lands covers
`153302a..<tip>` — both work units, the swallowed-commit disclosure chain included. `E9`
budget for the combined subject: that one FULL, at most one user-approved fix, one targeted
VERIFY.

## Expectations the shared FULL can hold this batch to

- The hook-environment test fails on the pre-fix tree and passes after (output pasted), with
  its negative control; battery green at the candidate revision.
- The walk's measured contrast (0 lines with the variable, 369 without) reproduces on the
  fixed tree as equal counts.
- Rider row deleted in the fixing commit; candidate body carries kind, `E1` disclosure,
  `HD-41` class-scan output (all `GIT_*` env consumers around submodule listing), and re-run
  measurements (`E3`).
