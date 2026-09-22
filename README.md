# Make No Mistakes.

**A structured software development workflow for AI coding agents.**

*Because "make no mistakes" is not a development methodology.*

AI coding agents can write a lot of code very quickly.

Unfortunately, they can also write a lot of wrong code very quickly.

**Make No Mistakes** is an open-source workflow for running non-trivial software projects with AI agents through explicit discovery, research, specification, architecture, implementation, review, testing and deployment phases.

The goal is not to pretend an AI agent will make no mistakes. The goal is to structure the work so mistakes, unsupported assumptions and architectural drift are easier to detect, review and correct.

## Workflow modes

```text
SIMPLE
Requirements -> Implementation -> Review -> Commit

MEDIUM
Research -> Specification/Architecture -> Baseline
-> Implementation -> Review -> Commit

COMPLEX
Discovery -> Research/Probes -> Specification -> Architecture
-> Repository Cleanup/Baseline -> Implementation Passes
-> Review Loops -> Deployment/Hardening
```

The workflow is adaptive. Use the smallest process that safely covers the complexity of the project.

## The core idea

```text
Repository + Canonical Documentation + Git History
                        =
              Persistent Project Memory

Chat / Agent Session
        =
Temporary Working Environment
```

A new agent or session should be able to continue from the repository and canonical documentation without reconstructing the project from old chat history.

## Repository structure

```text
Make-No-Mistakes/
├── README.md
├── LICENSE
├── core/
│   ├── PRINCIPLES.md
│   └── WORKFLOW.md
├── guidance/
│   ├── git-baseline.md
│   ├── external-capabilities.md
│   └── workflow-patterns.md
├── templates/
│   ├── handoff.md
│   └── review.md
├── examples/
└── skills/
    └── software-project-workflow/
        ├── SKILL.md
        └── agents/
            └── openai.yaml
```

The repository contains the methodology. `skills/software-project-workflow` is an adapter for AI environments that support skills.

## Principles

- Verify important unknowns instead of guessing.
- Keep one canonical source of truth for requirements and architecture.
- Separate verified facts from proposals, open decisions and TBD items.
- Use stable Git commits as reviewed phase boundaries.
- Split large implementations into controlled passes.
- Review before advancing.
- Keep secrets and raw sensitive outputs out of Git.
- Separate development, test/demo and production concerns.
- Do not confuse generated code with validated software.

## Using it

Clone or download the repository and give it to your AI coding environment as project guidance. If the environment supports skills, use the `skills/software-project-workflow` adapter.

## License

MIT. See [LICENSE](LICENSE).
