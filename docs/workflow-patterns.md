# Workflow patterns

## Sequential

Use when the output of one phase is a prerequisite for the next:

`Research -> Specification -> Architecture -> Baseline -> Implementation -> Review`

## Conditional

Insert a phase only when evidence requires it:

`Inspect -> Is empirical research needed? -> yes: Probe -> no: continue`

`Implementation -> Deployment target known? -> yes: package -> no: document TBD`

## Parallel, then merge

Use separate streams only when they are genuinely independent:

```text
Design review ----\
                   -> baseline -> implementation
Integration probe -/
```

Merge only through canonical docs/review, not informal chat.
