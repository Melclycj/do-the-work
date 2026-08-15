# Targeted VERIFY — `a7bb1d6..7a08265` (Batch A / A1, the round's one approved fix + its errata)

| | |
|---|---|
| round | VERIFY, construction-side (`CONSTRUCTION-CHECKLIST.md` E1–E12 / R1–R10) |
| subject | `a7bb1d6a1f489be22ba0482e9fceeba71e15bd3c..7a08265206de436f46b92bd912b1d947f9379f2b` |
| range content | three commits: `ed0b120` (`V3-REVIEW-RECORD-A1-a7bb1d6-v1`, kind: review record) · `fd058aa` (`V3-REVIEW-FIX-A1-B1-v1`, kind: review fix) · `7a08265` (`V3-REVIEW-ERRATA-A1-f1-f4-v1`, kind: errata) — 5 files, +604 / −4 |
| answers | FULL `v3-review-full-a7bb1d6.md` — blocker **`B-1`** (minimum fix **(a)**) and findings **`f-1`**–**`f-4`**; `f-5` declared uncorrectable |
| **verdict** | **`REVIEWED_NO_BLOCKER`** |
| findings | 3 requiring a user ruling · 5 low · 4 observations |
| record | this file; the execution side commits it (`R6`) |

**What this verdict does and does not mean.** `B-1` is closed, and closed by the mechanism it named:
the decision log is now a layer member, the guard demonstrably reaches it (mutation below), and the
dispatch → charter → `E10` chain now delivers the obligation — this session travelled that chain and
was told to read the file. Of the errata's four re-measurements, three reproduce **exactly** and one
is off by 176 in two of its three units. `VERIFY`'s vocabulary has no value meaning *the repair
created new questions*, and it created three: closing `B-1` by route (a) subjected a registry the
user writes into to machinery designed for nine slow-moving rule texts, and none of the three
resulting collisions is closed by the bytes that landed. They are findings, not blockers, because
each is answered by one user ruling and none of them makes the landed repair wrong.

---

## 1. What this round is, re-derived (`R2`)

Nothing below is taken from the dispatch, which carried the range and nothing else.

| Question | Answer | Where I read it |
|---|---|---|
| Round | **Batch A / A1** — its FULL leg, fix leg and errata | `ed0b120`/`fd058aa`/`7a08265` bodies; `HARNESS-LEDGER.md:92-96` |
| Governing instructions | `CONSTRUCTION-CHECKLIST.md` (E1–E12 / R1–R10); reached via the stub the dispatch names (`dispatch.py:508-510` hands `v3-harness-review-contract.md`, whose `:3` points here) | stub `:3`; checklist header `:9-12` |
| Which leg this is (`E9`) | `E9`'s test is "has a valid independent FULL already occurred?" — **yes**: the FULL's record landed at `ed0b120` (subject `dbec65f3..a7bb1d6a`, `CHANGES_REQUIRED`). So `fd058aa` is the one user-approved fix and **this is the obliged targeted VERIFY**. Budget is exhausted after it | `ed0b120` body + record `:1-6`; checklist `E9` |
| Verdict domain | VERIFY → `REVIEWED_NO_BLOCKER \| SPEC_GAP` (`R3`) | checklist `R3` |
| Authorization | Route (a) is asserted in `fd058aa`'s body ("用户 2026-08-08 裁 `B-1` 走最小修 (a)") and **nowhere else in the repository** — grep of both plans, the ledger, the decision log, the rider bank and the journal returns no record of it (`V-2`) | `fd058aa` body; grep |
| Obligation | Cover the accepted findings, the whole repair diff, and the permanent boundaries however narrow (`R3`) | checklist `R3` |
| Ledger state | A1 closed, step 8 (this review) owed, **A2 forbidden to open before it** | `HARNESS-LEDGER.md:92-96` |

**Ceiling (`R7`).** I see `fd058aa`'s claim of the route-(a) ruling and the 2026-08-04 ruling it and
the errata lean on; I cannot verify the conversations. "Fresh context" is marked, not verified
(`R4`). Worktree at `7a08265`, `git status --porcelain` empty before and after every probe.

---

## 2. Implementation (`R3` — lead)

### 2.1 Does the repair close `B-1`?

Three sites changed, not the two the FULL's (a) named — `E10`'s sentence, `layer_path_check.LAYER`,
and `test_precommit_checks.LayerMembership.EXPECTED`. The third is mechanically forced and the
commit says so (`ob-3`). Checked, each against the thing it is supposed to bind:

- **Count and enumeration moved together.** `E10:75` now says "these **ten** paths" and the sentence
  names exactly ten, in `LAYER`'s order. The `C1` dangling-neighbour shape is avoided, and the sweep
  is clean: across all ten members the only surviving `nine|九成员|九元组` hit is nothing — the one
  match is the amended "ten paths" line itself. Two stale copies live outside the layer:
  `.goals/plans/e2-verb-e10-pin.plan.md` (a closed round's plan, correctly left alone as a derived
  statement) and `HARNESS-RIDERS.md:15` (`V-4`, a live row).
- **All ten members resolve** from the repo root, and the new member is not a landmine: fed the whole
  of `HARNESS-DECISIONS.md` to `unresolved_tokens` as if every line were newly added → **0**
  findings; its archive likewise **0**. So the next commit touching it is not blocked by the guard
  it just joined. (`HD-17`'s seven directory tokens: one carries the `ResearchSystem/` prefix and
  resolves; six are bare and resolve from the file's own directory, which for a member sitting at
  `ResearchSystem/` is what the guard's relative-convention branch is for.)
- **Reachability, observed not argued.** `dispatch.py:626-639`'s `READ_PROMPT` still enumerates no
  members and tells the reader to derive them "from `E10`'s own sentence"; that sentence now names
  the decision log, so the chain *dispatch → stub → checklist → member* closes. This session entered
  through exactly that chain and read `HD-5`/`HD-7` because of it. Honest edge: `HARNESS-LEDGER.md:7`
  also points at the file, so `E10` is not the only path — but the ledger is neither in the layer nor
  in the charter chain, which is what `B-1` was about.
- **One structural note, not a defect.** For this member `file_dir` *is* `repo_root/ResearchSystem`,
  so the guard's second class (`not from_dir and under_rs` — the missing-prefix defect) is
  definitionally unreachable for it; it gets class-1 protection only. That is correct behaviour, not
  a gap: a bare relative path in a file living at `ResearchSystem/` is a legitimate reference.

### 2.2 Mutation probes (`R8`, `E4`) — three, reproducing the real defect shapes

Copies taken to a scratchpad and sha256-verified before and after; `git checkout --` was not used.

**P1 — the `B-1` shape: a member silently outside the scan.** Removed the new entry from `LAYER`:
```
FAILED …LayerMembership::test_every_member_is_scanned
FAILED …LayerMembership::test_layer_equals_the_hand_written_membership
2 failed, 44 passed in 17.95s
E  AssertionError: Tuples differ: … First extra element 9: 'ResearchSystem/HARNESS-DECISIONS.md'
E  AssertionError: 0 != 1        (subTest member=ResearchSystem/HARNESS-DECISIONS.md)
```
Both value-level, neither a crash. The decisive one is `0 != 1`: with a bad path staged in
`HARNESS-DECISIONS.md`, `check()` returns 1 with the entry and 0 without it — the guard genuinely
reaches the new member. Restored, sha256 `7dce1ba7…` identical.

**P2 — the pin's direction.** Removed the entry from the hand-written `EXPECTED` only:
`1 failed, 45 passed` — the equality test alone. So `E5`'s hand-written literal is what pins the set,
and dropping a member from *both* sides cannot pass silently.

**P3 — the residual: the prose leg.** Deleted the whole decision-log clause from `E10`'s sentence,
leaving "these **ten** paths" above nine enumerated ones and `LAYER` at ten:
```
632 passed in 116.80s
repo-audit.py            → RESULT: clean (exit 0)
ledger_cap_check.py      → exit 0
layer_path_check.py      → exit 0   (with the mutation STAGED)
```
Nothing catches it. This reproduces rider `E10-sync` at the tip and is the honest residual of route
(a): the leg the repair actually relies on to reach a cold reader is the one with no mechanical
binding, so a future edit reopens `B-1` in silence while the guard keeps scanning the file (`V-4`).
Restored, sha256 `d4e8a143…` identical; `git status --porcelain` empty.

Incidentally verified while staging P3: `review_freeze_check` fires correctly right now — marker
present for this VERIFY's subject, non-record path staged → exit 1 with the marker's subject printed.

### 2.3 The errata's four re-measurements, re-derived

Measured at the revisions the errata names, not at the tip, because the tip is what its own §14
changed — the §14 header pins `fd058aa`, which is what makes this recheckable at all.

**`f-1` — exact, all four figures, at both revisions.** Corpus = `v3-review-*.md` under
`migration/document-work-assurance-v3/`; stem match; `chk-repo-audit.out.txt` excluded (the journal's
own correct exclusion) and `.harness/runs.jsonl` out of scope because it is untracked:
```
rev a7bb1d6  corpus 53 · cited 49 · occ 294 · lines 276 · pairs 185
   never: v3-review-full-3ded65a · v3-review-full-86533f2 · v3-review-verify-440e205 · v3-review-verify-45cae29
rev fd058aa  corpus 54 · cited 53 · occ 310 · lines 292 · pairs 198   never: v3-review-full-a7bb1d6
rev fd058aa  corpus 53, new record excluded as citer: cited 49 · 294 · 276 · 185   never: the same four
```
Every number the errata prints, including the "怪事" pair (53/54 · 310/292/198), reproduces to the
digit. The uncited set is four, not three; "169 次" reproduces under none of the three rules; the
chosen ruler (record,file pairs) = 185. `f-1`'s minimum fix — state the rule, re-run it, correct the
list to four — is discharged.

**`f-2` — numbers exact, one stated reason wrong (`V-6`).** With the stem universe the errata used:
```
78 runs-only check-chk-*.json stems
rev fd058aa: 22 files · 148 occurrences   |  excluding the new FULL record: 21 · 147
check_result_refs: p3-corr 11 · p4-bridge 11 · p4-doc 23 · p5a-firewall 12 · p5a-shells 17
                   p5b-claims 21 · p5b-firewall 16 · w1-r1 8   = 119
```
Exact, including p4-doc = 23, the two `issues/*.json`, the absence of any test fixture, and
`v3-review-verify-275da5b.md`. The conclusion holds under my scan: all 22 referencing files are the
run's own control plane, scripts, evidence or issue records, that run's live review, this journal, or
the new review record. No later round consults a closed run's CheckResult.

**`f-3` — the correction is right and its new total is off by 176 in two units (`V-5`).** Per-member
`len(text)` figures are characters, as the finding said, and the new member's ratio is as claimed
(`HARNESS-DECISIONS.md` 165 lines / 8,292 chars / **13,415 bytes** — +61.8%, exact). But from the
committed blobs:
```
TOTAL(10)  1125 lines / 75424 chars / 81048 bytes      ← blob
TOTAL(10)  1125 lines / 75600 chars / 81224 bytes      ← worktree  (what §14.3 prints)
CONSTRUCTION-CHECKLIST.md: 176 CRLF pairs; core.autocrlf=true; it is the only member with CRLF
```
The delta is exactly one CR per line of that one member — the hazard the FULL's `f-3` named in its
closing sentence. Line counts are `\n`-count (the journal's own ruler, no +1 for a missing trailing
newline); the blob here ends with a newline, so 176 under either.

**`f-4` — exact.** `120 + 626 + 28 + 165 + 7 = 946` across the five files, as printed.

### 2.4 Battery, run at the tip on a clean tree

```
$ python -m pytest -q          (ResearchSystem/tooling)   → 632 passed in 115.67s
$ python Thesis/Work/Tooling/repo-audit.py                → RESULT: clean (exit 0)
$ python ResearchSystem/tooling/hooks/ledger_cap_check.py  → exit 0   (HARNESS-LEDGER.md = 120 lines)
$ python ResearchSystem/tooling/hooks/layer_path_check.py   → exit 0
$ git status --porcelain                                   → empty
```

---

## 3. Findings

### Requiring a user ruling

#### `V-1` — the new member's read scope is decided two ways, and one of the two is itself a layer member

**Location.** `CONSTRUCTION-CHECKLIST.md:75-112` (`E10` as amended: a cold read of *this layer* is
owed at each round's opening; coverage by citation requires "a recorded **end-to-end** read of it";
"a read's record states the blob id of each member it read") · `document-harness/README.md`, Decision-log
row ("every cold read MUST read its §live (**and only §live**)") · `HARNESS-DECISIONS.md:8` and `HD-5`
("每轮 cold read 必读 §live；§implemented 与 archive 不在必读内").

**What goes wrong.** A member read in part can never be discharged by citation, so every future round
owes a fresh read of this file while simultaneously being told to read only one of its sections. The
decision log's own tie-break ("细则与裁决冲突，细则错") resolves the collision *against* `E10` and so
produces an unsatisfiable state rather than an answer — which is why this is not recoverable from
adjacent text and therefore not wording-level under `R9`.

**Named downstream decision, with its deadline.** A2's opening cold read — the action
`HARNESS-LEDGER.md:92-96` gates on this very review — must decide what it covers and what its record
may claim. **Deadline: that read.**

**Minimum fix (one ruling, not mine to choose — `R5`).** Either narrow `HD-5` so that as a layer
member the file is read end-to-end and `§live` is what *binds* rather than what is *read*, amending
the README row in the same commit; or write the exception into `E10`, which then needs a
section-level anchor a read record can state, since blob-level citation cannot express a partial read.

#### `V-2` — the authorization for the one fix leg exists only in a commit body, and the narrowing it forces is unwritten

**Location.** `fd058aa` body ("用户 2026-08-08 裁 `B-1` 走最小修 (a)") · `HARNESS-DECISIONS.md:9-10`
(`HD-4`'s admission test) · `HD-7`.

Grep of both plans, `HARNESS-LEDGER.md`, `HARNESS-DECISIONS.md`, `HARNESS-RIDERS.md` and the journal
finds no record of the route-(a) ruling. `HD-4`'s third admission question — "用户裁决且除对话与
commit 正文外无别的家" — is satisfied verbatim, and so is the second: the ruling puts the decision
log under `E10`, which `HD-1`'s design (decision log *above* instruction) did not contemplate, and it
makes `HD-7`'s title over-broad. I verified the substance of `HD-7` survives: its three enumerated
items — entry-field completeness, the must-read obligation, the archive prompt — are each untouched
by `layer_path_check`, which only decides whether a newly written path token resolves. So the finding
is narrow and exactly as the fix predicted for the half it flagged: **the title over-reaches and the
entry needs a ruling; the ruling that authorised the fix needs an entry.** One ruling closes both.

**Deadline:** A2's plan authoring, which per `HD-5` must inherit every live ruling verbatim — a ruling
with no entry cannot be inherited.

#### `V-3` — writing a new user ruling is now an instruction-layer amendment, and nothing classifies that act

**Location.** `CONSTRUCTION-CHECKLIST.md:88-110` (`E10`'s amendment machinery) ·
`HARNESS-LEDGER.md:63-65` (the 2026-08-03 ruling "ledger 删减/记账批不开轮，user ruling 即 gate",
scoped to the **ledger**).

Every future `HD-nn` entry is now an edit to a layer member, so each must be classified: `E10`'s free
channel (relied upon before its read, provided the commit records both facts and the bytes ride the
next layer read) or design (opens a round). `E10`'s own test — "an amendment adding a clause to any
rule … is design and opens a round" — does not decide it, because an `HD` entry is not a clause of
E1–E12/R1–R10 yet binds every later round, and the decision log's header says instruction text
expands *under* it. The 2026-08-03 classification would answer it if extended, but it names the
ledger. **Deadline: the next ruling the user issues** — plausibly inside A2, since A2 opens with the
two rulings `V-1` and `V-2` ask for.

### Low

#### `V-4` — rider `E10-sync` is now stale, and this round moved what it guards

`HARNESS-RIDERS.md:15` still quotes `E10` as "exactly these **nine** paths and nothing else" and
dates its deadline at "the moment v4 is cast". Two things changed. The quotation is false (`ten`),
and — the substantive half — the prose leg is no longer only an internal-consistency risk: after
route (a) it is the path by which a cold reader learns to read the supreme ruling registry, so a
silent prose deletion reopens `B-1`. P3 above is that mutation, re-run at ten members: 632 passed,
three guards clean. `R10` requires a finding whose value expires to carry that moment as its
deadline; "v4 is cast" no longer bounds the damage. Bytes for the quotation are trivial; the deadline
is a judgment I leave with the executor and the user.

#### `V-5` — `f-3`'s repaired total mixes measurement conventions

§14.3 prints ten-member totals taken from the **working tree** (75,600 chars / 81,224 bytes) beside a
"原九成员口径" row taken from **blobs** (66,890 chars / 67,389 bytes), so the pair is not comparable
by exactly 176 — one CR per line of the single member that carries CRLF. Blob is the right convention
here because `E10`'s read records identify members by blob id. Committed-blob figures:
**1,125 lines / 75,424 characters / 81,048 bytes**. `D7`'s conclusion is unaffected under any of the
three conventions.

#### `V-6` — `f-2`'s numbers are right; its stated reason is not

§14.2 explains the dropped `v3-review-full-dcfb2f2.md` as naming "一个并不存在对应文件的 check id".
It exists. The id is `check-chk-governance`, and three files carry it:
`assurance/shadow/{run-p3,round-2/run-p3,round-3/run-p3}/control/check-chk-governance.json`. The
accurate statement is "no per-check file in any of the **eight closed runs**; its files live in the
shadow rehearsal tree". Related and unstated: the errata's stem universe is `assurance/runs/`-only
(78); repository-wide there are 89 `check-chk-*` stems, 90 counting the aggregate `check-results`.
Both numbers reproduce under the runs-only universe — the finding is that the boundary which makes
them reproduce is the one thing the correction does not state, which is the class `f-1` was about.

#### `V-7` — the amendment moved the antecedent of "Its edits" (wording-level; bytes supplied)

`CONSTRUCTION-CHECKLIST.md:85-89`. The inserted clause ends "— its archive holds only entries out of
force and is not a member." and the next sentence opens "Its edits are additive or subtractive…".
Before the amendment "Its" could only be the layer; now the nearest antecedent is the decision log,
so a reader can scope the additive-only discipline, the amendment read and the design test to that
one member. It is wording-level under `R9` because adjacent text recovers the intent ("a cold read of
**this layer**", "each amendment", "a **member** whose blob"). Exact replacement, adding no clause
and no bound, so `E10`'s free channel takes it: `…and is not a member. Its edits are additive` →
`…and is not a member. The layer's edits are additive`.

#### `V-8` — the errata's own invariant is false for two of its four corrections

§14's header and `7a08265`'s body both state "**原行一律不改**". Two original lines were edited in
place: §12.4's opening line took a parenthetical, and §13.4's table cell became `867 → **946**`. The
discipline actually cited from `2c3cc99` — the wrong number stays visible, nothing is silently
rewritten — **is** satisfied in all four cases; the stated invariant is not. Suggested bytes: "两处
就地加注、两处另加更正块；错的数字一律不删".

---

## 4. Boundary and process (`R3` — second)

**4.1 Change boundary — held.** Classified by hand from `git show --name-status`: `ed0b120` = the
record alone; `fd058aa` = the three fix sites; `7a08265` = the journal alone. No product path, no
schema, no run directory, no closed-run byte, no ledger, no plan.

**4.2 Frozen surface (`E2`) — intact.** `git diff --name-status a7bb1d6 HEAD` over
`schema/document-assurance-v3/` and `contract/` is empty; the three frozen blobs and the fifteen-file
pack are untouched. The new layer member is not a frozen path, and `E2`'s list is unchanged by this
round, so `E2-FC`'s dormant conflict is not disturbed.

**4.3 `E9` — the window held; one classification is the executor's reading, not a recorded ruling.**
Timing: `ed0b120` 07:36:47Z landed the record alone and deleted the marker; `fd058aa` 07:56:53Z and
`7a08265` 11:04:14Z landed with no marker; this VERIFY's marker was written 11:04:40Z — 26 seconds
after the last commit, and the branch has taken none since. Budget: FULL at `ed0b120`, the one
approved fix at `fd058aa`, this VERIFY. **The errata's authority is where I differ.** It cites
"2026-08-04 裁决（journal/ledger-only 的 finding 修不消耗 `E9` 修腿）"; the recorded ruling
(`HARNESS-LEDGER.md:78-81`) says **ledger/riders-only** and gives the criterion "判据=改的是不是被
评审的 work product". In A1 the journal *is* the reviewed work product: four of five findings are
against its numbers, and `HD-10`/`HD-15`/`HD-16`/`HD-17`/`HD-11`/`HD-12`/`HD-13`/`HD-14` each carry a
`basis:` pointer into it. Two things keep this a note rather than a finding of its own: precedent
exists (`8dae1e0` treated a journal-table correction as budget-free after `E9` was exhausted, and
said so), and the harm the cap prevents did not occur — the correction landed *inside* this VERIFY's
range, so it was reviewed. What is missing is a ruling making the extension citable instead of read
off a narrower one; `E9`'s "never self-classify which round consumed what" is why I name it.

**4.4 `E8` — form.** All three titles carry `V3-…-v1` and name the round; `ed0b120` matches `R6`'s
required record form exactly. All three bodies open with a `kind:` line drawn from `E8`'s vocabulary
(review record / review fix / errata), no trailers, dense. Multi-paragraph bodies are conformant
under the 2026-08-07 ruling. `f-5` is answered by form from `fd058aa` onward, as the errata says;
`5144e86`'s empty body is immutable and correctly left alone.

**4.5 `E10` debt — larger, and correctly disclosed.** One member changed blob in this range:
`CONSTRUCTION-CHECKLIST.md ce6d1609 → 5cddc0ca`. `fd058aa`'s body states the amendment owes an
independent read and that it is unpaid, standing beside the same debt from `C1` (`55fe4e9`) and the
decision-log round. I confirm all three are real and unpaid, and that **this VERIFY is not one of
them** (`E10`: an amendment's read has the amendment text as its subject and is never banked as the
round's review). On reliance: nothing in the range depends on the amended text in `E10`'s sense —
the fix authored it, the errata cites its consequence for a line count, and this record reviews it,
none of which is an outcome that would change if the text changed. Useful for the next read:
`HARNESS-DECISIONS.md`'s own blob is unchanged across the range (`724465f4`), so a read of it can be
discharged by citation once one exists. The ledger's owed-read list at `:96` names `C1` and the
decision-log round but not this amendment; `E10` makes the obligation per-blob, so nothing is lost.

**4.6 Observations.**

- **`ob-1`** — `f-1`'s self-invalidating shape turned over once more inside the errata itself: at
  `7a08265` the corpus-53 figures are 303/285/189 and **no** record is uncited, because §14.1's
  correction block names all four. The header pinning `fd058aa` is what keeps the numbers checkable;
  §14.5's own lesson ("要么轮末重测，要么在数字旁写死测量时的 commit") is applied, once, at the
  section head.
- **`ob-2`** — the approved fix boundary was exceeded by one site and said so, with the reason. I
  reproduced both directions (P1, P2): omitting `EXPECTED` would have been red on the spot. `E9`'s
  "requires saying so, never silently" is satisfied.
- **`ob-3`** — the FULL located the charter as `CONSTRUCTION-CHECKLIST.md`; the dispatch actually
  hands the retired stub (`dispatch.py:508-510`), which names the checklist. One hop, immaterial to
  `B-1`, recorded so the next reader does not re-derive it.
- **`ob-4` (`R5`, the shape)** — the FULL's `ob-4` reported an eleventh governance surface with no
  mechanical binding declared supreme over the rest. This round closed that bill by making it the
  tenth layer member, and the three findings above are the change of accounts: obligations designed
  for nine slow-moving rule texts now apply to a registry the user writes into whenever they rule.
  Whether that is the right trade is the user's; what I record is that route (a) converted one
  reachability defect into three governance questions, each closable by a single ruling, and that the
  round disclosed one of the three itself.

---

## 5. Honesty ceilings (`R4`)

1. **Read in full:** `CONSTRUCTION-CHECKLIST.md` · `v3-review-full-a7bb1d6.md` ·
   `HARNESS-DECISIONS.md` · `HARNESS-LEDGER.md` · `HARNESS-RIDERS.md` ·
   `document-harness/README.md` · `hooks/layer_path_check.py` · all three commit bodies and the
   complete diff of all five files · `dispatch.py:505-669`.
   **Sampled:** the journal — §12 and all of §14 (the errata) read, the other ~650 lines not.
   `test_precommit_checks.py` — the `LayerMembership` and `CandidatePath` classes and the header.
   **Not read:** both plans (grepped only), `HARNESS-DECISIONS-archive.md` (scanned for path tokens
   only), `EXECUTION.md`, `REVIEW.md`, the other 53 review records.
2. **`UNVERIFIABLE`, not folded into supported:** that `ed0b120` committed the FULL record byte-for-byte
   as the reviewer returned it (`R6`). There is no non-repository original to diff against; I checked
   only that the record is internally consistent and that its `f-1`/`f-2`/`f-4` figures reproduce,
   which is evidence of fidelity, not proof of it.
3. **Process claims are marked, not verified:** the route-(a) ruling, the 2026-08-04 ruling, and
   "fresh context". I read committed records only, and `V-2` is what follows from one of them having
   no record but a commit body.
4. **Mutation proves binding force, not sufficiency.** Three probes, one of them a negative result by
   design (P3). `P1` shows the guard reaches the new member; it does not show that a resolvable-path
   check is the *right* guard for a ruling registry, and `HD-7` says no other guard is wanted.
5. **A VERIFY is never a re-certification.** I did not re-review A1's measurement layer beyond the
   four corrected figures, and I did not re-judge anything the FULL marked `UNVERIFIABLE` — §10's
   per-line classification and the 34% handle rate remain un-reproducible, so `HD-13` still rests
   partly on numbers no command reproduces.
6. **Counting rules, stated because `f-1` is why:** review-record citations are stem substring
   matches, `chk-repo-audit.out.txt` excluded, untracked files out of scope, self-matches excluded,
   measured on the committed tree at the named revision. Line counts are `\n` counts with no +1 for a
   missing trailing newline. Sizes are blob bytes and decoded characters, never worktree bytes.
