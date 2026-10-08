"""Audit the deployable static artifact for broken local links and metadata."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

PUBLIC = Path(__file__).resolve().parents[1] / "public"


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path, self.links, self.ids, self.errors = path, [], set(), []
        self.h1, self.description, self.robots = 0, None, None
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if data.get("id"):
            if data["id"] in self.ids:
                self.errors.append(f"Duplicate id: {data['id']}")
            self.ids.add(data["id"])
        self.h1 += tag == "h1"
        if tag == "meta":
            if data.get("name") == "description":
                self.description = data.get("content")
            if data.get("name") == "robots":
                self.robots = data.get("content")
        if tag == "img" and not data.get("alt"):
            self.errors.append("Image lacks descriptive alt text")
        for attr in ("href", "src"):
            if attr in data:
                self.links.append(data[attr])


def main():
    pages = {path.resolve(): Page(path) for path in PUBLIC.rglob("*.html")}
    errors = []
    for path, page in pages.items():
        if page.h1 != 1 or not page.description or page.robots != "noindex, nofollow":
            page.errors.append("Expected one H1, description and preview noindex metadata")
        for link in page.links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            if target.is_dir():
                target = target / "index.html"
            if not target.is_relative_to(PUBLIC.resolve()) or not target.is_file():
                page.errors.append(f"Broken or escaping local link: {link}")
            elif url.fragment and target in pages and url.fragment not in pages[target].ids:
                page.errors.append(f"Missing fragment: {link}")
        errors.extend(f"{path.relative_to(PUBLIC)}: {message}" for message in page.errors)
    for path in PUBLIC.rglob("*"):
        if path.is_file() and (path.name == "wp-config.php" or path.suffix in {".php", ".sql", ".log", ".zip"}):
            errors.append(f"Forbidden publication file: {path.name}")
    for file in (PUBLIC / "assets/fonts/space-grotesk.woff2",):
        if not file.is_file() or file.read_bytes()[:4] != b"wOF2":
            errors.append(f"Missing or invalid font: {file.name}")
    workflow = (PUBLIC.parent / ".github/workflows/pages.yml").read_text()
    if "pull_request" in workflow or "branches: [main]" not in workflow:
        errors.append("Workflow violates the no-PR-Actions policy")
    if errors:
        print("\n".join(errors))
        return 1
    print(f"PASS: {len(pages)} pages; local assets/fragments, metadata, image alt text, font, publication files and no-PR workflow.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
