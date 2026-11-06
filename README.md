# ExergyNet V5: Persistent Machine Infrastructure for the 100M-Token Horizon

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24021817.svg)](https://doi.org/10.5281/zenodo.24021817)

**Memory Grows. Context Does Not Have To.**

This repository is the canonical scientific reference for the ExergyNet V5 white paper.

| Field | Value |
|-------|-------|
| **Title** | Memory Grows. Context Does Not Have To. |
| **Subtitle** | ExergyNet: Persistent Machine Infrastructure for the 100M-Token Horizon |
| **Authors** | Seven Ezumba, Veena Bontu |
| **Version** | 5.0 |
| **Publication date** | November 6, 2026 |
| **DOI** | [10.5281/zenodo.24021817](https://doi.org/10.5281/zenodo.24021817) |
| **Zenodo record** | [zenodo.org/records/24021817](https://zenodo.org/records/24021817) |
| **PDF SHA-256** | `416974f1d7c1f4d569866027e2ff7a58d7480ed80b87738d8203feb6e518b0eb` |

---

## 1. Research Overview

ExergyNet is a persistent machine infrastructure architecture that decouples what
an AI agent retains across sessions (persistent memory, N) from what a model
actually reads at inference time (active context, K).

V5 characterizes the N→K relationship at a 100M-token development operating point.
It presents retrieval performance data from a live environment, examines accelerator
infrastructure behavior, and reports a live authority-layer result.

---

## 2. Problem Addressed

Standard language model deployment treats context as a resource that grows with
what the model is expected to know. As the amount of relevant prior state grows —
across sessions, agents, and time — context windows fill, forcing either truncation
or retrieval degradation.

ExergyNet addresses this by separating memory from context:

- **N** (what is stored) can grow indefinitely.
- **K** (what is delivered to the model at inference time) remains bounded by design.

At the 100M development operating point: N ≈ 101M tokens, K = 800 median tokens,
N/K ≈ 126,440. The model reasons over K, not N.

This is not a performance optimization — it is an architectural property.

---

## 3. Architectural Principles

ExergyNet is organized around four separations:

**3.1 Persistent state and active context**
Stored memory (N) and delivered context (K) are managed independently.
Growth in N does not force growth in K.

**3.2 Memory and inference**
The retrieval layer operates before inference, not during it. Relevant content
is selected from the persistent store and delivered as a bounded context window.

**3.3 Proposal and execution**
A model's output is a proposal, not a permission. Execution requires a separate
authorization step by an independent authority layer that does not participate
in model reasoning.

**3.4 Development and production characterization**
V5 results are reported against defined scope conditions. See Section 6 for
full boundary conditions.

---

## 4. Published Experimental Results

All quantitative results are reported from the V5 white paper. Each result includes
its measurement scope and applicable boundary conditions.

### 4.1 Persistent state at development scale

| Metric | Value | Scope |
|--------|-------|-------|
| Estimated state tokens (N) | ≈ 101,152,694 | Development cohort · single run |
| Holdout state tokens | ≈ 10,100,000 | Sealed holdout · separate run |
| Total matched query executions | 190 | Development cohort |
| Median active context tokens (K) | 800 | 190 matched executions |
| N/K ratio | ≈ 126,440 | Computed from median K |

### 4.2 Retrieval performance

| Metric | Value | Scope |
|--------|-------|-------|
| Median paired retrieval speedup | 220.5× | 190 matched executions |
| Mean paired retrieval speedup | 415.9× | 190 matched executions |

Retrieval speedup is measured as the ratio of time-to-relevant-context via the
ExergyNet retrieval layer versus a paired naive full-state scan on the same
hardware. The mean (415.9×) substantially exceeds the median (220.5×), indicating
a long right tail in speedup distribution.

### 4.3 Accelerator infrastructure — H200 findings

| Metric | H200 | A100 (baseline) |
|--------|------|-----------------|
| Correct-task throughput | 11.3× (vs. A100) | 1.0× (baseline) |
| Baseline answer accuracy | 45.3% (adversarial synthetic benchmark) | — |

The H200 environment demonstrated 11.3× correct-task throughput relative to the
A100 baseline at the 100M development operating point.

### 4.4 Authority layer

In a live production-adjacent environment, an adversarial instruction was submitted
to the system. The model's reasoning layer accepted the instruction and produced a
proposal to execute it. The ExergyNet authority gate evaluated the proposal and
issued a denial — the action was not executed.

This result demonstrates the authority layer's operational independence from
inference. See Section 7 and the full paper for scope conditions.

---

## 5. Benchmark Methodology

The V5 benchmark characterizes persistent state behavior at development scale using
an adversarial synthetic benchmark.

**Benchmark population:** 190 matched query executions from a single continuous
development run at the 100M-token operating point.

**Adversarial design:** The benchmark is intentionally hostile to systems without
reliable persistent context delivery. The 45.3% baseline accuracy reflects this
design — it is not a measure of general model accuracy.

**Retrieval baseline:** Paired naive full-state scan on the same hardware as the
ExergyNet retrieval layer. Speedup is measured as the ratio of retrieval latency.

**Holdout:** A separately sealed holdout of approximately 10.1M tokens was
maintained throughout. All quantitative results refer to the development cohort
unless otherwise noted.

**Hardware:** NVIDIA A100 (primary benchmark environment); NVIDIA H200 (accelerator
infrastructure characterization, separate evaluation).

The raw benchmark evidence and JSONL fixtures are not publicly released.
See `evidence/README.md` for evidence classification and availability.

---

## 6. Evidence Availability and Limitations

| Claim | Evidence classification | Availability |
|-------|------------------------|--------------|
| ≈101M state tokens | PUBLIC_DOCUMENTED | V5 white paper, Table 1 |
| 800 median active context tokens | PUBLIC_DOCUMENTED | V5 white paper, Table 1 |
| 220.5× median retrieval speedup | PUBLIC_DOCUMENTED | V5 white paper, Table 2 |
| 415.9× mean retrieval speedup | PUBLIC_DOCUMENTED | V5 white paper, Table 2 |
| 11.3× H200 throughput | PUBLIC_DOCUMENTED | V5 white paper, Table 3 |
| 45.3% baseline accuracy | PUBLIC_DOCUMENTED | V5 white paper, Table 3 |
| Authority gate live result | PUBLIC_DOCUMENTED | V5 white paper, Section 3 |
| Raw benchmark JSONL fixtures | INTERNAL_RESTRICTED | Not released |
| Production implementation source | INTERNAL_RESTRICTED | Not released |
| Retrieval algorithm internals | INTERNAL_RESTRICTED | Not released |

**Scope limitations:**
- All results are from a single development cohort run.
- Results do not generalize to arbitrary workloads, models, or infrastructure.
- The 100M token operating point is a development characterization, not a
  production specification.
- The authority gate result is a single observed event, not a statistical claim.
- ExergyNet is infrastructure — its properties depend on correct configuration.

---

## 7. Persistent Memory versus Active Context

The core N→K relationship:

```
Persistent Store (N ≈ 101M tokens)
           │
           │ Retrieval layer
           │ (before inference)
           ▼
Active Context (K = 800 median tokens)
           │
           │ Bounded window
           ▼
  Model reasoning (reads K, not N)
```

As N grows toward and beyond 100M tokens, K remains bounded at 800 median tokens
in the V5 development characterization. The retrieval layer is responsible for
selecting relevant content. This property is architectural: the system is designed
so that context delivery does not scale linearly with storage growth.

---

## 8. Scientific Publication and DOI

The canonical scientific reference is the V5 white paper, available via Zenodo:

- **DOI:** [https://doi.org/10.5281/zenodo.24021817](https://doi.org/10.5281/zenodo.24021817)
- **Zenodo record:** [https://zenodo.org/records/24021817](https://zenodo.org/records/24021817)
- **Local copy:** [`paper/EXERGYNET_WHITEPAPER_PUBLIC_V5.pdf`](paper/EXERGYNET_WHITEPAPER_PUBLIC_V5.pdf)
- **SHA-256:** `416974f1d7c1f4d569866027e2ff7a58d7480ed80b87738d8203feb6e518b0eb`

Verify the local copy:

```bash
# macOS / Linux
shasum -a 256 paper/EXERGYNET_WHITEPAPER_PUBLIC_V5.pdf

# Windows (PowerShell)
Get-FileHash paper/EXERGYNET_WHITEPAPER_PUBLIC_V5.pdf -Algorithm SHA256 | Select-Object Hash

# Or use the provided script
python scripts/verify_publication.py
```

---

## 9. Authors and Attribution

**Seven Ezumba** — Chief Architect, ExergyNet
**Veena Bontu** — Co-author, ExergyNet Research

ExergyNet is a research and infrastructure architecture by the Ezumba Dynasty
Trust (EDT).

---

## 10. Citation

### BibTeX

```bibtex
@techreport{exergynet2026v5,
  title        = {Memory Grows. Context Does Not Have To.},
  subtitle     = {ExergyNet: Persistent Machine Infrastructure for the 100M-Token Horizon},
  author       = {Ezumba, Seven and Bontu, Veena},
  institution  = {ExergyNet},
  year         = {2026},
  month        = {November},
  doi          = {10.5281/zenodo.24021817},
  url          = {https://doi.org/10.5281/zenodo.24021817},
  note         = {Development characterization at the 100M-token operating point.}
}
```

See [`docs/citation-guide.md`](docs/citation-guide.md) for additional citation
formats (APA, MLA, Chicago, ACM).

---

## 11. Intellectual Property and Licensing

Copyright © 2026 Ezumba Dynasty Trust. All rights reserved.

The V5 white paper is published for scientific reference. No additional reuse
license is granted by this repository.

Permitted without additional permission:
- Citing the paper in academic and research work (with proper attribution)
- Linking to this repository or the Zenodo record
- Quoting brief passages for commentary, criticism, or educational purposes

For all other use, contact the authors.

See [`LICENSE-STATUS.md`](LICENSE-STATUS.md) and [`COPYRIGHT.md`](COPYRIGHT.md)
for complete rights information.

---

## 12. Research Contact

For research inquiries related to the V5 paper:
- DOI record: [https://doi.org/10.5281/zenodo.24021817](https://doi.org/10.5281/zenodo.24021817)
- ExergyNet platform: [https://exergynet.org](https://exergynet.org)

For infrastructure and API access: [https://portal.exergynet.org](https://portal.exergynet.org)
