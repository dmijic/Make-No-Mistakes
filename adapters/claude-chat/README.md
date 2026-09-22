# Claude Chat adapter

Design-oriented. Ships as a Claude.ai Skill (the open Agent Skills format: a directory with `SKILL.md`).

Not targeted: Claude Projects on their own — a Project's custom instructions and knowledge files are project-specific context MNM can consume, not the mechanism that installs the protocol itself.

## Install

Package `skills/software-project-workflow/` from this directory as a .zip (the skill folder containing `SKILL.md`) and upload it in claude.ai via Settings → Customize → Skills. Claude loads the skill's name and description first, and the full instructions when a task matches.

This is the source adapter. A self-contained, installable package that bundles the canonical directories together with this skill is Phase 5 work, not done here.
