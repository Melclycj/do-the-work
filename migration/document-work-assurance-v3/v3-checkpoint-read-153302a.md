# Checkpoint read — the instruction layer at `153302a` (the `E10` re-read paired with the `M-1` amendment)

**No verdict.** A read is not a round (`R3`): it spends no budget, carries no verdict, and its
output is findings tiered must-fix / low / observation. Nothing below certifies any text, and
nothing below is banked as any round's FULL. This is the independent re-read `E10`'s must-fix
channel owes beside the amendment commit — *"a read's must-fix findings are answered by an
amendment commit plus an independent re-read of the amended text, and that pair is not a round
and spends no budget"* — so it is a checkpoint read, not the round-opening cold read
`v3-cold-read-21dad76.md` already was.

**Findings: 0 must-fix, 2 low (both carried forward, neither new), 2 observations (both new).**
The amendment is clean: `M-1`'s prescribed bytes were applied character-for-character, the class
is closed by the word over all nine members, and the commit touched one line and nothing else.
The two lows are `v3-cold-read-21dad76.md`'s `L-1` and `L-2`, **re-derived here independently
before that record's findings section was opened**, and both still standing at this subject —
re-reported so their open state is visible, explicitly **not** re-filed and **not** to be banked
twice. The two observations are new and belong to an `ORCHESTRATION.md` surface three rider rows
already occupy.

**The citation channel was available for eight of nine and was not taken.** Members 1, 2, 3, 4,
6, 7, 8 and 9 are byte-identical to the blobs `v3-cold-read-21dad76.md` §2 records reading end
to end; only member 5 changed, and that change is the amendment this read exists for. All nine
were read end to end anyway (1640 lines), because the amendment's own class claim spans the
layer and a citation cannot establish that a *deletion* elsewhere did not land.

**Standing instructions read.** `migration/document-work-assurance-v3/v3-harness-review-contract.md`
(the stub, member 7) → `document-harness/CONSTRUCTION-CHECKLIST.md` in full, both sides, per the
stub's *"It is your standing instruction and its own counterpart; read all of it."*
`HARNESS-DECISIONS.md` header (1–27) plus `§live` (28–162, **eight** entries — `HD-56`, `HD-44`,
`HD-41`, `HD-36`, `HD-35`, `HD-34`, `HD-23`, `HD-9`), which `E10`'s tail owes. Unchanged in
membership against the previous read's eight. `§implemented` and the archive were **not** read
end to end — probed for `HD-57` and `HD-55` in full and for the ids the members cite (§3.5).
Cited by section, never by blob (`HD-19`).

---

## 1. What the subject is, and how it was derived

The dispatch supplied one commit and nothing else (`R2`). Everything below was re-derived.

```
$ git rev-parse HEAD
912f837bfd717e17db3b1ecb559dcb6f73745b2d

$ git status --porcelain
(empty)

$ git log -1 --format='%H%n%ad%n%s' 153302a1546a3cad91dbc552cce9edc27c123629
153302a1546a3cad91dbc552cce9edc27c123629
Mon Aug 24 01:25:03 2026 +1000
V3-STRANGER-PROOF-M1-AMENDMENT-v1
```

**The subject is not HEAD.** `HEAD` is one commit later, and the difference was derived rather
than assumed:

```
$ git diff --stat 153302a HEAD
 HARNESS-RIDERS.md | 1 +
 1 file changed, 1 insertion(+)
```

`HARNESS-RIDERS.md` is not a member, so **the layer at the subject and the layer at HEAD are the
same bytes** — checked per member, 9/9, not inferred from the stat. That commit (`912f837`,
`V3-STRANGER-PROOF-RIDERS-BANK-v1`) banks the previous read's `L-2`; it is outside this read's
subject and is read here only as the round record it is, never relied on (`R2`).

**The subject commit touches exactly one member.**

```
$ git show --stat --format='' 153302a
 document-harness/ORCHESTRATION.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

$ git log --format='%h %s' 21dad76..153302a -- <the nine>
153302a V3-STRANGER-PROOF-M1-AMENDMENT-v1
```

**The review window is intact, re-derived rather than assumed** (`REVIEW.md` says to). The
gitignored marker `.harness/review-pending.json` names subject
`153302a1546a3cad91dbc552cce9edc27c123629`, dispatched `2026-08-23T15:25:34+00:00`. The subject
commit is `2026-08-23 15:25:03` UTC and `912f837` is `15:25:28` UTC — **six seconds before the
dispatch**, so the riders commit landed outside the window rather than inside it, and no commit
has landed since. `E9`'s window is unbroken. This repository's tracked hook runs
`layer_path_check.py` alone, so the window here is discipline, held, not enforcement — the
standing shape rider `self-caller-guards` already banks that.

**The dispatch was the generated form, not a hand-composed one.** The prompt received is
`dispatch.READ_PROMPT` with `{charter}` = member 7 and `{commit}` = the subject SHA, verbatim
including the *"a fact you were handed is a fact you did not check"* sentence. One SHA and no
member table: the anchoring failure `v3-cold-read-451e8b0.md` `M-1` paid for did not recur.

## 2. The member set and each member's blob

The set is `E10`'s own sentence — **"exactly these nine paths and nothing else"** — hand-
transcribed from the checklist at the subject blob, then machine-compared against the guard's
mirror (§3.3). Blob ids per `E10`'s *"a read's record states the blob id of each member it read,
because citation depends on it"*.

```
 #  blob                                      lines  path                                             vs v3-cold-read-21dad76
 1  c0e3e2dd8960a00f0074d98b9ff79b85dcfb933b    249  document-harness/CONSTRUCTION-CHECKLIST.md       same
 2  0454c8a59db88fa4c4b599bb7f6de39681489682     38  document-harness/README.md                       same
 3  b187af5c836781a366aeb3c9ef3a1338a9955de0    519  document-harness/EXECUTION.md                    same
 4  86e5ed7ad6792a7548ce968dea3cbcfcc3ee9f3e    319  document-harness/REVIEW.md                       same
 5  ae641325c2f880347f187e9003cc494077de9c1e    119  document-harness/ORCHESTRATION.md                CHANGED (was 9a67401f)
 6  6d5714923870b4e13e8928221a80df68e563a5ed      5  migration/…/v3-harness-operating-contract.md     same
 7  29bdc9fbde6e8db38d601dd2340d4b46a24a296f      5  migration/…/v3-harness-review-contract.md        same
 8  dfc983d2e3d9fb5ca67b053a16fcfb0e6715b11a    342  contract/Document-Work-Assurance-Contract-v4.md  same
 9  09aa869962f592c2f86c9379be0ef3eb7d2232ff     44  schema/…/paragraph-map.schema.json               same
                                              -----
                                               1640  total lines read
```

Member 8 is `E2`-frozen and a member at once — the `HD-20` intersection `HD-56` ② names. Its
bytes are unchanged at this subject, so `HD-20` is not engaged by anything here.
`HARNESS-DECISIONS.md` is **not** a member: `E10`'s tail owes it while denying it membership
(`HD-19`).

## 3. What was checked, and what the commands returned

### 3.1 The amendment against the bytes `M-1` prescribed

The carrier cell was extracted from the table row and compared to the finding's prescribed
replacement as decoded strings, not as a terminal rendering (`REVIEW.md`'s Windows read
discipline — the p4-doc `f1` mojibake lesson; a first attempt at this comparison died on GBK
console decoding, which is the same defect arriving as a crash instead of as a false finding):

```
row cells: 3
carrier cell : 'a full session, in the form `E1` requires — what decides independence is who set the question (`R1`)'
M-1 prescribed: 'a full session, in the form `E1` requires — what decides independence is who set the question (`R1`)'
IDENTICAL
```

The withdrawn permission (`**or** a subagent`) and the now-false `not the form` half are both
gone; `R1`'s holding survives as a pointer rather than a restatement, which is the narrow form
`HD-46` fixed for this file and what `HD-5` (transcription as a drift surface) asks for. It adds
no clause and changes what no rule requires, so the replacement is not itself design and the
must-fix channel was the right route (`R10`, `HD-36` ①). The path is not one `E2` freezes, so
`HD-20`'s bar does not apply.

### 3.2 The class, re-derived rather than inherited

`E7` asks for the defect class, not the reported instance, and the amendment's body reports a
five-site inventory **inherited from the read** rather than rediscovered. Re-run here over the
nine members' whole text at the subject:

```
$ for p in <the nine>; do git show 153302a:$p | grep -in "subagent\|sub-agent"; done
CONSTRUCTION-CHECKLIST.md:31  E1's opening — an executor-dispatched subagent is a self-check   unaffected
CONSTRUCTION-CHECKLIST.md:33  the amended E1 clause                                            standing, correct
CONSTRUCTION-CHECKLIST.md:35  the amended E1 clause                                            standing, correct
EXECUTION.md:336              "a subagent auditor is V3-D7-distinct, never review-independent"  unaffected
```

Four lines, down from five: `ORCHESTRATION.md:24` has left the class, which is the fix. The two
sites called unaffected were tested rather than accepted — both describe a subagent **the
executor dispatches**, which `E1`'s first sentence still admits as a self-check carrying no
verdict, and neither describes an orchestrator dispatch. They stand.

The class was then re-run by *shape* rather than by that one word, since the site `1a0a200`'s own
grep missed was missed precisely because it used different words. Patterns `fresh.context` /
`in-process` / `spawn` / `claude -p` / `own session` / `a full session` / `separately launched`
over all nine members return: `EXECUTION.md:302,315` and `REVIEW.md:220,315` (process-claim and
executor-side-auditor language, neither an orchestrator dispatch), `CONSTRUCTION-CHECKLIST.md:236`
(`R4`'s process-claim ceiling), and `ORCHESTRATION.md:22-24` (the three-roles table, §4 `O-1`).
**No surviving site offers the withdrawn permission.**

### 3.3 `E10`'s membership sentence against its mirrors

Nine paths transcribed from `E10`; all nine resolve at the subject (§2). The guard's mirror
`tooling/hooks/layer_path_check.py:37-47` carries the same nine in the same order, exact match —
the drift its own comment says "is caught by the next layer read" is absent. `E2`'s second half
was re-counted rather than accepted: `git ls-tree 153302a:schema/document-assurance-v3/` returns
**15** files, which is the "fifteen files" the rule names.

### 3.4 Path resolution across the whole standing text — the class the guard never re-scans

`layer_path_check.py` scans only the lines a commit **adds**, and `E10`'s clause holds the rest
by discipline alone. The guard's own resolution logic was re-implemented and run over the entire
standing text of all nine members at the subject:

```
--- unresolved path-shaped tokens in standing layer text @153302a: 0
```

The markdown-link class `E10` names as invisible to the guard ("prose and markdown links carry no
backtick token for it to find") was swept separately:

```
--- relative markdown links checked: 64; unresolved: 0
```

Ceiling, stated: both sweeps inherit the guard's shape, so a bare filename with no `/` is outside
both — which is the *prescribed* form for a caller-held artifact, not a gap.

### 3.5 Every id the layer cites, resolved

Rule ids: the checklist defines `E1`–`E12` and `R1`–`R10`, 22 rules, matching README's
"E1–E12 execution, R1–R10 review". Every `E<n>`/`R<n>` token cited anywhere in the layer resolves
to a defined rule — one apparent miss, `EXECUTION.md:234`'s `R0`, is an instruction-section id
(`R0…Rn`) and not a review rule, i.e. a false positive of the sweep, not a dangling citation.

`HD` ids: every `HD-nn` the layer cites resolves in `HARNESS-DECISIONS.md` (41 entries) or its
archive (16). **None dangles.**

Commit and blob ids: 22 distinct hex tokens. All five `E2`-named blobs resolve here as blobs —
`614932de` (the signed v4 `HD-56` binds), `dfc983d2` (the corrected v4), `b2dbdf75`, `68031fa2`,
`e1a2f26b` — so `E2`'s list is decidable by inspection exactly as it claims. Of the commit ids,
`0d73a5f` resolves here (`V3-RIDER-DEADLINE-REPOINT-v1`, 2026-08-18, matching
`EXECUTION.md:408`'s "instrument `0d73a5f`" and its date); every other — `418b89c`, `6fd0ae3`,
`7011916`, `7db177d`, `820b287`, `838c413`, `9ba9bbc`, `a22cca0`, `a8af54c`, `ac1b383`,
`ddd773a`, `de39b3d`, `f91a7c4` — is absent here and routes to the extraction-source repository
by the checklist header's rule. Contract v4's own supporting claim was checked: this repository's
first commit is `345acdd` dated **2026-08-15**, which is the date its `:34-38` states.

### 3.6 Factual assertions the members make about code (`E3`)

`E3` says an assertion written into instruction text runs the command that could falsify it.
Member 7's four claims, each run:

- `dispatch.CONSTRUCTION_ROLE_INSTRUCTION` hard-codes the stub path — **yes**, `dispatch.py:548-550`.
- `test_dispatch.py`'s `CHARTER_OUTSIDE` pins it independently — **yes**, hand-written literal at `:398` and `:522`.
- `MEMBER` pins it independently — **yes**, hand-written literal at `:463`.
- the construction fixture carries `{charter}` as a substitution, not the path — **yes**,
  `tooling/tests/fixtures/expected-construction-prompt.txt:3` reads `` `{charter}` ``.

All four are hand-written literals rather than imports of the module's own constant, which is
`E5` satisfied where the stub claims it. Member 6's weaker claim ("historical records point
here") also holds: 71 tracked files reference that path.

`ORCHESTRATION.md:36-37`'s "three review-side modes, and two executor-side modes" was checked
against the argparse group rather than the prose: `--subject`, `--range`, `--read`, `--executor`,
`--construction-executor` — **five, split 3/2 as stated**. `EXECUTION.md:349-353`'s tier
exception names files that pin doc paths; the two checkable in this repository hold —
`contract/Document-Work-Assurance-Contract-v4.md` at
`tooling/rsclib/document_harness/__init__.py:41`, and `document-harness/README.md` under
`tooling/tests/document_harness/test_readme_enumeration.py`, which exists here.
`README.md`'s "nine of its twelve obligations" checks out: `ORCHESTRATION.md` carries a 9-row
obligation table plus 3 sections it is the text for. Its "added as the tenth member 2026-08-18"
was tested for staleness against today's nine and is **accurate as a dated fact** — `HD-46`'s
title records the charter being established as 第十成员, and the count fell to nine only when
round `CONTRACT-V4` merged two supersessions into one file.

### 3.7 The instrument's battery leg, re-run

`EXECUTION.md`'s tiering owes this repository one command. Run immediately before this claim
(`E3`), from `tooling` as the text requires:

```
$ cd tooling && python -m pytest -q
844 passed in 130.56s (0:02:10)
```

Scope, stated: this ran against the **worktree at HEAD**, not at the subject commit. It transfers,
because HEAD differs from the subject only in `HARNESS-RIDERS.md` and
`git grep -l HARNESS-RIDERS -- tooling/` returns nothing — no leg reads that file. Separately,
`README.md` was checked to name all **15** schema stems by delimited token, the property
`test_readme_enumeration.py` guards: none missing.

Against `EXECUTION.md:406-412`'s figures (712 / 93.67s, pinned to `0d73a5f`), the drift is the
text's own instruction working — it pins figures to a revision and says to re-run. Recorded, not
filed: `v3-cold-read-21dad76.md` `O-4` already made this point.

## 4. Findings

### must-fix — none

The amendment did what `M-1` asked, at the bytes `M-1` supplied, and closed the class rather than
the instance.

### `L-1` (low, **carried forward** from `v3-cold-read-21dad76.md` — not a new finding)

**Still standing at this subject.** Re-derived independently before that record was opened:

```
$ git show 153302a:HARNESS-DECISIONS.md | grep -n '2026-08-24'
(exit 1 — no match)
$ git show 153302a:HARNESS-DECISIONS-archive.md | grep -n '2026-08-24'
(exit 1 — no match)
highest HD id present: 57
```

`E1` at `document-harness/CONSTRUCTION-CHECKLIST.md:36` cites "(user ruling 2026-08-24)", and
that ruling — together with the second one `1a0a200`'s body records, the waiver of the round
apparatus for a rule-changing amendment — has no home outside a commit body. The decision log's
own 准入三问 admits it on two of three tests (binds later rounds; a user ruling whose only home
is 对话与 commit 正文), and the shape has been named twice before by the log itself: `HD-19`
records a ruling that "从未建条目、只活在 `fd058aa` 正文，正是 VERIFY 的 `V-2`", and `HD-56` ②
one that "此前该裁决只活在修腿 commit `d0f185c` 正文，VERIFY 点名欠簿".

**Route unchanged: the user's register.** An `HD` entry is the user's to write, no amendment
machinery here reaches `HARNESS-DECISIONS.md` (`HD-19`, `HD-7`), and whether the form ruling and
the waiver ride as one entry or two is the user's call (`R5`). `912f837`'s body records the
deliberate decision **not** to bank it — "the question goes to the user directly" — so it is open
pending a user action, not lost. Re-reported here so that open state is visible at this subject;
**it must not be filed a second time or banked.**

### `L-2` (low, **carried forward** from `v3-cold-read-21dad76.md` — not a new finding)

**Corroborated independently, then found already routed.** Before that record's findings were
opened, this read grepped the layer for the reader role and reached the same place: `E1`'s
amended clause binds "a reviewer **or executor** the orchestrator dispatches", and the **reader**
is a third dispatch family, not a sub-case of either. The code says so in as many words —
`cli.py:167-168` calls them "Three review-side modes (product evidence commit, construction
range, E10 layer read)" handing "a cold **reviewer or reader**" its subject, `--read` is its own
mutually-exclusive flag, and `ORCHESTRATION.md:34` enumerates "the **reviewer, the reader and** …
the executor" as the three that start cold. The stated rationale — a subagent does not load the
system config — applies to a reader identically, and a reader's whole product is a judgment about
this layer's own text. Read literally, the constraint does not reach the dispatch that produced
this record.

**Tier held at low, deliberately not raised.** The counter-reading is real: the *Review side*
heading calls its subject "the independent **session** a dispatch reaches", and `R3` places reads
under that heading. Two defensible readings of a permission is the shape `R9` excludes from
wording-level, which is why low is right — and raising it to must-fix would route a fix that
**adds a bound** through the one channel that skips the round `E10` opens for design. That would
be the inflation `R3` warns against, wearing a different hat.

**Already banked** as row `e1-reader` at `912f837`, on the surface `e1-table` and
`charter-qualifiers` already occupy, with a design-shaped redeem-when confined to a round-eligible
batch per `R10` / `HD-37` ②. Re-reported for its open state only; **do not bank twice.**

### `O-1` (observation, new) — the three-roles table's other two carrier cells did not move

`document-harness/ORCHESTRATION.md:22-24`. The amended reviewer row now reads "a full session,
**in the form `E1` requires** — …", while the orchestrator and executor rows still read "a full
session — the one the user is talking to" and "a full session" plain. `E1`'s form clause binds
"a reviewer **or executor**", so the executor is under the same constraint the reviewer row now
points at, and only the reviewer row points.

**Nothing is false**, which is why this is an observation and not a finding: "a full session"
*is* the form `E1` requires, so both rows state the right carrier and no permission differs. What
the asymmetry costs is a reader's inference — a qualifier on one row of three reads as
row-specific. Named so that whoever opens the round `e1-reader` waits for inherits it rather than
rediscovering it (`E7`, `HD-41` ④): that round already collects `e1-table` (a missing obligation
row) and `charter-qualifiers` (three cite-only rows that dropped their rules' qualifiers) on this
same file, and this is a fourth item on the same surface. **Bytes deliberately not supplied** —
adding the pointer to a second row is a restatement this file's narrow form exists to avoid, and
choosing between that and rewording the table header is design.

### `O-2` (observation, new) — one banked row's line cite is one line short

Rider `py-convention` names its member-side site as `document-harness/EXECUTION.md:364`; at this
subject the bare `python -m pytest -q` is at **`:365`** (`v3-cold-read-21dad76.md` `O-3` also read
it as 365). `HARNESS-RIDERS.md` is not a member and is outside this read's subject, so this is
recorded, not filed — noted only because a redeeming batch navigating by that number lands one
line above the site.

## 5. Coverage — what was read in full, sampled, and only probed (`R4`)

**Read in full, end to end:** all nine members at their subject blobs, 1640 lines (§2) — the
citation channel was available for eight and was not taken. `HARNESS-DECISIONS.md` lines 1–162
(header plus `§live`, eight entries). `HD-57` and `HD-55` in full inside `§implemented`.
`tooling/hooks/layer_path_check.py` lines 1–120. The amendment commit `153302a` in full, and
`1a0a200`'s diff and body in full.

**Sampled:** `v3-cold-read-21dad76.md` — its header, §1 (lines 1–80), §2, and §4 findings read in
full; **§3 and §5 were not read**, deliberately, so that this read's own checks were derived
rather than replayed. `HARNESS-RIDERS.md` — four rows read, the file not read end to end.
`912f837`'s body in full, its diff line in full.

**Probed only, for named claims and never read end to end:**
`tooling/rsclib/document_harness/dispatch.py`, `cli.py`, `__init__.py`,
`tooling/tests/document_harness_review/test_dispatch.py`,
`tooling/tests/document_harness/test_readme_enumeration.py`,
`tooling/tests/fixtures/expected-construction-prompt.txt`. `§implemented` beyond the two entries
above, and `HARNESS-DECISIONS-archive.md`, were probed by id only.

**Not done, and why.** No guard was mutation-tested (`E4`, `R8`). The subject adds no guard and
changes no code — one line of prose in one member — so there is no new binding force to prove.
The standing guard whose subject *is* this layer was instead exercised the other way: its
resolution logic was re-run over the whole standing text it never re-scans (§3.4), which measures
its blind spot rather than its binding force. **This read establishes nothing about whether
`layer_path_check.py` still fails when it should.**

**Honesty ceilings** (`R4`, and `REVIEW.md`'s own list):

- **Process claims have no evidence lock.** That this read ran in a fresh context, that it ran as
  its own session rather than as an in-process subagent, and that its findings were reached before
  `v3-cold-read-21dad76.md` §4 was opened, are **marked, not verified** — no artifact at any
  revision could settle them. The ordering claim matters to `L-1`/`L-2`'s value as corroboration,
  and it is exactly the class `REVIEW.md` says to state rather than paper over. It is also the
  class `L-2` is about, which is not a coincidence.
- **Declared identities are names, not proof of independent contexts.**
- **A byte comparison proves bytes.** §3.1 establishes that the applied cell equals the prescribed
  cell. It establishes nothing about whether `M-1` prescribed the right cell — that judgment was
  re-made here from `E1`'s text (§3.1, §3.2), not inherited.
- **The class sweeps are keyword- and shape-bound.** §3.2 ran one word and seven shapes over nine
  members. A site expressing the withdrawn permission in words none of the eight patterns contains
  would not have been found — which is the precise way `1a0a200`'s own scan missed
  `ORCHESTRATION.md:24`, so the ceiling is stated rather than assumed away.
- **Sites outside the nine members were not swept.** `v3-cold-read-21dad76.md` `O-2` names four
  (`io-design.md:31,34-35`, `split-design.md:265,277`, `harness-batch-b.plan.md:193-194`), two of
  them under signatures that make their bytes non-free-channel. This read did not re-derive that
  list and does not confirm it; none is a member, so none is this read's subject.
