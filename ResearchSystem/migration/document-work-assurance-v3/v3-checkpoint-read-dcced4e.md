# Checkpoint read — `CONSTRUCTION-CHECKLIST.md` blob `dcced4e6`, the E2 schema-pack amendment

**No verdict.** A read is not a round (R3): it spends no budget, carries no verdict, and its output
is findings tiered must-fix / low / observation. This is the independent re-read the convergence
clause of E10 owes on the amended bytes, and **no round, FULL or VERIFY, is banked as it.**

**Findings: 1 must-fix, 1 low, 1 banked wording-level, 5 observations.** Labels are local to this
record; cite them as `read dcced4e M-1` and so on — the `M-1`/`M-2` of read `f9a6600` and the
earlier reads' labels are different findings.

---

## 1. Subject, re-derived

The subject is a text, not a range:

```
$ git cat-file -t dcced4e6cba137ad8de47af126ba42b117dd8454
blob
$ git rev-parse 11d147e:ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md
dcced4e6cba137ad8de47af126ba42b117dd8454
$ git hash-object ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md
dcced4e6cba137ad8de47af126ba42b117dd8454
$ git status --porcelain ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md
(empty)
$ git cat-file -p dcced4e | wc -l
122
```

**`HEAD` moved while I was reading.** It was `11d147e` when I established identity and `f854b72`
when I re-derived the window. `f854b72` (`V3-RULING-NEXT-ITERATION-THRESHOLD-v1`) touches
`HARNESS-LEDGER.md` only, six insertions, and the subject blob is unchanged under it:

```
$ git rev-parse --short HEAD
f854b72
$ git show --stat --format='' f854b72
 ResearchSystem/HARNESS-LEDGER.md | 6 ++++++
$ git rev-parse HEAD:ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md
dcced4e6cba137ad8de47af126ba42b117dd8454
```

`git diff f9a6600 dcced4e` is the amendment and nothing else: **one hunk, in `E2`**, four lines out
and six in. The amended rule, subject lines 23-31:

```
23  - **E2** Frozen bytes are untouchable, and the list is exactly this: signed plan blob
24    `8ad404b1…`, contract `b2dbdf75…`, supersession-1 `68031fa2…`, and every existing file in
25    the `schema/document-assurance-v3/` pack, which `rsclib/document_harness` already treats as
26    one frozen object. Three blobs and one directory, both decidable by inspection, so nothing
27    has to decide what *signed* means or which schemas N0 named; **a path outside them is not
28    frozen by this rule**, and this harness does not claim to freeze instruments it does not
29    govern. When the cleanest fix needs one, take the in-boundary fix and
30    record why, or stop with `SPEC_GAP`. A boundary declared anywhere else — a plan's freeze
31    surface, a round's own card — is derived from this rule and never independently authoritative.
```

Separated, because they carry different weight below:

- **A-1 (lines 24-25)** — the fourth item becomes *"every existing file in the
  `schema/document-assurance-v3/` pack"*. Answers read `f9a6600`'s `M-1`.
- **A-2 (lines 25-26)** — a new justifying clause: *"which `rsclib/document_harness` already treats
  as one frozen object"*. Nothing in the previous text corresponded to it.
- **A-3 (line 26)** — *"Three blobs and one directory, both decidable by inspection"* replaces
  *"Enumerated by blob"*.
- **A-4 (lines 27-29)** — *"a **path** outside them"* replaces *"a **file** not listed"*, and
  *"this harness does not claim to freeze instruments it does not govern"* replaces *"signed
  instruments this harness does not govern are frozen by their own tracks, not here."*
- **Unchanged** — the three blob literals and the whole `SPEC_GAP` / derived-boundary tail; the
  tail's first line moves in the diff only as a rewrap.

Read `f9a6600`'s `M-2` is answered outside the subject, in `HARNESS-LEDGER.md` at the same commit.

---

## 2. The precondition, checked before anything else

C-3's route is available only *"for as long as no round has relied on the text."* The commit
asserts this; R2 forbids accepting it.

**The tight window.** Between the previously-read blob's commit and this amendment there is exactly
one commit:

```
$ git log --format='%h %s' 6f96139..11d147e
11d147e V3-E2-SCHEMA-PACK-AND-FACT-CORRECTION-v1
0a4fad8 V3-REVIEW-RECORD-E2-BLOB-ENUMERATION-READ-f9a6600-v1
$ git show --stat --format='' 0a4fad8
 .../v3-checkpoint-read-f9a6600.md | 386 +++++
```

One review record, one file, 386 insertions. A read is not a round (R3), so nothing in this window
is a round at all.

**The wide window, re-derived rather than carried over.** Twelve commits since `f054a08`, and their
union of touched paths:

```
$ git log --format='%h %s' f054a08..HEAD | wc -l
12
$ git diff --stat f054a08..HEAD
 ResearchSystem/HARNESS-LEDGER.md                   | 127 ++++++-
 .../document-harness/CONSTRUCTION-CHECKLIST.md     |  20 +-
 .../v3-checkpoint-read-9f2ec9a.md                  | 297 ++++++
 .../v3-checkpoint-read-f97b348.md                  | 236 ++++++
 .../v3-checkpoint-read-f9a6600.md                  | 386 ++++++
 .../v3-dispatch-checklist-amendment-read.md        |  25 ++
 .../v3-review-verify-f054a08.md                    | 327 ++++++
 7 files changed, 1402 insertions(+), 16 deletions(-)
```

Seven files: three review records, one VERIFY record, the ledger, one dispatch, and the checklist
itself. **No code, no schema, no test, no fixture, no contract byte.** No FULL, no fix, no VERIFY.

I read the two ledger-only commits in this window that postdate the last read rather than trusting
their `--stat`. `f854b72` is a threshold ruling; it *characterizes* the amended `E2` (*"`E2` 现在已
不依赖任何 digest ——它是三个 git blob id 加一个目录路径"*) but takes no outcome from it, which E10
names as citing, not reliance. The route was available and remains so.

---

## 3. Must-fix

### M-1 — A-2 states as code behaviour what is only a module docstring; the one object the module actually binds covers ten of the pack's fourteen files, and the tests deliberately refuse the direction A-2 asserts

**Location:** subject lines 25-26, the clause *"which `rsclib/document_harness` already treats as
one frozen object."* **Ground truth it violates:**
`ResearchSystem/tooling/rsclib/document_harness/`.

**The pack is fourteen files; the module's one object is ten of them.**

```
$ python - <<'PY'   (glob of the pack vs. SCHEMA_FILES parsed from __init__.py)
files on disk              : 14
SCHEMA_FILES (pack_digests): 10
in pack, NOT in that object: ['assurance.schema.json', 'harness-issue.schema.json',
                              'review.schema.json', 'review.v2.schema.json']
PY
```

`pack_digests()` (`__init__.py:237-250`) is the only thing in the module that makes the pack *one*
object: it digests `SCHEMA_FILES` per file and folds them into a single `schema_pack_digest`. Its
own docstring calls that *"the exact schema pack."* It is ten files. The harness's own record says
so in as many words — `W1/W1-record.md:100`: *"**`pack_digests()` output changes** — the schema-pack
digest now covers ten files."*

**The remaining four are not unbound; they sit in two further hand-maintained lists.**
`review.py:85` `N2_SCHEMA_FILES` registers `review` / `assurance` / `harness-issue` into a
*separate* registry (`_n2_registry`, line 98), and `review_subject.py:69` `W2_SCHEMA_FILES`
registers `review.v2` alone. Three lists in three modules, no shared structure, and no directory
enumeration anywhere in the module:

```
$ git grep -rn "document-assurance-v3" -- '*.py' | grep -iE "glob|iterdir|listdir|rglob"
(no output)
```

**The tests refuse the direction A-2 asserts, on purpose.**
`tests/document_harness/test_candidate_checks.py::test_r3_every_v3_schema_present_is_clean_under_the_extended_scan`
is the one place a `SCHEMA_DIR.glob` meets `SCHEMA_FILES`, and it asserts
`set(SCHEMA_FILES.values()) - present == []` — registered ⊆ directory — with the docstring
explaining why it is not equality: *"That is now a subset assertion, **which a later node cannot
trip by adding a file**."* A pack file that no list registers is an anticipated, permitted state.
The only instrument that treats the directory as a whole is
`test_readme_enumeration.py`, which globs it to check README coverage — a different path from
`rsclib/document_harness`, and a navigation guard, not a freeze.

**Why this is not merely imprecise.** A-2 is the stated ground for choosing directory scope over a
named list, and it is new text this amendment introduced. Two things follow from believing it:

1. *The ruling's basis.* The ledger records the choice as *"两者都 `ls` 可判，**与代码对上**"* — that
   the new scope matches the code. It does not: the code binds ten as one object and lets the
   directory hold files no list knows. This is the same shape as read `f9a6600`'s `M-2`, which the
   user chose to correct while keeping the ruling.
2. *Evidence binding.* `schema_pack_digest` is what a later reader uses to prove which interface
   version produced recorded evidence, and it is a required field in the v2 lineage's
   `receipt.schema.json:131` and `resolved-stage.schema.json:33`. A reader who takes A-2 at face
   value treats that digest as covering the frozen object; it misses four of the fourteen. R9
   excludes evidence binding from wording-level, which is why this is not banked. The honest bound:
   `W1-record.md:100` also records that it is *"a generated binding, not signed material; no test
   pins its value"* — so nothing gates on it today, and the exposure is latent rather than live.

**The operative rule is unaffected.** *"Every existing file in the `schema/document-assurance-v3/`
pack"* is decidable by `ls` whatever the module does, and A-1 genuinely closes read `f9a6600`'s
`M-1` — the asymmetry between `common.schema.json` and `review.schema.json` is gone because both
are now inside. The defect is one clause of justification attached to a sound rule.

**Minimum fix — subtractive, one clause, no machinery (E6).** Delete *"which
`rsclib/document_harness` already treats as one frozen object"*; A-3's *"decidable by inspection"*
already carries the whole weight the rule needs. If a ground is wanted, state the accurate one —
the module registers the pack across three named lists and digests ten of them, and the directory
is authoritative here precisely because no single code structure enumerates it.

---

## 4. Low

### L-1 — *"every **existing** file"* has no as-of point, and the pack's history is one of files being added

A-1's *existing* is unanchored. Read at authoring time it means the fourteen present now; read at
use time it means whatever is present then, in which case a schema added next week is frozen the
moment it lands and cannot be corrected in-boundary. The commit states the first reading —
*"写「现有」故新增 schema 不受阻"* — but the text does not, and *addable* and *editable-after-adding*
are different questions the sentence collapses.

The pack has grown by seven since N0 (`9237960` held seven, `HEAD` holds fourteen), so this is not
hypothetical. Established practice already answers it in the strict direction: `document-work-spec.v2`
and `review.v2` exist because their v1 predecessors were not edited, and
`tests/document_harness/test_workspec_v2.py:3` records the rule — *"The N0-signed v1 schema is never
modified; `document-work-spec.v2.schema.json` supersedes it."*

**The downstream decision:** whether a schema added after this amendment may be edited in-boundary
or owes `SPEC_GAP`. **Not raised to must-fix:** both readings fail safe, the strict one matches
observed practice, and the fix is one clause either way. Not wording-level under R9 — the text is
silent, so the accurate fact is not recoverable from it.

### Banked under R9 — the two paths in A-1 and A-2 do not resolve from where they are written

`schema/document-assurance-v3/` is `ResearchSystem/schema/document-assurance-v3/`, and
`rsclib/document_harness` is `ResearchSystem/tooling/rsclib/document_harness/` — two levels off.
The subject sits in `ResearchSystem/document-harness/`, and its own convention elsewhere is either
self-relative with `../` (the header's `../migration/document-work-assurance-v3/…`) or written with
the full prefix (the pre-chain `E2`'s `ResearchSystem/contract/`). Under the file's own convention
`schema/document-assurance-v3/` resolves to a directory that does not exist.

**Wording-level under R9 and banked:** each string matches exactly one directory in the tree, so a
single `ls-tree` recovers it, and no actor's action changes once it is recovered. The decision that
would go wrong without recovery is real and is the same shape that cost the last turn — a reader
resolving the path locally finds nothing and concludes the item is empty — but it does not survive
recovery. It rides the next batch touching this layer and spawns no round and no read. Recorded
here so the next batch has it, not raised.

---

## 5. Observations

**O-a — `HEAD` moved mid-read; the subject did not.** `11d147e` → `f854b72` between my first and
second command groups. The new commit is ledger-only and is a ruling, not a round, so §2's
conclusion is unaffected — but a read that quoted `HEAD` once at the start would have mis-stated it.
Recorded as a fact about this session, not as a finding against the executor.

**O-b — what the amendment got right, re-derived rather than accepted.** A-1 closes read
`f9a6600`'s `M-1` on its own terms: `common.schema.json` and `review.schema.json` now get the same
answer from `E2`, and it is *frozen*, which is the safe one. A-4 quietly does more than the commit
claims — it deletes *"are frozen by their own tracks, not here"*, which was exactly the false
comfort read `f9a6600`'s `L-1` named; the commit describes that finding as still banked, which is
right about the residual fact (nothing was found freezing those instruments) but understates that
the misleading sentence itself is gone. The `M-2` correction is factually right where I could check
it — `validate.py:1047` names `Stage-Control-Contract.md`, `:1059` is the `read_text` inside
`generic_core_errors`, and the honest bounds I supplied travelled into the ledger verbatim (one
token class, not a freeze, not wired into the five suites). *"另两份确无活代码读者"* holds: the only
`.py` mention of `ResearchSystem-Contract.md` outside shadow artifacts and tests is a docstring line
(`rsclib/__init__.py:10`), and `a1-p4-scoped.md` appears only under `assurance/shadow/**`.

**O-c — the ledger correction both struck the false words and appended a note; nothing was lost.**
Read `f9a6600`'s `M-2` asked for an append, never a rewrite. `11d147e` did both: it removed *"均无活
代码读者"* from the original ruling line and appended a `⚠ 事实更正` block that quotes the removed
words verbatim and names the commit body that also carries them. So the earlier state is recoverable
in place. I could find no rule making the live ledger append-only — source rule 6 at `7011916`
scopes that to an N-record's log section, `E10` does not list the ledger in the instruction layer,
and the project's own navigation calls the file a live pointer with history in the archive. Reported
because my own minimum fix asked for something narrower than what was done, not because what was
done is wrong.

**O-d — `pack_digests()`'s docstring makes the same overclaim one layer down.** It calls its output
*"Content digests binding … the exact schema pack"* while covering ten of fourteen. That is the
sentence A-2 inherited, and it is code prose adjacent to my subject rather than in it. Reported, not
raised; `W1-record.md:100` already states the true count, so the record is not silent.

**O-e — nothing reconciles the three code-side lists against the directory, and that is by
design.** `SCHEMA_FILES` ∪ `N2_SCHEMA_FILES` ∪ `W2_SCHEMA_FILES` happens to equal the fourteen
today; the only assertion in either direction is the deliberate subset check quoted in M-1, and
`test_readme_enumeration.py`'s own docstring records what the missing direction cost once —
*"the directory held 14 schema files, the README table enumerated 13, and no instrument noticed."*
This amendment moves the instruction layer onto the directory, which is the drift-resistant side;
the drift risk now sits entirely in the three hand-maintained lists. Reported as shape under R5 —
whether that wants an instrument is the user's question, and E6 is the reason I am not proposing
one.

**O-f — the E3 pattern the `25f2916` ruling declined to mechanize recurs here.** *"Suites re-run
immediately before this commit: 151, 325, 39, 20, 29, all green, repo-audit exit 0"* is five counts
and an exit code, described rather than emitted. The user ruled option A on exactly this (no new
rule; the clause already exists in `E3`), so this is one line of recurrence data for them, not a
re-litigation. This amendment touches two markdown files and no code, so the figures bear on
nothing in the subject and I have not banked them.

---

## 6. Disclosure (R4)

**Read in full:** the subject (`CONSTRUCTION-CHECKLIST.md`, 122 lines) — both my standing
instruction and my subject, since `v3-harness-review-contract.md` is a 6-line stub redirecting to
it; the amendment diff `f9a6600..dcced4e`; the commit body of `11d147e` and its complete
`HARNESS-LEDGER.md` hunk; `f854b72`'s ledger hunk; my own prior record
`v3-checkpoint-read-f9a6600.md`, to check what it asked for against what was done;
`rsclib/document_harness/__init__.py` lines 14-24, 39-63 and 185-250; `review.py` lines 79-99;
`review_subject.py` lines 69-71; `test_readme_enumeration.py` lines 1-45;
`test_candidate_checks.py` lines 1670-1700; `validate.py` lines 1045-1063.

**Sampled:** `W1/W1-record.md` lines 98-104 only; `HARNESS-LEDGER.md` lines 133-192 rather than the
whole file; `N0/N0-record.md` not re-opened this session — where §3 refers to N0's seven, I am
relying on the glob of `9237960`'s tree, which I ran, not on the record's wording, which I quoted
last read.

**Probed only:** the search for a directory enumeration over the pack — a repo-wide `.py` grep for
`glob|iterdir|listdir|rglob` against the pack path, plus a grep for `SCHEMA_FILES` under the test
tree, which returned two files, both opened. Absence found by grep is weak evidence of absence, not
proof. The `schema_pack_digest` consumers were established by grep across `.py`, `.json` and `.md`;
I did not trace whether any live run currently writes one.

**Not verified.** The commit's five suite counts and `repo-audit exit 0`: not re-run (O-f). The
`python` set-difference in §3 was computed from the worktree, whose bytes on this Windows checkout
are not guaranteed to be the blob bytes — for filenames that is immaterial, and the fourteen-file
listing is independently confirmed by `git ls-tree -r --name-only HEAD` in §1's window work.

**Marked, not verified (R4):** that this session is fresh context — a process claim, marked as such.
That the two rulings recorded at `11d147e` (whole-directory form; keep the ruling, correct the fact)
were put to and answered by the user; I can see the record, not the exchange, which is R7's ceiling
and not a block.

**`UNVERIFIABLE`:** whether the four pack files outside `pack_digests()` *should* be inside it —
M-1 reports that `E2` describes the module as binding them when it does not, not that the module is
wrong to bind ten. Whether *existing* in A-1 was meant to freeze future additions: the text does not
say, the commit says one thing about a neighbouring question, and L-1 is written so its evidence
holds either way.
