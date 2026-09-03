# Contract v4 signature record

## ⚠ Signature SUSPENDED — 2026-09-04 (revision period; re-signature owed)

**The user suspended v4's signature on 2026-09-04**, for a period of active contract revision,
and it has not been re-signed since. This register is the authority on the contract's
signed-status (the contract's own *Signature semantics* block and §14 delegate it here — the
file "never carries its own approval status"), so while this section stands, **v4 is a draft
under revision, not a signed contract.**

- **What it lifts.** §13's clause "Signed contracts are never amended in place; corrections
  create a versioned successor" keys on the contract being **signed**. A draft is not, so that
  clause does not bind during suspension: the contract may be edited in place, and no
  per-edit ruling (the `HD-63`/`64`/`67`/`68`/`70` family, all retired 2026-09-04) is needed.
- **What it does NOT lift.** The contract is still an `E2` announced path — a write to it is
  disclosed after the fact, site by site, in the commit body — and still an `E10` instruction-
  layer member, so an edit still owes `E10`'s independent re-read; a factual correction that
  adds no clause and changes no requirement takes `E10`'s free channel (relied on at once, the
  re-read riding the next layer read), and only a requirement-changing edit opens a round. That
  is the whole of what makes a contract edit cost anything now.
- **What was signed is preserved, not erased.** The blob recorded below (`614932de…`) remains
  the record of what the 2026-08-23 signature bound; suspension is a status change, not a
  deletion of that fact.
- **Re-enable (owed before stability is declared).** Add a re-signature entry here: the new
  blob's id and sha256, the date, and a statement that the whole text was read. §13 binds again
  the moment this section is replaced by that entry.
- **Why this is not a decision-log ruling.** Suspending and re-signing are the signer's own
  authorization events, recorded where signing status lives (here), not design-layer rulings —
  consistent with the 2026-08-21 ruling that an in-repo "the user approved" is an authorization
  fact, not a decision-log entry, and that no approval-carrier machine is built for it.

---

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
  - **Third post-signature write, 2026-08-28 — the `V1-RESULT-RETIRE` `M-1` amendment, this
    commit.** §13.1's promise that `review.schema.json` and the v1 checker functions stay frozen
    for reading pinned v1 history was false in its checker half from `56d1b17` and would have gone
    false in the other; the promise is gone and the bullet says what replaced it. `HD-63`
    authorises the in-place correction and is the first authorisation in this family to state that
    it overrides §13's "signed contracts are never amended in place" — the two writes above did
    the same thing without saying so, which that entry records as measured rather than recalled.
    The signed blob above is unchanged and v4 is not re-signed; `E2`'s disclosure rides the
    amendment commit's own body, as for the two before it.
  - **Fourth post-signature write, 2026-08-28 — the `V1-RESULT-RETIRE` second amendment, this
    commit.** §13.1's first bullet required a result with no `schema_version` key to be
    validated against pinned v1 semantics; the same round removes the only path that did so,
    and the user's ruling that no v1 ReviewResult instance exists anywhere leaves the
    requirement with nothing to act on. The bullet now prescribes no validation path for that
    result and keeps it fail-closed. `HD-64` authorises it and is the first authorisation in
    this family to reach a statement of what the contract **requires** — `HD-63`, one write
    above, reaches only statements of fact and its boundary paragraph excludes this class — so
    the two are separate rulings rather than one applied twice. `HD-64` also rules that this
    correction opens no design round, which `E10`'s design test would otherwise require; that
    set-aside is recorded in the entry as a cost, and it is greppable there rather than
    inferable from this file. The signed blob above is unchanged and v4 is not re-signed.
  - **Fifth post-signature write, 2026-08-30 — round `CORE-ONLY-LAYER`'s contract commit, this
    commit.** `HD-67` authorises the in-place removal of two blocks of pure construction history
    from contract v4 — the merged-sources paragraph in the header and `§12`'s first two
    paragraphs — on the ground that a product contract carrying this instrument's construction
    history is pollution of the rule text, and it is the third authorisation in this family to
    say in as many words that it overrides `§13`'s "signed contracts are never amended in
    place". The three do not collapse into one: `HD-63` reached a signed statement of fact made
    false elsewhere, `HD-64` a requirement acting on nothing, and this one reaches history a
    repository running against the contract cannot reach at all. The signed blob above is
    unchanged and v4 is **not** re-signed — `HD-67` takes plan ruling 11's light route, and that
    entry's own forward correction records that ruling 11's literal instruction, re-point the
    signature at the new blob, has had no object since `184387c`.
    **What this write did with this file's own name.** The contract named it at three sites, one
    more than `HD-67`'s census counted, which the round's opening read found and the user ruled
    on the same day: `:9`'s `signature_owner` front-matter key stays exactly as it was, being
    machine-read and pinned by a test; the two prose sites dropped the filename for a holder
    clause, because this file does not travel and a repository running against the contract
    cannot follow a name it does not hold. After this write the contract names this file once,
    at `:9`.
    **Rider `sig-write-once` is redeemed here, on its second arm.** That row records that the
    *Signature semantics* block replaced "recorded **append-only** as an `HD` entry" with
    "recorded, **write-once and after review**" and that the property which dropped out was
    never accounted for. The account is this, and it is the arm that records rather than
    restores: **write-once names the signature, not this record.** One blob is signed once and
    never re-pointed; this file is and stays **append-only**, which is visible in its own shape —
    five post-signature blocks now stand under the signed blob, every one appended and none
    rewritten — and what governs a correction to any of them is `HD-59`, correct forward and
    leave the original standing word for word. A sixth carrier file is what the property's
    absence invited, and it is exactly the add-a-component shape that ruling refuses.
    **Two statements in this file go stale with this round and are corrected forward here rather
    than in place (`HD-59`); both are left standing above and below word for word.** The section
    *What did not move with it* says v4's admission as the ninth instruction-layer member has its
    carrier in `E10`'s membership sentence "in `document-harness/CONSTRUCTION-CHECKLIST.md`":
    round `CORE-ONLY-LAYER` split that file and the sentence now lives in
    `document-harness/RULES.md`, still naming contract v4, so the membership is unchanged and
    only the address moved. The section *Is this an instruction-layer member?* says "`E10-sync`
    does not fall due — the membership sentence is untouched", which was true of the commit that
    wrote it: this round touches that sentence, `E10-sync` did fall due, and it was discharged in
    the round's rule-split commit with all three mirrors changed together. Unaffected and
    deliberately untouched: the blob this signature binds, what the signature means, and this
    file's own answer that it is not a member.
  - **Sixth post-signature write, 2026-08-30 — round `CORE-ONLY-LAYER`'s corrections commit, this
    commit.** Two sites, each with its own authorisation, and neither of them the same class as the
    five above. **§12's first paragraph is deleted entire** under the user's ruling of 2026-08-30
    (plan `document-harness/plans/core-only.plan.md` ruling 22, answering the round executor's
    first question): the fifth write kept that paragraph's two obligation sentences — v1/v2 material
    is immutable, and referencing a non-nominated old component is a `SPEC_GAP` — on the reading
    that removing an obligation is the irreversible direction, and reported the cost, that the
    surviving requirement named a set whose defining sentence had gone with the deleted history.
    The user ruled the other way and gave the ground: v4 depends on no v1/v2 component, so nothing
    about them is referenced and all of it goes; the ruling records that this was verified before
    it was taken, the contract's remaining v1/v2 mentions being §13's version-boundary statements
    about results and history rather than dependencies. `HD-67`'s named block therefore governs
    over an executor's reading of `HD-67`'s criterion, for this block. §12's *Removed from the v3
    default interface* paragraph stays, as `HD-67` and the ruling both require, and it is now the
    whole of §12. **The wikilink at `:29` ceases to be a link** under `HD-68`, the fourth
    authorisation in this family to say in as many words that it overrides §13's "signed contracts
    are never amended in place". What it reaches is neither a false statement nor a requirement nor
    unreachable history but a **reference form**: the plan is now named by its title and given no
    path and no link, the dead-digest parenthetical is deleted as the history it is, and the
    obligation sentence — plan §2's V3-D1–D10 are the locked design authority and a genuine
    conflict is a `SPEC_GAP` — is kept word for word. The signed blob above is unchanged and v4 is
    **not** re-signed; this write's `E2` disclosure rides its own commit body, naming
    `contract/Document-Work-Assurance-Contract-v4.md` site by site, and the changed text owes
    `E10`'s independent re-read, riding this round's next read of that layer.
    **Rider `contract-wikilink-tier` is redeemed and its row deleted in this same commit** (`R10`).
    That row had reached its redeem arm and its deadline in the round's earlier contract commit and
    could not be paid there for want of an authorisation; `HD-68` is that authorisation, and the row
    goes in the commit that spends it.
    **One statement in this file goes stale with this round and is corrected forward here rather
    than in place (`HD-59`); the original stands below word for word.** The closing sentence of
    *Which side it sits on* says a caller does not carry this file, "which is why the contract and
    `document-harness/README.md` **name** it rather than link it". As of this round the README does
    neither: plan ruling 24 deleted that name along with the other product-tier references to
    artifacts only this instrument holds, on the user's ground that a name replaced by a holder
    clause is not an improvement. What the contract does is what the fifth write recorded — it
    names this file once, at `:9`, machine-read and pinned by a test. So the sentence's reason
    survives and its enumeration does not: of the two carriers it named, one remains.
  - **Seventh post-signature write, 2026-08-30 — round `CORE-ONLY-LAYER`'s second corrections
    commit, this commit.** Two sites, one authorisation, and both of them the class `HD-63` already
    covers. **§12's heading now reads *Removed from the v3 default interface (plan §7)*** where it
    read *Dependency and historical map (plan §7)*: the sixth write deleted that section's first
    paragraph entire, so since that commit §12 has held its *Removed from the v3 default interface*
    paragraph and nothing else, and a heading naming a dependency map named something the section no
    longer contained. **§14's freeze list now reads *default-interface removals*** where it read
    *dependency map*, for the same reason and so that the list names what §12 actually holds; the
    other four items — interfaces, enums, invariants, version boundaries — are untouched, and so is
    the rest of the sentence. `HD-63` authorises both and no new entry opens: its class is a
    statement true at signing and made false by a later ruling or deletion elsewhere, its own
    boundary paragraph fixes the test as whether the sentence states a fact or imposes an
    obligation, and both sites state a fact about what this document contains. The user confirmed
    that reading and that the write happens now, on 2026-08-30 (plan
    `document-harness/plans/core-only.plan.md` ruling 25, answering the corrections pass's second
    question — that pass reported §12's heading and did not touch it, for want of an authorisation
    it could see). What the contract requires is unchanged, so `E10`'s design test does not fire and
    no round opens; and no valid independent FULL has occurred on this round's candidate, so under
    `E9` this is a pre-submission correction and consumes nothing. The signed blob above is
    unchanged and v4 is **not** re-signed; this write's `E2` disclosure rides its own commit body,
    naming `contract/Document-Work-Assurance-Contract-v4.md` site by site, and the changed text owes
    `E10`'s independent re-read, riding this round's next read of that layer.
    **One statement in this file goes stale with this write and is corrected forward here rather
    than in place (`HD-59`); the original stands below word for word.** The bullet *What the
    signature means* paraphrases §14's freeze list and so still says *dependency map*. What was
    signed is unchanged and that bullet records it correctly as of the signature; what it no longer
    reproduces is the contract's **current** §14, whose fifth item is now the default-interface
    removals. The set is the same either way — §12's surviving paragraph is what both names reach —
    and only the name of the fifth item differs between the signed text and the text in force.
  - **Eighth post-signature write, 2026-09-03 — round `PROMISE-PATH-VOCAB`'s vocabulary commit,
    this commit.** Two sites in §5, one authorisation each, and this is the first write in the
    `HD-63` family's line that makes the contract **require more** rather than correct or delete.
    **§5's VERIFY verdict row `:118` gains a third value**, `UNRESOLVED_BLOCKER`, meaning a
    blocking finding stands after the single permitted repair — the repair failed to close it, or
    created it — so that `SPEC_GAP` goes back to meaning only what §5 and §13 say it means, a
    defective specification owing a new WorkSpec and a new START. `HD-70` authorises exactly this
    row and this one value, expressly overriding §13's *Signed contracts are never amended in
    place*, and expressly refusing precedent for any other enum: the FULL row `:117` is untouched
    and the closed enums beside it are untouched. The engine borrowed `SPEC_GAP` for this outcome
    in a real run, which is the evidence the ruling was taken on. **§5's closing paragraph
    `:127-128` loses one ordinal**: *nonblocking uncertainty is never a fourth control verdict*
    now reads *never a control verdict*. With the union of the two rounds at four values the
    ordinal would have begun naming the new value, leaving the sentence true and empty instead of
    saying that disclosed uncertainty is not a verdict at all; no clause is added and no
    requirement changes. That deletion is the user's ruling of 2026-09-03 (plan
    `document-harness/plans/promise-path.plan.md` ruling 11), taken on the executor's class scan
    at the decision point `HD-70` reserved for it; the same ruling ratified leaving `:195-196`
    (*A remaining blocker or `SPEC_GAP` stops*) and `:200-201` (*an unrepaired blocker*) as
    written, both being descriptions of the flow that the new value reports rather than reroutes.
    Unlike every earlier write in this family, `E10`'s design test **does** fire here — the value
    changes what `R3` requires — and the round it opens is `PROMISE-PATH-VOCAB`, already open,
    which is where this write happens. No valid independent FULL has occurred on this round's
    candidate, so under `E9` this is candidate work and consumes no fix leg. The signed blob above
    is unchanged and v4 is **not** re-signed; this write's `E2` disclosure rides its own commit
    body, naming `contract/Document-Work-Assurance-Contract-v4.md` site by site, and the changed
    text owes `E10`'s independent re-read, riding this round's next read of that layer.
  - **Ninth post-signature write, 2026-09-03 — round `CORE-MOUNT`'s rider commit, this commit.**
    Two sites in §13.2, one authorisation, and both of them the class `HD-63` already covers.
    **The enumeration of `assurance_state.DIGEST_PROTECTED_FIELDS` gains
    `bind_authorization_ref`** — `:300-302` after this write, the `:299-301` rider
    `protected-set-says-five` named before it — and **"Only one protected field has a live
    write path … of the five … the other four" becomes two live write paths of six**, naming
    `bind_authorization_ref` as authored by `run_bind_v2.py` beside `review_ref` — `:335-340`
    after this write, `:334-338` before. Both sentences
    were true when v4 was signed on 2026-08-23 and were made false elsewhere: `97cc298`, round
    `PROMISE-PATH-VOCAB`, added `bind_authorization_ref` to that set as the fourth user-decision
    pointer and gave the round-0 `NO_REPAIR` gate the second live write path. That is `HD-63`'s
    class exactly — a statement of fact, not an obligation — so no new entry in this family
    opens, and what the contract **requires** is untouched: the policy's predicate has always
    been *a field the executor may not author the current version of*, and the enumeration
    states which fields those are rather than deciding it. `E10`'s design test therefore does not
    fire and no round opens for this write; it lands inside round `CORE-MOUNT`, whose FULL has
    not occurred, so under `E9` it is candidate work and consumes no fix leg. The user confirmed
    the class on 2026-09-03 when the finding was banked as rider `protected-set-says-five`, and
    ruled the form at this round's `E11` card (plan `document-harness/plans/core-mount.plan.md`
    ruling 2): its own commit, `E2` disclosure site by site, this entry, and the row deleted in
    the same commit. **What was reached outside this file's subject, recorded because `E7` makes
    the class the unit**: the same commit closes the class's other two sites,
    `tooling/rsclib/document_harness/summary.py:202` and
    `tooling/tests/document_harness_review/test_run_v2_template_bind.py:1041`, each reading
    *five* where the set is six; the class scan that bounded the sweep is pasted in that commit's
    body (`HD-41` ④). **The decision this closes**: a caller deriving digest policy from the
    signed text treated the licence pointer as unprotected and met `POINTER-UNVERIFIED`. The
    signed blob above is unchanged and v4 is **not** re-signed; this write's `E2` disclosure
    rides its own commit body, naming `contract/Document-Work-Assurance-Contract-v4.md` site by
    site, and the changed text owes `E10`'s independent re-read, riding the next read of that
    layer.
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

`E10`'s membership sentence does not name this one, and this file claims
authority over no rule: it records a signature that already happened and states which bytes it
binds. Every rule about what the signed text *requires* belongs to the contract. `E10-sync` does
not fall due — the membership sentence is untouched.

**Which side it sits on.** The construction side: this instrument's own governance record, like
the four carriers before it, and listed as such in `CONSTRUCTION-INDEX.md`. A caller does not
carry this file, which is why the contract and `document-harness/README.md` **name** it rather
than link it.
