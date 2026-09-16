"""Verifica destinos locais e âncoras de links Markdown deste repositório."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
IGNORED_DIRECTORIES = {".git", ".venv", "node_modules"}
LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^\s)]+)(?:\s+[^)]*)?\)")
HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
FENCE_PATTERN = re.compile(r"^\s*(```|~~~)")


def without_fenced_code(text: str) -> str:
    """Remove blocos de código, onde sequências parecidas com links são exemplos."""
    kept: list[str] = []
    fence: str | None = None
    for line in text.splitlines():
        matched = FENCE_PATTERN.match(line)
        if matched:
            marker = matched.group(1)
            if fence is None:
                fence = marker[0]
            elif marker[0] == fence:
                fence = None
            continue
        if fence is None:
            kept.append(line)
    return "\n".join(kept)


def github_slug(heading: str) -> str:
    """Produz a forma de âncora usada pelo renderizador Markdown do GitHub."""
    text = re.sub(r"[`*_~]", "", heading).strip().lower()
    text = re.sub(r"[^\w\- ]", "", text, flags=re.UNICODE)
    return re.sub(r"[ -]+", "-", text)


def anchors(path: Path) -> set[str]:
    values: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        matched = HEADING_PATTERN.match(line)
        if matched:
            values.add(github_slug(matched.group(2)))
    return values


def local_destination(source: Path, target: str) -> tuple[Path, str] | None:
    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc or target.startswith("//"):
        return None
    destination = unquote(parsed.path)
    path = source if not destination else (source.parent / destination).resolve()
    return path, unquote(parsed.fragment)


def main() -> int:
    errors: list[str] = []
    for source in sorted(ROOT.rglob("*.md")):
        if IGNORED_DIRECTORIES.intersection(source.relative_to(ROOT).parts):
            continue
        relative_source = source.relative_to(ROOT)
        text = without_fenced_code(source.read_text(encoding="utf-8"))
        for target in LINK_PATTERN.findall(text):
            result = local_destination(source, target.strip("<>"))
            if result is None:
                continue
            destination, fragment = result
            if not destination.exists():
                errors.append(f"{relative_source}: destino ausente: {target}")
                continue
            if fragment and destination.is_file() and destination.suffix.lower() == ".md":
                if github_slug(fragment) not in anchors(destination):
                    errors.append(f"{relative_source}: âncora ausente: {target}")
    if errors:
        print("Links Markdown locais com problema:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    print("Links Markdown locais: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
