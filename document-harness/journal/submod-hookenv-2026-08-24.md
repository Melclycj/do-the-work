# Round `SUBMOD-HOOKENV` — fix-leg record: errata + quickstart re-walk (2026-08-24)

The shared FULL over `153302a..3d5c705` (`migration/document-work-assurance-v3/v3-review-full-3d5c705.md`)
returned `CHANGES_REQUIRED`; the user approved the fix leg all-in (fix-gate section of
`document-harness/plans/submod-hookenv.plan.md`). This file is the record channel that fix
names twice: the **errata** for the candidate commit body's falsified mutation signatures
(its blocker on the mutation evidence) and its class-scan line drift (its low on the same
section) — the commit body cannot be amended under `E8`, so the correction lives here — and
the **re-walk** of the README quickstart after the missing tracked-hook step was added (its
blocker on the quickstart). The other two approved items — the onboarding long-path
threshold and the README three-hats quantifier — are one-sentence text corrections and live
in the fixing commit's diff, not here. Every output below is from a fresh run of 2026-08-24
by the fix executor, immediately before this file was written (`E3`); nothing is copied from
the review record, which is why the two can be compared.

## 1. Errata — the four mutation signatures in `3d5c705`'s VERIFICATION section

**What the candidate body claims, against what re-measurement shows.** The four mutations
were re-applied one at a time to the candidate bytes of
`tooling/rsclib/document_harness/paths.py` (sha256
`9089dc6769af29d63eb3b9c244cb71147bca474f347363c2012dbf2ac86144ba`, the digest the candidate
body itself names), the seven-test module run under each, and the file restored from a
sha256-checked scratchpad copy after every one — never `git checkout --`. Restore verified
against the same digest each time; after the last restore the module runs `7 passed in 7.87s`.

The exact edits, so the table is reproducible:

    M1  delete `env=env` from the `ls-files` call in `_submodule_files`
    M2  delete `env=env` from the `--show-toplevel` probe in `_submodule_files`
    M3  `return listed or None` -> `return listed` (the empty-listing guard, off again)
    M4  in `_repo_local_env_names`, drop `GIT_INDEX_FILE` from git's returned list

Per-mutation, per-test outcomes, measured — short names: **plain** =
`test_a_real_submodule_path_survives_a_plain_commit`, **all** = `…survives_an_all_commit`,
**shadow** = `test_the_superprojects_own_files_do_not_answer_for_the_mount`, **work-tree** =
`test_a_redirected_work_tree_does_not_reach_the_mounts_own_question`, **empty** =
`test_a_mount_whose_index_lists_nothing_is_out_of_index`, **ctl-mount** =
`test_a_nowhere_path_under_the_mount_is_still_blocked` (must-fire control), **ctl-super** =
`test_a_nowhere_path_in_the_superproject_is_still_blocked` (must-fire control):

    M1   plain PASS   all FAIL   shadow FAIL   work-tree FAIL   empty PASS   ctl-mount FAIL   ctl-super PASS
         ========================= 4 failed, 3 passed in 7.85s =========================
    M2   plain PASS   all PASS   shadow PASS   work-tree FAIL   empty PASS   ctl-mount PASS   ctl-super PASS
         ========================= 1 failed, 6 passed in 7.90s =========================
    M3   plain PASS   all PASS   shadow PASS   work-tree PASS   empty FAIL   ctl-mount PASS   ctl-super PASS
         ========================= 1 failed, 6 passed in 8.11s =========================
    M4   plain PASS   all FAIL   shadow FAIL   work-tree PASS   empty PASS   ctl-mount FAIL   ctl-super PASS
         ========================= 3 failed, 4 passed in 7.87s =========================

**What this corrects.** The candidate body's M2 and M3 rows reproduce exactly. Its M1 and M4
rows have the right counts and the wrong identities, both times in the same direction: it
lists the **plain-commit pin** among the failures, and the fourth (M1) / third (M4) failure
is actually the **`ctl-mount` must-fire control**. The plain-commit pin passes under both.
Consequently the body's summary sentence — *"The two must-fire controls … stay green under
all four, so the mutations kill the defect pins without killing the guard"* — **is false and
is withdrawn**: `ctl-mount` goes red under M1 and under M4.

**The mechanism, so the corrected table can be read rather than memorised.** Under M1 and M4
the inherited hook environment reaches the mount's `ls-files` again, and in the plain-commit
shape (`GIT_INDEX_FILE=.git/index`, relative) that listing is empty — but the fix's second
half, `return listed or None`, survives the mutation and converts the empty listing into
*this mount is unlistable*. The mount goes `OUT_OF_INDEX` for everything under it: a real
submodule path is no longer reported as resolving nowhere (the defect pin passes), and a
nowhere path under the mount is no longer blocked either (the control fails). The mutation
turns the relative-index branch from a false block into a **silent blind spot**, which the
defect pin cannot distinguish from correctness — only the must-fire control can, and it is
what goes red. This is also why no single-point mutation kills the plain-commit pin (the
review record's observation on `plain`, confirmed by the table above): that test goes red
only on the pre-fix tree, where both halves are absent; either half alone turns it green —
one by answering correctly, the other by going blind — so `ctl-mount`, not `plain`, is what
distinguishes the two halves on that branch.

## 2. Errata — the `HD-41` class-scan line numbers for `paths.py`

The candidate body's five `paths.py` rows are off by three at the committed revision; the
call-site enumeration itself is complete (the review record re-derived all twenty sites and
the membership matched). Corrected offsets, measured against the same bytes
(`9089dc67…44ba`):

    $ grep -n '\["git"' tooling/rsclib/document_harness/paths.py
    124:        ["git", "rev-parse", "--local-env-vars"],
    169:        ["git", "-C", str(mount), "rev-parse", "--show-toplevel"],
    184:        ["git", "-C", str(mount), "-c", "core.quotepath=off", "ls-files"],
    243:            ["git", "-C", str(root), "-c", "core.quotepath=off", "ls-files", "-s"],
    330:        ["git", "-C", str(repo_root), "diff", "--cached", "-U0", "--", path],

    claimed  121  166  181  240  327     (resolve to prose or unrelated lines)
    actual   124  169  184  243  330

## 3. The quickstart, re-walked as one sequence

The README's quickstart block gained its missing step — the tracked half of hook wiring, a
hook script in the tree committed executable, placed **before** the `core.hooksPath` step —
and was then executed end to end, in order, against a fresh repository that had never seen
the instrument, with `<mount-path>` substituted as `vendor/dtw`. The caller: a scratch
repository outside both trees with one prior commit (`README.md`, `docs/note.md`).

Step 0 — the runtime dependencies:

    $ python -m pip install "jsonschema>=4.18" referencing
    Requirement already satisfied: jsonschema>=4.18 in c:\users\j3236\...\python313\site-packages (4.25.1)
    Requirement already satisfied: referencing in c:\users\j3236\...\python313\site-packages (0.37.0)

Step 1 — mount and pin, from the published remote, no local-clone stand-in:

    $ git submodule add https://github.com/Melclycj/do-the-work.git vendor/dtw
    Cloning into '.../caller/vendor/dtw'...
    $ git submodule status
     1a0a200dc24b14ccd48c32d9aa9c8513031c5ce2 vendor/dtw (heads/main)

Step 2 — the mechanical half of onboarding:

    $ python vendor/dtw/tooling/dtw.py init --repo-root .
    created  : .harness/
    created  : .harness/scan-surfaces.json
    created  : HARNESS-DECISIONS.md
    created  : HARNESS-RIDERS.md
    created  : .gitignore
    ignore   : .gitignore gained `.harness/`
    NOT done by this command — these are the procedure's, and are judgment:
      ...
      - wire a pre-commit hook, and run the per-machine core.hooksPath step
      ...
    RESULT: 5 created, 0 left as found (exit 0)

Step 3 — the tracked half of hook wiring (the step the first form of the block did not
have; the hook authored is the one the README now quotes, `vendor/dtw` substituted):

    $ mkdir .githooks
    $ cat > .githooks/pre-commit <<'HOOK'
    ...the ten lines the README block carries (wc -l on the authored file: 10)...
    HOOK
    $ git add .githooks/pre-commit
    $ git update-index --chmod=+x .githooks/pre-commit
    $ git ls-files -s .githooks/pre-commit
    100755 7f672c4dff68687328f7a72c800a89d75198350b 0       .githooks/pre-commit

Step 4 — the per-machine half:

    $ git config core.hooksPath .githooks
    $ git config --get core.hooksPath
    .githooks

Step 5 — prove the guard fires, then the negative control. Must-fire first, a nowhere path
in a committed work product:

    $ printf 'See `docs/no-such-file-quickstart-probe.md` for details.\n' >> docs/note.md
    $ git add docs/note.md && git commit -m "quickstart step 5: cite a path that does not exist"
    pre-commit BLOCKED: newly written text names a repository path that exists nowhere:
      docs/note.md: `docs/no-such-file-quickstart-probe.md`
    Fix the path as written, or bypass with --no-verify.
    commit exit=1

Restore from a checksummed copy, then the clean commit — which also lands the tracked hook:

    $ cp ../note.md.bak docs/note.md && sha256sum docs/note.md ../note.md.bak
    b78341abf0b2875c2ad8023062a15ecc2d6e9b0384f2fcac096a6dfd72b4ac2d *docs/note.md
    b78341abf0b2875c2ad8023062a15ecc2d6e9b0384f2fcac096a6dfd72b4ac2d *../note.md.bak
    $ git add docs/note.md && git commit -m "caller: mount the instrument, wire the tracked hook"
    [master 38f4ef7] caller: mount the instrument, wire the tracked hook
     3 files changed, 14 insertions(+)
     create mode 100755 .githooks/pre-commit
     create mode 100644 .gitmodules
     create mode 160000 vendor/dtw
    commit exit=0

**Held, as a sequence:** the reader who follows the block verbatim now ends with a hook that
was seen to refuse and a clean commit that carries it — against the first form, where the
same reader ended with `core.hooksPath` naming a directory nothing had created, a step-4
"refusal" that committed silently at exit 0, and every reason to believe a guard was
running.

**Ceilings of this re-walk, stated rather than implied.** Same machine that grew the
harness, walker an agent following its own corrected text, Windows only — all three carried
over from the walk record unchanged. The pinned revision is the published `1a0a200`, which
predates this repository's `paths.py` hook-environment fix: the re-walk's subject is hook
*wiring*, no staged document cites a mount-internal path, so neither direction of that
defect is exercised here. And the interpreter note in the README preamble is a live caveat,
measured again: the hook's probe picked `python3` (a Python 3.12) —

    probe picks: python3
    3.12.10 C:\...\WindowsApps\...\python.exe
    deps import: ok

— while step 0 run verbatim installs into `python` (a Python 3.13). Both carried the
dependencies on this machine, but step 0 did not itself provision the probe's pick; a
machine where only `python` has them ends step 5 with a hook that fails every commit on
`ModuleNotFoundError`, which is exactly the onboarding file's warning and the reason the
preamble points at it.
