# Verification

Generated output or agent confidence does not establish completion (`core/PRINCIPLES.md` invariant 9). Verification is required according to the bounded objective — not as a fixed checklist applied uniformly regardless of consequence.

## Verification classes

Available classes, to be used only where justified by the task: static, unit/behavior, integration, negative/abuse, concurrency/state, security, runtime, performance, accessibility, recovery, diff, requirement trace, manual/expert.

A SIMPLE, low-consequence change may need only diff review and a targeted test. A COMPLEX, high-consequence change may need several classes layered together (`core/WORKFLOW.md` profiles).

## Verification results

- **PASS**
- **FAILED**
- **NOT RUN**
- **MANUAL CHECK REQUIRED**
- **UNVERIFIED**

**PASS requires evidence.** Plausible output, generated code, or confidence is never sufficient to mark PASS. Where required verification has not occurred, use UNVERIFIED — not "probably correct."

## Evidence

Distinguish two concepts that both use the word "evidence":

- **Verification evidence** — evidence supporting an engineering claim: tests, benchmarks, runtime observations, reviews.
- **Domain evidence** — evidence managed by the application itself, e.g. a security scanner's raw output.

## Independent challenge

Independent challenge attempts to falsify important engineering claims, not merely confirm them. It is required only when consequence or risk warrants it (`core/PRINCIPLES.md` invariant 10) — a SIMPLE change does not require a formal review phase or an independent reviewer.

When challenge is warranted, scope the reviewer's context to what's needed: requirements, relevant decisions, relevant design, the implementation/diff, existing verification evidence, relevant risk context. Do not supply the worker's entire reasoning transcript merely to preserve continuity. Independent review should be context-isolated where practical (`core/EXECUTION.md` agent capability model).

## Findings and escape analysis

A meaningful finding captures: problem, consequence/severity, evidence, affected surface, violated requirement or control (when applicable), remediation, verification state.

Finding provenance:

- **INTRODUCED_BY_CHANGE**
- **EXPOSED_BY_CHANGE**
- **PRE_EXISTING**
- **UNKNOWN**

A significant finding should trigger escape analysis: where should this defect have been prevented? Possible layers: requirement, decision, design, control, implementation, verification, context, applicability, review.

Do not automatically turn every project defect into a new MNM Core rule. Promote a finding into Core only when it reveals a reusable methodology or process failure. Domain-specific lessons belong in capabilities. Project-specific lessons belong in the project.
