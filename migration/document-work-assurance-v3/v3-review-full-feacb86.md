# FULL review — `0224176..feacb86` (layer-incorporation round)

Independent FULL of the layer-incorporation round. Subject received as one range and
nothing else (`R2`); everything below is re-derived from the repository. Standing
instructions: `CONSTRUCTION-CHECKLIST.md` at the subject tip (the blob this round amends —
read in the pre-amendment form `33126c19` via the stub chain first, then as amended).

**Verdict: `REVIEWED_NO_BLOCKER`.** 0 blockers, 2 lows (one with exact bytes supplied,
one wording-level), 3 observations.

## 1. Subject, re-derived

```
$ git rev-parse HEAD        -> feacb861051ef8d410bacd7c25c24216e1eea484
$ git status --porcelain    -> (empty)
$ git log --oneline 0224176..feacb86 -> 7 commits
```

Classified by hand: six bookkeeping commits touching only `.goals/**`,
`HARNESS-LEDGER.md`, `HARNESS-RIDERS.md` (`0a3d18d` bank backfill, `4ad1184` + `bf73536`
ledger ruling records, `d6a477c` plan write, `ef46c31` NEXT pointer, `c61d82d` preclear
reconcile) — none touches a layer file, a schema, a contract byte, or tooling
(`git diff 0224176..HEAD --stat -- ResearchSystem/tooling/` → 0 lines) — plus one
candidate `feacb86` amending `CONSTRUCTION-CHECKLIST.md`, `REVIEW.md`,
`HARNESS-RIDERS.md`, the round plan, and adding the round journal. Round identity from
the committed plan (`harness-layer-incorporation-round.plan.md`) and ledger: a true
amendment round, ruled 2026-07-31, sequenced before Phase C4; budget virgin at dispatch
(cold read discharged by citation at zero cost, this FULL is the first spend). The
freeze marker `.harness/review-pending.json` carries exactly this range; the branch has
taken no commit since the candidate (`E9` freeze holds).

## 2. Implementation — the nine edits against their sources (`R3`, run first)

Each edit was traced to its named source record, which I re-read at the cited lines.

| edit | source re-read | does the landed text do what the source asked? |
|---|---|---|
| `E10` seam: free channel for byte-supplied lows (BC-1) | `a6b87ad` commit body + ledger ruled-line 2026-07-30 | ✓ — clause content matches the (a) ruling (applied immediately, layer included, reported after, reversible; no-bytes lows bank; layer application owes the ride-along read at per-member digest cost) |
| `E10` seam: design clause moved after the relied qualifier + collision rule (F-1r) | `v3-review-full-8ec4c60.md:223-241` | ✓ — the minimum fix verbatim: clause now follows "…once one has, changing it opens a round;" and "design wins and the round opens" answers who-wins |
| `E10` seam: relied definition parenthesized (V-c) | `v3-review-verify-f054a08.md:244-249` | ✓ — the contrastive dash before "once one has" is restored |
| `E10` seam: design test extended to replacements/deletions (E10-d) | rider row; no verbatim minimum fix exists in any record — designed this round, disclosed on card and in journal | ✓ with a residue — see low L-2 |
| `E10` citation clause: read records state blob ids (L-2r) | `v3-checkpoint-read-d58969d.md:145-152` | ✓ — the record property is now a rule; `v3-cold-read-ae4df09.md` §1 already satisfies it, which is what made this round's citation coverage checkable |
| `E2` *existing* pinned (E2-t) | `v3-checkpoint-read-dcced4e.md:198-212` + `v3-cold-read-451e8b0.md` O-3 | ✓ — and the pin's facts hold by command: the pack entry joined the list at `11d147e` (2026-07-29); `git ls-tree` counts 14 files at `11d147e` and 14 at HEAD, `git diff 11d147e HEAD -- …schema/document-assurance-v3/` empty. The pin also makes `E10`'s schema-description clause reachable (O-3's second rule) |
| `E2` fourth blob (E2-s2, user ruled IN via card OK) | `v3-checkpoint-read-403fc9a.md` L-1 + §4 | ✓ — list line gains `e1a2f26b…`, "Three blobs" → "Four blobs"; carrier untouched: supersession-2 blob `e1a2f26b` identical at `ae4df09`, `c61d82d`, and HEAD |
| `E12` recorded-range qualifier (O-4r) | `v3-cold-read-451e8b0.md:204-209` | ✓ — "recorded in a file" + "CLI printing a resolved full SHA is display" is exactly the reading under which the record said rule and tool agree |
| `E8` kind vocabulary +amendment/ruling/record (O-6) | `v3-review-full-af2905c.md:401-403` + the four attested instances | ✓ — covers all four; see observation O-1 for the shapes this very round minted |
| new `R10` (bank governance incorporated) | riders header at `c61d82d` (the migrated text's single source) | ✓ — see §3 |
| `REVIEW.md` verdict-basis section (VB-1) | ledger line deleted by `8ec4c60` (recovered: *"review 判据 = repo 现实为判据、requirement 只当问题清单（`R3` 顺序当真…"*), `v3-review-full-8ec4c60.md:123` confirming the bank | ✓ — repository reality as verdict basis, obligation list as question list, implementation first / conformance second |

## 3. The R10 migration — deletions and seam-stitching only, verified line against line

Old header (three prose blocks at `c61d82d:HARNESS-RIDERS.md`) vs. landed R10:

- Routing sentence: kept; the dead `C-3` reference becomes "`E10`'s must-fix channel" —
  disclosed in the commit, and accurate (the must-fix amendment channel is `C-3`'s live
  successor in this checklist).
- Row format / no-narrative / redemption sentences: verbatim.
- Tightening ①: verbatim minus the transition tail ("rows predating this get their
  targets named at their next due-check") — disclosed; the backfill it scheduled was
  executed at `0a3d18d` (19 named rows counted at that commit), so it governed an empty set.
- Tightenings ② and ③: verbatim, including the "(a moment the defect starts to bite)"
  parenthetical the journal draft had elided — the landed text is closer to the source
  than the draft, in the right direction for a migration.
- New matter in R10 is exactly the bank/HarnessIssue division sentence, which the
  2026-07-31 ruling (`bf73536`) said would be written into the incorporated text.
- The "Split out of HARNESS-LEDGER.md 2026-07-29" provenance line is dropped; the fact
  survives at ledger line 48 and in git history — a deletion, not a loss.

Redemption discipline: the eleven rows (BC-1, E10-d, F-1r, L-2r, E2-t, E2-s2, O-4r, O-6,
V-c, O-1, VB-1) delete in the same commit their fixes land; 8 data rows remain (F-4, F-c,
F-d, O-2b, SCC, CT, RA, F-3r — counted, matches the plan's expected remainder). O-1
closes on the user's explicit no-split ruling, recorded in the journal. The riders file
stays outside the layer: `E10`'s membership sentence is unamended on that point and
`layer_path_check.LAYER` is the same eight paths, riders not among them.

## 4. Figures, re-derived (`R2` — no reported number accepted)

- Suites, all run here at HEAD: `tests` 29/29 OK · `tests/stage_control` 20 run, 0
  failures · `tests/harness` Ran 39 OK · `tests/document_harness` Ran 169 OK ·
  `tests/document_harness_review` Ran 354 OK · `repo-audit.py` exit 0.
- Frozen surface (`E2`, post-amendment four-blob form): `git rev-parse HEAD:<path>` →
  `8ad404b1…` (signed plan), `b2dbdf75…` (contract), `68031fa2…` (supersession-1),
  `e1a2f26b…` (supersession-2); porcelain over `schema/` + `contract/` empty; `git diff
  HEAD` over both user-locked oracles empty; no schema/contract path in the range.
- Cold-read citation coverage, re-derived per member: all eight layer blobs identical
  between `ae4df09` and the opening HEAD `c61d82d` (`33126c19`, `4daab565`, `bd490c8b`,
  `70bc521e`, `0ae222fd`, `7dcdb817`, `68031fa2`, `e1a2f26b`); `git diff --name-only
  ae4df09 c61d82d -- ResearchSystem/schema/ ResearchSystem/contract/` → 0 paths, so the
  member set is still eight. The citation to `v3-cold-read-ae4df09.md` is valid — that
  record tabulates each member's blob id (§1), which is the property L-2r now makes a rule.
- Bookkeeping spot-checks: `0a3d18d`'s CT rewrite is accurate — `issues.py:158-204` read
  here: `check_triage` validates phase, route membership, target-path presence and
  `work_id` equality, and never checks that the target path identifies the issue in hand.
  The three pointer-retrue commits (`ef46c31`, `c61d82d`) match git reality as I derived
  it independently (C3 closed on a fully-spent budget: `71d43be` → `0576322` FULL →
  `7e9c19b` fix → `f0e5d64` VERIFY; this round sequenced first).

## 5. Boundary checks (run second)

- `E9`: budget virgin before this FULL; the six pre-candidate commits are bookkeeping
  under the has-a-FULL-occurred test (none is a fix); branch frozen since dispatch. ✓
- `E8`: all seven titles `V3-…-v1`, single dense paragraph, kinds named (candidate
  explicitly; bookkeeping commits self-describe). Staging method and no-amend are process
  claims — marked, not verified (`R4`). No push (standing user gate). ✓
- `E11`/authorization: the card render and the user's reply are chat events; the
  decision-relevant content — three rulings, the R10 placement, the `C-3` substitution,
  the E10-d designed fix — is recorded in the journal, the candidate's commit body and
  the ledger ruled-lines, so nothing load-bearing is chat-only. The journal honestly
  distinguishes ruling 1 (voiced: "同意不拆") from rulings 2–3 (card recommendations
  adopted via the card OK). See observation O-2.
- Change boundary: everything in the range is inside the plan's declared surface; the OUT
  list holds — the ledger's citation rule is not incorporated (the `E10` blob-id clause
  is L-2r's read-record property, a different rule), no tooling, no frozen byte, no
  contract stub edit.
- `R8`: pure-text round, zero guard code changed — nothing to mutation-test; the suites'
  binding force is prior rounds' property and is not re-certified here (`R4`).

## 6. Findings

### Low

**L-1 — three layer members still enumerate the review side as "R1–R9" after R10
landed.** `document-harness/README.md:26` ("E1–E12 execution, R1–R9 review"),
`v3-harness-operating-contract.md:3` and `v3-harness-review-contract.md:3` (both "E1–E12
execution, R1–R9 review" / "R1–R9 review, E1–E12 execution"). Precedent says this
propagation belongs to the amendment: when R9 entered at `377d591`, README was corrected
at `cf040af` and both stubs `R1–R8`→`R1–R9` (recorded in `v3-checkpoint-read-ff05ea3.md:46,51`).
No decision goes wrong — all three sites direct the reader into the checklist itself,
which carries R10, and the locked README oracle asserts nothing about that row — so this
is not a blocker and must not burn the repair. **Exact bytes supplied:** at each of the
three sites, `R1–R9` → `R1–R10`. Under the just-landed byte-supplied-low channel this is
immediately appliable by the executor; the three edits are layer applications and owe
their ride-along read — the round's own closing read (plan Step 9) is still pending, so
applying before that dispatch lets the read cover the final bytes at no extra cost.

**L-2 — E10-d's fix closes the routing, not the named clause's letter.** The rider named
the deferral clause (延后条款): *"an amendment that adds no new clause to any rule and
whose effect on every round in flight is nil may be relied upon before its read"*. The
landed fix extends the **design test** ("…or replacing or deleting text so that what a
rule requires changes, is design and opens a round"), which takes rule-changing
replacements/deletions out of the amendment channel entirely — so the loophole has no
practical path left. The residue: the deferral clause's own precondition still says only
"adds no new clause", a rule-changing deletion still passes its letter, and the new
collision rule names the free channel only, not the deferral clause. No downstream
decision goes wrong (the design clause opens the round unambiguously either way):
wording-level under `R9`, rides the next batch touching `E10`. Recorded so the next
`E10` batch knows the seam is one clause earlier than the fix that closed it.

### Observations (`R5` — reported, the conclusions are the user's)

**O-1 — the extended kind vocabulary covers the four attested instances, and this round
minted six commits whose self-named kinds are still off-list.** "Bookkeeping commit",
"Bank-maintenance commit", "preclear reconcile" appear in the range; the new list adds
amendment / ruling / record. If `E8` is read to govern ledger/plan-only commits, O-6's
gap is narrowed, not closed; if those commits are outside `E8`'s scope (they touch no
code, schema or instruction file), the list is complete for its scope. Attribution cost
in this range was zero — every commit names itself plainly. Which reading governs is the
user's call.

**O-2 — two of the three rulings ran through a bulk card OK.** E2-s2 (expanding the
frozen surface) and the O-6 vocabulary were card recommendations adopted by "ok开工",
not separately voiced; only the no-split ruling was explicit. The journal records the
distinction honestly, and `E11` is satisfied on its face. Noted because one of the two
bulk-adopted decisions grows `E2` — a surface where the harness elsewhere insists on
per-item explicitness — and the record channel, not the decision, is what a future
reader will interrogate.

**O-3 — `E10` grew again, by roughly a third of its former clause count, in the same
round that closed O-1 with a no-split ruling.** The user asked what splitting would
involve and ruled with the answer in hand, so the R5 question is adjudicated, not open;
recorded only as continuity of the shape af2905c O-1 first reported, for whenever the
next growth round arrives.

## 7. Disclosure (`R4`)

- **Read in full:** the range's seven commit bodies; `CONSTRUCTION-CHECKLIST.md` (pre-
  and post-amendment); the candidate's full diff; `HARNESS-RIDERS.md` at `c61d82d`,
  `0a3d18d` and HEAD; `harness-layer-incorporation-round.plan.md`; the round journal;
  `HARNESS-LEDGER.md`; both contract stubs.
- **Sampled at the cited lines:** `v3-review-full-8ec4c60.md`, `v3-checkpoint-read-d58969d.md`,
  `v3-cold-read-451e8b0.md`, `v3-review-verify-f054a08.md`, `v3-review-full-af2905c.md`,
  `v3-checkpoint-read-dcced4e.md`, `v3-checkpoint-read-403fc9a.md`,
  `v3-cold-read-ae4df09.md` §1, `v3-checkpoint-read-ff05ea3.md`, `a6b87ad` and `11d147e`
  bodies/diffs, `issues.py:155-205`, `layer_path_check.py:28-42`, `8ec4c60`'s ledger diff.
- **Probed only:** `test_readme_enumeration.py` (asserts schema-file naming only),
  `run_tests.py` headers, `.harness/review-pending.json`.
- **Re-derived by command:** the five suites, repo-audit, four frozen blobs, schema/
  contract porcelain, oracle diffs, the eight-member blob table, member-set staleness,
  pack counts (14/14, zero diff), rider row counts (19 → 8), the recovered VB-1 ledger line.
- **Marked, not verified:** my own dispatch independence (the prompt set only the
  subject; `R1` satisfied on its face), the card render and the user's chat replies
  (accepted as the journal records them), staging method, no-amend.
- **UNVERIFIABLE:** nothing material to the verdict.

## 8. Verdict

**`REVIEWED_NO_BLOCKER`.** The nine edits do what their sources asked, the migration is
deletions-and-stitching with every departure disclosed, the redemption discipline held,
the figures reproduce, and the frozen surface is intact. The two lows do not oblige the
fix leg: L-1 carries its own bytes for the free channel, L-2 is wording-level under `R9`.
Under R10 the bank-or-spend choice on each goes to the user before closeout.
