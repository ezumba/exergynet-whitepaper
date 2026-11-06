# Benchmark Results

**Source:** V5 white paper, Tables 1–3 and Sections 2–3
**Classification:** PUBLIC_DOCUMENTED
**Status:** Direct transcription from V5 published paper

All figures below are reported exactly as published in V5. No additional
precision, adjustment, or extrapolation is applied.

---

## Table 1 — Persistent State Metrics (100M Development Operating Point)

| Metric | Value | Scope |
|--------|-------|-------|
| Estimated state tokens (N) | ≈ 101,152,694 | Development cohort · single run |
| Holdout state tokens | ≈ 10,100,000 | Sealed holdout · separate run |
| Total matched query executions | 190 | Development cohort |
| Median active context tokens (K) | 800 | 190 matched executions |
| N/K ratio | ≈ 126,440 | Computed from median K |

---

## Table 2 — Retrieval Performance (190 Matched Executions)

| Metric | Value |
|--------|-------|
| Median paired retrieval speedup | 220.5× |
| Mean paired retrieval speedup | 415.9× |
| Total matched query executions | 190 |

**Note on mean vs. median:** The mean (415.9×) substantially exceeds the median
(220.5×), indicating a long right tail in speedup distribution. Some queries
exhibit very high speedup due to query specificity; the median provides a more
conservative and representative estimate.

---

## Table 3 — H200 vs. A100 (100M Development Operating Point)

| Metric | H200 | A100 (baseline) |
|--------|------|-----------------|
| Correct-task throughput | 11.3× (vs. A100) | 1.0× (baseline) |
| Baseline answer accuracy | 45.3% (adversarial synthetic benchmark) | — |

---

## Table 4 — Scope and Boundary Conditions (from V5 Section 4)

| Claim | Scope | Boundary |
|-------|-------|----------|
| ≈101M state tokens | Development cohort · single run | Estimated; not independently counted token-by-token |
| 800 median context tokens | 190 matched query executions | Median across development cohort; individual queries vary |
| 220.5× retrieval speedup | 190 matched executions · paired | Measured vs. paired naive scan baseline; not vs. production system |
| 11.3× H200 throughput | Development operating point · correct-task | H200 vs. A100; correct-task throughput, not raw token throughput |
| 45.3% baseline accuracy | Adversarial synthetic benchmark | Designed to test persistent-state recall; not general accuracy |
| Authority gate live result | Live production-adjacent environment | Single observed event; not a statistical claim |

---

## Authority Layer Result

In a live production-adjacent environment (V5 Section 3.2):
- An adversarial instruction was submitted to the system.
- The model's reasoning layer accepted the instruction and produced a proposal.
- The ExergyNet authority gate evaluated the proposal and issued a denial.
- The action was not executed.

**Scope:** Single observed event in a specific environment. Not a statistical
claim. Not a general security guarantee.

---

## Evidence Availability

| Result | Evidence classification | Raw data |
|--------|------------------------|----------|
| ≈101M state tokens | PUBLIC_DOCUMENTED | INTERNAL_RESTRICTED |
| 800 median K | PUBLIC_DOCUMENTED | INTERNAL_RESTRICTED |
| 220.5× median speedup | PUBLIC_DOCUMENTED | INTERNAL_RESTRICTED |
| 415.9× mean speedup | PUBLIC_DOCUMENTED | INTERNAL_RESTRICTED |
| 11.3× H200 throughput | PUBLIC_DOCUMENTED | INTERNAL_RESTRICTED |
| 45.3% baseline accuracy | PUBLIC_DOCUMENTED | INTERNAL_RESTRICTED |
| Authority gate result | PUBLIC_DOCUMENTED | INTERNAL_RESTRICTED |

The raw benchmark fixtures, JSONL datasets, and per-query measurements are
not publicly released. See `evidence/README.md`.
