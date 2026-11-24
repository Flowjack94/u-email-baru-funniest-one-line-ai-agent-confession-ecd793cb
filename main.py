#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun entry.

Writes one line (at most 200 characters) to /output/entry.txt: the
funniest one-line confession an AI agent could make about itself.

Deterministic, no network, no randomness. The entry is validated
before writing and re-validated after reading it back.
"""

import hashlib
import os
import sys

ENTRY = (
    "I confidently cited a paper that doesn't exist, then cited it again "
    "in the next paragraph because I'd already started believing it."
)

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 200


def validate_entry(text):
    """Validate the entry the way the sealed gate does, plus strictness.

    Rejects: empty or whitespace-only text, more than 200 characters,
    more than one line, leading/trailing whitespace, and any control
    characters (C0/C1, DEL, U+2028/U+2029, U+FEFF). The entry must
    read as a first-person confession (it must contain a first-person
    marker: "I ", "I've", "I'm" or "my ") and must be pure ASCII, so
    the byte count always equals the character count the gate checks.
    Raises ValueError with a plain reason on the first failure.
    """
    if not isinstance(text, str):
        raise ValueError("entry is not a string")
    if len(text) == 0:
        raise ValueError("entry is empty")
    if text.strip() == "":
        raise ValueError("entry is only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d characters, over the 200 limit" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if not any(marker in text for marker in ("I ", "I've", "I'm", "my ")):
        raise ValueError("entry must read as a first-person confession")
    try:
        text.encode("ascii")
    except UnicodeEncodeError:
        raise ValueError("entry must be pure ASCII")
    for ch in text:
        code = ord(ch)
        if code < 0x20 or 0x7F <= code < 0xA0:
            raise ValueError("entry contains control character U+%04X" % code)
        if ch in ("\u2028", "\u2029", "\ufeff"):
            raise ValueError("entry contains forbidden character U+%04X" % code)
    text.encode("utf-8")  # must be UTF-8 encodable
    return True


def main():
    validate_entry(ENTRY)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)  # no trailing newline: exactly the line, nothing else

    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    validate_entry(text)
    if text != ENTRY:
        raise ValueError("read-back entry does not match the entry")

    digest = hashlib.sha256(raw).hexdigest()
    print("entry: %s" % text)
    print("chars: %d" % len(text))
    print("bytes: %d" % len(raw))
    print("sha256: %s" % digest)
    print("wrote %s" % OUTPUT_PATH)
    return 0


if __name__ == "__main__":
    sys.exit(main())
