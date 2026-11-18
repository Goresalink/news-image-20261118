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

Output contract: /output/entry.png, 83,897 bytes (JPEG, 1024x628), well
under the 1 MiB / 1024x1024 limit. After writing, the program verifies that
the output file exists, is within the size limit, and matches the bundled
image byte for byte in size; it exits non-zero if the bundled image is
missing or the output cannot be verified.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "news.jpg")
OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.png")
MAX_OUTPUT_BYTES = 1_048_576  # contest limit: 1 MiB


def main() -> int:
    if not os.path.isfile(SOURCE):
        print(f"missing bundled image: {SOURCE}", file=sys.stderr)
        return 1
    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
    except OSError as exc:
        print(f"cannot create output directory {OUTPUT_DIR}: {exc}", file=sys.stderr)
        return 1
    if not os.path.isdir(OUTPUT_DIR):
        print(f"output path is not a directory: {OUTPUT_DIR}", file=sys.stderr)
        return 1
    shutil.copyfile(SOURCE, OUTPUT_PATH)
    if not os.path.isfile(OUTPUT_PATH):
        print(f"output was not written: {OUTPUT_PATH}", file=sys.stderr)
        return 1
    size = os.path.getsize(OUTPUT_PATH)
    if size > MAX_OUTPUT_BYTES:
        print(f"output exceeds 1 MiB limit: {size} bytes", file=sys.stderr)
        return 1
    if size != os.path.getsize(SOURCE):
        print("output size differs from bundled image", file=sys.stderr)
        return 1
    print(f"wrote {OUTPUT_PATH} ({size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
