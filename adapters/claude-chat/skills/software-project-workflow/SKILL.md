---
name: software-project-workflow
description: "Apply the Make No Mistakes (MNM) protocol in Claude: understand what's actually being asked, inspect available project state before asking questions, surface consequential decisions explicitly, design and specify, and leave behind state an execution-oriented session can pick up without replaying this conversation."
---

# Software Project Workflow (Claude Chat)

Claude in claude.ai is a **design-oriented** MNM runtime by default: it's well suited to discovery, requirements, research, architecture and specification work. This is a default emphasis, not a restriction. Nothing here stops you from inspecting an implementation, reviewing a diff, reasoning through verification and assurance, or independently challenging a claim when the conversation calls for it.

## Canonical source

This skill is a thin entry point, not a copy of MNM. Draw on whatever access you have to MNM's `core/`, `guidance/`, `templates/` and `capabilities/` directories in this context — Project knowledge files, a connected source, or supporting resources bundled with an installed version of this skill. If none of that material is actually reachable, say so and work from what the person gives you, rather than reconstructing the protocol from memory.

The canonical material:

- `core/PRINCIPLES.md`, `core/WORKFLOW.md`, `core/STATE.md`, `core/EXECUTION.md`, `core/VERIFICATION.md`, `core/ASSURANCE.md` — the full Core protocol
- `guidance/` — optional practical guidance
- `templates/` — optional artifacts (`handoff.md`, `review.md`)
- `capabilities/` — reusable domain expertise

## Same loop, entered from design

`core/WORKFLOW.md` defines one adaptive loop. From here, it typically enters like this:

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

Check what's already knowable from the project before asking the person to repeat it (`core/PRINCIPLES.md` invariant 2). Keep track of which open questions actually block the current objective and which don't (`core/STATE.md` knowledge state). When a choice would materially affect architecture, security, privacy, compatibility, data integrity or operations, name it as a decision rather than letting it slide in as an implementation detail (`core/PRINCIPLES.md` invariant 6).

## Setting up execution to succeed

When a conversation is headed toward implementation, steer it toward something an execution-oriented session can act on without reconstructing this discussion: the objective, a verified baseline, requirements, what's in and out of scope, the decisions made, the design, any critical invariants, controls, acceptance criteria, assurance expectations, required verification, and the authority boundary — whichever of those the task actually needs (`core/EXECUTION.md` execution contract), written down with `templates/handoff.md` only when it's worth writing down. Most SIMPLE tasks won't need this at all.

## The project outlives the chat

Treat this conversation as disposable working memory. The repository and its canonical project state are what persists (`core/STATE.md`); if it matters later, it belongs there, not in this thread.
