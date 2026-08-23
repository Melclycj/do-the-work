# Second-caller walk — round `STRANGER-PROOF`, 2026-08-24

The record of item 1 of the round: a repository that had never seen this harness, taken through
[`ONBOARDING.md`](../ONBOARDING.md)'s nine items exactly as written, in order, with the command
run and its pasted output per item and the item's own *See* check either held or recorded as a
finding. The 2026-08-19 walk that wrote the procedure was executed by its author against a
throwaway caller; this one exists because that run's own closing paragraph said a real second
caller was what would close its last two ceilings.

Deviations here are findings, never silent adaptations. Where an item did not work as written,
what happened is below, and the fix — for the sites this round's declared change surface reaches
— is in the same candidate. Where the fix is outside that surface it is reported, not applied.

## Honesty caps, before anything else

- **Same machine.** The walker ran on the machine that grew the harness. This walk closes *the
  flow works as documented on a second layout*; it cannot close *a stranger on another machine
  succeeds*.
- **The walker is an agent**, following the file as an executor under dispatch, not a human
  stranger meeting it cold. A procedure an agent can follow is not thereby a procedure a person
  finds legible.
- **Windows only.** Nothing here ran on POSIX. The CI matrix covers the test suite on Ubuntu; it
  does not cover this procedure.
- **One ceiling did close.** The submodule source was the published remote, not a local clone of
  uncommitted work — the first of the three ceilings the 2026-08-19 run stated.

## The caller

Fresh repository at `D:/Project/Ongoing/stranger-proof-work/second-caller`, a sibling of this
repository and not inside it — the common path of the two is their shared parent:

```
$ python -c "import os;print(os.path.commonpath([<second-caller>, <do-the-work>]))"
D:\Project\Ongoing
```

Every `docs/…`, `lib/…`, `manuscript/…` and `.githooks/…` path below is **that** repository's,
not this one's; they resolve there and nowhere here, which is what makes them worth quoting.

The layout was chosen to share nothing with the first caller's, because a walk on the same shape
tests the shape and not the procedure:

| | first caller | this caller |
|---|---|---|
| mount path | `ResearchSystem/harness` (two deep) | `lib/vendor/assurance-harness` (three deep) |
| agent entry file | `CLAUDE.md` and `AGENTS.md`, mirrored | `AGENTS.md` alone |
| policy file | a fixed root-level name | `docs/policy/assurance-policy.md` |
| ledger | root-level | `docs/policy/work-ledger.md` |
| decision log | repository root | `docs/policy/decisions.md` — moved, per item 3 |
| returned records | the shipped default directory | `docs/policy/reviews/` — declared |
| scan surfaces | shipped defaults | edited, because of every row above |

Its six commits: `d0a4d45` seed · `f5e1f8e` mount · `519fb1b` items 2–4 · `3a53531` items 6–9 ·
`271910c` a returned record · `fbda824` a second one.

## Item 1 — mount the instrument as a submodule, and pin a revision

```
$ git submodule add https://github.com/Melclycj/do-the-work.git lib/vendor/assurance-harness
Cloning into 'D:/Project/Ongoing/stranger-proof-work/second-caller/lib/vendor/assurance-harness'...
exit=0

$ git submodule status
 1a0a200dc24b14ccd48c32d9aa9c8513031c5ce2 lib/vendor/assurance-harness (heads/main)

$ ls lib/vendor/assurance-harness/tooling/dtw.py
lib/vendor/assurance-harness/tooling/dtw.py

$ git ls-files -s .gitmodules lib/vendor/assurance-harness
100644 97a67e668e63124514f76543ef3393db22a7c37c 0	.gitmodules
160000 1a0a200dc24b14ccd48c32d9aa9c8513031c5ce2 0	lib/vendor/assurance-harness
```

**Held**, with two things worth stating exactly.

*The source was the real remote.* Credentials reached it — `git ls-remote --heads origin` printed
`1a0a200dc24b14ccd48c32d9aa9c8513031c5ce2 refs/heads/main` — so this walk pinned a published
revision rather than a local clone of uncommitted work. That revision is five commits behind this
repository's tip, and the difference is inert for the walk: `git diff --name-only 1a0a200..001816f`
enumerates exactly five files — `HARNESS-RIDERS.md`, `document-harness/ORCHESTRATION.md`, this
round's plan and its two read records — and none under `tooling/`, `schema/`, `contract/` or
`assurance/`. The instrument machinery walked is byte-identical to the tip's.

*The long-path caveat is real but conditional, and was measured rather than assumed.* No
`-c core.longpaths=true` was needed here. The longest path under the mount is 182 characters
against the 260 limit, of which 129 are the relative path and 52 the caller's root prefix — so the
first root prefix that trips it is 130 characters. The 2026-08-19 run met it because its root was
deeper, not because this tree cannot be cloned without the flag.

The third command of the *See* row is where this walk first went wrong, and it is item 1's rather
than item 9's — see **F-2**.

## Item 2 — `.harness/`, and its ignore entry

```
$ python lib/vendor/assurance-harness/tooling/dtw.py init --repo-root .
target   : D:\Project\Ongoing\stranger-proof-work\second-caller
created  : .harness/
created  : .harness/scan-surfaces.json
created  : HARNESS-DECISIONS.md
created  : HARNESS-RIDERS.md
created  : .gitignore
ignore   : .gitignore gained `.harness/`
RESULT: 5 created, 0 left as found (exit 0) — no verdict on whether this repository is onboarded

$ git check-ignore -v .harness/x
.gitignore:1:.harness/	.harness/x
```

**Held.** `init` did items 3 and 4 in the same act, reported every path it touched and every one
it left alone, and claimed no verdict about the repository.

## Items 3 and 4 — the decision log and the rider bank

The *See* rows ask three things: that the copy is verbatim, that the header carries `io-design`
§6's five plus narrowing, and that a second `init` refuses to overwrite.

```
$ grep -n -E '^> \*\*(State machine|Scope|Admission|Who reads it|Deletion|Narrowing)' HARNESS-DECISIONS.md
11:> **Who reads it.** ...                    15:> **Admission — three questions ...
20:> **State machine.** ...                   26:> **Scope.** ...
30:> **Narrowing is not a fifth state.** ...  33:> **Deletion — discipline, no lint.** ...

$ python .../dtw.py init --repo-root .          # second run
kept     : HARNESS-DECISIONS.md — already existed, left untouched
kept     : HARNESS-RIDERS.md — already existed, left untouched
RESULT: 0 created, 4 left as found (exit 0)
```

**Held**, all three. The verbatim claim was checked by hash rather than by `diff`, because `diff`
against `git show` reported every line as changed and that reading was wrong: the blob is stored
LF and the worktree is CRLF under `core.autocrlf=true`, which is a checkout artefact and not a
copy defect. Worktree template against written instance, byte for byte:

```
mount worktree template          bytes=  3521 CRLF=  61 bareLF=   0 sha256=70abe4858c3dfadf
caller instance                  bytes=  3521 CRLF=  61 bareLF=   0 sha256=70abe4858c3dfadf
mount worktree rider template    bytes=   657 CRLF=  12 bareLF=   0 sha256=86e8fa1bb2bd1417
caller rider instance            bytes=   657 CRLF=  12 bareLF=   0 sha256=86e8fa1bb2bd1417
```

Item 3's *Do* row also offers a move. Taking that offer is where **F-4** starts.

## Item 5 — the journal, deliberately not pre-created

```
$ find . -type d -name journal | grep -v assurance-harness
(no output)
```

**Held.** `init` created no journal directory anywhere in the caller.

## Items 6, 7 and 8 — ledger, policy file, entry-file pointer

Written by hand, as the items say. The ledger went to `docs/policy/work-ledger.md` with a 60-line
cap declared and nothing enforcing it; the policy file to `docs/policy/assurance-policy.md`,
naming the ledger and its parameters, where rulings and unresolved findings go at closeout, and
which guards this caller runs; the pointer to `AGENTS.md`.

```
$ grep -n "assurance-policy.md" AGENTS.md
8:`docs/policy/assurance-policy.md`.
```

**Held.** Item 8's colder test — that a session starting in that repository knowing nothing about
the harness reaches the policy file by reading only the entry file — is satisfied by construction
here and is *not* independently evidenced, because the walker wrote both files.

## Item 9 — hook wiring

Tracked half, per-machine half, and then the proof that it fires.

```
$ git ls-files -s .githooks/pre-commit
100755 a48e90352ac1c84807a2f0f8e5fe8459c1aaf301 0	.githooks/pre-commit

$ git config --get core.hooksPath       # before, then after
exit=1
.githooks
```

**Must-fire**, with the restore the item names — from a checksummed copy, never `git checkout --`:

```
$ printf '\nMethod details live in `manuscript/chapter-99-appendix.md`.\n' >> manuscript/chapter-01.md
$ git add manuscript/chapter-01.md && python .../candidate_path_check.py
guard exit=1
pre-commit BLOCKED: newly written text names a repository path that exists nowhere:
  manuscript/chapter-01.md: `manuscript/chapter-99-appendix.md`

$ cp <scratch>/ch01.bak manuscript/chapter-01.md && sha256sum manuscript/chapter-01.md <scratch>/ch01.bak
06d05e3c7512a47b94e3dc65dd2eebe058c4e6ec522518ef292700eb94ba71f0 *manuscript/chapter-01.md
06d05e3c7512a47b94e3dc65dd2eebe058c4e6ec522518ef292700eb94ba71f0 *<scratch>/ch01.bak
```

**Negative control** — the same guard, clean tree, and the commit carrying items 6–9:

```
$ git commit -m "caller: onboarding items 6-9 ..."
[master 3a53531] caller: onboarding items 6-9 (ledger, policy file, entry pointer, hook wiring)
 5 files changed, 155 insertions(+), 64 deletions(-)
exit=0
```

**Held — but only after two findings were worked around.** The first commit attempt of this item
crashed the guard outright (**F-2**); the second was falsely blocked (**F-1**).

## The freeze window, and the caller-declared record directory

Not one of the nine items, but the thing the nine exist to make possible — and the deliverable of
the previous round (`STRANGER-GUARDS`) exercised on a layout that is not the first caller's.

```
$ python .../dtw.py dispatch --range 519fb1b..HEAD
repo root discovered: D:\Project\Ongoing\stranger-proof-work\second-caller
freeze marker written: ...\.harness\review-pending.json
RESULT: derived (exit 0)

$ git commit -m "caller: edit during review window"       # an ordinary work product
exit=1
pre-commit BLOCKED: a review/read is out (E9: from dispatch to its record's
commit the branch takes no commit but the record itself).
  staged : manuscript/chapter-01.md  (not a review record)

$ git commit -m "caller: return the review record"        # docs/policy/reviews/v3-review-full-3a53531.md
[master 271910c] caller: return the review record
exit=0
```

**Held.** `dispatch` discovered the second caller's root correctly, and the declaration admitted
the record from a directory the shipped defaults do not name.

**Mutation, to prove the declaration is what did it** — `review_record_dirs` reverted to the
shipped default, same record, then restored from a checksummed copy:

```
review_record_dirs -> ['migration/document-work-assurance-v3/']
$ git commit ...      exit=1   pre-commit BLOCKED: ... (not a review record)
$ cp <scratch>/surfaces.bak .harness/scan-surfaces.json
a7fc6fa494cac473a4e92b07d6912954cff9ff739b6566d973c18eeb8c962bbf *.harness/scan-surfaces.json
a7fc6fa494cac473a4e92b07d6912954cff9ff739b6566d973c18eeb8c962bbf *<scratch>/surfaces.bak
$ git commit ...      exit=0
```

The declared directory is **necessary and not sufficient** — the filename must be a record family
too. That is correct behaviour, and it was isolated rather than left as an unexplained exit:

```
probe.md                     exit=1  not a review record
v3-review-full-abc1234.md    exit=0
```

**A malformed declaration refuses loudly**, both guards, each tested with a window open so that
neither short-circuited before reading it, and each restored by checksum afterwards:

```
$ printf '{ "record_surface": ["HARNESS-RIDERS.md",, ] }' > .harness/scan-surfaces.json
candidate_path_check exit=1  pre-commit BLOCKED: .harness/scan-surfaces.json is not readable
                             JSON: Expecting value: line 1 column 42 (char 41)
                             Fix the declaration as declared; this guard never falls back to
                             defaults silently.
review_freeze_check  exit=1  (same message)
$ cp <scratch>/surfaces.bak .harness/scan-surfaces.json
.harness/scan-surfaces.json: OK
```

## What a clone carries — the file's own table, on this layout

```
carried:      .githooks/pre-commit (mode 100755), HARNESS-RIDERS.md, docs/policy/decisions.md,
              .gitignore, the gitlink
not carried:  git config --get core.hooksPath  ->  exit=1
              .harness/                        ->  No such file or directory
              lib/vendor/assurance-harness/    ->  entries=0
```

**Held, every row.** The loud-versus-`-f` choice was seen rather than argued: with
`core.hooksPath` set and the submodule not yet initialised, the next commit failed —
`pre-commit: lib/vendor/assurance-harness/tooling/hooks/candidate_path_check.py is missing — the
mount is not initialised` — and succeeded after `git submodule update --init`.

Two further measurements taken here because they were cheap and could have gone the other way.
The cloned hook is CRLF (14 CRLF, 0 bare LF) and **still ran**: git's bundled `sh` on Windows
tolerates it, so the shebang worry is measured false on this platform and untested on POSIX. And
an **absent** declaration — which every fresh clone has, `.harness/` being ignored — falls back to
the shipped defaults silently, both guards exit 0. That is the documented behaviour and the right
one, but it means a caller's careful declaration is simply not in force in a fresh checkout until
`init` is re-run there; see **O-5**.

## Findings

### F-1 — the submodule-path fix does not hold inside a hook, which is the only place it runs

`candidate_path_check` falsely reports every submodule-internal path as resolving nowhere **when
git invokes it as a pre-commit hook**. Run by hand against the identical tree, the same paths
resolve. This is the defect rider `submod-index` was closed against one round ago, in
`STRANGER-GUARDS`.

Reproduced, then isolated to its mechanism with a paired control:

```
inside the hook   pre-commit BLOCKED: newly written text names a repository path that exists nowhere:
                    docs/policy/assurance-policy.md: `lib/vendor/.../candidate_path_check.py`
                    docs/policy/assurance-policy.md: `lib/vendor/.../review_freeze_check.py`
by hand           holds('lib/vendor/assurance-harness/tooling/hooks/candidate_path_check.py') = True
                  unlistable mounts: ()        total tracked entries: 380
```

Git exports `GIT_INDEX_FILE=.git/index` to every hook — a path relative to the *superproject*
root. `_submodule_files` runs `git -C <mount> ls-files` without clearing it, so git resolves
`.git/index` relative to the mount, where `.git` is a gitdir *file* and not a directory, reads a
nonexistent index, and returns **zero lines with exit 0**:

```
$ GIT_INDEX_FILE=.git/index python -c ...          # what the hook sees
git -C mount ls-files -> rc: 0 lines: 0
_submodule_files -> 0 entries
unlistable_mounts: ()
holds(candidate_path_check.py) = False

$ python -c ...                                    # negative control: same tree, variable absent
_submodule_files -> 369 entries
unlistable_mounts: ()
holds(candidate_path_check.py) = True
```

Exit 0 is what makes it silent. `_submodule_files` returns `None` only on a non-zero status, so an
empty listing is read as *this submodule tracks nothing*: the mount is never added to
`unlistable_mounts`, and the fail-open path built for exactly this case is bypassed.

Why it survived the round that fixed it: every verification of `submod-index` ran the guard
directly, which is the one context in which it works. Why it reaches past a second caller: the
first caller also runs both guards from a submodule mount through a pre-commit hook, and rider
`decited-paths` is banked waiting on `submod-index` precisely so that ten link texts can be
rewritten as real submodule paths — measured here, those rewrites would be falsely blocked.

**The fix is in `tooling/rsclib/document_harness/paths.py`, which this round's declared change
surface does not reach.** Not applied. Reported to the orchestrator for the user to route, and
banked as rider `submod-hookenv`.

### F-2 — no item installs the instrument's runtime dependencies

The word *install* appears nowhere in the nine items. The first command the procedure asks a
caller to run against the instrument — item 1's own *See* row — fails without them:

```
dtw.py --help    exit=1  ModuleNotFoundError: No module named 'jsonschema'
dtw.py init      exit=1  ModuleNotFoundError: No module named 'jsonschema'
dtw.py dispatch  exit=1  ModuleNotFoundError: No module named 'jsonschema'
```

and item 9 therefore ends with a hook that fails every commit, naming `jsonschema` rather than the
missing onboarding step. Installing them is the fix, and it was verified sufficient rather than
assumed to be:

```
$ python3 -m pip install --user "jsonschema>=4.18" referencing
Successfully installed ... jsonschema-4.26.0 ... referencing-0.37.0 ...

                        before      after
candidate_path_check    exit=1      exit=0
review_freeze_check     exit=1      exit=0
```

Why the instrument never noticed: its own `.githooks/pre-commit` runs `layer_path_check.py` and
nothing else, and that is the one guard with no third-party import — measured at exit 0 under both
interpreters throughout. **Fixed in this candidate**, as a prerequisite in ONBOARDING's *Read once
before starting* block.

### F-3 — the interpreter convention is false when both interpreters exist

ONBOARDING said that `python` in its commands and `.githooks/pre-commit`'s probe "resolve the same
choice". They do on a machine with one of the two, which is the only case the sentence considered.
On this machine both exist, and they diverge:

```
python3  ->  /c/Users/.../WindowsApps/python3   3.12.10   jsonschema: ModuleNotFoundError
python   ->  /c/Python313/python                3.13.6    jsonschema 4.25.1
```

The probe takes `python3` first, so the hook ran the interpreter without the dependencies while
every command in this walk, typed as `python`, ran the one with them. Silent until an import.
**Fixed in this candidate**, in the same paragraph.

### F-4 — item 3 offers a move without its cost, and the cost is a silent empty decision log

Item 3 says to move the log if the caller wants it elsewhere; item 3's *See* row says a second
`init` refuses to overwrite. Both taken as written:

```
$ git mv HARNESS-DECISIONS.md docs/policy/decisions.md    # and recorded the move in the file
$ python .../dtw.py init --repo-root .
created  : HARNESS-DECISIONS.md
$ find . -name "decisions.md" -o -name "HARNESS-DECISIONS.md" | grep -v assurance-harness
./docs/policy/decisions.md
./HARNESS-DECISIONS.md
```

Two logs, and the empty one sits at the path every convention names. A cold read discharging
`E10`'s `§live` obligation reads that one and finds no rulings at all; `init` reported `created`,
exit 0.

Tested as a class rather than an instance — the rider bank has the same shape, and one `init` run
recreates both:

```
created  : HARNESS-DECISIONS.md
created  : HARNESS-RIDERS.md
```

`init` has no placement option to fix it with — `--repo-root` is its only flag, and `HD-47` ruled
`--into` not worth adding on `E6` grounds, that no decision changes when it is absent. This walk is
a case where one does. That is not an argument for the flag: what was silent is the text offering
the move, so **the text is fixed in this candidate**, at items 3 and 4.

The class scan found a **second site outside this round's change surface**:
`document-harness/README.md` line 28 makes the same offer — "a caller wanting them elsewhere moves
them and records the move in its own decision log" — and is `E10` member two, which the plan
declares out of boundary. Not touched. Banked as rider `move-cost-member-site`, so the class is not
left half-swept.

## Observations — recorded, not acted on

- **O-1.** ONBOARDING item 1's *See* row says `--help` "lists the eight operations". Measured
  correct today: eight. The root README deliberately writes no such count, because two of them went
  stale there (riders `RA` and `readme-cli-stale`). Same class, one file behind.
- **O-2.** A `--range` dispatch names
  `migration/document-work-assurance-v3/v3-harness-review-contract.md` as the reviewer's standing
  instructions, and that file is a five-line retired stub redirecting to
  `CONSTRUCTION-CHECKLIST.md`. Deliberate, and pinned by tests; a second caller's reviewer takes
  one hop.
- **O-3.** The long-path caveat holds only above a 130-character root prefix (182 measured here
  against the 260 limit). Item 1 states it unconditionally.
- **O-4.** A policy file written before the first round cannot name the journal directory as a path
  token: item 5 keeps it uncreated, so the guard blocks it — correctly, and immediately, on the
  first work product a caller writes.
- **O-5.** A fresh clone has no `.harness/`, so a caller's edited declaration is silently absent and
  the shipped defaults are in force until `init` is re-run in that checkout. The clone table lists
  `.harness/` as per-checkout; it does not say "so re-run `init` there".
- **O-6.** The cloned hook is CRLF on Windows and runs anyway. Untested on POSIX.

## What this walk left behind

The caller repository is left in place at the path above as inspectable evidence, and is
disposable; nothing in this repository depends on it. Its decision log carries one live entry,
`D-1`, recording the wording this caller adopted to work around F-1 — which is `HD-34`'s prescribed
shape: the caller adapts in its own tree and records it, rather than editing a mounted instrument
in place.

One machine-level side effect, disclosed: `jsonschema` and `referencing` were installed into the
user-site of the Python 3.12 that `python3` resolves to on this machine, as F-2's fix. It is
reversible with `python3 -m pip uninstall jsonschema referencing`, and leaving it installed is the
state a caller following the corrected procedure would be in.
