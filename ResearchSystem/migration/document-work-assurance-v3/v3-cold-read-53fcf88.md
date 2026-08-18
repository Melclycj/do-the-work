# Cold read — the instruction layer at `53fcf88`

**No verdict.** A read is not a round (`R3`): it spends no budget, carries no verdict, and its
output is findings tiered must-fix / low / observation. This read discharges two obligations at
once, both owed by `E10`: the independent re-read of the amended text committed at `66133c6`
(the answers to the previous read's two must-fix findings), and the layer read the free-channel
bytes of `53fcf88` ride. Nothing below certifies any text, and nothing below is banked as any
round's FULL.

Named `cold-read` rather than `checkpoint-read` because all ten members were read end-to-end
and every blob id is stated below, which is what keeps `E10`'s citation channel open for the
next round's opening read.

**Findings: 1 must-fix, 1 low, 5 observations.** The must-fix is the unswept residue of the
previous read's `M-1`: the amendment fixed the bullet at `ORCHESTRATION.md`:89 but left the
file's own opening sentence, :3, defining the orchestrator as the session that runs a round
*without doing the work inside it* — the same claim, and the amendment's own new phrase at :90,
"a session holding both work-side roles", now contradicts it inside the same file.
The low is a second defect in the sentence `L-2` corrected: the numeral is now right and the
scope is still wrong. Both must-fix answers were checked against the repository and **hold**:
the three-mode claim is what `argparse` actually declares, and the rewritten bullet says only
what `E1` says.

---

## 1. Subject, re-derived

Derived from the repository, not from the dispatch. `HEAD` is the subject and the worktree is
clean, so every command below ran against bytes identical to the subject commit's:

    $ git rev-parse HEAD
    53fcf88bc8e9e86e9b44250cebd9b9b0b2316604
    $ git status --porcelain
    (no output)

`E9`'s window, re-derived rather than assumed: branch tip equals the dispatched subject, so no
commit landed between dispatch and this record. The status above was taken before anything was
read; the only later change to the worktree is this file, untracked.

Two commits separate this subject from the previous read's (`d8cc6d1`). Classified by hand from
`git diff --name-only d8cc6d1 53fcf88`, against `E10`'s sentence rather than any reported list:

| path | member? | which commit |
|---|---|---|
| `ResearchSystem/document-harness/ORCHESTRATION.md` | yes | both — `66133c6` (M-1, M-2), `53fcf88` (L-3) |
| `ResearchSystem/document-harness/README.md` | yes | `53fcf88` (L-2) |
| `README.md` (repository root) | no | `53fcf88` (L-1, plus two disclosed extensions) |
| `ResearchSystem/migration/document-work-assurance-v3/v3-cold-read-d8cc6d1.md` | no | the record commit `f3c0c07` |

`66133c6` is an amendment commit and `53fcf88` a free-channel application; neither is a round,
and neither spends `E9` budget. The four paths are the whole difference — in particular
`layer_path_check.py`, `test_precommit_checks.py` and `CONSTRUCTION-CHECKLIST.md` are
byte-unchanged since the previous read, which is what makes §3.2's citation sound.

## 2. The member set, and each member's blob

The member set comes from `E10`'s own sentence **at the subject blob** — ten paths, closing
with "and nothing else" — not from `LAYER`, not from the dispatch. Extracted mechanically from
the sentence and existence-checked one by one (§3.4). All ten read in full, none by citation:

| # | member | blob at `53fcf88` | lines |
|---|---|---|---|
| 1 | `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` | `87add4ce` | 212 |
| 2 | `ResearchSystem/document-harness/README.md` | `e1ea1412` | 38 |
| 3 | `ResearchSystem/document-harness/EXECUTION.md` | `4a7b6eca` | 465 |
| 4 | `ResearchSystem/document-harness/REVIEW.md` | `3350bfac` | 284 |
| 5 | `ResearchSystem/document-harness/ORCHESTRATION.md` | `1c9a705f` | 95 |
| 6 | `ResearchSystem/migration/document-work-assurance-v3/v3-harness-operating-contract.md` | `17ff31bb` | 5 |
| 7 | `ResearchSystem/migration/document-work-assurance-v3/v3-harness-review-contract.md` | `b576a45e` | 5 |
| 8 | `ResearchSystem/contract/Document-Work-Assurance-Contract-v3-supersession-1.md` | `68031fa2` | 124 |
| 9 | `ResearchSystem/contract/Document-Work-Assurance-Contract-v3-supersession-2.md` | `e1a2f26b` | 113 |
| 10 | `ResearchSystem/schema/document-assurance-v3/paragraph-map.schema.json` | `09aa8699` | 44 |

1 385 lines total. Three blobs moved since `d8cc6d1` and are stated here for the citation
channel: member 2 `5df14cdf` → `e1ea1412`, member 5 `ce37ae1a` → `1c9a705f` (and its length
92 → 95). The other seven are the digests the previous record already carries.

Every blob id above was produced by `git ls-tree -r 53fcf88` and independently reproduced by
`git hash-object` over the worktree copy, which is how the worktree was established as the
subject's bytes before any file was read.

`ResearchSystem/HARNESS-DECISIONS.md` (`9bbdb210`) is **not** a member (`HD-19`), and is owed at
this read by `E10`'s tail. Its `§live` was read in full — seven entries, `HD-44` / `HD-41` /
`HD-36` / `HD-35` / `HD-34` / `HD-23` / `HD-9`, :28–134. `§implemented` was probed, not read in
full: `HD-46` (this round's ruling), `HD-45`, `HD-38`, `HD-37`, `HD-32`, `HD-31`, `HD-30`,
`HD-25`, `HD-22`, `HD-21`, `HD-20`, `HD-19`, `HD-5`, `HD-2` were read because the subject's
carriers cite them. `HARNESS-RIDERS.md` was read in full, to keep this read from re-reporting
what is already banked — three of its rows cover findings I re-derived independently (§3.3).

**`E2`'s frozen bytes are untouched at the subject**, checked by inspection rather than by
report. `git ls-tree` returns `b2dbdf75` for the signed contract, `68031fa2` for supersession-1
and `e1a2f26b` for supersession-2 — the three digests `E2` names, unchanged — and the schema
pack enumerates to exactly the fifteen files `E2` re-baselined, `paragraph-map.schema.json`
among them. No frozen path appears in either commit's change set.

## 3. What I re-derived by command

### 3.1 The instrument's battery leg

`E3`'s measure-last, run at the subject from `ResearchSystem/tooling` because a run from the
repository root is the collection abort `EXECUTION.md` documents:

    $ python -m pytest -q
    712 passed in 92.14s (0:01:32)

Not owed by this read — a read lands one markdown record, which is doc-only — but run because
it is the one leg `EXECUTION.md` assigns to this repository, and it reproduces the previous
read's figure at a later subject.

### 3.2 Both membership guards still bind on the tenth member — mutation, not inspection

`R8` asks for the real defect shape, which here is *a member named in the sentence but absent
from the guard, so it is never scanned*. Mutation applied in-process to `layer_path_check.LAYER`
only; the worktree was never edited, and the tuple was compared against its pre-mutation copy
afterwards.

| state | `len(LAYER)` | `LayerMembership` | members the scan case reaches |
|---|---|---|---|
| baseline (negative control) | 10 | `ran=2 failed=0` | 10 BLOCKED lines, `ORCHESTRATION.md` among them |
| mutated — tenth member dropped | 9 | `ran=2 failed=2` | 9 BLOCKED lines, `ORCHESTRATION.md` **absent** |
| restored | 10 | `ran=2 failed=0` | identical to baseline; `tuple(LAYER) == ORIG` → `True` |

Re-run by hand rather than cited, even though the guard bytes are unchanged since the previous
read established the same result — the citation would have been sound (§1), and running it cost
seconds.

### 3.3 Full-stock path scan over all ten members

The shipped guard sees only staged added lines, so `unresolved_tokens` was driven over the
**whole** text of each member. Nine tokens do not resolve in this repository:

| member | tokens | class |
|---|---|---|
| `EXECUTION.md` | four caller battery scripts | already banked as `layer-crossrepo-token` |
| `EXECUTION.md` | two `assurance/runs/p5a-shells` audit-rounds, one `p4-doc` issue JSON | already banked as `layer-outbound-refs` |
| supersession-1, supersession-2 | `schema/document-assurance-v3/review.v2.schema.json`, `schema/` | already banked as `frozen-path-prefix`, and `E2`-frozen so unwritable without a ruling (`HD-20`) |

Two rather than the four `frozen-path-prefix` names, and the difference is a property of this
repository, not a repair: the rider's other two — `assurance/runs/` and `templates/run-v2/` —
resolve nowhere here (`ResearchSystem/assurance/runs/` does not exist in the instrument tree),
and a token that resolves nowhere is skipped by the guard as possibly illustrative.

Nine occurrences over six distinct paths, and no new member of this class. I extended the check
rather than repeat it: the **seven** distinct caller-side paths the layer names — those six plus
`ResearchSystem/tooling/rsc.py`, which the token regex cannot see because its backticks also
enclose `compile --check` — were resolved **against the caller worktree present on this
machine**, and all seven exist there. So the layer's cross-repo references are accurate as
caller paths, and only the guard's convention is at odds with them. That is a fact about this
machine, not about the repository, and is marked as such in §5.

### 3.4 The membership sentence, enumerated mechanically

`O-4` of the previous read banks the fact that the prose leg is unguarded, so the sentence was
enumerated rather than trusted: a regex over `E10`'s text up to "Its edits are" yields exactly
ten backticked paths, all ten resolve, and the numeral in the sentence reads "ten". The same
ten equal `LAYER` and equal `EXPECTED` — the three mirrors `E10-sync` tracks are in agreement at
ten, which is the compliance this round's touch of the sentence owed under `HD-22`.

### 3.5 The two must-fix answers, checked against the repository

- `M-2`'s replacement asserts that `dtw dispatch` has three modes, all review-side, none
  dispatching an executor. Re-derived from the `argparse` declaration itself, not from the
  commit body: the mutually exclusive required group is `--subject` (product run review),
  `--range` (construction round review), `--read` (E10 layer read). The claim holds.
- `M-1`'s replacement bullet now prohibits reviewing one's own round's work and routes the
  question of where the line runs to `E1`. Compared against `E1` at the subject: consistent.
  What it did **not** reach is `M-1`'s own class, one sentence into the same file — finding
  `M-1` below.
- The residual claim `M-2` left open, "no rule in this layer answers it either", was re-derived
  by scanning all ten members for mentions of either executor charter: 16 hits, matching the
  commit body's count. Fifteen are cross-references, counterpart lines or the membership
  enumeration. The sixteenth is not — observation `O-4` below.

## 4. Findings

Routing is not mine. `E10`, `R9` and `R10` decide it, and the `wl-route` rider records that for
a wording-level finding carrying bytes the routing is itself contested; `L-1` is another
instance of exactly that shape.

### M-1 (must-fix) — the charter still defines the orchestrator by the property the amendment deleted

**Location.** `ResearchSystem/document-harness/ORCHESTRATION.md` :3–4 (member 5, blob
`1c9a705f`), the file's opening sentence:

> Role instructions for the **orchestrator**: the session that runs a round without doing the
> work inside it.

**Ground truth.** `E1` at the subject (`87add4ce`) says the opposite of what that clause
implies: at :33, "orchestrator and executor are both the work side — the heading above binds
them in one breath", and at :30–31, for a session holding some but not all of `R1`'s four
holdings, it asks only that "the round **states in its record which of the four the executor
held**". `HD-46`'s recorded
tiebreak states the configuration this bound was written for in plain terms — one session
holding both the orchestrator and the executor role — and calls it today's actual shape.

The amendment at `66133c6` removed this exact claim from the file's prohibition list, where it
read "One session holds one role for its whole life (`E1`)", and replaced it with a bullet that
now says, at :89–91, "what a session holding **both work-side roles** owes in its record — is
`E1`'s to state". So the file as it stands contradicts itself: :3 defines the addressee as a
session that does not do the work, :90 contemplates the same session doing
it. The role table underneath reinforces :3 rather than :90 — the reviewer row explicitly
admits two carriers ("a full session **or** a subagent"), the orchestrator and executor rows
each name one, and the orchestrator's is "the one the user is talking to".

**Why this is the same class, not a new one.** The previous read swept `M-1` by the literal
sentence and named two further sites (`io-design.md`:33, left on that file's signature
precedent; a journal site, history). The sweep did not reach this one because the claim is
written in different words in the same file — and a newline falls between "without doing the"
and "work", so even a literal grep for the phrase misses it. Under `E7` and `HD-36` ① the
must-fix channel takes the same fix at every site of the defect the finding names; this is
that site.

**What changes if it stays.** A session holding both work-side roles — the shape actually in
use — can read :3 and conclude this file does not address it. That file is the sole carrier for
three obligations (delivering the instruction and stopping short of a decomposition, reading the
caller's policy file, taking the executor's report to the user), so the reading costs those
three their addressee. `E1`'s disclosure duty survives independently, because it lives in `E1`.

**Minimum fix.** Define the role positively and let `E1` hold the line, which is the contract
the amendment already adopted further down the same file. Bytes: replace "the session that runs a round
without doing the work inside it" with "the session that runs the round: transport, budget and
the review window". The role table's "starts the executor" needs no change under that wording;
whether the two carrier cells should also stop implying two sessions is a judgment I am not
making, because tightening them would add a bound and `E10` makes that design.

### L-1 (low, bytes supplied) — the corrected sentence in the harness README is right about the count and wrong about the scope

**Location.** `ResearchSystem/document-harness/README.md` :26 (member 2, blob `e1ea1412`), the
free-channel bytes applied at `53fcf88`:

> nine of its twelve obligations are already stated by rules **in this layer**

**Ground truth.** Eight of the nine cite-only rows cite rules in this layer (`E9` twice, `E10`,
`E11`, `E12`, `R5`, `R6`+`R1`, `R10`). The ninth cites `HD-2`, and the row saying so is in the
charter the same round wrote — `git show d8cc6d1` puts it there at :46, unchanged since, and it
reads "`HD-2`, which lives in the decision log — **outside this layer**, and reached through
`E10`'s standing `§live` obligation rather than through membership". So the sentence and the
member it describes disagreed from the moment both were written, and the free-channel commit,
which touched the sentence and the table on the same pass, corrected the numeral and left the
scope.

**What changes if it stays.** Read strictly, the sentence places the decision log inside the
instruction layer, which `E10`'s membership sentence denies in terms ("It is not a member: no
amendment machinery here reaches it") and `HD-19` ruled. The accurate fact is recoverable from
`ORCHESTRATION.md` :48 and from `E10` itself, which is why this is low rather than must-fix.

**Bytes.** `in this layer` → `elsewhere`. That leaves the sentence true of all nine and keeps
the point it is making (the charter names owners instead of restating rules). A longer variant
naming the split is available but adds words for no decision.

Member file, not `E2`-frozen. Whether it takes `E10`'s free channel or banks under `R9` is the
`wl-route` question, unchanged by this read.

### O-1 (observation) — the `L-3` fix repoints "lands unchanged" to a holding indexed to the executor

`ORCHESTRATION.md` :45 now reads "`R6` for the title; that it lands unchanged is `R1`'s
*reported through* holding, not `R6`'s text". `R1` indexes all four holdings to the executor
("Dispatched by, prompted by, scoped by and reported through **the executor** = executor
self-check"), so a session that is purely an orchestrator is not reached by that holding at all;
it is reached only in the dual-role shape. Meanwhile `R6`'s own verb split — "you write … the
orchestrator commits it" — does assign authorship to the reviewer and does reach a pure
orchestrator, so the property the previous read found absent from `R6` is arguably there by role
assignment rather than by the word "unchanged", which was what the grep tested. Harmless in the
configuration actually in use; naming a prohibition would add a clause, so no bytes are supplied.

### O-2 (observation) — the previous read's banked `O-1` does not survive re-derivation

`O-1` banks the claim that "the carrier formulation belongs to `HD-30`, not to `HD-2`". Three
decision entries attribute exactly that rule to `HD-2` in their own status lines — `HD-25`
("`HD-2` 要求 live→implemented 的挪节与实现它的 commit 同一个"), `HD-32` and `HD-37` (both
"`HD-2` 要求挪节与实现同 commit") — and `HD-2`'s own text carries "supersession 与挪节同
commit". The second half of `O-1`, that the row is silent on whose flip it is, is true of the
row but the fact is carried: the decision log's header invariant reads "只有用户能翻状态，
session 只能提议". Recorded so that redeeming `O-1` later does not repoint a citation that is
already correct.

### O-3 (observation) — `E10` is cited for a proposition it does not make

`ORCHESTRATION.md` :13: "`E10` forbids re-typing member text 'with the same content'". `E10`'s
clause reads "**Its edits** are additive or subtractive, never re-typed 'with the same
content'" — a rule about how the layer is amended, not about whether one member may restate
another's rule. The conclusion the sentence draws is independently carried by the `HD-5` half of
the same sentence, so nothing downstream changes; noted because `HD-46` ② uses the same phrasing,
which makes any correction here something to put to the user rather than to apply.

### O-4 (observation) — "no rule in this layer answers it either" is overstated for the product-run executor

`ORCHESTRATION.md` :32. `EXECUTION.md` :413–418, under *Instruction authoring rules*, requires
that "the rules the session runs under … live in `EXECUTION.md` and the governing plans; the
instruction references them from its non-normative Context section". That is a delivery path for
the product-run executor's charter, and combined with this file's own §*Handing the executor its
instruction* — the orchestrator delivers the instruction — the layer does answer the question for
that case. What stays unanswered is the construction executor's charter, which no rule routes to
anyone. This refines the banked `O-2` of the previous read rather than contradicting it; the
question itself remains `R5`'s.

### O-5 (observation) — `E1`'s new middle-state disclosure names no carrier and no owner

`E1` :30–31 requires that "the round **states in its record** which of the four the executor
held". Which record is not said — the commit body, the round journal and the preview card are
all live candidates, and `E3` sets the precedent of "the commit body or the round journal" for a
different obligation. `ORCHESTRATION.md`'s obligation table, which assigns nine obligations to
the orchestrator, does not carry this one, and `E1` sits under the *Execution side* heading that
binds orchestrator and executor jointly. So the newest bound in the layer has no named location
and no named actor. Naming either adds a clause and is design under `E10`, so no bytes.

## 5. Coverage, and what this read did not establish

**Read in full:** all ten members (1 385 lines), `HARNESS-DECISIONS.md` `§live`,
`HARNESS-RIDERS.md`, the previous read record `v3-cold-read-d8cc6d1.md`, and the full commit
bodies of `66133c6` and `53fcf88`.

**Read in part:** `HARNESS-DECISIONS.md` `§implemented` (fourteen entries probed by citation, not
read end-to-end); `layer_path_check.py`, `review_freeze_check.py`, `dispatch.py`'s read-dispatch
section and `cli.py`'s argument declarations, read to the extent the claims under check required.

**Probed only:** the caller repository. Eight paths — its five battery scripts, one
run-directory audit-rounds file, one triage-decision JSON, and the one review record `REVIEW.md`
cites — were existence-checked in the caller worktree that happens to sit on this machine. That establishes the tokens are accurate as
caller paths **here**; it establishes nothing about a fresh clone, and a reader who takes §3.3's
seven-of-seven as a repository property will over-trust it.

**Not established.** That the suite's 712 tests are sufficient for anything — mutation proves the
two membership tests bind, not that their force is enough (`R4`). That the amended text is
*good*, only that its two factual claims survive the commands that could falsify them. Any
process claim: that this read ran in a fresh context is marked, not verified, and the same is
true of the previous read whose findings I compared against. Whether `M-1`'s fix is worth its
round, or whether `L-1` takes the free channel — both are routing questions the rules give to
the user, and `R5` keeps me out of them.

**Not in the subject.** The caller repository holds a copy of at least one category-C review
record (`v3-review-full-fef3a2e.md`, the sole empirical basis `REVIEW.md` cites for *What is not
in the subject*) that does not exist in this repository. Whether that is a split residue is a
question about the split, not about the layer's bytes, and `layer-outbound-refs` already banks
the dead reference itself.
