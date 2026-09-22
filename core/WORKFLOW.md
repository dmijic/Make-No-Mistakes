# Workflow

MNM defines an adaptive engineering loop: a set of responsibilities that produce verified software, not a mandatory sequence of phases.

## The loop

```text
INTENT -> INSPECT -> REQUIRE -> DECIDE -> DESIGN -> CONTROL
       -> IMPLEMENT -> VERIFY -> EVIDENCE -> CHALLENGE -> COMPLETE
```

Every non-trivial change passes through these responsibilities in spirit. It does not need a dedicated phase, document or commit for each one. For a trivial change the loop compresses to:

```text
inspect -> implement -> test -> diff review
```

CHALLENGE is not a mandatory phase gate: it is required only when the work's consequence or risk warrants independent verification (`core/PRINCIPLES.md` invariant 10, `core/VERIFICATION.md`). A SIMPLE change does not require a formal review phase or an independent reviewer. Stable Git states are useful durable boundaries (`core/STATE.md`), but not every responsibility in the loop needs its own commit.

A FINDING at any point can trigger:

```text
FINDING -> ESCAPE ANALYSIS -> REMEDIATE -> RE-VERIFY
```

See `core/VERIFICATION.md` for what a finding must capture and how escape analysis works.

## Adaptive depth

Workflow depth is not determined by change size. It is determined by:

- uncertainty
- consequence
- security exposure
- data sensitivity
- change surface
- reversibility
- integration complexity
- operational impact

**Risk and consequence are not equivalent to implementation size.** A small authentication change may warrant more rigor than a much larger low-risk implementation.

MNM may internally consider broad engineering concerns (security, data integrity, operability) without forcing every concern to appear as explicit ceremony for small, low-consequence work. This progressive disclosure is what keeps SIMPLE changes simple.

## Profiles

Use the smallest profile that safely covers the work's uncertainty and consequence.

**SIMPLE** — small, well-understood, low-consequence change. Loop compresses to inspect, implement, verify, diff review. No independent challenge required by default.

**MEDIUM** — meaningful design choices, integrations, or existing code that must be understood first, and/or moderate consequence. The full loop applies; consequential decisions (`core/PRINCIPLES.md` invariant 6) are made explicit; verification and challenge are scoped to what the risk warrants (`core/VERIFICATION.md`, `core/ASSURANCE.md`).

**COMPLEX** — substantial uncertainty in requirements, integrations, security, architecture, deployment or project state; high consequence; multiple system invariants at stake. The full loop applies with layered verification, explicit system invariants (`core/EXECUTION.md`), and independent, specialized challenge (`core/ASSURANCE.md`).

Split work further when a responsibility becomes too large or mixes incompatible concerns. Do not create phases, documents or agent sessions merely for ceremony.

## Durable memory

Repository, canonical documentation, version history and verification evidence form persistent project memory; chat and agent sessions are temporary working environments. See `core/STATE.md` for the full semantics of what is durable, when to persist it, and how a session should begin and end.

See `docs/workflow-patterns.md` for sequential, conditional and parallel composition of the loop across a larger project.
