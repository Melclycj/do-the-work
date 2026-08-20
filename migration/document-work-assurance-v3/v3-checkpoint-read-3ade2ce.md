# Amendment checkpoint read — `e3c7446` + `3ade2ce` (the scope-discipline corrective batches)

The rule-1 / §12 checkpoint read both batches declare they owe. **Not a round in §3's sense:**
it consumes no plan-§8 budget and carries **no verdict** — findings only, tiered
must-fix / low / observation. Its authorization is the `ADOPT_DOCUMENT_V3` standing-discipline
entry (N3 record §8; N3-R10) plus the user's routing of this read to this session; the ledger's
当前指针 names it as the one genuinely open review before the ①⑤ construction rounds may rely
on the amended scope-discipline text.

**Subject, re-derived before reading any content:**

- `e3c7446` (`V3-SCOPE-DISCIPLINE-CHECKPOINT-FIX-v1`), parent `763ef2a` — the checkpoint-read
  record commit, as required. Numstat 32+/15− (execution contract), 13+/3− (review contract);
  matches the message's own "32+/15- and 13+/3-".
- `3ade2ce` (`V3-SCOPE-DISCIPLINE-DENARRATE-v1`), parent `e3c7446`. Numstat 51+/45− and
  19+/14−; total 70+/59−, matching `--stat`.
- `git diff 3ade2ce..HEAD` over both contract files is **empty** — the worktree text at tip is
  the amendment text, so the current files were read as the subject.
- Worktree: both contract files clean; the only deviation is untracked
  `ResearchSystem/docs/General-Harness-v2-Design.md` (see observation O3).
- Both batches touch only the two contracts — no earlier commit's signed bytes involved.

**Yield:** 1 must-fix + 3 low in ~96 new/changed lines, plus 4 observations. The §12 precedent
predicts ~3 per 79; this is at rate. The must-fix is the same defect class all three
scope-discipline batches have now carried in turn: an overstated universal about a history the
writer had just lived.

---

## Findings

### F1 — must-fix — "every one of them in the narration, none in the rules" is false, and its own sentence proves it

**Locators, three sites:**

- Execution contract, Scope discipline pointer paragraph, verbatim —

  > its own checkpoint read returned six findings — every one of them in the narration, none
  > in the rules

- Execution contract provenance note (second 2026-07-26 entry) and the review contract's
  identical copy, verbatim —

  > All six findings were in the narration and none in the rules, so removing it moots five of
  > them; C5, which was the two contracts disagreeing over whether a review may *raise* the
  > ratchet, was a real defect in the rules and its correction stands.

The sentence contradicts itself within one breath: if all six were in the narration, deletion
would moot six, not five. The reason it moots five is precisely that C5 was **not** narration —
its site was the ratchet paragraph *inside numbered rule 1* ("a review is structurally
incapable of raising it"), which is why its correction survives in the rules today (the
"incapable of *concluding*" sentence). The section-body version is worse than the note: it
carries no C5 qualifier at all, and this layer's stated risk is exactly that a number written
here is what a later round will cite as established.

Secondary imprecision at the same site: the section-body sentence attributes all six findings
to "this section", but C2's primary locator was the **review contract's §10**, not this
section.

**Minimum fix:** in all three sites, "five in the narration it replaced; the sixth (C5) was in
the rules and is corrected in place" — and in the section body, "the amendment's checkpoint
read" rather than "its own", since the read's subject was both files.

### F2 — low — "this file's own opening discipline" is true in one file and false in the other

**Locator:** the second 2026-07-26 provenance note, identical in both files, verbatim —

> What remains is the rules plus a pointer to the records — this file's own opening
> discipline, applied to itself.

In the execution contract this is accurate: its opening block states "**State is not
duplicated here.** … a second copy drifts the moment the node moves." The review contract's
opening states no such discipline — its no-duplication sentence lives only in §10's new tail,
added by this same batch. The note was written once and pasted into both files, and its
self-reference survives the paste in only one of them. Hunt-list item 6's shape: a document
asserting something about itself that is not true of itself.

**Minimum fix:** in the review contract's copy, "the harness's no-duplication discipline" (or
point at the execution contract's opening).

### F3 — low — the first 2026-07-26 note's "Owes a rule-1 checkpoint read" flag is discharged but still standing

**Locator:** both files, first 2026-07-26 provenance entry, closing sentence, verbatim —

> **Owes a rule-1 checkpoint read before any round relies on it.**

That read occurred (record committed at `763ef2a`), its findings were applied (`e3c7446`) and
then denarrated (`3ade2ce`). The harness's own convention closes the flag on the note once
discharged — the 2026-07-22 §12-amendment entry was edited to "Corrected same day after the
amendment's checkpoint read — … findings: [link]". Here a cold reader applying rule 1
literally would first conclude the scope-discipline section is unusable, then have to infer
the discharge from the *following* entry. Low, because the following entry does carry the
story; but the standing flag is the exact stale-pointer shape the ledger warns about.

**Minimum fix:** append a discharge pointer to that entry ("Read same day — findings applied,
then superseded by the denarration batch below; record:
[`v3-checkpoint-read-1d25aae.md`](v3-checkpoint-read-1d25aae.md)").

### F4 — low — rule 2's closing instruction prescribes a mechanism the repository has since deleted as unnecessary

**Locator:** execution contract, Scope discipline rule 2, verbatim —

> annotation alone is not enough: prose has never terminated this class here, so add the check
> that reads its own source and refuses the module-qualified reference.

At the batches' commit time this matched reality (the G1 source-reading guard existed, and
`389173b` hardened it to AST within the hour). Two commits later the golden-file round
(`e5c6005`) **deleted that guard along with its reason to exist**: the expectation moved into
a committed fixture (`tooling/tests/fixtures/expected-construction-prompt.txt`), removing the
in-file duplication the guard policed; `df2b84d` swept the orphaned `import ast`. Verified at
tip: no source-reading check remains in `test_dispatch.py`, and `389173b` is an ancestor of
`HEAD`.

So the repository's own final resolution of the incident is a third shape the rule does not
name — **externalize the expectation so no in-file duplication exists to guard** — and it is
rule 1's own principle applied to the meta-guard itself (machinery added to close a finding,
deleted a round later). A future round following the sentence literally will rebuild deleted
machinery.

The rule is not wrong where its premise holds: *if* the hand-written literal must stay in the
test file, the source-reading check is the proven termination of the class. But the sentence
states the check as the unconditional next step after annotation.

**Minimum fix (next instruction-layer batch, not urgent):** name the fixture option first —
"prefer moving the expectation into a committed fixture file, which removes the duplication
outright; where the literal must stay in-file, add the check that reads its own source and
refuses the module-qualified reference."

**Honesty note:** `e5c6005` and `df2b84d` are unreviewed by explicit user ruling (the
cancelled dispatch-generator reviews). This finding takes their existence and stated shape as
repository facts; it does not certify them as good.

---

## What I checked and found sound

Stated by dimension, because a silent dimension is indistinguishable from an unchecked one.

- **C5's correction stands and restores the counterpart property.** Execution side now reads
  "structurally incapable of *concluding* it … A reviewer may and should report the shape —
  the review contract's §10 instructs exactly that"; review §10 retains "say so as an
  observation … I cannot conclude it should go." The two sides agree. **No SPEC_GAP.**
- **The denarration's arithmetic is right.** C1, C2, C3, C4 and C6's defect sites are all
  gone from both files (re-checked against each C-finding's verbatim locator); C5's corrected
  sentence survives. Five mooted, one fixed — the *count* in the note is correct; only the
  "all six in narration" framing is wrong (F1).
- **No dated measurement survives in the rules themselves.** Rule 1 and rule 2's surviving
  illustrative material is generic shape (`assertIn("2", …)` against 40-hex output; allowlist
  built from the source it polices; schema validated against itself) — names no count, no
  date, no finding ID. The one surviving count sits in the pointer paragraph and is F1.
- **Quotes are faithful.** The review charter §8 opening quoted in rule 1 truncates at
  "myself" faithfully; "§5.1 forbids a reviewer to accept a reported number" is an accurate
  characterisation; hard rule 4's characterisation ("how to *detect* a powerless guard and
  not how to avoid building one") matches hard rule 4's text.
- **All four linked records are tracked at tip** (`git ls-files`):
  `v3-review-full-0439efe.md`, `v3-review-verify-d55d5ce.md`, `v3-review-full-c6d4eb4.md`,
  `v3-checkpoint-read-1d25aae.md` — including the third, which the 1d25aae read had recorded
  as untracked at its time.
- **The false-authorization correction is consistent with everything I can see.** The claimed
  disposition's absence is a cross-session fact I cannot verify (review contract §10 ceiling);
  the ledger's account corroborates the note's, and the correction's direction — replacing a
  claimed authorization with a statement of what actually happened — is the honest one. Raised
  as consistent, not as verified.
- **Nothing mechanical moved, re-derived myself at tip:** `pytest` 426 passed; compiler golden
  29/29; `repo-audit.py` exit 0. Correct for an instruction-only change; per discipline rule
  3, green suites are not evidence about this layer — the read is.

---

## Observations — no fix owed

1. **O1 — "The rules are unchanged in substance" undersells the batch.** `3ade2ce`'s message
   discloses the rule-2 source-reading instruction as new, but the batch also added rule 1's
   "a caveat conceding as much is a confession dressed as a feature" and "Watch the ratio:
   components added to close findings, against components still alive a round later", and
   rule 2's closing "Never trust a guard you have not seen fail." All are improvements, and
   messages are immutable provenance — recorded so a later reader does not take "unchanged"
   at face value.
2. **O2 — hunt-list item 8 still carries its own mini-narration** ("Found this way on the
   dispatch rounds, twice in the same file within one day, the second time inside the fix for
   the first"). Outside this subject — it is `1d25aae` text, already read and verified
   accurate — but it is a second copy of record content and will drift exactly as the new
   pointer paragraphs warn. Candidate for the same denarration treatment at the next batch.
3. **O3 — untracked `ResearchSystem/docs/General-Harness-v2-Design.md`** sits in the worktree.
   Not a smuggled change to the subject files (they are clean); recorded per §2's worktree
   check so it is attributed before anything else lands near it.
4. **O4 — the yield pattern is now three-for-three.** The amendment overstated its history
   (C1–C6); the fix batch misstated its authorization; the denarration batch overstates its
   own completeness (F1). Each batch's defect was in the part written *about* the just-lived
   act, never in the rules. The rules themselves have survived three reads unchanged in
   substance — which is evidence they are sound, and evidence the checkpoint-read requirement
   is doing exactly what it was bought for.

---

## Coverage and recompute list

- **Read in full:** both batches' diffs; both contracts at tip (the operative amendment
  text); `v3-checkpoint-read-1d25aae.md` (the C1–C6 ground truth).
- **Probed:** `test_dispatch.py` guard region at tip; `389173b` / `e5c6005` / `df2b84d`
  messages and stats (F4's timeline); `ResearchSystem/docs/` listing.
- **Not read:** the three pointed-at review records' bodies — they are the pointer targets,
  not the subject; their link integrity and tracked status were verified.
- **Recomputed myself, accepting no reported number:** both parents; both numstats; the
  empty `3ade2ce..HEAD` diff over the contracts; `git ls-files` on four linked records;
  `389173b` ancestry of `HEAD`; absence of `import ast` and of the source-reading guard at
  tip; pytest 426; golden 29/29; repo-audit exit 0.

---

*Authored by the **execution session**, not the review side — recorded plainly because a
standing claim the repository does not hold is the defect class these batches exist to refuse.
The user routed this read here and granted a one-time dispensation (2026-07-26): the ①⑤
executor rounds had not started, so the read reviewed no work of this session's own. It does
not set a precedent — the role rule stands (one session per harness role), and future
instruction-layer reads go to an independent review session. Not a node artifact; outside
every node allowlist; bears on no verdict.*
