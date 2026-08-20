"""Tracked pre-commit checks — called existence-guarded from the untracked git hook.

Each module exposes `check(repo_root) -> int` (0 pass / 1 block) and runs on the STAGED
bytes, so the tests can drive them against disposable repositories (E4/E5: expectations
are hand-written fixtures, never the module's own constants).
"""
