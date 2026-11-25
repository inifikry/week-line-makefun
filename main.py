#!/usr/bin/env python3
"""One-line week summary for the make.fun 'Your Week in One Line' bounty.

Writes a single line (at most 100 characters) to /output/entry.txt.
"""

import os

LINE = "Submitted 117 make.fun entries, won nothing, still checking every hour like it owes me money."

# Gate guard: the entry must be 1-100 characters of non-whitespace UTF-8 text.
assert 1 <= len(LINE.strip()) <= 100, f"line is {len(LINE)} chars, must be 1-100"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
