#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse.

Writes one funny one-line excuse from a robot vacuum for missing a spot
to <MAKEFUN_OUTPUT_DIR>/entry.txt (default /output).
Stdlib only.
"""

import os

EXCUSE = (
    "I mapped that dust bunny as a new roommate, so legally I can't "
    "vacuum him without a 30-day eviction notice."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
