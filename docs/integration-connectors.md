# Optional integration connectors

Connectors are optional capabilities, not mandatory workflow stages.

## GitLab

Use GitLab integration when available for:

- repository inspection
- branches/tags
- commits and push history
- merge requests
- issues where appropriate
- implementation/review status

Keep the repository on disk and Git as the canonical source of code state. Use connector data to inspect or manage remote state, not to replace the repository.

## Jira

Use Jira integration when available for:

- project/issue discovery
- linking requirements to implementation work
- reading acceptance criteria
- updating issue status when explicitly requested
- referencing issue IDs in implementation handoffs

Do not invent Jira issue fields or workflow states. Inspect the connected project's actual configuration first.

## Other systems

Apply the same pattern to Confluence, SharePoint, Teams, CI/CD, cloud consoles, or other connected systems: verify capabilities first, respect source/target boundaries, and record durable conclusions in project documentation.
