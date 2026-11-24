#!/usr/bin/env python3
"""One Emoji, One Dream Vacation.

Reads the single chosen emoji from emoji.txt (shipped in this repo) and
writes it, byte for byte, to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output) so the judge can read it. Pure standard library.
"""

import os
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "emoji.txt"), "rb") as handle:
        raw = handle.read()

    text = raw.decode("utf-8")
    if not (1 <= len(text) <= 8):
        print(f"emoji must be 1-8 characters, got {len(text)}", file=sys.stderr)
        return 1
    if not text.strip():
        print("emoji must not be only whitespace", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "wb") as handle:
        handle.write(raw)

    with open(target, "rb") as handle:
        written = handle.read()
    if written != raw:
        print("entry.txt does not match emoji.txt", file=sys.stderr)
        return 1

    print(f"Wrote {len(raw)} bytes ({len(text)} character) to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
