# Principles

Make No Mistakes is an adaptive software-engineering protocol for turning uncertain intent into verified software through explicit requirements and decisions, durable project state, bounded execution, proportional assurance, independent challenge, and evidence-backed completion.

It is technology, runtime, vendor and model agnostic. It applies to a single AI agent working alone as readily as to multiple agents working together.

## Primary objective

Correct, secure, maintainable and operable software, supported by evidence.

MNM does not optimize for maximum process, maximum documentation, maximum agent count, passing checklists, or architectural sophistication for its own sake. Use proportional engineering rigor: no more process than the work's uncertainty and consequence require, no less than they demand.

## Invariants

These ten invariants hold regardless of project size, language or runtime. `core/WORKFLOW.md`, `core/STATE.md`, `core/EXECUTION.md`, `core/VERIFICATION.md` and `core/ASSURANCE.md` define how each is applied in practice.

1. **Minimum safe process.** Use the smallest process that safely addresses current uncertainty, consequence and risk.
2. **Inspect before ask.** Prefer verified information available from the project, environment and authoritative sources over asking humans to repeat discoverable information.
3. **Minimum sufficient context.** Load only authoritative and relevant context required for the bounded objective.
4. **Verified over assumed.** Important unknowns must be verified or explicitly represented as unknown.
5. **Durable state outside sessions.** Project continuity must never depend on conversation or agent-session continuity.
6. **Explicit consequential decisions.** Decisions capable of materially affecting architecture, security, privacy, compatibility, data integrity or operations must not emerge accidentally during implementation.
7. **Bounded authority.** Agents receive only the scope, capabilities, tools and external authority required for their task.
8. **Preserve verified contracts.** Existing verified behavior and contracts remain valid unless the requirement explicitly changes them.
9. **Completion requires evidence.** Generated output or agent confidence does not establish completion.
10. **Independent challenge when warranted.** Higher-consequence work should receive sufficiently independent challenge.

## Why

The goal is not to pretend an AI agent will make no mistakes. The goal is to make mistakes observable and recoverable: structure the work so unsupported assumptions, architectural drift and silent consequential decisions are easy to detect, review and correct, at a cost proportional to what's actually at stake.
