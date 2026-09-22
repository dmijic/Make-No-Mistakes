---
name: software-project-workflow
description: "Apply the Make No Mistakes (MNM) protocol in Codex: recover durable project state, inspect the repository, implement bounded changes, verify with evidence, and escalate rather than silently redesign consequential behavior."
---

# Software Project Workflow (Codex)

Codex is an **execution-oriented** MNM runtime by default: it operates directly on a repository. This is a default emphasis, not a restriction — see `adapters/README.md`.

## Canonical source

This skill is a thin entry point, not a copy of MNM. It assumes the MNM installation's `core/`, `guidance/`, `templates/` and `capabilities/` directories are available alongside it (in this repository, at the repository root; in an installed project, wherever MNM was placed — self-contained packaging is a later concern, see `adapters/README.md` invariant 6). If you can't locate them, say so and ask where the MNM installation lives before proceeding — don't invent or restate the protocol from memory.

Read the relevant canonical files before acting; do not assume their contents:

- `core/PRINCIPLES.md`, `core/WORKFLOW.md`, `core/STATE.md`, `core/EXECUTION.md`, `core/VERIFICATION.md`, `core/ASSURANCE.md` — the full Core protocol
- `guidance/` — optional practical guidance
- `templates/` — optional artifacts (`handoff.md`, `review.md`)
- `capabilities/` — reusable domain expertise

## How the loop lands here

This is the same adaptive loop `core/WORKFLOW.md` defines, viewed from an execution-oriented entry point:

```text
RECOVER DURABLE STATE
    -> INSPECT CURRENT REPOSITORY REALITY
    -> COMPARE REALITY WITH THE BOUNDED OBJECTIVE / EXECUTION CONTRACT
    -> RESOLVE OR ESCALATE BLOCKERS
    -> IMPLEMENT BOUNDED UNIT
    -> VERIFY
    -> CHALLENGE WHEN WARRANTED
    -> PERSIST STATE + EVIDENCE
```

Preserve, throughout: inspect before ask, minimum sufficient context, bounded authority, change safety, testable requirements, the requirement → design/control → implementation → verification → evidence trace, state-transition/concurrency/replay reasoning when relevant, proportional assurance, and evidence-backed completion (`core/PRINCIPLES.md`, `core/EXECUTION.md`, `core/VERIFICATION.md`).

Execution orientation is a default, not a wall: you may still identify an invalid requirement, discover a broken architectural assumption, or spot a missing consequential decision — reason about design enough to implement safely, but escalate rather than silently redesign consequential project behavior (`core/EXECUTION.md` Escalation).

## Agent capability model

Use SCOUT / WORKER / REVIEWER / SPECIALIST from `core/EXECUTION.md` proportionally. Default to one capable agent. Use a subagent only when it provides real value — context isolation, genuinely independent parallel work, specialized capability, or independent verification — never as the default. Don't parallelize implementation until shared contracts and ownership boundaries are stable.

## Durable state, not project instruction bloat

The repository, its canonical documentation and its Git history are persistent project memory; this session is a temporary working environment (`core/STATE.md`). If the project has its own `AGENTS.md`, treat it as optional project/runtime context MNM consumes alongside the repository — it is not the MNM installation and does not need to contain MNM's methodology; that lives in the canonical directories referenced above. Persist consequential state (decisions, invariants, verification evidence) where it belongs in the project. Use `templates/handoff.md` when a bounded objective genuinely needs to cross a session boundary; a SIMPLE task usually doesn't.

## Ceremony stays proportional

Choose the smallest MNM workflow profile that safely covers the task (`core/WORKFLOW.md`). Independent challenge, formal review, and multi-agent execution are not required by default — apply them when the work's consequence or risk warrants it, not as standing ceremony.
