# FULL review — round `RIDER-SETTLEMENT` at `8aa9f6e`

**Verdict: `CHANGES_REQUIRED`.** 2 blockers, 3 low, 4 observations.

**The one real defect the round set out to fix is fixed, and I could not break it.**
`discover_repo_root` now clears git's own repository-scoping variables before asking, and the
paired test binds: with `env=env` deleted from the query the new test fails on this machine,
and it fails on the *right* assertion — its negative control (`uncleared == elsewhere`) passes
first, proving `GIT_WORK_TREE` really does redirect an uncleared query here rather than the
test passing for want of a live defect. The helper extraction into `paths.py` is
behaviour-preserving: the `None` sentinel still means *git could not name the variables*, and an
empty-but-not-None environment is still distinguished from it, so `_submodule_files`'
fail-open is unchanged. The executor-charter mount pin fires only on its own new test, which
is the measurement that proves the rider was naming a real hole rather than a redundant one.
Battery 854 green at the tip, against 851 at the base — both re-derived here.

**The two blockers are both about a claim that outruns what was measured.** `B-1` is the
`retire-suite` redemption: the rider's row is deleted, but the class it named still
reproduces — a different and equally plausible wrong implementation of the same kept-count
leaves all twelve tests green, because the new `RAW_IDS` was chosen equal to `PRESENT_IDS`.
The same choice removed the one fixture case that instantiated the property the fixture's own
rewritten docstring still asserts. `B-2` is the round's `HD-41` class scans: both absolute
claims are falsified inside their own declared scope, and neither pasted the scan output that
rule's clause ④ requires — which is why they were not caught before the commit landed. Each
blocker has an exact minimum fix, and I measured `B-1`'s.

---

## 1. Subject, round, budget and authorization — re-derived, nothing taken from the dispatch

The dispatch handed one range and the standing-instruction pointer. Everything below is from
the repository.

**Subject.**
`2522ce1f8e1733227bafe66d11dc1d4f57045460..8aa9f6efd78fed1a0276e0c17aa73e1b10398788`, three
commits. `8aa9f6e` is `HEAD` (`git rev-parse HEAD`). The worktree was clean at the start of
this review, after every mutation restore, and at its end (`git status --porcelain` → empty
each time; each restore was from a sha256-checked scratch copy, never `git checkout --`).

| commit | title | kind (named in its own body) |
|---|---|---|
| `d41484c` | `V3-RIDER-SETTLEMENT-PLAN-v1` | orchestrator bookkeeping plus the round's plan |
| `fd525e4` | `V3-RIDER-SETTLEMENT-v1` | candidate (work product) |
| `8aa9f6e` | `V3-RIDERS-RETIRE-FOUR-v1` | riders-only bookkeeping |

**Round.** `RIDER-SETTLEMENT`. Its plan is `document-harness/plans/rider-settlement.plan.md`,
landed inside this range at `d41484c`, status open.
`CONSTRUCTION-LEDGER.md`'s queue paragraph, amended in the same commit, now names the rider
bank settlement batch as the queue head.

**Budget.** `E9`: one FULL, at most one user-approved fix, one targeted VERIFY. No valid
independent FULL had occurred on this candidate before this record, so this is the FULL; the
verdict below obliges the fix leg and its targeted VERIFY if the user approves one. The
riders-only commit `8aa9f6e` consumes nothing under the 2026-08-04 ruling (`HD-23` records
its criterion and its extension) — its precondition, that the correction fall inside the next
review's subject range, is met: it is the tip of this range.

**Authorization.** Three opening rulings, dated 2026-08-25, carried by the plan's *Opening
rulings* section, which names itself their carrier; `d41484c`'s body states they were given in
conversation that day. They are visible in the repository, so `R7`'s ceiling does not bite. No
decision-log entry was opened for them; ruling 1 and ruling 2 are one-shot and consumed here,
and ruling 3 is scheduling — see `O-3` for the one part of that which has no carrier outside
this round's own plan.

**Review window (`E9`).** `.harness/review-pending.json` names exactly this range,
`dispatched_at` `2026-08-25T03:01:51+00:00`. `git reflog` shows `8aa9f6e` as the newest commit
on the branch, so the branch has taken nothing since dispatch. `E12`'s written-tip prohibition
is about a range recorded *in a commit inside the round*; the freeze marker is a runtime file
written after the round's commits and is not that.

**`E2`.** Nothing frozen was touched. The changed-path list below contains neither
`contract/Document-Work-Assurance-Contract-v4.md` nor any file under
`schema/document-assurance-v3/`.

**Layer state going in.** Verified rather than accepted: `git log 21dad76..8aa9f6e` over the
nine `E10` member paths returns exactly two commits — `153302a` and this round's `fd525e4`.
`v3-cold-read-21dad76.md` records all nine blob ids; comparing them to
`git rev-parse HEAD:<member>` today, six are byte-identical, and the three that changed are
`document-harness/ORCHESTRATION.md` (`153302a`, whose paired re-read
`v3-checkpoint-read-153302a.md` exists, committed as
`V3-REVIEW-RECORD-STRANGER-PROOF-153302a-v1`) and this round's two,
`document-harness/EXECUTION.md` and `document-harness/README.md`. The plan's ruling 1 is
therefore accurate about what it waived and what it left owed, and its disclosed cost — those
two member edits owe an independent read at the next round's opening — is the right debt.
Neither edit is *design* under `E10` (neither adds a clause to any rule nor changes what any
rule requires), and this round opened properly in any case, so the `E10` route is clean. No
round relies on either text yet.

**Changed paths, classified by hand** (`git show --name-only` per commit):

| path | commit | class |
|---|---|---|
| `document-harness/plans/rider-settlement.plan.md` | `d41484c` | plan (new) |
| `CONSTRUCTION-LEDGER.md` | `d41484c` | record |
| `HARNESS-RIDERS.md` | `fd525e4`, `8aa9f6e` | rider bank |
| `document-harness/EXECUTION.md` | `fd525e4` | `E10` member |
| `document-harness/README.md` | `fd525e4` | `E10` member |
| `document-harness/ONBOARDING.md` | `fd525e4` | instruction-adjacent, not a member |
| `assurance/templates/run-v2/README.md` | `fd525e4` | template doc |
| `assurance/templates/run-v2/run_bind_v2.py` | `fd525e4` | template code |
| `tooling/rsclib/document_harness/caller.py` | `fd525e4` | resident code |
| `tooling/rsclib/document_harness/paths.py` | `fd525e4` | resident code — **not on the plan's change surface**, see `L-1` |
| `tooling/tests/document_harness/test_repo_root_discovery.py` | `fd525e4` | test |
| `tooling/tests/document_harness_review/test_dispatch.py` | `fd525e4` | test |
| `tooling/tests/document_harness_review/test_run_v2_template_retire.py` | `fd525e4` | test |

**Bank arithmetic, re-derived** (row ids extracted from each revision of `HARNESS-RIDERS.md`
and diffed with `comm`): 30 rows at `2522ce1`, 20 after `fd525e4`, 16 at `8aa9f6e`. The ten
`fd525e4` deletes are exactly the ten the plan's change-surface table names; the four
`8aa9f6e` deletes are exactly `ctx-ground`, `status-key`, `self-caller-guards` and `F-c`. No
row was added. Every one of the ten was deleted in the same commit as its fix (`R10`), and the
four retirements carry no fix and claim none.

---

## 2. Blockers

### `B-1` — the `retire-suite` rider is deleted, but the class it named still reproduces

**Location.** `tooling/tests/document_harness_review/test_run_v2_template_retire.py:87`
(`RAW_IDS = ("chk-a", "chk-b")`), with `:104-118` (the fixture) and `:186`, `:196`, `:204`
(the assertions that read it).

**Ground truth.** `E7` — test the defect class, not the reported instance. `E4` — never trust
a guard you have not seen fail. The rider `retire-suite` recorded, of the *pre-fix* fixture,
that deleting the template's `.is_file()` predicate left all twelve tests green; the plan's
*Expectations* section holds this round to "deleting `.is_file()` from the retire count now
turns a test red (it did not before)".

**What I measured.** Three runs against
`assurance/templates/run-v2/run_retire.py:152-155` (the `out_files` derivation), each with the
file restored from a sha256-checked copy afterwards:

```
pre-fix fixture (2522ce1) + predicate deleted   : 12 passed        <- reproduces the rider
shipped fixture + predicate deleted             : 1 failed
shipped fixture + out_files = list(to_delete)   : 12 passed        <- the class survives
```

The first two confirm the executor's own claim; the third is the finding. Replacing the whole
filesystem derivation with the deletion set — `out_files = list(to_delete)`, a wrong
implementation at least as plausible as counting `check_order`, since `to_delete` is the list
sitting three lines above — prints `+ 2 raw output(s)`, which is what the test expects, and
the suite stays green. The guard binds against one alternative, not against asking the
filesystem.

The cause is the value chosen: `RAW_IDS == PRESENT_IDS == ("chk-a", "chk-b")`. The fixture
docstring's stated invariant is only that `raw_ids` be "a proper subset of `check_order`",
which is satisfied; what it needed to be is distinct from *both* other id sets.

**Second half, from the same choice.** The rewritten docstring at `:109-111` says a check in
`raw_ids` gets a raw output "whether or not its per-result JSON is present — the two survive
or vanish independently in this harness, exactly as HD-12 describes". With
`raw_ids == present_ids` no fixture case instantiates that any more: every ordered id now has
its JSON and its raw output agreeing. The case that did instantiate it was `chk-c` — JSON
already gone, raw output present — and removing `chk-c`'s raw output is precisely the edit
this round made. The claim outlived the case it rested on.

**Minimum fix, measured.** `RAW_IDS = ("chk-c",)`, with the expected line at `:204` becoming
`+ 1 raw output(s)`. One element, and the one whose per-result JSON is already gone, so the
count (1) differs from `len(check_order)` (3) and from `len(to_delete)` (2), and the
JSON-gone/raw-present case comes back. Measured on a scratch edit:

```
proposed fixture + real template                 : 12 passed
proposed fixture + out_files = list(check_order) : 1 failed
proposed fixture + out_files = list(to_delete)   : 1 failed
```

I am reporting the defect and one fix that works; which fix to take is the executor's (`E12` —
reproduce to write the fix correctly, not to adjudicate the reviewer).

### `B-2` — both `HD-41` class scans are falsified inside their own declared scope, and neither pasted its output

**Location.** `fd525e4`'s commit body, the paragraph beginning "HD-41 class scans, with their
ranges."

**Ground truth.** `HD-41` (§live, standing, and the decision log outranks the instruction
layer on conflict): ① an assertion declares its scope first and then runs a command covering
that scope; ② absolute quantifiers carry their scope; ④ fixing a finding means grepping the
class first and **pasting the grep output into the commit body**, because the scan is an
action rather than a good intention and the evidence is what lets a reviewer see on the spot
whether it ran. `E3` says the same from the other side: paste tool output, never describe it
from memory.

The body declares its scope — tracked `*.md`, excluding `migration/`, the archives, `journal/`
and `plans/` — and then describes the result in prose instead of pasting it. Re-running that
exact scope (`git ls-files '*.md'` minus those four patterns, 19 files) falsifies both
sentences:

**Class 1, bare reader-facing `python`.** The body: "every remaining occurrence sits under a
convention sentence — README.md:100 and :205, ONBOARDING.md:27, and the two added here."

- `document-harness/history/REVIEW-v1-package-flow.md:59` carries a reader-facing
  `python -c "…"` command. That file contains no convention sentence — `grep -c python3` on it
  returns 0 — and it is inside the declared scope, which excludes `migration/`, the archives,
  `journal/` and `plans/`, but not `document-harness/history/`.
- `HARNESS-DECISIONS.md:357` carries a bare `python -m pytest -q`, likewise with no convention
  sentence in that file. This one reads as quotation inside a ruling, which is the rationale
  the body gives for its exclusions — but it is not an excluded path.
- The enumeration of *covering* sentences is also short: `README.zh-CN.md:96` and `:192` are
  two more, and that file's four occurrences sit under them.

**Class 2, hard-coded command counts.** The body: "only README.md:245 (the five commands in
the Quickstart) survives, and it is a different class."

- `README.md:95` — "Five commands stand between a repository that has never seen this harness
  and one where the guard actually fires" — is the same sentence family in the same file.
- `README.zh-CN.md:92` and `:229` mirror both of them.

So four sites of that class survive in the declared scope, not one. The `--help`-derived count
the rider `onboard-cmd-count` actually named *is* closed — I checked, and over the same scope
no line pairs a number with what `--help` lists — which is the part of the claim that holds.

**Why this is a blocker rather than a wording note.** It names a downstream decision that goes
wrong (`R9`'s test): a later round redeeming a sibling of `py-convention`, or touching the
Quickstart's step count, reads this body as "class closed" and skips the sites it does not
list — and one of those sites, the bilingual mirror, is new enough that no earlier scan
covered it. Had clause ④'s paste been made, the divergence would have been visible in the
commit itself.

**Minimum fix.** Paste both greps' actual output; and either declare
`document-harness/history/` excluded, giving the reason, or give that file the same
one-sentence convention the other four sites got — then correct both enumerations to what the
scan returns.

---

## 3. Low

### `L-1` — `paths.py` is changed by the candidate and is not on the plan's declared change surface

`tooling/rsclib/document_harness/paths.py:139-151` (`env_without_repo_scope`, extracted) and
`:175-180` (`_submodule_files` rewired to it). The plan's *Change surface* table lists ten
paths; this is an eleventh. Its row for `discover-root-env` names only
`tooling/rsclib/document_harness/caller.py:166` and describes the fix as copying the shape
that round `SUBMOD-HOOKENV` used in `paths.py` — copying the shape, not editing the file.

`E8` says stay inside the round's declared change boundary; `E9` says exceeding an approved
boundary requires saying so, never silently. The body does describe the change plainly ("the
two lines paths.py used to build the cleared environment are now the named function
env_without_repo_scope(), so the second site reuses it instead of copying it; paths.py's
behaviour is unchanged"), so it is not silent — what is missing is naming it as outside the
declared surface.

The engineering is right, and I verified the invariant rather than taking it: extraction
preserves the `None`-means-git-cannot-answer sentinel, an empty-but-not-`None` environment is
still distinguished from it, so `_submodule_files`' fail-open to `OUT_OF_INDEX` is unchanged,
and there is no import cycle (`paths.py` imports nothing from `caller.py`). Extracting rather
than copying is also the direction `decl-dup`, redeemed in this same commit, exists to push.
The minimum fix is a sentence, not a revert.

### `L-2` — `document-harness/README.md:28` states the move cost for one instance file where the measurement covers two

The sentence's subject is both: "The two instance files land at the target root … a caller
wanting them elsewhere moves **them** … — at a measured cost: a later `init` finds nothing at
the default path and silently creates an empty **decision log** there".

Measured on a scratch caller (`git init`, `dtw init`, move both files into a subdirectory,
`dtw init` again): `RESULT: 2 created, 2 left as found (exit 0)` — **both**
`HARNESS-DECISIONS.md` and `HARNESS-RIDERS.md` were recreated at the root. `ONBOARDING.md`
item 4 already says so ("Moving it carries item 3's cost unchanged — measured on the same
walk, both files recreated at the root by one `init` run"), so the member is narrower than the
file it points at. The sharp consequence the sentence names — a cold read discharging `E10`'s
§live obligation reading the empty one — is decision-log-specific and correct; the file count
is not. Minimum fix: name both, or narrow the subject to the decision log.

The word *empty* is right in the sense the sentence uses it — the recreated file is the
3521-byte template carrying no rulings, not a zero-byte file — and `ONBOARDING.md` item 3 uses
the same word the same way, so the two agree.

### `L-3` — `assurance/templates/run-v2/README.md:15-17` names `run_repair.py` as taking round refs; it takes none

The `readme-three` fix turned "the three step scripts additionally take the round's refs as
CLI flags" into "the three round steps — `run_evidence_v2.py`, `run_bind_v2.py`,
`run_repair.py` — additionally take the round's refs as CLI flags (`run_retire.py`, the fourth
invocation below, takes none)".

`run_repair.py` has exactly three arguments (`assurance/templates/run-v2/run_repair.py:56`,
`:58`, `:60`): `run_dir`, `--repo-root`, `--emit`. `--emit` is a mode flag — `run_bind_v2.py`
takes it too — and `--repo-root` is not a round ref either. The README's own invocation list
shows this at `:22`: `run_repair.py <run-dir> [--emit]`, no refs beside it, against
`--base --candidate --candidate-branch` and `--evidence-commit --bound-at` on the other two.

The rider's premise was that the sentence was literally still true because those three happen
to take refs; that premise does not hold for `run_repair.py`, so naming the three converted a
vague sentence into a specific false attribution. Minimum fix: name the two that take refs and
say what `run_repair.py` takes, or replace "the round's refs" with "the round's flags".

---

## 4. Observations

### `O-1` — the new refusal test asserts a substring where its sibling asserts the whole line

`tooling/tests/document_harness/test_repo_root_discovery.py:114`:
`self.assertIn("--local-env-vars", str(caught.exception))`. `E5` says assert the whole line,
never a substring unrelated content can satisfy; the sibling refusal test at `:116-126`, in
the same class, asserts the entire message with `assertEqual`. No message this function can
currently raise other than the intended one contains that substring, so it binds today — this
is a consistency note, not a hole I could open.

### `O-2` — the `E1` disclosure is a process claim, marked and not verified (`R4`)

`fd525e4`'s body states all four holdings (dispatched by, prompted by, scoped by, reported
through) were in the executor's hands, one session throughout, taking `E1`'s exception
channel, with the FULL dispatched to its own session. Session facts are not visible to me.
What the repository does show, and I checked, is consistent with it: the disclosure is in the
commit body, which is where `E1` puts it; the plan's role-form line says the same; and the
freeze marker plus reflog show the review window opened at the tip and has taken nothing
since.

### `O-3` — ruling 3's routing has no carrier outside this round's own plan

The plan's opening ruling 3 sends the thirteen design-shaped rows to the `dispatch-economy`
batch. `CONSTRUCTION-LEDGER.md`'s `dispatch-economy` backlog paragraph — edited nowhere in
this range — does not record that they are coming, and none of the thirteen rows was touched.
The plan file stays in the tree, so the fact is recoverable; but that ledger paragraph calls
itself the scheduling carrier for the batch, and it is now one of two places that answers what
is in `dispatch-economy`. No rule I can find obliges the update, so this is an observation,
not a finding.

### `O-4` — the shape, reported and not concluded (`R5`)

This round's whole subject is the bank: thirty rows, of which ten were redeemed, four retired
by ruling, thirteen deferred as design and three left as standing checks. Sixteen remain, and
the plan's own inventory says thirteen of those sixteen need a round to redeem. Whether a debt
ledger whose redeemable fraction is a third of its rows is doing the work it was created to do
is not mine to conclude; I am reporting the shape because `R5` says to.

---

## 5. Coverage — what I read in full, sampled, and only probed (`R4`)

**Read in full.** `document-harness/CONSTRUCTION-CHECKLIST.md`;
`document-harness/ORCHESTRATION.md`; `document-harness/README.md`;
`document-harness/plans/rider-settlement.plan.md`; all three commit bodies; the full text of
all fourteen deleted rider rows; the entire candidate diff, all eleven files;
`tooling/tests/document_harness/test_repo_root_discovery.py`;
`tooling/rsclib/document_harness/caller.py:100-196`;
`tooling/rsclib/document_harness/paths.py:112-200`;
`tooling/rsclib/document_harness/dispatch.py:56-80` and `:800-965`;
`assurance/templates/run-v2/run_retire.py:140-166`;
`assurance/templates/run-v2/README.md:1-32`; the changed classes of
`tooling/tests/document_harness_review/test_dispatch.py` and
`tooling/tests/document_harness_review/test_run_v2_template_retire.py`;
`document-harness/ONBOARDING.md`'s clone table and items 1–4;
`tooling/hooks/layer_path_check.py:1-60`.

**Sampled.** `HARNESS-DECISIONS.md` — the header, §live in full (`HD-56`, `HD-44`, `HD-41`,
`HD-23`, `HD-9`, plus the titles of the rest), and the §implemented titles; not the
§implemented bodies. `CONSTRUCTION-LEDGER.md` — the two changed lines, reconstructed
character-level, plus the backlog section; not the CLOSED roll in full. Root `README.md` —
Quickstart, the commands table, Install; not in full. `README.zh-CN.md` — the two convention
paragraphs and the commands table only.

**Not read.** `document-harness/REVIEW.md` and `document-harness/EXECUTION.md` in full (I read
`EXECUTION.md:355-380` and `:514`), `contract/Document-Work-Assurance-Contract-v4.md`, the
sixteen surviving rider rows, and every prior review record except `v3-cold-read-21dad76.md`
(header and blob table) and the existence check on `v3-checkpoint-read-153302a.md`. This is a
FULL of one range, not a re-certification of the layer (`R4`), and the opening cold read was
waived by the user, not by me.

**Probed by execution.** `python -m pytest -q` at `8aa9f6e` → `854 passed in 142.76s`. Test
method counts re-derived from the trees rather than run at the base: 851 at `2522ce1`, 854 at
`8aa9f6e`, matching the body's 851 → 854. Five mutations of shipped code (`env=` dropped from
`discover_repo_root`; `.is_file()` deleted from the retire count, against both the pre-fix and
the shipped fixture; `out_files = list(to_delete)`; the executor charter bypassing
`instrument_relative`) and two against the proposed `B-1` fix. `dtw init` run twice on a
scratch caller with the instance files moved between runs.
`layer_path_check.unresolved_tokens` run over the added lines of both member edits — clean —
and all nine members resolve.

**Not verifiable from the repository.** Whether `E11`'s preview card was rendered and the user
waited on, and whether the executor session was cold. Both are marked, per `R4`, not folded
into supported.
