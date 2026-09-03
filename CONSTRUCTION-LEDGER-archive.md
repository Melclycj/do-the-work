# HARNESS LEDGER — archive (read-only)

> Split off `HARNESS-LEDGER.md` on 2026-07-27, same operation and same reason as the
> `.goals/LEDGER.md` split earlier that day: the live pointer has to be readable in one go.
> **Moved verbatim, nothing deleted, nothing retyped.** Do not append here — a round's
> narrative belongs in its own review record and commit message, both immutable.

## 历史轮次叙事（2026-07-27 从 `.goals/LEDGER.md` 原样搬入 — 只读，勿续写）

- **▶▶ RESUME HERE (2026-07-27, executor session #3). ⑤ RAN, was reviewed `CHANGES_REQUIRED`, and is REVERTED — the user's questioning of the requirement found the issue's own premise false. Nothing from ⑤ is in the tree; the review record is kept.** Chain: candidate `9c13008` → independent FULL (3 must-fix / 4 low / 5 observations) → user asked what the field buys → **revert `7011916`** (+14/−462, exact inverse) → review record `2ace576` (`v3-review-full-9c13008.md`). **The false premise, recorded because it is the reusable part:** `issue-p3-corr-no-vocabulary-for-repaired-blocker` asserted that the controller "has no vocabulary for 'repaired' and should not invent one, since that judgment is the reviewer's", and the `cc873e6` triage rationale adopted that sentence unchallenged. It does not hold — a VERIFY that names a finding in `verify_scope.accepted_finding_ids` and returns `REVIEWED_NO_BLOCKER` **has already made the judgment**, because a blocker the repair failed to close must be re-raised as a blocking finding in that same VERIFY or the verdict contradicts itself (`V3-REVIEW-BLOCKER-CONTRADICTS-VERDICT` already enforces this). Enumerated over the three situations a VERIFY can meet (all closed / one open and blocking / one open and non-blocking), the **existing vocabulary expresses every case**, and p3-corr demonstrated the third literally (`v1-f3-condition-discharged-at-four-of-six-sites`). So a per-finding resolution column buys **no expressiveness — only one derivation**, and the whole benefit was two rendered lines on the FINAL surface, once per repaired run, in a harness that has had one repaired run. **If it is ever wanted, two things not to rebuild wrong:** (i) the cheap form is ~5 lines in `check_assurance_candidate` — open = raised blocking by any bound review, minus those a VERIFY declared covered **and** returned `REVIEWED_NO_BLOCKER` on; verified against p3-corr's committed bytes to yield `open = []` where the run actually listed f1 + a disclosure, and it works on already-closed runs, which the new field could not; its cost is coarseness (mixed round → nothing subtracted); (ii) if a per-finding column is ever built anyway, **put the result on the `verify_scope` entries, not in a parallel array** — the round's three alignment checks (out-of-scope / duplicate / incomplete) existed only to keep two arrays in step, and 2 of the 3 must-fix findings grew on that machinery; the parallel array was chosen only to avoid duplicating v1's frozen `verifyScope` $def in v2. **Riders `nd-F1` and the `O3` read-flag closure were bundled into `9c13008`, so the revert returned them to the bank** — they ride the next batch touching the instruction layer; nothing else was lost. **Instruction layer is byte-identical to `afa06ac`** (`15b49790` / `d553c098` / `a56c4d02`), a state already read at `7e7c3b5`, so **no amendment exists and no checkpoint read is owed**; the contract-provenance pre-commit hook was deliberately bypassed on the revert commit (user ran it) rather than satisfied by a fresh entry that would itself owe a fresh read — `repo-audit.py` was run by hand instead (exit 0). Suite back to **432**; three signed blobs untouched throughout. **Process lesson, and the strongest data point yet for `issue-p3-corr-harness-self-maintenance-burden`:** the preview card described *how* the round would build, never *what it buys / how often it is used / what happens if skipped* — one line of that would have stopped this before the round opened; and ISSUE_TRIAGE adopted the issue's own sentence instead of testing it. **NEXT unchanged: the channel HarnessIssue** (standing ruling: before Stage 2), **then Stage 2 (P4-ACTIVATION-BRIDGE)**. Push debt re-derive with `git rev-list --count origin/main..HEAD` before quoting it.

- **▶▶ (superseded by the bullet above, same day) ⑤ candidate LANDED `9c13008`.** Round opened on the user's two rulings at the preview card: **(a) no node-boundary cold read** — this is a continuation of the same construction thread, not a new node, and the layer was cold-read at `1df6245` with every batch since carrying its own read; **(b) the instruction-layer bytes in this batch are approved, and this round's own FULL serves their rule-1 read.** What landed: `review.v2.schema.json` gains an optional root `finding_resolutions` (VERIFY-only via a new allOf branch; `$defs/findingResolution` = `finding_id` + `RESOLVED`/`UNRESOLVED`/`UNVERIFIABLE` + required `note`), `review_result_v2.py` gains `resolved_finding_ids` + three checks (`RESOLUTION-OUT-OF-SCOPE` / `DUPLICATE-RESOLUTION` / `RESOLUTION-INCOMPLETE`), and `summary.check_assurance_candidate` subtracts a VERIFY's `RESOLVED` ids from the open-blocker set, reporting a listed-but-resolved id under its own `RESOLVED-BLOCKER-LISTED` because the existing `BLOCKER-INVENTED` message ("no review records it as a blocking finding") becomes false in that case. **Fail-closed at every layer**: a v1 result, an unrecognised `schema_version`, a FULL, a VERIFY that answered nothing, and a finding answered two ways each resolve nothing — so p3-corr and every closed run bind exactly as before and there is no migration. The version test is a plain key comparison rather than `result_schema_kind`, because at the binding an unreadable review must leave blockers standing rather than raise. **Declared deviation (same shape as ①): the triage rationale predicted "a signed-schema change plus an invariant change" — no signed byte is touched** (plan `8ad404b1` · contract `b2dbdf75` · supersession-1 `68031fa2`, all three re-derived identical at commit) **and N2-A9's plan text is unchanged**; what changed is its mechanical rule in `summary.py`. **Deliberately absent**: a helper deriving `unresolved_finding_ids` for the run script — it would make the N2-A9 guard read its expectation out of the thing it guards (scope rule 2). Instruction layer: `REVIEW.md` gains one VERIFY-scoped bullet under "What every result must carry"; the operating contract's discipline lead-in takes banked rider **nd-F1** ("The three rules below" → "Rules 1–3 below" + rule-4 attribution); **and — an addition beyond the preview card, declared rather than silent — both contracts' 2026-07-27 read flags close to `v3-checkpoint-read-afa06ac.md` (`7e7c3b5`)**, which is the banked observation **O3** riding this batch by the same bank rule as nd-F1. **The bank is now empty.** Facts: 9 files **+462/−14**; suite **432 → 443** (11 added, none replaced or deleted); fixture validator 41/41; repo audit exit 0 via the pre-commit hook, which also passed the provenance check on both contracts. Nine mutation probes M1–M9 each went red **on the intended test** and each file restored **byte-identical** from scratchpad copies (sha256-compared, never `git checkout --`); the three `summary.py`/`review_result_v2.py` mutations were re-run without `-x` to read the failing node ids rather than trusting a first-failure count. Dispatch derived `rsc v3 dispatch --range f25358e..9c13008` exit 0 — **NEXT: user routes it to an independent review session; after this round closes → the channel HarnessIssue** (standing ruling: handled before Stage 2), **then Stage 2 (P4-ACTIVATION-BRIDGE)**. Push debt re-derived `git rev-list --count origin/main..HEAD` = **182**, user-gated. Working tree at this point: this file (uncommitted per convention) + untracked `ResearchSystem/docs/` (still unattributed, untouched).

- **▶▶ (superseded by the bullet above, same day) executor session #2. ①'s FULL returned `CHANGES_REQUIRED`, the user ruled the guard DELETED, the fix LANDED `dc1e8a3` — a targeted VERIFY is now owed and the dispatch is derived.** FULL record `d7d621d` (`v3-review-full-dcfb2f2.md`): 2 must-fix + 6 low + 3 observations, **both blockers in the postcondition guard the candidate added on its own initiative, neither in the capability the issue authorized** — which the reviewer confirmed closed by its own counting probe. I reproduced both bypasses against the committed bytes before touching anything: a command that runs `git checkout --detach HEAD~1` and then exits 0 only when it counts the *base* file set gets `PASS` provenanced to the candidate (the V3-D5 "check candidate A, report candidate B" shape, unreachable before this round), and a command that writes an untracked file and counts it gets `PASS` on a count the candidate does not have. **User rulings 2026-07-27, recorded here because the chat is the only other place they exist:** the guard is **deleted** (their answer to the O4 question review-contract §10 forbids a reviewer to conclude — a boundary **wider** than the reviewer's minimum fixes, declared in the fix commit per hard rule 9), and the remaining findings are applied. Deletion moots F1/F2/F3, all three being properties of that guard. What the guard actually was, structurally: `command_exit`'s judgement is the exit code and `subject_tree` is only *what the judgement is about*; the pre-change HEAD-equality rule was a **precondition on the tree** (correct but unsatisfiable under the same-branch evidence-commit topology, which is the issue), materialization replaces it **by construction**, and the guard was a **postcondition on the process** — a third thing neither the closed union, the contract nor the issue asked for. It also overloaded `WRONG_SUBJECT`, whose schema meaning is "observed a tree it was not entitled to observe", to mean "the entitled tree was disturbed"; neither the reviewer nor I named that until the structure was drawn out. Landed in `dc1e8a3`: F3's false "independent evidence" claim replaced by what the mechanism does establish + the **permanent endpoint** (mutate→read→restore is invisible to any end-state oracle; marked do-not-schedule) + where a command's behaviour is actually settled (WorkSpec author writes the argv, review reads it); **F4** the eol/filter sentence (`core.autocrlf=true` → a subject stored LF is written CRLF while `subjects[].digest_sha256` comes from the Git object); **F5** the repository-wide `git worktree prune` deleted — probe M5 re-added it and an unrelated sibling worktree whose directory was renamed away went 2 registrations → 1, absent it 2 → 2 with the sibling intact, `candidate.py` restored byte-identical (`d62287f6`) between runs; **F8** the surviving `assertIn("tools", …)` → full-line `assertEqual`. Suite 434 → **432** (two guard tests deleted; no test pins the ceiling, since asserting PASS-on-mutation would encode a ceiling as an expectation). Three signed blobs re-verified. **F6 and F7 are false statements inside `dcfb2f2`'s immutable commit message; the true values are: M2's mutation failed 4 tests, not 3 (I counted within the new class and wrote it unscoped), and ① is first of what *remained* under the ④→①→⑤-after-②③ ruling, not first of the pre-Stage-2 fixes.** **The targeted VERIFY RAN and returned `PASS` same day — record `f25358e`** (`v3-review-verify-dc1e8a3.md`): 0 must-fix, 0 low, 4 observations none owing a fix. Every ruled disposition verified against the repair diff; the capability re-verified in the reviewer's own repository and mutation-proven to still have teeth (running the command in `repo_root` instead of the materialization fails 3 tests); the prune deletion probed independently at 2 → 2 registrations across a live check run; the repaired F8 assertion mutation-proven red. Their two mutations were restored byte-identical, which I verified rather than accepted — all three tooling files' worktree sha256 equal their `dc1e8a3` blob content. **Round budget now fully consumed: the FULL, the one user-approved fix, and the targeted VERIFY.** Four observations carried, none owing a fix: **O1** the fix commit's "recorded in the ledger" points at this uncommitted file (both F6/F7 true values are committed in the FULL record, so no fact is repository-absent); **O2** this bullet had written the VERIFY verdict set as `REVIEWED_NO_BLOCKER / SPEC_GAP` — **wrong, and corrected here**: review-contract §4 line 154 gives the construction-round VERIFY set as **`PASS` / `SPEC_GAP`**, while `REVIEWED_NO_BLOCKER` is contract-v3 §5's *product-side* ReviewResult vocabulary. Root cause: I pattern-copied the p3-corr entry below, where that word was correct because p3-corr was a product run. That is precisely the defect class discipline rule 4 names — characterizations copied from neighboring entries; **O3** both operating contracts' last provenance entry still ends "Read: owed by this batch" although the read was recorded at `7e7c3b5` — outside this round's bytes, rides the next batch touching the layer alongside banked **nd-F1**; **O4** the ratchet broke toward deletion at net −33 lines, nothing added that can earn a finding next round. **NEXT = ⑤** (repaired-blocker vocabulary in the VERIFY schema, consumed by the N2-A9 binding rule) in a NEW session, **then the channel HarnessIssue** (standing ruling: handled before Stage 2), **then Stage 2 (P4-ACTIVATION-BRIDGE)**. Push debt re-derived at this point by `git rev-list --count origin/main..HEAD`: **181**, user-gated (re-derive, never trust a number in prose). Session honesty note: I read only lines 1–73 of this 666-line file at session start and worked off page 1 all session, and I reversed position on the guard three times before the user forced the structural question; nothing in the Claude Code settings was throttling (checked: `effortLevel: xhigh`, no thinking cap).

- **▶▶ (superseded by the bullet above, same day) ① construction candidate LANDED — `dcfb2f2` awaits its independent review.** The round (preview card approved in-session): `command_exit` declaring `candidate_commit` is no longer refused `WRONG_SUBJECT` on HEAD≠candidate — it runs inside a disposable `git worktree` materialization of the exact candidate commit (`candidate.py`: `materialized_candidate` + `materialization_drift`; `checks.py`: `_wrong_subject` drops the HEAD-equality clause, `_check_command_exit` materializes + post-run re-verifies: tracked modify/delete → `WRONG_SUBJECT` no exit_code; untracked additions excluded). Facts: 3 files +273/−24; suite 427→434 (1 test replaced, 7 added in `CommandExitMaterializationTests`); mutation probes M1–M4 each red then restored byte-identical (sha256-checked; M4's first attempt was a syntax-broken mutant — collection error, not a guard proof — reapplied clean); zero schema/contract/plan/instruction-layer bytes (closed six-kind union + two-value treeKind stand; three signed blobs re-verified at commit); every pre-existing `command_exit` check declares `worktree`, that path untouched. **Declared deviation (user saw it on the preview card and approved): the triage rationale predicted "either one changes the signed check surface" — the chosen materialization fix touches no signed byte.** nd-F1 stays banked (this batch touches no instruction layer). Dispatch derived `rsc v3 dispatch --range 7e7c3b5..dcfb2f2` exit 0 — **NEXT: user routes it to an independent review session; after this round closes → ⑤ (repaired-blocker vocabulary, review.v2/N2-A9), then the channel HarnessIssue, then Stage 2.**

- **▶▶ RESUME HERE (2026-07-27). ①'s opening cold read is DONE and RECORDED; four findings await user dispositions — ① construction does NOT open until they are ruled.** Chain: user ruled **"Route"** on the owed rule-2 read → independent review session cold-read the whole instruction layer at tip `1df6245` under the executor-authored charter (the memory template — subagent-shaped, which forced a user relay; see the banked issue below) → record committed **`19bbc6d`** (`v3-cold-read-1df6245.md`, condensed form, e90243a shape). Yield 2+2+4: **F1 must-fix** — the layer still steers a fresh reader into the retired package-bound regime (supersession-1 signed 2026-07-24 is invisible from inside the layer; the carrier's own status line still reads UNSIGNED; fix = additive README supersession-1 row + one signature-state pointer sentence at each EXECUTION/REVIEW stage marker, zero carrier bytes); **F2 must-fix** — `review.v2.schema.json` root description falsely claims all five reused definitions are $ref-only (verdict + residual_uncertainty are inline restatements; fix = that one prose sentence, no schema logic); **F3 low** — README schema table omits review.v2, the only 1 of 14 absent (fold into F1's README edit); **F4 low** — review contract §2 signed-bytes row pins two blobs where the signed set has held three since the W2 signature (append supersession-1 blob `68031fa2…`); **F5–F8 observations, none owing a fix** (rule-1 termination clause; README record-admission criterion; spec.v2 byte-for-byte claim verified TRUE; worktree carries). The channel question the routing itself exposed — §12 fixes the record's *form* but not its *channel*, and the operative dispatch charter lives in memory outside rule-1's reach — is banked as the **sixth p3-corr HarnessIssue** `issue-p3-corr-review-record-channel-unspecified` (**`9da20ef`**, `check_issue` ok against live state; **user ruling 2026-07-27: handled before Stage 2** — the ruling lives here and in the commit message only, the schema carries no routing by design). **All four findings ruled fix and LANDED (same day): F3 `8d03563`** (README review row gains review.v2 AND the decay class is closed by `tooling/tests/document_harness/test_readme_enumeration.py` — every schema-file stem must appear in the README; guard proven RED on the pre-fix README with missing==['review.v2'] then GREEN, suite 426→427; both contracts' "no test reads it" sentences qualified in the same commit with the named exception + "otherwise", so the property claim stays true — the F2 lesson applied prospectively); **F1+F2+F4 `39e4136`** (README Supersession-1 row incl. naming the carrier's top-of-file UNSIGNED line as pre-signature authoring residue inside signed bytes; signature-state sentence appended to both EXECUTION/REVIEW stage markers; review.v2 root description restated per the reviewer's verbatim fix — three by $ref, verdict + residual_uncertainty inline because v1 holds them inline; review contract §2 signed-bytes row now pins all three blobs incl. supersession-1 `68031fa2…`; all three signed blobs re-verified byte-untouched at commit, suite 427, schema fixture validator OK). **The accumulated rule-1 read RAN and is CLOSED same day.** Dispatch `rsc v3 dispatch --range 9da20ef..39e4136` (record/issue commits excluded as provenance per the 94a97f5 precedent) → independent session returned **1 must-fix + 1 low + 5 observations, all four fix contents verified correct**: F1 — both contracts amended with zero provenance entry (the `979a983` omission class recurring); F2 — the new guard's bare substring match mutation-proven weak (2 of 14 stems unconstrained; README byte-restored). Record **`c9a1ac1`** (`v3-checkpoint-read-39e4136.md`). **User ruled: both fix, and mechanize the F1 class — with the constraint that a hook is a non-paper actor and its existence must be REGISTERED.** **Closure landed `43fb1c5`**: two provenance entries back-filled (both contracts again end "may be relied on as it stands"); guard narrowed to delimited tokens (`` `stem` ``/`[stem]`), re-proven RED ×3 directions with byte-verified restores; **`ResearchSystem/tooling/hooks/contract_provenance_check.py`** (tracked) wired into the untracked shared pre-commit hook (main-repo `.git/hooks/pre-commit`, existence-guarded so other worktrees/branches unaffected), registered in README's new **Local-enforcement row** with the honesty boundary (per-machine, absent on fresh clone, bypassable, advisory only). Probe-honesty trail, all caught in-session before being trusted: (i) the check's first RED was **fake** — GBK decode crash on the contracts' UTF-8 punctuation (`text=True` uses the locale codec on Windows; fixed to bytes + explicit UTF-8); (ii) the hook block was first appended **after the hook's unconditional `exit`** — dead code, which makes `43fb1c5`'s message claim "this commit itself exercises the hook's green path live" **false** (recorded here; commit messages are immutable and not instruction layer, O2 precedent) — hook rewritten with the check before the exit; (iii) a python-side `bash`→WSL-shim resolution produced a fake full-hook failure, identified before trusting; final LIVE proof via Git Bash: full hook **RED** (exit 1 + block message) on an unregistered contract edit, byte-exact restore verified, full hook **GREEN** (exit 0) on the clean tree. **CORRECTION (user caught it same day): the closure batch `43fb1c5` itself owes a read** — my commit-message self-declaration ("registrational bookkeeping, swept by the next boundary read") stretched the pointer-form exemption beyond its `1df6245` shape: the batch carries the F2 guard fix + a new check script + the README Local-enforcement row, and every fix batch in this thread got its own read; only pure flag closures rode free. This is exactly the cold read's F5-observed stretch risk, performed by me. **User ruled Route (2026-07-27); the read RETURNED same day: 0 must-fix / 2 low / 6 observations — record `4b1f7e9`** (`v3-checkpoint-read-43fb1c5.md`). Substance fully affirmed (back-fill attributions diff-verified; guard re-proven by five mutations incl. the reviewer's own M4 prefix-sibling probe; script + hook red/green/idle live-probed by the reviewer on this machine; suite 427 reviewer-run; signed blobs identical; pure appends). The two lows are registration-wording precision, one sentence each, reviewer-designed to **ride the next batch that touches the layer**: **cr-F1** — the review contract's 2026-07-27 entry says "Additive only; no earlier line changed", false for the batches it registers (both reworded a sentence in place; drafting slip — the entry's own neighbors name the reworded sites, and the operating contract's parallel entry avoided the phrase); **cr-F2** — the guard fix silently dropped the ruled "within the enumeration table region" qualifier (currently zero consequence — all 14 delimited stems sit in the three enumeration rows, reviewer-recomputed; disclosure sentence owed, region parser NOT recommended per scope discipline). Reviewer's closing: the registered amended text and the closure's substance **may be relied on** meanwhile. **User closed the loop 2026-07-27 ("越修越多" — stop), then ruled the NARRATION DIET after the burden assessment (definitions 认定 same day): rules-stratum untouched; narration is the sole recurring defect source and gets cut.** Landed **`afa06ac`** `V3-NARRATION-DIET-AMENDMENT-v1`: operating contract **discipline rule 4** (provenance entries = one-line derived facts, no characterization, pasted git facts over adjectives) + review contract **§12 wording-level bank rule** (fix changes no actor's action + accurate fact recoverable in place → rides the next layer-touching batch, no round, no read; test = name the downstream decision that goes wrong, or bank) + both riders cleared in the same batch (cr-F1 false phrase deleted; cr-F2 whole-README-matching choice disclosed in the guard docstring); both contracts' new entries are the one-line format's first application; suite 427. **PROCESS_BURDEN banked `a3054f9`** (`issue-p3-corr-harness-self-maintenance-burden`, the seventh p3-corr issue and first of its kind — the ~25-commit self-maintenance window with zero document work protected, recorded as the plan §10 adoption-criterion evidence; `check_issue` ok). The narration-diet batch's read **RAN and RETURNED 2026-07-27: 0 must-fix / 0 low / 1 banked wording-level / 7 observations — record `7e7c3b5`** (`v3-checkpoint-read-afa06ac.md`; one relay duplication disclosed per e90243a precedent). Both riders verified landed; both new entries conform to the rule-4 format they introduce; suite 427 reviewer-run; amendment text **may be relied on**. **The bank now holds ONE rider: nd-F1** — the discipline lead-in's "The three rules below" expired by rule 4's own addition (minimum fix "Rules 1–3 below" + rule-4 attribution, rides the next layer-touching batch; the bank rule's first catch is the amendment's own corner). Observations carried, none owing a fix: O3 bootstrap ordering (the read classified F1 under the bank rule the subject itself introduces — harmless here, user glanced); O4 one-sided counterparts recorded as choice; O1 standing authorization ceiling. **NEXT = REAL WORK: ① in a NEW session, then ⑤, then Stage 2** (channel HarnessIssue first per standing ruling). Push debt **177** (re-derived), user-gated. **Session-close preclear (2026-07-27), residuals for the record:** (i) `43fb1c5`'s commit message carries the immutable false claim "exercises the hook's green path live" — already documented in this bullet's probe-honesty trail, no further action possible; (ii) `contract_provenance_check.py` is live-probe-verified only, no in-suite regression test (the F7 residual class — a future round that owns the path may add one; not owed now); (iii) the pre-commit hook rewrite is machine-local (`D:/Thesis/.git/hooks/pre-commit`, shared by both worktrees, existence-guarded so the main worktree is a no-op; durably registered only via the README row + tracked script); (iv) the cold-read charter memory updated with the channel-issue caveat so a fresh session doesn't redispatch the subagent-shaped clauses to a full session. **User rulings this close: existing provenance entries stay as-is** (rewriting history = rule-3 risk for zero benefit; full deletion stays a REVISE_V3 candidate); **nd-F1 stays banked**. Working tree at close: this file (uncommitted per convention) + untracked `ResearchSystem/docs/` (unattributed, ask before touching). No background processes started or left running this session. Bank contents: **nd-F1** (sole rider). Ruling ledger for the harness user decisions this session lives in this bullet + the three read records + two issue files — nothing exists only in chat. Untracked `ResearchSystem/docs/` still as found (carried as F8, unattributed — ask before touching).

- **▶▶ RESUME HERE (2026-07-26 session close). The one review the 2026-07-25 bullet left genuinely open — the contract corrective batches' checkpoint read — is DISCHARGED and the whole scope-discipline thread is CLOSED; NEXT = open ① in a NEW session.** Full chain, all same day: the user routed the read to this session, which is the **executor** session — performed under a **one-time dispensation** (the ①⑤ executor rounds had not started, so nothing self-reviewed; dispensation recorded in the report's own footer, sets no precedent; the one-session-per-role rule stands — second incident logged in the `v3-session-role-separation` memory: flag the mis-address first, let the user route). Read record **`f7bd8f6`** (`v3-checkpoint-read-3ade2ce.md`): F1 must-fix ("every one of them in the narration, none in the rules" — false and self-contradicted, 3 sites) + F2/F3/F4 low + 4 observations. User dispositions same day: F1 as deletion, F2+F3 as fixes, F4 as fixture-first, all four in one batch → **`b953b3c`** (47+/22−, incl. closing the second entries' discharged flags — leaving them standing would have recreated F3 one entry later). That batch's own rule-1 read ran in an **independent review session** on the harness-generated dispatch (`rsc v3 dispatch --range f7bd8f6..b953b3c` — the ④ product's first governance use; range deliberately excludes the record commit per the 94a97f5-read precedent, records being provenance not instruction layer) → **CLEAN: 0 must-fix, 0 low, 5 observations none owing a fix**; record **`7417fba`** (`v3-checkpoint-read-b953b3c.md`); flags closed to pointer form **`1df6245`**. Both contracts now carry **no open owed-read flag**; the scope-discipline text may be relied on as it stands. Carried observations (no fix owed): **O1** — the `b953b3c` commit message's "a disposition the repository actually holds" overclaims (a repository holds the batch's own assertion, never the chat fact; reviewer marked it consistent-not-verified). That is the recurring authorization-evidence question, and the **user ruled on it 2026-07-26 (recorded here because it exists nowhere else): option (a), keep the current regime** — honest-form provenance assertions + review-contract §10 ceiling + independent reads; no user-signing mechanism; **not banked as a HarnessIssue**. Also carried: hunt-list item 8's mini-narration stays a candidate for the next instruction-layer batch (prior read's O2, this read's O4); untracked `ResearchSystem/docs/General-Harness-v2-Design.md` sits in the worktree unattributed by any session record here — left as found, ask the user before touching it. **NEXT (user re-confirmed at this close): ① opens in a NEW session** (`command_exit` subject-tree — the closed `LocalCheckSpec` kind union + `checks.py::_wrong_subject`), **then ⑤** (per-finding resolution in the VERIFY schema, consumed by the N2-A9 binding rule), each its own construction round on the versioned-successor pattern (signed bytes untouchable) — **then Stage 2 (P4-ACTIVATION-BRIDGE)**. At ①'s opening a **node-boundary cold read** of the instruction layer is owed per discipline rule 2 — **route-or-waive not yet ruled**; the cold-read charter template is in memory. Push debt re-derived at this close: **167** ahead of `origin/main`, user-gated. Working tree at close: clean except this file (left uncommitted per convention) and the untracked docs dir.

- **▶▶ RESUME HERE (2026-07-25 session close / preclear). Stage 1 of 4 is DONE and CLOSED; Stages 2–4 have NOT started.** The user's original request was a three-part programme (P3-CORR · P4-ACTIVATION-BRIDGE · P4 split into CODE+DOC) — **only P3-CORR ran**. Nothing is in flight, no background process, working tree clean apart from this file. **ISSUE_TRIAGE of the five banked HarnessIssues is DONE (`cc873e6`, 2026-07-25)** — routes: ① `command-exit-subject-tree` → `CORE_CANDIDATE`; ② `template-write-text-newline` → `WORKFLOW_FIX`; ③ `template-next-action-round-blind` → `WORKFLOW_FIX`; ④ `no-dispatch-generator` → `CORE_CANDIDATE`; ⑤ `no-vocabulary-for-repaired-blocker` → `CORE_CANDIDATE`. **AUTHORIZATION (user, 2026-07-25, recorded here because it exists nowhere else — FULL finding F5): all five issues are to be fixed BEFORE Stage 2 (P4-ACTIVATION-BRIDGE) opens, in the order ④ → ① → ⑤ after ②③.** The committed triage decisions predate that ruling and still say "No timing ruled at this triage" for ①④⑤; they are correct as of their own date and are deliberately not rewritten, so this line is the only record of the later schedule. **Status at tip: ②③④ DONE, ①⑤ NOT STARTED.** ②③ landed `2d5a646` (both defects probed directly: default `write_text` gives CRLF 2 / bare-LF 0, with `newline="\n"` gives 0 / 2; `next_action_for(0)`→FULL, `(1)`/`(2)`→VERIFY). ④ landed across `43ea599`…`0439efe` (`rsc v3 dispatch`, both modes) and its review-round fixes at `9956231`. **Next action = ① (`command_exit` cannot read the payload candidate) then ⑤ (no vocabulary for a repaired blocker)** — both touch signed schemas and are their own construction rounds — then Stage 2. Honesty note for a fresh session: a route says which **layer** owns a defect, not when it is fixed (contract §11 has no Retrospective machine and no automatic maintenance stage); the schedule above is the user's separate ruling, not something the routes carry. **User ruling 2026-07-26 (FULL finding F4): a template README is NOT instruction layer** — consistent with the execution contract's closed enumeration, which does not list it; moving that ruling into the enumeration itself would be an instruction-layer amendment owing its own rule-1 checkpoint read, and is not done here. Preclear residuals (low): ① I reported "push debt 135" once mid-session; the true count is **134** (122 at session start + 12 new commits) — re-derive rather than trust any number in prose; ② the six regression tests added at `a007f4f` include two that *look* like duplicates of the existing `VersionKeying` class but are not — they pin that `check_repair_decision`'s **call site** does not swallow a version error, and a probe confirmed `VersionKeying` stays green while those two go red when the call site is made to fall back; do not delete them as redundant; ③ branch `p3-corr-candidate` is merged and left in place (w1-r1 precedent), delete at will.

- **▶ ACTIVE (2026-07-25): wave 2's first real run subject CHOSEN — the research-agent-development reactivation program.** User approved ("ok", 2026-07-25) the 4-stage program **P3-CORR → P4-ACTIVATION-BRIDGE → P4-CODE → P4-DOC**; durable plan [`plans/research-agent-dev-p3corr-p4.plan.md`](../.goals/plans/research-agent-dev-p3corr-p4.plan.md). Delegated rulings locked: (a) Coverage Manifest re-approval **NOT needed** (manifest is count-free; revisit only if the recount reclassifies any of the 4 evidence-report files); (b) the BRIDGE runs as a **narrow harness run**. This realizes NEXT-item (1) below (wave 2's first real run). Live ToDo #1–#4 mirror the four stages. **Stage 1 (P3-CORR) EXECUTED 2026-07-25 to state `EVIDENCED`** — the run-v2 template's maiden real use. Instruction frozen `cb6bf7c`; WorkSpec v2 (10 units incl. the mapped normative preamble, 8 obligations, 11 checks) + coverage audit `COVERED` (fresh-context auditor) committed `5c88403`; user signed **START**; payload candidate **`640a28d`** on isolated branch `p3-corr-candidate` (2 files, `Thesis/**` never touched, main tree verified clean); evidence: **11/11 checks PASS**, manifest CONFORMANT, coverage clean, 8/8 obligations IMPLEMENTED. Corrected figures (re-derived at base through `git ls-tree`): ExperimentLab **110→51**, total **220→161**, `smoke-01` 55→1, `REPORT-r1-*` 5→4, out-of-scope ~78→11; Thesis 54 / Paper 39 / Knowledge 17 / PDF 35 were already correct. Ruling (a) **confirmed by observation** — the 4 evidence reports stay classified `evidence:` count 4, so **Coverage Manifest re-approval is NOT required**; §5 load-bearing set byte-untouched. **FULL RETURNED `CHANGES_REQUIRED` 2026-07-25** (independent session, user-routed, subject `4362572`): all 8 obligations **SUPPORTED** and every figure independently re-derived by the reviewer (161 / 54·51·39·17, the five ExperimentLab role rows an exact partition of 51, §5 byte-identical, manifest carries no counts, exactly 2 files changed) — but **1 blocking finding**: §4's *opening* sentence still read "Every one of the 220 scanned files", so the section opened at 220 and closed at 161 and asserted a role assignment over 59 files that do not exist. No obligation reached that line, which is why 11 checks passed over it. 6 non-blocking findings besides. **User accepted f1 + f3 + f5 + f6** (f2/f4/f7 declined). **REPAIR EXECUTED same day → candidate C2 `fe4c3bb`**: f1 per the reviewer's verbatim one-token fix; f6 the untrue present-tense "is banked as a HarnessIssue" restated as recorded-for-banking (schema admits one only after CLOSED); f5 **candidate half only** — §8d's attribution corrected (git addresses content and reads the candidate whatever is checked out; the real exclusion is the harness's own conservative `command_exit` subject-tree rule), while **the WorkSpec's own `review_only_rationale` carries the same inaccuracy and is NOT repaired — that needs a new WorkSpec revision + new START (V3-D7), carried forward**; f3 the four historical `220 md` sites in the plan each gained a supersession note rather than a rewritten number (reviewer's own second option; preserves what P2/P3 actually observed). Round-1 evidence fully regenerated: 11/11 PASS, boundary CONFORMANT, `check_subject` clean, `check_repair_regeneration_v2` clean (all three digests changed + new evidence commit). **VERIFY RETURNED `REVIEWED_NO_BLOCKER` 2026-07-25** (independent session, subject `8459c0d`; verify_scope = the 4 accepted findings + the whole repair diff + the permanent boundaries): all four repairs landed, and the reviewer re-derived every figure at **two** base revisions, re-executed all 11 checks, re-ran six deterministic suites and reproduced both mutation probes of the mid-run construction fix. **6 non-blocking findings**, of which two matter at FINAL: **v1** — the f3 condition is discharged at only **4 of 6** sites, because the FULL's enumeration was built from the phrase `220 md` and two further sites read `220 files` (executor reproduced: plan lines 352 and 615). The executor repaired exactly what the REPAIR decision authorized, so the shortfall is in the finding's enumeration, not the repair — but the repository now asserts 161 in the inventory and 220 un-noted in two places, and the repair budget is spent; **v2** — the committed state's `next_action` still says "route one FULL review" at `repair_round 1`, which `rsc v3 status` prints verbatim as the cold-resume instruction; root cause is the run-v2 template hard-coding it with no dependence on the round, so every future repair round inherits it. Also: **v5** flags for the record that the guard gating this run's repair (`check_repair_decision`) was fixed mid-run by the executing side — the reviewer found nothing wrong on the merits (it re-derived every figure in `a007f4f` and reproduced both probes) but notes the authorization of that construction round is not establishable from the repository. **AssuranceCandidate bound `7cdbdb3`, state `AWAITING_FINAL`, digest `d7d404ba…`.** N2-A9 forced f1 into `unresolved_finding_ids` (it counts every finding any bound review marked blocking, and the FULL is immutable; the controller has no vocabulary for "repaired" and must not invent one), so **three disclosures** carry the nuance: f1's listing is bookkeeping not a live defect, the f3 4-of-6 shortfall, and that the witnessed control-plane limitations exist only as prose until banked. **✅ STAGE 1 CLOSED — user FINAL 2026-07-25 = `ACCEPT_WITH_LIMITATIONS`.** Promotion merge **`2b52460`** brought the reviewed candidate `fe4c3bb` into the main tree preserving its identity (no cherry-pick rewrite); the main tree now states 161 with **zero residue** of the superseded total in the inventory. Five limitations recorded in `user-decision-final.json`: ① the two un-noted `220 files` sites; ② f7's Thesis-subsection figures; ③ the WorkSpec's uncorrected `review_only_rationale`; ④ the three-unit instruction-map omission that let f1 reach no obligation; ⑤ the mid-run repair of the guard gating this run (VERIFY found nothing wrong on the merits but the authorization is not establishable from the repo). AssuranceSummary clean, state **CLOSED**, cold resume verifies **all 13 pointers**. Closeout `4440fa2`. **▶ ISSUE_TRIAGE DONE `cc873e6` (2026-07-25)** — all five routed in one pass as the user ruled: ①④⑤ `CORE_CANDIDATE` (each needs its own construction round: ① the closed `LocalCheckSpec` kind union + `checks.py::_wrong_subject`; ④ the `rsc v3` CLI surface; ⑤ a per-finding resolution in the VERIFY schema consumed by the N2-A9 binding rule), ②③ `WORKFLOW_FIX` **with a user-ruled timing** — a template-maintenance round **before** Stage 2 opens, because Stage 2 is a narrow harness run on that same run-v2 template and would otherwise reproduce ② (the first evidence commit refused with `POINTER-STALE`) and inherit ③ (a cold-resume instruction to open a second FULL at `repair_round 1`). Timing lives in the decisions' `rationale` and nowhere else — the route enum cannot express it. `check_triage` clean 5/5, `rsc v3 status` resumable with 13/13 pointers, pytest 379 passed, audit exit 0; the five issue files and `state.json` are untouched per V3-D10 / N2-A11 and the w1-r1 precedent (`state.next_action` therefore still reads "…ISSUE_TRIAGE when routed" —既定形状, not a stale pointer). Recorder `run_triage.py` committed; it deviates from the w1-r1 recorder by validating all five before writing any. **▶ NEXT: ① then ⑤ — user ruled 2026-07-26 both are fixed in a NEW session — then Stage 2 (P4-ACTIVATION-BRIDGE)** (ToDo #2). **②③④ DONE and verified at tip** (② five `newline="\n"` sites + ③ `next_action_for` present in the template; ④ both dispatch modes exit 0). Review coverage, complete list: FULL of `4440fa2..0439efe` `PASS` 7 findings (record `be4e6e2`); targeted VERIFY of the F1/F2/F3/F6 fix round `PASS` 4 findings V1–V4 (record `96cedb5`); FULL of the deletion round `d55d5ce..c6d4eb4` `PASS` 4 findings G1–G4 (record `949bf58`); rule-1 checkpoint read of the contract amendment `1d25aae`, 6 findings C1–C6 (record `763ef2a`). **④'s final shape after the deletion + golden-file rounds**: a constant prompt with two substitutions, three one-git-call checks, output asserted equal to the committed fixture `tooling/tests/fixtures/expected-construction-prompt.txt`; the churn/count derivations, the partition guard and the AST meta-guard are all **deleted, not fixed** — the fixture removed the adjacent duplication that kept inviting the vacuous-guard rewire. **User ruling 2026-07-26: all dispatch-generator-related reviews CANCELLED** — the a65cca1 fix round's VERIFY, and any review of `389173b`/`e5c6005`/`df2b84d`; those commits are therefore **unreviewed by explicit ruling**, not by omission. **One review genuinely open (DISCHARGED 2026-07-26 — see the RESUME HERE bullet above): the contract corrective batches `e3c7446`+`3ade2ce` owe their checkpoint read** per their own provenance notes — rule 1 says no round may rely on the amended scope-discipline text until read, and the ①⑤ construction rounds would be the first to rely on it; the new session should get that read (or the user's waiver) before opening ①. Also still true: F7 — the run-v2 template fixes have no regression test, only probes; and `3ade2ce`'s provenance records that one earlier batch had claimed a user disposition that was never given (corrected in place). Push debt **162**, user-gated. **The five banked HarnessIssues** (schema admits them only after `CLOSED`): ① `command_exit` subject-tree rule excludes the counting/diffing check class — **and per the FULL, the exclusion is the harness's own conservative rule, not a git limitation**; ② the run-v2 template's `write_text` newline defect; ③ the same template's round-independent `next_action`; ④ no executor-side dispatch generator; ⑤ N2-A9 has no way to express a blocker resolved by repair, so every repaired run must list it and disclose around it. **Carried forward from this review, deliberately not fixed** (both are permanently recorded in the committed `review-full.json` at `8459c0d`, and the first also as live ToDo #6): **(i) f7 — the same defect class survives in §4's THESIS subsection** (`Intake/**/raw/* (4)` where the base holds 5; row total "~13" where its enumeration resolves to 15; reproduced by the executor. The partition is sound — 13+5+13+3+3+15+2 = 54 — so the root total and every coverage claim stand; only two row figures are wrong. R2 scoped this run to the ExperimentLab section, so it was out of authorization); **(ii) f2 — the WorkSpec's unit map omits three normative units** (the defect-statement paragraph, the scope-discipline paragraph, and the HarnessIssue clause), which is *why* f1 escaped all 11 checks and the COVERED coverage audit; a map defect cannot be repaired by editing the candidate, so it needs a future WorkSpec (or a run-v2 template that maps preamble-level paragraphs by construction — the same omission class was reported at w1-r1 and both N3 shadow runs); **(iii) f5's WorkSpec half** — the `review_only_rationale` still misattributes the counting limitation to git rather than to the harness's own `command_exit` subject-tree rule; **(iv) f4** — §8a does not exhaustively list every modification the candidate made (all verified correct, but a reader of §8a alone would not know they happened). **Three HarnessIssues witnessed, to be banked at run close** (`observed_after` only accepts CLOSED; **user ruled 2026-07-25 that all three are routed together at that ISSUE_TRIAGE, not fixed ad hoc mid-run**): ① `command_exit` cannot observe the payload candidate — it requires candidate==checkout HEAD, which the same-branch evidence-commit topology precludes, so the harness cannot re-derive counts itself (hence 1 review_only obligation + reviewer-established truth); ② the run-v2 template's evidence step wrote JSON via `write_text()` without `newline="\n"`, so on Windows (`core.autocrlf=true`) committed bytes ≠ digested bytes and `check_subject` correctly refused the first evidence commit `609b24b` with 4 × `POINTER-STALE` — fixed in the run-local copy, **the template itself still carries the defect**; ③ **no executor-side dispatch generator exists** — `rsc v3` offers `governance-scan/status/flow/disposition/review` only, and every dispatch to date (incl. `W2/W2-dispatch-*.md`) is hand-written, although every field is derivable from committed state (role from `status`, subject SHA + control root from `state.json`, output schema from the run's `schema_version`). The reviewer side has its cold entry (`read_control_plane`, "needs nothing but the SHA"); the executor side has no counterpart, so each dispatch carries avoidable anchoring risk and is neither reproducible nor digestible. Adding `rsc v3 dispatch` is a core change and would need its own construction round.

## Mandatory ResearchSystem control-plane interlock

- **▶▶ CURRENT STATE (2026-07-25 preclear): the migration AND the entire special-case-bucket
  programme (wave 1 + wave 2) are COMPLETE — wave 2 CLOSED, carrier signed (`ac1b383`), B1
  read DISCHARGED (`37ee713`); nothing open. The freshest detail is the W2 sub-bullets deeper
  in this block; the "▶ LIVE POINTER" headline immediately below is dated 2026-07-22 and is
  now HISTORY. Next = wave-2 first real run (user-gated). See the top-of-file 当前指针 for the
  next-steps list.**
- **▶ LIVE POINTER (updated 2026-07-22; V3-N4 closed 2026-07-21 evening) — read this
  headline for the migration state, then the 断点 sub-bullet below it for the current
  (2026-07-22) state; everything below this bullet is history.**
  **V3-N0 / N1 / N2 / N3 all CLOSED. N3 closed at its decision gate: the user ruled
  `ADOPT_DOCUMENT_V3` (2026-07-21)** after the revise round ran three shadow rounds — round 2
  exposed five review-layer defects (N3-R6/R7/R8 + the disposition split) → amendments 2+3
  (`eca4902` + `c07d682`, both externally checkpoint-reviewed; L1 history-leak in the dispatch
  prompts caught and fixed pre-dispatch) → round 3 clean on de-contaminated instructions:
  run-a1 `REVIEWED_NO_BLOCKER`+`INCOMPLETE`+disclosure, run-p3 `CHANGES_REQUIRED` with the
  P3-inventory count blocker independently reproduced a **fourth** time (N3-R3, user-owned).
  Residual register now N3-R1–R10; the three review-side notes are committed (`f01502f`).
  **V3-N4 CLOSED — the user confirmed the cutover 2026-07-21: v3 = the default assurance
  entry for document work** (`rsc v3 status`; pointer = rsc.py declaration +
  ResearchSystem/README.md line; rollback tested by reverse-patch, N4-A4) plus the C1/C2/C3
  instruction-prose fixes. **The v3 migration (N0 → N4) is complete** — candidate `1e6dde9`,
  closeout = the commit carrying this line.
  - **断点 / next step:** (1) the harness-contract discipline edit is **landed, reviewed,
    and repaired** — `94a97f5` `V3-CONTRACT-DISCIPLINE-AMENDMENT-v1` (+71/−0) → checkpoint
    read #1 (2026-07-22, findings F1–F4 + observations A/B) → **all four user dispositions
    taken same day** (F1–F3 fix boundary approved; F4 same-batch pointer-form; A informed
    approval, no text change; B deferred — **open item: the "each node boundary" referent
    is the user's to define at the next real boundary event**). Landed: `fdd2f9d`
    `V3-CHECKPOINT-READ-RECORD-94a97f5-v1` (reviewer report + dispositions, durable at
    `ResearchSystem/migration/document-work-assurance-v3/v3-checkpoint-read-94a97f5.md`)
    and `f6a7bf8` `V3-CONTRACT-DISCIPLINE-CHECKPOINT-FIX-v1` (21+/14−, all six finding
    sites; four suites green 404, audit exit 0). **Checkpoint read #2 DONE 2026-07-22**
    (same-reviewer continuation, contract read at parent `fdd2f9d`): all four fixes
    landed as prescribed, no new defect introduced, numstat 21/14 re-derived with zero
    out-of-site changes — **the two contracts now carry no unfixed finding**. Read #2
    reported 2 findings + 1 observation **against the record file `fdd2f9d`, not the
    contracts** (record = provenance, not instruction layer → no rule-1 re-read owed):
    R1 the record header's "reproduced verbatim" over-claim, R2 the six paste-truncation
    repairs mis-attributed to the reviewer (they were the dispatching side's pre-dispatch
    act), R3 the B-deferral pointer living only in the uncommitted LEDGER. **All three
    landed 2026-07-22 in the commit carrying this line** (record header → condensed-form
    wording with substance confirmed unaltered by read #2; appendix re-attributed; a
    "Checkpoint read #2" section appended to the record file; this LEDGER committed).
    (2) the 特例-bucket design round **ran its authoring step 2026-07-22**: proposal
    committed `88948b3` `V3-SPECIAL-CASE-BUCKET-DESIGN-v1`
    (`ResearchSystem/migration/document-work-assurance-v3/v3-special-case-bucket-design.md`)
    — (a) `review_only_rationale` + (b) `not_supported_condition` carried by a versioned
    successor schema `document-work-spec.v2.schema.json` (N0-signed v1 untouched; the
    `8efe3e9` amendment pattern cannot carry signed-schema changes), (c) commit-first
    ReviewPackage successor as **outline only** (N3-R9; N2-A1 re-satisfied by the
    successor's own acceptance, never amended), plus the two deferred visibility items
    (START-surface `review_only` ratio; `EXECUTION.md`/`REVIEW.md` prose batch);
    recommendation = two waves, (c) parked until wave 1's first real run. **The design's
    independent review ran 2026-07-22** (fresh-context reviewer, subject at `88948b3`):
    evidence fidelity / schema idiom / carrier mechanism / no-promise-raising / deferral
    coverage all verified solid; **8 findings (F1–F8), all fixed same day in the design
    revision — the commit carrying this line.** Highlights: F1 → §4 now names the v2
    version-discriminator fork (root `schema_version` const recommended vs run-state pin)
    and bans cross-version fallback; F2 → §6 corrected, wave 2 is
    **versioned-contract-successor** territory (invariant 9 + §4 topology + §8 step 7,
    not just N2-A1); F4 → §3 gains the strongest universal-side argument; F5 → rule-3
    citation deleted; full findings + resolutions in the doc's own §11 (condensed form).
    **§9 adjudicated 2026-07-22 — all six points per recommendation** (narrow scope ·
    `review_only_rationale`+`not_supported_when` · two waves + hunt item · wave-1
    authorized in the same adjudication · (c) parked · root `schema_version` const).
    **Wave 1 EXECUTED same day:** candidate `cabf539` `V3-W1-REVIEW-ONLY-FIELDS-CANDIDATE-v1`
    — `document-work-spec.v2.schema.json` (N0-signed v1 untouched), explicit version keying
    with **no cross-version fallback**, coverage-view mode-ratio line, 18 new tests (pytest
    334 green + compiler 29 + harness-v2 39 + stage-control 20 + fixture validators
    36/93/41), 3 mutation probes red-then-byte-verified-restored; acceptance matrix
    W1-A1..A7 + honesty ceilings in
    `ResearchSystem/migration/document-work-assurance-v3/W1/W1-record.md`. Prose batch
    `041cc1b` `V3-W1-PROSE-AMENDMENT-v1` (EXECUTION.md WorkSpec-author section + REVIEW.md
    `review_only` question, additive +48/0). **① and ② RAN 2026-07-22 in one
    fresh-context round** (reviewer re-derived everything; mutation work in an isolated
    copy, worktree untouched). Subject A (candidate review): every suite independently
    re-run green (334/29/39/20 + validators 36/93/41, audit 0), 7 changed paths ⊆
    allowlist, signed blobs byte-identical, v1→v2 delta exactly the declared three,
    golden +1 line, record's 3 mutation probes repeated + 5 added — all red; version
    keying has **no silent-validate path**. **3 findings:** **A1** explicit
    `"schema_version": null` silently keys to v1 (net still fail-closed via v1's closed
    root, but the W1-A3 matrix statement "anything else → SpecGap" is false for
    present-null and unpinned; min fix = distinguish present-null → SpecGap + test, or
    correct W1-A3 wording + pin test); **A2** the v2 unit-test fixture is symmetric
    (2-of-4, one check per row) so two semantic mutations (count inversion,
    check-total-vs-obligation-count) survive all unit tests — only the golden catches
    them (min fix = asymmetric fixture with a multi-check row); **A3** `review.py`'s
    "nine schemas / no later node may write `__init__`" comment is made stale by this
    candidate and W1-record §6 doesn't list it (min fix = record note; the comment
    itself waits for a round that owns the path). Subject B (checkpoint read of
    `041cc1b`): additive-only re-derived, all four cited figures match N3 §4.1, honesty
    boundary present, zero test movement. **4 findings:** **B1** (most severe) "review
    can only spend a `SUPPORTED` on it" contradicts REVIEW.md's "`UNVERIFIABLE` is the
    honest answer" discipline — the sentence teaches the banned collapse (min fix = "an
    empty `SUPPORTED` or an honest `UNVERIFIABLE` — neither of which tests anything");
    **B2** "dressing … is visible in the same ratio line" is factually overstated —
    dressing makes the line look *better*, and the new REVIEW.md question only audits
    `review_only` obligations so dressed ones escape it too (min fix = name the real
    catch-site — triviality of the bound check at review time — and drop "visible");
    **B3** new stage marker lacks the provenance parenthetical and the file header now
    under-describes content (next-batch item); **B4** the blocker-rule restatement
    omits "or the contract". **All seven findings independently re-verified by the
    executor and fixed same day inside the user-approved boundary (A1 as code fix — a
    present key is a declaration whatever its value):** `8e681f8`
    `V3-W1-REVIEW-ONLY-FIELDS-FIX-v1` (A1 `_ABSENT` sentinel + `None` negative + probe 4
    red-then-byte-verified-restored; A2 asymmetric fixture 1-of-4 with a two-check row;
    A3 + W1-record §3/§4/§6/§7 sync) and `7640709` `V3-W1-PROSE-AMENDMENT-FIX-v1` (B1
    `UNVERIFIABLE` correction; B2 real catch-site named, "visible" dropped; B3 marker
    provenance; B4 "or the contract"; header broadening deferred per reviewer routing).
    Suites re-run green (334). **Targeted VERIFY DONE 2026-07-22** (same reviewer;
    for `7640709` the VERIFY doubles as its rule-1 checkpoint read): **findings list
    EMPTY, no blocker** — all seven fixes landed as prescribed (A1 `_ABSENT` sentinel
    behaviour executed directly: absent→v1, "2"→v2, null→SpecGap; probe 4 re-done by the
    reviewer, exactly one test red; A2's two semantic mutants re-run and now killed at
    unit level; A3 record-note quotes match `review.py` verbatim; B1/B2/B3/B4 as
    prescribed, "if at all" honestly carries the accepted F4 risk); no new defect, both
    numstats re-derived with zero out-of-site changes (record edits enumerated as round
    sync); signed blobs byte-identical `417b55a`↔`7640709`, v1's 316 pre-existing tests
    untouched, all suites re-run green post-fix (334/29/39/20 + validators 36/93/41,
    audit 0). Mutation work in an isolated copy; worktree unpolluted. **Residual-hygiene
    batch RAN 2026-07-22 (user-authorized at catch-up):** `50d5480`
    `V3-W1-RESIDUAL-HYGIENE-v1` (review.py registry comment refreshed — ten schemas,
    node-vs-successor-round distinction, pointer to W1 record §6; §6 marked discharged +
    §7 log line) and `e9e06c1` `V3-W1-HEADER-AMENDMENT-v1` (EXECUTION.md header names
    the WorkSpec-author section; instruction-layer). **The batch's rule-1 checkpoint
    read RETURNED same day: `e9e06c1` clean — additive re-derived, named section + stage
    marker match, B3 fully discharged, no remainder; `50d5480` accurate (count
    re-derived, N2 reasoning preserved); one low non-blocking finding — the bare "ten"
    repeats the nine-count decay shape — FIXED same day as `2c8f8bd`
    `V3-W1-HYGIENE-READ-FIX-v1` (pinned "ten as of W1, 2026-07-22"; comment-only, no
    further read owed).** All suites green pre-commit both times (334/29/OK/20 +
    validators 36-OK/93/41 + N0 frozen 41/41, audit 0). User rulings at catch-up: A1 key confirmed
    ("declared but no value = mistake"); dressing dodge stays witness-first, handled by
    agent-work quality + human review of the review_only/local_check_and_review
    classification. **Sequencing ruled by the user at catch-up (2026-07-22):** the
    harness I/O boundary design round (backlog externalization — move long-term backlog
    OUT through a one-way interface: harness emits typed residuals at round close,
    WorkSpecs may cite backlog items, harness never reads the queue; ledger returns to
    thin-pointer charter so it stays replaceable) is **PARKED until after wave 2** —
    witnessed-case pool grows through wave 1's real run + wave 2, and wave 2 exercises
    the contract-successor machinery the backlog object would reuse. The "node boundary"
    referent ruling (read-#1 observation B) naturally lands **at wave-2 opening** — the
    next real boundary event, per the standing deferral; clarified to the user: the cold
    read is construction-side governance only (subject = the product instruction files;
    the product flow §8 never performs it — every product run's fresh-context reviewer
    already cold-reads structurally). **v2-mandate recommendation: land BEFORE wave 1's
    first real run** (one-line instruction amendment + rule-1 read; without it that run
    could legally author a v1 spec and bypass the new machinery) — drafted, still
    awaiting the user's explicit go ("make sense" not treated as approval).
    **WAVE-1 ROUND CLOSED — user sign-off 2026-07-22** ("wave 1 i sign off"; W1-record
    header → CLOSED + §7 final entry; closeout `00e8aeb`). **v2-mandate GO ruled same
    day** → landed as `a22cca0` `V3-WORKSPEC-V2-MANDATE-AMENDMENT-v1` (one additive
    paragraph in EXECUTION.md's WorkSpec-author section: newly authored WorkSpecs always
    declare `schema_version: "2"`; version-less = pre-wave-1 historical form only;
    wording-level, loader keying untouched). **Its rule-1 read RETURNED same day (fresh
    context): substance verified in full** (additive 7/0 single file; every mechanical
    claim re-derived true — v2-only fields, date-blind explicit keying with no upgrade
    path, supersession model consistent with contract §13); **3 non-blocking findings,
    user-approved routing executed same day in the corrective commit carrying this
    line:** F1 "stays valid" normative/mechanical double-read → "stays legitimate …
    (the loader itself is date-blind — absence still keys to v1)"; F2 unnamed
    catch-site → "nothing mechanical refuses it; it is caught, if at all, by whoever
    reads the spec before START" (both reviewer-prescribed wording); F3 (observation:
    the W1-record's "open at close" item lacked a back-reference) closed by committing
    this ledger — the GO + `a22cca0` line above is the durable back-reference; the
    CLOSED W1-record stays untouched. **The fix's verify-shaped read RETURNED same day:
    findings EMPTY** — F1/F2 landed verbatim (no residual mechanical-enforcement
    reading; catch-site clause accurate, "before START" is the only pre-reliance
    refusal point), double-em-dash parse converges to one meaning, numstat exact, the
    ledger entry fact-checked line by line, F3 judged sufficient per the original
    finding's own terms. One disclosed residual (user-approved shape, not a finding):
    W1-record §7's "Open at close" line carries no forward pointer — a reader of that
    file alone won't learn of the resolution; the ledger is the discovery path.
    **v2-mandate chain CLOSED: `a22cca0` → read (3 low) → `62db9ac` → verify empty.
    Wave 1's first real run is now fully unblocked** and remains the next
    witnessed-case source. **Then: wave 1's first real run is the
    next witnessed-case source**, and wave 2 (the commit-first successor) stays parked
    until after it —
    boundary-referent ruling due at wave-2 opening; the I/O-boundary design round
    parked until after wave 2. Durable detail: the W1 record +
    the design doc (§9/§11) + N3 record §8/§9 + the checkpoint-read record above.
    **[Superseded same day: w1-r1 ran and CLOSED — see the w1-r1 bullets below.]**
  - **Push debt: 91 commits ahead of `origin/main`** as of `56898b0`, measured 2026-07-22
    after the w1-r1 closeout (supersedes every earlier count in this file; re-derive with
    `git rev-list --count origin/main..HEAD`). Push is user-gated — no ruling yet.
  - Preclear note (2026-07-22): the v2-mandate chain's two reviewer reports have no
    record file — their substance is in this ledger + the commit messages; author a
    record from those summaries only if ever needed.
  - **w1-r1 IN FLIGHT (2026-07-22, executor session) — wave 1's first real run started.**
    Subject: design-chapter §2.1 (session-table lifecycle + uid hygiene), user-dispatched
    with an explicit isolation condition (payload candidate on an isolated branch rooted at
    `2bf8809`; main tree `Thesis/**` untouched; nothing promoted without FINAL ACCEPT).
    Control plane at `ResearchSystem/generated/document-assurance/runs/w1-r1/`: instruction
    frozen `cd5633d`; WorkSpec **v2** (8 obligations, 3 review_only each carrying both v2
    sentences — first real use of the wave-1 machinery) + resolved plan + COVERED coverage
    audit (fresh-context subagent auditor, declared-names ceiling disclosed) committed
    `2b59a3c`; state = **AUDITED**. Cold resume: `python ResearchSystem/tooling/rsc.py v3
    status --state ResearchSystem/generated/document-assurance/runs/w1-r1/control/state.json`.
    **START signed + execution DONE same day** (`start-w1-r1` recorded, binds plan
    `7d0abb03…` + audit `931597a8…`). Payload candidate **C = `8504093`** on isolated
    branch `w1-r1-candidate` (2 files: §2.1 prose + the two state cells; boundary
    CONFORMANT; main tree `Thesis/**` verified untouched by diff; worktree removed —
    the candidate lives only in git). Evidence committed `312481c`: 8/8 checks PASS,
    8/8 fulfillment claims with uniquely-resolving locators, coverage clean, frozen
    ReviewPackage **pkg-w1-r1, 19 members, digest `c2d70273…`**; state = **EVIDENCED**.
    One witnessed control-plane defect (freeze guard fired: check_result members shared
    the aggregate path, 8 collapsed to 1 — inherited from the shadow freeze template;
    fixed via per-result files; HarnessIssue candidate at run end, and the shadow
    round-2/3 freeze scripts likely carry the same latent defect).
    **FULL review RETURNED same day (independent session): `REVIEWED_NO_BLOCKER`, 8/8
    SUPPORTED** — 1 non-blocking finding (f1: the instruction preamble's isolation
    conditions were normative but unmapped in the WorkSpec unit map; conditions verified
    satisfied from pinned revisions; map defect, no repair requested; wave-2 template
    item) + 5 residual-uncertainty disclosures. ReviewResult custody-copied byte-exact
    (canonical `adf41bda…`), `check_review_result` re-run clean; controller bound
    **AssuranceCandidate `ac-w1-r1` digest `7b72c591…`** (references-only; empty
    unresolved set per reviewer's blocking:false; governance-scan honest skip) —
    committed `743a4f5`. **RUN CLOSED same day — FINAL = `ACCEPT_WITH_LIMITATIONS`**
    (user ruling: "keep as the draft, will have a look later"; two recorded
    limitations — ① workbench-draft only, user has NOT yet close-read §2.1, the section
    is not settled; ② **no thesis tracker may claim the engine design done — the engine
    remains the user's own careful design work**; STATUS/THESIS-MAP untouched by the
    whole run). Promotion executed as the one explicit recorded step: merge `0bc684c`
    brings candidate `8504093` into the main tree preserving the reviewed SHA.
    AssuranceSummary clean; state **CLOSED**, cold resume verifies all 12 pointers
    (review_ref re-pointed to bytes digest — the canonical-digest pointer committed at
    `743a4f5` was correctly refused by the resume guard). Closeout `56898b0`. **Three
    immutable HarnessIssues banked for wave 2, awaiting user ISSUE_TRIAGE whenever
    routed** (`runs/w1-r1/issues/`): freeze-template check-member path collapse;
    unmapped normative instruction preamble (authoring + coverage audit both passed it,
    FULL review caught it); pointer-digest-kind convention unnamed by the pointer API.
    Candidate branch `w1-r1-candidate` left in place (merged; delete at will).
    Run-shape conventions this run established (wave-2 template inherits): real-run
    control root = `ResearchSystem/generated/document-assurance/runs/<run-id>/`; one
    file per CheckResult in the package; state pointers carry BYTES digests.
    **Wave 1's first real run is COMPLETE end-to-end** — the v2 review_only machinery
    held in production use per the independent review.
  - **[Superseded 2026-07-22 by the wave-2 opening bullet below — wave 2 opened in the
    fresh executor session as prescribed.]** (2026-07-22 session close, /preclear): open
    WAVE 2 in a FRESH session. Wave 2 = the commit-first ReviewPackage successor —
    versioned-contract-successor territory (invariant 9 + §4 topology + §8 step 7). New
    session reads: `v3-special-case-bucket-design.md` (§6 wave-2 scope + the (c) outline,
    N3-R9) + `v3-harness-operating-contract.md` + this bullet. FIRST act at opening =
    obtain the user's "node boundary" referent ruling (checkpoint-read-#1 observation B,
    standing deferral). Witnessed-case pool for the design: `runs/w1-r1/issues/`
    (3 HarnessIssues) + the review's residual_uncertainty in
    `runs/w1-r1/evidence/review-full.json`.
  - **▶ 当前指针 — WAVE 2 OPENED (2026-07-22, executor session).** Opening acts all
    ruled and landed same day: **(1) boundary-referent ruling obtained** (closing
    checkpoint-read-#1 observation B): a node boundary = the **opening of each
    construction-side round** (wave / derivative round / future construction node); the
    rule-2 cold read is owed before that round's work relies on the instruction layer;
    product runs never perform it (construction-side governance only). Landed as
    additive amendment `e90243a` `V3-BOUNDARY-REFERENT-AMENDMENT-v1` (operating contract
    rule 2 12+/0−; review contract §12 10+/0−; provenance notes pointer-form) —
    **awaiting its rule-1 checkpoint read**, combined into one dispatch with the
    wave-2 opening **cold read** (whole instruction layer as subject — first application
    of the fresh referent rule; last whole-layer cold read was the 2026-07-21 custody
    note). Dispatch package handed to the user in-session; user routes to the concurrent
    review agent. **(2) ISSUE_TRIAGE of the 3 w1-r1 HarnessIssues ruled + recorded**
    `f4b7994` `V3-W1R1-ISSUE-TRIAGE-v1` (check_triage clean ×3; issues untouched per
    V3-D10): freeze-check-paths → **CORE_CANDIDATE** (absorbed into wave-2 scope; freeze
    layer re-homed, defect class dies with it; shadow scripts historical, not
    retro-fixed), unmapped-preamble → **WORKFLOW_FIX** (successor template maps
    preamble-level run conditions; wave-2 acceptance matrix), pointer-digest-kind →
    **CORE_CANDIDATE** (bytes-digest pointer convention pinned; wave-2 acceptance
    matrix). Route names are executor transcription of the user's rulings, surfaced for
    correction. **(3) design-doc authoring authorized** ("直接开工") — draft authored in
    the worktree but **NOT committed until the cold read returns** (the fresh referent
    rule's first application is kept clean: wave-2 work must not rely on the instruction
    layer before its opening cold read). Suites green pre-commit both commits (pytest
    334, golden 29/29, validators 36/93 + stage-control OK, N0 frozen 41/41, audit 0).
    **Same day, later: both reads RETURNED** (READ 1 on `e90243a`: 0 defects + 1
    observation — rule-1 debt discharged, the amendment may be relied on; READ 2 whole-layer
    cold read: 3 low + 3 observations, no must-fix — the referent rule's first application
    discharged). User approved **all six fixable sites** → corrective batch `979a983`
    `V3-W2-OPENING-COLD-READ-FIX-v1` (L1 "uncommitted" de-staled / L2 count pinned to three
    runs as of w1-r1 / L3 README + v2 schema row / O1 WorkSpec-author mention / O2 digest
    "in full" / R1-O1 "its subjects, not the instruction layer"; O3 verified-true, no
    change). Findings record committed `7cb0f6a` `v3-cold-read-e90243a.md` (condensed form
    + dispositions; ground truth for the batch's own read). **W2 design committed
    `8c77f1e`** `V3-W2-COMMIT-FIRST-DESIGN-v1` (`W2/W2-design.md`; hold honored — committed
    only after the cold read returned; four-site signed surface incl. the invariant-11
    "package" word F2 missed; tree-derived enumeration kills the authored-member-list
    class; acceptance draft W2-A1..A8; six §8 adjudication points). Push debt 97 as of
    `8c77f1e`; push user-gated, no ruling. **① RETURNED same day (verify-shaped,
    same-reviewer): all six fixes landed as prescribed, zero out-of-site, record
    transcription faithful — the rule-1 obligation on `979a983` is DISCHARGED, the
    instruction layer may be relied on in full.** Two non-blocking residuals routed same
    day: **F1 deferred-banked** (operating-contract provenance note owes a one-line entry
    for the `979a983` edit — rides the NEXT instruction-layer batch, per the reviewer's
    own minimum fix; wording banked in the record file §Verify-shaped read); **F2 fixed**
    in the record file (verbatim corrupted spans + dispatch-side originals replace the
    conjectural bracket-reconstruction; provenance layer, no read owed) — the commit
    carrying this line. **Next: awaiting ② (fresh-session independent review of design
    `8c77f1e`)** → fold findings → user adjudicates §8 → implementation behind its own
    explicit gate. **Third instruction batch landed `bf32d68`
    `V3-REPORT-FORMAT-AMENDMENT-v1`** (user-requested light add-on: review contract §13
    advisory report-format recommendation — binding elements stay in §4/§5.1/§10, a
    differently-shaped report violates nothing, product-side ReviewResult out of scope;
    + discharges banked F1 via the back-filled operating-contract provenance entry for
    `979a983`). Additive 26+/0− + 4+/0−, pytest 334 green. **Its checkpoint read RETURNED
    same day: additivity ✔, F1-discharge endorsed (back-fill parenthetical called a
    beneficial deviation), 1 low + 2 observations, no must-fix.** User approved F1+F2 →
    `47b1cb4` `V3-REPORT-FORMAT-READ-FIX-v1` (§13 point 2 "no fix owed" parenthetical;
    tier-vocabulary context sentence; F3 = pre-existing footer approximation, no fix owed
    per the reviewer's own finding). `bf32d68`'s rule-1 obligation discharged per user
    disposition; `47b1cb4` owes a tiny verify-shaped read that **rides the next natural
    dispatch** to the review session. **② RETURNED 2026-07-23 (fresh-context design
    review of `8c77f1e`): 2 must-fix + 4 low + 4 observations** — must-fix 1: §3.2 had no
    successor home for the two check classes git cannot replace (check_package identity
    cross-checks + package-coupled check_review_result verdict binding → V3-D5 reopened
    at the result layer); must-fix 2: same-branch topology left contract-§4 separation
    unchecked (no evidence-commit containment check). **All ten resolved same day in
    revision `3a12f04` `V3-W2-DESIGN-REVISION-v1`** (executor re-verified both must-fix
    against review.py/candidate.py first; §10 condensed findings table; W2-A9/A10 added;
    §3.6 version fork closed by W1 precedent with override note; carrier renamed
    `-v3-supersession-1`; SHA-1 digest-strength ceiling added; corrupted report spans
    disclosed, nothing invented). Revision NOT independently re-read (§9 ceiling; bucket
    precedent — user adjudicates §8 directly or routes a verify first). **User chose
    verify-first; the verify RETURNED 2026-07-23** (same-reviewer continuation): nine of
    ten resolutions no-fix-owed; one low residual (v1: `work_id`/`run_id` orphaned by the
    prescription itself — reviewer's own honesty note) + recovered near-miss content (v2)
    both landed in **second pass `19d1bf7` `V3-W2-DESIGN-VERIFY-FIX-v1`** (follows the
    verify's verbatim prescription; itself not re-read — proportionality, micro-verify
    available). **Rider on `47b1cb4` fully confirmed — that verify debt DISCHARGED.**
    Design now at `19d1bf7`. **§8 ADJUDICATED 2026-07-23 — all six points per
    recommendation** (same-branch evidence commits · package → subject binding +
    tree-derived enumeration · small successor carrier `-v3-supersession-1` · legacy
    pinned v1 no migration · **design signature does NOT authorize implementation** ·
    working names stand; §2 near-miss note retained). Recorded `d9c4b1e`
    `V3-W2-DESIGN-ADJUDICATED-v1` — the design is the implementation round's governing
    input. **Wave-2 DESIGN ROUND COMPLETE.** Full chain: `8c77f1e` (authored, commit held
    for the opening cold read) → fresh-context review (10 findings) → `3a12f04` revision
    → verify (9/10 no-fix-owed) → `19d1bf7` second pass → `d9c4b1e` adjudication.
    **Next: the W2 implementation round — BLOCKED until the user's own explicit go** (§8
    point 5; at go, executor derives the allowlist from W2-design §4, renders the
    preview card, and runs construction-node discipline candidate→FULL→fix→VERIFY→sign).
    Still open, user-gated: push ruling (**109** ahead as of `a9bdee6` — the sync commit
    could not count itself; re-derive always); user's own close read of §2.1.
  - **Session closed 2026-07-23 (/preclear).** Working tree clean (only the
    standing-ignored `ResearchSystem/docs/`); 17 commits this session
    (`e90243a`→`a9bdee6`), no read/verify debt open. Preclear residuals (recorded, all
    low): ① `19d1bf7` (verify second pass, verbatim-prescription) + `d9c4b1e`
    (adjudication record, provenance layer) are **not independently re-read** — declared
    in the design §9/§10; a micro-verify can ride the implementation round's opening if
    wanted; ② dispatch/report **relay paste-corruption occurred ×3** this session
    (checkpoint-#1 precedent, cold-read dispatch, design-review report) — each handled by
    minimal-interpretation + in-record verbatim disclosure (the F2-fix precedent);
    channel-level risk, consider one §13-adjacent sentence at a future instruction batch,
    not owed now; ③ the ISSUE_TRIAGE enum transcription (CORE_CANDIDATE ×2 /
    WORKFLOW_FIX) stands by surfaced-without-objection, never explicitly confirmed —
    recorded in `run_triage.py` + `f4b7994`; ④ full suite battery ran before
    `e90243a`/`f4b7994`; later prose-only commits ran pytest + the pre-commit audit hook
    (exit 0 every commit) — no binding force on prose either way, disclosed. 断点
    unchanged: **W2 implementation round, BLOCKED until the user's explicit go.**
  - **▶ 当前指针 — W2 IMPLEMENTATION ROUND: candidate authored, AWAITING INDEPENDENT FULL
    REVIEW (2026-07-23, executor session).** User gave the explicit go (design §8 point 5);
    preview card rendered + approved (allowlist derived from W2-design §4 + four in-round
    decisions D1–D4). Three commits: **`19cb882` `V3-W2-COMMIT-FIRST-CANDIDATE-v1`** (the
    implementation), **`3b50738` `V3-W2-PROSE-AMENDMENT-v1`** (instruction layer, additive
    9+/0− + 35+/0−, **its rule-1 checkpoint read is OWED before any run relies on it**), and
    **`eb3d7db` `V3-W2-PRE-SUBMISSION-CORRECTION-v1`**. Delivered: the **unsigned** carrier
    `contract/Document-Work-Assurance-Contract-v3-supersession-1.md` re-homing all four
    signed statements (S1 §4 topology line · S2 invariant 9 · S3 invariant 11 · S4 flow
    step 7), each signed text quoted and each successor stated in full; `review.v2.schema.json`
    binding `subject={evidence_commit,candidate_ref,base_revision,control_root,repair_round}`
    in place of `package_ref`, root `schema_version` const with **no cross-version fallback**,
    v1 `$defs` reused by `$ref`; two new sibling modules `review_subject.py` (559 — subject:
    tree-derived enumeration from the committed plan's `check_order`, identity cross-checks
    against the CandidateRecord read AT the evidence commit, containment of the evidence
    commit in the control root, `check_repair_regeneration_v2`) + `review_result_v2.py`
    (292 — verdict: version keying + `check_review_result_v2`, closing V3-D5 at the result
    layer); additive `assurance_state.pointer_to` making the bytes-digest pointer convention
    executable; `generated/document-assurance/templates/run-v2/` (same-branch evidence-commit
    topology + preamble-mapping authoring gate). **38 new tests** (W2-A1..A5, A7, A9, A10 +
    a both-module issue-code reachability sweep); **6 mutation probes all red**, restored
    byte-identical by SHA-256, never `git checkout --`. Suites: pytest **372**, golden 29/29,
    harness-v2 39/39, stage-control 20/20, validators 36/93/41 + the stage-control matrix,
    audit exit 0. Signed bytes untouched (`git diff` empty over contract / common / v1 spec /
    v1 review / plan). **Two executor-found defects fixed before review, both recorded:**
    (a) a W2-A4 test fixture that asserted the stale-pointer guard from a document whose
    canonical and bytes digests coincide (`{}`) — no mismatch existed to catch;
    (b) **`review_subject.py` shipped at 821 lines, over the <800 hard rule**, in the very
    round whose D1 rationale invokes that rule — nothing mechanical caught it (repo-audit's
    tripwire is Markdown-scoped) and the first count was taken with PowerShell
    `Measure-Object -Line`, which omits blank lines; corrected by the object split above and
    a witnessed-gap note (no Python line-count guard exists in this repo). **One declared
    deviation outside the allowlist** (W2-record §2): `test_fix_round_locks.py`'s package
    partition guard necessarily fails on any new module, so a `SUCCESSOR_ROUND_MODULES`
    classification was added rather than the guard weakened. **断点 / next: the user routes
    an independent FULL review — the subject is the corrected tip `eb3d7db`, NOT `19cb882`.**
    Then fix-boundary → VERIFY → user sign (the sign also signs the carrier, which is what
    makes the successor semantics govern; until then every run is package-bound). Durable
    detail: `W2/W2-record.md` (§2 boundary + deviation + D1–D4, §3 acceptance, §4 probes,
    §5 measurements, §6 ceilings, §7 log).
  - **FULL RETURNED + FIX LANDED (2026-07-24).** Independent FULL on `eb3d7db`:
    **0 must-fix — the implementation body and all ten acceptance items came back with zero
    defects found**; 4 low + 5 observations, every low a claim-precision defect in the record
    or the reachability test rather than in behaviour. The reviewer independently re-ran every
    suite, re-derived every figure, re-verified both signed blob hashes against their pins,
    matched the carrier's four quotations verbatim against the signed contract (grep confirms
    exactly four `package` sites = S1–S4), and ran nine self-built mutation probes, all red
    with byte-verified restoration. **All four reproduced by the executor, then fixed inside
    the user-approved boundary (3 files) as `f751358` `V3-W2-REVIEW-FIX-v1`:** **F1** the
    reachability sweep read 33 of 38 — `check_subject`'s identity table built its codes as
    `f"{CODE}-{code}"` from a loop variable, invisible to any source sweep; no silent surface
    existed (all five were asserted by hand) but a row added later would have carried no
    assertion obligation → codes moved into whole f-string literals (behaviour identical) +
    a test pinning the five + probe 7 reverting one row to prove that test can fail; **F2**
    the round-opening §7 entry had been edited in place in `eb3d7db` (hard rule 6) →
    corrected by **appending** an entry naming it, quoting each edit, separating the
    legitimate SHA back-fill, and pointing at `19cb882` for the pre-edit text — that entry
    also records that this very fix round re-worded the following entry before catching and
    reverting it; **F3** §5's unqualified "zero edits to any pre-existing assertion" →
    "outside the declared deviation"; **F4** deviation numstat +9/−3 → **+12/−3** (measured
    after the first of two edits and never re-taken — measure-last broken in the record, not
    in the code) and test count 37 → 39. Suites at the fix: pytest **373** (W2 file 39),
    golden 29/29, harness-v2 39/39, stage-control 20/20, validators 36/93/41 + matrix, audit
    0; signed bytes untouched across the whole round. Root cause shared with the design
    round's must-fix 1 and worth carrying forward: **an enumerated claim outrunning the
    mechanism that backs it** — both times caught by an independent read, neither by a test.
    **断点 / next: one combined dispatch, drafted at
    `ResearchSystem/migration/document-work-assurance-v3/W2/W2-dispatch-verify-and-read.md`
    and routed by the user 2026-07-24** — **Subject A** = targeted VERIFY of `f751358`
    (answerable for the accepted findings + the whole repair diff + the permanent
    boundaries; may return only `REVIEWED_NO_BLOCKER` or `SPEC_GAP`), **Subject B** = the
    still-owed rule-1 checkpoint read of the prose batch `3b50738` (until it returns no run
    may rely on that text — wave 2's first real run would be the first to). Reported
    separately, never merged. After both: user sign-off — **and that sign-off also signs the
    carrier, which is what makes the successor semantics govern; until then every run is
    package-bound.**
  - **VERIFY + prose read RETURNED, second cleanup LANDED (2026-07-24) — round is now
    review-complete, awaiting only the user's sign-off.** Subject A (VERIFY of `f751358`) =
    **`REVIEWED_NO_BLOCKER`** (four fixes effective, whole repair diff + boundaries clean).
    Subject B (rule-1 read of prose `3b50738`) = clean, additive, scoping holds, three-way
    consistent with implementation + carrier. Both surfaced 3 non-blocking low findings, all
    handled in a user-approved second cleanup: **A1** the fix-round's F2 correction entry had
    claimed to quote each edit to entry 1 but named four of six — and the enumeration was
    *unnecessary*; fixed **not by completing the list but by dropping the claim** — an
    appended §7 entry supersedes it, marks the enumeration illustrative-never-complete, and
    sets the standing rule: *an append-only correction states the nature/reason of an in-place
    edit and points at the diff for the exact bytes, never hand-enumerates them as
    authoritative* (the git diff is the canonical fact, a hand-list is an N0-A6 second copy
    that drifts — this was the same defect class a **third** time, inside the entry that named
    it). **A2** the `## 4a.` heading collided with entry 1's `(§4a)` item ref → renamed
    un-numbered (`4b` also collides with §4 item (b)); the one dispatch reference updated.
    **B1** REVIEW.md successor section had dropped the "in full" qualifier the v1 custody-chain
    bullet carries (abbreviated SHA = git default, the O2 lesson) → restored. Commits:
    `6f7b2dc` `V3-W2-PROSE-INFULL-AMENDMENT-v1` (B1, instruction-layer — **owes its own rule-1
    read before any run relies on it**, rides the next dispatch; nothing relies on it yet) +
    `8a165bc` `V3-W2-REVIEW-FIX-v2` (A1/A2, record + dispatch). Cleanup is prose-only (no code/
    schema/test/fixture/golden touched) → suites & probes unaffected since `f751358`; pytest
    re-run 373, audit exit 0 each commit; signed bytes untouched across the whole round.
    **断点 / next: the user's sign-off — that signature also signs the carrier
    `Document-Work-Assurance-Contract-v3-supersession-1.md`, which is what makes the successor
    (commit-bound) semantics govern; until it is signed every run stays package-bound. After
    sign-off, one durable debt remains: the B1 prose amendment's rule-1 checkpoint read, to
    ride the next natural dispatch. Then wave 2's first real run becomes the next
    witnessed-case source; the I/O-boundary design round stays parked until after it.**
  - **✅ WAVE-2 IMPLEMENTATION ROUND CLOSED — user sign-off 2026-07-24 ("签字"), carrier
    signed.** The sign-off closed the round and signed
    `Document-Work-Assurance-Contract-v3-supersession-1.md`; per the carrier's own §5 the
    signature is recorded in W2-record §7, never in the carrier's bytes, so the carrier is
    byte-untouched and the signed object = the reviewed one. **Signed carrier git blob
    `68031fa2…`, byte-identical since candidate `19cb882` (`git log 19cb882..HEAD` over the
    carrier is empty), sha256 `c3925b5a…`; signed at the reviewed+cleaned tip `6b43057`;
    closeout `ac1b383`.** Effect: the four supersessions S1–S4 + the version boundary now
    **govern** — commit-bound successor semantics apply to newly opened runs, package-bound
    is pre-wave-2 history. The carrier header's "UNSIGNED" line is an authoring residue left
    unedited (N0 §8 precedent) so the signed blob stays put. **The whole special-case-bucket
    programme (wave 1 + wave 2) is now COMPLETE.** **B1 rule-1 read DISCHARGED 2026-07-25** (independent reviewer,
    user-routed; subject `6f7b2dc`; verdict clean, no fix owed; the amendment may now be
    relied upon) — **the programme's one carried debt is cleared; nothing in wave 1 + wave 2
    remains open.** ▶ **NEXT (all user-gated, nothing running): (1) wave 2's first real run**
    is the next witnessed-case source (now fully unblocked — would legally author a v2
    subject; it doubles as the first shakedown of the never-run `run-v2` template, so expect
    HarnessIssues à la w1-r1; its subject is real document/thesis content = user-owned, user
    picks it; executor renders a full preview card before opening). **(2)** the I/O-boundary
    design round stays PARKED until after that first run (standing sequencing ruling —
    witnessed-case pool + machinery reuse). **(3)** push debt now **122** ahead of
    `origin/main` at `16f0aad` (`git rev-list --count origin/main..HEAD`; re-derive), still
    user-gated — no push ruling yet. Durable detail: `W2/W2-record.md` (§7 sign-off +
    discharge entries).

- **Superseded live pointer (2026-07-21 morning) — history.**
  **V3-N0 / N1 / N2 all CLOSED and user-signed. V3-N3's shadow runs are executed and committed;
  the node is OPEN and unsigned, and the adoption decision has NOT been taken** — the user is
  adjudicating it separately and has indicated `REVISE_V3`.
  - **断点 / next step:** read
    [`plans/document-work-assurance-v3-revise.plan.md`](document-harness/plans/document-work-assurance-v3-revise.plan.md)
    (committed `6bad2b5`, self-contained for a cold session), then
    `ResearchSystem/migration/document-work-assurance-v3/N3/N3-record.md`. Step 1 of that plan is
    to re-check the actual adoption ruling before doing anything.
  - **`N3-A5` settled 2026-07-21 after two user challenges** (N3 record §4.2, §8, N3-R5).
    Its first half — what the START decision surface actually contains — was already observed in
    run 1 and merely unrecorded: **13 obligations + 1 declared exception reached the user; none
    of the 94% generated control volume did.** Its second half — whether a human engages with
    that surface under real stakes — is a **permanent boundary**, unreachable by any shadow run,
    and the first real use is its own observation. **No live run is needed; P6 stays where it
    is.** `N3-A1`/`A2`/`A4`/`A6` remain unstated but do not block: plan §8 gives N3 a *decision*
    gate, not a signature.
  - Commits this session: `0ba649c` → `23ac473` → `655bae5` (N2 closed) → `8e863c5` → `00c78fd`
    → `00963e4` → `6bad2b5`.
  - Still uncommitted by design: two review-side notes at the migration root
    (`v3-review-note-obligation-authoring.md`, `v3-review-handoff-2026-07-21.md`) — committing
    them is the execution side's act but the user routes.
  - **Push debt: 49 commits ahead of `origin/main`** (`git rev-list --count origin/main..HEAD`,
    measured 2026-07-21). This supersedes both the "31" and the "40" figures below, which were
    mutually inconsistent and stale.
  - Open user rulings carried forward: the adoption decision; the **P3-inventory count defect**
    (claims ExperimentLab holds 110 in-scope Markdown files; the base commit holds 51 — real
    committed project data, outside every v3 node's allowlist); N2-R2 stale README line; N2-R5
    two test files over 800 lines; N2-R7 the V3-N2 VERIFY report is not in the repository.

- **ACTIVE control-plane roadmap — Document Work Assurance Harness v3:** follow only
  [`plans/document-work-assurance-harness-v3.plan.md`](document-harness/plans/document-work-assurance-harness-v3.plan.md)
  (**user-approved 2026-07-20**; approval binds plan SHA-256 `9B08CD00…F171F`, committed byte-exact as
  blob `8ad404b` in `V3-PLAN-BOUNDARY-v1` = `ebbc304`). The v2 plan
  [`plans/general-harness-v2-architecture-revision.plan.md`](document-harness/plans/general-harness-v2-architecture-revision.plan.md)
  is **SUPERSEDED/historical** (banner + pointer updated): A1–A4 closed and immutable (A4 accepted at
  fix `f91a7c4`, closeout `de39b3d`); **A5–A7 and cutover are parked**: they never started and do not
  continue automatically; resuming requires explicit user authorization. v3 executes on branch
  `document-work-assurance-v3`, rooted at accepted A3 closeout `7db177d` — A4 is deliberately NOT the
  physical base (reachable source material only; reuse governed by the N0 record §4 reuse decisions).
  **V3-N0 is CLOSED — signed off by the user 2026-07-20** (FULL `CHANGES_REQUIRED` → bounded 3-file
  fix `85742ae` → VERIFY `PASS`, user re-ran all three checks himself). Delivered: **Contract v3
  — SIGNED 2026-07-20.** Signed blob `b2dbdf752d8c155e4c65b14b5f420b880b8184a1`, identical at
  `9237960` / `85742ae` / `9bda771`, so the reviewed object and the signed object are the same bytes;
  the signature lives in N0 record §8, never in the contract's own bytes (its frontmatter `status:`
  is an authoring residue — see the §8 errata and residual R4). Plus 7 `document-assurance-v3`
  schemas + [N0 record](migration/document-work-assurance-v3/N0/N0-record.md)
  (plan binding / A4 disposition / 5 reuse decisions / field traceability / §9 residuals) + 41/41
  contract fixtures. Commits: `ebbc304` → `9237960` → `85742ae` →
  `V3-N0-ADMINISTRATIVE-CLOSEOUT-v1` (the closeout carrying this pointer — a commit cannot contain
  its own SHA; find it as the branch tip).
  **V3-N1 is CLOSED — signed off by the user 2026-07-20** (candidate `74e8154` → pre-submission
  correction `c5d5535` → **independent FULL `PASS`** → fix `802e16a` → **targeted VERIFY `PASS`** →
  closeout `e4ad88e`). Budget fully spent: FULL 1/1, fix 1/1, VERIFY 1/1. Delivered: the
  obligation-to-evidence vertical slice — 2 schemas (`local-check-spec`, `candidate-record`),
  9 `rsclib/document_harness/` modules, 113-test acceptance matrix, `rsc v3 governance-scan`
  + blob-keyed grandfather register. All 11 acceptance IDs verified independently; N0 residuals
  **R1/R3/R4 discharged at N1** (R4's fail-closed behaviour was empirically tested — one byte added
  to the contract makes the exemption evaporate); ~~**R2 → V3-N2** (`N2-A7`) still open~~ —
  **superseded 2026-07-21: N0-R2 was discharged at V3-N2** (N2 record §4).
  ~~**⚠ 断点 = V3-N2 is NOT yet authorized.**~~ **Superseded 2026-07-21 — V3-N2 and V3-N3 are both
  past. See the 2026-07-21 block at the top of this interlock for the live pointer.** The text
  below is left standing as history. N1's own four carried-forward
  residuals are in [N1 record §10](migration/document-work-assurance-v3/N1/N1-record.md):
  N1-R1 + N1-R2 → V3-N2; **N1-R3 and N1-R4 are permanent endpoints, not debt — do not schedule work
  against them.**
  **N1 record errata — CORRECTED `220bf6b` (`V3-N1-RECORD-ERRATA-v1`).** The closed record had
  stated the targeted VERIFY "was available and was not used" and that the F1/F2 fix was never
  independently verified; both were false — an independent targeted VERIFY of `802e16a` was
  performed and returned `PASS` (all three new guards mutation-tested, both fixes probed, whole
  repair diff + permanent boundaries checked, every suite re-run by the reviewer). The result had
  not reached the execution session when the closeout was written. Corrected by the record's own
  rules, never by rewriting: §9 errata naming the superseded entry, §10 N1-R1 sharpened to
  **DISCHARGED**, forward pointer added to the closing box (whose wrong text stands, as with every
  other superseded claim here). **V3-N2 must not re-verify `check_audit` / `resume` on the premise
  that no review covered them.**
  Original S3, P4, cutover remain blocked; `P4-IMPL-v1` remains `approved / effective=false`.
  Untracked `ResearchSystem/docs/General-Harness-v2-Design.md` stays ignored (user ruling).
  **Agent operating contracts — LANDED `c0664f4` (`V3-AGENT-CONTRACTS-v1`).** Both sides now have a
  written contract at `ResearchSystem/migration/document-work-assurance-v3/v3-harness-{operating,review}-contract.md`,
  each referencing the other, **outside every node's `N<n>/**` allowlist** so neither can be modified
  inside a node candidate. The execution contract was authored by the execution session as a Claude
  memory atom and relocated here; the review side then applied six changes (two factual corrections —
  the `.goals/LEDGER.md` rule was wrong for N0/N4, the section numbers were hard-coded to N1 — plus
  four gap fills), all listed in the file's own provenance note. A cold session finds them via the
  memory pointer `v3-harness-operating-contract`, rewritten from a full copy to a pointer with the
  `MEMORY.md` index line updated — **those two memory-side edits are outside git and have no version
  history**; the relocated text itself is preserved verbatim in the repo file.
  **Two divergent unpushed lines** (push user-gated, re-measured 2026-07-20 at `220bf6b`):
  v3 `document-work-assurance-v3` = ~~**40 commits**~~ **49 as of 2026-07-21** ahead of `origin/main`; v2
  `codex/research-system-stage-control-refactor` @ `de39b3d` = **31**; they share 28 commits up to
  `7db177d`.

- **Gate G0 complete (2026-07-18; authoritative current override):** governance base
  `5ca6cc1cbf4ba0694130704d7aaf0e5c16fca71c`; A1 is signed; reviewed pre-sign
  SHA-256 `5E21899E33D1EE118B967F94F84BB202B972CAC7556B802415996EDFA2005EE2` was independently
  `SIGNABLE`; signed A1 SHA-256 is
  `2D672D0D329E845CC598FF6089B3FA460118C382A66CB67635C910652E23F04C`.
  `P4-IMPL-v1 approval_status=approved`, `effective_at=null`; implementation remains forbidden.
  Signed A1, abandoned/parked history and governing plans/handoff are now Git-protected. S0 completed
  the WIP snapshot and clean-baseline transition and the user confirmed its stop gate. S1 and S2 are
  now historical v1 boundaries; (superseded 2026-07-20: the "simplified A1 replan" next action is
  long done — see the A1–A4 CLOSED update in the block above; resume = await explicit A5
  authorization).

---

## 待办 backlog — harness 侧（2026-07-27 从 `.goals/LEDGER.md` 原样搬入）

- **ResearchSystem + long-lived ResearchAgent integration** (plan: [`plans/research-system-agent-integration.plan.md`](../.goals/plans/research-system-agent-integration.plan.md); phase-gated P0–P14; does **not** replace the thesis-writing pointer). **P0 EXECUTED 2026-07-12** (`/lite-execute`, stage-by-stage mode): frozen contract + baseline + home scaffold written under `ResearchSystem/` (contract freezes D1–D6 + executable interpretation; baseline records base `a09513c` / audit exit 0 / counts / ID namespaces / state owners; block-grammar + content-roots.yaml + handoff template + P0→P1 allowlist). Change surface = `ResearchSystem/` only; **no thesis content touched**; repo-audit **exit 0** (scope 169→179 md). Uncommitted (P0 = one planning/baseline commit, user-gated). **P1 EXECUTED 2026-07-12** (same session): P0 signed off (contract §4); P1 froze Protocol v1 — `schema/object.schema.json` (envelope + per-type + D3 epistemic matrix + load-bearing/evidence rules) + `persisted-index.schema.json` (closed allowlist, `additionalProperties:false`) + `coverage-manifest.schema.json` + `contract/adapter-map.md` (legacy T/B·W/A·bnd·dr·frag·lab mapping; **`SC` namespace dropped/folded into `evidence:`+`rel:`**) + 36 seeded fixtures. `python ResearchSystem/schema/fixtures/validate_fixtures.py` → **36/36, exit 0** (every P1 acceptance item has a passing test). repo-audit **exit 0**. Still `ResearchSystem/`-only, no thesis content touched. **P2 EXECUTED 2026-07-12** (`/lite-execute`, same plan): built the Markdown→JSON compiler + shadow lint under `ResearchSystem/tooling/` (`rsc.py` + `rsclib/` 10 modules) — G1–G8 anti-harvest fence parser, 15-code stable lint, `inventory`/`compile`/`compile --check` modes, projection to the persisted allowlist, generated `object-index`/`relation-graph`/`coverage` views. **Golden tests 29/29 (exit 0)**; real-content run = 220 md, **0 live objects / 0 diagnostics** (shadow — objects are authored in P4/P5); delete+rebuild **byte-identical** (sha256 OK); `compile --check` fresh; repo-audit **exit 0**; canonical Markdown provably unchanged. Change surface = `ResearchSystem/tooling/` + `ResearchSystem/generated/` only. **P3 EXECUTED 2026-07-12** (`/lite-execute`, same plan): the one-time full inventory is authored + frozen under `ResearchSystem/inventory/` — `P3-inventory.md` (baseline `90deba7`; **220 md 100%-accounted** by 6-bucket rules; object inventory by namespace: tb 11 · bnd 8 · wa 26 · gap 3 · paper 37 · evidence 4 · atom 5 · dr 20 · decision 24 · frag 63), `dependency-baseline.md` (direct edges only; hashing→P6), `coverage-manifest.json` (**14-Claim load-bearing set FROZEN** + 3 Gaps via `coverage_manifest_ref`; schema-VALID; `approved_by: user (Melclycj)`). **User gate PASSED 2026-07-12** ("approve as-is"; boundary B1–B8 fold into Claims; RQ1 model admitted `evidence-insufficient`+`blocker`; RQs = the 3 contribution Claims). golden **29/29**, `compile --check` fresh, repo-audit **exit 0**, manifest schema-VALID; change surface = `ResearchSystem/` only, **no thesis content touched**. Accepted deviation: manifest `--manifest` default not wired until P5B (`claim_ref`s minted then). **P4 EXECUTED 2026-07-12** (`/lite-execute`, same plan): the one vertical pilot — chain **Gap `gap:agent-identity-adversarial` → Claim `claim:liveness-far-contrast` → Evidence `evidence:far-contrast` + ClaimEvidence `rel:liveness-far-contrast`** authored as 4 additive `research-object` blocks (first writes into `Thesis/**`+`ExperimentLab/**`; **no prose rewrite**). Verified: 4 live / 0 diag, golden **29/29**, `compile --check` fresh, manifest spot-check 13-expected-dangling + authored Claim resolves, repo-audit **exit 0**, delete+rebuild **byte-identical**, 0 content fields in persisted projection. **Post-review fix (2026-07-12, user adversarial review):** corrected a wrong `spec_hash 4ec90d7cfb89` (that hash = GuardAgent `r3_guard_defense.py`, NOT the binding lab, per its `run.json`) → real artifacts `binding_far_contrast.py` + `results-binding-far-contrast.json` (self_check GREEN); **tightened `object.schema.json`** (locator requires anchor; Gap requires partial_coverage+refuting_prior_art; ClaimEvidence requires polarity/applicability/conditions/verification_ref) as a **pre-commit v1 correction** (fixtures 39/39, golden 29/29); Gap gained `#relationship-to-agent-identity` anchor + refuting_prior_art + coverage-honest wording. **Second review fix (2026-07-12):** anchor now required non-empty in 3 layers (locator+envelope+persisted; `model.py` injects effective anchor); ClaimEvidence `origin` required; **projector fixed** — the generated index was carrying only node coordinates, now it carries the full argument semantics (ClaimEvidence relation/conditions/verification; Claim load_bearing/statement-ref; Gap sources/novelty/refuting_prior_art) while still forbidding content bodies (3 new `projection:` golden tests); Gap prior-art restructured (bearer→RFC 6750 arm1; Pirch moved to a supports-source; SPIFFE added as structured `limits` near-miss + falsification). Re-verified: fixtures **45/45**, golden **32/32**, delete+rebuild byte-identical, 0 forbidden fields in JSON, repo-audit exit 0. Change surface now 17 tracked files. (Manifest `--manifest` enforcement intentionally unwired until P5B → 13-expected-dangling; Obsidian visual not independently verified.) **P4 user format gate PENDING → uncommitted** (per `ResearchSystem/handoffs/P4-to-P5.md` — **parked 2026-07-17, non-authoritative; see the REOPENED entry below**). Deviation: Gap's lit-review source dropped as redundant per user (single Pirch `survey` source); unrelated user WIP in `sota-comparison.md` left untouched, excluded from P4 surface. **P4 REOPENED (2026-07-17, user ruling — amendment split):** the four review rounds traced to one root cause — the fix-amendment had swollen into a monolith (P4 format + P5 Ref/type freeze + P6 hash/stale + Gap research in one doc, revised as prose patches). Monolith **abandoned** (parked with a split map); `P4-to-P5.md` parked as non-authoritative. **当前指针 for this plan:** NEW SESSION authors **`A1 — P4-scoped, rev1`** (only the 5 pilot objects / 4 types, as executable artifacts) per the authoritative contract **`ResearchSystem/handoffs/P4-reopen-2026-07-17.md`** (allowlists / locked rulings / OPEN items / read order) → user signs → implement → stop at the P4 format gate. Pre-refactor **payload** snapshot: stash commit `91b819da6abf03fd97ba54cfc659a7413ce23521` (P4 WIP + then-untracked monolith/handoff as of BEFORE the refactor; applied, kept, not popped; restore via the immutable SHA — **not** a full session-close snapshot: excludes the reopen handoff, park banners and pointer edits). Commits: **P0/P1/P2** (`1c8bb3d`, `bd37b9e`, `f2c5993`), **P3** (`244e057`); **P4 uncommitted (reopened)**. **当前指针 (2026-07-18): P4 / contract-authoring under Scope Firewall `P4-CF-v1`.** `A1 — P4-scoped, rev1` is authored — sole output `ResearchSystem/contract/amendments/2026-07-18-a1-p4-scoped.md` — and hardened through **6 Codex rounds** (R5 `SIGNABLE`; **R6 user-directed → NOT SIGNABLE / 2 fixed**) + **2 user bounded audits** (3 + 6 fixes) — every finding fixed in A1, plus the user's final 5 OPEN adjudications applied (child ID → `gap:per-use-same-host-caller-binding`; child proposition = final post-theft-replay wording; two-enum `origin_mode`; child owner `scope-and-boundary.md`; coverage→P6). **The post-audit text is NOT yet independently re-reviewed** (≤5-round cap governs autonomous Codex rounds; R6 was a user-directed exception) → **A1 SIGNED 2026-07-18** (user Melclycj; status `approved-pending`): the signature approved the contract, set `P4-IMPL-v1 approval_status=approved` / `effective_at=null` (`effective=false`), and PASSED the child Gap `gap:per-use-same-host-caller-binding` P3 inventory gate — it did **NOT** authorize implementation or constitute P4 format acceptance. **Implementation NOT started; blocked until a later control-plane-refactor Stage Record activates `P4-IMPL-v1`** (that Stage Record is the sole activation owner). Signed A1 + this pointer are uncommitted (governance-boundary commit is user-gated; contains no implementation). **Do NOT implement** (implementation is the separate later `P4-IMPL-v1` firewall inside the amendment, still ending at the P4 format-acceptance gate; signing A1 also = the child Gap's P3 inventory gate, NOT P4 format acceptance). High-level phase state lives in the plan; precise scope / closure / active-firewall values live in the P4 reopen handoff + `P4-CF-v1`.
- Push debt: **superseded 2026-07-21 → 49 commits** ahead of `origin/main` on v3
  `document-work-assurance-v3`; v2 `codex/research-system-stage-control-refactor` @ `de39b3d`
  unchanged at 31; they share 28 commits up to `7db177d`. Push is user-gated. (The "31" here and
  the "40" in the interlock were two mutually inconsistent stale counts — that inconsistency was

---

## 2026-08-17 · 自 `HARNESS-LEDGER.md` §当前指针搬入：「已裁但只存在于对话里的」十条

搬入判据是该账本自己的规矩「supersede = 搬走，不是贴标签」：下列各条**已由别处说话**（指令层
正文 / 已签载体 / 决策簿条目），或是**一次性且已消耗**，故不再占用 live pointer 的行数。原文
逐字照搬，未改写。仍留在 ledger 的六条见该文件同一 bullet。

- **digest 收窄到 5 个保护字段（不删）** —— 已由 supersession-2 的签字文本与 run-v2 README 的
  `DIGEST_PROTECTED_FIELDS` 段承载。
- **`E2` 对签名文本的 override 由 C1.5 承担、C1.6 的 supersession-2 只管今后** —— C1.5 / C1.6 均已
  CLOSED，承载在 supersession-2 的签字文本。
- **`E2` 收敛为 3 blob + schema pack，未列即不冻，本 harness 不管的签名件一律出圈**（含 3 份已签
  文件，反转 `f054a08` 方向）—— 已落进 `E2` 正文（「Three blobs and one directory」）。
- **`O-2` 交换照收、不在 harness 自身治理上多花时间** —— 一次性态度裁决，无今后援引面。
- **`O-C` 不加规则**（根因是 `E3` 被破，非 `E8` 缺条款）—— 一次性，根因已记在该轮记录。
- **`O-3` 三文件不保护** —— 一次性。
- **`E10-D-NARROWING`（2026-08-04）「read 与 FULL 成本近似」那条定性观察已由实测接手**
  （`HI-REDEEM-5`，2026-08-07）：FULL 252k tokens / 25.5 分，targeted VERIFY 208k / 23.8 分 =
  **83%**——主体小三分之二而只省 17%，故 retro §7 ruling 2 的诚实边界**已关**（n=1、token 口径
  未验证；广度确实减半，省下的被「读 FULL 记录 + 同一套电池 + 每项挖更深」吃掉）。已结。
- **L3（2026-08-04 设计轮 FULL）**：`22b27aa` 正文自述「非 doc-only」有误——BATTERY-TIERING 判据是
  路径类型+树位置、无指令层项，那批实为 doc-only 且已跑该档检查，无漏跑；风险仅在先例，勿引作跳
  电池依据。—— 一次性更正，可由 `22b27aa` 与该轮 FULL 记录反推。
- **松冻结裁决（2026-08-04，设计轮 VERIFY 的 V-2 要求落此）**：为改正
  `paragraph-map.schema.json` 自述「不在冻结面内」这一处**永久边界**假陈述，用户裁定**只为该文件、
  只此一次**重开 `E2` 冻结（`O-2b` 同款形状）；冻结面其余不动，pack 仍 15 件。—— one-shot 已消耗。
- **`E2` 动词换掉、第三出路入正文（2026-08-04，`E2-VERB-E10-PIN` 轮 FULL 的 L-1 落此）**：用户批准
  把 `E2` 动词由 untouchable 改为「不得无裁决写入」，菜单句同批补第三分支。**本条取代此前「第三
  出路不写进正文」那条裁决**——那次的前提是保留 untouchable、只问要不要另加例外；动词一换，「拿
  裁决后写入」就不是例外而是唯一常规路径，前提消失。—— 已落进 `E2` 正文。

## CLOSED 卷（2026-08-28 从 `CONSTRUCTION-LEDGER.md` 原样搬入 — 只读，勿续写）

> 搬迁理由与授权在搬迁 commit 正文。**原样搬入，一字未删未改写**——与本档 2026-07-27 那次
> 同一操作、同一理由：活指针必须一口气读得完。

- **CLOSED（此处只留名与锚；链条、blocker、修法、预算全在各轮 commit 正文与
  `migration/document-work-assurance-v3/` 的 record / journal——不可变、可 grep）**：v3 迁移
  N0–N4 · wave 1/2 · p3-corr · Phase A/B/B2/C0/C1/C1.5/C1.6/C2/C3/C4/D · 指令层 amendment 轮
  （指令层成员 9 条）· Stage 2 `p4-bridge` · Stage 3 P4-CODE · Stage 4 `p4-doc`——**P4 全程
  ②–⑦ 完成，`P4-IMPL-v1` effective**（两个锚点原写在此处、均指调用者仓，2026-08-28 用户裁删——
  搬迁触发路径守卫，见搬迁 commit 正文）· p4-doc 三
  triage + 维护批/rider 兑付轮 · O-5 amendment read（record `10c040b`）· run `p5a-firewall`
  （A2 已签已激活 `6295346`）· run `p5a-shells`（148 壳 promotion `d749406`）· pre-START
  优化维护批 · 回归电池分层批（tiering 规则落 run-v2 README，该节即 revert unit）· **撤回轮
  `E10-D-NARROWING`（净变化零，closeout `4ab1db1`）· 设计轮 `E2-REBASELINE-DESIGN`（closeout
  `e55d304`）· 构造轮 `E2-VERB-E10-PIN`（record `c667d08`）· run `p5b-firewall`（A3 已签 `935cada`、
  已激活 `959104d`；closeout `89383b1`，FULL record `v3-review-full-fef3a2e.md`）· 精简轮 `SIMP-ABCD`
  （closeout `214f743`）· `V1-CONTEXT-EXACT` · `SIMP-A4` · run `p5b-claims`（153→173 objects，promotion `3074ce4`，closeout `efa56ea`；FULL `v3-review-full-8ad8c2f.md` + VERIFY `v3-review-verify-275da5b.md`）· **批 A（A1+A2，2026-08-10 收批）**——A1 链 `a7bb1d6`→`fd058aa`→`7a08265`；A2 五轮链在 plan 步骤注与 `V3-A2-R*-CLOSEOUT` commits，batch:A 裁决 retired 入 decisions-archive、`HD-18` implemented，收批 commit `V3-A2-CLOSE-v1`** · 设计轮 `BATTERY-REPO-SCOPE`（2026-08-18，仪器仓内第一个构造轮：全档电池六条按**被验证的仓**分档、doc-only 例外句改按子句读、revert anchor 标明其价已是设计轮，`HD-45`；rider `battery-travel`/`tier-file-vs-clause`/`tier-scope` 兑付删行，`layer-crossrepo-token`/`layer-outbound-refs` 新入 bank；read `v3-cold-read-28501fe` 0 must-fix，`E9` 三腿全程未花） · 设计轮 `ORCHESTRATOR-CHARTER`（2026-08-18；orchestrator 的角色说明书立为 `E10` **第十成员**，走收窄形——九条已在层里的义务只点名归属并指向规则 id、三条层内零承载的写正文；`E1` 的「派发即独立」由充分条件改为必要非充分并加中间态披露句，`HD-46`；rider `E1-suff` 兑付删行，`e1-disclose-home` 与 `charter-qualifiers` 新入 bank；三次独立 read 收敛——2 must-fix → 1 → **0**，`E9` 三腿全程未花）· 轮 `CALLER-ONBOARDING`（2026-08-19，第三期：onboarding 九条 + 两模板 + 第七命令 `dtw init` + `layer_path_check` 归位；九条在临时仓实跑、两支守卫各见拦一次放行一次；FULL `CHANGES_REQUIRED`（hook 提交成 100644 · 测试少钉一条头部规矩）→ 一次用户批准的修 → VERIFY `REVIEWED_NO_BLOCKER`，`E9` 三腿走满；`HD-47`/`HD-48`，五条 rider 新入 bank；记录 `v3-{cold-read-c22e229,review-full-2026a14,review-verify-4029b43}.md`）。· 轮 `LEDGER-SPLIT`（2026-08-19，批 DTW-INDEPENDENCE R1：仪器开发史入本仓——本账本 + archive + 16 份构造 plan，17 件逐 blob 对账；调用者账瘦 113→57 行；FULL `CHANGES_REQUIRED`（搬入 plan 内 10 条挂载前缀死链）→ 一次用户批准的修 → VERIFY `REVIEWED_NO_BLOCKER`，`E9` 三腿走满；`HD-49` 取代 `HD-28`、`HD-50` 取代 `HD-48`；记录 `v3-{cold-read-7701f03,review-full-e74be07,review-verify-8f1ad1d}.md`）。· 轮 `XREPO-REFS`（2026-08-20，批 DTW-INDEPENDENCE R2：指令层不再写调用者路径——`E10` 收caller-held-path 条款、四处降名、`E1` 披露句得载体与责任人、`E10` provenance 死从句删除，零守卫代码改动；开轮 read 返 1 must-fix（层内 15 处裸 commit id 无家）→ amendment `48b6c5f` + 复读 `c53fc4e` 结对；FULL `CHANGES_REQUIRED`（新条款把守卫说大了）→ 一次用户批准的修（收口径；守卫认全类改入 R3）→ VERIFY `REVIEWED_NO_BLOCKER`，`E9` 三腿走满；V-1/O-3 字节走自由通道 `34a5ae9`；rider 三删五增二细化；记录 `v3-{cold-read-69fc082,checkpoint-read-48b6c5f,review-full-dd18226,review-verify-2937bcd}.md`，journal `xrepo-refs-2026-08-20.md`）。· 轮 `DE-PREFIX`（2026-08-20，批 DTW-INDEPENDENCE R3：去 `ResearchSystem/` 前缀——313 件上提一层、冻结字节按 `HD-44` 整体移动、2 处 `parents[4]`→`[3]`（重测确认台账原数仍准）；守卫认全类（resolve-nowhere 单一类、escape 不算解析、`.harness/` 运行时豁免）+ rename 感知（候选第一次实弹被自己守卫拦下，pre-submission correction 修成 un-pathspec'd `-M` diff）；`E10-sync` 三镜像同 commit（`HD-22`）；`sweep_refs.py` 入仓；开轮 read 0 must-fix（`L-1` 字节随候选、`L-2` 入条款、`L-3` 入 bank 行 `e9-pair-budget`）；FULL `CHANGES_REQUIRED`（B-1 四处守卫分工描述被证伪 · B-2 解析器 fail-open）→ 一次用户批准的修 → VERIFY `REVIEWED_NO_BLOCKER`，`E9` 三腿走满；VERIFY V-1/V-2 字节走免通道 `f8b4ef3`、V-3 入 bank 行 `e10-cannot-see`；rider 一删（`mount-inert` 由调用者侧 `$H` 重指 + hook 硬失败兑付，落调用者本轮 gitlink-bump commit——跨仓兑付，「同 commit 删行」按仓各自成立）三注（`frozen-path-prefix` 事实重写 4→5 处、`submod-index`/`decited-paths` 记 touch 到达不可兑）两增；候选带 trailers 为 `E8` 违规孤例（修腿正文起永不再有）；**层欠一次独立 read，随下一轮开轮**（tip 十成员 blob id 列在 VERIFY 记录）；记录 `v3-{cold-read-4410899,review-full-39a21a8,review-verify-2538893}.md`，journal `de-prefix-2026-08-20.md`）。· 轮 `INIT-SURFACE`（2026-08-21，批 DTW-INDEPENDENCE R4 收官：`dtw init` 命令面判据入层——README onboarding 行载「树里那半接线可进 `init`、机器那半不进」+ `--into` 不加（`HD-47` 转 implemented）；分工收拢——两路径守卫的分工一处说、其余指过去（home = README *Local enforcement* 行，rider `guard-division-home` 兑付删行）；`sweep_refs.py` 补 9 条测试（FULL `39a21a8` `O-4` 账清，电池 739→748）；开轮 cold read 兑 DE-PREFIX 欠的层 read，1 must-fix（`M-1`：REVIEW.md 给 caller 持有的产品评审记录写了仓库路径 token）由 amendment `bba6f94` + 复读结对清掉、零预算；FULL `CHANGES_REQUIRED`（`B-1`：home 句量词被三处残留证伪——含 candidate 自己写的一处）→ 一次用户批准的修 `84dea06`（含搭车 `L-2`/`O-3`/`O-4`）→ VERIFY `REVIEWED_NO_BLOCKER`，`E9` 三腿走满；VERIFY `L-1` 字节走免通道 `9fe60b9`（修腿自己复制了 `B-1` 的内部矛盾形状，第三方连续第四次在同族句子上翻车后由通读收口）；rider `submod-index` redeem-when 改 round-eligible 形（VERIFY `2538893` `O-4` 尾注兑现）；`HD-50` retire 入档；记录 `v3-{cold-read-17ce3ed,checkpoint-read-bba6f94,review-full-7f6e7f0,review-verify-84dea06}.md`，journal `init-surface-2026-08-21.md`）。· 轮 `PREVIEW-RENDER`（2026-08-21，`E11` 载体裁决「脚本化」半边兑现：`dtw preview` 第八命令（`HD-51`）——从产品 run 冻结 control plane 确定性渲染 START 预览，不经 LLM、可重推导不落盘；`EXECUTION.md` SIMP-C4 接线句 + `REVIEW.md` O-1 字节随候选，两成员的独立 read 随下轮开轮；开轮 cold read 0 must-fix（兑 `9fe60b9` 欠读，十成员全实读）；FULL `CHANGES_REQUIRED`（`B-1` boundary 对象按 list 渲染、八真实 plane 全中丢 14–91 条路径 · `B-2` Context 省略吞嵌套节）→ 一次用户批准的修（全包）`15a53fe` → VERIFY `REVIEWED_NO_BLOCKER`，`E9` 三腿走满；VERIFY `V-1`/`V-2` 字节走免通道 `76ebf4a`（含用户裁删 boundary 计数）、`V-3` 裁不加 catch-all；rider `review-record-loc` 迟兑整行删、`RA` 计数改八命令、`e10-cannot-see` 追注两句量程；电池 763→770；记录 `v3-{cold-read-dd22789,review-full-57d1312,review-verify-15a53fe}.md`，journal `preview-render-2026-08-21.md`）。· 轮 `TEMPLATE-LIB-ROOT`（2026-08-21/22，重扎根第③件的收窄首刀，队首由用户当场裁定：两个 run-v2 模板脚本**对着调用者 run 目录 import 就死**——`check_template_instance.py`（唯一 pre-START gate）与 `make_paragraph_map.py` 把 `repo_root` 一个变量当两件事使（找库 + `git -C` 的指令所在仓），拆仓后这是两个仓，而调用者那棵树只有 run 数据没有库；修法＝照抄那四个 `run_*.py` 早就对的形状，库走 `__file__` 相对、`repo_root` 只留给 git。新测试 `test_run_v2_template_library_path.py` 走**子进程**测缺陷类（六个脚本全测，四个本就对的当回归钉）——老测试进程内 `exec_module` 且 `_harness` 已把 `tooling/` 放进 `sys.path`，替脚本满足了它该自证的 import，故 770 全绿而脚本是死的；电池 770→774。开轮 cold read 0 must-fix（兑 PREVIEW-RENDER 欠的两成员读，十成员全实读）；FULL `CHANGES_REQUIRED`（`B-1`：候选正文同时写「orchestrator 与 executor 同 session」与「四持有一项不占、故结构性独立」，自相矛盾且**回归**两轮前已被 `L-4` 纠正过的形式）→ 一次用户批准的修 `627df95`（errata + journal 落盘贴实测 + 假量词）→ VERIFY `REVIEWED_NO_BLOCKER`，`E9` 三腿走满；收批三裁（`V-1` 扫类未贴：补跑两类**均已关闭无新实例**，用户裁不记不贴 · `V-3`+`O-3` 单 session 角色题入 bank 待裁 · cold read `L-1` 范围题**已裁**＝对所有 run 都算，建 `HD-52`）；rider 两处行号更正、两行新增（`startcard-form`/`one-session-roles`）；**披露一次自身越界**：验证时往调用者仓写了一个 `paragraph-map.json`，已删并核对调用者树复原，`ORCHESTRATION.md` 的事前路由在单 session 轮无处可走即 `O-3` 的题；记录 `v3-{cold-read-39e395e,review-full-83e3191,review-verify-627df95}.md`，journal `template-lib-root-2026-08-21.md`）。· 轮 `EXECUTOR-CHARTER`（2026-08-22，队首由用户裁定插于重扎根之前：执行者第一次有机器生成的 charter——`dtw dispatch` 加第四个 dispatch family 两模式（`HD-53`）：`--executor` 产品侧交三事实（run id · 冻结指令 path+revision · charter=`EXECUTION.md`）带四类拒绝（目录出仓 / 无指令 / 未冻结 / worktree 漂移按 blob-id 等值判），`--construction-executor` 构造侧单句指 `CONSTRUCTION-CHECKLIST.md` 零推导；两模式均不写 freeze marker（executor 派发不开评审窗口）；`EXECUTION.md` 删「运行纪律走 Context 引用」写作规则并命名部分 supersession（p4-bridge f1 的 2026-08-01 路由裁决——留强半边：Context 只装背景、出现要求即缺陷；换掉半边：引用之职由 dispatch 承担），`dtw preview` 的 Context 省略就此由「诚实」转「正确」；`HD-52` 载体同批落（START 卡句移出编号态范围成独立段）转 implemented；采样义务定读数时刻（`HD-54`）安家 `EXECUTION.md` Authoring gate；`ORCHESTRATION.md` 被证伪段重写；rider `startcard-form`/`charter-prose-overreach` 兑付删行、义务表刻意不碰（`e1-table`/`charter-qualifiers` 不开）、`mark-case` 明确不兑；电池 774→790。开轮 cold read 0 must-fix + 1 low（十成员全实读、可全引而未引）；FULL `REVIEWED_NO_BLOCKER`（0 blocker 5 low，九 mutation 九红）→ 收批三角六件一次修 `3dd226b`（用户批全包：L-5 counterpart 幻指 · L-2 恢复对冲句 · L-3+L-1 采样段主体句+四改五 · L-4 修 ONBOARDING 簿留史 · 冷读 L-1 判据读法五路径落地）→ VERIFY `REVIEWED_NO_BLOCKER`（2 low 3 obs，接受项逐条重跑、五 mutation 带绿色负对照），`E9` 三腿走满（FULL 返无 blocker 后经 `R10` 晚激活修腿，仍计本轮唯一修）；VERIFY 两 low 入 bank（`plan-delivery` 带 deadline、`fixleg-scan-paste` 记四连趋势）+ FULL `O-1` 入 bank（`exec-mount-test`）；成员编辑欠独立 read 随下轮开轮，咬合时刻=第一份按新规则起草的产品 run 指令；`ORCHESTRATOR-CHARTER` 未答问题①就此关闭；记录 `v3-{cold-read-693b692,review-full-229f03f,review-verify-3dd226b}.md`，journal `executor-charter-2026-08-22.md`）。· 轮 `PRERUN-RIDERS`（2026-08-22/23，产品首跑前清账批，用户批插队于重扎根第③件前、收批即消费、队首回该项；**首个 `HD-55` 独立角色形态轮**——冷读/executor/FULL/修腿/VERIFY 五次派发全部独立 session（`dtw dispatch` 出单），orchestrator 全程零手改，候选 `E1` 披露首次以四持有零占声明 structural）：七裁决落层——plan 送达 + 指令优先 bound（`ORCHESTRATION.md` Handing + `EXECUTION.md` 写作规则；理由=调用者开发自己规则的落脚点）· 薄检查=控制面 finding（`REVIEW.md` 两节对齐 review_only 镜像）· 观察路由成文化（record observations → closeout 按 policy 归口）· status-key 二次维持 + `dtw flow` 递单前纪律 · mark-case **当日翻案**改判维持词表（executor-charter.plan 实测 0/1/0 为据）· ctx-ground 二次维持 · `HD-55` 落层三站点（家=三角色表，冷读 `O-1` 补第三站）同 commit 翻 implemented；riders 五删（plan-delivery/chk-thin/HI-route/mark-case/fixleg-scan-paste——末条由修腿贴扫类自兑）二改写（status-key/ctx-ground）二新增（io-hiroute-stale 超范围披露、用户裁保留；hi-schema-gloss=VERIFY `V-1`）；开轮 cold read 0 must-fix（兑 EXECUTOR-CHARTER 欠读）；FULL `REVIEWED_NO_BLOCKER`（5 low 4 obs）→ 全包修 `860729f`（勘误 journal 逐数重测、四类扫贴正文并扫出英文 pattern 漏中文形的第二重、`io-design` 引文精确化）→ VERIFY `REVIEWED_NO_BLOCKER`（1 low 2 obs），`E9` 三腿走满；纯文本轮零代码零 schema，电池 790 三测同数；两成员编辑欠独立 read 随下轮开轮；记录 `v3-{cold-read-3a6a10b,review-full-7cb7213,review-verify-860729f}.md`，journal `prerun-riders-2026-08-22.md`）。· 轮 `PUB-FACADE`（2026-08-23，公开化批 A 门面件；队首两问当场裁——**MIT** · **顺序 A→B→C**——随第三裁**轻量轮形**落 plan `publicization-a.plan.md`：用户豁免开轮冷读（rider `waiver-live` deadline 到达、未咬——豁免前 `§live` 已整读，touch note 落行；PRERUN-RIDERS 欠的两成员 read 续欠、随下一轮开轮）· 工作侧两角色单 session 合并（`E1` 例外通道，四持有全 held 披露于候选正文）· 独立 FULL 保留：LICENSE(MIT) + 双平台 CI（ubuntu+windows × py3.12/3.13；ubuntu 腿=本仓**首次 POSIX 验证**，定出 jsonschema>=4.18 下限——系统 4.10.3 下 571 failed 单根因）+ 根 README 除锈（`readme-cli-stale` 四句全清兑付删行）+ ONBOARDING 第 9 条按实测改写（`posix-mode-wording` 兑付删行：644 hook=带 hint 跳过、hint 可抑制）+ 计划外抓修两件——`.githooks/pre-commit` 裸 python 使 POSIX 接线后**有钩必死**（python3→python 带 `-c pass` 探测循环，防 Store 假别名）、`test_candidate_checks.py:523` 唯一被执行的裸 python fixture（sys.executable）——+ 新增 `test_precommit_hook.py` 以 subprocess 钉 wrapper 缺陷类；电池 790→793 双平台绿。FULL `CHANGES_REQUIRED`（B-1 本轮自己的缺陷类只扫 tooling、漏了正在改的文档且 README 新写两处裸 python · B-2 新测试三行为只钉一半、exit-0 空壳存活）→ 一次用户批准的修 `71e1f24`（两文件各一句解释器约定句赎清七站点 + blocking 测试杀 mutation 2/4 + docstring 收窄 + GBK errors=replace 第三坑顺手修）→ VERIFY `REVIEWED_NO_BLOCKER`（7 mutation sha256 还原、双平台 793 独立复现），`E9` 三腿走满；VERIFY `V-1`/`O-3` 字节走免通道 `a3ef5ee`；`V-2` 入 bank 行 `fixleg-scan-raw`、`O-1` 入 bank 行 `py-convention`（类残存 `EXECUTION.md:364` 成员内 + run-v2 README 四处）、`O-2` 注入 `E10-sync` 行（第四份机器侧成员路径拷贝）；测量通道两次翻车（wsl.exe 回传 $? 不可信 · 反引号被中间 shell 当命令替换吃掉致正对照一度测了空气）当场识破、有效实验重做，记 journal；**CI 落仓未跑（零 push）——首跑等用户 push**；记录 `v3-{review-full-28dd80b,review-verify-71e1f24}.md`，journal `pub-facade-2026-08-23.md`）。· 轮 `CONTRACT-V4`（2026-08-23，公开化批 B 重签打包批；plan 四裁：冷读+FULL+VERIFY 全独立、v4 捆绑 `wspec-owner` 契约站点、卡片裁授权触 `E2` 面、§10.5 两问立案挪后：**契约 v4 单文件成立并已签署（`HD-56`，blob `614932de…`，用户通读后签）**——合并 v3+s1+s2（考古更正：两份补丁实已签过字，UNSIGNED 是签前残迹）、四句替换+两节版本边界落 13.1/13.2、五断链按三类修、frontmatter 清态、§3 归属行改 executor；三源文件退役入历史（用户确认）、`E2` 冻结面十六件、`E10` 成员 10→8→**9**（v4 入层=用户裁，`HD-56` ②落簿；`E10-sync` 三站同 commit 轮内走两次、散文腿全扫）；豁免簿契约条退役（removing decision=`HD-56` ③）；split-design/io-design 除锈随签重签（`HD-40`/`HD-35` 第三签，四 rider 由此兑付）。开轮冷读 `b8df15a` 0 must-fix（偿两轮欠的成员 read；其 L-1 入 bank 行 `read-name-split`）；FULL `CHANGES_REQUIRED`（B-1 四站点「未签先称签」——D1 刚清的缺陷类在周边文本重现；合并本身逐字节核净、plan 声明 verbatim 处 ratio 1.0000）→ 一次用户批准的修 `d0f185c`（四裁折入：修+O-5 三句补回+v3 退役确认+v4 入层；L-1..L-5 搭车，`fixleg-scan-raw` 以贴原始输出自兑删行）→ VERIFY `REVIEWED_NO_BLOCKER`（V-1 第五站点 operative 走免通道删 `f112135`；L-4 判 transcription 维持；E2 字面量无机器绑定实测在案），`E9` 三腿走满；riders 四删一改写一自兑一增 + `PD` 触注；`HD-20` 枚举随 `HD-56` 同批更新（`HD-44` 的同批更新为签字 commit 声称而 diff 未含——`v3-cold-read-cf54a79.md` `L-3`；2026-08-23 依用户「落」裁决补落）；记录 `v3-{cold-read-b8df15a,review-full-5f849da,review-verify-d0f185c}.md`，journal `contract-v4-2026-08-23.md`；**本轮成员编辑（含免通道 `f112135`）欠独立 read 随下一轮开轮，且下轮冷读并新收 v4 这个 339 行成员、无先前 read 可引**——VERIFY 已注此成本）。· 轮 `STRANGER-GUARDS`（2026-08-23，批 C 陌生人可用性第一轮；开轮四裁 + fix-gate 五裁全在 plan `stranger-guards.plan.md`；`HD-55` 常规形态——冷读/施工/FULL/修腿/VERIFY 五次派发全独立 session，orchestrator 零手改工作产物）：守卫扫描面调用者化——新 `caller.py` 声明加载（`.harness/scan-surfaces.json`，`dtw init` 写默认绝不覆盖、malformed 响亮拒绝不静默回退）+ 两支守卫同读一份声明，首调用者 `ResearchSystem/…` 条目以声明形态存活（测试逐字节钉住）；`TrackedPaths` 认 submodule 内部路径（`submod-index` 裁「认」并兑付删行）；12 解析点全改「git 发现或响亮拒绝」（`review_freeze_check.py` 超 plan 表半步，类扫描证成、代价披露于候选正文）；层修正段对第二调用者不再读反（`amend-exempt-caller` 兑付）；README terminus 经用户否 request-access 提案（「不写，thesis 就是 private」）后回单机历史形态 + 一句 private 说明；候选 `c2e955b` 27 文件、三 rider 同 commit 兑付、`decited-paths` 触注（跨仓兑付待调用者侧）。开轮冷读 `cf54a79` 0 must-fix 3 low 5 obs——一次清偿三笔欠读（本轮开轮读 + v4 首读 339 行 + CONTRACT-V4 成员编辑欠读）；L-1/L-2 入 bank 行 `v4-verifmode`/`v4-plan-digest`，L-3（签字 commit 声称改 `HD-44` 而 diff 未含）归口用户。FULL `REVIEWED_NO_BLOCKER`（2 low 4 obs；电池 838/792 独立重导、8 组自写 mutation、守卫负对照非空转）→ `R10` 晚激活修腿（用户批：Low-1 尾斜杠归一 + README「不写」）`54f7fa7` → VERIFY `REVIEWED_NO_BLOCKER`（2 obs），`E9` 三腿走满；registers `53ec1a6`（`HD-44` 十八→十六带日期注 + ledger public-仓句证伪更正 + `HD-57` 立条——`E2` 五处陈旧字面一次裁「可以改」，应用批排收批后）；Low-2 教训入档＝出单 base 取上一已评审 tip、riders-only commit 落候选之后（本轮 VERIFY 已照此跑）；电池 792→844；成员编辑（checklist 修正段 + 应用批将触的 v4/`E2` 字面量）欠独立 read 随下轮开轮；记录 `v3-{cold-read-cf54a79,review-full-c2e955b,review-verify-53ec1a6}.md`，journal `stranger-guards-2026-08-23.md`。· 轮 `STRANGER-PROOF` ＋ 批 `SUBMOD-HOOKENV`（2026-08-24 合并收批，用户裁一次共享 FULL 罩两单元；全程 `claude -p` 独立 session 派发——`E1` 修正 `1a0a200` 后第一批，该修正由用户裁免轮当日落、其在 `ORCHESTRATION.md:24` 的镜像句由开轮冷读抓出走 must-fix 结对清掉 `153302a`）：第二调用者实证真发生——异布局新仓九条照文档实走（`stranger-proof-walk-2026-08-24.md`），抓出文档三缺陷（依赖步骤缺失 / 双解释器假话 / 决策簿挪位重建空簿，候选内修）+ 重缺陷：守卫 submodule 识别在 pre-commit hook（唯一真实运行环境）失效、`commit -a` 下四探针全反——根因＝git 泄漏给 hook 的定位 env vars 未清，修＝查询前清掉且名单向 `git rev-parse --local-env-vars` 现问，7 条真 `git commit` subprocess 测试 5 红→7 绿；观众向根 README 重写、quickstart 全命令实走背书；候选曾被 orchestrator 记账 commit `0133d1b` 连锅吞（共享 git index，声称 ledger-only 实载 587 行）——用户裁 append-only，披露 `e620b43`、归属勘误落 journal，**教训＝executor 运行期间 orchestrator 零 commit**；首次共享 FULL 派发被用户叫停（按 `E9` 判据未发生、零消耗）后重派返 `CHANGES_REQUIRED`（B-1 quickstart 缺 tracked-hook 步骤、读者会拿到永不运行的 hook 还以为在跑 · B-2 mutation 签名两条身份错）→ 一次用户批全包修 `3149581`（补步并从已发布 remote 逐字重走、关掉 local-clone 天花板 + errata 贴逐测实测撤回假句 + 三 low）→ VERIFY `REVIEWED_NO_BLOCKER`（hook 字节旁证逐字节同、四 mutation 逐格复现），`E9` 三腿走满；电池 792→851；riders：`submod-hookenv` 兑付删行，`discover-root-env` / `move-cost-member-site` / `onboard-clone-decl` / `onboard-cmd-count` / `e1-reader` 新入 bank，`decited-paths` 前提解锁；memory 禁用与「都不立」处置、取消派发披露均落 journal `stranger-proof-2026-08-24.md`；记录 `v3-{cold-read-21dad76,checkpoint-read-153302a,review-full-3d5c705,review-verify-3149581}.md`。· 轮 `README-BILINGUAL`（2026-08-24 落 `2522ce1`，**用户 2026-08-25 裁免轮**——不派冷读、不派 FULL、不派 VERIFY，`E9` 三腿全程未花，故本轮无 plan、无 journal、无评审记录，**本行即其唯一记账**）：批 C 收批时用户指定的队首「观众向根 README 的可读性与内容逻辑 review」由此消费——根 README 按编辑视角重写（开篇改写成仪器的第一目的＝它交付的工作是对的、受众重锚到非代码工作、轮次画成 mermaid 时序图含人类下指令与 START 坎、quickstart 把五条机械命令与四项判断分开写、新增 Install 节写明 submodule 挂载是今天唯一支持形态、提取史不再复述），并**队列外增件**一份 `README.zh-CN.md` 简体镜像（顶部互链、自陈同步日期与「分歧以英文为准」）。两文件皆非 `E10` 成员，故不欠层 read。提交前自验三项（相对链接全解析 · 双语章节与代码块计数同 · 电池 851 全绿）系候选正文自陈、无独立复核——免轮的代价即此。· 轮 `RIDER-SETTLEMENT`（2026-08-25，bank 结算批；**轻量轮形**——用户裁豁免开轮冷读、独立 FULL 保留；三条开批裁决载 plan `rider-settlement.plan.md`）：**bank 30 行 → 16 行**——十条兑付随修同 commit 删（候选 `fd525e4`：`py-convention`/`readme-three`/`onboard-cmd-count`/`onboard-clone-decl`/`onboarding-labels`/`move-cost-member-site`/`decl-dup`/`retire-suite`/`discover-root-env`/`exec-mount-test`），四条按用户裁 retire 删行（riders-only `8aa9f6e`：`ctx-ground`/`status-key`/`self-caller-guards`/`F-c`——各自裁决另有家，行是第二份拷贝）；十三条 design 行路由入 `dispatch-economy` 批（其中九条同两表面一次收，见下方该条）。**唯一真缺陷**＝`caller.py` 的 `discover_repo_root` 未清 git 定位 env（`GIT_WORK_TREE` 下答环境的仓而非探针），即 `SUBMOD-HOOKENV` 那一类的第二站点；修法复用 `paths.py` 已验证形状并把两行抽成 `env_without_repo_scope()`（越 plan 变更面，`L-1` 披露）；配对实测同探针有无变量皆答对、同查询不清 env 答错。电池 851→854。FULL `CHANGES_REQUIRED`（`B-1` `retire-suite` 兑付未关缺陷类——新 `RAW_IDS` 与 `PRESENT_IDS` 相等致「按删除清单算」仍全绿 · `B-2` 两段 `HD-41` 扫类结论在其自身声明量程内为假且未按 clause ④ 贴输出）→ 一次用户批准的修**全包** `5873840`（两 blocker + 三 low + `O-1` 断言整句 + `O-3` 账本记 ruling 3 路由；`B-2` errata 撤回假句、`L-2` 实测 `2 created` 两实例文件皆重建、`L-3` 撤回自己改出的 `run_repair.py` 假归属）→ VERIFY `REVIEWED_NO_BLOCKER`（七件全交付，5 残留不拦路）；`E9` 三腿走满。**五条残留按用户裁全走 `E10` 免通道当场清** `6a73c79`（不是轮、零预算）：`V-1` 同一缺陷第三次换马甲（新 `RAW_IDS` 又与 `already_gone` 相等）——三个 ordered check 下**无解**，fixture 加第四个 check 并**穷举**八种「不问文件系统」的实现全红、真实实现绿 · `V-2` ONBOARDING 约定句原写「下面的命令」而条目 1 的 `pip install` 在它上面，改 file-scoped · `V-4` `--repo-root` 六脚本通用说一次 · `V-5` 两处约定句行号更正（`:10`→`:11`、`:365`→`:368`）· `V-3` errata＝扫类命令带省略号跑不了，且**英文 pattern 漏中文形**（仓内第二次，首次在 `PRERUN-RIDERS` journal），重跑覆盖中英文形后类实例＝四处 quickstart 步数，`onboard-cmd-count` 指的 `--help` 派生计数确已关闭。**成员编辑（`EXECUTION.md` + `document-harness/README.md`）欠独立 read 随下轮开轮**（豁免冷读的代价）；`R5` 观察（16 行中 13 行需开轮才可兑）按用户裁待 `dispatch-economy` 收完 9 条、bank 降至 7 行时再评；记录 `v3-{review-full-8aa9f6e,review-verify-5873840}.md`，journal `rider-settlement-2026-08-25.md`）。journal 在 `document-harness/journal/<轮名>-<日期>.md`。

### 2026-08-30 第二次搬入 —— 九条 CLOSED 条目（从 `CONSTRUCTION-LEDGER.md` 原样搬入 — 只读，勿续写）

> 用户 2026-08-30 裁「closed 全部撤走」，为一条 `R5` 观察腾位；授权与逐条清单在搬迁 commit 正文。
> 原样搬入，一字未删未改写。

- **保障面二期复盘 CLOSED（2026-08-03）**：底账 + 六裁决在 `document-harness/journal/retro-2026-08-03.md` §7 与 `22b27aa`
  正文。后续指针三条：audit 降本收在 (d)（下个产品 run 先测新 cadence 基线）· (c) 跨 freeze 继承挂起 ·
  (b) 轮数封顶压后。
- **HI-REDEEM-5 CLOSED（2026-08-07）**：FULL + 一次修腿 + targeted VERIFY 均
  `REVIEWED_NO_BLOCKER`；锚 = [`journal`](document-harness/journal/hi-redeem-5-2026-08-07.md) +
  [plan](document-harness/plans/harness-issue-redemption-batch.plan.md)。P5C 归根 LEDGER/独立 plan，不归本账本。
- **「harness 对外 I/O 边界」整条 CLOSED 2026-08-13**（随批 B 收批；两件均已落地——接线 `HD-25`、
  解耦 `HD-31`）。supersession-2 签字 2026-07-30 记录 `migration/…/supersession-2-signature.md`；
  理由错模式已裁——历史两例接受、今后判据 = `E3` 断言条款。
- **批 B —— 「谁调用、谁绑定」CLOSED 2026-08-13**（plan
  [`harness-batch-b.plan.md`](document-harness/plans/harness-batch-b.plan.md)）：R1 `run_all` 接线
  （`HD-25`）· R2 io-design v1 签字（`HD-35`）· R3 ledger 解耦（`HD-31`）· R4 三角色重指 +
  rider `tier-scope` 三件 · R5 `E10` 通道放松 + `R10` rider 到期判据（`HD-36` 留 live——其②层内
  无承载；`HD-37`/`HD-38` implemented）。③ `E2` 不加守卫已裁不做，重开条件＝拆分批（`HD-27`，
  rider `PD` 重定范围）。**R4/R5 用 `E10` 独立 read 而非 FULL，`E9` 三腿两轮全程未花**；五份 read
  记录 `migration/…/v3-checkpoint-read-{be9878a,0aed595,8884f47,136f27f,f61ce2c}.md`。

- **拆分批 —— harness 搬成独立仓**（`HD-18`）：**整批 CLOSED 2026-08-17**，五轮——R0 设计 · R1 搬 254 件 + 执行 `HD-39` 的删除 · R2 摘 CLI 成 `dtw` · R3 调用者侧接线 · R4 记账收批。**结果**：新仓 = private `Melclycj/do-the-work`，产品仓以 gitlink 钉住 `ResearchSystem/harness`；pre-commit 改 tracked 且三支守卫从 submodule 跑；记账断言定终局（调用者 `HARNESS-POLICY.md` §4）；八条 rider 逐条有归宿；`HD-33` / `HD-28` / `HD-15` / `HD-10` 转 implemented。**「重扎根轮」原定三件，2026-08-18 拆开做**——第一件 CLOSED（轮名 `SPLIT-COPY-RETIRE`：调用者副本 273 件删除 + 入链重写；FULL `CHANGES_REQUIRED` → 修 → VERIFY `REVIEWED_NO_BLOCKER`，`E9` 三腿走满；记录 `v3-review-{full-2d148f3,verify-bef77f3}.md`，两份都留在调用者仓——那一轮的 subject 是调用者的树）。**余下两件仍未排期，且「重扎根轮」这个名字自此不再指任何单一轮次**：② 去 `ResearchSystem/` 前缀与 `REPO_ROOT` 深度（实测只 2 处 `parents[4]` 会断）+ `E10-sync` 三处同改（须同一 commit）③ 步骤 19 的十一个 `--repo-root` 解析点。**三条 rider 的 deadline 原文指向「重扎根轮」，按此重指**：`mount-inert` 与 `PD` → 第 ② 件（`$H` 与冻结面都在那一刻动）· `submod-index` → **deadline 已于第一件到达且未付**，改指下一个碰 `paths.py` / `candidate_path_check` 的批。`nonrec-clone` 已兑付（第一件删副本 + `repo-audit` 认挂载点）；`battery-travel` 已于 2026-08-18 轮 `BATTERY-REPO-SCOPE` 兑付删行（其 deadline 即「第一个于 harness 仓内开的构造轮」，那一轮就是）。五轮叙事在各轮 commit 正文与 `ResearchSystem/migration/document-work-assurance-v3/` 的评审记录里，不在账本重写。plan [`harness-repo-split.plan.md`](document-harness/plans/harness-repo-split.plan.md)。**三期至此全部 CLOSED（2026-08-19，第三期见下方 onboarding 项）。批 DTW-INDEPENDENCE（`HD-50`→retired 入档）四轮全 CLOSED（2026-08-19/21；R4 = 轮 `INIT-SURFACE`，判据入层 + 分工收拢）。构造轮 `PREVIEW-RENDER` 已于 2026-08-21 CLOSED（见当前指针 CLOSED 卷）**。**第 ③ 件的数已按现场重测更正：不是十一个而是 **12 个解析点 / 7 个文件**（`cli.py` 6 个 `args.repo_root else` @ `:43 :80 :147 :329 :414 :462` + 5 个 parser site，`init` 与 `preview` 两个新命令使原数作废；run-v2 六脚本各 1 个 `parents[3]`）。其中**会当场咬人的 2 个已由轮 `TEMPLATE-LIB-ROOT` 修掉**（2026-08-21/22 CLOSED），**余 10 个**（`cli.py` 六 + 六脚本的 `parents[3]` 默认，后者只在不传根时才走到，而今天所有调用都传）。**轮 `EXECUTOR-CHARTER` 已于 2026-08-22 CLOSED**（见当前指针 CLOSED 卷；其 plan——[`executor-charter.plan.md`](document-harness/plans/executor-charter.plan.md)——载的四条用户裁决与一个未答问题均已消费，问题的答案即 `HD-54` 的读数时刻裁决）。**下一队首＝公开化三批（用户 2026-08-23 改队，见下条）**；重扎根第③件余下的 10 个解析点退居其后、拟并入公开化批 C（实测今天不咬人：`cli.py` 六个不传即取 cwd、六脚本的 `parents[3]` 对调用者布局解析正确）；契约 v4 并入公开化批 B。**第③件的 10 个解析点已由轮 `STRANGER-GUARDS` 清零（2026-08-23，批 C 第一轮）——十二处全数改「git 发现或响亮拒绝」，步骤 19 一脉就此全部关闭。**
- **批 `CORE-SET` —— 让核心集脱离本仪器自己的建造史**（用户方向 2026-08-25，自此为本仓队首）：
  挂载本仪器的仓只带核心集就能开轮、跑轮、收轮。**十九条用户裁决、四个轮次的量程、验收与全部量测
  在 [`document-harness/plans/core-set.plan.md`](document-harness/plans/core-set.plan.md)**，本行只
  留指针——2026-08-26 一次把复述压回去，因为它撞破了同日新立的每条上限。
  **轮 1 `CORE-SET-LAYER` CLOSED 2026-08-26**（收轮 `83aecd4`；记录 `v3-{cold-read-ff4b749,
  review-full-92cc514,review-verify-0f0498f}.md`；journal `core-set-layer-2026-08-26.md`）：剥史树
  上九成员真断链 **31→13**、`ONBOARDING.md` 另测 **2→0**；`E9` 三腿走满且**修腿花了两次**（用户
  2026-08-26 裁「算，照实写」，VERIFY `V-4`）；bank 16→19。
  **本轮五个在仓成员全部改动，欠独立 read 随下轮开轮**（含免通道 `0420d99` 的字节）；下轮冷读若再走
  窄形态，基线须按 `E10` 取「自**某一份**已记录整读以来未变」，不得只钉一份记录（本轮开轮读的 `O-1`
  即栽在这里）。
  **轮 2 `CORE-SET-SIGNATURE` CLOSED 2026-08-27**（记录 `v3-{cold-read-d3ba221,review-full-a554c0b,
  review-verify-5e5bebf}.md`，三份皆原样落；journal `core-set-signature-2026-08-26.md`）：契约 v4
  的签字迁至根目录 `CONTRACT-V4-SIGNATURE.md`、`HD-56` 转 `superseded`、签字对象仍 `614932de…`
  不重签；轮 1 归本轮的 8 处残留全清，剥史树真断链 **13→5**（余 5 处：3 处裁决 12 明许、2 处为
  `REVIEW.md:93` 一站点、裁决 13 明许悬空、item G 于轮 3 收）；`CORE-SET.md` 并入
  `CONSTRUCTION-INDEX.md`（裁决 22）。开轮两裁落 `HD-61`（`E2` 授权扩至五处引用降名）与裁决 20
  （`README.md:16` 并入范围）；`HD-60`/`HD-61` 消耗后经用户裁转 `retired`（`a554c0b`）。
  **`E9` 三腿走满、修腿只花一次**：FULL `REVIEWED_NO_BLOCKER`（4 low/3 obs）→ 一次用户批准的修
  `5e5bebf`（答 `L-1`，另三条入 bank，bank 19→22）→ VERIFY `REVIEWED_NO_BLOCKER`（2 low/2 obs）。
  **本轮改动的是三个在仓成员，不是两个——契约 v4 是第三个，其字节欠独立 read 随下轮开轮**
  （blob `dfc983d2…`→`5dfb7b64…`，开轮冷读整读的是旧 blob，故无可引之读；VERIFY `V-1`，本行即其
  载体）；`CONSTRUCTION-CHECKLIST.md` 与 `document-harness/README.md` 同欠。**更正一句已提交的
  结论**（`HD-59` 向前更正，原文留在 journal §9）：该节「本轮花的预算是零」写于 `66dfd30` 时为真，
  此后本轮花掉一次 FULL 加一次修腿，VERIFY `V-2` 点名。
  **轮 3 `CORE-SET-CODE` CLOSED、批 `CORE-SET` 整批 CLOSED 2026-08-27**（记录 `v3-{cold-read-b737742,
  review-full-1db5155,review-verify-7a4e47b}.md`）：v1 package 评审腿整条退役、
  `DEFAULT_REVIEW_RECORD_DIRS` 的值改中性。电池 854→**795**（少的 59 条逐条对账）；
  **全批口径：剥史树非解析引用 31→3**，余三条皆裁决 12 明许。FULL `CHANGES_REQUIRED` → 一次修 →
  VERIFY `REVIEWED_NO_BLOCKER`，修腿只花一次；bank 24→27。**本仓自 2026-08-27 起持有
  `.harness/scan-surfaces.json`**（声明旧目录）——gitignore、每个新克隆须重写，直到记录搬家。
  **未结六条逐条见 plan 的 *What this batch leaves open***，皆不卡。**收批 tip `418477a` 上
  orchestrator 亲测复核**：电池 795 passed · 剥史树真断链 3（皆裁决 12 明许）· 成员 9/9 · 三守卫 exit 0。
  **push 债：`origin/main..HEAD` = 58**（本 session 未推；推与不推归用户）。
- **批 `FREEZE-TO-ALARM`（拆冻结）—— 整批 CLOSED 2026-08-28**。plan
  [`document-harness/plans/freeze-to-alarm.plan.md`](document-harness/plans/freeze-to-alarm.plan.md)
  是 2026-08-27 六条裁决 + 四条答问的载体；理由与实测在各 commit 正文与
  `migration/document-work-assurance-v3/` 的三份 record，此处只留指针。
  **结果**：`E2` 由「无裁决不得写」改为**事后在 commit 正文逐条点名完整仓内路径**；CI job
  `announced-path-disclosure` 逐 commit 机械判定并已设为 `main` 的 required status check；
  `main` 转 **PR flow**（`enforce_admins: true`，仓主同受约束，force-push／删分支皆拒）——
  端点回读实测，非据命令回显。`HD-20` retired；`HD-44` superseded、后继 **`HD-62`** 承载收窄全文，
  **全仓再无「`E2` 写前欠裁决」的活要求**。
  **链**：`464b7dc` 冷读 → `580d236` 其 must-fix → `a2d3fb4` B → `184387c` A → `1d4d9aa` C
  → `0355b36` E → `ad0663d` 勘误 → FULL `CHANGES_REQUIRED` `9580ca9` → 唯一修腿
  `013483f`/`1830d47`/`34d63cc`/`629cff5` → VERIFY **`REVIEWED_NO_BLOCKER`** `a8bfe5b` → `57a31c1`。
  电池 795→**813**（新增 18 条为报警的测试）；九条验收全过；报警在 GitHub 实跑两次（后一次判 8 个
  commit）。**本轮 commit 全直推 `main`、保护落在其后——本批装的 PR flow 没管到装它的这一批**，照记。
  **入 bank 未修四件**：`announced-set-anchor`（十六条路径无本仓可解析枚举，判 design；deadline ＝
  pack 首次增减件）· `e10-freeze-exception` · `archive-header-selfcount`（触碰未兑）· 三条 `E2`
  老 rider 改随下一批。
  **另一件小的**：CI 依赖未固定 ＋ 第三方 Action 不受限（`allowed_actions: all`、可变 tag）。
  用户裁「与 `E2` 无关、单独一件小的」。
  **⚠ 落地流程（已实测一次）**：直推 `main` 被拒，走分支 → PR → 报警绿 → 合；**PR #1 已于
  2026-08-28 合入**（`607ec17`，merge 非 squash，`pull_request` 首次求值取范围正确）。**工作分支
  自此为长期 `dev`**（用户 2026-08-28 裁；CI `on: push:` 无分支限定，推即判）——**代价：轮边界与
  PR 边界可能不重合**，评审走 `dtw dispatch --range`、独立于 PR。
  **无 round journal**：本批的理由与实测只活在各 commit 正文与 plan（历批皆有 journal，本批无）——
  **用户 2026-08-28 于 preclear 裁「认了」，不补**。同批路由的 `R5` observation：`O-2` 报警 YAML 接线
  无测试、`O-6` 两处 mutation 未被钉住，二者入 bank 为 rider `alarm-yaml-untested` / `alarm-mutation-gaps`；
  `O-5`（squash 合并可绕过报警）**已修**：`allow_squash_merge` 关闭——端点回读实测
  `squash=False` · `merge=True` · `rebase=True`。留着的两种安全：merge commit 被报警跳过而它带进来的
  原始 commit 逐个受判，rebase 保留每个 commit 自己的说明；只有 squash 会把 N 个压成 `main` 上的一个
  新对象、让报警去判一段它没判过的文字。未裁而按既有路线走的：`O-4`（`HD-57` 主题被 item A 删除，
  但其状态是 `implemented` 非 `live`、不主张现行要求，属陈旧交叉引用）· `V-2`/`V-3` wording-level 按 `R9`
  随下一批 · `V-4`/`V-5` 已发生、留在 VERIFY 记录里。
- **契约 v4 —— CLOSED 2026-08-23**（轮 `CONTRACT-V4`，`HD-56`：s1/s2 并入 v4 并经用户通读签署；§13 未改、无 s3；豁免簿契约半退役；两份 s 的 UNSIGNED 残迹随文件退役消失；「签 v4 前整份读一遍」的价钱已付）。原立项文案照录：（用户意向 2026-08-04）：§13 自身已允许（"corrections create
  a versioned successor"，v4 即 successor），**不需改 §13、不需 s3**。带进去：s1 四句（§4 control-root
  图行 · §7 invariant 9 · §7 invariant 11 · §8 step 7）+ s2 一句（§3 state-pointer digest）· 清掉契约
  自身 frontmatter 的 `status: candidate-awaiting-user-signature` 自相矛盾（清了之后
  `N1/governance-exemptions.json` 的契约那半可退役）· 两份 s 顶部 "UNSIGNED" 残迹随文件消失。
  （E topology-claim 项已 2026-08-12 按用户裁删除、不带进 v4；「s1 的 S1 改过 §4 topology」这一
  事实仅留此提示。）真代价 = 签 v4 前整份读一遍——这正是"签过=读过"那个等式的价钱。

- **新调用者 onboarding —— CLOSED 2026-08-19**（轮 `CALLER-ONBOARDING`，三期收官）：九条准备工作
  自此有清单且**被实跑验证过**——`document-harness/ONBOARDING.md`（每条＝做什么/怎么看出生效/归谁）+
  decision-log 与 rider-bank 两个空模板 + 第七个命令 `dtw init`（`HD-47`：§1 的「六命令原样」读作搬迁
  指令、非命令数上限）+ `layer_path_check` 归位（仪器仓自己的 tracked hook，十成员 10/10 解析；调用者
  `HARNESS-POLICY.md` §3 与其 `.githooks/pre-commit` 注释同批更正）。**三条诚实上限照记**：无网故 submodule
  源是本地克隆 · Windows 长路径要额外开关 · **作者在自己机器上走自己写的流程，不构成陌生人能照着走的
  证据**——真正的第二个调用者才关得掉后两条。


### 2026-09-01 第三次搬入 —— 批 `CORE-ONLY` 行与 `R5` 观察条（从 `CONSTRUCTION-LEDGER.md` 原样搬入 — 只读，勿续写）

> 用户 2026-09-01 三裁（批 `CORE-ONLY` 收口批准 · ISSUE_TRIAGE 六条路由批 `PROMISE-PATH` ·
> `R5` 观察条退休）；授权与处置在搬迁 commit 正文与 `document-harness/plans/core-only.plan.md`
> step 8。

- **批 `CORE-ONLY` 三轮全 CLOSED（38+5 条裁决与全部处置在 plan [`core-only.plan.md`](document-harness/plans/core-only.plan.md)）**：
  轮 1 `CORE-ONLY-LAYER`、轮 2 `CORE-ONLY-CODE` CLOSED 2026-08-30（链条见 plan）；**轮 3 `CORE-ONLY-RUN`
  CLOSED 2026-09-01**——真产品 run 在调用者 `D:/Thesis-stage-control-refactor`（其 base `2b1ad3b`，挂载
  `3060a23`，sparse 59 件，读审计全程）：一个工单三次 run 产出 A4 amendment 并 promote（前两次诚实停机，
  各自收口正文即证据；r3 FULL 零 blocker → FINAL `ACCEPT` → promotion `d6a5919` → closeout `c184681`）。
  验收 4 就此满足。**归用户三件**（plan step 8）：批收口宣告与 `HD-66` 读法 · 六条仪器侧观察的
  ISSUE_TRIAGE 路由（拟并入 dispatch-economy 或独立批）· 本档 `R5` 观察条的退休。其后队列：候选隔离 ·
  dispatch-economy。**⚠ 本档 20/20 条已顶满**。

- **`R5` 观察：工具键扫类关不掉「调用者解析不到」这一类（用户 2026-08-30 裁「账本单立一项」）**：
  批 `CORE-ONLY` 两轮共六次 pre-FULL 修正 + 轮 2 的两个 blocker，每一圈关掉的都只是当时那把量具看得见的
  形状——`sweep_refs` 只认路径与文件名，漏裸标识符；grep 文件名漏裸 `R<n>`；grep「nine」漏清单外的
  文件；反引号 7 位 commit id 两把量具都看不见（rider `caller-cannot-resolve-ids`）。会话形态那一半
  `HD-69` 已答；**量具这一半未答**：要么换量法（在剥史树上以调用者视角逐 token 解析，而非按写法
  grep），要么承认扫类对此类只能靠独立评审兜底。**再读时刻（用户裁，只此一处）：任何验收靠「对产品
  层扫类」来量的批开轮时**——下一个即轮 3 `CORE-ONLY-RUN`。来源 FULL `v3-review-full-70c82b4.md` `O-3`。
  → retired 2026-09-01（用户裁「退」）：三轮实证选定条目自陈两选中的第二选——此类由真实冷读者＋
  独立评审＋读审计兜底，不造 token 级量具；两笔残差各有家：rider `caller-cannot-resolve-ids`
  （`E10` 设计题）与批 `PROMISE-PATH`（层 3 盲区成文）。

### 2026-09-03 第四次搬入 —— 批 `PROMISE-PATH` 行（从 `CONSTRUCTION-LEDGER.md` 原样搬入 — 只读，勿续写）

> 用户 2026-09-03 收轮裁决「按建议」（批 `PROMISE-PATH` 两轮全 CLOSED）；授权与处置在搬迁 commit 正文与
> `document-harness/plans/promise-path.plan.md` Steps。

- **批 `PROMISE-PATH` 立项，队首（用户 2026-09-01 三裁：批 `CORE-ONLY` 收口批准 · ISSUE_TRIAGE
  六条全数路由本批、独立批插队首 · 本档 `R5` 观察条退休）**：修「规则承诺、引擎无路」类——六条观察
  逐字在调用者三份收口正文（其 `1a634fe` / `fe9f36a` / `c184681`）：blocking VERIFY 后
  `ACCEPT_WITH_LIMITATIONS` 无路 · VERIFY 词表缺「blocker 仍立」值 · 干净 FULL 后修腿不可达（bind 直冲
  `AWAITING_FINAL`，违 `R10`）· `run_evidence_v2` 自写 commit message（`E8` 面）· governance digest 拷贝
  不校验 · `bind-declarations.json` 无 schema、上限只在 bind 咬人。脊柱＝`E4` 反向套件：规则层点名的每个
  处置，引擎要么有被测的路，要么显式落盘「无路」。开批时付 `RULES.md` 两处自由通道欠的层读。
  **2026-09-01 六问全裁**（1a 建路 · 2a 词表加值 · 3 确认 · 两轮 · 第七件并入〔`check_repair_decision`
  不验证，`HD-65` 边界之缺〕· 契约走族内第五裁），载 plan `promise-path.plan.md`。**轮 1 `ENGINE`
  CLOSED 2026-09-03**（件 3–7＋套件落地；FULL `CHANGES_REQUIRED`→修（ii）→VERIFY 绿；bank +3、
  观察路由已裁；链与细节在 plan Steps）。**轮 2 `VOCAB` CLOSED 2026-09-03**（件 1–2＋两 rider 并入；`HD-70` 转写、审毕转 implemented；FULL `CHANGES_REQUIRED`→修（ii）→VERIFY 绿；bank +4；链在 plan Steps）。**批整体 CLOSED 2026-09-03。**
  其后：候选隔离 · dispatch-economy（携 `HD-69`）。CLOSED 的 `CORE-ONLY` 行与退休的 `R5` 条
  2026-09-01 原样搬入 [archive](CONSTRUCTION-LEDGER-archive.md)。
