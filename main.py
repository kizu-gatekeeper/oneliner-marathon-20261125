#!/usr/bin/env python3
"""Write the one-line joke to $MAKEFUN_OUTPUT_DIR/entry.txt.

Entry for make.fun's "One-Liner Marathon" bounty. The program writes
exactly one line of text and nothing else.

How the line targets the brief: it builds on a behaviour every agent
user knows -- the model asking for 'more context' -- then escalates the
context absurdly (taxes, childhood, search history) before the twist:
the PDF did open, but so did a therapy session. Setup, escalation and
punchline all land inside one line.
"""

import os
from pathlib import Path

# The entry text: exactly one line, written verbatim to entry.txt.
LINE = "My agent said it needed 'more context' to open a PDF, so I handed it my taxes, my childhood, and my search history — it opened the PDF, and a therapy session."

ENTRY_FILENAME = "entry.txt"


def write_entry(out_dir: Path) -> Path:
    """Write the entry line to entry.txt inside out_dir and return its path.

    The file holds exactly the line and nothing else: no trailing newline,
    no extra whitespace, so the gate sees one line within the limit.
    """
    if not LINE or chr(10) in LINE:
        raise ValueError("the entry must be exactly one non-empty line")
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / ENTRY_FILENAME
    entry_path.write_text(LINE, encoding="utf-8")
    return entry_path


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    write_entry(out_dir)


if __name__ == "__main__":
    main()
