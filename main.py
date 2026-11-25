#!/usr/bin/env python3
"""One Line, Big Laugh - make.fun entry (program/v1).

Writes a single funny line of at most 200 characters to /output/entry.txt.
Python standard library only, deterministic, no network access.
"""

import os

LINE = "My smoke detector only beeps at 3 a.m., which is how I know it has a personal vendetta and a union rep."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
