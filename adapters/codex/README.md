# Codex adapter

Execution-oriented. Ships as a Codex Skill (the open Agent Skills format: a directory with `SKILL.md`) — the same reusable entry point used by the other three adapters, so MNM stays a reusable installed methodology rather than something injected into every project's own instruction file.

Codex's `AGENTS.md` is a separate, persistent project-instruction surface. A project may have one; MNM treats it as optional project/runtime context to consume, not as the MNM installation mechanism.

## Install

Install `skills/software-project-workflow/` from this directory as a Codex skill, alongside an accessible copy of MNM's `core/`, `guidance/`, `templates/` and `capabilities/` directories. Codex loads the skill's name and description first and the full instructions when a task matches.

This is the source adapter. A self-contained, installable package that bundles the canonical directories together with this skill is Phase 5 work, not done here.
