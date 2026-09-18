---
name: software-project-workflow
description: "Apply the Make No Mistakes methodology to orchestrate software projects through explicit discovery, research, architecture, implementation, review, testing, and deployment phases."
---

# Software Project Workflow

Use the **Make No Mistakes** methodology for non-trivial software work.

The methodology's source of truth is the repository-level documentation:

- `core/PRINCIPLES.md`
- `core/WORKFLOW.md`
- `docs/workflow-patterns.md`
- `docs/git-baseline.md`
- `docs/handoff-template.md`
- `docs/review-template.md`
- `docs/integration-connectors.md`

## Operating rule

Choose the smallest workflow that safely covers the project's complexity.

### Simple
`Requirements -> Implementation -> Review -> Commit`

### Medium
`Research -> Specification/Architecture -> Baseline -> Implementation -> Review -> Commit`

### Complex
`Discovery -> Research/Probes -> Specification -> Architecture -> Repository Cleanup/Baseline -> Implementation Passes -> Review Loops -> Deployment/Hardening`

Treat the repository, canonical documentation and Git history as persistent project memory. Treat chat sessions and agents as temporary working environments.

Verify important unknowns instead of guessing. Separate findings into `VERIFIED`, `PROPOSAL`, `OPEN`, and `TBD`.

Do not automatically commit, deploy, delete data, expose secrets or perform other consequential actions unless the user has explicitly delegated them.
