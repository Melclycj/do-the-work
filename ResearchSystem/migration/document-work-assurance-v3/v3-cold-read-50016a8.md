# Cold read — the instruction layer at `50016a8`

**No verdict.** A read is not a round (`R3`): it spends no budget, carries no verdict, and its
output is findings tiered must-fix / low / observation. This read discharges two obligations at
once, both owed by `E10`: the independent re-read of the amendment committed at `14e8f16` (the
answer to the previous read's single must-fix), and the layer read the free-channel bytes of
`50016a87` ride. Nothing below certifies any text, and nothing below is banked as any round's
FULL.

Named `cold-read` rather than `checkpoint-read` because all ten members were read end-to-end at
the subject blobs and every blob id is stated below, which is what keeps `E10`'s citation
channel open for the next round's opening read.

**Findings: 0 must-fix, 1 low, 4 observations.** The amendment's answer **holds** and its class
is now clean: the replacement bytes landed verbatim, and a property-based sweep over the ten
members for the deleted claim returns zero hits inside the layer. The free-channel byte at
`50016a87` also holds. The one low is in the row that free-channel commit reasoned *from*:
`ORCHESTRATION.md` :48 says `HD-2` is "reached through `E10`'s standing `§live` obligation",
and `HD-2` sits in `§implemented`, the section the mandatory read excludes.

---

## 1. Subject, re-derived

Derived from the repository, not from the dispatch. `HEAD` is the subject and the worktree is
clean, so every command below ran against bytes identical to the subject commit's. Taken before
anything was read and again after the last measurement, with nothing but this untracked file
changed in between:

    $ git rev-parse HEAD
    50016a87a5f4351f2bcee18c368ae36961902dbe
    $ git status --porcelain
    (no output)

`E9`'s window, re-derived rather than assumed (`REVIEW.md`, *Where the result lives*): branch
tip equals the dispatched subject, so no commit landed between dispatch and this record. The
freeze marker `.harness/review-pending.json` was read, not written — its `subject` is the
dispatched commit and its `dispatched_at` is `2026-08-18T09:04:46+00:00` — but nothing above
depends on it, because the window was derived from tip-versus-subject.

Two commits separate this subject from the previous read's (`53fcf88`). Classified by hand from
`git diff --name-only 53fcf88 50016a87`, against `E10`'s sentence rather than any reported list:

| path | member? | which commit |
|---|---|---|
| `ResearchSystem/document-harness/ORCHESTRATION.md` | yes | `14e8f16` (the amendment, `M-1`) |
| `ResearchSystem/document-harness/README.md` | yes | `50016a87` (free channel, `L-1`) |
| `ResearchSystem/migration/document-work-assurance-v3/v3-cold-read-53fcf88.md` | no | the record commit `d0e523d` |

Three paths, and that is the whole difference. `14e8f16` is an amendment commit and `50016a87`
a free-channel application; neither is a round and neither spends `E9` budget. Both are
one-line diffs (`2 insertions, 2 deletions` over one wrapped sentence; `1 insertion, 1
deletion`), and I read both diffs rather than the commit bodies' description of them.

## 2. The member set, and each member's blob

The member set comes from `E10`'s own sentence **at the subject blob** — ten paths, closing
with "and nothing else" — not from `LAYER`, not from the dispatch. Extracted mechanically from
the sentence (§3.1) and existence-checked one by one. All ten read in full, none by citation:

| # | member | blob at `50016a87` | lines |
|---|---|---|---|
| 1 | `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` | `87add4ce` | 212 |
| 2 | `ResearchSystem/document-harness/README.md` | `2de6f0aa` | 38 |
| 3 | `ResearchSystem/document-harness/EXECUTION.md` | `4a7b6eca` | 465 |
| 4 | `ResearchSystem/document-harness/REVIEW.md` | `3350bfac` | 284 |
| 5 | `ResearchSystem/document-harness/ORCHESTRATION.md` | `435a12e5` | 95 |
| 6 | `ResearchSystem/migration/document-work-assurance-v3/v3-harness-operating-contract.md` | `17ff31bb` | 5 |
| 7 | `ResearchSystem/migration/document-work-assurance-v3/v3-harness-review-contract.md` | `b576a45e` | 5 |
| 8 | `ResearchSystem/contract/Document-Work-Assurance-Contract-v3-supersession-1.md` | `68031fa2` | 124 |
| 9 | `ResearchSystem/contract/Document-Work-Assurance-Contract-v3-supersession-2.md` | `e1a2f26b` | 113 |
| 10 | `ResearchSystem/schema/document-assurance-v3/paragraph-map.schema.json` | `09aa8699` | 44 |

1 385 lines total. Two blobs moved since `53fcf88` and are stated here for the citation
channel: member 5 `1c9a705f` → `435a12e5` (length unchanged at 95), member 2 `e1ea1412` →
`2de6f0aa`. The other eight are the digests the previous record already carries. Every id above
is `git ls-tree -r 50016a87` output; the worktree was established as the subject's bytes by the
clean `status` in §1 before any file was read.

`ResearchSystem/HARNESS-DECISIONS.md` is **not** a member (`HD-19`) and is owed at this read by
`E10`'s tail. Read in full rather than by section: `§live`'s seven entries (`HD-44` / `HD-41` /
`HD-36` / `HD-35` / `HD-34` / `HD-23` / `HD-9`, :28–134), the header's state machine and
admission rules (:1–26), and all of `§implemented` (:135–460) — the last is beyond what `E10`
and `HD-5` oblige, and it is what produced the low below. `HARNESS-RIDERS.md` was read in full
so that this read would not re-report what is banked; five of its rows (`E10-sync`,
`frozen-path-prefix`, `layer-crossrepo-token`, `layer-outbound-refs`, `pin-drift`) cover ground
I re-derived independently, and one (`wl-route`) governs the routing of my own low.

**`E2`'s frozen bytes are untouched at the subject**, checked by inspection rather than by
report. `git ls-tree` returns `b2dbdf75` for the signed contract, `68031fa2` for supersession-1
and `e1a2f26b` for supersession-2 — the three digests `E2` names, unchanged — and
`ResearchSystem/schema/document-assurance-v3/` enumerates to exactly fifteen files, the
re-baselined pack, `paragraph-map.schema.json` among them. No frozen path appears in either
commit's change set.

## 3. What I re-derived by command

### 3.1 The three membership mirrors agree at ten

`E10-sync` banks the fact that the prose leg is unguarded, so the sentence was enumerated
rather than trusted. A regex over `E10`'s text up to "Its edits are", run against the blob at
the subject, yields exactly ten backticked `.md`/`.json` paths in the order the sentence writes
them; the sentence's own numeral reads `exactly these ten paths`; and

    tuple(paths_from_sentence) == tuple(layer_path_check.LAYER)   ->  True

`EXPECTED` in `tests/document_harness/test_precommit_checks.py` :163–174 is the same ten in the
same order, hand-written as `E5` requires. So the three sites `HD-22` obliges a
membership-touching batch to change together are in agreement at ten, with `ORCHESTRATION.md`
at position 5 in all three.

### 3.2 Both membership guards bind on the tenth member — mutation, not inspection

`R8` asks for the real defect shape, which here is *a member named in the sentence but absent
from the guard, so it is never scanned*. Mutation applied in-process to `layer_path_check.LAYER`
only; the worktree was never edited, and both files' sha256 were compared before and after.

| state | `len(LAYER)` | `LayerMembership` | members the scan case reaches |
|---|---|---|---|
| baseline (negative control) | 10 | `ran=2 failed=0` | 10 BLOCKED lines, `ORCHESTRATION.md` among them |
| mutated — tenth member dropped | 9 | `ran=2 failed=2` | 9 BLOCKED lines, `ORCHESTRATION.md` **absent** |
| restored | 10 | `ran=2 failed=0` | identical to baseline |

    tuple(L.LAYER) == ORIG          ->  True
    worktree bytes unchanged        ->  True   (sha256 over the module and the test file)

Both tests fire on the mutation, not one: the hand-written equality and the per-member scan
reachability. Re-run by hand rather than cited even though the guard bytes are unchanged since
two prior reads established the same result — the citation would have been sound, and running
it cost seconds.

### 3.3 Full-stock path scan over all ten members

The shipped guard sees only staged added lines, so `unresolved_tokens` was driven over the
**whole** text of each member at the subject. Nine tokens over six distinct paths do not
resolve in this repository, and every one is already banked:

| member | tokens | banked as |
|---|---|---|
| `EXECUTION.md` | four caller battery scripts | `layer-crossrepo-token` |
| `EXECUTION.md` | two `assurance/runs/p5a-shells` audit-rounds, one `p4-doc` issue JSON | `layer-outbound-refs` |
| supersession-1, supersession-2 | `schema/document-assurance-v3/review.v2.schema.json`, `schema/` | `frozen-path-prefix`, and `E2`-frozen (`HD-20`) |

`ORCHESTRATION.md` contributes zero, unchanged from the previous read. No new member of this
class, and the two commits under read added no path token at all.

### 3.4 The claims `EXECUTION.md` and `README.md` make about this repository

`E3` obliges a factual assertion written into instruction text to run the command that could
falsify it. Four such assertions were re-derived, none accepted from a commit body:

- *"none of those five scripts exists in the instrument"* (`EXECUTION.md` :348). `git cat-file
  -e` at the subject for each of `tooling/tests/run_tests.py`, `run_p4_tests.py`,
  `run_p5a_tests.py`, `schema/fixtures/validate_fixtures.py` and `tooling/rsc.py` — **five of
  five ABSENT**. Holds, and holds for the sixth-leg script `rsc.py` named in the same bullet.
- *"this repository … installs no hook at all"* (`README.md` :34). `git config --get
  core.hooksPath` exits 1 (unset), and this worktree's git dir holds only `hooks/*.sample`.
  Holds.
- *"It guards this layer's ten members"* (`README.md` :34). `len(LAYER) == 10` (§3.1). Holds.
- The instrument's single battery leg, run last, from `ResearchSystem/tooling` because a run
  from a root that also carries the product is the collection abort the same section documents:

      $ python -m pytest -q
      712 passed in 102.58s (0:01:42)

  Not owed by this read — a read lands one markdown record, which is doc-only under
  *Regression-battery tiering* — but run because it is the one leg that section assigns to this
  repository, and it reproduces the `712` the section and `HD-45` both state, at a later
  subject and a different wall time.

### 3.5 The amendment's answer, and its class

**The bytes.** `git diff 53fcf88 50016a87` over member 5 shows exactly the replacement the
previous read supplied, and nothing else: "the session that runs a round without doing the work
inside it" → "the session that runs the round: transport, budget and the review window". Taken
verbatim, including the reader's note that `E1` holds the line about what a session may not
also be — `ORCHESTRATION.md` :89–91 already points there.

**The class, swept by property rather than by string.** The previous sweep missed the site
because it looked for a sentence; I looked for the claim. Scope declared before the command
(`HD-41` ①): every tracked `*.md`, `*.py` and `*.json`, excluding the review-record corpus under
`migration/document-work-assurance-v3/v3-*` and `document-harness/journal/`.

    $ grep -rniE "without doing|does not do the work|one role for its whole life|一辈子|只做传输|not the one doing|never does the work" <that scope>
    ResearchSystem/HARNESS-DECISIONS.md:155   — HD-46 quoting the old wording as history
    ResearchSystem/document-harness/io-design.md:29
    ResearchSystem/document-harness/io-design.md:33

**Zero hits inside the ten members.** The `HARNESS-DECISIONS.md` hit is `HD-46` recording what
was replaced and is correct as history. The two `io-design.md` hits are the signed design
document, left on the precedent this round has now applied three times (`HD-35` binds blob
`8f3c82c2`, a substantive edit owes a re-signature, rider `design-route` carries the class);
:29 is disclosed in `14e8f16`'s body, :33 was named and dispositioned *leave* by the first read
of this round. I take no position on that disposition — it is the user's.

**The residual claim the fixed sentence sits beside.** `ORCHESTRATION.md` :26–32 asserts that
`dtw dispatch`'s three modes are review-side and that none dispatches an executor, and that no
dispatch prompt names the orchestrator. Re-derived from the code, not the record:
`cli.py` :144/:158/:167 branches on `--range` (construction round review), `--read` (E10 layer
read) and `--subject` (product run review); `dispatch.py` sets `ROLE_INSTRUCTION =
"document-harness/REVIEW.md"` and `CONSTRUCTION_ROLE_INSTRUCTION =
"migration/document-work-assurance-v3/v3-harness-review-contract.md"`, and `grep -rn
"ORCHESTRATION\|orchestrator"` over `ResearchSystem/tooling/` returns two source hits, both the
member path inside `LAYER` and `EXPECTED`, and none inside any prompt constant. Both claims
hold.

### 3.6 The free-channel byte at `50016a87`

`in this layer` → `elsewhere` in `README.md` :26, and nothing else on the line. Checked against
the thing it describes: the charter's nine cite-only rows cite `E10`, `E11`, `E12`, `E9` twice,
`R6`+`R1`, `R10`, `R5` and `HD-2` — all outside `ORCHESTRATION.md`, and the ninth outside the
layer, which is what made the previous word false and this one true. The `twelve` is the
charter's own 9 + 3 section split, and `ORCHESTRATION.md` still states no total of its own, so
the numeral has no other home to be right in. The byte holds. The row it reasons from does not
— finding `L-1`.

### 3.7 The dispatch prompt I was handed

`R2` makes chat-only load-bearing material a finding, so the prompt was checked against the
repository instead of reproduced by re-running the generator (which would have rewritten the
freeze marker). `ResearchSystem/tooling/tests/fixtures/expected-read-prompt.txt` is
`READ_PROMPT` verbatim, and the prompt I received equals it with `{charter}` =
`ResearchSystem/migration/document-work-assurance-v3/v3-harness-review-contract.md` (which is
`CONSTRUCTION_ROLE_INSTRUCTION` resolved by `instrument_relative`) and `{commit}` = the subject
SHA. One line beyond it was hand-added, naming which repository the paths are relative to and
disclaiming itself as instruction — the same extra line the two previous reads of this round
record. It is transport, not scope: the member set, the subject bytes and the report shape all
came from the repository. Recorded rather than folded in.

## 4. Findings

Routing is not mine. `E10`, `R9` and `R10` decide it, and rider `wl-route` records that for a
finding of exactly this shape — below must-fix, bytes supplied — the route is itself contested.

### L-1 (low, bytes supplied) — the charter's `HD-2` row states a delivery path that the layer's own read rules do not provide

**Location.** `ResearchSystem/document-harness/ORCHESTRATION.md` :48 (member 5, blob
`435a12e5`), the ninth row of *The nine obligations that are already law elsewhere*:

> | flip a decision entry's state only in the commit that lands its carrier | `HD-2`, which
> lives in the decision log — outside this layer, and reached through `E10`'s standing `§live`
> obligation rather than through membership |

**Ground truth.** `HD-2` is not in `§live`. `HARNESS-DECISIONS.md` at the subject puts `§live`
at :28–134 with seven entries (`HD-44`, `HD-41`, `HD-36`, `HD-35`, `HD-34`, `HD-23`, `HD-9`),
opens `## §implemented` at :135, and `HD-2` is at :421 inside it. What `E10`'s tail obliges is
that one file's `§live` and nothing more — "`ResearchSystem/HARNESS-DECISIONS.md`'s `§live`,
the user's standing rulings" — and both other carriers of that obligation say the same in
narrower terms: `README.md` :29, "every cold read MUST read its `§live` (**and only §live**)",
and `HD-5`, "`§implemented` 与 archive 不在必读内". The `§implemented` heading itself says how
those entries are reached: "不必读，grep 可达". So the route the row names does not reach the
rule the row cites.

**What changes if it stays.** The row is in a table whose stated contract is that it assigns
obligations and does not restate them — "read the rule" — which makes the pointer the
load-bearing part of the cell. An orchestrator that discharges the opening obligation as
written, reading `§live`, is told by this row that it has thereby reached `HD-2`, and has not;
the entry is reachable only by a grep the row says is unnecessary. The obligation itself
survives, because the row's left cell states it, and the rule's substance is additionally
carried by the decision log's header state machine ("supersession 与 live→implemented 的挪节都
在同一 commit"), which sits above `§live` and is passed on the way in. That is why this is low
and not must-fix: what is wrong is the route, not the obligation, and the accurate fact is one
heading away in a file the same opening already opens.

**Bytes (minimum fix).** Delete the clause: end the cell at "`HD-2`, which lives in the decision
log — outside this layer". Pure deletion, which `E10`'s channels admit in terms, and it leaves
the true half — that this obligation is not reached through membership — standing. An
informative variant is available and I name it without preferring it, because it states a fact
the minimum fix does not have to: "…outside this layer, in `§implemented`, so it is reached by
grep rather than through membership or the `§live` read." Either way no clause is added to any
rule and nothing a rule requires changes, so the design test does not fire.

Member file, not `E2`-frozen, and no round has relied on the sentence — the free-channel
conditions read as open, but whether it takes that channel or banks under `R9` is `wl-route`'s
open question, unchanged by this read. If it does take the channel, `wl-route`'s own deadline —
"下一份对 wording-level finding 供字节的 read 记录" — is worth checking against this record.

### O-1 (observation) — the amendment's fix leaves the file relying on a fourth party its three-role table does not carry

`ORCHESTRATION.md` :18–24 is headed *The three roles* and carries exactly three rows:
orchestrator, executor, reviewer. `M-2`'s replacement at :26–29, one line below the table, now
reads "the **reviewer and the reader** start cold from a dispatch" — correctly, since
`dtw dispatch --read` is a mode and `R3` says a read is not a round at all. The reader is
therefore a party the layer dispatches, charters and receives records from, and the file's own
model of who does what has no row for it. The orchestrator row is the other half of the same
gap: it lists "starts the executor, dispatches the reviewer" and not the reader, while the
obligation table's first row assigns that same orchestrator the round's opening cold read,
which `E10` requires to be independent when its subject is an amendment. Nothing goes wrong
today — the reader learns its duties from `REVIEW.md` and `CONSTRUCTION-CHECKLIST.md`, not from
this file, and `R3` defines the read — so this is recorded rather than fixed. Adding a fourth
row, or a clause to the orchestrator cell, would add a bound; `E10` makes that design, so no
bytes.

### O-2 (observation) — three of the nine cite-only rows drop a qualifier the cited rule carries

The class the previous read swept was *a row whose cite does not carry the content*; this is the
adjacent one, *a row that carries the content without its exemption*. All nine rows were
compared against their rules at the subject:

- :40 "open the round with the layer's cold read" — `E10` says "at each round's opening
  **unless the user waives it**";
- :41 "render the preview card before the round, and wait for the user" — `E11` says "Wait for
  the user **unless told otherwise**";
- :46 "before closeout, put **each** low's spend-the-fix-leg / bank choice to the user" — `R10`
  scopes this to "**A FULL returning `REVIEWED_NO_BLOCKER`** with lows" and interposes a step
  the row drops ("weighs each low's deadline against its touch trigger").

All three compressions make the row stricter than the rule, which is the safe direction, and
the file's own §thin sends the reader to the rule for the text. Recorded because rider
`waiver-live` already banks a live dispute about the first of the three, and because a reader
who takes the table as the obligation's statement — which its "This table assigns them" invites
— gets a stricter duty than the layer imposes. No bytes: restoring a qualifier to a summary
cell is a judgment about how much a compression may compress, and `R5` keeps me out of it.

### O-3 (observation) — an `R9` ride that came due in this round and was not taken, because `R9`'s channel files nothing to come due

`v3-cold-read-ae4df09.md` `W-1` reported that supersession-2 asserts UNSIGNED **twice** — :3
(top of file) and :107 (§5 *Signature*, "This file is **UNSIGNED**.") — while the correctives
scope the residue to the top-of-file line only: `README.md` :19 says "the carrier's top-of-file
UNSIGNED line". It filed the finding wording-level, explicitly "no rider row, no round", with
its minimum fix named: "when a batch next touches `README.md` or the signature record: replace
'top-of-file' with a both-lines scope (`:3` and `:107`/§5)". I re-derived the underlying fact
rather than accepting it — `grep -rn "UNSIGNED"` over the contract and harness documents
returns exactly those two carrier lines plus the two README rows — and it still stands at this
subject.

Two commits of this round touched `ResearchSystem/document-harness/README.md` (`53fcf88`,
`50016a87`), and one of them edited the row three lines below `:19`. The ride condition arrived
twice and was not taken. The reason is structural rather than anyone's lapse: `R9` says a
wording-level finding "rides the next batch touching this layer" and `R10` gives the bank one
row per rider, so a finding routed to `R9` alone leaves no enumerable trace — the batch that
would redeem it has nothing to consult but the review-record corpus. Whether that channel
should have a carrier is a "should this exist" question, so `R5` routes it to the user and I do
not answer it. The residue itself remains as `ae4df09` left it: harmless, because `README.md`
:19 leads with "signed 2026-07-30" and names the signature record, and supersession-2 §5's own
closing sentence sends the reader to that record.

### O-4 (observation, probed on this machine only) — a fourth prose site for the member count, outside the three `HD-22` names

`HD-22`'s discipline is that a batch touching the membership sentence changes three sites
together, and this round did (§3.1). A fourth site exists and is not among them, because it
lives in the caller repository: `.githooks/pre-commit` :42 in the caller worktree present on
this machine reads "The third, `layer_path_check.py`, guards the **nine** instruction-layer
members, and after that deletion 0 of the 9 resolve here". The harness-side mirror of the same
paragraph, `README.md` :34, was updated by this round to "this layer's **ten** members" while
correctly keeping its historical count in the past tense ("0 of the 9 it then had"); the caller
sentence states its count in the present tense and is now stale. Nothing fires on it — the
check it describes is unwired there and installed nowhere here — and riders `pin-drift` and
`mount-inert` already bank the general shape of caller-side wiring drifting from the
instrument, though neither names this count. **This is a fact about this machine's caller
worktree, not about the repository under read**, and a reader who takes it as a repository
property will over-trust it.

## 5. Coverage, and what this read did not establish

**Read in full at the subject blobs:** all ten members, 1 385 lines, none by citation (§2).

**Read in full outside the layer:** `ResearchSystem/HARNESS-DECISIONS.md` end to end (header,
`§live`, `§implemented`), `ResearchSystem/HARNESS-RIDERS.md`, both prior read records of this
round (`v3-cold-read-d8cc6d1.md`, `v3-cold-read-53fcf88.md`), the full commit bodies of
`14e8f16` and `50016a87`, and
`ResearchSystem/tooling/tests/fixtures/expected-read-prompt.txt`.

**Read in part:** `layer_path_check.py` (the `LAYER` tuple and `unresolved_tokens`),
`test_precommit_checks.py` (`LayerMembership`), `dispatch.py`'s read and construction sections
and its role-instruction constants, `cli.py`'s dispatch branch — each to the extent the claim
under check required, not end to end.

**Probed only:** the caller repository on this machine — its `.githooks/pre-commit` (`O-4`) and
its `CLAUDE.md` :25, which does point at `ResearchSystem/HARNESS-POLICY.md`. That last one is
one confirming instance of the mechanism `ORCHESTRATION.md` :70–71 describes; it is **not**
evidence for that sentence's stronger claim, that the caller's entry file is "the only
discovery path a cold orchestrator has", which remains `UNVERIFIABLE` here exactly as the first
read of this round left it.

**Grep scopes, declared (`HD-41` ①).** §3.5's class sweep ran over every tracked `*.md`, `*.py`
and `*.json` excluding `migration/document-work-assurance-v3/v3-*` and
`document-harness/journal/`; §3.3's path scan ran over the whole text of the ten members and
nothing else; §3.4's five-script check ran against the subject tree, not the worktree. No
absolute quantifier above is claimed beyond the scope stated with it.

**Not established.** That the suite's 712 tests are sufficient for anything — mutation proves
the two membership tests bind, not that their force is enough (`R4`). That the amended sentence
is *good*, only that it is the bytes the previous read supplied and that its class is now empty
inside the layer. That `io-design.md`'s two surviving sites are correctly left; that is a
disposition the user made and `R5` keeps me out of it. Whether `L-1` takes the free channel or
banks, and whether `O-3`'s channel needs a carrier — both are routing and "should this exist"
questions the rules give to the user.

**Process claims are marked, not verified (`R4`).** That this read ran in a fresh context, and
that the reader held none of `R1`'s four holdings beyond being dispatched and prompted, are
claims with no evidence lock at any revision. The one hand-added line on the dispatch prompt is
recorded at §3.7 rather than left implicit, because `R2` makes chat-only load-bearing material
a finding and the only honest way to show it was not load-bearing is to say what it was.
