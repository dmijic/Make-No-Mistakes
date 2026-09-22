# ChatGPT adapter

Design-oriented. Ships as a ChatGPT Skill (the open Agent Skills format: a directory with `SKILL.md`).

Not targeted: Custom GPTs (OpenAI is retiring this mechanism) or ChatGPT Projects (project-level context/state that MNM can consume, not an installation mechanism for the protocol itself).

## Install

In ChatGPT, go to Skills → Create → Create with editor, or Upload from computer/GitHub, and provide `skills/software-project-workflow/SKILL.md` from this directory. ChatGPT loads the skill's name and description first, and the full instructions when a task matches.

This is the source adapter. A self-contained, installable package that bundles the canonical directories together with this skill is Phase 5 work, not done here.
