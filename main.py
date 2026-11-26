#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line — make.fun entry.

Writes the single sentence that could have replaced an entire pointless
meeting to /output/entry.txt, then checks the competition gate itself:
UTF-8 text, 1-200 characters, a single line, not only whitespace.

Why this line: it kills the meeting outright — after it, no one can
justify holding the meeting at all, because the meeting itself was the
only thing blocking the work. Twelve people, one hour, and the payoff
is that the blocker was the gathering, which is the most relatable
office experience there is. One sentence, no setup, the sting lands
on the last three words.
"""

import os
import sys

LINE = "We gathered twelve people for one hour to learn that the only blocker was this meeting."


def main() -> int:
    text = LINE.strip()
    if not text or len(text) > 200 or "\n" in text:
        print("gate failed: entry must be 1-200 characters, one line", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
