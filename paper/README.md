# paper/

This directory contains the canonical published V5 white paper.

| File | Description |
|------|-------------|
| `EXERGYNET_WHITEPAPER_PUBLIC_V5.pdf` | V5 white paper (8 pages) |
| `EXERGYNET_WHITEPAPER_PUBLIC_V5.sha256` | SHA-256 checksum |
| `SHA256SUMS` | Verified hash manifest |

---

## Integrity Verification

**SHA-256:** `416974f1d7c1f4d569866027e2ff7a58d7480ed80b87738d8203feb6e518b0eb`

```bash
# macOS / Linux
shasum -a 256 EXERGYNET_WHITEPAPER_PUBLIC_V5.pdf

# Windows (PowerShell)
Get-FileHash EXERGYNET_WHITEPAPER_PUBLIC_V5.pdf -Algorithm SHA256 | Select-Object Hash
```

The expected output is:
```
416974f1d7c1f4d569866027e2ff7a58d7480ed80b87738d8203feb6e518b0eb
```

---

## Canonical Record

The authoritative record for this paper is the Zenodo deposit:

**DOI:** [https://doi.org/10.5281/zenodo.24021817](https://doi.org/10.5281/zenodo.24021817)

If the hash of this file does not match the expected value above, obtain the
canonical copy from Zenodo and report the discrepancy per SECURITY.md.
