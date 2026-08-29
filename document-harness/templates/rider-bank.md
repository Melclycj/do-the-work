# RIDERS — banked findings, redeemed on touch

Pure data table. The rules that govern it — what belongs here rather than in a `HarnessIssue`
or in a round of its own, how a finding routes, the row format, and what redemption is — are
`R10` in the instrument's `RULES.md`. They are deliberately **not** restated
here: a second copy is a second thing that has to stay true.

One row per rider, four columns, no narrative — the source records hold that. Redemption means
the fix rides a batch already touching that surface, and the row is deleted in the same commit.

| id | what | redeem when | source |
|---|---|---|---|
