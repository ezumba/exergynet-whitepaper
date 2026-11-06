# Terminology

Key terms used in the ExergyNet V5 white paper.

---

## Core Terms

**N**
Total estimated persistent state tokens. The full token count stored in
the ExergyNet persistent memory layer. At the V5 100M development operating
point, N ≈ 101,152,694 (estimated).

**K**
Active context tokens delivered per query. The number of tokens retrieved
from persistent state and placed into the AI agent's active context window
for a given query. V5 median K = 800 tokens across 190 matched executions.

**N/K Ratio**
The ratio of total persistent state tokens to active context tokens per query.
At the V5 100M operating point, N/K ≈ 126,440. This is a development
characterization of the separation achieved; it is not a constant across all
operating points or workloads.

**Bounded Active Context**
The active portion of the AI agent's working context — bounded by the
context window constraint K. ExergyNet manages what is placed into this
window from the full persistent state N.

**Persistent State**
The complete accumulated state stored by ExergyNet across interactions.
N represents the size of this state.

**Persistent Memory Interface**
The retrieval layer that mediates access between the AI agent's active
context and the persistent state. It enforces the governed retrieval
boundary.

**Governed Retrieval Boundary**
The authority-enforced boundary around retrieval operations. Access to
persistent state passes through the authority gate before being delivered
to the active context.

**Authority Gate**
The ExergyNet component that evaluates whether a proposed retrieval or
action should be authorized. In V5, the gate issued DENY in one observed
live production-adjacent event (see §3.2 and [limitations.md](../research/limitations.md)).

---

## Measurement Terms

**Adversarial Synthetic Benchmark**
The benchmark used for V5 accuracy and throughput measurements. Specifically
designed to surface persistent-state recall failures. Not a measure of
general model accuracy.

**Paired Naive Scan Baseline**
The comparison condition for retrieval speedup measurements. A naive
full-state scan (querying all N tokens without a retrieval layer) on the
same hardware, paired against each query. The 220.5× speedup is relative
to this baseline.

**Correct-Task Throughput**
The number of correctly completed tasks per unit time. The metric used
for the H200 vs. A100 comparison (11.3×). Different from raw token
throughput.

**Development Cohort**
The specific run from which V5 results are drawn. Single cohort, single
run. All quantitative results refer to this cohort unless otherwise stated.

**Development Operating Point**
The 100M token scale at which V5 was characterized. This is a development
characterization, not a production specification.

---

## Architecture Terms

**ExergyNet**
Persistent memory infrastructure for AI systems. The subject of the V5
white paper.

**xLMP**
The ExergyNet persistent-state layer behind the V5 research results.

**LNES-13**
ExergyNet subsystem number 13. LNES subsystem identifiers are internal
references. LNES-13 is referenced in the V5 architecture context; its
implementation details are INTERNAL_RESTRICTED.

**V5**
Version 5 of the ExergyNet white paper (DOI: `10.5281/zenodo.24021817`).
The current canonical public disclosure. Supersedes V4.

---

## Repository Terms

**PUBLIC_DOCUMENTED**
Evidence class: published in V5 with supporting data in the paper.

**PUBLIC_INDEPENDENTLY_VERIFIABLE**
Evidence class: verifiable by third parties without access to ExergyNet
infrastructure (e.g., PDF SHA-256 against Zenodo record).

**INTERNAL_RESTRICTED**
Evidence class: evidence exists but is not authorized for public release.

**INTERNAL_RESTRICTED** (applied to source)
Source material that is not publicly disclosed, including raw benchmark
fixtures, per-query measurement data, and production source code.
