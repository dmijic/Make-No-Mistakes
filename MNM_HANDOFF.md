# MNM Development Handoff

## Current State
- Branch: `v2/core-protocol`
- HEAD: will be the commit created by this handoff (see commit SHA reported after push)
- Current phase: v2 Phase 6 — Dogfood (in progress). DOGFOOD-00 finding fixed in source; **runtime re-test not yet performed**.
- Status: Phases 1–5 remain ACCEPTED. VERSION unchanged at `2.0.0-dev` (dogfood correction, not a release event). DOGFOOD-01 has not begun.

## DOGFOOD-00 — Product Identity

- **ID:** DOGFOOD-00
- **Phase:** 6 — Dogfood
- **Runtime:** ChatGPT
- **MNM version:** 2.0.0-dev
- **Observed:** During the first real ChatGPT installation, before DOGFOOD-01 began, the installed Skill exposed legacy "Software Project Workflow (ChatGPT)" identity — frontmatter `name: software-project-workflow` and a `# Software Project Workflow (ChatGPT)` heading — instead of the intended public product identity.
- **Expected:** Installed product identity is "Make No Mistakes" (machine identifier `make-no-mistakes`), uniformly across all four runtime packages. Runtime remains an orientation/implementation detail inside the adapter, not a separate product identity.
- **Classification:** Adapter / Product Identity
- **Severity:** Low
- **Core defect:** No
- **Packaging defect:** No
- **Adapter defect:** Yes
- **Remediation:** Standardized Skill identity across all four runtime adapters (frontmatter `name:` and top-level heading), and strengthened the packaging validator to enforce the canonical machine identifier on every source and packaged Skill, so this class of drift can't silently reappear.
- **Verification performed:** Rebuilt all four packages; confirmed via direct inspection that every generated `SKILL.md` now has `name: make-no-mistakes` and `# Make No Mistakes`; confirmed design/execution orientation content is unchanged; confirmed package root remains `make-no-mistakes/`; `git diff --check` clean; full diff reviewed — exactly the identity strings changed, nothing else.
- **Status:** **FIXED PENDING RUNTIME RE-TEST.** The fix is verified in source and in the build output. It is *not* yet verified against the actual runtime: the rebuilt ChatGPT package has not yet been reinstalled in ChatGPT and observed by the user. Do not treat this as PASS until that reinstall/observation happens.
- **Next action:** Rebuild (already done, see below) → reinstall the ChatGPT package (`dist/chatgpt/make-no-mistakes.zip` or the `dist/chatgpt/make-no-mistakes/` directory) → user confirms the displayed identity now reads "Make No Mistakes" → only then resume toward DOGFOOD-01. DOGFOOD-01 has not started.

## What Changed (this round)

- All four `adapters/*/skills/software-project-workflow/SKILL.md`: frontmatter `name: software-project-workflow` → `name: make-no-mistakes`; top-level heading `# Software Project Workflow (<Runtime>)` → `# Make No Mistakes`. Descriptions left unchanged — they're runtime-specific activation metadata and were already good activation signals, per explicit instruction not to mechanically genericize them. Orientation content (design-oriented for chatgpt/claude-chat, execution-oriented for codex/claude-code) and all other body text left unchanged.
- `scripts/build-packages.py`: `check_frontmatter()` now validates that `name:` is present *and* equals the canonical machine identifier `make-no-mistakes` (was: only checked that some `name:`/`description:` keys existed). Still no YAML dependency — same lightweight regex-based frontmatter check as before, just stricter on the value. Applies to both source adapter files (`validate_source`) and packaged output (`validate_package`), so drift is caught at both points.
- No change to Core, `guidance/`, `templates/`, `capabilities/`, `VERSION`, or any adapter README.

## Source Directory Name — Determination

The task asked me to determine, not assume, whether `skills/software-project-workflow/` (the source subdirectory each adapter's `SKILL.md` lives under) has any user-visible or runtime-semantic effect, before deciding whether to leave it alone.

**Determination: no effect, left unchanged.** `scripts/build-packages.py`'s `build_package()` copies only the `SKILL.md` *file* into the package root (`shutil.copyfile(ADAPTERS[runtime], package_dir / "SKILL.md")`) — it never copies or references the source subdirectory's name. The generated, installed artifact is `make-no-mistakes/SKILL.md` in every case, regardless of what the source-tree folder was called. The installed Skill's identity is driven entirely by the frontmatter `name:` field (now fixed) and the package's own root directory name (already `make-no-mistakes/` since Phase 5) — never by the source repository's internal path. This is a verified property of the build script, not an assumption about runtime behavior, so no repository-wide rename was performed or needed.

## Build Result
`python3 scripts/build-packages.py` — exit 0, all four packages built and validated with the strengthened name check in effect.

## Verification
1. Build ran clean (exit 0) after the fix.
2. All four generated `SKILL.md` files confirmed to contain `name: make-no-mistakes` (`grep` across `dist/*/make-no-mistakes/SKILL.md`).
3. All four generated `SKILL.md` files confirmed to have the heading `# Make No Mistakes`.
4. Descriptions confirmed unchanged and still runtime-specific.
5. Design/execution orientation content confirmed unchanged and present in all four (`grep` for "design-oriented"/"execution-oriented").
6. Package root confirmed still `make-no-mistakes/` in all four `dist/<runtime>/` directories.
7. Confirmed no DOGFOOD-01 work was started.
8. `git diff --check` — clean.
9. Full diff reviewed line by line: exactly 8 lines changed across the four adapters (2 each) plus the validator strengthening in `scripts/build-packages.py` — no accidental semantic changes anywhere.

## Open Questions
None blocking. The one open item is operational, not a design question: the ChatGPT package needs to actually be reinstalled and visually confirmed before DOGFOOD-00 can be marked fully resolved (see Status above).

## Next Recommended Step
Reinstall the rebuilt `dist/chatgpt/make-no-mistakes` package (or its `.zip`) in ChatGPT and confirm the displayed Skill identity now reads "Make No Mistakes." Once confirmed, update this record's Status to reflect the passed runtime re-test, and resume toward DOGFOOD-01. Do not begin DOGFOOD-01 before that confirmation.

## Review Target
Confirm the four `SKILL.md` diffs contain only the two intended identity-string changes each (no wording, orientation, or semantic drift), and confirm the packaging-validator change is narrowly scoped (no YAML dependency, no schema, no manifest — just a stricter value check on the existing lightweight frontmatter parser).
