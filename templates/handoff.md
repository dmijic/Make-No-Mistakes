# Handoff template

Optional. A handoff transfers project state, not conversation history (`core/STATE.md`). Use it when a bounded objective needs to cross a session boundary and the receiving session shouldn't have to reconstruct context from a transcript.

This is not a mandatory document. For SIMPLE work a handoff may be unnecessary, or only a few lines covering objective, baseline and acceptance. Fill in only the fields relevant to this objective's scope and consequence (`core/EXECUTION.md` execution contract).

```markdown
## Objective
What this bounded unit of work must deliver.

## Baseline
- Repository / branch:
- Git commit:
- Verified starting state:

## Scope
What this unit covers.

## Out of scope
What must remain untouched or deferred.

## Canonical inputs
Relevant specification, architecture, prior decisions — pointers, not copies.

## Requirements / acceptance criteria
Objectively testable where practical (core/EXECUTION.md requirement trace).

## Consequential decisions
Decisions already made that this work must honor (core/PRINCIPLES.md invariant 6).

## Critical invariants
Stateful or high-consequence invariants this work must not violate (core/EXECUTION.md).

## Constraints
Technical, authority, or timing constraints that bound the work.

## Blocking unknowns
OPEN items that block this objective (core/STATE.md knowledge state).

## Required verification
Which verification classes apply, and why (core/VERIFICATION.md).

## Assurance expectations
Which assurance lenses are applicable, and at what depth (core/ASSURANCE.md).

## Authority boundary
What the receiving session may read, modify, execute, access externally, write externally, deploy — and what it may not (core/EXECUTION.md).

## Unresolved state / known limitations
What is intentionally left open, and why.

## Expected completion report
What evidence the receiving session should return: files changed, verification results, residual risks, next bounded action.
```
