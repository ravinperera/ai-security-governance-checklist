#!/usr/bin/env python3
"""Run dependency-free quality checks for this documentation and template repository."""

from __future__ import annotations

import argparse
import csv
import re
import subprocess
import urllib.parse
from pathlib import Path
from typing import Iterable

TEXT_SUFFIXES = {".md", ".csv", ".json", ".yml", ".yaml"}
LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def repository_files(root: Path) -> list[Path]:
    try:
        result = subprocess.run(
            ["git", "-C", str(root), "ls-files", "-z"],
            check=True,
            capture_output=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return sorted(
            path
            for path in root.rglob("*")
            if path.is_file() and ".git" not in path.parts
        )

    return [
        root / raw.decode("utf-8")
        for raw in result.stdout.split(b"\0")
        if raw
    ]


def check_text_file(path: Path, root: Path) -> list[str]:
    relative = path.relative_to(root)
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        return [f"{relative}: invalid UTF-8 ({exc})"]

    errors: list[str] = []
    if text and not text.endswith("\n"):
        errors.append(f"{relative}: missing final newline")

    for number, line in enumerate(text.splitlines(), start=1):
        if line.rstrip(" \t") != line:
            errors.append(f"{relative}:{number}: trailing whitespace")

    return errors


def check_csv(path: Path, root: Path) -> list[str]:
    relative = path.relative_to(root)
    try:
        with path.open(newline="", encoding="utf-8") as handle:
            rows = list(csv.reader(handle))
    except (csv.Error, UnicodeDecodeError) as exc:
        return [f"{relative}: invalid CSV ({exc})"]

    if not rows:
        return [f"{relative}: CSV is empty"]

    header = rows[0]
    errors: list[str] = []
    if not header or all(not value.strip() for value in header):
        return [f"{relative}: CSV header is empty"]

    blank_headers = [
        str(index + 1) for index, value in enumerate(header) if not value.strip()
    ]
    if blank_headers:
        errors.append(
            f"{relative}: blank header column(s): {', '.join(blank_headers)}"
        )

    normalized = [value.strip().casefold() for value in header if value.strip()]
    duplicates = sorted(
        {value for value in normalized if normalized.count(value) > 1}
    )
    if duplicates:
        errors.append(f"{relative}: duplicate header(s): {', '.join(duplicates)}")

    expected = len(header)
    for number, row in enumerate(rows[1:], start=2):
        if not row or all(not value.strip() for value in row):
            continue
        if len(row) != expected:
            errors.append(
                f"{relative}:{number}: expected {expected} column(s), found {len(row)}"
            )

    return errors


def markdown_targets(text: str) -> Iterable[tuple[int, str]]:
    in_fence = False
    for number, line in enumerate(text.splitlines(), start=1):
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for match in LINK_PATTERN.finditer(line):
            yield number, match.group(1).strip()


def check_markdown_links(path: Path, root: Path) -> list[str]:
    relative = path.relative_to(root)
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    for number, raw_target in markdown_targets(text):
        target = raw_target
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1].strip()

        lowered = target.casefold()
        if (
            not target
            or target.startswith("#")
            or lowered.startswith(
                ("http://", "https://", "mailto:", "tel:", "data:")
            )
            or "${{" in target
        ):
            continue

        target = urllib.parse.unquote(target.split("#", 1)[0].split("?", 1)[0])
        if not target:
            continue

        resolved = (path.parent / target).resolve()
        try:
            resolved.relative_to(root.resolve())
        except ValueError:
            errors.append(
                f"{relative}:{number}: local link escapes repository: {raw_target}"
            )
            continue

        if not resolved.exists():
            errors.append(
                f"{relative}:{number}: missing local link target: {raw_target}"
            )

    return errors


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []

    for path in repository_files(root):
        if not path.exists() or path.suffix.casefold() not in TEXT_SUFFIXES:
            continue
        errors.extend(check_text_file(path, root))
        if (
            path.suffix.casefold() == ".csv"
            and "templates" in path.relative_to(root).parts
        ):
            errors.extend(check_csv(path, root))
        if path.suffix.casefold() == ".md":
            errors.extend(check_markdown_links(path, root))

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "root",
        nargs="?",
        default=".",
        type=Path,
        help="Repository root to validate (default: current directory)",
    )
    args = parser.parse_args()

    errors = validate(args.root)
    if errors:
        for error in errors:
            print(error)
        print(f"repository validation failed with {len(errors)} issue(s).")
        return 1

    print("repository validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
