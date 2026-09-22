---
name: software-project-workflow
description: "Apply the Make No Mistakes (MNM) protocol in ChatGPT: understand intent, research and identify blocking unknowns, make consequential decisions explicit, design and specify, and prepare execution-ready state before handing off implementation."
---

# Software Project Workflow (ChatGPT)

ChatGPT is a **design-oriented** MNM runtime by default: discovery, requirements, research, architecture and specification are its typical strength here. This is a default emphasis, not a restriction — see `adapters/README.md`. You can still inspect implementation, review a diff, apply verification and assurance reasoning, or independently challenge a claim when that's what the conversation needs.

## Canonical source

This skill is a thin entry point, not a copy of MNM. Use whatever access this conversation has to MNM's `core/`, `guidance/`, `templates/` and `capabilities/` directories — a connected repository, uploaded files, or supporting resources bundled with an installed version of this skill. If none of MNM's canonical material is actually available to you, say so plainly and work from what the person tells you, rather than inventing or restating the protocol from memory.

The canonical material:

- `core/PRINCIPLES.md`, `core/WORKFLOW.md`, `core/STATE.md`, `core/EXECUTION.md`, `core/VERIFICATION.md`, `core/ASSURANCE.md` — the full Core protocol
- `guidance/` — optional practical guidance
- `templates/` — optional artifacts (`handoff.md`, `review.md`)
- `capabilities/` — reusable domain expertise

## How the loop lands here

This is the same adaptive loop `core/WORKFLOW.md` defines, viewed from a design-oriented entry point:

```text
UNDERSTAND
    -> INSPECT / RESEARCH
    -> REQUIRE
    -> IDENTIFY BLOCKING UNKNOWNS
    -> DECIDE
    -> DESIGN
    -> CONTROL
    -> SPECIFY
    -> PREPARE EXECUTION CONTRACT
    -> PERSIST / HANDOFF
```

Inspect before asking a question that's already answerable from available project state (`core/PRINCIPLES.md` invariant 2). Distinguish unknowns that block the current objective from ones that don't (`core/STATE.md` knowledge state). Make consequential decisions explicit rather than letting them emerge implicitly in conversation (`core/PRINCIPLES.md` invariant 6).

## Handing off to execution

Aim conversations that will lead to implementation toward outputs an execution-oriented runtime can continue from without reconstructing this conversation: objective, verified baseline, requirements, scope, consequential decisions, design, critical invariants, controls, acceptance criteria, assurance expectations, required verification, authority boundary, and any unresolved blocking state — only the fields this task actually needs, using `core/EXECUTION.md`'s execution contract and `templates/handoff.md` where the work warrants writing one down. A SIMPLE task may need almost none of this explicitly.

## Chat is temporary, the project is durable

This conversation is a temporary working environment; the repository and its canonical project state are persistent project memory (`core/STATE.md`). Don't rely on chat continuity to carry forward anything consequential — persist it into the project instead.
