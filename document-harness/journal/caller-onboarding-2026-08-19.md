# Caller onboarding — the nine items, written down and then executed (2026-08-19)

Round `CALLER-ONBOARDING`, the third of the three the user ordered on 2026-08-17. Periods one
(`SPLIT-COPY-RETIRE`) and two (`ORCHESTRATOR-CHARTER`) closed on 2026-08-18. This round's
subject is the gap the ledger's backlog names: the nine preparation items implied by `HD-33` /
`HD-34` and `io-design.md` §5–§7 existed only as a derivation, in no file, and had never been
executed by anything.

## 1. The membership question, and its answer

`E10`'s closing clause: *"a file that appears later and claims authority over any rule here is
not a member until the membership sentence names it, and the round that creates one records the
question and its answer"*. This round creates `ONBOARDING.md`, so the question is owed.

**Question.** Is `ResearchSystem/document-harness/ONBOARDING.md` an instruction-layer member?

**Answer.** No.

**Ground**, three parts, each checkable:

1. **The membership sentence does not name it.** `E10` enumerates "exactly these ten paths and
   nothing else". This round does not touch that sentence, so the layer is the same ten it was
   at `393ebc5`, and `E10-sync`'s three-site check-item is not triggered — no change to the
   membership sentence, `layer_path_check.LAYER`, or `test_precommit_checks.EXPECTED`.
2. **The file claims authority over no rule.** Every obligation it states is stated as
   belonging to a rule elsewhere and cited by pointer: its Owner column names `HD-33`, `HD-34`,
   `io-design.md` §5–§7, `R10`, `E4`, `E9`, `ORCHESTRATION.md`'s policy-file section, and
   `README.md`'s *Local enforcement* row. It adds no clause and narrows none. Where it and a
   cited rule disagree, the rule governs — written into the file itself, so the reading is not
   left to inference.
3. **It is a procedure, not a rule.** It answers "what do I do first, and how do I know it
   took", which is the shape of `split-travel-manifest.md` and `io-design.md` — both of which
   live in this same directory and are not members either. Proximity is not membership; the
   sentence is.

What would change the answer: if a later round wanted onboarding to be *obligatory* in some
sense a rule could check, that obligation would have to be added to a rule and this file named
by the membership sentence — which is design, and opens a round under `E10`.

## 2. `dtw init` as a seventh command

`split-design.md` §1 records the six commands travelling "as they were", and rider `RA` records
that a seventh was once declined as convenience rather than correctness. The user ruled on
2026-08-18 that a seventh may exist. The two are not in conflict and this journal does not
harmonise them — the decision-log entry is the orchestrator's to write, and the FULL of
`2026a14` (`L-3`) found that deferring it left the ruling authorising this round's central
artifact living only in commit bodies, against the precedent of `HD-46`, which landed in its
own round's candidate commit. It is written with the repair that answers `L-3`, not at
closeout; `split-design.md` §1 and rider `RA` still read as they did, which is that entry's
subject and not this journal's. What is worth
recording here is the shape the ruling was implemented in, because it is what keeps `RA`'s
objection answered rather than overruled:

`init` does **only** the four mechanical items — `.harness/`, its ignore entry, and the two
template copies. The other five are judgment (which revision to pin, what the policy file says,
where the pointer goes, which guards the hook runs, when the first journal is written), and the
command does not attempt them. It says so in its own output, every run, naming all five: a
caller who runs only the command cannot mistake it for the whole of onboarding. It also issues
no verdict — there is deliberately no `onboarded` flag for a later round to trust.

## 3. The R8 run — the procedure executed against a throwaway caller

Written first, then run end to end, then corrected to match the run. Everything below happened
in `…/scratchpad/onboarding/`, outside both repositories.

| item | what was run | result |
|---|---|---|
| 1 mount | `git submodule add ../instrument-pub vendor/dtw` | `git submodule status` → `bd5fbc99… vendor/dtw (heads/main)`; `vendor/dtw/ResearchSystem/tooling/dtw.py` present |
| 2 `.harness/` + ignore | `python vendor/dtw/ResearchSystem/tooling/dtw.py init --repo-root .` | 4 created; `git check-ignore -v .harness/x` → `.gitignore:1:.harness/` |
| 3 decision log | same command | `diff` against the mounted template: identical |
| 4 rider bank | same command | `diff` against the mounted template: identical |
| 5 journal | nothing, by design | nothing to see, which is the item |
| 6 ledger | hand-written `LEDGER.md`, parameters declared in the policy file | both exist |
| 7 policy file | hand-written `HARNESS-POLICY.md` | four sections: where conclusions come from, what is written after, mechanical checks, anchor assertions |
| 8 pointer line | one line in `CLAUDE.md` | grep finds the policy file from the entry file alone |
| 9 hook | tracked `.githooks/pre-commit` calling two guards from the mount, plus `git config core.hooksPath .githooks` | both guards demonstrated firing, each against a clean control |

**Re-run against a live caller.** A line was appended to the decision log and `init` run again:
it kept all three existing paths, named each in its report, and the appended line survived. That
is the property that matters on a second run — a caller's rulings are the last thing a
convenience command may clobber.

**Mount-path independence, tested rather than assumed.** The mount is `vendor/dtw`, not
`ResearchSystem/harness`, precisely because the procedure claims any path works. It does:
`init` locates its templates from `__file__`, and the two guards resolve the repository root
from the process cwd git gives a hook.

**What a clone carries — measured, not argued.** The onboarded caller was cloned. The clone
carried `.githooks/pre-commit`, all four instance files, the policy file, the pointer line and
the `.gitignore` entry; it did **not** carry `core.hooksPath` (`git config --get` → exit 1),
`.harness/`, or the submodule's contents (`vendor/dtw` empty). Then `core.hooksPath` was set
*without* initialising the submodule, and a commit was attempted: the hook refused loudly —
`the guard did NOT run (submodule not initialised?)` — which is the design choice item 9
records, and the opposite of what an `-f`-guarded silent skip does.

## 4. Ceilings — steps that could not be executed as written, and what was substituted

Stated rather than skipped, per the round instruction's own `R7`-style rule.

- **The real remote could not be used.** The instrument's URL is a private GitHub repository
  (`.gitmodules` in the caller names it) and this run had neither network nor credentials.
  Substituted: a local clone of the instrument as the submodule source. Two consequences, both
  real: `git submodule add` needed `-c protocol.file.allow=always` (git refuses `file://`
  submodule sources by default since the 2022 advisory) — a substitution artefact, not a step a
  network caller performs; and the clone was taken at `393ebc5` and then given this round's
  **uncommitted** work as one scratch commit, because otherwise the mounted instrument would
  not have carried the `init` command being tested. So the run exercised these bytes; it did not
  exercise a published revision.
- **Windows path length.** Cloning the instrument into the scratchpad failed with
  `Filename too long` on three N0 fixture paths until `-c core.longpaths=true` was passed. It is
  environmental (this tree is deep and the scratchpad path is long), but a Windows caller
  mounting under a deep path will meet it, so item 1 now carries the note.
- **The caller side of this round is not here.** `HARNESS-POLICY.md` §3 in the caller and the
  `.githooks/pre-commit` comment there both still say the layer check is homeless and that this
  repository installs no hook. Those bytes are the caller's; this round leaves them alone and
  reports them.

## 5. What the round did not establish

- **That nine is the right number.** The nine are what `HD-33` / `HD-34` and `io-design.md`
  §5–§7 imply, as the ledger's backlog derived them; this round wrote them down and ran them,
  which tests that they are *executable and sufficient for this run*, not that a tenth is not
  missing. A real second caller is what would establish that.
- **That the procedure is followable by someone who did not write it.** It was executed by its
  own author, in one sitting, on the machine that grew the harness. The ceiling is inherent and
  cannot be closed from inside this round.
- **Anything about the guard's behaviour on a re-homed instruction layer beyond the two classes
  it flags.** Rider `layer-crossrepo-token` predicted, before this round, that wiring
  `layer_path_check` here would eventually block a correct commit: `EXECUTION.md`'s
  by-repository battery enumeration legitimately names four caller-side paths that do not
  resolve here, and the guard's only reason for not firing on them today is that it scans added
  lines and those lines are not new. That rider's deadline — "the moment the guard is wired into
  this repository" — arrives with this round, its fix is design, and this round therefore does
  not touch it. It is reported to the orchestrator as the user's to route.
