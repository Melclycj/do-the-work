# VERIFY review — `88fa1d7..674ac43` (round `CORE-MOUNT`, batch `CORE-MOUNT`)

**Verdict: `REVIEWED_NO_BLOCKER`** — both accepted findings closed and re-measured, no blocking
finding standing at the end of this round; three non-blocking findings, three lows and one
observation, all created by the repair diff and none of them a repair that failed to close.

`B-1` is closed on the merits, not on the record's word. Four of the six digest-protected
fields have a live write path in the shipped template; §13.2 and the template README now both
say four and name all six correctly; the ninth signature entry is corrected forward with every
original word standing. `L-1` is closed and the assertion binds — I mutated it myself, twice,
with controls green on both sides. The repair also corrected one measurement of the FULL's own
(`E12`), and the correction is right: I reproduced it.

> Subject received as a range and nothing else (`R2`). Round, budget, authorization, boundary
> and every figure below were re-derived from this repository; no reported figure was accepted
> as reported, and where a claim is reproduced, the reproduction is what is stated.
>
> Written by the reviewer and **not committed by it** — `R6`. `.harness/review-pending.json` is
> deliberately left in place; the commit that lands this file is what deletes it.
>
> **One artifact, not two.** `REVIEW.md`'s *Where the result lives* names a ReviewResult beside
> this record, written to a control root the caller holds. A construction round has no control
> root, no WorkSpec and no obligation list, so there is nothing for that document to be
> schema-valid against and nothing to bind it to. The record alone is returned, as every prior
> construction VERIFY in this directory returned it. The absence is stated rather than passed over.

## 1. Subject, re-derived

```
$ git rev-list --count 88fa1d72bceaea12b65107fad036da98339ef57e..674ac43135374e57e073a6f881165edcfba935ad
2
$ git diff --numstat 88fa1d7 674ac43
57      0       CONTRACT-V4-SIGNATURE.md
220     0       HARNESS-DECISIONS-archive.md
0       204     HARNESS-DECISIONS.md
5       3       assurance/templates/run-v2/README.md
9       6       contract/Document-Work-Assurance-Contract-v4.md
27      1       tooling/tests/document_harness/test_product_tier_manifest.py
$ git diff --name-status 88fa1d7 674ac43          -> 6 files, all M, nothing added, nothing deleted
$ git rev-parse HEAD ; git branch --show-current
674ac43135374e57e073a6f881165edcfba935ad
dev
$ git status --porcelain
?? .goals/
```

The branch tip is the dispatched tip; nothing landed after the dispatch. The freeze marker's
own bytes agree with the prompt I received:

```
$ cat .harness/review-pending.json
{ "subject": "88fa1d72bceaea12b65107fad036da98339ef57e..674ac43135374e57e073a6f881165edcfba935ad",
  "dispatched_at": "2026-09-03T23:55:12+00:00" }
```

`674ac43` is stamped `2026-09-04T09:49:44+10:00` = `23:49:44Z`, five and a half minutes before
the marker. The window is empty.

Oldest first, kind taken from each commit's own body (`E8`):

| # | sha | title | kind |
|---|-----|-------|------|
| 1 | `7908a8e` | `V3-CONTRACT-SIGNATURE-SUSPEND-AND-RETIRE-FAMILY-v1` | ruling bookkeeping — signature suspended, `HD-63`/`64`/`67`/`68`/`70` retired to archive |
| 2 | `674ac43` | `V3-CORE-MOUNT-FIX-v1` | review fix — the round's `E9`-approved repair, `B-1` + `L-1` |

**Paths classified by hand** (`R2`):

- **Announced (`E2`)** — 1: `contract/Document-Work-Assurance-Contract-v4.md`. No file under
  `schema/document-assurance-v3/` appears in the range at all.
- **Instruction layer, `E10` members** — 1: the contract above. No other member is touched.
- **Governance registers** — 3: `CONTRACT-V4-SIGNATURE.md` · `HARNESS-DECISIONS.md` ·
  `HARNESS-DECISIONS-archive.md`.
- **Product tier, non-member** — 1: `assurance/templates/run-v2/README.md` (product-run table row 8).
- **Tests** — 1: `tooling/tests/document_harness/test_product_tier_manifest.py`.

Nothing else moved: no plan, no journal, no ledger, no rider bank.

## 2. Round, budget and authorization, re-derived

The round is `CORE-MOUNT`, one round in a batch of the same name — `CONSTRUCTION-LEDGER.md`'s
current pointer carries the batch and the user's 2026-09-03 queue ruling;
`document-harness/plans/core-mount.plan.md` carries the goal, eight design decisions, the change
boundary, six acceptance criteria and four `E11`-card rulings, with step 5 written as
"FULL → (fix → VERIFY) → closeout" and still unchecked. `harness.json` declares
`document-harness/CONSTRUCTION-CHECKLIST.md` under `rules`; `document-harness/RULES.md` is the
counterpart it names. I read both, plus `document-harness/REVIEW.md`, plus
`HARNESS-DECISIONS.md` `§live` in full.

**`§live` at this tip — eleven entries, unchanged by this range**, measured rather than counted
by eye:

```
                                    §live   §implemented
at 88fa1d7                            11         38
at 674ac43                            11         33
```

`HD-69` `HD-66` `HD-65` `HD-62` `HD-59` `HD-41` `HD-36` `HD-35` `HD-34` `HD-23` `HD-9`. The five
that left went out of `§implemented`, which is where `HD-63`/`64`/`67`/`68`/`70` sat.

**Budget (`E9`), and what I will and will not conclude.** A valid independent FULL has occurred:
`v3-review-full-3deb304.md`, committed at `88fa1d7`, whose parent is `3deb304` — the dispatched
tip, so the read window took no commit but the record. Both commits in this range therefore land
after a valid FULL. `674ac43`'s body calls itself "round `CORE-MOUNT`'s single `E9`-approved
repair"; `7908a8e`'s body claims exemption. The dispatched VERIFY range covers both, so whatever
the accounting, nothing in this range escaped review. The exemption's stated ground is measurably
false and is `F-1` below; the accounting itself is the orchestrator's and the user's, not mine
(`E9`: never self-classify).

**Authorization ceiling (`R7`, `R4`).** Two user rulings of 2026-09-04 carry this range — fold
`L-1` into the fix, and suspend the contract's signature while retiring the family — and both are
recorded only as the orchestrator's own statement, in the two commit bodies and in the register
banner `7908a8e` wrote. That is this repository's settled position (`CONSTRUCTION-LEDGER.md`'s
2026-08-21 entry declines to build an approval carrier on the ground that an in-repo "the user
approved" is a claim and never evidence), so I state the ceiling and do not treat it as a
finding. The material is **committed and greppable, not chat-only** (`R2`), which is the axis
that would have been a finding.

**Where the suspension sits is not a defect.** I checked whether a standing ruling belonged in
`HARNESS-DECISIONS.md` rather than in the signature register, and it does not: `HD-56`
(archived) records that the user ruled on 2026-08-25 that the signature carrier moves out of the
decision log into `CONTRACT-V4-SIGNATURE.md`, and the contract's own *Signature semantics* block
(`:14-19`) and §14 (`:346-352`) both delegate signed-status there and say the file "never carries
its own approval status". The banner is in the right file, and §13's clause at `:245` does key on
the word *signed*, so the reading that it does not bind a draft holds.

**Boundary.** The plan's *Change boundary* names `CONTRACT-V4-SIGNATURE.md` under ruling 2's
conditional grant and does not name `HARNESS-DECISIONS.md` or its archive; `7908a8e` places
itself outside the round as a ruling-bookkeeping batch under the ledger's 2026-08-03 rule (a
bookkeeping batch opens no round, the user ruling is the gate). Both commits state their position
rather than assuming it, which is what `E9` asks of a boundary that grows.

## 3. The two accepted findings, led with

### 3.1 `B-1` — closed, and I measured the fact rather than the record

The command that could falsify the sentence, re-run by me at this tip:

```
$ grep -rn -A3 "pointer_for(" assurance/templates/run-v2/*.py
run_bind_v2.py:252:  review_ref=assurance_state.pointer_for("review_ref", review_path, repo),
run_bind_v2.py:530:  bind_auth_ref = assurance_state.pointer_for(
run_bind_v2.py-531-      "bind_authorization_ref",
run_bind_v2.py:653:  final_ref = assurance_state.pointer_for(
run_bind_v2.py-654-      "final_decision_ref", ...
run_bind_v2.py:698:  assurance_candidate_ref=assurance_state.pointer_for(...)   # unprotected
run_evidence_v2.py:391,393,395,397                                            # all unprotected
run_repair.py:105:   repair_decision_ref=assurance_state.pointer_for(
run_repair.py-106-      "repair_decision_ref", ...
```

`assurance_state.py:82-96` reads back exactly six members. Four of them have a live write path in
the shipped template; `work_spec_ref` and `start_decision_ref` have none. §13.2 at `:335-343` now
says exactly that, and names both scripts.

**I checked the half a `pointer_for` scan cannot see**, because that is the shape that produced
`B-1` in the first place — a sentence measured by the wrong command. Does any shipped template
write those two fields by some other helper?

```
$ grep -rn "work_spec_ref\|start_decision_ref" assurance/templates/ document-harness/templates/
assurance/templates/run-v2/README.md:76, :84                     -- prose
assurance/templates/run-v2/run_bind_v2.py:585: work_spec_ref=digest_ref_of(state["work_spec_ref"], REPO),
$ grep -rn "pointer(\|pointer_to(\|pointer_for(" assurance/templates/ document-harness/templates/
   -- pointer_for only: run_bind_v2 x4, run_evidence_v2 x4, run_repair x1; no bare pointer(, no pointer_to(
```

`:585` is inside `S.bind_candidate(...)` — it builds the **AssuranceCandidate document** from a
state pointer somebody else wrote, not a state pointer. §13.2's subject is state pointers
(`:298-300`: "A state pointer carries the BYTES digest … when, and only when, its field is one the
executor may not author"). So the new sentence survives the wider command too. `document-harness/templates/`
holds only `decision-log.md` and `rider-bank.md` — no script.

**The end-to-end clause, checked field by field** rather than accepted. The contract now says all
four are "demonstrated over a real run directory … a test drives the template's own entry point
and asserts the pointer in the state it saved". Each of the four has such a test, and the
mechanism is what the sentence describes — both templates are loaded by
`importlib.util.spec_from_file_location` (`test_run_v2_template_bind.py:60`,
`test_run_v2_template_repair.py:65`) and their `main(argv)` is called in-process over a real temp
run directory:

| field | test | what it asserts |
|---|---|---|
| `review_ref` | `test_run_v2_template_bind.py:1043` | saved state's `review_ref` == path + bytes digest of the fixture's own bytes |
| `bind_authorization_ref` | `:1410` | saved state's pointer == `user-decision-repair.json` + digest, and `repair_decision_ref` still refused at round 0 |
| `final_decision_ref` | `:1825`, `:1829` | saved state's path, and `digest_sha256` present |
| `repair_decision_ref` | `test_run_v2_template_repair.py:326` | saved state's pointer == path + `self.decision_digest()` |

**The `E12` correction the fix made to the FULL, reproduced.** The FULL read
`test_run_v2_template_repair.py:208`'s `subprocess.run` as invoking `run_repair.py` as a process.
Measured at `:208-211`, that call is `git -C <root> init -q` on the throwaway root. The fix is
right and `B-1` is untouched by it — the four write paths and the falsity of the two-of-six
sentence never depended on it. This is `E12` used as written: reproduced to write the fix
correctly, not to adjudicate the reviewer.

**The twin, and the class.** `assurance/templates/run-v2/README.md:80-84` now reads four and
names all six fields. I ran the phrasing scan myself over the **whole tracked tree with no
exclusions** — the fix's own scan excluded `migration/`, journals, plans, the archives and the
rider bank, and I wanted the unexcluded answer:

```
pattern: live write path|shipped template|authored outside this template|written by these scripts|end-to-end demonstration
LIVE sites (non-record, non-register):
  assurance/templates/run-v2/README.md:80, :83     -- four, correct
  contract/Document-Work-Assurance-Contract-v4.md:336, :341  -- four, correct
REGISTER quoting itself: CONTRACT-V4-SIGNATURE.md:225,230 (original, standing) and :256,257,259 (the withdrawal)
HISTORICAL, correctly untouched (HD-59): document-harness/journal/core-mount-2026-09-03.md:98
  ("one live write path of five -> two of six" -- the journal's record of what 4020efa did),
  document-harness/plans/core-mount.plan.md:153, and 22 lines across migration/ records
```

Two live sites, both fixed. Nothing of the class is left standing.

I also re-ran the cardinality scan (`one|two|…|six` on a line carrying protected-set language)
over the whole tree and checked the two sites the fix's body dismisses. Both dismissals hold:
`README.md:76` says "`work_spec_ref`, the four decision refs, `review_ref`" — six, correct;
`test_run_v2_template_bind.py:944` describes `clean_round_zero_state`, whose six pointers are
`work_spec_ref` (digested) plus `resolved_plan_ref`, `instruction_audit_ref`, `fulfillment_ref`,
`manifest_ref` and `coverage_ref` — none of the other five is in `DIGEST_PROTECTED_FIELDS`, so
"exactly what `pointer_for` writes for them" is true. `summary.py:202` reads "the six protected
fields", correct.

**The signature entry.** The forward correction at `CONTRACT-V4-SIGNATURE.md:251-277` withdraws
the class claim, states that `run_repair.py` was in the shipped template writing
`repair_decision_ref` on the day v4 was signed, states that the entry's own replacement count of
two was wrong at four, and names what the entry still records correctly. Every original word of
the ninth entry stands — the diff is pure addition, 26 lines, no deletion (`HD-59`).

The FULL's minimum-fix item 3 left a question for the user: a new family ruling admitting
"false at signing", or a correction confined to what `HD-63` reaches. The round took neither and
a third route — suspend the signature, retire the family, write the whole correction under
`E10`'s free channel — and records the `HD-63` question as **moot** rather than answered. With
§13 not binding on a draft, that reading is sound: both routes existed to obtain authorization to
edit signed text, and there is no signed text to authorize an edit to.

**The free-channel test, applied to the contract edit.** Adds no clause; changes no requirement
(the digest policy's predicate at `:298-300` is untouched, and the sentence states which scripts
happen to write which fields rather than deciding who may); no round relied on it — an outcome
would not have changed had it read otherwise. The owed independent re-read is recorded in the
commit body and in the signature entry as riding the next read of this layer.

### 3.2 `L-1` — closed, and the assertion binds (`E4`, `R8`)

`tooling/tests/document_harness/test_product_tier_manifest.py:204-224` now runs
`[sys.executable, "tooling/dtw.py", "--help"]` with `cwd=clone` and asserts exit 0, last inside
the (d) case's `try`, before the `finally: shutil.rmtree`. No second fixture (`E6`): it rides the
clone the case already builds and already tears down.

I ran the mutations myself. `git clone` to a scratch path was available to me, but editing the
tracked manifest was not something I would do as reviewer, so I replaced the guard's reader
(`manifest_lines`) — the same input the assertions would have seen had the file been edited, and
no tracked file was written. Probe at `.harness/verify-mutation-probe.py` (gitignored, deleted
after the run); output verbatim:

```
baseline manifest lines : 15

control before (unmutated)                                 GREEN  (0 failing of 1)
M-A: drop tooling/rsclib/document_harness/ from the manifest RED    (1 failing of 1)
    ModuleNotFoundError: No module named 'rsclib'
M-B: drop tooling/dtw.py from the manifest                 RED    (1 failing of 1)
    can't open file '...\core-mount-ck_d8dlj\tooling\dtw.py': [Errno 2] No such file or directory
control after (readers restored)                           GREEN  (0 failing of 1)

restored manifest_lines equals baseline: True
```

Both mutations fire **the new assertion and no other** — captured in full on a second pass so the
line is named rather than inferred:

```
File ".../tooling/tests/document_harness/test_product_tier_manifest.py", line 219, in
    test_the_narrowed_clone_holds_exactly_what_the_manifest_matches
AssertionError: 1 != 0 : the CLI does not run inside the narrowed checkout, so the product-run
tier is not import-complete:
Traceback (most recent call last):
  File "C:\...\Temp\core-mount-w5szlljw\tooling\dtw.py", line 16, in <module>
    from rsclib.document_harness.cli import main
ModuleNotFoundError: No module named 'rsclib'
```

That the mutation cannot instead turn the two-consumer comparison red is structural and worth
stating: both `on_disk` and `matched` are derived from the same `lines`, so dropping a line
shrinks them together and they still agree. The new assertion is the only one that can see it,
which is exactly what `L-1` said was missing.

The manifest is byte-identical to what the FULL read, and to the sha256 the fix's body cites for
its own scratch copy:

```
$ python -c "sha256 of document-harness/product-tier.txt"
dfa84d7bd8983a4076bc51a0285daeb284825af3e5cf1818e17da073b9e690a6
```

### 3.3 Battery and guards, re-run at this tip

```
$ python -m pytest tooling/tests -q
961 passed in 189.61s   (exit 0)
$ python tooling/ledger_cap_check.py                      -> 0
$ python tooling/announced_path_disclosure.py --before 88fa1d7… --after 674ac43…
  range 88fa1d7…..674ac43…; floor 1d4d9aa1…; 2 non-merge commit(s) judged
  every announced path changed in this range is named by the commit that changed it   (exit 0)
```

961 is the same 961 the FULL measured and the same the fix's body claims: one existing case
gained one assertion, so the case count did not move. That is the right shape for this repair —
a new case would have been the `E6` answer, and this is not one.

`layer_path_check` is `O-1v` below and I did not accept its bare exit code as evidence.

### 3.4 The archived block, checked for verbatimness

`7908a8e` moves five entries out of `HARNESS-DECISIONS.md` (204 lines removed) into
`HARNESS-DECISIONS-archive.md` (220 added). Diffing the removed lines against the added ones:
the only differences are the 16-line dated section header and four status lines, each flipping
`implemented` → `retired` while carrying the prior state's reason forward verbatim inside the
same parenthesis (`HD-59`). `HD-70` was already `retired` and its line is untouched. Every other
byte of all five entries is identical. The body's claim of verbatimness is accurate on the only
reading that could be true of a status flip.

## 4. Findings

None of these is a blocker. `R3`: a non-blocking finding is never inflated, and a VERIFY that
inflated one would stop the run over something no repair failed to close.

### `F-1` (finding, non-blocking) — `7908a8e` claims an `E9` exemption on a ground the FULL's own blocker refutes

**Where.** `7908a8e` commit body, first sentence: *"not a round and no E9 spend — nothing here is
a reviewed work product; the decision log, its archive and the signature record are
construction-side registers, none an E10 member or an announced path."*

**What is true.** The second half is right: none of the three is an `E10` member (`RULES.md:86-94`
lists seven, none of them) or an announced path (`E2` names the contract and the schema pack).
The first half is not. The exemption it invokes is the ledger's 2026-08-04 ruling, whose criterion
is written in the ledger as *"改的是不是被评审的 work product"* — is what changed a reviewed work
product. `CONTRACT-V4-SIGNATURE.md` is one, unambiguously and for this very round: `4020efa` wrote
its ninth entry, the FULL reviewed it, `B-1`'s *Where* names `CONTRACT-V4-SIGNATURE.md:186-217`,
and `B-1`'s minimum fix item 3 is a change to that file — which `674ac43` then made.

**What did not go wrong.** No budget escaped. The dispatched range covers both commits, `674ac43`
names itself the single approved repair, and this VERIFY reviews the pair. Read together the two
bodies describe one repair in two commits, which is `E8`'s ordinary shape.

**The decision that goes wrong.** The ground, not the outcome, is what persists. A later round
citing this sentence would conclude that a post-FULL write to `CONTRACT-V4-SIGNATURE.md` consumes
no fix leg and owes no VERIFY — and `E9` says in as many words that *every recorded escape from
the cap was a renamed round*. Had `7908a8e` been the only post-FULL commit, its stated ground
would have licensed exactly that.

**Minimum fix.** One sentence, written forward (`HD-59` — the body is a committed conclusion):
state that the round's one approved repair is `7908a8e` + `674ac43` under one 2026-09-04 ruling
and that the VERIFY covers both, rather than that one of the two is exempt because nothing in it
was reviewed.

### `F-2` (finding, non-blocking) — the suspension is invisible to every repository that mounts this harness

**Where.** `CONTRACT-V4-SIGNATURE.md:3-30` (the banner) against `document-harness/product-tier.txt`.

**Measured.** The manifest is fifteen lines and `CONTRACT-V4-SIGNATURE.md` is not one of them; the
contract **is** (line 1). The contract carries `signature_owner: CONTRACT-V4-SIGNATURE.md` at `:9`
and, at `:14-19`, *"This contract becomes binding only when the user signs it. The signature is
recorded … in this instrument's own signature record."* So the travelling file tells its reader
that its binding status lives in a file that does not travel.

**What changed on 2026-09-04.** Before it, a caller that could not reach the register defaulted to
"signed" and was right. After it, the same caller defaults to "signed" and is wrong, and the same
sentence that keys the in-place prohibition on signature also keys binding-ness on it. The
banner's *What it does NOT lift* list enumerates `E2` and `E10` membership and is silent on that
half, so a reader who does reach the banner still is not told what suspension does to the
contract's own binding clause.

**The decision that goes wrong.** A caller reading v4 to learn whether it is the operative binding
text gets the pre-suspension answer, and cannot learn that the text it pinned may now change in
place under a free channel with no versioned successor and no re-signature — which is the whole
of what §13 exists to prevent.

**Not a blocker, and why.** It violates no rule in `RULES.md` or the checklist: the contract's
operative force inside this harness comes from `E10` membership, which the banner explicitly
preserves, and the register is the delegated authority on status by the contract's own words.
Whether the suspension should be reachable by a caller — a manifest row, a line in the contract,
or nothing — is a distribution question of the kind `HD-66` owns, and it is the user's, not mine
(`R5`). Recorded, not concluded.

### `F-3` (finding, non-blocking) — retiring the family falsified a banked rider's stated reason, and the rider will now misroute

**Where.** `HARNESS-RIDERS.md` row `enum-single-home`, last sentence: *"Fix needs a family ruling
(a signed statement false at signing is a new class) or a v5 successor, so no bytes."* Its
redeem-when is *"the next round touching contract §5, or a v5 successor"*.

**What `7908a8e` did to it.** The family is retired and the signature is suspended, so the fix that
row describes as impossible-without-a-ruling is now a plain `E2` write on a draft — the same route
`674ac43` took for §13.2, at no round's cost.

**The decision that goes wrong.** The next round touching contract §5 reads the row, concludes it
needs a family ruling or a v5 successor, finds neither obtainable, and banks it a second time —
paying the round cost the suspension was ruled to remove. This changes an actor's action, so it is
not `R9` wording-level.

**Minimum fix.** The row's reason clause, updated to say the fix is now a free-channel write while
the signature stands suspended; redeem-when unchanged. `R10`'s touch condition (contract §5) was
not met by this range, so this is not a redemption the repair skipped.

### `L-1v` (low) — the archived section cites, as proof the retired entries are still referenced, a rider row deleted one commit earlier

`HARNESS-DECISIONS-archive.md:460` records the eighth `HD-6` prune question and answers it:
*"五条仍被外部援引（`HD-63` 尤甚，rider `protected-set-says-five` 等仍写「HD-63 的类」；`HD-65` 引
`HD-64`）"*. Measured:

```
$ git show 88fa1d7:HARNESS-RIDERS.md | grep -c "protected-set-says-five"   -> 0
$ git show 674ac43:HARNESS-RIDERS.md | grep -c "protected-set-says-five"   -> 0
```

That row was deleted at `4020efa`, the commit that paid it — as the FULL measured and recorded.
The second example holds (`HARNESS-DECISIONS.md:113,124,132`: `HD-65` cites `HD-64`), and I
measured `HD-63` cited in nine other places outside the archive, so the **conclusion** — the
deletion conjunction fails, do not prune — stands on grounds that are true. `R9` wording-level:
no actor's action changes and the accurate fact is recoverable from the same sentence and from
`4020efa`'s body.

### `L-2v` (low) — the eighth `HD-6` payment is not recorded where the previous seven are

`HARNESS-DECISIONS-archive.md`'s header block holds the first through seventh payments, and its
seventh ends *"下次触发点仍是下一次有条目移入本档时"* — which is this move-in. The header block
gained nothing in this range (`git diff --numstat`: 220 added, 0 removed, all inside the new
dated section at `:447`). A reader consulting the header, which is where the register's own
convention puts these, sees seven payments and a pending trigger. `R9` wording-level: the record
exists in the same file, one section away.

### `L-3v` (low) — the new assertion's comment claims a half it cannot see

`test_product_tier_manifest.py:204-210` and the module docstring at `:21-24` say the assertion
catches "a module added under `tooling/` outside every manifest line, **or a new third-party
import**". The first half binds — `M-A` proves it. The second does not, in general: the clone runs
under `sys.executable`, so it shares the developer's site-packages, and a newly added third-party
import that is installed locally exits 0 inside the narrowed clone while breaking a caller that
lacks it. No manifest line could have carried a third-party package anyway, so what the assertion
actually establishes is that the tier carries everything the CLI needs **from this repository** —
which is the property `L-1` asked for. Comment, not assertion.

### `O-1v` (observation) — `layer_path_check`'s standalone exit code certifies nothing after the fact, and three records now cite it as if it did

`tooling/hooks/layer_path_check.py` scans `git diff --cached` (`added_lines_by_path`, `:105-106`).
On a clean worktree it finds no staged diff, scans nothing, and returns 0. Both commit bodies in
this range, and the FULL's §3.3, record `layer_path_check … exit 0` as evidence about the lines
the commits added; my own re-run returns 0 for the same vacuous reason.

I established the property the guard is for by feeding its own predicate the commits' added
lines instead (`.harness/verify-layer-probe.py`, gitignored, deleted after the run):

```
paths this guard scans: the seven E10 members + document-harness/CONSTRUCTION-CHECKLIST.md
7908a8e: added lines in CONTRACT-V4-SIGNATURE.md, HARNESS-DECISIONS-archive.md
         -> none of them scanned by this guard        VERDICT: would pass
674ac43: added lines in CONTRACT-V4-SIGNATURE.md, assurance/templates/run-v2/README.md,
         contract/Document-Work-Assurance-Contract-v4.md, tooling/tests/.../test_product_tier_manifest.py
         -> scanned: contract/…-v4.md, 9 added lines, 0 unresolved tokens
                                                       VERDICT: would pass
```

So the property holds; what did not hold is the way it was evidenced. Whether the round records
should stop citing a post-hoc standalone exit code, or the script should grow a range mode, is a
question about whether a component should change — `R5`'s and the user's. Recorded, not concluded.

## 5. Boundary check — process and record conformance, run second

| obligation | held? | how established |
|---|---|---|
| `E9` FULL occurred, window clean | yes | `v3-review-full-3deb304.md` at `88fa1d7`, parent `3deb304` = the dispatched tip |
| `E9` VERIFY window — nothing lands after dispatch | yes | `HEAD` == dispatched tip; tip commit 5m28s before the marker |
| `E9` fix-boundary growth stated, never silent | yes, with a false ground | `674ac43` states the `L-1` fold and the third route; `7908a8e` states its position — `F-1` is the ground, not the silence |
| `E8` staged paths, new commits, no amend, no push, `V3-…-v1`, dense body, kind named | yes | 2 commits, linear (`674ac43`←`7908a8e`←`88fa1d7`), 0 merges, 0 trailers, both kinds named; `origin/dev` at `3060a23`, far behind — nothing pushed |
| `E2` disclosure of announced paths | yes, mechanically | `announced_path_disclosure` exit 0 over the range; `674ac43`'s body names the one announced path and its one site with before/after line ranges, both of which I re-derived (`:335-340` → `:335-343`) |
| `E3` measure-last, paste output | **no, at two sites** | the falsifying command was run and pasted, and every figure I re-ran matched (961; the manifest sha256; the four test line numbers; the three scans). The two misses are `L-1v` (a citation the command would have refuted) and `O-1v` (a guard exit cited for more than it decides) |
| `E4` / `R8` mutation-tested guard | yes | §3.2 — two mutations red on the new assertion by name, controls green both sides |
| `E5` guard expectation independent of the guarded thing | yes | the new assertion's expectation is the literal `0`, and the thing guarded is the tier's import-completeness — no shared derivation |
| `E6` no new machinery | yes | one assertion on a fixture that already existed; no second clone, no new file |
| `E7` defect class not instance | yes | the twin fixed in the same commit; my own unexcluded whole-tree scan finds no third live site |
| `E10` free channel for the contract edit | yes | no clause added, no requirement changed, no reliance; re-read recorded as owed in two committed carriers |
| `E10` `§live` read at opening | yes | eleven entries in full, unchanged by this range |
| `E12` one SHA / range handoff, reproduce not adjudicate | yes | marker carries the range and nothing else; the one measurement differing from the FULL's is reproduced and reported, and `B-1` is left standing on it |
| `R10` rider routing | **one row now misroutes** | no rider row is touched by this range and none needed to be; `F-3` is a row whose reason the range falsified |
| `HD-59` correct forward, never rewrite | yes | the ninth entry is pure addition; the four archived status lines carry the prior reason verbatim |
| ledger admission and cap | yes | `ledger_cap_check` exit 0; the ledger is not touched by this range |
| `E1` / `R1` independence | declared, not verifiable | see ceilings |

## 6. Coverage, and the honesty ceilings

**Read in full:** `document-harness/CONSTRUCTION-CHECKLIST.md`, `document-harness/RULES.md`,
`document-harness/REVIEW.md`, `CONSTRUCTION-LEDGER.md`, `document-harness/plans/core-mount.plan.md`,
`migration/document-work-assurance-v3/v3-review-full-3deb304.md`, `HARNESS-DECISIONS.md` `§live`,
`document-harness/product-tier.txt`, `tooling/tests/document_harness/test_product_tier_manifest.py`,
both commit bodies, the complete diff of the range for all six files, `HARNESS-RIDERS.md`,
`.harness/scan-surfaces.json`, `harness.json`.

**Sampled:** `contract/Document-Work-Assurance-Contract-v4.md` (`:1-30`, `:240-250`, `:296-345`,
`:346-352`; not the whole contract), `CONTRACT-V4-SIGNATURE.md` (the banner, `:220-277`, and every
line the scans returned; not all 320), `HARNESS-DECISIONS-archive.md` (its header block, the new
dated section, and the four flipped status lines line-by-line against their removed counterparts;
not all five entries' bodies), `assurance/templates/run-v2/run_bind_v2.py` (`:245-260`, `:520-540`,
`:645-660`, `:560-620`, `:690-712`), `assurance/templates/run-v2/README.md` (`:70-90`),
`tooling/rsclib/document_harness/assurance_state.py` (`:75-145`),
`test_run_v2_template_bind.py` (`:55-70`, `:938-1000`, and the four cited assertions),
`test_run_v2_template_repair.py` (`:60-70`, `:200-215`, `:318-336`),
`tooling/hooks/layer_path_check.py` (in full for the predicate, `:1-150`),
`document-harness/journal/core-mount-2026-09-03.md` (its tail).

**Probed only:** `run_evidence_v2.py` and `run_retire.py` (by grep for pointer helpers, not read),
`tooling/rsclib/document_harness/summary.py` (`:195-210`), `HARNESS-DECISIONS.md` `§implemented`
(entry counts and `HD-1`/`HD-2`/`HD-6` in full; the other thirty by heading), `HD-56` in the
archive, `CONSTRUCTION-INDEX.md` (by scan only — this range does not touch it).

**Ceilings, stated rather than papered over (`R4`):**

- **Process claims have no evidence lock.** That the executor was a cold `claude -p` session on
  `opus` without web tools, that this range's rulings were taken as the bodies describe, that the
  fix's own mutation used sha256-checked scratch copies and never `git checkout --` — all declared.
  I mark them; I do not verify them. What I can say is that the manifest's bytes at this tip hash
  to the value the body cites, and that the worktree is clean.
- **The user's rulings are the orchestrator's own record of them.** §2 states why that is this
  repository's settled position and not a finding.
- **My mutation replaced the guard's reader rather than the bytes on disk.** Editing a tracked file
  is not the reviewer's act (`REVIEW.md`, *What you never do*), so I fed `manifest_lines` the input
  an edited manifest would have produced. The assertions saw identical input either way, and I say
  so rather than claim the byte-level form `E4` prescribes for the executor.
- **`dtw --help` proves import-completeness from this repository, not functional completeness and
  not environment completeness.** `L-3v` names the second half. No `dtw` subcommand other than
  `--help` was run against a narrowed tree, by the round or by me.
- **The suspension's downstream reach is larger than I measured.** I scanned for present-tense
  "signed contract" claims outside records and found the contract's own header, `RULES.md:93`/`:111`
  (historical, about the merged predecessors) and two code comments (`checks.py:28`, `cli.py:61` —
  the latter says "signed Contract v3", stale since round `CONTRACT-V4` and untouched by this
  range, so not mine to widen into). What a suspended signature does to every citation of contract
  §N across the instruction layer is a question this record does not settle.
- **One review round is bounded by one context.** I did not read the whole contract, the whole
  signature register, the whole archive, or the whole rider bank; a reader who treats
  `REVIEWED_NO_BLOCKER` on the parts I did read as coverage of the parts I did not will over-trust
  this verdict.

## 7. What the verdict means

`REVIEWED_NO_BLOCKER`: no blocking discrepancy was found within this subject and these review
dimensions. Both accepted findings are closed and I established both on the merits — the four
write paths by the command that could falsify them plus a wider command the original scan could
not see, and the new assertion by two mutations that name the failing line. `UNRESOLVED_BLOCKER`
was the value to reach for had a blocking finding survived the repair or been created by it, and
none did: `F-1` is a false ground under a correct outcome, `F-2` is a disclosed consequence of a
user ruling whose design question is the user's, and `F-3` is a bank row the range made stale.

It is not a proof of correctness and it does not certify that contract §13.2 is now right about
everything — only that the sentence `B-1` named is measured true at this tip, and that the class
scan behind it was run over a wider scope than the one the fix declared.

`E9`'s single repair is spent. Three findings and three lows route at closeout under `R10`: `F-1`
and `L-2v` are forward corrections to committed conclusions (`HD-59`), `F-3` is a rider-row
update whose touch condition this range did not meet, `L-1v` and `L-3v` are `R9` wording-level,
and `F-2` and `O-1v` carry questions that are the user's (`R5`).
