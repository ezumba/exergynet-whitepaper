# Bounded Context Model

**Source:** V5 white paper, Sections 1 and 4
**Classification:** PUBLIC_DOCUMENTED
**Status:** Reflects V5 published disclosure boundary

---

## Overview

In standard language model deployment, context grows with what the model is
expected to know. ExergyNet's bounded context model treats this as an
architectural problem, not a resource limit to be managed by truncation.

The ExergyNet retrieval layer selects relevant content from the persistent
store before inference and delivers a bounded context window (K) regardless
of total storage size (N).

---

## Measured Behavior at the 100M Operating Point

| Metric | Value | Notes |
|--------|-------|-------|
| Median active context tokens (K) | 800 | Per query, 190 matched executions |
| Persistent state (N) | ≈ 101M tokens | Development cohort |
| N/K ratio | ≈ 126,440 | Computed |

K = 800 is the median across 190 matched query executions. Individual queries
vary. The distribution is not fully reported in V5.

---

## Architectural Property vs. Performance Optimization

V5 is explicit on this distinction (Section 1.1):

> "As N grows, K stays bounded. The ExergyNet retrieval layer selects relevant
> content from the persistent store before inference, delivering a bounded
> context window regardless of total storage size. This is not a performance
> optimization — it is an architectural property."

The bounded context property means:
- The model's inference cost does not scale with total stored state.
- The model reasons only over what the retrieval layer has selected.
- The selection quality determines how relevant the delivered context is.

---

## What V5 Does Not Claim

Per V5 Section 4.1:

> "V5 does not claim that the results generalize to arbitrary workloads,
> models, or infrastructure configurations. The 100M token operating point
> is a development characterization, not a production specification."

Specifically, V5 does not claim:
- That K = 800 is a fixed limit — it is a measured median.
- That the N/K ratio of 126,440 holds at other scales.
- That bounded context delivery is proven for all query types.
- That the retrieval layer maintains this property under adversarial inputs
  beyond those tested.
