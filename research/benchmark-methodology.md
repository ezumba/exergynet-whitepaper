# Benchmark Methodology

**Source:** V5 white paper, Sections 2 and 4
**Classification:** PUBLIC_DOCUMENTED
**Status:** Reflects V5 published disclosure boundary

---

## Overview

V5 uses an adversarial synthetic benchmark to characterize ExergyNet's
behavior at the 100M-token development operating point. The benchmark is
designed to test persistent-state recall failures — it is intentionally
hostile to systems without reliable persistent context delivery.

---

## Benchmark Population

| Parameter | Value |
|-----------|-------|
| Development cohort | Single continuous run |
| Estimated state tokens at characterization | ≈ 101,152,694 |
| Total matched query executions | 190 |
| Sealed holdout | ≈ 10,100,000 tokens (separate run, not included in figures) |

All reported quantitative results refer to the 190 matched executions from the
development cohort unless noted otherwise.

---

## Retrieval Measurement

Retrieval speedup is measured as a **paired comparison**: for each of the 190
matched query executions, the time to locate and deliver relevant context via
the ExergyNet retrieval layer is compared to the time for a naive full-state
scan on the same hardware.

This measures time-to-relevant-context, not total inference time.

**Baseline definition:** Naive full-state scan on the same hardware as the
ExergyNet retrieval layer. The baseline does not represent an optimized
retrieval system; it represents the absence of a retrieval layer.

---

## Accelerator Comparison

The H200 characterization (11.3× correct-task throughput vs. A100) uses
**correct-task throughput** as the metric, not raw token throughput.

Correct-task throughput counts tasks completed correctly per unit time,
not tokens generated. This metric reflects the combined effect of hardware
capability and ExergyNet's bounded context delivery at the tested operating
point.

The H200 and A100 evaluations were conducted at the same 100M development
operating point.

---

## Benchmark Design — Adversarial Synthetic

The 45.3% baseline answer accuracy is measured on an adversarial synthetic
benchmark designed to probe persistent-state recall failures:

> "It does not represent general model accuracy. The benchmark is intentionally
> hostile to systems without reliable persistent context delivery."
> — V5, Section 2.3

**What 45.3% means:** 45.3% of benchmark questions were answered correctly by
the system using the delivered bounded context window. This figure is relative
to the specific adversarial benchmark, not to general language model performance.

---

## What Is Not Disclosed

- Raw benchmark JSONL fixtures or query datasets
- Internal construction methodology (chunk types, query class distribution)
- Per-query breakdown or class-level accuracy
- Retrieval algorithm implementation

The benchmark design methodology is not disclosed to prevent benchmark
contamination. See `evidence/README.md` for evidence classification.

---

## Scope Conditions

| Claim | Applies to |
|-------|-----------|
| ≈101M state tokens | Development cohort · single run · estimated |
| 800 median context tokens | 190 matched executions |
| 220.5× median retrieval speedup | 190 matched executions · paired measurement |
| 11.3× H200 throughput | Development operating point · correct-task metric |
| 45.3% baseline accuracy | Adversarial synthetic benchmark |

These results characterize a specific environment at a specific time. They do
not constitute general performance claims for ExergyNet infrastructure.
