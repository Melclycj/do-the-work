# FULL review — `17e2b65..af2905c` (instruction-layer amendment round: E10 deferral + E10 convergence + E2 narrowing)

**Verdict: `CHANGES_REQUIRED` — 2 blockers, 5 non-blocking findings, 6 observations.**

---

## 1. What this round is, re-derived

Nothing below was taken from the dispatch, which carried only the range.

```
$ git log --oneline 17e2b65..af2905c
af2905c V3-E10-E2-AMENDMENT-v1
6618b84 V3-ORDERING-RULING-CONVERGE-CHAIN-FIRST-v1

$ git diff --name-status 17e2b65..af2905c
M	.goals/plans/harness-digest-narrowing.plan.md
M	ResearchSystem/HARNESS-LEDGER.md
M	ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md

$ git rev-parse HEAD
af2905c3fe3d2da2918016f5731da8b35996036d

$ git status --porcelain
?? ResearchSystem/docs/
```

**Path classification, done by hand (R2).** Three files, zero code, zero schema, zero test,
zero fixture. `CONSTRUCTION-CHECKLIST.md` is instruction layer by E10's own first sentence.
`HARNESS-LEDGER.md` is the live control-plane pointer. `harness-digest-narrowing.plan.md` is
a closed plan's resume pointer. The untracked `ResearchSystem/docs/` holds one file
(`General-Harness-v2-Design.md`, mtime 2026-07-19), predates the range, and is unstaged.

**Which round, and its budget.** The round is the instruction-layer amendment round the
2026-07-29 ordering ruling promoted ahead of Phase C1.7 (`HARNESS-LEDGER.md:85-94`, `95-106`).
`af2905c` names itself *"Candidate for the instruction-layer amendment round"* and claims to
consume nothing on the ground that no independent FULL has occurred; that is E9's own test
applied correctly — I find no earlier FULL on these bytes in `git log`, so `6618b84` and
`af2905c` are both pre-submission and **this review is the round's one FULL**. Fix and VERIFY
are untouched.

**This FULL is not the read E10 owes on these bytes.** E10: an amendment's independent read
*"is never banked as the round's FULL"*. `af2905c` states the same about itself. The read
remains owed and its subject is the amended `CONSTRUCTION-CHECKLIST.md` text, not this round's
work. My verdict below discharges the round's review; it discharges nothing of E10.

**How I know this is a FULL and not that read.** The prompt I received is byte-for-byte
`CONSTRUCTION_PROMPT` from `rsclib/document_harness/dispatch.py:498-511` — the construction
*round* dispatch, whose subject is a `base..tip` range. The precedent read dispatch
(`v3-dispatch-supersession-2-read.md`) is a hand-written file naming a blob, because E10 scopes
a read to a text. My subject is a range spanning a ruling commit that touches no
instruction-layer byte, which no read's subject could contain.

**What the work was obliged to do.** Three items, merged by the user's ordering ruling into one
edit of one file (`HARNESS-LEDGER.md:85-94`): ① an E10 deferral clause for the amendment-read,
resting on the size argument behind two recorded overrides; ② an E10 convergence clause
answering whether an UNSIGNED successor revised before first reliance must repeat a round per
revision; ③ the banked E2 narrowing (VERIFY-② / `v3-review-verify-293f657.md` V-b).

**Authorization ceiling (R7).** The user rulings this round rests on — *"the user ruled deferral
acceptable"*, the ordering ruling, the three-item scope, and the E11 preview card — exist in the
repository only as the execution side's own ledger and commit-body records. I take them at face
value and do not treat them as verified. Item ② in particular is recorded as a *question* put in
scope; the answer in the text is the executor's draft, and only the user's signature settles it.

---

## 2. Implementation (R3 — lead)

The payload is three clauses that will be acted on. I judge them as instructions, not as prose.

### 2.1 The E2 narrowing — right against its source, wrong in the enumeration that scopes it

The source rule, read directly rather than accepted from the round:

```
$ git show 7011916:…/v3-harness-operating-contract.md   (hard rule 5, line 174-176)
5. **Signed bytes are untouchable** (approved plan, contracts, N0 schemas incl.
   `common.schema.json`). When the *cleanest* fix needs one, that is an out-of-boundary write in
   better clothes: take the in-boundary fix and record why, or stop with `SPEC_GAP`.
```

The round's central claim — that rule 5 froze signed bytes **by category and never by
directory** — holds verbatim. The compressed E2 had widened it to a path, and V-b named the
downstream decision that goes wrong. The new text (`CONSTRUCTION-CHECKLIST.md:23-30`) restores
the category basis, cites the source, and routes an unsigned successor to E10's read path. That
is the right shape and it pays the banked item.

**But the round then enumerates what the path holds, and the enumeration is false.**
`HARNESS-LEDGER.md:91-92` and the `af2905c` body both state that `contract/` also holds
`adapter-map.md`, `block-grammar.md`, `content-roots.yaml`, `baseline/` and `amendments/`,
*"none of them signed contracts"*. See **Blocker B-2**: one of those is signed by the user, with
a digest recorded in the main contract, and its bytes still hash to it.

**Verified clean around it.** The other named files check out as unsigned:
`amendments/2026-07-17-projection-v2.md` opens *"ABANDONED … Never signed"*;
`adapter-map.md` is *"reviewed at P1"* with no signature.
`General-Harness-Contract-v2.md`, not in the round's list, is an explicit `UNSIGNED CANDIDATE`
and correctly leaves the frozen surface. `ResearchSystem-Contract.md` (FROZEN at P0, signed
2026-07-12 at its §4) and `Stage-Control-Contract.md` (`corrective status: SIGNED`) stay frozen
under the new wording, as they must.

### 2.2 The E10 deferral clause — sound in shape, unowned in custody

> *an amendment of at most one sentence whose effect on every round in flight is nil may be
> relied upon before its read, provided the commit records both facts and the bytes ride the
> next read of this layer — deferral, never exemption*

The design choice — deferral rather than the exemption the user's earlier ruling wording
suggested — is the stronger of the two and the commit argues it from a real instance
(`f453369` changed a live obligation about how a dispatch range is written). "At most one
sentence" is mechanically decidable. "Effect on every round in flight is nil" is an executor
self-judgment, but it is bounded: the bytes are still read later, so a wrong self-judgment is
deferred, not erased. I have no blocker here.

What it does not do is say **who holds the deferred bytes until that read**. The clause hands
the obligation to *"the next read of this layer"*, while the same rule scopes an amendment read
to *"the amendment text itself"* — a different text — and the other candidate, the cold read at
each round's opening, carries *"unless the user waives it"* and has been waived at Phase A, C0,
C1 and C1.5 (`HARNESS-LEDGER.md:120-124, 143-146, 189-191, 204-206`). The one live instance is
carried by hand in the pointer section (`:27-30`). See **F-3**.

### 2.3 The E10 convergence clause — the gap it closes is real; its guard is not the mechanical thing the round says it is

> *a read's must-fix findings are answered by an amendment commit plus an independent re-read of
> the amended text, and that pair is not a round and spends no budget, for as long as no round
> has relied on the text — once one has, changing it opens a round*

The gap is real and I re-derived it: R9 routes only *wording-level* read findings to the bank,
so a non-wording-level must-fix from a read has no route but a round, and a round draws a FULL
under E9. The clause is also correctly narrow — it is scoped to *a read's* findings, so it
cannot be turned on a FULL's blockers to escape a VERIFY, and the reliance test excludes
`README.md` / `EXECUTION.md` / `REVIEW.md` / this checklist by construction, since every round
relies on those.

The load-bearing term is **"no round has relied on the text"**, and `af2905c` certifies it as
*"greppable rather than self-asserted"*. I ran the grep the claim invites, on the artifact the
clause was written for:

```
$ grep -rn "supersession-2" --include=*.py ResearchSystem
ResearchSystem/tooling/rsclib/document_harness/assurance_state.py:113

$ git log --oneline -L113,114:…/assurance_state.py
f2507a5 V3-PHASE-C1.6-CONTRACT-SUCCESSOR-AND-WORDING-v1
```

Live code carries *"supersession-2 (2026-07-29) supersedes that one statement"*, written by
round C1.6 — a round that spent a FULL, a fix and a VERIFY. A grep answers *relied upon*. A
careful reader may well answer *authored, not relied upon*, and I think that reading is the
better one. Both are available, the difference is one FULL of budget, and C1.7 is the next round
to face it. See **F-1**.

### 2.4 Edit form under E10

E10 requires edits *"additive or subtractive, never re-typed with the same content"*. Satisfied:
the E10 hunk is a pure insertion, and the E2 hunk substitutes one phrase and inserts a clause.
Both are permitted. The commit's *account* of that is wrong in a small way — see **F-2**.

### 2.5 Guards, tests, frozen surface

There is nothing to mutation-test: the round adds no guard and no executable byte, so E4 / E5 /
R8 are vacuous against it, and their absence is not an omission. What I re-derived rather than
accepted:

```
$ python tests/document_harness/run_tests.py          Ran 151 tests   OK
$ python tests/document_harness_review/run_tests.py   Ran 325 tests   OK
$ python tests/harness/run_tests.py                   Ran  39 tests   OK
$ python tests/stage_control/run_tests.py             Ran  20 tests   OK
$ python tests/run_tests.py                           tests: 29   passed: 29   failed: 0
$ python Thesis/Work/Tooling/repo-audit.py            RESULT: clean (exit 0)

$ git rev-parse HEAD:.goals/plans/document-work-assurance-harness-v3.plan.md
8ad404b12b3242e700d0ad215048dffccada7d9c
$ git rev-parse HEAD:…/Document-Work-Assurance-Contract-v3.md
b2dbdf752d8c155e4c65b14b5f420b880b8184a1
$ git rev-parse HEAD:…/Document-Work-Assurance-Contract-v3-supersession-1.md
68031fa2ca31272e31da0d42a9a02189d28fcc21

$ git diff --stat 17e2b65..af2905c -- ResearchSystem/contract ResearchSystem/schema \
    ResearchSystem/assurance ResearchSystem/tooling \
    .goals/plans/document-work-assurance-harness-v3.plan.md
(empty)
```

Every figure the round reported reproduces exactly, including the three blob digests and all
five suite counts. The two user-locked oracles (`tooling/tests/fixtures/expected-construction-prompt.txt`,
`tooling/tests/document_harness/test_readme_enumeration.py`) are inside that empty diff and are
untouched. The round's own caveat that a green suite is weak evidence about a prose payload is
correct and I add nothing to it.

---

## 3. Boundary and process conformance (R3 — run second)

- **E2 frozen surface:** not crossed (diff above empty over `contract/`, `schema/`, `assurance/`
  and the signed plan).
- **E8:** explicit paths (no `-A` artifacts — three files, all intended), new commits, no amend,
  no push, single dense title per commit in `V3-…-v1` form, one paragraph, no trailers. Kind is
  named in both bodies. `6618b84`'s kind — a ruling record that is not a round — matches none of
  E8's five names; it self-describes unambiguously, so nothing is lost (**O-6**).
- **E9:** the classification (candidate, consumes nothing) follows E9's stated test, and the
  round did not self-classify beyond it.
- **E12:** the range's tip equals `HEAD`, so nothing written inside the round was dropped from
  the subject — including the ledger bullet and the plan pointer, both written in `af2905c`
  itself.
- **E3:** the reported figures are all true (re-derived above). One characterization is not
  (**F-2**), and two counts describing another record are not (**B-1**).
- **E10 layer scope:** `CONSTRUCTION-CHECKLIST.md` is in the layer; `HARNESS-LEDGER.md` and the
  plan are not, so their edits owe no read.
- **E11 preview card:** chat-only. `UNVERIFIABLE` (R4), not folded into supported.
- **Fresh context:** a process claim. Marked, not verified (R4).

---

## 4. Blockers

### B-1 — the round's records mis-state read `17e2b65`'s findings; C1.7's declared scope targets two findings that record does not contain, and drops the one it does

**Location.** `6618b84` commit body; `HARNESS-LEDGER.md:96` and `:100`;
`.goals/plans/harness-digest-narrowing.plan.md:197`; repeated in `af2905c`'s body.

**What they say.** *"The E10 independent read of supersession-2 returned two must-fix and three
low (record 17e2b65), and the reader judged both must-fix outside R9's wording-level class"*;
*"2 must-fix / 3 low / 4 observation"*; C1.7's scope *"already fixed and unchanged — R-1's
qualifier moved into section 2's main clause, R-2's undecidable time word replaced by a
mechanically decidable boundary, and the three low findings paid in the same batch under R9"*.

**Ground truth.** `17e2b65` added exactly one file, 265 lines. Its complete finding inventory:

```
$ grep -n "^### " …/v3-checkpoint-read-6e30c07.md
128:### M-1 (must-fix) — §4 names `instruction_ref` as a `digestRef`; it is a `frozenFileRef`,
     and nothing requires or checks a digest on it
190:### L-1 (low) — the `cf51534` blast radius is eight ISSUE_TRIAGE decisions, not five

$ grep -n "^\*\*O-" …/v3-checkpoint-read-6e30c07.md
221:**O-1 …   229:**O-2 …   240:**O-3 …   249:**O-4 …
```

**One** must-fix, **one** low, four observations. No finding is labelled `R-1` or `R-2`; the
strings do not occur in the file. The record explicitly forecloses inference of more: *"There is
no verdict below and none may be inferred from the absence of must-fix findings beyond the one
recorded."* And the two subjects C1.7 is told to fix were, in that same record, **cleared**, not
raised: §2's qualification is in the *verified clean* table (*"The §2 qualification about
`pointer_to` is **exhaustive**"*), and §3's forward statement about *"newly opened runs"* is
listed under R4 as `UNVERIFIABLE` **by construction** — no run has opened — which is an answer,
never a defect. Both descriptions instead match C1.6's already-**paid** blockers: B-1 (a global
present-tense docstring claim) and B-3 (the *"newly opened run"* qualification), both certified
paid by `v3-review-verify-293f657.md` §2.

**The decision that goes wrong.** C1.7 is suspended with its scope declared *fixed and
unchanged* in three committed files, one of which is the live pointer read at the start of every
session. As written, C1.7 will re-open two settled sentences and will **not** carry M-1 — the
one real must-fix, which the read argued at length lands *"on the one distinction the whole
adjudication turns on, and points the wrong way"* (§4 places `instruction_ref` in the ref class
needing a user decision against E2, when it is in fact the `frozenFileRef` the same triage
decision names as *the replacement*). M-1 appears in no ledger bullet, no plan step and no bank
entry; on the current records it is lost. The count error compounds it: three lows are budgeted
where one exists, and the real one (L-1, `five` → `eight`) is named nowhere.

**Minimum fix.** Correct `HARNESS-LEDGER.md:96/100` and `plan:197` to the record's actual
inventory (1 must-fix M-1, 1 low L-1, 4 observations), restate C1.7's scope as M-1 plus L-1, and
add an errata commit naming the two commit bodies that carry the wrong figures (E8: never
amend). If material outside the repository informed the *"R-1 / R-2"* scope, it is chat-only
load-bearing material and must be written down (R2).

### B-2 — the enumeration that scopes the E2 narrowing calls a user-signed file unsigned

**Location.** `HARNESS-LEDGER.md:91-92`; the same sentence in `af2905c`'s body.

**What they say.** `contract/` *"还装着 `adapter-map.md` / `block-grammar.md` /
`content-roots.yaml` / `baseline/` / `amendments/`，都不是签名契约"* — *"none of them signed
contracts"*.

**Ground truth.** `ResearchSystem/contract/amendments/2026-07-18-a1-p4-scoped.md` is signed:

```
$ grep -n "Sign-off (SIGNED" …/amendments/2026-07-18-a1-p4-scoped.md
710:## §9. Sign-off (SIGNED 2026-07-18) — approves §0–§8; does not activate implementation

ResearchSystem-Contract.md:25  (Active Amendment Index)
  … Signature and digest evidence: user Melclycj, 2026-07-18; … signed file SHA-256
    2D672D0D329E845CC598FF6089B3FA460118C382A66CB67635C910652E23F04C …

$ git show HEAD:…/amendments/2026-07-18-a1-p4-scoped.md | sha256sum
2d672d0d329e845cc598ff6089b3fa460118c382a66cb67635c910652e23f04c
```

The stored bytes still hash to the recorded signed digest. Under the source rule the round is
restoring — *"Signed bytes are untouchable"* — this file is squarely inside it, and the banked
finding it pays (V-b) says *"the freeze is on **signed bytes**"*, not on signed *contracts*.

**The decision that goes wrong.** The narrowing's whole justification is that everything else
under the path is safe to drop. A future executor reading the ledger — or the provenance in the
commit body — concludes `amendments/` left the frozen surface, and edits user-signed bytes
carrying a published digest, which is the single case E2 exists to refuse. The rule text alone
would probably still catch it (*"signed contracts"* + a file whose §9 says SIGNED), but the
round's own record instructs the opposite, and E2's closing sentence makes the rule authoritative
precisely so that derived statements do not have to be trusted — here the derived statement is
the one that scopes the rule.

**Minimum fix.** Write E2 as *"the **signed bytes** under `ResearchSystem/contract/`"*, matching
rule 5's category and V-b's wording, which resolves it without any enumeration; or keep *"signed
contracts"* and correct the ledger sentence so `amendments/2026-07-18-a1-p4-scoped.md` is named
as signed and inside the frozen surface. Either is one sentence. The checklist edit is
instruction layer and rides the read this round already owes.

---

## 5. Non-blocking findings

**F-1 — the convergence clause's guard is not mechanical, and its own instrument returns the
wrong answer on the case it was written for.** `af2905c` certifies *"the reliance test, which is
greppable rather than self-asserted"*. Grepping `supersession-2` across the tree hits
`assurance_state.py:113`, a docstring written by round C1.6 (`f2507a5`) stating that
supersession-2 supersedes supersession-1 §3 — so a grep says *relied upon*, and the clause would
already exclude the artifact that motivated it. The distinction that saves it — a round that
**authored and recorded** a text has not *relied* on it — is nowhere in the text. The
consequence is immediate: C1.7 is the next round and must decide, with no criterion, whether it
is a round at all, and the two answers differ by one FULL. Not raised to blocker because a
defensible clean reading exists and the clause is otherwise correct; a single qualifier ("no
round has taken its governance from the text; authoring it is not reliance") settles it. Note
also that *"greppable rather than self-asserted"* is a characterization no command establishes —
E3's class — and the command I ran contradicts it.

**F-2 — `af2905c`'s account of its own edit form.** The body states *"both hunks are insertions,
and the only lines showing as deleted are ones whose unchanged fragments share a wrapped line
with the insertion point"*. True of the E10 hunk. The E2 hunk deletes `existing files under` and
writes `and the **signed** contracts under` in its place — a substitution, which is the round's
actual intent and is permitted by E10 (*additive or subtractive*), so the compliance conclusion
stands on a false ground. *"Additive only"* and its kin are the characterization class the source
discipline's rule 4 names as this layer's dominant defect. Wording-level under R9 — the accurate
fact is stated correctly two sentences earlier in the same body (*"E2 now says signed contracts
under that path"*) — so it rides the next batch touching these records, alongside B-1's errata.

**F-3 — the deferral clause creates a second unowned obligation queue.** *"The bytes ride the
next read of this layer"* names no custodian and no deadline, while the amendment read is scoped
to a different text and the cold read is routinely waived. `HARNESS-LEDGER.md:84` already records
the identical gap for R9's bank — *"R9 自身未写「家在哪、谁登记」……待裁"* — and this round, whose
batch touched exactly that file, did not pay it for either queue. The one live instance
(`f453369`) survives only because the pointer section carries it by hand. Non-blocking: the
practice exists and the obligation is stated. Fixing both queues in one sentence is the natural
scope for whichever batch next opens this layer.

**F-4 — the two new ledger bullets are a second copy of each other, and they have already
drifted.** `HARNESS-LEDGER.md:85-94` (from `af2905c`) and `:95-106` (from `6618b84`) both
enumerate the same three-item scope. Item ① reads *"加明确出口"* in one and *"延后条款……取代原
「出口」措辞"* in the other. The file's own header forbids exactly this: *"A bullet that restates
them is a second copy that drifts."* The narrative belongs in the round record and the commit
bodies; the pointer needs one line.

**F-5 — the bank list still shows a paid item as open.** `HARNESS-LEDGER.md:61-63` lists
`VERIFY-②` (the E2 wording) among five banked items with the instruction *"随「`E10` 出口条款」那
一轮一起做"*, while `:94` states it is paid this round. The same bullet already demonstrates the
file's convention for closing bank items in place (*"（`F-b` 的活语态与 VERIFY-①③ 已在本收口兑
付。）"*), which was not applied here. Wording-level; rides the same batch.

---

## 6. Observations (R5 — reported, the conclusion is the user's)

**O-1 — E10 is now seven semicolon-joined clauses, and this round added two of them to close
findings.** It carries layer membership, edit form, the amendment read, deferral, convergence,
the cold read and provenance form in one rule. The shape R5 asks me to report is present:
successive rounds keep attaching clauses to this rule to close what the previous round's text
left open. I draw no conclusion about whether E10 should be split, only that the growth is
finding-driven.

**O-2 — the convergence clause removes the instrument that made a non-converging correction
chain countable.** C1.6's FULL referred exactly that question to the user under R5 (*"whether
the correction chain is converging is the user's question"*), and the ordering ruling was the
user's answer. Under the new clause, iterations on an unrelied-upon text spend no budget, so the
count that made the chain visible no longer runs. That may be the intended trade — the round
argues the round was the expensive half, not the read — but it is worth stating that the signal
and the cost were the same instrument.

**O-3 — the narrowing silently drops three self-declared-frozen files from E2's reach.**
`block-grammar.md` (*"FROZEN at P0"*), `content-roots.yaml` (*"frozen at P0"*) and
`baseline/P0-baseline.md` (*"FROZEN at P0"*, the reference state P8 compares against) are not
signed and so leave the rule's scope. Two of them are load-bearing to running code —
`rsclib/config.py:24` reads `content-roots.yaml`, `rsclib/grammar.py` implements
`block-grammar.md` G1-G8. This is faithful to rule 5, which never covered them either; whether
anything should protect them is the user's question, not a finding against this round.

**O-4 — three plan files still declare a freeze surface wider than E2.**
`harness-deletion-first-stabilization.plan.md:46` (the active carrier),
`harness-memory-lessons-integration.plan.md:44` and `harness-phase-c0-m8-m10.plan.md:142` all say
*"`ResearchSystem/contract/` 既有文件"*. E2's closing sentence makes them derived and never
independently authoritative, so nothing breaks, and over-freezing fails safe. Recorded because
the carrier plan was previously kept aligned with E2 by hand (its line 46 records a 2026-07-28
alignment) and this round changed E2 without a matching pass — correctly, since the plan was
outside the declared boundary.

**O-5 — the read this round owes has a narrower subject than usual, and B-2's fix would widen
it.** The owed read's subject is the amended checklist text. If B-2 is fixed by editing E2, the
read is owed on the repaired bytes, not these — the same sequencing C1.6 hit when `293f657`
changed supersession-2 after its FULL.

**O-6 — E8's commit-kind vocabulary has no name for `6618b84`.** It is a ruling record that is
not a round and consumes nothing; candidate / pre-submission correction / review fix / closeout /
errata all miss. Its body says so plainly in its first clause, so attribution cost me nothing.

---

## 7. Coverage (R4)

- **Read in full:** both commit bodies; the complete diff; `CONSTRUCTION-CHECKLIST.md` at
  `17e2b65` and at `af2905c`; `HARNESS-LEDGER.md` at `af2905c`; `v3-checkpoint-read-6e30c07.md`;
  `v3-dispatch-supersession-2-read.md`; the review-contract stub; `7011916`'s operating contract
  through hard rule 9, the scope discipline and the instruction-layer discipline;
  `dispatch.py`'s construction half; `assurance_state.py:95-134`; the headers of all twelve files
  under `ResearchSystem/contract/`.
- **Sampled:** `v3-review-verify-293f657.md` §§5-6; `v3-review-full-f2507a5.md` headings and
  blocker titles; the three plan files' freeze-surface lines.
- **Probed only:** the five suites and `repo-audit.py` (run, not read); `rsclib/config.py` and
  `rsclib/grammar.py` (reference sites only, by grep).
- **Not run, not owed:** mutation probes. The round adds no guard and no executable byte; E4 /
  E5 / R8 are vacuous against it.
- **`UNVERIFIABLE` (R4, R7), not folded into supported:** the E11 preview card; the user's
  ruling that deferral is acceptable; the user's three-item scoping; the executor's fresh
  context. Each is recorded only by the execution side. I also cannot verify the *absence* of a
  source for `R-1` / `R-2` outside the repository — B-1 states only that the cited record does
  not contain them, which is what R2 makes decidable.

---

## 8. Verdict

**`CHANGES_REQUIRED`.**

The three clauses are, as text, close to right: the E2 narrowing restores the category basis its
source rule always had, the deferral clause chooses deferral over exemption and argues it from a
real instance, and the convergence clause closes a routing gap in R9 that is genuinely there.
Every figure the round reported reproduces, the frozen surface is intact, and the boundary held.

Two things must change before the round closes. The records that scope the *next* round
mis-state the read they cite — two must-fix findings and three lows where one and one exist,
under labels the record does not use — with the effect that C1.7 is aimed at two settled
sentences and the one real must-fix is tracked nowhere (B-1). And the enumeration that justifies
the E2 narrowing names a user-signed, digest-published file as unsigned, pointing the rule's own
readers at the exact bytes it exists to protect (B-2). Both fixes are sentence-sized; neither
touches code.

Two further notes the fix round should carry rather than rediscover: the convergence clause's
key term is undefined at exactly the case C1.7 will face (F-1), and the read E10 owes on these
bytes is still owed — this FULL is not it, and cannot be banked as it.
