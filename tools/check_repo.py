"""Lightweight repository checks. Copyright (c) 2026 Mohamed Dawood."""
from pathlib import Path
import ast
import re
import sys

root = Path(__file__).resolve().parents[1]
errors = []

for path in root.rglob("*.py"):
    if ".git" in path.parts:
        continue
    try:
        ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except (SyntaxError, UnicodeDecodeError) as exc:
        errors.append(f"Python parse failure: {path.relative_to(root)}: {exc}")

private_ip = re.compile(r"(?<![0-9.])(?:10\.\d{1,3}\.\d{1,3}\.\d{1,3}|192\.168\.\d{1,3}\.\d{1,3}|172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3})(?![0-9.])")
for path in [*root.rglob("*.py"), *root.rglob("*.md")]:
    if ".git" not in path.parts and private_ip.search(path.read_text(encoding="utf-8")):
        errors.append(f"Private IP found: {path.relative_to(root)}")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print("All checks passed.")
