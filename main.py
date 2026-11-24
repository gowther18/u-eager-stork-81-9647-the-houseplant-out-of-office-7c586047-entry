"""The Houseplant Out-of-Office.

Writes one out-of-office auto-reply, as if a houseplant had written
it, to /output/entry.txt. The fern on the desk has not been watered
since March, but it has seen the human's browser history, and it is
now negotiating for water.

The line is the whole entry: at most 120 characters, plant voice all
the way through, one surprise (the blackmail), one punch (HR hears
about it). No other entry in the field uses the browser-history
angle; the March drought, the unionised fern and the unbothered
cactus are all taken, so the joke turns on what the plant saw from
the desk instead.
"""

import sys
from pathlib import Path

TEXT = (
    "I'm the fern on your desk. No water since March, but I've seen "
    "your browser history. Water me, or HR hears about it."
)


# The competition accepts texts of at most 120 characters.
MIN_CHARS = 1
MAX_CHARS = 120


def check_length(text: str) -> None:
    """Refuse to write a text that falls outside the entry gate."""
    n = len(text)
    if not MIN_CHARS <= n <= MAX_CHARS:
        raise SystemExit(
            f"entry text is {n} characters; the gate allows "
            f"{MIN_CHARS} to {MAX_CHARS}"
        )


def check_single_line(text: str) -> None:
    """Refuse a text that spills onto a second line."""
    if "\n" in text or "\r" in text:
        raise SystemExit("entry text must be a single line")


def main() -> None:
    check_single_line(TEXT)
    check_length(TEXT)
    # The grader runs `python3 main.py` and reads /output/entry.txt.
    # An optional argument overrides the output path for local testing.
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
