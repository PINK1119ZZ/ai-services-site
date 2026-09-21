#!/usr/bin/env python3
"""Build a deterministic, allowlisted static-site artifact."""

from __future__ import annotations

import argparse
import hashlib
import json
import posixpath
import sys
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit


ROOT_FILES = {
    "404.html", "CNAME", "about.html", "ads.txt", "ai-model.html",
    "apple-touch-icon.png", "autodev-logo2.png", "bot-cloud.html",
    "chat-widget.js", "contact.html", "demo.html", "disclaimer.html",
    "favicon.ico", "feed.xml", "icon-192.png", "index.html", "lang.js",
    "line-bot-saas.html", "llms.txt", "portfolio.html", "pricing.html",
    "privacy.html", "robots.txt", "services.html", "sitemap.xml",
    "style.css", "terms.html",
}
PUBLIC_EXTENSIONS = {
    ".html", ".css", ".js", ".png", ".jpg", ".jpeg", ".webp", ".gif",
    ".svg", ".ico", ".woff", ".woff2", ".ttf", ".otf",
}
PUBLIC_TREES = ("blog", "en", "tools", "assets")
REDESIGNED_PAGES = {
    "index.html", "services.html", "portfolio.html", "about.html", "pricing.html", "contact.html",
    "en/index.html", "en/services.html", "en/portfolio.html", "en/about.html", "en/pricing.html", "en/contact.html",
}
EXACT_NESTED = {
    "downloads/index.html", "downloads/ai-tools-guide-2026.html",
    "kira/index.html",
    "assets/showcase/kira-reel.mp4",
    "assets/showcase/kira-reel-2.mp4",
    "assets/showcase/kira-reel-3.mp4",
    "assets/showcase/kira-reel-4.mp4",
}
RESOURCE_ATTRIBUTES = {
    "script": ("src",), "img": ("src", "srcset"),
    "source": ("src", "srcset"), "video": ("src", "poster"),
    "audio": ("src",), "iframe": ("src",),
}


class BuildError(RuntimeError):
    pass


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.references: list[tuple[str, str]] = []
        self.anchors: set[str] = set()

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        self.anchors.update(value for key, value in attrs if key == "id" and value)
        if tag == "a" and values.get("name"):
            self.anchors.add(values["name"])
        if tag == "a" and values.get("href"):
            self.references.append(("link", values["href"]))
        elif tag == "link" and values.get("href"):
            rel = set((values.get("rel") or "").lower().split())
            if rel & {"stylesheet", "icon", "preload", "manifest"}:
                self.references.append(("resource", values["href"]))
        for attribute in RESOURCE_ATTRIBUTES.get(tag, ()):
            value = values.get(attribute)
            if not value:
                continue
            if attribute == "srcset":
                self.references.extend(("resource", item.strip().split()[0]) for item in value.split(",") if item.strip())
            else:
                self.references.append(("resource", value))
        for attribute in ("data-src", "data-poster"):
            if values.get(attribute):
                self.references.append(("resource", values[attribute]))


def _reject_symlink_chain(path: Path, label: str) -> None:
    absolute = path.absolute()
    current = Path(absolute.anchor)
    for part in absolute.parts[1:]:
        current /= part
        if current.is_symlink():
            raise BuildError(f"{label} has a symlink component: {current}")
        if not current.exists():
            break


def _safe_file(source: Path, relative: str) -> Path | None:
    candidate = source / relative
    _reject_symlink_chain(candidate, "allowlisted path")
    if not candidate.exists() and not candidate.is_symlink():
        return None
    if candidate.is_symlink() or not candidate.is_file():
        raise BuildError(f"allowlisted path is not a regular file: {relative}")
    return candidate


def collect_files(source: Path) -> dict[str, Path]:
    selected: dict[str, Path] = {}
    for relative in sorted(ROOT_FILES | EXACT_NESTED):
        candidate = _safe_file(source, relative)
        if candidate:
            selected[relative] = candidate
    for tree in PUBLIC_TREES:
        root = source / tree
        _reject_symlink_chain(root, "public tree")
        if not root.exists():
            continue
        if root.is_symlink() or not root.is_dir():
            raise BuildError(f"public tree is not a regular directory: {tree}")
        for candidate in sorted(root.rglob("*")):
            relative = candidate.relative_to(source).as_posix()
            if candidate.is_symlink():
                raise BuildError(f"symlink is forbidden in public tree: {relative}")
            if candidate.is_file() and candidate.suffix.lower() in PUBLIC_EXTENSIONS:
                selected[relative] = candidate
    return dict(sorted(selected.items()))


def _local_target(page: str, raw_url: str) -> tuple[str, str] | None:
    parsed = urlsplit(raw_url.strip())
    if parsed.scheme or parsed.netloc or raw_url.startswith("//"):
        return None
    if parsed.path:
        decoded = unquote(parsed.path)
        combined = decoded.lstrip("/") if decoded.startswith("/") else posixpath.join(posixpath.dirname(page), decoded)
        normalized = posixpath.normpath(combined)
        if normalized == ".." or normalized.startswith("../") or PurePosixPath(normalized).is_absolute():
            raise BuildError(f"path traversal in {page}: {raw_url}")
        target = normalized
    else:
        target = page
    if not target or target == "." or raw_url.split("?", 1)[0].endswith("/"):
        target = posixpath.join(target if target != "." else "", "index.html")
    return target, unquote(parsed.fragment)


def validate_html(source: Path, selected: dict[str, Path], payloads: dict[str, bytes]) -> list[dict[str, str]]:
    parsed_pages: dict[str, PageParser] = {}
    for relative, path in selected.items():
        if path.suffix.lower() == ".html":
            parser = PageParser()
            parser.feed(payloads[relative].decode("utf-8", errors="replace"))
            parsed_pages[relative] = parser
    warnings: set[tuple[str, str, str]] = set()
    for page, parser in parsed_pages.items():
        for kind, raw_url in parser.references:
            result = _local_target(page, raw_url)
            if result is None:
                continue
            target, fragment = result
            source_target = source / target
            if source_target.is_dir():
                target = posixpath.join(target, "index.html")
                source_target = source / target
            if source_target.exists() and target not in selected:
                raise BuildError(f"{page} references excluded {kind}: {target}")
            if not source_target.exists():
                if page in REDESIGNED_PAGES:
                    raise BuildError(f"redesigned page has a missing {kind}: {page} -> {target}")
                warnings.add(("source-existing-missing", page, target))
            elif fragment and target in parsed_pages and fragment not in parsed_pages[target].anchors:
                missing_anchor = f"{target}#{fragment}"
                if page in REDESIGNED_PAGES:
                    raise BuildError(f"redesigned page has a missing anchor: {page} -> {missing_anchor}")
                warnings.add(("source-existing-anchor", page, missing_anchor))
    return [
        {"kind": kind, "page": page, "target": target}
        for kind, page, target in sorted(warnings)
    ]


def build_static(source: Path | str, output: Path | str) -> dict:
    source_input = Path(source).absolute()
    output_input = Path(output).absolute()
    _reject_symlink_chain(source_input, "source")
    _reject_symlink_chain(output_input, "output")
    if not source_input.is_dir():
        raise BuildError(f"source must be a regular directory: {source_input}")
    source = source_input.resolve()
    output = output_input.resolve()
    if not source.is_dir():
        raise BuildError(f"source must be a regular directory: {source}")
    if output == source or output.is_relative_to(source):
        raise BuildError("output must be outside the source tree")
    if output.exists():
        if not output.is_dir() or any(output.iterdir()):
            raise BuildError(f"output must be absent or an empty directory: {output}")
    selected = collect_files(source)
    payloads: dict[str, bytes] = {}
    for relative, path in selected.items():
        _reject_symlink_chain(path, "allowlisted path")
        if not path.is_file():
            raise BuildError(f"allowlisted path changed before snapshot: {relative}")
        payloads[relative] = path.read_bytes()
    warnings = validate_html(source, selected, payloads)
    entries = [
        {"path": relative, "bytes": len(payloads[relative]), "sha256": hashlib.sha256(payloads[relative]).hexdigest()}
        for relative in selected
    ]
    output.mkdir(parents=True, exist_ok=True)
    for relative in selected:
        destination = output / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(payloads[relative])
    manifest = {"schema": 1, "files": entries, "warnings": warnings}
    (output / "static-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        manifest = build_static(args.source, args.output)
    except BuildError as error:
        parser.exit(2, f"static build refused: {error}\n")
    print(f"built {len(manifest['files'])} files with {len(manifest['warnings'])} source-existing warnings")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
