"""Build website-ready markdown pages from canonical workshop docs.

Each markdown file under `AAS Workshop/` that ends with
`<!-- COPY TO: "bin/<filename>.md" -->` acts as a canonical source. This script
copies the preamble, web-content block, and any session overview snippets into
the corresponding `bin/` file, performing site-url templating along the way so
that `rges-pit.org` links become `{{ site.url }}{{ site.baseurl }}`."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Iterable, List, Optional, Tuple
from urllib.parse import quote

REPO_ROOT = Path(__file__).resolve().parents[1]
AAS_WORKSHOP_SUMMARY = REPO_ROOT / "bin/data_challenge_aas_workshop.md"
SITE_BASE = "https://rges-pit.org"
SOURCE_REPO = "rges-pit/data-challenge-bnotebooks"
SOURCE_BASE_URL = f"https://github.com/{SOURCE_REPO}/blob/main"

PREAMBLE_PATTERN = re.compile(r"(?s)^---.*?<!-- END PREAMBLE -->")
WEB_PATTERN = re.compile(
    r"<!-- BEGIN WEB CONTENT -->.*?<!-- END WEB CONTENT -->",
    re.DOTALL,
)
SESSION_PATTERN = re.compile(
    r"<!-- BEGIN SESSION (?P<label>[A-Za-z0-9]+) OVERVIEW -->"
    r".*?<!-- END SESSION (?P=label) OVERVIEW -->",
    re.DOTALL,
)
COPY_PATTERN = re.compile(r'<!--\s*COPY TO:\s*"([^"]+)"\s*-->\s*$')


def _read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def _replace_pattern(text: str, pattern: re.Pattern[str], replacement: str) -> str:
    if pattern.search(text):
        return pattern.sub(replacement, text, count=1)
    prefix = text if not text or text.endswith("\n") else text + "\n"
    return prefix + replacement


def _replace_tagged_block(text: str, begin: str, end: str, block: str) -> str:
    pattern = re.compile(re.escape(begin) + r".*?" + re.escape(end), re.DOTALL)
    if pattern.search(text):
        return pattern.sub(block, text, count=1)
    suffix = "" if not text or text.endswith("\n") else "\n"
    return text + suffix + block


def _apply_site_template(text: str) -> str:
    return text.replace(SITE_BASE, "{{ site.url }}{{ site.baseurl }}")


def _source_url(path: Path) -> str:
    rel_path = path.resolve().relative_to(REPO_ROOT).as_posix()
    return f"{SOURCE_BASE_URL}/{quote(rel_path, safe='/')}"


def _source_comment(path: Path, section: Optional[str] = None) -> str:
    label = f" ({section})" if section else ""
    return f"<!-- SOURCE{label}: {_source_url(path)} -->"


def _insert_comment_after(block: str, marker: str, comment: str) -> str:
    if marker not in block or comment in block:
        return block
    return block.replace(marker, f"{marker}\n{comment}", 1)


def _extract_section(pattern: re.Pattern[str], text: str) -> Optional[str]:
    match = pattern.search(text)
    return match.group(0) if match else None


def _extract_sessions(text: str) -> List[Tuple[str, str]]:
    return [(m.group("label"), m.group(0)) for m in SESSION_PATTERN.finditer(text)]


def _process_source(path: Path) -> None:
    text = _read_text(path)
    match = COPY_PATTERN.search(text.strip())
    if not match:
        return

    target_rel = Path(match.group(1))
    target_path = (REPO_ROOT / target_rel).resolve()

    preamble = _extract_section(PREAMBLE_PATTERN, text)
    web_block = _extract_section(WEB_PATTERN, text)
    session_blocks = _extract_sessions(text)

    target_text = _read_text(target_path)
    if preamble:
        preamble = _insert_comment_after(
            preamble, "<!-- END PREAMBLE -->", _source_comment(path, "preamble")
        )
        target_text = _replace_pattern(target_text, PREAMBLE_PATTERN, preamble)
    if web_block:
        web_block = _insert_comment_after(
            web_block,
            "<!-- BEGIN WEB CONTENT -->",
            _source_comment(path, "web content"),
        )
        target_text = _replace_pattern(target_text, WEB_PATTERN, web_block)
    target_text = _apply_site_template(target_text)
    _write_text(target_path, target_text)

    if session_blocks:
        summary_text = _read_text(AAS_WORKSHOP_SUMMARY)
        for label, block in session_blocks:
            begin = f"<!-- BEGIN SESSION {label} OVERVIEW -->"
            end = f"<!-- END SESSION {label} OVERVIEW -->"
            block = _insert_comment_after(
                block,
                begin,
                _source_comment(path, f"session {label} overview"),
            )
            summary_text = _replace_tagged_block(summary_text, begin, end, block)
        summary_text = _apply_site_template(summary_text)
        _write_text(AAS_WORKSHOP_SUMMARY, summary_text)


def _iter_sources(paths: Iterable[str]) -> List[Path]:
    resolved: List[Path] = []
    if paths:
        for entry in paths:
            candidate = Path(entry)
            if candidate.is_file():
                resolved.append(candidate)
            else:
                resolved.extend(sorted(candidate.rglob("*.md")))
    else:
        resolved = sorted((REPO_ROOT / "AAS Workshop").rglob("*.md"))
    return resolved


def main(argv: Optional[List[str]] = None) -> None:
    parser = argparse.ArgumentParser(
        description="Transform canonical workshop markdown into website-ready pages."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="Specific markdown files or directories to process. Defaults to all "
        "files under 'AAS Workshop/'.",
    )
    args = parser.parse_args(argv)

    sources = _iter_sources(args.paths)
    if not sources:
        print("No markdown sources found.")
        return

    for source in sources:
        try:
            _process_source(source)
        except Exception as exc:  # pragma: no cover - ad-hoc helper
            raise RuntimeError(f"Failed to transform {source}") from exc


if __name__ == "__main__":
    main()
