#!/usr/bin/env python3
"""
Validate publication metadata for the ExergyNet V5 white paper repository.

Checks:
    - CITATION.cff is parseable YAML with required fields
    - evidence/evidence-index.json is valid JSON with required fields
    - evidence/publication-provenance.json is valid JSON
    - DOI consistency across files

Usage:
    python scripts/validate_metadata.py

Exit codes:
    0 = all checks pass
    1 = one or more checks failed
"""

import json
import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EXPECTED_DOI = "10.5281/zenodo.24021817"
EXPECTED_PDF_SHA256 = (
    "416974f1d7c1f4d569866027e2ff7a58d7480ed80b87738d8203feb6e518b0eb"
)

checks_passed = []
checks_failed = []


def ok(msg: str) -> None:
    print(f"  PASS  {msg}")
    checks_passed.append(msg)


def fail(msg: str) -> None:
    print(f"  FAIL  {msg}")
    checks_failed.append(msg)


def check_citation_cff() -> None:
    path = os.path.join(REPO_ROOT, "CITATION.cff")
    if not os.path.isfile(path):
        fail("CITATION.cff not found")
        return
    ok("CITATION.cff exists")

    try:
        import yaml
    except ImportError:
        print("  SKIP  PyYAML not installed — skipping CITATION.cff parse check")
        print("        Install with: pip install pyyaml")
        return

    with open(path) as f:
        data = yaml.safe_load(f)

    required = ["cff-version", "title", "version", "doi", "authors"]
    for field in required:
        if field in data:
            ok(f"CITATION.cff has required field: {field}")
        else:
            fail(f"CITATION.cff missing required field: {field}")

    if "doi" in data:
        doi = str(data["doi"])
        if EXPECTED_DOI in doi:
            ok(f"CITATION.cff DOI matches expected: {EXPECTED_DOI}")
        else:
            fail(f"CITATION.cff DOI mismatch: got '{doi}', expected '{EXPECTED_DOI}'")


def check_evidence_index() -> None:
    path = os.path.join(REPO_ROOT, "evidence", "evidence-index.json")
    if not os.path.isfile(path):
        fail("evidence/evidence-index.json not found")
        return
    ok("evidence/evidence-index.json exists")

    with open(path) as f:
        data = json.load(f)
    ok("evidence/evidence-index.json is valid JSON")

    for field in ["schema_version", "doi", "pdf_sha256", "entries"]:
        if field in data:
            ok(f"evidence-index.json has required field: {field}")
        else:
            fail(f"evidence-index.json missing required field: {field}")

    if "doi" in data:
        if EXPECTED_DOI in str(data["doi"]):
            ok("evidence-index.json DOI matches expected")
        else:
            fail(f"evidence-index.json DOI mismatch: {data['doi']}")

    if "pdf_sha256" in data:
        if data["pdf_sha256"].lower() == EXPECTED_PDF_SHA256.lower():
            ok("evidence-index.json PDF SHA-256 matches expected")
        else:
            fail(f"evidence-index.json PDF SHA-256 mismatch")

    if "entries" in data and isinstance(data["entries"], list):
        ok(f"evidence-index.json has {len(data['entries'])} evidence entries")


def check_publication_provenance() -> None:
    path = os.path.join(REPO_ROOT, "evidence", "publication-provenance.json")
    if not os.path.isfile(path):
        fail("evidence/publication-provenance.json not found")
        return
    ok("evidence/publication-provenance.json exists")

    with open(path) as f:
        data = json.load(f)
    ok("evidence/publication-provenance.json is valid JSON")

    if "doi" in data:
        if EXPECTED_DOI in str(data["doi"]):
            ok("publication-provenance.json DOI matches expected")
        else:
            fail(f"publication-provenance.json DOI mismatch: {data['doi']}")

    if "sha256" in data:
        if data["sha256"].lower() == EXPECTED_PDF_SHA256.lower():
            ok("publication-provenance.json PDF SHA-256 matches expected")
        else:
            fail("publication-provenance.json PDF SHA-256 mismatch")


def check_paper_sha256sums() -> None:
    path = os.path.join(REPO_ROOT, "paper", "SHA256SUMS")
    if not os.path.isfile(path):
        fail("paper/SHA256SUMS not found")
        return
    ok("paper/SHA256SUMS exists")

    with open(path) as f:
        content = f.read()
    if EXPECTED_PDF_SHA256 in content:
        ok("paper/SHA256SUMS contains expected PDF hash")
    else:
        fail("paper/SHA256SUMS does not contain expected PDF hash")


def main() -> int:
    print("ExergyNet V5 — Metadata Validation")
    print("=" * 44)
    print()

    print("CITATION.cff")
    check_citation_cff()
    print()

    print("Evidence Index")
    check_evidence_index()
    print()

    print("Publication Provenance")
    check_publication_provenance()
    print()

    print("Paper SHA256SUMS")
    check_paper_sha256sums()
    print()

    total = len(checks_passed) + len(checks_failed)
    if not checks_failed:
        print(f"RESULT: ALL {total} CHECKS PASS")
        return 0
    else:
        print(
            f"RESULT: {len(checks_failed)} of {total} CHECK(S) FAILED"
        )
        for msg in checks_failed:
            print(f"        FAIL: {msg}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
