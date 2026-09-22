# MNM Development Handoff

## Current State
- Branch: `v2/core-protocol`
- HEAD: will be the commit created by this handoff (see commit SHA reported after push)
- Current phase: v2 Phase 4 — Runtime Adapters (stable, review fixes applied, pending independent re-review)
- Status: Phases 1–3 remain ACCEPTED. Phase 4's initial implementation had one blocking architecture issue and two minor documentation issues, both now fixed. Phase 5 not started.

## What Changed (this round — independent-review fixes on top of Phase 4)

**1. BLOCKING, fixed — Codex adapter architecture.** The initial Codex adapter shipped as `adapters/codex/AGENTS.md`, instructing installation at a project's root. Independent review found this violated the accepted boundary (MNM installation ≠ project/runtime instruction state): `AGENTS.md` is Codex's own persistent project-instruction surface and must not be the carrier of the MNM protocol.
- Removed `adapters/codex/AGENTS.md`.
- Added `adapters/codex/skills/software-project-workflow/SKILL.md` — same execution-oriented semantic content (canonical-source note, the `core/WORKFLOW.md` loop framed for execution entry, agent capability model, proportional ceremony), now delivered as the same reusable Agent Skills format the other three adapters use.
- Rewrote `adapters/codex/README.md`: install instructions now describe installing the Skill; a project's own `AGENTS.md`, if it has one, is described as optional project/runtime context MNM can consume, not the installation mechanism.
- Updated `adapters/README.md`: the adapter table now lists "Codex Skill (Agent Skills format)"; the closing paragraph now states all four adapters share the reusable Skill entry point, and names `AGENTS.md`/`CLAUDE.md`/Project instructions collectively as optional project/runtime context a runtime may have alongside MNM — never the installation mechanism (invariant 7).
- No `AGENTS.md` template was added anywhere else, per instruction.

**2. MINOR, fixed — Claude Chat plan-availability wording.** `adapters/claude-chat/README.md` stated Skills were unavailable on the Free plan; current Anthropic documentation says Skills are available on Free, Pro, Max, Team and Enterprise (subject to required capabilities/settings). Removed the plan-specific availability sentence entirely rather than restate a corrected but still-volatile commercial fact.

**3. MINOR, fixed — Claude Chat upload instructions.** Corrected to describe packaging `skills/software-project-workflow/` as a `.zip` and uploading it via Settings → Customize → Skills, matching current Anthropic documentation.

**4. Volatile-fact sweep.** Reviewed all four adapter READMEs for other unnecessary volatile claims. Removed the specific Custom GPT retirement dates from `adapters/chatgpt/README.md` (kept the qualitative "OpenAI is retiring this mechanism," dropped the calendar dates, which will go stale and aren't needed to justify not targeting Custom GPTs). No other volatile plan/date/UI claims found in `claude-code/README.md` or `codex/README.md`. Did not broaden this into a general release-documentation cleanup, per instruction.

## Decisions Made
- Preserved semantic behavior exactly when converting Codex from `AGENTS.md` to a Skill: the same canonical-source note, the same execution-oriented loop framing, the same agent-capability-model and proportional-ceremony sections — only the delivery mechanism and install instructions changed.
- `adapters/README.md`'s closing paragraph now generalizes the "optional project/runtime context, not an installation mechanism" point across all three native project-instruction surfaces (`AGENTS.md`, `CLAUDE.md`, Project instructions) instead of only Codex, since the same principle applies uniformly and stating it once avoids repeating it per-adapter.

## Files Changed (this round)
- Removed: `adapters/codex/AGENTS.md`.
- Added: `adapters/codex/skills/software-project-workflow/SKILL.md`.
- Modified: `adapters/codex/README.md`, `adapters/README.md`, `adapters/chatgpt/README.md`, `adapters/claude-chat/README.md`.
- Untouched: `adapters/chatgpt/skills/.../SKILL.md`, `adapters/claude-chat/skills/.../SKILL.md`, `adapters/claude-code/` (entirely), Core, `guidance/`, `templates/`, `capabilities/`.

## Verification
- Confirmed exactly four adapter directories exist under `adapters/`, all four now using the reusable Agent Skills `SKILL.md` entry point.
- Confirmed no `AGENTS.md` remains anywhere under `adapters/` (`find -iname AGENTS.md` — no output).
- Confirmed Codex no longer requires project-root `AGENTS.md` for MNM; its README and Skill both describe `AGENTS.md` as optional, consumable project context.
- Confirmed `adapters/README.md` states project `AGENTS.md`/`CLAUDE.md`/Project instructions are optional context, never MNM protocol carriers, for all runtimes uniformly.
- Confirmed all adapters still state full MNM protocol access, and design/execution orientation is unchanged (chatgpt/claude-chat still design-oriented; codex/claude-code still execution-oriented) — verified via grep across all four `SKILL.md` files.
- Confirmed no Core duplication (grep for Core-specific prose inside `adapters/` — no matches) and `core/`/`guidance/`/`templates/`/`capabilities/` remain free of runtime/vendor names.
- Confirmed no Phase 5 packaging artifacts exist.
- `git diff --cached --check` — clean.
- Full diff reviewed: 5 files changed (1 removed, 1 added, 3 modified), matches the bounded fix scope exactly — no unrelated files touched.

## Open Questions
None blocking.

## Known Problems / Risks
Carried over, unchanged (not this round's scope): `README.md` still shows a stale 2-file `core/` listing, v1.1 principles bullets, and no `capabilities/` mention — deferred to a future repository/release cleanup phase.

## Next Recommended Step
Independent re-review of this fix round (see Review Target below). After sign-off, Phase 5 — not started as part of this unit.

## Review Target
Review the diff on `adapters/codex/` (AGENTS.md → Skill conversion preserves semantic content), `adapters/README.md` (invariant 7 now applies uniformly across all native project-instruction surfaces), and `adapters/{chatgpt,claude-chat}/README.md` (plan-availability and upload-instruction corrections, retirement-date removal). Confirm the Codex Skill's execution-oriented content reads as equivalent to the original `AGENTS.md` version, just re-delivered.
