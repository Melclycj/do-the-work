# Cold read — the instruction layer at `cf54a79` (round `STRANGER-GUARDS` opening)

**No verdict.** A read is not a round (`R3`): it spends no budget, carries no verdict, and its
output is findings tiered must-fix / low / observation. Nothing below certifies any text, and
nothing below is banked as any round's FULL.

**Findings: 0 must-fix, 3 low, 5 observations.** No member misdirects an actor at this commit.
The three lows share one family: text that was true when frozen and is stale against a later
ruling, at sites nothing yet re-scans — two sit inside the newly admitted, `E2`-frozen contract
v4 (`L-1` a closed-enum row its own single home contradicts; `L-2` a plan digest that verifies
against nothing in this repository), and one is a decision-log edit the signature commit's body
claims and its diff refutes (`L-3`). All three routes are stated per `R10`; none takes the free
channel — the first two are barred by `HD-20` (bytes on an `E2`-frozen path bank until that
rule's recorded ruling), the third belongs to the user's register.

**What this read discharges.** Three debts the ledger's `CONTRACT-V4` CLOSED entry names
(sentence added by `1bce371`, re-derived here rather than inherited): the opening cold read of
round `STRANGER-GUARDS` (dispatched, not waived — the subject commit's own ruling 4); the first
end-to-end read of contract v4, a 339-line member with no prior read record to cite; and the
independent reads owed by round `CONTRACT-V4`'s member edits, the free-channel application
`f112135` included (its whole scope is member 1, verified from its stat), each read at
per-member digest cost as part of the full member reads below.

**Standing instructions read.** `migration/document-work-assurance-v3/v3-harness-review-contract.md`
(the stub, member 7) → `document-harness/CONSTRUCTION-CHECKLIST.md` in full, both sides, per the
stub's *"It is your standing instruction and its own counterpart; read all of it."*
`HARNESS-DECISIONS.md` header (1–27, its own state machine) plus `§live` (28–160, **eight**
entries — `HD-56`, `HD-44`, `HD-41`, `HD-36`, `HD-35`, `HD-34`, `HD-23`, `HD-9`), which `E10`'s
tail owes at a round's opening. Against the previous read's seven, `HD-56` arrived (the v4
signature entry). `§implemented` and the archive were **not** read end to end — probed for the
ids the members cite (§3.5) and for `HD-20`'s intersection text (§4 `L-3`). Cited by section,
never by blob.

---

## 1. What the subject is, and how it was derived

The dispatch supplied one commit and nothing else. Everything below was re-derived (`R2`).

```
$ git rev-parse HEAD
cf54a79b73d568d1728854e1974b90564ba32c34

$ git status --short | wc -l
0

$ git log -1 --format='%H%n%ad%n%s' cf54a79b
cf54a79b73d568d1728854e1974b90564ba32c34
2026-08-23 20:58:52 +1000
V3-STRANGER-GUARDS-PLAN-v1
```

HEAD is the subject commit and the worktree is clean, so the worktree bytes are the subject
bytes — verified per member with `git hash-object` against `git rev-parse cf54a79b:<path>`,
9/9 MATCH (§2), rather than inferred.

**The subject commit touches no member.** `git show --stat cf54a79b` returns
`document-harness/plans/stranger-guards.plan.md` (106 insertions) and nothing else — a cold
read of standing layer text at a round's opening, not a read of a diff. The plan is not a
member and was deliberately not relied on (`R2`); the commit body's four rulings were read as
the round-opening record they are.

**The freeze window is intact, re-derived rather than assumed.** The gitignored marker
`.harness/review-pending.json` (`.gitignore:18` — untracked by design) names subject
`cf54a79b73d568d1728854e1974b90564ba32c34`, dispatched `2026-08-23T10:58:57+00:00` — five
seconds after the subject commit (10:58:52 UTC). The branch tip is the subject, so no commit
has landed since dispatch (`E9`). This repository's tracked hook runs `layer_path_check.py`
alone (its own comment says so, `E6` the reason), so the window here is discipline, held, not
enforcement — the standing shape rider `self-caller-guards` already banks.

## 2. The member set and each member's blob

The set is `E10`'s own sentence — **"exactly these nine paths and nothing else"** — hand-
transcribed from the checklist at the subject blob, then machine-compared against the guard's
mirror (§3.3). Blob ids per `E10`'s *"a read's record states the blob id of each member it
read, because citation depends on it"*. Line counts are `git show | wc -l`, sizes
`git cat-file -s`.

```
 #  blob                                      lines  bytes  path                                            vs v3-cold-read-b8df15a
 1  7a18cd1cffa9b25fce9f1f37449be5d55c7c70fc    243  19325  document-harness/CONSTRUCTION-CHECKLIST.md      CHANGED (was 31e785f8)
 2  0454c8a59db88fa4c4b599bb7f6de39681489682     38  10511  document-harness/README.md                      CHANGED (was 7591c533)
 3  b187af5c836781a366aeb3c9ef3a1338a9955de0    519  36636  document-harness/EXECUTION.md                   CHANGED (was 3908907a)
 4  86e5ed7ad6792a7548ce968dea3cbcfcc3ee9f3e    319  20627  document-harness/REVIEW.md                      CHANGED (was c84b8288)
 5  9a67401f12da68b8990c4543867f204163d12e32    119   8382  document-harness/ORCHESTRATION.md               same
 6  6d5714923870b4e13e8928221a80df68e563a5ed      5    511  migration/…/v3-harness-operating-contract.md    same
 7  29bdc9fbde6e8db38d601dd2340d4b46a24a296f      5    924  migration/…/v3-harness-review-contract.md       same
 8  614932de40b841ec9777719aea88de04864eb67b    339  21983  contract/Document-Work-Assurance-Contract-v4.md NEW MEMBER (no prior end-to-end read)
 9  09aa869962f592c2f86c9379be0ef3eb7d2232ff     44   2812  schema/…/paragraph-map.schema.json              same
                                              -----
                                               1631  total lines read
```

**The citation channel was available for four of nine and was not taken.** Members 5, 6, 7
and 9 are byte-identical to the blobs `v3-cold-read-b8df15a.md` §2 records — re-derived here
against that record's stated ids rather than assumed — so `E10`'s citation clause would have
covered them. All nine were read end to end anyway; member 8 had no record to cite.

**Where the four changes and the new member came from.** `git log b8df15a..cf54a79 -- <the
nine>` returns exactly four commits, all round `CONTRACT-V4`: `23ca45b` (candidate — v3
renamed to v4 merging both supersessions, which leave the tree; membership sentence ten→eight),
`d0f185c` (the round's one user-approved fix — v4 admitted as the ninth member by user ruling,
eight→nine), `f112135` (free-channel application, member 1 only, 2 insertions 3 deletions),
`3b25f3c` (signature carrier — touches no member bytes; **the signed blob is therefore the
fix leg's**, verified: `git rev-parse d0f185c:contract/…-v4.md` = `614932de…`, unchanged
since). The aggregate member diff `b8df15a..cf54a79` was read in full alongside the standing
text. Both member-editing commit bodies carry the `E10-sync` three-site naming with pasted
sweeps, the `E1` merged-roles disclosure (all four holdings held, per the pre-`HD-55`-norm
shape that round declared), and `d0f185c` records `HD-21`'s membership question and the user's
answer — the disclosures `E10` and `E1` require of the round that creates a member.

`HARNESS-DECISIONS.md` is **not** a member — `E10`'s tail owes it at a round's opening while
denying it membership. It is cited by section, never by blob.

## 3. What was checked, and what the commands returned

Unless a line says otherwise, the scope is **the nine member blobs at `cf54a79b`** and nothing
else.

### 3.1 `E2`'s freeze surface — first read of the one-blob shape

```
$ git ls-tree cf54a79b --name-only -- contract/
contract/Document-Work-Assurance-Contract-v4.md          (exactly one file)

$ git ls-tree cf54a79b --name-only -- schema/document-assurance-v3/ | wc -l
15                                                       (paragraph-map.schema.json among them)

$ git cat-file blob 614932de… | sha256sum
1b1061cbdeb6585ee5b33f3dcf91c2ee376f60f3e92076998d7930b70f7a23fa
```

`E2`'s literal `614932de…` matches the member blob; the sha256 and the 339-line count match
`HD-56`'s signature binding exactly (`git cat-file blob | sha256sum` discipline per `HD-40`);
the surface is one blob plus fifteen pack files = the sixteen items `HD-56` rules. The three
merged sources resolve as blobs in history (`b2dbdf75` / `68031fa2` / `e1a2f26b`, all
`git cat-file -t` → blob), which is what `E2`'s parenthetical and `HD-44` require of them —
immutable, and not what the list governs. `git log --diff-filter=AD -- schema/…` still returns
only `39a21a8`'s re-rooting: no pack file has been added or removed in this repository's
history. **Ceiling, stated rather than folded in** (`R4`): whether today's fifteen are the
2026-08-03 re-baseline's fifteen remains `UNVERIFIABLE` from here — history begins 2026-08-15.

### 3.2 Every path reference in the layer, resolved

**(a) Backtick path tokens**, driven through the guard's own predicate
(`layer_path_check.unresolved_tokens`) over the **whole standing text** of all nine members —
precisely the stock `E10` says the guard never re-scans:

```
all nine members: 0 unresolved.  TOTAL 0
```

The previous read's five frozen-supersession tokens left the layer with their files. For the
first time the layer's path-token debt is zero with no frozen exception in use — contract v4's
own path tokens (schema table, §13.1/13.2) all resolve.

**(b) Relative markdown links** — the blind spot `E10` names by name:

```
64 links checked (http/https/anchor-only excluded); broken: 0
```

**(c) Placeholder-segment tokens** — held by `E10`'s clause alone. Six, unchanged in location
and holder from the previous read's table: the checklist's three record-name forms (`R6` writes
the directory), `EXECUTION.md`'s `<control root>/control/paragraph-map.json` and `REVIEW.md`'s
`<control root>/evidence/review-full.json` (each with *"the control root lives in the caller"*
adjacent), and `REVIEW.md`'s `v3-review-<round>-<subject short SHA>.md` (*"The caller holds
it"*).

**(d) One wikilink** — `[[document-work-assurance-harness-v3.plan|…]]`, contract v4:35. Not a
backtick token, not a markdown link: invisible to (a) and (b) alike. Resolves by basename to
`document-harness/plans/document-work-assurance-harness-v3.plan.md`. The digest beside it is
`L-2`.

### 3.3 The membership sentence and its mirrors (`E10-sync`)

```
E10 (hand-transcribed) == layer_path_check.LAYER : True | n = 9 | distinct = 9 | same order
test_precommit_checks.py EXPECTED (:225-235)     : the same nine, hand-written literals (E5)
test_precommit_hook.py MEMBER (:58 family)       : one member path, still a member
guard diff since previous read                   : LAYER tuple only (-2/+1); behavior code byte-identical
```

The round touched the membership sentence twice and the rider `E10-sync`'s check-item held both
times: three machine sites changed in the same commits, prose legs swept with raw grep output
pasted in the commit bodies. Re-measured here at the subject: root `README.md:58/:83`,
`document-harness/README.md:34` (×3), `ONBOARDING.md:133`, `.githooks/pre-commit:14-15` all
say nine; the hook's *"0 of the 9 it then had"* is the 2026-08-17 historical fact and stays
correctly at nine-of-that-day.

### 3.4 Rule enumerations and the counts the members state about themselves

```
E-rules: 12 (E1…E12, distinct, in order)      R-rules: 10 (R1,R2,R3,R9,R10,R4,R5,R6,R7,R8 — complete)
ORCHESTRATION "nine obligations" table: 9 rows · "three obligations": 3 subsections · roles table: 3 rows
EXECUTION run-template sections: 6 (Pre-freeze gate · Instruction form · Authoring gate ·
  Audit cadence · Regression-battery tiering · Instruction authoring rules)
```

9 + 3 = 12 matches `README.md:24`'s *"nine of its twelve obligations"*; the six sections match
the same row's enumeration and the `:174` stage-marker span. `E10`'s *"exactly these nine
paths"* enumerates nine.

### 3.5 `HD` ids and commit ids cited in the layer

```
HD ids cited: 16 distinct — the previous read's 15 plus HD-56.   Dangling: 0
  (12 resolve in HARNESS-DECISIONS.md — §live: HD-34 HD-35 HD-41 HD-56 among the cited —
   4 in the archive: HD-14 HD-28 HD-39 HD-42)

hex ids in backtick: 21 distinct.
  Resolve here (5): 0d73a5f (commit — EXECUTION's instrument base) · 614932de (v4 blob, E2's
    literal) · b2dbdf75 / 68031fa2 / e1a2f26b (the merged sources' blobs, short in members
    1–2 and full-length in member 8)
  Absent here (13): 418b89c 6fd0ae3 7011916 820b287 838c413 9ba9bbc a22cca0 a8af54c ac1b383
    ddd773a de39b3d f91a7c4 7db177d — all commit-id-shaped, exactly the class E10's "Where a
    cited commit id resolves" clause covers; three (de39b3d f91a7c4 7db177d) are v4's §12–§13
    citations, newly inside the layer with v4's admission and covered the same way. Root
    README.md §"Where the bytes came from" (:14) exists and names the source repository.
```

### 3.6 Factual assertions in the layer, run rather than read (`E3`)

```
$ python -m pytest -q            # from tooling/, per EXECUTION.md's battery bullet
792 passed in 115.46s
$ python -m pytest -q            # from the repository root (what .github/workflows/ci.yml runs)
792 passed in 105.73s
$ python validate_fixtures.py    # migration/document-work-assurance-v3/N0/fixtures/
41/41 cases behaved as declared; failures=0
```

- **792 is this read's own measurement**; the previous read measured 793, and the drop
  re-derives to the round: `test_candidate_checks.py`'s R4 flagged/exempted pair collapsed to
  one merit test when v4 stopped needing a governance exemption (`HD-56` ③ — the retired
  `governance-exemptions.json` entry made real in tests). Both member-editing commit bodies
  state 792 with the same command; they check out.
- `README.md:33`'s *(41/41 green)* re-derives exactly. Both invocation forms still collect the
  same set here (the previous read's `O-2` shape, unchanged, still unacknowledged in the
  enumeration — that observation stands as written there).

### 3.7 The claims the members make about the dispatch and template code

All run (`E3`), all hold:

- `dispatch.py:429/548/770/776` — the four role constants match `ORCHESTRATION.md`'s and the
  stub's claims: `CONSTRUCTION_ROLE_INSTRUCTION` hard-codes the stub's path;
  `EXECUTOR_ROLE_INSTRUCTION` = `EXECUTION.md`; `CONSTRUCTION_EXECUTOR_CHARTER` = the
  checklist. `cli.py:580-601`: five dispatch flags, one mutually-exclusive required group,
  split 3 review-side / 2 executor-side as `ORCHESTRATION.md` states.
- `test_dispatch.py` `CHARTER_OUTSIDE` (:398 :522 :570) / `MEMBER` (:463) — hand-written
  literals (`E5`); the construction fixtures carry `{charter}` as a substitution, not the path.
- `grep -ri orchestrator tooling/rsclib/` → 0 hits: *"no dispatch prompt names it, and none
  should"* holds module-wide.
- `EXECUTION.md`'s tiering pin list: `test_readme_enumeration.py` pins
  `document-harness/README.md` ✔; the layer-path mirror ✔ (§3.3); the two shipped templates
  (`decision-log.md`, `rider-bank.md`) under `document-harness/templates/`, copied by
  `init_target.py` (`TEMPLATE_DIR`, `_copy_templates`) ✔; `CONTRACT_PATH` in
  `tooling/rsclib/document_harness/__init__.py:41` pins the **v4** path ✔ — re-pointed by the
  round as its commit body states.

### 3.8 Contract v4's own verifiable assertions — the new member's first read

The 339 lines were read end to end and every claim that names a checkable property of *this*
repository was run:

- **§3 table**: all seven schema links resolve (§3.2b); the `DocumentWorkSpec` owner cell reads
  *"the run's executor (its WorkSpec author)"* — the `wspec-owner` rider's contract-side
  redemption, verified against the row's own text.
- **§5 enums vs their declared single home** (`common.schema.json`): WorkState status 9/9 ✔,
  audit result ✔, both review-verdict rows ✔ (`review.v2.schema.json` root `schema_version`
  const `"2"` ✔), decision phases ✔, LocalCheckSpec kinds 6/6 ✔ (`checkKind`). **One row
  fails**: Verification mode — `L-1`.
- **§13.1**: v2 subject binding and no-cross-version-fallback match `review.v2.schema.json`;
  the SHA-1/SHA-256 digest-strength disclosure is present as described.
- **§13.2**: `DIGEST_PROTECTED_FIELDS` = exactly the five fields named
  (`assurance_state.py:81-89`) ✔; `pointer` / `pointer_to` / `pointer_for` all exist with the
  described division ✔; `pointerRef` requires only `path` ✔; `digestRef` requires
  `[path, digest_sha256]` ✔; `instruction_ref` is a `frozenFileRef` requiring
  `[path, revision]` ✔ (all three read out of `common.schema.json`); `run_bind_v2.py` authors
  `review_ref` ✔.
- **Frontmatter and §14**: no self-carried approval state; signature owner named as the `HD`
  entry — and `HD-56` exists, binding this exact blob (§3.1). The R4 governance-scan test now
  asserts the real contract passes on its own merit, which this shape is.
- **§intro's delta claim** (*"Where wording differs … the change is one of the enumerated
  deltas … nothing else was rewritten"*): not re-audited line-by-line — the round's FULL did
  that (its record reports the merge byte-核净, verbatim ratio 1.0000) and a read does not
  repeat a FULL. What this read adds is the two places where **verbatim carriage itself** is
  the defect: `L-1`, `L-2`.

### 3.9 What the previous read left, reconciled

- Its `L-1` (R6's two record filenames, criterion nowhere) is banked as rider
  `read-name-split`, accurately describing the current text — `R6` and `E10`'s cold-read
  sentence are byte-unchanged in the relevant clauses. This read followed the 58-record
  precedent: cold read at a round's opening → `v3-cold-read-<sha>.md`.
- Its `O-1` (rider `py-convention`): substance unchanged — `EXECUTION.md`'s battery leg is
  still bare `python`; the row's cited line drifted `:364`→`:365` (the round added one line
  above it). The row names file and fix shape, so it still routes; noted for the redeemer.
- Its `O-5` (dispatch wrapper): recurred in the same shape — `O-4` below.

## 4. Findings

### `L-1` (low) — contract v4 §5 lists an enum value its declared single home deleted

`contract/Document-Work-Assurance-Contract-v4.md:133`:
`| Verification mode | `local_check · review_only · local_check_and_review` |` — under the §5
heading *"Closed enums (single home: common.schema.json)"*. Measured at the subject:
`common.schema.json#/$defs/verificationMode` = `["local_check", "review_only"]`. The both-modes
value was deleted by SIMP-A1 (recorded user ruling 2026-08-05), and member 3 says so in prose
(*"The both-modes value is deleted from the enum"*, EXECUTION.md, with the design rationale).
The row is inherited byte-identical from the frozen v3 source (`b2dbdf75:121`, signed
2026-07-20 — true when signed, stale at merge time); neither the round's FULL nor its VERIFY
mentions it, and the delta plan does not enumerate it, so the carriage is consistent with the
round's verbatim discipline and the staleness survived it.

**Downstream decision that goes wrong**: a WorkSpec author reading the operative contract —
which is what §14 makes v4 — authors `local_check_and_review` and is refused, because
`document-work-spec.v2.schema.json:151` refs the two-value home (**fail closed, measured** —
the enum ref, not a local copy). So the machine catches the instance; what stands is the
operative contract and a member disagreeing about a closed enum's membership, on the exact
surface (§5) whose stated job is to be the authoritative table.

**Routing** (`R10`): the fix bytes land on a path `E2` freezes, and v4 sits in `HD-20`'s
intersection (now explicitly two paths) — so the finding **banks until `E2`'s recorded ruling
exists**, however appliable the bytes (drop `· local_check_and_review`, or annotate the row as
v1-history the way §13.1 handles version boundaries). Same route and same shape as riders
`wspec-owner` (remaining schema-title sites) and `hi-schema-gloss`.

### `L-2` (low) — contract v4's plan digest verifies against nothing in this repository

`contract/…-v4.md:34-36` binds its plan authority as *"Authored under the user-approved plan
[[document-work-assurance-harness-v3.plan|…]] (plan SHA-256 `9B08CD00…F171F`)"*. Measured: the
plan at `document-harness/plans/document-work-assurance-harness-v3.plan.md` hashes
`37EA94BD…`, its only other blob in this repository's history (`39a21a8`) hashes `8ECA2A0E…`
— neither matches. The sentence is inherited byte-identical from the frozen v3 source
(`b2dbdf75:23-24`); the digest presumably binds the caller-era plan bytes at the 2026-07-20
signing, which is `UNVERIFIABLE` from here (history begins 2026-08-15; the plan was moved and
re-rooted after extraction). No adjacent text says so.

**Downstream decision that goes wrong**: a reader — the publicization batches' stranger
audience in particular — verifying the contract→plan binding by this digest concludes mismatch
or tampering, with the correct explanation held only by provenance history it has no pointer
to. Nothing machine-checks this digest, so no verdict path moves — low, not must-fix.

**Routing** (`R10`): bytes inside v4 take the same `E2`/`HD-20` bank as `L-1`. A fix **outside
the frozen bytes** — one clause on the dh-README contract-v4 row, or the plan row, saying the
digest binds the caller-era signing bytes — supplies no frozen bytes; whether to take that
route instead is the user's, via the orchestrator. Bank with both stated.

### `L-3` (low) — the signature commit's body claims an `HD-44` edit its diff does not contain

`3b25f3c`'s body: *"HD-44's consequence line and HD-20's intersection enumeration are updated
under the signing authorization (sixteen-item freeze surface; two paths in the E2xE10
intersection)."* Measured: the commit's diff over `HARNESS-DECISIONS.md` contains four hunks —
`HD-56` inserted, `HD-35` and `HD-40` third-signing bullets, and `HD-20`'s enumeration
(updated ✔, *"2026-08-23 起共两件"*). **No hunk touches `HD-44`**, whose consequence line
still ends *"这十八件"* at the subject; no later commit touches the file
(`git log 3b25f3c..cf54a79 -- HARNESS-DECISIONS.md` is empty). The ledger's `CONTRACT-V4`
entry repeats the claim (*"`HD-44`/`HD-20` 枚举随 `HD-56` 同批更新"*).

**Downstream decision that goes wrong**: `§live` is the one section every cold read must read,
and it now carries two live entries three entries apart disagreeing on the freeze-surface
enumeration — `HD-56` says sixteen, `HD-44`'s consequence line says the eighteen of its own
date without a date-guard on that clause. A reader who takes `HD-44`'s number derives a freeze
surface containing three blobs that left the tree. No permissible action actually flips —
the three source files are history and nothing can write them; `E2` and `HD-56` agree and
outrank — so this is low. The immutable commit body asserting an edit its diff refutes is the
`E3` shape (a characterization no command established), noted here as the record channel `E8`'s
errata kind exists for.

**Routing**: the fix is the already-claimed-as-authorized `HD-44` edit actually landing — a
decision-log edit, the user's register (only the user flips or amends entries; a session
proposes, `E1`/`R5`), and ledger-correction class for the ledger's sentence (the 2026-08-03
ledger-batch ruling: no round, user ruling is the gate). Put to the user by the orchestrator;
this read supplies the location and the ground truth, deliberately not the register bytes.

### `O-1` (observation) — the member-set transition executed clean, twice in one round

The membership sentence went ten→eight (`23ca45b`) then eight→nine (`d0f185c`, v4 admitted by
user ruling answering the FULL's `O-2` through `R5`, `HD-21`'s record kept in the commit body
and later `HD-56` ②). Both times the three machine mirrors moved in the same commit and the
prose legs were swept with output pasted — rider `E10-sync`'s per-touch check-item, verified
held (§3.3). The `E1` exception channel was exercised in the declared pre-`HD-55` shape (all
four holdings stated in `23ca45b`); the subject commit's round opens under the `HD-55` norm
with all five dispatches cold, this read being the first of them.

### `O-2` (observation) — the retired-contract stubs now carry the layer's only supersession pointers

With the two contract supersessions gone, members 6 and 7 (the 5-line stubs) and the E10
resolution clause are what keep `7011916` and the other caller-commit citations legible. The
stubs' three testable claims all still hold (§3.7). Nothing acts wrongly; recorded because the
stubs are now load-bearing for provenance in a way the previous ten-member shape shared with
the supersessions, and `STRANGER-PROOF`'s second-caller walk (the round this read opens toward)
is where that load is next exercised — rider `amend-exempt-caller` already banks the one known
soft spot.

### `O-3` (observation) — the guard's standing-text debt is zero for the first time

0 unresolved backtick tokens across all nine members with no frozen-bytes exception in use
(§3.2a) — the previous read's five frozen tokens left with the supersessions, and v4's own
tokens resolve. The guard's behavior code is byte-identical to what the previous read
exercised branch-by-branch; only its `LAYER` tuple changed. The `E10` clause's blind-spot list
was therefore not re-exercised here beyond the live-predicate scan; riders `e10-cannot-see`
(the list is still short two shapes) and `submod-index` stand as written — and the subject
round's own plan takes `submod-index` up, which is the correct surface finally arriving.

### `O-4` (observation) — the dispatch carried the same wrapper shape as the previous read's `O-5`

The prompt this reader received matches `tooling/tests/fixtures/expected-read-prompt.txt` line
for line, preceded by one orchestrator-session line naming the repository root and its
worktree-directive. Not load-bearing (a transport fact, checked: the root is this repository),
not a finding; recorded because the fixture's own closing sentence promises nothing is
restated, and the drift that would matter is the first wrapper that carries something the
layer does not say.

### `O-5` (observation) — rider table currency after the round

Re-derived against the subject: `wspec-owner`'s contract-side half-redemption matches v4 §3's
actual row; `read-name-split` accurately describes the unchanged `R6`/`E10` text;
`py-convention`'s target line is off by one (`:364`→`:365`, substance intact); `hi-schema-gloss`
and `PD`'s `CONTRACT-V4` touch-notes match what the round's commits show. One row interacts
with this read's findings: `L-1` and `L-2` join the `wspec-owner`/`hi-schema-gloss` family
(frozen bytes stale against a later ruling, banked on `E2`'s ruling) — three riders and two
lows now wait on the same class of recorded ruling, which is the accumulation shape `R5` says
to report and not conclude on: whether one `E2` ruling should sweep the class is the user's
question.

## 5. Coverage — what was read in full, what was sampled, what was only probed (`R4`)

- **Read in full at the subject blobs:** all nine members, 1 631 lines. Blob ids in §2. No
  member was covered by citation, though four were eligible.
- **Read in full outside the member set:** `HARNESS-DECISIONS.md:1-160` (header + `§live`,
  eight entries); the aggregate member diff `b8df15a..cf54a79` and all four member-touching
  commits' stats and full bodies; `tooling/hooks/layer_path_check.py`; `.githooks/pre-commit`;
  `HARNESS-RIDERS.md` (all 32 rows); `CONSTRUCTION-LEDGER.md` (header, pointer roll, backlog —
  the whole current file); `tooling/tests/fixtures/expected-read-prompt.txt`;
  `v3-cold-read-b8df15a.md` (the previous read, for its blob table and to reconcile its
  findings); the subject commit's body; `3b25f3c`'s full diff over `HARNESS-DECISIONS.md`.
- **Sampled:** `dispatch.py` (four role constants, the construction-prompt head),
  `cli.py:575-604`, `test_dispatch.py` (the literal constants),
  `test_precommit_checks.py:225-237`, `tooling/rsclib/document_harness/__init__.py:41,249-250`,
  `assurance_state.py` (docstring head, `DIGEST_PROTECTED_FIELDS`, the three pointer
  signatures), `run_bind_v2.py` (review_ref sites), `common.schema.json` (its enum `$defs` and
  three ref shapes), `review.v2.schema.json` (version key, subject),
  `document-work-spec.v2.schema.json` (description, verification_mode wiring),
  `local-check-spec.schema.json` (kinds), root `README.md:14-22,58,83`,
  `document-harness/ONBOARDING.md:51,77,133`, `test_readme_enumeration.py` (pin sites),
  `init_target.py` (template sites), `git log --follow` over the v3 plan file plus sha256 of
  its two blobs.
- **Probed only:** `HARNESS-DECISIONS.md` `§implemented` and the archive — grepped for the 16
  cited ids and read `HD-20`/`HD-21` entries only; the `CONTRACT-V4` FULL and VERIFY records —
  grepped for `9B08CD` / `local_check_and_review` / the v4 blob id, deliberately not read as
  findings sources (`R2`); `document-harness/plans/stranger-guards.plan.md` and
  `contract-v4.plan.md` — not relied on (`R2`), the latter grepped once for the enum row.
- **Not established (`UNVERIFIABLE`, stated rather than folded in):** whether the fifteen pack
  files are the 2026-08-03 baseline's (§3.1); whether `9B08CD00…` matches the caller-era plan
  bytes at the v3 signing (`L-2` — the repository that could answer is not this one); the
  caller repository's five battery legs (not owed here, per member 3); CI status (never run —
  push remains the outstanding user action the `PUB-FACADE` closeout records).
- **Process claims are marked, not verified** (`R4`): that this read ran in a fresh context is
  a declared identity, not something the repository can lock.
