---
id: EXP-2026-006
title: "Measured verdict signing in an AVF protected VM"
related_entry: FBR-2026-001
status: queued
priority: "P3 (61–90 days)"
created_date: 2026-11-22
acceptance_criteria_defined: true
run_started: ""
run_completed: ""
environment: isolated / non-production (required)
---

# Experiment: Measured verdict signing in an AVF protected VM

**Acceptance criteria are defined below, before any run.** Never execute untrusted source code on production infrastructure, data, credentials or networks. Use an isolated test handset with no personal accounts.

## Hypothesis

Label: HYPOTHESIS. Running the verdict signer in Microdroid yields code provenance (vmComponents codeHash) in addition to device provenance.

## Environment

- Pixel (Tensor) first; then the REDMAGIC if a protected VM is available
- MANAGE_VIRTUAL_MACHINE granted via adb for development only

## Acceptance criteria

1. [ ] The pVM obtains an RKP-backed chain with extension OID 1.3.6.1.4.1.11129.2.1.29.1.
2. [ ] The codeHash matches the FR3K-built payload.
3. [ ] The off-device checker accepts the verdict, and rejects it after a one-byte payload change (10/10).
4. [ ] The REDMAGIC result (supported, unsupported or UNKNOWN) is recorded with system property evidence.

## Method

CPU-only small model inside the pVM; NPU access from the pVM is not expected (ASSUMPTION).

## Results

Not run.

## Outcome

- Pass / fail against acceptance criteria: not run
