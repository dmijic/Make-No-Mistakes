# Runtime adapters

An MNM runtime adapter is a thin runtime-specific entry point that maps a runtime's own capabilities and conventions onto the canonical MNM protocol. Canonical methodology lives in `core/`, `guidance/`, `templates/` and `capabilities/`; adapters reference that material, they don't contain it.

## Invariants

1. An adapter is a thin runtime-specific entry point that maps the runtime's capabilities and conventions onto the canonical MNM protocol.
2. Runtime differences may change how MNM is executed, but must not change what MNM means.
3. All adapters have access to the complete MNM protocol — none is a reduced or partial version.
4. Responsibility orientation (design-oriented vs. execution-oriented) is a default emphasis, not a hard capability wall.
5. Adapters do not own copies of Core — no adapter directory contains a duplicate of `core/`, `guidance/`, `templates/` or `capabilities/` content.
6. Source adapters and installable runtime packages are different artifacts. What's here is source; self-contained, installable packages are a later, separate concern.
7. Project repositories should contain project-specific durable state, not a vendored copy of MNM Core merely to make the protocol available.
8. Runtime-specific behavior belongs in adapters; reusable engineering expertise belongs in `capabilities/`; generic methodology belongs in `core/`.

## Adapters

| Runtime | Orientation | Entry point |
|---|---|---|
| [`chatgpt/`](chatgpt/) | Design-oriented | ChatGPT Skill (Agent Skills format) |
| [`claude-chat/`](claude-chat/) | Design-oriented | Claude.ai Skill (Agent Skills format) |
| [`codex/`](codex/) | Execution-oriented | `AGENTS.md` |
| [`claude-code/`](claude-code/) | Execution-oriented | Claude Code Skill (Agent Skills format) |

Design-oriented and execution-oriented are defaults, not restrictions: a design-oriented runtime may still inspect implementation, review a diff, apply verification and assurance, or independently challenge a claim; an execution-oriented runtime may still identify an invalid requirement, a broken architectural assumption, or a missing consequential decision — and must escalate rather than silently redesign consequential behavior either way. See each adapter's own README and entry point for its specific emphasis.

Three of the four converge on the same open Agent Skills `SKILL.md` format (a directory with `SKILL.md` — YAML frontmatter plus markdown instructions); Codex uses its own persistent, always-loaded `AGENTS.md` layer instead, since MNM there is closer to an ambient operating manual than a single triggered procedure.
