# REVIEW — package-bound flow (v1, pre-supersession-1)

> Moved verbatim from [`../REVIEW.md`](../REVIEW.md) on 2026-07-27 (Phase A of
> `.goals/plans/harness-deletion-first-stabilization.plan.md`). These two sections governed
> runs dispatched as a `ReviewPackage` file. Supersession-1 (signed 2026-07-24, W2) made
> every new run commit-bound, so this flow is read only when reading pre-wave-2 history —
> no new run follows it. Cross-references to sections "below" resolve in `../REVIEW.md`.

## What you are given: a floor, never a ceiling

The `ReviewPackage` freezes the raw instruction, the sources, the plan, the **actual candidate
artifacts**, the fulfillment, the manifest, the checks and the coverage — by exact revision,
locator and digest.

**The package is the guaranteed minimum the executor must deliver to you. It is not a bound on
what you may read.** You may read anything at the pinned revisions, and each disposition
records your real judgment of the obligation against the evidence you actually examined —
findings drive verdicts, and a finding may rest on any pinned-revision evidence, in either
direction. What keeps this honest is disclosure, not confinement: say what you read and what
you could not (see *Evidence discipline* below).

An executor summary may be attached. It is supplemental, always. If you find yourself
reviewing the summary rather than the artifacts, stop: the summary was written by the party
under review, so checking it establishes only that the executor described its own output
consistently.

Refuse a package whose **binding** has failed — these are tamper evidence, not effort:

- a member whose digest no longer matches the bytes it names — the frozen subject and the real
  one have diverged, and nothing downstream can say which side moved;
- a package bound to a branch rather than an exact commit, which follows the branch as it
  moves.

A package missing one of the six schema-mandated roles (raw instruction, resolved plan,
candidate artifact, fulfillment, manifest, coverage) is structurally invalid — the schema
refuses it at freeze time, so it can never have been validly frozen and should never reach
you; if one arrives anyway, refuse it as before. Anything short of that — a declared source
input absent, fewer `check_result` members than the run produced — is **not** a refusal
ground under floor semantics: the omission costs you effort, not validity. Record it as a
finding and read what the package omitted at the pinned revisions.

## Evidence discipline — where each kind of material is read

- **Tree material is read only at the pinned revisions** (`git show <revision>:<path>`) — the
  candidate at the candidate commit, the instruction and sources at the revisions the package
  pins, and anything you reach beyond the package at those same revisions. Never the working
  tree: a check observed on the worktree says nothing about the reviewed bytes.
- **The control plane** — the resolved plan, fulfillment, manifest, check results
  and coverage, committed or not — is read from the working tree, and must be verified against
  the frozen package digests **before** you rely on it. That is the package's load-bearing function: it
  pins the one set of materials the executor could otherwise edit mid-review.
- **The package digest reaches you out-of-band and in full, from the dispatching party — never
  from the package file itself.** The custody chain is: out-of-band package digest → member digests →
  bytes. A digest read from the thing it certifies certifies nothing. The digest is
  `canonical_digest(package)` — computed over the package's canonical JSON (NFC-normalized,
  sorted keys, compact separators), **not** over the file's bytes: `sha256sum
  review-package.json` will not reproduce it, and a CRLF checkout must not change package
  identity. Reproduce it from `ResearchSystem/tooling` with:
  `python -c "from rsclib.document_harness import load_json; from rsclib.document_harness.review import package_digest; print(package_digest(load_json('<review-package.json>')))"`
- **Scope, reconciled with contract §5.** The verdict stays scope-relative: *no blocking
  discrepancy found within the frozen subjects and review dimensions* (§5, immutable).
  Disclosed out-of-package reads at the pinned revisions **widen the declared review
  dimensions**; the coverage disclosure in `residual_uncertainty` is what keeps §5 true of
  the result. *This is this file's reading of §5, stated rather than derived — the same
  convention as the collision-precedence rule below.*
