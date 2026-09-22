---
name: software-project-workflow
description: "Apply the Make No Mistakes methodology to orchestrate software projects through explicit discovery, research, architecture, implementation, review, testing, and deployment phases."
---

# Software Project Workflow

Use the **Make No Mistakes** methodology for non-trivial software work.

The methodology's source of truth is the repository-level documentation. Read the relevant files before acting; do not assume their contents:

- `core/PRINCIPLES.md` — core principles
- `core/WORKFLOW.md` — Simple/Medium/Complex workflow modes and the persistent-project-memory model
- `guidance/workflow-patterns.md` — sequential/conditional/parallel phase patterns
- `guidance/git-baseline.md` — Git hygiene before baseline commits
- `templates/handoff.md` — phase handoff format
- `templates/review.md` — review checklist
- `guidance/external-capabilities.md` — pattern for using optional external capabilities (source control hosting, issue tracking, docs systems, CI/CD, infrastructure, APIs, communication, data sources)

## Operating rule

Choose the smallest workflow defined in `core/WORKFLOW.md` that safely covers the project's complexity.

Treat the repository, canonical documentation and Git history as persistent project memory. Treat chat sessions and agents as temporary working environments.

Verify important unknowns instead of guessing. Separate findings into `VERIFIED`, `PROPOSAL`, `OPEN`, and `TBD`.

Do not automatically commit, deploy, delete data, expose secrets or perform other consequential actions unless the user has explicitly delegated them.
