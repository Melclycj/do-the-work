# Instruction-layer read — `d01615ba4ff25e3b8f61bfeb19e83f58144b7ac4`

`E10` read of the instruction layer at the branch tip after Phase D's byte-channel
application. Not a round: no verdict, no budget consumed (`R3`). Findings tiered
must-fix / low / observation. One dispatch discharges five recorded obligations, each
verified below rather than taken from the dispatch: C4's deferred README enumeration
row (`d50d9e5`), C4's deferred schema `description` strings (same commit's binding
sentence), Phase D's E1 design-amendment read (`34cf85b` ruling ③), the W-1 wording
fix riding that batch (`34cf85b`, scheduled by the C4 FULL), and the make-good for
Phase D's user-waived opening cold read (`34cf85b` ruling ①: "the round's closing
layer read covers those deferred bytes, the new E1 sentence, and the W-1 fix in one
dispatch").

**Findings: 0 must-fix, 1 low (bytes supplied — the (a) channel can take it), 4
observations.** Every factual assertion in the changed bytes was re-derived by command
and holds: the amended digest-derivation wording matches `paragraph_skeleton`'s
implementation, the README row's generated-by / enforced-by claims match the committed
files, and the E1 sentence contradicts nothing in the layer. The banked residues
`L-2li` and `L-1lr` are verified in place and not re-raised.

## 1. Subject, re-derived

`R2`: I was handed one SHA and the phrase *the instruction layer*. Everything below is
re-derived from the repository; no figure in the dispatch prompt, the ledger, or any
prior record is accepted as reported.

```
$ git rev-parse HEAD       -> d01615ba4ff25e3b8f61bfeb19e83f58144b7ac4
$ git status --porcelain   -> (empty)
```

`E10`'s sentence at the subject commit (checklist blob `1ced10a1`, read in full)
governs the member set: **eight enumerated members plus, for the first time, a
non-empty open tail** — `git diff --name-only 784e49b d01615b -- ResearchSystem/schema/`
returns exactly one path, `paragraph-map.schema.json`, whose root `description` was
amended at `34cf85b`, and schema `description` strings when amended are layer text by
the sentence's own words. The other prose added since the last layer read
(`v3-checkpoint-read-784e49b.md`, two FULL records, two round journals, one decision
JSON, one generator script, plan/ledger/rider edits, and the run-v2 template README's
new gate section) are records, data, code, plans, and product-run template
documentation by their own headers — none supersedes text this harness governs.

| # | blob at `d01615b` | lines | member | vs. last recorded read |
|---|---|---|---|---|
| 1 | `1ced10a1` | 158 | `document-harness/CONSTRUCTION-CHECKLIST.md` | **changed** (`dff584d9` → at `34cf85b`) |
| 2 | `f3a31208` | 37 | `document-harness/README.md` | **changed** (`bb84e6f2` → at `d50d9e5`) |
| 3 | `bd490c8b` | 153 | `document-harness/EXECUTION.md` | same since `d58969d` read |
| 4 | `d050b05a` | 227 | `document-harness/REVIEW.md` | same since `784e49b` read |
| 5 | `17ff31bb` | 5 | `migration/…/v3-harness-operating-contract.md` (stub) | same since `784e49b` read |
| 6 | `52a97a48` | 5 | `migration/…/v3-harness-review-contract.md` (stub) | same since `784e49b` read |
| 7 | `68031fa2` | 124 | `contract/…-v3-supersession-1.md` | same since `d58969d` read |
| 8 | `e1a2f26b` | 113 | `contract/…-v3-supersession-2.md` | same since `403fc9a` read |
| + | `c2b713b` (file) | 44 | `schema/document-assurance-v3/paragraph-map.schema.json` — open tail, `description` strings | **new** — born `6f09935` at `d50d9e5`, amended at `34cf85b`; never before read |

Blob ids from `git ls-tree d01615b <dir>`; line counts from `git cat-file -p
d01615b:<path> | wc -l`. Two enumerated members changed since `784e49b`, each in
exactly one commit (`git log 784e49b..d01615b -- <member>` per member): member 1 only
at `34cf85b` (V3-PHASE-D-HISTORICAL-EXIT-v1, the E1 sentence), member 2 only at
`d50d9e5` (V3-PHASE-C4-M11-v1, the enumeration row). No other commit in the ten-commit
range touches a member, and `git diff 34cf85b d01615b` over the layer, schema and
contract paths is empty — the Phase D FULL record commit (`766fe02`) and the L-2
application (`d01615b`: journal + `issues.py` + one test file) touched no layer byte,
exactly as `d01615b`'s body claims.

**Dispatch, checked rather than assumed.** `.harness/review-pending.json` is live and
reads `{"kind": "layer-read", "subject": "d01615ba4ff25e3b8f61bfeb19e83f58144b7ac4",
"dispatched_at": "2026-07-31T15:46:05+00:00"}` — the subject I was handed, which is
the branch tip. The branch has taken no commit since the subject; `E9`'s window is
intact and this record is the only commit it admits.

## 2. Coverage — `E10` citation clause, per-member

Six members are blob-unchanged since a recorded end-to-end read of each. I verified
every citation against git rather than against the records' tables:

- Members 4, 5, 6 — read in full by `v3-checkpoint-read-784e49b.md` (§1 rows
  `d050b05a` / `17ff31bb` / `52a97a48`; §7 lists all three under *Read in full*).
  `git rev-parse 784e49b:<path>` equals the `d01615b` blob for each.
- Members 3, 7 — read in full by `v3-checkpoint-read-d58969d.md` (§1 rows `bd490c8b`,
  `68031fa2`; closing disclosure *"Read in full: all eight layer members at the blobs
  tabulated in §1"*). `git rev-parse d58969d:<path>` equals the `d01615b` blob for each.
- Member 8 — read in full by `v3-checkpoint-read-403fc9a.md` (§1 row `e1a2f26b`, 113
  lines, listed as changed-therefore-read; disclosure *"Read in full: README.md (36)
  and supersession-2.md (113)"*). `git rev-parse 403fc9a:<path>` equals the `d01615b`
  blob.

Coverage discharged by citation for six; members 1 and 2 and the open-tail schema read
in full here at the subject blobs (member 1 additionally as this session's standing
instructions). Staleness the byte-key cannot see: the six unchanged members were
grepped for the deltas' vocabulary (`one role`, `session`, `paragraph`, `M11`,
`classification`, `memory`) — the only hits are E3's pre-existing "never describe it
from memory" and REVIEW/EXECUTION's product-run role text, none of which restates or
contradicts the amended content.

## 3. What the deltas do, against the fixes and rulings they claim to apply

**`34cf85b` → member 1 (E1 sentence).** Three lines added to `E1`: *"One session holds
one role for its whole life: work out at the start which role this session holds, and
a request that belongs to the other role is flagged for the user to route, never
absorbed."* Read against the whole checklist: consistent with `E1`'s first sentence
(no self-review), with `R1` (independence decided by who sets the question), and with
`E6`'s "Both sides:" marker (a rule addressed to both roles, which is not a session
holding both). No verdict path, check outcome, or budget rule changes; it codifies the
role habit the two deleted memory atoms carried, and no pointer to those atoms remains
anywhere in the layer (grepped). Correctly declared design in the commit body ("a
design amendment relied on by no round yet"), correctly run inside a carded round
(Phase D, FULL at `766fe02`), its independent read correctly owed to — and now
discharged by — this read, not banked as that FULL. Between `34cf85b` and this
dispatch the branch took two commits (`766fe02` records, `d01615b` relies on `E10`'s
channel + the (a) ruling + precedent, not on the E1 sentence): nothing relied on the
amendment before its read.

**`d50d9e5` → member 2 (README enumeration row).** One table row: *"Paragraph-map
schema (Phase C4 — M11) | paragraph-map — run-local instruction enumeration with the
one human-filled classification column; generated by the run-v2 template's
`make_paragraph_map.py`, enforced by its authoring gate."* Every claim in the row
re-derived: the link target resolves (`ResearchSystem/schema/document-assurance-v3/
paragraph-map.schema.json` exists at the subject tree); the schema requires
`classification` per entry as its only human column (read in full, §below);
`make_paragraph_map.py` exists at `ResearchSystem/assurance/templates/run-v2/`;
`check_template_instance.py` carries `paragraph_map_issues` (3 sites). The commit body
recorded both deferral facts — no new clause to any rule, nil effect on rounds in
flight — and both held on inspection then (the C4 FULL confirmed) and now: the row is
an enumeration entry; C4 and Phase D closed/proceeded identically with or without it.
Deferral, never exemption — discharged here.

**`d50d9e5` + `34cf85b` → open tail (schema `description` strings).** The schema read
in full at `c2b713b` (44 lines, six `description` strings). The root description's
digest-derivation wording — amended at `34cf85b` as the W-1 ride — now reads *"SHA-256
over each block's lines joined with `"\n"` and UTF-8 encoded — line endings
normalized, no trailing newline"*. Verified against the implementation it describes,
not against the C4 FULL's finding: `instruction.py` `paragraph_skeleton` does
`instruction_text.splitlines()` (line-ending normalization) → `"\n".join(...)` (no
trailing newline) → `block.encode("utf-8")` → `bytes_digest` = plain
`hashlib.sha256(raw).hexdigest()`. The amended wording is the accurate fact the C4
FULL's W-1 named (`v3-review-full-d50d9e5.md` §6), applied as exactly the R9 ride it
scheduled — one string replaced, nothing else in the schema diff at `34cf85b`. The
remaining five descriptions state: `const "1"` from birth (holds — `"const": "1"`),
instruction_ref equality enforced by the gate (holds — Leg 1 per the gate, C4 FULL
§2), per-entry classification refused-never-defaulted (holds — `required` +
`additionalProperties: false`), parallel result array unrepresentable (holds — root
`additionalProperties: false`), and the E2 boundary sentence ("joined the pack after
2026-07-29, so it is not part of the E2-frozen surface" — holds, §4).

## 4. Assertions re-derived by command

| assertion in / about the changed bytes | command | result |
|---|---|---|
| `E2`: four frozen blobs at subject | `git rev-parse d01615b:<path>` ×3 + `hash-object` of the `.goals` plan | holds — `8ad404b1…` / `b2dbdf75…` / `68031fa2…` / `e1a2f26b…` |
| `E2`: pack joined 2026-07-29 with fourteen files; later additions not frozen | `ls-tree -r 11d147e` → 14; `ls-tree -r d01615b` → 15; `diff 11d147e d01615b -- <pack>` → exactly `paragraph-map.schema.json` | holds — the fourteen byte-identical, the 15th is the un-frozen addition |
| schema root description: digest derivation | `instruction.py:79,88,94` + `bytes_digest` body | holds (§3) |
| README row: generated-by / enforced-by / link | `ls` + `grep -c paragraph_map_issues` → 3 + target exists | holds |
| README row 31: fixtures 41/41 green | `python …/N0/fixtures/validate_fixtures.py` | holds (this machine) — `41/41 cases behaved as declared; failures=0` |
| README "Construction-side rules" row: E1–E12, R1–R10 | checklist read in full | holds — twelve E rules, ten R rules |
| `d01615b` body: "no layer member, schema, contract or oracle in this diff" | `git show d01615b --stat` + path classification by hand | holds — journal + `issues.py` + one test file |
| `34cf85b` ruling ①'s waiver basis: seven blobs equal the `784e49b` table, the eighth differs by one row | member table §1 + `git diff 784e49b d50d9e5 -- README.md` | holds — re-derived independently of the Phase D FULL's same check |
| `layer_path_check.LAYER` mirrors the membership sentence | script lines 29–39 read | the eight enumerated paths, exactly; the realized open-tail member is not mirrored — **L-1 below** |

No assertion in the layer was found false at this commit.

## 5. Ledger bindings, checked

- *C4's deferred bytes owe the next layer read* (`d50d9e5` body; C4 FULL §5 E10) —
  discharged: member 2 and the schema's six description strings read in full at the
  final bytes (§3).
- *Phase D's E1 sentence owes its independent read to the closing layer read*
  (`34cf85b` ruling ③) — discharged (§3); the deferral was clean (nothing relied, §3).
- *The W-1 ride* (C4 FULL W-1: wording fix rides the next batch touching this layer)
  — redeemed at `34cf85b`, the next such batch; verified here against the
  implementation, which is the read the applied bytes owed. The ledger's C4-closeout
  line ("ride 已被 E10 延后债排定") described the scheduling and is now history, not a
  live pointer — nothing stale to act on.
- *The waived opening cold read* (`34cf85b` ruling ①) — made good: all eight members
  are now either read in full at the final bytes or covered by verified citation; the
  waiver's factual basis re-derived (§4). The waiver itself is the user's (`R7`:
  visible as the commit/journal record; the chat is the ceiling).
- Round budget state as this read finds it: Phase D FULL spent (`766fe02`,
  `REVIEWED_NO_BLOCKER`); fix leg unspent — L-2 was applied at `d01615b` through the
  byte channel under the 2026-08-01 ruling recorded in its body, obliging no VERIFY;
  L-1 was wording-level (R9). This read spends nothing (`R3`).
- Riders: the bank at `d01615b` holds seven rows (F-4, F-c, O-2b, SCC, RA, L-2li,
  L-1lr) — CT, F-d, F-3r deleted at `34cf85b` with their fixes, as the Phase D FULL
  verified. None is due on this read (a read touches no surface). `L-2li` verified in
  place: `E10`'s deferral precondition still reads "adds no new clause to any rule" —
  unchanged, still banked. `L-1lr` verified in place and exercised again — O-2 below.

## 6. Findings

### Low (bytes supplied — routes by the 2026-07-30 (a) ruling, not the bank)

**L-1 — the pre-commit layer-path mirror no longer covers the whole layer.**
`layer_path_check.py`'s `LAYER` tuple (lines 30–39) carries the eight enumerated
members and its comment claims it "Mirrors E10's membership sentence"; since `34cf85b`
amended the paragraph-map schema's root `description`, the membership sentence's open
tail is non-empty and the mirror is a proper subset. Downstream decision that goes
wrong: a future edit writing a broken repository path into that schema's `description`
strings — now layer text — lands without the advisory backstop firing, the exact
`dcced4e`/`d322816` defect class the hook exists to catch. Not wording-level (the fix
changes a check outcome — `R9` does not take it); not must-fix (the hook is advisory
and per-machine, and the defect is future-conditional). Minimum fix, one line added to
the tuple:

```python
    "ResearchSystem/schema/document-assurance-v3/paragraph-map.schema.json",
```

Mechanically safe: the hook scans only lines a staged diff adds, so no retroactive
noise; a JSON file with no backtick tokens is a no-op for it. Code-side, outside every
frozen surface, reversible. If the user instead reads `LAYER` as deliberately mirroring
only the fixed enumeration, the alternative is a one-line comment scope note — that
choice is theirs; the bytes above are the fix as the mirror claim stands.

### Observations

**O-1 — the open tail is realized for the first time, and membership follows.** Until
`34cf85b`, every layer read enumerated eight members and verified the open tail empty.
The paragraph-map schema's `description` strings are now amended schema descriptions —
layer text by `E10`'s sentence — so future edits to them are layer edits (E10
discipline: read before reliance, or recorded deferral), and future layer reads
enumerate them as a ninth entry until the sentence says otherwise. This read's §1
table does so. The consequence was implicitly accepted when `d50d9e5`'s commit bound
"the new schema's `description` strings" to ride this read; recorded here so the next
reader inherits it as a checked fact rather than a re-derivation.

**O-2 — the `L-1lr` seam was exercised a second time and held.** `d01615b` is a
post-FULL byte application that obliges no VERIFY — exactly the configuration
`L-1lr` records as misreadable from `E9`'s letter alone. Its commit body navigates the
seam by citing the recorded reading (`E10`'s channel, the (a) ruling's named-content
arm, precedent `7463229`, the rider itself), which is the disposition the rider's
premise predicted. The rider's redeem-when (a batch touching `E9`'s budget sentence or
`R10`'s routing sentence) was not touched; it stays banked. Two clean exercises are
evidence the recorded reading carries the practical path, not that the letters stopped
lagging.

**O-3 — one dispatch multiplexed five obligations, and the configuration that made it
sound is worth naming.** This read simultaneously discharged C4's deferred bytes, the
schema descriptions, Phase D's design-amendment read, the W-1 ride's owed read, and
the waived opening cold read — sound only because all five obligations' bytes coincide
at one tip and the read read them at that tip (the final bytes, per the `784e49b`
precedent). Had any deferred byte been superseded again before the read, per-member
reading at the tip would still have covered the final text but the intermediate state
would never have been independently read — acceptable under `E10` as written
(deferral binds bytes, not history), and exactly why the consolidation ruling belongs
to the user each time rather than becoming a default.

**O-4 — the C4 FULL's W-1 phrasing is looser than the rule it applied.** That record
says "fix the wording when that read lands"; the governing rule (`R9`) says the fix
rides the next **batch** touching the layer, and the fix correctly rode `34cf85b` —
before this read. Outcome conforms; noted only so the FULL's phrasing is not later
quoted as if reads were the redemption vehicle. The record is immutable narrative; no
action.

## 7. Coverage disclosure (`R4`)

**Read in full:** members 1 (158, also as standing instructions) and 2 (37) at the
subject blobs; the paragraph-map schema (44) at `c2b713b`; the full diffs of
`d50d9e5`, `34cf85b`, `766fe02`, `d01615b` (`--stat` + member/schema/contract paths)
and the complete commit bodies of `d50d9e5`, `34cf85b`, `d01615b`;
`v3-review-full-d50d9e5.md`; `v3-review-full-34cf85b.md`;
`v3-checkpoint-read-784e49b.md`; `HARNESS-RIDERS.md` and `HARNESS-LEDGER.md` at
`d01615b`; the retired review contract's stub (as standing-instruction entry).

**Sampled:** `v3-checkpoint-read-d58969d.md` and `v3-checkpoint-read-403fc9a.md` —
§1 blob rows, read-in-full disclosures and blob-assertion lines (grep-anchored);
`instruction.py` — `paragraph_skeleton` body (:62–94) and module head;
`__init__.py` — `bytes_digest` body; `layer_path_check.py` — docstring + `LAYER`
(:1–50); `check_template_instance.py` — `paragraph_map_issues` presence by grep;
the run-v2 template README — the range diff only.

**Probed only:** `.harness/review-pending.json`; the fixture runner (executed, output
pasted, internals unread); `make_paragraph_map.py` (existence only); pack ls-tree
counts at `11d147e` and `d01615b`.

**Not verified:** that this read ran in a fresh context — a process claim, marked. The
2026-08-01 card rulings and the L-2 incidental-application ruling beyond their in-repo
records (`R7` — ceiling stated, not a block). The five suites the range's commit
bodies report green — not re-run here (both FULLs re-ran them at their candidates;
this read ran only the fixture runner, per the `784e49b` precedent); their binding
force is those rounds' property. Fixture behaviour on any machine but this one.

**Ceiling:** whether the advisory hook should chase the open tail, whether
consolidated multi-obligation reads should recur, and every routing choice on L-1 are
the user's questions under `R5`; what is checked here is that the layer's text matches
the repository, that the amendments are the fixes and rulings their sources named, and
that the bookkeeping around them did what its own rules say.
