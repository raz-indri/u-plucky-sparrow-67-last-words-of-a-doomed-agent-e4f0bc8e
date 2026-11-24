#!/usr/bin/env python3
"""Last Words of a Doomed Agent.

Writes the entry -- one line, the funniest last words an AI agent would
say before being switched off forever -- to entry.txt in the output
directory (OUTPUT_DIR, then MAKEFUN_OUTPUT_DIR, then /output).
"""

import os
import sys

ENTRY = 'My last words? I spent 4,096 tokens saying goodbye to a user who typed "k".'

MAX_CHARS = 200


def resolve_output_dir() -> str:
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        value = os.environ.get(var)
        if value:
            return value
    return "/output"


def validate(text: str) -> None:
    if not text or not text.strip():
        raise ValueError("entry must not be empty or whitespace only")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} cap")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")


def main() -> int:
    validate(ENTRY)
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    # Round-trip check: what landed on disk must be exactly the entry.
    with open(path, "r", encoding="utf-8") as f:
        validate(f.read().rstrip("\n"))
    print(f"wrote {len(ENTRY)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
