# Application Security

Fills the generic capability contract in `core/ASSURANCE.md` for application-security engineering. This document defines MNM's own reusable application-security expertise — it does not reproduce an external standard's categories or descriptions.

## Purpose

Help identify, prevent, verify and challenge application-security risk throughout requirements, design, implementation and verification — not only at the end of a project.

## Applicability signals

Signals that this capability is likely relevant — not an exhaustive checklist, and none of these alone makes it mandatory:

- authentication
- authorization
- sessions
- sensitive data
- user-controlled input
- APIs
- file handling
- external integrations
- privileged actions
- secrets
- cryptographic behavior
- multi-tenancy
- security-sensitive state transitions

## Design concerns

Kept system-oriented, not a control catalog:

- trust boundaries
- identity and authorization boundaries
- input/output trust
- sensitive-data lifecycle
- state-transition security
- abuse paths
- external authority
- failure behavior
- auditability, where warranted

## Control guidance

Principles, not a prescribed stack:

- Make trust boundaries and authorization boundaries explicit in the design, not implicit in scattered checks.
- Treat input crossing a trust boundary as untrusted until validated; treat output crossing one as needing the receiving context's encoding/escaping.
- Fail closed on security-relevant paths — an error or an unhandled case should not default to granting access or exposing data.
- Scope privileged actions and secrets to the minimum authority needed (`core/EXECUTION.md` Authority).
- For security-sensitive mechanisms, prefer mature, maintained primitives over custom implementations (`core/EXECUTION.md` Mature primitives) — a custom mechanism needs justification proportional to its consequence.

## Verification guidance

Verification classes to consider, drawn from `core/VERIFICATION.md`'s verification classes — apply only where the applicability signals justify them, not all of them for every change:

- negative/abuse testing
- authorization-boundary testing
- replay/state-transition testing
- integration verification
- secret/sensitive-output inspection
- relevant static/security tooling, where justified

## Challenge method

Adversarial, per `core/VERIFICATION.md` Independent Challenge: attempt to violate the stated security requirements, cross trust boundaries, bypass controls, abuse state transitions, exploit unstated assumptions, and identify controls that exist only nominally (present in code but not actually enforced on the path that matters).

A specialized, runtime-level security-review implementation can satisfy or strengthen this challenge method when one is available to the session. That's an optional, implementation-level choice — not part of this capability's contract, and never a requirement to fetch or install one as part of applying MNM.

## Expected evidence

Evidence types, not a specific tool: passing negative/abuse tests, authorization-boundary test results, static-analysis findings and their disposition, a record of what was probed and what held, and — where independent challenge was warranted — its findings in `core/VERIFICATION.md`'s finding schema.

## Cross-domain note

This capability classifies and challenges application-security concerns; it does not own a separate copy of controls that other lenses also rely on. A control such as input validation or rate limiting may satisfy application security alongside reliability, API security or privacy at once — see `core/ASSURANCE.md` Cross-domain controls. Don't implement it twice because two lenses named it.
