"""One-Liner Marathon entry.

This program writes a single marathon one-liner about an agent.
The joke escalates in one breath: the agent asks for more context
just to open a PDF, the narrator hands over an entire life, and the
payoff lands when the agent opens both the file and a therapy
session. One line, no setup paragraph, punchline at the very end.

Running the module writes the line to ``entry.txt`` in the output
directory chosen by ``MAKEFUN_OUTPUT_DIR`` (default ``/output``).
"""

import os
from pathlib import Path

LINE = "My agent said it needed 'more context' to open a PDF, so I handed it my taxes, my childhood, and my search history — it opened the PDF, and a therapy session."

ENTRY_FILENAME = "entry.txt"


def validate_line(line):
    """Reject an entry that is empty or carries a newline."""
    if not line:
        raise ValueError("entry line must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")


def write_entry(out_dir):
    """Validate the line and write it to ``entry.txt`` in out_dir."""
    validate_line(LINE)
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    target = out_path / ENTRY_FILENAME
    target.write_text(LINE, encoding="utf-8")
    return target


def resolve_out_dir():
    """Return the output directory from the environment."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    write_entry(resolve_out_dir())


if __name__ == "__main__":
    main()
