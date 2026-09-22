# External capabilities

The repository, canonical documentation and Git history are the durable source of truth. External systems are optional capabilities a session may or may not have access to — not mandatory workflow phases.

## Categories

- **Source control hosting** — remote repository state, branches, pull/merge requests, commit/push history (the local Git repository remains canonical for code state; hosting is where it happens to live)
- **Issue/work management** — requirements, acceptance criteria, work-item status
- **Documentation/knowledge systems** — canonical or supporting docs kept outside the repository
- **CI/CD** — build, test and pipeline status
- **Infrastructure/deployment** — environments, deployment targets, hosting/cloud consoles
- **External APIs/services** — third-party integrations the project depends on
- **Communication systems** — channels used to notify people or request approval
- **Databases/data sources** — data the project reads from or writes to

None of these categories is required. Use whichever are actually available and relevant to the task. The capability category and its verified boundaries matter, not the specific product providing it.

## Pattern

```text
discover / inspect capability
  -> determine source of authority
  -> determine read/write boundary
  -> perform the minimum required action
  -> verify the result
  -> persist durable conclusions in project documentation, when appropriate
```

## Authority and safety

- Keep the local repository and Git history canonical for code state; use external systems to inspect or manage remote/related state, not to replace it.
- Inspect a capability's actual configuration before acting on it. Do not invent fields, states or capabilities that were not verified.
- Prefer read access over write access; confirm read/write boundaries before writing.
- Do not perform destructive or consequential external actions without explicit authorization.
- Do not expose secrets or raw sensitive outputs.
- Verify external writes where practical.
