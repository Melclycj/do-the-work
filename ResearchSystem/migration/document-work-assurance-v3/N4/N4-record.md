# V3-N4 administrative record — conditional administrative cutover

Node: `V3-N4` of [[document-work-assurance-harness-v3.plan|the v3 plan]] §9. Sole writer: the
execution session. Section roles: **§7 is the append-only log; §§1–6 record this node's own
facts** and are not rewritten once the node closes.

## 1. Entry and authorization (plan §9, V3-N4)

- **Entry condition met:** the user ruled `ADOPT_DOCUMENT_V3` at the V3-N3 decision gate on
  2026-07-21 (N3 record §8; closeout `0b67d3b`).
- **N4 authorized separately by the user on 2026-07-21** ("签字N4 开始") — the adoption ruling
  did not itself authorize execution, matching every prior node.
- **Gate (plan §9):** deterministic administrative verification, then **the user confirms
  cutover**; no additional FULL review. An external checkpoint read of the candidate's
  instruction-layer changes is run as *extra discipline* (the standing rule attached to
  adoption), not as a new gate.

## 2. Change boundary actually used

Derived fresh from plan §9 V3-N4 before any write:

| Path | Basis | Used |
|---|---|---|
| `ResearchSystem/tooling/rsc.py` — document-work default only | allowlist | yes — docstring `v3` mode entry, the registration comment, the `v3` subparser help. No behavior change: declarations only |
| `ResearchSystem/document-harness/{README,EXECUTION,REVIEW}.md` | allowlist | yes — the C1/C2/C3 batch (§4) |
| `ResearchSystem/README.md` — document-harness link only | allowlist | yes — one link line added (none existed) |
| this plan + `.goals/LEDGER.md` — pointer/status only | allowlist | **LEDGER yes** (live pointer + push debt; also carries the review-side drift repair that waited for this boundary per the committed handoff note §1). **The plan file deliberately NOT touched** — see §5 |
| v2 plan historical banner | allowlist | not needed — banner landed at v3 plan approval, verified still present |
| `ResearchSystem/migration/document-work-assurance-v3/N4/**` | allowed new root | this record |

## 3. The cutover itself

**The default pointer is text, by design** (plan §11: *"N4 changes only the document-work
entry/pointer. Rollback restores that pointer."*):

1. `rsc.py` module docstring: the `v3` mode is declared **the default assurance entry for
   document work** — entry `rsc v3 status --state <AssuranceWorkState>` (byte-verifies the
   WorkSpec / ResolvedAssurancePlan / evidence pointers via `assurance_state.resume`,
   N1-A10); fixed role instructions named as `document-harness/{EXECUTION,REVIEW}.md`.
2. The `v3` registration comment and subparser help updated to the same declaration; the
   pre-existing seam text (*"The v3 default entry is a V3-N4 decision and is not taken
   here"*) is replaced by the taken decision.
3. `ResearchSystem/README.md`: one line linking `document-harness/` as the default document
   work assurance entry.

**Scope (N4-A1):** document-work consumers only. v1 `stage ...` remains the Stage Record
runtime; the v2 harness remains side-by-side read-only; P4 and every business run remain
separately authorized (N4-A5, `P4-IMPL-v1` still `approved / effective=false`).

**One entry (N4-A2):** `rsc v3 status` reads the `AssuranceWorkState` and byte-verifies its
`work_spec_ref` / `resolved_plan_ref` / evidence pointer set; the fixed role instructions are
named at the entry's own declaration. Verified live against round-3 state:
`rsc v3 status --state …/round-3/run-a1/control/state.json` → `resumable (exit 0)`.

## 4. The C1/C2/C3 instruction-prose batch

Per the committed custody note ([`v3-review-note-instruction-layer-custody.md`](../v3-review-note-instruction-layer-custody.md))
and its user-approved routing (N3 record §8) — batched here because N4's allowlist holds
exactly their landing files; no fourth ad-hoc out-of-node amendment:

- **C1 (subtractive):** `document-harness/README.md`'s hand-written status banner deleted
  (it was three nodes stale and self-contradicting). Replaced by the ownership statement:
  node state lives only in node records. The structural link table stays.
- **C2 (subtractive):** the same README's duplicate of the N0 §8 errata (the contract
  frontmatter `status:` explanation) deleted; the row now points at the record. The signed
  contract itself untouched, as the note requires.
- **C3 (additive):** one stage-marker paragraph in `EXECUTION.md` §*When the instruction
  itself is the problem* (execution-time rule) and one in `REVIEW.md` §*When the map is
  incomplete* (post-hoc recheck rule), each naming the other two stages (pre-START audit =
  contract §6). No rule content changed — the markers only carry the stage qualifier that
  no file carried.

## 5. Deliberate non-implementations

| Not done | Why not |
|---|---|
| plan-file status update (allowlisted) | The approved plan blob `8ad404b1…` has been re-verified unchanged at every commit this round; keeping it byte-identical is worth more than a status line. Plan state is carried by the LEDGER and the node records. If a later reader trips over this, the allowlist permits a successor node to take the edit |
| `ResearchSystem/README.md` staleness beyond the link ("Current phase: P1 done" is three phases stale — C1-class drift in another file) | Outside the N4 allowlist ("document-harness link only"). Observed and recorded here; belongs to the ResearchSystem P-track's own maintenance |
| any test/tooling/schema change | Nothing in this node touches behavior; the five suites are re-run to show nothing broke |

## 6. Deterministic results (N4-A6) and the rollback test (N4-A4)

**Rollback test, performed before commit** (never `git checkout --`; byte-checked
patch restore):

| Step | Result |
|---|---|
| pointer diff saved (`rsc.py` + `ResearchSystem/README.md`) + sha256 of both files recorded | done |
| entry with pointer applied | `rsc v3 status` on round-3 run-a1 state → **resumable (exit 0)** |
| `git apply -R` (pointer rolled back) | `rsc v3 --help` shows pre-cutover text; **`rsc v3 status` still fully functional** — rollback removes only the default declaration, breaks nothing |
| `git apply` (restored) + `sha256sum -c` | **OK on both files** — byte-identical restore |

**Exact rollback procedure, recorded per N4-A4:** reverse-apply the cutover commit's diff to
`ResearchSystem/tooling/rsc.py` + `ResearchSystem/README.md` (and, if desired, the
document-harness README/role-file hunks). v1/v2 remain recoverable history throughout
(N4-A3) — no old root was touched.

**Suites and audit** (measured immediately before the candidate commit; figures last):
V3-N1 113 · V3-N2 203 · harness 39 · stage-control 20 · compiler 29 — all OK;
`repo-audit.py` exit 0; changed-path set verified ⊆ the §2 allowlist.

**External checkpoint read** of the candidate's instruction-layer diff: see §7.

## 7. Append-only log

- 2026-07-21 — node opened on explicit user authorization following the `ADOPT_DOCUMENT_V3`
  ruling. Boundary derived from plan §9 before any write (§2). Cutover pointer, C1/C2/C3
  batch, LEDGER sync and the rollback test executed as recorded above.
- 2026-07-21 — **external checkpoint read of the candidate's diff returned clean on all five
  questions** (no behavior change — verified down to `ast.parse` and live `--help`; stage
  markers correct against contract §6 and both rule bodies; no new C1/C2/C3-class defect; no
  scope creep; no contamination wording) **plus four LOW/NOTE findings — three applied
  before commit, one recorded**: F1 the REVIEW.md marker restated EXECUTION.md's rule
  mechanism (a fresh C5-class seed) → reduced to a pointer; F2 the README replacement baked
  a quantified historical characterization into a permanent index file → trimmed to the
  governance principle; F3 "authoring or working the WorkSpec" overstated the executor's
  stage → "working against the WorkSpec"; F4 (no action) the cutover declaration appears on
  four surfaces — the cheap fixed-sentence kind, rollback fully enumerated in §6. The
  checkpoint-read discipline attached to adoption caught a C5 seed in the very commit that
  fixes C1–C3, which is the discipline earning its keep. Candidate committed as `1e6dde9`;
  **cutover awaits the user's confirmation** (plan §9 N4 gate).
- 2026-07-21 — **the user confirmed the cutover ("确认 cutover"). V3-N4 CLOSES, and with it
  the v3 migration (N0 → N4) is complete.** v3 is the default assurance entry for document
  work; the exact rollback is §6's reverse-patch procedure. Nothing further is open on any
  v3 node. The queue handed back to the user, both gates theirs: (1) the harness-contract
  discipline edit (per-amendment checkpoint reads / node-boundary cold reads / no rewrites);
  (2) the 特例-bucket design round (`review_only` incentive + obligations-declare-evidence +
  commit-first successor — versioned-successor territory, N3-R9/R10 and the two committed
  review-side notes are its inputs). This record is sealed; §§1–6 are final.
