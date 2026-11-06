# Limitations

**Source:** V5 white paper, Section 4
**Classification:** PUBLIC_DOCUMENTED
**Status:** Direct from V5 published text

---

## Stated Limitations (V5 Section 4)

V5 explicitly states the following boundary conditions and limitations.

### Development cohort, single run

All quantitative results refer to a single development cohort run. The
characterization is not an average across multiple runs or deployments.
Run-to-run variation is not characterized in V5.

### Estimated token count

The ≈101M figure is an estimate. It is not an independently verified
token-by-token count.

### Adversarial synthetic benchmark

The 45.3% baseline answer accuracy is measured on a benchmark designed
specifically to test persistent-state recall failures. It is not a measure
of general model accuracy. It does not represent ExergyNet's accuracy on
general workloads.

### Paired naive scan baseline

The retrieval speedup (220.5× median) is measured against a paired naive
full-state scan on the same hardware. The baseline represents the absence
of a retrieval layer, not an optimized alternative retrieval system.
Comparisons against other retrieval approaches are not part of V5.

### Single authority gate observation

The authority layer result — adversarial instruction rejected — is a single
observed event in a specific live production-adjacent environment. It is not
a statistical claim and not a general security guarantee. The authority layer
must be correctly configured for the property to hold.

### No generalization claim

> "V5 does not claim that the results generalize to arbitrary workloads,
> models, or infrastructure configurations. The 100M token operating point
> is a development characterization, not a production specification.
> ExergyNet is infrastructure — its properties depend on correct configuration
> and integration."
> — V5, Section 4.1

### Individual query variation

K = 800 is the median across 190 matched executions. Individual queries vary.
The distribution of K across the 190 executions is not fully characterized in
V5's public disclosure.

### Hardware specificity

H200 findings are from a specific hardware configuration at the 100M operating
point. The 11.3× throughput ratio applies to correct-task throughput on the
tested workload, not to arbitrary GPU workloads.

---

## What These Limitations Mean for Reproducibility

The raw benchmark evidence (JSONL fixtures, per-query measurements, benchmark
harness source) is not publicly released. Independent reproduction of V5
results requires:

1. Equivalent or comparable persistent memory infrastructure
2. Access to comparable state at a comparable scale
3. A comparable adversarial retrieval benchmark

V5 provides the measurement results and scope conditions. It does not provide
a replication kit. Independent replication is not claimed in this repository.
