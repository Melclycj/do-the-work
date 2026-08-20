# Supersession-2 signature record

Per the carrier's own §5 — the signature record lives outside the file — the user signed
**`Document-Work-Assurance-Contract-v3-supersession-2.md`** on **2026-07-30**.

- **Exact blob signed:** `e1a2f26b1d8d323d11e900f8137dea222b6571c1` — the post-repair state
  carrying the `a7d7121` S2-1 citation widening and the `451e8b0` L-1 boundary-sentence fix,
  both applied in the commit that introduces this record (derive it:
  `git log --format=%H -1 -- <this file's path>`).
- **User words (chat, 2026-07-30):** "supersession-2 签字，但是确保这些历史决策记录和
  contract v3 不要放一起，污染执行。"
- **The condition, and how it is met:** reading-level separation, same commit — the
  document-harness README's authoritative table states this signature, and a companion row
  names everything else in `ResearchSystem/contract/` as either v1/v2 historical-only
  (N0 record §3) or the P0–P14 track's instruments, none of it v3 law. Physical relocation
  of the v1/v2 contracts is the version-quarantine item already in the ledger backlog
  (guarantee-surface session).
- **Effect (carrier §5):** this one supersession and its §3 version boundary govern
  successor runs. `E2`'s frozen-byte list is unchanged by signing; whether the signed blob
  joins it rides `HARNESS-RIDERS.md` row `E2-s2`.
- The carrier's own top-of-file UNSIGNED lines are a residue of the pre-signature state:
  correcting them was in boundary before the blob was cut and was not done; once signed,
  the contract's §13 rule — signed text is never amended in place — bars the in-place fix,
  so this record and the README row state the signature. (Ground corrected per
  `v3-checkpoint-read-403fc9a.md` L-1: the earlier "§5 design" citation was wrong — §5 bars
  the record from living in the carrier, not the status line from being corrected.)
