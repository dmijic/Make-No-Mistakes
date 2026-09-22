# Codex adapter

Execution-oriented. Ships as `AGENTS.md`, Codex's native, persistent, always-loaded project-instruction layer (verified: global `~/.codex/AGENTS.md` → project-root `AGENTS.md` → nested — an open convention beyond OpenAI). MNM is closer to an ambient operating manual than a single triggered procedure, so `AGENTS.md` is the better native fit here than Codex's separate, on-demand Skills mechanism.

## Install

Place `AGENTS.md` from this directory at your project's root (or reference it from a project's existing `AGENTS.md`), alongside an accessible copy of MNM's `core/`, `guidance/`, `templates/` and `capabilities/` directories. A project's own `AGENTS.md` does not need to duplicate MNM's methodology text — see the file's "Durable state, not project instruction bloat" section.

This is the source adapter. A self-contained, installable package that bundles the canonical directories together with this entry point is Phase 5 work, not done here.
