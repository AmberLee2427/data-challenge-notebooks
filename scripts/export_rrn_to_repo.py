#!/usr/bin/env python3
"""
Export transformed RRN notebooks into a directory structure that matches
the roman_notebooks repository.

For each notebook entry in notebooks_manifest.yml that defines an
`rrn_target`, this script copies the corresponding file from RRN/build
into the target path under the specified destination directory.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path
from typing import Iterable, Optional, Tuple

import yaml


def load_manifest(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def _write_refdata_stub(destination: Path) -> Path:
    """Ensure a top-level refdata_dependencies.yaml exists.

    STScI wrangler expects one global file per repository.
    This project does not require reference-data installs, so the file is minimal.
    """

    target = destination / "refdata_dependencies.yaml"
    if target.exists():
        return target

    # Keep this minimal and valid YAML. This repo does not require refdata.
    # STScI asked for a single global file per repository.
    lines = [
        "# See https://github.com/spacetelescope/roman_notebooks/blob/main/refdata_dependencies.yaml\n",
        "install_files: {}\n",
        "other_variables: {}\n",
    ]
    target.write_text("".join(lines), encoding="utf-8")
    return target



def export_rrn_notebooks(
    manifest: dict,
    build_dir: Path,
    destination: Path,
    *,
    clean: bool = False,
    env_source: Path | None = None,
    env_target_name: str = "environment.yml",
    requirements_source: Path | None = None,
    write_requirements: bool = True,
    write_refdata: bool = True,
    copy_ci_runner: bool = False,
    ci_runner_source: Path | None = None,
) -> Tuple[list[Path], Optional[Path]]:
    exported: list[Path] = []
    notebooks: Iterable[dict] = manifest.get("notebooks", [])

    destination.mkdir(parents=True, exist_ok=True)

    if write_refdata:
        _write_refdata_stub(destination)

    env_target: Path | None = None

    # Determine which notebook directories we will touch (for safe cleaning and
    # for requirements.txt placement).
    notebook_dirs: set[Path] = set()
    for entry in notebooks:
        if not entry.get("nexus_support", False):
            continue
        target = entry.get("rrn_target")
        nb_id = entry.get("id")
        if not nb_id or not target:
            continue
        target_path = destination / Path(target)
        notebook_dirs.add(target_path.parent)

    if clean:
        # Delete only the notebook directories we manage, never the repo root.
        for nb_dir in sorted(notebook_dirs, key=lambda p: len(p.parts), reverse=True):
            if nb_dir.exists():
                shutil.rmtree(nb_dir)

    for entry in notebooks:
        if not entry.get("nexus_support", False):
            continue
        nb_id = entry.get("id")
        target = entry.get("rrn_target")
        if not nb_id or not target:
            continue

        source_path = build_dir / f"{nb_id}.ipynb"
        if not source_path.exists():
            print(f"[warn] missing build artifact: {source_path}", file=sys.stderr)
            continue

        target_path = destination / Path(target)
        target_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_path, target_path)
        print(f"[export] {source_path} -> {target_path}")
        exported.append(target_path)

    # Optional: write a single top-level environment.yml.
    if env_source and env_source.exists():
        env_target = destination / env_target_name
        shutil.copy2(env_source, env_target)

    # Optional: write a per-directory requirements.txt (wrangler unions these).
    if write_requirements and requirements_source and requirements_source.exists():
        for nb_dir in sorted(notebook_dirs):
            nb_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(requirements_source, nb_dir / "requirements.txt")

    # Optional: copy a notebook CI runner script into the destination repo.
    if copy_ci_runner and ci_runner_source and ci_runner_source.exists():
        scripts_dir = destination / "scripts"
        scripts_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ci_runner_source, scripts_dir / ci_runner_source.name)

    return exported, env_target



def main() -> None:
    parser = argparse.ArgumentParser(
        description="Export RRN build notebooks into a target repository structure."
    )
    parser.add_argument(
        "--manifest",
        default="notebooks_manifest.yml",
        help="Path to notebooks manifest (default: notebooks_manifest.yml).",
    )
    parser.add_argument(
        "--build-dir",
        default="RRN/build",
        help="Directory containing transformed RRN notebooks (default: RRN/build).",
    )
    parser.add_argument(
        "--dest",
        required=True,
        help="Destination directory where exported notebooks should be written.",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Remove managed notebook directories before exporting (safe; never removes destination root).",
    )
    parser.add_argument(
        "--env-source",
        default="env.yml",
        help="Path to a source environment spec to copy into the destination (default: env.yml).",
    )
    parser.add_argument(
        "--env-target-name",
        default="environment.yml",
        help="Filename to use for the copied environment spec in the destination (default: environment.yml).",
    )
    parser.add_argument(
        "--requirements-source",
        default="requirements.txt",
        help="Path to a requirements.txt to copy into each notebook directory (default: requirements.txt).",
    )
    parser.add_argument(
        "--no-requirements",
        action="store_true",
        help="Do not write per-directory requirements.txt files into the destination.",
    )
    parser.add_argument(
        "--no-refdata",
        action="store_true",
        help="Do not create a refdata_dependencies.yaml stub in the destination.",
    )
    parser.add_argument(
        "--copy-ci-runner",
        action="store_true",
        help="Copy scripts/execute_notebooks_ci.py into the destination repo under scripts/.",
    )
    parser.add_argument(
        "--ci-runner-source",
        default="scripts/execute_notebooks_ci.py",
        help="Path to CI runner script to copy when --copy-ci-runner is set.",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    manifest_path = (repo_root / args.manifest).resolve()
    build_dir = (repo_root / args.build_dir).resolve()
    destination = (repo_root / args.dest).resolve()

    if not manifest_path.exists():
        print(f"[error] manifest not found: {manifest_path}", file=sys.stderr)
        sys.exit(1)

    if not build_dir.exists():
        print(f"[error] build directory not found: {build_dir}", file=sys.stderr)
        sys.exit(1)

    manifest = load_manifest(manifest_path)

    env_source = (repo_root / args.env_source).resolve() if args.env_source else None
    requirements_source = (
        (repo_root / args.requirements_source).resolve()
        if args.requirements_source
        else None
    )
    ci_runner_source = (
        (repo_root / args.ci_runner_source).resolve()
        if args.ci_runner_source
        else None
    )

    exported, env_target = export_rrn_notebooks(
        manifest,
        build_dir,
        destination,
        clean=args.clean,
        env_source=env_source,
        env_target_name=args.env_target_name,
        requirements_source=requirements_source,
        write_requirements=not args.no_requirements,
        write_refdata=not args.no_refdata,
        copy_ci_runner=args.copy_ci_runner,
        ci_runner_source=ci_runner_source,
    )
    if env_target:
        print(f"[export] copied env spec to {env_target}")
    print(f'[export] wrote {len(exported)} notebook(s) to {destination}')


if __name__ == "__main__":
    main()

