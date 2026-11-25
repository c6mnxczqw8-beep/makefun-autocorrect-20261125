#!/usr/bin/env python3
"""Entry program for Funniest Autocorrect Fail.

Writes one line (under 200 characters) to the output directory
(MAKEFUN_OUTPUT_DIR, default /output) as entry.txt, that READS
as a hilarious autocorrect fail: a message whose intended and
received meanings are separated by one small, fatal correction.
"""

import os

LINE = "I will defiantly be there at 8!! *definitely"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
