# Claude Code adapter

Execution-oriented. Ships as a Claude Code Skill (the open Agent Skills format: a directory with `SKILL.md`).

## Install

Place `skills/software-project-workflow/` from this directory under your project's `.claude/skills/` (project-scoped) or `~/.claude/skills/` (personal, all projects), alongside an accessible copy of MNM's `core/`, `guidance/`, `templates/` and `capabilities/` directories. Claude Code loads the skill's name and description first and reads the full `SKILL.md` body when the task matches.

This is the source adapter. A self-contained, installable package that bundles the canonical directories together with this skill is Phase 5 work, not done here.
