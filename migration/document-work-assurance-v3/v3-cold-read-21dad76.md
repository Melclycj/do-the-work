# Cold read — the instruction layer at `21dad76` (round `STRANGER-PROOF` opening)

**No verdict.** A read is not a round (`R3`): it spends no budget, carries no verdict, and its
output is findings tiered must-fix / low / observation. Nothing below certifies any text, and
nothing below is banked as any round's FULL.

**Findings: 1 must-fix, 2 low, 4 observations.** The must-fix is a member that misdirects an
actor: `ORCHESTRATION.md`'s three-roles table still offers the reviewer carrier `E1` stopped
allowing yesterday, and it is the orchestrator's own charter — the file the session choosing a
dispatch form reads. `M-1` supplies the bytes. The two lows are the same amendment's other
edges: the 2026-08-24 user rulings behind it have no home outside a commit body (`L-1`), and
its new form constraint enumerates two of the three dispatched roles (`L-2`).

**The citation channel was available for seven of nine and was not taken.** Members 2, 3, 4,
5, 6, 7 and 9 are byte-identical to the blobs `v3-cold-read-cf54a79.md` §2 records —
re-derived here against `cf54a79` itself rather than read off that table (`R2`). Members 1 and
8 changed under round `STRANGER-GUARDS`, the `HD-57` application and the `E1` amendment, and
were owed a read regardless. All nine were read end to end anyway.

**What this read discharges.** The member-edit debts `CONSTRUCTION-LEDGER.md`'s
`STRANGER-GUARDS` entry names (the checklist's citation-resolution paragraph, and the v4 /
`E2`-literal edits the `HD-57` application would land — `HD-57`'s 后果 line says the same,
"v4 与 checklist 的成员编辑欠独立 read，随下一轮开轮冷读"), plus the read `1a0a200` deferred
under `E10`'s deferral lane. All three sit inside the two changed members below and were read
at full-member cost.

**Standing instructions read.** `migration/document-work-assurance-v3/v3-harness-review-contract.md`
(the stub, member 7) → `document-harness/CONSTRUCTION-CHECKLIST.md` in full, both sides, per the
stub's *"It is your standing instruction and its own counterpart; read all of it."*
`HARNESS-DECISIONS.md` header (1–27, its own state machine) plus `§live` (28–162, **eight**
entries — `HD-56`, `HD-44`, `HD-41`, `HD-36`, `HD-35`, `HD-34`, `HD-23`, `HD-9`), which `E10`'s
tail owes at a round's opening. Unchanged in membership against the previous read's eight.
`§implemented` and `HARNESS-DECISIONS-archive.md` were **not** read end to end — probed for the
ids the members cite (§3.6) and for `HD-57` in full (§3.1), it being the ruling one of the two
member diffs applies. Cited by section, never by blob.

---

## 1. What the subject is, and how it was derived

The dispatch supplied one commit and nothing else. Everything below was re-derived (`R2`).

```
$ git rev-parse HEAD
21dad76901526abb7b84845d7b927c56adc6c962

$ git status --porcelain
(empty)

$ git log -1 --format='%H%n%ad%n%s' 21dad76901526abb7b84845d7b927c56adc6c962
21dad76901526abb7b84845d7b927c56adc6c962
Mon Aug 24 00:57:18 2026 +1000
V3-STRANGER-PROOF-PLAN-v1
```

HEAD is the subject commit and the worktree is clean, so the worktree bytes are the subject
bytes — verified per member with `git hash-object` against `git rev-parse 21dad76:<path>`,
9/9 MATCH (§2), rather than inferred.

**The subject commit touches no member.**

```
$ git show --stat --format='' 21dad76
 document-harness/plans/stranger-proof.plan.md | 80 +++++++++++++++++++++++++++
 1 file changed, 80 insertions(+)
```

A cold read of standing layer text at a round's opening, not a read of a diff. The plan is not
a member and was deliberately not relied on (`R2`); the commit body's declarations were read as
the round-opening record they are, and one of them — "every dispatch this round runs as its own
`claude -p` session" — is what `M-1` below shows the layer does not uniformly say.

**The freeze window is intact, re-derived rather than assumed** (`REVIEW.md` says to). The
gitignored marker `.harness/review-pending.json` names subject
`21dad76901526abb7b84845d7b927c56adc6c962`, dispatched `2026-08-23T14:57:24+00:00` — six
seconds after the subject commit (14:57:18 UTC). The branch tip is the subject, so no commit
has landed since dispatch (`E9`). This repository's tracked hook runs `layer_path_check.py`
alone, so the window here is discipline, held, not enforcement — the standing shape rider
`self-caller-guards` already banks it.

## 2. The member set and each member's blob

The set is `E10`'s own sentence — **"exactly these nine paths and nothing else"** — hand-
transcribed from the checklist at the subject blob, then machine-compared against the guard's
mirror (§3.3). Blob ids per `E10`'s *"a read's record states the blob id of each member it
read, because citation depends on it"*. Line counts are `git show | wc -l`, sizes
`git cat-file -s`.

```
 #  blob                                      lines  bytes  path                                            vs v3-cold-read-cf54a79
 1  c0e3e2dd8960a00f0074d98b9ff79b85dcfb933b    249  19869  document-harness/CONSTRUCTION-CHECKLIST.md      CHANGED (was 7a18cd1c)
 2  0454c8a59db88fa4c4b599bb7f6de39681489682     38  10511  document-harness/README.md                      same
 3  b187af5c836781a366aeb3c9ef3a1338a9955de0    519  36636  document-harness/EXECUTION.md                   same
 4  86e5ed7ad6792a7548ce968dea3cbcfcc3ee9f3e    319  20627  document-harness/REVIEW.md                      same
 5  9a67401f12da68b8990c4543867f204163d12e32    119   8382  document-harness/ORCHESTRATION.md               same
 6  6d5714923870b4e13e8928221a80df68e563a5ed      5    511  migration/…/v3-harness-operating-contract.md    same
 7  29bdc9fbde6e8db38d601dd2340d4b46a24a296f      5    924  migration/…/v3-harness-review-contract.md       same
 8  dfc983d2e3d9fb5ca67b053a16fcfb0e6715b11a    342  22185  contract/Document-Work-Assurance-Contract-v4.md CHANGED (was 614932de)
 9  09aa869962f592c2f86c9379be0ef3eb7d2232ff     44   2812  schema/…/paragraph-map.schema.json              same
                                              -----
                                               1640  total lines read
```

**Where the two changes came from.** `git log cf54a79..21dad76 -- <the nine>` returns exactly
three commits, and the aggregate member diff was read in full alongside the standing text:

- `c2e955b` `V3-STRANGER-GUARDS-v1` (that round's candidate) — member 1 only, the
  citation-resolution paragraph gains the by-name / role-word test and the worked
  "caller `6fd0ae3`" case. Reviewed by that round's FULL `18bb2bf` and VERIFY `483dbf3`;
  read here as standing text.
- `1656e59` `V3-HD57-APPLICATION-v1` — members 1 and 8. `E2`'s v4 literal `614932de…` becomes
  `dfc983d2…` with the correction's provenance; v4 §5's Verification-mode row loses the
  deleted third value; v4 `:34-36` gains the plan-digest provenance sentence.
- `1a0a200` `V3-E1-SESSION-FORM-v1` — member 1 only, `E1`'s form clause. This is the amendment
  `M-1`, `L-1` and `L-2` are all about.

**Member 8 is `E2`-frozen and a member at once** — the `HD-20` intersection `HD-56` ② names.
Its bytes moved under `HD-57`'s recorded ruling, which is the order `HD-20` requires, and the
signature object `HD-56` binds is unchanged in history (§3.2).

`HARNESS-DECISIONS.md` is **not** a member — `E10`'s tail owes it at a round's opening while
denying it membership (`HD-19`). Cited by section, never by blob.

## 3. What was checked, and what the commands returned

Unless a line says otherwise, the scope is **the nine member blobs at `21dad76`** and nothing
else.

### 3.1 The two changed members, read against the rulings that authorised them

`1656e59` was checked clause by clause against `HD-57`'s five-site ruling (read in full at
`HARNESS-DECISIONS.md:165-186`). Sites ① and ② are member 8 and landed as ruled; ③④⑤ are
schema-pack files outside the layer and were spot-checked only — `document-work-spec.schema.json`
and `document-work-spec.v2.schema.json` line 4 now read
`sole owner: the run's executor, its WorkSpec author`, which is what v4 §3 says.

The corrected enum row was checked against its declared single home rather than against the
ruling's description of it:

```
$ git show 21dad76:schema/document-assurance-v3/common.schema.json | grep -n verificationMode -A2
118:    "verificationMode": {
119-      "enum": ["local_check", "review_only"],
```

and the deleted value survives nowhere in the layer — a tree-wide `git grep` for it returns ten
hits, all in journals, plans, the ledger archive and closed-run records, none in a member.

### 3.2 `E2`'s freeze surface

Both halves are decidable by inspection and were inspected.

```
$ git rev-parse 21dad76:contract/Document-Work-Assurance-Contract-v4.md
dfc983d2e3d9fb5ca67b053a16fcfb0e6715b11a          # = E2's literal

$ git cat-file blob 614932de40b841ec9777719aea88de04864eb67b | wc -l
339
$ git cat-file blob 614932de40b841ec9777719aea88de04864eb67b | sha256sum
1b1061cbdeb6585ee5b33f3dcf91c2ee376f60f3e92076998d7930b70f7a23fa
```

The signed blob is byte-intact at the id, line count and digest `HD-56` records, so `E2`'s
"the signed blob remains the signature object `HD-56` binds" is true as written, and the
correction did not overwrite the signature object. `git ls-tree --name-only 21dad76
schema/document-assurance-v3/` returns **15** files, which is the re-baseline count `E2`
states. One blob and one directory: sixteen frozen files, matching `HD-56` ① and `HD-44`'s
2026-08-23 correction.

### 3.3 `E10`'s membership sentence against its mirrors

The nine paths were parsed out of the `E10` bullet's own prose and compared with the guard
and the hand-written test constant:

```
paths in E10's membership sentence: 9
equal to LAYER (in order): True
sentence says: exactly these nine paths
```

`tooling/tests/document_harness/test_precommit_checks.py`'s `EXPECTED` is the same nine in the
same order, hand-written per `E5`. The five prose sites rider `E10-sync` also tracks were
re-read and all say nine: `.githooks/pre-commit:14-15`, root `README.md:62`,
`document-harness/ONBOARDING.md:133`, `document-harness/README.md:34`, and
`document-harness/io-design.md:8,42`. Root `README.md:84` and `CONSTRUCTION-LEDGER.md:146` say
ten and are dated historical statements about `DE-PREFIX` day, not standing counts. The
`E10-sync` discipline held through the `CONTRACT-V4` ten→nine change.

`document-harness/README.md:24`'s "added as the tenth member 2026-08-18" was checked rather than assumed: the
layer held ten on that date (the present nine, minus contract v4, plus the two supersessions
that left with round `CONTRACT-V4`), so the sentence is a historical fact and not a stale count.

### 3.4 Path resolution across the whole standing text — the class the guard never re-scans

`E10` assigns this to the clause and not to the script ("the standing text it never re-scans
stays unscanned"). Run here with the guard's own predicate over the **entire** text of all
nine members, not just added lines:

```
TOTAL unresolved backtick path tokens in standing text: 0
```

Every markdown link target in the nine was resolved independently (relative to each member's
own directory, rejecting any resolution escaping the repository root): **0 unresolved**. Bare
non-backticked path-shaped tokens were swept separately; the only true hits are member 9's
`$id` values (`researchsystem/schema/…`), the pack-wide JSON-Schema identifier convention on
all fifteen files — `E10`'s own tail excepts `E2`-frozen bytes while they are frozen, so the
clause covers it and this is not a finding.

`E10`'s account of what the guard cannot see was verified against the code rather than trusted:
`PATHLIKE` admits no angle brackets (placeholder segments invisible), `TOKEN` requires
backticks (prose and markdown links invisible), and the `-U0` header branches require a space
in fourth position, so an added line whose content opens `++ b/` mis-files and any other
`++ ` silences, while a pasted `+++ ` header does not. All four statements hold.

### 3.5 Commit ids cited by the layer, against `E10`'s resolution rule

Every hex object id in the nine members was extracted and resolved — 22 distinct, counting the
all-digit `7011916` the naive scan drops:

```
  blobs   : 5  614932de 68031fa2 b2dbdf75 dfc983d2 e1a2f26b
  commits : 2  0d73a5f8 25388938
  absent  : 15 418b89c 6fd0ae3 7011916 7db177d 820b287 838c413 86defbc 9ba9bbc
               a22cca0 a8af54c ac1b383 ddd773a de39b3d f91a7c4 fef3a2e
```

The five blobs are the frozen contract set (§3.2). The second commit is an artefact of the
extraction worth naming rather than hiding: `25388938` came out of the *filename*
`v3-review-verify-2538893.md` in `README.md`'s Local-enforcement row, not out of a bare
citation — and it resolves here, as `V3-DE-PREFIX-FIX-v1` of 2026-08-20, which is the subject
that record is named for. Applying `E10`'s test to the bare citations:

```
$ git log -1 --format='%H | %ad | %s' 0d73a5f
0d73a5f8fad2a2fe821429539cd777f496709af3 | Tue Aug 18 16:04:37 2026 +1000 | V3-RIDER-DEADLINE-REPOINT-v1
$ git cat-file -t 6fd0ae3
fatal: Not a valid object name 6fd0ae3
$ git cat-file -t 7011916
fatal: Not a valid object name 7011916
```

`EXECUTION.md`'s paired "instrument `0d73a5f`, caller `6fd0ae3`" is the paragraph's worked
case, and it works: the role word routes by the first sentence's test, the instrument id is a
commit of this repository dated inside its history (which begins 2026-08-15 — v4 `:34-36`'s
claim, verified against `git log --reverse`), and the caller id is not, so it reaches the
extraction-source repository. `7011916`, named in `E10`'s own preamble and in both stubs,
likewise does not resolve here and routes as the rule says. No cited id is homeless.

### 3.6 Cross-references the members make outside themselves

Rule ids: `E1`–`E12` and `R1`–`R10` are each declared exactly once, no gaps, no duplicates.
Every `E<n>`/`R<n>` cited anywhere in the layer is declared, the single apparent exception
being `R0`, which is `EXECUTION.md`'s numbered-section label under the enumerated form and a
different namespace. `V3-D1`–`D7`, `D9`, `D10` and invariants 4 and 10 are cited; the
invariants are v4 §7 (`:158`, thirteen of them) and the decision ids are the plan §2 set v4
`:39` names as the locked design authority. All seventeen `HD-<n>` ids the layer cites exist
in `HARNESS-DECISIONS.md` or its archive; four are `retired` or `superseded` (`HD-14`, `HD-28`,
`HD-39`, `HD-42`) and every one of those is cited as provenance for a past change, never as a
rule in force.

Code and file claims the members make, each checked at the subject commit rather than accepted:

| the member's claim | checked |
|---|---|
| stub 7: `dispatch.CONSTRUCTION_ROLE_INSTRUCTION` hard-codes this path | `dispatch.py:548-550`, exact string |
| stub 7: `test_dispatch.py`'s hand-written `CHARTER_OUTSIDE` / `MEMBER` pin it independently (`E5`) | `:398`, `:463`, `:522` — three hand-written literals |
| stub 7: the construction fixture carries `{charter}` as a substitution, not the path | `expected-construction-prompt.txt`, `.format(charter=…)` at `:681` |
| `ORCHESTRATION.md`: `dtw dispatch` has three review-side and two executor-side modes | `cli.py:167-169`, and the four dispatch families in `dispatch.py`'s docstring |
| `EXECUTION.md`: the doc paths code or a test pins | all four confirmed — `test_readme_enumeration.py:36`; `layer_path_check.LAYER`; `document-harness/templates/` holds exactly the two files `init_target.py` copies; `__init__.py:41` `CONTRACT_PATH` |
| `EXECUTION.md`: `transcript_audit(spec, instruction_text)` returns `(result, findings)` | `instruction.py:349-355`, signature and docstring |
| `EXECUTION.md`: `resolve_form`, one place | `instruction.py:329`, sole definition; all other hits are call sites and tests |
| `EXECUTION.md`: run-v2 template members | `check_template_instance.py`, `make_paragraph_map.py`, `compare_blocks.py`, `run_bind_v2.py` all present |
| v4 §13.1: successor result root `schema_version` const `"2"` | `review.v2.schema.json:22-23` |
| v4 §13.2: `assurance_state.DIGEST_PROTECTED_FIELDS` is those exact five fields; `pointer_for` is the documented path, `pointer_to`/`pointer` still exist | `assurance_state.py:81-89`, `:92`, `:100`, `:122-138` |
| `REVIEW.md`: the pre-wave-2 package-flow sections moved to a history file beside it | `document-harness/history/REVIEW-v1-package-flow.md` present; the member writes the link relative to its own directory, which resolves |
| `README.md`: this repository's hook runs the instruction-layer check, the caller's runs the other two | `.githooks/pre-commit` runs `layer_path_check.py` and says why it runs neither other |
| v4 §5's closed enums against their homes | every row matches `common.schema.json`, `user-decision.schema.json`, `review.schema.json`, `local-check-spec.schema.json` |

### 3.7 The instrument's battery leg, re-run

`EXECUTION.md` names one command for this repository and warns against trusting the tallies
written beside it. Re-run at the subject (`E3`):

```
$ cd tooling && python -m pytest -q
844 passed in 128.74s (0:02:08)
```

Against the `712 passed in 93.67s` the text pins to `0d73a5f` (2026-08-18). The text's own
instruction — "Re-run the battery for a current figure rather than trusting any list written
here (`HD-41` ③)" — is what makes that gap correct rather than stale, so this is evidence, not
a finding (`O-4`).

## 4. Findings

### `M-1` (must-fix) — `ORCHESTRATION.md`'s three-roles table still offers the reviewer carrier `E1` withdrew

**Location.** `document-harness/ORCHESTRATION.md:24`, the reviewer row's carrier column:

> a full session **or** a subagent — what decides independence is who set the question (`R1`), not the form

**The ground truth it violates.** `E1` as amended at `1a0a200`
(`document-harness/CONSTRUCTION-CHECKLIST.md:33-35`): *"a reviewer or executor the orchestrator
dispatches runs as its own session (`claude -p` or a separately launched session), **never as
an in-process subagent**: a subagent does not load the system config, so the forms are not
equivalent (user ruling 2026-08-24)."* The cell offers a subagent as a legitimate carrier and
closes with "not the form", which is the mirror of the exact sentence that amendment replaced —
the pre-amendment `E1` read "may run as a subagent or as its own session, and the form changes
nothing".

**What goes wrong.** `ORCHESTRATION.md` is the orchestrator's charter, and the orchestrator is
the role that chooses a dispatch's form. The table's subject is precisely which session carries
which role — the file says so itself two paragraphs down, which is why `HD-55`'s carrier was put
there. An orchestrator reading its own charter is told a subagent reviewer is permitted; `E1`
tells the same session it is not. Two members, opposite permissions, and the permissive one is
the one that role reads first. Round `STRANGER-PROOF` opens by declaring every dispatch runs as
its own `claude -p` session, so the round in flight has resolved the conflict by hand — the next
one has no reason to.

**Why the amendment missed it.** `1a0a200`'s body records a class scan and its terms:
*"grep for: form changes nothing / as a subagent / subagent form, over document-harness
markdown, returned only CONSTRUCTION-CHECKLIST.md:33-35, so this edit is the class entire."*
Re-run here, that grep does return only the checklist — the declared scope covered the sibling
site, and the three search terms did not match it, because the cell writes "**or** a subagent"
and "not the form". The full class, by the word itself, over the nine members' whole text:

```
CONSTRUCTION-CHECKLIST.md:31  E1's opening — an executor-dispatched subagent is a self-check   unaffected
CONSTRUCTION-CHECKLIST.md:33  the amended clause                                              the fix
CONSTRUCTION-CHECKLIST.md:35  the amended clause                                              the fix
EXECUTION.md:336              "a subagent auditor is V3-D7-distinct, never review-independent" unaffected —
                              an executor-side gate, not an orchestrator dispatch
ORCHESTRATION.md:24           the reviewer carrier column                                     M-1
```

`E1`'s first sentence and `EXECUTION.md:336` were checked and stand: both describe an
executor-side subagent, which `E1` still admits as a self-check. The defect is one site.

**Minimum fix (bytes).** In `document-harness/ORCHESTRATION.md:24`, replace the carrier cell

> a full session **or** a subagent — what decides independence is who set the question (`R1`), not the form

with

> a full session, in the form `E1` requires — what decides independence is who set the question (`R1`)

This deletes the withdrawn permission and the now-false "not the form" half, keeps `R1`'s
holding, and points rather than restating, which is what this file's stated narrow form
requires (`HD-46`; `HD-5` on transcription as a drift surface). It adds no clause and changes
no rule, so the replacement is not itself design.

**Route.** `E10`'s must-fix channel — an amendment commit plus an independent re-read of the
amended text, not a round and no budget (`R10`, `HD-36` ①). The path is not one `E2` freezes,
so `HD-20`'s bar does not apply.

### `L-1` (low) — the 2026-08-24 rulings have no home outside a commit body

**What.** Two user rulings of 2026-08-24 are recorded only in `1a0a200`'s commit body: the
session-form constraint itself, and the waiver of the round apparatus for applying it ("the
user approved skipping review, executor dispatch and the independent-read leg for this
one-sentence keyword edit"). Re-derived rather than assumed:

```
$ grep -rn '2026-08-24' HARNESS-DECISIONS.md HARNESS-DECISIONS-archive.md \
      CONSTRUCTION-LEDGER.md CONSTRUCTION-LEDGER-archive.md HARNESS-RIDERS.md
(exit 1 — no match)

highest HD id present: 57
```

**The downstream decision that goes wrong** (`R9` requires one to be named). The substance of
the first ruling is carried — `E1`'s own text now says it — but the second is carried nowhere.
It is the ruling that says a rule-changing amendment may skip the round `E10` otherwise
requires, and the next session facing that choice reads `E10`, finds no waiver channel for the
design test, and either re-derives the permission from a commit body nothing points it at, or
opens a round the user has already shown willing to waive. `E10`'s deferral lane is not that
channel (see `O-1`). The decision log's own admission test admits this — 绑下一轮及以后 is
plainly true — and the shape has been called twice before: `HD-19` records a ruling that
"从未建条目、只活在 `fd058aa` 正文，正是 VERIFY 的 `V-2`", and `HD-56` ② records one that
"此前该裁决只活在修腿 commit `d0f185c` 正文，VERIFY 点名欠簿，本条即其家".

**Route.** The user's register, not this layer and not the bank — an `HD` entry is the user's
to write, and no amendment machinery here reaches `HARNESS-DECISIONS.md` (`HD-19`, `HD-7`).
Same route as `v3-cold-read-cf54a79.md`'s `L-3`. The reader supplies no bytes: what the entry
says, and whether the form ruling rides it as one entry or two, is the user's (`R5`).

### `L-2` (low) — `E1`'s form constraint names two of the three dispatched roles

**What.** The amended clause binds "a reviewer **or executor** the orchestrator dispatches".
The **reader** — this role — is a third dispatch family, not a sub-case of either:
`cli.py:167-169` calls them "three review-side modes (product evidence commit, construction
range, E10 layer read)", `dispatch.py`'s docstring counts four families, and
`ORCHESTRATION.md:34` enumerates "the **reviewer, the reader and** … the executor" as the three
that start cold. `R3` says in as many words that a read is not a round at all.

**What goes wrong.** The stated rationale — a subagent does not load the system config —
applies to a reader identically, and a reader's whole product is a judgment about the layer's
own text. Read literally, the constraint does not reach the dispatch that produced this record.
The counter-reading is available and not weak: the *Review side* heading calls its subject "the
independent **session** a dispatch reaches", so that heading already says session. Two
defensible readings of a permission is the disagreement shape `R9` excludes from wording-level,
which is why this is filed as low rather than banked silently.

**Route.** The bank (`HARNESS-RIDERS.md`). The fix adds a bound to a rule, so `E10`'s design
test opens a round for it and `R10`/`HD-37` ② confine its redeem-when to a round-eligible
surface. Suggested row — *what*: `E1`'s form constraint enumerates reviewer and executor and
omits the reader, the third `dtw dispatch` family; *redeem-when*: the next round-eligible batch
touching `E1`'s form clause or `ORCHESTRATION.md`'s three-roles table (`M-1` will touch the
latter, but as a must-fix amendment, which per `R10` meets the touch condition while being
unable to redeem it); *deadline*: the first read dispatched as an in-process subagent on the
strength of the omission. Bytes deliberately not supplied.

### `O-1` (observation) — the amendment's self-classification, for the precedent it sets

`1a0a200`'s body says the edit "rides the next opening read of this layer per `E10`'s deferral
lane - deferral, never exemption". That lane is conditioned: it is for "an amendment that
neither adds a clause to any rule nor changes what any rule requires … and whose effect on
every round in flight is nil", and the commit's own next sentence says "what changes is that
form is now additionally constrained". By `E10`'s following clause — "replacing or deleting
text so that what a rule requires changes, is design and opens a round" — this was design. What
actually covers it is the recorded user waiver, which is `L-1`'s subject; the lane citation is
the wrong name for the right authorisation. Recorded, not routed for a fix: commit bodies are
immutable and are not instruction layer (`HD-38`'s "已落地的三个混装 commit 照记不回改"
precedent). The deferred read itself has now happened — this record is it.

### `O-2` (observation) — sibling sites of the withdrawn claim outside the layer

Declared scope: all tracked files, excluding `migration/` records and `document-harness/journal/`
(quotation-bearing history). Outside the nine members, the pre-amendment form-equivalence claim
survives at four sites:

- `document-harness/io-design.md:31` — the three-roles table this layer's table descends from,
  reviewer carrier `**可为 subagent**`; and `:34-35`, which flags the conflict in the *opposite*
  direction (the old `E1` versus reviewer-may-be-subagent) and routes it to §8/R4, the round
  that produced the sentence `1a0a200` has now withdrawn. This file is **signed** (`HD-35`,
  blob `a1594eb27311cfe4cdc1aa32c32a521c0af4b65f`, third signature 2026-08-23), and `HD-35`
  says "对该文件的后续实质修改欠重签" — so bytes there are not free-channel material.
- `document-harness/split-design.md:265` and `:277` — the same carrier claim, and the
  three-roles ↔ three-carriers mapping (`session / subagent / claude -p`) that motivates it.
  Also signed (`HD-40`).
- `document-harness/plans/harness-batch-b.plan.md:193-194` — records the discipline as in force
  and notes "尚未行使 subagent-reviewer", which as of the 2026-08-24 ruling will now stay true.

None is a member, so none is this read's subject and none is filed as a finding. They are named
so the `M-1` fix leg inherits the list rather than rediscovering it (`E7`, `HD-41` ④), and so
that the re-signature cost of the io-design and split-design halves is visible before anyone
treats them as one sweep.

### `O-3` (observation) — banked rider `py-convention`'s member-side site still stands

`document-harness/EXECUTION.md:365` still reads `python -m pytest -q` bare, which is the site
rider `py-convention` banks with the note "**`E10` 成员**——POSIX executor 照句执行即
command not found". Re-verified standing at the subject; `EXECUTION.md` is unchanged since the
rider was written, so its touch condition has not arrived. Re-filed as nothing — noted only so
this read is not read as having missed it.

### `O-4` (observation) — the battery figures beside `EXECUTION.md`'s tiering

844 passed / 128.74s at the subject, against the text's 712 / 93.67s pinned to `0d73a5f` (§3.7).
The text pins its figures to a revision and instructs re-running, so the drift is the rule
working. Recorded because a reader comparing the two numbers cold could mistake it for staleness.

## 5. Coverage — what was read in full, sampled, and only probed (`R4`)

**Read in full (end to end):** all nine members, 1640 lines. `HARNESS-DECISIONS.md` lines 1–162
(header + `§live`, eight entries, the section ending at `:162` where `§implemented` opens on
`:163`) and `HD-57` at `:165-186`. `HARNESS-RIDERS.md` in full (**26** rows), to check whether
`M-1`, `L-1` and `L-2` were already banked — none is; the closest,
`charter-qualifiers` and `e1-table`, are about the nine-obligation table, not the roles table.
The three member diffs across `cf54a79..21dad76` in full. `tooling/hooks/layer_path_check.py`
and `.githooks/pre-commit` in full.

**Sampled:** `tooling/rsclib/document_harness/` — `dispatch.py` (docstring, the four family
sections' constants and prompts), `cli.py` (subcommand construction and the dispatch-mode
branch), `assurance_state.py:1-140`, `instruction.py` (two named functions), `init_target.py`,
`__init__.py` (contract path and `pack_digests`). The schema pack: member 9 in full, the other
fourteen probed for the `$id`, enum and title claims the members make about them.

**Probed only:** `HARNESS-DECISIONS.md` `§implemented` and `HARNESS-DECISIONS-archive.md` —
grepped for the seventeen ids the members cite and for `2026-08-24`, never read through.
`CONSTRUCTION-LEDGER.md` and its archive — grepped for the same and for member counts.
`document-harness/plans/` — grepped for the `O-2` class; `stranger-proof.plan.md` deliberately
not relied on (`R2`). The test suite was executed, not read: 844 cases, of which I read
`test_precommit_checks.py`'s membership class and `test_readme_enumeration.py`'s docstring.

**Honesty ceilings.**

- **Process claims are marked, not verified.** That this session started cold, holds none of
  `R1`'s four holdings but "reported through", and read what §5 says it read, is my declaration.
  Nothing in the repository locks it. Note the standing irony `L-2` names: whether *this*
  dispatch's form satisfies `E1` is exactly what the layer does not say.
- **Not mutation-tested.** `R8` asks for mutation on the guards that matter; this read ran
  `layer_path_check`'s predicate over standing text as a *measurement*, not as a proof that the
  guard binds. `E10-sync` already banks the standing evidence that the prose leg has no guard at
  all, and I did not re-prove it.
- **Absence claims are scoped, not absolute** (`HD-41` ①②). "No unresolved path token" means the
  guard's own predicate, plus a link resolver, plus a bare-token sweep, over the nine members'
  whole text at this commit. Tokens with placeholder segments, tokens without one of seven
  extensions, and extensionless tokens are outside all three — the blind spots rider
  `e10-cannot-see` banks, unchanged and not re-measured here.
- **`M-1` is a text-versus-text contradiction, established by reading both.** I did not observe
  an orchestrator act on it. The failure it enables is available, not witnessed.
