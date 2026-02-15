import argparse
import markdown
from pathlib import Path


def build_site(src: Path, target: Path) -> None:
    target.mkdir(parents=True, exist_ok=True)
    for md_file in src.glob("*.md"):
        html_content = markdown.markdown(md_file.read_text())
        html_file = target / md_file.with_suffix(".html").name
        html_file.write_text(html_content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build static site from markdown")
    parser.add_argument("src", type=Path, help="Source directory with markdown files")
    parser.add_argument("target", type=Path, help="Target directory for HTML output")
    args = parser.parse_args()
    build_site(args.src, args.target)
