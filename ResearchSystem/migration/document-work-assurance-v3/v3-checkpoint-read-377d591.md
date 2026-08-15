# Amendment read — Phase A brake (`377d591`)

Subject: `4ba5e9527eb85a7445f4801867534a99ac70ab81..377d5912a512207ca0643a7209860810cb203d00`
(one commit, `V3-PHASE-A-BRAKE-v1`). Round derived from the repository: the disposition batch for
the three must-fix and three low of [`v3-checkpoint-read-aa72c82.md`](v3-checkpoint-read-aa72c82.md),
which amended the checklist banner and four rules (`E2`, `E9`, `E10`, `R3`) and added `R9` —
therefore owing the read `E10` mandates. The plan's resume pointer (`:87`), rewritten by this same
commit, names this dispatch and states its purpose: *"刹车轮的 read（E10，用户路由）——它同时是刹车
是否装对的检验"*.

**This is a read, not a FULL or a VERIFY.** `R3`: a read *"is not a round at all: it spends no
budget, carries no verdict, and its output is findings tiered must-fix / low / observation in its
record."* Standing re-derived rather than accepted: `ls` of this directory returns FULL records for
`0439efe`, `9c13008`, `c6d4eb4`, `dcfb2f2` only — none of them a Phase A sha (`820b287`, `cf8e1b1`,
`aa72c82`, `377d591`) — so under the discriminator `E9` now carries, no valid independent FULL has
occurred in Phase A and this commit is a pre-submission correction consuming nothing. That matches
the label its body gives itself; it was checked, not accepted. Unlike the previous two reads, this
one did not have to open `7011916` to establish it: `E9` now states the test. That is the first
measurable effect of the amendment.

Scope taken: the five amended rules and the new banner primarily, plus the whole diff and the
permanent boundaries. `R9` is applied to this read's own output, and the findings say where.

## Subject re-derivation

| Item | Re-derived value |
|---|---|
| tip == `HEAD`, branch | `377d5912a512207ca0643a7209860810cb203d00`, `document-work-assurance-v3` |
| range contents | exactly one commit; parent is `4ba5e95`, the read record it disposes |
| changed paths | 2 (2 M) — the stabilization plan, `CONSTRUCTION-CHECKLIST.md`; classified by hand below |
| line churn | +22 / −7 (plan 2/2, checklist 20/5); `--ignore-all-space` numstat identical, so no whitespace-only edit is hiding |
| worktree | clean except untracked `ResearchSystem/docs/General-Harness-v2-Design.md` (Phase D disposition; never tracked, mtime 07-19, unchanged, not smuggled) |
| suite | `432 passed in 50.45s` — re-run; matches the claim and matches `aa72c82`'s 432 |
| repo-audit | `RESULT: clean (exit 0)` — re-run, matches the claim |
| signed blobs | plan `8ad404b12b32…` (owner re-identified as `.goals/plans/document-work-assurance-harness-v3.plan.md`, not the plan this commit edits) ✓ · contract `b2dbdf752d8c…` ✓ · supersession-1 `68031fa2ca31…` ✓ |
| user-locked oracles | `tooling/tests/document_harness/test_readme_enumeration.py` `57cecbb0…` and `tooling/tests/fixtures/expected-construction-prompt.txt` `5cf970c1…` — byte-identical at both ends of the range ✓ |
| `schema/document-assurance-v3/` + `ResearchSystem/contract/` | `git diff` empty across the range ✓ |
| checklist content lines | **74**, **21 rules** (`E1–E12` + `R1–R9`) — re-derived by the bullet's own stated method |
| trajectory at five revisions | `2b5fa28` 49 · `820b287` 51 · `cf8e1b1` 62 · `aa72c82` 64 · `377d591` **74** — the Notes' *"62 → 64 → 74"* is exact |
| compression baseline | `7011916` op 308 + rev 375 = **683** ✓; 74/683 → −89% ✓ (62/683 → −91% ✓ — both right, one is current) |

A method note, since the count is what a pending ruling turns on: the bullet states its own
caliper — *"口径 = `## Execution side` 起至文末，去标题去空行"*. Applied literally
(`awk` from `^## Execution side` to EOF, dropping blank lines and `^#` headings) it yields 74 at
`HEAD` and reproduces every earlier figure the record claims. The caliper being stated is itself
new this round and is what made the trajectory checkable.

Per-path classification: **checklist** — banner (new operative-rule-set clause), `E2` (+boundary
derivation clause), `E9` (+FULL discriminator), `E10` (−four-word parenthetical), `R3` (+tier
names), `R9` (new rule); **plan** — `:87` resume pointer rewritten, `:91` Notes deviation bullet
rewritten. Both inside the boundary as `E2` now reads. The ledger was *not* touched — that is MF-1.

### Disposition of the previous read, checked one by one

| Prior finding | Disposition | Verified |
|---|---|---|
| MF-1 `E9` self-classification with no independent criterion | fixed | discriminator restored verbatim in substance from `rev.md:133-145`; *"applied to substance, never to the commit message"* rendered as *"What consumes it is never what a commit is called"* ✓ — and it worked: this read established its own standing without opening `7011916` |
| MF-2 the read-recursion bank rule was dropped | fixed | `R9` added; against `rev.md:340-346` the restoration is faithful (see fidelity note) ✓ |
| MF-3 plan Note states a figure this batch invalidated | **partly** | the figure was re-measured to 74/24 rather than patched to 64/14 — better than the minimum fix, and correct. But the displaced baseline survives in the same bullet (L-1), the resume pointer carries a third number (L-2), and the option built on the old figure was not re-checked (MF-2 below) |
| L-1 `"tiered findings"` mandated, tiers never named | fixed | `R3` now names must-fix / low / observation ✓. The previous read banked this one under the rule it was asking to have restored; taking it here is the brake's first actual operation, as the commit body says |
| L-2 `E10` carried rationale into a rules file that declares rationale absent | fixed | the four words *"(they route every reviewer)"* are gone ✓ |
| L-3 plan freeze-surface declaration load-bearing but outside `E10` | fixed, with reach | the `E2` clause landed as the reviewer's own second option — and then added *"a round's own card"*, which is where change boundaries live (L-3 below) |

### Fidelity of the two restorations, against source at `7011916`

- **`E9` discriminator** — source `rev.md:133-145`. Carried: the question, both branches, the
  substance-not-name rule. Not carried: *"Consumes the fix"* on the yes-branch (kept: *"it obliges
  the VERIFY"*), and the two named historical escapes (V3-N0, V3-N1), whose absence is the banner's
  declared policy on rationale. Both recoverable from the rule's own first sentence and from
  `7011916` — banked, see O-5.
- **`R9` bank rule** — source `rev.md:340-346`. Carried in full: the wording-level definition with
  all four exclusions, the recoverability half, the name-the-decision test, and the ride-the-batch
  disposal. Changed: *"spawns no fix round and no read of its own"* → *"spawns no round and no
  read"*, a widening from fix-rounds to all rounds; and the attribution (*"user ruling 2026-07-27,
  ending a 2→1→0 read recursion"*) is dropped, consistent with the banner. Neither changes an
  actor's action — banked.

## Must-fix

**MF-1 — `HARNESS-LEDGER.md` is one round behind, and it is the file a cold session is routed to
first.** Ledger `:19`: *"**状态 (2026-07-28)：deletion-first stabilization 执行中——Phase A 收口。**
链：收缩 `820b287` → checkpoint read `3743849` → 修复 `cf8e1b1` → amendment read `1ddece7` → 本收口
轮"*, and `:23`: *"**NEXT = Phase B 搬家（plan Step 4）的 preview card；其前只欠对本收口轮 checklist
两行的短 read**"*. That short read exists — its record is `v3-checkpoint-read-aa72c82.md`, committed
at `4ba5e95`, which is this commit's parent. So the ledger states that the one thing standing
between the project and Phase B is already discharged. The plan's resume pointer, edited by this
same commit, says otherwise: the owed read is the brake round's. The two live pointers disagree, and
the wrong one is the one that owns pointers — the ledger's own header (`:17`) scopes it to
*"当前指针"*, and the repository's `CLAUDE.md` routes every new session through `.goals/LEDGER.md`
to this file before any other harness state. The date on the stale line reads `2026-07-28`, so a
cold reader gets no staleness cue. **Failure shape:** a fresh session opens the ledger, sees the
outstanding read discharged, and opens Phase B's preview card — relying on an instruction-layer
amendment that has not passed its `E10` read. That is the exact sequence `E10` exists to prevent,
and it is reachable today. This is also a recurrence, not a first: MF-1 of read `cf8e1b1` was the
same file and the same line, fixed one round ago as an instance; the class is that the pointer goes
stale in every round that does not touch it. **Minimum fix:** ledger `:19-23` — extend the chain
with `aa72c82` → `4ba5e95` → this round, and repoint NEXT at this read, matching `plan:87`.

**MF-2 — the pending user ruling's first option became arithmetically impossible in the same commit
that corrected the number it rests on.** `plan:91` closes: *"**处置待用户裁**：接受实测值并把
Acceptance 改成 ≤65，或指定砍哪几条（砍=丢已复原的义务）。未擅自改 Acceptance."* The measured value
stated at the head of that same bullet is now **74**. *"接受实测值"* and *"≤65"* cannot both hold —
accepting the measured value and writing ≤65 would ratify an Acceptance the file already violates
by 9 lines. The ≤65 offer was authored when the count was 62 and survived when it was 64; this
commit moved it to 74 and re-checked the figure but not the decision built on it. `plan:87` routes
the user here for the ruling (*"待用户裁：checklist … vs Acceptance ≤50（见 Notes）"*), so the option
would be taken from this line. `E3` is the rule the round applied to the number and not to its
consequent: *"a figure is invalidated by any later change to what it measures."* Not bankable — the
downstream decision is nameable and is the user's own. **Minimum fix:** one number on `plan:91` —
≤65 → ≤75, or phrase the option as *"改成实测值"* so it cannot go stale again.

## Low

- **L-1 — the deviation bullet keeps both the corrected baseline and the one it displaced.**
  `plan:91` states *"对比基线不变：两份契约 683 行 → 74 行，−89%"* in its new parenthetical and then,
  four clauses later, the untouched *"对比基线：两份契约 683 行 → 62 行（−91%）"*. Both are
  arithmetically correct (683 re-derived as 308 + 375; 74/683 → −89%, 62/683 → −91%); only one is
  current. **Bankable under `R9`** — the accurate figure is adjacent, no check outcome, permission,
  obligation or verdict path turns on the compression percentage, and I can name no decision that
  goes wrong. Recorded, not fixed, as `R9` requires. **Minimum fix if taken:** delete the second
  sentence.
- **L-2 — the resume pointer carries a third number.** `plan:87`: *"待用户裁：checklist 72 行 vs
  Acceptance ≤50（见 Notes）"*. Re-derived by the bullet's own method at five revisions — 49 / 51 /
  62 / 64 / 74 — 72 matches no revision of the file. **Bankable under `R9`**: the line itself says
  *"见 Notes"*, and the Notes are right. **Minimum fix if taken:** 72 → 74.
- **L-3 — the new `E2` clause reaches past freeze surfaces into the boundaries `E8` and `E9` bind
  the executor to.** `E2`: *"A boundary declared anywhere else — a plan's freeze surface, a round's
  own card — is derived from this rule and never independently authoritative."* `E8` obliges the
  executor to *"stay inside the round's declared change boundary"*; `E9` says *"Exceeding an
  approved fix boundary requires saying so, never silently."* A round's card is where a change
  boundary is declared, not a freeze surface — so read literally, `E2` strips independent authority
  from precisely the declaration `E8` makes binding, and an executor could argue that leaving the
  card's declared paths is unremarkable so long as no frozen byte was touched. That is a permission,
  so this is not bankable. It is low rather than must-fix because the clause sits inside the
  frozen-bytes rule and `E8`'s obligation stands adjacent and unqualified, so the working rule is
  recoverable. **Minimum fix:** one word — *"A **freeze** surface declared anywhere else…"* — or
  exclude `E8`/`E9` boundaries by name.
- **L-4 — the banner routes silences to `R9`, whose stated test sends the consequential ones back.**
  Banner: *"the silence is not a defect, and closing it rides the next batch under `R9` rather than
  opening a round."* `R9`: *"Name the downstream decision that goes wrong if it stays unfixed; if
  none can be named, it rides the next batch…"*. The two of this batch's own predecessors are the
  test case: MF-1 and MF-2 of read `aa72c82` were both silences, both had nameable decisions, and
  both were taken as must-fix and fixed here. Under the banner they were not defects at all; under
  `R9`'s test they do not ride. A determinate reading is available — *"the silence is not a defect"*
  is categorical and more specific than the cross-reference — which is why this is low. But the
  cross-reference points at the one rule that contradicts it, and this read is the first occasion to
  apply either. **Minimum fix:** delete *"under `R9`"* (the banner then carries its own disposal),
  or name the silence class inside `R9`.
- **L-5 — an `E10` instruction-layer file now misstates the rule inventory.**
  `document-harness/README.md:24`: *"E1–E12 execution, R1–R8 review"*, with `R9` live since this
  commit; `plan:63` carries the same *"review R1–R8 [起草时为 R1–R7]"*. **Bankable under `R9`**: the
  row links to the checklist, which is the accurate record; no actor's action changes; I can name no
  downstream decision. Recorded here and riding the next batch touching this layer. Checked and
  worth stating: the user-locked README oracle pins *schema-file stems*, not rule ranges
  (`test_readme_enumeration.py`, byte-identical across the range), so nothing catches this class.

## Observations — no fix owed

1. **The banner makes 683 retired lines the reference of record, so the compression reduced what is
   *stated*, not what *governs*.** The pending Acceptance ruling (MF-2) is a decision about the size
   of the stated layer while the governing layer is now 74 + 683. Two figures for context, both
   re-derived: the `≤50` Acceptance has been met exactly once, by the never-effective draft at
   `2b5fa28` (49 lines), and every read-driven restoration since has raised the count. `R5` bars me
   from concluding what to do with that; the shape is reported.
2. **Phase A still has no FULL, and `E9` as restored makes that structural rather than incidental.**
   With no FULL, every batch is a pre-submission correction consuming nothing, and the file places no
   bound on how many may occur; four commits have now touched the checklist under that status.
   Carried from read `aa72c82` observation 1 — the amendment made the rule explicit without bounding
   it, which is a different thing from closing it.
3. **`R9` sits between `R3` and `R4`, out of numeric order.** Topically placed next to the read
   definition it qualifies. Bankable; noted only because a reader scanning `R1…R9` in sequence meets
   it early.
4. **`E9` is now both the prohibition on self-classification and the test the executor applies to
   itself.** This commit's body opens by applying it (*"no FULL exists for any Phase A sha"*). The
   working division is recoverable — `E8` has the executor name the kind, `E9` has the review side
   re-derive and never accept the label — and it held here. Recorded because MF-1 of the previous
   read named this tension and the amendment mitigates rather than removes it.
5. `E9` drops the source's *"Consumes the fix"* from the yes-branch (`rev.md:137`). Recoverable from
   the rule's own first sentence. Banked.
6. Carried unchanged, all re-checked this round: `plan:6` still reads `status: planned` with Steps
   1–3 ticked; `dispatch.py:362` still attributes the numbered `§n` form to
   `v3-harness-review-contract.md`, now a five-line stub with no sections; the ledger pointer block
   is 53 non-blank lines against its own *"≤ 30 行"* (`:17`) — unchanged this round because the
   ledger was not touched, which is MF-1.
7. `R3`'s tier mandate is stronger than its source: `rev.md:350-356` calls the report format *"a
   recommendation, not a rule … A report in a different shape violates nothing"*, and `rev.md:367`
   gives the tier vocabulary as observed practice. The mandate predates this commit (`aa72c82`
   already said *"tiered findings"*); this commit only named the tiers, which is what the previous
   read asked for. Reported, not concluded (`R5`).

## Negative results by dimension

Checked, found nothing: all three signed blobs intact, and the plan blob's owning path
re-identified from scratch rather than assumed (it is `document-work-assurance-harness-v3.plan.md`,
a different file from the one this commit edits); both user-locked oracles byte-identical across the
range — verified at their real paths under `tooling/tests/document_harness/` and
`tooling/tests/fixtures/`, after a first pass at guessed paths returned a vacuously empty diff;
`schema/document-assurance-v3/` and `ResearchSystem/contract/` diff-empty; no whitespace-only or
invisible edit (`--ignore-all-space` numstat identical to plain); the two changed files are the
whole change; the `E10` deletion removes only the four words the previous read named and leaves the
clause's scope intact; the banner's new clause does not collide with `SPEC_GAP` (`E2`/`R3`) — that
verdict is about a gap in the round's own spec, not about the checklist's silence, so the banner
does not retire it; `7011916` still resolves and still carries both contracts in full (308 + 375
lines re-extracted); the stated caliper reproduces every count in the record; the commit body's four
verification claims (suite, audit, blobs, tree/oracle diffs) all reproduce. Also checked against
`R2`'s chat-only clause: the user ruling that shaped this round (*"install the brake and then verify
it with one more read rather than … waive the read"*) is not chat-only — it is in the commit body,
which is committed and greppable — so it is not a finding, though the ledger's rulings block is
where it would be found by anyone not reading `git log` (see MF-1).

## Guard probe (E4/R8) — run as a negative control

No test in the repository reads any changed file: `grep -rn "CONSTRUCTION-CHECKLIST|HARNESS-LEDGER|
harness-deletion-first" ResearchSystem/tooling/` returns nothing. So the probe was aimed at this
commit's own new bytes, to measure what its green evidence is worth:

- **Deleted `R9` and the whole new banner clause** — the two rule blocks this round adds — and re-ran
  both instruments: suite **`432 passed in 56.34s`**, unchanged; repo-audit **`RESULT: clean (exit
  0)`**, unchanged. The 432-green and audit-clean claims therefore carry *zero* information about
  the bytes this round adds. Measured, not assumed, and now measured on the new rules specifically
  rather than on `E10` as last round.
- **Negative control** — appended one markdown link to the checklist whose target
  (`./NO-SUCH-FILE-xyz.md`) does not exist; the link syntax is described rather than reproduced
  here, because reproducing it makes this record itself fail the audit — observed, not assumed.
  repo-audit went **RED**, `[!!] Broken markdown links: 1`, `RESULT: hard issues found (exit 1)`. So the
  audit does read this file, and the first probe's green is a real negative rather than an unreached
  guard. Worth pairing with the count: `grep -c "](" CONSTRUCTION-CHECKLIST.md` = **0** — the file
  contains no markdown links at all, so the only property the audit can bind here is currently
  vacuous.
- Restored both files from sha256-checked scratchpad copies, never `git checkout --`:
  `cbe75add2e66…` (checklist) and `ed5b609f7792…` (plan) before and after; `git status --short`
  back to the single known untracked path; audit back to `exit 0`.

Binding force, not sufficiency (`R4`): the audit binds link resolution only, and on this file that
set is empty.

## Coverage

**Read in full:** `CONSTRUCTION-CHECKLIST.md` at `HEAD`; the full diff; both retired contracts at
`7011916` (683 lines, re-extracted — `rev.md` §3, §12, §13 closely, the rest scanned);
`v3-checkpoint-read-aa72c82.md`; the stabilization plan's Acceptance, Resume pointer and Notes;
`HARNESS-LEDGER.md`; `test_readme_enumeration.py`.
**Sampled:** `document-harness/README.md` (rows 22-28); `EXECUTION.md` / `REVIEW.md`
(checklist-referencing regions); `plan:63` (Step 2); `.goals/LEDGER.md` (router rows);
`dispatch.py` (contract-referencing regions); the checklist at four earlier revisions (rule
inventory and content count only).
**Probed only:** the 432-test suite (run twice — clean and mutated); `repo-audit.py` (run four times
— clean, mutated, negative control, restored); the checklist and plan under mutation.

**Recomputed, never accepted as reported:** the range and its single commit, parent, numstat and
whitespace-insensitive numstat; every changed path classified by hand; all three signed blobs and
the path that owns each; both oracle blobs at their real paths; schema and contract tree diffs; the
checklist's 74 content lines and 21 rules, and the same count at four earlier revisions; the stated
caliper itself; the 683-line baseline from its two components and both percentages; the absence of
any Phase A FULL record; suite count and audit exit; the identity of the untracked file.

## Ceilings

The claim that this round ran in a fresh context is marked, not verified. The user's approval of
this batch's boundary and the ruling that shaped it are visible to me only inside the commit body,
not as an independent repository fact — `R7` applies: stated as a ceiling, not treated as a block.
`UNVERIFIABLE`, not folded into supported: whether the brake is *sufficient* is not establishable
from one read. What this read can report is what it measured. The unbounded class the brake targets
did close — no finding above is of the form *"the live text does not say X"*, and the two silences
that would previously have been raised (`E9`'s dropped *"Consumes the fix"*, `R9`'s dropped
attribution) are banked in the observations instead. Three of the five low findings were banked
under `R9` rather than tiered up, which is the brake operating on this read's own output. What the
brake does not touch is where the two must-fix landed: a pointer that was not updated, and a
decision that was not re-checked after its number moved. Both are `E3`'s defect class, not the
recursion's — and whether that is the shape to work on next is yours to decide, not mine (`R5`).
