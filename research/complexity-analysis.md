# Complexity Analysis

**Source:** V5 white paper
**Classification:** PUBLIC_SUMMARY_ONLY
**Status:** Reflects V5 published disclosure boundary

---

## Important Scope Note

V5 does not contain formal computational complexity proofs. The results
in V5 are empirical characterizations at a specific development operating
point.

This document summarizes what V5 does and does not claim about scaling
behavior and complexity.

---

## What V5 Reports

V5 reports empirical measurements at the 100M development operating point:

- N ≈ 101M tokens stored; K = 800 median tokens delivered
- N/K ratio ≈ 126,440 at this operating point
- Retrieval speedup: 220.5× median over naive full-state scan baseline

These are measurements, not proofs. V5 does not prove that:
- K remains bounded at all values of N
- The N/K ratio is constant across scales
- Retrieval complexity is sublinear in the general case

---

## What V5 Does Not Claim

Per V5 Section 4.1:

> "V5 does not claim that the results generalize to arbitrary workloads,
> models, or infrastructure configurations."

Specifically not claimed:
- Universal sublinear retrieval complexity as a mathematical theorem
- Constant-K behavior across all operating points
- Proven scaling laws derived from V5 data alone

The 100M operating point is one characterized data point. Extrapolation
to other scales is not authorized by V5 findings.

---

## Prior Version Note

The V4 white paper (predecessor to V5) contained architectural complexity
descriptions that were revised for V5. The V4 descriptions are superseded
and should not be treated as current claims. The canonical current reference
is V5 (DOI: 10.5281/zenodo.24021817).
