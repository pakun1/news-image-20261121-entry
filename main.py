#!/usr/bin/env python3
"""Publish the front-page image for the 21 November 2026 news contest.

The entry is a single rendered picture, entry.png, held beside this
program in the repository. Running this program places a copy of that
picture at the location the grader reads, /output/entry.png, or at
$MAKEFUN_OUTPUT_DIR/entry.png when that variable is set.

Standard library only. No network, no randomness, no clock reads:
every run writes the same bytes.
"""

import os
import shutil
from pathlib import Path


def entry_image() -> Path:
    """Path of the front-page picture shipped in this repository."""
    return Path(__file__).resolve().parent / "entry.png"


def output_dir() -> Path:
    """Directory the grader reads, honouring MAKEFUN_OUTPUT_DIR."""
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if chosen:
        return Path(chosen)
    return Path("/output")


def main() -> None:
    source = entry_image()
    if not source.is_file():
        raise SystemExit(f"missing entry image: {source}")
    target_dir = output_dir()
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / "entry.png"
    shutil.copyfile(source, target)
    if target.stat().st_size != source.stat().st_size:
        raise SystemExit(f"incomplete copy: {target}")
    size = target.stat().st_size
    print(f"wrote {target} ({size} bytes)")


if __name__ == "__main__":
    main()
