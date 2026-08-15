# FULL review — `52d8efb..0b8b824` (round AUDIT-CADENCE)

Independent FULL of the construction round whose candidate is
`0b8b8247de1f3a6b3c9f7ab3aa5838cac870c6e5` (`V3-AUDIT-CADENCE-v1`). Verdict at the end;
implementation first, boundary conformance second (`R3`).

## 1. Subject, re-derived (`R2`)

I was handed one range and nothing else. Everything below is re-derived from the repository;
no reported figure is accepted.

```
$ git log --format='%H %s' 52d8efb..0b8b824
  0b8b8247de1f3a6b3c9f7ab3aa5838cac870c6e5 V3-AUDIT-CADENCE-v1        (exactly one commit)
$ git rev-parse HEAD          -> 0b8b8247... (== subject tip; branch has taken nothing since)
$ git status --porcelain      -> (empty)
$ cat .harness/review-pending.json
  {"kind": "construction-round", "subject": "52d8efb...0b8b824...",
   "dispatched_at": "2026-08-01T17:56:34+00:00"}   (gitignored, not a committed range — E12 clean)
```

Subject commit dates 2026-08-01T17:56:23Z; dispatch follows it by 11 s; `E9`'s window is
intact and this record is the only commit it admits.

**Round identity.** Commit kind self-declares `candidate`; no `v3-review-full-*` record for
this subject exists in the migration directory — so no valid independent FULL has occurred
and this dispatch is the round's FULL (`E9`). Budget state found: FULL spent by this record;
fix leg and VERIFY unspent. Authorization: the 2026-08-02 user ruling's operative content is
committed (commit body + the section's own heading date); the adjudication behind it
(three-knob assessment, preview/wait) is chat-side — `R7` ceiling, stated, not a block.

**The change set, classified by hand:** `ResearchSystem/assurance/templates/run-v2/README.md`
(+28: one new section, *Audit cadence — pre-START rounds*) and `ResearchSystem/HARNESS-LEDGER.md`
(−2/+3: one completed struck backlog bullet deleted; one data-point line joined to the due
guarantee-surface retrospective bullet). Nothing else.

## 2. Implementation — do the three rules do what they claim (`R3` lead)

**The gate survives.** Rule 1 keeps round 1 a full walk; the section's opening sentence keeps
the InstructionCoverageAudit mandatory before START; from-scratch stays the fallback for
non-enumerable diffs and the rule for code/schema/generated-touching runs. No gate is
removed. The claimed backstop is real: REVIEW.md *What every result must carry* requires "an
instruction-completeness recheck against the raw instruction, not against the derived unit
map" at every result (invariant 10), and contract §6's own last sentence says the same —
so the review-independent full walk does survive downstream of any audit-side relaxation.

**Contract compatibility (the load-bearing question).** Contract §6 (the V3-D7 spine, frozen
blob `b2dbdf75` at the subject — re-derived by `git rev-parse`) says "performs **exactly one** `InstructionCoverageAudit` over the raw
frozen instruction and the proposed unit/obligation map… the audit has no repair loop.
`SPEC_GAP` requires a new WorkSpec revision and a new user START decision." The reading that
reconciles this with multi-round practice: *exactly one audit per frozen
instruction/proposed-map revision*; successive rounds exist only because a repair produced a
new revision. That practice predates this ruling and is committed: both `p4-doc` and
`p5a-firewall` carry `instruction-audit.json` with `audited_by: "…fresh-context subagent,
opus, round 4"`, each landed through a FULL-reviewed evidence commit. The audit schema
(`instruction-coverage-audit.schema.json`, frozen pack) requires
`{audit_id, work_id, work_spec_ref, instruction_ref, result, audited_by, audited_at}` — no
walk-method field; a delta-derived audit binding the exact final bytes satisfies it and
satisfies invariant 1 (binds the exact WorkSpec/instruction, `COVERED` before START).
Letter preserved; the reconciliation is implicit, though — low L-1.

**The delta mechanism is sound on its own precondition.** Rule 2's re-walk scope is {changed
units} ∪ {everything the repair touched} ∪ {prior round's flags}. The edge I probed: a
byte-unchanged unit whose *obligation* the repair deleted or rewrote — its coverage relation
changes with unchanged unit bytes. It is caught, because the WorkSpec diff (handed over in
full) contains the map-side change, putting it inside "everything the repair touched." The
soundness of citation-coverage rests entirely on the diff being cleanly enumerable over
exactly the bytes the prior audit bound — which `work_spec_ref.digest_sha256` +
`instruction_ref.revision` pin at run granularity. That precondition is the rule's own
fallback trigger, so the failure mode collapses into from-scratch. Observation O-3.

**The admissibility rationale is accurate.** The section's closing paragraph — a subagent
auditor is V3-D7-distinct, never review-independent — matches the record: N1's F1 fixed
distinctness-off-by-default, N1-R3 is the permanent limit ("`check_audit` cannot prove the
auditor and executor were independent contexts — it compares declared names"), and REVIEW.md
defines independence by who sets the question, which an executor-dispatched auditor never
satisfies. Handing the prior report to a delta auditor therefore degrades no independence
the audit ever had, while the reviewer-side prohibition stands untouched. The E10-citation
analogy is faithful: byte-unchanged ⇒ covered by citing the recorded prior audit, exact-byte
binding supplied by digest+revision where E10 uses blob ids.

**Rule 3** (one repair batch per round) conflicts with nothing: the contract's "the audit has
no repair loop" places repairs spec-side, and batching spec-side fixes before re-dispatch
changes no verdict path — it is the construction layer's own one-fix-round shape applied to
audit rounds.

**Ledger edits.** The deleted bullet was struck and complete ("已落候选… 等 FULL + 它自己的
read" — that round closed; the landed clause is live in checklist `E10` today, its narrative
in the amendment round's records); deleting it is recoverable bookkeeping in service of the
cap. The retrospective bullet gains the p5a data point and correctly leaves only the data
point here, rules in the README — conforms to the ledger's pointer-only discipline.

## 3. Assertions re-derived by command (`E3`-side claims in the commit body)

| assertion | command | result |
|---|---|---|
| ledger at 119 lines after commit | `wc -l ResearchSystem/HARNESS-LEDGER.md` → 119 | holds (cap 120, `tooling/hooks/ledger_cap_check.py` `MAX_LINES = 120`, runs clean) |
| nine layer members blob-unchanged since `v3-checkpoint-read-9541e1e.md` (record `10c040b`) | `git rev-parse 0b8b824:<path>` ×9 vs the read's table | holds — `02461be7 / f3a31208 / bd490c8b / 7b553516 / 17ff31bb / 52a97a48 / 68031fa2 / e1a2f26b / c2b713bf`, identical row for row; `10c040b` exists and adds exactly that record |
| batch touches no layer member | change set §1 vs the nine paths | holds (template README's non-member classification has recorded precedent — `9541e1e` read §1, `d01615b`) |
| L-3 / F-1 rides parked | ride condition = next batch touching the layer | holds — no member touched |
| p5a-firewall: four audit rounds, opus, fresh-context, two-file prose candidate | committed `instruction-audit.json` (`round 4`); candidate `8f6d872` (A2 amendment + one index row) | holds |
| "~50 min pre-START" (body) | freeze `2f07ce2` 01:50 → candidate `8f6d872` 02:37 | bracket 47 min — approximation holds for p5a; p3/p4 not timed from repo |
| rider bank owes nothing on this batch | `HARNESS-RIDERS.md` — five rows (F-c, O-2b, SCC, RA, F-f3) | holds — none targets either touched file |

## 4. Boundary conformance (run second)

`E8`: title `V3-AUDIT-CADENCE-v1`, kind named (candidate), one dense paragraph, no trailers,
two files both inside the ruling's scope, new commit, no push. `E9`: candidate consumed
nothing; this FULL is the round's first spend. `E10` opening coverage: discharged by
citation, re-derived here (§3). `E11`: preview/wait chat-side — `R7` ceiling. `E12`: subject
arrived as one range; the marker is gitignored worktree state, not a committed written-tip
range. No new guard code shipped, so `E4`/`E5`/`R8` mutation duties are vacuous this round —
the only mechanical instrument near the change (`ledger_cap_check.py`) is pre-existing and
was run, not trusted.

## 5. Findings

### Low — L-1 (`R9` wording-level; content named, so byte-channel (a) eligible)

**The section normalizes audit "rounds"; the frozen contract says "exactly one," and the
reconciliation is written nowhere.** Contract §6 reads "exactly one `InstructionCoverageAudit`"
per proposed map before START; the section speaks of rounds 1…N as ordinary practice. The
reconciling fact — one audit per frozen WorkSpec/instruction revision; rounds exist only
because repairs produce new revisions — is implicit in the contract's own SPEC_GAP sentence
and witnessed in the committed round-4 audits, but a reader holding only the two texts meets
an apparent contradiction. Downstream slip if unfixed: a reader taking "exactly one" per-run
either refuses a legitimate re-audit (conservative, harmless) or treats round 1 as
discharging the gate across a later spec repair — and that second path is already caught
mechanically, because invariant 1 binds the audit to `work_spec_ref.digest_sha256`, which a
repaired spec no longer matches. No unguarded decision path ⇒ wording-level. Content for the
channel, one clause at the end of rule 1 or the section's opening paragraph: *"a round is
the contract's exactly-one audit of one frozen WorkSpec/instruction revision; successive
rounds exist only because a repair produced a new revision."* Template README is not a layer
member, so an application owes no read.

### Observations (`R5` — reported; conclusions are the user's)

**O-1 — operative rule mass is accreting in the template README, outside the layer's read
discipline.** The run-v2 README now holds three bodies of operative text (authoring gate,
instruction authoring rules, audit cadence). The recorded classification that keeps it out
of the `E10` layer — "registers rules that *live* in EXECUTION.md and the governing plans and
forbids restating them — template documentation" (`9541e1e` read §1, `d01615b` precedent) — no
longer describes the new section, which is the *primary home* of its three rules by explicit
ruling ("the operative home of the authoring gate"). Consequence of the current
classification: amendments to this file take no independent post-amendment read. This round
took the stricter round path voluntarily; nothing obliges the next one to. Whether the README
joins the layer, the rules move to EXECUTION.md, or the classification stands is the user's
question; the shape is reported here so it is inherited deliberately.

**O-2 — the witnessed-cost figures are session-witnessed, not repo-derivable.** "~525k
tokens, ~28 min" and "changed by 1–4 lines each time" have no in-repo source: rounds 1–3 of
the audit and the intermediate spec states were working-tree-only, and token telemetry is not
recorded anywhere I can reach. `UNVERIFIABLE` (`R4`), disclosed — not folded into supported.
Shape corroboration is real: round-4 marker, opus, fresh-context in the committed audit;
two-file prose candidate; 47-min freeze→candidate bracket. The text's own "witnessed cost"
wording marks the provenance, and no rule's outcome turns on the exact figures.

**O-3 — the citation analogy binds at run granularity, not per-unit.** E10's citation clause
works because a read's record states each member's blob id; the audit analog pins bytes at
`work_spec_ref.digest_sha256` + `instruction_ref.revision` and delegates per-unit identity to
the handed-over diff. Sound while the diff is cleanly enumerable — which is the rule's own
fallback condition — but a future delta auditor citing a prior round across a boundary where
the diff was reconstructed rather than emitted would be citing bytes nothing pinned. Noted
for inheritance; no fix proposed, the fallback already owns the failure mode.

## 6. Coverage disclosure (`R4`)

**Read in full:** the subject commit (diff and body); `run-v2/README.md` at `0b8b824` (139
lines); `HARNESS-LEDGER.md` (119) and `HARNESS-RIDERS.md` at the tip;
`CONSTRUCTION-CHECKLIST.md` (standing instructions) and the review-contract stub;
EXECUTION.md (153); REVIEW.md (256); `v3-checkpoint-read-9541e1e.md` (239); contract §6–§8.

**Sampled:** contract §5 (schema/kind tables); N1-record — F1 block and rows N1-R1/N1-R3;
`2f07ce2` and `8f6d872` bodies; p4-doc and p5a-firewall `instruction-audit.json`;
`instruction-coverage-audit.schema.json` (required/properties);
`ledger_cap_check.py` (:1–40); p5a `user-decision-{start,final}.json`.

**Probed only:** `.harness/review-pending.json` (+ its gitignore status); template and run
directory listings; `10c040b` stat; freeze/candidate timestamps; migration-directory grep for
a prior record of this subject.

**Not verified:** that this review ran in a fresh context — a process claim, marked. The
chat-side adjudication behind the committed ruling (`R7`). The token/time figures (O-2).
p3-corr/p4-doc pre-START durations (only p5a bracketed from commit times). No product-run
suite was re-run: the batch ships prose and ledger lines, no code, schema or generated
surface.

## 7. Verdict

**`REVIEWED_NO_BLOCKER`.** The three rules do what they claim; the mandatory gate and its
review-side backstop stand; the frozen contract's letter is preserved; the admissibility
rationale matches the N1 record; both ledger edits check out; the commit body's re-derivable
claims all re-derive true. One wording-level low (L-1, content named — byte-channel
eligible, no read owed), three observations. Per `R10`, the low does not bank by default:
the spend-the-fix-leg / channel-apply / bank choice is the executor's to put to the user
before closeout.
