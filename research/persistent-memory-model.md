# Persistent Memory Model

**Source:** V5 white paper, Section 1–2
**Classification:** PUBLIC_DOCUMENTED
**Status:** Reflects V5 published disclosure boundary

---

## Overview

ExergyNet's persistent memory model stores state across sessions without
requiring that state to fit within a model's context window. The key
characteristic is that stored state (N) and delivered context (K) scale
independently.

---

## State at the 100M Development Operating Point

V5 characterizes persistent state at approximately 101 million estimated
state tokens:

| Metric | Value | Scope |
|--------|-------|-------|
| Estimated state tokens (N) | ≈ 101,152,694 | Development cohort · single run |
| Holdout state tokens | ≈ 10,100,000 | Sealed holdout · separate run |
| Total matched query executions | 190 | Development cohort |
| Median active context tokens (K) | 800 | 190 matched executions |
| N/K ratio | ≈ 126,440 | Computed from median K |

The 100M operating point represents a single continuous development run.
The separately sealed holdout (≈10.1M tokens) was maintained throughout and
is not included in these figures.

---

## The N→K Relationship

The core relationship is that K does not grow as N grows. This is an
architectural constraint — the retrieval layer is designed to select and
deliver a bounded context regardless of total storage size.

At 101M state tokens and 800 median context tokens, the ratio N/K ≈ 126,440.
The model at inference time reads 1 token for every 126,440 stored tokens,
approximately.

V5 does not claim that this ratio holds at operating points not characterized.
The 100M result is a development characterization, not a proven universal bound.

---

## What Persistent State Contains

V5 (Section 2.1) describes the persistent store at the development operating
point as containing:

> "structured state, identity records, evidence shards, and query history
> from 190 matched query executions."

The specific internal representation of these content types is not disclosed.

---

## Limitations

- All figures are from a single development cohort run.
- "Estimated state tokens" reflects an approximation method, not a
  token-by-token count.
- Results do not generalize to arbitrary state content, query distributions,
  or infrastructure configurations.
- The separately sealed holdout (10.1M tokens) is reported for completeness;
  all quantitative performance claims refer to the development cohort.
