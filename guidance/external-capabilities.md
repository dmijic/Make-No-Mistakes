# External capabilities

Optional practical guidance for applying MNM Core when a session has access to external systems. It does not override Core.

The repository and its durable state (`core/STATE.md`) remain canonical. External systems are optional capabilities a session may or may not have access to — never a mandatory workflow responsibility.

## Categories

- **Source control hosting** — remote repository state, branches, pull/merge requests, commit/push history (the local Git repository remains canonical for code state; hosting is where it happens to live)
- **Issue/work management** — requirements, acceptance criteria, work-item status
- **Documentation/knowledge systems** — canonical or supporting docs kept outside the repository
- **CI/CD** — build, test and pipeline status
- **Infrastructure/deployment** — environments, deployment targets, hosting/cloud consoles
- **External APIs/services** — third-party integrations the project depends on
- **Communication systems** — channels used to notify people or request approval
- **Databases/data sources** — data the project reads from or writes to

No category is required. Use whichever are actually available and relevant to the bounded objective (`core/PRINCIPLES.md` invariant 3, minimum sufficient context). The capability category and its verified authority boundary matter, not the specific product providing it.

## Pattern

```text
discover / inspect capability
  -> determine source of authority
  -> determine read/write boundary
  -> perform the minimum required action
  -> verify the result
  -> persist durable conclusions, when appropriate
```

## Authority and evidence

- Apply bounded authority (`core/EXECUTION.md`): inspect a capability's actual configuration before acting on it, do not invent fields, states or capabilities that were not verified.
- Prefer read access over write access; confirm the read/write boundary before writing.
- Do not perform destructive or consequential external actions without the authority that action requires.
- Do not expose secrets or raw sensitive outputs.
- Verify external writes where practical, and treat the result as verification evidence (`core/VERIFICATION.md`) — persist durable conclusions into project state (`core/STATE.md`), not just into the session.
