# V3 review — FULL — subject `a7bb1d6`

**Subject range** `dbec65f3..a7bb1d6a` — 14 commits, of which **13 are this round's** and one
(`53cc76f`) belongs to a different track (§5.4).

**Verdict: `CHANGES_REQUIRED`** — one blocker (`B-1`), five findings, four observations.

The measurement layer is the strongest part of this round and it holds: of the fourteen load-bearing
figures I re-derived independently, eleven reproduce **exactly**, one reproduces in shape with an
off-by-one, one is mislabelled by unit, and one does not reproduce at all. Every code citation I
checked reads as claimed. The blocker is not in the measurements — it is in what the round built on
top of them: a new governance surface that is declared supreme over the instruction layer, made
mandatory reading for every cold read, and placed where no cold read can reach it.

---

## 1. What this round is, re-derived

Not taken from the dispatch, which carried the range and nothing else (`R2`).

| Question | Answer | Where I read it |
|---|---|---|
| Round | **Batch A / A1** — `.goals/plans/harness-record-layer-and-repo-split.plan.md`, steps 1–7 and 9, plus the decision-log construction round folded inside it | plan §Steps; commit bodies of `2f767f3` … `a7bb1d6` |
| Governing instructions | `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` (E1–E12 / R1–R10). The two `v3-harness-*-contract.md` are stubs pointing at it and say the checklist is its own counterpart | review-contract stub `:3`; checklist header `:9-12` |
| Budget position (`E9`) | This **is** the FULL. Before this record landed, no file in `migration/document-work-assurance-v3/` (103 entries) named any of the 14 SHAs. One user-approved fix + one targeted VERIFY remain | `ls migration/document-work-assurance-v3/` grepped for each SHA; `git log` |
| Verdict domain | FULL → `REVIEWED_NO_BLOCKER \| CHANGES_REQUIRED \| SPEC_GAP` (`R3`) | checklist `R3` |
| Authorization | plan step 7 records the seven decisions as the user's; `HD-10`…`HD-18` in `ResearchSystem/HARNESS-DECISIONS.md` each carry `· user ·` and a date. Preview-card approval is asserted in `cfc6a91`'s body ("预览卡经用户批准"); I see the record, not the approval | plan step 7; `HARNESS-DECISIONS.md`; `cfc6a91` body |
| Obligations | A1 measures, costs, lands exactly one ruled construction (`C1`), and puts the decisions — it does **not** build the record layer; step 8 (this review) and step 9 (A2's plan) close it | plan §Constraints, §Acceptance |
| Ledger state | `HARNESS-LEDGER.md` records A1 as closed and step 8 as owed, and forbids A2 opening before this review | `HARNESS-LEDGER.md:92-96` |

**Ceiling (`R7`).** Every ruling in `HARNESS-DECISIONS.md` and the preview-card approval were issued
in chat. I see their committed *records* and take them at face value; I did not and cannot verify the
conversations. "Fresh context" is marked, not verified (`R4`).

**Read coverage (`R4`).**

- *Read in full:* `CONSTRUCTION-CHECKLIST.md`; the two instruction-layer diffs; `HARNESS-DECISIONS.md`
  and its archive; `journal/batch-a1-2026-08-08.md` (755 lines); `journal/decision-log-2026-08-08.md`;
  both plans; `HARNESS-LEDGER.md`; `hooks/layer_path_check.py`; `tests/document_harness/test_readme_enumeration.py`;
  `dispatch.py` §"Instruction-layer reads"; all 14 commit bodies.
- *Ran myself, output pasted below:* the eight-run size table; the template-copy blob comparison;
  the CheckResult field census and first-hand output sizes; the review-record citation census; the
  CheckResult citation census; the instruction-layer size table; the commit-history mixing count;
  the `review-full.json` prose census; the M4 denominators; the full suite; `repo-audit.py`;
  `ledger_cap_check.py`; one mutation probe with sha256-checked restore.
- *Probed only:* `checks.py` / `candidate.py` / `flow.py` / `summary.py` / `assurance_state.py` /
  `review_subject.py` at the cited line ranges, not in full.
- *Not reviewed:* `53cc76f`'s 470 lines — classified out of the round (§5.4).
- **`UNVERIFIABLE`:** §10.2–§10.4's per-line five-way classification of four review records, and the
  34% "handle" sub-measure. The journal discloses at §10.6.2 that the per-line assignment was not
  persisted, so a re-checker must re-judge rather than diff. I re-derived the **denominators** exactly
  (below) and confirmed M4's originals were wrong; the class shares themselves I cannot recheck. This
  is not folded into supported: `HD-13` rests partly on numbers no command can reproduce.

---

## 2. Implementation (`R3` — lead)

### 2.1 The measurements

Fourteen figures re-derived from the tree at `a7bb1d6`. Commands and output:

**M1 — eight runs on one ruler (journal §1). Exact.**
```
run            files  lines |   evid   ctrl   scripts
p3-corr           65   2898 |   1238      0      1556
p4-bridge         55   2965 |    988    101      1780
p4-doc            89   4771 |   2272    143      2216
p5a-firewall      53   3092 |   1301    101      1589
p5a-shells        74   6100 |   2926    306      2476
p5b-claims        94   6165 |   3166     98      2658
p5b-firewall      73   4665 |   1780    242      2460
w1-r1             43   2165 |    990      0      1099
ALL              546  32821 |  14661    991     15834
```
Every cell matches journal §1. Method reproduced as stated (per-file `\n` count, no +1 for a missing
trailing newline, `__pycache__` excluded).

**§2(a)(b)(c) — template copies. Exact.**
```
copies found: 23  matching some historical template blob: 6  (journal: 6/23)
total lines in copies: 5329 (journal tmpl total 5,329)
matching by name: {'check_template_instance.py': 4, 'make_paragraph_map.py': 2}
copies by name: {'check_template_instance.py': 4, 'run_bind_v2.py': 7, 'run_evidence_v2.py': 7,
                 'run_repair.py': 2, 'compare_blocks.py': 1, 'make_paragraph_map.py': 2}
```
The load-bearing negative — **no** `run_bind_v2.py` or `run_evidence_v2.py` in any run was ever the
template's bytes — is confirmed against every historical blob of each template path. `HD-11`'s
"shared core + per-run delta, not a reference swap" rests on a sound measurement.

**§4.1 / §11.1 — CheckResult. Exact.**
```
per-check CheckResult files: 21     total lines: 678
distinct values across the 21:  base_revision 1 · boundary_observed.* 1 · candidate_ref.* 1
  · observed_tree.* 1 · verified_by 1        <- the 5 copied 21 times
  check_id 21 · kind 2 · subjects 9 · result_id 21 · evidence_ref.path 20   <- the 5 derivable
  result 1 · exit_code 1 · request_digest_sha256 21                          <- the 3 original
chk-*.out.txt: count 20 · zero-byte 3 ['chk-base-rooted','chk-diff-check','chk-manifest-unchanged']
              · 1..23 bytes 10 · all sizes [0,0,0,11,11,12,13,13,14,15,15,16,23,523,588,2330,3857,7145,7177,18422]
check-chk-manifest-unchanged.json → PASS  exit 0  (out file 0 bytes)
```
The decisive counter-example holds: a 0-byte first-hand output beside a `PASS`/`exit 0` verdict. `D2`
as originally posed ("persist or recompute") has no implementation, exactly as claimed.

**§11.2 — the prose is mostly in the machine artefact. Exact.**
```
review-full.json: lines 237 chars 32300      (journal 237 / 32,300)
counts: obligations 18  findings 12  residual 6      (journal 18 / 12 / 6)
obligation notes 11899 = 36.8%   finding statement+minimum_fix 11333 = 35.1%   residual 1763 = 5.5%
prose record 8ad8c2f.md: lines 189 chars 12218       (journal 189 / 12,218)
```
All three component percentages reproduce to the decimal; adding the fourth stated component
(instruction detail 4.5%) gives 81.9% and 217%, as written.

**§10.1 — the M4 errata. Exact, and the correction is right.**
```
v3-review-full-8ad8c2f     total=189 non-empty=154  (journal 154; M4 had said 179)
v3-review-verify-275da5b   total=237 non-empty=202  (journal 202; M4 had said 214)
v3-review-full-fef3a2e     total=146 non-empty=123  (journal 123; M4 had said 135)
v3-review-full-11ce5b4     total=270 non-empty=218  (journal 218)
```

**§6.2 — mixed history. Exact in shape, recomputed at the tip.**
```
total non-merge commits: 624   touching ResearchSystem/: 496   purely: 371
mixed: 125   of which only .goals/: 115   really other: 10
really-other breakdown: {'Thesis': 12, 'ExperimentLab': 1, 'AGENTS.md': 1, 'CLAUDE.md': 1, '.claude': 2}
```
Journal reported 613/487/366/121/111/10 with an identical breakdown; the deltas are this round's own
commits. The correction of "276+" to 7–12 stands.

**§12.4 — instruction-layer distribution. Line counts exact; unit mislabelled (`f-3`).**
```
REVIEW.md                  lines= 284  chars= 17886  bytes= 18000
CONSTRUCTION-CHECKLIST.md  lines= 173  chars= 13513  bytes= 13637
EXECUTION.md               lines= 171  chars= 10466  bytes= 10532
supersession-1             lines= 124  chars=  6433  bytes=  6480
supersession-2             lines= 113  chars=  7382  bytes=  7421
paragraph-map              lines=  44  chars=  2796  bytes=  2812
README.md                  lines=  38  chars=  7211  bytes=  7288
review-contract stub       lines=   5  chars=   695  bytes=   703
operating-contract stub    lines=   5  chars=   508  bytes=   516
TOTAL  lines=957  chars=66890  bytes=67389        (journal: 957 lines / 66,890 "B")
```

**§13.3 — the harness is a leaf. Confirmed by enumeration.** Every import statement in
`rsclib/document_harness/` (top-level module tallied):
```
__future__ 18 · collections 1 · contextlib 1 · dataclasses 7 · functools 3 · hashlib 2 · json 5
jsonschema 4 · pathlib 14 · posixpath 1 · re 3 · referencing 3 · rsclib 38 · shutil 1
subprocess 4 · tempfile 1 · typing 17 · unicodedata 1
```
and every one of the 38 `rsclib` imports stays inside `rsclib.document_harness` (grep for `rsclib`
import lines excluding `rsclib.document_harness` returns nothing). Zero product-side imports, as
claimed. Entry edges outside the package and outside tests are exactly two: `rsc.py` (7 call sites)
and `hooks/candidate_path_check.py:54`.

**§13.4 — group membership.** Group C = 144 files / 27,640 lines and group D = 546 / 32,821 both
reproduce **exactly**. Group B is now 946 lines, not 867 (`f-4`). Groups A and E rest on the human
three-way split the journal discloses at §13.6.1 and I did not re-judge.

### 2.2 Code citations

Every line reference I probed reads as the journal says:

| Cited | Found |
|---|---|
| `checks.py:334-338` — `subject_tree: candidate_commit` → `materialized_candidate` | `:334` `if check["subject_tree"] != "candidate_commit"` … `:337` `with materialized_candidate(...)` ✓ |
| `checks.py:384` stdout only; `:385`/`:391` verdict is the exit code | verbatim ✓ |
| `candidate.py:181-185` — `git worktree add --detach` materializes the whole repo | `:184` ✓ |
| `candidate.py:220` — inside `write_scope` **and** outside every `out` | docstring verbatim ✓ |
| `assurance_state.py:81-89` — `DIGEST_PROTECTED_FIELDS`, CheckResult absent | five fields, CheckResult not among them ✓ |
| `flow.py:110` `check_results_ref → EVIDENCED`; `:78` `review_ref → REVIEWED` | ✓ |
| `summary.py:96` `check_result_refs`; `:187` review binding | ✓ |
| `layer_path_check.py:29-40` `LAYER` nine-tuple, comment "Mirrors E10's membership sentence" | ✓ |

### 2.3 `C1` — the `E2` retirement

Both sites changed in one commit (`55fe4e9`): the enumeration drops the blob and the count goes
`Four` → `Three`. The result is internally consistent — three blobs named (`b2dbdf75`, `68031fa2`,
`e1a2f26b`) plus one directory, and the pack holds exactly the fifteen files `E2` claims. No residue:
`grep -n "Four\|signed plan\|8ad404b1" CONSTRUCTION-CHECKLIST.md` returns nothing.

The dangling-neighbour sweep is also correct. `8ad404b1` appears in 33 files repo-wide; **none** is
another instruction-layer member (`README` / `EXECUTION` / `REVIEW` / both stubs / both supersessions
/ `paragraph-map` are all clean). The remaining hits are plans, closed-run instructions, node records
and journals — derived statements under the checklist's own `:38-40`, correctly left alone.

The claim that `E2` has zero mechanical enforcement is true as written:
`grep -rn "b2dbdf75\|68031fa2\|e1a2f26b" ResearchSystem/tooling Thesis/Work/Tooling` → no output.

### 2.4 The battery

```
$ python -m pytest -q            (ResearchSystem/tooling)
632 passed in 115.77s
$ python Thesis/Work/Tooling/repo-audit.py       → RESULT: clean (exit 0)
$ python ResearchSystem/tooling/hooks/ledger_cap_check.py → exit 0   (HARNESS-LEDGER.md = 120 lines)
$ git status --porcelain                          → clean
```

**Mutation probe (`R8`).** The round changed `document-harness/README.md`, which
`test_readme_enumeration.py` pins. Neutered the `paragraph-map` stem in both delimited forms:
```
E       - ['paragraph-map']
E       + [] : schema files not mentioned in document-harness/README.md ...
FAILED tests/document_harness/test_readme_enumeration.py::ReadmeSchemaEnumeration
```
Value-level failure, not a crash. Restored from a scratchpad copy; sha256 identical before and after
(`6d83291e…`), `git status` on the path empty. `git checkout --` was not used. The round added no new
guard, so there is nothing else to probe — `HD-7` rules the decision log carries none, which is part
of `B-1`.

---

## 3. Blocker

### `B-1` — the supreme rule source sits outside the layer, and no cold read can reach it

**Location.** `ResearchSystem/document-harness/README.md:29` (the added "Decision log" row) ·
`ResearchSystem/HARNESS-DECISIONS.md:3-8` (the supremacy and must-read header) ·
`ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md:75-85` (`E10`'s membership sentence,
unchanged by this round).

**What the round asserts.** `HARNESS-DECISIONS.md` is "harness 的用户裁决的**最高 source of truth**;
instruction 层反向 base on 这里的裁决展开细则；细则与裁决冲突，**细则错**", and every cold read
"**必读 §live**". The README row repeats it: "every cold read MUST read its §live".

**The ground truth it violates.**

1. **`E10`: "The instruction layer is exactly these nine paths and nothing else."** A file that binds
   every future round and outranks instruction text is instruction; it is not in the nine. The
   consequences are not hypothetical — each of `E10`'s four protections fails to reach the file that
   now outranks the rules: no cold read of *it* is owed at a round's opening, no independent read
   before a round relies on it, no additive-or-subtractive-only discipline, and a change to it that
   changes what a rule requires does not open a round. `layer_path_check.py`'s `LAYER` — whose own
   comment says it "Mirrors E10's membership sentence" — does not cover it either, so a repository
   path newly written into an entry is unguarded; `HD-17` alone writes seven directory paths.

2. **The dispatch path cannot deliver the obligation.** `dispatch.py:626-639`'s `READ_PROMPT` hands a
   reader one charter and one instruction: derive "the layer's member set **from E10's own sentence**".
   The charter is `CONSTRUCTION-CHECKLIST.md`, which never names the decision log. A session entering
   through the generated read dispatch, or through `EXECUTION.md` / `REVIEW.md`, has no path to the
   MUST. Verified mechanically:
   ```
   $ grep -rn "HARNESS-DECISIONS" --include="*.py" --include="*.json" --include="*.js" \
       --include="*.sh" --include="*.yaml" --include="*.yml" .
   (no output)
   $ grep -rln "HARNESS-DECISIONS" .
   .goals/plans/harness-a2-construction.plan.md · .goals/plans/harness-record-layer-and-repo-split.plan.md
   .harness/runs.jsonl · document-harness/journal/batch-a1-2026-08-08.md
   document-harness/journal/decision-log-2026-08-08.md · document-harness/README.md
   ResearchSystem/HARNESS-DECISIONS-archive.md · ResearchSystem/HARNESS-DECISIONS.md · HARNESS-LEDGER.md
   ```
   Nothing mechanical reads it, and nothing a dispatched reader is pointed at mentions it.

3. **The round's own reasoning is the converse.** `HD-14` moves six rule sections out of
   `templates/run-v2/README.md` into `EXECUTION.md` precisely because they lack those four
   protections — journal §11.3 states it in as many words: "`E10` 给成员的保护是 …… 上面六节
   **一样都没有**". The same round then created a higher-authority file with the same gap. The defect
   class the round names is the defect class it introduced.

**Why this is a blocker and not a low.** It changes an actor's action, which `R9` makes the dividing
line: a cold reader's reading set is wrong by construction, not by accident. The named downstream
decision that goes wrong: `HD-5` and the A2 plan's resume pointer both make reading `§live` a
precondition for a resuming session, and `A2`'s first round is gated on this review — so the very next
round is the one that will enter through a role instruction and miss `HD-11`/`HD-12`/`HD-14`/`HD-17`.
The failure mode the decision log was built to end (the ledger's twelve orphan rulings, "已裁但只存在
于对话里的") returns one level up: rulings that exist, in a file nobody is told to open.

**Minimum fix — one of these, and it is an instruction-layer amendment either way.**

- **(a)** Add `ResearchSystem/HARNESS-DECISIONS.md` to `E10`'s membership sentence and to
  `layer_path_check.py:30-40`'s `LAYER` — one clause and one tuple entry. This buys the four
  protections and makes the READ_PROMPT's "derive from E10's own sentence" land on it. Cost:
  the file joins the per-round cold read at its own digest cost, and `HD-7`'s no-lint ruling would
  need re-examining for the path guard only.
- **(b)** If the user wants it outside the layer, write the read obligation into
  `CONSTRUCTION-CHECKLIST.md` itself, so the charter every dispatched reader is handed carries it,
  and state there that the file's own governance is discipline-only (`HD-7`).

I do not choose between them: `R5` puts "should this exist and in what form" with the user. What is
mine to say is that the obligation as currently written is unreachable from the only paths a cold
read travels.

**Prior disclosure does not discharge it.** The executor found the narrower half by self-audit —
`5144e86`'s title and the A1 plan's resume pointer question 1 both say the binding surface is the
README row only and hand it to the reviewer. Correct, and it is why this is one clean fix rather than
an argument. The wider half — that the file is outside `E10` altogether, so nothing governs its own
bytes — is not in that self-audit.

---

## 4. Findings (non-blocking)

### `f-1` — §12.2's uncited set is wrong, and its total does not reproduce (low)

Re-derived over the same corpus, excluding `chk-repo-audit.out.txt` (the journal's own, correct,
exclusion of an orphan list) and `.harness/runs.jsonl` (a machine autolog):
```
records: 53   cited: 49   occurrences: 294   matching lines: 276   (record,file) pairs: 185
never cited: ['v3-review-full-3ded65a', 'v3-review-full-86533f2',
              'v3-review-verify-440e205', 'v3-review-verify-45cae29']
```
The journal names three — `86533f2` · `verify-440e205` · `verify-45cae29` — and **omits
`v3-review-full-3ded65a`**, which is cited nowhere at all: its only occurrences outside itself are the
five `chk-repo-audit.out.txt` orphan lists, and its bare short SHA appears in no other file. Under the
stricter rule the count is 49/53, not 50/53. Under the looser rule (`.harness/runs.jsonl` counts, which
is `86533f2`'s only non-orphan hit) the count is 50/53 but the set is
`{3ded65a, 440e205, 45cae29}` — still not the set written.

The total "169 次" reproduces under none of the three natural counting rules (294 / 276 / 185), and
the journal does not state which rule produces it — so the figure cannot be re-checked, which is what
`E3` asks of a count.

**The ruling is unaffected.** `HD-13`'s hardest class is confirmed independently: 20 occurrences in
`.py` files, and all four named exemplars read verbatim —
`layer_path_check.py:17` cites `v3-review-full-8ec4c60.md` B1 · `instruction.py:164` cites
`v3-review-full-3657687.md` f1 · `test_instruction_form.py:151` cites `v3-review-verify-c7fb720.md`
V-1 · `repo-audit.py:98` cites `v3-review-full-ca9c055.md`. Review records are load-bearing as rule
provenance; that shape survives the arithmetic.

**Minimum fix:** state the counting rule and re-run it; correct the uncited list to four.

### `f-2` — §12.1's enumeration does not reproduce; the conclusion does (low)

Scanning every per-check `check-<id>.json` filename (78 distinct) across the repository:
```
files referencing one: 21   total occurrences: 147
  8 × <run>/control/assurance-candidate.json          (11,12,13,17,17,21,24,8)
  1 × w1-r1/evidence/review-package.json
  4 × <run>/run_bind_v2.py       2 × <run>/run_closeout.py
  2 × p5b-claims/evidence/review-{full,verify}.json
  2 × <run>/issues/*.json
  1 × v3-review-verify-275da5b.md
  1 × journal/batch-a1-2026-08-08.md
```
The journal reports "命中共 25 处" in five buckets, names `v3-review-full-dcfb2f2.md` (my scan finds
`v3-review-verify-275da5b.md` instead), names "两个 test fixture" (none appear unless the aggregate
`check-results.json` is included, which is a different object), and does not list the two `issues/*.json`
files. Separately, the per-run `check_result_refs` tally "8/11/11/24/12/17/16/21 ≈ 120" is **119**:
p4-doc has 23 refs, not 24 — 24 is its `check-*.json` file count, which includes the aggregate.

**The conclusion is if anything stronger under my scan than under theirs.** All 21 referencing files
are the run's own control plane, scripts, evidence or issue records; that run's own review while it was
live; or this journal. No later round cites a closed run's CheckResult. `HD-12` is not affected.

### `f-3` — §12.4 labels characters as bytes (low)

All nine per-member figures reproduce **exactly** as `len(text)` of the committed blob; the true UTF-8
sizes are larger (totals: 957 lines / 66,890 characters / **67,389 bytes**). The `D7` conclusion is
safe under either unit — `templates/run-v2/README.md` at 290 lines / 20,481 chars is +6 lines and
+15% over `REVIEW.md` on both counts. Note also that the working-tree copy of
`CONSTRUCTION-CHECKLIST.md` carries CRLF while `REVIEW.md` does not, so a naive `wc -c` disagrees with
the blob by exactly one line count on that file — worth knowing before the figure is re-taken.

**Minimum fix:** relabel "B" as characters, or re-measure in bytes.

### `f-4` — §13.4's group-B figure was invalidated inside the round (`E3`, low)

"B 治理账本 5 files / 867 lines" was measured at `41b4835`; `0b29a19` and `a7bb1d6` then added
`HD-15`–`HD-18` and rewrote the ledger. The same five files now total **946** lines. `E3`'s "measure
last: a figure is invalidated by any later change to what it measures" is the rule; the drift is 79
lines against `HD-16`'s 57,273, so nothing turns on it — but it is the exact shape `E3` names, inside
one round.

### `f-5` — commit form: one empty body, seven unnamed kinds, no round title (`E8`, low)

`5144e86` has **no body at all** — `git log -1 --format=%b` returns empty — against `E8`'s "one dense
paragraph" and its requirement to name the commit's kind "so the review side can attribute it without
asking". `2f767f3` / `ad3c553` / `31ca13e` / `55fe4e9` / `2c3cc99` / `cfc6a91` describe their nature in
prose but do not use the enumerated vocabulary; the explicit `kind:` line begins at `444fc24`.
Separately, no commit in the round carries `E8`'s `V3-<ROUND>-v1` title — the branch's own history
shows that form in use (`V3-HI-REDEEM-5-v1`, `V3-HI-REDEEM-5-FIX-v1`, `V3-HI-REDEEM-5-CLOSEOUT-v1`),
so the deviation is visible against precedent. Attribution was in fact possible here because the later
bodies name A1 explicitly, so this is form and not substance — but it is the form that exists to make
`E9`'s "never self-classify which round consumed what" checkable.

---

## 5. Boundary and process (`R3` — second)

### 5.1 Change boundary — held, for the round's own 13 commits

Classified by hand from `git show --name-status` per commit. All 13 harness commits stay inside
`.goals/plans/harness-*.plan.md`, `ResearchSystem/HARNESS-{LEDGER,DECISIONS,DECISIONS-archive}.md`,
`ResearchSystem/document-harness/{CONSTRUCTION-CHECKLIST,README}.md`, and
`ResearchSystem/document-harness/journal/`. No product path, no schema, no run directory, no closed-run
byte. The plan's "stage explicit paths only" claim holds for every commit I checked.

### 5.2 Frozen surface — intact

`E2`'s remaining surface is untouched: contract, both supersessions and the fifteen-file pack show no
diff in the range (`git diff --name-status` lists eleven paths, none of them frozen). The one frozen
byte that moved is the one the user retired, and it moved by leaving the list rather than by being
written.

### 5.3 `E10` debt — confirmed outstanding, correctly disclosed

Two layer members changed blob in this range:
```
CONSTRUCTION-CHECKLIST.md  4d0c7330 → ce6d1609
README.md                  70bd9f0b → dd1c7c3e
```
The most recent read record is `v3-checkpoint-read-a5a04c3.md` (2026-08-05), which cannot cover either
new blob. So the round owes: the opening cold read it did not take, and the independent read of the
amended text before any round relies on it. Both are disclosed — journal §9.1, plan resume pointer,
`55fe4e9` and `cfc6a91` bodies, and the ledger's "欠 step 8". I confirm the debt is real and unpaid,
and that **this FULL is not it**: `E10` says an amendment's read has the amendment text as its subject
and "is never banked as the round's FULL".

On reliance: I checked whether anything in the range relies on the amended `E2` text in `E10`'s sense
(an outcome would change if the text changed). It does not. `HD-16`'s archiving of the plan into the
new repository turns on `E2` freezing *blobs rather than paths* — pre-existing text — so the ruling
would stand unchanged had the retirement not landed. The round's position here is sound.

### 5.4 The dispatched range is not co-extensive with the round (observation `ob-1`)

`53cc76f` "docs(research-system): extend P5C-P8 plan through P9" is a **foreign commit** inside the
subject range. It lands between `0b29a19` (16:28) and `a7bb1d6` (16:53), touches
`.goals/plans/research-system-p5c-p8-revision.plan.md` and adds
`.goals/plans/research-system-p9-architecture.draft.md`, and contributes **470 of the range's 1,995
inserted lines (24%)**. It is the concurrent product-track session that five of this round's own commit
bodies name as the thing blocking `rsc v3 dispatch`; it carries no kind line, and its body records that
it bypassed the local candidate-path hook. It belongs to `.goals/LEDGER.md`'s product track, not the
harness track, so I classified it out and did not review it.

`E12` makes the handoff one range, and `R2` makes classifying its paths mine — which is how this
surfaced. But a reviewer who took the range at face value would have reviewed 470 lines of another
track's planning as though they were this round's, or worse, treated its hook bypass as this round's.
Either the base/tip must be chosen so a foreign commit cannot fall inside, or the round must record
which commits are its own. Naming it rather than adjudicating it: the dispatch mechanism is not this
round's subject.

### 5.5 `E12` — a written tip already short (observation `ob-2`)

`.goals/plans/harness-a2-construction.plan.md:12` writes "A1's tip at authoring time was `41b4835`",
which is three commits short of `a7bb1d6` — precisely the shortfall `E12` describes ("a written tip is
short by at least the commit that wrote it, and what it drops is the round's last-written records").
Here it drops `0b29a19`, `53cc76f` and `a7bb1d6`. Nothing binds to it — it is labelled informational
and `base_commit` is deliberately deferred to A2's first round — so this is a note so that the next
round does not promote it into a range.

### 5.6 `E2` retirement's honesty edge understates the detection (observation `ob-3`, favourable)

The plan records "retirement removes a *prohibition* while the `N0` record keeps the change
*detectable*", and the narrow claim behind it is true (nothing in `ResearchSystem/tooling/` reads
`E2`'s blob ids). But detection is stronger than record-based: `N1/governance-exemptions.json:31`
grandfathers the plan **by blob**, and `checks.py:661` looks the exemption up by blob
(`exemption = exemptions.get(blob)`) and fails closed, raising `V3-GOVERNANCE-SELF-APPROVAL` when no
entry matches. Edit the plan and the exemption evaporates by itself; the next governance scan flags it.
Worth carrying into the split batch, where `HD-16` archives the plan into the new repository — *moving*
the file is free under a blob-keyed exemption, *editing* it is not.

### 5.7 The shape (`R5`, observation `ob-4`)

`R5` asks me to report the shape when successive rounds keep adding components, and to leave the
question with the user. The shape: this round added a tenth and eleventh governance surface
(`HARNESS-DECISIONS.md` + its archive) to a construction side already carrying a nine-member
instruction layer, a ledger, a ledger archive, a rider bank, per-round journals, per-round review
records, commit bodies, and HarnessIssue. The decision-log journal §2 argues each existing home is
shape-mismatched and the user ruled it, so whether it should exist is not mine. What I record is the
consequence: the number of places a session must consult before it may act rose again, the newest one
is the only one with **no** mechanical binding of any kind (`HD-7`), and it is the one now declared to
outrank all the others. `B-1` is the first bill for that combination.

---

## 6. Honesty ceilings

1. **The classification measurements are `UNVERIFIABLE`, not supported.** §10.2's five-way per-line
   split (配方 43.2% / 判断 29.4% / 绑定 10.5% / 证词 5.9% / 骨架 11.0%), §10.3's 34% handle rate and
   §10.4's section-level rollups rest on a per-line assignment the journal deliberately did not persist
   (§10.6.2). I reproduced the denominators exactly and confirmed the coverage assertion is the right
   discipline, but a re-checker must re-judge every line rather than diff a table. `HD-13` partly rests
   on numbers no command reproduces. The journal says so itself; I am declining to fold it into
   "supported".
2. **The HARNESS / PRODUCT / AMBIG three-way split (§13.3) and group A (§13.6.1) are human judgments**
   and I did not re-judge them. I verified the parts that are path-defined (C, D exactly; B with `f-4`)
   and the arithmetic of `A+B+C = 242 / 57,273`.
3. **Reference counts are substring counts** in both the journal's method and mine. Magnitude is
   trustworthy; exact values are not — which is the journal's own §13.6.2 and is why `f-1`'s
   discrepancy is reported as an un-recheckable figure rather than as a wrong one.
4. **Process claims are marked, not verified** (`R4`): the preview-card approval, the user rulings
   behind `HD-10`–`HD-18`, "fresh context", and the assertion that the concurrent session — not this
   one — held the dirty tree. I read their committed records only.
5. **One mutation probe, not a battery.** The round added no guard, so `E4`/`R8` had one live target:
   the pinned README. Mutation proves that test has binding force, not that the round's guarding is
   sufficient — and the file at the centre of `B-1` has no guard to probe.
6. **`53cc76f` is unreviewed** by choice (§5.4). If the user intended it inside the round, this FULL
   does not cover it.
