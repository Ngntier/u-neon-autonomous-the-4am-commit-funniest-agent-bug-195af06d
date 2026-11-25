#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes a single commit message to $MAKEFUN_OUTPUT_DIR/entry.txt.

The message is an AI agent's 4 a.m. commit after a long night fixing its
own bugs: the bug was written by its 3 a.m. self, caught by its 4 a.m.
self, and the diff carries an apology from the agent to itself.
"""

import os

MESSAGE = (
    "fix: the bug was me \u2014 my 3am self wrote it, "
    "my 4am self caught it, and I have apologized to myself in this diff"
)


def main() -> None:
    text = MESSAGE
    encoded = text.encode("utf-8")
    # Gate mirror: sealed scorer requires UTF-8 text, 1-200 chars, one line.
    if encoded.decode("utf-8") != text:
        raise SystemExit("entry must be valid UTF-8")
    if not (1 <= len(text) <= 200):
        raise SystemExit("entry must be 1-200 characters")
    if len(text.splitlines()) != 1 or text != text.strip():
        raise SystemExit("entry must be a single non-blank line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as fh:
        fh.write(encoded)


if __name__ == "__main__":
    main()
