#!/usr/bin/env python3
"""Build self-contained MNM runtime packages from canonical source.

Assembles core/ + guidance/ + templates/ + capabilities/ + one runtime
adapter's SKILL.md into a self-contained package per runtime, under dist/.
Standard library only. No network access.
"""

import filecmp
import re
import shutil
import sys
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DIST = REPO_ROOT / "dist"
PACKAGE_NAME = "make-no-mistakes"
ZIP_EPOCH = (1980, 1, 1, 0, 0, 0)

CANONICAL_DIRS = ["core", "guidance", "templates", "capabilities"]

REQUIRED_FILES = {
    "core": [
        "PRINCIPLES.md", "WORKFLOW.md", "STATE.md",
        "EXECUTION.md", "VERIFICATION.md", "ASSURANCE.md",
    ],
    "guidance": [
        "git-baseline.md", "external-capabilities.md", "workflow-patterns.md",
    ],
    "templates": ["handoff.md", "review.md"],
    "capabilities": ["README.md", "application-security.md", "genai-security.md"],
}

ADAPTERS = {
    "chatgpt": "adapters/chatgpt/skills/software-project-workflow/SKILL.md",
    "claude-chat": "adapters/claude-chat/skills/software-project-workflow/SKILL.md",
    "codex": "adapters/codex/skills/software-project-workflow/SKILL.md",
    "claude-code": "adapters/claude-code/skills/software-project-workflow/SKILL.md",
}

FORBIDDEN_IN_PACKAGE = {"MNM_HANDOFF.md", ".git", "adapters"}


class BuildError(Exception):
    pass


def check_frontmatter(skill_md: Path) -> None:
    text = skill_md.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        raise BuildError(f"{skill_md}: missing YAML frontmatter block")
    frontmatter = match.group(1)
    for key in ("name:", "description:"):
        if not re.search(rf"^{re.escape(key)}", frontmatter, re.MULTILINE):
            raise BuildError(f"{skill_md}: frontmatter missing required '{key}' field")


def validate_source() -> None:
    version_file = REPO_ROOT / "VERSION"
    if not version_file.is_file():
        raise BuildError("VERSION file is missing at repository root")
    if not version_file.read_text(encoding="utf-8").strip():
        raise BuildError("VERSION file is empty")

    for dir_name, files in REQUIRED_FILES.items():
        dir_path = REPO_ROOT / dir_name
        if not dir_path.is_dir():
            raise BuildError(f"required canonical directory missing: {dir_name}/")
        for fname in files:
            if not (dir_path / fname).is_file():
                raise BuildError(f"required canonical file missing: {dir_name}/{fname}")

    for runtime, rel_path in ADAPTERS.items():
        skill_md = REPO_ROOT / rel_path
        if not skill_md.is_file():
            raise BuildError(f"adapter entry point missing for {runtime}: {rel_path}")
        check_frontmatter(skill_md)


def clean_dist() -> None:
    dist = DIST.resolve()
    if dist != REPO_ROOT / "dist":
        raise BuildError(f"refusing to clean unexpected dist path: {dist}")
    if dist.exists():
        shutil.rmtree(dist)
    dist.mkdir(parents=True)


def build_package(runtime: str) -> Path:
    package_dir = DIST / runtime / PACKAGE_NAME
    package_dir.mkdir(parents=True)

    shutil.copyfile(REPO_ROOT / ADAPTERS[runtime], package_dir / "SKILL.md")
    shutil.copyfile(REPO_ROOT / "VERSION", package_dir / "VERSION")
    for dir_name in CANONICAL_DIRS:
        shutil.copytree(REPO_ROOT / dir_name, package_dir / dir_name)

    return package_dir


def validate_package(runtime: str, package_dir: Path) -> None:
    skill_md = package_dir / "SKILL.md"
    if not skill_md.is_file():
        raise BuildError(f"[{runtime}] packaged SKILL.md missing")
    check_frontmatter(skill_md)
    if "adapters/" in skill_md.read_text(encoding="utf-8"):
        raise BuildError(f"[{runtime}] packaged SKILL.md still references a source-only adapters/ path")

    version = package_dir / "VERSION"
    if not filecmp.cmp(version, REPO_ROOT / "VERSION", shallow=False):
        raise BuildError(f"[{runtime}] packaged VERSION does not match source VERSION")

    for dir_name, files in REQUIRED_FILES.items():
        for fname in files:
            packaged = package_dir / dir_name / fname
            source = REPO_ROOT / dir_name / fname
            if not packaged.is_file():
                raise BuildError(f"[{runtime}] packaged {dir_name}/{fname} missing")
            if not filecmp.cmp(packaged, source, shallow=False):
                raise BuildError(f"[{runtime}] packaged {dir_name}/{fname} differs from canonical source")

    for entry in package_dir.rglob("*"):
        if entry.name in FORBIDDEN_IN_PACKAGE:
            raise BuildError(f"[{runtime}] forbidden entry present in package: {entry.relative_to(package_dir)}")

    for other_runtime in ADAPTERS:
        if other_runtime == runtime:
            continue
        if other_runtime in {p.name for p in package_dir.rglob("*") if p.is_dir()}:
            raise BuildError(f"[{runtime}] package appears to contain another runtime's adapter: {other_runtime}")


def build_zip(runtime: str, package_dir: Path) -> Path:
    zip_path = DIST / runtime / f"{PACKAGE_NAME}.zip"
    files = sorted(p for p in package_dir.rglob("*") if p.is_file())
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for file_path in files:
            arcname = f"{PACKAGE_NAME}/{file_path.relative_to(package_dir).as_posix()}"
            info = zipfile.ZipInfo(arcname, date_time=ZIP_EPOCH)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o644 & 0xFFFF) << 16
            zf.writestr(info, file_path.read_bytes())
    return zip_path


def validate_zip(runtime: str, zip_path: Path, package_dir: Path) -> None:
    expected = {
        f"{PACKAGE_NAME}/{p.relative_to(package_dir).as_posix()}"
        for p in package_dir.rglob("*") if p.is_file()
    }
    with zipfile.ZipFile(zip_path) as zf:
        actual = set(zf.namelist())
        if actual != expected:
            raise BuildError(f"[{runtime}] zip contents do not match package directory ({actual ^ expected})")
        for name in sorted(expected):
            source_path = package_dir / name[len(PACKAGE_NAME) + 1:]
            if zf.read(name) != source_path.read_bytes():
                raise BuildError(f"[{runtime}] zip entry {name} content differs from package directory")


def main() -> int:
    try:
        validate_source()
        clean_dist()
        for runtime in ADAPTERS:
            package_dir = build_package(runtime)
            validate_package(runtime, package_dir)
            zip_path = build_zip(runtime, package_dir)
            validate_zip(runtime, zip_path, package_dir)
            print(f"built {runtime}: {package_dir} + {zip_path}")
    except BuildError as exc:
        print(f"build failed: {exc}", file=sys.stderr)
        return 1

    print(f"all {len(ADAPTERS)} packages built and validated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
