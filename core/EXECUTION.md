# Execution

Execution implements accepted intent within a bounded contract. It must not silently redesign consequential project behavior (`core/PRINCIPLES.md` invariant 6).

## The execution contract

A bounded execution task may need, according to its scope and consequence:

- objective
- scope, and explicitly out of scope
- verified baseline
- requirements
- consequential decisions
- critical invariants
- constraints
- acceptance criteria
- required verification
- assurance expectations
- authority boundary

This is a semantic contract, not necessarily a separate file. For SIMPLE work it may be a sentence; for COMPLEX work it may warrant a written handoff (`docs/handoff-template.md`).

## Requirement trace

For meaningful requirements, trace from intent to evidence:

```text
REQUIREMENT -> DESIGN / CONTROL -> IMPLEMENTATION -> VERIFICATION -> EVIDENCE
```

Example:

```text
Requirement:    Tenant A cannot access Tenant B findings.
Control:        Tenant-aware authorization boundary.
Implementation: Central authorization policy, tenant-scoped access.
Verification:   Cross-tenant negative tests.
Evidence:       Passing tests and relevant review evidence.
```

Requirements should be objectively testable where practical. Avoid unverifiable requirements such as "must be secure" or "must be fast" unless refined into observable constraints. This is not a mandate for a heavyweight requirements-management system.

## System invariants

For stateful or high-consequence behavior, state invariants explicitly — for example: a reset token succeeds at most once; raw evidence cannot be mutated; a normalized finding remains traceable to its source evidence; tenant boundaries cannot be crossed.

When correctness depends on state transitions, relevant verification should consider, where applicable: concurrency, replay, retries, duplicate execution, partial failure. Do not require these checks for unrelated simple work.

## Mature primitives

Where behavior is security-sensitive, prefer mature, maintained platform primitives over custom implementations when they satisfy the verified requirement — password hashing, cryptographic randomness, authentication mechanisms, secure protocol implementations, mature parsers and security controls. This is not a blanket prohibition on custom implementation; a custom security-sensitive mechanism needs justification proportional to its consequence.

## Escalation

When implementation discovers a blocking consequential conflict, stop and report:

```text
VERIFIED FACT
CONFLICT
IMPACT
OPTIONS
DECISION REQUIRED
```

Examples that may require escalation: an invalid architecture assumption, contradictory requirements, a missing consequential decision, a material new security or privacy risk, an unacceptable architecture tradeoff, scope expansion, a destructive-action requirement, insufficient authority.

## Change safety

Preserve verified existing behavior and contracts unless the requirement explicitly changes them (`core/PRINCIPLES.md` invariant 8) — including, where applicable: API contracts, database/schema contracts, events, configuration, user-visible behavior, data semantics, deployment compatibility, external integrations.

## Agent capability model

MNM defines generic execution capabilities, not mandatory agents:

- **SCOUT** — investigates.
- **WORKER** — performs bounded implementation.
- **REVIEWER** — independently challenges artifacts and claims.
- **SPECIALIST** — applies domain expertise.

One agent may perform several capabilities. Default to one capable agent. Use additional agents only when they provide meaningful context isolation, genuinely independent parallel work, specialized capability, or independent verification. Multi-agent execution is not inherently superior. Parallelize implementation only after shared contracts and ownership boundaries are sufficiently stable.

## Authority

Execution operates within an explicit authority boundary:

```text
MAY READ
MAY MODIFY
MAY EXECUTE
MAY ACCESS EXTERNAL SYSTEMS
MAY WRITE EXTERNALLY
MAY DEPLOY
MAY NOT
```

Apply least authority, least tooling, and minimum sufficient context (`core/PRINCIPLES.md` invariants 3 and 7). Do not automatically commit, deploy, delete data, access production, expose secrets, or perform other consequential actions without appropriate authorization.
