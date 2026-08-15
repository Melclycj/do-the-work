# Checkpoint read — `CONSTRUCTION-CHECKLIST.md` blob `f9a6600b`, the E2 blob-enumeration amendment

**No verdict.** A read is not a round (R3): it spends no budget, carries no verdict, and its output
is findings tiered must-fix / low / observation. This is the independent re-read the convergence
clause of E10 owes on the amended bytes, and **no round, FULL or VERIFY, is banked as it.**

**Findings: 2 must-fix, 2 low, 5 observations.** Labels are local to this record; cite them as
`read f9a6600 M-1` and so on — read `9f2ec9a`'s `M-1`/`L-1`–`L-3` and read `f97b348`'s `M-1`–`M-3`
are different findings.

---

## 1. Subject, re-derived

The subject is a text, not a range. Its identity, established before reading it:

```
$ git cat-file -t f9a6600bc7786172f877b8e2118d8d851a386221
blob
$ git rev-parse HEAD:ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md
f9a6600bc7786172f877b8e2118d8d851a386221
$ git rev-parse 6f96139:ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md
f9a6600bc7786172f877b8e2118d8d851a386221
$ git hash-object ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md
f9a6600bc7786172f877b8e2118d8d851a386221
$ git status --porcelain ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md
(empty)
$ git rev-parse --short HEAD
6f96139
$ git cat-file -p f9a6600 | wc -l
120
```

The bytes at `6f96139`, at `HEAD` and in the worktree are one object, so reading the file reads the
subject. `9f2ec9a` is likewise a blob (`git rev-parse 87a4ced:<path>`), so `git diff 9f2ec9a f9a6600`
is the amendment and nothing else: **one hunk, in `E2`, net subtractive** (13 removed, 6 added).

The amended rule in full, subject lines 23-29:

```
23  - **E2** Frozen bytes are untouchable, and the list is exactly this: signed plan blob
24    `8ad404b1…`, contract `b2dbdf75…`, supersession-1 `68031fa2…`, existing N0 schema files.
25    Enumerated by blob, so nothing has to decide what *signed* means and **a file not listed is
26    not frozen by this rule** — signed instruments this harness does not govern are frozen by
27    their own tracks, not here. When the cleanest fix needs one, take the in-boundary fix and
28    record why, or stop with `SPEC_GAP`. A boundary declared anywhere else — a plan's freeze
29    surface, a round's own card — is derived from this rule and never independently authoritative.
```

What the hunk did, separated into what is new and what is inherited, because the two carry
different weight below:

- **D-1 (deletion)** — the `signed bytes under ResearchSystem/contract/` clause and the definition
  of `signed` that read `9f2ec9a`'s `M-1` attacked, together with **the citation
  `(7011916 rule 5: approved plan, contracts, N0 schemas)`** and the `UNSIGNED successor … falls to
  E10's read path` carve-out. All four went out in one hunk.
- **A-1 (addition, line 23)** — *"and the list is exactly this"*.
- **A-2 (addition, lines 25-26)** — *"Enumerated by blob, so nothing has to decide what signed
  means and a file not listed is not frozen by this rule"*.
- **A-3 (addition, lines 26-27)** — *"signed instruments this harness does not govern are frozen by
  their own tracks, not here"*.
- **Inherited unchanged** — the three blob literals, the phrase *"existing N0 schema files"*, and
  the whole `SPEC_GAP` / derived-boundary tail (lines 27-29). The tail's first line is re-typed in
  the diff only as a rewrap; its content is byte-identical in substance.

---

## 2. The precondition, checked before anything else

C-3's route is available only *"for as long as no round has relied on the text."* The commit asserts
this; R2 forbids accepting it. Two windows, both classified by diff and not by message.

**The tight window — the bytes actually deleted.** The `signed` definition inside D-1 was written at
`87a4ced`. Between `87a4ced` and `6f96139` there is exactly one commit:

```
$ git log --format='%h %s' 87a4ced..6f96139
2bd678f V3-REVIEW-RECORD-CHECKLIST-REREAD-9f2ec9a-v1
$ git show --stat --format='' 2bd678f
 .../v3-checkpoint-read-9f2ec9a.md | 297 +++++
```

One review record, one file. A read is not a round (R3), so nothing in this window is a round at
all, and no round can have relied on bytes that did not exist during one.

**The wide window — all of `E2` since the last round closed.** Part of D-1 (`signed bytes … by any
instrument`) predates `87a4ced`; it was written by `f054a08`, the repair half of the last round.
Classifying every commit after `f054a08` by its own diff:

```
$ for c in 6798ebc 5760f8b 707722d e56af0d 25f2916 c50729e 87a4ced 2bd678f; do git show --stat --format='' $c; done
 .../v3-review-verify-f054a08.md                 | 327 +++++
 ResearchSystem/HARNESS-LEDGER.md                |  46 ++--
 ResearchSystem/HARNESS-LEDGER.md                |   9 +--
 ResearchSystem/HARNESS-LEDGER.md                |   8 +-
 ResearchSystem/HARNESS-LEDGER.md                |  10 +
 .../v3-dispatch-checklist-amendment-read.md     |  25 +
 .../v3-checkpoint-read-f97b348.md               | 236 +++++
 ResearchSystem/HARNESS-LEDGER.md                |  25 +
 .../document-harness/CONSTRUCTION-CHECKLIST.md  |  13 ++-
 .../v3-checkpoint-read-9f2ec9a.md               | 297 +++++
```

Eight commits, four files between them: three review records, the ledger, one dispatch, and one
amendment. **No code, no schema, no test, no fixture, no contract byte.** Nothing here is a FULL, a
fix or a VERIFY.

I read the ledger hunks rather than only their `--stat`, because a ruling is where reliance would
hide. `707722d` is the one that cites the amended `E2` — *"故按修好的 `E2`（冻 signed bytes）在保护
范围外——**忠于源规则**"* — and it is over-determined exactly as read `9f2ec9a` reported: it rests on
the source rule as well, and it is a ruling, not a round. `e56af0d` and `25f2916` turn on `C1.7`
scope and on `E3`/`E6` respectively, not on `E2`. Under E10's test — *would the outcome change if
the text changed* — none is reliance.

**The route was available.** It remains available as of this reading, so this record's must-fixes
are answerable the same way.

---

## 3. Must-fix

### M-1 — `E2` now says non-membership is dispositive, but one of its four items is an unenumerated category covering 7 of the 14 files in one directory, and the amendment deleted the only pointer that resolved it

**Location:** subject lines 23-26 (`E2`), the interaction of the inherited phrase *"existing N0
schema files"* with A-1 and A-2. **Ground truth it violates:** the contents of
`ResearchSystem/schema/document-assurance-v3/`.

A-2 makes two claims about the list: that it is *"[e]numerated by blob"*, and that *"a file not
listed is not frozen by this rule."* The first is false for the fourth item and the second is
therefore load-bearing in a way it cannot support.

**The directory holds fourteen schema files; `E2` freezes seven of them and names none:**

```
$ git ls-tree -r --name-only HEAD ResearchSystem/schema/document-assurance-v3/ | grep -c '\.schema\.json$'
14
$ N0C=$(git log --diff-filter=A --format=%h -- .../document-assurance-v3/common.schema.json | tail -1); echo $N0C
9237960   (V3-N0-TRANSITION-CONTRACT-CANDIDATE-v1)
$ git ls-tree -r --name-only 9237960 ResearchSystem/schema/document-assurance-v3/ | grep '\.schema\.json$' | sed 's|.*/||'
assurance-work-state.schema.json  common.schema.json  document-assurance-profile.schema.json
document-work-spec.schema.json    instruction-coverage-audit.schema.json
resolved-assurance-plan.schema.json  user-decision.schema.json
```

Seven at N0, and `N0/N0-record.md` confirms the count is deliberate — *"`ResearchSystem/schema/
document-assurance-v3/**` (7, exactly the nominated schema files)"*. The other seven
(`assurance`, `candidate-record`, `document-work-spec.v2`, `harness-issue`, `local-check-spec`,
`review`, `review.v2`) were added afterwards and are not "existing N0 schema files" on the reading
that makes the word *existing* mean anything.

**`N0` is not a directory that contains schemas.** The one directory named `N0` holds a record,
fixtures and a runner:

```
$ git ls-tree -r --name-only HEAD .../document-work-assurance-v3/N0/ | grep -c 'schema\.json'
0
```

So a reader who takes *"N0 schema files"* at face value looks under `N0/`, finds no schema at all,
and concludes the item is empty — after which A-2's *"a file not listed is not frozen by this
rule"* licenses editing every one of the fourteen.

**The amendment removed the pointer that made this resolvable.** D-1 deleted
`(7011916 rule 5: approved plan, contracts, N0 schemas)`. The source rule reads:

```
$ git show 7011916:.../v3-harness-operating-contract.md | sed -n '174,176p'
5. **Signed bytes are untouchable** (approved plan, contracts, N0 schemas incl.
   `common.schema.json`). When the *cleanest* fix needs one, that is an out-of-boundary write in
   better clothes: take the in-boundary fix and record why, or stop with `SPEC_GAP`.
```

`common.schema.json` — named in the source rule by name, and living in
`schema/document-assurance-v3/`, not under `N0/`. That citation was the one thing in `E2` connecting
the phrase to its referent, and it went out in the same hunk that declared the list exact.

**The decision that goes wrong.** An executor asked to change `common.schema.json` (nominated,
frozen) and one asked to change `review.schema.json` (added later, not frozen) get the same answer
from `E2`: neither is listed, and the rule now says a file not listed is not frozen. The first
answer is wrong, on the single file the source rule names explicitly, and no `SPEC_GAP` is owed
because the rule appears to have answered. Live code independently treats the whole directory as
frozen — `rsclib/document_harness/__init__.py:20`, *"The v3 pack is the frozen
`schema/document-assurance-v3/` directory"* — so the instruction layer and the code now disagree
about the harness's own schemas.

**What is new versus inherited.** The phrase *"existing N0 schema files"* is inherited and has been
carried unflagged through a FULL, a VERIFY and two reads. What is new is that non-membership became
dispositive (A-2) while the resolving citation was deleted (D-1). A latent ambiguity became an
affirmative licence in one hunk. That is why it is raised now and was not raised before.

**Minimum fix, subtractive or a citation — no new machinery (E6).** Either drop *"Enumerated by
blob"* and point the fourth item at its source (*"existing N0 schema files — the seven nominated in
`N0/N0-record.md`"*), or replace the category with the seven paths. Do not add a guard: the defect
is that the text is wrong, so the fix is that text changing.

### M-2 — the recorded ground of the user's ruling is false for one of the three files: `Stage-Control-Contract.md` has a live-code reader

**Location:** `HARNESS-LEDGER.md` at `6f96139` — *"三者均无活代码读者、均不属本 harness"* — and the
same claim in the commit body, *"None has a live-code reader."* **Ground truth it violates:**
`ResearchSystem/schema/stage-control-fixtures/validate.py`.

```
$ sed -n '1045,1063p' ResearchSystem/schema/stage-control-fixtures/validate.py
def generic_core_errors() -> list[str]:
    targets = [
        RESEARCH_SYSTEM_DIR / "contract" / "Stage-Control-Contract.md",
        *SCHEMA_PATHS.values(),
    ]
    banned = { "phase-specific-stage-token": …, "domain-object-type": …, … }
    for path in targets:
        text = path.read_text(encoding="utf-8")
        for name, pattern in banned.items():
            if pattern.search(text):
                errors.append(issue("GENERIC", f"{path.name}: banned {name}"))
$ grep -n 'generic_core_errors\|def main' ResearchSystem/schema/stage-control-fixtures/validate.py
1045:def generic_core_errors() -> list[str]:
1066:def main() -> int:
1310:    generic_errors = generic_core_errors()
```

The file is opened and read at runtime, from a reachable path in `main()`, and a genericity
invariant is asserted over its bytes. Recorded evidence runs it as a command —
`nodes/A0/deterministic-test-report.md`: *"`python ResearchSystem/schema/stage-control-fixtures/
validate.py` … generic-core checks PASS."*

**Precision, so this is not overstated.** The reader is not a freeze: it fails on banned P4 /
domain tokens, not on arbitrary edits, so it constrains one dimension rather than protecting the
bytes. And it is a standalone runnable, **not** wired into the five suites the commit names —
`tests/stage_control/run_tests.py` reads the stage-control *fixtures* (lines 26-27), not this
module. Both qualifications narrow the consequence; neither rescues the claim, which was
*no live-code reader*, stated flatly and twice.

**The decision that goes wrong.** The user's cost-acceptance rests on two stated grounds — no live
reader, and not this harness's. One is false for one of the three files, and it is the ground that
speaks to blast radius: an executor editing `Stage-Control-Contract.md` on the recorded premise
expects nothing to notice, when a runnable validator asserts an invariant over it. The ledger is
permanent; a future reader inherits the false premise with the ruling.

**Minimum fix.** Correct the record by appending — never by rewriting (the append-only discipline
of source rule 6) — that `Stage-Control-Contract.md` is read by
`schema/stage-control-fixtures/validate.py::generic_core_errors`, with the two qualifications
above, and put the corrected premise to the user, since the ruling was made on the stated one. No
change to `E2`'s text is implied; whether the corrected premise changes the ruling is the user's
(R5).

---

## 4. Low

### L-1 — A-3 asserts a protection I cannot find, and the same commit's own risk sentence contradicts it

Line 26-27 says *"signed instruments this harness does not govern are frozen by their own tracks,
not here."* I looked for those tracks. Every reference to the three departing files outside the
migration folder, the ledger and `contract/` itself is a README link, a plan line, or a historical
shadow-run artifact (`assurance/shadow/**` — recorded evidence, not a live guard). There are no
non-sample git hooks bearing on them beyond the thesis `repo-audit.py` and an advisory
contract-provenance check, neither of which enumerates these paths. The ledger already carries a
probe on a sibling file establishing the class — `707722d`: *"改 `content-roots.yaml` 一个字节 →
476 passed + 编译套件 OK … 说明**当前零守卫**"*. I did not re-run that probe on the three departing
files; mutating a user-signed contract to prove a negative is not a test I will run unasked.

The commit body says the truth plainly — *"an executor may now silently edit a file the user
signed"* — so `E2`'s text and its own authoring commit state opposite things.

**The downstream decision:** whether an executor stops and asks before editing one of the three.
A-3 tells them someone else has it; the ledger tells them nobody does. **Not raised to must-fix:**
the outcome A-3 mis-describes is the outcome the user knowingly chose, and the accurate fact is one
paragraph away in the same commit's ledger entry. The fix is subtraction — delete the reassurance,
keep *"a file not listed is not frozen by this rule"*, which is true and sufficient.

### L-2 — the C-3 route has now been used to undo the certified repair of an accepted FULL blocker, at zero budget, and E10 is silent on whether it may

D-1 deletes the exact wording that repaired blocker **B-2** of the FULL at `af2905c` — *"the
enumeration that scopes the E2 narrowing calls a user-signed file unsigned"*, whose ground truth
was that `amendments/2026-07-18-a1-p4-scoped.md` is signed and still hashes to its recorded digest.
The repair is visible in the diff:

```
$ git diff 8264a7d f97b348          # af2905c blob -> f054a08 blob
-  supersession-1 `68031fa2…`, existing N0 schema files, and the **signed** contracts under
+  supersession-1 `68031fa2…`, existing N0 schema files, and the **signed bytes** under
+  `ResearchSystem/contract/` — signed by any instrument, contract or amendment alike — because
```

and the VERIFY at `6798ebc` certified it: *"B-2 is paid on both halves, and the wording chosen —
signed bytes … by any [instrument]"*, verdict `REVIEWED_NO_BLOCKER`. Under the new `E2` that
amendment is outside the freeze again — not by an enumeration error this time, but on purpose.

The reversal itself is not the finding: it is disclosed in the commit, ruled by the user, and
recorded (*"不是缺陷，是方向改变"*). R5 puts the substance beyond a reviewer. The finding is the
route. E10's C-3 clause conditions only on *no round having relied*; it says nothing about undoing
what a round's accepted blocker required, and here that undoing cost no budget, carried no verdict,
and was surfaced only because the executor volunteered it.

**The downstream decision:** whether a future C-3 amendment may reverse an accepted blocker's repair
without saying so. **Not raised to must-fix:** the file's own header rules that where it is silent
on a question a round faces, `7011916` is the reference of record, the silence is not a defect, and
closing it rides the next batch under R9. This is that shape, and it is banked accordingly.

---

## 5. Observations

**O-a — the loop is at turn three, and this turn dissolved its predecessor rather than answering
it.** Read `9f2ec9a`'s `O-c` recorded that C-3 has no convergence bound and that the user ruled the
trade intended (`5760f8b`). Turn 3 is a subtraction, which is the right instinct — but it carries
two must-fixes, one of them (M-1) on the single clause of `E2` no turn of this loop has touched.
Recorded so the user has the count, not re-raised as a new question.

**O-b — what the amendment got right, re-derived rather than accepted.** The three blob literals are
live and unchanged at `HEAD`, and I resolved them against the tree rather than trusting the commit:

```
$ git ls-tree -r HEAD | grep -E 'b2dbdf752d8c|68031fa2ca31|8ad404b12b32'
8ad404b12b32…  .goals/plans/document-work-assurance-harness-v3.plan.md
68031fa2ca31…  ResearchSystem/contract/Document-Work-Assurance-Contract-v3-supersession-1.md
b2dbdf752d8c…  ResearchSystem/contract/Document-Work-Assurance-Contract-v3.md
```

The *"twelve tracked files … two in and ten out"* count is correct: `git ls-tree -r --name-only HEAD
ResearchSystem/contract/` returns exactly twelve, and exactly two of them carry an enumerated blob.
Read `9f2ec9a`'s `L-2` genuinely disappears — the `N0/N0-record.md` reference it named went out with
the definition, verified by grepping the subject for it and finding none. And the deletion does
answer that read's `M-1` on its own terms: with no definition of *signed* in `E2`, no test exists to
misapply, so the contradiction it named cannot recur in this rule.

**O-c — the defect class M-1 named survives the deletion, on the one item it left untouched (E7).**
Read `9f2ec9a`'s `M-1` was an instance of *the rule's own criterion, applied to the objects the rule
scopes, gives the wrong answer for a real file*. Deleting the criterion removed that instance. This
record's M-1 is the same class arriving through *"existing N0 schema files"*: same rule, same kind of
wrong answer, different clause. E7 asks for the class, not the instance, and the class was not swept.

**O-d — `Stage-Control-Contract.md`'s self-approval defect is unchanged and now also outside `E2`.**
Read `9f2ec9a`'s `O-d` recorded it carrying `corrective status: SIGNED` / `approval status: APPROVED`
as body list items where the scanner reads frontmatter keys. The commit re-states this as recorded,
not fixed. It remains true, and the file has now left the freeze as well. Adjacent to my subject and
reported, not raised.

**O-e — the amendment removes in-file citations, which routes more traffic to `7011916`.** D-1 took
out the source-rule citation and the `UNSIGNED successor … falls to E10's read path` carve-out. Both
were navigation. The file's header already designates `7011916` as the reference of record for its
silences; each deleted citation makes that trip mandatory rather than optional for a question the
rule used to answer in place. M-1 is the first bill for it. Reported under R5 — whether the trade is
worth it is the user's.

---

## 6. Disclosure (R4)

**Read in full:** the subject (`CONSTRUCTION-CHECKLIST.md`, 120 lines); the amendment diff
`9f2ec9a..f9a6600`, its single hunk, and the earlier `8264a7d..f97b348` and `5980421` states of `E2`;
the commit body of `6f96139` and its `HARNESS-LEDGER.md` hunk; the prior read record
`v3-checkpoint-read-9f2ec9a.md` (297 lines); `v3-harness-review-contract.md`, a 6-line stub
redirecting to the subject, which is therefore both my standing instruction and my subject;
`generic_core_errors` and `main` in `schema/stage-control-fixtures/validate.py`; the active
`pre-commit` hook at `D:/Thesis/.git/hooks/pre-commit`.

**Sampled:** `v3-review-full-af2905c.md` — heading list, `B-2` in full, `§2.1`; `v3-review-verify-
f054a08.md` — the `B-2` disposition and the verdict section. `7011916`'s retired operating contract
opened only at rule 5 and its neighbours, which is the one place this record depends on it, and it
is quoted from the fetch rather than from the prior read's quotation. The ledger hunks of `707722d`,
`e56af0d`, `25f2916` read as added lines only. `N0/N0-record.md` by grep for `schema` plus lines
78-84.

**Probed only:** the search for guards over the three departing paths — a repo-wide grep excluding
the migration folder, ledger and `contract/`; a `.py`-scoped grep for runtime readers; the hooks
directory of the real common gitdir. Absence found by grep is weak evidence of absence, not proof,
and L-1 is written to that ceiling. `tests/stage_control/run_tests.py` by grep for the fixture paths
only; I did not execute any suite.

**Not verified.** The commit's five suite counts (151 / 325 / 39 / 20 / 29) and `repo-audit.py exit
0`: not re-run. The amendment touches two markdown files and no code, so re-running them would
measure nothing about the subject — but they are the executor's figures, unpasted, and I am not
banking them. Same for *"Frozen surface re-verified after the last change"* beyond the three blob
literals, which I did re-derive (O-b).

**Marked, not verified (R4):** that this session is fresh context — a process claim, marked as such.
That the ruling recorded in `HARNESS-LEDGER.md` at `6f96139` was put to and answered by the user; I
can see the record, not the exchange, which is R7's ceiling and not a block.

**`UNVERIFIABLE`:** whether the seven N0-nominated schemas *should* still be frozen while their seven
later siblings are not — M-1 reports that `E2` cannot express the distinction, not that the
distinction is wrong. Whether the three departing signed files should be protected: already ruled,
and R5 puts it beyond me in any case. Whether `validate.py` is executed by anything in current
practice; it is runnable and reachable, and recorded evidence shows it run, which is the whole of
what M-2 claims.
