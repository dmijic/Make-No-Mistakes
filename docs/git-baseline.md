# Git baseline hygiene

Before a baseline commit:

```text
git status
git diff --check
git diff --stat
git diff --cached --check
```

Check that secrets and generated outputs are ignored.

After staging, review the status before committing. Prefer meaningful commits that mark stable phase boundaries.

Do not commit automatically unless the user explicitly delegates that action.
