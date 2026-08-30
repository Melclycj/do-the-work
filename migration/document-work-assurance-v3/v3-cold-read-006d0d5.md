# Instruction-layer read — subject `006d0d53b6f441b2a1a7ad5c454224530ee380d7`

An `E10` read, at the opening of round 3 `CORE-ONLY-RUN` of batch `CORE-ONLY`. **Not a round**:
no budget spent, no verdict carried, output is findings tiered must-fix / low / observation
(`R3`). Dispatched with the charter `document-harness/CONSTRUCTION-CHECKLIST.md` — this
repository's own rule file, declared under `rules` in `harness.json` at its root — which was read
in full, and then the counterpart *that* file names, `document-harness/RULES.md`, also in full.

Record name: `v3-cold-read-`. `R6` offers two read filenames and the layer still defines no
criterion for choosing between them (rider `read-name-split`, open). I took `cold-read` for the
reason every previous whole-layer opening record took it — the subject is the layer at a round's
opening.

**Findings: 0 must-fix, 2 low, 2 observation.**

---

## 1. The member set and the coverage, both derived — not received

The dispatch enumerated no members and handed me no member table (`R2`). Its addendum named plan
ruling 43 and told me to derive the coverage myself; I did, and I state below where my derivation
agrees with that ruling and where I checked rather than accepted it.

`E10`'s own sentence at the subject (`document-harness/RULES.md:86-94`) reads **exactly seven
paths**. All seven resolve at the subject — `git cat-file -t 006d0d5:<path>` returned `blob` for
each, run here. Blob ids from `git ls-tree -r 006d0d5`, run here:

| # | member | blob at `006d0d5` | last recorded end-to-end read | this read |
|---|---|---|---|---|
| 1 | `document-harness/RULES.md` | `5ab152ad0aa3595bb6c601e51f4388324c259543` | `v3-cold-read-e88094c.md`, blob `47a7fbe1…` — **moved** | **end to end** |
| 2 | `document-harness/README.md` | `7decb095ff8d93aa209f460805465288f7f973cf` | `v3-cold-read-e88094c.md`, blob `5586b066…` — **moved** | **end to end** |
| 3 | `document-harness/EXECUTION.md` | `08fa87f8380b60a0af4e125e1bfe88747d26f0e4` | `v3-cold-read-e88094c.md`, **same blob** — unmoved | covered by citation |
| 4 | `document-harness/REVIEW.md` | `71707a3a01016e86b63238d494df98abbd2408c3` | `v3-cold-read-e88094c.md`, **same blob** — unmoved | covered by citation |
| 5 | `document-harness/ORCHESTRATION.md` | `3f9cd61ca42c94ca2a3080d13412741173bd73b4` | `v3-cold-read-e88094c.md`, blob `633db268…` — **moved** | **end to end** |
| 6 | `contract/Document-Work-Assurance-Contract-v4.md` | `de210772994ee49bf8fa7d7a68510ca49e290a88` | `v3-cold-read-e88094c.md`, **same blob** — unmoved | covered by citation |
| 7 | `schema/document-assurance-v3/paragraph-map.schema.json` | `09aa869962f592c2f86c9379be0ef3eb7d2232ff` | `v3-cold-read-e88094c.md`, **same blob** — unmoved | covered by citation |

Plus, not a member and read for the reason `E10`'s second sentence gives:

| — | this repository's declared rule | blob at `006d0d5` | last recorded end-to-end read | this read |
|---|---|---|---|---|
| — | `document-harness/CONSTRUCTION-CHECKLIST.md` | `97ed956be92864dda125cb2ac8970b1375bcc8bc` | `v3-cold-read-e88094c.md`, blob `d4e95f34…` — **moved** | **end to end** |

**Why that file is here, verified rather than accepted.** `harness.json` at this repository's root
reads `{"policy": "CONSTRUCTION-LEDGER.md", "rules": ["document-harness/CONSTRUCTION-CHECKLIST.md"]}`
— I read the file. `E10`'s second sentence says a declared rule "is amended under this rule's own
discipline — including the independent read", so it is owed a read of the same kind. It is not an
eighth member: the membership sentence names seven and this file is not among them, and its own
header says so in as many words.

**Which record can be cited, and for what.** `v3-cold-read-e88094c.md` is an end-to-end read of
every member it lists: its §1 states all nine blob ids of the then-membership and its §5 opens
*"Read in full, end to end: all nine members"*. Its commit landed — `git log` on that file returns
one commit, `69a9a71 V3-REVIEW-RECORD-CORE-ONLY-CODE-e88094c-v1` — so under `E9` that read has
occurred. Members 3, 4, 6 and 7 carry blobs byte-identical to the ones that record states, so those
four are coverable by citation and I took the citation.

**Coverage derived, not taken from the addendum.** Measured here:

```
$ git diff --stat e88094c 006d0d53b6f441b2a1a7ad5c454224530ee380d7 -- <the seven members and the declared rule>
 document-harness/CONSTRUCTION-CHECKLIST.md |  6 +++---
 document-harness/ORCHESTRATION.md          | 23 +++++++++++++----------
 document-harness/README.md                 |  4 ++--
 document-harness/RULES.md                  | 19 +++++++++++--------
 4 files changed, 29 insertions(+), 23 deletions(-)
```

Exactly the four files plan ruling 43 names, at exactly the 29/23 it names — derived, and it
agrees. Two facts that ruling asserts which I checked rather than took:

```
$ git diff --stat 78d51ac 006d0d5 -- <the same eight paths>     ->  (empty)
$ git rev-list --count 78d51ac..006d0d5                         ->  1
$ git rev-parse HEAD                                            ->  006d0d53b6f441b2a1a7ad5c454224530ee380d7
$ git status --porcelain --untracked-files=no | wc -l           ->  0
```

The subject's members are byte-identical to `78d51ac`'s, the subject is the only commit between
them, and the worktree I read is the subject — so every file read below is the subject's bytes.

**The two members deleted since the cited record.** `E10` read nine paths at `e88094c` and reads
seven here. `git ls-tree 006d0d5 migration/document-work-assurance-v3/` matches neither
`v3-harness-operating-contract` nor `v3-harness-review-contract`: both stubs are gone from the
tree, so the list is seven because two members were deleted, not because a member was silently
dropped from the sentence. The deletion commit is `08d3137 V3-CORE-ONLY-CODE-STUBS-DELETED-v1`, and
it lands **after** `7bcdace V3-CORE-ONLY-CODE-DISPATCH-SPLIT-v1`, which is the order `E10`'s own
clause requires ("deleted them once no dispatch prompt named them").

## 2. What the changed bytes claim, and what the commands say

`E3` binds a factual assertion written into instruction text to the command that could falsify it.
Every claim the four moved files make about this repository's own machinery, run here at the
subject:

| claim, and where | command | result |
|---|---|---|
| `E10`: the layer is these seven paths | `git cat-file -t 006d0d5:<path>` ×7 | `blob` ×7 — all seven resolve |
| `E10`: `layer_path_check.py` scans the declared files exactly as it scans the members | read `tooling/hooks/layer_path_check.py` | `LAYER` is those seven in order; `scanned_paths` returns `LAYER + declared`, the declaration read from `harness.json` |
| `E10`: "and so does the reference sweep this instrument runs over the same list" | read `tooling/sweep_refs.py:41` | it imports `scanned_paths` from the guard — one list, not a second copy |
| `E10`: `dtw init` writes the file empty, both fields present | read `caller.render_harness_config` | `json.dumps({"policy": …, "rules": …})` — both keys emitted when empty |
| `E10`: the orchestrator reads `policy` | `ORCHESTRATION.md:88-103` | the obligation is written there |
| `ORCHESTRATION.md:37-39`: `dtw dispatch` is "one review-side mode and one executor-side mode for a product run" | `python tooling/dtw.py dispatch --help` | `(--subject SUBJECT \| --executor RUN)`, described as "PRODUCT run review" and "PRODUCT run executor" — two, and both product-side |
| `ORCHESTRATION.md:37-39`: the construction side is "a repository's own construction-side dispatch" | `python tooling/construction_dispatch.py --help` | `(--range RANGE \| --read READ \| --construction-executor)` — the three construction modes live there, not in `dtw dispatch` |
| `ORCHESTRATION.md:41-42`: that command derives the charter "from the declaration rather than from a constant of its own" | read `tooling/construction_dispatch.py:148-150` | `_charter` calls `declared_rules(repo_root)`, which reads `harness.json`; no charter constant |
| `README.md:26`: the instruction-layer check guards "this layer's seven members" | as above | `LAYER` is seven |
| `CONSTRUCTION-CHECKLIST.md` `R6`: this repository's review-records directory is what `.harness/scan-surfaces.json` declares | `cat .harness/scan-surfaces.json` | `{"review_record_dirs": ["migration/document-work-assurance-v3/"]}` — the value the file states, and the four `v3-*` families do land there (42 checkpoint-read, 29 cold-read, 52 review-full, 41 review-verify) |
| `CONSTRUCTION-CHECKLIST.md` `E2`: fifteen pack files at the 2026-08-03 re-baseline, a dated snapshot the pack no longer equals | `git ls-tree 006d0d5 --name-only schema/document-assurance-v3/` | 14 files — consistent with a dated snapshot, and with `CONSTRUCTION-INDEX.md` row 2 |
| the whole layer resolves | `python tooling/sweep_refs.py` | `13 caller-held or unresolvable references over 8 members and declared rule files` — all 13 `NAMETOK`, the compliant caller-held bare-name form; zero non-resolving path tokens |

One claim in that set does **not** survive its command, and it is finding L-1 below.

**Cross-member staleness checked rather than assumed.** A command changed inside this round
(`7bcdace` split the construction modes out of `dtw dispatch`), and that could have falsified
standing text in the members I cover by citation — citation covers the bytes read, never the world
around them. Measured: `grep -n "dtw dispatch\|dispatch --\|--range\|--read\|--construction-executor"`
over all seven members and the declared rule returns hits at `RULES.md:99`, `README.md:26` and
`ORCHESTRATION.md:37,70`, all about `dtw dispatch` itself, plus `EXECUTION.md:450`
(`dtw dispatch --executor` names `EXECUTION.md` to the executor), which the `--help` output above
confirms still exists. No member cites a mode that moved. `grep -n
"operating-contract\|review-contract\|CONSTRUCTION-CHECKLIST"` over the seven members returns
nothing, so no member points at a deleted stub or at the file that stopped being a member.

## 3. Findings

### L-1 (low) — `document-harness/RULES.md:101-102`: `E10` says the dispatch behaviour is not built; it is built

`E10`'s first reader now reads: "`dtw dispatch` is held to naming the declared files in every
prompt it writes, so that a cold session receives a repository's rules by the channel it receives
its charter — **the one of the four stated as an obligation on the command rather than as
behaviour already built**".

The appositive was true when written and is false at the subject. Measured here, in order:

```
$ git show 5a9c0fd^:tooling/rsclib/document_harness/dispatch.py | grep -c declared_rules   ->  0
$ git show 5a9c0fd:tooling/rsclib/document_harness/dispatch.py  | grep -c declared_rules   ->  0
$ git show 006d0d5:tooling/rsclib/document_harness/dispatch.py  | grep -c declared_rules   -> 18
$ git log --oneline -S declared_rules -- tooling/rsclib/document_harness/dispatch.py
7bcdace V3-CORE-ONLY-CODE-DISPATCH-SPLIT-v1
```

`5a9c0fd` is the amendment that wrote this wording, and its own commit body says so plainly ("the
command does not do it yet"). `7bcdace` lands later in the same round and builds it. At the subject
the behaviour exists in both of the command's two prompt families: `render_dispatch` emits
`declared_rules_line(dispatch.declared_rules)` into the review prompt, and `EXECUTOR_PROMPT` carries
a `{declared_rules}` slot filled from the same function. Run here, without side effects (I invoked
neither dispatch command: both write the freeze marker `.harness/review-pending.json`, which is
`E9`'s window and not a read's to open):

```
$ python -c "from rsclib.document_harness.dispatch import declared_rules, declared_rules_line, EXECUTOR_PROMPT; ..."
declared_rules() -> ('document-harness/CONSTRUCTION-CHECKLIST.md',)
line -> **This repository's own rules:** `document-harness/CONSTRUCTION-CHECKLIST.md` — declared under `rules` in its `harness.json`, to be read after the charter above. They bind this repository alone.
EXECUTOR_PROMPT has slot: True
```

**The downstream decision that goes wrong** (`R9`): a session reading `E10` to find out whether a
cold dispatch already carries this repository's declared rules is told it does not, and acts on
that — either by handing the rules over a second channel, or by opening work to build what
`7bcdace` built. The second is the shape `E6` exists to stop.

**Why the obligation half stays.** "is held to" is the right form and I am not asking for it back:
a rule that describes today decays every time the code moves, which is how this sentence got here
in the first place. Only the appositive claiming the code has *not* moved is wrong.

**Exact bytes.** Replace lines 99-102:

```
  is absent: `dtw dispatch` is held to naming the declared files in every prompt it writes,
  so that a cold session receives a repository's rules by the channel it receives its
  charter — the one of the four stated as an obligation on the command rather than as
  behaviour already built;
```

with:

```
  is absent: `dtw dispatch` is held to naming the declared files in every prompt it writes,
  so that a cold session receives a repository's rules by the channel it receives its
  charter;
```

**Route.** The record supplies the exact bytes, so `E10`'s free channel takes it, on the two
conditions that clause states and that are the orchestrator's to confirm rather than mine: the fix
is a deletion that adds no clause and changes what no rule requires, so the design test does not
fire; and no round has relied on the deleted appositive — nothing turns on whether the sentence
describes today, because the obligation it states is unchanged either way.

### L-2 (low) — `document-harness/RULES.md:16-18`: the header's byte-provenance sentence is false at the subject

The header reads: "Every rule below **carries** the identifier it has always carried and, apart
from the two disclosed in that round's commit body, the bytes it has always carried; what changed
is which file holds it."

The two disclosed in `4b81dd9`'s body are `E10` and `R6` — its own words, "EXACTLY TWO RULES CHANGE
BYTES, both disclosed here in full", followed by the membership sentence and `R6`'s record channel.
Since that split, at the subject:

```
$ git log --oneline -- document-harness/RULES.md
894bc92 V3-CORE-ONLY-CODE-FIX-v1              # E12
08d3137 V3-CORE-ONLY-CODE-STUBS-DELETED-v1    # E10
5a9c0fd V3-CORE-ONLY-CODE-E10-AMENDMENT-M1-v1 # E10
c7f9c8d V3-CORE-ONLY-LAYER-FIX-v1             # a header paragraph, no rule
4b81dd9 V3-CORE-ONLY-LAYER-RULE-SPLIT-v1      # the split
```

`894bc92` deleted "(`dtw dispatch`)" from `E12`. `E12` is not one of the two, so at the subject a
rule below does not carry the bytes it has always carried, and the sentence's present tense says it
does. The final clause anchors the sentence to the split, so a careful reader may take the whole
thing as history; the sentence does not say so, and it decays one rule further with every
amendment this file legitimately receives.

**The downstream decision that goes wrong** (`R9`): a reader establishing which of this file's
rules have been amended since the split — the question `E10`'s "each amendment passes an
independent read" makes someone ask — is told the answer is two, and at the subject it is three. It
is recoverable from `git log` and from the commit bodies, which is why this is low and not
must-fix.

**Exact bytes.** Replace lines 16-18:

```
> harness rather than a part of it. Every rule below carries the identifier it has always
> carried and, apart from the two disclosed in that round's commit body, the bytes it has
> always carried; what changed is which file holds it.
```

with:

```
> harness rather than a part of it. At that split every rule below kept the identifier it
> had and, apart from the two disclosed in that round's commit body, its bytes; what
> changed was which file holds it.
```

That is a historical claim, so it is true at the split and stays true however often these rules are
amended afterwards — the property the current sentence lacks.

**Route.** Exact bytes supplied, no clause added, nothing a rule requires changed: `E10`'s free
channel, on the same two conditions as L-1.

### O-1 (observation) — `document-harness/ORCHESTRATION.md:41-44`: a property asserted of any caller's declared rule file that no rule requires

The construction-round executor's charter is "that repository's own rule file — the one its
`harness.json` declares, … and **which names [RULES.md](RULES.md) as its counterpart**". True of
this repository: `CONSTRUCTION-CHECKLIST.md`'s header names `RULES.md` and sends the reader to
both. But `ORCHESTRATION.md` travels, a caller reads it as written, and nothing in the layer
obliges a caller's declared rule file to name `RULES.md` at all — `E10` asks only that a declared
rule be amended under its discipline. So a member describes a caller's own file by a property the
caller was never asked to give it.

Not introduced by the changed bytes: the clause stood at `e88094c`, and this round only inserted a
sub-clause ahead of it. I report it rather than propose bytes because every fix I can see either
merely generalises the sentence, with no decision behind the change, or states a requirement on a
caller's declared rule file — and the second adds a bound, which is `E10`'s design test and a
round's to open, not a read's to slip in.

### O-2 (observation) — `document-harness/RULES.md:116`: "Its" now sits behind two intervening sentences

`E10`'s deletion history — "The two contract supersessions were members until round `CONTRACT-V4`…
The two retired operating contracts' stubs were members until round `CORE-ONLY-CODE`… **Its** edits
are additive or subtractive" — leaves the pronoun's antecedent (the instruction layer) three
sentences back, with "the sentence above" as the nearest noun phrase. Wording-level under `R9`: the
fix changes no check outcome, no evidence binding, no permission, no obligation and no verdict
path, and the meaning is recoverable from the clause itself, which can only be about the layer. I
can name no downstream decision that goes wrong, so by `R9` it rides the next batch touching this
layer and spawns no round and no read.

## 4. What this read discharges

`c7f9c8d`'s body ends "The `E10` read debt on the two stubs and on `RULES.md` rides the next
opening read of this layer", and plan ruling 43 states the same debt as round 2's closeout stated
it at step 7. The stubs are gone from the tree, so that half of the debt is moot rather than
discharged. The other half is the four moved files, and this record is their end-to-end read:
`RULES.md`, `README.md`, `ORCHESTRATION.md` and the declared `CONSTRUCTION-CHECKLIST.md`. Two of
the amendments inside that stock arrived through channels that owe a read of their own text —
`5a9c0fd` through `E10`'s must-fix channel, whose re-read landed at `d771cc4`, and `08d3137` /
`894bc92` inside the round — and all of their bytes are in this read's end-to-end stock at their
subject values.

Nothing in this section is a verdict: a read carries none (`R3`).

## 5. What I read, and the ceilings (`R4`)

**Read in full, end to end:** `document-harness/RULES.md` (250 lines), `document-harness/README.md`
(26), `document-harness/ORCHESTRATION.md` (126), and this repository's declared rule
`document-harness/CONSTRUCTION-CHECKLIST.md` (78); `HARNESS-DECISIONS.md` `§live` (`:30-283`,
eleven entries: `HD-69`, `HD-66`, `HD-65`, `HD-62`, `HD-59`, `HD-41`, `HD-36`, `HD-35`, `HD-34`,
`HD-23`, `HD-9`) and the file's header block; `harness.json`; `.harness/scan-surfaces.json`; plan
ruling 43 and its two neighbours; the full commit bodies of `4b81dd9`, `c7f9c8d` and `5a9c0fd`; the
full diff `e88094c..006d0d5` over the eight paths; `v3-cold-read-e88094c.md` §1 and §5.

**Covered by citation, not read here:** members 3, 4, 6 and 7 — `EXECUTION.md`, `REVIEW.md`,
`contract/Document-Work-Assurance-Contract-v4.md`,
`schema/document-assurance-v3/paragraph-map.schema.json` — each byte-identical to the blob
`v3-cold-read-e88094c.md` records reading end to end. What citation does **not** cover is standing
text in those four falsified by this round's code changes around them, which is why §2's last
paragraph greps them for the two shapes this round could have broken. Those greps are the whole of
what I looked at inside those four, plus `paragraph-map.schema.json:5` and `EXECUTION.md:450`, read
in full to check two claims the changed bytes make about them.

**Sampled:** `tooling/hooks/layer_path_check.py` — `LAYER`, `TOKEN`, `PATHLIKE`, `RUNTIME_PREFIX`,
`unresolved_tokens`, `added_lines_by_path`, `scanned_paths` and `check`'s loop head in full, the
rest by name. `tooling/rsclib/document_harness/dispatch.py` — the module docstring,
`declared_rules`, `declared_rules_phrase`, `declared_rules_line`, `EXECUTOR_PROMPT` and the review
prompt's line list in full; the derivation helpers by name.
`tooling/construction_dispatch.py` — `_charter` and the three modes' prompt renderers by name and
call site. `tooling/rsclib/document_harness/caller.py` — `render_harness_config` in full.
`CONSTRUCTION-INDEX.md` — the travel rows and the two non-travelling rows naming the checklist and
the wiring. `tooling/sweep_refs.py` — the docstring and its import line.

**Probed only:** `tooling/rsclib/document_harness/cli.py` (the `dispatch` subparser's arguments).

**`UNVERIFIABLE`, stated rather than folded into supported:**

- That this session ran cold, in a fresh context, as its own session on `opus` under plan ruling
  43's tool restriction. A process claim about a session nobody can inspect from the repository —
  marked, not verified (`R4`). What *is* structural: I was dispatched by, prompted by and scoped by
  the orchestrator, received a generated prompt naming only the charter and the commit, and report
  through a record the orchestrator commits unchanged — all four of `R1`'s holdings outside the
  work side.
- Whether the free channel is open for L-1 and L-2 at the moment they are applied. I state the two
  conditions and my reading of them; whether a round has since relied on either text is the
  orchestrator's to confirm, because that is the role which knows what this round has done.
- `4b81dd9`'s claim that the split was byte-preserving for nineteen of the twenty-one moved rules.
  I did not re-derive it; the one-shot script it names is not committed. Nothing here rests on that
  claim except L-2, which rests only on the *two* the same body discloses — and those two are named
  in the body itself.

**What I did not do, deliberately.** I ran neither `dtw dispatch` nor `construction_dispatch.py` in
any mode: both write `.harness/review-pending.json`, and a read opening `E9`'s freeze window is a
side effect no finding here needed. Every claim about what those commands emit comes from `--help`
output and from reading the prompt constants and their call sites.
