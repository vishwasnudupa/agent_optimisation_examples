from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TECHNIQUES = ROOT / "techniques"
OUTPUT = ROOT / "TECHNIQUE_INDEX.md"


def first_paragraph(text: str) -> str:
    body = re.sub(r"^# .+?\n+", "", text, count=1, flags=re.DOTALL)
    paragraphs = [part.strip().replace("\n", " ") for part in body.split("\n\n") if part.strip()]
    return paragraphs[0] if paragraphs else ""


def main() -> int:
    rows = []
    for folder in sorted(path for path in TECHNIQUES.iterdir() if path.is_dir()):
        readme = folder / "README.md"
        description = first_paragraph(readme.read_text(encoding="utf-8")) if readme.exists() else ""
        rows.append((folder.name, description))

    lines = [
        "# Technique Index",
        "",
        "This file is generated from the technique folder READMEs.",
        "",
        "| Technique | Description |",
        "| --- | --- |",
    ]
    for name, description in rows:
        lines.append(f"| `{name}` | {description} |")

    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
