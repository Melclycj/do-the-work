# Instruction-layer read — subject `e88094c5e0ea00ab9ac9b57e2e79ff74e6ee59c3`

An `E10` read, at the opening of round 2 `CORE-ONLY-CODE` of batch `CORE-ONLY`. Not a round: no
budget spent, no verdict carried, output is findings tiered must-fix / low / observation (`R3`).
Dispatched with the charter `migration/document-work-assurance-v3/v3-harness-review-contract.md`,
whose named successor `document-harness/CONSTRUCTION-CHECKLIST.md` was read in full, and then the
counterpart *that* file names, `document-harness/RULES.md`, also in full.

Record name: `v3-cold-read-`. `R6` offers two read filenames and the layer still defines no
criterion for choosing between them (rider `read-name-split`, not closed here). I took
`cold-read` for the reason the five previous whole-layer records took it — the subject is the
layer at a round's opening.

**Findings: 1 must-fix, 1 low, 1 observation.**

---

## 1. The member set and the coverage, both derived — not received

The dispatch enumerated nothing and handed me no member table (`R2`); the prompt I received is
byte-for-byte `dispatch.READ_PROMPT`, which names the charter and the commit and nothing else.
`E10`'s own sentence at the subject names the members, and reads **exactly nine paths**
(`document-harness/RULES.md:86-96`). All nine resolve at the subject. Blob ids from
`git rev-parse e88094c5e0ea00ab9ac9b57e2e79ff74e6ee59c3:<path>`, run here.

| # | member | blob at `e88094c` | last recorded end-to-end read | this read |
|---|---|---|---|---|
| 1 | `document-harness/RULES.md` | `47a7fbe17d50b35505baaf7a003a2bbd33bf116a` | none — the file did not exist at `a542c6d` | **end to end** |
| 2 | `document-harness/README.md` | `5586b06621f1dc8ab413683b4a9793956a694c44` | `v3-cold-read-a542c6d.md`, blob `271e9344…` — **moved** | **end to end** |
| 3 | `document-harness/EXECUTION.md` | `08fa87f8380b60a0af4e125e1bfe88747d26f0e4` | `v3-cold-read-006138e.md`, blob `234fdddf…` — **moved** | **end to end** |
| 4 | `document-harness/REVIEW.md` | `71707a3a01016e86b63238d494df98abbd2408c3` | `v3-cold-read-006138e.md`, blob `13f91419…` — **moved** | **end to end** |
| 5 | `document-harness/ORCHESTRATION.md` | `633db2683afbd7e2f09627fd6c1bab05a37c5ac2` | `v3-cold-read-006138e.md`, blob `a9e9f75e…` — **moved** | **end to end** |
| 6 | `migration/document-work-assurance-v3/v3-harness-operating-contract.md` | `729313a4c47d3de5c852f9544fd5d7712f58c6b3` | `v3-cold-read-006138e.md`, blob `6d571492…` — **moved** | **end to end** |
| 7 | `migration/document-work-assurance-v3/v3-harness-review-contract.md` | `b79ebb206b6b7ebaccde97724da11088b041ad68` | `v3-cold-read-006138e.md`, blob `29bdc9fb…` — **moved** | **end to end** |
| 8 | `contract/Document-Work-Assurance-Contract-v4.md` | `de210772994ee49bf8fa7d7a68510ca49e290a88` | `v3-cold-read-006138e.md`, blob `a90c90fd…` — **moved** | **end to end** |
| 9 | `schema/document-assurance-v3/paragraph-map.schema.json` | `09aa869962f592c2f86c9379be0ef3eb7d2232ff` | `v3-cold-read-006138e.md`, same blob — **unmoved** | covered by citation; read end to end anyway |

Plus, not a member and read for the reason `E10`'s second sentence gives:

| — | this repository's declared rule | blob at `e88094c` | last recorded end-to-end read | this read |
|---|---|---|---|---|
| — | `document-harness/CONSTRUCTION-CHECKLIST.md` | `d4e95f3476b4b4c3757deb0c4f5eee7f32f0a187` | `v3-cold-read-a542c6d.md` read it as the charter, blob `5f77c3fd…` — **moved** | **end to end** |

**Why that file is in this read, verified rather than accepted.** `harness.json` at this
repository's root reads `{"policy": "CONSTRUCTION-LEDGER.md", "rules":
["document-harness/CONSTRUCTION-CHECKLIST.md"]}` — I read the file. `E10`'s second sentence says a
declared rule "is amended under this rule's own discipline — including the independent read". So
the declared rule is owed a read of the same kind, and it is not a tenth member: the membership
sentence names nine and this file is not among them.

**Which record can be cited, and for what.** `v3-cold-read-006138e.md` §1 states all nine blob ids
of the then-membership and its §5 coverage list opens *Read in full: all nine members*; it is
therefore an end-to-end read of each. `v3-cold-read-a542c6d.md` read `document-harness/README.md`
end to end and cited `006138e` for the other eight. Only member 9 is byte-unchanged since either,
so only member 9 is coverable by citation. I read it anyway — citation is a permission, not a bar.

**What is *not* a citable record, and this matters here.** `v3-review-verify-c7f9c8d.md` states
the blob ids of members 1, 6 and 7 (its `V-2`), and it says in as many words that it is *"a VERIFY
of a repair, not the `E10` read, whose subject is the amendment text itself"*. I did not treat it
as discharging the read on those three. Plan ruling 32 and round 1's closeout step 6d record the
same debt, and this record is what discharges it.

**Coverage derived, not taken from the addendum.** Measured here:

```
$ git diff --stat a542c6d e88094c -- <the nine members and the declared rule>
 contract/Document-Work-Assurance-Contract-v4.md    |  60 ++---
 document-harness/CONSTRUCTION-CHECKLIST.md         | 215 ++----------------
 document-harness/EXECUTION.md                      |  22 +-
 document-harness/ORCHESTRATION.md                  |  24 +-
 document-harness/README.md                         |  20 +-
 document-harness/REVIEW.md                         |  11 +-
 document-harness/RULES.md                          | 247 +++++++++++++++++++++
 .../v3-harness-operating-contract.md               |   2 +-
 .../v3-harness-review-contract.md                  |   2 +-
 9 files changed, 322 insertions(+), 281 deletions(-)

$ git log --oneline a542c6d..e88094c -- <the same ten paths>
c7f9c8d 02bb0bc 110924f 40f20eb 322fd1c b235701 228df32 4b81dd9 cbaee8e     # 9 commits
$ git rev-list --count a542c6d..e88094c   ->  28
```

`schema/document-assurance-v3/paragraph-map.schema.json` appears in neither list. This agrees with
the orchestrator's addendum and with plan ruling 32, which I read at
`document-harness/plans/core-only.plan.md:261-274` rather than accepting as reported; the ruling
is present and says what the addendum says it says.

**Worktree integrity.** `git rev-parse HEAD` returns the subject and `git status --porcelain`
returns only `?? .goals/`, untracked and outside the layer. I did not rely on that alone:
`git hash-object` on each of the ten paths in the worktree returns the ten blob ids tabled above,
so the bytes I read are the subject's bytes. `.harness/review-pending.json` exists and names this
same subject (`dispatched_at 2026-08-30T03:32:39+00:00`), so `E9`'s window is mine and nothing but
this record is owed to it; `.harness/` is gitignored and nothing committed carries it.

## 2. `HARNESS-DECISIONS.md` `§live`, read in full

Owed at every opening whether or not the layer read is waived, and not a member — cited by section,
never by blob (`E10`). At the subject `§live` runs from `:30` to `:232` and holds **ten** entries:
`HD-66` `HD-65` `HD-62` `HD-59` `HD-41` `HD-36` `HD-35` `HD-34` `HD-23` `HD-9`. Two fewer than the
twelve the previous VERIFY read at `c7f9c8d`: `HD-68` and `HD-67` moved to `§implemented` at
`cfa73df`, which is the round-1 closeout, and both are present there. Nothing in `§live` conflicts
with the layer as I read it. Three bear on what follows and are obeyed here:

- **`HD-41` ① and ④** — scope before assertion, and a class scan before writing a fix. Every
  absolute quantifier below carries its scope; finding **M-1** carries the class scan for its own
  defect class rather than the reported instance.
- **`HD-59`** — corrections go forward, never in place. Nothing in this record rewrites an earlier
  record; where I disagree with an earlier figure I say which measurement changed it.
- **`HD-66`** — distribution form is conditional on core distribution proving possible, and it
  names the checklist-and-stubs non-travel as the structural half. Observation **O-1** reports the
  state of that half at the subject; the question and the conclusion are the user's (`R5`).

## 3. What the layer says, checked against the tree rather than read

Every figure here is my own run at the subject tip.

**The membership sentence and its machine mirror agree exactly.** Parsed the nine backticked paths
out of `E10`'s first sentence and compared with `layer_path_check.LAYER` as ordered tuples:

```
sentence: 9   LAYER: 9   equal as ordered tuples: True   set difference: set()
scanned_paths(<this repo>) -> the nine, then 'document-harness/CONSTRUCTION-CHECKLIST.md'
```

So `E10`'s second reader — *the guard scans the declared files exactly as it scans the members* —
is true, and true live on this repository rather than only in a fixture.

**The split preserved every rule but the two it disclosed.** I re-derived this rather than trusting
`4b81dd9`'s body: parsed each `- **E<n>**` / `- **R<n>**` block out of
`CONSTRUCTION-CHECKLIST.md` at `a542c6d` and out of both files at the subject.

```
pre-split ids (22): E1 E2 E3..E12 R1 R2 R3 R9 R10 R4..R8
post-split     : RULES.md 21 (E1, E3..E12, R1..R10)  +  CONSTRUCTION-CHECKLIST.md 1 (E2)
lost: none   gained: none
byte-changed: E10 (5580 -> 6822), R6 (279 -> 453)   — and nothing else
```

Exactly the two `4b81dd9`'s body discloses, and no third. `R6`'s change demotes the token
`migration/document-work-assurance-v3/` to *the review-records directory that repository
declares*; I checked the machinery behind it, because a rule that points a cold reviewer at a
per-checkout gitignored file could have lost the caller its answer — it does not:
`caller.DEFAULT_REVIEW_RECORD_DIRS` is `("assurance/review-records/",)`, a caller-neutral
convention rather than this instrument's own directory, and `load_scan_surfaces` returns the
defaults when no declaration exists while refusing loudly on a malformed one. `R6`'s other claim,
that the declared directory is also the only place the freeze guard admits a returned record from,
is `review_freeze_check.is_record` at `:67-69`.

**Assertions in the layer about code, each run rather than described.**

| assertion | where | result |
|---|---|---|
| `contract/Document-Work-Assurance-Contract-v4.md`'s path is pinned under `tooling/rsclib/document_harness/__init__.py` | `EXECUTION.md:353` | true — `CONTRACT_PATH`, `:38` |
| `document-harness/README.md`'s path is pinned by a test | `EXECUTION.md:350` | true — three test modules name it |
| the two shipped instance templates under `document-harness/templates/` are copied by `init_target.py` | `EXECUTION.md:351-352` | true — `TEMPLATE_DIR` `:55`, `_copy_templates` `:81`; the directory holds exactly `decision-log.md` and `rider-bank.md` |
| the v1 review schema's stem appears in `document-harness/README.md` as neither a code span nor a link | `README.md:20` | true — no occurrence in either form |
| `dtw dispatch` has three review-side and two executor-side modes | `ORCHESTRATION.md:37-38` | true — product / `--construction` / `--read`, and `--executor` / `--construction-executor` |
| `ORCHESTRATION.md` has nine cite-only obligations and three it is the text for | `README.md:22`, `ORCHESTRATION.md:46,62` | true — 9 table rows, 3 subsections, 12 total |
| the sweep scans the declared files over the same list | `E10` | true — `sweep_refs.py` imports `scanned_paths`; its tally line reads "members and declared rule files" |
| `dtw init` writes `harness.json` empty, both fields present | `E10` | true — `init_target:146-155`, `caller.render_harness_config` emits both keys even when empty |
| **`dtw dispatch` names the declared files in every prompt it writes** | `E10` | **false — finding M-1** |

**Whole-tree state at the subject.**

```
$ python -m pytest tests -q          (run from tooling/)   853 passed in 148.46s   exit 0
$ python tooling/hooks/layer_path_check.py        exit 0
$ python tooling/hooks/candidate_path_check.py    exit 0
$ python tooling/hooks/review_freeze_check.py     exit 0
$ python tooling/sweep_refs.py
-- 13 caller-held or unresolvable references over 10 members and declared rule files
   (all 13 NAMETOK, the compliant caller-held form)
```

The rider bank's id set is byte-identical to its set at `c7f9c8d` — 24 rows, none added, none
deleted. `checklist-cited-not-carried` is correctly absent, redeemed in round 1.

## 4. Findings

### M-1 (must-fix) — `E10` states a channel that does not exist, in the indicative, beside three that do; `ORCHESTRATION.md` states the same channel a second time and more strongly

**Location.** `document-harness/RULES.md:100-102` (`E10`, the second sentence's reader list) and
`document-harness/ORCHESTRATION.md:37-41`.

**What the text says.** `E10`: *"Four readers, each a decision that changes when the file is
absent: `dtw dispatch` names the declared files in every prompt it writes, so a cold session
receives a repository's rules by the channel it receives its charter; …"* — one parallel list, four
clauses, all present indicative. `ORCHESTRATION.md`: *"something must hand each its charter at
startup, and `dtw dispatch` does: … the construction-round executor's is that repository's own rule
file — the one its `harness.json` declares …"*.

**The ground truth, measured.** `tooling/rsclib/document_harness/dispatch.py` never reads the
declaration. Counted over the whole module:

```
load_harness_config -> 0     harness.json -> 0     HarnessConfig -> 0     .rules -> 0
```

The charters are two hard-coded constants: `CONSTRUCTION_ROLE_INSTRUCTION` (`:548-550`, the review
stub) and `CONSTRUCTION_EXECUTOR_CHARTER` (`:776`, the literal string
`"document-harness/CONSTRUCTION-CHECKLIST.md"`). I rendered all four prompt constants directly
rather than through the CLI, so as not to write the freeze marker: `CONSTRUCTION_PROMPT`,
`READ_PROMPT`, `EXECUTOR_PROMPT` and `CONSTRUCTION_EXECUTOR_PROMPT` each name one charter and no
declared file. **I am the live instance:** the prompt that reached me is `READ_PROMPT`, and it named
no declared rule — I learned that `harness.json` declares one from the orchestrator's addendum and
then from the file, not from the channel `E10` says carries it.

That `ORCHESTRATION.md`'s claim is the stronger one is worth stating separately: `E10` says the
declared files are *named in the prompt*, while `ORCHESTRATION.md` says the construction-round
executor's *charter is* the file `harness.json` declares. In this repository the constant and the
declaration happen to be the same path, so the sentence is accidentally true here and false in
every other repository — which is the generality it claims.

**Class scan (`HD-41` ④), my own, at this tip over all nine members and the declared rule file:**

```
$ git grep -n 'harness.json' -- <the nine members and the declared rule>
CONSTRUCTION-CHECKLIST.md:9  ORCHESTRATION.md:9  ORCHESTRATION.md:40  ORCHESTRATION.md:93
README.md:23  README.md:25  EXECUTION.md:14  REVIEW.md:9  RULES.md:10  RULES.md:98
```

Ten sites. Eight say only that a repository declares its rules there, or that `policy` names the
policy file — all true. Exactly two assert the dispatch channel, and both are named above. No third.

**Why it is there, and why that does not settle it.** `cbaee8e`'s own commit body says the reader
was to be written *"as an obligation the command is held to and not as behaviour that exists
today — measured here, git grep for harness.json under tooling/rsclib/document_harness/ returns
caller.py and init_target.py and nothing in dispatch.py"*. The executor measured it and said so;
the bytes that landed at `4b81dd9` carry no such marking. `E3` is explicit that a factual assertion
written into instruction text runs the command that could falsify it first — the command was run,
it returned the falsifying answer, and the sentence went in anyway in the same grammatical form as
its three true neighbours.

**Downstream decision that goes wrong.** A repository that declares its own rules in `harness.json`
reads `E10` — the rule that tells it what the declaration buys — and is told its cold sessions
receive those rules by the channel that carries the charter. Its orchestrator therefore hands them
by no other channel. The cold executor then runs answering to `EXECUTION.md` alone, and the
caller's own rules, which `E10` says bind only that repository, reach nobody in it. `R2` calls
chat-only load-bearing material a finding; this is the rule that makes the committed channel exist,
and it does not.

**Minimum fix — bytes supplied.**

`document-harness/RULES.md:101-102`, replace

> `dtw dispatch` names the declared files in every prompt it writes, so a cold
> session receives a repository's rules by the channel it receives its charter;

with

> `dtw dispatch` is held to naming the declared files in every prompt it writes,
> so that a cold session receives a repository's rules by the channel it receives
> its charter — the one of the four stated as an obligation on the command rather
> than as behaviour already built;

`document-harness/ORCHESTRATION.md:39-40`, replace

> the construction-round executor's is that repository's own rule file — the one
> its `harness.json` declares, which names [RULES.md](RULES.md) as its

with

> the construction-round executor's is that repository's own rule file — the one
> its `harness.json` declares, which the command is held to deriving from the
> declaration rather than from a constant of its own, and which names
> [RULES.md](RULES.md) as its

Neither replacement adds a clause to any rule and neither changes what any rule requires: the
obligation `E10`'s second sentence already places on the declaration is unchanged, and what changes
is whether a reader takes it for a description of today. Both stay true once the code lands.

**The equivalent disposition, stated because it closes the same gap.** Plan item H schedules
`dtw dispatch` naming the declared rules for this round, and acceptance 11 measures it. If that
code lands, both sentences become true as written and no amendment is owed. Which route the round
takes is not mine; what I can say is that at the subject the text is false, and `E10`'s must-fix
channel — an amendment commit plus an independent re-read of the amended text, which is not a round
and spends no budget — is what the layer gives a read for text that is wrong.

### L-1 (low) — nine commit and blob ids in members that travel resolve nowhere for a caller, and the rule saying where they resolve is in a file the caller does not have

**Location.** `document-harness/README.md:26`; `document-harness/EXECUTION.md:259`, `:358`,
`:407`, `:409`, `:412`, `:435`, `:494`; `contract/Document-Work-Assurance-Contract-v4.md:246`.

**Measured, scope = all backticked hex tokens of 7–40 characters in the eight prose members
(the schema carries none):** twelve such tokens. Resolved against this repository:

```
0d73a5f  commit    (EXECUTION.md:411, labelled "instrument")
56d1b17  commit    (contract v4:281)
3617b74e9149e3c51ddfaf9c969a6be584972961  blob  (contract v4:284)
820b287 a22cca0 838c413 ddd773a a8af54c 6fd0ae3 418b89c 9ba9bbc 7db177d   -> MISSING (9)
```

Contract v4's blob citation is the one that handles itself: its own sentence says the blob is
reachable *in this repository's git history* and *"in no working tree and in no repository that
runs against this contract"*, so a caller reading it is told not to look. The nine have no such
sentence. The rule that resolves them — *"A commit id cited in this file or in any other
instruction-layer member (`E10`) that this repository does not have … is a commit of the repository
this one was extracted from"* — is `document-harness/CONSTRUCTION-CHECKLIST.md`'s *Where a cited
commit id resolves*, this repository's own declared rule, which `E10` says binds only the
repository declaring it and which `CONSTRUCTION-INDEX.md` keeps on the construction side.

**Downstream decision that goes wrong.** `EXECUTION.md:358` tells a reader deciding whether a
change set is doc-only or tooling-touching — a tier decision the same section makes binding on
every pass — that two accepted rounds had already read the clause that way, and names `838c413` as
one of them. In a caller, `git show 838c413` fails, and nothing the caller holds says whether the
id is stale, whether its clone is short, or whether it belongs to another repository. The same
shape sits on the revert anchor's price (`:435`, `418b89c`) and the checker-authoring rules'
provenance (`:494`, `9ba9bbc`).

**Why it survived the round that hunted this class.** `E10`'s caller-held-artifact clause is
written for *paths* — *"a caller-held path is named, never written as a path token … an artifact
living only in a caller is given its name and its holder instead"* — and both instruments that
enforce it read path-shaped tokens or bare filenames: `layer_path_check.PATHLIKE` requires an
admitted extension or a trailing slash, and `sweep_refs`'s `NAMETOK` form matches basenames. A
seven-character hex id is neither, so the class is invisible to the measurement acceptance 1 rests
on, and the sweep's zero on a harness-only tree will be silent about these nine.

**No bytes supplied, deliberately.** The fix that would make the class decidable is a clause in
`E10` extending the holder convention from paths to cited ids — adding a bound, which `E10`'s
design test makes a round rather than a free-channel application. Rewriting the nine sentences by
hand without that clause would be an edit no rule requires. So this banks (`R10`): target =
`E10`'s caller-held-reference clause and the nine sites above; redeem-when = the next
round-eligible batch touching that clause, or `sweep_refs`'s resolution rules; deadline = the first
repository that mounts this harness without also holding this repository's history — the moment the
nine first fail for a reader who has no other route, which by `HD-37` ① is not inside the round
that writes the row.

### O-1 (observation) — the two stubs are still members, still name construction-side paths, and `HD-66` calls that a definitional conflict; ruling 34 is the route and nothing here judges it

At the subject, members 6 and 7 each carry a link to
`document-harness/CONSTRUCTION-CHECKLIST.md` and a path token for
`document-harness/plans/harness-deletion-first-stabilization.plan.md`, and both stubs are
themselves construction-side by `CONSTRUCTION-INDEX.md`. `HD-66` states the consequence in as many
words — a membership set three of whose nine do not travel is incompatible *by definition* with
core-only distribution — and the rider that carried it, `checklist-cited-not-carried`, was redeemed
in round 1 rather than re-banked, on the ground that its condition would not survive this round.
Plan ruling 34 executes item D and deletes the stubs, taking the membership sentence from nine to
seven. I record the state and not a verdict: whether the stubs should exist is not mine to conclude
(`R5`), and the round that removes them is the one now open. What this read fixes is the count I
read them at — nine, all resolving, and the sentence agreeing with `LAYER` exactly.

## 5. What I read, and the ceilings (`R4`)

**Read in full, end to end:** all nine members — `document-harness/RULES.md` (247 lines),
`document-harness/README.md` (26), `document-harness/EXECUTION.md` (522),
`document-harness/REVIEW.md` (325), `document-harness/ORCHESTRATION.md` (123), both retired-contract
stubs (5 each), `contract/Document-Work-Assurance-Contract-v4.md` (347) and
`schema/document-assurance-v3/paragraph-map.schema.json` (44) — plus this repository's declared rule
`document-harness/CONSTRUCTION-CHECKLIST.md` (78); `HARNESS-DECISIONS.md` `§live` (`:30-232`, ten
entries) and the file's header block; `harness.json`; plan rulings 32–35 and ruling 9, item H and
the twelve acceptances; the subject commit's body in full;
`v3-review-verify-c7f9c8d.md`; `v3-cold-read-a542c6d.md` §1 and `v3-cold-read-006138e.md` §1.

**Sampled:** `HARNESS-RIDERS.md` — the 24 ids in full, six rows read in full
(`E10-sync`, `charter-qualifiers`, `e9-pair-budget`, `e1-reader`, `announced-set-anchor`,
`onboarding-carries-construction`), the rest by id. `tooling/rsclib/document_harness/dispatch.py` —
the four prompt constants and their two charter constants in full, the resolution helpers by name.
`tooling/hooks/layer_path_check.py` — `LAYER`, `PATHLIKE`, `RUNTIME_PREFIX`, `scanned_paths`.
`tooling/rsclib/document_harness/caller.py` — the module docstring, the three defaults,
`load_scan_surfaces`, `render_harness_config`. `tooling/rsclib/document_harness/init_target.py` —
the docstring, `NOT_DONE`, `init_target`. `cbaee8e`'s and `4b81dd9`'s commit bodies.
`document-harness/plans/core-only.plan.md` — the rulings section, item list and acceptances.

**Probed only:** `tooling/sweep_refs.py` (its docstring and tally line);
`tooling/hooks/review_freeze_check.py` (`is_record` and the docstring);
`tooling/rsclib/document_harness/cli.py` (the docstring and the dispatch branches);
`tooling/rsclib/document_harness/__init__.py` (`CONTRACT_PATH`).

**`UNVERIFIABLE`, stated rather than folded into supported:**

- That this session ran cold, in a fresh context, as its own `claude -p` session on `opus`
  (plan ruling 33). A process claim about a session nobody can inspect from the repository —
  marked, not verified (`R4`). What is structural: I was dispatched by, prompted by and scoped by
  the orchestrator, received `READ_PROMPT` and nothing else as the generated dispatch, and report
  through this record.
- That the addendum I received alongside the dispatch did not narrow what I looked at. I derived
  the member set, the moved set and the citation chain from `E10`, `git rev-parse` and the two read
  records before checking them against the addendum, and they agree; but I cannot prove the order
  from the repository, so it is marked.
- Whether the nine unresolving ids in **L-1** are in fact commits of the extraction-source
  repository. `CONSTRUCTION-LEDGER.md`'s header names that repository as a single-machine worktree
  path, which identifies it without making it reachable from here, so I confirmed only that they do
  not resolve in this one.

**Ceilings on my own coverage:**

- A read is not a round and carries no verdict (`R3`). I did not review round 1's work, the rule
  split's design, the contract corrections, or any code beyond the assertions the layer text makes
  about it. Where I ran code it was to falsify a sentence in the layer, never to certify the module.
- I mutated nothing. `E4` binds a round adding a guard; this read adds none, and the guard over the
  amended members was mutation-tested at `c7f9c8d` by the VERIFY that preceded me. So my
  `layer_path_check` and `sweep_refs` results are runs, not proofs of binding force.
- The nine members were read at the subject's blobs, which I verified equal the worktree bytes.
  Line numbers in this record drift with the next commit.
- I did not exercise any `dtw dispatch` mode through the CLI, deliberately: the review-side modes
  write `.harness/review-pending.json` and a marker written by me would sit on top of the one that
  carries my own subject. The prompt constants were rendered in-process instead, which reads the
  same bytes the CLI prints but proves nothing about the CLI's own wiring.
- `HARNESS-DECISIONS.md`'s `§implemented` was not read; `E10` owes `§live` and only `§live`, and I
  read `§implemented` only far enough to confirm `HD-67` and `HD-68` landed there.

## 6. Record channel (`R6`)

This record is `v3-cold-read-e88094c.md` under `migration/document-work-assurance-v3/`, which is
what `.harness/scan-surfaces.json` declares under `review_record_dirs` and what
`document-harness/CONSTRUCTION-CHECKLIST.md`'s `R6` instance value states. Written in the worktree,
uncommitted; the orchestrator commits it unchanged, title
`V3-REVIEW-RECORD-CORE-ONLY-CODE-e88094c-v1`.

## 7. Routing, for the orchestrator (`R10`)

- **M-1** takes `E10`'s must-fix channel: an amendment commit carrying the two replacements above,
  plus an independent re-read of the amended text — the pair is not a round and spends no budget.
  If the round instead lands item H's code first, both sentences become true as written and the
  amendment is unnecessary; that choice is the round's, and either route closes it.
- **L-1** banks: fix is design, target and redeem-when named in the finding.
- **O-1** asks for nothing. Ruling 34 already carries it.
