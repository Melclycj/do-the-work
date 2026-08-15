# FULL review — `8e9b60b..8ec4c60` (the 2026-07-29 reform round: three tracked guards + a third
dispatch family + record homes + six instruction-layer amendments)

**Verdict: `CHANGES_REQUIRED` — 3 blockers, 3 non-blocking findings, 5 observations.**

The guards work on the class they were built for: `layer_path_check` flags the real
`dcced4e` defect and passes the `d322816` repair, and 5 of the 7 mutations I ran went red.
The two that went green are the same defect twice — a guard's *target path* taken from the
guard's own constant, which `E5` names. The third blocker is not in the code: the round
deletes the artifact its own opening cold read's must-fix is about, on a stated ground that
the cold read's record contradicts.

---

## 1. Subject, re-derived

```
$ git rev-parse HEAD
8ec4c60b16caf1864e4262567a7b22995c232029          # tip == the handed range's tip
$ git log --oneline 8e9b60b..8ec4c60
8ec4c60 V3-REFORM-A-INSTRUCTION-AMENDMENTS-v1
717e547 V3-REFORM-B-GUARDS-GENERATOR-RECORD-HOMES-v1
$ git status --porcelain
?? ResearchSystem/docs/                            # untracked, predates this work, not in the subject
$ cat .harness/review-pending.json
{"kind":"construction-round",
 "subject":"8e9b60b9…..8ec4c60b…","dispatched_at":"2026-07-29T13:28:25+00:00"}
```

The marker's subject is byte-identical to the range I was handed, and its timestamp is after
both candidate commits — so the round's own new `E9` clause ("from dispatch to that commit the
branch takes no commit but the record itself") is satisfied so far: `HEAD` is still `8ec4c60`.

**Change set, classified by hand** — `git diff --name-status`, 15 paths, 8 A / 6 M / 1 D, all
under `ResearchSystem/`:

| kind | paths |
|---|---|
| guards (A) | `tooling/hooks/{__init__,review_freeze_check,ledger_cap_check,layer_path_check}.py` |
| generator (M) | `tooling/rsc.py`, `tooling/rsclib/document_harness/dispatch.py` |
| tests (A/M) | `tooling/tests/document_harness/test_precommit_checks.py` (A), `tooling/tests/document_harness_review/test_dispatch.py` (M), `tooling/tests/fixtures/expected-read-prompt.txt` (A) |
| record homes (A/M/D) | `HARNESS-RIDERS.md` (A), `migration/…/journal/reform-2026-07-29.md` (A), `HARNESS-LEDGER.md` (M), `migration/…/v3-dispatch-instruction-layer-cold-read.md` (**D**) |
| instruction layer (M) | `document-harness/CONSTRUCTION-CHECKLIST.md`, `document-harness/README.md` |

**Round, budget, authorization.** The ledger at `8e9b60b` names the reform 轮 as NEXT with the
sequence B → A → FULL → (fix+VERIFY) → amendment read → Phase C2. No `v3-review-full-*` record
keyed to this range exists, so this is the round's single `E9` FULL and no fix has been
consumed. The round's opening cold read is discharged (`v3-cold-read-451e8b0.md`, record
committed at `8e9b60b`, no commit between dispatch and record). The `E11` preview card and the
user's approval of the round are chat-only and therefore **`UNVERIFIABLE` from the repository**
(`R7`: stated as a ceiling, not a block).

---

## 2. Implementation first (`R3`) — what I ran, not what was reported

**Suites, re-run by me, not accepted from the commit body:**

```
Ran 164 tests in 23.018s  OK      (tooling/tests/document_harness)
Ran 329 tests in 51.704s  OK      (tooling/tests/document_harness_review)
```

**The three guard modules' sha256 match the journal's reported prefixes** (`2ef34839b6e4fdf6`
/ `aa4bc454b7e20cf9` / `e11d4cd5ebbc3c9b`), so the E4 evidence is at least keyed to the shipped
bytes.

**The wiring exists.** `D:/Thesis/.git/hooks/pre-commit` (untracked, shared via the common git
dir; read in full) carries the existence-guarded loop over all three scripts. It is per-machine
and outside the subject — see F-2.

**`layer_path_check` catches the defect class it claims (`E7`).** Run against the historical
blobs rather than a synthetic case:

```
dcced4e (122 lines) -> [('schema/document-assurance-v3/', 'resolves only under ResearchSystem/ — prefix missing')]
d322816 (122 lines) -> clean
```

That is the exact `dcced4e`-banked / `d322816`-paid defect, flagged before the repair and
silent after it. This is the strongest thing in the round.

**Mutation matrix (`R8` — real defect shapes, not `return 1 → return 0`).** Each mutation
applied to the shipped module, `test_precommit_checks` run, module restored from a
sha256-checked scratchpad copy, sha re-verified (`restored sha match=True` on all seven; the
worktree is byte-identical to `8ec4c60` now):

| # | mutation (the real defect it reproduces) | result |
|---|---|---|
| M1 | freeze: record-family regex → `^.*\.md$` (family boundary stops binding) | **RED** |
| M2 | freeze: marker filename drifts from what the CLI writes | **RED** (3 failures) |
| M3 | ledger: `LEDGER` path typo'd — guard can never fire in the real repo | **GREEN** |
| M4 | ledger: `MAX_LINES` 120 → 10000 (bound stops binding) | **RED** |
| M5 | layer: `README.md` dropped from `LAYER` — member stops being scanned | **GREEN** |
| M6 | layer: the missing-prefix class stops being flagged | **RED** |
| M7 | layer: the broken-`ResearchSystem/`-prefix class stops being flagged | **RED** |

Two further mutations on the read prompt (`dispatch.py`, restored the same way): one word
changed in `READ_PROMPT`, and a member list injected into it — **both RED**. The golden fixture
is a committed artifact and binds, which is `E5` done right; B2 is about the two places it was
not.

**`layer_path_check` over the live layer, all eight members** — a measurement the round does
not contain, and the basis of B1:

```
CONSTRUCTION-CHECKLIST.md            clean
README.md                            clean
EXECUTION.md                         clean
REVIEW.md                            clean
v3-harness-operating-contract.md     clean
v3-harness-review-contract.md        `tooling/tests/fixtures/expected-construction-prompt.txt`  -> prefix missing
supersession-1.md                    `schema/document-assurance-v3/review.v2.schema.json`       -> prefix missing
supersession-2.md                    `assurance/runs/`, `schema/`                               -> prefix missing
```

**Instruction text checked against the repository, not against itself:**

| claim | re-derived |
|---|---|
| `layer_path_check.LAYER` "mirrors E10's membership sentence" | 8 entries; all 8 resolve; set equals the amended sentence's enumeration ✓ |
| ledger cap 120 vs the ledger | `wc -l HARNESS-LEDGER.md` → 64 ✓ |
| commit A: "the repair-batch ruling block deletes as landed" | 9 deleted ledger rulings walked one by one: `E9`/`E3`/`E10`-digest land in the amended rules ✓; rationale-ban already carried by the file header ✓; ledger cap lands as guard + header line ✓; journal/RIDERS land as files ✓; the reality-as-verdict-basis ruling does **not** land and is correctly banked as `VB-1` ✓ |
| rider bank redemption discipline | `L-1` `S2-1` (supersession-2 untouched), `O-4r` `E2-t` (`E12`/`E2` untouched), `L-2` (user undecided) all correctly un-redeemed ✓ — see O-4 for the one borderline |
| `R6` record naming for a range subject | precedent is the tip short sha (`v3-review-full-11ce5b4.md` for `f4533691..11ce5b41`); this record follows it ✓ |

---

## 3. Blockers

### B1 — `layer_path_check` blocks three of the eight layer members on content it did not change, and the collision is already scheduled

**Location:** `ResearchSystem/tooling/hooks/layer_path_check.py:61-90` (`check` scans the whole
staged file, not the staged diff). **Ground truth it violates:** the repository's own layer
members, enumerated in the same module's `LAYER`, plus `HARNESS-RIDERS.md` rows `S2-1` and
`L-1`, both of which schedule a batch that touches `supersession-2`.

The guard fires on any missing-prefix token anywhere in a staged layer file. Three members
carry such tokens today (table in §2). The consequence is not hypothetical: `S2-1` and `L-1`
are banked *against supersession-2*, so the next batch that redeems either one stages a file
the new guard rejects for two tokens (`` `assurance/runs/` ``, `` `schema/` ``) that batch did
not write. The escapes are to edit superseding contract prose unrelated to the change, or
`--no-verify` — which is the guard being routed around on its first real encounter. On
`supersession-1` the same shape collides with `E2`: "fix the path as written" is an edit to
frozen bytes, and only `E2`'s own prohibition on staging it keeps that unreachable.

The round asserts the opposite in the journal (`journal/reform-2026-07-29.md:47-48`): *"Tokens
resolvable nowhere are skipped as possibly illustrative — the supersession-2 prose mention of a
`templates/run-v2/`-shaped path stays legal."* True of that one token; false of the file. The
command that falsifies it is the guard itself run over the layer, which is the round's own new
`E3` clause applied to its own journal.

**Minimum fix.** Scope the scan to lines the staged diff *adds* — the defect class is a path
newly written, which is what both `dcced4e` and `d322816` were — or, if whole-file scope is
wanted, record the three pre-existing hits in the module and state that touching those files
requires the prefix repair first. Either way the measurement in §2 belongs in the journal.

### B2 — two of the three guards take the path they guard from their own constant, so a drift in that constant leaves all 13 tests green and the guard silently dead

**Location:** `ResearchSystem/tooling/tests/document_harness/test_precommit_checks.py:20`
(`CHECKLIST = layer_path_check.LAYER[0]`) and `:75` (`LEDGER = ledger_cap_check.LEDGER`).
**Ground truth it violates:** `E5` — *"A guard's expectation must be independent of the thing it
guards — a hand-written literal or a committed fixture, never the module's own constant, list,
or template."*

Demonstrated, not argued: M3 typo'd `LEDGER` to `HARNESS-LEDGR.md` — the guard can then never
fire on the real ledger — and the suite stayed **OK**. M5 dropped `README.md` from `LAYER` — the
member stops being scanned — and the suite stayed **OK**. The contrast is instructive: the two
expectations that *are* hand-written literals (the 120/121 line counts, and
`.harness/review-pending.json` written out by hand in `write_marker`) both bind, M4 and M2 red.
So the discipline was applied to the numbers and dropped on the paths.

This matters more than a generic test-quality note because `LAYER` is the module's declared
mirror of `E10`'s membership sentence: the only thing standing between it and silent drift is
the docstring's "drift here is caught by the next layer read", and a layer read reads the
*instruction layer*, not this module.

**Minimum fix.** Hand-write both paths in the test file, and add one case that stages every
entry of `LAYER` (parameterised over the tuple is fine — the *expectation* is then "all eight
are scanned", which is independent of any one of them being right).

### B3 — the round deletes the artifact its own opening cold read's must-fix is about, on a stated ground the cold read's record contradicts

**Location:** commit `717e547` body (*"The never-consumed hand-written dispatch note is
deleted; the two consumed ones stay as history"*) and
`journal/reform-2026-07-29.md:49-52` (*"never consumed (the read was re-dispatched by
phrase)"*), deleting
`migration/document-work-assurance-v3/v3-dispatch-instruction-layer-cold-read.md`.
**Ground truth it violates:** `v3-cold-read-451e8b0.md`, the committed record of the read in
question, read in full.

The note (39 lines, read in full at `451e8b0`) was consumed, and the record says so four ways:

- §1 line 16 runs `git log --format=%h -1 -- .../v3-dispatch-instruction-layer-cold-read.md`
  → `451e8b0` — that command *is* the note's own closing instruction for deriving the record's
  filename, which the reader could not have known otherwise;
- the record's filename and its commit title `V3-REVIEW-RECORD-INSTRUCTION-LAYER-COLD-READ-451e8b0-v1`
  are exactly the two the note prescribes;
- §1 quotes the note's disclaimer and tabulates its seven blobs against the reader's own eight;
- §6 O-5 opens *"The note handed me seven blob ids plus three facts"*, and §7 lists "the
  dispatch note" among what was read.

M-1 — the round's whole reason for amending `E10`'s membership sentence — is a finding **about
that note's member table**. So the rule the round applied ("consumed → keep as history;
never-consumed → delete") was applied backwards on the one instance where the note carried a
live finding, and the two notes kept as history are the ones no open finding points at.

This is `E3`'s class — a characterization no command established, contradicted by a committed
record — and it is the third consecutive round in which the action is defensible and the stated
reason is factually wrong, which is the ledger's open user question ①. Whether that pattern is
acceptable is the user's to answer (`R5`); that this instance is an instance is mine.

**Minimum fix — text, not machinery (`E6`).** The journal sentence changes to state what the
record shows: the note was the `451e8b0` cold read's dispatch document, its member table is
M-1's subject, and the deletion is justified as *superseded by the generator's `--read` mode*,
not as unconsumed. Restoring the 39 bytes-worth of file is a separate call and the user's
(`R5`); correcting the record is not optional.

---

## 4. Non-blocking findings (`R3` — named, not inflated)

### F-1 — `E10`'s inserted clause detaches the "no round has relied on it" qualifier from the sentence it qualified, and overlaps the free path it restricts

`CONSTRUCTION-CHECKLIST.md:75-82`. Before: *"…that pair is not a round and spends no budget,
for as long as no round has relied on the text — relied means … — once one has, changing it
opens a round"*. After, a new clause sits between them, so the qualifier now trails *"an
amendment adding a clause to any rule is design and opens a round"* and the free-pair sentence
reads unconditioned.

Two readings survive. Under the intended one (commit body: "the free-path restriction") the
new clause carves clause-additions out of the free path and the trailing "once one has,
changing it opens a round" still catches relied-on text, so no permission actually widens —
which is why this is not a blocker. The residue is the overlap: this round's own M-1 fix was
*a literal replacement the finding named* (free path admits it) that *tightens a rule by adding
a bound* (new clause sends it to a round). The round took the conservative branch and opened;
the text does not compel that, and the next reader facing the same shape has no rule to point
at. **Named downstream decision:** whether a read's must-fix whose named minimum fix narrows a
rule spends a round. **Minimum fix if it rides a batch:** move the new clause after
*"…once one has, changing it opens a round;"* and say which of the two wins when both apply.
`HARNESS-RIDERS.md` row `E10-d` is the same seam one clause earlier.

### F-2 — README now asserts the hook wiring, and no command output backs it in either place the round's own new `E3` clause names

`README.md:30` gains *"Since 2026-07-29 it also calls three tracked checks, existence-guarded,
from `ResearchSystem/tooling/hooks/`"*. The subject is an **untracked per-machine file** outside
the commit; neither commit body nor journal carries the output of the command that would
falsify it. The same commit adds the `E3` clause requiring exactly that. I verified it true
here by reading `D:/Thesis/.git/hooks/pre-commit`, which does carry the loop — so the assertion
is accurate and the defect is evidentiary. The README row's own "per-machine; NOT a harness
guarantee" hedge covers the reach of the claim but not its backing. **Minimum fix:** the hook's
relevant lines pasted into the round journal.

### F-3 — no test reaches the CLI, so the marker's writer and its reader are bound only by a manual smoke

The new marker write lives in `rsc.py::_cmd_v3_dispatch` (`if derived.report.ok: …
marker.write_text(...)`), and the new `--read` mode is argparse wiring in the same function.
`grep` over the whole test tree returns `.harness/review-pending.json` only inside
`test_precommit_checks.py`'s own hand-written `write_marker`, and nothing named
`_cmd_v3_dispatch` or `--read`. So M2 proves the *consumer* binds to the filename; nothing
proves the *producer* writes that filename, or that `--read` is reachable through the CLI at
all — the unit tests call `read_dispatch_of` / `render_read_dispatch` directly. In practice
both hold: the live `.harness/review-pending.json` that dispatched this review was written by
the real CLI and carries exactly the `kind` / `subject` keys the guard reads, which I checked.
**Minimum fix if it rides a batch:** one CLI-level test asserting the file the command writes.

---

## 5. Observations (`R5` — reported; the conclusion is the user's)

- **O-1 — `E9`'s clause is universal; its mechanical carrier is not.** The freeze marker is
  written only by `rsc v3 dispatch`. The `451e8b0` cold read was, by the journal's own account,
  "re-dispatched by phrase" — a dispatch that opens no window. The rule binds every dispatched
  FULL, VERIFY or read; the guard binds only generated ones.
- **O-2 — the freeze guard does not check *which* record.** The marker carries `subject`, and
  `review_freeze_check` prints it but admits any path matching the record-family regex. A
  record for a different subject lands clean. Whether that is worth closing is a design call.
- **O-3 — the guard reads staged text against the worktree filesystem.** `layer_path_check`
  resolves tokens with `(repo_root / token).exists()` while reading bytes from `git show :path`.
  A staged deletion whose file is still on disk (`git rm --cached`) resolves; the committed tree
  would not have it. Narrow, and the opposite direction of B1.
- **O-4 — one borderline rider non-redemption.** `E10-d`'s redeem-when is "the next batch
  touching `E10`'s deferral clause". This batch edits `E10` in three places but leaves the
  deferral clause's own bytes untouched, so the row stayed. Defensible on the letter; F-1 is the
  same seam, now sharper.
- **O-5 — the shape `R5` asks me to report rather than conclude.** This round closes findings by
  adding three guards, a third dispatch family, two new record homes and six rule clauses; the
  round before it closed findings by amending rules; the cold read that opened it found the
  member set of the layer those rules govern was itself wrong. Components accumulate faster than
  the rounds that retire them. The question, and the conclusion, are the user's.

---

## 6. Disclosure (`R4`)

**Read in full.** `CONSTRUCTION-CHECKLIST.md` (131 lines, worktree at `8ec4c60`);
`v3-harness-review-contract.md` (5); `document-harness/README.md` (34); `HARNESS-LEDGER.md`
(64); `HARNESS-RIDERS.md` (31); `journal/reform-2026-07-29.md` (52);
`v3-cold-read-451e8b0.md` (264); the deleted dispatch note at `451e8b0` (39, via `git show`);
`tooling/hooks/{__init__,review_freeze_check,ledger_cap_check,layer_path_check}.py`;
`tooling/tests/document_harness/test_precommit_checks.py` (125);
`tooling/rsclib/document_harness/dispatch.py` (685);
`tooling/tests/fixtures/expected-read-prompt.txt`; `D:/Thesis/.git/hooks/pre-commit` (53,
untracked); both commit bodies; the full diff of all 15 changed paths.

**Sampled.** `rsc.py` and `tests/document_harness_review/test_dispatch.py` through their diffs
in this range plus targeted `grep`, not end to end. Prior records
(`v3-review-full-{11ce5b4,af2905c,0439efe}.md`) by heading only, for the `R6` naming precedent.
`supersession-1` / `supersession-2` / `EXECUTION.md` / `REVIEW.md` **not read** this session —
unchanged in the range; my statements about the first two are the guard's output over their
bytes, not a reading of their content.

**Probed only.** `grep -rn` for surviving references to the deleted dispatch note (two hits,
both listed in B3); `git rev-list --count origin/main..HEAD` → 271, unchanged by this round.

**Not verified.** The `E11` preview card and the user's approval of this round (chat-only —
`R7` ceiling stated, not a block). Whether the hook wiring exists on any machine but this one;
it cannot, being untracked. `validate_fixtures.py` was not re-run — README's "41/41 green" is
unchanged in this range and was re-derived by the `451e8b0` read.

**Marked, not verified (`R4`).** That this session is fresh context. It opened on the range and
has read only what this section lists, but that is a process claim with no evidence lock; `R1`
is answered by who set the question, which is why §1 re-derives the round, budget and
authorization rather than adopting the prompt's framing — the prompt handed me a range and
nothing else, which is `E12`'s shape.

**Mutation caveat (`R4`).** The nine mutations prove the tests have binding force on the shapes
I chose. They do not prove that force is sufficient, and B1 is precisely a defect no mutation
would have found — it needed the guard run over real inputs the suite never gives it.

**`UNVERIFIABLE`.** Whether the "consumed / never-consumed" distinction in B3 was meant in some
narrower sense than the record demonstrates — the repository records no definition of
*consumed*, and I ruled on what the cold read did with the note, not on what the word was
intended to mean.
