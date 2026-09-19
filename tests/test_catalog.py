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

    def test_readme_completion_count_matches_catalog(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        match = re.search(r"\*\*Completion: 100% \((\d+) / (\d+) problems\)\*\*", readme)

        self.assertIsNotNone(match)
        completed, total = map(int, match.groups())
        self.assertEqual(completed, total)
        self.assertEqual(total, len(catalog_paths()))

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
