"""Repository-path tokens written into document text, and whether they resolve.

The candidate-side lint SIMP-A4 asked for: *one lint that binds no obligation's truth,
catching only low-level errors and saving review time* (recorded user ruling 2026-08-05,
`document-harness/journal/checker-and-map-2026-08-05.md`). It decides nothing about any
obligation, so it is never a review subject and never a part-owner of a disposition — it
reports a token whose target does not exist, and stops there.

**Why the resident layer rather than a run-local script.** The same journal measured it:
across all committed history the run-local checkers caught nothing, while the accumulating
shared validators — `check_record` refusing an empty locator, `check_spec` refusing an
over-long field — are what actually stopped defects. A lint written fresh each round and
discarded with it would repeat the shape SIMP-A1 deleted.

**The rule.** A token resolves DIRECTly when git tracks it from the repo root, from the
containing file's own directory, or under `ResearchSystem/` — the caller trees this lint
scans keep that directory, so the third branch stays meaningful here (how this lint and the
instruction-layer guard divide the work is stated once, in the *Local enforcement* row of
`document-harness/README.md`, not here). On work products a token resolving nowhere *may be
illustrative*, and that exemption is this lint's whole subject. Measured on the four real product candidates (p4-doc, p5a-firewall,
p5a-shells, p5b-firewall), that exemption is where the defects live — 47 added path tokens,
4 resolving nowhere, of which three are shorthand for exactly one tracked file
(`tests/run_p4_tests.py`, `tests/run_p5a_tests.py`, `rsclib/lint.py`) and one is simply
wrong: `Thesis/literature-analysis/sota-comparison.md`, written into the A3 amendment,
carried through an independent FULL that returned seven findings without it, and signed.
So the exemption splits: a unique path suffix is SHORTHAND and passes; nothing anywhere is
UNRESOLVED and is reported.

**Ceilings, because a lint that is trusted past its reach is worse than none.**

* Only backtick-quoted tokens are read. A path inside a Markdown link, a wikilink or plain
  prose is invisible here — those are the thesis `repo-audit.py`'s subject, not this one.
* SHORTHAND is accepted without asking whether the one file it matches is the file the
  author meant. A wrong path that happens to end like a real one passes silently.
* A token that resolves but names the *wrong* file cannot be seen at all. That is the other
  measured candidate-side defect (p5a-firewall: A2 §1 attributed the enumeration source to
  the wrong file), and this module does not address it.
* Resolution is against the git index, not the filesystem: a file that exists but is
  untracked does not resolve, because it will not exist for the reviewer either. The two
  trees git never tracks *by design* are exempted by name (`UNTRACKABLE`) rather than by a
  filesystem fallback — a fallback would let an untracked scratch file resolve for whoever
  wrote it and for nobody else, which is the failure the index rule exists to prevent.
"""
from __future__ import annotations

import pathlib
import posixpath
import re
import subprocess
from collections.abc import Iterable

#: A backtick-quoted token — the only path form this module reads (see the ceiling above).
_TOKEN = re.compile(r"`([^`\s]+)`")
#: Path-shaped: a slash, plus either a known extension or a trailing slash. Mirrors
#: `layer_path_check.PATHLIKE`, kept identical by hand; what keeps them equal is the
#: `OneNotionOfAPath` pin in `tooling/tests/document_harness/test_precommit_checks.py`.
_PATHLIKE = re.compile(r"^[A-Za-z0-9_.\-/]+(?:\.(?:md|py|json|yaml|yml|txt|js)|/)$")

DIRECT = "DIRECT"
SHORTHAND = "SHORTHAND"
OUT_OF_INDEX = "OUT_OF_INDEX"
UNRESOLVED = "UNRESOLVED"

#: Trees git never tracks by design — its own directory, and the harness runtime state that
#: `dtw dispatch` writes. The index cannot answer for these, so the lint says so instead
#: of pretending: `OUT_OF_INDEX`, never `UNRESOLVED`. Found the way it should be found — the
#: guard's first live run blocked its own round on `.git/hooks/` and
#: `.harness/review-pending.json`, two legitimate references in the harness README. The
#: four-candidate sample that justified this lint contained no such path, which is exactly
#: what a sample of four cannot tell you.
UNTRACKABLE = (".git/", ".harness/")


def _is_citation_shaped(token: str) -> bool:
    """Is this token citing a location, or naming a thing in prose?

    A token without a slash is never path-shaped here: bare `README.md` or `lint.py` is far
    more often a name being discussed than a location being cited, and flagging those would
    bury the one real finding under them.

    The same argument reaches one segment further for directories, which the first form
    missed: `` `vendor/` ``, `` `raw/` ``, `` `docs/` ``, `` `.venv/` ``, `` `../` `` are
    prose that happens to carry a trailing slash, and one slash was never evidence of a
    citation — 78 distinct such tokens sit in the tracked corpus. So a directory token needs
    an interior slash: `tooling/hooks/` cites, `hooks/` does not.
    """
    if not _PATHLIKE.match(token):
        return False
    if token.endswith("/"):
        return token.count("/") >= 2
    return "/" in token


def path_like_tokens(text: str) -> tuple[str, ...]:
    """Every backtick token in `text` shaped like a repository citation, in order, with repeats."""
    return tuple(token for token in _TOKEN.findall(text) if _is_citation_shaped(token))


class TrackedPaths:
    """Every path git tracks, as files plus the directories implied by them.

    Git tracks files, not directories, so a directory token can only be answered by asking
    whether any tracked file lives under it. Both sets are built once per process: the
    caller scans many files against one index.
    """

    def __init__(self, entries: Iterable[str]) -> None:
        self.files = frozenset(entry for entry in entries if entry)
        directories: set[str] = set()
        for entry in self.files:
            parts = entry.split("/")
            for depth in range(1, len(parts)):
                directories.add("/".join(parts[:depth]) + "/")
        self.directories = frozenset(directories)

    @classmethod
    def from_index(cls, repo_root: pathlib.Path | str) -> "TrackedPaths":
        """The index, not `HEAD`: a file added by the very commit being linted resolves."""
        out = subprocess.run(
            ["git", "-C", str(repo_root), "-c", "core.quotepath=off", "ls-files"],
            check=False,
            stdout=subprocess.PIPE,
        )
        return cls(out.stdout.decode("utf-8", errors="replace").splitlines())

    def holds(self, path: str) -> bool:
        if path.endswith("/"):
            return path in self.directories
        return path in self.files

    def suffix_matches(self, token: str) -> list[str]:
        """Tracked paths that end with `token` at a segment boundary.

        Segment boundary, never a bare `endswith`: `.../my-lint.py` must not answer for
        `lint.py`, or the shorthand branch would swallow real misses.
        """
        pool = self.directories if token.endswith("/") else self.files
        return sorted(
            candidate
            for candidate in pool
            if candidate == token or candidate.endswith("/" + token)
        )


def classify_path_token(token: str, containing_dir: str, tracked: TrackedPaths) -> str:
    """One token's verdict — the whole decision, in one place.

    `DIRECT` / `SHORTHAND` / `OUT_OF_INDEX` / `UNRESOLVED`; only the last is ever reported.
    """
    if token.startswith(UNTRACKABLE):
        return OUT_OF_INDEX
    if tracked.holds(token):
        return DIRECT
    if containing_dir:
        joined = posixpath.normpath(posixpath.join(containing_dir, token))
        if token.endswith("/"):
            joined += "/"
        if tracked.holds(joined):
            return DIRECT
    if tracked.holds("ResearchSystem/" + token):
        return DIRECT
    return SHORTHAND if len(tracked.suffix_matches(token)) == 1 else UNRESOLVED


def unresolved_path_tokens(
    tracked: TrackedPaths, containing_path: str, text: str
) -> tuple[str, ...]:
    """The `UNRESOLVED` tokens in `text`, de-duplicated, in first-appearance order.

    De-duplicated because the finding is *this path is wrong*, once, however many times the
    author wrote it; a repeat count would only pad the block a reader has to triage.
    """
    containing_dir = posixpath.dirname(containing_path.replace("\\", "/"))
    seen: list[str] = []
    for token in path_like_tokens(text):
        if token in seen:
            continue
        if classify_path_token(token, containing_dir, tracked) == UNRESOLVED:
            seen.append(token)
    return tuple(seen)


def staged_added_lines(repo_root: pathlib.Path | str, path: str) -> list[str]:
    """The lines this commit ADDS to `path` — the only lines a candidate lint may judge.

    A token already in the file is not this batch's to repair (`v3-review-full-8ec4c60.md`
    B1), and scanning whole files would make every batch inherit every predecessor's
    shorthand.
    """
    out = subprocess.run(
        ["git", "-C", str(repo_root), "diff", "--cached", "-U0", "--", path],
        check=False,
        stdout=subprocess.PIPE,
    )
    return [
        line[1:]
        for line in out.stdout.decode("utf-8", errors="replace").splitlines()
        if line.startswith("+") and not line.startswith("+++")
    ]
