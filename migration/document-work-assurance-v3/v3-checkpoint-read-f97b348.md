# Checkpoint read — `CONSTRUCTION-CHECKLIST.md` blob `f97b3483`, the E10/E2 amendment

**No verdict.** A read is not a round (R3): it spends no budget, carries no verdict, and its
output is findings tiered must-fix / low / observation. This is the independent read E10 owes on
this amendment.

**Findings: 3 must-fix, 1 low, 4 observations.**

---

## 1. Subject, re-derived

The subject is a text, not a range. Its identity, established before reading it:

```
$ git rev-parse f054a08:ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md
f97b3483c4ac0ab22257ad8ce16fe62b9727e962
$ git rev-parse HEAD:ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md
f97b3483c4ac0ab22257ad8ce16fe62b9727e962
$ git log --oneline f054a08..HEAD -- ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md
(empty)
```

The bytes at `f054a08` are the bytes at `HEAD`; the four intervening commits touch this path not
at all. The dispatch's claim that the subject is unaffected by later commits holds.

The amendment is `git diff 17e2b65..f054a08` over that path: **three clauses**, two of them
repaired by `f054a08` relative to the candidate `af2905c`.

- **C-1 (E2)** — `existing files under ResearchSystem/contract/` → `the **signed bytes** under
  ResearchSystem/contract/ — signed by any instrument, contract or amendment alike`, plus the
  reasoning that the source rule froze signed bytes by category, never a directory. *Repaired:*
  the candidate said `the **signed** contracts`, which by the noun would have dropped the signed
  A1 amendment out of the freeze; `f054a08` replaced the enumeration with a category.
- **C-2 (E10)** — the deferral clause: an amendment of at most one sentence with nil effect on
  every round in flight may be relied on before its read, if the commit records both facts and
  the bytes ride the next read. Unchanged by the repair.
- **C-3 (E10)** — the convergence clause: a read's must-fix findings are answered by an amendment
  commit plus an independent re-read, which is not a round and spends no budget, until a round has
  relied on the text. *Repaired:* `f054a08` added `relied means took its governance from it, which
  authoring, citing or recording it is not`.

**The three dispatch facts, each verified rather than accepted.** (1) E10 obliges the read and
scopes it to the amendment text — confirmed in the subject's own line 65-67. (2) Both reviews of
the round declined to be it: `v3-review-full-af2905c.md` §1 — *"This FULL is not the read E10 owes
on these bytes… The read remains owed"*; `v3-review-verify-f054a08.md` §8 — *"the read E10 owes on
this layer is still owed, now on the repaired bytes. This VERIFY is not it and cannot be banked as
it."* (3) `f054a08` changed both E2 and E10 — confirmed by the split diff above.

**The citation C-1 rests on is accurate.** `7011916` rule 5 reads: *"**Signed bytes are
untouchable** (approved plan, contracts, N0 schemas incl. `common.schema.json`)"* — a category
list, and the word governing it is *signed*. No directory appears in it. C-1's characterization of
its own source is correct, and the pre-amendment directory wording was introduced later, by
`2b5fa28` (2026-07-27), not by the source rule.

**The repair to C-1 is load-bearing and correct.** Under the candidate's `signed **contracts**`,
`amendments/2026-07-18-a1-p4-scoped.md` — signed at §9 by the user, 2026-07-18 — is not a contract
and would have left the freeze. `signed bytes … contract or amendment alike` keeps it in.

---

## 2. Must-fix

### M-1 — `at most one sentence` is not a size bound in this file

**Location:** line 67, C-2. **Ground truth it violates:** the clause's own function, which is to
gate deferral on smallness, and the demonstrated grammar of the rule it sits in.

E10's entire rule body is **one sentence**. Every clause is semicolon-joined; the only terminal
period after the opening definition is the one closing `no characterization.`:

```
$ sed -n '61,75p' … | tr '\n' ' ' | sed 's/\. /.\n>>>PERIOD<<< /g'
- **E10** The instruction layer is … when amended.
>>>PERIOD<<< Its edits are additive or subtractive … no characterization.
>>>PERIOD<<<
```

The amendment under read added C-2 and C-3 — two complete governance clauses, eleven lines —
**without creating a single new sentence boundary.** An amendment that introduces two rules
therefore satisfies "at most one sentence" verbatim. The test is defeated by the bytes that
introduced it.

The only restraint left standing is the second condition, *nil effect on every round in flight*,
which does all the real work and is self-judged.

**Latent, not exercised:** this round claimed no deferral — it went to a FULL, a fix and a VERIFY.
Nothing has escaped through this yet.

**Minimum fix:** replace the sentence count with a test that measures effect rather than
punctuation — e.g. an amendment that adds no new clause to any rule — or delete the size condition
and let the nil-effect condition carry the clause alone.

### M-2 — `signed` is an undefined guard term and is not determinable from the bytes it scopes

**Location:** line 24-25, C-1. **Ground truth it violates:** the standard this same amendment
adopted one clause later.

C-1 replaces an enumerable criterion (*existing files under a directory* — decidable by `ls`) with
a property of file content, and never says how to test it. Probing every tracked file under
`ResearchSystem/contract/` finds **four different encodings of signature and one deliberate
absence**:

| encoding | file | evidence |
|---|---|---|
| signature held **externally**, file carries none *by design* | `Document-Work-Assurance-Contract-v3.md` | frontmatter `status: candidate-awaiting-user-signature`; *"this file never carries its own approval status or digest"* — signature recorded in `N0/N0-record.md`, binding the blob |
| inline status field | `Stage-Control-Contract.md` | `corrective status: SIGNED` |
| inline prose at a section | `amendments/2026-07-18-a1-p4-scoped.md` | *"signed at §9 by the user (Melclycj), 2026-07-18"* |
| sign-off block at file end | `ResearchSystem-Contract.md` | §4, `signed-by: user (Melclycj)`, `signed-date: 2026-07-12` |

The first row is the sharp one: **applied to the harness's flagship contract by reading the file,
the new test returns "not signed."** That file survives inside E2 only because it is separately
enumerated by blob `b2dbdf75…`. Where the category clause is the *only* thing deciding — every
file not in the enumeration — the reader must know which of four conventions to look for, and for
one convention must know to look in a different file entirely.

This is the same defect class as **F-1**, the undefined guard term the same amendment repaired in
E10 by defining `relied`. The round adopted the standard and applied it to one of the two terms it
introduced.

**Minimum fix:** state the test in E2 — signed = a signature recorded against the file's blob,
either in the file's own sign-off block or in a committed record that names the blob — and name
`N0/N0-record.md` as that record for the contract whose file carries none.

### M-3 — the narrowing's reach was never enumerated; the only record addressing it names three files

**Location:** not the checklist text but the round's record of it — `707722d` closing O-3.
**Ground truth it violates:** R2's requirement that a classification of changed paths be done by
hand rather than reported.

Classifying all twelve tracked files under `ResearchSystem/contract/` by hand against both
wordings:

| leaves E2 | status | disposition |
|---|---|---|
| `…supersession-2.md` | UNSIGNED | **intended** — the amendment's whole purpose |
| `amendments/2026-07-17-projection-v2.md` | *"ABANDONED … Never signed"* | harmless |
| `block-grammar.md` | frozen at P0, unsigned | ruled — `707722d`, no protection |
| `content-roots.yaml` | frozen at P0, unsigned | ruled — `707722d`, no protection |
| `baseline/P0-baseline.md` | frozen at P0, unsigned | ruled — `707722d`, no protection |
| `General-Harness-Contract-v2.md` | `UNSIGNED CANDIDATE` | **never put to the user** |
| `adapter-map.md` | *"reviewed at P1"*, no signature | **never put to the user** |

Seven files leave E2; the ruling adjudicated three. Two were never put to the user, and one of
them is **read by live code**:

```
rsclib/harness/schemas.py:20  CONTRACT_PATH = RS_ROOT / "contract" / "General-Harness-Contract-v2.md"
rsclib/harness/schemas.py:77  contract_digest = bytes_digest_ref(CONTRACT_PATH.read_bytes())
```

Editing it changes a `contract_digest` the harness emits — the same shape of consequence as the
`content-roots.yaml` caveat that *was* put to the user before the O-3 ruling.

`ResearchSystem-Contract.md` and `Stage-Control-Contract.md` stay inside E2, but only via M-2's
fourth and second encodings.

**Minimum fix:** record the complete list of what the narrowing moved out of E2, and put the two
un-adjudicated files to the user. Whether they should be protected is the user's question, not a
reviewer's (R5) — the defect is that a ruling was taken against an inventory of three when the set
was seven.

---

## 3. Low

### L-1 — `citing` versus `took its governance from it` leaves load-bearing citation unclassified

C-3's repair defines `relied` by excluding *authoring, citing or recording*. A citation that
**decides** a question sits in neither box.

**The downstream decision, named as R9 requires:** `707722d` closes O-3 on the ground that *"the
repaired E2 — which freezes signed bytes rather than a directory — leaves them outside."* That is a
citation of the amended text used as the operative reason for a disposition. Whether it counts as
`citing` (no round ever opens on a later change) or as taking governance from the text (any later
change opens a round) is not answerable from the sentence.

**Not inflated to must-fix:** nothing turns on it there, because the ruling is over-determined — it
also rests on hard rule 5, which reaches the same outcome, and it states so. The exposure is that
the next such citation may not be over-determined.

---

## 4. Observations

**O-a — E2's freeze surface has only ever contracted, across three edits by three instruments.**
`2b5fa28` wrote `ResearchSystem/contract/` **and `.goals/plans/`**; `cf8e1b1`
(`V3-PHASE-A-READ-FIX-v1` — a prior read's fix) dropped `.goals/plans/`; this amendment narrowed
the directory to signed bytes. Each step was separately justified and the first two are outside
this read's subject. Reporting the shape only; the question and the conclusion are the user's (R5).
Read beside O-1's report of E10 growing clause by clause, this is one file in which the freeze rule
shrinks while the amendment rule grows.

**O-b — C-2's two recorded facts are both self-judged.** *One sentence* and *nil effect in flight*
are asserted by the execution side in its own commit, against E9's *"Never self-classify which
round consumed what: every recorded escape from the cap was a renamed round."* The mitigation is
real — the next read audits the bytes — and F-3 already banks the unowned queue for *"the bytes
ride the next read."* Noted, not raised.

**O-c — C-3's read→amend→re-read loop has no convergence bound**, and the FULL's O-2 already
observed that the clause removes the instrument that made a non-converging chain countable. The
user ruled that trade intended (`5760f8b`). Recorded so the next read does not re-raise it either.

**O-d — what this read costs.** No round has relied on these bytes. The four commits after
`f054a08` touch only `HARNESS-LEDGER.md` and the read dispatch, and each self-declares *"not a
round, consumes no budget."* Under C-3, M-1 through M-3 are therefore answerable by an amendment
commit plus an independent re-read of the amended text — not a round, no budget. The single strain
is L-1: `707722d` is the one candidate for reliance, and it is a ruling rather than a round, so
C-3's *"no round has relied"* is satisfied on its face.

---

## 5. Disclosure (R4)

**Read in full:** the subject (`CONSTRUCTION-CHECKLIST.md`, 121 lines); the amendment diff and both
its halves; `v3-harness-review-contract.md` (a 6-line stub redirecting to the subject, which is
therefore both my standing instruction and my subject); the four commit bodies after `f054a08`.

**Sampled:** `v3-review-full-af2905c.md` §1 only and `v3-review-verify-f054a08.md` §8 only — the
two sections the dispatch named. I did **not** read either review in full; my knowledge of what
those rounds banked (F-3, O-1, O-2, O-3) comes from the commit bodies, not from the records
themselves. `7011916`'s operating contract: opening 80 lines plus rule 5 at 174-176, not the whole
file.

**Probed only:** the twelve files under `ResearchSystem/contract/` — signature-word grep across
all, plus headers of six and the sign-off block of one. Live-code reachability by grep over
`rsclib/` and `ResearchSystem/`.

**Marked, not verified (R4):** that this session is fresh context — a process claim, marked as
such.

**`UNVERIFIABLE`:** whether the two un-adjudicated files in M-3 *should* be protected. That is the
user's question under R5, and I record the inventory rather than the answer. I did not attempt to
determine whether any signature exists for `General-Harness-Contract-v2.md` or `adapter-map.md`
outside their own bytes, which M-2 is precisely the complaint about — if such a record exists, M-3's
un-adjudicated set shrinks and M-2 grows correspondingly stronger.
