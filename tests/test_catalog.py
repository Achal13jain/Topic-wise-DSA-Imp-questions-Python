"""Repository-wide checks for catalog consistency and Python syntax."""

from __future__ import annotations

import ast
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOPIC_PATTERN = re.compile(r'folder:"([^"]+)".*?p:\[(.*?)\]\}', re.DOTALL)
FILE_PATTERN = re.compile(r'\["[^"]+","([^"]+\.py)"')


def catalog_paths() -> list[Path]:
    """Return every solution path declared in the website catalog."""
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    return [
        ROOT / folder / filename
        for folder, body in TOPIC_PATTERN.findall(html)
        for filename in FILE_PATTERN.findall(body)
    ]


class CatalogTests(unittest.TestCase):
    """Keep source files, the website, and README counts synchronized."""

    def test_every_catalog_entry_exists_and_is_unique(self) -> None:
        paths = catalog_paths()
        relative_paths = [path.relative_to(ROOT) for path in paths]

        self.assertEqual(len(relative_paths), len(set(relative_paths)))
        self.assertEqual([], [str(path) for path in paths if not path.is_file()])

    def test_every_solution_is_listed_in_catalog(self) -> None:
        listed = {path.relative_to(ROOT) for path in catalog_paths()}
        on_disk = {
            path.relative_to(ROOT)
            for topic in ROOT.iterdir()
            if topic.is_dir() and re.match(r"^\d+\.", topic.name)
            for path in topic.glob("*.py")
            if path.name != "TreeNode.py"
        }

        self.assertEqual(on_disk, listed)

    def test_readme_and_roadmap_progress_match_catalog(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        roadmap = (ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        readme_match = re.search(
            r"\*\*Core 120 progress:\*\* (\d+) / (\d+) problems",
            readme,
        )
        roadmap_match = re.search(r"\*\*Current progress: (\d+) / (\d+) problems\*\*", roadmap)

        self.assertIsNotNone(readme_match)
        self.assertIsNotNone(roadmap_match)
        self.assertEqual(readme_match.groups(), roadmap_match.groups())
        completed, target = map(int, readme_match.groups())
        self.assertEqual(completed, len(catalog_paths()))
        self.assertEqual(120, target)

    def test_website_does_not_link_to_raw_repository_documents(self) -> None:
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        relative_documents = re.findall(r'href="\./[^\"]+(?:\.md|LICENSE)"', html)

        self.assertEqual([], relative_documents)

    def test_direct_document_urls_redirect_to_rendered_github_pages(self) -> None:
        redirects = (ROOT / "_redirects").read_text(encoding="utf-8")
        for document in (
            "ROADMAP.md",
            "PATTERNS.md",
            "DATA_STRUCTURES.md",
            "README.md",
            "CONTRIBUTING.md",
            "LICENSE",
        ):
            with self.subTest(document=document):
                self.assertRegex(
                    redirects,
                    rf"(?m)^/{re.escape(document)} https://github\.com/.+/blob/main/{re.escape(document)} 302$",
                )

    def test_public_files_use_current_repository_name(self) -> None:
        old_name = "Topic-wise-DSA-Imp-questions-Python"
        new_name = "python-dsa-interview-prep"

        for relative_path in ("index.html", "README.md", "_redirects"):
            with self.subTest(path=relative_path):
                content = (ROOT / relative_path).read_text(encoding="utf-8")
                self.assertNotIn(old_name, content)
                self.assertIn(new_name, content)

    def test_all_python_files_parse(self) -> None:
        for path in ROOT.rglob("*.py"):
            if ".git" in path.parts:
                continue
            with self.subTest(path=path.relative_to(ROOT)):
                ast.parse(
                    path.read_text(encoding="utf-8-sig"),
                    filename=str(path),
                    feature_version=(3, 9),
                )


if __name__ == "__main__":
    unittest.main()
