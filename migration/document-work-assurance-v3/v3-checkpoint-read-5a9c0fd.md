# Instruction-layer read — subject `5a9c0fd6debcb771044663b94b28d8e1eca24eb2`

An `E10` read. Not a round: no budget spent, no verdict carried, output is findings tiered
must-fix / low / observation (`R3`). Dispatched with the charter
`migration/document-work-assurance-v3/v3-harness-review-contract.md`, whose named successor
`document-harness/CONSTRUCTION-CHECKLIST.md` was read in full, and then the counterpart *that*
file names, `document-harness/RULES.md`, also in full.

**Subject, derived rather than accepted.** The commit at the subject is an `E10` amendment, and
`E10` says of such a commit that *"a read's must-fix findings are answered by an amendment commit
plus an independent re-read of the amended text"* and that *"that read's subject is the amendment
text itself, never the work it governs"*. So the subject is the two replacements `5a9c0fd` made in
`document-harness/RULES.md` and `document-harness/ORCHESTRATION.md`, and this record is the
independent re-read that `E10` pair owes. That scope is derivable from the repository alone — the
commit's own body opens `Kind: amendment (E10 must-fix channel, orchestrator)`, its diff touches
exactly two members, and `E10`'s sentence does the rest — so the orchestrator's addendum narrowed
nothing I could not have derived. I checked that before relying on it.

Record name: `v3-checkpoint-read-`. `R6` offers two read filenames and the layer still defines no
criterion (rider `read-name-split`, not closed here). I took `checkpoint-read` on the precedent of
`v3-checkpoint-read-f61ce2c.md`, the previous read whose subject was an amendment text mid-round.

**Findings: 0 must-fix, 0 low, 3 observations.** The amendment applies the finding's supplied bytes
and nothing else, at both sites the finding named, and the class it belongs to has no third site.

---

## 1. Coverage: what moved, what is covered by citation, what I read anyway

Blob ids from `git rev-parse <rev>:<path>`, run here; the worktree check is `git hash-object` on the
same paths, so the bytes I read are the subject's bytes.

| # | member | blob at `e88094c` | blob at `5a9c0fd` | this read |
|---|---|---|---|---|
| 1 | `document-harness/RULES.md` | `47a7fbe1…` | **`b860d4a0d87e1585869950d69770554cc01ec74c`** — moved | **end to end** (249 lines) |
| 2 | `document-harness/README.md` | `5586b066…` | same | citation — `v3-cold-read-e88094c.md` §1 |
| 3 | `document-harness/EXECUTION.md` | `08fa87f8…` | same | citation; `:1-22` re-read for the class scan |
| 4 | `document-harness/REVIEW.md` | `71707a3a…` | same | citation; `:1-16` re-read for the class scan |
| 5 | `document-harness/ORCHESTRATION.md` | `633db268…` | **`dfe8f4fe1dcf1229b48ab91db3bd7911e02f45ea`** — moved | **end to end** (125 lines) |
| 6 | `…/v3-harness-operating-contract.md` | `729313a4…` | same | citation |
| 7 | `…/v3-harness-review-contract.md` | `b79ebb20…` | same | **end to end** — it is my charter |
| 8 | `contract/Document-Work-Assurance-Contract-v4.md` | `de210772…` | same | citation |
| 9 | `schema/…/paragraph-map.schema.json` | `09aa8699…` | same | citation |
| — | declared rule `document-harness/CONSTRUCTION-CHECKLIST.md` | `d4e95f34…` | same | **end to end** (78 lines) — `E10`'s second sentence |

`v3-cold-read-e88094c.md` §1 states the blob id of each of the nine and its §5 opens *Read in full,
end to end: all nine members*, so it is the end-to-end record the citation clause wants, and it is
committed at `69a9a71`. Seven members are byte-unchanged since it and are covered by it. The two
that moved are not, and I read both end to end at the subject's blobs — **stated so that a later
read may cite this record for members 1 and 5**, which otherwise have no end-to-end read at their
current bytes. Rider `read-name-split` notes that `E10`'s citation clause admits only a *recorded
end-to-end* read and that an amendment re-read does not qualify as such; that is a statement about
what a read's subject is, not about what a record may report, and the coverage above is reported
per `R4` rather than claimed by filename.

**The change boundary, measured, not taken from the body.**

```
$ git diff --stat e88094c 5a9c0fd
 document-harness/ORCHESTRATION.md                  |   4 +-
 document-harness/RULES.md                          |   6 +-
 .../v3-cold-read-e88094c.md                        | 418 +++++++++++++++++++++
 3 files changed, 425 insertions(+), 3 deletions(-)

$ git rev-list --count e88094c..5a9c0fd  ->  2      (69a9a71 the record, 5a9c0fd the amendment)
```

Two commits, and the first is the read record itself — which is what `E9` requires of the window
between a read's dispatch and its record landing: *the branch takes no commit but the record
itself*. No code changed in the interval, so the code measurements in `v3-cold-read-e88094c.md` §3
still stand on unchanged bytes; where I rely on one below I say so, and I re-ran the ones the
amendment's own new claim depends on.

**Worktree integrity.** `git rev-parse HEAD` returns the subject; `git status --porcelain` returns
only `?? .goals/`, untracked and not gitignored, holding seven files (two plan copies and five
`.commitmsg` drafts), none of them a member and none of them this round's. `git hash-object` on all
ten tracked paths above returns the ten blob ids tabled. `.harness/review-pending.json` names this
subject with `dispatched_at 2026-08-30T03:55:50+00:00`, so the window is mine. `origin/dev` is at
`fff2203`; the subject is unpushed (`E8`).

## 2. `HARNESS-DECISIONS.md` `§live`, read in full

Owed at every opening whether or not the layer read is waived, not a member, cited by section and
never by blob (`E10`). The file is byte-identical to its state at `e88094c` (blob
`c02118c65a1bb2d2cdba3cd5a183af674c81efa2`). `§live` runs `:30-232` and holds **ten** entries:
`HD-66` `HD-65` `HD-62` `HD-59` `HD-41` `HD-36` `HD-35` `HD-34` `HD-23` `HD-9` — the same ten the
previous read counted. Nothing in `§live` conflicts with the layer as I read it. Three bear on this
subject:

- **`HD-36` ②** — *`E10` 优先句 … 把 design test **收窄回自由通道**，不再伸进 must-fix 通道.* This is
  the ruling that decides whether the amendment could take the channel it took. It is `live`
  precisely because the layer carries none of it; see **O-2**.
- **`HD-41` ① and ④** — scope before assertion, and a class scan with its grep output pasted into
  the commit body before a finding is fixed. Both are obligations on the commit I am reading and
  both are met: the body carries the ten-site scan with its output, and its absolute quantifiers
  carry their scope. Every quantifier below carries mine.
- **`HD-59`** — corrections go forward. Nothing here rewrites an earlier record. Where a figure of
  mine differs from the previous read's I name the measurement that moved it (§3, the class scan's
  line numbers).

## 3. The amendment, checked byte for byte against what the finding supplied

**Both replacements are the reader's bytes and nothing else.** The strongest form of this check is
not a diff read by eye but a reconstruction: take each file at `e88094c`, apply *only* the
replacement `M-1` supplied, whitespace-normalize, and compare with the file at `5a9c0fd`.

```
RULES old text present pre   -> True     RULES new text present post  -> True
RULES old text gone post     -> True     RULES new text absent pre    -> True
ORCH  old text present pre   -> True     ORCH  new text present post  -> True
ORCH  old text gone post     -> True     ORCH  new text absent pre    -> True

RULES.md         : whole file == pre with ONLY that replacement applied -> True
ORCHESTRATION.md : whole file == pre with ONLY that replacement applied -> True
```

So each amended member is, modulo whitespace, its `e88094c` self with exactly one substitution.
Nothing else was written, deleted or re-typed, which is what `E10` admits through this channel and
what the body claims. The reflow the body discloses is real and within the files' own widths: the
added lines run 91/85/87/26 and 88/76/27 characters against existing maxima of 136 (`RULES.md`) and
208 (`ORCHESTRATION.md`); two of them are short orphan lines mid-paragraph, which markdown joins and
which changes nothing.

**The class is complete — my scan, at this tip, scope = the nine members and the declared rule
file.**

```
$ git grep -n 'harness\.json' 5a9c0fd -- <the nine members and the declared rule>
CONSTRUCTION-CHECKLIST.md:9   EXECUTION.md:14   ORCHESTRATION.md:9  :40  :95
README.md:23  :25              REVIEW.md:9       RULES.md:10  :98
```

Ten sites — the same ten the previous read and the commit body counted; `ORCHESTRATION.md:95` is the
previous read's `:93`, moved two lines by this amendment and by nothing else. Eight say only where a
repository declares its rules or that `policy` names the policy file, and I read each in place to
classify it by hand rather than by grep: `EXECUTION.md:13-14` and `REVIEW.md:8-9` say the
construction-side rule file is *declared under `rules` in its `harness.json`* and claim no channel;
`ORCHESTRATION.md:9` addresses the orchestrator's own reading, not a dispatch prompt. Exactly two
asserted the dispatch channel and both are the ones rewritten. **I widened the scan** past the token
the body keyed on, in case a site asserted the channel without naming the file: `git grep -i
'declar'` over the same ten paths returns 44 lines, and none of those outside the `harness.json` set
asserts anything about what a dispatch prompt names. No third site.

```
$ git grep -n "names the declared files in every prompt" 5a9c0fd     # whole tree
migration/document-work-assurance-v3/v3-cold-read-e88094c.md:161, :186, :246
```

The old wording survives only inside the read record that quotes it.

**The ground truth the amended text now describes as an obligation is still what it was.** The
amendment would have been unnecessary if item H's code had landed; it has not.

```
$ git show 5a9c0fd:tooling/rsclib/document_harness/dispatch.py   ->  1005 lines
   load_harness_config 0    harness.json 0    HarnessConfig 0    .rules 0
   declared_rules 0         scan_surfaces 0
   CONSTRUCTION_EXECUTOR_CHARTER = "document-harness/CONSTRUCTION-CHECKLIST.md"   (:776)
```

So `dtw dispatch` still derives the construction executor's charter from a constant, and the amended
sentences are correctly in the obligation voice rather than the indicative.

**The new factual assertion, run rather than described (`E3`).** The `RULES.md` replacement adds a
uniqueness claim — *the one of the four stated as an obligation on the command rather than as
behaviour already built*. It is true, read at the width its own qualifier gives it. Of the four
readers: reader 1 is unbuilt, as measured above; readers 2 and 4 are built, and I re-ran them here
rather than inheriting them, because this new claim is what depends on them — `scanned_paths()`
returns the nine members then `document-harness/CONSTRUCTION-CHECKLIST.md`, and `sweep_refs.py`
imports that same function (`:69`) and tallies over *members and declared rule files* (`:93`);
`caller.render_harness_config()` returns `{"policy": null, "rules": []}`, both fields present,
written by `init_target:154`. Reader 3, *the orchestrator reads `policy`*, is also an obligation
rather than built behaviour — but it is an obligation on a **role**, carried by `ORCHESTRATION.md`'s
*Reading the caller's policy file*, not on a command, so the qualifier *on the command* is what makes
the uniqueness claim hold. Read without that qualifier it would be false; read as written it is true.

**Does the design test fire? No — and by two independent routes.** `E10` makes an amendment design,
and opens a round, when it adds a clause to any rule or replaces text *so that what a rule requires
changes*. I checked the substantive route rather than accepting the body's assertion of it: plan
ruling 9 already places this exact obligation on the command — *"`dtw dispatch`, in every mode, adds
one line to the prompt naming the declared rules, to be read after the charter"* — which I read at
`document-harness/plans/core-only.plan.md` rather than taking from the body, and ruling 35 re-states
it as *"ruling 9's last sentence the obligation: that dispatch, wherever it lands, names the declared
rules too"*. So the obligation pre-existed the amendment, and the layer's own prior text asserted the
same content in the stronger indicative form. The amendment therefore *weakens* the sentence — from
accomplished fact to acknowledged obligation — and requires nothing new. The second route is
`HD-36` ②, which exempts the must-fix channel from the design test outright; see **O-2**. Both hold,
so the round correctly did not open.

**Not filed, but checked.** `E10`'s list opener still reads *Four readers, each a decision that
changes when the file is absent*, now sitting above an item that concedes it is not built. I looked
for an inconsistency and did not find one worth a finding: plan ruling 9 frames it identically —
*"Four readers, each a decision that changes when the file is absent (`E6`): `dtw dispatch`, in every
mode, adds one line…"* — pairing the same `E6` justification with the same unbuilt reader, so the
layer now mirrors its own ruling exactly, and the qualifier tells a reader the truth in the same
clause.

**Guards and tests, my runs, at the subject.**

```
$ python -m pytest tests -q          (run from tooling/)   853 passed in 148.91s   exit 0
$ python tooling/hooks/layer_path_check.py        exit 0
$ python tooling/hooks/candidate_path_check.py    exit 0
$ python tooling/hooks/review_freeze_check.py     exit 0
$ python tooling/sweep_refs.py
-- 13 caller-held or unresolvable references over 10 members and declared rule files
   (all 13 NAMETOK, the compliant caller-held form)
```

The `layer_path_check` exit above is **worth less than it looks and I will not lean on it**: the
guard scans `git diff --cached` added lines only, so on a clean worktree it scans nothing. To get a
measurement that means something without staging anything or disturbing the index, I replayed the
guard's own `unresolved_tokens` / `scanned_paths` over exactly the lines `5a9c0fd` adds:

```
document-harness/RULES.md          4 added lines, scanned
document-harness/ORCHESTRATION.md  3 added lines, scanned
GUARD REPLAY -> failures: []
  ORCHESTRATION.md: `harness.json` -> skipped (no slash, so outside PATHLIKE)
```

Zero failures on the real added lines. The one backtick token among them is skipped rather than
resolved, which is the guard's documented shape limit and `E10`'s clause to hold, not a defect here.

**The membership sentence is untouched and still agrees with its machine mirror.** Parsed the
backticked paths out of `E10`'s first sentence at the subject and compared with
`layer_path_check.LAYER` as ordered tuples: `sentence: 9  LAYER: 9  equal: True`. Rider `E10-sync`'s
check does not arise, as the body says.

**Process conformance, run second (`R3`).** `E8`: the title `V3-CORE-ONLY-CODE-E10-AMENDMENT-M1-v1`
names the round and follows the `V3-<ROUND>-<KIND>-v<n>` shape the branch's own recent history uses;
the body names the kind in its first two words, is one paragraph, carries no trailers, and names both
changed paths in its closing sentence; the commit is new, unpushed, and its change boundary is the
two sites `M-1` named. `E9`: no FULL has occurred in round `CORE-ONLY-CODE` — the round opened at
`e88094c` and the only commits since are the read record and this amendment — so the amendment spends
nothing, which is what `E10` says of the pair anyway. `E10`'s pre-read reliance provision does not
apply and was not invoked: the body states the amendment *"owes the independent re-read of its own
text before any round relies on it"*, which is the deferral declined rather than taken. `R10`: the
previous read's `L-1` is not banked in `HARNESS-RIDERS.md` (byte-identical to its state at
`e88094c`), and correctly not — `R10` says an `E10` amendment commit *admits only the answers to a
read's must-fix findings*, so it could not carry the row. The routing is recorded in committed text
(*"The record's L-1 and O-1 route to the executor with the instruction"*), and the finding itself is
committed at `69a9a71`, so nothing load-bearing is living in chat (`R2`). The row is still owed.

## 4. Findings

### O-1 (observation) — the text is fixed; the channel `M-1` named is still absent, and the amended layer obliges no one to substitute for it

`M-1`'s defect had two layers: the layer text said a channel existed, and the channel did not exist.
The amendment closes the first exactly and cannot close the second — building it is item H's, and
acceptance 11 is what measures it. Nobody should read this record as closing `M-1`'s underlying gap.

What remains after the amendment: a repository that declares its own rules now reads, correctly, that
`dtw dispatch` *is held to* naming them and that this is not built. It is not told to do anything in
the meantime, and nothing in the amended layer obliges its orchestrator to hand those rules by
another channel. That is not a defect in the amendment — supplying such an obligation would add a
clause, which `E10`'s design test makes a round, and the reader deliberately supplied no such bytes —
but it is the state at the subject and it is worth seeing whole.

**I am the live instance, again.** The prompt that reached me is byte-for-byte
`dispatch.READ_PROMPT` (rendered in-process, not through the CLI, so as not to write a second freeze
marker over the one carrying my own subject), with `{charter}` bound to the review-contract stub. It
names one charter and no declared file. I reached `document-harness/CONSTRUCTION-CHECKLIST.md` —
this repository's declared rule — only because the stub's own supersession sentence points at it. In
a repository whose declared rule is not the charter's named successor, that chain does not exist and
the cold reader gets nothing. This is the same measurement the previous read made one commit earlier;
the amendment did not change it, nor claim to.

One further property of that same constant, observed and not filed separately: `READ_PROMPT`'s
subject line reads *the instruction layer at `{commit}`*, which for an amendment re-read is wider
than `E10` says the subject is. A reader who took it at its word would read more than it owes and
reach no wrong answer, so this changes no outcome; the narrowing reached me in the addendum and, as
the header records, was independently derivable from `E10` plus the commit.

### O-2 (observation) — what actually authorizes this channel is `HD-36` ②, and neither the finding nor the amendment cites it

`E10`'s design-test sentence is unqualified — *an amendment adding a clause to any rule, or replacing
or deleting text so that what a rule requires changes, is design and opens a round* — and only the
tie-breaker after it is scoped, to the free channel. On the layer's text alone the design test reads
as covering every amendment, a must-fix answer included. The exemption lives in `HD-36` ②, whose own
status block says so in as many words: *`E10` 的通用 design test 仍无限定地盖住每一个 amendment，
豁免只由本条承载*, and which is `live` for exactly that reason, needing a design round to be carried
in the layer.

Both `M-1` and the amendment's body settle admissibility the other way — by arguing the design test
does not fire on these particular bytes. As §3 records, that argument holds here on its merits, so
the disposition is right by both routes and nothing is owed. What is worth naming is which route
governs when they come apart: a future must-fix whose supplied bytes *do* add a bound would, under
the merits argument, open a round — and under `HD-36` ②, which `E10` says outranks the layer on
conflict, it must not, because a must-fix is the one class that may not wait. The question and the
conclusion are the user's (`R5`); `HD-36`'s own status block already carries the debt.

### O-3 (observation) — the amendment was authored and applied by the orchestrator, and the layer does not address who may author one

The body discloses it plainly — `Kind: amendment (E10 must-fix channel, orchestrator)`. The pair is
not a round, so `ORCHESTRATION.md`'s three-roles table and `E1`'s exception channel, which bind *a
round* that merges the two work-side roles, do not literally reach it; and `R1` is satisfied
structurally regardless, since the orchestrator holds all four holdings and no executor holds any.

What makes it safe here is narrower than the disclosure: the bytes were the reader's own, applied
verbatim, so no authoring judgment was exercised — and that is a mechanical fact, which §3
establishes by reconstruction rather than by reading the diff. `E10` names the executor as the author
for the case where it would matter — *where the finding supplies no bytes, the fix the executor
writes* — and says nothing about who applies bytes that were supplied. The silence gave the right
answer this time because the verbatim check was available; it would not be available for a must-fix
the reader supplies no bytes for. Recorded, not concluded (`R5`).

## 5. What I read, and the ceilings (`R4`)

**Read in full, end to end:** `document-harness/RULES.md` (249 lines) and
`document-harness/ORCHESTRATION.md` (125) at the subject's blobs — the two amended members;
`migration/document-work-assurance-v3/v3-harness-review-contract.md` (5), my charter;
`document-harness/CONSTRUCTION-CHECKLIST.md` (78), this repository's declared rule;
`migration/document-work-assurance-v3/v3-cold-read-e88094c.md` (418), the record whose must-fix this
answers; `HARNESS-DECISIONS.md` `§live` (`:30-232`, ten entries) and the file's header block; the
subject commit's body in full and its diff in full; `.harness/scan-surfaces.json`;
`.harness/review-pending.json`; `harness.json`.

**Sampled:** the other seven members — `EXECUTION.md:1-22`, `REVIEW.md:1-16` and the eight
non-asserting `harness.json` sites read in place for the class scan, the rest covered by citation to
`v3-cold-read-e88094c.md` on unchanged blobs. `document-harness/plans/core-only.plan.md` — rulings 9,
20–24 and 35, item H, the ruling index. `HARNESS-RIDERS.md` — `read-name-split`, `e10-cannot-see`,
`e10-freeze-exception`, `onboarding-carries-construction` in full, the file's blob compared whole.
`tooling/hooks/layer_path_check.py` — the docstring, `LAYER`, `TOKEN`, `PATHLIKE`, `RUNTIME_PREFIX`,
`unresolved_tokens`, `scanned_paths`, `check`, and `added_lines_by_path`'s header.
`tooling/rsclib/document_harness/dispatch.py` — the four prompt constants and the two charter
constants, the module counted for declaration-reading tokens.
`tooling/rsclib/document_harness/caller.py` — `render_harness_config`, `load_harness_config`.
`tooling/rsclib/document_harness/init_target.py` — `:118`, `:145-155`. `tooling/sweep_refs.py` —
`:28`, `:41`, `:69`, `:93`.

**Probed only:** `document-harness/journal/` (listing; no `CORE-ONLY-CODE` journal exists yet, so
`E3`'s *commit body or the round journal* is discharged by the body); `.goals/` (file listing).

**`UNVERIFIABLE`, stated rather than folded into supported:**

- That this session ran cold, in a fresh context, as its own session. A process claim nobody can
  inspect from the repository — marked, not verified (`R4`). What is structural: I was dispatched
  by, prompted by and scoped by the orchestrator, received `READ_PROMPT` as the generated dispatch,
  and report through this record.
- That the addendum did not narrow what I looked at. The header gives the derivation that makes the
  scope independent of it, and the two agree; I cannot prove the order from the repository, so it is
  marked.
- Whether the amendment commit staged explicit paths rather than `add -A` (`E8`). Not observable
  after the fact; the change boundary is consistent with either.

**Ceilings on my own coverage:**

- A read is not a round and carries no verdict (`R3`). I did not review round 2's work, item H's
  design, or any code beyond what the amended sentences assert about it and what the guard replay
  needed. Where I ran code it was to falsify a sentence, never to certify a module.
- I mutated nothing (`E4` binds a round adding a guard; this adds none), so the guard results above
  are runs, not proofs of binding force. The guard over these two members was mutation-tested at
  `c7f9c8d` by an earlier VERIFY, not by me.
- The `layer_path_check` clean-worktree exit is vacuous and is reported as such; the replay is the
  measurement that carries weight, and it exercises the guard's functions rather than the hook's
  wiring.
- I exercised no `dtw dispatch` mode through the CLI, deliberately — the review-side modes write
  `.harness/review-pending.json`, and a marker written by me would sit on top of the one carrying my
  own subject. Prompt constants were rendered in-process instead.
- Members 2, 3, 4, 6, 8 and 9 were covered by citation, not re-read end to end. If
  `v3-cold-read-e88094c.md` §5's own coverage claim is wrong, my coverage inherits that error.
- Line numbers in this record drift with the next commit.
- `HARNESS-DECISIONS.md`'s `§implemented` was not read; `E10` owes `§live` and only `§live`.

## 6. Record channel (`R6`)

This record is `v3-checkpoint-read-5a9c0fd.md` under `migration/document-work-assurance-v3/`, which
is what `.harness/scan-surfaces.json` declares under `review_record_dirs` and what
`document-harness/CONSTRUCTION-CHECKLIST.md`'s `R6` instance value states. Written in the worktree,
uncommitted; the orchestrator commits it unchanged, title
`V3-REVIEW-RECORD-CORE-ONLY-CODE-5a9c0fd-v1`.

## 7. Routing, for the orchestrator (`R10`)

- **No must-fix.** The `E10` pair `M-1` opened — amendment plus independent re-read — is complete
  with this record, and the amended text may be relied on.
- **O-1, O-2 and O-3 ask for nothing.** `O-1` names what item H still owes and warns against reading
  `M-1` as closed; `O-2`'s debt is already carried by `HD-36`'s `live` status; `O-3` is recorded for
  a case that has not happened yet. None supplies bytes, none banks, none opens a round.
- **Still owed from the previous read, and not by this commit:** `L-1`'s rider row. `R10` barred the
  amendment commit from carrying it; it rides the executor's next commit, as the body says.
