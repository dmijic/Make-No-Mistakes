# Project State

Project continuity must never depend on conversation or agent-session continuity (`core/PRINCIPLES.md` invariant 5). This file defines what durable state is, when to persist it, how it's classified, and how a session should begin and end.

## What is durable

The repository, its canonical documentation, its version history and its verification evidence form persistent project memory. Chat sessions and individual agent sessions are temporary working environments.

Code, tests and Git history are themselves valid durable state — documentation is not the only form of project memory.

Durable project state may include, when relevant:

- purpose, scope, requirements, constraints
- verified facts, assumptions, open questions
- consequential decisions
- system design, critical invariants
- implementation state, assurance state
- verification evidence
- known limitations, residual risks
- next bounded action

This is not a mandatory filesystem structure or schema. Represent whichever of these are relevant, wherever they naturally belong in the project (docs, code comments where genuinely load-bearing, commit history, issue tracker, test suite).

**Persistence rule:** persist information when losing it would make future work materially less safe, correct, efficient or understandable. Do not persist ephemeral reasoning merely because it occurred.

## Knowledge state

Mark project knowledge with one of:

- **VERIFIED** — confirmed against the project, environment or an authoritative source.
- **PROPOSAL** — a suggested direction, not yet decided.
- **ASSUMPTION** — treated as true for now but not verified; consequential assumptions should be tracked toward verification.
- **OPEN** — an unresolved question. An OPEN item should state whether it blocks the current bounded objective.
- **TBD** — intentionally deferred, not currently relevant.

Do not invent additional status taxonomies beyond these. UNVERIFIED is a verification result, not a knowledge state — see `core/VERIFICATION.md`.

## Context classes

- **CANONICAL** — the project's source of truth: accepted requirements, decisions, architecture, verified facts.
- **TASK** — scoped to the current bounded objective.
- **HISTORICAL** — past reasoning, prior sessions, superseded proposals.
- **EPHEMERAL** — working notes with no lasting value.

Load context by funneling down to what's needed, not by loading everything by default:

```text
current objective
    -> relevant canonical state
    -> current repository/project reality
    -> required evidence
    -> minimum sufficient context
```

## Session lifecycle

A session should:

1. identify the bounded objective
2. recover durable state
3. inspect current reality (repository, environment)
4. resolve blocking unknowns
5. load minimum sufficient context
6. perform the work
7. verify
8. persist consequential state
9. record unresolved state
10. end

**Session continuity must never be required for project continuity.** A handoff is state transfer, not a conversation transcript — see `templates/handoff.md` for the transfer format.
