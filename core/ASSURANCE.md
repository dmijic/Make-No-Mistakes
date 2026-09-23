# Assurance

Assurance is system-first. Do not design software as a set of independent checklists for security, privacy, architecture, performance, reliability, etc. Instead, design one coherent system, then challenge it through specialized lenses:

```text
SYSTEM / CHANGE
    -> SYSTEM CONCERNS
    -> REQUIREMENTS / INVARIANTS
    -> CONTROLS
    -> COHERENT DESIGN
    -> IMPLEMENTATION
    -> VERIFICATION
```

## Assurance lenses

Potential lenses, applied only where relevant: architecture, application security, API security, GenAI/LLM security, dependency/supply-chain, infrastructure/IaC, database/data, privacy, accessibility, performance, reliability/operations.

Core does not encode detailed category lists (e.g. OWASP categories) for these lenses. That belongs in capabilities, not Core.

## Capability contract

Core defines only the generic interface a capability fills. A capability may define:

- **PURPOSE**
- **APPLICABILITY SIGNALS**
- **DESIGN CONCERNS**
- **CONTROL GUIDANCE**
- **VERIFICATION GUIDANCE**
- **CHALLENGE METHOD**
- **EXPECTED EVIDENCE**

A capability does not imply a separate agent, a separate skill, a mandatory review, or a mandatory document. It is engineering expertise MNM applies when relevant, by whatever agent is doing the work (`core/EXECUTION.md` agent capability model).

## Assurance dimensions

For a relevant concern, determine these separately — do not collapse them into one severity/depth label:

1. **Applicability** — is the concern relevant to this system or change at all?
2. **Control & verification depth** — how much is warranted, proportional to consequence (`core/WORKFLOW.md` adaptive depth)?
3. **Independence** — does this work warrant independent, specialized challenge (`core/VERIFICATION.md`)?

## Cross-domain controls

Assurance lenses classify concerns; they do not own duplicate implementations. One coherent control can satisfy several concerns at once — e.g. rate limiting can address security, reliability, performance and cost control together. Avoid checklist-driven duplication of the same control under multiple labels.

## Definition of done

Completion may require, according to applicability:

- required behavior satisfied
- required controls implemented
- relevant existing contracts preserved (`core/EXECUTION.md` change safety)
- required verification performed, with evidence (`core/VERIFICATION.md`)
- required challenge completed, where warranted
- blocking findings resolved
- residual risks and known limitations made explicit
- durable state updated (`core/STATE.md`)

If required verification has not occurred, the state is UNVERIFIED — not "probably correct."
