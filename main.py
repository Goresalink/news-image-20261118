#!/usr/bin/env python3
"""News image entry for make.fun bounty news-image-20261118.

Sums up the world news of Wednesday 18 November 2026 in one image:
the Kerch (Crimean) Bridge after Ukraine's strike on 17 November 2026,
its road arch collapsed into the Kerch Strait while the railway arch still
stands, on the eve of the Trump-Xi-Putin meeting at the APEC summit in
Shenzhen. Photo: Crimean monitoring channels via UNITED24 Media / The War
Zone, as published 18 November 2026.

The program is fully offline and deterministic: it copies the image bundled
in this repository to /output/entry.png, so every run writes identical bytes.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "news.jpg")
OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.png")


def main() -> int:
    if not os.path.isfile(SOURCE):
        print(f"missing bundled image: {SOURCE}", file=sys.stderr)
        return 1
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT_PATH)
    size = os.path.getsize(OUTPUT_PATH)
    print(f"wrote {OUTPUT_PATH} ({size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
