# Changelog

## 1.1.0 - Tech-agnostic skill cleanup

- Replaced product-specific integration guidance (GitLab, Jira, Confluence, SharePoint, Teams) with a generic external-capabilities model organized by category (source control hosting, issue/work management, documentation/knowledge systems, CI/CD, infrastructure/deployment, external APIs/services, communication systems, databases/data sources), plus a generic discover/verify/persist pattern. Renamed `docs/integration-connectors.md` to `docs/external-capabilities.md`.
- Trimmed `skills/software-project-workflow/SKILL.md` to a thin adapter that points to `core/` and `docs/` as canonical sources instead of duplicating the Simple/Medium/Complex workflow diagrams.

## 0.1.0 - Initial public draft

- Added Make No Mistakes project structure.
- Separated core methodology from the AI skill adapter.
- Added Simple, Medium and Complex workflow modes.
- Added project-level workflow, review, handoff, integration and Git baseline guidance.
