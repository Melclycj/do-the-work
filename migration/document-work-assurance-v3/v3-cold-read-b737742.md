# Cold read — the instruction layer at `b737742` (batch `CORE-SET`, round 3 opening)

**No verdict.** A read is not a round (`R3`): it spends no budget, carries no verdict, and its
output is findings tiered must-fix / low / observation. Nothing below certifies any text, and
nothing below is banked as any round's FULL.

**Findings: 0 must-fix, 2 low, 2 observations.** The lows: contract v4 `:36` carries the one
followable cross-tier link that round 2's own demotion criterion reaches and `HD-61`'s
enumeration missed, and the guard is structurally blind to its form (`L-1`); and `R9`'s
terminal route — *rides the next batch* — was exercised once between the last read and this one
and produced nothing, because it names no carrier (`L-2`). The observations: the signature move
fixed the pointer's **form** and not its **tier reachability**, while its own rationale reads as
if it had fixed both (`O-1`); and `README.md:24`'s *"nine rows"* was falsified by this same
round's item N, under the reading the previous read verified it by (`O-2`).

**All nine members were read end to end** — 1,648 lines — so nothing here rests on `E10`'s
citation clause. The citable set was computed anyway (§2) and would have been six.

**This read discharges three deferred obligations.** `07ef526` relied on two member edits before
their read under `E10`'s deferral clause, and `b737742` corrected that forward to **three**
members with contract v4 among them (`CONSTRUCTION-LEDGER.md:186`, carrying VERIFY `V-1`).
All three were read at the subject blob here.

**The dispatch withheld what it should withhold.** The prompt is `dispatch.READ_PROMPT`
(`tooling/rsclib/document_harness/dispatch.py:671-684`) verbatim, with `{charter}` and `{commit}`
substituted and nothing appended — no member table, no round name, no scope. The member set below
was derived from `E10`'s own sentence at the subject blob. No chat-only load-bearing material
(`R2`).

**Standing instructions read.** `migration/document-work-assurance-v3/v3-harness-review-contract.md`
(the stub, member 7) → `document-harness/CONSTRUCTION-CHECKLIST.md` in full, both sides, per the
stub's *"It is your standing instruction and its own counterpart; read all of it."*
`HARNESS-DECISIONS.md` lines 1–162: the header (1–29) plus `§live` (30–162), which `E10`'s tail
owes at a round's opening. **`§live` now carries eight entries, not the ten the previous read
recorded** — `HD-56` left as `superseded` and `HD-60` / `HD-61` as `retired`, all three archived
during round 2; the survivors are `HD-59`, `HD-44`, `HD-41`, `HD-36`, `HD-35`, `HD-34`, `HD-23`,
`HD-9`. `§implemented` and `HARNESS-DECISIONS-archive.md` were **not** read end to end — probed
by id only. Cited by section, never by blob.

**Why this name.** `R6` offers two read filenames and the layer defines neither; this dispatch
lands at a round's opening, which is the only read shape `E10` does define, so it takes
`v3-cold-read-`. That the criterion is missing is already banked as rider `read-name-split`, and
this is not re-filed.

---

## 1. What the subject is, and how it was derived

Everything below was re-derived from the repository (`R2`).

```
$ git rev-parse HEAD
b737742c68ba9260d87d704d56c6103685f097fc

$ git status --porcelain
?? .goals/

$ git log -1 --format='%H%n%ci%n%s' b737742
b737742c68ba9260d87d704d56c6103685f097fc
2026-08-27 00:50:32 +1000
V3-CORE-SET-SIGNATURE-CLOSEOUT-v1
```

HEAD is the subject commit. The one worktree entry is untracked and outside every member path,
so the tracked worktree bytes are the subject bytes — verified per member with `git hash-object`
against `git rev-parse b737742:<path>`, **9/9 MATCH** (§2), rather than inferred.

**The subject commit touches no member.** It is round 2's closeout: `CORE-SET-SIGNATURE` CLOSED,
batch `CORE-SET` with rounds 1 and 2 closed and round 3 remaining. Its body names round 3
`CORE-SET-CODE` (items G and H) as still open, which is the round this read opens.

**The freeze window is intact, re-derived rather than assumed.** The gitignored marker
`.harness/review-pending.json` names subject `b737742c68ba9260d87d704d56c6103685f097fc`,
dispatched `2026-08-26T16:25:32+00:00`. The branch tip is the subject, so no commit has landed
since dispatch (`E9`).

`document-harness/plans/core-set.plan.md` is not a member and was **not read** — no finding below
rests on it. Round 3's declared scope is taken from `b737742`'s own body and from
`CONSTRUCTION-LEDGER.md:191-192`, both of which are quoted where used.

## 2. The member set, each member's blob, and the coverage arithmetic

The set is `E10`'s own sentence — **"exactly these nine paths and nothing else"** —
hand-transcribed from the checklist at the subject blob, then machine-compared against the
guard's mirror and the test's. All three agree; the prose leg has no guard, which is banked as
rider `E10-sync`.

```
$ git rev-parse b737742:<path>   /   git rev-parse d3ba221:<path>

 #  blob @ b737742                              lines  bytes  path                                            vs d3ba221
 1  fce40914cb9c9cfd16a59dd2b6f8f9167656e274     257  20536  document-harness/CONSTRUCTION-CHECKLIST.md      CHANGED (was 3d049a13)
 2  0a4da19b0d522d307997f681d5dec333b9349486      30   9114  document-harness/README.md                      CHANGED (was c43b8e87)
 3  234fdddf974e580d22a1a26b54587d11c24863b3     524  37011  document-harness/EXECUTION.md                   same
 4  395995d45991670dc67e2eb616624c44b30ec123     320  20688  document-harness/REVIEW.md                      same
 5  a9e9f75e484f40f4a1014e5d68ed6c73aa5fbdc2     119   8352  document-harness/ORCHESTRATION.md               same
 6  6d5714923870b4e13e8928221a80df68e563a5ed       5    511  migration/…/v3-harness-operating-contract.md    same
 7  29bdc9fbde6e8db38d601dd2340d4b46a24a296f       5    924  migration/…/v3-harness-review-contract.md       same
 8  5dfb7b64265c821c715f23de52824beeadea3405     344  22350  contract/Document-Work-Assurance-Contract-v4.md CHANGED (was dfc983d2)
 9  09aa869962f592c2f86c9379be0ef3eb7d2232ff      44   2812  schema/…/paragraph-map.schema.json              same
```

The two machine mirrors, compared rather than assumed:
`tooling/hooks/layer_path_check.py:37-47` `LAYER` and
`tooling/tests/document_harness/test_precommit_checks.py:229-239` `EXPECTED` — nine entries each,
identical to `E10`'s prose, in the same order.

**Citable set, computed and then not used.** Three members changed since `v3-cold-read-d3ba221.md`,
so six would have been citable against it (members 3–7 and 9). All nine were read end to end
regardless; no finding below rests on a citation.

**Where the three changes came from.** `git log d3ba221..b737742 -- <the nine>` returns exactly
one commit that touches a member out of the range's four:

- `07ef526` `…-SIGNATURE-ITEM-F-v1` — members 1, 2 and 8. Contract v4's signature carrier moves
  from `HD-56` in the decision log to the new root file `CONTRACT-V4-SIGNATURE.md` (three sites)
  and five citations demote to name + holder; `E2`'s v4 blob literal follows to `5dfb7b64…` and
  its binder clause renames; `README.md:16` names the new carrier, closing the previous read's
  `L-1`.

The other three commits in the range (`a554c0b`, `5e5bebf`, `b823506`) touch
`migration/document-work-assurance-v3/` review records and registers, not members.

**The deferral is discharged here.** `07ef526`'s body claims *"Two members are edited here and
both edits ride E10's deferral channel"*; it edited **three**. The round corrected that forward
rather than in place (`HD-59`), in `b737742`'s body and in
`CONSTRUCTION-LEDGER.md:186` — *「本轮改动的是三个在仓成员，不是两个——契约 v4 是第三个，其字节
欠独立 read 随下轮开轮」*. Members 1, 2 and 8 were read at the subject blob end to end, at more
than per-member digest cost, so the debt is paid in full rather than by digest.

## 3. The read

### 3.1 The signature re-siting (members 1, 2, 8) — every leg checked against its own source

| claim, in the member text | check | result |
|---|---|---|
| `E2`: contract v4 is blob `5dfb7b64…` | `git ls-files -s contract/…v4.md` | `5dfb7b64265c821c715f23de52824beeadea3405` ✓ |
| `E2`: the signed blob remains `614932de…`, bound by `CONTRACT-V4-SIGNATURE.md` | the carrier's own text | *"Exact blob signed: `614932de40b841ec9777719aea88de04864eb67b` — 339 lines"* ✓ |
| `E2`: that record succeeded `HD-56` on 2026-08-26 | `HD-56` in the archive + the carrier | both directions of the pointer present ✓ |
| `E2`: written under recorded rulings `HD-60` / `HD-61` of 2026-08-26 | `HARNESS-DECISIONS-archive.md:28,59` | both entries present, both `retired` after consumption ✓ |
| `E2`: the pack is **fifteen** files | `git ls-tree -r --name-only b737742 schema/document-assurance-v3/ \| wc -l` | `15` ✓ |
| `README.md:16`: signature state is `CONTRACT-V4-SIGNATURE.md` | file exists at the root; no superseded entry named | ✓ |
| the new file is **not** a member (`HD-21` asked and answered) | `E10`'s sentence does not name it; the file says so itself | ✓ |

`E2`'s frozen surface is therefore sixteen items — v4 plus the fifteen-file pack — which is what
`HD-44` in `§live` states. Consistent.

### 3.2 The layer's other factual assertions about code, schemas and counts

Each is a claim written into instruction text that a command could falsify (`E3`). Every one was
run; all hold.

| member claim | check | result |
|---|---|---|
| stub 7: `dispatch.CONSTRUCTION_ROLE_INSTRUCTION` hard-codes its own path | `dispatch.py:548-549` | ✓ literal |
| stub 7: `test_dispatch.py`'s hand-written `CHARTER_OUTSIDE` / `MEMBER` pin it (`E5`) | `test_dispatch.py:398,463,522` | ✓ literals, not the module's constant |
| stub 7: the construction dispatch fixture carries `{charter}` as a substitution | `dispatch.py:558,674,784,800` | ✓ |
| `ORCHESTRATION.md`: **three** review-side and **two** executor-side dispatch modes | the five `*dispatch_of` families | `dispatch_of` · `construction_dispatch_of` · `read_dispatch_of` / `executor_dispatch_of` · `construction_executor_dispatch_of` ✓ |
| `ORCHESTRATION.md`: nine cite-only obligations + three own-text ones | the two tables | 9 + 3 ✓ |
| `README.md:22`: nine of `ORCHESTRATION.md`'s **twelve** obligations are law elsewhere | same | 12 ✓ |
| `README.md:22`: **six** run-template rule sections | `EXECUTION.md` `## ` headings `:183,206,254,291,341,444` | 6 ✓ |
| `README.md:25`: onboarding is **nine** items | `ONBOARDING.md` `### 1`–`### 9` | 9 ✓, and the row's eight labels cover them with *instance files* plural for 3 and 4 |
| `README.md:26`: the caller's hook calls **two** guards, the third runs here | `tooling/hooks/` = `__init__` + 3 guards; `.githooks/pre-commit` present | ✓ |
| `README.md:17`: `contract/` holds exactly one file | `git ls-tree -r --name-only b737742 contract/` | one path ✓ |
| `EXECUTION.md`: `README.md` pinned by `test_readme_enumeration.py` | file + the pinned path at `:3,:57` | ✓ |
| `EXECUTION.md`: two shipped templates under `document-harness/templates/`, copied by `init_target.py` | `git ls-tree` + `TEMPLATES` / `_copy_templates` | 2 ✓ |
| `EXECUTION.md`: contract v4 pinned by `document_harness/__init__.py` | `CONTRACT_PATH`, `:41` | ✓ |
| contract §5: `LocalCheckSpec` kinds, six | `common.schema.json` `checkKind` | exact match ✓ |
| contract §5: verification mode, two | `common.schema.json` `verificationMode` | `["local_check","review_only"]` ✓ both-modes gone |
| contract §5: WorkState status, nine | `common.schema.json` `assuranceStatus` | exact match ✓ |
| contract §5: audit result, decision phases, and all four decision enums | `common.schema.json` + `user-decision.schema.json` | exact match, all five ✓ |

**Read-discipline note (`REVIEW.md`, *Read discipline (Windows)*).** Schema and register loads
were run under explicit UTF-8 (`python -X utf8`, `PYTHONUTF8=1`) rather than through the console's
locale decoding. The previous read recorded a `gbk` `UnicodeDecodeError` on the first attempt;
following the rule from the start, that failure did not recur.

### 3.3 Mechanical scan of standing text — the stock the guard never re-scans

`layer_path_check` reads only the lines a staged diff adds, so all standing text was scanned here
instead, by applying the guard's own `unresolved_tokens` to each member's full bytes
(`tooling/sweep_refs.py`), and independently by resolving every relative markdown-link target and
every wikilink target by hand.

```
$ python -X utf8 tooling/sweep_refs.py
… 15 lines …
-- 15 caller-held or unresolvable references over 9 members

$ python -X utf8 tooling/hooks/layer_path_check.py ; echo $?
0
```

Thirteen are `NAMETOK` bare filenames — the compliant form for a caller-held artifact — and one
site accounts for the remaining two entries: `document-harness/REVIEW.md:93`, reported once as
`LINK` and once as `PATHTOK` (13 + 2 = 15, counted by command, not by eye). That is still the
layer's **only** non-resolving path token, it is `O-2` of the previous read, and it is scheduled:
round 3 item G retires it. **Not re-filed.** The total is unchanged at 15 while its composition
moved — `README.md`'s mount-reaching token is gone and contract v4 `:25` gained a `NAMETOK` — so
the round's demotions traded a resolving-but-mount-reaching reference for a compliant named one
without adding a break.

**The class the round was closing, measured over all nine members** rather than over the sites the
round named. A followable link out of a **product-tier** member into **construction-tier**
material — the tiers as `CONSTRUCTION-INDEX.md` defines them — occurs seven times:

```
markdown links, product-tier member -> construction-tier target
  document-harness/README.md:23        -> document-harness/CONSTRUCTION-CHECKLIST.md   exists
  document-harness/EXECUTION.md:13     -> document-harness/CONSTRUCTION-CHECKLIST.md   exists
  document-harness/REVIEW.md:8         -> document-harness/CONSTRUCTION-CHECKLIST.md   exists
  document-harness/ORCHESTRATION.md:7  -> document-harness/CONSTRUCTION-CHECKLIST.md   exists
  document-harness/ORCHESTRATION.md:39 -> document-harness/CONSTRUCTION-CHECKLIST.md   exists
  document-harness/REVIEW.md:93        -> document-harness/history/REVIEW-v1-package-flow.md   MISSING
wikilinks, all nine members
  contract/Document-Work-Assurance-Contract-v4.md:36 -> document-harness/plans/document-work-assurance-harness-v3.plan.md
```

Five of the six markdown links are the checklist pointers rider `checklist-cited-not-carried`
banks — that row's sixth is `ONBOARDING.md:109`, which is not a member, which is why this scope
returns five and the rider's returns six. The seventh line is `L-1`.

## 4. Findings

### `L-1` (low) — contract v4 `:36`'s wikilink is the one followable cross-tier link round 2's own criterion reaches, its enumeration missed, and no guard can see

**Location.** `contract/Document-Work-Assurance-Contract-v4.md:35-42`:

```
Authored under the user-approved plan
[[document-work-assurance-harness-v3.plan|Document Work Assurance Harness v3]] (plan SHA-256 …)
… Plan §2 decisions V3-D1–D10 are the locked design authority; a genuine conflict between this
contract and the plan is a `SPEC_GAP`, not a reinterpretation opportunity.
```

**Ground truth.** `07ef526`'s body states the criterion the round demoted five citations under:
*"Every demotion takes items J and M's form: the markdown link or path token goes, the file name
and a sentence naming its holder stay, so a reader cannot follow a link into bytes a caller does
not have."* The criterion's own test is **followability**, and a wikilink is followable. This
repository's own precedent agrees that a wikilink is a link class, not prose:
`HARNESS-DECISIONS-archive.md:274,278` counts *"13 markdown 链接 + 1 wikilink"* as one population
and records that the caller-side `repo-audit` scans wikilinks *「与 markdown-link 并列的另一道」*.
Measured over the nine members at the subject blob, exactly one wikilink exists, it sits in a
product-tier member, and its target `document-harness/plans/document-work-assurance-harness-v3.plan.md`
is construction-tier by `CONSTRUCTION-INDEX.md:46`.

**Why nothing caught it.** `layer_path_check` is structurally blind to the form on two counts,
both established by reading the guard: `TOKEN = re.compile(r"`([^`\s]+)`")` requires backticks and
a wikilink has none, and `PATHLIKE` admits only `md|py|json|yaml|yml|txt|js` or a trailing slash,
so `…-v3.plan` fails the shape even if it were backticked. `sweep_refs.py` imports the same two
patterns and likewise returns nothing for it. The five demotions were derived from `HD-61`'s
enumeration of five citation sites, and an enumeration cannot reach a form its guard cannot show
it.

**The downstream decision that goes wrong (`R9` — this is not wording-level).** The sentence the
wikilink sits in makes plan §2 `V3-D1–D10` the **locked design authority** and a contract-versus-plan
conflict a `SPEC_GAP`. A reader carrying the product tier alone is sent to adjudicate a `SPEC_GAP`
against bytes it does not have, and — unlike the five demoted sites and unlike the checklist
pointers — the wikilink form gives it no holder sentence to tell it so. The immediately preceding
parenthesis already discloses that the plan's SHA-256 *"verifies against no blob here"* (`HD-57`),
so the reference is known-unverifiable in one respect and silently unreachable in another.

**Class sweep, per `HD-41` ④ / `E7`.** The class is *followable link from a product-tier member
into construction-tier material*; the scan and its counts are §3.3, run at this tip. Seven
instances: five banked (`checklist-cited-not-carried`), one ruled and scheduled to round 3 item G
(`REVIEW.md:93`), one — this — neither. Scope of the scan: the nine members at blob `b737742`,
markdown links and wikilinks both, targets resolved relative to each member's own directory.

**No bytes supplied, and not by preference.** `contract/Document-Work-Assurance-Contract-v4.md` is
a path `E2` freezes, so `R10`'s standing override applies — *"bytes on a path `E2` also freezes
bank until that rule's recorded ruling exists (`HD-20`), however appliable they are"* — and `E10`
says the same of both its channels. `HD-60` and `HD-61`, the two authorisations that could have
carried it, were consumed by `07ef526` and retired at `a554c0b`. So this banks whatever bytes a
record supplied, and supplying them would only invite the write the rule forbids.

**Suggested routing, which is the orchestrator's and the user's to settle (`R5`).** A bank row
whose redeem-when is *the next round holding a contract v4 `E2` write ruling* and whose deadline
is *the next contract v4 `E2` write window, or the next re-signature, whichever arrives first* —
the same arm rider `sig-write-once` already carries on the same file, and the two are candidates
to redeem together.

**A second, separable half — the guard's blind-spot clause.** `CONSTRUCTION-CHECKLIST.md:174-179`
enumerates what `layer_path_check` cannot see and does not name the wikilink form. Rider
`e10-cannot-see` already banks two falsifications of that same sentence and its redeem-when is the
same surface. This is a third item for that row, not a fourth row; whether to annotate is the
orchestrator's call, exactly as the previous read's `O-1` left it.

### `L-2` (low) — `R9`'s terminal route names no carrier, and the one finding sent down it since the last read was lost

**What was measured.** `v3-cold-read-d3ba221.md` `O-3` reported `README.md:22`'s *"added as the
tenth member 2026-08-18"* as an ordinal that has outlived its arithmetic, and routed it explicitly
under `R9`: *"this rides the next batch touching this member and spawns no round and no read."*

Round 2 then touched that exact member — `07ef526` edits `document-harness/README.md:16` — and the
phrase is byte-unchanged at the subject. It is carried nowhere else either:

```
$ git grep -n "tenth member" -- <all tracked .md outside migration/…/v3-*>
document-harness/README.md:22        (the phrase itself, and nothing else)

$ grep -n "tenth|第十成员" HARNESS-RIDERS.md CONSTRUCTION-LEDGER.md document-harness/plans/core-set.plan.md
CONSTRUCTION-LEDGER.md:91            (history: ORCHESTRATOR-CHARTER established it as the tenth)

$ grep -l "tenth member" v3-review-full-a554c0b.md v3-review-verify-5e5bebf.md
(neither)
```

**The finding is the route, not the phrase.** The phrase is accurate as history and `E10`'s
sentence is the sole authority on membership, which is why the previous read tiered it an
observation and why this read does not re-tier it. What this read adds is the measurement of what
happened to it: `R9`'s terminal branch — *"it rides the next batch touching this layer and spawns
no round and no read"* — is the only routing branch in the layer that names **no carrier**.
`E10`'s two channels apply bytes immediately; `R10`'s bank writes a row with a redeem-when and a
deadline; `R9`'s terminal branch writes nothing anywhere, so the finding survives only inside the
read record that raised it, and the next batch has no reason to open that record. One cycle, one
instance, zero carriers.

**The downstream decision that goes wrong.** At closeout the orchestrator weighs each low's
deadline against its touch trigger and routes it (`R10`). For a finding `R9` sends to *the next
batch*, there is nothing to weigh and nothing to redeem, so "routed" and "dropped" are the same
state and neither the orchestrator nor the next round can tell them apart. That is not
hypothetical here: round 2 was that next batch, it met the touch condition, and it had no way to
know.

**No bytes supplied.** Giving `R9`'s terminal branch a carrier adds a clause to a rule, so `E10`'s
design test opens a round for it and the free channel is closed by that test's own precedence
sentence. Whether the branch should have one is the user's (`R5`); a reader naming it here has
done its part.

**Not folded into an existing row.** The bank has no row about `R9`'s routing. The nearest
neighbours are `wl-route` — which records that `E10`'s enumeration, `R9`'s heading and `R10`'s
routing sentence disagree two-to-one about where a *byte-supplied* wording-level finding goes —
and this is the adjacent, distinct question of where a *byte-less* one goes. Same surface, so they
are candidates to redeem together; `wl-route`'s redeem-when already names the three sentences one
of which is `R9`'s heading.

### `O-1` (observation) — the signature move fixed the pointer's form, not its tier reachability, while its own rationale reads as if it fixed both

`CONTRACT-V4-SIGNATURE.md` states the reason for the move: *"contract v4 travels to every
repository that mounts this instrument, and the decision log does not, so a signed product-tier
document pointed at a register a caller never receives."* The same file, four paragraphs later,
places itself on **the construction side** — *"A caller does not carry this file"* — and
`CONSTRUCTION-INDEX.md:42` lists it under *Construction-side tier — what stays here*.

So under product-tier-only carry the state before and after is the same shape: a signed
product-tier document naming a record the reader does not have. What genuinely improved, and it is
not nothing: the three references went from a mount-reaching markdown link and path token to a
bare name plus a holder sentence, which is exactly `E10`'s stated purpose — *"a reader following a
path in this layer cannot land on another repository's bytes or on nothing"* — and that purpose is
met. What did not change is whether a caller can reach the signature of the contract it runs
against.

Recorded because the rationale is the thing a later round will read when it asks whether this
question is settled. It is the same measured class as rider `checklist-cited-not-carried`, and it
is **not re-filed**: that row's scope is the checklist specifically, re-measured at `07ef526` as
*"6 处指针 + 35 处规则引用 / 26 行原样"*, and these sites are not in it. Whether to widen the row,
to ship a signature stub with the product tier, or to accept the state and say so once is design
and is the user's (`R5`); this reader names the gap and stops.

### `O-2` (observation) — `README.md:24`'s "nine rows" was falsified by this same round, under the reading the previous read verified it by

**Location.** `document-harness/README.md:24` — *"`CONSTRUCTION-INDEX.md` at this instrument's own
repository root — nine rows, moved out of this table 2026-08-26 (round `CORE-SET-LAYER`)"*.

**Measured.** At `d3ba221` the file was one table of nine data rows. At the subject, after item N
merged `CORE-SET.md` into it (`cb4f22f`, this round, ruling 22), it is **two** tables — a
product-run tier of 8 rows and a construction-side tier of 13 — 21 data rows in all:

```
$ git show d3ba221:CONSTRUCTION-INDEX.md | grep -c '^|'   -> 11   (header + separator + 9)
$ git show b737742:CONSTRUCTION-INDEX.md | grep -c '^|'   -> 25   (2 × (header + separator) + 8 + 13)
```

**Two readings, and the previous read took the one that has since gone false.** *"nine rows, moved
out of this table"* can describe the nine rows that were moved out of `README.md` — history, still
true — or the file's own size, which is how `v3-cold-read-d3ba221.md` §3.3 verified it: *"README:
`CONSTRUCTION-INDEX.md` has **nine rows** | row count excluding header | 9 ✓"*. One competent
reader took the count reading when both were true. Only the historical one survives.

**No downstream decision goes wrong (`R9`), so it rides the next batch.** No check outcome, no
obligation, no verdict path turns on it, and the true reading is recoverable from the same clause.
Reported all the same because `README.md` is the member whose silent decay bought its own pinning
test, and because a second, softer half travels with it: the row's *What* column still describes
`CONSTRUCTION-INDEX.md` as construction-side registers and history only, while the file is now also
the single inventory of **what a caller mounts** — the one question a product-facing navigation
surface most obviously owes a pointer to.

**The content of a fix is named, not the bytes** (`E10`'s free channel admits either):
drop the bare ordinal in favour of what the clause is actually asserting — that the nine rows
listed alongside it moved out of this table on that date — and let the *What* column say the file
now carries both tiers. `README.md` is not a path `E2` freezes, so unlike `L-1` this one is
appliable; whether it is applied now or rides a batch is the orchestrator's, and rider `wl-route`
records that the layer's own three sentences disagree about which. This reader does not break that
tie.

## 5. Coverage — what was read in full, sampled, and only probed (`R4`)

**Read in full, end to end** — all nine members, 1,648 lines:

| blob | lines | path |
|---|---|---|
| `fce40914cb9c9cfd16a59dd2b6f8f9167656e274` | 257 | `document-harness/CONSTRUCTION-CHECKLIST.md` (both sides, as standing instruction) |
| `0a4da19b0d522d307997f681d5dec333b9349486` | 30 | `document-harness/README.md` |
| `234fdddf974e580d22a1a26b54587d11c24863b3` | 524 | `document-harness/EXECUTION.md` |
| `395995d45991670dc67e2eb616624c44b30ec123` | 320 | `document-harness/REVIEW.md` |
| `a9e9f75e484f40f4a1014e5d68ed6c73aa5fbdc2` | 119 | `document-harness/ORCHESTRATION.md` |
| `6d5714923870b4e13e8928221a80df68e563a5ed` | 5 | `migration/…/v3-harness-operating-contract.md` |
| `29bdc9fbde6e8db38d601dd2340d4b46a24a296f` | 5 | `migration/…/v3-harness-review-contract.md` |
| `5dfb7b64265c821c715f23de52824beeadea3405` | 344 | `contract/Document-Work-Assurance-Contract-v4.md` |
| `09aa869962f592c2f86c9379be0ef3eb7d2232ff` | 44 | `schema/document-assurance-v3/paragraph-map.schema.json` |

Also read end to end: `HARNESS-DECISIONS.md` lines 1–162 (header plus `§live`, eight entries);
`HARNESS-RIDERS.md` in full, all 22 rows; `CONSTRUCTION-INDEX.md` in full (63 lines);
`CONTRACT-V4-SIGNATURE.md` in full (60 lines); `v3-cold-read-d3ba221.md` in full; the commit
bodies of `b737742` and `07ef526` in full; the aggregate member diff `d3ba221..b737742` in full.

**Sampled:** `CONSTRUCTION-LEDGER.md` — `:170-200` (the two round entries of batch `CORE-SET`) read
closely, `:91` located; not read end to end. `tooling/hooks/layer_path_check.py` — `:30-55`
(`LAYER`, `TOKEN`, `PATHLIKE`, `RUNTIME_PREFIX`) read closely, the rest not.
`tooling/rsclib/document_harness/dispatch.py` — `:655-700` (`READ_PROMPT`, `ReadDispatch`) read
closely, plus the five dispatch-family signatures.
`document-harness/ONBOARDING.md` — its nine item headings and the section headings, not the body.
`HARNESS-DECISIONS-archive.md` — the `HD-56` / `HD-60` / `HD-61` entries' heading and status lines,
and `:274-278`; not read end to end.

**Probed only, for named claims, never read end to end:**
`tooling/tests/document_harness/test_precommit_checks.py` (`:220-240`),
`tooling/tests/document_harness_review/test_dispatch.py` (the constant lines),
`tooling/tests/document_harness/test_readme_enumeration.py` (`:3`, `:57`),
`tooling/rsclib/document_harness/init_target.py` (`TEMPLATES`, `_copy_templates`),
`tooling/rsclib/document_harness/__init__.py` (`:41`),
`tooling/sweep_refs.py` (invocation only),
`schema/document-assurance-v3/common.schema.json` and `user-decision.schema.json` (the enum
`$defs` only).
`§implemented` was probed by id only.

**Not read at all:** `document-harness/plans/core-set.plan.md`; the round's own review records
`v3-review-full-a554c0b.md` and `v3-review-verify-5e5bebf.md` (grepped for two named strings, not
read) — none of them is a member and no finding above rests on any of them.

**Marked, not verified (`R4`).** That this session ran with fresh context and as its own session is
a process claim this reader cannot verify from inside. Rider `e1-reader` already records that
`E1`'s form clause names *reviewer or executor* and omits the reader, which is the role this
dispatch filled; not re-filed.

**Not done, and why.** **No guard was mutation-tested in `E4`'s sense** — neuter → red → restore
from sha256-checked scratchpad copies. The subject commit changes no code and adds no guard, so
there is no new binding force to prove; what §3.3 and `L-1` report about `layer_path_check` is
established by **reading** `TOKEN` and `PATHLIKE` and by running `sweep_refs.py`, which imports
them, not by proving any committed test binds them. The three membership mirrors were compared,
not mutated. The full battery was not run: `E9`'s window is open and this read lands one record.
