# Cross-repository references — the sweeps and the guard experiment (2026-08-20)

Round `XREPO-REFS`, R2 of batch DTW-INDEPENDENCE (`HD-50`). Analysis and measurement only:
the rulings are the user's and live in the decision log, the outcome lives in the round's
commit body, and what is here is the evidence those two rest on — the class definition the
round had to settle before it could sweep, the before/after sweeps, the guard experiment with
its negative control, and one measurement that falsified a sentence this round had already
written.

Kept here rather than in the commit body under `E3`'s *"output kept in the commit body or the
round journal"* and `HD-41` ④, and because the opening pair's `L-2` found the previous
amendment's sweep evidence in neither place.

## 1. The class, defined before it was swept

`E10`'s new clause and `R2`'s acceptance criterion both need a class, and three earlier reads
left it underdetermined: `v3-cold-read-69fc082.md` `O-1` found a caller path with no
`ResearchSystem/` prefix (`EXECUTION.md:340`, `ExperimentLab/papers/`), and
`v3-checkpoint-read-48b6c5f.md` `O-2` found two record **filenames** carrying a subject SHA
and recorded that whether such a filename counts is undecided.

The definition this round used, by **where the target lives** rather than by string prefix:

> A *caller-held reference* is a reference written in an instruction-layer member whose
> target exists at no path of this repository.

That test is prefix-blind, so `ExperimentLab/papers/` is in the class and
`ResearchSystem/tooling` (which resolves here) is not.

**The remedy, however, is decided by the reader's action**, and that is what settles the
filename question. A markdown link and a backticked token containing `/` both ask a reader —
or a guard — to *resolve* something; when the target is elsewhere they resolve to nothing, or
worse to a same-named local file. A bare backticked **name** asks the reader to *identify* an
artifact and offers no path to follow, so it cannot resolve wrong. A bare name is therefore
**in the class and already in the remedy's output form**: what it still owes is the sentence
saying which repository holds it.

So a SHA inside a record filename does not make the filename a commit citation, and a record
filename is not a path reference. `EXECUTION.md`'s `v3-review-full-86defbc.md` and
`REVIEW.md`'s `v3-review-full-fef3a2e.md` needed the holder sentence, not the demotion — and
both sat inside sentences this round was rewriting anyway, so the decision cost nothing. The
overlap `O-2` reports (one site classified both as a broken link and as a filename) is
resolved the same way: `REVIEW.md:45` carried a link *and* a name; the link went, the name
stayed.

## 2. The reference sweep — pattern, and before/after

The sweep is `sweep_refs.py`, which enumerates three reference forms over the ten `E10`
members and resolves each against this repository:

- `LINK` — markdown link target, matched by `\]\(([^)\s]+)\)`
- `PATHTOK` — backticked token containing `/`, matched by layer_path_check's own pair
  `` `([^`\s]+)` `` + `^[A-Za-z0-9_.\-/]+(?:\.(?:md|py|json|yaml|yml|txt|js)|/)$`
- `NAMETOK` — backticked token with no `/` matching `^[A-Za-z0-9_.\-]+\.(ext)$`

`LINK` and `PATHTOK` resolve by layer_path_check's three roots (repo root, the file's own
directory, under `ResearchSystem/`), with a target that only resolves by escaping the repo
root counted as not resolving. `NAMETOK` resolves against the **basenames of every tracked
file**, because a bare name has no directory to resolve from — an earlier version of this
sweep resolved names root-relatively and produced five false hits, including
`Document-Work-Assurance-Contract-v3-supersession-1.md`, which does live here.

**Before** — 20 hits at `c53fc4e`:

```
PATHTOK ResearchSystem/document-harness/README.md:36      .harness/review-pending.json
PATHTOK ResearchSystem/document-harness/EXECUTION.md:186  ResearchSystem/assurance/runs/p5a-shells/control/audit-rounds.md
NAMETOK ResearchSystem/document-harness/EXECUTION.md:193  build_run.py
NAMETOK ResearchSystem/document-harness/EXECUTION.md:198  check_shells.py
NAMETOK ResearchSystem/document-harness/EXECUTION.md:282  write_audit.py
PATHTOK ResearchSystem/document-harness/EXECUTION.md:340  ExperimentLab/papers/
NAMETOK ResearchSystem/document-harness/EXECUTION.md:340  smoke_test.py
PATHTOK ResearchSystem/document-harness/EXECUTION.md:343  ResearchSystem/tooling/tests/run_tests.py
PATHTOK ResearchSystem/document-harness/EXECUTION.md:345  ResearchSystem/tooling/tests/run_p4_tests.py
PATHTOK ResearchSystem/document-harness/EXECUTION.md:346  ResearchSystem/tooling/tests/run_p5a_tests.py
PATHTOK ResearchSystem/document-harness/EXECUTION.md:347  ResearchSystem/schema/fixtures/validate_fixtures.py
NAMETOK ResearchSystem/document-harness/EXECUTION.md:448  v3-review-full-86defbc.md
PATHTOK ResearchSystem/document-harness/EXECUTION.md:449  ResearchSystem/assurance/runs/p5a-shells/control/audit-rounds.md
PATHTOK ResearchSystem/document-harness/EXECUTION.md:452  ResearchSystem/assurance/runs/p4-doc/issues/user-decision-triage-comparator-environment-defects.json
LINK    ResearchSystem/document-harness/REVIEW.md:45      ../migration/document-work-assurance-v3/v3-review-full-fef3a2e.md
NAMETOK ResearchSystem/document-harness/REVIEW.md:45      v3-review-full-fef3a2e.md
NAMETOK ResearchSystem/document-harness/REVIEW.md:132     review-verify.json
PATHTOK ResearchSystem/document-harness/REVIEW.md:138     .harness/review-pending.json
PATHTOK ResearchSystem/contract/…-supersession-2.md:60    assurance/runs/
PATHTOK ResearchSystem/contract/…-supersession-2.md:99    templates/run-v2/
-- 20 caller-held or unresolvable references over 10 members
```

**After** — 16 hits, of which `LINK` is empty and every remaining `PATHTOK` is accounted for:

```
PATHTOK ResearchSystem/document-harness/README.md:36      .harness/review-pending.json
NAMETOK ResearchSystem/document-harness/EXECUTION.md:186  audit-rounds.md
NAMETOK ResearchSystem/document-harness/EXECUTION.md:194  build_run.py
NAMETOK ResearchSystem/document-harness/EXECUTION.md:199  check_shells.py
NAMETOK ResearchSystem/document-harness/EXECUTION.md:283  write_audit.py
NAMETOK ResearchSystem/document-harness/EXECUTION.md:342  smoke_test.py
NAMETOK ResearchSystem/document-harness/EXECUTION.md:346  run_p4_tests.py
NAMETOK ResearchSystem/document-harness/EXECUTION.md:346  run_p5a_tests.py
NAMETOK ResearchSystem/document-harness/EXECUTION.md:451  v3-review-full-86defbc.md
NAMETOK ResearchSystem/document-harness/EXECUTION.md:452  audit-rounds.md
NAMETOK ResearchSystem/document-harness/EXECUTION.md:455  user-decision-triage-comparator-environment-defects.json
NAMETOK ResearchSystem/document-harness/REVIEW.md:45      v3-review-full-fef3a2e.md
NAMETOK ResearchSystem/document-harness/REVIEW.md:133     review-verify.json
PATHTOK ResearchSystem/document-harness/REVIEW.md:139     .harness/review-pending.json
PATHTOK ResearchSystem/contract/…-supersession-2.md:60    assurance/runs/
PATHTOK ResearchSystem/contract/…-supersession-2.md:99    templates/run-v2/
-- 16 caller-held or unresolvable references over 10 members
```

The four surviving `PATHTOK`s split two ways. Both `.harness/review-pending.json` sites are
the freeze marker `dtw dispatch` writes in **whichever repository dispatches** — `.harness/`
exists here and carries `runs.jsonl` — so the target's home is this repository and it is
simply absent at rest; the retired rider `layer-outbound-refs` excluded them for the same
reason. The two supersession-2 sites are `E2`-frozen and bank (R0.2). Of those two, only
`assurance/runs/` is genuinely caller-held; `templates/run-v2/`'s real target is
`ResearchSystem/assurance/templates/run-v2/` **in this repository**, so it is the
missing-prefix class the retired-in-place rider `frozen-path-prefix` carries, not this one.
The sweep cannot tell those apart and neither can be written, so the distinction changes
nothing this round — it is recorded so the next round that can write them knows there are two
defects there, not one.

Every `NAMETOK` is a name, which §1 rules the compliant form.

## 3. The whole standing stock against the guard's own criterion

`R1`'s consistency bullet asks for text and guard agreeing **by construction**, not by the
accident that the guard scans only added lines. So the guard's own predicate was run over the
complete text of all ten members rather than over a staged diff:

```
$ python -c "… from hooks import layer_path_check as L; for m in L.LAYER: print(L.unresolved_tokens(root, m, read(m)))"
ResearchSystem/contract/…-supersession-1.md [('schema/document-assurance-v3/review.v2.schema.json', 'resolves only under ResearchSystem/ — prefix missing')]
ResearchSystem/contract/…-supersession-2.md [('schema/', 'resolves only under ResearchSystem/ — prefix missing')]
whole-stock scan complete
```

Two violations, both inside the `E2`-frozen supersessions — the exact exception the new `E10`
clause names. The eight writable members are clean against the guard's criterion for their
whole standing text, so the added-lines limitation has nothing left to hide: the stock is
empty of the class, the guard covers what a commit adds, and the clause binds both.

## 4. The guard experiment — before, after, negative control

Run in a throwaway clone of the instrument at `c53fc4e`, so that the subject repository's
index was never touched. The before-state reproduces rider `layer-crossrepo-token`'s own
experiment: the caller-side battery bullet was re-wrapped — same five commands, byte-identical
path tokens, one wording word — which is what a batch rewriting that sentence does, and which
puts those lines into the added set the guard scans.

```
BEFORE  $ git add ResearchSystem/document-harness/EXECUTION.md
        $ python ResearchSystem/tooling/hooks/layer_path_check.py
        exit=1
        pre-commit BLOCKED: newly added instruction text names a repository path that does not resolve:
          …EXECUTION.md: `ResearchSystem/tooling/tests/run_tests.py` — does not resolve from the repo root
          …EXECUTION.md: `ResearchSystem/tooling/tests/run_p4_tests.py` — does not resolve from the repo root
          …EXECUTION.md: `ResearchSystem/tooling/tests/run_p5a_tests.py` — does not resolve from the repo root
          …EXECUTION.md: `ResearchSystem/schema/fixtures/validate_fixtures.py` — does not resolve from the repo root

AFTER   (this round's three amended members staged, 32 insertions / 20 deletions)
        $ python ResearchSystem/tooling/hooks/layer_path_check.py
        exit=0

NEGCTL  (two tokens injected into EXECUTION.md on top of the after-state)
        $ python ResearchSystem/tooling/hooks/layer_path_check.py
        exit=1
          …EXECUTION.md: `ResearchSystem/document-harness/NO-SUCH-FILE.md` — does not resolve from the repo root
          …EXECUTION.md: `document-harness/EXECUTION.md` — resolves only under ResearchSystem/ — prefix missing
```

The negative control is doing two jobs. `NO-SUCH-FILE.md` proves the guard did not stop
binding on the broken-absolute class — the after-state's `exit=0` is the text having nothing
left to catch, not the check having gone quiet. `document-harness/EXECUTION.md` proves the
second branch, missing-prefix, also still fires; that branch is the one the frozen supersession
tokens sit on, so it had to be shown alive rather than assumed.

`R4`'s ceiling applies to all three: this proves the guard has binding force on these two
classes, not that its force is sufficient. It sees backticked tokens only. The markdown link
this round removed from `REVIEW.md:45` was never visible to it and would not have been caught
by any amount of staging — which is why the round's answer is the text changing and the rule
in `E10`, not a new check (`E6`).

## 5. A measurement that falsified this round's own first draft

The first draft of the demoted battery bullet read *"five commands whose scripts live in the
caller's own tree and in no path of this one"*. The after-sweep contradicted it: `run_tests.py`
and `validate_fixtures.py` did not appear as unresolved `NAMETOK`s, because files of those
basenames exist here.

```
$ git ls-files | grep -E "/(run_tests|run_p4_tests|run_p5a_tests|validate_fixtures|rsc)\.py$"
ResearchSystem/migration/document-work-assurance-v3/N0/fixtures/validate_fixtures.py
ResearchSystem/tooling/tests/document_harness/run_tests.py
ResearchSystem/tooling/tests/document_harness_review/run_tests.py
```

Scope: tracked files of this repository at `c53fc4e`. Three files, two of the five names. None
is the caller's battery script; the `validate_fixtures.py` here is the N0 contract-fixture
runner, and the two `run_tests.py` are per-package test entry points.

This is the real cost of demoting a path to a name, and it is not the cost the sentence first
assumed. A path is unique inside a repository; **a name is not unique across repositories**, so
demotion trades a reference that resolves *wrongly* for one that may resolve *ambiguously*. The
trade is still right — a wrong resolution is silent, an ambiguous one is visible to a reader
who is told to expect it — but the sentence has to tell them. It now does, and it does so as a
standing rule rather than a count, because the count drifts and the hazard does not.

Same shape, already in the text one bullet above: the instrument's own leg must be run from
`ResearchSystem/tooling` precisely because a papers tree in the caller carries two files named
`smoke_test.py` (measured there: `ExperimentLab/papers/agentspec/replication/smoke_test.py`
and `…/guardagent/replication/smoke_test.py`). The collision hazard was already the reason for
one clause in this section before it became the reason for another.

## 6. What the round measured about itself

- Membership sentence, `E10`: extracted from `HEAD` and from the working tree and hashed —
  `sha256 ab50782010cfa8e6…`, 869 chars, **IDENTICAL**. `E10-sync` (`HD-22`) does not fire, and
  the two mirrors were checked anyway: `test_layer_equals_the_hand_written_membership` and its
  neighbour, `2 passed, 41 deselected`.
- Provenance clause (`R4`): `grep -rn "provenance"` across the ten members returns the clause
  itself and nothing else; the other hits in this repository are plans, `split-design.md`, and
  the `document-harness/README.md` Local-enforcement row, all of them narrating the
  `contract_provenance_check.py` deletion of 2026-07-28 rather than relying on the clause. No
  round in flight relies on it: `XREPO-REFS` is the only open round and its candidate does not.
- Tier (`R6`): derived from the diff — five markdown files, no schema, tooling or generated
  path, and no member path added, removed or renamed, so the tiering section's own exception
  does not convert it. **Doc-only**; the instrument leg was run anyway because it is cheap:
  `733 passed in 100.67s`, unchanged in count from the two reads of the opening pair.

## 7. Method note, for the next sweep

`\b`-anchored hex or token patterns silently fail before `…` in this environment's grep build:
`grep -oE '\b[0-9a-f]{7,40}\b'` returns nothing for `` `b2dbdf75…` `` while `grep -oE
'[0-9a-f]{8}'` returns it. Unanchored patterns over-match instead. Neither is wrong to use —
what is wrong is using one without saying which, so every sweep in this record states its
pattern beside its output. This cost the phase-1 amendment nothing only because the tokens it
missed were blob ids already outside its class.

## 8. Repair leg — what the FULL falsified, and what the clause now says

`v3-review-full-dd18226.md` returned `CHANGES_REQUIRED` on `B-1`: the clause's enforcement
sentence claimed `layer_path_check` enforces the caller-held-path rule, and the guard is blind
to the class's central shape. The user approved one fix covering `B-1`, `L-1`, `O-2`'s wording
half and `O-3`.

**The measurement that decided it, re-run after the repair.** The reviewer's falsifying
experiment, reproduced in a throwaway clone of `55c36c9` with the repaired clause staged. One
added line carrying three caller-held tokens, none written in this repository's path
convention:

```
+A caller-held example: `ExperimentLab/papers/` and `assurance/runs/p5a-shells/control/audit-rounds.md` and `.goals/plans/x.plan.md`.
$ python ResearchSystem/tooling/hooks/layer_path_check.py
exit=0   (no output)

POSITIVE CONTROL — the same run artifact, this repository's prefix restored:
+Positive control: `ResearchSystem/assurance/runs/p5a-shells/control/audit-rounds.md`.
$ python ResearchSystem/tooling/hooks/layer_path_check.py
exit=1
pre-commit BLOCKED: newly added instruction text names a repository path that does not resolve:
  …EXECUTION.md: `ResearchSystem/assurance/runs/p5a-shells/control/audit-rounds.md` — does not resolve from the repo root
```

Unchanged from the reviewer's run, and that is the point: the repair changed no behaviour,
only the sentence that described it. Three caller-held tokens still pass silently; the same
target with the prefix still blocks. What the clause now says is that this is so.

**Why the replacement is not the reviewer's line verbatim.** The minimum fix offered enumerates
the guard's two decidable shapes, one of which is *missing-prefix* — a shape that exists only
because this repository still carries the caller's `ResearchSystem/` prefix, which R3 is
chartered to remove. Baking it in would make the clause false one round from now, in the
opposite direction. The replacement states the guard's **trichotomy** instead: it decides
tokens it can relate to this repository — written in its path convention, or resolving
somewhere inside it — and skips the rest as possibly illustrative. That is convention-neutral,
so re-rooting changes what "its path convention" denotes without touching the sentence, and the
honest half `B-1` demanded is the clause's own last sentence: the skipped shape, and the
standing stock the guard never re-scans, are held by the clause alone.

The witnessed instance stays named but is deliberately **not reproduced as a token** — the
caller's ExperimentLab papers directory is written as prose, because writing it as a backticked
path token in a member is precisely what the clause forbids. A rule that violated itself in its
own example would be the same defect one layer down.

**`L-1`: the at-rest falsifier, and the sweep for others.** `.harness/review-pending.json`
appears at `README.md:36` and `REVIEW.md:139`, and at rest the file does not exist —
`ls .harness/` returns `runs.jsonl` and nothing else, the dispatch window having closed. Under
the clause's flat first sentence those two member sites were violations; the exception now
lives in the clause rather than in this journal, which is not a member and cannot carry a
rule's exception.

Two instruments, because one cannot see the class. The guard's own predicate over the complete
text of all ten members:

```
$ python -c "… from hooks import layer_path_check as L; for m in L.LAYER: print(L.unresolved_tokens(root, m, read(m)))"
…supersession-1.md [('schema/document-assurance-v3/review.v2.schema.json', 'resolves only under ResearchSystem/ — prefix missing')]
…supersession-2.md [('schema/', 'resolves only under ResearchSystem/ — prefix missing')]
whole-stock scan complete -- members: 10
```

That predicate **skips the resolve-nowhere class by design**, which is the class both the
runtime marker and `B-1`'s central shape sit in — so running only it would repeat the error
`B-1` names. `sweep_refs.py`'s broader `LINK` + `PATHTOK` classes (§2 for the patterns), at
rest:

```
$ python sweep_refs.py . | grep -v "^NAMETOK"
PATHTOK ResearchSystem/document-harness/README.md:36    .harness/review-pending.json
PATHTOK ResearchSystem/document-harness/REVIEW.md:139   .harness/review-pending.json
PATHTOK …supersession-2.md:60                           assurance/runs/
PATHTOK …supersession-2.md:99                           templates/run-v2/
-- 16 caller-held or unresolvable references over 10 members
```

`LINK` is empty. Four `PATHTOK`s: the two runtime markers the new exception covers, and the two
`E2`-frozen sites the clause already excepts. **No other at-rest falsifier exists** — the
sentence is now true of the whole standing stock, not merely of the writable part.

**`O-2`'s wording half.** `ORCHESTRATION.md:90` glossed the `E1` disclosure as what a session
"owes **in its record**" — the wording `E1` had just replaced with its named carriers. In a
cite-only file the repair is to shrink toward the pointer, never to grow toward a copy, so the
gloss loses the stale carrier and keeps the assignment: *"what a session holding both work-side
roles owes — is `E1`'s to state"*. The nine-obligation-table gap the same observation names is
**not** in this leg; it banks at closeout, because a table row opens rider `charter-qualifiers`'
surface for the same reason the candidate gave.
