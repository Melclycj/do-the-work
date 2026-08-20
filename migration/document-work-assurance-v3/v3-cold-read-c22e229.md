# Cold read — the instruction layer at `c22e229`

`E10` read. Not a round: no verdict, no budget spent (`R3`). Findings are tiered
must-fix / low / observation, and their routing is `E10` / `R9` / `R10`'s, not mine.

**Dispatch as received.** One SHA — `c22e229776c8cb6f0b5ec0923f061ed3ccd086f2` — plus the
characterization "the instruction layer … (an E10 read)" and a pointer to the standing
contract. Under `R2` I treated the characterization as unverified until re-derived: the
repository states the same thing twice over (the freeze marker names this SHA as the
dispatched subject; the layer carries an application no independent read has covered — §1),
so nothing in this record rests on the chat text. Everything else below is re-derived from
the repository, including the member set, which comes from `E10`'s own sentence at the
subject blob rather than from any list I was handed. Every blob id is stated, which is what
keeps `E10`'s citation route open for the next read.

**Standing instructions read.** `ResearchSystem/migration/document-work-assurance-v3/v3-harness-review-contract.md`
(the stub) → `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` in full, both sides,
per the stub's "It is your standing instruction and its own counterpart; read all of it".
`ResearchSystem/HARNESS-DECISIONS.md` `§live` read in full as `E10`'s tail requires, plus the
file header and `§implemented`'s `HD-46` / `HD-45` / `HD-2` entries by grep (`§implemented`
is grep-reachable and outside the mandatory read; I opened those three because they are the
recorded rulings the newest layer text claims to carry).

## 1. Subject, re-derived

```
$ git rev-parse --show-toplevel
D:/Thesis-stage-control-refactor/ResearchSystem/harness

$ git status --porcelain
(no output)

$ git log --oneline -3 HEAD
c22e229 V3-PRECLEAR-BANK-CHARTER-PROSE-THIRD-v1
f854454 V3-PRECLEAR-BANK-CHARTER-PROSE-v1
8fbd8ea V3-ORCHESTRATOR-CHARTER-CLOSEOUT-RIDERS-v1

$ git log --oneline c22e229..HEAD
(no output)
```

The subject is the branch tip and the worktree is clean, so blob = file for every member; I
still read each member out of the object store where a quotation is load-bearing.

```
$ cat .harness/review-pending.json
{
 "subject": "c22e229776c8cb6f0b5ec0923f061ed3ccd086f2",
 "dispatched_at": "2026-08-18T13:35:12+00:00"
}
```

The marker's subject equals the dispatched SHA. `E9`'s window therefore opened at that
timestamp and closes when this record's commit lands; the branch has taken no commit since
(`git log … c22e229..HEAD` is empty), so the window held.

**Why this read is owed.** The layer changed after the last recorded end-to-end read of it:

```
$ git diff --stat 50016a8 c22e229 -- ResearchSystem/document-harness ResearchSystem/contract \
    ResearchSystem/schema/document-assurance-v3 \
    ResearchSystem/migration/document-work-assurance-v3/v3-harness-operating-contract.md \
    ResearchSystem/migration/document-work-assurance-v3/v3-harness-review-contract.md
 ResearchSystem/document-harness/ORCHESTRATION.md | 2 +-
 ResearchSystem/document-harness/README.md        | 2 +-
 2 files changed, 2 insertions(+), 2 deletions(-)
```

Both lines are `777d180` (`V3-ORCHESTRATOR-CHARTER-FREE-L1C-RIDE-v1`), a free-channel byte
application. `E10` says such an application "still owes its independent read, riding the next
read of this layer at per-member digest cost". This is that read, and those two lines get the
closest attention below.

## 2. The member set, and each member's blob

The set is `E10`'s own enumeration at the subject blob — "exactly these ten paths and nothing
else". Read in full, none by citation:

| # | member | blob at `c22e229` | lines |
|---|---|---|---|
| 1 | `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` | `87add4cef021153e465aaf30ff0c674dc19b6a0b` | 212 |
| 2 | `ResearchSystem/document-harness/README.md` | `f6aa735c4ad9315088799aebafbf58fd0fa5da92` | 38 |
| 3 | `ResearchSystem/document-harness/EXECUTION.md` | `4a7b6eca3e8f4fd43c2887005c44a5e616d8b5da` | 465 |
| 4 | `ResearchSystem/document-harness/REVIEW.md` | `3350bfac1b190cb1dac8566247f5382a7136f094` | 284 |
| 5 | `ResearchSystem/document-harness/ORCHESTRATION.md` | `82f10c1bd173fb795c723df072a6357287d4d366` | 95 |
| 6 | `ResearchSystem/migration/document-work-assurance-v3/v3-harness-operating-contract.md` | `17ff31bba177689bf22144603cecba533b5a4087` | 5 |
| 7 | `ResearchSystem/migration/document-work-assurance-v3/v3-harness-review-contract.md` | `b576a45e142015e128f4ab9d1461667f991aa046` | 5 |
| 8 | `ResearchSystem/contract/Document-Work-Assurance-Contract-v3-supersession-1.md` | `68031fa2ca31272e31da0d42a9a02189d28fcc21` | 124 |
| 9 | `ResearchSystem/contract/Document-Work-Assurance-Contract-v3-supersession-2.md` | `e1a2f26b1d8d323d11e900f8137dea222b6571c1` | 113 |
| 10 | `ResearchSystem/schema/document-assurance-v3/paragraph-map.schema.json` | `09aa869962f592c2f86c9379be0ef3eb7d2232ff` | 44 |

1 385 lines. Blob ids from `git ls-tree -r c22e229 --format='%(objectname) %(path)'`, line
counts from `git cat-file blob <id> | wc -l`. Members 2 and 5 are the two `777d180` touched;
the other eight are byte-identical to their state at `50016a8` and would have been citable —
I read them anyway, so no citation is claimed and the next read may cite this record for any
of the ten.

Two of the three `E2` blob ids `E2` names are members (8 and 9); the third, the signed
contract `b2dbdf752d8c155e4c65b14b5f420b880b8184a1`, is not a member and matched at the
subject. The pack directory `E2` freezes holds 15 files
(`git ls-tree c22e229 ResearchSystem/schema/document-assurance-v3/ | wc -l` → `15`), which is
the count `E2`'s parenthesis states.

## 3. What I re-derived by command

**3.1 The membership sentence's three mirrors agree.** `E10`'s ten paths, `layer_path_check.LAYER`
(:30–41) and `test_precommit_checks.LayerMembership.EXPECTED` (:164–175) are the same ten
paths in the same order, compared by hand and then mechanically:

```
$ python -m pytest -q tests/document_harness/test_readme_enumeration.py \
    tests/document_harness/test_precommit_checks.py      # run from ResearchSystem/tooling
44 passed in 13.78s
```

`HD-22`'s three-site discipline is satisfied at this subject; `E10-sync` stays a live
check-item rather than being redeemed, which is what that row says it is.

**3.2 The README's schema enumeration is current.** 15 schema files, 15 stems named across
the README's four schema rows; the guard that pins this is the same suite above.

**3.3 The contract fixtures reproduce the README's figure.**

```
$ python validate_fixtures.py            # migration/document-work-assurance-v3/N0/fixtures
41/41 cases behaved as declared; failures=0
```

README :33 says "41/41 green" — re-run, not accepted.

**3.4 The local-enforcement row is true of both repositories.** The caller's
`.githooks/pre-commit` :57–59 invokes exactly `review_freeze_check.py` and
`candidate_path_check.py` from the submodule; `layer_path_check.py` is not invoked, and its
paragraph there now says "ten of them since 2026-08-18" (the stale "nine" the `50016a8` read
reported as `O-4` has been corrected). This repository's git dir holds only
`*.sample` hooks and `core.hooksPath` is unset (`git config --get core.hooksPath` → exit 1),
so README :34's "this repository … installs no hook at all" holds. Scope of this paragraph:
this machine's two worktrees, at this moment — a caller-side fact, not a repository property.

**3.5 `dtw dispatch` has three modes and none dispatches an executor.**
`rsclib/document_harness/cli.py` :487–498 defines one mutually-exclusive required group:
`--subject` ("PRODUCT run"), `--range` ("CONSTRUCTION round"), `--read` ("E10 layer read").
`ORCHESTRATION.md` :26–32 asserts exactly this; it holds at the subject.

**3.6 The battery enumeration's split-by-repository claim holds.** None of the five
caller-side scripts `EXECUTION.md` :343–348 names exists in this repository
(`find` over the whole tree returns `tests/document_harness/run_tests.py` and
`tests/document_harness_review/run_tests.py` — different paths — plus
`migration/…/N0/fixtures/validate_fixtures.py`, not `schema/fixtures/`; no `rsc.py`,
no `run_p4_tests.py`, no `run_p5a_tests.py`), and all five exist in the caller. `0d73a5f`, the
instrument base that section cites, is a commit in this repository.

**3.7 `REVIEW.md`'s witnessed example checks out.** Its :44–47 claims four of the
`p5b-firewall` FULL's seven findings name checker assertion strength. The record
(`v3-review-full-fef3a2e.md`, in the caller tree) lists f1–f7, and f2–f5 name
`chk-bookkeeping`, `chk-tripwires`, `chk-tooling`, `chk-open` respectively. Four of seven,
exactly as written.

**3.8 The `777d180` application swept its class.** The corrective it applied re-scoped
README :19 from one UNSIGNED site to two. The sibling site is README :18 (supersession 1):

```
$ grep -n "UNSIGNED" <supersession-1> <supersession-2> <document-harness/README.md>
supersession-1.md:3
supersession-2.md:3
supersession-2.md:107
README.md:18
README.md:19
```

Supersession 1 asserts UNSIGNED once, so README :18's singular scope is correct and the class
has no second instance to fix. `E7` / `HD-41` ④ satisfied for that application.

## 4. Findings

0 must-fix · 2 low · 3 observation.

### L-1 (low, bytes supplied) — README's local-enforcement row now attributes the candidate lint's scope rule to the unwired layer check

**Location.** `ResearchSystem/document-harness/README.md` :34 (member 2, blob `f6aa735c`),
inside the *Local enforcement* cell:

> **The third, instruction-layer path resolution, currently runs nowhere.** It guards this
> layer's ten members, … Re-homing it is caller-onboarding work and is open. It judges work
> products only: a record quotes the broken path it reports, and a specification (a run's
> instruction and control plane) names the files the work is required to create, so neither
> is scanned.

**Ground truth.** The three sentences beginning "The third…" bind three pronouns to
`layer_path_check.py`, and the third binding is false. Records and specifications are
`candidate_path_check.py`'s exemptions, not that check's: `RECORD_SURFACE` /
`SPECIFICATION_SURFACE` / `VENDORED` are defined at `hooks/candidate_path_check.py` :64–94 and
consumed by its `scanned()` (:97–100); `layer_path_check.py` has no such list — it scans exactly the ten
members of `LAYER` (:30–41), two of which (the retired-contract stubs) live under
`ResearchSystem/migration/`, a `RECORD_SURFACE` prefix. Under the sentence as it now reads,
those two would be exempt from the layer check; they are its members. Provenance, since the
sentence itself is old: at `345acdd` it sat immediately after the clause introducing "the
candidate-side path lint", where it was correct, and `35e9a05` inserted the third-check
paragraph between the two, stranding it.

**What changes if it stays.** The adjacent sentence names the live decision — "Re-homing it is
caller-onboarding work and is open". Whoever performs that re-homing reads this cell for what
the check does and finds a record/specification exemption it does not have; the cheapest wrong
outcome is a re-homed guard that skips the two stub members, and the layer's own amendment
files are exactly the class the candidate lint's docstring says the guard "waves through" is
where the defect it exists for was found. Nothing fires today, because the check is installed
in neither repository (§3.4), which is why this is low and not must-fix.

**Bytes (minimum fix).** Replace the sentence's opening pronoun so it names its subject:
`It judges work products only:` → `That candidate-side lint judges work products only:`.
Nothing else in the cell changes; no clause is added to any rule and nothing a rule requires
changes, so the design test does not fire. The path is a member but is not `E2`-frozen, and no
round has relied on the sentence in `E10`'s sense — an outcome would not have changed had it
read correctly, since no round has re-homed or run the check — so the free-channel conditions
read as open. Whether it takes that channel is `E10` / `R10`'s to say, not mine.

### L-2 (low, wording-level, bytes supplied) — the `777d180` correction left its own trailing pronoun singular

**Location.** `ResearchSystem/document-harness/README.md` :19 (member 2, blob `f6aa735c`), the
Supersession-2 row, in the bytes `777d180` wrote:

> The carrier asserts UNSIGNED twice — its top-of-file status line and its own §5 Signature —
> and both are pre-signature residue; post-signature the contract's own §13 … bars the
> in-place correction, so this row and the record, **not that line**, state the signature

**Ground truth.** The row's subject was made plural ("twice", "both", two named sites) and the
clause that closes the sentence still says "not that line". Verified against the carrier
(§3.8): two sites, :3 and :107. The neighbouring row :18 correctly keeps the singular, because
supersession 1 has one such line — so this is one site, not a class.

**What changes if it stays.** Nothing an actor does. The row leads with "signed 2026-07-30",
names the signature record, and the plural is stated twice in the same sentence before the
stray singular, so the accurate fact is recoverable from the adjacent text. Under `R9`'s test
I can name no downstream decision that goes wrong, which is what makes this wording-level
rather than low-with-consequence; I file it at low only because the tiers a read has are
must-fix / low / observation.

**Bytes (minimum fix).** `not that line` → `not those lines`.

**Routing note, stated because it is checkable and not mine to decide.** Rider `wl-route`
banks the open dispute over where a wording-level finding *with supplied bytes* goes, and
gives it a deadline: "下一份对 wording-level finding 供字节的 read 记录". `777d180`'s body
judged that deadline not to have arrived, on the ground that the `50016a8` read's `L-1` had a
nameable downstream miss and so was not wording-level. This finding has no nameable
downstream decision and supplies exact bytes, so on the face of the rider's own words the
deadline arrives with this record. I do not route it; I report that the condition it names is
now met.

### O-1 (observation) — the charter's `HD-2` row assigns the state flip to the orchestrator without the restriction that only the user may make one

`ORCHESTRATION.md` :48 (member 5, blob `82f10c1b`), the ninth row of *The nine obligations
that are already law elsewhere*, now reads — after `777d180` deleted its false `§live` route —

> | flip a decision entry's state only in the commit that lands its carrier | `HD-2`, which
> lives in the decision log — outside this layer |

The rule it cites carries a restriction the row does not: `HARNESS-DECISIONS.md` :16–17 lists
as an invariant "只有用户能翻状态，session 只能提议（`E1`/`R5`）", and `HD-45` / `HD-46` each
record their own initial state as carried in the same commit precisely because it is "不是
session 事后翻态". The row states a timing constraint as an orchestrator obligation and is
silent on who decides. Two things keep this an observation rather than a low. First, the
charter's closing prohibition already covers the substance in general terms — "Automating the
answer is signing for the user, and no session may do that" — though its enumeration of
routed questions is "`R5`, `R10` and `E11`" and does not include this one. Second, the
restriction sits in the decision log's header, above `§live`, which the opening obligation
opens anyway.

This is the same class as rider `charter-qualifiers` (a cite-only row carrying the content
without a qualifier of the cited rule) but not covered by it: that row names three instances
and records that all three compress in the stricter direction, whereas this one drops an
actor-restriction, which is the looser direction. **No bytes.** `charter-qualifiers` already
records the user's-judgment shape of the fix — restoring a qualifier to a summary cell in a
file whose whole design is not to restate rules is a bound, and `E10` makes that design.

### O-2 (observation, outside the layer) — a fifth prose site keyed to membership went stale when the tenth member joined

`hooks/candidate_path_check.py` :15 says "the six Markdown instruction-layer members outside
`NOT_SCANNED` are scanned by both". Computed at the subject from the two modules themselves:

```
$ python -c "... [p for p in layer_path_check.LAYER if candidate_path_check.scanned(p)]"
7
  …/CONSTRUCTION-CHECKLIST.md  …/README.md  …/EXECUTION.md  …/REVIEW.md
  …/ORCHESTRATION.md  …/supersession-1.md  …/supersession-2.md
```

Six was right while the layer had nine members; `ORCHESTRATION.md` made it seven. `HD-22`
pins three sites and the `50016a8` read added a fourth in the caller; this is a fifth, in this
repository, in a module docstring rather than in a rule. Nothing fires on it — no test asserts
the number, and the count is descriptive prose about a guard that is wired in one repository
and describes a set it does not itself enumerate. It is outside the ten members, so it is
outside the subject of this read and outside `E10`'s channels; I report it because it drifted
as a direct consequence of a layer change and the round that made that change swept three
sites plus the caller's hook.

### O-3 (observation) — the two older role files still describe a two-role world

`EXECUTION.md` :4 ("Its counterpart is [REVIEW.md]") and `REVIEW.md` :4 ("counterpart is
[EXECUTION.md]") were not touched when `ORCHESTRATION.md` became the tenth member, while
`ORCHESTRATION.md` :4–5 names both of them as its counterparts. A reader entering the layer
through either older file is told the role model has two sides. Nothing is misstated — neither
file makes a claim about the number of roles — and the layer's navigator (`README.md` :26)
does point at the new member, so the file is reachable. Recorded rather than fixed: whether a
role file should name a third is the kind of judgment `R5` keeps me out of, and the reading
under which the pair are each other's counterpart *as the two sides of a run* is available and
consistent with `ORCHESTRATION.md`'s own §thin. **No bytes.**

## 5. Coverage, and what this read did not establish

**Read in full at the subject blobs:** all ten members, 1 385 lines, none by citation (§2).

**Read in full outside the layer:** `ResearchSystem/HARNESS-DECISIONS.md` header and `§live`
(:1–134) end to end; `ResearchSystem/HARNESS-RIDERS.md` (all 29 rows); the commit bodies of
`c22e229`, `f854454`, `777d180`; `hooks/layer_path_check.py`, `hooks/candidate_path_check.py`
:1–100, `tests/document_harness/test_precommit_checks.py` :155–190,
`tests/document_harness/test_readme_enumeration.py`; the caller's `.githooks/pre-commit`;
`v3-review-full-fef3a2e.md`'s findings table; §4 and §5 of `v3-cold-read-50016a8.md`.

**Sampled / probed only:** `HARNESS-DECISIONS.md` `§implemented` (only `HD-46`, `HD-45`,
`HD-40` headers and `HD-1`–`HD-8`, by grep); `rsclib/document_harness/cli.py` (docstring and
the `dispatch` / `review` parser blocks only); the schema pack beyond `paragraph-map` (listed,
counted, not read); the earlier read and review records beyond the two named above (used to
locate already-banked findings, not re-verified).

**Not established.**

- **Whether the banked findings this read did not re-raise still hold.** I checked the rider
  bank to avoid re-reporting, and re-derived only the ones my findings touch
  (`charter-qualifiers`, `wl-route`, `E10-sync`). The other rows are taken as filed.
- **That the layer is defect-free.** One context read 1 385 lines of instruction prose plus
  its cited machinery; the three findings above are what that pass surfaced, and a reader who
  reads "0 must-fix" as a proof of soundness will over-trust it.
- **`R4` items.** No process claim in this record is verifiable: that this context was fresh,
  that no material beyond the dispatch reached it, and that the reasoning above was not
  influenced by the executor are declarations, not evidence. My independence is structural in
  `R1`'s sense only if the orchestrator, not the executor, set this question — which I cannot
  see from inside the repository (`R7`: I state the ceiling and move on).
- **Anything about the caller repository beyond §3.4 and §3.6.** Those two paragraphs read one
  worktree on one machine at one moment. The gitlink that pins this instrument was not
  inspected.
- **Whether the guards in §3.1 bind.** I ran them; I did not mutate them. `R8`'s
  mutation-testing is a round's instrument, and the guard concerned
  (`test_layer_equals_the_hand_written_membership`) carries its own mutation provenance in its
  docstring (`v3-review-full-8ec4c60.md` B2), which I cite rather than repeat. What the suite's
  green in §3.1 establishes is that the three sites agree today, not that a fourth site could
  not drift unnoticed — rider `E10-sync` records that the prose leg has no guard at all.
