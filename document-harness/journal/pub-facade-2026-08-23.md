# Round `PUB-FACADE` — candidate-revision measurements and their validity

2026-08-23. Lightweight round per plan ruling 3 (`document-harness/plans/publicization-a.plan.md`);
work-side roles merged, disclosed in the candidate commit body. This file holds the
measurements taken at the candidate revision `87004fb`, and — because two measurement
channels failed mid-round — the record of which observations are valid and which were
artifacts of the instrument doing the measuring.

## Valid measurements at `87004fb` (WSL Ubuntu, git 2.43.0, Python 3.12.3, jsonschema 4.26.0)

Fresh clone of the candidate revision:

- Full battery: `792 passed, 865 subtests passed in 11.12s`.
- Wired hook (`core.hooksPath .githooks`), benign commit: lands, exit 0 — the operation the
  pre-fix hook failed on every attempt (base-revision measurement in the plan).
- Positive control, quoting-safe run (see §validity below), all output verbatim:
  the probe line — the word "probe", then a backtick-quoted token naming
  document-harness/no-such-file-xyz.md (a path that resolves nowhere; written here without
  its backticks, because quoting it live is the de-backticking dodge rider `decited-paths`
  records), then the word "token" — lands as the last line of
  `document-harness/EXECUTION.md`, verified verbatim by `tail -1`; then
  - `python3 tooling/hooks/layer_path_check.py` → `pre-commit BLOCKED: newly added
    instruction text names a repository path that does not resolve: …` exit **1**
  - `sh .githooks/pre-commit` → same output, exit **1**
  - `git commit` → same output, exit **1**, HEAD unmoved at `87004fb`
  - benign control commit afterwards: exit **0**.
- RED evidence for the new `test_precommit_hook.py` (E4: neuter → red → restore), run in the
  throwaway clone, never in this repository's tree:
  - pre-fix hook bytes restored via `git show f7fcbe9:.githooks/pre-commit` →
    `test_hook_resolves_an_interpreter_and_runs_the_check` **FAILED** (1 failed, 1 passed);
  - loud-missing line deleted from the hook (`sed -i '/the layer path check did NOT run/d'`)
    → `test_hook_is_loud_when_the_check_script_is_missing` **FAILED** (1 failed, 1 passed);
  - bytes restored → `2 passed`. Restoration was by `git checkout --` **in the disposable
    clone**, not the sha256-scratchpad route `E4` names for a working tree: the mutated bytes
    never existed in this repository, the clone's index was pristine at `87004fb`, and the
    clone was discarded after the green re-run. Named here so the FULL can weigh the letter
    of `E4` against that substance rather than discover it.

Windows measurements are in the candidate commit body: `792 passed in 99.04s`, the two hook
tests running (not skipping — Git supplies `sh`) and passing, which exercises the
`python`-fallback leg of the interpreter probe.

## Measurement validity — two instrument failures, both caught in-round

1. **Exit codes echoed through `wsl.exe` argument passing are unreliable.** Decisive probe:
   `bash -lc "true; echo probe-true:$?; false; echo probe-false:$?"` through `wsl.exe`
   printed `0` for **both**. Every `$?` reported through that channel this round is
   therefore void. Conclusions standing only on verbatim *stdout text* are unaffected: the
   644-mode hint text (plan measurement — the hint line itself was the observation), the
   pre-fix `python: Permission denied` hook failure (the message and the absence of a commit
   success line, not the echoed code, carry it), and every pytest tail line.
2. **An earlier positive-control run was invalid — the probe never landed.** The backtick
   token travelled through three shell layers, one of which executed it as command
   substitution (`…arness/no-such-file-xyz.md: No such file or directory` on stderr) and
   appended a line with **no token in it**; the check then correctly found nothing, the
   scratch commit landed, and the round briefly held the false belief that the guard had
   passed a bad token. The quoting-safe re-run above (script piped over stdin, backtick as
   octal `\140`) is the valid experiment and reverses that belief: the guard blocks. The two
   stray commits this produced existed only in the throwaway clone and were reset away;
   this repository took no commit but the plan and the candidate.
