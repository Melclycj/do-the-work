#!/usr/bin/env python3
"""Reference sweep over the instruction layer: every reference form, resolved, enumerated.

Round `XREPO-REFS` ran this sweep from a scratch script and committed only its output
(`document-harness/journal/xrepo-refs-2026-08-20.md` §2); `HD-50` charters round `DE-PREFIX`
to bring the script itself into the repository, so the next sweep is a command and not an
archaeology exercise. Three reference forms are enumerated over the instruction layer's
members and resolved against this repository:

- LINK    — a markdown link target
- PATHTOK — a backticked token containing `/` that matches the guard's own path shape
- NAMETOK — a backticked bare filename (no `/`), resolved against the basenames of every
            tracked file, because a bare name has no directory to resolve from; root-relative
            resolution of names produced five false hits in the first version of this sweep

A LINK or PATHTOK counts as resolving when its target exists from the repository root or from
the member's own directory; a target that only resolves by escaping the repository root does
not resolve, and a run-time marker this repository itself writes counts as resolving whether
or not it exists at rest (E10). The guard's placeholder blindness is shared: a token carrying
`<...>` matches no pattern here either (`v3-cold-read-4410899.md` L-2). This is a sweep, not
a guard — it prints every non-resolving reference and a tally, always exits 0, and decides
nothing. `layer_path_check.py` is the guard, and the member list, path shape and marker
prefix are imported from it rather than written a fourth time (`HD-22` keeps three mirrors of
the membership; a sweep that hand-copied the list would quietly become a fourth). A NAMETOK
hit is not necessarily a defect: a bare name is the compliant form for a caller-held artifact
(XREPO-REFS §1), and this sweep surfaces it so a reader can check the holder sentence exists.
"""
from __future__ import annotations

import pathlib
import re
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent / "hooks"))
from layer_path_check import LAYER, PATHLIKE, RUNTIME_PREFIX, TOKEN  # noqa: E402

LINK = re.compile(r"\]\(([^)\s]+)\)")
NAME = re.compile(r"^[A-Za-z0-9_.\-]+\.(?:md|py|json|yaml|yml|txt|js)$")


def tracked_basenames(repo_root: pathlib.Path) -> set[str]:
    out = subprocess.run(
        ["git", "-C", str(repo_root), "ls-files"],
        check=True,
        stdout=subprocess.PIPE,
    ).stdout.decode("utf-8", errors="replace")
    return {line.rsplit("/", 1)[-1] for line in out.splitlines() if line.strip()}


def resolves(repo_root: pathlib.Path, member: str, target: str) -> bool:
    if target.startswith(RUNTIME_PREFIX):
        return True
    root = repo_root.resolve()
    for base in (repo_root, (repo_root / member).parent):
        candidate = (base / target).resolve()
        if candidate.exists() and candidate.is_relative_to(root):
            return True
    return False


def sweep(repo_root: pathlib.Path) -> int:
    basenames = tracked_basenames(repo_root)
    hits = 0
    for member in LAYER:
        path = repo_root / member
        if not path.exists():
            print(f"MISSING {member} — member absent from the working tree")
            hits += 1
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for lineno, line in enumerate(text.splitlines(), start=1):
            for target in LINK.findall(line):
                if not resolves(repo_root, member, target):
                    print(f"LINK    {member}:{lineno}  {target}")
                    hits += 1
            for token in TOKEN.findall(line):
                if "/" in token and PATHLIKE.match(token):
                    if not resolves(repo_root, member, token):
                        print(f"PATHTOK {member}:{lineno}  {token}")
                        hits += 1
                elif NAME.match(token) and token not in basenames:
                    print(f"NAMETOK {member}:{lineno}  {token}")
                    hits += 1
    print(f"-- {hits} caller-held or unresolvable references over {len(LAYER)} members")
    return 0


if __name__ == "__main__":
    root = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path.cwd()
    sys.exit(sweep(root))
