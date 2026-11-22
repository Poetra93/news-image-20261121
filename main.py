#!/usr/bin/env python3
"""news-image-20261121 entrypoint.

Copies the pre-drawn front page (front-page.png, drawn by compose.py
from verified news of Saturday 21 November 2026) to the output directory
as entry.png, after validating that it is a well-formed 1024x1024 PNG
within the 1 MiB limit. Standard library only; no network.
"""

import hashlib
import os
import shutil
import struct
import sys
import zlib

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "front-page.png")
MAX_BYTES = 1048576
MAX_DIM = 1024


def validate_png(path):
    """Check the PNG signature, IHDR dimensions and chunk checksums."""
    with open(path, "rb") as fh:
        data = fh.read()
    if len(data) > MAX_BYTES:
        raise ValueError("front-page.png exceeds 1 MiB: %d bytes" % len(data))
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG file")
    if len(data) < 33 or data[12:16] != b"IHDR":
        raise ValueError("missing IHDR chunk")
    width, height = struct.unpack(">II", data[16:24])
    if width > MAX_DIM or height > MAX_DIM:
        raise ValueError("image too large: %dx%d" % (width, height))
    # Walk the chunks and verify every CRC.
    pos = 8
    while pos < len(data):
        if pos + 8 > len(data):
            raise ValueError("truncated chunk header")
        length = struct.unpack(">I", data[pos:pos + 4])[0]
        ctype = data[pos + 4:pos + 8]
        end = pos + 8 + length + 4
        if end > len(data):
            raise ValueError("truncated %s chunk" % ctype.decode("latin-1"))
        crc_stored = struct.unpack(">I", data[end - 4:end])[0]
        crc_actual = zlib.crc32(ctype + data[pos + 8:pos + 8 + length]) & 0xFFFFFFFF
        if crc_stored != crc_actual:
            raise ValueError("bad CRC in %s chunk" % ctype.decode("latin-1"))
        pos = end
        if ctype == b"IEND":
            break
    if pos != len(data):
        raise ValueError("trailing bytes after IEND")
    return width, height, hashlib.sha256(data).hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    width, height, digest = validate_png(SRC)
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dest)
    # Confirm the copy is byte-identical to the validated source.
    with open(dest, "rb") as fh:
        copied = fh.read()
    copied_digest = hashlib.sha256(copied).hexdigest()
    if copied_digest != digest:
        raise ValueError("copied entry.png differs from front-page.png")
    print("wrote %s (%dx%d, %d bytes, sha256 %s)"
          % (dest, width, height, len(copied), copied_digest))
    return 0


if __name__ == "__main__":
    sys.exit(main())
