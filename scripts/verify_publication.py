#!/usr/bin/env python3
"""
Verify the integrity of the ExergyNet V5 white paper PDF.

Usage:
    python scripts/verify_publication.py

Checks:
    - paper/EXERGYNET_WHITEPAPER_PUBLIC_V5.pdf exists
    - SHA-256 matches the published canonical hash
    - paper/SHA256SUMS is consistent

Exit codes:
    0 = all checks pass
    1 = one or more checks failed
"""

import hashlib
import os
import sys

PAPER_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "paper",
    "EXERGYNET_WHITEPAPER_PUBLIC_V5.pdf",
)

SHA256SUMS_PATH = os.path.join(os.path.dirname(PAPER_PATH), "SHA256SUMS")

CANONICAL_HASH = (
    "416974f1d7c1f4d569866027e2ff7a58d7480ed80b87738d8203feb6e518b0eb"
)

DOI = "https://doi.org/10.5281/zenodo.24021817"


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def check_file_exists(path: str, label: str) -> bool:
    if os.path.isfile(path):
        print(f"  PASS  {label} exists")
        return True
    print(f"  FAIL  {label} not found at: {path}")
    return False


def check_sha256(path: str) -> bool:
    actual = sha256_file(path)
    if actual == CANONICAL_HASH:
        print(f"  PASS  SHA-256 matches canonical hash")
        print(f"        {actual}")
        return True
    print(f"  FAIL  SHA-256 mismatch")
    print(f"        expected: {CANONICAL_HASH}")
    print(f"        actual:   {actual}")
    return False


def check_sha256sums_file(paper_path: str, sums_path: str) -> bool:
    if not os.path.isfile(sums_path):
        print(f"  SKIP  SHA256SUMS file not found (optional check)")
        return True
    actual = sha256_file(paper_path)
    with open(sums_path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(None, 1)
            if len(parts) == 2:
                hash_in_file, filename = parts
                if "EXERGYNET_WHITEPAPER_PUBLIC_V5.pdf" in filename:
                    if hash_in_file.lower() == actual.lower():
                        print(f"  PASS  SHA256SUMS entry is consistent")
                        return True
                    print(f"  FAIL  SHA256SUMS entry does not match computed hash")
                    print(f"        in file:  {hash_in_file}")
                    print(f"        computed: {actual}")
                    return False
    print(f"  SKIP  No matching entry for PDF found in SHA256SUMS")
    return True


def main() -> int:
    print("ExergyNet V5 — Publication Integrity Verification")
    print("=" * 56)
    print(f"DOI: {DOI}")
    print()

    checks = []
    checks.append(check_file_exists(PAPER_PATH, "paper/EXERGYNET_WHITEPAPER_PUBLIC_V5.pdf"))

    if checks[0]:
        checks.append(check_sha256(PAPER_PATH))
        checks.append(check_sha256sums_file(PAPER_PATH, SHA256SUMS_PATH))

    print()
    if all(checks):
        print("RESULT: ALL CHECKS PASS")
        print(f"        PDF integrity verified against canonical hash.")
        print(f"        Verify against Zenodo: {DOI}")
        return 0
    else:
        failed = sum(1 for c in checks if not c)
        print(f"RESULT: {failed} CHECK(S) FAILED")
        return 1


if __name__ == "__main__":
    sys.exit(main())
