# Cold read — the instruction layer at `451e8b0` (opening of the 2026-07-29 reform 轮)

**No verdict.** A read is not a round (`R3`): it spends no budget, carries no verdict, and its
output is findings tiered must-fix / low / observation. This is the cold read `E10` owes at a
round's opening — the round being the reform 轮 the ledger carries as ② under NEXT. Nothing
below may be read as certifying any text; nothing below is banked as any round's FULL.

**Findings: 1 must-fix, 2 low, 6 observations.** The must-fix is on `E10`'s own membership
sentence and it bit inside this read: my re-derived member set is not the dispatched one.

---

## 1. Subject, re-derived

```
$ git log --format=%h -1 -- .../v3-dispatch-instruction-layer-cold-read.md
451e8b0
$ git log --format='%h %s' -1
451e8b0 V3-INSTRUCTION-LAYER-COLD-READ-DISPATCH-v1     # tip == HEAD, branch document-work-assurance-v3
$ git status --porcelain
?? ResearchSystem/docs/                                 # untracked, predates this work, not in the subject
```

The dispatch hands seven blobs and says its table is the execution side's derivation, that
`E10`'s sentence governs, and that a different member set is itself a finding. `E10` reads:

> The instruction layer is this file, `README.md`, `EXECUTION.md`, `REVIEW.md`, the two
> retired contracts' stubs, and any prose successor to signed text, including schema
> `description` strings when amended.

Enumerating that sentence against the repository at `451e8b0` yields **eight** members, not
seven, and its last clause reaches further than the harness governs (M-1).

| # | blob | lines | path | dispatched? |
|---|---|---|---|---|
| 1 | `d3228163` | 122 | `document-harness/CONSTRUCTION-CHECKLIST.md` | yes |
| 2 | `b344d807` | 32 | `document-harness/README.md` | yes |
| 3 | `bd490c8b` | 153 | `document-harness/EXECUTION.md` | yes |
| 4 | `70bc521e` | 218 | `document-harness/REVIEW.md` | yes |
| 5 | `0ae222fd` | 5 | `migration/.../v3-harness-operating-contract.md` (stub) | yes |
| 6 | `7dcdb817` | 5 | `migration/.../v3-harness-review-contract.md` (stub) | yes |
| 7 | `2cf4983c` | 110 | `contract/…-v3-supersession-2.md` | yes |
| 8 | `68031fa2` | 124 | `contract/…-v3-supersession-1.md` | **no** — added by my reading |

All eight blob ids re-derived by `git ls-tree 451e8b0 <path>` / `git rev-parse HEAD:<path>`;
blobs 1-7 match the dispatched table exactly. **All eight were read end to end this session.**

Provenance of each member's current bytes, and whether a prior read exists for them:

| member | current bytes from | prior read |
|---|---|---|
| checklist | `7615733` | `v3-checkpoint-read-d322816.md` — end-to-end, same blob |
| README | `cf040af` | one line verified in `v3-checkpoint-read-ff05ea3.md`; whole file last cold-read at blob `0763c84` (`1df6245`), 4+/1− since |
| EXECUTION / REVIEW | `820b287` | `v3-checkpoint-read-820b287.md` (diff-scoped, incl. the verbatim `history/` move) |
| both stubs | `a8113d4` | `v3-checkpoint-read-ff05ea3.md` |
| supersession-2 | `d0372d8` | **parked** (`bfb233f`); predecessor blob read at `v3-checkpoint-read-a7d7121.md` |
| supersession-1 | `19cb882` | cold-read at `1df6245`; frozen under `E2` since |

## 2. The three dispatched facts, checked

1. **Owed at a round's opening — holds, with one correction of wording.** `E10` says a cold
   read "is owed at each round's opening unless the user waives it". `HARNESS-LEDGER.md` at
   `451e8b0` does not name the reform 轮 as NEXT; it names *this read* as ① under NEXT and the
   reform 轮 as ②, with the reform plan card explicitly deferred until this read returns. The
   read therefore precedes the round rather than accompanying it, which is what `E10` asks for.
2. **`v3-checkpoint-read-d322816.md` §6 — holds.** Its disclosure reads "the subject
   (`CONSTRUCTION-CHECKLIST.md`, 122 lines, read end to end this session)", and the blob is the
   same; `git cat-file -p d3228163 | wc -l` → **122**. The second sentence ("no read record is
   keyed to any of the other six blobs") is true as stated — `grep -rl` for each of the seven
   short shas across this directory returns only the dispatch note itself for six of them —
   but it understates coverage: the *commits* that produced five of those six blobs each carry
   their own checkpoint read (table above). The one genuinely unread state is supersession-2's,
   which is fact 3's second debt.
3. **Both debts — dischargeable, and discharged here.**
   - `f453369` (`V3-E12-RANGE-TIP-v1`): `git merge-base --is-ancestor f453369 HEAD` → true; its
     hunk added three lines to `E12`, and those lines are present verbatim in blob `d3228163`,
     which I read in full. The commit body records the user's override of the amendment read.
     **Read, this session, at its current bytes.**
   - supersession-2 §3: `git diff 4e80df7 d0372d8` on that path is one hunk, §3's first
     sentence, and it is the *first* of the two minimum fixes `v3-checkpoint-read-a7d7121.md`
     M-1 offered, applied with the wording it proposed. **Re-read, this session** — result at
     L-1 below: the collision M-1 named (two branches, different objects, both fire) is gone;
     a narrowed residue of M-1's second half survives and is not must-fix.

## 3. Implementation first (`R3`) — what I checked in the repository, not in the prose

| claim in the layer | re-derived |
|---|---|
| `E2`: plan `8ad404b1…`, contract `b2dbdf75…`, supersession-1 `68031fa2…` | all three `git rev-parse HEAD:<path>` identical ✓ |
| `E2`: "every existing file in `schema/document-assurance-v3/`" | 14 files; README's enumeration names exactly those 14 ✓ |
| README: fixtures "41/41 green" | re-ran `validate_fixtures.py` → `41/41 cases behaved as declared; failures=0` ✓ (the 34 in `cases.json` are the schema cases; bundle cases make the rest) |
| README: N0 record §8 / W2-record §log (`ac1b383`) | both headings exist; `ac1b383 V3-W2-SIGN-OFF-CLOSEOUT-v1` ✓ |
| README: supersession-1's own top line says UNSIGNED | it does ("UNSIGNED until the wave-2 gate"); README's row states the signature, as it says ✓ |
| stubs: full text at `7011916` | `git cat-file -s 7011916:<both paths>` → 21737 / 22719 bytes ✓ |
| stub: "the construction dispatch fixture hard-codes this path" | `tooling/tests/fixtures/expected-construction-prompt.txt` names the review-contract stub as standing instruction; the stub redirects to the checklist and calls itself "its own counterpart" — the chain closes ✓ |
| `E12`: `rsc v3 dispatch` | exists — `rsc.py::_cmd_v3_dispatch`, `--range BASE..TIP` and `--subject` ✓ (see O-4) |
| supersession-2 §2: the five protected fields | `DIGEST_PROTECTED_FIELDS` is exactly those five ✓ |
| supersession-2 §4: "only `review_ref` has a live template write path" | `templates/run-v2/` has 5 `pointer_for` calls: `review_ref` (protected) + fulfillment/manifest/check_results/coverage (unprotected) ✓ |
| supersession-2 §4: hand scripts still pass caller digests | `assurance/runs/{p3-corr,w1-r1}/*.py` — every direct `pointer(...)` call passes a digest ✓ |
| supersession-2 §2 quotes supersession-1 §3's bullet | byte-identical to supersession-1's final §3 bullet ✓ |

## 4. Must-fix

### M-1 — `E10`'s member sentence is under-inclusive as dispatched and over-inclusive as written; a cold read cannot derive its own subject from it without arbitrating

**Location:** `CONSTRUCTION-CHECKLIST.md:61`, the clause *"and any prose successor to signed
text"*. **Ground truth it violates:** the repository's own `contract/` tree, and `E2`'s
adjacent scope qualifier.

Two halves, one sentence.

**(a) It includes supersession-1, and the dispatch dropped it.** Supersession-1 is a prose
successor to signed text by the same words `v3-checkpoint-read-a7d7121.md` used to place
supersession-2 inside the layer ("Supersession-2 is inside E10's instruction layer as *any
prose successor to signed text*"). Nothing in `E10` distinguishes a signed successor from an
unsigned one. Being frozen under `E2` removes its *amendment* reads — it cannot be edited —
but not its cold-read coverage, and it is precisely the member whose §3 the shipped code now
contradicts. I read it (124 lines) rather than inherit the omission.

**(b) It reaches instruments this harness does not govern.** `contract/amendments/2026-07-18-a1-p4-scoped.md`
is a prose amendment signed by the user against `ResearchSystem-Contract.md` — a prose
successor to signed text on its face, and a document of the P0-P14 track, not this harness.
`E2` was narrowed on 2026-07-29 with an explicit qualifier — *"a path outside them is not
frozen by this rule, and this harness does not claim to freeze instruments it does not
govern"* — and `E10` received no parallel words. So the freeze surface is bounded by ruling
while the read surface is bounded by nothing.

**Why must-fix rather than low.** It changes an obligation — what a cold read must cover — so
`R9`'s wording-level test fails at its first condition, and the accurate answer is not
recoverable from adjacent text: `E2`'s qualifier is about freezing, and no committed record
says whether supersession-1 is in or out of the layer. It is not hypothetical: it produced a
divergence in this read's subject, which is the read the reform 轮 opens on.

**Minimum fix — text only, no machinery (`E6`).** Replace the clause with an enumeration plus
the qualifier `E2` already carries, e.g.:

> …the two retired contracts' stubs, the contract supersessions under `ResearchSystem/contract/`
> (`supersession-1`, `supersession-2`), and any later prose successor to text **this harness
> governs**, including schema `description` strings when amended.

Decidable by inspection, same shape as `E2`'s "three blobs and one directory", and it costs one
sentence in a file the reform 轮 is already amending.

## 5. Low (`R3` — named, not inflated; no route exists for this tier, per the 2026-07-29 ruling)

### L-1 — supersession-2 §3 still classifies as *prior text* bytes that `pointer_for` itself produces

The re-fix cured M-1's first half: both branches now quantify over the pointer, so a run can no
longer satisfy both. The second half survives, narrowed. `pointer_for` returns a bare
`pointer(path)` for every unprotected field (`assurance_state.py:134-139`), so a hand-authored
`assurance_state.pointer(path)` for `resolved_plan_ref` is **byte-identical** to what the
successor text prescribes — and §3's second branch places it under the prior text, which
obliges a digest it does not carry.

**Why this is low and not must-fix.** Nothing acts on the classification. The code decides by
field, not by text version, and its negative control is explicit:
`test_an_unprotected_pointer_without_a_digest_is_unverified_but_not_an_issue` asserts
`report.ok` — a missing digest on an unprotected field raises nothing, whichever text governs.
The only affected reader is a future reviewer hand-classifying a run, and §2 + §4 recover the
intent. No live run is open; the templates never call `pointer` directly.

**Minimum fix if it rides a batch:** close the sentence with the equivalence rather than a
third branch — *"…is under the prior text where the two texts differ; for an unprotected field
written as a bare `pointer(path)` they do not."*

### L-2 — README's authoritative-documents table does not name supersession-2, so the layer steers a fresh reader into a bullet the shipped code contradicts

The chain a cold reader follows is README → "Supersession 1 (signed 2026-07-24)" → its §3
bullet *"A state pointer carries the BYTES digest of the pointed-at file… the documented
authoring path is `assurance_state.pointer_to`"*. Since 2026-07-29 both halves are false of the
code: `pointer_for` is the documented path and writes bare pointers for 9 of the 14 state
fields. The corrective exists, is committed, and appears nowhere in the layer's index.

**Named downstream decision that goes wrong:** a reviewer of the next run reads the layer,
finds `pointer_for` emitting digest-less pointers, and reports a contract violation — the
`REVIEWED_NO_BLOCKER` path turns on it. **Precedent that makes it worth naming:** `F1` of the
`1df6245` cold read was this exact shape one contract-version earlier ("the layer now states
the supersession-1 signature instead of steering a fresh reader into the retired package-bound
regime"), and its fix was one README row.

**Counter-argument, stated because it may be decisive:** README's table has never carried an
unsigned successor — the supersession-1 row was added `39e4136` (2026-07-27), three days
*after* signature — and `bfb233f` parked supersession-2's own read on the ground that nothing
relies on it. Listing it now is therefore a change of practice, not a repair of one. That is
the user's call (`R5`).

**Minimum fix if taken:** one row in the same shape as the supersession-1 row, stating
UNSIGNED and that it narrows §3's digest bullet.

## 6. Observations (`R5` — reported; the conclusion is the user's)

- **O-1 — `R9` sits out of sequence.** Order in the file is R1, R2, R3, **R9**, R4, R5, R6, R7,
  R8 (lines 89-121). Adjacency to `R3`'s read clause is presumably why; a reader scanning for
  `R4` after `R3` meets `R9` instead. No obligation turns on it.
- **O-2 — 57 lines of `REVIEW.md` live outside the layer.** `820b287` moved the package-bound
  sections verbatim to `document-harness/history/REVIEW-v1-package-flow.md`; that path matches
  no clause of `E10`. It governs only the reading of pre-wave-2 history, so the exposure is
  bounded — but it is editable today with no amendment read, which is the property `E10` exists
  to deny the text it enumerates.
- **O-3 — `E10`'s schema-`description` clause is currently unreachable.** `E2` freezes every
  *existing* file in the pack, so no existing description can be amended at all; the clause can
  only bite on a pack file added after the (unpinned) "existing" moment. That moment is the
  already-banked `existing` 未钉时刻 item; recorded here only as the second rule it affects.
- **O-4 — `E12`'s "never a written SHA" is unqualified where the tool is not.** `rsc v3
  dispatch --range BASE..TIP` resolves both ends and prints full SHAs, and `dispatch.py:152`
  says the dispatcher "may type `HEAD` or a short SHA while the routed document always carries
  the full commit"; the prompt is printed, never written (`rsc.py`). Read as governing a range
  *recorded in a file*, rule and tool agree; the sentence does not say so, and a dispatcher
  applying it literally to the CLI argument would think the shipped invocation violated it.
- **O-5 — this dispatch, and the record channel.** The note handed me seven blob ids plus three
  facts, which is more than `R2`'s "one SHA / range and nothing else"; it disclaimed all of it
  ("yours governs and the difference is a finding", "pointers, not conclusions; verify each"),
  and the disclaimer earned its keep — the member set differed (M-1). Separately, `R6`
  enumerates `v3-review-{full,verify}-<subject-sha>.md` and `v3-checkpoint-read-<sha>.md`
  only, while `v3-cold-read-<sha>.md` is the established third family (two exist; this note
  instructs a third). I wrote the instructed name; the enumeration is stale, and that is
  wording-level under `R9` — no actor's action turns on it — so it is banked, not a finding.
- **O-6 — the divergence window is open by design, and nothing schedules its close.** Signed
  supersession-1 §3 and the shipped code disagree; the reconciling text is authored, UNSIGNED,
  and parked at "first reliance" per `bfb233f`, which reasons that first reliance may never
  come. Meanwhile the code's own docstrings carry the correction. Whether to sign
  supersession-2, or to leave a signed statement standing falsified indefinitely, appears in no
  ledger line and in no NEXT item.

## 7. Disclosure (`R4`)

**Read in full:** all eight layer members at the blobs tabulated in §1 (122 / 32 / 153 / 218 /
5 / 5 / 110 / 124 lines), each fetched by `git cat-file -p <blob>`, not from the worktree;
`HARNESS-LEDGER.md` at `451e8b0`; the dispatch note; `v3-checkpoint-read-a7d7121.md` §4-§5 and
§7, `v3-checkpoint-read-d322816.md` §6, the headings and subject sections of
`v3-checkpoint-read-820b287.md` and `v3-checkpoint-read-ff05ea3.md`; the commit bodies of
`f453369`, `d0372d8`, `bfb233f`, `cf040af`, `39e4136`; `assurance_state.py:81-139` and its
module docstring; the three digest tests in `test_spec_plan_state.py:890-1000`;
`expected-construction-prompt.txt`.

**Sampled:** `dispatch.py` and `rsc.py` by grep for the range/tip path only; the run scripts
under `assurance/runs/` and `assurance/templates/run-v2/` by grep for `pointer`/`pointer_for`
call sites plus two read in context (`p3-corr/run_audit.py`, `p3-corr/run_start.py`);
`contract/amendments/` by their first 12 lines each; the earlier read records by heading and
targeted grep, not end to end.

**Probed only:** the claim that no read record is keyed to the other six blobs — seven `grep -rl`
runs over this directory, one per short sha. Absence by grep is weak evidence of absence; the
provenance table in §1 is the stronger form of the same question and is what fact 2's correction
rests on.

**Not verified.** No suite was run: this read changes nothing and every figure I cite came from
a command in this session, but I did not re-run the 151/325/39/20/29 suites or `repo-audit` that
`d0372d8` reports, so those numbers are the executor's, unchecked. `validate_fixtures.py` I did
re-run because README states a standing count.

**Marked, not verified (`R4`):** that this session is fresh context. It is — it opened on the
dispatch note and has read only what §7 lists — but that is a process claim with no evidence
lock, and `R1`'s independence question is answered by who set the question, not by my say-so:
the note that scoped me was authored by the execution side, which is why §1 re-derives the
subject rather than adopting it.

**`UNVERIFIABLE`:** whether `E10`'s "any prose successor to signed text" was *intended* to
reach supersession-1 or the P4 amendment. M-1 rests on what the sentence says, not on intent,
and the repository records no ruling either way — the 2026-07-29 adjudication that narrowed
`E2` is recorded as being about the freeze surface. Also unverifiable from the repository:
whether the user's park of the supersession-2 read (`bfb233f`) was meant to survive this cold
read or to be superseded by it; the ledger says the debt is cleared by this record stating its
coverage, which §2.3 does, and I have taken that as the answer.
