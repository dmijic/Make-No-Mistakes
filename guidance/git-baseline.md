# Git baseline hygiene

Optional practical guidance for applying `core/STATE.md` and `core/EXECUTION.md` to Git. It does not override Core; use only what a given change warrants.

## Safety checks

Before a commit meant to represent a durable, reviewable state:

```text
git status
git diff --check
git diff --stat
git diff --cached --check
```

Check that secrets and generated outputs are excluded. Review the staged status before committing.

## Commits as durable state, not mandatory boundaries

Stable Git commits are a useful durable, reviewable boundary — one form of the durable state described in `core/STATE.md`. They are not a mandatory phase gate: the adaptive loop in `core/WORKFLOW.md` does not require a commit for every responsibility, and a SIMPLE change may reach COMPLETE in a single commit or none beyond the working change itself.

Prefer commits that mark a meaningful, verified state over commits that exist merely to close a ceremony step.

## Authority

Commits, pushes, deployments and destructive operations (`git reset --hard`, force-push, history rewrites, branch deletion) require the authority appropriate to that action — see `core/EXECUTION.md` Authority. Do not perform them automatically without that authorization.
