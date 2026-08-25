# Round journal — `RIDER-SETTLEMENT` (2026-08-25)

> Closeout dispositions for the bank settlement round. Plan:
> `rider-settlement.plan.md`. Records: `v3-{review-full-8aa9f6e,review-verify-5873840}.md`
> — no cold read, waived by the user (opening ruling 1). Written by the orchestrator at
> closeout; figures quoted from the records and this round's own commits, none new.

## What closed

The bank went from thirty rows to sixteen: ten redeemed with their fixes, four retired by
ruling. The one real defect among the ten — `discover_repo_root` answering about the
environment's repository rather than the probe, the second site of the class round
`SUBMOD-HOOKENV` closed — is fixed and the reviewer could not break it. Everything else
was documentation, one constant, and three tests.

The round also recorded the previous one. `README-BILINGUAL` (`2522ce1`) had landed with
no plan, no journal, no review record and no ledger line; the user ruled it exempt from
review on 2026-08-25 and it is now entered in the CLOSED roll as exempt, with the cost
stated plainly — its self-verification is the candidate's own claim, independently checked
by nobody.

## The rulings this round consumed

Opening (three, carried by the plan): light round form, cold read waived and the
independent FULL kept · the four ruled-not-to-do rows retired by deletion rather than left
standing · the thirteen design rows routed to the already-queued `dispatch-economy` batch,
nine of them collectable there in one pass on the two surfaces that batch already opens.
Fix gate (one, carried by the fix commit): the fix leg approved all-in — both blockers,
three lows, two observations. Closeout (one, carried by the free-channel commit): all five
VERIFY residuals take the free channel rather than the bank, so the bank does not grow
back on the way out.

## What this round got wrong, and why it is worth keeping

**One defect class survived three disguises, and the reason was arithmetic.** Rider
`retire-suite` said the retire template's kept count was bound by nothing. The first fix
made raw outputs a subset of the ordered ids — and chose the subset equal to `PRESENT_IDS`,
so a count taken from the deletion set still agreed. The FULL caught that; the second fix
chose `("chk-c",)` — equal to `already_gone`, so a count taken from *that* still agreed.
The VERIFY caught it again. With three ordered checks there was no escape: every non-zero
raw count collides with one of `check_order` (3), the deletion set (2) or `already_gone`
(1). The fixture needed a fourth check, not a better subset. What finally closed it was
not a cleverer choice but a different method — mutating **every** derivation available at
that site rather than the two or three a record named. Eight wrong implementations, eight
red; the real one green.

**An English pattern missed the Chinese form of its own class — for the second recorded
time.** The fix leg's `HD-41` scan of hard-coded command counts pasted a count of four
sites while the command it pasted, run as written, returns two: the bilingual mirror
writes its count in Chinese and no English regex reaches it. The four was the reviewer's
hand-found number travelling under a scan's authority. The first instance is in round
`PRERUN-RIDERS`' journal (2026-08-22, "扫出英文 pattern 漏中文形的第二重") and the lesson
did not travel, because a journal is where lessons go to be true and unread. It is
recorded here too, which does not solve that — the durable form would be a clause in
`HD-41` requiring a scan over a bilingual surface to state which language forms its pattern
covers, and that is a decision-log change, so it is the user's to make, not this round's.

**The same scan was pasted in a form that could not be run.** An ellipsis stood in the
middle of the regex. `HD-41` clause ④ exists so a reviewer can re-run the scan rather than
trust its conclusion; a command with a hole in it defeats the clause while appearing to
satisfy it. Both scans are pasted runnable in `6a73c79`.

## Costs carried forward

- **The layer is owed an independent read**, this round having waived its cold read while
  editing two members (`EXECUTION.md`, `document-harness/README.md`). It rides the next
  round's opening at per-member digest cost.
- **The `R5` observation the FULL routed to the user** — sixteen rows remain and thirteen
  of them need a round to redeem — is banked as a question, not a conclusion, and the user
  ruled on 2026-08-25 that it is judged after the `dispatch-economy` batch takes the bank
  to seven.
- **`E1`**: the round did not separate orchestrator from executor. All four holdings sat
  in one session; the work side never crossed into the review side, and both the FULL and
  the VERIFY ran as their own `claude -p` sessions.
