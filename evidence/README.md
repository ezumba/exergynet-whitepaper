# evidence/

This directory contains evidence provenance records for the V5 white paper claims.

---

## Evidence Classification

| Class | Meaning |
|-------|---------|
| `PUBLIC_DOCUMENTED` | Claim is published in the V5 paper with supporting data in the paper itself |
| `PUBLIC_INDEPENDENTLY_VERIFIABLE` | Claim can be verified by third parties using publicly available methods |
| `PUBLIC_SUMMARY_ONLY` | Summary or conclusion is public; supporting raw data is not released |
| `INTERNAL_RESTRICTED` | Evidence exists but is not authorized for public release |
| `NOT_VERIFIED` | Claim status is unresolved |

---

## Files in This Directory

| File | Description |
|------|-------------|
| `evidence-index.json` | Machine-readable index of all V5 evidence entries |
| `publication-provenance.json` | Provenance record for the V5 PDF publication |
| `verified-claims.md` | Human-readable summary of verified public claims |

---

## What Is and Is Not Released

**Released in this repository:**
- The V5 white paper PDF (`paper/EXERGYNET_WHITEPAPER_PUBLIC_V5.pdf`)
- The PDF SHA-256 checksum
- Provenance metadata for the Zenodo publication
- Evidence classification for all V5 claims

**Not released:**
- Raw benchmark JSONL fixtures
- Per-query measurement data
- Benchmark harness source code
- Internal operational logs
- Hardware configuration details beyond what appears in V5

---

## Verification

The PDF SHA-256 (`416974f1...`) is independently verifiable against the Zenodo
record at [https://doi.org/10.5281/zenodo.24021817](https://doi.org/10.5281/zenodo.24021817).

This is the only V5 claim that is `PUBLIC_INDEPENDENTLY_VERIFIABLE` without
access to the original infrastructure.
