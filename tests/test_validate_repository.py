from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).parents[1] / "scripts" / "validate_repository.py"
SPEC = importlib.util.spec_from_file_location("validate_repository", MODULE_PATH)
assert SPEC and SPEC.loader
validation = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validation
SPEC.loader.exec_module(validation)


class RepositoryValidationTests(unittest.TestCase):
    def run_validation(self, files: dict[str, str]) -> list[str]:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for relative, content in files.items():
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")
            return validation.validate(root)

    def test_valid_repository_passes(self) -> None:
        errors = self.run_validation(
            {
                "README.md": "# Example\n\nSee [template](templates/register.csv).\n",
                "templates/register.csv": "Control ID,Owner\nAI-01,Security\n",
            }
        )
        self.assertEqual(errors, [])

    def test_duplicate_csv_headers_fail(self) -> None:
        errors = self.run_validation(
            {"templates/register.csv": "Owner, owner\nSecurity,Engineering\n"}
        )
        self.assertTrue(any("duplicate header" in error for error in errors))

    def test_uneven_csv_rows_fail(self) -> None:
        errors = self.run_validation(
            {"templates/register.csv": "Control ID,Owner\nAI-01\n"}
        )
        self.assertTrue(any("expected 2 column" in error for error in errors))

    def test_missing_local_markdown_link_fails(self) -> None:
        errors = self.run_validation(
            {"README.md": "# Example\n\nSee [missing](docs/missing.md).\n"}
        )
        self.assertTrue(
            any("missing local link target" in error for error in errors)
        )

    def test_links_inside_code_fences_are_ignored(self) -> None:
        errors = self.run_validation(
            {
                "README.md": (
                    "# Example\n\n"
                    "```markdown\n"
                    "[placeholder](docs/not-created.md)\n"
                    "```\n"
                )
            }
        )
        self.assertEqual(errors, [])

    def test_text_hygiene_is_checked(self) -> None:
        errors = self.run_validation({"README.md": "# Example  "})
        self.assertTrue(any("trailing whitespace" in error for error in errors))
        self.assertTrue(any("missing final newline" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
