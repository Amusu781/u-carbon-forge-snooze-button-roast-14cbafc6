"""Snooze Button Roast: write one roast line to /output/entry.txt."""

import shutil
from pathlib import Path

ENTRY = (
    "My alarm went off at 6 AM on a Saturday, and I realised it has never "
    "once asked what day it is \u2014 it just assumes I'm employed."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MAX_CHARS = 200


def main() -> None:
    # The gate wants exactly one line of 1-200 characters, not only whitespace.
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    if not 1 <= len(ENTRY.strip()) <= MAX_CHARS:
        raise ValueError("entry must be 1-200 characters")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    # Clear only the output directory's contents, never the directory itself.
    for old in OUTPUT_DIR.iterdir():
        if old.is_dir() and not old.is_symlink():
            shutil.rmtree(old)
        else:
            old.unlink()
    OUTPUT_FILE.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
