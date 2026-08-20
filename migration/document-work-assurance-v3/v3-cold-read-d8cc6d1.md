# Cold read — the instruction layer at `d8cc6d1`

**No verdict.** A read is not a round (`R3`): it spends no budget, carries no verdict, and its
output is findings tiered must-fix / low / observation. This is the read `E10` owes over the
amendment text itself; nothing below certifies any text, and nothing below is banked as any
round's FULL.

**Findings: 2 must-fix, 3 low, 4 observations.** Both must-fix live in the round's own new
member, `ORCHESTRATION.md`, and both are the same shape — a line that cites a rule while
carrying content that rule does not have. `M-1` re-types, at :87, the exact `E1` sentence this
same commit deleted as false, and cites `E1` for it; the deleted sentence forbids the operating
mode `HD-46` records the user permitting in the same commit, so the charter as written is
violated by the round that wrote it. `M-2`'s claim that `dtw dispatch` hands the executor a
charter is refuted by the CLI: all three dispatch modes are reviewer- or reader-facing and no
mode dispatches an executor. The round's two headline claims were re-derived and **hold** — the
instrument's single battery leg returns `712 passed` at the subject, and both membership guards
bind on the new tenth member under mutation. The three lows all supply bytes, so they take
`E10`'s free channel; the observations bank.

---

## 1. Subject, re-derived

Derived from the repository, not from the dispatch. `HEAD` is the subject and the worktree is
clean, so every command below ran against bytes identical to the subject commit's:

    $ git rev-parse HEAD
    d8cc6d10deb023c8dfb744ea543b0450d49ab7e0
    $ git status --porcelain=v1
    (no output)

`E9`'s window, re-derived rather than assumed (`REVIEW.md`, *Where the result lives*): branch
tip equals the dispatched subject, so no commit landed between dispatch and this record.

The round is `V3-ORCHESTRATOR-CHARTER-v1`, its own first commit; its change set is eight paths,
of which three are instruction-layer members. Classified by hand from `git show --stat`, against
`E10`'s sentence rather than against any reported list:

| path | member? |
|---|---|
| `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` | yes (`E1`, `E10` amended) |
| `ResearchSystem/document-harness/README.md` | yes (two rows) |
| `ResearchSystem/document-harness/ORCHESTRATION.md` | yes — **new**, added at position 5 |
| `ResearchSystem/HARNESS-DECISIONS.md` | no (`HD-19`); owed at opening by `E10`'s tail |
| `ResearchSystem/HARNESS-RIDERS.md` | no |
| `ResearchSystem/document-harness/split-travel-manifest.md` | no |
| `ResearchSystem/tooling/hooks/layer_path_check.py` | no (guard mirror) |
| `ResearchSystem/tooling/tests/document_harness/test_precommit_checks.py` | no (guard mirror) |

## 2. The member set, and each member's blob

The member set comes from `E10`'s own sentence **at the subject blob** — ten paths, closing
with "and nothing else" — not from `LAYER`, not from the dispatch. All ten resolve at the
subject tree. Read in full, none by citation:

| # | member | blob at `d8cc6d1` | lines |
|---|---|---|---|
| 1 | `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` | `87add4ce` | 212 |
| 2 | `ResearchSystem/document-harness/README.md` | `5df14cdf` | 38 |
| 3 | `ResearchSystem/document-harness/EXECUTION.md` | `4a7b6eca` | 465 |
| 4 | `ResearchSystem/document-harness/REVIEW.md` | `3350bfac` | 284 |
| 5 | `ResearchSystem/document-harness/ORCHESTRATION.md` | `ce37ae1a` | 92 |
| 6 | `ResearchSystem/migration/document-work-assurance-v3/v3-harness-operating-contract.md` | `17ff31bb` | 5 |
| 7 | `ResearchSystem/migration/document-work-assurance-v3/v3-harness-review-contract.md` | `b576a45e` | 5 |
| 8 | `ResearchSystem/contract/Document-Work-Assurance-Contract-v3-supersession-1.md` | `68031fa2` | 124 |
| 9 | `ResearchSystem/contract/Document-Work-Assurance-Contract-v3-supersession-2.md` | `e1a2f26b` | 113 |
| 10 | `ResearchSystem/schema/document-assurance-v3/paragraph-map.schema.json` | `09aa8699` | 44 |

1 382 lines total. `HARNESS-DECISIONS.md` (`9bbdb210`) `§live` was read in full as well — seven
entries, `HD-44` / `HD-41` / `HD-36` / `HD-35` / `HD-34` / `HD-23` / `HD-9` (:28–134) — and
`§implemented`'s `HD-46`, `HD-45`, `HD-21`, `HD-22`, `HD-19`, `HD-2` were probed because this
round's carriers cite them.

**The citation channel is open for the next opening read**: every blob id above is stated, which
is `E10`'s stated precondition.

**Free-channel bytes riding this read.** `EXECUTION.md` changed between the last recorded
end-to-end read (`v3-cold-read-28501fe.md`) and this round's base — `git diff --name-only
28501fe 1d2d264` over the ten members returns exactly that one path. The applied bytes are the
prior read's `O-1`, and they read sound: a gitlink bump is not a prose/markdown path, so a
caller-side batch carrying one is never doc-only and the caller's five legs run at every bump.
The sentence also disclaims being a rule ("though not by any rule here"), which is the honest
form. No finding.

**`E2`'s frozen bytes are untouched at the subject**, checked by inspection rather than by
report: `git ls-tree` returns `b2dbdf75` for the signed contract, `68031fa2` for supersession-1
and `e1a2f26b` for supersession-2 — the three digests `E2` names, unchanged. No schema-pack path
appears in the change set.

## 3. What I re-derived by command

### 3.1 The battery leg

`E3`'s measure-last, run immediately before writing this section, from `ResearchSystem/tooling`
because a run from the repository root is the collection abort `EXECUTION.md` documents:

    $ python -m pytest -q
    712 passed in 97.78s (0:01:37)

Reproduces the round's claim at the subject itself.

### 3.2 Both membership guards bind on the new member — mutation, not inspection

`R8` asks for the real defect shape, which here is *a member named in the sentence but absent
from the guard, so it is never scanned*. Mutation was applied in-process to
`layer_path_check.LAYER` only; the worktree was never edited, and the tuple was compared
against its pre-mutation copy afterwards.

| state | `len(LAYER)` | `LayerMembership` result | members the scan case reaches |
|---|---|---|---|
| baseline (negative control) | 10 | `ran=2 failed=0` | 10 `BLOCKED` lines, `ORCHESTRATION.md` among them |
| mutated — tenth member dropped from `LAYER` | 9 | `ran=2 failed=2` | 9 `BLOCKED` lines, `ORCHESTRATION.md` **absent** |
| restored | 10 | `ran=2 failed=0` | identical to baseline (`tuple(L.LAYER) == ORIG` → `True`) |

Both tests fire: the equality (`E5`: the expectation is a hand-written literal, not the module's
own tuple) and the reachability case. The new member is genuinely guarded, not merely listed.

### 3.3 Full-stock path scan over all ten members

The shipped guard sees only staged added lines, so I drove `unresolved_tokens` over each
member's **whole** text at the subject. Nine hits, all pre-existing and all correctly
dispositioned by text that is already there:

- seven in `EXECUTION.md` — the caller-side battery scripts and two `assurance/runs/` paths.
  The file itself says "the five paths that follow are the caller's and do not resolve here",
  and I confirmed the sixth leg's script, `ResearchSystem/tooling/rsc.py`, likewise does not
  exist in this repository (`ResearchSystem/tooling/` holds `do-the-work.py` and `dtw.py` only),
  so the file's "none of those five scripts exists in the instrument" holds;
- two in the supersessions — `E2`-frozen bytes, which `HD-20` puts beyond both `E10` channels
  until a recorded ruling exists.

`ORCHESTRATION.md` contributes zero, so the round's stated ceiling — `layer_path_check` did not
run on this commit because this repository installs no hook — cost nothing here.

### 3.4 The membership sweep, re-run over the scope the round declared

`HD-41` ④ obliges the round to grep the assertion class and paste the output. The commit body
declares scope "every tracked `*.md` and `*.py` outside `document-harness/journal/`" and pastes
five hits. Re-run over exactly that scope (194 files from `git ls-files`), review records
excluded as the round excluded them, the same pattern returns **seven**:

    $ grep -n "nine members\|these nine paths\|九成员" $(git ls-files -- '*.md' '*.py' | grep -v '^ResearchSystem/document-harness/journal/')
    README.md:33
    README.md:50
    ResearchSystem/HARNESS-DECISIONS.md:402
    ResearchSystem/HARNESS-RIDERS.md:17
    ResearchSystem/HARNESS-RIDERS.md:32
    ResearchSystem/document-harness/io-design.md:8
    ResearchSystem/document-harness/io-design.md:42

The two `README.md` hits are the repository-root README, and they are missing from the pasted
output — `L-1`.

---

## 4. Findings

### M-1 (must-fix) — the charter re-types the `E1` sentence this commit deleted, and cites `E1` for it

**Location.** `ResearchSystem/document-harness/ORCHESTRATION.md` (`ce37ae1a`) :87–88, under
*What the orchestrator may never do*:

> - **Do the work, or review it.** One session holds one role for its whole life (`E1`). A
>   request that belongs to another role is flagged for the user to route, never absorbed.

**Ground truth it violates.** `E1` at the same commit (`87add4ce`, :21–34) does not contain
that sentence. This commit deleted it — `git diff` over the member shows `One session holds one
role for its whole life: work out at the start which role this session holds` removed, and
replaced by:

> The line one session may not cross is the one between the **work side** and the **review
> side**: orchestrator and executor are both the work side — the heading above binds them in one
> breath — so work out at the start which side this session is on, and a request that belongs to
> the other side is flagged for the user to route, never absorbed.

`HD-46` records the user's reason for that replacement in this same commit: the old wording was
false as written and "消掉字面读法下每一轮都违规的矛盾" — it was deleted precisely because, read
literally, every round violates it.

**Why it is not wording-level (`R9`).** The fix changes an actor's permission. `E1` now permits
one session to hold both work-side roles, subject to a record clause; `ORCHESTRATION.md` :87
forbids the orchestrator to do the work at all. `HD-46` states the mixed state is how every
round in this project actually runs, and the subject commit's own body discloses that this
round ran that way. So the charter, as written, is violated by the round that wrote it. The
file's own §thin makes the citation load-bearing — "Where a line below cites a rule, **that rule
is the text**" — so a cite carrying content its rule does not have is not a paraphrase, it is a
false attribution. `E10` puts the decision log above instruction text on conflict, so the
charter is what is wrong.

**Minimum fix.** Delete the sentence and its "another role" tail from :87–88, and let the
bullet's prohibition cite `E1`'s current line without re-typing it — the prohibition the
orchestrator is under is *review it*, and *do the work* belongs to the disclosure `E1` already
requires, not to a ban.

**The class, not the instance (`E7`, `HD-41` ④).** The deleted sentence survives at two further
sites outside the review records; I checked and name both so the fix is not narrowed to the
reported one:

- `ResearchSystem/document-harness/io-design.md:33` — "三角色与 `E1`「一个 session 一辈子只持一个
  角色」**相容**", now stale. **Disposition = leave**, on this same commit's own precedent for
  `io-design.md:8/:42`: the file is signed (`HD-35` binds blob `8f3c82c2`) and a substantive edit
  owes a re-signature; the shape rider `design-route` already carries that document class.
- `ResearchSystem/document-harness/journal/d-2026-08-01.md:29` — history, out of scope.

Only the member site is the must-fix.

### M-2 (must-fix) — `dtw dispatch` does not hand the executor a charter

**Location.** `ORCHESTRATION.md` :26–30:

> Why this role had no charter until now, and why that was not an oversight: the other two are
> **dispatched cold**, so something has to hand them a charter at startup, and `dtw dispatch`
> does.

**Ground truth it violates.** The CLI, re-derived rather than accepted:

    $ python ResearchSystem/tooling/dtw.py dispatch --help
    usage: do-the-work dispatch [-h] (--subject SUBJECT | --range RANGE | --read READ) ...
      --subject  PRODUCT run: the evidence commit — the only input needed
      --range    CONSTRUCTION round: BASE..TIP, the one thing no control plane records
      --read     E10 layer read: the commit whose instruction layer is the subject

All three modes are reviewer- or reader-facing, and their charters are review-side by
construction: `dispatch.py` sets `ROLE_INSTRUCTION = "document-harness/REVIEW.md"` and
`CONSTRUCTION_ROLE_INSTRUCTION = "migration/document-work-assurance-v3/v3-harness-review-contract.md"`,
and the three renderers' own docstrings read "The reviewer-facing prompt", "The reviewer-facing
prompt: the charter, the range, and nothing else" and "The reader-facing prompt". No mode
dispatches an executor, and no emitted prompt names `EXECUTION.md` or `CONSTRUCTION-CHECKLIST.md`
as an executor's charter. `E3` obliges a factual assertion written into instruction text to run
the command that could falsify it first; this one is refuted by that command.

**Why it is not wording-level.** The sentence is the file's justification for the shape of the
whole document, and it is what tells a reader that the executor's charter already has a carrier.
Combined with §*Handing the executor its instruction*, which scopes the orchestrator's delivery
to "the round's **instruction and subject**, and stops there", the layer as written leaves the
executor's role instruction handed over by nobody.

**Minimum fix.** Strike the claim as to the executor: `dtw dispatch` charters the **reviewer and
the reader**, which is what the constant and the three renderers say. The residue — who hands
the executor its charter — is `O-2` below, and answering it adds a clause, so it is not part of
this fix.

### L-1 (low, bytes supplied) — the repository-root README still says the layer has nine members

**Location.** `README.md` :33 and :50 (repository root; not a member, not `E2`-frozen).

    :33  ...three separate places hard-code the instruction layer's nine members as strings...
    :50  | Do the instruction layer's nine members resolve here? | python -c "... L.LAYER ..." |

**Bytes.** `nine` → `ten` at both lines. Nothing else on either line changes; ":33"'s "three
separate places" is still correct (the sentence, `LAYER`, `EXPECTED`).

The sweep evidence is §3.4: the round's own pattern over the round's own declared scope returns
seven hits, and these two are the pair the pasted output omits. `:50` is the sharper of the two
because it heads a table whose stated design is "run these, do not trust a sentence" — the
command it carries is correct and derives from `LAYER`, so a reader who runs it sees ten and is
told nine.

No round has relied on this text, so `E10`'s free channel is open.

### L-2 (low, bytes supplied) — `document-harness/README.md` miscounts the charter's obligations

**Location.** `ResearchSystem/document-harness/README.md` :26 (member 2), in the row added by
this commit: "nine of its **eleven** obligations are already stated by rules in this layer".

**Ground truth.** `ORCHESTRATION.md` carries nine cite-only rows under *The nine obligations
that are already law elsewhere* and three written-out ones under *The three obligations this
file is the text for*. 9 + 3 = 12. `ORCHESTRATION.md` itself states no total, and `HD-46` states
none, so the numeral has no other home to be right in.

**Bytes.** `eleven` → `twelve`.

Member file, not `E2`-frozen, no round has relied on the numeral → free channel.

### L-3 (low, bytes supplied) — the charter attributes "unchanged" to `R6`, which does not say it

**Location.** `ORCHESTRATION.md` :43: "commit the reviewer's record unchanged, under the title
the rule names | `R6`".

**Ground truth.** `R6` (`87add4ce`, :205–208) reads "you write … in the worktree; the
orchestrator commits it, title `V3-REVIEW-RECORD-<ROUND>-<sha>-v1`". `grep -n "unchanged"` over
the whole checklist returns exactly one line, `:125`, inside `E10`'s citation clause — the word
is nowhere in `R6`. Under the file's own "read the rule" contract an orchestrator that follows
the pointer finds no such requirement.

The property is real, and it does have a home: editing a returned record is the *reported
through* holding of `R1` / `E1`, which is what makes a reviewer non-independent.

**Bytes.** Change that row's right-hand cell from `` `R6` `` to `` `R6`; `R1` (the *reported
through* holding) ``. This corrects a pointer and adds no clause to any rule, so the design test
does not fire and the free channel holds.

I checked this class exhaustively rather than reporting the instance: all nine cite-only rows
were compared against their cited rules. Seven match (`E9` ×2, `E10`, `E11`, `E12`, `R5`, `R10`);
this row and the `HD-2` row (`O-1`) are the two that do not.

### O-1 (observation) — the `HD-2` row states a timing rule `HD-2` does not carry, and is silent on who may flip

`ORCHESTRATION.md` :46 assigns "flip a decision entry's state only in the commit that lands its
carrier" and cites `HD-2`. `HD-2` says "live / implemented / superseded / retired；同主题至多一条
live；supersession 与挪节同 commit；终态不可逆". The carrier formulation belongs to `HD-30`
(and its uses at `HD-45` / `HD-46`, "承载与建条同一个 commit"), not to `HD-2`. Separately, the
decision log's header carries "只有用户能翻状态，session 只能提议（`E1`/`R5`）", and the row —
which is an *orchestrator* obligation table — does not say the flip is the user's to decide.
Read as a timing constraint the row is harmless, which is why this banks rather than joining
`L-3`.

### O-2 (observation, `R5`) — the executor's charter has no carrier anywhere in the layer

Following from `M-2`. `EXECUTION.md` is the product-run executor's role instruction and
`CONSTRUCTION-CHECKLIST.md` is the construction executor's; nothing in the layer, and nothing in
the CLI, says who puts either in front of an executor at startup. `ORCHESTRATION.md`'s
§*Handing the executor its instruction* deliberately stops at "instruction and subject". Whether
a carrier should exist — a fourth dispatch mode, a clause in that section, or nothing at all
because the orchestrator already reads this file — is exactly the "should this thing exist"
question `R5` routes to the user, and adding one is design under `E10`. Reported, not concluded.

### O-3 (observation) — the root README's "is there a CLI?" command answers its own question wrongly

`README.md` :53 offers `ls ResearchSystem/tooling/rsc.py`. That path does not exist at the
subject: the directory holds `do-the-work.py` and `dtw.py`, and `split-travel-manifest.md` :57
records that `rsc.py` is the product compiler and deliberately did not travel. A row in a
section whose whole design is "carries commands instead of claims" returns a false negative.
Non-member, predates this round, and the fix is a byte swap someone should make while `L-1` is
in that same file — but I am not naming it as `L-1`'s bytes, because it is a different defect.

### O-4 (observation) — the prose leg of the membership sentence is still unguarded at ten members

Independently re-derived rather than taken from rider `E10-sync`: `grep -rn` over
`ResearchSystem/tooling/tests/` finds no test that reads `CONSTRUCTION-CHECKLIST.md`'s `E10`
sentence. The only assertions are `LAYER == EXPECTED` and per-member scan reachability, both
over hand-written path tuples (§3.2). A path silently dropped from the sentence — or the
sentence's self-count left at "nine" — is caught by nothing mechanical. This is the exposure
`E10-sync` banks and `HD-22` ruled against mechanizing (`E6`), so it is correctly banked;
recorded here only so this read's coverage of the guard question is legible.

---

## 5. Coverage, and what this read did not establish

- **Read in full at the subject blobs:** all ten members, 1 382 lines, none by citation (§2);
  `HARNESS-DECISIONS.md` `§live` (:28–134) in full, plus six `§implemented` entries probed.
- **Read in full outside the layer:** `ResearchSystem/tooling/hooks/layer_path_check.py`,
  `ResearchSystem/tooling/tests/document_harness/test_precommit_checks.py` `LayerMembership`,
  `ResearchSystem/tooling/rsclib/document_harness/dispatch.py` §construction and §read, the
  repository-root `README.md` :1–55, and the subject commit's full body.
- **Probed only:** `ResearchSystem/document-harness/io-design.md` (grepped for the two classes
  `M-1` and §3.4 name; not read end to end — it is not a member and declares in its own header
  that it has authority over no rule), `HARNESS-RIDERS.md` (rows `E10-sync` and `pin-drift`),
  the rest of `HARNESS-DECISIONS.md` `§implemented`.
- **Not read:** the review-record corpus under this directory, except the immediately prior
  read's header for the record-naming precedent.
- **Commands re-run:** the instrument's battery leg (§3.1), the guard mutation with its negative
  control and its restore check (§3.2), a full-stock path scan over all ten members (§3.3), the
  membership sweep over the round's declared scope (§3.4), and `git ls-tree` for every blob id in
  §2. Every figure above comes from a command in this session; none is carried from the
  dispatch, the commit body, or another record.

**`UNVERIFIABLE`, stated rather than folded in (`R4`).** `ORCHESTRATION.md`'s §*Reading the
caller's policy file* asserts that a caller's agent-facing entry file is "the only discovery path
a cold orchestrator has". That is a claim about repositories outside this one and has no evidence
lock here; I did not establish it either way, and it is not counted as supported.

**Two facts about how this read was carried out, recorded because `R2` makes chat-only
load-bearing material a finding.**

1. As in the previous read, the dispatch prompt carried **one hand-added line** beyond the CLI's
   text, naming which repository the paths are relative to. I reproduced the generated prompt
   (`dtw dispatch --read d8cc6d10…`) and confirmed the rest is `READ_PROMPT` verbatim. The extra
   line is transport, not scope — the question was still set by the repository — but it was
   handed over rather than derived.
2. Reproducing that prompt **rewrote the freeze marker** `.harness/review-pending.json`. The file
   is untracked and gitignored here (`git status --ignored` returns `!! .harness/`), its
   `subject` field is unchanged and equals the dispatched subject, and only `dispatched_at` moved
   — to `2026-08-18T08:29:01+00:00`. `E9`'s window was re-derived from branch tip versus subject
   (§1) rather than from the marker, so nothing above depends on it. The marker is left in place
   for the act that commits this record to delete.

**Process claims are marked, not verified (`R4`).** That this read ran in a fresh context, and
that the reader held none of `R1`'s four holdings beyond being dispatched and prompted, are
claims with no evidence lock at any revision.
