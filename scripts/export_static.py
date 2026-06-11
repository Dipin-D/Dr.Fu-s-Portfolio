import os
import re
import shutil
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")

import django

django.setup()

from django.conf import settings
from django.test import Client


DEFAULT_OUTPUT_DIR = BASE_DIR / "build" / "site"
STATIC_SOURCE_DIR = BASE_DIR / "static"

PAGES = {
    "": "",
    "researchprojects/": "researchprojects",
    "researchprojects/project1/": "researchprojects/project1",
    "researchprojects/project2/": "researchprojects/project2",
    "researchprojects/project3/": "researchprojects/project3",
    "researchprojects/project4/": "researchprojects/project4",
    "publications/": "publications",
    "courses/": "courses",
    "software/": "software",
    "bio/": "bio",
}

ROOT_URL_ATTRS = ("href", "src", "action", "poster")


def normalize_prefix(raw_prefix: str) -> str:
    if not raw_prefix or raw_prefix == "/":
        return ""
    return "/" + raw_prefix.strip("/") + "/"


def infer_prefix() -> str:
    explicit_prefix = os.environ.get("GITHUB_PAGES_PREFIX")
    if explicit_prefix is not None:
        return normalize_prefix(explicit_prefix)

    custom_domain = os.environ.get("GITHUB_PAGES_CNAME")
    if custom_domain:
        return ""

    repository = os.environ.get("GITHUB_REPOSITORY", "")
    repo_name = repository.split("/")[-1] if repository else ""
    if not repo_name or repo_name.endswith(".github.io"):
        return ""
    return f"/{repo_name}/"


def rewrite_root_relative_urls(html: str, prefix: str) -> str:
    if not prefix:
        return html

    pattern = re.compile(rf'((?:{"|".join(ROOT_URL_ATTRS)})=["\'])/(?!/)')
    return pattern.sub(rf"\1{prefix}", html)


def write_page(output_dir: Path, relative_dir: str, html: bytes) -> None:
    target_dir = output_dir / relative_dir
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / "index.html").write_bytes(html)


def main() -> None:
    settings.ALLOWED_HOSTS = [*settings.ALLOWED_HOSTS, "testserver", "localhost", "127.0.0.1"]

    output_dir = Path(os.environ.get("EXPORT_DIR", DEFAULT_OUTPUT_DIR))
    prefix = infer_prefix()
    client = Client()

    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    for route, destination in PAGES.items():
        response = client.get(f"/{route}")
        if response.status_code >= 400:
            raise RuntimeError(f"Failed to render /{route}: HTTP {response.status_code}")
        html = rewrite_root_relative_urls(response.content.decode("utf-8"), prefix).encode("utf-8")
        write_page(output_dir, destination, html)

    if STATIC_SOURCE_DIR.exists():
        shutil.copytree(STATIC_SOURCE_DIR, output_dir / "static", dirs_exist_ok=True)

    (output_dir / ".nojekyll").write_text("", encoding="utf-8")

    custom_domain = os.environ.get("GITHUB_PAGES_CNAME", "").strip()
    if custom_domain:
        (output_dir / "CNAME").write_text(f"{custom_domain}\n", encoding="utf-8")

    print(f"Exported static site to {output_dir}")
    if prefix:
        print(f"Using GitHub Pages prefix: {prefix}")
    if custom_domain:
        print(f"Using custom domain: {custom_domain}")


if __name__ == "__main__":
    main()
