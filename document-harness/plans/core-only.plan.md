# Plan — batch `CORE-ONLY`: the construction side becomes an ordinary caller of the harness

> **Status: OPEN — round 1 `CORE-ONLY-LAYER` opened 2026-08-29, third sitting, off the `E11`
> card.** **base_commit: `db1bfa1`**, the `dev` tip at opening — stated here and not derived from
> `main` (31 commits behind `dev` at that moment), for the reason `V1-RESULT-RETIRE`'s own base
> correction records. Rounds 2 and 3 are not open. The round's steps are the *Steps — round 1*
> checklist below. Rewritten 2026-08-29 (second sitting) after the framing below replaced the
> one this file carried at `18d120d`.
>
> **This file is the carrier of the user's rulings of 2026-08-29** in *Rulings*. Until they land
> here they live only in the conversation that took them, which is chat-only load-bearing material
> and a finding under `R2`.
>
> **Every figure was measured 2026-08-29 at `607728a`** with `tooling/sweep_refs.py`, `git ls-files`
> and `grep`. Re-run them before any claim; line numbers drift.
>
> **This is design.** It changes what the instruction-layer membership rule says, so a round opens
> and the opening cold read is not waivable by this file.
>
> **Second sitting, 2026-08-29: all six open questions are answered — rulings 8–15.** The user
> directed that this sitting lands the design and opens nothing; the round opens in a later
> session. Re-measured at `ea6485d` before writing (`E3`): `git ls-files | wc -l` 410 · the eight
> product-tier rows 58 · `python tooling/sweep_refs.py` on this repository **14** · on a
> `git archive` harness-only tree **48** (3 MISSING · 5 LINK · 2 PATHTOK · 38 NAMETOK, 14 of them
> the full-repository set) — identical to the `607728a` figures below; `python -m pytest
> tooling/tests -q` **830 passed**.
>
> A cold session reads this file, then `CONSTRUCTION-LEDGER.md`'s current pointer, then works.

## What changed from the version at `18d120d`, written forward rather than over

That version framed the work as three shapes — repair the dangling references, split the code, or
let the construction checklist travel — and asked the user to pick. **The user replaced the frame
rather than picking from it**: *如果按照开发层自己是 harness 的一个实例来看，需要做到所有库自己的
规则都是 harness 的附加*. That is not shape C, and it subsumes shape B. Everything below follows
from it. Four things the earlier version got wrong or too small, each corrected here and left
visible because it was committed:

1. **The citation count was 37; it is 36.** `EXECUTION.md:235`'s `` `R0` `` is a product run's own
   review-dimension name, not a citation of a construction rule. No such rule exists.
2. **The contract work was stated as "seven sites needing a ruling"; that is the wrong unit.**
   Three of the seven already carry the holder clause the rule asks for. The real object is three
   blocks of provenance, not seven lines — see *The contract's provenance*.
3. **"The layer guard follows the construction side" was wrong.** Under ruling 5 it becomes a
   general guard that both sides use. Stated in the earlier version's item C; withdrawn here.
4. **The A/B/C framing is withdrawn entire.** It is preserved in this paragraph because a future
   reader will re-derive it, and because ruling 2's reason is not "B was cheapest".

## Goal (one line)

**The construction side stops being a special case and becomes an ordinary caller**: the harness
carries the rules every caller needs, each caller — this instrument included — declares its own
additions, and a repository that mounts only the harness can open, run and close a real run.

## Rulings (this file is their carrier)

1. **Core-only usability comes before the first product run** (2026-08-29). Overturns the queue
   order committed hours earlier at `689ae5d`. Recorded at `607728a`.
2. **The construction side is an instance of the harness applied to itself, so its own rules are an
   *addition* to the harness rather than part of it** (2026-08-29). This is the frame, and the
   reason is structural rather than economic. Consequence: the construction checklist splits — the
   part every caller needs travels as harness text, the part that is only this instrument's own
   working discipline stays as this instrument's caller-side addition.
3. **Acceptance is the mechanical check *and* a real product run** (2026-08-29, 机械检查 + 产品
   run 实测). This pulls the product run — queue position ② until now — into this batch, and with
   it the 2026-08-23 ruling that a first product run happens in a caller repository rather than
   here. The batch therefore spans two repositories.
4. **The contract's provenance goes with this batch** (2026-08-29, 要一起做了). A product contract
   carrying this instrument's construction history is pollution of the rule text; the earlier
   answer — label each citation with its holder — treated the symptom.
5. **The instruction-layer membership rule does not cover the construction side** (2026-08-29).
   It names the harness's own members; every caller, this instrument included, declares its own
   additions. The guard reads the union.
6. **The two retired-contract stubs may be removed if the work permits** (2026-08-29, 可以看着
   情况移除). Not mandated — item D states the condition.
7. **How a caller declares its additions is decided at round open, not here** (2026-08-29, answer
   to *这个留到开轮再做吗*). This file enumerates the candidate shapes so the decision is one
   sitting rather than research, and records what `E6` asks of any of them.
8. **The shared half is `document-harness/RULES.md`** (2026-08-29). A new product-tier file
   beside the three role charters, linked by the same bare same-directory form the six
   checklist pointers use today; the `E*` / `R*` identifiers the 36 citations carry do not
   change. `CONSTRUCTION-CHECKLIST.md` keeps its name and its place in `document-harness/` as
   this instrument's own rule file: the product tier is a list and not a directory prefix
   (core-set rulings 11 and 19), so the folder's 69 construction-side files — 76 tracked, 7 in
   the product tier — cost a caller nothing on a harness-only tree. Moving the checklist beside
   the root registers was priced — `git grep -l` finds 15 tracked files naming its path outside
   `migration/`, `journal/` and `plans/` — and is out of scope.
9. **A caller declares its own rules and its policy in one tracked config, `harness.json`, at
   its repository root** (2026-08-29). Two fields, both paths: `policy` — the caller's policy
   file, or null — and `rules` — the caller's own rule files. Four readers, each a decision
   that changes when the file is absent (`E6`): `dtw dispatch`, in every mode, adds one line
   to the prompt naming the declared rules, to be read after the charter — so a cold session
   receives a caller's rules by the channel it receives `EXECUTION.md` / `REVIEW.md`;
   `layer_path_check.py` and `sweep_refs.py` scan the declared files as they scan the harness
   members; the orchestrator reads `policy` where it read the entry-file pointer line; `dtw
   init` writes an empty default. The config holds paths only — rule and policy text stay
   markdown, read by people and by sessions and subject to the layer's amendment discipline.
   Of the three shapes enumerated under question 2: **(b)** is rejected because
   `.harness/scan-surfaces.json` is per-checkout by design and `caller.py`'s own docstring
   records what a fresh clone loses; **(c)** is rejected because only the caller's `CLAUDE.md`
   is injected into a session automatically — every other file enters context by being named
   and then read, and a dispatch prompt cannot name a file no machine can find. That `claude -p`
   loads the working directory's `CLAUDE.md` unprompted was verified 2026-08-29 rather than
   assumed: a scratch directory whose `CLAUDE.md` carried a sentinel token, and a `claude -p`
   session started there returned the token when asked for it.
   `review_record_dirs` stays where it is: it is checkout state, and folding it in is another
   question. The entry-file pointer line (README `:163-167`, ONBOARDING item 7) remains as the
   human path; ONBOARDING gains an item for the config. *Every mode* means every dispatch mode
   that stays in the product tier; this repository's construction-side dispatch, wherever item C
   puts it, does the same, and where the construction charter and a declared rule are one file
   the prompt names it twice or the generator folds them — the executor's call.
10. **The membership rule reads in two sentences** (2026-08-29). The first names the harness's
    own members and nothing else; the second says a repository declares its own rules in
    `harness.json`, that dispatch names them and the guards scan them, and that a declared
    rule binds only the repository declaring it. The exact words are the executor's. Rider
    `E10-sync` binds the sentence, `LAYER` and the test's `EXPECTED` to one commit, with the
    five prose sites it lists.
11. **The contract's provenance takes the light route** (2026-08-29): a recorded ruling
    permitting in-place removal of the pure-history blocks — the shape of `HD-63` / `HD-64` —
    plus `CONTRACT-V4-SIGNATURE.md` re-pointed at the new blob, plus the independent re-read
    `E10` owes. The ruling entry lands as a ruling commit inside round 1, as `HD-64` did at
    `4a380be`, not here. §12's third paragraph stays.
12. **The product run happens in the caller `D:/Thesis-stage-control-refactor`** (2026-08-29) —
    the one real caller on this machine, mounting this repository at `ResearchSystem/harness`
    (gitlink `2522ce1` when this was written), and it has been waiting to start one. The
    gitlink is bumped to this batch's tip and the run is a small real piece of work, not a
    scratch. Which piece of work it is gets chosen on the caller's side when round 3 opens;
    nothing here names it.
13. **Three rounds** (2026-08-29): **`CORE-ONLY-LAYER`** — A, B, E, G, the guards' half of H,
    and I; **`CORE-ONLY-CODE`** — C, D, and the dispatch half of H; **`CORE-ONLY-RUN`** — F, in
    the caller. The cut follows the surfaces: `E10-sync` binds the membership sentence and the
    guard to one commit, so the guard's change is round 1's; C, D and the dispatch line touch
    no member; F is in another repository.
14. **This repository gets a three-line `CLAUDE.md`** (2026-08-29): where `harness.json` is,
    where the ledger's pointer is, where the registers are — an entry file and nothing more.
    The checklist's text does not move into it: `CLAUDE.md` is injected into every session in
    this repository, and the checklist carries the layer's amendment discipline, which an
    injected file does not. This repository's own `harness.json` lists
    `document-harness/CONSTRUCTION-CHECKLIST.md` under `rules`; what its `policy` names is the
    executor's to propose — the ledger header's *What may enter* already plays that role — and
    the user's to rule.
15. **This sitting lands the design and opens nothing** (2026-08-29). The round opens in a later
    session, and `base_commit` is stated then.
16. **The opening cold read runs in the narrow form** (2026-08-29, third sitting, off the `E11`
    card): `document-harness/README.md` end to end, the other eight members by citation of
    `v3-cold-read-006138e.md`, `HARNESS-DECISIONS.md` `§live` in full. Ground, measured at
    `db1bfa1` before the card: `git diff --stat 006138e db1bfa1 --` over the nine members
    returns `document-harness/README.md | 2 +-` and nothing else, the one commit being
    `1f3e213`. The reader derives the coverage itself; the dispatch hands it the ruling and no
    member table (`R2`; journal `core-set-layer-2026-08-26.md` §4).
17. **Every cold session this round — reader, executor, reviewer — runs as its own `claude -p`
    session on `opus`** (2026-08-29, third sitting): the `E1` / `HD-55` form, the model chosen
    because the round rewrites the membership sentence and the contract, where a wrong edit is
    expensive.
18. **`HD-67` is the orchestrator's to write and lands before the cold read** (2026-08-29, third
    sitting): it transcribes rulings 4 and 11 above and decides nothing new, so that the `§live`
    the reader reads at the subject already carries it; status `live`, and flipping it is the
    user's (`HD-2`).
19. **Contract `:302`'s bare `review.schema.json` gains a holder-or-history clause in this
    round's contract commit** (2026-08-29, answering the opening read's `L-1`,
    `v3-cold-read-a542c6d.md`): the file left the pack at `1f3e213` and the sentence naming it,
    true as history, carries no holder. The executor writes the bytes and discloses them under
    `E2`; this ruling is the authorisation, since `HD-64`'s boundary reaches only its own bullet
    and `HD-67` only its two blocks. Chosen over banking because such a rider's redeem-when
    would be the very write this round is already making.
20. **Contract `:9`'s `signature_owner` field stays as it is** (2026-08-29, answering the same
    read's `M-1`): a machine-read owner-delegating key, test-pinned, already carrying its holder
    phrase. `HD-67` is corrected forward (`HD-59`) to count three sites and name this disposal,
    in the commit that carries this ruling. The read's `O-1` is accepted with it: ruling 11's
    *re-pointed at the new blob* has had no object since `184387c`, `HD-67`'s *fifth
    post-signature write* is what is executed, and ruling 11 is read that way from here.
21. **`policy` is `CONSTRUCTION-LEDGER.md`** (2026-08-30, step 5, the user's word 「账本」): the
    executor's proposal stands as written into `harness.json` at `cbaee8e`. The ledger's
    header block is this repository's closeout policy — what may enter, what may not, where
    each other kind of conclusion goes, the caps and their check — and a separate file would
    be a second copy of it. Stated because the question was misread once: `policy` is not
    the split's product. The split produced `RULES.md` and left `CONSTRUCTION-CHECKLIST.md`
    as this repository's `rules`; `policy` is ruling 9's second field, the file
    `ORCHESTRATION.md`'s *Reading the caller's policy file* has always asked a caller for.
22. **§12's first paragraph goes entire** (2026-08-30, answering the executor's question 1 in
    journal `core-only-layer-2026-08-30.md` §7). The user's ground: v4 depends on no v1/v2
    component, so nothing about them is referenced and all of it goes — verified before the
    ruling was taken: the contract's remaining v1/v2 mentions are §13's version-boundary
    statements about results and history, not dependencies. The two obligation sentences the
    executor kept at `228df32` (immutability of v1/v2 material; `SPEC_GAP` on referencing a
    non-nominated old component) are history together with the nomination list and go with
    it; `HD-67`'s named block governs over the executor's reading of its criterion, for this
    block. A pre-submission correction (`E9`: no FULL yet), disclosed under `E2`, recorded in
    `CONTRACT-V4-SIGNATURE.md` as the sixth post-signature write.
23. **`HD-68` is ruled** (2026-08-30, answering question 2): the wikilink at contract `:29`
    (`:36` at `607728a`) ceases to be a followable link, in this round, as a pre-submission
    correction; rider `contract-wikilink-tier` is deleted in that commit. The entry lands in
    the commit that carries this ruling.
24. **Item J joins the Sketch and this round** (2026-08-30, answering question 3): the twelve
    product-tier sites naming instrument-held artifacts that no item owned —
    `document-harness/README.md` `:16` (four record names), `:20` (a path token into
    `tooling/tests/`), `:24`, `:26`, `:29`; `document-harness/EXECUTION.md`'s six;
    `document-harness/REVIEW.md:90` — are **deleted, not de-named**. The user's words: 倾向删除，
    不能再名字+holder句子. Where a sentence cannot stand without the reference, the sentence is
    rewritten without it; the executor writes and discloses. Acceptance 1 then reaches zero
    except item D's two stubs, which are round 2's. Question 4 — whether `RULES.md`'s `##
    Execution side` gloss is too narrow for a file a product run answers to — is left to the
    FULL: wording, no actor's action changes today.
25. **§12's heading and §14's "dependency map" are corrected in place under `HD-63`**
    (2026-08-30, answering the corrections pass's question 2): after ruling 22 the section holds
    no dependency map, so the heading *Dependency and historical map (plan §7)* and §14's
    *dependency map are frozen* are statements true at signing and made false by a later
    deletion — exactly `HD-63`'s standing class, so no new entry is opened; the user confirms
    the write happens now, as a pre-submission correction, the executor writing and disclosing
    the bytes under `E2`, `CONTRACT-V4-SIGNATURE.md` recording the seventh post-signature write.
26. **The two `historical-only` survivors go** (2026-08-30, answering question 3, on ruling 24's
    deletion principle): `document-harness/README.md:30`'s *Predecessors … every old root is
    historical-only for v3 per N0 record §3* sentence is deleted; the docstring at
    `tooling/rsclib/document_harness/__init__.py:12` drops its reference to the contract's
    default and to the N0 record and keeps the code fact — the two primitives are adaptations,
    not imports.

**Ruling 24's twelve are nine, corrected forward (`HD-23`, 2026-08-30).** The corrections pass
measured that `EXECUTION.md:375`, `:377` and `:394` are not instrument-held: the paragraph they
sit in says the five battery commands are *named here rather than written as paths (`E10`)
because their scripts live in the caller's tree* and warns that a name may also belong to an
unrelated file in this repository — which is why the harness-only sweep reports them, resolving
bare names against this repository's basenames. They are the compliant caller-held form,
deleting two would strike entries from the enumeration `HD-42` guards, and the third is
caller-side history of the class ruling 19 kept. The plan's 34-site table and the journal's first
§4 table classed them as this instrument's; the sentence above stands as written and this
paragraph is the correction. Item J is nine sites, all carried out at `b235701`.

**Disclosed at opening, not softened.** Before the card was rendered the orchestrator ran
`dtw dispatch --read db1bfa1` to see the prompt's shape; that command writes the freeze marker
`.harness/review-pending.json` as a side effect. No reader session was launched on it, no commit
landed while it existed, and the orchestrator deleted it by hand — so in `E9`'s terms no
dispatch occurred, since a dispatch has occurred only when its record's commit lands. The
marker is per-checkout and gitignored; nothing committed carries it.

## Measured starting state — 2026-08-29 at `607728a`

### What the harness carries today: 58 files of 409

| # | row of `CONSTRUCTION-INDEX.md` | files |
|---|---|---|
| 1 | `contract/Document-Work-Assurance-Contract-v4.md` | 1 |
| 2 | `schema/document-assurance-v3/` | 14 |
| 3 | README · EXECUTION · REVIEW · ORCHESTRATION | 4 |
| 4 | `ONBOARDING.md` | 1 |
| 5 | `document-harness/templates/` | 2 |
| 6 | `tooling/dtw.py` · `tooling/do-the-work.py` | 2 |
| 7 | `tooling/rsclib/document_harness/` | 22 |
| 8 | `tooling/hooks/` 4 + `assurance/templates/run-v2/` 8 | 12 |
| | **total** | **58** |

**Row 8 disagrees with itself**: its prose says *"the two caller-side guards a caller wires into its
own `pre-commit`"* while its count takes all four files in `tooling/hooks/`. Under ruling 5 the
disagreement dissolves rather than being repaired — see item C.

### The rule surface: 36 citations, and 26 of them are shared

Counted over the five product documents with
`grep -ohE '`(E[0-9]{1,2}|R[0-9]{1,2})`'`, minus the one false positive named above:

| what the cited rule says | citations | does a product run obey it? |
|---|---|---|
| never review, verify or sign your own work | 5 | **yes** |
| the per-round review budget: one FULL, at most one approved fix, one VERIFY | 5 | **yes** |
| how findings route — bank, HarnessIssue, or the caller's own bank | 4 | **yes** |
| whether a thing should exist at all is the user's question, not the reviewer's | 3 | **yes** |
| the preview card before starting, and waiting for the user | 3 | **yes** |
| independence is decided by who set the question | 2 | **yes** |
| what a review record is called and where it goes | 2 | **yes** |
| measure last; a figure is invalidated by any later change | 1 | **yes** |
| the handoff is one commit or range, with no per-acceptance argument | 1 | **yes** |
| **subtotal — shared** | **26** | |
| the instruction layer is exactly these nine files, and how to amend them | 8 | **no** — this instrument's own rule text |
| the announced/frozen surface | 1 | **no** — this instrument's own bytes |
| never trust a guard you have not seen fail | 1 | construction-leaning |
| **subtotal — this instrument's own** | **10** | |

**This is the measurement ruling 2 rests on.** The checklist is not a construction file with
product rules leaking into it; it is the *only home* of rules both sides obey, and that home was
filed on the construction side.

### The reference breakage: 48 sites, of which 34 are this batch's

Three trees, one instrument (`tooling/sweep_refs.py`), over the nine members:

| tree | files | non-resolving sites |
|---|---|---|
| this repository | 409 | **14** |
| history-stripped (batch `CORE-SET`'s) | 120 | 3 |
| **harness-only** | **58** | **48** |

**The 14 are not defects and must not be "fixed".** All are a backticked bare filename, which is
the form the membership rule *requires* for a caller-held artifact — *a caller-held path is named,
never written as a path token*. Twelve name a caller's own run artifacts (`build_run.py`,
`check_shells.py`, `write_audit.py`, `smoke_test.py`, `run_p4_tests.py`, `run_p5a_tests.py`,
`audit-rounds.md` ×2, `v3-review-full-86defbc.md`,
`user-decision-triage-comparator-environment-defects.json`, `v3-review-full-fef3a2e.md`,
`review-verify.json`); two are deliberate history (`Document-Work-Assurance-Contract-v3.md`, left
in git history by `HD-62`, and `review.schema.json`, which round `V1-RESULT-RETIRE` retired and the
contract names in the past tense). That count moved 13 → 14 in that round, the new one being the
past-tense sentence it wrote.

**34 break only because the tree was stripped.** 3 members absent · 5 markdown links · 2 path
tokens · 24 bare names carrying 14 distinct targets: `CONSTRUCTION-CHECKLIST.md`,
`CONSTRUCTION-INDEX.md`, `CONTRACT-V4-SIGNATURE.md`, `HARNESS-DECISIONS.md`, `N0-record.md`,
`W2-record.md`, `supersession-2-signature.md`, `retro-2026-08-03.md`,
`v3-review-verify-2538893.md`, `contract-v4.plan.md`,
`general-harness-v2-architecture-revision.plan.md`, `run_tests.py`, `test_readme_enumeration.py`,
`validate_fixtures.py`.

**The judge for every one is who holds the thing.** A caller holds its own run artifacts, so a bare
name is complete. Nobody on the caller's side holds this instrument's construction history, so the
sentence the rule demands — *its name and its holder* — cannot be completed at all.

**The 34, verbatim at `607728a`. Re-derive before editing.**

```
MISSING  document-harness/CONSTRUCTION-CHECKLIST.md
MISSING  migration/document-work-assurance-v3/v3-harness-operating-contract.md
MISSING  migration/document-work-assurance-v3/v3-harness-review-contract.md
LINK     document-harness/README.md:23        CONSTRUCTION-CHECKLIST.md
LINK     document-harness/EXECUTION.md:13     CONSTRUCTION-CHECKLIST.md
LINK     document-harness/REVIEW.md:8         CONSTRUCTION-CHECKLIST.md
LINK     document-harness/ORCHESTRATION.md:7  CONSTRUCTION-CHECKLIST.md
LINK     document-harness/ORCHESTRATION.md:39 CONSTRUCTION-CHECKLIST.md
PATHTOK  document-harness/README.md:20        tooling/tests/document_harness/test_readme_enumeration.py
PATHTOK  document-harness/README.md:26        .githooks/
NAMETOK  document-harness/README.md:16        CONTRACT-V4-SIGNATURE.md · N0-record.md · W2-record.md · supersession-2-signature.md
NAMETOK  document-harness/README.md:24        CONSTRUCTION-INDEX.md
NAMETOK  document-harness/README.md:26        v3-review-verify-2538893.md
NAMETOK  document-harness/README.md:29        general-harness-v2-architecture-revision.plan.md
NAMETOK  document-harness/EXECUTION.md:13     CONSTRUCTION-CHECKLIST.md
NAMETOK  document-harness/EXECUTION.md:110    W2-record.md
NAMETOK  document-harness/EXECUTION.md:350    test_readme_enumeration.py
NAMETOK  document-harness/EXECUTION.md:375    run_tests.py
NAMETOK  document-harness/EXECUTION.md:377    validate_fixtures.py
NAMETOK  document-harness/EXECUTION.md:394    run_tests.py
NAMETOK  document-harness/EXECUTION.md:400    retro-2026-08-03.md
NAMETOK  document-harness/REVIEW.md:8         CONSTRUCTION-CHECKLIST.md
NAMETOK  document-harness/REVIEW.md:89        W2-record.md
NAMETOK  document-harness/ORCHESTRATION.md:51 HARNESS-DECISIONS.md
NAMETOK  contract/…-v4.md:16   CONTRACT-V4-SIGNATURE.md
NAMETOK  contract/…-v4.md:27   N0-record.md
NAMETOK  contract/…-v4.md:28   W2-record.md
NAMETOK  contract/…-v4.md:31   supersession-2-signature.md
NAMETOK  contract/…-v4.md:33   contract-v4.plan.md
NAMETOK  contract/…-v4.md:254  N0-record.md
NAMETOK  contract/…-v4.md:365  CONTRACT-V4-SIGNATURE.md
```

### The contract's provenance — ruling 4's object, in blocks rather than lines

| block | size | what it is | verdict |
|---|---|---|---|
| §12 *Dependency and historical map*, first two paragraphs | ~12 lines | v1/v2 immutability, A4 as accepted v2 history, the nominated reuse candidates recorded in `N0-record.md` | **construction history** |
| §12's third paragraph | ~6 lines | what was removed from the v3 default interface and may never return without an approved amendment | **operative for a caller — stays** |
| `:24-33`, the merged-sources paragraph | 10 lines | which three documents v4 merged, their blob hashes, signature dates and record filenames | **construction history** |
| the signature-semantics header and §14 | a few lines | that a signature binds and where the record lives | **operative, but the record can be named by holder rather than by filename** |

Three of the seven sites already carry *held by this instrument's own construction record*. **That
is the compliant form, and it is also the evidence that whoever wrote it already knew the caller
could not reach these** — and answered by labelling rather than by removing. Ruling 4 chooses
removal.

### The code the caller receives and cannot use

Measured by reading the modules. Three of the four hits a grep for *construction* produced
(`checks.py`, `instruction.py`, `review_subject.py`) are the ordinary English word and are **not**
coupling.

| # | site | size | note |
|---|---|---|---|
| 1 | `dispatch.py` | **≈423 of 1,005 lines** — `--range` ≈123, `--read` ≈105, `--construction-executor` ≈195 | three modes only a construction round uses |
| 2 | `cli.py` | the `dispatch` handler from `:167`, 23 construction references | their command-line entry |
| 3 | `tooling/hooks/layer_path_check.py` | 134 lines | **under ruling 5 this becomes general rather than moving** — it reads the harness members plus the local declaration |

One hard-coded constant in product-tier code names a file that does not travel: `dispatch.py:776`,
`CONSTRUCTION_EXECUTOR_CHARTER = "document-harness/CONSTRUCTION-CHECKLIST.md"`. A second,
`dispatch.py:549`, names the retired review-side stub as every cold reviewer's standing
instruction, and `test_dispatch.py` pins it in three hand-written constants.

### The declaration precedent this repository already has

`.harness/scan-surfaces.json` — `{"review_record_dirs": ["migration/document-work-assurance-v3/"]}`
— is a per-repository declaration of a repo-local surface, read by `caller.py:42` and written by
`dtw init`. **Membership additions could take the same shape.** It is per-checkout and gitignored,
which is a known cost: every fresh clone rewrites it.

## Open questions — answered at round open, before any work

**All six answered 2026-08-29 — rulings 8–13 in order.** The questions stand as written.

1. **What is the shared half called and where does it live?** It decides what a dispatch prompt
   points at, and therefore whether the two stubs survive (ruling 6's condition).
2. **How does a caller declare its additions?** Ruling 7 defers the choice; the candidates are:
   **(a)** a new declaration file; **(b)** a key added to `.harness/scan-surfaces.json`, which
   already exists and is already read; **(c)** no machine at all — the addition is declared in the
   caller's own addition document as prose, and the guard reads that. **`E6` must be answered
   first for whichever is chosen: what decision changes if the declaration is absent?** If the
   honest answer is *none*, (c) wins by that rule.
3. **How does the split membership rule read?** One sentence naming harness members and a second
   naming the mechanism for additions — or something else. This is the sentence the round exists to
   change, and changing it is why the round is design.
4. **Which route do the contract's provenance blocks take?** Removing pure history does not change
   what the contract requires, which is a different class from the two in-place corrections round
   `V1-RESULT-RETIRE` obtained rulings for. **Whether that difference earns a lighter route is the
   user's**, and the round must ask rather than assume.
5. **Where does the product run happen and who builds it?** Ruling 3 makes it acceptance; the
   2026-08-23 ruling puts it in a caller repository. Which repository, and whether it is a scratch
   one or a real piece of work, is unanswered.
6. **How is the batch cut into rounds?** The rule split, the code split, the contract, and the
   product run are plausibly four; nothing here fixes that.

## Out of scope

- OUT: the candidate-isolation design question (queue ③, still unruled).
- OUT: `dispatch-economy` (queue ④).
- OUT: declaring `HD-66`'s plugin trigger fired. This batch is that entry's option two; failure is
  evidence toward the plugin, and the declaration stays the user's.
- OUT: sparse-checkout as a substitute — it materialises fewer files and makes no reference resolve.
- OUT: repairing the 14 sites that fail on the full repository. Repairing them breaks the rule they
  satisfy.
- OUT: moving `CONSTRUCTION-CHECKLIST.md` out of `document-harness/` (ruling 8).
- OUT: folding `review_record_dirs` into `harness.json` (ruling 9).

## Sketch of the work — not a decomposition; the executor writes its own

- **A — the rule split.** The checklist divides along the 26/10 line measured above. The five
  product documents' 11 path references and 36 code citations follow whichever names result.
  The 26/10 line is the measurement, not the criterion: the judge for every rule, cited by a
  product document or not, is the table's third column — *does a product run obey it* — so an
  uncited rule goes where that answer puts it. And the checklist, once split, names `RULES.md`
  as its counterpart, so a construction session dispatched with the checklist as charter reaches
  the shared rules by the sentence the dispatch already carries — *read it, and the counterpart
  it names*.
- **B — the membership rule and its guard.** The sentence per question 3; `layer_path_check.py`'s
  `LAYER` and `sweep_refs.py` both import from it rather than being edited in parallel, so they
  follow. Since ruling 10 the sentence is two, and since ruling 9 the guard and the sweep also
  read `harness.json`'s `rules`.
- **C — the code split.** `dispatch.py`'s three construction modes, `cli.py`'s branches, and both
  hard-coded constants. `CONSTRUCTION-INDEX.md`'s tier table changes with every one, row 8 included.
- **D — the stubs.** Removable once no dispatch prompt names them (ruling 6's condition); that
  frees `dispatch.py:549` and three hand-written test constants.
- **E — the contract.** The two provenance blocks, under whatever question 4 rules. §12's third
  paragraph stays.
- **F — the product run.** Ruling 3's acceptance, in a caller repository.
- **G — riders.** `checklist-cited-not-carried` redeemed; `onboarding-carries-construction` checked
  for whether it redeems with it.
- **H — the caller config** (ruling 9). `harness.json`: its two fields, `dtw init`'s empty
  default, the guards reading `rules` and the ONBOARDING item in round 1; `dtw dispatch` naming
  the declared rules in round 2. Every guard change mutation-tested with a negative control
  (`E4`).
- **I — this repository as a caller** (ruling 14). The three-line `CLAUDE.md` and this
  repository's own `harness.json`.
- **J — the product-tier residue** (ruling 24, added 2026-08-30). The twelve references from
  product-tier documents to instrument-held artifacts that A–I reached: deleted, the sentence
  rewritten where it cannot stand without them. Round 1.

## Acceptance (done = ?)

1. A harness-only tree, built by `git archive` and made a git repository, reports **zero**
   non-resolving sites naming an instrument-held artifact. Caller-held bare names are reported
   **separately and still present** — collapsing the two classes is how this defect hid.
2. `python tooling/sweep_refs.py` on both trees, output pasted.
3. On that tree: `dtw --help` exit 0 · `dtw init` into a fresh repository exit 0 · the caller-side
   guards exit 0.
4. **A real product run completes on that tree** (ruling 3): a run directory built, an instruction
   frozen, a reviewer dispatched from the mounted harness, a verdict recorded, the run closed.
   Which repository it runs in is question 5's.
5. `grep -rn 'CONSTRUCTION-CHECKLIST' <harness tree>` returns nothing, or only what a ruling
   admitted, each accounted for in a commit body.
6. No file in the harness tree holds a construction-only code path; `dispatch.py`'s and `cli.py`'s
   line counts re-measured either side of the split.
7. `python -m pytest tooling/tests -q` green on the full repository, delta accounted.
8. `CONSTRUCTION-INDEX.md` re-measured by its own commands, and row 8's prose agreeing with its
   count.
9. The guards exit 0 and the membership rule resolves N/N for whatever N it ends up naming, on
   **both** trees.
10. Rider `checklist-cited-not-carried` deleted in the commit that earns it.
11. On the harness-only tree, `dtw init` writes a default `harness.json`; with one rule file
    declared, every `dtw dispatch` mode left in the product tier carries the line naming it in
    its prompt and both guards scan it — each guard change seen red once (`E4`), paired with a
    negative control.
12. This repository's own `harness.json` declares the checklist, and `layer_path_check.py`
    blocks a dangling path newly written into it — seen red once.

## Steps — round 1 `CORE-ONLY-LAYER`

Checked off as each lands; a box that reads done names the commit that made it so.

- [x] 1. **Open.** `E11` card rendered and approved 2026-08-29; rulings 16–18 taken off it;
  `base_commit` `db1bfa1` written above; the ledger's queue-head row rewritten in place. This
  commit.
- [ ] 2. **`HD-67`** — the ruling commit for the contract's provenance (rulings 4, 11, 18), in
  `HARNESS-DECISIONS.md` `§live`, before the read.
- [x] 3. **DONE.** Read at subject `a542c6d`, its own `claude -p` session, narrow form as
  ruled; record `v3-cold-read-a542c6d.md` committed unchanged at `ac39d35`, marker deleted in
  that act: **1 must-fix, 1 low, 7 observations**, no verdict, no budget. `M-1` (a third
  `CONTRACT-V4-SIGNATURE.md` site `HD-67` did not count) and `L-1` (a bare name for a deleted
  schema at contract `:302`) both put to the user the same sitting → rulings 19 and 20, `HD-67`
  corrected forward — the `E10` channel does not apply, the object being a `§live` entry.
  `O-5` (README `:22` stale "tenth member", a touch record owed on rider
  `r9-terminal-no-carrier`) and `O-6` (a test docstring's row count) go to the executor with
  the instruction; `O-2`, `O-3`, `O-4`, `O-7` confirm and owe nothing. Original text: `dtw
  dispatch --read <tip>` → cold `claude -p` → record committed unchanged, freeze marker deleted
  in that act; must-fix, if any, takes the `E10` channel.
- [x] 4. **DONE.** Cold `claude -p` executor, dispatched with `dtw dispatch
  --construction-executor` plus the instruction, subject and this plan; 82 minutes; four
  candidates — `cbaee8e` (H guards' half + I), `4b81dd9` (A + B, rider
  `checklist-cited-not-carried` deleted), `228df32` (E under `HD-67`, rulings 19–20 applied),
  `eadcfe0` (journal `core-only-layer-2026-08-30.md`). The orchestrator re-ran at the tip: 853
  passed, both guards exit 0, sweep 13 on this repository. It reported the `policy` proposal and
  four questions (journal §7). Original text: execute items A, B, E, G, the guards' half of H,
  and I; the executor proposes `policy` and reports back; the orchestrator hand-edits nothing.
- [x] 5. **DONE.** `policy` ruled 「账本」 → ruling 21, value unchanged; the four questions
  answered as rulings 22–24 and `HD-68`, the fourth left to the FULL. Original text: the
  proposal put to the user before the FULL; a changed answer lands as a pre-submission
  correction.
- [x] 5b. **DONE.** Second cold executor, 19 minutes, three pre-submission corrections:
  `b235701` (item J, nine of the twelve — three re-classified, see the forward correction under
  the rulings), `322fd1c` (rulings 22 and 23 in one contract commit, `E2` disclosed, signature
  record's sixth block, rider `contract-wikilink-tier` deleted), `70839b1` (journal §3/§4/§7
  written forward). Re-measured by the executor at `322fd1c` and by the orchestrator at
  `70839b1`: 853 passed, both guards exit 0, sweep 13 here and **33** on the harness-only tree
  (45 → 33). Three questions came back and became rulings 25–26 plus the re-classification.
  Original text: §12 ¶1 deleted entire and the `:29` wikilink de-linked in one contract commit;
  item J's twelve deletions; the journal's §7 answered forward; acceptance 1 and 2 re-measured.
- [ ] 5c. **Corrections, second pass** (rulings 25–26), a third cold executor dispatch before
  any FULL, still pre-submission under `E9`: §12's heading and §14's phrase under `HD-63` in one
  contract commit with `E2` disclosure and the signature record's seventh block;
  `document-harness/README.md:30` deleted and the `__init__.py` docstring rewritten; the
  journal's second-pass questions answered forward and acceptance 1 and 2 re-measured.
- [ ] 6. **FULL** on `db1bfa1..<tip>` via `dtw dispatch --range` → cold `claude -p` reviewer →
  record committed unchanged → at most one user-approved fix → targeted VERIFY → closeout: this
  checklist, the ledger row, riders, and a journal if detail needs a home.

## Resume pointer

当前指针: **round 1 `CORE-ONLY-LAYER` OPEN at `db1bfa1`; steps 1–5b done, the candidate stands
at `70839b1` plus this ruling commit; step 5c (the second corrections dispatch) next, then the
FULL.** The step list above is the pointer; a cold session reads it, then
`CONSTRUCTION-LEDGER.md`'s queue-head row, then continues at the first unchecked box. `§live`
holds twelve entries, `HD-67` (with its forward correction) and `HD-68` among them. One thing
stays open by design and is settled at its round's opening, not before: which piece of work the
product run is (ruling 12, round 3).

## Notes

- **Why the A/B/C framing died.** It asked which repair to buy. The user asked a different question
  — what the construction side *is* — and answered it: an instance of the harness applied to
  itself. Repairs follow from that; they do not substitute for it.
- **Why the 14 full-repository sites stay.** The rule requires a caller-held artifact be named
  rather than pathed. A round that "fixes" them breaks the rule it thinks it serves. The number
  looks like a defect and is not one, which is exactly why it is written down.
- **What this batch is evidence for.** `HD-66` made the distribution form conditional on core
  distribution being shown impossible. This is the attempt. Neither its success nor its failure is
  this file's to declare.
