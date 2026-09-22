# Workflow patterns

Optional practical patterns for composing the adaptive loop in `core/WORKFLOW.md` across a larger project. It does not override Core.

## Sequential

Use when the output of one responsibility is a prerequisite for the next:

`INSPECT -> REQUIRE -> DECIDE -> DESIGN -> IMPLEMENT -> VERIFY`

## Conditional

Engage a responsibility only when evidence requires it:

`INSPECT -> is empirical research needed? -> yes: investigate further -> no: continue`

`IMPLEMENT -> deployment target known? -> yes: package -> no: record as TBD (core/STATE.md)`

## Parallel, then merge

Split into separate streams only when doing so provides a real benefit: independent work streams, context isolation, specialized capability, or independent verification (`core/EXECUTION.md` agent capability model). Parallel work is not inherently faster or better.

```text
Design review ----\
                   -> baseline -> implementation
Integration probe -/
```

Do not parallelize implementation until shared contracts and ownership boundaries are sufficiently stable (`core/EXECUTION.md` change safety) — parallelizing against a moving contract creates rework, not speed.

Merge only through durable project state and verification evidence (`core/STATE.md`, `core/VERIFICATION.md`), not through assumed shared chat or session context. A parallel stream's conclusions must be recoverable by a session that didn't participate in producing them.
