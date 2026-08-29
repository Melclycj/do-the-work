# Instruction-layer read — subject `a542c6db39ca470d8f02fc32c288cd126944e974`

An `E10` read. Not a round: no budget spent, no verdict carried, output is findings tiered
must-fix / low / observation (`R3`). Dispatched with the charter
`migration/document-work-assurance-v3/v3-harness-review-contract.md`, a stub whose named
successor `document-harness/CONSTRUCTION-CHECKLIST.md` was read in full as both the standing
instruction and its own counterpart, per that file's own opening line.

Record name: `v3-cold-read-`. `R6` offers two read filenames and the layer still defines no
criterion for choosing between them (rider `read-name-split`, not closed here). I took
`cold-read` for the reason the four previous whole-layer records took it — the subject is the
layer at a round's opening.

## 1. The member set and the coverage, both derived — not received

The dispatch enumerated nothing and handed me no member table. `E10`'s own sentence at the
subject does, and reads **exactly nine paths** (`CONSTRUCTION-CHECKLIST.md:117`). All nine
resolve at the subject. Blob ids from `git rev-parse a542c6db…:<path>`, run here, against the
blob ids `v3-cold-read-006138e.md` §1 states for the same nine:

| # | member | blob at `a542c6d` | vs `006138e` |
|---|---|---|---|
| 1 | `document-harness/CONSTRUCTION-CHECKLIST.md` | `5f77c3fdbc0f5fc5a04516a044292d9f35885068` | same |
| 2 | `document-harness/README.md` | `271e934460069d8e2862e5d45b6757a26834630b` | **moved** (`a9c388ca…`) |
| 3 | `document-harness/EXECUTION.md` | `234fdddf974e580d22a1a26b54587d11c24863b3` | same |
| 4 | `document-harness/REVIEW.md` | `13f91419df0eaf607b5b15b8b6fe5c7e0369c775` | same |
| 5 | `document-harness/ORCHESTRATION.md` | `a9e9f75e484f40f4a1014e5d68ed6c73aa5fbdc2` | same |
| 6 | `migration/document-work-assurance-v3/v3-harness-operating-contract.md` | `6d5714923870b4e13e8928221a80df68e563a5ed` | same |
| 7 | `migration/document-work-assurance-v3/v3-harness-review-contract.md` | `29bdc9fbde6e8db38d601dd2340d4b46a24a296f` | same |
| 8 | `contract/Document-Work-Assurance-Contract-v4.md` | `a90c90fde879039f6b0a7d8ca7917e6a06482117` | same |
| 9 | `schema/document-assurance-v3/paragraph-map.schema.json` | `09aa869962f592c2f86c9379be0ef3eb7d2232ff` | same |

**Why `v3-cold-read-006138e.md` is a record that can be cited.** `E10`'s citation clause admits
only a *recorded end-to-end read of that member*, and a narrow-form record covers by citation
only what it read end to end (rider `read-name-split` makes the same point). That record states
all nine blob ids and says in as many words: *I did not rely on the citation channel: all nine
were read end to end in this session regardless of whether their blobs moved*; its §5 coverage
list opens **Read in full: all nine members**. So it is an end-to-end read of each of the nine,
and citation of it is available for every member whose blob has not moved since.

**Coverage, derived from the two columns above.** Eight members are byte-unchanged since that
read and are covered by citing it. One — `document-harness/README.md` — moved, and I read it end
to end. Independently confirmed at the subject rather than taken from the ruling:

```
$ git diff --stat 006138e a542c6db39ca470d8f02fc32c288cd126944e974 -- <the nine>
 document-harness/README.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

$ git log --oneline 006138e..a542c6db39ca470d8f02fc32c288cd126944e974 -- <the nine>
1f3e213 V3-V1-RESULT-RETIRE-ITEMS-ABCDEFH-v1
```

`db1bfa1..a542c6d` is `257235b` and `a542c6d`; neither touches a member, so plan ruling 16's
ground — measured at `db1bfa1` — still holds two commits later at the subject. This agrees with
the orchestrator's addendum, which I verified rather than accepted: ruling 16 is present at
`document-harness/plans/core-only.plan.md` and reads as the addendum reports it.

**Worktree integrity.** `git rev-parse HEAD` returns the subject; `git status --porcelain`
returns only `?? .goals/`, untracked and outside the layer. I additionally ran `git hash-object`
over all nine members plus `HARNESS-DECISIONS.md` and compared each to the subject's tree entry:
ten of ten identical. The bytes I read are the subject's bytes. (After the mutations in `O-2` the
same check was re-run — see there.)

**`HARNESS-DECISIONS.md` `§live`** is not a member and is cited by section, never by blob; it was
read **in full**, lines 30–266, **eleven** entries: `HD-67`, `HD-66`, `HD-65`, `HD-62`, `HD-59`,
`HD-41`, `HD-36`, `HD-35`, `HD-34`, `HD-23`, `HD-9`. Since the previous read, `HD-63` and `HD-64`
have left `§live` (both now sit under `§implemented`, at `:311` and `:269`) and `HD-65`, `HD-66`,
`HD-67` are new. The file is at this repository's root, which is the copy `E10` names.

**The previous read's `M-1` is discharged, and I checked it at the bytes rather than by report.**
It required that `document-harness/README.md:20`'s live markdown link to `review.schema.json` be
dealt with before item C landed. The diff over member 2 is exactly that row: the `[review](…)`
link is gone, and the replacement deliberately declines to write the stem in either form the
guard reads, saying so in the row itself. `O-2` mutation-tests that the stated hazard is real.

## 2. Findings

### `M-1` (must-fix) — `HD-67`'s site census inherits the reference sweep's backtick blindness without saying so, and the contract holds a **third** `CONTRACT-V4-SIGNATURE.md` site that its "remaining two" sentence does not reach

`HD-67`'s consequences paragraph tells the executor what is left after the two authorised blocks
are removed:

> 剥史树上契约的 7 处 NAMETOK（plan 量程表 `:16/:27/:28/:31/:33/:254/:365`，于 `607728a` 测）中
> 五处随两块消失，余两处（`CONTRACT-V4-SIGNATURE.md`）由 holder 句处置。

The arithmetic inside that census is correct and I reproduced it: block ① (`:21-33`) contains
`:27 :28 :31 :33`, block ② (`§12`'s first two paragraphs, `:248-257`) contains `:254`, five
vanish, and `:16` and `:365` remain, both `CONTRACT-V4-SIGNATURE.md`. The contract blob is
unmoved between `607728a` and the subject (`a90c90fd…` at both), so the measurement is current.

**But the contract names `CONTRACT-V4-SIGNATURE.md` at three sites, not two.** Grepped here over
the member at the subject:

```
9:signature_owner: CONTRACT-V4-SIGNATURE.md (this instrument's v4 signature record)
16:> and after review, in `CONTRACT-V4-SIGNATURE.md` — held by this instrument's own construction
365:signature record (exact contract blob + date) lives in `CONTRACT-V4-SIGNATURE.md`, held by this
```

`:9` is a YAML front-matter field. It is absent from the census for a mechanical reason, not a
decided one: `sweep_refs.py`'s NAMETOK is *a backticked bare filename* (its own docstring, `:12`)
and it imports the backtick-anchored `TOKEN` pattern from `layer_path_check.py:48`. `:9` carries
no backticks, so no scanner run can ever report it. I confirmed the predicate by reading both
files and by running the sweep at the subject.

**Why this is not a scope-declaration defect in `HD-67`.** The entry does declare its scope —
*剥史树上*, *7 处 NAMETOK*, *于 `607728a` 测* — which is what `HD-41` ① asks. The defect is the
inference drawn from it: a NAMETOK census is treated as the census of caller-unreachable
references to that file, and the sentence *余两处…由 holder 句处置* tells the executor that
handling two sites finishes the class. It does not.

**Why `:9` cannot simply be given the same treatment, which is what makes leaving it silent
expensive.** `:9` is load-bearing and pinned: `tooling/rsclib/document_harness/checks.py:486`
records that keys ending `_owner` — `signature_owner` named — are the *correct* pattern, naming
who owns approval without carrying it, and
`tooling/tests/document_harness/test_candidate_checks.py:1997-2000` asserts the contract's front
matter carries `signature_owner` and that it is not a self-approval field. So the site cannot be
deleted, and a prose holder clause — the disposal `HD-67` prescribes for `:16` and `:365` — does
not fit a YAML scalar. Whatever is done with it needs a decision; the current text hands the
executor a count saying no decision is owed.

**Why it may not wait.** The executor writes the contract commit in this round, immediately after
this record lands, and `HD-67` is the authorisation it writes under. `HD-41` ④ requires the class
to be swept before the fix is written, and `E7` binds the executor to the defect class rather
than the reported instance. A round that closes having treated two of three sites will have
treated the class by the one census that could not see the third.

**Minimum fix.** Before the contract commit lands, the third site is on the executor's list:
either `HD-67` is corrected forward (`HD-59` — a new paragraph, the original left verbatim)
naming `contract/Document-Work-Assurance-Contract-v4.md:9` and what happens to it, or the round's
own record does, and the contract commit's `E2` body states the disposal. **I supply no bytes for
`:9` itself**: what a front-matter governance field should say when its object is
caller-unreachable is a decision about signed text with a test pinned to it, and under `R5` the
choice is the user's, not mine.

**Routing note, because the usual channel does not reach this.** The object of this finding is a
`§live` entry, and `E10` says of that file that *no amendment machinery here reaches it, its own
bytes are discipline (`HD-7`)*. So this must-fix is **not** answerable by an `E10` amendment plus
re-read; it is answerable by the forward correction above, and it spends no budget either way.

### `L-1` (low) — the contract carries a bare filename for a schema that now exists nowhere, with no holder sentence, and it travels to every caller

`contract/Document-Work-Assurance-Contract-v4.md:302`:

> Until 2026-08-28 this bullet promised instead that `review.schema.json` and the v1 checker
> functions stay frozen for that reading.

The sentence is **true** — it reports what the bullet used to promise — and the previous read
correctly cleared it on that ground at `006138e`, where the file still existed. Round
`V1-RESULT-RETIRE` then deleted it (`1f3e213`), and the name now resolves nowhere:
`schema/document-assurance-v3/` holds 14 files and `review.schema.json` is not among them.
`sweep_refs.py` reports it at the subject, and its docstring says why that matters here — *a bare
name is the compliant form for a caller-held artifact … this sweep surfaces it so a reader can
check the holder sentence exists*. I checked: there is none, and `review.schema.json` was never a
caller-held artifact — it was a harness schema this repository shipped. The neighbouring NAMETOK
at `:25` is unlike it: `Document-Work-Assurance-Contract-v3.md` is covered by its own sentence,
*reachable in git history at their recorded blobs*.

**Why low and not wording-level.** No actor's action changes today and the statement is not
false, so `R9`'s test nearly takes it. What keeps it off that branch is a nameable consequence:
`HD-66` records the measurement *全仓 409 件上真断链为 0（14 条全是 NAMETOK，扫描器自陈那是调用者
持有物的合规写法）*, and that measurement is the material for the core-distribution question the
entry exists to keep open. At least this one of the fourteen is not the compliant caller-held
form, so the residue is understated by one in the optimistic direction. `HD-66` disclaims
deciding — *今日实测只作判断材料，不构成判定* — so nothing is overturned; the characterization is
what needs correcting, not the ruling.

**No bytes.** The obvious repair adds a clause saying where the file went, inside `E2`-frozen
signed text; which of the live shapes applies is the user's under `R5`. It also sits one line
from the bullet `HD-64` authorised, and `HD-64`'s boundary is explicit that it authorises only
that bullet on only that ground.

## 3. Observations

- `O-1` — **`HD-67` departs from plan ruling 11's literal words on the signature, and is right
  to; recorded so the closeout does not read it as a deviation.** Ruling 11 prescribes
  `CONTRACT-V4-SIGNATURE.md` *re-pointed at the new blob*. That instruction has had no object
  since 2026-08-28: the file's own forward correction (`:17-33`) records that item A `184387c`
  left `E2` pinning **no blob hash at all**, so *there are not two literals to differ by
  construction; there is one, the signed one*. The file records a signed blob and a growing list
  of post-signature writes, and nothing else to re-point. `HD-67` substitutes the established
  shape — *记入第五笔签署后写入，不重指签字 blob* — which is exactly what the third and fourth
  writes (`:34-54`) did. Plan ruling 18's claim that `HD-67` *transcribes rulings 4 and 11 and
  decides nothing new* holds on this point; what it does is decline an unexecutable instruction,
  and it discloses the declining. Worth not reusing ruling 11's wording downstream.
- `O-2` — **the mutations the previous read asked a successor to run, run.** That record's ceiling
  was explicit: no Python, nothing mutation-tested, and *a reader wanting binding force on `M-1`
  should demand that mutation*. Python 3.13.6 is reachable in this session, so I ran it. Method
  per `E4`: a sha256-checked scratchpad copy, restore by copy, never `git checkout --`. Original
  `document-harness/README.md` sha256
  `4a0444d2c068e49213a017ab5f172c28a031cf8f53724358cfd89eb9a759908e`.
  - **Must-fire control** — replace the live `[paragraph-map]` link form:
    `test_readme_enumeration` goes **red** at `:54`. The guard has binding force.
  - **The blind spot, reproduced** — restore a
    `[review](../schema/document-assurance-v3/review.schema.json)` link for the deleted schema:
    the same test **passes**. So `README.md:20`'s own warning — that writing the stem *would
    satisfy that guard in advance for a file that no longer exists* — is measured, not argued,
    and the row's decision to withhold the stem is load-bearing.
  - On the same mutated tree `layer_path_check.py` exits **0** (it scans only a commit's added
    lines, and a markdown link carries no backticked token), while `sweep_refs.py` **does** report
    the dangling link. `E10`'s *what the guard still cannot see* clause is accurate, and the sweep
    is the only instrument covering this class — a sweep that always exits 0 and is not wired into
    the hook.
  - Restored and re-verified: sha256 back to `4a0444d2…`, `git status --porcelain` back to
    `?? .goals/` alone.
- `O-3` — **the enumerations the layer states still hold at this subject**, re-derived rather than
  carried over, since a member moved and a schema left the tree. `layer_path_check.py:37-47`'s
  `LAYER` is the same nine paths in the same order as `E10`'s sentence, so `E10-sync` does not
  fall due (member 1 is unmoved in any case). `ORCHESTRATION.md` has nine rows under *The nine
  obligations that are already law elsewhere* plus three under *The three obligations this file is
  the text for*, making `README.md:22`'s twelve. `EXECUTION.md` carries all six run-template
  sections (`:183 :206 :254 :291 :341 :444`). The README's schema table names 14 delimited stems
  and the pack holds 14 files; `test_readme_enumeration` and `test_announced_path_disclosure` pass
  (19 tests) and `layer_path_check` exits 0 at the subject.
- `O-4` — **`E2` survives the pack's first deletion, and the rider bank already holds the reason,
  so I am not re-filing it.** `announced_path_disclosure.py:56-73`'s `ANNOUNCED` still lists 15
  schema paths including `review.schema.json` while the directory holds 14. That is not drift:
  `E2` names the files the pack held at the 2026-08-03 re-baseline — a dated snapshot — and the
  guard's list is hand-written per `E5` and deliberately does not read the directory back. Rider
  `announced-set-anchor` records this exact divergence, records that its deadline arrived at
  `V1-RESULT-RETIRE`, and records the user's ruling of 2026-08-28 to maintain and re-set
  redeem-when. Checked, current, nothing owed.
- `O-5` — **`README.md:22`'s "tenth member" is stale for a fifth cycle, and this cycle supplies
  the measurement rider `r9-terminal-no-carrier` was created to wait for.** The sentence — *added
  as the tenth member 2026-08-18* — is true as dated history, and `E10`'s membership sentence
  remains the only authority on the count, which reads nine. The rider's claim is that `R9`'s
  terminal branch (*rides the next batch touching this layer*) writes down no carrier, so
  "routed" and "lost" are the same state; its evidence was one instance. There are now two: round
  `V1-RESULT-RETIRE` touched **this exact member** at `1f3e213`, and the line is byte-unchanged
  across it — verified as a context line, not a changed line, in
  `git diff 006138e a542c6d -- document-harness/README.md`. **I am deliberately not routing this
  through `R9`'s terminal branch again**; that is the branch which lost it four times. It belongs
  on the rider row that already exists, as a touch record.
- `O-6` — **one small staleness item, not in a member, not worth a channel.**
  `test_readme_enumeration.py`'s docstring says *all 14 delimited stems sit in the three
  enumeration rows today*; today they sit in four (`README.md:18 :19 :20 :21`), the paragraph-map
  row having become its own. The count 14 is right and the docstring's actual argument — that
  whole-README matching and table-scoped matching are equivalent — is unaffected.
- `O-7` — **`E9`'s review window is intact and the subject is HEAD.**
  `.harness/review-pending.json` names the subject, dispatched `2026-08-29T12:58:53+00:00`, 45
  seconds after the subject commit's own timestamp (`2026-08-29T22:58:08+10:00`).
  `git rev-parse HEAD` returns the same SHA, so the branch has taken no commit since dispatch, as
  `E9` requires. The marker is gitignored (`.gitignore:18`, `.harness/`) and nothing committed
  carries it. The plan's opening disclosure about an earlier marker written by a
  `dtw dispatch --read db1bfa1` that launched no reader is consistent with what I see: no commit
  landed between `db1bfa1` and the round's open but the round's own records.

## 4. Coverage and ceilings (`R4`)

- **Read in full**: `document-harness/README.md` (member 2, the one that moved);
  `document-harness/CONSTRUCTION-CHECKLIST.md` as the standing instruction and its own
  counterpart; `migration/document-work-assurance-v3/v3-harness-review-contract.md` as the
  dispatched charter; `HARNESS-DECISIONS.md` `§live` (lines 30–266); `CONTRACT-V4-SIGNATURE.md`;
  `tooling/tests/document_harness/test_readme_enumeration.py`; `v3-cold-read-006138e.md` as the
  cited record.
- **Covered by citation, not re-read** (`E10`'s narrow form, plan ruling 16): members 1, 3, 4, 5,
  6, 7, 8, 9 — each byte-unchanged since `v3-cold-read-006138e.md`, which read all nine end to end
  and states their blob ids. Blob equality is shown in §1 and is the whole of the ground.
  **What this costs, stated rather than softened:** I did not re-read those eight, so a defect
  visible only in their standing text — one that was there at `006138e` and was missed then — is
  outside this read. Findings `M-1` and `L-1` both concern member 8, which I did not read end to
  end; both were reached from outside it (a `§live` entry's census, and a sweep run) and both were
  then confirmed against the member's own bytes at the sites named.
- **Sampled**: `document-harness/plans/core-only.plan.md` (rulings 1–18 and the opening
  disclosure, not the whole file); `contract/Document-Work-Assurance-Contract-v4.md` at `:1-33`,
  `:246-268`, `:292-310`, `:365`; `document-harness/ORCHESTRATION.md:45-62`;
  `document-harness/EXECUTION.md` headings; `tooling/sweep_refs.py:1-36`;
  `tooling/hooks/layer_path_check.py:25-60`; `tooling/announced_path_disclosure.py:53-73`;
  `HARNESS-RIDERS.md` rows `E10-sync`, `read-name-split`, `checklist-cited-not-carried`,
  `onboarding-carries-construction`, `contract-wikilink-tier`, `r9-terminal-no-carrier`,
  `announced-set-anchor`.
- **Probed by command only**: the nine blob ids and `HARNESS-DECISIONS.md`'s, via `git rev-parse`
  and `git hash-object`; the member diffstat and commit list over `006138e..a542c6d`, via
  `git diff --stat` and `git log`; the schema pack listing; `signature_owner` readers, via grep;
  the sweep's full output at the subject.
- **Executed**: `python -m pytest` over `test_readme_enumeration.py` and
  `test_announced_path_disclosure.py` (19 passed); `python tooling/hooks/layer_path_check.py`
  (exit 0); `python tooling/sweep_refs.py` (exit 0, *14 caller-held or unresolvable references
  over 9 members*); the two mutations of `O-2`. **No full regression battery was run**, and
  nothing outside the two named test files was executed.
- **Process claims are marked, not verified** — that this session started cold and read nothing of
  the round beyond what is committed is a declaration with no evidence lock. What is checkable is
  that every fact above cites a command or a committed byte.
- **`M-1` supplies the site but deliberately no bytes** (what a pinned front-matter governance
  field should say is a decision about signed text; `R5`). **`L-1` supplies no bytes and says
  why.** Neither finding takes `E10`'s free channel, so nothing in this record is self-applying.
  `M-1`'s object is a `§live` entry, which `E10`'s amendment machinery does not reach.
