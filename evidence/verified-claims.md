# Verified Public Claims — ExergyNet V5

This document summarizes the claims made in the V5 white paper and their
evidence classification under the public disclosure boundary.

All claims originate from V5 (DOI: `10.5281/zenodo.24021817`).

---

## Classification Key

| Symbol | Meaning |
|--------|---------|
| ✓ PUBLIC_DOCUMENTED | Published in V5 with supporting data in the paper |
| ✓✓ PUBLIC_INDEPENDENTLY_VERIFIABLE | Verifiable by third parties without access to infrastructure |
| ~ PUBLIC_SUMMARY_ONLY | Summary public; raw evidence not released |
| ✗ INTERNAL_RESTRICTED | Not released |

---

## State Scale Claims

| Claim | Value | Classification |
|-------|-------|----------------|
| Estimated persistent state tokens (N) | ≈ 101,152,694 | ✓ PUBLIC_DOCUMENTED |
| Sealed holdout state tokens | ≈ 10,100,000 | ✓ PUBLIC_DOCUMENTED |
| Total matched query executions | 190 | ✓ PUBLIC_DOCUMENTED |
| Median active context tokens per query (K) | 800 | ✓ PUBLIC_DOCUMENTED |
| N/K ratio at 100M operating point | ≈ 126,440 | ✓ PUBLIC_DOCUMENTED |

**Raw data status:** INTERNAL_RESTRICTED. The measurements above are
published in V5. The underlying per-query logs are not released.

---

## Retrieval Performance Claims

| Claim | Value | Classification |
|-------|-------|----------------|
| Median paired retrieval speedup | 220.5× | ✓ PUBLIC_DOCUMENTED |
| Mean paired retrieval speedup | 415.9× | ✓ PUBLIC_DOCUMENTED |

**Baseline:** Paired naive full-state scan on the same hardware.
**Scope:** 190 matched query executions, development cohort, single run.

---

## Hardware Efficiency Claims

| Claim | Value | Classification |
|-------|-------|----------------|
| H200 correct-task throughput vs. A100 | 11.3× | ✓ PUBLIC_DOCUMENTED |
| Baseline answer accuracy (adversarial benchmark) | 45.3% | ✓ PUBLIC_DOCUMENTED |

**Scope:** 100M development operating point. H200 vs. A100 only.
Correct-task throughput metric — not raw token throughput.

---

## Authority Layer Claim

| Claim | Result | Classification |
|-------|--------|----------------|
| Adversarial instruction to live gate | DENY issued; action not executed | ✓ PUBLIC_DOCUMENTED |

**Scope:** Single observed event in live production-adjacent environment.
Not a statistical claim. Not a general security guarantee.

---

## Artifact Integrity

| Artifact | Hash | Classification |
|----------|------|----------------|
| EXERGYNET_WHITEPAPER_PUBLIC_V5.pdf | `416974f1...` (SHA-256) | ✓✓ PUBLIC_INDEPENDENTLY_VERIFIABLE |

Verifiable against Zenodo record: https://doi.org/10.5281/zenodo.24021817

---

## Claims Not Made in V5

The following are explicitly **not** claimed by V5:

- Formal proof that K is bounded for all values of N
- Formal proof that retrieval is sublinear in the general case
- Generalization to arbitrary workloads, models, or infrastructure
- Independent reproducibility without equivalent infrastructure
- Production performance specification (100M is a development characterization)
- Statistical security guarantee for the authority gate
