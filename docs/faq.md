# Frequently Asked Questions

---

## General

**Q: What is ExergyNet?**

ExergyNet is persistent memory infrastructure for AI systems. It addresses
the N→K problem: enabling AI agents operating at large N (persistent state
tokens) to access task-relevant context within a bounded K (active context
window).

---

**Q: What does V5 demonstrate?**

V5 characterizes ExergyNet at the 100M token development operating point.
Key results:

- N ≈ 101M estimated persistent state tokens; median K = 800 active context tokens per query
- 220.5× median retrieval speedup over naive full-state scan baseline (190 matched executions)
- 11.3× H200 correct-task throughput vs. A100 at this operating point
- Authority gate: adversarial instruction rejected in live production-adjacent environment

---

**Q: Does V5 prove that ExergyNet scales to 100M tokens for all workloads?**

No. V5 characterizes one development cohort run at the 100M development
operating point. It does not claim generalization to arbitrary workloads,
models, or infrastructure configurations.

See [Limitations](../research/limitations.md) for the full list of V5's
stated boundary conditions.

---

**Q: Is the raw benchmark data available?**

The raw benchmark fixtures, per-query measurements, and harness source code
are not publicly released. The V5 paper contains the aggregated results.
See `evidence/README.md` for the evidence classification of each claim.

---

## Technical

**Q: What does "K = 800 median" mean?**

K is the number of tokens delivered from persistent state into the active
context window per query. The V5 median is 800 tokens, measured across 190
matched query executions. Individual queries vary — 800 is the distribution
median, not a fixed value.

---

**Q: What baseline does the 220.5× speedup compare against?**

A paired naive full-state scan on the same hardware. The baseline represents
querying the entire ≈101M persistent state without a retrieval layer. It
is not a comparison against an alternative optimized retrieval system.

---

**Q: What does "correct-task throughput" mean?**

Correct-task throughput counts the number of correctly completed tasks per
unit time, not raw tokens per second. The 11.3× H200 figure measures this
metric against an A100 baseline at the 100M development operating point.

---

**Q: Does the authority gate result mean ExergyNet is secure against adversarial instructions?**

No. V5 reports a single observed event: a live gate issued DENY and the
action was not executed. This is not a statistical security guarantee.
The property holds only when the authority layer is correctly configured and
integrated. See V5 Section 3.2 and [research/limitations.md](../research/limitations.md).

---

## Repository

**Q: Why is the benchmark code not in this repository?**

The benchmark harness and raw measurement data are INTERNAL_RESTRICTED.
This repository contains the published paper, its metadata, and companion
documentation. It does not include production infrastructure source code.

---

**Q: How do I verify the PDF is authentic?**

Compute the SHA-256 of `paper/EXERGYNET_WHITEPAPER_PUBLIC_V5.pdf` and
compare against `416974f1d7c1f4d569866027e2ff7a58d7480ed80b87738d8203feb6e518b0eb`.
You can also verify against the Zenodo canonical record at
https://doi.org/10.5281/zenodo.24021817.

See `scripts/verify_publication.py` for an automated verification script.

---

**Q: What license applies to the paper?**

All rights are reserved. See `LICENSE-STATUS.md` for the current licensing
status and authorized uses.
