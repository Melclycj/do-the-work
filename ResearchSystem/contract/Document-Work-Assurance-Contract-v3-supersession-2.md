# Document Work Assurance Contract v3 — supersession 2 (narrowed state-pointer digests)

**Status: authored at Phase C1.6 (2026-07-29); UNSIGNED.** This file is a
versioned successor under the signed contract's own §13 rule — *"Signed contracts are never
amended in place; corrections create a versioned successor"* — the same rule
[`supersession 1`](Document-Work-Assurance-Contract-v3-supersession-1.md) was written
under, and it is authorized by the user's 2026-07-29 adjudication narrowing state-pointer
digests. The signed
[`Document-Work-Assurance-Contract-v3.md`](Document-Work-Assurance-Contract-v3.md) and
supersession 1 both stay **byte-identical**; nothing here rewrites either. This file
carries exactly one statement supersession and nothing else. Where it is silent, the signed
contract and supersession 1 govern unchanged.

## 1. What is superseded, and why

Supersession 1 §3 states, without qualification, that a state pointer carries the bytes
digest of the pointed-at file. That sentence is now false for most state pointers, and this
file makes the contract say what the harness does instead of leaving a signed statement the
code contradicts.

The adjudicated ground: the digest is computed by the executor, over a file the executor
wrote, and checked against a pointer the executor also wrote. Against the one actor it
would have to constrain it therefore binds nothing — that actor can change file and digest
together in a single consistent edit. What it does still catch is an **uninformed
mis-write**: a write that did not know the pointer was there. That is worth having only
where a mis-write followed by the executor regenerating the file would be **forgery** —
where the executor is not entitled to author the file's current version at all. The
criterion is permission, not value, and it is asked about the *current* version, not about
who wrote the first one.

Witnessed grounds: thirteen state pointers carried digests and four pointer-ref families
carried digests no code in the v3 package ever read back; `cf51534` moved evidence paths
and invalidated the digests of eight committed ISSUE_TRIAGE decisions — five in `p3-corr`,
three in `w1-r1` — while the whole test suite stayed green — a binding nothing was checking,
on files nobody was checking it for
(`issue-p3-corr-digest-binds-nothing-against-the-only-writer`, triaged `CORE_CANDIDATE`,
scoped to `p3-corr` where five is exact; the w1-r1 three fall out of the same recomputation).

## 2. The supersession

### S1 — §3 "Version boundary", the state-pointer digest bullet

Signed text (supersession 1 §3, final bullet):

> A state pointer carries the **BYTES digest** of the pointed-at file (the w1-r1
> pointer-digest-kind lesson, triaged `CORE_CANDIDATE`); the documented authoring path is
> the `assurance_state.pointer_to` helper, which computes the bytes digest itself.

Successor text:

> A state pointer carries the **BYTES digest** of the pointed-at file **when, and only
> when, its field is one the executor may not author the current version of**:
> `work_spec_ref`, `start_decision_ref`, `repair_decision_ref`, `final_decision_ref` and
> `review_ref` (`assurance_state.DIGEST_PROTECTED_FIELDS`). Every other state pointer
> carries the path
> alone; `pointerRef` requires only `path`, so this needs no schema change. The documented
> authoring path is the `assurance_state.pointer_for` helper, which applies the field
> policy and delegates to `pointer_to` for the digest; `pointer_to` remains correct for
> what it does and is **no longer the authoring path for a newly opened run** — closed-run
> scripts under `assurance/runs/` and the helper's own tests still call it directly, and
> nothing here asks them to change. **When a digest is present it is still of
> the pointed-at file's bytes and is still verified** — the w1-r1 pointer-digest-kind
> lesson is unchanged, and a wrong digest on any field remains `POINTER-STALE`. What
> changed is the obligation to write one, never the meaning of one that is written.

## 3. Version boundary

A state pointer is authored under the successor text when it is written by
`assurance_state.pointer_for`; one written by `pointer_to` or `pointer` directly is under
the prior text where the two texts differ; for an unprotected field written as a bare
`pointer(path)` they do not. The boundary is the authoring call, not a date, and the unit is the pointer
— the same granularity §2 quantifies over — because a single run may author some pointers
each way, which §4 says is the shape to expect. It is decidable by reading the writing call,
which is what supersession-1 achieved with a `schema_version` constant and what a time word
could not. Closed runs and shadow rounds
keep the digests they were written with as **pinned history**: no migration, no re-write,
no retroactive removal — a record edited to match a later rule stops being a record of what
happened. Existing digests on closed runs remain verifiable exactly as before.

## 4. What this supersession does not touch

- **No schema byte changes.** `pointerRef` already made `digest_sha256` optional; this
  narrows which fields are obliged to supply it, and nothing in `schema/` is amended.
- **The `digestRef` side is untouched.** The plan's `work_spec_ref` binding and the
  review/summary/profile digest comparisons continue to require and check a digest; those
  refs require `[path, digest_sha256]` by schema and are outside this statement entirely.
  `instruction_ref` is **not** among them — it is a `frozenFileRef`, required as
  `[path, revision]`, and nothing requires or checks a digest on it; it was named here in
  error and is outside this statement for a different reason.
- **Detection strength is stated, not glossed.** The surviving digests detect an uninformed
  mis-write. They do **not** detect a consistent rewrite of file and digest together, and
  they never did — this file records the limit rather than narrowing it.
- **Coverage of the narrowing is partial and named.** `assurance_state.pointer(path,
  digest)` still accepts a caller-supplied digest and is used directly by hand-written run
  scripts, so a run authored by copying an existing precedent will keep writing digests on
  unprotected fields. Nothing here forbids that; the obligation the successor text removes
  is on the documented authoring path.
- **Only one protected field has a live write path.** Of the five, only `review_ref` is
  authored by `templates/run-v2/` (`run_bind_v2.py`); the other four are written by
  hand-authored run scripts, which this successor text governs but no shipped template
  exercises. So "protected fields still carry digests" is demonstrated end-to-end for one
  field and by unit test for the rest. Stated here because a contract implying uniform
  coverage would be the same kind of defect this file corrects.

## 5. Signature

This file is **UNSIGNED**. Under `E10` it is a prose successor to signed text and owes an
independent read before any round relies on it; that read's subject is this text, it is
never banked as a round's FULL, and its record lives under
`ResearchSystem/migration/document-work-assurance-v3/`. A user signature, when given, means
this one supersession and the §3 version boundary are frozen for successor runs; the
signature record (exact blob + candidate SHA + date) lives in the round record, never
inside this file.
