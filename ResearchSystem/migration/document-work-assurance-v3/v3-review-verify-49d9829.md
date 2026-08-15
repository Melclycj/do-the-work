# VERIFY — `1592181..49d9829` (the reform 轮's single repair: B1, B2, B3, F-2, plus the F-1/F-3 banking commit)

**Verdict: `REVIEWED_NO_BLOCKER`.**

All four accepted findings are closed by the fix the FULL named, and the two that were code
defects are now held by tests that go red when the defect is put back. The B1 collision is
gone on the real bytes that were going to hit it: staging `supersession-2` with the exact
edits rider rows `S2-1` and `L-1` schedule now exits 0, while the historical `dcced4e` defect
still blocks under the new scope. The two B2 escape mutations the FULL demonstrated
(`M3`, `M5`) both go red on the repaired suite, as do six further mutations I chose myself.
Nothing frozen moved. Four observations, none of them a defect in the repair.

---

## 1. Subject, re-derived (`R2`)

```
$ git rev-parse HEAD
49d9829f622fd5c5659de401ffd4397cbdefa4c8          # == the handed range's tip
$ git log --oneline 1592181..49d9829
49d9829 V3-REFORM-BANK-F1-F3-v1
1c45e24 V3-REFORM-REPAIR-B1-B2-B3-F2-v1
$ git status --porcelain
?? ResearchSystem/docs/                            # untracked, predates this work, not in the subject
$ cat .harness/review-pending.json
{"kind":"construction-round",
 "subject":"1592181cd2e0f57433a33cd8550ef1e8a895db96..49d9829f622fd5c5659de401ffd4397cbdefa4c8",
 "dispatched_at":"2026-07-29T14:19:25+00:00"}
$ git log -1 --format=%cI 49d9829
2026-07-30T00:19:24+10:00                          # == 2026-07-29T14:19:24Z, one second before dispatch
```

The marker's subject is byte-identical to the range I was handed; its base is the FULL's
record commit and its tip is `HEAD`. `E9`'s window clause holds: the branch has taken no
commit since dispatch.

**Change set, classified by hand** — `git diff --name-status 1592181..49d9829`, 4 paths, all
`M`, all under `ResearchSystem/`:

| commit | paths | kind |
|---|---|---|
| `1c45e24` (repair) | `tooling/hooks/layer_path_check.py`, `tooling/tests/document_harness/test_precommit_checks.py`, `migration/…/journal/reform-2026-07-29.md` | the three files the journal declares as the approved boundary |
| `49d9829` (banking) | `HARNESS-RIDERS.md` | +2 rows (`F-1r`, `F-3r`), nothing else |

**Round, budget, authorization.** The ledger at `1592181` still names the reform 轮 as in
flight with the sequence B → A → FULL → (fix+VERIFY) → amendment read → Phase C2. `E9`'s test
is *has a valid independent FULL already occurred?* — yes: `v3-review-full-8ec4c60.md`,
`CHANGES_REQUIRED`, its record landed as `1592181`. So `1c45e24` is the round's one fix and
obliges this VERIFY, which is the third and last thing the cap allows. No fourth commit
exists.

**`R7` ceiling.** The user's acceptance of {B1, B2, B3, F-2}, the choice of the diff-scoped
shape for B1, the three-file boundary, the ruling that the deleted note stays deleted, and the
routing of F-1/F-3 to the bank are all recorded **only in the journal and the two commit
bodies, all executor-authored**. They are in the repository, but the repository holds no
user-attested trace of them. Stated as a ceiling, not a block.

---

## 2. Implementation first (`R3`) — what I ran

**Suites, re-run by me:**

```
Ran 169 tests in 25.263s  OK      (tooling/tests/document_harness)
Ran 329 tests in 50.649s  OK      (tooling/tests/document_harness_review)
Ran  18 tests in  4.461s  OK      (test_precommit_checks alone — the mutation baseline)
```

169 is 164 + 5, and I count exactly five new test methods in the diff, so the journal's
"5 cases added" is the diff and not a description of it.

**Shipped guard bytes**, so every mutation below is keyed to what actually ships:

```
$ sha256sum ResearchSystem/tooling/hooks/{layer_path_check,ledger_cap_check}.py
864fb40258685d4ebb88d316715c4c31c8830c6ab3391830fe1d90e420eff301  layer_path_check.py
aa4bc454b7e20cf944ebad6866226b4b0d059dabedf67b21632404776f117d7b  ledger_cap_check.py
```

Both match the journal's reported prefixes (`864fb40258685d4e`, `aa4bc454b7e20cf9`).

### 2.1 Mutation matrix (`R8`) — eight mutations, real defect shapes

Each applied to the shipped module from a sha256-checked scratchpad copy, `test_precommit_checks`
run, module restored from that copy, sha re-verified. Every mutation asserted `match count == 1`
before it was applied; one that failed that assertion was **discarded and re-authored**, and is
recorded below rather than counted (a mutation that does not land proves nothing).

| # | mutation (the real defect it reproduces) | result |
|---|---|---|
| V1 | `ledger_cap_check.LEDGER` typo'd — the guard can never fire on the real ledger (**the FULL's M3**) | **RED** (2 failures) |
| V2 | `README.md` dropped from `LAYER` — the member stops being scanned (**the FULL's M5**) | **RED** (2 failures) |
| V3 | `supersession-2` dropped from `LAYER` — a *different* member, to prove the new case is not README-shaped | **RED** (2 failures) |
| V4 | `LAYER`'s first two entries transposed — probes whether the equality binds the tuple or only the set | **RED** (1 failure) |
| V5′ | `check` reverted to the pre-repair whole-file read (valid Python, no crash) | **RED** — exactly `test_a_pre_existing_token_is_not_this_batchs_to_repair` |
| V6 | `added_lines` returns `[]` always — the guard goes permanently silent | **RED** (11 failures) |
| V7 | the missing-prefix class stops being flagged | **RED** (1 failure) |
| V8 | the broken-`ResearchSystem/`-prefix class stops being flagged | **RED** (10 failures) |

`restored_sha_match=True` on all eight; the worktree's `layer_path_check.py` is
`864fb402…` again and `git status --porcelain` is unchanged from §1.

**Discarded, disclosed.** My first V5 spliced the whole-file expression into the middle of
`text = "\n".join(…)`, producing `"\n".subprocess.run(…)` — 14 *errors*, i.e. a crash. Under
`R8` that proves the test touched the code, not that it binds the behaviour. V5′ above
replaces the entire statement with a syntactically valid whole-file read, and its single
failure names the one test written for B1. That is the binding claim; the crashing run is not
evidence and is not counted.

### 2.2 The B1 collision, reproduced on the real bytes rather than a synthetic case (`E7`)

Two disposable repositories, the actual blobs and the actual `supersession-2` file:

```
A0 baseline (pre-defect blob committed, nothing staged)              -> 0
A1 stage 11d147e's defective checklist blob (dcced4e)                -> 1   BLOCKED: `schema/document-assurance-v3/` — prefix missing
A2 stage 7615733's repaired blob (d322816)                           -> 0
B0 supersession-2 staged as a new file (every line added)            -> 1   both tokens flagged
B1 supersession-2 + one clean appended line                          -> 0
C  supersession-2 with the `assurance/runs/` line itself rewritten   -> 1
```

`A1`/`A2` are the exact historical defect the guard was built for, replayed as a *staged diff*:
the class the guard exists to catch still binds under the narrowed scope. `B1` is the FULL's
blocker, gone.

And the two rider rows that were going to hit it, redeemed for real — `S2-1` targets
`supersession-2` §1 (lines 14–36), `L-1` targets §3 (lines 64–76), while the offending tokens
sit at line 58 (§2) and line 80 (§4):

```
added lines seen by the guard:
  ['> Widened citation: the numbers the S2-1 rider says the citation is narrower than.',
   'The bytes `pointer_for` itself produces are not prior text (L-1 byte-level fix).']
S2-1 + L-1 redemption staged together -> exit 0
```

The scheduled collision is not merely narrowed — for these two riders it is eliminated by
construction, because neither one's target section contains a bad token.

### 2.3 The journal's pasted measurement, re-derived

`unresolved_tokens()` over the whole current text of all eight live members, my run:

```
CONSTRUCTION-CHECKLIST.md            clean
README.md                            clean
EXECUTION.md                         clean
REVIEW.md                            clean
v3-harness-operating-contract.md     clean
v3-harness-review-contract.md        `tooling/tests/fixtures/expected-construction-prompt.txt` -> prefix missing
supersession-1.md                    `schema/document-assurance-v3/review.v2.schema.json`      -> prefix missing
supersession-2.md                    `assurance/runs/`, `schema/`                              -> prefix missing
```

Identical to the table the repair pasted into the journal, member for member and token for
token. See O-2 for the one seam in how it is labelled.

---

## 3. The four accepted findings, one by one

### B1 — closed

`layer_path_check.py:64-75` adds `added_lines()` (`git diff --cached -U0`, `+` lines minus the
`+++` header) and `check()` scans only those. The whole-file `git show :path` read is **deleted**,
not supplemented — the `E6` direction. Held by two new tests: a negative control
(pre-existing token + a clean added line → 0) and a must-fire (clean base + a newly added bad
token → 1). V5′ shows the negative control is what binds the scope. The B1 measurement is in
the journal, which is where the round's own `E3` clause wanted it.

I checked the scope change for a new hole and found none that matters: a moved or reflowed
line is an added line and is still scanned; the `TOKEN` regex excludes whitespace, so joining
non-adjacent added lines with `\n` can neither fabricate a token across the join nor lose one
inside a line; a staged deletion yields no added lines, which is the same clean result the old
`shown.returncode != 0` branch produced.

### B2 — closed

`CHECKLIST` and `LEDGER` are hand-written literals (`:21-22`), `test_the_guard_targets_the_real_ledger_path`
asserts `ledger_cap_check.LEDGER` against the literal, and a new `LayerMembership` class
carries a hand-written eight-path tuple asserted equal to `LAYER` plus a subTest that stages
every member and requires each to block. V1 and V2 — the FULL's two escapes — are now red,
V3 shows the membership case is not README-specific, and V4 shows the assertion pins the
ordered tuple, not a set. This is `E5` as written: the expectation is independent of the
thing it guards.

### B3 — closed

The journal's wrong bullet is annotated in place (`*[Corrected below — B3: the "never
consumed" half of this sentence is false.]*`) and a new §"B3" states what the record shows —
the note was the `451e8b0` cold read's dispatch document, its member table is M-1's subject,
and the deletion stands as superseded by the generator's `--read` mode. I re-read
`v3-cold-read-451e8b0.md` M-1 (`:104-148`) and the correction is faithful to it: M-1(a) turns
on the dispatched member set having dropped supersession-1, which is the note's table. The
wrong sentence is *kept* with a marker rather than rewritten, which is the right call for an
append-only record — the false claim is no longer reachable without its correction, and a
grep for it lands on both.

`717e547`'s body carries the same wrong ground and is immutable; the journal correction quotes
it and is the only available remedy.

### F-2 — closed

The journal now pastes `D:/Thesis/.git/hooks/pre-commit` lines 37-49. I read the file: the
paste is byte-accurate and the line numbers are right. See O-1 for the one line it stops
short of.

---

## 4. The rest of the repair diff, and the permanent boundaries

**Beyond the four fixes the repair diff contains nothing else.** I read both diffs in full;
every hunk is attributable to B1, B2, B3 or F-2, including the docstring rewrite (which states
the new scope accurately) and the `BLOCKED:` message gaining the word "newly added", which is
now true of what the guard reports.

**`E2`** — `git diff --name-only 1592181..49d9829 -- ResearchSystem/schema/document-assurance-v3/
ResearchSystem/contract/` is empty; the schema-pack tree sha is `ca47f575…` at both ends of the
range; supersession-1's blob is `68031fa2ca31272e…`, the byte string `E2` names. Nothing frozen
moved.

**`E8`** — linear parents (`49d9829→1c45e24→1592181`), no amend, no push
(`git rev-list --count origin/main..HEAD` → 274, three more than the FULL's 271, matching
record + repair + banking exactly), single dense `V3-<ROUND>-v1` titles, one paragraph each,
`%(trailers)` empty on both. Both bodies name their kind in the first clause — "Review fix"
and "Administrative banking commit" — which is what `E8` asks for.

**`E9` boundary discipline.** The banking commit moves a fourth file, outside the approved
three-file repair boundary. It is a separate commit, it carries no repair content, and its
body says so explicitly rather than letting the reader infer it. `E9` requires that exceeding
or reordering around an approved boundary be *said, never silent*; it was said. See O-3 for
what it discloses about the repair commit's own body.

**`E10`** — no instruction-layer member is in the range. Nothing here relies on unread
amendment text.

**`E6`** — worth recording because it is the rule most often lost in a repair: B1 deleted
machinery rather than adding a compensating guard, B3's fix is text only, and B2 added tests
rather than production code. No fix in this round required new machinery.

---

## 5. Observations (`R5` — reported; the conclusion is the user's)

- **O-1 — F-2's paste stops one line short of the loop it demonstrates.** The block is
  labelled "lines 37-49" and is accurate for that range, but `done` is line 50, so the pasted
  shell reads as an unterminated `for`. Everything the README row asserts — three scripts,
  existence-guarded, non-zero propagates — is visible in what was pasted, and I confirmed the
  real file, so no decision here turns on it. The one downstream action it could bend is
  someone reconstructing the wiring on a second machine from the journal alone, which would be
  a copy-paste of an unclosed loop. The hook is untracked, so the missing line is not
  recoverable from any committed record — only from the line-number label. Routing is the
  user's; it is a two-line edit whenever the journal is next touched.
- **O-2 — the journal's eight-member table is the pre-repair guard's output, correctly
  attributed but labelled as "the guard's output".** The shipped `check()` can no longer
  produce it, because the repair changed the thing that measures — which is `E3`'s own trigger.
  The table is nonetheless still *true*: I re-derived it through the unchanged
  `unresolved_tokens()` and it matches exactly (§2.3). Naming the attribution
  ("reviewer's run, `v3-review-full-8ec4c60.md` §2") is what keeps this honest rather than
  stale.
- **O-3 — the sequencing slip is self-disclosed, which makes it a different animal from the
  ledger's open question ①.** `1c45e24`'s body asserts the banking in the present tense one
  commit before it happened. The ledger's unresolved question is about a stated *reason* being
  factually wrong and being caught only by a later independent read; here the author caught it,
  named it, and made the assertion true in the next commit. I report the distinction because
  the question is open and this instance is evidence for it, not because it is a defect.
- **O-4 — a counter-datapoint to the FULL's O-5.** The FULL observed that rounds were closing
  findings by accumulating components. This repair adds no component: it narrows one guard by
  deleting its whole-file read, adds five tests and two rider rows. Whether that is a turn or a
  single data point is the user's call; recording it because O-5's shape is only visible across
  rounds and this is the next one.

---

## 6. Disclosure (`R4`)

**Read in full.** `CONSTRUCTION-CHECKLIST.md` (131); `v3-harness-review-contract.md` (5);
`v3-review-full-8ec4c60.md` (334); `journal/reform-2026-07-29.md` (126);
`HARNESS-LEDGER.md` (64); `HARNESS-RIDERS.md` (33); `layer_path_check.py` (104);
`test_precommit_checks.py` (179); `tests/document_harness/_harness.py` `TempRepo` setup;
`D:/Thesis/.git/hooks/pre-commit` lines 30-52 (untracked); both commit bodies; the full diff
of all 4 changed paths.

**Sampled.** `v3-cold-read-451e8b0.md` (264) — M-1 §`:104-148` in full plus targeted `grep`,
not end to end. `supersession-2` (110) — section headers, the two token-bearing lines, and its
bytes as guard input; not read as prose. `ledger_cap_check.py` / `review_freeze_check.py`
through the mutation harness only.

**Not read this session.** `EXECUTION.md`, `REVIEW.md`, supersession-1, `rsc.py`,
`dispatch.py` — none is in the range. My statements about supersession-1 are its blob sha and
the guard's output over its bytes, not a reading of its content.

**Probed only.** `git rev-list --count origin/main..HEAD` → 274; the schema-pack tree sha at
both ends of the range; `%(trailers)` on both commits; `git check-ignore` on the dispatch
marker (`.gitignore:19` — so writing the range into the marker is not a commit, and `E12`'s
"a written tip is short by the commit that wrote it" does not bite here).

**`UNVERIFIABLE`.** Every user decision this round executes — the acceptance of the four
findings, the diff-scoped choice for B1, the three-file boundary, the not-restored ruling, the
F-1/F-3 routing. All are executor-authored records of chat. I verified they are *internally
consistent* with the diff; I cannot verify they are what the user said.

**Marked, not verified.** That this session is fresh context — a process claim with no
evidence lock. `R1` is answered by who set the question, which is why §1 re-derives the round,
budget and authorization rather than adopting the prompt's framing.

**Mutation caveat (`R4`).** Eight mutations prove these tests have binding force on the shapes
I chose, not that the force is sufficient. This is a VERIFY, not a re-certification: I covered
the four accepted findings, the whole repair diff, and the permanent boundaries. The parts of
the round the FULL passed were not re-litigated, and the FULL's own caveat still stands —
B1 was a defect no mutation would have found, because it needed the guard run over real inputs
the suite never gives it. That is the class §2.2 now runs deliberately.
