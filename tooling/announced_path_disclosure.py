#!/usr/bin/env python3
"""CI alarm: a commit that changed an announced path names that path in its own message.

`E2` stopped being a gate on 2026-08-27 and became an announcement (user ruling, batch
`FREEZE-TO-ALARM`): the announced paths may be written, and what is owed is disclosure after
the fact — the commit that writes one names, in its own body, the full repo-relative path of
every announced file it changed. This is the machine that notices when that did not happen.

**Why this is a different question from the guard `HD-27` refused three times.** That guard
was to run on *pre-commit* and its predicate was "was there a recorded ruling?", which no
machine can see — the refusals stand on that, under `E6`, and nothing here reopens them. The
predicate below is "did an announced path change in this commit, and does this commit's own
message contain that path?" Both halves are mechanically decidable from committed objects
alone. This also runs *after* the write rather than before it, so it blocks nothing and
authorises nothing; it makes a missing disclosure visible to the independent review that `E2`
sends to the commit body. A pre-commit gate on authorisation and a post-write alarm on
disclosure are not the same mechanism wearing two hats.

**Not in `tooling/hooks/`, deliberately.** The three scripts there are pre-commit hooks that
read a staged tree. This reads committed history over a range and is wired to CI, never to a
hook — a hook could be skipped by the same `--no-verify` that made ruling 2 move the alarm off
pre-commit in the first place.

**What it does not use, and why.** `pack_digests()` in `rsclib/document_harness/__init__.py`
hashes the contract plus the whole pack and has no callers; the plan named it as this alarm's
ready-made mounting point. It is not used here and the reason is a measurement, not a
preference: it answers "what is the pack's aggregate digest in the working tree right now",
while the failure this alarm has to print is *which* announced file *this commit* changed.
An aggregate digest cannot name the file, and it reads the working tree rather than a commit,
so evaluating a range through it would mean checking each commit out. `git diff-tree` answers
the actual question exactly, per commit, from the object store. Wiring the digest here would
be adding machinery to answer a question it does not answer, which is the shape `E6` refuses.

**Ceilings, stated rather than left to be inferred.** The whole commit message is searched
(`%B`, subject line included), not the body alone, because the whole message is what the
independent review reads; under `E8`'s title form (`V3-<ROUND>-v1`) a path can never appear
only in a subject, so the looser surface is vacuous today. That a message names a path is all
this proves — whether what it says about that path is true, and whether the write should have
happened, stay the independent review's to judge (`E2` says so in its own text). Merge commits
are skipped: their changes belong to the commits they merge. Commits at or below the commit
that first added this file are not judged, because they were written under a rule that did not
yet exist; that floor is derived from history, never hand-pinned, and it is printed on every
run so a reader can see what was excluded.
"""
from __future__ import annotations

import argparse
import pathlib
import subprocess
import sys

#: `E2`'s announced list, hand-written and never read back from the directory (E5): the rule
#: names the fifteen files the pack held at the 2026-08-03 re-baseline, so a pack file added
#: later is deliberately absent here until a re-baseline adds it. Listing the directory would
#: enrol new schemas silently and make this guard's expectation a function of what it guards.
ANNOUNCED = (
    "contract/Document-Work-Assurance-Contract-v4.md",
    "schema/document-assurance-v3/assurance-work-state.schema.json",
    "schema/document-assurance-v3/assurance.schema.json",
    "schema/document-assurance-v3/candidate-record.schema.json",
    "schema/document-assurance-v3/common.schema.json",
    "schema/document-assurance-v3/document-assurance-profile.schema.json",
    "schema/document-assurance-v3/document-work-spec.schema.json",
    "schema/document-assurance-v3/document-work-spec.v2.schema.json",
    "schema/document-assurance-v3/harness-issue.schema.json",
    "schema/document-assurance-v3/instruction-coverage-audit.schema.json",
    "schema/document-assurance-v3/local-check-spec.schema.json",
    "schema/document-assurance-v3/paragraph-map.schema.json",
    "schema/document-assurance-v3/resolved-assurance-plan.schema.json",
    "schema/document-assurance-v3/review.schema.json",
    "schema/document-assurance-v3/review.v2.schema.json",
    "schema/document-assurance-v3/user-decision.schema.json",
)

#: This file's own path. The commit that added it is the floor: nothing at or below it is
#: judged, which is how "commits made before this job landed are not re-judged" is enforced
#: without a hand-pinned SHA nobody could write before the commit existed.
SELF_PATH = "tooling/announced_path_disclosure.py"

#: What GitHub sends as `github.event.before` when a push creates a branch — there is no range.
NO_RANGE = "0" * 40


def git(repo_root: pathlib.Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", "-C", str(repo_root), *args],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        errors="replace",
    )
    if completed.returncode:
        raise RuntimeError(
            f"git {' '.join(args)} failed: {completed.stderr.strip() or completed.stdout.strip()}"
        )
    return completed.stdout


def alarm_floor(repo_root: pathlib.Path) -> str | None:
    """The commit that first added this file, or None when history does not reach it.

    `git log --diff-filter=A` can list more than one commit if the file were ever deleted and
    restored; the oldest is the first landing and that is the floor. None means no floor was
    found — a shallow clone, or a checkout whose history predates this file — and the caller
    then judges the whole range, which errs strict rather than silent.
    """
    added = git(repo_root, "log", "--diff-filter=A", "--format=%H", "--", SELF_PATH).split()
    return added[-1] if added else None


def commits_to_judge(
    repo_root: pathlib.Path, before: str | None, after: str, floor: str | None
) -> list[str]:
    """Non-merge commits of the range, oldest first, with the floor and below removed."""
    if before and before != NO_RANGE:
        args = ["rev-list", "--no-merges", f"{before}..{after}"]
    else:
        args = ["rev-list", "--no-merges", "-n", "1", after]
    if floor:
        args.append("^" + floor)
    return list(reversed(git(repo_root, *args).split()))


def announced_paths_changed(repo_root: pathlib.Path, sha: str) -> list[str]:
    changed = set(
        git(repo_root, "diff-tree", "--no-commit-id", "--name-only", "-r", sha).split("\n")
    )
    return [path for path in ANNOUNCED if path in changed]


def undisclosed(repo_root: pathlib.Path, sha: str) -> list[str]:
    """Announced paths this commit changed that its own message does not name in full."""
    message = git(repo_root, "log", "-1", "--format=%B", sha)
    return [path for path in announced_paths_changed(repo_root, sha) if path not in message]


def check(repo_root: pathlib.Path, before: str | None, after: str) -> int:
    floor = alarm_floor(repo_root)
    commits = commits_to_judge(repo_root, before, after, floor)
    print(f"announced-path disclosure: range {before or '(none)'}..{after}")
    print(
        f"  floor {floor or '(none found - judging the whole range)'}; "
        f"{len(commits)} non-merge commit(s) judged"
    )
    failures = [(sha, path) for sha in commits for path in undisclosed(repo_root, sha)]
    if not failures:
        print("  every announced path changed in this range is named by the commit that changed it")
        return 0
    print("FAILED: a commit changed an announced path without naming it in its own message:")
    for sha, path in failures:
        print(f"  {sha} changed {path} - that path is not named in the commit message")
    print(
        "E2: the commit that writes an announced path names, in its own body, the full "
        "repo-relative path of every announced file it changed. Correct forward (HD-59): "
        "the disclosure belongs in a new commit, never in a rewritten one."
    )
    return 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--before", default="", help="range base; empty or all-zeros means no range")
    parser.add_argument("--after", default="HEAD", help="range tip")
    parser.add_argument("--repo-root", default=".", help="repository to evaluate")
    args = parser.parse_args(argv)
    return check(pathlib.Path(args.repo_root), args.before, args.after or "HEAD")


if __name__ == "__main__":
    sys.exit(main())
