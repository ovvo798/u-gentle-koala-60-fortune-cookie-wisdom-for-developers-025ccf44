#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers.

Writes one original line of fortune-cookie wisdom for a software
developer to /output/entry.txt. Python 3.13, standard library only.
"""

import os

FORTUNE = (
    "Your future self is already debugging this at 2 a.m.; "
    "leave them a map, not a mystery."
)


def main() -> None:
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
