# GenAI / LLM Security

Fills the generic capability contract in `core/ASSURANCE.md` for systems that use models or agentic AI. This document defines MNM's own reusable engineering concerns for such systems — it does not reproduce an external standard's categories or descriptions.

## Purpose

Help identify, prevent, verify and challenge the security and trust risks specific to software where a model or agent participates in the system — not only at the end of a project.

## Applicability signals

Signals that this capability is likely relevant — not an exhaustive checklist:

- model input derived from untrusted users or external content
- retrieval/RAG
- tool use
- agent actions
- external-system writes
- model-generated decisions
- sensitive context
- model output consumed by executable or privileged systems
- model-generated security claims
- multi-tenant model context
- prompt/system-instruction boundaries

## Design concerns

- instructions vs. untrusted data
- prompt-injection boundaries
- tool/agent authority
- model-output trust
- deterministic facts vs. model interpretation
- sensitive-context exposure
- retrieval trust/provenance
- downstream-action validation
- human-approval boundaries, where consequential
- model/provider boundary
- auditability and provenance, where warranted

**AI interpretation must not silently become authoritative deterministic fact.** Model output must be assigned an explicit trust role appropriate to the system it's used in — treated as a claim to verify, not a fact to act on, unless the system deliberately grants it that authority. Content a model consumes as evidence or external input is treated as untrusted data even when it is an authoritative *stored* artifact elsewhere in the system: authoritative storage does not make content trusted the moment a model reads it and turns it into text.

## Control guidance

Architectural and technology-neutral:

- Keep instructions and untrusted data separated wherever the runtime allows it, and don't let content from an untrusted source silently gain instruction-level authority.
- Bound what tools/actions an agent can invoke, and scope that authority to the task (`core/EXECUTION.md` Authority) — don't grant broad authority because it's convenient.
- Validate model output before it drives a privileged or downstream action; don't let a model's claim substitute for the system's own verification of a consequential fact.
- Keep a human-approval boundary in front of sufficiently consequential agent actions.
- Preserve provenance from source content through retrieval/interpretation to the point it's used, where that traceability is warranted by consequence.

## Verification guidance

Adversarial testing to consider — only where applicable, drawn from `core/VERIFICATION.md`'s verification classes:

- prompt-injection attempts
- malicious retrieved/external content
- tool-authority boundary testing
- unsafe downstream-action attempts
- sensitive-context leakage attempts
- malformed/adversarial model output
- provenance/traceability checks

## Challenge method

Adversarial, per `core/VERIFICATION.md` Independent Challenge: attempt to make the model or agent cross its intended trust or authority boundary — inject instructions through untrusted content, push it to take an action or disclose context outside its granted authority, and see whether the system's own controls catch it rather than relying on the model to refuse.

A specialized, runtime-level security-review implementation can satisfy or strengthen this challenge method when one is available to the session. That's an optional, implementation-level choice — not part of this capability's contract, and never a requirement to fetch or install one as part of applying MNM.

## Expected evidence

Evidence types, not a specific tool: results of injection/adversarial-input attempts, tool-authority boundary test results, a record of what downstream actions were attempted and what was blocked or allowed, and — where independent challenge was warranted — its findings in `core/VERIFICATION.md`'s finding schema.

## Cross-domain note

This capability classifies and challenges GenAI/agentic concerns; it does not own a separate copy of controls that other lenses also rely on. A tool-authority boundary or output-validation control may satisfy GenAI security alongside application security, privacy or reliability at once — see `core/ASSURANCE.md` Cross-domain controls. Don't implement it twice because two lenses named it.
