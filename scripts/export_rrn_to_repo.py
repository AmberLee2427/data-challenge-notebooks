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



def export_rrn_notebooks(
    manifest: dict, build_dir: Path, destination: Path
) -> Tuple[list[Path], Optional[Path]]:
    exported: list[Path] = []
    notebooks: Iterable[dict] = manifest.get("notebooks", [])

    if destination.exists():
        shutil.rmtree(destination)
    destination.mkdir(parents=True, exist_ok=True)

    env_source = Path("env.yml")
    env_target: Path | None = None

    for entry in notebooks:
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

        if env_source.exists():
            env_target_dir = target_path.parent
            env_target = env_target_dir / env_source.name
            shutil.copy2(env_source, env_target)

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
    exported, env_target = export_rrn_notebooks(manifest, build_dir, destination)
    if env_target:
        print(f'[export] copied env.yml to {env_target}')
    print(f'[export] wrote {len(exported)} notebook(s) to {destination}')


if __name__ == "__main__":
    main()

