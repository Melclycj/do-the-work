# FULL review — round `STRANGER-GUARDS` at `95ca8d2..c2e955b`

**Verdict: `REVIEWED_NO_BLOCKER`.** 2 low, 4 observations.

**The implementation does what it claims, and every guard I attacked bound.** The two
pre-commit guards genuinely read the caller's declaration and genuinely refuse a malformed
one rather than falling back; the submodule fix separates DIRECT from OUT_OF_INDEX on the
test that matters (the typo under a live mount still blocks); all twelve resolution points
discover or refuse, none guesses. Every figure the commit body reports as its own
measurement that I could re-run, I re-ran and matched: 838 passed at the tip, 792 at the
base (fresh worktree), +46 summing exactly to the six enumerated additions, the HD-41 class
scan's six hits at the six named lines with zero template and zero `.goals` hits, the
GitHub API 404 anonymous, both foreign commits ancestors of `origin/document-work-assurance-v3`
in the caller's checkout, and all three tracked guards exit 0 against the full candidate
diff re-staged in a throwaway worktree — with a planted broken member path making the layer
guard fire, so that 0 was not vacuous. Eight of the ten claimed mutation red-counts I
reproduced independently with my own patches; every one went red on exactly the claimed
tests at exactly the claimed counts. Nothing `E2` freezes was touched; the round's
authorization (the four 2026-08-23 rulings) is committed at plan `cf54a79`, visible in the
repository.

**The two lows are one code edge my own probe found and one process gap in the subject's
base; neither burns the fix leg on its own.**

---

## 1. Subject, round, budget, authorization — re-derived (`R2`)

- **Subject**: `95ca8d2..c2e955b` — exactly one commit, `c2e955b` `V3-STRANGER-GUARDS-v1`,
  27 files, +1456/−212 (diffstat re-run). HEAD = `c2e955b`, worktree clean, branch `main`
  ahead of `origin/main` by 5 — nothing pushed since before the round (`E8`).
- **Round**: `STRANGER-GUARDS`, first of two in publicization batch C, opened by plan
  commit `cf54a79` (`document-harness/plans/stranger-guards.plan.md`, read in full). The
  plan carries the four 2026-08-23 user rulings; ruling 4's dispatched opening cold read
  landed at `2f1f919` (`v3-cold-read-cf54a79.md`); the riders-bank commit `95ca8d2` banked
  its two E2-path lows. `HARNESS-DECISIONS.md` §live read in full — HD-56/44/41/36/35/34/23/9,
  matching the plan's enumeration; none is violated by this candidate.
- **Budget** (`E9`): this is the round's first and only FULL — no prior FULL in the round
  (the cold read is an `E10` read, no verdict, no budget; the riders-bank commit consumes
  nothing per the 2026-08-04 ruling). One user-approved fix and one targeted VERIFY remain.
  From dispatch (marker `dispatched_at` 2026-08-23T12:26Z, three minutes after the
  candidate) to now the branch has taken no commit — the window held.
- **Commit form** (`E8`): kind named ("candidate"), single dense title `V3-STRANGER-GUARDS-v1`,
  one paragraph, no attribution trailers, no amend. Changed paths classified by hand: 2
  hooks, 4 rsclib modules (1 new: `caller.py`), 6 run-v2 templates, 11 test files, 2
  instruction-adjacent docs (`ONBOARDING.md`, root `README.md`), 1 member
  (`document-harness/CONSTRUCTION-CHECKLIST.md`), `HARNESS-RIDERS.md`. Nothing under
  `contract/` or `schema/document-assurance-v3/` — the `E2` surface is untouched.
- **Member edits** (`E10`): `CONSTRUCTION-CHECKLIST.md` only, the header correction
  paragraph — a rule-changing amendment (it changes how citations route), correctly ridden
  on a round rather than the free channel, enumerated in the commit body, owing its
  independent read at the next opening. The membership sentence is untouched — diff
  verified — so no E10-sync falls due. The amended rule resolves correctly against ground
  truth: `6fd0ae3`, `7011916`, `e4ffa2b` are all absent from this repository
  (`git cat-file -t` fatal on each), and `EXECUTION.md:408` does carry the role-annotated
  "caller `6fd0ae3`" the narrowing exists for; `EXECUTION.md` itself deliberately untouched,
  the plan's only-if-ambiguous branch not taken — defensible, since the reading rule now
  names that exact site.
- **Riders** (`R10`): `chk-caller-prefixes`, `submod-index`, `amend-exempt-caller` rows
  deleted in the fix commit — same-commit redemption verified in the diff. `decited-paths`
  correctly kept: its sites are caller-side, deletion rides the caller's gitlink-bump batch
  (mount-inert precedent), and its now-false present-tense clause is marked as the
  then-state. The two rows `95ca8d2` banked (`v4-verifmode`, `v4-plan-digest`) are outside
  this subject's diff (see L-2) but I read them anyway: well-formed, targets and joint
  redeem route named, and both correctly bank under `HD-20` — their bytes fall on the `E2`
  path and wait for the recorded ruling.

## 2. The implementation, piece by piece (`R3` lead)

**(1) chk-caller-prefixes.** `caller.py` read in full. The loader refuses — never
defaults — on unreadable JSON, a non-object, an unknown key, and a non-string-list entry;
an absent key keeps its default; an empty list is a declaration, not an error. `dtw init`
writes the default declaration and never overwrites (must-fire test verified in diff). The
first caller's nine record entries + record dir + runs tree survive byte-for-byte as a
hand-written fixture (`E5`) in `test_caller_surfaces.py` — I compared them entry-by-entry
against the deleted constants in the diff: identical, including the
`HARNESS-DECISIONS.md`-not-exempt asymmetry. My mutations: loader swallows malformed JSON →
3 red; loader ignores unknown key → 1 red; candidate guard scans with DEFAULTS ignoring the
declaration → 3 red; freeze guard judges with DEFAULTS → 3 red. All counts match the
commit's claims exactly, on the claimed tests.

The disclosed boundary extension to `review_freeze_check.py` is justified on its own terms:
the old `RECORD_DIR`/`PRODUCT_RESULT` were the same first-caller class one deadlock deeper
(during `E9`'s window a second caller's returned record was the only admissible commit and
the one being blocked), and the plan's own expectation could not hold while it stood. The
new rsclib import in the freeze hook fails loud (traceback blocks the commit), not silent.

**(2) submod-index.** `from_index` reads `ls-files -s`, pulls each `160000` gitlink's
contents from the mounted submodule's own index, and — the subtle part, correctly done —
verifies the reported toplevel `samefile`s the mount before trusting a listing, because
`git -C` pointed at an empty mount climbs into the superproject and happily lists nothing.
An unlistable mount is carried and classified `OUT_OF_INDEX` (the UNTRACKABLE precedent),
with the disclosed price (a typo under it passes) stated in the docstring. My mutations:
listing disabled → 2 red, the typo-under-mount must-fire being the one that separates
DIRECT from OUT_OF_INDEX; carve-out deleted → 1 red. The `paths.py:237`
`ResearchSystem/`-widening survivor is judged out correctly: it can only turn a block into
a pass on trees that keep that directory and decides nothing about what is scanned.

**(3) The twelve resolution points.** All six cli sites route through `_rooted` (diff
verified, six conversions: governance-scan, status, dispatch, review's two modes, init);
all six templates' `parents[3]` defaults became `discover_repo_root(run_dir)` with
`SPEC_GAP` exit 2 (bind/evidence/repair/retire via argparse, the two argv gates
positionally); the four "e.g. ResearchSystem/assurance/runs" help examples de-prefixed. My
mutations: `_rooted` reverted to bare cwd → 3 red (the subprocess tests caught it even
though my spelling evaded the exact-string source pin — the pin is defense-in-depth, the
behavior tests carry the weight, and they do); `run_retire.py` reverted to `parents[3]` →
2 red, including the all-six refusal sweep. The repair suite's inverted planted-depth test
and the fulfillment suite's two-depth test are honest successors to M11/M13 — the old
records' claims about what those mutations survived are preserved, re-scoped, not erased.

**(4) amend-exempt-caller.** Both halves verified against ground truth (§1). The README
terminus now names `https://github.com/Melclycj/Thesis-Work` with the single-machine paths
kept as recorded history and the private-as-measured framing — which I re-measured: the API
answers 404 anonymously today, and both `e4ffa2b` and `7011916` are ancestors of
`origin/document-work-assurance-v3` in the caller's checkout (`merge-base --is-ancestor`
exit 0 each, re-run 2026-08-23). The ledger's stale "public 仓" note (`CONSTRUCTION-LEDGER.md`
~:87) is correctly reported for the orchestrator to route rather than fixed here. **The URL
write is `R5`-flagged and awaits the user's ratification at the fix gate or earlier — the
orchestrator must actually put it to the user; this record is the reminder.**

**Battery and guards.** Tip: `838 passed` (py3.13.6, Windows, re-run). Base `95ca8d2` in a
fresh worktree: `792 passed`. Delta +46 = 23 caller-surfaces + 9 repo-root-discovery + 5
template-repo-root + 6 SubmoduleInternalPaths + 2 init declaration + 1 repair refusal —
each suite's collected count re-derived, sum exact. All three tracked guards exit 0 against
the re-staged candidate diff; negative control fired.

## 3. Findings

### L-1 (low, code) — the freeze guard and the candidate guard disagree on a declaration entry without a trailing slash

- **Location**: `tooling/hooks/review_freeze_check.py`, `is_record` —
  `re.match("^" + re.escape(prefix) + _RESULT_TAIL, path)` with
  `_RESULT_TAIL = r"[a-z0-9][a-z0-9-]*/evidence/review-(full|verify)\.json$"`.
- **Ground truth violated**: `caller.ScanSurfaces`'s documented contract — "An entry ending
  in `/` is a whole tree; any other entry matches by leading string, the same rule the
  guards have always applied."
- **Measured** (probe, this tree): declaration `{"specification_surface": ["work/runs"]}`
  (valid per the loader — no refusal), marker present, staged
  `work/runs/p9/evidence/review-full.json` → freeze guard **blocks** (the char after the
  prefix must match `[a-z0-9]`, and `/` does not), while the candidate guard on the same
  declaration honors the leading-string rule (instruction under the tree passes, exit 0).
  The failure shape is the returned-record false block during `E9`'s window — the very
  deadlock this round exists to end — reachable by a caller's natural hand-edit that the
  loader accepts without complaint.
- **Not a blocker because**: the defaults, `dtw init`'s written bytes, and the first
  caller's fixture declaration are all slash-terminated; no existing declaration hits it;
  the block is loud and names the path.
- **Minimum fix**: normalize in `is_record` (compose against
  `prefix if prefix.endswith("/") else prefix + "/"`), or normalize directory-kind surfaces
  once in the loader; one must-fire test with a slash-less declared entry.

### L-2 (low, process) — the riders-bank commit sits outside the subject range its own legality cites

- **Location**: dispatch base. `95ca8d2` `V3-STRANGER-GUARDS-RIDERS-BANK-v1` justifies
  itself by the 2026-08-04 ruling — "not a reviewed work product, consumes no E9 leg,
  **lands inside the next review subject range**" — and was then made the *base* of that
  range, which excludes it: `95ca8d2..c2e955b` covers `c2e955b` alone.
- **Ground truth violated**: the quoted ruling's own premise (the exemption from review is
  paid for by riding inside the next subject).
- **Cured in substance here**: I read the two banked rows in full and they conform (§1,
  Riders) — so nothing in this instance goes unreviewed. The gap is the pattern: a base
  chosen at the riders-bank commit leaves such bookkeeping permanently outside every
  subject while still claiming the ruling's exemption.
- **Minimum fix**: none to the tree. For future dispatches, set the range base at the last
  reviewed tip (or land riders-only commits after the candidate); for this round, the
  closeout can cite this record as the rows' review coverage.

### O-1 (observation) — `ONBOARDING.md` is outside the plan's declared change surface, disclosed but not labeled

The plan's change-surface table and its out-of-boundary list both omit
`document-harness/ONBOARDING.md`; the candidate rewrote items 2 and 9. The edit is correct
and wanted — leaving the stale hard-coded-prefix description standing would contradict the
fix (`E6` both-sides) — and the commit body describes it, but unlike the
`review_freeze_check.py` extension it is not labeled as a boundary extension. Nothing to
fix in the tree; recorded so the round's boundary accounting is complete.

### O-2 (observation) — the HD-41 class-scan quantifier's headline over-claims relative to the command run

"Quantifier scope = all tracked bytes under `tooling/` (rsclib, hooks, the two entry
scripts)…" — `tooling/tests/` is tracked bytes under `tooling/` and holds 67 matches of the
scan pattern (deliberate `E5` fixtures preserving first-caller spellings), which the "full
hit list" omits. The restrictive parenthetical does reconcile it, and the scan's purpose
(load-bearing names in scan machinery) rightly excludes fixtures — the accurate scope is
recoverable from adjacent text, so this is wording-level (`R9` shape), riding here rather
than spawning anything. The six in-scope hits I re-derived match the claimed list exactly.

### O-3 (observation) — a seventh run-v2 script keeps a cwd-derived root, by argued design

`assurance/templates/run-v2/compare_blocks.py:60` (`REPO = pathlib.Path.cwd()`) is the
directory's seventh script; the plan and commit scope "six" and the round's "zero bare-cwd
defaults" pin is cli.py-scoped. The file carries an explicit in-place rationale (its cwd is
set by the frozen check spec, not by an operator), predating this round. No action; noted
so the count "twelve points, all closed" is not misread as "no cwd derivation exists
anywhere."

### O-4 (observation) — first-caller adoption is sequenced, not yet done

Until the first caller writes `FIRST_CALLER_DECLARATION` into its own
`.harness/scan-surfaces.json` (riding its gitlink bump, per `HD-34` — cross-repo, out of
this round's boundary), a bumped checkout there gets the DEFAULTS and would scan its
`ResearchSystem/…` records again. The commit discloses this and the byte-exact declaration
lives as the fixture in `test_caller_surfaces.py` for the caller to copy. Sequencing note
for the orchestrator, not a defect here.

## 4. What I read, ran, and could not verify (`R4`)

- **Read in full**: `CONSTRUCTION-CHECKLIST.md` (current tip, all E/R rules), the review
  contract stub, plan `stranger-guards.plan.md`, `HARNESS-DECISIONS.md` §live,
  `caller.py`, `compare_blocks.py`, `test_caller_surfaces.py`,
  `test_repo_root_discovery.py`, `test_run_v2_template_repo_root.py`, and the candidate's
  complete diff for all 27 files (the five adapted run-v2 suites read as diffs, not
  re-read whole).
- **Sampled/probed**: `paths.py` (the classify/holds region whole, rest as diff),
  `CONSTRUCTION-LEDGER.md` (the stale-note region), prior review records (subject-framing
  convention), `EXECUTION.md:405-412`.
- **Ran**: full battery at tip (838) and at base in a fresh worktree (792); 8 independent
  mutations, all red as claimed, all restored, worktrees removed; the three guards against
  the re-staged candidate diff plus one negative control; the L-1 probe; the GitHub 404 and
  caller-checkout ancestry re-measurements.
- **Marked, not verified** (process claims): the executor session's cold dispatch and the
  four `R1` holdings resting with the orchestrator (`HD-55` norm — consistent with the
  record trail, unprovable from the tree); the sha256-checked scratchpad restore mechanics
  and the two mutation mechanisms I did not re-run ("journal/ dropped from defaults = 4
  red", "init's declaration write deleted = 3 red", "all six templates = 7 red" beyond my
  one-template reproduction); the `git ls-remote` credential-probe half of the private-repo
  measurement (I reproduced the 404 half). Mutation proves the tests bind the mechanisms
  they name, not that their force is sufficient (`R4`).

**Verdict: `REVIEWED_NO_BLOCKER`.** The fix leg is not obliged by anything here; if the
user chooses to spend it (L-1 is the only tree change on offer), the VERIFY covers the
repair diff and the permanent boundaries. The user's pending act either way: ratify or
reject the README terminus URL (§2 piece 4).
