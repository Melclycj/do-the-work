#!/usr/bin/env python3
"""`dtw init` — the mechanical half of caller onboarding, and nothing beyond it.

Onboarding a repository that has never seen this harness is nine items
(`ONBOARDING.md` beside this package's `document-harness/` docs). Five of them are
judgment: what the caller's policy file says, where its pointer line goes, which guards its
hook runs, which revision the submodule pins, and when its first journal is written. The
mechanical slice — and mechanical work done by hand is work done differently every time —
is this command's whole job: `.harness/` with the default scan-surface declaration inside
it (round STRANGER-GUARDS; the guards read `.harness/scan-surfaces.json` and this write is
how a caller discovers the schema to edit), the ignore entry, the two template instances,
and refusal to overwrite. It says, in its own output, that it did not do the rest.

Two design points, both deliberate:

* **It copies; it does not generate.** The two template instances ship as files
  (`document-harness/templates/`), and `init` writes their bytes unchanged. A generator would
  be a second copy of the header rules, which is the drift surface `HD-5` records.
* **It refuses to overwrite, and appending is not overwriting.** A file that already exists is
  left byte-for-byte alone and named in the report — the caller's own decision log is the last
  thing a re-run may clobber. `.gitignore` is the one file it may extend, because the ignore
  entry is an addition to a file the caller owns rather than a file this command authors; the
  existing bytes are preserved and the entry is never added twice.

Not a guard, and it issues no verdict: the exit code says whether the command ran, never
whether the target is correctly onboarded. What onboarded looks like is `ONBOARDING.md`'s to
state and the caller's to verify.
"""
from __future__ import annotations

import dataclasses
import pathlib

from rsclib.document_harness import caller

#: Source name -> the name it takes in the target. The destination names are a default, not a
#: requirement: a caller that wants them elsewhere moves them and records that in its own
#: decision log (`HD-34`'s adaptation discipline). io-design §6 fixes only which two files
#: ship as empty instances.
TEMPLATES = (
    ("decision-log.md", "HARNESS-DECISIONS.md"),
    ("rider-bank.md", "HARNESS-RIDERS.md"),
)

#: Runtime state, never committed: the freeze marker `dtw dispatch` writes lives here.
RUNTIME_DIR = ".harness"
IGNORE_ENTRY = ".harness/"
IGNORE_FILE = ".gitignore"

#: `<repo>/tooling/rsclib/document_harness/init_target.py` -> the repository root. The
#: depth held across round DE-PREFIX's re-rooting because the file and its target moved
#: up together; only a `parents[n]` reaching across the old instrument/repo boundary broke.
TEMPLATE_DIR = pathlib.Path(__file__).resolve().parents[3] / "document-harness" / "templates"

#: What this command deliberately leaves to the procedure. Named, never numbered: numbering
#: them here would be a second copy of `ONBOARDING.md`'s ordering, free to drift from it.
NOT_DONE = (
    "mount the instrument as a submodule, and pin a revision",
    "write the caller's policy file",
    "add the one-line pointer to that policy file in CLAUDE.md / AGENTS.md",
    "wire a pre-commit hook, and run the per-machine core.hooksPath step",
    "the journal is not pre-created (one file per round) and the ledger has no template",
)

PROCEDURE = "document-harness/ONBOARDING.md, in the instrument repository"


@dataclasses.dataclass(frozen=True)
class InitResult:
    """What one `init` did, in the target's own relative paths."""

    target: pathlib.Path
    created: tuple[str, ...]
    already_present: tuple[str, ...]
    ignore_appended: bool


def _copy_templates(target: pathlib.Path) -> tuple[list[str], list[str]]:
    created: list[str] = []
    already: list[str] = []
    for source_name, dest_name in TEMPLATES:
        source = TEMPLATE_DIR / source_name
        if not source.is_file():
            raise FileNotFoundError(f"template missing from the instrument: {source}")
        dest = target / dest_name
        if dest.exists():
            already.append(dest_name)
            continue
        # Bytes, not text: a copy that round-trips through decode/encode is a copy that can
        # normalise line endings, and "verbatim" is the property this command is tested on.
        dest.write_bytes(source.read_bytes())
        created.append(dest_name)
    return created, already


def _ensure_ignore_entry(target: pathlib.Path) -> tuple[bool, bool]:
    """Return (entry_appended, file_created). Existing bytes are never rewritten."""
    ignore = target / IGNORE_FILE
    if not ignore.exists():
        ignore.write_text(IGNORE_ENTRY + "\n", encoding="utf-8")
        return True, True
    text = ignore.read_text(encoding="utf-8")
    # Both spellings count as present: a caller who wrote `.harness` without the slash has
    # already ignored the tree, and adding the other form would be a second entry saying the
    # same thing.
    if any(line.strip() in (IGNORE_ENTRY, RUNTIME_DIR) for line in text.splitlines()):
        return False, False
    separator = "" if text.endswith("\n") or not text else "\n"
    with ignore.open("a", encoding="utf-8") as handle:
        handle.write(f"{separator}{IGNORE_ENTRY}\n")
    return True, False


def init_target(repo_root: pathlib.Path) -> InitResult:
    """Create `.harness/`, its ignore entry, and the two empty instance files."""
    target = pathlib.Path(repo_root).resolve()
    if not target.is_dir():
        raise NotADirectoryError(f"target repository root does not exist: {target}")

    created: list[str] = []
    already: list[str] = []

    runtime = target / RUNTIME_DIR
    if runtime.is_dir():
        already.append(RUNTIME_DIR + "/")
    else:
        runtime.mkdir(parents=True)
        created.append(RUNTIME_DIR + "/")

    # The default scan-surface declaration, so the guards' surfaces are editable where
    # they are read (`caller.load_scan_surfaces`). Absent it the guards use the same
    # defaults, so this write changes nothing until the caller edits it — what it buys is
    # the schema being discoverable. Never overwritten: a caller's declared surfaces are
    # exactly the adaptation `HD-34` tells them to keep.
    declaration = runtime / "scan-surfaces.json"
    if declaration.is_file():
        already.append(caller.DECLARATION)
    else:
        declaration.write_text(caller.render_declaration(), encoding="utf-8")
        created.append(caller.DECLARATION)

    copied, present = _copy_templates(target)
    created += copied
    already += present

    appended, ignore_created = _ensure_ignore_entry(target)
    if ignore_created:
        created.append(IGNORE_FILE)

    return InitResult(
        target=target,
        created=tuple(created),
        already_present=tuple(already),
        ignore_appended=appended,
    )


def render(result: InitResult) -> str:
    """The report — including what was not done, which is half of what it is for."""
    lines = [f"target   : {result.target}"]
    for path in result.created:
        lines.append(f"created  : {path}")
    for path in result.already_present:
        lines.append(f"kept     : {path} — already existed, left untouched")
    lines.append(
        f"ignore   : {IGNORE_FILE} gained `{IGNORE_ENTRY}`"
        if result.ignore_appended
        else f"ignore   : {IGNORE_FILE} already ignores `{IGNORE_ENTRY}`"
    )
    lines.append("-" * 72)
    lines.append("NOT done by this command — these are the procedure's, and are judgment:")
    lines += [f"  - {item}" for item in NOT_DONE]
    lines.append(f"procedure: {PROCEDURE}")
    return "\n".join(lines)
