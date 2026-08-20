# Cold read — the instruction layer at `4410899`

`E10` read. Not a round (`R3`): no verdict, no budget spent, and the output is findings tiered
must-fix / low / observation. Routing is `E10` / `R9` / `R10`'s, not mine.

**Findings: 0 must-fix, 3 low, 3 observations.** The layer's newest clause — `E10`'s
*"a caller-held path is named, never written as a path token"*, landed by the round this
subject closes — has **one live counterexample inside the layer it governs**:
`EXECUTION.md:260` still writes the paragraph map's location as
`` `ResearchSystem/assurance/runs/<run-id>/control/paragraph-map.json` ``, a path that
resolves nowhere in this repository. It survived the round's own sweep because both the guard
and the sweep match path tokens with a regex that rejects `<` and `>`, so a token carrying a
placeholder segment is invisible to them — proven below with a positive and a negative control
(§3.3). That is `L-1` (bytes supplied) and `L-2` (the clause's description of the guard's reach
is false for that shape). `L-3` re-reports a contradiction a previous read already filed and
that then reached neither the text nor the bank. Everything else the layer asserts that a
command can falsify was run and held: the fifteen-file `E2` pack, the three frozen blob ids,
the three `E10-sync` mirrors, the `(41/41 green)` fixture claim, the `.githooks/pre-commit`
wiring, and every commit id cited in a member.

**Named `cold-read` rather than `checkpoint-read`**: all ten members were read end to end at
this subject, none by citation.

**Standing instructions read.** `…/v3-harness-review-contract.md` (the stub, member 7) →
`ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` in full, both sides, per the stub's
*"It is your standing instruction and its own counterpart; read all of it."*
`ResearchSystem/HARNESS-DECISIONS.md` read end to end (504 lines): the header (1–27) and
`§live` (28–195, ten entries — `HD-49`, `HD-50`, `HD-47`, `HD-44`, `HD-41`, `HD-36`, `HD-35`,
`HD-34`, `HD-23`, `HD-9`) are what `E10`'s tail requires, and `§implemented` (196–504) was read
too because claims I checked cite `HD-46`, `HD-45`, `HD-40`, `HD-38`, `HD-37`, `HD-33`, `HD-22`,
`HD-21`, `HD-20`, `HD-19` and `HD-2`. Cited by section, never by blob, per that clause.

---

## 1. Subject, re-derived

```
$ git rev-parse HEAD
4410899485620a761178569855eca1a7767607b1

$ git status --porcelain --untracked-files=all
(no output)

$ git log --oneline 4410899485620a761178569855eca1a7767607b1..HEAD
(no output)

$ cat .harness/review-pending.json
{
 "subject": "4410899485620a761178569855eca1a7767607b1",
 "dispatched_at": "2026-08-20T02:25:36+00:00"
}

$ git check-ignore -v .harness/review-pending.json
.gitignore:18:.harness/	.harness/review-pending.json
```

Subject = branch tip; worktree clean and untracked-free, so the working-tree bytes are the
subject bytes. Every quotation that carries weight in this record was nonetheless taken from
the object store (`git show <sha>:<path>` / `git cat-file -p <blob>`), not from the worktree.
The marker's subject equals the dispatched SHA, so `E9`'s window opened at that timestamp and
closes when this record's commit lands; `git log 4410899..HEAD` is empty, so the branch has
taken no commit inside the window. From the moment this file is written, exactly one path
falsifies the untracked-free line — this record, until the orchestrator commits it.

One checkout property, because it bears on any digest computed here: `core.autocrlf` is on, so
worktree copies are CRLF while blobs are LF — `HARNESS-DECISIONS.md` is 49 159 B as a blob and
49 663 B on disk, exactly one CR per its 504 lines. `HD-40`'s sha256 correction is the recorded
version of this trap; every digest and line count in this record was taken from the object
store, never from disk.

The subject commit is `V3-XREPO-REFS-CLOSEOUT-v1`, a closeout. It touches no member: the
layer's bytes here were written by `1cb80bb` / `48b6c5f` / `dd18226` / `2937bcd` / `34a5ae9`
(§3.6).

## 2. The member set and each member's blob

Derived from `E10`'s own sentence at the subject (`CONSTRUCTION-CHECKLIST.md:94-105`), which
reads *"exactly these ten paths and nothing else"* and then enumerates them. Nothing was taken
from the dispatch, which enumerates nothing. Blob ids per `E10`'s *"a read's record states the
blob id of each member it read, because citation depends on it"*:

```
$ git ls-tree -r 4410899485620a761178569855eca1a7767607b1 -- <the ten paths>
 1  92cbaea309d633f01902caa3dca57d1d622f9f97   231 lines   18410 B  ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md
 2  be4766fc1496b41eb6d8f0b3c0f50acb698fd934    40 lines    9630 B  ResearchSystem/document-harness/README.md
 3  6dc79f3fd20e1b142629a443aeb4c653ccbca30f   469 lines   32737 B  ResearchSystem/document-harness/EXECUTION.md
 4  4a407f65beb1e73f81e2ffb1468708cb641cf669   285 lines   18036 B  ResearchSystem/document-harness/REVIEW.md
 5  80f42658a2961eeb10a168bd7bd729121c6c05ae    95 lines    6389 B  ResearchSystem/document-harness/ORCHESTRATION.md
 6  70f3e5dda9ce069489432a592a025b9da36cf0e0     5 lines     541 B  ResearchSystem/migration/document-work-assurance-v3/v3-harness-operating-contract.md
 7  bc395e1c22af05aeacb0ed0b9813b66c8de75644     5 lines     984 B  ResearchSystem/migration/document-work-assurance-v3/v3-harness-review-contract.md
 8  68031fa2ca31272e31da0d42a9a02189d28fcc21   124 lines    6480 B  ResearchSystem/contract/Document-Work-Assurance-Contract-v3-supersession-1.md
 9  e1a2f26b1d8d323d11e900f8137dea222b6571c1   113 lines    7421 B  ResearchSystem/contract/Document-Work-Assurance-Contract-v3-supersession-2.md
10  09aa869962f592c2f86c9379be0ef3eb7d2232ff    44 lines    2812 B  ResearchSystem/schema/document-assurance-v3/paragraph-map.schema.json
```

Ten paths enumerated, ten present, none missing. Members 8 and 9 are also `E2`-frozen, and
their blob ids are the ones `E2` itself names (§3.1) — so for those two the freeze list and the
tree agree by inspection, which is what `E2` says it wants.

`ResearchSystem/HARNESS-DECISIONS.md` is **not** a member and is not listed above; it was read
under `E10`'s tail clause, by section (`§live`), never by blob, exactly as that clause requires.

## 3. What was checked, and what the commands returned

### 3.1 `E2`'s freeze surface — three blobs and one directory

```
$ git ls-tree -r 4410899… -- ResearchSystem/contract/
100644 blob 68031fa2ca31272e31da0d42a9a02189d28fcc21	…-supersession-1.md
100644 blob e1a2f26b1d8d323d11e900f8137dea222b6571c1	…-supersession-2.md
100644 blob b2dbdf752d8c155e4c65b14b5f420b880b8184a1	Document-Work-Assurance-Contract-v3.md

$ git ls-tree -r --name-only 4410899… -- ResearchSystem/schema/document-assurance-v3/
(15 files: assurance-work-state, assurance, candidate-record, common,
 document-assurance-profile, document-work-spec, document-work-spec.v2, harness-issue,
 instruction-coverage-audit, local-check-spec, paragraph-map, resolved-assurance-plan,
 review, review.v2, user-decision)
```

`E2` names `b2dbdf75…` / `68031fa2…` / `e1a2f26b…` and *"fifteen files"*. All three prefixes
match, and the pack holds exactly fifteen. `HD-44`'s *"这十八件"* (3 + 15) is the same set
counted the other way, and it agrees. The `README.md:22-25` rows enumerate those fifteen
schemas by name across four rows (8 core + 2 evidence + 4 review/disposition + 1 paragraph
map); the enumeration and the directory are the same fifteen.

### 3.2 The `E10-sync` three mirrors

`HD-22` makes membership-sentence synchronisation a per-touch checklist item across three
sites. All three carry the same ten paths in the same order at this subject:

- `CONSTRUCTION-CHECKLIST.md:94-105` — the membership sentence;
- `ResearchSystem/tooling/hooks/layer_path_check.py` `LAYER` (comment: *"Mirrors E10's
  membership sentence"*);
- `ResearchSystem/tooling/tests/document_harness/test_precommit_checks.py:164-175` `EXPECTED`,
  a hand-written tuple asserted equal to `LAYER` — `E5`-clean, since the expectation is not the
  module's own constant.

### 3.3 The path-token class — the sweep, and what the sweep cannot see

Every backtick token and markdown-link target in all ten members was enumerated at the subject
and resolved against the subject tree (three roots: repository root, the member's own
directory, and under `ResearchSystem/`). Unlike `layer_path_check`, my tokenizer does **not**
apply a shape regex, so tokens carrying a `<placeholder>` segment are included:

```
=== ResearchSystem/document-harness/README.md
  :36  .harness/review-pending.json                                      -> nowhere
=== ResearchSystem/document-harness/EXECUTION.md
  :260 ResearchSystem/assurance/runs/<run-id>/control/paragraph-map.json -> nowhere
=== ResearchSystem/document-harness/REVIEW.md
  :139 .harness/review-pending.json                                      -> nowhere
=== ResearchSystem/contract/…-supersession-1.md
  :89  schema/document-assurance-v3/review.v2.schema.json                -> under-RS-only
=== ResearchSystem/contract/…-supersession-2.md
  :60  assurance/runs/                                                   -> nowhere
  :83  schema/                                                           -> under-RS-only
  :99  templates/run-v2/                                                 -> nowhere
```

Disposition of each, against `E10`'s clause:

- The two `.harness/review-pending.json` sites are inside the clause's own carve-out — *"a
  run-time marker this repository itself writes counting as resolving whether or not it exists
  at rest"*. Verified rather than assumed: `.harness/` exists in this checkout and holds
  `review-pending.json` and `runs.jsonl`, and is `.gitignore`d at line 18 (§1), which is why
  the tree scan cannot see it. **Compliant.**
- The four supersession sites are `E2`-frozen bytes, which the clause excepts *"while they are
  frozen"*, and `HD-20` banks any supplied bytes for them until `E2`'s ruling exists. Rider
  `frozen-path-prefix` already carries all four, refined at this same subject. **Banked, not
  mine to re-file.**
- `EXECUTION.md:260` is in none of those categories. It is a token written with the prefix the
  guard recognises, whose target exists at no path of this repository — the round's own class
  definition, quoted from its journal §1: *"a reference written in an instruction-layer member
  whose target exists at no path of this repository."* → **`L-1`**.

Why it survived. `layer_path_check.unresolved_tokens` filters candidates through
`PATHLIKE = ^[A-Za-z0-9_.\-/]+(?:\.(md|py|json|yaml|yml|txt|js)|/)$`, which rejects `<` and
`>`. Run against the real bytes, with the defect's real shape and a control on each side, per
`R8`'s *"reproducing the real defect shape"*:

```
$ python -c "… from hooks import layer_path_check as L; L.unresolved_tokens(root, EXECUTION, text)"
'the real :260 token'                          -> []
'same token, no placeholder (positive control)' -> [('ResearchSystem/assurance/runs/p5a-shells/control/paragraph-map.json',
                                                     'does not resolve from the repo root')]
'a token that does resolve (negative control)'  -> []
```

The positive control shows the guard's first branch does fire on this exact target when the
placeholder is removed; the negative control shows it stays silent on a resolvable token. So
the guard is not broken — it is **shape-blind**, and `E10:147-153` describes its reach without
saying so → **`L-2`**.

The round's own sweep inherited the same blindness: its journal §2 states `PATHTOK` is matched
by *"layer_path_check's own pair"* — the same regex — so its "before" listing of 20 hits and
its "after" listing of 16, on which *"every remaining `PATHTOK` is accounted for"* rests, could
not contain `:260`. `sweep_refs.py` itself is **not in the repository** at this subject
(`git ls-tree | grep sweep_refs` → absent; `HD-50` moves its admission to R3), so the sweep is
not reproducible here; that is already the user's routing and I file nothing for it.

Class completeness (`E7`, `HD-41` ④): the layer contains exactly **two** placeholder-bearing
path tokens. The other, `REVIEW.md:132` `` `<control root>/evidence/review-full.json` ``, is
the **compliant** form — it names a location relative to the run's own control root and carries
no repository prefix, so it can neither resolve wrong nor land on another repository's bytes.
That contrast is where `L-1`'s replacement bytes come from.

### 3.4 Commit ids cited in members

`CONSTRUCTION-CHECKLIST.md:14-19` (new this round) rules that a cited commit id this repository
does not have belongs to the repository this one was extracted from, and that *"a citation
naming its own repository is read as written; a silent one means that one."* Every hex id in
the ten members, resolved:

```
0d73a5f    commit   EXECUTION.md:382
418b89c    ABSENT   EXECUTION.md:406        6fd0ae3    ABSENT   EXECUTION.md:383
7011916    ABSENT   CONSTRUCTION-CHECKLIST.md:5,10,15
820b287    ABSENT   README.md:36            838c413    ABSENT   EXECUTION.md:331
9ba9bbc    ABSENT   EXECUTION.md:441        a22cca0    ABSENT   EXECUTION.md:250
a8af54c    ABSENT   EXECUTION.md:380        ac1b383    ABSENT   README.md:18, EXECUTION.md:109, REVIEW.md:66
cf51534    ABSENT   …-supersession-2.md:32  ddd773a    ABSENT   EXECUTION.md:378
```

Exactly one of the twelve resolves here, and it is the only one whose sentence names the
instrument — `EXECUTION.md:382-383`, *"its bases: instrument `0d73a5f`, caller `6fd0ae3`"*.
`6fd0ae3` names the caller and is absent; the other ten are silent and absent. The new clause
discharges the whole class with no exception, and the root `README.md`'s *Where the bytes came
from* section it points at exists and names `D:/Thesis` at `e4ffa2b`. **Clean.**

### 3.5 Assertions re-run rather than read

- **`README.md:35`, `(41/41 green)`.** The runner is in this repository
  (`…/N0/fixtures/validate_fixtures.py`) and was executed at the subject:
  `41/41 cases behaved as declared; failures=0`. **Holds.**
- **`README.md:36`, Local enforcement — *"The third, instruction-layer path resolution, runs
  here"*.** `.githooks/pre-commit` exists at the subject, runs `layer_path_check.py` and
  nothing else, fails loudly if the script is missing, and documents the per-machine
  `core.hooksPath` step. **Holds.**
- **`ORCHESTRATION.md:26-28`, *"its three modes are review-side by construction, and none of
  them dispatches an executor"*.** `dispatch.py` exposes exactly `dispatch_of` (product-run
  reviewer), `construction_dispatch_of` (construction reviewer) and `read_dispatch_of` (layer
  reader); `cli.py:144-175` routes `--subject` / `--construction` / `--read` to those three and
  no fourth. **Holds.**
- **Member 7's pinning sentence** — *"`dispatch.CONSTRUCTION_ROLE_INSTRUCTION` … hard-codes
  this path, and `test_dispatch.py`'s hand-written `CHARTER_OUTSIDE` / `MEMBER` constants pin
  it independently (`E5`); the construction dispatch fixture carries `{charter}` as a
  substitution, not the path."* `dispatch.py:545-547` holds the instrument-relative form of
  that path, and `CONSTRUCTION_PROMPT` carries `{charter}`. **Holds** — and it is the sentence
  that put this read's own charter in front of it.
- **`paragraph-map.schema.json`'s description** — *"index, 1-based inclusive lines, SHA-256
  over each block's lines joined with `"\n"` and UTF-8 encoded"*. `instruction.py:98-110`
  computes exactly that (`bytes_digest("\n".join(lines[start-1:end]).encode("utf-8"))`).
  **Holds.**
- **`EXECUTION.md:348-350`, *"A name here may also belong to an unrelated file in this
  repository"*.** It does: `validate_fixtures.py` is one of the five caller-owed battery
  legs **and** the name of a file that exists here under `…/N0/fixtures/`. The hedge is
  earned, not decorative. **Holds.**

### 3.6 What the round wrote into the layer

`git diff --numstat 69fc082 4410899 --` over the ten members: five members changed, **+50 /
−26** (checklist 22/3, `EXECUTION.md` 20/16, `REVIEW.md` 5/4, `ORCHESTRATION.md` 2/2,
`README.md` 1/1); members 6–10 untouched. One `E10` clause added (the caller-held-path rule),
one dead clause deleted
(provenance entries), one `E1` sentence re-pointed to name the carrier and the owner, four
caller-held references demoted to names in `EXECUTION.md` (`:186`, `:343-350`, `:452`, `:455`)
and one in `REVIEW.md` (`:45`), plus two navigation corrections. I checked the deleted provenance
clause left nothing dangling: `README.md:36` still refers to the provenance-entry *check* as
deleted in 2026-07-28, which is a historical statement, not a live obligation, and no member
now imposes a provenance-entry format. The `E1` re-point is consistent with `E3`, which does
name the commit body and the round journal as the carriers.

## 4. Findings

### `L-1` (low; bytes supplied) — `EXECUTION.md:260` writes a caller-held location as a repository path token, against `E10`'s own clause

**Location.** `ResearchSystem/document-harness/EXECUTION.md:258-262`, the *Authoring gate*
section's third bullet:

> generate
> `` `ResearchSystem/assurance/runs/<run-id>/control/paragraph-map.json` `` with
> `` `make_paragraph_map.py` `` (every derived column is machine-written), …

**Ground truth violated.** `CONSTRUCTION-CHECKLIST.md:143-147`: *"a caller-held path is named,
never written as a path token — a member's path tokens resolve in this repository … so that a
reader following a path in this layer cannot land on another repository's bytes or on
nothing."* `ResearchSystem/assurance/runs/` exists at no path of this repository
(`ResearchSystem/assurance/` does exist, holding `templates/run-v2/`, `test/` and
`review-test/`, but no `runs/`), and `HD-33` (implemented) puts run directories in the caller's
repository. Neither carve-out reaches it: it is not `E2`-frozen, and it is not a marker this
repository writes at its own root — `make_paragraph_map.py` writes it into whatever `<run-dir>`
it is handed, in the caller's tree.

**Minimum fix (exact bytes).** Replace the two lines

```
  (M11, Phase C4 — the p3-corr omission made mechanical): generate
  `ResearchSystem/assurance/runs/<run-id>/control/paragraph-map.json` with `make_paragraph_map.py` (every derived column is
```

with

```
  (M11, Phase C4 — the p3-corr omission made mechanical): generate the run's
  `<control root>/control/paragraph-map.json` — the control root lives in the caller, not
  here — with `make_paragraph_map.py` (every derived column is
```

`<control root>` is `REVIEW.md:132`'s existing convention for the same kind of location, and
the schema's own `control_root` field is defined as *"The control root E(C) holding this record
and all other assurance evidence"* — i.e. the run directory — so the replacement names the same
place the old token did, with the holder said and no path to follow wrongly.

**Class sweep for the fix (`E7`, `HD-36` ①).** Exactly one other placeholder-bearing path token
exists in the layer, `REVIEW.md:132`, and it is already in the compliant form (§3.3). Outside
placeholders, the only remaining non-resolving tokens are the two marker sites (carved out) and
the four `E2`-frozen supersession sites (banked, `HD-20`). So the class has **one** site to fix
and the fix above is the whole of it.

**Why low and not must-fix, stated so it can be overruled.** The rule violation is certain and
measured, but no actor is misdirected *today*: the shipped `make_paragraph_map.py` derives
`repo_root = run_dir.parents[3]`, i.e. it assumes precisely the
`<root>/ResearchSystem/assurance/runs/<run-id>` layout the sentence spells, so a run author
following the text gets a working invocation in the caller that grew this harness. What is
wrong is the *presentation* rule the layer adopted one round ago, not the instruction's
outcome. Since the record supplies the exact bytes, `E10`'s free channel applies them
immediately anyway — the must-fix channel would buy only its class-widening, and §3.3 shows
there is no sibling site to widen to. If the orchestrator reads the replacement as changing
what the authoring gate *requires* rather than how it is written, `E10`'s design test sends it
to a round instead; that call is not mine.

### `L-2` (low; no appliable bytes) — `E10`'s description of `layer_path_check`'s reach is false for tokens carrying a placeholder

**Location.** `CONSTRUCTION-CHECKLIST.md:147-153`.

**Ground truth violated.** The clause says the guard *"decides, on the lines a commit adds,
only tokens it can relate to this repository — **written with the single prefix it
recognizes**, or resolving somewhere inside it; a token it can relate neither way it skips as
possibly illustrative."* Measured (§3.3), the guard skips a token written with that prefix
whenever the token carries a `<…>` segment, because `PATHLIKE` rejects `<` and `>` before any
prefix test runs. A reader of the clause believes newly written prefixed tokens are decided;
one whole shape of them is not.

**Downstream decision that goes wrong (`R9`).** An executor amending a member trusts the guard
for the class the clause says it covers and does not hand-sweep it. That is not hypothetical:
it is exactly what happened to `L-1` in the round this subject closes, whose sweep reused the
same regex and then recorded the class accounted for.

**Minimum fix.** Either bound the clause (name the shape filter as a third skip class) or widen
`PATHLIKE` so placeholder segments are stripped before resolution. Both add a clause or change
a guard's behaviour, so both are design under `E10` and neither channel here can write them.
**No bytes supplied deliberately** — per `HD-37` ② this banks with a redeem-when naming a
round-eligible surface: the next round-eligible batch touching `E10`'s guard sentence or
`layer_path_check.PATHLIKE`. Deadline: the next member amendment that relies on the guard for
its class sweep — the moment the same miss can recur.

### `L-3` (low; no appliable bytes; re-report) — `E9`'s exception list and `E10`'s must-fix clause disagree on whether a must-fix amendment spends the round's fix leg

**Location.** `CONSTRUCTION-CHECKLIST.md:85-90` (`E9`) against `:113-115` (`E10`).

**Ground truth violated.** `E9:86-89`: *"has a valid independent FULL already occurred? … yes →
it is the fix round, and it obliges the VERIFY — except an `E10` free-channel byte application,
which is not a round and consumes nothing."* The exception names **one** of the two zero-budget
channels. `E10:113-115` says of the other: a must-fix finding's *"amendment commit plus an
independent re-read of the amended text … is not a round and spends no budget."* An
orchestrator reading `E9`'s enumeration literally, after a FULL has occurred, counts a must-fix
amendment as the round's one user-approved fix and owes a VERIFY; `E10` says it owes neither.

**Downstream decision that goes wrong (`R9`).** Whether a VERIFY is dispatched, and whether the
round's single repair is spent — a budget and verdict-path outcome, which `R9` explicitly
excludes from wording-level. It is live right now: any must-fix this read had returned would
have landed after `XREPO-REFS`'s FULL.

**Re-report, and why that matters.** This was already filed as `O-3` of
`v3-checkpoint-read-136f27f.md`, which dated both sides (`af2905c` wrote the pair clause,
`5f029cd` later wrote `E9`'s exception naming one of the two). At this subject it is **neither
in the text nor in `HARNESS-RIDERS.md`** — I read the bank at the subject blob `2c7369f` and
enumerated all 36 rows by id; none carries it. The nearest two do not: `wl-route` is about
*which* channel a wording-level finding with bytes takes, not about whether the must-fix pair
spends the fix leg, and `freeze-audit` cites `E9` only for the freeze window. So the finding
was recorded, routed nowhere, and would have been lost had a later read not re-derived it.
`R10` says the bank takes what is left; here it did not. The fix is design (adding to `E9`'s
exception list changes what a rule requires), so it banks — but it should actually reach the
bank this time.

### `O-1` (observation) — `README.md:20` describes a population that is empty in this repository

The row reads *"What else lives in `ResearchSystem/contract/` (none of it v3 law) | Everything
else under `ResearchSystem/contract/` is either v1/v2 historical-only for v3 (N0 record §3) or
a P0–P14 instrument governed there."* At this subject that directory holds exactly the three v3
files (§3.1) and nothing else, so the row's subject is the empty set and its claim is
vacuously true. It was accurate in the caller before the 2026-08-17 split and travelled
unchanged. No actor is misled — the operative half, *"the live v3 contract texts are exactly
the three rows above"*, is true — so this is `R9`'s no-nameable-decision case and rides the
next batch touching `README.md`'s table.

### `O-2` (observation) — `ORCHESTRATION.md`'s table restates rule content while claiming not to

`:36` says *"This table assigns them. It does not restate them — read the rule"*, and `:15`
says *"Where a line below cites a rule, **that rule is the text**."* Two rows carry the cited
rule's operative content rather than a label: `:43` reproduces `E9`'s budget triple (*"one
FULL, at most one user-approved fix, one targeted VERIFY"*), and `:44` reproduces `E9`'s
review-window sentence nearly verbatim (*"from dispatch until the record's commit lands, the
branch takes no commit but that record"*). If `E9`'s numbers or window ever change, those two
rows are a second place that must change — the transcription drift surface (`HD-5`) the file's
own thin-by-construction rationale invokes. This is the mirror image of banked rider
`charter-qualifiers`, which records three rows carrying *less* than the rule they cite; same
file, same table, same fix window, so it belongs to that rider's batch rather than a new row.

### `O-3` (observation) — the review side's rules are ordered `R1 R2 R3 R9 R10 R4 R5 R6 R7 R8`

`R9` and `R10` sit between `R3` and `R4` (`CONSTRUCTION-CHECKLIST.md:182`, `:188`, `:217`).
The placement is defensible — both elaborate the finding routing `R3` introduces — and the
content is all present, so nothing acts wrongly on it. Recorded only because a reader
scanning for `R4`–`R8` in a 231-line file will look below `R10` and find them above it, and
because a reader who stops at `R3` (as a numeric scan invites) misses the two rules that
decide where their findings go. Rides the next batch touching the review side.

## 5. Coverage disclosure (`R4`)

- **Read in full at the subject blobs:** all ten members (1 411 lines total, blob ids in §2);
  `HARNESS-DECISIONS.md` header (blob `e1e0866`, lines 1–27) and `§live` (lines 28–195);
  `HARNESS-RIDERS.md` (blob `2c7369f`) — all **36** rider ids enumerated, the ten rows most
  relevant to what I checked read in full, the remainder scanned by id and `redeem-when`;
  `layer_path_check.py` (105 lines); the round's journal `xrepo-refs-2026-08-20.md` §1–§3;
  the full member diff `69fc082..4410899` and the subject's commit body.
- **Read in part:** `dispatch.py` (the three dispatch families, `CONSTRUCTION_ROLE_INSTRUCTION`
  and `READ_PROMPT`); `cli.py` (the `dispatch` command's routing and the operations docstring);
  `test_precommit_checks.py` (the `EXPECTED` block and its two assertions);
  `instruction.py` (`paragraph_skeleton` only); `make_paragraph_map.py` (the first 60 lines);
  `candidate-record.schema.json` (`control_root` only); `v3-checkpoint-read-136f27f.md`
  (`O-3` and its coverage section only); root `README.md` in full but as a **non-member**, only
  to discharge the checklist header's pointer.
- **Probed only, not established:**
  - The **battery** was not run. `EXECUTION.md`'s figures are explicitly pinned to revisions
    (`0d73a5f` / `6fd0ae3`, `a8af54c`, `ddd773a`) and the text itself says to re-run rather
    than trust them, so there is no standing claim here to falsify; the subject's commit body
    reports `733 passed in 96.62s`, which I did **not** reproduce. `UNVERIFIABLE`.
  - Every **date** any member asserts (paragraph-map joining the pack 2026-07-31, the
    2026-08-03 re-baseline, the 2026-07-24 and 2026-07-30 signatures). This repository's
    history begins at the extraction, so no date before it can be checked here at all. The
    signature *records* they point at exist (`W2-record.md`, `supersession-2-signature.md`);
    that the dates in them are right is `UNVERIFIABLE` from this repository.
  - Whether members 6–9 and the two supersessions' bytes are byte-identical to the caller's —
    the extraction claim in the root README. Not checkable from here. `UNVERIFIABLE`.
  - **Process claims** are marked, not verified (`R4`): that this read ran in a fresh context,
    and that its question was set by the orchestrator rather than the executor (`R1`), are
    declared identities, not proof. What I can state is structural: the dispatch reached me as
    `dtw dispatch --read` output naming only a SHA and a charter path, it enumerated no member
    and reported no figure, and every number above was re-derived from the repository (`R2`).
- **Guard exercise (`R8`):** `layer_path_check.unresolved_tokens` was exercised on real bytes
  with a positive and a negative control (§3.3). That establishes the guard's first branch fires
  on this defect's real shape and stays silent on a resolvable token. It does **not** establish
  that the guard's force is sufficient — `L-2` is precisely a case where it is not.
- **Authorization ceiling (`R7`):** `HD-50` authorises batch `DTW-INDEPENDENCE` and records
  `XREPO-REFS` as its R2, received 2026-08-20 with three legs run. That is what the repository
  shows; the preview-card approval behind it lives in conversation and I state the ceiling
  rather than treating its absence as a defect.
