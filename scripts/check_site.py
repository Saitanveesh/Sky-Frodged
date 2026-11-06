#!/usr/bin/env python3
"""Basic dependency-free static-site source checks (not a browser test)."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PAGES = [
    "index.html", "academy.html", "anatomy.html", "blueprint.html",
    "builder.html", "handbook.html", "maps.html", "ops.html",
    "pid.html", "platforms.html", "tools.html",
]

class LocalReferences(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ("href", "src"):
            value = attrs.get(key)
            if value:
                self.refs.append((tag, key, value))

def main():
    missing = []
    for page in PAGES:
        f = ROOT / page
        if not f.is_file():
            missing.append(f"{page}: missing page")
            continue
        parser = LocalReferences()
        parser.feed(f.read_text(encoding="utf-8"))
        for tag, attr, ref in parser.refs:
            if ref.startswith(("#", "//", "data:", "mailto:", "tel:", "javascript:")):
                continue
            url = urlsplit(ref)
            if url.scheme or url.netloc:
                continue
            path = unquote(url.path)
            if not path:
                continue
            target = (ROOT / path.lstrip("/") if path.startswith("/") else f.parent / path).resolve()
            if not target.is_relative_to(ROOT) or not target.exists():
                missing.append(f"{page}: {tag} {attr}={ref}")
    if missing:
        print("Missing or unsafe local references:")
        for item in missing:
            print(f" - {item}")
        raise SystemExit(1)
    print(f"PASS: {len(PAGES)} HTML pages and local references checked.")

if __name__ == "__main__":
    main()
