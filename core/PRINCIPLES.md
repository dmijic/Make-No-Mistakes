# Principles

Make No Mistakes is a structured software-development methodology for working with AI coding agents.

## Core principles

1. **Use the smallest safe workflow.** Process should match project complexity.
2. **Verify important unknowns.** Probe APIs, integrations and constraints instead of guessing.
3. **Keep durable project memory outside chat.** Repository, canonical documentation and Git history are persistent memory.
4. **Treat agent sessions as temporary.** A new session should be able to continue from the repository and canonical docs.
5. **Separate facts from assumptions.** Mark findings as VERIFIED, PROPOSAL, OPEN or TBD.
6. **Create explicit phase boundaries.** Research, specification, architecture, implementation, review, testing and deployment should not blur together on non-trivial projects.
7. **Review before advancing.** Stable Git commits should represent reviewed project states.
8. **Do not confuse generated code with validated software.** Implementation is not completion.
9. **Protect secrets and production.** Keep credentials, raw secret-bearing outputs and unsafe production actions outside normal implementation flow.
10. **Make mistakes observable and recoverable.** The goal is not to pretend AI will make no mistakes. The workflow exists to catch them early.
