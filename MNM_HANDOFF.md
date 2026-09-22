# MNM Development Handoff

## Current State
- Branch: `v2/core-protocol`
- HEAD: will be the commit created by this handoff (see commit SHA reported after push)
- Current phase: v2 Phase 4 — Runtime Adapters (complete, pending independent review)
- Status: Phases 1–3 remain ACCEPTED and unmodified this round except one flagged mechanical wording fix in `capabilities/README.md`. Phase 4 adds four source runtime adapters and removes the legacy v1.1 skill. Phase 5 not started.

## What Changed

Added `adapters/README.md` (the adapter-system overview: the eight invariants, the four-way index, and the note that three adapters share the open Agent Skills format while Codex uses its own `AGENTS.md`) plus four source adapters:

- `adapters/chatgpt/` — design-oriented ChatGPT Skill (`skills/software-project-workflow/SKILL.md` + `README.md`).
- `adapters/claude-chat/` — design-oriented Claude.ai Skill, written independently (not copy-pasted from the ChatGPT one, per explicit instruction), same semantic behavior.
- `adapters/codex/` — execution-oriented `AGENTS.md` + `README.md`.
- `adapters/claude-code/` — execution-oriented Claude Code Skill (`skills/software-project-workflow/SKILL.md` + `README.md`).

Each adapter cross-references the canonical `core/`, `guidance/`, `templates/`, `capabilities/` directories rather than containing copies, states the same `core/WORKFLOW.md` adaptive loop framed for that runtime's typical entry point (design-oriented: UNDERSTAND→…→PERSIST/HANDOFF; execution-oriented: RECOVER DURABLE STATE→…→PERSIST STATE+EVIDENCE), states full MNM access is retained despite the default orientation, and states its default is not a hard wall (design-oriented runtimes may inspect/review/verify/challenge; execution-oriented runtimes may identify invalid requirements/broken assumptions/missing decisions and must escalate rather than silently redesign).

Removed the legacy `skills/software-project-workflow/` (its `SKILL.md` and the unverified `agents/openai.yaml`) — see Decisions Made.

Fixed one Phase 3 wording issue in `capabilities/README.md` (flagged by independent review): "Nothing in `capabilities/` is built or referenced in this phase" → "No runtime adapter or specialist implementation is built or required by this capability layer." No other change to that file.

Made the minimum mechanical fix to `README.md` needed to avoid a factually broken reference: its structure-tree `skills/` block (pointing at the now-deleted legacy path) is replaced with an `adapters/` entry, and the "Using it" section now points at `adapters/` instead of the deleted `skills/software-project-workflow` path. The stale 2-file `core/` listing and v1.1 principles bullets remain untouched — that broader rewrite is still deferred, per explicit instruction not to expand scope.

## Decisions Made

- **Verified runtime facts, materially affecting structure**: Agent Skills (`SKILL.md`: YAML frontmatter + markdown instructions, optional supporting files) is a real, open, cross-vendor standard (agentskills.io, originally from Anthropic) now supported by Claude Code, Claude.ai (paid plans), ChatGPT, and Codex. Codex additionally has `AGENTS.md` as a separate, persistent, always-loaded layer. OpenAI is retiring Custom GPTs (creation ends 2026-09-25, shutdown 2026-12-11).
- Initially proposed building the ChatGPT adapter on ChatGPT Projects (verified as the surviving mechanism after Custom GPTs' retirement) — **user corrected this**: Projects are project-specific context/state, not an MNM installation mechanism; target ChatGPT's Skills feature instead, since it's the real, current, cross-vendor-compatible mechanism.
- Given that correction and the verified facts, **ChatGPT, Claude Chat and Claude Code adapters all converge on the identical open `SKILL.md` format** — differing per-adapter in README install instructions and in default responsibility-emphasis content (design-oriented for chatgpt/claude-chat, execution-oriented for claude-code), not in file format. Codex keeps its own native `AGENTS.md` (persistent operating-manual layer) rather than a second Skill, to stay thin.
- **Legacy skill**: removed `skills/software-project-workflow/` entirely rather than leaving it as a second, competing Claude Code entry point alongside the new `adapters/claude-code/skills/software-project-workflow/SKILL.md`. Confirmed with the user before executing. `agents/openai.yaml` (an `interface.display_name` manifest) matched no verified real Claude Code or OpenAI convention found during research and was not carried forward.
- **README**: initially planned to leave `README.md` untouched and only report the resulting broken reference (following Phase 2's narrower precedent). **User corrected this**: make the minimum mechanical edit needed to remove the broken reference and reflect `adapters/`'s existence, without doing the broader v1.1→v2 rewrite. Applied as described above.

## Files Changed
- Added: `adapters/README.md`, `adapters/chatgpt/README.md`, `adapters/chatgpt/skills/software-project-workflow/SKILL.md`, `adapters/claude-chat/README.md`, `adapters/claude-chat/skills/software-project-workflow/SKILL.md`, `adapters/codex/README.md`, `adapters/codex/AGENTS.md`, `adapters/claude-code/README.md`, `adapters/claude-code/skills/software-project-workflow/SKILL.md`.
- Removed: `skills/software-project-workflow/SKILL.md`, `skills/software-project-workflow/agents/openai.yaml` (and the now-empty `skills/` directory).
- Modified: `capabilities/README.md` (one-line wording fix), `README.md` (minimum mechanical fix for the broken `skills/` reference, per user correction).
- Core (`core/*.md`), `guidance/`, `templates/`, and the rest of `capabilities/` (README's substance, `application-security.md`, `genai-security.md`): untouched.

## Runtime Assumptions Verified
- Agent Skills open standard (`SKILL.md`) — supported by Claude Code, Claude.ai (paid), ChatGPT, Codex.
- Codex's `AGENTS.md` hierarchy (global → project-root → nested), open standard beyond OpenAI.
- ChatGPT Custom GPTs retiring (2026-09-25 creation cutoff, 2026-12-11 shutdown); ChatGPT Projects and Claude Projects both confirmed to persist but are explicitly *not* targeted as the MNM installation mechanism (project-context containers, not protocol carriers).
All verified via web search this session (dated September 2026); not assumed from training data alone.

## Legacy Skill Treatment
Removed (option B from the task's A/B framing), not marked-deprecated-in-place, because leaving both the legacy skill and the new Claude Code adapter would have created two competing canonical entry points for the same runtime — explicitly warned against. Confirmed with the user before executing (see Decisions Made).

## Known README / Release Drift
- `README.md` still shows a stale 2-file `core/` (`PRINCIPLES.md`, `WORKFLOW.md`) and v1.1-era principles bullets, and does not mention `capabilities/`. Only the `skills/`→`adapters/` breakage from this phase was fixed, per explicit instruction not to expand scope into the full README/release rewrite. Still deferred to a future repository/release cleanup phase.
- No new broken references were introduced beyond the one fixed above.

## Verification
- Confirmed exactly four adapter directories exist under `adapters/`, each referencing canonical directories rather than containing copies (`grep` for Core-specific prose inside `adapters/` found no matches — nothing restated).
- Confirmed no adapter redefines knowledge states, workflow semantics, execution-contract semantics, verification/assurance semantics, finding provenance, capability contracts, workflow profiles, or Core invariants — all cross-referenced by filename/section only.
- Confirmed chatgpt/claude-chat content states full MNM access despite design default (may inspect implementation, review diffs, apply verification/assurance, challenge).
- Confirmed codex/claude-code content states full MNM access despite execution default (may identify invalid requirements/broken assumptions/missing decisions; must escalate rather than silently redesign).
- Confirmed no adapter requires conversation/session continuity, mandates multi-agent execution, mandates review for SIMPLE work, requires network/GitHub access for protocol semantics, or requires Core to be copied into every project repository.
- Confirmed no Phase 5 packaging artifacts exist (`find` for `dist`, `*.zip`, `.mnm` — no output).
- Confirmed `core/`, `guidance/`, `templates/`, `capabilities/` remain free of runtime/vendor names (`grep -rliE "claude|chatgpt|codex|openai|anthropic|gpt"` — no output); such names appear only inside `adapters/`, where they belong.
- `git diff --cached --check` — clean.
- Full `git diff --cached --stat` reviewed: 13 files, matches intended scope exactly.

## Open Questions
None blocking.

## Next Recommended Step
Independent review of the Phase 4 diff (see Review Target below). After sign-off, Phase 5 (self-contained, installable packages built from `core/`+`guidance/`+`templates/`+`capabilities/`+one adapter) — not started as part of this unit.

## Review Target
Review the four adapters against `adapters/README.md`'s eight invariants and against `core/WORKFLOW.md`/`core/EXECUTION.md` for the loop-framing and escalation language. Specifically check:
- The ChatGPT/Claude Chat pivot from Projects to Skills (per your correction) is applied consistently across both adapters' content and READMEs.
- The claude-chat SKILL.md reads as independently written, not a renamed copy of the chatgpt one.
- The legacy-skill removal and the README mechanical fix match what you approved.
- The remaining README v1.1 drift (2-file `core/` listing, old principles, no `capabilities/` mention) is acceptable to keep deferring.
