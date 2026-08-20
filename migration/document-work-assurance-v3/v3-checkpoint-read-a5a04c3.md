# Instruction-layer read — `a5a04c338decb9c61d0a94338455861f520f5f1b`

`E10` read of the instruction layer at `a5a04c3`. Not a round: no verdict, no budget
consumed (`R3`). It discharges the independent read the three `SIMP-ABCD` amendments
declared owed and rode to *the next read of this layer* (`6f850db` for `EXECUTION.md` and
`REVIEW.md`, `3657687` for `document-harness/README.md`), and every member is read end to
end here, so a later opening can cite this record for all nine rather than a chain.

**Findings: 0 must-fix, 2 low, 1 observation.** The three amendments say what they claim;
their two factual assertions about the repository reproduce; the nine-path enumeration is
still item-for-item equal to both code pins; no round has relied on the amended text, so
the read lands before `E10`'s deadline and not after it. Both lows are on the new
`REVIEW.md` section: it changes which observations reach a verdict without settling how the
one it removes is disposed of.

## 1. Subject, re-derived (`R2`)

Handed one SHA and the phrase *an E10 read*. Round, obligations, member set and every figure
below are re-derived here; nothing is taken from the dispatch prompt, the ledger, the commit
bodies, or the round's own FULL and VERIFY.

```
$ git rev-parse HEAD                  -> a5a04c338decb9c61d0a94338455861f520f5f1b
$ git status --porcelain              -> (empty)
$ git rev-list --count 838c413..HEAD  -> 42
$ cat .harness/review-pending.json
  {"kind": "layer-read", "subject": "a5a04c338decb9c61d0a94338455861f520f5f1b",
   "dispatched_at": "2026-08-05T12:38:58+00:00"}
```

HEAD **equals** the subject and the tree is clean, so worktree reads are reads of the subject
bytes and the branch has taken no commit since dispatch — this record is the first it admits
(`E9`). Dispatch (12:38:58Z = 22:38:58+10:00) post-dates the subject commit (22:02:30+10:00).

`E10`'s sentence **at the subject blob** governs the member set: it enumerates nine paths and
closes with "and nothing else", so the set is decidable by reading it and no open tail has to
be swept.

| # | blob at `a5a04c3` | lines | member | since the last read |
|---|---|---|---|---|
| 1 | `4d0c7330` | 173 | `document-harness/CONSTRUCTION-CHECKLIST.md` | unchanged (also this session's standing instructions) |
| 2 | `ae887dd4` | 37 | `document-harness/README.md` | **changed** (`f3a31208` → here, at `3657687`) |
| 3 | `df2a7834` | 162 | `document-harness/EXECUTION.md` | **changed** (`bd490c8b` → here, at `6f850db`) |
| 4 | `3350bfac` | 284 | `document-harness/REVIEW.md` | **changed** (`c19d8cb9` → here, at `6f850db`) |
| 5 | `17ff31bb` | 5 | `migration/…/v3-harness-operating-contract.md` (stub) | unchanged |
| 6 | `52a97a48` | 5 | `migration/…/v3-harness-review-contract.md` (stub) | unchanged |
| 7 | `68031fa2` | 124 | `contract/…-v3-supersession-1.md` | unchanged |
| 8 | `e1a2f26b` | 113 | `contract/…-v3-supersession-2.md` | unchanged |
| 9 | `09aa8699` | 44 | `schema/document-assurance-v3/paragraph-map.schema.json` | unchanged |

Blob ids from `git ls-tree -r a5a04c33`, line counts `wc -l` on `git show` at the subject.
The six unchanged rows are byte-identical to the table in `v3-checkpoint-read-838c413.md` §1,
re-derived by `git ls-tree -r 838c413` rather than read off that record. **All nine were read
end to end here regardless of citation eligibility** — members 7 and 8 were previously covered
only through chains to `v3-checkpoint-read-d58969d.md` and `v3-checkpoint-read-403fc9a.md`,
and 237 lines is cheaper than carrying the chain forward again.

`git diff --stat 838c413 a5a04c33` over the nine returns exactly three files, 40 insertions
and 6 deletions. Exactly 2 of the range's 42 commits touch a member; the other 40 touch none.

## 2. The three amendments against the repository (`E3`)

**`EXECUTION.md`** replaces the paragraph warning that a trivial check bound under the
both-modes value dodged the two `review_only` sentences with a rule: the mode is a two-way
choice, `local_check` means the check decides the obligation outright, and a demand with a
script-decidable half plus a semantic residue becomes two obligations. The deletion the rule
rests on is real at the subject — `common.schema.json`'s `verificationMode` is
`["local_check", "review_only"]`, and `document-work-spec.v2.schema.json`'s deterministic
conditional is `{"verification_mode": {"const": "local_check"}}`. "One honesty boundary"
now matches the one boundary that follows it.

**`REVIEW.md`** adds §*What is not in the subject: the run's own checkers*. Its one factual
claim about the repository reproduces: `v3-review-full-fef3a2e.md` carries findings `f1`–`f7`
(seven), and `f2`–`f5` name assertion strength in `chk-bookkeeping`, `chk-tripwires`,
`chk-tooling` and `chk-open` respectively. Its outbound link resolves at the subject tree.

**`README.md`** widens the journal row and repairs it while touching it. Both hrefs resolve
(`document-harness/journal/checker-and-map-2026-08-05.md` and
`migration/…/journal/reform-2026-07-29.md`); the row's link text and target now agree, where
before the text said `journal/` and the href reached one file in the migration tree. Nine
journals live beside the README at the subject and one in the migration tree — the row now
reaches both directories.

**Membership, mechanically.** Parsing the backticked path tokens out of `E10`'s sentence at
the subject blob and comparing against both code pins:

```
prose tokens: 9   LAYER: 9   EXPECTED: 9
prose == LAYER      : True
LAYER == EXPECTED   : True
('exactly these nine paths' and 'and nothing else' both present; all nine resolve at the subject tree)
```

No `.py` file appears in the range, so the pins did not move; the prose was already equal to
them at `838c413` and still is. The prose leg remains bound by nothing mechanical — rider
`E10-sync`, not re-reported.

## 3. What the amendments may have falsified elsewhere — swept

- **Both-modes vocabulary.** Grepping all nine members for `local_check_and_review` /
  `both-modes`: two hits, both inside the new text itself, both describing the deletion in
  the past tense. No member still offers the value. Repo-wide the string survives only under
  `assurance/runs/` (closed runs) and `HARNESS-LEDGER-archive.md`, which supersession-1 §3
  keeps as pinned history — not a defect.
- **The paragraph map is now form-conditional; two members describe it unconditionally.**
  Under `SIMP-B/C` the enumerated form stops owing the paragraph map and the preamble gate
  (`run-v2/README.md` form table). Member 9's `description` and member 2's row 25 describe how
  the artifact is produced and enforced, not that every run owes one, so neither is false;
  the obligation lives in `run-v2/README.md`, which states the branch. **Checked and cleared,
  not banked** — under `R9` I can name no downstream decision that goes wrong, so it spawns
  nothing. Recorded here because a later reader will ask.
- **Supersession-2's two `UNSIGNED` assertions** (`:3` and `:107`) against a file signed
  2026-07-30. Already found and dispositioned as `L-1` of `v3-checkpoint-read-403fc9a.md`,
  which established the repair path narrowed to §13-successor at the moment of signature. Not
  re-reported; re-reporting a dispositioned finding spends the channel twice.
- **Cross-references into the amended text.** `supersession-2:107`'s `E10` citation still
  lands on vocabulary `E10` holds. `CONSTRUCTION-CHECKLIST.md` `R10`'s sentence — product-run
  observations belong to `HarnessIssue`, never the bank — is *corroborated* by the new
  `REVIEW.md` routing rather than contradicted by it; it is also why `L-2` below has nowhere
  else to go.

## 4. Process boundary — second (`R3`)

- **`E10` sequencing holds.** Both commits declare the amendments and the owed read in their
  first line. They are design — they change what `EXECUTION.md` and `REVIEW.md` require — so
  the deferral clause (no clause added, nil effect in flight) was never available to them, and
  the design route was taken: a round opened, ran its FULL and its VERIFY. `E10`'s deadline for
  the read is *reliance*, not the round's close. **No reliance has occurred**:
  `git log 3657687..a5a04c33 -- ResearchSystem/assurance/runs/` is empty, so no product run has
  opened since, and the amended text governs product runs. The round's own FULL cites the new
  `EXECUTION.md` sentence when disposing of `f4`, which is `E10`'s excluded *citing*, and it is
  expressly disqualified from being this read.
- **Nothing else rides.** Grepping the 42 commit bodies for free-channel language returns two
  hits, both in `7ef4ed4` / `c68d3d4`, which dispose of the **previous** read's findings into
  riders `E2-FC` and `E10-crit` (both present in the bank) and write no layer bytes. No
  outstanding layer application.
- **Ledger bindings.** The ⛔ breakpoint is the P5B batch, whose precondition is rider `V-1`.
  Neither is this read's subject. The two `SIMP-ABCD` items the ledger records as unsettled —
  the VERIFY's five observations and `SIMP-A4`'s second reading — are round bookkeeping, not
  layer bytes; `SIMP-A4`'s ambiguity concerns which lint discharged it, and both readings
  leave the layer text as it stands.
- **This read is a checkpoint read, not the cold read `E10` owes at a round's opening.** No
  round is open at the subject; the warrant is the three amendments. If the members are
  unchanged when P5B opens, that opening is covered by citing this record.

## 5. Findings

### Low

**L-1 — for a `local_check` obligation whose check decides less than the obligation demands,
the new section and the file's own `UNVERIFIABLE` principle give opposite dispositions, and
the section's own worked case is exactly that shape.** Location: `REVIEW.md` at `3350bfac`,
§*What is not in the subject* (`:24-47`) against §*`UNVERIFIABLE` is a real answer* (`:221-231`)
and `EXECUTION.md` at `df2a7834` `:145-155`. Ground truth: after the amendment `local_check`
means "a deterministic check decides the obligation outright". The new section tells the
reviewer to establish that the check *ran, reproduces, and observed the tree it was entitled
to* — three properties a check asserting the bare word `battery` satisfies — and then puts
*should this checker assert more?* out of scope, "never move a verdict". So an obligation can
take `SUPPORTED` on a check that decided almost none of it, which is the move
§`UNVERIFIABLE` names as the product's characteristic failure: "folding it into `SUPPORTED`
because nothing contradicted it is how an unverified property becomes an asserted one".
The mirror direction is settled and settled the other way — §*The `review_only` question*
makes a `review_only` declaration a script could have decided **a finding** about the
WorkSpec — and the WorkSpec is control plane, which the new section's own first sentence puts
*inside* the subject. **Decision that goes wrong unfixed:** one reviewer reports the thin
check as a control-plane finding on the mode declaration, another suppresses it as checker
weakness, with equal textual support, and the two disagree about whether the obligation is
`SUPPORTED`. **Deadline:** the next product run's FULL — the ledger's breakpoint is the P5B
batch, and the section's own witnessed case is that four of `p5b-firewall`'s seven findings
were of this class. **No bytes are supplied, deliberately:** every tiebreak I can write adds a
bound to one of the two rules, which `E10` sends to design and opens a round; reported without
them so it banks (`R10`, and the 2026-07-29 routing for a middle low without appliable bytes).

**L-2 — the observation the new section removes from the verdict is routed to a channel the
reviewer has no stated way to reach, and the same file already records this defect class.**
Location: `REVIEW.md` at `3350bfac` `:29-31` ("a **`HarnessIssue`**, raised through that
channel and triaged after the run") against `:127-135`. Ground truth: `HarnessIssue` occurs
exactly once in `REVIEW.md` — that sentence. The file's deliverables section says the reviewer
persists and commits **exactly two artifacts**, and `HarnessIssue` is neither. The schema
narrows `observed_after` to `CLOSED` / `STOPPED_REPLAN` and says so in terms — "an issue
claiming to be observed mid-run is unrepresentable, so it cannot be used to influence a run in
flight" — and a review round happens mid-run, so the reviewer cannot represent the observation
when they have it. Contract §3 does make the owner the *observer* rather than the executor, so
the reviewer is eligible; nothing tells them that, nothing gives them a carrier for the
observation until `CLOSED`, and nothing tasks anyone with collecting it afterwards.
`EXECUTION.md:26` lists `HarnessIssue` under what the **executor** owns, which is the only
role-to-artifact statement in the layer. **Decision that goes wrong unfixed:** the reviewer,
correctly declining to make it a finding, has nowhere to put it and it is lost — under the
zero-restatement dispatch contract they learn their duties from this file alone, and this file
already carries the precedent at `:120-125`, where the p4-doc FULL "was completed correctly and
then stopped with the verdict in-session, because nothing here said where the result goes".
**Deadline:** the same one as `L-1`, and for the same reason. **No bytes:** naming a carrier
adds an obligation to `REVIEW.md`, which is design.

### Observation (`R5` — reported; the conclusion is the user's)

**O-1 — the design route borrows the deferral clause's mechanism, and `E10` does not say it
may.** `E10` gives two paths for an amendment. The deferral path spells out its timing —
relied on before its read, provided the commit records both facts and *the bytes ride the next
read of this layer*. The design path says only that a round opens; it fixes no read timing at
all, so the deadline falls back to the general sentence, *before any round relies on it*. Both
`SIMP-ABCD` commits correctly classified themselves as design and then adopted the deferral
path's sentence — "rides the next read of this layer" — to say when. The outcome here is right
on the general rule, and this read confirms it. What the shape costs is that the honest timing
of a design amendment's read is an inference each executor re-derives, in language the rule
attaches to the other branch. Whether `E10` should say so is the user's question, not a defect
in these bytes.

## 6. Coverage disclosure (`R4`)

**Read in full at the subject blobs:** all nine members — 1 (173, also as standing
instructions), 2 (37), 3 (162), 4 (284), 5 (5), 6 (5, standing-instruction entry point),
7 (124), 8 (113), 9 (44). Also: the three-member diff, plain; `v3-checkpoint-read-838c413.md`
(248); the commit bodies of `6f850db`, `e01314f`, `75df9be`, `3657687`, `c7fb720`, `214f743`;
`HARNESS-LEDGER.md` (119) and `HARNESS-RIDERS.md` (19) at the subject;
`harness-issue.schema.json`; `layer_path_check.py`'s docstring and `LAYER`; the
`LayerMembership` block of `test_precommit_checks.py`.

**Sampled:** `v3-review-full-3657687.md` §5–§7 and `v3-review-verify-c7fb720.md` §f-table and
§O-5 for the reliance question; `v3-checkpoint-read-403fc9a.md` §L-1 for the `UNSIGNED`
disposition; `v3-review-full-fef3a2e.md`'s findings table; `run-v2/README.md`'s form table and
pre-freeze gate; `common.schema.json`'s `verificationMode`; `document-work-spec.v2.schema.json`'s
deterministic conditional; contract §3 / §8 step 11 / §11.

**Only probed:** the 40 non-member commits in the range — classified by path, bodies grepped
for free-channel language, not read; the repo-wide `local_check_and_review` survivors, counted
by file, not read; the tests and modules `SIMP-ABCD` added, which are the round's work product
and not this read's subject.

**Not verified:** that this read ran in a fresh context — a process claim, marked, not
verified (`R4`). The user rulings behind `SIMP-A1` and `SIMP-A5` exist in the round journal and
the commit bodies; their originals are chat (`R7` — ceiling stated, not a block). That the
executor's mutation evidence for the round was performed as described — the round's own VERIFY
and closeout already record a correction to one restore digest, and adjudicating that is not
this read's subject.

**Ceiling:** what is established is that the three amendments say what they claim, that their
two repository assertions reproduce at the subject, that the enumeration still equals both code
pins, that no member is left holding a statement they falsified, and that no round has relied on
them. What is **not** established is how a real reviewer will resolve `L-1` — both readings have
textual support and I cannot predict which a fresh reviewer takes; what I can show is that they
differ on whether an obligation is `SUPPORTED`. Whether either low is worth a round before the
P5B batch is the user's call, and deciding either one is design.
