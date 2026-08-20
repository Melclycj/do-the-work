# Checkpoint read — Phase B2 instruction-layer amendment (`ff05ea3`)

Subject: `604ee27940e3cedb400b83317dd908134ccbbafb..ff05ea3018a544d1a141539acf2df8f83c8ca850`
(two commits: `a8113d4 V3-PHASE-B2-AMENDMENT-v1`, self-named *candidate*; `ff05ea3
V3-PHASE-B2-TRACKER-v1`, self-named *pre-submission correction*). Round derived from the
repository: Step 2/6 of `.goals/plans/harness-memory-lessons-integration.plan.md` (Phase B2,
the expansion of `harness-deletion-first-stabilization` Step 4.5). The read it owes is that
plan's Step 6 — *"suite + audit + 冻结面 → commit → dispatch → 用户路由 read"*.

**This is a read, not a FULL.** `E10` requires each instruction-layer amendment to pass an
independent read whose subject is the amendment text itself, and says it "is never banked as
the round's FULL"; `R3` says a read "is not a round at all: it spends no budget, carries no
verdict". The reference of record is the same: retired review contract §12 (`7011916`)
schedules the amendment checkpoint read under the user's `ADOPT_DOCUMENT_V3` ruling (N3
record §8, N3-R10) — so performing it is authorization I can see, not initiative (`R7`
needs no ceiling here). Phase B2's FULL is therefore unspent. Findings are tiered
must-fix / low / observation. If the user instead classifies this dispatch as the round's
FULL, the corresponding verdict on the must-fix set below is `CHANGES_REQUIRED` — but that
classification is the user's, not mine.

## Subject re-derivation

Every figure below was produced by a command run in this session, immediately before writing.

| Item | Re-derived value |
|---|---|
| tip == `HEAD`, branch | `ff05ea3018a544d1a141539acf2df8f83c8ca850`, `document-work-assurance-v3` |
| changed paths | 6 (5 M, 1 A) — classified by hand below |
| worktree | `?? ResearchSystem/docs/` only — untracked, Phase D disposition, named at plan L45; not smuggled into the subject |
| suite | `432 passed in 52.82s`, re-run; `432 passed in 47.81s` again after my mutation probe restored |
| repo-audit | `RESULT: clean (exit 0)` from the repository root, re-run |
| plan blob | `8ad404b12b3242e700d0ad215048dffccada7d9c` ✓ |
| contract blob | `b2dbdf752d8c155e4c65b14b5f420b880b8184a1` ✓ |
| supersession-1 blob | `68031fa2ca31272e31da0d42a9a02189d28fcc21` ✓ |
| `ResearchSystem/contract/` + `ResearchSystem/schema/` | `git diff --name-only 604ee27..ff05ea3 --` on both: empty ✓ |
| user-locked oracle 1 | `5cf970c17ad509e7517f59fb9421a2de4cb9bd68` at `604ee27` **and** at `HEAD` — positive identity, not an empty diff ✓ |
| user-locked oracle 2 | `57cecbb0c467485b692308ebb13cc64dfeb630b7` at `604ee27` **and** at `HEAD` ✓ |
| E3 edit | +38 words appended; longest common prefix = all 29 base words; **0 words removed** ✓ |
| R3 edit | +30 words inserted after base word 15; 76-word suffix identical; **0 words removed** ✓ (`E10` "additive or subtractive, never re-typed" holds mechanically, not by eye) |
| new triage decision digest | `56ef90d3…72d58` stored == `sha256` of the target issue's current bytes ✓ |
| `check_triage(new decision, its issue)` | `ok=True`, `issues=()`, `triage_route` → `CORE_CANDIDATE` ✓ |
| five pre-existing triage digests | all five **MISMATCH** current bytes — the executor's disclosed finding, independently reproduced |
| commit shape | linear `604ee27→a8113d4→ff05ea3`; author date == commit date on both (no amend); `%(trailers)` empty on both; titles match `V3-<ROUND>-v1`; each body names its kind ✓ (`E8`) |
| push | `git rev-list --count origin/main..HEAD` = 210; neither commit on any remote ✓ (`E8` no push) |
| budget | no `v3-review-{full,verify}-*.md` exists for any sha in this range → no independent FULL has occurred → `ff05ea3` is correctly a pre-submission correction consuming nothing (`E9`) ✓ |
| R9 rider provenance | `R9` entered the checklist at `377d591` (`V3-PHASE-A-BRAKE-v1`); README:24 was corrected to `R1–R9` at `cf040af`; both stubs still said `R1–R8` at `604ee27` ✓ |
| banked item L-5 (read `377d591`) | named `README.md:24` and `plan:63`; both now correct at HEAD. Remaining `R1-R8` hits outside review records are WorkSpec *requirement* numbers in `w1-r1`/`p3-corr`, an unrelated namespace ✓ |

Per-path classification (by hand, `R2`): plan (tracker + judgment table + verification block +
Notes), HARNESS-LEDGER (NEXT pointer + three ruling bullets), CONSTRUCTION-CHECKLIST (`E3`
append, `R3` insert), both retired stubs (`R1–R8`→`R1–R9`), new ISSUE_TRIAGE decision JSON.
All six sit inside the round's declared boundary — instruction layer + this phase's triage
decision + the round's own tracking. `E2` frozen bytes untouched.

## Guard binding (`R8`)

Nothing in the suite reads the bytes this round changed. The one named exception to the
layer's "no test reads it" property — `test_readme_enumeration.py` — pins README *schema
stems*, not rule ranges; the golden fixture pins the dispatch prompt, which references the
review-contract stub by **path**, not by content. So the class that let both stubs sit at
`R1–R8` since `377d591` is untouched, and this read is the only instrument over the change.
That is the design (README L28; `E10`), stated here rather than assumed.

Mutation probe on the one guard that touches this round's surface — the fixture pinning the
stub path, which is what makes the stub edit safe:

- **Control first.** `…::ConstructionDispatchPrompt::test_the_prompt_is_exactly_the_golden_file`
  → `no tests ran in 0.04s`. Wrong class name; a green here would have been empty. Correct node
  `…::ConstructionRoundsGenerateToo::test_the_prompt_is_exactly_the_golden_file` → `1 passed`.
- **First mutation was worthless and is reported as such.** Replacing the first occurrence of
  the stub path hit a *comment* at `dispatch.py:362`; test stayed `1 passed`. A mutation in dead
  text proves nothing, the mirror of `R8`'s crash warning.
- **Real mutation.** `CONSTRUCTION_ROLE_INSTRUCTION` (`dispatch.py:492`, the `{charter}`
  substitution) → `…-MUTANT.md`, golden file untouched → `1 failed`, on a genuine rendered-text
  diff, not an error. The guard binds.
- **Restore.** From a scratchpad copy taken before mutating (`E4`, not `git checkout --`):
  `sha256 106d99d8b618fecfe6f76d48f9d65752b7aaa6825e9ac43d364c2db2107dcbac`, equal to baseline;
  `git status --porcelain` back to `?? ResearchSystem/docs/` alone; suite `432 passed`.

## Must-fix

**MF-1 — `R3`'s new sentence enumerates an implementation the instruction layer is not part
of, on a round that is nothing but instruction layer.** `CONSTRUCTION-CHECKLIST.md:76-78`:
*"Lead with the implementation — whether the code, schemas and tests do what they claim and
whether the guards bind; process and record conformance is a boundary check, run second."*
This subject contains no code, no schema and no test — by design, under the recorded ruling
that *"B2 轮 authors 零个可执行字节"*. The leading term therefore has no referent here, while
the second clause demotes the only surface that exists. The ground truth it sits against is
the reference of record the checklist banner routes to: retired review contract §12
(`7011916`) — *"§1 applies to prose exactly as to work — the reader's question decides the
yield — so the read must have the text as its subject, never merely as its manual."* The new
sentence ranks prose below code without saying so, and a reviewer working from the checklist
alone (which is the point of the checklist) never sees §12. This is not a corner case: the
record holds 11 checkpoint reads + 2 cold reads against 5 FULLs + 3 VERIFYs, and reads are
exactly where instruction-only subjects land. **Minimum fix:** name the layer inside the
existing enumeration — *"whether the code, schemas, tests **or instruction text** do what they
claim"*. One insertion, no new machinery, `E6`-clean. Counter-reading I owe you: the sentence
sits inside the verdict rule, and reads carry no verdict, so it can be argued the sentence
never binds a read at all — which would make it silent on the shape it was written during.

**MF-2 — Step 3 is checked closed against a standard the same file records the user as
rejecting.** Plan Notes §用户思路 item 2 states the completion criterion for atom
`feedback-prose-claims-derive-or-omit` verbatim: *"完成标准**不是「加了一条 instruction」**，而是
相关自由文本已被生成字段替代或删除"*. What shipped is precisely an added instruction — Step 3
closes with *"→ 即 `E3` 的追加句"* — and Acceptance L109 restates the criterion as *"C 规则生效"*,
which is the thing the user said is not the standard. The competing ruling is also in the
repository (`一次性搬迁不允许 executor 出守卫`; zero executable bytes this round), so this may be
a deliberate trade — but nowhere is it recorded as one, and `R5` leaves that conclusion to you,
not me. **The decision that goes wrong if it stays unfixed:** Step 4 is next, it deletes and
rewrites the memory atoms, and memory is not under version control. Closing Step 3 on the
weaker standard retires that atom's prose while the mechanization it names never happened, with
no committed record that the substitution was chosen. **Minimum fix:** record the ruling —
either that the added sentence discharges atom #4 (with the trade named), or that Step 3
reopens — *before* Step 4 runs. No code either way.

## Low

- **L-1 — the evidence for the two user-locked oracles is an absence, not an identity.** Plan
  §本轮验证: *"`git diff --stat 604ee27 -- <两个 user-locked oracle>` （空输出 = 逐字节未动）"*,
  paths elided. An empty diff is also what a mistyped path returns: my own first attempt used
  `tooling/tests/test_readme_enumeration.py`, which does not exist, and exited 0 in silence —
  the real path carries `document_harness/`. The fact is true (I re-derived it as blob equality,
  table above) and plan L44 carries both correct paths, so this is record form, not a false
  claim. But it is unrunnable as written and indistinguishable from having checked nothing, on
  the one surface the user reserved to their own intervention. **Fix:** record the two blob
  hashes.
- **L-2 — `E4`'s restore method was substituted silently.** The probe is recorded as restoring
  *"从 `git show HEAD:<path>` 字节还原后 sha256 与基线相同"*; `E4` prescribes restoring from
  sha256-checked scratchpad copies. The substitution is safe **only because** `dispatch.py` was
  clean at HEAD — a precondition `E4`'s own method does not need and the record does not state.
  Applied to a file the round had also edited, the same shortcut silently reverts the round's
  own work while the sha256 check still passes against the wrong baseline.
- **L-3 — the plan's front-matter `status:` is stale in the commit whose sole purpose was the
  tracker.** L6 still reads *"Step 0/1 闭合…Step 2 等 preview card 确认"* while Steps 2, 3, 4b, 5
  and 6 are all `[x]` below it. `ff05ea3` moved Step 6 and the Resume pointer and left the
  status line three steps behind — the same class as the plan's own Why-table entry *"ledger
  指针连续两轮落后"*. Wording-level under `R9` (the Resume pointer carries the truth, and the
  file's own resume instruction says to read it in full), so **banked, not a round**.
- **L-4 — `check_triage clean` is cited for a binding it cannot establish.** Placed in
  §本轮验证 as evidence for the new decision, the function checks phase, route membership,
  presence of a target path, `work_id` equality and schema — never the digest, and never that
  `target.harness_issue_ref.path` designates the issue it is being checked against. Negative
  control run here: `check_triage(new decision, issue-p3-corr-template-write-text-newline)` →
  `ok=True, issues=()`. Since all eight p3-corr issues share `work_id`
  `p3-inventory-count-correction`, the one discriminating field discriminates nothing in this
  run. The decision itself is sound — its digest matches, recomputed above — but the cited
  check is not what establishes that.

## Observations — no fix owed

1. **`R3`'s new priority and `R2` order different axes, and nothing says so.** `R2` makes
   re-deriving round, budget, authorization and obligations from the repository the precondition
   for knowing what the subject *is*; the new sentence tells the reviewer that "process and
   record conformance" runs second. Read together, "run second" can be taken as ranking `R2`'s
   own work below the code it is a precondition for.
2. **The rule-range enumeration now lives in three hand-maintained copies** — README:24 and both
   stubs — with no instrument over any of them. This round synced all three; the class that let
   them drift from `377d591` to `604ee27` is unchanged, and the user ruling that declined `R10`
   did so precisely to avoid *"又一处会漂的规则范围枚举"*. Shape reported per `R5`; the question
   and the conclusion are yours.
3. **The parked immutability item is wider than digests.** The ledger parks *"`check_triage`
   不核 digest"*. As shown in L-4 it also never checks path→issue identity, so the binding
   between a triage decision and the issue it routes is currently carried by a field nothing
   verifies. Worth folding into the same ruling rather than a second one.
4. **Reflow residue.** `CONSTRUCTION-CHECKLIST.md:81` is 108 characters against a median body
   width of 89, and it is the only line in the file over 96 — the tail of the `R3` insertion.

## Coverage and honesty ceilings (`R4`)

- **Read in full:** `CONSTRUCTION-CHECKLIST.md`, `document-harness/README.md`, `EXECUTION.md`,
  `REVIEW.md`, both retired stubs, `HARNESS-LEDGER.md`, the complete `604ee27..ff05ea3` diff,
  the new triage decision and its target issue, `rsclib/document_harness/issues.py`,
  `test_readme_enumeration.py`, `expected-construction-prompt.txt`, and
  `harness-memory-lessons-integration.plan.md` (L1–55 and L104–121 directly; L53–140 via the
  diff, which covers every changed hunk).
- **Sampled:** the retired review contract at `7011916` — §12 in full plus targeted searches for
  a priority rule and for instruction-layer treatment. I did not read its 683 lines end to end,
  so a silence I attribute to the checklist could in principle be closed somewhere in it that I
  did not reach.
- **Probed only:** `dispatch.py` (the two constants and the comment I mutated),
  `test_dispatch.py:380–424`, the five pre-existing triage decisions (digest recomputation and
  route/phase/work_id fields only — not their prose), the deletion-first plan (L60–66 and
  targeted searches).
- **Not verifiable from the repository:** everything on the memory side. The judgment table's
  "delete 8 / rewrite 3", the `MEMORY.md` 24→16 line claim and the issue's "24 atoms" are
  `UNVERIFIABLE` here by construction — memory is outside the repository, which is the very
  property `issue-p3-corr-harness-knowledge-in-memory` names. Step 4 will not be reviewable
  either; the user ruled that explicitly, and this read does not weaken that ruling, it records
  its consequence.
- **Process claims are marked, not verified:** that `a8113d4` was authored before `ff05ea3`
  rather than reconstructed, and that this read ran in a context independent of the executor's,
  have no evidence lock. Author/commit-date equality and linear parentage are consistent with
  the first; nothing establishes it.
- A mutation proving a guard binds is not a claim that its force is sufficient, and this read
  certifies nothing about the memory migration it precedes.
