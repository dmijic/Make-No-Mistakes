# MNM Development Handoff

## Current State
- Branch: `v2/core-protocol`
- HEAD: will be the commit created by this handoff (see commit SHA reported after push)
- Current phase: v2 Phase 1 — Core Protocol (stable, review fixes applied)
- Status: Phase 1 accepted by independent review with three targeted fixes, now applied and re-verified. Phase 2 not started.

## What Changed
Evolved MNM Core from v1.1 (two files: `PRINCIPLES.md`, `WORKFLOW.md`) into six files that together define the v2 adaptive protocol:

- `core/PRINCIPLES.md` (modified) — protocol definition, primary objective/non-goals, the 10 core invariants, closing rationale.
- `core/WORKFLOW.md` (modified) — adaptive engineering loop (INTENT→...→COMPLETE) as responsibilities rather than mandatory phases, FINDING trigger, depth factors, SIMPLE/MEDIUM/COMPLEX profiles.
- `core/STATE.md` (new) — durable state semantics, persistence rule, knowledge-state vocabulary, context classes, session lifecycle.
- `core/EXECUTION.md` (new) — bounded execution contract, requirement trace, system invariants, mature-primitives guidance, escalation protocol, change safety, agent capability model, authority boundary.
- `core/VERIFICATION.md` (new) — verification classes/results, PASS-requires-evidence rule, verification-evidence vs. domain-evidence, independent challenge, findings and escape analysis.
- `core/ASSURANCE.md` (new) — system-first assurance flow, assurance lenses, generic capability contract, three assurance dimensions, cross-domain controls, Definition of Done.

This round applied three independent-review fixes on top of that baseline (see Decisions Made). Nothing outside `core/` was touched: README, CHANGELOG, CONTRIBUTING, `docs/`, `skills/`, `examples/` remain unchanged in Phase 1.

## Decisions Made
- Superseded v1.1's fixed phase-boundary model with an adaptive loop of engineering responsibilities; phases are no longer mandatory ceremony.
- "Review before advancing" is **not** a universal gate in v2: independent challenge (invariant 10) is required only when warranted by consequence/risk; SIMPLE changes are explicitly exempted from a formal review phase or independent reviewer, and no loop responsibility requires its own commit. The `WORKFLOW.md` loop diagram now renders this directly as `[CHALLENGE WHEN WARRANTED]` rather than leaving it implicit in surrounding prose.
- Secrets/production-safety guidance relocated from a standalone principle into `EXECUTION.md`'s Authority section (stated once, not duplicated).
- Knowledge-state vocabulary (`STATE.md`) is VERIFIED / PROPOSAL / ASSUMPTION / OPEN / TBD. `UNVERIFIED` was removed from this list per independent review: it belongs exclusively to `VERIFICATION.md`'s verification-result vocabulary (PASS/FAILED/NOT RUN/MANUAL CHECK REQUIRED/UNVERIFIED). Rationale: ASSUMPTION already covers "treated as true, not verified," and OPEN covers unresolved knowledge — reusing UNVERIFIED for both a knowledge state and a verification result was redundant and ambiguous.
- `ASSURANCE.md`'s second assurance dimension is named **Control & verification depth** (previously "Required rigor," which drifted from the spec's naming). No scoring levels or enums introduced — applicability, control & verification depth, and independence remain qualitative, assessed separately per concern.
- No OWASP or other vendor/standard category lists encoded in Core; that's left to future capabilities.

## Files Changed
- Modified this round: `core/STATE.md`, `core/WORKFLOW.md`, `core/ASSURANCE.md` (three targeted review fixes)
- Unchanged from Phase 1 baseline: `core/PRINCIPLES.md`, `core/EXECUTION.md`, `core/VERIFICATION.md`
- `MNM_HANDOFF.md` — development coordination artifact, not part of Core, not included in runtime packages; overwritten to reflect current state.

## Verification
- All six Core files re-read together as one system after the fixes; checked for contradictory terminology, duplicated rules, runtime/vendor leakage, accidental mandatory ceremony, implicit multi-agent assumptions, and PASS-without-evidence gaps — none found.
- Confirmed `UNVERIFIED` now appears only in `VERIFICATION.md`'s result vocabulary and in `ASSURANCE.md`'s Definition of Done (which references the verification-result meaning, not a knowledge state); `STATE.md` explicitly cross-references this instead of restating it.
- Confirmed no other reference to "Required rigor" remains; the two other uses of the word "rigor" in Core are ordinary prose, not the dimension name.
- `grep -iE "claude|chatgpt|codex|openai|anthropic|gpt|owasp"` across `core/*.md` — no positive matches (one intentional negative reference in `ASSURANCE.md` stating OWASP categories are *not* encoded in Core).
- `git diff --check -- core/` — clean, no whitespace/EOF issues.
- This is document/methodology work with no build or test suite; verification is diff review plus the self-review pass above, not automated test evidence.

## Open Questions
None outstanding. The independent reviewer found no other Phase 1 changes necessary beyond the three applied this round.

## Known Problems / Risks
- None identified. Phase 1 is scoped to `core/` only; no runtime, packaging, or skill-adapter code was touched, so no regression risk to existing integrations.

## Next Recommended Step
Phase 1 Core is stable pending final sign-off on this round's fixes. Begin Phase 2 scoping only after that sign-off — not started as part of this unit.

## Review Target
Review the diff on `core/STATE.md`, `core/WORKFLOW.md`, `core/ASSURANCE.md` against the three requested fixes:
1. `STATE.md` Knowledge State no longer lists UNVERIFIED; the note at the end of that section correctly points to `VERIFICATION.md` instead.
2. `WORKFLOW.md`'s canonical loop diagram shows `[CHALLENGE WHEN WARRANTED]`, not a bare `CHALLENGE`.
3. `ASSURANCE.md`'s second dimension reads "Control & verification depth," with no scoring levels or enums introduced anywhere in the dimensions section.

Also confirm the patch stayed narrowly scoped — no unrelated edits were made to `core/PRINCIPLES.md`, `core/EXECUTION.md` or `core/VERIFICATION.md` this round.
