# Getting Started

## Accessing the Paper

The V5 white paper is included in this repository at:

```
paper/EXERGYNET_WHITEPAPER_PUBLIC_V5.pdf
```

It is also available on Zenodo:
- **DOI:** https://doi.org/10.5281/zenodo.24021817
- **Zenodo record:** https://zenodo.org/records/24021817

---

## Verifying PDF Integrity

The PDF SHA-256 checksum is:
```
416974f1d7c1f4d569866027e2ff7a58d7480ed80b87738d8203feb6e518b0eb
```

### Verify on Linux/macOS:
```bash
sha256sum paper/EXERGYNET_WHITEPAPER_PUBLIC_V5.pdf
```

### Verify on Windows:
```powershell
Get-FileHash paper\EXERGYNET_WHITEPAPER_PUBLIC_V5.pdf -Algorithm SHA256
```

### Python verification script:
```bash
python scripts/verify_publication.py
```

---

## Understanding the Results

Before drawing conclusions from V5 results, review:

1. **[Benchmark Methodology](../research/benchmark-methodology.md)** — how measurements were taken
2. **[Limitations](../research/limitations.md)** — stated boundary conditions
3. **[Complexity Analysis](../research/complexity-analysis.md)** — what V5 does not claim

The key scope conditions are:
- All results are from a single development cohort run
- The 100M token figure is an estimated development operating point
- Retrieval speedup is measured against a paired naive full-state scan baseline
- Hardware efficiency results are H200 vs. A100 only
- The authority gate result is a single observed event, not a statistical claim

---

## Citing This Work

See the [Citation Guide](citation-guide.md) for citation formats.

---

## Questions

See [FAQ](faq.md) or open an issue using the [Research Question template](../.github/ISSUE_TEMPLATE/research-question.yml).
