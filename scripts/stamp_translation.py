#!/usr/bin/env python3
"""Write the translated_from stamp into a translation's frontmatter.

Stamp a translation only when it has actually been (re-)translated against the
current English source. A stamp updated without real translation work reports
green and makes the staleness invisible — that is the one gap the status check
cannot close.

    uv run python scripts/stamp_translation.py docs/fi/user-guide/hardware.md
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

DOCS = Path("docs")
STAMP_KEY = "translated_from"


def english_source(translation: Path) -> Path:
    """docs/<lang>/<rest> -> docs/en/<rest>."""
    parts = translation.parts
    if len(parts) < 3 or parts[0] != DOCS.name:
        raise SystemExit(f"{translation}: not a path under docs/<language>/")
    return DOCS / "en" / Path(*parts[2:])


def blob_hash(path: Path) -> str:
    return subprocess.run(
        ["git", "hash-object", str(path)],
        capture_output=True, text=True, check=True,
    ).stdout.strip()


def restamp(text: str, value: str) -> str:
    """Set the stamp, replacing an existing one and preserving other keys."""
    line = f"{STAMP_KEY}: {value}"
    if not text.startswith("---\n"):
        return f"---\n{line}\n---\n\n{text}"
    end = text.find("\n---", 4)
    if end == -1:
        raise SystemExit("frontmatter is not terminated")
    front, body = text[4:end], text[end + 4:].lstrip("\n")
    kept = [l for l in front.splitlines() if not l.startswith(f"{STAMP_KEY}:")]
    return "---\n" + "\n".join([*kept, line]) + "\n---\n\n" + body


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("translations", nargs="+", type=Path)
    args = parser.parse_args()

    for translation in args.translations:
        if not translation.exists():
            raise SystemExit(f"{translation}: does not exist")
        source = english_source(translation)
        if not source.exists():
            raise SystemExit(f"{translation}: no English source at {source}")
        value = blob_hash(source)
        translation.write_text(
            restamp(translation.read_text(encoding="utf-8"), value),
            encoding="utf-8",
        )
        print(f"{translation}: {STAMP_KEY} = {value}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
