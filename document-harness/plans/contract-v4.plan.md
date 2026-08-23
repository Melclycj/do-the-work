# Plan — round `CONTRACT-V4` (publicization batch B: the re-signing / packaging batch)

> **Status: open.** Written 2026-08-23 at round open, after the opening layer read
> (`v3-cold-read-b8df15a.md`: 0 must-fix / 1 low / 5 observations; the member reads owed
> since `PRERUN-RIDERS` are paid by it; its `L-1` banks as rider `read-name-split` in this
> plan's commit). This file is the carrier of the **four user rulings of 2026-08-23 (batch
> B)** below until the round records them. Queue: batch B is the queue head the batch-A
> closeout named; the `split-design.md` §10.5 parked items are raised and routed by ruling 4.
>
> **Role form.** As in round `PUB-FACADE`: orchestrator and executor are one session
> (`E1`'s exception channel; all four `R1` holdings held over the candidate, stated in the
> candidate commit body, nothing about its authoring independent). Independent legs: the
> opening read above, one FULL, one targeted VERIFY (`E9` intact — a fix needs the user's
> approval). The user's own leg is new to this round: **reading contract v4 in full and
> signing it**; the signature is a recorded ruling in `HARNESS-DECISIONS.md` binding the
> exact blob, and until it lands v4 is candidate text, not a contract.

## The four user rulings of 2026-08-23 (batch B; this file is their carrier)

1. **Process weight: opening read + FULL + VERIFY** (the read landed before this plan).
2. **v4 bundles the `wspec-owner` §3 correction** — the `DocumentWorkSpec` row's sole-owner
   label aligns with the three-role model (`HD-35`): the WorkSpec author is the run's
   executor. The two schema-title sites of that rider stay banked (`E2` pack, untouched).
3. **The card's authorization ruling**: this round may touch the `E2` freeze surface —
   retiring the two supersession files into git history and re-pointing the freeze list —
   with v4's *effectiveness* still gated on the signature.
4. **`split-design.md` §10.5's two parked items are raised and deferred**: distribution
   form (submodule vs plugin install) and whether `.claude/` carries harness pieces are
   **recorded in the ledger for batch C or their own round, not designed here**.

## Why this round

The operative contract is a three-file puzzle: a 255-line signed base whose frontmatter
still says `candidate-awaiting-user-signature`, plus two successor files whose headers say
UNSIGNED, holding five statement supersessions among five path tokens that no longer
resolve (rider `frozen-path-prefix`). A stranger opening `contract/` meets exactly the
wrong first minute. Batch B merges the three into one signed v4, retires the residue, and
re-signs the two design documents whose banked stale sentences (`six-signed`,
`design-route`, `io-hiroute-stale`) were all waiting for this batch by name.

## The delta enumeration (authoritative; the FULL verifies the candidate against it)

v4 = the frozen v3 text, byte-faithful except at exactly these sites:

| # | site | change | authority |
|---|---|---|---|
| D1 | frontmatter | drop `status:` and `document_role:` (self-approval residue); keep title/tags/created (created = 2026-08-23); `signature_owner:` re-pointed to the decision log | governance-scan rule; N0 §8 errata called the old field authoring residue |
| D2 | header warning block | signature semantics re-pointed: record lives as an `HD` entry in `HARNESS-DECISIONS.md` binding the exact blob; lineage sentence names v3 + s1 + s2 and their blobs as the merged sources, all reachable in git history | v3 §13 (successor rule); `HD-2` |
| D3 | §3 table, `DocumentWorkSpec` row | owner cell `stage author / planning agent` → `the run's executor (its WorkSpec author)` | ruling 2; `HD-35` |
| D4 | §4 diagram line | s1 S1 successor text verbatim | s1 (user-adjudicated 2026-07-23) |
| D5 | §7 invariant 9 | s1 S2 successor text verbatim | s1 |
| D6 | §7 invariant 11 | s1 S3 successor text verbatim | s1 |
| D7 | §8 step 7 | s1 S4 successor text verbatim | s1 |
| D8 | §13, new subsection «Review-subject version boundary» | s1 §3 absorbed (schema_version keying, no cross-version fallback, pinned v1 history) with its final bullet replaced by s2's successor text (digest-protected fields, pointer_for, authoring-call boundary from s2 §3), plus s1 §4's digest-strength disclosure (SHA-1 content addressing, stated not glossed) and s2 §4's four honesty notes | s1 §3-4 · s2 §2-4 |
| D9 | absorbed-text path fixes | s2's `assurance/runs/` token → named artifact + holder (closed-run scripts, held in the caller's run directories); s2's `templates/run-v2/` → `assurance/templates/run-v2/` (spelling class). The three stale-prefix tokens (s1:7, s1:123, s2:110) die with the unabsorbed signature/authorization headers | rider `frozen-path-prefix`'s three-class split |
| D10 | §14 signature section | rewritten for v4: signature = `HD` entry with blob + date; what signing means (interfaces/enums/invariants/version boundaries frozen; v4 supersedes v3+s1+s2 as the operative text) | v3 §14 shape |

Everything else in v3 §1–§13 is copied unchanged; the FULL's job includes diffing the copy
against blob `b2dbdf75…` and confirming no unenumerated drift.

## Change surface beyond the v4 file

| surface | what changes |
|---|---|
| `contract/Document-Work-Assurance-Contract-v3{,-supersession-1,-supersession-2}.md` | **Retired: deleted from the tree, reachable at their recorded blobs in history** (`b2dbdf75…` / `68031fa2…` / `e1a2f26b…`), the same shape v1/v2 already have — they live in the caller's history, not this tree. **Sub-decision flagged for the signing checkpoint**: keeping v3 in-tree beside v4 is the alternative; it costs the frontmatter contradiction and the exemption entry staying alive. Recommended: retire all three. |
| `document-harness/CONSTRUCTION-CHECKLIST.md` (`E10` member) | Membership sentence: the two supersessions leave; ten → **eight**. `E2` clause: freeze list re-pointed — v4 blob (+ v3/s1/s2 named as history-frozen at their blobs) + the fifteen-file pack unchanged. Design edits inside an open round; the members' independent reads ride the next opening read. |
| `tooling/hooks/layer_path_check.py` + `tooling/tests/document_harness/test_precommit_checks.py` | `LAYER` / `EXPECTED` drop the two paths — the `E10-sync` three-site same-commit obligation, named in the commit body, prose legs swept per the rider (ten-member mentions in `.githooks/pre-commit`, root `README.md`, `document-harness/README.md`, `document-harness/ONBOARDING.md`). |
| `tooling/rsclib/document_harness/__init__.py:41` + `tooling/tests/document_harness/test_candidate_checks.py:1721` | `CONTRACT_PATH` → the v4 file; the R4 governance scan now passes the operative contract on merit (no status field), and the test's expectations move accordingly. |
| `migration/document-work-assurance-v3/N1/governance-exemptions.json` | The contract entry (blob `b2dbdf75…`) deleted — nothing in the tree carries that blob any more; the plan entry stays. |
| `document-harness/split-design.md` (signed `HD-40`) | De-rust for re-signing: §1's 「六命令原样」 gains the two-later-commands reality (`HD-47`/`HD-51`); §2's EXCLUDE proposal gains the one-line road-not-taken marker (R3 implemented a path-style constant instead). Riders `six-signed` (half) + `design-route` redeem. |
| `document-harness/io-design.md` (signed `HD-35`) | De-rust for re-signing: :115's 「六个命令中五个纯读」 recounted against the present command set; :99-100's dangling `HI-route` pointer replaced by the codified route (`REVIEW.md`, observation findings; closed 2026-08-22). Riders `six-signed` (half) + `io-hiroute-stale` redeem. |
| Other live references | `assurance/templates/run-v2/README.md` and `E10` members (`EXECUTION.md` / `REVIEW.md` / `document-harness/README.md`) that name the contract or supersessions re-pointed to v4; enumerated by grep at fix time, scan pasted. |
| `HARNESS-RIDERS.md` | Delete `frozen-path-prefix`, `design-route`, `io-hiroute-stale`, `six-signed` in the same commit as their fixes; rewrite `wspec-owner` (contract site fixed; two frozen schema-title sites remain, `E2`-gated); add `read-name-split` (this plan's commit, from the opening read's `L-1`). |
| `HARNESS-DECISIONS.md` | At signature only: the v4 signature entry (new `HD`), `HD-35` re-sign note for io-design, `HD-40` re-sign note for split-design — orchestrator-written at the signing checkpoint, blob-bound. |
| `CONSTRUCTION-LEDGER.md` | At closeout only (+ ruling 4's two parked items recorded under batch C). |

**Out of boundary, deliberately:** the fifteen-file schema pack (`hi-schema-gloss` and the
two schema-title halves of `wspec-owner` stay banked — no pack ruling is asked for here);
`EXECUTION.md:364`'s bare `python` (rider `py-convention`, its own surface); the `.claude/`
and plugin questions (ruling 4); batch C entire; any push.

## Sequence and gates

1. Plan commit (this file + rider row) — done at `V3-CONTRACT-V4-PLAN-v1`.
2. Candidate: everything above except the `HARNESS-DECISIONS.md` signature entries.
3. Independent FULL against this delta enumeration → record commit.
4. Any fix: user-approved, once (`E9`), then targeted VERIFY.
5. **Signing checkpoint (the user's leg):** the user reads v4 in full with the delta table
   as guide, answers the retire-v3-in-tree sub-decision, and signs; the orchestrator writes
   the signature `HD` entry binding the final blob. No signature → v4 stays candidate text
   and the round stops there, disclosed.
6. Closeout: ledger, rider accounting, plan status flip.

## Opening conditions, measured 2026-08-23

- Opening read `v3-cold-read-b8df15a.md`: 0 must-fix; battery **793 passed** re-derived at
  `b8df15a`; `E2` surface = 3 named blobs + exactly 15 pack files; membership sentence ==
  guard `LAYER`; 0 unresolved path tokens outside the frozen supersessions.
- `HARNESS-DECISIONS.md` `§live` read this session (blob unchanged since `860729f`).
- `E9` budget: one FULL, at most one user-approved fix, one targeted VERIFY.
- Disciplines: `E8` (dense body, no trailers, kind named); `HD-41` (scope before assertion;
  fix legs paste **raw** grep output — rider `fixleg-scan-raw` is redeemed by exactly that);
  `HD-5` (one home, others point); `E10-sync` (three machine sites + prose legs, one commit,
  named in its body).
