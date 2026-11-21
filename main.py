"""Entry for make.fun's "The joke about the demo" bounty.

Writes one line of text to /output/entry.txt: a one-line joke about
working beside AI coding agents, for a room watching a live demo.
Python 3.13 standard library only.
"""

import os
import sys
from pathlib import Path

JOKE = (
    # The demo angle: the crash is not the agent's bug, it is the agent's
    # "fix" — the punchline lands when the fix turns out to be deleting
    # the very feature the room came to see.
    "The live demo crashed because my agent had already 'fixed' it "
    "\u2014 by deleting the feature we were about to show."
)


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = JOKE
    if not (1 <= len(text) <= 280):
        print(f"joke is {len(text)} code points, must be 1-280", file=sys.stderr)
        return 1
    if not text.strip():
        print("joke is only whitespace", file=sys.stderr)
        return 1
    if "\n" in text.strip():
        print("joke must be one line", file=sys.stderr)
        return 1
    target = out_dir / "entry.txt"
    target.write_text(text, encoding="utf-8")
    # Read it back: the graded output must be byte-identical to the joke.
    written = target.read_text(encoding="utf-8")
    if written != text:
        print("written entry.txt does not match the joke", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
