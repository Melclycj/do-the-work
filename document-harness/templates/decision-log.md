# DECISION LOG — user rulings for this repository's use of the harness

> **What this is.** The highest source of truth for this repository's user rulings about the
> harness. Instruction-layer text expands *under* these rulings: where a rule and a ruling
> conflict, the rule is what is wrong. One entry carries the ruling itself — one sentence —
> plus its metadata; the reasoning goes to that round's journal and is reached through
> `basis`; open work goes to the rider bank; a decision taken inside a single run belongs to
> that run's own `user-decision-*.json`, which binds by digest and is stronger than this file,
> and is not registered here twice.
>
> **Who reads it.** Every cold read MUST read `§live`, and only `§live`. A plan author reads
> all live entries and inherits them **verbatim** — never by transcription, which is a drift
> surface. **The obligation is the round's opening, not the cold read**: `§live` is owed at
> that opening whether or not the instruction layer's cold read was waived, because that
> waiver is of that layer's members and this log is not one of them, so a waived opening
> still reads it. Anything unplanned met mid-round is found by grepping this file and its
> archive.
>
> **Admission — three questions; any yes admits.** Does it bind the next round and beyond? ·
> Does it overturn or narrow an existing ruling? · Is it a user ruling with no home outside
> the conversation and a commit body? **Granularity: one entry = one thing that can be
> overturned on its own.**
>
> **State machine.** `live` (in force and required reading — ruled but not yet carried, or
> with nowhere else to live) → `implemented` (in force, its detail now carried by instruction
> text, code or a template; not required reading, reachable by grep) → `superseded` (has a
> successor; pointers both ways) / `retired` (no successor: finished, topic gone, or spent).
> The terminal states are irreversible; a revival is a new entry citing the old id.
>
> **Scope.** `standing` (only supersedable) · `mechanism:<path>` (retires with the mechanism)
> · `batch:<id>` (binds one batch's sequencing; retires when that batch is executed) ·
> `one-shot` (retires when consumed; supersedable until then).
>
> **Narrowing is not a fifth state.** A successor entry carries the narrowed text **in full**
> and the original moves to `superseded` whole, pointers both ways, in the same commit.
>
> **Deletion — discipline, no lint.** Dead entries move to the archive file beside this one.
> Deleting one needs both conditions together — it will never be cited again **and** it can be
> reconstructed from the record (commit body, plan, review record) — and the default is not to
> delete. A `superseded` chain is never deletable.
>
> **Invariants.** At most one `live` entry per topic · a supersession, and a `live` →
> `implemented` move, land in the same commit as the carrier that justifies them · only the
> user flips a state; a session may propose one and never perform one.
>
> **Boundary.** Rulings made before this file existed stay where they already are and are not
> migrated. Entry-format integrity is discipline: no machine checks it.
>
> **Entry shape.**
>
> ```
> ### <id> · <one-line title: the ruling, not the topic>
> - <date> · user · scope: <scope> · status: **<state>**（why it is in that state）
> - Ruling: <one sentence>
> - Consequence: <what changes elsewhere, if anything>
> - basis: <where the reasoning lives — journal, review record, commit>
> ```

## §live — required reading (in force, and nothing else speaks for it)

_No entries yet._

## §implemented — in force, detail carried elsewhere (not required reading, grep-reachable)

_No entries yet._
