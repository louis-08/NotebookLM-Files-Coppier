#!/usr/bin/env python3
"""
flatten_folder.py - Copy all files from a folder tree into a single flat folder.

Usage:
    python flatten_folder.py <source_folder> <destination_folder>

The source folder is left unchanged. All files (from all subfolders, recursively)
are copied into destination_folder with no subdirectory structure.
If two files share the same name, a numeric suffix (_1, _2, ...) is appended.
"""

import sys
import shutil
from pathlib import Path


def flatten_folder(src: Path, dst: Path) -> None:
    if not src.exists() or not src.is_dir():
        print(f"Error: source '{src}' does not exist or is not a folder.")
        sys.exit(1)

    dst.mkdir(parents=True, exist_ok=True)

    copied = 0
    skipped = 0

    for file in src.rglob("*"):
        if not file.is_file():
            continue

        dest_file = dst / file.name

        # Resolve name collision
        if dest_file.exists():
            stem = file.stem
            suffix = file.suffix
            counter = 1
            while dest_file.exists():
                dest_file = dst / f"{stem}_{counter}{suffix}"
                counter += 1
            print(f"  Renamed: {file.name} -> {dest_file.name}  (collision)")
            skipped += 1

        shutil.copy2(file, dest_file)
        copied += 1

    print(f"\nDone. {copied} file(s) copied to '{dst}'.")
    if skipped:
        print(f"  {skipped} file(s) were renamed due to name collisions.")


def main():
    if len(sys.argv) != 3:
        print("Usage: python flatten_folder.py <source_folder> <destination_folder>")
        sys.exit(1)

    src = Path(sys.argv[1])
    dst = Path(sys.argv[2])

    if dst.resolve() == src.resolve():
        print("Error: source and destination must be different folders.")
        sys.exit(1)

    print(f"Source:      {src}")
    print(f"Destination: {dst}")
    print()

    flatten_folder(src, dst)


if __name__ == "__main__":
    main()
