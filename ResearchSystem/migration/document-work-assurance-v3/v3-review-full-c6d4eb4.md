# V3 construction round — FULL review of `d55d5ce..c6d4eb4`

Review-side output for the construction-dispatch deletion round. Authored by the independent
bounded reviewer under [`v3-harness-review-contract.md`](v3-harness-review-contract.md);
**not a node artifact**, outside every node allowlist, binds nothing. Committing it is the
execution session's act, not the reviewer's.

Predecessors: [`v3-review-full-0439efe.md`](v3-review-full-0439efe.md) and
[`v3-review-verify-d55d5ce.md`](v3-review-verify-d55d5ce.md) — the round whose five findings
this round deletes rather than repairs.

- **Round:** this range's one FULL. §3's discriminator: no commit in `d55d5ce..c6d4eb4`
  records an independent FULL, so both commits are pre-submission and this is it. **Budget
  after this round: the fix and the targeted VERIFY are unspent.**
- **Verdict:** `PASS` — no blocking discrepancy found within the frozen subject and the
  review dimensions in §5. Per §4 that is all it means.
- **Findings:** 4, none blocking. The first is the one that matters.

**§3 anti-renaming test, applied explicitly.** The previous round's budget was exhausted, so
a continuation under a new name is exactly what §3 exists to catch. This is not one: the
subject is different, no commit here repairs F1 or V1–V4, and the code those findings were
about is *removed*, which moots them rather than patching them inside a closed round. That is
the shape my own VERIFY named as the legitimate path — "a new authorization, not a
continuation." §10 ceiling: `c6d4eb4` asserts "User-authorized deletion round"; I cannot
verify the authorization, only that its shape is right and that the user routed this range as
a fresh subject.

---

## 1. Subject re-derivation

| Check | Result |
|---|---|
| parent == last reviewed commit | `d55d5ce` = the VERIFY's tip |
| unique direct child | `git rev-list --children` gives `d55d5ce` exactly one child, `96cedb5` |
| range linear | 2 commits; `--merges` count 0 |
| HEAD == tip | `c6d4eb47789f230a2dda0cc62f1f67b42e993e24` |
| worktree carries no smuggled change | no tracked-file modification; the same pre-existing untracked `ResearchSystem/docs/General-Harness-v2-Design.md` as at both prior rounds |
| changed paths | **3**, counted by hand: `…/v3-review-verify-d55d5ce.md` (A), `dispatch.py`, `test_dispatch.py` |
| churn | recomputed: **empty** |
| A4 `f91a7c4` is not an ancestor | confirmed |

**Permanent boundaries — intact.** Plan blob `8ad404b1…`, review-contract blob `6b170d8c…`,
execution-contract blob `31179580…` byte-identical base↔tip. Net diff over
`ResearchSystem/schema/`, `document-harness/`, `contract/`, `.goals/plans/` is **empty**. No
instruction-layer amendment, so **no rule-1 checkpoint read is owed**.

**§12 cold read — not owed, reasoning stated.** The referent is "the opening of each
construction-side round." This range's work is the deletion itself; the instruction layer is
untouched and nothing in this round relies on an amended reading of it.

**The VERIFY report was committed unaltered.** `96cedb5` touches that path once and only that
path; 276 lines, structure and all four V-headings match what I authored, no execution-side
commentary inserted. Its commit message states the budget position correctly.

**The prompt I was handed this round was a fragment.** What arrived was the `**Subject:**`
line alone, with no charter pointer and no derive-instruction. Regenerating at HEAD shows the
command emits the full prompt — the omission was in the paste, not the code. Recorded because
"the instruction paragraph is missing" was exactly V1's failure mode and had to be excluded
before anything else.

---

## 2. What the round did, and whether the deletion is sound

`churn_of`, `merge_count`, `commit_count`, `CONSTRUCTION_FIXED_LINES`, `_MERGE_CAVEAT`,
`construction_subject_line` and the partition guard are gone. What remains is
`CONSTRUCTION_PROMPT` — one constant, two substitutions — and three one-git-call checks
(resolvable, ancestral, non-empty).

**The argument for deleting is correct, and it is stronger than the round states.** §8 opens
"One commit SHA. Nothing else. Everything else I read from the repository myself" and §5.1
forbids me to accept a reported number, so a dispatched churn list must be recomputed by its
recipient — which is what both reviewers did. The DAG objection is also right: count a merge
and a path revised once on the merged branch is reported as churn; do not count it and the
merge's content is invisible; there is no third answer. Calling the upper-bound caveat "a
confession dressed as a feature" is an accurate self-assessment.

One correction to the round's own reasoning, in the round's favour and against my earlier
report: I told the user in-session that churn had one non-vacuous use — it surfaced
`HI-dispatch-p3corr-issues.md`, a path added and deleted inside the range and therefore
absent from `git diff`. That remains true as an observation about *net-invisible paths*, but
it is not an argument for keeping `churn_of`: "revised more than once" only caught that path
incidentally, and a reviewer who wants net-invisible paths derives them directly. The
deletion does not lose anything I actually used.

**The product half is untouched and still earns its keep.** Its refusals — a closed run, an
incomplete evidence set, two control roots in one commit, a non-evidence commit — are
mis-routes a human cannot see. Verified: no product-side code or test changed in this range.

---

## 3. Findings

### G1 — must-fix — the new guard's independence is load-bearing and held by prose alone

**Locator:** `test_dispatch.py:377-399` (`EXPECTED`) and its three protecting comments,
against `dispatch.py:472-486` (`CONSTRUCTION_PROMPT`).

The round's central claim is that the emitted document equals an expected document exactly,
catching added, missing and reordered lines alike. **That claim holds only while `EXPECTED`
is written independently of the module.** The round knows this — it says so in three places
and admits its own first attempt got it wrong:

> asserting equality against `CONSTRUCTION_PROMPT.format(...)` compares the output to the
> renderer's own source, so mutating the constant satisfies both sides at once and all four
> probes stayed green — the identical defect V2 named, in a third form.

and, in the test file:

> The duplication is the whole point and must not be "cleaned up".

**Nothing mechanical enforces it.** I applied the single most plausible future refactor — one
line replacing the hand-written literal with
`D.CONSTRUCTION_PROMPT.replace('{charter}', D.CONSTRUCTION_ROLE_INSTRUCTION)`:

| | with the literal | after the "cleanup" |
|---|---|---|
| baseline suite | 47 passed | **47 passed** |
| instruction paragraph deleted | red | **green** |
| line inserted at head of the prompt | red | **green** |
| two lines swapped | red | **green** |
| derived-facts sentence added | red | **green** |
| charter swapped to the product one | red | red (survives via the absence test) |

So a refactor that looks like tidying, leaves the suite green, and would pass any review that
only runs the suite, silently disarms four of the five probes this round rests on.

**Why this is the finding and not a stylistic note.** This exact defect class has now occurred
three times in this module — the partition allowlist (V1, V2), the first replacement guard
(admitted in `c6d4eb4`'s own message), and it remains reachable in the third. §6.6's precedent
is precise: the class "was only terminated by building a checker (R4), never by more prose."
§9 likewise names fixing something with prose "where a check is possible" as what the
execution side must not do.

**A check is possible, cheap, and already exemplified in this very file.**
`NamedIssueReachability` reads `pathlib.Path(__file__).read_text()` to pin its own source. The
same four lines would assert that `test_dispatch.py` contains no reference to
`CONSTRUCTION_PROMPT` — turning "must not be cleaned up" from advice into a failing test.

**Why not a blocker.** No acceptance matrix exists for this round, so §4's element ① cannot be
named, and no signed contract clause is squarely breached — §9 governs fixing a *finding* with
prose, and here the prose protects a property of a real check rather than standing in for one.
Reported as a finding, ranked first, not inflated.

**Minimum fix.** Add the source-reading assertion. Optionally also drop `CONSTRUCTION_PROMPT`
from any import surface the test can reach — but the assertion is the load-bearing part.

### G2 — low — `rsc.py` still describes the deleted derivation

**Locator:** `ResearchSystem/tooling/rsc.py:325-327`, verbatim:

> `# A CONSTRUCTION round: no control plane declares where it began, so the two`
> `# revisions bounding it are the one irreducible input. Everything else — the`
> `# charter, the commit count, the churn — is derived exactly as in the product`
> `# path, which is why hand-writing these was never justified.`

`rsc.py` is **not in this range's changed-path set**. The commit count and the churn no longer
exist, and "derived exactly as in the product path" is now false in both directions — the
construction path derives nothing but two resolved SHAs. This is the CLI's own source, the
first place someone reads to understand the command.

**Minimum fix.** Restate the comment to match the deletion, or delete it — the module's
construction section now carries the reasoning in full.

### G3 — low — two off-by-one counts

Both recomputed mechanically (`grep -c "^    def test_"` over the class at each revision):
the class held **11** test methods before and holds **7** now; **7** were removed and **3**
added.

- `test_dispatch.py:370`, verbatim: *"This class used to hold **twelve** tests"* — it held
  eleven.
- `c6d4eb4`'s message: *"the partition guard and **eight** tests"* — seven test methods were
  removed.

Neither changes any behaviour, and the headline figure that *is* load-bearing is right: 430
− 4 = **426**, which I re-ran and confirmed. Recorded because §5.1 exists for exactly this
class — at N1 a record's own count was off by one and only an independent count found it.

**Minimum fix.** Correct the docstring; the commit message is immutable and needs no action
beyond not being carried forward.

### G4 — observation, no fix owed — `EMPTY-RANGE` still absorbs a git failure

**Locator:** `dispatch.py:551-560`, `if revs.returncode != 0 or int(...) == 0:`.

A failed `git rev-list --count` is reported as `EMPTY-RANGE`, whose message asserts the range
"contains no commit" — which would be false. The conflation pre-dates this round and the
rewrite only made it explicit; both endpoints are already resolved and ancestry already
checked, so it is not reachable in practice.

Also recorded: `test_a_range_containing_no_commit_is_refused` lost its
`assertIn("NOT DISPATCHABLE", …)` line, which moved to the new
`test_a_refusal_is_not_a_prompt_and_names_no_subject` on the reversed-range path. Same
`if not dispatch.report.ok` branch, and the new test asserts more (no `Subject:`), so this is
not a coverage loss.

---

## 4. Negative results by dimension

- **All five mutation probes `c6d4eb4` claims are genuine** — each reproduced red (table in
  G1's left column), each with the module byte-restored and SHA-256 verified. The new guard
  does catch the two failure modes V1 and V2 named and the previous one could not.
- **Every deterministic suite re-run by me:** `pytest tests -q` → **426 passed**;
  `tests/run_tests.py` → 29/29; `schema/fixtures/validate_fixtures.py` → 36/36;
  `repo-audit.py` → exit 0.
- **The deletion is complete.** No reference to `churn_of`, `merge_count`, `commit_count`,
  `CONSTRUCTION_FIXED_LINES`, `_MERGE_CAVEAT` or `construction_subject_line` survives anywhere
  in `ResearchSystem/tooling/`, `document-harness/` or `ResearchSystem/README.md` — except
  G2's comment and the historical review records, which are correctly immutable.
  `.pytest_cache` hits are gitignored.
- **Named-code surface unchanged.** No issue code was removed with the feature;
  `NamedIssueReachability` still passes at 11.
- **`ResearchSystem/README.md` needed no change** — its dispatch line never mentioned churn or
  a count, and both statements it does make remain true at tip.
- **CLI still behaves.** `rsc v3 dispatch --range d55d5ce..c6d4eb4` emits the full prompt on
  stdout (charter, subject, derive-instruction) and one derivation line on stderr, exit 0.
- **Numbers in the commit message that I re-derived and found true:** net 127 insertions /
  245 deletions excluding the review record (67+60 / 144+101); pytest 426.
- **Worktree and module integrity.** After every probe — including the test-file mutation —
  the worktree is identical to session start; `dispatch.py` restores to
  `106d99d8b618fecf…` and `test_dispatch.py` to `cf40f01630cd9835…`. Mutations applied from
  byte-checked scratchpad copies; never `git checkout --`.

---

## 5. Coverage and recompute list

**Read in full:** the whole diff (`dispatch.py` +67/−144, `test_dispatch.py` +60/−101), both
commit messages, `CONSTRUCTION_PROMPT` and `EXPECTED` line by line against each other, the
rewritten construction-section comment.

**Read as structure:** the committed `v3-review-verify-d55d5ce.md` against what I authored.

**Sampled:** `rsc.py`'s dispatch command, `ResearchSystem/README.md`'s harness line, the
product-side renderer for the comparison in §2.

**Recomputed, none accepted as reported:** pytest **426**; `run_tests.py` **29/29**; fixtures
**36/36**; repo-audit **exit 0**; changed paths **3**; commits **2**; churn **empty**; test
methods **11 → 7**, **7 removed / 3 added**; insertions/deletions **127/245**.

**Honesty ceilings (§10).** The user authorization for opening this round is asserted in a
commit message and is not establishable by me. Mutation testing shows a test has binding
force, not that its force is sufficient — G1 is precisely a case where force is contingent on
something no test holds. A FULL is bounded by what one context can hold.

---

## 6. Open for the user

1. G1 is the only finding worth the fix round: a four-line source-reading assertion converts
   the round's central property from advice into a test.
2. G2 is a comment correction in a file this round did not touch — decide whether it rides
   along or waits for a round that owns `rsc.py`.
3. G3 is a one-word docstring fix. G4 needs nothing.
