# Round `CORE-ONLY-LAYER` — the executor's journal

Batch `CORE-ONLY`, round 1 of 3, base `db1bfa1`. Written by the round's cold executor, which
holds none of `R1`'s four holdings: dispatched by the orchestrator, prompted by its instruction,
scoped by that instruction and by `document-harness/plans/core-only.plan.md`, reported through
the orchestrator.

What this file is for: the round's measurements, the judgement calls that are the executor's,
and the four things that go up rather than get decided here. The commit bodies carry the
site-by-site record of what changed; this file does not repeat them.

## 1. The item map, and what this round did not touch

| item | this round | where the rest is |
|---|---|---|
| A — the rule split | done, commit 2 | — |
| B — the membership rule and its guard | done, commit 2 | — |
| E — the contract's provenance | done, commit 3 | — |
| G — riders | done across commits 1–3 | — |
| H — the caller config | guards' half done, commit 1 | `dtw dispatch` naming the declared rules: round `CORE-ONLY-CODE` |
| I — this repository as a caller | done, commit 1 | — |
| C — the code split | not this round | round `CORE-ONLY-CODE` |
| D — the two stubs | not this round | round `CORE-ONLY-CODE` |
| F — the product run | not this round | round `CORE-ONLY-RUN`, in the caller |

## 2. The rule split, and the three judgements the plan left open

The plan's *Sketch* gives the criterion and not the answer: **does a product run obey it**, rule
by rule, cited or not. Twenty-one rules go to `document-harness/RULES.md`; one stays.

**`E2` stays**, and it is the only one. Its subject is this instrument's own bytes — one contract
path and one schema directory that a repository mounting this harness may not write at all under
`HD-34` — so a product run does not obey it, it is merely subject to what it names. That agrees
with the plan's measurement table.

**`E4` travels**, where the plan's table called it *construction-leaning* rather than deciding.
`document-harness/ONBOARDING.md` cites it for a caller wiring its own hook — *a hook that has
never been seen to block is a hook nobody has tested* — and a rule a product-tier document cites
for a caller's own act is a rule a caller obeys.

**`E10` travels**, where the plan's table counted its eight citations as this instrument's own
rule text. Three grounds, and the first two are in the rule's own bytes:

1. It already addresses a caller directly — *a caller reads its own log there, never the
   instrument's copy of that name under the mount*, and *a caller-held path is named, never
   written as a path token*. A rule that spends sentences telling a caller what to do is a rule
   a caller obeys.
2. Ruling 9 says a caller's declared rule and policy text stays markdown *and subject to the
   layer's amendment discipline*. That discipline is `E10` and nothing else, so a caller obeying
   ruling 9 is obeying `E10`.
3. `E10-sync` binds the membership sentence to `LAYER` and `EXPECTED`, both of which live in
   product-tier code. A sentence that stayed behind would leave a travelling guard mirroring a
   sentence its own reader cannot read — which is the defect `checklist-cited-not-carried`
   records, reproduced rather than closed.

**The move is byte-preserving where it is a move.** A one-shot script cut the source on its rule
boundaries, reassembled both files, applied three named replacements, then re-parsed the outputs
and compared every rule block against the source. It printed `identical` for nineteen of the
twenty-one moved rules and for `E2` in its new home, and `CHANGED` only for `E10` and `R6`. Both
changes are disclosed in commit 2's body in full. The script is not committed.

**Two things the split leaves imperfect, stated rather than softened.**

- `RULES.md` keeps the source's `## Execution side` heading verbatim, whose gloss names *any
  session changing harness code, schemas, or instruction files*. In a file a product run also
  answers to, that gloss is narrow. It is kept because `ORCHESTRATION.md` quotes it word for
  word and widening it would falsify a quotation inside a member; the breadth is stated in the
  header paragraph directly above it. Whether that is enough is the review's to say.
- `RULES.md`'s `R6` now points at *the review-records directory that repository declares*, and
  the declaration it names — `.harness/scan-surfaces.json` — is per-checkout and gitignored, so
  a fresh clone of any repository is running on the shipped default until it runs `dtw init`.
  That hazard predates this round (`caller.py`'s own docstring records it) and this round did
  not widen it, but `R6` now depends on it where before it hard-coded one repository's answer.

## 3. `policy`, proposed and not decided (plan ruling 14, step 5)

**Proposal: `"policy": "CONSTRUCTION-LEDGER.md"`.**

`ORCHESTRATION.md`'s *Reading the caller's policy file* asks for a file saying what this machine
does with a round's conclusions — which ledgers get written, where rulings and unresolved
findings go at closeout, which mechanical checks the caller runs. This repository already has
one, and it is that file's header block: *What may enter* (the current pointer, and
construction-side rulings with no other home), *What does not enter*, where each other kind of
conclusion goes instead (`HARNESS-DECISIONS.md` for a ruling, `HARNESS-RIDERS.md` for an
unresolved finding, the round's review record and commit body for its narrative, the journal for
a ruling's reasons), the `R5` routing rule, the per-entry and per-file caps, and the one
mechanical check that enforces them by name.

The alternative is a new `HARNESS-POLICY.md` holding a second copy of that block, which is `E6`
refused and `HD-5`'s drift surface. `null` was also available and would be false: this
repository has closeout policy, and it is written down.

The user rules on this before the FULL; a changed answer lands as a pre-submission correction.

**Ruled 2026-08-30 — the proposal stands, and this paragraph is the record rather than an edit of
the ones above, which are left word for word (`HD-59`).** Plan ruling 21: the user's word was
「账本」, so `policy` is `CONSTRUCTION-LEDGER.md` — the value already written into `harness.json`
at `cbaee8e`, so nothing in this repository changes on its account and the corrections dispatch
carries no commit for it. The ruling also closes a misreading the question had invited, and says
so rather than leaving it inferable: `policy` is **not** the split's product. The split produced
`document-harness/RULES.md` and left `document-harness/CONSTRUCTION-CHECKLIST.md` as this
repository's `rules`; `policy` is ruling 9's second field, the file `ORCHESTRATION.md`'s *Reading
the caller's policy file* has always asked a caller for, and this repository's answer to it is the
ledger's header block for the reasons stated above.

## 4. The acceptances this round answers, with output

**Acceptance 2 — `python tooling/sweep_refs.py`, both trees.** On this repository at the round's
tip: `13 caller-held or unresolvable references over 10 members and declared rule files` — the
ten being the nine members plus the checklist this repository declares. That is 14 at the round's
base; the one that left is `Document-Work-Assurance-Contract-v3.md`, which went with `HD-67`'s
first block. On a harness-only tree of 59 files, built by copying the product tier and making it
a git repository: **45**, against 48 at the base.

**Acceptance 1 — and it is not zero.** Every remaining non-resolving site on the harness tree
that names an **instrument-held** artifact, with its owner:

| site | artifact | owner |
|---|---|---|
| `RULES.md:87`, `:88` (PATHTOK) + the two `MISSING` members | the two retired-contract stubs | item D, round `CORE-ONLY-CODE` |
| `README.md:16` ×4 | `CONTRACT-V4-SIGNATURE.md`, `N0-record.md`, `W2-record.md`, `supersession-2-signature.md` | **no item of this batch** |
| `README.md:20` (PATHTOK), `:24`, `:26`, `:29` | this instrument's test module, index, a review record, a superseded plan | **no item of this batch** |
| `EXECUTION.md:112`, `:352`, `:377`, `:379`, `:396`, `:402` | `W2-record.md`, `test_readme_enumeration.py`, `run_tests.py` ×2, `validate_fixtures.py`, `retro-2026-08-03.md` | **no item of this batch** |
| `REVIEW.md:90` | `W2-record.md` | **no item of this batch** |

Everything else the sweep prints is the compliant caller-held form and is *reported separately
and still present*, as acceptance 1 requires: the fourteen the plan measured on the full
repository minus the one that left, plus `harness.json` at nine sites (each with its holder in
the same clause), `HARNESS-DECISIONS.md` and `HARNESS-RIDERS.md` — both files `dtw init` writes
into a caller's own root — and `.githooks/`, which every repository wires for itself.

**The gap this round found and did not close.** The rows marked *no item of this batch* are the
plan's own 34-site table, and its *Sketch of the work* assigns them to no item: A is the rule
split, B the membership rule, C the code, D the stubs, E the contract, F the run, G riders, H the
config, I this repository. Acceptance 1 asks for zero and no item reaches them. This is reported
to the orchestrator; it is not fixed here, because a round that widened itself to reach them
would be doing an item nobody wrote.

**Acceptance 5 — `git grep -rn 'CONSTRUCTION-CHECKLIST'` on the harness tree** returns exactly
one line, and it is accounted for:

```
tooling/rsclib/document_harness/dispatch.py:776:CONSTRUCTION_EXECUTOR_CHARTER = "document-harness/CONSTRUCTION-CHECKLIST.md"
```

That constant is item C's, which ruling 13 puts in round `CORE-ONLY-CODE`. As far as the rule
split reaches — the five product-tier role documents and the two READMEs — the answer is zero,
measured in commit 2's body.

**Acceptance 9 — the guards exit 0 and the membership resolves N/N, on both trees.**
`tooling/hooks/layer_path_check.py` exits **0** on this repository and **0** on the harness-only
tree. Membership resolution: **9 of 9** here; **7 of 9** there, the two absent being the stubs,
item D again. So half of this acceptance is met and the other half is round 2's, by the same
cause as acceptance 1's first row.

**Acceptance 10 — rider `checklist-cited-not-carried` deleted in the commit that earned it**:
commit 2, with the redemption measured in that body (0 pointers, 39 rule citations over 31 lines,
every distinct identifier resolving in `RULES.md`).

**Acceptance 11, the guards' half — on the harness-only tree, in a fresh git repository.**
`dtw --help` exit 0. `dtw init --repo-root <fresh>` exit 0, and the `harness.json` it wrote:

```
{
 "policy": null,
 "rules": []
}
```

Then one rule file of the caller's own, `docs/MY-RULES.md`, carrying a backticked path that
resolves nowhere, with the pair run either side of the declaration:

```
-- rules empty (negative control)
   layer_path_check exit=0
   sweep reports on the declared file: none
   sweep tally: -- 9 caller-held or unresolvable references over 9 members and declared rule files
-- rules declares docs/MY-RULES.md
   layer_path_check exit=1  pre-commit BLOCKED: newly added instruction text names a repository path that does not resolve:
   sweep reports on the declared file: ['PATHTOK docs/MY-RULES.md:1  docs/no-such.md']
   sweep tally: -- 10 caller-held or unresolvable references over 10 members and declared rule files
```

**Acceptance 12 — this repository's own `harness.json` declares the checklist and the guard
blocks a dangling path newly written into it, seen red once.** Run twice, and the second run is
the one that means something: at commit 1 the checklist was still a member, so emptying `rules`
did not change the outcome and the red run proved only that the file was scanned. At commit 2,
with the checklist out of `LAYER`, the same staged bytes give exit **1** declared and exit **0**
undeclared. Both runs restored the file by copy from a sha256-checked scratchpad, never
`git checkout --`, and the digest matched on the way back.

**Acceptance 7 — `python -m pytest tooling/tests -q` green on the full repository, delta
accounted.** At the round's last content commit `228df32`: `853 passed in 529.90s (0:08:49)`,
exit 0. The base is 830, which is the figure the plan measured at `ea6485d`, and the delta is
**+23, every one of them new and none of them moved**: 21 in the new
`tooling/tests/document_harness/test_harness_config.py` and 2 added to `test_init_command.py`,
both in commit 1. Commits 2 and 3 have a delta of zero — the split moved rules and the two test
constants that name a member moved inside the same commit, and the contract commit changes no
test at all. The figure was 853 at commit 1, 853 at commit 2 and 853 here.

### Re-measured after the corrections dispatch — written forward, the block above left word for word (`HD-59`)

Every figure below was taken at `322fd1c`, the corrections dispatch's last content commit, by the
same two instruments and the same two trees as the block above. The harness-only tree is `git
archive HEAD` over the product-tier paths into a fresh git repository: **59 files**, the same 59.
Nothing between that commit and this journal changes what any of them measures — this file is
neither an instruction-layer member nor a declared rule file, so no sweep and no guard reads it,
and no test enumerates `document-harness/journal/`.

**Acceptance 2 — `python tooling/sweep_refs.py`, both trees.** On this repository:
`13 caller-held or unresolvable references over 10 members and declared rule files`, unchanged
from the block above and unchanged by all three corrections commits, because every name deleted
from a product-tier document resolves here and neither the wikilink nor the deleted contract
paragraph was a form the sweep can see. On the harness-only tree: **33**, against 45 in the block
above and 48 at the round's base. The twelve that left are item J's twelve sweep hits over nine
sites.

**Acceptance 1 — closer, and still not zero.** Every remaining non-resolving site on the harness
tree that names an **instrument-held** artifact, with its owner:

| site | artifact | owner |
|---|---|---|
| `RULES.md:87`, `:88` (PATHTOK) + the two `MISSING` members | the two retired-contract stubs | item D, round `CORE-ONLY-CODE` |
| `EXECUTION.md:375`, `:377`, `:394` | `run_tests.py` ×2, `validate_fixtures.py` | **contested — the classification above is wrong, and the correction goes to the orchestrator** |

The second row is this dispatch's own finding against the block above. Those three sites were
listed there as instrument-held and became three of plan ruling 24's twelve; measurement says they
are not. The paragraph they sit in states in its own words that the five battery commands are
*named here rather than written as paths (`E10`) because their scripts live in the caller's tree*,
and then warns that *a name here may also belong to an unrelated file in this repository, so a
caller identifies each command by its battery leg inside its own tree and never by name-matching
against this one* — which is exactly what happened: `git ls-files` matches
`tooling/tests/document_harness/run_tests.py`, `tooling/tests/document_harness_review/run_tests.py`
and `migration/document-work-assurance-v3/N0/fixtures/validate_fixtures.py`, none of them the file
the sentence means, and the sweep resolves the name against basenames because a bare name has no
directory to resolve from. Deleting two of them would strike two of five entries from an
enumeration whose own text reads *Five commands, and nothing fewer* and which `HD-42` guards, which
is a change to what a rule requires and therefore design; the third is a past-tense sentence about
two caller-side runners whose trees `HD-39` deleted, the same deliberate-history class plan ruling
19 disposed of by keeping the name. So nine of the twelve are carried out and three are reported;
the reasoning is in `b235701`'s body site by site.

Everything else the sweep prints on that tree is the compliant caller-held form, *reported
separately and still present*: the caller's own run artifacts, `harness.json` at nine sites,
`HARNESS-DECISIONS.md` and `HARNESS-RIDERS.md` — both files `dtw init` writes into a caller's own
root — `.githooks/`, which every repository wires for itself, and the contract's past-tense
`review.schema.json` under plan ruling 19.

**Acceptance 5 — unchanged.** `git grep -rn 'CONSTRUCTION-CHECKLIST'` on the harness tree still
returns exactly the one accounted-for line,
`tooling/rsclib/document_harness/dispatch.py:776`, which is item C's in round `CORE-ONLY-CODE`.

**Acceptance 7 — `python -m pytest tests -q` run from `tooling`, on the full repository, at
`322fd1c`: `853 passed in 157.17s`, exit 0.** The delta across all three corrections commits is
**zero**: the figure was 853 at the block above's last content commit and is 853 here. Nothing in
this dispatch adds, removes or edits a test — the sites it changed are prose that no test reads,
and the two modules that do read a member (`test_readme_enumeration.py`, which pins schema stems
in `document-harness/README.md`, and the layer-path mirror's `EXPECTED`) are untouched and stay
green with the edited bytes.

**Acceptance 9 — the guards exit 0 and the membership resolves N/N, on both trees.**
`tooling/hooks/layer_path_check.py` exits **0** on this repository and **0** on the harness-only
tree with a clean index. Membership resolution: **9 of 9** here; **7 of 9** there, the two absent
being the stubs, item D again — unchanged from the block above, because this dispatch neither adds
nor removes a member. One measurement worth recording beside it, taken because the number differs
by method and a reader re-running this will meet it: with the whole harness-only tree staged as new
(`git add -A` in the fresh repository, before any commit), the guard reads every line as an added
line and exits **1**, naming three path tokens — `RULES.md`'s two stub paths and
`README.md`'s `.githooks/`. All three predate this round, none is this dispatch's, and the first
two are item D's; it is recorded because the ordinary caller act of committing a first checkout is
exactly the state that produces it.

## 5. Every guard change, seen red once, with its control (`E4`)

| mutation | must fire | control that stays green |
|---|---|---|
| `scanned_paths` returns `LAYER` alone | declared rule joins the surface · guard blocks in a declared file · sweep reports it — 3 red | the other 18, including both *undeclared is not blocked / not swept* controls |
| `load_harness_config` returns the defaults on malformed input | unparseable JSON · a JSON array · the guard stopping rather than emptying — 3 red | 18 green |
| `init_target`'s config write deleted | the empty-config bytes · the never-overwrite case · nothing-else-is-written — 3 red | 22 green |
| `RULES.md` dropped from `LAYER` while the sentence still says nine | `LayerMembership`'s two — 2 red | the same two green on the unmutated file, before and after, same sha256 |

Restores were copies from sha256-checked scratchpad files in every case.

## 6. Riders

**Redeemed and deleted:** `checklist-cited-not-carried` (commit 2), `readme-common-clause`
(commit 2), `index-repo-count` (commit 2), `sig-write-once` (commit 3, on its
record-rather-than-restore arm). **Redeemed on one arm, row kept for the other:**
`onboarding-carries-construction` — arm (b), the three journal path tokens de-named, in commit 1;
arm (a), the four Owner cells, needs a clause added to a rule and is not in this round's
authorisation.

**Touched, not redeemed, each with its reason in the row:** `E10-sync` (a per-touch check by its
own text, discharged), `e9-pair-budget`, `e10-cannot-see`, `e10-freeze-exception`, `wl-route`,
`hd38-both-ways`, `read-name-split`, `r9-terminal-no-carrier`, `announced-set-anchor`,
`figure-units`, `contract-wikilink-tier`. Every one of those fixes adds or removes a bound, which
is design; this round is a design round but its authorisation is the plan's rulings and `HD-67`,
and none of them reaches these.

**`r9-terminal-no-carrier` is the one worth reading twice.** The opening read's `O-5` measured
`document-harness/README.md`'s "added as the tenth member 2026-08-18" stale for a fifth cycle and
deliberately routed it to that row rather than through `R9`'s terminal branch again — the branch
that lost it four times. This round touched the file, so the sentence is fixed: the date stays,
the ordinal goes, and what replaced it says how many members there are is `E10`'s sentence to say
and it reads nine. The row is **not** redeemed, because one instance being fixed does not give
`R9`'s terminal branch a carrier.

**Not due, decided explicitly:** `charter-qualifiers`, `e1-table` and `e1-reader` name
`ORCHESTRATION.md`'s two tables and this round edits that file outside both; `pin-drift`,
`template-clause-unguarded`, `itemh-sweep-count`, `itemg-linecount-file`, `alarm-mutation-gaps`,
`alarm-yaml-range-untested`, `archive-header-selfcount`, `freeze-audit`, `argv-cap`,
`delta-prose`, `RA` and `PD` name surfaces this round does not touch.

The opening read's `O-6` is settled by not settling it: `test_readme_enumeration.py`'s docstring
says the fourteen delimited stems sit in three enumeration rows where there are four. This round
does not touch that module — the split moved no test that reads the README — so under `E8`'s
change boundary the fix does not ride a commit here, and it is reported rather than banked, since
a rider row for a docstring count with no nameable downstream decision is `R9`'s terminal branch,
which is the exact defect `r9-terminal-no-carrier` is open about.

## 7. Four things that go to the orchestrator, not decided here

1. **`HD-67`'s named block against `HD-67`'s stated criterion, in §12.** The entry names §12's
   first two paragraphs by content and by line range; its boundary paragraph says the judge is
   whether a passage is caller-reachable and whether it imposes an obligation, and that a
   sentence with obligation effect is out of range. ¶1's first two sentences impose one — old
   directories default to historical-only, and referencing a non-nominated old component is a
   `SPEC_GAP`. They are **kept**, because removing an obligation is the irreversible direction.
   The cost of keeping them is stated plainly: the surviving requirement names a set — *the
   nominated components* — that the paragraph defining it took with it, so it now points at a
   list its reader cannot enumerate. Which of the two readings governs is the user's.

   **Answered 2026-08-30 (plan ruling 22), written forward; the paragraph above stands word for
   word (`HD-59`).** The user ruled the other way: §12's first paragraph goes **entire**, the two
   obligation sentences included, and the ground is that v4 depends on no v1/v2 component, so
   nothing about them is referenced and all of it goes — verified before the ruling was taken, the
   contract's remaining v1/v2 mentions being §13's version-boundary statements about results and
   history rather than dependencies. `HD-67`'s named block therefore governs over an executor's
   reading of `HD-67`'s criterion, for this block. Carried out at `322fd1c` as a pre-submission
   correction, with the `E2` disclosure in that body and `CONTRACT-V4-SIGNATURE.md`'s sixth
   post-signature write in the same commit; §12 is now its *Removed from the v3 default interface*
   paragraph and nothing else. **Two residues this executor found and did not touch, reported
   rather than fixed.** §12's heading still reads *Dependency and historical map (plan §7)* over a
   section holding no dependency map — signed contract text that no ruling in force reaches, since
   `HD-67`'s boundary names two blocks and ruling 22 names one paragraph. And the class scan
   `HD-41` ④ owes (`grep -rn 'historical-only\|non-nominated\|nominated old component'` over the
   product tier) returns two survivors: `document-harness/README.md:30`, now the last statement of
   the historical-only default in any product-tier document, citing the N0 record descriptively
   rather than by filename so no sweep sees it and ruling 24's site list does not reach it; and
   `tooling/rsclib/document_harness/__init__.py:12`, a docstring citing the same record for the
   same default. Both are outside every ruling in force.
2. **Rider `contract-wikilink-tier` needs a fourth ruling in the `HD-63` / `HD-64` / `HD-67`
   family.** Its arm and its deadline both arrived with commit 3. Its fix is an in-place edit of
   signed contract text, §13 still forbids that, and each of the three existing overrides covers
   only its own class. `E2` ceasing to be a gate on 2026-08-27 changed what `E2` requires, not
   what §13 forbids.

   **Answered 2026-08-30 — the fourth ruling exists: `HD-68`** (plan ruling 23), written forward;
   the paragraph above stands word for word (`HD-59`). It states in as many words that it overrides
   §13, and what it covers is the class the three before it left uncovered: a **reference form**
   that is followable but reaches bytes no caller holds and gives neither a path nor a holder.
   Carried out at `322fd1c`: the plan is named by its title and given no link and no path, the dead
   digest parenthetical is deleted as history, and the locked-authority sentence is kept word for
   word. Rider `contract-wikilink-tier` is redeemed and its row deleted in that same commit, as
   `R10` requires — 28 rider rows at its parent, 27 after. The changed text owes `E10`'s independent
   re-read, riding this round's next read of that layer.
3. **The sites acceptance 1 asks for and no item of this batch owns** — §4's table above.

   **Answered 2026-08-30 (plan ruling 24, item J), written forward; the line above stands word for
   word (`HD-59`).** The user's disposal is deletion, not de-naming, and never a name replaced by a
   holder clause; where a sentence cannot stand without the reference, the sentence is rewritten
   without it. Nine of the twelve sites are carried out at `b235701` — five in
   `document-harness/README.md`, three in `document-harness/EXECUTION.md`, one in
   `document-harness/REVIEW.md`, each named in that body with what it now says. Three are **not**,
   and go back to the orchestrator with the measurement: `EXECUTION.md:375`, `:377` and `:394` name
   caller-held commands and caller-side history, not instrument-held artifacts, so the ruling's
   premise fails at them and carrying them out would strike two entries from an enumeration `HD-42`
   guards. §4's re-measured block above holds the evidence. Acceptance 1 therefore reaches item D's
   four sites plus those three, rather than item D's four alone.
4. **`RULES.md`'s `## Execution side` gloss** — §2's second bullet.

   **Left to the FULL 2026-08-30 (plan ruling 24's closing sentence), written forward; the line
   above stands word for word (`HD-59`).** The user's ground: it is wording, and no actor's action
   changes today. This dispatch touched neither the heading nor the header paragraph above it.

## 8. Ceilings

- **Not run:** any `dtw dispatch` mode, in any tree. This round changes no dispatch behaviour,
  and the round's own dispatch is the orchestrator's.
- **Not run:** a product run. That is item F, round `CORE-ONLY-RUN`, and acceptance 3 and 4 are
  not this round's.
- **The harness-only tree was built two ways and they agree**, which is why the intermediate
  measurements taken by copy are reported beside the ones acceptance 1 asks for. `git archive`
  at `db1bfa1` over the product-tier paths gave 58 files and **48**, reproducing the plan's own
  figure exactly; `git archive HEAD` over the same paths plus `RULES.md` gives 59 files and
  **45**, identical to the copy of those paths into a fresh git repository, which is the method
  used mid-round while commits were still unstaged. The guard exits 0 on both.
- **Every count in this file is invalidated by the commit that carries it**, this journal
  included (`E3`). The commands are printed so they can be re-run.
