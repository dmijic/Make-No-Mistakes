# Workflow

Choose the smallest workflow that safely covers the project's complexity.

## Simple

`Requirements -> Implementation -> Review -> Commit`

Use for small, well-understood changes with few unknowns.

## Medium

`Research -> Specification/Architecture -> Baseline -> Implementation -> Review -> Commit`

Use when the project has meaningful design choices, integrations or existing code that must be understood first.

## Complex

`Discovery -> Research/Probes -> Specification -> Architecture -> Repository Cleanup/Baseline -> Implementation Passes -> Review Loops -> Deployment/Hardening`

Use when requirements, integrations, security, architecture, deployment or project state contain substantial uncertainty.

## Persistent project memory

Treat these as durable:

1. Repository
2. Canonical documentation
3. Git history

Treat chat sessions and individual AI agents as temporary working environments.

## Phase rule

Split work further when a phase becomes too large or mixes incompatible concerns. Do not create phases or agent sessions merely for ceremony.

See `docs/` for workflow patterns, Git baseline guidance, handoff templates, review templates and integration guidance.
