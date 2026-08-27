# Contract v4 signature record

Per the contract's own *Signature semantics* block and §14 — the signature record lives outside
the file it signs — the user signed **`Document-Work-Assurance-Contract-v4.md`** on
**2026-08-23**, at the close of round `CONTRACT-V4`, after stating that the whole text had been
read.

- **Exact blob signed:** `614932de40b841ec9777719aea88de04864eb67b` — **339 lines**, sha256 of
  the blob content (LF; `git cat-file blob <id> | sha256sum`, the caliber `HD-40` fixed)
  `1b1061cbdeb6585ee5b33f3dcf91c2ee376f60f3e92076998d7930b70f7a23fa`.
- **The contract's current blob is not the signed blob, and that is not drift.** `HD-57`'s
  recorded ruling of 2026-08-23 corrected five stale literals in the file after signing, and
  round `CORE-SET-SIGNATURE` (2026-08-26) rewrote eight pointer sites under `HD-60` and `HD-61`.
  Both wrote under `E2`'s "obtain the ruling and write under it" clause. What a signature binds
  is the blob above; what `E2`'s frozen-byte list names is the *current* blob, so the two
  literals differ by construction and each is checked against its own source.
  - **Corrected forward 2026-08-28, batch `FREEZE-TO-ALARM` — the sentences above are left
    standing verbatim (`HD-59`) and this paragraph is the correction.** Item A of that batch
    (`184387c`, 2026-08-27, carrying the user's rulings of 2026-08-27) rewrote `E2` from a gate
    into an announcement, and two of the claims above did not survive it. **`E2` now pins no blob
    hash at all** — its own text says so, and the signed blob's carrier is this file — so there
    are not *two* literals to differ by construction; there is one, the signed one recorded
    above, and nothing in `E2` to check the current blob against. **`E2`'s "obtain the ruling and
    write under it" clause no longer exists**, having gone with the gate it served, so the
    sentence naming it reads as history only: both post-signature writes did go through that
    clause under the regime then in force, and the clause itself is now findable in this
    repository's history rather than in `document-harness/CONSTRUCTION-CHECKLIST.md`. What the
    current blob is, is recovered from the commit record instead: since item A, a write to
    `contract/Document-Work-Assurance-Contract-v4.md` is owed disclosure after the fact, the
    commit that writes it naming that path site by site in its own body. **Unaffected, and
    deliberately untouched here:** the blob this signature binds, and what the signature means
    (§14) — item A changed the rule about writing those bytes, not what was signed or what
    signing them did.
- **What the signature means** (contract §14): the interfaces, enums, invariants, version
  boundaries and dependency map are frozen as the operative text for v3-family construction, and
  this file supersedes the v3 contract and its two supersessions as one operative document.
- **Review chain:** a FULL over subject `5f849da` returned `CHANGES_REQUIRED` (its record landed
  at `28852a6`, the id `HD-56` cites) → one user-approved fix `d0f185c` → VERIFY
  `REVIEWED_NO_BLOCKER`. Records `v3-review-full-5f849da.md` and `v3-review-verify-d0f185c.md`,
  held by this instrument's own construction record and not by a repository that runs against it.
- **Merged sources, retired into git history 2026-08-23** and immutable there per `HD-44`:
  v3 `b2dbdf752d8c155e4c65b14b5f420b880b8184a1` (signed 2026-07-20) · supersession 1
  `68031fa2ca31272e31da0d42a9a02189d28fcc21` (signed 2026-07-24) · supersession 2
  `e1a2f26b1d8d323d11e900f8137dea222b6571c1` (signed 2026-07-30).

## Why this file exists, and what it succeeds

This contract family's signature has had four carriers, none of which re-signed on the move: the
N0 record §8 (v3) · the W2 record (supersession 1) · `supersession-2-signature.md`
(supersession 2) · `HD-56` in the decision log (v4). This file is the fifth, and moving a
carrier preserves the signature — the signed bytes above are unchanged by it (user ruling
2026-08-25, batch `CORE-SET` ruling 10; v4 is **not** re-signed).

**It succeeds `HD-56`**, which is `superseded` and archived as of the commit that created this
file, with the pointer written in both directions (`HD-30` full-text succession, `HD-2`
state flip in the same commit). The reason for the move is user ruling 2026-08-25, batch
`CORE-SET` ruling 5: contract v4 travels to every repository that mounts this instrument, and
the decision log does not, so a signed product-tier document pointed at a register a caller
never receives. The write authorisation is `HD-60`.

**What did not move with it.** `HD-56` carried two further rulings, and neither is re-decided
here: v4's admission as the ninth instruction-layer member, whose carrier is `E10`'s own
membership sentence in `document-harness/CONSTRUCTION-CHECKLIST.md`; and the retirement of the
contract entry in `governance-exemptions.json`, already done and citing `HD-56` from that file's
retired block. Both stay findable in the archived entry.

## Is this an instruction-layer member? No — the `HD-21` question, asked and answered

`E10`'s membership sentence names nine paths and does not name this one, and this file claims
authority over no rule: it records a signature that already happened and states which bytes it
binds. Every rule about what the signed text *requires* belongs to the contract. `E10-sync` does
not fall due — the membership sentence is untouched.

**Which side it sits on.** The construction side: this instrument's own governance record, like
the four carriers before it, and listed as such in `CONSTRUCTION-INDEX.md`. A caller does not
carry this file, which is why the contract and `document-harness/README.md` **name** it rather
than link it.
