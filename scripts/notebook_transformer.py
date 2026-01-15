#!/usr/bin/env python3
"""Utilities for building derived notebook artifacts (RRN, website, etc.)."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "PyYAML is required to run this script. Install with `pip install pyyaml`."
    ) from exc


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = REPO_ROOT / "notebooks_manifest.yml"
RRN_BUILD_DIR = REPO_ROOT / "RRN" / "build"
RRN_FOOTER_PATH = REPO_ROOT / "RRN" / "footer.md"
FOOTER_PATTERN = re.compile(
    r"<!-- Footer Start -->.*?<!-- Footer End -->",
    re.DOTALL,
)


class NotebookTransformer:
    """Transform notebooks based on manifest metadata."""

    def __init__(self, manifest_path: Path) -> None:
        self.manifest_path = manifest_path
        self.manifest = self._load_manifest(manifest_path)
        self._rrn_footer_content = self._load_rrn_footer()

    def build_rrn(
        self,
        include_ids: Iterable[str] | None = None,
        force: bool = False,
    ) -> List[Path]:
        """Create Nexus-ready notebook copies under RRN/build."""
        include_ids = set(include_ids) if include_ids else None
        RRN_BUILD_DIR.mkdir(parents=True, exist_ok=True)

        written: List[Path] = []
        for entry in self.manifest.get("notebooks", []):
            notebook_id = entry["id"]
            if include_ids and notebook_id not in include_ids:
                continue
            if not entry.get("nexus_support", False):
                continue

            source_path = REPO_ROOT / entry["source_path"]
            if not source_path.exists():
                raise FileNotFoundError(f"Source notebook not found: {source_path}")

            dest_path = RRN_BUILD_DIR / f"{notebook_id}.ipynb"
            if dest_path.exists() and not force:
                if dest_path.stat().st_mtime > source_path.stat().st_mtime:
                    # Dest newer than source; skip unless forcing rebuild.
                    continue

            notebook_data = self._load_notebook(source_path)
            transforms = entry.get("rrn_transforms") or [
                "clear_outputs",
                "record_metadata",
                "insert_rrn_footer",
                "warn_required_sections",
            ]
            for transform in transforms:
                self._apply_transform(transform, notebook_data, entry)

            self._write_notebook(dest_path, notebook_data)
            written.append(dest_path)

        return written

    @staticmethod
    def _load_manifest(path: Path) -> Dict[str, Any]:
        if not path.exists():
            raise FileNotFoundError(f"Manifest not found: {path}")

        with path.open("r", encoding="utf-8") as stream:
            data = yaml.safe_load(stream) or {}

        if "notebooks" not in data:
            raise ValueError("Manifest missing 'notebooks' key.")
        return data

    @staticmethod
    def _load_rrn_footer() -> str:
        if not RRN_FOOTER_PATH.exists():
            raise FileNotFoundError(
                f"RRN footer template not found: {RRN_FOOTER_PATH}"
            )
        text = RRN_FOOTER_PATH.read_text(encoding="utf-8").strip()
        if "<!-- Footer Start -->" not in text or "<!-- Footer End -->" not in text:
            raise ValueError(
                "RRN footer template must include '<!-- Footer Start -->' and '<!-- Footer End -->' markers."
            )
        return text

    @staticmethod
    def _load_notebook(path: Path) -> Dict[str, Any]:
        with path.open("r", encoding="utf-8") as stream:
            return json.load(stream)

    @staticmethod
    def _write_notebook(path: Path, data: Dict[str, Any]) -> None:
        with path.open("w", encoding="utf-8") as stream:
            json.dump(data, stream, indent=1)
            stream.write("\n")

    def _apply_transform(
        self, transform: str, notebook: Dict[str, Any], entry: Dict[str, Any]
    ) -> None:
        if transform == "clear_outputs":
            self._clear_outputs(notebook)
        elif transform == "record_metadata":
            self._record_metadata(notebook, entry)
        elif transform == "replace_purple_hr":
            self._replace_purple_hr(notebook)
        elif transform == "remove_colab_only":
            self._remove_cells_with_tag(notebook, "colab-only")
        elif transform == "insert_rrn_footer":
            self._insert_rrn_footer(notebook)
        elif transform == "warn_required_sections":
            self._warn_required_sections(notebook, entry)
        else:
            raise ValueError(f"Unknown transform '{transform}'")

    @staticmethod
    def _clear_outputs(notebook: Dict[str, Any]) -> None:
        for cell in notebook.get("cells", []):
            if cell.get("cell_type") == "code":
                cell["outputs"] = []
                cell["execution_count"] = None

    @staticmethod
    def _record_metadata(notebook: Dict[str, Any], entry: Dict[str, Any]) -> None:
        metadata = notebook.setdefault("metadata", {})
        sync_meta = metadata.setdefault("rges_sync", {})
        sync_meta["source_id"] = entry.get("id")
        sync_meta["session"] = entry.get("session")
        sync_meta["audiences"] = entry.get("audiences", [])
        sync_meta["website_render"] = entry.get("website_render")
        sync_meta["nexus_support"] = entry.get("nexus_support")

    @staticmethod
    def _replace_purple_hr(notebook: Dict[str, Any]) -> None:
        pattern = re.compile(r"<hr[^>]*a859e4[^>]*>", re.IGNORECASE)
        for cell in notebook.get("cells", []):
            if cell.get("cell_type") != "markdown":
                continue
            source = cell.get("source")
            if isinstance(source, list):
                new_lines = []
                for line in source:
                    if isinstance(line, str):
                        new_lines.append(pattern.sub("***", line))
                    else:
                        new_lines.append(line)
                cell["source"] = new_lines
            elif isinstance(source, str):
                cell["source"] = pattern.sub("***", source)

    @staticmethod
    def _remove_cells_with_tag(notebook: Dict[str, Any], tag: str) -> None:
        filtered = []
        for cell in notebook.get("cells", []):
            tags = set(cell.get("metadata", {}).get("tags", []))
            if tag in tags:
                continue
            filtered.append(cell)
        notebook["cells"] = filtered

    def _insert_rrn_footer(self, notebook: Dict[str, Any]) -> None:
        replacement = self._rrn_footer_content
        if not replacement:
            return

        for cell in notebook.get("cells", []):
            if cell.get("cell_type") != "markdown":
                continue

            source = cell.get("source", [])
            if isinstance(source, list):
                text = "".join(source)
            else:
                text = str(source)

            if "<!-- Footer Start -->" not in text:
                continue

            new_text = FOOTER_PATTERN.sub(replacement, text)
            if isinstance(source, list):
                cell["source"] = new_text.splitlines(keepends=True)
            else:
                cell["source"] = new_text

    _REQUIRED_SECTION_KEYWORDS: Dict[str, List[str]] = {
        "Learning Goals": ["learning goal"],
        "Introduction": ["introduction"],
        "Exercises": ["exercise"],
        "Additional Resources": ["additional resource"],
        "About this Notebook": ["about this notebook"],
    }

    def _warn_required_sections(
        self, notebook: Dict[str, Any], entry: Dict[str, Any]
    ) -> None:
        headings: List[str] = []
        for cell in notebook.get("cells", []):
            if cell.get("cell_type") != "markdown":
                continue
            text = "".join(cell.get("source", []))
            for line in text.splitlines():
                stripped = line.strip().lower()
                if stripped.startswith("#"):
                    headings.append(stripped)

        missing: List[str] = []
        for label, keywords in self._REQUIRED_SECTION_KEYWORDS.items():
            matched = False
            for heading in headings:
                if any(keyword in heading for keyword in keywords):
                    matched = True
                    break
            if not matched:
                missing.append(label)

        if missing:
            notebook_id = entry.get("id", "unknown")
            print(
                f"[warn] {notebook_id}: missing sections -> {', '.join(missing)}",
                file=sys.stderr,
            )

def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Transform notebooks for website/RRN targets based on manifest.",
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        default=DEFAULT_MANIFEST,
        help=f"Path to manifest file (default: {DEFAULT_MANIFEST})",
    )
    parser.add_argument(
        "--target",
        choices=["rrn"],
        default="rrn",
        help="Output target to build (currently only 'rrn' is supported).",
    )
    parser.add_argument(
        "--only",
        nargs="*",
        help="Optional list of notebook IDs to process.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Rebuild even if destination appears up-to-date.",
    )
    return parser.parse_args(argv)


def main(argv: List[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    transformer = NotebookTransformer(args.manifest)

    if args.target == "rrn":
        written = transformer.build_rrn(include_ids=args.only, force=args.force)
        if written:
            print("Updated RRN notebooks:")
            for path in written:
                print(f"  - {path.relative_to(REPO_ROOT)}")
        else:
            print("RRN notebooks already up-to-date.")
    else:  # pragma: no cover
        raise ValueError(f"Unsupported target {args.target}")

    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())

