# Review-side handoff — 2026-07-21

**What this is.** A routing note authored by the **independent review side** after the V3-N2
FULL + VERIFY rounds. It is **not a node artifact**, carries **no verdict**, names **no acceptance
ID**, and sits at the migration root — outside every node's `N<n>/**` allowlist — for the same
reason the two agent contracts do.

**Standing.** The review side may not update a pointer, write a node candidate, or set the
execution side's agenda. So the two items below are **reported, not assigned**: the user is the
routing point. Committing anything here is the execution session's act, never the reviewer's.

**Lifetime.** §1 is disposable — delete or supersede this file once actioned. §2 is a pointer to
durable content that outlives it.

**Observed state when this was written** (re-derive before acting — the branch was moving):

```
观测时刻   2026-07-21 00:35:41 +1000
HEAD       00c78fd  V3-N3-WITNESSED-CASE-ADDENDUM-v1  (2026-07-21 00:13:55 +1000)
push debt  47 commits ahead of origin/main
untracked  ResearchSystem/docs/General-Harness-v2-Design.md          (pre-existing, not this session's)
           ResearchSystem/migration/.../v3-review-note-obligation-authoring.md   (review side, §2)
```

---

## §1 — `.goals/LEDGER.md` has drifted, in four places

Found by reconciling the ledger against `git log` during a session-close pass. Reported here
because the ledger is the execution side's to write: for node state the durable ledger **is** the
node record, and `.goals/LEDGER.md` is excluded from the N1–N3 allowlists (plan §9), so touching it
is an out-of-node act either way.

| # | Line | Ledger currently says | Repository reality |
|---|---|---|---|
| 1 | 9 | *"V3-N0 and V3-N1 both CLOSED and signed; **V3-N2 awaiting explicit user authorization**"* | V3-N2 authorized → built → FULL (`CHANGES_REQUIRED`, 1 blocker + 7 findings) → user-approved bounded fix (blocker + F1–F6; F7 disclosed as residual **N2-R6**) → targeted VERIFY (`PASS`, 3 residuals recorded) → **closed at `655bae5`**. V3-N3 is already past two commits. |
| 2 | 89 | *"⚠ 断点 = V3-N2 is NOT yet authorized. The signature closed N1 only…"* | Same. The 断点 is now V3-N3, whose plan §8 gate is *deterministic results + real-pilot user adoption decision, **no extra code FULL***. |
| 3 | 117 | *"v3 `document-work-assurance-v3` = **40 commits** ahead"* | **47** at the timestamp above. Re-derive: `git rev-list --count origin/main..HEAD` |
| 4 | 28 | *"Push debt (re-measured 2026-07-20 …): **31 commits** ahead"* | Same figure as #3 — two mutually inconsistent stale counts (31 / 40) live in one file, which is itself the drift signal. |

Also worth a pass while in there: line 88 still reads *"**R2 → V3-N2** (`N2-A7`) still open"* — N0-R2 was
discharged at V3-N2 (see the N2 record §4).

**Timing.** Do **not** do this mid-N3. `1e34a1e` (`V3-LEDGER-SYNC-v1`) set the pattern — a separate
out-of-node commit — but it landed **between** nodes. Editing `.goals/LEDGER.md` while an N3
candidate is open dirties the worktree that N3's own changed-path derivation reads (the N2 record
§7.4 had to account for an untracked path for exactly this reason). Wait for the node boundary.

**None of this is a defect in any node.** It is a shared pointer going stale while the work moved —
the failure mode a fresh session hits first, because line 9 is the first thing it reads.

---

## §2 — A review-side note exists; **do not act on it during V3-N3**

File: `ResearchSystem/migration/document-work-assurance-v3/v3-review-note-obligation-authoring.md`
(untracked, review-side, same standing as this file).

One-line summary: **a WorkSpec author can declare an obligation `review_only` when a deterministic
check was possible (an effort gradient, not ignorance), and can word an obligation so that nothing
could ever falsify it — and v3 measures neither.**

Three things about it, so nobody has to open it to route it correctly:

- **It is not a finding against V3-N2, or against any node.** No acceptance ID or signed clause is
  violated. It is a product-side property that has never been claimed at any node.
- **Its landing site is `document-work-spec.schema.json`, an N0 signed schema** — so any change is
  an out-of-node amendment (the `8efe3e9` pattern) or a post-v3 revision, never a small edit.
- **Its correct sequencing is after V3-N3**, and N3 is the thing that supplies the evidence for it.
  The note names the concrete question to carry into the shadow runs:

  > *What fraction of this run's obligations are `review_only`, and how many of those could a script
  > have verified?*

  A real occurrence justifies amending a signed schema; no occurrence is the evidence not to build
  it. Plan §9's N3 measure list already asks for `obligation omissions` and `unused mechanisms`.

**So: register it, do not implement it, do not fold it into an open N3 candidate.** Injecting a new
upstream consideration into a node in flight is scope creep in its standard form. The user has said
they will revise the note themselves.

The execution side did **not** know about this when `V3-N3-WITNESSED-CASE-ADDENDUM-v1` was written —
confirmed by the user. The two are unrelated; the name collision on "witnessed case" is coincidental.

---

## What this file is not

Not a verdict, not a review round, not an authorization, and not a node artifact. The V3-N2 budget
is fully spent (FULL 1/1, fix 1/1, VERIFY 1/1) and no round is open on V3-N3. Nothing here obliges
the execution side to do anything — it obliges only the user, who decides what gets routed where.
