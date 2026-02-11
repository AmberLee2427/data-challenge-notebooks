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
CI_BUILD_DIR = REPO_ROOT / "RRN" / "ci_build"
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
            transforms = entry.get("rrn_transforms") or [
                "clear_outputs",
                "record_metadata",
                "insert_rrn_footer",
                "warn_required_sections",
            ]

            if "sync" in transforms:
                self._sync_source(entry)

            dest_path = RRN_BUILD_DIR / f"{notebook_id}.ipynb"
            if dest_path.exists() and not force:
                if source_path.exists() and dest_path.stat().st_mtime > source_path.stat().st_mtime:
                    # Dest newer than source; skip unless forcing rebuild.
                    continue

            if "convert_rst_to_notebook" in transforms:
                notebook_data = self._new_notebook()
            else:
                if not source_path.exists():
                    raise FileNotFoundError(f"Source notebook not found: {source_path}")
                notebook_data = self._load_notebook(source_path)

            if "tag_ci_skip_nexus_only" not in transforms:
                # Always tag Nexus-only env activation cells so CI can skip them.
                # Keep this behavior independent of per-notebook rrn_transforms.
                transforms = ["tag_ci_skip_nexus_only", *transforms]
            for transform in transforms:
                if transform == "sync":
                    continue
                self._apply_transform(transform, notebook_data, entry)

            self._write_notebook(dest_path, notebook_data)
            written.append(dest_path)

        for entry in self.manifest.get("scripts", []):
            notebook_id = entry["id"]
            if include_ids and notebook_id not in include_ids:
                continue
            if not entry.get("nexus_support", False):
                continue
            written.append(self._process_script_entry(entry, force))

        for entry in self.manifest.get("other", []):
            notebook_id = entry["id"]
            if include_ids and notebook_id not in include_ids:
                continue
            if not entry.get("nexus_support", False):
                continue
            written.append(self._process_other_entry(entry, force))

        return written

    def _process_script_entry(self, entry: Dict[str, Any], force: bool) -> Path:
        notebook_id = entry["id"]
        source_path = REPO_ROOT / entry["source_path"]
        if not source_path.exists():
            raise FileNotFoundError(f"Source script not found: {source_path}")

        # Determine target filename from rrn_target or default to .ipynb
        dest_filename = f"{notebook_id}.ipynb"
        if entry.get("rrn_target"):
             dest_filename = Path(entry["rrn_target"]).name

        dest_path = RRN_BUILD_DIR / dest_filename
        if dest_path.exists() and not force:
            if dest_path.stat().st_mtime > source_path.stat().st_mtime:
                return dest_path

        # Check if the target is intended to stay as a script/plaintext
        if dest_path.suffix.lower() != ".ipynb":
            import shutil
            shutil.copy2(source_path, dest_path)
            return dest_path

        # Else, wrap in notebook structure
        script_content = source_path.read_text(encoding="utf-8")
        notebook = self._new_notebook()
        
        # Create a single code cell with the script content
        notebook["cells"].append({
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": script_content.splitlines(keepends=True)
        })

        transforms = entry.get("rrn_transforms", [])
        for transform in transforms:
             self._apply_transform(transform, notebook, entry)

        self._write_notebook(dest_path, notebook)
        return dest_path


    def _process_other_entry(self, entry: Dict[str, Any], force: bool) -> Path:
        notebook_id = entry["id"]
        source_path = REPO_ROOT / entry["source_path"]
        if not source_path.exists():
            raise FileNotFoundError(f"Source file not found: {source_path}")

        # Use source suffix for the build artifact
        dest_filename = f"{notebook_id}{source_path.suffix}"
        if entry.get("rrn_target"):
            dest_filename = Path(entry["rrn_target"]).name

        dest_path = RRN_BUILD_DIR / dest_filename

        if dest_path.exists() and not force:
            if dest_path.stat().st_mtime > source_path.stat().st_mtime:
                return dest_path

        # If it's a markdown file and has transforms, process it as text
        transforms = entry.get("rrn_transforms", [])
        if source_path.suffix.lower() == ".md" and transforms:
            content = source_path.read_text(encoding="utf-8")
            for transform in transforms:
                content = self._apply_text_transform(transform, content, entry)
            dest_path.write_text(content, encoding="utf-8")
        else:
            import shutil
            shutil.copy2(source_path, dest_path)
            
        return dest_path

    def _apply_text_transform(self, transform: str, content: str, entry: Dict[str, Any]) -> str:
        if transform == "build_like_website":
            return self._inject_web_content(content)
        elif transform == "footer" or transform == "insert_rrn_footer":
            return self._insert_rrn_footer_text(content)
        elif transform == "clear_outputs": # Not applicable to text
             return content
        elif transform == "record_metadata": # Not applicable to text
             return content
        elif transform == "remove_colab_only": # Not applicable to text
             return content
        elif transform == "replace_purple_hr": # Could apply
             return content.replace('<hr style="border:2px solid #a859e4">', '***')
        elif transform == "warn_required_sections": # Not applicable to text
             return content
        else:
            print(f"[warn] Transform '{transform}' not supported for text files", file=sys.stderr)
            return content

    def _inject_web_content(self, content: str) -> str:
        """Inject content from a source URL defined in a comment."""
        source_match = re.search(r"<!-- SOURCE \(web content\): (.*?) -->", content)
        if not source_match:
            return content

        source_url = source_match.group(1).strip()
        # Resolve URL to local path if possible
        repo_prefix = "https://github.com/rges-pit/data-challenge-notebooks/blob/main/"
        if source_url.startswith(repo_prefix):
            rel_path = source_url[len(repo_prefix):]
            from urllib.parse import unquote
            rel_path = unquote(rel_path)
            source_path = REPO_ROOT / rel_path
            
            if not source_path.exists():
                print(f"[warn] Web content source not found: {source_path}", file=sys.stderr)
                return content
                
            source_text = source_path.read_text(encoding="utf-8")
            
            # Extract content between markers
            web_pattern = re.compile(r"<!-- BEGIN WEB CONTENT -->.*?<!-- END WEB CONTENT -->", re.DOTALL)
            match = web_pattern.search(source_text)
            if match:
                extracted = match.group(0)
                # Replace in target
                if web_pattern.search(content):
                    return web_pattern.sub(lambda m: extracted, content)
                else:
                    print("[warn] Target missing '<!-- BEGIN/END WEB CONTENT -->' markers", file=sys.stderr)
                    return content
            else:
                 print(f"[warn] Source {source_path} missing '<!-- BEGIN/END WEB CONTENT -->' markers", file=sys.stderr)
                 return content
        else:
             print(f"[warn] Web content source URL not supported: {source_url}", file=sys.stderr)
             return content

    def _insert_rrn_footer_text(self, content: str) -> str:
        replacement = self._rrn_footer_content
        if not replacement:
            return content
            
        if "<!-- Footer Start -->" in content:
            return FOOTER_PATTERN.sub(replacement, content)
        else:
            return content + "\n\n" + replacement

    def build_ci(
        self,
        include_ids: Iterable[str] | None = None,
        force: bool = False,
    ) -> List[Path]:
        """Create CI-executable notebook copies under RRN/ci_build.

        This target is meant to be runnable on GitHub Actions (standard Jupyter
        kernel) and therefore removes Nexus-only activation cells such as
        `%source kernel-activate ...`.
        """

        include_ids = set(include_ids) if include_ids else None
        CI_BUILD_DIR.mkdir(parents=True, exist_ok=True)

        written: List[Path] = []
        for entry in self.manifest.get("notebooks", []):
            notebook_id = entry["id"]
            if include_ids and notebook_id not in include_ids:
                continue

            # CI should only execute notebooks intended to run outside Nexus.
            # Default rule: skip notebooks explicitly marked as not applicable to Colab.
            if entry.get("ci_support") is False:
                continue
            if entry.get("colab_support") == "not_applicable":
                continue

            source_path = REPO_ROOT / entry["source_path"]
            if not source_path.exists():
                raise FileNotFoundError(f"Source notebook not found: {source_path}")

            dest_path = CI_BUILD_DIR / f"{notebook_id}.ipynb"
            if dest_path.exists() and not force:
                if dest_path.stat().st_mtime > source_path.stat().st_mtime:
                    continue

            notebook_data = self._load_notebook(source_path)
            transforms = entry.get("ci_transforms") or [
                "clear_outputs",
                "record_metadata",
                "replace_purple_hr",
                "remove_nexus_only_cells",
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
            json.dump(data, stream, indent=1, ensure_ascii=False)
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
        elif transform == "tag_ci_skip_nexus_only":
            self._tag_ci_skip_nexus_only(notebook)
        elif transform == "remove_nexus_only_cells":
            self._remove_nexus_only_cells(notebook)
        elif transform == "insert_rrn_footer" or transform == "footer":
            self._insert_rrn_footer(notebook)
        elif transform == "warn_required_sections":
            self._warn_required_sections(notebook, entry)
        elif transform == "convert_rst_to_notebook":
            self._convert_rst_to_notebook(notebook, entry)
        else:
            raise ValueError(f"Unknown transform '{transform}'")

    @staticmethod
    def _new_notebook() -> Dict[str, Any]:
        return {
            "cells": [],
            "metadata": {},
            "nbformat": 4,
            "nbformat_minor": 5,
        }

    def _sync_source(self, entry: Dict[str, Any]) -> None:
        upstream_url = entry.get("upstream_url")
        source_path = entry.get("source_path")
        if not upstream_url or not source_path:
            raise ValueError("Sync requires both 'upstream_url' and 'source_path'.")

        dest_path = REPO_ROOT / source_path
        dest_path.parent.mkdir(parents=True, exist_ok=True)

        from urllib.request import urlopen

        with urlopen(upstream_url, timeout=30) as response:
            payload = response.read()
        dest_path.write_bytes(payload)
        print(f"[sync] {upstream_url} -> {dest_path}")

    def _convert_rst_to_notebook(self, notebook: Dict[str, Any], entry: Dict[str, Any]) -> None:
        source_path = REPO_ROOT / entry["source_path"]
        if not source_path.exists():
            raise FileNotFoundError(f"Source RST not found: {source_path}")

        rst_text = source_path.read_text(encoding="utf-8")
        html_body: str | None = None

        try:
            from docutils.core import publish_parts

            parts = publish_parts(source=rst_text, writer_name="html")
            html_body = parts.get("html_body")
        except Exception:
            html_body = None

        if html_body:
            # Drop syntax-highlighting spans for cleaner markdown conversion.
            html_body = re.sub(r"</?span[^>]*>", "", html_body)

            try:
                from markdownify import markdownify as html_to_md

                markdown_text = html_to_md(
                    html_body,
                    heading_style="ATX",
                    code_block_style="fenced",
                )
                markdown_text = self._clean_markdown(markdown_text)
                cell_source = [markdown_text]
            except Exception as e:
                print(f"[error] Markdown conversion failed: {e}", file=sys.stderr)
                cell_source = [html_body]
        else:
            cell_source = [
                "# Notebook Content\n\n",
                "> **Note:** RST conversion requires `docutils`. Showing raw content below.\n\n",
                "```text\n",
                rst_text,
                "\n```\n",
            ]

        notebook.clear()
        notebook.update(self._new_notebook())
        notebook["cells"].append(
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": cell_source,
            }
        )

    @staticmethod
    def _clean_markdown(text: str) -> str:
        lines = text.splitlines()
        cleaned: List[str] = []
        first_heading_seen = False
        admonition_labels = {"note", "warning", "tip", "important"}

        # State for code block handling
        buffer: List[str] = []
        in_block = False
        block_indent = ""
        block_char = ""
        block_len = 0
        block_info = ""

        # Pattern for fence detection
        fence_pattern = re.compile(r"^(\s*)(`{3,}|~{3,})(.*)$")

        i = 0
        skip_system_block = False
        
        while i < len(lines):
            line = lines[i]
            # Handle system messages (docutils artifacts)
            if skip_system_block:
                if line.strip() == "":
                    skip_system_block = False
                i += 1
                continue
            if line.strip().startswith("System Message:"):
                skip_system_block = True
                i += 1
                continue

            # Code Block Handling
            match = fence_pattern.match(line)
            is_fence = match is not None

            if not in_block:
                if is_fence:
                    in_block = True
                    block_indent = match.group(1)
                    block_char = match.group(2)[0]
                    block_len = len(match.group(2))
                    block_info = match.group(3)
                    buffer = []
                    i += 1
                    continue
            else:
                # Inside block
                is_closing = False
                if is_fence:
                    # Check if it matches opening fence
                    char = match.group(2)[0]
                    length = len(match.group(2))
                    # strict length match to handle nested fences that are longer
                    if char == block_char and length == block_len:
                        is_closing = True
                
                if is_closing:
                    # Flush buffer
                    in_block = False
                    
                    # Calculate safe fence length based on content
                    required_len = block_len
                    for bline in buffer:
                        b_match = fence_pattern.match(bline)
                        if b_match:
                            b_len = len(b_match.group(2))
                            if b_len >= required_len:
                                required_len = b_len + 1
                    
                    delimiter = "~" * required_len
                    cleaned.append(f"{block_indent}{delimiter}{block_info}")
                    cleaned.extend(buffer)
                    cleaned.append(f"{block_indent}{delimiter}")
                    i += 1
                    continue
                else:
                    # Buffer content, fixing the inner markdown heading issue if needed
                    # We can retain the content exactly or fix specific issues
                    if line.strip().startswith("## Fitting code snippet"):
                        # Convert to comments or text
                         buffer.append("# Fitting code snippet")
                    else:
                        buffer.append(line)
                    i += 1
                    continue

            # Standard line processing (outside block)
            stripped = line.strip()

            # Normalize headings
            if stripped.startswith("#"):
                if stripped.startswith("# **") and stripped.endswith("**"):
                    content = stripped.lstrip("#").strip()
                    content = content.strip("*")
                    heading = "# " + content
                else:
                    heading = stripped

                if heading.startswith("# "):
                    if first_heading_seen:
                        heading = "## " + heading[2:]
                    else:
                        first_heading_seen = True
                cleaned.append(heading)
                i += 1
                continue

            # Convert admonitions
            if stripped.lower() in admonition_labels:
                label = stripped.capitalize()
                cleaned.append(f"> **{label}:**")
                i += 1
                # Capture block content until empty line
                while i < len(lines) and lines[i].strip() == "":
                    i += 1
                while i < len(lines) and lines[i].strip() != "":
                    cleaned.append(f"> {lines[i]}")
                    i += 1
                cleaned.append("")
                continue

            # Fix hanging indents from RST
            if line.startswith("   ") and not line.startswith("    "):
                if not stripped.startswith(("-", "*")) and not re.match(r"\d+\.\s", stripped):
                    line = " " + line

            cleaned.append(line)
            i += 1
        
        # Flush any remaining buffer if block wasn't closed (shouldn't happen with valid md)
        if in_block:
             delimiter = "~" * block_len
             cleaned.append(f"{block_indent}{delimiter}{block_info}")
             cleaned.extend(buffer)

        filtered: List[str] = []
        skip_block = False
        for line in cleaned:
            stripped = line.strip()
            if skip_block:
                if stripped == "":
                    skip_block = False
                continue
            if "System Message:" in line:
                skip_block = True
                continue
            if "Unexpected indentation." in line:
                continue
            if "Cannot analyze code. No Pygments lexer found for \"csv\"." in line:
                continue
            filtered.append(line)

        return "\n".join(filtered).strip() + "\n"

    @staticmethod
    def _clear_outputs(notebook: Dict[str, Any]) -> None:
        for cell in notebook.get("cells", []):
            if cell.get("cell_type") == "code":
                cell["outputs"] = []
                cell["execution_count"] = None

    @staticmethod
    def _record_metadata(notebook: Dict[str, Any], entry: Dict[str, Any]) -> None:
        metadata = notebook.setdefault("metadata", {})
        
        # Enforce Nexus-compatible kernelspec if rges-pit-dc
        kspec = metadata.get("kernelspec", {})
        if kspec.get("name") == "rges-pit-dc" or kspec.get("display_name") == "rges-pit-dc":
             kspec["name"] = "rges-pit-dc" # Ensure internal name matches
             kspec["display_name"] = "RGES PIT Nexus"
             kspec["version"] = "3.11.14" # As requested by Nexus PR
             metadata["kernelspec"] = kspec

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

    @staticmethod
    def _tag_ci_skip_nexus_only(notebook: Dict[str, Any]) -> None:
        """Tag Nexus-only cells so generic CI execution can skip them.

        Some Nexus environments provide custom magics (e.g. `%source kernel-activate ...`).
        Those magics are not available in a standard Jupyter kernel, so CI should skip
        these cells while leaving them in the notebook for real Nexus/RRN runs.
        """

        nexus_only_pattern = re.compile(r"(?m)^\s*#\s*NEXUS-ONLY\b")
        source_magic_pattern = re.compile(r"(?m)^\s*%source\b")

        for cell in notebook.get("cells", []):
            if cell.get("cell_type") != "code":
                continue

            source = cell.get("source", [])
            if isinstance(source, list):
                text = "".join(str(line) for line in source)
            else:
                text = str(source)

            if not (nexus_only_pattern.search(text) or source_magic_pattern.search(text)):
                continue

            meta = cell.setdefault("metadata", {})
            tags = meta.get("tags")
            if not isinstance(tags, list):
                tags = []
            if "ci-skip" not in tags:
                tags.append("ci-skip")
            meta["tags"] = tags

    @staticmethod
    def _remove_nexus_only_cells(notebook: Dict[str, Any]) -> None:
        """Remove Nexus-only cells so the notebook is runnable in vanilla Jupyter."""

        nexus_only_pattern = re.compile(r"(?m)^\s*#\s*NEXUS-ONLY\b")
        source_magic_pattern = re.compile(r"(?m)^\s*%source\b")
        kernel_activate_pattern = re.compile(r"kernel-activate\b")

        filtered = []
        for cell in notebook.get("cells", []):
            if cell.get("cell_type") != "code":
                filtered.append(cell)
                continue

            meta = cell.get("metadata", {}) or {}
            tags = set(meta.get("tags", []) or [])
            if "nexus-only" in tags:
                continue

            source = cell.get("source", [])
            if isinstance(source, list):
                text = "".join(str(line) for line in source)
            else:
                text = str(source)

            if nexus_only_pattern.search(text) or source_magic_pattern.search(text) or kernel_activate_pattern.search(text):
                continue

            filtered.append(cell)

        notebook["cells"] = filtered

    def _insert_rrn_footer(self, notebook: Dict[str, Any]) -> None:
        replacement = self._rrn_footer_content
        if not replacement:
            return

        footer_found = False
        for cell in notebook.get("cells", []):
            if cell.get("cell_type") != "markdown":
                continue

            source = cell.get("source", [])
            if isinstance(source, list):
                text = "".join(source)
            else:
                text = str(source)

            if "<!-- Footer Start -->" in text:
                footer_found = True
                new_text = FOOTER_PATTERN.sub(replacement, text)
                if isinstance(source, list):
                    cell["source"] = new_text.splitlines(keepends=True)
                else:
                    cell["source"] = new_text
                # Assuming only one footer per notebook
                break
        
        if not footer_found:
            notebook.setdefault("cells", []).append({
                "cell_type": "markdown",
                "metadata": {},
                "source": replacement.splitlines(keepends=True)
            })

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
        choices=["rrn", "ci"],
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
    elif args.target == "ci":
        written = transformer.build_ci(include_ids=args.only, force=args.force)
        if written:
            print("Updated CI notebooks:")
            for path in written:
                print(f"  - {path.relative_to(REPO_ROOT)}")
        else:
            print("CI notebooks already up-to-date.")
    else:  # pragma: no cover
        raise ValueError(f"Unsupported target {args.target}")

    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())

