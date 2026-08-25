# Plan — batch `CORE-SET`: take the instrument's own construction history off a product run's dependency surface

> **Status: open.** Written 2026-08-25 at batch open, base `5425fa2`, branch `main`. **This file
> is the carrier of the eight user rulings of 2026-08-25** below: until this commit they lived
> only in the conversation that took them and in a session-side briefing outside the tracked
> tree, which is chat-only load-bearing material and a finding under `R2`. A cold session reads
> this file, then `CONSTRUCTION-LEDGER.md`'s current pointer, then works.
>
> **No round is open yet.** Four questions in *Open questions* below are the user's to answer
> before round 1 opens; step 3 is the `E10` cold read and the `E11` card, not this commit. This
> commit is orchestrator bookkeeping — a plan plus a ledger pointer entry, the ledger batch
> shape of 2026-08-03, whose gate is the user ruling rather than a round.

## Goal (one line)

A repository that mounts this instrument must be able to carry the core set alone — no
construction journal, no plans, no review records, no decision log, no rider bank, no
construction ledger — and open, run and close a product round without any of them.

## The eight user rulings of 2026-08-25 (this file is their carrier)

1. **The `§live` reading obligation refers to the decision log of the repository the round runs
   in.** The harness's own `HARNESS-DECISIONS.md` is this instrument's internal file; a caller
   has its own, created by `dtw init`, and the layer may refer to it **directly by name**. The
   defect is the `../` prefix, not the name: written from inside the instruction-layer
   directory that prefix resolves to the instrument's own copy under the mount, never to the
   caller's.
2. **Onboarding no longer reads it at all.** `ONBOARDING.md`'s pre-start read obligation drops
   the decision log — it does not exist yet at that moment, since `dtw init` (its own item 3) is
   what creates it.
3. **The permission to move the decision log is revoked.** `ONBOARDING.md` item 3's "Move it if
   the caller wants it elsewhere" goes; the log is pinned to the repository root, the only place
   `init` writes and the only path every convention names.
4. **The C4 `O-1` sampling obligation is cut in two.** A product run's closeout writes its one
   comparison line and owes nothing else; reading the collected lines and taking the
   three-branch re-ruling is a construction round's work, not a product run's closeout.
5. **The contract v4 signature moves to a standalone signature file beside `contract/`**, out of
   `HARNESS-DECISIONS.md`.
6. **The v1 package-bound leg retires whole** — `REVIEW.md`'s pointer, the CLI's `--package`
   mode and `review.py`'s v1 half together. Distribution post-dates v3; no new caller can meet a
   package-bound run.
7. **`DEFAULT_REVIEW_RECORD_DIRS` is renamed**, and existing callers do a one-time migration.
8. **The 2026-08-24 ruling that closed §10.5 does not bind this batch** — it answered "submodule
   or plugin", not "what belongs in the mount". The user set it aside explicitly. Recorded here
   so a later reader does not read this batch as overturning that ruling.

## Measured starting state — this session, at `5425fa2` (`E3`: re-run before any claim)

`git ls-files | wc -l` → **384** tracked files; summed `stat -c%s` over them → **6,576,091 bytes
(6.27 MB)**. History buckets by `git ls-files <path> | wc -l`: `migration/` **199**, of which two
are the retired-contract stubs that are `E10` members and survive any strip, so **197** are
history; `document-harness/journal/` **34**; `document-harness/plans/` **24**.

**The mechanical layer is already history-free** — inherited from the batch briefing's
end-to-end measurement (a `git archive HEAD` tree with every history path deleted ran
`dtw --help`, `dtw init` into a fresh repository, `candidate_path_check.py`,
`review_freeze_check.py` and a 9/9 member resolve, all green) and **not re-run by this
session**; step 6 re-runs it. What this session did re-run: the nine members resolve **9/9** at
`5425fa2` (`test -f` each).

**What breaks when history is stripped**, measured by this session's own script (markdown link
targets plus backtick path-shaped tokens, de-duplicated per site, resolved against a tree with
`migration/` — less the two member stubs — `document-harness/{journal,plans,history}/` and the
five root registers removed):

| member | newly broken by the strip | already broken at `5425fa2` |
|---|---|---|
| `document-harness/README.md` | 17 | 4 |
| `contract/Document-Work-Assurance-Contract-v4.md` | 9 | 3 |
| `document-harness/EXECUTION.md` | 4 | 18 |
| `document-harness/CONSTRUCTION-CHECKLIST.md` | 3 | 0 |
| `document-harness/REVIEW.md` | 2 | 4 |
| the two retired-contract stubs | 1 each | 0 |
| `document-harness/ORCHESTRATION.md` | 1 | 0 |
| `schema/document-assurance-v3/paragraph-map.schema.json` | 0 | 0 |
| **total** | **38** | **29** |

The briefing reported 32 / 24 on its own tokenizer. **Neither figure is re-derived from the
other and the difference is method, not disagreement** — the already-broken column here is
inflated by design, since it counts run-time markers `E10` explicitly rules as resolving. The
figure a reviewer should re-derive is the load-bearing subset below, which is method-independent
because it is a fixed name list.

**The load-bearing subset — every site naming one of the three registers**, from
`grep -n -o -E '(\.\./)?(HARNESS-DECISIONS|HARNESS-RIDERS|CONSTRUCTION-LEDGER(-archive)?)\.md'`:

- `ORCHESTRATION.md:51` — one markdown link into the mount (item A)
- `EXECUTION.md:283`, `:285` — the construction ledger named twice (item E)
- `CONSTRUCTION-CHECKLIST.md:151` — bare `HARNESS-DECISIONS.md`; `:206` — bare `HARNESS-RIDERS.md`
- `ONBOARDING.md:16` — prefixed (item B); `:98` bare, `:100` prefixed, `:106` bare rider bank (item C)
- `document-harness/README.md` — 9 sites (item D)
- contract v4 `:16` and `:341` — 2 sites, each counted twice by the tokenizer (round 2, item F)
- `REVIEW.md` — **0**

## How acceptance 1 is read (stated, because ruling 1 makes the literal reading wrong)

The briefing's acceptance 1 asks for **zero** references to the three registers from the
product-facing documents. Ruling 1 keeps the **bare name** and removes only the `../` prefix and
the link target, so a literal zero would contradict the ruling that authorises the change.
**The test is therefore: zero path-shaped references — no link target, no `../`-prefixed
token — from `ORCHESTRATION.md`, `EXECUTION.md`, `CONSTRUCTION-CHECKLIST.md` or `ONBOARDING.md`
into the three registers. Bare names survive by design**, and `CONSTRUCTION-CHECKLIST.md:151`
and `:206` are expected to still hold theirs when the round closes.

## Open questions — the user's, before round 1 opens

1. **The slicing.** Proposal, risk-graded: round 1 `CORE-SET-LAYER` = items A B C D E (prose
   only; delivers the goal; no frozen bytes, no code) · round 2 `CORE-SET-SIGNATURE` = item F
   (`E2` frozen bytes plus a signature re-siting; its own ruling, its own review) · round 3
   `CORE-SET-CODE` = items G H (code, a large test surface, a migration with a silent failure
   mode).
2. **Item F's signature question.** `HD-56` *is* the signature. Does moving it to a standalone
   file **preserve** the signature, or does v4 need **re-signing**? Not the executor's call.
   Separately, writing contract v4's bytes at all needs `E2`'s recorded ruling.
3. **How the core set is defined.** It **cannot be carved by directory**: `document-harness/`
   holds 70 tracked files of which 59 are history (34 journal, 24 plans, 1 retired instruction
   text), leaving 9 top-level documents plus 2 templates — and 3 of those 9 are design drafts
   (`io-design.md`, `split-design.md`, `split-travel-manifest.md`), not layer members. So the
   definition needs either an explicit member list or a move of `journal/`, `plans/` and
   `history/` out from under `document-harness/`. No ruling above answers this.
4. **Newly found by this session, and it is a scope question, not a ruling.** Item A edits
   `ORCHESTRATION.md`'s nine-obligation table and `E10`'s `§live` clause — which is the recorded
   touch surface of **three banked riders**: `waiver-live` (the `E10` cold-read / `§live`
   clause), `charter-qualifiers` and `e1-table` (both `ORCHESTRATION.md`'s obligation table).
   All three were routed on 2026-08-25 to the **dispatch-economy** batch as design rows, and
   round 1 reaches their surface first and is round-eligible, so `R10`'s touch condition arrives
   here. The briefing directs only `waiver-live` to be redeemed in the item-A commit. **Do the
   other two ride round 1, or stay with dispatch-economy carrying a touch note?**
   (`e1-reader` names the *three-roles* table, a different surface; it does not fall due.)

## Constraints

- **`E2` frozen bytes** = contract v4 (`dfc983d2…`, corrected under `HD-57`; the signed blob
  `614932de…` stays the object `HD-56` binds) plus the fifteen files of
  `schema/document-assurance-v3/`. Item F touches the contract → **needs a recorded user ruling
  before any byte is written**. Item G must **not** touch
  `schema/document-assurance-v3/review.schema.json`, which holds both ReviewPackage and
  ReviewResult and is frozen; that retirement is code and prose only.
- **`E10` design test.** Items A–E change what a rule requires *inside a caller* even where this
  repository sees no change → design, opens a round; the free channel does not apply.
- **`E10-sync` does NOT fall due.** No item touches the membership sentence. The three-site
  checklist is not applied, and the commit body says so, so the next reader does not wonder.
- **`HD-55` role form**: orchestrator, executor and reviewer are three sessions; dispatch cold
  via `dtw dispatch`, and the orchestrator hand-edits no work product.
- **`HD-34` caller discipline** is untouched: nothing here lets a caller modify instrument
  content.
- **`E10` already contains the rule items A–C enforce** — "a caller-held path is *named, never
  written as a path token* … an artifact living only in a caller is given its name and its
  holder instead". This is alignment to a stated rule, not new design of one. Two places already
  say the intended thing: `document-harness/templates/decision-log.md` is titled "user rulings
  for **this repository's** use of the harness", and `ONBOARDING.md` item 3's Owner cell already
  calls the harness's own copy "a filled **example** of the same".
- **`layer_path_check.py:63` skips tokens without a `/`**, so a bare `HARNESS-DECISIONS.md`
  token is never scanned; the guard cannot see whether ruling 1 was honoured. The round's
  evidence is the grep above, not the guard.

## Out of scope

- OUT: changing the distribution mechanism. Submodule stays; packaging as a plugin is not this
  batch (ruling 8 sets the 2026-08-24 §10.5 ruling aside rather than overturning it).
- OUT: producing a stripped or published core-set artifact or branch. This batch removes the
  *dependency*; how the core set is shipped is a later question.
- OUT: deleting any history from this repository. Everything stays; only the product run's
  reliance on it goes.
- OUT: `schema/document-assurance-v3/` — frozen, and item G is defined to avoid it.
- OUT: reorganising `tooling/tests/` beyond what items G and H break.

## Work items

Sites are at `5425fa2`.

### A — the `§live` obligation stops pointing into the mount

- `ORCHESTRATION.md:51` — drop the link, leave the bare name.
- `README.md:27` — drop the link target into the mount, keep the obligation sentence, and point
  the mechanism at `templates/decision-log.md`, where the rules actually live (`HD-19`).
- `CONSTRUCTION-CHECKLIST.md:151` — **no path change**; it already reads the bare name. Add only
  what ruling 1 makes explicit: the file meant is the one in the repository the round runs in.
- Redeem rider `waiver-live` in the same commit (same clause), deleting its row there.

### B — onboarding drops the read

- `ONBOARDING.md:16` — remove the decision log from the "Read once before starting" sentence,
  leaving the instrument's navigation surface.

### C — the decision log is pinned to the root

- `ONBOARDING.md` item 3 **Do** cell — remove "Move it if the caller wants it elsewhere; record
  that in the file itself"; state that the root is the only supported placement, and why: the
  layer refers to it by bare name and `init` writes only there. Keep the measured empty-log
  paragraph — it becomes the *reason* rather than a caveat.
- Item 4 (rider bank) says "Moving it carries item 3's cost unchanged" — make it consistent with
  whatever item 3 becomes.
- **Added by this session's measurement:** item 3's **Owner** cell carries a prefixed token into
  the mount at `:100`, a site the briefing's item C did not list. Either it goes the way of item
  A's or the round states the residual it leaves.

### D — `document-harness/README.md` splits

- Keep 10 rows: contract v4 · what else lives in `contract/` · the four schema rows · role
  instructions · construction-side rules · onboarding · local enforcement.
- Move 9 rows to a new tracked file at the repository root, beside the other construction
  registers: **`CONSTRUCTION-INDEX.md`** — v3 execution plan · N0 record · N1 record · N2 record
  · contract fixtures · journals · decision log · rider bank · construction ledger.
- Leave one row in `document-harness/README.md` pointing at it.
- **Not folded into `CONSTRUCTION-LEDGER.md`**: that file's header admits only two things
  (current pointer, construction rulings with no other home) and carries a 180-line bound.
- Row 27 is also item A's site → **A and D land in one commit**.

### E — the C4 `O-1` obligation is cut in two

- `EXECUTION.md:283-285` — a product run's closeout writes the one comparison line, full stop.
  Remove from the product-side charter the reach into the construction ledger's
  conversation-only line and the "next product run's closeout" reading moment.
- `CONSTRUCTION-LEDGER.md:110-114` conversation-only list — the three branches stay; the reading
  moment becomes a construction round's, not a product run's closeout.
- `HD-54` (`§implemented`, scope `one-shot`) states the reading moment as the next product run's
  closeout. Changing it needs a **successor entry carrying the narrowed text in full**, the
  original moved to `superseded`, both in the same commit as the carrier (decision-log
  invariant, `HD-30`).

### F — contract v4's signature moves out of the decision log *(round 2)*

- New file beside the contract, shaped like the retired supersession-2 signature record.
- `contract/Document-Work-Assurance-Contract-v4.md` — the frontmatter `signature_owner:` field
  and the signature-semantics block both name the decision log today; both repoint.
- **The machine does not constrain the carrier**: `checks.py:489` rejects only a document
  carrying its *own* approval status; `_owner`-suffixed fields are whitelisted as the correct
  delegating form and nothing ever opens the delegate. Precedent: this contract family's
  signature has lived in four carriers — the N0 record §8 (v3) · the W2 record (s1) · the
  supersession-2 signature record (s2) · `HD-56` (v4).
- **Highest-risk item**, and the reason for the slicing: two things need the user, not the
  executor — the `E2` ruling to write frozen bytes, and open question 2's signature call.

### G — the v1 package-bound leg retires *(round 3)*

- `REVIEW.md:92` pointer + the v1 package-flow document under `document-harness/history/`.
- `tooling/rsclib/document_harness/cli.py` — the `--package` option (`:662`) and
  `_cmd_v3_review`'s v1 branch (`:452` onward); `review` keeps its `--subject` mode.
- `tooling/rsclib/document_harness/review.py` — the package half: `member` · `freeze_package` ·
  `package_digest` · `members_by_role` · `check_package` · `verify_member_bytes` ·
  `load_package`. Decide per function whether the v2 path still calls it before deleting;
  `review_result_v2.py` is the v2 side.
- Tests: the package-and-review suite under `tooling/tests/document_harness_review/`, plus the
  v2-subject CLI suite and the fix-round-locks suite, which also reference the package.
- **Do not touch `schema/document-assurance-v3/review.schema.json`** — `E2`-frozen.
- Removing a CLI *option* has the shape `HD-47` rules per-case for a command; ruling 6 covers it.

### H — `DEFAULT_REVIEW_RECORD_DIRS` is renamed *(round 3)*

- `tooling/rsclib/document_harness/caller.py:50` — the old migration directory default becomes
  `("assurance/review-records/",)`, matching the shape of `DEFAULT_SPECIFICATION_SURFACE`.
- **Migration hazard, and it is silent.** `dtw init` writes the defaults into
  `.harness/scan-surfaces.json`, and `.harness/` is gitignored. An existing caller keeps working
  where the declaration already exists (`init` refuses to overwrite), but **any fresh clone
  loses the declaration**, and a re-run `init` writes the new default — at which point that
  repository's existing records stop being recognised, with nothing to say so. Ruling 7 accepts
  a one-time migration; the round states what it is — at minimum the known caller's declaration
  written explicitly and the advice recorded in its policy file.
- Prose sites naming the old directory need the same pass: `caller.py` docstrings, `REVIEW.md`'s
  record channel, and `ONBOARDING.md` where it appears.

## Steps

- [x] 1. Carry the eight rulings out of session-side material into committed state: this tracked
  plan plus a `CONSTRUCTION-LEDGER.md` current-pointer entry (batch name, queue position against
  the dispatch-economy batch). Until this is done the rulings are unreachable by any reviewer.
- [ ] 2. Put the four open questions above to the user and record the answers in this file.
- [ ] 3. Open round 1 under `HD-55` role form: cold layer read via `dtw dispatch --read`, then
  render the `E11` preview card and wait for the user.
- [ ] 4. Execute items A+D in one commit; B+C in one commit; E in one commit, with the `HD-54`
  successor entry in the same commit as its carrier.
- [ ] 5. Redeem rider `waiver-live` in the item-A commit, deleting its row in that same commit;
  the other two riders per open question 4's answer.
- [ ] 6. Re-run the stripped-tree measurement — the mechanical end-to-end run this session
  inherited rather than re-ran, and the reference count — and record both in the round's journal.
- [ ] 7. Dispatch the FULL, walk the `E9` budget, land the record unchanged, close round 1.
- [ ] 8. Open rounds 2 and 3 per the ruling from step 2, each with its own plan file if their
  shape has changed by then.

## Acceptance — round 1

Each shown by its command, not by a sentence.

1. On a tree with every history path removed, **zero path-shaped references** (link target or
   `../`-prefixed token — see *How acceptance 1 is read*) from `ORCHESTRATION.md`,
   `EXECUTION.md`, `CONSTRUCTION-CHECKLIST.md` or `ONBOARDING.md` into the decision log, the
   rider bank or the construction ledger. Residual pure-citation breaks in `REVIEW.md` and
   contract v4 belong to rounds 2 and 3; the round **states the count it leaves** rather than
   implying none.
2. `document-harness/README.md`'s table holds 10 rows; `CONSTRUCTION-INDEX.md` exists at the
   root and holds the other 9; the README-owned breaks measured above are gone.
3. `python -m pytest -q` green — report the run, not a remembered figure.
4. `layer_path_check.py`, `candidate_path_check.py` and `review_freeze_check.py` each exit 0 on
   the staged tree, and the `E10` members resolve 9/9.
5. `dtw init` into a fresh repository still exits 0, and in that repository the decision log
   resolves to exactly one file.
6. Rider `waiver-live`'s row is gone from `HARNESS-RIDERS.md`, in the same commit as its carrier.
7. The round's FULL returned `REVIEWED_NO_BLOCKER`, or `CHANGES_REQUIRED` → one approved fix →
   VERIFY `REVIEWED_NO_BLOCKER`, with all three records committed unchanged.

## Resume pointer

当前指针: step 2 — the four open questions are with the user. Round 1 does not open until the
slicing is ruled; steps 3–7 follow that answer.

## Notes

- A second name collision exists, and item H is only half of it: `dtw init` creates a decision
  log and a rider bank at a caller's root under the same names this repository uses at its own
  root. That half dissolves by construction once the core set excludes the instrument's own
  registers, which is what items A–C make legal. **Verify it (acceptance 5) rather than editing
  anything for it.**
- Figures here are measurements at `5425fa2`, scope `git ls-files`, and go stale. Re-run rather
  than cite.
