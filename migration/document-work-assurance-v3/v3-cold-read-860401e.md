# Instruction-layer read — subject `860401e16d21d1792ee75e94268d391eedfbda5f`

An `E10` read. Not a round: no budget spent, no verdict carried, output is findings tiered
must-fix / low / observation (`R3`). Dispatched with the charter
`migration/document-work-assurance-v3/v3-harness-review-contract.md`, which is a stub —
its operative successor `document-harness/CONSTRUCTION-CHECKLIST.md` was read in full as
both the standing instruction and its own counterpart, per that file's own opening.

Record name: `v3-cold-read-`. `R6` offers two read filenames and the layer defines no
criterion for choosing between them — that gap is banked as rider `read-name-split` and I
am not closing it here. I took `cold-read` because the subject is the whole layer at a
commit that opens a batch (`860401e`'s own body records batch `FREEZE-TO-ALARM`'s four
gating questions as answered with no round open), which is the shape `E10` calls a round's
opening cold read.

## 1. The member set, derived — not received

The dispatch enumerated nothing; `E10`'s own sentence at the subject does. Read there, the
layer is **exactly nine paths**, and all nine resolve at the subject commit. Blob ids are
`git rev-parse 860401e:<path>`, run here:

| # | member | blob at `860401e` |
|---|---|---|
| 1 | `document-harness/CONSTRUCTION-CHECKLIST.md` | `fce40914cb9c9cfd16a59dd2b6f8f9167656e274` |
| 2 | `document-harness/README.md` | `0a4da19b0d522d307997f681d5dec333b9349486` |
| 3 | `document-harness/EXECUTION.md` | `234fdddf974e580d22a1a26b54587d11c24863b3` |
| 4 | `document-harness/REVIEW.md` | `aad3dd83643a4656aa239e97afec8edb691228a6` |
| 5 | `document-harness/ORCHESTRATION.md` | `a9e9f75e484f40f4a1014e5d68ed6c73aa5fbdc2` |
| 6 | `migration/document-work-assurance-v3/v3-harness-operating-contract.md` | `6d5714923870b4e13e8928221a80df68e563a5ed` |
| 7 | `migration/document-work-assurance-v3/v3-harness-review-contract.md` | `29bdc9fbde6e8db38d601dd2340d4b46a24a296f` |
| 8 | `contract/Document-Work-Assurance-Contract-v4.md` | `5dfb7b64265c821c715f23de52824beeadea3405` |
| 9 | `schema/document-assurance-v3/paragraph-map.schema.json` | `09aa869962f592c2f86c9379be0ef3eb7d2232ff` |

`HEAD` is the subject and `git status --porcelain` reports one untracked path (`.goals/`)
and no modified tracked file, so the worktree bytes I read are these blobs.

**What moved since the last recorded end-to-end read.** The most recent one is
`v3-cold-read-b737742.md` (record commit `7135cd2`). `git diff --stat b737742 860401e --`
over the nine returns one file:

```
 document-harness/REVIEW.md | 14 +++++++++-----
 1 file changed, 9 insertions(+), 5 deletions(-)
```

Two hunks, both read as accurate corrections and neither carrying a defect I can name: the
stale `history/REVIEW-v1-package-flow.md` markdown link is replaced by prose saying the
package-bound sections are gone (that file is indeed absent from `git ls-files` at the
subject), and the record-channel paragraph is re-pointed from a hard-coded caller directory
to "the caller's own review-records directory". The second is corroborated outside the layer:
`tooling/rsclib/document_harness/caller.py:71` carries
`DEFAULT_REVIEW_RECORD_DIRS = ("assurance/review-records/",)` beside
`DEFAULT_SPECIFICATION_SURFACE = ("assurance/runs/",)` — "inside the caller's assurance tree,
beside its runs tree" is literally true — and the declaration file the sentence calls a
"scan-surface declaration" is `.harness/scan-surfaces.json`, loaded by
`caller.load_scan_surfaces`.

I did **not** rely on the `b737742` citation channel. All nine members were read end to end
in this session regardless of whether their blobs moved.

## 2. Findings

### must-fix

**`M-1` — `CONSTRUCTION-CHECKLIST.md:17` sends every unresolvable commit id to a section of
the root README that does not exist.**

*Location.* `document-harness/CONSTRUCTION-CHECKLIST.md:14-22`, the *Where a cited commit id
resolves* block:

> A commit id cited in this file or in any other instruction-layer member (`E10`) that this
> repository does not have — `7011916` included — is a commit of the repository this one was
> extracted from; the root [`README.md`](../README.md)'s *Where the bytes came from* names
> that repository and says why the history stayed there.

*What is false.* The root `README.md` at the subject carries no such section. `git grep -n -i
"bytes came from" 860401e` returns ten hits and **not one of them is in `README.md`**; the
only two live carriers of that heading are `CONSTRUCTION-LEDGER.md:32` and this very sentence.
The path token itself resolves — `../README.md` exists — so the whole failure is in the part
`layer_path_check` structurally cannot see. Nothing in the guard reads headings.

*When it broke, and how long it has stood.* The section existed and was checked repeatedly:
`v3-cold-read-cf54a79.md:219`, `-39e395e.md:343`, `-693b692.md:203`, `-dd22789.md:288`,
`-3a6a10b.md:191` and `v3-checkpoint-read-48b6c5f.md:142` each record verifying it at
`README.md:12`/`:14`. Commit `2522ce1` (2026-08-24, `README-BILINGUAL-v1`) rewrote the root
README and deleted it, saying so in its own body — *"Extraction/provenance narrative
(first-commit byte lineage, caller history) is no longer retold here"* — without touching the
member that points at it. `git merge-base --is-ancestor 2522ce1 <sha>` puts `2522ce1` inside
the history of `ff4b749`, `d3ba221` and `b737742`, so **three recorded end-to-end reads have
run over the broken pointer and none reported it.**

*The ground truth it violates.* `E3`: a factual assertion written into instruction text runs
the command that could falsify it first. `E10`: a member's pointers must not land a reader
"on another repository's bytes or on nothing" — the clause states that principle for path
tokens, and this is the same failure one level down, at the heading.

*The downstream obligation that cannot be discharged.* Not cosmetic, which is why I am not
tiering this wording-level. The block immediately above it makes `7011916` load-bearing: where
this checklist is silent on a question a round actually faces, "the retired contracts at
`7011916` are the reference of record." `7011916` does not resolve here (`git cat-file -t
7011916` → `fatal: Not a valid object name`), by design — the rule exists to tell the reader
which repository does have it, and the only place it names for that answer is gone. A round
meeting a silence is therefore told to consult a reference it has no route to. That is an
obligation the header creates and the layer can no longer satisfy, which is `R9`'s
"no obligation" clause and puts this outside the banked tier.

*Minimum fix.* One sentence; two admissible forms, and the executor picks:

- **(a) re-point the terminus** at the record that does carry that heading —
  `CONSTRUCTION-LEDGER.md`'s own *Where the bytes came from* block, which names the caller
  the entries were moved out of. Smaller diff, and it keeps a construction-side rule pointing
  at a construction-side record, which is what `CONSTRUCTION-CHECKLIST.md` is. Caveat worth
  stating rather than hiding: that terminus names a single-machine path, so it identifies the
  source repository without making it reachable — `document-harness/plans/stranger-guards.plan.md:93`
  had already scheduled that same terminus to gain a reachable name and is itself stranded by
  the deletion.
- **(b) restore a *Where the bytes came from* section** to the root README.

Either way this is an `E10` **amendment**, not design: the routing test in the first sentence
is unchanged, no clause is added to any rule, and nothing a rule requires changes — only the
terminus is corrected. So it takes the must-fix channel (amendment commit plus an independent
re-read of the amended text, which `E10` says is not a round and spends no budget), and it does
not touch a path `E2` freezes.

### low

**`L-1` — contract v4 §5's "single home: common.schema.json" is not true of four of its own
rows.** `contract/Document-Work-Assurance-Contract-v4.md:124` heads the closed-enum table
*"Closed enums (single home: common.schema.json)"*, and annotates the two review-verdict rows
with "(schema at N2)" — so the table does mark rows whose machine home is elsewhere. The four
per-phase decision rows carry no such mark, but their enums are not in that file. Measured at
the subject: `git grep -c '"enum"' 860401e -- schema/document-assurance-v3/common.schema.json`
returns **6**, and those six are `checkKind`, `verificationMode`, `assuranceStatus`,
`auditResult`, `auditFindingKind` and `decisionPhase`. `START · REPLAN`,
`APPLY_ACCEPTED_FINDINGS · NO_REPAIR`, the four FINAL decisions and the six ISSUE_TRIAGE
decisions all live in `schema/document-assurance-v3/user-decision.schema.json:55,64,73,83`.
A grep for those literals in `common.schema.json` returns nothing.

The values themselves are right — I compared all twelve rows against the schemas and every
one matches, including the `local_check · review_only` row `HD-57` corrected. What is wrong
is the locational claim. The decision it can send astray: someone amending a decision enum
under the contract's "single home" instruction edits `common.schema.json`, where the enum is
absent, and believes it landed. That is bounded by the freeze — those bytes are `E2` — but the
contract is the document that says where to look, and here it says wrong.

**Routing is forced and is not mine to choose.** These bytes sit on a path `E2` freezes, so
`R10`'s override applies (`HD-20`): the finding banks until a contract-v4 `E2` write ruling
exists, however appliable it is. Both authorisations that could have carried it (`HD-60`,
`HD-61`) are one-shot and were `retired` at `a554c0b`. Same redemption arm as riders
`sig-write-once` and `contract-wikilink-tier` — the next round holding a contract-v4 `E2`
write ruling, one write window collecting all three. **Deadline:** the next contract-v4 `E2`
write window or the next re-signature, whichever arrives first — shared with those two rows
and, per `HD-37` ①, outside the round that files this.

### observation

**`O-1` — the "tenth member" ordinal is still at `document-harness/README.md:22`, one full
touch cycle after being routed away.** The Role-instructions row still reads "added as the
tenth member 2026-08-18" while `E10` fixes nine. The statement is *historically* true as
dated — `HD-46` did admit `ORCHESTRATION.md` as the tenth, and the two contract supersessions
left the layer afterwards — and `E10`'s sentence is the only authority on the count, so no
reader is misled about membership. I record it only because it is the exact instance rider
`r9-terminal-no-carrier` was written about: the previous read routed it under `R9`'s terminal
branch, round 2 touched that member (`07ef526` changed `:16`), and the byte went unchanged and
unrecorded anywhere. It is still there at the subject. Nothing new to bank; the rider holds it.

**`O-2` — `E10`'s "what the guard still cannot see" list is short by the class this read's own
must-fix belongs to.** The clause enumerates four blind spots — placeholder segments, prose and
markdown links, the `++ ` diff-header ambiguity, and unre-scanned standing text. A pointer to a
**heading** in another file is a fifth: the path resolves, the guard passes it, and nothing
anywhere checks the heading. `M-1` is a live instance and it survived three reads. Rider
`e10-cannot-see` already records that this same list is short by two path-shape classes (no
extension, and outside the seven-extension whitelist — both confirmed here by reading
`PATHLIKE` at `tooling/hooks/layer_path_check.py:50`), so the fix surface is one that already
has a bank row. I supply no bytes: adding an item to that enumeration is on the surface `E10`'s
design test governs, exactly as that rider says.

**`O-3` — `dispatch.py` cites a `REVIEW.md` section that no longer exists.** The rendering
commentary at `tooling/rsclib/document_harness/dispatch.py:399-401` cites "`REVIEW.md`'s *What
you are given: a floor, never a ceiling*". `REVIEW.md` at the subject carries no heading of
that name; the surviving carrier is the sentence "The floor-versus-ceiling rule is unchanged"
inside *When the subject is one commit*. Outside the layer and therefore outside what I may
conclude about (`R5`), but the same class as `M-1` pointing the other way — non-member code
citing a member's heading — and cheap to fix on the next batch touching that module.

## 3. What I checked that held

Recorded because a read that reports only failures leaves the next reader unable to tell
checked-and-clean from never-looked-at.

- **Membership, three copies.** `E10`'s nine equal `LAYER` in
  `tooling/hooks/layer_path_check.py:37-47` and equal the hand-written `EXPECTED` tuple in
  `tooling/tests/document_harness/test_precommit_checks.py:229-239`, which is `E5`-shaped —
  a literal list, asserted whole, never read back from the module. `document-harness/README.md`'s
  own claim that the nine are hard-coded in exactly those three places is true at the subject.
- **`E2`'s frozen list, both halves.** `git rev-parse 860401e:contract/Document-Work-Assurance-Contract-v4.md`
  is `5dfb7b64265c821c715f23de52824beeadea3405`, matching the clause's literal. The pack holds
  exactly fifteen `*.schema.json` files. The two rulings `E2` cites for the move off
  `dfc983d2…` are real: `HD-60` and `HD-61` are in `HARNESS-DECISIONS-archive.md:28,59`
  (consumed and `retired`, which does not unmake the record). The signed blob `614932de…` is
  the object `CONTRACT-V4-SIGNATURE.md:8` binds, and that record does say it succeeded `HD-56`.
- **The commit-id routing rule's own inputs.** `7011916` and `6fd0ae3` and `ac1b383` are not
  objects here, so they route outward as the header says; `0d73a5f`, labelled *instrument* in
  `EXECUTION.md`, is a commit here, so it routes inward. The rule's premises are consistent —
  only its terminus is broken (`M-1`).
- **The review-contract stub's three claims.**
  `dispatch.CONSTRUCTION_ROLE_INSTRUCTION` at `dispatch.py:548-550` is that stub's path;
  `test_dispatch.py`'s `CHARTER_OUTSIDE` (`:398`, `:522`) and `MEMBER` (`:463`) are hand-written
  literals carrying it, docstring-marked `E5`; and
  `tooling/tests/fixtures/expected-construction-prompt.txt` carries `{charter}` as a
  substitution rather than the path.
- **`EXECUTION.md`'s doc-paths-pinned-by-code list.** All five sites exist and pin what the
  clause says: `test_readme_enumeration.py:36` opens `document-harness/README.md` by path;
  `layer_path_check.py` mirrors the member paths; `document-harness/templates/` holds exactly
  two files, which `init_target.py:17` names as the shipped instance templates; and
  `tooling/rsclib/document_harness/__init__.py:41` sets `CONTRACT_PATH` to the v4 contract.
- **`E10`'s three mechanical claims about the guard, read against the code.** `.harness/` is
  exempt (`RUNTIME_PREFIX`, `:53`); escaping resolution counts as nowhere
  (`is_relative_to(root)`, `:70`); and the `++ ` diff-header ambiguity is exactly as described
  — an added line whose content opens `++ b/…` re-targets `current` and mis-files what follows,
  any other `++ …` sets `current = None` and silences it (`:104-109`). The clause's parenthetical
  is a correct reading of that parser, not an approximation.
- **Every path token and markdown link in all nine members, standing text included** — the
  sweep the guard never performs, since it scans only added lines. Extraction was
  `` `…/…` `` tokens plus `](…)` targets, per member, resolved from both the repo root and the
  member's own directory. **Everything resolves.** Two tokens are deliberately non-literal and
  I am not calling either a defect: the brace form
  `` `../migration/document-work-assurance-v3/v3-harness-{operating,review}-contract.md` ``
  and the glob `` `../migration/document-work-assurance-v3/v3-*.md` ``, both in the checklist
  header, both expanding onto files that exist.
- **Cross-member heading pointers.** Four of the five inside the layer land:
  `EXECUTION.md:454` → `ORCHESTRATION.md`'s *Handing the executor its instruction*;
  `ORCHESTRATION.md:7` and `:39` → the checklist's *Execution side* heading;
  `ORCHESTRATION.md:81` → `EXECUTION.md`'s *Instruction authoring rules*. The fifth is `M-1`.
- **Contract v4 §5 against the schemas.** All twelve rows' values match
  `common.schema.json`, `user-decision.schema.json`, `review.schema.json` and
  `review.v2.schema.json`. Only the locational heading is wrong (`L-1`).
- **Internal counts.** `ORCHESTRATION.md`'s "nine obligations that are already law elsewhere"
  table has nine rows, and with its three own-text obligations makes the twelve
  `document-harness/README.md:22` claims for it.
- **Boundary check on the subject commit itself.** Its body says no round is open and no work
  item has been executed; `.github/workflows/ci.yml` at the subject carries one `test` job and
  no alarm job, consistent with that.

## 4. Coverage and ceilings (`R4`)

- **Read in full:** all nine members, at the blobs tabulated above; `HARNESS-DECISIONS.md`
  `§live` in full (`HD-59`, `HD-44`, `HD-41`, `HD-36`, `HD-35`, `HD-34`, `HD-23`, `HD-9`),
  which `E10` owes at a round's opening whether or not the layer read is waived and which is
  the file at *this* repository's root, not an instrument copy under a mount;
  `HARNESS-RIDERS.md` in full, to route rather than duplicate; `layer_path_check.py`,
  `.githooks/pre-commit`, `dispatch.py`, `test_readme_enumeration.py` in full.
- **Sampled:** `HARNESS-DECISIONS.md` `§implemented` (read to `HD-32`, not to the end of the
  641-line file); `HARNESS-DECISIONS-archive.md` by grep only; `caller.py`,
  `assurance_state.py`, `instruction.py`, `test_precommit_checks.py`, `test_dispatch.py`,
  `init_target.py`, `__init__.py` by targeted grep around the claim under test, never end to end.
- **Probed only:** the run-template scripts under `assurance/templates/run-v2/`; the frozen
  schema pack beyond `common`, `user-decision`, `review`, `review.v2` and `paragraph-map`.
- **Not run: the test suite.** `python -m pytest -q` was refused by this environment's
  permission layer, twice. So every statement above about the tests is a statement about the
  **text** of the tests as I read it, not about their passing here, and I am not folding an
  unrun command into a supported claim (`R4`). Nothing in this record depends on a pass —
  `M-1` and `L-1` are both established by `git grep` and `git cat-file` output.
- **No mutation testing.** `R8` asks for it where guards matter, and I did not do it: it needs
  writes to guarded files, and `E4`'s neuter-and-restore protocol is an executor-side procedure,
  not a read-side one. The `E5` shape of the membership pin is asserted from reading the
  literal, not from watching it fail. `E10-sync`'s standing finding — that the **prose** leg of
  the membership sentence has no guard at all and a deleted path leaves everything green —
  I did not re-demonstrate; I re-confirmed by reading that no test asserts against the prose.
- **Process claims are marked, not verified.** That this read ran in a fresh context is a
  process claim with no evidence lock. What is checkable is in the record: `M-1` reproduces
  from `git grep -n -i "bytes came from" 860401e`, `L-1` from
  `git grep -c '"enum"' 860401e -- schema/document-assurance-v3/common.schema.json`.
- **`R2` compliance.** The member set came from `E10`'s own sentence at the subject, every
  blob id from `git rev-parse` run here, every count from a command re-run here, and no figure
  was taken from the dispatch, the commit body, a plan, or a prior record. Where I cite a prior
  read it is as evidence that a check *was made then*, never as the value.
- **Chat-only load-bearing material: none found**, and none introduced. One note in passing:
  `.goals/` is untracked at the subject and holds copies of two plans that also exist tracked
  under `document-harness/plans/`. It is outside the layer and outside the subject; I read the
  tracked copies, not those.
