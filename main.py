#!/usr/bin/env python3
"""One-Line Laugh Sprint: write one original funny line about everyday
life to /output/entry.txt. Pure stdlib, deterministic, no network."""

import os

LINE = (
    "My smartwatch congratulated me on 10,000 steps \u2014 "
    "I'd spent the whole hour looking for the TV remote."
)


def main():
    # Keep it tight: the judge tie-breaks on fewer bytes.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
