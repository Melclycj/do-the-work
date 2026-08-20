# FULL review — round CALLER-ONBOARDING, `c22e229..2026a14`

**Verdict: `CHANGES_REQUIRED`.**

Two blockers, and both are guards that do not bind. The round's substance is otherwise sound
and I proved that rather than read it: `dtw init` copies verbatim, refuses per file, and never
adds a second ignore entry, and all three properties are must-fire under five neutered
mechanisms each paired against a clean baseline; the newly wired hook blocks a real broken path,
passes a clean control, and fails loudly when its script is missing; the battery is green at the
tip and the round's `712 → 733` delta reproduces exactly. The procedure document is accurate
where I could check it, and its three stated ceilings are real ceilings honestly stated.

The blockers are the two guards this round created, each of which has a hole precisely where its
own text says it does not:

- **`B-1`** the new tracked hook is committed `100644`, so it is skipped on any POSIX clone —
  the failure mode its own comment says it exists to avoid, and the exact mode error a FULL in
  this same directory called out as making the "it travels now" claim hollow;
- **`B-2`** the guard on the shipped decision-log template pins four of the five header rules
  `io-design.md` §6 requires, and its docstring names as the fifth one it does not pin.

Neither costs more than a line to fix. Both are the kind of defect that is invisible until the
day it matters, which is why they are blockers rather than lows.

Counts: **2 blocker · 3 low · 3 observation**.

---

## 1. Subject and dispatch, re-derived

Under `R2` I accepted nothing from the dispatch but the range, and re-derived the round, its
budget, its authorization and every figure below from the repository.

```
$ git rev-parse --show-toplevel
D:/Thesis-stage-control-refactor/ResearchSystem/harness

$ git status --porcelain
(no output)

$ git log --oneline c22e229776c8cb6f0b5ec0923f061ed3ccd086f2..2026a144f4dea83d4ac6c8235a647abe2cbd2590
2026a14 V3-CALLER-ONBOARDING-v1
393ebc5 V3-CALLER-ONBOARDING-FREE-L1-L2-v1
6b5c154 V3-REVIEW-RECORD-CALLER-ONBOARDING-c22e229-v1

$ cat .harness/review-pending.json
{
 "subject": "c22e229776c8cb6f0b5ec0923f061ed3ccd086f2..2026a144f4dea83d4ac6c8235a647abe2cbd2590",
 "dispatched_at": "2026-08-18T15:04:13+00:00"
}
```

The freeze marker names the same range I was handed, so the subject is corroborated inside the
repository and not only by the chat text. The tip is the branch head and the worktree is clean.

**Round and budget, derived.** The three commits are, oldest first: the record of the `E10`
opening read (a read — `E9`: spends nothing, `R3`: carries no verdict), a free-channel byte
application (`E10`: not a round, consumes nothing), and the round's first candidate. `E9`'s test
— *has a valid independent FULL already occurred?* — answers **no**, so nothing before this
record consumed the cap and **this is the round's one FULL**. The read's window held: its own
record states `git log --oneline c22e229..HEAD` was empty when it landed, and the ordering above
confirms no commit preceded `6b5c154` in the range.

**Change-set classification, by hand** (`R2`; 14 paths, `git diff --name-only` over the range):

| path | ∆ | what it is |
|---|---|---|
| `.githooks/pre-commit` | A | tracked hook — the round's new enforcement wiring |
| `README.md` | M | root navigator; not a layer member |
| `ResearchSystem/HARNESS-RIDERS.md` | M | rider bank; `layer-crossrepo-token`'s premise |
| `ResearchSystem/document-harness/ONBOARDING.md` | A | the procedure; declared **not** a member |
| `ResearchSystem/document-harness/README.md` | M | **instruction-layer member 2** |
| `…/journal/caller-onboarding-2026-08-19.md` | A | round journal |
| `…/templates/decision-log.md` | A | shipped instance template |
| `…/templates/rider-bank.md` | A | shipped instance template |
| `…/v3-cold-read-c22e229.md` | A | review record (the read's own commit) |
| `…/rsclib/document_harness/cli.py` | M | seventh subcommand |
| `…/rsclib/document_harness/init_target.py` | A | the command's body |
| `…/tests/document_harness/test_cli_entry.py` | M | surface literal six → seven |
| `…/tests/document_harness/test_init_command.py` | A | 21 tests |
| `…/tests/document_harness_review/test_fix_round_locks.py` | M | partition guard membership |

**`E2`.** No frozen byte was written:

```
$ git diff --name-only c22e229..2026a14 -- ResearchSystem/schema/document-assurance-v3 ResearchSystem/contract
(no output)
$ git ls-tree 2026a14 ResearchSystem/schema/document-assurance-v3/ | wc -l
15
```

**`E10`.** One member (`document-harness/README.md`) is written, twice — once by the free-channel
commit and once by the candidate. Both invoke the deferral clause and both record the two facts
it requires; I agree with the classification in each case. The *Local enforcement* row is
descriptive and self-labelled advisory, no clause is added to any rule, and nothing a rule
requires changes. `HD-38` is honoured: the free-channel bytes ride their own commit
(`393ebc5`: `1 file changed, 2 insertions(+), 2 deletions(-)`, and the two changed strings are
the two the read supplied). `E10-sync` is not triggered — the membership sentence,
`layer_path_check.LAYER` and `test_precommit_checks.EXPECTED` are all untouched, and the layer
is still ten.

**`E8`.** Titles, kinds and shape conform: each commit names the round, names its own kind
(*candidate* / *free-channel byte application* / *record*), carries one dense paragraph and no
trailers.

---

## 2. What binds, proved rather than read

### 2.1 The battery, and the round's own delta

```
$ python -m pytest -q            # from ResearchSystem/tooling, at 2026a14
733 passed in 94.15s (0:01:34)
```

The round claims a 712-passing baseline. Re-derived rather than accepted, in a throwaway clone
checked out at the base:

```
$ git checkout -q c22e229 && python -m pytest -q --collect-only | tail -1
712 tests collected in 0.97s
```

712 + the 21 tests of `test_init_command.py` = 733. The claim reproduces exactly, and it is
independently corroborated by `HD-45`'s own 2026-08-18 measurement (`712 passed / 92.87s`).
`HD-45`'s by-repository tiering is applied correctly: the change set touches tooling, so the
doc-only exception does not apply, and the one battery leg this repository holds is the one run.

### 2.2 `dtw init` — five mutations, each paired with a clean baseline (`E4`, `R8`)

Module copied to a scratchpad, sha256-checked, neutered one mechanism at a time, restored from
the scratch copy (never `git checkout --`), verified byte-identical before and after.

```
baseline sha256: 6eacddf057e3443c8379a2208c9cf470d89ef8bdb99d64637c37e43f4bd23b33
[CLEAN BASELINE (negative control)]            exit=0  21 passed
[M1 decode/encode round trip on the copy]      exit=1  1 failed   TheCopyIsVerbatim::test_each_copy_is_byte_identical_to_its_tracked_template
[M2 overwrite refusal removed]                 exit=1  3 failed   RefusesToOverwrite:: {a_second_run_creates_nothing, an_existing_instance_file_keeps_its_bytes, the_report_says_which_file_it_kept}
[M3 ignore entry not idempotent]               exit=1  2 failed   TheIgnoreEntry:: {a_second_run_adds_no_second_entry, the_slashless_spelling_counts_as_present}
[M4 destination silently renamed]              exit=1  10 failed  across FreshTarget / TheCopyIsVerbatim / RefusesToOverwrite / ThroughTheCommandLine
[M5 ignore match widened to a substring]       exit=1  1 failed   TheIgnoreEntry::test_a_lookalike_entry_does_not_count_as_present
final restore sha256: 6eacddf057e3443c8379a2208c9cf470d89ef8bdb99d64637c37e43f4bd23b33
[CLEAN BASELINE (after restore)]               exit=0  21 passed
```

Each mutation is a defect shape, not a crash: `M1` is the decode/encode normalisation the
docstring itself names as the near miss, `M4` is the silent rename `E5` exists for. The module's
two load-bearing properties bind, and the `E5` claim holds — the expectations are hand-written
literals and template files read from hand-written paths, which is why `M4` fails ten cases
instead of passing vacuously.

### 2.3 The newly wired hook fires, on this machine

Run in a throwaway clone with `core.hooksPath` set, at the tip:

```
A  broken path newly written into a layer member        exit=1
   | pre-commit BLOCKED: newly added instruction text names a repository path that does not resolve:
   |   ResearchSystem/document-harness/README.md: `ResearchSystem/nope/does-not-exist.md` — does not resolve from the repo root
B  a resolving path, same member (clean control)        exit=0   [main 17ec98f] probe
C  check script deleted (the loud branch)               exit=1
   | pre-commit: ResearchSystem/tooling/hooks/layer_path_check.py not found — the layer path check did NOT run.
C' script restored, same edit (control for C)           exit=0   [main 4148222] probe-C-control
```

The loud-versus-`-f` choice the file argues for is real and was seen. See `B-1` for the half of
this that does **not** hold off this machine.

### 2.4 The candidate's own layer edits pass the guard it wired

Replayed `layer_path_check.unresolved_tokens` over the added lines of each layer member in each
commit of the range:

```
c22e229 -> 393ebc5  document-harness/README.md  added_lines=2  unresolved=[]
393ebc5 -> 2026a14  document-harness/README.md  added_lines=1  unresolved=[]
```

`core.hooksPath` is in fact `.githooks` in this checkout, so the round's claim that the candidate
was checked by the hook it adds is consistent with the state I can observe.

### 2.5 The procedure's checkable claims

`--help` lists seven operations, as `ONBOARDING.md` :55 says. `init` locates its templates from
`__file__` (`parents[3]` → `ResearchSystem/`, correct) and both wired guards resolve their root
from `pathlib.Path.cwd()` (`layer_path_check` :106, `candidate_path_check` :131,
`review_freeze_check` :78), so item 1's mount-path-independence claim holds by construction and
not only by the `vendor/dtw` run. Every backtick path token in the new documents resolves from
this repository's root except two, and those two are correct (see `O-1`).

The membership question `E10`'s closing clause obliges is asked and answered, in the file itself
and in the journal, and the answer is right: the membership sentence is untouched, the file
claims authority over nothing and says the cited rule governs on disagreement, and its two
neighbours in the same directory sit on the same footing.

---

## 3. Blockers

### `B-1` — the tracked hook is committed non-executable, so it binds on Windows only

**Location.** `.githooks/pre-commit`, added by `2026a14`.

```
$ git ls-files -s .githooks/pre-commit
100644 521e707be370d7fbbdbca491344686be42917cf5 0   .githooks/pre-commit

$ git -C <caller> ls-tree HEAD -- .githooks/pre-commit
100755 blob e350b922e836136913c71bcc928e71b812669fd6   .githooks/pre-commit

$ git config --get core.fileMode
false
$ git version
git version 2.48.1.windows.1
```

**Ground truth.** Git runs a hook only if the file is executable; a tracked hook committed
`100644` is skipped on a POSIX checkout and the commit proceeds. That is not my inference — it is
written into a committed record in this same directory, `v3-review-full-eb6fbc2.md` :184, which
checked the caller's hook mode for exactly this reason: *"Mode `100755` matters and is right: a
tracked hook committed `100644` is skipped with a warning on any POSIX clone, which would have
made the whole 'it travels now' claim hollow."* One round later the instrument's own hook is
committed `100644`. `core.fileMode=false` here, and Windows git masks the executable bit out of
`access()`, which is why §2.3 saw it fire and why the round's execution could not have caught it.

**What changes if it stays.** The round's stated purpose for the file is that the layer check has
"run nowhere since the caller's duplicate copy was deleted on 2026-08-17". On every non-Windows
clone it still runs nowhere — silently, because a hook that is not executable is not a hook that
failed. `README.md` :64–68 now asserts the gap is closed and that "A clone carries the file";
`ONBOARDING.md` :24–36 teaches every future caller that the tracked half travels and only
`core.hooksPath` does not. Both are true only on this operating system, and neither says so. The
file's own comment argues at length for loud-over-silent failure while being, on POSIX, the
silent case.

**Minimum fix.** `git update-index --chmod=+x .githooks/pre-commit`, committed — index mode
`100755`, matching the caller's sibling artifact and the norm the `eb6fbc2` record already
established.

**`R4` ceiling.** I verified the mode, the asymmetry with the caller, and the Windows free pass
directly. The POSIX skip itself I did not execute — there is no POSIX checkout on this machine —
so it rests on git's documented behaviour and on the committed record cited above, which is a
stronger source than my reading but is still not a run.

### `B-2` — the template guard pins four of `io-design` §6's five header rules, and names the fifth as pinned

**Location.** `ResearchSystem/tooling/tests/document_harness/test_init_command.py` :43–53
(`DECISION_LOG_HEADER_LINES` and the comment above it). Second site, same defect:
`ResearchSystem/document-harness/ONBOARDING.md` :81, item 3's *See* row.

**Ground truth.** `io-design.md` §6 — signed, `HD-35` — requires the shipped decision log to be
「空条目 + 头部同步指令（状态机四态 / scope 四档 / 准入三问 / **继承** / 删除纪律）」: five things,
the fourth being **inheritance**. The comment claims exactly that scope — *"one per thing
io-design §6 requires the decision-log header to carry: the state machine, the four scopes, the
three admission questions, inheritance, and the deletion discipline"* — and the docstring
promises *"A template edited to drop any of the five fails here rather than reaching a caller
half-formed."* The tuple pins state machine, scopes, admission, **narrowing** and deletion.
Narrowing (`HD-30`) is not one of §6's five; inheritance is pinned nowhere. This is the only
guard on the template's content:

```
$ grep -rn "decision-log.md\|rider-bank.md\|DECISION_LOG_HEADER" ResearchSystem/tooling --include=*.py
  -> init_target.py:36,37 and test_init_command.py:39,40,47,122 only
```

Measured, by deleting one header block from the template at a time and running the suite:

```
[CLEAN BASELINE]                                        exit=0  21 passed
[DROP inheritance  ("> **Who reads it.** …", :11-13)]   exit=0  21 passed   <- the hole
[DROP state machine   (control)]                        exit=1  1 failed
[DROP four scopes     (control)]                        exit=1  1 failed
[DROP admission       (control)]                        exit=1  1 failed
[DROP deletion        (control)]                        exit=1  1 failed
[DROP narrowing       (pinned, not in §6's list)]       exit=1  1 failed
[CLEAN BASELINE after restore]                          exit=0  21 passed
```

Template restored byte-identical (`sha256 8e9d863c…d038d2` before and after).

**What changes if it stays.** The block that is unguarded is the one carrying *"Every cold read
MUST read `§live`, and only `§live`"* and the verbatim-inheritance rule — the two obligations
`E10`'s tail and `HD-5` rest on, and the reason a caller's decision log is worth shipping at all.
A later edit that hollows the template of exactly that block ships every subsequently onboarded
caller a decision log with no required-reading rule in it, and this suite stays green while its
own docstring says it is the thing that catches that. `ONBOARDING.md` item 3's *See* row repeats
the same wrong five, so the caller's manual check misses it too.

**Minimum fix.** Add the whole line to the tuple —

```
"> **Who reads it.** Every cold read MUST read `§live`, and only `§live`. A plan author reads",
```

— and correct the two prose enumerations (the comment at :43–46 and `ONBOARDING.md` :81) so both
name §6's five, with narrowing declared as the extra it is. No new machinery (`E6`): the mechanism
exists and the fix is one more literal in a list it already holds.

---

## 4. Lows

### `L-1` — the round created a stale "six operations" class and swept two of its four live sites

`test_cli_entry.py` :4 and :10 were correctly rewritten (*then-six*, *exactly seven*). Two
sibling sites, both in files this round edited, were not:

- `rsclib/document_harness/cli.py` :13 — *"while these six travel with the instrument"*, ten
  lines below the paragraph the round rewrote to say **Seven operations**; the antecedent
  *"They"* at :12 is that paragraph's enumeration, and `init` travels with the instrument too.
- `tests/document_harness_review/test_fix_round_locks.py` :328 — *"`TheTwoNames` in
  `tests/document_harness/test_cli_entry.py` (the six operations and the two entry names, both
  mutation-tested)"*, twelve lines above the `SUCCESSOR_ROUND_MODULES` line the round changed.
  That sentence is the stated justification for `cli.py` being exempt from the code sweep, so it
  is the sentence a later auditor of that exemption reads.

`E7` and `HD-41` ④ bind the executor to the class, not the instance; the class here is the one
this round's own change created, and no sweep for it appears in the commit body. Three further
sites in the root README are disclosed and routed (`O-3`).

**Bytes.** `cli.py` :13 `while these six travel with the instrument` → `while these travel with
the instrument`; `test_fix_round_locks.py` :328 `(the six operations and` → `(the operation
surface and`.

### `L-2` — the class-sweep figure does not reproduce from the command it is attributed to

The candidate body names the sweep grep and asserts *"returns four sites in this repository, all
four now corrected, and three in the caller"*. Re-run, whole-repository scope, same pattern and
same exclusions:

```
$ git grep -n -I -E -i "<the pattern>" -- . ':!ResearchSystem/migration' ':!…/journal'
  at c22e229 : 3 files, 3 lines
  at 393ebc5 : 3 files, 3 lines
  at 2026a14 : 5 files, 6 lines   (.githooks/pre-commit, README.md ×2, HARNESS-RIDERS.md,
                                   ONBOARDING.md, document-harness/README.md)
  in the caller (excluding the submodule) : 8 files, 10 lines
```

Four is not what that command returns at any revision in the round. `HD-41` ④ requires the grep
**output** in the commit body precisely so a reviewer can see whether it ran; `E3` requires a
count to come from the command that produces it or be dropped. Neither happened, and the caller
half is worse than loose: the caller's most load-bearing stale site,
`ResearchSystem/HARNESS-POLICY.md` :62 (「而那个仓今天还没装任何 hook」), is Chinese and matched by
none of the pattern's nine alternatives — the journal found it by reading, not by the grep the
commit credits.

Filed low, not blocker, because the **substance** is sound: I read all six surviving sites at the
tip and each is now accurate. What failed is the evidence discipline, which is the half `HD-41`
deliberately left as discipline with a reviewer as its only enforcement.

**Bytes.** None supplied — the fix is to paste the run's actual output, which only the executor
has.

### `L-3` — the ruling that authorises the round's central artifact lives only in this round's own commit bodies

`cli.py` :8–10, the candidate body and `journal/caller-onboarding-2026-08-19.md` §2 all state
that *"the user ruled on 2026-08-18 that a seventh command may exist"*. `HARNESS-DECISIONS.md`
carries no such entry — `§live`'s newest is `HD-44`, on a different subject — while
`split-design.md` §1 (:44, signed, `HD-40`) still reads 「六命令原样」 and rider `RA` still records the
2026-08-17 ruling that a seventh was 「便利性而非正确性」 and 「不为此推翻 §1」, neither annotated.
The decision log's own admission test admits this on two of three grounds (it binds the next
round and beyond; it narrows an existing ruling), and the precedent set one round earlier is that
such an entry lands with its carrier: `HD-46` was written in that round's **candidate** commit
`d8cc6d1`, not at its closeout.

`R2` makes chat-only load-bearing material a finding, so it is filed. `R7` caps it below blocker:
an authorization I cannot see is a hint, never a block. **Ceiling stated:** I cannot confirm or
deny the 2026-08-18 ruling; the round's disclosure is explicit and consistent across three
places, and the deferral to closeout is declared rather than hidden. Whether the entry may wait
is the user's, not mine.

---

## 5. Observations

### `O-1` — `ONBOARDING.md` adds two more tokens of rider `layer-crossrepo-token`'s class, saved only by not being a member

Running the wired guard's own resolver over the new documents:

```
ONBOARDING.md            [('ResearchSystem/HARNESS-POLICY.md', 'does not resolve from the repo root') ×2]
journal/…08-19.md        []
templates/*.md           []
.githooks/pre-commit     []
document-harness/README.md []
```

Both tokens are **correct as written** — they name the caller's policy file, and the surrounding
prose says so. They are inert today only because `ONBOARDING.md` is not one of the ten. The
journal §1 explicitly contemplates a later round naming it: on the day that happens, the guard
this round wired blocks it on its own procedure document. That is the same shape the rider
records for `EXECUTION.md`, in a file created after the rider's deadline was declared arrived.
Reported, not routed (`R5`).

### `O-2` — the read's `O-2` was routed to ride this round's scan, and did not

The record commit `6b5c154` routed it: *"O-2 names its content … and is a sibling site of the
class this round's instruction already obliges the executor to scan, so it rides that scan."* The
candidate instead lists it under *"Left open and routed to the user at closeout, not decided
here"*. Still stale, measured at the tip:

```
$ python -c "[p for p in layer_path_check.LAYER if candidate_path_check.scanned(p)]"
7      # candidate_path_check.py:15 says "the six Markdown instruction-layer members"
```

The divergence is disclosed, not silent, and is defensible on the merits — the class the executor
swept was hook wiring, and no grep for that class would ever have reached a membership count. It
is recorded because two commits in the same range give the same finding two different owners, and
the closeout should pick one.

### `O-3` — the three stale root-README CLI claims the candidate discloses are exactly three, and all three are false

Confirming the disclosure rather than adding to it. `README.md` :59 *"**The CLI is not here.**"*
— `ResearchSystem/tooling/dtw.py` is here, and the table row at :54 in the same file says so;
:59–60 *"extracting the six v3 commands into `do-the-work` (alias `dtw`) is R2's work"* — R2 is
done; :61–63 *"the CLI extraction alone will not make the suite green"* — `python -m pytest -q`
returns 733 passed. The count is right, the attribution to the split batch's R2 is right, and the
round's choice to route rather than fix keeps it inside `E8`'s change boundary. The section's own
opening sentence — *"run these, do not trust a sentence"* — is the reason these matter more than
their size suggests.

---

## 6. Coverage, and what this review did not establish

**Read in full:** `CONSTRUCTION-CHECKLIST.md` (both sides) and the review-contract stub it
supersedes; `HARNESS-DECISIONS.md` header and `§live`; every file the range adds or changes,
including all 14 diffs end to end; `hooks/layer_path_check.py`; `templates/decision-log.md` and
`templates/rider-bank.md`; `v3-cold-read-c22e229.md`; the round journal; `ONBOARDING.md`;
`io-design.md` §6–§7; rider rows `RA` and `layer-crossrepo-token`.

**Read in part:** `HARNESS-DECISIONS.md` `§implemented` (`HD-33`/`HD-34`/`HD-38`/`HD-40`/`HD-45`/
`HD-46` by grep); `split-design.md` §0–§2; `hooks/candidate_path_check.py` and
`review_freeze_check.py` (root resolution and exemption lists only); `v3-review-full-eb6fbc2.md`
(the hook-mode and wiring sections); the caller's `HARNESS-POLICY.md` (grep only — it is not my
subject, and I opened it solely to test a count the subject asserts).

**Executed:** the full battery at the tip; `--collect-only` at the base in a throwaway clone;
five module mutations and six template mutations, each restored from a sha256-checked scratch
copy; four hook probes in a throwaway clone; the layer resolver replayed over the range's added
lines and over every new document. The clone and all scratch copies are outside both
repositories and have been deleted.

**Not established.**

- **The POSIX half of `B-1`.** I have the mode, the asymmetry and the Windows free pass by
  measurement; the skip itself is git's documented behaviour and a committed record's finding,
  not a run I performed.
- **That the nine items are nine.** `R5` keeps me out of it, and the round says the same: one
  author, one sitting, one machine, one throwaway caller. Whether a tenth item is missing is not
  answerable from inside this repository, and the round's ceiling on that point is honest.
- **Whether `dtw init` should write both instance files at the target root.** The round routes
  this to the user and I leave it there: the instrument keeps its own two under
  `ResearchSystem/`, `init` writes a caller's at the root, and no rule pins either.
- **`R4` process claims.** The `E1` disclosure — that the executor was a subagent holding none of
  `R1`'s four holdings — is **marked, not verified**. I cannot see who set this question from
  inside the repository; my own independence is structural only if the orchestrator, not the
  executor, dispatched and scoped me (`R7`: ceiling stated, moving on).
- **That the round is defect-free.** Two blockers, three lows and three observations are what
  this pass surfaced across 1 279 added lines and their machinery. Mutation proved the guards I
  mutated have binding force where they fired and a hole where they did not; it did not prove
  that force is sufficient anywhere.
