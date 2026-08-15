# Checkpoint read — `CONSTRUCTION-CHECKLIST.md` blob `9f2ec9a9`, the E10/E2 amendment re-read

**No verdict.** A read is not a round (R3): it spends no budget, carries no verdict, and its output
is findings tiered must-fix / low / observation. This is the independent re-read the convergence
clause of E10 owes on the amended bytes, and no round, FULL or VERIFY is banked as it.

**Findings: 1 must-fix, 3 low, 5 observations.** Labels are local to this record; cite them as
`read 9f2ec9a M-1` and so on — the prior read's `M-1`–`M-3` and `L-1` are different findings.

---

## 1. Subject, re-derived

The subject is a text, not a range. Its identity, established before reading it:

```
$ git cat-file -t 9f2ec9a9705448da116a1a3e26994363121b031a
blob
$ git rev-parse HEAD:ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md
9f2ec9a9705448da116a1a3e26994363121b031a
$ git rev-parse 87a4ced:ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md
9f2ec9a9705448da116a1a3e26994363121b031a
$ git hash-object ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md
9f2ec9a9705448da116a1a3e26994363121b031a
$ git status --porcelain ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md
(empty)
```

The bytes at `87a4ced`, at `HEAD` and in the worktree are one object, so reading the file reads the
subject. `f97b348` is likewise a blob — `git rev-parse f054a08:<path>` — so `git diff f97b348 9f2ec9a`
is the amendment and nothing else: **two hunks**, one in `E2` and one in `E10`.

- **A-1 (E2, subject lines 29-33)** — a definition of `signed`: *"a signature recorded against the
  file's exact blob, either in the file's own sign-off block or in a committed record naming that
  blob — four encodings are in use and one file carries none by design, so read the record rather
  than the file where they disagree: `N0/N0-record.md` holds it for
  `Document-Work-Assurance-Contract-v3.md`…"*. Answers the prior read's M-2.
- **A-2 (E10, subject lines 72-73)** — the deferral bound changes from *"an amendment of at most one
  sentence"* to *"an amendment that adds no new clause to any rule"*. Answers the prior read's M-1.
- **A-3 (E10, subject lines 77-79)** — `relied` changes from *"took its governance from it, which
  authoring, citing or recording it is not"* to *"an outcome would change if the text changed, which
  authoring, citing or recording it **alone** is not"*. Pays the prior read's L-1.

The prior read's **M-3** is answered outside the subject, in `HARNESS-LEDGER.md` at the same commit:
a seven-row inventory of what the narrowing moved out of `E2`, plus a ruling on the two files that
had never been put to the user.

---

## 2. The precondition, checked before anything else

C-3's route is available only *"for as long as no round has relied on the text."* The commit asserts
this; R2 forbids accepting it. Classifying every commit after `f054a08` by its own diff, not by its
message:

```
$ for c in 6798ebc 5760f8b 707722d e56af0d 25f2916 c50729e 87a4ced; do git show --stat --format='' $c; done
 .../v3-review-verify-f054a08.md                    | 327 +++++
 ResearchSystem/HARNESS-LEDGER.md                   |  46 +++--
 ResearchSystem/HARNESS-LEDGER.md                   |   9 +--
 ResearchSystem/HARNESS-LEDGER.md                   |   8 +-
 ResearchSystem/HARNESS-LEDGER.md                   |  10 +
 .../v3-dispatch-checklist-amendment-read.md        |  25 +
 .../v3-checkpoint-read-f97b348.md                  | 236 +++++
 ResearchSystem/HARNESS-LEDGER.md                   |  25 +
 .../document-harness/CONSTRUCTION-CHECKLIST.md     |  13 ++-
```

Seven commits, three files between them: two review records, the ledger, one dispatch, and the
amendment itself. **No code, no schema, no test, no fixture, no contract byte.** Nothing here is a
FULL, a fix or a VERIFY, so no round has relied on the text under either definition of `relied` —
the one in force when the amendment was written or the one it installs. The route was available.
The same is true as of this reading, so this record's must-fix is answerable the same way.

The one candidate for reliance the prior read named, `707722d`, is a ruling rather than a round, and
it is over-determined besides: it rests on hard rule 5 at `7011916` as well as on the amended `E2`,
and says so. Under A-3's new test — *would the outcome change if the text changed* — it is not
reliance. The two definitions agree on every fact in this window.

---

## 3. Must-fix

### M-1 — A-1's test, applied to the directory it scopes, unfreezes a signed contract, and contradicts the inventory landed in the same commit

**Location:** subject lines 29-30 (`E2`), against `HARNESS-LEDGER.md`'s seven-row table at the same
commit. **Ground truth it violates:** the bytes under `ResearchSystem/contract/`.

A-1 makes `signed` testable, which is what the prior read's M-2 asked for. Applied, it answers a
question M-2's own survey never asked: **what happens when a file bears a signature that binds bytes
other than the ones now at that path.** Two of the twelve files are in that state, and both are
files the prior read placed *inside* `E2`.

**Instance 1 — `Stage-Control-Contract.md`.** Its §13 sign-off names the signed object exactly:

```
- signed-date: 2026-07-19
- signed corrective candidate commit/digest: commit `49e421e0d6aa8876c1aa9700d38357d40305df9a`;
  tree `3b1145f68c3e9a16e05d8b3803a207ed73f22cc2`; contract SHA-256
  `5bd863787c1ae1ba4398a3ed9da0467d9da3fee60f65d9e90b7a52f5ccc47f5e`
```

That digest is correct for the bytes it names, and wrong for the bytes at `HEAD`:

```
$ SHA='python -c "import sys,hashlib;print(hashlib.sha256(sys.stdin.buffer.read()).hexdigest())"'
$ git show 49e421e:ResearchSystem/contract/Stage-Control-Contract.md | $SHA
5bd863787c1ae1ba4398a3ed9da0467d9da3fee60f65d9e90b7a52f5ccc47f5e
$ git show HEAD:ResearchSystem/contract/Stage-Control-Contract.md | $SHA
34a5406ed98887fee804c4821b04693c97d492e63724fb3eb157dfb3d975ac89
$ git diff --stat 49e421e e64618d -- ResearchSystem/contract/Stage-Control-Contract.md
 1 file changed, 24 insertions(+), 21 deletions(-)
```

The 24/21 delta is the signature-recording edit itself: `corrective status` flips `VERIFY_PENDING` →
`SIGNED`, `approval status` `PENDING` → `APPROVED`, and the empty sign-off block is filled in. So the
signed bytes are `5bd8637…` and they are not at that path; the bytes at that path are their
signature-recording successor, and **no signature is recorded against them.** Under A-1 the file is
not signed bytes and leaves `E2`. Read the other way — that `E2` freezes the *signed* object,
`5bd8637…` — the file at `HEAD` is still outside `E2`, because it is not that object. Both readings
reach the same place: today an executor may edit a signed contract in-boundary without `E2` stopping
them or `SPEC_GAP` being owed.

**Instance 2 — `ResearchSystem-Contract.md`,** the same shape with no digest at all:

```
$ git log --format='%h %ad %s' --date=short -- ResearchSystem/contract/ResearchSystem-Contract.md
5ca6cc1 2026-07-18 chore(research-system): establish signed A1 G0 boundary
1c8bb3d 2026-07-12 chore(research-system): P0 — execution contract + repository baseline
```

Its §4 sign-off block reads `signed-date: 2026-07-12` and names no blob and no digest; the bytes
changed six days later. The change is legitimate and designed — the A1 amendment's §6 write
allowlist names this file for its Active-Amendment index, and the file itself says *"The index
records status; it does not change the frozen D1–D6 decisions."* A-1 has no way to express that: it
requires a signature *against the file's exact blob*, and this signature is against no blob.

**Both readings of A-1 are live, and they differ on this.** The head phrase *"recorded against the
file's exact blob"* governs both branches, but *"naming that blob"* appears only on the record
branch — which is a real cue that explicit blob-binding is required only there, and that the in-file
branch means no more than *"the file has a sign-off block."* Under that looser reading both files
stay in `E2` and the head phrase does work in exactly one place, the `N0/N0-record.md` case it was
written for. Under the stricter reading, which the words support at least as well, both leave. The
sentence does not decide, and one of its answers unfreezes the harness's other signed contract.

**The contradiction is inside one commit.** `HARNESS-LEDGER.md` at `87a4ced` records that **seven**
files leave `E2` and rules each; neither of these two is among them, and the prior read said
explicitly *"`ResearchSystem-Contract.md` and `Stage-Control-Contract.md` stay inside `E2`."* That
classification was made against the pre-A-1 question *does the file bear a signature at all*, which
A-1 replaced. The inventory and the definition shipped together and answer differently.

**Not inherited from the executor.** A-1 is the prior read's stated minimum fix transcribed nearly
verbatim; the executor implemented what it was handed. The defect is in the wording, not in its
adoption — see O-e.

**Minimum fix:** say which bytes a signature binds when the edit that records it necessarily follows
it — for instance, that a signature binds the bytes as signed and that the edit recording the
signature, or an edit a signed instrument's own write allowlist authorizes, does not un-sign the
file. Then re-derive the inventory under the decided reading and put any file it newly moves to the
user, since whether these should be protected is theirs to answer (R5), not a reviewer's.

---

## 4. Low

### L-1 — A-2's bound is silent on replacement and subtractive edits, and this commit contains a replacement

The prior read's M-1 asked for *"a test that measures effect rather than punctuation — e.g. an
amendment that adds no new clause to any rule."* A-2 adopts the example. It does what was asked of
it: the two-clause amendment that defeated the old sentence-count test would not qualify under it,
and the commit's own self-test agrees that the E2 hunk adds a clause and so this amendment does not
qualify either. That is a real improvement and M-1 is answered on its own terms.

What the example does not measure is effect. **A-3 is the demonstration, in this same commit:** a
pure replacement of the definition of `relied`, adding no new clause to any rule, materially
changing the term on which the whole convergence route and `E2`'s own carve-out turn. Taken alone —
and nothing prevents an executor from committing it alone — it satisfies A-2 and would be
deferrable. Subtraction has the same property and no size cap at all, and E10 names subtraction as a
permitted edit kind in its first line.

**The downstream decision:** whether a single-hunk amendment that redefines a governance term may be
relied on before its read. **Not raised to must-fix:** the second condition (*nil effect on every
round in flight*) and the hard requirement that *the bytes ride the next read* still stand, so the
exposure is bounded and auditable rather than open — and the prior read's O-b already recorded that
both recorded facts are self-judged.

### L-2 — `N0/N0-record.md` does not resolve from where A-1 is written (wording-level, R9)

The path is `ResearchSystem/migration/document-work-assurance-v3/N0/N0-record.md`; A-1 sits in
`ResearchSystem/document-harness/`, which has no `N0/`. Every other cross-reference in this file is
written relative to itself (`../migration/document-work-assurance-v3/…`).

```
$ ls ResearchSystem/document-harness/N0/
(no such directory)
$ find . -name N0-record.md -not -path './.git/*'
./ResearchSystem/migration/document-work-assurance-v3/N0/N0-record.md
```

**Wording-level under R9** and banked: the accurate location is recoverable from a committed
record — the contract's own frontmatter carries `signature_owner: V3-N0 administrative record` and
its warning block spells the relative path out. The named decision that would go wrong without that
recovery is real but does not survive it: a reader who cannot find the record concludes the contract
is unsigned and treats a frozen file as editable.

### L-3 — the recorded authority for folding A-3 into this commit does not cover it

The commit body justifies A-3 as *"R9 sends a banked wording-level finding to the next batch touching
this layer and this is that batch."* Two steps of that do not hold. R9's *"rides the next batch"*
clause is conditioned on **no** downstream decision being nameable, and the prior read's L-1 named
one — `707722d`. And R9's own definition makes a finding wording-level only when *"its fix changes no
actor's action"*; A-3 changes what counts as reliance, which decides whether a later change opens a
round. The prior read tiered it **low**, not wording-level, and R9 does not reach it.

**Nothing turned on it here** — the commit was already authorized to touch this text for M-1 and M-2,
and A-3 pays a finding that needed paying. The exposure is precedent: on this citation any low
finding can be folded into a convergence amendment, and E9's *"never self-classify which round
consumed what"* is the rule that shape erodes. What is actually missing is a route for a read's
**low** findings; C-3 covers must-fix and R9 covers wording-level, and the file is silent between
them. Its own header says a silence is not a defect and closing it rides the next batch.

---

## 5. Observations

**O-a — the amendment redefines the term its own authorizing precondition turns on, in the commit
that uses that precondition.** C-3's gate is *"no round has relied"*; A-3 changes what `relied`
means. I verified both definitions give the same answer across the whole window (§2), so nothing
turned on it. The pattern is reported, not concluded on: the question is the user's (R5).

**O-b — what the fix got right, re-derived rather than accepted.** The seven-row inventory is
correct as a classification of *bears a signature at all*: I classified all twelve tracked files
under `ResearchSystem/contract/` by hand and reached the same seven. A-1's anchor is real and
current — `N0/N0-record.md` line 135 records `signed contract blob:
b2dbdf752d8c155e4c65b14b5f420b880b8184a1`, and `git rev-parse HEAD:…Contract-v3.md` returns exactly
that. The A1 amendment, whose retention motivated the `f054a08` repair, is still inside on both
branches of A-1: §9 is a sign-off block, and the index row in `ResearchSystem-Contract.md` names
signed file SHA-256 `2D672D0D…`, which is what `HEAD`'s blob hashes to. E2's three enumerated blobs
are all live and unchanged: `b2dbdf75…`, `68031fa2…`, and `8ad404b1…` at
`.goals/plans/document-work-assurance-harness-v3.plan.md`.

**O-c — the read→amend→re-read loop has now run twice and is not converging on this rule.** The
prior read's O-c recorded that C-3 has no convergence bound and that the user ruled the trade
intended (`5760f8b`); this is the second iteration and it carries a must-fix. Recorded so it is not
re-raised as a new observation, and so the user has the count.

**O-d — `Stage-Control-Contract.md` carries its own approval status in body fields** (`corrective
status: SIGNED`, `approval status: APPROVED`), which is the R4 defect class the N1 blob-keyed
exemption register exists for; that register enumerates two blobs and does not include it, its
authority being scoped to parsed frontmatter. Adjacent to my subject and reported, not raised.

**O-e — the convergence route transcribes reviewer-authored wording.** Both A-1 and A-2 are the
prior read's stated minimum fixes adopted near-verbatim, and M-1 and L-1 above are defects in that
proposed wording rather than in its adoption. The consequence is structural: on this route the next
reader is reading text the previous reader wrote, with no independent design pass between them, and
the redundancy E1 protects elsewhere is not present here. Reported under R5 — the question and the
conclusion are the user's.

---

## 6. Disclosure (R4)

**Read in full:** the subject (`CONSTRUCTION-CHECKLIST.md`, 128 lines); the amendment diff
`f97b348..9f2ec9a` and both hunks; the prior read record `v3-checkpoint-read-f97b348.md` (236
lines); the commit body of `87a4ced` and its `HARNESS-LEDGER.md` hunk;
`v3-harness-review-contract.md`, a 6-line stub redirecting to the subject, which is therefore both
my standing instruction and my subject; `N1/governance-exemptions.json`.

**Sampled:** commit bodies of the six other commits after `f054a08`, read in full as bodies but not
against their diffs except for the `--stat` classification in §2. `N0/N0-record.md` by grep plus
lines 128-170 and residual R4; `7011916`'s retired contracts **not** opened at all this session —
where §2 and §3 refer to hard rule 5, I am relying on the prior read's quotation of it, which I did
not independently re-fetch. The four sign-off blocks quoted in §3 were read in place with
surrounding context; the rest of those contracts was not.

**Probed only:** the twelve tracked files under `ResearchSystem/contract/` — signature-word grep
across all, headers of six, sign-off blocks of four. `General-Harness-Contract-v2.md` §14 for the
second immutability statement about Stage-Control. A grep for `.py` consumers of
`governance-exemptions.json` found none, which is weak evidence of absence, not proof.

**Measurement caveat (E3).** My first digest run hashed the worktree files and returned figures for
two of three paths that do not appear here; this checkout is on Windows and the worktree bytes are
not the blob bytes. Every digest in this record is from `git show <rev>:<path>` piped to the
`hashlib.sha256` one-liner shown in §3 — blob bytes — and the discarded run is named so the
discrepancy is not rediscovered as a finding.

**Marked, not verified (R4):** that this session is fresh context — a process claim, marked as such.
That the two rulings recorded in `HARNESS-LEDGER.md` at `87a4ced` were actually put to and answered
by the user; I can see the record, not the exchange, which is R7's ceiling and not a block.

**`UNVERIFIABLE`:** which reading of A-1 was intended. The sentence supports both, the commit body
does not disambiguate, and M-1 is written so that its evidence holds either way. Also unverifiable
from the repository: whether `Stage-Control-Contract.md` and `ResearchSystem-Contract.md` *should*
be frozen at their current bytes. `General-Harness-Contract-v2.md` §14 says the former is
*"immutable, read-only historical evidence"*, but that file is an `UNSIGNED CANDIDATE` with no
construction authority and was itself just ruled unprotected, so it is weak ground to stand a freeze
on. The inventory is recorded; the answer is the user's (R5).
