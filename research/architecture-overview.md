# Architecture Overview

**Source:** V5 white paper, Sections 1 and 3
**Classification:** PUBLIC_DOCUMENTED
**Status:** Reflects V5 published disclosure boundary

---

## The N→K Separation

ExergyNet is built on a single architectural principle: persistent memory (N)
and active context (K) are managed as separate concerns.

```
N — Persistent State
    What the system has stored across all sessions and time.
    At the 100M development operating point: ≈101,152,694 estimated tokens.

K — Active Context
    What is delivered to the model at inference time.
    At the 100M development operating point: 800 median tokens.

N/K ratio: ≈126,440
```

As N grows toward and beyond 100M tokens, K remains bounded at 800 median
tokens in the V5 characterization. The model reasons over K, not N.

This is an architectural property, not a performance optimization.

---

## Four Architectural Separations

V5 identifies four key separations:

### 1. Persistent state and active context

Stored memory (N) and delivered context (K) are managed independently.
The retrieval layer selects relevant content from N and delivers a bounded
K to the model before inference. Growth in N does not force growth in K.

### 2. Memory and inference

The retrieval layer selects relevant content from the persistent store
before inference, delivering a bounded context window regardless of total
storage size.

### 3. Proposal and execution

A model's output is a proposal, not a permission. The authority layer is
a separate deterministic system that evaluates proposals against policy.
Execution requires explicit authorization from the authority layer,
independent of the model's reasoning.

The authority layer does not reason — it enforces policy.

### 4. Development and production characterization

V5 results are reported against defined development cohort conditions.
They represent a characterization of behavior at the tested operating
point, not a production specification or general claim.

---

## Authority Layer Architecture

The authority layer is described in V5 Section 3:

```
Model reasoning
      │  Receives bounded context K
      │  Produces a proposal (recommended action or response)
      ↓
Authority gate
      │  Receives the proposal
      │  Evaluates against policy
      │  Issues allow or deny
      │  Independent of the reasoning that produced the proposal
      ↓
Execution
      Only authorized proposals reach execution.
      A denied proposal is never executed, regardless of model confidence.
```

### Live environment result

In a reported live production-adjacent environment:
- An adversarial instruction was submitted to the system.
- The model's reasoning layer accepted the instruction and produced a proposal.
- The authority gate evaluated the proposal and issued a denial.
- The action was not executed.

**Scope:** Single observed event. Not a statistical claim. Not a general security
guarantee. The authority layer must be correctly configured for this property
to hold.

---

## Disclosure Boundary

This document reflects the V5 public disclosure boundary. The following are
not disclosed:

- Internal retrieval algorithm implementation
- Production routing logic
- Capability registry structure
- Policy enforcement implementation details
- Internal component names, identifiers, or operational metadata

For infrastructure access, see [https://portal.exergynet.org](https://portal.exergynet.org).
