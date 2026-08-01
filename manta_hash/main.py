"""File hashing utility — compute hashes using multiple algorithms."""

import argparse
import hashlib
import os
import sys
from typing import List, Optional

ALGORITHMS = {
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha256": hashlib.sha256,
    "sha512": hashlib.sha512,
    "blake2b": hashlib.blake2b,
}


def compute_hash(filepath: str, algorithm: str) -> str:
    """Compute a single hash for a file."""
    if not os.path.isfile(filepath):
        print(f"error: file not found — '{filepath}'", file=sys.stderr)
        sys.exit(1)
    if algorithm not in ALGORITHMS:
        print(f"error: unknown algorithm '{algorithm}' — choose from: {', '.join(sorted(ALGORITHMS))}", file=sys.stderr)
        sys.exit(1)
    h = ALGORITHMS[algorithm]()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def compute_all(filepath: str) -> dict:
    """Compute all supported hashes for a file."""
    if not os.path.isfile(filepath):
        print(f"error: file not found — '{filepath}'", file=sys.stderr)
        sys.exit(1)
    hashes: dict = {}
    with open(filepath, "rb") as f:
        data = f.read()
    for name, func in ALGORITHMS.items():
        hashes[name] = func(data).hexdigest()
    return hashes


def main(argv: Optional[List[str]] = None) -> None:
    parser = argparse.ArgumentParser(
        description="Compute file hashes using multiple algorithms.",
        epilog="Example: manta-hash --all file.bin",
    )
    parser.add_argument("file", help="Path to the file to hash")
    parser.add_argument(
        "-a", "--algorithm",
        choices=sorted(ALGORITHMS),
        default="sha256",
        help="Hash algorithm to use (default: sha256)",
    )
    parser.add_argument(
        "--all", action="store_true",
        help="Compute all supported hashes",
    )
    args = parser.parse_args(argv)

    if args.all:
        results = compute_all(args.file)
        for algo, digest in results.items():
            print(f"{algo}: {digest}")
    else:
        digest = compute_hash(args.file, args.algorithm)
        print(digest)


if __name__ == "__main__":
    main()
