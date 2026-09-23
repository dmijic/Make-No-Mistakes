# Capabilities

A capability is reusable engineering expertise applied through the generic capability contract defined in `core/ASSURANCE.md`: PURPOSE, APPLICABILITY SIGNALS, DESIGN CONCERNS, CONTROL GUIDANCE, VERIFICATION GUIDANCE, CHALLENGE METHOD, EXPECTED EVIDENCE.

A capability is **not** necessarily:

- a separate agent
- a runtime skill
- a checklist
- a standard
- a tool integration
- a mandatory review phase

It is domain expertise that MNM can apply when relevant, by whatever agent is doing the work.

## Layering

```text
MNM Core
    -> generic engineering protocol and assurance semantics (WHEN / WHY specialized assurance applies)

Capability
    -> reusable domain expertise (WHAT concerns to address)

Runtime adapter / specialist implementation
    -> maps a capability into a concrete runtime, skill, tool or specialist agent (HOW it's executed)

Project
    -> project-specific requirements, decisions, controls, findings, evidence
```

Core stays independent of any runtime, vendor, model or external standard. A capability document stays independent of any specific runtime, skill or tool. No runtime adapter or specialist implementation is built or required by this capability layer.

## Rules

- A capability must not duplicate Core rules. Where a capability's guidance is already stated in Core (mature primitives, independent challenge, evidence, cross-domain controls), it cross-references that section instead of restating it.
- A capability must not claim applicability merely because it exists. Applicability, control & verification depth, and independence remain three separate decisions, made per concern, per `core/ASSURANCE.md` Assurance Dimensions — not implied by a capability document's presence in this directory.

## Available capabilities

- [`application-security.md`](application-security.md) — application-security engineering expertise.
- [`genai-security.md`](genai-security.md) — engineering expertise for systems that use models or agentic AI.

Other assurance lenses recognized by `core/ASSURANCE.md` (architecture, privacy, performance, reliability, API security, database assurance, dependency/supply-chain, infrastructure/IaC, accessibility, and others) remain valid lenses to apply through engineering judgment. They don't get a capability document here until they're specified and tested the way these two were.
