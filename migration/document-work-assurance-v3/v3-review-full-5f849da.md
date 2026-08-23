# FULL — `b8df15a..5f849da`

**Verdict: `CHANGES_REQUIRED`.** One blocker. The merge itself is sound — every byte of
contract v4 that differs from its three signed sources is one of the plan's enumerated
deltas, and the two absorptions the plan called *verbatim* are verbatim — but the text
around it, in three `E10` members and one register, already says the user signed it. He has
not.

**Findings: 1 blocker, 5 low, 6 observations.** The blocker is one class at four sites, and
its fix is four short edits with the bytes supplied below. The lows are two counts the
round's own change falsified, two clauses of amended rule text that say more than one thing,
and one scan-evidence discipline. The observations include one measurement worth keeping:
the `CONTRACT_PATH` re-point this round performed is bound by nothing — pointed back at the
retired v3 path, the whole battery stays green.

Independence: this session received the range and nothing else. Round, budget,
authorization, obligations and every number below were derived from the repository; no
reported figure was accepted. `R1`'s four holdings are the orchestrator's. That this session
was in fact cold is a process claim about itself and is not verifiable from the repository
(`R4`); what is structural is that nothing in the dispatch set the question.

---

## 1. What the subject is, derived

`git rev-list --count b8df15a..5f849da` → **4**.

| | |
|---|---|
| base | `b8df15a14229944270ae6ff720b14f57170f9b1a` — `V3-PUB-FACADE-CLOSEOUT-v1` |
| tip | `5f849dadaac4a76482eafd0409994759dafb5eb1` — `V3-CONTRACT-V4-JOURNAL-v1` |
| round | `CONTRACT-V4` (publicization batch B — the ledger names batch B "重签打包批" and the queue head) |
| commits, kinds as their bodies name them (`E8`) | `f0b891d` record (opening `E10` read) · `0616fcf` plan (ruling carrier) · `23ca45b` candidate · `5f849da` record (round journal) |
| branch tip at review time | `5f849da` — the dispatched tip, so the `E9` window has held |
| worktree | clean; `git status --porcelain` empty |
| freeze marker | `.harness/review-pending.json` carries this exact range, `dispatched_at` `2026-08-23T06:32:55+00:00` |
| push state | `main...origin/main [ahead 4]` — nothing pushed (`E8`) |

**Budget position, derived.** No `v3-review-full-*` or `v3-review-verify-*` record for this
round exists under `migration/document-work-assurance-v3/` at the subject. The only review
record inside the range is `v3-cold-read-b8df15a.md` (`f0b891d`), an `E10` read, which by
`R3` is not a round and spends nothing. **This is the round's FULL and consumes the FULL
leg.** One user-approved fix and one targeted VERIFY remain. The plan's ruling 1 sets the
process weight at opening read + FULL + VERIFY, which matches.

**Authorization, derived.** Four user rulings of 2026-08-23, carried by the plan commit
`0616fcf` (the plan declares itself their carrier until the round records them). Ruling 3 is
the one that matters here: *this round may touch the `E2` freeze surface — retiring the
supersession files into git history and re-pointing the freeze list — with v4's
effectiveness still gated on the signature.* `HARNESS-DECISIONS.md` carries no entry for
this round; per `R7` that is a ceiling stated, not a block: the rulings' origin is a
conversation I cannot see, but they are **recorded** in the repository, in the carrier the
plan names, so `R2`'s chat-only test is not tripped.

**Obligations, derived.** The plan's delta enumeration D1–D10 ("authoritative; the FULL
verifies the candidate against it"), its change-surface table, and the permanent boundaries
`E1`–`E12` / `HD-20` / `HD-41` / `HD-44`. `HARNESS-DECISIONS.md` `§live` read this session
(`HD-44`, `HD-41`, `HD-36`, `HD-35`, `HD-34`, `HD-23`, `HD-9`); the file was then read end to
end.

---

## 2. Lead with the implementation

### 2.1 The merge — D1–D10 against the frozen sources

`git cat-file blob` for all four objects, then `diff -u` v3 → v4: **six hunks**, and each maps
onto an enumerated delta with nothing left over.

| hunk | v3 lines | delta |
|---|---|---|
| 1 | 1–24 | D1 frontmatter (`status:` / `document_role:` dropped, `signature_owner:` re-pointed) + D2 warning block and lineage paragraph |
| 2 | 59 | D3 §3 `DocumentWorkSpec` owner cell |
| 3 | 88 | D4 §4 diagram line |
| 4 | 150–160 | D5 invariant 9 + D6 invariant 11 |
| 5 | 170 | D7 §8 step 7 |
| 6 | 247– | D8 new §13.1/§13.2 + D10 §14 (D9's path fixes live inside) |

**"Verbatim" was checked as verbatim, not read as verbatim.** Normalising whitespace and
stripping the `>` quote prefix, s1's four successor texts were searched for in v4:
S2 (595 chars), S3 (178) and S4 (200) are **present byte-for-byte**; S1 matches once its
backtick wrapper is removed, since v4 carries it inside the fenced diagram
(`contract/…-v4.md:103`).

For the absorbed material a character-level diff was run rather than a similarity judgement:

- s1 §3 bullet 1 → **ratio 1.0000**, byte-identical.
- s1 §3 bullet 2 → the only difference is `signed contract §13` → `§13 above`, exactly D8's
  declared self-reference adaptation.
- s1 §3 bullet 3 → replaced by s2's successor text, exactly D8's declared replacement.
- s2's successor text → the only difference is `under \`assurance/runs/\`` →
  `(held in the caller's run directories)`, exactly D9's caller-held-path fix. The second D9
  fix, `templates/run-v2/` → `assurance/templates/run-v2/`, is present and resolves.

So the plan's own acceptance — "diffing the copy against blob `b2dbdf75…` and confirming no
unenumerated drift" — **holds**. §§1–13 outside the six hunks are byte-identical.

**The signature claims inside the lineage paragraph were checked against the records, not
accepted.** `W2-record.md:323-336` records the 2026-07-24 sign-off binding blob
`68031fa2…`, and explicitly rules the carrier's own "UNSIGNED" header authoring residue.
`supersession-2-signature.md:4-6` records the 2026-07-30 signature binding `e1a2f26b…`.
`N0-record.md` §8 records the 2026-07-20 v3 signature with its blob binding appended. The
candidate's correction of its own first draft — *signed*, not merely *adjudicated* — is
right, and the journal's self-catch 1 is an accurate account of it.

`E2`'s new literal `a775e28f…` equals the tip blob (`git ls-tree -r 5f849da -- contract/`).
`pack_digests()` returns `contract_digest` `76b16638…`, which is the sha256 of that same
blob — so the worktree copy is LF-identical to the object, and the `HD-40` CRLF trap is not
open here.

### 2.2 Do the guards still bind

Four mutations, each restored from a sha256-checked scratchpad copy, never `git checkout --`
(`E4`); restore digests re-verified after each.

| # | mutation | expected | result |
|---|---|---|---|
| A | drop `document-harness/REVIEW.md` from `LAYER` | red | **red** — 2 failed (`test_layer_equals_the_hand_written_membership`, `test_every_member_is_scanned`) |
| B | neuter `unresolved_tokens` to always return `[]` | red | **red** — 7 failed; the negative controls stayed green |
| C | re-inject `status: candidate-awaiting-user-signature` into v4's frontmatter | red | **red** — the rewritten `test_r4_the_real_contract_passes_on_its_own_merit` fails on the real document |
| D | point `CONTRACT_PATH` back at the retired v3 path | red | **SURVIVED — 792 passed** |

A and B prove the `E10-sync` machine leg still binds after the shrink; the `EXPECTED` tuple
is hand-written and never imported from the module it guards (`E5`), and each of the eight
members is separately proven reachable. C proves the round's one rewritten test is bound to
the real document rather than trivially true. D is finding `O-1`.

The coverage the round traded away was checked rather than taken on trust: the two deleted
`GovernanceRealDocumentTests` cases covered *flagged* and *exempted* behaviour on a real
document; both classes remain covered in memory —
`GovernanceFieldMatchTests.test_r4b_self_approval_fields_are_flagged` and the eight-case
`GovernanceExemptionTests`, including blob evaporation and `V3-GOVERNANCE-EXEMPTION-NARROWER`.
**No defect class lost coverage in the 793 → 792 step.**

### 2.3 Re-derived measurements (`E3`, `R2` — no reported figure accepted)

| claim | where claimed | re-derived |
|---|---|---|
| battery green at the tree | candidate body, journal | **792 passed in 121.26s**, Windows, `python -m pytest -q` from `tooling/` |
| POSIX validation | journal | **792 passed, 863 subtests in 12.70s**, WSL Ubuntu (Python 3.12.3), fresh clone checked out at `23ca45b` — reproduced, not accepted |
| eight-member layer resolves in a clone | journal | `members: 8`, `unresolved: []` in that clone; `contract/` holds exactly one file there |
| membership sentence == guard `LAYER` | candidate body | hand-compared: same eight paths, same order, and `EXPECTED` matches both |
| no unresolved path token added to a member | — | `layer_path_check`'s own `unresolved_tokens` replayed over the round's added lines in all four touched members: **0** |
| markdown links | — | 56 relative links across the 13 files this round centres on: **0 broken** |
| schema pack still fifteen | `E2` clause | `ls schema/document-assurance-v3/` → **15**; `git diff --name-only b8df15a 5f849da -- schema/` → **empty** |
| all three source blobs stay reachable | candidate body | `git cat-file -e` → yes for `b2dbdf75` / `68031fa2` / `e1a2f26b`, and for `a775e28f` |

A measurement-channel note, since this repository has been burned by it before
(`pub-facade-2026-08-23.md`): `$(…)` inside a single-quoted argument to `wsl.exe` was
expanded by the **outer** Windows shell, so a first attempt reported the Windows `HEAD`
while the Linux clone was correctly at `23ca45b`. Detected by re-running `git rev-parse`
without command substitution. The WSL figures above are from the corrected channel.

### 2.4 The class scans, re-run rather than read (`HD-41` ④)

- The candidate's own sweep pattern, over the seven files its body names, returns **one**
  line today — `README.md:80`, the historical "ten" the round deliberately kept with a
  count-note. Body and journal both name that site, so the sweep is coherent; the wording is
  `L-5`.
- Widening the class: `tenth member` cannot match that pattern. Two sites survive
  (`document-harness/README.md:24`, `tooling/hooks/candidate_path_check.py:16`); both are
  past-tense and true, so nothing is wrong today. Recorded so the pattern's blind spot is
  known, not as a defect.
- Residual references to the three retired filenames, live files only: v4's own lineage,
  seven historical plans, `split-travel-manifest.md`, and the two signature records — all
  intentional history, exactly as the body claims.
- `contract/` at the tip holds **one** file. That measurement is what falsifies `L-1`.

### 2.5 Process and record conformance (boundary check, run second)

`E8`: four commits, each a single dense title of the round's own form, each body one
paragraph, each naming its kind, no trailers, explicit paths, nothing pushed. `E9`: the
budget test is applied correctly — the journal commit states "no FULL has occurred", which
is the objective test, not a self-classification of consumption. `E12`: the recorded range
in `.harness/review-pending.json` carries a written tip, but that file is gitignored, so
recording it is not a commit inside the round and the clause's rationale does not reach it;
no committed file records a range. `E1`: the exception channel is taken and disclosed — all
four `R1` holdings named as the executor's, "nothing about this candidate's authoring is
independent", and no claim of structural independence. `E10`: the two amended members are
written inside an open round with their independent reads deferred to the next opening read,
as the plan states and as precedent (`HD-45`'s closing note) establishes. `R10`: the four
deleted rider rows are redeemed by fixes in the same commit, and the ledger settles the
question their redeem-when raised — it names batch B by name as "那个「打包批」" those rows
waited for. `read-name-split` is well formed (design-shaped, round-eligible surface, no
deadline). The plan edit inside the candidate commit is the four→five honesty-note
correction and nothing else; the rulings are untouched — checked by diffing
`0616fcf..23ca45b` on the plan.

---

## 3. Findings

### `B-1` (blocker) — the tree states a signature the user has not given

**Location.**

| site | text |
|---|---|
| `document-harness/CONSTRUCTION-CHECKLIST.md:111` | "merged into **the signed contract v4** and left the tree with it" |
| `document-harness/README.md:17` | row label "**Contract v4 (operative)**" |
| `README.md:82-83` | "the count is eight since round `CONTRACT-V4` merged the two supersessions into **the signed contract**" |
| `migration/document-work-assurance-v3/N1/governance-exemptions.json:44` | "the removing decision **is** the CONTRACT-V4 signature entry in HARNESS-DECISIONS.md" |

**Ground truth it violates.** `HARNESS-DECISIONS.md` carries no v4 entry —
`grep -n -E "v4|CONTRACT-V4|a775e28"` over the register and its archive returns one line
(`:518`), about an unrelated 2026-08-08 deadline. The round's own plan says it: "until it
lands v4 is candidate text, not a contract" (`:16`), and sequences the signing checkpoint as
step 5, **after** this FULL (`:88-91`). v4's own header agrees: "This contract becomes
binding only when the user signs it." The fourth site is worse than an adjective — it
retires a register entry on the authority of a decision that does not exist, in a register
whose own note reserves that authority to the user.

**Why this binds an action rather than reading as a wording slip.** v4 §13, carried unchanged
from v3, is *signed contracts are never amended in place; corrections create a versioned
successor*. Text calling v4 signed says an in-place correction is barred and a v5 is owed;
the truth says an in-place correction is free. That permission is live in this very round —
the journal already anticipates "if a fix leg touches v4, the literal moves with it". A cold
executor reads the layer, not the plan, and `§live` (the one non-member file `E10` sends him
to) says nothing either way. It is also, precisely, the defect class D1 removed from the
frontmatter one file over: a governance document's surroundings asserting an approval state
it does not hold.

**Minimum fix** (bytes, so the leg is cheap):

- checklist `:111` → `merged into contract v4 and left the tree with it`
- `document-harness/README.md:17` label → `Contract v4 (candidate — awaiting signature)`
- `README.md:82-83` → `merged the two supersessions into contract v4`
- `governance-exemptions.json:44` → end the `why` with: `…the removing decision is round
  CONTRACT-V4's signature entry in HARNESS-DECISIONS.md, owed at the signing checkpoint and
  not yet written.` (The alternative — leave the entry in `exemptions` until that entry
  exists — is also correct and is the user's call, not mine.)

Nothing here adds a clause or changes what any rule requires.

### `L-1` (low) — `contract/` holds one file; the row two lines below says three

`document-harness/README.md:18`: "What else lives in `contract/` | Nothing: since the
2026-08-17 split that directory holds exactly **the three files the rows above name**." The
round replaced those three rows with one and left this row standing. `ls contract/` returns
one file, on Windows and in the POSIX clone alike. This is a false factual claim in an `E10`
member, introduced by this round, in a file the round edited — the class `E3` governs. It
escaped because the sweep's pattern was the member count, not the directory count.

Bytes: `Nothing: since the 2026-08-17 split that directory holds exactly the one file the row
above names.`

### `L-2` (low) — the exemption register's note and its own new entry both misstate it

`migration/document-work-assurance-v3/N1/governance-exemptions.json`:

- `:6` — the note still opens "**Two** documents in this repository permanently carry a
  self-referential approval field", while `exemptions` now holds **one** entry, whose
  `path_hint` (`.goals/plans/…`) is the caller's tree, not this repository. The note was
  already half-stale from the split; this round made it wholly so and touched this exact
  file.
- `:44` — the retired entry justifies itself with "the register's own note says entries are
  added **and removed** only by user decision". The note (`:26`) says only "**Adding** an
  entry here requires a user decision." The quoted rule is broader than the rule.

Nothing machine-readable consumes this file (`grep -rn governance-exemptions` finds three
prose references and no loader; the tests build exemptions in memory), so no check outcome
moves.

### `L-3` (low) — `E10`'s new parenthetical is attached to the wrong item

`document-harness/CONSTRUCTION-CHECKLIST.md:107-111`: the list now ends
"…and `schema/document-assurance-v3/paragraph-map.schema.json` (the two contract
supersessions, members until round `CONTRACT-V4` …)". Syntactically the parenthetical
describes the schema file it follows; its subject is the two paths that just left. In a
membership sentence whose whole job is to be read literally, a reader can land on "the
paragraph-map schema is the two contract supersessions".

Bytes: close the list after `paragraph-map.schema.json`, then a new sentence —
`The two contract supersessions were members until round \`CONTRACT-V4\`, as prose successors
to signed text; they merged into contract v4 and left the tree with it.`

### `L-4` (low) — `E2` says one blob and also says four sets of bytes stay frozen

`document-harness/CONSTRUCTION-CHECKLIST.md:49-58`: "the list is exactly this: contract v4
`a775e28f…` (… the v3 contract `b2dbdf75…` and the two supersessions … **stay frozen as
history at those blobs**), and every file the … pack held … **One blob and one directory**".
A reader asking whether `b2dbdf75…` still owes `E2`'s recorded ruling gets both answers from
one clause. `HD-44` settles the substance — `E2` freezes bytes, and bytes in history cannot
be written — but this clause, which is where a cold executor looks, does not say so, and the
count sentence and the parenthetical disagree on their face.

Bytes (a candidate, not a demand): `… — left the tree with round \`CONTRACT-V4\`; their bytes
are immutable in history at those blobs and are not what this list governs)`. If the
orchestrator judges that this changes what `E2` governs rather than saying what it already
governs, then the fix is design and the finding banks instead (`R10`).

### `L-5` (low) — the sweep is summarised, not pasted, and its absolute quantifier carries no scope

`HD-41` ④ requires the class-scan grep **output** in the commit body; rider `fixleg-scan-raw`
exists because two consecutive legs passed with summaries and the round that opened it wrote
"don't let that become the habit". This candidate redeems four banked findings and reports
its sweep as prose: "raw sweep '…' over the seven live files returned exactly those sites and
zero remain". No output is pasted. Separately, "zero remain" is an absolute quantifier
without its scope (`HD-41` ②): re-running that exact pattern over those exact seven files
returns one line. The body does name that survivor elsewhere, so the claim is recoverable —
but only by reading two sentences against each other.

---

## 4. Observations

### `O-1` — the `CONTRACT_PATH` re-point is bound by nothing (measured)

Mutation D: `tooling/rsclib/document_harness/__init__.py:41` pointed back at
`contract/Document-Work-Assurance-Contract-v3.md`, a path that no longer exists — **792
passed**. The whole battery is blind to it. The reason it costs nothing today is worth
recording with it: the constant's only consumer is `pack_digests()` at `:249-250`, behind
`if CONTRACT_PATH.exists()`, so a stale path silently drops `contract_digest`; and
`pack_digests()` has no callers (re-derived: definition `:238` and the `__all__` export
`:266`, nothing else). So a fail-open exists, in a function no decision depends on. This is a
measurement, **not a request for machinery** — `E6` points the other way and `HD-27` has
refused an `E2` guard three times. It does sharpen the second half of rider `PD`, which
already records the zero-caller fact.

### `O-2` — whether contract v4 is an `E10` member was answered by omission (`R5` → user)

`s1` and `s2` were members because they were **prose successors to signed text**; `s2` §5 says
so in its own words, and says such a text "owes an independent read before any round relies
on it … never banked as a round's FULL". v4's §13.1/§13.2 are new prose merging three signed
texts, and v4 is unsigned. The round removed the two members and did not put v4 in; the
membership sentence's parenthetical records the *removal* but the round records no answer to
the question `HD-21` puts. There is a defensible answer — a contract governs product runs,
not this layer's rules, and once signed it is `E2`'s business, not `E10`'s — and there is a
consequence: after this round, nothing obliges an independent read of that merged prose
except the user's own signing leg, and a read that is the round's FULL is exactly what `E10`
says cannot serve. Whether that trade is right is the user's to conclude, not mine; adding a
member is design and would open a round.

### `O-3` — two signed design documents now sit modified, with the register still binding their old blobs

`document-harness/io-design.md` `8f3c82c2` → `a1594eb2` (`HD-35` binds `8f3c82c2`);
`document-harness/split-design.md` `3140faf1` → `a078ea31` (`HD-40` binds `3140faf1`). Both
`HD` entries say a substantive modification owes a re-signature, and the plan defers the
re-sign notes to the signing checkpoint. That is planned and disclosed. The exposure is the
branch the plan itself keeps open: "No signature → v4 stays candidate text and the round
stops there" — in which case both documents remain modified, unsigned, with stale bindings
and no re-sign record.

### `O-4` — the retire-v3-in-tree sub-decision is open, and already implemented

The plan reserves it for the user at the signing checkpoint (`:88-91`) while its
change-surface row implements the recommended branch. That is internally coherent — build the
recommendation, flag the alternative — but the reversal is no longer cheap: answering "keep
v3 in tree" now reopens `E2`'s clause, the `document-harness/README.md` row, the
`governance-exemptions.json` entry (whose `carried_value`/`fields`/`immutability_rule` were
dropped, not just moved) and the test's comment block. Worth knowing before the checkpoint.
On `E2` itself no violation is found: ruling 3 authorises the surface, and under `HD-44`
removing bytes that survive intact is not a write.

### `O-5` — D8's absorption is faithful but compressed, and the compression is invisible in a v3→v4 diff

D8 declared absorption, not verbatim, so this is in boundary. Named because the reader about
to sign v4 cannot see it: s2 §4's five notes lose "`instruction_ref` … nothing requires or
checks a digest on it" and "it was named here in error", and s1 §4's disclosure loses its
"(wave-2 design §9)" citation. Nothing false is introduced; three statements of fact are
dropped, and the only way to notice is to diff v4 against `e1a2f26b…` rather than against
`b2dbdf75…`.

### `O-6` — after this round the `E2` freeze surface is not wholly present in a clone

Three of the four blobs `E2` names now exist only in history. A shallow, single-branch or
filtered clone — the ordinary way a stranger takes a public repository, which is what this
batch is preparing for — carries `contract/`'s one file and not the frozen sources. Full
clones are unaffected; all four blobs are reachable here.

---

## 5. Routing, stated without adjudicating it

`R10` routes by the 2026-07-29 ruling; I state where each finding lands and do not decide it.

- `B-1` is a blocker in a FULL, so it is the round's one user-approved fix and obliges the
  targeted VERIFY. Bytes supplied above.
- `L-1`, `L-2`, `L-3` supply exact bytes and touch no path `E2` freezes, so on their face
  they take `E10`'s free channel — applied immediately, reported after the fact, riding the
  next read of this layer at per-member digest cost. If the orchestrator prefers, they ride
  the `B-1` fix leg instead; none of them adds a clause.
- `L-4` supplies bytes but may be read as changing what `E2` governs. If so it is design and
  banks; if not, free channel.
- `L-5` names a discipline, not text — its home is the fix leg's own commit body, where
  rider `fixleg-scan-raw` is redeemed by pasting raw output.
- `O-1`, `O-2` are `R5` questions for the user. `O-3`, `O-4`, `O-6` are inputs to the signing
  checkpoint. `O-5` is a note for the reader who signs.

---

## 6. Coverage — read in full, sampled, only probed (`R4`)

**In full:** the four commit bodies; the whole `b8df15a..5f849da` diff; contract v4 (as blob
and as diff against v3); the v3, s1 and s2 blobs; `document-harness/CONSTRUCTION-CHECKLIST.md`;
`document-harness/plans/contract-v4.plan.md`; `document-harness/journal/contract-v4-2026-08-23.md`;
`HARNESS-DECISIONS.md` (both sections, end to end); the `HARNESS-RIDERS.md` diff;
`migration/document-work-assurance-v3/N1/governance-exemptions.json`;
`migration/document-work-assurance-v3/supersession-2-signature.md`;
`tooling/hooks/layer_path_check.py`.

**Sampled:** `document-harness/README.md`, `EXECUTION.md`, `REVIEW.md`, `ONBOARDING.md`, root
`README.md`, `io-design.md`, `split-design.md` — read at the diff plus surrounding context,
not end to end. `W2-record.md`, `N0-record.md` §8, `N1-record.md`, `CONSTRUCTION-LEDGER.md` —
read at the sections the claims point to. Test files read at the classes this round touched.

**Only probed:** the rest of the 792-case battery (run, not read). `ORCHESTRATION.md` not read
this session — no change touched it. The caller repository is not present; every claim about
it is `UNVERIFIABLE` from here, including whether `ac1b383` is what
`document-harness/README.md` says it is (it does not resolve in this repository, which the
checklist's preamble makes the expected reading for a caller-repo id).

**Marked, not verified:** that the executor session merged the two work-side roles as
disclosed, and that this session was cold — both process claims about sessions, not
repository facts (`R4`). The four user rulings' origin in conversation is likewise outside my
surface (`R7`); they are recorded in the plan, which is what I checked.

**What mutation proved and did not.** A–C show those tests have binding force on the defect
shapes reproduced; they do not show that force is sufficient, and D shows one constant with
no force at all. This FULL certifies nothing about whether contract v4 is good text — only
that its bytes are the enumerated merge of texts the records show were signed, and that the
prose around it currently says one thing that is not so.
