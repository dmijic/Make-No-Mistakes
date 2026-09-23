# Review template

Optional. Use only when the work's consequence or risk warrants independent challenge (`core/PRINCIPLES.md` invariant 10, `core/VERIFICATION.md`). A SIMPLE change does not require this template, a formal review phase, or an independent reviewer.

This is an adversarial challenge, not a confirmation checklist: the goal is to attempt to falsify the claims made about the work, not to rubber-stamp them.

## Reviewer context (bounded — see core/VERIFICATION.md)

Provide only what's needed to challenge this specific work, not the worker's full reasoning transcript:

- objective / requirements
- relevant consequential decisions
- relevant architecture / design
- implementation or diff
- existing verification evidence
- relevant risk context

## Challenge targets

- **Correctness claims** — does the evidence actually support what's claimed, or only what's plausible?
- **Preserved contracts** — was anything in `core/EXECUTION.md` change safety (API/schema/events/config/user-visible behavior/data semantics/deployment/external integrations) altered without an explicit requirement to do so?
- **Relevant controls** — do the implemented controls actually address the applicable concerns (`core/ASSURANCE.md`), or only the obvious ones?
- **Verification adequacy** — is PASS backed by evidence (`core/VERIFICATION.md`), or asserted? Are the right verification classes engaged for this consequence level?
- **Consequential assumptions** — were any ASSUMPTION-state items (`core/STATE.md`) treated as VERIFIED without justification?
- **Scope boundaries** — did the work stay within its stated scope, or drift into an undeclared consequential decision?
- **Residual risks** — what's left unaddressed, and is that acceptable given the consequence of this work?

## Findings

Capture each finding using Core's finding schema (`core/VERIFICATION.md`):

```markdown
## Finding: <short title>
- Problem:
- Consequence / severity:
- Evidence:
- Affected surface:
- Violated requirement / control (if applicable):
- Remediation:
- Verification state: PASS | FAILED | NOT RUN | MANUAL CHECK REQUIRED | UNVERIFIED
- Provenance: INTRODUCED_BY_CHANGE | EXPOSED_BY_CHANGE | PRE_EXISTING | UNKNOWN
```

Do not encode domain-specific security checklists (e.g. OWASP categories) here — that belongs to specialized capabilities, not this generic template.
