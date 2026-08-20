# Checkpoint read — the `E10` amendment at `bba6f94`

`E10` read, and specifically the **re-read half of a must-fix pair**: the amendment at `bba6f94`
answers `v3-cold-read-17ce3ed.md`'s `M-1`, and `E10` fixes this read's subject as *"the amendment
text itself, never the work it governs"*. Not a round (`R3`): no verdict, no budget spent, output
is findings tiered must-fix / low / observation. Routing is `E10` / `R9` / `R10`'s, not mine.

**Findings: 0 must-fix, 0 low, 2 observations.** The amendment is the finding's supplied bytes
**byte-for-byte** — the five replacement lines and the five landed lines hash to the same sha256
(§3.1) — and it changes nothing else in the repository (§3.2). The new text is true where the old
was false: from the caller's root the replaced token resolved nowhere, the directory the new text
names by holder exists and holds that run's sibling records (§3.3). It is internally consistent
with `REVIEW.md`'s own `:6-8` and `:44-46`, and it now matches the name-and-holder form
`EXECUTION.md:452` and `REVIEW.md:45` already use (§3.4). The defect class is gone, swept two
independent ways — the commit body's keyword grep, which reproduces exactly, and a resolver sweep
over the whole standing text of all ten members, which returns **zero** unresolved path tokens in
the seven non-frozen prose members (§3.5, §3.6). The fix stayed inside the must-fix channel: it
adds no clause and moves no actor's obligation, and independently `HD-36` ② holds the design test
out of that channel altogether (§3.7). The two observations are shape, not defect, and both are
recurrences of things already on the books.

**Named `checkpoint-read` rather than `cold-read`**: one of the ten members was read end to end at
this subject and one more was read in full for other reasons; the remaining eight are **covered by
citation**, which I verified rather than accepted (§2).

**Standing instructions read.** `document-harness/CONSTRUCTION-CHECKLIST.md` in full, both sides
(235 lines, blob `cacd99d4`). `HARNESS-DECISIONS.md` read by section per `E10`'s tail clause —
`HD-49` (the ground truth `M-1` names), `HD-41` (the sweep-trace discipline the commit body
invokes), `HD-36` (the must-fix channel and the design-test narrowing) from `§live`, and `HD-38`
(free-channel bytes carry their own commit) from `§implemented`, because claims I checked cite it.
Cited by section, never by blob, exactly as that clause requires.

---

## 1. Subject, re-derived

```
$ git rev-parse --show-toplevel
D:/Thesis-stage-control-refactor/ResearchSystem/harness

$ git rev-parse HEAD
bba6f942a4b71906d28923091a3bc436c7d72cb6

$ git rev-parse --abbrev-ref HEAD
main

$ git status --porcelain
(no output)

$ cat .harness/review-pending.json
cat: .harness/review-pending.json: No such file or directory
```

Subject = branch tip, confirmed rather than accepted from the dispatch; worktree clean. **There is
no dispatch freeze marker**, so `E9`'s window has no mechanical carrier for this read either —
the same condition the cited read recorded as its `O-2`, unchanged one commit later. Nothing here
depends on the marker; it is disclosed because its absence is the reason the window is
reconstructed from the log below rather than read off a file.

**What stands between the cited read and this subject** — the range this read is paying for:

```
$ git log --oneline 17ce3ed..bba6f94
bba6f94 V3-INIT-SURFACE-AMEND-M1-v1
32f24b8 V3-REVIEW-RECORD-INIT-SURFACE-17ce3ed-v1

$ git show --stat 32f24b8
 .../v3-cold-read-17ce3ed.md    | 524 +++++++++++++++++++++
 1 file changed, 524 insertions(+)

$ git diff --stat 17ce3ed bba6f94 -- <the ten members>
 document-harness/REVIEW.md | 8 +++++---
 1 file changed, 5 insertions(+), 3 deletions(-)
```

Two commits. The first is the cited read's own record and touches nothing but that record —
`E9`'s *"from dispatch to that commit the branch takes no commit but the record itself"* holds.
The second is the amendment, which is the pair `E10` opens and not a round commit. Timestamps put
the record at `22:51:29` and the amendment at `22:52:39`, so the read's record landed **before**
the amendment, in the order `E10` requires.

One member site changed in the range, and it is this read's whole subject.

## 2. The member set, and each member's blob

The set is `E10`'s own enumeration read at the subject (`CONSTRUCTION-CHECKLIST.md:94-105`),
which reads *"exactly these ten paths and nothing else"*; nothing was taken from the dispatch.
`E10` makes citation depend on these ids, so each is stated.

| # | member | blob at `bba6f94` | vs `17ce3ed` | how covered |
|---|---|---|---|---|
| 1 | `document-harness/CONSTRUCTION-CHECKLIST.md` | `cacd99d49d80ce4bf33e94b733a07f1dd6b247e8` | unchanged | **read in full** (235 lines) — citation was available and is not claimed |
| 2 | `document-harness/README.md` | `3a49e0328cbd6e0bc36b331d43f32f33f8bf36ab` | unchanged | covered by citation + sweep probes |
| 3 | `document-harness/EXECUTION.md` | `0d0c617ba09c8e37013545776bc517c54dede439` | unchanged | covered by citation + targeted read (`:448-456`) + sweep probes |
| 4 | `document-harness/REVIEW.md` | `4cae5ce76d84571f1bf92ab89001f3e8f2c98ae3` | **changed** (`bba6f94`) | **the subject** — read at `:1-70` and `:110-164`, plus whole-file sweeps |
| 5 | `document-harness/ORCHESTRATION.md` | `80f42658a2961eeb10a168bd7bd729121c6c05ae` | unchanged | covered by citation + sweep probes |
| 6 | `…/v3-harness-operating-contract.md` | `6d5714923870b4e13e8928221a80df68e563a5ed` | unchanged | covered by citation + sweep probes |
| 7 | `…/v3-harness-review-contract.md` | `29bdc9fbde6e8db38d601dd2340d4b46a24a296f` | unchanged | covered by citation + sweep probes |
| 8 | `contract/…-supersession-1.md` | `68031fa2ca31272e31da0d42a9a02189d28fcc21` | unchanged | covered by citation + resolver sweep |
| 9 | `contract/…-supersession-2.md` | `e1a2f26b1d8d323d11e900f8137dea222b6571c1` | unchanged | covered by citation + resolver sweep |
| 10 | `schema/…/paragraph-map.schema.json` | `09aa869962f592c2f86c9379be0ef3eb7d2232ff` | unchanged | covered by citation + resolver sweep |

**Citation checked, not accepted.** `v3-cold-read-17ce3ed.md` §2 records blob ids for all ten
members and states that members 1–7 were **read end to end** at those blobs, members 8–10 covered
by a verified citation onward to `v3-cold-read-4410899.md`. Nine of the ten ids in that table are
byte-identical to the ids above; the tenth is member 4, the subject. `E10`'s condition — *"a
member whose blob is unchanged since a recorded end-to-end read of it is covered by citing that
record"* — is therefore met for members 2, 3, 5, 6 and 7 directly, and for 8–10 through the chain
that read already verified. The `git diff --stat` in §1 is the same fact from the other direction.

Member 4's working-tree bytes were proven equal to the subject blob before anything was quoted
from them:

```
$ git hash-object document-harness/REVIEW.md
4cae5ce76d84571f1bf92ab89001f3e8f2c98ae3      → MATCH
```

**`E2`'s frozen surface is untouched.** The amendment's one path is `document-harness/REVIEW.md`,
which is none of `E2`'s three blobs (`b2dbdf75…`, `68031fa2…`, `e1a2f26b…`) and is not in the
`schema/document-assurance-v3/` pack. Members 8, 9 and 10 — the frozen ones present in this layer
— carry the same blobs as at `17ce3ed`. No `E2` ruling is owed by this amendment, and `HD-20`'s
banking rule is not engaged.

**Not a member, read by section:** `HARNESS-DECISIONS.md`, per `E10`'s tail clause. It is not in
the table and is cited by section, never by blob.

## 3. The amendment, checked

Scope declaration (`HD-41` ①): every enumeration in this section is over the **ten member blobs at
`bba6f94`** unless a narrower scope is stated on the line itself.

### 3.1 The bytes are the bytes the finding supplied

`M-1`'s *Minimum fix* supplies a five-line replacement at `v3-cold-read-17ce3ed.md:410-414`. The
amendment lands five lines at `document-harness/REVIEW.md:134-138`. Rather than compare them by
eye, both slices were extracted to files and hashed:

```
$ sed -n '410,414p' migration/document-work-assurance-v3/v3-cold-read-17ce3ed.md > supplied.txt
$ sha256sum supplied.txt
8dcd01b818d27955d013c84695480745ca558283403810ed434bdba5e9c0f616

$ sed -n '134,138p' document-harness/REVIEW.md > landed.txt
$ sha256sum landed.txt
8dcd01b818d27955d013c84695480745ca558283403810ed434bdba5e9c0f616
```

**Identical.** The amendment is the literal replacement the finding names — `E10`'s must-fix
channel admits exactly this — with no executor paraphrase, no re-typing "with the same content",
and no drift in the placeholder spelling.

Because an equality test cannot detect a defect the two sides *share*, the landed bytes were also
checked as bytes rather than as a terminal rendering (`REVIEW.md:147-151`'s own read discipline):

```
$ python -c "... REVIEW.md read_bytes().decode('utf-8') ..."
line134 codepoints of dash: ['0x2014']
file decodes as UTF-8: OK, bytes= 18165
```

The dash is a real U+2014 and the file is well-formed UTF-8, so the sha256 equality is equality of
correct bytes, not of shared mojibake. (The console rendering of that dash is mangled in this
session's terminal — which is precisely why the claim rests on `read_bytes()` and not on what the
console printed.)

### 3.2 Nothing else changed

```
$ git diff-tree -r --numstat bba6f94^ bba6f94
5	3	document-harness/REVIEW.md

$ git diff --stat bba6f94^ bba6f94 -- . ':!document-harness/REVIEW.md'
(no output)
```

One file, five insertions, three deletions, and the exclusion pathspec confirms the rest of the
repository is untouched. In particular the amendment carries **no free-channel byte**: the cited
read's `L-1` supplies bytes for `EXECUTION.md:194`, and `EXECUTION.md` is not in this diff. That
is correct twice over — `HD-38` rules that free-channel bytes take their own commit and do not
ride the amendment, and `R10`'s sentence (*"an `E10` amendment commit admits only the answers to a
read's must-fix findings"*) is the carrier `HD-38` chose to leave standing.

### 3.3 The new text is true

The replaced text located a caller-held artifact with a repository path token. Both halves of
`M-1`'s measurement were re-run here, at this tree:

```
$ ls -d D:/Thesis-stage-control-refactor/migration
ls: cannot access 'D:/Thesis-stage-control-refactor/migration': No such file or directory

$ ls -d D:/Thesis-stage-control-refactor/ResearchSystem/migration/document-work-assurance-v3
D:/Thesis-stage-control-refactor/ResearchSystem/migration/document-work-assurance-v3

$ ls …/ResearchSystem/migration/document-work-assurance-v3/ | grep -c '^v3-review-full'
17
$ ls …/ResearchSystem/migration/document-work-assurance-v3/v3-review-full-fef3a2e.md
…/ResearchSystem/migration/document-work-assurance-v3/v3-review-full-fef3a2e.md
```

The old token resolved **nowhere** from the caller's root, as the finding said. The directory the
new text names by holder — *"the caller's own document-work-assurance-v3 migration directory"* —
exists, and the clause *"beside that run's other records"* is true of it in the strong sense: it
holds seventeen `v3-review-full-*.md` records including `fef3a2e`, the very one `REVIEW.md:45`
names, alongside the runs' activation and signature records (`a1-p4-…`, `a2-p5a-…`, `a3-p5b-…`).
A reviewer told to write beside that run's other records has somewhere to land.

The sentence *"The caller holds it; this layer does not write its path"* is true of the layer as
amended: after the change, no member writes a path token for the product-run review record (§3.5),
and the one remaining `migration/document-work-assurance-v3` line in `REVIEW.md` is `:66`, a
W2-record citation that resolves in this repository.

The premise the fix's sufficiency rests on — that these bytes are the whole of the instruction —
was re-derived rather than accepted from the finding:

```
$ grep -n "ROLE_INSTRUCTION\|v3-review\|review record\|migration/" tooling/rsclib/document_harness/dispatch.py
426:ROLE_INSTRUCTION = "document-harness/REVIEW.md"
545:CONSTRUCTION_ROLE_INSTRUCTION = (
546:    "migration/document-work-assurance-v3/v3-harness-review-contract.md"
… (charter constants only; no v3-review record path anywhere)
```

The dispatcher names the charter and no record path, so nothing outside `REVIEW.md` tells a
product-run reviewer where the record goes. The bytes carry the whole instruction, and correcting
them corrects the whole instruction.

### 3.4 Internal consistency with the member's other clauses

Swept across the five prose members for every clause that could disagree:

```
$ grep -n "v3-review\|review record\|review-full.json\|review-verify.json" <the five document-harness members>
CONSTRUCTION-CHECKLIST.md:228:- **R6** Record channel: you write `v3-review-{full,verify}-<subject-sha>.md` (or
EXECUTION.md:452:  here: the FULL record `v3-review-full-86defbc.md` f1–f2, and audit rounds 4 o1–o2 and
REVIEW.md:45:`v3-review-full-fef3a2e.md`, which is held with that run's records in the caller that grew
REVIEW.md:132:   names, written to `<control root>/evidence/review-full.json` (a round-1 targeted VERIFY:
REVIEW.md:133:   `review-verify.json`), bound to the dispatched subject.
REVIEW.md:134:2. **The review record** — the prose record of what you read, re-executed and found: a file
REVIEW.md:135:   named `v3-review-<round>-<subject short SHA>.md` (`<round>` = `full` | `verify`; repo
```

- **`REVIEW.md:6-8`** scopes the whole file to a product run and disclaims the construction-side
  contract. The amended item is now consistent with that scope instead of contradicting it.
- **`REVIEW.md:44-46`** already said a product-run FULL record *"is held with that run's records in
  the caller that grew this harness rather than here"*. The amendment makes `:134-138` say the same
  thing about the same class of artifact. The ninety-line self-contradiction `M-1` named is gone.
- **`REVIEW.md:132-133`**, item 1 of the same list, locates the ReviewResult at
  `<control root>/evidence/review-full.json` — placeholder-rooted, so it names its holder rather
  than writing a repository path. After the amendment **both** items of the deliverables list are
  in the holder-named form; item 2 no longer sits oddly beside item 1.
- **`EXECUTION.md:452`** and **`REVIEW.md:45`** are the two precedents the commit body claims the
  new form matches. Read at the subject, both are backticked filename plus prose holder (*"held in
  the caller that grew this harness rather than here"*). The claim holds; the new text is slightly
  more specific, naming the directory in prose, which is still no path token.
- **`CONSTRUCTION-CHECKLIST.md:228`** (`R6`) does write `migration/document-work-assurance-v3/` for
  review records — but for the **construction** side, whose records genuinely live in this
  repository (this file is one), and that token resolves here. Different audience, different
  holder, no conflict; `HD-49`'s (a)/(b) split is exactly this line. See `O-1` for the one reading
  risk this pairing leaves.

### 3.5 Free of the defect class — swept two independent ways

`E10` names the class as a caller-held artifact written as a path token, and `E7` requires testing
the class rather than the instance. Two sweeps with different blind spots were run.

**(a) The resolver sweep** — `layer_path_check.py`'s own `unresolved_tokens` applied to the
**whole standing text** of all ten members at the subject (not just added lines):

```
document-harness/CONSTRUCTION-CHECKLIST.md: 0 unresolved path token(s)
document-harness/README.md: 0
document-harness/EXECUTION.md: 0
document-harness/REVIEW.md: 0
document-harness/ORCHESTRATION.md: 0
migration/…/v3-harness-operating-contract.md: 0
migration/…/v3-harness-review-contract.md: 0
contract/…-supersession-1.md: 2   `ResearchSystem/migration/…/W2/W2-design.md`, `…/W2-record.md`
contract/…-supersession-2.md: 3   `assurance/runs/`, `templates/run-v2/`, `ResearchSystem/migration/…/`
schema/…/paragraph-map.schema.json: 0
TOTAL: 5
```

All five sit in the two supersessions, which `E10` excepts *"while they are frozen"* — the same
five sites the cited read recorded as its `O-3`. The seven non-frozen prose members carry **zero**.

**(b) The guard's actual reach at this site, tested rather than assumed.** The same module was run
against the amendment's added lines and, as a control, its removed lines:

```
=== ADDED lines (5) ===
TOKEN regex matches in ADDED: ['<round>', 'full', 'verify']
guard verdict on ADDED: CLEAN (no finding)

=== REMOVED lines (3) ===
TOKEN regex matches in REMOVED: ['<round>', 'full', 'verify']
guard verdict on REMOVED: CLEAN (no finding)
```

The negative control is the informative half: **the guard was blind to the original defect too**.
Its `TOKEN` regex admits no whitespace inside backticks, and the old token was both
placeholder-bearing and split across two lines, so it never matched. The three tokens it does see
are identical on both sides and none contains a `/`. This is not a defect in the amendment — it is
`E10`'s stated division (*"What the guard still cannot see is held by this clause alone"*) doing
its job — but it bounds sweep (a): a zero there proves no token of the shape the resolver can see,
not the absence of every possible sibling. Recorded as `O-2` and carried into §5's ceilings.

**Scope boundary.** Sweep (a) cannot see the *wrong-tree* variant — a token that resolves here but
denotes a caller thing. That is `L-1`'s shape at `EXECUTION.md:194`, which the cited read tiered
low and banked under `R9` on an explicit test, and which `HD-38` in any case bars from this
commit. It is a different defect from the one `M-1` names (`M-1` misdirects an action; `L-1`
misattributes an anecdote), so its remaining in place is not an unswept sibling of this amendment.

### 3.6 The commit body's falsifiable claims, re-run (`E3`, `HD-41` ④)

The commit body states a class sweep. Re-run verbatim at the amendment tree:

```
$ grep -c "migration/document-work-assurance-v3" <the seven prose members>
document-harness/CONSTRUCTION-CHECKLIST.md:5
document-harness/README.md:8
document-harness/EXECUTION.md:1
document-harness/REVIEW.md:1
document-harness/ORCHESTRATION.md:0
migration/…/v3-harness-operating-contract.md:1
migration/…/v3-harness-review-contract.md:1
```

`5 · 8 · 1 · 1 · 0 · 1 · 1` = **17**, matching the commit body digit for digit, and matching the
cited read's pre-amendment `18` less the one line the amendment removed. The claim that the
seventeen remainders are construction-side or instrument-internal was **inspected, not accepted**:

- `CONSTRUCTION-CHECKLIST.md:4,23` — header citations, relative `../migration/…`, resolve here;
  `:100,101` — `E10`'s own membership enumeration; `:230` — `R6`'s construction record channel.
- `README.md:17,18,19,21,28,33,34,35` — markdown links to N0/N1/N2/W2 records, journals and
  fixtures, all `../migration/…`, all resolving here (sweep (a) returns 0 for this member).
- `EXECUTION.md:109` and `REVIEW.md:66` — the same W2-record citation, resolving here.
- the two stubs — `git show 7011916:ResearchSystem/migration/…` source-repo paths inside a commit
  citation, which `E10`'s *"Where a cited commit id resolves"* clause covers as written.

None is product-run-audience. `REVIEW.md:135` was the whole of that class, as the finding said and
the commit body claims, and the amendment closed it.

The commit body's other checkable assertions also hold: the commit is titled
`V3-INIT-SURFACE-AMEND-M1-v1`, one dense paragraph, no trailers, and names its kind
(*"Amendment commit (kind: amendment)"*) — `E8` satisfied; and its closing promise that *"the
re-read of the amended text is dispatched immediately after this commit and its record lands next
on this branch"* is what this record discharges.

### 3.7 Did the fix stay inside the must-fix channel?

This is the one question the finding explicitly refused to answer (*"whether the fix reads as
changing what the deliverables rule requires … is the orchestrator's call"*), so it is checked
here on its own merits rather than inherited.

**What the deliverables rule requires, before and after.** The trigger (*"A review is not returned
until it is committed"*), the count (*"exactly two artifacts"*), the actor (the dispatched
reviewer), the artifact's kind, and its filename convention are **all unchanged**. What changed is
the statement of where it lands — from a token that named this repository to a name plus a holder.
No check outcome, evidence binding, permission, obligation or verdict path moves. An obligation
that was unsatisfiable as written becoming satisfiable is a correction of text that `E10`'s
caller-held-path clause, `HD-49` and `REVIEW.md`'s own `:6-8` / `:44-46` already falsified — which
is what `E6`'s *"When a finding names existing text or code as wrong, the fix is that text
changing"* describes.

**The one sentence that could read as added.** *"The caller holds it; this layer does not write its
path."* is new prose with no predecessor in the removed lines. It adds no bound: `E10` already
imposes exactly this on every member (*"a caller-held path is named, never written as a path
token"*), and `HD-49` already assigns product-run records to the caller. It is a local echo of a
global rule applied to one artifact, not a new requirement on any actor — and it is in any case
inside the bytes the finding supplied, which `E10`'s must-fix channel admits literally.

**And independently, the design test does not reach here.** `HD-36` ② (`§live`, and `§live`
outranks the checklist on conflict) rules that `E10`'s priority sentence was narrowed to *"the
bytes the finding supplies"* precisely to hold the design test **back inside the free channel** and
out of the must-fix channel. `E10`'s own collision sentence is scoped to match — *"when the **free
channel** and the design test both apply … design wins and the round opens"*. So even a reader who
judged the added sentence a clause would not thereby open a round for a must-fix answer.

The routing is correct on both grounds. That it takes a reading outside the layer to be sure of
the second is `O-1`.

## 4. Findings

**0 must-fix. 0 low. 2 observations.** Neither observation names a defect in the amendment; both
are shape, and both are recurrences (`R5`: the question and the conclusion are the user's).

### `O-1` (observation) — this pair's routing is only reproducible by reading `HD-36` ② outside the layer

`E10`'s design test is written without limitation — *"an amendment adding a clause to any rule, or
replacing or deleting text so that what a rule requires changes, is design and opens a round"* —
and the exemption that keeps it out of the must-fix channel exists **only** in `HD-36` ②.
`HARNESS-DECISIONS.md` says so itself in `HD-36`'s status note: *「`E10` 的通用 design test 仍无限定地
盖住每一个 amendment，豁免只由本条承载」*, and holds the entry at `live` pending *「一个设计轮给那句加限定」*.

What is new here is not the gap but its first live exercise. Previous filings
(`v3-checkpoint-read-136f27f.md` / `-f61ce2c.md` `O-1`) reported it abstractly; this is the first
must-fix pair where the routing question was actually contested — the cold read declined to decide
it and handed it to the orchestrator, and the orchestrator's commit body had to argue it in prose.
A later auditor reading the layer alone cannot reproduce that decision.

Related and smaller: `CONSTRUCTION-CHECKLIST.md:228` (`R6`) writes
`migration/document-work-assurance-v3/` for construction-side review records while the amended
`REVIEW.md:137-138` says *"this layer does not write its path"* of the product-run one. The two are
consistent under `HD-49`'s (a)/(b) split and `REVIEW.md:6-8` pre-empts the mis-read for anyone
reading `REVIEW.md` as their charter, so no downstream decision goes wrong. Noted because it is the
only place in the amended text where the sentence's scope depends on the reader having the
file-level framing in hand.

**No action implied.** Whether the design test should carry a limiting clause is a design round's
question and already has a home in `HD-36`'s status note.

### `O-2` (observation) — nothing mechanical binds this site, in either direction

Measured, not inferred (§3.5b): `layer_path_check.py` returns CLEAN on the amendment's added lines
**and on its removed lines**. The guard never caught the defect `M-1` reported and would not catch
its return — the token was placeholder-bearing and line-split, two shapes `E10` names as outside
the guard's reach.

The consequence worth recording is about evidence, not about the fix: my §3.5a sweep uses that same
resolver, so its zero is a zero over the shapes the resolver can see. The correction rests on the
`E10` clause plus reviewer attention, and a regression at this site would have to be caught the
same way. `E10` already says this is the clause's territory and the guard's docstring says the same
(*"One class is flagged now, and nothing else"*), so this is confirmation of a known division, not
a new finding against it — and `HD-50` R4 already carries the guard-division question in rider
`guard-division-home`.

## 5. Coverage, and the ceilings on it (`R4`)

**Read in full:** `document-harness/CONSTRUCTION-CHECKLIST.md` (235 lines, blob `cacd99d4`) —
both sides, `E1`–`E12` and `R1`–`R10` plus the header. `tooling/hooks/layer_path_check.py`
(135 lines), read in full because §3.5 runs its internals rather than the hook.

**Read to settle a specific claim, not in full:** `document-harness/REVIEW.md` — `:1-70` (the
opening, `:6-8`, and `:44-46`) and `:110-164` (the whole *Where the result lives — deliverables*
section with its stage marker and the read-discipline paragraph that follows), roughly 125 of its
287 lines; the remainder was covered only by the whole-file sweeps of §3.4 and §3.5.
`v3-cold-read-17ce3ed.md` — §2 (`:62-116`), `M-1` and `L-1` in full (`:327-456`), `O-1`
(`:458-466`), and a heading map of the rest; not its 524 lines entire.
`HARNESS-DECISIONS.md` — `HD-49`, `HD-41`, `HD-36`, `HD-38` and the `§live` heading, by section as
`E10` requires; the file was not read whole and no blob is claimed for it.
`document-harness/EXECUTION.md:448-456`, to check the `:452` precedent.
`v3-checkpoint-read-48b6c5f.md` — `:1-110` plus a heading map, consulted **for record structure
only**; nothing in this record's findings depends on it.

**Probed only (blob equality plus targeted grep / resolver sweep):** members 2, 3, 5, 6, 7, 8, 9
and 10 of §2's table, each proven byte-identical to the blob `v3-cold-read-17ce3ed.md` §2 records
as read end to end, then swept by §3.5a and §3.6. `tooling/rsclib/document_harness/dispatch.py` —
one targeted grep (§3.3); I did not read the module.

**Re-executed rather than accepted:** the `git rev-parse` / `status` / `log` / `diff-tree` /
`diff --stat` / `ls-tree` set of §1–§2; the sha256 comparison of §3.1; the UTF-8 and codepoint
check of §3.1; the caller-tree `ls` probes of §3.3; the seven-member `grep -c` class sweep of §3.6;
the ten-member resolver sweep of §3.5a; and the guard probe with its negative control of §3.5b.

**Ceilings, stated rather than folded into supported:**

1. **The class sweeps are two partial views, not a proof.** §3.5a sees only backticked tokens
   without whitespace or placeholders (`O-2`); §3.6 sees only lines containing one keyword string.
   Their union covers the shapes at issue here, but *"no other site of this class exists anywhere in
   the layer"* is **`UNVERIFIABLE`** by these means. What is verified is narrower and sufficient for
   this amendment: no product-run-audience site of the keyword remains, and no resolver-visible
   unresolved token remains outside the frozen bytes.
2. **`REVIEW.md` was not read end to end at this blob.** Consistency was checked by targeted read
   plus whole-file grep; a clause disagreeing with the amendment in wording that neither my greps
   nor my section reads touch would not have been seen.
3. **The caller-tree probes describe this machine.** *"The caller's own document-work-assurance-v3
   migration directory"* was confirmed to exist and hold sibling records **here**. That the phrase
   resolves for a different caller is a property of the form `E10` mandates, not something I
   measured, and it is why the form is a name and not a path.
4. **Freshness of context is a process claim, marked not verified** (`R4`). I derived the subject,
   the member set and every figure from the repository; I did not receive and do not rely on any
   reported figure from the executing side beyond the commit body, which §3.6 re-ran.
5. **No dispatch marker existed** (§1), so `E9`'s window for this read is reconstructed from commit
   order and timestamps rather than read off a file.

## 6. Already on the books, not re-filed

- The **guard's blindness to placeholder-bearing tokens** is stated in `E10` itself, in
  `layer_path_check.py`'s docstring, and in `v3-cold-read-4410899.md` `L-2`. `O-2` records the
  measured confirmation at this site and its effect on my own evidence; it does not re-file the gap.
- The **`E2`-frozen exception's five sites** are the cited read's `O-3`, reproduced unchanged in
  §3.5a. Not re-filed.
- **`HD-49` carrying `status: implemented` inside `§live`** is the cited read's `O-1`. Unchanged at
  this subject; not re-filed.
- **`L-1` (`EXECUTION.md:194`)** remains unapplied and is correctly absent from this commit
  (`HD-38`, `R10`). It is the cited read's to route, banked under `R9`; not re-filed here.
- The **absence of a dispatch marker** is the cited read's `O-2`; disclosed in §1 as a ceiling on
  this read rather than filed again.
