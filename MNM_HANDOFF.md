# MNM Development Handoff

## Current State
- Branch: `v2/core-protocol`
- HEAD: will be the commit created by this handoff (see commit SHA reported after push)
- Current phase: v2 Phase 3 — Capability System + First Capabilities (complete, pending independent review)
- Status: Phase 1 Core and Phase 2 Guidance + Templates remain ACCEPTED and unmodified this round. Phase 3 adds the capability system and its first two capabilities. Phase 4 not started.

## What Changed
Added a new `capabilities/` directory implementing the capability layer that `core/ASSURANCE.md` already defines the generic contract for:

- `capabilities/README.md` — defines what a capability is and isn't (not necessarily a separate agent/skill/checklist/standard/tool integration/mandatory review), the four-layer separation (Core → Capability → Runtime adapter/specialist implementation → Project), the two governing rules (no duplicating Core rules; no claiming applicability by mere existence — applicability/control & verification depth/independence stay separate decisions per `core/ASSURANCE.md`), and an index of the two capabilities that exist today plus a note that other recognized assurance lenses don't get a document until specified and tested.
- `capabilities/application-security.md` — fills the seven-field capability contract (Purpose, Applicability signals, Design concerns, Control guidance, Verification guidance, Challenge method, Expected evidence) with MNM's own application-security expertise. No OWASP category names or descriptions.
- `capabilities/genai-security.md` — fills the same contract for systems that use models or agentic AI, including the generalized principle that AI interpretation must not silently become authoritative deterministic fact, and that model-consumed content is untrusted even when it's an authoritative stored artifact elsewhere in the system. No OWASP GenAI/LLM Top 10 category names or descriptions.

Both capability documents: state design/control guidance before challenge/verification (shift-left, not audit-only); state applicability is signal-based, never automatic; state verification/challenge steps apply only where warranted, not as a mandatory checklist; cross-reference `core/EXECUTION.md` (mature primitives, authority) and `core/VERIFICATION.md` (verification classes, independent challenge, finding schema) instead of restating them; include a Cross-domain note that a capability classifies and challenges concerns rather than owning a separate copy of controls another lens also relies on; and note, as an optional implementation-level detail, that a specialized runtime-level security-review implementation can satisfy or strengthen the Challenge Method when available — never fetched, installed, or made mandatory here.

Nothing in Core, `guidance/`, `templates/`, `README.md`, `CHANGELOG.md`, or `skills/` was touched this round.

## Decisions Made
- Only the two capabilities with real evidence (application security, GenAI/LLM security) were written; no other assurance lens got a capability document, per explicit scope.
- No reference to any specific external security-review implementation (by name or otherwise) was added — the capability documents describe the *relationship* (an implementation can strengthen the Challenge Method) without naming, requiring, or depending on one.
- `capabilities/README.md`'s "Runtime adapter / specialist implementation" layer is described conceptually only; nothing was built for it this phase.

## Files Changed
- Added: `capabilities/README.md`, `capabilities/application-security.md`, `capabilities/genai-security.md`.
- Everything else in the repository: untouched.

## Verification
- Re-read all three new files against `core/ASSURANCE.md` side by side: the seven-field capability contract is filled, not redefined; nothing contradicts Core.
- Grepped both capability files for OWASP Top-10 / LLM-Top-10 category labels (Broken Access Control, Insecure Design, Excessive Agency, System Prompt Leakage, Unbounded Consumption, etc.) and "OWASP" itself: no matches. "Prompt injection" appears only as the generic, pre-existing security-industry term the user's own spec explicitly required as design-concern/verification content — not as a copied Top-10 category description.
- Confirmed both files state applicability is signal-based ("signals, not an exhaustive checklist") and that verification/challenge steps are qualified ("only where applicable" / "not all mandatory for every application").
- Confirmed section order in both capability files is Purpose → Applicability signals → Design concerns → Control guidance → Verification guidance → Challenge method → Expected evidence — design/control guidance precedes challenge/verification in both.
- `grep -iE "claude|chatgpt|codex|openai|anthropic|gpt"` across the new files: no matches.
- Confirmed exactly three new files exist under `capabilities/`, nothing else created.
- `git diff --cached --check`: clean.
- Full `git status` reviewed: only the three new files staged; `.DS_Store` remains untracked and excluded.

## Open Questions
None blocking.

## Known Problems / Risks
- Carried over, unchanged from Phase 2 (not this round's scope): `README.md` still describes a two-file `core/` and v1.1-era principles bullets; `skills/software-project-workflow/SKILL.md` still lists only `core/PRINCIPLES.md`/`core/WORKFLOW.md` as canonical sources and has stale per-file descriptions. Both are candidates for a future repository/skills cleanup phase, not Phase 3 or Phase 4.
- `capabilities/README.md` names a "Runtime adapter / specialist implementation" layer that has no concrete implementation yet — intentional per this phase's scope, but worth noting so a future phase doesn't mistake the conceptual description for a built adapter.

## Next Recommended Step
Independent review of the Phase 3 diff (see Review Target below). After sign-off, Phase 4 scoping — not started as part of this unit.

## Review Target
Review the three new files in `capabilities/` against `core/ASSURANCE.md`'s capability contract and against the task's anti-goals. Specifically check:
- Neither capability document is, in substance, an OWASP checklist with the labels swapped out.
- The GenAI capability's "AI interpretation must not silently become authoritative fact" principle reads as general system guidance, not tied to any specific prior case.
- Applicability, control & verification depth, and independence are kept as separate, non-automatic decisions in both files.
- No capability implies a mandatory review phase, a required external tool, or a specific runtime.
