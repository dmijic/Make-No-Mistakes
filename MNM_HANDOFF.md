# MNM Development Handoff

## Current State
- Branch: `v2/core-protocol`
- HEAD: will be the commit created by this handoff (see commit SHA reported after push)
- Current phase: v2 Phase 2 — Guidance + Templates (complete, pending independent review)
- Status: Phase 1 Core remains ACCEPTED and unmodified beyond the two prior mechanical path cross-references described below. Phase 2 migrates supporting docs; not yet reviewed. Phase 3 not started.

## What Changed
Migrated the five v1.1 `docs/` files into two new directories, rewritten to align with the accepted v2 Core and cross-reference it instead of restating it:

- `docs/git-baseline.md` → `guidance/git-baseline.md` — same safety checks; commits reframed as durable/reviewable states (not mandatory phase boundaries); authority requirement for commit/push/deploy/destructive ops preserved.
- `docs/external-capabilities.md` → `guidance/external-capabilities.md` — same category list and discover→authority→boundary→action→verify→persist pattern; terminology aligned to bounded authority, minimum sufficient context, durable state, verification evidence.
- `docs/workflow-patterns.md` → `guidance/workflow-patterns.md` — same sequential/conditional/parallel patterns; added the parallel-justification rule, the "don't parallelize until contracts/ownership are stable" rule, and "merge through durable state and verification, not assumed shared session context."
- `docs/handoff-template.md` → `templates/handoff.md` — redesigned as a minimal state-transfer artifact built from `core/EXECUTION.md`'s execution-contract fields and `core/STATE.md`'s handoff semantics; explicit that it transfers state, not conversation history, and that SIMPLE work may need none or a few lines.
- `docs/review-template.md` → `templates/review.md` — replaced the v1.1 generic checklist with an adversarial-challenge template aligned to `core/VERIFICATION.md`/`core/ASSURANCE.md`: bounded reviewer context, explicit challenge targets, and Core's finding schema (including provenance tags). No OWASP categories or domain-specific checklists.

`docs/` was deleted entirely (no compatibility stub — nothing in the repo needed the old path once cross-references were updated, so a stub would have been dead weight, not a real compatibility bridge).

Cross-references updated for consistency (not a Core redesign): `core/STATE.md`, `core/WORKFLOW.md`, `core/EXECUTION.md` now point at `guidance/`/`templates/` instead of `docs/`. `skills/software-project-workflow/SKILL.md` and `README.md` had their 5 `docs/*.md` path references mechanically swapped to the new locations — narrow, path-only edits, nothing else in either file touched.

Untouched: all six Core documents' substantive content, `CHANGELOG.md` (historical record), everything else in `README.md` beyond the 5 path strings, and everything else in `SKILL.md` beyond the same 5 path strings.

## Decisions Made
- No compatibility stubs left at the old `docs/*.md` paths — see rationale above.
- `SKILL.md` and `README.md` are both "adapter/non-Core" surfaces that were out of the original narrow scope, but both contained literal stale-path references after the migration; per explicit user direction, both got the same narrow exception: mechanical path-string swap only, no other modernization.
- `guidance/` content stays optional practical guidance; `templates/` content stays optional artifacts. Neither introduces new mandatory ceremony, scoring, or checklists beyond what Core already requires.

## Files Changed
- Deleted: `docs/git-baseline.md`, `docs/external-capabilities.md`, `docs/workflow-patterns.md`, `docs/handoff-template.md`, `docs/review-template.md`, and the now-empty `docs/` directory.
- Added: `guidance/git-baseline.md`, `guidance/external-capabilities.md`, `guidance/workflow-patterns.md`, `templates/handoff.md`, `templates/review.md`.
- Modified (cross-reference only): `core/STATE.md`, `core/WORKFLOW.md`, `core/EXECUTION.md`, `skills/software-project-workflow/SKILL.md`, `README.md`.
- Modified (rewritten to current state): `MNM_HANDOFF.md` (this file).
- Core substantive content, `CHANGELOG.md`, `CONTRIBUTING.md`, `examples/`, `LICENSE`: untouched.

## Verification
- `grep` for all 5 old canonical paths (`docs/git-baseline`, `docs/handoff-template`, `docs/external-capabilities`, `docs/review-template`, `docs/workflow-patterns`) across the repo: zero live references remain; only `CHANGELOG.md`'s two v1.1 historical entries still contain the old paths, intentionally (historical record, not a live reference).
- Confirmed `docs/` no longer exists and no duplicate old/new canonical copies remain anywhere.
- Re-read `guidance/*.md` and `templates/*.md` against all six Core files: no restated Core prose, no new mandatory ceremony, no contradiction found. Both templates explicitly state they're optional; `templates/review.md` and `templates/handoff.md` both explicitly say SIMPLE work doesn't require them.
- `grep -iE "claude|chatgpt|codex|openai|anthropic|gpt|owasp"` across the new files: no positive matches (one intentional negative OWASP reference in `templates/review.md`, mirroring `core/ASSURANCE.md`'s existing pattern).
- `git diff --check`: clean.
- Full `git status` reviewed: exactly the files listed above changed; `.DS_Store` remains untracked and excluded from the commit.

## Open Questions
None blocking. Two known, out-of-scope drift items are recorded below for a later cleanup pass rather than resolved now.

## Known Problems / Risks
- `README.md` still describes a two-file `core/` (`PRINCIPLES.md`, `WORKFLOW.md`) and still lists v1.1-era principles bullets that predate the accepted v2 Core. Only its `docs/*` path references were fixed this round, per explicit scope. Needs a dedicated repository/release cleanup pass, not a Phase 2/3 concern.
- `skills/software-project-workflow/SKILL.md` still lists only `core/PRINCIPLES.md` and `core/WORKFLOW.md` as canonical sources (missing `STATE.md`, `EXECUTION.md`, `VERIFICATION.md`, `ASSURANCE.md`), and its per-file descriptions ("review checklist", "phase handoff format") reflect v1.1 semantics, not the redesigned `templates/review.md`/`templates/handoff.md`. Only its `docs/*` path references were fixed this round, per the same narrow scope. This is adapter/skill content and belongs to a future skills-alignment phase, not Phase 2's guidance/templates migration.

## Next Recommended Step
Independent review of the Phase 2 diff (see Review Target below). After sign-off, Phase 3 scoping — not started as part of this unit. The two known-drift items above (README, SKILL.md) are candidates for a future cleanup phase, separate from Phase 3's own scope.

## Review Target
Review the full Phase 2 diff: the five new `guidance/`+`templates/` files against the five deleted `docs/` files (content realignment, not just relocation), and the five cross-reference-only edits (`core/STATE.md`, `core/WORKFLOW.md`, `core/EXECUTION.md`, `SKILL.md`, `README.md`). Specifically check:
- No Core prose was restated in `guidance/`/`templates/` instead of cross-referenced.
- No new mandatory ceremony was introduced for SIMPLE work.
- The `SKILL.md`/`README.md` edits are genuinely path-only, with no other content drift introduced.
- The two known-drift items above are acceptable to defer rather than fix now.
