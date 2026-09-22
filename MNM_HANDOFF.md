# MNM Development Handoff

## Current State
- Branch: `v2/core-protocol`
- HEAD: will be the commit created by this handoff (see commit SHA reported after push)
- Current phase: v2 Phase 1 — Core Protocol (complete)
- Status: Phase 1 verified and committed. Phase 2 not started.

## What Changed
Evolved MNM Core from v1.1 (two files: `PRINCIPLES.md`, `WORKFLOW.md`) into six files that together define the v2 adaptive protocol:

- `core/PRINCIPLES.md` (modified) — protocol definition, primary objective/non-goals, the 10 core invariants, closing rationale.
- `core/WORKFLOW.md` (modified) — adaptive engineering loop (INTENT→...→COMPLETE) as responsibilities rather than mandatory phases, FINDING trigger, depth factors, SIMPLE/MEDIUM/COMPLEX profiles.
- `core/STATE.md` (new) — durable state semantics, persistence rule, knowledge-state vocabulary, context classes, session lifecycle.
- `core/EXECUTION.md` (new) — bounded execution contract, requirement trace, system invariants, mature-primitives guidance, escalation protocol, change safety, agent capability model, authority boundary.
- `core/VERIFICATION.md` (new) — verification classes/results, PASS-requires-evidence rule, verification-evidence vs. domain-evidence, independent challenge, findings and escape analysis.
- `core/ASSURANCE.md` (new) — system-first assurance flow, assurance lenses, generic capability contract, three assurance dimensions, cross-domain controls, Definition of Done.

Nothing outside `core/` was touched: README, CHANGELOG, CONTRIBUTING, `docs/`, `skills/`, `examples/` are unchanged in Phase 1.

## Decisions Made
- Superseded v1.1's fixed phase-boundary model with an adaptive loop of engineering responsibilities; phases are no longer mandatory ceremony.
- "Review before advancing" is **not** a universal gate in v2: independent challenge (invariant 10) is required only when warranted by consequence/risk; SIMPLE changes are explicitly exempted from a formal review phase or independent reviewer, and no loop responsibility requires its own commit.
- Secrets/production-safety guidance relocated from a standalone principle into `EXECUTION.md`'s Authority section (stated once, not duplicated).
- Knowledge-state vocabulary extended from v1.1's VERIFIED/PROPOSAL/OPEN/TBD to also include ASSUMPTION and UNVERIFIED (both explicitly spec-authorized, not an invented taxonomy).
- Assurance dimensions (applicability / required rigor / independence) are assessed separately and deliberately left without a locked BASIC/STANDARD/ELEVATED/CRITICAL-style enum.
- No OWASP or other vendor/standard category lists encoded in Core; that's left to future capabilities.

## Files Changed
- Modified: `core/PRINCIPLES.md`, `core/WORKFLOW.md`
- Added: `core/STATE.md`, `core/EXECUTION.md`, `core/VERIFICATION.md`, `core/ASSURANCE.md`
- Added: `MNM_HANDOFF.md` (this file — development coordination artifact, not part of Core, not included in runtime packages)

## Verification
- All six Core files re-read together as one system; checked for contradictory terminology, duplicated rules, runtime/vendor leakage, accidental mandatory ceremony, implicit multi-agent assumptions, and PASS-without-evidence gaps — none found.
- `grep -iE "claude|chatgpt|codex|openai|anthropic|gpt|owasp"` across `core/*.md` — no positive matches (one intentional negative reference in `ASSURANCE.md` stating OWASP categories are *not* encoded in Core).
- `git diff --check -- core/` — clean, no whitespace/EOF issues.
- Mentally validated against three acceptance scenarios (optional API field / password reset / security-scanning subsystem): workflow depth, challenge requirements and assurance lenses scale proportionally to consequence rather than code size in each case.
- This is document/methodology work with no build or test suite; verification is diff review plus the self-review pass above, not automated test evidence.

## Open Questions
- `ASSURANCE.md`'s second dimension is named "Required rigor" rather than the spec's literal "REQUIRED CONTROLS / VERIFICATION DEPTH" — shortened for concision, meaning preserved. Confirm this rename is acceptable or revert to the longer form.
- `STATE.md` (knowledge state) and `VERIFICATION.md` (verification result) both use `UNVERIFIED` for two distinct concepts (status of a fact vs. outcome of a check). Intentional and spec-authorized, but worth a second look once Phase 2 capabilities start referencing it, to confirm it doesn't read as accidental overlap.

## Known Problems / Risks
- None identified. Phase 1 is scoped to `core/` only; no runtime, packaging, or skill-adapter code was touched, so no regression risk to existing integrations.

## Next Recommended Step
Independent review of the six Core files (see Review Target below). After review sign-off, begin Phase 2 scoping — not started as part of this unit.

## Review Target
Review `core/PRINCIPLES.md`, `core/WORKFLOW.md`, `core/STATE.md`, `core/EXECUTION.md`, `core/VERIFICATION.md`, `core/ASSURANCE.md` as one coherent system (diff against the previous commit for `PRINCIPLES.md`/`WORKFLOW.md`; the other four are new). Specifically check:
- No file duplicates another's rules instead of cross-referencing it.
- No runtime/vendor/model-specific assumptions leaked into Core.
- Every mandatory-sounding rule is proportional (no forced ceremony for low-consequence work) and every optional/conditional rule is clearly marked as such.
- The two open questions above, and whether the rename/vocabulary decisions should stand.
