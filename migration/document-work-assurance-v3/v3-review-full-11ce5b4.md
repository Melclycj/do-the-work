# V3 review — FULL — subject `11ce5b4`

**Subject range** `f4533691..11ce5b41` — one commit, `V3-PHASE-C1-CHECKS-v1`.

**Verdict: `REVIEWED_NO_BLOCKER`.**

The four fixes do what the round claims, each guard binds at value level under an independent
mutation probe, the boundary holds, and the frozen surface is intact. No blocker. Five
non-blocking observations follow §4; the first of them (the range base is an instruction-layer
amendment whose non-waivable read was overridden) is the round's foundation, not its code, and
is surfaced for the user, not adjudicated here.

---

## 1. What this round is, re-derived

Not taken from the dispatch, which carried the range and nothing else (R2).

| Question | Answer | Where I read it |
|---|---|---|
| Round | Phase C1 (Step 5) of `.goals/plans/harness-deletion-first-stabilization.plan.md` — the `checks.py` group, M1–M4 | plan Step 5; commit body's first sentence |
| Governing instructions | `ResearchSystem/document-harness/CONSTRUCTION-CHECKLIST.md` (E1–E12 / R1–R9); the two `v3-harness-*-contract.md` are superseded stubs pointing at it | `v3-harness-review-contract.md` banner; checklist header |
| Budget position | First review of this candidate → this **is** the FULL. No prior `v3-review-*-11ce5b4.md`; branch log shows C0 fully closed and no C1 review commit exists. One user-approved fix + one targeted VERIFY remain (E9) | `git log document-work-assurance-v3`; migration dir listing |
| Verdict domain | FULL → `REVIEWED_NO_BLOCKER \| CHANGES_REQUIRED \| SPEC_GAP` (R3) | checklist R3 |
| Authorization | plan Step 5 (committed) authorizes M1–M4 as one round; two opening rulings recorded for attribution (E10 opening cold-read waive; M3 `FAIL`→`SPEC_GAP` under E2). The preview-card approval and the waivers are chat-issued but their **records** are committed | plan Step 5; commit body; HARNESS-LEDGER pointer block |
| Obligations | fix M1–M4; each with a negative test that was red before it, a positive control, and a mutation probe; suite green; `repo-audit` exit 0; frozen surface intact; stay in the `checks.py` change boundary | plan Step 5 + §Constraints + §冻结面 |

**Ceiling (R7).** The user's E10 waivers/overrides and the preview-card approval were issued in
chat; I see only their committed *records* (`f453369` body, HARNESS-LEDGER, plan Steps 4.6/5 and
Resume pointer). I take the records at face value and state the ceiling; I did not and cannot
verify the conversation in which they were issued. "Fresh context" / independence of prior rounds
is marked, not verified (R4).

**Read coverage (R4).**
- *Read in full:* the `checks.py` diff; the 185 added test lines (the four new classes
  `MarkdownLinkEscapeTests` / `RunAllStopsAtTheFirstGapTests` / `CommandTimeoutTests` /
  `GovernanceQuotedKeyTests` + the added imports); the three tracker diffs
  (`.goals/LEDGER.md`, the stabilization plan, `HARNESS-LEDGER.md`); the range **base** commit
  `f453369` in full; `CONSTRUCTION-CHECKLIST.md`; `local-check-spec.schema.json`
  (`commandExitConfig` + the result `allOf`).
- *Ran myself, pasted below:* all five suites; `repo-audit`; four mutation probes; the three
  signed-blob resolutions; the `run_all` caller grep.
- *Sampled / not re-reviewed:* the ~1,890 pre-existing lines of `test_candidate_checks.py`
  outside the subject's 185 added lines, and the pre-existing helpers the new tests call
  (`frontmatter_keys`, `governance_scan`, `_result`, `_write_evidence`) beyond the diff hunks —
  out of subject scope; I read only their behaviour where a new test depends on it.

---

## 2. Implementation (R3 — lead)

All four fixes verified against ground truth, and each paired guard mutation-probed **by me** in
the worktree: neuter the fix → observe a value-level failure (never a crash) → restore from a
scratchpad copy whose sha256 matched the pre-mutation original on every restore; `git checkout --`
was not used. Backup sha256 `f1f2738947db57cebf6195e16a0f786cd2af12c120addda9119a0ae099b53b87`,
matched after each of the four restores.

### M1 — `_collapse` leaves an escape visible; `_check_markdown_link` reports it broken — **sound**

The old `_collapse` popped whatever sat on top of the stack, so a leading `..` cancelled an
earlier `..`; `../../../README.md` from `docs/guide.md` folded to the root's own `README.md` and
the check PASSed. The new `_collapse` only pops a real name (`out[-1] != ".."`), so every residual
`..` clusters at the front — which is what makes the caller's single test `collapsed[0] == ".."`
a *complete* escape detector: a `..` can never follow a real name in the output, so a non-leading
`..` is unrepresentable. The full-message assertion binds the caller branch and the
`FAIL`-vs-`PASS` assertion binds `_collapse`; both halves of the fix are pinned.

Probe (reverted `_collapse` to the pre-fix pop):
```
>           self.assertEqual(result["result"], "FAIL")
E           AssertionError: 'PASS' != 'FAIL'
```

### M2 — `run_all` raises on the first `SPEC_GAP` instead of finishing the order — **sound**

The old shape collected the gap and ran the whole order, `command_exit` among them, then raised;
the new shape raises immediately. The guard cannot witness this through the exception (identical
either way), so it uses a side-effect sentinel: a `command_exit` ordered after the gap writes a
file, and the test asserts the file does **not** exist. That is the correct — and only —
discriminator.

Probe (reverted `run_all` to collect-all-then-raise; `SpecGap` still raised, so `assertRaises`
still held, and the discriminating assertion is the one that moved):
```
>               self.assertFalse(sentinel.exists(), "a check ordered after the gap still ran")
E               AssertionError: True is not false : a check ordered after the gap still ran
```

### M3 — fixed timeout ceiling; a killed process is `SPEC_GAP`, not `FAIL` — **sound; ruling ② vindicated**

`_run_command` now passes `timeout=COMMAND_TIMEOUT_SECONDS` (module constant `600`, not a request
field) and returns `SPEC_GAP` with a detail string and the partial output as `evidence_ref`,
omitting `exit_code`. The `FAIL`→`SPEC_GAP` ruling is not taste — it is forced by the E2-frozen
schema, which I read at the tip:

```
local-check-spec.schema.json  (allOf branch):
  "if":   kind == "command_exit" AND result in ["PASS","FAIL"]
  "then": "required": ["exit_code"],
          "…WRONG_SUBJECT and SPEC_GAP results carry none, because no process was run —
           reporting exit 0 there would invent evidence."
  separate branch: result in ["FAIL","WRONG_SUBJECT","SPEC_GAP"] → "required": ["detail"]
```

A `FAIL` would require an `exit_code` the killed process never produced; inventing one is what the
schema's own description forbids. Among the closed result enum, `SPEC_GAP` is the only outcome that
needs no `exit_code`, requires the `detail` the code supplies, and stops the run. The config side
carries no `timeout` knob, and the guard asserts that too (`commandExitConfig.properties ==
["allowed_exit_codes","argv","cwd","subject_paths"]`) — independently confirmed.

This is the guard whose behavioural binding the round disclosed rests **solely** on the mutation
probe (its RED phase was an `AttributeError`, a crash, not a value failure). I reproduced the real
defect shape — removed the `timeout=` argument — and got a value-level failure, slow because the
20-second sleep ran to completion:
```
>           self.assertEqual(result["result"], "SPEC_GAP")
E           AssertionError: 'PASS' != 'SPEC_GAP'
1 failed … in 20.49s
```
The ceiling truly fires in the shipped code, and the guard binds the behaviour, not merely the
symbol. (See O-2 on `SPEC_GAP`'s semantic width — non-blocking.)

### M4 — frontmatter key pattern accepts YAML's quoted spellings — **sound**

The pattern became `^(["']?)([A-Za-z_][A-Za-z0-9_-]*)\1\s*:` with the backreference forcing the
quotes to match, and the capture moved to `group(2)`. `"approved_by":` now parses to the key
`approved_by`; a mismatched pair (`"approved_by':`) is not a key and is not valid YAML either. The
guard runs the *actual* `governance_scan` consumer, not just the regex, and asserts the exact issue
code `V3-GOVERNANCE-SELF-APPROVAL`; its two negative controls hold the scope to the frontmatter
block (a quoted mention in the body is not a key) and prevent a false positive on the quoted
*owner* form.

Probe (reverted to the bare-key regex + `group(1)` — the real pre-fix code, not a crash mutation):
```
>               self.assertEqual(frontmatter_keys(...), ["approved_by"])
E               AssertionError: Lists differ: [] != ['approved_by']
```
The quoted key is not captured under the old pattern — the exact bypass, reproduced.

### E5 (expectation independence) — met

Every new assertion compares against a hand-written literal (`"FAIL"`, the full
`"… (resolves outside the repository)"` message, `["approved_by"]`, `["V3-GOVERNANCE-SELF-APPROVAL"]`,
`600`, the explicit property list) or a committed schema value, never the module's own constant,
and asserts whole values rather than an unrelated substring.

---

## 3. Boundary / process conformance (R3 — run second)

**E3 — figures re-derived at the tip, pasted not described.** Five suites, all green, at exactly
the counts the commit claimed (re-derived, not trusted):
```
document_harness          147 passed
document_harness_review   321 passed
harness (run_tests.py)     39 tests OK
stage_control              20 run, 0 failure(s)
tooling/tests/run_tests.py 29 passed        RESULT: OK
repo-audit.py             exit 0            RESULT: clean (exit 0)
```

**E2 — frozen surface intact.** The three signed blobs resolve, at the subject commit, to exactly
the recorded prefixes, and none is the file this round edited:
```
8ad404b1…  .goals/plans/document-work-assurance-harness-v3.plan.md   (signed plan)
b2dbdf75…  ResearchSystem/contract/Document-Work-Assurance-Contract-v3.md
68031fa2…  ResearchSystem/contract/Document-Work-Assurance-Contract-v3-supersession-1.md
```
The subject's five changed paths — `checks.py`, `test_candidate_checks.py`, `.goals/LEDGER.md`,
`.goals/plans/harness-deletion-first-stabilization.plan.md`, `ResearchSystem/HARNESS-LEDGER.md` —
touch **no** frozen path: nothing under `schema/document-assurance-v3/`, nothing under
`ResearchSystem/contract/`, and neither oracle (`expected-construction-prompt.txt`,
`test_readme_enumeration.py`). The edited plan file is the writable stabilization *tracker*
(blob ≠ 8ad404b1), which E2 explicitly permits.

**E8 — git discipline.** Single dense title `V3-PHASE-C1-CHECKS-v1`; one paragraph body; no
trailers; one parent (a new commit, not an amend or merge); the commit's kind is named
("Candidate for Phase C1"). One caveat carried to O-3.

**E9 — budget.** This candidate is the first FULL subject on Phase C1; it consumes no repair
budget, correctly self-classified ("no independent FULL has occurred on this round"). My FULL is
the round's one FULL.

**E10 — instruction layer (subject).** The subject touches no instruction-layer byte
(`checks.py` code + tests + trackers; no schema `description` was amended), so C1's opening
cold-read waive is the within-rule clause E10 provides, correctly framed. The HARNESS-LEDGER
records this and distinguishes it from the amendment-read overrides — internally consistent.
(The **base** commit's amendment read is O-1.)

**E12 — range.** Base written `f4533691`, tip `11ce5b41`. I verified `11ce5b41` is the branch
HEAD with no commits after it, so the written tip coincides with HEAD and drops no records; the
E12 concern does not bite this dispatch.

**E1 — independence.** This review set its own questions, re-derived every figure, and ran its own
probes in a detached worktree; no executor output was accepted as a verdict input.

**Tracker diffs.** All three are the disclosed housekeeping: checkbox flips (4.5/4.6/5), the C0
close-out round-chain, C1's two rulings and three disclosures recorded for attribution, and the
resume-pointer rewrite (which itself carries the O-1 flag). No instruction-layer or frozen content;
no load-bearing change smuggled in.

---

## 4. Observations (non-blocking; not inflated — R3)

**O-1 — the round's foundation, not its code. The range base `f453369` is an instruction-layer
amendment whose non-waivable E10 read was overridden, and C1's dispatch depends on it.**
`f453369 V3-E12-RANGE-TIP-v1` adds one sentence to E12 (tip is HEAD, never a written SHA). I read
it in full: it is additive in E10's sense — the prior two E12 sentences survive verbatim, only
re-wrapped — and its effect on *this* dispatch is null, since the tip already equals HEAD. But its
independent read was **overridden**, not waived: the commit body, the HARNESS-LEDGER, and the plan
each state that E10 attaches a waiver clause only to the round-opening cold read and gives the
amendment read no exit, and that this is the **second** such override of the same rule in one day
(C0 was the first). Per R5 I report the shape and not a conclusion: a non-waivable read is being
routed around by override on consecutive rounds, and whether that is acceptable is the user's call.
Per R7 I state the ceiling — the override is recorded and I take it at face value — and I do not
convert it into a blocker: the missing artefact is an E10 *read*, which by R3 spends no budget and
carries no verdict, so it cannot ride the FULL's single repair, and the subject's own code is not
what is wrong. **Surfaced for the user's decision.**

**O-2 — `SPEC_GAP` is used slightly wider than its schema definition.** The schema defines
`SPEC_GAP` as "a schema-valid request whose declared subject could not be resolved"; a wedged
command is a different failure mode (it ran but did not finish). Within the closed result enum it
is nonetheless the only representable outcome (PASS/FAIL need an impossible `exit_code`,
WRONG_SUBJECT is about the observed tree), and widening the enum or making `exit_code` optional is
exactly the schema amendment E2 bars without a higher ruling. The detail string is explicit, so no
consumer is misled. The `SPEC_GAP` `description` does not yet mention the timeout case; recording
that as a wording-level note (R9-bankable, no round) for the next batch that touches the frozen
schema — if and when a ruling reopens it.

**O-3 — the C1 commit bundles Phase C0's close-out tracker edits.** Disclosed ("the ledger and
plan edits describing Phase C0's close were uncommitted at handoff and are carried in here"). The
4.5/4.6 checkbox flips and the C0 chain belong to C0's change surface, not C1's, so this is a minor
stretch of E8's "stay inside the round's declared change boundary." It is harmless (tracker text,
no behaviour) and the honest alternative — leaving them dangling — is worse. Noted, not charged.

**O-4 — M2 repairs an unwired API.** I confirmed `run_all` has zero callers anywhere in the
repository outside its own test (grep: only the import, docstring, and two test call sites). M2
changes no runtime behaviour today; the fix and its guard are real, but the product path does not
yet reach them — the same unwired state C0 found in the CLI. Whether/when to wire it is the user's
question (R5), not a defect.

**O-5 — M3's behavioural binding is probe-only, as disclosed — and I re-ran the probe.** The RED
phase was an `AttributeError` (the constant did not exist), i.e. a crash, which per R8 proves the
test touched the code, not that it binds the behaviour. The binding evidence is therefore the
mutation probe, which I reproduced independently (M3 above, value-level red, 20.49 s). Honest
disclosure, verified — recorded so the reliance is visible, not as a fault.

---

## 5. Verdict

`REVIEWED_NO_BLOCKER`.

M1–M4 do what the round claims; each guard binds at value level under an independent, real-defect
mutation probe; the tests' expectations are independent literals; M3's `SPEC_GAP` ruling is correct
against the frozen schema; and the boundary — frozen surface, git discipline, budget, range,
instruction layer of the subject — holds. The five observations are non-blocking: O-1 is a
foundation question for the user (an overridden non-waivable read, whose amendment is benign and
whose effect here is null), O-2 is a bankable wording note, and O-3/O-4/O-5 are disclosed shapes I
independently confirmed. None would survive as a blocker, and none should burn the round's single
repair.

Per E9, `REVIEWED_NO_BLOCKER` sends the plan to Step 6 · Phase C2 (flow/summary group, M5–M7).

---

*Record written by the independent review session in the worktree (R6); the execution side commits
it, title `V3-REVIEW-RECORD-PHASE-C1-11ce5b4-v1`. This review carries no verdict on `f453369`
itself — it is the range base, outside the subject — only on how C1 depends on it (O-1).*
